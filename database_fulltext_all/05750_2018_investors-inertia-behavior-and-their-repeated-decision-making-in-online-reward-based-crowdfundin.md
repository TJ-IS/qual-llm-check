---
otero_id: 5750
otero_key: "HDPFJS2E"
title: "Investors' inertia behavior and their repeated decision-making in online reward-based crowdfunding market"
authors: "Shengsheng Xiao; Qing Yue"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.05.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Investors' inertia behavior and their repeated decision-making in online reward-based crowdfunding market

![](/api/attachments/HDPFJS2E/fulltext/images/b3f1734a523d6257414b0a5f6737ca8267ad2ba34186cf2ab5237f2b48394dc4.jpg)

Shengsheng Xiao, Qing Yue

<table><tr><td>PII:</td><td>S0167-9236(18)30088-5</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.05.005</td></tr><tr><td>Reference:</td><td>DECSUP 12956</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>23 October 2017</td></tr><tr><td>Revised date:</td><td>30 May 2018</td></tr><tr><td>Accepted date:</td><td>30 May 2018</td></tr></table>

Please cite this article as: Shengsheng Xiao, Qing Yue , Investors' inertia behavior and their repeated decision-making in online reward-based crowdfunding market. Decsup (2017), doi:10.1016/j.dss.2018.05.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Investors’ Inertia Behavior and Their Repeated Decision-Making in Online Reward-based Crowdfunding Market

Shengsheng Xiao\*

Department of Management Information Systems Shanghai University of Finance and Economics Shanghai, China 200433 xiao.shengsheng@shufe.edu.cn

Qing Yue

Department of Business Management and Economics Shanghai University of International Business and Economics Shanghai, China 201620 yueqing@suibe.edu.cn

May 30, 2018

\* Corresponding author: Shengsheng Xiao; Email: xiao.shengsheng@shufe.edu.cn;

Tel: +86-021-65901447; Fax: +86-021-65901447

A research paper revised and resubmitted to Decision Support Systems (DSS)

# Investors’ Inertia Behavior and Their Repeated Decision-Making in Online Reward-based Crowdfunding Market

## Abstract

Extending recent work on individual-level decision in the emerged reward-based crowdfunding market, we formulated a Panel Vector Auto Regression Model with exogenous variables to examine whether investors’ Inertia Behavior (IB) exists in their repeated investment decisions (i.e., which reward tier to select and when to invest). If so, how to quantify the effect of this behavior and how investors’ heterogeneity moderates the effect of this behavior. We collected a novel and individual-level dataset from a leading crowdfunding market. Our analysis suggests the existence of investors’ IB. Furthermore, we also found that (1) Investors’ IB in reward tier selection seems to be stronger than that in investment timing selection. (2) Investors’ platform tenure significantly accentuates their IB reward tier selection, but weakens that in investment timing selection. (3) Project attributes related factors have different impacts on investors’ decision-making and peer investors’ influence have stronger impact on backers’ investment timing selection when compared with fundraisers’ fundraisers and the crowdfunding intermediaries hosting them.

Keywords: Crowdfunding; Inertia Behavior; Dynamic Repeated Investments; Investment Decision; Reward Tier Selection

# ACCEPTED MANUSCRIPT

## 1. Introduction

Online crowdfunding market has recently emerged as a novel venture finance model for sourcing capital to support individual or entrepreneurial ideas or ventures [31, 33]. It is defined as “a collective effort by people who network and pool their money together, usually via the internet, in order to invest in and support efforts initiated by other people or organizations [30]” and has experienced a tremendous increase. A report from the World Bank pointed out that the market size of crowdfunding will reach \$90 billion by 2020. <sup>1</sup> The explosive growth and prospective value of crowdfunding market have attracted attentions from both practitioners and researchers.

Compared with traditional finance markets (e.g., stock market), there are some unique operation mechanisms and characteristics in online crowdfunding market. First, in online crowdfunding market, the fundraising target and duration of each project are predetermined by fundraisers. Investors are only allowed to support a project within its active period and fundraisers are usually permitted to take away the money when their fundraising targets are reached. Second, investors’ detailed investment information (e.g., investors’ identities, time, amount and so on) are visible and traceable in online crowdfunding market, which implies that prior investors’ investment decisions are usually available for the later investors. Third, in online crowdfunding market, fundraisers are allowed to conduct marketing activities (e.g., providing project updates and comment conversations) to promote their projects and improve their fundraising performances. Therefore, it is expected that investors participating in crowdfunding might exhibit different behavior from traditional investors in the financial markets. However, previous studies on investors’ behavior mainly focused on the traditional finance markets [14] and existing studies on crowdfunding mainly concentrated on investigating factors that affect projects’ crowdfunding performances and backers’ aggregated investment decision from the perspective of fundraiser, backers and crowdfunding projects [11, 36, 29, 2, 23]. Research on the decision of individual investor in the emerging crowdfunding market is relatively limited.

In addition, if we want to culture a better crowdfunding market, it is very necessary for fundraisers,

# ACCEPTED MANUSCRIPT

crowdfunding platform and even government legislators to well understand individual investor’s decision making behavior in this new market. In this study, we conducted an in-depth analysis of investors’ possible Inertia Behavior (IB) in the reward-based crowdfunding market. In physics, inertia refers to an object’s “amount of resistance to change in velocity.” In social science, IB is a kind of behavioral patterns that individual usually repeat most. It is usually found in individual’s repeated activities. In our research context, investors’ potential IB refers to the possible positive temporal correlation among their repeated investment decisions (i.e., reward tier and investment timing selection). To well explore this possible behavior, we designed the following research questions: (1) Does IB exist in backer’s investment decisions making (i.e., which reward tier to select and when to invest)? (2) If so, how to formulate a model to simultaneously quantify the effect of this behavior? (3) How to tease out its effect from other cofounders? And (4) how does investors’ heterogeneity (e.g., platform tenure) moderate the effect of their IB and other factors?

To answer those questions, we first formulated a Panel Vector Auto Regression (PVAR) model with exogenous variables to examine the existence of investor’s IB. We then interpreted the moderating effect of investors’ platform tenure on the identified behavior and other confounders. Finally, we estimated the proposed empirical model based on a unique and individual-level panel data and the estimation results suggest the following main findings: (1) Investors’ IB does exist in both their reward tier selection and investment timing selection decisions. (2) Investors’ IB in choosing reward tier seems to be stronger than that in choosing investment timing. (3) Investors’ platform tenure significantly accentuates their IB in reward tier selection, but weakens that in investment timing selection. In addition, (4) Project attributes related factors have different impacts on investors’ decision-making and peer investors’ average investment amount seems to have stronger impact on their investment timing selection when compared with fundraisers’ marketing related factors. This study advances our understanding of individual backer’s repeated investment decision behavior in online reward-based crowdfunding market and contributes to the literature in three ways.

First, we contribute to the emerging crowdfunding literature by examining investors’ IB in their repeated reward tier and investment timing selection decisions. Although crowdfunding has attracted much attention from academia in recent years, previous studies—with only rare exceptions [21, 38, 10]—mainly focused on the determinants of successful crowdfunding projects. Our study focused on individual-level IB in their repeated investments. We verified the existence of this behavior, quantified its effect and interpreted its interaction role with other factors. To the best of our knowledge, this is our original contribution. We answered the call for studies that stress the importance of tracking and unraveling individual backers’ investment behavior in the online crowdfunding market [10].

Second, we make contributions to the literature of behavioral finance by examining investor’s decision making behavior in the emerging online crowdfunding market. Existing studies on investors behavior mainly stay in traditional finance market. Because of the unique characteristics of the crowdfunding market, it is expected that investors would exhibit very different behaviors. A closer examination of the behavior of the investors in the crowdfunding market may contribute to behavioral finance by advancing our understanding of investors’ decision making mechanisms.

Third, we also make theoretical contributions from a methodological point of view. We formulated a Panel Vector Auto Regression (PVAR) model with exogenous variables in this paper. It is able to capture the simultaneous mutual influences of backers’ reward tier selection and investment timing selection decision without imposing ad hoc model restrictions. It can also explicitly account for the estimation biases in our regression system caused by endogeneity, omitted variables, autocorrelations [25, 26], and visualize the dynamic relationships among dependent variables, as well as their lagged variables through impulse and response analysis. To obtain consistent and efficient estimation results, we estimated the proposed PVAR model in a Generalized Method of Moments (GMM) framework by constructing instruments based on the lagged dependent variables and many exogenous variables.

The remainder of this study is organized as follows. We first review related literature in Section 2, and then describe our research context, data and variables in Section 3. We formulate the model and conduct the empirical analysis in Section 4. In Section 5, the moderating role of investors’ heterogeneous platform tenure is interpreted. We provide our robustness checks in Section 6, and discuss our findings,

limitations and managerial implications in Section 7.

## 2. Literature Review

In this section, we are going to review related literature from online crowdfunding, behavioral finance and Panel VAR model to justify our research motivations and contributions.

## 2.1 Online Crowdfunding

Crowdfunding is an emerging viable alternative for raising capital from the “crowd” to support innovative, entrepreneurial ideas and ventures [32] and has received much attention from academic in recent years. Kuppuswamy and Bayus (2014) divided crowdfunding projects into four types: reward-based, equity-based, lending-based, and donation-based crowdfunding platforms [21]. Our study concentrates on reward-based crowdfunding market. Extant studies in this area mainly focus on project-level determinants of projects achieving good crowdfunding performance (e.g., successful projects) [11, 36, 29, 21, 2, 23]. They found that listed project features in the online platform, fundraiser’s social capital and marketing efforts will significantly influence projects’ crowdfunding performances. Furthermore, they noted that, prior support/investment, especially the initial support, are very important to the success of projects in the reward-based crowdfunding market [11, 21, 22], and the text information are good indicators for fraudulent behavior detection and project success prediction on crowdfunding platforms [28, 37].

reward-based crowdfunding market, researches on individual-level investment decisions are relatively limited. Burtch et al. (2015) conducted a randomized field experiment and found that controlling public investment information reduces backers’ investment amount, but increases their propensity to engage with the crowdfunding platform [10]. Wessel et al. (2016) examined the effects of fake social information on consumer decision-making in the context of crowdfunding [35].

