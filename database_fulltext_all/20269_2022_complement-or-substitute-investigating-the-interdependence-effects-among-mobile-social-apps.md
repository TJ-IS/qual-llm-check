---
otero_id: 20269
otero_key: "Q3TG85X4"
title: "Complement or substitute? Investigating the interdependence effects among mobile social apps"
authors: "Chuang Wang; Shaochun Zheng"
year: "2022"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103362"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Complement or substitute? Investigating the interdependence e<sup>f</sup>ects among mobile social apps

Chuang Wang<sup>a,</sup>\*, Shaochun Zheng

<sup>a</sup> School of Business Administration, South China University of Technology, China <sup>b</sup> School of Business Administration, South China University of Technology, China

## A R T I C L E I N F O

Keywords: Mobile social apps Interdependence e<sup>f</sup>ects Complement Substitute Psychological needs

## A B S T R A C T

Interdependence e<sup>f</sup>ects would arise when individuals consume two or more products simultaneously. However, comprehensive understanding and quantitative analysis of such interdependence e<sup>f</sup>ects in the use of mobile social apps are still limited. The few existing studies mainly considered whether the apps are installed together by unique devices, while the actual usage behaviors are totally ignored. The current study developed an adapted utility function model to quantify the interdependence e<sup>f</sup>ects and found that social apps satisfying users’ different psychological needs would be complementary at most times, while those apps gratifying similar psychological needs would also complement rather than substitute each other

## 1. Introduction

The burgeoning development of the mobile telecommunication industry has shifted conventional social activities to mobile platforms, leading to an explosion of diverse mobile social apps (e.g., Facebook, Twitter, WhatsApp, WeChat). According to Google Play’s report released by App Annie, mobile social apps are the most popular apps in the app market from January 2012 to August 2018 [1]. To satisfy individuals’ diverse psychological needs (e.g., autonomy, relatedness, competence, having a place, and self-identity), a great amount of mobile social apps have sprung up and embraced di<sup>f</sup>erent a<sup>f</sup>ordances and features [2], such as allowing individuals to present themselves, share content, hold conversations, form relationships, and manage groups at any time and any place [2–5]. Overwhelmed by a considerable number of options, users have to select which app to use and decide how much time to spend on each app. Additionally, a report supported by iResearch has revealed that 94.6 % of users embrace two or more mobile social apps [6], which would induce interdependence e<sup>f</sup>ects (i.e., either complementary or substitution e<sup>f</sup>ects) among mobile social apps.

Typically, mobile apps that are simultaneously installed or used by the same users are perceived as competitors (i.e., substitutes of each other), while the possible cooperative relationship (i.e., complements of each other) is always ignored. Nevertheless, for the sake of sustainable development of the mobile social apps market, it is believed that both competitive and cooperative relationships should be taken into account [7,8]. As such, a deep insight into individuals’ usage behaviors and the interdependence e<sup>f</sup>ects among apps is helpful to provide more e<sup>f</sup>ective and strategical products and services for app developers.

In spite of the practical pertinence, the interdependence e<sup>f</sup>ects among mobile social apps have not received su<sup>fi</sup>cient attention either in the marketing literature or in the information systems research, and a thorough understanding is still evolving. To the best of our knowledge, theory-based empirical study on app interdependence is extremely lacking, and the few existing studies either employed the descriptive approach or merely used the co-occurrence on smartphones as a representative to explain the interdependence e<sup>f</sup>ects [7,9,10], while the actual usage behaviors and quanti<sup>fi</sup>ed e<sup>f</sup>ects are totally ignored. Furthermore, previous literature provides contradictory results on the interdependence e<sup>f</sup>ects among mobile apps [9–11]. For instance, using the dependency ratio, Xu, Erman [9] proposed that apps in the same categories are more likely to have correlated usage, and mobile social apps are among the most interdependent genres. In contrast, Huang, Xu [10] claimed that some social apps would be installed together, while others would undermine each other's rate of installation.

To resolve this dilemma, we would like to primarily understand the underlying mechanism of the mobile social apps’ usage – the use of di<sup>f</sup>erent apps is motivated by the grati<sup>fi</sup>cation of di<sup>f</sup>erent sets of psychological needs [2]. Take the example of WhatsApp and Twitter. Although both apps function as mobile social apps, WhatsApp is mainly designed to satisfy users’ need for relatedness and self-identity (i.e., other-focused psychological needs), while Twitter focuses more on the grati<sup>fi</sup>cation of competence needs and autonomy needs (i.e., selffocused psychological needs). Following this line of reasoning, we <sup>fi</sup>rst divide mobile social apps into two subcategories based on users’ psychological needs – instant messaging apps (e.g., WhatsApp and We Chat) that mainly satisfy users’ other-focused psychological needs, and community social apps (e.g., Twitter and Sina Weibo) that mainly gratify users’ self-focused psychological needs. It is further proposed that social apps satisfying users’ similar needs would likely be more substitutive with each other, whereas those apps gratifying di<sup>f</sup>erent needs would be complementary to a large degree.

According to the utility maximization theory, we then use the utility function model to quantify the complementary and substitution e<sup>f</sup>ects among mobile social apps. The basic assumption is that the utility appears and is the ranking of preferences when people consume two or more goods or services [12]. As a rational individual, a user would control each app usage to get the maximum utility in the current period. We also use frequent pattern mining (FPM) to discover the app-sets that are frequently installed together. Only if those apps are concurrently installed by most users, can we monitor and study the interdependence e<sup>f</sup>ects among them by conducting the utility function model. The subset of frequent app-sets thus acts as the dataset of the utility function model. Our data is collected by a third-party application that records the actual usage behaviors of smartphone users.

Our paper makes several theoretical and practical contributions. In terms of theory, the proposed model advances our understanding of how mobile social apps complement or substitute each other through the actual usage behavior. Moreover, our study demonstrates that a more <sup>fi</sup>ne-grained subcategory analysis from the perspective of psychological needs is of necessity to investigate the interdependence effects among social apps. In terms of practice, we provide a comprehensive insight into the interdependence e<sup>f</sup>ects among mobile social apps for app providers, marketers, and operators. Better service design and e<sup>f</sup>ective marketing strategies can be developed by taking advantage of the complementary and substitution e<sup>f</sup>ects among mobile social apps. From this perspective, our study o<sup>f</sup>ers a deep under standing of the sustainable development of mobile social apps.

The rest of this paper is organized as follows. We describe the related literature and theoretical background of the study in Section 2. Next, we describe the adapted utility function model, followed by the empirical validation and the main results. We conclude the paper by discussing the implications of our study and claiming the limitations and future research.

## 2. Literature review and theoretical background

## 2.1. Prior studies of app usage patterns

Previous studies have widely investigated the usage patterns of mobile apps. The three main lines of research lie on app diurnal pat terns, app popularity patterns, and app selection patterns [7,9,10,13,14].

More speci<sup>fi</sup>cally, app diurnal patterns consist of diurnal down loading, updating, and uninstallation distribution of apps, as well as tra<sup>fi</sup>c usage and access time [7,9]. It has been found that the peak time for downloading, updating, and uninstalling apps during the day coincides with people's leisure time after dinner [7]. Importantly, dif ferent app categories have di<sup>f</sup>erent diurnal patterns. For example, Xu, Erman [9] have observed that the weather and news apps are used most frequently in the morning, while sports and games apps peak in the early evening. Consistently, other scholars found that the usage of news apps is active in the early morning from 6 a.m. to 9 a.m., while games apps are used frequently in the evening [15]. The only exception is social network apps, whose diurnal patterns are less visible and more <sup>fl</sup>at during a day [9]. That is to say, social apps are used with a relatively high frequency at all times. Well aligned with this <sup>fi</sup>nding, previous literature has highlighted that mobile social apps act as the predominantly real-time apps that cannot be substituted by other apps

[16,17].

App popularity patterns are also a heated topic in the <sup>fi</sup>eld of app usage patterns research. It has been found that 10 % of the apps account for 70 %−90 % of the total downloads, which indicated the “Pareto e<sup>f</sup>ect” [13]. In addition, a large amount of users would like to down load apps from a single or very few app categories, called the “clustering e<sup>f</sup>ect” [13]. To further illuminate those factors that imply app popularity, Li, Lu [7] proposed two kinds of factors as indicators, that is, the conventional factors like the number of monthly downloads and unique users, and the innovative factors like the network tra<sup>fi</sup>c and the network access time of an app.

Besides diurnal usage patterns and app popularity patterns, app selection patterns have been extensively explored. In the area of app selection patterns, scholars investigated the transition of apps [15,18,19] and co-occurrence of apps (i.e., app interdependence) [7,9,10] in diverse app categories. The research on apps transition mainly studied the app usage chains (i.e., the sequence of apps that are used in a session) [15] and the prediction of the next app in the chains [19]. It has been found that communication apps are the <sup>fi</sup>rst used apps in a session, and there is a great possibility that users would transit to communication apps after they use other apps in a session [15], indicating that communication apps are among the most popular and vital apps.

