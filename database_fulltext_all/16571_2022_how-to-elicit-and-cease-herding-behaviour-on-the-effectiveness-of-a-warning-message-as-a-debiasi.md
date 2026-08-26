---
otero_id: 16571
otero_key: "SYUDRZHT"
title: "How to elicit and cease herding behaviour? On the effectiveness of a warning message as a debiasing decision support system"
authors: "Boukje Compen; Francisco Pitthan; Wouter Schelfhout; Kristof De Witte"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113652"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
How to elicit and cease herding behaviour?

On the effectiveness of a warning message as a debiasing decision support system.<sup>1</sup>

## Abstract

Behavioural economics has been argued to be a productive basis for decision support system (DSS) research. Whereas traditional economics assumes that individuals make decisions independently of others, behavioural economists have shown that humans tend to follow the crowd in their decisions (i.e., exhibit herding bias). However, the literature is silent on how convincing the information on the decisions of the crowd needs to be to elicit herding bias and on whether herding can be reduced (i.e., debiased) by presenting a warning message. This paper addresses both questions in the contexts of financial decisions that were guided by two DSSs in the form of simulation tools. In particular, we conduct a randomised controlled trial with 768 respondents randomly assigned to peer information. The results indicate that the intervention successfully elicited herding bias and that herding occurs when respondents are informed that at least 50% of other people made a particular decision. The results further show that a DSS in the form of a warning message is not sufficient to debias herding. In conclusion, these findings showed that individuals are easily influenced by erroneous peer information and that this effect is robust against debiasing using a warning message. Hence, DSS developers need to consider more intense debiasing strategies to overcome herding.

Keywords. Behavioural Economics; Cognitive bias; Debiasing; Financial decision making; Herding

bias; Randomised Controlled Trial

JEL-classification. G53; D91; G22

## 1. Introduction

In contrast to what is assumed in traditional economics, psychological factors such as cognitive biases, heuristics and emotions have been shown to lead to systematic and predictable deviations from rational decision-making (Baddeley, 2010; Huang et al., 2012; Thaler, 2000; Tversky & Kahneman, 1974). Behavioural decision theory, which analyses why and how decisions are made (Arnott and Gao, 2019), has shown that humans tend to “imitate each other’s actions and/or base their decisions upon the actions of others” (Spyrou, 2013, p. 175). Individuals herd when they believe that the ‘crowd’ is better informed than they are (Altman, 2013; Baddeley, 2010; Banerjee, 1992; Bikhchandani & Sharma, 2000), or because of an intrinsic preference for conformity (Cialdini & Goldstein, 2004; Goeree & Yariv, 2015). It has been argued that insights from behavioural economics should be integrated more intensively in decision support systems (DSS) research (Arnott & Gao, 2019; Huang et al., 2012).

However, it has been emphasised that ‘crowd wisdom’ could mislead knowledge formation, such that herding may not necessarily be a desirable decision strategy (Baddeley, 2013). A specific field where the cognitive bias of herding has been shown to play a role is in financial decisions related to stock market investment, entrepreneurship, risk preferences, retirement savings, and the use of government health insurance (Ahern et al., 2014; Brown et al., 2008; Bursztyn et al., 2014; Chatterjee et al., 2018; Duflo & Saez, 2002; Hong et al., 2005; Lahno & Serra-Garcia, 2015; Lerner & Malmendier, 2013). Indeed, it has been posited that especially in times of a rapidly growing share of financial products and services being offered online, individuals make sub-optimal financial decisions as they are increasingly vulnerable to “biased and unsubstantiated information from the web” (Bhandari et al., 2008, p. 399). Among other tactics, organisations may “strategically manage cues to generate a desirable herding effect among consumers to improve purchases and create value” (Ding & Li, 2018, p. 460). Furthermore, herding may distort collective decisions, as the herding behaviour of investors has been claimed to be one of the reasons for financial crises (Chari & Kehoe, 2004; Kabir, 2017). Consequently, individuals should be made aware of the potential influence of herding bias on their decision-making.

In the present study, we use a randomised peer information intervention to evaluate whether herding behaviour influences decision-making in the context of financial decisions, in particular buying disability insurance and retirement planning. As a basis for this study, we design a DSS that intends to support the decision-making of individuals in these specific contexts, noting the growing importance of DSSs for financial decisions (de Andrés Calle et al., 2020; Kraus & Feuerriegel, 2017). We also examine how convincing the information on the crowd’s decision needs to be before people start to demonstrating herding behaviour. Finally, we evaluate whether herding can be reduced by evaluating an additional DSS in the form of a warning message. Herewith, we aim to “provide decision makers with the additional capabilities to extend their bounds of rationality and thus, in turn, to eliminate or at least mitigate, the decision bias” (Cheng & Wu, 2010, p. 328), which has been noted to be of particular interest in the development of effective DSSs (Arnott & Gao, 2019; Aviad & Roy, 2012; Chai & Ngai, 2020; Shaikh, 2020).

In peer information interventions, individuals are informed about the decisions made by others, striving to induce social or observational learning. To our best knowledge, only one study thus far has used a peer information intervention to elicit herding in the personal finance context. This was a study by Beshears et al. (2015), who conducted an experiment using a peer information intervention aiming to increase the retirement savings of employees in a manufacturing firm. While it was hypothesised that informing employees about how many others were contributing a certain percentage of their income to a retirement plan would increase retirement savings, the results indicated that savings actually decreased among employees who did not yet have a savings plan. As these were often employees with relatively low incomes, it was suggested that these employees were discouraged by peer information indicating that higher income employees tended to have higher savings rates.

As a first contribution of the present paper, we evaluate whether a different peer information intervention might elicit the expected herding effects in the context of retirement planning decisions. In particular, we used a DSS to present personalised options to the respondents on the basis of respondents’ individual financial situations. Consequently, the ‘boomerang’ effect supposedly caused by upward comparisons, as identified in Beshears et al. (2015), was less likely to be of influence in the present study thanks to the DSS. Furthermore, to test the external validity of the findings, we also evaluated the impact of a highly similar DSS in the context of disability insurance decisions, as previous literature has presented mixed results regarding the impact of herding with respect to buying insurance (Chatterjee et al., 2018; Lieber & Skimmyhorn, 2018).

As a second contribution to the literature, this paper evaluates how convincing the peer information must be before herding behaviour is elicited. This is done by presenting the respondents with multiple random percentages in relation to peer choices. Peer information interventions have been shown to induce herding effects in various decision making situations, ranging from menu choices in a restaurant and sustainable behaviour in hotels to voting and charitable giving (Cai et al., 2009; Frey & Meier, 2004; Gerber & Rogers, 2009; Goldstein et al., 2008). Often, these interventions consist of informing people about the share of others who make a particular decision. Intuitively, the proportion of others they report should matter. However, few studies have provided the respondents with different magnitudes of peer information in this respect. Frey and Meier (2004) presented two different percentages to respondents (i.e., 46% and 64%) in their experiment to encourage charitable giving. Although they observed that contributions were larger for the group presented with the higher percentage, this result was not statistically significant. In Beshears et al. (2015), it was shown that a 1% increase in the proportion of peers contributing a certain amount to the retirement plan decreased the savings rate by 1.8%. However, only percentages of at least 72% were presented. This paper differs from those of Frey and Meier (2004) and Beshears et al. (2015) in presenting random percentages ranging from 10 to 90%, which allows us to evaluate when people start to follow the crowd.

