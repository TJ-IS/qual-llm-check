---
otero_id: 21741
otero_key: "FEY5PWYF"
title: "Designing personalized intelligent financial decision support systems"
authors: "António Palma-dos-Reis; Fatemeh “Mariam” Zahedi"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00027-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing personalized intelligent financial decision support systems

Antonio Palma-dos-Reis <sup>a,2</sup>, Fatemeh ‘‘Mariam’’ Zahedi <sup>b,)</sup> ´

Instituto Superior de Economia e Gestao, Technical Uni˜ Õersity of Lisbon, Rua Miguel Lupi, 20, 1200 Lisbon, Portugal School of Business Administration, UniÕersity of Wisconsin-Milwaukee, P.O. Box 742, Milwaukee, WI 53201, USA

Accepted 12 May 1999

## Abstract

The variety of investment methods and the complexity of investment decisions have increased steadily in the last two decades. This growth has created a need for comprehensive and expandable financial decision support systems DSS thatŽ . embody major approaches toward investment decisions. The question is whether such systems should take into account the investor’s unique requirements and personal characteristics. The answer to this question is critical to the development of personal intelligent financial agents. In this paper, we present the design of such a system, the creation of a prototype, and its use in an exploratory investigation of the impact of investors’ individual characteristics on their use of models in making investment decisions. More specifically, we report on how the gender of investors, and their attitudes towards risk, relate to their choice of investment models, and provide evidence for the possibility of personalizing DSS. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Decision support systems; Financial DSS; Human<sup>r</sup>computer interaction; Risk attitude; Intelligent systems; Personalizing DSS

## 1. Introduction

Financial investment in stocks and bonds has attracted increasingly diverse groups, with varying goals and personal preferences. The volume of investment, the diversity of available options, and many investors’ lack of financial expertise call for the creation of decision support systems DSS toŽ . help individual investors make investment decisions.

There are a number of models designed to aid investors in selecting securities. In many cases, the investor does not have the technical knowledge necessary to choose an appropriate investment model. A support system aimed at aiding a diverse population must include various security selection methods, and should guide users in selecting model s useful for Ž . them. We posit that the system should have intelligent components for customizing and personalizing the system, based on the profiles and needs of investors, in order to guide them in selecting the appropriate methods for making investment decisions. Here, we explore the possibility of creating such systems.

Building a personalized intelligent DSS implies that investors’ personal characteristics have an impact on their preferences for different types of decision models. Therefore, prior to building the system, one needs to investigate whether personalization of DSS has any merit. This constitutes the focus of our research project. The answer to the question we raise in this paper has consequences far beyond the field of personal finance. If we consider intelligent agents as a type of intelligent DSS, our work could open the door to DSS types that are able to provide personal assistance by being responsive to the personalities of their users.

This paper reports the first phase of our project — designing the system, creating a prototype, exploratory data collection, and exploratory data analysis. Section 2 discusses the need for personalized DSS. Section 3 reports on the design of the personalized, intelligent, multiple-model, security selection DSS. Section 4 discusses the experiment design. Section 5 briefly reports on the experiment methodology. Section 6 describes the exploratory experiment results, and Section 7 presents our conclusions.

## 2. The need for personalized DSS

DSS are mainly used when decision-makers face an unstructured decision of major importance. Gonc¸alves et al. 14 found that the adoption of DSS <sup>w</sup> <sup>x</sup> technology by financial firms depends on the competitive pressures faced by the firm. However, the use of a DSS by individuals may depend on factors of a more personal nature.

There is some discussion in the literature of how an individual’s personality is reflected in his decision-making style. Kilmann and Mitroff 21 were <sup>w</sup> <sup>x</sup> among the first who discussed the importance of Jungian personality types in the managers’ views of their ideal organization. Land and Kennedy-Mc-Gregor 22 , in the context of informal elements of<sup>w</sup> <sup>x</sup> information systems, suggested that system designers could use the Jungian typology of decision-makers as models of human behavior. Davis et al. 9 also<sup>w</sup> <sup>x</sup> constructed four decision styles by combining the sensing–intuiting and thinking–feeling indexes of the Myers–Briggs Type Indicator MBTI . An analy-Ž . sis of variance of decision-makers’ cost performance showed statistically significant differences among the four decision styles. Stumpf and Dunbar 38 found that individuals with different personality types exhibit cognitive styles that are associated with specific patterns of choices. Ben-Zur and Wardi 3<sup>w</sup> <sup>x</sup> found that people with a Type A personality type are faster decision-makers than Type Bs. Type As more often use noncompensatory strategies, that is, they chose the alternative with the highest value for the most important dimension. In doing so, Type As filter the most important information 3 .<sup>w</sup> <sup>x</sup>

Research has already shown that DSS usage, satisfaction and performance may depend on a set of user-specific variables. Zinkhan et al. 43 identified risk aversion, cognitive differentiation, experience with DSS, managerial experience, age and involvement as factors explaining DSS usage and satisfaction. Alavi and Joachimsthaler 1 grouped the fac- <sup>w</sup> <sup>x</sup> tors determining DSS implementation success into cognitive style, personality, demographics, and user-situational variables. They carried out an extensive meta analysis in identifying the significant user-dependent factors for the success of DSS.

Huber 16 questioned the usefulness of cognitive<sup>w</sup> <sup>x</sup> style in the design of DSS and argued that cognitive styles are not a satisfactory basis for design guidelines. However, Huber 16 and Robey 30 observed that flexibility is a highly desirable feature in DSS design, in which users have the maximum choice over various aspects of the DSS. In our research, we discuss a DSS design that provides the maximum flexibility in using decision models. However, having the maximum choice puts a considerable burden on users to discover, understand, and select the options suitable for them. We report on the possibility of personalizing such a system, based on users’ characteristics. Our work has immediate application in developing personal intelligent agents.

We also develop an interface prototype for our system and collect exploratory data to investigate the possibility of personalizing DSS. In our experiment, we used a demographically homogenous sample of users with similar user-situational variables to explore the possibility that an individual’s personal characteristics may influence his use of software.

## 3. System design

A financial decision, especially the investment in securities, is one of the most important and complex decisions that diverse individuals engage in. Such decisions depend not only on market factors, but also on the investor’s preferences. There are a number of models developed to help the investor deal with market elements, but little guidance is provided to help the average investor choose the model best suited to him. These models by design do not deal with the investor’s preferences, because the underlying assumption in each model is that it is the only choice. Hence, a DDS for security selection not only should include all major security selection models, it also should be able to help the investor choose the best models, taking the user’s personality into account where appropriate.

The comprehensiveness of the system, taking the user profile into account when selecting the portfolio strategy and supporting multiple selection methods, requires this system to be designed as four subsystems, or system modules, that interact to accomplish the proposed results 27 . The system’s components<sup>w</sup> <sup>x</sup> are the meta selection module, personalizing and customizing module, the selection methodology module, and the database module. The classes implementing each of the modules are listed in Fig. 1.

Since flexibility and expandability are major requirements for a security selection DSS, we chose to use an object-oriented framework for the design of this system 27 . The object model for this system,<sup>w</sup> <sup>x</sup> presented in Fig. 2, shows the relationships between the objects listed in Fig. 1.

## 3.1. The meta selection module

