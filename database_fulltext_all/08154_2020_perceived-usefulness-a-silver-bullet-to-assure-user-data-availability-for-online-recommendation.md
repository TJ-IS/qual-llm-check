---
otero_id: 8154
otero_key: "Z6NU4BTA"
title: "Perceived usefulness: A silver bullet to assure user data availability for online recommendation systems"
authors: "Daniel Mican; Dan-Andrei Sitar-Tăut; Ovidiu-Ioan Moisescu"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113420"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Perceived usefulness: A silver bullet to assure user data availability for online recommendation systems

Daniel Mican, Dan-Andrei Sitar-Tăut , Ovidiu-Ioan Moisescu

Faculty of Economics and Business Administration, Babeş-Bolyai University, Theodor Mihaly Street 58-60, 400591, Cluj-Napoca, Romania

## A R T I C L E I N F O

Keywords: Recommendation systems Data privacy Content recommendation Privacy Personal data Decision-making

## A B S T R A C T

Online stores currently use recommendation systems (RSs) quasi-universally to provide their customers with added value and increase their profits, thus reshaping the world of e-commerce. RSs, however, depend on the availability of e-commerce user data to be efective. Nevertheless, data privacy regulations are increasingly becoming more restrictive and e-commerce users more aware of and concerned about their data being collected, stored, and processed for RSs. On the other hand, in the RSs context, there is currently a very limited understanding of e-commerce users' attitudes toward data privacy and of these attitudes' antecedents. This study examines the influence that an RS's perceived usefulness has on e-commerce users in terms of a specific RS collecting, storing, and processing their data. In addition, this study investigates the extent to which RSs' overall relevance for users depends on their perceived usefulness and users' degree of consent. We conducted an online survey of 597 e-commerce users, thereafter analyzing the data by means of partial least squares structural equation modeling (PLS-SEM). The results indicate that an RS's perceived usefulness positively and significantly influences the extent to which users consent to the RS's provider collecting and storing their data, which in turn also impact RSs' overall relevance for e-commerce users. The findings have practical implications for e-commerce industry players, as well as for national and international authorities responsible for online data privacy regulations

## 1. Introduction

Online recommendation systems (RSs) have received a great deal of attention from both industry and researchers, especially during the last decade. RSs have reshaped the world of e-commerce [1] since online stores currently use RSs quasi-universally to provide their customers with added value and increase their profits. Previous research has shown that recommendations have a significant and positive impact on sales [2] by reducing search costs and the perceived risks associated with purchasing products that are not popular, with which consumers are not familiar, or are even of poor quality [3], as well as by influ encing cross-selling eforts' success rates positively [1].