When it comes to the research of co-occurrence apps, scholars merely explore the installation correlations among apps. For instance, Li, Lu [7] used Jaccard similarity coe<sup>fi</sup>cient to investigate which apps would be installed together and found apps that provided related functionalities or apps that come from the same vendor are more likely to be installed together. Consistently, Xu, Erman [9] found that apps in the same genres are more likely to have a high interdependency ratio, suggesting that apps in the same categories would strengthen each other’s usage. Huang, Xu [10], however, used FPM algorithm to explore app interdependence e<sup>f</sup>ects and found that apps in the social network category do not always strengthen each other’s rate of installation. That is, some mobile social apps are frequently installed together while others undermine each other’s rate of installation.

As a branch of app usage patterns, the research of app selection patterns, especially app interdependence e<sup>f</sup>ects, is still at its nascent stage. Although prior studies have made great contributions to this issue, few of them focused on the actual usage behaviors and quanti<sup>fi</sup>ed their e<sup>f</sup>ects. In addition, to the best of our knowledge, previous lit erature did not clearly articulate the interdependence e<sup>f</sup>ects among mobile apps from a theoretical standpoint and provided contradictory results. Whether the consumption relationships among mobile social apps are complementary or substitutive thus needs further investigation. In the next subsection, we further discuss the conceptualization and theoretical background of interdependence e<sup>f</sup>ects.

## 2.2. Substitution and complementary efects

Substitution and complementary e<sup>f</sup>ects are two types of interdependence e<sup>f</sup>ects. When people consume two products or services simultaneously, either substitution e<sup>f</sup>ect or complementary e<sup>f</sup>ect exists [20]. Extending this point to the mobile context, scholars have demonstrated that substitution or complementary e<sup>f</sup>ect occurs when people consume diverse mobile apps [11]. In this study, substitution efect refers to the use of an app that would undermine the use of another app, and complementary efect indicates that two apps would strengthen the use of each other when users consume them simultaneously.

Following this line of de<sup>fi</sup>nition, we further attribute the substitution e<sup>f</sup>ect in mobile social context to the economic behaviors under resource constraints (e.g., time, attention). Acting as a critical constraint, time plays an important role in individuals decision-making as well as consumption behavior [21–25] and is the crucial resource for which all media compete [25]. This is mainly because users have to decide how to allocate their limited time to diverse mobile apps. When users spend a high amount of time on one mobile app, the time left for other mobile apps might be relatively little. Furthermore, <sup>fi</sup>nite attention also acts as a constraint [26] in the use of mobile social apps, because it is the most vital and scarce resource online [27–29]. With a large amount of social apps, the abundant information users are ex posed to through social network services exceeds the capacity to con sume, and thus readily and vulnerably leads to information overload and social overload. Given that the abundance of information creates the competition for attention [30], individuals have to allocate their attention to a substantial number of social apps, which results in the substitution e<sup>f</sup>ect among social apps.

In contrast to this assumption, it is also postulated that a high level of consumption of one mobile social app may motivate other apps’ consumptions, indicating the complementary e<sup>f</sup>ect among di<sup>f</sup>erent mobile social apps. One possible reason for this mutual complement is that mobile social networking platforms always establish various links with diverse apps to meet the needs of heterogeneous users [31]. For instance, they allow users to jump to other mobile social apps via web links, encourage users to share information on other mobile social platforms, and so forth. These interactive measures make it easier for users to switch from one mobile social app to another. When sharing other apps’ contents or consumption information on the current app, users’ behaviors serve as a promotional activity and inform other individuals about the ecosystem of the application [31]. From this per spective, the promotional capability of the social network would increase product adoptions [32]. Furthermore, it has been highlighted that individual’s usage behavior is positively in<sup>fl</sup>uenced by their social network neighbors [33–35]. When users <sup>fi</sup>nd the recommended information from other mobile social apps on their social networking groups or friends’ home page, they are more likely to have a try as well. Therefore, mobile social apps may complement each other.

## 2.3. Psychological needs in the mobile social apps context

The divergent theoretical bases lead to a dilemma in understanding the interdependence e<sup>f</sup>ects among mobile social apps. To resolve this inconsistency, we would like to further discuss this issue from the lens of psychological needs. Unlike the theoretical bases above, needs-based theories focus more on the intrinsic motivations of individuals and thus transcend contexts. As everyone has innate psychological needs [36], needs grati<sup>fi</sup>cation is a powerful lens to explain why individuals use mobile apps as well as the diverse mobile app usage behaviors. Because innate psychological needs provide strong motivations to individuals’ usage behaviors, it has been proposed that the use of mobile apps is motivated by di<sup>f</sup>erent sets of innate psychological needs [2,37]. For instance, it has been con<sup>fi</sup>rmed that the satisfaction of need for relat edness motivates the use of Facebook [38].

By synthesizing self-determination theory and psychological ownership theory, scholars have identi<sup>fi</sup>ed <sup>fi</sup>ve salient psychological needs in the social media context, that is, need for autonomy, need for com petence, need for relatedness, need for having a place, and need for self identity [2]. The de<sup>fi</sup>nitions are presented in Table 1.Table 1

Generally, basic psychological needs can be conceived as a duality, that is, self-focused and other-focused [2,43]. Self-focused psychological needs are those that individuals strive for themselves, while otherfocused psychological needs indicate those that are focused on the relationships between individuals and others. In the social media context, Karahanna, Xu [2] proposed that self-focused needs mainly include the need for autonomy, need for competence, need for having a place, and need for self-identity; other-focused needs that are salient in the social media context include need for relatedness and one aspect of self identity (i.e., expressing self-identity).

Considering the di<sup>f</sup>erent psychological needs of social apps use, we then divide mobile social apps into two main subcategories, that is, instant messaging apps and community social apps. Speci<sup>fi</sup>cally, it is believed that instant messaging apps mainly satisfy other-focused psychological needs, while community social apps satisfy self-focused psychological needs [2]. Motivated by di<sup>f</sup>erent psychological needs, individuals use instant messaging apps to manage the relationships between themselves and others, and use community social apps to strive for self-enhancement. Accordingly, it is assumed that social apps satisfying users’ similar needs would probably be more substitutive with each other, whereas those apps gratifying di<sup>f</sup>erent needs would be complementary to a large extent. In this case, it is more appropriate to investigate the interdependence e<sup>f</sup>ects of mobile apps based on a more <sup>fi</sup>ne-grained psychological need, rather than the traditional classi<sup>fi</sup>cation based on general categories of mobile apps.

## 3. Analytical model

In this study, we use the utility model to analyze the app complementary and substitution e<sup>f</sup>ects. It is widely known that utility is the ranking of preferences. The individual’s ranking of two goods can be represented by a utility function of the form

utility U( , ; )= x x other things ,

where x and x refer to the consumption quantity of two goods respectively, and the “other things’’ notation “is used as a reminder that many aspects of individual welfare are being held constant in the analysis [12]”.

Considering the mobile app usage context, the utility of an individual at any time depends on the consumption (i.e., the usage time) of two apps. In addition, the habit forming theory has highlighted that an individual’s current utility depends on his/her past consumption patterns [44]. Hence, we consider the past consumption of the two apps into the function, and the utility of user i in period t is given by a concave utility function, as shown in Eqn 1.

$$
U _ {i, t} = U (C _ {i, t}, S _ {i, t}, Y _ {i, t}, X _ {i, t}),\tag{1}
$$

where $C _ { i , t }$ is the current consumption of user i on app $\mathsf { A } , S _ { i , t }$ is the past consumption of user i on app $\mathrm { A } , Y _ { i , t }$ is the current consumption of user i on app B, and $X _ { i , t }$ is the past consumption of user i on app B. Speci<sup>fi</sup>- cally, current consumption means the time spent on app A or app B by user i in period t, and each period represents a day.

As for the past consumption, we regard the consumption in period t-1 as the representative of past consumption; neither $S _ { i , t }$ nor $X _ { i , t }$ contains the more distant past consumption. This is mainly because in the utility function, “consumption in the previous period in<sup>fl</sup>uences current preference and demand, but that consumption in the more distant past does not [44].” The habit-forming theory also stated that “only one previous period is enough to indicate a habit-forming property [45].” If we add too many variables of past periods “without much addition to the economic content,” the model would become a tedious mathema tical problem [45]. Hence, it is assumed that $S _ { i , t } = C _ { i , t - }$ <sub>1</sub> and $X _ { i , t } ~ = ~ Y _ { i , t - 1 }$

Table 1  
Salient Psychological Needs in Social Apps Context.

<table><tr><td>Psychological Needs</td><td>Definitions</td></tr><tr><td>Autonomy</td><td>Need for autonomy is the psychological need to act in harmony with one&#x27;s true self, and to engage in activities that obey their genuine desires and preferences [36].</td></tr><tr><td>Competence</td><td>Need for competence is the psychological need to be confident and effective in action and feel capable of performing tasks [36,39,40].</td></tr><tr><td>Relatedness</td><td>Need for relatedness is the psychological need to interact with others, care for, and be cared for [36,41].</td></tr><tr><td>Having a place</td><td>Need for having a place is the psychological need of innate territoriality [42].</td></tr><tr><td>Self-identity</td><td>Need for self-identity is the psychological need to define oneself and have a clear sense of oneself [42]. Specifically, there are three aspects of need for self-identity [42]: coming to know the self, expressing self-identity, and maintaining continuity of self-identity.</td></tr></table>

Using second-order Taylor polynomial to expand Eq. (1), we get Eqn 2:

