---
otero_id: 28302
otero_key: "7KV2FZYF"
title: "How Is Mobile User Behavior Different? A Hidden Markov Model of Cross-Mobile Application Usage Dynamics"
authors: "Shaohui Wu; Yong Tan; Yubo Chen; Yitian (Sky) Liang"
year: "2022"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1093"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How Is Mobile User Behavior Different? A Hidden Markov Model of Cross-Mobile Application Usage Dynamics

Shaohui Wu,<sup>a,b</sup> Yong Tan,<sup>c</sup> Yubo Chen,<sup>d,</sup>\* Yitian (Sky) Liang<sup>d</sup>

<sup>a</sup> School of Management, Harbin Institute of Technology, Harbin 150080, China; <sup>b</sup> International Institute of Finance, School of Management, University of Science and Technology of China, Hefei 230026, China; <sup>c</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>d</sup> Department of Marketing, School of Economics and Management, Tsinghua University, Beijing 100084, China \*Corresponding author

Contact: wushaohui@hit.edu.cn (SW); ytan@uw.edu, https://orcid.org/0000-0001-8087-3423 (YT); chenyubo@sem.tsinghua.edu.cn, https://orcid.org/0000-0002-2322-2349 (YC); liangyt@sem.tsinghua.edu.cn, https://orcid.org/0000-0002-3091-4861 (Y(S)L)

Received: November 13, 2018 Revised: January 6, 2020; April 29, 2021; October 16, 2021 Accepted: November 14, 2021 Published Online in Articles in Advance: January 20, 2022

https://doi.org/10.1287/isre.2021.1093

Copyright: © 2022 INFORMS

Abstract. Mobile application use has become an essential activity in many people’s daily lives in the mobile Internet era. Driven by its ubiquity and strong context dependence, In ternet companies are in a race of cross-industry expansion to build a seamless ecosystem incorporating various contexts. Amid such trends, a better understanding of cross-app uses and the impact of contexts becomes critical and imperative. Yet, research on cross-app uses in information systems and marketing is scarce. In this paper, we aim to <sup>fi</sup>ll this gap. We develop a hidden Markov model to study cross-app uses (choice and duration), captur ing their interdependence and the impacts of contextual factors. We calibrate it using a consumer panel that contains real-time app use information. Our key <sup>fi</sup>ndings are as follows. (1) In addition to the utilitarian and hedonic states behind consumer decisions identi<sup>fi</sup>ed in prior literature, we uncover a novel social state behind mobile user behavior. App use behavior exhibits large differences across three states. (2) Within-state app interdependence is strongest in the hedonic state, followed by the social and utilitarian states. (3) Social state is the most transient (i.e., mostly likely to switch away), followed by the hedonic and utili tarian states. (4) Contextual factors—in particular, location and time of day—in<sup>fl</sup>uence the state dynamic. Compared with the intrinsic state transition, being at home or on the way (versus of<sup>fi</sup>ce) and in the morning or evening (versus night) leads to higher volatility. We discuss the managerial implications for a variety of mobile digital strategies.

History: D. J. Wu, Senior Editor; Vibhanshu Abhishek, Associate Editor.

Funding: This work was supported by the National Natural Science Foundation of China [Grants 71991461, 71902095, 91746302, 71532006, and 71325005], the China Ministry of Education Project for Key Research Institute of Humanities and Social Sciences in Universities [Grant 16JJD630006], and the Fundamental Research Funds for the Central Universities [WK2040000022] Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1093.

Keywords: econometrics economics of IS electronic commerce mobile computing mobile Internet

## 1. Introduction

With the increasing popularity of mobile technologies, we have collectively launched the era of mobile Internet, which is drastically changing our daily lives. A recent report reveals that there are more than 5.1 billion mobile Internet users around the world.<sup>1</sup> Mobile applications, or “apps,” greatly increase the functionalities of mobile devices beyond mere communication. The two dominant app platforms, Google Play and Apple App Store, provide more than 2 million apps for users to download. These countless apps rely on continuously developing mobile Internet technology to provide opportunities for people to meet their various use requirements including social, information, entertainment, shopping, and so on. According to an industry report,<sup>2</sup> there are about 45 apps on each smartphone, and 15 of them are used every day. On average, adults in the United States spend more than three hours on smartphones daily, and mobile app use accounts for more than 90% of the mobile time.<sup>3</sup> Mobile app use has become an indispensable everyday activity.

To create a seamlessly connected ecosystem for their users, today’s Internet companies are in a <sup>fi</sup>erce race of cross-industry expansions. Facebook, best known as a social media company, is expanding its businesses into entertainment and e-commerce.<sup>4</sup> Having tapped into several other areas such as entertainment, Amazon is no longer a mere e-commerce giant that started to get social networking involved recently.<sup>5</sup> Similarly, in the Chinese market, Tencent owns WeChat (one of the most widely used social apps in the world) and Tencent Games (one of the largest gaming companies in the world). Moreover, Tencent is the largest and a principal shareholder of JD.com and Pinduoduo, the two biggest e-commerce companies after Alibaba in China. Meanwhile, the e-commerce giant Alibaba is also building its own digital empire, covering entertainment, social, Fin Tech, online maps, and others.

One important reason for such strong cross-industry expansion is that mobile use, compared with personal computer (PC) use, is ubiquitous: consumers can access any mobile app at any time and place. For instance, a person may shop or chat with friends on her smartphone lying on the bed right before sleep or commuting to work. Such a feature implies that consumers can be exposed to a greater variety of contexts and use their fragmented free micromoments to access various mobile apps. Therefore, Internet giants strive their best to attract consumers’ attention within their own ecosystems under various contexts. As a result, they aggressively engage in the aforementioned contest of cross-industry expansion.

This poses great challenges to the management of mobile ecosystem because effective digital strategies, such as targeted advertising, personalized recommendation, search algorithm, and content design, rely on understanding the underlying mechanism of mobile uses not just within a certain app but across apps. For example, a user launching Facebook after using Amazon likely differs from after playing Angry Birds or reading the Wall Street Journal. Furthermore, such difference can depend on whether it is daytime or night and in the of<sup>fi</sup>ce or at home. Therefore, optimal digital strategies should take into account the interdependence of app uses and the impact of contexts.

Although there are existing studies examining app use (Zhang et al. 2019) and the impact of contexts (Luo et al. 2014, Fong et al. 2015), they all focus on within-app behavior. Surprisingly, cross-app interdependence and the in<sup>fl</sup>uence of contexts attract limited research. Two exceptions are Han et al. (2016), who examined the allocation of use time among mobile apps at the weekly level, and Zheng et al. (2019), who applied the graphical model to estimate the spillover effects of WeChat use on the top 50 most used apps. To our best knowledge, in information systems (IS) and marketing, there is no study investigating the underlying mechanism of cross-app uses and the impact of context at the real-time level, which is a natural analytical base for the nature of app interdependence given fragmented-time uses, contexts that typically change at the real-time level, and mobile digital strategies that typically rely on real-time data.

In this paper, we attempt to <sup>fi</sup>ll this gap by developing a model to capture the mechanism underlying the real-time uses across mobile apps and how it is affected by contexts. We collect a consumer panel data containing real-time app use information. We then develop our theoretical framework. Similar to that of Ding et al. (2015), we argue that consumers’ real-time mobile consumption is driven by their internal states, which may emerge from different antecedents such as daily routine, surrounding environment, economic incentives, and so on. Because of the ubiquity of mobile use, these internal states are potentially volatile, possibly driven by various contexts. We then develop a hidden Markov model (HMM) to capture the dynamic of internal states, cross-app use (choice and duration), and the in<sup>fl</sup>uence of contexts.

We focus on three contextual factors: time, location, and bandwidth. First, it is natural to investigate the effects of time and location because mobile use is ubiq uitous in both dimensions. Theoretically, consumers typically establish personal lifestyles and thus develop daily routines during different times of day (Bhat and Misra 1999, Luo et al. 2013). Prior studies show that such time factors have an impact on decision making (Yoon et al. 2007, Danziger et al. 2011). Therefore, we theorize that consumers may be in different internal states during different times of day. Second, prior literature shows that environmental cues have an impact on consumer behavior (Yang et al. 2002). Location—which is strongly associated with environmental cues—may thus in<sup>fl</sup>uence consumers’ internal states, which ultimately affects mobile use. Last, because many apps are designed to be used with Internet (Shin et al. 2012), bandwidth (WiFi versus cellular) becomes a potentially important factor. Speci<sup>fi</sup>cally, a cellular network, compared with WiFi, poses a use cost in terms of speed and an economic cost in terms of extra charge if the data exceed the cellular plan. Both costs may exert an impact on mobile use.

Our results show interesting <sup>fi</sup>ndings. First, in addition to utilitarian and hedonic states typically identi-<sup>fi</sup>ed by prior literature on PC use (Moe 2003), we uncover a third state behind mobile user behavior: social. App uses exhibit different patterns across states. In the utilitarian state, tool and information apps are most preferred, followed by social apps. In addition, users are most likely to stop mobile use in the utilitarian state than in other states. In the hedonic state, entertainment and social apps collectively take up a large share, followed by information apps. In the social state, social apps occupy more than 60% of the share, followed by entertainment. Among them, the hedonic state is the most prevalent (38.7%), followed by social (35.0%) and utilitarian (26.3%). Second, users show strong interdependence in app choices but not in use duration. Speci<sup>fi</sup>cally, users tend to use the same app category over use occasions at the expense of other categories. Such choice interdependence is strongest in the hedonic state, followed by the social and utilitarian states. Third, our result demonstrates interesting patterns of the state dynamic. For the intrinsic state transition, utilitarian is sticky (66% chance to stay), whereas social and hedonic are transient (56% and 45% chances of switching away, respectively). In addition, utilitarian and hedonic states are “twins” in that they typically switch to each other. Conversely, starting from the social state, the transition exhibits the pattern of a random walk. Fourth, for contextual factors, location and time of day have signi<sup>fi</sup>cant impacts on the state dynamic (versus intrinsic state transition), whereas the in<sup>fl</sup>uence of bandwidth is limited. Location, compared with of<sup>fi</sup>ce, home, or on-the-way, leads to a more volatile state dynamic. For time of day, the state dynamic is more volatile in the morning or evening. Last, past app use has a mild effect on the state dynamic.

Our results provide important managerial implications. In particular, we show that the HMM model is able to recover rich patterns of state evolution in the data through posterior analysis. Furthermore, we demonstrate that such important output of the model can be useful for a variety of mobile digital strategies. These include the design of search algorithm, personalized recommendation, targeted advertising, digital social strategy, app content preload, and app noti<sup>fi</sup>cation push, as well as app use improvement.

The main contributions of this paper are as follows. First, unlike existing research on mobile use and contextual marketing, which largely focuses on within-app behavior, we develop a framework to model cross-app uses. Such framework allows us to uncover a new social state behind mobile user behavior that is absent in prior studies of PC use. We show that it plays important roles in the mobile Internet era. It is prevalent, frequently intermitting between the utilitarian and hedonic states. Although social apps take up a large share, people still engage in other types of mobile activities in the social state. Together, these partially explain the cross-industry expansion phenomena mentioned earlier (e.g., Tencent’s holdings of JD.com and Pinduoduo). Second, our study identi<sup>fi</sup>es the mechanism of mobile user behavior under different contexts. We show that location and time of day signi<sup>fi</sup>cantly in<sup>fl</sup>uence the state dynamic. As a distinguished feature of mobile Internet, how various contexts affect cross-app behavior is still understudied. Answering this question helps us better understand how mobile user behavior differs from the PC Internet. Last but not least, we offer important managerial insights based on our framework of cross-app uses.

The rest of this paper is organized as follows. In Section 2, we review the relevant literature. We present data descriptions and descriptive statistics in Section 3. In Section 4, we propose an HMM for mobile cross-app uses. We discuss variable construction and estimation in Section 5. In Section 6, we present the estimation results and discuss managerial implications. We conclude and discuss limitations in Section 7.

## 2. Literature Review

In general, this paper is related to three streams of research in IS and marketing: consumer behavior in the PC Internet, mobile app use, and mobile contextual targeting.

A number of studies have investigated how people browse the PC Internet and the underlying mechanisms. Moe (2003) differentiated four patterns of PC Internet browsing, namely directed buying, search/ deliberation, hedonic browsing, and knowledge building. Montgomery et al. (2004) developed an HMM and identi<sup>fi</sup>ed two hidden states for PC Internet browsing: deliberation and browsing. Ding et al. (2015) found that online shopping cart choices are driven by two hidden states: low and high intent.

