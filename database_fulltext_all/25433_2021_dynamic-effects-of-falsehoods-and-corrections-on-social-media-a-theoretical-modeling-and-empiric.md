---
otero_id: 25433
otero_key: "QT7RV2GJ"
title: "Dynamic Effects of Falsehoods and Corrections on Social Media: A Theoretical Modeling and Empirical Evidence"
authors: "Kelvin K. King; Bin Wang; Diego Escobari; Tamer Oraby"
year: "2021"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2021.1990611"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dynamic Effects of Falsehoods and Corrections on Social Media: A Theoretical Modeling and Empirical Evidence

Kelvin K. King, Bin Wang, Diego Escobari & Tamer Oraby

To cite this article: Kelvin K. King, Bin Wang, Diego Escobari & Tamer Oraby (2021) Dynamic Effects of Falsehoods and Corrections on Social Media: A Theoretical Modeling and Empirical Evidence, Journal of Management Information Systems, 38:4, 989-1010, DOI: 10.1080/07421222.2021.1990611

To link to this article: https://doi.org/10.1080/07421222.2021.1990611

![](/api/attachments/QT7RV2GJ/fulltext/images/a21ddc270eb94f6db4a6e117db2ce9498e09c87fb86524aa8c22dfb371f7a7ae.jpg)

View supplementary material

![](/api/attachments/QT7RV2GJ/fulltext/images/cbf0724319073df80c1cdfb64b5f9f3501bf952a623969e304f7de583002bd2c.jpg)

Submit your article to this journal

![](/api/attachments/QT7RV2GJ/fulltext/images/7d9d4f404631feba04a96cd2160186b16a1429d449fa0919bfc7798d968ce3ed.jpg)

View related articles

![](/api/attachments/QT7RV2GJ/fulltext/images/37aa2185059b3b8bebcf3ee3bc8fbbd3e85c27ad750fde7af93df4bb54549b3f.jpg)

Published online: 02 Jan 2022.

![](/api/attachments/QT7RV2GJ/fulltext/images/c635015124ac9d58dbfcce312f73252666b8dd610783fdfc93adab0a4edac26a.jpg)

Article views: 675

![](/api/attachments/QT7RV2GJ/fulltext/images/f4eb5fbde47cfbbd78a6c264be63388ddf5d1837185d614e26e81531e3c5bba5.jpg)

View Crossmark data CrossMark

![](/api/attachments/QT7RV2GJ/fulltext/images/555e0567c47dc73ca3555def632f35b459161d99e1a53f58db363137cfda21ab.jpg)

Citing articles: 1 View citing articles

Check for updates

# Dynamic Efects of Falsehoods and Corrections on Social Media: A Theoretical Modeling and Empirical Evidence

Kelvin K. King <sup>a</sup>, Bin Wang <sup>b</sup>, Diego Escobari <sup>b</sup>, and Tamer Oraby <sup>b</sup>

<sup>a</sup>School of Information Studies, Syracuse University, 343 Hinds Hall, Syracuse, NY 13244; <sup>b</sup>University of Texas Rio Grande Valley, 1201 W University Dr, Edinburg, TX 78539

## ABSTRACT

Government agencies and fact-checking websites have been combating the spread of falsehoods on social media by issuing correction messages. There has been, however, no research on the efectiveness of correction messages on falsehoods and their dynamic interaction. We develop a theoretical model of the competition between falsehoods and correction messages on Twitter and show diferent interventions under which falsehoods could be hampered. Moreover, we use panel vector autoregressive models and machine learning techniques to empirically investigate the dynamic interactions between falsehoods and correction messages through a unique longitudinal dataset of 279,597 tweets. We find that correction messages cause an increase in the propagation of falsehoods on social media if their use is not optimized. This study highlights the importance of having government agencies, fact-checking websites, and social media platforms work together to optimize efective correction messages. We argue such an efort will counter the spread of falsehoods.

## KEY WORDS

## AND PHRASES

fake news; online falsehoods; online rumor; online misinformation; social media; combating fake news; panel vector autoregression; fact-checking online; online corrections

## Introduction

A vast majority of Americans are easily deceived by false news, with 50% of the American public willingly endorsing at least one conspiracy theory [47] and up to 75% believing false news headlines [52]. Online social networks propagate misinformation [30] due to the dynamic nature of the content and the reliance of the public on microblogging sites such as Twitter for news and information [45].

In recent years, information systems (IS) researchers have investigated the concept of misinformation [3, 21, 28, 35, 46] and have suggested ways of combating this and other related phenomena [19, 37, 54]. One such proposed method is the use of correction messages to mitigate potentially disruptive rumors. However, such proposed methods may be inefective or even counterproductive if they cause blowbacks [40]. In recognition of the need to address this issue, the Department of Homeland Security (DHS) recently established a 25-member agency, the Social Media Working Group (SMWG) for Emergency Services and Disaster Management; the Federal Emergency Management Agency (FEMA) is a member to help provide recommendations to curb the menace. The agency published a set of guidelines for dispelling rumors in 2018 but noted that correction messages may not always be efective and even have the potential to make the spread of falsehoods worse [16]. Results from prior studies have not only been fragmented, inconsistent, and inconclusive but have also primarily relied on surveys [17, 28, 37, 43, 47].

In this study, we investigate the dynamic interaction between falsehoods and correction messages both theoretically and empirically using panel data. Our research questions are as follows:

(1) Are there bidirectional relationships between the difusion of falsehoods and correction messages on Twitter during shock events?

(2) What are the efects of correction messages on falsehoods and vice versa?

To address these questions and advance our knowledge of this crucial yet intricate relationship, we first develop a theoretical (mechanistic) model depicting the difusion of both falsehoods and correction messages on Twitter and their mutual relationship. We show the conditions under which they can both cease to propagate, both continue to propagate, or only one continues to propagate. Additionally, we use a unique panel dataset containing 279,597 social media interactions during Hurricane Harvey in 2017 and Hurricane Florence in 2018 to empirically examine the bidirectional relationships between the difusion of falsehoods and their correction messages through the structural panel vector autoregression (PVAR) methodology.

Our study has the following contributions to the literature on information difusion, misinformation, and rumors. First, our research holistically examines the difusion of both falsehoods and correction messages, thus achieving a better understanding of how falsehoods and correction messages co-difuse – as well as reinforce and compete with each other – rather than just examining the difusion of each type of message on its own. Second, the use of a theoretical model coupled with empirical evidence allows us to identify scenarios under which each type of message continues or ceases to propagate. We then empirically examine the dynamic relationships using real Twitter data during Hurricanes Harvey and Florence. Third, we derive three possible outcomes through a theoretical and mechanistic model: (1) The numbers of tweets for falsehoods and correction messages both diminish (2) One message (either falsehood or correction) stops spreading and the other one continues to propagate; and (3) Both falsehoods and correction messages continue to difuse. The outcome where falsehoods cease to spread and correction messages continue is the ideal outcome. Fourth, our empirical results using Twitter data show robust evidence that falsehoods cause an increase in correction messages. Counterintuitively, correction messages have a positive efect on the propagation of falsehoods, suggesting that the current state of correction messages is neither optimal nor efective. These results highlight the importance for policy makers, social media administrators, and developers of emergency warning systems to design more efective correction messages and coordinate to efectively combat the propagation of falsehoods while improving the difusion of correction messages.

## Related Literature

## Recent Proposed Solutions

There have been several major proposals for curbing misinformation. For example, researchers have recommended the use of detection [33, 34, 40] to target falsehoods and automated entities on social media in order to prevent the spread of falsehoods. However, several studies using large datasets have shown that falsehoods are not primarily shared by automated entities but rather by humans [19, 54]. Others have proposed the use of source credibility as a solution to this phenomenon [3]. However, the results of these studies have proven to be quite inconsistent. For example, [46] showed that credible sources may be able to lower anxiety and be more successful in suppressing falsehoods, while a more recent study [40] revealed that appealing to coherence was more successful in reducing falsehoods. Finally, two recent studies [31, 32] proposed the use of source rating and presentation in suppressing falsehoods and nudging users toward rethinking and believing a story. Using a survey instrument, the authors found that presenting news in a story format with source ratings may cause users to evaluate the veracity of the news content more critically. However, this solution is mostly used in the retail domain, where users rate credible buyers and sellers and may be vulnerable to manipulations that are dificult to detect [27, 29, 58, 37].

## Information Correction

