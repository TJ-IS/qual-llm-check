---
otero_id: 3812
otero_key: "DT2BA37J"
title: "A linguistic signaling model of social support exchange in online health communities"
authors: "Langtao Chen; Aaron Baird; Detmar Straub"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113233"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A linguistic signaling model of social support exchange in online health communities

Langtao Chen<sup>a,⁎</sup>, Aaron Baird<sup>b</sup>, Detmar Straub<sup>c</sup>

<sup>a</sup> Department of Business and Information Technology, Missouri University of Science and Technology, Rolla, MO, USA <sup>b</sup> Institute of Health Administration and Department of Computer Information Systems, Robinson College of Business, Georgia State University, Atlanta, GA, USA <sup>c</sup> Fox School of Business, Temple University, Philadelphia, PA, USA

## A R T I C L E I N F O

Keywords: Online health communities Social support exchange Signaling theory Sentiment Negativity bias Linguistic style matching

## A B S T R A C T

Health care consumers and patients are increasingly using online health communities (OHCs) to exchange social support and enhance their well-being. The success of OHCs in promoting health, however, depends not just on posting activity by participants, but, crucially, on whether or not responses are subsequently received. While previous studies have considered various mechanisms by which the likelihood of social support provisioning can be increased (e.g., the establishment of social capital), the impacts of linguistic signals have yet to be considered. Therefore, we consider whether or not linguistic signals in posts—including sentiment valence, linguistic style matching, readability, post length, and spelling—impact the amount of support received. Adopting an overarching theoretical framework of signaling theory, this study proposes a model that explains the signaling roles of linguistic features within OHC posts in promoting social support provision from OHC participants. The re search model is empirically tested on a large dataset collected from an OHC platform covering multiple health conditions. Results show that afective linguistic signals, including negative sentiment and linguistic style matching, are efective in invoking both informational and emotional support from the community. We also find that informative linguistic signals including readability, post length, and spelling are positively associated with informational support receipt, while readability and spelling are also positively associated with emotional support receipt. Overall, this research not only enriches our current understandings of the linguistic signaling in OHCs, but also provides practical insights into improving social support exchange in OHCs.

## 1. Introduction

Online health communities (OHCs) are social media platforms where health consumers can post health-related questions, share health information and experiences, and exchange social support [1]. OHCs facilitate participant sharing information and emotional support by providing a vast amount of readily accessible resources that may otherwise be dificult to obtain in physical social networks. Extant research generally reinforces the idea that online social exchanges enhance participant psychological and functional well-being [2–4]. Such participant empowerment leads to benefits such as emotional well being, social well-being, increased optimism, being better informed, improved disease management, and enhanced confidence in relation ships with physicians [5].

If OHCs are to provide health care benefits and sustain (and grow) their operations, however, attention must be paid not only to factors such as structural social network patterns [2,3,6], reciprocity [7], and self-disclosure [8], but also to how the content itself impacts the willingness of participants to expend time and efort to respond. Of particular interest in this study is that consciously or unconsciously, OHC participants use linguistic signals in their online posts to motivate responses from other participants (these responses being termed “social support provision”) [9,10]. Interestingly, linguistic signals are relative to social groups, requiring that participants take the time and efort needed to understand how to most efectively communicate within a particular group. In other words, linguistic signals are not just a means of communication, but are also highly related to the social groups to which one belongs, meaning efective communication is predicated on not assuming homogeneity of linguistic signals between groups [11–13]. However, purposively choosing or refining language according to social groups' preferences can be time consuming, requiring voluntary time and efort on the part of participants [14–16]. Thus, when communicating within a particular social group, the participant must decide how much efort should be dedicated to signaling that he or she is willing to conform to the norms of the group [12,15]. Of particular importance is that choice of language has been widely regarded as a key feature for enacting social identity and displaying membership in social groups [17]. Further, language use has been found to relate to various online contexts such as online community leadership and social influence [18,19], online multiparty negotiations [20], crowdfunding platforms [21], and online customer reviews [22]. Such findings have yet to be fully extended to the OHC context, however, and little consideration has been given to the efect of linguistic signals on the propensity to receive social support responses. Thus, a fundamental question arising in this setting is whether linguistic fea tures afect how social support is exchanged within an OHC as well as the efectiveness of such exchange. We ask:

## RQ: How do linguistic features embedded in online health community posts impact the amount of social support provisioned by the community?

This study seeks to contribute to the literature by drawing on sig naling theory as our overarching theoretical framework, supplemented by other theories including negativity bias and communication accommodation theory. The overall goal is to investigate how multiple linguistic signals, including sentiment valence, linguistic style matching, readability, post length, and spelling, lead to social support provided to OHC posts. The proposed research model is tested by using fixed-efects Poisson models on a dataset collected from an OHC plat form covering multiple health conditions. This research has implications for participants who seek for social support from the OHCs. It also provides guidance for the design and management of online communities focused on social support exchange and promotion of well-being. To the best of our knowledge, the present study is the first to suggest how a set of important linguistic features in online posts can be lever aged to elicit a deeper level of social support from OHC peers.

## 2. Theoretical foundation and hypotheses

This study applies the overarching theoretical framework of sig naling theory. We start with a brief discussion of social support exchange, then discuss signaling theory, and then present our research model and provide support for our hypotheses.

## 2.1. Social support exchange

Social support is generally defined as the degree to which an in dividual's basic social needs such as afection, esteem or approval, belonging, identity, and security are met by others through interaction [23,24]. According to Cutrona and Suhr's classification scheme [25], social support exchanged in ofline settings can be categorized as: (1) informational support (e.g., providing detailed information or facts); (2) emotional support (e.g., being empathetic, caring, etc.); (3) esteem support (e.g., helping to build confidence); (4) tangible support (e.g., ofering services); and (5) network support $( \boldsymbol { \mathrm { e . g . } } ,$ , confirming belonging). The current study focuses on the efects of two of these, namely informational support and emotional support. These are the two most relevant types of social support exchanged in OHCs [3,26–29]. We assess the efects of linguistic signals on informational and emotional support separately in order to check whether such efects are similar across these two types of social support. Combining informational and emotional support may lead to the problem of Simpson's paradox [30] in which the efects of some factors on the sum of informational and emotional support may reverse when we check them on informational and emotional support individually.

Extant studies generally assert that social support exchange can promote the psychological health and functional well-being of participants. A variety of theoretical perspectives have been drawn on to explain this health-promoting function. The perspective of supportive actions posits that receipt of social support enhances coping, an outcome that can bufer the harmful impacts of stressors on health [31].

From the point of view of analogical behavioral processes, social support enhances healthy behaviors such as exercising, eating right, cessation of smoking, and active engagement in medical regimens [32]. Moreover, stress bufering theory likewise explains how social support promotes health [33]. According to stress bufering theory, social support not only boosts individuals' perceived capability to cope with stressful events, but also alleviates harmful stressors by providing solutions to the specific problems one encounters [33]. Despite this, the support seeker must obtain suficient and appropriate social support in a timely manner to experience well-being. We suggest linguistic signals will play a significant role in obtaining social support.

## 2.2. Signaling theory

Signaling theory, initially developed by Spence [34], addresses the information asymmetry between two parties in various economic and social settings where one party holds information about quality or intent while the other party lacks such information. Signaling theory explains how the former party communicates that information to the latter through a variety of signals, all with the intent of obtaining de sirable outcomes. Since its inception, signaling theory has been applied to a wide range of management and information systems (IS) contexts such as human resource management [35], entrepreneurship [36], ecommerce [37,38], consumer purchase decision [39], and knowledge management [40]. Signaling theory ties nicely to the setting of online social support exchange as well as the information asymmetry between social support seekers and givers, especially given that linguistics are the prime communication signals between individuals who do not always have access to the same information [41–43].

The key concepts in signaling theory include signaler, receiver, and signal [44]. In the context of OHCs, health consumers who are seeking social support are signalers with private information about their health conditions, with the intention of providing this information to the community. On the other hand, signal receivers are those participants who want to access (i.e., be in receipt of) private information about the seekers and thereafter potentially ofer support to others in need. Signals are how the social support seekers linguistically communicate [43]; this is carried out via online messages, the efort being expended to receive desired support from others. In the presence of information asymmetries, support seekers need to send deliberate signals to potentially under-informed others in an eficient and efective fashion in order to obtain a suficient amount of desired support in return. Choosing appropriate linguistic features in the OHC messages is critical for the success of online social support exchange since various linguistic characteristics can convey diferent kinds of information or emotion and ultimately lead to unequal outcomes. Afective and informative signals are two major types of properties embedded in social media content [45,46]. Afective properties express emotions or feelings [45], while informative properties disclose a high degree of accurate information to reduce information asymmetry between the two communication parties [47]. As explained in the sections that follow, we propose two specific types of signaling embedded in OHC posts: (1) afective signaling to elicit or enhance receivers' emotion or empathy and feelings of similarity; and (2) informative signaling to enhance signal observability and reduce the information acquisition cost for signal receivers.

## 2.3. Research model

As summarized in Fig. 1, and as further described in the following sub-sections, our research model leverages signaling theory to help understand and explain how negative sentiment, linguistic style matching, readability, post length, and the spelling of OHC posts as forms of signals explain variation in received social support. In sum, higher levels of all independent variables are hypothesized to positively relate to the receipt of informational and emotional social support.