Recently, a number of studies investigated individuals’ mobile behavior from different perspectives. The most relevant study to this paper is Han et al. (2016), who proposed a structural model to understand mobile app use at an aggregate (weekly) level. This paper differs from theirs in two regards. First, we focus on a different level of cross-app use. Driven by the fragmented time use pattern, our analysis is at the realtime level. Second, we focus on the impact of context, which is a critical feature in the era of mobile Internet. Therefore, we contribute to this literature by complementing Han et al. (2016) with a study on real-time mobile cross-app use focusing on the impact of context. Another relevant study is Zhang et al. (2019), who proposed a structural HMM to study user engagement within a reading app. We differ from them by studying cross-app uses.

Recently, there are several studies on mobile contextual marketing. Luo et al. (2014) found that temporal and geographical targeting strategies are effective to drive up sales. Fang et al. (2015) showed that mobile purchases can be improved by location-based promotions. Fong et al. (2015) demonstrated that competitive locational targeting is effective. Phang et al. (2019) explored the ef<sup>fi</sup>cient match between information technology (IT) product and time of day. This paper differs from them by studying the impact of contexts on cross-app uses, which is largely neglected in this stream of literature.

## 3. Data and Descriptive Statistics 3.1. Data Description

Our data are provided by a leading Chinese market research <sup>fi</sup>rm. It is a panel containing mobile app use information of 717 users in Beijing over three weeks from October 6 to 26, 2014. The data contain time stamps of all app use for each user. It also contains the name of the location and bandwidth (WiFi versus 3G<sup>6</sup>) information for each use record.

Table 1. Descriptive Statistics

<table><tr><td></td><td>Numbers of observations</td><td>Percentage</td><td>Mean duration (min)</td><td>Standard deviation duration (min)</td></tr><tr><td>Social</td><td>102,278</td><td>0.446</td><td>3.48</td><td>12.08</td></tr><tr><td>Information</td><td>31,356</td><td>0.137</td><td>5.53</td><td>15.88</td></tr><tr><td>Entertainment</td><td>53,102</td><td>0.232</td><td>4.18</td><td>12.64</td></tr><tr><td>Shopping</td><td>12,425</td><td>0.054</td><td>1.76</td><td>9.50</td></tr><tr><td>Tool</td><td>30,160</td><td>0.131</td><td>3.66</td><td>13.29</td></tr></table>

There are <sup>fi</sup>ve app categories classi<sup>fi</sup>ed by the <sup>fi</sup>rm: social, information, entertainment, shopping, and tools. Social apps include WeChat, QQ, and so on.<sup>7</sup> Information apps include news, browser apps, and so on. Entertainment apps mainly include music, video, and gaming apps. Shopping apps include several business-to-customer (B2C) and customer-to-customer (C2C) apps. Tool apps include note, map, and weather apps. Following the literature (Montgomery et al. 2004, Ding et al. 2015), we divide app use into sessions. Intuitively, each session is a period of continued app use. If two consecutive app uses occur within 20 minutes, we assume they are in one session.<sup>8</sup> Otherwise, the <sup>fi</sup>rst app use marks the end of the current session and the second one marks the beginning of a new session. Within a session s, we de<sup>fi</sup>ne an app use incidence as an occasion, denoted by t. During each occasion, users select an app from the <sup>fi</sup>ve categories or to stop the current session (i.e., outside option). An observation in our analysis is an occasion. The data contain 717 users, 64,872 sessions, and 268,337 use occasions. We randomly choose 100 users as the holdout sample to test the predictive ability of the proposed model. All subsequent analyses are performed on the calibration sample that includes 617 users, 55,589 sessions, and 229,321 use occasions.

## 3.2. Summary Statistics

Table 1 reports summary statistics of use frequency and duration. Social apps have the largest share (45%), followed by entertainment (23%). The shares of information (14%) and tool (13%) apps are close to each other. Shopping apps (5%) have the smallest share. In terms of duration, the top two categories are information and entertainment, whereas shopping is at the bottom. This suggests users use social apps most frequently. Interestingly, although mobile shop ping has been growing continuously in recent years, it is not used as frequently as other apps and is used with the shortest duration.

Table 2. Distribution of Number of App Uses Within a Session

<table><tr><td>Number of app uses</td><td>Percentage</td></tr><tr><td>1</td><td>40.07%</td></tr><tr><td>2</td><td>18.46%</td></tr><tr><td>3</td><td>10.57%</td></tr><tr><td>4</td><td>6.79%</td></tr><tr><td>5</td><td>4.86%</td></tr><tr><td>6</td><td>3.45%</td></tr><tr><td>7</td><td>2.44%</td></tr><tr><td>8</td><td>2.02%</td></tr><tr><td>9</td><td>1.58%</td></tr><tr><td>≥10</td><td>9.76%</td></tr></table>

Tables 2 and 3 show summary statistics at the session level. Table 2 shows the distribution of number of app uses within a session. Many sessions are short, with roughly 70% having no more than three app uses. Meanwhile, many sessions are long, with about 10% having more than 10 app uses. Table 3 illustrates the distribution of unique app categories within a session. Overall, use is relatively concentrated in that roughly 98% of all sessions contain no more than three app categories, although many sessions contain more than three individual app uses.

We further examine choices of app category at the start of a session and how they switch among each other within the session in Tables 4 and 5. The results show that users are most likely to use social apps at the start of a session, and they are the stickiest. In addition, users are most likely to switch to social apps from other app categories. These suggest social is a critical component in the era of mobile Internet. We also calculate the probability of switching to the outside option “stop.” Overall, they are relatively close to each other (about 25%) for the <sup>fi</sup>ve app categories.

We then examine use patterns across different contextual factors. We <sup>fi</sup>rst examine time of day in Figure 1. It shows that mobile activity is largely consistent with a person’s normal daily life: high during daytime and low during night. In terms of share, most app categories are stable during daytime, but at night, social decreases, whereas information, tool, and shopping increase. Interestingly, for duration, users have the longest app use time at night. This may be because of self-selection, that is, those prefer staying up late at night to use mobile phone tend to spend more time on mobile apps in general.

Table 3. Distribution of Unique App Categories at the Session Level

<table><tr><td>Number of unique app categories</td><td>Number of sessions</td><td>Percentage</td></tr><tr><td>1</td><td>34,116</td><td>0.614</td></tr><tr><td>2</td><td>15,096</td><td>0.271</td></tr><tr><td>3</td><td>5,051</td><td>0.091</td></tr><tr><td>4</td><td>1,213</td><td>0.022</td></tr><tr><td>5</td><td>113</td><td>0.002</td></tr></table>

Table 4. Initial Use Distribution

<table><tr><td></td><td>Social</td><td>Information</td><td>Entertainment</td><td>Shopping</td><td>Tool</td></tr><tr><td>Frequency</td><td>25,280</td><td>8,231</td><td>11,783</td><td>3,036</td><td>7,259</td></tr><tr><td>Percentage</td><td>45.47%</td><td>14.81%</td><td>21.20%</td><td>5.46%</td><td>13.06%</td></tr></table>

Next, we examine uses across bandwidths (WiFi versus 3G) and locations (home, of<sup>fi</sup>ce, on the way) in Tables 6 and 7. First, consistent with our expectation, use is more frequent under WiFi than 3G. The shares among <sup>fi</sup>ve categories are largely consistent in 3G and WiFi except that the share of information is lower in 3G by around one-fourth. Interestingly, information apps are used longer in 3G than WiFi by 18%. This suggests that information seeking is sensitive to cost because of extra data fees and/or lower speeds. However, once people start to use information apps, they tend to spend more time, possibly driven by user heterogeneity and/or idiosyncratic shocks. For location, home is where app use is most frequent, whereas the of<sup>fi</sup>ce has the lowest frequency. The average durations for social, entertainment, and tool apps are the longest at home, whereas those for information and shopping apps are the shortest on the way.

## 4. Model

## 4.1. Theoretical Background

Our study uses a stimulus-organism-response (S-O-R) framework from previous environmental psychology and marketing literature (Donovan and Rossiter 1982). We posit that users’ app use (R) is driven by their internal states (O), which are not constant over time, and their dynamics are in<sup>fl</sup>uenced by contextual factors (S). Studies have shown that online environmental stimuli could affect users’ internal states, prompting approach and avoidance behaviors (Ding et al. 2015). There are also studies showing physical environmental stimulus can affect consumers’ emotional states, leading to different in-store behavior (Donovan and Rossiter 1982, Bitner 1992). Others examine the impact of retail atmospheric cues on consumer responses based on the S-O-R framework (Mattila and Wirtz 2001, Spangenberg et al. 2005).

There is a large amount of literature exploring the nature of internal states (Goldberg and Gorn 1987, Babin et al. 1994, Voss et al. 2003, Brown and Venkatesh 2005, Chitturi et al. 2008, Botti and McGill 2010). These studies illustrate two main types of underlying needs driving consumer decisions. One is task related and rational, namely utilitarian. The other is mainly about entertainment and emotional needs, namely hedonic. As shown earlier, social apps account for a large share of mobile use, suggesting there is an additional social state that is about the need for social activities. It potentially plays an important role in the era of mobile Internet. In addition, these internal states are possibly volatile over time and are subject to contextual factors such as time, location, and bandwidth. As discussed earlier, consumers typically develop daily habitual routines across times of a day (Bhat and Misra 1999), suggesting their internal states also follow a certain pattern throughout a day. Consumers’ internal states are also related to their cognitive capacity by nature. Meanwhile, past research has shown that cognitive capacity could be affected by time constraints (Chaiken et al. 1989, Park et al. 1989, Suri and Monroe 2003) that typically vary across geographical locations (Collins et al. 2016, Sedani et al. 2019) and the use of the Internet (Small et al. 2009, Park et al. 2011, Hadlington 2015). We thus expect these contextual factors could be impactful on the dynamic of these internal states.

Our objective is to develop a framework that captures the impact of users’ internal states on app use and the impact of contexts. Because these internal states are inherently unobservable to researchers, we propose a HMM that integrates the dynamic processes of both internal state transitions and cross-app use. HMM has been widely used in IS and marketing (Netzer et al. 2008; Singh et al. 2011, 2014; Yan and Tan 2014). We allow these two processes to depend on contexts. Based on app use data, we uncover the hidden states, how users behave in each state, and the impact of contextual factors.

## 4.2. Model Development

We assume a <sup>fi</sup>nite number (n) of hidden states that cannot be directly observed. All else being equal, each state leads to a unique app use pattern. At any given point of time, a user resides in only one state. Users can switch from one state to another. Figure 2 illustrates the transitions among states and withinstate app use decisions for a user within a session. Let $J _ { i s t } = \{ 1 , 2 , \ldots , n \}$ be the set of possible hidden states for user i in occasion t of session $s ,$ and $B _ { i s t }$ be the set of app use behavior. The model is composed of three elements. (1) The initial state distribution $\pi \left( n \times 1 \right.$ vector). Each element in π represents the probability of the state at the start of the session. (2) The $n \times n$ statetransition probability matrix Q. (3) App use behavior B contains two parts: app choices and use time (conditional on app choice). The choice probabilities are captured by the $n \times ( M + 1 )$ matrix $B ^ { c } ,$ where M is the number of app categories. Elements in $B ^ { c }$ represent the probabilities of choosing each app category in each state, including the probabilities of stopping the current session.<sup>9</sup> We model duration conditional on app choice, which is captured by the $n \times M$ matrix $B ^ { d }$ Element $B _ { j m } ^ { d }$ is the expected use time for app category m in state $j ,$ conditional the user choosing app category m. We assume that the matrices B<sup>c</sup> and ${ \bar { B ^ { d } } } _ { }$ are governed by a distribution that is parameterized by $\Theta _ { B }$

Table 5. Switching Matrix Among App Categories and Outside Option Stop

