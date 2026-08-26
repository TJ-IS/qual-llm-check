---
otero_id: 14192
otero_key: "3T2S3BK9"
title: "A social appraisal mechanism for online purchase decision support in the micro-blogosphere"
authors: "Yung-Ming Li; Cheng-Yang Lai"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.11.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A social appraisal mechanism for online purchase decision support in the micro-blogosphere

![](/api/attachments/3T2S3BK9/fulltext/images/e2ae2de72271a7a511da2c9409e69e0c93c021c134ffe9f291d27f045d6a3f68.jpg)

Yung-Ming Li ⁎, Cheng-Yang Lai

Institute of Information Management, National Chiao Tung University, Hsinchu 300, Taiwan

## a r t i c l e i n f o

Article history: Received 5 June 2012 Received in revised form 25 November 2013 Accepted 27 November 2013 Available online 4 December 2013

Keywords: Social appraisal support Social network Online purchasing Intuitionistic fuzzy set TOPSIS

## a b s t r a c t

Owing to the plentiful participation of knowledgeable users, an online social network could be seen as a large group of experts that support the decisions of online users. Collective opinions solicited from friends are largely bene<sup>fi</sup>cial for online purchase support and can create signi<sup>fi</sup>cant opportunities for sales. In this paper, a social appraisal mechanism composed using the methodologies of social companionship analysis, collective opinion analysis, and consensus decision analysis is proposed for the online users of the micro-blogosphere. The proposed mechanism can successfully summarize collective opinions and expedite the decision-making process that characterizes users' purchasing behaviors

© 2013 Elsevier B.V. All rights reserved

## 1. Introduction

Social media, such as social networking sites (e.g. Facebook), blogospheres (e.g. Blogspot), and micro-blogospheres (e.g. Twitter and Plurk), have recently been experiencing fast growth. Academics, enterprises, and even individuals are increasingly conducting research and developing business models and applications on social networking sites. A business report by Steegenga and Forge [36] highlights that social media have a greatly increasing in<sup>fl</sup>uence on consumers' online purchase decisions. Over 50% of consumers would access the Internet and their own social network for online shopping decision support. In this investigation, 35% of consumers report that they read reviews and rank products on social media platforms. Additionally, 25% of these consumers believe that it is important to use social networks to assist with their buying decisions. Recently, consumers have promisingly turned to seek shopping advice from their friends through online media [39]. Therefore, it is worthwhile investigating and designing a novel mechanism for supporting consumers' online shopping decision-making.

Social support is generally de<sup>fi</sup>ned as help from others when people are facing a dif<sup>fi</sup>cult life event [5]. That is, social support refers to the assistance available from other people who are part of a social network. In an online shopping scenario, for example, making purchase decisions sometimes constitutes stressful behavior. The stress increases when consumers face a wide range of choices and have insuf<sup>fi</sup>cient information and few resources; seeking social support thus becomes a helpful way to mitigate the problem. However, the mental stress might not decrease but can even increase if the support provided is not what the recipient wished to receive (e.g. time-consuming or irrelevant informa tion, etc.) [11,41].

The micro-blogosphere provides a lightweight and easy form of communication that enables users to share information with their friends about their activities, experiences, opinions, and status [15]. Users' communication in the micro-blogosphere is faster and more frequent than in the blogosphere. The characteristics of micro-blogs are widely discussed by Jansen et al. and Java et al. [14,15]. The limitation of message length in the micro-blogosphere, i.e. that each message should not exceed 140 characters, enables users to write and read messages more easily and ef<sup>fi</sup>ciently. With this lightweight communication and the <sup>fl</sup>ourishing of mobile devices, users are able to request or provide social support conveniently and in a timely manner as well as receive prompt responses. With its superior properties, the microblogosphere is therefore a good social platform on which to seek decision support on online shopping.

In the context of electronic commerce, many sophisticated recommender systems are designed to identify a set of items suitable for and interesting to a user according to his/her personalized preferences, purchase history, past ratings, other similar customers, and so on. Collaborative and content-based are the two main types of recommender systems [40]. For instance, the former, for example the features “Customers Who Bought This Item Also Bought” in Amazon<sup>1</sup> and “See What Other People Are Watching” in eBay,<sup>2</sup> recommends items suitable for the targeted user by collectively analyzing the choices of customers who have similar preferences. The latter, such as the “More Items to Consider” and “Recommendations For You,” on Amazon and eBay, respectively, identi<sup>fi</sup>es items suitable for the current user based on what she/he has viewed. These recommendation systems are mainly developed by online retailers for the purpose of sales improvement. However, customers in the new economy have begun to mistrust of<sup>fi</sup>cial advertising/recommendations [21] and are turning to rely on the opinions and social appraisal support from their close friends. As previous research [12] has noted, social support is one of the important functions of social networks; however, methods for building social support mechanisms on online media have not been widely discussed. From the perspective of customers' interests, it is bene<sup>fi</sup>cial to develop an appropriate appraisal system that can analyze collective opinions to enhance online purchase decision support.

The goal of this research is thus to investigate ways in which to achieve external appraisal support for online purchasing through the micro-blogosphere. Three main research questions are to be studied in this research:

(1) How can the social companionship between the support requester and decision supporters be identified? Because closer friends might understand our preferences, habits, and needs better, their appraisals should be more reliable than those of others. Therefore, the relation closeness between a decision requester and his/her friends plays an important role in the appraisal process.

(2) How can the collective opinions given by decision supporters be analyzed and consolidated? The opinions/appraisals given in a micro-blog are generally short and are likely to be vague. To exploit the wisdom of the crowd from the friend network of a decision requester, the opinions of decision supporters with different friend closeness have to be analyzed semantically and integrated structurally.

(3) How can the decision consensus on the alternative ranking to support online purchasing be obtained? Each support requester has individual preferences regarding the purchase decision criteria. It is thus effective and essential to rank the alternatives appropriately by consensually considering personal preferences and collective external evaluations.

In this research, we propose a social appraisal mechanism (SAM) that integrates the methodologies and techniques of social network analysis (SNA), intuitionistic fuzzy sets (IFSs), and the technique for order preference by similarity to the ideal solution (TOPSIS) to achieve social decision support for online users. Through the proposed mechanism, online users can ef<sup>fi</sup>ciently reduce their decision-making processes and reduce the risk of purchasing an unsuitable product.

The remaining parts of the paper are organized as follows. In Section 2, we discuss the existing literature related to our research topics. In Section 3, we propose the SAM combined with SNA, IFS, and TOPSIS. An empirical experiment is studied in Section 4. Section 5 provides the experiment results and evaluations. Section 6 concludes our research contributions and presents future research directions.

## 2. Literature review

## 2.1. Social support mechanism

Social support is a concept that involves the help provided by other people and the social network as a mediating construct of social support [9]. It provides people with a trusted environment for information exchange with friends. The opinions of the people with close friendships in social networks could be seen as helpful sources of social support, for example, by providing answers to questions. Generally, a social network is expressed as the structural aspect, while social support is investigated from the utilization aspect of a social network [33].

Social support and SNA are mutually reinforcing. They form one of the important functions of social networks [12]. Recently, the utilization of a social network in electronic commerce has mainly focused on information <sup>fi</sup>ltering [24,27,48] and spreading [14,20,46]. Meo et al. [27] propose an approach to recommend resources (e.g. similar users or articles) to a user in the social networking environment. Liu et al. [24] propose a novel hybrid recommendation method that integrates the segmentation-based sequential rule method to consider the sequence of customers' purchase behavior over time. Jansen et al. [14] <sup>fi</sup>nd that the micro-blogosphere is an excellent platform for word-of-mouth communication and discuss how <sup>fi</sup>rms can build word-of-mouth marketing strategies to spread brand information based on social networking and trust. People's behaviors in broadcasting information they would like to share with their friends are explored by Zhao and Rosson [46].

These existing studies mainly aim to <sup>fi</sup>lter or provide information (e.g. <sup>fi</sup>lter unsuitable products and provide the products that users might be interested in) to increase business opportunities. Although a large amount of research has been undertaken on information <sup>fi</sup>ltering and dissemination for increasing business opportunities on the <sup>fi</sup>rm side, few systems have been developed for the social support of users' online shopping behavior. Thus, the aim of the current paper is to develop a SAM for online purchase support.

## 2.2. Companionship and SNA

The provision of social appraisal support is one of the important functions of social companionships. Social companionship is a ubiquitous part of psychological and behavioral functions over time. Recently, SNA has become one of the most important methodologies for estimating tie strength by investigating the complex activities of actors in a social networking environment. According to SNA, a person with more connections (e.g. friendship or interaction) is more important and in<sup>fl</sup>uential than another with fewer connections [44]. Generally, the stronger the tie strength between two actors, the deeper the relationship they have [34]. That is, they might know each other's preferences, habits, and needs.

In practice, the structural dimension (e.g. possessing friend networks [7,35]) and the behavioral dimension (e.g. interaction frequency [20,22]) are two measurement proxies that substitute for tie strength. Granovetter [7] de<sup>fi</sup>nes tie strength as the relative overlap of the neighborhood of two nodes in networks. Shi et al. [35] indicate that communities are composed of various people with strong ties, and social networks are composed of overlapping communities. Li and Du [22] use the frequency of interactions to represent the social tie and measure the relationships between blog readers and authors by analyzing similarity.

When the ties between two persons are stronger, they will be more willing to share opinions with each other openly. Levin and Cross [20] use the interaction effects between knowledge seekers and knowledge sources as one of the important factors to investigate the effectiveness of knowledge transfer. In this research, we use the measurement of social companionship to model the importance level of a social supporter's opinion.