$$
\begin{array}{r l} U _ {i, t} = & U _ {c} C _ {i, t} + U _ {s} S _ {i, t} + U _ {y} Y _ {i, t} + U _ {x} X _ {i, t} + U _ {c c} C _ {i, t} ^ {2} / 2 + U _ {s s} S _ {i, t} ^ {2} / 2 + U _ {y y} Y _ {i, t} ^ {2} / 2 \\ & + U _ {x x} X _ {i, t} ^ {2} / 2 + U _ {c s} C _ {i, t} S _ {i, t} + U _ {c y} C _ {i, t} Y _ {i, t} + U _ {c x} C _ {i, t} X _ {i, t} + U _ {s y} S _ {i, t} Y _ {i, t} \\ & + U _ {s x} S _ {i, t} X _ {i, t} + U _ {y x} Y _ {i, t} X _ {i, t} \end{array} \tag {2}\tag{2}
$$

U is the <sup>fi</sup>rst-order partial derivative of Eq. (1) with respect to $C _ { i , t } . U _ { c c }$ <sub>c</sub> is the second-order partial derivative of Eq. (1) with respect to $C _ { i , t } . U _ { c s }$ is the second-order partial derivative of Eq. (1) with respect to $C _ { i , t }$ and $S _ { i , t } .$ The rest may be deduced by analogy.

It is important to note that habit-forming is unable to explain the intertemporal consumption relationships between the two apps. Furthermore, given that resource constraints are unobvious in di<sup>f</sup>erent periods, the intertemporal consumption of two apps seems to be independent. Therefore, it is concluded that $C _ { i , t }$ is irrelevant to $X _ { i , t }$ $( U _ { c x } = 0 )$ , and $Y _ { i , t }$ is irrelevant to $S _ { i , t } ~ ( U _ { s y } = 0 )$ , so that Eq. (2) can be expressed likeEqn 3:

$$
\begin{array}{r l} U _ {i, t} = & U _ {c} C _ {i, t} + U _ {s} S _ {i, t} + U _ {y} Y _ {i, t} + U _ {x} X _ {i, t} + U _ {c c} C _ {i, t} ^ {2} / 2 + U _ {s s} S _ {i, t} ^ {2} / 2 + U _ {y y} Y _ {i, t} ^ {2} / 2 \\ & + U _ {x x} X _ {i, t} ^ {2} / 2 + U _ {c s} C _ {i, t} S _ {i, t} + U _ {c y} C _ {i, t} Y _ {i, t} + U _ {s x} S _ {i, t} X _ {i, t} + U _ {y x} Y _ {i, t} X _ {i, t} \end{array} \tag {3}\tag{3}
$$

According to the rational person hypothesis, users will maximize their lifetime utility, and we can getEqn 4:

$$
M a x \sum_ {t = 1} ^ {\infty} \beta^ {t - 1} U (C _ {i, t}, S _ {i, t}, Y _ {i, t}, X _ {i, t}),\tag{4}
$$

where $\beta = 1 / ( 1 { + } \mathrm { r } ) ,$ , and r is the time preference.

It has been highlighted that a consumer s marginal utility di minishes as the level of consumption of any particular app increases–a phenomenon known as satiation [11].” Therefore, it is believed that the consumption of mobile social apps also obeys the law of diminishing marginal utility. In other words, the more time users spend on an app, the less utility they would gain from the additional unit of consumption. As a result, the second-order partial derivative of utility function with respect to $C _ { i , t }$ is negative, and the utility function is a natural concave function in $C _ { i , t } .$ . We thus use the <sup>fi</sup>rst-order condition to solve the utility maximization issue. Perform the <sup>fi</sup>rst derivative of $C _ { i , t }$ for the utility function of user i at time t and time $\mathrm { ~ t ~ } + \mathrm { ~ 1 ~ }$ , and we get Eqn 5:

$$
\frac {\partial U (C _ {i , t} , S _ {i , t} , Y _ {i , t} , X _ {i , t})}{\partial C _ {i , t}} + \frac {\beta \partial U (C _ {i , t + 1} , S _ {i , t + 1} , Y _ {i , t + 1} , X _ {i , t + 1})}{\partial C _ {i , t}} = 0.\tag{5}
$$

By calculating and transforming Eq. (5), we can get a linear equation function Eqn 6 that represents the linear relationship among the current consumption of app A, the past consumption of app A, the future consumption of app A, and the current consumption of app B:

$$
C _ {i, t} = \delta_ {0} + \delta_ {1} C _ {i, t - 1} + \delta_ {2} C _ {i, t + 1} + \delta_ {3} Y _ {i, t} + \mu_ {i} + \varepsilon_ {i, t}\tag{6}
$$

where δ U βU U βU= − + ⁄ +( ) ( ), δ U U βU= − +/( ), $\delta _ { 2 } = - \beta U _ { c s } / ( U _ { c c } + \beta U _ { s s } ) , ~ \delta _ { 3 } = - ( U _ { c y } + \beta U _ { s x } ) / ( U _ { c c } + \beta U _ { s s } ) , ~ \mu _ { \mathrm { i } }$ is the <sup>fi</sup>xed e<sup>f</sup>ect of individual i, and $\varepsilon _ { \mathrm { i , t } }$ is the disturbance term. It is noteworthy that Eq. (6) is an econometric model derived from the utility max imization framework (i.e., the economic model). Thus, $\mu _ { \mathrm { i } }$ is added be cause individual heterogeneity cannot be ignored in the econometric model; $\varepsilon _ { \mathrm { i , t } }$ is added into the econometric model to deal with variable that cannot be reasonably observed.

Importantly, we mainly focus on the coe<sup>fi</sup>cient of $Y _ { i , t }$ in the current study. If $\delta _ { 3 } > 0 ,$ , it implies that the use of app B will increase the use of app A, indicating the complementary e<sup>f</sup>ect. If $\begin{array} { r } { \dot { } \delta _ { 3 } < 0 , } \end{array}$ higher use of app B will induce lower use of app A, indicating the substitution e<sup>f</sup>ect.

## 4. Empirical validation

## 4.1. Empirical context and data description

The dataset of this study was provided by an application that records the usage behaviors of smartphone users in China. We collected the panel dataset consisting of information such as usage time and usage duration. Four top instant messaging apps (i.e., WeChat, QQ, MiTalk, and EasyChat) and four top community social apps (i.e., Sina Weibo, Zhihu, Douban, and Jike) in the Chinese mobile apps market are chosen as the research context.

To empirically validate our research model, we <sup>fi</sup>rst conduct FPM to <sup>fi</sup>nd the apps that are used by most users and frequently installed together (i.e., frequent app-sets). In this part, our dataset, which is denoted as D1, contains the user id, app name, and usage time of the eight mobile social apps $( \mathrm { i . e . , }$ , WeChat, QQ, MiTalk, EasyChat, Sina Weibo, Zhihu, Douban, and Jike) from January 9, 2016 to August 14, 2016. Next, we use the utility function model to analyze the interdependence e<sup>f</sup>ects of these co-occurrence apps that are discovered in the FPM. In this part, our dataset is the subset of the frequent app-sets discovered in the <sup>fi</sup>rst step. The dataset in this part is a dynamic unbalanced panel, involving 1878 panel members and including user id, app name, usage time, and usage duration.

## 4.2. Extract frequent app-sets

Importantly, the premise of the utility function model is that the apps should have a high level of co-occurrence probability. In other words, only if the apps are concurrently installed by most users, can we monitor and study the interdependence e<sup>f</sup>ects among them by conducting the utility function model. Thus, in this part, we will use FPM algorithms to <sup>fi</sup>nd the apps that are used by most users and frequently installed together.

## 4.2.1. Frequent pattern mining

Frequent pattern mining has been widely used in the data mining domain over a decade. FPM was <sup>fi</sup>rst proposed by Agrawal and Imielinski [46], who use the methodology to mine association rules of market basket data. Frequent patterns refer to “itemsets, subsequences, or substructures that appear in a dataset with frequency no less than a user-speci<sup>fi</sup>ed threshold [47].” Thus, FPM can help <sup>fi</sup>nd associations, correlations, and other patterns among data, as it consists of the research of association rules and correlation rules [48].

Let $I = ( I _ { 1 } , I _ { 2 } , \ldots , I _ { m } )$ be a set of all items. T is a nonempty itemset and refers to the transaction. In the traditional market basket context, each transaction contains items purchased by a consumer in a visit to the supermarket [46]. D is a database of transactions T. Both A and B are itemsets, and $\mathrm { A C \ I , B C \ I , A \cap B = \emptyset }$

Association rules are thus expressed as $A \Rightarrow B .$ . In FPM, Support and Con<sup>fi</sup>dence are vital metrics to generate association rules. Support is de<sup>fi</sup>ned as the percentage of transactions in transaction database D that contain both A and B, which is denoted as $S ( A \Rightarrow B )$ . Confidence refers to the percentage of transactions in transaction database D containing A that also contain B, which is denoted as $C \left( A \Rightarrow B \right)$ [48]. Because $\mathbf { A } \cap \mathbf { B } = \mathbf { \nabla } \emptyset$ , the probability that A and B appear simultaneously is P( A B)∪ . In the market basket context, for instance, if $S ( A \Rightarrow B ) = 0 . 2 $ and $C ( A \Rightarrow B ) = 0 . 3 _ { ! }$ , it means that 20 % of the consumers would purchase both A and B in a visit, and 30 % of those who have purchased A would also purchase B. The expressions of support and con<sup>fi</sup>dence are shown as follows.