<table><tr><td> $t \rightarrow t + 1$ </td><td>Social</td><td>Information</td><td>Entertainment</td><td>Shopping</td><td>Tool</td><td>Stop</td></tr><tr><td>Social</td><td>49.79%</td><td>7.50%</td><td>10.20%</td><td>2.45%</td><td>6.14%</td><td>23.92%</td></tr><tr><td>Information</td><td>23.32%</td><td>31.65%</td><td>8.42%</td><td>2.41%</td><td>6.62%</td><td>27.58%</td></tr><tr><td>Entertainment</td><td>19.03%</td><td>4.74%</td><td>45.82%</td><td>2.64%</td><td>4.61%</td><td>23.16%</td></tr><tr><td>Shopping</td><td>19.33%</td><td>6.37%</td><td>11.24%</td><td>32.56%</td><td>5.68%</td><td>24.82%</td></tr><tr><td>Tool</td><td>20.74%</td><td>7.39%</td><td>8.35%</td><td>2.27%</td><td>37.77%</td><td>23.48%</td></tr></table>

Figure 1. (Color online) App Use Across Time of Day  
![](/api/attachments/7KV2FZYF/fulltext/images/e1dee358a5e951ac39a8325822152531e353b243c95c5f7538a67e5385031e10.jpg)

![](/api/attachments/7KV2FZYF/fulltext/images/5507a6b6a819605fc83f6b0f0502b8ca6667acc71352d5a0a80aa73a7c23590f.jpg)

An HMM requires the speci<sup>fi</sup>cation of n (number of states) and the three components $( \pi , \ Q , \ B )$ . For convenience, we use the following compact notation, $\lambda = \left( \pi , \ Q , \Theta _ { B } \right)$ , to represent the set of parameters of the model. For user i in session $s ,$ there are two sequences: (1) an unobserved state sequence $J _ { i s } = J _ { i s 1 } J _ { i s 2 }$ $\cdots J _ { i s T }$ and (2) an observed outcome sequence $B _ { i s } =$ $B _ { i s 1 } B _ { i s 2 } . . . B _ { i s T }$ . The probability that we observe the outcome sequence $B _ { i s }$ given the state sequence $J _ { i s }$ and the parameter λ is

![](/api/attachments/7KV2FZYF/fulltext/images/b1a3774409c328ba6b7f2843e21ab88e3d029a981e2f73722622c3276e977694.jpg)  
Table 6. Summary of App Use Frequency Across Bandwidths and Location

$$
P (B _ {i s} | \lambda , J _ {i s}) = \prod_ {t = 1} ^ {T} P (B _ {i s t} | \lambda , J _ {i s t}),\tag{1}
$$

where $P ( B _ { i s t } | \lambda , J _ { i s t } )$ is the probability of the observed app choices and durations given that user i is in state $J _ { i s t }$ of occasion t during session s. The probability of a state sequence $J _ { i s }$ is given by

$$
P (J _ {i s} | \lambda) = \pi (i s) q _ {i s} (J _ {i s 1}, J _ {i s 2}) \dots q _ {i s} (J _ {i s t}, J _ {i s t + 1}) \dots q _ {i s t} (J _ {i s T}, J _ {i s T}),\tag{2}
$$

where $\pi ( i s )$ is the initial probability that user i is in state $J _ { i s 1 }$ in occasion t 1 of session s; $q _ { i s t } ( J _ { i s t } ,  J _ { i s t + 1 } ) .$ , an element of $Q ,$ is the probability that user i will be in state $J _ { i s t + 1 }$ in occasion t 1 given that she is in state $J _ { i s t }$ in occasion t of session s. The joint probability of $B _ { i s }$

<table><tr><td colspan="2">Context</td><td>Social</td><td>Information</td><td>Entertainment</td><td>Shopping</td><td>Tool</td><td>Stop</td><td>Total</td></tr><tr><td rowspan="2">Bandwidth</td><td>WiFi</td><td>59,443(35.65%)</td><td>20,632(12.37%)</td><td>30,174(18.09%)</td><td>6,577(3.94%)</td><td>17,142(10.28%)</td><td>32,798(19.67%)</td><td>166,766(100%)</td></tr><tr><td>3G</td><td>42,835(36.25%)</td><td>10,724(9.08%)</td><td>22,928(19.41%)</td><td>5,848(4.95%)</td><td>13,018(11.02%)</td><td>22,791(19.29%)</td><td>118,144(100%)</td></tr><tr><td rowspan="3">Location</td><td>Home</td><td>68,291(35.31%)</td><td>21,939(11.34%)</td><td>36,876(19.07%)</td><td>8,475(4.38%)</td><td>20,330(10.51%)</td><td>37,499(19.39%)</td><td>193,410(100%)</td></tr><tr><td>Office</td><td>15,396(38.08%)</td><td>4,030(9.97%)</td><td>6,786(16.78%)</td><td>1,893(4.68%)</td><td>3,928(9.71%)</td><td>8,401(20.78%)</td><td>40,434(100%)</td></tr><tr><td>Way</td><td>18,591(36.40%)</td><td>5,387(10.55%)</td><td>9,440(18.49%)</td><td>2,057(4.03%)</td><td>5,902(11.56%)</td><td>9,689(18.97%)</td><td>51,066(100%)</td></tr></table>

Table 7. Summary of App Use Duration (Minutes) Across Bandwidths and Locations

<table><tr><td rowspan="3"></td><td colspan="6">Location</td><td colspan="4">Bandwidth</td></tr><tr><td colspan="2">Home</td><td colspan="2">Office</td><td colspan="2">Way</td><td colspan="2">WiFi</td><td colspan="2">3G</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Social</td><td>3.60</td><td>12.63</td><td>3.38</td><td>11.07</td><td>3.17</td><td>10.77</td><td>3.64</td><td>12.64</td><td>3.27</td><td>11.26</td></tr><tr><td>Information</td><td>5.40</td><td>15.88</td><td>6.32</td><td>17.16</td><td>5.48</td><td>14.86</td><td>5.22</td><td>15.45</td><td>6.14</td><td>16.66</td></tr><tr><td>Entertainment</td><td>4.46</td><td>13.19</td><td>3.76</td><td>11.46</td><td>3.41</td><td>11.08</td><td>4.61</td><td>13.59</td><td>3.63</td><td>11.23</td></tr><tr><td>Shopping</td><td>1.77</td><td>9.18</td><td>2.07</td><td>11.66</td><td>1.47</td><td>8.53</td><td>2.49</td><td>11.37</td><td>0.95</td><td>6.73</td></tr><tr><td>Tool</td><td>3.75</td><td>14.00</td><td>3.50</td><td>11.47</td><td>3.43</td><td>11.85</td><td>3.35</td><td>12.65</td><td>4.06</td><td>14.08</td></tr></table>

and $J _ { i s }$ is

$$
P (B _ {i s}, J _ {i s} | \lambda) = P (B _ {i s} | \lambda , J _ {i s}) P (J _ {i s} | \lambda).\tag{3}
$$

Hence, the probability of the observed app use sequence $B _ { i s }$ given the model parameter λ is the integration of Equation (3) over all possible state sequences $J _ { i s }$ (Rabiner 1989):

$$
L (B _ {i s}) = P (B _ {i s} \mid \lambda) = \sum_ {\forall J _ {i s}} P (B _ {i s} \mid \lambda , J _ {i s}) P (J _ {i s} \mid \lambda).\tag{4}
$$

According to MacDonald and Zucchini (1997), the individual likelihood can be written as

$$
\begin{array}{r} L (B _ {i s}) = \pi (i s) \Lambda (i s, 1) Q (i s, 1, 2) \Lambda (i s, 2) \\ \dots Q (i s, p - 1, p) \Lambda (i s, T) \mathbf {1} ^ {\prime}, \end{array}\tag{5}
$$

where, matrix $\Lambda ( i s , t ) = d i a g ( P ( O _ { i s t } \mid J _ { i s t } = 1 ) , P ( B _ { i s t } \mid J _ { i s t } = 2 ) .$ $\dots , P ( B _ { i s t } \mid J _ { i s t } = n ) )$ , and $\mathbf { 1 } ^ { \bar { \prime } }$ is a n 1 vector of ones. In the following sections, we specify the state transition, state-dependent choice and duration, and the likelihood.

4.2.1. State Transition. The state-transition probability is de<sup>fi</sup>ned as $Q _ { i s t } = \{ q _ { i s t } ( j , k ) \}$ , where

$$
q _ {i s t} (j, k) = P (J _ {i s t + 1} = k \mid J _ {i s t} = j),
$$

that ${ \mathrm { i } } s ,$ the probability that user i transits from state j in occasion t to state k in occasion $t + 1$ of session s. For each state $j ,$ we have $\begin{array} { r } { \sum _ { k = 1 } ^ { n } q _ { i s t } ( j , k ) = 1 } \end{array}$ and $0 \leq q _ { i s t } ( j , k ) \leq 1$ . We model the transition probability as a function of contextual and other variables that will be discussed later. State transitions are also affected by unobserved idiosyncratic factors. We adopt the multinomial Logit for state transition probabilities:

$$
q _ {i s t} (j, k) = \frac {e x p (\mu_ {j k} - \gamma_ {j} A _ {i s t} - \xi_ {i})}{1 + \sum_ {k \neq j} e x p (\mu_ {j k} - \gamma_ {j} A _ {i s t} - \xi_ {i})},\tag{6}
$$

$$
q _ {i s t} (j, j) = \frac {1}{1 + \sum_ {k \neq j} e x p (\mu_ {j k} - \gamma_ {j} A _ {i s t} - \xi_ {i})}.\tag{7}
$$

Here, j is the current state, and k is the targeting state at the next occasion; $\mu _ { j k }$ is the intrinsic value for switching from state j to state $k , A _ { i s t }$ is a vector of observed variables, and parameter $\gamma _ { j }$ measures the impact of these variables in current state j. We also allow the state transition to depend on user unobserved heterogeneity, which is captured by the random effect $\xi _ { i }$ .

4.2.2. State-Dependent App Choice and Use Duration. We model the joint decisions of app choice and use duration following Abhishek et al. (2013). We adopt the Logit model for the probability of user i choosing app category v in occasion t of session s:

Figure 2. HMM of Mobile App Use Dynamics  
![](/api/attachments/7KV2FZYF/fulltext/images/fb9cf8ec2123dc16d6813c11e10c6920b17977afca5202ac329fcd27d37eb524.jpg)

$$
P (O _ {i s t} = v \mid S _ {i s t} = j) = \frac {e x p (\alpha_ {j v} - \beta_ {j v} X _ {i s t} - \eta_ {i})}{1 + \sum_ {v ^ {\prime} = 1} ^ {M} e x p (\alpha_ {j v ^ {\prime}} - \beta_ {j v ^ {\prime}} X _ {i s t} - \eta_ {i})},\tag{8}
$$

where $\alpha _ { j v }$ is the intrinsic value for app category v in state j. The vector $X _ { i s t }$ includes variables that in<sup>fl</sup>uence users’ app choices, which will be discussed later. The term $\beta _ { j v } ,$ which is state and app category dependent, represents the effects of these variables. The user unobserved heterogeneity for app choices is captured by the random effect $\eta _ { i }$ . For identi<sup>fi</sup>cation, we normalize the utility of the outside option “stop” to be zero.

Conditional on choosing app category v in occasion t of session s, we model use duration as exponentially distributed (Ding et al. 2015). Speci<sup>fi</sup>cally, the conditional density of use duration is

$$
f _ {i s} (\triangle t \mid B _ {i s t} ^ {c} = v, J _ {i s t} = j) = \theta_ {i s t v j} \cdot e ^ {- \theta_ {i s t v j} \cdot \triangle t},\tag{9}
$$

where $\theta _ { i s t v j } = e ^ { \delta _ { j v } \cdot Y _ { i s t } - \tau _ { i } }$ and $Y _ { i s t }$ are the variables (including a constant term, i.e., the intrinsic value) that affect use duration, which will be discussed later, and $\delta _ { j v }$ is the associated vector of coef<sup>fi</sup>cients. The user unobserved heterogeneity for app use duration is captured by the random effect $\tau _ { i } .$

4.2.3. Likelihood. Conditional on the random effects, the likelihood of observing a sequence of outcomes $B _ { i s } = B _ { i s 1 } B _ { i s 2 } . . . B _ { i s T }$ is the sum over all possible state

sequences:

$$
\begin{array}{l} L (B (i s) \mid \eta , \xi , \tau) = \sum_ {j _ {1} = 1} ^ {n} \sum_ {j _ {2} = 1} ^ {n} \dots \sum_ {j _ {T} = 1} ^ {n} P (J _ {i s 1} = j _ {1}) \prod_ {t = 2} ^ {T} P (J _ {i s t} = j _ {t} \\ \quad | J _ {i s t - 1} = j _ {t - 1}) \prod_ {t = 1} ^ {T} P (B _ {i s t} \mid J _ {i s t} = j _ {\mathrm{t}}). \end{array} \tag {10}
$$