As a third contribution to the DSS literature, this paper empirically examines whether a DSS in the form of a warning message can reduce the effects of herding bias. Hence, we make use of the one main advantages of DSSs, namely the “ability for the DSS developers to take into account the biases and limitations inherent in the decision-making process and design accordingly” (George et al., 2000, p. 204). Indeed, as most individuals are unaware of the potential influence of biases on their decisions (Scopelliti et al., 2015), efforts have been made to reduce or eliminate the influence of cognitive biases on decision-making, a process referred to as debiasing (Arnott, 2006; Cheng & Wu, 2010; George et al., 2000; Morewedge et al., 2015). The reasoning is that educating individuals about the influence of the decision context may not influence the attitudes and subjective beliefs of people (Chai & Ngai, 2020), but may also enhance the rationality of the decision-making process (Altman, 2012; Consumer Financial Protection Bureau, 2017). Besides, Arnott and Gao (2019) state that previous DSS research failed to address advances in behavioural economics, using out-of-date theories. Hence, we follow Bhandari et al. (2008) in evaluating a DSS that strives to reduce the negative impact of cognitive bias on the quality of the decisions using a debiasing approach. This could be considered challenging, due to the existing evidence on preference stability (Andersen et al., 2008; de Andrés Calle et al., 2020; Stigler, 1977). Four main types of debiasing techniques have been evaluated, which differ in terms of intensity and required effort: 1) a warning message on the possibility of bias; 2) a description of the bias and its direction; 3) personalised feedback on the individual’s behaviour; and 4) extensive training (George et al., 2000). Previous studies have evaluated the effectiveness of using debiasing strategies as basis for DSSs in relation to various cognitive biases, such as anchoring-and-adjustment bias, confirmation bias and framing effects (Cheng & Wu, 2010; George et al., 2000; Morewedge et al., 2015). However, no studies thus far have developed DSSs to attempting to reduce herding effects.

To attain our three research objectives, we conducted a field experiment on a website that guided financial decision making by providing independent financial education to the Belgian public.<sup>2</sup> The peer information intervention was linked to two DSSs in the form of simulation tools. Based on variables such as website visitors’ household income and job type, these DSSs indicated whether, in the case of becoming unable to work or retirement, an individual would require disability insurance or additional retirement savings, respectively, to complement their income. Website visitors were then presented with three types of insurance or retirement savings options. In the first step of this study, we established whether respondents could be herded towards a specific option. For respondents who were randomly assigned to the experimental condition, one of the three options was accompanied by peer information, indicating the percentage of others who chose this option. We hypothesised that the share of respondents choosing the herded option would be larger in the experimental condition than in the control condition, in which this information was not provided. The percentage shown in the present intervention was a random number between 10 and 90. This allowed us to more precisely determine the point where herding behaviour emerges. We hypothesised that the higher the percentage of peers shown to engage in the behaviour, the greater the likelihood that respondents would choose the herded option.

In the second step, we evaluated whether a DSS in the form of a warning message could reduce the impact of herding bias. Respondents in the experimental condition received a warning message after making their choice of one of the three options. This message contained information about the existence of herding bias and mentioned that the percentage shown in the intervention was randomly generated. Consequently, the message emphasised the potential risk of following the crowd when peer information is presented by commercial institutions. Respondents were then invited to reconsider their initial choice. We hypothesised that having become aware of herding bias, a share of respondents would indeed update their choice.

Our results indicated that the odds of choosing the herded option in the experimental condition were significantly larger than in the control condition, which confirms that a peer information intervention can elicit herding bias in financial decision-making contexts. The results further suggest that the peer information shown must indicate that at least 50% of others choose the targeted option for herding bias to occur, as the difference between the conditions was driven by respondents who were shown percentages between 50% and 89%. We did not observe that a warning message significantly influenced respondents’ preferences for the herded option. This implies that this DSS was insufficient to debiased the herding behaviour elicited. In sum, our paper sheds light on how easily individuals can be deceived by erroneous peer information, while the reducing of herding bias was shown to be challenging. To overcome the robustness of herding bias,

DSS developers should consider designing more intense DSSs than the warning message used in the present study to debias individuals.

The remainder of this article is organised as follows. In Section 2, we describe the methodology of the study, discussing the DSSs, the experimental design and the empirical analysis. Section 3 discusses the results. The discussion and conclusion are provided in Section 4.

## 2. Methodology

## 2.1. The decision support systems

To guide financial decision making, we developed a website with short informative articles and videos on financial products (e.g. on disability insurance and retirement planning) and two decision support systems (DSS) in the form of simulation tools.<sup>3</sup> The latter DSSs provided website visitors with personalised information on their income loss in the case of becoming unable to work, or when they plan to retire. These tools could be considered DSSs since they meet the definition of “computer technology solutions that can be used to support complex decision making and problem solving” (Shim et al., 2002, p. 111). The calculations in the DSSs were personalised based on information the respondents provided on household composition, work experience, income and job type. The DSSs also indicated whether website visitors could maintain their desired standard of living in either of these two situations. At the end of the DSSs, three general options for supplementary insurance or retirement savings were presented: Basic, Premium and Custom. These options are elaborated upon in Section 2.1.1. For each option, it was shown how much money the website visitor should save monthly to reach the desired income in the case of becoming unable to work or retiring.

Website visitors indicated their initial preference for one of the three options by clicking a button and were then forwarded to a page in which they can obtain more detailed information by making an appointment with a financial advisor. Panel A of Figure 1 presents the three options.

As part of the intervention of this study, a second DSS in the form of a warning message was integrated into the simulation tools in order to help individuals make unbiased decisions. Section 2.2 elaborates on the experimental design and the warning message.

## 2.1.1. Overview of Basic, Premium and Custom options

Following the DSS, respondents chose between three financial products: a Basic, Premium and Custom financial product. To set the scene, we show the working of the DSSs for the ‘average’ respondent: a single, 50-year-old individual without children, with a €2500 net salary, who is employed in the commercial sector, plans to retire at age 67, and is considering either additional retirement savings or buying income protection in the case of becoming unable to work.

