---
otero_id: 4134
otero_key: "TFWXH6H6"
title: "Mutual influences between message volume and emotion intensity on emerging infectious diseases: An investigation with microblog data"
authors: "Jiangnan Qiu; Liwei Xu; Jingguo Wang; Wenjing Gu"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103217"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Mutual Influences between Message Volume and Emotion Intensity on Emerging Infectious Diseases: An Investigation with Microblog Data

Jiangnan Qiu, Liwei Xu, Jingguo Wang, Wenjing Gu

![](/api/attachments/TFWXH6H6/fulltext/images/18bf2ab5af8200703fb2220e643c250d289c2f260ade89684c5301396b8211c9.jpg)

PII: S0378-7206(18)30632-3

DOI: https://doi.org/10.1016/j.im.2019.103217

Reference: INFMAN 103217

To appear in: Information & Management

Received Date: 1 August 2018

Revised Date: 22 October 2019

Accepted Date: 25 October 2019

Please cite this article as: Qiu J, Liwei X, Wang J, Gu W, Mutual Influences between Message Volume and Emotion Intensity on Emerging Infectious Diseases: An Investigation with Microblog Data, Information and amp; Management (2019), doi: https://doi.org/10.1016/j.im.2019.103217

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# Mutual Influences between Message Volume and Emotion Intensity on Emerging Infectious Diseases: An Investigation with Microblog Data

Jiangnan Qiu School of Economics and Management, Dalian University of Technology Dalian 116024, China Email: qiujn@dlut.edu.cn Tel: +8641184707648 Liwei Xu School of Economics and Management, Dalian University of Technology Dalian 116024, China Email: xuliwei@mail.dlut.edu.cn, Tel: +8618342209446 Jingguo Wang Department of Information Systems and Operations Management, Co Texas at Arlington, Arlington, Texas 76019, United States Email: jwang@uta.edu Tel: +18172723502

Wenjing Gu School of Economics and Management, Dalian University of Technology Dalian 116024, China Email: 598228662@qq.com, Tel: +8618340879297

## Abstract

The dynamic interdependence between microblog volume and emotions expressed in message content has been largely underexplored. To understand the public’s reaction to emerging infectious diseases, we draw upon theories in psychology and social media, and propose that there is a cyclical relationship between message volume and the intensity of emotions (positive or negative) in which they influence each other positively over time. Furthermore, negative and positive emotions mutually suppress each other, yet are autocorrelated, respectively. Relying on more than 560,000 microblogs collected from Sina Weibo between February 2013 and June 2013 on the outbreak of avian influenza in China, we used vector autoregression to test the research model. We find a cyclical relationship between microblog volume and the intensity of negative emotions (fear in particular, a subcategory of negative emotions). Microblog volume positively contributes to positive emotions. While the intensity of negative emotions, and that of positive emotions is autocorrelated, respectively, surprisingly our results suggest that negative emotion intensity positively affects positive emotion intensity. We further rely on impulse response functions to illustrate how the impacts of a variable on another change over time, and generalized forecast error variance decomposition to understand the importance of each variable contributing to the others. Theoretical and practical implications of the study are discussed.

Keywords: social media; emerging infectious diseases; microblog volume; emotion intensity; dynamic mutual influences; vector autoregression.

## Introduction

Emerging infectious diseases (EIDs) (such as avian influenza) are one of the greatest threats to public health [1], often caused by newly identified viruses or strains that the public has little to no understanding of [2]. EID incidents [3] usually spark wide media coverage alarming the public [4]. Web 2.0 technologies, such as microblogging or tweeting, enable the public to share their own stories and feelings about EID events [5]. Analyzing microblogs or tweets may help to understand the public’s reactions to EID threats [6].

Researchers have suggested relying on the volume of related posts and emotions expressed in user-generated content to help organizations, such as Centers for Disease Control (CDC), to better understand the epidemic and public concerns [7]. A number of studies have proposed to monitor disease incidents based on the frequency of relevant searches or keywords in user-generated content [8, 9]. The fundamental premise is that people concerned about a disease are likely to seek information online or discuss it through social media. User-generated content can help determine whether there is a disease outbreak, and identify the public’s emotions toward EIDs [10]. Emotions expressed in user-generated content reflect how the public react to EIDs [11]. Furthermore, in linking emotion intensity and microblog volume, a number of studies [12, 13] have analyzed the emotions embodied in user-generated content, such as microblogs and tweets lead to more tweeting or retweeting.

However, there is little investigation on how microblog volume and the intensity of emotions (including positive and negative emotions) mutually affect each other, and how their interdependence evolves over time in the context of EIDs. This study aims to bridge this literature gap. From a theoretical perspective, such an investigation will deepen our understanding of the evolving relationships between message volume and emotion intensity in the context of public crises. From a technical perspective, the consideration of dynamic mutual influences is crucial in reducing estimation biases on the impact of emotion intensity on microblog volume, or microblog volume on emotion intensity.

Drawing upon theories in psychology and social media, we develop a research model proposing that microblog volume and emotion intensity (negative or positive) influence each other positively over time. Furthermore, negative and positive emotions mutually suppress each other, yet are autocorrelated, respectively. Microblog volume is also autocorrelated. To test our research model, we collected more than 560,000 microblogs from Sina Weibo discussing avian influenza (H7N9)<sup>1</sup> during its outbreak between February 2013 and June 2013 in China [14]. Sina Weibo is the biggest social network in China, similar to Twitter. It allows users to post microblogs of 140 characters and offers features comparable to tweeting and retweeting [15]. The vector autoregression (VAR) methodology was used to analyze the dynamic interdependence among message volume, negative and positive emotion intensity. The methodology allows analyzing a system of interdependent variables without imposing many assumptions and restrictions [16]. Fitting our research purpose, it provides a proper approach to understand the dynamic relationships and feedback effects between microblog volume and emotion intensity.

The results show a cyclical relationship between microblog volume and negative emotions. Especially, microblog volume has an immediate but fast decay influence on negative emotion intensity, and negative emotion intensity has a delayed but stable and persistent influence on microblog volume. The cyclical relationship is especially strong between microblog volume and fear, a subcategory of negative emotions. Microblog volume also contributes to positive emotions. Microblog volume, negative emotions, and positive emotions are autocorrelated, respectively, presenting a phenomenon of inertia. Surprisingly, negative emotions positively influence positive emotions. Further, subcategories of negative emotions with high arousal have more significant impacts on positive emotions. Subcategories of emotions with high arousal, regardless of positive or negative have a more significant influence on themselves. In other words, high arousal emotions are more persistently existing and contagious. The results of impulse response functions (IRFs) show that negative emotions have a delayed effect on the microblog volume, and it has the highest impact at the fifth time window (in one hour units). Generalized forecast error variance decomposition (GFEVD) analysis demonstrates that each variable is mainly accounted by its own shock.

This study makes several contributions to research and practice. First, this study contributes to understanding the public’s reaction to EID events with social media data. While most prior studies provide a snapshot of the relationship between microblog volume and emotion intensity by considering it to be one-way and time invariant, this study recognizes its dynamic and mutually influencing nature. It is important to recognize that the impact of emotion on behavior or vice versa is immediate or has some lead time to reach its maximum. Second, we validate the autocorrelation and extend the studies in human emotion. The study shows that emotions with high arousal could be more contagious and easily repaired. Prior studies in this area rarely explore the important role of arousal in the process of emotional contagion and repair. Third, our study suggests the importance of proper interventions, because negative emotions could build up over the course of an EID event through a spiral process. As our results suggest, part of the reason may be because of the inertia of negative emotions, and the other part is that negative emotions influence the public to act in such a way that further increases the intensity of negative emotions. The intensity of negative emotions may escalate that need for proper interventions. For practices, our analytical framework can be used as a foundation to construct models to monitor EID outbreaks, and analyze the evolvement of the public’s reaction. By recognizing the time-varying and dynamic relationships between microblog volume and emotions, we may improve the efficiency of forecasting models that could predict the trend of the public’s reaction and provide information for relevant stakeholders.

The rest of the paper is organized as follows. Section 2 provides literature review. Section 3 provides the theoretical background. Section 4 develops the research model for our empirical analyses. Section 5 presents the strategies of data analyses and estimation methods. Section 6 discusses the estimation results and provides robustness analyses. Section 7 discusses findings, implications for theory and practice and concludes the paper.

## Related Literature

## Research on the Public’s Reaction to EID Events

Research on the public’s reaction to EID events through the use of user-generated content mainly explores two aspects (Table 1): (1) the pattern and lifecycle of the public’s reaction to EID events; and (2) early warning of the EIDs outbreak by detecting the public’s reaction or relevant health behaviors. These studies provide new methodologies to detect disease outbreaks based on user-generated content; they lay a foundation for further analysis of the public’s reaction to EID events. The basic assumption is that people who are concerned about a disease will seek relevant information on the Internet, and therefore, the development of crisis can be estimated based on the search frequency of relevant keywords. However, these studies largely ignore the importance of emotions expressed in user-generated content. Such emotions may reflect the public’s attitude, and impact how the public will think and evaluate social information subsequently. Emotions could be important for understanding the public’s reaction toward a certain event, especially a crisis.

Table 1. Reviews on the public’s reaction to EID events

<table><tr><td>Research Problem</td><td>Data source</td><td>Starting point</td><td>Result</td><td>EID type</td><td>Ref.</td></tr><tr><td rowspan="2">Patterns of the public's reaction toward EID events</td><td>Poll data</td><td>Attention to news coverage</td><td>Public attention peaks when there are new cases and decreases rapidly when the diseases seem to have been contained.</td><td>Avian influenza</td><td>(Ho,2007)</td></tr><tr><td>Google query and Twitter trends</td><td>Keyword searches</td><td>People react significantly to both outbreaks online, but the magnitudes are different.</td><td>MERS, avian influenza</td><td>(Fung,2013)</td></tr><tr><td rowspan="5">Research on surveillance and early warning by detecting the public's reaction or health behaviors related to EID events</td><td>Google trends</td><td>Health-seeking behavior</td><td>Google search queries can be used for early detection.</td><td>Seasonal influenza</td><td>(Ginsberg,2009)</td></tr><tr><td>Social media</td><td>Health behaviors and emotions</td><td>Clusters of negative vaccine sentiments lead to clusters of unprotected individuals, and the likelihood of disease outbreaks is greatly increased.</td><td>Pandemic influenza</td><td>(Salathé,2011)</td></tr><tr><td>Twitter</td><td>Health behaviors</td><td>The frequency of the diseases mentioned can be used to estimate disease outbreak.</td><td>Pandemic influenza</td><td>(Signorini,2011)</td></tr><tr><td>Twitter</td><td>Content analysis</td><td>Twitter messages can be highly relevant for early hints regarding public health threats to a certain extent.</td><td>Swine flu, Pandemic influenza</td><td>(Krieck,2011)</td></tr><tr><td>Sina</td><td>Popularity of</td><td>Microblogs are meaningful for EID events</td><td>Avian flu</td><td>(Liu,2014)</td></tr><tr><td>microblog</td><td>microblog</td><td>management.</td><td></td><td></td></tr><tr><td>Sina microblog</td><td>The public attention to the outbreak</td><td>The first three days of an epidemic is a critical period for the authorities to take appropriate action through internet surveillance to prevent and control the epidemic.</td><td>Avian flu</td><td>(Gu,2014)</td></tr><tr><td>Baidu attention index</td><td></td><td></td><td></td><td></td></tr><tr><td>Twitter</td><td>Contents of Twitter</td><td>Social media is useful for tracking a disease threatening public health.</td><td>Pandemic influenza</td><td>(Jain,2015)</td></tr><tr><td>Twitter</td><td>Information dissemination</td><td>The results demonstrate the usefulness of Twitter mining to inform public health education.</td><td>Ebola</td><td>(Odlum,2015)</td></tr><tr><td>Survey</td><td>Outbreak mechanism</td><td>Communication behaviors influence preventive behaviors during the outbreak of EID events.</td><td>MERS</td><td>(Yoo,2016)</td></tr><tr><td>Google trends and Twitter</td><td>Predict future development trends of EID events</td><td>These internet-based data streams can be used as timely and complementary ways to assess the dynamics of the outbreak.</td><td>Zika virus</td><td>(McGough,2017)</td></tr></table>