In order to be efective, RSs depend on e-commerce user data's availability. These systems need to collect, store, and process users' online data as explicit (i.e. explicitly provided by users) and implicit (i.e. implicitly collected by RSs) feedback [4,5]. In turn, the process of collecting, storing, and processing users' online data raises consumer privacy concerns and is increasingly perceived as substantially harming users' privacy interests [6]. Furthermore, new data protection regulations (e.g. the European Union's General Data Protection Regulation (GDPR) [7]) and users' increasing awareness of their data being collected [8–11], have turned data retrieval and storage, as well as profile building within an RS, into sensitive activities. Individuals' lack of control over their information, particularly in terms of implicit feedback. leads to privacy concerns about RSs [8]. It is therefore imperative to have a clear understanding of how technology and data collection, storage, and usage might afect users' security and privacy rights [12], as well as to understand their attitude to RSs. From a legal and an ethical perspective, e-commerce sites should transparently disclose which user data they collect and what they are used for. Such disclosures mean users are fully in control of their personal and personally identifiable information that they might decide to share [13].

In online behavioral advertising, industries, regulators, consumer organizations, and scholars have paid much attention to the collection and use of personal data [14]. Consequently, industry alliances have set up self-regulatory programs to protect consumer privacy and describe how consumers should be informed about data collection and usage, as well as what users could receive in exchange for providing their data. On the other hand, the trade-of between usefulness and privacy is not explicit in an RS, as the entire mechanism is less transparent and occurs against a quasi-obscure background.

Although there are currently no explicit legal obligations for online retailers to obtain users' consent when collecting, storing, and processing their behavioral online data to use for RSs, given the current regulatory trends [14–16], we expect this to become mandatory in the near future. In the meantime, the European Commission and the U.S. Federal Communications Commission have introduced data protection policies requiring websites to obtain consumers' explicit consent before using or sharing sensitive data with third parties [15]. There is no reasonable argument indicating that such an approach should not apply to the user data required for RSs. Ultimately, the data comprise consumers' information, and “how it is used should be the consumers' choice, not the choice of some corporate algorithm” [16]. There should certainly be convincing reasons or rewards for users to give away their data [15].

Internet users' concerns about their digital footprint were on an increasing trend several years before regulations such as the GDPR were implemented [8–11]. Such concerns, along with various scandals and controversies related to online data exploitation, push authorities into issuing more data protection regulations. Further on, such regulations give consumers even more awareness of their personal data being col lected and employed [17]. Therefore, it can be stated that consumers becoming more privacy-conscious and data protection regulations be coming wider and stricter are inter-related, and this trend will continue.

During their early development, RSs were based on statistical data and ofered each client identical recommendations, without any attempt at personalization. Technological advancements, however, have led to increased personalization, starting from more than a decade ago, resulting in RSs suggesting customized items based on e-commerce users' specific online behavior. Nevertheless, as long as user data are collected from a specific user and stored at a certain time to provide the same user with personalization at a later time, these data are more or less personally identifiable and could be subject to existing privacy regulations (e.g. GDPR).

Moreover, many RSs have become hybrid in recent years, combining basic RS types or adding new information about users [10]. By incorporating data from a variety of information sources, such an RS comprises huge databases of information about a large number of users [18]. By aggregating personally identifiable data with various user online behavioral data [8,18], the whole data package could become personally identifiable, leading to a potential GDPR violation if users' consent is not explicitly given. Users are, at least for now, often una ware of what data are stored and how they are used in RSs [11], al though their awareness of this privacy issue is increasing [8,10,11].

Although it is universally accepted that privacy concerns influence users' willingness to provide their data to a service provider, the extent to which these concerns influence recommendation algorithms' acceptance is still unclear [11]. Despite online data privacy's growing importance in RSs and RS users' increasing awareness that their data are being stored and processed in the background, there is currently a very limited understanding of e-commerce users' attitudes toward data privacy in the context of RSs, as well as of these attitudes' antecedents [8–11].

This study aims to fill this significant knowledge gap by capturing users' attitudes toward the most popular RS types on the market from two essential perspectives: usefulness, and data collection and storage acceptance. More specifically, the study examines the influence of RSs' perceived usefulness on e-commerce users' data collection and storage consent, taking the main types of RSs into account and the core input data categories that these systems use.

The research goal is to predict the extent to which e-commerce users are willing to share their online data with RS providers, with the per ceived benefits of using such systems as antecedents. In this context, users' online data refer to explicit feedback as identifiable personal data and to users' implicit feedback as comprising their online behavioral data. Another important aspect that we analyze in the current research is the extent to which RSs' overall relevance for users depends on their perceived usefulness and on users' degree of consent to the collecting and storing of their identifiable personal and online behavioral data.

Based on data collected from a large sample of e-commerce users via an online questionnaire, our research extends the literature on data privacy issues by revealing that an RS's perceived usefulness is an essential ingredient in assuring user data availability in the long run. The latter not only applies in the context of increasing legal restrictions on data collection, but also in terms of increasing e-commerce users' awareness and concerns about implicit data collection by means of RSs. Consequently, the current study has practical implications for e-commerce industry players, as well as for national and international authorities responsible for online data privacy regulations.

RSs have emerged as a distinct research field in the mid-1990s, growing in importance in the following decades [19–21]. Analyzing the evolution of research in the RSs field, scholars have identified various perspectives, core topics and trends related to this field.

Thus, Jannach et al. [20] point out that previous research on RSs has generally been conducted considering three perspectives: information retrieval, machine learning, and decision support systems. From the information retrieval perspective, studies have addressed the issue of information overload and properly identifying the items that are relevant to users. From the machine learning perspective, research has generally focused on algorithm improvements, in order to predict users' feedback on specific items as accurately as possible. Finally, from the decision support systems perspective, research has revolved around the idea of RSs as tools that help consumers with their decisions making processes, studies usually focusing on factors influencing users' decisions and their behavior as customers (i.e.: attitudes to RSs, trust in such systems, preferences etc.). Valdez et al. [19] indicate that RSs research started with the main focus on technique and algorithms development aimed at improving recommendation accuracy, and further developed into a second direction related to human factors that afect the user experience (e.g. attitudes, trust, preferences). The latter research direction has generated a significant number of studies underpinned in social sciences, while the former evolved, especially during recent years, toward big data, deep learning, and artificial intelligence.

The current paper extends the RSs research related to the human factors, being in line with the decision support systems approach. At the same time, our research results are relevant from both the information retrieval and machine learning perspectives, having implications for technique and algorithms development, by providing means for assuring user data availability, which is essential for generating big data, as well as for fostering deep learning and artificial intelligence.

Further, we outline the theoretical foundations and conceptual framework required to layout the proposed research model. Thereafter, we develop and describe the research model and the corresponding hypotheses. We also provide details of the research methodology and technical aspects related to the PLS-SEM technique employed, such as measurement assessment, structural model assessment, predictive relevance, and model fit, as well as a discussion of the results. The paper concludes with an outline of the study's main conclusions, along with its theoretical and practical implications, limitations, and future research directions.

## 2. Theoretical foundations and conceptual framework

Generally, RSs collect information about online users' preferences from multiple sources, estimate these users' preferences for unseen items, and then generate appropriate recommendations. RSs, therefore, help users save time and discover interesting content quickly and easily. The purpose of developing RSs is to reduce the information overload by selecting the most relevant information and services from a large data volume, thus ofering personalized services [22].

By personalizing experiences, optimizing sales, and maximizing profitability, RSs have led to a reshaping of e-commerce, while access to information has led to information market innovation [12]. The provision of personalized content is based on predicting consumer behavior [23], which requires user data [10]. Since everyone is not only connected online, but also through online activities, users leave a series of traces on the online environment. Data on, for example, online searches, what we like, whom we interact with, what we buy, or what we view, are captured and linked to personal profiles [9].

## 2.1. Types of RSs

E-commerce sites have implemented various RSs in order to help consumers find the products they need, make purchase decisions, thereby increasing sales volumes. From the consumers' perspective, which overlaps with this research's approach, an RS's taxonomy should be based on what e-commerce users see and perceive, and not on the algorithms that underlie recommendations. Furthermore, given this perspective, we will briefly describe the most popular types of RSs that extant e-commerce sites implement and to which our empirical research refers.

One of the most popular types of RS takes e-commerce users' per sonal online shopping behavior into account and provides recommendations based on recently viewed products, similar products, complementary products, or accessories. To make recommendations, such RSs capture usage data, store product viewing sessions and allow users to return to the products included in the browsing sessions history [24]. Recommendations can also be provided by analyzing users' purchase history as a basis for predictions of future buying behavior [25] (e.g. a consumer who has bought many books by one author is likely to buy new ones by the same author).

In order to provide recommendations for a given user, another frequently implemented type of RS takes the online shopping behavior of other users into account. This behavior might refer to products bought together [1] (an idea coined by Amazon.com and one of the most popular in e-commerce stores), similar products identified on the basis of behavioral data (e.g. added together to favorites, included in the same browsing session) [25], as well as similar products identified based on social media peers' behavioral data [26] because such peers do influence purchase decisions [27].

Special ofers recommendations are another popular RS category. In this context, recommendations are provided if price discounts are available on favorite products or similar products to these. Such an RS can be very efective because, in addition to users' preference for certain products, discounts can also have a significant impact on purchase decisions [28].

Last but not least, another traditional and frequently used RS type refers to general trend recommendations, which are based on statistical data. In this case, recommendations include best-selling products, top products, top brands, trend products, or editor choices [25]. In many cases, such RSs have evolved into more personalized systems by incorporating user information [10] and subsequently providing diferent users with adapted recommendations.

More recently, in line with the hybridization process [29], RSs have been improved by combining traditional RS types included in our taxonomy and/or by adding new user information [10]. A hybrid RS incorporates data from a variety of information sources, thereby acquiring a user's history (bought items, used contents, behavioral information), social connections, tags, and popularity statistics. This RS uses these signals to create a hybrid model that incorporates user-touser and item-to-item similarities by using CF, content, social, and popularity information [29]. In such hybrid RSs, each user will, therefore, receive personalized recommendations depending on a specific user's existing profile and the implemented hybridization model.

## 2.2. Types of input data that RSs employ

In order to provide meaningful recommendations, RSs need to col lect, store, and process users' online data, more specifically their explicit and implicit feedback [4,5]. Users provide explicit feedback, which may contain personal or identifiable personal data [30]. The implicit feedback includes users' online behavioral data, purchase history, social information, etc.; these data are then used to derive users' preferences [8,9]. Based on user profiles, RSs will provide recommendations specifically designed to meet specific users' needs. The most valuable data are related to the explicit feedback that users provide, which are also considered high-quality data. When explicit feedback data are not available, RSs can infer user preferences by using implicit feedback data, which indirectly reflect the user's opinion [5,8,9].

In the initial stages of RSs' implementation on e-commerce sites, data such as user ratings, favorite products, search patterns, purchase history, etc. were collected and stored anonymously in order to find similarities between products [1]. Consequently, using such data wa not regarded as a privacy issue at the time, as it was not linked to a single user identity. However, the vast majority of current RSs store user data in a way that allows users to be identified and traced [8–10,18], thus raising privacy-invasion concerns [8].

RSs use and process a large variety of data. We will briefly describe the main types of data that e-commerce sites employ most frequently to provide recommendations, and to which our empirical research refers. First, RSs exploit data on users' preferences [30]. These preferences are dynamic, as they are subject to change over time and certain product attributes influence them. These data include users' input regarding their likes or dislikes, which users can provide explicitly, or which can be implicitly inferred via RSs' algorithms. Another data category comprises users' personal attributes, which users generally provide explicitly and which contain demographic information, such as a user's name, gender, age, marital status, education, occupation, income, residence, etc. [8,10].

Users also explicitly provide opinions about items, which is another important data category that RSs harness. Such opinions are stated by means of scalar measures (e.g. ratings on a 1–5 stars scale), binary indicators (e.g. included in a favorite list or an interest list), or text (e.g. reviews, comments, tags) [10,26] . In recent years, reviews and comments have been increasingly used to provide relevant recommendations, as well as being used in rating prediction models [28]. Another important data category that RSs employ refers to users' online shop ping behavior, more specifically to implicitly collected data on users' purchase history, browsing history, search patterns, or even mouse movements [5]. Online stores often use data from browsing and online shopping sessions to track user interests [31].

Social media data on the relationship between diferent e-commerce users [10] is another important data category that RSs use because if users link their social media profiles with e-commerce platforms, this allows them to receive more meaningful recommendations [11,26]. Based on social relations data, on received feedback, and on contribu tions within online social networks, RSs can infer the level of trust between users [17] and, consequently, provide recommendations that their receivers perceive as more trustworthy. This type of data can be explicitly and/or implicitly collected and is regarded as a means to overcome many of the traditional RSs' shortcomings [26].

## 2.3. Data privacy concerns

In recent years, the public has increasingly acknowledged e-commerce sites' massive retention of their personal information, which they regard as substantially prejudicing online users' privacy interests [6].

Online data privacy protection is important to everybody in the current age of big data [32]. RSs make use of big data and, consequently, privacy protection is a crucial issue in this context [33]. User data are employed in various ways by RSs, all of them have the po tential to raise privacy concerns for users. Thus, online users' purchase records can be employed to infer their financial status and shopping preferences. Also, their search keywords can be used to infer personal interests, concerns, preferences, and knowledge. For example, searching for medical information could indicate a user's health con cerns, looking for information on travel services could indicate his/her intention to travel, as well as preferred types of destinations, news search and reading patterns could expose a user's political attitudes, etc. Moreover, the possibility of transferring (or leaking) such information to third parties increases users' perceived risks related to data privacy. For example, an online user's medical data leaking to a potential employer could make the hiring decision unfairly based on the users medical history.

Data privacy represents a hot topic not only in the media, which raises public awareness but also within e-commerce practitioners and in academic research [32]. Over the past several decades, both researchers and practitioners have acknowledged the need to build privacy-friendly systems [34]. Examining trends in academic research on data privacy, Choi et al. [35] emphasize that users' online privacy concerns and attitudes represent emerging research areas that need further analysis.

A recent study conducted by Boerman et al. [36], which investigated online privacy-protective behavior, showed that online users are concerned about the collection, storage, usage, and sharing of their personal information and perceive this as a serious problem. Further more, this perceived severity significantly and positively predicts online users' protective behavior.

The emergence of new data protection regulations, such as the European Union's General Data Protection Regulation (GDPR), was one of the consequences of these privacy concerns [7]. Owing to these regulations, retrieving and storing user data required for profile building within RSs have become a real challenge. Additionally, Isaak et al. [12] point out that having a clear understanding of how such data collection afects people's lives, their privacy rights, and their security is of the utmost importance. Consequently, both researchers and practi tioners should be actively involved in this debate and make a significant contribution to data privacy policies' development.

Currently, advertisers are increasingly monitoring people's online behavior and using the collected information to present individually targeted advertisements, a practice which raises concerns about privacy. Previous research [14] has suggested that greater transparency and consumer awareness of such practices impact consumers' responses to online behavioral ads positively. In other words, when companies inform people that they collect and use their data to personalize ads, their click-through rates actually increase. Previous studies also analyzed the privacy trade-of's costs and benefits regarding mobile app downloads. Wottrich et al. [37], for example, showed that an app's higher perceived value increased the probability of users granting access to personal data, and reduced their privacy concerns.

In the case of RSs, the more the amount of personal data collected, the more accurate and meaningful the recommendations provided to users are [9]. However, if the information resulting from the aggrega tion [18] of collected data becomes identifiable, this can be very sensitive from a confidentiality point of view [9], as this is a potential breach of confidential data [8]. In the past, users were not implicitly aware that RSs collected and processed their online activity data. However, in recent years, users have become more aware of this data collecting and usage and have become much more reluctant to allow their data to be supplied or acquired [14–16]. Recently, Choi et al. [15] proposed a theoretical model of privacy in which data collection requires consumers' consent and consumers are fully aware of the consequences of such consent. Similarly, Mazeh and Shmueli [18] proposed an RS architecture that would allow users to manage and keep control of their own data.

Users' perceptions are essential criteria for assessing RSs, although the way these perceptions impact users' privacy concerns and their attitude to RSs' collecting and usage of their data is still an uncharted research territory. One of the few studies in this direction assessed users' perspectives on the privacy-utility trade-ofs in health RSs, concluding that users believe that sharing their data should be their decision and that, “without [the] acceptance and the willingness of users to share their information and allowing RS to use it, even perfect algorithms are meaningless” [38]. In line with these conclusions, Ardissono and Mauro [39] emphasize that, despite RSs' good results, online users nevertheless hardly accept them due to serious concerns about privacy intrusion and the ways they collect personal and social relationships information.

A recent study exploring privacy concerns in news RSs suggests that the received recommendations' perceived value is an important driver of users' consent to allow their data to be collected and processed [8]. Besides, the results that Smink et al. [40] obtained by means of augmented reality product presentations suggest that if users perceive recommendations as being highly informative, this increases their purchase intentions and willingness to share personal data.

Another recent issue regarding online privacy is the cross-sharing of personal data. For example, if someone searched for a product with Google, or Facebook, or viewed it on one of the AdWords or Facebook Ads partner sites, YouTube or partner sites will later post recommendations that reflect what they searched for earlier. This is because companies turn their customers' behavioral data into opportunities to sell targeted advertising (remarketing), or imply that private data has leaked into a wider range, or has been hacked. Both cases generate privacy issues that have been acknowledged by authorities, as well as by e-commerce users [14–16].

All this incipient research on RS users' attitudes to their data being employed explicitly and implicitly, conveys the idea that providing content and recommendations of perceived high value, as well as adding transparency, developing practical privacy-preserving techni ques, and protecting user data, are all of the utmost importance.

## 3. Research model and research hypotheses

This study examines the extent to which RSs' perceived usefulness can predict e-commerce users' consent to RSs collecting, storing, and processing their explicit and implicit feedback. This causal relationship is analyzed multi-dimensionally, taking into account the most important and frequently implemented types of RSs, as well as the main input data types that RSs employ. In addition, the study evaluates the extent to which RSs' overall relevance for users depends on their perceived usefulness and on users' degree of consent to having their data collection and storage.

Firstly, the most important and frequently implemented types of RSs were grouped into four categories, taking into account the way recommendations are provided to a given e-commerce user: based on the user's personal online shopping behavior (POSB), based on other users online shopping behavior (OOSB), based on general trends in online shopping (GT), and based on special ofers (SO). We further conceptualized several reflectively measured constructs, one for each of the four RSs, to depict their perceived usefulness (PU). Thus, “PU” prefixes each RS type (PUPOSB, PUOOSB, PUGT, and PUSO).

Secondly, the main input data types employed by RSs were grouped into five categories, taking into account how these data are collected and their explicit/implicit nature: likes/dislikes (LD); personal/sensitive information such as gender, age, location, job, address, etc. (PSI); ratings/reviews/interests (RRI); personal online shopping behavior (POSB), and social data, such as friends/acquaintances' online shopping behavior (FAOSB). Consequently, we developed five reflectively measured variables aimed at assessing users' consent/acceptance (A) to RSs collecting and storing each specific category of data. Therefore, “A” prefixes each data category (ALD, APSI, ARRI, APOSB, and AFAOSB).

Thirdly, in order to evaluate the extent to which RSs' overall relevance for users depends on their perceived usefulness and on users' degree of consent to having their data collected and stored, we conceptualized a final reflectively measured variable aimed at depicting RSs' overall relevance as perceived by e-commerce users (PRRS). Fig. 1 provides a graphical representation of our proposed research model, including the hypothesized relationships.

![](/api/attachments/Z6NU4BTA/fulltext/images/ea78b75fd99fd3503d4412f3bcb62454d01c0f96cb435f616e96d9bc9478d519.jpg)  
Fig. 1. Research model depicting the influence of RSs' perceived usefulness on e-commerce users' consent to RSs collecting and storing their explicit and implicit data.

The logical assumption that drives the first set of our research hy potheses is that the perceived usefulness of RSs that provide recommendations based on personal online shopping behavior (PUPOSB) impacts users' acceptance of data collection and storing in terms of all types of information, except the data referring to friends/acquaintances' online shopping behavior, which are not at all relevant for this type of RS:

H1a. PUPOSB has a positive and significant influence on ALD.

H1b. PUPOSB has a positive and significant influence on APSI.

H1c. PUPOSB has a positive and significant influence on ARRI.

H1d. PUPOSB has a positive and significant influence on APOSB.

The second set of hypotheses focuses on RSs' perceived usefulness when providing recommendations to a given user based on other users' online shopping behavior (PUOOSB). The perceived usefulness in this case is expected to influence users' consent to RSs collecting and storing all types of data included in our analysis. This is based on the logic that users want their preferences, transactions, likes, ratings, etc. to be in cluded in the overall dataset on which such RSs rely in order to determine general shopping behaviors (so that recommendations can be more relevant and meaningful).

H2a. PUOOSB has a positive and significant influence on ALD.

H2b. PUOOSB has a positive and significant influence on APSI.

H2c. PUOOSB has a positive and significant influence on ARRI.

H2d. PUOOSB has a positive and significant influence on APOSB.

H2e. PUOOSB has a positive and significant influence on AFAOSB.

We also posited a hypothesis regarding RSs' perceived usefulnes when providing recommendations based on special ofers (PUSO). More specifically, in this case, we expect the perceived usefulness to impact users' acceptance of the collecting and storing of their data from ex plicitly expressed reviews, ratings, and personal interests. This re lationship is based on the logic that such RSs are normally based on the interests that users express (e.g., adding a product to a favorites list and waiting for the price to become more advantageous).

H3. PUSO has a positive and significant influence on ARRI.

The final set of hypotheses focusing on predicting users' consent is related to the influence of RSs' perceived usefulness when their recommendations are based on general trends in online shopping (PUGT). In this context, we expect perceived usefulness to impact e-commerce users' consent to RSs collecting and storing data on their personal online shopping behavior and their social peers (i.e. friends', acquaintances', and people followed on social media's behavior and purchase preferences). Other types of data, such as likes/dislikes, sensitive personal information, as well as ratings/reviews/interests were not posited in similar hypotheses, as these data would not be suficiently relevant to indicate general trends.