In the disability insurance DSS, the respondent is asked to indicate which net income would be desirable to maintain throughout their career. By answering €2400 net – which is above the income level protected by social security and below the respondent’s net wage – the indicative costs of the Basic option are between €50 and €75. This option has a six-month waiting period before receiving income protection and offers a fixed settlement across the time of protection. The Premium option costs between €75 and €100, has a three-month waiting period, and a progressive settlement that increases over time. The Custom option allows the respondent to customise the product to their preferred parameters. Here, the respondent chooses the waiting time (between 1 and 12 months) and the settlement type (fixed, progressive or optimally progressive). By choosing the highest end option (one-month waiting period and optimally progressive settlements), the indicative costs are between €100 and €125.

In the retirement planning DSS, the respondent is asked to indicate what their desired net pension would be, and for how long they would like to receive this pension. To illustrate the DSS, assume an income of €2400 and a desired pension for 20 years. The Basic option offers conservative annual returns of 0.75% with no compensation for inflation in the additional monthly pension payments after retirement. The indicative savings are between €350 to €400 a month. The indicative costs for the Premium option are between €650 and €700, proposing the same 0.75% conservative annual returns, but with additional protection against purchasing-power losses due to inflation of up to 2% a year. The parameters for the Custom option are the desired annual interest (0% in a current account, or between 0.75% and 3%, depending on the respondent’s risk aversion), the desired inflation protection (from 0 to up to 2%) and the desired period in which the respondents would like to receive the payments (before retirement, after retirement or both). If the respondent chooses more conservative protection (0% interest rate, 2% inflation protection and payments both before and after retirement), the indicative costs are between €800 and €850. A riskier alternative (3% interest with no inflation protection and payments only after retirement) would imply that the respondent would need to save between €200 and €250 a month.

## 2.2. Experimental design

In line with Beshears et al. (2015), we strove to elicit herding behaviour by using a peer information intervention. As an outcome variable of the intervention, we measured respondents’ actual preferences as described in Section 2.1. After agreeing with the website’s privacy policy and terms of use, respondents were randomly assigned to a control condition or an experimental condition. To avoid returning visitors ending up in different treatment arms, and hence spill-over effects, the randomisation was based on internet cookies in the respondents’ internet browser.

Figure 1: Peer information intervention

A

## Basic

A basic protection that settles when adversity strikes. This allows you to live comfortably, in an uncomfortable situation.

Indicative costs € 50 - € 75 / month Excluding package deal (in combination with a pension saving plan you can often get up to 30% discount)

Add to my wish list

## Basic

A basic protection that settles when adversity strikes. This allows you to live comfortably, in an uncomfortable situation.

6-month waiting period

![](/api/attachments/SYUDRZHT/fulltext/images/0e9af431ca0bbb5bc2550e9006d58909e0ae82105de427f8704f6cf15acec376.jpg)

Fixed settlement

€ 50 - € 75 / month Excluding package deal (in combination with a pension saving plan you can often get up to 30% discount)

An income protection that meets all needs. A fast payment and you can also be assured concerning the future: the amount of the settlement increases.

Indicative costs € 75 - € 100 / month Excluding package deal (in combination with a pension saving plan you can often get up to 30% discount)

Add to my wish list

An income protection that meets all needs. A fast payment and you can also be assured concerning the future: the amount of the settlement increases.

3-month waiting period

Increasing settlement

## Premium

€ 75 - € 100 / month Excluding package deal (in combination with a pension saving plan you can often get up to 30% discount)

Add to my wish list

The way you want it. Completely customise the coverage so that it meets all your wishes.

Choose a waiting period

Choose a settlement

The way you want it. Completely customise the coverage so that it meets all your wishes.

Choose a waiting period

Choose a settlement

Excluding package deal (in combination with a pension saving plan you can often get up to 30% discount)

Add to my wish list

Note. Panel A shows the three options as presented to respondents in the control condition. Panel B shows the three options as presented to respondents in the experimental condition. The percentage shown in Panel B varied randomly between 10% and 90%.

The first step of the intervention examined whether herding bias is elicited in these financial decision-making contexts and provided insight into the necessary treatment intensity before respondents start demonstrating herding behaviour. Respondents in the control condition completed the DSS, indicated their preference for one of the three options and were forwarded to the page where they could schedule an appointment with a financial advisor. Respondents in the experimental condition completed the DSS in a similar manner as respondents in the control condition. However, when presented with the options, the Premium option was accompanied by an indication that a certain percentage of people chose that option. The percentage shown in this herded option was a randomly drawn number between 10 and 90. Panel B of Figure 1 shows an example from the disability insurance DSS.

Figure 2: Overview of the experimental design  
![](/api/attachments/SYUDRZHT/fulltext/images/14fbac89657424958483d179f0ccfb08934c2f14c03d023d4037e18e6a7104c9.jpg)

The second step of the intervention examined whether a DSS in the form of a warning message was an effective debiasing technique to reduce herding behaviour. Given that only respondents in the experimental condition were provided with the peer information, only these respondents were part of the second step. After respondents indicated which of the three options they preferred, the warning message popped up. This message aimed to increase respondents’ awareness of people’s innate tendency to follow the crowd and attempted to make them reflect on whether they were influenced by the peer information that was included for the herded option. The message revealed that the peer information was randomly generated and erroneous and that commercial institutions may similarly misuse the principles of herding bias to enhance the likelihood of people choosing particular products or services. Respondents could indicate whether and to which option they would like to change their initial preference. Figure 2 provides an overview of the two steps in the experimental design.

## 2.3. Econometric estimation

We estimated the extent to which we elicited herding bias and the impact of the warning message by using logit models. We created a binomial dependent variable: the decision to choose the herded option over choosing one of the alternative options. The resulting odds ratios provide insight into the influence of various factors (e.g., provision of peer information, respondents’ age) on the respondents’ preference for the herded option over the other alternatives. The effect of the peer information intervention on herding behaviour was evaluated by comparing the decisions of the respondents in the control condition and those in the experimental condition. We estimated the model using the following equation:

$$
Y _ {H e r d e d, 1} = \beta_ {0} + \beta_ {1} P e e r i n f o r m a t i o n + \beta_ {2} R e t i r e m e n t + \beta_ {3} X + \varepsilon
$$

where $Y _ { H e r d e d , 1 }$ reflects the decision to select the herded option (coded 1 when the respondent chose this option), ???????? ?????????????????????? is the treatment dummy identifying the two conditions (coded 1 when the respondent is in the experimental condition), ???????????????????? is the dummy variable that identifies which of the two DSSs was completed (coded 1 in case of the retirement DSS) and, finally, ?? refers to the set of covariates at the individual respondent level (i.e., age and household composition). The error term is captured by ??.

Given that respondents in the experimental condition were presented with a (random) percentage between 10 and 90% to indicate the share of others choosing the Premium option, we were also able to test whether herding is dependent on the percentage shown, using the following specification:

$$
\begin{array}{l} (2) Y _ {H e r d e d, 1} = \beta_ {0} + \beta_ {1} P I _ {1 0 - 2 9 \%} + \beta_ {2} P I _ {3 0 - 4 9 \%} + \beta_ {3} P I _ {5 0 - 6 9 \%} + \beta_ {4} P I _ {7 0 - 8 9 \%} + \beta_ {5} R e t i r e m e n t \\ + \beta_ {6} X + \varepsilon \end{array}
$$