Our study complements to this stream of literature by looking into the IB of investors based on their repeated investments. Different from existed studies, we decompose individual’s investment action into two simultaneous and related decisions: reward tier selection and investment timing selection, and examine them based on an individual-level panel data. We believe this is the first work that investigates the impact of backers’ IB based on their repeated investments in online crowdfunding market.

## 2.2 Behavioral Finance and Investment Decision

Our study is also related to the behavior finance literature by interpreting investors’ dynamic behavior in an emerging fundraising market (e.g., online crowdfunding market) with rich observable information. Studies in the area of behavioral finance usually attempt to explain the psychological and emotional factors in traditional financial market (e.g., stock market), as well as their impact on the behavior of investors and market efficiency [6, 14]. They are able to provide detailed pictures on how investors actually behave and how they differ from one another when making investment decision under the same circumstance. For example, Grinblatt and Keloharju (2000) identified different investment behaviors and performances of foreign investors and Finland investors by using a unique investment data from Finland [17]. Generally speaking, extant behavioral factors that influence investment decisions can be widely divided into two categories. The first one refers t ctors that are relevant to investors’ psychology and emotion such as optimism [33], overconfidence [27], bounded rationality [3], and home bias [23]. The second one refers to those circumstances related factors such as peer influence [15], observation learning from investment signals [20] and media attention [19].

Considering the special context of online crowdfunding market, at least three behavior related factors in our study should be pointed out here: investor’s inertia behavior, peer influence and fundraisers’ marketing related factors. Inertia behavior, an interesting factor belonging to the first category mentioned above, usually refers to a behavioral pattern that individual usually repeat most. It can be explained by the fact that “Individuals who have experienced an event in the past are more likely to experience the event in the future than individuals who have not experienced the event” [18]. Similar behavior pattern may exist in backers’ repeated investments in crowdfunding market. However, it has not been explored yet. Peer influence and fundraisers’ marketing related factors belong to the second category mentioned above. The increasing digital visibility of online crowdfunding market grants investors greater access to information about their peer investors [10], peer influence (i.e., investment decisions from peer investors)

is a very important factor in affecting individual’s decision-making. Furthermore, to improve project’s crowdfunding performances, fundraisers usually update their fundraising progress, and actively participate in the comment conversations. Those can be treated as fundraisers’ marketing activities, and they also have been proved to have impact on backers’ investment decisions [21].

Because of data limitation, a simultaneous analysis of the impact of investors’ psychology/action related factors and investment scenario related factors in previous behavioral finance studies seem to be limited. The emerging online crowdfunding market provides us a good chance and rich data to do this. Complementing to the stream of behavioral finance literature, our study examin investors’ IB in their reward tire and investment timing selection in the emerging crowdfunding market.

## 2.3 Panel VAR Model

Third, this study also relates to the emerging literature employing and developing Panel Vector Auto Regression (PVAR) model. As a variant of the VAR model, the PVAR model has been increasingly used in many studies. For example, Chen et al. (2015) employed a PVAR model to investigate the interrelationship between broadcasting promotions in social media and music sales [12]. Ferdinand et al. (2016) used a PVAR model to examine the dynamic effects of online social interactions on backers’ funding decisions [34]. Chung et al., (2016) empirically studied the relationship between users’ dynamic engagements, friends’ engagements, and social network size on Facebook [13]. Generally speaking, PVAR models are employed to study the relationships between a system of interdependent variables without any ad hoc restrictions on the model [1]. Its strengths come from the benefits of the VAR models and the used panel data set. In a VAR model, main variables are treated as endogenous and interdependent [25], the bidirectional relationship between any two endogenous variables can be inferred through Granger causality test, and their dynamic influences can also be examined by conducting impulse response analysis (to be discussed in Section 4.4). The availability of panel data set enables us to control for individual’s unobserved heterogeneity and construct useful instruments based on the lagged dependent variables to obtain consistent estimation results.

Since investors’ reward tier selection and investment timing selection are usually two interactional and simultaneous decisions, we formulated and estimated a PVAR model with exogenous variables, as well as unobserved fixed individual effects in this study. In the model, backers’ reward tier selection and investment timing selection decisions are interpreted by their past selection decisions and many other exogenous variables. It is able to capture the complex dynamic relationships between investors’ focal investment decisions and lagged investment decisions and can be estimated through GMM estimation.

## 3. Study Context, Data Set and Variables

## 3.1 Study Context and Data Set

The data set leveraged for this study comes from a leading reward-based crowdfunding platform in China named Zhongchou.com (hereafter we use Zhongchou). It was founded in Beijing in February 2013 and has developed into one of the largest reward-based crowdfunding platforms in China. Similar to Kickstarter, Zhongchou provides detailed information about crowdfunding projects and their real-time performances. The project information includes fundraising goal, duration, and project description and introduction. The project's real-time performance information includes project pledge amount, the percentage ratio of pledge over goal, the number of investors, the remaining days before deadline, the number of project updates and the number of comment conversations in the online community. A screen shot of a project on this platform can be found in Figure 1. Note that it is very easy and convenient for a potential investor to calculate the average investment amount from the peer investors, know the number of updates and comments for the listed project at any time based on the provided information.

Our data contains observations on Zhongchou from December 2013 to August 2015. In our data set, we observe both project attributes and individual backer’s investment histories. For each crowdfunding project, we know its static information like the projects’ released time, fundraising target, duration, project description, reward tiers and so on. We also know its dynamic information like daily #investors, pledge amount, cumulative pledge amount and backers, #update and #comment from the fundraisers. For each unique investor, we have information about her identities, the project he has invested, the exact time and amount (the selected reward tier) of her investments. We exclude individuals who have invested less than 10 projects (the bottom 1% threshold of investors’ total investment count) in our observation period to ensure an eloquent empirical analysis. We also drop investors whose historical investment counts during the same period are so high that they cannot represent the behavior of a typical investor.<sup>3</sup> Since we focus on investors’ reward tier and investment timing selection behavior, we also exclude backers who make pledge without choosing reward tiers (they are less than 1% of the total investors in our sample). The resulting dataset has 20,035 investments made to 2,653 projects, involving 820 investors, ￥5,018,328.3 investment amount, and 9 different project categories. It should be noted that the 20,035 investments include both successful and unsuccessful investments made by the 820 investors within our observation period and all the investors use reward tier as their investment decisions instead of investment amount.

## -Insert Table 1 about Here-

Table 1 provides descriptions and summary descriptive statistics of the main variables in our study. All variables are measured with the original scales and can be further divided into two categories: project level and individual level variables. Considering the skewed measurement of the variables, we take the natural logarithm of those variables in the following empirical analysis.<sup>4</sup> As we can see from Table 1, the average percentage position of a reward tier selected by investors is the bottom 38.40% within a project’s reward scheme, and the average investment timing chosen by investors is 58.63%. In other words, on average, investors in our data set usually support a project when 58.63% of its fundraising goal is reached, and they always choose the reward tier which locates in the bottom 38.40% of a project’s reward scheme.

![](/api/attachments/HDPFJS2E/fulltext/images/ec0a881c14789ab3c9927e967e2ea82f89c7c8169436d02c77bf5e850f0be2ff.jpg)  
Figure 1. A screen shot of an active project on Zhongchou

## 3.2 Investment Inertia Persistence Measures

Inertia behavior is a behavioral patterns that individual usually repeats most. In our research context, investors’ IB refers to the possible temporal correlation among their repeated investment decisions. For example, a backer exhibits investment IB may always choose the reward tier with relative higher price within a project’s reward scheme, and support the project when its fundraising goal is almost reached. Therefore, backers’ IB can be measured by the potential temporal correlation-ship between their focal unobservable factors (e.g., unobserved heterogeneity).

Since backers’ investment action usually involves two simultaneous and related decisions: how much to invest and when to invest, we should measure their IB in those two decisions separately. Generally speaking, individual’s investment amount (i.e., the amount of money invested on a project) and original investment timing (i.e., the percentage ratio of elapsed time since the supported project was launched over its predetermined fundraising duration) on a project are two intuitive dependent variables to explore investors’ IB. However, if we take the operation reality of reward-based crowdfunding market into consideration, they are not reasonable. On one hand, a unique feature of the crowdfunding market is the tiered reward mechanism. There is no financial incentive for investors to put in more money than the minimum amount to get to the desired reward. Directly treating the absolute investment amount of each backer as a dependent variable cannot fully measure backers’ real investment aspiration. On the other hand, directly using of the original investment timing variable mentioned above requires every investor to evaluate the projects from day one (i.e., their launch day). However, this is highly unrealistic. Because crowdfunding projects may have varying funding time frames and investors may not always discover a project from the launch day. As a result, more reasonable measures of investment amount and timing should consider both project’s tiered reward mechanism and investors’ project evaluating timing. With those in mind, two new variables are constructed: InvRewardTier (the relative position of a reward tier selected by an investor within a project’s reward scheme) and InvTiming (the percentage fundraising progress of a project when a backer makes her investment).

More specifically, InvRewardTier<sub>i,j</sub><sup>5</sup> refers to the relative position of a reward tier chosen by investor i within project j’s reward scheme. For example, if a backer supported \$100 (i.e., the 4<sup>th</sup> reward {\$10, \$20, \$50, \$100, \$500}), the value of InvRewardTier in this context is 80% (measured by 4<sup>th</sup>/5). It means that the investor chosen the reward tier locating on the top-20% within the reward scheme to support this project. Different from the absolute investment amount, InvRewardTier considers both backer’s investment amount information and project’s tiered reward mechanism when meas ring individual investor’s decision on how much to support. InvTiming<sub>i,j</sub> here refers to the percentage fundraising progress of project j toward its goal when backer i makes her investment. For example, if a backer decided to support a project that has already collected \$800 over its \$1000 target, the investment timing for this backer is 80% (measured by 800/1000). Normalized with respect to campaign goal, InvTiming is able to capture the relative positon of an investment on the project’s fundraising process. Although the specific value of InvTiming in a backer’s particular investment can be affected by many factors, its repeated records form a backer’s repeated investment actions still enable us to examine her potential IB in investment timing selection. Furthermore, since InvTiming is dynamically updated on each projects’ home page, we do not need to require every investor to evaluate the projects from their launch day again. To sum up, investors’ IB in both reward tier and investment timing selection can be explored by examining the potential temporal correlation-ship between the focal value of InvRewardTier, InvTiming and their past values after controlling other cofounders.