The probability of the outcomes in each occasion is the production of the probability of app choice and app duration, that is, $\begin{array} { r } { P ( B _ { i s t } \mid \bar { J } _ { i s t } = j _ { t } ) \bar { \ = } \ } \end{array}$ $\frac { e x p ( \alpha _ { j v } - \beta _ { j v } X _ { i s t } - \eta _ { i } ) } { 1 + \sum _ { v ^ { \prime } = 1 } ^ { M } e x p ( \alpha _ { j v ^ { \prime } } - \beta _ { j v ^ { \prime } } X _ { i s t } - \eta _ { i } ) } \cdot \theta _ { i s t v j } \cdot e ^ { - \theta _ { i s t v j ^ { \ast } } \triangle t }$ . Thus, the likelihood for user i can be obtained by integrating over $\eta , \xi ,$ , and τ:

$$
L (B (i)) = \int_ {\eta} \int_ {\xi} \int_ {\tau} L (B (i) \mid , \eta , \xi , \tau) d G (\eta) d H (\xi) d K (\tau),\tag{11}
$$

where $G , H ,$ and K are the corresponding distributions of the random effects.

## 5. Variable Construction and Model Estimation

## 5.1. Variable Construction

Table 8 shows four sets of variables, contextual variables C, app use duration variables D, app use frequency variables F, and other control variables O. In all analyses, we take log transformation (e.g., log 1  x ) of all continuous variables in Table 8 to capture possible nonlinear effect and to stabilize the estimation process. The contextual variables C contains time, location, and bandwidth. For time, we use night (2300 to 0500 hours the next day) as the baseline in the model. For locations, we classify them as: home, office, and on the way. We use office as the baseline.<sup>10</sup> For bandwidth, we use 3G as the baseline. To capture app interdependence, we let F and D be the sets of within-session cumulative app use frequencies and durations before the current occasion, broken down by app categories. In addition, in set O, we control for time trends with day-of-week and calendar week. To further control for the effect of previous use, we include the time interval since the last app use before the current occasion.

Table 8. Variable De<sup>fi</sup>nition

<table><tr><td></td><td>Variable</td><td>Definition</td></tr><tr><td rowspan="6">Contextual variable C</td><td>Morning</td><td>Dummy variable equals one if between 5 a.m. and 9 a.m. and zero otherwise</td></tr><tr><td>Day</td><td>Dummy variable equals one if between 9 a.m. and 6 p.m. and zero otherwise</td></tr><tr><td>Evening</td><td>Dummy variable equals one if between 6 p.m. and 11 p.m. and zero otherwise</td></tr><tr><td>WiFi</td><td>Dummy variable equals one if WiFi is connected and zero otherwise</td></tr><tr><td>Home</td><td>Dummy variable equals one if at home and zero otherwise</td></tr><tr><td>On the Way</td><td>Dummy variable equals one if on the way and zero otherwise</td></tr><tr><td rowspan="5">Use duration variable D</td><td>TSocial</td><td>The cumulative use time of social apps before this occasion in this session</td></tr><tr><td>TInfo</td><td>The cumulative use time of information apps before this occasion in this session</td></tr><tr><td>Tent</td><td>The cumulative use time of entertainment apps before this occasion in this session</td></tr><tr><td>Tshop</td><td>The cumulative use time of shopping apps before this occasion in this session</td></tr><tr><td>TTool</td><td>The cumulative use time of tool apps before this occasion in this session</td></tr><tr><td rowspan="5">Use frequency variable F</td><td>NumSocial</td><td>The cumulative number of social apps uses before this occasion in this session</td></tr><tr><td>NumInfo</td><td>The cumulative number of information apps uses before this occasion in this session</td></tr><tr><td>NumEnt</td><td>The cumulative number of entertainment apps uses before this occasion in this session</td></tr><tr><td>NumShop</td><td>The cumulative number of shopping apps uses before this occasion in this session</td></tr><tr><td>NumTool</td><td>The cumulative number of tool apps uses before this occasion in this session</td></tr><tr><td rowspan="8">Other control variables O</td><td>Week_k</td><td>Dummy variable equals one if in the kth week and zero otherwise</td></tr><tr><td>Mon</td><td>Dummy variable equals one if on Monday</td></tr><tr><td>Tues</td><td>Dummy variable equals one if on Tuesday</td></tr><tr><td>Wed</td><td>Dummy variable equals one if on Wednesday</td></tr><tr><td>Thur</td><td>Dummy variable equals one if on Thursday</td></tr><tr><td>Fri</td><td>Dummy variable equals one if on Friday</td></tr><tr><td>Sat</td><td>Dummy variable equals one if on Saturday</td></tr><tr><td>Tinterval</td><td>Time since the last app use before this occasion in this session</td></tr></table>

Table 9. Model Selection

<table><tr><td>Number of states</td><td>Log-likelihood</td><td>Variables</td><td>BIC</td></tr><tr><td>2</td><td>-346,202.3</td><td>578</td><td>-349,832.1</td></tr><tr><td>3</td><td>-338,271.0</td><td>867</td><td>-343,715.7</td></tr><tr><td>4</td><td>-337,207.2</td><td>1158</td><td>-344,479.4</td></tr></table>

We allow all three processes (i.e., state transition, state-dependent choice, and duration) depend on all four sets of variables. For contextual factors, as discussed extensively earlier, they might affect app use indirectly by in<sup>fl</sup>uencing a user’s internal state via daily routine and environmental cues, and so on. Meanwhile, they could also have a direct impact on app use. For example, one might naturally seek for work-related information or use work-related tool apps while in the of-<sup>fi</sup>ce. For past use, it might directly affect the current use. For example, a user may choose the social app at the current occasion simply because of an un<sup>fi</sup>nished conversation with friends a few minutes ago. At the same time, past use may also in<sup>fl</sup>uence the current use indirectly through its impact on the state transition. For example, past use may lead to state-stickiness because of inertia or state switches because of saturation.<sup>11</sup> Our modeling strategy aims to take these possible effects into consideration <sup>fl</sup>exibly.

## 5.2. Model Estimation

Similar to Yan and Tan (2014), we start with a <sup>fi</sup>nite mixture model to estimate the initial distribution for the hidden states and then use Maximum Likelihood Estimation to estimate the model parameters. For user heterogeneity, we follow the approach by Heckman and Singer (1984). The approximation process for the unknown probability distribution was evaluated by <sup>fi</sup>- nite sampled supporting points associated with probability mass distributions. The number of states n was chosen according to Bayesian information criterion (BIC): $B I C = l n L - k \times \bar { l n } P / 2 .$ , where P is sample size, L is the likelihood of the model, and k is the number of parameters.<sup>12</sup> Table 9 indicates that the three-state model outperforms others.

## 6. Results and Managerial Implication

In this section, we report the results from the proposed HMM with three hidden states. The initial state distribution is (0.263, 0.350, 0.387). In what follows, we <sup>fi</sup>rst discuss the interpretation and critical features for each state and then examine app interdependence within each state, followed by an examination of state transition. Last, we discuss the managerial implications.

## 6.1. Interpretation of States

Following Singh et al. (2014), we <sup>fi</sup>rst explore the pattern of app choices in each hidden state. Based on this, we interpret their meanings and assign labels. We plot the intrinsic shares<sup>13</sup> in Figure 3. Overall, it shows that the distributions of app choices differ across the three states, suggesting that users do behave differently when they are in different states. Speci<sup>fi</sup>cally, in state 1, the shares are greater for tools (35.72%) and information (27.55%), followed by social (24.90%), and the others are relatively low (8.81% for entertainment and 3.02% for shopping). Because tool and information apps typically represent functional needs, we label state 1 as the utilitarian state. In state 2, the share of social apps is greater than 60%, followed by entertainment (25.60%).<sup>14</sup> We therefore label state 2 as the social state. In the social state, users’ preferences are mainly tilted toward social apps. In state 3, the shares are concentrated in entertainment (41.12%) and social (36.05%) apps, whereas the others are comparatively low (13.15% for information, 3.76% for shopping, and 5.92% for tool). Because many social activities (e.g., chatting and browsing friends’ activity feeds) can also be perceived as relaxing/leisure activities (Sledgianowski and Kulviwat 2009), we label state 3 as the hedonic state. In the hedonic state, users mainly seek for relaxation/entertainment mobile activities.

Figure 3. (Color online) Intrinsic Share and Duration for Each App Category in Each State  
![](/api/attachments/7KV2FZYF/fulltext/images/7d25b98b59ba369fdfd569a9565d2832fe563e58a61c0e475f094e2b5387b8d8.jpg)

![](/api/attachments/7KV2FZYF/fulltext/images/2d6e26a792861872c64b0a21527207b7f69a4634688e87df1453be5a3c444bc9.jpg)

We also plot the intrinsic use duration in Figure 3, which shows similar pattern as the intrinsic share. Speci<sup>fi</sup>cally, for the most frequently used apps in each state, they are also used for longer. In addition, we also <sup>fi</sup>nd interesting results for the impact of day of week as reported in the online appendix. Speci<sup>fi</sup>- cally, when users are in the utilitarian state, conditional on choosing entertainment or shopping app, they tend to consume shorter duration during weekdays (versus weekend) possibly because of a work schedule.

In sum, our estimation result suggests that in addition to the typical utilitarian and hedonic states identi<sup>fi</sup>ed in prior studies, a social state plays a key role in mobile use. Furthermore, our results indicate that social apps are not the exclusive choice reserved for the social state: they also have a large share in the hedonic state and a nontrivial share in the utilitarian state.

## 6.2. Within-State App Interdependence

In this section, we explore the app interdependence pattern within each state. Speci<sup>fi</sup>cally, we examine the marginal impact of previous use on current use.

The full estimation results of the state-dependent app choice and duration processes are shown in the online appendix.<sup>15</sup> We <sup>fi</sup>rst explore app choice interdependence by examining the marginal effect of previous app choice on current app choice, using the intrinsic share as the baseline. The results are shown in Tables 10–12. In each table, the probability of choosing stop is calculated for each app category after its own use. We also calculate the probabilities of choosing the <sup>fi</sup>ve app categories, which are then compared with the intrinsic shares in the bottom of the table. To better compare with the intrinsic share, numbers inside the parentheses are the current choice probabilities after using the previous app conditional on not choosing stop. Numbers outside are the marginal effects, that is, differences of current choice probabilities after using the previous app to the intrinsic shares. For example, for the <sup>fi</sup>rst cell in Table 10, 35.85% is the choice probability of choosing social app after using social app given the user does not stop, whereas the marginal effect of 10.95% is the difference of such probability to the intrinsic share of social app (i.e., 10.95% 35.85% 24.90%).

The tables show interesting <sup>fi</sup>ndings. First, we measure the overall choice interdependence by calculating the average absolute marginal effect in each state. The results show that they are 5.43%, 9.75%, and 12.23% for utilitarian, social, and hedonic states, respectively. In other words, the overall choice interdependence is the strongest in the hedonic state, weakest in the utilitarian state, and social is in the middle. Second, the marginal effects on the diagonal are all positive, whereas the off-diagonals (excluding stop) are mostly negative. In addition, most effects are signi<sup>fi</sup>cant. Third, users are much more likely to stop using mobile in the utilitarian state compared with other states.

Table 10. Effects of Previous App Choice on Current Choice (Utilitarian State)

<table><tr><td> $t \rightarrow t + 1$ </td><td>Social (%)</td><td>Information (%)</td><td>Entertainment (%)</td><td>Shopping (%)</td><td>Tool (%)</td><td>Stop</td></tr><tr><td>Social</td><td>10.95***(35.85)**</td><td>-2.38***(25.17)**</td><td>-2.05***(6.76)**</td><td>-0.74***(2.28)**</td><td>-5.78***(29.94)**</td><td>55.35</td></tr><tr><td>Information</td><td>-6.75***(18.15)**</td><td>18.52***(46.07)**</td><td>-2.46***(6.35)**</td><td>-1.13***(1.89)**</td><td>-8.18***(27.54)**</td><td>51.34</td></tr><tr><td>Entertainment</td><td>-5.15***(19.75)**</td><td>-4.18***(23.37)**</td><td>10.65***(19.46)**</td><td>-1.24***(1.78)**</td><td>-0.08***(35.64)**</td><td>59.60</td></tr><tr><td>Shopping</td><td>-5.07***(19.83)**</td><td>0.85***(28.40)**</td><td>-1.45***(7.36)**</td><td>9.75***(12.77)**</td><td>-4.08***(31.64)**</td><td>61.16</td></tr><tr><td>Tool</td><td>-6.01***(18.89)*</td><td>-6.40***(21.15)*</td><td>-3.08***(5.73)*</td><td>-1.67***(1.35)*</td><td>17.16***(52.88)*</td><td>50.98</td></tr><tr><td>Intrinsic share</td><td>(24.90)</td><td>(27.55)</td><td>(8.81)</td><td>(3.02)</td><td>(35.72)</td><td>——</td></tr></table>

