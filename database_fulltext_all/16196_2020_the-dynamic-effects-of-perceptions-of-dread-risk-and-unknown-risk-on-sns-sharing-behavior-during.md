---
otero_id: 16196
otero_key: "TPR2KJ8Z"
title: "The Dynamic Effects of Perceptions of Dread Risk and Unknown Risk on SNS Sharing Behavior During Emerging Infectious Disease Events: Do Crisis Stages Matter?"
authors: "Liwei Xu; Jiangnan Qiu; Wenjing Gu; Yidi Ge"
year: "2020"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00612"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Dynamic Effects of Perceptions of Dread Risk and Unknown Risk on SNS Sharing Behavior During Emerging Infectious Disease Events: Do Crisis Stages Matter?

Liwei Xu<sup>1</sup>, Jiangnan Qiu<sup>2</sup>, Wenjing Gu<sup>3</sup>, Yidi Ge<sup>4</sup>

<sup>1</sup>Dalian University of Technology, China, xuliwei@mail.dlut.edu.cn <sup>2</sup>Corresponding Author, Dalian University of Technology, China, qiujn@dlut.edu.cn <sup>3</sup>Dalian University of Technology, China, 598228662@qq.com <sup>4</sup>Dalian University of Technology, China, gyidi0627@163.com

## Abstract

In response to the increasing prevalence of emerging infectious disease (EID) threats, individuals are turning to social media platforms to share relevant information in ever greater numbers. In this study, we examine whether risk perceptions related to user-generated content have dynamic impacts on social networking site (SNS) sharing behavior in different crisis stages. To answer this question, we applied psychometric analysis to evaluate how dread risk and unknown risk can characterize EID threats. Drawing broadly on the literature of risk perceptions, self-perception theory, and crisis stages, we relied on microblogs collected from Sina Weibo, utilizing the vector autoregression model to analyze dynamic relationships. We found that perceptions of dread risk have a dominant and immediate impact on SNS sharing behavior in the buildup, breakout, and termination stages of EID events. Perceptions of unknown risk have a dominant and persistent impact on sharing behavior in the abatement stage. The joint effect of these two types of risk perception reveal an antagonism impact on SNS sharing behavior, and perceptions of dread- and unknown risk have interaction effects from the buildup to termination stages of EID events. To check robustness, we analyzed keywords related to perceptions of dread- and unknown risk. The results of this study support the empirical application of Slovic’s risk perception framework for understanding the characteristics of EID threats and provide a picture of how perceptions of dread- and unknown risk exert differential time-varying effects on SNS sharing behavior during EID events. We also discuss theoretical and practical implications for the crisis management of EID threats. This study is among the first that uses usergenerated content in social media to investigate dynamic risk perceptions and their relationship to SNS sharing behavior, which may help provide a basis for timely and efficient risk communication.

Keywords: Emerging Infectious Disease, Risk Perceptions, Sharing Behavior, Dynamics, Self-Perception Theory, Vector Autoregression Model

Dorothy E. Leidner was the accepting senior editor. This research article was submitted on February 6, 2020, and underwent one revision.

## 1 Introduction

Emerging infectious disease (EID) outbreaks pose abrupt and unpredictable threats to global health, often bringing major economic losses and a general sense of dread in their wake (Abraham, 2007; Smith, 2006). Prominent examples of impactful EIDs include HIV,