## 3.3 Main Variables of Interest

We next interpret some other variables which have been proved to be able to influence individual’s investment decision in the crowdfunding market. First, extant literature has pointed out that project attributes, representing project quality signals, would influence backers’ investment decision [11, 29]. As a result, similar variables relevant to project attributes are constructed based on our data set: the fundraising target of a project (ProTarget), the length of project description in the online crowdfunding platform (ProDesLen), the category type of a project (ProType). In addition, the action from other backer’s investment decision [34]. To control this influence, we constructed a variable called AvgSupAmt<sub>i,t</sub>. It captures the average pledge amount from other investors on the same project before backer i’s t-th investment. For example, if a crowdfunding project has already attracted \$4500 from 50 backers before backer A’s investment, the AvgSupAmt in this context is \$90 per person (4500/50=90). It measures the peer influence that a backer may face when deciding which reward tier to choose. Furthermore, fundraisers usually promote their projects by providing project updates, and conducting comment conversations [29, 22]. To control this effect on individual’s investment decisions, we constructed two more variables: AccumNumComment<sub>i,t</sub> and AccumNumUpdate<sub>i,t</sub>. They refer to the accumulative number of project comment conversations and project updates before investor i's t-th investment respectively. Finally, backer’s investment experience and platform tenure may also affect their focal investment decisions. To control this influence, we constructed two variables named $A c c u m S u p P r o _ { \mathrm { i t } }$ and $T e n u r e _ { \mathrm { i t } }$ . They separately measure individual i's accumulative number of investments and platform tenure on the platform before her t-th support.

In sum, four sets of variables are constructed based on previous studies: (1) project’s attributes related variables, (2) peer influence related variable, (3) fundraisers’ marketing related variables, and (4) investors’ heterogeneity related variables. They will help us to estimate investors’ IB more easily.

## 4. Empirical Analysis

In this section, we begin our analysis by empirically examining whether investors as a whole demonstrate IB when choosing reward tier and investment timing in online crowdfunding market. Then an impulse and response analysis is conducted to explore this behavior.

## 4.1 The Econometric Model

To examine the potential temporal correlation-ship among backers repeated investment decisions (i.e., the inertia behavior), we separately treat their decisions on reward tier selection and investment timing selection as a function of her past decisions and other cofounders. Specifically, $I n \nu R e w a r d T i e r _ { \mathrm { i t } }$ is treated as a function of its past value (e.g., $I n \nu R e w a r d T i e r _ { \mathrm { i t - 1 } }$ $I n \nu R e w a r d T i e r _ { \mathrm { i t - 2 } } , \ . . . )$ , a set of variables including project related factors, individual investor related factors, and other factors. Similarly, $I n \nu T i m i n g _ { \mathrm { i t } }$ is also treated as a function of its past value (e.g., $I n \nu T i m i n g _ { \mathrm { i t } - 1 }$ $I n \nu T i m i n g _ { \mathrm { i t - 2 } } , \ . . . )$ , a set of variables mentioned above. However, since backers’ investment decisions on reward tier and investment timing selection are usually two simultaneous and related decisions, separately estimating them in two equations is always biased and inefficient [1].

In order to jointly estimate those two variables, we adopt a reduced form of VAR models in which each dependent variable is endogenous and is a linear function of the past values of all the dependent variables (e.g., InvRewardTier and InvTiming) in the system, a set of exogenous or predetermined variables, and an error term. The panel structure of our data set enables us to control for unobserved individual heterogeneity. The detailed form of our proposed PVAR model is specified as follows:

$$
\binom {I n v R e w a r d T i e r _ {i, t}} {I n v T i m i n g _ {i, t}} = \sum_ {j = 1} ^ {k} \left[ \begin{array}{c c} \beta_ {1 1} ^ {j} & \beta_ {1 2} ^ {j} \\ \beta_ {2 1} ^ {j} & \beta_ {2 2} ^ {j} \end{array} \right] \cdot \binom {I n v R e w a r d T i e r _ {i, t - j}} {I n v T i m i n g _ {i, t - j}} + \pmb {\gamma} \cdot \mathbf {X} _ {i, t} + \binom {\delta_ {t} ^ {1}} {\delta_ {t} ^ {2}} + \binom {\eta_ {i} ^ {1}} {\eta_ {i} ^ {2}} + \binom {\varepsilon_ {i, t} ^ {1}} {\varepsilon_ {i, t} ^ {2}}\tag{1}
$$

In Equation (1), $I n \nu R e w a r d T i e r _ { \mathrm { i , t } }$ and $I n \nu T i m i n g _ { \mathrm { i , t } }$ are endogenous variables. They denote the reward tier and investment timing selection decisions of investor i’s t-th investment. The matrix of $\beta$ is the

# ACCEPTED MANUSCRIPT

slope coefficients for the endogenous variables and k is the number of lags of dependent variables (we are going to discuss the optimal value of k in section 4.2). $\mathbf { X } _ { i , t }$ refers to the exogenous or predetermined variables which influence the t-th investment of backer i, including the listed project attributes in investor i’s t-th investment (e.g., $P r o T a r g e t _ { \mathrm { i , t } } ,$ $P r o D e s L e n _ { \mathrm { i , t } } ,$ , and $P r o j e c t T y p e _ { \mathrm { i , t } } )$ , other investors’ average investment amount on the same project before investor i’s t-th investment (e.g., $A \nu g S u p A m t _ { \mathrm { { - i , t } } } ,$ , treated as peer influence related factor), the accumulative number of project updates and comment conversations before investor i’s t-th investment (e.g., AccumNumUpdate<sub>i,t</sub> and AccumNumComment<sub>i,t</sub>, treated as fundraiser’s marketing related factors), the accumulative number of prior investments $( A c c u m S u p P r o _ { \mathrm { i , t } } )$ and platform tenure $( T e n u r e _ { \mathrm { i t } } )$ of backer i before her t-th support, as well as 8 project category dummy variables $( P r o j e c t T y p e \mathrm { { _ { i , t } } ) }$ . ?? is a matrix of coefficients to be estimated for those specified exogenous variables. The vector $( \delta _ { t } ^ { 1 } , \ \delta _ { t } ^ { 2 } )$ contains time dummies and it is used to control for any time effects of investment. (η<sub>??</sub><sup>1</sup>, $\boldsymbol { \mathsf { \eta } } _ { t } ^ { 2 } ) ^ { * }$ is a vector of unobserved individual effects, representing investors’ time-invariant characteristics. The vector $( \varepsilon _ { i , t } ^ { 1 } , \ \varepsilon _ { i , t } ^ { 2 } )$ is standard error term, and they are serially uncorrelated if a sufficient number of lags k is specified.

Note that our model is actually a dynamic model, and the lagged dependent variables can capture the potential factors that would affect investors’ past and current investment decisions.

## 4.2 Model Identification and Estimation

The model specified in Equation (1) is actually a panel VAR model with exogenous variables and unobservable fixed individual effects. As a kind of dynamic models with fixed effect, the main challenges to estimate the proposed model come from those lagged variables of dependent variables (i.e., $I n \nu R e w a r d T i e r _ { \mathrm { i , t - j } }$ and $I n \nu T i m i n g _ { \mathrm { i , t - j } } )$ . To get rid of the influence of fixed effect, within-group estimator (i.e., the least-squares estimator after subtracting the individual means of the observations) is widely used in the economic literature. However, in Equation (1), those lagged dependent variables are correlated with the average error term vector $( \overline { { \varepsilon } } _ { i } ^ { 1 } , ~ \overline { { \varepsilon } } _ { i } ^ { 2 } )$ in the within-group estimator. Many prior studies [30, 5] have pointed out that the within-group estimator is biased when it is used to estimate a dynamic panel model with fixed effects. To efficiently estimate all the coefficients in Equation (1), we estimate the proposed model by using standard generalized method of moments (GMM) estimator.

Following the standard procedure for estimating PVAR model, we start with a unit-root test to examine the stationarity of our data set. This is because the standard GMM estimator for panel VAR model may suffer from the weak instruments problems and the moment conditions will be break down if variables modeled in the system are near unit root [9, 8]. In our study, we use the Phillips-Perron (PP) unit-root test, which is a unit-root test widely used in dynamic panel analysis and find that there is no unit

Table 2. Phillips-Perron Unit Root Test

<table><tr><td></td><td>p-Statistic: Inverse chi-squared</td><td>p-Values</td></tr><tr><td>InvRewardTier</td><td>1.29e+04</td><td>0.0000</td></tr><tr><td>InvTiming</td><td>1.12e+04</td><td>0.0000</td></tr></table>

Next, we have to specify our model with an optimal k in Equation (1). Generally speaking, the value of the lag length k can be determined automatically by using the Moment Model Selection Criteria (MMSC) proposed by Andrews and Lu (2001) [4]. The criterion for choosing the optimal lag order is minimizing M-BIC (Bayesian Information Criterion), M-QIC (Hannan and Quinn Information Criterion) and M-AIC (Akaike Information Criterion). As we can see from Table 3, one lag of the dependent variables is sufficient for the two equations listed in our panel VAR model after considering both the values of M-BIC and M-QIC criteria. <sup>7</sup> Next we estimate the formulated panel VAR model by using Generalized Method of Moments (GMM) estimator [8].

Table 3. The Optimal Lag Order Selection of the Proposed Panel VAR model

<table><tr><td>Lag Order</td><td>M-BIC</td><td>M-QIC</td><td>M-AIC</td></tr><tr><td>1</td><td>-175.52*</td><td>-60.25*</td><td>-1.45</td></tr><tr><td>2</td><td>-155.70</td><td>-59.64</td><td>-10.64</td></tr><tr><td>3</td><td>-129.83</td><td>-52.98</td><td>-13.78*</td></tr><tr><td>4</td><td>-99.69</td><td>-42.05</td><td>-12.65</td></tr></table>