Note. Numbers in the parentheses are choice shares conditional on nonstop.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Table 11. Effects of Previous App Choice on Current Choice (Social State)

<table><tr><td> $t \rightarrow t + 1$ </td><td>Social (%)</td><td>Information (%)</td><td>Entertainment (%)</td><td>Shopping (%)</td><td>Tool (%)</td><td>Stop</td></tr><tr><td>Social</td><td>29.06***(89.49)**</td><td>-3.48***(1.35)**</td><td>-18.84***(6.76)**</td><td>-4.83***(1.70)**</td><td>-1.91***(0.70)**</td><td>8.77</td></tr><tr><td>Information</td><td>-19.33***(41.10)**</td><td>32.81***(37.64)**</td><td>-9.68***(15.92)**</td><td>-2.71***(3.82)**</td><td>-1.09***(1.52)**</td><td>16.39</td></tr><tr><td>Entertainment</td><td>-15.62***(44.81)**</td><td>-1.25***(3.58)**</td><td>19.89***(45.49)**</td><td>-2.13***(4.40)**</td><td>-0.89***(1.72)**</td><td>18.67</td></tr><tr><td>Shopping</td><td>-9.11***(51.32)**</td><td>-1.66***(3.17)**</td><td>-10.77***(14.83)**</td><td>22.43***(28.96)**</td><td>-0.89***(1.72)**</td><td>17.48</td></tr><tr><td>Tool</td><td>-9.05***(51.38)**</td><td>-0.06***(4.77)**</td><td>-7.56***(18.04)**</td><td>-1.02***(5.51)**</td><td>17.69***(20.30)**</td><td>21.45</td></tr><tr><td>Intrinsic share</td><td>(60.43)</td><td>(4.83)</td><td>(25.60)</td><td>(6.53)</td><td>(2.61)</td><td>—</td></tr></table>

Note. Numbers in the parentheses are choice shares conditional on nonstop.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Together, these results show that consumers are more likely to use the same app category over use occasions at the expense of other app categories. Such choice interdependence is strongest in the hedonic state, followed by the social and utilitarian states. Moreover, mobile use is more likely to cease when users are in the utilitarian state. These results can be explained by the theory of utilitarianism and hedonism. There is a rich literature on this topic (cited earlier), and the basic <sup>fi</sup>nding is that utilitarian is more task related and rational; hence, people seek ef<sup>fi</sup>- ciency. Conversely, hedonism is associated with fun and pleasure; hence, people seek exploration (Grif<sup>fi</sup>n et al. 2000, Chaudhuri et al. 2010). Thus, in terms of app use, in the utilitarian state (versus hedonic), users are less likely to use the same app category once a certain task is ful<sup>fi</sup>lled or to stop using mobile when al tasks are ful<sup>fi</sup>lled. Our results are largely consistent with this. In addition, our results suggest that the social state, which lacks prior research on its property, is more balanced in that it “behaves” in the middle of the utilitarian and hedonic states.

Interestingly, the duration interdependence is limited in that most of the marginal effects are insigni<sup>fi</sup>- cant (reported in the online appendix). In sum, our results show a signi<sup>fi</sup>cant within-state choice interdependence pattern, with hedonic state being the strongest, followed by the social and utilitarian states. Conversely, duration interdependence is limited.

## 6.3. Across-State: State Transitions

In this section, we turn to the across-state analysis. We <sup>fi</sup>rst examine the intrinsic state transition and then explore how it is affected by the contextual factors and past app uses. The full estimation results of the state transition process are shown in the online appendix.

6.3.1. Intrinsic State Transition. We report the intrinsic state transition in Table 13. It shows very interesting <sup>fi</sup>ndings. Utilitarian is a sticky state in that it has a 65.69% chance of being maintained. However, social and hedonic states are transient. For example, there is a more than 56% chance of switching to other states from the social state and an almost 45% chance of switching away from the hedonic state. A priori, consumer behavior theory is not conclusive on the tran sient ranking between hedonic and utilitarian states. According to the involvement theory (Zaichkowsky 1985, Wang et al. 2011), users in the utilitarian state are task oriented and thus would exert a greater level of effort. Conversely, Laurent and Kapferer (1985) suggest that people can engage in a different type of involvement, that is, hedonic involvement. Therefore, it is an empirical question as to which state is more mentally involved and therefore less transient. Our result suggests that in the mobile era, the utilitarian state is less transient than hedonic, although the latter is more frequent (suggested by the initial distribution). To explain that the social state is the most transient, we resort to the ubiquity feature of mobile Internet, which gives users plenty of opportunities to communicate with others within micromoments, for example, a short con<sup>fi</sup>rmation to a friend on when and where to meet. This could explain why the social state is the most transient.

Table 12. Effects of Previous App Choice on Current Choice (Hedonic State)

<table><tr><td> $t \rightarrow t + 1$ </td><td>Social (%)</td><td>Information (%)</td><td>Entertainment (%)</td><td>Shopping (%)</td><td>Tool (%)</td><td>Stop</td></tr><tr><td>Social</td><td>36.55***(72.60)**</td><td>-7.48***(5.67)**</td><td>-23.50***(17.62)**</td><td>-1.92***(1.84)**</td><td>-3.65***(2.27)**</td><td>12.00</td></tr><tr><td>Information</td><td>-11.01***(25.04)**</td><td>25.34***(38.49)**</td><td>-12.04***(29.08)**</td><td>-0.91***(2.85)**</td><td>-1.38***(4.54)**</td><td>19.36</td></tr><tr><td>Entertainment</td><td>-14.37***(21.68)**</td><td>-8.68***(4.47)**</td><td>28.07***(69.19)**</td><td>-1.93***(1.83)**</td><td>-3.09***(2.83)**</td><td>9.26</td></tr><tr><td>Shopping</td><td>-14.47***(21.58)**</td><td>-5.69***(7.46)**</td><td>-16.37***(24.75)**</td><td>38.65***(42.41)**</td><td>-2.12***(3.80)**</td><td>17.59</td></tr><tr><td>Tool</td><td>-7.91***(28.14)**</td><td>-5.40***(7.75)**</td><td>-10.14***(30.98)**</td><td>-0.81***(2.95)**</td><td>24.26***(30.18)**</td><td>16.23</td></tr><tr><td>Intrinsic share</td><td>(36.05)</td><td>(13.15)</td><td>(41.12)</td><td>(3.76)</td><td>(5.92)</td><td>—</td></tr></table>

Note. Numbers in the parentheses are choice shares conditional on nonstop.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Table 13. Intrinsic State Transition Matrix

<table><tr><td> $t \rightarrow t + 1$ </td><td>Utilitarian (%)</td><td>Social (%)</td><td>Hedonic (%)</td></tr><tr><td>Utilitarian</td><td>65.69</td><td>11.93</td><td>22.38</td></tr><tr><td>Social</td><td>31.67</td><td>43.71</td><td>24.62</td></tr><tr><td>Hedonic</td><td>37.17</td><td>7.81</td><td>55.02</td></tr></table>

We also examine the directions of transitions among states. We <sup>fi</sup>nd that utilitarian and hedonic states are “twin” states. When users move away from the utilitarian state, they are twice likely to move to the hedonic state than the social state; when they move away from the hedonic state, they primarily switch to the utilitarian state. The social state, in contrast, behaves like a “transitory” state to <sup>fi</sup>ll users fragmented micromoments. Speci<sup>fi</sup>cally, users’ mindsets do not change to the social state frequently when they are in either a utilitarian (<12%) or hedonic (<8%) state. In addition, when users are in the social state, the distribution of their next states is similar to a random walk.

One thing to be noted is that earlier results (Table 5) show that social apps uses are stickiest, whereas Table 13 shows the social state is the least sticky. The reason, as shown in Figure 3, is that social apps not only dominate in the social state but also constitute a large share in the hedonic state and a nontrivial share in the utilitarian state. Thus, when a user’s social state changes to another state, there is still a nonnegligible chance to use social apps. As a result, although the social state is the least sticky, social apps need not be.

Table 14. Change in State Transition Probability: WiFi (Baseline: 3G)

<table><tr><td> $t \rightarrow t + 1$ </td><td>Utilitarian (%)</td><td>Social (%)</td><td>Hedonic (%)</td></tr><tr><td>Utilitarian</td><td>-2.06(64.85)</td><td>0.72(12.22)</td><td>1.34(22.93)</td></tr><tr><td>Social</td><td>0.06(31.78)</td><td>-0.10(43.67)</td><td>0.04(24.55)</td></tr><tr><td>Hedonic</td><td>-0.50(36.97)</td><td>-0.10(7.77)</td><td>0.60(55.26)</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

## 6.3.2. Impact of Contextual Factors.

<sup>6.3.2.1. Bandwidth.</sup> We examine the effect of band width using 3G as the baseline. We report the results in Table 14. Numbers outside the parentheses are the average difference of WiFi to 3G, whereas numbers inside are the average transition probabilities under WiFi.

Overall, the bandwidth condition has a limited impact on the transition of states; that is, all effects are insigni<sup>fi</sup>cant. One reason could lie in the fragmented use of mobile apps. Because users frequently utilize their fragmented free time to access mobile apps, such use tends to be light in terms of time length and the amount of content loaded from the Internet. Therefore, bandwidth condition does not have a large impact on the transition of states.

<sup>6.3.2.2.</sup> <sup>Location.</sup> Using office as the baseline, we examine the effects of home and on the way as well. We report the results in Table 15. Numbers outside the parentheses are the average difference of home to office (or on the way to office), whereas numbers inside are the average transition probabilities under home (or on the way).

The results show that location has a signi<sup>fi</sup>cant impact. Speci<sup>fi</sup>cally, compared with the of<sup>fi</sup>ce, when users are at home or on the way, their states are more transient (with home being the most transient), re-<sup>fl</sup>ected by the signi<sup>fi</sup>cantly negative change in the diagonals. This shows that users’ mindsets are more volatile when they are at home or on the way (versus of<sup>fi</sup>ce). As discussed earlier, this could be driven by the presence of time constraint when people are in workplaces, which leads to lower cognitive capacity allocated for mobile use and thus a less volatile state transition. Speci<sup>fi</sup>cally, past research (Collins et al. 2016, Sedani et al. 2019) show that people face stronger time constraints in the of<sup>fi</sup>ce.<sup>16</sup> That could reduce their cognitive capacity (Park et al. 1989, Suri and Monroe 2003) allocated to mobile use. Consequently, users may focus their limited cognitive resources on a certain type of mobile activity in their fragmented free times during work, leading to a less volatile state transition. This is consistent with the <sup>fi</sup>nding in Xu et al. (2014), which shows that users are less likely to use multiple mobile media channels with stronger time constraints.

<sup>6.3.2.3.</sup> <sup>Time</sup> <sup>of</sup> <sup>Day.</sup> Using night as the baseline, we examine the effects of morning, day, and evening. We report the results in Table 16. Numbers outside the parentheses are the average difference of morning to night (or day to night, or evening to night), whereas numbers inside are the average transition probabilities with morning (or day or evening).

Table 15. Change in State Transition Probability: Location (Baseline: Office)