![](/api/attachments/DT2BA37J/fulltext/images/4006d00c1c12a1193f42774b94f9d5400b89f410e77d8b7b23e3c39251c90be8.jpg)  
Fig. 1. A linguistic signaling model of social support exchange in online health communities.

## 2.4. Afective signaling in OHC messages

Afective signals are linguistic features of OHC posts that provide heuristic cues for motivating greater social support exchange in the community through emotion invoking linguistic mechanisms. Researchers have argued that afect should be incorporated into theory building as an inseparable part of social support exchange [48,49]. In the context of OHCs, we evaluate the efects of two such linguistic signals, namely negative sentiment and linguistic style matching.

## 2.4.1. Negativity bias

Individuals respond diferentially to positive and negative information. A large body of research suggests an inherent negativity bias in human information processing and decision making across a broad range of do mains [50]. Negativity bias generally refers to an automatic tendency for people to give a greater weight to negative entities (e.g., events, objects, or personal traits) than positive or neutral ones [51]. Rozin and Royzman [51] proposed four distinct manifestations of this general asymmetric bias towards negative information, including: (1) a stronger negative potency (i.e., negative information is perceived to be more salient to people than the equivalent positive information); (2) steeper negative gradients (i.e., the negativity of negative information grows faster in space or time than does the positivity of positive information); (3) higher negative dominance (i.e., combining negative and positive information leads, ironically perhaps, to a more negative impact on individuals); and (4) greater negative diferentiation (i.e., negative information results in more variability in individual responses). A brief explanation of the negativity bias is that “bad things will produce larger, more consistent, more multifaceted, or more lasting efects than good things” [50,p.,325].

User-generated content in social media is usually embedded with sentiment valence (i.e., an overall positive, neutral, or negative sentiment). Previous research on user-generated content has reported ne gativity bias in a wide range of settings. For instance, Eslami et al. [52] found that negatively framed online consumer reviews are perceived to be more helpful than positively or neutrally framed reviews. Stieglitz and Dang-Xuan [53] observed that negative Facebook postings trigger a larger number of responses/comments than positive posts. Park [54] suggested that highly negative news on Twitter induces more active information-seeking behavior than weakly negative news. In spite of the interesting inferences in this work, there have been few attempts to study negativity bias in online social support exchange.

Social support seekers hold both positive and negative private information about themselves. They can decide whether and how to reveal such information to potential respondents. Signaling theory applied at organizational levels traditionally focuses on “the deliberate communication of positive information in an efort to convey positive organizational attributes” [44,p.,44]. In OHCs, however, negativity bias theory would suggest that negative information would be more powerful in motivating social support exchange. According to this theory, hence, OHC posts characterized by negative sentiment valence will be more likely to attract attention from other online peers and thus lead to higher levels of social support provision. As negative information is detected by people faster than positive information [55], negativelyvalenced OHC posts should exert a stronger impact on impression formation [56]. As a result, posts with higher negative sentiment valence will tend to elicit stronger cognitive and behavioral responses from online peers. To summarize, online participants are more strongly motivated to detect and respond to negatively-valenced posts than positively-valenced ones. Hence, we propose:

H1a. The negative sentiment expressed in an OHC post is positively associated with the amount of informational support received.

H1b. The negative sentiment expressed in an OHC post is positively associated with the amount of emotional support received.

## 2.4.2. Linguistic style matching

Besides sentiments expressed in OHC posts, appropriate linguistic styles can also be an important signal for efectively eliciting social support from OHCs [9,10]. Communication accommodation theory (CAT) is a multidisciplinary theoretical framework of interpersonal communications that predicts and explains why individuals adapt their communication styles and patterns to create, maintain, or decrease social distance in social interaction [57]. Accommodation refers to the constant movement towards or away from others by changing one's communication behavior [57]. Two strategies of accommodation have been observed in a variety of situations: (1) convergence strategies have been used by individuals to adapt their communication styles to be come more similar to those of others as part of their need for approval or social acceptance; (2) divergence strategies are instead used to make focal individuals dissociate personally from others in social encounters [58]. Communication convergence can be achieved through verbal and nonverbal mimicking tactics such as matching linguistic styles, utter ance length, choice of words, gesture, and posture [59].

CAT has been applied to guide research in a wide range of contexts such as online customer reviews [41], online multiparty negotiations [20], social networks [60], user communities [42], to name a few. These studies have found a direct association between communication accommodation (mimicking) and interaction outcomes [12,15]. The current research extends the same CAT mechanism to OHC social support exchange. The basic tenet is that to obtain OHC social support when in need, support seekers must alter their linguistic styles to match the overall community linguistic style.

Linguistic mimicking or convergence can be further explained via the principle of homophily, a belief that individuals interact more with similar peers [61]. With respect to collaborative settings, previous studies have shown the existence of various forms of homophily such as knowledge homophily, gender homophily, and status homophily [7,62,63]. OHC social support exchange clearly depends on a strong basis of similarity between participants. Since participants purposively join a particular OHC to find and collaborate with peers with similar health conditions, they are drawn to community members with similar attributes. Linguistic mimicking in OHC posts can incentivize more efective social support exchange with similar participants compared with those same kind of exchanges with dissimilar members [7]. In fact, an OHC post that does not well match the overall linguistic style of the community indicates dissimilarity. Lack of perceived similarity or social identity between the social support seeker and most potential providers demotivates the act of social support provisioning. Thus, linguistic homophily, an important form of homophily, in OHCs can signal and enhance social ties among participants and foster supportive relationships among them [7]. Accordingly, we propose:

H2a. An OHC post's degree of convergent linguistic style matching with the linguistic style of the community is positively associated with the amount of informational support received.

H2b. An OHC post's degree of convergent linguistic style matching with the linguistic style of the community is positively associated with the amount of emotional support received.

## 2.5. Informative signaling in OHC messages

Although efective in eliciting an emotional arousal and enhanced homophily, afective signals embedded in OHC posts may not influence social support exchange on their own. OHC participants appear to also need informative signals in their posts, signals that allow more eficient information processing by potential support givers in the communities. Importantly, this has to be carried out so that such posts can motivate more social support exchange. The greater or more eficient information processing of OHC posts is reflected in the greater attention paid by potential support providers who have more thorough elaboration and extensive cognitive interpretations [50].

This study considers three important linguistic features as informative signals in OHC posts: (1) readability, (2) length, and (3) spelling of the post text. From the perspective of signaling theory, these linguistic features can enhance the observability (i.e., intensity, strength, clarity, and visibility) of signals sent out by social support seekers, thus facilitating information transfer from social support seekers to potential providers. This study focuses on the informative signals that facilitate to disclose a high degree of accurate information rather than on the facts of communication themselves. When these linguistic features are embedded and salient, potential social support providers will expend lower cogni tive efort in processing relevant information. A post with augmented linguistic features should thus engage more potential support providers, eliciting, in turn, more social support for the social support seeker.

Readability (or, expressed conversely, reading dificulty) refers to the extent to which the content can be easily understood by an intended audience. Existing research shows conflicting results regarding the efect of readability on online social interactions across settings. For example, Yin et al. [22] observed that reading dificulty has a negative efect on the usefulness of online merchant reviews at Yahoo! Shopping website. Yin et al. [64] later found that reading dificulty has a positive efect on the usefulness voting of online reviews at Apple's App Store. In OHCs, a social support seeker can readily adapt the readability of her/his posts to motivate responses. An OHC post with a low level of readability places a con siderable cognitive burden on the potential responders. Therefore, we posit:

H3a. The readability of an OHC post has a positive efect on the amount of informational support received.

H3b. The readability of an OHC post has a positive efect on the amount of emotional support received.

According to several scholars, the overall length of an OHC post is a direct proxy for the degree of information completeness [65]. Successful collaboration between participants largely depends on the efective and eficient information interchange between members. For social support seekers, the post should contain a full description of her/his health conditions, treatments, and questions or concerns about these conditions and treatments. A comprehensive description of the stresses currently encountered, or dificulties/hardships being experienced also makes evident the criticality of such social support to the original requester. Holding all other factors constant, a longer post not only invokes trust, but also provides suficient information for responding with specialized informational or emotional support. Thus, the following two hypotheses are proposed.

H4a. The length of an OHC post has a positive efect on the amount of informational support received.

H4b. The length of an OHC post has a positive efect on the amount of emotional support received.

Non-standard spelling and outright spelling errors are pervasive in online user-generated content [66,67]. The situation is very possibly even worse in OHCs where participants have health conditions that may degrade their ability to spell correctly. For this reason, spelling is another important factor that we posit can lead to successfully obtaining social support from online peers. In generic online social contexts, correct spelling in one's posts will not only create a good impression about the literacy of the sender, but also efectively convey the correct meaning to the target audience. Evidence for the perhaps surprising importance of this feature, Ghose and Ipeirotis [68] found that the proportion of spelling errors in an online product review is negatively associated with helpful votes received by the review. Given the pervasive nature of spelling errors in OHCs, we argue that the spelling of an OHC post matters for eficient social support exchange. An OHC post with good spelling can eficiently transfer accurate information from the social support seeker to potential support givers. Thus, we propose:

H5a. The degree of correct spelling in an OHC post has a positive efect on the amount of informational support received.

H5b. The degree of correct spelling in an OHC post has a positive efect on the amount of emotional support received.

## 3. Methods

## 3.1. Research setting and data collection