## 2.3. Vague information and multi-criteria decision-making

The opinions received from a person's friend network play an important role in the human decision-making process [17]. However, the opinions expressed by natural language are likely to be vague. As a result, the related decision information (i.e. criteria weights and criteria evaluation of alternatives) might be completely unknown or incompletely known in a decision-making process because of the time pressure, lack of knowledge, and limited expertise of decision supporters regarding the problem domain [4]. Recently, IFSs have been found to be highly useful in dealing with vagueness on the semantic web [10,20]. Conceptually, an IFS, which has feasible presentation for the degree of membership, degree of non-membership, and degree of uncertainty [2], is very well suited to modeling the fuzziness and uncertainty of opinions used in social appraisal support. In order to handle the issue of vague information gathered from social networks and deal with multi-criteria fuzzy decision-making problems, an IFS could be applied to represent the characteristic criteria values of alternatives by fuzzy numbers [25,45].

The multi-criteria decision-making technique is commonly applied to identify the compromised or optimal solution from all the feasible alternatives evaluated according to multiple criteria [19,23]. It has been particularly in<sup>fl</sup>uential in contributing insights into the domain of decision-making. This technique simpli<sup>fi</sup>es the complex human decision-making process into the quanti<sup>fi</sup>ed distance using relative closeness coef<sup>fi</sup>cient measurements. TOPSIS is an appropriate tool for resolving multiple-attribute decision-making problems [13]. The concept of TOPSIS is to select an alternative that is closer to the positive ideal solution and farther from the negative ideal solution simultaneously. In the proposed SAM, IFS and TOPSIS are incorporated to consolidate the collective opinion and generate consensus decision analysis with complex and unintelligible information from social networks.

## 3. The system framework

Micro-blogging has become an important platform for seeking knowledge and expertise [15,46]. One can utilize one's social network as an expert knowledge base for facilitating the decision-making process. In addition, with the advantage of the real-time nature of micro-blogs, users can collect a huge number of opinions from their social networks in a short time. In this section, we propose a social appraisal framework to support a user's online purchase decisions in the micro-blogosphere.

To implement the proposed mechanism, we develop an application on the Plurk platform, utilizing the available of<sup>fi</sup>cial APIs. The developed Plurk application is a software agent, named AppPlurk, which will automatically reply information to a request according to the message it receives. To use this agent, users can simply add it as one of his/her friends and initiate an appraisal request in a speci<sup>fi</sup>c message format to activate the mechanism. A user who is making a purchase choice from a list of alternative products, which were previously surveyed by the user or recommended by retailers can send an appraisal request to AppPlurk for decision support.

The procedures for a user to solicit decision support from his/her friend network in the context of online purchasing are shown in Fig. 1 and detailed as follows.

(1) The support requester initiates a request message with a list of product alternatives. For example, the message is described as “[DC]: [Camera 1, Camera 2, Camera 3],” where DC denotes “Digital Camera.”

(2) The agent would automatically reply to the related decision criteria by seeking suggestions from his/her friends (decision supporters) in the micro-blogosphere according to the product category. For example, the message is described as “[Criteria]: [Resolution, Price, Lens].”

(3) The support requester could set the personal criteria importance rating according to the criteria obtained in step 2. For example, the message i described as “[Weighting]: [3,1,2].” The group weighting would be used if the support requester did not provide a criteria importance rating.

(4) Those friends who receive the request message and reply opinions (including criteria evaluations and importance ratings) become decision supporters. For example, the message is described as “[ans]: [Good, Bad, Unknown], [Unknown, Good, Good], [Bad, Good, Bad], [1,3,2].”

(5) The agent responds to the result of the decision analysis. The received feedback is consolidated by the proposed mechanism to rank the product candidates. For example, the message is described as “[Rank]: [Camera 2 N Camera 1 N Camera 3].”

![](/api/attachments/3T2S3BK9/fulltext/images/f5c1d5b6b1450d7b3e40f1be0ec10dc70dfec7116df4c14049607dd2930996bb.jpg)  
Fig. 1. Processes of the social appraisal mechanism.

![](/api/attachments/3T2S3BK9/fulltext/images/60f3c1c2e5fa779b25c09eb7e96d967f7f5b431c4fa4bf12307a4ccef439c19d.jpg)  
Fig. 2. The framework of the social appraisal mechanism.

Fig. 2 depicts the framework of our system model. The proposed model comprises three main components: the social companionship analysis module, collective opinion analysis module, and consensus decision analysis module:

(1) Social companionship analysis module: the purpose of social companionship analysis is to identify the importance degree of a decision supporter based on the companionship between the support requester and decision supporter. We consider social factors in both the behavioral and the structural dimension to derive social companionship.

(2) Collective opinion analysis module: the aim of collective opinion analysis is to discover the criteria and evaluations from the opinions of decisio supporters. The responses of decision supporters are transformed into a collective decision matrix, which is expressed by intuitionistic fuzzy values to represent the uncertainty and incompleteness of collective criteria evaluations.

(3) Consensus decision analysis module: the objective of consensus decision analysis is to consolidate the collective opinions to generate a list of ranked alternatives. By combining the personal preference criteria of the support requester and collective evaluations of decision supporters, the TOPSIS method is utilized to rank all alternatives by evaluating the distance of an alternative relative to an ideal choice.

## 3.1. Social companionship analysis

Onnela et al. [34] point out that two social actors have a deeper relation if there are strong ties between them. That is, they might know each other's preferences and real needs. Therefore, the goal of social companionship analysis is to estimate the tie strength between the support requester and supporters in order to represent the social companionship degree.

Tie strength determination could be simply separated into the behavioral dimension (e.g. interaction frequency [20,22]) and the structural dimension (e.g. possession of a friend network [7,35]). We analyze the interaction network and friend network in the micro-blogosphere to measure the tie strengths of these two dimensions, respectively. According to these, we can measure the decision support's relevance and closeness to the support requester.

## 3.1.1. Behavioral tie analysis

Granovetter [7] describes social interaction tie strength as a combination of the amount of time, the emotional intensity, the intimacy (mutual con<sup>fi</sup>ding), and the reciprocal services that characterize the tie. In this study, social interaction tie strength measured by the interaction frequenc in a time period is used to represent the social companionship degree of the members of the micro-blogosphere.

Two-mode network data could be de<sup>fi</sup>ned as two sets of social units and they contain relation measurements from the elements of one social unit set to the elements of another social unit set [44]. For instance, in this study, the social network of users that interact with micro-blogging messages is a kind of a two-mode network that includes two social unit sets, namely a set of users and a set of micro-blogging messages, and the relations tha re<sup>fl</sup>ect the social interactions. The two-mode network in the context of the micro-blogosphere is depicted in Fig. 3-(a). The user set is a set of users who interact with the support requester. The set of micro-blogging messages is a pool of messages posted by the members of the user set. A relation is established by posting or replying to a message. A two-mode network can be represented as a bipartite graph $G = ( M \cup U , I )$ , where M and U indicate the message set and the user set, respectively, and I stands for the set of interaction relations between M and U.

![](/api/attachments/3T2S3BK9/fulltext/images/51204180b64cf64a9b72dcdcb517a8ac4fca9b94f9aff83bf72397933a2e837e.jpg)  
a) Bipartite graph of the micro-blogosphere

![](/api/attachments/3T2S3BK9/fulltext/images/e8b83974618801007f2569f536f31985a8d1b292069d4f2129b145987ced40be.jpg)  
b) User interaction network  
Fig. 3. Two-mode network of the micro-blogosphere.

After constructing the two-mode network of the micro-blogosphere, we then compress it into a user-projection network (named the user inter action network). The compressed network describes the social interactions between the support requester and decision supporters and this can be used to obtain behavioral tie strength based on the interaction frequency between the requester and each decision supporter. Fig. 3-(b) depicts the interaction network of the bipartite graph, in which the value attached to an edge between two nodes in set U represents the total number of messages in set M associated with these two nodes. That is, the relation values of users are measured by counting the micro-blogging messages in which the users have commonly interacted, and vice versa. For example, in Fig. 3-(b), there is an edge between $U _ { 1 }$ and $U _ { 2 }$ and the relation value is marked by 1 because they have commonly participated in only one micro-blogging message $M _ { 1 }$ in Fig. 3-(a). Similarly, the relation value between $U _ { 1 }$ and $U _ { 3 }$ is 2 as they interacted via messages $M _ { 1 }$ and $M _ { 5 }$

Before being combined with structural tie strength, behavioral tie strength should be normalized. The normalized behavioral tie strength value between a decision supporter i and the support requester is formulated as

$$
B T _ {i (n o r m a l i z e d)} = \frac {B T _ {i} - B T _ {\min}}{B T _ {\max} - B T _ {\min}},\tag{1}
$$

where $B T _ { \mathrm { m i n } }$ and $B T _ { \mathrm { m a x } }$ indicate the weakest and strongest behavioral tie strengths from all decision supporters to the support requester, respectively.

## 3.1.2. Structural tie analysis

In order to determine structural tie strength, the friend network <sup>fi</sup>rst has to be extracted based on the friend list in the blogosphere. Then, we can determine structural tie strength from the friend network. Onnela et al. [34] use the aggregated duration of communications between two social unit within a time period as the tie strength, utilizing a communication network data set. They indicate that there is a stronger tie between two social units if most of their friends overlap. In this research, we use the following formula to estimate structural tie strength [47]:

$$
S T _ {i j} = \frac {n _ {i j}}{(d _ {i} - 1) + (d _ {j} - 1) - n _ {i j}},\tag{2}
$$