IS researchers have examined information correction using predictions [25] and inoculation theories [44]. In recent times, government agencies created rumor control mechanisms and aimed to identify, investigate, and mitigate potentially disruptive rumors, especially during extreme events, such as during the aftermath of the great East Japan Earthquake on March 11, 2011 [54]. While results on their efectiveness have been mixed and inconclusive, questions have been raised regarding ideal ways to create and deploy efective correction mechanisms to combat falsehoods. For example, some studies showed that including both facts as well as the falsehood in the same message causes engagement and leads to an overall increase in the knowledge about the falsehood [10]. However, using qualitative studies and reviews from previous studies [50] showed that repeating falsehoods could be detrimental to the overall correction eforts because receivers of the messages may not be able to diferentiate facts from falsehoods and may misremember the message. Quite recently, using a meta-analysis of several studies [59] showed that corrections may reduce misinformation across diverse audiences and may be more successful in informing the receivers. Their study was partially supported by findings from [26], whose results showed that corrections reduce people’s beliefs in specific rumor content, but the senders of the messages were often unable to recover the trust that was lost due to the falsehood. Other studies have introduced factors such as source credibility and coherence in tackling against misinformation correction. For example, [40] showed that when sending a correction message, appealing to coherence was more successful at minimizing the influence of misinformation than using fact checking and source credibility. This occurrence is in direct contrast to [46], who showed that using reliable information with credible sources can lower anxiety and be much more successful in suppressing falsehoods. Another method currently used by rumor control mills is the pairing of correction messages with warnings, which leads to reduced rumor spread [49]. However, this study is the first of its kind to use Twitter data prior to, during, and after shock events that captures in its entirety the interactions between a government agency, fact-checking organizations, and their responses to falsehoods.

In summary, our review of prior research reveals the following gaps in the extant literature:

(1) Due to the fragmented and inconsistent findings, our understanding of the intricate relationship between correction messages and falsehoods is limited with the empirical findings often being contradictory [e.g., 16, 27, 36].

(2) Several prior studies on correction messages have been based on rumors [e.g., 45], which showed that when correction messages are paired with warning messages, rumors tend to reduce in their dissemination. Rumors are social in nature and can be either true or false. It is therefore necessary to investigate the propagation of verifiable false and correction messages.

(3) Findings from prior research have favored the use of small and individual survey samples [e.g., 10, 24] and may lack generalizability to other contexts.

(4) Existing studies did not treat the difusion of both falsehoods and correction messages as endogenous that have feedback loops. Furthermore, none have attempted to investigate the potential for causal inference. As a result, the endogeneity and possible causal relationship between both variables need to be further investigated.

(5) None of the studies have presented a solution supported by theory to mitigate the flow of falsehoods while improving the eficacy of correction messages. Our research examining the co-difusion of falsehoods and corrections will help us better understand how the two afect each other in the difusion process and allow us to design better counter mechanisms.

Our goal is to address these research gaps using a theoretical study supplemented by an empirical analysis using two Twitter datasets.

## Influence of Falsehoods on Correction Messages and Vice Versa

As suggested by previous studies, falsehoods tend to be resilient [19], and the format and presentation of the message may have an impact on their believability [32]. While most studies have centered correction messages as a general topic, none of the studies have investigated this phenomenon using real datasets nor has any attempted to infer causality. A recent study using simulations and networks showed how rumors and correction messages difuse independently through the same users [54]. While several studies have shown that correction messages can be very efective in addressing misinformation on social media by reducing the credibility of the refuted contents and as such are shared more [12, 25], other studies have also pointed out that even after the rebuttals, falsehoods continually influence memory and reasoning even if the retraction is recalled [18]. The study further noted that even after the retraction of false information and specific warnings were combined with an explanation of the misinformation, users still remembered and were influenced significantly by falsehoods. One study further noted that in some cases even though corrections reduce beliefs in the misinformation, the trust may be lost [26].

A recent study [49] argued that when combating falsehoods, presenting warning messages may reduce their propagation and thus improve the quality of information that is being shared in online social networks. This analogy does not state that the news ultimately dies but that it counterbalances the information flow. We therefore argue that once the correction message is introduced and people see the message, some may refrain from resharing the false messages while others may engage the correction message. These actions will slow the rate of the difusion of falsehoods but increase the difusion of correction messages over time.

## Theoretical Model and Analysis

We develop a mathematical mechanistic model that describes the difusion of a falsehood topic and its corresponding correction messages on Twitter. In contrast to the Bass difusion model [6] that describes the spread of an innovation, our model describes the competition between the two messages besides their spread. Our model originates in the literature of mathematical ecology as a model of competitive exclusion [20]. We extend the model based on the literature to include mutual reinforcement of each message to the other. The model is comprised of a system of ordinary diferential equations and implemented via numerical simulations and stability analysis. The model depicts the competition of these two falsehood and correction messages.

Let $M _ { t }$ be the number of tweets and retweets of falsehood $F _ { t }$ and correction $C _ { t }$ messages at hour t. The system ofdiferential equations:

$$
\frac {d F _ {t}}{d t} = r _ {F} F _ {t} \left[ \left(1 - \frac {F _ {t}}{K}\right) - \beta_ {F} \frac {C _ {t}}{K} \right] - \mu_ {F} F _ {t} + \gamma_ {F} C _ {t}\tag{1}
$$

and

$$
\frac {d C _ {t}}{d t} = r _ {C} C _ {t} \left[ \left(1 - \frac {C _ {t}}{K}\right) - \beta_ {C} \frac {F _ {t}}{K} \right] - \mu_ {C} C _ {t} + \gamma_ {C} F _ {t}\tag{2}
$$

depict the rate of change in the numbers of tweets or retweets of the falsehood and correction messages at time $t ,$ respectively. The first components in both equations $r _ { M } M _ { t } \big [ ( 1 - M _ { t } / K ) - \beta _ { M } M _ { t } ^ { \prime } / K \big ]$ capture the growth rate of the message $M _ { t }$ (where $M _ { t } =$ $F _ { t }$ or $C _ { t } \mathrm { ; }$ and $M _ { t } ^ { \prime } = C _ { t }$ or $F _ { t } { \mathrm { : } }$ , respectively) with a maximum capacity to tweet/retweet, as well as the negative impact (competition efect) of the other message $M ^ { \prime }$ on the difusion of M. $K ,$ measured on the same scale as $F _ { t }$ and $C _ { t } ,$ is the capacity (e.g., number of Twitter user or bot accounts) to tweet or retweet, $r _ { M }$ (units: hour ) is the per-tweet retweet rate of message M, and $\mu _ { M }$ (units: hour<sup>−1</sup>) captures the loss of interest among Twitter users of the falsehood or correction message M, $\beta _ { M }$ (unitless) is the aggressiveness of the message $M ^ { \prime }$ in its interaction with message ${ \cal M } ( M , M ^ { \prime } = F , C ; M \ne M ^ { \prime } )$ and captures the reputation of the issuer of the message as well as the efectiveness or structure of the message. The parameter $\gamma _ { M }$ $( \mathrm { u n i t s } ; \mathrm { h o u r } ^ { - 1 } )$ is the rate at which the other message $M ^ { \prime }$ is reinforcing the growth of message M: Despite the common conception that correction messages reduce the spread of falsehoods, academic research has shown the opposite may happen due to how correction messages are interpreted and used to reinforce beliefs of falsehoods [22]. Hence, we use $\gamma _ { M } M _ { t } ^ { \prime }$ to capture such possible positive impacts (reinforcement) of falsehoods and correction messages on each other’s difusion. All the parameters in this model are positive.

![](/api/attachments/QT7RV2GJ/fulltext/images/b30ccd4a1493ed8805854827a5a948ea98ac46787e2aaf9b09b60748b7c4b503.jpg)  
Figure 1. Possible Outcomes of Interaction Between Falsehood (F) and Correction (C) Tweets.

We provide the complete details on the stability analysis in the online supplemental Appendix A. In summary, the underlying system of equations has the following possible equilibria:

(1) ${ \cal F } ^ { * } = 0 ,$ , and $C ^ { * } = 0 ;$

(2) $F ^ { * } = 0$ , and $C ^ { * } \ = K \big ( 1 - \mu _ { C } / r _ { C } \big )$ , which exists only if $\gamma _ { F } = \gamma _ { C } = 0$ and $\mu _ { C } < r _ { C } ;$

(3) $F ^ { * } = K \big ( 1 - \mu _ { F } / r _ { F } \big )$ , and $C ^ { * } = 0$ , which exists only if $\gamma _ { F } = \gamma _ { C } = 0$ and $\mu _ { F } < r _ { F } ;$

$$
\gamma_ {F} = \gamma_ {C} = 0, F ^ {*} = K \left(\left(1 - \mu_ {F} / r _ {F}\right) - \beta_ {F} \left(1 - \mu_ {C} / r _ {C}\right)\right) / \left(1 - \beta_ {F} \beta_ {C}\right)
$$