## Research on Social Media Behavior and Emotions in User-generated Content

Previous studies on the relationship between behavior and emotions focus on several aspects. As shown in Table 2, some studies have investigated the influence of valence on social media behaviors (such as tweeting/retweeting and/or blogging) or performing field experiments [13, 27], especially how positive emotions, negative emotions, and subcategories of these emotions may shape behavior. Some have examined emotional contagion in different contexts [32, 33]. But so far, few studies have examined the feedback effects of content generation behavior on emotions in the context of social media. In particular, studies on the public’s reaction to EIDs are rare; especially investigations of the mutual influences between microblog volume and emotion intensity in the context of social media. Bridging the literature gap, our study develops a model of mutual influences between microblog volume and emotion intensity. Our examination of the subcategories of emotions can further illustrate the robustness in relationships.

Table 2. Reviews on behavior and emotions

<table><tr><td>Research Problem</td><td>Data source</td><td>Starting point</td><td>Result</td><td>Ref.</td></tr><tr><td rowspan="2">Influence of emotions on behavior</td><td>Mozilla browser</td><td>Positive and negative emotions</td><td>Positive and negative emotions influence feedback differently.</td><td>(Joyce,2006)</td></tr><tr><td>Participants,questionnaire</td><td>Subcategories ofemotions and different people</td><td>People may be more likely to share stories aboutothers that arouse emotions.</td><td>(Peters,2009)</td></tr><tr><td rowspan="6"></td><td>Participants</td><td>Emotion and emotional sharing</td><td>Emotion elicits the social sharing of emotion.</td><td>(Rimé,2009)</td></tr><tr><td>Google Groups</td><td>Positive and negative emotions</td><td>People who use affective, emotional language in their messages receive more feedback than those who do not.</td><td>(Huffaker,2010)</td></tr><tr><td>New York Times articles</td><td>Emotion and sharing</td><td>Both articulated emotion and physiological arousal can influence the likelihood of articles being shared.</td><td>(Berger,2012)</td></tr><tr><td>Political blogs</td><td>Positive, negative, and neutral emotions</td><td>Blog entries with either more positive or negative sentiments tend to receive significantly more comments compared to sentiment-neutral ones.</td><td>(Dang-Xuan,2012)</td></tr><tr><td>Twitter</td><td>Quantity and speed of sharing behavior</td><td>Emotionally charged Twitter messages tend to be retweeted more often and more quickly, especially ones with a negative emotion.</td><td>(Stieglitz,2013)</td></tr><tr><td>Twitter</td><td>Quantify the effect of positive and negative emotions</td><td>Positive and negative emotions have different effects on information diffusion.</td><td>(Ferrara,2015)</td></tr><tr><td rowspan="4">Emotional contagion</td><td>Participants</td><td>Emotional contagion</td><td>Emotional contagion occurs in text-based communication.</td><td>(Hancock,2008)</td></tr><tr><td>Facebook</td><td>Emotional contagion</td><td>User's emotion positively impacts their friend's emotion.</td><td>(Kramer,2012)</td></tr><tr><td>Facebook</td><td>Emotional contagion</td><td>Emotion expressed by others on Facebook influences others' emotions, and positive emotions have a suppression effect on negative emotions, and vice versa.</td><td>(Kramer,2014)</td></tr><tr><td>Facebook</td><td>Emotional contagion</td><td>Rainfall affects the emotional status of users, which also influences their friends.</td><td>(Coviello,2014)</td></tr></table>

The social transmission of emotional content may be driven by more than just valence, and the arousal of emotions could be another factor. Arousal is a subjective state of feeling activated or deactivated. Emotions differ on the level of physiological arousal they evoke [35]. Given their degree of physiological impulse and activation of emotion arousal, these subcategories of emotions can be divided into different levels [36]. Table 3 shows the valence and arousal level of Ekman’s basic subcategories of emotions [37], including happiness, surprise, fear, sadness, anger, and disgust. User-generated content containing high-arousal emotions is more likely to be shared [13]. Subcategories of emotions have different valence. Happiness is considered to be positive [38]. Fear [39], sadness [40], anger [40], and disgust [41] are negative. As surprise can be either positive or negative, the valence of surprise depends on the triggering event. In the context of a harmful event, attack, or threat to survival, surprise has been often considered to have a negative valence [42].

Table 3. Emotion and arousal

<table><tr><td></td><td>Happiness</td><td>Sadness</td><td>Anger</td><td>Fear</td><td>Disgust</td><td>Surprise</td></tr><tr><td>Emotion Valence</td><td>Positive</td><td>Negative</td><td>Negative</td><td>Negative</td><td>Negative</td><td>Negative</td></tr><tr><td>High Arousal</td><td>√</td><td></td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>Low Arousal</td><td></td><td>√</td><td></td><td></td><td>√</td><td></td></tr></table>

## Theoretical Background

To develop our research model, we draw upon theories and empirical findings, particularly the feedback theory proposed by Baumeister [43]. The theory views the mutual influences between behavior and emotions as a feedback system. It considers that one’s emotional states can be pursued and regulated by behavior. Individuals may choose their behavior to pursue anticipated emotional outcomes. After performing the chosen behavior, individuals experience emotional outcomes.

![](/api/attachments/TFWXH6H6/fulltext/images/3acc658c311b450b61765f0e748ef091e5518567c9308d47fd51250bf7fa1aee.jpg)  
Note: 1: Behavior leads individuals to experience emotions; 2: Emotions affect individuals’ behavioral choices; 3: Emotions may be contagious; 4: Behavior may be repeated or imitated by others.

Figure 1. Loop between behavior and emotions suggested by the feedback theory

Figure 1 depicts the mutual influences between behavior and emotions suggested by the feedback theory. Relationship 1 describes that individuals’ behavior leads them to experience emotions. The chosen behavior may result in certain emotional outcomes. The experienced emotional outcomes can provide feedback about the behavior. Individuals may learn from their experienced emotions, and subsequently modify their perception or cognition regarding the behavior. In other words, emotions leave an affective cue that may guide future behavior. Further, individuals are often goal-directed and behave based on their needs [44]. Once their needs are satisfied by their actions, they may experience positive emotions [45]. Otherwise, they may have negative emotions [45].

Relationship 2 suggests that individuals’ emotions affect their behavioral choices. Individuals’ emotional state affects the choice of behavior because emotional state influences how they attend to, process, and use information. Emotions may alter individuals’ desire for information and drive behavior through cognitive appraisal and physiological arousal [13]. As discussed above, in the context of user-generated content, it has been shown that emotional microblogs embodying verbal cues [13], such as emotional words or emotional framing, may elicit users’ physiological arousal, attract more attention, and spread faster [13].

Relationship 3 suggests that emotions may be contagious. Within a group of individuals, one’s emotions are susceptible to external stimuli and others’ emotions. In other words, during the process of interactions, one’s emotional state may transfer to others’, because individuals have the tendency to automatically mimic and synchronize facial expressions, vocalization, postures, and movements with others [33]. As such, one’s emotional states may be contagious through the conscious and unconscious induction [34]. Subsequently, individuals who interact with each other may experience similar types of emotions but suppress other types [32].

Relationship 4 suggests behavior may be repeated or imitated by others. Within a group, when an individual has limited knowledge, and the outcomes have a lot of uncertain, and/or there may be no proper anticipation of rewards or punishment guiding one’s behavior, an individual may discount his or her own information, but look for others’ behavior. In other words, individuals may rely on others’ actions to guide their behavior [46]. Thus, herding may arise as individuals take the same or similar choices as others in a context where they have limited knowledge [46].

## Hypotheses Development

Following the feedback theory, in the context of EID events with social media data, we explore the mutual influences of microblog volume and emotions expressed by microblogs that may evolve over time, and understand how information dissemination is facilitated and public emotional states change on Weibo (or other social media platforms) in the context of EID events. Figure 2 describes the research model of mutual influences between microblog volume and emotion intensity based on the feedback theory [43]. We propose that message volume induces positive and negative emotions because of the satisfaction of information demand and the burden of information overload (Hypothesis 1 and 2). Positive and negative emotions are autocorrelated, respectively, because of emotional contagion (Hypothesis 3 and 4). Positive emotion and negative emotion are mutually suppressed (Hypothesis 5 and 6). Message volume is autocorrelated (Hypothesis 7).

![](/api/attachments/TFWXH6H6/fulltext/images/73c708a072bfc186bd86c39959a2b63c38dbd3565e323b7c9fac0133d6a2ead0.jpg)  
Figure 2. Research hypotheses model on the public’s reaction to EID events<sup>2</sup>

The public fulfill their information needs and decrease their undesired state of uncertainty through social media platforms by tweeting or retweeting. Information is vital to analyze the pandemic and understand apprehension in the population [47]. Tweeting or retweeting facilitates information dissemination through social networks [13]. Liu et al. [48] also have reported that enjoyment and happiness are considered main forms of motivation for Twitter users, with tweeting or retweeting being the primary means to achieve it. Therefore, we propose:

Hypothesis 1 (H1): Microblog volume related to the EID event has a positive impact on the intensity of positive emotions articulated in microblogs regarding an EID event.

However, on the other hand, the public may not be satisfied with the use of social media. The public might also be overwhelmed by the large amount of information on social media about an EID event. Researchers [49] point out that information tweeted or retweeted has different quality and credibility. Previous research also identifies a number of uncertainties associated with information tweeted or retweeted through social media, the most important being credibility [50]. Microblogs may contradict each other, which deepens the public’s feeling of uncertainty. If the usage behavior of microblogs has not reached the public’s goal, they may have ungratified feelings. Thus, negative emotions, such as fear or sadness, may be triggered. Further, Miller et al. [44] and Sicilia et al. [45] suggest that too much information leads to overload, and individuals may experience negative emotions, such as anxiety and disgust. Thus, negative emotions may also be aroused because of the large scale of tweeting or retweeting. Therefore, we propose:

Hypothesis 2 (H2): Microblog volume related to the EID event has a positive impact on the intensity of negative emotions articulated in microblogs regarding an EID event.