$$
S (A \Rightarrow B) = P (A \cup B)
$$

$$
C (A \Rightarrow B) = P (B | A) = \frac {P (A \cup B)}{P (A)}
$$

A valid association rule would satisfy both the minimum support threshold and minimum con<sup>fi</sup>dence threshold. We use support to <sup>fi</sup>nd the frequent itemsets and use both support and con<sup>fi</sup>dence to generate association rules. With the given minimum support threshold $S _ { m i n } , \left( \mathsf { A } , \right.$ B) is a frequent itemset if it satis<sup>fi</sup>es $S ( A \Rightarrow B ) > S _ { m i n }$ . Given the minimum con<sup>fi</sup>dence threshold $C _ { m i n } , \quad \mathrm { i f } \quad \left( \mathrm { A } , \quad \mathrm { B } \right)$ also satis<sup>fi</sup>es $C ( A \Rightarrow B ) > C _ { m i n } ,$ , it is believed that $A \Rightarrow B$ is a valid association rule.

The basic de<sup>fi</sup>nitions are shown as follows in the mobile app context. Let $I = ( I _ { 1 } , I _ { 2 , \cdots , I _ { m } } )$ be a set of all apps in the dataset that we get, where I refers to an app and $\mathrm { i } = ( 1 , ~ 2 , ~ . . . , \mathrm { m } )$ . Both A and B refer to appsets. An app-set that contains k apps is a k-itemset $( k \leq m )$ . For instance, the set {WeChat, QQ} is a 2-itemset. If the k-itemset is a frequent itemset, it means that the apps of the set are frequently installed by users.

In order to mine interesting rules and avoid useless rules due to the low support threshold, a correlation measure has been used to strengthen the association rules. The correlation measures are di<sup>f</sup>erent, such as lift, λ<sup>2</sup>, cosine, and all-con<sup>fi</sup>dence [47]. We use the lift value in the current study, and de<sup>fi</sup>ne it as follows:

$$
L (A, B) = \frac {P (A U B)}{P (A) P (B)} = \frac {C (A \Rightarrow B)}{S (B)}
$$

In the context of mobile apps use, A and B represent two app-sets, respectively. $\begin{array} { r } { \mathrm { I f } \ L ( A , B ) > 1 , } \end{array}$ , it suggests that the installation of app-set A would promote the installation of app-set B. If $\because L ( A , B ) < 1 ,$ , it indicate that the installation of app-set A would undermine the installation of app-set B.

## 4.2.2. Results of frequent pattern mining

Next, we use the FPM algorithm to <sup>fi</sup>nd the apps that are used by most of the users and frequently installed together. Speci<sup>fi</sup>cally, we use the Apriori algorithm, which is proposed by Agrawal and Srikant [49]. Our itemset is I {WeChat, QQ, MiTalk, EasyChat= , Sina Weibo, Zhihu, Douban, Jike}, and we set 0.1 as the minimum support and 0.3 as the minimum con<sup>fi</sup>dence. The 1-itemsets that satisfy the minimum support (i.e., frequent itemsets) are {WeChat}, {QQ}, {Sina Weibo}, and {Zhihu}, which suggests that more than 10 % of the users use WeChat, QQ, Sina Weibo, and Zhihu. As the users of the other four apps are less than 10 % and the usage data would be relatively small, they are removed from our dataset. In the frequent itemsets, we mined the itemsets that satisfy the minimum con<sup>fi</sup>dence and calculated the lift value. The results are given in Tables 2 and 3.Table 2 and 3

The results of Table 2 indicate that 93.2 % of the users who install Zhihu will install WeChat, and 93.0 % of the users who install Sina Weibo will install WeChat, suggesting the dominant position of WeChat in the Chinese mobile social app market. In addition, the association rules of QQ WeCha⇒ t, Sina Weibo Q⇒ Q, Zhihu Q⇒ Q, and WeChat Q⇒ Q with the con<sup>fi</sup>dence range from 0.6 to 0.8; and the association rules of Zhihu Sina Weibo⇒ , QQ Sina Weibo⇒ , WeChat Sina Weibo⇒ , and Sina Weibo Zhih⇒ u with the con<sup>fi</sup>dence range from 0.4 to 0.6; the con<sup>fi</sup>dence of $\mathrm { Q Q } { \Rightarrow } \mathrm { Z h i h u }$ , as well as WeChat Zhih⇒ u, is lower than 0.4.

Con<sup>fi</sup>dence of Frequent App-Sets.

<table><tr><td>A</td><td>B</td><td>C ( A⇒ B)</td></tr><tr><td>Zhihu</td><td>WeChat</td><td>0.932</td></tr><tr><td>Sina Weibo</td><td>WeChat</td><td>0.930</td></tr><tr><td>QQ</td><td>WeChat</td><td>0.883</td></tr><tr><td>Sina Weibo</td><td>QQ</td><td>0.869</td></tr><tr><td>Zhihu</td><td>QQ</td><td>0.853</td></tr><tr><td>WeChat</td><td>QQ</td><td>0.796</td></tr><tr><td>Zhihu</td><td>Sina Weibo</td><td>0.596</td></tr><tr><td>QQ</td><td>Sina Weibo</td><td>0.493</td></tr><tr><td>WeChat</td><td>Sina Weibo</td><td>0.475</td></tr><tr><td>Sina Weibo</td><td>Zhihu</td><td>0.405</td></tr><tr><td>QQ</td><td>Zhihu</td><td>0.329</td></tr><tr><td>WeChat</td><td>Zhihu</td><td>0.324</td></tr></table>

Table 3  
Lift Values and Correlation Rules.

<table><tr><td></td><td>WeChat</td><td>QQ</td><td>Sina Weibo</td><td>Zhihu</td></tr><tr><td>WeChat</td><td>\</td><td>-</td><td>+</td><td>+</td></tr><tr><td>QQ</td><td>0.991</td><td>\</td><td>+</td><td>+</td></tr><tr><td>Sina Weibo</td><td>1.044</td><td>1.083</td><td>\</td><td>+</td></tr><tr><td>Zhihu</td><td>1.046</td><td>1.063</td><td>1.308</td><td>\</td></tr></table>

According to the results given in Table 3, the lift values among the four apps are all greater than 1, except for WeChat and QQ (L(WeChat, $\mathrm { Q Q } ) = 0 . 9 9 1 < 1 )$ . Therefore, WeChat and QQ would undermine each other’s installation rate at a relatively low level and are infrequently installed together by users, indicating the potential substitution e<sup>f</sup>ect between these two social apps.

Interestingly, the lift value between Sina Weibo and Zhihu is higher than 1, illuminating that community social apps are frequently installed together. This result indicates a potential complementary e<sup>f</sup>ect among these two apps.

The results also suggest that instant messaging apps and community social apps would strengthen each other’s rate of installation. This may be because users use instant messaging apps to contact and maintain their relationship with others (i.e., satisfy other-focused psychological needs), and use community social apps to engage in activities that help <sup>fi</sup>nd their integrated self (i.e., satisfy self-focused psychological needs).

To summarize, the results of FPM help understand whether the mobile social apps are installed together, but do not inform the speci<sup>fi</sup>c usage relationships among apps. Next, we use the utility function model to quantify the interdependence e<sup>f</sup>ects among apps.

## 4.3. Main results

In this part, we use the system generalized method of moments (GMM) to empirically analyze the panel data. The dataset in this part is the subset of D1, and we explore only the usage relationships among the frequent app-sets discovered by FPM. There are several missing values of usage consumption; thus, we replace the missing values with zero and then conduct the log(x+1) transition. The analytical model is shown in Eq. (6). Table 4 shows the main results obtained from the system GMM.

First and foremost, the results indicate that the use of instant messaging apps and community social apps is complementary. More speci<sup>fi</sup>cally, an increase of 1% in the usage time of WeChat corresponded with an increase of 0.026 % and 0.023 % in the usage time of Sina Weibo and Zhihu, respectively; an increase of 1 % in the usage time of QQ corresponded with an increase of 0.029 % and 0.020 % in the usage time of Sina Weibo and Zhihu, respectively; an increase of 1 % in the usage time of Sina Weibo corresponded with an increase of 0.032 % and 0.019 % in the usage time of WeChat and QQ, respectively; and an

## Table 4

System GMM Estimates (mainly shows the value of δ ).

<table><tr><td>DVIV</td><td>log_WeChat</td><td>log_QQ</td><td>log_Sina Weibo</td><td>log_Zhihu</td></tr><tr><td>log_WeChat</td><td>\</td><td>0.052***</td><td>0.026**</td><td>0.023*</td></tr><tr><td>log_QQ</td><td>0.037***</td><td>\</td><td>0.029***</td><td>0.020**</td></tr><tr><td>log_Sina Weibo</td><td>0.032***</td><td>0.019**</td><td>\</td><td>0.030***</td></tr><tr><td>log_Zhihu</td><td>0.028***</td><td>0.038***</td><td>0.031***</td><td>\</td></tr></table>