and $C ^ { * } = K \big ( \big ( 1 - \mu _ { C } / r _ { C } \big ) - \beta _ { C } \big ( 1 - \mu _ { F } / r _ { F } \big ) \big ) / \big ( 1 - \beta _ { F } \beta _ { C } \big )$ , which exists only when $0 \leq F ^ { * } , C ^ { * } \leq K$ . If, $\gamma _ { F } , \gamma _ { C } { \neq } 0$ , the fourth equilibrium point is more complicated to be presented here, and it will be handled numerically. In that case there are only two equilibria, (1) and (4).

Figure 1 provides a visual illustration of the possible outcomes. Figure 1(a) shows the scenario where eventually both falsehood and correction messages stop spreading under the appropriate conditions. Figure 1(b) shows a situation where tweets containing falsehoods stop spreading, while correction tweets continue to propagate. This scenario is ideal in the fight against misinformation. We can reduce and eliminate falsehoods while ensuring that correction messages continue spreading. In this simulation, we show that correction messages eliminate falsehoods while increasing in tweet/retweets. This model can be interchanged to ensure that the opposite happens: falsehoods continue to spread by eliminating correction messages. Figure 1(c) shows a scenario in which both falsehood and correction messages continue.

The mathematical model in Equations (1-2) can be linearized to create a panel vector autoregression model with p lags. The derivation of the empirical model based on the theoretical model can be found in the online supplemental Appendix B.

## Empirical Evidence

## Data

Our data consist of verified false tweets and their correction tweets during Hurricane Harvey in 2017 and Hurricane Florence in 2018. We selected these two extreme events because studies have shown that misinformation propagates the most “during events that have importance in the lives of individuals and when the news received about them is either lacking or subjectively ambiguous” [4]. Hurricanes match these descriptions because they create public safety concerns and are quite unpredictable. Furthermore, hurricanes allow researchers to accurately record exactly when the rumor associated with the shock event begins and ends. As a result, we can measure the beginning and ending of the shock event (a hurricane), which cannot be said for other crisis scenarios. For example, unlike hurricanes, it is not easy to predict when an earthquake or other natural disasters occur. Hence, when we capture data after a shock event occurs, it may lead to not only data with missing information but also endogeneity.

Our data collection steps were as follows: First, we identified and collected all tweets during Hurricane Harvey, from August 18 to September 22, 2017, and Hurricane Florence, from September 5 to October 3, 2018, using the Twitter stream API in real time. We used keywords and hashtags related to the hurricanes and the ensuing flooding, such as “#Harvey,” “Hurricane Harvey,” “Gulf Coast Hurricane Harvey,” “#HoustonFlood,” “#HoustonFlooding,” “#Florence,” “Hurricane Florence,” “#FlorenceNC,” “#FlorenceFlood,” and “#FlorenceFlooding.” This resulted in 12,357,530 tweets and retweets during the two extreme events with data on the content of each tweet, user metadata that includes information about the post, the author, a snapshot of the author’s profile, and other related images at the time the tweet was posted. We performed standard text preprocessing on the tweet corpus, including converting all characters to lower cases, tokenization, text normalization and removing stop words.

Next, we identified 21 falsehood stories during the two hurricanes, either from FEMA’s rumor control page and their Twitter timelines within those periods or from verified fake stories by at least four out of five independent fact-checking websites: Snopes, Factcheck.org, PolitiFact, Truth or Fiction and BS Detector. The use of these fact-checking websites similar to [57] allows us to ensure the accuracy of the veracity of the news. We obtained a total of 21 verified falsehoods topics as a result. An example of a false tweet on a shark on the freeway in Houston during Hurricane Harvey, an ensuing correction message, a rebuttal of the correction message, and another subsequent correction tweet are shown in Table 1.

As the number of keywords from each verified false tweet topic from FEMA and factchecking websites was limited and would not allow us to identify all related tweets from our sample, we next used topic modeling technique Latent Dirichlet allocation (LDA) to identify a more comprehensive list of keywords associated with each topic. This process was done by running the LDA separately for each of the 21 tweet topics by trying diferent numbers of subtopics, reviewing the resulting subtopics and keywords associated with each subtopic, and identifying all relevant keywords. This generative modeling technique exposes and identifies underlying topics in text documents and their similarities between them [8]. An example would be identifying “fish” as an additional keyword based on the LDA results for the fake shark story during the hurricanes, as using “shark” only would leave out relevant tweets including “fish” in the tweets. We used this more comprehensive list of keywords to filter our tweet sample and removed all irrelevant or duplicate tweets. At the end, we obtained 279,597 tweets and retweets on the 21 verified falsehoods and their correction message topics during the two hurricanes. We then hand-coded each tweet as either a falsehood or a correction message. Tweets that repeat, corroborate, or cite verified falsehoods were coded as falsehoods, while tweets debunking or citing those rebutting the falsehoods were coded as correction messages.

Table 1. Sample False and Correction Tweets.

<table><tr><td>Tweet Type</td><td>Tweet Content</td></tr><tr><td>Original falsehood</td><td>&quot;Believe it or not, this is a shark on the freeway in Houston, Texas. #HurricaneHarvy&quot;</td></tr><tr><td>Correction message</td><td>&quot;Harvey Hoax: There are no sharks on Houston&#x27;s flooded freeways http://dlvr.it/PjCr91&quot;</td></tr><tr><td>Rebuttal of correction message</td><td>&quot;That ain&#x27;t what I heard&quot;</td></tr><tr><td>Additional correction message</td><td>&quot;Fact check: A shark in the street, and other Hurricane Harvey rumors you shouldn&#x27;t believe&quot;</td></tr></table>

Table 2. Descriptive Statistics of Falsehoods and Correction Messages.

<table><tr><td rowspan="2">Topic</td><td colspan="3">Falsehoods</td><td colspan="3">Corrections</td></tr><tr><td>Obs.</td><td>Mean</td><td>Std. Dev.</td><td>Obs.</td><td>Mean</td><td>Std. Dev.</td></tr><tr><td>Black Lives Matter and emergency response</td><td>10</td><td>0.08</td><td>0.40</td><td>9,651</td><td>72.56</td><td>140.90</td></tr><tr><td>Donation to Clinton foundation</td><td>10,130</td><td>25.33</td><td>59.41</td><td>500</td><td>1.25</td><td>6.20</td></tr><tr><td>Georgia mosque relief effort</td><td>793</td><td>8.62</td><td>13.61</td><td>45</td><td>0.49</td><td>2.89</td></tr><tr><td>FEMA hiring</td><td>6</td><td>0.02</td><td>0.15</td><td>755</td><td>2.71</td><td>14.57</td></tr><tr><td>Prince Harry&#x27;s donation</td><td>8,433</td><td>32.31</td><td>68.57</td><td>5</td><td>0.02</td><td>0.14</td></tr><tr><td>Harvey shark</td><td>2,787</td><td>6.88</td><td>7.90</td><td>1,562</td><td>3.86</td><td>12.74</td></tr><tr><td>Florence shark</td><td>42,197</td><td>126.34</td><td>231.72</td><td>40,182</td><td>120.31</td><td>439.22</td></tr><tr><td>Texas mosque relief effort</td><td>10</td><td>0.04</td><td>0.22</td><td>357</td><td>1.47</td><td>4.24</td></tr><tr><td>Underwater planes</td><td>33</td><td>0.41</td><td>0.92</td><td>141</td><td>1.74</td><td>3.38</td></tr><tr><td>Brunswick nuclear plant</td><td>13,559</td><td>39.53</td><td>55.32</td><td>694</td><td>2.02</td><td>4.72</td></tr><tr><td>Diverted funds</td><td>12,043</td><td>35.84</td><td>128.32</td><td>45</td><td>0.13</td><td>0.50</td></tr><tr><td>FEMA budget</td><td>4,824</td><td>8.82</td><td>45.79</td><td>191</td><td>0.35</td><td>4.44</td></tr><tr><td>Tetanus due to flooding</td><td>106,748</td><td>207.68</td><td>113.26</td><td>65</td><td>0.13</td><td>0.72</td></tr><tr><td>Environmental Protection Agency</td><td>31</td><td>0.10</td><td>0.47</td><td>10</td><td>0.03</td><td>0.24</td></tr><tr><td>Navy destroyer</td><td>3</td><td>0.14</td><td>0.47</td><td>25</td><td>1.14</td><td>4.89</td></tr><tr><td>Mayweather donation</td><td>716</td><td>3.20</td><td>9.80</td><td>248</td><td>1.11</td><td>3.55</td></tr><tr><td>Category 6 hurricane</td><td>87</td><td>0.34</td><td>0.92</td><td>72</td><td>0.28</td><td>1.15</td></tr><tr><td>Manny donation</td><td>195</td><td>1.08</td><td>2.52</td><td>5</td><td>0.03</td><td>0.20</td></tr><tr><td>Pets and service animals</td><td>14</td><td>0.04</td><td>0.24</td><td>127</td><td>0.34</td><td>1.22</td></tr><tr><td>Immigration law enforcement</td><td>8,461</td><td>23.31</td><td>126.18</td><td>13,755</td><td>37.89</td><td>132.98</td></tr><tr><td>Prince William&#x27;s donation</td><td>80</td><td>0.12</td><td>0.85</td><td>2</td><td>0.003</td><td>0.06</td></tr><tr><td>Total</td><td>211,160</td><td>33.29</td><td>99.56</td><td>68,437</td><td>10.79</td><td>111.44</td></tr></table>