During the process of emotion evolvement, positive and negative emotions may be autocorrelated, respectively. We define emotional autocorrelation as the emotion intensity in a current time window, which is correlated with that in a later time window(s). Emotional contagion results from social influence [51]. It is observed that Facebook users are likely to make posts having valence consistent with the ones they follow, even several days later [32]. On the basis of Facebook data, Coviello et al. [34] find that rainfall directly influences the emotional content of status messages, as well as the status messages of friends who are not experiencing rainfall. Kramer et al. [33], also using Facebook data, show that after users make status updates with emotional content, their friends are significantly more likely to post content with similar emotional tendencies later on. Thus, the emotional autocorrelation process is consistent with the emotional contagion process, as emotional content may be spread from one user to another subsequently. Therefore, we propose:

Hypothesis 3 (H3): The intensity of positive emotions articulated in microblogs regarding an EID event is autocorrelated

Hypothesis 4 (H4): The intensity of negative emotions articulated in microblogs regarding an EID event is autocorrelated.

Positive and negative emotions may suppress each other. As stated above, the emotions expressed by friends on social media influence our own emotions. Kramer [32] tests whether emotional contagion works outside of in-person communication by investigating whether the amount of content with positive and negative emotions on Facebook would have an effect on the content of subsequent posts. The results show that when positive posts are reduced, people produce fewer positive posts but more negative posts; when negative posts are reduced, positive posts increase. This phenomenon of negative (or positive) posts reducing positive (or negative) ones is referred to as emotional suppression [52], in which the use of positive (or negative) emotion words buffers users’ friends against negativity (positivity). Therefore, we hypothesize:

Hypothesis 5 (H5) The intensity of positive emotions has a negative impact on the intensity of negative emotions articulated in microblogs regarding an EID event.

Hypothesis 6 (H6) The intensity of negative emotions has a negative impact on the intensity of positive emotions articulated in microblogs regarding an EID event.

Furthermore, the public’s behavior may also affect each other, known as herding [46]. In the context of EID events, the public are likely to do what others are doing because of the threat and uncertainty they face regarding the development of such crisis [53]. Tweeting or retweeting with others may help spread the word to decrease someone’s uncertainty in the situations with an urgent need of immediate and accurate information [54]. Therefore, tweeting or retweeting in the current time window may influence that in the next time window. We posit the hypothesis:

Hypothesis 7 (H7) Microblog volume related to the EID event is autocorrelated.

## Research Methodology

Our analysis process has four steps: data acquisition, feature calculation, time series calculation, and finally, estimation. First, we used a web crawler to obtain relevant microblogs related to avian influenza (H7N9) from Sina Weibo between February 2013 and June 2013. Second, we used the Natural Language Processing and Information Retrieval (NLPIR) system from the Chinese Academy of Sciences to preprocess microblog data. We used the Lin Hongfei ontology library [55] to obtain feature vectors of microblogs measuring the intensity of positive and negative emotions, as well as the intensity of subcategories of emotions. Third, we aggregated a measure across all microblogs within a time window and formed time series feature vectors. Fourth, we employed the unit root test to verify whether the time series data are stationary, and then constructed a VAR model.

## Data and Context Description

There are three categories of EID events [56]: (1) diseases previously known as noninfectious redefined as EIDs, such as peptic ulcers and adult T cell lymphoma; (2) diseases known as EIDs in modern times, such as the hepatitis C virus, Lyme disease, and legionnaires disease; (3) diseases which never existed in the past, such as avian influenza, Zika virus, and SARS.

We collected Sina Weibo microblog data on avian influenza (H7N9, category 3). Avian influenza (H7N9) received extensive public attention. Since the disease’s emergence in China on

February 19, 2013, it infected 217 humans and resulted in 57 deaths, characterized by rapidly progressive pneumonia, respiratory failure, acute respiratory distress syndrome, and fatal outcomes [57]. The biological features of the virus and its pandemic potential had caused global concern [57]. By April 2013, although the epidemic had declined quickly after the closure of live poultry markets, new cases in humans were still emerging and the stream of the Chinese public’s opinions did not slow down until June of that same year. Following prior research [19], we identified microblogs by searching keywords to obtain microblogs related to the EID event between February 2013 and June 2013 on Sina Weibo. We searched hour by hour, which the minimum possible time interval was allowed. We used several keywords, including H7N9, avian influenza, flu, vaccine, symptom, syndrome, and illness (these words are “禽流感，疫苗，症状， 综合症，疾病” in Chinese). We found 565,427 microblogs between February 19, 2013 and June 15, 2013. To test the research model, we measured these variables in each time window: (i) microblog volume, (ii) the intensity of positive emotions, and (iii) the intensity of negative emotions.

We applied the Chinese Academy of Sciences segmentation system NLPIR to preprocess (segmentation and stop words removal) the microblog data for text analysis. Because there are no spaces between words in Chinese sentences, we therefore used NLPIR to separate sentences into words and then delete stop words. NLPIR is one of the top systems in Chinese word segmentation systems [58]. Its accuracy reaches more than 95% in segmenting words [58].

For subcategories of emotions, we used Ekman’s six basic emotion categories as a basis [37]. As mentioned in the section of Literature Review, the subcategory of positive emotions is happiness, while the subcategories of negative emotions are as follows: (i) surprise, (ii) fear, (iii) sadness, (iv) anger, and (v) disgust. To obtain the emotions feature matrix of the microblogs, we employed the Lin Hongfei ontology library [55] to calculate the emotion intensity of each microblog. Lin Hongfei ontology library is a famous dictionary in China, similar to the dictionary of Linguistic Inquiry and Word Count. There are two dimensions in the Lin Hongfei ontology library, including valence and weight. The valence values of positive and negative emotions are 1 and -1, respectively. Weight represents the strength of emotion words. Therefore, this ontology library can be used as the basis to obtain the emotion intensity of each microblog explained below.

Definition 1. (Feature Vectors of Emotion Intensity and Microblog Volume) ??????????????<sup>(??)</sup> denotes an emotion feature vector to each microblog, according to the different type of emotions constituted in the content. Each one can be viewed as a 6-dimensional emotion vector $e m o t i o n ^ { ( n ) } = \{ e m o t i o n _ { i } ^ { 1 } , \dots , e m o t i o n _ { i } ^ { n } , \dots , e m o t i o n _ { 6 } ^ { n } \}$ . ??????????????<sup>??</sup> represents the intensity of emotion i and $\mathrm { i } = \{ 1 , 2 , 3 , 4 , 5 , 6 \}$ . The flow chart shown in Figure 3 can calculate emotion feature ??????????????<sup>??</sup> of each microblog. The algorithm in Figure 3 was used for the calculation of emotions for microblog n. The input includes the Lin Hongfei ontology library and word series $\{ w _ { 1 } , w _ { 2 } , \ldots , w _ { q } \}$ of microblog n after preprocessing. The output is ??????????o??<sup>??</sup>. ??????????????(??<sub>??</sub>) is the weight value of emotion word $w _ { j }$ . c denotes the weight of emotion word in Lin Hongfei ontology library, m represents the weight of modifier words (the words in front of emotion words) in Lin Hongfei ontology library.

![](/api/attachments/TFWXH6H6/fulltext/images/e20541f011695b1d51a15e360afdcfb5d4d8979c9b6fa384cb7ad49c82d51fc6.jpg)  
Figure 3. Flow chart showing the feature calculation of emotion intensity for each microblog

??????????????????????????????<sup>(n)</sup> denotes the sum intensity of positive emotions of happiness for each microblog; while ??????????????????????????????<sup>(n)</sup> represents the sum intensity of negative emotions (because negative emotions include surprise, fear, sadness, anger, and disgust. Therefore, the value of negative emotions is the sum of the five emotions). ??????????????????????????????<sup>(n)</sup> represents the number of times shared, as shown in the following formula:

$$
\begin{array}{c} \text {positiveEmotion} ^ {\mathrm{(n)}} = [ e m o t i o n _ {1} ^ {n} ] \\ \text {negativeEmotion} ^ {\mathrm{(n)}} = [ e m o t i o n _ {2} ^ {n} + e m o t i o n _ {3} ^ {n} + e m o t i o n _ {4} ^ {n} + e m o t i o n _ {5} ^ {n} + e m o t i o n _ {6} ^ {n} ] (2) \end{array} \tag {1}
$$

$$
m i c r o b l o g V o l u m e ^ {(n)} = [ p o s t i n g _ {1} ^ {n} ]\tag{3}
$$

Definition 2. (Time Series Data for Emotion Intensity and Microblog Volume). We defined a time window as t and the calculation of feature vectors based on all microblog data within the time window, including ??????????????????????????????, ?????????????????????????????? , andMicroblogVolume. We assumed that there are m microblogs at a time window t. ??????????????????????????????, ??????????????????????????????, ?????? ?????????????????????????????? represent the time series of positive emotion intensity, negative emotion intensity, and microblog volume, respectively.

$$
P o s i t i v e E m o t i o n _ {t} = p o s i t i v e E m o t i o n ^ {(1)} + \dots + p o s i t i v e E m o t i o n ^ {(m)}\tag{4}
$$

$$
N e g a t i v e E m o t i o n _ {t} = n e g a t i v e E m o t i o n ^ {(1)} + \dots + n e g a t i v e E m o t i o n ^ {(\mathrm{m})}\tag{5}
$$

$$
M i c r o b l o g V o l u m e _ {t} = m i c r o b l o g V o l u m e ^ {(1)} + \dots + m i c r o b l o g V o l u m e ^ {(m)}\tag{6}
$$

We obtained two sets of time series data, which include the emotions (MicroblogVolume, PositiveEmotion, NegativeEmotion) and subcategories of emotions (MicroblogVolume, Happiness, Surprise, Fear, Sadness, Anger, Disgust) . The descriptive statistics of these variables are in Table 4:

Table 4. Statistic results of variables (t=1)

<table><tr><td rowspan="2"></td><td colspan="4">Time series data</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Skewness</td><td>Kurtosis</td></tr><tr><td>MicroblogVolume</td><td>1029.30</td><td>3339.05</td><td>16.31</td><td>427.19</td></tr><tr><td>PositiveEmotion</td><td>209.42</td><td>322.74</td><td>2.83</td><td>16.09</td></tr><tr><td>NegativeEmotion</td><td>226.54</td><td>360.33</td><td>2.52</td><td>12.46</td></tr><tr><td>Happiness</td><td>209.42</td><td>322.74</td><td>2.83</td><td>16.09</td></tr><tr><td>Surprise</td><td>3.91</td><td>7.39</td><td>3.55</td><td>21.24</td></tr><tr><td>Fear</td><td>115.18</td><td>196.00</td><td>2.62</td><td>12.60</td></tr><tr><td>Sadness</td><td>26.16</td><td>43.78</td><td>3.33</td><td>20.94</td></tr><tr><td>Anger</td><td>3.73</td><td>6.84</td><td>3.93</td><td>27.12</td></tr><tr><td>Disgust</td><td>77.57</td><td>124.74</td><td>2.82</td><td>14.85</td></tr></table>

A nonzero skewness reveals a lack of symmetry of the empirical distribution, while the kurtosis value quantifies the weight of tails in comparison to the normal distribution for which the kurtosis equals 3. Therefore, these variables are right skewed and have high kurtosis. To reduce the skewness and kurtosis of our data, for our regression we used the natural log of these variables. Because there are zeros in our data set, we adjusted the raw data by adding one before the natural log.