Here, we created four dummy variables for the different percentage ranges, $P I _ { a \% - b \% } ,$ in which ???? is the abbreviation for peer information. We created the groups using 20% brackets to differentiate between the different levels in the strength of the peer information, while at the same time not inducing a major reduction in inference power. The dummies were coded 1 if the respondent was in the experimental condition and was presented with a percentage between the particular $a \% - b \%$ range.

The effectiveness of the DSS in the form of the warning message was evaluated using the following specification:

$$
\begin{array}{r l} Y _ {H e r d e d, t | P I = 1} & = _ {0} + \beta_ {1} W a r n i n g _ {t} + \beta_ {2} P I _ {3 0 - 4 9 \%} + \beta_ {3} P I _ {5 0 - 6 9 \%} + \beta_ {4} P I _ {7 0 - 8 9 \%} + \beta_ {5} R e t i r e m e n t \\ & + \beta_ {6} X + \varepsilon_ {t} \end{array} \tag {3}
$$

where $Y _ { H e r d e d , t | P I = 1 }$ refers to the decision of respondents in the experimental condition to choose the herded option, with the time indicator being equal to 1 when the decision was made before the warning message was shown, and 2 when the decision was made afterwards. The dummy $W a r n i n g _ { t }$ is coded 1 when it concerns the final decision (i.e., at time equals 2) and 0 when it concerns the initial decision (i.e., at time equals 1).

## 3. Results

This section starts with a description of how the final sample was deduced from the raw dataset. Subsequently, we assess the balance in the sample and descriptive statistics. Finally, we discuss the results of the various logit models.

## 3.1. Sample and attrition

In total, 8385 observations were collected in the two simulation DSSs. However, 2190 respondents started the same DSS more than once or completed both DSSs. To prevent learning effects, duplicates were removed based on respondents’ cookies and simulation identifiers. In these situations, we only include the data from the first DSS that was completed by the respondent. Furthermore, as is common in simulation tools, 88% of the remaining 6195 respondents did not fully complete the intervention. Respondents with incomplete data were also removed from the sample. This resulted in a final sample of 768 unique respondents who had fully completed the intervention. Of this sample, 428 (i.e., 56%) respondents were in the control condition, and 340 (i.e., 44%) in the experimental condition. From the total number of respondents, 465 (i.e., 61%) completed the DSS on disability insurance, and 303 (i.e., 39%) completed the retirement DSS. Given that the warning message was only presented in the experimental condition, the final choice was indicated by a maximum of 340 respondents. We note that 75 respondents (i.e., 22%) dropped out, resulting in a sample of 265 respondents.

To test for differential attrition, we ran a logit model based on an approach that is similar to Fryer Jr. (2016). The results indicated that the odds of dropping out were significantly larger for respondents who completed the retirement planning DSS and those in the experimental condition.

Interestingly, the likelihood of attrition appears larger for respondents in the lower percentage groups.

## 3.2. Descriptive statistics

For the final sample of 768 observations, we were able to derive information on the respondents’ age and household composition from the DSSs. Other variables were only obtained for a selection of the sample (i.e., gender and net wage), as these items were not needed in the DSSs. To examine the sample balance between the control condition and the experimental condition, we performed a sample composition analysis. The results are presented in Panel A of Table 1. Given that the t-statistic resulting from the independent t-test was only significant for the age group 18-25, with a larger share of respondents in this age in the experimental condition than in the control condition, we conclude that the sample was fairly balanced. Nevertheless, to account for potential imbalances, the background characteristics that were obtained for the full sample (i.e., age and household composition) were included as covariates in specifications used for the logit analyses.<sup>4</sup>

In Panel B of Table 1, we present the share of respondents choosing each of the three options. We observe that in both the control condition and experimental condition, the herded option was preferred by most respondents. This might be explained by the compromise effect, which refers to the consistent finding that the choice probability of an option tends to increase when it is the ‘middle option (Simonson, 1989). Furthermore, this finding may be due to the herded option being framed as the ‘Premium’ option, as this may result in perceptions of this option containing superior features relative to the other options (Brun & Castelli, 2013).

Nevertheless, the descriptive statistics suggest that the preference for the herded option was stronger in the experimental condition than in the control condition. The independent t-test indicated that this difference was significant at the 0.1% level. The greater share of respondents choosing the herded option results in a smaller share of respondents choosing Basic or Custom.

Figure 3: Share of respondents in each percentage range choosing the herded option  
![](/api/attachments/SYUDRZHT/fulltext/images/f8069360e16e53059f22d2d50333a9c1075753c3e2b36a5ce928757722e9a0db.jpg)

Since respondents in the experimental condition were presented with randomly generated percentages indicating the share of peers selecting the herded alternative, we were able to evaluate whether herding behaviour was influenced by the percentage that was shown. The descriptive statistics, visualised in Figure 3, indicate that generally – with the exception of the percentage range of 10-29% – the higher the percentage range, the higher the share of respondents choosing the herded option. In other words, the larger the ‘crowd’ making a particular choice, the more respondents followed this option. The graph further indicates that even a percentage in the lower ranges induces herding. This is surprising, as one would not expect that a low percentage – reflecting that a larger share chose one of the other options presented – would still enhance the probability of people choosing the herded option. This may be due to respondents not critically reflecting on the additional information presented. Nevertheless, it should be noted that this graph does not provide insight into whether the differences between the percentage ranges were statistically significant, and that in these initial analyses, differences in background characteristics were not yet controlled for.

Table 1: Descriptive statistics