Note: $\mathrm { ^ { \ast \ddag } \mathrm { ~ p < 0 . 0 0 1 , ~ \mathrm { ^ { \ast \ast } \mathrm { ~ p < 0 . 0 1 , ~ \mathrm { ^ { \ast } \mathrm { ~ p < 0 . 0 5 . ~ D V } } } } } }$ are dependent variables, IV are independent variables, The number of observations is 23567, and the number of groups is 1878.

increase of 1% usage time of Zhihu would correspond with an increase 0.028 % and 0.038 % in the usage time of WeChat and QQ, respec tively.

Unexpectedly, the usage relationships between WeChat and QQ are signi<sup>fi</sup>cantly positive $( \delta _ { 3 } = 0 . 0 3 7 \mathrm { o r } \delta _ { 3 } = 0 . 0 5 2 )$ . That is, although most users would not install WeChat and QQ together $\mathrm { ( L ( W e C h a t , ~ Q Q ) = 0 . 9 9 1 < 1 ) }$ , their actual usage is complementary. Furthermore, unlike our previous assumption, the usage relationships among community social apps are also statistically signi<sup>fi</sup>cant $( \delta _ { 3 } = 0 . 0 3 1 \mathrm { o r } \delta _ { 3 } = 0 . 0 3 0 )$ . To summarize, our results indicate that mo bile social apps that satisfy similar psychological needs of users are complementary with each other, rather than the expected substitution e<sup>f</sup>ect.

## 5. Discussion

In this study, we aim to theoretically examine and empirically quantify the interdependence e<sup>f</sup>ects among mobile social apps. Given that an increasing number of apps have a social feature, it is more appropriate to investigate the interdependence e<sup>f</sup>ects in a <sup>fi</sup>ne-grained subcategory. Hence, we mainly divide mobile social apps into two genres (i.e., instant messaging apps and community social apps) through the lens of psychological needs. We conduct FPM to <sup>fi</sup>nd the social apps that are frequently installed together, and then use the utility function model to quantify the app complementary and sub stitution e<sup>f</sup>ects. The results have interesting implications.

## 5.1. Key findings

Firstly, instant messaging apps and community social apps are in stalled together by a large number of users and also complement each other in the usage time, indicating that apps in di<sup>f</sup>erent subcategories gratifying di<sup>f</sup>erent psychological needs would be complementary at most times.

However, the usage relationships intra instant messaging apps and community social apps are relatively more intertwined. Contrasted with our previous assumption, the relationship between the consumption of Sina Weibo and Zhihu is signi<sup>fi</sup>cantly positive, suggesting that social apps satisfying users’ similar needs complement each other rather than the substitution e<sup>f</sup>ect. This <sup>fi</sup>nding is counterintuitive and invites fur ther exploration. One potential explanation is that although both Sina Weibo and Zhihu satisfy users’ self-focused needs (e.g., autonomy, competence, having a place, coming to know the self, maintaining continuity of self-identity, expressing self-identity), they di<sup>f</sup>er in their product orientation and market positioning, and thus have di<sup>f</sup>erent a<sup>f</sup>ordances and features. More speci<sup>fi</sup>cally, Sina Weibo aims to help people discover what is going on in the world at any time and place, as well as share what they would like to express, while Zhihu is devoted to building a reliable community of questioning and answering. From this perspective, although these two apps gratify users’ similar needs, they might not be substitutive with each other. As a result, a higher use of Sina Weibo would not undermine the use of Zhihu, and vice versa.

More interestingly, the actual usage relationship among instant messaging apps is signi<sup>fi</sup>cantly positive, although the installation among them is substitutive. In other words, the more the use of WeChat/QQ, the more the use of QQ/WeChat. The critical explanation for this complementary e<sup>f</sup>ect might also be further explained by the di<sup>f</sup>erences in the a<sup>f</sup>ordances and features of these two apps. According to the needs-a<sup>f</sup>ordances-features perspective proposed by Karahanna, Xu [2], the a<sup>f</sup>ordances that mobile apps provide help ful<sup>fi</sup>ll individuals psychological needs. Although both WeChat and QQ are designed to satisfy individuals’ need for relatedness, WeChat focuses more on crossplatform communication integration, whereas QQ concentrates on the communication itself. Hence, WeChat and QQ embrace di<sup>f</sup>erent com binations of a<sup>f</sup>ordances to ful<sup>fi</sup>ll individuals’ other-focused psycholo gical needs. Speci<sup>fi</sup>cally, through the use of QQ, individuals always chat with their friends in real-time with the a<sup>f</sup>ordance of presence signaling to ensure that users can “know if other users are accessible”. In addition, a great majority of friends on QQ are real-world friends and acquaintances, and thus the main reason to use QQ is to maintain strongtie relationships. Unlike QQ, WeChat does not have the a<sup>f</sup>ordance of presence signaling, and thus users cannot know if other users are accessible online. Users of WeChat are thus expected to be online at all times and able to respond in time. From this perspective, although WeChat and QQ satisfy individuals’ similar psychological needs, the di<sup>f</sup>erent a<sup>f</sup>ordances of the two apps provide distinct usage experiences for users. Hence, WeChat and QQ might not be substitutive in the actual usage behavior.

Furthermore, the results illuminate that only the installation could not re<sup>fl</sup>ect the actual usage relationships. Although the majority of users believe that one instant messaging app is enough to satisfy their interpersonal needs and would not both install WeChat and QQ $\mathrm { ( L ( W e C h a t , ~ Q Q ) = 0 . 9 9 1 < 1 ) }$ , the users who have installed them together are found that a higher level of WeChat/QQ use would strengthen a higher level of QQ/WeChat use. One critical explanation for this might be that the installation simply indicates the usage intention, instead of the actual usage behaviors. From this perspective, the utility function model provides more comprehensive and objective results than traditional FPM.

## 5.2. Theoretical and practical implications

Our study makes several contributions to both theory and practice. First, we o<sup>f</sup>er a deep insight into the understanding of interdependence e<sup>f</sup>ects among mobile social apps. From the perspective of psychological needs, we theoretically explain individuals’ usage behaviors and the interdependence e<sup>f</sup>ects among apps [2,37,50]. Our results have demonstrated a previous assumption, that is, social apps gratifying different psychological needs would be complementary at most time. However, the interdependence e<sup>f</sup>ects among those apps satisfying users’ similar psychological needs would also complement each other, instead of the expected substitution e<sup>f</sup>ect. We further explain thi puzzle through the needs-a<sup>f</sup>ordances-features framework by discussing the relationship between needs and a<sup>f</sup>ordances/features [2]. That is, although social apps satisfy users’ similar needs (e.g., autonomy, competence), they might di<sup>f</sup>er in their speci<sup>fi</sup>c a<sup>f</sup>ordances and features, as well as product orientation and market positioning. In this case, it is believed that we should investigate mobile social app interdependence e<sup>f</sup>ects in a more <sup>fi</sup>ne-grained subcategory. Given that increasing apps embrace social features and a broader genre of social apps has appeared, our study indicates that analyzing mobile social app usage behaviors in the subcategories is imperative. Hence, our work not only complements the study of app interdependence, but also provides a new way for social networking research.

Second, we advance our understanding on how mobile social apps complement and substitute each other based on actual usage behaviors. In the limited literature of app interdependence, the majority of research explained this issue from the perspective of app installation, and little e<sup>f</sup>ort has been devoted to investigating individuals’ actual usage behaviors. The proposed utility function model helps us understand how much the increased/decreased consumption of the current mobile social app would result from the usage of other mobile social apps, which is more objective, accurate, and quanti<sup>fi</sup>ed.

The <sup>fi</sup>ndings of this study also provide a comprehensive insight into the complementary and substitution e<sup>f</sup>ects among mobile social apps for app providers, marketers, and operators. Importantly, it should be noted that the actual usage behavior rather than the initial installation is more e<sup>f</sup>ective for service providers to capture the interdependence e<sup>f</sup>ects among mobile apps. In addition, better design and marketing strategies can be made by taking advantage of the complementary and substitution e<sup>f</sup>ects. For instance, the apps in the same subcategory can embrace di<sup>f</sup>erent a<sup>f</sup>ordances and features, and thus avoid homogeneous competition. Given that a<sup>f</sup>ordances are enabled by speci<sup>fi</sup>c features [51], app providers can design diverse features to provide the a<sup>f</sup>ordances that ful<sup>fi</sup>ll the needs, and thus distinguish their apps from each other.

Additionally, unlike the previous interpretation of app popularity/ app competitiveness through downloads, number of unique devices, network tra<sup>fi</sup>c, and network access time [7,8], our study proposes a new way (i.e., complementary and substitution e<sup>f</sup>ects) to explain this issue. For instance, if an app can be complemented by all other apps, the app is relatively more competitive. On the contrary, if an app is readily substituted by other apps, the app is less competitive. By doing so, app providers would have a deep understanding of their apps market position.

Last but not the least, our study provides a deep understanding of the sustainable development of mobile social apps. According to the World Commission on Environment and Development, sustainability development is de<sup>fi</sup>ned as “development that meets the needs of the present without compromising the ability of future generations to meet their own needs” [52]. Following this line of de<sup>fi</sup>nition, the United Nations Commission on Sustainable Development (CSD) proposed that the progress made toward sustainability development could be measured by four aspects, including social, environment, economic, and institutional issues [53].