where $n _ { i j }$ is the number of common acquaintances of social units i and j. d and $d _ { j }$ are the degrees of social unit i and j, respectively. In this paper, we de<sup>fi</sup>ne $S T _ { i j }$ as the structural tie strength between decision supporter i and support requester j.

Note that Onnela et al. [34] apply in-degree centrality in the above formula to discover the weak ties for information diffusion. However, according to Kiss and Bichler [18], out-degree centrality performs better in in<sup>fl</sup>uencer identi<sup>fi</sup>cation. An information seeker on online media follows other users' information regularly, including daily chat from friends and information from professionals [15]. Therefore, a person with a higher out-degree (mak ing friends with many other users) could simply infer that he/she might be an information seeker so that he/she could give helpful product appraisal according to preferences, habits, and needs from the daily chat information observed from other professionals. Therefore, in our research, we use out degree centrality to measure tie strength. The out-degree centrality of node i is de<sup>fi</sup>ned as

$$
d _ {i} = \sum_ {j = 1} ^ {n} f _ {i j}\tag{3}
$$

where $f _ { i j }$ is 1, while the edge from node i to node j exists in a relation matrix, otherwise it is 0.

After obtaining behavioral and structural tie strengths, the social companionship degree $( S C _ { \alpha } )$ of decision supporter α is measured as $S C _ { \alpha } =$ $B T _ { \alpha j } \times S T _ { \alpha j } .$ Finally, the obtained social companionship can be further normalized as

$$
\lambda_ {\alpha} = \frac {S C _ {\alpha}}{\sum_ {i \in \Theta_ {s}} S C _ {i}},\tag{4}
$$

![](/api/attachments/3T2S3BK9/fulltext/images/07750fc6cf229a50f5cc81abd2858af50e03c18d11076b8cad325bc87407bc1a.jpg)  
Fig. 4. Collective opinion analysis module

where $\theta _ { S }$ denotes the set of decision supporters included in the user set, $S C _ { \alpha }$ denotes the relation measurement value of the decision supporter α, and $\lambda _ { \alpha }$ denotes the importance weight of the decision supporter α. Decision supporters with a greater social companionship degree will be allocated greater importance weight during the decision process support and their opinions are more trusted by the support requester.

## 3.2. Collective opinion analysis

Constructing the decision criteria, evaluating the alternatives, and making a decision are the three sequential routines of the decision-making phase [30]. The aim of the collective opinion analysis module is to deal with criteria extraction and alternative evaluation to construct the collective decision matrix. Generally speaking, differentiated by the process of product information acquirement for product evaluation prior to purchasing, products can be categorized into search goods (e.g. consumer electronics, etc.) and experience goods (e.g. restaurants, movies, and peripheral products, etc.) [31]. In this section, we <sup>fi</sup>rst describe the basic concept of collective opinion analysis for search goods and then extend the module to experience goods by adding semantics analysis.

## 3.2.1. Criteria and evaluation extraction

3.2.1.1. Basic model for search goods. In economics, search goods are products or services with features and characteristics easily evaluated befor purchase [31]. For search goods, the procedures involved in this module are depicted in Fig. 4.

3.2.1.1.1. Criteria extraction. For constructing the decision criteria, they can be extracted from public and impartial third parties and automatically reply to the request message while the originator initiates appraisal request. Then, decision supporters give their criteria evaluation according to the explicit criteria.

3.2.1.1.2. Evaluation extraction. Decision supporters can directly evaluate the alternatives according to each criterion by answering “G,” “B,” or “U,” which represent “good,” “bad,” or “unknown,” respectively, to evaluate each criterion. However, this approach cannot be applied directly to experi ence goods as their product characteristics and evaluation criteria are implicit or not described.

3.2.1.2. Extended model for experience goods. In economics, experience goods are contrasted with search goods [31], which means that their features and characteristics cannot be evaluated before purchase. The collective opinion analysis module is extended to deal with experience goods. We design a lightweight criteria construction and evaluation mechanism by using the semantic analysis of micro-blog messages. The procedures involved in this extended module are depicted in Fig. 5. Micro-blogospheres are platforms with message length-limited communication. Users usually write short sentences with a simple sentence structure [26,38]. In the current paper, we use semantic analysis to extract the criteria and evaluation from micro-blog messages, After a decision supporter posts an opinion, we first utilize the NLProcessor linguistic parser, a text analysis toolkit [32], to parse the sentences and yield the part-of-speech tag of each word (whether the word is a noun, verb, adjective, etc.). For each sentence in an opinion, nouns are extracted as one of the criteria and the nearby adjectives are identi<sup>fi</sup>ed as the criteria evaluation. In order to identify the semantic orientation of criteria evaluation posted by a decision supporter, a lexical database is required. In this research, WordNet [28,29] is applied as the lexical database. Over time, WordNet has successfully evolved to become widely used as one of the important lexical resources for natural language processing sys tems. It enables users to access lexical information in a much faster and more convenient way [1]. Finally, the extracted criteria and evaluations are then used to construct a collective decision matrix.

3.2.1.2.1. Criteria extraction. After the NLProcessor linguistic parser has parsed the opinions posted by decision supporters, the part-of-speech tag of each word is tagged. The noun and noun phrase followed by adjectives are extracted as one of the criteria. In order to reduce the criteria set, we construct synonym matching between the criterion and each previously extracted criterion contained in the criteria set established on WordNet. The criterion is not added to the criteria set if it matches a synonym in the criteria set.

![](/api/attachments/3T2S3BK9/fulltext/images/fd5a155c1fc9992d7391951c5421d587ed858b285e7183041fbbfbde76c0072a.jpg)  
Fig. 5. Collective opinion analysis module.

3.2.1.2.2. Evaluation extraction. Typically and intuitively, adjectives have been indicated as useful indicators of sentiment [1]. The semantic ori entation of adjectives is identi<sup>fi</sup>ed as the evaluation of criteria. Owing to the length limitation of a post (140 words per post) within the micro blogosphere, an opinion has to be concise rather than lengthy. In addition, the aim of the proposed mechanism is to ascertain whether a decision supporter gives positive or negative evaluations for criteria to support the decision-making of the originator. Therefore, we focus on identifying the semantic orientation of short text messages. In this research, the semantic orientation (positive, negative, or vague orientation) of an adjective is identi<sup>fi</sup>ed as criteria evaluation. In the proposed method, the orientation identi<sup>fi</sup>cation begins with building an undirected synonymous adjec tive graph, $G _ { a } = ( A , E )$ , and we add edges (E) between the seed word and non-duplicate synonyms $( a _ { i } \in A )$ to represent the synonymous rela tionship. As suggested by Turney and Littman [42], we use a seed word set of adjectives that de<sup>fi</sup>nes a subjective positive and negative word set with 14 words.

Positive: good, nice, excellent, positive, fortunate, correct, superior

Negative: bad, nasty, poor, negative, unfortunate, wrong, inferior

This word set is used to search non-duplicate synonyms from WordNet in order to expand the synonymous adjective graph for identifying seman tic orientation. The semantic orientation of an adjective can be measured by comparing the length of the shortest paths from this adjective to the selected polar positive adjective and from this adjective to the selected polar negative adjective [16]. Denote PP as the positive polar adjective and NP as the negative polar adjective. SP is the length of the shortest path between the adjective used by the decision supporter $( D S _ { a d j } )$ and the polar adjective within the synonymous adjective graph $G _ { a } .$ The tendency of the semantic orientation of an adjective SO is formulated as

$$
S O \left(D S _ {a d j}\right) = S P \left(D S _ {a d j}, P P\right) - S P \left(D S _ {a d j}, N P\right).\tag{5}
$$

According to the quanti<sup>fi</sup>ed semantic orientation, we can judge that