# ACCEPTED MANUSCRIPT

## 4.3 Estimation Results

Table 4 reports the empirical results for our baseline model in Equation (1).<sup>8</sup> It shows the short-term effects among investor’s reward tier and investment timing selection.<sup>9</sup> We first look at the estimated results in the InvRewardTier equation. The coefficient of InvRewardTier<sub>i,t-1</sub> (0.160) is positive and significant at the 0.1% level, indicating investor’s past reward tier selection is correlated with her current reward tier selection after controlling other observable and unobservable factors. This suggests the existence of investor’s IB in their reward tier selection. The length of project description (ProDesLen<sub>it</sub>) and fundraiser’s marketing effort in the project’s comment are found to have positive and sign ificant impacts on backers’ reward tier selection. This result points out the information value of project description and fundraisers’ marketing efforts in the online crowdfunding market. We also find that the coefficients of ProTarget<sub>it</sub> and AvgSupAmt<sub>-i,t</sub> are negative and significant, which means that larger project’s fundraising target and higher peer backers’ average investment amount intend to make investors choose reward tiers with relative lower price. This seems to be reasonable. In the eyes’ of investors, the success probability for a project with larger goal is usually relatively lower than a project with smaller one, and potential investors usually intend to support the project with caution. Furthermore, extant research also pointed out that projects with relative higher AvgSupAmt are usually associated with crowding-out effect [29], so investors also usually intend to choose the reward tier with lower price or even do not support when facing a project with relative higher AvgSupAmt. The positive and significant coefficient of Tenure<sub>i,t</sub> indicates that investors’ longer platform tenure usually encourage them to choose reward tiers with relative higher price, while the negative and significant coefficient of AccumSupPro<sub>i,t</sub> shows that backers with more investment experience intend to choose reward tiers with relative lower price.

Next, we turn our attention to the coefficients in the InvTiming equation. The positive and significant coefficient of InvTiming<sub>i,t-1</sub> (0.082) indicates that investor’s past investment timing selection is correlated with her current investment timing selection after controlling other observable and unobservable factors.

# ACCEPTED MANUSCRIPT

This also suggests the existence of investors’ IB in choosing investment timing. The positive and significant coefficients of $A \nu g S u p A m t _ { \mathrm { - i , t } } ,$ $A c c u m N u m U p d a t e _ { \mathrm { i , t } }$ and AccumNumComment<sub>i,t</sub> suggest that peer backers’ investment amount, fundraisers’ marketing effects in both project update and comment usually make backers make their investment decision later. One possible explanation for this is that backers are rational. They intend to spend more time to deal with the information received from peer investors and fundraisers, and finally use them to help their decision-making. What is interesting, if we compare their coefficients, we will find that the coefficient value of $A \nu g S u p A m t _ { \mathrm { - i , t } }$ variables, indicating that peer investors’ influence seems to be stronger than fundraisers’ marketing efforts related factors in affecting backers’ investment timing selection. $P r o T a r g e t _ { \mathrm { i t } }$ is found to have significantly negative influence on backers’ investment timing selection, which means that backers usually make their investment decisions a little bit earlier when they supporting projects with lager fundraising goals.

Table 4. Coefficient Estimates of the Proposed Panel VAR Model

<table><tr><td rowspan="2">Independent Variables</td><td colspan="2">Dependent Variables</td></tr><tr><td> $InvRewardTier_{i,t}$ </td><td> $InvTiming_{i,t}$ </td></tr><tr><td> $InvRewardTier_{i,t-1}$ </td><td>0.169***(5.79)</td><td>0.032(0.63)</td></tr><tr><td> $InvTiming_{i,t-1}$ </td><td>0.001(0.12)</td><td>0.082***(11.07)</td></tr><tr><td> $ProTarget_{i,t}$ </td><td>-0.059***(-5.03)</td><td>-0.463***(-23.94)</td></tr><tr><td> $ProDesLen_{i,t}$ </td><td>0.026+(1.90)</td><td>0.021(0.89)</td></tr><tr><td> $AccumSupPro_{i,t}$ </td><td>-0.128***(-3.82)</td><td>0.078(1.39)</td></tr><tr><td> $Tenure_{i,t}$ </td><td>0.076***(4.18)</td><td>-0.016(-0.54)</td></tr><tr><td> $AvgSupAmt_{i,t}$ </td><td>-0.030***(-9.07)</td><td>0.648***(119.03)</td></tr><tr><td> $AccumNumUpdate_{i,t}$ </td><td>0.008(0.37)</td><td>0.509***(13.20)</td></tr><tr><td> $AccumNumComment_{i,t}$ </td><td>0.032***(6.35)</td><td>0.463***(52.32)</td></tr><tr><td>Project Category Control</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Effect Control</td><td>Yes</td><td>Yes</td></tr></table>

Notes: (1) Numbers in parentheses are t-statistics;  
(2) $^ { * * * } p < 0 . 0 0 1 , ^ { * * } p < 0 . 0 1 , ^ { * } p < 0 . 0 5 , + p < 0 . 1 ;$

## 4.4 Impulse and Response Analysis of Investor’s Inertia Behavior

To examine the long-term effect of the PVAR model, Impulse and Response Functions (IRFs) are often used. It describes the response effect of one standard deviation shock of one dependent variable on the future values of other dependent variables in the model system after keeping all other variables constant. Figure 2 provides the four possible IRFs for our formulated PVAR model. It visualizes the dynamic pairwise relationships between InvRewardTier, InvTiming and their preceding variables (i.e., $I n \nu R e w a r d T i e r _ { \mathrm { i , t - 1 } }$ and $I n \nu T i m i n g _ { \mathrm { i , t - 1 } } )$ . The $5 ^ { \mathrm { t h } }$ and $9 5 ^ { \mathrm { t h } }$ confidence computed using 1000 Monte Carlo draws based on the estimated model.

![](/api/attachments/HDPFJS2E/fulltext/images/17b175c9b5ce73a2397b4a7ff54976aa0285bdb0554230aeedff5d59f358eaaa.jpg)  
(c) InvTiming(i,t-1) -> InvRewardTier(i,t)

(b) InvRewardTier(i,t-1) -> InvTiming(i,t)  
![](/api/attachments/HDPFJS2E/fulltext/images/a208ae7a0e15296b0e3924722cad99fcc0575fc3a02ebdb0453050a7639b0ea9.jpg)

![](/api/attachments/HDPFJS2E/fulltext/images/18b64507aa4c9e93ced79ae565aa3fc21520b04710db89c5d640d118fc06af0c.jpg)

(d) InvTiming(i,t-1) -> InvTiming(i,t)  
![](/api/attachments/HDPFJS2E/fulltext/images/f0d42dea31cc11d94034c78356ba6a3a136386b01e92a51b3ee1c5c721ccf889.jpg)  
Notes: (1)Impulse -> Response; (2) The dashed lines are 5th and 95th percentiles;  
Figure 2. The Results of Impulse Response Function Analysis

We are very interested in how InvRewardTier and InvTiming response to an exogenous shock of their own preceding variables (i.e., Figure 2(a) and Figure 2(d)), because they visualize the long-term effect of investors’ inertia behavior. As we can see from Figure 2(a) and Figure 2(d), an exogenous one-unit increasing shock to the preceding InvRewardTier (or InvTiming) is associated with an increase in InvRewardTier (or InvTiming) during the first several periods. However, this effect gradually reduces to zero as the time periods go on. Compared with Figure 2(a) and Figure 2(d), we can easily find that, the response magnitude of InvRewardTier is larger than that of InvTiming. It means that, backers’ IB in reward tier selection seems to be stronger than that in investing timing selection. Figure 2(b) and Figure 2(c) show the response of InvRewardTier (or InvTiming) to the positive shock of lagged InvTiming (or InvAmt). In Figure 2(b), we observe a nearly zero response of InvTiming, while in Figure 2(c) we first find an increase and then a decreased response of InvRewardTier. All those effects in Figure 2 gradually reduce to zero as time goes on.

## 5. The Moderating Effect of Investors’ Platform Tenure

Although previous analysis has pointed out the existence of investors’ IB in their investment decisions, its effect on backers’ reward tier selection or investing timing selection might be moderated by investors heterogeneities. For example, investors with different “platform age” in the crowdfunding platform may have different granularity responses to their IB. To better disentangle backers’ IB in their repeated investment decision behavior, we next interpret and evaluate the moderating of investors’ platform tenure on the identified inertia behavior and other cofounders (i.e., peer influence and fundraisers’ marketing related factors) in the online crowdfunding market.

## 5.1 The Moderating Effect of Platform Tenure on Investors’ Inertia Behavior

To examine the moderating effect of platform tenure on investors’ IB, we added two interaction terms InvRewardTie ${ \cdot } r _ { \mathrm { i , t - 1 } } { \times } T e n u r e _ { \mathrm { i , t } }$ and $I n \nu T i m i n g _ { \mathrm { i , t - 1 } } \times T e n u r e _ { \mathrm { i , t } }$ to the right hand of Equation (1). Similar processes introduced in Section 4 are conducted to estimate the parameters. The first and fourth column of Table 5 reports the estimated results in this new situation.

\- Insert Table 5 about Here -

As we can see from Table 5, the main effect of $I n \nu R e w a r d T i e r _ { \mathrm { i , t - 1 } }$ in the first column and the main effect of $I n \nu T i m i n g _ { \mathrm { i , t - 1 } }$ in the fourth column are still positive and significant. This further verified the existence of investors’ IB. In addition, it should be noted that all the coefficients of other variables are consistent with Table 4. This indicates that all the findings in Section 4 are still hold after considering the moderating effect of platform tenure. What is interesting, the coefficient of interaction term InvRewardTier<sub>i,t-1</sub>×Tenure<sub>i,t</sub> is significantly positive, while the coefficient of $I n \nu T i m i n g _ { \mathrm { i , t - 1 } } \times T e n u r e _ { \mathrm { i , t } }$ is significantly negative. This implies that investors’ platform tenure significantly accentuates their IB in reward tier selection, but weakens their IB in investment timing selection.

