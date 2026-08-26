---
otero_id: 20537
otero_key: "KZB8MV3Y"
title: "Effect of writing style on social support in online health communities: A theoretical linguistic analysis framework"
authors: "Shan Jiang; Xuan Liu; Xiaotong Chi"
year: "2022"
journal: "Information & Management"
doi: "10.1016/j.im.2022.103683"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Effect of writing style on social support in online health communities: A theoretical linguistic analysis framework

![](/api/attachments/KZB8MV3Y/fulltext/images/f237bd7465102486c759fb607d8f84b34e7ab35d7395a03a47b35dfb489bd9d1.jpg)

Shan Jiang <sup>a</sup>, Xuan Liu <sup>b,\*</sup>, Xiaotong Chi <sup>b</sup>

<sup>a</sup> College of Management, Univ. of Massachusetts Boston, 100 Morrisey Blvd., Boston, MA, 02125

<sup>b</sup> School of Business, East China University of Science and Technology, 130 Meilong Rd., Shanghai 200237, China

## A R T I C L E I N F O

Keywords: Online health communities Social support Linguistic analysis Exponential random graph models

## A B S T R A C T

In online health communities (OHCs), patients can exchange social support through text-based communication. However, research on how various linguistic characteristics of patients’ communication in these communities affect their social support outcomes remains limited. This study performs linguistic profiling on OHC participants based on a large dataset and empirically evaluates how lexical, syntactic, semantic, and pragmatic features affect users’ communication and social support outcomes. The results show that lexical richness in health-related vocabulary negatively correlates with receiving informational support. The readability and brevity of written texts have positive relationships with incoming social support. Writing longer sentences positively correlates with receiving informational support but negatively correlates with receiving emotional support. Expressing negative sentiment leads to higher chances of receiving both types of social support. The use of terms related to perception and body parts increases the chances of receiving emotional support. The use of terms related to perception words additionally correlates to higher chances of receiving informational support. To receive socia supports, being logical in expressions is also critical. Furthermore, the relationships between shared health language and social support are determined by the word category and social support type.

## 1. Introduction

In the past decade, online health communities (OHCs) have become a popular source for patients to communicate with peers and seek social support [58,60]. These communities provide patients and caregivers with new resources, such as information, solidarity, and social support [24,26]. With the increasing popularity of OHCs, patients can receive various health care benefits online that complement what they receive from offline contacts. With asynchronous communication, participants in OHCs can post and reply at times most convenient to them and without geographic and transportation barriers [74]. Additionally, the anonymity provided by OHCs allows discussion of potentially embar rassing topics, which increases the possibility of self-disclosure and en courages honesty and intimacy [73,81]. Maintaining the healthy growth of OHCs and improving patients’ well-being have become important tasks for policymakers and health practitioners.

Abundant OHC research has shown that the community structure and structural capital developed between OHC participants are key antecedents of effective social support [9,29,30,34,85]. Recently, research has also suggested that linguistic signals embedded in the texts used for communication could affect patients’ social support outcomes [1,10,13,18,35,64]. The impact of language use in OHCs differs considerably from other contexts because a unique aspect of OHCs is that most patients use plain language to describe complicated disease symptoms and treatments [75]. The discrepancy between the plain health care language (i.e., what patients actually used) and professional medical terms (i.e., what patients try to phrase) could change the ways in which linguistic features affect the outcomes of communication. For example, the brevity of messages is a crucial characteristic of leaders in online communities [35], but patients may sacrifice succinctness by using more body- and feeling-related words to offer a more accurate description of disease symptoms. In addition to the stylistic features, the meanings of words and the context of communication could also affect how online language affects social support outcomes. Being pessimistic and frequently expressing negative feelings could make others uncom fortable in many social groups [66]. Still, OHC participants may instead provide encouragement and other support to peers suffering from a disease. A study has shown that support seekers with high levels of emotional disclosures would enhance the viewer's intention to provide support [41]. Therefore, examining how various linguistic features affect OHC participants’ communication and social support outcomes could provide insights into these unique aspects of OHCs. However, among various linguistic features, less attention has been given to se mantic and pragmatic features of texts. Moreover, previous studies have mostly analyzed the linguistic characteristics of message postings. A user-level linguistic analysis would complement the existing literature by providing additional insights into how patients should adjust their overall writing strategies to receive enhanced social support from the entire community.

This study examines the influence of various user-level linguistic features of OHC participants on their communication and social support outcomes. From a patient-centered perspective, selected lexical, syn tactic, semantic, and pragmatic features specific to the health care context are extracted from the messages posted by OHC participants. We then explore the relationships between these user-level linguistic fea tures and possible outcomes, including receiving message replies, developing reciprocal conversation, receiving helpful information, and obtaining emotional support. Finally, exponential random graph models (ERGMs) are used to model the interdependencies of these relationships and understand how these factors facilitate the development of communication and social support networks in OHCs.

## 1.1. Related work

## 1.1.1. Communication, interaction, and social support in OHCs

In many OHCs, interactions between participants are initiated by starting a thread or sending the first private message. Peers who are interested in the message content will reply to the message. Notably, prior literature has suggested that most interactions in OHCs end at this stage [29]. This finding implies that most OHC participants read through replies to see whether any reply content is relevant to their concerns. Still, it is expensive to maintain relationships with all repliers by furthe replying to them [86]. According to social exchange theory, individuals engage in social interactions with the expectation of social rewards [5]. Thus, reciprocated conversations would be more likely to occur when message recipients see value in the reply content. Mutual relationships are maintained in the long term if both parties keep providing values in their conversation

However, simple message exchanges may be the weakest type of social support [39]. Although receiving replies and finding peers to reciprocate messages from time to time may be comforting to some OHC participants, the more valuable assets an OHC offers its members come from social support, such as helpful information and emotional relief [4, 40,69,78,85]. According to [39], social support is the "aid and assistance exchanged through social relationships and interpersonal transactions." In recent years, research on social support in OHCs has grown signifi cantly. The primary research focuses have been (1) understanding various benefits of social support and (2) identifying antecedents (or facilitators) of social support in OHCs

Social support is vital in helping individuals improve their health status [35,37,72]. Unlike traditional offline settings where social sup port typically comes from family members and friends, patients can now receive social support from online strangers with whom they have never talked before. These strangers voluntarily provide help and support to each other and contribute to the growth and prosperity of OHCs [29]. Among various types of social support, informational and emotional support have been the most common forms [9,27,56,62,85]. An OHC participant typically seeks informational support by creating a thread/post and asking questions about a disease, its treatments, and potential side effects from peers [12,58, 79]. Peers who can answer the questions provide the required information by replying to the post. Emotional support includes care, sympathy, concern, and encourage ment [65]. It typically comes from other participants who share similar experiences of the disease. Patients can obtain understanding, relief, and psychological well-being from emotional support [45,63,85]. In the long term, emotional support could be the most needed support for patients with chronic diseases such as diabetes [38,51] and cancer [17].

Extant research has explored various antecedents of this social sup port. In this research stream, much focus has been on understanding the influence of community structure on the exchange of social support. By communicating and friending with each other, participants develop a social network in OHCs [30,34]. The network typically presents a core-periphery structure where the core consists of members who are tightly bonded by reciprocated communication, while the periphery consists of other members of the community who have weaker con nections to the core [30]. Within such a network structure, consistent findings have found that an individual’s position within the network can critically affect the effectiveness of social support exchange $[ 3 , 9 , 2 9 , 3 0 ]$ For instance, members belonging to the core tend to provide the most informational support to the entire OHC [30]. Some scholars have also examined the effect of betweenness centrality [21], which is a measure that reflects the influence a node has on the spread of information through the network. It has been found that a patient’s betweenness centrality is positively associated with the amount of social support exchange [9].

## 1.1.2. Language use and outcomes in online communities

Numerous studies have found an association between language usage and outcomes in online communities. For example, leaders in online communities were found to post more concise messages with simple language familiar to other participants [35]. Sentiments expressed in text and the complexity of sentences were found to be effective in detecting fraud on crowdfunding platforms [64]. In the online review context, the usage of negative emotion words has influ enced the perceived helpfulness of reviews [18].

Regarding OHCs, however, research on the use of language and its effects on social support acquisition is still limited. A recent study found that general language use, represented mainly by lexical and syntactic features of writing (e.g., readability, spelling, message lengths), was positively associated with social support [10]. While providing valuable insights for general language usage of online community members and the social support received, existing research has yet to address the importance of other unique linguistic features specific to OHCs, such as the usage of health-related terms. Specifically, OHCs are platforms where patients can exchange information on diseases, symptoms, and treatments. Thus, OHC participants must use many health-related terms, such as names of diseases and medicines. Many patients also prefer using fewer professional terms and more plain words such as body parts and feelings to describe their health status and concerns due to their limited familiarity with professional medical terms [7,19]. However, little has been done to identify the usage patterns of such words and the extent to which they facilitate communication and social support among OHC participants.