<table><tr><td>Panel A:Analysis of balance in sample</td><td>Control condition</td><td>Experimental condition</td><td>t-test</td></tr><tr><td>Age</td><td></td><td></td><td></td></tr><tr><td>18 – 25</td><td>6.3%</td><td>10.3%</td><td>-2.02*</td></tr><tr><td>26 – 40</td><td>40.9%</td><td>37.9%</td><td>0.83</td></tr><tr><td>41 – 64</td><td>52.8%</td><td>51.8%</td><td>0.29</td></tr><tr><td>Household composition</td><td></td><td></td><td></td></tr><tr><td>Cohabiting</td><td>25.0%</td><td>26.2%</td><td>-0.37</td></tr><tr><td>Married</td><td>36.0%</td><td>37.3%</td><td>-0.39</td></tr><tr><td>Single</td><td>39.0%</td><td>36.5%</td><td>0.72</td></tr><tr><td>DSS</td><td></td><td></td><td></td></tr><tr><td>Retirement simulation</td><td>38.3%</td><td>40.9%</td><td>-0.72</td></tr><tr><td>N</td><td>428</td><td>340</td><td>768</td></tr><tr><td>Gender (male)</td><td>72.4%</td><td>63.6%</td><td>1.06</td></tr><tr><td>N</td><td>76</td><td>55</td><td>131</td></tr><tr><td>Net wage (in euros per month)</td><td>2064.56</td><td>2130.95</td><td>-0.91</td></tr><tr><td>N</td><td>283</td><td>214</td><td>497</td></tr><tr><td>Panel B:Division of choices per condition</td><td>Control condition</td><td>Experimental condition</td><td>t-test</td></tr><tr><td>Basic</td><td>34.8%</td><td>24.7%</td><td>3.04**</td></tr><tr><td>Premium (herded option)</td><td>40.9%</td><td>56.5%</td><td>-4.34***</td></tr><tr><td>Custom</td><td>24.3%</td><td>18.8%</td><td>1.82**</td></tr><tr><td>N</td><td>428</td><td>340</td><td>768</td></tr><tr><td>Panel C:Number of switched preferences</td><td>No switch</td><td>Switch</td><td></td></tr><tr><td>Basic</td><td>56</td><td>3</td><td></td></tr><tr><td>Premium (herded option)</td><td>153</td><td>6</td><td></td></tr><tr><td>Custom</td><td>46</td><td>1</td><td></td></tr><tr><td>N</td><td>255</td><td>10</td><td></td></tr></table>

Note. \* p ≤ .05 \*\* p ≤ .01 \*\*\* p ≤ .001.

Panel C in Table 1 provides a first indication of whether the warning message was an effective DSS to reduce herding bias, by evaluating the share of respondents changing their initial preference.

The descriptive statistics show that 6 of the 219 respondents (i.e., 3%) in the experimental condition decided to change their initial choice. Two thirds of these respondents had chosen the herded option before they were presented with the warning message. This is a first indication of herding bias having a persistent impact on financial decision-making, even when respondents are made aware of this bias.

## 3.3. Logit models

Table 2 presents the logit estimations that indicate whether the peer information induces herding bias. The dependent variable is the decision to choose the herded option rather than choosing one of the other two alternatives. Model 1 includes the peer information dummy to distinguish the control condition and the experimental condition. The significant odds ratio of 1.876 implies that the odds of choosing the herded option are 88% higher in the experimental condition than in the control condition.<sup>5</sup> Considering the fitted values, the probability of choosing the herded option is 38% higher when peer information is presented. Therefore, this estimate shows that the peer information elicited herding bias.

In Model 2, the overall treatment dummy is replaced by the dummies reflecting the different percentage groups indicating the share of others choosing the Premium option. This allows us to examine which percentage must be shown to elicit herding bias. Model 3 adds a dummy that reflects whether the data were collected in the disability insurance or the retirement planning DSS, as it is possible that respondents may be influenced by the peer information differently depending on the specific DSS that was completed. Models 4 and 5 control for heterogeneity in the sample by adding covariates reflecting the respondent’s age and household composition, respectively.

We observe that in Models 2-5 the odds ratios for the 50-69% and 70-89% groups are statistically significant. In Model 5, the odds ratio for the 70%-89% range is 2.464, which implies that the probability of selecting the herded option is 53% higher for respondents in this group compared to respondents in the control condition. Furthermore, the odds ratios (and significance levels) tend to increase when the percentage range increases. This does not hold when moving from the 10-29% to the 30-49% range, as the odds ratios are slightly lower in the latter. Nevertheless, these results confirm that the preferences of the respondents are influenced by peer information and that this influence is enlarged when they believe more people have chosen the herded option. From Models 3-5, we observe that the decision to choose the herded option was not influenced by the DSS that was completed. Among the covariates, the only significant variable was the age dummy from 26 to 40 years, which indicates that respondents in this group have a stronger preference for the herded option. Generally, however, the peer information appears to impact the choices of respondents of various ages and with different household compositions in a similar manner.

We also performed various robustness tests to find further evidence to explain our results. First, we ran logit models for the disability insurance and retirement planning DSSs separately. The results indicate that in the retirement planning DSS, the average herding effect is not significant; herding only occurs when peer information in the range of 70-89% is presented. Second, we ran a multinomial logit model. The estimates revealed that the pattern of results in the comparison between the Basic and the Premium options was similar to the pattern obtained in the comparison between the Custom and the Premium options. Third, we estimated a model in which, rather than use the 20% percentage ranges, we treat the peer information percentage as a continuous variable. We obtained a significant odds ratio of 1.011. We also checked for non-linearity by estimating a quadratic function, but the squared peer information variable was not significant.

Table 2: Logit model – effectiveness peer information intervention

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Peer information</td><td>1.876***(0.276)</td><td></td><td></td><td></td><td></td></tr><tr><td>10 – 29%</td><td></td><td>1.573(0.405)</td><td>1.568(0.404)</td><td>1.606(0.418)</td><td>1.601(0.417)</td></tr><tr><td>30 – 49%</td><td></td><td>1.560(0.383)</td><td>1.553(0.382)</td><td>1.542(0.382)</td><td>1.521(0.377)</td></tr><tr><td>50 – 69%</td><td></td><td>1.952***(0.450)</td><td>1.959**(0.452)</td><td>1.957**(0.454)</td><td>1.947**(0.454)</td></tr><tr><td>70 – 89%</td><td></td><td>2.410***(0.560)</td><td>2.390***(0.557)</td><td>2.415***(0.567)</td><td>2.464***(0.581)</td></tr><tr><td>Retirement DSS</td><td></td><td></td><td>1.152(0.173)</td><td>1.231(0.188)</td><td>1.217(0.187)</td></tr><tr><td>Age 18 – 25</td><td></td><td></td><td></td><td>1.383(0.386)</td><td>1.454(0.412)</td></tr><tr><td>Age 26 – 40</td><td></td><td></td><td></td><td>1.574**(0.248)</td><td>1.625**(0.260)</td></tr><tr><td>Single</td><td></td><td></td><td></td><td></td><td>0.848(0.148)</td></tr><tr><td>Cohabiting</td><td></td><td></td><td></td><td></td><td>0.746(0.145)</td></tr><tr><td>Constant</td><td>0.692***(0.068)</td><td>0.692***(0.068)</td><td>0.655***(0.075)</td><td>0.517***(0.073)</td><td>0.586**(0.099)</td></tr><tr><td>Pseudo  $R^2$ </td><td>.017</td><td>.020</td><td>.021</td><td>.029</td><td>.031</td></tr><tr><td>N</td><td>768</td><td>768</td><td>768</td><td>768</td><td>768</td></tr><tr><td> $X^2$ </td><td>18.50</td><td>21.19</td><td>22.08</td><td>30.70</td><td>33.08</td></tr><tr><td>p &gt; $X^2$ </td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td></tr></table>

Note. Reference categories: control condition, insurance simulation DSS, age 41-64, married. The coefficients represent odds ratios. Standard errors in parentheses. $^ { \ast } p \leq . 0 5 ^ { \ast \ast } p \leq . 0 1 ^ { \ast \ast \ast } p \leq . 0 0 1$