## 5.2 The Moderating Effect of Platform Tenure on Peer Influence Factor

Next, we are going to examine the moderating effect of investors’ platform tenure on the peer influence factor (i.e., $A \nu g S u p A m t _ { \mathrm { i , t } } )$ . Analogously, we add an interaction term $A \nu g S u p A m t _ { \mathrm { - i , t } } \times T e n u r e _ { \mathrm { i , t } }$ to the model parameters. The second and fifth column of Table 5 reports the estimated results.

As we can see from Table 5, the main effect of InvRewardTier<sub>i,t-1</sub> in the second column and the main effect of $I n \nu T i m i n g _ { \mathrm { i , t - 1 } }$ in the fifth column are still positive and significant. All the coefficients of other variables are consistent with Table 4. So the findings in the aforementioned sections are still hold. The coefficients for interaction term AvgSupAmt $_ { \mathrm { i , t } } { \times } T e n u r e _ { \mathrm { i , t } }$ in InvRewardTier equation and InvTiming equation are not significant, indicating that the impact of peer influence factor on investors’ reward tier selection and investment timing selection is not significantly affected by their platform tenure in our Zhongchou platform.

## 5.3 The Moderating Effect of Platform Tenure on Fundraiser’s Marketing Related Factors

Finally, we are going to examine the moderating effect of investors’ platform tenure on AccumNumUpdate and AccumNumUpdate . Analogously, we formulate a nested model by adding two interaction terms: AccumNumUpdate ×Tenure and AccumNumComment ×Tenure in the model mentioned in Section 5.2. Similar processes are also conducted to estimate all the parameters and the results are reported in the third and sixth column of Table 5.

As we can see from Table 5, the main effect of $I n \nu R e w a r d T i e r _ { \mathrm { i , t - 1 } }$ in the third column and the main effect of $I n \nu T i m i n g _ { \mathrm { i , t - 1 } }$ in the sixth column are still positive and significant, and all the coefficients of other variables are also consistent with the aforementioned findings. In InvRewardTier equation, the coefficients for $A c c u m N u m U p d a t e _ { \mathrm { i , t } } { \times } T e n u r e _ { \mathrm { i , t } }$ and AccumNumComment<sub>i,t</sub>×Tenure<sub>i,t</sub> are negative but not significant. This indicates that the effect of fundraisers’ marketing related factors on investors’ reward tier selection is not affected by their platform tenure in Zhongchou. However, in InvTiming equation, the coefficient for AccumNumUpdate<sub>i,t</sub>×Tenure<sub>i,t</sub> is significantly negative, and the coefficient for AccumNumComment<sub>i,t</sub>×Tenure<sub>i,t</sub> is not significant. This implies that the effect of fundraisers’ marketing related factors on backers’ investment timing selection is partially moderated by their platform tenure in our Zhongchou platform.

## 6. Robustness Checks

In this section, we conduct robustness checks to rule out alternative explanations for our empirical results presented earlier.

## 6.1 Controlling the Time Interval between Individual’s Two Consecutive Investments

Since the time interval between two consecutive investments made by an investor could influence her IB (i.e., some backers may forget their last investment decisions due to a long time interval between the focal investment and last investment), we control this variable in our first robustness checks. Specifically, we re-estimated all the models formulated in Section 4 and 5 by adding two interaction terms, InvRewardTier<sub>i,t-1</sub> $\times T i m e I n t e r \nu a l _ { \mathrm { i , t } }$ , InvTiming<sub>i,t-1</sub>× $\begin{array} { r } { T i m e I n t e r { \nu } a l _ { \mathrm { i , t } } } \end{array}$ <sub>t</sub>, into the regression system. The TimeInterval<sub>i,t</sub> here refers to the time interval (measured by day) between investor i’s t-th and (t-1)-th investment. Regression results are presented in Table 6.

## - Insert Table 6 Here -

As we can see from Table $6 , \mathrm { a l t h o u g h }$ the time interval between two consecutive investments coefficients of $I n \nu T i m i n g _ { \mathrm { i , t - 1 } }$ nd $I n \nu T i m i n g _ { \mathrm { i , t - 1 } } { } ^ { * }$ $T i m e I n t e r \nu a l _ { \mathrm { i , t - 1 } }$ are opposite and statistically significant), the main effect of investors’ inertia behavior still exists. In addition, almost all the other empirical findings mentioned in our study are still hold according to this table.

## 6.2 Different Lag Orders of Dependent Variables

Although the M-BIC and M-QIC criteria in Section 4.2 suggest one lag of the dependent variables in the proposed PVAR model is sufficient, we consider higher order lag of the dependent variables in this section to make sure our empirical results are robust to the choice of lag orders. Specifically, we separately added the second and third-order lag of InvRewardTier and InvTiming into the proposed PVAR model, and re-estimate the models. Regression results are summarized in Table 7 and Table 8. As we can see from those tables, the main effects of investors’ IB on their investment decisions still exist and almost all the other empirical findings aforementioned are still hold.

-Insert Table 7 and Table 8 Here-

## 7. Conclusion and Discussion

We studied investors’ IB in making their investment decisions on which reward tier to choose and when to invest in the reward-based crowdfunding market. We formulated a Panel Vector Auto Regression (PVAR) model with exogenous variables to examine the dynamic interactions among investor’s reward tier selection and investment timing selection. Considering investors’ heterogeneity in their platform age, we formulated models to interpret the moderating effect of investors’ platform tenure on the identified inertia behavior, the peer influence related factor and the fundraisers’ marketing related factors. A series of robustness checks were also conducted to rule out alternative explanations for our study.

Overall, we found positive and significant temporal correlation-ship among backers’ repeated investment decisions (i.e., which reward tier to choose and when to support) after controlling both observable and unobservable factors. This suggests the existence of IB in backers’ both reward tier selection and investment timing selection. Our impulse and response analysis shows that investors’ IB in reward tier selection seems to be stronger than that in investment timing selection. Project attribute related factors have different impacts on investors’ decision-making. Specifically, project’s fundraising target has significant and negative influence on investors’ both reward tier selection and investment timing selection, while the length of project description only has significantly positive impact on their reward tier selection. Peer investors’ influence seems to be stronger than fundraisers’ marketing efforts in affecting backers’ investment timing selection. Furthermore, investors’ platform tenure can significantly accentuate the IB in their reward tier selection, but weaken that in their investment timing selection.

## 7.1 Managerial Implications

Our study sheds light on various practical implications for the crowdfunding participants including investors, fundraisers, as well as the crowdfunding intermediaries hosting them. First, fundraisers in the

# ACCEPTED MANUSCRIPT

crowdfunding market should keep in mind that backers’ reward tier selection and investment timing selection are affected not only by those widely accepted factors (i.e., project attributes, peer investors and fundraisers’ project marketing activities), but also their own behavior (i.e., IB). What is more, backers with more investment experience seem to be cautious when making reward tier selectin decision. Since backers’ historical investment records are usually publicly viewable in the crowdfunding market, fundraisers are encouraged to make full use of this kind of information to conduct personalized project or reward tier recommendation to help investors’ decision-making. Second, investors, especially those new investors in the crowdfunding market, usually imitate others’ investment decisions. Our study points out that the imitation action should be treated with caution. That is because the imitated decisions sometimes are not entirely rationally made. Some of them are affected by prior investors’ IB. Backers are encouraged to rationally infer useful information from projects rather than simply imitate other backers’ investment decisions. Third, understanding the inherit investment behavior from investors can help crowdfunding platforms provide more fine-grained service to both investors and fundraisers. On one hand, they can make full use of its information advantages to guide investors, especially those new investors with limited investment knowledge on the platform, to make rational investment decisions. On the other hand, online crowdfunding platform can also help fundraisers design efficient information disclosing tools (i.e., project rating board from investors) and personalized recommendation system to further reduce the information asymmetry between projects and potential investors.

## 7.2 Limitation and Further Research

Although this study provides useful insights and implications in the emerging fundraising market, we would also like to acknowledge a few limitations and point out further research directions. First of all, we identified investors’ IB in their repeated investment in the online crowdfunding market. However, we cannot provide more detailed answers to the questions like why do backers exhibit this behavior, and how do they combine IB with other factors to make their final investment decisions. Future research should conduct a randomized filed experiment to control for a broader spectrum of factors and provide more comprehensive insights into backers’ behavioral mechanism of investment decisions.

# ACCEPTED MANUSCRIPT

Second, since our data is collected from one of the largest crowdfunding market in China, the object we analyzed here are the investment behavior of Chinese investors. However, the determinants of investor’s decision and behavior may change because of different cultures [17, 7], there is a need to conduct such an analysis in other country to verify the generalizability of our findings in future research.

Third, prior studies have pointed out that backers’ motivation of participating in different kinds of crowdfunding market varies, and their investment behavior and decision making process may be also different [16, 11, 24]. Although we observe investors’ IB in their reward tier selection and investment timing selection, we have to acknowledge that there exists a need for further studies to verify the generalizability of our findings in other crowdfunding context (e.g., the equity-based crowdfunding market, the lending-based crowdfunding market).

Finally, understanding the behavior mechanism of investors is just an efficient one-step we moved in the crowdfunding research. Next we can develop predictive analysis (e.g., crowdfunding project recommender or investment prediction), and evaluate the effects of the predictive analysis based on our understandings of investors’ behavior.

## Acknowledgements

This work is supported by the National Natural Science Foundation of China [grant numbers 71701119], Excellent Faculty Research Foundation of Shanghai University of Finance and Economics [grant numbers 2017110159] and the Young Faculty Development Foundation of Shanghai Government [grant numbers ZZSUIBE16025].

## Reference:

[1] Adomavicius, G., Bockstedt, J., and Gupta, A. Modeling supply-side dynamics of IT components, products, and infrastructure: An empirical analysis using vector auto regression. Information Systems Research, 23, 2 (2012), 397–417.

[2] Agrawal, Ajay, Christian Catalini, and Avi Goldfarb. Crowdfunding: Geography, Social Networks,