<table><tr><td rowspan="2"> $t \rightarrow t + 1$ </td><td colspan="3">Home (%)</td><td colspan="3">On the Way (%)</td></tr><tr><td>Utilitarian</td><td>Social</td><td>Hedonic</td><td>Utilitarian</td><td>Social</td><td>Hedonic</td></tr><tr><td>Utilitarian</td><td>-11.78***(62.48)</td><td>4.10***(13.05)</td><td>7.68***(24.47)</td><td>-6.76**(67.50)</td><td>2.35**(11.30)</td><td>4.41**(21.20)</td></tr><tr><td>Social</td><td>4.96***(33.27)</td><td>-8.79***(41.04)</td><td>3.83***(25.69)</td><td>1.66*(29.97)</td><td>-2.95*(46.88)</td><td>1.29*(23.15)</td></tr><tr><td>Hedonic</td><td>6.18***(38.65)</td><td>1.30***(8.12)</td><td>-7.48***(53.23)</td><td>3.85**(36.32)</td><td>0.81**(7.63)</td><td>-4.66**(56.05)</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Compared with night, users’ states are more transient at other times of a day as re<sup>fl</sup>ected by the signi<sup>fi</sup>- cantly negative change on the diagonals. Overall, morning is the most transient followed by evening. Speci<sup>fi</sup>cally, users are more likely to switch to utilitarian from hedonic in the morning, whereas they are more likely to switch to hedonic from utilitarian in the evening. Such a pattern is consistent with past <sup>fi</sup>ndings (Bhat and Misra 1999, Luo et al. 2013) that people form habitual routines across different times of day, in which morning is typically <sup>fi</sup>lled with work-related tasks and evening is often reserved for relaxation.

6.3.3. Impact of Past App Use. We explore the impacts of past use on state transition and report the results in Tables 17–21. Each subtable corresponds to a speci<sup>fi</sup>c past use’s app category. Numbers inside the parentheses are the state transition probabilities after using the previous app. Numbers outside are the marginal effects, that is, differences of state transition probabilities after using the previous app to the intrinsic state transition. For example, for the <sup>fi</sup>rst cell in Table 18, 62.64% is the transition probability from utilitarian to utilitarian after using information app, whereas the marginal effect 3.05% is the difference of such probability to the intrinsic transition probability in Table 13 (i.e., 3.05% 62.64% 65.69%).

In general, past app use has a milder impact on the state transition than contexts. There is no signi<sup>fi</sup>cant impact of past social or tool app use. Of the three states, the transition from the hedonic state is the least sensitive to past app uses, that is, no signi<sup>fi</sup>cant effect. Interestingly, starting from the utilitarian state, previous use of information app leads to higher chance of switching to the social or hedonic state. Because the utilitarian state is characterized by heavy use of information apps, one reason could be saturation; that is, the marginal utility of gaining information decreases. In addition, previous use of shopping app leads to higher chance of switching from utilitarian to hedonic. A possible explanation is that after making consump tion choices in a more rational state (i.e., utilitarian), users’ mindsets are more likely to seek for fun/relaxation (i.e., hedonic). When starting in the social state, previous use of an entertainment ap p<sup>17</sup> leads to a higher chance of staying in the social state and a lower chance of switching to the utilitarian state. Because the entertainment app occupies a nontrivial share in the social state, a likely reason could be inertia.

## 6.4. Model Fit

Following Netzer et al. (2008), we examine the <sup>fi</sup>t of the proposed HMM (model 1) with other models, using the hold-out sample. We consider two alternative models: HMM without user heterogeneity (model 2) and a static latent class model without user heterogeneity (model 3). The results are shown in Table 22. We consider the log-likelihood and BIC calculated from the hold-out sample. Furthermore, we compare the predictive abilities of app choice based on hit rate<sup>18</sup> and the root-mean-square prediction error (RMSPE) between the predicted choice probabilities and the actual choices. As a benchmark, we consider the random choice rule that is based on the app category share (including stop) in the calibration sample, which is then compared with the actual choice in the holdout sample. The hit rate and RMSPE of the random choice rule in the hold-out sample are 38.29% and 76.52%, respectively.

Table 16. Change in State Transition Probability: Time of Day (Baseline: Night)

<table><tr><td rowspan="2"> $t \rightarrow t + 1$ </td><td colspan="3">Morning (%)</td><td colspan="3">Day (%)</td><td colspan="3">Evening (%)</td></tr><tr><td>Utilitarian</td><td>Social</td><td>Hedonic</td><td>Utilitarian</td><td>Social</td><td>Hedonic</td><td>Utilitarian</td><td>Social</td><td>Hedonic</td></tr><tr><td>Utilitarian</td><td>-3.02**(67.35)*</td><td>1.05(11.35)</td><td>1.97*(21.30)</td><td>-3.81*(66.56)</td><td>1.33*(11.63)</td><td>2.48*(21.81)</td><td>-7.31***(63.06)</td><td>2.54***(12.84)</td><td>4.77***(24.10)</td></tr><tr><td>Social</td><td>2.34**(31.78)*</td><td>-4.15*(43.67)</td><td>1.81*(24.55)</td><td>2.64**(32.08)</td><td>-4.67**(43.15)</td><td>2.03**(24.77)</td><td>2.47***(31.91)</td><td>-4.37***(43.45)</td><td>1.90***(24.64)</td></tr><tr><td>Hedonic</td><td>8.09***(42.34)*</td><td>1.70***(8.90)</td><td>-9.79***(48.76)</td><td>3.14*(37.39)</td><td>0.66*(7.86)</td><td>-3.80*(54.75)</td><td>2.03*(36.28)</td><td>0.42(7.62)</td><td>-2.45(56.10)</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Table 17. Change in State Transition Probability: Social App Usage

<table><tr><td> $t \rightarrow t + 1$ </td><td>Utilitarian (%)</td><td>Social (%)</td><td>Hedonic (%)</td></tr><tr><td>Utilitarian</td><td>0.64(66.33)</td><td>-0.22(11.71)</td><td>-0.42(21.96)</td></tr><tr><td>Social</td><td>0.27(31.94)</td><td>-0.32(43.39)</td><td>0.05(24.67)</td></tr><tr><td>Hedonic</td><td>-0.69(36.48)</td><td>-0.14(7.67)</td><td>0.83(55.85)</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

The results show that the proposed HMM outperforms the other two alternatives in all measures, with improvements of hit rate and RMSPE (versus random choice rule) being 55% and 23%, respectively. Speci<sup>fi</sup>- cally, comparing model 2 with model 3 shows that extending static latent class to dynamic latent class improves predictive ability. Comparing model 1 and model 2 shows the value of incorporating user heterogeneity. In fact, the parameter estimates reported in the online appendix show that user heterogeneity plays an important role in the app choice process and the state transition (i.e., the estimates in both processes are signi<sup>fi</sup>cant with large magnitude), but not in use duration (i.e., the estimate is insigni<sup>fi</sup>cant).

## 6.5. Managerial Implication

As discussed earlier, the trend of many Internet companies’ strategies is cross-industry expansion. Companies with a portfolio of various app categories require management across apps. In addition, with better online tracking technology, mobile analytics platforms or consulting <sup>fi</sup>rms can provide cross-app management services. An important output of the proposed HMM for managerial implications is the state dynamic. Thus, we <sup>fi</sup>rst perform the posterior analysis to recover the state evolution as a numerical demonstration. We then discuss how companies with data of cross-app use may leverage the insights gained from such output and, in general, the proposed framework to design better dig ital strategies.

Table 18. Change in State Transition Probability: Info App Use

<table><tr><td> $t \rightarrow t + 1$ </td><td>Utilitarian (%)</td><td>Social (%)</td><td>Hedonic (%)</td></tr><tr><td>Utilitarian</td><td>-3.05***(62.64)**</td><td>1.06***(12.99)**</td><td>1.99***(24.37)*</td></tr><tr><td>Social</td><td>-0.95**(30.72)**</td><td>1.85**(45.56)**</td><td>-0.90**(23.72)*</td></tr><tr><td>Hedonic</td><td>3.57**(40.74)**</td><td>0.76**(8.57)**</td><td>-4.33**(50.69)*</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Table 19. Change in State Transition Probability: Ent App Use

<table><tr><td> $t \rightarrow t + 1$ </td><td>Utilitarian (%)</td><td>Social (%)</td><td>Hedonic (%)</td></tr><tr><td>Utilitarian</td><td>-0.74**(64.95)*</td><td>0.26**(12.19)*</td><td>0.48**(22.86)*</td></tr><tr><td>Social</td><td>-1.62***(30.05)*</td><td>3.04***(46.75)*</td><td>-1.42**(23.20)*</td></tr><tr><td>Hedonic</td><td>1.80**(38.97)*</td><td>0.38**(8.19)*</td><td>-2.18**(52.84)*</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

6.5.1. Posterior Analysis. Although the analyses in Section 6.3 provide important insights on how contextual factors and previous app uses in<sup>fl</sup>uence the state dynamic, the analytical base is the intrinsic state transition that may limit the scope of discussion, because in practice, the state evolution is a complicated dynamic process with nonlinear interaction effects between contexts and past use. Therefore, we perform the posterior analysis to recover the state evolution in the data to gain more insight.

Similar to previous studies (Singh et al. 2011, 2014; Yan and Tan 2014), we applied the <sup>fi</sup>ltering approach proposed by Hamilton (1989) to recover users’ unobserved states across occasions in each session. Once the model parameters are estimated, the likelihood can be obtained using the information until occasion t. The probability for a user in a given state can be calculated using the Bayes rules:

$$
\begin{array}{c} \mathrm{P} (S _ {i t} = s \mid O _ {i s 1}, O _ {i s 2}, \dots , O _ {i s t}) = \pi (i s) \Lambda (i s, 1) Q (i s, 1, 2) \\ \Lambda (i s, 2) \dots Q (i s, t - 1, t) P (O _ {i s t} \mid s) / L _ {i s t}, \end{array}\tag{12}
$$

where $L _ { i s t }$ is the likelihood of the observed sequence of app use for session s of user i up to occasion t. The Bayes rule allows each occasion in each session to be classi<sup>fi</sup>ed into a state according to the largest posterior probability. We report the results in Figures 4–8.

Table 20. Change in State Transition Probability: Shopping App Use

<table><tr><td> $t \rightarrow t + 1$ </td><td>Utilitarian (%)</td><td>Social (%)</td><td>Hedonic (%)</td></tr><tr><td>Utilitarian</td><td>-2.59***(63.10)*</td><td>0.90(12.83)*</td><td>1.69***(24.07)*</td></tr><tr><td>Social</td><td>-0.19***(31.48)*</td><td>0.51***(44.22)*</td><td>-0.32***(24.30)*</td></tr><tr><td>Hedonic</td><td>4.98**(42.15)*</td><td>1.04**(8.85)*</td><td>-6.02**(49.00)*</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Table 21. Change in State Transition Probability: Tool App Use

<table><tr><td> $t \rightarrow t + 1$ </td><td>Utilitarian (%)</td><td>Social (%)</td><td>Hedonic (%)</td></tr><tr><td>Utilitarian</td><td>-1.78(63.91)</td><td>0.62(12.55)</td><td>1.16(23.54)</td></tr><tr><td>Social</td><td>1.26(32.93)</td><td>-2.07(41.64)</td><td>0.81(25.43)</td></tr><tr><td>Hedonic</td><td>1.12(38.29)</td><td>0.24(8.05)</td><td>-1.36(53.66)</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

For each occasion, we aggregate over all corresponding sessions to obtain shares of each state.

We <sup>fi</sup>rst examine the overall state evolution for short (5 occasions) and long (10 occasions) sessions in Figure 4. Both graphs show that the share of hedonic decreases over occasions but the share of utilitarian increases, whereas social’s share is relatively stable. It shows that users typically start using smartphones with a hedonic mindset (possibly seeking for entertainment), but gradually switch to more utilitarian, while social is an intermittent state between them. Such a pattern is consistent with previous <sup>fi</sup>ndings. In what follows, we only present results for sessions with 10 occasions. Results for shorter sessions (<sup>fi</sup>ve occasions) are largely consistent and reported in the online appendix.

We then examine the differential patterns of state evolution under different contexts in Figures 5–7. The results suggest that the decay of hedonic within a session is faster under WiFi than 3G. For time of day, the decay of hedonic is the fastest in evening, whereas the shares are the most stable in morning. For location, the decay of hedonic is the fastest in of<sup>fi</sup>ce, whereas the shares are the most stable on the way. In addition, the share of social is the lowest in of<sup>fi</sup>ce and the share of utilitarian is the largest on the way.