Table 3 presents the specifications for the second research objective, namely whether the DSS in the form of a warning message effectively reduces the impact of herding bias. The dependent variable corresponds to the decision to choose the herded option rather than the alternative options, conditional on having been presented with the warning message. The warning message dummy indicates whether the respondent’s choice was made before (i.e., the initial choice) or after receiving the warning message (i.e., final choice). Thus, the decision to choose the herded option before or after receiving the warning message is compared, integrating a time dimension, since the choice is time-dependent. The odds ratio observed in Model 1 is close to the value of 1 and not significant, suggesting that the DSS did not impact respondents’ preferences to choose the herded option.

Table 3: Logit model – Effectiveness of the warning message

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Warning message</td><td>0.969(0.172)</td><td>0.969(0.172)</td><td>0.969(0.173)</td><td>0.969(0.173)</td><td>0.968(0.174)</td></tr><tr><td>30 – 49%</td><td></td><td>1.044(0.272)</td><td>1.040(0.272)</td><td>1.070(0.283)</td><td>1.069(0.283)</td></tr><tr><td>50 – 69%</td><td></td><td>1.549(0.402)</td><td>1.539(0.401)</td><td>1.585(0.418)</td><td>1.632(0.434)</td></tr><tr><td>70 – 89%</td><td></td><td>1.737*(0.449)</td><td>1.735*(0.449)</td><td>1.776*(0.462)</td><td>1.824*(0.477)</td></tr><tr><td>Retirement DSS</td><td></td><td></td><td>0.948(0.174)</td><td>0.945(0.176)</td><td>0.938(0.175)</td></tr><tr><td>Age 18 – 25</td><td></td><td></td><td></td><td>1.676(0.511)</td><td>1.780(0.561)</td></tr><tr><td>Age 26 – 40</td><td></td><td></td><td></td><td>1.199(0.230)</td><td>1.289(0.256)</td></tr><tr><td>Single</td><td></td><td></td><td></td><td></td><td>0.942(0.209)</td></tr><tr><td>Cohabiting</td><td></td><td></td><td></td><td></td><td>0.720(0.168)</td></tr><tr><td>Constant</td><td>1.500**(0.221)</td><td>1.136(0.241)</td><td>1.163(0.249)</td><td>0.998(0.289)</td><td>1.066(0.289)</td></tr><tr><td>Pseudo  $R^2$ </td><td>.000</td><td>.010</td><td>.010</td><td>.015</td><td>.018</td></tr><tr><td>N</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td></tr><tr><td> $X^2$ </td><td>0.03</td><td>7.31</td><td>7.39</td><td>10.59</td><td>12.77</td></tr><tr><td>p &gt; $X^2$ </td><td>.859</td><td>.120</td><td>.193</td><td>.157</td><td>.173</td></tr></table>

Note. Reference categories: initial choice (i.e., before presentation of the warning message), 10-29% percentage group, insurance DSS, age 41-64, married. The coefficients represent odds ratios. Standard errors in parentheses. $^ { * } p \leq . 0 5 ^ { * * } p \leq . 0 1 ^ { * * * } p \leq . 0 0 1 _ { }$

Model 2 explores the potential heterogeneous impact across the different percentage ranges. The lowest percentage group (i.e., 10%-29%) serves as the reference category. It can be observed that, conditional on receiving the warning message, respondents in the 50-69% group are not significantly more likely to choose the herded option than respondents in the 10-29% group. Respondents in the 70-89% group, however, are significantly more likely to choose the herded option than respondents in the reference category. Models 3, 4, and 5 control for the type of DSS that was completed, the age of the respondent, and the household composition of the respondent, respectively. The results indicate that controlling for these variables only has a minor impact on the main odds ratios of interest, providing further evidence of the ineffectiveness of the warning message to reduce herding.

As a robustness test, we considered the decision to change the initial choice or not as the dependent variable. The results reveal a similar pattern to the main specification; that is, the warning message does not significantly influence people’s preference after being herded. We additionally evaluated whether limiting the sample to the respondents shown peer information in the ranges for which we found a significant herding effect (i.e., 50-69% and 70-89%) leads to a different conclusion regarding the effectiveness of the DSS, since these respondents received the most convincing – but erroneous – peer information. However, we found that the warning message did not significantly influence the likelihood of these respondents again indicating a preference for the herded option.

## 4. Discussion and conclusion

Given that cognitive biases have been shown to affect rational decision-making and may result in suboptimal decision-making, individuals should be made aware of the fact that they are susceptible to ‘biased and unsubstantiated’ online information. Therefore, this study aimed at examining whether and when herding behaviour influences decision-making in the context of financial decisions, and whether warning messages are an effective DSS to debias herding. To test the research questions, we conducted a randomised controlled trial in a real-life financial decision-making context with a sample of 768 respondents.

Our results indicated that the randomised peer information intervention was successful in eliciting herding behaviour in financial decision-making. Compared to the control condition, a significantly larger share of respondents in the experimental condition decided to follow the option that contained information on the share of people choosing that particular option. Specifically, the results of the logit analysis demonstrated that the odds of choosing this targeted option were approximately 88% higher in the experimental condition than the odds in the control condition. Considering the fitted values, this implies that the probability of choosing the herded option is 38% larger when presented with peer information. Thus, we showed that a DSS that includes peer information resulted in an enhanced share of respondents choosing the herded option, which confirmed our hypothesis. While this result aligns with previous studies which indicated that herding behaviour plays a role in the contexts of buying insurance and retirement planning (Chatterjee et al., 2018; Duflo & Saez, 2002), they contrast those of Beshears et al. (2015), in which the peer information intervention resulted in effects in the opposite direction hypothesised.

In the simulation tool DSSs, we have shown respondents a random number of people that was supposed to take a particular decision. Therefore, we were able to gain insight into how convincing the peer information had to be before people started to demonstrate herding behaviour. Our results showed that herding bias tended to occur when the information suggested that at least half of other people chose the targeted option. Compared to the control condition, the respondents who were shown peer information in the highest percentage range (70-89%) were 53% more likely to choose the herded option. In fact, we observed that the tendency to herd generally increased as the percentage shown increased. Thus, respondents who were shown a percentage between 70 and 89% were even more likely to choose the herded option than respondents who were shown a percentage between 50 and 69%, which seems an intuitive result. Given that Frey and Meier (2004) and Beshears et al. (2015) are the only studies that examine the differential impact of presenting multiple percentages, but were rather limited in the percentages shown, our results provide a highly relevant contribution to the existing literature.