$$
D S _ {a d j} \text {   has   } \left\{ \begin{array}{l} \text { positive   orientation   (G)   if   SO <   0 }, \\ \text { negative   orientation   (B)   if   SO > 0 }, \\ \text { vague   orientation   (U)   if   SO = 0 }. \end{array} \right.\tag{6}
$$

Note that if there is “no” or “not” in front of an adjective in the sentence, the identi<sup>fi</sup>ed orientation would be reversed, except the vague orientation.

The following example demonstrates the semantic orientation identi<sup>fi</sup>cation process. Suppose that the expanded synonymous adjective graph is structured as shown in Fig. 6. If a decision supporter gives an adjective “fat” in his/her opinion, we can derive $S P ( " f a t " , P P ) = 2 , S P ( " f a t " , N P ) = 1$ , and $S O = 2 - 1 = 1$ . Because “fat” is far away from $P P$ (two steps) and closer to NP (one step), the semantic orientation of “fat” $( S O > 0 )$ would be identi<sup>fi</sup>ed as a negative orientation (B).

## 3.2.2. Decision matrix construction

We can obtain the collective decision matrix according to the evaluations submitted by decision supporters. Suppose that the decision-making originator releases m alternatives (A) and n criteria (C) and there are k decision supporters who have evaluated each alternative with respect to the criteria given by the support requestor. According to Section 3.2.1, the evaluation of whether an alternative $A _ { i }$ satis<sup>fi</sup>es a criterion $C _ { j }$ can be expressed as (1) “good/positive orientation $\left( \mathbf { G } \right) , ^ { \mathfrak { n } } \left( 2 \right)$ “bad/negative orientation (B),” or (3) “unknown/vague orientation (U).” Denote $d _ { i j } ^ { l }$ as decision supporter l's evaluation of alternative $A _ { i }$ with respect to the criterion $C _ { j } .$ k decision matrixes are collected:

$$
D ^ {\alpha} = \left[ d _ {i j} ^ {\alpha} \right] _ {m \times n}, \text { where } d _ {i j} ^ {\alpha} \in \{G, B, U \}, \alpha \in \{1, \dots , k \}, i \in \{1, \dots , m \}, j \in \{1, \dots , n \}.\tag{7}
$$

As the criteria evaluation may diverge among different decision supporters, we apply the IFS technique to quantify the collective opinions. IFSs were introduced by Atanassov [2] as an extension of classical fuzzy set theory. They represent a suitable way to deal with the problem of information vagueness. An IFS A in a <sup>fi</sup>nite set X is de<sup>fi</sup>ned by the following form:

$$
A = \left\{<   x, \mu_ {A} (x), v _ {A} (x) > | x \in X \right\}, \text { where } \mu_ {A}: X \rightarrow [ 0, 1 ], v _ {A}: X \rightarrow [ 0, 1 ].\tag{8}
$$

![](/api/attachments/3T2S3BK9/fulltext/images/690fe42dbe566130de26484f6c23023af961061773267a187c3fcb4e75531f72.jpg)  
Fig. 6. Semantic orientation identi<sup>fi</sup>cation.

The values of $\dot { \mu } _ { A } ( x )$ and $\nu _ { A } ( { \boldsymbol { x } } )$ denote the degree of membership of x in A and the degree of non-membership of x in A, respectively ${ . \mu _ { A } ( x ) }$ and $v _ { A } ( x )$ satisfy the following condition:

$$
0 \leq \mu_ {A} (x) + v _ {A} (x) \leq 1, \forall x \in X.\tag{9}
$$

Note that a fuzzy set could be viewed as a special case of an IFS. An IFS A will become a crisp set if for $\forall x \in X ,$ , either $\mu _ { A } = 0 , \nu _ { A } = 1 \mathrm { o r } \mu _ { A } = 1$ $\nu _ { A } = 0 .$ . According to [2], we use the following de<sup>fi</sup>nition as the intuitionistic index of x in A. It is a general measurement of the hesitancy degree of x to A:

$$
\pi_ {A} (x) = 1 - \mu_ {A} (x) - \nu_ {A} (x),\tag{10}
$$

where $0 \leq \pi _ { A } ( x ) \leq 1$ for each $x \in X , \mathsf { A }$ smaller value of $\pi _ { A } ( { \boldsymbol { x } } )$ means that the knowledge about x is more certain. On the contrary, the knowledge about x is more uncertain if the value of $\pi _ { A } ( { \boldsymbol { x } } )$ becomes greater.

Denote $G _ { i j }$ and $B _ { i j }$ as the set of decision supporters who respond with “good” and “bad” to alternative $A _ { i }$ regarding criterion $C _ { j } ,$ respectively. A decision supporter $\alpha \in G _ { i j } \operatorname { i f } d _ { i j } ^ { \alpha } = G$ and $\alpha \in B _ { i j } \operatorname { i f } d _ { i j } ^ { \alpha } = B .$ The collected evaluations are transformed into a collective decision matrix expressed in the form of intuitionistic fuzzy values. That is, each element of the collective decision matrix denotes the opinion of the majority and therefore it comprises the membership, non-membership, and indeterminacy of a fuzzy concept “excellence." The collective decision matrix can be expressed as

$$
C D = \left[ c d _ {i j} \right] _ {m \times n},\tag{11}
$$

in which the characteristics of alternatives $c d _ { i j }$ are represented as

$$
c d _ {i j} = \left\{\left. <   \mu_ {A _ {i}} (C _ {j}), v _ {A _ {i}} (C _ {j}) > \mid C _ {j} \in C \right\}, i \in \{1, \dots , m \}, j \in \{1, \dots , n \}. \right.\tag{12}
$$

where $\mu _ { A _ { i } } \left( C _ { j } \right)$ and $\nu _ { A _ { i } } \left( C _ { j } \right)$ indicate the degree to which alternative $A _ { i }$ satis<sup>fi</sup>es and does not satisfy criterion $C _ { j } ,$ , respectively, and these are formulated as

$$
\mu_ {A _ {i}} \left(C _ {j}\right) = \sum_ {\alpha \in G _ {i j}} \lambda_ {\alpha} \text { and } v _ {A _ {i}} \left(C _ {j}\right) = \sum_ {\alpha \in B _ {i j}} \lambda_ {\alpha}.\tag{13}
$$

Note that the third intuitionistic index $\pi _ { A _ { i } } ( C _ { j } ) = 1 - \mu _ { A _ { i } } ( C _ { j } ) - \nu _ { A _ { i } } ( C _ { j } )$ is used to evaluate the collective level of hesitation in criterion $C _ { j } .$ Speci<sup>fi</sup>- cally, a larger value of $\pi _ { A _ { i } } ( C _ { j } )$ <sup>¼</sup>indicates a higher hesitation margin of decision supporters regarding alternative $A _ { i }$ with respect to criterion $C _ { j } .$

## 3.3. Consensus decision analysis

After the intuitionistic fuzzy decision matrix has been obtained, consensus decision analysis is conducted to analyze the collective evaluations and provide the ranking list of alternatives for supporting the decision-making originator. In this research, TOPSIS is utilized to consolidate the evaluations from decision supporters. The procedures of TOPSIS calculation for consensus decision analysis are described as follows:

## Step 1 Obtain the criteria weight set.

In the decision analysis process, the support requester might have different criteria importance preferences for the alternative evaluation. The support requester could give his/her criteria weight set (w). If the support requester does not set his/her criteria weight, we simply use the default group weighting.

The criteria importance of group weighting is formulated as follows:

$$
w _ {C _ {j}} = \frac {\sum_ {i = 1} ^ {n} R _ {C _ {j}} ^ {D S _ {i}}}{\sum_ {j = 1} ^ {n} \sum_ {i = 1} ^ {n} R _ {C _ {j}} ^ {D S _ {i}}},
$$

where $w _ { C _ { i } }$ indicates the criteria importance of the group suggestion of criteria j and $R _ { C _ { j } } ^ { D S _ { i } }$ is the importance rating of criteria j given by decision supporter i. For each $c d _ { i j } \in \mathrm { I F S } , c d _ { i j \_ W _ { C _ { i } } }$ is de<sup>fi</sup>ned as follows [6]:

$$
c d _ {i j \_} w _ {C _ {j}} = \left\{<   1 - \left(1 - \mu_ {A _ {i}} (C _ {j})\right) ^ {w _ {C _ {j}}}, \left(v _ {A _ {i}} (C _ {j})\right) ^ {w _ {C _ {j}}} > \right\}.\tag{14}
$$

After including the weight, the new weighted matrix is generated for consensus decision analysis.

Step 2 Determine the intuitionistic fuzzy positive ideal solution (IFPIS) and the intuitionistic fuzzy negative ideal solution (IFNIS).

The calculations of the IFPIS $( A ^ { + } )$ and IFNIS $( A ^ { - } )$ in this step are respectively de<sup>fi</sup>ned as follows:

$$
A ^ {+} = \left\{\max _ {i} \bar {\mu} _ {A _ {i}} (C _ {j}), \min _ {i} \bar {\nu} _ {A _ {i}} (C _ {j}) \right\} \text {   and   } A ^ {-} = \left\{\min _ {i} \bar {\mu} _ {A _ {i}} (C _ {j}), \max _ {i} \bar {\nu} _ {A _ {i}} (C _ {j}) \right\}\tag{15}
$$

$$
\overline {{\mu}} _ {A _ {i}} \left(C _ {j}\right) = 1 - \left(1 - \mu_ {A _ {i}} \left(C _ {j}\right)\right) ^ {w _ {C _ {j}}}, \overline {{v}} _ {A _ {i}} \left(C _ {j}\right) = \left(v _ {A _ {i}} \left(C _ {j}\right)\right) ^ {w _ {C _ {j}}}\tag{16}
$$

Step 3 Calculate the distance between the alternative and the IFPIS and between the alternative and the IFNIS

The following measurement de<sup>fi</sup>nitions [37] were used to determine the Euclidean distance. $\mathrm { E D } ( A _ { i } , A ^ { + } )$ and $\mathrm { E D } ( A _ { i } , A ^ { - } )$ respectively denote the Euclidean distance between alternative $A _ { i }$ and IFPIS $A ^ { + }$ and between alternative $A _ { i }$ and IFPIS A<sup>−</sup>:

$$
\operatorname{ED} \left(A _ {i}, A ^ {+}\right) = \sqrt {\sum_ {j = 1} ^ {n} \left[ \left(\bar {\mu} _ {A _ {i}} \left(C _ {j}\right) - \mu_ {A ^ {+}} \left(C _ {j}\right)\right) ^ {2} + \left(\bar {\nu} _ {A _ {i}} \left(C _ {j}\right) - \nu_ {A ^ {+}} \left(C _ {j}\right)\right) ^ {2} + \left(\bar {\pi} _ {A _ {i}} \left(C _ {j}\right) - \pi_ {A ^ {+}} \left(C _ {j}\right)\right) ^ {2} \right]};\tag{17}
$$

$$
\mathrm{ED} (A _ {i}, A ^ {-}) = \sqrt {\sum_ {j = 1} ^ {m} \left[ \left(\bar {\mu} _ {A _ {i}} (C _ {j}) - \mu_ {A ^ {-}} (C _ {j})\right) ^ {2} + \left(\bar {\nu} _ {A _ {i}} (C _ {j}) - \nu_ {A ^ {-}} (C _ {j})\right) ^ {2} + \left(\bar {\pi} _ {A _ {i}} (C _ {j}) - \pi_ {A ^ {-}} (C _ {j})\right) ^ {2} \right]}.\tag{18}
$$

Step 4 Calculate the relative closeness coefficient (CC) and rank the preference order of all the alternatives.

The relative CC of each alternative with respect to the intuitionistic fuzzy ideal solutions is calculated as

$$
C C _ {A _ {i}} = \frac {\operatorname{ED} (A _ {i} , A ^ {-})}{\operatorname{ED} (A _ {i} , A ^ {+}) + \operatorname{ED} (A _ {i} , A ^ {-})}, \text {   where   } C C _ {A _ {i}} \in [ 0, 1 ], i = \{1, 2,..., m \}.\tag{19}
$$

A greater CC value indicates that the alternative is simultaneously closer to IFPIS and farther from IFNIS. Hence, the ranking list of all alternatives can be determined according to the descending order of CC values. Finally, the alternative with the highest ranking is the most preferred.

## 4. Experiments

## 4.1. Experiment source

In order to evaluate the proposed social appraisal support mechanism, we construct experiments on both search goods and experience goods in the Plurk<sup>3</sup> micro-blogosphere. According to the report from InRev Inc. [3], the Plurk micro-blogosphere is popular in Taiwan, the Philippines, Indonesia, and the United States. Based on the statistics of May 18, 2010, almost 50% of Plurk users are teenagers and 30% of users are aged 20–30. Because Plurk is predominantly used by youths and young adults for information sharing, we believe that it is an excellent platform for soliciting social appraisal support when users face a purchase decision.

## 4.1.1. Construction of the friend network

In the experiments, 113 active Plurk users are invited to be support requesters. All these quali<sup>fi</sup>ed support requesters have undertaken at least one purchasing activity in the past three months. In addition, to ensure that a support requester has suf<sup>fi</sup>cient time to evaluate the satisfaction degree of the purchased product, the latest purchase decision of a support requester should have been more than one week ago. We construct the friend network as initiated and expanded from these support requesters. Data descriptions of the experiments are outlined in Table 1.

In the experiments, 161 purchase decisions (88 for search goods and 73 for experience goods) are evaluated. A typical decision support request contains 3–5 alternatives and on average 16 friends (decision supporters) reply to a request with their opinions. For analyzing the companionships of decision supporters who respond, we collected the post and response activity records in the past six months from participants' public Plurk interfaces.

## 4.1.2. Construction of the decision criteria

Four kinds of search goods, namely “digital camera,” “computer,” “MP3 player,” and “cell phone,” and three kinds of experience goods, namely “restaurant,” “movie,” and “peripheral products,” are analyzed in the experiments. Note that “peripheral products” mainly refers to the peripheral products of mobile devices (e.g. cases, headsets for tablets or smartphones, etc.). As the features and characteristics of search goods can be explicitly evaluated by customers before purchasing, we pre-collect product features as the appraisal criteria from the buying guide of the CNET<sup>4</sup> product review site. The pre-collected product categories and features of search goods are listed in Table 2. Participants were asked to initiate a request for decision support and disseminate it over their own social networks on the Plurk platform. For experience goods, we use the semantic analysis of micro-blog messages to extract the implicit decision criteria, as described in Section 3.2.1.

Table 1  
Data descriptions of the experiment.

<table><tr><td colspan="2">Statistics of the experiment data</td></tr><tr><td>Number of invited participants</td><td>113</td></tr><tr><td>Number of available social appraisal requests</td><td>161</td></tr><tr><td>Average number of decision supporters per social appraisal request</td><td>16</td></tr><tr><td>Average number of friends per participant</td><td>83</td></tr><tr><td>Average number of interactions per participant (6 months)</td><td>2967</td></tr><tr><td>Average number of requests released per participants</td><td>1.6</td></tr><tr><td>Average number of alternatives per social appraisal request</td><td>4.2</td></tr></table>

## 4.1.3. Construction of the adjective word graph

Fig. 7 depicts the evolving process of the word set expansion. We can observe that the expansion of the word set is marginally diminishing from Fig. 7-(a). Altogether 1127 non-duplicate adjectives are included in the word set used for synonymous adjective graph building. In Fig. 7-(b–c), an example of the two-level synonymous adjective expansion of the adjective “good” is shown. The word “good” has synonymies of “full,” “estimable,” “bene<sup>fi</sup>cial,” and so on in the <sup>fi</sup>rst-level expansion according to WordNet. These extracted synonymies are used as the seed words for further extracting the second-level synonymies of “good” in the second-level expansion, and so on. The <sup>fi</sup>nal expanded synonymous adjective graph is shown in Fig. 7-(d).

## 4.1.4. Selection of the polar adjectives

As explained in Section 3.2.1, the semantic orientation of an adjective is calculated by the comparison of the shortest paths between this adjective and the positive polar adjective and between this adjective and the negative polar adjective. In this research, we use 27 words (19 words of high popularity and eight words of low popularity) selected from the list of adjective words used by Vegnaduzzo [43] to evaluate whether the orientation identi<sup>fi</sup>cation mechanism could deal with the user's daily used adjectives. These words are included in the synonymous adjective graph created as the evaluation word set. These 27 words are sequentially fed into the proposed evaluation extraction process to estimate the semantic orientation identi<sup>fi</sup>cation accuracy. However, these words are without orientation or polarity information. A group of 10 human judges (consisting of two doctoral students and eight master's students) was invited to pre-identify the semantic orientation (positive or negative) using the majority voting method. If an adjective were identi<sup>fi</sup>ed as having a positive orientation and a negative orientation with an equal number of votes, it was marked as a vague orientation.