In order to obtain the difusion count data, we kept track of tweets and retweets by hour for each falsehood and correction topic over the duration of the data collection period and obtained a minimum of 22 and a maximum of 648 hours of tweets for every falsehood and correction topic. This tally ultimately resulted in 6,343 hourly observations for 21 topics. Table 2 summarizes the descriptive statistics of the counts of the tweets and retweets by veracity and topic. The correlation coeficient between the hourly tweet counts of falsehoods and correction messages was 0.41.

## Empirical Model Specification

Based on our simulation results, we next conducted an empirical analysis using time series and PVAR models [1, 41] to characterize the dynamic relationships between falsehoods and correction messages. Vector autoregression (VAR) is a stochastic process model commonly used in economics to capture the linear relationships among multiple time series variables [1, 30]. It has a robust framework that can be easily verified and replicated. In addition, it addresses biases that might arise due to autocorrelations, endogeneity and causal inferences [42]. In IS research, it has been applied to examine the relationships between sentiments from microblogs and stock returns [15] as well as the existence of several patterns of supply-side technology relationships in the context of wireless networking [2]. In this research, we use it to examine how the difusion of falsehoods and correction messages unfold as a result of falsehood and correction message tweets in the past. The framework allows us to treat both falsehoods and correction message tweets as endogenous, predict them using their lags, and capture the feedback loops among them [1]. For example, falsehoods in the current period may influence the number of correction messages in the next period, which may cause a change in the following period’s falsehoods.

Building on a structural VAR, we analyze the dynamic efects between false tweets and their correction messages during Hurricanes Harvey and Florence based on [1]. We empirically estimate the difusion between falsehoods $F _ { t }$ and correction messages $C _ { t }$ based on their past difusion histories. We model both as endogenous in the $\left( 2 \mathbf { \Delta x } 1 \right)$ vector $M _ { i t } = \left( F _ { i t } , C _ { i t } \right)$ , where we now include subscript i as we have data on 21 diferent topics $i \in \left( 1 , 2 , \ldots , 2 1 \right)$ at every hour $t \in \left( 1 , 2 , \ldots , T _ { i } \right)$ : Due to the non-stationarity nature of our sample and excessive zeros, we follow [2] and transform both messages by taking natural logarithm plus 0.5 of the variables. Dickey Fuller and the Fisher type unit root tests [11] for non-strongly balanced data sets show that the transformations are stationary.

To capture the dynamics between falsehoods and correction messages we estimate the following:

$$
M _ {i t} = M _ {i, t - 1} A _ {1} + M _ {(i, t - 2)} A _ {2} + \dots + M _ {i, t - p} A _ {p} + \eta_ {i t} \theta_ {1} + h _ {i t} \theta_ {2} + u _ {i} + \varepsilon_ {i t},\tag{3}
$$

where the $( 2 \times 2 )$ matrices $A _ { 1 } , \ A _ { 2 } , \ . . . , \ A _ { p }$ along with the vectors $\theta _ { 1 }$ and $\theta _ { 2 }$ are the parameters to be estimated. Moreover, $\eta _ { i t }$ is a $( 1 \times 2 )$ vector of exogenous dummy variables representing the year and $h _ { i t }$ is the matrix of exogenous dummy variables that captures the hour of the day. The lag order $\boldsymbol { p }$ is determined empirically from the data. In addition, $u _ { i }$ and $\varepsilon _ { i t }$ are $( 1 \times 2 )$ vectors of dependent variable-specific panel fixed efect and idiosyncratic errors, respectively.

In the online supplemental Appendix B, Equation 3 follows from Equations 1 and 2, where we approximate the continuous changes in falsehoods and corrections with discrete changes at the hourly level. The structure in Equation 3 is a panel version of [53] that allows a flexible approach to model dynamics between falsehoods and corrections. The assumptions on the innovations are $E ( \varepsilon _ { i t } ) = 0 , E \bigl ( \varepsilon _ { i t } ^ { \phantom { \dagger } T } \varepsilon _ { i t } \bigr ) = \Sigma$ , and $E \big ( \varepsilon _ { i t } ^ { ~ T } \varepsilon _ { i s } \big ) = 0$ for all $t > s$ which is a white noise multivariate process of our two variables. Following studies by [24], we assume that the topics (i.e., cross-sectional units) share the same underlying data generating process, with common parameters $A _ { 1 } , A _ { 2 } , . . . , A _ { p } .$ We use Equation 3 to test for the existence of dynamic relationships between the number of falsehood tweets and correction tweets. The time period is from 0 to 313 hours.

Table 3. Estimates of Dynamic Efects Between Falsehoods and Corrections.

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td colspan="3">All Topics</td><td colspan="2">Florence</td><td colspan="2">Harvey</td></tr><tr><td>Variables:</td><td> $F_{it}$ </td><td> $C_{it}$ </td><td> $F_{it}$ </td><td> $C_{it}$ </td><td> $F_{it}$ </td><td> $C_{it}$ </td></tr><tr><td> $F_{i,t-1}$ </td><td>0.504***(0.021)</td><td>0.027**(0.015)</td><td>0.491***(0.028)</td><td>0.042**(0.016)</td><td>0.02(0.023)</td><td>0.004(0.032)</td></tr><tr><td> $F_{i,t-2}$ </td><td>0.243***(0.022)</td><td>0.032**(0.017)</td><td>0.211***(0.028)</td><td>0.007(0.018)</td><td>0.01(0.020)</td><td>0.078**(0.034)</td></tr><tr><td> $F_{i,t-3}$ </td><td>0.169***(0.019)</td><td>-0.018(0.015)</td><td>0.169***(0.024)</td><td>-0.02(0.017)</td><td>0.003(0.022)</td><td>-0.032(0.028)</td></tr><tr><td> $C_{i,t-1}$ </td><td>0.042***(0.016)</td><td>0.538***(0.027)</td><td>0.494***(0.036)</td><td>0.534***(0.034)</td><td>0.070***(0.021)</td><td>0.527***(0.039)</td></tr><tr><td> $C_{i,t-2}$ </td><td>0.001(0.014)</td><td>0.218***(0.024)</td><td>0.288***(0.035)</td><td>0.232***(0.030)</td><td>-0.021(0.021)</td><td>0.205***(0.039)</td></tr><tr><td> $C_{i,t-3}$ </td><td>0.008(0.016)</td><td>0.153***(0.021)</td><td>0.155***(0.031)</td><td>0.131***(0.026)</td><td>0.015(0.020)</td><td>0.169***(0.033)</td></tr><tr><td>Topic  $FE^a$ </td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Year FE</td><td colspan="2">Yes</td><td colspan="2">No</td><td colspan="2">No</td></tr><tr><td>Hour FE</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Obs.</td><td colspan="2">5,997</td><td colspan="2">3,870</td><td colspan="2">2,127</td></tr></table>

Notes: Robust standard errors in parentheses. \* p<0.1; \*\* p<0.05; \*\*\*p<0.01. Controls for topic, year, and hour fixed efects.

## Empirical Results

We estimate diferent versions of Equation 3 using the generalized method of moments (GMM) estimators described in [1]. Our baseline model pools data from all topics, while our second and third models use only the topics for Florence and Harvey, respectively. We select the optimal lag $\boldsymbol { p }$ for each of the models based on a multivariate version of the Bayesian information criteria as recommended in [5].<sup>1</sup> For our three models $\boldsymbol { p } = 3$ had the best performance. To improve eficiency, we included longer sets of lags as instruments as recommended by [1]. This approach has the unattractive property of reducing observations, especially with unbalanced panels and those with missing data because past realizations are not included. A proposed solution recommended by [24] is to use the method of moments in the estimation, which substitutes missing observations with zeros, but this solution does not solve the reduced observation problem associated with unbalanced panels. Hence, we used the first to fourth lags as instruments.