Based on our <sup>fi</sup>ndings, although mobile social apps seem to be competitors in the market, win-win cooperation should be encouraged among those service providers. Establishing a close cooperative relationship is conducive to the sustainability development of the mobile social apps market, which is consistent with the more promising consumption and production patterns in economics [53]. To improve the market penetration and ensure sustainable development, app operators could leverage the complementary e<sup>f</sup>ect and seek win-win cooperation among their seeming “competitors”; for example, designing APIs (i.e., Application Program Interface) to bridge mutual complementary apps, allowing the complementary apps to freely navigate to their own apps, and so forth.

Furthermore, our results indicate that individuals will inevitably engage in an increasing use of their mobile social apps given the complementary e<sup>f</sup>ect of the actual usage behavior. It is further believed that such excessive use will impede the sustainability development to individuals themselves due to potential negative outcomes. More speci<sup>fi</sup>cally, as shown in the results of the utility function model, the use of one mobile social app would strengthen the use of another. That is, users may increase their total usage time and even excessively use their mobile social apps [54]. It has been found that excessive use of mobile social apps exacerbates family, work, and personal con<sup>fl</sup>icts, indicating a con<sup>fl</sup>ict between family tasks/ work tasks/ health and physical pro blems and the use of mobile social apps [55]. In a consistent manner, scholars have recognized that the increased use of mobile social apps would not only give rise to lesser time devoted to family activities and work, but also bring about personal health problems such as eyestrain, backaches, carpal tunnel syndrome, and chronic sleep deprivation [55,56]. From this perspective, the complementary use of multiple mobile social apps would result in negative consequences and impede individuals’ sustainable development in the social aspect, especially with regard to health issues [53]. Therefore, people should consciously control the use of mobile social apps to avoid potential negative out comes.

## 5.3. Limitations and future research

Our study is not without limitations, thus indicating the directions

## Appendix A

A.1 Mobile Photo Apps

of future research. First, we only explore mobile social apps in the Chinese app market. Therefore, future studies should resolve the generalization issue of this study by conducting more research in di<sup>f</sup>erent countries.

Second, our model is merely validated in those app categories with a high level of co-installation probability. For other mobile contexts (e.g., mobile photo apps, mobile game apps, mobile map apps), the prerequisite of the model could not be met. Thus, we cannot use the utility function model to explore the interdependence e<sup>f</sup>ects among these apps (see the details in Appendix A).

Third, we only explore the social apps whose user penetration is more than 10 % and disregard the long-tail social apps. Whether the interdependence e<sup>f</sup>ects among long-tail social apps are the same with those top social apps needs further examination. Future research could extend the current study by investigating the interdependence e<sup>f</sup>ects among long-tail social apps.

## 6. Conclusion

In this study, the interdependence e<sup>f</sup>ects among mobile social apps are identi<sup>fi</sup>ed through the actual usage behavior. Moreover, our study demonstrates that a more <sup>fi</sup>ne-grained subcategory analysis from the perspective of psychological needs is necessary in investigating interdependence e<sup>f</sup>ects. Speci<sup>fi</sup>cally, we use FPM to <sup>fi</sup>nd the apps that are frequently installed together and propose a utility function model to quantify their interdependence e<sup>f</sup>ects. The empirical <sup>fi</sup>ndings indicate that social apps satisfying users’ di<sup>f</sup>erent psychological needs would be complementary at most times, while those apps gratifying simila psychological needs would also complement, rather than substitute, each other. Furthermore, our study demonstrates that the simple installation correlation could not re<sup>fl</sup>ect the actual usage relationships, and a more objective and accurate exploration is imperative. This study complements the existing literature on interdependence e<sup>f</sup>ects and provides a new way of conducting social network research, and also o<sup>f</sup>ers a comprehensive insight for app providers, marketers, and operators. Additionally, this study contributes to the sustainability lit erature by providing a deep understanding of the sustainable economic development for mobile social apps, as well as individuals’ health issues on sustainability.

## CRediT authorship contribution statement

Chuang Wang: Conceptualization, Methodology, Writing - review & editing. Shaochun Zheng: Data curation, Writing - original draft.

## Declaration of Competing Interest

The authors report no declarations of interest.

## Acknowledgements

The work was substantially supported by the National Natural Science Foundation of China (Nos 71871095, 71601080), the Ministry of Education of China (Project No. 16YJC630113), and the Fundamental Research Funds for the Central Universities(No. 2018MS32).

Table A1  
Results of FPM Among Mobile Photo Apps.

<table><tr><td>A</td><td>B</td><td>C( A⇒ B)</td><td>Lift</td></tr><tr><td>Meiyan Camera</td><td>Meitu</td><td>0.282</td><td>0.446</td></tr><tr><td>Meitu</td><td>Meiyan Camera</td><td>0.080</td><td>0.446</td></tr><tr><td>Meiyan Camera</td><td>Tencent Pic</td><td>0.083</td><td>0.473</td></tr><tr><td>Tencent Pic</td><td>Meiyan Camera</td><td>0.085</td><td>0.473</td></tr><tr><td>Meitu</td><td>Tencent Pic</td><td>0.044</td><td>0.250</td></tr><tr><td>Tencent Pic</td><td>Meitu</td><td>0.158</td><td>0.250</td></tr><tr><td>Selfiecity</td><td>Meitu</td><td>0.190</td><td>0.301</td></tr></table>

Table A2  
System GMM Estimates of Mobile Photo Apps (mainly shows the value of δ<sub>3</sub>).

<table><tr><td>DVIV</td><td>log_MY</td><td>log_MT</td><td>log_TP</td><td>log_SI</td></tr><tr><td>log_MY</td><td>\</td><td>-0.141</td><td>-0.048</td><td>0.008</td></tr><tr><td>log_MT</td><td>-0.013</td><td>\</td><td>-0.009</td><td>0.044</td></tr><tr><td>log_TP</td><td>-0.013</td><td>-0.043</td><td>\</td><td>-0.082</td></tr><tr><td>log_SI</td><td>0.003</td><td>0.014</td><td>-0.046</td><td>\</td></tr></table>

Note: \*\*\* $\mathsf { p } < 0 . 0 0 1$ 1, \*\* $\stackrel { * } { \cdot } { \bf { p } } < 0 . 0 1$ 1, \* $\mathbf { p } < 0 . 0 5 .$ . DV are dependent variables, IV are independent variables. MY is Meiyan Camera, MT is Meitu, TP is Tencent Pic, SI is Sel<sup>fi</sup>ecity. The number of observations is 405, and the number of groups is 148.

Table A3  
Results of FPM Among Mobile Game Apps.

<table><tr><td>A</td><td>B</td><td>C( A⇒ B)</td><td>Lift</td></tr><tr><td>Happy Elements</td><td>Arena of Valor</td><td>0.057</td><td>0.141</td></tr><tr><td>Arena of Valor</td><td>Happy Elements</td><td>0.034</td><td>0.141</td></tr><tr><td>Arena of Valor</td><td>Happy Joker</td><td>0.031</td><td>0.219</td></tr><tr><td>Happy Joker</td><td>Arena of Valor</td><td>0.088</td><td>0.219</td></tr><tr><td>Arena of Valor</td><td>Battle of Balls</td><td>0.104</td><td>0.554</td></tr><tr><td>Battle of Balls</td><td>Arena of Valor</td><td>0.224</td><td>0.554</td></tr><tr><td>Arena of Valor</td><td>Cross Fire</td><td>0.063</td><td>0.906</td></tr><tr><td>Cross Fire</td><td>Arena of Valor</td><td>0.366</td><td>0.906</td></tr><tr><td>Battle of Balls</td><td>Cross Fire</td><td>0.057</td><td>0.825</td></tr><tr><td>Cross Fire</td><td>Battle of Balls</td><td>0.155</td><td>0.825</td></tr></table>

Table A4  
System GMM Estimates of Mobile Game Apps (mainly shows the value of δ ).

<table><tr><td>DVIV</td><td>log_HE</td><td>log_AoV</td><td>log_HJ</td><td>log_BoB</td><td>log_CF</td></tr><tr><td>log_HE</td><td></td><td>-0.046***</td><td>-0.017</td><td>-0.016</td><td>0.001</td></tr><tr><td>log_AoV</td><td>-0.013</td><td></td><td>-0.015</td><td>-0.013</td><td>0.003</td></tr><tr><td>log_HJ</td><td>-0.020</td><td>-0.013</td><td></td><td>-0.036</td><td>0.000</td></tr><tr><td>log_BoB</td><td>-0.017</td><td>-0.038</td><td>-0.016</td><td></td><td>-0.002</td></tr><tr><td>log_CF</td><td>-0.060</td><td>0.019</td><td>-0.026</td><td>0.005</td><td></td></tr></table>

Note: \*\*\* $\mathsf { p } < 0 . 0 0 1$ $\ddot { \mathbf { \beta } } ^ { * } \mathbf { \beta } _ { \mathbf { p } } < 0 . 0 1$ 1, \* $\mathbf { p } < 0 . 0 5$ . DV are dependent variables, IV are independent variables. HE is Happy Elements, AoV is Arena of Valor, HJ is Happy Joker, BoB is Battle of Balls, and CF is Cross Fire. The number of observations is 2270, and the number of groups is 421.