We experimented with various polar pairs such as (good, bad), (positive, negative), and (excellent, poor) to study the impact on the accuracy of semantic orientation identi<sup>fi</sup>cation. The experimental results and two-paired sample t-test at the 95% signi<sup>fi</sup>cance level are respectively shown in Fig. 8. As we can observe, the accuracy rate of adjective semantic orientation identi<sup>fi</sup>cation using the polar pair of (good, bad) is significantly higher than that of other pairs. Hence, it is used for the semantic orientation identi<sup>fi</sup>cation process in the experiments.

## 4.2. Experiment design

In the experiments, we asked participants to recall their original decision-making processes and report (1) the product they bought and the alternatives they took into account, (2) the criteria they considered, and (3) whether the product purchase decision was satisfactory.

First, we have to know which product they bought because different products have different criteria for decision-making. The alternatives together with the suitable criteria set were sent to their friends through Plurk. A friend becomes a decision supporter when he/she replies to the message with his/her criteria evaluation.

Second, although we pre-collected a general criteria set (i.e. product features) of products, in order to make the criteria set closer to participants' considerations, the collective criteria for each product were additionally collected from participants. For search goods, the system would respond to the pre-collected criteria set (as shown in Table 2) according to the product category mentioned in the social appraisal request. Decision supporters could give their evaluation (“G,” “B,” or “U”) to each criterion of the alternatives. For experience goods, the system analyzes the opinions posted by decision supporters to extract possible criteria and evaluations.

Table 2  
Features of products in different categories.

<table><tr><td>Digital camera</td><td>Computer</td><td>MP3 player</td><td>Cell phone</td></tr><tr><td>Resolution</td><td>Processor</td><td>PC interface</td><td>Cellular tech.</td></tr><tr><td>Price</td><td>Memory</td><td>Flash memory</td><td>Specific absorption rate</td></tr><tr><td>Lens</td><td>Video graphic</td><td>Dimension</td><td>Band/mode</td></tr><tr><td>Storage</td><td>Size of case</td><td>Weight</td><td>Wireless interface</td></tr><tr><td>Interfaces</td><td>Storage</td><td>Resolution</td><td>Weight</td></tr><tr><td>Exposure controls</td><td>Warranty</td><td>Battery tech.</td><td>Memory</td></tr><tr><td>Focus controls</td><td>Network</td><td>Battery life</td><td>Battery life</td></tr><tr><td>Flash modes</td><td>Audio</td><td></td><td></td></tr></table>

Third, after gathering the evaluation and building the collective decision matrix, the proposed SAM provides a ranking list of all the alternatives to support the originator's decision-making on product purchasing. In order to evaluate the ef<sup>fi</sup>ciency of the proposed social appraisal support mechanism, it is necessary to know whether participants are satis<sup>fi</sup>ed with their product purchase decisions. In our mechanism evaluation process, the item ranked in <sup>fi</sup>rst place is selected as the purchasing target and used to evaluate the effectiveness of the proposed mechanism.

We illustrate the system process with the following example. User A wants to buy a camera. According to self-survey or other recommendations, he/she has narrowed the choice to three camera alternatives but it is hard to decide which one is most suitable. He/she initiates a support request in the micro-blogosphere. The request message is formed as “[Digital camera]: [camera1, camera2, camera3].” The extracted criteria set for the digital camera would be posted in the form of “[Criteria]: [resolution, price, lens, storage, interfaces, exposure controls, focus controls, <sup>fl</sup>ash modes].” Then, decision supporters (the friends of A) reply with their criteria evaluations of each alternative in the following form “[ans]: [G, B, U, G, G, B, U, G], [U, G, G, B, B, B, U, G], [G, G, G, G, U, G, G, B], [1,3,8,4,2,7,5,6].” After the consensus decision analysis, the system produces a list of ranked cameras for A in the form of “[Rank]: [camera2 N camera3 N camera1],” which indicates that A's friends think that “camera2” is the most suitable camera.