## 1.1.3. Types of linguistic features and adaptation in OHC

Linguistic features in texts can be categorized into several types, including morphological, lexical, syntactic, semantic, and pragmatic [14,47]. The latter four are most relevant to written texts in online settings. The first two columns in Table 1 summarize common linguistic features studied in previous linguistics and stylometry literature. Lexical features focus on the usage of characters and words in sentences, such as the frequencies of various letters and the average length of words. For example, vocabulary richness measures have been used to reflect the educational background of authors [71]. Syntactic features focus on grammar and the appropriate use of words in sentences. Unlike lexical analysis, which is concerned with the inclusion of words, syntactic analysis emphasizes the concatenation and order of words in a sentence. Semantic features focus on the meanings of words behind their occur rence, such as the frequency of content-specific keywords [87] and topics (Nguyen et al., 2015). Another extensively studied semantic feature is sentiment polarity [52]. Past research has found that senti ment expressed by community members has a significant influence on their communication outcomes [23]. For example. opinion leaders commonly use many positive words to motivate and influence others [35]. Pragmatic features focus on the meaning of words and word choice in the appropriate contexts. Past research has consistently observed that using words and language matching that of the social group can significantly enhance the effectiveness of communication and social acceptance [10,35]. This phenomenon can be explained by homophily, where social interactions are more efficient between parties sharing commonalities [36,68]. Another interpretation is that shared language between an individual and peers is part of cognitive capital developed within online communities [32,48,83].

Common linguistic features in the literature and their adaptation in OHCs from a patient-centered perspective.

<table><tr><td rowspan="2">Type</td><td rowspan="2">Typical features</td><td colspan="2">Can OHC participants control this feature in their writing?</td></tr><tr><td>Yes</td><td>Not practical</td></tr><tr><td rowspan="3">Lexical</td><td rowspan="3">Character level Frequency of lowercase/uppercase letters Frequency of letters/digits/spaces/vowels/special characters Word level Frequency of words/long words/short words/alphanumeric words Average word length Average sentence length in words Length of the entire text in words Vocabulary richness</td><td>Patients can write or avoid complex sentences in their messages.</td><td>✓</td></tr><tr><td>Patients can write longer/shorter messages.</td><td>✓</td></tr><tr><td>Patients can choose to diversify their word choice.</td><td>✓</td></tr><tr><td>Syntactic</td><td>Frequency of function words/stopwords Frequency of punctuation Readability</td><td>Patients can carefully write messages to increase readability</td><td>✓</td></tr><tr><td>Semantic</td><td>Content-specific keywords/topics Sentiment</td><td>Patients can determine to what extent they discuss topics related to diseases, symptoms, treatments, and their relations. Patients can decide whether to reveal their emotions.</td><td></td></tr><tr><td>Pragmatics</td><td>Shared language use</td><td>Patients observe and use language conforming to the community norm.</td><td></td></tr></table>

A patient-centered perspective is essential when adopting these lin guistic features to the OHC context. A patient-centered perspective ad vocates that attention should be directed toward patient users during the design of health care services, including e-health services [82,84]. Pa tients’ needs, capabilities, and feelings should be prioritized over the efficiency of operations from health service providers. In OHCs, although many linguistic features can be extracted from the messages posted by users, not all of them have meaningful implications for pa tients. For example, while character-level lexical features could be useful for authorship attribution tasks [49], they are meaningless for patients in terms of obtaining social support because a typical patient user does not intentionally control the number of uppercase letters or digits in her posted messages. Similarly, patients do not determine the frequency of punctuation before writing; the actual usage of punctuation results from other aspects of writing, such as message length.

From a patient-centered perspective, some linguistic features are more relevant than others regarding whether OHC participants can consciously control them in their writing. Table 1 summarizes these features.

In the lexical feature category, vocabulary richness measures the number of unique words present in the text. Compared to all other lexical features, an individual has better control over the variety of words used for expression. For example, when expressing similar meanings, a user can decide whether to use synonyms or simply use the same term all the time. In the health care context, familiarity with various names of diseases, symptoms, medicines, treatments, and body parts could improve communication effectiveness. In addition, the health care vocabulary should help OHC participants effectively express their current situation and needs [50]. For example, instead of writing "feeling sick" all the time, an accurate description of the feeling such as "nasty," "dizzy," and "painful" in different situations could provide more information and help others provide better feedback.

For syntactic features, users can control the readability of their messages by carefully using punctuations and functional words [20]. Messages with great readability facilitate subsequent communication and social support. The effect of message length on communication outcomes is mixed. On the one hand, a long message (in terms of words or sentences) is likely to contain rich and detailed information that helps peers provide appropriate responses. For example, a recent study found that the message length of OHC messages was positively associated with the amount of informational support received [10]. On the other hand, long messages could cause cognitive burdens to readers, and most people might prefer succinct messages. In the same study, message length was found to be negatively associated with the amount of emotional support. Another study also observed that community mem bers appreciated brevity and succinctness in conversations [35].

For semantic features, OHC participants can decide whether to ex press their sentiment in the messages. Many participants join OHCs because of illness or other health concerns. Hence, negative sentiment is common among newcomers to OHCs. With the help of other peers, many patients overcome their difficulties over time. Previous research has observed negativity bias in many online communities [31]. For example, negative reviews could be perceived as more helpful than positive or neutral reviews [18]. In OHCs, participants tend to react more to mes sages with negative emotions [10]

In addition to sentiment, discussing relevant health care topics is another important semantic feature in the OHC context. For this pur pose, using correct terms plays an important role [8]. Past studies have observed a discrepancy between how medical experts and patients un derstand the same medical terms [7]. Likewise, interpretations of many terms may differ between OHC participants. For example, a diabetes patient in stage I seeking informational assistance may obtain inappro priate information from others if the patient simply uses the word "diabetes" instead of "diabetes-I." Many new patients experience lan guage barriers and are unfamiliar with professional medical terms [8]. Nevertheless, they can try to use plain health-related words to describe as many details as possible regarding their body parts, feelings, and disease progression. If these words semantically convey the meanings that patients wish to express, the communication can still be effective.

Among pragmatic features, a shared language is an important aspect of online communities. In OHCs, participants use many Internet slangs (e.g., sugarbetes to indicate diabetes). Using health language that other OHC participants also use may increase one’s social acceptance and lead to better communication outcomes.

## 1.2. Research gaps

The major research gaps in the existing literature are summarized below. First, for research investigating the antecedents of social support in OHCs, the central focus has been the community structure [3,9,30]. Existing research has mainly explained social support exchange based on social connections and structural capital accumulated by members of OHCs [9.34]. Limited research has attempted to understand how the linguistic features of OHC participants affect their communication and social support outcomes. In other nonhealthcare contexts, such as e-commerce and company discussion forums, various studies have shown that linguistic features embedded in texts play a crucial role in facilitating communication [18,35,64]. However, the impact of lan guage use in OHCs can differ considerably from other contexts because a unique aspect of OHCs is that patients generally have to use plain lan guage to describe complicated disease symptoms and treatments [75]. The discrepancy between simple health care language and professional medical terms could change how linguistic features affect communica tion outcomes. Therefore, examining how linguistic features of OHC participants affect their communication and social support outcomes could provide insights into these unique aspects. Second, studies investigating language use in online communities have focused on generic syntactic and lexical clues such as sentence length, vocabulary richness, and misspellings [10,35]. Few studies have examined semantic and pragmatic clues beyond sentiment in OHCs. Furthermore, not all linguistic features have meaningful implications for patients. Third, previous studies have focused on the linguistic characteristics of mes sage postings. A user-level linguistic analysis would complement the existing literature by providing additional insights into how patients should adjust their overall writing strategies to receive enhanced social support from the entire community.

To address these gaps, this study extracts various linguistic feature from OHC participants with a patient-centered perspective in mind. These features are used to construct user-level linguistic profiles that represent OHC participants’ language use. We then examine commu nication and social support patterns associated with these individual linguistic profiles.

## 2. Method

Fig. 1 shows the overall research framework and procedure used in this study. We collected data from a large OHC community and computationally generated linguistic profiles of OHC participants based on their texts. Relationships between the linguistic profiles of users and their communication activities were modeled as network patterns. The primary reason for examining the relationships from a network perspective using ERGM is that it enables an in-depth exploration of the interrelated factors, including linguistic features, different types of communication outcomes, their relationships, and the in terdependencies of such relationships [15,57,67]. In the next sub sections, we explain each component in Fig. 1.

## 2.1. Data collection and research testbed