Next, we examine the differential patterns under different app choices of the <sup>fi</sup>rst occasion in Figure 8. The results show rich heterogeneities. When the <sup>fi</sup>rst app is social, the chance of being in the social state is greater (versus the aggregate share in Figure 4) at the beginning but then quickly returns to the average level. When the <sup>fi</sup>rst app is information, the initial state is unlikely to be social (versus Figure 4). Then the social state quickly picks up with a rapid decay of the hedonic state. When the <sup>fi</sup>rst app is entertainment, the initial state is very likely to be hedonic mostly at the expense of utilitarian. Then the hedonic state quickly decays with the recovery of utilitarian while the share of social remains relatively stable. When the <sup>fi</sup>rst app is shopping, the initial state is much more likely to be social mainly at the expense of utilitarian (versus Figure 4). Then the utilitarian state picks up, whereas the social state stumbles over time. When the <sup>fi</sup>rst app is tool, the initial state is almost certainly to be utilitarian, which rapidly decreases in the next occasion with fast recovery of both social and hedonic states.

We conduct similar analyses for both <sup>fi</sup>rst and second choices of apps. The results (reported in the online appendix) show that the state evolutions vary drastically under different scenarios. We also report several session level state dynamic examples in the online appendix, showing both volatile and stable sessions. Overall, the posterior analysis shows rich heterogeneity of state evolution under different contexts and past use. We believe that such an output can provide valuable insight to practitioners.

6.5.2. Implications on Digital Strategies. As shown previously, the model can be used to recover users states and their dynamic. Although such state is unobserved, it can be predicted when a user launches the app under various contexts based on the model. As discussed earlier, users behave differently in the utilitarian and hedonic states. The former typically involves rationality, goal, and task orientation. The latter is associated with fun, curiosity, and exploration. Thus, upon knowing the state of an incoming user, app managers can react accordingly.

One example is for shopping apps and other types of apps that offer in-app purchase options. Prior literature (Hirschman 1984, Jarboe and McDaniel 1987, Sherry et al. 1993, Babin et al. 1994, Janiszewski 1998) suggests that consumer shopping behavior is driven

Table 22. Model Fit and Predictive Ability Measures

<table><tr><td>Measure</td><td>Model 1:HMM with heterogeneity</td><td>Model 2:HMM without heterogeneity</td><td>Model 3:Static latent class</td></tr><tr><td>Hold-out log-likelihood</td><td>-51,587.0</td><td>-55,230.9</td><td>-56,806.7</td></tr><tr><td>Hold-out BIC</td><td>-56,245.2</td><td>-59,856.9</td><td>-60,977.5</td></tr><tr><td>Hit rate (%)</td><td>59.35</td><td>58.68</td><td>56.10</td></tr><tr><td>Improvement over the random hit rate (%)</td><td>55.00</td><td>53.25</td><td>46.51</td></tr><tr><td>RMSPE</td><td>59.27</td><td>60.40</td><td>61.78</td></tr><tr><td>Improvement over the random RMSPE (%)</td><td>22.54</td><td>21.06</td><td>19.26</td></tr></table>

Figure 4. Posterior States over Time  
![](/api/attachments/7KV2FZYF/fulltext/images/07b943706169448af64eae6762abbb8809076a833d9fda6ad2aca19264842105.jpg)

![](/api/attachments/7KV2FZYF/fulltext/images/588af457109ece239339b481b2c74248046c08cf003649b19c4e2744a15317fd.jpg)

more by making better purchasing decision in the utilitarian state, whereas they engage more in hedonic browsing and impulsive buying in the hedonic state. Thus, upon detecting a user’s state, a shopping app may tilt its search and recommendation algorithms to depend more on the user’s past behavior within the app if it is a utilitarian state. The purpose is to better match the recommended products to the user’s preference, increasing the conversion rate for a utilitarian-oriented consumer. Such effort should be enhanced when the user is at home or on the way and/or in the evening because people are more likely to transit away from the utilitarian state under these contexts. Conversely, if the user is in a hedonic mind set, the app may consider displaying more diversi<sup>fi</sup>ed (e.g., products that are less known to the user to spur

Figure 5. Posterior States over Time (Bandwidth)  
![](/api/attachments/7KV2FZYF/fulltext/images/69774b717487e06431692d47e1f1feac2126ed6204169f916fcca6e0981e2f26.jpg)

Figure 6. Posterior States over Time (Time of Day)  
![](/api/attachments/7KV2FZYF/fulltext/images/49fefd1d99bfa84a10178a791b315811c3fd3409a14c2c185efb38d90523a3de.jpg)

![](/api/attachments/7KV2FZYF/fulltext/images/aab7c6157239151b575a3521f4ad76c526d52fdb0fefa2d6fc9d0139248d26c9.jpg)

![](/api/attachments/7KV2FZYF/fulltext/images/e9f73876bfd4bd0dbf7f8c7206d3604fee48c5d3ad3352ea1935cffb614666e0.jpg)

curiosity) and impulsive-buying products to satisfy her hedonic browsing need and to increase the chance of impulsive purchase.

Another example is targeted advertising. Many apps’ business models strongly rely on attracting traf-<sup>fi</sup>c and then selling advertising slots. Thus, increasing click-through rate and strengthening memory of the ad content are critical. The implications derived from the previous discussion are as follows. If the user is in the utilitarian state, ads with concrete incentivized information (e.g., discounts) could be prioritized. Conversely, ads with hedonic information, such as those with fun content, should be preferred if the user is in the hedonic state.

Unlike previous research, our model also recovers an additional social state. Such social state bears important managerial implications, particularly under the burgeoning integration of social network and e-commerce. Motivated by the success of Pinduoduo, one of the largest Chinese e-commerce platforms worth \$110 billion,<sup>19</sup> which encourages users to participate in group buying deals, other e-commerce giants (e.g., JD.com) are also aggressively designing their social strategies. Ef<sup>fi</sup>cient information dissemination and social persuasion are at the heart of such a “social shopping” trend. Therefore, an important implication is that, upon detecting an incoming user being in the social state, a shopping app should adopt strategies to encourage product sharing to the user’s social network. Such strategies may include in-app noti<sup>fi</sup>cations of sharing and/or giving out economic incentive (e.g., loyalty points). In particular, such strategies should be strengthened when the user is at home or on the way, and/or in the morning because our results indicate that people are more likely to switch away from the social state under these contexts. Except for shopping apps, many gaming apps are inherently social in that they are multiplayer games or involve contest among the social network. Thus, the implications discussed above also apply to them.

![](/api/attachments/7KV2FZYF/fulltext/images/520cf5a700615af8ee93070433c993307e68edd33ed5095b2772173827889409.jpg)

As a by-product, the proposed model can also generate predictions of app category choice and use dura tion. These outputs are also managerially informative. For example, a critical challenge for shopping apps is the low conversion rate.<sup>20</sup> One important reason is the speed of loading mobile pages. Some industry statistics show that 40% of users will not wait for longer than three seconds, and after a poor experience, 79% will not return.<sup>21</sup> However, with the prediction of the next-chosen app category and its use duration, apps in the next category can receive a notice in advance so that contents can be preloaded to fasten the page load. Another example for the application of our model is app noti<sup>fi</sup>cation push. With the prediction of app category choices and duration, one can push apps in the category with the highest choice probability, or the longest use duration, or a certain combination of them to better satisfy the user.

Figure 7. Posterior States over Time (Location)  
![](/api/attachments/7KV2FZYF/fulltext/images/43aa7a006ceb1d5355ac3d519a026a5eab52089781b9e6950ceadeeebdc16bc8.jpg)

Last but not least, our <sup>fi</sup>ndings offer several insights on improving app use in a mobile Internet context. Different from the PC context, we identify a social state that is prevalent but most transient, indicating mobile users have a fundamental need for frequent light-social activities. Thus, one strategy to increase use is to enrich an app’s social components. More importantly, such enhancement should focus more on light-social functionalities. In addition, as discussed earlier, our results show that app interdependence is the strongest under the hedonic state. This indicates that, ceteris paribus, the strategic value of boosting current app use on future use is the highest in the hedonic state, providing guidance to companies on better spending of their limited marketing resources. Furthermore, we have shown that these internal states are interdependent of each other, and their dynamic is affected by contextual factors (e.g., time of day and location) that are distinct in the mobile context. Thus, to win user loyalty, companies should put more weight on tailoring their engagement strategies under different contexts in mobile Internet rather than the traditional PC context.

## 7. Conclusion and Limitation

In this paper, we study users’ cross-app use behavior. We argue that compared with PC Internet, mobile use

Figure 8. Posterior States over Time (First App)  
![](/api/attachments/7KV2FZYF/fulltext/images/a2a41c2a21741d3e767aa1f6186699e6d1c5efa67f77dee1f7603734cc9f95d2.jpg)

![](/api/attachments/7KV2FZYF/fulltext/images/9e1af7f09eb08bf3bb96ba01947d13d026ac2b6efc6ba31f216561fbc2d0581f.jpg)

![](/api/attachments/7KV2FZYF/fulltext/images/2ed736d1eecfb0202265d2d0b4be4637524ce38ba4dca48d3c9fb4244f107aae.jpg)

![](/api/attachments/7KV2FZYF/fulltext/images/9f5eea37863d60ab2c9ed1c6a9b55dd2d9c2a172ef35d6b0330c76fc67eb953f.jpg)

![](/api/attachments/7KV2FZYF/fulltext/images/f16e98164bcdc8b5d257a276cab0341fb28057cc54408d843bd408ed7984e173.jpg)  
is ubiquitous and more context dependent. We develop an HMM to uncover the underlying mechanism of cross-app uses. Our empirical results identify three hidden states: utilitarian, social, and hedonic. Consumers use information and tool apps more often at the utilitarian state. Social apps occupy roughly half the share and the other apps take up the rest when consumers are at the social state. In the hedonic state, users largely use social and entertainment apps. Users exhibit strong within-state interdependence in app choices but not duration. Such interdependence is strongest in the hedonic state, followed by the social and utilitarian states. In terms of state transition, social state is the most transient, followed by the hedonic and utilitarian states. Utilitarian and hedonic states primarily intercommunicate with each other, whereas the social state is frequently intermittent. We also <sup>fi</sup>nd that location and time of day have signi<sup>fi</sup>cant impacts on the state dynamic (versus the intrinsic state transition), whereas bandwidth has limited effects. For location, the state dynamic is more volatile at home or on the way (versus at the of<sup>fi</sup>ce). Speci<sup>fi</sup>- cally, utilitarian and hedonic states switch from one to another more frequently, whereas the social state is more transient. For time of day, the state dynamic is more volatile in the morning or evening (versus night), with a tendency toward denser functional activities in the morning and denser hedonic activities in the evening. The results also show that previous use of information, entertainment, or shopping apps also affect the state transition.

Finally, we discuss the managerial implications amid a strong trend of cross-industry expansion in the mobile landscape. We examine the patterns of state evolution recovered from the data—a critical output from the HMM model. We discuss how knowledge of users’ internal state can help better design search algorithm, personalized recommendation, targeted advertising, and digital social strategies. We also discuss how predictions of app category choices and durations can help design more ef<sup>fi</sup>cient app content preload and app noti<sup>fi</sup>cation push. Finally, we shed light on how companies can use the unique features of mobile Internet (versus PC Internet) to increase app use based on the main <sup>fi</sup>ndings.

There are several limitations in our study. First, our model is at the app category level. An alternative framework is to model mobile use at the individual app level. However, because of the large number of apps $( \mathrm { e . g . } ,$ , roughly 1,800 apps in our study), the model will quickly explode in such a case. Given that the main focus of this study is to better understand the structure of internal states (i.e., a driving force of mobile app use) based on which managerial insights are derived, we choose to model app use at the app category level. We leave the extension to the individual app level for future research. Second, we model the HMM in a stationary fashion, whereas nonstationarity might occur because of, for example, transition probabilities being dependent on the state duration. Given the complexity of the current model that a rich set of control variables are included and asymmetric effects (across app categories and states) are allowed, incorporating nonstationarity is a fruitful extension yet, a challenging task. To partially account for such effect, we include the cumulative app use frequency and duration (for each category) before the current occasion in the state transition probabilities. Third, because our analysis is at the industry level, a single company may <sup>fi</sup>nd it challenging to run the same analyses. We believe that the framework developed in this study and the insights gained from our industry level analyses with multiple apps will be useful for an app to understand its upstream and downstream traf-<sup>fi</sup>c. For example, this may allow the identi<sup>fi</sup>cation of potential referral apps and also the potential competitors where the users switch to. An interesting future research direction will be to explore cases where a company can only access data from its own apps.<sup>22</sup>

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for constructive comments and suggestions throughout the review process.