The meta selection module provides the intelligent interface for the system. It takes into account the investor’s profile, which consists of customizing and personalizing information such as phase in life, personality type, investment goals and risk aversion. The finance literature already recommends the inclusion of some of these factors in making financial decisions see, for example, Refs. 4,37 . Ž <sup>w</sup> <sup>x</sup>.

![](/api/attachments/FEY5PWYF/fulltext/images/e7f0b4cfb265f7896bf811db3468f4b4a3f068150a49b98e00f345c19b539ef4.jpg)  
Fig. 1. Class list.

![](/api/attachments/FEY5PWYF/fulltext/images/f65419429525b3c0818972707993497ef10fa0eec7e1ae227ceb08e6bc5c2946.jpg)  
Fig. 2. Objects.

The intelligent interface interacts with other components. Once the investor’s profile is determined, it sends the information to the customizing and personalizing module in order to recommend security selection methods most suited to the investor’s needs and characteristics. The interface presents the recommendation to the user, who will make the final choice of method s . It then orders the methodology module to Ž . execute the methods selected by the user.

In order to recommend an investment strategy, the system matches the investor’s profile with a security selection strategy. In this procedure, the system considers strategy attributes, such as assumptions used in different selection models, their historical performance and variability of results. These attributes are then matched with the user’s attributes, defined as user-specified constraints, and the type of selection approach with which the investor feels most comfortable. Based on this match, the system recommends a strategy for the selection process. This module may also question the consistency of the data entered and propose changes in the constraints.

The interface presents the system recommendation in the form of a ranked list of methods and a proposed strategy. The user is given the choice of either accepting the system recommendation or selecting his own strategy. The user may define a new strategy by allocating percentages of the investment budget to different methods, or use the combined security selection strategy, which combines the outcome of various methods through a weighting scheme.

## 3.2. The selection methodology module

The selection methodology module executes the selection methodologies ordered by the meta selection module and proposes the actions that should be taken according to that methodology. Selection methodologies covered by this system are the capital asset pricing model CAPM , factor models, techni-Ž . cal analysis, fundamental analysis and neural networks.

The CAPM optimizes the return–risk ratio for a portfolio of securities. It selects a portfolio combining securities in pre-specified weights rather than selecting each security by its own features. The use of CAPM diversifies away the unsystematic risk, leaving the expected return of the portfolio as a linear function of systematic risk.

According to CAPM, all desirable securities and portfolios lie on the efficient frontier in the return– risk space, where risk is measured by the variance or standard deviation of return. The efficient set orŽ efficient portfolio frontier is defined as the set of. investment portfolios that have the minimum possible risk for a given expected return 31 . The portfo- <sup>w</sup> <sup>x</sup> lio proposed by CAPM is a point on the efficient frontier that maximizes the slope of the line going from the risk-free rate to the efficient frontier. Users who select the CAPM model rely on an optimization model, without knowing the exact mathematical structure of the selection procedure.

Factor models were developed based on the assumption that various economic factors have a different impact on each firm, and therefore its stocks and bonds 8,32 . According to this model, the actual<sup>w</sup> <sup>x</sup> return on a security is determined by its expected return as well as the macroeconomic factors that have impacts on the return of the security.

Several factors were identified in the literature, such as the business cycle, interest rates, the level of investor confidence, the short-term inflation rate, and the expectations for long-term inflation 15 . Chen et<sup>w</sup> <sup>x</sup> al. 6 found a number of variables that were impor-<sup>w</sup> <sup>x</sup> tant in explaining security returns, such as industrial production, changes in the risk premium, twists in the yield curve, unanticipated inflation and changes in expected inflation when inflation is highly volatile. Nicholson’s security selection model 39 takes into<sup>w</sup> <sup>x</sup> account several macroeconomic factors such as economic cycles, historical inflation rates, wage-rate trends, capacity utilization, monetary policy and the relationship between long-term and short-term rates.

While CAPM and factor models are portfolio strategies, that is, they propose a set of securities that are expected to perform well as a group, the other selection models technical analysis, fundamental Ž analysis and neural networks are security strategies,. that is, they select securities one-by-one in an independent fashion.

Technical analysis consists of a search for recurrent and predictable patterns in security prices, and implies the belief of market inefficiency. It may assume mathematical formulations, such as regression or ARIMA models, or may have graphical forms. Some strategies prescribed by the technical analysis are trend identification, use of moving averages, compared performance or relative strength and resistance<sup>r</sup> support levels 4 .<sup>w</sup> <sup>x</sup>

The fundamental analysis is based on company or security features that may lead to above-average performance. Ultimately, it attempts to determine the present discounted value of all the payments that a stockholder will receive from each share of a security 4 . Examples of attributes that may make securi-<sup>w</sup> <sup>x</sup> ties attractive are high ownership by management, low ownership by institutions, unique products, 20% or more annual growth in earnings potential and high-technology companies whose spending on research and development is rising compared to their market capitalization 35 . <sup>w</sup> <sup>x</sup>

David Nicholson, a hedge-fund manager, was able to achieve a notable performance by taking into account factors such as the price–earnings ratio, the price–cash flow ratio, the price–book value ratio and the cash reserves 39 . Other aspects considered in<sup>w</sup> <sup>x</sup> Nicholson’s analysis were macroeconomic factors Ž . used in the factor model and other company-specific variables, such as analysts’ revision trends, reported earnings compared to expectations, emotional factors, insider purchases, net purchases of mutual funds and market speculation.

Fama and French 11 describe a set of attributes<sup>w</sup> <sup>x</sup> or effects that may explain security returns or deviations from the returns expected by the Markowitz model 24 . These attributes include the small-firm<sup>w</sup> <sup>x</sup> effect, the equity effect, the leverage effect, and the earnings–price ratio.

Neural networks can model nonlinear relationships that other models are unable to capture. The use of neural networks in financial decision-making is growing rapidly 42 . According to Enrado 10 the<sup>w x</sup> <sup>w x</sup> use of neural networks by Mellon Equity Associates yielded fairly significant improvements in the security selection process. Wong et al. 40 designed the <sup>w</sup> <sup>x</sup> Intelligent Security Selection ISS system that in- Ž . cluded company, industry, economic, and country data. The data was processed by a neural-gate network, and combined the results with an expert system that contained company, industry and country rules.

The object-oriented nature of the design allows the possibility of adding more methods to the system. Expert systems in general, and case-based reasoning systems in particular, are among the methods that could increase the capability of the DSS for qualitative analysis of financial data for a discussionŽ of such applications, see for example, Refs. <sup>w</sup> <sup>x</sup> 23,36,41 ..

## 3.3. The database module

The database module stores the information required for the execution of the selection methodology module. It includes items describing the environment, such as the risk-free rate, factor data, and items describing the securities. The securities are described through market information, such as security prices, as well as through accounting informa tion, such as balance sheets or income statements.

## 3.4. The customizing and personalizing module

In designing a DSS that is responsive to the needs of its users, we distinguish two categories: customizing and personalizing. For customizing a DSS, it is important to take into account the situation-specific factors related to the user. In the design of our system, factors such as investment goal, desired duration of investment short-term or long-term , Ž . purpose of investment such as retirement or collegeŽ tuition would be the customizing aspects of the. system.

