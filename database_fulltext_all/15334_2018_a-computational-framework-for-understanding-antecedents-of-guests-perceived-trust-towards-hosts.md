---
otero_id: 15334
otero_key: "XKSA4RYA"
title: "A computational framework for understanding antecedents of guests' perceived trust towards hosts on Airbnb"
authors: "Le Zhang; Qiang Yan; Leihan Zhang"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A computational framework for understanding antecedents of guests' perceived trust towards hosts on Airbnb

Le Zhang<sup>a</sup>, Qiang Yan<sup>a,\*</sup>, Leihan Zhang

<sup>a</sup> School of Economics and Management, Beijing University of Posts and Telecommunications, Beijing 100876, PR China <sup>b</sup> Institute of Computer Science and Technology, Peking University, Beijing 100871, PR China

## A R T I C L E I N F O

Keywords: Airbnb Perceived trust Antecedents Sentiment Self-description

## A B S T R A C T

Several studies have researched the antecedents influencing the perceived trust of guests towards hosts on Airbnb typically relying on survey data. However, the contribution of these antecedents to trust building in a practical context remains unclear. To fill this gap, we focused on the antecedents within the manageable information about hosts and proposed a computational framework for understanding the antecedents influencing perceived trust. Specifically, perceived trust was proxied by the growth rate of bookings and the validity of the proxy method was proved through comparing with human labeled data. From the snapshot information about hosts, the antecedents were quantified through text mining and face recognition methods. The least square regression was applied to analyze and compare the influence of these antecedents. We found that the contribution of reputation is not less than the summation of all the other antecedents. Additionally, in terms of selfdescriptions, it is worthwhile to pay more attention to interactions and services. Expressing positive sentiment in either self-descriptions or profile photo is also helpful. The response behavior pattern and the number of verifications also matter. At last, several efective trust prediction models were built by using deep neural network and the ensemble method. The findings shed light on the working of the antecedents in trust formation and can provide instructions for the transaction partners, designers and managers of online services in the sharing economy.

## 1. Introduction

In the sharing economy, the trust between providers and consumers forms the basis of a successful resource-sharing transaction. Airbnb is a good example, acting as an online lodging marketplace for short-term peer-to-peer rentals, where guests seek low-cost accommodations and direct interactions with the local community [1]. The necessity of faceto-face interactions implies that the hosts may experience severe da mage to their properties or theft of personal belongings and the guests may also be faced with risk of unreliable hosts or even personal security [2,3]. What's more, the quality of the accommodation service is highly dependent upon the hosts. Therefore, trust, as an eficient mechanism for lowering transaction costs of social exchange [4], is absolutely ne cessary in the sharing economy.

From the guests' perspective on Airbnb, the main sources of in formation for inferring a host's trustworthiness is the online profile provided by the platform, which contains important trust-related cues, such as reviews, rating score, verifications, self-descriptions, profile photos, and so on. According to the characterization of Mayer et al. [5], guests can assess the trustworthiness of hosts with the criteria of ability, integrity, and benevolence, based on the information provided. Indeed, a lot of studies have been performed according to the subjective measurement criteria. However, the subjective measurement methods are not applicable to large scale data and research based on actual trusting behavior in the sharing economy remains scarce, although it can help show the actual working of trust mechanisms. Therefore, it is necessary to develop a computation method to measure perceived trust based on real world data.

For convenience, we will use “perceived trust” to represent “Airbnb guests' perceived trust towards hosts” in the following sections. It should be noted that perceived trust is diferent to trustworthiness. In detail, perceived trust can be considered as the reflected trustworthi ness of the trustees and trustworthiness is subjectively entertained in the judgment of the trustors [6]. From the microscopic perspective, a particular trustee's trustworthiness can be taken as a constant and the perceived trust towards him may difer among trustors. But from the macroscopic perspective, it is generally acknowledged that the more guests trust a trustee, the more trustworthy the trustee probably is. Although trust is not a behavior (e.g. cooperation) or a choice (e.g. take a risk), it is an underlying psychological condition that can cause such actions [7]. And when trusting behavior occurs, it generally means that trust has been built [8]. Accordingly, we assume that perceived trust on Airbnb can be measured based on the accumulated trusting behavior of guests.

Besides of ability, integrity, and benevolence, Sztompka [6] claims that people employ three other criteria in estimating the trustworthiness of their transactional partners: reputation, performance, and appearance. The majority of information online about hosts, presented by Airbnb, can be generally categorized into the three criteria. Thus, by managing the antecedents such as self-description, profile photo, service behavior, hosts can accumulate reputation and earn trust from the guests.

At present, reputation is often regarded as the panacea for establishing trust [2], and a lot of research has been devoted to understanding the inner workings of reputation mechanisms [9,10]. However, trust in the sharing economy is much more complex and extends far beyond reputation [2]. In fact, Airbnb's reciprocal review system enables both hosts and guests to review one another and the reviews tend to comprise a restricted set of highly positive commentary [11]. Except for the reputation system, the impact of linguistic features within self-descriptions and personal photos on trust has also been investigated by manually analyzing limited survey data [12-17]. But, majority of the studies are focusing on isolated antecedents in fabricated settings, and the contribution of these antecedents in real-world trust related behavior remains unclear. Consequently, from the perspective of hosts and platform managers, it is important to gain better understanding about the contribution of the aforementioned antecedents. Haas and Deseran [18] assert that the transaction partners have the burden of not only creating trust but also maintaining it and this process involves the duty of presenting themselves as trustworthy persons. Meanwhile, the self theory suggests that people are constantly engaged in managing and controlling the impressions they make on others to attain their goals [19]. Therefore, we contend that it would be valuable to use a more complete framework that incorporates all possible antecedents within hosts' online information to study the full spectrum of trust-building mechanisms.

In this paper, we propose a computational framework for understanding antecedents of guests' perceived trust based on real-world trust related behavior data of Airbnb. For each host, the perceived trust was proxied by the growth rate of bookings in three months. Then, the antecedents were extracted and quantified from the snapshot of host information. Regression analysis on datasets with both human labeled perceived trust and quantified perceived trust proves the validity of the proxy variable. And our study generated several interesting findings. Among all the antecedents, reputation plays the most important role in building trust, while the rating system was proved to be a failure. In respect to self-descriptions, it is worthwhile to pay more attention to guest's concern, such as interactions and services and use positive words or phrases. Quick response speed and high response rate can represent a hospitable attitude, which can also significantly improve perceived trust. Additionally, more verifications and photos with positive facial expression are also helpful. Based on these antecedents, four predictive models were proposed to identify hosts with higher/lower perceived trust. The findings provide the hosts with a comprehensive set of instruction for presenting themselves efectively and further help earn trust of guests. According to the antecedents influencing guests' perceived trust, the service platforms can focus on building a better trust evaluation system.

The rest of the paper is organized as follows. Section 2 presents related work and relevant theory. In Section 3, the experimental data and methods are introduced. Section 4 introduces the data analysis, empirical result and prediction model. The final section provides a discussion of the findings and concludes with limitations and implications of this study.

## 2. Literature review and theory

## 2.1. Trust in sharing economy

Although trust has been defined in many diferent ways, a widely held definition of trust is as follows: trust is a psychological state comprising the intention to accept vulnerability based upon positive expectations of the intentions or behavior of another [7,20]. Across disciplines, there is agreement on the conditions that must exist for trust to arise: risk and interdependence. Risk is the perceived probability of loss as interpreted by a decision maker [21]. Interdependence means that the interests of one party cannot be achieved without reliance upon another. Although both risk and interdependence are required for trust to emerge, the nature of risk and trust changes as interdependence increases [7,22].

Sharing economy is an economic model based on sharing under utilized resources between peers without the transfer of ownership, ranging from spaces, to skills, for monetary or non-monetary benefits via an online mediated platform [2]. To some extent, sharing economy can be taken as a special case of consumer-to-consumer (C2C) e-commerce, because transactions take place between peers via online platforms and both are faced with similar trust issues, e.g., transaction partners are unable to inspect and evaluate goods upfront. However, sharing economy difers from the C2C e-commerce in three aspects. Firstly, sharing economy is based on “access to” rather than “ownership of” underutilized physical or human assets [23]. Secondly, sharing economy mainly focuses on providing services instead of selling products, such as the short-term rent services (Airbnb) and taxi services (Uber). The quality of these services cannot be checked until being experienced [24]. Thirdly, sharing economy not only involves online transactions, but also may require face-to-face interactions between providers and demanders, which results in greater uncertainty towards service quality, personal security and private asset [15,17,25]. These diferences characterize sharing economy as economic model with higher risk, more uncertainty, and greater interdependence. Since the nature of trust and risk changes as interdependence increases, we contend that trust in the sharing economy is a more complex construct and plays a more important role in overcoming uncertainty and mitigating risk than in traditional settings.

## 2.2. Antecedents of perceived trust