Focusing on the effectiveness of presenting respondents with a warning message as a debiasing technique, the results indicated that this DSS was unable to reduce the effects of herding, as the preference for the herded option was not significantly influenced when respondents were informed about the fact that the percentage shown was randomly generated and that their initial decision might have been biased. A potential explanation for the robustness of the herding bias be related to a choice-supportive bias, which refers to the tendency to perceive the chosen option as more preferential and the non-chosen options as less preferential than they actually were (Lind, 2019). In other words, having made a particular decision, people tend to prefer to believe that this option was indeed the best choice after all. Consequently, they are less tempted to change their initial decision. Hence, this may have contributed to preference stability of the respondents, even after being presented with the warning message (de Andrés Calle et al., 2020). Since we only presented the peer information for one option, which was also susceptible to the compromise effect and framing effects (since ‘Premium’ may elicit the expectation that this is a high-quality option), this effect may have been enhanced. Similarly, the anchoring-and-adjustment bias possibly contributed to the ineffectiveness of the warning message to induce changes in people’s choices. The anchor of the peer information may have been strong enough to repeal the adjustments from the respondents’ own preferences and the warning message. The findings of previous studies that used a warning message as a basis for DSSs to reduce the effects of cognitive biases, namely the framing effect, hindsight bias, the anchoring and adjustment effect and the outcome effect, also showed mixed results on the effectiveness of the warning message as a DSS (e.g., Cheng & Wu, 2010; Clarkson et al.,

2002; George et al., 2000). Cheng and Wu (2010) suggested that the potential of warning messages may depend on the strength of the warning message itself and the type of bias on which it is focused.

In terms of implications for the DSS arena, our results provided additional evidence for the fact that peer information can induce herding behaviour. As mentioned by van der Werf et al. (2019, p. 197), “biases can provide useful starting points for designing interventions that steer people in the right direction”. In other words, people may be nudged towards the desired behaviour and decision (García & Vila, 2020). Given that peer information interventions require very little monetary investment, DSS developers and analysts are recommended to design and empirically evaluate DSSs in which peer information is used in an attempt to nudge individuals to make decisions or demonstrate behaviours that are in their best interests. In the development of DSSs with this nudging intention, the wide different set of preferences, biases and socio-economic conditions of individuals should preferably be taken into account, since the optimal decisions may differ strongly between individuals based on these influences. Although the present study focused on financial decisionmaking, existing research has shown that herding behaviour also influences decision-making processes in other contexts (Raafat et al., 2009). Finally, following Huang et al. (2012), designers of DSSs should include debias functions as part of the design in order to reduce those biases, but should account possible negative impacts of debiasing designs, such as confusion, annoyance and information loading. Therefore, nudging DSSs based on the provision of peer information could be considered in other contexts too.

However, providing individuals with information on the choices or behaviours of their peers could also be misleading and result in suboptimal decisions or behaviours. Our study showed that the impact of herding bias on respondents’ decisions overrules the impact of warning messages. Consequently, this suggests that DSS developers should take the robustness of herding bias into consideration in the design of DSSs. It appears that more intense DSSs are required to reduce or eliminate the effects of herding bias, and hence, to improve decision-making. Since other cognitive biases may have played a role in the difficulty to overcome herding, these should be taken into account in the development of future DSSs that strive to debias herding behaviour.

Although our study was not the first to conclude that the warning message did not suffice as a DSS to reduce or eliminate the influence of cognitive bias on the decision-making process, the design of our experiment may partly explain why only a few respondents chose to alter their initial choice. In particular, respondents did not have a clear incentive to switch their preference, which we consider a limitation of our study. Specifically, when clicking on the option they preferred, respondents did not immediately make a definitive choice to buy his product. Rather, the preferred option would be included in a final report that could be used when respondents met a financial advisor. Given that no direct monetary, or other incentive was involved, there were no potentially disadvantageous consequences of keeping the initially preferred option.

As a second limitation, we note that our design did not include a condition in which respondents did not receive a warning message but were still given the option to change their initial choice. While this would have allowed the assessment of the impact of the warning message in isolation, rather than a combined effect of offering an opportunity to change one’s decision and the warning message, we believed that this would be highly confusing to the respondents in this condition, as they would have been asked whether they wanted to change their choice immediately after indicating their preference. A final limitation of our study concerns the fact that we were unable to collect data on the financial knowledge of a sufficiently large share of the respondents to conduct correlational analyses. Future research is therefore recommended to explore whether or not there is a correlation between the individual’s level of financial knowledge and their sensitivity to herding bias. In the case that such a correlation does not exist, this may provide support for the assumption that cognitive biases may indeed be one of the causes of the general observation that even the decision-making processes of financially knowledgeable individuals are suboptimal. If, however, a correlation between financial knowledge and herding behaviour is established, it would be highly relevant to explore whether financial education could help reduce the impact of cognitive biases on financial decisions, considering the growing importance of financial literacy to behavioural biases (Pitthan & De Witte, 2021).

## References

Ahern, K. R., Duchin, R., & Shumway, T. (2014). Peer effects in risk aversion and trust. The Review of Financial Studies, 27(11), 3213–3240.

Altman, M. (2012). Implications of behavioural economics for financial literacy and public policy. The Journal of Socio-Economics, 41(5), 677–690.

Altman, M. (2013). What behavioural economics has to say about financial literacy. Applied Finance Letters, 2(1), 13–17.

Andersen, S., Harrison, G. W., Lau, M. I., & Rutström, E. E. (2008). Eliciting risk and time preferences. Econometrica, 76(3), 583-618.

Arnott, D. (2006). Cognitive biases and decision support systems development: A design science approach. Information Systems Journal, 16(1), 55–78.

Arnott, D., & Gao, S. (2019). Behavioral economics for decision support systems researchers. Decision Support Systems, 122, 113063.

Aviad, B., & Roy, G. (2012). A decision support method, based on bounded rationality concepts, to reveal feature saliency in clustering problems. Decision Support Systems, 54(1), 292-303.

Baddeley, M. (2010). Herding, social influence and economic decision-making: Socio-psychological and neuroscientific analyses. Philosophical Transactions of the Royal Society B-Biological Sciences, 365, 281–290.

Baddeley, M. (2013). Herding, social influence and expert opinion. Journal of Economic Methodology, 20(1), 35–44.

Banerjee, A. V. (1992). A simple model of herd behavior. The Quarterly Journal of Economics, 107(3), 797–817.

Beshears, J., Choi, J. J., Laibson, D., Madrian, B. C., & Milkman, K. L. (2015). The effect of providing peer information on retirement savings decisions. The Journal of Finance, 70(3), 1161–1201.

Bhandari, G., Hassanein, K., & Deaves, R. (2008). Debiasing investors with decision support systems: An experimental investigation. Decision Support Systems, 46, 399–410.

Bikhchandani, S., & Sharma, S. (2000). Herd behavior in financial markets. IMF Economic Review, 47, 279–310.

Brown, J. R., Ivkovic, Z., Smith, P. A., & Weisbenner, S. (2008). Neighbors matter: Causal community effects and stock market participation. The Journal of Finance, 63(3), 1509–1531.