Another customizing component could be the familiarity of the user with the system. For example, a novice user may need more descriptive information, while an expert user may prefer shorter and faster responses. One may measure the familiarity construct by the history of use and the user’s skill. Yet another possible way of customizing could be asking the user’s preferences directly. Customization is not a new concept, but is a requirement for an intelligent financial DSS — a requirement that is not satisfied in most of the existing DSS.

Personalizing DSS takes customization one step further by accounting for the user’s personal characteristics that may be related to his preference for specific tools or methods.

Personalizing differs from customizing in several ways.

Ž . 1 Personalizing is based on the user’s characteristics, while customizing is based on the user’s experience with the software and its contents.

Ž . 2 Personalizing information may not change rapidly, while the customizing preferences of users may change as they become more familiar with the software or when their goals and needs change.

Ž . 3 Personalizing knowledge and rules should be accumulated from statistical analysis of data collected for various personality dimensions, while customizing information is collected directly from the user.

Ž . 4 Personalizing is based on statistical analysis, and therefore, is normally unknown to the user, while customizing is based on the customer’s knowledge of his or her own preferences and personal facts.

Ž . 5 Personalizing knowledge may have more universality in that it may be the same for a number of software products or various versions of the same product, while customizing depends on the particular version of the software being used.

Ž . 6 Personalizing may offer a greater productivity gain than customizing.

Data for customizing and personalizing the DSS are collected from the user by the intelligent interface, which asks a series of questions in the form ofŽ an expert system interface in order to populate the . personal database.

Our design contains an intelligent component that captures the existing knowledge regarding both customization and personalization of investment strategies. In customizing the system, the intelligent engine uses the customizing knowledge base, the constraints database constraints imposed by the user ,Ž . and the personal database. It thus uses the situational-specific information about the user and determines how to customize the system for him Fig. 2 . Ž .

The intelligent engine also uses the personalizing knowledge base and personal database to determine how to personalize the system for the user. The contents of such a knowledge base are the focus of our study. The possible relationship between a software system and its user’s personal characteristics is not explored in the literature. Therefore, in order to create a personalized intelligent DSS, we first need to establish if such a relationship exists, and if so, in what forms.

## 4. Experiment design

In investigating the possibility of personalizing DSS, we need to establish whether users with different personal characteristics would use models differently, and if so, how the personal features impact the use of the DSS models. To investigate the validity of our approach, we need to go through the following steps:

Ž .i Create a DSS or a prototype of a DSS that conforms to our design.

Ž . ii Identify some important personal characteristics that could give some indication of the validity of our approach in its exploratory phase.

Ž . iii Collect and analyze exploratory data for a preliminary indication of the possibility of personalization.

Ž . Ž . iv In case of positive results in iii , increase the scope of the personal characteristics and population types in order to show external validity and the possibility for generalizing the results.

In this paper, we report on the steps i – iiiŽ . Ž . above through the exploratory data analysis, and leave the confirmatory variable specification, data collection, and analysis to a subsequent report.

## 5. Exploratory experiment design

The exploratory phase of our work consisted of developing a DSS prototype, identifying the limited set of important personal characters, and collecting and analyzing exploratory data.

## 5.1. Prototype

In order to identify users’ preferences for security selection methodologies, we developed a prototype consisting of a part of the interface for our proposed system. The prototype contains a number of screens with options for viewing the recommendations or analysis provided by four investment models: the CAPM, factor, fundamental, and technical models. Although the design of our system allows for the use of neural networks in distinguishing complex patterns in the yield of a security, we chose not to include neural networks as a model in our prototype in order to reduce the number of choices and the complexity of explanation in our experiments.

The prototype was implemented as a Microsoft Access database, with Visual Basic Applications. The user is asked to invest US\$10,000 in stocks of six real US companies. The prototype then describes each one of the models to the user and guides the user in exploring recommendations or information provided by each one of four models, while allowing the user to go back and forth between the screens.

The description of each model is short and nontechnical. The CAPM screen states that ‘‘CAPM recommends a portfolio that has the best possible combination of high return and low risk, where risk is defined as the Õariability of return.’’ The CAPM model gives a pre-defined recommendation as to which stock should be selected and the proportion of investment in each stock.

The description of the factor model is: ‘‘Factor analysis recommends a portfolio that has the best possible combination of high return and low risk, where risk is defined as the uncertainty due to a set of economic factors.’’ The factor model menu also gives the user a pre-determined recommendation of three securities to buy in pre-specified proportions as an approximation for a factor-model recommendation.

The fundamental analysis screen presents a set of financial indicators to the investor and allows the investor to sort securities based on each one of the financial indicators by pressing a button. The financial indicators available are the price, the price–earnings ratio, the cash flow per share, the price divided by the cash flow per share, the book value per share, and the price divided by the book value per share. The fundamental analysis does not make specific recommendations, and it is up to the user to select the securities based on the financial indicators.

For each stock, the technical analysis shows a table and a graph with the historical values of its price and return. The returns are graphed against the market index in the same period. As in fundamental analysis, this screen does not make pre-determined recommendations. Fig. 3 contains a sample screen for the technical analysis.

The final screen asks the user to make his own investment decision. The user is asked to state the degree of his reliance on each model in making the final decision.

The models used in our prototype could be grouped into two categories: black-box and whitebox. CAPM and factor models are black-box portfolio-selection models, because the user relies solely on the description of the model and trusts that the underlying mathematical optimization or statistical analysis would make the best recommendation. Fundamental analysis and technical analysis are whitebox models, because they provide the user with relevant information without making a specific recommendation. A black-box model takes away the user’s control, and requires him to have faith in the theory, while a white-box model gives the user more control and consequently more responsibility in making the final decision.

## 5.2. Personal characteristics

Risk aversion is a widely accepted component of personality 1,43 . Since 1738, when Daniel Bernoulli <sup>w</sup> <sup>x</sup> reported the existence of risk aversion, people’s attitude toward risk has been a topic of growing interest in a number of disciplines, including economics, finance, decision theory, management, psychology, and even biology see, for example, Ref. 33 for aŽ <sup>w</sup> <sup>x</sup> critical review ..

![](/api/attachments/FEY5PWYF/fulltext/images/2769d3e75f64f402e287c01182d11bed4188c9d0fb1e027260a4c8a82b4efca7.jpg)  
Fig. 3. Sample screen for technical analysis.

In economics, finance, and decision theory, an individual’s attitude toward risk is specified in his utility function, which must satisfy von Neumann– Morgestern’s axioms 1947 . It has been shown that Ž . for an individual to be risk-averse, his utility function must be concave 20 p. 149 .<sup>w</sup> <sup>x</sup> Ž .

The use of variance or standard deviation as a measure of risk has its root in finance and economics. Markowitz 24 advanced portfolio theory by <sup>w</sup> <sup>x</sup> using variance of returns as a measure of risk. Variance and standard deviation have been used to measure risk in the management and finance literature Žsee for example, Refs. 5,12,25 . Although behav-<sup>w</sup> <sup>x</sup>. ior research has revealed biases in measuring risk through probabilistic outcomes 18,19,33 , variance<sup>w</sup> <sup>x</sup> and standard deviation remain the most widely used measures of risk.

Pratt 28 showed that when a decision-maker is<sup>w</sup> <sup>x</sup> indifferent between a risky $( Y _ { \mathrm { r } } )$ and risk-free $( Y _ { \mathrm { f } } )$ asset, the difference between the two is an ‘‘in surance premium’’, and is a function of variance:

$$
Y _ {\mathrm{r}} - Y _ {\mathrm{f}} = 0. 5 C \delta^ {2} + \text { terms   of   higher   order },\tag{1}
$$

where C is the measure of risk aversion, and terms of higher order depend on higher moments of the probability distribution of the risky choice see Ref.Ž <sup>w</sup> <sup>x</sup> 2 , pp. 95–96 ..

In finance, the risk aversion coefficient is measured as in see, for example, Ref. 4 :Ž <sup>w</sup> <sup>x</sup>.

$$
U = E (r) - C \sigma^ {2},\tag{2}
$$

where U is the investor’s utility function, $E ( r )$ is the expected return on the investment, $\sigma ^ { 2 }$ is the expected variance, and C is the risk aversion coefficient.

We used the standard deviation of risky rates of return as the measure of risk, in order to measure risk in the same unit as the rate of return. The questions were posed in the context of rate of return, and did not have any reference to total returns. This way, differences in utility for monetary assets would not impact the measurement of risk aversion. We defined the risk aversion level similar to Eq. 1 :Ž .

$$
\text { Required   Rate   of   Return } = R _ {\mathrm{f}} + \nu \sigma ,\tag{3}
$$

where $R _ { \mathrm { f } }$ is the risk-free rate, is the risk aversion level, and $\sigma$ is the standard deviation of the rate of return. We captured the value of when the respondent switches from a risk-free choice to a risky choice for the first time. This switch indicates that the respondent has just crossed his indifference point between the risk-free choice and risky choice, as described in the instrument design.

## 5.3. The instrument for measuring risk aÕersion

To measure users’ risk aversion, we designed an instrument to operationalize the risk aversion in Eq. Ž . Ž . 3 Appendix A . The instrument elicits risk aversion Ž . using nine questions. Each question offers the rate of return on two investment options, A and B. The first option is a risk-free choice A and theŽ . second option is a risky choice B ; the risky choiceŽ . offers a higher rate of return than the risk-free choice in all but one question. The standard deviation of all risky choices is fixed at about 0.038. Therefore, the only variation in choosing a risky option from one question to the next is the degree of the respondent’s risk aversion. Note that since the standard deviation of all risky choices is kept constant in our instrument, our measure of risk aversion in Eq. 3 isŽ . proportional to C in Eq. 1 .Ž .

A respondent with a lower risk aversion would be willing to settle for the risky choice with a rate of return closer to the risk-free rate; whereas a respondent with a higher risk aversion would require a higher rate of return to choose a risky option.

The questions were set up in such a way that, in the first five questions, a switch from the risky option to the risk-free option would indicate the degree of risk aversion. For example, in the first five questions, a respondent whose answers have the pattern B–A–A–A–A is more risk-averse than the one with B–B–A–A–A response pattern. The response pattern of $\mathbf { B } { - } \mathbf { B } { - } \mathbf { B } { - } \mathbf { A } { - } \mathbf { A }$ indicates that the respondent has even less risk aversion, because the risky asset with a lower expected return was selected.

To counter the effect of order in the first five questions, we have reversed the sequence in the last four questions, and, as the investor switches from a risk-free to risky choice, the risk aversion of the respondent is captured. For example, the response of A–A–A–B in the last four questions is an indication of lower risk aversion than A–A–B–B. Thus, we have elicited risk aversion twice.

If the first and second measures are equal, then the responses will be symmetric around the fifth question. That is, equal responses would have one of the following patterns:

$$
\cdot \quad \mathrm{A} - \mathrm{A} - \mathrm{A} - \mathrm{A} - \mathrm{A} - \mathrm{A} - \mathrm{A} - \mathrm{A} - \mathrm{A}
$$

$$
\cdot \mathrm{B-A-A-A-A-A-A-A-B}
$$

$$
\cdot \quad \mathrm{B} - \mathrm{B} - \mathrm{A} - \mathrm{A} - \mathrm{A} - \mathrm{A} - \mathrm{A} - \mathrm{B} - \mathrm{B}
$$

$$
\cdot \mathrm{B-B-B-A-A-A-B-B-B}
$$

$$
\cdot \quad \mathrm{B} - \mathrm{B} - \mathrm{B} - \mathrm{B} - \mathrm{A} - \mathrm{B} - \mathrm{B} - \mathrm{B} - \mathrm{B}
$$

$$
\cdot \quad \mathrm{B} - \mathrm{B} - \mathrm{B} - \mathrm{B} - \mathrm{B} - \mathrm{B} - \mathrm{B} - \mathrm{B} - \mathrm{B}
$$

The answers to the first five questions determine one observation for risk aversion — the point where the respondent switches from the risky investment to the risk-free investment. The last four questions provide a second observation for risk aversion — the point where the respondent switches from a risk-free option to a risky one. If the answers are not symmetric around the fifth question, then the two elicited values of risk aversion are not equal. In that case, we take the average of the two measurements.

While Eq. 3 does not impose any limit on the Ž . measure of risk aversion, we needed to limit our implementation of Eq. 3 to the interval 0–1 ;Ž . Ž . otherwise many more questions would be needed to measure risk aversion. To this end, we assigned the risk aversion value of 1 to the first pattern all As Ž . and 0 to the last all Bs . The patterns in betweenŽ . have a risk aversion of 0.8, 0.6, 0.4, and 0.2, respectively. These four risk aversion values are a simple linear transformation of Eq. 3 , with a factor ofŽ . about 0.76.

The justification for the assignment of 0 to the last pattern all Bs is based on the definition of riskŽ . aversion: ‘‘ a decision-maker is<sup>w</sup> <sup>x</sup> risk aÕerse if he prefers the expected consequence of any nondegenerative lottery to that lottery,’’ Ref. 20 , p. 149 . AŽ <sup>w</sup> <sup>x</sup> . nondegenerative lottery is defined as a lottery that does not have a result with probability 1. In our instrument, when the respondent chooses all Bs, including the fifth question, where the risky option B has the same expected value as the risk-free option A, the individual does not match the definition of a risk-averse person. Hence, his risk aversion measure should be 0.

Those respondents who do not choose any of the risky choices in the instrument selected all AsŽ . require higher rate of returns than offered in the instrument and are considered highly risk averse. Therefore, they receive 1 for risk aversion. This way, it is possible to limit the risk aversion interval to 0–1, while remaining faithful to the theoretical definition of risk aversion in Eq. 3 .Ž .

We performed pre-test experiments for testing the content validity and convergent validity of our instrument. The content validity test investigates whether the scale measures what it is expected to measure 13 , while the convergent validity test involves the degree of agreement among different measures of a construct 34 . In our case, the con-<sup>w</sup> <sup>x</sup> struct is the individual’s degree of risk aversion.

Our pre-test experiments involved 12 participants of diverse backgrounds. These individuals completed only the risk aversion instrument and answered three additional questions, as listed in Table 1. They did not participate in the subsequent experiments.

The three questions in Table 1 were designed to test the content validity of the instrument. The first two questions were used to establish that the instrument captured the direction of risk aversion correctly. We expected our risk aversion measure to have a positive correlation with the first question and a negative correlation with the second question. This was confirmed by the pre-test data.