H4a. PUGT has a positive and significant influence on APOSB.

H4b. PUGT has a positive and significant influence on AFAOSB.

Further, in order to assess the extent to which RSs' overall relevance for users depends on their perceived usefulness and on users' degree of consent to having their data collected and stored, we issued five specific hypotheses referring to each of the data types.

H5. ALD has a positive and significant influence on PRRS.

H6. APSI has a positive and significant influence on PRRS.

H7. ARRI has a positive and significant influence on PRRS.

H8. APOSB has a positive and significant influence on PRRS

H9. AFAOSB has a positive and significant influence on PRRS.

## 4. Methodology

## 4.1. Sampling and data collection

The empirical study's data collection tool was an online anonymous questionnaire sent via email to a large group of undergraduate and graduate students, who participated voluntarily in the study. Student sampling was previously employed for research on the use of RSs on ecommerce sites (e.g. [41]). In general, young consumers have a favor able attitude to e-commerce, as they are very familiar with online shopping processes and systems [42]. Moreover, younger e-commerce users are generally more aware of privacy issues than older ones, have certain expectations of online retailers regarding their personal or personally identifiable data usage, are more pragmatic with respect to privacy, more responsive regarding information sharing, as well as more informed about and aware of online data collection practices' costs and benefits [43]. Consequently, in our research framework context, student sampling was considered adequate.

The invitation to complete the questionnaire was sent to students of the largest faculty (in terms of the number of students) in one of the largest EU countries (in terms of its population) in June 2019. A total of 632 participants completed the questionnaire, of which the answers of 35 were straight-liners or the participants stated they do not shop online. The final investigated sample, therefore, included 597 valid questionnaires.

Regarding the sample demographics, the average respondent's age was 22.87 years, of whom 60.3% were women. Most of the subject indicated that they generally did their online shopping using a laptop/ desktop (66.0%) and only 34.0% used a mobile device.

## 4.2. Measurements