The coeficients in $A _ { 1 } , A _ { 2 } ,$ and $A _ { 3 }$ from the estimation of Equation 3 for the first three models are reported in Table 3. The numbers in parentheses are robust standard errors. All specifications include topic and hour dummies to control for unobserved diferences between topics as well as factors that might change during the day. In addition, the first model includes a year fixed efect to control for diferences across hurricanes. We observe that across all models most of the coeficients on the lagged falsehoods and corrections are statistically significant in both the falsehood and correction equations. The positive coeficients show that lagged falsehood and correction tweets not only contribute to more of their own tweets in subsequent hours but also reinforce subsequent tweets of the opposite message type. This evidence supports the existence of dynamics between $F _ { i t }$ and $C _ { i t }$ , and it is consistent with the predictive causality tests between $F _ { i t }$ and $C _ { i t }$ reported in the online supplemental Appendix C.

All the statistically significant point estimates reported in Table 3 are positive, suggesting a direct bidirectional relationship between $F _ { i t }$ and $C _ { i t }$ . To be able to better assess the relationship between the two, we focus on the analysis of the results using the vector moving average representation of Equation 3. Hence, in Figure 2 we plot the impulse response functions to capture the dynamic efects of an exogenous variation in corrections on falsehoods (left-hand side), and of falsehoods on corrections (right-hand side), with all other efects held constant [1, 38]. The shaded areas correspond to the 95% confidence intervals based on 200 Monte Carlo simulations using the Gaussian approximation.

The plot on the left-hand side of Figure 2 shows how a one standard deviation positive shock in $C _ { i t }$ has a positive and statistically significant efect on $F _ { i t }$ that lasts for over 48 hours. Note that the response in the Y-axis is measured in number of falsehoods. The efect is quite surprising, as it illustrates how corrections actually increase falsehoods. It is reasonable to argue that FEMA is likely to pursue the opposite efect when trying to correct false messages. That is, the organization probably expects that the competition efect, captured by $\beta _ { F }$ in Equation 1, dominates the reinforcement efect $\gamma _ { F }$ . This interpretation is consistent with the existing literature that documents policies that obtain results that are the opposite of the expected results as originally intended [23], with our estimates suggesting that correction tweets increase the awareness of or strengthen prior beliefs of falsehoods, thus intensifying the spread of falsehoods. Note that the contemporaneous response is constrained to zero due to the ordering of the endogenous variables in the Cholesky decomposition. The Cholesky decomposition, originally proposed by [50], imposes identification restrictions, and in our case, we impose the restriction that falsehoods occur first. This makes sense because corrections can only exist if there has been a falsehood.

![](/api/attachments/QT7RV2GJ/fulltext/images/a07633d1454beb7c7ba1bb8a9496a6ec0172ebfb194ac9066fe16257a5b4695f.jpg)  
Figure 2. Impulse Response Functions for All Topics.

The plot on the right-hand side shows how a one standard deviation exogenous increase in falsehoods increases corrections, where the response in the Y-axis is measured in number of corrections. The efect is statistically significant at the 95% level for at least 48 hours. This result is expected where the relative importance of $\gamma _ { C }$ is greater than $\beta _ { C }$

The results on the left-hand side of Figure 3 illustrate how an exogenous increase in $F _ { i t }$ leads to more falsehood messages in the following two days, with the efect being statistically significant at the 95% level. Note that the marginal efect is relatively larger during the first few hours and drops relatively fast and monotonically. This positive efect shows how the natural growth rate of falsehoods $r _ { F }$ is dominating the loss of interest $\mu _ { F } ,$ , signaling the existence of herding efects [60]. A similar story holds for corrections on the right-hand side of the figure, where it is worth noting the similarity between both sides.

![](/api/attachments/QT7RV2GJ/fulltext/images/3c7ae019784830ec76fdc2f7c5d37a571efdf218347e6e07a04c6f435dd3f10e.jpg)  
Figure 3. Impulse Response Functions for All Topics.

![](/api/attachments/QT7RV2GJ/fulltext/images/752db87b218884b9b81e526d67be1d901c9c031bb0e5dc84435b74d64dc36ae0.jpg)  
Figure 4. Impulse Response Functions at the Hurricane Level.

![](/api/attachments/QT7RV2GJ/fulltext/images/84227c4b135949b1c63490173465c6fcef79e1b9cf5aa3dc7e3b75b3304b73a0.jpg)  
Figure 5. Impulse Response Functions When Controlling for Networks and Bots.

We plot the impulse response functions for falsehoods and corrections on each other separately for Hurricanes Harvey and Florence in Figure 4. The results are similar across the two hurricanes and are consistent with those in Figure 2, where positive reinforcement efects of falsehoods exist on both correction tweets and on correction tweets of falsehoods.

## Robustness Checks

We performed multiple robustness checks to verify our empirical results under diferent scenarios. First, we calculated bi-hourly tweet counts instead of hourly counts for our main empirical analyses. The optimal lag of the bihourly model was two, consistent with the lag of three for the hourly tweet count model of data from both hurricanes. We also obtained consistent results of the dynamic efects where correction tweets caused falsehoods to increase and falsehoods also caused corrections to increase.

Second, we controlled for the networks of the accounts responsible for tweets and retweets in terms of the numbers of followers and obtained similar results. We achieved this outcome by multiplying each tweeted or retweeted message by the account’s total number of followers. This new measure is likely to be a good approximation of the number of people who see the message. The resulting impulse response functions are plotted on the left-hand side of Figure 5. Consistent with previous results, the responses of falsehoods and corrections to one another are both positive and statistically significant, with efects that last for over two days. The most striking diference is on the magnitude of the coeficients as on average the responses are at least twice as large as before. Moreover, the marginal efects peak at about 10 hours after the original message versus the 18 hours found earlier. It makes sense to observe these larger efects as messages from accounts with more followers are more likely to have larger impacts.

Third, we controlled for bots on Twitter. A Twitter bot performs automated actions such as tweeting or retweeting which have been pre-programmed by a user on an account. In this research, we are interested in modeling the dynamics between falsehood and correction messages, including the participation of bots because users experience it. However, we also assessed whether our results change after controlling for bots, as some bots might be aimed at reproducing falsehoods. Leveraging the Botometer bot detection algorithm [13], we calculated the likelihood of each Twitter account in our sample being a bot based on the account profile and tweet/retweet history. Accounts with likelihoods less than .5 were labeled as humans and those with .5 or higher were labeled as bots. We then aggregated the total number of tweets/retweets per hour in our dataset for bots and non-bots separately. The impulse response functions on the right-hand side of Figure 5 control for bots by estimating an augmented version of Equation 3 using $M _ { i t } = ( F _ { i j } ^ { \times B } , F _ { i j } ^ { B } , C _ { i j } ^ { \ N B } , C _ { i j } ^ { \ B } )$ to model the dynamics of messages from bots $( F _ { i j } ^ { B }$ and $C _ { i j } ^ { B } )$ and non-bots $( \check { F } _ { i j } ^ { N B }$ and $C _ { i j } ^ { N B } )$ as four endogenous variables.<sup>2</sup> The results mirror the previous results in statistical significance and magnitude.

Fourth, we controlled for the fact that diferent topics have diferent total numbers of messages. We reran the analysis after dropping 11 topics that had less than 1,000 observations between falsehoods and corrections and another analysis using the total number of messages as weights. This process is similar to running weighted least squares to correct for heteroscedasticity and account for the possibility that topics with more messages might be measured with more precision. The results showed to be consistent across all these robustness checks.<sup>3</sup>

Fifth, we ran separate analyses after classifying topics under environmental news and under social news. The results were consistent with positive reinforcements between falsehoods and correction messages on Twitter.

## Discussion

The current research examines the dynamic efects between the difusion of falsehoods and correction messages on social media during shock events. We model falsehoods and corrections as two competing messages on Twitter and develop a theoretical model that illustrates diferent scenarios under which only one type of message survives, both survive, or both die of. We further provide empirical evidence supporting our theoretical modeling results using tweets data collected from Hurricanes Harvey and Florence. Our study has the following theoretical contribution and practical implications.

## Theoretical Contributions