In the context with greater interdependence, the transaction part ners try to overcome uncertainty and mitigate risk by assessing the trustworthiness of transaction partners. A set of criteria has been proposed to make assessments. According to the characterization of Mayer et al. [5], parties can be deemed as trustworthy when they (1) have the required competencies and characteristics that enable them to exert influence within a specific domain, (2) are believed to do good to trustors, keeping the trustor's interests in mind, (3) are perceived to adhere to a set of principles that trustors consider acceptable. This assessment criteria is usually applied to conduct surveys or field research. With regards to the criteria which can be used in computational methods, Sztompka [6] proposed another three criteria: reputation, performance, and appearance. Reputation refers to a record of past deeds. Performance includes actual deeds, present conduct, and currently obtained results. Appearance matters as one's look and self-presentation can exude trustworthiness or stimulate suspicion on the part of the looker [6]. Furthermore, Beldad et al. [26] asserted that the information quality, graphical characteristics, social presence cues, ofline presence can also be used to assess trustworthiness. Since we are aiming to investigate the antecedents of perceived trust by using computational methods, the investigated antecedents will be confined in the manageable information about hosts provided by Airbnb. Considering the aforementioned criteria, we will summarize the research on the antecedents influencing perceived trust from the following aspects: reputation mechanism [9,15,27-29], response behavior pattern [30- 32], verifications [33,34], perceived information quality [13,14,35,36], and profile photos [15,17].

![](/api/attachments/XKSA4RYA/fulltext/images/e7c97afcc6c97fc51438928db46adfc7a2eb2779025a9db4ede2cfc2abea44f1.jpg)  
Fig. 1. The computational framework.

Reputation mechanism, which contains rating scores, ratings, textual review and so on, is one of the most important mechanism to build trust in online marketplaces [37]. The positive ratings or reviews of sellers can generally lead to higher trust levels [9,38]. However, nearly 95% of listings on Airbnb have an average rating higher than 4.5 stars [27] and Airbnb reviews tend to comprise of a very restricted set of highly positive commentary, which results in nearly all Airbnb reviews being positive [11]. The slight diference usually makes it dificult for guests to infer the trustworthiness solely based on the rating score and reviews. What's more, the badge of “superhost” on Airbnb is another important indicator of reputation and hosts with “superhost” badges tend to get higher perceived trust [10].

Besides the reputation system, the response behavior can reflect hosts' hospitality, which can further influence perceived trust. Two aspects of the response behavior are important, namely, the speed of response (the faster, the better [32]) and the response rate. On Airbnb, the host's response rate to guests is a subjective behavior. Hosts who respond to guests quicker and try to solve their problems in a more timely manner can appear to be more hospitable. Moreover, verifications can provide personal identities of a peer and suggest that the peer really exists [33]. Hosts who provide more verification items demonstrate their willingness to be held accountable for their actions, thu increasing their trustworthiness [34].

Perceived information quality can also influence perceived trust [39]. The perceived information quality refers to the perception of the accuracy and completeness of the information provided [40,41]. The self-description of a seller in the form of well written texts, high quality texts can provide cues for personal characteristics, such as perceived social capital, ability, and integrity, which can significantly influence perceived trust [32,35,36]. Ma et al. [14] found that longer self-descriptions can reduce information asymmetry and tend to be perceived as more trustworthy. Additionally, sentiment and semantic topics in self-descriptions can provide more detailed information about hosts, such as profession, personality, and values, which can also influence perceived trust [12-14].

In regards to appearance, the transaction partners' facial expression can also influence house renting [17]. Specifically, the perceived trust based on profile photos can influence guests' choice and the more trustworthy the profile photo, the higher probability of the house being booked [15]. In addition, hosts' smile can act as a signal of kindness, sociability, honesty, pleasantness, politeness [42], which can reduce the distance between two strangers, increase the feeling of familiarity, and improve perceived trust [43].

The above mentioned antecedents can be classified into three kind according to the data type, i.e., numeric, textual, and image. Numeric features have been widely investigated and many researchers now turn to textual and image data and try to mine information quality and facial expression through survey methods [13-15,17]. However, majority of the research is focusing on a few isolated antecedents of perceived trust and the efects of online trustworthiness cues on trust formation do not transcend contextual diferences and are relatively dependant on the context of a particular online transaction and the parties involved in the transaction [26]. Therefore, it would be beneficial to use a more complete framework that incorporates all possible antecedents within the online information. What's more, the transaction partners have the duty of not only creating trust but also maintaining it and this process involves presenting themselves as trustworthy persons [18]. Thus, we contend that it is necessary to investigate the mechanism of how these antecedents influence perceived trust. In respect of the research methods, most studies use survey data to measure the perceptions of trust [15,17] and quantitative research based on trusting behavior in sharing economy remains scarce. Therefore, it is necessary to find a method to measure perceived trust based on trusting behavior data and further identify key antecedents influencing perceived trust by using computational methods.

## 3. Datasets and methods

The computational framework for understanding antecedents influencing perceived trust is outlined in Fig. 1. The framework mainly consists of snapshot data processing, perceived trust quantification, feature engineering, regression analysis, comparison of feature contribution and prediction model. In general, we firstly cleaned and aligned the series data. Then, perceived trust was proxied by the growth rate of bookings. Thirdly, seven group of features, i.e., reputation, response behavior pattern, verification, information quality, sentiment, semantic topic, facial expression, were obtained by using the method of quantitative analysis, text mining and face recognition. Fourthly, regression analysis was performed to find the influence of various antecedents on perceived trust and the contributions of these features were also compared. Finally, the prediction models based on deep neural network and voting mechanism were built and evaluated.

## 3.1. Datasets and preprocessing