In the third question, we expected our measure of risk aversion to have a negative and significant relation with the self-perception of individuals regarding their risk attitude. We purposefully used a question that was in the opposite direction of what we were trying to measure in order to avoid any possibility of bias, although it might have introduced the possibility of a measurement error in establishing the relationship. The measures of risk aversion had a significant Pearson correlation of <sup>y</sup>0.66, withŽ P<sup>s</sup> 0.021 with the answers to the third question in. Table 1.

Table 1  
Additional questions for instrument validity and scale reliability

<table><tr><td>Questions</td><td>Type of scale</td></tr><tr><td>In making financial decisions, I usually avoid risk (check one)</td><td>Five-item Likert Scale</td></tr><tr><td>In making financial decisions, I usually take risk (check one)</td><td>Five-item Likert Scale</td></tr><tr><td>Put a cross on the line to rate yourself as a risk taker in financial decisions: (0 = no risk at all, 10 = highly risk taker)</td><td>Continuous-line rating between 0 and 10</td></tr></table>

We also tested the convergent validity of the instrument in pre-test trials. Since we captured risk aversion twice through different sets of questions, we could test the convergent validity of the instrument via the correlation between the two measurements. In the pre-test experiments, the correlation between the two sets of risk aversion measures was 0.975, with $P = 0 . 0 0 1$ the internal reliability of the instrumentŽ was tested using the experimental data, as reported in Section 6 ..

## 6. Exploratory data collection and analysis

For this first phase of the data collection, we investigate the possibility of a relationship between model use and personal characteristics. The questions we posed were i whether the individuals haveŽ . different preferences for various types of models, and ii whether their attitudes toward risk, as well asŽ . gender and age, impact their use of models.

## 6.1. Data collection

We chose a demographically homogeneous population of users with similar user-situational variables for the exploratory data collection. Our sample consisted of 39 undergraduate students, who participated in the experiments on a voluntary basis with no remuneration. The students surveyed had the com puter skills to run the user-friendly interface without prior training and a general understanding of securities.

The students first completed the risk aversion instrument, and then used the prototype to make decisions regarding a hypothetical investment of US\$10,000 in six US companies. After the investment decision was made, the software asked the subjects to report which models they used in making their decisions, and how they weighted each of the models used. ‘‘None’’, meaning that no model was responsible for any portion of the decision, was one of the possible choices. This captured the relative weights assigned to each model in the decisionmaker’s final investment.

We present our exploratory findings in two segments. The first part discusses the use of the models, and the second part reports on the possibility of a relationship between model use and personal characteristics — risk aversion, gender, and age. Table 2 reports the summary statistics for the data.

## 6.2. The use of models

Table 2 shows the average weights assigned by participants to each of five models they could have used for making their final decisions: CAPM, Factor, Fundamental, Technical, and None. When a model was assigned a weight of 50% or more, we considered it to be a main model for the decision-maker, and computed the proportion of times each model was the main model for a decision-maker. Note that a decision-maker may not have a main model if he or she did not assign a weight of 50% or more to a model. Table 2 reports the summary statistics for the use of models as the main source: CAPM\_c, Factor\_c, Fundamental\_c, Technical\_c, and None\_c.

To examine the difference in the use of models, we tested two hypotheses:

Hypothesis 1:

H $_ { \cdot 0 } \colon$ all models received equal weights

$\operatorname { H } _ { 1 } { \mathrm { : } }$ models did not receive equal weights

Table 2  
Summary statistics

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td colspan="3">Models&#x27; weights</td></tr><tr><td>CAPM</td><td>30.846</td><td>22.053</td></tr><tr><td>Factor</td><td>18.564</td><td>16.396</td></tr><tr><td>Fundamental</td><td>20.718</td><td>19.550</td></tr><tr><td>Technical</td><td>25.436</td><td>23.431</td></tr><tr><td>None</td><td>4.436</td><td>10.787</td></tr><tr><td colspan="3">Use as a main model</td></tr><tr><td>CAPM_c</td><td>0.282</td><td>0.456</td></tr><tr><td>Factor_c</td><td>0.051</td><td>0.223</td></tr><tr><td>Fundamental_c</td><td>0.077</td><td>0.270</td></tr><tr><td>Technical_c</td><td>0.179</td><td>0.389</td></tr><tr><td>None_c</td><td>0.026</td><td>0.160</td></tr><tr><td>Number of models used:  $N_{models}$ </td><td>3.230</td><td>0.986</td></tr><tr><td colspan="3">Personal characteristics</td></tr><tr><td>Risk aversion</td><td>0.351</td><td>0.245</td></tr><tr><td>Gender</td><td>0.538</td><td>0.505</td></tr><tr><td>Age</td><td>20.538</td><td>2.901</td></tr></table>

Hypothesis 2:

$\operatorname { H } _ { 0 } { \mathrm { : } }$ all models were used equally as the main source

$\operatorname { H } _ { 1 } { \mathrm { : } }$ models were not equal in their use as the main source

We used a Chi-square, as described in Appendix B, to test the hypotheses 1 and 2 . Table 3 showsŽ . Ž . the test results. The hypothesis 1 was rejected forŽ . value at or above 0.0724, and hypothesis 2 was Ž . rejected for  value at or above 0.0119. Therefore, our experiments show that the four models were not equally used by the participants in making their investment decisions in this exploratory data set.

## 6.3. Personal characteristics