Another example considers experience goods. User B initiates a support request for restaurant selection as “[Restaurant]: [restaurant1, restaurant2, restaurant3]. For a family dinner, which one is the best?” Suppose that friend1 gives his opinion as “[ans]: [the service is great and the food is delicious but the price is expensive], [the distance is too far but food and service are good].” After collective opinion analysis, the system respectively transforms the sentences into the criteria set as “[Criteria]: [service, food, price, distance]” and the criteria evaluation as “[ans]: [G, G, B, U], [U, G, U, B], [U, U, U, U]” for these three restaurants and feeds these into the consensus decision analysis. Note that the system would post the current criteria set to the support request message and allow other friends to give their opinions according to these criteria. Then, if friend2 mentioned other features of the restaurants, such as “[ans]: [the service is great but I do not like their food and the price is a little bit expensive, distance is ok to me], [service and food are great], [very nice background music],” the criteria set would be expanded automatically as “[Criteria]: [service, food, price, distance, music]” and the evaluation of the criterion “music” of friend1 would be set as “U” and the evaluations updated as “[ans]: [G, G, B, U, U], [U, G, U, B, U], [U, U, U, U, U]” for consensus decision analysis. Finally, after the consensus decision analysis, the social appraisal system would reply with the restaurant ranking to B as “[Rank]: [restaurant2 N restaurant1 N restaurant3],” which means that B's friends think “restaurant2” is the most suitable restaurant for B.

![](/api/attachments/3T2S3BK9/fulltext/images/2a2baec7e79c3a7e78dbe96d2d51d9a2602d925ffe9545defd2cfdfe64559da7.jpg)

![](/api/attachments/3T2S3BK9/fulltext/images/095dd2c4e1cae202bcd5302677686c98a771231f4b56de8143ee96fa2d2ec35f.jpg)  
Fig. 7. Synonymous adjective graph creation.

## 5. Results and evaluation

Because the effectiveness of social decision support is determined by the recipient's subjective judgment [8], the results recommended by the proposed mechanism should be compared with the support requester's self-evaluation. The detailed comparison rules are listed in Table 3.

There are two major evaluation rules to judge the effectiveness of the social support mechanism:

(1) Recommend that the user buys the product he/she is satis<sup>fi</sup>ed with. If the support requester feels satis<sup>fi</sup>ed with the product and the SAM also recommends purchasing it (i.e. it is placed in <sup>fi</sup>rst place by the system), a mark “CSS,” which means correct social support is made:

![](/api/attachments/3T2S3BK9/fulltext/images/39c453c086747dcd60f20444474975532ca41ae8c1b0caf64259a9a477a81df8.jpg)  
Fig. 8. Accuracy comparison between different polar word pairs.

Table 3 Evaluation rule table.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">User evaluation</td></tr><tr><td>Satisfied</td><td>Unsatisfied</td></tr><tr><td rowspan="2">System recommendation</td><td>Purchasing</td><td>CSS</td><td>1 - CSU</td></tr><tr><td>Not purchasing</td><td>1 - CSS</td><td>CSU</td></tr></table>

$$
C S S = \frac {| S \cap R |}{| S |},\tag{20}
$$

where S stands for the set of satisfactory products purchased and R for the set of products recommended for purchasing.

(2) Do not recommend that the user buys the product he/she is dissatis<sup>fi</sup>ed with. If the support requester feels dissatis<sup>fi</sup>ed with the product and the SAM does not recommend purchasing it, a mark “CSU” is given, which means that wrong social support is avoided:

$$
C S U = \frac {| \bar {S} - R |}{| \bar {S} |},\tag{21}
$$

where $\bar { S }$ stands for the set of unsatisfactory products purchased. For enterprises, these two rules could enhance customers' degrees of satisfaction and create more business opportunities.

The overall successful support is measured as

$$
S S = \frac {\left| S \cap R \right| + \left| \overline {{S}} - R \right|}{\left| S \right| + \left| \overline {{S}} \right|}.\tag{22}
$$

## 5.1. Comparisons of criteria weighting strategies

We construct three experiments and compare the results with respect to the self-weighting, group-weighting, and equal-weighting strategies. The criteria importance of self-weighting and group-weighting strategies is respectively obtained from the decision requester and the group of decision supporters. For the equal-weighting strategy, the criteria importance is set to 1. The results shown in Fig. 9-(a) and (b) show that the self-weighting strategy is more effective than other strategies for both search and experience goods. This is because when making a purchasing decision, the decision-maker most clearly knows his/her individual needs. In addition, as our close friends might know us better, the group-weighting strategy has better performance than the equal-weighting strategy. Therefore, it is suitable to use the groupweighting strategy as the default criteria weighting if the support requester does not give his/her own criteria importance settings.

![](/api/attachments/3T2S3BK9/fulltext/images/2e3977c4e32dcad7c5bdff3de8b4308b2bb765c2b50017290cbcfa5a3ad2dc9e.jpg)  
a) Search goods

Table 4 Statistical veri<sup>fi</sup>cation of the decision analysis results with different approaches for search goods.

<table><tr><td colspan="2">Paired group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T value</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="2">Self V.S.</td><td>Group</td><td>-0.063</td><td>0.358</td><td>0.020</td><td>-3.138</td><td>0.002</td></tr><tr><td>Equal</td><td>-0.036</td><td>0.394</td><td>0.022</td><td>-1.670</td><td>0.003</td></tr><tr><td>Group V.S.</td><td>Equal</td><td>0.026</td><td>0.389</td><td>0.021</td><td>1.198</td><td>0.011</td></tr></table>

Tables 4 and 5 show the results of the 95% signi<sup>fi</sup>cance level twopaired sample t-test. The results verify that the self-weighting strategy signi<sup>fi</sup>cantly outperforms the other strategies.

## 5.2. Comparisons of support effectiveness

We construct and compare the results of three experiments with three product selection approaches: the proposed SAM, the majority voting method, the <sup>fi</sup>ve-star rating method, and the random selection method. The majority voting method is one of the baseline social support methods allowing users to aggregate friends' opinions. For example, Facebook has developed a simple social support function, “Questions.” In this scenario, support requesters are asked to repost their social appraisal requests and then decision supporters vote directly for which candidate is most suitable without criteria and evaluations. The <sup>fi</sup>ve-star rating method is one of the baseline product evaluation methods for gathering the collective opinions of public users. In this scenario, decision supporters are requested to reply with their opinions by using a <sup>fi</sup>ve-star scale for each alternative. The random selection method is used to simulate the scenario that there is no social support mechanism. In this scenario, participants do not know which product is the most suitable and pick one to buy randomly. Fig. 10 indicates that the proposed mechanism is more effective than the other baseline social support methods. The measures “CSS” and “CSU” respectively indicate that the support requester indeed buys the most suitable product and that the support requester indeed avoids buying an unsuitable product.

![](/api/attachments/3T2S3BK9/fulltext/images/24a9ca895d391d785e2335b0e824d0a73dc4a9b24dd8f979bcf0a5b2783836d7.jpg)  
b) Experience goods  
Fig. 9. Accuracy rates of different criteria weighting strategies.

Table 5  
Statistical veri<sup>fi</sup>cation of the decision analysis results with different approaches for experience goods

<table><tr><td colspan="2">Paired group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T value</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="2">Self V.S.</td><td>Group</td><td>0.099</td><td>0.370</td><td>0.023</td><td>4.306</td><td>0.000</td></tr><tr><td>Equal</td><td>0.083</td><td>0.376</td><td>0.024</td><td>3.535</td><td>0.000</td></tr><tr><td>Group V.S.</td><td>Equal</td><td>-0.017</td><td>0.381</td><td>0.024</td><td>-0.699</td><td>0.001</td></tr></table>

As we can observe, the performance of our proposed SAM is better than that of the other approaches. First, the SAM, majority voting method, and <sup>fi</sup>ve-star rating method perform better than the random approach. This <sup>fi</sup>nding indicates that soliciting external appraisement from the social network is helpful for supporting customers' online shopping behavior. Second, both the SAM and the majority voting method aim to provide social appraisal support for support requesters, but the majority voting method does not consider the relative importance of decision supporters. This <sup>fi</sup>nding shows that considering social companionship could improve the SAM. Third, the result of the <sup>fi</sup>ve-star rating method is similar to the voting method. From the purchasing purpose, the buyer would like to buy the most suitable product. A decision supporter provides the highest star to a product to indicate that he/she feels the product is the most appropriate. Similarly, he/she will vote for the most suitable product by using the voting method.

Owing to the dif<sup>fi</sup>culty of complex nature language analysis and heterogeneity of user tastes, the extracted criteria and evaluations using semantic analysis for experience goods might not perfectly represent the characteristics of a product, meaning that the CSS evaluation values of experience goods are lower than those for search goods and that CSU is greater than CSS in the evaluations of experience goods.

Finally, the result of the overall performance of these approaches is further evaluated by using a two-paired sample t-test (Tables 6 and 7). At the 95% signi<sup>fi</sup>cance level, all the test results show that the proposed SAM signi<sup>fi</sup>cantly outperforms the other product selection approaches.

Table 6  
Statistical veri<sup>fi</sup>cation of the decision analysis results with different approaches for search goods.

<table><tr><td colspan="2">Paired group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T value</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="3">SAM V.S.</td><td>Voting</td><td>-.01904</td><td>.38157</td><td>.02140</td><td>-.890</td><td>.003</td></tr><tr><td>Five-star</td><td>.02918</td><td>.39352</td><td>.02207</td><td>1.322</td><td>.002</td></tr><tr><td>Random</td><td>-.04526</td><td>.39169</td><td>.02197</td><td>-2.061</td><td>.000</td></tr></table>

We further compare the effectiveness of various appraisal mechanisms by using different social companionship measures: (1) the proposed SAM, which considers behavioral and structural tie strengths, (2) an appraisal mechanism that uses only behavior weighting (SAM-B), (3) an appraisal mechanism that uses only structural weighting (SAM-S), and (4) an appraisal mechanism that uses equal weighting (SAM-E). These alternatives are ranked by the appraisal mechanisms.