First, we contribute to the literature on information difusion, rumors, misinformation and correction and bridge the gaps in literature by investigating the bidirectional relationships between both falsehoods and correction messages and how each afects the other in the Twittersphere. Previous studies have examined the efects of either falsehoods or correction messages on human behavior [17, 18, 28] or the lasting efects of misinformation on the behavior of humans after exposure to falsehoods [26]. Some studies have also proposed methods to efectively debunk misinformation and present correction messages [31, 37, 46]. Our study is the first to examine both simultaneously and how falsehoods and correction messages afect each other’s difusion on social media. As a result, our research provides a more holistic picture of the diferent scenarios under which each type of message propagates or is eliminated, how falsehoods and correction messages co-difuse on social media, and how one afects the other’s tweet count. Furthermore, we show how user networks and automated entities such as bots play a role in the nomology of things.

Second, we develop a theoretical model of the difusion using ordinary diferential equations. The model takes into consideration the fact that when both falsehoods and correction messages coexist dependently of each other, they vie for users’ attention. Our model allows us to capture the competition between falsehoods and correction messages, their reinforcement of each other, and the loss of interest among Twitter users for either type of messages during their difusion. Our analysis shows three possible outcomes. First, the more dominant message eliminates the weaker. In our model, we posit that the ideal or optimal scenario (Figure 1(b)) occurs when we observe falsehoods die of because their pertweet retweet rate is considerably lower than users’ interest in the message and correction messages prevail with a per-tweet retweet rate that is higher than users’ loss of interest in the correction message. This occurrence happens when Twitter users share the correction messages more than falsehoods when they find these correction tweets to be more novel, newsworthy, or awe-inspiring. In contrast, when users find falsehoods to be more appealing, newsworthy, or believable, they share them more than correction tweets, leading to the scenario when falsehoods prevail, and correction messages die of. Second, our theoretical model shows that under certain conditions both falsehood and correction messages “survive” (Figure 1(c)). This behavior was noted in a recent study by [57] that showed that sometimes messages may survive at lower frequencies only to resurface and flare up once the conditions are appropriate. An example is the shark story during both hurricanes that resurfaced several times in the past years. This falsehood may thus become quite harmless, receive less tweets and shares, and its target audience also changes. This finding is supported by empirical evidence that suggests when tension from those messages dissolves, it resurfaces by repackaging itself as a diferent news story to attract a diferent audience [51]. Third, falsehoods and correction messages may both die of (Figure 1(a)). On Twitter, this occurrence happens when the users do not find the news or messages appealing enough to share. Studies have shown that falsehoods usually contain less information but aim for novelty and some awe-inspiring efect on users [48]. Previous studies further corroborated this theory by showing that novel and awe-inspiring news stories go viral more than news stories that are not [7, 26].

Third, we provide empirical analyses using data of falsehood and correction tweets collected during Hurricanes Harvey and Florence. Our results are consistent across both hurricanes and are robust in additional analyses that control for the networks, bots, number of messages on the topic, and news category. Our empirical results reveal that the third outcome of our theoretical model where both types of messages survive (Figure 1(c)) to be the case, rather than the optimal scenario where correction messages eliminate falsehoods (Figure 1(b)). Specifically, we find that correction messages from FEMA and other factchecking organizations are not only inefective but also help in spreading falsehoods on social media. The results may be indicative of the flaws that can be attributed to FEMA and other fact-checking organizations’ responses to falsehoods on social media. Our result further contradicts those from studies on the efectiveness of using correction messages. For example, prior research [25, 46, 56] suggests that exposing users to correction information that refutes falsehood reduces its spread. In contrast, our results indicate that the reinforcement efect (γ) dominates the competition efect (β) where correction messages create awareness or reinforce users’ prior beliefs of falsehoods, thus leading to a wider spread of falsehoods. We propose increasing the per-tweet retweet rate of correction messages in order to overwhelm falsehoods or not issuing corrections at all. Our results indicate that currently leaving falsehoods to run their course may be even more efective than the current correction approaches, as results indicate they cause blowbacks. This phenomenon can be attributed to falsehoods losing their novelty over time if left alone. Prior studies have shown that the spread of falsehoods on social media is afected by its novelty, such that falsehoods are more novel than real news stories and disseminate faster [57]. Moreover, studies on message framing showed that humans behaved consistently irrationally, relying on several mental shortcuts to speed up reasoning, which can make people remarkably sensitive to how events are framed [56]. Recent studies have shown that humans may be reinforcing beliefs when they attempt to warn of inherent misinformation, such as during political elections without framing the correction accurately [39]. This notion can also be attributed to the presentation and format of the news item, as espoused by a recent study [24] that revealed certain changes in the way information is presented influences how users perceive and behave on the information.

Finally, our theoretical results show how the difusion of falsehoods can eventually be reduced and removed by making the per-tweet retweet rate of correction greater than the rate of the loss in interest in it. An alternative is to make the correction message aggressive enough to discredit the falsehood and establish the facts correctly. Even though the ideal scenarios from our theoretical model suggest that one message will survive while the other one dies of, our empirical results suggest falsehoods and correction messages feed of each other on Twitter and each lead to more of the other. Hence, the current state of correction messages has not reached the equilibrium state of reducing and eventually eliminating falsehoods. Given the inefectiveness of the correction messages in reducing falsehoods, our theoretical modeling results show the conditions under which correction messages can efectively eliminate falsehoods. For instance, when there is no reinforcement, when the per-tweet retweet rate of correction messages are greater than its loss of interest rate, correction messages will expel falsehoods and prevail on Twitter.

## Practical Implications

This study has the following practical implications for government agencies and social media platforms. First, the results from our study can inform government agencies such as FEMA and policy makers on the inefectiveness of current rebuttals and correction messages on social media and help them understand the relationships between falsehoods and correction messages and the impact of framing correction messages. For example, repeating the same falsehood message “shark on the freeway in Houston” when debunking the falsehoods on shark sightings might not be the best approach and might reinforce the belief in the falsehood. This procedure may also encourage people to look for and reshare those false messages, as research has shown that falsehoods tend to contain less information and instead rely on “catchy” headlines meant to attract users [48]. This change in procedure can go a long way in helping government agencies design more efective correction messages in the fight against misinformation. For example, rather than simply refuting the Hurricane

Harvey shark story as false, correction tweets with more supporting evidence, such as Google reverse image search results showing a date earlier than Hurricane Harvey or the original image where the photoshopped Houston freeway shark image came from, may provide a more convincing rebuttal of the falsehood. Such messages with more clear evidence may be perceived as more novel and garner more per-tweet retweets, thus curbing the difusion of falsehoods.

Second, the findings from this study can assist government agencies and administrators in the design of efective emergency warning systems that can safeguard lives during emergencies and crises situations, such as earthquakes and hurricanes. Studies have shown that during emergency situations people are susceptible and fall prey to falsehoods [52]. Hence, we propose a few actionable recommendations. For government agencies to efectively succeed in their combat against falsehoods on social media, we suggest they first increase the per-tweet retweet rates (sharing) of correction messages. This action may be achieved by restructuring and strategizing on their social media presence. Studies have shown that the majority of US citizens use social media for news [45]. Government agencies should consider increasing their social media presence, for example, in every state. In addition, they can consider having their social media presence interconnected with other federal and state agencies across the country. These government agencies (federal and state) may then mirror rebuttals and corrections where appropriate. For example, a recent study on the analysis of cascades suggests that while difusion is inhibited when similar content from competing cascades difuse in tandem, similar content from parallel cascades tend to amplify each other [61]. Thus, if such agencies work in unison, the per-tweet retweet rate for correction messages can substantially increase. Moreover, government agencies may need to create incentives, such as tax benefits for private entities and independent fact-checking organizations to encourage fact checking. Government agencies may also form partnerships with fact-checking organizations and exchange information with each other when important falsehoods emerge. These collaborations ensure that shared knowledge can flow more freely, and the response time to debunk falsehoods is improved. It also provides a single voice in the fight against misinformation.

Third, the results from this study can help social media platforms in understanding the difusion of falsehoods and correction messages and in combating the spread of the former. In order to reduce the per-tweet retweet rate of falsehoods, social media platforms can use more eficient automated detection technology to flag suspicious messages based on a combination of user, textual content, and network features. The use of these methods as a first line of defense may drastically reduce the total number of falsehoods being spread. In addition, empirical evidence suggests that bots are also responsible for sharing falsehoods though not significantly higher than humans [57]. Hence, it is important for social media platforms to efectively detect, thwart, and remove automated malicious entities [36]. The adoption of such technologies can considerably reduce the per-tweet retweet rate of falsehoods by automated entities and ultimately reduce the spread and per-tweet retweet rate of falsehoods.