This study utilized real world data about tens of thousands of houses in New York, USA from June 1, 2017 to September 30, 2017, which was collected from insideairbnb.com<sup>1</sup>. The dataset is comprised of a series of monthly snapshots of listings (collected in the first two days of each month) and each snapshot contains public information compiled from Airbnb website including information about hosts, the availability calendar for 365 days in the future and reviews for each listing. By aligning the information of listings in the period from June to September according to the listing ID, 33,747 listings with detailed information (superhost status, rating, reviews, verifications, response time, response rate, self-description, photo's URL) were obtained. Firstly, we crawled the photos of hosts based on photo's URL by using python scripts.

Then, for each listing, non-English texts in descriptions was detected and removed by using langdetect<sup>2</sup>. If the self-description contains less than five words, the listing was also dropped. After filtering, 13,003 listings remained. Next, we performed facial recognition on the photos of the 13,003 listings by using Face++<sup>3</sup>, which ofers leading and reliable facial recognition technology in APIs, and finally 3801 listings with facial emotion were obtained (the other photos may either contain no human face or cannot be detected).

## 3.2. The proxy variable of perceived trust

For guests on Airbnb, their perceived trust typically undergoes three stages of evolution: the first stage is before check in and the perceived trust is mainly dependent on the online snapshot information; the second stage is during the stay and the perceived trust may keep changing according to the experience; and the third stage is after check out and the perceived trust maybe most accurate. As we aim to find antecedents influencing perceived trust, which further decides the purchase intension of guests, it is reasonable to use the perceived trust of the first stage. It has been found that perceived trust is positively related to online purchase intention [44,45]. And consider that a re servation on Airbnb generally means that the guest has made a judgment based on the online snapshot information and chosen to trust the host. What's more, the online snapshot information during a particular short period of time, such as one season, can be taken as unchanged approximately. Therefore, we assume that the perceived trust during the period can be proxied by the growth rate of bookings. Although the other factors like location, accommodations, and price can also influ ence the choice, we contend that trust is the foundation of a reservation and the growth rate of reservations can statistically reflect the perceived trust of hosts to some extent. Additionally, the rationality of the proxy method will be verified through comparing with human labeled data. For simple, we will use “quantified perceived trust” to denote the proxy variable of perceived trust in the following sections.

Unfortunately, the number of bookings on Airbnb is unavailable, and researchers usually use review rate, which ranges from 18.6% [46] to 72%<sup>4</sup>, to convert reviews to estimated bookings. As the number of reviews has been proved to be a proxy for online sales [47], we measured the relative perceived trust with the ratio between the review volume and the online days of the hosts' houses.

For the target listings, the snapshot data collected on June 02, 2017 was selected and the perceived trust (PerceivedTrust) of these listings is measured by the growth rate of reviews during the following three months. Because most hosts only have one house in the filtered data set, it can be assumed that there is a one-to-one correspondence between the listings and the hosts. Considering that guests usually make reservations in advance and the closer the time, the smaller the probability of the calendar being changed, so it is reasonable to calculate the online days of the particular month with the calendar of the prior month. For instance, the calendar file of June was used to calculate the online days of the listings in July. Then, the total online days (OnlineDays) could be aggregated from the calendar files of the three months. Similarly, after a stay, guests can post reviews within a few days. Hence, it is reasonable to calculate the number of reviews in a month from the review snapshot in the following month. For instance, the number of reviews(#Reviews) of listings in July was calculated from the reviews file of August. And then, #Reviews of the three months can be aggregated from the monthly number of reviews in the three months.

As #Reviews is roughly a proxy for the number of bookings, so the booking quantity can be denoted as #Reviews(l )/α, and α is usually set to a constant in [0.18,0.72]. Then, because we mainly care for the relative value of perceived trust and α is a constant, we only calculate the relative perceived trust for each listing l .

$$
\text { PerceivedTrust } (l _ {i}) = \frac {\# \text { Reviews } (l _ {i})}{\text { OnlineDays } (l _ {i})}\tag{1}
$$

## 3.3. Feature engineering

The antecedents influencing perceived trust can be divided into three categories according to the data type, i.e., numeric features, textual features, and image features. The numeric features contain reputation-related features, verification, and response behavior pattern. The textual features are mainly derived from descriptions, such as information amount, readability, sentiment, and semantic topics. The image features refer to the facial emotions within the profile photos.

## 3.3.1. Numerical features

When guests are making a reservation on Airbnb, rating score and number of reviews are often the primary considerations. Generally, the higher the rating score and the number of reviews, the higher the perceived trust. On Airbnb, except for the rating score and reviews, the “superhost” badge is an important component of the established reputation system. The “superhost” badge is assessed quarterly according to the performance over the past 365 days and five requirements shall be satisfied: (1) completed at least 10 orders; (2) maintained a 50% review rate or higher; (3) maintained a 90% response rate or higher; (4) nearly never canceled confirmed orders; (5) received a 5-star review at least 80% of the time. Naturally, the “superhost” badge is a signal of outstanding service quality and could hence help build trust. Additionally, the way hosts respond to guests through instant messaging service can also impact perceived trust. In general, a faster speed of responses can express hosts' enthusiasm. What's more, Airbnb encourages hosts and guests to provide personal verifications such as an email, phone number and Facebook account to prove personal authenticity [33]. For the hosts, providing more verification items can demonstrate their willingness to hold accountable for their actions, which can increase perceived trust [34]. In summary, we propose six numerical features, i.e., rating score, number of reviews, response time, response rate, superhost badge and verifications. The detailed mea surement methods of these features are as follow

The reputation-related features contain rating score, number of reviews and the superhost badge. Rating score is the average review score given by guests. Airbnb enables guests to give ratings on listings from six aspects: accuracy, location, communication, check in, clean liness and value. Here, we won’t distinguish the ratings of the six different aspects but will instead use the overall rating score. Number of reviews is the cumulative number of reviews received by each listing. Finally, for the feature of the superhost badge, the hosts with superhost badge will be labeled as 1, otherwise 0.

The response behavior involves two aspects: the response time and the response rate. Response time represents the waiting time for a guest after he has started a conversation until he receives the first response from the host. The response time is classified into five categories: within an hour, a few hour, hours, a few days, days. The five kinds of response time are labeled as 1, 2, 3, 4, 5 respectively. Response rate refers to the rate of a host responding to his guests. For example, if 100 guests have tried to start a conversation with the host and only 98 guests got responses from the host, then the host's response rate is 98%.

The number of verification items is used to represent the value of verifications. For example, if the verification items of a host are “Email, phone, Facebook, kba and jumio”, then the number of verifications is set to 5.

Table 1  
Topics in self-descriptions.

<table><tr><td>T1 Profession &amp; Personality</td><td>T2 Communication &amp; Service</td><td>T3 Local-expert</td><td>T4 Hobby</td></tr><tr><td>I&#x27;m 0.039work 0.025friendly 0.022easy 0.018going 0.017</td><td>available 0.053phone 0.033questions 0.032text 0.027email 0.025</td><td>Brooklyn 0.018restaurants 0.014New york 0.012Manhattan 0.012neighborhood 0.012</td><td>love 0.046music 0.024art 0.023food 0.022travel 0.011</td></tr><tr><td>clean 0.016apartment 0.013person 0.013busy 0.011</td><td>stay 0.024answer 0.014help 0.013guests 0.011</td><td>apartment 0.012park 0.011great 0.010city 0.008</td><td>design 0.01wine 0.009enjoy 0.009friends0.009</td></tr><tr><td>respectful 0.010</td><td>contact 0.010</td><td>welcome 0.007</td><td>cooking0.008</td></tr><tr><td>quiet 0.009</td><td>meet 0.009</td><td>living 0.007</td><td>fashion0.007</td></tr><tr><td>professional 0.008</td><td>needs 0.007</td><td>guests 0.007</td><td>places0.006</td></tr></table>

## 3.3.2. Textual features

The information amount within descriptions provided on Airbnb, represented by the number of words, can influence perceived trust. Except for the information amount, we believe that other features such as sentiment and semantic topics can also play an important role in trust-building. For instance, well-written descriptions with high readability and quality can provide cues for personal characteristics such as social status and education level. Sentiment in descriptions can reflect hosts' personality traits, such as enthusiasm, to guests. Finally, semantic topics in descriptions can provide more detailed information about the hosts such as their profession, values, and hobbies. This information can help increase the familiarity between hosts and guests and enable guests to make better informed judgments about hosts' trustworthiness. Therefore, we propose four textual features, i.e., information amount, readability, sentiment, and semantic topics.

## (1) Information quality

The amount of information directly determines whether the readers can obtain integrated information. Especially, notional words contribute to a more detailed description of objects [48]. Therefore, we counted the number of notional words, such as nouns, adjectives and verbs, in self-description to represent information amount. In detail, by using Stanford CoreNLP [49], the descriptions are segmented into a list of tokens with parts-of-speech (POS). Then the number of notional words can be counted.

Readability is the ease with which a reader can understand a written text and it involves the language complexity of the text, especially in the dimensions of vocabulary and syntax [50]. Texts with poor readability will bring reading barriers to readers, which means that readers need to spend more time and efort to obtain relevant information. In contrast, texts with higher readability en able readers to understand the information easily and can further help improve perceived trust. Here, the Gunning Fog formula [51] was used to measure text readability. The method assumes that complex words and long sentences are dificult to understand. If a word contains three or more syllables, it will be regarded as a complex word. The greater the Fog index, the more dificult for the text to be understood. The reciprocal value of the Fog index was used to represent readability. Then, the readability of each self-description could be calculated as follows:

$$
R e a d a b i l i t y = \frac {1}{F o g},\tag{2}
$$

$$
F o g = (A S L + P H W) \times 0. 4.
$$

ASL represents the average sentence length, and PHW is the percentage of complex words in a description text.

## (2) Sentiment in descriptions

Self-descriptions expressing hospitality have been found to be highly associated with perceived trust [13]. Here, we think that sentiment in self-descriptions can imply the hospitality and enthusiasm of hosts, which can further influence perceived trust. We propose a method to identify the sentiment intensity of self-descriptions based on the Stanford Tree-bank Sentiment analysis method [49].

The text of each description can be split into sentences by punctuations like period, exclamation, question mark and so on. The sentiment eSens(s) for each sentence s can be classified into five categories by using the Sentiment Tree-bank: very negative, negative, neutral, positive, very positive, and the sentiment intensities are set $\mathsf { t o } - 2 , - 1 , 0 , 1$ 1 and 2 respectively. Then, the total sentiment intensity Sens(d ) of description $d _ { i }$ can be computed as follows:

$$
S e n s (d _ {i}) = \sum_ {s _ {j} \in d _ {i}} e S e n s (s _ {j}).\tag{3}
$$

$s _ { j }$ is the sentence in description $d _ { i }$ and eSens(s ) is the sentiment in tensity of $s _ { j } .$

## (3) Semantic topics in descriptions

According to the uncertainty reduction theory, comprehensive and concrete information provided by hosts can reduce guests' uncertainty regarding to the service ability [52] and trustworthiness. Therefore, besides of the information amount, it is necessary to delve into the influence of semantic topics on perceived trust.

The Latent Dirichlet Allocation (LDA) [53] is applied to extract topics from the descriptions about hosts. If the model is given a set of training documents, it will return two main outputs. The first one is the topic list containing a set of words with diferent weights. The second one is the document list with a vector of topics with weight, which presents the probability of the document containing a specific topic.

Table 1 shows the major topics identified from hosts' self-descrip tions. We got four topics which can cover the meaningful interpretation of the semantic space to some extent by using the Elbow Method [54]. Then, the topics within the self-descriptions were manually summarized as “Profession & Personality”, “Communication & Service”, “Local-expert”, and “Hobby”. As shown in Table 1, “T1 Profession & Personality” represents the occupations and personality of hosts. “T2 Communication & Service” denotes the communication methods ofered by the hosts and what kinds of additional services, e.g. travel advice, will be provided. “T3 Local-expert” highlights the competency of hosts in introducing their hometown, such as restaurants and attractions. “T4 Hobby” represents the individual interests of the hosts. The values corresponding to the words represent the importance of the word in the particular topic (to save space, only 12 words are provided for each topic). In general, T2 and T3 are mainly about the interactions between transaction partners, while T1 and T4 are mainly about self introduction.

## 3.3.3. Image features

A few experiments and surveys have found that facial expression in profile photos of Airbnb hosts can influence perceived trust and purchasing behavior [15,17,55]. A smiling person is generally considered to be more kind, sociable, honest and trustworthy than person without a smile [42]. Here, we suppose that the facial emotion in profile photos can influence perceived trust. In our study, the facial emotion was also detected by using the service provided by Face++.

The image feature of four hosts in Fig. 2 can be obtained by Face+ +. As shown in Table $^ { 2 , }$ the facial expressions in the four photos were identified and the value vector of seven emotions (sad, neutral, disgust, angry, surprise, fear, happy) were also measured. The value of each emotion ranges from 0 to 100 and the larger value suggests the higher

![](/api/attachments/XKSA4RYA/fulltext/images/11d5c7c7c63243f186ec33bef7cb674eb91b4ff36e5efe083f22495efbe3f741.jpg)  
A

![](/api/attachments/XKSA4RYA/fulltext/images/66a5193a671d12e182d3b1e82ba4d73410299a49d474c25641b687222bd81416.jpg)  
B

![](/api/attachments/XKSA4RYA/fulltext/images/9369f294b872db0f8cfabbb6b7caa7397ddeebbcea25da731fa694587ba21dd6.jpg)  
C

![](/api/attachments/XKSA4RYA/fulltext/images/386cc28dfe02fb03b152f50a08ae1d76592969a9fded85043c8154168297e5b7.jpg)  
D  
Fig. 2. The profile photos of four hosts.  
confidence of the status represented by this emotion. In order to find whether the facial emotion polarity can influence perceived trust, the emotion with the maximum value was considered as the key emotion and the emotion polarity can be got accordingly. Then, for positive emotions (happy), the emotion polarity will be set to 1; for neutral emotions (neutral), the emotion polarity will be set to 0; for negative emotions (sad, disgust, angry, fear, surprise), the emotion polarity will be set to −1. As shown in Table 2, the emotion polarities of A and B are 1; the emotion polarity of C is 0; the emotion polarity of D is −1.

## 4. Data analysis and results

After the feature engineering, the antecedents containing 11 variables were obtained from the dataset with 3801 listings and the summary statistics of these variables can be seen in Table 3. In the following section, we will first prove the validity of the proxy method of perceived trust by comparing with human labeled data. Then we will examine how these antecedents corporately influence the perceived trust through the multivariate linear regression by ordinary least squares (OLS). Lastly, four classification models will be built to predict perceived trust.

## 4.1. Human coding of perceived trust

As previously mentioned, we took the growth rate of bookings in a particular period as the proxy of perceived trust. In order to prove that the growth rate can indeed reflect the perceived trust, we turned to human coders to label the perceived trust of hosts and examine whether the growth rate was in agreement with human judgment. A subset of records $( n _ { 1 } = 1 0 0 0 )$ among the 3801 listings were randomly selected. Coders $( n _ { 2 } = 6 )$ were blind to our research intentions. The descriptive information about the coders can be seen in Appendix Table A2. They received the primary information about hosts through a website (see Appendix Fig. A1), which was designed according to the style of Airbnb platform. A six-item perceived trustworthiness scale on three dimensions: ability, benevolence, and integrity[14] was utilized to measure host's trustworthiness(see Appendix Table A1). For each host, six independent coders rated the six-item questionnaire on a seven-point Likert scale (1 = “not at all”, and $7 = ^ { \circ } \mathrm { e x t r e m e l y ^ { \circ } ) }$ and the perceived trust of a coder towards a host was taken as the average score of the six items. Since the perceived trust of each coder may be diferent, we performed z-score standardization on the perceived trust towards all hosts given by each coder. Then, for each host, the average score of the perceived trust given by the six coders was taken as “labeled perceived trust” (diferentiate from “quantified perceived trust”). It should be noted that the Kendall's coeficient of concordance between the labeled perceived trust across the coders was 0.77, which indicates that the labeling is highly reliable. What's more, we also found a significant correlation between a coder's perceived trust and the average perceived trust score the coder assigned to all the hosts $( \mathbf { r } = 0 . 8 8 8 , \ \mathbf { p } < 0 . 0 1 )$ , which further reflects the reliability of the labeling.

Table 3  
Descriptive statistics of the variables.

<table><tr><td>Variables</td><td>Min</td><td>Max</td><td>Mean</td><td>SD</td></tr><tr><td colspan="5">Reputation</td></tr><tr><td>Superhost</td><td>0</td><td>1</td><td>0.175</td><td>0.380</td></tr><tr><td>Rating score</td><td>40</td><td>100</td><td>94.974</td><td>5.738</td></tr><tr><td>Number of reviews</td><td>0</td><td>357</td><td>27.300</td><td>37.093</td></tr><tr><td colspan="5">Verification</td></tr><tr><td>Number of verifications</td><td>1</td><td>12</td><td>4.567</td><td>1.279</td></tr><tr><td colspan="5">Response behavior pattern</td></tr><tr><td>Response time</td><td>1</td><td>4</td><td>1.723</td><td>0.861</td></tr><tr><td>Response rate</td><td>0</td><td>1</td><td>0.942</td><td>0.153</td></tr><tr><td colspan="5">Information quality</td></tr><tr><td>Readability</td><td>0.013</td><td>0.313</td><td>0.065</td><td>0.017</td></tr><tr><td>Information amount</td><td>1</td><td>702</td><td>70.994</td><td>59.624</td></tr><tr><td colspan="5">Sentiment</td></tr><tr><td>Sentiment intensity</td><td>-15</td><td>19</td><td>0.924</td><td>2.317</td></tr><tr><td colspan="5">Semantic topics</td></tr><tr><td>T1 profession &amp; personality</td><td>0.004</td><td>0.667</td><td>0.105</td><td>0.091</td></tr><tr><td>T2 communication &amp; hospitality</td><td>0.003</td><td>0.632</td><td>0.110</td><td>0.097</td></tr><tr><td>T3 local-expert</td><td>0.006</td><td>0.828</td><td>0.086</td><td>0.080</td></tr><tr><td>T4 hobby</td><td>0.005</td><td>0.556</td><td>0.098</td><td>0.084</td></tr><tr><td colspan="5">Facial expression</td></tr><tr><td>Emotion polarity</td><td>-1</td><td>1</td><td>0.527</td><td>0.694</td></tr><tr><td>Perceived trust</td><td>0</td><td>0.95</td><td>0.151</td><td>0.196</td></tr></table>

To prove the validity of the proxy method, we compared the regression analysis results on the dataset with both labeled perceived trust (Table 4, Model 3) and quantified perceived trust (Table 4, Model 2). It is shown that the valence and significance level of the antecedents in Model 2 are consistent with Model 3. On the other hand, for all the hosts, the quantified perceived trust is significantly correlated with the labeled perceived trust $( \mathbf { r } = 0 . 6 3 8 , \mathbf { p } < 0 . 0 1 )$ . These points prove that the growth rate of bookings can indeed well reflect the perceived trust of guests and it is reasonable to take it as the proxy of perceived trust in the context of big data. Because the validity of the proxy method has been proved, we will mainly analyze the regression results on the 3801 listings with the proxy of perceived trust.

Table 2  
Facial expressions detected by Face++.

<table><tr><td>Photo</td><td>Sad</td><td>Neutral</td><td>Disgust</td><td>Angry</td><td>Surprise</td><td>Fear</td><td>Happy</td><td>Key emotion</td><td>Emotion polarity</td></tr><tr><td>A</td><td>0.08</td><td>0.00</td><td>0.17</td><td>0.01</td><td>0.00</td><td>0.01</td><td>99.73</td><td>Happy</td><td>1</td></tr><tr><td>B</td><td>0.07</td><td>0.61</td><td>0.73</td><td>0.07</td><td>0.17</td><td>0.06</td><td>98.30</td><td>Happy</td><td>1</td></tr><tr><td>C</td><td>0.00</td><td>99.84</td><td>0.00</td><td>0.16</td><td>0.00</td><td>0.00</td><td>0.00</td><td>Neutral</td><td>0</td></tr><tr><td>D</td><td>90.34</td><td>9.21</td><td>0.02</td><td>0.01</td><td>0.01</td><td>0.22</td><td>0.20</td><td>Sad</td><td>-1</td></tr></table>

Table 4  
Results of ordinary least squares regression.

<table><tr><td rowspan="3">Variables</td><td colspan="3">Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td rowspan="2">Coefficient (standard error)</td><td colspan="2"> $R^2$  decomposition(%)</td><td rowspan="2">Coefficient (standard error)</td><td rowspan="2">Coefficient (standard error)</td></tr><tr><td>Individual</td><td>Group</td></tr><tr><td>Reputation</td><td></td><td></td><td>71.110</td><td></td><td></td></tr><tr><td>Superhost</td><td>0.073***(0.008)</td><td>9.771</td><td></td><td>0.149***(0.023)</td><td>0.546***(0.050)</td></tr><tr><td>Rating score</td><td>0.021(0.001)</td><td>0.404</td><td></td><td>0.043(0.001)</td><td>0.058(0.003)</td></tr><tr><td>Number of reviews</td><td>0.323***(0.000)</td><td>60.936</td><td></td><td>0.032***(0.000)</td><td>0.432***(0.000)</td></tr><tr><td>Verification</td><td></td><td></td><td>1.577</td><td></td><td></td></tr><tr><td>Number of verifications</td><td>0.052***(0.000)</td><td>1.577</td><td></td><td>0.075***(0.000)</td><td>0.036***(0.000)</td></tr><tr><td>Response behavior pattern</td><td></td><td></td><td>16.404</td><td></td><td></td></tr><tr><td>Response time</td><td>-0.112***(0.004)</td><td>10.639</td><td></td><td>-0.137***(0.010)</td><td>-0.050***(0.023)</td></tr><tr><td>Response rate</td><td>0.040**(0.023)</td><td>5.765</td><td></td><td>0.151***(0.045)</td><td>0.102***(0.101)</td></tr><tr><td>Information quality</td><td></td><td></td><td>0.937</td><td></td><td></td></tr><tr><td>Readability</td><td>0.003(0.178)</td><td>0.100</td><td></td><td>-0.016(0.416)</td><td>0.007(0.930)</td></tr><tr><td>Information amount</td><td>0.013*(0.000)</td><td>0.837</td><td></td><td>0.088***(0.000)</td><td>0.120***(0.008)</td></tr><tr><td>Sentiment</td><td></td><td></td><td>1.340</td><td></td><td></td></tr><tr><td>Sentiment intensity</td><td>0.055***(0.001)</td><td>1.340</td><td></td><td>0.090**(0.004)</td><td>0.041***(0.008)</td></tr><tr><td>Semantic topics</td><td></td><td></td><td>8.605</td><td></td><td></td></tr><tr><td>T1 profession &amp; personality</td><td>-0.038**(0.033)</td><td>1.625</td><td></td><td>-0.042***(0.087)</td><td>-0.027**(0.193)</td></tr><tr><td>T2 communication &amp; service</td><td>0.088***(0.031)</td><td>5.174</td><td></td><td>0.121***(0.086)</td><td>0.025*(0.193)</td></tr><tr><td>T3 local-expert</td><td>0.028*(0.037)</td><td>0.517</td><td></td><td>0.030*(0.098)</td><td>0.028**(0.220)</td></tr><tr><td>T4 hoppy</td><td>-0.030*(0.036)</td><td>1.288</td><td></td><td>-0.077***(0.093)</td><td>-0.018*(0.207)</td></tr><tr><td>Facial expression</td><td></td><td></td><td>0.028</td><td></td><td></td></tr><tr><td>Emotion polarity</td><td>0.010*(0.004)</td><td>0.028</td><td></td><td>0.061**(0.010)</td><td>0.053***(0.023)</td></tr><tr><td>Dependent variables</td><td>Quantified perceived trust</td><td></td><td></td><td>Quantified perceived trust</td><td>Labeled perceived trust</td></tr><tr><td> $R^2$ (Adjusted  $R^2$ )</td><td>0.179(0.176)</td><td></td><td></td><td>0.403(0.395)</td><td>0.838(0.836)</td></tr><tr><td>VIF range</td><td>1.01-1.45</td><td></td><td></td><td>1.03-1.93</td><td>1.03-1.93</td></tr><tr><td>Observations</td><td>3801</td><td></td><td></td><td>1000</td><td>1000</td></tr></table>

\* p < 0.1.  
Notes: Standard coeficients are shown in the table. Standard errors are shown in parentheses.  
\*\* p < 0.05.  
\*\*\* p < 0.01.

## 4.2. Regression analysis

Table 4 reported the OLS regression results. The standard coeficients, significance levels and standard errors were given. Together with the Appendix Table A3, the contribution of each antecedent (Shapley value) or variable (Owen value) represented by the decom position of $R ^ { 2 }$ in the three models were also given. We strove to understand how these antecedents influence perceived trust by (1) investigating the role that reputation plays in determining perceived trust, (2) analyzing the influence of verification and response behavior pattern on perceived trust, (3) comparing the importance of semantic topics in impacting perceived trust, (4) researching the influence of the sentiment related antecedents on perceived trust, and (5) identifying the influence of the information quality on perceived trust.

(1) The role of reputation plays in influencing perceived trust. As shown in Model 1, it can be found that reputation related features play the most important role in influencing perceived trust and the proportion of decomposition of $R ^ { 2 }$ in Model 1 reaches 71%. Overall, the contribution rate of reputation in the three models is in [49%, 78%], which suggests that the reputation mechanism is indeed the basis of trust building. Among the three reputation features, both the number of reviews and the superhost status play an important role. In Model 1, the superhost status is statistically significant (coef. = 0.073, p < 0.01) and the number of reviews is significantly correlated with perceived trust (coef. = 0.323, p < 0.01). The qualification of being a “superhost” reflects higher service quality and ability of being a host and can also help improve perceived trust. The result shows that the guests prefer to trust the hosts who have received more reviews, which is consistent with the social comparison theory [56]. As the theory suggests, because individuals mostly believe that the choices of the majority are right, the popular products/persons usually have a higher probability to be trusted and chosen. However, the rating score is not significantly correlated with the perceived trust (coef. = 0.021, p > 0.1), which is also consistent with previous studies [15]. The failure of the rating mechanism perhaps results from the low degree of diferentiation. As can be seen in Table $^ { 3 , }$ the average rating score reaches 94.974 and the standard deviation is as small as 5.738.

(2) The influence of verification and response behavior pattern on perceived trust. According to the decomposition (16.40%) of $\cdot _ { R ^ { 2 } }$ in Model 1, the response behavior pattern plays the second important role in influencing perceived trust. The response time can significantly decrease perceived trust $( \mathrm { c o e f . } = - 0 . 1 1 2 , \ \mathrm { p } < 0 . 0 1 )$ , and the response rate has a positive impact on perceived trust (coef. = 0.04, p < 0.05). The results indicate that the habit of quick response and keeping high response rate can help improve perceived trust. In general, response to guests is a kind of subjective behavior, and those who provide more friendly and quick responses can show their hospitality and benevolence [30]. The more hospitable the host, the higher the probability for him to be trusted. Also, the number of verifications is positively correlated with perceived trust (coef. = 0.052, p < 0.01). More verifications expose much more personal information and social identify, which can further enhance the feeling of deserving trust.

(3) The importance of diferent semantics topics in afecting perceived trust. According to the decomposition (8.60%) of $R ^ { 2 }$ in Model 1, the semantic topics play the third important role in influencing perceived trust. However, the importance of the four topics is distinct from each other. The “T1 profession & personality” and “T4 hobby” have significant negative influence on perceived trust, while, the “T2 communication & service” and “T3 local-expert” have significant positive impact on perceived trust. Among the four topics, “T2 communication & service” has the most important contribution in building perceived trust. These results suggest that the guests care more about the interaction with the hosts and what kind of service they would be ofered, rather than their occupations or the personal hobbies.

(4) The influence of the sentiment related antecedents on perceived trust. As shown in Model 1, the positive sentiment expressed in self-descriptions (coef. = 0.055, p < 0.01) or facial expressions $( \mathrm { c o e f . } = 0 . 0 1 0 , \ \mathrm { p } < 0 . 1 )$ can help improve perceived trust. This is likely because that the positive emotions of a service provider can arouse emotional contagion between transaction partners [57]. Therefore, the positive sentiment of hosts can afect guests, which in turn positively influence their perceived trust towards host. In re spect to facial expressions, hosts with smiling photos are usually perceived as kind, friendly, honest and polite, which are positively correlated with perceived trust [58].

(5) The influence of information quality on perceived trust. The information amount within self-descriptions can positively influence perceived trust $( \mathrm { c o e f . } = 0 . 0 1 3 , \mathrm { p } < 0 . 1 )$ . Namely, hosts who provide detailed and longer self-description are more likely to receive higher perceived trust by reducing information asymmetry, and the result is consistent with the finding of Ma [14]. However, the readability of the self-description has no significant influence on perceived trust $( \mathrm { c o e f . } = 0 . 0 0 3 , \mathrm { p } > 0 . 1 )$ and the result is not in agreement with Ma [13]. The disparity in results is probably because that the influence of cues on trust formation is relatively dependent on the contextual settings. As Ma et al. [13] limited their research within the linguistic characteristics, which results in the efect of readability on trust formation being exaggerated.

## 4.3. Prediction model

In order to build the predictive model, the hosts need to be divided into two groups. If the quantified perceived trust of a host is higher than the median will be labeled as “high perceived trust”, or the host will be labeled as “low perceived trust”. With the quantified features, a Deep Neural Network based classification model was proposed to predict perceived trust. Then, the prediction performance of the proposed classifier was compared with the other two machine learning methods: Logistic Regression (LR) and Naive Bayesian (NB). Moreover, inspired by the work of [28,59], the three classifiers were also integrated to construct an ensemble classifier (Vote).

A Deep Neural Network (DNN) based classifier is introduced to predict perceived trust. DNN is an artificial neural network (ANN) with multiple hidden layers between the input and output layers [60]. DNNs can model complex linear or non-linear relationships and have dramatically improved the state-of-the-art in various domains. Here, we proposed a five-layer neural network (Fig. 3) to fulfill the classification of perceived trust. For input $I = ( I _ { 1 } , I _ { 2 } , . . . , I _ { m } )$ , m is the dimension of features. For all the three hidden layers, the number of neural units is set to k times of the dimension of the input laver. i.e.. k \* m. And the output layer is denoted by $O = ( O _ { 1 } , O _ { 2 } , . . . , O _ { n } )$ , n is the number of target categories. The ReLU function was selected as the activation function. Then, to avoid over fitting, the dropout rate was set to 0.5, and k was set to 8.

With the aforementioned three classifiers, we also proposed an ensemble classifier (Vote) by using the voting method. The category of a particular host was decided by the average probability predicted by the three classifiers.

The prediction performance of the proposed DNN classifier and the ensemble classifier was compared with the other two classifiers, i.e., LR and NB. Five-fold cross validation was delivered to evaluate the performance of these classifiers. The Precision, Recall, F1-score and AUC were used to evaluate the prediction performance. As shown in Table 5, the proposed DNN classifier outperforms the other two classifiers. In detail, DNN improves the F1-Score by 2.29% and 0.52% than NB and LR respectively. With the index of AUC, DNN outperforms NB and LR by 2.47% and 0.56% respectively. The results indicate that the proposed DNN based classifier is more eficient in predicting perceived trust. In addition, the ensemble classifier Vote outperforms the DNN classifier in precision, recall, and F1-score. Considering the performance of the proposed classifiers, both the DNN classifier and the Vote classifier could be used to predict the perceived trust of hosts.

## 5. Discussion and conclusion

A lot of researchers have focused on the antecedents influencing trust formation, such as profile photos [12,15,17], linguistic features [13,14], reputation [10,29]. However, these antecedents are usually analyzed in isolation by using questionnaires within fabricating settings and the role that diferent antecedents play in trust building within the real world remains unclear. This paper proposed a computational framework for understanding antecedents of perceived trust based on reallife data of Airbnb. To the best of our knowledge, we are the first to investigate the antecedents influencing perceived trust in full spectrum by using computational methods. In detail, we proposed a proxy variable to measure perceived trust and the method was proved to be rational by using human labeled data. Additionally, the antecedents influencing perceived trust were extracted from diferent types of data automatically by using text mining and facial recognition methods. A series of regression analysis were performed to examine the relationship between the antecedents and perceived trust. In addition, the contributions of diferent antecedents in building trust were also analyzed and compared. A few interesting findings were obtained, which can advance the understanding of the working of these antecedents. At last, predictive models were designed and the evaluation results suggested their potential for practical application.

## 5.1. Research findings

We limited our research in the antecedents within the controllable or manageable information about the hosts on Airbnb. This means that the controllable or manageable information may be changed, for ex ample, the self-description could be rewritten, the profile photos could be replaced, and the response behavior patterns could also be altered. In contrast, the attributes of hosts such as gender, race, and age are generally dificult or impossible to be changed at will. Thus, we contend that researching the antecedents within the manageable information is more valuable. Subsequently, by comprehensively analyzing the influence of these antecedents, we obtained several interesting findings.

Among all the antecedents, reputation plays the most important role in afecting trust building and the contribution of reputation is not less than the contribution of the rest antecedents. Although a lot of research has been devoted to investigating the working of reputation [15,28], we are the first to reveal the importance of reputation among the proposed antecedents on Airbnb through quantitative analysis. We found that comparing with traditional e-commerce, the importance of reputation has been weakened and the other antecedents about hosts play a role of equal importance in trust building of sharing economy. The finding suggests that trust in the sharing economy extends far beyond reputation. Among the reputation related antecedents, the superhost badge and the number of reviews can generate significant and positive influence on perceived trust, which is consistent with the finding of [10,38]. While the ratings system is failed in helping build trust for its poor discrimination. The finding supports the work of [27]. Besides, the response behavior pattern plays the second important role in influencing perceived trust. Improving the response rate and decreasing the response time can help enhance perceived trust, and the finding is agreement with [30].

![](/api/attachments/XKSA4RYA/fulltext/images/bf2615587955d87b8ab4482465461196468358f0076aff161de846a430cebda5.jpg)  
Fig. 3. Architecture of deep neural network.

Table 5  
Prediction performance (%) of the proposed classifiers.

<table><tr><td>Classifier</td><td>NB</td><td>LR</td><td>DNN</td><td>Vote</td></tr><tr><td>Precision (%)</td><td>69.05</td><td>71.62</td><td>72.21</td><td>72.32</td></tr><tr><td>Recall (%)</td><td>68.99</td><td>70.96</td><td>71.48</td><td>71.56</td></tr><tr><td>F1-Score (%)</td><td>68.96</td><td>70.73</td><td>71.25</td><td>71.56</td></tr><tr><td>AUC (%)</td><td>74.16</td><td>76.07</td><td>76.63</td><td>74.04</td></tr></table>

In terms of antecedents within self-descriptions, semantic topics are the third important in influencing perceived trust. The existing studies [14] often identify semantic topics manually and the number of topics is usually arbitrarily selected, which cannot guarantee the comprehensiveness and accuracy of topics. In contrast, we identify topics au tomatically by using LDA and make quantitative analysis on the importance of semantic topics. We are the first to find that the hosts who organize their self-description by concentrating on interactions, services, and the familiarity with nearby places rather than profession, personality, and hobbies, tend to be perceived as more trustworthy. Besides, consistent with the finding of Ma et al. [14], the information amount is helpful to perceived trust. But we find that the readability of self-descriptions is not significantly correlated with perceived trust, which is usually helpful in traditional e-commerce. In respect to the sentiment in self-descriptions, we are the first to reveal that positive sentiment can help building trust by using sentiment analysis method. At last, we also reveal that positive facial expression in profile photos can significantly influence perceived trust, which is consistent with the findings of [15,17]. The number of verifications, which has not been researched on Airbnb, is also significantly related to perceived trust.

## 5.2. Theoretical and practical contributions

The study makes both theoretical and practical contributions. From the theoretical perspective, the computational framework for under standing antecedents of perceived trust provides a holistic view of factors determining the formation of perceived trust and introduces computational methods to measure the perceived trust and the ante. cedents. To the best of our knowledge, it is the first time that a com prehensive model is proposed to analyze the factors within the man ageable information about hosts that contribute to the development of consumers' trust in the sharing economy. Thus, our study provides perhaps the most comprehensive understanding of the trust-related antecedents that consumers consider as they engage in online transactions. Furthermore, the importance of diferent mechanisms was also compared, which is relevant for academics and researchers engaged in the study of online trust. Understanding the antecedents of trust in online sharing transactions could also inform research interests in online trust within various kinds of sharing services. What's more, the proxy variable of perceived trust based on the trusting behavior is applicable to other similar situations in online sharing economy, which can help decrease the labor costs on surveys or human labeling. The introduced methods of text mining and face recognition can also be used to extract and quantify features from other textual and image data.

From the practical standpoint, the results highlight several antecedents influencing perceived trust that may guide the successful completion of sharing transactions in online environments. The findings of this paper will be useful not only for customers involved in online sharing transaction, but also for people engaged in the implementation, design and management of infrastructures for online services in the sharing economy.

As the hosts have the duty of not only creating trust but also maintaining it and this process involves presenting themselves as trustworthy person [18], we assert that the transaction partners shall consciously make presentation management and the findings of the paper can help service providers manage their self-description and serving behavior more eficiently. In particular, it is important to maintain a good reputation by accumulating reviews and striving for the superhost badge. If the two conditions are fulfilled, you are already half-way to success. Then, more attention should be placed on the response behavior pattern. Keeping a higher response rate and quicker response can help reflect hospitality and service ability and further improve the perceived trust. Thirdly, it is interesting that consumers engaged in online sharing transactions would like to find more information about the interactions with the service provider, such as communication, services, and introduction about the residence place. In contrast, too much description of personality, profession, and personal interests are not welcome. Fourthly, positive words in self-descriptions and positive facial expression in profile photos can also be beneficial. At last, it is advisable to provide as much verifications as possible and avoid skimping on words when making descriptions. In general, our findings can help hosts manage their self-representation better. For the people engaged in the implementation, design and management of infrastructures for online services, the influence of the antecedents on perceived trust can shed light on the mechanism of the trust formation in online sharing economy, and the prediction model can also be helpful in designing a trust-based recommendation service.

## 5.3. Limitations and directions for future research

There are several limitations to this research, which can be overcome in future work. Firstly, perceived trust is measured based on the renting behavior in New York during the period of three months. If the data of other cities in USA or in other counties can also be investigated, the findings of the research would be more accurate and convincing. Secondly, besides of the accommodation sharing services, the antecedents influencing trust building in other kinds of sharing services, such as skills sharing, also need to be researched. In the future, a sentiment analysis method for distinguishing the subtle diference between the positive reviews should be developed. The antecedents influencing the dynamic evolution of perceived trust on Airbnb from a long-term perspective also provide an interesting direction for future studies.

## Appendix A

## Acknowledgments

This work was supported by a grant from the National Social Science Foundation of China [No. 17AGL026].

![](/api/attachments/XKSA4RYA/fulltext/images/55427d9206bcef4a5c0c883fbdf0cf9068cf0ed41465a8092d2f41ffb1a96155.jpg)

<table><tr><td colspan="2">Verifications</td></tr><tr><td>email</td><td>√</td></tr><tr><td>phone</td><td>√</td></tr><tr><td>reviews</td><td>√</td></tr><tr><td>kba</td><td>√</td></tr><tr><td>work_email</td><td>√</td></tr></table>

I'm a full time musician, part time Real estate mogul! :) I love to travel and have friends in all parts of the world. One of the customs I picked up in my travels, and which I exercise in my home now, is the practice of removing outdoor shoes after I enter my Apt. (thanks to the Danes and Japanese!)

\* Superhost: No

\* Response time: within a day

\* Response rate: 80%

\* Number of reviews: 64

\* Review scores rating: 92

```txt
Please make ratings about the trustworthiness of the host. (1-not at all to 7-extremely)

This person is capable of paying his/her own rent mortgage.

○ 1 ○ 2 ○ 3 ○ 4 ○ 5 ○ 6 ○ 7

This person maintains a clean, safe, and comfortable household.

○ 1 ○ 2 ○ 3 ○ 4 ○ 5 ○ 6 ○ 7

This person will be concerned about satisfying my needs during the day.

○ 1 ○ 2 ○ 3 ○ 4 ○ 5 ○ 6 ○ 7

This person will go out of his/her way to help me in case of an emergency during my stay.

○ 1 ○ 2 ○ 3 ○ 4 ○ 5 ○ 6 ○ 7

This person will stick to his/her word, and be there when I arrive instead of standing me up.

○ 1 ○ 2 ○ 3 ○ 4 ○ 5 ○ 6 ○ 7

This person will not intentionally harm, overcharge, or scam me.

○ 1 ○ 2 ○ 3 ○ 4 ○ 5 ○ 6 ○ 7
```  
Fig. A1. The demo of the questionnaire website.

Table A1 The six-item perceived trustworthiness scale.

<table><tr><td>Dimensions</td><td>Items</td></tr><tr><td>Ability</td><td>This person is capable of paying his/her own rent or mortgage.</td></tr><tr><td>Ability</td><td>This person maintains a clean, safe, and comfortable household.</td></tr><tr><td>Benevolence</td><td>This person will be concerned about satisfying my needs during the stay.</td></tr><tr><td>Benevolence</td><td>This person will go out of his/her way to help me in case of an emergency during my stay.</td></tr><tr><td>Integrity</td><td>This person will stick to his/her word, and be there when I arrive instead of standing me up.</td></tr><tr><td>Integrity</td><td>This person will not intentionally harm, overcharge, or scam me.</td></tr></table>

Table A2  
Coders descriptive statistics.

<table><tr><td>Dimensions</td><td>Number</td><td>Mean</td><td>SD</td></tr><tr><td>Sex</td><td></td><td></td><td></td></tr><tr><td>Male</td><td>3</td><td></td><td></td></tr><tr><td>Female</td><td>3</td><td></td><td></td></tr><tr><td>Age</td><td>6</td><td>24</td><td>3.521</td></tr><tr><td>Education</td><td></td><td></td><td></td></tr><tr><td>Undergraduate</td><td>2 (one male and one female)</td><td></td><td></td></tr><tr><td>Postgraduate</td><td>2 (one male and one female)</td><td></td><td></td></tr><tr><td>PhD student</td><td>2 (one male and one female)</td><td></td><td></td></tr><tr><td colspan="4">Disposition to trust (seven-point Likert-type scale)</td></tr><tr><td>Most people are reliable</td><td>6</td><td>5</td><td>0.894</td></tr><tr><td>Most people are honest</td><td>6</td><td>5</td><td>0.894</td></tr><tr><td>Most people are of good faith</td><td>6</td><td>4.833</td><td>0.753</td></tr></table>

## Table A3

Results of the $R ^ { 2 }$ decomposition of Model 2 and Model 3.

<table><tr><td rowspan="3">Variables</td><td colspan="2">Model 2</td><td colspan="2">Model 3</td></tr><tr><td colspan="2"> $R^2$  decomposition(%)</td><td colspan="2"> $R^2$  decomposition(%)</td></tr><tr><td>Individual</td><td>Group</td><td>Individual</td><td>Group</td></tr><tr><td>Reputation</td><td></td><td>49.496</td><td></td><td>78.779</td></tr><tr><td>Superhost</td><td>13.553</td><td></td><td>45.524</td><td></td></tr><tr><td>Rating score</td><td>1.040</td><td></td><td>0.802</td><td></td></tr><tr><td>Number of reviews</td><td>34.903</td><td></td><td>32.453</td><td></td></tr><tr><td>Verification</td><td></td><td>2.195</td><td></td><td>0.484</td></tr><tr><td>Number of verifications</td><td>2.195</td><td></td><td>0.484</td><td></td></tr><tr><td>Response behavior pattern</td><td></td><td>26.678</td><td></td><td>8.502</td></tr><tr><td>Response time</td><td>11.458</td><td></td><td>2.870</td><td></td></tr><tr><td>Response rate</td><td>15.221</td><td></td><td>5.632</td><td></td></tr><tr><td>Information quality</td><td></td><td>7.808</td><td></td><td>8.877</td></tr><tr><td>Readability</td><td>0.097</td><td></td><td>0.167</td><td></td></tr><tr><td>Information amount</td><td>7.711</td><td></td><td>8.710</td><td></td></tr><tr><td>Sentiment</td><td></td><td>2.185</td><td></td><td>0.849</td></tr><tr><td>Sentiment intensity</td><td>2.185</td><td></td><td>0.849</td><td></td></tr><tr><td>Semantic topics</td><td></td><td>10.975</td><td></td><td>2.171</td></tr><tr><td>T1 profession &amp; personality</td><td>1.461</td><td></td><td>0.797</td><td></td></tr><tr><td>T2 communication &amp; service</td><td>5.773</td><td></td><td>0.432</td><td></td></tr><tr><td>T3 local-expert</td><td>0.588</td><td></td><td>0.462</td><td></td></tr><tr><td>T4 hobby</td><td>3.198</td><td></td><td>0.479</td><td></td></tr><tr><td>Facial expression</td><td></td><td>0.664</td><td></td><td>0.337</td></tr><tr><td>Emotion polarity</td><td>0.664</td><td></td><td>0.337</td><td></td></tr><tr><td>Overall  $R^2$ </td><td>0.403</td><td></td><td>0.838</td><td></td></tr><tr><td>Observations</td><td>1000</td><td></td><td>1000</td><td></td></tr></table>

## References

[1] D. Guttentag, Airbnb: disruptive innovation and the rise of an informal tourism accommodation sector. Current Issues in Tourism 18 (12) (2015) 1192–1217.

[2] M. Huurne, A. Ronteltap, R. Corten, V. Buskens, Antecedents of trust in the sharing economy: a systematic review, Journal of Consumer Behaviour 16 (6) (2017) 485-498.

[3] T.A. Weber, Intermediation in a sharing economy: insurance, moral hazard, and rent extraction. Journal of Management Information Systems 31 (3) (2014) 35–71

[4] D.H. McKnight, N.L. Chervany, What trust means in e-commerce customer relationships: an interdisciplinary conceptual typology, International Journal of Electronic Commerce 6 (2) (2001) 35–59

[5] R.C. Mayer, J.H. Davis, F.D. Schoorman, R.C. Mayer, J.H. Davis, An integrative model of organizational trust. Academy of Management Review 20 (3) (1995) 709–734.

[6] P. Sztompka, Trust: A Sociological Theory, Cambridge University Press, 1999.

[7] D.M. Rousseau, S.B. Sitkin, R.S. Burt, C. Camerer, Not so different after all: a cross discipline view of trust. Academy of Management Review 23 (3) (1998) 393–404.

[8] W.B. Pearce, Trust in interpersonal communication, Speech Monographs 41 (3) (1974) 236–244.

[9] B.A. Sparks, V. Browning, The impact of online reviews on hotel booking intentions and perception of trust, Tourism Management 32 (6) (2011) 1310–1323.

[10] S. Liang, M. Schuckert, R. Law, C.C. Chen, Be a “superhost”: the importance of badge systems for peer-to-peer rental accommodations, Tourism Management 60 (2017) 454–465.

[11] J. Bridges, C. Vásquez, If nearly all airbnb reviews are positive, does that make them meaningless? Current Issues in Tourism (2016) 1-19

[12] F. Hawlitschek. T. Teubner, M.T.P. Adam, N.S. Borchers, M. Mohlmann. C. Weinhardt, Trust in the sharing economy: an experimental framework, ICIS 2016 Proceedings, 2016, pp. 1–14.

[13] X. Ma, T. Neeraj, M. Naaman, A computational approach to perceived trustworthiness of airbnb host profiles, ICWSM, 2017, pp. 604–607

[14] X. Ma, J.T. Hancock, K. Lim Mingjie, M. Naaman, Self-disclosure and perceived trustworthiness of airbnb host profiles, Proceedings of the 2017 ACM Conference on Computer Supported Cooperative Work and Social Computing, CSCW ’17, ACM, New York, NY, USA, 2017, pp. 2397–2409.

[15] E. Ert, A. Fleischer, N. Magen, Trust and reputation in the sharing economy: the role of personal photos in airbnb, Tourism Management 55 (Supplement C) (2016) 62-73.

[16] G. Bente, O. Baptist, H. Leuschner, To buy or not to buy: influence of seller photos and reputation on buyer trust and purchase behavior, International Journal of Human-Computer Studies 70 (1) (2012) 1–13

[17] A. Fagerstrøm, S. Pawar, V. Sigurdsson, G.R. Foxall, M.Y. de Soriano, That personal profile image might jeopardize your rental opportunity! On the relative impact of the seller's facial expressions upon buying behavior on airbnb, Computers in Human Behavior 72 (Supplement C) (2017) 123–131.

[18] D.F. Haas, F.A. Deseran, Trust and symbolic exchange, Social Psychology Quarterly 44 (1) (1981) 3–13

[19] E. Gofman, The presentation of self in everyday life, American Journal of Sociology 55 (1949) 6–7.

[20] A.C. Costa. C.A. Fulmer, N.R. Anderson, Trust in work teams: an integrative review. multilevel model, and future directions, Journal of Organizational Behavior 39 (2) (2017) 169–184.

[21] T.H. Chiles, J.F. McMackin, Integrating variable risk preferences, trust, and transaction cost economics. The Academy of Management Review 21 (1) (1996) 73–99

[22] S. Grabner-Kräuter, E.A. Kaluscha, Empirical research in on-line trust: a review and critical assessment, International Journal of Human Computer Studies 58 (6) (2003) 783–812.

[23] R. Botsman, R. Rogers, What's Mine is Yours: The Rise of Collaborative Consumption, Harper Business, 2010.

[24] A. Wilson, V.A. Zeithaml, M.J. Bitner, D.D. Gremler, Services Marketing: Integrating Customer Focus Across the Firm, McGraw Hill, 2012.

[25] C.S. Liu, A couchsurfing ethnography: traveling and connection in a commodified world, Inquiries Journal 4 (07) (2012) 1–3.

[26] A. Beldad, M. de Jong, M. Steehouder, How shall I trust the faceless and the intangible? A literature review on the antecedents of online trust, advancing Educational Research on Computer-supported Collaborative Learning (CSCL) through the use of gStudy CSCL Tools, Computers in Human Behavior 26 (5) (2010 857–869.

[27] G. Zervas, D. Proserpio, J. Byers, A First Look at Online Reputation on Airbnb Where Every Stay is Above Average, available at SSRN: https://ssrn.com/abstract= 2554500 (accessed 28 January 2015) (2015), pp. 1–22.

[28] S. Banerjee, S. Bhattacharyya, I. Bose, Whose online reviews to trust? Understanding reviewer trustworthiness and its impact on business. Decisior Support Systems 96 (2017) 17–26.

[29] T. Teubner, N. Saade, F. Kawlitschek, C. Weinhardt, It's only pixels, badges, and stars: on the economic value of reputation on airbnb, Proceedings of the Australasian Conference on Information Systems, 2016, pp. 1–11.

[30] J. Wu, P. Ma, K. Xie, In sharing economy we trust: the efects of host attributes on short-term rental purchases, International Journal of Contemporary Hospitality Management 29 (11) (2017) 2962–2976.

[31] S. Utz, U. Matzat, C. Snijders, On-line reputation systems: the efects of feedback comments and reactions on building and rebuilding trust in on-line auctions, International Journal of Electronic Commerce 13 (3) (2009) 95–118.

[32] S. Malinen, J. Ojala, Perceptions of trust between online auction consumers, International Journal of Web Portals 3 (4) (2011) 15–26

[33] K. Minghui, G. Yiwen, W. Tao, Z. Haichao, Understanding the determinants of funders' investment intentions on crowdfunding platforms: a trust-based perspec tive, Industrial Management and Data Systems 116 (8) (2016) 1800–1819.

[34] G. Norcie, E. De Cristofaro, V. Bellotti, Bootstrapping trust in online dating: social verification of online dating profiles, Financial Cryptography and Data Security: FC 2013 Workshops, USEC and WAHC 2013, Okinawa, Japan, Springer, Berlin, Heidelberg, 2013, pp. 149–163

[35] C. Dongyu, L. Hao, C. Van Slyke, Toward an understanding of online lending intentions: evidence from a survey in China. Communications of the Association for Information Systems 36 (2015) 317–336

[36] I. Alfina, J. Ero, A.N. Hidayanto, M.R. Shihab, The impact of cognitive trust and e wom on purchase intention in c2c e-commerce site, Journal of Computer Science 10 (12) (2014).2518–2524

[37] Y. Liu, L. Nie, L. Li, Homogeneity, trust, and reciprocity: three keys to the sustainable hospitality exchange of couchsurfing, Tourism Analysis 21 (2-3) (2016) 145–157.

[38] N. Yacouel, A. Fleischer, The role of cybermediaries in reputation building and price premiums in the online hotel market, Journal of Travel Research 51 (2) (2012) 219–226.

[39] X. Chen, O. Huang, R.M. Davison, Z. Hua, What drives trust transfer? The moderating roles of seller-specific and general institutional mechanisms. International Journal of Electronic Commerce 20 (2) (2015) 261–289

[40] C. Liao, P. Palvia, H.-N. Lin, The roles of habit and web site quality in e-commerce, International Journal of Information Management 26 (6) (2006) 469–483.

[41] X. Chen, Q. Huang, R. Davison, Z. Hua, The moderating efects of contextual factors on a buver's trust in e-commerce platforms and sellers. Pacific Asia Conference or Information Systems, 2014, pp. 1–18.

[42] D. Bugental, Unmasking the polite smile: situational and personal determinants of managed afect in adult-child interaction, Personality and Social Psychology Bulletin 12 (1) (1986) 7–16.

[43] J.-Y. Baudouin, D. Gilibert, S. Sansone, G. Tiberghien, When the smile is a cue to familiarity, Memory 8 (5) (2000) 285–292.

[44] K.-C. Chang, N.-T. Kuo, C.-L. Hsu, Y.-S. Cheng, The impact of website quality and perceived trust on customer purchase intention in the hotel sector: website brand and perceived value as moderators, International Journal of Innovation Management and Technology 5 (4) (2014) 255–260

[45] K.C. Ling, D. bin Daud, T.H. Piew, K.H. Keoy, P. Hassan, Perceived risk, perceived technology, online trust for the online purchase intention in Malaysia, International Journal of Business and Management 6 (6) (2011) 167–182.

[46] Q. Ke, Sharing means renting?: an entire-marketplace analysis of airbnb, Proceedings of the 2017 ACM on Web Science Conference Websci '17 ACM New York, NY, USA, 2017, pp. 131–139.

[47] Q. Ye, R. Law, B. Gu, The impact of online user reviews on hotel room sales, International Journal of Hospitality Management 28 (1) (2009) 180–182.

[48] L. Larrimore, L. Jiang, J. Larrimore, D. Markowitz, S. Gorski, Peer to peer lending: the relationship between language features, trustworthiness, and persuasion success, Journal of Applied Communication Research 39 (1) (2011) 19–37

[49] R. Socher, A. Perelygin, J. Wu, J. Chuang, C.D. Manning, A. Ng, C. Potts, Recursive

deep models for semantic compositionality over a sentiment treebank, Proceeding of the 2013 conference on empirical methods in natural language processing, 2013, pp. 1631–1642.

[50] N. Hu, I. Bose, N.S. Koh, L. Liu, Manipulation of online reviews: an analysis of ratings, readability, and sentiments, Decision Support Systems 52 (3) (2012) 674–684.

[51] F. Li, Annual report readability, current earnings, and earnings persistence, Journa of Accounting and Economics 45 (2) (2008) 221–247.

[52] I. Tussyadiah, Strategic self-presentation in the sharing economy: implications for host branding, in: A. Inversini, R. Schegg (Eds.), Information and Communication Technologies in Tourism 2016, Springer International Publishing, Cham, 2016, pp. 695–708.

[53] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, Journal of Machine Learning Research 3 (2003) 993–1022.

[54] D.J. Ketchen, C.L. Shook, The application of cluster analysis in strategic management research: an analysis and critique, Strategic Management Journal 17 (6) (1996) 441–458.

[55] G. Bente, T. Dratsch, K. Kaspar, T. Häßler, O. Bungard, A. Al-Issa, Cultures of trust: efects of avatar faces and reputation scores on German and Arab players in an online trust-game, PLoS ONE 9 (6) (2014) 1–7

[56] L. Festinger, A theory of social comparison processes, Human Relations 7 (2) (1954) 117–140.

[57] G. Schoenewolf, Emotional Contagion: Behavioral Induction in Individuals and Groups, 15 (1990), pp. 49–61

[58] K. Brian, Facial Expressions of Emotion Influence Interpersonal Trait Inferences, 20 (1996), pp. 165–182

[59] Z. Liu. B.J. Jansen. Identifving and predicting the desire to help in social questior and answering, Information Processing & Management 53 (2) (2017) 490–504

[60] Y. Bengio, Learning deep architectures for ai, Foundations and Trends in Machine Learning 2 (1) (2009) 1–127.

![](/api/attachments/XKSA4RYA/fulltext/images/96c05e88339ba8f9b3e34ad846c86075cdfc7faa41b577278fe7b22c15c7b6e0.jpg)  
Le Zhang is a Ph.D. candidate in the School of Economics and Management, Beijing University of Posts and Telecommunications, Beijing, China. Her research interests include trust in the sharing economy, social computing, natural language processing.

![](/api/attachments/XKSA4RYA/fulltext/images/a03c97201cf59bb6a66a48dbdd0800221cb4f7fd82745f350411522351ac45b0.jpg)

Qiang Yan is a professor in the School of Economics and Management at Beijing University of Posts and Telecommunications. His researches focus on E-commerce and information systems. He has published more than 90 papers in peer-reviewed journals.

![](/api/attachments/XKSA4RYA/fulltext/images/0a7f22648ac7dc9a9a2e626e16e574883f05436ad48707fd2c8db3cdf28dc216.jpg)

Leihan Zhang is a research associate in the Institute of Computer Science and Technology. Peking University Beijing, China. His research interests include data mining, complex network, and natural language processing.