The measuring of online privacy concerns has received a lot of attention from researchers who developed and validated various measurement scales for this purpose (e.g. the IUIPC – Internet users' information privacy concerns – scale [44]). However, to the best of our knowledge, there is as yet no scale that, in a typical RS typology framework, measures RSs' perceived usefulness and the extent to which ecommerce users are willing to approve these systems' collection and storage of their personal (or personally identifiable) data. Since our research purpose was to capture users' particular attitudes to each of the most popular RS types, we had to develop new scales structured to follow the typical RS structure that most e-commerce sites ofer and to measure attitudes to each RS type.

In order to allow us to measure various RSs' perceived usefulness, respondents were asked to state the extent to which they agreed that RSs providing recommendation based on certain types of information were useful for them (e.g. “Recommendations based on similarity to products I previously bought are very useful”). Furthermore, to assess users' acceptance of the collection and storage of their data, re spondents were asked to express their agreement with RSs' collecting and storing of certain types of data (e.g. “I would agree to an RS collecting and storing my general personal information, such as my gender, age, location”).

The RSs' overall perceived relevance (PRRS) was measured by means of three items. The first item refers to the RSs helping users discover new and interesting things that they would not otherwise have discovered (serendipitous recommendation) [23]. The second relates to the trust that users associate with the recommendations they receive through the RSs [31]. Finally, the third item refers to the relevance of the RSs' recommendations and the extent to which these impact users' purchase decisions [2]. We measured all the items on a five-point Likert scale ranging from “strongly disagree” (1) to “strongly agree” (5). Table 1 presents the descriptive statistics of the 34 items included in the questionnaire.

To ensure that the participants understood and could imagine the real-life situations to which the employed scales referred, we implemented three measures. First, only persons with previous experiences of e-commerce sites and online shopping were included in the sample. Second, the online questionnaire began with a description of what a typical RS means, what it comprises, how it works, and what it looks like on a regular e-commerce site. Third, the structure of the questionnaire followed a typical RS structure that an e-commerce site would use, with each set of items referring to a specific RS type.

## 5. Data analysis, results, and discussion

The collected data were analyzed through the statistical software

SmartPLS version 3.2.8 [45], which employs partial least squares structural equation modeling (PLS-SEM). Even though PLS-SEM has become a quasi-standard in marketing and management research in terms of analyzing cause-efect relationships between latent constructs [46], PLS-SEM-based research is just at the beginning in the information systems and RS fields of study.

In the RS field of research, PLS-SEM was previously used for an exploratory test of a theoretical model on the impact of RSs' use [47], as well as to explore the factors that influence users' confidence in travel tips obtained from smartphone social network services [48]. In these cases, PLS-SEM was a suitable tool, because the authors evaluated the relationships between several latent variables, the method combining the advantages of path analysis, factor analysis, and multiple regression analysis, while simultaneously helping researchers examine the relationship between variables in terms of the explained variation.

PLS-SEM is used appropriately when the research goal is prediction oriented and/or when the research is exploratory by nature and researchers develop theories using multivariate analysis and by focusing on explaining the dependent variables' variance [49]. PLS-SEM was considered a suitable and adequate data analysis method due to our study's exploratory nature, the scarcity of previous research on the topic, and given the current research goals' predictive nature.

## 5.1. Measurements assessment

Table 2 presents the reflective measurements' assessment in terms of their reliability and convergent validity, specifically in terms of the outer loadings, Cronbach's alpha values, composite reliability, and average variance extracted (AVE). The outer loadings indicate the relationships between constructs and indicator variables and are computed for all the constructs. Since outer loadings values are higher than those of the threshold of 0.7 [50], we can conclude that there is an adequate level of indicator reliability. Regarding the internal consistency reliability, since all the composite reliability values and the Cronbach's alpha are considerably above the critical value of 0.7 [49], all the measurements are internally consistent. The average variance extracted (AVE) is a traditional measure to evaluate the constructs convergent validity. Given that all the AVE values are higher than the minimum threshold of 0.5 [51], the convergent validity of all the measurements is established.

In addition, we assessed the employed scales' discriminant validity, using the heterotrait-monotrait ratio of correlations (HTMT). In this case, as can be seen in Table 3, all the HTMT values are lower than the conservative threshold value of 0.85 [52]. Discriminant validity was therefore established between all the construct pairs.

## 5.2. Structural model assessment

## 5.2.1. Collinearity issues assessment

Before the evaluation of the structural model, the collinearity be tween the predictor constructs needs to be examined. Table 4 shows the VIF values of all the combinations of endogenous constructs and the corresponding exogenous constructs, which are, as can be observed, all below the threshold of 3 [50]. Consequently, the collinearity between the predictor constructs is not an issue in the current structural model.

## 5.2.2. Structural model relationships and discussion

The statistical significance of the relationships between the constructs, as well as the size of the corresponding path coeficients, were first analyzed to evaluate the structural model. Fig. 2 shows a graphic representation of the structural model's assessment, while Table 5 presents a summary of the results. As the results show, all the hypotheses are confirmed, with the exceptions of H6, H2a, and H2c. Consequently, the RSs' perceived usefulness positively and significantly influences users' acceptance of such systems collecting and storing their data. Furthermore, the extent to which users accept having their data combined for recommendation purposes positively impacts RSs' perceived overall relevance. In the case of an RS based on personal online shopping behavior, its perceived usefulness's highest impact is on users acceptance of having their data on their likes/dislikes shared, followed by their shopping behavior data. Although not surprising, this result is useful, since developers should focus on providing higher user utility within such systems in order to have better access to this type of data.

Table 1  
Questionnaire items, constructs, and descriptive statistics.

<table><tr><td>Latent reflective variable</td><td>Reflective indicators</td><td>Description</td><td>Mean</td><td>Deviation</td></tr><tr><td rowspan="6">Perceived usefulness - personal online shopping behavior (PUOSB)</td><td>PUOSB1</td><td>Similarity to the products previously bought</td><td>3.712</td><td>0.958</td></tr><tr><td>PUOSB2</td><td>Browsing history (time spent on product / movie page)</td><td>3.340</td><td>0.942</td></tr><tr><td>PUOSB3</td><td>Similarity to liked products</td><td>3.690</td><td>0.889</td></tr><tr><td>PUOSB4</td><td>Similar products (based on similar characteristics)</td><td>3.576</td><td>0.854</td></tr><tr><td>PUOSB5</td><td>Similarity to viewed products*</td><td>3.497</td><td>0.862</td></tr><tr><td>PUOSB6</td><td>Complementary products / Accessories*</td><td>3.291</td><td>0.966</td></tr><tr><td rowspan="4">Perceived usefulness - others&#x27; online shopping behavior (PUOOSB)</td><td>PUOOSB1</td><td>Other users who have an interest in the product</td><td>2.754</td><td>1.000</td></tr><tr><td>PUOOSB2</td><td>Products bought together by other users</td><td>2.874</td><td>0.970</td></tr><tr><td>PUOOSB3</td><td>Products viewed, liked or purchased together by social media peers</td><td>2.998</td><td>1.046</td></tr><tr><td>PUOOSB4</td><td>Products seen / liked frequently by other users</td><td>3.067</td><td>0.952</td></tr><tr><td rowspan="2">Perceived usefulness - special offers (PUSO)</td><td>PUSO1</td><td>Products on offer</td><td>3.479</td><td>1.104</td></tr><tr><td>PUSO2</td><td>Products on offer considering the product category</td><td>3.447</td><td>1.144</td></tr><tr><td rowspan="4">Perceived usefulness - general trends (PUGT)</td><td>PUGT1</td><td>What users are buying now</td><td>2.772</td><td>1.077</td></tr><tr><td>PUGT2</td><td>Popular / best-selling products</td><td>3.477</td><td>1.017</td></tr><tr><td>PUGT3</td><td>Top products / brands</td><td>3.420</td><td>1.019</td></tr><tr><td>PUGT4</td><td>Trendy products</td><td>3.263</td><td>1.043</td></tr><tr><td rowspan="2">Acceptance - likes/dislikes (ALD)</td><td>ALD1</td><td>What I dislike</td><td>3.844</td><td>1.039</td></tr><tr><td>ALD2</td><td>What I like</td><td>4.067</td><td>0.887</td></tr><tr><td rowspan="2">Acceptance - personal/ sensitive information (APSI)</td><td>APSI1</td><td>My general personal information (gender, age, location)</td><td>3.090</td><td>1.104</td></tr><tr><td>APSI2</td><td>My sensitive personal information (name, job, address)</td><td>2.295</td><td>1.101</td></tr><tr><td rowspan="3">Acceptance - ratings, reviews, interests (ARRI)</td><td>ARRI1</td><td>Preferences and interests selected from a product list</td><td>3.722</td><td>0.920</td></tr><tr><td>ARRI2</td><td>Reviews / comments after product purchase</td><td>3.988</td><td>0.894</td></tr><tr><td>ARRI3</td><td>Product ratings</td><td>4.015</td><td>0.840</td></tr><tr><td rowspan="3">Acceptance - personal online shopping behavior (APOSB)</td><td>APOSB1</td><td>My purchased products</td><td>3.566</td><td>1.001</td></tr><tr><td>APOSB2</td><td>My viewed products</td><td>3.308</td><td>0.943</td></tr><tr><td>APOSB3</td><td>Number of product views and time spent for viewing</td><td>3.246</td><td>1.103</td></tr><tr><td rowspan="5">Acceptance - friends/acquaintances online shopping behavior (AFAOSB)</td><td>AFAOSB1</td><td>Products wanted or bought by persons I follow on social media</td><td>2.489</td><td>1.060</td></tr><tr><td>AFAOSB2</td><td>Products bought by my social media friends</td><td>2.613</td><td>1.069</td></tr><tr><td>AFAOSB3</td><td>Products wanted by my social media friends</td><td>2.481</td><td>1.051</td></tr><tr><td>AFAOSB4</td><td>Products wanted or bought by my social media friends with whom I constantly and frequently interact</td><td>2.702</td><td>1.096</td></tr><tr><td>AFAOSB5</td><td>Products wanted or bought by my social media friends with whom I interact from time to time</td><td>2.328</td><td>1.045</td></tr><tr><td rowspan="3">Perceived relevance of RS (PRRS)</td><td>PRRS1</td><td>Recommendations help me discover new and interesting things, products or information that I would not otherwise have discovered</td><td>3.652</td><td>0.806</td></tr><tr><td>PRRS2</td><td>I find recommendations useful and trustworthy</td><td>3.333</td><td>0.867</td></tr><tr><td>PRRS3</td><td>Recommendations are useful and influence my purchase decision</td><td>3.303</td><td>0.910</td></tr></table>

<sup>⁎</sup> Deleted from the construct due to low outer loadings.

With regard to an RS based on others' online shopping behavior, its perceived usefulness's highest impact on data collection and storing acceptance refers to friends/acquaintances' shopping behavior, followed by personal/sensitive information. The latter might come as a surprise: Why would users be more inclined to reveal their gender, age, job, and address data if they have a better perception of a system based on others' shopping behavior? A possible reason could be that when users are recommended products based on other users' preferences, they expect customization based on their gender, age, etc.

Regarding the unconfirmed hypotheses H2a and H2c, the perceived usefulness of an RS based on others' online shopping behavior does not impact users' consent positively in terms of having their likes/dislikes data and their ratings/reviews/interests data collected and stored. RS developers could focus on improving users' perceptions of the system's utility in order to implicitly have easier access to these users' data on their personal and friends' online shopping behavior, as well as on personal/sensitive information such as their gender, age, job, etc. However, about users' consent in terms of providing data on their likes/ dislikes, and on their ratings, reviews or interests, developers should try to identify other ways of ensuring users' consent in terms of giving away such data (e.g. developing alternative or supplementary RS, with betterperceived usefulness, and based on personal shopping behavior and special ofers).

Regarding the other two types of RSs taken into account – based on special ofers and general trends – their perceived usefulness has, as expected, a positive impact on the extent to which users are willing to share their reviews, ratings or interests and their friends' and acquaintances' shopping behavior with the RS. Users naturally expect that such systems will consider their interests when suggesting products with special ofers, and take their friends/acquaintances' shopping behavior into account when modeling general market trends (popular/ top/trendy products).

The results also show that the extent to which users consent to their data being collected and stored and the perceived usefulness of the specific types of RS taken into account impact RSs' perceived overall relevance respectively directly and indirectly. In other words, to make RSs more relevant for online users, developers should endeavor to open users more to sharing their data. An important way of doing this is by making the systems as useful as possible. Consequently, it is of the utmost importance for such systems to provide relevant suggestions regarding products or services, which will allow users to perceive them as highly useful and, further, might stimulate such users to consent to their data being collected and stored. Better (i.e. more meaningful and relevant) recommendations lead to users willingly sharing more data with developers, which in turn leads to an improved system and even more user data.

However, there is one unconfirmed hypothesis in this case: the influence that the extent to which users consent to share their personal/ sensitive data has on an RS's perceived overall relevance. Contrary to other types of data indicating that users' higher acceptance rates gen erate better perceptions of an RS's relevance, the impact is non-significant in this case. In terms of maximizing the overall perception of RSs, developers should, therefore, focus on those types of data indicating that users' acceptance is impactful: likes/dislikes, ratings/reviews/interests, personal online shopping behavior, friends' online shopping behavior.

Table 2  
Convergent validity and internal consistency assessment of the reflective vari ables.

<table><tr><td>Latent reflective variable</td><td>Reflective indicators</td><td>Outer loadings</td><td>Cronbach&#x27;s Alpha</td><td>Composite Reliability</td><td>Average Variance Extracted (AVE)</td></tr><tr><td rowspan="4">PUPOSB</td><td>PUPOSB1</td><td>0.808</td><td>0.781</td><td>0.859</td><td>0.605</td></tr><tr><td>PUPOSB2</td><td>0.753</td><td></td><td></td><td></td></tr><tr><td>PUPOSB3</td><td>0.825</td><td></td><td></td><td></td></tr><tr><td>PUPOSB4</td><td>0.721</td><td></td><td></td><td></td></tr><tr><td rowspan="4">PUOOSB</td><td>PUOOSB1</td><td>0.777</td><td>0.811</td><td>0.876</td><td>0.639</td></tr><tr><td>PUOOSB2</td><td>0.837</td><td></td><td></td><td></td></tr><tr><td>PUOOSB3</td><td>0.783</td><td></td><td></td><td></td></tr><tr><td>PUOOSB4</td><td>0.798</td><td></td><td></td><td></td></tr><tr><td rowspan="2">PUSO</td><td>PUSO1</td><td>0.963</td><td>0.931</td><td>0.966</td><td>0.935</td></tr><tr><td>PUSO2</td><td>0.971</td><td></td><td></td><td></td></tr><tr><td rowspan="4">PUGT</td><td>PUGT1</td><td>0.802</td><td>0.830</td><td>0.884</td><td>0.657</td></tr><tr><td>PUGT2</td><td>0.799</td><td></td><td></td><td></td></tr><tr><td>PUGT3</td><td>0.809</td><td></td><td></td><td></td></tr><tr><td>PUGT4</td><td>0.830</td><td></td><td></td><td></td></tr><tr><td rowspan="2">ALD</td><td>ALD1</td><td>0.875</td><td>0.793</td><td>0.904</td><td>0.824</td></tr><tr><td>ALD2</td><td>0.940</td><td></td><td></td><td></td></tr><tr><td rowspan="2">APSI</td><td>APSI1</td><td>0.884</td><td>0.656</td><td>0.853</td><td>0.743</td></tr><tr><td>APSI2</td><td>0.840</td><td></td><td></td><td></td></tr><tr><td rowspan="3">ARRI</td><td>ARRI1</td><td>0.785</td><td>0.666</td><td>0.816</td><td>0.597</td></tr><tr><td>ARRI2</td><td>0.787</td><td></td><td></td><td></td></tr><tr><td>ARRI3</td><td>0.745</td><td></td><td></td><td></td></tr><tr><td rowspan="3">APOSB</td><td>APOSB1</td><td>0.836</td><td>0.767</td><td>0.865</td><td>0.681</td></tr><tr><td>APOSB2</td><td>0.828</td><td></td><td></td><td></td></tr><tr><td>APOSB3</td><td>0.812</td><td></td><td></td><td></td></tr><tr><td rowspan="5">AFAOSB</td><td>AFAOSB1</td><td>0.879</td><td>0.924</td><td>0.943</td><td>0.767</td></tr><tr><td>AFAOSB2</td><td>0.848</td><td></td><td></td><td></td></tr><tr><td>AFAOSB3</td><td>0.901</td><td></td><td></td><td></td></tr><tr><td>AFAOSB4</td><td>0.903</td><td></td><td></td><td></td></tr><tr><td>AFAOSB5</td><td>0.847</td><td></td><td></td><td></td></tr><tr><td rowspan="3">PRRS</td><td>PRRS1</td><td>0.807</td><td>0.752</td><td>0.858</td><td>0.668</td></tr><tr><td>PRRS2</td><td>0.799</td><td></td><td></td><td></td></tr><tr><td>PRRS3</td><td>0.847</td><td></td><td></td><td></td></tr></table>

## 5.2.3. Model fit

In order to evaluate the model's goodness of fit, we used the standardized root mean square residual (SRMR) indicator. The obtained SRMR value is 0.06 for the saturated model and 0.08 for the estimated model. The SRMR value is less than the threshold of 0.08 [53] for the saturated model, but at the threshold level for the estimated model, indicating the latter's borderline goodness of fit. However, the notion of fit is not so relevant in this context, as the analyzed model aims to find a solution based on prediction [49]. Aside from assessing the goodness of fit, the structural model also needed to be primarily assessed on its predictive capabilities.

Table 4  
Collinearity assessment among the predictor constructs (Inner VIF values).

<table><tr><td></td><td>AFAOSB</td><td>ALD</td><td>APOSB</td><td>APSI</td><td>ARRI</td><td>PRRS</td></tr><tr><td>AFAOSB</td><td></td><td></td><td></td><td></td><td></td><td>1.295</td></tr><tr><td>ALD</td><td></td><td></td><td></td><td></td><td></td><td>1.302</td></tr><tr><td>APOSB</td><td></td><td></td><td></td><td></td><td></td><td>1.493</td></tr><tr><td>APSI</td><td></td><td></td><td></td><td></td><td></td><td>1.392</td></tr><tr><td>ARRI</td><td></td><td></td><td></td><td></td><td></td><td>1.217</td></tr><tr><td>PRRS</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PUSO</td><td></td><td></td><td></td><td></td><td>1.064</td><td></td></tr><tr><td>PUGT</td><td>1.330</td><td></td><td>1.364</td><td></td><td></td><td></td></tr><tr><td>PUOOSB</td><td>1.330</td><td>1.145</td><td>1.417</td><td>1.145</td><td>1.178</td><td></td></tr><tr><td>PUPOSB</td><td></td><td>1.145</td><td>1.174</td><td>1.145</td><td>1.161</td><td></td></tr></table>

## 5.2.4. Predictive relevance

To evaluate the model's predictive relevance, the $\mathbb { R } ^ { 2 }$ and $Q ^ { 2 }$ values of the target variable (PRRS) were first computed. The $\mathbb { R } ^ { 2 }$ value of the final dependent variable in the model is 0.256, denoting moderate predictive accuracy [50]. The $Q ^ { 2 }$ value of the target dependent variable in the model is 0.16, indicating its moderate predictive power [50].

Furthermore, we emploved the PLSPredict algorithm to better assess the model's predictive power. This algorithm was developed by Shmuel et al. [54] and uses training and holdout samples to generate and evaluate predictions from PLS path model estimations. As Table 6 shows, all the $Q ^ { 2 }$ values are positive, while the PLS-SEM results' (RMSE) prediction errors are smaller for each indicator than the prediction error obtained by simply using the mean values. The investigated model, therefore, ofers better predictive performance than the naïve benchmark model. In other words, the PLS-SEM results have a lower prediction error in terms of RMSE than the LM for all the items, which indicates that the proposed model has high predictive power.

## 6. Conclusions

The current research's goal was to predict the extent to which ecommerce users are willing to share their online data with RSs providers, given the perceived benefits of using such systems as antecedents. Besides, we analyzed the extent to which RSs' perceived usefulness and users' consent to RSs collecting and storing their data impact their perceived overall relevance.

The results showed that RSs' perceived usefulness positively and significantly influences the extent to which e-commerce users consent to RS providers collecting and storing their data. We outlined that in each of the four types of RSs (based on users' personal online shopping behavior, on other users' online shopping behavior, on general shopping trends, and on special ofers), the more useful users perceive the system to be, the more willing they are to share their data with the RSs' developers. However, users' acceptance of RSs collecting and storing various types of data is not equally influenced by all types of RS. First, in terms of an RS based on personal online shopping behavior, its perceived usefulness's highest impact is on users' consent to share their likes/dislikes data and their personal shopping behavior data. Second, if an RS based on others' online shopping behavior is considered, the highest impact of its perceived usefulness is in terms of data on friends/ acquaintances' shopping behavior and on the user's personal/sensitive information. Third, in the case of an RS based on special ofers or of one based on general trends, the perceived usefulness has a positive impact on users' consent to share their reviews/ratings/interests data and their friends' and acquaintances' shopping behavior data.

Table 3  
Discriminant validity assessment for the reflective variables (HTMT criterion).

<table><tr><td></td><td>AFAOSB</td><td>ALD</td><td>APOSB</td><td>APSI</td><td>ARRI</td><td>PRRS</td><td>PUSO</td><td>PUGT</td><td>PUOOSB</td></tr><tr><td colspan="10">AFAOSB</td></tr><tr><td>ALD</td><td>0.167</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>APOSB</td><td>0.463</td><td>0.453</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>APSI</td><td>0.551</td><td>0.279</td><td>0.646</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ARRI</td><td>0.185</td><td>0.535</td><td>0.356</td><td>0.277</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PRRS</td><td>0.374</td><td>0.456</td><td>0.512</td><td>0.397</td><td>0.414</td><td></td><td></td><td></td><td></td></tr><tr><td>PUSO</td><td>0.157</td><td>0.120</td><td>0.220</td><td>0.186</td><td>0.293</td><td>0.194</td><td></td><td></td><td></td></tr><tr><td>PUGT</td><td>0.365</td><td>0.213</td><td>0.350</td><td>0.365</td><td>0.323</td><td>0.310</td><td>0.415</td><td></td><td></td></tr><tr><td>PUOOSB</td><td>0.636</td><td>0.205</td><td>0.407</td><td>0.445</td><td>0.284</td><td>0.374</td><td>0.249</td><td>0.572</td><td></td></tr><tr><td>PUPOSB</td><td>0.263</td><td>0.574</td><td>0.599</td><td>0.310</td><td>0.454</td><td>0.503</td><td>0.216</td><td>0.382</td><td>0.452</td></tr></table>

![](/api/attachments/Z6NU4BTA/fulltext/images/4af282bcffdadfe89feb4391abe6029e261b549a4e55d678db0ec58873e021af.jpg)  
Fig. 2. Graphic representation of the structural model relationships.

Table 5  
Direct and indirect effects.

<table><tr><td>Hypothesized path</td><td>Path coefficient</td><td>T Statistics</td><td>P Values</td><td>Hypothesis confirmed</td></tr><tr><td>H1a: PUPOSB → ALD</td><td>0.468</td><td>11.615</td><td>0.000</td><td>Yes</td></tr><tr><td>H1b: PUPOSB → APSI</td><td>0.126</td><td>2.575</td><td>0.008</td><td>Yes</td></tr><tr><td>H1c: PUPOSB → ARRI</td><td>0.277</td><td>5.985</td><td>0.000</td><td>Yes</td></tr><tr><td>H1d: PUPOSB → APOSB</td><td>0.390</td><td>8.606</td><td>0.000</td><td>Yes</td></tr><tr><td>H2a: PUOOSB → ALD</td><td>-0.001</td><td>0.028</td><td>0.978</td><td>No</td></tr><tr><td>H2b: PUOOSB → APSI</td><td>0.279</td><td>6.111</td><td>0.000</td><td>Yes</td></tr><tr><td>H2c: PUOOSB → ARRI</td><td>0.076</td><td>1.654</td><td>0.085</td><td>No</td></tr><tr><td>H2d: PUOOSB → APOSB</td><td>0.125</td><td>2.622</td><td>0.009</td><td>Yes</td></tr><tr><td>H2e: PUOOSB → AFAOSB</td><td>0.494</td><td>12.963</td><td>0.000</td><td>Yes</td></tr><tr><td>H3: PUSO → ARRI</td><td>0.165</td><td>4.087</td><td>0.000</td><td>Yes</td></tr><tr><td>H4a: PUGT → APOSB</td><td>0.113</td><td>2.267</td><td>0.022</td><td>Yes</td></tr><tr><td>H4b: PUGT → AFAOSB</td><td>0.115</td><td>2.827</td><td>0.004</td><td>Yes</td></tr><tr><td>H5: ALD → PRRS</td><td>0.205</td><td>4.251</td><td>0.000</td><td>Yes</td></tr><tr><td>H6: APSI → PRRS</td><td>0.061</td><td>1.390</td><td>0.161</td><td>No</td></tr><tr><td>H7: ARRI → PRRS</td><td>0.127</td><td>2.691</td><td>0.009</td><td>Yes</td></tr><tr><td>H8: APOSB → PRRS</td><td>0.193</td><td>4.004</td><td>0.000</td><td>Yes</td></tr><tr><td>H9: AFAOSB → PRRS</td><td>0.164</td><td>4.022</td><td>0.000</td><td>Yes</td></tr><tr><td>PUGT → PRRS (Indirect effect)</td><td>0.041</td><td>2.905</td><td>0.004</td><td></td></tr><tr><td>PUOOSB → PRRS (Indirect effect)</td><td>0.131</td><td>5.049</td><td>0.000</td><td></td></tr><tr><td>PUPOSB → PRRS (Indirect effect)</td><td>0.214</td><td>6.872</td><td>0.000</td><td></td></tr><tr><td>PUSO → PRRS (Indirect effect)</td><td>0.021</td><td>2.298</td><td>0.022</td><td></td></tr></table>

Table 6  
Predictive power assessment using the PLSpredict procedure

<table><tr><td rowspan="2">Indicator</td><td colspan="2">PLS</td><td>LM</td><td rowspan="2"> $RMSE_{PLS} < RMSE_{LM}$ </td><td rowspan="2">Predictive power</td></tr><tr><td>RMSE</td><td> $Q^{2}_{-}predict$ </td><td>RMSE</td></tr><tr><td>PRRS1</td><td>0.763</td><td>0.107</td><td>0.770</td><td>Yes</td><td>High</td></tr><tr><td>PRRS2</td><td>0.820</td><td>0.108</td><td>0.830</td><td>Yes</td><td></td></tr><tr><td>PRRS3</td><td>0.855</td><td>0.121</td><td>0.856</td><td>Yes</td><td></td></tr></table>

Info: PLS = prediction using PLS-SEM; LM = prediction using a linear model; RMSE = root mean squared error

The results also showed that users' perceptions of RSs' overall relevance depend on their data sharing acceptance (directly) and on the systems' perceived usefulness (indirectly). From a practical point of view, these results suggest that RS developers should pay attention to their systems' usefulness, taking into account their users' perspective. In other words, the better and more relevant the systems' suggestions are, the more willing users will be to share their data with the systems' developers. In turn, this will lead to better suggestions, and even more valuable data that the users would share afterward.

Our research results have practical implications for e-commerce industry players and for authorities at a national and an international level who are responsible for online data privacy regulations. Additionally, this paper's findings could foster RSs' transparency, since competitors in this field will gain an understanding of the benefits of being open about what user data they process, how they do so, and for what reason. Our results suggest that it is of paramount importance for RS providers to develop practical privacy-preserving techniques to maintain personalized recommendation services' intelligence while re specting user privacy. This can be done, for example, by allowing all users to set their own privacy level and by suggesting relevant recommendations based on the data retrieved through their consent. Users should, therefore, be notified that the greater the amount of personal data a recommender collects, the more accurate and relevant its recommendations. Further, the experience will allow users to understand that the exchange of their data for relevant recommendations is a fair one.

Concerning this study's limitations, since the investigated sample comprised only young respondents in ongoing higher education, the results' generalizability is limited. However, these types of consumers are an important part of the online shopping population, and probably the most important part of this population in the near future when their careers have advanced and their incomes increased. The scarcity of previous research on the topic and, inherently, the unavailability of previously developed and validated scales targeted at measuring RSs' perceived usefulness and data sharing acceptance are two more limitations. These limitations forced us to conduct an exploratory study and to propose new scales for approaching all types of RSs and all types of data that such systems use.

In terms of future research directions, the impact of privacy issues and incidents (e.g. data theft via system cracking) on users' willingness to further share their data with RS providers is an important aspect requiring more research. Various psychological characteristics' (e.g. self-esteem, narcissism, extraversion, etc.) influence users' acceptance or not of having RSs providers collect and store their data would be another important and relevant research topic whose results would be extremely useful for market segmentation and better customization within RSs. In addition, future research should also focus on serendipity recommendations. These recommendations are unexpected, yet fortunate and useful to e-commerce users [23], thus avoiding narrowing down users' options when seeing only similar items, while also enhancing users' capability of imagination and creativity.

## Credit authorship statement

## Category 1

Conception and design of study: D. Mican, O.I. Moisescu, D.A. Sitar-Tăut;

acquisition of data: D.A. Sitar-Tăut, D. Mican;

analysis and/or interpretation of data: O.I. Moisescu, D. Mican, D.A. Sitar-Tăut.

## Category 2

Drafting the manuscript: D. Mican, O.I. Moisescu, D.A. Sitar-Tăut; revising the manuscript critically for important intellectual content: D. Mican, O.I. Moisescu, D.A. Sitar-Tăut.

## Category 3

Approval of the version of the manuscript to be published (the names of all authors must be listed): D. Mican, D.A. Sitar-Tăut, O.I. Moisescu.

## References

[1] J. Ben Schafer, J. Konstan, J. Riedi, Recommender systems in e-commerce, in: Proc. 1st ACM Conf. Electron. Commer. - EC ’99, ACM Press, New York, USA, New York,

1999, pp. 158–166, , https://doi.org/10.1145/336992.337035.

[2] B. Xiao, I. Benbasat, An empirical examination of the influence of biased persona lized product recommendations on consumers’ decision making outcomes, Decis. Support. Syst. 110 (2018) 46–57, https://doi.org/10.1016/J.DSS.2018.03.005.

[3] B. Pathak, R. Garfinkel, R.D. Gopal, R. Venkatesan, F. Yin, Empirical analysis of the impact of recommender systems on sales, J. Manag. Inf. Syst. 27 (2010) 159–188, https://doi.org/10.2753/MIS0742-1222270205.

[4] B. Paudel, F. Christofel, C. Newell, A. Bernstein, Updatable, accurate, diverse, and scalable recommendations for interactive applications, ACM Trans. Interact. Intell. Syst. 7 (2016) 1–34, https://doi.org/10.1145/2955101.

[5] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommender systems, Computer (Long. Beach. Calif). 42 (2009) 30–37, https://doi.org/10. 1109/MC.2009.263

[6] A. Tsesis, Marketplace of ideas, privacy, and digital audiences, Notre Dame Law Rev, 94 (2018) 1585–1630.

[7] W.G. Voss, K.A. Houser, Personal Data and the GDPR: Providing a Competitive Advantage for U.S. Companies, Am. Bus. Law J. 56 (2019), https://doi.org/10. 1111/abli,12139 287-344

[8] I. Mohallick, Ö. Özgöbek, Exploring privacy concerns in news recommender sys tems, in: Proc. - 2017 IEEE/WIC/ACM Int. Conf. Web Intell. WI 2017, NY, USA, (2017), https://doi.org/10.1145/3106426.3109435 1054–1061.

[9] C. Wang, Y. Zheng, J. Jiang, K. Ren, Toward privacy-preserving personalized re commendation services, Engineering. 4 (2018) 21–28, https://doi.org/10.1016/j eng.2018.02.005.

[10] A.J.P. Jeckmans, M. Beye, Z. Erkin, P. Hartel, R.L. Lagendijk, Q. Tang, Privacy in Recommender Systems, in: Springer, London, (2013), pp. 263–281, https://doi.org 10.1007/978-1-4471-4555-4.12

[11] L. Burbach, J. Nakayama, N. Plettenberg, M. Ziele, A.C. Valdez, User Preferences in Recommendation Algorithms, in: RecSys 2018 - 12th ACM Conf, Recomm. Syst, NY, USA, 2018, pp. 306–310, https://doi.org/10.1145/3240323.3240393.

[12] J. Isaak, M.J. Hanna, User data privacy: Facebook, Cambridge Analytica, and privacy protection, Computer (Long. Beach. Calif). 51 (2018) 56–59, https://doi. org/10.1109/MC.2018.3191268.

[13] I.R. Blakesley, A.C. Yallop, What do you know about me? Digital privacy and online data sharing in the UK insurance sector, J. Inf. Commun. Ethics Soc. 18 (2019) 281–303, https://doi.org/10.1108/JICES-04-2019-0046.

[14] S.C. Boerman, S. Kruikemeier, F.J. Zuiderveen Borgesius, Online behavioral advertising: a literature review and research agenda, J. Advert. 46 (2017) 363–376 https://doi.org/10.1080/00913367.2017.1339368.

[15] J.P. Choi, D.S. Jeon, B.C. Kim, Privacy and personal data collection with informa tion externalities, J. Public Econ. 173 (2019) 113–124, https://doi.org/10.1016/j. ipubeco.2019.02.001.

[16] F. Brian, C. Timberg, The FCC Just Passed Sweeping New Rules to Protect your Online Privacy - the Washington Post, Washington Post, https://www. washingtonpost.com/news/the-switch/wp/2016/10/27/the-fcc-just-passedsweeping-new-rules-to-protect-your-online-privacy/, (2016) , Accessed date: 2 July 2020.

[17] Einat Weiss, Data privacy rules are changing. How can marketers keep up? Harv. Bus. Rev. (2020), https://hbr.org/2020/08/data-privacy-rules-are-changing-how can-marketers-keep-up , Accessed date: 27 September 2020.

[18] I. Mazeh, E. Shmueli, A personal data store approach for recommender systems: enhancing privacy without sacrificing accuracy. Expert Syst. Appl. 139 (2020) 112858. https://doi.org/10.1016/i.eswa.2019.112858.

[19] A.C. Valdez, M. Ziefle, K. Verbert, HCI for recommender systems: The past, the present and the future, in: RecSys 2016 - Proc. 10th ACM Conf, Recomm. Syst., NY USA, (2016), pp. 123–126, https://doi.org/10.1145/2959100.2959158.

[20] D. Jannach, M. Zanker, M. Ge, M. Gröning, Recommender Systems in Computer Science and Information Systems - a Landscape of Research, in: Lect, Notes Bus, Inf Process., Springer, (2012), pp. 76–87, https://doi.org/10.1007/978-3-642-32273- 0\_7.

[21] D.H. Park, H.K. Kim, I.Y. Choi, J.K. Kim, A literature review and classification of recommender systems research, Expert Syst, Appl. 39 (2012) 10059–10072. https://doi.org/10.1016/j.eswa.2012.02.038.

[22] J. Lu, D. Wu, M. Mao, W. Wang, G. Zhang, Recommender system application developments: a suryey, Decis. Support. Syst. 74 (2015) 12–32, https://doi,org/10. 1016/JDSS 2015.03.008

[23] C.-D. Wang, Z.-H. Deng, J.-H. Lai, P.S. Yu, Serendipitous recommendation in E commerce using innovator-based collaborative filtering, IEEE Trans. Cybern. 49 (2019) 2678–2692, https://doi.org/10.1109/TCYB.2018.2841924.

[24] E.R. Núñez-Valdéz, J.M. Cueva Lovelle, O. Sanjuán Martínez, V. García-Díaz, P. Ordoñez de Pablos, C.E. Montenegro Marín, Implicit feedback techniques on recommender systems applied to electronic books, Comput. Hum. Behav. 28 (2012) 1186–1193, https://doi.org/10.1016/i.chb.2012.02.001.

[25] J. Ben Schafer, J.A. Konstan, J. Riedl, E-Commerce Recommendation Applications, in: Appl. Data Min. to Electron. Commer., Springer US, (2001), pp. 115–153, https://doiorg/10.1007/978-1-4615-1627-9.6

[26] L. Esmaeili, S. Mardani, S.A.H. Golpayegani, Z.Z. Madar, A novel tourism recommender system in the context of social commerce, Expert Syst. Appl. 149 (2020) 113301, https://doi.org/10.1016/j.eswa.2020.113301.

[27] M.I. Martín-Vicente, A. Gil-Solla, M. Ramos-Cabrer, J.J. Pazos-Arias, Y. Blanco-Fernández. M. López-Nores. A semantic approach to improve neighborhood for: mation in collaborative recommender systems, Expert Syst. Appl. 41 (2014) 7776–7788. https://doi.org/10.1016/i.eswa.2014.06.038.

[28] M. Sato, H. Izumo, T. Sonoda, Discount Sensitive Recommender System for Retail Business, in: Proc. Emp. ’15, ACM Press, New York, New York, USA, 2015, pp. 33–40. https://doi.org/10.1145/2809643.2809646

[29] P.U. Kouki Santa Cruz, J. Schafer, J. Pujara, L. Getoor, P. Kouki, Personalized Explanations for Hybrid Recommender Systems, in: Proc. 24th Int. Conf. Intell. User Interfaces, ACM, New York, 2019, p. 12, https://doi.org/10.1145/3301275. 3302306.

[30] Y. Koren, Recommender system utilizing collaborative filtering combining explicit and implicit feedback with both neighborhood and latent factor models, U.S. Patent No. 8,037,080. 11 Oct, (2011).

[31] Y. Wang, L. Qian, F. Li, L. Zhang, A comparative study on shilling detection methods for trustworthy recommendations, J. Syst. Sci. Syst. Eng. 27 (2018) 458–478, https://doi.org/10.1007/s11518-018-5374-8.

[32] Z. Sun, K.D. Strang, F. Pambel, Privacy and security in the big data paradigm, J. Comput. Inf. Syst. 60 (2020) 146–155, https://doi.org/10.1080/08874417.2017. 1418631.

[33] Z. Lv, H. Song, P. Basanta-Val, A. Steed, M. Jo, Next-generation big data analytics: state of the art, challenges, and future research topics, IEEE Trans. Ind. Informatics. 13 (2017) 1891–1899, https://doi.org/10.1109/TII.2017.2650204.

[34] S. Gurses, J.M. del Alamo, Privacy engineering: shaping an emerging field of research and practice, IEEE Secur. Priv. 14 (2016) 40–46, https://doi.org/10.1109/ MSP.2016.37.

[35] H.S. Choi, W.S. Lee, S.Y. Sohn, Analyzing research trends in personal information privacy using topic modeling, Comput. Secur. 67 (2017) 244–253, https://doi.org 10.1016/i.cose.2017.03.007

[36] S.C. Boerman, S. Kruikemeier, F.J. Zuiderveen Borgesius, Exploring motivations for online privacy protection behavior: insights from panel data, Commun. Res. 009365021880091 (2018), https://doi.org/10.1177/0093650218800915.

[37] V.M. Wottrich, E.A. van Reiimersdal, E.G. Smit, The privacy trade-off for mobile app downloads: the roles of app value, intrusiveness, and privacy concerns, Decis. Support. Syst. 106 (2018) 44–52, https://doi.org/10.1016/j.dss.2017.12.003.

[38] A. Calero Valdez, M. Ziefle, The users’ perspective on the privacy-utility trade-ofs in health recommender systems, Int. J. Hum. Comput. Stud. 121 (2019) 108–121, https://doi.org/10.1016/j.ijhcs.2018.04.003.

[39] L. Ardissono, N. Mauro, A compositional model of multi-faceted trust for personalized item recommendation, Expert Syst. Appl. 140 (2020) 112880, https://doi.org 10.1016/j.eswa.2019.112880.

[40] A.R. Smink, S. Frowijn, E.A. van Reijmersdal, G. van Noort, P.C. Neijens, Try online before vou buy: how does shopping with augmented reality affect brand responses and personal data disclosure, Electron. Commer. Res. Appl. 35 (2019) 100854, https://doi.org/10.1016/j.elerap.2019.100854.

[41] E. Lepkowska-White, Are they listening? Designing online recommendations for today’s consumers, J. Res. Interact. Mark. 7 (2013) 182–200, https://doi.org/10. 1108/JRIM-0Z-2012-002Z

[42] M. Dharmesti, T.R.S. Dharmesti, S. Kuhne, P. Thaichon, Understanding Online Shopping Behaviours and Purchase Intentions amongst Millennials, Young Consum, (2019), https://doi.org/10.1108/YC-12-2018-0922

[43] I.D. Anic, V. Škare, I. Kursan Milaković, The determinants and efects of online privacy concerns in the context of e-commerce, Electron. Commer. Res. Appl. 36 (2019) 100868, https://doi.org/10.1016/j.elerap.2019.100868.

[44] N.K. Malhotra, S.S. Kim, J. Agarwal, Internet users’ information privacy concerns (IUIPC): the construct, the scale, and a causal model, Inf. Syst. Res. 15 (2004) 336–355, https://doi.org/10.1287/isre.1040.0032.

[45] J.-M. Ringle, M. Christian, Sven Wende, Becker, SmartPLS 3, Boenningstedt SmartPLS GmbH. http://www.smartpls.com. (2015).

[46] J.F. Hair, C.M. Ringle, M. Sarstedt, PLS-SEM: indeed a silver bullet, J. Mark. Theory Pract. 19 (2011) 139–152. https://doi,org/10.2753/MTP1069-6679190202.

[47] M.R. Hasan, A.K. Jha, Y. Liu, Excessive use of online video streaming services: impact of recommender system use, psychological factors, and motives, Comput. Hum. Behav, 80 (2018) 220–228. https://doi,org/10.1016/i.chb.2017.11.020.

[48] S.E. Chang, W.-C. Shen, A.Y. Liu, Why mobile users trust smartphone social networking services? A PLS-SEM approach, J. Bus. Res. 69 (2016) 4890–4895, https:/ doi.org/10.1016/j.jbusres.2016.04.048.

[49] J.F. Hair, G.T.M. Hult, C.M. Ringle. M. Sarstedt. A Primer on Partial Least Squares Structural Equation Modeling (PLS-SEM). SAGE Publications, 2016

[50] J.F. Hair, J.J. Risher, M. Sarstedt, C.M. Ringle, When to use and how to report the results of PLS-SEM. Eur. Bus, Rev, 31 (2019) 2–24. https://doi,org/10.1108/EBR-

11-2018-0203.

[51] C. Fornell, D.F. Larcker, Evaluating structural equation models with unobservable variables and measurement error, J. Mark. Res. 18 (1981) 39, https://doi.org/10. 2307/3151312

[52] J. Henseler, C.M. Ringle, M. Sarstedt, A new criterion for assessing discriminant validity in variance-based structural equation modeling, J. Acad. Mark. Sci. 43 (2015) 115–135, https://doi.org/10.1007/s11747-014-0403-8

[53] J. Henseler, G. Hubona, P.A. Ray, Using PLS path modeling in new technology research: updated guidelines, Ind. Manag. Data Syst. 116 (2016) 2–20, https://doi. org/10.1108/IMDS-09-2015-0382.

[54] G. Shmueli, S. Ray, J.M. Velasquez Estrada, S.B. Chatla, The elephant in the room: predictive performance of PLS models, J. Bus. Res. 69 (2016) 4552–4564, https:/ doi.org/10.1016/LJBUSRES.2016.03.049

![](/api/attachments/Z6NU4BTA/fulltext/images/1cf3f6f2135c3ae537a8c2353cccc67d48098adad34562d899b59d8bea65df75.jpg)

Daniel Mican is an Assistant Professor at the Faculty of Economics and Business Administration, Babeş-Bolyai University of Cluj-Napoca, România, within the Department of Business Information Systems. He completed his Ph.D. in 2013 in Cybernetics and Economic Statistics. His research interests are in the field of recommendation systems, web usage mining, collective intelligence and social networking. He also works as a consultant project manager and web developer for FSEGA and companies from Europe and US.

![](/api/attachments/Z6NU4BTA/fulltext/images/84501df9d751744b0a559721fbac2469d0db639428930443c07bf593bb3a2753.jpg)

Dan-Andrei Sitar-Tăut is an Associate Professor at the Faculty of Economics and Business Administration. He has a Bachelor's degree in Business Information Systems from Faculty of Economics and Business Administration, Babeş- Bolyai University of Cluj-Napoca and a Master's degree in Informatics Strategies Applied in Economy and Business from the same educational institution. He also holds a PhD diploma in Cybernetics and Economic Statistics. He is the author of 3 books, co-author of another 30 books, 50 papers in the field of Databases, ERP, Data mining, and Web related subdomains. Mr. Dan Sitar occupied the manager position in 2 national research projects and he was member in research teams in other 20 projects. He is Editorial Assistant in STUDIA OECONOMICA Universitatis Babes

Bolyai board.

![](/api/attachments/Z6NU4BTA/fulltext/images/16ea28c1e1fa14d602e85b9ff37dcd52d1d6abf67a64903a95ef5de127073d46.jpg)

Ovidiu-Ioan Moisescu is Associate Professor in Marketing and Branding at Babeș-Bolyai University of Cluj-Napoca, Romania. He completed his PhD in Marketing at the West University of Timișoara (Romania), as well as postdoctoral research proiect at Babes-Bolvai University of Clui-Napoca (Romania) and Corvinus University of Budapest (Hungary). His research focuses on consumer behavior, brand equity, CSR and PLS-SEM methodological issues in marketing.