and the Timing of Investment Decisions. Journal of Economics & Management Strategy, 24, 2 (2015), 253-274.

[3] Ahmad, Z., Ibrahim, H., and Tuyon, J. Behavior of fund managers in Malaysian investment management industry. Qualitative Research in Financial Markets, 9, 3 (2017), 205-239.

[4] Andrews, D.W.K., and Lu, B. Consistent model and moment selection procedures for GMM estimation with application to dynamic panel data models. Journal of Econometrics, 101, 1 (2001), 123–164.

[5] Arellano M,. Panel Data Econometrics, Oxford University Press, Oxford, UK, 2003.

[6] Barberis, N., and Thaler, R. A survey of behavioral finance. Handbook of the Economics of Finance, 1 (2003), 1053-1128.

[7] Bekaert, G., Hoyem, K., Hu, W. Y., & Ravina, E. Who is internationally diversified? Evidence from the 401 (k) plans of 296 firms. Journal of Financial Economics, 124, 1 (2017), 86-112.

[8] Binder M, Hsiao C, Pesaran MH. Estimation and inference in short panel vector auto regressions with unit roots and cointegration. Econometric Theory, 21, 4 (2005), 795–837.

[9] Blundell, R. and Bond, S. Initial conditions and moment restrictions in dynamic panel data models. Journal of Econometrics, 87, 1 (1998), 115–143.

[10] Burtch, G., Ghose, A. and Wattal, S. The hidden cost of accommodating crowdfunder privacy preferences: a randomized field experiment, Management Science, 61, 5 (2015), 949–962.

[11] Burtch, G., Ghose, A., & Wattal, S. An empirical examination of the antecedents and consequences of contribution patterns in crowd-funded markets. Information Systems Research, 24, 3 (2013), 499-519.

[12] Chen, H., De, P., & Hu, Y. J. IT-enabled broadcasting in social media: An empirical study of artists’ activities and music sales. Information Systems Research, 26, 3 (2015), 513-531.

[13] Chung, Sunghun and Animesh, Animesh and Han, Kunsoo and Pinsonneault, Alain, 2016. Does Give-And-Take Really Matter? Dynamics of Social Interactions in Social Network (November 17, 2016). Available at SSRN: https://ssrn.com/abstract=2871047.

[14] Filbeck, G., Ricciardi, V., Evensky, H. R., Fan, S. Z., Holzhauer, H. M., & Spieler, A. Behavioral finance: A panel discussion. Journal of Behavioral and Experimental Finance, 15 (2017), 52-58.

[15] Foucault, T., & Fresard, L. Learning from peers' stock prices and corporate investment. Journal of Financial Economics, 111, 3 (2014), 554-577.

[16] Gerber, E. M., Hui, J. S., & Kuo, P. Y. Crowdfunding: Why people are motivated to post and fund projects on crowdfunding platforms. In Proceedings of the International Workshop on Design, Influence, and Social Technologies: Techniques, Impacts and Ethics, 2012, 2, 11.

[17] Grinblatt, M., and Keloharju, M. The investment behavior and performance of various investor types: a study of Finland's unique data set. Journal of financial economics, 55, 1 (2000), 43-67.

[18] Heckman, James J. Heterogeneity and State Dependence. National Bureau of Economic Research, Inc, 2009.

[19] Kaniel, R., and Parham, R. WSJ Category Kings–The impact of media attention on consumer and mutual fund investment decisions. Journal of Financial Economics, 123, 2 (2017), 337-356.

[20] Kuhnen, C. M., and Miu, A. C. Socioeconomic status and learning from financial information. Journal of Financial Economics, 124, 2 (2017), 349-372.

[21] Kuppuswamy, V. and Bayus, B. L. Crowdfunding creative ideas: The dynamics of project backers in kickstarter, UNC Kenan-Flagler Research Paper (2013-15).

[22] Li, Zhuoxin and Duan, Jason A. Network Externalities in Collaborative Consumption: Theory, Experiment, and Empirical Investigation of Crowdfunding (November 17, 2016). Available at SSRN: https://ssrn.com/abstract=2506352.

[23] Lin, M., Viswanathan, S. Home bias in online investments: An empirical study of an online crowdfunding market. Management Science, 62, 5 (2015), 1393-1414.

[24] Lukkarinen, Anna, et al., Success drivers of online equity crowdfunding campaigns. Decision Support Systems, 87 (2016), 26-38.

[25] Luo, X., and Zhang, J. How do consumer buzz and traffic in social media marketing predict the value of the firm? Journal of Management Information Systems, 30, 2 (2013), 213–238.

[26] Luo, X., Zhang, J., and Duan, W. Social media and firm equity value. Information Systems Research, 24, 1 (2013), 146-163.

[27] Menkhoff, L., Schmeling, M., and Schmidt, U. Overconfidence, experience, and professionalism: An experimental study. Journal of Economic Behavior & Organization, 86 (2013), 92-101.

[28] Michael Siering, Jascha-Alexander Koch and Amit V. Deokar. DetectingFraudulent Behavior on Crowdfunding Platforms: The Role of Linguistic and Content-Based Cuesin Static and Dynamic Contexts, Journal of Management Information Systems, 33, 2 (2016), 421-455.

[29] Mollick, Ethan R. The dynamics of crowdfunding: An exploratory study. Journal of Business Venturing, 29, 1 (2014), 1-16.

[30] Nickell S. Biases in dynamic models with fixed effects. Econometrica, 49, 6 (1981), 1417–1426.

[31] Ordanini A, Miceli L, Pizzetti M, Parasuraman A. Crowdfunding: transforming customers into investors through innovative service platforms. Journal of service management, 22, 4 (2010), 443– 470.

[32] Schwienbacher, Armin and Larralde, Benjamin, Crowdfunding of Small Entrepreneurial Ventures (September 28, 2010). HANDBOOK OF ENTREPRENEURIAL FINANCE, Oxford University Press. Available at SSRN: https://ssrn.com/abstract=1699183.

[33] Sen, R., and Tumarkin, R. Stocking up: Executive optimism, option exercise, and share retention. Journal of Financial Economics, 118, 2 (2015), 399-430.

[34] Thies, Ferdinand, M. Wessel, and A. Benlian. Effects of Social Interaction Dynamics on Platforms, Journal of Management Information Systems, 33, 3 (2016), 843-873.

[35] Wessel, Michael, F. Thies, and A. Benlian. The emergence and effects of fake social information: Evidence from crowdfunding. Decision Support Systems, 90(2016):75-85.

[36] Xiao, S., Tan, X., Dong, M., and Qi, J. How to design your project in the online crowdfunding market? Evidence from Kickstarter. Proceedings of International Conference on Information Systmes (ICIS, 2014), Auckland, New Zealand.

[37] Yuan, Hui, R. Y. K. Lau, and W. Xu. The determinants of crowdfunding success: A semantic text

analytics approach. Decision Support Systems, 91(2016):67-76.

[38] Zhang, J., and Liu, P. Rational herding in microloan markets. Management Science, 58, 5 (2012), 892-91.

## ACCEPTED MANUSCRIPT

## Tables and Figures

Table 1. Main Variables and Summary Statistics

<table><tr><td>Variables</td><td>Definition</td><td>Observation</td><td>Mean</td><td>Std. Dev.</td></tr><tr><td>Project Level</td><td></td><td></td><td></td><td></td></tr><tr><td> $ProTarget_{i,t}$ </td><td>The Fundraising goal of project in investor i&#x27;s t-th support</td><td>20,035</td><td>38,245.46</td><td>177,812.10</td></tr><tr><td> $ProDesLen_{i,t}$ </td><td>The length of project description in investor i&#x27;s t-th support</td><td>20,035</td><td>1,306.99</td><td>1,282.98</td></tr><tr><td> $AvgSupAmt_{-i,t}$ </td><td>The average pledge amount contributed by others on the same project before investor i&#x27;s t-th support</td><td>20,035</td><td>261.25</td><td>2,812.84</td></tr><tr><td> $AccumNumUpdate_{i,t}$ </td><td>The accumulated number of project updates before investor i&#x27;s t-th support</td><td>20,035</td><td>1.058</td><td>3.72</td></tr><tr><td> $AccumNumComment_{i,t}$ </td><td>The accumulated number of project comment conversations before investor i&#x27;s t-th support</td><td>20,035</td><td>27.84</td><td>118.23</td></tr><tr><td> $ProjectType_{i,t}$ </td><td>Dummy variables used to represent the project categories in our data set</td><td>20,035</td><td>-</td><td>-</td></tr><tr><td>Individual Level</td><td></td><td></td><td></td><td></td></tr><tr><td> $InvRewardTier_{i,t}$ </td><td>The relative percentage position of a reward tier chosen by investor i in her t-th support</td><td>20,035</td><td>38.44</td><td>29.28</td></tr><tr><td> $InvTiming_{i,t}$ </td><td>Investment timing of investor i&#x27;s t-th support</td><td>20,035</td><td>58.63</td><td>83.68</td></tr><tr><td> $AccumSupPro_{i,t}$ </td><td>The #investment made by investor i before her t-th support</td><td>20,035</td><td>57.15</td><td>103.33</td></tr><tr><td> $Tenure_{i,t}$ </td><td>Investor i&#x27;s platform tenure on before her t-th support (measured by day)</td><td>20,035</td><td>142.23</td><td>133.59</td></tr></table>

Table 5. The Moderating Roles of Investors’ Platform Tenure