![](/api/attachments/3T2S3BK9/fulltext/images/5f4481ca6cb4150e16f8f39e2a9c638d447937831722d7340a44e29ca626c8ff.jpg)

Fig. 11 shows that using both the behavioral and the structural characteristics to evaluate the importance of friends can signi<sup>fi</sup>cantly improve appraisal effectiveness. The results of the two-paired sample t-test are shown in Tables 8 and 9. At the 95% signi<sup>fi</sup>cance level, all the test results show that the proposed companionship evaluation approach signi<sup>fi</sup>cantly outperforms the other approaches. This <sup>fi</sup>nding implies that it is bene<sup>fi</sup>cial and essential to consider behavioral information and structural information together when developing a social support mechanism.

## 5.3. Comparison of search and experience goods

The accuracy rates with respect to different products are shown in Fig. 12. The proposed mechanism achieves an overall 83% accuracy rate. The accuracy rates for search goods and for experience goods are 83% and 82%, respectively. Among search goods, cell phones have the highest accuracy rate (87%). Among experience goods, peripheral products have the highest accuracy rate (88%). Mobile devices, such as smartphones and tablets, are trendy products and most decision supporters invited to take part in the experiments already had one or more mobile devices and peripheral products. Respectively, 21% and

a) Search goods  
![](/api/attachments/3T2S3BK9/fulltext/images/67ae40e5837f81e28e155c43b0789aa8855f0277ebfdc65764e42745b2630959.jpg)  
b) Experience goods  
Fig. 10. Accuracy rates of different methods.

Table 7  
Statistical veri<sup>fi</sup>cation of the decision analysis results with different approaches for experience goods.

<table><tr><td colspan="2">Paired group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T value</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="3">SAM V.S.</td><td>Voting</td><td>0.051</td><td>0.406</td><td>0.017</td><td>3.025</td><td>0.003</td></tr><tr><td>Five-star</td><td>0.027</td><td>0.392</td><td>0.016</td><td>1.620</td><td>0.000</td></tr><tr><td>Random</td><td>0.097</td><td>0.386</td><td>0.016</td><td>6.002</td><td>0.006</td></tr></table>

32% of the requests for social appraisal support are related to peripheral products and mobile devices (cell phones and computer categories). Therefore, social support has a relatively suf<sup>fi</sup>cient basic knowledge to judge whether a product is good or bad and provide more appropriate product opinions and criteria evaluations.

As Fig. 12 shows, movies have the lowest rate (64%) for two reasons. First, movies are highly dependent on individual preferences, meaning that 11 (about 7%) appraisal requests are released. The number of decision samples might be insuf<sup>fi</sup>cient to evaluate performance accurately. Second, there are too many “unknown” criteria evaluations in the movie category. In addition, as watching a movie is a costly activity (time and price), comparatively few friends have watched all the alternatives of a movie appraisal request and respond with their opinions. However, the proposed mechanism still received approximately a 64% support accuracy rate in the movie category.

## 6. Conclusion

In this paper, a SAM composed of social companionship analysis, collective opinion analysis, and consensus decision analysis for online purchase support in the micro-blogosphere was proposed. To measure the social companionship of decision support, we constructed an interaction network based on the interactions of posts and responses in micro-blogs in order to measure the behavioral and structural tie strengths of the social relationship by analyzing the friend network. To analyze the collective opinions, a text-mining technique with semantic orientation identi<sup>fi</sup>cation was developed for criteria and evaluation extraction. In addition, to resolve the inherent issue of information incompleteness in collective opinions, IFS was applied to model vague or incompletely known opinions from the micro-blogosphere. Finally, to consolidate the evaluations from various decision supporters and the support requester's decision criteria preference, TOPSIS was applied to rank the <sup>fi</sup>nal alternative. Our experimental results show that the accuracy of the proposed social appraisal support mechanism outperforms that of other benchmark approaches. The proposed social appraisal framework that solicits opinions from trusted friends can thus be effectively applied to support individual decisions, such as online purchasing.

Table 8  
Statistical veri<sup>fi</sup>cation of the decision analysis results with different weighting methods for search goods.

<table><tr><td colspan="2">Paired group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T value</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="3">SAM V.S.</td><td>SAM-B</td><td>-.06406</td><td>.36091</td><td>.02024</td><td>-3.165</td><td>.002</td></tr><tr><td>SAM-S</td><td>-.04501</td><td>.37700</td><td>.02114</td><td>-2.129</td><td>.003</td></tr><tr><td>SAM-E</td><td>-.04043</td><td>.39475</td><td>.02214</td><td>-1.826</td><td>.000</td></tr></table>

## 6.1. Research contributions

The methodological and practical contributions of this research are summarized as follows. First, from the perspective of systems innovation, as online social intercourse and online shopping have become increasingly popular, the design of social appraisal systems has grown in importance. This research proposes a new and feasible mechanism that seeks decision support from friends in the blogosphere. Second, from the perspective of methodology, the proposed framework appropriately integrates techniques from various domains, such as SNA, text mining, fuzzy computing, and multi-criteria decision-making, to resolve the decision-making problems of electronic commerce in the emerging social networking environment. Third, from the perspective of practice, through this proposed social appraisal support mechanism, users could treat their social networks as their own expert groups and leverage them for decision support. Although the aggregated public evaluations expressed on online review platforms (e.g. Amazon) are comparatively stable and objective, they may not really <sup>fi</sup>t the preferences and needs of an individual decision requester. The proposed mechanism, which solicits and consolidates comments from close friends, can better provide a more helpful and suitable support, speeding up the decision process.

![](/api/attachments/3T2S3BK9/fulltext/images/5f15532e587751c37e2a09912d6fe793e4c90dbb310dceecd41c1f733560964c.jpg)  
a) Search goods

![](/api/attachments/3T2S3BK9/fulltext/images/0e804588d5bd6cf843ae20827928bc662d24a8e04ab8dd1fd33ec7db2ed9d7f7.jpg)  
b) Experience goods  
Fig. 11. Accuracy rates of different companionship measures.

Table 9  
Statistical veri<sup>fi</sup>cation of the decision analysis results with different weighting methods for experience.

<table><tr><td colspan="2">Paired group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T value</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="3">SAM V.S.</td><td>SAM-B</td><td>.09978</td><td>.37075</td><td>.02317</td><td>4.306</td><td>.000</td></tr><tr><td>SAM-S</td><td>.08013</td><td>.37909</td><td>.02369</td><td>3.382</td><td>.001</td></tr><tr><td>SAM-E</td><td>.08312</td><td>.37627</td><td>.02352</td><td>3.535</td><td>.000</td></tr></table>

## 6.2. Limitations and future studies

There are several limitations to this research. First, some preparation for acquiring product information still needs to be carried out before the appraisal system is applied. For example, before soliciting decision support from their friends, customers have to prepare the candidate products according to their own product survey or through other recommender systems. Second, owing to the word limit in micro-blogs, the sentences in the opinions expressed by decision supporters have to be short. As a result, the information represented from the extracted criteria and evaluation might not be suf<sup>fi</sup>cient to appraise a product. Third, although the current adjective graph could satisfactorily identify most of the adjectives with high usage frequency, the adjective orientation might not be easily identi<sup>fi</sup>able if decision supporters use words with low usage frequency. Fourth, for experience goods, owing to the problem of ambiguous nature langue (e.g. the user might tend to improvise new words and abbreviations) and because they are a matter of taste, the semantic analysis might not well extract and represent the criteria and evaluations of a product. Therefore, the SAM for experience goods might not work as effectively as it does for search goods.

Some aspects can still be further improved. First, in our experiment design, we asked participants to recall their original purchase decision-making processes; there is thus a possibility of recall bias regarding the things they discovered. To reduce this potential bias, we could conduct experiments to trace the related information automatically within participants' decision-making processes. Second, the approach to extracting criteria from the opinions expressed in natural language could be elaborated upon. If only the noun and noun phrase in the opinion are extracted, some important criteria may not be captured and some criteria may become too lengthy. Well-known topic detection methodologies can thus be utilized to enhance the effectiveness of criteria extraction. Third, in addition to the behavioral and structural dimensions, the method for measuring the importance or in<sup>fl</sup>uence of decision supporters might consider other factors. For example, the expertise or interest domains of decision supporters could be considered. Lastly, the impact of the “unknown” evaluations of criteria in the consensus decision analysis could be further investigated. The effectiveness of the system might be improved if these “unknown” criteria evaluations could be reduced.

## Acknowledgment

This research was supported by the National Science Council of Taiwan (Republic of China) under grant NSC 99-2410-H-009-035-MY2.

## References

[1] A. Agarwal, P. Bhattacharya, Augmenting Wordnet with polarity information on adiectives. 3rd International Wordnet Conference, Jeiu Island. Korea. 2006

[2] K.T. Atanassov, Intuitionistic fuzzy sets, Fuzzy Sets and Systems 20 (1986) 87–96

[3] Bangalore, Analysis on the General Pro<sup>fi</sup>le of Users on Plurk.com. InRev Systems, Available at http://www.slideshare.net/bexdeep/plurk-analysis-4136802(Accessed February 20, 2012).

[4] S.Y. Chou, Y.H. Chang, C.Y. Shen, A fuzzy simple additive weighting system under group decision-making for facility location selection with objective/subjective attributes, European Journal of Operational Research 189 (2008) 132–145.

[5] O.S. Dalgard, Social support—de<sup>fi</sup>nition and scope, Available at http://www.euphix. org/object\_document/o5479n27411.html(Accessed April 10, 2012).