Table A5  
Results of FPM Among Mobile Map Apps.

<table><tr><td>A</td><td>B</td><td>C( A⇒ B)</td><td>Lift</td></tr><tr><td>Baidu Map</td><td>Gaode Map</td><td>0.093</td><td>0.188</td></tr><tr><td>Gaode Map</td><td>Baidu Map</td><td>0.100</td><td>0.188</td></tr><tr><td>Tencent Map</td><td>Baidu Map</td><td>0.197</td><td>0.369</td></tr><tr><td>Tencent Map</td><td>Gaode Map</td><td>0.242</td><td>0.486</td></tr><tr><td>Sougou Map</td><td>Baidu Map</td><td>0.462</td><td>0.863</td></tr><tr><td>Sougou Map</td><td>Gaode Map</td><td>0.462</td><td>0.925</td></tr></table>

selected as the research context. Our dataset contains the user id, app name, and usage time of the seven mobile photo apps from January 9, 2016 to August 14. 2016.

We <sup>fi</sup>rst conduct frequent pattern mining (FPM) to <sup>fi</sup>nd the apps that are used by most of users (i.e., frequent app-sets). As the market penetration rate of mobile photo apps is not as high as that of mobile social apps, we set 0.01 as the minimum support and 0.03 as the minimum con<sup>fi</sup>dence. The 1-itemsets that satisfy the minimum support are {Meiyan Camera}, {Meitu}, {Tencent Pic}, and {Sel<sup>fi</sup>ecity}, which suggests that more than 1 % of the users use these four apps. As the users of other three apps are less than 1 % and the usage data would be relatively small, they are removed from our dataset. In the frequent app-sets, we mined the app-sets that satisfy the minimum con<sup>fi</sup>dence and calculated the lift value. The results are given in Table A1.

Table A6  
System GMM Estimates of Mobile Map Apps (mainly shows the value of δ ).

<table><tr><td>DVIV</td><td>log_BM</td><td>log_GM</td><td>log_TM</td><td>log_SM</td></tr><tr><td>log_BM</td><td>\</td><td>-0.041</td><td>0.001</td><td>-0.003</td></tr><tr><td>log_GM</td><td>-0.015</td><td>\</td><td>0.002</td><td>-0.000</td></tr><tr><td>log_TM</td><td>-0.037</td><td>-0.106</td><td>\</td><td>0.002</td></tr><tr><td>log_SM</td><td>0.020</td><td>-0.060</td><td>0.000</td><td>\</td></tr></table>

Note: \*\*\* $\mathsf { p } < 0 . 0 0 1$ , \*\* p < 0.01, \* p < 0.05. DV are dependent variables, IV are independent variables. BM is Baidu Map, GM is Gaode Map, TM is Tencent Map, and SM is Sougou Map. The number of observations is 2163, and the number of groups is 777.

According to the results of Table A1, all of the lift values are smaller than 1, which indicates that none of the apps would strengthen the installation of the others. That is, the installations among these apps are negatively correlated, thus the premise of the utility function model could not be met.

Next, we use the utility function model to explore the interdependence e<sup>f</sup>ects among mobile photo apps. In this part, our dataset is the subset of the frequent app-sets discovered by FPM. The dataset in this part is a dynamic unbalanced panel, involving 953 panel members. We use the system generalized method of moments (GMM) to empirically analyze the panel data, and the results are given in Table A2.

The results given in Table A2 indicate that the interdependence e<sup>f</sup>ects among the four mobile photo apps are insigni<sup>fi</sup>cant. Hence, we could not <sup>fi</sup>nd whether the complementary e<sup>f</sup>ect or the substitution e<sup>f</sup>ect exists among mobile photo apps by utilizing the utility function model

## A.2 Mobile Game Apps

Nine top Chinese mobile game apps (i.e., Happy Elements, Arena of Valor, Tiles, Happy Joker, Battle of Balls, Wepie Snake, Tencent Run, Cross Fire, and JJ Joker) were selected as the research context. Our dataset contains the user id, app name, and usage time of the nine mobile game apps from January 9, 2016 to August 14, 2016.

We <sup>fi</sup>rst conduct FPM to <sup>fi</sup>nd the apps that are used by most of users (i.e., frequent app-sets). We set 0.01 as the minimum support and 0.03 as the minimum con<sup>fi</sup>dence. The 1-itemsets that satisfy the minimum support are {Happy Elements}, {Arena of Valor}, {Happy Joker}, {Battle of Balls}, and {Cross Fire}, which suggests that more than 1% of the users use these <sup>fi</sup>ve apps. As the users of other four apps are less than 1% and the usage data would be relatively small, they are removed from our dataset. In the frequent app-sets, we mined the app-sets that satisfy the minimum con<sup>fi</sup>dence and calculated the lift value. The results are given in Table A3.

According to the results given in Table A3, all of the lift values are smaller than 1, which indicates that none of the apps would strengthen the installation of the others. That is, the installations among these apps are negatively correlated, thus the premise of the utility function model could not be met.

Next, we use the utility function model to explore the interdependence e<sup>f</sup>ects among mobile game apps. In this part, our dataset is the subset of the frequent app-sets discovered by FPM. The dataset in this part is a dynamic unbalanced panel, involving 934 panel members. We use the system GMM to empirically analyze the panel data, and the results are given in Table A4.

The results given in Table A4 indicate that the interdependence e<sup>f</sup>ect among Happy Elements and Arena of Valor is negatively signi<sup>fi</sup>cant, while the interdependence e<sup>f</sup>ects among other apps are all insigni<sup>fi</sup>cant. Hence, we could not demonstrate the interdependence e<sup>f</sup>ects among mobile game apps by utilizing the utility function model.

## A.3 Mobile Map Apps

Four top Chinese mobile map apps (i.e., Baidu Map, Gaode Map, Tencent Map, and Sougou Map) were selected as the research context. Our dataset contains the user id, app name, and usage time of the four mobile map apps from January 9, 2016 to August 14, 2016.

We <sup>fi</sup>rst conduct FPM to <sup>fi</sup>nd the apps that are used by most of the users (i.e., frequent app-sets). As the market penetration rate of mobile photo apps is not as high as that of mobile photo/game apps, we set 0.001 as the minimum support and 0.03 as the minimum con<sup>fi</sup>dence. The 1-itemsets that satisfy the minimum support are {Baidu Map}, {Gaode Map}, {Tencent Map}, and {Sougou Map}, which suggests that more than 0.1 % of the users use these four apps. In the frequent app-sets, we mined the app-sets that satisfy the minimum con<sup>fi</sup>dence and calculated the lift value. The results are given in Table A5.

According to the results given in Table A5, all of the lift values are smaller than 1, which indicates that none of the apps would strengthen the installation of the others. That is, the installations among these apps are negatively correlated, thus the premise of the utility function model could not be met.

Next, we use the utility function model to explore the interdependence e<sup>f</sup>ects among mobile map apps. In this part, our dataset is the subset of the frequent app-sets discovered by FPM. The dataset in this part is a dynamic unbalanced panel, involving 2939 panel members. We use the system GMM to empirically analyze the panel data, and the results are given in Table A6.

The results given in Table A6 indicate that the interdependence e<sup>f</sup>ects among the four mobile map apps are insigni<sup>fi</sup>cant. Hence, we could not <sup>fi</sup>nd whether the complementary e<sup>f</sup>ect or the substitution e<sup>f</sup>ect exists among mobile map apps by utilizing the utility function model.

## References

[1] D. Kristianto, The Most Popular Google Play Apps of All Time, (2018) https://www. appannie.com/en/insights/market-data/google-play-all-time/.

[2] E. Karahanna, S. Xin Xu, Y. Xu, N. (Andy) Zhang, The Needs–a<sup>f</sup>ordances–features perspective for the use of social media, MIS O. 42 (2018) 737–756.

[3] J.H. Kietzmann. K. Hermkens, I.P. McCarthy. B.S. Silvestre. Social media? Get serious! Understanding the functional building blocks of social media, Bus. Horiz

54 (2011) 241–251.

[4] H. Lin, W. Fan, P.Y.K. Chau, Determinants of users continuance of social net working sites: a self-regulation perspective, Inf. Manag. 51 (2014) 595 603.

[5] K.-Y. Lin, H.-P. Lu, Why people use social networking sites: an empirical study integrating network externalities and motivation theory, Comput. Human Behav. 27 (2011) 1152 1161.

[6] iResearch, Insight Report of Users of Chinese Mobile Social Apps, (2017) http:// report iresearch cn/report/201707/3020 shtml

[7] H. Li, X. Lu, X. Liu, T. Xie, K. Bian, F.X. Lin, Q. Mei, F. Feng, Characterizing

smartphone usage patterns from millions of android users, Internet Meas. Conf., Tokyo, Japan (2015) 459 472.

[8] X. Liu, H. Li, X. Lu, T. Xie, Q. Mei, F. Feng, H. Mei, Understanding diverse usage patterns from large-scale appstore-service pro<sup>fi</sup>les, IEEE Trans. Softw. Eng. 44 (2018) 384–411

[9] Q. Xu, J. Erman, A. Gerber, Z. Mao, J. Pang, S. Venkataraman, Identifying diverse usage behaviors of smartphone apps, Proc. 2011 ACM SIGCOMM Conf. Internet Meas. Conf., ACM, Berlin, Germany (2011) 329–344.