The data were collected from Tianmijiayuan (bbs.tnbz.com), a leading online diabetes community in China where participants can discuss various topics related to diabetes and other health concerns. It was established in 2005, and the number of registered members exceeds 250,000 as of 2020. On Tnbz.com, users can leave replies to a thread or another reply by specifying the reply target (using buttons). A user can receive notifications from the website when replies are made to the user’s postings. This design helps us trace the replies between users as well as original message contents. All the messages and basic user profile information (e.g., registration time, diabetes type, and online friend ships) from 2005 to 2015 were collected.

## 2.2. User linguistic profiling

To extract the four levels of linguistic features from Chinese texts posted by Tnbz.com users, the software TextMind was used [22]. The TextMind was developed based on the Linguistic Inquiry and Word Count (LIWC) program. LIWC is a popular textual analysis package for studying word counts, word choice, and language styles. The primary goal of LIWC is to analyze the usage of words and the psychological process underlying word choice and categorize words into a large number of preset dictionary sets [54]. Its most commonly used pub lished set in 2007 covers over 30 different psychological process cate gories of words [55]. LIWC has gained increasing popularity in linguistic research, and its Chinese variant TextMind has also been used in previ ous research $[ 2 2 , 4 2 , 4 4 ]$

Among the various dictionary sets in LIWC 2007, the most relevant ones in our research context are biological words (including body, health, sexual, and ingestion words), perceptual words (see, hear, and feel related words), and causation words in the cognitive category. Causation words were included in our analysis because they help pa tients logically describe what may have caused their health condition. Additionally, affective process words, including positive and negative emotions (anxiety, anger, and sadness), are used to measure the senti ment expressed in messages. Table 2 lists the LIWC word categories used in this study and representative words in our research testbed. Based on these categories, the linguistic profiles of OHC participants were operationalized.

## 2.2.1. Health vocabulary richness (lexical feature)

To evaluate a user’s vocabulary richness in terms of health language, we first calculated the number of unique words falling in the LIWC 2017 biological and perceptual word categories based on all messages posted by the user. As the total word count increases, the number of unique words increases as well. To reduce the effect of total word count in measuring vocabulary richness, we adopted Dugast’s formula [70] to calculate user-level vocabulary richness:

$$
D = \frac {(\log (\text { total   word   count })) ^ {2}}{\log (\text { total   word   count }) - \log (\# \text { of   unique   bio   or   perception   words })}\tag{1}
$$

## 2.2.2. Message length (lexical feature)

Each user’s average message length was calculated based on the number of Chinese characters.

## 2.2.3. Sentence length (lexical feature)

Each user’s average sentence length in Chinese characters was calculated based on all the messages posted by the user.

## 2.2.4. Readability (syntactic feature)

Most messages in our research testbed were written in Chinese. To evaluate the readability of these Chinese messages, we used the Baidu readability API<sup>1</sup>, which is powered by a deep neural network (DNN)- based language model [2]. The DNN model evaluates the posterior probability of each tokenized Chinese unigram in a given sentence based on observations from training corpora. Typographical errors, syntactical errors, and word choice are inherently considered in the DNN-based language model. The probability of the entire sentence $\mathsf { P } ( \mathsf { w } _ { 1 } , \mathsf { w } _ { 2 } , . . . \mathsf { w } _ { \mathrm { N } } )$ is used to calculate sentence perplexity as

$$
p p l = 2 ^ {- 1 / N l o g _ {2} P (\mathrm{w1,w2,...wN})}\tag{2}
$$

where N is the number of words in the sentence, and w $( \mathrm { i } = 1 , 2 , . . . \mathrm { N } )$ are Chinese unigrams. The lower the perplexity is, the higher the readability of a sentence is. In this study, we standardized the perplexity (ppl) value of each sentence to [0, 1] and calculated the average ppl value of each user i as ppl . Finally, 1-ppl was used as the readability measure of user i, representing the average readability of sentences written by the user. To assess the validity of the returned readability scores by the API, we randomly selected 30 messages as our experiment set and randomly divided them into three equal portions. For each piece of data, according to the readability returned by the Baidu API. we sorted the text and generated ranking order 1. Then, we hired a native Chinese investigator to manually rank ten random messages from the set in terms of their readability, generating ranking order 2. We then compared ranking orders 1 and 2 to calculate Spearman's rank correlation between DNN readability scores and manual readability scores [61]. The process was repeated three times, and the three correlation coefficients were 0.976, 0.976, and 0.988, suggesting that the readability scores returned by the

![](/api/attachments/KZB8MV3Y/fulltext/images/4285e741a1bfd74eca6f858753daf9454b7b831e54fc260bc895d9ce7a81ae77.jpg)  
Fig. 1. Research framework and procedures.

Table 2  
LIWC word categories adopted in the OHC context.

<table><tr><td>LIWC category</td><td>Subcategory</td><td>Examples</td><td>Representative words in research testbed</td></tr><tr><td rowspan="4">Biological</td><td>Body</td><td>Cheek, hands, spit</td><td>脸,手,痰</td></tr><tr><td>Health</td><td>Clinic, flu, pill</td><td>医疗,感冒,药剂</td></tr><tr><td>Sexual</td><td>Horny, love, incest</td><td>发情,情爱,亲密</td></tr><tr><td>Ingestion</td><td>Dish, eat, pizza</td><td>食,碗筷,粥</td></tr><tr><td rowspan="3">Perceptual</td><td>See</td><td>View, saw, seen</td><td>看,见,瞅</td></tr><tr><td>Hear</td><td>Listen, hearing</td><td>听,闻,听见</td></tr><tr><td>Feel</td><td>Feels, touch</td><td>触摸,接触</td></tr><tr><td>Cognitive</td><td>Causation</td><td>Because, effect, hence</td><td>因为,所以,因此</td></tr><tr><td rowspan="5">Affective</td><td>Positive emotion</td><td>Love, nice, sweet</td><td>喜爱,良好,甜蜜</td></tr><tr><td>Negative emotion</td><td>Hurt, ugly, nasty</td><td>疼,痛,恶心</td></tr><tr><td>Anxiety</td><td>Worried, fearful, nervous</td><td>担心,害怕,紧张</td></tr><tr><td>Anger</td><td>Hate, kill, annoyed</td><td>恨,杀,烦躁</td></tr><tr><td>Sadness</td><td>Crying, grief, sad</td><td>哭,悲痛,悲伤</td></tr></table>

API were consistent with human judgment.

## 2.2.5. Sentiment (semantic feature)

The sentiment polarity of words was identified based on the LIWC2007 affective words category. Based on negativity bias [10,18,31] discussed in the previous section, the average number of negative emotion words in each message was used to calculate the negative sentiment of OHC participants. Most negation phrases in Chinese were tokenized as one word $( \boldsymbol { \mathrm { e . g . } }$ , 不好=not good) by LIWC, and hence the bias resulting from negation phrases was minimal [53].

## 2.2.6. Use of health-related terms (semantic feature)

For each user, we first identified the number of words falling into the LIWC 2017 biological, perceptual, and causation word categories. All threads and replies were combined to form the corpus for term identi fication. Based on the identified health-related terms, the average number of category terms in messages was used to measure the extent to which OHC participants used health-related language in each category. Repetitive words were counted during computation.

## 2.2.7. Shared health language (pragmatics feature)

To measure how well a user’s health-related word choice matches that of the entire community, we followed a previous study and used a style match measure adapted to the health language context [10,46]. Specifically, the proportion of health-related words falling under sub category k under LIWC-health categories (see Table 2) by user j was calculated as $\mathrm { P _ { j k } } .$ . For the causation word category with only one sub category, we extended the category to all functioning word categories, including pronouns, articles, prepositions, auxiliary verbs, and conjunction words, to better capture the writing logic. Similarly, the proportion of health-related words in the same subcategory by all other users was calculated as $\overline { { P } } _ { \mathrm { j k } }$ . Then, the linguistic style match of user j on subcategory k was calculated as:

$$
L S M _ {j k} = 1 - \frac {\left(\left| P _ {j k} - \overline {{P}} _ {j k} \right|\right)}{\left(\left| P _ {j k} + \overline {{P}} _ {j k} + 0 . 0 0 0 1 \right|\right)}\tag{3}
$$

Finally, all the subcategory style match scores $\mathrm { L S M _ { j k } }$ were averaged to calculate the overall style match score of the parent category.

## 2.3. Social support classification

In this study, we examine how the aforementioned linguistic char acteristics of OHC participants affect their chances of receiving replies, the chances that those replies develop into reciprocated conversations, and more importantly, the chances that social support emerges from these conversations.

As discussed previously, informational support and emotional sup port are two major types of social support in OHC, but they are not necessarily present in all message exchanges. To identify OHC messages that contain quality informational and emotional support content, we performed a pilot study to manually label over 2,600 messages on Tnbz. com. Two investigators reviewed each message to determine whether it contained informational support, emotional support, or both. To guide the manual review process, we used the Social Support Behavior Code (SSBC) [16]. This code has been used in previous research to classify social support messages into informational and emotional support [9]. More details regarding guidelines and inconsistency resolution are provided in Appendix A.

The manually labeled gold standard data were used as training and testing datasets to train and evaluate social support classification models. The source Chinese texts were first tokenized by Jieba (a Python package for splitting Chinese sentences). A list of custom diabetes terms was added to refine the word tokenization result (see Appendix B for the list of diabetes terms). The resulting term list was used to train the naïve Bayes, random forest, logistic regression, and XGBoost classifiers [11]. Tenfold cross-validation was used to evaluate the performance of all classifiers. The naïve Bayes classifier resulted in the best overall per formance, with 85% accuracy for informational support and 80% ac curacy for emotional support, which is comparable to previous studies [10,27]. More details regarding the performance metrics of all classifiers are presented in Appendix C.

## 2.4. Network construction

In this study, communication and social support activities were modeled as network patterns. Based on the reply relationships and message classification results, four different networks were extracted from the testbed: a reply network, a reciprocity network, an informa tional support network, and an emotional support network. The four types of ties in these networks serve as the dependent variables in the subsequent statistical models. We now describe how each type of tie was identified in this study.

The reply network was constructed based on reply relationships between OHC participants. If user A has replied to a message by user B, a directed link from A to B was identified. The tie strength (the number of times replies were made) was also calculated to identify strong and weak ties. Similarly, a reciprocated link was identified for a pair of users if user A replied to B and user B replied back to A. We also calculated the in tensity of reciprocated ties based on the number of mutual replies in different threads (e.g., a reply pattern A→B→A→B→A in the same thread will only create an intensity of 1 between users A and B, whereas multiple treads indicating mutual communications between A and B will increase the intensity of reciprocated ties between users A and B). The informational support and emotional support networks were con structed in a similar way as the reply network, except that only messages containing informational support or emotional support (identified in the social support classification step) were used during network construction.

Strong ties have always been considered to be beneficial to the ex change of information [25]. In line with the previous study, we further dichotomized the network and removed relatively weaker ties to capture the most representative communication and social support patterns between users [32,33,76]. The remaining isolated nodes were then removed from the network. Furthermore, we removed articles copied from other Internet sources and users who often post them<sup>2</sup>. These posts were typically very long and did not reflect users’ own linguistic char acteristics (e.g., tendencies to write long messages or sentences, ten dencies to use diverse vocabularies, etc.). The remaining number of nodes in each type of network is reported in Appendix D.

## 2.5. Exponential random graph model analysis

ERGM is a statistical network analysis model that can be used to test whether the observed networks exhibit theoretically hypothesized network patterns [57,80]. The network patterns (named configurations in ERGM terms) are specific combinations of nodes and ties in the network, reflecting the tendency for such network substructures to be exhibited during the network formation process. Specifically, recei ver/nodecov patterns represent tendencies for nodes with specific cat egorical/quantitative attributes to receive incoming network ties [57, 77]. Due to the exploratory nature of this study, we use the linguistic features of OHC participants and various types of interactions discussed in the previous subsections to construct various network patterns rep resenting possible underlying hypotheses leading to network formation. The constructed patterns and their explanation are summarized in Table 3.

In addition to the abovementioned network patterns, other structural configurations used in previous studies were also included as controls in ERGM analysis [9,10,32,43]. These control variables include edge/arc, the out-degree centrality of OHC participants (because social support was measured through content analysis of incoming replies, in-degree centrality was not considered as a control variable), user type (e.g., diabetes-I, diabetes-II), friendship (dyadic attribute for user pairs, indi cating whether one user has accepted a friendship request from the other), activity level (activity scores were provided by the OHC web site), and tenure (the length of membership in the online diabetes community since registration). Details of these control variables as well as the specification of the final ERGM are provided in Appendix E.

## 3. Results and discussion

## 3.1. ERGM coefficient estimation

Table 4 shows the results of the ERGM for four types of networks, where a user’s linguistic profile was evaluated based on all threads and replies posted by the user. Estimated ERGM coefficients are presented, and p-values are shown below them. The estimated ERGM coefficients represent the log-odds of the corresponding network ties, as shown in Table 3 and E (provided in Appendix E). A positive and significant co efficient indicates that the corresponding network ties are more likely to develop than by random chance. For instance, the estimated coefficient readability is 0.072 in the reply network. Then, the conditional log-odds of a directed tie adding a readability pattern is -6.411 + 0.072 = -6.339 (because the tie automatically adds an arc pattern as well). The proba bility that such a tie (a reply tie toward a user with one unit of read ability measure) would develop in the network is exp(-6.339)/(1 + exp (-6.339)) = 0.176%, which is greater than the probability that a reply tie would develop between any pair of users, which is exp(-6.411)/(1 + exp

Table 3  
Research hypotheses and graphical illustrations.

<table><tr><td>Configuration</td><td>Explanation of the hypothesized pattern</td></tr><tr><td>health_richness</td><td>The health vocabulary richness of an individual is positively associated with the chances of receiving incoming communication or social support.</td></tr><tr><td>message_length</td><td>The length of messages by an individual is positively associated with the chances of receiving incoming communication or social support.</td></tr><tr><td>sentence_length</td><td>The average length of sentences by an individual is positively associated with the chances of receiving incoming communication or social support.</td></tr><tr><td>readability</td><td>The readability of messages by an individual is positively associated with the chances of receiving incoming communication or social support.</td></tr><tr><td>negemo</td><td>The negative sentiment expressed by an individual is positively associated with the chances of receiving incoming communication or social support.</td></tr><tr><td>Percept bio cause</td><td>An individual&#x27;s use of health language is positively associated with the chances of receiving incoming communication or social support.</td></tr><tr><td>shared_affect shared_percept shared_bio shared_cause</td><td>Shared health language with the community is positively associated with the chances of receiving incoming communication or social support.</td></tr></table>

Table 4  
ERGM coefficients and p-values, all threads and replies combined.

<table><tr><td rowspan="2"></td><td colspan="4">Network type</td></tr><tr><td>Reply</td><td>Reciprocity</td><td>Informational support</td><td>Emotional support</td></tr><tr><td colspan="5">Control variables</td></tr><tr><td rowspan="2">arc/edge</td><td>-6.411***</td><td>-7.847***</td><td>-6.428***</td><td>-6.238***</td></tr><tr><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="2">out_degree</td><td>-0.0002</td><td>N/A</td><td>-0.0004</td><td>0.00003</td></tr><tr><td>0.226</td><td></td><td>0.105</td><td>0.886</td></tr><tr><td rowspan="2">type</td><td>0.312***</td><td>0.318***</td><td>0.255***</td><td>0.189***</td></tr><tr><td>0.000</td><td>0.000</td><td>0.000</td><td>0.001</td></tr><tr><td rowspan="2">friend</td><td>4.330***</td><td>4.901***</td><td>4.256***</td><td>4.724***</td></tr><tr><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="2">activity</td><td>-0.122**</td><td>-0.199**</td><td>-0.240***</td><td>-0.094</td></tr><tr><td>0.039</td><td>0.034</td><td>0.000</td><td>0.238</td></tr><tr><td rowspan="2">tenure</td><td>0.299***</td><td>0.624***</td><td>-0.538***</td><td>0.644***</td></tr><tr><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td colspan="5">Linguistic variables</td></tr><tr><td colspan="5">Lexical features</td></tr><tr><td rowspan="2">health_richness</td><td>-0.067***</td><td>0.006</td><td>-0.070***</td><td>-0.036</td></tr><tr><td>0.004</td><td>0.861</td><td>0.002</td><td>0.239</td></tr><tr><td rowspan="2">message_length</td><td>-0.002***</td><td>-0.002***</td><td>-0.001***</td><td>-0.002***</td></tr><tr><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="2">sentence_length</td><td>0.012</td><td>0.035**</td><td>0.024**</td><td>-0.043***</td></tr><tr><td>0.295</td><td>0.044</td><td>0.030</td><td>0.007</td></tr><tr><td colspan="5">Syntactic features</td></tr><tr><td rowspan="2">readability</td><td>0.072***</td><td>0.103**</td><td>0.039*</td><td>0.113**</td></tr><tr><td>0.008</td><td>0.043</td><td>0.058</td><td>0.012</td></tr><tr><td colspan="5">Semantic features</td></tr><tr><td rowspan="2">negemo</td><td>7.607***</td><td>6.403***</td><td>10.271***</td><td>4.174***</td></tr><tr><td>0.000</td><td>0.000</td><td>0.000</td><td>0.007</td></tr><tr><td rowspan="2">percept</td><td>13.020***</td><td>14.702***</td><td>16.393***</td><td>18.018***</td></tr><tr><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="2">bio</td><td>3.554***</td><td>6.106***</td><td>-0.423</td><td>2.699***</td></tr><tr><td>0.000</td><td>0.000</td><td>0.545</td><td>0.005</td></tr><tr><td rowspan="2">cause</td><td>18.320***</td><td>21.777***</td><td>6.222*</td><td>30.177***</td></tr><tr><td>0.000</td><td>0.000</td><td>0.058</td><td>0.000</td></tr><tr><td colspan="5">Pragmatic features</td></tr><tr><td rowspan="2">shared_affect</td><td>0.149</td><td>0.552***</td><td>0.077</td><td>-0.429***</td></tr><tr><td>0.140</td><td>0.001</td><td>0.427</td><td>0.001</td></tr><tr><td rowspan="2">shared_percept</td><td>-0.202**</td><td>-0.351**</td><td>-0.396***</td><td>-0.305**</td></tr><tr><td>0.028</td><td>0.016</td><td>0.000</td><td>0.011</td></tr><tr><td rowspan="2">shared_bio</td><td>-0.063</td><td>-0.409**</td><td>0.027</td><td>0.112</td></tr><tr><td>0.607</td><td>0.035</td><td>0.816</td><td>0.483</td></tr><tr><td rowspan="2">shared_cause</td><td>-0.320**</td><td>-1.219***</td><td>0.296**</td><td>-0.296</td></tr><tr><td>0.027</td><td>0.000</td><td>0.036</td><td>0.116</td></tr></table>

Note: \*p<0.1; \*\*p<0.05; \*\*\*p<0.01.

(-6.411)) = 0.164%. Similarly, a negative and significant coefficient indicates that the corresponding network ties develop with a lower probability than by random chance.

In all networks, coefficient estimates of arc/edge are negative and significant, indicating that the four types of networks after network dichotomization were sparse, which is consistent with the characteris tics of reply-based networks in other OHC studies [9,43]. For both type and friend configurations, the coefficients are positive and significant in all networks, indicating that OHC participants who were online friend or who had similar health conditions were likely to receive replies, develop reciprocated communication, and receive social support from one another. The coefficient for activity is negative and significant in all networks except the emotional support network, which indicates that highly active OHC participants received fewer replies and informational support and developed less reciprocated communication. These obser vations are consistent with prior findings [43]. The coefficient for tenure is positive and significant in the reply network, the reciprocity network, and the emotional support network, indicating that OHC participants who had long been in the community were associated with better chances of receiving replies, involving in reciprocated communication, and receiving emotional support. However, the coefficient of tenure is negative and significant in the informational support network, sug gesting that informational support to OHC participants with tenure was much less than the amount of emotional support they received. This finding implies that informational support was prioritized more toward new users in our research testbed.

The coefficient of health\_richness is negative and significant in both the reply network and informational support network, indicating that OHC participants who used a diverse set of perception and body-related terms were associated with lower chances of receiving replies and informational support. This observation diverges from our initial expectation that being versatile in using health-related words would increase one’s chances of receiving social support. We found that some of these users shared general knowledge and tips regarding the disease. These users were not asking for help and hence typically received only a couple of brief replies (e.g., "thanks for sharing!") rather than messages providing informational support. For users seeking informational sup port, using too many different terms may lead to confusion. For example, one patient posted "My abs hurt. Is there good medicine to deal with acid in stomach?" (after translation) The patient was replied with "Are you talking about muscle pain or stomachache? Waiting for him to clarify…." Therefore, consistently using the same words to describe the problems could be more effective when seeking informational support in OHCs.

The coefficient of message\_length is negative and significant in all four networks, indicating that OHC participants who tended to post long messages were associated with lower chances of receiving replies, reciprocated communication, informational support, and emotional support. These results are consistent with prior findings except for the one for informational support [10]. After reading several messages, we found that long messages typically ended with only a couple of replies. Users were less likely to participate in discussions where they needed to spend much time reading long messages. In light of this, starting a thread with brief messages could encourage more follow-up questions from OHC participants, which eventually helps increase the amount of social support.

The coefficient of sentence\_length is positive and significant in the reciprocity network and informational support network but is negative and significant in the emotional support network, indicating that OHC participants who tended to write long sentences in messages were associated with higher chances of reciprocated communication and informational support, but lower chances of emotional support. While an overall lengthy message might decrease its chance of being read and replied to, writing just a few longer sentences could help a patient accurately express their informational needs while maintaining a reasonable length of the message. Therefore, writing complex sentences may not negatively affect the chances of receiving informational sup port. However, patients who tended to write long sentences received less emotional support. To receive encouragement and sympathy from more peers, patients should avoid writing complex sentences.

The coefficient of readability is positive and significant in all four networks, indicating that OHC participants with low average sentencelevel perplexity were associated with higher chances of receiving re plies, reciprocated communication, informational support, and emotional support. This result is consistent with prior findings that the Flesch Reading Ease (FRE) index [20] of messages is positively associ ated with the amount of social support received in these messages [10]. However, FRE evaluates readability based on the number of words, the number of sentences, and the number of syllables. For a syntactically different language such as Chinese in our testbed, FRE is not applicable. Our DNN-based language model-based measure evaluates the read ability of a sentence by statistically estimating the likelihood of the given sequence of words and hence is applicable to a broader selection of languages. Furthermore, the DNN model does not consider the number of syllables in sentences. Thus, our finding suggests that for written Chinese texts in OHCs, sentences do not have to be easily pronounced to encourage communication or receive social support.

The coefficient of negemo is positive and significant in all four net works, indicating that OHC participants with more frequent use of negative terms per message were associated with higher chances of receiving replies, reciprocated communication, informational support, and emotional support. This result aligns with prior findings that the strength of negative sentiment expressed in an OHC message is posi tively related to the amount of social support received in these messages [10,43]. Although our results based on ERGM do not indicate causal relationships between the use of negative terms and outcomes of social support, by comparing our result with the message-level finding in Chen et al. [10], our result implies that this negativity bias [18,31] may also apply to the user level, indicating that desperate users receive more attention and social support in OHCs.

The coefficients for percept are positive and significant in all four networks, indicating that OHC participants with more frequent use of perception terms per message were associated with higher chances of receiving replies, reciprocated communication, informational support, and emotional support. The coefficients for bio are positive in all four networks except the informational support network, indicating that OHC participants with more frequent use of biological terms per mes sage were associated with higher chances of receiving replies, recipro cated communication, and emotional support. The coefficient of cause is positive and significant in all the networks except the informational support network. Using lots of causation words was typically associated with story-telling, where communication and social support were more likely to follow. Being logical and clearly expressing the situation is particularly important when seeking informational support. Overall, terms related to perception, body parts, and causation positively affected the chances of receiving replies, reciprocated communication, and emotional support.

For pragmatic features, the coefficient of shared affect is positive and significant in the reciprocity network but negative and significant in the emotional support network. This observation supports the principle of homophily, i.e., patients with similar moods and attitudes tend to develop long-term relationships [68]. However, the negative and sig nificant coefficient in the emotional support network indicates that the similarity of a user’s sentiment to the community is associated with lower chances of emotional support. This finding suggests that showing stronger sentiment (a higher proportion of affect words than the com munity average) could be more effective in causing emotional arousal [59]. Similarly, the negative and significant coefficients of shared\_percept in all four networks suggest that expressing how one feels in a unique way might be more effective for receiving replies, reciprocated communication, informational support, and emotional support. For example, a user with much more frequent use of perception words than an average OHC participant successfully showed his or her positive attitude toward living with diabetes and received many replies from others, most of which contained advice and encouragement. The coef ficient for shared\_bio is negative and significant in the reciprocity network, indicating that describing body parts in a unique way could lead to more attention and subsequent reciprocated communication. The coefficient of shared\_cause is negative and significant in both the reply network and the reciprocity network but is positive and significant in the informational support network. Exceptionally high or low usage of causation words that deviate from the community average often resulted in follow-up conversations to clarify the intent of OHC partic ipants, which potentially explains the negative coefficient of share d\_cause in the reply network and the reciprocity network. However, using a proportion of causation words that match the community norm led to receiving informational support efficiently with smaller number of replies. Overall, the effect of shared health language depends on both shared word categories and types of communication and social support.

## 3.2. Robustness tests

To assess the consistency of our findings, we performed several robustness tests. First, most users in our research testbed were patients and their family members. Only 11 users were doctors who posted at least one message. Considering that these medical professionals might have unique ways of responding to messages with different linguistic features, we reconstructed the networks based on only users who registered as "patients (including type 1/2/X diabetes)" or "a patient’s family members." The results show that all qualitative results remained the same as those in Table 4, indicating that our findings regarding the effect of linguistic features pertain to patient-patient communication. The quantitative analysis of patient-only networks can be found in Ap pendix F, Table F1.

Second, we used alternative corpora to evaluate the linguistic pro files of OHC participants. Specifically, only the starting threads of each user were used in the robustness tests because when OHC participants seek social support, they are more likely to start a thread than reply to others’ messages. Thus, evaluating linguistic features based only on starting threads could provide additional insights for OHC participants when they solicit social support from peers. The qualitative results from our robustness tests were largely consistent with our main results. Further details of the robustness tests are provided in Table F2 of Ap pendix F. Furthermore, goodness-of-fit (GOF) test results indicate that our coefficient estimates fit the observed networks well. All GOF pa rameters were smaller than 2, indicating a good fit of the models [28, 77]. Details of GOF tests are reported in Appendix G.

## 4. Conclusion

This study performed linguistic profiling on OHC participants based on a large dataset and empirically evaluated how users’ lexical, syn tactic, semantic, and pragmatic features affect their communication and social support outcomes. We found that lexical richness in health-related vocabulary was negatively associated with receiving replies and infor mational social support. Message length had negative relationship with receiving replies, reciprocated messages, informational support, and emotional support. Sentence length had positive relationship with receiving reciprocated communication and informational social support but had negative relationship with receiving emotional support. The readability of written texts consistently had positive relationships with these outcomes. Showing negative sentiment led to receiving both types of social support as well. The use of terms related to perception and body parts positively affected the chances of receiving replies and emotional support. The user of terms related to perception was additionally posi tively correlated with informational support. To receive communication and both social supports, being logical in expressions was also critical. The relationships between shared health language and social support were determined by the word category and social support type. Our study contributes to both the literature and practice, as discussed next.

## 4.1. Research implications

Our study contributes to the OHC and social support literature by examining various linguistic features of patients and their effects on the acquisition of social support. Most previous studies in this stream have focused more on the social network features of OHC participants [9,29]. Only a few recent studies have examined the linguistic characteristics of health-related posts, focusing mainly on a subset of linguistic features such as readability [10] and sentiment [10,43]. The work of [10] pro vides many insights into how linguistic signals embedded in OHC postings can affect social support exchange. Our work extends their study in three ways. First, to the best of our knowledge, this study is the first to examine linguistic features at multiple theoretical levels (i.e., lexical, syntactic, semantic, and pragmatic). This study thereby provides a comprehensive understanding of how social support can be facilitated by OHC participants’ writings, particularly semantic and pragmatic features that have been largely neglected in the literature. Second, the analyses of [10] were based on message-posting level (i.e., how the linguistic features of a post affect subsequent replies to the same post), whereas our analysis is based on individual user level (i.e., how the language use of individuals affects their overall communication and social support outcomes). The posting-level analysis could suggest how one can increase replies and social support given to a thread. Our user-level analysis complements the existing literature by providing additional insights into how patients should adjust their overall partic ipation activities to receive enhanced social support from the entire community. Third, importantly, this study adapts numerous linguistic features previously used in other fields to the OHC context. For example, in [10], the linguistic style match of a message posting to the community was evaluated based on general linguistic clues such as the use of pro nouns, articles, and prepositions. Instead, our study examined pragmatic features based on shared health language, including the use of body and perception-related words. The lexical richness measure in our study was also evaluated based only on health-related words instead of all unig rams. Examining these linguistic features adapted to the OHC context offers more precise advice to OHC stakeholders (elaborated in the practical implications section). Furthermore, the conceptualization and operationalization of these health-related linguistic features can be used in future OHC research.

Our work also contributes to the literature on health literacy and health outcomes. Numerous studies have highlighted the gap in profi ciency in medical terms between medical professionals and patients [7, 81. This knowledge discrepancy has resulted in communication barriers between experts and nonexperts in offline settings [8]. While OHCs are becoming increasingly popular for patients as an additional source to seek health care support, evaluating the need for health literacy in on line settings is a critical task in health care information systems research. In a previous study, the health literacy of a patient was found to posi tively relate to the acquisition of both informational support and emotional support [9]. In their work, health literacy was measured based on matching terms with a unified medical language system (UMLS), which includes more professional health terminologies than the LIWC health categories used in this study. As shown in our experimental results, our findings suggest that the requirement of health literacy can be relaxed when obtaining social support; hence, patients can use less professional language as long as they use words that accurately describe their body parts and feelings. Thus, our study provides additional in sights into how different levels of health literacy are associated with different types of social support in OHCs.

## 4.2. Practical implications

This study provides several implications to practitioners. Using a patient-centered perspective, we examined linguistic features that OHC participants can control. First, patients do not need great lexical richness when expressing their health care concerns online. Using too many different words to describe body parts and feelings could lead to confusion and hence fewer replies and informational support. Second, patients do not need to write long messages to obtain social support. Possibly due to lack of clarity, messages with lower lexical richness or brief messages receive more replies because peers tend to follow up with additional questions to clarify what the patient is asking. Through these interactions, patients eventually obtain social support. Therefore, one can strategically post brief messages with fewer details to solicit more replies and social support from peers. Second, although details are un necessary, the message content should be highly relevant. Our findings show that the more patients discuss their health care concerns by using terms related to body parts and feelings, the more likely they will receive informational and emotional support. Patients do not need to diversify their word choice about these topics, but they should increase the pro portion of health-related words in their messages. Third, readability is an essential factor in receiving more replies or social support. Patients should aim to reduce grammatical errors or typos in their messages. The developers of the OHC platform could also consider embedding auto mated grammar check tools in their sites to help patients improve the readability of messages. Fourth, using more negative emotional words increases the chances of receiving more replies and social support.

However, patients should express their true feelings rather than inten tionally increasing the frequency of negative words to make themselves look needy. In this regard, moderators of OHCs should redirect some of the community’s attention to patients who exhibit relatively positive moods, such as setting up a subforum for sharing positive patient stories. Finally, using causation words and functioning words that match the community’s standard increases the chances of receiving informational support. Patients are encouraged to read messages posted by other participants in the community for a while before posting their threads so that they can learn commonly used expressions by their peers to increase affinity.

## 4.3. Limitations and future directions

This study examined various linguistic features, including lexical, syntactic, semantic, and pragmatic features. One missing linguistic feature category includes morphology, which focuses on the roots of words or morphemes [6]. The morphological analysis does not apply to our research setting because of the nature of Chinese texts. Still, mor phemes can signal the motivation behind word choice, and it can be insightful to examine how patients’ psychological processes behind the texts ultimately affect their social support outcomes. Another limitation of this study is that our research testbed focused on only one prevalent chronic disease, namely diabetes. The lack of variety in diseases exam ined may have resulted in the insignificant effect of body part-related words on health outcomes, particularly the informational support received. To address this issue, future research could explore OHC platforms involving multiple diseases. Finally, our dataset included only a small number of medical professionals, and most of our findings are limited to patient-patient interactions. In other communities where more medical professionals interact with patients, the effects of lin guistic features may vary.

## CRediT authorship contribution statement

Shan Jiang: Research Idea, Paper Writing, Paper Reorganization; Xuan Liu: Research Idea, Paper Writing, Paper Revising; Xiaotong Chi: Data Collection, Data Analysis.

## Author statement

This is a statement for our entitled research “Effect of Writing Style on Social Support in Online Health Communities: A Theoretical Lin guistic Analysis Framework” submitted to the Information and Management.

## Declaration of Competing Interest

No competing financial interests exist.

## Acknowledgments

This research was supported by the National Natural Science Foun dation of China with grants (71971082, 71471064, 71371005, and 91646205), the Science and Technology Innovation Plan of Shanghai Science and Technology Commission (grant number 22692110200, 19692106700), and Fundamental Research Funds for the Central Universities.

## References

[1] Andy, A., & Guntuku, S. (2020). "Does Social Support Expressed in Post Titles Elicit Comments in Online Substance Use Recovery Forums?" arXiv preprint arXiv: 2011.05103.

[2] Arısoy, E., Sainath, T.N., Kingsbury, B., Ramabhadran, B., Arisoy, E., Sainath, T.N., Kingsbury, B., et al. (2012). "Deep Neural Network Language Models", NAACL-HLT

2012 Workshop, Association for Computational Linguistics, Montreal, Canada, pp. 20–28.

[3] Bambina, A. (2007), Online Social Support: The Interplay of Social Networks and Computer-Mediated Communication, Cambria Press, Amherst, NY.

[4] C.E. Beaudoin, C.C. Tao, Benefiting from social capital in online support groups: An empirical study of cancer patients, Cyberpsychol. Behav. 10 (4) (2007) 587–590.

[5] R. Bierstedt, P.M. Blau, Exchange and power in social life, Am. Sociol. Rev. 30 (5) (1964) 789–790.

[6] G. Booij, Lexical Phonology and Morphology. Encyclopedia of Language & Linguistics. Elsevier. Amsterdam. Netherlands. 2006, pp. 94–97.

[7] C.M. Boyle, Difference between patients’ and doctors’ interpretation of some common medical terms, Br. Med, J. (Clin, Res, Ed) 2 (5704) (1970) 286–289.

[8] C.M. Castro, C. Wilson, F. Wang, D. Schillinger, Babel babble: physicians’ use of unclarified medical jargon with patients, Am. J. Health Behav. 3 (1) (2007) 123–128.

[9] L. Chen, A. Baird, D. Straub, Fostering participant health knowledge and attitudes: an econometric study of a chronic disease-focused online health community J. Manage. Inform. Syst. 36 (1) (2019) 194–229.

[10] L. Chen, A. Baird, D. Straub, A linguistic signaling model of social support exchange in online health communities, Decis. Supp. Syst. 130 (1) (2020) 113–133.

[11] Chen, T. and Guestrin, C. (2016), "XGBoost: A scalable tree boosting system", Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 785–794.

[12] W.Y.S. Chou, Y.M. Hunt, E.B. Beckjord, R.P. Moser, B.W. Hesse, Social media use in the United States: implications for health communication, J. Med. Intern. Res. 11 (4) (2009) e48.

[13] Choudhury,D.M., & Kiciman, E. (2017). "The language of social support in social media and its effect on suicidal ideation risk". In Proceedings of the International AAAI Conference on Web and Social Media, Vol. 11, No. 1,pp.32-41.

[14] edited by A. Clark, C. Fox, S. Lappin, The handbook of computational linguistics and natural language processing, in: A. Clark, C. Fox, S. Lappin (Eds.), The Handbook of Computational Linguistics and Natural Language Processing, Wiley, Hoboken, 2010, https://doi.org/10.1002/9781444324044. available at.

[15] N.S. Contractor, P.R. Monge, P.M. Leonardi, Multidimensional networks and the dynamics of sociomateriality: Bringing technology inside the network, Int. J. Commun, 5 (1) (2011) 682–720

[16] C.E. Cutrona, J.A. Suhr, Controllability of stressful events and satisfaction with spouse support behaviors, Commun. Res. (1992), https://doi.org/10.1177/ 009365092019002002 available at.

[17] C. Dunkel-Schetter, Social support and cancer: findings based on patient interviews and their implications, J. Soc. Issu. 40 (4) (1984) 77–98.

[20] R. Flesch, A new readability yardstick, J. Appl. Psychol. 32 (3) (1948) 221–233.

[18] S.P. Eslami, M. Ghasemaghaei, K. Hassanein, Which online reviews do consumers find most helpful? A multi-method investigation". Decis, Supp. Syst, 113 (1) (2018) 32–42.

[19] L. Fallowfield, V. Jenkins, Effective communication skills are the key to good

[211 LC. Freeman. Centrality in social networks conceptual clarification. Soc. Netw. 1 (3) (1978) 215–239.

[22] R. Gao, B. Hao, H. Li, Y. Gao, T. Zhu, Developing simplified Chinese psychological linguistic analysis dictionary for microblog, Lect. Notes Comput. Sci. (2013) 359-368.

[23] A. <sup>´</sup> García-Crespo, R. Colomo-Palacios, J.M. Gomez-Berbís, ´ B. Ruiz-Mezcua, SEMO: a framework for customer social networks analysis based on semantics, J. Inform. Technol. (2010), https://doi.org/10.1057/jit.2010.1 available at

[24] E.P. Gianchandani, Toward smarter health and well-being: an implicit role for networking and information technology, J. Inform. Technol. (2011), https://doi. org/10.1057/jit.2011.5 available at.

[25] C. Haythornthwaite, Social network analysis: An approach and technique for the study of information exchange, Libr. Inform, Sci, Res. 18 (4) (1996) 323–342.

[26] Hodgkin, P., Louis, H. and Ben, M. (2018), "The Emerging World of Online Health Communities", available at: https://ssir.org/articles/entry/the\_emerging\_world \_of\_online\_health\_communities.

[27] Huang, K.Y. and Chengalur-Smith, I.S. (2014), "A social capital perspective to understand individual contribution of social support in healthcare virtual support communities", Proceedings of the Annual Hawaii International Conference on System Sciences, Waikola, HI, pp. 3489–3498.

[28] Huffaker, D., Wang, J.A., Treem, J., Ahmad, M.A., Fullerton, L., Williams, D. and Poole, M.S. (2009), "The social behaviors of experts in massive multiplayer online role-playing games", Proceedings of International Conference on Computational Science and Engineering, IEEE, Vancouver, Canada, pp. 1-14.

[29] J. Introne, I. Erickson, B. Semaan, S. Goggins, Designing sustainable online support: Examining the effects of design change in 49 online health support

[30] Introne, J., Semaan, B. and Goggins, S. (2016), "A sociotechnical mechanism for online support provision", Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, pp. 3559-3571.

[31] T.A. Ito, J.T. Larsen, N.K. Smith, J.T. Cacioppo, Negative information weighs more heavily on the brain: the negativity bias in evaluative categorizations, J. Pers. Soc. Psychol, 75 (4) (1998) 887–900.

[32] S. Jiang, H. Chen, Examining patterns of scientific knowledge diffusion based on knowledge cvyber infrastructure: a multi-dimensional network approach Scientometrics 121 (3) (2019) 1599–1617

[33] S. Jiang, Q. Gao, H. Chen, M.C. Roco, The roles of sharing, transfer, and public funding in nanotechnology knowledge-diffusion networks, J. Assoc. Inform. Sci. Technol,66 (5) (2015) 1017–1029

[34] S. Jiang, X. Liu, S. Lin, Y. Cheng, When do patients start benefiting from electronic weak ties? Empirical examination of online social capital accumulation", in: Proceedings of 40th International Conference on Information System, 2019, pp. 1–12.

[35] S.L. Johnson, H. Safadi, S. Faraj, The emergence of online community leadership, Inf. Syst. Res. 26 (1) (2015) 165–187.

[36] D.B. Kandel, Homophily, selection, and socialization in adolescent friendships, Am.

[37] P.J. Kovacs, M.H. Bellin, D.P. Fauri, Family-centered care: a resource for social work in end-of-life and palliative care. J. Soc. Work End-of-Life Palliat. Care 2 (1) (2006) 13–27.

[38] S D Kowitt, D Urlaub, L Guzman-Corrales, et al., Emotional support for diabetes management : an international cross-cultural study, Diabet. Educ. 41 (3) (2015) 291–300.

[39] B. Lakey, S. Cohen, Social Support Theory and Measurement, in: S. Cohen, G. Lynn, B. Underwood (Eds.), Social Support Measurement and Intervention, Oxford University Press, London, 2015, pp. 29–45.

[40] C.P.H. Langford, J. Bowsher, J.P. Maloney, P.P. Lillis, Social support: a conceptual analysis, J. Adv. Nurs. 25 (1) (1997) 95–100.

[41] S. Li, K.D. Coduto, L. Morr, Communicating social support online: the roles of emotional disclosures and gender cues in support provision, Telemat. Inform. 39 (2019) 92–100.

[42] H. Lin, J. Jia, J. Qiu, Y. Zhang, G. Shen, L. Xie, J. Tang, et al., Detecting stress based on social interactions in social networks, IEEE Trans. Knowl. Data Eng. 29 (9) (2017) 1820–1833.

[43] X. Liu, S. Jiang, M. Sun, X. Chi, Examining patterns of information exchange and social support in web-based health community: exponential random graph models, J. Inter. Med. Res. 29 (22) (2020) e18062.

[44] X. Liu, X. Liu, J. Sun, N.X. Yu, B. Sun, Q. Li, T. Zhu, Proactive suicide prevention online (PSPO): Machine identification and crisis management for Chinese socia media users with suicidal thoughts and behaviors, J. Med. Inter. Res. 21 (5) (2019) e11705.

[45] Ludlow, P. (1996), High Noon on the Electronic Frontier Conceptual Issues Iin Cyberspace, edited by Peter, L., MIT Press, Cambridge, available at:https://doi.org/ 10.1561/1500000001

[46] S. Ludwig, K. De Ruyter, D. Mahr, M. Wetzels, E. Brüggen, T. De Ruyck, Take their word for it: the symbolic role of linguistic style matches in user communities, in: MIS Quarterly: Management Information Systems, 38, 2014, pp. 1201–1217.

[47] R. Mitkov, The Oxford Handbook of Computational Linguistics, Oxford University Press, London, 2012, https://doi.org/10.1093/oxfordhb 9780199276349.001.0001 edited by Mitkov, R.available at.

[48] J. Nahapiet. S. Ghoshal, Social capital , intellectual capital , and the organizational advantage, Acad, Manage, Rey, 23 (2) (1998) 242–266.

[49] T. Neal, K. Sundararajan, A. Fatima, Y. Yan, Y. Xiang, D. Woodard, Surveying stylometry techniques and applications. ACM Comput, Sury. (CSUR) 50 (6) (2017

[50] L. Nie, Y.L. Zhao, M. Akbari, J. Shen, T.S. Chua, Bridging the vocabulary gap between health seekers and healthcare knowledge, IEEE Trans. Knowl. Data Eng. 27 (2) (2015) 396–409.

[51] M. Norberg, H. Stenlund, B. Lindahl, C. Andersson, J.W. Eriksson, L. Weinehall, Work stress and low emotional support is associated with increased risk of future type 2 diabetes in women, Diabet. Res. Clin. Pract. 76 (3) (2007) 368–377.

[52] B. Pang, L. Lee, Opinion mining and sentiment analysis, Found. Trend. Inform. Retriev, 2 (1) (2008) 1–90

[53] H. Park, S. Jiang, O.K.D. Lee, Y. Chang, Exploring the attractiveness of service robots in the hospitality industry: analysis of online reviews, Forthcoming in, Inform Syst Front (2021)

[54] Pennebaker, J.W. (2015), "The Development and Psychometric Properties of LIWC2015 James", University of Texas at Austin, available at:https://doi.org/ 10.2165/00044011-199815050-00006

[55] Pennebaker, J.W., Booth, R.J. and Francis, M.E. (2007), "Operator’s Manual: Linguistic Inquiry and Word Count LIWC2007", Depts.Ttu.Edu, available at:https:// doi.org/10.4018/978-1-60960-741-8.ch012.

[56] C.M. Ridings, D. Gefen, Virtual community attraction: why people hang out online, J. Comput.-Mediat. Commun. 10 (1) (2006) 1–10.

[57] G. Robins, P. Pattison, Y. Kalish, D. Lusher, An introduction to exponential random graph (p\*) models for social networks, Soc. Netw. 29 (2) (2007) 173–191.

[58] E.L. Rubenstein, They are always there for me’: The convergence of social support

[59] J.A. Russell. Core affect and the psychological construction of emotion. Psychol

[60] I. Ruthven, S. Buchanan, C. Jardine, Isolated, overwhelmed, and worried: Young first-time mothers asking for information and support online, J. Assoc. Inform. Sci. Technol, 69 (9) (2018) 1073–1083

[61] P. Sedgwick, Spearman’s rank correlation coefficient, BMJ (2014) 349

[62] S. Sharma, A. Khadka, Role of empowerment and sense of community on online social health support group, Inform. Technol. People 32 (6) (2019) 1564–1590.

[63] S.A. Shumaker, A. Brownell, Toward a theory of social support: closing conceptua

[64] M. Siering, J.A. Koch. A.V. Deokar, Detecting fraudulent behavior on crowdfunding platforms: the role of linguistic and content-based cues in static and dynamic contexts, J. Manage. Inform. Syst. 33 (2) (2016) 421–455.

[65] M.L. Slevin, S.E. Nichols, S.M. Downer, P. Wilson, T.A. Lister, S. Arnott, J. Maher, et al., Emotional support for cancer patients: what do patients really want? Br. J Cancer 74 (8) (1996) 1275–1279

[66] T.W. Smith, J.M. Ruiz, J.M. Cundiff, K.G. Baron, J.B. Nealey-Moore, Optimism and pessimism in social context: an interpersonal perspective on resilience and risk, J. Res. Personal. (2013), https://doi.org/10.1016/j.jrp.2013.04.006 available at.

[67] T.A.B. Snijders, P.E. Pattison, G.L. Robins, M.S. Handcock, New specifications for exponential random graph models, Sociol. Methodol. 36 (1) (2006) 99–153.

[68] X. Song, S. Jiang, X. Yan, H. Chen, Collaborative friendship networks in online healthcare communities: an exponential random graph model analysis, Lect. Notes Comput. Sci. (2014) 75–87.

[69] P. Spagnoletti, A. Resca, G. Lee, A design theory for digital platforms supporting online communities: a multiple case study, J. Inform. Technol. (2015), https://doi. org/10.1057/jit.2014.37 available at.

[70] J. Torruella, R. Capsada, Lexical statistics and tipological structures: a measure of lexical richness, Procedia 95 (25) (2013) 447–454.

[71] F.J. Tweedie, R. Harald-Baayen, How variable may a constant be? measures of lexical richness in perspective", Comput. Human. 32 (1998) 323–352.

[72] B.N. Uchino, Social support and health: a review of physiological processes potentially underlving links to disease outcomes, J. Behay. Med. 29 (4) (2006) 377-387.

[73] J.M. Ussher, C. Parton, J. Perz, Need for information, honesty and respect: patien perspectives on health care professionals communication about cancer and fertility, Reproduct. Health 15 (1) (2018) 1–12.

[74] M. Van der Eijk, M.J. Faber, J.W. Aarts, J.A. Kremer, M. Munneke, B.R. Bloem, Using online health communities to deliver patient-centered care to people with chronic conditions, J. Med. Intern. Res. 15 (6) (2013) e115.

[75] N.A. Vasilevsky, E.D. Foster, M.E. Engelstad, L. Carmody, M. Might, C. Chambers, H.J.S. Dawkins, et al., Plain-language medical vocabulary for precision diagnosis, Nat. Genet. (2018), https://doi.org/10.1038/s41588-018-0096-x available at.

[76] L. Wang, J. Chen, A. Marathe, A framework for discovering health disparitie among cohorts in an influenza epidemic, World Wide Web. 22 (6) (2019) 2997–3020.

[77] P. Wang, K. Sharpe, G.L. Robins, P.E. Pattison, Exponential random graph (p \*) models for affiliation networks, Soc, Netw, 31 (1) (2009) 12–25.

[78] X. Wang, K. Zhao, N. Street, Analyzing and predicting user participations in online health communities: a social support perspective, J. Med. Inter. Res. 19 (4) (2017) e130.

[79] Y.C. Wang, R.E. Kraut, J.M. Levine, Eliciting and receiving online support: Using computer-aided content analysis to examine the dynamics of online social support,

[80] Wasserman, S. and Robins, G.L. (2005), "An introduction to random graphs, dependence graphs, and p\*", Models and Methods in Social Network Analysis, pp. 148-161.

[81] M. White, S.M. Dorman, Receiving social support online: implications for health education, Health Educ. Res. 16 (2001) 693–707, https://doi.org/10.1093/her/ 16.6,693.

[82] E.Vance Wilson (Ed.), Patient-centered e-health, IGI Global, 2008.

[83] Y.L. Wu, Y.H. Tao, C.P. Li, S.Y. Wang, C.Y. Chiu, User-switching behavior in social network sites: A model perspective with drill-down analyses, Comput. Hum. Behav. 33 (2014) 92–103.

[84] J Xiang, S. Stanley, From online to offline: Exploring the role of e-health consumption, patient involvement, and patient-centered communication on perceptions of health care quality, Comput. Hum. Behav. 70 (2017) 446–452

[85] L. Yan, Y. Tan, Feeling blue? Go online: An empirical study of social support among patients", Inf. Syst. Res. 25 (4) (2014) 690–709.

[86] S. Zhang, L. Zhao, Y. Lu, J. Yang, Do you get tired of socializing? An empirical explanation of discontinuous usage behaviour in social network services", Inform. Manage, 53 (7) (2016) 904–914.

[87] R. Zheng, J. Li, H. Chen, Z. Huang, A framework for authorship identification of online messages: writing-style features and classification techniques, J. Am. Soc. Inform. Sci. Technol. 57 (3) (2006) 378–393.

Shan Jiang received a BS in management information systems from Tsinghua University, China, and the PhD degree in management information systems from University of Ari zona. He is now working as an assistant professor at University of Massachusetts Boston. His research interests include business intelligence, social media analytics, computational linguistics, and social network analysis. His works have appeared in IEEE TKDE, Decision Support Systems, Journal of American Society for Information Science and Technology, Journal of the Association for Information Systems, Information Frontier, and Interna tional Conference on Information Systems. Prior to joining UMass Boston, Professor Jiang worked as a visiting assistant professor at Pennsylvania State University.

Xuan Liu received a BS in software engineering and PhD degree in management infor mation systems from Shanghai Jiaotong University, China. She is now an associate pro fessor in business school at East China University of Science and Technology. Her research interests include e-health. business intelligence, social media analytics, and social network analysis. Her works have appeared in Journal of American Society for Information Science and Technology, International Journal of Electronic Commerce, Scientometrics, Com puters in Human Behavior, Information Technology & People, Journal of Medical Internet Research. International Journal of Medical Informatics. Telemedicine and e-Health, and so on.

Xiaotong Chi received a BS in business school and now is master student in management information systems at East China University of Science and Technology. Her research interests include e-health, text mining, and social network analysis. Her work is published in Journal of Medical Internet Research.