Finally, government agencies and fact-checking organizations can use the empirical framework presented in this research to further understand the bidirectional relationships between additional falsehoods and corrections. As our results show evidence of heterogeneities in the responses (e.g., when controlling for bots), we understand that further heterogeneities can exist when considering falsehoods beyond the extreme events we have in our sample. As more data become available, government agencies and fact-checking organizations can use our proposed framework to learn more about the types of falsehoods and test the efectiveness of diferent corrections. They can fine-tune their correction messages and respond even more selectively than they currently do, depending on the nature of the falsehood and its potential to become viral. Being more selective may be the most eficient approach given the large volume, variety, and velocity of falsehoods (a characteristic of social media) and the diferences in the severity of falsehoods. Responding selectively can help establish and increase the issuer’s reputation, which in turn can further help the efectiveness of correction messages.

While the empirical results show that for our sample of falsehoods, government agencies and fact-checking organizations should not intervene as corrective tweets can spur more false tweets, we acknowledge that they might have additional objectives and priorities. However, we believe that selectively responding to falsehoods both in frequency and quality is the most efective approach.

## Conclusion and Limitations

We examine the bidirectional relationship between falsehoods and correction messages on social media. Our theoretical model and empirical evidence show the scenarios under which each type of message survives or dies of and their impacts on each other. Our study has several limitations. First, we had to aggregate our tweet data at the hourly level to obtain the counts, which may cause loss of information at the granular level. Second, we only analyzed tweets during two crisis events from two periods. Future studies can investigate other news stories from other social media platforms to cross-validate our results. Third, we only included verifiable false news and correction messages. Future studies may examine other types of news, such as rumors, urban legends, and conspiracy theories. Fourth, as a study on the dynamics between falsehoods and correction messages on social media, we examine their difusion at the hourly and topic levels. Studies have shown that cognitive and behavioral factors such as cognitive ability, expert sources, and clearly phrased messages afect the efectiveness of correction messages on falsehoods [9, 14, 55]. Future research can examine the issue at a more granular level and the impacts of factors such as user cognition, sentiment of the tweet, and source of the tweet using other research designs, such as surveys and experiments. Furthermore, future research may also investigate other factors that may contribute to the in/efectiveness of correction messages on falsehoods, such as message framing, timing of the correction message, tone, emotions and textual similarities between both falsehoods and correction messages. Fifth, even though we showed the bidirectional relationships between falsehoods and correction messages, we were unable to show why they happened. Future studies may employ surveys or experiments to examine why correction messages are inefective and identify the optimal timing to correct falsehoods. Finally, a full sensitivity analysis can be beneficial to understand the degrees of change of the quantitative outcomes of the model in response to slight changes in the parameters. While that analysis was partially done here for some parameters, it will be useful to rank those parameters influence on the quantitative and qualitative results of the model.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Notes on contributors

Kelvin King (kkking@syracuse.edu; corresponding author) is an Assistant Professor of Digital Misinformation at Syracuse University. His research leverages econometric models, machine learning algorithms as well as lab and field experiments and consists of two, often overlapping streams. The first stream focuses on information difusion and big data use, specifically misinformation. The second stream is at the intersection of behavioral economics and information decision-making in virtual communities. His research work has received several awards. Dr. King has industry experience working with big data.

Bin Wang (bin.wang@utrgv.edu) is the endowed Robert C. Vackar College of Business and Entrepreneurship Professor of Business and a Professor of Information Systems at the University of Texas Rio Grande Valley. Her research focuses on social media and social commerce, crowdfunding, electronic commerce, mobile commerce, IT adoption, and performance of IT-focused firms. Dr. Wang has published over forty refereed articles in such journals as the Journal of Management Information Systems, Information and Management, Information Systems Journal, Computers in Human Behavior, and others. She is a senior editor at Electronic Commerce Research and Applications and an associate editor at Journal of Electronic Commerce Research.

Diego Escobari (diego.escobari@utrgv.edu) is an Associate Professor of Economics in the Robert C. Vackar College of Business and Entrepreneurship at the University of Texas Rio Grande Valley. His research focuses on pricing, industrial organization, energy, and real estate markets. He has published over thirty articles in such journals as Journal of Industrial Economics, International Journal of Industrial Organization, Transportation Research Part A, Economics Letters, Energy Economics, Energy, and others.

Tamer Oraby (tamer.oraby@utrgv.edu) is an Associate Professor of Statistics and Mathematics in the School of Mathematical and Statistical Sciences at the University of Texas Rio Grande Valley.. His research interest is in mathematical and statistical modeling of spread of infectious diseases. He has published several papers in that domain in such journals as Lancet, Nature’s Scientific Reports, and Proceedings of the Royal Society B. Dr. Oraby has also a special interest in behavioral modeling of vaccine acceptance that resulted in published and in-progress papers, one of which was featured by health news. He has also published papers on chronic wasting disease, MERS-CoV, and COVID-19 including in Plos One. Dr. Oraby serves as an editorial board member of Nature’s Scientific Reports and Frontiers, Public Health.

## ORCID

Kelvin K. King http://orcid.org/0000-0002-8774-1148 Bin Wang http://orcid.org/0000-0002-4479-2500 Diego Escobari http://orcid.org/0000-0003-4532-8563 Tamer Oraby http://orcid.org/0000-0002-8176-1324

## References

1. Abrigo, M.R.M. and Love, I. Estimation of panel vector autoregression in Stata. The Stata Journal: Promoting Communications on Statistics and Stata, 16, 3 (September 2016), 778–804.

2. Adomavicius, G., Bockstedt, J., and Gupta, A. Modeling supply-side dynamics of IT components, products, and infrastructure: An empirical analysis using vector autoregression. Information Systems Research, 23, 2 (June 2012), 397–417.

3. Agrawal, M., Rao, H.R., and Oh, O. Community intelligence and social media services: A rumor theoretic analysis of tweets during social crises. MIS Quarterly, 37, 2 (February 2013), 407–426.

4. Allport, G.W. and Postman, L. An analysis of rumor. Public Opinion Quarterly, 10, 4 (Winter 1946), 501–517.

5. Andrews, D.W.K. and Lu, B. Consistent model and moment selection procedures for GMM estimation with application to dynamic panel data models. Journal of Econometrics, 101, 1 (March 2001), 123–164.

6. Bass, F.M. A new product growth for model consumer durables. Management Science, 15, 5 (January 1969), 215–227.

7. Berger, J. and Milkman, K.L. What makes online content viral? Journal of Marketing Research, 49, 2 (April 2012), 192–205.

8. Blei, D.M., Ng, A.Y., and Jordan, M.I. Latent Dirichlet Allocation. The Journal of Machine Learning Research, 3, (January 2003), 993–1022.

9. Bode, L. and Vraga, E.K. See something, say something: Correction of global health misinformation on social media. Health Communication, 33, 9 (September 2018), 1131–1140.

10. Cameron, K., Roof, M., Friesema, E., et al.Patient knowledge and recall of health information following exposure to “facts and myths” message format variations. Patient Education and Counseling, 92, 3 (September 2013), 381–387.

11. Choi, I. Unit root tests for panel data. Journal of International Money and Finance, 20, 2 (April 2001), 249–272.

12. Chua, A.Y.K., Tee, C.-Y., Pang, A., and Lim, E.-P. The retransmission of rumor and rumor correction messages on Twitter. American Behavioral Scientist, 61, 7 (June 2017), 707–723.

13. Davis, C.A., Varol, O., Ferrara, E., Flammini, A., and Menczer, F. BotOrNot: A system to evaluate social bots. In Proceedings of the 25th International Conference Companion on World Wide Web - WWW’16 Companion. ACM Press, Montreal, Quebec, Canada, 2016, pp. 273–274.

14. De Keersmaecker, J. and Roets, A. “Fake news”: Incorrect, but hard to correct. The role of cognitive ability on the impact of false information on social impressions. Intelligence, 65, (November 2017), 107–110.

15. Deng, S., Huang, Z.J., Zhao, H., and Sinha, A. The interaction between microblog sentiment and stock returns: An empirical examination. MIS Quarterly, 42, 3 (March 2018), 895–918.

16. Department of Homeland Security. Countering false information on social media in disasters and emergencies. 2018. https://www.dhs.gov/publication/st-frg-countering-false-informationsocial-media-disasters-and-emergencies .

17. Ecker, U.K.H., Lewandowsky, S., and Apai, J. Terrorists brought down the plane!—No, actually it was a technical fault: Processing corrections of emotive information. Experimental Psychology, 64, 2 (February 2011), 283–310.

18. Ecker, U.K.H., Lewandowsky, S., and Tang, D.T.W. Explicit warnings reduce but do not eliminate the continued influence of misinformation. Memory & Cognition, 38, 8 (December 2010), 1087–1100.