[6] S.K. De, R. Biswas, A.R. Roy, Some operations on intuitionistic fuzzy sets, Fuzzy Sets and Systems 114 (2000) 477–484.

[7] M.S. Granovetter, The strength of weak ties, The American Journal of Sociology 78 (6) (1973) 1360–1380.

[8] R.A.R. Gurung, Coping and social support, Health Psychology: A Cultural Approach, Thomson Wadsworth, Belmont, CA, 2006. 131–171.

[9] A. Hall, B. Wellman, Social networks and social support, in: S. Cohen, S.L. Syme (Eds.), Social Support and Health, Academic Press, Orlando, Florida, 1985, pp. 23–41.

[10] C.J. Hinde, R.S. Patching, S.A. McCoy, Semantic transfer and contradictory evidence in intuitionistic fuzzy sets in: Proceedings of 2008 IEEE International Conference on Fuzzy Systems Hong Kong,2008, 2095-2102

[11] L.M. Horowitz, E.N. Krasnoperova, D.G. Tatar, M.B. Hansen, E.A. Person, K.L. Galvin, K.L. Nelson, The way to console may depend on the goal: experimental studies of social support, Journal of Experimental Social Psychology 37 (1) (2001) 49–61.

[12] J.S. House, Work Stress and Social Support, Addison-Wesley Reading, Mass, 1981.

[13] Y.C. Hu, Classi<sup>fi</sup>cation performance evaluation of single-layer perceptron with Choquet integral-based TOPSIS, Applied Intelligence 29 (3) (2008) 204–215.

[14] B.J. Jansen, M. Zhang, K. Sobel, A. Chowdury, Twitter power: tweets as electronic word of mouth, Journal of the American Society for Information Science and Technology 60 (11) (2009) 2169–2188.

![](/api/attachments/3T2S3BK9/fulltext/images/b77d12f184acb737615c9ab4667a251b791cca718655914711e77a8d11ad550e.jpg)  
a) Search goods  
Fig. 12. Accuracy rates for different products

![](/api/attachments/3T2S3BK9/fulltext/images/0ef54cc53057776a605d3cc836383f7925b86bc86207b98ba33dc8b3f32d6d22.jpg)  
b) Experience goods

[15] A. Java, X. Song, T. Finin, B. Tseng, in: Proceedings of the 9th WebKDD and 1st SNA-KDD 2007 Workshop on Web Mining and Social Network Analysis, Why we twitter: Understanding microblogging usage and communities, ACM, New York, NY, USA, 2007.

[16] J. Kamps, M. Marx, R.J. Mokken, M.D. Rijke, Using Wordnet to measure semantic orientation of adjectives, Proceedings of LREC, 4th International Conference on Language Resources and Evaluation, 4, 2004, pp. 1115–1118.

[17] M. Kilduff, The friendship network as a decision-making resource: dispositional moderators of social in<sup>fl</sup>uences on organizational choice, Journal of Personality And Social Psychology 62 (1) (1992) 168–180.

[18] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers—measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008) 233–253.

[19] M.S. Kuo, G.H. Tzeng, W.C. Huang, Group decision-making based on concepts of ideal and anti-ideal points in a fuzzy environment, Mathematical and Computer Modelling 45 (3–4) (2007) 324–339.

[20] D.Z. Levin, R. Cross, The strength of weak ties you can trust: the mediating role of trust in effective knowledge transfer, Management Science 50 (11) (2004) 1477–1490.

[21] D. Lewis, D. Bridger, The Soul of the New Consumer: Authenticity—What We Buy and Why in the New Economy, Nicholas Brearley, London, 2000.

[22] F. Li, T.C. Du, Who is talking? An ontology-based opinion leader identi<sup>fi</sup>cation framework for word-of-mouth marketing in online social blogs, Decision Support Systems 51 (1) (2011) 190–197.

[23] Y.M. Li, C.P. Kao, TREPPS: a trust-based recommender system for peer production services, Expert Systems with Applications 36 (2) (2009) 3263–3277.

[24] D.R. Liu, C.H. Lai, W.J. Lee, A hybrid of sequential rules and collaborative <sup>fi</sup>ltering for product recommendation, Information Sciences 179 (20) (2009) 3505–3519.

[25] H.W. Liu, G.J. Wang, Multi-criteria decision-making methods based on intuitionistic fuzzy sets, European Journal of Operational Research 179 (2007) 220–233.

[26] Z. Liu, W. Yu, W. Chen, S. Wang, F. Wu, Short text feature selection and classi<sup>fi</sup>cation for micro blog mining, Proceedings of International Conference on Computational Intelligence and Software Engineering, 2010, pp. 1–4.

[27] P.D. Meo, A. Nocera, G. Terracina, D. Ursino, Recommendation of similar users, resources and social networks in a social internetworking scenario, Information Sciences 181 (7) (2011) 1285–1305.

[28] G.A. Miller, WordNet: an on-line lexical database, International Journal of Lexicography 3 (4) (1990) 235–312.

[29] G.A. Miller, WordNet: a lexical database for English, Communications of the ACM 38 (11) (1995) 39–41.

[30] H. Mintzberg, D. Raisinghani, A. Theoret, The structure of “unstructured” decision processes, Administrative Science Quarterly 21 (1976) 246–275.

[31] P. Nelson, Information and consumer behavior, Journal of Political Economy 78 (2) (1970) 311–329.

[32] NLProcessor Text Analysis Toolkit, Available at http://www.infogistics.com textanalysis.html2000.

[33] P. O'Reilly, Methodological issues in social support and social network research, Social Science and Medicine 26 (8) (1988) 863–873.

[34] J.P. Onnela, J. Saramaki, J. Hyvonen, G. Szabo, D. Lazer, K. Kaski, J. Kertesz, A.L. Barabasi, Structure and tie strengths in mobile communication networks, Proceedings of the National Academy of Sciences of the United States of America 104 (18) (2007) 7332-7336.

[35] X. Shi, L.A. Adamic, M.J. Strauss, Networks of strong ties, Physica A: Statistical Mechanics and its Applications 378 (1) (2007) 33–47.

[36] W. Steegenga, S. Forge, IBM study <sup>fi</sup>nds social networks in<sup>fl</sup>uence more than half of shoppers' decision-making—even in the store. IBM Research Center, Available at http://www-03.ibm.com/press/uk/en/pressrelease/35340.wss#release(Accessed April 10, 2012).

[37] E. Szmidt, J. Kacprzyk, Distances between intuitionistic fuzzy sets, Fuzzy Sets and Systems 114 (2000) 505–518.

[38] Y.J. Tang, C.Y. Li, H.H. Chen, A comparison between microblog corpus and balanced corpus from linguistic and sentimental perspectives, Proceedings of AAAI Workshop on Analyzing Microtext, San Francisco, 2011, pp. 68–73.

[39] D. Tapscott, Net gen transforms marketing, Bus. Week, Available at http://www. businessweek.com/technology/content/nov2008/tc20081114\_882532.htm (Accessed April 9, 2012).

[40] L. Terveen, D.W. McDonald, Social matching: a framework and research agenda, ACM Transactions on Computing-Human Interaction 12 (3) (2005) 401–434.

[41] P.A. Thoits, Social support as coping assistance, Journal of Consulting and Clinical Psychology 54 (1986) 416–423.

[42] P.D. Turney, M.L. Littman, Measuring praise and criticism: inference of semantic orientation from association, ACM Transactions on Information Systems 21 (4) (2003) 315–346.

[43] S. Vegnaduzzo, Acquisition of subjective adjectives with limited resources, Proceedings of the AAAI Spring Symposium on Exploring Attitude and Affect in Text: Theories and Applications, Stanford, US, 2004.

[44] S. Wasserman, K. Faust, Social Network Analysis: Methods and Applications, Cambridge University Press, Cambridge, 1994.

[45] J. Ye, Multicriteria fuzzy decision-making method based on a novel accuracy function under interval-valued intuitionistic fuzzy environment, Expert Systems with Applications 36 (2009) 6899–6902.

[46] D. Zhao, M.B. Rosson, How and why people Twitter: the role that micro-blogging plays in informal communication at work, Proceedings of the ACM 2009 International Conference on Supporting Group Work, New York, NY, USA, 2009, pp. 243–252.

[47] J. Zhao, J. Wu, K. Xu, Weak ties: subtle role of information diffusion in online social networks, Physical Review E 82 (1) (2010) 16–105.

[48] C.N. Ziegler, J. Golbeck, Investigating interactions of trust and interest similarity, Decision Support Systems 43 (2) (2007) 460–475

![](/api/attachments/3T2S3BK9/fulltext/images/e84f0f836d025f136298894ef3f957b7e4cd8a7371ef42b2c2c40496599bbd42.jpg)  
Yung-Ming Li is a Professor at the Institute of Information Management National Chiao Tung University in Taiwan. He received his Ph.D. in Information Systems from the University of Washington. His research interests include network science, Internet economics, and business intelligence. His research has appeared in IEEE/ACM Transactions on Networking, INFORMS Journal on Computing, Decision Sciences, European Journal of Operational Research, Decision Support Systems, International Journal of Electronic Commerce, ICIS, WITS, among others

![](/api/attachments/3T2S3BK9/fulltext/images/0604226f7537b947e342ed7bc00a37fd2259d06e928cb3a974545b56acca4416.jpg)

Cheng-Yang Lai received his Ph.D. from the Institute of Information Management, National Chiao Tung University in Taiwan. His research interests include electronic commerce and business intelligence. His research has appeared in Decision Support Systems, Electronic Commerce Research and Applications, and Information Sciences.
