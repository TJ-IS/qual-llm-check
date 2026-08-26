---
otero_id: 19652
otero_key: "937SESPW"
title: "A social mechanism for task-oriented crowdsourcing recommendations"
authors: "Yung-Ming Li; Chin-Yu Hsieh; Lien-Fa Lin; Chi-Hsuan Wei"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113449"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

A social mechanism for task-oriented crowdsourcing recommendations

Decision Support Systems

Yung-Ming Li, Chin-Yu Hsieh, Lien-Fa Lin, Chi-Hsuan Wei

![](/api/attachments/937SESPW/fulltext/images/8e3d3b1d93a385d35a7c238cce4359e2d2b520c2f174d0f11d6935c757c41d13.jpg)

PII: S0167-9236(20)30204-9

DOI: https://doi.org/10.1016/j.dss.2020.113449

Reference: DECSUP 113449

To appear in: Decision Support Systems

Received date: 18 May 2020

Revised date: 13 October 2020

Accepted date: 11 November 2020

Please cite this article as: Y.-M. Li, C.-Y. Hsieh, L.-F. Lin, et al., A social mechanism for task-oriented crowdsourcing recommendations, Decision Support Systems (2020), https://doi.org/10.1016/j.dss.2020.113449

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# A social mechanism for task-oriented crowdsourcing recommendations

Yung-Ming Li<sup>a,\*</sup> yml@mail.nctu.edu.tw, Chin-Yu Hsieh<sup>a</sup> hsieh.chinyu@gmail.com, Lien-Fa Lin<sup>b</sup> lienfa@asia.edu.tw, Chi-Hsuan Wei<sup>a</sup> kobewei81@gmail.com Institute of Information Management, National Chiao Tung University, Hsinchu, 300, Taiwan <sup>b</sup>Department of M-Commerce and Multimedia Applications, 41354, Asia University, Taiwan. Correponding author.

## Abstract

Crowdsourcing is a new trend that uses the wisdom of crowds on the Internet to solve certain problems that need vast amounts of human resources. There have been a number of crowdsourcing platforms developed for various domains. However, the landscape of crowdsourcing platforms is widely dispersed and most tasks remain hidden. Finding out the tasks closely matching contributors’ personal preference and capabilities is difficult. In this research, we aim to design a social mechanism for task-oriented crowdsourcing recommendations, which the requesters can easily use to find suitable contributors who are also very willing to finish their tasks. Our experimental results show that the proposed mechanism is effective in identifying appropriate contributors with respect to different types participants of task-oriented crowdsourcing.

Keywords: Task-oriented, Crowdsourcing, Contributor preference, Social relationship, Social recommendation.

## 1. Introduction

In recent years, crowdsourcing has become a new trend that uses the wisdom of crowds on the Internet to solve certain problems that need enormous amounts of human resources [8]. This can solve significant and complex problems by aggregating distributed online computing resources to reduce costs and time [29]. This paradigm shift originated with companies and individuals starting to provide outsourcing services based on anonymous communities, or ―crowds,‖ throughout the Web (e.g., iStockPhoto, Taskcn, InnoCentive, and Amazon’s Mechanical Turk). A number of business models

have emerged that use crowdsourcing to manage and distribute works to the crowd. Generally speaking, task-oriented crowdsourcing operations comprise two dimensions: (i) the crowdsourcing organizations who publish their tasks to the public through public call, not limited to specific groups, are normally called as ―requesters,‖; (ii) The crowd who engage freely and are willing to contribute to a task are often called ―contributors‖[9].

The contributors may receive a small reward if their completed tasks are accepted by the requesters. Besides monetary rewards, some contributors participate in crowdsourcing for community-based or social motivations [17]. The landscape of tasked-oriented crowdsourcing platforms is widely dispersed and most tasks are still hidden from the majority of the crowd. Consequently, contributors search only a limited number of tasks before deciding on those in which they will participate, often examining only the tasks that appear on the first couple of pages of the task listings [5]. As one of the world’s largest task-oriented crowdsourcing marketplaces, Amazon Mechanical Turk enables individuals and businesses to use human intelligence to perform tasks that Mechanical Turk sites usually consist of hundreds of pages. There are almost 500,000 contributors to this marketplace from 190 countries around the world, and over 2,500 human intelligence tasks (HITs) from which contributors can choose per day. Higher search costs may induce contributors to accept efficiency of crowdsourcing and the quality of the results are seriously deteriorated [13]. If requesters are not satisfied with the outcome, they may leave the platform; as a result, the platform could not only lose revenue from current tasks, but also future business opportunities. Several studies have shown that contributors have difficulty in finding the tasks that closely match their personal preference and capabilities [34], despite crowdsourcing platforms providing some selecting mechanisms for both requesters and contributors.

An effective recommendation mechanism could be a way of resolving this issue, helping both sides find each other more easily. However, due to some of the specific characteristics of crowdsourcing, previous recommendation systems, based on either a content filtering or collaborative filtering approach, have not been capable of satisfactorily resolving the problem. Therefore, in this

research we aim to design a social-based mechanism to create better task-oriented crowdsourcing recommendations. Nowadays, social networks are growing rapidly and occupy much of people’s time. People like to share their opinions or ideas on social media sites, such as Facebook, Twitter or Instagram [23]. It is possible to analyze information on social networks and crowdsourcing platforms such as contributors’ preferences, backgrounds, task-related information, and social relationships to match requesters and contributors for crowdsourcing tasks. To exploit the power of social networks for crowdsourcing recommendations, two research problems must be resolved: (i) how to use social networks to identify suitable and interested contributors for the crowdsourcing task, and (ii) how to use social influence to improve the willingness of contributors to complete tasks.

In terms of the first issue, the user’s preference is the primary factor in making a successful recommendation, but the contributor’s preference is not explicitly obtainable. Recently, however, as more people have begun to share social activities online, it has been possible to access certain contributor information such as interests, abilities, and motivation related to participation in crowdsourcing and social networking platforms. In addition, contributors’ performance and search histories reflect their abilities and interests in completing various kinds of task. It is thus possible to analyze a contributor’s preference and the task profile to evaluate the suitability of a contributor for a task.

Concerning the second issue, crowdsourcing is a particular way of soliciting contributions from strangers. A contributor’s interest in a task can be identified from the implicit social influence of social affiliations. A contributor is likely to be influenced by his/her close friends. If a contributor’s friend has shown interest in or had experience of certain kinds of task, the contributor will likely also be interested in them. Thus, one way of increasing the possibility of contributors accepting a task would be to recommend contributors who have a stronger relationship with the requester. In this regard, analyzing the social relationship between a requester and a contributor would be beneficial because a closer relationship will influence the willingness of contributor to complete the requester’s task.

To resolve these issues, we propose a social task-oriented crowdsourcing recommendation mechanism that will enable a requester to find suitable contributors easily and attain high quality results. The proposed recommendation mechanism has been built by considering three factors: (1) contributor preference, which comprises a contributor’s interests, abilities, and motivation related to participating, (2) contributor history, namely the contributor’s past experience and performance, and (3) social influence, which is based on social affiliations with the crowdsourcing tasks and the degree of social closeness between contributors and requesters. This mechanism could significantly reduce search costs and increase contributors’ motivation to take part in crowdsourcing tasks. The mechanism can help requesters identify suitable contributors efficiently and enable them to build more satisfying tasks. In turn, contributors can easily find those tasks that closely match their preferences. In terms of benefits for the crowdsourcing platform, this mechanism can induce more requesters and contributors to collaborate in the crowdsourcing market because of its more detailed matching. A valuable long-term partnership could be established to create value for the crowdfunding platform and all participants.

The remainder of the paper is outlined as follows. Section 2 discusses the literature related to this research, Section 3 describes the overall system framework, Section 4 details the experiments conducted for the proposed mechanism, Section 5 discusses the evaluation and results. Finally, section 6 discusses the study’s contributions, limitations, and areas for future research.

## 2. Related literature

## 2.1. Task-oriented crowdsourcing