19. Friggeri, A., Adamic, L., Eckles, D., and Cheng, J. Rumor cascades. In Proceedings of the Eighth International AAAI Conference on Weblogs and Social Media. AAAI Publications, 2014, pp. 101–110.

20. Gause, G.F. Experimental studies on the struggle for existence. Journal of Experimental Biology, 9, 1 (April 1932), 389–402.

21. Gimpel, H., Heger, S., Olenberger, C., and Utz, L. The efectiveness of social norms in fighting fake news on social media. Journal of Management Information Systems, 38, 1 (January 2021), 196–221.

22. Glaeser, E. and Sunstein, C.R. Does more speech correct falsehoods? The Journal of Legal Studies, 43, 1 (January 2014), 65–93.

23. Hoekstra, M., Puller, S.L., and West, J. Cash for Corollas: When stimulus reduces spending. American Economic Journal: Applied Economics, 9, 3 (July 2017), 1–35.

24. Holtz-Eakin, D., Newey, W., and Rosen, H.S. Estimating vector autoregressions with panel data. Econometrica, 56, 6 (November 1988), 1371–1395.

25. Hovland, C. Reconciling conflicting results derived from experimental and survey studies of attitude change. American Psychologist, 14, 1 (1959), 8–17.

26. Huang, H. A war of (mis)Information: The political efects of rumors and rumor rebuttals in an authoritarian country. British Journal of Political Science, 47, 2 (April 2017), 283–311.

27. Itti, L. and Baldi, P. Bayesian surprise attracts human attention. Vision Research, 49, 10 (June 2009), 1295–1306.

28. Jindal, N., Liu, B., and Lim, E.-P. Finding unusual review patterns using unexpected rules. In Proceedings of the 19th ACM International Conference on Information and Knowledge Management - CIKM ’10. ACM Press, Toronto, ON, Canada, 2010, pp. 1549.

29. Jolley, D. and Douglas, K.M. The efects of anti-vaccine conspiracy theories on vaccination intentions. PLoS ONE, 9, 2 (February 2014), 1–9 e89177.

30. Kazienko, P. and Chawla, N. Applications of Social Media and Social Network Analysis. Springer, Cham, Switzerland, 2015.

31. Killins, R.N., Egly, P.V., and Escobari, D. The impact of oil shocks on the housing market: Evidence from Canada and U.S. Journal of Economics and Business, 93, (September 2017), 15–28.

32. Kim, A. and Dennis, A.R. Says Who? The efects of presentation format and source rating on fake news in social media. MIS Quarterly, 43, 3 (March 2019), 1025–1040.

33. Kim, A., Moravec, P.L., and Dennis, A.R. Combating fake news on social media with source ratings: The efects of user and expert reputation ratings. Journal of Management Information Systems, 36, 3 (July 2019), 931–968.

34. King, K. The gray side of fake news: A multiclass approach to detecting fake news, real news and everything else in between. In The 26th Americas Conference on Information Systems. , AIS Electronic Library, Utah 2020, pp. 1–10.

35. King, K., Wang, B., and Escobari, D. Efects of Sentiments on the morphing of falsehoods and correction messages on social media. In Proceedings of the 54th Hawaii International Conference on System Sciences. Hawaii, 2021, pp. 6563–6572.

36. King, K.K. and Sun, J. Catch bots with a bot: An automated approach to misinformation detection. In 4th International Conference on Design Science Research in Information Systems and Technology</i>. Springer, Worcester, MA, 2019, pp. 1–6.

37. Kumar, N., Venugopal, D., Qiu, L., and Kumar, S. Detecting review manipulation on online platforms with hierarchical supervised learning. Journal of Management Information Systems, 35, 1 (January 2018), 350–380.

38. Kwon, H.E., Oh, W., and Kim, T. Platform structures, homing preferences, and homophilous propensities in online social networks. Journal of Management Information Systems, 34, 3 (July 2017), 768–802.

39. Lakof, G., Dean, H., and Hazen, D. George Lakof -The Essential Guide for Progressives. Chelsea Green Publishing, White River Junction, Vermont, 2004.

40. Lewandowsky, S., Ecker, U.K.H., Seifert, C.M., Schwarz, N., and Cook, J. Misinformation and its correction: Continued influence and successful debiasing. Psychological Science in the Public Interest, 13, 3 (December 2012), 106–131.

41. Love, I. and Zicchino, L. Financial development and dynamic investment behavior: Evidence from panel VAR. The Quarterly Review of Economics and Finance, 46, 2 (May 2006), 190–210.

42. Luo, X., Zhang, J., and Duan, W. Social media and firm equity value. Information Systems Research, 24, 1 (March 2013), 146–163.

43. Ma, J., Gao, W., Mitra, P., et al. Detecting rumors from microblogs with recurrent neural networks. In Proceedings of the Twenty-Fifth International Joint Conference on Artificial Intelligence (IJCAI-16). New York, USA, 2016, pp. 3818–3824.

44. McGuire, W.J. Inducing resistance to persuasion. Some contemporary approaches. Advances in Experimental Social Psychology, 1, (1964), 191–229.

45. Moon, A. Most American adults get news from social media. Media and Telecoms, 2017. https://www.reuters.com/article/us-usa-internet-socialmedia-idUSKCN1BJ2A8 .

46. Oh, O., Kwon, K.H., and Rao, H.R. An exploration of social media in extreme events: Rumor theory and Twitter during the Haiti earthquake 2010. In the Thirty-First International Conference on Information Systems. AIS Electronic Library, St. Louis, Missouri, USA, 2010, pp. 1–13.

47. Oliver, J.E. and Wood, T.J. Conspiracy theories and the paranoid style(s) of mass opinion. American Journal of Political Science, 58, 4 (October 2014), 952–966.

48. Osatuyi, B. and Hughes, J. A tale of two internet news platforms-real vs. fake: An elaboration likelihood model perspective. In Proceedings of the 51st Hawaii International Conference on System Sciences. Hawaii, 2018, pp.3986–3994.

49. Ozturk, P., Li, H., and Sakamoto, Y. Combating rumor spread on social media: The efectiveness of refutation and warning. In Proceedings of the 48th Hawaii International Conference on System Sciences. IEEE, HI, USA, 2015, pp. 2406–2414.

50. Schwarz, N., Sanna, L.J., Skurnik, I., and Yoon, C. Metacognitive experiences and the intricacies of setting people straight: Implications for debiasing and public information campaigns. In Advances in Experimental Social Psychology. Elsevier, 2007, pp. 127–161.

51. Shin, J., Jian, L., Driscoll, K., and Bar, F. The difusion of misinformation on social media: Temporal pattern, message, and source. Computers in Human Behavior, 83, 6 (June 2018), 278–287.

52. Silverman, C. and Singer-Vine, J. Most Americans who see fake news believe it, new survey says. BuzzFeed News, 2016. https://www.buzzfeednews.com/article/craigsilverman/fake-newssurvey#.hjpN2eMqqg .

53. Sims, C.A. Macroeconomics and reality. Econometrica, 48, 1 (January 1980), 1–48.

54. Takayasu, M., Sato, K., Sano, Y., Yamada, K., Miura, W., and Takayasu, H. Rumor difusion and convergence during the 3.11 Earthquake: A Twitter case study. PLoS ONE, 10, 4 (April2015), 1–18 e0121443.

55. Torres, R.R., Gerhart, N., and Negahban, A. Combating fake news: An investigation of information verification behaviors on social networking sites. In The 51st Hawaii International Conference on System Sciences. Hawaii, 2018, pp. 3976–3985.

56. Tversky, A. and Kahneman, D. Rational choice and the framing of decisions. The Journal of Business, 59, 4 Part 2: The Behavioral Foundations of Economic Theory (October 1986), S251– S278.

57. Vosoughi, S., Roy, D., and Aral, S. The spread of true and false news online. Science, 359, 6380 (March 2018), 1146–1151.

58. Vraga, E.K. and Bode, L. Using expert sources to correct health misinformation in social media. Science Communication, 39, 5 (October 2017), 621–645.

59. Walter, N. and Murphy, S.T. How to unring the bell: A meta-analytic approach to correction of misinformation. Communication Monographs, 85, 3 (July 2018), 423–441.

60. Xitong Li and Lynn Wu. Herding and social media word-of-mouth: Evidence from Groupon. MIS Quarterly, 42, 4 (December 2018), 1331–1351.

61. Yoo, E., Gu, B., and Rabinovich, E. Difusion on social media platforms: A point process model for interaction among similar content. Journal of Management Information Systems, 36, 4 (October 2019), 1105–1141.