## Endnotes

<sup>1</sup> See https://wearesocial.com/blog/2019/01/digital-2019-global-internetuse-accelerates, accessed October 10, 2021.

<sup>2</sup> See www.questmobile.cn/blog/blog-39.html, accessed October 10, 2021.

<sup>3</sup> See www.emarketer.com/content/mobile-time-spent-2018, accessed October 10, 2021.

<sup>4</sup> Facebook has acquired several gaming (e.g., PlayGiga, Best Games) and e-commerce (e.g., Packagd, GrokStyle, TheFind) companies.

5 Amazon acquired the social network Bebo in June 2019.

<sup>6</sup> During our sample period, 3G is the dominant data connection technique used by the major carriers in China.

<sup>7</sup> According to CNNIC 2014 China Social App Usage Report released by the China Internet Network Information Center, the most important function for most WeChat users is social, for example, chatting and browsing friends’ activity feeds.

<sup>8</sup> We also try 15- and 25-minute thresholds. The main findings (see the online appendix) are robust.

<sup>9</sup> In this study, M is five. For the first observation in a session, B<sup>c</sup> is a n M matrix because stop is not a choice; that is, we model a user’s app use behavior conditional on deciding to start a session.

<sup>10</sup> The algorithm to infer location types, which is reported in the online appendix, follows Zheng et al. (2009).

<sup>11</sup> Moving ahead to the results section where we identify three states (social, hedonic, and utilitarian), an example could be as follows: one might be more likely to stick to the social state after using social apps because of inertia, whereas one would be more likely to transition out from the hedonic state after using entertainment apps for too long because of feeling bored or guilty. We thank an anonymous referee for suggesting this example and inspiring such discussion.

<sup>12</sup> BIC used here as a false positive is more misleading than a false negative.

<sup>13</sup> Following Yan and Tan (2014), the intrinsic share is calculated by taking the variables in set D and F to zero. Thus, the outside option stop is not included in the calculation. In addition, the calculation is performed for all combinations of the contextual factors and then aggregated by their sample weights.

<sup>14</sup> In state 2, the shares for the other app categories are as follows: 4.83% (information), 6.53% (shopping), and 2.61% (tool).

<sup>15</sup> We allow the effects of a variable to depend on state and app category. Because these effects interact with each other in a nonlinear way, direct interpretation for the sign and magnitude of the coefficient is inconclusive. We therefore present the detailed estimation results in the online appendix.

<sup>16</sup> Our data are consistent with this notion in that users visit fewer apps in office (versus home and on the way). Specifically, in the calibration sample, the average numbers of app visit within a session are 5.15, 5.25, and 4.85 for home, on the way, and office, respectively

<sup>17</sup> Although previous use of shopping app has a statistically significant impact on the transition from social state, the magnitudes are small.

<sup>18</sup> To estimate hit rate, we predict a specific app category choice if its predicted probability is the largest.

<sup>19</sup> The number is recorded from NASDAQ in October 2021.

20 An industry report reveals that it is around 1.96% in the United States (see https://www.smartinsights.com/ecommerce/ecommerceanalytics/ecommerce-conversion-rates, accessed October 10, 2021.

<sup>21</sup> See www.bigcommerce.com/blog/mobile-commerce/#the-impactof-page-speed-on-mobile-commerce, accessed October 10, 2021.

<sup>22</sup> We thank the review team for inspiring these discussions.

## References

Abhishek V, Fader PS, Hosanagar K (2013) Media exposure through the funnel: A model of multi-stage attribution. Working paper, Carnegie Mellon University, Pittsburgh.

Babin BJ, Darden WR, Grif<sup>fi</sup>n M (1994) Work and/or fun: Measuring hedonic and utilitarian shopping value. J. Consumer Res. 20(4):644–656

Bhat CR, Misra R (1999) Discretionary activity time allocation of individuals between in-home and out-of-home and between weekdays and weekends. Transportation 26(2):193–229.

Bitner MJ (1992) Servicescapes: The impact of physical surroundings on customers and employees. J. Marketing 56(2):57–71.

Botti S, McGill AL (2010) The locus of choice: Personal causality and satisfaction with hedonic and utilitarian decisions. J. Consumer Res. 37(6):1065–1078.

Brown SA, Venkatesh V (2005) Model of adoption of technology in households: A baseline model test and extension incorporating household life cycle. Management Inform. Systems Quart. 29(3): 399–426.

Chaiken S, Liberman A, Eagly AH (1989) Heuristic and systematic information processing within and beyond the persuasion context. Uleman JS, Bargh JA, York N, eds. Unintended Thought Guilford), 212–252

Chaudhuri A, Aboulnasr K, Ligas M (2010) Emotional responses on initial exposure to hedonic or utilitarian description of a radical innovation. J. Marketing Theory Practice 18(4):339–359.

Chitturi R, Raghunathan R, Mahajan V (2008) Delight by design: The role of hedonic vs. utilitarian bene<sup>fi</sup>ts. J. Marketing 72(3):48–63.

Collins K, Shiffman D, Rock J (2016) How are scientists using social media in the workplace? PLoS One 11(10):e0162680.

Danziger S, Levav J, Avnaim-Pesso L (2011) Extraneous factors in ju Proc. National Acad. Sci. USA –

Ding AW, Li S, Chatterjee P (2015) Learning user real-time intent for optimal dynamic web page transformation. Inform. System Res. 26(2):339–359.

Donovan RJ, Rossiter JR (1982) Store atmosphere: An environmental psychology approach. J. Retailing 58(1):34–57.

Fang Z, Gu B, Luo X, Xu Y (2015) Contemporaneous and delayed sales impact of location-based mobile promotions. Inform. Systems Res. 26(3):552–564.

Fong N, Fang Z, Luo X (2015) Geo-conquesting: Competitive locational targeting of mobile promotions. J. Marketing Res. 52(5): 726–735.

Goldberg ME, Gorn GJ (1987) Happy and sad TV programs: How they affect reactions to commercials. J. Consumer Res. 14(3):387–403.

Grif<sup>fi</sup>n M, Babin BJ, Modianos D (2000) Shopping values of russian consumers: The impact of habituation in a developing economy. J. Retailing 76(1):33–52.

Hadlington LJ (2015) Cognitive failures in daily life: Exploring the link with Internet addiction and problematic mobile phone use. Comput. Human Behav. 51:75–81.

Hamilton JD (1989) A new approach to the economic analysis of nonstationary time series and the business cycle. Econometrica 57(2):357–384.

Han SP, Park S, Oh W (2016) Mobile app analytics: A multiple discrete-continuous choice framework. Management Inform. Sys tems Quart. 40(4):983–1008.

Heckman J, Singer B (1984) A method for minimizing the impact of distributional assumptions in econometric models for duration data. Econometrica 52(2):271–320.

Hirschman EC (1984) Experience seeking: A subjectivist perspective of consumption. J. Bus. Res. 12(1):115–136.

Janiszewski C (1998) The in<sup>fl</sup>uence of display characteristics on visual exploratory search behavior. J. Consumer Res. 25(3): 290–301.

Jarboe GR, McDaniel CD (1987) A pro<sup>fi</sup>le of browsers in regional shopping malls. J. Acad. Marketing Sci. 15(1):46–53.

Laurent G, Kapferer JN (1985) Measuring consumer involvement pro<sup>fi</sup>les. J. Marketing Res. 22(1):41–53.

Luo L, Ratchford BT, Yang B (2013) Why we do what we do: A model of activity consumption. J. Marketing Res. 50(1):24–43.

Luo X, Andrews M, Fang Z, Phang CW (2014) Mobile targeting. Management Sci. 60(7):1738–1756.

MacDonald IL, Zucchini W (1997) Hidden Markov and Other Models for Discrete-Valued Time Series (Chapman & Hall/CRC).

Mattila AS, Wirtz J (2001) Congruency of scent and music as a driver of in-store evaluations and behaviour. J. Retailing 77(2): 273–289.

Moe WW (2003) Buying, searching, or browsing: Differentiating between online shoppers using in-store navigational clickstream. J. Consumer Psych. 13(1-2):29–39.

Montgomery AL, Li S, Srinivasan K, Liechty JC (2004) Modeling on line browsing and path analysis using clickstream data. Market ing Sci. 23(4):579–595.

Netzer O, Lattin JM, Srinivasan V (2008) A hidden Markov model of customer relationship dynamics. Marketing Sci. 27(2):185–204.

Park WC, Iyer ES, Smith DC (1989) The effects of situational factors on in-store grocery shopping behavior: The role of store environment and time available for shopping. J. Consumer Res. 15(4):422–433.

Park MH, Park EJ, Choi J, Chai S, Lee JH, Lee C, Kim DJ (2011) preliminary study of internet addiction and cognitive function in adolescents based on IQ tests. Psychiatry Res. 190(2-3):275–281.

Phang CW, Luo X, Fang Z (2019) Mobile time-based targeting: Matching product-value appeal to time of day. J. Management Inform. Systems 36(2):513–545.

Rabiner LR (1989) A tutorial on hidden Markov models and selected applications in speech recognition. Proc. IEEE 77:257–286.

Sedani A, Stover D, Coyle B, Wani RJ (2019) Assessing workplace health and safety strategies, trends, and barriers through a statewide worksite survey. Internat. J. Environ. Res. Public Health 16(4):2475.

Sherry JF, McGrath M, Levy SJ (1993) The dark side of the gift. J. Bus. Res. 28(3):225–245.

Shin C, Hong JH, Dey AK (2012). Understanding and prediction of mobile application use for smart phones. Proc. ACM Conf. on Ubiquitous Comput., 173–182.

Singh PV, Sahoo N, Mukhopadhyay T (2014) How to attract and retain readers in enterprise blogging? Inform. Systems Res. 25(1):35–52.

Singh PV, Tan Y, Youn N (2011) A hidden Markov model of developer learning dynamics in open source software projects. In form. Systems Res. 22(4):790–807.

Sledgianowski D, Kulviwat S (2009) Using social network sites: The effects of playfulness, critical mass and trust in a hedonic context. J. Comput. Inform. Systems 49(4):74–83.

Small GW, Moody TD, Siddarth P, Bookheimer SY (2009) Your brain on Google: Patterns of cerebral activation during internet searching. Amer. J. Geriatric Psychiatry 17(2):116–126.

Spangenberg ER, Grohmann B, Sprott DE (2005) It’s beginning to smell (and sound) a lot like Christmas: The interactive effects of ambient scent and music in a retail setting. J. Bus. Res. 58(11): 1583–1589.

Suri R, Monroe KB (2003) The effects of time constraints on consumers’ judgments of prices and products. J. Consumer Res. 30(1): 92–104.

Voss KE, Spangenberg ER, Grohmann B (2003) Measuring the hedonic and utilitarian dimensions of consumer attitude. J. Marketing Res. 40(3):310–320

Wang YJ, Minor MS, Wei J (2011) Aesthetics and the online shopping environment: Understanding consumer responses. J. Retailing 87(1):46–58.

Xu J, Forman C, Kim JB, Van Ittersum K (2014) News media channels: Complements or substitutes? Evidence from mobile phone use. J. Marketing 78(4):97–112.

Yan L, Tan Y (2014) Feeling blue? Go online: An empirical study of social support among patients. Inform. Systems Res. 25(4): 690–709.

Yang S, Allenby GM, Fennell G (2002) Modeling variation in brand preference: The roles of objective environment and motivating conditions. Marketing Sci. 21(1):14–31.

Yoon C, Lee MP, Danziger S (2007) The effects of optimal time of day on persuasion processes in older adults. Psych. Marketin 24(5):475–495.

Zaichkowsky JL (1985) Measuring the involvement construct. J. Con sumer Res. 12(3):341–352.

Zhang Y, Li B, Luo X, Wang X (2019) Personalized mobile targeting with user engagement stages: Combining a structural hidden markov model and <sup>fi</sup>eld experiment. Inform. Systems Res. 30(3):787–804.

Zheng J, Qi Z, Dou Y, Tan Y (2019) How mega is the mega? Exploring the spillover effects of WeChat using graphical model. In form. Systems Res. 30(4):1343–1362.

Zheng Y, Zhang L, Xie X, Ma WY (2009). Mining interesting locations and travel sequences from GPS trajectories. Proc. 18th Internat. Conf. on World Wide Web, 791–800.

C<sub>opy</sub>ri<sub>g</sub>ht 2022 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