In our sample, subjects used on average 3.23 models in making their decisions $( N _ { \mathrm { m o d e l s } }$ in Table 2 . The average risk aversion level among the sub-. jects was 0.35. The survey was built to identify risk-aversion levels from 0 to 1, 1 being the highest degree of risk aversion. The subjects’ gender, which was coded as 1 for males and 0 for females, was about evenly distributed; 54% of our subjects were male while 46% of our subjects were female. Since all our subjects were business school students, the average age rounds to 20 years, with a moderate standard deviation. For the exploratory stage of our study, we chose a homogeneous population in order to reduce the impact of other factors in the data.

We tested the convergent validity of the risk aversion again using the experimental data. The correlation of the two measures of risk aversion was 0.75, with $p = 0 . 0 0 0 1$ , which provided evidence for the convergent validity for our measure. A factor analysis of the two measures of risk aversion was also loaded into one factor, which provided more evidence of convergent validity of the measures of risk aversion.

We also tested the internal consistency reliability of the risk aversion measure by the Cronbach Alpha test. Cronbach Alpha was 0.85, which is well above the cutoff value of 0.75 for exploratory experiments <sup>w</sup> <sup>x</sup> 26 .

## 6.3.1. Correlation analysis

In order to explore the relationship between the use of models and personal characteristics, we were interested in the pairwise correlation among the two sets of variables. In this discussion, a p value less than 0.10 is reported as statistically significant. Table 4 provides the Pearson correlation and the p values for each pair Appendix C provides justification ofŽ this test ..

Risk aversion and weights for Technical and None showed significant correlation Table 4 . The risk-Ž . averse decision-makers used the technical model more often positive significant correlation and as- Ž . signed less weight to None negative significantŽ correlation . Gender and three choices CAPM, Fac-. Ž tor, and None showed significant correlation Table. Ž 4 . Male decision-makers relied less on CAPM. Ž . negative significant correlation , and more on the factor model positive significant correlation , andŽ .

Table 3  
Chi-square tests of equality of models

<table><tr><td>Contrasts</td><td> $\chi^{2}$ </td><td> $df$ </td><td> $p$  value</td></tr><tr><td>Models&#x27; weights</td><td>6.984</td><td>3</td><td>0.0724</td></tr><tr><td>Use as main model</td><td>10.967</td><td>3</td><td>0.0119</td></tr></table>

Table 4  
Pearson correlation coefficients

<table><tr><td>Personal characteristics</td><td>CAPM</td><td>Factor</td><td>Fundamental</td><td>Technical</td><td>None</td><td> $N_{models}$ </td></tr><tr><td rowspan="2">Risk aversion</td><td>-0.1052</td><td>-0.1464</td><td>-0.0018</td><td>0.3653*</td><td>-0.3525*</td><td>0.2877*</td></tr><tr><td>p = 0.524</td><td>p = 0.374</td><td>p = 0.991</td><td>p = 0.022</td><td>p = 0.028</td><td>p = 0.076</td></tr><tr><td rowspan="2">Gender</td><td>-0.3302*</td><td>0.2833*</td><td>0.0744</td><td>0.1909</td><td>-0.3051*</td><td>0.0610</td></tr><tr><td>p = 0.040</td><td>p = 0.080</td><td>p = 0.653</td><td>p = 0.244</td><td>p = 0.059</td><td>p = 0.712</td></tr><tr><td rowspan="2">Age</td><td>-0.1106</td><td>0.0206</td><td>0.1503</td><td>-0.0965</td><td>0.1319</td><td>-0.0814</td></tr><tr><td>p = 0.503</td><td>p = 0.901</td><td>p = 0.361</td><td>p = 0.559</td><td>p = 0.423</td><td>p = 0.622</td></tr></table>

Significant correlation.

assigned less weight to the None category Table 4 .Ž . This shows a pattern of possible relationship between gender and the choice of models. Age did not show any significant correlation, which could be explained by the low variability in the age of respondents.

## 6.4. Discussion

In this phase of our research project, we developed a design for a flexible, intelligent financial DSS. We explored the possibility of personalizing such a system through lab experiments. In our exploratory data collection and analysis, we found that the personal features of the decision-makers are correlated with the models they choose for making decisions.

Although our analysis shows that the personal features, such as risk aversion and gender have impact on the use of models, the results have limited external validity because of the limited size of the sample, lack of group diversity, and limited number of personal variables 7,29 . In the next phase of this<sup>w</sup> <sup>x</sup> research, we will report on our experiments with sample data that do not have the above limitations and could have more general implications.

Such findings could be used to create the intelligent interface for personalizing the financial DSS or software agents. For example, once the intelligent interface measures the risk aversion of the user, it may offer a certain type of model as the primary decision tool, and provide him with detailed information on the nature of the model as well as an extensive support for using the model in making his financial decisions. One can see that this approach adds a new dimension to the development of DSS. In creating personalized DSS or personal intelligent financial agents, DSS developers will need to tailor the software to users’ specific personal characteristics. In doing so, they need to create a knowledge base by performing similar experiments on samples drawn from potential user populations. This makes it possible to add some degree of personalization to the systems.

## 7. Conclusions

This paper reported our research findings in investigating the feasibility of personalized intelligent DSS. To investigate this question, we developed the design of an intelligent financial DSS, which provides help in making investment decisions using a number of financial models. We incorporated the possibility of customizing and personalizing this design through an intelligent module and an intelligent interface. In order to populate the knowledge base for personalizing such a system, one needs to know whether users’ personal characteristics have any bearing on their behavior in using the DSS.

Since this question is broad and multidimensional, we set out first to explore the possibility of the existence of a relationship between a limited set of personal characteristics and the use of DSS; in this case, the use of models for making stock-selection decisions. We devised a prototype based on our design in order to carry out lab experiments, and chose a limited number of personal characteristics — risk aversion, age, and gender — for the exploratory phase of our study. We developed and tested a risk aversion instrument, in which we implemented the theory of risk aversion. Our pre-test data analysis showed an acceptable level of validity for the instrument.

We then carried out lab experiments from a homogeneous student body, analyzing the data to investigate whether there was a difference in the use of models, and if so, whether personal characteristics had any impact on their use. This phase of our investigation showed that the use of models was not the same, and that some models were more instrumental in aiding the decision-makers.

We observed some patterns of the possible relationship between model use and personal characteristics that we intend to investigate in a more comprehensive analysis. Risk aversion and gender showed some significant correlation with model choices. In the next phase of our study, we will explore these relationships for more diverse populations of users and a more extensive list of personality traits.

## Appendix A. The risk aversion instrument

ID:

For each investment, you are provided with the expected return, a pessimistic (Worst Case), and an optimistic (Best Case) return.

Which of these investments

(A or B) would you prefer?

Percentage return in 1 year:

<table><tr><td></td><td>A</td><td>B</td></tr><tr><td>Worst Case, 5% likelihood</td><td>5%</td><td>-3%</td></tr><tr><td>Expected</td><td>5%</td><td>9%</td></tr><tr><td>Best Case, 5% likelihood</td><td>5%</td><td>21%</td></tr></table>

Which of these investments

(A or B) would you prefer?

Which of these investments (A or B) would you prefer?

Which of these investments (A or B) would you prefer?

(A or B) would you prefer?

Percentage return in 1 year:

<table><tr><td></td><td>A</td><td>B</td></tr><tr><td>Worst Case, 5% likelihood</td><td>5%</td><td>-4%</td></tr><tr><td>Expected</td><td>5%</td><td>8%</td></tr><tr><td>Best Case, 5% likelihood</td><td>5%</td><td>20%</td></tr></table>

Percentage return in 1 year:

<table><tr><td></td><td>A</td><td>B</td></tr><tr><td>Worst Case, 5% likelihood</td><td>5%</td><td>-5%</td></tr><tr><td>Expected</td><td>5%</td><td>7%</td></tr><tr><td>Best Case, 5% likelihood</td><td>5%</td><td>19%</td></tr></table>

Percentage return in 1 year:

<table><tr><td></td><td>A</td><td>B</td></tr><tr><td>Worst Case, 5% likelihood</td><td>5%</td><td>-6%</td></tr><tr><td>Expected</td><td>5%</td><td>6%</td></tr><tr><td>Best Case, 5% likelihood</td><td>5%</td><td>18%</td></tr></table>

Percentage return in 1 year:

<table><tr><td></td><td>A</td><td>B</td></tr><tr><td>Worst Case, 5% likelihood</td><td>5%</td><td>-7%</td></tr><tr><td>Expected</td><td>5%</td><td>5%</td></tr><tr><td>Best Case, 5% likelihood</td><td>5%</td><td>17%</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="5">Percentage return in 1 year:</td><td></td></tr><tr><td></td><td>A</td><td>B</td><td></td><td></td><td></td></tr><tr><td rowspan="3">Which of these investments(A or B) would you prefer? _</td><td>Worst Case, 5% likelihood</td><td>7%</td><td>-4%</td><td></td><td></td><td></td></tr><tr><td>Expected</td><td>7%</td><td>8%</td><td></td><td></td><td></td></tr><tr><td>Best Case, 5% likelihood</td><td>7%</td><td>20%</td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td colspan="5">Percentage return in 1 year:</td><td></td></tr><tr><td></td><td>A</td><td>B</td><td></td><td></td><td></td></tr><tr><td rowspan="3">Which of these investments(A or B) would you prefer? _</td><td>Worst Case, 5% likelihood</td><td>7%</td><td>-3%</td><td></td><td></td><td></td></tr><tr><td>Expected</td><td>7%</td><td>9%</td><td></td><td></td><td></td></tr><tr><td>Best Case, 5% likelihood</td><td>7%</td><td>21%</td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td colspan="5">Percentage return in 1 year:</td><td></td></tr><tr><td></td><td>A</td><td>B</td><td></td><td></td><td></td></tr><tr><td rowspan="3">Which of these investments(A or B) would you prefer? _</td><td>Worst Case, 5% likelihood</td><td>7%</td><td>-2%</td><td></td><td></td><td></td></tr><tr><td>Expected</td><td>7%</td><td>10%</td><td></td><td></td><td></td></tr><tr><td>Best Case, 5% likelihood</td><td>7%</td><td>22%</td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td colspan="5">Percentage return in 1 year:</td><td></td></tr><tr><td></td><td>A</td><td>B</td><td></td><td></td><td></td></tr><tr><td rowspan="3">Which of these investments(A or B) would you prefer? _</td><td>Worst Case, 5% likelihood</td><td>7%</td><td>-1%</td><td></td><td></td><td></td></tr><tr><td>Expected</td><td>7%</td><td>11%</td><td></td><td></td><td></td></tr><tr><td>Best Case, 5% likelihood</td><td>7%</td><td>23%</td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td rowspan="2">In making financial decisions,I usually avoid risk (check one):</td><td>strongly agree</td><td>agree</td><td>neutral</td><td>disagree</td><td>strongly disagree</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>I usually take risk (check one):</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Put a cross on the line to rate yourself as a risk taker in financial decisions: (0=no risk at all, 10= highly risk taker) 上

## Appendix B. The Chi-square test

Since the assigned weights of the models are dependent, in that, assigning a higher weight to a model reduces the share of weights that can be assigned to the other models, we need to account for their covariance. The following multivariate Chisquare test accounts for the covariance of the variables in testing the equality of multiple means Ref.Ž <sup>w</sup> <sup>x</sup> 17 , Chapter 6 :.

$$
\chi^ {2} = n \left(\mathbf {C} \bar {\boldsymbol {X}}\right) ^ {\prime} \left(\mathbf {C S C} ^ {\prime}\right) ^ {- 1} \mathbf {C} \bar {\boldsymbol {X}}
$$

where n is the number of observations, C is the matrix with contrast coefficients in its rows, S is the sample covariance matrix, and $\overbar { X }$ is the vector of sample means. The vector $\mathbf { C } \bar { \mathbf { X } }$ contains estimates of contrasts or the pairwise means differences. In our case, C and $\mathbf { C } \overbar { \mathbf { X } }$ have the following form:

$$
\mathbf {C} = \left( \begin{array}{c c c c} 1 & - 1 & 0 & 0 \\ 1 & 0 & - 1 & 0 \\ 1 & 0 & 0 & - 1 \end{array} \right)
$$

$$
\text { and } \mathbf {C}   \overline {{\boldsymbol {X}}} = \left( \begin{array}{c} \overline {{\boldsymbol {X}}} _ {1} - \overline {{\boldsymbol {X}}} _ {2} \\ \overline {{\boldsymbol {X}}} _ {1} - \overline {{\boldsymbol {X}}} _ {3} \\ \overline {{\boldsymbol {X}}} _ {1} - \overline {{\boldsymbol {X}}} _ {4} \end{array} \right).
$$

## Appendix C. Justification of the correlation test

Note that the test of significance for Pearson correlation assumes bivariate normal distribution, which clearly does not hold for our data. For example, the binary nature of the Gender variable violates this assumption. In order to circumvent this problem, we ran the simple linear regression with each personal characteristic as the explanatory variable. This was possible because the underlying assumption of regression is that the dependent variable use ofŽ models in our case conditioned by the value of the. independent variable personal characteristics shouldŽ . have a normal distribution. With a large sample size, this assumption could also be relaxed. Since the Pearson correlation is the square root of $R ^ { 2 }$ with the same test value in this case, we chose to report correlation values and their tests in the following discussion, in order to make the presentation more intuitively accessible.

## References

<sup>w</sup> <sup>x</sup> 1 M. Alavi, E.A. Joachimsthaler, Revisiting DSS implementation research: a meta-analysis of the literature and suggestions for researchers, MIS Quarterly 16 1992 95–116.Ž .

<sup>w</sup> <sup>x</sup> 2 K. Arrow, Essays in the Theory of Risk Bearing, Amsterdam, North Holland, 1971.

<sup>w</sup> <sup>x</sup> 3 H. Ben-Zur, N. Wardi, Type A behavior pattern and decision making strategies, Personality Individual Differences 173 Ž . 1994 323–334.

<sup>w</sup> <sup>x</sup> 4 Z. Bodie, A. Kane, A. Marcus, Investments, 2nd edn., Irwin, Boston, MA, 1993.

<sup>w</sup> <sup>x</sup> 5 P. Bromiley, Testing a casual model of corporate risk taking and performance, Academy of Management Journal 34 1991 Ž . 37–59.

<sup>w</sup> <sup>x</sup> 6 N.F. Chen, R. Roll, S.A. Ross, Economic forces and the stock market,, Journal of Business 59 3 1986 383–403.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 T.D. Cook, D.T. Campbell, Quasi-Experimentation: Design and Analysis Issues for Field Settings, Rand McNally, Chicago, IL, 1978.

<sup>w</sup> <sup>x</sup> 8 T.E. Copeland, J.F. Weston, Financial Theory and Corporate Policy, 2nd edn., Addison-Wesley, 1983.

<sup>w</sup> <sup>x</sup> 9 D.L. Davis, S.J. Grove, P.A. Knowles, An experimental application of personality type as an analogue for decisionmaking style, Psychological Reports 66 1990 167–175.Ž .

<sup>w</sup> <sup>x</sup> 10 P. Enrado, Bank on neural networks, AI Expert 9 6 1994Ž . Ž . 56.

<sup>w</sup> <sup>x</sup> 11 E.F. Fama, K. French, The cross-section of expected stock returns, Journal of Finance XLVII 2 1992 427–465. Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 A. Fiegenbaum, Prospect theory and the risk–return association: an empirical examination of 85 industries,, Journal of Economic Behavior and Organization 14 1990 187–204.Ž .

<sup>w</sup> <sup>x</sup> 13 E.E. Ghiselli, J.P. Campbell, S. Zedeck, Measurement Theory for the Behavior Sciences, Freeman, San Francisco, 1981.

<sup>w</sup> <sup>x</sup> 14 V.FC. Gonc¸alves, A. Palma-dos-Reis, J. Duque, The impact of corporate strategy on the information system strategy: a survey of Portuguese financial corporations, Cadernos de Economicas, No. 2´ <sup>r</sup>97, ISEG — Instituto Superior de Economia e Gestao, Universidade Tecnica de Lisboa, 1997.˜ ´

<sup>w</sup> <sup>x</sup> 15 M.D. Griffiths, Factor analysis and risk modeling, Unpublished manuscript, University of Wisconsin-Milwaukee, 1992.

<sup>w</sup> <sup>x</sup>16 G. Huber, Cognitive style as a basis for MIS and DSS designs: much ado about nothing, Management Science 29 Ž . Ž .5 1983 567–579.

<sup>w</sup> <sup>x</sup> 17 R.A. Johnson, D.W. Wichern, Applied Multivariate Statistical Analysis, Prentice-Hall, Englewood, NJ, 1988.

<sup>w</sup> <sup>x</sup> 18 D. Kahneman, A. Tversky, Prospect theory: an analysis of decision under risk, Econometrica 47 1979 262–291.Ž .

<sup>w</sup> <sup>x</sup>19 D. Kahneman, P. Slovic, A. Tversky Eds. , Judgment UnderŽ . Uncertainty: Heuristics and Biases, Cambridge Univ. Press, Cambridge, UK, 1982.

<sup>w</sup> <sup>x</sup> 20 R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoff, Wiley, New York, NY, 1976.

<sup>w</sup> <sup>x</sup> 21 R.H. Kilmann, I.I. Mitroff, Qualitative versus quantitative analysis for management science: different forms for different psychological types, Interfaces 6 2 1976 17–27.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 F.F. Land, M. Kennedy-McGregor, Information and information systems: concepts and perspectives, in: R.D. Galliers Ž . Ed. , Information Analysis: Selected Readings, Addison-Wesley, Reading, MA, 1987, pp. 63–91.

<sup>w</sup> <sup>x</sup> 23 D. Leake Ed. , Case-based Reasoning: Experiences, Lessons,Ž . and Future Directions, MIT Press, Cambridge, MA, 1996.

<sup>w</sup> <sup>x</sup> 24 H.M. Markowitz, Portfolio Selection, Wiley, New York, 1959.

<sup>w</sup> <sup>x</sup> 25 K.D. Miller, J.J. Reuer, Measuring organizational downside risk, Strategic Management Journal 179 1996 671–691.Ž .

<sup>w</sup> <sup>x</sup> 26 J.C. Nunnally, Psychometric Theory, McGraw-Hill, New York, NY, 1978.

<sup>w</sup> <sup>x</sup> 27 A. Palma-dos-Reis, F.M. Zahedi, A general framework for developing financial decision-support systems, Proceedings of the Annual Meeting of the Decision Sciences Institute, Boston, 1995, pp. 465–467.

<sup>w</sup> <sup>x</sup> 28 J.W. Pratt, Risk aversion in the small and in the large, Econometrica 32 1964 122–136.Ž .

<sup>w</sup> <sup>x</sup> 29 E.J. Pedhazur, L.P. Schmelkin, Measurement, Design, and Analysis: An Integrated Approach, Lawrence Erlbaum, Hillsdale, NJ.

<sup>w</sup> <sup>x</sup> 30 D. Robey, Cognitive style and DSS design: a comment on Huber’s paper, Management Science 29 5 1983 580–582.Ž . Ž .

<sup>w</sup> <sup>x</sup> 31 R. Roll, A critique of the asset pricing theory’s tests, Journal of Financial Economics 4 1977 129–176.Ž .

<sup>w</sup> <sup>x</sup> 32 S.A. Ross, The arbitrage theory of capital asset pricing, Journal of Economic Theory 13 1976 341–360.Ž .

<sup>w</sup> <sup>x</sup> 33 P.J.H. Schoemaker, Determinants of risk-taking: behavioral and economic views, Journal of Risk and Uncertainty 6 Ž . 1993 49–73.

<sup>w</sup> <sup>x</sup> 34 L.F. Schoenfeldt, Psychometric properties of organizational research instruments, in: T.S. Bateman, G.R. Ferris Eds. ,Ž . Methods and Analysis in Organizational Research, Reston Publishing, Reston, VA, 1984.

<sup>w</sup> <sup>x</sup> 35 G. Smith, Welcome to the \$100,000 challenge, Business Week, December 27, 1993, 106–108.

<sup>w</sup> <sup>x</sup> 36 B. Smyth, P. Cunningham Eds. , Advances in case-basedŽ . reasoning, 4th European Workshop, Ewcbr-98, Dublin, Ireland, September 23–25, Proceedings Lecture Notes in Com-Ž puter Science by Ewcbr-9 , Springer-Verlag, London, 1998..

<sup>w</sup> <sup>x</sup>37 R.J. Stalla, The 1991 CFA II Review Course Outline, Vol. II, Stalla Seminars, Westlake, OH, 1991.

<sup>w</sup> <sup>x</sup> 38 S.A. Stumpf, R.L.M. Dunbar, The effects of personality type on choices made in strategic situations, Decision Sciences 22 Ž . 1991 1047–1069.

<sup>w</sup> <sup>x</sup>39 S. Taub, Nicholson: the black box made me do it, Financial World 162 16 1993 12.Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 F.S. Wong, P.Z. Wang, T.H. Goh, B.K. Quek, Fuzzy neural systems for stock selection, Financial Analysts Journal 48 1Ž . Ž . 1992 47–52.

<sup>w</sup> <sup>x</sup> 41 F.M. Zahedi, Intelligent Systems for Business: Expert Systems with Neural Networks, Wadsworth Publishing, Belmont, CA, 1993.

<sup>w</sup> <sup>x</sup> 42 F.M. Zahedi, A meta-analysis of financial applications of neural networks, Journal of Computational Intelligence and Organization 1 3 1996 164–178.Ž . Ž .

<sup>w</sup> <sup>x</sup> 43 G.M. Zinkhan, E.A. Joachimsthaler, T.C. Kinnear, Individual differences and marketing decision-support system usage and satisfaction,, Journal of Marketing Research 24 2 1987Ž . Ž . 208–214.

![](/api/attachments/FEY5PWYF/fulltext/images/ccf69a5d99ff3892489701de49a85f7bf09ea947f5e7d2ee5228ea704a29ef26.jpg)

Antonio Palma-dos-Reis is an Assistant´ Professor at the Instituto Superior de Economia e Gestao. At this institute, Dr.˜ Palma-dos-Reis is also a Member of the Directors Board and the Chairman for an Information Systems Graduate Program. He holds a PhD and a MSc in Management Information Systems from the University of Wisconsin-Milwaukee and a BA in Management Science from the Instituto Superior de Economia e Gestao, where he was designated for the˜

Eng. Antonio de Almeida award. Dr. Palma-dos-Reis research´ interests include information systems strategy, DSS and groupware.

![](/api/attachments/FEY5PWYF/fulltext/images/55eb5bbccdf774088bc328af4f1525d4e94f3dd9782a9cdcb7133790e29d21d5.jpg)

Dr. Fatemeh ‘‘Mariam’’ Zahedi is Wisconsin Distinguished Professor at the School of Business, University of Wisconsin-Milwaukee. She has received her doctoral degree from Indiana University. Her present areas of research include IS policy issues including quality, mainte- Ž nance and e-commerce , intelligent sys- . tems, and DSS. She has published in a number of journals, including: MIS Quarterly, Decision Sciences, IEEE Transactions for Software Engineering,

Operations Research, European Journal of Operational Research, Computers and Operations Research, Computational Intelligence and Organizations, Journal of Operational Research Society, Mathematical and Computer Modelling, Review of Economics and Statistics, Empirical Economics, and Socio-Economic Planning Sciences. She also has published two books.