[10] J. Huang, F. Xu, Y. Lin, Y. Li, On the understanding of interdependency of mobile app usage, 2017 IEEE 14th Int. Conf. Mob. Ad Hoc Sens. Syst., IEEE, Orlando, FL, USA, 2017, pp. 471–475

[11] S.P. Han, S. Park, W. Oh, Mobile app analytics: a multiple discrete-continuous choice framework, MIS Q. 40 (2016) 983–1008.

[12] W. Nicholson, C.M. Snyder, Microeconomic theory: basic principles and extensions, Nelson Education, (2012).

[13] T. Petsas, A. Papadogiannakis, M. Polychronakis, E.P. Markatos, T. Karagiannis, Rise of the planet of the apps: a systematic study of the mobile app ecosystem, Proc. 2013 Conf. Internet Meas. Conf. Barcelona, Spain, 2013, pp. 277–290.

[14] A. Tongaonkar, S. Dai, A. Nucci, D. Song, Understanding mobile app usage patterns using in-app advertisements, Int. Conf. Passiv. Act. Netw. Meas. Springer, Hong Kong, China, 2013, pp. 63–72.

[15] M. Böhmer, B. Hecht, J. Schöning, A. Krüger, G. Bauer, Falling asleep with angry birds, facebook and kindle: a large scale study on mobile application usage, Proc. 13th Int. Conf. Hum. Comput. Interact. with Mob. Devices Serv. ACM, Stockholm, Sweden, 2011, pp. 47 56.

[16] Z. Xu, O. Turel, Y. Yuan, Online game addiction among adolescents: motivation and prevention factors, Eur. J. Inf. Syst. 21 (2012) 321 340.

[17] C. Wang, M.K.O. Lee, Z. Hua, A theory of social media dependence: evidence from microblog users, Decis. Support Syst. 69 (2015) 40–49.

[18] F.A. Silva, A.C.S.A. Domingues, T.R.M. Silva, Discovering mobile application usage patterns from a large-scale dataset, ACM Trans. Knowl. Discov. 12 (2018) 5901 5936 from Data.

[19] K. Huang, C. Zhang, X. Ma, G. Chen, Predicting mobile application usage using contextual information, Proc. 2012 ACM Conf. Ubiquitous Comput. ACM, New York, USA, 2012, pp. 1059–1065.

[20] J. Xu, C. Forman, J.B. Kim, K. Van Ittersum, News media channels: complements or substitutes? Evidence from mobile phone usage, J. Mark. 78 (2014) 97–112.

[21] J. Jacoby, G.J. Szybillo, C.K. Berning, Time and consumer behavior: an inter disciplinary overview. J. Consum. Res, 2 (1976) 320–339

[22] M.I. Hwang, Decision making under time pressure: a model for information systems research, Inf. Manag. 27 (1994) 197–203.

[23] E. Reutskaja, R. Nagel, C.F. Camerer, A. Rangel, Search dynamics in consumer choice under time pressure: an eye-tracking study, Am. Econ. Rev. 101 (2011) 900–926.

[24] S. Okazaki, J. Romero, Online media rivalry: a latent class model for mobile and PC internet users, Online Inf, Rey, 34 (2010) 98–114

[25] J. Dimmick, Y. Chen, Z. Li, Competition between the Internet and traditional news media: the grati<sup>fi</sup>cation-opportunities niche dimension, J. Media Econ. 17 (2004) 19–33.

[26] L. Weng, A. Flammini, A. Vespignani, F. Menczer, Competition among memes in a world with limited attention. Sci. Rep. 2 (2012) 1–8.

[27] W. Shen. YJ. Hu. J.R. Ulmer. Competing for attention: an empirical study of online reviewers' strategic behavior, MIS O. 39 (2015) 683–696.

[28] L. Dahlberg, The corporate colonization of online attention and the marginalizatior of critical communication, J. Commun. Inq. 29 (2005) 160–180.

[29] T.H. Davenport, J.C. Beck, The Attention Economy: Understanding the New Currency of Business, Harvard Business Press, Boston, Massachusetts, 2001.

[30] D. Van Knippenberg, L. Dahlander, M.R. Haas, G. George, Information, attention, and decision making, Acad. Manag. J. 58 (2015) 649 657.

[31] Z.X. Li, A. Agarwal, Platform integration and demand spillovers in complementary markets: evidence from Facebook s integration of instagram, Manage. Sci. 63 (2016) 3438 3458

[32] S. Aral, D. Walker, Creating social contagion through viral product design: a ran domized trial of peer in<sup>fl</sup>uence in networks, Manage. Sci. 57 (2011) 1623 1639.

[33] H.S. Nair, P. Manchanda, T. Bhatia, Asymmetric social interactions in physician

prescription behavior: the role of opinion leaders, J. Mark. Res. 47 (2010) 883 895.

[34] W.R. Hartmann, P. Manchanda, H. Nair, M. Bothner, P. Dodds, D. Godes, K. Hosanagar. C.E. Tucker. Modeling social interactions: identification. empirical methods and policy implications, Mark. Lett. 19 (2008) 287–304.

[35] C.F. Manski, Dynamic choice in social settings: learning from the experiences of others, J. Econ. 58 (1993) 121–136.

[36] E.L. Deci, R.M. Ryan, The“ what” and“ why” of goal pursuits: human needs and the self-determination of behavior, Psychol. Inq. 11 (2000) 227–268.

[37] E.L. Deci, R.M. Ryan, The support of autonomy and the control of behavior, J. Pers. Soc. Psychol. 53 (1987) 1024–1037.

[38] K.M. Sheldon, N. Abad, C. Hinsch, A two-process view of Facebook use and relat edness need-satisfaction: disconnection drives use, and connection rewards it, J. Pers, Soc, Psychol, 100 (2011) 766–775

[39] S. Harter, E<sup>f</sup>ectance motivation reconsidered. Toward a developmental model, Hum. Dev. 21 (1978) 34–64.

[40] R.W. White, Motivation reconsidered: the concept of competence, Psychol. Rev. 66 (1959) 297–333.

[41] R.F. Baumeister, M.R. Leary, The need to belong: desire for interpersonal attach ments as a fundamental human motivation. Psychol. Bull. 117 (1995) 497–529

[42] J.L. Pierce, T. Kostova, K.T. Dirks, The state of psychological ownership: integrating and extending a century of research, Rev. Gen. Psychol. 7 (2003) 84–107.

[43] H.J.M. Hermans, E. Hermans-Jansen, Self-narratives: the Construction of Meaning in Psychotherapy, The Guilford Press, New York, 1995.

[44] R.A. Pollak, Habit formation and dynamic demand functions, J. Polit. Econ. 78 (1970) 745–763.

[45] M. Boyer, A habit forming optimal growth model, Int. Econ. Rev. (Philadelphia). 19 (1978) 585 609.

[46] R. Agrawal, T. Imieliński, A. Swami, Mining association rules between sets of items in large databases, Proc. 1993 ACM SIGMOD Conf. Manag. Data 22 (1993) 207 216.

[47] J.W. Han, H. Cheng, D. Xin, X.F. Yan, Frequent pattern mining: current status and future directions, Data Min. Knowl Discov, 15 (2007) 55–86

[48] J. Han, J. Pei, M. Kamber, Data Mining: Concepts and Techniques, 3rd ed., Morgan Kaufmann, Massachusetts, USA, 2012.

[49] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proc. 20t VLDB Conf. Santiago, Chile, 1994, pp. 487 499.

[50] A. Nadkarni, S.G. Hofmann, Why do people use Facebook? Pers. Individ. Dif. 52 (2012) 243 249.

[51] P.M. Leonardi, When <sup>fl</sup>exible routines meet <sup>fl</sup>exible technologies: a<sup>f</sup>ordance, con straint, and the imbrication of human and material agencies, MIS Q. 35 (2011) 147–167.

[52] WCED, Our Common Future, Oxford University Press, Oxford, 1987.

[53] R.K. Singh, H.R. Murty, S.K. Gupta, A.K. Dikshit, An overview of sustainability assessment methodologies, Ecol. Indic. 9 (2009) 189–212

[54] S.E. Caplan, A.C. High, Beyond excessive use: the interaction between cognitive and behavioral symptoms of problematic Internet use, Commun. Res. Rep. 23 (2006) 265–271.

[55] X. Zheng, M.K.O. Lee, Excessive use of mobile social networking sites: negative consequences on individuals, Comput. Human Behav. 65 (2016) 65–76.

[56] A.C. Santos, J.M.P. Cardoso, D.R. Ferreira, P.C. Diniz, P. Chaínho, Providing user context for mobile and social networking applications. Pervasive Mob. Comput. 6 (2010) 324–341.

Chuang Wang is an associate professor at the School of Business Administration, South China University of Technology. Her research focuses on IT challenges and negative issues, social media. social network, and mobile commerce, She has published in journals such as Information Systems Research, Journal of Management Information Systems, Journal of the Association for Information Systems, Decision Support Systems, Information Processing & Management, Electronic Commerce Research and Applications, Internet Research, and Journal of Services Marketing

Shaochun Zheng is a master student at the School of Business Administration, South China University of Technology. Her research focuses on mobile apps, social media, and social networking service.