## The VAR Methodology

Understanding the dynamics and feedback effects between microblog volume and emotion intensity can help us better understand the public’s reaction. To look for interdependence, we used a VAR empirical model for analyzing dynamic mutual influences and feedback effects between microblog volume and emotion intensity. VAR is an empirical framework proposed by Sims [59] to address too many restrictions imposed by traditional simultaneous equation models for analyzing time series data. The modeling approach provides a systematic approach for analyzing the comovements of multiple time series, and the analytical results are relatively easy to interpret [60].VAR has recently been employed in a number of IS studies [16, 61]. This methodology is very useful for testing models with multiple time series data, especially in the situation that these variables have dynamic relationships and mutually influence each other.

In our research context, VAR is suitable for analyzing the mutual influences over alternative modeling techniques. First, VAR has the advantages of being able to address biases, including endogeneity, autocorrelations, and causality loops [61]. Emotions in the current period may influence the microblog volume in the next period, which in turn, may cause a change in the emotions after the next period. Second, VAR provides a useful approach for simultaneously identifying the dynamic and intricate mutual influences among the variables, without imposing prior assumptions and unnecessary restrictions [16].

A VAR model can characterize the dynamic relationships among microblog volume, positive emotion intensity, and negative emotion intensity simultaneously. Furthermore, the dynamic influence of variables can be shown through the Granger causality test, impulse response function plots, and general forecast error variance decomposition analysis. Granger causality analysis provides initial support for the mutual influences between variables, but without the direction. Impulse response function plots can further illustrate the dynamic effects between variables by showing the effect size of each coefficient at a different time window. GFEVD can demonstrate that the proportion of variance is explained at a given time window point by other variables [61].

Specifically, a VAR model is an n − equation, n − variable model, in which each dependent variable is endogenous and is a linear function of its own past values, the past values of all other dependent variables, a set of exogenous variables, and an error term [62]. For instance, emotion intensity in the current period may be influenced by the intensity of emotions and microblog volume in the previous period. The general standard reduced-form VAR(p) model can be written as:

$$
\left\{ \begin{array}{c} y _ {i} = \Phi_ {1} y _ {i - 1} + \dots + \Phi_ {p} y _ {i - p} + \varepsilon_ {i} \\ i = 1, 2, \ldots I \end{array} \right.,\tag{7}
$$

where $y _ { i }$ denotes k-dimensional endogenous vector of time series variables. The $\Phi _ { 1 } , \ldots , \Phi _ { p }$ are coefficient matrices, and p is the lagged time periods. $\varepsilon _ { i }$ is a vector of disturbances that have a mean of zero and are serially uncorrelated. Assuming that $\Sigma$ is the covariance matrix of $\varepsilon _ { i }$ and $\Sigma$ is a positive definite matrix, formula (7) can be expanded as follows:

$$
\left\{ \begin{array}{c} {\left[ \begin{array}{c} y _ {1 i} \\ y _ {2 i} \\ \vdots \\ y _ {k i} \end{array} \right] = \Phi_ {1} \left[ \begin{array}{c} y _ {1 i - 1} \\ y _ {2 i - 1} \\ \vdots \\ y _ {k i - 1} \end{array} \right] + \dots + \Phi_ {p} \left[ \begin{array}{c} y _ {1 i - p} \\ y _ {2 i - p} \\ \vdots \\ y _ {k i - p} \end{array} \right] + \left[ \begin{array}{c} \varepsilon_ {1 i} \\ \varepsilon_ {2 i} \\ \vdots \\ \varepsilon_ {k i} \end{array} \right],} \\ i = 1, 2, \ldots , I \end{array} \right.\tag{8}
$$

On the basis of the following forms of VAR model and research variables, our VAR model is specified for analyses:

$$
\left[ \begin{array}{c} M i c r o b l o g V o l u m e _ {t} \\ P o s i t i v e E m o t i o n _ {t} \\ N e g a t i v e E m o t i o n _ {t} \end{array} \right] = \sum_ {p = 1} ^ {P} \left[ \begin{array}{c c c} \varphi_ {1 1} ^ {t - p} & \varphi_ {1 2} ^ {t - p} & \varphi_ {1 3} ^ {t - p} \\ \varphi_ {2 1} ^ {t - p} & \varphi_ {2 2} ^ {t - p} & \varphi_ {2 3} ^ {t - p} \\ \varphi_ {3 1} ^ {t - p} & \varphi_ {3 2} ^ {t - p} & \varphi_ {3 3} ^ {t - p} \end{array} \right] \left[ \begin{array}{c} M i c r o b l o g V o l u m e _ {t - p} \\ P o s i t i v e E m o t i o n _ {t - p} \\ N e g a t i v e E m o t i o n _ {t - p} \end{array} \right] +
$$

$$
\left[ \begin{array}{c} \varepsilon_ {M i c r o b l o g V o l u m e, t} \\ \varepsilon_ {P o s i t i v e E m o t i o n, t} \\ \varepsilon_ {N e g a t i v e E m o t i o n, t} \end{array} \right] (9)
$$

???????????????????????????? $\mathbf { \nabla } \cdot e _ { t } ,$ ??????????????????????????????<sub>??</sub> , and ??????????????????????????????<sub>??</sub> are our endogenous be noted that the predicting variables on the right-hand side of each equation in the VAR have the same lagged values. The VAR model with microblog volume and subcategories of emotions has been omitted because it is similar to formula (9). Figure 4 illustrates the mutual influences process modeled conceptually when $\mathsf { p } { = } 1$ by only including microblog volume and emotion intensity. The last time window is T.

![](/api/attachments/TFWXH6H6/fulltext/images/d3fd5baac140119a6b6e0a70caac3e0b7042d7ee1dd1b3ccb417bf1ce5b1483e.jpg)  
Figure 4. The process of mutual influences analysis (p=1)

## Model Estimation

The process of the VAR model construction and analysis involves two basic processes: (i) unit root test and (ii) lag length selection. To construct the VAR model, the stationarity of time series data is an important requirement necessary before carrying out the Granger causality test [62]. We performed an augmented Dicker-Fuller (ADF) unit root test [16] for all endogenous variables, respectively. Only the time series data that have stationarity can be used to construct a VAR model. For data that do not, we used a difference method for data smoothing and afterward performed the ADF test again. The time series data, which pass the stationarity test are used for the following analysis. Figure 5 illustrates the model estimation process of VAR methodology.

![](/api/attachments/TFWXH6H6/fulltext/images/0e08299eaff49f173ff8189513da407b291294d3dd120b4f3c0338d684c4125b.jpg)  
Figure 5. Process of VAR methodology analysis

The lag length p was chosen based on the three commonly used statistics, which include Akaike information criterion, Hannan-Quinn criterion, and final prediction error, to reflect the forecasted mean squared error. Liitkepohl [62] discusses details of the above statistics. With our dataset, (MicroblogVolume, PositiveEmotion, NegativeEmotion) and (MicroblogVolume, Happiness, Surprise, Fear, Sadness, Anger, Disgust), all three metrics indicated that the optimal lag length is p = 2.

## Empirical Analysis with the VAR Model

In this section, we first analyzed the empirical results of the VAR model and demonstrated the significant interrelationships among microblog volume, the intensity of positive emotions, and the intensity of negative emotions. Next, we introduced the analyses based on subcategories of emotions.

## Empirical Results with the Intensity of Positive and Negative Emotions

The magnitudes of estimated coefficient in a VAR model are not useful for studying the mutual influences between the variables, given the complex dynamic nature of the VAR methodology [62]. Therefore, in the following discussion, we focused on the standard procedures for the VAR analysis, which include the Granger causality test, IRFs analysis, and GFEVD [62]. Before these procedures, the basic VAR model specification processes described in the above section were formed to test the stationarity and construct VAR model. The overall VAR estimated results of variables are shown in the following Table 5. It is noticed that $R ^ { 2 }$ and Adjusted $R ^ { 2 }$ denote the reasonable fit of the VAR model, which are bigger than 0.85.

<table><tr><td></td><td>MicroblogVolume</td><td>PositiveEmotion</td><td>NegativeEmotion</td></tr><tr><td> $R^{2}$ </td><td>0.92</td><td>0.88</td><td>0.88</td></tr><tr><td>Adjusted  $R^{2}$ </td><td>0.92</td><td>0.88</td><td>0.88</td></tr></table>

## Granger Causality Analysis

Granger causality analysis deals with the problem of whether x triggers y, and to which extent Y can be explained by the lagged X. If the answer is yes, or the correlation coefficient between X and Y is significant, it can be said that "Y is Granger caused by X or X can trigger Y." Granger causality analysis can show initial evidence for the relationships between variables, but without a positive or negative direction. Following the work of Tirunillai et al. [63], we performed Granger causality tests and reported the results in Figure 6 with the p − values for all possible pairwise Granger-causes.

For H1 and H2, MicroblogVolume can Granger-cause PositiveEmotion (with a p-value<0.001) and NegativeEmotion (with a p-value<0.001), respectively. All variables are significantly affected by their lagged values, thereby initially supporting H3, H4, and H7. We also observe that PositiveEmotion does not Granger-cause NegativeEmotion, while NegativeEmotion does Granger-cause PositiveEmotion. Thus, H6 is initially supported but not H5. Most of the results mentioned above are consistent with our research model and imply there may be a cyclical relationship between MicroblogVolume and NegativeEmotion of the public’s reaction to EID events. However, there is no such cyclical relationship between MicroblogVolume and PositiveEmotion, but MicroblogVolume drives PositiveEmotion. The p-value of NegativeEmotion to MicroblogVolume is less than 0.01, and that of PositiveEmotion to MicroblogVolume is greater than 0.1.

![](/api/attachments/TFWXH6H6/fulltext/images/171cd3893b5ba09885b5d06c8c40477c84e64c82889ab9d4e611dbdc4badd57a.jpg)  
Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001

Figure 6. Results of Granger Causality Analysis

## Impulse Response Functions

Impulse response functions consider how the influence of error terms transmits to other variables over time in a time series model [62]. IRF analyses can illustrate the dynamic impact of one variable on another within each time window [16], and can serve as additional evidences for our hypotheses to show the dynamic nature of the mutual influences between microblog volume and emotion intensity. IRF plots illustrate the time-varying effects of the mutual influences between microblog volume and emotion intensity, especially how long it takes to reach the peak point and decreases to the non-significance point.

The results of IRFs on the public’s reaction to EID events are reported in Figure 7 and provide nine possible IRFs for the estimated VAR model. Each plot in the figure can be explained by showing the response of a variable over a period given one unit of impulse from time windows one through ten. The x-axis is the time line (i.e., hourly time windows) and the y-axis represents the response of the dependent variable to a unit shock in the impulse variable. Dotted bands are 95% confidence intervals that are bootstrapped based on studentized interval [16, 62]. The results of IRF analysis corroborate most of the results of Granger causality analysis. Specifically, NegativeEmotion does not have an immediate impact on MicroblogVolume at the first time window, there are significantly positive responses of MicroblogVolume from time

##

windows 3 to 10 in NegativeEmotion  MicroblogVolume plot (first row and third column of Figure 7). Such an impact from PositiveEmotion to MicroblogVolume, however, is not found (as evidenced by the confidence intervals including the zero line). The responses of both PositiveEmotion and NegativeEmotion resulted from MicroblogVolume are significantly positive from time windows 1 to 10. The MicroblogVolume  PositiveEmotion and the MicroblogVolume  NegativeEmotion plots attenuate quickly over time. Thus, H1 and H2 are supported. We find significant positive responses in MicroblogVolume  MicroblogVolume at the time windows of 1-10, PositiveEmotion  PositiveEmotion at the time windows of 1-6, and NegativeEmotion  NegativeEmotion at time windows 1-10. Additionally, the impact of NegativeEmotion on PositiveEmotion is significantly positive at time windows 4-10 in NegativeEmotion  PositiveEmotion; therefore, H6 is rejected as the direction is opposite. It is also worth mentioning that all responses converge at zero after 10 time-windows (or 10 hours), and reach a stable state. That is, one variable will not have a significant response to the other variable.

The magnitude of one variable’s response to one unit of other variables is illustrated in Figure 7. For example, the NegativeEmotion  MicroblogVolume plot has a response value of 0.04 at time window 3, demonstrating that a one-unit increase in NegativeEmotion at time window 1 can trigger a 0.04 unit increase of MicroblogVolume in time window 3. The IRF plots illustrate the dynamic impact of one variable on another. In NegativeEmotion  MicroblogVolume, the peak impact is at the $5 ^ { \mathrm { t h } }$ time window.

![](/api/attachments/TFWXH6H6/fulltext/images/f7b4d24f4714e1281b20f079d9ceb0642922cbaefe8f66f30f4bfc3862d70aa8.jpg)  
Figure 7. IRFs results of avian influenza (H7N9) event

## Generalized Forecast Error Variance Decomposition

Generalized forecast error variance decomposition analysis of the VAR model provides us insights into analyzing the contribution of structural impact that explains variances of endogenous variables. GFEVD can demonstrate that the percentage of variance of a variable is explained at a given time window by others [62]. Table 6 shows the GFEVD results for MicroblogVolume, PositiveEmotion, and NegativeEmotion, with each row representing the percentage, in ten time windows, explained by other variables [62]. As expected, the lagged values of a variable explain the most of its own error variance. About 99% error variance of MicroblogVolume is accounted for by its own lagged values, 0.70% by NegativeEmotion and 0.30% by PositiveEmotion. These results suggest that NegativeEmotion is more important than PositiveEmotion to MicroblogVolume. Less than 15% error variance of PositiveEmotion is accounted for by MicroblogVolume and NegativeEmotion. Approximately 16% error variance of NegativeEmotion is accounted for by MicroblogVolume and PositiveEmotion, but the majority by MicroblogVolume. As the time window progresses, the proportion of error variance explained by one’s own lagged value decreases, while that by other variables increases. The percentages shown in Table 6 quantify the dynamic relationships between microblog volume and the intensity of emotions over time.

Table 6. GFEVD results of MicroblogVolume, PositiveEmotion, and NegativeEmotion

<table><tr><td rowspan="2">Period</td><td colspan="3">MicroblogVolume</td><td colspan="3">PositiveEmotion</td><td colspan="3">NegativeEmotion</td></tr><tr><td>Microblog Volume</td><td>Positive Emotion</td><td>Negative Emotion</td><td>Microblog Volume</td><td>Positive Emotion</td><td>Negative Emotion</td><td>Microblog Volume</td><td>Positive Emotion</td><td>Negative Emotion</td></tr><tr><td>1</td><td>100.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>100.00</td><td>0.00</td><td>0.0000</td><td>0.0000</td><td>100.0000</td></tr><tr><td>2</td><td>99.92</td><td>0.07</td><td>0.01</td><td>2.92</td><td>96.01</td><td>1.07</td><td>4.56</td><td>2.56</td><td>92.89</td></tr><tr><td>3</td><td>99.66</td><td>0.14</td><td>0.20</td><td>3.63</td><td>94.21</td><td>2.16</td><td>5.40</td><td>3.41</td><td>91.19</td></tr><tr><td>4</td><td>99.48</td><td>0.20</td><td>0.32</td><td>4.76</td><td>91.96</td><td>3.27</td><td>6.67</td><td>4.34</td><td>88.99</td></tr><tr><td>5</td><td>99.31</td><td>0.24</td><td>0.45</td><td>5.57</td><td>90.21</td><td>4.22</td><td>7.45</td><td>5.03</td><td>87.52</td></tr><tr><td>6</td><td>99.17</td><td>0.27</td><td>0.56</td><td>6.28</td><td>88.70</td><td>5.01</td><td>8.10</td><td>5.57</td><td>86.33</td></tr><tr><td>7</td><td>99.07</td><td>0.30</td><td>0.63</td><td>6.86</td><td>87.49</td><td>5.66</td><td>8.58</td><td>5.99</td><td>85.43</td></tr><tr><td>8</td><td>98.99</td><td>0.32</td><td>0.69</td><td>7.33</td><td>86.48</td><td>6.19</td><td>8.96</td><td>6.33</td><td>84.71</td></tr><tr><td>9</td><td>98.92</td><td>0.34</td><td>0.74</td><td>7.73</td><td>85.65</td><td>6.62</td><td>8.96</td><td>6.60</td><td>84.13</td></tr><tr><td>10</td><td>98.87</td><td>0.35</td><td>0.78</td><td>8.05</td><td>84.97</td><td>6.98</td><td>9.51</td><td>6.83</td><td>83.66</td></tr></table>

## Empirical Results for Introduction of Subcategories of Emotions

We further refined PositiveEmotion and NegativeEmotion into six subcategories of emotions to provide a better understanding of whether there exists a difference among them. First, we verified the results of Granger causality tests between MicroblogVolume and the subcategories of emotions. Then we used both the IRFs and GFEVD to further verify their mutual influences. The IRFs and GFEVD results are omitted here because of space limitations, but we showed the positive or negative direction based on the IRFs results in Table 7 and Table 8.

Table 7. Granger-causes relationship from subcategories of negative emotions to MicroblogVolume

<table><tr><td rowspan="2">Dependent Variable</td><td colspan="5">Independent Variable</td></tr><tr><td>Anger</td><td>Sadness</td><td>Fear</td><td>Disgust</td><td>Surprise</td></tr><tr><td>MicroblogVolume</td><td>n.s</td><td>n.s</td><td>+***</td><td>n.s</td><td>n.s</td></tr></table>

Note. H0: Column variables (or sets) do not Granger-cause row variables (or sets). \*\*\* p<0.001, n.s not significant. + positive influence.

Regarding the subcategories of NegativeEmotion, Table 7 shows that only Fear Granger-causes MicroblogVolume in the context of EID events with a p-value <0.001. As mentioned in the previous section, the subcategory of PositiveEmotion happiness Granger-causes on MicroblogVolume is not significant. So, we do not repeat its results here. The causality effects from MicroblogVolume to subcategories of positive and negative emotions are shown in

Table 8. MicroblogVolume has a significant influence on Happiness (p-value<0.001) and all of the categories of NegativeEmotion, including Anger (p-value<0.001), Sadness (p-value<0.001), Fear (p-value<0.001), Disgust (p-value<0.001), and Surprise (p-value<0.001). Tables 7 and 8 suggest that there is reciprocal influence between MicroblogVolume and Fear. All these results are consistent with H1 and H2.  
Table 8. Granger-causes relationship from MicroblogVolume to subcategories of emotion intensity

<table><tr><td rowspan="2">Independent Variable</td><td colspan="6">Dependent Variable</td></tr><tr><td>Happiness</td><td>Anger</td><td>Sadness</td><td>Fear</td><td>Disgust</td><td>Surprise</td></tr><tr><td>MicroblogVolume</td><td>+***</td><td>+***</td><td>+***</td><td>+***</td><td>+***</td><td>+***</td></tr></table>

Note. H0: Column variables (or sets) do not Granger-cause row variables (or sets). \*\*\* p<0.001.

Fear has the largest percentage among the subcategories of negative emotions as shown in Table 9. The results show that Fear is the only subcategory that triggers tweeting or retweeting and has the feedback effect from MicroblogVolume.

Table 9. Emotions proportions

<table><tr><td colspan="5">NegativeEmotion</td></tr><tr><td>Sadness</td><td>Anger</td><td>Fear</td><td>Disgust</td><td>Surprise</td></tr><tr><td>0.1155</td><td>0.0164</td><td>0.5084</td><td>0.3424</td><td>0.0172</td></tr></table>

Figure 6 shows that the intensity of both positive and negative emotions has autocorrelations. We surprisingly find that only those subcategories with high physiological arousal have a significant autocorrelation and those with low arousal do not (Figure 8). Fear has the strongest significance of autocorrelations among all the subcategories of emotions, whether positive or negative. The result illustrates that fear is the most contagious and self-sustained emotion.

![](/api/attachments/TFWXH6H6/fulltext/images/0103f7b49041fc154ddbd04dd7e3ce395e4a1d62a80feefeb41778c37daa62ee.jpg)  
Note: The bolded words are subcategories of emotion intensity with high physiological arousal. ^ p<0.1, \*\* p<0.01, \*\*\* p<0.001, n.s not significant, + positive influence.  
Figure 8. Granger causality relationship from the intensity of subcategories of emotions to itself

The impact of happiness on the subcategories of negative emotions is not significant (H5 is unsupported). Table 10 provides the positive impact of subcategories of negative emotions on happiness (H6 is unsupported). The subcategories of negative emotions, including surprise, anger and fear, have a positive impact on Happiness. The relationship between fear and happiness is the strongest. To check how the process is going, the results of IRFs of subcategories of negative emotions on subcategories of positive emotions are reported in Figure 9. It shows that all of the impulse response is significant from time window 1 to 10 in Surprise  Happiness, Anger  Happiness, and Fear  Happiness. The results in Table 10 and Figure 9 illustrate that subcategories of Negative Emotions with a high arousal more likely lead to Happiness, with Fear having the strongest impact.

Table 10. Granger-causes relationship of H6 by introducing subcategories of emotions

<table><tr><td rowspan="2">Dependent Variable</td><td colspan="5">Independent Variable</td></tr><tr><td>Anger</td><td>Sadness</td><td>Fear</td><td>Disgust</td><td>Surprise</td></tr><tr><td>Happiness</td><td>+^</td><td>n.s</td><td>+***</td><td>n.s</td><td>+*</td></tr></table>

Note. H0: Column variables (or sets) do not Granger-cause row variables (or sets). ^ p<0.1, \* p<0.05, \*\*\* p<0.001, n.s not significant, + positive influence.

![](/api/attachments/TFWXH6H6/fulltext/images/547e60272468ec83d4dc525684dab9341387d2e57c969e0b30d2d8cd6ae855ef.jpg)

![](/api/attachments/TFWXH6H6/fulltext/images/b7cfc34f92a5dc58730b0ef4b8d82d4e79989f3586526c284d11afae19f0ade0.jpg)

![](/api/attachments/TFWXH6H6/fulltext/images/bdc20c024959c52822f194a45b292ebdd73a3b826a7aec5007f7a49acb537e9b.jpg)  
Figure 9. IRFs results of subcategories of negative emotions on subcategories of positive emotion

## Robustness Checks

In addition to the full-sample analysis described above, we performed multicollinearity tests, and used different time windows and alternative samples of EID events to conduct several additional analyses to ascertain the robustness of the results.

To check the sensitivity of the results due to the length of the time window, we conducted additional analyses with 0.5 hour, 2 hours, and 4 hours as the interval to define a time window. Table 11 shows that the results do not change significantly (Table 11). In addition, a different EID event is used to validate the robustness of the hypotheses model. We chose the Zika virus as the other typical EID event in the third category referenced before and then examined the hypotheses. Zika virus happened in February 2016. The new results of Granger causality analysis and IRFs for all hypotheses are shown in Table 11 and are consistent with those in the results above.

Table 11. Robustness results of Granger causality analysis p-values for the hypotheses model

<table><tr><td rowspan="3">Dependent variable</td><td colspan="12">Independent variable</td></tr><tr><td colspan="4">MicroblogVolume</td><td colspan="4">PositiveEmotion</td><td colspan="4">NegativeEmotion</td></tr><tr><td>0.5hour</td><td>2hour</td><td>4hour</td><td>zika</td><td>0.5hour</td><td>2hours</td><td>4hours</td><td>zika</td><td>0.5hour</td><td>2hours</td><td>4hours</td><td>zika</td></tr><tr><td>MicroblogVolume</td><td>+***</td><td>+**</td><td>+*</td><td>+^</td><td>n.s</td><td>n.s</td><td>n.s</td><td>n.s</td><td>+*</td><td>+*</td><td>+***</td><td>+***</td></tr><tr><td>PositiveEmotion</td><td>+***</td><td>+*</td><td>+***</td><td>+*</td><td>+***</td><td>+***</td><td>+^</td><td>+*</td><td>+^</td><td>+^</td><td>+***</td><td>+**</td></tr><tr><td>NegativeEmotion</td><td>+***</td><td>+***</td><td>+**</td><td>+***</td><td>n.s</td><td>n.s</td><td>n.s</td><td>n.s</td><td>+***</td><td>+***</td><td>+^</td><td>+*</td></tr></table>

Note. H0: Column variables (or sets) do not Granger-cause row variables (or sets). ^ p<0.1, \* p<0.05, \*\* p<0.01, \*\*\* p<0.001, n.s not significant, + positive influence.

Lastly, we would like to note the necessity of considering if there is multicollinearity among each of the variables that may bias the estimation. The condition index of multicollinearity is computed to assess whether a model has multicollinearity. According to Kennedy’s [64] definition on the threshold value, a condition index greater than 10, and less than 30, indicates a slight multicollinearity, while greater than 30 is indicative of significant multicollinearity. Tolerance less than 0.1 and a variance inflation factor (VIF) greater than 5 indicate the existence of multicollinearity. Table 12 shows all condition indexes less than 10, all tolerance greater than 0.1, and all VIF less than 5. Thus, these results suggest that multicollinearity is not a concern in our analyses.

Table 12. Multicollinearity test indexes for an EID even

<table><tr><td>Index</td><td>Microblog Volume</td><td>Positive Emotion</td><td>Negative Emotion</td><td>Happiness</td><td>Anger</td><td>Sadness</td><td>Fear</td><td>Disgust</td><td>Surprise</td></tr><tr><td>Condition Index</td><td>7.85</td><td>7.21</td><td>7.26</td><td>1.00</td><td>2.88</td><td>2.59</td><td>6.38</td><td>7.30</td><td>3.21</td></tr><tr><td>Tolerance</td><td>0.33</td><td>0.37</td><td>0.34</td><td>0.37</td><td>0.37</td><td>0.33</td><td>0.11</td><td>0.33</td><td>0.31</td></tr><tr><td>VIF</td><td>3.05</td><td>2.68</td><td>2.93</td><td>2.69</td><td>2.67</td><td>3.06</td><td>8.99</td><td>2.99</td><td>3.21</td></tr></table>

## Discussion

With time series data, this study analyzes the mutual influences between microblog volume and the intensity of emotions (both negative and positive) that are dynamic in nature and vary over time in the context of the public’s reaction to EID events. There are several key findings. First, microblog volume impacts the intensity of negative emotions (H2), and the intensity of negative emotions has a feedback effect on microblog volume. Combing with IRFs results in Figure 7, we see that negative emotions have lagged and stable impact on microblog volume, while microblog volume has an instantaneous but fast decreased impact on negative emotions. Moreover, fear plays the most significant role among the subcategories of emotions. Fear has been used to explain and predict how people respond facing existential threats [65]. In the context of EID events, microblog volume and fear intensity mutually influence each other. Fear motivates individuals to tweet or retweet relevant microblogs, and the more microblogs on the EID event may also stir up fears.

While microblog volume impacts the intensity of positive emotions (H1), the intensity of positive emotions does not have a significant impact on message volume in the empirical results. As an EID event is a negative public crisis by nature, the public may be more easily influenced by negative emotions [66] embodied in microblogs. In addition, the impact of microblog volume on positive and negative emotions is at the similar level of significance. But the IRFs results in Figure 7 indicate the response of PositiveEmotion decreases faster than that of NegativeEmotion with a unit increase of MicroblogVolume impulse. Further, the intensity of negative emotions has a more significant impact on microblog volume than the intensity of positive emotions, which is consistent with previous empirical findings [13].

Second, the Granger causality analyses of H3, H4, and H7 illustrate a significant autocorrelation of variables (include microblog volume, the intensity of positive and negative emotions, as well as that of their subcategories) in Figure 6 and Figure 8. Subcategories that have high arousal, especially fear, have a more significant autocorrelation than those with low physiological arousal. The results confirm and extend emotional contagion in the EID events context. Here, we should also note that microblog volume has an autocorrelation. As microblog volume on an event increases, the event could draw more attention and discussion.

Third, the results of H5 and H6 are contrary to our expectations. Positive and negative emotions do not have a mutual suppression relationship. Instead, the intensity of negative emotions has a significantly positive impact on the intensity of positive emotions. Such an impact could be due to the automatic repair process as depicted in the mood repair hypothesis [67]. The unpleasant emotion experience may motivate the public to act in ways to feel better. The IRF plots in Figure 7 show that the intensity of negative emotions has a significant impact on the intensity of positive emotions at time window 4. Therefore, the lagged effects of mood repair may begin from time window 4, and the response increases gradually after time window 4. Furthermore, the subcategories of negative emotions with high arousal are more likely to lead to positive emotions.

In summary, through the VAR model, the results show the significant mutual influences among microblog volume and the intensity of positive and negative emotions of the public’s reaction to EID events. Table 13 summarizes the results of hypotheses testing, and Table 14 presents the new discovery.

Table 13. Test results for hypotheses

<table><tr><td>Hypothesis</td><td>Description</td><td>Emotions</td><td>Subcategories of emotions</td></tr><tr><td>H1</td><td>Microblog volume related to the EID event has a positive impact on the intensity of positive emotions articulated in microblogs regarding an EID event.</td><td>Support</td><td>Support</td></tr><tr><td>H2</td><td>Microblog volume related to the EID event has a positive impact on the intensity of negative emotions articulated in microblogs regarding an EID event.</td><td>Support</td><td>Support</td></tr><tr><td>H3</td><td>The intensity of positive emotions articulated in microblogs regarding an EID event is autocorrelated.</td><td>Support</td><td>Support</td></tr><tr><td>H4</td><td>The intensity of negative emotions articulated in microblogs regarding an EID event is autocorrelated.</td><td>Support</td><td>Support</td></tr><tr><td>H5</td><td>The intensity of positive emotions has a negative impact on the intensity of negative emotions articulated in microblogs regarding an EID event.</td><td>Not support</td><td>Not support</td></tr><tr><td>H6</td><td>The intensity of negative emotions has a negative impact on the intensity of positive emotions articulated in microblogs regarding an EID event.</td><td>Not Support</td><td>Not Support</td></tr><tr><td>H7</td><td>Microblog volume related to the EID event is autocorrelated.</td><td>Support</td><td>Support</td></tr></table>

Table 14. New findings

<table><tr><td>Findings</td><td>Description</td></tr><tr><td>F1</td><td>The relationship between microblog volume and the intensity of negative emotions is different from that between microblog volume and the intensity of positive emotions related to the EID event.</td></tr><tr><td>F2</td><td>Microblog volume related to the EID event has cyclical relationship with the intensity of fear articulated in microblogs regarding an EID event.</td></tr><tr><td>F3</td><td>The intensity of high arousal emotions articulated in microblogs is more likely to be autocorrelated than the intensity of low arousal emotions articulated in microblogs regarding an EID event.</td></tr><tr><td>F4</td><td>The intensity of negative emotions with high arousal has a more significant impact on the intensity of positive emotions than the intensity of negative emotions with low arousal articulated in microblogs regarding an EID event.</td></tr></table>

## Theoretical Implications

The theoretical implications of the study are threefold. First, it contributes to IS research by examining the mutual influences between microblog volume and emotion intensity. Prior studies mostly consider the relationship between microblog volume and emotion intensity to be one-way and time invariant [13, 30]. Our study quantifies their dynamic and interdependent relationship in the context of EID events. The public’s emotion intensity may be endogenous and originated from previously generated content, which, in turn, alters subsequent content generation. We find that microblog volume has an immediate but fast decay influence on negative emotion intensity, while negative emotion intensity has a delayed but stable and persistent influence on microblog volume. It is important for the researchers to recognize the nature of being interdependent and dynamic in future investigations, because the consideration may help avoid biases in the conclusion and prepare for the possibly varying strength of the relationship with different lead time windows.

In addition, based on the findings regarding the mutual influences, we provide a new perspective in analyzing the public’s reaction by incorporating the time-varying and circular relationships. Future research may be informed of the potential feedback loop that exists between microblog volume and emotion intensity when developing predictive models. It would help avoid the potential pitfall of “forecasting the past”. Further, there are differential mutual influences between different subcategories of emotions and message volume. What subcategories of emotions are used to explain the related behavior could affect the strength of the relationship.

Second, this study empirically validates the autocorrelation among emotions in the context of EID events and presents a phenomenon of inertia in the public’s response to EID events. The results show that subcategories of emotions with high arousal could be more contagious and easily repaired. In the literature on social media, less attention has been given to arousal compared with valence as an important dimension for content virality [68]. Our study suggests that it could be important to take into account both valence and arousal of subcategories of emotion in explaining related outcomes.

Moreover, our study contributes to the literature in human emotion. Our study shows differential effects of the subcategories of emotions in their emotional contagion and mood repair. Prior studies [67, 69] mostly suggest mood repair for negative emotions and maintenance (or inertia) for positive emotions. Our results show that there is inertia for both subcategories of positive and negative emotions, but dynamic mood repair for subcategories of negative emotion in the public’s reaction. The research context of EIDs may matter for such findings, as EID events could more likely evoke uncertainty and fear among the public [70]. Therefore, it may be important to take account of both the context and subcategories of emotions in investigating the dynamic process of mood management.

Third, by exploring the subcategories of emotions, this study shows fear to be the most salient that has a circular and dynamic relationship with microblog volume. The role of fear in facilitating behavioral changes has been long recognized in health communication literatures [22,

71]. Future research could pay special attention to the role of fear and its evolvement in the context of EID events or other public crises. How the level of fear is abated in such a spiral process with content generation behavior could be further investigated. Fear embodied in user-generated content may be used as the key factor in risk analysis or for the construction of forecasting models. The existence of a spiral process between fear and message volume could also be examined in other contexts.

## Practical Implications

Our study also provides several practical implications. First, due to the complexity of disease management, novel methodologies and frameworks for disease surveillance are needed [72]. This study provides an approach and analysis framework for public health management to identify the public’s reaction to EID events as early signals. Social media would potentially indicate the trends of disease outbreak quicker and more reliably compared to traditional methods of public health reporting [73]. Our approach could help monitor an EID outbreak, allowing related entities to timely intervene the situation necessarily. The analysis approach proposed in this study can be used to predict microblog volume that is associated with the development of the public’s reaction, and subsequently help relevant parties’ decision making. The quality of information disseminated over social media may vary. As suggested in our study, the public may be misinformed by the spread of low quality information, and relevant stakeholders can take proper actions for public intervention.

On the basis of the results of IRFs, there is a time window that a variable has the highest impact on another variable. Relevant stakeholders may take proper action to mitigate this kind of impact before that time window. As shown in our results, negative emotions have the most significant impact on microblog volume at time window 5. Relevant stakeholders can take proper actions such as identifying affected subjects, investigating outbreaks, implementing proper measures to calm the public [74], and timely communication to avoid the further diffusion of negative emotions. Meanwhile, relevant stakeholders may focus on pursuing the richness of information to satisfy the public’s information demand. They shall also recognize the limited ability of people to process the information. Both the quality and quantity of information on social media affect the public’s emotions. Therefore, it is important to disseminate high-quality microblogs based on the accurate development of the EID events and refute any rumors in time.

Second, we find that high arousal emotions are more contagious, with fear playing a key role. Therefore, it is important for disease control agencies to monitor emotions with high arousal, especially fear, on social media. As the formation of fear may be largely because of the feeling of uncertainty and lack of relevant knowledge [75], it is necessary for the CDC to announce in a timely manner the cause of the EID event and any related educational programs. Such programs may decrease the fear by increasing relevant knowledge, promoting self-protection behavior, building trust, and preventing the dissemination of misinformation [76]. Reinecke et al. [67] show that the mood management process [77] depends on two basic key mechanisms: distraction from negative emotions and addressing the cause. Therefore, public interventions with family-based education [78] should be encouraged. Mental health surveillance interventions could be planned [79]. The experiences from the West Nile virus epidemic demonstrate that public activities, such as education and communication [80], can reduce the public fear and panic.

## Limitations and Future Studies

There are several limitations of our study, which may be overcome in the future. First, our analyses are restricted to two EID events of category 3. How other categories of public health crises may be different can also be explored. In addition, the generalizability of our findings could be further investigated in other crisis contexts for example, natural disasters, terrorist attacks, school attacks, social unrest, and ransomware attacks.

Second, it is possible that the microblogs, without the keywords we used to search, are relevant to the EID event. Using those keywords may not exhaustively include all possible microblogs. Further, some microblogs included may not be relevant to the EID event. Thus, we performed additional sensitivity analyses by only using those microblogs with the keyword H7N9 and avian influenza. We have not found significant changes in the results.

Third, from 2013 to 2018, there are some changes on Weibo. One aspect is Weibo interfaces and functionalities. The overall style of Weibo became more concise with more functionalities, such as fan service and comment review. We should note that there is no major change in terms of how users can compose their microblogs or the restrictions related to microblog contents from 2013 to 2018 [81]. Moreover, the number of Weibo users has grown tremendously in the past five years from 196 million active users a month (according to company’s Q1 earning report in 2013 [82]) to 411 million active users a month (according to the company’s Q1 earning report in 2018 [83]. Though our hypotheses and research model are not contingent on the ease of use of Weibo, and user attributes, future studies may use more recent events to validate our research.

Finally, VAR is a data-driven method, which can characterize time-varying and feedback relationships among the variables in a closed loop system. We may integrate different parts of the systems where the relationships among the variables may be estimated by VAR, but rely on system dynamics modeling to provide a holistic view on system behavior [84]. In other words, the relationships estimated by VAR can provide some empirical guidance and localized view for system dynamics modeling in creating the models for a complex system. Future research may incorporate VAR methodology with system dynamics modeling to investigate dynamic patterns through “what if” analyses and simulations for more complex and open loop systems [85].

Our research is an endeavor toward understanding mutual interdependence between microblog volume and emotions in the context of EID events. It may provide an impetus for future studies on reciprocal influences between microblog volume and emotions in different contexts, and can be a foundation to support decision-making in disease management.

## Acknowledgments

The work described in this paper has been supported by the National Nature Science Foundation of China (No.71573030) & (No.71533001), and the Social Science Planning Fund Key Program, Liaoning Province (No. L15AGL017).

## References

[1] C. E. Winslow, The untilled fields of public health, Science (1920) 23-33.

[2] A. S. Fauci, Emerging and reemerging infectious diseases: the perpetual challenge, Acad. Med. 80 (12) (2005) 1079-1085.

[3] K. E. Jones, N. G. Patel, M. A. Levy, A. Storeygard, D .Balk, J. L. Gittleman, P. Daszak, Global trends i n emerging infectious diseases, Nature 451 (7181) (2008) 990-993.

[4] M. Odlum, S. Yoon, What can we learn about the Ebola outbreak from tweets?, Am. J. Infect. Control. 43 (6) (2015) 563-571.

[5] N. Kanhabua, S. Romano, A. Stewart, W. Nejdl, Supporting temporal analytics for health-related events in microblogs, In Proceedings of the 21st ACM international conference on Information and knowledge management (2012).

[6] D. Gundogdu, O. D. Incel, A. A. Salah, B. Lepri, Countrywide arrhythmia: emergency event detection using mobile phone data, EPJ Data Sci. 5 (1) (2016) 25.

[7] G. J. Milinovich, G. M. Williams, A. C. Clements, W. Hu, Internet-based surveillance systems for monitoring emerging infectious diseases, Lancet Infect. Dis. 14 (2) (2014) 160-168.

[8] A. Seifter, A. Schwarzwalder, K. Geis, J. Aucott, The utility of “Google Trends” for epidemiological research: Lyme disease as an example. Geospatial Health. (2010) 135-137.

[9] M. Santillana, D. W. Zhang, B. M. Althouse, J. W. Ayers, What can digital disease detection learn from (an external revision to) Google Flu Trends? Am. J. Prev. Med. 47 (3) (2014) 341-347

[10] M. Salathé, S. Khandelwal, Assessing vaccination sentiments with online social media: implications for infectious disease dynamics and control, PLoS Comput. Biol. 10 (7) (2011) e1002199.

[11] L. Mollema, I. A. Harmsen, E. Broekhuizen, R. Clijnk, H. De Melker, T. Paulussen, E. Das, Disease detection or public opinion reflection? Content analysis of tweets, other social media, and online newspapers during the measles outbreak in The Netherlands in 2013. J. Med. Internet Res. 17(5) (2015) e128.

[12] J. Berger, K.L. Milkman, What makes online content viral?, J. Mark. Res. 49 (2) (2012) 192-205.

[13] S. Stieglitz, L. Dang-Xuan, Emotions and information diffusion in social media—sentiment of microblogs and sharing behavior, J. Manage. Inform. Syst. 29 (4) (2013) 217-248.

[14] I. C. H. Fung, K. Wong, Efficient use of social media during the avian influenza A (H7N9) emergency response, Western Pacific surveillance and response journal: WPSAR. 4 (4) (2013) 1.

[15] J. Liu, Z. Cao, D. Zeng, Predicting popularity of microblogs in emerging disease event. In International Conference on Web-Age Information Management. (2014).

[16] G. Adomavicius, J. Bockstedt, A. Gupta, Modeling supply-side dynamics of IT components, products, and infrastructure: An empirical analysis using vector autoregression, Inf. Syst. Res. 23 (2) (2012) 397-417.

[17] S. S. Ho, D. Brossard, D. A. Scheufele, The Polls—Trends: Public Reactions to Global Health Threats and Infectious Diseases, Public Opin. Q. 71 (4) (2007) 671-692.

[18] J. Ginsberg, M. H. Mohebbi, R. S. Patel, L. Brammer, M. S. Smolinski, L. Brilliant, Detecting influenza epidemics using search engine query data, Nature 457 (7232) (2009) 1012-1014.

[19] A. Signorini, A. M. Segre, P. M. Polgreen, The use of Twitter to track levels of disease activity and public concern in the US during the influenza A H1N1 pandemic. PloS one, 6(5) (2011), e19467.

[20] M. Krieck, J. Dreesman, L. Otrusina, K. Denecke, A new age of public health: Identifying disease outbreaks by analyzing tweets. In Proceedings of health web-science workshop, ACM Web Science Conference (2011).

[21] H. Gu, B. Chen, H. Zhu, T. Jiang, X. Wang, L. Chen, J. Jiang, Importance of Internet surveillance in public health emergency control and prevention: evidence from a digital epidemiologic study during avian influenza A H7N9 outbreaks, J. Med. Internet Res. 16 (1) (2014) e20.

[22] V. K. Jain, S. Kumar, An Effective Approach to Track Levels of Influenza-A (H1n1) Pandemic in India Using Twitter, Procedia Computer Science. 70 (2015) 801-807.

[23] W. Yoo, D. H. Choi, K. Park, The effects of SNS communication: How expressing and receiving information predict MERS-preventive behavioral intentions in South Korea, Comput. Hum. Behav. 62 (2016) 34-43.

[24] S. F. McGough, J. S. Brownstein, J. B. Hawkins, M. Santillana, Forecasting Zika incidence in the 2016 Latin America outbreak combining traditional disease surveillance with search, social media, and news report data, Plos Neglect. Trop. Dis. 11 (1) (2017) e0005295.

[25] E. Joyce, R. E. Kraut, Predicting continued participation in newsgroups, J. Comput.-Mediat. Commun. 11 (3) (2006) 723-747.

[26] K. Peters, Y. Kashima, A. Clark, Talking about others: Emotionality and the dissemination of social information, Eur. J. Soc. Psychol. 39 (2) (2009) 207-222.

[27] B. Rimé, Emotion elicits the social sharing of emotion: Theory and empirical review, Emot. Rev. 1 (1) (2009) 60-85.

[28] D. Huffaker, Dimensions of leadership and social influence in online communities, Hum. Commun. Res. 36 (4) (2010) 593-617.

[29] L. Dang-Xuan, S. Stieglitz, Impact and Diffusion of Sentiment in Political Communication-An Empirical Analysis of Political Weblogs, ICWSM (2012).

[30] E. Ferrara, Z. Yang, Quantifying the effect of sentiment on information diffusion in social media, PeerJ Computer Science 1 (2015) e26.

[31] J. T. Hancock, K. Gee, K. Ciaccio, M. H. Lin, I'm sad you're sad: emotional contagion in CMC, ACM Conference on Computer Supported Cooperative Work (2008).

[32] A. D. Kramer. The spread of emotion via Facebook. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (2012).

[33] A. D. Kramer, J. E. Guillory, J. T. Hancock, Experimental evidence of massive-scale emotional contagion through social networks. Proceedings of the National Academy of Sciences (2014).

[34] L. Coviello, Y. Sohn, A.D. Kramer, C. Marlow, M. Franceschetti, N. A. Christakis, J. H. Fowler, Detecting emotional cont agion in massive social networks, PLoS One 9 (3) (2014) e90315.

[35] C. A. Smith, P. C. Ellsworth, Patterns of cognitive appraisal in emotion, J. Pers. Soc. Psychol. 48(4) (1985) 813.

[36] C.A. Cottrell, S. L. Neuberg, Different emotional reactions to different groups: a sociofunctional threat-based approach to “prejudice”, J. Pers. Soc. Psychol. 88 (5) (2005) 770.

[37] P. Ekman, An argument for basic emotions, Cogn. Emot. 6 (3-4) (1992) 169-200

[38] M. A. Cohn, B. L. Fredrickson, S. L. Brown, J. A. Mikels, A. M. Conway, Happiness unpacked: positive emotions increase life satisfaction by building resilience, Emotion. 9(3) (2009) 361.

[39] E. C. Winton, D. M. Clark, R. J. Edelmann, Social anxiety, fear of negative evaluation and the detection of negative emotion in others, Behav. Res. Ther. 33(2) (1995) 193-196

[40] L. Z. Tiedens, Anger and advancement versus sadness and subjugation: the effect of negative emotion expressions on social status conferral, J. Pers. Soc. Psychol. 80(1) (2001) 86.

[41] S. R. Vrana, The psychophysiology of disgust: Differentiating negative emotional contexts with facial EMG, Psychophysiology 30(3) (1993) 279-286

[42] B. L. Fredrickson, M. M. Tugade, C. E. Waugh, G. R. Larkin, What good are positive emotions in crisis? A prospective study of resilience and emotions following the terrorist attacks on the United States on September 11th, 2001, J. Pers. Soc. Psychol. 84(2) (2003) 36 5.

[43] R. F. Baumeister, K. D. Vohs, C. Nathan DeWall, L. Zhang, How emotion shapes behavior: Feedback, anticipation, and reflection, rather than direct causation, Pers. Soc. Psychol. Rev. 11(2) (2007) 167-203.

[44] G. A. Miller, The magical number seven, plus or minus two: Some limits on our capacity for processing information, Psychol. Rev. 101 (2) (1994) 343.

[45] M. Sicilia, S. Ruiz, The effect of web-based information availability on consumers' processing and attitudes, J. Interact. Mark. 24 (1) (2010) 31 -41.

[46] H. Sun, A longitudinal study of herd behavior in the adoption and continued use of technology. MIS Q. 37(4) (2013).

[47] M. Sharma, K. Yadav, N. Yadav, K. C. Ferdinand, Zika virus pandemic—analysis of Facebook as a social media health information platform, Am. J. Infect. Control. 45(3) (2017) 301-302.

[48] I. L. B. Liu, C. M. K. Cheung, M. K. O. Lee, Understanding Twitter Usage: What Drive People Continue to Tweet. 2010 Pacis (2010).

[49] S. Li, B. Lin, Accessing information sharing and information quality in supply chain management, Decis. Support Syst. 42 (3) (2006) 1641-1656.

[50] B. Osatuyi, Information sharing on social media sites, Comput. Hum. Behav. 29 (6) (2013) 2622-2631.

[51] J.T. Cacioppo, R.E. Petty, Stalking rudimentary processes of social influence: A psychophysiological approach, Social Influence: The Ontario Symposium: Ontario Symposium on Personality and Social Psychology, 1987.

[52] J. J. Gross, R.W. Levenson, Emotional suppression: physiology, self-report, and expressive behavior, J. Pers. Soc. Psychol. 64 (6) (1993) 970.

[53] M. Lipsitch, S. Riley, S. Cauchemez, A. C. Ghani, N. M. Ferguson, Managing and reducing uncertainty in an emerging influenza pandemic, N. Engl. J. Med. 361(2) (2009) 112-115.

[54] T. L. Sellnow, M. W. Seeger, R. R. Ulmer, Chaos theory, informational needs, and natural disasters, J. Appl. Commun. Res. 30(4) (2002) 269-292.

[55] L. Xu, H. Lin, Y. Pan, H. Ren, J. Chen, Constructing the affective lexicon ontology, Journal of the China Society for Scientific and Technical Information. 27 (2) (2008) 180-185.

[56] V. R. Racaniello, Emerging infectious diseases, J. Clin. Invest. 113 (6) (2004) 796 -798.

[57] T. M. Uyeki, N. J. Cox, Global concerns regarding novel influenza A (H7N9) virus infections, N. Engl. J. Med. 368 (20) (2013) 1862-1864.

[58] H. P. Zhang, K. Gao, H.Y. Huang, Y. Zhao, Big data search and mining. Science Press, 2014.

[59] C. A. Sims, Interpreting the macroeconomic time series facts: The effects of monetary policy, Eur. Econ. Rev. 36(5) (1992) 975-1000

[60] W. Enders, Applied econometric time series. John Wiley & Sons, 2008.

[61] P. Song, L. Xue, A. Rai, C. Zhang, The ecosystem of software platform: A study of asymmetric cross-side network effects and platform governance, MIS Q. 42 (1) (2018) 121-142.

[62] H. Liitkepohl, Introduction to Multiple Time Series Analysis, Technometrics 35 (1) (1991) 88-89.

[63] S. Tirunillai, G. J. Tellis, Does chatter really matter? Dynamics of user-generated content and stock performance, Mark. Sci. 31 (2) (2012) 198-215.

[64] P. Kennedy, A guide to econometrics. MIT press. (2003).

[65] J. Greenberg, J. Arndt, Terror management theory, Handbook of theories of social psychology. 1 (2011) 398-415.

[66] T. A. Ito, J. T. Larsen, N. K. Smith, J. T. Cacioppo, Negative information weighs more heavily on the brain: the negativity bias in evaluative categorizations, J. Pers. Soc. Psychol. 75(4) (1998), 887.

[67] L. Reinecke, R.Tamborini, M. Grizzard, R. Lewis, A. Eden, N. David Bowman, Characterizing mood management as need satisfaction: The effects of intrinsic needs on selective exposure and mood repair, J. Commun. 62 (3) (2012) 437-453.

[68] R. Gaspar, C. Pedro, P. Panagiotopoulos, B. Seibt, Beyond positive or negative: Qualitative sentiment analysis of social media reactions to unexpected stressful events. Comput. Hum. Behav. 56 (2016) 179-191.

[69] K. Passyn, & M. Sujan, Skill-based versus effort-based task difficulty: A task-analysis approach to the role of specific emotions in motivating difficult actions, J. Consum. Psychol. 22(3) (2012) 461-468

[70] B. Person, F. Sy, K. Holton, B. Govert, A. Liang, Fear and stigma: the epidemic within the SARS outbreak, Emerg. Infect. Dis. 10 (2) (2004) 358

[71] A. M. M. De Vries, M. M. Gholamrezaee, I. M. Verdonck‐ de Leeuw, Y. de Roten, J. N. Despland, F. Stiefel, & J. Passchier, Physicians' emotio regulation during communication with advanced cancer patients, Psycho-Oncol. 27(3) (2018) 929-936.

[72] I. C. H. Fung, Z. T. H. Tse, K. W. Fu, The use of social media in public health surveillance, Western Pacific surveillance and response journal: WPSAR. 6 (2) (2015) 3.

[73] H. Oinas-Kukkonen, K.Lyytinen, Y. Yoo, Social networks and information systems: ongoing and future research streams, J. Assoc. Inf. Syst. 11 (2) (2010) 61-68.

[74] L. D. Rotz, J. M. Hughes, Advances in detecting and responding to threats from bioterrorism and emerging infectious disease, Nat. Med. 10(12s) (2004), S130.

[75] R. D. Lebel, Moving beyond fight and flight: A contingent model of how the emotional regulation of anger and fear sparks proactivity, Acad. Manage. Rev. 42 (2) (2017) 190-206.

[76] G. J. Y. Peters, R. A. Ruiter, G. Kok, Threatening communication: a critical re-analysis and a revised meta-analytic test of fear appeal theory, Health Psychol. Rev. 7 (sup1) (2013) S8-S31.

[77] J. D. Hess, J. J. Kacen, J. Kim, Mood-management dynamics: The interrelationship between moods and behaviours, Br. J. Math. Stat. Psychol. 59 (2) (2006) 347-378

[78] C.C. Engel, W.J. Katon, Population and need-based prevention of unexplained physical symptoms in the community, Strategies to protect the health o deployed US forces: medical surveillance record keeping and risk reduction, 1999

[79] V. T. Covello, R. G. Peters, J. G. Wojtecki, R. C. Hyde, Risk communication, the West Nile virus epidemic, and bioterrorism: responding to the commnication challenges posed by the intentional or unintentional release of a pathogen in an urban setting, J. Urban Health 78 (2) (2001) 382-391

[80] J. P. Koplan, Communication during public health emergencies, J. Health Commun. 8 (S1) (2003) 144-145.

[81] K. Y. Ng, A. Feldman, C. Leberknight, Detecting Censorable Content on Sina Weibo: A Pilot Study. In Proceedings of the 10th Hellenic Conference on Artificial Intelligence. ACM. (2018) 41.

[82] Y. Rong, J. Song, Mining a government affairs microblog network on Sina Weibo with social network analysis. In Fuzzy Systems and Knowledge Discovery (FSKD), 2013 10th International Conference on IEEE. (2013) 515-519.

[83] http://www.sohu.com/a/231933536\_422018. Microblog 2018 Q1 report.

[84] J. D. Sterman, System Dynamics Modeling: Tools for learning in a complex world, Calif. Manage. Rev. 43(4) (2001) 8-25.

[85] Y. Fang, K. H. Lim, Y. Qian, B. Feng, System dynamics modeling for information systems research: Theory development and practical application. MIS Q. 42 (4) (2018) 1303-1329.

## Brief biographical statements

Jiangnan Qiu is a Professor at School of Economics and Management, Dalian University of Technology, China. He received his B.S., M.S., and Ph.D. degrees in Engineering Mechanics, Computer Software and Theory, and Management Science and Engineering from Dalian University of Technology. His work has been published in Decision Support Systems, Journal of Knowledge Management, and Behaviour & Information Technology, among others. His research interests are emergency management and big data analysis.

Liwei Xu is a Ph.D. candidate at School of Economics and Management, Dalian University of Technology, China. She received her B.S. and M.S. degrees in Information Management and Information System, and Computer Software and Theory from Northeast Forestry University. Her paper has received best paper awards at China Association for Information Systems Conference. Her current research interests include machine learning, emergency management, sentiment analysis, and big data analysis.

Jingguo Wang is a Professor of Information Systems. He graduated from SUNY-Buffalo. His work has been published in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of the Association for Information Systems, Decision

Support Systems, among others. His papers have received best paper awards at AMCIS and the International Conference on Internet Monitoring and Protection. His research has been supported by National Science Foundation and the University of Texas at Arlington.

Wenjing Gu is a Ph.D. candidate at School of Economics and Management, Dalian University of Technology, China. She received her B.S. degree in Information Management and Information System from Liaocheng University, and received her M.S. degree in Management Science and Engineering from Dalian University of Technology. Her research interests include emergency management and big data analysis.