According to Howe [14 $^ { \Gamma } ( 4 _ { \perp } )$ ―crowdsourcing is the act of taking a task traditionally performed by a designated agent (such as an employee or a contractor) and outsourcing it by making an open call to an undefined but large group of people.‖ The basic concept of crowdsourcing derived from open innovation and open sources [11]. The concept of crowdsourcing has been extended to many types of application, such as crowdsourcing referral and tasked-oriented crowdsourcing.

In tasked-oriented crowdsourcing, those who post tasks on social networks are often called ―requesters,‖ while those who are willing and able to contribute to these tasks are often called ―contributors.‖ Contributors can receive a reward if their completed tasks are accepted by requesters. Crowdsourcing tasks can be classified as professional and non-professional tasks. Professional tasks require abstract thinking and people with specialized skills, including software engineers, data

scientists, artists, designers, management consultants, and enthusiasts with advanced academic degrees or industry experience [24]. Non-professional tasks, such as language translation services, data entry, photograph tagging, and transcription, are popular items that allow large workloads to be split across remote workforces with no geographic or time restrictions [24].

Recently, a few studies have been conducted on the concept of budget-aware task allocation in crowdsourcing. For example, [26] use the location-based social network Foursquare to obtain specific location information, including users and venues, extracted as a dataset to perform tasks. [38] also use spatial crowdsourcing to collect data or road information in real time for a budget-aware task to improve the task allocation rate and maximize the quality of results with limited budgets. However, most of the existing works only consider partial factors and focus on the preference aspect of crowdsourcing. In this research, we combine preference, and social factors to recommend contributors who are highly suited to the crowdsourcing task.

In this research, the crowdsourcing tasks are principally classified as professional and non-professional types, and the corresponding contributors are recommended according to the task characteristics. Combining social relationships and user preferences, we aim to develop a new social mechanism to recommend suitable contributors who are highly relevant to the task being crowdsourced. Specifically, we analyze contributors’ preferences, capabilities, and willingness to take on the task, using the information extracted from social networking and crowdfunding platforms.

## 2.2. Recommendation systems

Recommendation systems utilize a category of tools and techniques to suggest potentially useful items matching personal preferences [31]. Recommendation systems can be classified into two types: content-based and collaborative-based filtering systems [27]. Content-based systems create a profile for each user or product. The profiles of users and products allow the recommendation programs to associate users with matching products. The advantage of this is that it can access new products and users within the system. In contrast, collaborative-based systems focus on finding similar users related to the target and generate recommended items through the preferences of similar users. The drawback of the collaborative-based method is that it has limitations in terms of rating sparsity, scalability, and efficiency [21].

To solve these various problems, many researchers have aimed to develop more customized recommendations. Customized recommendations create user profiles according to users’ preferences, interests, and needs. Personalized recommendations suggest items or products according to the user’s preferences. A user can give feedback evaluating quality and usefulness of the recommendation to improve the effectiveness of the system [16]. Recently, social media sites such as Facebook, Google+, and Twitter have started to play an increasingly important role in people’s daily lives, and recommendation systems based on the social networking service (SNS) model have been developed. This type of recommendation system searches for popular and influential people on social network sites to generate social recommendations [40]. Social recommendation systems analyze social relationships and use social influence to enhance the performance of recommendations [39]. People demonstrated to enhance recommendation quality significantly [25].

The success of task crowdsourcing depends on factors such as the type of task, contributors preferences and capabilities, and social relationships. In our research, we aim to develop a social mechanism to support task crowdsourcing recommendations. Specifically, we analyze related tasks.

## 2.3. Social influence

Social network structures consist of individuals with implied relations, which can be used to explain many social phenomena. Social influence occurs when someone’s emotions, behaviors or opinions are influenced by others. Social influences have a significant impact on people’s lives, influencing ideas and behavior [18]. The application of social influence is mainly seen between friends, family, and partners [1]. By looking at people’s intimate social circles, we can discover the same habits, interests, and activities, as behavior is easily affected by close others. A famous example of social influence from 2014 is the Ice Bucket Challenge, a charity drive that went viral on social networks around the world. Friends who have closer relationships and frequent interactions tend to have the same interests, so they will receive recommendations for similar events [3].

Social networks are structures in which every user connects with other users, resulting in a connection network that includes both nodes and edges. A node represents an individual and an edge denotes a direct connection between two persons [35]. Previous studies have suggested that similarity in interests is strongly associated with the relationship between two users [44], with people being more willing to accept similar content shared by friends [12]. Therefore, if a user is interested in and works on one task, the friends with whom the user has strong ties are also more likely to take an interest in it. In addition, a close social relationship between a contributor and a requester will increase the likelihood that the contributor will help the requester to complete his/her tasks. Equally, a

Crowdsourcing is a particular way of soliciting solutions and contributions from the crowd. The strength of a social relationship will have a significant impact on contributors’ willingness to participate, as corresponding social influences will implicitly induce their participation. In this research, we use aforementioned theories and techniques to compute the social relationships between contributors and requesters, and thus ensure social affiliations and social closeness.

## 3. The system framework

We develop a social recommendation mechanism for task-oriented crowdsourcing that can identify suitable contributors with high levels of willingness to contribute and able to complete a task with high quality results. Contributors’ preferences, performance history, and social influences are analyzed to infer suitability for a take. The proposed mechanism can help both requesters and contributors find long-term partners and generate profitability for the task-oriented crowdsourcing platform. The processes of our proposed mechanism are described as follows

Fig. 1:

![](/api/attachments/937SESPW/fulltext/images/a542149cfcaad1c19521cbc1370d6daee471cb666800608c4fc5c3bf0c1d030a.jpg)  
Fig. 1 The processes of the task-oriented crowdsourcing mechanism

1. The requester creates and submits a task to the crowdsourcing platform. The task is categorized by analyzing the information posted, such as task properties, task description, time allotted, and reward.

2. The social recommendation mechanism measures the suitability of the contributors for the task. A contributor is evaluated according to his/her preferences, capabilities, and willingness to participate, using the information extracted from social networking and crowdfunding platforms.

3. The system generates a list of recommended contributors for the requester according to the suitability scores of the potential contributors.

4. The requester selects the final contributors from the recommendation list and sends them task invitations.

The system framework for task-oriented crowdsourcing recommendation is depicted in Fig. 2 and four main modules described as follows

(1) Type tree construction module. In this module, we aim to establish a type tree to classify crowdsourcing tasks and describe a contributor’s preferences. The category tree is built by referring to different crowdfunding platforms.

(2) Contributor pool analysis module. This module analyzes the contributors’ preferences, including their interests, capacity, and motivation. We also analyze their search history and performance history in the task-oriented crowdsourcing platform because past performance has been observed to be a good predictor of future performance.

(3) Social influence analysis module. This module analyzes the social affiliation of a contributor in relation to the task and the social closeness of the contributor to the requester, which will influence a contributor’s willingness to engage in the task.

(4) Task-oriented crowdsourcing recommendation module. This purpose of the recommendation engine is to generate a list of suitable contributors for the requester’s task according to the information analysis.

![](/api/attachments/937SESPW/fulltext/images/e8105b834397d72d6d59285a4e5859fd674e1518b85a1c17fcc80a9a985ac077.jpg)  
Fig. 2. The system framework

## 3.1. Type tree construction module

A hierarchical structure is a good construction for use in classification. In this research, we use a tree structure to classify the task into different levels of types. A node closer to a leaf represents a more specific classification attribute. Conversely, a node closer to a root represents a vaguer semantic concept. For example, as shown in

Fig. 3, the first layer is the root, the second layer includes classification into professional and non-professional task types, and the third layer includes task types defined more specifically from the second layer. It should be noted that there are many nodes in the type tree constructed, and we display only a part of these. Several studies have provided support for this type of structure performing effectively in the fields of product taxonomy [45] and semantic similarity analysis in taxonomy [22]. In this research, the tree-like structure is used to describe the type of task requested and the potential contributors’ preferences.

![](/api/attachments/937SESPW/fulltext/images/b8a0f10f18f6f20e7f9151376f5545c23eb60cb81070ff88615b616476e5af77.jpg)  
Fig. 3. Example of tree construction

## 3.2. Contributor pool analysis module

In this module, we analyze the contributors’ preferences and their performance histories. Individual preference is converted to keywords by taxonomy. By estimating the semantic similarity of the keywords in the taxonomy [30], individual preferences are then categorized based on the type tree constructed. Contributors’ performance histories for a task-oriented crowdsourcing platform are recorded using a contributor–task matrix.

## 3.2.1. Contributors’ preference analysis

We can infer a contributor’s preferences from user posts, profiles, and ―likes‖ on social media [32], [41], [43]. The analysis helps us to understand a contributor’s interests, capacities, and motivation in assessing what they want to gain after completing their contributions.

Contributors’ interests. In this research, we consider the following social activities (1) check-ins: these reveal location-based service (LBS) data such as location, time, and what the use is doing; (2)

pages: on Facebook, a user can choose their preferred pages, and we can use these to infer his/her interests; (3) likes: a user can use these to display the fact that they ―like‖ someone’s opinion; (4) comments: a user can post comments related to specific themes on social media. As social media have their own specific rules for classifying check-ins, pages, ―likes,‖ and comments, we need to transform the social data to match the task type tree constructed. The interests of contributor $C _ { i }$ in type T can be inferred from their social activities and computed as:

$$
\begin{array}{r l} & S o c i a l I n t e r e s t (C _ {i}, T) \\ & \qquad = c h e c k i n s _ {t y p e} (C _ {i}, T) + p a g e _ {t y p e} (C _ {i}, T) + l i k e _ {t y p e} (C _ {i}, T) + c o m m e n t _ {t y p e} (C _ {i}, T) \end{array}\tag{1}
$$

In the process of generating a suitable recommendation list, we need to understand the benefits of contributors. Through the structure of the task type tree, we can easily transform social data (sign-ins, pages, likes, and comments) to match user preferences and types of tasks by measuring their similarity. Cosine similarity is a popular measure to determine the similarity of two vectors of characteristic information in a vector space model, which is commonly used to measure the matching fitness of two objects. For example, [36] use a similar approach to analyze social media information and propose a recommendation method for discovering user interests. The similarity between a contributor $C _ { i }$ and a type T task can be obtained as follows:

$$
\text {Similarity} (C _ {i}, T) = \cos (\overrightarrow {C _ {i}}, \overrightarrow {T}) - \frac {\overrightarrow {C _ {i}} \cdot \overrightarrow {T}}{\| \overrightarrow {C _ {i}} \| \| \overrightarrow {T} \|},\tag{2}
$$

where $\overrightarrow { C _ { \iota } }$ and $\vec { T }$ represents the vectors denoting the times of message sharing for different nodes in the type tree. This can be seen, for example, if a contributor is interested in ―Design‖ and likes to share related information in his/her social network, or comments on related ―Graphic‖ messages three times and ―Logo‖ messages four times. There are two vectors, $\overrightarrow { D e s \imath g n }$ and $\overrightarrow { C _ { \imath } }$ with 9 dimensions constructed by the index of nodes in the category tree. The nine dimensions are (1) Root, (2) Professional, (3) Non-Professional, (4) Design, (5) Research, (6) Transcribe, (7) Survey, (8) Graphic, and (9) Logo. As shown in Fig. 4 and Fig 5, we have

$$
\overline {{D e s i g n}} = (2, 2, 0, 2, 0, 0, 0, 1, 1), \quad \overrightarrow {C _ {l}} = (7, 7, 0, 7, 0, 0, 0, 3, 4).
$$

The similarity between a contributor $C _ { i }$ and the task type ―Design,‖ ????????????????????(?? , ????????????), can be

$$
\text { obtained   as } \frac {1 4 + 1 4 + 1 4 + 3 + 4}{\sqrt {2 ^ {2} + 2 ^ {2} + 2 ^ {2} + 1 ^ {2} + 1 ^ {2}} \sqrt {7 ^ {2} + 7 ^ {2} + 7 ^ {2} + 3 ^ {2} + 4 ^ {2}}} \cong 0. 9 9 8.
$$

![](/api/attachments/937SESPW/fulltext/images/d8006ffefd32accb0ab25301c6ddd2e35604cdd86865a2ffddd50c87e65236c4.jpg)  
Fig.4. Vector of Design  
Fig.5. Vector of C

Finally, a contributor’s interest in a task of type T can be measured as:

$$
\text { ContributorInterest } (C _ {i}, T) = \text { SocialInterest } (C _ {i}, T) \times \text { Similarity } (C _ {i}, T).\tag{3}
$$

Contributors’ capacity. We need to evaluate the capacity of contributors, as a qualified contributor should be able to complete tasks $\therefore a ^ { \prime } \mathrm { e v } _ { \downarrow } ^ { \phantom { \dagger } }$ of quality acceptable to the requester. In this research, we judge a contributor’s capacity through related background analysis, including: (1) educational background: analyze the education level of people who responded to articles published by keywords in the article and $\boldsymbol { \cdot } ^ { \ s _ { 1 } }$ people's responses to the article. Users might treat some of their background information as confidential and not display it on a social network. If the capacity of a contributor is low, suggesting that he/she might not be able to complete the task, we will not recommend this contributor as his/her contribution is unlikely to be acceptable to the requester. A contributor $C _ { i } \mathrm { ' s }$ capacity in a specific task type T is measured as:

$$
C o n t r i b u t o r C a p a c i t y (C _ {i}) = E n g l i s h (C _ {i}) + E d u c a t i o n (C _ {i}) + C o m p u t e r (C _ {i})\tag{4}
$$

$$
E n g l i s h (C _ {i}) = \left\{ \begin{array}{c c} 0, & \text {not at all.} \\ 1, & \text {fair.} \\ 2, & \text {fluency.} \end{array} \right.\tag{5}
$$

$$
E d u c a t i o n (C _ {i}) = \left\{ \begin{array}{l l} 0, & m i d d l e s c h o o l. \\ 1, & h i g h s c h o o l. \\ 2, & u n i v e r s i t y d e g r e e. \end{array} \right.\tag{6}
$$

$$
C o m p u t e r (C _ {i}) = \left\{ \begin{array}{l l} 0, & \qquad \text {not at all.} \\ 1, & \qquad \text {fair.} \\ 2, & \qquad \text {know well.} \end{array} \right.\tag{7}
$$

Note that the value of ??????????????????????????????????????(??<sub>??</sub>) should be normalized to a value between 0 and 1.

Contributors’ motivation. It is important to identify the motivations of contributors and why they participate in task-oriented crowdsourcing. According to the study conducted by [4], the primary motivation for a contributor is a financial incentive, with learning and leisure also listed. These three motivations are defined as ???????????????????? $( C _ { i } )$ . To consider the different motivations for crowdsourcing contributions, we calculate ??????????????????????????????????????????, the weights of which are differentiated with respect to different contributors.

## ???????????????????? $( C _ { i } ) \in$ \*????????????, ????????????????, ??????????????+

(8)

## 3.2.2. Contributors’ history analysis

The contributors’ performance histories reflect their ability to accomplish various kinds of tasks, so this information is important for identifying valuable contributors. We collect and analyze contributors’ activities in the task-oriented crowdsourcing platforms. We analyze a contributor’s performance records, such as the number of tasks browsed through, the number of tasks selected, the number of tasks completed, and the number of tasks accepted.

Contributors’ search history. The search histories of a contributor reflects his/her interest in the pages they have browsed. If a contributor has browsed information relevant to a task, it indicates that he/she may be interested in this or similar tasks.

Contributors’ performance history. We analyze these features to measure the extent of the contributor’s interest in tasks and his/her capability to undertake them. If a contributor has selected a task to work on, it indicates that they may prefer to work on similar tasks. If a contributor has completed a task, it indicates that they may have the ability to complete similar tasks. If the requester has accepted the work done by the contributor, it indicates that the contributor is likely to produce output of good quality. As illustrated in

Fig. 4, the popularity of each task and each contributor can be expressed on a 5-point integer scale (from 0 to 4) as shown in the following matrix:

0: The contributor does not browse the task information. Get 0 point.

1: The contributor browses the task information. Get 1 point.

2: The contributor selects the task to work on. Get 2 point. If a contributor has selected the task to work on, it indicates the contributor may prefer to work on similar tasks.

3: Contributor completes the task. Get 3 point. If a contributor has completed the task, it indicates the contributor may have the ability to complete similar tasks.

4: The contributor's contribution is accepted by the requester. Get 4 point. If the requester has accepted the work done provided by the contributor, it indicates the contributor is likely to have the ability to provide output of good quality.

<table><tr><td></td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td></tr><tr><td>C1</td><td>3</td><td>0</td><td>4</td><td>1</td><td>0</td></tr><tr><td>C2</td><td>1</td><td>3</td><td>0</td><td>0</td><td>0</td></tr><tr><td>C3</td><td>0</td><td>0</td><td>2</td><td>0</td><td>4</td></tr><tr><td>C4</td><td>4</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>C5</td><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td></tr></table>

Fig. 4. The example of contributor–task matrix

The value of $M a r t r i x ( C _ { i } , T _ { x } )$ epresents the performance of contributor $C _ { i }$ on task $T _ { x }$ in the $T _ { x } \in T$ . For example, the value of ?????????????? $( C _ { 3 } , T _ { 5 } )$ is 4. Using the matrix of the contributor’s past performance, we compute the performance of contributor $C _ { i }$ on a task of type T as:

$$
\text { ContributorHistory } (C _ {i}, T) = \sum_ {T _ {x} \in T} \text { Matrix } (C _ {i} T _ {x}) / \text { Number } (T)\tag{9}
$$

where the value of $C o n t r i b u t o r H i s t o r y ( C _ { i } , T )$ will also be normalized from 0 to 1 by min-max normalization.

## 3.3. Social influence analysis module

In this module, we analyze social influence based on social affiliation analysis, which measures the influence of other contributors on a contributor’s interests, and social closeness analysis, which measures social influence on a contributor’s willingness to contribute to a task.

## 3.3.1. Social affiliation analysis

A social affiliation network can be built from a group of contributors with a social relationship who share similar tastes in tasks. If a contributor is interested in a task and shares it with his/her friend (also a contributor), social influence will take effect and arouse similar interest in his/her friend [20].

However, not all friends of a contributor will have the same power to arouse his/her interest. Take the example in

Fig. 5, in which contributors A and C are contributor B’s friends, and contributor B has a closer relationship (represented by the bold line) with contributor C. When contributors A and C like different tasks (D and E), and respectively share their interests, contributor B will be more interested in task E because of the stronger influence of contributor C.

![](/api/attachments/937SESPW/fulltext/images/bfca35013073be750ba405d4c5b8d081e925a606fdaa04fbaf9df3da4c91822b.jpg)  
Fig. 5. The example of social affiliation network

Therefore, we can evaluate the level of social influence that friends may exert on a contributor. First, we denote ???????????????? $i  ( a _ { 1 } , f )$ to represent the interaction intensity between contributors $C _ { i }$ and friend ?? in a social network. The ?????????????????????? $( C _ { i } , f )$ is measured as follows: (1) $T a g ( C _ { i } , f )$ means the accumulated number of comments and posts that two users have been tagged together (e.g. statuses, check-ins, and photos), (2) Comment $( C _ { i } , f )$ means the number of comments written by the two users in the same post, (3) $L i k e ( C _ { i } , f )$ mean the aggregated occurrences of likes given by the two users in comments and posts (e.g. statuses, check-ins, and personal photos) and (4) the number of mutual friends, which we denote as ???????????????????????? $( C _ { i } , f )$

The interactions between contributor $C _ { i }$ and friend f are computed as:

?????????????????????? $( C _ { i } , f )$

$$
= \operatorname{Tag} \left(C _ {i}, f\right) + \operatorname{Comment} \left(C _ {i}, f\right) + \operatorname{Like} \left(C _ {i}, f\right) + \operatorname{MutualFriend} \left(C _ {i}, f\right)\tag{10}
$$

We would use Jaccard similarity coefficient to compute the interaction intensity in various activities. For example, Contributor $C _ { B }$ has 8 Tags and friend contributor $C _ { C }$ ,has 7 Tags, and they have 3 common Tags, so we can know $\mathrm { T a g } ( C _ { \cal B } , C _ { \cal C } ) = J a c c a r d \big ( T a g _ { C _ { \cal B } } , T a g _ { C _ { \cal C } } \big ) = \textstyle { \frac { 3 + 1 } { 8 + 7 - 3 } } = 0 . 3 3 ,$ Analogously, comment, like, and mutual friends apply the same calculation method.

We have recorded the performance histories of contributors on the crowdsourcing platform. When a contributor browses the content of a task or selects tasks to work on, it suggests that his/her close friends may also be interested in them. Let us assume that a contributor’s friend $C _ { x }$ works on a task $T _ { j }$ and that contributor $C _ { i }$ browsed task ??<sub>??</sub>. We measure the interest of contributor $C _ { i }$ interest in task $T _ { j }$ as:

## ??????????????????????????????????(??<sub>??</sub>, ??<sub>??</sub>)

$$
= w \times \frac {\sum_ {C _ {x} \in F r i e n d s (C _ {i}) ^ {*}} W o r k \left(C _ {x} , T _ {j}\right) \times I n t e r a c t i o n (C _ {i} , C _ {i})}{| F r i e n d s (C _ {i}) |} + (1 - w) \times B r o w s e \left(C _ {i}, T _ {j}\right).\tag{11}
$$

where $W o r k ( C _ { x } , T _ { j } )$ and ???????????? $\left( C _ { i } , T _ { j } \right) \in \langle \langle \mathscr { n } _ { , 1 } \rangle ,$ represent whether or not the contributor’s friend $C _ { x }$ works on task $T _ { j }$ , and whether or not contributor $C _ { i }$ browses task ?? . ??????????????(?? ) denotes the set of friends of contributor $C _ { i }$

## . 3.3.2. Social closeness analysis

We compute the social closeness between a contributor and a requester through the type of social connection. If a contributor has a close relationship with the requester, he/she will be more likely to accept a task invitation. The social closeness between contributor $C _ { i }$ and requester $R _ { k }$ is computed as follows:

$P a t h ( C _ { i } , R _ { k } )$ denotes a set that contains all the paths between contributor $C _ { i }$ and requester $R _ { k }$ Each social path has a set of links, denoted as ????????(??, ??), and each link connects two people through their ?????????????????????? $\left( P _ { i } , P _ { j } \right)$ . Therefore, we can denote $P a t h s ( C _ { i } , R _ { k } )$ and ?????????? $( P a t h _ { n } ( C _ { i } , R _ { k } ) )$ as:

$$
P a t h s (C _ {i}, R _ {k}) = \{P a t h _ {1} (C _ {i}, R _ {k}), P a t h _ {2} (C _ {i}, R _ {k}), \dots , P a t h _ {n} (C _ {i}, R _ {k}) \}\tag{12}
$$

$$
\text { Links } (P a t h _ {n} (C _ {i}, R _ {k}))\tag{13}
$$

$$
= \{L i n k _ {1} (P a t h _ {n} (C _ {i}, P _ {2})), L i n k _ {2} (P a t h _ {n} (P _ {2}, P _ {3})), \dots , L i n k _ {z} (P a t h _ {n} (P _ {z}, R _ {k})) \}
$$

Next, we can compute the social closeness between contributor $C _ { i }$ and requester $R _ { k }$ . This can be estimated as:

$$
SocialCloseness(C_{i},R_{k}) = Max\{\prod_{\substack{Links(Path_{n}(C_{i},R_{k}))\in Path(C_{i},R_{k})}}Interaction\big(P_{i},P_{j}\big)\}\tag{14}
$$

We utilize social influence theories to compute the social relationships between contributors and requesters, and thus ensure the suitability of a contributor through the influence of social affiliations and social closeness. Social affiliation represents a group of contributors with social relationships of having similar preferences in the task [19]. If a contributor is interested in a task and shares it with his/her friend (also a contributor), social influence will take effect and arouse his/her friend’s similar interest. Social affiliation is a measure integrated from equation (10) and (11). Social closeness represents the social intimacy between the contributor and $\bf \Pi _ { \mathrm { - } \mathrm { ~ a ~ } } ^ { \mathrm { + 1 } } \cdot \mathrm { r } \mathrm { c . , u e s t e r }$ [10]. If the contributor has a close relationship with the requester, he/she equation will be more likely to accept the task invitation. Social closeness is a measure integrated from equation (12) - (14). Since social affiliations and social these two indicators in the overall evaluation of social influence impact, we add the concept of weight, alpha and beta, and evaluated the social influence through the linear combination two indicators.

Finally, following normalization, we can calculate the influence of the social closeness between contributor $C _ { i }$ and requester $R _ { k ^ { 1 } }$ $S o c i a l l n f l u e n c e ( C _ { i } , \textsc { p } _ { \nu } , \textsc { r } _ { \cdot } ) = a S o c i a l A f f i l i a t i o n ( C _ { i } , T _ { j } ) + \beta S o c i a l C l o s e n e s s ( C _ { i } , R _ { k } )$ (15) where $\alpha + \beta = 1$

## 3.4. Task-oriented crowdsourcing recommendation module

After collecting and analyzing related personal and social information in various analysis modules, we can program the recommendation engine to generate lists of potential contributors. First, we evaluate whether a task is valuable in terms of the reward and execution time. Next, the mechanism identifies appropriate contributors for whatever task is specified by considering the weight given to each of a requester’s preferences. Finally, we generate a list of recommended contributors for the requester.

## 3.4.1. Crowdsourcing task analysis

We compute the rewards and execution times of all tasks belonging to the same task type. To examine whether a task’s reward is sufficient to attract contributors, particularly those whose motivation is financial, we measure the value of a task as:

$$
\operatorname{TaskValue} \left(T _ {j}, T\right) = \frac {\text {AverageExecutionTime*Reward} \left(T _ {j}\right)}{\text {AverageReward*ExecutionTime} \left(T _ {j}\right)},\tag{16}
$$

where $T _ { j }$ is the task belonging to type ??. ???????????? $( T _ { j } )$ and ?????????????????????????? $( T _ { j } )$ denote the task’s reward and approximate execution time, respectively. ?????????????????????????? and ???????????????????????????????????????? are computed for all tasks of the same $\mathsf { 1 / p e } \mathrm { ~ . ~ }$ $T a s k V a l u e ( T _ { j } , T )$ is normalized.

Following this, we can compute contributor $C _ { i } \mathrm { ' s }$ preference for task $T _ { j }$ as:

?????????????????????????????????????????? $\left( C _ { i } , T _ { j } \right) =$

(17)

???????????????????????????????????????? $( C _ { i } , T ) +$ ????????????????????????????????????????(?? ) + ???????????????????? $\left( T _ { j } , T \right)$ \_

where $\alpha + \beta + \gamma = 1$

As people have different motivations for becoming contributors, the weight of preferences in their profiles are determined by $C _ { i } ^ { ~ \gtrless }$ motivations for crowdsourcing as ???????????????????? $( C _ { i } )$ . For example, a contributor whose primary motivation is financial will give more weight to tasks of higher value, whereas the weight of a contributor’s interest in less financially rewarding tasks will be higher if motivated by leisure. The mechanism we propose will adjust the weights and find different contributors according to the interest, capacity and value of a task to the contributors.

## 3.4.2. Suitability criteria aggregation

We will determine the weight of different motivations according to the different reasons for recommendations. We compute the weight of the requester’s three criteria for finding contributors, including: (1) contributor preference, (2) contributor history, and (3) social influence. We adopt the analytic hierarchy process ([AHP]; [33]) to organize and analyze complex decisions with multiple criteria. We have three criteria in the decision hierarchy structure, so we need to have ${ \pmb n } ( { \pmb n } + { \pmb 1 } ) * { \pmb 2 }$ pairwise comparisons, where n=3. Using AHP, we build a matrix $M _ { P H S }$ to determine the pairwise weight ratios, where P represents contributor preference, H represents contributor history, and S represents social influence. Each element $G _ { i j }$ represents the relative weight of criterion i in terms of criterion $j .$

$$
M _ {P H S} = \left[ \begin{array}{c c c} 1 & G _ {P H} & G _ {P S} \\ \frac {1}{G _ {P H}} & 1 & G _ {H S} \\ \frac {1}{G _ {P S}} & \frac {1}{G _ {H S}} & 1 \end{array} \right]\tag{18}
$$

The upper triangle is the relative weight between each two criteria and the value of the lower triangle is the upper triangle’s reciprocal. That is to say, $\begin{array} { r } { G _ { i j } = \frac { 1 } { G _ { i j } } . \mathrm { T ^ { 1 } \sim r e a ^ { \cdot } v r e } } \end{array}$ , we can define a set of decisions and consider the weight of each decision in requester $k \mathbf { \bar { s } }$ task-oriented crowdsourcing as $G _ { P H S } ( k )$ , which we denote as:

$$
G _ {P H S} (k) = \{G _ {P H} (k), G _ {P S} (k), G _ {H S} (k) \}\tag{19}
$$

Next, after the constructing pairwise matrix, we can get weights of different criteria by eigenvectors because the pairwise matrix is not usua th e same as the consistency matrix and apply the ANC method, which can get higher accuracy than other methods [6]. For a requester k, we define a weight set that contain three different criteria as $W _ { P H S } ( k )$ ), which can be estimated as:

$$
W _ {P H S} (k) = \{W _ {P} (k), W _ {H} (k), W _ {S} (k) \}\tag{20}
$$

$$
W _ {\alpha} (k) = \frac {1}{3} \sum_ {\gamma = 1} ^ {3} \frac {G _ {\beta \gamma} (k)}{\sum_ {\beta = 1} ^ {3} G _ {\beta \gamma} (k)}, \forall W _ {\alpha} (k) \in W _ {P H S} (k), \forall G _ {\beta \gamma} (k) \in G _ {P H S} (k)\tag{21}
$$

Finally, using the weighted value obtained for the three criteria, we can measure the likelihood that contributor $C _ { i }$ will be recommended for task $T _ { j }$ initiated by requester $R _ { k }$ . We can calculate the value of $S u i t a b i l i t y { \left( { C _ { i } } , { T _ { j } } , { R _ { k } } \right) }$ by aggregating the scores obtained for contributor preference, history, and social influence:

$$
\begin{array}{r l} & S u i t a b i l i t y \big (C _ {i}, T _ {j}, R _ {k} \big) = W _ {P} (i) \times C o n t r i b u t o r P r e f e r e n c e \big (C _ {i}, T _ {j} \big) \\ & \qquad + W _ {H} (i) \times C o n t r i b u t o r H i s t o r y \big (C _ {i}, T _ {j} \big) + + W _ {S} (i) \times S o c i a l I n f l u e n c e (C _ {i}, R _ {k}) \end{array}\tag{22}
$$

## 3.4.3. Contributor list generation

After calculating and ranking the contributor’s suitability, we can generate a list of recommended contributors for the task requester. A recommendation includes six types of contributor information: (1) name, (2) picture, (3) social relationship with the contributor, (4) individual preferences, (5) performance history, and (6) personal Facebook website link. Contributors will then receive a task invitation from the requester, which will include information regarding (1) type, (2) requester’s name, (3) description of the task, (4) social relationship with the requester, (5) reward, and (6) approximate execution time.

## 4. Experiment

In this section, we describe the experimental process for verifying the proposed mechanism. In collecting social information, we use Facebook (the most popular social network in the world) to collect users' social information. In terms of crowdsourcing tasks, we chose Amazon Mechanical Turk and Taskcn as our major references for task-oriented crowdsourcing platforms. Amazon Mechanical Turk provides access to hundreds of thousands of tasks that can be completed to earn rewards. There intelligence tasks (HITs) from which contributors can choose per day. Taskcn is one of the largest websites in China, and represents Chinese culture through its use of a Chinese interface for all of its site content. It has gathered millions of users since it was launched a few years ago (crowdsourcing.org).

## 4.1. Experimental process

There were five main steps in the experimental process:

Step 1: We implemented the social recommendation mechanism by building a web-based system and shared the system in task-oriented crowdsourcing clubs on Facebook, inviting clubs users to join our experiment to construct a social network. Due to its privacy policy, users were asked to log in to their personal accounts via Facebook’s authentication service to enable us to collect their personal and social information. We then asked users to complete a questionnaire evaluating the weight given to the different criteria, including contributors’ preferences, history, and social influences.

Step 2: Next, the requester uploaded his/her task file or link and input the relevant information in the system, including task name, task type, number of contributors, approximate execution time, reward, and task description.

Step 3: After the requester created a task, we classified it through the constructed type tree. Next, we used the comparative 7-level scale to create the AHP questionnaire on personal criteria weighting. For each potential contributor, we analyzed preferences, history, and social influences based on the data from the crowdsourcing and social networking platforms to calculate their suitability score.

Step 4: Based on the ranked suitability scores for all contributors, the system generated a list of recommended contributors for the requester. Following this, the requester could select and invite contributors to work on his/her task. After the contributors received the task invitation, they were asked to complete feedback questionnaires to evaluate their suitability, liking for the task, and willingness to participate in response to the invitation.

Step 5: After contributors submitted their contributions, we asked the task requester to complete questionnaires to assess whether the contributions were acceptable. This feedback was to evaluate the success of the recommendations.

## 4.2. Data collection

## 4.2.1. User profile

In total, 138 users participated in the experiments and a total of 518 contributions were check-ins, 12,548 tags, 271,278 likes, 22,657 comments, and 25,912 fan pages ―liked,‖ with the average number of friends per user being 545. Due to the privacy constraint, we can only collect the social information from those users who are willing to authorize us to do that. Snowball sampling is a feasible method for use when studying issues concerning social networks [2], and thus this method was used to construct our experiment. Comparing with some existing works on a field study [15],[28],[37], the sample size in the experiment is above the average level. The gender distribution of users was 78 males (57%) and 60 females (43%), and they were aged 18 to 55 years old. In terms of English ability, 36 (26%) were fluent, 93 (67%) were fair, and 9 (7%) had none. Concerning educational background, 66 (48%) held a master’s degree, 71 (51%) had a university degree, and 1

(1%) had a high school qualification. For computer ability, 108 (73%) were proficient, 38 (26%) were fair, and 2 (1%) had none. Motivation for participating in task-oriented crowdsourcing was as follows: 102 (74%) reward, 11 (8%) learning, and 25 (18%) leisure. We also analyzed users’ past experiences in task-oriented crowdsourcing, including their activities and the rewards received. All users had taken part in relevant activities for task-oriented crowdsourcing, such as sharing content or helping people to design things on Facebook. There were 113 users who had been both contributors and requesters, and 25 who had only been contributors. In addition, there were 62 users who had not received a reward, 9 who had received money, 56 who had received virtual points, and 11 who had received money and virtual points.

Table 1. Summary of dataset

<table><tr><td>Title</td><td>Value</td></tr><tr><td>Number of participants</td><td>138</td></tr><tr><td>Number of posts</td><td>5,579</td></tr><tr><td>Number of check-ins</td><td>1,588</td></tr><tr><td>Number of tags</td><td>12,548</td></tr><tr><td>Number of “likes”</td><td>271,278</td></tr><tr><td>Number of comments</td><td>22,657</td></tr><tr><td>Number of fan pages “liked”</td><td>25,912</td></tr><tr><td>Average number of friends of users</td><td>545</td></tr></table>

## 4.2.2. Task profile

In our experiment, the 39 tasks were classified into 13 different types, as shown in Table 2 and referenced the categories of two famous task-oriented crowdsourcing platforms (Amazon Mechanical Turk and Taskcn).

Table 2. Task type classification

<table><tr><td>Type</td><td>Graphic Design, Logo Design, Visual Identity Design, Media to Text, Graphics to Text, Document Handling, Image Handling, Research, Spread, Software Development, Photography, Classification, Survey</td></tr></table>

![](/api/attachments/937SESPW/fulltext/images/18ed861758943034e537b7d3429e1624c9d8548c1c7273ac76ce9d9ce755e7f1.jpg)  
Fig. 6. Distribution of classification type

During the experiments, the requesters set their task-related information and chose one type. We computed the similarity between the task type and contributors’ interests. These tasks could be principally classified as professional (Graphic Design, Logo Design, Visual Identity Design, Research, Software Development, and Photography) and non-professional (Media to Text, Graphics to Text, Document Handling, Image Handling, Spread, Classification, and Survey).

## 4.2.3. Criteria weight computing

As task types were principally classified as professional and non-professional, we analyzed the importance of the three factors—contributor preference, contributor history, and social influence—in relation to professional and non-professional types, respectively. After users completed the questionnaire, we used AHP to analyze users’ preferences with respect to different types. The results are shown in Table 3. The default weight was used if a user did not specify his/her preferences among our criteria.

Table 3. System default weight for two major types

<table><tr><td></td><td>Contributor preference</td><td>Contributor history</td><td>Social influence</td></tr><tr><td>Professional</td><td>0.363</td><td>0.344</td><td>0.293</td></tr><tr><td>Non-professional</td><td>0.304</td><td>0.324</td><td>0.372</td></tr></table>

Consistent with our hypothesis, the weight of contributor preferences in professional type tasks was more important than in non-professional types. In contrast, the weight of social influence in non-professional type tasks was higher than in professional types. This reflects the fact that when a task is easier, a requester’s friends will be more willing to help and will have greater capability.

## 4.2.4. Suitability computation

For the purpose of verifying the effectiveness of the recommendations generated by the proposed mechanism, we compared the performance of the mechanism with four other benchmark recommendation methods.

(1) Random recommendation model: This simply recommends contributors at random.

(2) Content-based recommendation model: In a content-based recommendation system, keywords are used to describe the items and a user’s profile is built to indicate the type of item. This approach recommends items similar to those that the user enjoyed in the past, meaning that the factors contributor preference and contributor history (CP+CH) are considered in recommendations.

(3) Collaborative-based recommendation model: This approach analyzes users’ behavior, activities, and preferences, and makes recommendations based on aspects that similar users or users’ friends like, as social influences include social affiliations. Therefore, the factors contributor preference and social influence (CP+SI) are considered in recommendations.

(4) General platform recommendation model: On the whole, most task-oriented crowdsourcing platforms recommend contributors base d on u sers past performance, and the frequency of cooperation between a contributor and a requester. As social influence includes the type of social closeness between a contributor and a requester, the factors contributor history and social influence (CH+SI) are considered in recommendations.

(5) Social crowdsourcing task (SCT) recommendation model: Our proposed SCT recommendation mechanism comprehensively considers the factors contributor preference, contributor history, and social influence $\left( \mathrm { C P + C } \right) \left. \mathrm { { 1 + S I } } \right)$ in recommendations.

## 5. Results and evaluation

The evaluation of the performance of the recommendation mechanism includes two parts: (1) contributor recommendations, evaluated by the requesters, and (2) task invitations, evaluated by the contributors.

## 5.1. Contributor recommendations

## 5.1.1. Accuracy of recommendations

We evaluated the accuracy of the proposed recommendation mechanism by reviewing the list of

contributors recommended. We measured the accuracy as:

$$
A c c u r a c y = \frac {\left| \varPhi_ {r e c o m m e n d l i s t \cap p i c k u p} \right|}{\left| \varPhi_ {r e c o m m e n d l i s t} \right|},\tag{23}
$$

where $\Phi _ { r e c o m m e n d e d l i s t }$ was the set of recommended contributors and <sub>?????????????????????? ???????? ∩ ????????????</sub> $\varPhi _ { \gamma }$ was the set of the contributors finally acquired by the requester. For example, if five contributors were recommended to the requester, and the requester chose four contributors to work on his/her task, the accuracy would be 80%.

We evaluated and compared the accuracy levels of the proposed SCT recommendation mechanism resulting from three different weighting combinations: (1) equal weighting, (2) default weighting, and (3) AHP weighting. Equal weighting assigns each component 1/3, whereas the default approach assigns weighting as shown in Table 3. Fig. 7 displays the accuracy levels of the proposed recommendation mechanism using the different weighting $\mathrm { a p _ { r } }$ roaches. T-test is a statistics method used to compare whether two sets of data are significantly different [36], [42]. We use t-test to verify whether the outcome of our proposed appro ach is s tatistically outperform the other benchmark approaches (e.g. Table 4), additional to the average performance (e.g. Fig. 7)

![](/api/attachments/937SESPW/fulltext/images/f5e6c084306e869b070f0a2c9186673202c2d98c5cb4d84372e0c0d37064bae2.jpg)  
Fig. 7. Accuracy of recommendation

As we can observe, the accuracy of the AHP weighting approach is better than the other approaches. As shown in Table 4, based on a paired-samples t-test used to verify the statistical differences and 95% confidence interval, the AHP weighting approach is also statistically better than the other two.

Table 4. Paired-samples t-test of the accuracy of different approaches

<table><tr><td>Paired Group</td><td>Mean</td><td>Std. Dev.</td><td>Std. Error</td><td>t</td><td>Sig.</td></tr></table>

<table><tr><td colspan="4"></td><td colspan="2">Mean</td><td>(2-tailed)</td></tr><tr><td rowspan="2">AHP</td><td>Equal</td><td>0.37170</td><td>0.12012</td><td>0.01215</td><td>7.487</td><td>0.000</td></tr><tr><td>Default</td><td>0.14573</td><td>0.13233</td><td>0.01753</td><td>3.857</td><td>0.143</td></tr></table>

## 5.1.2. Satisfaction with contribution

We further evaluated the requester’s satisfaction regarding the work produced by the contributors recommended by the proposed mechanism. In the design of the experiment, when the contributor completes the work, the system will ask the requester if he is satisfied with the performance of the contributor. We measured satisfaction regarding contributions as:

$$
\text { Satisfaction } = \frac {\left| \Phi_ {\text { recommended   list } \cap \text { pickup } \cap \text { application }} \right|}{\left| \Phi_ {\text { recommended   list } \cap \text { pickup }} \right|},\tag{24}
$$

where recommended list represents a list of contributors selected by the system. ―pickup‖ means that the requester selects the appropriate contributor from the recommended list. ―approve‖ indicates that the requester is satisfied with the performance of the contributor. We calculate the percentage of requesters to select contributors from our recommended list and approve their contributions to evaluate the requester’s satisfaction. $\Phi _ { r e c o r }$ ?????? ???????? ???????????? is the set of requesters who acquired contributors from the recommendation list and $\varPhi _ { \gamma }$ <sub>??????????????????????</sub> <sub>????????</sub> <sub>∩</sub> <sub>????????????</sub> <sub>∩</sub> <sub>??????????????</sub> is the set of requesters who acquired contributors from our recommendation list and approved their contributions. We compared the satisfaction levels for five models, including: (1) random recommendation, (2) content-based recommendation (CP+CH), (3) collaborative-based recommendation (CP+SI), (4) general platform recommendation (CH+SI), and (5) proposed SCT recommendation (CP+CH+SI). We then respectively examined the influence of each factor on the results in different models. The pseudo code of the satisfaction of different recommendation models is shown in Algorithm 1 and Fig. 8 shows the results of the satisfaction of different recommendation models.

Algorithm 1 Satisfaction of Contributions

Input: Factor={SI, CP, CH} , Requester list R

\* SI as Social Influence, CP as Contributor Preference, CH as Contributor History

Output: Satisfaction

1. For each Requester i do

2. Generate Contributor list for $i = \mathrm { S C T } ( S I _ { i } , C P _ { i } , C H _ { i } )$

$$
/ *
$$

$$
(C H _ {i}, S I _ {i}) ^ {*} /
$$

3. pickup(i) = Assign the task to the contributor from Contributor list for Requestor i

4. approve(i) = Requester i is satisfied with the contributors from pickup(i)

5. Satisfaction of requster $( i ) = \mathrm { \ a p p r o v e } ( i )$ pickup(??)<sup>⁄</sup>

6. End for

$= \Sigma i$ Satisfaction of requster(??) 7. Satisfaction number of requsters

## 8. Return Satisfaction

![](/api/attachments/937SESPW/fulltext/images/9bde60475e55c4ffe233cebd0652ff7126cedfae5ed1ab2efe4241da2a7dfc77.jpg)  
Fig. 8. Satisfaction with contribution

We can see that the proposed SCT recommendation model has the highest satisfaction levels of all models and types. Generally speaking, the satisfaction found for all of the models was higher in non-professional types. The reason for this may be attributed to the fact that non-professional tasks are generally easier to complete, meaning that requesters have a greater opportunity to appreciate the contributions. A paired-samples t-test demonstrated that our model is statistically better than the other models, as shown in Table

Table 5. Paired-samples t-test of satisfaction for different models

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Dev.</td><td>Std. Error Mean</td><td>t</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="4">SCT mechanism</td><td>Random</td><td>0.34663</td><td>0.07445</td><td>0.01297</td><td>24.213</td><td>0.000</td></tr><tr><td>Content-based</td><td>0.09458</td><td>0.08831</td><td>0.01351</td><td>7.343</td><td>0.000</td></tr><tr><td>Collaborative-based</td><td>0.14538</td><td>0.07329</td><td>0.01125</td><td>6.143</td><td>0.001</td></tr><tr><td>General platform</td><td>0.08235</td><td>0.07337</td><td>0.01043</td><td>6.321</td><td>0.000</td></tr></table>

## 5.2. Task invitation

In addition, we evaluated whether the contributors were suitable for the tasks we recommended. We received contributor feedback through a questionnaire to evaluate the suitability and usefulness of the task crowdsourcing invitations. We also computed contributors’ willingness to participate based on records of the task invitations that they accepted and rejected.

## 5.2.1. Fitness of task invitation

We assessed contributor suitability via the question “To what extent do you think the task invitation fits you?” employing a scale of 1 to 5. Fig. 9 shows the fitness levels of task invitations for different models and task types.

![](/api/attachments/937SESPW/fulltext/images/341901bcbe8a50d3671c89cecf77543d97c9bb7a113bc266be0253975150e4fc.jpg)  
Fig. 9. Fitness of task invitation

From Fig. 9 we can observe that the proposed SCT recommendation model outperforms other benchmark models. A paired-samples t-test was used to verify the statistical difference of suitability for different models. According to Table 6, our proposed model yields higher levels of suitability than other models.

Table 6. Paired-samples t-test of different models for fitness

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Dev.</td><td>Std. Error Mean</td><td>t</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="4">SCT mechanism</td><td>Random</td><td>1.74663</td><td>0.18452</td><td>0.03497</td><td>15.233</td><td>0.000</td></tr><tr><td>Content-based</td><td>0.82458</td><td>0.21313</td><td>0.04491</td><td>6.464</td><td>0.000</td></tr><tr><td>Collaborative-based</td><td>0.80538</td><td>0.23296</td><td>0.03725</td><td>7.423</td><td>0.000</td></tr><tr><td>General</td><td>0.83235</td><td>0.22371</td><td>0.03243</td><td>7.211</td><td>0.000</td></tr></table>

## 5.3.2. Liking for task invitation

We also assessed user suitability by asking “To what extent do you like the task invitation?”

Fig. 10 shows the results for different models and types.

![](/api/attachments/937SESPW/fulltext/images/310c05bfd353c1225e02f3e9f0cdd9159c96b7614f5f7f44edbb29a319e486cb.jpg)

## Fig. 10. Liking for task invitation

The random model has the lowest value with regard to liking for task invitations and the proposed SCT recommendation model has the highest. The results of a paired-samples t-test shown in the other models.

Table 7. Paired-samples t-test of different models for liking task invitations

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Dev.</td><td>Std. Error Mean</td><td>t</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="4">SCT mechanism</td><td>Random</td><td>1.94514</td><td>0.20014</td><td>0.03475</td><td>14.172</td><td>0.000</td></tr><tr><td>Content-based</td><td>0.75453</td><td>0.28465</td><td>0.04178</td><td>8.641</td><td>0.000</td></tr><tr><td>Collaborative-based</td><td>0.32813</td><td>0.31642</td><td>0.04238</td><td>6.961</td><td>0.000</td></tr><tr><td>General</td><td>0.78411</td><td>0.27531</td><td>0.03875</td><td>7.123</td><td>0.000</td></tr></table>

## 5.3.3. Willingness to take up task invitation

In this section, we computed the value of willingness to accept the task invitation as:

$$
W i l l i n g n e s s = \frac {\left| \Phi_ {t a s k i n v i t e d \cap a c c e p t e d} \right|}{\left| \Phi_ {t a s k i n v i t e d} \right|},\tag{25}
$$

where $\Phi _ { t a s k i n v i t e d }$ is the set of task invitations and $\Phi _ { t a s k }$ <sub>??????????????∩????????????????</sub> is the set of the tasks that the contributors accepted.

Fig. 11 shows the results for willingness levels in relation to different models and task types.

![](/api/attachments/937SESPW/fulltext/images/2346ec87787f098a9b54c86a60654d40384c741c6da02109959b080d1c69c525.jpg)  
Fig. 11. Willingness to take up task invitations

Fig. 11 shows that the proposed SCT recommendation model yields the highest level of willingness to take up task invitations. Contributors’ willingness is quite high across all models, except for the random category for non-professional types, because non-professional tasks do not need special abilities. As shown in Table 8, the paired-samples t-test also verifies that our proposed model outperforms other benchmark models.

Table 8. Paired-samples t-test of different models for willingness

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Dev.</td><td>Std. Error Mean</td><td>t</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="4">SCT mechanism</td><td>Random</td><td>0.34413</td><td>0.08451</td><td>0.01372</td><td>31.103</td><td>0.000</td></tr><tr><td>Content-based</td><td>0.08612</td><td>0.07934</td><td>0.01194</td><td>8.132</td><td>0.000</td></tr><tr><td>Collaborative-based</td><td>0.09538</td><td>0.08219</td><td>0.01225</td><td>7.812</td><td>0.000</td></tr><tr><td>General</td><td>0.09234</td><td>0.07473</td><td>0.01104</td><td>8.512</td><td>0.000</td></tr></table>

## 6. Discussion and conclusion

Task-oriented crowdsourcing has become a trend in recent years, with both individuals and businesses increasingly using crowdsourcing to help them accomplish tasks. In this paper, we have proposed a social recommendation mechanism that uses social networks to discover capable contributors with high levels of willingness to participate in crowdsourcing tasks. To infer individual preferences, capabilities, and willingness to contribute, we collected and analyzed related social information and performance histories from social media and crowdsourcing platforms. The

task-oriented crowdsourcing recommendations were derived based on three aspects: (1) contributor preference, composed of contributor’s interests, abilities, and motivation related to participation in task-oriented crowdsourcing, (2) contributor history, namely past participation and performance in crowdsourcing activities, and (3) social influence, entailing social affiliations with tasks and social closeness between a contributor and the requester. Finally, we identified suitable contributors and considered these key factors using the AHP as the weighting method for criteria. The experimenta results have shown that the proposed social recommendation mechanism outperforms other benchmark recommendation methods in terms of accuracy of recommendations, satisfaction with contributors to participate. The proposed mechanism can be used to help crowdsourcing requesters find suitable contributors and establish long-term partners task-oriented crowdsourcing market.

## 6.1. Research contributions

perspective, we designed an effective recommendation system for a task-based crowd outsourcing. According to the experimental results, we have proved that our system can help the person initiating the task find the right human resources more simply and easily, thereby helping the two parties establish a long-term cooperative relationship and create a win-win result. Second, from a methodological perspective, social networks are becoming more and more important in our lives and in the most popular advertising media for companies, but few studies have proposed task-oriented crowdsourcing social-based recommendations mechanism. We consider the factors of contributor preference, contributor history, and social degree to recommend tasks to suitable contributors and find that use the three factors at the same time can provide the perfect results for recommendation. Third, from the empirical perspective, by analyzing the integrated the user behavioral data from crowdsourcing and social networking platforms, we prove that a system incorporating the factors of contributor preference, contributor history, and social degree has great performance on recommendation accuracy, satisfaction of recommendation system and contributor’s fitness, likeness and willingness. Lastly, from the practice perspective, the existing crowdsourcing platforms (such as iStockPhoto, Taskcn, InnoCentive, and Amazon's Mechanical Turk) only provide a platform for contributors and requesters. High search costs make it difficult for contributors to find suitable tasks closely match their personal preferences and abilities such that the efficiency and quality of crowdsourcing are seriously deteriorated. The proposed social task-oriented crowdsourcing recommendation mechanism can attract more requesters and contributors to collaborate in the crowdsourcing market. Valuable long-term partnerships can be established to create value for the crowdfunding platform and all participants.

## 6.2. Research limitations

There are, however, some limitations to our research. First, our proposed mechanism gathers related social information from Facebook, but there are other popular social media sites, such as Twitter and Instagram, which we could use in the future to collect and analyze further user information. Second, our research relied heavily on social media activities to keep track of users’ online behavior based on search history dat a. Reco mmendation performance may suffer when analyzing data from new users or those with few or perhaps no activities on social networks. Third, some private capacity information such as language ability, education background, computing ability might not available online. For the capacity information not explicitly expressed, we might extract relevant information to predict it. Fourth, our mechanism st ill has a cold start problem, as it needs a sufficient number of users to collect and analyze user behavior data and information on social interactions. Finally, due to constraints in terms of time and the platform chosen for our experiment, the sample size of participants was smaller than the actual user population of task-oriented crowdsourcing. The performance of recommendations could be improved by increasing the network size.

## 6.3. Future studies

There are several research issues that could be further studied. First, although we examined several types of social activity through social networks, we did not include social interactions such as pokes, reactions, frequency of messages or events, etc. Social networks establish and connect people in the real world as well as virtual world. People can interact in social networks through various social activities. In the future, we could analyze more types of social interactions to assess the socia influence. Second, many social media provide extensions to the likes function, called "Reactions". In our recommendation system, we only use like to indicate users who like certain things. We believe that other types of reactions can represent different emotional levels of liking or even negative emotions, such as angry reactions. Currently, there is not enough response data to analyze or calculate detailed sentiment on social media. We can incorporate these factors for sentimental analysis in the future to enhance user preferences. Third, in this research, we mainly conduct experiments on the platforms Facebook and crowdsourcing platform Amazon Mechanical Turk and Taskcn. There are other social networking platforms with community services and many crowdsourcing platforms that provide different types of task. If our system were able to integrate different platforms, we could gather richer information and enhance the accuracy of the recommendation mechanism. Lastly, with the rapid development of Smartphones, mobile crowdsourcing has become a new trend. The proposed system could be combined with a mobile platform to provide real-time crowdsourcing tasks and attract more requesters., some other factors (such a s context awareness and location suitability) could be considered further in the recommendation mechanism. These factors could improve accuracy levels and increase the richness of the task mechanism through a more comprehensive information analysis.

## Acknowledgments

This research was supported by the Ministry of Science and Technology of Taiwan under grant MOST106-2410-H-009 -021.

## Author statement

Yung-Ming Li: Methodology, Formal analysis, Investigation, Data Curation, Writing - Review & Editing, Visualization, Supervision, Project administration, Funding acquisition.

Chin-Yu Hsieh: Conceptualization, Experiments, Formal analysis, Investigation, Validation, Writing.

Lien-Fa Lin: Conceptualization, Methodology, Formal analysis, Investigation, Validation, Writing.

Chi-Hsuan Wei: Conceptualization, Experiments, Investigation, Validation, Resources, Data Curation, Writing - Original Draft

## Reference

[1] T. Ahmed, C.C. Brumbaugh, One foot out of the nest: how parents and friends influence social perceptions in emerging adulthood, Journal of Adult Development 21 (3) (2014) 147-158.

[2] Y. Y. Ahn, S. Han, S. Moon, H. Jeohg, Analysis of topological characteristics of huge online social networking services. Proceedings of the 16th International ACM Press Conference on World Wide Web, New York, USA, 2007, pp. 835–844.

[3] A. Bagherjeiran, R. Parekh,. Combining behavioral and social network data for online advertising, Paper presented at the Data Mining Workshops, 2008. ICDMW'08. IEEE International Conference on, 2008.

[4] T.S. Behrend, D.J. Sharek, A.W. Meade, E.N. Wiebe, The viability of crowdsourcing for survey research, Behavior research methods 43 (3) (2011) 800-813.

[5] L.B. Chilton, J.J. Horton, R.C. Miller, S. Azenkot, Task search in a human computation market, Paper presented at the Proceedings of the ACM SIGKDD workshop on human computation, 2010.

[6] C.P. Chu, Analytic hierarchy process theory (AHP) theory and practice, 2009.

[7] G. Dror, Y. Koren, Y. Maarek, I. Szpektor, I want to answer; who has a question?: Yahoo! answers recommender system, Proceedings of the 17th ACM SIGKDD international conference on Knowledge discovery and data mining, 2011, pp. 1109-1117.

[8] R. Gatautis, E. Vitkauskaite, Crowdsourcing application in marketing activities, Procedia-Social and Behavioral Sciences 110 (24) 1243-1250.

[9] D. Geiger, M. Schader, Personalized task recommendation in crowdsourcing information systems — Current state of the ar, Decision Support Systems , 65 (2014) 3-36.

[10] E. Gilbert, K. Karahalios, Predicting tie strength with social media, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (2009), pp. 211-220

[11] M.C.D. Guardo, M. Castriotta, The Challenge and Opportunities of Crowdsourcing Web Communities: An Italian Case Study, International Journal of Electronic Commerce Studies 4 (1) 79-92.

[12] X. Han, L. Wang, N. Crespi, S. Park, Á. Cuevas, Alike people, alike interests? Inferring interest similarity in online social networks, Decision Support Systems 69 96-106.

[13] C.J. Ho, J.W. Vaughan, Online Task Assignment in Crowdsourcing Markets, Proceedings of the Twenty-Sixth AAAI Conference on Artificial Intelligence, Toronto, Ontario, Canada, 2012, pp. 45–51.

[14] J. Howe, Crowdsourcing: How the power of the crowd is driving the future of business: Random House, Jeff Howe, 2008.

[15] L. Kai, C. D. Timon, Building a targeted mobile advertising system for location-based services, Decision Support Systems, 54(1) (2012), 1-8

[16] A.A. Kardan, M. Ebrahimi, A novel approach to hybrid recommendation systems based on association rules mining for content recommendation in asynchronous discussion groups, Information Sciences 219 (2013) 93-110.

[17] N. Kaufmann, T. Schulze, D. Veit, More than fun and money. Worker Motivation in Crowdsourcing-A Study on Mechanical Turk, Proceedings of the Seventeenth Americas Conference on Information Systems, 2011, pp. 1-11.

[18] I. Konstas, V. Stathopoulos, J.M. Jose, On social networks and collaborative recommendation, Proceedings of the 32nd international ACM SIGIR conference on Research and development in information retrieval, Boston, MA, USA, 2009, pp.195-202.

[19] S. Lattanzi, D. Sivakumar, Affiliation networks, Proceedings of the Forty-first Annual ACM

Symposium on Theory of Computing (2009), pp. 427-434 (New York, NY)

[20] Y. M. Li, L. F. Lin, C. C. Ho, A social route recommender mechanism for store shopping support, Decision Support Systems , 94 (2017) 97-108.

[21] X. Li, M. Wang, T.P. Liang, A multi-theoretical kernel-based approach to social network-based recommendation, Decision Support Systems 65 (2014) 95-104.

[22] Y. Li, Z.A. Bandar, D. McLean, An approach for measuring semantic similarity between words using multiple information sources. IEEE Transactions on Knowledge and Data Engineering, 15 (4) (2003) 871-882.

[23] Y. Li, M. Qian, D. Jin, P. Hui, A.V. Vasilakos, Revealing the efficiency of information diffusion in online social networks of microblog, Information Sciences, 293 (2015) 383-389.

[24] N.Luz, N. Silva, P. Novais, A survey of task-oriented crowdsourcing. Artificial Intelligence Review, 44 (2) (2015) 187-213.

[25] H. Ma, D. Zhou, C. Liu, M. R. Lyu, I. King, Recommender systems with social regularization. Proceedings of the fourth ACM international conference on Web search and data mining, Hong Kong, China, 2011 pp. 287-296.

[26] C. Miao, H. Yu, Z. Shen, C. Leung. Balancing quality and budget considerations in mobile crowdsourcing. Decision Support Systems, 90 (2016) 56–64.

[27] R. Mishra, P. Kumar, B. Bhasker, A Web Recommendation System Considering Sequential Information. Decision Support Systems, 57 (2015) 1-10.

[28] A.Moayedikia, W. Yeoh, K..L. Ong, Y. L. Boo, Improving accuracy and lowering cost in crowdsourcing through an unsupervised expertise estimation approach, Decision Support Systems, 122 (2019) 113065.

[29] D. Nevo, J. Kotlarsky, Primary vendor capabilities in a mediated outsourcing model: Can IT service providers leverage crowdsourcing?, Decision Support Systems, 65 (2014) 17-27.

[30] P. Resnik, Semantic similarity in a taxonomy: An information-based measure and its application to problems of ambiguity in natural langu (1999) 95-130.

[31] F. Ricci, L. Rokach, B. Shapira,. Introduction to recommender systems handbook, Springer, Boston, MA, (2011).

[32] K. Roethke, J. Klumpe, M. Adam, Al. Benlian, Social influence tactics in e-commerce onboarding: The role of social proof and reciprocity in affecting user registrations, Decision Support Systems, 131 (2020) 113268.

[33] T. L. Saaty, Decision making with the analytic hierarchy process, International journal of services sciences 1 (1) (2008) 83-98.

[34] M. Stankovic, J. Jovanovic, P. Laublet, Linked data metrics for flexible expert search on the open web The Semantic Web, Proceedings of the 8th extended semantic web conference on The semantic web: research and applications, Part I, 2011, pp. 108-123.

[35] J.C. Wang, C.H. Chang, How online social ties and product-related risks influence purchase intentions: A Facebook experiment, Electronic Commerce Research and Applications 12 (5) (2013) 337-346.

[36] Q. Wang, W. Du, J. Ma, X. Liao, Recommendation Mechanism for Patent Trading Empowered by Heterogeneous Information Networks, International Journal of Electronic Commerce, 23 (2) (2019) 47-178.

[37] S. Wang, D. Dang, Incentive mechanism for the listing item task in crowdsourcing, Information Sciences, 512 (2020) 80-95.

[38] T. Wu, Eric W.T. Ngai, Y. Wu. Toward a real-time and budget-aware task package allocation in spatial crowdsourcing, Decision Support System 110 (2018) 107-117

[39] M.Ye, X. Liu, W.C. Lee, Exploring social influence for recommendation: a generative model approach. Proceedings of the 35th international ACM SIGIR conference on Research and development in information retrieval, Portland, Oregon, USA, 2012, pp. 671-680.

[40] S.J. Yu, The dynamic competitive recommendation algorithm in social network services, Information Sciences 187 (2012) 1-14.

[41] J. D. Zhang, C. Y. Chow, CoRe: Exploiting the personalized influence of two-dimensional geographic coordinates for location recommendations, Information Sciences, 293 (2015) 163-181.

[42] M. Zhang, J. Bockstedt, Complements and substitutes in online product recommendations: The differential effects on consumers’ willingness to pay, Information & Management, 57(6) (2020) 103341.

[43] W. Zhao, H. Ma, Z. Li, X. Ao, N. Li, Improving social and behavior recommendations via network embedding, Information Sciences, 516 (2020) 125-141.

[44] C.N. Ziegler, J. Golbeck, Investigating interactions of trust and interest similarity, Decision Support Systems 43 (2) (2007) 460-475.

[45] C.N. Ziegler, G. Lausen, L.S. Thieme,. Taxonomy-driven computation of product recommendations. Proceedings of the thirteenth ACM international conference on Information and knowledge management, Washington, D.C., USA, 2004, pp. 406-415.

## Highlights

Crowdsourcing is a new trend that uses the wisdom of crowds to solve certain problems that need vast amounts of human resources.

We design a social mechanism for task-oriented help the requesters easily find suitable c ho are also very willing to finish their tasks.

 The task-oriented crowdsourcing recommendations were derived based on the factors of contributor preference, contributor history and social influence

 The proposed mechanism can help to establish a long-term partnership that brings value to the participants of task-oriented crowdsourcing.

## Authors biography

Yung-Ming Li is a Professor at the Institute of Information Management, National Chiao Tung University in Taiwan. He received his Ph.D. in Information Systems from the University of Washington. His research interests include network science, Internet economics, and business intelligence. His research has appeared in IEEE/ACM Transactions on Networking, INFORMS Journal on Computing, Production and Operations Management, Decision Sciences, International Journal of Electronic Commerce, Information and Management, Decision Support Systems, European Journal of Operational Research, International Conference on Information Systems (ICIS), Workshop on Information Technology and Systems (WITS), among others.

Chin-Yu Hsieh is a Ph.D. student at the Institute of Information Management, National Chiao Tung University in Taiwan. His research interests include artificial intelligence and electronic ecommerce.

Lienfa Lin is an Associate Professor at the Department of M-Commerce and Multimedia Applications, Asia University in Taiwan. He received Ph.D. degree in Information Management from National Chiao Tung University. His research interests include electronic commerce, mobile computing, and social computing. His research has appeared in Decision Support Systems, International Journal of Electronic Commerce, and Information and Management.

Chi-Hsuan Wei received his M.S. degree from the Institute of Information Management, National Chiao Tung University in Taiwan and B.S. degree in Information Management from the National Central University, Taiwan. His research interests focus on electronic commerce and social computing.