Our primary research method was a field study of a U.S.-hosted web-based OHC platform that uses communities to support social exchange among members. Participants in this no-charge platform can join one or more communities, each of which focuses on a particular health condition or disease; this allows them to readily share health related experience, ask questions, and respond to others. Specifically, a community member can submit a post to initialize a discussion on a particular question or topic. Other users then can share information or provide support by replying to this discussion thread. The similar research setting has been widely used by previous studies (e.g., [3,27,69,70]) to investigate online social support exchange.

![](/api/attachments/DT2BA37J/fulltext/images/4d6dadcdef4788c255ab13306a595670d6c6a7e6f69c94d883ec8fe715a9cd52.jpg)  
Fig. 2. A typical social support exchange scenario and measurement.

We collected a rich dataset of 238,617 posts with 2,312,410 replies submitted to nine communities on the OHC platform during the period from July 2006 to November 2014. Each community deals with one of nine chronic health conditions, specifically chronic pain, obesity, depression, anxiety, alcoholism, physical and emotional abuse, insomnia, type 2 diabetes, and HIV. In total there are 32,405 participants who submitted at least one post and 49,076 participants who replied at least once. On average, each poster submitted 7.4 posts and each respondent provided 47.1 replies. Data for the first 6 months were excluded to avoid the potential efect of initializing the online platform. The fixedefects regression model used in this research required at least two posts from each participant. Removing participants with only one post to the platform resulted in an unbalanced panel dataset containing 221,404 posts by 15,928 participants through 95 months (or nearly 8 years) from January 2007 to November 2014. The large volume of the data and the variety of communities ensure our dataset to be representative. Fig. 2 shows a typical example of social support exchange in OHCs as well as important linguistic measures extracted from the post and social support classification results. The details of variables and analytical methods used to measure them are explained in the sub-sections that follow.

## 3.2. Variables

Table 1 shows the definitions of variables in the analysis and analytical methods used to measure them. The unit of analysis was the individual OHC post. Fig. 3 summarizes the variable measurement and analysis procedures.

## 3.2.1. Dependent variables

A straight-forward count of replies containing informational and emotional support to an OHC post measured the amount of social support received by the post [3,71]. Given the large dataset of OHC posts and replies, automated content analysis was the most tractable approach [2,3,72,73]. This study applied natural language processing and machine learning methods to build social support classification algorithms. To test these approaches, the first procedure focused on randomly selecting 3086 replies from our dataset and then manually coding each reply as whether it provides informational and/or emotional support, according to the Social Support Behavior Code (SSBC) developed by Cutrona and Suhr [25].<sup>1</sup> The manual coding was treated as true classes for our support vector machine (SVM)-based classification algorithms [75]. Previous studies have shown that results of SVMbased automatic qualitative content analysis are comparable to those using manual content analysis [76,77]. Textual features extracted from the reply messages were input into the SVM classifiers. Applying a 10- fold cross-validation, we found that the SVM algorithm for the informational support classification had an 87.41% accuracy while the emotional support classifier resulted in an 84.01% accuracy rate. The performance of the SVM algorithm was similar to that of a classification framework using deep learning [78]. Then, the trained social support classification algorithms were used to automatically classify the remaining OHC replies. In that the unit of analysis for this study is the OHC post, automatic content analyses of social support at the reply level were aggregated to the post level (i.e., the total amount of information and emotional support that a post receives from the replies) in order to constitute the dependent variables.

## 3.2.2. Independent variables

The sentiment analysis tool SentiStrength<sup>2</sup> [79,80] yielded metrics for the strength of sentiment expressed in the OHC posts. This tool has been shown to perform better than a variety of other machine learning approaches [79]. SentiStrength assigns both a positive and a negative sentiment score to each OHC post. The positive sentiment score ranges from 1 (no positive attitude) to 5 (very strong positive attitude). Since SentiStrength calculates the raw negative sentiment score as a negative number, we reverse-coded it for easy interpretation such that the final negative sentiment score is on a scale of 1 (no negative attitude) through 5 (very strong negative attitude).

Table 1  
Description of variables.

<table><tr><td>Variable type</td><td>Variable</td><td>Description</td><td>Analytical Method</td></tr><tr><td rowspan="2">Dependent variables</td><td>Informational support</td><td>The number of replies with informational social support submitted to a post initiated by a participant.</td><td rowspan="2">Social support classification using SVM</td></tr><tr><td>Emotional support</td><td>The number of replies with emotional social support submitted to a post initiated by the participant.</td></tr><tr><td rowspan="5">Independent variables</td><td>Negative sentiment</td><td>The strength of negative opinion (in the range [1, 5], where 5 is the strongest negative opinion) expressed in the post initiated by the participant.</td><td>Sentiment analysis</td></tr><tr><td>Linguistic style match</td><td>The extent to which the linguistic style of the OHC post matches to the overall linguistic style of the community.</td><td rowspan="4">Linguistic analysis</td></tr><tr><td>Readability</td><td>The ease of reading the post initiated by the participant.</td></tr><tr><td>Post length</td><td>The number of words in the post initiated by the participant.</td></tr><tr><td>Spelling</td><td>The level of spelling of the post initiated by the participant as compared to a fully spell-checked and corrected version of the same post.</td></tr><tr><td rowspan="5">Control variables</td><td>Positive sentiment</td><td>The strength of positive opinion (in the range [1, 5], where 5 is the strongest positive opinion) expressed in the post initiated by the participant.</td><td>Sentiment analysis</td></tr><tr><td>Tenure</td><td>The tenure of the participant in the OHC, measured as the number of years between the current date and the date of the participant&#x27;s first activity.</td><td rowspan="4">Structured information extraction</td></tr><tr><td>Recent messages</td><td>The total number of posts and replies submitted by the participant in the most recent 30 days.</td></tr><tr><td>Health conditions</td><td>A particular chronic health condition that the post is about. We used eight dummy variables, each representing a health condition (or community).</td></tr><tr><td>Recent daily users</td><td>The average number of daily active users in the community in the most recent 30 days (in thousands).</td></tr></table>

![](/api/attachments/DT2BA37J/fulltext/images/eccf83e9b1517ce3ff99ffe99065f4ce257b74e615dec3690911865b4e39cc58.jpg)  
Fig. 3. Variable measurement and analysis procedures.

The formulas by Ludwig et al. [41,42] were adapted to calculate linguistic style matching of OHC posts to the overall linguistic style of the community. First, linguistic dimensions of OHC posts were analyzed using the linguistic inquiry and word count (LIWC) software tool [81].