Ebola, avian influenza A(H7N9) virus, Middle East respiratory syndrome coronavirus (MERS-Cov), Zika virus, and, most recently, COVID-19, which has caused a global crisis. As of April 28, 2020, the World Health Organization (WHO) has reported a total of 2,954,222 confirmed cases globally, and the situation remains uncertain to date (https://www.who.int/ emergencies/diseases/novel-coronavirus-2019/ situation-reports). However, COVID-19 represents only the most recent major EID outbreak; in addition to wars and famine, EIDs, which are often caused by newly identified species or strains to which individuals lack resistance, have long factored as one of the most significant threats to human survival, which is increasingly the case in an era of globalization (Morens, Folkers, & Fauci, 2004; Marston et al., 2014).

As the current COVID-19 outbreak illustrates, because the uncertainty associated with EIDs means that infection rates and outcomes are unpredictable, EIDs attract much public attention and often engender fear and even panic concerning whether the threat of disease can be controlled or eliminated (Stramer et al., 2009). Web 2.0 technologies, microblogging, and social media posts represent some of the main cathartic channels that individuals use to share their own stories, feelings, opinions, judgments, or evaluations about EIDs. This sharing behavior generates vast amounts of user-generated content (Stieglitz & Dang-Xuan, 2013) and can also facilitate the dissemination of information (Stieglitz & Dang-Xuan, 2013) concerning EID threats, potentially resulting in the emergence of new ways of evaluating the EID threats. Therefore, there is an urgent need to understand how the public perceives and shares information about EID threats on socia networking sites (SNS). Such information could help health agencies, such as the Centers for Disease Control (CDC) and WHO, understand the public reaction to EID threats and promote efficiency in the timely communication of risks. Previous researchers have analyzed the characteristics of crisis information based on information technology (IT). For example, risk maps illustrate incident locations associated with EIDs (Arab-Mazar et al., 2020; Haider et al., 2020), epidemic trends trace developments and public responses (Fong et al., 2020), and the frequency of relevant searches or keywords in user-generated content can be used to analyze the public reaction to a crisis event (Kim, Bae, & Hastak, 2018). Other work has focused on information networks (Pan, Pan, & Leidner, 2012), resource deployment (Leidner, Pan, & Pan, 2009), connective action (Vaast et al., 2017), and information flow (Day, Junglas, & Silva, 2009) related to crisis response. However, there remains little investigation into the characteristics of EID threat information and specific public responses to relevant EID threat information.

Although threat information disseminated on social media platforms and between health agencies can help address crises provoked by EIDs, the same information can also increase risk perceptions and inflame panic (Lupton, 1995). Individuals process physical signals (information) about potentially harmful events or activities and form perceptions and judgments about the seriousness, likelihood, and acceptability of the risks associated with the respective event or activity (Fischhoff, Bostrom, & Quadrel, 1993). They continually adjust perceptions as they acquire new information about the focal behavior (by observing others and their own behavior) (Bhattacherjee, 2001; Bem, 1972), and the adjusted perceptions provide a basis for subsequent behavior (Bhattacherjee, 2001). Stevenson and Taylor (2018) have pointed out that risk communication should consider the multistage process, which can be used in deciding how to prepare for and respond to a crisis. Comparing risk perception differences in distinct crisis stages may help generate a more accurate understanding of the public response. Therefore, the objective of our research is to study how risk perceptions of EID threats dynamically evolve and how they are related to public sharing behavior in different crisis stages.

Since social media functions as a sensor of society (Dave et al., 2013), the time-varying risk perceptions associated with EID threats conveyed on social media sites are associated with both good and bad effects: while they may provide accurate information for risk surveillance and precognition, they can also lead to negative behaviors such as the hoarding of supplies and the general economic paralysis of society. Understanding how risk is perceived by individuals and transmitted through institutions is fundamental to preparing for potential threats, which can help individuals take appropriate precautions to avoid health hazards and can minimize panic in the face of new or changing risks associated with a crisis (Slovic, 1987). Further, risk perceptions have a decisive role in SNS sharing behavior, with the effects varying in different crisis stages. Understanding such differences can theoretically enrich the crisis management literature, can practically assist in crisis response, and can promote efficient risk communication in online and offline contexts, thus potentially reducing the negative social impacts associated with risk perceptions.

We accomplish the proposed research objective through an exploratory study. We introduced psychometric analysis (Bhatia, 2019; Slovic, 1987; Wang, Xiao, & Rao, 2015) into the EID context, which uses dread and the unknown to describe the risk characteristics of EID threats. Drawing on the literature of risk perceptions, self-perception theory, and crisis stages, we used the vector autoregression model (Song et al., 2018) to analyze the interactions between perceptions of dread- and unknown risk as well as the dynamic effects of risk perceptions on sharing behavior in multistage EID events. This study evaluates both the joint effect of perceptions of dread risk and unknown risk as well as their separate impacts on SNS sharing behavior. Our research contributes to the IS domain by enriching and extending Slovic’s risk perception framework and the application of selfperception theory and we contribute to the crisis management literature through our use of the social media context. Our proposed framework may particularly benefit public health agencies in their attempts to formulate timely and efficient risk communication strategies aimed at reducing public uncertainty and panic during EID outbreaks.

The paper is organized as follows: we first provide a literature review and theoretical background. Then, we present the strategies of data analyses and estimation methods. Next, we discuss exploratory results and provide further analyses. Finally, we present some implications for theory and practice, followed by our conclusions.

## 2 Related Work and Theoretical Background

## 2.1 User-Generated Content Influence on Sharing Behavior

Previous studies have investigated the relationship between content characteristics and sharing behavior in diverse ways. As shown in Table 1, some studies have investigated the influence of emotions on sharing behavior using social media data or with field experiments, focusing especially on how positive emotions, negative emotions, and subcategories of emotions can shape sharing behavior. Other studies have identified the influence of topics, URLs, and hashtags on sharing behavior in different contexts (Pang & Law, 2017). However, few studies have thus far investigated risk perceptions in user-generated content, especially in the context of EID events.

Many risk perception studies have shown that the estimation of risk is a complex process, dependent on factors such as the context in which risk information is presented (Wolff, Larsen, & Øgaard, 2019) and the way that risk is described. While a recent study has also used survey data to analyze public risk perceptions (Oh, Lee, & Han, 2020), there is an urgent need to assess the precise role of perceived risk in inducing behavioral change. In the era of big data, it is difficult to use large-scale data about risk perceptions to measure the dynamic changes in public risk perceptions reflected in social media. Therefore, our paper bridges this gap in the literature by developing a model to analyze the time-varying risk perceptions in user-generated content and their relationships with sharing behavior.

Table 1. Reviews on the Relationships Between Content Characteristics and Sharing Behavior

<table><tr><td>Data source</td><td>Starting point</td><td>Result</td><td>Reference</td></tr><tr><td>Participants</td><td>Subcategories of emotions</td><td>Participants were more willing to share social anecdotes that arouse interest, surprise, disgust, or happiness.</td><td>Peters, Kashima, &amp; Clark, 2009</td></tr><tr><td>Participants</td><td>Arousal</td><td>Arousal increases the social transmission of information.</td><td>Berger, 2011</td></tr><tr><td>New York Times</td><td>Emotions and physiological arousal</td><td>Both articulated emotion and physiological arousal can influence the likelihood of articles to be shared.</td><td>Berger &amp; Milkman, 2012</td></tr><tr><td>Blogs</td><td>Emotions</td><td>Blog entries with either more positive or negative emotions tend to receive significantly more feedback than sentiment-neutral entries.</td><td>Dang-Xuan &amp; Stieglitz, 2012</td></tr><tr><td>Twitter</td><td>Quantity and speed of sharing behavior</td><td>Emotionally charged Twitter messages tend to be retweeted more often and more quickly.</td><td>Stieglitz &amp; Dang-Xuan, 2013</td></tr><tr><td>Twitter</td><td>Quantify positive and negative emotion effects</td><td>Positive and negative emotions have different effects on information diffusion.</td><td>Ferrara &amp; Yang, 2015</td></tr><tr><td>Social media platforms</td><td>Positive and negative emotions</td><td>Facebook statuses, Instagram, and Snapchat are mostly used for sharing positive emotions. Twitter and Messenger are also used for sharing negative emotions.</td><td>Vermeulen, Vandebosch, &amp; Heirman, 2018</td></tr><tr><td>Social media platforms</td><td>Positive and negative emotions</td><td>Ads that evoke positive emotions of inspiration, warmth, amusement, and excitement significantly stimulate positive social sharing.</td><td>Tellis et al., 2019</td></tr></table>

## 2.2 Self-Perception Theory

To investigate the dynamic influences of risk perceptions on SNS sharing behavior, we draw broadly on self-perception theory, which provides a framework for understanding individuals’ dynamic evolution of risk perceptions. Drawing on the literature on psychology and social psychology (Woosnam et al., 2018), self-perception theory uses individuals’ observations of information to analyze time-variant perceptions. Self-perception theory suggests that individuals dynamically and continually adjust their perceptions as they acquire new information about a focal behavior (by observing their own and others’ behavior) (Bhattacherjee, 2001; Bem, 1972); moreover, the adjusted perceptions then provide the basis for subsequent behaviors (Bhattacherjee, 2001). Hence, once the perceptions are updated, new perceptions replace previous perceptions as the basis for guiding individuals’ subsequent decision-making. Further, the modified decision behavior provides information a basis for subsequent perceptions of individuals, which illustrates the dynamic relationship.

Self-perception theory provides a dynamic perspective that differs from traditional modes of thinking based on a model with time-invariant relationships between perceptions and behavior (Dowling & Staelin, 1994; Thistlethwaite et al., 2018). Risk perceptions are the main perceptions of individuals in the social media context of EID events, and the relationships between risk perceptions and sharing behavior are not straightforward but exert various reciprocal feedback effects at different times: risk perceptions may motivate sharing behavior but, information accessed through social media sharing may also impact risk perceptions.

Our use of self-perception theory generates a dynamic perspective of risk perception analysis, enabling us to compare the evolution of risk characteristics; it also provides a theoretical foundation for subsequently using the evolution of risk perceptions to explain changes in SNS sharing behavior by considering the feedback effect of sharing behavior on risk perceptions.

## 2.3 Psychometric Analysis of Risk Perceptions

Risk perception is important in crisis response and management because it identifies which hazards people care about and how they deal with them (Wang et al., 2015). Psychometric analysis has been used for decades in psychology as the dominant theoretical framework for analyzing individuals’ risk perceptions (Bhatia, 2019) by identifying the underlying factors of risk characteristics and evaluating how these factors influence public reaction to hazards (both natural and human-made) (Wang et al., 2015). It encompasses a theoretical framework suggesting that individuals’ risk perceptions related to hazards can be described by a wide array of factors (Slovic, 1987) and has been used to examine diverse groups to show that psychometric scaling can identify and quantify similarities and differences in risk perceptions. Psychometric analysis is useful for evaluating why the public is concerned about some hazards, but not about others.

Slovic (1987) first proposed the risk perception framework and identified two underlying factors of risk characteristics based on psychometrics analysis: dread and the unknown. Unknown risk corresponds to the cognitive dimension and relates to people’s understanding of risks, whereas dread risk corresponds to the emotional dimension and relates to how people feel about risks. Moreover, dread risk is defined in terms of the potential for hazards to result in a lack of control, dread, and potentially catastrophic consequences. Dread risk typically corresponds to the perceived severity, vulnerability, and feelings of fear associated with a threat. Unknown risk is broadly defined in terms of hazards that are deemed unobservable, unknown, or new that are associated with delayed consequences. In other words, perceptions of unknown risk refer to unfamiliar risk issues that have lack of knowledge at their core (Bassarak, Pfister, & Böhm, 2017).

Risks and perceptions of risk that drive individual and societal responses to EID outbreaks include the probability of infection coupled with the potential consequences of infection (Medley & Vassall, 2017). Widespread fear associated with epidemics is generally driven by the lack of effective treatment; furthermore, if treatments are developed, individuals may harbor fears associated with the novel technologies used to treat epidemic diseases, which may subsequently contribute to higher levels of perceived risk. Uncertainty often increases public stress and fear because of the associated lack of control. Current literature has found that the extent to which a risk is unknown is independent of the extent of dread associated with a risk and the degree to which desire for strict risk-reducing policies is supported (Wang et al., 2015). However, when a situation is ambiguous, unpredictable, or probabilistic (Wolff et al., 2019), individuals experience uncertainty, which leads to feelings of dread (Armfield, 2006). Crisis events tend to invoke public uncertainty, which diffuses a feeling of dread throughout the population (Armfield, 2006). Furthermore, Slovic (1987) found that hazards perceived as uncontrollable, inequitable, involuntary, and potentially catastrophic tend to be perceived as risky. Therefore, in the context of a crisis event, perceptions of unknown risk may influence perceptions of dread risk, and the joint effect of these two types of risk perception may also impact sharing behavior.

In the EID events context, the characteristics of risk perceptions can be described along two dimensions: related experience/feeling and knowledge and event effects that are exposed and subject to time lag. These dimensions correspond to perceptions of dread- and unknown risk (Slovic, 1987). Our research applies psychometric analysis to the public reaction to EID events for two reasons. First, in contrast to traditional EID events literature that focuses primarily on the probability of occurrence and the magnitude of a specific threat (Herath & Rao, 2009; Liang & Xue, 2009), psychometric analysis considers risks to be multidimensional, with characteristics other than occurrence probability and severity (Boholm, 1998), which may allow for a richer description of EID threats. Second, psychometric analysis has become one of the most influential models in the domain of risk analysis. The extant literature primarily analyzes the static risk perceptions of diverse hazards or threats (Wang et al., 2015; Deng & Liu, 2017). However, research has thus far largely ignored the time-variant characteristics of a specific hazard or threat. Moreover, self-perception theory illustrates that individuals’ risk perceptions evolve dynamically. Therefore, we bridge this gap in the literature and compare risk perceptions of EID threats based on psychometric analysis.

## 2.4 Crisis Stages

Stevenson and Taylor (2018) suggest that risk communication should consider the multistage process that people use in deciding how to prepare for and respond to a crisis. Considering that nonpharmaceutical public health policies are vital in curtailing the spread of disease (Aledort et al., 2007), the multistage crisis process should account for the analysis or management of public risk perceptions.

Crises progress through a series of stages, each with its own set of dynamics and dimensions. One view defines this progression as “life cycle” (Fink, 1986). Fink (1986) and Sturges (1994) suggest that the life cycle of a crisis includes four crisis stages. The first is the buildup stage (Sturges, 1994), a period during which clues or hints begin to appear about a potential crisis. During this period, precursors to the crisis appear and the general public does not yet realize the severity of the crisis but is sensitive to threatening information. The second stage is the breakout stage (Sturges, 1994), during which a triggering event occurs, which may cause great physical, fiscal, and emotional trauma to society at large. At this point, widespread realization of the severity of the crisis and individual susceptibility develop and the public remains sensitive to dread-risk information, which may threaten the basic sense of public safety. The third stage, abatement (Sturges, 1994), is characterized by a public desire for more relevant knowledge about the crisis to balance widespread negative emotions associated with it. The last stage is the termination stage (Sturges, 1994), in which a final resolution signals that the crisis is no longer a public concern. During this period, public sensitivity to information decreases and stabilizes.

Crisis stages play a significant role in how IT is used in crisis response; this has been evaluated in relation to previous crises such as SARS (Leidner et al., 2009; Pan et al., 2012) and Hurricane Katrina (Pan et al., 2012). Crisis response is a continuous process that requires health agencies to make timely and targeted responses based on changes in the life cycle of a crisis. The level of public sensitivity to information is distinct (McKimm-Breschkin et al., 2007) in the four crisis stages. In other words, SNS sharing behavior may differ based on the stimulus of risk perceptions in the four crisis stages. This study evaluates crisis stages in relation to risk perceptions and sharing behavior and provides stage-based information and mechanisms that may be useful for generating effective risk communication and crisis response.

## 3 Methodology

Our analysis includes three steps: data acquisition, data processing, and the introduction of an estimation model. First, we used a web crawler to obtain relevant microblogs related to avian influenza from Sina Weibo between February 2013 and June 2013. Second, we used a Chinese natural language processing tool to process microblog data. We used Chinese Lin Hongfei ontology (Xu et al., 2008) and the traditional Chinese version of the Linguistic Inquiry and Word Count (CLIWC) dictionaries (Huang et al., 2012) to extract risk perceptions and emotions from microblogs. To analyze dynamic effects, we aggregated a measure across all microblogs within the time window to create time-series data. Finally, we tested the stationarity of the different time series and constructed the VAR model.

## 3.1 Data Collection and Context Description

EID events have three categories (Marston et al., 2014; Sun & Wang, 2009): (1) diseases previously known as noninfectious—for example, peptic ulcers and adult Tcell lymphoma—are sometimes redefined as emerging infectious diseases; (2) diseases known as emerging infectious diseases in modern times, such as the Hepatitis C virus, Lyme disease, and Legionnaires disease; (3) newly emerging, previously unknown infectious diseases, such as avian influenza A(H7N9) virus, Zika virus, SARS, and COVID-19.

![](/api/attachments/TPR2KJ8Z/fulltext/images/2b177aa8237c8dcc07eaa8de853c579ecfb8b92689e80471a29a13185def3928.jpg)  
Figure 1. Example of User-Generated Content in Sina Weibo

We collected Sina Weibo microblog data on avian influenza A(H7N9) virus (Category 3) because this event received extensive public attention, which led to an abundant number of microblogs. Since the disease’s emergence in China on February 19, 2013, it has resulted in the 217 human infections and 57 deaths, characterized by rapidly progressive pneumonia, acute respiratory distress syndrome, and respiratory failure. The biological features of the virus and its pandemic potential caused global concern. By April 2013, although the epidemic declined quickly after the closure of live poultry markets, new cases in humans were still emerging and the stream of public opinion on Chinese SNS platforms did not slow down until June 2013. We searched related microblogs by inputting keywords and selecting time intervals in Sina Weibo. We searched hour-by-hour because that is the minimum time interval allowed. For example, we used the time period of 9:00-10:00 on June 9, 2013, and inputted the keywords “H7N9,” “avian influenza,” “flu,” “vaccine,” “symptom,” “syndrome,” and “illness” to locate related microblogs posted during this time period. In all, we found 565,427 microblogs between February 19, 2013, and June 15, 2013.

Figure 1 shows an example of a post. We collected the username, contents of microblog, time of usergenerated content, posting number, and reposting number.

## 3.2 Data Processing

As the Chinese language does not use spaces between words, we first chose the Chinese Academy of Science segmentation system NLPIR (Natural Language Processing and Information Retrieval), one of the best systems for Chinese word segmentation, to preprocess microblogs (Zhang et al., 2014). This process includes word segmentation and stop word deletion. We should note that the segmentation accuracy of NLPIR is more than 95% (Zhang et al., 2014). The word series of each microblog after segmentation and stop word deletion was $\{ w _ { 1 } , w _ { 2 } , \ldots , w _ { q } \}$

In the following, we used the Lin Hongfei ontology and CLIWC dictionaries to extract perceptions of dread- and unknown risk, positive emotions, and negative emotions.

## 3.2.1 Dependent Variables

Definition 1: Feature vector of sharing behavior. For the purposes of our study, sharing behavior is a type of information behavior characterized by the public sharing of information with others (Oh & Syn, 2015) through posting or reposting on a social networking site. We define sharing behavior as an action that provides information such as risk perceptions to other community members who may need it (Park et al., 2014). The numbers of posts and reposts have become an important measure of information sharing. The construct ??ℎ??????????????ℎ??????????<sup>(n)</sup> represents the sharing behavior for microblog n and consists of posting {??????????????<sup>??</sup>} and reposting {??????????????????<sup>??</sup>} for microblog n, as shown in the following formula:

$$
\begin{array}{c} \text {sharingBehavior} ^ {(n)} = \\ \left[ \begin{array}{c} p o s t i n g ^ {1} + r e p o s t i n g ^ {1} \\ p o s t i n g ^ {2} + r e p o s t i n g ^ {2} \\ \vdots \\ p o s t i n g ^ {n} + r e p o s t i n g ^ {n} \end{array} \right] \end{array}\tag{1}
$$

## 3.2.2 Independent Variables

We conducted psychometric analysis to identify perceived risk characteristics of hazards shared among individuals. In the previous psychometric paradigm for studying risk perceptions, individuals are asked to evaluate the riskiness of various risk sources and make judgments about the risk sources (Bhatia, 2019). However, it is difficult to measure the dynamic characteristics of risk perceptions through surveys, especially in the big data era. Mass media have long been considered to be important shapers of public risk perceptions (Snyder & Rouse, 1995). User-generated content in social media is an important basic medium that people use to express their attitudes, reactions, and perceptions of EID threats (Chen et al., 2019; Fung et al., 2013). Therefore, we chose user-generated content to measure public risk perceptions. Previous research has used the number of people affected as the measurement of the “magnitude” of perceived dread- and unknown risk (Boholm, 1998). In other words, the more people that perceive dread- and unknown risk, the larger the magnitude of public risk perceptions. Therefore, we used the number of words expressing perceptions of dreadand unknown risk to measure risk perceptions, assuming that the more words used that connoted perceptions of dread risk or unknown risk, the higher the level of perceived risk. There are two dimensions that sufficiently represent risk characteristics, including dread risk and unknown risk. We define these two variables in Definition 2 and 3 below.

Definition 2: Feature vector of unknown-risk perceptions. Perceptions of unknown risk represent the perceptions of insufficient knowledge (Brashers & Hogan, 2013). ??????????????<sup>(n)</sup> denotes the number of words associated with perceptions of unknown risk for microblog n that were obtained by CLIWC.

Pennebaker, Booth, & Francis (2007) developed the English LIWC dictionary as a computerized way to analyze the word used in a text. Huang et al. (2012) developed the Chinese version of LIWC. CLIWC operates as a processing phase. It can compare every microblog word after segmentation from the input files to a preloaded CLIWC dictionary of words. The dictionary of CLIWC provides a basis to give an output measure for each of these categories. Each word can be classified into different dimensions. Different domains have extensively used and validated these dimensions. In the dictionary of CLIWC, the “Tentative” dimension represents unknown words of microblog user-generated contents, such as “maybe,” “or,” “approximately,” “seemingly,” etc. (in Chinese “可能,” “或,” “几乎”, “似 乎”). We employ a lexicon-based methodology and used the CLIWC dictionary to obtain the count of words associated with unknown-risk perceptions in each microblog, as follows:

$$
U n k n o w n ^ {(n)} = T e n t a t i v e ^ {(n)}\tag{2}
$$

Definition 3: Feature vector of dread-risk perceptions. We used the Lin Hongfei ontology and CLIWC dictionaries to measure the number of words associated with fear and death. Lin Hongfei ontology is a famous dictionary in China, similar to the CLIWC dictionaries.

Figure 2 illustrates the calculation process of the feature vector of perceptions of dread- and unknown risk. The input includes the Lin Hongfei ontology dictionary, the CLIWC dictionaries, and the word series $\{ w _ { 1 } , w _ { 2 } , \ldots , w _ { q } \}$ of content ?? after preprocessing. The output is ??????????<sup>(??)</sup> and ????????????<sup>(??)</sup>. ??????????(??<sub>??</sub>) is the number of words associated with perceptions of dread risk used in the word series $w _ { i }$ of microblog n. ??????????????(?? ) is the number of words associated with perceptions of unknown risk used in the word series $w _ { i }$ of microblog n. Each microblog has the value of ??????????<sup>(??)</sup> and ????????????<sup>(??)</sup>.

Figure 3 visualizes the primary risk perceptions: dread risk and unknown risk. From left to right, EID threats are judged as being associated with increased unknown-risk perceptions and less expert knowledge, and being newer, less controllable, and consequently not mitigable. From bottom to top, EID threats are judged as being associated with increased dread-risk perceptions, more fear, greater fatal consequences, and as being less easily reduced. The higher the perception values of dread- and unknown risk, the higher the level of perceived risk. Therefore, Area 1 of Figure 3 shows the highest perception values of dread risk and unknown risk.

![](/api/attachments/TPR2KJ8Z/fulltext/images/e4b80945ce65f1f62375c2fad0485aaf20c3c2e73d4a5682f14ada69f759c05e.jpg)  
Figure 2. Flow Chart of Risk Perceptions Calculation

![](/api/attachments/TPR2KJ8Z/fulltext/images/5d6475ce5a5d3cb13d7fe7bf73689637abbcc6d3de87fcd7cc15ccc54bfce13b.jpg)  
Figure 3. Risk Characteristics of EID Threats

![](/api/attachments/TPR2KJ8Z/fulltext/images/682ac49559814dea2900789adf2b45270d7fe0496c6a359d48a4c332ca77d144.jpg)  
Note: In this figure, we present the topics related to the buildup, breakout, abatement, and termination stages as “What is the virus and what are its causes?” “Where are the virus cases and new cases of infection, and how can infection be prevented?” “Prevention and control of the virus,” and “Prevention and control of the virus and accountability,” respectively. The latent dirichlet allocation (LDA) model is used to extract topic words. These words are also used for enriching the dictionaries of Lin Hongfei ontology and CLIWC, which may provide risk characteristic words in the EID context.  
Figure 4. Crisis Stages of Avian Influenza

## 3.2.3 Moderating Variables

Definition 4: Feature vector of crisis stages. There are four stages for EID crises: (1) the buildup stage, during which the crisis begins to appear; (2) the breakout stage, in which the crisis is aggressively fought; (3) the abatement stage, in which the indirect consequences of the crisis become important; (4) the termination stage, during which the public response dissipates. ??????????????????????<sup>(n)</sup> represents the different stages of development stages in EID events and has four values 1, 2, 3, and 4, corresponding to the respective stage of EID events.

WHO and CDC reports are often used to mitigate negative public emotional responses and perceptions of information uncertainty (Baker & Fidler, 2006). Figure 4 depicts the four development stages of avian influenza A (H7N9) virus as reported by WHO news (https://www.who.int/influenza/human\_animal\_interf ace/avian\_influenza/archive/en/). The buildup stage of avian influenza began on February 19, 2013, the day the first case of infection emerged. The crisis moved to the breakout stage after March 31, 2013, when human infections were first reported on the WHO website. The abatement stage began on April 24, 2013, when updates of human infections on the WHO website became significantly less frequent. Finally, the termination stage began on May 30, 2013, after which there were no further updates regarding human avian influenza infections on the WHO website until June 15, 2013.

## 3.2.4 Control Variables

To control the influence of other factors, we introduced control variables into our research model. Previous literature has analyzed the influence of positive and negative emotions on sharing behavior. However, since emotions are not the main focus of this paper, we used emotions as control variables. To control for the threat of information overload, we also controlled the total amount of information by total words count in each microblog.

Definition 5: Feature vectors of positive and negative emotions. The constructs ??????????????????????????????<sup>(??)</sup> and ??????????????????????????????<sup>(??)</sup> denote the positive and negative emotions feature vectors for each microblog, according to the different types of emotions reflected in the content. This calculation is also lexicon-based and includes input from the Lin Hongfei ontology dictionary and word series $\{ w _ { 1 } , w _ { 2 } , \ldots , w _ { q } \}$ of microblog ?? after preprocessing. Each word in microblog n matches an entry in the Lin Hongfei ontology dictionary. The number of matched positive or negative emotion words represents the number of positive or negative emotions in microblog n.

$$
U n k n o w n _ {t} = U n k n o w n ^ {(1)} + \dots + U n k n o w n ^ {(m)}
$$

Definition 6: Feature vector of information volume. ??????????????????????????????????<sup>(??)</sup> denotes the total number of words in each microblog.

## 3.2.5 Main Variables of Interest

Following Adomavicius, Bockstedt, & Gupta (2012), we analyzed the dynamic effects between variables by first calculating the time series for each variable. For example, we calculated the time series of dread- and unknown-risk perceptions by aggregating the number of risk perception words associated with dread risk and unknown risk in microblogs on an hourly basis.

Let ?? denote the number of sharing microblogs, ?? represent the time window (t equals 1 hour here). ??????????????<sub>??</sub> , ??????????<sub>??</sub> , ????????????????????????????<sub>??</sub> ??????????????????????????????<sub>??</sub> , ??????????????????????????????????<sub>??</sub> ??ℎ??????????????ℎ?????????? represent the time series variables, given below in formulas (3) through (8). Table 2 summarizes the detailed definitions of all dependent variable, independent variables, moderating variable, and control variables used in our regression.

(3)

$$
D r e a d _ {t} = D r e a d ^ {(1)} + \dots + D r e a d ^ {(\mathrm{m})}\tag{4}
$$

$$
P o s i t i v e E m o t i o n _ {t} = p o s i t i v e E m o t i o n ^ {(1)} + \dots + p o s i t i v e E m o t i o n ^ {(m)}\tag{5}
$$

$$
N e g a t i v e E m o t i o n _ {t} = n e g a t i v e E m o t i o n ^ {(1)} + \dots + n e g a t i v e E m o t i o n ^ {(m)}\tag{6}
$$

$$
I n f o r m a t i o n V o l u m e _ {t} = i n f o r m a t i o n V o l u m e ^ {(1)} + \dots + i n f o r m a t i o n V o l u m e ^ {(m)}\tag{7}
$$

$$
\text { SharingBehavior } _ {\mathrm{t}} = \text { sharingBehavior } ^ {(1)} + \dots + \text { sharingBehavior } ^ {(m)}\tag{8}
$$

Table 2. Definition of Variables

<table><tr><td>Variable type</td><td>Variable</td><td>Definition</td></tr><tr><td>Dependent variable</td><td>Sharing behavior</td><td>The number of times posted and reposted within time window t.</td></tr><tr><td rowspan="2">Independent variables</td><td>Unknown-risk perceptions</td><td>The number of uncertainty words the microblogs contained within time window t.</td></tr><tr><td>Dread-risk perceptions</td><td>The number of dread words the microblogs contained within time window t.</td></tr><tr><td>Moderating variable</td><td>Crisis stages</td><td>The crisis stages of EID events.</td></tr><tr><td rowspan="3">Control variables</td><td>Positive emotions</td><td>The number of positive emotions words the microblogs contained within time window t.</td></tr><tr><td>Negative emotions</td><td>The number of negative emotions words the microblogs contained within time window t.</td></tr><tr><td>Information volume</td><td>The number of words the microblogs contained within time window t.</td></tr></table>

## 3.3 VAR model

In constructing our estimation model, we used the vector autoregression (VAR) model, which has been used in recent IS (information system) research (Adomavicius et al., 2012) and allows us to capture the dynamic relationships between variables. In our research context, VAR has several advantages over alternative modeling techniques. First, it can measure the effects of risk perceptions on sharing behavior over time. Second, VAR has the advantage of being able to address feedback biases from reversed causality; risk perceptions in the current period may influence the sharing behavior in the next period, which may in turn cause a change in the risk perceptions in the next period. Therefore, VAR methodology can simultaneously measure the dynamic and intricate mutual influences between different variables. VAR can uncover the full influence of risk perceptions and show the time-varying effects of risk perceptions on sharing behavior by considering the feedback effect of sharing behavior on risk perceptions.

We also included the intercept C. By introducing our variables, the VAR specification is shown in Model (9) below. Model (9) represents each variable as a function of its own past value, the past value of other variables, and an error term. ?????????????? , and ?????????? represent time series variables of independent variables, and ??????????????<sub>??</sub> × ??????????<sub>??</sub> is the joint effect of dread-risk and unknown-risk perceptions. ?????????????????????????????? , ?????????????????????????????? ,

and ?????????????????????????????????? denote the control variables. ??ℎ??????????????ℎ?????????? denotes the dependent variable. J is the maximum number of lags. $\alpha _ { i 1 } \ldots \alpha _ { i 3 }$ denotes the coefficient matrices. $\varepsilon _ { i }$ is a vector of white-noise disturbances with a normal distribution of N(0, Σ). Where t is the index of an hour.

We treated the crisis stage as the classification variable and divided the dataset into four parts to analyze the moderating effect of the crisis stage. For example, we used Model (10) to analyze the dynamic effects of perceptions of dread- and unknown risk on sharing behavior in the buildup stage. $U n k n o w n _ { t 1 } , D r e a d _ { t 1 }$ $S h a r i n g B e h a v i o r _ { t 1 } , P o s i t i v e E m o t i o n _ { t 1 }$

$N e g a t i v e E m o t i o n _ { t 1 } , U n k n o w n _ { t 1 } \times D r e a d _ { t 1 }$ , and ???????????????????????????????? $e _ { t 1 }$ represent time series variables in the buildup stage. The analysis models of the breakout, abatement, and termination stages have similarities with Model (10), so we omitted them here.

![](/api/attachments/TPR2KJ8Z/fulltext/images/42c5c9b2fec27f250899fd5fe16c4de234a67b5b91c613d92726cfd5e526c80f.jpg)  
(9)

$$
\left[ \begin{array}{c} U n k n o w n _ {t 1} \\ D r e a d _ {t 1} \\ U n k n o w n _ {t 1} \times D r e a d _ {t 1} \\ P o s i t i v e E m o t i o n _ {t 1} \\ N e g a t i v e E m o t i o n _ {t 1} \\ I n f o r m a t i o n V o l u m e _ {t 1} \\ S h a r i n g B e h a v i o r _ {t 1} \end{array} \right] = \left[ \begin{array}{c} C _ {U n k n o w n} \\ C _ {D r e a d} \\ C _ {U n k n o w n \times D r e a d} \\ C _ {P o s i t i v e E m o t i o n} \\ C _ {N e g a t i v e E m o t i o n} \\ C _ {I n f o r m a t i o n V o l u m e} \\ C _ {S h a r i n g B e h a v i o r} \end{array} \right] + \sum_ {j = 1} ^ {J} \left[ \begin{array}{c} \alpha_ {1, 1} ^ {j} \dots \alpha_ {1, 7} ^ {j} \\ \alpha_ {2, 1} ^ {j} \dots \alpha_ {2, 7} ^ {j} \\ \alpha_ {3, 1} ^ {j} \dots \alpha_ {3, 7} ^ {j} \\ \alpha_ {4, 1} ^ {j} \dots \alpha_ {4, 7} ^ {j} \\ \alpha_ {5, 1} ^ {j} \dots \alpha_ {5, 7} ^ {j} \\ \alpha_ {6, 1} ^ {j} \dots \alpha_ {6, 7} ^ {j} \\ \alpha_ {7, 1} ^ {j} \dots \alpha_ {7, 7} ^ {j} \end{array} \right] \left[ \begin{array}{c} U n k n o w n _ {t 1 - j} \\ D r e a d _ {t 1 - j} \\ U n k n o w n _ {t 1 - j} \times D r e a d _ {t 1 - j} \\ P o s i t i v e E m o t i o n _ {t 1 - j} \\ N e g a t i v e E m o t i o n _ {t 1 - j} \\ I n f o r m a t i o n V o l u m e _ {t 1 - j} \\ S h a r i n g B e h a v i o r _ {t 1 - j} \end{array} \right] + \left[ \begin{array}{c} \varepsilon_ {U n k n o w n} \\ \varepsilon_ {D r e a d} \\ \varepsilon_ {U n k n o w n \times D r e a d} \\ \varepsilon_ {P o s i t i v e E m o t i o n} \\ \varepsilon_ {N e g a t i v e E m o t i o n} \\ \varepsilon_ {I n f o r m a t i o n V o l u m e} \\ \varepsilon_ {S h a r i n g B e h a v i o r} \end{array} \right]\tag{10}
$$

The basis of VAR model construction has two processes: (1) the stationarity test and (2) optimal lag length selection. The stationarity of time series data is an important requirement that must be evaluated before carrying out the dynamic analysis. We performed an augmented Dicker-Fuller (ADF) unit root test for all endogenous variables respectively. We used the time series data with stationarity to construct the VAR model. For time series that did not have stationarity, we used a difference method for data smoothing and then performed the ADF test again. Time series that passed the ADF test were used for VAR analysis. The optimal lag length was chosen based on three commonly used indexes, including Akaike information criterion (AIC), Hannan-Quinn criterion (HQC), and final prediction error (FPE). With our time series, all three indexes indicated that the optimal lag length is 2.

## 4 Results and Discussion

To derive our results, we justified the appropriateness of the VAR methodology and analyzed the dynamic evolution of perceptions of dread- and unknown risk in the context of EID events. Then, we introduced the estimation results of the VAR model and demonstrated the significant relationships between risk perceptions and SNS sharing behavior. Finally, we compared the keywords associated with perceptions of dread- and unknown risk in different crisis stages.

## 4.1 Dynamic Evolving and Interactions of Risk Perceptions

We first analyzed the dynamic evolution of risk perceptions. Based on Figure 3, we added a time dimension in Figure 5 that shows perceptions of dreadand unknown risk have similar dynamic evolution trends in the overall crisis development. However, in the buildup stage, we found more perceptions of dread risk than unknown risk in total (unknown: 2430 vs. dread: 3129), and the highest value of dread-risk perceptions is 96, which is 53 units larger than that of unknown-risk perceptions. In the breakout stage, total perceptions of dread- and unknown risk are 366,735 and 372,787, respectively, and the highest values are 3,165 and 3,319, respectively. In the abatement stage, dread-risk perceptions have a higher total count and a larger highest value than unknown-risk perceptions. Conversely, in the termination stage, unknown-risk perceptions have a higher total count and a larger highest value than dread-risk perceptions.

Generally, a lack of timely and relevant knowledge tends to cause public uncertainty. However, official reports of cases of infection may also cause increases in public fear or anxiety. Our findings suggest that (1) perceptions of dread- and unknown risk reach their highest levels in the breakout stage; (2) in both the buildup and abatement stages, dread-risk perceptions are higher than unknown-risk perceptions; (3) in the breakout and termination stages, unknown-risk perceptions are higher than dread-risk perceptions.

We now discuss the interactions between dread-risk perceptions and unknown-risk perceptions. The coefficients of the VAR model are not useful for studying the dynamic effects of risk perceptions on sharing behavior because is infeasible to interpret the estimated VAR coefficients directly. The main interest of VAR modelers, therefore, lies in the net result of all the modeled actions and reactions over time, which can be derived from the estimated coefficients through the associated impulse response functions (IRFs). Additionally, we introduced the Granger causality test to evaluate the appropriateness of further analyzing the dynamic relationships between risk perceptions and sharing behavior before IRFs analysis. These are standard procedures for analyzing the VAR model (Adomavicius et al., 2012; Luo, Zhang, & Duan, 2013).

Granger causality analysis deals with the problem of whether x triggers $y ,$ and to which extent y can be explained by the lagged x. If so, x Granger causes y, or y can be triggered by x. Granger causality analysis presents the initial causality and provides evidence that it is necessary to further analyze the dynamic relationships between variables. Following Tirunillai and Tellis’s (2012) work, we performed a Granger causality test and found that unknown-risk perceptions Granger cause dread-risk perceptions $( p < 0 . 0 1 )$ . The feedback of dread-risk perceptions Granger also cause unknown-risk perceptions $( p < 0 . 0 1 )$ .

![](/api/attachments/TPR2KJ8Z/fulltext/images/7cf8b71ee13f70b630b6059bf15ef93aa97f03f15b70bbfa43dd3128ed675710.jpg)  
Note: The coordinates in parentheses include time window, unknown-risk and dread-risk perceptions.  
Figure 5. The Evolution of Risk Perceptions

Impulse response functions (IRFs) trace the timevarying effects of a one-unit shock of an endogenous variable on the other variables. That is, IRFs can stimulate the influence of a one-unit shock of one endogenous variable on future changes of other endogenous variables and can assess the significance of these changes. Following Song et al. (2018) and Dekimpe and Hassens (1999), we used generalized IRFs to avoid such influences of the variables’ order on results and accounted for the same-period effect. Standard errors are derived by simulating the fitted VAR model using a Monte Carlo simulation with 1000 run times to test the results of generalized IRFs. We compared the results of six time windows in which the dynamic relationships reach stabilization (Song et al., 2018). The x-axis is the timeline (i.e., hourly time windows) and the y-axis represents the response of a dependent variable to a unit of shock in the impulse variable. The error bar is 95%-confident intervals that are bootstrapped based on the studentized interval (Lütkepohl, 2005; Adomavicius et al., 2012).

Figure 6 shows the IRFs results of the interactions between perceptions of dread- and unknown risk. It is interesting here that not only do unknown-risk perceptions cause dread-risk perceptions, but dreadrisk perceptions can also lead to unknown-risk perceptions. Unknown-risk perceptions have a higher magnitude impact on dread-risk perceptions at Time Window 1. However, at Time Window 6, the response of unknown-risk perceptions to dread-risk perceptions is higher than the response of dread-risk perceptions to unknown-risk perceptions. The results illustrate that unknown-risk perceptions have a dominant and immediate impact on dread-risk perceptions, while dread-risk perceptions have a dominant and persistent/durable impact on unknown-risk perceptions.

In Figure 7, we compared the IRFs results of perceptions of dread- and unknown risk in different crisis stages and compared the relationship magnitudes of Unknown→Dread and Dread→Unknown in the same stage. Surprisingly, unknown-risk perceptions had the highest impact on dread-risk perceptions at time Window 1 in the buildup stage and Time Window 3 in the abatement stage. The response of unknownrisk perceptions to dread-risk perceptions had the highest magnitude at Time Window 1 in the breakout stage and Time Window 2 in the termination stage. In other words, the dominant relationship between perceptions of dread- and unknown risk in the buildup, breakout, abatement, and termination stages can be summarized as Unknown→Dread, Dread→Unknown, Unknown→Dread, and Dread→Unknown, respectively, which constitutes a spiral process.

![](/api/attachments/TPR2KJ8Z/fulltext/images/4e217144c66805b49d7f9ba40a6e540f7323bce24ddaa10f900a2fccaf2dfa2f.jpg)  
(a)

![](/api/attachments/TPR2KJ8Z/fulltext/images/4e89f42be58797af082e9bd7f832a6df614a84e7e108cf95136d8529e654bee3.jpg)  
(b)  
Figure 6. The IRFs Results of the Interactions Between Risk Perceptions

![](/api/attachments/TPR2KJ8Z/fulltext/images/dc6df1e365d7d9d1adf03fe58f2be238b98d75cb2ff7934efaa62f248d6bf1dc.jpg)  
(a)

![](/api/attachments/TPR2KJ8Z/fulltext/images/2e202602ad878892e0582d758a38d7c33c7819de2a2b9df5a92fb26511776c4e.jpg)

![](/api/attachments/TPR2KJ8Z/fulltext/images/4d25e75d4c986ee8e1858f894ae8691393d1d35303455f21f38be92c99c265ae.jpg)  
(c)

(b)  
![](/api/attachments/TPR2KJ8Z/fulltext/images/6e82ace89cd67ffb0629ad937d714c03a76f50809e17df430b3f991f47794fd3.jpg)  
(d)

![](/api/attachments/TPR2KJ8Z/fulltext/images/d0ceef0fdd353b1efdb8b070a846243ab0bf32acc0b46999cbc6cddf678bb038.jpg)  
(e)

![](/api/attachments/TPR2KJ8Z/fulltext/images/51e51d141c3259d9193b753c207b4663c6d72d9f0976ab4921f8ed5bf771f8d3.jpg)  
(f)

![](/api/attachments/TPR2KJ8Z/fulltext/images/f90f7dbaca5dd264e6f63c297b7302c7f7b9aafb1805c6fd60fdb96a36144399.jpg)  
(g)

![](/api/attachments/TPR2KJ8Z/fulltext/images/d868caa29c9e6639085c881b67d5394dd35fbf9e056cabed4a73d603efa678e2.jpg)  
(h)  
Figure 7. The IRFs Results of the Interactions Between Risk Perceptions in Four Crisis Stages

## 4.2 The Dynamic Effects of Risk Perceptions on SNS Sharing Behavior

We found that dread-risk perceptions Granger cause sharing behavior $( p \mathrm { ~  ~ { ~  ~ } ~ } 0 . 0 0 1 )$ unknown-risk perceptions Granger cause sharing behavior $( p \texttt { < }$ 0.001), and the joint effect of perceptions of dread risk and unknown risk Granger cause sharing behavior $( p <$ 0.1). These results illustrate that both dread-risk and unknown-risk perceptions have significant impacts on sharing behavior. Therefore, we now analyze the IRFs.

We first analyzed the dynamic relationships between risk perceptions and sharing behavior in Model (9). Next, we introduced the results of how the crisis stages influence the dynamic relationships between risk perceptions and sharing behavior based on Model (10).

Figure 8 shows the dynamic relationships between dread-risk perceptions, unknown-risk perceptions, and the joint effect of risk perceptions on sharing behavior. Specifically, dread-risk perceptions have a higher magnitude impact on sharing behavior than unknownrisk perceptions at Time Windows 1-3. Unknown-risk perceptions have a higher impact on sharing behavior at Time Windows 4-6. Furthermore, the responses of sharing behavior at Time Window 1 invoked by perceptions of dread- and unknown risk are higher than persistent responses at Time Window 6. The joint effect of perceptions of dread risk and unknown risk on sharing behavior is also significant at Time Windows 1-6. However, the magnitude of the joint effect of risk perceptions is smaller than the product of separate impacts of dread-risk perceptions and unknown-risk perceptions on sharing behavior. It is also should be mentioned that all responses eventually reach a stable state.

![](/api/attachments/TPR2KJ8Z/fulltext/images/a8245e5dd77d6852d8c7bab408caf98909f7e36d9e6be9eb8c619795449b9c63.jpg)  
Figure 8. The Dynamic Effects of Risk Perceptions on Sharing Behavior

The IRFs results of control variables are illustrated in Table A1 of Appendix A. Positive emotions, negative emotions, and information volume exert significant impact on sharing behavior from Time Windows 1-6.

Figure 9 shows the IRFs results of risk perceptions on sharing behavior in different crisis stages and provides six time windows of IRFs for the estimated VAR model. For example, in Figure 9(a), sharing behavior has a 20-unit response to dread-risk perceptions in the buildup stage, demonstrating that a one-unit increase in dread-risk perceptions at Time Window 0 can trigger a 20-unit increase in sharing behavior at Time Window 1. We found a significant response in sharing behavior with both perceptions of dread-risk and unknown-risk in the breakout stage. Dread-risk perceptions trigger a higher response in sharing behavior than unknown-risk perceptions (ca. 185 units higher), as does the joint effect of both risk perceptions (ca. 35 units higher). In the abatement stage, sharing behavior has a higher magnitude of response to unknown-risk perceptions at Time Window 1. The results from the termination stage at Time Window 1 illustrate that sharing behavior has a higher magnitude of response to dread-risk perceptions than unknownrisk perceptions. We also found that the impacts on sharing behavior of dread-risk perceptions, unknownrisk perceptions, and the joint risk perceptions all attenuate quickly from the buildup stage to the termination stage.

Figure 9(b) shows how the four crisis stages influence the impact of risk perceptions on sharing behavior at Time Window 2. We found that the magnitudes of response to both the perceptions of dread- and unknown risk decrease, compared to Time Window 1. In the breakout stage, perceptions of dread- and unknown risk have a similar impact on sharing behavior, exerting an approximately equal impact on sharing behavior at Time Window 2. In comparison, the response of sharing behavior to the joint effect of perceptions of dread risk and unknown risk is 3, 1089, 499, and 16 in the buildup, breakout, abatement, and termination stages, respectively. However, the influence magnitude of the joint effect on sharing behavior is significantly less than the product of the magnitude of dread-risk perceptions on sharing behavior and unknown-risk perceptions on sharing behavior (The magnitude of IRFs results $I R F _ { D r e a d \times U n k n o w n } < I R F _ { D r e a d } \times I R F _ { U n k n o w n } )$

Figure 9(c) illustrates the relationship between risk perceptions and sharing behavior at the Time Window 3. All of the relationships are strongly diminished, except the response of sharing behavior to unknownrisk perceptions in the abatement stage. Sharing behavior has a response value of 382 to the stimulus of unknown-risk perceptions in the breakout stage. In the abatement stage, the magnitude of the impact of unknown-risk perceptions on sharing behavior increases to 532.

In Figure 9(d), (e), and (f), the 95% confidence interval illustrates that dread-risk perceptions, unknown-risk perceptions, and the joint effect of the two types of risk perceptions do not have a significant impact on sharing behavior. It is also worth mentioning that all responses converge to zero after three time-windows (or hours) and therefore reach a stable state. In other words, risk perceptions do not trigger sharing behavior at Time Window 4.

Generally, the response of sharing behavior to dreadrisk perceptions has the highest magnitude at Time Window 1, when compared with the impact of dreadrisk perceptions, unknown-risk perceptions, and the joint effect on sharing behavior in the other time windows of the buildup stage. Dread-risk perceptions also have a dominant effect on sharing behavior at Time Window 1 in the breakout and termination stages, while unknown-risk perceptions have a

dominant effect on sharing behavior at Time Window 1 in the abatement stage. Therefore, the dynamic effect of dread-risk perceptions on sharing behavior is dominant in the buildup, breakout, and termination stages, and the response of sharing behavior to unknown-risk perceptions is dominant in the abatement stage. The results also illustrate that unknown-risk perceptions have a more persistent impact on sharing behavior because only unknownrisk perceptions have a significant impact on sharing behavior at Time Window 3 in the breakout and abatement stages. Sharing behavior has a more immediate response to dread-risk perceptions at Time Window 1 in the four crisis stages. Perceptions of dread risk and unknown risk jointly influence sharing behavior; however, the magnitude of such influence is less than the influence of the product of dread-risk and unknown-risk perceptions on sharing behavior.

![](/api/attachments/TPR2KJ8Z/fulltext/images/cab30149c854b28cca775f69853ed4aa4dfdf94b18de789763b1edc555c769c8.jpg)  
(a)

![](/api/attachments/TPR2KJ8Z/fulltext/images/ff7dcbefbf0c81e9c17b41f0ea544902e0d7b777de1615e3564da76a963a25da.jpg)  
(b)

![](/api/attachments/TPR2KJ8Z/fulltext/images/a6f9f40f639a17e264d67226483ba2b8e5c68e24655837609eaee026d38c0654.jpg)  
(c)

![](/api/attachments/TPR2KJ8Z/fulltext/images/1673aa8b1656c2a4c1832a3db23a875d8e6fc89a503894b9106c93e8616155e7.jpg)  
(d)

![](/api/attachments/TPR2KJ8Z/fulltext/images/829c411d31097bd13936469706faffedc002986ced0ef137bdd91d22dd43e3f9.jpg)  
(e)

![](/api/attachments/TPR2KJ8Z/fulltext/images/7c36bbe63d6882dd9118315a86750d545c3746d92e47632fb4ab75173ceedf41.jpg)  
(f)  
Note: The dash line represents the trend of influences of risk perceptions on sharing behavior.  
Figure 9. IRFs Results of Risk Perceptions on Sharing Behavior in Different Crisis Stages

In Figure 10, we also compared the deceleration speed of the dynamic evolving influences at different time windows. We find that the influences of deceleration magnitudes of dread-risk and unknown-risk perceptions on sharing behavior are different in the four crisis stages. Specifically, other than the influence of unknown-risk perceptions on sharing behavior in the abatement stage at Time Windows 2-3, the influence of the risk perceptions on sharing behavior decreases. In the breakout stage, the influence of dread-risk perceptions on sharing behavior decreases faster than that of unknown-risk perceptions. In the abatement stage, the influence of unknown-risk perceptions on sharing behavior decreases more slowly than that of dread-risk perceptions, illustrating the respective immediate and persistent characteristics of the impact of dread-risk and unknown-risk perceptions on sharing behavior.

## 4.3 Further Analysis

In this section, we compared the keywords associated with perceptions of dread- and unknown risk in different crisis stages. Table 3 presents keywords associated with dread-risk perceptions in the buildup stage, including “rescue,” “outbreak,” “panic,” etc. (“ 抢 救 ”, “ 爆 发 ”, “ 恐 慌 ”, etc. in Chinese). In the breakout stage, keywords associated with dread-risk perceptions include “terrible,” “be careful,” “panic,” “fear,” and so on (“可怕”, “小心”, “恐慌”, etc. in Chinese). While “terrible” and “be careful” are keywords common to the breakout, abatement, and termination stages, there begins to be more talk about the “emergency” (“应急”, in Chinese) in the abatement stage. In the termination stage, important keywords include “emergency,” “be careful,” “terrible,” etc.

In contrast to the keywords associated with dread-risk perceptions, keywords associated with unknown-risk perceptions mainly describe uncertain feelings. The magnitude of uncertain feelings in the breakout and abatement stages is stronger than in the buildup and termination stages. For example, “how,” “still,” “suspected ” (“怎么”, “还是”, “疑似” in Chinese) are the main keywords in the breakout and abatement stages, whereas “or,” “who,” “someone,” “if,” (“或”, “ 谁”, “某”, “如果” in Chinese) are the main keywords in the buildup and termination stages.

![](/api/attachments/TPR2KJ8Z/fulltext/images/79d9ee6939205f39c854240f46f8ae7211a51725fc2648540f051a8b967621f3.jpg)  
Figure 10. The Deceleration Speed of the Influences of Risk Perceptions on Sharing Behavior

Table 3. Keywords of Perceptions of Dread- and Unknown Risk in Different Crisis Stages

<table><tr><td>Keywords</td><td>Buildup stage</td><td>Breakout stage</td><td>Abatement stage</td><td>Termination stage</td></tr><tr><td>Dread</td><td><img src="/api/attachments/TPR2KJ8Z/fulltext/images/113fef5bde80c8cc28303821f17793b6d1a0ddf4c2acab1968ee3f8feef025c6.jpg"/></td><td><img src="/api/attachments/TPR2KJ8Z/fulltext/images/10c6c7fed00394d807a56d666d1e35cddacb6a3eac04d53cb3bb1418863050c4.jpg"/></td><td></td><td><img src="/api/attachments/TPR2KJ8Z/fulltext/images/605d813e5a4bfda40bcf2f61943b1d7acff2d55b3f11da524316d1afae0101a3.jpg"/></td></tr><tr><td>Unknown</td><td><img src="/api/attachments/TPR2KJ8Z/fulltext/images/afc476058c85dcf513de1f1a97067193b550a5f481a8fd149efa6bddcf98abfc.jpg"/></td><td></td><td></td><td></td></tr></table>

## 4.4 Discussion

This study seeks to identify an appropriate theoretical lens to explain the dynamic evolution of risk perceptions and sharing behavior in the context EID events. Toward this end, we discuss several important findings.

First, we found that perceptions of dread- and unknown risk dynamically evolve and their dynamic characteristics are consistent with self-perception theory. The spiral process of unknown-risk and dreadrisk perceptions can be summarized as Unknown → Dread, Dread→Unknown, Unknown→Dread, Dread→ Unknown in the buildup, breakout, abatement, and termination stages, respectively. At the beginning of EID events, during the buildup stage there is public uncertainly about, for example, how an infectious disease is propagated, who the carriers of the disease are, and when or where an epidemic will begin to emerge. During such times, great efforts are made to gain a sense of control in the face of uncertainty. Since individuals tend to perceive uncertainty in conjunction with emotions such as dread and fear (Armfield, 2006), the actual extent and severity of a hazard may be overestimated. Therefore, during the buildup stage unknown-risk perceptions cause dread-risk perceptions to intensify. In this stage, dread-risk perceptions are much more dominant than unknown-risk perceptions. In the next stage, the breakout stage, dread-risk perceptions begin to impact unknown-risk perceptions, leading to the dominance of unknown-risk perceptions during this stage. In the abatement and termination stages, the spiral process of the interactions between perceptions of dread- and unknown risk continue; however, the strength of the interaction gradually diminishes as the crisis abates.

Second, as illustrated in Figure 8, we found that dreadrisk perceptions have a dominant and immediate effect on sharing behavior at Time Window 1 and unknownrisk perceptions have a dominant and persistent effect on sharing behavior at Time Window 6. Kahnemann’s theory of two systems—one fast and one slow—that control public information processing (Kahneman, 2011) can perhaps clarify the reason for this. The sharing behavior we reveal here, in response to perceptions of dread- and unknown risk, corresponds to Kahnemann’s two systems. The fast system operates automatically and quickly, with little or no effort and no sense of voluntary control. The capabilities of the fast system include innate skills shared with others. We are born prepared to perceive the world around us, avoid losses, and fear threats. As such, public responses to perceptions of dread risk during EID events are instinctive, natural, and linked to our emotions because of threatening characteristics of such events. In contrast, the slow system allocates attention to effortful mental activities, including complex computations. The slow system is often associated with the subjective operations of agency, choice, and concentration. The slow system is more logical, thorough, and time consuming. Therefore, the effect of unknown-risk perceptions on sharing behavior in the abatement stage of a crisis perhaps correlates with the slow system and the higher levels of effort necessary for understanding relevant information central to EID events.

We also found that the impacts of perceptions of dreadand unknown risk on sharing behavior decreased with subsequent time windows. The effects of dread-risk perceptions on sharing behavior decrease more quickly than the effects of unknown-risk perceptions. The decreasing impacts of perceptions of both dread risk and unknown risk on sharing behavior suggest individuals’ limited information processing capacity and/or fatigue (Krupp & Elkins, 2000) in response to the deluge of user-generated content proliferated during a crisis, which may paradoxically result in decreased information diffusion.

Third, we found that dread-risk perceptions have a more dominant and immediate impact on sharing behavior than unknown-risk perceptions in the buildup, breakout, and termination stages. However, the highest value of risk perception is that of unknown risk in the breakout stage. We speculate that public sharing behavior is at least partially determined by sensitivity to different risk perception characteristics in different crisis stages, rather than by the bulk of risk perceptions. Official reports of pathogenicity, fatality numbers, threats, and actual deaths associated with EID events are likely to invoke strong fears about death at the early stages of an EID outbreak. To alleviate anxiety, individuals may engage in compensatory behavior to enhance their sense of self-esteem (Florian, Mikulincer, & Hirschberger, 2002; Greenberg, 1990). As a type of compensatory behavior, sharing on social media platforms can diffuse information more broadly, which can satisfy individuals’ interpersonal needs and decrease the discomfort generated by anxiety. Skinner (2013) and Simon, Goldberg, & Adini (2015) show how individuals collect and aggregate information from social media platforms during crisis events and share information to further inform those affected by the event, which may direct people “to official sources of information and result in amplifying this information to a broader audience” (Taylor et al., 2012). As such, during early stages of a crisis, individuals are more generally and profoundly influenced by dread-risk perceptions and engage in sharing behavior to buffer their anxiety in the buildup and breakout stages of EID events. Therefore, during the buildup and breakout stages, individuals may not have detailed information about the crisis and tend to be strongly influenced by their emotions when they make judgments about risk and thus engage in sharing behavior related to risk perceptions of dread in order to reduce anxiety.

In contrast, unknown-risk perceptions have a dominant and persistent impact on sharing behavior in the abatement stage in which public sensitivity to dreadrisk perceptions is diminished. Therefore, in the abatement stage, individuals seek to give meaning to EID events and regain a feeling of control. Individuals cognitively process physical threats associated with EID events as a means of controlling them, which fosters more stable and manageable emotions. During this process of cognition, individuals seek a comprehensive understanding of EID events, especially the origin of EID events, what is important to recognize during EID events, and how to protect oneself from EIDs. In other words, during this stage, individuals seek relevant summary information about the EID events, which may offer support for decisionmaking in similar potential future crises and are more likely to engage in sharing behavior related to unknown-risk perceptions.

![](/api/attachments/TPR2KJ8Z/fulltext/images/b44aa0b10d1b8d231c3a18c247004c13fd7f1e4a0d52159b90e8607758f63a15.jpg)  
Figure 11. Dynamic Evolution of Two Systems

![](/api/attachments/TPR2KJ8Z/fulltext/images/1acf04ee78007ac3f4874cbf1cd24943a51a8d6456ef40bf083339c873fc9758.jpg)  
Note: Symbol “↑” represents the higher influence between variables; Symbol “↓” represents the lower influence between variables.  
Figure 12. Relationships Between Risk Perceptions and Sharing Behavior

The dominant effects of perceptions of dread- and unknown risk on sharing behavior evolve dynamically, as illustrated in Figure 11. We speculate that both fast and slow systems are employed during EID events. In the buildup and breakout stages, there is an instinctive response of sharing behavior to dread-risk perceptions. The effect of unknown-risk perceptions on sharing behavior in the abatement stage illustrates that individuals require more effort to understand the relevant knowledge behind EID events because their information demands cannot be met in the fast system. In the termination stage, information processing aligns with the fast system again because of the low levels of attention and cognitive fatigue that have developed by this time.

Figure 12 shows the interactions between perceptions of dread- and unknown risk and the dominant influence of risk perceptions on sharing behavior. Interestingly, the joint effect of perceptions of dread risk and unknown risk is antagonistic in the four crisis stages. In other words, the influence magnitude of the joint effect of perceptions of dread risk and unknown risk on sharing behavior is less than the product of the separate influence of the individual risk perceptions. This phenomenon can be explained by the mental noise theory (Baron, Hershey, & Kunreuther, 2000), which suggests that when individuals are stressed, internal “mental noise” makes them less able to attend to externally generated information (Glik, 2007). In the context of EID events, the joint effect of perceptions of dread risk and unknown risk exert high levels of stress, which makes individuals unable to adequately comprehend cumulative risk (Glik, 2007). Therefore, sharing behavior responses are calmer in the context of the joint effect than with separate perceptions of dread risk and unknown risk. The antagonism may influence the interaction between risk perceptions, and the relationship between risk perceptions on sharing behavior, which further leads to dynamic effects between risk perceptions and sharing behavior in all four stages.

Further, the keywords of risk characteristics in different crisis stages indicate the topics associated with perceptions of dread- and unknown risk are timevarying; the keywords illustrate the type of contents that caused the sharing behavior. In the buildup and breakout stages, individuals care more about the range of contagion and disease fatality, are interested in how they might be influenced by the EID, and engage in sharing behavior to alleviate negative emotions. In contrast, keywords associated with unknown-risk perceptions in the abatement stage mainly concentrate on words like “still,” “suspected,” “how,” “maybe” (“ 还是”, “疑似”, “如何”, “可能” in Chinese) because individuals need relevant experiential knowledge to further protect themselves should they confront similar EID events in the future.

In summary, through the VAR model, our results show significant and different influences of risk perceptions on sharing behavior at distinct time windows of crisis stages. Figure 13 summarizes the main findings of our estimation model.

Crisis stage

<table><tr><td>Termination</td><td>1Dread-risk perceptions cause unknown-risk perceptions. 2Both the response of sharing behavior to dread- and unknown- risk perceptions are dying out. Dread-risk perceptions have a dominant and immediate impact on sharing behavior.</td></tr><tr><td>Abatement</td><td>1Unknown-risk perceptions have a higher magnitude impact on dread-risk perceptions. 2Unknown-risk perceptions have a dominant and persistent impact on sharing behavior among all the time windows. The joint effect of risk perceptions shows the antagonism. 3The decay speed of unknown-risk perceptions is accelerated slower than dread-risk perceptions.</td></tr><tr><td>Breakout</td><td>1Dread-risk perceptions have a higher magnitude impact on unknown-risk perceptions. 2Dread-risk perceptions have a dominant and immediate impact on sharing behavior among all the time windows. The joint effect of risk perceptions shows the antagonism. 3The decay speed of dread-risk perceptions is accelerated faster than unknown-risk perceptions.</td></tr><tr><td>Buildup</td><td>1Unknown-risk perceptions cause dread-risk perceptions. 2Dread-risk perceptions have a dominant and immediate impact on sharing behavior, such influences are dying out with the increasing of time windows.</td></tr></table>

Figure 13. Summary of Main Findings

## 5 Contributions and Implications

## 5.1 Theoretical Implications

This research has several theoretical implications. First, we extend the psychometric analysis from risk analysis fields to public response as reflected in a social media setting. This study introduces a novel perspective for understanding risk perceptions of EID threats based on user-generated content. Because EID threats create varying levels of dread-risk and unknown-risk perceptions, it is important for risk communication and risk management researchers to control for risk characteristics beyond perceived vulnerability and probability when investigating SNS sharing behavior in response to EID threats. Furthermore, our analysis shows that these characteristics of risk are dynamic and qualitative because knowledge in the public domain varies with time (Wildemuth, 2004), whereas previous literature only treats perceived risk as static and quantifiable (Wang et al., 2015; Deng & Liu, 2017). Therefore, future research should recognize the nature of risk perceptions in user-generated content as being dynamic, which could help account for the potentially variable strength of relationship analyses.

Additionally, microblogging has become increasingly powerful and more people use social media platforms to share information (Wang et al., 2017), including risk-related information. Microblogging provides a unique opportunity to observe how people behave when confronted with risks in real life. Social media platforms such as Sina Weibo, Twitter, Facebook, etc. represent rich data sources that contain public perceptions and can be used as a research tool.

Previous studies on risk perceptions and behavior have primarily relied on interview, survey, or laboratory observations (Deng & Liu, 2017; Ferrer et al., 2018), which are incapable of accurately reflecting the dynamic evolution of risk perceptions based on small intervals, such as one hour. Therefore, analysis of risk perceptions obtained from user-generated content could complement IS studies by capturing quiver changes and delicate observations of risk perceptions.

Second, this study contributes to Slovic’s framework of risk perception and self-perception theory by illustrating the effects of risk perceptions on sharing behavior not only with respect to quantity and joint effect but also in terms of time. Although several studies have investigated how content influences sharing behavior (Stieglitz & Dang-Xuan, 2013; Wang et al., 2017), studies remain sparse on what content is influential and how risk characteristics dynamically drive sharing behavior in the EID events context. This study sheds light on this research direction by showing that the two underlying factors of risk perceptions and their joint effect exert time-varying effects on sharing behavior. Moreover, the influence magnitude of the joint effect is less than the product of the separate influence of the individual perceptions of dread- and unknown risk on sharing behavior, which, as discussed above, can be explained by the mental noise theory. When confronting EID threats with different levels of risk perceptions, individuals use different information processing modes and adopt different behaviors. The magnitude of the effects varies and depends on the risk characteristics and specific time windows of EID events. Therefore, IS researchers should pay attention to the context and dynamic evolution of risk characteristics when applying risk analysis literature to studies on the public response to EID events. The characteristics of risk perceptions that are used to explain related behavior could affect the strength of the relationships.

Moreover, our model outperforms models that do not measure dynamic relationships between variables (Oh et al., 2020). The consideration of dynamic effects is crucial for reducing estimation biases such as endogeneity of potential feedback loops from sharing behavior to risk perceptions. By using IRFs plots to illustrate the dynamic relationships between variables, our results can provide a new perspective to analyze how the public behaves when facing different risk perceptions stimuli in a closed-loop system. The existence of dynamic effects between risk perceptions and sharing behavior could also be examined in other contexts.

Third, this study provides a dynamic perspective on crisis management research. Previous literature mainly concentrates on the static or qualitative crisis response and crisis management (Day et al., 2009; Pan et al., 2012). However, crisis management decision-making is not a single decision, but rather a sequential decision-making process that is dynamic and subject to adjustment. This study introduces crisis stages to analyze the relationships between risk perceptions and sharing behavior as a moderator. We found that perceptions of dread- and unknown risk show timevarying effects on sharing behavior in different crisis stages. Dread-risk perceptions, in particular, have a dominant and immediate impact on sharing behavior in the buildup, breakout, and termination stages, unknown-risk perceptions have a dominant and persistent impact on sharing behavior in the abatement stage. Perceptions of dread- and unknown risk have a spiral interaction process deriving from unknown-risk perceptions that lead to dread-risk perceptions in the buildup stage. As our results suggest, the reasons for this may include public sensitivity to risk perceptions in different crisis stages, individual information processing ability, and dynamically evolving risk perceptions. The keywords associated with risk perceptions reveal differences in how the public perceives risk in different crisis stages, which further explains public sensitivity to risk perceptions. Therefore, adding the indirect relationships between risk perceptions and sharing behavior, moderated by crisis stages, is helpful to understand the public response to EID events. Crisis management should consider the time-varying effects of the public response by incorporating keywords (Grover et al., 2019; Kim et al., 2018; Rathore & Ilavarasan, 2020) associated with risk perceptions in the buildup, breakout, abatement, and termination stages.

## 5.2 Practical Implications

Our research also provides several practical implications. Health agencies should promote efficient risk communication in the social media context. Our findings indicate that perceptions of dread- and unknown risk dynamically evolve and have a spiral relationship from the buildup to termination stages. The formation of dread-risk perceptions are largely due to unknown-risk perceptions characterized by feelings of uncertainty and lack of relevant information (Lebel, 2017). Therefore, for the ongoing COVID-19 pandemic, health agencies such as the CDC and WHO should seek to ease public panic through the transmission of the right type and amount of information, delivered in multiple languages in a way that people can understand and be able to act upon (Freimuth, Linnan, & Potter, 2000). However, in our IT-centric society most people suffer from a severe case of information overload. Health agencies should thus also recognize the limited ability of people to process information and disseminate accurate information and immediately refute any rumors. Since social media has become a vital part of everyday life for many individuals (Ahani, Rahim, & Nilashi, 2017), reliable collaborative platforms such as Sina Weibo, Twitter, and Facebook can provide a channel for immediate information dissemination of EID events. Early release of information on EIDs and early implementation of containment measures can help to counteract the lack of information and may help to effectively address public panic and improve control of the epidemic. Especially for the ongoing COVID-19 situation, social media can be used to detect misinformation, refute inaccurate information, and identify public opinion.

Our research demonstrates that there are distinct differences in how the public perceives uncertainties in the four crisis stages. It is important for health agencies to understand the differential sensitivity and demand for information. Through combing the topics and keywords that appear in each crisis stage, information about the concerns and interests of the public in different stages can be identified. We suggest that health agencies disseminate information around targeted topics to reduce uncertainty, such as “EID causes, fatality, transmissibility, and prevention”, “EID causes, fatality, transmissibility, and prevention and control”, “EID prevention and control”, and “EID accountability and lessons learned” in the buildup, breakout, abatement, and termination stages, respectively.

As an important channel mediating between health agencies and the public, social media can play a role in surveillance, early detection, and warning, and can potentially aid in tracking the dynamic evolution of public risk perceptions of COVID-19 before they are even necessarily recognized by health agencies. Therefore, social media surveillance can offer irregular insight into public risk perceptions associated by COVID-19 that could be useful to health agencies, the medical community, and researchers and enable authorities to make timely judgments. In the context of COVID-19, different countries, areas, or territories could use dynamically adjusting risk communication strategies based on their national conditions to develop effective messages. Since dread-risk perceptions have a dominant and immediate impact on sharing behavior in the buildup stage of a crisis, they have a stronger influence from the buildup stage to the breakout stage than in other stages. Our results suggest that organizations should consider designing messages to improve the accuracy and effectiveness of health warnings and limit the large-scale diffusion of panic in the breakout stage. Using risk communication messages such as fear appeals is an important strategy that can motivate the public to engage in responsible health behaviors (Johnston & Warkentin, 2010), which may help further reduce the outbreak and limit the diffusion of panic in social media. Such messages should be properly framed and consider the effects of perceptions of both dread- and unknown risk in order to avoid misunderstandings or underestimations of the risk. Effective risk communication can improve the mental health and foster important public health behavior (Jun et al., 2019) by cultivating a sense of power over circumstances that can decrease individuals’ sense of helplessness and mental stress, foster hope, and improve future outlooks. In the abatement stage, health agencies should seek to prevent a rebound of public fear and panic. As perceptions of unknown risk have a dominant and persistent impact on sharing behavior, relevant stakeholders can take actions such as timely point-topoint feedback intended to alleviate public uncertainty and diminish fear.

Moreover, this study also suggests that sharing behavior has a dominant and immediate response to the perceptions of dread risk in the buildup, breakout, and termination stages. As discussed above, the immediate response of individuals corresponds to the “fast” system (Kahneman, 2011), which can lead to a downward spiral and to an inability to distinguish fact from fiction. Therefore, processing EID information using the “slow” system (Kahneman, 2011) through mindful consumption is a requirement for news media literacy to be summoned in crisis stages. Individuals processing “slowly” have the time to questions and think about the source of the news, unstated assumptions, and questionable conclusions in a way that protects individuals from a disproportionate impact of emotional content. Accessing and sharing reliable and balanced media sources may further help individuals perceive risk in a more realistic way, reduce stress, and limit the diffusion of panic.

## 6 Limitations

We note several limitations of the present study. First, our data were collected from Sina Weibo sources that focuses on EID events. Thus, our findings may not apply to other domains that have different risk characteristics associated with threats such as financial crises or natural disaster events. Future research could extend the current study by applying it to public response in the context of other specific events and by examining different participant backgrounds. Second, the psychometric analysis we used does not adequately consider individual differences (Kraus & Slovic, 1988) such as gender and age. Moreover, we could not control for these individual characteristics when estimating our model due to the limitations of the dataset. Future research should investigate how and why individuals with distinct individual characteristics evaluate EID threats differently. Third, this study treats each microblog message we examined equally. However, microblogs from opinion leaders may have a more significant impact than those of ordinary users. Thus, future studies could account for the influence bias between different “levels” of users to yield more comprehensive and precise results.

## 7 Conclusions

In this study, we conducted an exploratory study using a dynamic perspective to examine how perceptions of dread- and unknown risk interact to evolve and influence sharing behavior in different crisis stages of EID events. The results confirmed the dominant and immediate effect of dread-risk perceptions on sharing behavior in the buildup, breakout, and termination stages and the persistent effect of unknown-risk perceptions on sharing behavior in the abatement stage. This study contributes to the IS domain by enriching and extending Slovic’s risk perception framework, self-perception theory, and applying the social media context to crisis management. Those involved with risk communication associated with the ongoing COVID-19 pandemic may particularly benefit from our proposed framework when formulating strategies to reduce uncertainty and provide timely and efficient information to the public.

## Acknowledgments

The work described in this paper has been supported by the National Natural Science Foundation of China (No.71573030) & (No.71533001), the Social Science Planning Fund Program, Liaoning Province (No. L19BGL001), and the Fundamental Research Funds for the Central Universities (No.DUT20RW207).

## References

Abraham, T. (2007). Twenty-first century plague the story of SARS. Johns Hopkins University Press.

Adomavicius, G., Bockstedt, J., & Gupta, A. (2012). Modeling supply-side dynamics of IT components, products, and infrastructure: An empirical analysis using vector autoregression. Information Systems Research, 23(2), 397-417.

Ahani, A., Rahim, N. Z. A., & Nilashi, M. (2017). Forecasting social CRM adoption in SMEs: A combined SEM-neural network method. Computers in Human Behavior, 75,560-578.

Aledort, J. E., Lurie, N., Wasserman, J., & Bozzette, S. A. (2007). Non-pharmaceutical public health interventions for pandemic influenza: An evaluation of the evidence base. BMC public health, 7(1), 208.

Arab-Mazar, Z., Sah, R., Rabaan, A. A., Dhama, K., & Rodriguez-Morales, A. J. (2020). Mapping the incidence of the COVID-19 hotspot in Iran: Implications for travellers. Travel Medicine and Infectious Disease, forthcoming.

Armfield, J. M. (2006). Cognitive vulnerability: A model of the etiology of fear. Clinical Psychology Review, 26(6), 746-768.

Baker, M. G., & Fidler, D. P. (2006). Global public health surveillance under new international health regulations. Emerging Infectious Diseases, 12(7), 1058.

Baron, J., Hershey, J.C., & Kunreuther, H. (2000). Determinants of priority for risk reduction: Yhe role of worry. Risk Analysis, 20(4), 413-428.

Bassarak, C., Pfister, H., & Böhm, G. (2017). Dispute and morality in the perception of societal risks: Extending the psychometric model. Journal of Risk Research, 20(3), 299-325.

Bem, D. J. (1972). Self-perception theory. Advances in Experimental Social Psychology.

Berger, J. (2011). Arousal increases social transmission of information. Psychological Science, 22(7), 891-893.

Berger, J., & Milkman, K. L.(2012). What makes online content viral. Journal of Marketing Research, 49(2), 192-205.

Bhatia, S. (2019). Predicting risk perception: New insights from data science. Management Science, 65(8), 3800-3823.

Bhattacherjee, A. (2001). Understanding information systems continuance: An expectation-

confirmation model. MIS Quarterly, 25(3), 351-370.

Boholm, A. (1998). Comparative studies of risk perception: A review of twenty years of research. Journal of Risk Research, 1(2), 135- 163.

Brashers, D. E., & Hogan, T. P. (2013). The appraisal and management of uncertainty: Implications for information-retrieval systems. Information Processing & Management, 49(6), 1241-1249.

Chen, Y., Zhang, Y. Z, Xu, Z., Wang, X., Lu, J., & Hu, W. (2019). Avian Influenza A (H7N9) and related Internet search query data in China. Scientific Reports, 9(1), 1-9.

Dang-Xuan, L., & Stieglitz, S. (2012). Impact and diffusion of sentiment in political communication: An empirical analysis of political weblogs. Proceedings of the Sixth International AAAI Conference on Weblogs and Social Media.

Dave, R., Boddhu, S. K., McCartney, M., & West, J. (2013). Augmenting situational awareness for first responders using social media as a sensor. IFAC Proceedings Volumes, 46(15), 133-140.

Day, J., Junglas, I., & Silva, L. (2009). Information flow impediments in disaster relief supply chains. Journal of the Association for Information Systems, 10(8), 637-660.

Dekimpe, M. G., & Hanssens, D. M. (1999). Sustained spending and persistent response: A new look at long-term marketing profitability. Journal of Marketing Research, 36(4), 397-412.

Deng, Z., & Liu, S. (2017). Understanding consumer health information-seeking behavior from the perspective of the risk perception attitude framework and social support in mobile social media websites. International Journal of Medical Informatics, 105, 98-109.

Dowling, G. R., & Staelin, R. (1994). A model of perceived risk and intended risk-handling activity. Journal of Consumer Research, 21(1), 119-134.

Ferrara, E., & Yang, Z. (2015). Quantifying the effect of sentiment on information diffusion in social media. PeerJ Computer Science, 1, e26 .

Ferrer, R. A., Klein, W. M. P., Avishai, A., Jones, K., Villegas, M., & Sheeran, P. (2018). When does risk perception predict protection motivation for health threats? A person-by-situation analysis. PLoS One, 13(3), e0191994 .

Fink, S. (1986). Crisis management: Planning for the inevitable. American Association of Management.

Fischhoff, B., Bostrom, A., & Quadrel, M. J. (1993). Risk perception and communication. Annual Review of Public Health, 14(1), 183-203.

Florian, V., Mikulincer, M., & Hirschberger, G. (2002). The anxiety-buffering function of close relationships: Evidence that relationship commitment acts as a terror management mechanism. Journal of Personality and Social Psychology, 82(4), 527-542.

Fong, S. J., Li, G., Dey, N., Crespo, R. G., & Herrera-Viedma, E. (2020). Finding an accurate early forecasting model from small dataset: A Case of 2019-nCoV novel coronavirus outbreak. International Journal of Interactive Multimedia and Artificial Intelligence, 6(1), 132-140.

Freimuth, V., Linnan, H. W., & Potter, P. (2000). Communicating the threat of emerging infections to the public. Emerging Infectious Diseases, 6(4), 337-347.

Fung, I. C. H., Fu, K. W., Ying, Y., Schaible, B., Hao, Y., Chan, C. H., & Tse, Z. T. H. (2013). Chinese social media reaction to the MERS-CoV and avian influenza A(H7N9) outbreaks. Infectious Diseases of Poverty, 2(1), 31.

Glik, D. C. (2007). Risk communication for public health emergencies. Annual Review of Public Health, 28, 33-54.

Greenberg, J., Pyszczynski, T., Solomon, S., Rosenblatt, A., Veeder, M., Kirkland, S., & Lyon, D. (1990). Evidence for Terror Management Theory II: The Effects of Mortality Salience on Reactions to Those Who Threaten or Bolster the Cultural Worldview. Journal of Personality and Social Psychology, 58(2), 308.

Grover, P., Kar, A. K., Dwivedi, Y. K., & Janssen, M. (2019). Polarization and acculturation in US Election 2016 outcomes: Can twitter analytics predict changes in voting preferences. Technological Forecasting and Social Change, 145, 438-460.

Haider, N., Yavlinsky, A., Simons, D., Osman, A. Y., Ntoumi, F., Zumla, A., & Kock, R. (2020). Passengers’ destinations from China: Low risk of Novel Coronavirus (2019-nCoV) transmission into Africa and South America. Epidemiology and Infection, 148, 1-7.

Herath, T., & Rao, H. R. (2009). Protection motivation and deterrence: A framework for security policy compliance in organisations. European

Journal of Information Systems, 18(2), 106- 125.

Huang, C. L., Chung, C.K., Hui, N., Lin, Y. C., Seih, Y. T., Lam, B. C. P., Chen, W. C., Bond, M. H., & Pennebaker, J. W. (2012). The development of the Chinese linguistic inquiry and word count dictionary. Chinese Journal of Psychology, 54(2), 185-201.

Johnston, A. C., & Warkentin, M. (2010). Fear appeals and information security behaviors: An empirical study. MIS Quarterly, 34(3), 549- 566.

Jun, E. R., Kim, S. H., Cho, Y. J., Kim, Y. A., & Lee, J. Y.(2019). The influence of negative mental health on the health behavior and the mortality risk: Analysis of Korean longitudinal study of aging from 2006 to 2014. Korean Journal of Family Medicine, 40(5), 297-306.

Kahneman, D. (2011). Thinking, fast and slow. Macmillan.

Kim, J., Bae, J., & Hastak, M. (2018). Emergency information diffusion on online social media during storm Cindy in U.S. International Journal of Information Management, 40, 153- 165.

Kraus, N. N., & Slovic, P. (1988). Taxonomic analysis of perceived risk: Modeling individual and group perceptions within homogeneous hazard domains. Risk Analysis, 8(3), 435-455.

Krupp, L. B., & Elkins, L. E. (2000). Fatigue and declines in cognitive functioning in multiple sclerosis. Neurology, 55(7), 934-939.

Lebel, R. D. (2017). Moving beyond fight and flight: A contingent model of how the emotional regulation of anger and fear sparks proactivity. Academy of Management Review, 42(2), 190- 206.

Leidner, D. E., Pan, G., & Pan, S. L. (2009). The role of IT in crisis response: Lessons from the SARS and Asian Tsunami disasters. The Journal of Strategic Information Systems, 18(2), 80-99.

Liang, H., & Xue, Y. (2009). Avoidance of information technology threats: A theoretical perspective. MIS Quarterly, 33(1), 71-90.

Luo, X., Zhang, J., & Duan, W. (2013). Social media and firm equity value. Information Systems Research, 24(1), 146-163.

Lupton, D. (1995). Risk as Moral Danger: The social and political functions of risk discourse in public health. International Journal of Health Services, 23(3), 425-435.

Lütkepohl, H. (2005). New introduction to multiple time series analysis. Springer Science & Business Media.

Marston, H. D., Folkers, G. K., Morens, D. M., & Fauci, A. S. (2014). Emerging viral diseases: Confronting threats with new technologies. Science Translational Medicine, 6, 1-6.

McKimm-Breschkin, J. L., Selleck, P. W., Usman, T. B., & Johnson, M. A. (2007). Reduced sensitivity of influenza A (H5N1) to oseltamivir. Emerging Infectious Diseases, 13(9), 1354-1357.

Medley, G. F., & Vassall, A. (2017). When an emerging disease becomes endemic. Science, 357(6347), 156-158.

Morens, D. M., Folkers, G. K., & Fauci, A. S. (2004). The challenge of emerging and re-emerging infectious diseases. Nature, 430, 242-249.

Oh, S., Lee, S. Y., & Han, C. (2020). The effects of social media use on preventive behaviors during infectious disease outbreaks: The mediating role of self-relevant emotions and public risk perception. Health Communication, 1-10.

Oh, S., & Syn, S. Y. (2015). Motivations for sharing information and social support in social media: A comparative analysis of Facebook, Twitter, Delicious, YouTube, and Flickr. Journal of the Association for Information Science and Technology, 66(10), 2045-2060.

Pan, S. L., Pan, G., & Leidner, D. (2012). Crisis response information networks. Journal of the Association for Information Systems, 13(1), 31- 56.

Pang, N., & Law, P. W. (2017). Retweeting# WorldEnvironmentDay: A study of content features and visual rhetoric in an environmental movement. Computers in Human Behavior, 69, 54-61.

Park, J. H., Gu, B., Leung, A. C. M., & Konana, P. (2014). An investigation of information sharing and seeking behaviors in online investment communities. Computers in Human Behavior, 31, 1-12.

Pennebaker, J. W., Booth, R. J., & Francis, M. E. (2007). Linguistic inquiry and word count: LIWC2007. LIWC2007 Operators Manual.

Peters, K., Kashima, Y., & Clark, A. (2009). Talking about others: Emotionality and the dissemination of social information. European Journal of Social Psychology, 39(2), 207-222.

Rathore, A. K., & Ilavarasan, P. V. (2020). Pre- and post-launch emotions in new product development: Insights from twitter analytics of three products. International Journal of Information Management, 50, 111-127.

Simon, T., Goldberg, A., & Adini, B. (2015). Socializing in emergencies: A review of the use of social media in emergency situations. International Journal of Information Management, 35(5), 609-619.

Skinner, J. (2013). Natural disasters and twitter Thinking from both sides of the tweet. First Monday, 18(9), https://doi.org/10.5210/fm. v18i9.4650.

Slovic, P. (1987). Perception of risk. Science, 236, 280-285.

Smith, R. D. (2006). Responding to global infectious disease outbreaks: Lessons from SARS on the role of risk perception, communication and management. Social Science & Medicine, 63(12), 3113-3123.

Snyder, L. B., & Rouse, R. A. (1995). The media can have more than an impersonal impact: The case of AIDS risk perceptions and behavior. Health Communication, 7(2), 125-145.

Song, P., Xue, L., Rai, A., & Zhang, C. (2018). The ecosystem of software platform: A study of asymmetric cross-side network effects and platform governance. MIS Quarterly, 42(1), 121-142.

Stevenson, M., & Taylor, B. J. (2018). Risk communication in dementia care: Family perspectives. Journal of Risk Research, 21(6), 692-709.

Stieglitz, S., & Dang-Xuan, L. (2013). Emotions and information diffusion in social media: Sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29(4), 217-248.

Stramer, S.L., Hollinger, F. B., Katz, L. M., Kleinman, S., Metzel, P. S., Gregory, K. R., & Dodd, R. Y. (2009). Emerging infectious disease agents and their potential threat to transfusion safety. Transfusion, 49,1S-29S.

Sturges, D. L. (1994). Communicating through crisis: A strategy for organizational survival. Management Communication Quarterly, 7(3), 297-316.

Sun, X. D., & Wang, H. Y. (2009). Epidemic status and prevention strategies of emerging infectious diseases. Shanghai Journal of Preventive Medicine, 21(9), 461-465.

Taylor, M., Wells, G., Howell, G., & Raphael, B. (2012). The role of social media as psychological first aid as a support to community resilience building. Australian Journal of Emergency Management, The, 27(1), 20-26.

Tellis, G. J., MacInnis, D. J., Tirunillai, S., & Zhang, Y. (2019). What drives virality (sharing) of online digital content? The critical role of information, emotion, and brand prominence. Journal of Marketing, 83(4), 1-20.

Thistlethwaite, J., Henstra, D., Brown, C., & Scott, D. (2018). How flood experience and risk perception influences protective actions and behaviours among Canadian homeowners. Environmental Management, 61(2), 197-208.

Tirunillai, S., & Tellis, G. J. (2012). Does chatter really matter? Dynamics of user-generated content and stock performance. Marketing Science, 31(2), 198-215.

Vaast, E., Safadi, H., Lapointe, L., & Negoita, B. (2017). Social media affordances for connective action: An examination of microblogging use during the Gulf of Mexico Oil Spill. MIS Quarterly, 41(4), 1179-1205.

Vermeulen, A., Vandebosch, H., & Heirman, W. (2018). #Smiling, #venting, or both? Adolescents’ social sharing of emotions on social media. Computers in Human Behavior, 84, 211-219.

Wang, C., Zhou, Z., Jin, X., Fang, Y., & Lee, M. K. (2017). The influence of affective cues on positive emotion in predicting instant information sharing on microblogs: Gender as a moderator. Information Processing & Management, 53(3), 721-734.

Wang, J., Xiao, N., & Rao, H. R. (2015). Research note: An exploration of risk characteristics of information security threats and related public information search behavior. Information Systems Research, 26(3), 619-633.

Wildemuth, B. M. (2004). The effects of domain knowledge on search tactic formulation. Journal of the American Society for Information Science and Technology, 55(3), 246-258.

Wolff, K., Larsen, S., & Øgaard, T. (2019). How to define and measure risk perceptions. Annals of Tourism Research, 79, 1-9.

Woosnam, K. M., Draper, J., Jiang, J. K., Aleshinloye, K. D., & Erul, E. (2018). Applying selfperception theory to explain residents' attitudes about tourism development through travel histories. Tourism Management, 64, 357-368.

Xu, L., Lin, H., Pan, Y., Ren, H., & Chen, J. (2008). Constructing the affective lexicon ontology. Journal of the China society for scientific and technical information, 27(2), 180-185.

Zhang, H. P., Gao, K., Huang, H. Y., & Zhao, Y. (2014). Big data search and mining. Science Press.

## Appendix A

The influence of control variables on sharing behavior

The IRFs results of control variables are illustrated in Table A1.

Table A1. IRFs Results of Control Variables

<table><tr><td rowspan="2" colspan="2"></td><td colspan="6">Time window</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td rowspan="5">PositiveEmotion→SharingBehavior</td><td>Overall</td><td>829</td><td>572</td><td>331</td><td>283</td><td>263</td><td>247</td></tr><tr><td>Buildup</td><td>8</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Breakout</td><td>1614</td><td>886</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Abatement</td><td>557</td><td>485</td><td>368</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Termination</td><td>32</td><td>33</td><td>25</td><td>14</td><td>13</td><td>8</td></tr><tr><td rowspan="5">NegativeEmotion→SharingBehavior</td><td>Overall</td><td>951</td><td>647</td><td>376</td><td>319</td><td>294</td><td>275</td></tr><tr><td>Buildup</td><td>20</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Breakout</td><td>1825</td><td>1019</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Abatement</td><td>586</td><td>428</td><td>368</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Termination</td><td>37</td><td>36</td><td>19</td><td>10</td><td>9</td><td>-</td></tr><tr><td rowspan="5">InformationVolume→SharingBehavior</td><td>Overall</td><td>952</td><td>639</td><td>367</td><td>312</td><td>275</td><td>268</td></tr><tr><td>Buildup</td><td>16</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Breakout</td><td>1768</td><td>992</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Abatement</td><td>845</td><td>470</td><td>422</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Termination</td><td>32</td><td>36</td><td>14</td><td>-</td><td>-</td><td>-</td></tr></table>

## About the Authors

Liwei Xu is a PhD candidate in the School of Economics and Management, Dalian University of Technology, China. Her work has been published in Information & Management, among other outlets. Her current research interests include machine learning, emergency management, and big data analysis.

Jiangnan Qiu is a professor in the School of Economics and Management, Dalian University of Technology, China. His work has been published in Decision Support Systems, Information & Management, Information Processing & Management, and Computers in Human Behavior, among other outlets. His primary research interests are emergency management and big data analysis. His research has been supported by the National Natural Science Foundation of China.

Wenjing Gu is a PhD candidate in the School of Economics and Management, Dalian University of Technology, China. Her research interests include emergency management and big data analysis.

Yidi Ge is a master’s degree candidate in the School of Economics and Management, Dalian University of Technology, China. Her work has been published in Information Processing & Management, among other outlets. Her current research interests include machine learning, data analysis, and emergency management.

Copyright © 2020 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