<table><tr><td rowspan="2">Independent Variables</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td colspan="3"> $InvRewardTier_{i,t}$ </td><td colspan="3"> $InvTiming_{i,t}$ </td></tr><tr><td> $InvRewardTier_{i,t-1}$ </td><td>0.295+(1.81)</td><td>0.282+(1.85)</td><td>0.320+(1.83)</td><td>0.300(1.07)</td><td>0.266(1.02)</td><td>0.383(1.27)</td></tr><tr><td> $InvTiming_{i,t-1}$ </td><td>0.022(1.53)</td><td>0.018(1.55)</td><td>0.018(1.47)</td><td>0.120***(4.79)</td><td>0.109***(5.44)</td><td>0.113***(5.36)</td></tr><tr><td> $InvRewardTier_{i,t-1} \times Tenure_{i,t}$ </td><td>0.031***(10.01)</td><td>0.049***(3.49)</td><td>0.044*(2.43)</td><td>--</td><td>--</td><td>--</td></tr><tr><td> $InvTiming_{i,t-1} \times Tenure_{i,t}$ </td><td>--</td><td>--</td><td>--</td><td>-0.010+(-1.88)</td><td>-0.008+(-1.80)</td><td>-0.008+(-1.89)</td></tr><tr><td> $ProTarget_{it}$ </td><td>-0.061***(-5.65)</td><td>-0.062***(-6.13)</td><td>-0.061***(-5.59)</td><td>-0.463***(-23.94)</td><td>-0.466***(-26.40)</td><td>-0.468***(-28.47)</td></tr><tr><td> $ProDesLen_{it}$ </td><td>0.021*(2.11)</td><td>0.020*(2.17)</td><td>0.023*(2.15)</td><td>0.021(0.89)</td><td>0.012(0.67)</td><td>0.009(0.57)</td></tr><tr><td> $AccumSupPro_{i,t}$ </td><td>-0.127***(-3.81)</td><td>-0.129***(-3.86)</td><td>-0.099*(-2.37)</td><td>0.078(1.39)</td><td>0.079(1.41)</td><td>0.075(1.36)</td></tr><tr><td> $Tenure_{i,t}$ </td><td>0.031***(10.01)</td><td>0.049***(3.49)</td><td>0.044*(2.43)</td><td>0.245(1.08)</td><td>0.251(1.09)</td><td>0.355(1.34)</td></tr><tr><td> $AvgSupAmt_{-i,t}$ </td><td>-0.032***(-10.20)</td><td>-0.012*(-2.13)</td><td>-0.018**(-2.61)</td><td>0.645***(131.00)</td><td>0.687***(25.25)</td><td>0.699***(22.33)</td></tr><tr><td> $AccumNumUpdate_{i,t}$ </td><td>0.013(0.67)</td><td>0.014(0.68)</td><td>0.022(0.96)</td><td>0.521***(14.87)</td><td>0.521***(14.94)</td><td>0.786***(6.16)</td></tr><tr><td> $AccumNumComment_{i,t}$ </td><td>0.030***(6.95)</td><td>0.030***(7.02)</td><td>0.041***(3.89)</td><td>0.459***(59.79)</td><td>0.459***(60.89)</td><td>0.457***(23.10)</td></tr><tr><td> $AvgSupAm_{-i,t} \times Tenure_{i,t}$ </td><td></td><td>-0.004(-1.08)</td><td>-0.004(-1.01)</td><td></td><td>-0.010(-1.59)</td><td>-0.011(-0.96)</td></tr><tr><td> $AccumNumComment_{i,t} \times Tenure_{i,t}$ </td><td></td><td></td><td>-0.003(-1.15)</td><td></td><td></td><td>0.000(0.09)</td></tr><tr><td> $AccumNumUpdate_{i,t} \times Tenure_{i,t}$ </td><td></td><td></td><td>-0.025(-1.22)</td><td></td><td></td><td>-0.066*(-2.12)</td></tr><tr><td>Project Category Control</td><td>Yes</td><td></td><td>Yes</td><td>Yes</td><td></td><td>Yes</td></tr><tr><td>Time Effect Control</td><td>Yes</td><td></td><td>Yes</td><td>Yes</td><td></td><td>Yes</td></tr></table>

Notes: (1) Numbers in parentheses are t-statistics;  
(2) \*\*\* $p < 0 . 0 0 1 , ^ { * * } p < 0 . 0 1 , ^ { * } p < 0 . 0 5 , + p < 0 . 1 ;$

## ACCEPTED MANUSCRIPT

Table 6. Robustness Check by Controlling the Investment Time Interval

<table><tr><td rowspan="2">Independent Variables</td><td colspan="8">Dependent Variables</td></tr><tr><td colspan="4"> $InvRewardTier_{i,t}$ </td><td colspan="4"> $InvTiming_{i,t}$ </td></tr><tr><td>(1):  $InvRewardTier_{i,t-1}$ </td><td>0.161***(5.19)</td><td>0.208*(2.12)</td><td>0.228*(2.32)</td><td>0.290+(1.65)</td><td>-0.020(-0.37)</td><td>0.288(1.04)</td><td>0.251(0.97)</td><td>0.373(1.24)</td></tr><tr><td>(2):  $InvTiming_{i,t-1}$ </td><td>-0.015*(-2.38)</td><td>0.007(0.47)</td><td>0.004(0.30)</td><td>0.004(0.31)</td><td>0.164***(15.08)</td><td>0.179***(6.93)</td><td>0.168***(7.96)</td><td>0.172***(7.71)</td></tr><tr><td>(1) $\times TimeInterval_{i,t}$ </td><td>0.001(0.64)</td><td>0.000(0.36)</td><td>0.000(0.39)</td><td>0.000(0.17)</td><td>0.009***(6.26)</td><td>0.009***(6.70)</td><td>0.010***(6.75)</td><td>0.009***(6.44)</td></tr><tr><td>(2) $\times TimeInterval_{i,t}$ </td><td>0.003***(3.36)</td><td>0.003***(3.81)</td><td>0.003***(3.77)</td><td>0.003***(3.75)</td><td>-0.014***(-10.81)</td><td>-0.014***(-10.69)</td><td>-0.014***(-10.71)</td><td>-0.014***(-10.72)</td></tr><tr><td> $ProTarget_{it}$ </td><td>-0.062***(-5.21)</td><td>-0.064***(-5.95)</td><td>-0.065***(-6.45)</td><td>-0.064***(-5.82)</td><td>-0.458***(-23.47)</td><td>-0.460***(-26.18)</td><td>-0.463***(-28.25)</td><td>-0.458***(-25.51)</td></tr><tr><td> $ProDesLen_{it}$ </td><td>0.024+(1.72)</td><td>0.019+(1.92)</td><td>0.019*(1.99)</td><td>0.021*(1.99)</td><td>0.022(0.90)</td><td>0.013(0.74)</td><td>0.010(0.63)</td><td>0.018(0.95)</td></tr><tr><td> $AccumSupPro_{i,t}$ </td><td>-0.119***(-3.62)</td><td>-0.117***(-3.56)</td><td>-0.118***(-3.61)</td><td>-0.090*(-2.19)</td><td>0.064(1.17)</td><td>0.064(1.17)</td><td>0.061(1.11)</td><td>0.126+(1.77)</td></tr><tr><td> $Tenure_{i,t}$ </td><td>0.066***(3.62)</td><td>0.159+(1.90)</td><td>0.180*(2.41)</td><td>0.226*(2.34)</td><td>-0.006(-0.20)</td><td>0.270(1.19)</td><td>0.277(1.21)</td><td>0.385(1.45)</td></tr><tr><td>(3): AvgSupAmt $_{i,t}$ </td><td>-0.029***(-8.75)</td><td>-0.030***(-9.77)</td><td>-0.014***(-10.81)</td><td>-0.013***(-10.45)</td><td>0.643***(118.38)</td><td>0.640***(130.28)</td><td>0.686***(25.31)</td><td>0.697***(22.25)</td></tr><tr><td>(4):  $AccumNumUpdate_{i,t}$ </td><td>0.009(0.41)</td><td>0.012(0.62)</td><td>0.013(0.63)</td><td>0.015(0.33)</td><td>0.508***(13.16)</td><td>0.525***(14.95)</td><td>0.525***(15.04)</td><td>0.794***(6.20)</td></tr><tr><td>(5):AccumNumComment $_{i,t}$ </td><td>0.033***(6.47)</td><td>0.031***(7.15)</td><td>0.031***(7.24)</td><td>0.041***(3.86)</td><td>0.459***(51.96)</td><td>0.456***(59.50)</td><td>0.455***(60.60)</td><td>0.456***(23.06)</td></tr><tr><td>(1) $\times Tenure_{i,t}$ </td><td></td><td>0.022*(2.17)</td><td>0.027*(2.01)</td><td>0.042*(2.01)</td><td></td><td>-</td><td>-</td><td>-</td></tr><tr><td>(2) $\times Tenure_{i,t}$ </td><td></td><td>-</td><td>-</td><td>-</td><td></td><td>-0.003***(-3.40)</td><td>-0.003***(-3.44)</td><td>-0.003***(-3.52)</td></tr><tr><td>(3) $\times Tenure_{i,t}$ </td><td></td><td></td><td>-0.003(-0.88)</td><td>-0.003(-0.85)</td><td></td><td></td><td>-0.012(-0.33)</td><td>-0.015(-0.88)</td></tr><tr><td>(5) $\times Tenure_{i,t}$ </td><td></td><td></td><td></td><td>-0.002(-1.02)</td><td></td><td></td><td></td><td>-0.000(-0.10)</td></tr><tr><td>(4) $\times Tenure_{i,t}$ </td><td></td><td></td><td></td><td>-0.028(-1.63)</td><td></td><td></td><td></td><td>-0.067*(-2.15)</td></tr><tr><td>Project Category Control</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Effect Control</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: (1) Numbers in parentheses are t-statistics;  
(2) \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, + p < 0.1;

Table 7. Robustness Check by Choosing 2 Lag Orders of Dependent Variables