Brun, A., & Castelli, C. (2013). The nature of luxury: A consumer perspective. International Journal of Retail & Distribution Management, 41(11/12), 823–847.

Bursztyn, L., Ederer, F., Ferman, B., & Yuchtman, N. (2014). Understanding mechanisms underlying peer effects: Evidence from a field experiment on financial decisions. Econometrica, 82(4), 1273–1301.

Cai, H., Chen, Y., & Fang, H. (2009). Observational learning: Evidence from a randomized natural field experiment. American Economic Review, 99(3), 864–882.

Chai, J., & Ngai, E. W. (2020). The variable precision method for elicitation of probability weighting functions. Decision Support Systems, 128, 113166.

Chari, V. V., & Kehoe, P. J. (2004). Financial crises as herds: Overturning the critiques. Journal of Economic Theory, 119(1), 128–150.

Chatterjee, C., Joshi, R., Sood, N., & Boregowda, P. (2018). Government health insurance and spatial peer effects: New evidence from India. Social Science & Medicine, 196, 131–141.

Cheng, F., & Wu, C. (2010). Debiasing the framing effect: The effect of warning and involvement. Decision Support Systems, 49(3), 328–334.

Cialdini, R. B., & Goldstein, N. J. (2004). Social influence: Compliance and conformity. Annual Review of Psychology, 55(1), 591–621.

Clarkson, P., Emby, C., & Watt, V. (2002). Debiasing the effect of outcome knowledge: The role of instructions in an audit litigation setting. Auditing: A Journal of Practice and Theory, 21(2), 1–14.

Consumer Financial Protection Bureau. (2017). Effective financial education: Five principles and how to use them.

de Andrés Calle, R., Cascón, J. M., & González-Arteaga, T. (2020). Preferences stability: A measure of preferences changes over time. Decision Support Systems, 129, 113169.

Ding, A. W., & Li, S. (2018). Herding in the consumption and purchase of digital goods and moderators of the herding bias. Journal of the Academy of Marketing Science 47, 460–478.

Duflo, E., & Saez, E. (2002). Participation and investment decisions in a retirement plan: The influence of colleagues’ choices. Journal of Public Economics, 85(1), 121–148.

Frey, B. S., & Meier, S. (2004). Social comparisons and pro-social behavior: Testing "conditional cooperation" in a field experiment. The American Economic Review, 94(5), 1717–1722.

Fryer Jr., R. G. (2016). Information, non-financial incentives, and student achievement: Evidence from a text messaging experiment. Journal of Public Economics, 144, 109–121.

García, J. M., & Vila, J. (2020). Financial literacy is not enough: The role of nudging toward adequate longterm saving behavior. Journal of Business Research, 112, 472–477.

George, J. F., Duffy, K., & Ahuja, M. (2000). Countering the anchoring and adjustment bias with decision support systems. Decision Support Systems, 29, 195–206.

Gerber, A. S., & Rogers, T. (2009). Descriptive social norms and motivation to vote: Everybody’s voting and so should you. The Journal of Politics, 70(1), 178–191.

Goeree, J. K., & Yariv, L. (2015). Conformity in the lab. Journal of the Economic Science Association, 1, 15–28.

Goldstein, N. J., Cialdini, R. B., & Griskevicius, V. (2008). A room with a viewpoint: Using social norms to motivate environmental conservation in hotels. Journal of Consumer Research, 35(3), 472–482.

Hong, H., Kubik, J. D., & Stein, J. C. (2005). Social interaction and stock‐market participation. The Journal of Finance, 59(1), 137–163.

Huang, H. H., Hsu, J. S. C., & Ku, C. Y. (2012). Understanding the role of computer-mediated counterargument in countering confirmation bias. Decision Support Systems, 53(3), 438-447.

Kabir, M. H. (2017). Did investors herd during the financial crisis? Evidence from the US financial industry. International Review of Finance, 18(1), 59–90.

Keren, G. (1990). Cognitive aids and debiasing methods: Can cognitive pills cure cognitive ills? Advances in Psychology, 68, 523–552.

Kraus, M., & Feuerriegel, S. (2017). Decision support from financial disclosures with deep neural networks and transfer learning. Decision Support Systems, 104, 38-48.

Lahno, A. M., & Serra-Garcia, M. (2015). Peer effects in risk taking: Envy or conformity? Journal of Risk and Uncertainty, 50, 73–95.

Lerner, J., & Malmendier, U. (2013). With a little help from my (random) friends: Success and failure in post-business school entrepreneurship. The Review of Financial Studies, 26(10), 2411–2452.

Lieber, E. M. J., & Skimmyhorn, W. (2018). Peer effects in financial decision-making. Journal of Public Economics, 163, 37–59.

Lind, M. (2019). Choice-supportive misremembering: A robust phenomenon? [PhD Dissertation]. University of Trento.

Morewedge, C. K., Yoon, H., Scopelliti, I., Symborski, C. W., Korris, J. H., & Kassam, K. S. (2015). Debiasing decisions: Improved decision making with a single training intervention. Policy Insights from the Behavioral and Brain Sciences, 2(1), 129–140.

Pitthan, F., & De Witte, K. (2021). Puzzles of insurance demand and its biases: A survey on the role of behavioural biases and financial literacy on insurance demand. Journal of Behavioral and Experimental Finance, 30, 100471.

Raafat, R. M., Chater, N., & Frith, C. (2009). Herding in humans. Trends in Cognitive Sciences, 13(10), 420- 428.

Scopelliti, I., Morewedge, C. K., McCormick, E., Lauren Min, H., Lebrecht, S., & Kassam, K. S. (2015). Bias blind spot: Structure, measurement, and consequences. Management Science, 61(10), 2468–2486.

Shaikh, S. E. (2020). Interactive and revisable decision-support: Doing more harm than good? Behaviour & Information Technology.

Shim, J. P., Warkentin, M., Courtney, J. F., Power, D. J., Sharda, R., & Carlsson, C. (2002). Past, present, and future of decision support technology. Decision Support Systems, 33(2), 111-126.

Simonson, I. (1989). Choice based on reasons: The case of attraction and compromise effects. Journal of Consumer Research, 16(2), 158–174.

Spyrou, S. (2013). Herding in financial markets: A review of the literature. Review of Behavioral Finance, 5(2), 175–194.

Stigler, G. J., & Becker, G. S. (1977). De gustibus non est disputandum. . The American Economic Review, 67(2), 76-90.

Thaler, R. (2000). From homo economicus to homo sapiens. Journal of Economic Perspectives, 14(1), 133–141.

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124–1131.

van der Werf, M. M. B., van Dijk, W. W., Wilderjans, T. F., & van Dillen, L. F. (2019). The road to the piggy bank: Two behavioral interventions to increase savings. In K. Sassenberg & M. L. W. Vliek (Eds.), Social psychology in action. Evidence-based interventions from theory to practice (pp. 195–204). Springer.