LIWC has been widely applied by many studies for text analysis and its reliability and validity have been previously verified [81–83]. LIWC analyzes the linguistic styles of a text using a set of function word categories including: (1) personal pronouns (e.g., I, you, them, her), (2) impersonal pronouns (e.g., it, it's, that, those), (3) articles (i.e., a, an, the), (4) prepositions (e.g., to, at, with, above), (5) auxiliary verbs (e.g., am, will, have, can), (6) adverbs (e.g., absolutely, very, really, finally), (7) conjunctions (e.g., and, also, but, whereas), and (8) negations (e.g., can't, don't, no, never). Next a measure of the function word usage intensity of each OHC post p for each function word category j was calculated by the number of total function words in category j divided by the number of total words in post $p ,$ using the following formula:

$$
F W I _ {p j} = \frac {\text { TotalFunctionWords } _ {p j}}{\text { TotalWords } _ {p}}\tag{1}
$$

Following this was the measure of community level linguistic style as the average function word intensity of all posts $p ^ { \prime }$ submitted before the post p using the following formula:

$$
F W I _ {c p j} = \frac {\sum_ {p ^ {\prime} \in c} F W I _ {p ^ {\prime} j}}{N _ {c p}}\tag{2}
$$

where $N _ { c p }$ is the number of posts submitted before the post $p$ in community c. At this point, linguistic style matching of post $p$ for each function word category j is calculated as:

$$
L S M _ {p j} = 1 - \frac {(| F W I _ {p j} - F W I _ {c p j} |)}{(| F W I _ {p j} + F W I _ {c p j} + 0 . 0 0 0 1 |)}\tag{3}
$$

Consistent with Ludwig et al. [42], a very small number 0.0001 was added to the denominator to avoid empty sets. The overall linguistic style matching of post $p$ across all eight function word categories is calculated as the mean of linguistic style matching ratios for each function word category, using the following formula:

$$
L S M _ {p} = \frac {\sum_ {j} L S M _ {p j}}{8}\tag{4}
$$

Readability of the OHC post was set with the Flesch Reading Ease (FRE) metric originally developed by Flesch [84]. FRE estimates the ease of reading a text based on the number of words per sentence and the number of syllables per word. A higher FRE score means an easierto-read text. Previous studies on online communities have shown the validity of using FRE to measure online user-generated content [85,86]. The FRE measure was calculated as follows:

$$
\begin{array}{c} \text {Flesch Reading Ease = 206.835 - 1.015 * \frac {total words}{total sentences} - 84.6} \\ * \frac {\text {total syllables}}{\text {total words}} \end{array}\tag{5}
$$

Spelling correctness can be measured as the similarity between the original post text and the suggested revision of the text by an open source spell checker.<sup>3</sup> We calculated the Jaro-Winkler similarity [87] between the original text and the corrected text as the measure of the OHC post's spelling. The Jaro-Winkler similarity score falls between 0 and 1. The higher the similarity between the original text and the corrected version, the closer the metric approaches 1.

## 3.2.3. Control variable

We controlled for a set of other factors that could potentially explain the amount of social support provided to an OHC post, as described in Table 1. These control variables include: (1) the strength of positive sentiment expressed in the post (PosSenti); (2) tenure of the support seeker in the OHC (Tenure); (3) the number of messages (including both posts and replies) submitted by the seeker in the most recent 30 days (RecentMessages); (4) the average number of daily active users in the community in the most recent 30 days (RecentDailyUsers); and (5) the health condition of the poster. Table 2 shows the descriptive statistics and correlations of the variables.

## 3.3. Model specification and estimation

Because received informational support and emotional support are count variables, Poisson regression methods are the natural choice for estimating the efects of independent variables on them [88,89]. For such count data, a linear regression model even with a log-transformed dependent variable could perform poorly and thus not recommended [90]. Since individual posts are nested within participants who posted them, unobserved characteristics of participants could correlate with received social support as well as covariates, thus leading to biased estimates. To control for unobserved, time-invariant heterogeneity (such as personality traits and gender of the support seeker), we used a fixed-efects Poisson regression model where the fixed-efects represent the impact of participant heterogeneity on social support receiving [91]. The fixed-efects Poisson model is specified as:

$$
S o c i a l S u p p _ {i p} = \exp \left(\frac {N e g S e n t i _ {i p} \alpha_ {1} + L S M _ {i p} \alpha_ {2} + R e a d a b i l i t y _ {i p} \alpha_ {3} +}{\log (L e n g t h _ {i p}) \alpha_ {4} + S p e l l i n g _ {i p} \alpha_ {5} + W _ {i p} \delta + \mu_ {i}}\right) + \varepsilon_ {i p}\tag{6}
$$

where SocialSupp denotes the amount of social support (informational or emotional) that participant (i.e., social support seeker) i's post p receives from the online community; $N e g S e n t i _ { i p }$ is the negative sentiment score expressed in post p submitted by participant $i ; L S M _ { i p } ,$ , Readability<sub>ip</sub>, $L e n g t h _ { i p } ,$ and $S p e l l i n g _ { i p }$ denote the overall linguistic style matching, readability, length, and spelling of post p submitted by participant i; $W _ { i p }$ represents all control variables; $\mu _ { i }$ represents multiplicative participant level fixed efects (or unobserved heterogeneity); $\varepsilon _ { i p }$ is the error term; and ${ \bf { a } } _ { 1 } \mathrm { ~ - ~ } { \bf { a } } _ { 5 }$ and δ are the parameters for estimation. We conducted an F-test on a fixed-efects linear model and found that we can reject the null hypothesis that there is no participant-level heterogeneity (p-values $< \ 0 . 0 0 1 )$ , thus supporting the choice of fixed-efects models. We also carried out the Hausman [92] specification test and found evidence to support the choice of fixed-efects Poisson models, rather than random-efects Poisson models $( \chi ^ { 2 } = 3 4 6 . 9 6$ and 592.60 for informational support and emotional support, respectively, with p-values < 0.001). Robust standard errors clustered at the participant level were used to account for potential heteroscedasticity, autocorrelation, and overdispersion in the data [93].

## 4. Results

Table 3 presents the estimation results of comparative informational support receipt models. Variables were entered in a stepwise manner in order to check if the efects of primary independent variables keep consistent, thus ofering a more complete identification of the primary effects [94]. Model 1 only includes negative sentiment. Models 2 through 5 add linguistic style matching, readability, post length, and spelling in sequence. In model $^ { 6 , }$ control variables are added. Model 7 includes health condition dummies. The full model, model $^ { 8 , }$ brings in monthly dummies to control for potential time efects. Chi-square goodness of fit test shows that the empirical data fit the Poisson regression model very well (Wald $\chi ^ { 2 }$ ranges from 2312 to 5955, p-values < 0.001). As Poisson regressions do not report $\mathbb { R } ^ { 2 }$ type goodnessof-fit test statistics, we also calculated McFadden's Pseudo $\scriptstyle \mathrm { \mathrm { R } } ^ { 2 }$ as a measure to assess the model fit. The McFadden's Pseudo $\scriptstyle \mathrm { \mathrm { R } } ^ { 2 }$ values range from 20.8% in column 1 to 23.0% in column 8. The results provide evidence that negative sentiment, readability, post length, and spelling of post are important explanatory variables for informational support received by an OHC post, with statistically significant positive efects of all these explanatory variables (p-values $< ~ 0 . 0 0 1 $ ). Thus, hypotheses H1a, H2a, H3a, H4a, and H5a are supported.

Table 4 presents the estimation results of the emotional support receipt models. Variables were entered into the models in a similar stepwise manner as in the informational support receipt models. Wald $\chi ^ { 2 }$ ranges from 402.6 in column 1 to 4150 in column 8 with p-values < 0.001, suggesting that the empirical data fit the Poisson regression model very well. The McFadden's Pseudo $\mathbb { R } ^ { 2 }$ values range from 16.2% in column 1 to 17.6% in column 8. We note that the efect of post length on received emotional support changes from positive to negative after control variables are added into the regression model. This provides support that those control variables are important in order to obtain a more complete and accurate estimation of the primary efects proposed in the research model. As column 8 of Table 4 shows, the coeficients of negative sentiment, linguistic style matching, readability, and spelling are positive and statistically significant (p-values < 0.05) in the full model. Thus, hypotheses H1b, H2b, H3b, and H5b are supported. However, the efect of post length is negative (p-value < 0.05). Thus, hypothesis H4b is not supported.

Table 2  
Descriptive statistics and correlation coeficients (N = 221,404).

<table><tr><td>Variables</td><td>Mean</td><td>S.D.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1. Informational support</td><td>1.77</td><td>2.68</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Emotional support</td><td>1.87</td><td>3.29</td><td>0.23</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Negative sentiment</td><td>3.04</td><td>1.29</td><td>0.23</td><td>0.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Linguistic style matching</td><td>0.72</td><td>0.20</td><td>0.22</td><td>0.04</td><td>0.54</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Readability</td><td>68.30</td><td>186.76</td><td>0.02</td><td>0.01</td><td>0.03</td><td>0.09</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. Post length</td><td>149.81</td><td>240.96</td><td>0.12</td><td>0.02</td><td>0.35</td><td>0.35</td><td>0.01</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7. Spelling</td><td>0.94</td><td>0.04</td><td>-0.08</td><td>-0.04</td><td>-0.31</td><td>-0.44</td><td>-0.00</td><td>-0.32</td><td></td><td></td><td></td><td></td></tr><tr><td>8. Positive sentiment</td><td>2.43</td><td>0.92</td><td>0.02</td><td>0.10</td><td>0.25</td><td>0.41</td><td>0.02</td><td>0.34</td><td>-0.34</td><td></td><td></td><td></td></tr><tr><td>9. Tenure</td><td>0.79</td><td>1.04</td><td>0.01</td><td>0.02</td><td>0.01</td><td>0.03</td><td>-0.01</td><td>0.03</td><td>-0.04</td><td>0.03</td><td></td><td></td></tr><tr><td>10. Recent messages</td><td>136.25</td><td>252.43</td><td>-0.14</td><td>0.06</td><td>-0.18</td><td>-0.20</td><td>-0.01</td><td>-0.10</td><td>0.05</td><td>-0.05</td><td>-0.07</td><td></td></tr><tr><td>11. Recent daily active users</td><td>0.27</td><td>0.10</td><td>-0.14</td><td>0.01</td><td>-0.15</td><td>-0.16</td><td>0.00</td><td>-0.12</td><td>0.08</td><td>-0.09</td><td>-0.34</td><td>0.29</td></tr></table>

Table 3  
Estimates of received informational support model.

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td></tr><tr><td colspan="9">Primary variables</td></tr><tr><td>NegSenti</td><td>0.220***(0.005)</td><td>0.156***(0.005)</td><td>0.157***(0.005)</td><td>0.140***(0.005)</td><td>0.140***(0.005)</td><td>0.131***(0.005)</td><td>0.135***(0.005)</td><td>0.135***(0.005)</td></tr><tr><td>LSM</td><td></td><td>1.205***(0.039)</td><td>1.149***(0.041)</td><td>0.750***(0.048)</td><td>0.756***(0.048)</td><td>0.713***(0.048)</td><td>0.687***(0.047)</td><td>0.687***(0.047)</td></tr><tr><td>Readability</td><td></td><td></td><td>0.002***(0.000)</td><td>0.002***(0.000)</td><td>0.002***(0.000)</td><td>0.002***(0.000)</td><td>0.002***(0.000)</td><td>0.002***(0.000)</td></tr><tr><td>log (Length)</td><td></td><td></td><td></td><td>0.092***(0.008)</td><td>0.108***(0.009)</td><td>0.176***(0.009)</td><td>0.175***(0.009)</td><td>0.174***(0.008)</td></tr><tr><td>Spelling</td><td></td><td></td><td></td><td></td><td>0.942***(0.138)</td><td>0.808***(0.137)</td><td>0.827***(0.136)</td><td>0.853***(0.136)</td></tr><tr><td colspan="9">Control variables</td></tr><tr><td>PosSenti</td><td></td><td></td><td></td><td></td><td></td><td>-0.156***(0.006)</td><td>-0.153***(0.006)</td><td>-0.152***(0.006)</td></tr><tr><td>Tenure</td><td></td><td></td><td></td><td></td><td></td><td>-0.009(0.008)</td><td>-0.017*(0.008)</td><td>-0.151†(0.087)</td></tr><tr><td>log (RecentMessages)</td><td></td><td></td><td></td><td></td><td></td><td>-0.045***(0.003)</td><td>-0.043***(0.003)</td><td>-0.042***(0.003)</td></tr><tr><td>RecentDailyUsers</td><td></td><td></td><td></td><td></td><td></td><td>-0.565***(0.103)</td><td>-0.572***(0.102)</td><td>-0.725†(0.378)</td></tr><tr><td>Health condition</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Monthly dummies</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Observations</td><td>220,080</td><td>220,080</td><td>220,080</td><td>220,080</td><td>220,080</td><td>220,080</td><td>220,080</td><td>220,080</td></tr><tr><td>Log-likelihood</td><td>-380,151</td><td>-376,375</td><td>-376,106</td><td>-375,678</td><td>-375,575</td><td>-372,723</td><td>-370,195</td><td>-369,531</td></tr><tr><td>Wald  $\chi^2$ </td><td>2312***</td><td>2851***</td><td>2820***</td><td>2824***</td><td>2864***</td><td>3693***</td><td>4659***</td><td>5955***</td></tr><tr><td>McFadden&#x27;s Pseudo R2</td><td>0.208</td><td>0.216</td><td>0.216</td><td>0.217</td><td>0.218</td><td>0.223</td><td>0.229</td><td>0.230</td></tr></table>

Notes: (1) Fixed-efects Poisson regression for models 1 through 8; (2) \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, †p < 0.1; (3) Robust standard errors in parentheses.

The results suggest that providing full information in a post is in deed efective in obtaining informational support. Contrary to our hypothesis, too much information expressed in the post, especially when the post is intended to seek emotional support, increases the efort for the potential support providers to process it and thus may actually result in less emotional support receipt. Interestingly, our results show that positive sentiment is negatively associated with informational support receipt, but positively associated with emotional support receipt. This finding conflicts with previous studies in other settings. We provide more insights into why this might be in the Discussion section.

Since the coeficients of Poisson models cannot be directly interpreted, we also report the incidence rate ratios (IRR) to better understand the efects of explanatory variables on dependent variables. A shown in Table 5, the IRR estimates of negative sentiment for informational and emotional support receipt models are 1.145 and 1.078 respectively, meaning that an increase in negative sentiment by one unit (from a less negative sentiment to a more negative sentiment) lead to a hefty 14.5% increase in received informational support and a 7.8% increase in received emotional support, controlling for all other factors. In the same way, increasing the readability score by one unit increase the amount of received informational and emotional support by a miniscule 0.2% and 0.1%, keeping all other factors the same. As the LSM and spelling are measured as a ratio in the range of 0 to 1, their IRR estimates can be interpreted as the percentage of change in the received social support amount for the change of LSM and spelling from the worst score 0 to the best score 1. Thus, the change of an OHC post from no linguistic matching to perfect linguistic matching leads to on average a 98.8% increase in received informational support and a 24.5% increase in received emotional support. These results are particularly exciting.

Similarly, the change of an OHC post from all incorrect spelling to no spelling errors leads to on average a 134.6% increase in received informational support and a 52.3% increase in received emotional support. With respect to length of posts, the IRR coeficients of the log of post length are 1.190 and 0.979 for received informational and emotional support respectively, suggesting that a 100% increase in the number of words used in the OHC post leads to a 19.0% increase in received informational support and a 2.1% decrease in received emotional support, holding other factors constant. This is likewise substantial, but producing one expected result and one unanticipated result.

Table 4  
Estimates of received emotional support model.

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td></tr><tr><td colspan="9">Primary variables</td></tr><tr><td>NegSenti</td><td>0.098***(0.005)</td><td>0.075***(0.005)</td><td>0.077***(0.005)</td><td>0.071***(0.005)</td><td>0.071***(0.005)</td><td>0.078***(0.005)</td><td>0.075***(0.005)</td><td>0.075***(0.005)</td></tr><tr><td>LSM</td><td></td><td>0.361***(0.037)</td><td>0.305***(0.042)</td><td>0.181**(0.056)</td><td>0.181**(0.056)</td><td>0.209***(0.055)</td><td>0.218***(0.055)</td><td>0.219***(0.055)</td></tr><tr><td>Readability</td><td></td><td></td><td>0.001***(0.000)</td><td>0.001***(0.000)</td><td>0.001***(0.000)</td><td>0.001***(0.000)</td><td>0.001***(0.000)</td><td>0.001***(0.000)</td></tr><tr><td>log(Length)</td><td></td><td></td><td></td><td>0.030**(0.010)</td><td>0.036***(0.010)</td><td>-0.024*(0.010)</td><td>-0.021*(0.010)</td><td>-0.022*(0.010)</td></tr><tr><td>Spelling</td><td></td><td></td><td></td><td></td><td> $0.316^†$ (0.177)</td><td>0.396*(0.178)</td><td>0.423*(0.179)</td><td>0.421*(0.176)</td></tr><tr><td colspan="9">Control variables</td></tr><tr><td>PosSenti</td><td></td><td></td><td></td><td></td><td></td><td>0.135***(0.006)</td><td>0.131***(0.006)</td><td>0.130***(0.006)</td></tr><tr><td>Tenure</td><td></td><td></td><td></td><td></td><td></td><td>0.052***(0.009)</td><td>0.052***(0.010)</td><td>-0.453***(0.095)</td></tr><tr><td>log(RecentMessages)</td><td></td><td></td><td></td><td></td><td></td><td>-0.021***(0.004)</td><td>-0.025***(0.004)</td><td>-0.025***(0.004)</td></tr><tr><td>RecentDailyUsers</td><td></td><td></td><td></td><td></td><td></td><td>0.734***(0.133)</td><td>0.753***(0.137)</td><td>-0.102(0.371)</td></tr><tr><td>Health condition</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Monthly dummies</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Observations</td><td>218,669</td><td>218,669</td><td>218,669</td><td>218,669</td><td>218,669</td><td>218,669</td><td>218,669</td><td>218,669</td></tr><tr><td>Log-likelihood</td><td>-413,358</td><td>-412,795</td><td>-412,533</td><td>-412,479</td><td>-412,466</td><td>-410,174</td><td>-407,532</td><td>-406,647</td></tr><tr><td>Wald  $\chi^2$ </td><td>402.6***</td><td>417.4***</td><td>429.3***</td><td>430.4***</td><td>434***</td><td>1060***</td><td>3002***</td><td>4150***</td></tr><tr><td>McFadden&#x27;s Pseudo R2</td><td>0.162</td><td>0.163</td><td>0.164</td><td>0.164</td><td>0.164</td><td>0.169</td><td>0.174</td><td>0.176</td></tr></table>

Notes: (1) Fixed-efects Poisson regression for models 1 through 8; (2) \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, †p < 0.1; (3) Robust standard errors in parentheses.

## 5. Discussion

OHCs have emerged as an important research theme that ofers significant opportunities to contribute to information systems and associated research fields [95]. In this paper, we apply signaling theory to the new setting of OHCs. The theory has traditionally been applied to evaluations of transactions under conditions of information asymmetry when one party (e.g., a seller) is trying to signal information (e.g., quality) to another party (e.g., a buyer) [44]. Interestingly, signaling is also an essential aspect of linguistic theory in that vocabulary, grammar, syntax, and style act as representational signals of what a writer wants to convey to the recipient [96]. Linguistic signals also assume information asymmetry, as one individual is trying to inform another individual through the linguistic transfer. Furthermore, linguistic styles are not only used to inform, such as through the transfer of information from one individual to another, but also to influence, such as attempting to change another individual's thinking or to invoke a reaction [43].

Linguistic signaling is a fascinating and complex subject, especially so in an online environment where information asymmetries are often considerable. Invoking a response (such as an answer to a question or a supportive response) can be a major challenge given the weak ties as well as the temporal, social, and geographical separation that char acterize OHCs. However, we have yet to see a theoretical model that considers signaling with respect to linguistic styles in the context of OHCs. Given that linguistic styles have not been fully studied in prior OHC research, but are likely to play a significant role in the amount and form of social exchange that occurs in OHCs, this study has examined the efects of linguistic features of OHC posts on the social support provision. The understanding of linguistic features in online social interaction provides a theoretical foundation for understanding and promoting social support exchange within OHCs. The results of hypothesis testing are summarized in Table 6.

Incidence rate ratios (IRR) estimates of social support exchange model

<table><tr><td rowspan="2"></td><td colspan="3">Received informational support</td><td colspan="3">Received emotional support</td></tr><tr><td>IRR</td><td>Robust Std. Err.</td><td>P-value</td><td>IRR</td><td>Robust Std. Err.</td><td>P-value</td></tr><tr><td colspan="7">Primary variables</td></tr><tr><td>NegSenti</td><td>1.145***</td><td>0.005</td><td>0.000</td><td>1.078***</td><td>0.005</td><td>0.000</td></tr><tr><td>LSM</td><td>1.988***</td><td>0.093</td><td>0.000</td><td>1.245***</td><td>0.068</td><td>0.000</td></tr><tr><td>Readability</td><td>1.002***</td><td>0.000</td><td>0.000</td><td>1.001***</td><td>0.000</td><td>0.001</td></tr><tr><td>log(Length)</td><td>1.190***</td><td>0.010</td><td>0.000</td><td>0.979*</td><td>0.009</td><td>0.025</td></tr><tr><td>Spelling</td><td>2.346***</td><td>0.319</td><td>0.000</td><td>1.523*</td><td>0.267</td><td>0.016</td></tr><tr><td colspan="7">Control variables</td></tr><tr><td>PosSenti</td><td>0.859***</td><td>0.005</td><td>0.000</td><td>1.139***</td><td>0.007</td><td>0.000</td></tr><tr><td>Tenure</td><td>0.860†</td><td>0.075</td><td>0.081</td><td>0.635***</td><td>0.061</td><td>0.000</td></tr><tr><td>log(RecentMessages)</td><td>0.959***</td><td>0.003</td><td>0.000</td><td>0.975***</td><td>0.004</td><td>0.000</td></tr><tr><td>RecentDailyUsers</td><td>0.484†</td><td>0.183</td><td>0.055</td><td>0.903</td><td>0.334</td><td>0.782</td></tr></table>

Notes:  
⁎⁎p < 0.01.  
<sup>⁎⁎⁎</sup> p < 0.001.  
<sup>⁎</sup> p < 0.05.  
<sup>†</sup> p < 0.1.

Table 6  
Summary of hypothesis testing.

<table><tr><td>No.</td><td>Hypothesis</td><td>Supported?</td></tr><tr><td>H1a</td><td>The negative sentiment expressed in an OHC post is positively associated with the amount of informational support received.</td><td>Yes</td></tr><tr><td>H1b</td><td>The negative sentiment expressed in an OHC post is positively associated with the amount of emotional support received.</td><td>Yes</td></tr><tr><td>H2a</td><td>An OHC post&#x27;s degree of convergent linguistic style matching with the linguistic style of the community is positively associated with the amount of informational support received.</td><td>Yes</td></tr><tr><td>H2b</td><td>An OHC post&#x27;s degree of convergent linguistic style matching with the linguistic style of the community is positively associated with the amount of emotional support received.</td><td>Yes</td></tr><tr><td>H3a</td><td>The readability of an OHC post has a positive effect on the amount of informational support received.</td><td>Yes</td></tr><tr><td>H3b</td><td>The readability of an OHC post has a positive effect on the amount of emotional support received.</td><td>Yes</td></tr><tr><td>H4a</td><td>The length of an OHC post has a positive effect on the amount of informational support received.</td><td>Yes</td></tr><tr><td>H4b</td><td>The length of an OHC post has a positive effect on the amount of emotional support received.</td><td>No</td></tr><tr><td>H5a</td><td>The degree of correct spelling in an OHC post has a positive effect on the amount of informational support received.</td><td>Yes</td></tr><tr><td>H5b</td><td>The degree of correct spelling in an OHC post has a positive effect on the amount of emotional support received.</td><td>Yes</td></tr></table>

## 5.1. Implications for research and theory

While signaling has been extensively addressed in the management literature [44], the context of OHCs is very diferent from signaling between firms or between leaders, managers, and employees. In particular, OHCs are more similar to markets than hierarchies of individuals that have explicit reporting structures and relational norms. Reciprocity is not a requirement or even an expected norm within an OHC and invoking responses from other OHC participants is not simply about power relationships (as when my manager requests information that I must provide), but rather about seeking eforts of “volunteers” (when one receives prosocial behaviors from those with no obligation to respond).

Thus, we extend current research findings and theory by: (1) investigating a broad array of linguistic signals observed within OHC posts to better understand what motivates social support exchange in a prosocial environment, and (2) assessing the distinct impact of these signals on both informational support and emotional support received.

First and foremost, our findings demonstrate that linguistic sig nals—including negative sentiment valence, linguistic style matching, readability, post length, and spelling—do impact the amount (and type) of social support received from OHC participants. In other words, if social support exchange is the goal of the individual composing a post, the sentiment of the post. the style of the post content (relative to the style of the other posts in the particular OHC), the readability of the post, the length of the post, and the efort put into correctly spelling the words, all need to be carefully considered by the poster. This suggests that the conscientious poster needs to expend efort to both understand how the online community prefers to communicate as well as to how to best formulate the information in the original post. If the poster's goal is to engage the rest of the community, as it should be, then the original posting should be attractive to those who may voluntarily respond.

Second, as mentioned earlier, one of our results conflicts with prior findings in that we found that positive sentiment is negatively associated with informational support receipt, but positively associated with emotional support receipt. Prior research has found that sentiment of either type, positive or negative, typically results in a larger quantity of feedback, suggesting that emotion of any type invokes responses from community participants. For example, Hufaker [19] found that online community participants who express afect (both positive and negative) receive more message feedback from group members. Stieglitz and Dang-Xuan [97] concluded that political Twitter messages characterized by more sentiment (both positive and negative) are retweeted more often and receive the first retweet more quickly. Our findings, though, show a more complex relationship in OHCs. In this community, we argue that positive and negative sentiment have to be diferentially modelled to best uncover the fundamental impacts of positive versus negative sentiment on interaction outcomes. This may explain why our results difer from that of prior studies.

## 5.2. Implications for practice

Our results have interesting implications for those who design and manage OHCs. Given that the goal of OHC designers and managers is typically to develop a platform that can generate a large number of posts and responses by a wide variety of participants, our findings demonstrate that attention needs to be paid not only to facilitating eficient exchange, but also to the linguistic form of the exchange. In particular, research has generally shown that individuals participating in social groups often want to achieve their individual goals efectively when making use of group-resources and will engage in mimicking and conforming behaviors in order to be accepted [12,15]. Given that lin guistic signals are an important mechanism of gaining acceptance [10] and, in our case, improving the chances of receiving responses, it is natural to think that adopting an efective linguistic form is typically the responsibility of the OHC participants. In other words, the OHC provides the platform, but it is up to the members to efectively make use of the social features that emerge. However, interestingly, our findings suggest that OHCs could take a more proactive role in facilitating linguistic behaviors that, as a result of this study, are now known to increase the potential for receiving responses.

For instance, OHC designers, managers, and moderators could take an active role in examining what types of linguistic features invoke the preferred quality and quantity of responses. Perhaps in a particular OHC, most posters use a specific style of writing that helps to eficiently convey facts first and contains opinions or more emotional content second. In such cases where certain styles become norms and social conformity is essential for increasing the probability of receiving social support, then the OHC could proactively: (1) educate new participants as to what linguistic features are preferred by the community (e.g., sentiment, length, style, etc.), and/or (2) provide real-time suggestions as posts (or responses) are being written, such as alternate wordings or styles that better match the type of posts (or responses) previously seen in the community. Designers and managers may even consider an innovative feature that can analyze the content of the post and then provide a probability of receiving social support given the writing style used (e.g., length, spelling errors, style match to the community, etc.). If the participant then saw something like, “This post has a 19% chance of re ceiving 1 response and an 8% chance of receiving more than 1 response,” as well as some suggestions on how to increase these probabilities, perhaps social support would become more efectively exchanged. In this way, OHC designers and mangers can take an active, rather than a passive role in building the community in ways that may be more eficient (and immediate) than by simply having moderators try to either regulate content or suggest revisions before content is posted.

## 5.3. Limitations and future research

This study is limited by: (1) our focus on specific linguistic features, (2) our focus on one set of OHC communities, and (3) the methods we have applied on our analysis. We note that there are many additional linguistic features, including grammar, the mix of information, emotion, and opinion in a single post, acknowledgement of prior posts, etc. that may play a role in whether or not responses are received. Further, communities of diferent types, such as health support versus IT support [94], are likely to value diferent linguistic styles. Even further, participants from diferent cultures, or those who are divided into sub-groups within a single community, would also be interesting considerations.

Therefore, we also suggest that there are many opportunities for fu ture research in this interesting area of study. For instance, perhaps linguistic style matching is especially important for new members of a community, but then becomes less important as a member's tenure increases. Of course, such findings could also be nuanced by the type of community, the type of support being requested, as well as cultural norms exogenous to the online community itself. Further, there might be an opportunity to evaluate linguistic style matching at a more granular level, such as for certain sub-groups within online communities. For example, some posting in an online community about depression may need to follow a somewhat diferent linguistic style than someone posting in a discussion group focused on cancer. In addition, future research can further explore the inconsistent efects of positive sentiment and post length on online social support exchange by adopting new theoretical perspectives as well as considering potential moderation efects.

## 6. Conclusion

Health consumers can benefit from OHC participation only if they are able to obtain needed social support from the community. Drawing from the overarching conceptual framework of signaling theory, this study proposed a comprehensive model to explain how linguistic features of OHC posts influence the amount of informational and emo tional support that the support seeker can receive from the community. Our empirical analysis shows that efective communication in health social media platforms depends on the deliberate selection of signals to transfer. This research not only provides a nuanced theoretical understanding of how afective signaling (including sentiment valence and linguistic style matching) and informative signaling (including readability, post length, and spelling) impact social support exchange in online health communities, but also ofers practical implications for improving social support exchange in such communities.

## References

[1] G. Eysenbach, J. Powell, M. Englesakis, C. Rizo, A. Stern, Health related virtual communities and electronic support groups: systematic review of the efects of online peer to peer interactions, BMJ 328 (7449) (2004) 1–6.

[2] L. Yan, Y. Tan, Feeling blue? Go online: an empirical study of social support among patients, Information Systems Research 25 (4) (2014) 690–709.

[3] L. Chen, A. Baird, D. Straub, Fostering participant health knowledge and attitudes: an econometric study of a chronic disease-focused online health community, Journal of Management Information Systems 36 (1) (2019) 194–229.

[4] P.K.H. Mo, N.S. Coulson, Developing a model for online support group use, empowering processes and psychosocial outcomes for individuals living with HIV AIDS. Psychology & Health 27 (4) (2012) 445–459.

[5] P.K.H. Mo, N.S. Coulson, Are online support groups always beneficial? A qualitative exploration of the empowering and disempowering processes of participation within HIV/AIDS-related online support groups, International Journal of Nursing Studies 51 (7) (2014) 983–993.

[6] S. Ba, L. Wang, Digital health communities: the efect of their motivation mechanisms, Decision Support Systems 55 (4) (2013) 941–947.

[7] N. Kordzadeh, C.Z. Liu, Y. Au, J. Clark, A multilevel investigation of participation within virtual health communities, Communications of the Association for Information Systems 34 (26) (2014) 493–512

[8] Y.-C. Wang, R.E. Kraut, J.M. Levine, Eliciting and receiving online support: using computer-aided content analysis to examine the dynamics of online social support, Journal of Medical Internet Research 17 (4) (2015).1–23

[9] T. Carrick, A. Rashid, P.J. Taylor, Mimicry in online conversations: an exploratory

study of linguistic analysis techniques, Proceedings of the 2016 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining, IEEE Press, San Francisco, CA, 2016, pp. 732–736.

[10] S.A. Rains, Language style matching as a predictor of perceived social support in computer-mediated interaction among individuals coping with illness, Communication Research 43 (5) (2016) 694–712.

[11] J. Bryden, S. Funk, V.A. Jansen, Word usage mirrors community structure in the online social network twitter, EPJ Data Science 2 (3) (2013) 1–9.

[12] R.B. Cialdini, N.J. Goldstein, Social influence: compliance and conformity, Annua Review of Psychology 55 (1) (2004) 591–621.

[13] A.L. Gonzales, J.T. Hancock, J.W. Pennebaker, Language style matching as a predictor of social dynamics in small groups, Communication Research 37 (1) (2010) 3–19.

[14] S. Narayanan, P.G. Georgiou, Behavioral signal processing: deriving human beha vioral informatics from speech and language, Proceedings of the IEEE, 2013, pp. 1203–1233.

[15] T.L. Chartrand, J.L. Lakin, The antecedents and consequences of human behavioral mimicry. Annual Review of Psychology 64 (2013) 285–308

[16] J.L. Lakin, T.L. Chartrand, Using nonconscious behavioral mimicry to create af filiation and rapport, Psychological Science 14 (4) (2003) 334–339.

[17] J.M. Miller, Language use, identity, and social interaction: migrant students in Australia, Research on Language and Social Interaction 33 (1) (2000) 69–100.

[18] S.L. Johnson, H. Safadi, S. Faraj, The emergence of online community leadership, Information Systems Research 26 (1) (2015) 165–187.

[19] D. Hufaker, Dimensions of leadership and social influence in online communities, Human Communication Research 36 (4) (2010) 593–617.

[20] D.A. Hufaker, R. Swaab, D. Diermeier, The language of coalition formation in online multiparty negotiations, Journal of Language and Social Psychology 30 (1) (2011) 66–81.

[21] M. Siering, J.-A. Koch, A.V. Deokar, Detecting fraudulent behavior on crowdfunding platforms: the role of linguistic and content-based cues in static and dynamic contexts, Journal of Management Information Systems 33 (2) (2016) 421–455.

[22] D. Yin, S. Bond, H. Zhang, Anxious or angry? Efects of discrete emotions on the perceived helpfulness of online reviews, MIS Quarterly 38 (2) (2014) 539–560.

[23] P.A. Thoits, Conceptual, methodological, and theoretical problems in studying social support as a bufer against life stress, Journal of Health and Social Behavior 23 (2) (1982) 145–159.

[24] B.H. Kaplan, J.C. Cassel, S. Gore, Social support and health, Medical Care 15 (5) (1977) 47–58.

[25] C.E. Cutrona, J.A. Suhr, Controllability of stressful events and satisfaction with spouse support behaviors, Communication Research 19 (2) (1992) 154–174

[26] D.O. Braithwaite, V.R. Waldron, J. Finn, Communication of social support in computer-mediated groups for people with disabilities, Health Communication 11 (2) (1999) 123–151.

[27] P.K.H. Mo, N.S. Coulson, Exploring the communication of social support within virtual vommunities: a content analysis of messages posted to an online HIV/AIDS support group, Cyberpsychology & Behavior 11 (3) (2008) 371–374.

[28] K.-Y. Huang, I. Chengalur-Smith, A social capital perspective to understand individual contribution of social support in healthcare virtual support communities, Proceedings of the 47th Hawaii International Conference on System Sciences, 2014, pp. 3489–3498.

[29] N.S. Coulson, H. Buchanan, A. Aubeeluck, Social support in cyberspace: a content analysis of communication within a Huntington's disease online support group, Patient Education and Counseling 68 (2) (2007) 173–178

[30] C.R. Blyth, On Simpson's paradox and the sure-thing principle, Journal of the American Statistical Association 67 (338) (1972) 364–366.

[31] B. Lakey, S. Cohen, Social support theory and measurement, in: S. Cohen, LG. Underwood. B. Gottlieb (Eds.). Social Support Measurement and Intervention: A Guide for Health and Social Scientists, Oxford University Press, New York, 2000 pp. 29–52.

[32] B.N. Uchino, Social support and health: a review of physiological processes potentially underlving links to disease outcomes, Journal of Behavioral Medicine 29 (4) (2006) 377–387

[33] S. Cohen, Social relationships and health, American Psychologist 59 (8) (2004) 676-684

[34] M. Spence, Job market signaling, Quarterly Journal of Economics 87 (3) (1973) 355-374.

[35] M.M. Suazo, P.G. Martínez, R. Sandoval, Creating psychological and legal contracts through human resource practices: a signaling theory perspective, Human Resource Management Review 19 (2) (2009) 154–166.

[36] J.J. Janney, T.B. Folta, Moderating efects of investor experience on the signaling value of private equity placements, Journal of Business Venturing 21 (1) (2006) 27–44.

[37] J.D. Wells. J.S. Valacich. T.J. Hess, What signal are vou sending? How website quality influences perceptions of product quality and purchase intentions, MIS Quarterly 35 (2) (2011) 373–396.

[38] H.S. Choi, M.S. Ko, D. Medlin, C. Chen, The efect of intrinsic and extrinsic quality cues of digital video games on sales: an empirical investigation. Decision Support Systems 106 (2018) 86–96.

[39] C.M.K. Cheung, B.S. Xiao, I.L.B. Liu, Do actions speak louder than voices? The signaling role of social information cues in influencing consumer purchase deci sions. Decision Support Systems 65 (2014) 50–58

[4o] A. Durcikova. P. Grav. How knowledge validation processes affect knowledge contribution. Journal of Management Information Systems 25 (4) (2009) 81-17

[41] S. Ludwig, K.d. Ruyter, M. Friedman, E.C. Brüggen, M. Wetzels, G. Pfann, More than words: the influence of affective content and linguistic style matches in online re: views on conversion rates, Journal of Marketing 77 (1) (2013) 87–103.

[42] S. Ludwig, K. De Ruyter, D. Mahr, M. Wetzels, E. Brüggen, T. De Ruyck, Take their

word for it: the symbolic role of linguistic style matches in user communities, MI Quarterly 38 (4) (2014) 1201–1217.

[43] K.L. Blankenship, T.Y. Craig, Language use and persuasion: multiple roles for linguistic styles, Social and Personality Psychology Compass 5 (4) (2011) 194–205.

[44] B.L. Connelly, S.T. Certo, R.D. Ireland, C.R. Reutzel, Signaling theory: a review and assessment, Journal of Management 37 (1) (2011) 39–67.

[45] K. Denecke, W. Nejdl, How valuable is medical social media data? Content analysis of the medical web, Information Sciences 179 (12) (2009) 1870–1880.

[46] X. Ni, G.-R. Xue, X. Ling, Y. Yu, Q. Yang, Exploring in the weblog space by detecting informative and affective articles. Proceedings of the 16th International Conference on World Wide Web, ACM, Banf, Alberta, Canada, 2007, pp. 281–290.

[47] I. Montiel, B.W. Husted, P. Christmann, Using private management standard cer tification to reduce information asymmetries in corrupt environments, Strategic Management Journal 33 (9) (2012) 1103–1113

[48] E.J. Lawler, S.R. Thye, Bringing emotions into social exchange theory, Annual Review of Sociology 25 (1999) 217–244.

[49] K.S. Cook, C. Cheshire, E.R. Rice, S. Nakagawa, Social exchange theory, Handbook of Social Psychology, Springer, New York, NY, 2013, pp. 61–88.

[50] R.F. Baumeister, E. Bratslavsky, C. Finkenauer, K.D. Vohs, Bad is stronger than good, Review of General Psychology 5 (4) (2001) 323–370.

[51] P. Rozin, E.B. Royzman, Negativity bias, negativity dominance, and contagion, Personality and Social Psychology Review 5 (4) (2001) 296–320.

[52] S.P. Eslami, M. Ghasemaghaei, K. Hassanein, Which online reviews do consumers find most helpful? A multi-method investigation, Decision Support Systems 113 (2018) 32-42.

[53] S. Stieglitz, L. Dang-Xuan, Impact and difusion of sentiment in public communication on facebook, 20th European Conference on Information Systems, 2012, pp. 1–13 Barcelona, Spain.

[54] C.S. Park, Applying “negativity bias” to twitter: negative news on twitter, emotions, and political learning, Journal of Information Technology & Politics 12 (4) (2015) 342–359.

[55] A. Dijksterhuis, H. Aarts, On wildebeests and humans: the preferential detection of negative stimuli, Psychological Science 14 (1) (2003) 14–18.

[56] G. Peeters, J. Czapinski, Positive-negative asymmetry in evaluations: the distinction between afective and informational negativity efects, European Review of Socia Psychology 1 (1) (1990) 33–60

[57] H. Giles, T. Ogay, Communication accommodation theory, Explaining Communication: Contemporary Theories and Exemplars, Lawrence Erlbaum, Mahwah, NJ, 2007, pp. 293–310.

[58] C. Gallois, T. Ogay, H. Giles, Communication accommodation theory: a look back and a look ahead, in: W.B. Gudykunst (Ed.), Theorizing About Intercultural Communication, Sage, Thousand Oaks, 2005, pp. 121–148.

[59] J. Gasiorek, Theoretical perspectives on interpersonal adjustments in language and communication, in: H. Giles Ed (Ed.), Communication Accommodation Theory: Negotiating Personal Relationships and Social Identities Across Contexts, Cambridge University Press, 2016, pp. 13–35.

[60] N. Tamburrini, M. Cinnirella, V.A.A. Jansen, J. Bryden, Twitter users change word usage according to conversation-partner social identity, Social Networks 40 (2015) 84–89.

[61] E.M. Rogers, D.K. Bhowmik, Homophily-heterophily: relational concepts for communication research, Public Opinion Quarterly 34 (4) (1970) 523–538.

[62] Z. Wang, J.B. Walther, S. Pingree, R.P. Hawkins, Health information, credibility, homophily, and influence via the internet: web sites versus discussion groups, Health Communication 23 (4) (2008) 358–368.

[63] J.B. Walther, S. Pingree. R.P. Hawkins. D.B. Buller. Attributes of interactive online health information systems. Journal of Medical Internet Research 7 (3) (2005) e33

[64] D. Yin, S.D. Bond, H. Zhang, Keep your cool or let it out: nonlinear efects of expressed arousal on perceptions of consumer reviews, Journal of Marketing Research 54 (3) (2017) 447–463.

[65] G. Eysenbach, J. Powell, O. Kuss, E. Sa, Empirical studies assessing the quality of health information for consumers on the world wide web: a systematic review, JAMA 287 (20) (2002) 2691–2700.

[66] B. Desmet. V. Hoste. Emotion detection in suicide notes, Expert Systems with Applications 40 (16) (2013) 6351–6358.

[67] X. Liu, J. Liu. H. Chen, Identifving adverse drug events from health social media: a case study on heart disease discussion forums, International Conference on Smart Health, Springer, Beijing, China, 2014, pp. 25–36.

[68] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Transactions on Knowledge and Data Engineering 23 (10) (2011) 1498–1512

[69] A.T. Chen, Exploring online support spaces: using cluster analysis to examine breast cancer, diabetes and fibromvalgia support groups, Patient Education and Counseling 87 (2) (2012) 250–257.

[70] S.J. Beck, E.A. Paskewitz, W.A. Anderson, R. Bourdeaux, J. Currie-Mueller, The task and relational dimensions of online social support. Health Communication 32 (3) (2017).347–355

[71] H. Kuang-Yuan. L. Chengalur-Smith. A. Pinsonneault. Sharing IS caring: social support provision and companionship activities in healthcare virtual support communities, MIS Ouarterly 43 (2) (2019) 395–423

[72] R. Aggarwal, H. Singh, Diferential influence of blogs across diferent stages of decision making: the case of venture capitalists, MIS Quarterly 37 (4) (2013) 1093-1112.

[73] J. Wu, L. Huang, J.L. Zhao, Z. Hua, The deeper, the better? Efect of online brand community activity on customer purchase frequency, Information & Management 52 (7) (2015) 813–823.

[74] D. Straub, M.-C. Boudreau, D. Gefen, Validation guidelines for IS positivist research, Communications of the Association for Information Systems 13 (1) (2004) 380–427.

[75] L. Wang, Support Vector Machines Theory and Applications, Springer, Berlin; New York, 2005.

[76] K.-Y. Huang, P. Nambisan, Ö. Uzuner, Informational support or emotional support: preliminary study of an automated approach to analyze online support community contents, Proceedings of the 31st International Conference on Information Systems, 2010 St. Louis.

[77] Y.-C. Wang, R. Kraut, J.M. Levine, To stay or leave?: the relationship of emotional and informational support to commitment in online health support groups, Proceedings of the ACM 2012 Conference on Computer Supported Cooperative Work, ACM, Seattle, Washington, USA, 2012, pp. 833–842.

[78] L. Chen, A classification framework for online social support using deep learning, Lecture Notes in Computer Science 11589 (2019) 178–188.

[79] M. Thelwall, K. Buckley, G. Paltoglou, D. Cai, A. Kappas, Sentiment strength detection in short informal text. Journal of the American Society for Information Science and Technology 61 (12) (2010) 2544–2558.

[80] M. Thelwall, K. Buckley, G. Paltoglou, Sentiment strength detection for the social web, Journal of the American Society for Information Science and Technology 63 (1) (2012) 163–173.

[81] J.W. Pennebaker, R.L. Boyd, K. Jordan, K. Blackburn, The Development and Psychometric Properties of LIWC2015, University of Texas at Austin, Austin, TX, 2015.

[82] Y.R. Tausczik, J.W. Pennebaker, The psychological meaning of words: LIWC and computerized text analysis methods, Journal of Language and Social Psychology 29 (1) (2010) 24–54.

[83] J.W. Pennebaker, M.E. Francis, Cognitive, emotional, and language processes in disclosure, Cognition & Emotion 10 (6) (1996) 601–626.

[84] R. Flesch, A new readability yardstick, Journal of Applied Psychology 32 (3) (1948) 221-233.

[85] E. Omernick, S.O. Sood, The impact of anonymity in online communities, 2013 International Conference on Social Computing, 2013, pp. 526–535. Alexandria, VA, USA.

[86] M. Oztok, D. Zingaro, C. Brett, J. Hewitt, Exploring asynchronous and synchronous tool use in online courses, Computers & Education 60 (1) (2013) 87–94

[87] W.E. Winkler, String comparator metrics and enhanced decision rules in the fellegi sunter model of record linkage, Proceedings of the Section on Survey Research Methods, American Statistical Association, 1990, pp. 354–359

[88] A.C. Cameron, P.K. Trivedi, Microeconometrics: Methods and Applications, Cambridge University Press. New York. 2005.

[89] J. Hausman, B.H. Hall, Z. Griliches, Econometric models for count data with an application to the patents-r & d relationship, Econometrica 52 (4) (1984) 909–938.

[90] R.B. O’hara, D.J. Kotze, Do not log-transform count data, Methods in Ecology and Evolution 1. (2) (2010) 118–122

[91] A.C. Cameron, P.K. Trivedi, Microeconometrics Using Stata, Stata Press, College Station, Texas, 2009.

[92] J.A. Hausman, Specification tests in econometrics, Econometrica: Journal of the Econometric Society 46 (6) (1978) 1251–1271.

[93] J.M. Hilbe, Negative Binomial Regression, 2nd ed., Cambridge University Press, 2011.

[94] L. Chen, A. Baird, D. Straub, Why do participants continue to contribute? Evaluation of usefulness voting and vommenting motivational affordances withir an online knowledge community. Decision Support Systems 118 (2019) 21–32

[95] L. Chen. A. Baird. D. Straub. An analysis of the evolving intellectual structure of health information systems research in the information systems discipline, Journa of the Association for Information Systems 20 (8) (2019) 1023–1074

[96] J.L. Morgan, K. Demuth, Signal to Syntax: Bootstrapping From Speech to Grammar in Early Acquisition, Psychology Press, New York, 2014.

[97] S. Stieglitz, L. Dang-Xuan, Emotions and information difusion in social media—- sentiment of microblogs and sharing behavior, Journal of Management Informatior Systems 29 (4) (2013) 217–248

Dr. Langtao Chen is an Assistant Professor in the Department of Business and Information Technology at Missouri University of Science and Technology. Dr. Chen's research focuses on health information technology, online communities, business analy tics, and user experience. He has published in such journals as Decision Support Systems, Journal of Management Information Systems, Journal of the Association for Information Systems, Journal of Computer Information Systems, and others

Dr. Aaron Baird is an Associate Professor in the Institute of Health Administration and Department of CIS at the Robinson College of Business at Georgia State University. Dr. Baird's research primarily focuses on the assimilation and use of health IT. He has pub lished in such journals as the Decision Support Systems, European Journal of Information Systems, Journal of Management Information Systems, Information Systems Research, Journal of Medical Internet Research. and others

Dr. Detmar Straub is a Professor and the IBIT Research Fellow at Temple University's Fox School. He is a Regents Professor Emeritus of the University System of Georgia, formerly holding an endowed professorship in the Robinson College of Business at Georgia State University. He has published over 200 papers in such journals as MIS Quarterly, Management Science, Information Systems Research, Journal of Management Information Systems. Journal of AIS. Decision Sciences, and Organization Science