<table><tr><td rowspan="2">Independent Variables</td><td colspan="8">Dependent Variables</td></tr><tr><td colspan="4"> $InvRewardTier_{i,t}$ </td><td colspan="4"> $InvTiming_{i,t}$ </td></tr><tr><td>(1):  $InvRewardTier_{i,t-1}$ </td><td>0.172***(6.07)</td><td>0.336+(1.84)</td><td>0.321+(1.87)</td><td>0.350+(1.88)</td><td>0.017(0.35)</td><td>0.256(0.82)</td><td>0.225(0.77)</td><td>0.320(1.01)</td></tr><tr><td>(2):  $InvTiming_{i,t-1}$ </td><td>0.002(0.44)</td><td>0.027+(1.90)</td><td>0.023*(1.96)</td><td>0.022+(1.90)</td><td>0.078***(11.11)</td><td>0.109***(4.41)</td><td>0.100***(4.98)</td><td>0.104***(5.09)</td></tr><tr><td> $ProTarget_{it}$ </td><td>-0.059***(-5.35)</td><td>-0.060***(-5.68)</td><td>-0.061***(-6.15)</td><td>-0.061***(-6.00)</td><td>-0.468***(-26.39)</td><td>-0.469***(-27.66)</td><td>-0.471***(-29.65)</td><td>-0.469***(-28.74)</td></tr><tr><td> $ProDesLen_{it}$ </td><td>0.025+(1.90)</td><td>0.020*(2.02)</td><td>0.019*(2.06)</td><td>0.021*(2.09)</td><td>0.016(0.70)</td><td>0.009(0.54)</td><td>0.007(0.45)</td><td>0.012(0.68)</td></tr><tr><td> $AccumSupPro_{i,t}$ </td><td>-0.124**(-3.18)</td><td>-0.124**(-3.22)</td><td>-0.126**(-3.27)</td><td>-0.092*(-1.98)</td><td>0.072(1.09)</td><td>0.071(1.09)</td><td>0.068(1.05)</td><td>0.133(1.64)</td></tr><tr><td> $Tenure_{i,t}$ </td><td>0.079***(3.89)</td><td>0.203*(2.07)</td><td>0.184+(1.91)</td><td>0.265+(1.65)</td><td>-0.006(-0.18)</td><td>0.215(0.87)</td><td>0.222(0.88)</td><td>0.299(1.10)</td></tr><tr><td>(3): AvgSupAmt. $_{i,t}$ </td><td>-0.031***(-8.81)</td><td>-0.032***(-10.12)</td><td>-0.029*(-2.00)</td><td>-0.028*(-1.74)</td><td>0.650***(113.72)</td><td>0.648***(126.71)</td><td>0.688***(22.99)</td><td>0.700***(21.33)</td></tr><tr><td>(4):AccumNumUpdate $_{i,t}$ </td><td>0.007(0.32)</td><td>0.015(0.70)</td><td>0.015(0.70)</td><td>0.016(0.74)</td><td>0.501***(12.44)</td><td>0.511***(13.98)</td><td>0.511***(14.00)</td><td>0.768***(6.06)</td></tr><tr><td>(5):AccumNumComment $_{i,t}$ </td><td>0.031***(6.04)</td><td>0.029***(6.44)</td><td>0.029***(6.48)</td><td>0.034**(3.02)</td><td>0.460***(52.32)</td><td>0.458***(58.74)</td><td>0.457***(59.47)</td><td>0.438***(20.78)</td></tr><tr><td>(1) $\times$ Tenure $_{i,t}$ </td><td></td><td>0.054**(3.22)</td><td>0.049*(2.32)</td><td>0.058+(1.69)</td><td></td><td>-</td><td>-</td><td>-</td></tr><tr><td>(2) $\times$ Tenure $_{i,t}$ </td><td></td><td>-</td><td>-</td><td>-</td><td></td><td>-0.009*(-2.09)</td><td>-0.008*(-1.91)</td><td>-0.006*(-2.13)</td></tr><tr><td>(3) $\times$ Tenure $_{i,t}$ </td><td></td><td></td><td>-0.005(-1.20)</td><td>-0.005(-1.17)</td><td></td><td></td><td>-0.009(-1.38)</td><td>-0.012(-1.63)</td></tr><tr><td>(5) $\times$ Tenure $_{i,t}$ </td><td></td><td></td><td></td><td>-0.001(-0.56)</td><td></td><td></td><td></td><td>0.004(0.95)</td></tr><tr><td>(4) $\times$ Tenure $_{i,t}$ </td><td></td><td></td><td></td><td>-0.028(-0.55)</td><td></td><td></td><td></td><td>-0.063*(-2.07)</td></tr><tr><td>Project Category Control</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Effect Control</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: (1) Numbers in parentheses are t-statistics;  
(2) $^ { * * * } p < 0 . 0 0 1 , ^ { * * } p < 0 . 0 1 , ^ { * } p < 0 . 0 5 , + p < 0 . 1 ;$

## ACCEPTED MANUSCRIPT

Table 8. Robustness Check by Choosing 3 Lag Orders of Dependent Variables

<table><tr><td rowspan="2">Independent Variables</td><td colspan="8">Dependent Variables</td></tr><tr><td colspan="4"> $InvRewardTier_{i,t}$ </td><td colspan="4"> $InvTiming_{i,t}$ </td></tr><tr><td>(1):  $InvRewardTier_{i,t-1}$ </td><td>0.184***(6.55)</td><td>0.422*(2.13)</td><td>0.401*(2.17)</td><td>0.408*(2.14)</td><td>0.010(0.22)</td><td>0.238(0.71)</td><td>0.207(0.66)</td><td>0.277(0.86)</td></tr><tr><td>(2):  $InvTiming_{i,t-1}$ </td><td>0.002(0.37)</td><td>0.029*(2.00)</td><td>0.023*(2.01)</td><td>0.021+(1.84)</td><td>0.078***(11.29)</td><td>0.111***(4.51)</td><td>0.103***(5.13)</td><td>0.107***(5.42)</td></tr><tr><td> $ProTarget_{it}$ </td><td>-0.059***(-5.87)</td><td>-0.059***(-5.72)</td><td>-0.061***(-6.26)</td><td>-0.062***(-6.47)</td><td>-0.467***(-28.85)</td><td>-0.467***(-28.15)</td><td>-0.469***(-30.33)</td><td>-0.468***(-30.75)</td></tr><tr><td> $ProDesLen_{it}$ </td><td>0.027*(2.16)</td><td>0.022*(2.24)</td><td>0.021*(2.28)</td><td>0.022*(2.30)</td><td>0.016(0.79)</td><td>0.011(0.69)</td><td>0.010(0.63)</td><td>0.012(0.77)</td></tr><tr><td> $AccumSupPro_{i,t}$ </td><td>-0.114**(-2.59)</td><td>-0.114**(-2.60)</td><td>-0.116**(-2.65)</td><td>0.078***(11.38)</td><td>0.075(1.00)</td><td>0.075(1.01)</td><td>0.073(0.99)</td><td>0.130(1.46)</td></tr><tr><td> $Tenure_{i,t}$ </td><td>0.075**(3.24)</td><td>0.286+(1.82)</td><td>0.288+(1.82)</td><td>0.296+(1.82)</td><td>0.006(0.15)</td><td>0.213(0.81)</td><td>0.217(0.82)</td><td>0.265(0.97)</td></tr><tr><td>(3): AvgSupAmt $_{i,t}$ </td><td>-0.031***(-8.62)</td><td>-0.033***(-10.01)</td><td>-0.006*(-2.34)</td><td>-0.007*(-2.28)</td><td>0.651***(110.57)</td><td>0.649***(123.09)</td><td>0.685***(21.75)</td><td>0.698***(21.12)</td></tr><tr><td>(4):AccumNumUpdate $_{i,t}$ </td><td>0.007(0.28)</td><td>0.016(0.73)</td><td>0.016(0.73)</td><td>0.015(0.63)</td><td>0.488***(11.80)</td><td>0.497***(13.03)</td><td>0.497***(13.04)</td><td>0.717***(5.95)</td></tr><tr><td>(5):AccumNumComment $_{i,t}$ </td><td>0.031***(5.98)</td><td>0.028***(6.21)</td><td>0.028***(6.23)</td><td>0.037**(3.03)</td><td>0.458***(51.95)</td><td>0.455***(57.18)</td><td>0.455***(57.73)</td><td>0.421***(18.85)</td></tr><tr><td>(1) $\times$ Tenure $_{i,t}$ </td><td></td><td>0.053**(2.88)</td><td>0.050*(2.29)</td><td>0.059**(3.13)</td><td></td><td>-</td><td>-</td><td>-</td></tr><tr><td>(2) $\times$ Tenure $_{i,t}$ </td><td></td><td>-</td><td>-</td><td>-</td><td></td><td>-0.008+(-1.91)</td><td>-0.009+(-1.86)</td><td>-0.007+(-1.76)</td></tr><tr><td>(3) $\times$ Tenure $_{i,t}$ </td><td></td><td></td><td>-0.006(-1.40)</td><td>-0.005(-1.28)</td><td></td><td></td><td>-0.008(-1.18)</td><td>-0.011(-1.51)</td></tr><tr><td>(5) $\times$ Tenure $_{i,t}$ </td><td></td><td></td><td></td><td>-0.002(-0.79)</td><td></td><td></td><td></td><td>0.008(1.58)</td></tr><tr><td>(4) $\times$ Tenure $_{i,t}$ </td><td></td><td></td><td></td><td>-0.027(-1.18)</td><td></td><td></td><td></td><td>-0.053+(-1.87)</td></tr><tr><td>Project Category Control</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Effect Control</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: (1) Numbers in parentheses are t-statistics;  
(2) $^ { * * * } p < 0 . 0 0 1 , ^ { * * } p < 0 . 0 1 , ^ { * } p < 0 . 0 5 , + p < 0 . 1 ;$

## Biographical Statements

Shengsheng Xiao is an Assistant Professor at the Department of Management Information Systems, Shangha University of Finance and Economics. His research interests include enterprises information management, online crowdfunding markets, and supply chain financing. He has published in Information & Management, Decision Support Systems and others.

Qing Yue is an Assistant Professor at the Department of Business Management and Economics, Shangha University of International Business and Economics. Her research interests include data driven operations research and supply chain financing. She has published in the Journal of the Operational Research Society and others.

## Highlights

 Verify the existence of Inertia Behavior (IB) in investors’ reward tier and investment timing selection decisions in online crowdfunding market.

 Quantify and estimate the effect of this behavior by formulating a PVAR model.

 Investors’ IB in reward tier selection seems to be stronger than that in investment timing selection.

Investors’ platform tenure significantly accentuates their IB in reward tier selection, but weakens that in investment timing selection.

 Peer investors’ influence seems to have stronger impact on backers’ investment timing selection when compared with the fundraisers’ marketing efforts.
