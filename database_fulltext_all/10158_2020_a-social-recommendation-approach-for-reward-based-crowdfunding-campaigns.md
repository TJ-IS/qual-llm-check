---
otero_id: 10158
otero_key: "XUDDF6P9"
title: "A social recommendation approach for reward-based crowdfunding campaigns"
authors: "Yung-Ming Li; Jyh-Hwa Liou; Yi-Wen Li"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103246"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

A Social Recommendation Approach for Reward-based Crowdfunding Campaigns

Yung-Ming Li (Conceptualization) (Methodology) (Validation)

![](/api/attachments/XUDDF6P9/fulltext/images/10523bf6a876b86da6c2f48c675ecf9a30538f5a7b3eebf6046e40fa2b0349bf.jpg)

(Formal analysis) (Investigation)

(Resources)<ce:contributor-role>Data Curation) (Writing - original

draft) (Writing - review and editing) (Visualization) (Supervision)

(Project administration) (Funding acquisition), Jyh-Hwa Liou

(Methodology) (Validation) (Formal analysis)

(Investigation)<ce:contributor-role>Data Curation) (Writing - original draft) (Writing - review and editing) (Visualization), Yi-Wen Li (Methodology) (Formal analysis)

(Investigation)<ce:contributor-role>Data Curation) (Writing - original draft)

PII: S0378-7206(18)30381-1

DOI: https://doi.org/10.1016/j.im.2019.103246

Reference: INFMAN 103246

To appear in: Information & Management

Received Date: 1 May 2018

Revised Date: 3 December 2019

Accepted Date: 6 December 2019

Please cite this article as: Li Y-Ming, Liou J-Hwa, Li Y-Wen, A Social Recommendation Approach for Reward-based Crowdfunding Campaigns, Information and amp; Management (2019), doi: https://doi.org/10.1016/j.im.2019.103246

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# A Social Recommendation Approach for Reward-based Crowdfunding Campaigns

Yung-Ming Li<sup>a,</sup> <sup>\*</sup> • Jyh-Hwa Liou<sup>b</sup> • Yi-Wen Li<sup>a</sup>

<sup>a</sup> Institute of Information Management, National Chiao Tung University, Hsinchu, 300, Taiwan

yml@mail.nctu.edu.tw •c80617@hotmail.com

<sup>b</sup> Department of International Business, Hsin Sheng College of Medical Care and Management, Taoyuan, 325,

Taiwan

alioujh@gmail.com

\* Corresponding Author: Yung-Ming Li (yml@mail.nctu.edu.tw)

## Abstract

In recent years, a new kind of fundraising mode known as crowdfunding has gradually emerged. Because of the rapid spread of the internet, people can offer their creative ideas on a fundraising platform and attract mass backers to invest in their projects. Crowdfunding not only helps users to realize their dreams but also allows companies to carry out test marketing. Although crowdfunding brings huge opportunities, the success rate of fundraising plans remains low. In this study, we therefore propose a phasebased backer recommendation mechanism, which integrates information from crowdfunding and social networking platforms by analyzing the factors of social relationships, user preferences, and economic backgrounds, to help project creators to reach their fundraising goals at each stage. Our experimental results show that the proposed mechanism is effective in identifying appropriate backers with respect to the status of the project and significantly improves the success rates of crowdfunding. The proposed mechanism can provide greater business value and more opportunities to crowdfunding platforms and contribute to more successful fundraising plans.

Keywords: Crowdfunding, Fundraising, Project backer, Social network, Social recommendation

## 1. Introduction

Crowdfunding is a new way to raise funds from the public to complete a specific project. Crowdfunding extends the concept of crowdsourcing, which aggregates the talents and resources of a large pool of individuals through the internet, to the context of fundraising [39, 50]. Interesting and creative ideas that individuals want to realize sometimes fail in the initial stages because they cannot obtain sufficient funds. Crowdfunding is an effective approach, which exploits the power of crowd cooperation to co the problem of funding insufficiency. People who originate fundraising projects on crowdfunding platforms are called creators, while people who have a willingness to invest in crowdfunding projects are known as backers [37]. Creators can present their projects on crowdfunding platforms such as Kickstarter, Indiegogo, and GoFundMe, and attract backers to invest in them. If they can achieve their fundraising goals, the creators can obtain the necessary funds to begin the project and provide some form of reward to the backers.

In recent years, increasing numbers of crowdfunding platforms have appeared; the crowdfunding marketplace has continuously grown and reached \$50 billion in 2013 [9]. Among these emerging crowdfunding platforms is Kickstarter, which is the largest crowdfunding platform in the world and provided \$529 million in 2014. There are more than 3.3 million backers for the projects on Kickstarter [20]. The crowdfunding model has incubated many successful creative ideas and impressive plans. For example, in February 2015, a crowdfunding project was realized for a disabled pensioner called Alan Barnes, who was a victim of a mugging attack. The project’s creators wanted to offer him a new home and support his living arrangements, and therefore created a fundraising campaign [38]. In the future, crowdfunding will be integrated more closely with our lives, not just in terms of business needs but also for more general purposes.

Crowdfunding has certain features and limitations, because only when the investment goal for the project is reached within a specified time period can the project be successful. People back projects that they feel are interesting and which have high possibility of success. If a project cannot easily gain funding

##

in its initial phase and undergo continuous further expansion in the following phases, it has a high probability of failure. Although the number of crowdfunding projects and participants is increasing, according to recent statistics the success rate of projects has never exceeded 50% since crowdfunding platforms appeared [55]. Crowdfunding still has many problems to overcome. For example, the diffusion of projects is too slow to improve the success rate. Project creators can only passively wait for attention from backers, and this is wasteful in terms of time. In addition, the network effect is also an important factor affecting other users; general users do not want to invest in a project, which has a lack of support. As a result, the creator’s family or close friends become the main source of funds at the beginning of a crowdfunding project [36]. Generally only after the project reaches 60% of its goal do people feel safe in investing.

Recently, a few studies investigate the success factors of crowdfunding campaigns on the preference aspect [29, 33, 53]. Some researchers use the social network theory to develop empirical models studying crowdfunding dynamics [18, 55]. These existing works merely consider partial factors either on the preference aspect or the social aspect. Social relationship is a critical success factor in crowdfunding [29, 44] but social-based recommendation faces the issue that it is generally hard to get the explicit or implicit social information [32]. Besides, existing works mainly study the effect of social relationship on crowdfunding without considering the fundraising status. However, the group of backers in different fundraising stages should have different characteristics, which need elaborate investigation and exploitation. In this study, we aim to classify the identified relevant backer groups by evaluating social relationships with respect to various phases of a crowdfunding project. By dynamically combining social relationship and user preference, we develop a new recommendation mechanism to find appropriate backers who are highly relevant, to promote crowdfunding projects. The proposed backer recommendation mechanism can help project creators to overcome the bottlenecks in various fundraising phases. People enjoy sharing their opinions and ideas on social media, such as Facebook, Twitter or Instagram [28], which allows us to extract personal information and to determine a user’s background, preferences, and social relationships [43]. The proposed mechanism aims to identify appropriate backers by analyzing backers’ preferences for projects, their social relationships, and their level of trust in the project creators. In determining how to identify appropriate backers for projects at different stages of crowdfunding, three main questions arise, and will be addressed in this research, as follows:

1. How can backers, be found from a social network, who are interested in crowdfunding projects?

User preference is a key factor to making a satisfactory recommendation. However, the interest profile of a user is not explicitly available. Even though we can gather a great deal of information from social media, it is still difficult to accurately identify the types of people who will be interested in investing in a creator’s project. To resolve this issue, in this research, we aim to combine the activity data from social networking and crowdfunding platforms to discover backers’ preferences. Users often share their consumption behavior or profiles on social media, which provides a way to gather a wider range of related c capacity and investing experiences from the crowdfunding platforms to better infer their preference patterns.

2. How can we reinforce a user’s willingness to invest in crowdfunding projects and improve his/her degree of trust in the creator?

A lack of trust makes it difficult to invest in a stranger’s project. A backer’s trust in the creator becomes a critical factor, which affects his/her willingness to invest in a crowdfunding project. However, the trust between a backer and a creator cannot be explicitly obtained from crowdfunding platforms. To alleviate this problem, in the proposed mechanism, we analyze the relevance to the potential backers and the social relationship between the potential backers and the project creator. Specifically, we consider the intensity of interactions and social closeness to evaluate the social relationship between a backer and a creator. In the early stages of crowdfunding, projects are mainly recommended to the project creator’s family and friends, because studies have shown that family and friends are important sources of funds for startups [36].

3. How can the power of social networks be utilized in different fundraising phases to improve the success rate of crowdfunding?

In addition to users’ preferences and social relationships relating to the crowdfunding project, the status of the crowdfunding project will significantly affect the investing decision of potential backers. Because of herd behavior and word-of-mouth effects, the more backers a project has in the early phases, the higher its success rate will be. However, how to identify the suitable backer groups with respect to different crowdfunding stages, so as to effectively exert the network effect is still not extensively studied. The proposed mechanism should be capable of flexibly identifying appropriate backers at different crowdfunding stages. Specifically, family and close friends, regular friends, and strangers are the potential backer groups to be targeted in the early, intermediate, and late crowdfunding phases.

To resolve these issues, we develop a new recommendation mechanism to identify appropriate backers relevant to particular crowdfunding projects at various stages. The main components of the proposed mechanism include an analysis of user preferences and social relationships. The fundraising activities are divided into several stages. In the initial stage, we aim to raise early funds from the creators’ close family, and friends. Next, through social network analysis, we further identify friends who are interested in the crowdfunding project to reach the intermediate goal of fundraising; meeting this threshold means that the project will have a high probability of success at the final stage. Using this phase-based recommendation mechanism, we dynamically recommend a suitable list of backers for creators at these three stages. The proposed mechanism was implemented, based on information combined from social media and crowdfunding platforms, and the experimental results show that our proposed recommendation system for crowdfunding projects outperforms all other benchmark recommendation methods in terms of effectiveness. In practice, a creator can repeatedly use our system to search for suitable backers at each phase; the system can also speed up fundraising and alleviate the current crowdfunding problems.

The remainder of this paper is set out as follows. Section 2 reviews the literature related to this research. The proposed crowdfunding backer recommendation mechanism is presented in Section 3. Section 4 discusses the methodology of the experiments conducted on the proposed mechanism. The results of these experiments and an evaluation are presented in Section 5. Finally, in Section 6, we describe our research contributions, the limitations of this research and future work.

## 2. Related literature

## 2.1 Crowdfunding

Crowdsourcing is a new trend, which utilizes the resources of crowds on the internet to solve certain problems [11, 12, 17]. Extended from the concept of crowdsourcing, crowdfunding is a novel method of fundraising for people who do not have independent wealth but who want to complete a project [55]. Crowdfunding has three basic, different types of funding classified according to the type of feedback: reward crowdfunding [24, 30], lending crowdfunding [7], and equity crowdfunding [45]. In this research, we will focus on backer recommendations for reward-based crowdfunding projects.

Crowdfunding can help creators earn funds from the internet [4]. Generally, backers are ordinary people, and the money they are required to invest is too little to have a serious effect on daily life; thus, most people have the ability to back interesting projects [37]. Massolution reported that crowdfunding reached \$1.5 billion in 2013 [34]. Kickstarter, Indiegogo, and GoFundMe are famous crowdfunding platforms across the world [13]. Kickstarter is the most well-known, and this site has raised \$1.5 billion in funding and over 7.8 million backers for 78,000 successful projects [20]. Reward-based crowdfunding generally adopts an “all-or-nothing” policy, which means that the creator can receive the funds only if the fundraising goals are achieved [48]. Achieving the project’s goals is therefore extremely important, otherwise the crowdfunding project fails. According to a recent report, the success rate of crowdfunding projects has been only 39% because Kickstarter was founded in 2009 [20]. Overall, it has had only a small number of successful non-profit projects [28]. Recently, to enhance the success rate of projects, large crowdfunding platforms have offered connections with social media, such as Facebook, Twitter, Instagram, and Google+. Users can share the project’s context on these social media. However, advertising is annoying for some receivers; in addition, a backer supporting too many projects at the same time will disperse his/her investment resources [40].

##

Recently, a few studies have tried to identify the success factors of crowdfunding campaigns [29, 33, 53]. The work [33] uses the content of postings and non-content factors to identify features associated with successful donations. Some studies [29, 53] using the text analytics approach to analyze crowdfunding successes, have found that past participation positively impacts the success of a project. The funders’ age, gender, education, income, crowdfunding experience, and website familiarity are considered as the control variables affecting the success of crowdfunding [29]. Furthermore, some researches use social capital theory to develop an empirical research model on crowdfunding [18, 55]. However, these existing works merely consider partial factors either on the preference aspect or social aspect. In this research, dynamically combining social relationship and user preference, we aim to develop a new recommendation mechanism to find appropriate backers who are highly relevant, to promote crowdfunding projects. Specifically, we analyze the preference of a backer by a backer’s activities on the crowdfunding platforms, his/her activities on social media by individual preference analysis, and economic capacity. Furthermore, as the characteristics of backers differ, the set of potential backers is classified into various groups according to different phases of a crowdfunding project.

## 2.2 Recommendation systems

Recommendation systems are developed to suggest something or someone to a specific user. Traditional recommendation systems often focus on identifying relevant items, which satisfy a user’s requirements and then rank them for users [21]. They can mainly be classified into two types: content-based and collaborative-based systems. Various techniques such as decision trees, clustering, regression, neural networks, and association rule mining are utilized in these recommendation systems [35]. Content-based recommendation systems suggest items based on a user’s previous preferences. They rank items for users by calculating a similarity rating for the items that are of particular interest to personalized recommendation; however, a lack of diversity is an obvious disadvantage for the content-based method [10]. Collaborativebased systems focus on finding users who are similar to a target user, and generating recommended items that are of many variations to diverse recommendations based on the preferences of these similar users. The collaborative-based method has several limitations, such as rating sparsity and low scalability [1, 25]. In recent years, researchers have made efforts to develop more customized and personalized recommendations. Personalized recommendation first creates a user profile according to the user’s preferences and needs. Then, the recommendation system suggests items based on this user profile and the context of items. Finally, users can give feedback and related measures to evaluate its quality and usefulness [19]. Recently, with the availability of traceable online social activities, many social network-based recommendation systems utilizing the social influence theory to generate trustable recommendation have been developed [25, 51]. Social information allows us to infer more characteristics of users’ preferences, to measure their social relationships and identify their social circles. The social recommendation approach can be used to search for popular and influential people on social networks with a combination of preference similarity, social trust, and social relationships [26, 27]. However, the social-based recommendation faces the issue that it is

On the basis of the above studies, we can observe that recommendation systems have undergone a great deal of development in recent years. However, the success of crowdfunding depends on many factors, such as the type of project, backer’s preference, social relationship, and the status of the project goal. Existing recommendation systems consider only partial factors and cannot be effectively applied to enhance based, and social-based recommendation with multi-criteria factors, we design a phase-based recommender system utilizing the power of social networks, which can effectively identify appropriate backers with respect to the various crowdfunding phases. In addition, backers can easily make decisions when choosing from relevant projects. Table 1 summarizes the characteristics (description, advantages, and shortcomings) of different recommendation approaches.

## 2.3 Social network and relationships

Social media allows people to create, share, and exchange information, and to form friendships. People can browse each other’s personal pages on social networking websites, such as Facebook, Twitter, and YouTube [43]. They can also spread content, not only to small social circles but to other connected social networks [52]. A social network is a structure in which users form a connection network, including nodes and edges. The nodes represent individuals and the edges represent the direct connection between two nodes [47]. The connection between two individuals is described as a “social tie” [8]. There are two different types of social ties: strong and weak. A strong tie means that the linked people have a very close relationship and a high level of trust in each other; this usually occurs between families and close friends. A weak tie means there is a more distant relationship between two people. People with weak ties may not have a direct link, such as classmates and friends of friends [46, 49]. If two nodes have a relationship with a strong tie, this indicates that they have more trust [14]. Therefore, for higher-risk products, friends with strong ties have a higher influence than friends with weak ties. For lower-risk products, the influence of strong and weak ties is the same [47]. Trust is based on the belief that a future action of a person will bring good results, and can affect a user’s purchasing decision through electronic word-of-mouth marketing [31]. A consumer’s trust expectation has a positive association with product performance and risk reduction [16]. As people can share their experiments in buying products or services with a large number of unknown users, the degree of trust is very important in enhancing the sharing and exchanging activities of the members in online communities. The degree of trust between people can be evaluated in terms of expertise, preference, and relationships [22]. Prior studies show that a similarity of interests is strongly associated with the relationship between two users [56]. In other words, if similar users have strong ties and common characteristics such as location, age, gender, and similar friends, they will have greater trust than strangers. They are willing to accept the content shared by these similar friends [15].

Crowdfunding is a particular way of raising funds from strangers. To attract strangers to invest money, social relationships have significant effects on improving backer recommendation as social trust is a commitment to affect people’s actions, which is based on the belief that a future action of a person will bring good results [31]. Social capital is a critical success factor in the early stage of crowdfunding [29, 44]. An initial project has a higher risk because it is unstable and difficult to predict the results. Therefore, we search for strong tie friends who have similar preferences as the creator. Existing studies mainly empirically study the effect of social relationships on crowdfunding. In this study, we will classify the identified relevant backer groups by evaluating social relationships with respect to the various phases of a crowdfunding project. Specifically, we consider the intensity of interactions and social closeness to evaluate the social relationship between a backer and a creator.

## 3. The system framework

## 3.1 Design of system modules

Utilizing the theory of social network, we develop a novel phase-based crowdfunding recommendation mechanism that can help all participants engaged in a crowdfunding campaign. The proposed mechanism can help creators to identify potential backers and reach their crowdfunding goals, through a mechanism of social network activity mining and a suitable selection of recommendation lists. Specifically, we collect and integrate different sources of behavioral information to identify a user’s preferences from the activities on the user’s social network and crowdfunding platforms. Grounded on the social network theory, those friends with closer relationships are more trustable [14, 46, 49]. A user’s friends with a stronger tie have higher influence on his/her selection decision on high-risk items [47]. We analyze the intensity of social interaction and social closeness to evaluate the strength of the social relationship between the creator and the backer, based on the concepts of social tie [8], social influence [47], and social trust [14]. According to the study [23] on the dynamics of project backers, backers contribute more in the first week and last week over the project funding cycle and family and friend backers tend to occur in the first week. On the basis of the various phases of crowdfunding progress (early, intermediate, and late phases), the proposed mechanism will dynamically adjust the criterion weights for the different discovered groups (family and close friends, acquaintances, and strangers) and generate a list of ranked appropriate backers according to their relevance to the project. The system architecture is shown in Fig. 1.

![](/api/attachments/XUDDF6P9/fulltext/images/1bb7c72fd6c4029f9a76053e0389ea9e408365484fea319dcb87baaba3bd72b9.jpg)  
Fig. 1. The system framework  
The main modules in the system framework are as follows:

(1) TypeTree construction module. A hierarchical structure is a good construction for classification. This type of structure performs effectively in the fields of product taxonomy [57]. In this module, we aim to establish a TypeTree to classify projects from different crowdfunding platforms. This is used to analyze and identify a user’s preferences and his/her relevance to the specified projects from social networking and crowdfunding activities.

(2) Social relationship analysis module. Social capital is a critical success factor in the early stage of crowdfunding, [44]. Trust plays a significant role in backers investing in crowdfunding projects [29]. If two persons have a relationship with a strong tie, they have more trust in each other [14]. Based on the concept of social tie and social trust, we build the social relationship analysis module. This module will analyze the intensity of the interaction and social closeness to evaluate the strength of the relationship between the creator and the backer. According to the strength of the social relationship, we classify these potential backers into several candidate groups.

(3) User preference analysis module. A backer only considers those projects, which are interesting to him/her. A successful crowdfunding recommendation is strongly associated with whether the type of project fits with a backer’s preference. Besides individual preference, we consider a person’s backing preference, and his/her economic capacity to obtain a more comprehensive view of a user’s preference. The module will collect personal information, including backer preference, individual preference, and economic capacity, to infer the user’s preferences.

(4) Crowdfunding recommendation engine module. In this study, we incorporate the concept of social relationship into the development of crowdfunding project recommendation, considering multicriteria factors (social relationship, individual preferences, backer’s preferences, and economic capacity) to identify the appropriate target backers according to the status of the project. In this module, we first calculate the weight of the project’s characteristics, including project phase (time period), and project distance (funding goal). A creator can use the proposed mechanism to dynamically search for potential backers, based on the crowdfunding phase, until the goal is achieved.

## 3.2 TypeTree construction module

In this module, we construct a tree to match project types with a user’s preference. Numerous crowdfunding platforms have emerged in recent years, and these focus on different goals and offer many types of projects to choose from. We classify all types of projects from these crowdfunding platforms and their preference classification from social media.

A hierarchical structure is an effective approach to building a tree for classification. In this section, we use a hierarchical tree structure to classify the project types, and name this structure “TypeTree.” As shown in Figure 2, the first layer is the root; the second layer is a type name from different crowdfunding platforms; and the third layer is the classification of preference type from Facebook. The TypeTree indexes from the root to the lowest nodes. The index is used to identify a user’s preference. Note that there are many nodes of the TypeTree, and only a few of these are shown in Fig. 2.

![](/api/attachments/XUDDF6P9/fulltext/images/4fa2eaabbff22940de67856f4195adfb5927888165494a6c389593ae4f4354d9.jpg)  
Fig. 2. An example of the TypeTree module

## 3.3 Social relationship analysis module

This module will construct a creator’s social network to evaluate the social relationship between the creator and the backer by combining social interaction and closeness analyses. Then, according to the social relationship value, we will classify the backers into three candidate backer groups corresponding to three different recommendation phases.

## 3.3.1 Social interaction analysis

We use ?????????????????????? $( b _ { i } , c _ { j } )$ to denote the intensity of the interactions between a backer $b _ { i }$ and a $c _ { j } .$ users are tagged together in the same comments, photos, check-ins, and posts, denoted as $T a g ( b _ { i } , c _ { j } )$ ; (2) the number of comments from the two users on each other’s posts, comments, photos, statuses, and checkins, denoted as ?????????????? $( b _ { i } , c _ { j } )$ ; (3) the number of times the two users have “liked” each other’s posts, comments, photos, status, and check-ins, denoted as $L i k e ( b _ { i } , c _ { j } )$ ; and (4) the number of clubs both users have joined, denoted as $C l u b ( b _ { i } , c _ { j } )$ .

The intensity of social interactions between the backer $b _ { i }$ and creator $c _ { j }$ , ?????????????????????? $( b _ { i } , c _ { j } )$ is computed as:

$$
I n t e r a c t i o n (b _ {i}, c _ {j}) = \operatorname{Tag} (b _ {i}, c _ {j}) + \operatorname{Comment} (b _ {i}, c _ {j}) + \operatorname{Like} (b _ {i}, c _ {j}) + \operatorname{Club} (b _ {i}, c _ {j})\tag{1}
$$

Next, the value of ?????????????????????? $( b _ { i } , c _ { j } )$ should be normalized. We adopt a min-max normalization approach because this has a higher efficiency than other normalization approaches. The formula for minmax normalization is shown in (2) and the ?????????????????????? $( b _ { i } , c _ { j } )$ value will be normalized from 0 to 1.

$$
V ^ {\prime} = \frac {V - M i n (S e t _ {v})}{M a x (S e t _ {v}) - M i n (S e t _ {v})},\tag{2}
$$

where $V ^ { \prime }$ is the normalized value and V is the value before normalizing. $S e t _ { v }$ is a set, which contains all the values of ?????????????????????? $( b _ { i } , c _ { j } )$ . The value of $M i n ( S e t _ { v } )$ is the minimum value of $S e t _ { v }$ and the value of $M a x ( S e t _ { v } )$ is the maximum value of $S e t _ { v }$

## 3.3.2 Social closeness analysis

The number of mutual friends of a backer $b _ { i }$ and a creator ?? is denoted as ?????????????????????????? $\left( b _ { i } , c _ { j } \right)$ . If two users have many mutual friends in a social network, we can infer that they have a close relationship. Similarly, we use min-max normalization to normalize ?????????????????????????? $\left( u _ { f } , u _ { g } \right)$ and adjust the social interaction intensity to measure social closeness as:

$$
\text { SocialCloseness } \left(b _ {i}, c _ {j}\right) = \text { Interaction } \left(b _ {i}, c _ {j}\right) * \text { MutualFriends } \left(b _ {i}, c _ {j}\right)\tag{3}
$$

It is likely that backer $b _ { i }$ and creator $c _ { j }$ are not direct friends and do not have direct interactions; there may be many paths of friendships connecting them. We use $P a t h s { \left( b _ { i } , c _ { j } \right) }$ to denote the set of all paths between the backer $b _ { i }$ and the creator $c _ { j }$ . Assuming there are n paths, we have

$$
P a t h s \left(b _ {i}, c _ {j}\right) = \left\{P a t h _ {1} \left(b _ {i}, c _ {j}\right), P a t h _ {2} \left(b _ {i}, c _ {j}\right), \dots , P a t h _ {n} \left(b _ {i}, c _ {j}\right) \right\}\tag{4}
$$

We use $P a t h L e n g t h ( P a t h _ { n } \big ( b _ { i } , c _ { j } \big ) )$ to denote the number of links in a social path $P a t h _ { n } \big ( b _ { i } , c _ { j } \big )$ and $H o p ( c _ { j } , L i n k )$ as the number of hops from the creator $c _ { j }$ to a particular connection edge Link. The social relationship between the creator $c _ { j }$ and the backer $b _ { i }$ can be measured as:

$$
\begin{array}{l} \text {SocialRelationship} (b _ {i}, c _ {j}) \\ = \underset {\text {Path} _ {l} \in \text {Paths} (b _ {i}, c _ {j})} {\text {Max}} \left(\frac {1}{\text {PathLength} (\text {Path} _ {l})} * \sum_ {\text {link} \in \text {Path} _ {l}} \frac {\text {SocialCloseness} (\text {Link})}{\text {Hop} (c _ {j} , \text {Link})}\right). \end{array}\tag{5}
$$

Next, we generate a list of m backers ranked according to the value of their social relationship as:

$$
S R S o r t (c _ {j}) = \{u s e r _ {1} (c _ {j}), u s e r _ {2} (c _ {j}), \dots , u s e r _ {m} (c _ {j}) \}\tag{6}
$$

Finally, we divide all users into three candidate backer groups, corresponding to the three different crowdfunding phases, as:

$$
\begin{array}{l} \bigl \{G r o u p _ {p h a s e 1}, G r o u p _ {p h a s e 2}, G r o u p _ {p h a s e 3} \bigr \} = \\ \Bigl \{\{u s e r _ {1} (c _ {j}), \ldots , u s e r _ {k} (c _ {j}) \}, \{u s e r _ {k + 1} (c _ {j}), \ldots , u s e r _ {p} (c _ {j}) \}, \{u s e r _ {p + 1} (c _ {j}), \ldots , u s e r _ {m} (c _ {j}) \} \Bigr \}. \end{array}\tag{7}
$$

## 3.4 User preference analysis module

In this module, we aim to analyze information from the crowdfunding platforms and social networking websites to infer the backer’s preferences.

## 3.4.1 Backer preference analysis

To understand users’ participation behavior, we collect and analyze backers’ activities on crowdfunding platforms. ???????????????????????????????? $( b _ { i } , t y p e )$ is a value that represents the tendency of backer $b _ { i } ^ { \prime } s$ to have a preference for a specific project type on crowdfunding websites and is measured as:

$$
\text { BackerPreference } (b _ {i}, \text { type }) = \text { ShareTimes } (b _ {i}, \text { type }) + \text { TypePreference } (b _ {i}, \text { type }),\tag{8}
$$

where ??ℎ???????????????? $( b _ { i } , t y p e )$ is the total number of times a specific type of project is shared by backer $b _ { i } .$ . For example, if a backer $b _ { i }$ shared a crowdfunding project involving art three times on Facebook, the value of ??ℎ???????????????? $( b _ { i } , A r t )$ is 3. Assume the set of project types is T; then backer $b _ { i } { } ^ { \circ } \mathrm { s }$ preference for a project type from the crowdfunding platforms is evaluated as

$$
T y p e P r e f e r e n c e (b _ {i}, t y p e) = \frac {B a c k T i m e (b _ {i} , t y p e) * B a c k M o n e y (b _ {i} , t y p e)}{\sum_ {t \in T} (B a c k T i m e (b _ {i} , t) * B a c k M o n e y (b _ {i} , t))},\tag{9}
$$

where ?????????????????? $\left( b _ { i } , t y p e \right)$ represents the number of times backer $b _ { i }$ has invested in this project type and $B a c k M o n e y ( b _ { i } , t y p e )$ represents the average amount of money backer $b _ { i }$ invested in the project type. Note that the value of ???????????????????????????????? $\left( b _ { i } , t y p e \right)$ should be normalized and used for further analysis.

In the backer preference analysis, some backers do not have any prior history of behavior on the crowdfunding platforms. We set the value of backers’ preference as zero. To avoid the cold start problem, we obtain more preference information from social media to increase the accuracy in the next part (individual preference analysis).

## 3.4.2 Individual preference analysis

In addition to the backer’s activities on the crowdfunding platform, we further analyze a user’s preferences according to his/her activities on social media. Assume that ???????????????????????????????? $( b _ { i } , t y p e )$ represent the backer’s social activities of a specific type on social media. $S i m i l a r i t y ( b _ { i } , t y p e )$ represents the similarity between the backer’s social activities and the specified project type. The individual preference of a user is evaluated as:

$$
I n d i v i d u a l P r e f e r e n c e (b _ {i}, t y p e) = S o c i a l A c t i v i t i e s (b _ {i}, t y p e) * S i m i l a r i t y (b _ {i}, t y p e)\tag{10}
$$

The value of ???????????????????????????????? $( b _ { i } , t y p e )$ is calculated based on the following kinds of social activities: (1) check-ins: check-ins record activities, which show what the user does or where he/she is; (2) pages which a user likes or pays attention to; (3) “likes”: this is a button that a user can click on social media; and (4) comments which a user writes or responds to. These check-ins, pages, likes, and comments are classified and mapped to the constructed TypeTree. For example, if a user frequently checks in to art exhibitions, we can infer that he/she might be interested in the arts. Similarly, likes and pages can be classified using the mapped categories. The individual preferences of a user for specific types of social activities can be measured as:

$$
\begin{array}{l} \text {SocialActivities} (b _ {i}, t y p e) \\ = c h e c k i n s _ {t y p e} (b _ {i}) + p a g e _ {t y p e} (b _ {i}) + l i k e _ {t y p e} (b _ {i}) + c o m m e n t _ {t y p e} (b _ {i}). \end{array}\tag{11}
$$

To recognize the individual preferences of these users, we used the Chinese Knowledge and Information Process (CKIP) to filter frequently appearing words. The CKIP is a tool developed by the Institute of Information Science and the Institute of Linguistics of Academia Sinica [2]. In the experiments, we input sentences from users’ historical Chinese posts to the CKIP. We identify the most frequent words. The discovered keywords were matched with the TypeTree by the system.

Next, we will use the TypeTree to compute the similarity between the preferences of backer $b _ { i }$ and a project type as:

$$
S i m i l a r i t y (b _ {i}, t y p e) = \overrightarrow {b _ {i}} \cdot \overrightarrow {T y p e}.\tag{12}
$$

For example, a user has check-ins involving music videos four times and billboard music three times. According to the example TypeTree in Fig 2, a vector with nine dimensions is (1) Root, (2) Music, (3) Food, (4) Billboard Music, (5) Music Awards, (6) Music Videos, (7) Food/Beverages, (8) Food/Groceries, and (9) Restaurants/Coffee Shops. As the dimensions of Billboard Music, Music Awards, and Music Videos belong to Music, the value of the nodes is 1, and the vector representing the property of Music is $( 3 , 3 , 0 , 1 , 1 , 1 , 0 , 0 , 0 )$ . The vector $\overrightarrow { b _ { \imath } }$ recording the activities of backer $b _ { i }$ is $\widehat { b _ { \iota } } ( 7 , 7 , 0 , 3 , 0 , 4 , 0 , 0 , 0 )$ $S i m i l a r i t y ( b _ { i } , T y p e )$ is $\overrightarrow { b _ { \iota } } \cdot \overrightarrow { M u s u c } = 2 1 + 2 1 + 3 + 4 = 4 9$

## 3.4.3 Economic capacity analysis

In addition to these preferences, whether or not a potential backer has the economic capacity to invest is also important. The economic capacity will affect his/her willingness to back crowdfunding behavior [3]. We would not recommend any projects to a user because the backer has no money to invest. We evaluate the economic capacity based on occupation and relevant background in a socioeconomic level, including four aspects: (1) age, (2) educational background, (3) work experience, and (4) income. A backer’s economic capacity is measured as three levels and evaluated as:

$$
E c o n o m y C a p a c i t y (b _ {i}) = A g e (b _ {i}) + E d u c a t i o n (b _ {i}) + W o r k (b _ {i}) + I n c o m e (b _ {i}), \text {where}\tag{13}
$$

$$
A g e (b _ {i}) = \left\{ \begin{array}{l l} 0, & \text {if b_{i} <  18 years old;} \\ 1, & \text {if 18 years old\leq b_{i} <  24 years old;} \\ 2 & \text {if b_{i} \geq 24 years old.} \end{array} \right.\tag{14}
$$

$$
E d u c a t i o n (b _ {i}) = \left\{ \begin{array}{l l} 0, & m i d d l e s c h o o l; \\ 1, & h i g h s c h o o l; \\ 2, & u n i v e r s i t y d e g r e e. \end{array} \right.\tag{15}
$$

$$
W o r k (b _ {i}) = \left\{ \begin{array}{l l} 0, & \text {No work experience;} \\ 1, & \text {one or two years' work experience;} \\ 2, & \text {over two years' work experience.} \end{array} \right.\tag{16}
$$

$$
I n c o m e (b _ {i}) = \left\{ \begin{array}{c c} 0, & \text {no salary;} \\ 1, & 0 <   s a l a r y <   1 0 0 0 d o l l a r s; \\ 2, & \text {salary} > 1 0 0 0 d o l l a r s. \end{array} \right.\tag{17}
$$

## 3.5 Crowdfunding recommendation engine module

Phase 1 is the first week of the project, Phase 2 is the intermediate period, from the seventh day to the final week, and Phase 3 is the last week of the fundraising period. When the project is in these different phases, our mechanism will use different factor weight distributions. Next, we use the weight method to calculate the weights and form a suitable list for the creator.

## 3.5.1 Crowdfunding project analysis

We first determine the status of an ongoing project. The project phase of the ongoing project p is

$$
P r o j e c t P h a s e (p) = \frac {P r o j e c t D a y s (p) - T i m e L e f t (p)}{P r o j e c t D a y s (p)},\tag{18}
$$

where ??????????????????????(??) is the total number of days of the ongoing project, and $T i m e L e f t ( p )$ is the time

$$
P P h a s e (p) = \left\{ \begin{array}{l l} 1, & \text {if ProjectPhase(p) <   \varphi_{phase1} (p);} \\ 2, & \varphi_ {p h a s e 1} (p) <   P r o j e c t P h a s e (p) <   \varphi_ {p h a s e 2} (p); \\ 3, & \text {if ProjectPhase(p) > \varphi_{phase2} (p).} \end{array} \right.\tag{19}
$$

Note that the threshold of Phase 2 indicates the end of the first week and the start of the last week.

Next, the project distance of an ongoing project in achieving the fundraising goal is evaluated as:

$$
P r o j e c t D i s t a n c e (p) = \frac {P r o j e c t G o a l s (p) - P r o j e c t P l e d g e d (p)}{P r o j e c t G o a l s (p)},\tag{20}
$$

where ????????????????????????????(??) is the money pledged to the project and ????????????????????????(??) is the fundraising goal of the project.

$$
P D i s t a n c e (P) = \left\{ \begin{array}{l l} 1, & \text {if ProjectDistance(p) <   \varphi_ {distance1} (p);} \\ 2, & \varphi_ {d i s t a n c e 1} (p) <   P r o j e c t D i s t a n c e (p) <   \varphi_ {d i s t a n c e 2} (p); \\ 3, & \text {if ProjectDistance(p) > \varphi_ {distance2} (p),} \end{array} \right.\tag{21}
$$

To categorize the ongoing projects into these three levels of project distance, we define two thresholds:

$$
\varphi_ {d i s t a n c e 1} (p) = \frac {\text {ProjectGoals} (p) - (\text {ProjectGoals} (p) * 1 / 3)}{\text {ProjectGoals} (p)},\tag{22}
$$

$$
\varphi_ {d i s t a n c e 2} (p) = \frac {\text {ProjectGoals} (p) - (\text {ProjectGoals} (p) * 2 / 3)}{\text {ProjectGoals} (p)}.\tag{23}
$$

Note the two distance thresholds indicate that funding of over 1/3 and over 2/3 of the goal has been reached, respectively.

## 3.5.2 Candidate backer group computing

The project distance and phase are important factors to select the candidate backer group. In this section, we allocate the candidate backer groups according to the status of the project phase and project distance. The status of an ongoing project is evaluated by

$$
\text { FundraisingStatus } (p) = P \text { Distance } (p) * P \text { Phase } (p).\tag{24}
$$

The maximum value of FundraisingStatus(p) is 9 and the minimum is 1. The candidate backer group is selected using the following rule.

$$
C B G (p) = \left\{ \begin{array}{c} C a n d i d a t e G r o u p _ {p h a s e 1}, i f F u n d r a i s i n g S t a t u s (p) \leq \theta ; \\ C a n d i d a t e G r o u p _ {p h a s e 2}. i f \theta <   F u n d r a i s i n g S t a t u s (p) \leq \mu ; \\ C a n d i d a t e G r o u p _ {p h a s e 3}, i f F u n d r a i s i n g S t a t u s (p) > \mu , \end{array} \right.\tag{25}
$$

??ℎ?????? $\theta + \mu = 9$

## 3.5.3 Suitability criteria aggregation

After determining the targeted backer group, we decide the criteria weights to identify the appropriate backers for a project. Four criteria are considered when evaluating the suitability of the potential backers:

(1) social relationships, (2) individual preferences, (3) backer preferences, and (3) economic capacity. We use the analytic hierarchy process (AHP) theory to organize and analyze complex decision-making problems with multiple criteria, as proposed by Thomas L. Saaty in 1971 [5, 6, 42]. We build a pairwise matrix $M _ { S I B E }$ in which S represents social relationships, I represents individual preference, B represents backer preference, and E represents economic capacity.

$$
M _ {S I B E} = \left[ \begin{array}{c c c c} 1 & A _ {S I} & A _ {S B} & A _ {S E} \\ \frac {1}{A _ {I S}} & 1 & A _ {I B} & A _ {I E} \\ \frac {1}{A _ {B S}} & \frac {1}{A _ {B I}} & 1 & A _ {B E} \\ \frac {1}{A _ {E S}} & \frac {1}{A _ {E I}} & \frac {1}{A _ {E B}} & 1 \end{array} \right],\tag{26}
$$

where $A _ { S I }$ represents the relative decision weights of social relationships to individual preferences, $A _ { S B }$ represents the relative decision weight of social relationships to backer preferences, $A _ { S E }$ represents the relative decision weight of social relationships to economic capacity, $A _ { I B }$ represents the relative decision weight of individual preferences to backer preferences, $A _ { I E }$ represents the relative decision weight of individual preferences to economic capacity, and $A _ { B E }$ preference to economic capacity.

We collect these data from questionnaires on users’ first usage, and their values may be affected by the crowdfunding phase of a user i as $A _ { S I B E } ( i )$ , and this set can be represented as:

$$
A _ {S I B E} (i) = \{A _ {S I} (i), A _ {S B} (i), A _ {S E} (i) A _ {I B} (i), A _ {I E} (i), A _ {B E} (i) \}.\tag{27}
$$

After the establishment of the complete comparison matrix, we use the eigenvalue solution from the numerical analysis of the eigenvalues method to identify the characteristics of this value and then to determine the weights of the elements at all levels. We use the average of the normalized columns (ANC) to calculate the eigenvectors, because the pairwise matrix is not usually a consistent matrix, and this ANC method can give a better accuracy when computing results than other methods [5]. At the same time, we use a set to record the values of the four weights of user i for the four same criteria as $W _ { S I B E } ( i )$ as:

$$
W _ {S I B E} (i) = \{W _ {S} (i), W _ {I} (i), W _ {B} (i), W _ {E} (i) \}.\tag{28}
$$

$$
W _ {\alpha} (i) = \frac {1}{4} \sum_ {\gamma = 1} ^ {4} \frac {A _ {\beta \gamma} (i)}{\sum_ {\beta = 1} ^ {4} A _ {\beta \gamma} (i)}, \forall W _ {\alpha} (i) \in W _ {S I B E} (i), A _ {\beta \gamma} (i) \in A _ {S I B E} (i).\tag{29}
$$

Using the weight values of the four criteria, this mechanism has the ability to measure the suitability of the recommendation of backer $b _ { i }$ to invest in project p created by creator $c _ { j }$ in a specific crowdfunding phase. We denote the suitability of recommendation of the backer as:

$$
\begin{array}{l} S u i t a b i l i t y (b _ {i}, c _ {j}, t y p e) \\ = W _ {S} (i) * S o c i a l R e l a t i o n s h i p (b _ {i}, c _ {j}) + W _ {I} (i) * I n d i v i d u a l P r e f e r e n c e (b _ {i}, t y p e) \\ + W _ {B} (i) * B a c k e r P r e f e r e n c e (b _ {i}, t y p e) + W _ {E} (i) * E c o n o m y C a p a c i t y (b _ {i}) \end{array}\tag{30}
$$

## 3.5.4 Backer list generation

Following the calculations in the above analyses, we can generate a suitable list of backers and show it to the creator. The creator will receive a recommendation list, which provides basic information about the project: (1) the distance of the project and (2) the phase of the ongoing project. In addition, the backer list also provides five types of information about the backer: (1) name, (2) picture, (3) social relationship with the creator, (4) individual preferences, and (5) Facebook personal website, to offer a way for the creator to contact the backer.

## 4. Experiments

To verify our proposed mechanism, we conducted experiments based on two crowdfunding platforms, FlyingV and zeczec, and the social media site Facebook. FlyingV is one of the largest crowdfunding platforms in Asia, with 1.7 million members, 1,000 projects, and over 190 million fundraising money. These platforms offer over 20 types of projects to choose from, and it is easy for a user to create a project to raise funds. Zeczec is another popular platform within Asia; it was founded in 2012 [54] and offers 11 types of projects for users. We constructed the TypeTree based on category information and analyzed activities concerning crowdfunding projects from these two major platforms. We chose Facebook, the most popular social network in the world, to gather the user’s social information. Facebook provides a good platform environment for analyzing a user’s social relationships and offers more public personal information.

## 4.1 Experimental method

The experimental method is described in the following steps.

Step 1: We developed a web system and shared it through crowdfunding clubs on Facebook. We invited users to participate in our experiment to construct the network, and we asked the creators to distribute a web-based system to their friends on Facebook. When users used our web-based system, they were asked to log into their personal Facebook account; otherwise, it is not possible to collect their personal information from social network due to constraints of the site’s privacy policy. We then asked the users to fill in the AHP questionnaire to calculate the weights of the criteria.

Step 2: The creator inputs the project information into the system, including the project’s name, type, start time, end time, goal, pledged money, and content. In our experiment, we invited users to offer a project or idea, which was a preliminary concept but had not yet become a complete crowdfunding project.

Step 3: After the creator sent the requests to analyze a project, we conducted corresponding analyses to evaluate the suitability of potential backers for a project. We first computed the project phase and project distance to identify the candidate backer group and corresponding weights to choose suitable backers. The weights were based on a questionnaire survey using a comparative seven-level scale and were calculated using the AHP method.

Step 4: Based on the suitability-to-recommend score for each user, the system generated a list of recommended backers for the creator. The creator could invite them to invest in his/her project from this allow us to understand their liking, satisfaction, and willingness. We also asked them to share the project through Facebook if they were willing.

## 4.2 Data collection

By sharing our web system through crowdfunding clubs and personal pages on Facebook, we collected users’ information.

## 4.2.1 User profile

A total of 282 users participated in the experiments. We used Facebook PHP SDK and Graph API to access their Facebook information after they had given permission for this. Over the previous 12 months, they had 27,636 check-ins, 81,216 posts, 133,104 tags, 11,280 fan page likes, 345,732 likes, and 225,600 comments. The average number of friends of each user was 280.

The users’ ages were from 18 to 40 years. The gender distribution was 161 males and 121 females (43% male, 57% female). The distribution of educational backgrounds was as follows: master’s degree (58%), university degree (40%), and high school (2%). Twenty-four percent of users had one to two years’ working experience, 50% of users had one year’s working experience and 26% of users had no working experience.

![](/api/attachments/XUDDF6P9/fulltext/images/1058ff21712bae8aa577c468fcf5497b4cdd15e3ff9d5241f5127f61724380a1.jpg)  
Fig. 3. The gender distribution of users

![](/api/attachments/XUDDF6P9/fulltext/images/861e79a35f0ab87324365760d40cb91bed8fdb4b019ff87643ff0956d8b45a33.jpg)  
Fig. 4. The age distribution of users

![](/api/attachments/XUDDF6P9/fulltext/images/51f0b8007dd08169ec3cbdbca1c44ab1d07978759beeec79cbe32eeb846e6c87.jpg)

![](/api/attachments/XUDDF6P9/fulltext/images/cdd0394baf78ee96e183da6da28152c2fa4e9a6330b7b18169892ae4a6c65db8.jpg)  
Fig. 5. The education level distribution of users

![](/api/attachments/XUDDF6P9/fulltext/images/9b38140b7d49796ee74bae02a10b2f63ba9329d74b38383fd707c78cec8ae181.jpg)  
Fig. 6. The work experience distribution of users

Furthermore, we also analyzed some statistics data about users’ crowdfunding activities, including the participation status, the number of times that they had participated, the total amount of investment, and the factors influencing participation. We found that 178 users had never been a creator or backer and 96 users had been a backer. Only a few users had been a creator. Seventy-three users backed projects one to two times; 18 users backed projects three to four times; 11 users backed projects five to six times; 2 users backed projects seven to eight times. Thirty-one users backed 100 to 500 dollars and 50 users backed 500 to 1,000 dollars. A few users backed over 1,000 dollars. Furthermore, the most important factor in choosing to back is the content of the project. The second factor is economic capacity. The third factor is individual preference. Other factors’ included in the ranking are social media influence, the content of feedback, social relationship influence, and others.

![](/api/attachments/XUDDF6P9/fulltext/images/ed307118bf1b643cf9f7bd29abd47c9889b4752ced00a35873058b3f3a27c68c.jpg)  
Fig. 7. The role distribution of users

![](/api/attachments/XUDDF6P9/fulltext/images/3f76bf11227c7e91f6bafaa28b8c610d81ecc4c2aac3bc805c75a4e0ef77d339.jpg)  
Fig. 8. The number of times participated distribution of users

![](/api/attachments/XUDDF6P9/fulltext/images/4e6cefaed34ae62a26128b1ed85fb220cd8ab233f8a31ed7b92a7a9e72bed904.jpg)  
Fig. 9. The investment distribution of users

![](/api/attachments/XUDDF6P9/fulltext/images/713de8232e80ba75140be5f291d209aef449e7d090cd059a887318025fe5f46c.jpg)  
Fig. 10. The factor distribution of users

## 4.2.2 Project profile

Using the classification of project types used by the crowdfunding websites FlyingV and zeczec, we had 16 types of projects (Design, Music, Film, Entertainment, Publishing, Community, Technology, Food, Travel, Freebird, Photography, Creative, Fashion, Design, Art, and Performance). The creators could input information about an ongoing project on the crowdfunding platforms and could input those which had not yet officially started, and those which might be approved or restarted. A total of 59 different projects were collected. After computing the project phase and project distance, there were 25 projects in Phase 1, 20 projects in Phase 2, and 14 projects in Phase 3. In addition, 36 projects had a project distance of 1, 15 projects had a project distance of 2, and 8 projects had a project distance of 3. Table 3 outlines the statistics of these crowdfunding projects. According to the above project status information, our experiment covered all possible scenarios for evaluating the proposed mechanism.

## 4.2.3 ProjectTree profile

“ProjectTree” is a construction of the different kinds of crowdfunding project types, that is, a combination of categories on Facebook and the types of projects, which indicate the backer preferences and individual preferences of a user. Based on the 282 participants and the projects, we constructed a sampled project tree as shown below (Fig. 11). Note that only a part of the project tree is shown due to the limitations of the layout.

![](/api/attachments/XUDDF6P9/fulltext/images/8923ab31d37329ca2b1399b2f3eb9477f5a5812b10b1f47ba176c66fc348dfaa.jpg)  
Fig. 11. Sample project tree

## 4.3 Criteria weight computing

In the proposed mechanism, we need to know how to compute the importance of four factors: social relationship, backer preference, individual preference, and economic capacity. We invited users to fill an

AHP questionnaire on users’ first usage to get their values about the relative weights of the SIBE matrix. First, users were asked to indicate which factor is the most important to them with respect to three scenarios (family and close friends, acquaintances, and strangers). According to the AHP structure, we used the Likert scale to represent the relative importance: a score of 1 represents “equal importance,” 3 represents “weak importance,” 5 represents “essential importance,” and 7 represents “very strong importance.” We had three scenarios regarding the relationship between the creator and the backer, and used questions aimed at understanding the importance of four factors with respect to these different scenarios. Scenario 1 is a crowdfunding invitation to a friend with a strong tie, Scenario 2 is an invitation to a friend with a weak tie, and Scenario 3 is an invitation to a stranger. Table 4 shows the questionnaire content of scenario 1 as an example.

The final criteria weight combinations derived from SIBE matrixes for different backer groups are outlined in Table 5.

We found that social relationship is the most important factor affecting the willingness of the backer to invest in the crowdfunding projects in Scenario 1 (Phase 1), and individual preference is a more important factor in Scenario 3 (Phase 3). We inferred that when a close friend or family member asks the backer to join his/her crowdfunding project, the backer would fulfill the request because of their strong relationship. However, the social relationship factor becomes weak in Scenario 2 (Phase 2) and the key factor switches to personal preference. If backers do not have a strong personal preference for a project, they will have low willingness to invest in it. Moreover, unless they have a strong interest in crowdfunding projects, the backer is unlikely to invest in a stranger’s fundraising projects.

## 4.4 Suitability computation

To validate the accuracy of suitability-to-recommend in the proposed mechanism, we compared the proposed approach with other benchmark approaches.

1. Phase-based recommendation (our approach): We used the phase-based recommendation to analyze the project’s phase and distance to decide the candidate backer group. We dynamically combined the four factors of social relationship, individual preference, backer preference, and economic capacity to compute the suitability of backers in different fundraising phases. Based on the suitability-to-recommend score for each user, the system generated a list of recommended backers for the creator.

2. Content-based recommendation: This is a recommendation method based on past preference or product. After collecting a user’s preference, the system would recommend relevant projects; therefore, we chose the backer preference and economic capacity as comparisons.

3. Collaborative-based recommendation: This is a recommendation based on a similar user’s preference. The system would find the users who had similar backgrounds or preferences, and recommend the product which other users like. Therefore, we chose the individual preference and economic capacity as comparisons.

4. Social-based recommendation: This is a recommendation method utilizing social influence to generate a trustable backer recommendation list with a combination of economic preference and social relationship. Therefore, we chose social relationship and economic capacity as comparisons.

Content-based recommendation, collaborative-based recommendation, and social-based recommendation are three different approaches with representativeness, and they are grounded on individual preference, user similarity, and social relationship, respectively. In Table 6, we outline the characteristics of these recommendation approaches as follows.

## 5. Results and evaluation

To evaluate the proposed crowdfunding recommendation mechanism, we developed a web-based system to trace users’ behaviors (the “like” and sharing rates), and used online questionnaires to gather feedback from the user about the mechanism with respect to liking, satisfaction, and suitability.

## 5.1 Evaluation of behavior

## 5.1.1 Evaluation of the “like” rate

After the backers received the project invitation, they could choose to “like” the system page through the Facebook plugin function. The like rate is measured as:

$$
L i k e R a t e = \frac {\Phi L i k e T i m e}{\Phi I n v i t a t i o n},\tag{31}
$$

where ?????????????????????? is the total number of invitations sent by the system, and Φ???????????????? the total number of backers’ clicks. As shown in Figure 12, the results show that the proposed phase-based recommendation approach achieved a 0.598 like rate, the content-based approach achieved a 0.338 like rate, the collaborative-based approach achieved a 0.401 like rate, and the social-based approach achieved a 0.454 like rate.

![](/api/attachments/XUDDF6P9/fulltext/images/b28cd890bfdc4db2a163ec4351eee54ac0faba861815a5c5e506742ba9bbb794.jpg)  
Fig. 12 Like rates of the five models

Next, we used a paired-samples t-test to verify the statistical significance of the differences between the like rates for different models. First, we received the values of like rate in five models from the same backers. Totally, 282 backers’ like rate values with respect to the different modes were obtained. Second, we compared the values of like rate of the proposed phase-based model to other benchmark models as a paired group. Third, we used a 95% confidence interval for the difference to verify this. As shown in Table 7, our proposed phase-based recommendation approach significantly outperformed the other methods in terms of like rate.

## 5.1.2 Evaluation of sharing rate

After the backer received the project invitation, they could choose to “share” the system page through the Facebook plugin function. The share times could be obtained from our system record and were measured as:

$$
S h a r e R a t e = \frac {\Phi S h a r e T i m e}{\Phi I n v i t a t i o n}\tag{32}
$$

?????????????????????? is the total number of invitations sent by the system, and Φ??ℎ?????????????? is the total number of backers sharing the invitation. As shown in Figure 13, the results of the like rates show that our proposed phase recommendation approach achieved a 0.404 share rate, the content-based approach achieved 0.266, the collaborative-based approach achieved 0.281, and the social-based approach achieved a 0.356 share rate.

![](/api/attachments/XUDDF6P9/fulltext/images/e3e703710cd7378714acadbae1fc0b43eef04b47d3f12bc5c7e3023a79b256bb.jpg)

Fig. 13 Share rates of the five models

Next, we used another paired-sample t-test to verify the statistical significance of the difference between the share rates for the different models. We used a 95% confidence interval for the difference to verify this. As shown in Table 8, our proposed phase recommendation approach significantly outperforms the other methods in terms of share rate.

## 5.2 Evaluation of questionnaire

We also used a questionnaire to understand the user’s feelings in three respects: (1) liking for the invitation, (2) satisfaction with the project’s context, and (3) willingness to invest in the crowdfunding project. After receiving an invitation for a project, each invited backer was requested to answer the following three questions:

● Question 1: How much do you like this project invitation?

Question 2: How satisfied are you with the project’s context?

● Question 3: How much do you want to invest in the crowdfunding project?

The scale for scoring these three questions was from one to five.

## 5.2.1 Evaluation of liking

Fig. 14 shows the results of how much users liked this project invitation with respect to the different models and scenarios. The value of every model is the average score. We found that the random model has the lowest value of liking for the project invitation, and the phase recommendation model had the highest value. We also saw that social relationship has a relatively high influence on users.

![](/api/attachments/XUDDF6P9/fulltext/images/8451f6987dfc5f35fc9ed010cf046d8bd1d011f85d1477a991053c8834c4ffca.jpg)  
Fig. 14 Liking for the project invitation

## 5.2.2 Evaluation of satisfaction

Fig. 15 shows the results of how satisfied users feel with the project’s context for the different models and scenarios. We found that the random model has the lowest value for satisfaction with the project invitation and the proposed phase model has the highest value. We could see that there is a higher influence from the social relationship in Scenario 1, and could infer that users might support close friends on the basis of the relationship.

![](/api/attachments/XUDDF6P9/fulltext/images/af498299a8da782b3308637e62de1d0f33088043a1d7a8e47aecfe888b9505ab.jpg)  
Fig. 15 Satisfaction with the project invitation

## 5.2.3 Evaluation of willingness

Fig. 16 shows the results in terms of how much users wanted to invest in the crowdfunding project with respect to the different models and scenarios. We found that the random model has the lowest value for willingness to invest in the project invitation, and the phase recommendation model has the highest value. At the same time, we found that preference and economic capacity have a higher influence in Scenario 3. As there was no direct connection between the backer and the creator, the backer would pay attention to the content of the crowdfunding project and their personal economic capacity.

![](/api/attachments/XUDDF6P9/fulltext/images/dcc13ba4ca7a0fbbe2f0c15ff173ef037344442fb792c43d02f29c1cc3aa5de7.jpg)  
Fig. 16 Willingness to invest in the project invitation

## 6. Discussion and conclusion

Crowdfunding has become a trend in fundraising in recent years, and most reward-based crowdfunding is based on an “all or nothing” approach. Our research proposes a phase-based backer recommendation mechanism to improve the success rate of the crowdfunding project by utilizing the power of social networks. We first classify the ongoing projects into various phases by analyzing information such as the project’s goals, its context, and its progress status. Secondly, we analyze the relevance of potential backers to the crowdfunding projects by considering four key factors: (1) social relationship: the relationship between the creator and the backer is evaluated based on their interaction within the social network; (2) individual preference: the personal preference is measured by comments, pages, and clubs from the social network; (3) backer preference: the backer’s preference is measured by their footprint and activity in crowdfunding websites; and (4) economic capacity: an analysis of the personal economic situation from the social network. Finally, utilizing AHP criteria computing, the proposed mechanism identifies suitable backers according to the project’s type, phase, and goal status. The results of our experiments show that the proposed system performs better than the other benchmark approaches. Instead of a one-time recommendation approach, the proposed mechanism continues searching for suitable backers for the creator throughout the various phases, until the project’s goal is achieved and the funds obtained.

## 6.1 Research contributions

Here, we develop a new crowdfunding project recommendation mechanism, and its contributions are as follows. For the theoretical implications, first, we combine the theories of network effect and social capital to develop a novel phase-based recommendation mechanism, which can significantly improve the success rate of crowdfunding. Specifically, we classify the identified relevant backer groups by evaluating social relationships with respect to the various phases of a crowdfunding project. We can ensure a backer’s willingness to invest in crowdfunding projects and improve their degree of trust in the creator based on social relationships. Second, the proposed framework considers multi-criteria factors of social relationship, individual preferences, backer’s preferences, and economic capacity, and we find that dynamically incorporating these four criteria can offer a significantly better recommendation accuracy.

For the practical implications, first, from the application perspective, we design an efficient and effective phase-based recommendation system for a crowdfunding project in which different groups of backers are considered with respect to the status of the project. Based on the experimental results, we prove that the proposed system can improve a backer’s willingness to invest. The existing crowdfunding platforms (e.g., Kickstarter and FlyingV) offer only a platform for the creator, and the success rate has never exceeded 50%. The proposed approach can effectively help the creator to find potential backers and to overcome the current problems of crowdfunding projects. Second, from a business perspective, the proposed mechanism provides greater business value and more opportunities to crowdfunding platforms, as the platforms can obtain money from the successful projects. In addition, as crowdfunding has become a new paradigm for fundraising, the proposed system can contribute to more successful fundraising plans.

## 6.2 Research limitations

There are some limitations to this research, and these are listed as follows. First, the proposed mechanism gathers related information mainly from Facebook; however, there are other popular social media such as Twitter and Weibo. In the future, we will analyze users’ preferences by collecting social activities from several types of social media. Through a more plentiful supply of data sources, we can improve the accuracy of recommendation. Second, although we can observe activities, social media cannot fully reflect the real world. For example, a husband and wife have a very close relationship in reality, although they are likely to have different social circles, and we cannot accurately evaluate their relationship from social media. Thirdly, the proposed mechanism aims to offer a suitable backer list for the creator of a crowdfunding project; however, we cannot track the actual activities of the creator and the backer because of the unavailability of business records. Instead, we use online sharing activities (e.g., “likes” and sharing) and a questionnaire for evaluation. In the future, other traceable activities and measures could be considered to evaluate the accuracy of crowdfunding recommendations.

## 6.3 Future work

There are several potential issues that could be further researched. First, there are many crowdfunding platforms. We can examine and analyze the activities of backers by integrating information from a greater number of different platforms. With more information on users’ habits and activities, we can gain more complete information and accuracy of inference. Secondly, we use information from Facebook to compute individual preferences and social relationships; however, there are other dimensions of activities, which can be used to identify a person’s preferences apart from likes, pages, and clubs. Similarly, we can also compute the social relationship through “pokes” and the frequency of messages. Thirdly, in addition to crowdfunding rewards, there are several other types of crowdfunding platforms. For example, increasing numbers of startups prefer to use crowdfunding to gain entrepreneurial finance, and equity crowdfunding may therefore become another kind of trend in crowdfunding. It would be interesting and valuable to extend the proposed model to equity crowdfunding recommendations by considering more economic parameters. Fourthly, geographic distance may also affect the success of crowdfunding. Raising funds from the backers with less geographical distance is helpful to the completion of a crowdfunding project [18]. Therefore, the geographical location factor can be further considered and integrated in a mobile app system to support location-based crowdfunding campaigns. Finally, crowdfunding is a financing activity, which is required to follow related legislation, such as the Jumpstart Our Business Startups (JOBS) Act in America [45]. A mechanism related to crowdfunding is therefore required to consider legal issues. With the rise of the crowdfunding paradigm, many new issues in terms of laws and regulations for standardizing crowdfunding will emerge for study.

## Author statement

Yung-Ming Li: Conceptualization, Methodology, Validation, Formal analysis, Investigation, Resources, Data Curation, Writing - Original Draft, Writing - Review & Editing, Visualization, Supervision, Project administration, Funding acquisition.

Liou-Jyh Hwa: Methodology, Validation, Formal analysis, Investigation, Data Curation,

Yi-Wen Li: Methodology, Formal analysis, Investigation, Data Curation, Writing - Original Draft

## References

1. J. Bobadilla, F. Ortega, A. Hernando, A. Gutiérrez, Recommender systems survey, Knowledge-Based Systems 46 (2013) 109-132.

2. CKIP, Chinese knowledge and information processing, 2018, Retrieved from http://ckip.iis.sinica.edu.tw/CKIP/engversion/index.htm.

3. G. Cecere, F. Le Guel, F. Rochelandet, Crowdfunding and social influence: an empirical investigation, Applied Economics 49 (57) (2017) 5802-5813.

4. C.M. Chiu, T.P. Liang, E. Turban, What can crowdsourcing do for decision support? Decision Support Systems 65 (2014) 40-49.

5. C.P. Chu, Analytic hierarchy process theory (AHP) theory and practice, 2009, Retrieved from ftp://mail.im.tku.edu.tw/Prof\_Shyur/AHP/AHP2009.pdf.

6. Y. Dong, G. Zhang, W.C. Hong, Y. Xu, Consensus models for AHP group decision making under row geometric mean prioritization method, Decision Support Systems 49 (3) (2010) 281-289.

7. N. Dragojlovic, L.D. Lynd, Crowdfunding drug development: the state of play in oncology and rare diseases, Drug Discov. Today 19 (11) (2014) 1775-1780.

8. D. Easley, J. Kleinberg, Strong and weak ties, In Networks, Crowds, and Markets: Reasoning about a Highly Connected World, Cambridge: Cambridge University Press, 2010.

9. Entrepreneur, The basics of crowdfunding, 2013, Retrieved form https://www.entrepreneur.com/article/228125.

10. H. Feng, J. Tian, H.J. Wang, M. Li, Personalized recommendations based on time-weighted overlapping community detection, Information & Management (2015) 789-800.

11. R. Gatautis, E. Vitkauskaite, Crowdsourcing application in marketing activities, Procedia - Social and Behavioral Sciences 110 (2014) 1243-1250.

12. D. Geiger, M. Schader, Personalized task recommendation in crowdsourcing information systems — Current state of the art, Decision Support Systems 65 (2014) 3-16.

13. Gofundme, Top 10 crowdfunding sites, Retrieved from http://www.crowdfunding.com/.

14. M.S. Granovetter, The strength of weak ties. American Journal of Sociology, 78 (6) (1973) 1360- 1380.

15. X. Han, L. Wang, N. Crespi, S. Park, Á. Cuevas, Alike people, alike interests? Inferring interest similarity in online social networks, Decision Support Systems 69 (2015) 92-106.

16. I.B. Hong, Understanding the consumer's online merchant selection process: The roles of product involvement, perceived risk, and trust expectation, International Journal of Information Management 35 (3) (2015) 322-336.

17. J. Howe, Crowdsourcing a definition. Retrieved from http://crowdsourcing.typepad.com/cs/2006/06/crowdsourcing\_a.html.

18. L. Kang, Q. Jiang, C. H. Tan, Remarkable Advocates: An investigation of geographic distance and social capital for crowdfunding, Information and Management. 54 (3) (2017) 336–348.

19. A.A. Kardan, M. Ebrahimi, A novel approach to hybrid recommendation systems based on association rules mining for content recommendation in asynchronous discussion groups, Information Sciences 219 (2013) 93-110.

20. Kickstarter, The year in Kickstarter 2014 in Kickstarter. Retrieved from https://www.kickstarter.com/year/2014?ref=footer#intro.

21. J.K. Kim, H.K. Kim, H.Y. Oh, Y.U. Ryu, A group recommendation system for online communities, International Journal of Information Management 30 (3) (2010) 212-219.

22. Y.A. Kim, R. Phalak, A trust prediction framework in rating-based experience sharing social networks without a Web of Trust, Information Sciences 191 (2012) 128-145.

23. V. Kuppuswamy, B. L. Bayus, Crowdfunding creative ideas: the dynamics of project backers in Kickstarter, SSRN Electronic Journal (2015) 1-40.

24. N. Kshetri, Success of Crowd-based Online Technology in Fundraising: An Institutional Perspective, Journal of International Management 21 (2) (2015) 100-116.

25. X. Li, M. Wang, T.P. Liang, A multi-theoretical kernel-based approach to social network-based recommendation, Decision Support Systems 65 (2014) 95-104.

26. Y.M. Li, C.L. Chou, L.F. Lin, A social recommender mechanism for location-based group commerce, Information Sciences 274 (2014) 125-142.

27. Y.M. Li, C.T. Wu, C.Y. Lai, A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship, Decision Support Systems 55 (3) (2013) 740-752.

28. Y. Li, Qian, D. Jin, P. Hui, A.V. Vasilakos, Revealing the efficiency of information diffusion in online social networks of microblog, Information Sciences 293 (2015) 383-389.

29. T.P. Liang, S.P. J. Wu, C.C. Huang, Why funders invest in crowdfunding projects: Role of trust from the dual-process perspective, Information & Management. (2018).

30. Y.Y. Lin, A New Fundraising Approach –Preliminary Survey of Crowdfunding Behaviour, Economy Research 14 (2012) 152-172.

31. X. Liu, C. Jiang, Z. Lin, Y. Ding, R. Duan, Z. Xu, Identifying effective influencers based on trust for

electronic word-of-mouth marketing: A domain-aware approach, Information Sciences 306 (2015) 34-52.

32. H. Ma. An experimental study on implicit social recommendation. In Proceedings of the 36th international ACM SIGIR conference on Research and development in information retrieval, ACM (2013) 73-82.

33. A. Majumdar, I. Bose, My words for your pizza: An analysis of persuasive narratives in online crowdfunding, Information & Management. 55 (6) (2018) 781-794.

34. Massolution.com, 2013 The Crowdfunding Industry from http://www.crowdsourcing.org/research (2013).

35. R. Mishra, P. Kumar, B. Bhasker, A Web Recommendation System Considering Sequential Information, Decision Support Systems 75 (2015) 1-10.

36. A. Moisseyev, Effect of social media on crowdfunding project results, Unpublished MA Dissertation, The University of Nebraska–Lincoln, Lincoln, NE, 2013.

37. E. Mollick, The dynamics of crowdfunding: An exploratory study, Journal of Business Venturing 29 (1) (2014) 1-16.

38. M. Sarkar, Fundraising campaign raises more than \$452K for disabled mugging victim, CNN (2015).

39. D. Nevo, J. Kotlarsky. Primary vendor capabilities in a mediated outsourcing model: Can IT service providers leverage crowdsourcing? Decision Support Systems 65 (2014) 17-27.

40. S.C. Parker, Crowdfunding, cascades and informed investors, Economics Letters 125 (3) (2014) 432- 435.

41. S. Pitschner, Pitschner-Finn, Non-profit differentials in crowd-based financing: Evidence from 50,000 campaigns, Economics Letters 123 (3) (2014) 391-394.

42. T.L. Saaty, Decision making with the analytic hierarchy process, International Journal of Services Sciences 1 (1) (2008) 83-98.

43. O. Shafiq, R. Alhajj, J.G. Rokne, On personalizing Web search using social network analysis, Information Sciences 314 (2015) 55-76.

44. O. Spiegel, P. Abbassi, M.P. Zylka, D. Schlagwein, K. Fischbach, D. Schoder, Business model development, founders' social capital and the success of early stage internet start‐ ups: a mixedmethod study, Information Systems Journal. 26 (5) (2016) 421-449.

45. A.R. Stemler, The JOBS Act and crowdfunding: Harnessing the power—and money—of the masses, Business Horizons 56 (3) (2013) 271-275.

46. C.I. Teng, Drivers of interdependence and network convergence in social networks in virtual communities. Electronic Commerce Research and Applications 14 (3) (2015) 204-212.

47. J.C. Wang, C.H. Chang, How online social ties and product-related risks influence purchase intentions: A Facebook experiment, Electronic Commerce Research and Applications 12 (5) (2013) 337-346.

48. R.E. Wheat, Y. Wang, J.E. Byrnes, J. Ranganathan, Raising money for scientific research through crowdfunding, Trends in Ecology & Evolution 28 (2) ( 2013) 71-72.

49. W. Xie, Social network site use, mobile personal talk and social capital among teenagers, Computers in Human Behavior 41 (2014) 228-235.

50. H. Ye, A. Kankanhalli, Investigating the antecedents of organizational task crowdsourcing, Information & Management 52 (1) (2015) 98-110.

51. S.J. Yu, The dynamic competitive recommendation algorithm in social network services, Information Sciences 187 (2012) 1-14.

52. Z. Yu, C. Wang, J. Bu, X. Wang, Y. Wu, C. Chen, Friend recommendation with content spread enhancement in social networks, Information Sciences 309 (2015) 102-118.

53. H. Yuan, R.Y.K. Lau, W. Xu, The determinants of crowdfunding success: A semantic text analytics approach, Decision Support Systems. 91 (2016) 67–76.

54. Zeczec, from https://www.zeczec.com/about (2015).

55. H. Zheng, D. Li, J. Wu, Y. Xu, The role of multidimensional social capital in crowdfunding: A comparative study in China and US, Information & Management 51 (4) (2014) 488-496.

56. C.N. Ziegler, J. Golbeck, Investigating interactions of trust and interest similarity, Decision Support Systems 43 (2) (2007) 460-475.

57. C.N. Ziegler, G. Lausen, L. Schmidt-Thieme, Taxonomy-driven computation of product recommendations, Paper presented at the Proceedings of the thirteenth ACM international conference on Information and knowledge management (2004).

#

## Biography

Yung-Ming Li is a professor at the Institute of Information Management, National Chiao Tung University in Taiwan. He received his Ph.D. in Information Systems from the University of Washington. His research interests include network science, Internet economics, and business intelligence. His research has appeared in IEEE/ACM Transactions on Networking, INFORMS Journal on Computing, Production and Operations Management, Decision Sciences, International Journal of Electronic Commerce, Information and Management, Decision Support Systems, European Journal of Operational Research, International Conference on Information Systems (ICIS), Workshop on Information Technology and Systems (WITS), among others.

Jyh-Hwa Liou is a lecturer at the Department of International Business, Hsin Sheng College of Medical Care and Management in Taiwan. She received Ph.D. degree from the Institute of Information Management, National Chiao Tung University in Taiwan. Her research interests include electronic commerce and business intelligence. Her research has appeared in Decision Support Systems.

Yi-Wen Li received her MS degree from the Institute of Information Management, National Chiao Tung University in Taiwan and BS degree in Information Management from the National Chung Cheng University, Taiwan. Her research interests focus on electronic commerce and social computing.

Table 1. Summary of different recommendation approaches

<table><tr><td>Methods</td><td>Description</td><td>Advantages</td><td>Shortcomings</td></tr><tr><td>Content-based recommendation</td><td>Based on a user&#x27;s previous preferences</td><td>Personalized recommendation</td><td>Lack of diversity</td></tr><tr><td>Collaborative-based recommendation</td><td>Based on the preferences of similar users</td><td>Diverse recommendation</td><td>Rating sparsity and low scalability</td></tr><tr><td>Social-based recommendation</td><td>Based on the social relationships between two users</td><td>Trustable recommendation</td><td>Hard to get the explicit or implicit social information</td></tr><tr><td>Phase-based recommendation</td><td>Based on the type of project, backer&#x27;s preference, social relationship, and the status of the project goal</td><td>Dynamic recommendation with multi-criteria factors</td><td>Need more comprehensive factor analysis</td></tr></table>

Table 2. Summary of dataset

<table><tr><td>Title</td><td>Value</td></tr><tr><td>Number of participants</td><td>282 users</td></tr><tr><td>Number of check-ins</td><td>27,636</td></tr><tr><td>Number of posts</td><td>81,216</td></tr><tr><td>Number of tags</td><td>133,104</td></tr><tr><td>Number of fan pages liked</td><td>11,280</td></tr><tr><td>Number of likes</td><td>345,732</td></tr><tr><td>Number of comments</td><td>225,600</td></tr><tr><td>Average number of friends of users</td><td>280</td></tr></table>

Table 3. Statistics relating to project phase and project distance

<table><tr><td></td><td colspan="3">Project Phase</td><td colspan="3">Project Distance</td><td rowspan="2">Total</td></tr><tr><td></td><td>P1</td><td>P2</td><td>P3</td><td>D1</td><td>D2</td><td>D3</td></tr><tr><td>Design</td><td>3</td><td>2</td><td>1</td><td>5</td><td>1</td><td>0</td><td>6</td></tr><tr><td>Music</td><td>2</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td></tr><tr><td>Film</td><td>1</td><td>2</td><td>0</td><td>2</td><td>1</td><td>0</td><td>3</td></tr><tr><td>Entertainment</td><td>2</td><td>1</td><td>1</td><td>3</td><td>0</td><td>1</td><td>4</td></tr><tr><td>Publishing</td><td>2</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>2</td></tr><tr><td>Community</td><td>6</td><td>4</td><td>3</td><td>8</td><td>3</td><td>2</td><td>13</td></tr><tr><td>Technology</td><td>3</td><td>2</td><td>0</td><td>3</td><td>2</td><td>0</td><td>5</td></tr><tr><td>Food</td><td>0</td><td>2</td><td>0</td><td>1</td><td>1</td><td>0</td><td>2</td></tr><tr><td>Travel</td><td>1</td><td>1</td><td>1</td><td>2</td><td>0</td><td>1</td><td>3</td></tr><tr><td>Freebird</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Photography</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>2</td></tr><tr><td>Creative</td><td>0</td><td>1</td><td>2</td><td>2</td><td>1</td><td>0</td><td>3</td></tr><tr><td>Fashion</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Design</td><td>2</td><td>1</td><td>2</td><td>2</td><td>1</td><td>2</td><td>5</td></tr><tr><td>Art</td><td>1</td><td>1</td><td>2</td><td>2</td><td>1</td><td>1</td><td>4</td></tr><tr><td>Performance</td><td>0</td><td>3</td><td>0</td><td>2</td><td>1</td><td>0</td><td>3</td></tr><tr><td>Total</td><td>25</td><td>20</td><td>14</td><td>36</td><td>15</td><td>8</td><td>59</td></tr></table>

Table 4. Content of questionnaire for Scenario 1

<table><tr><td colspan="9">Scenario 1</td></tr><tr><td>Question 1</td><td colspan="8">If your close friends like: a family member invites you to join his/her crowdfunding projects and invest money in it. When you consider whether to join the crowdfunding project, which factor is relatively more important to you?</td></tr><tr><td></td><td>7:1</td><td>5:1</td><td>3:1</td><td>1:1</td><td>1:3</td><td>1:5</td><td>1:7</td><td></td></tr><tr><td>Social Relationship</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>Individual Preference</td></tr><tr><td>Social Relationship</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>Backer Preference</td></tr><tr><td>Social Relationship</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>Economy Capacity</td></tr><tr><td>Individual Preference</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>Backer Preference</td></tr><tr><td>Individual Preference</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>Economy Capacity</td></tr><tr><td>Backer Preference</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>Economy Capacity</td></tr></table>

Table 5. Weights for different backer groups

<table><tr><td></td><td>Social Relationship</td><td>Individual Preference</td><td>Backer Preference</td><td>Economy Capacity</td></tr><tr><td>Candidate backer group 1 (Phase 1)</td><td>0.461</td><td>0.299</td><td>0.163</td><td>0.07721</td></tr><tr><td>Candidate backer group 2 (Phase 2)</td><td>0.3292</td><td>0.359</td><td>0.211</td><td>0.10031</td></tr><tr><td>Candidate backer group 3 (Phase 3)</td><td>0.1766</td><td>0.499</td><td>0.22</td><td>0.10448</td></tr></table>

Table 6. Different recommendation benchmarks

<table><tr><td>Benchmarks</td><td>Method</td><td>Factors</td></tr><tr><td>Phase-based Recommendation</td><td>Analyze the project&#x27;s phase and distance and dynamically combine all factors to recommend candidate backers in each phase</td><td>Social relationshipIndividual preferenceBacker preferenceEconomic capacity</td></tr><tr><td>Content-based Recommendation</td><td>Analyze the backer preference and recommend relevant projects</td><td>Backer preferenceEconomic capacity</td></tr><tr><td>Collaborative-based Recommendation</td><td>Find the backers who have similar background or preference and recommend the project, which other backers like</td><td>Individual preferenceEconomic capacity</td></tr><tr><td>Social-based Recommendation</td><td>Analyze a backer&#x27;s social information, including user preferences, the general acceptance of the item, and social influence to recommend trustable backers</td><td>Social relationshipEconomic capacity</td></tr></table>

Table 7. Paired-sample t-test of like rate

<table><tr><td rowspan="3">Paired Group</td><td colspan="5">Paired Differences</td><td rowspan="3">T</td><td rowspan="3">Sig. (2-tailed)</td></tr><tr><td rowspan="2">Mean</td><td rowspan="2">Std. Deviation</td><td rowspan="2">Std. Error Mean</td><td colspan="2">95% Confidence Interval</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td>Phase-based vs. Random</td><td>-0.36</td><td>0.03</td><td>0.01</td><td>-0.39</td><td>-0.34</td><td>-33.57</td><td>0.00</td></tr><tr><td>Phase-based vs. Content-based</td><td>-0.26</td><td>0.01</td><td>0.00</td><td>-0.27</td><td>-0.25</td><td>-62.14</td><td>0.00</td></tr><tr><td>Phase-based vs. Collaborative-based</td><td>-0.20</td><td>0.01</td><td>0.00</td><td>-0.21</td><td>-0.19</td><td>-51.43</td><td>0.00</td></tr><tr><td>Phase-based vs. Social-based</td><td>-0.15</td><td>0.01</td><td>0.00</td><td>-0.16</td><td>-0.14</td><td>-39.24</td><td>0.00</td></tr></table>

Table 8. Paired-samples t-test of share rate

<table><tr><td rowspan="3">Paired Group</td><td colspan="5">Paired Differences</td><td rowspan="3">T</td><td rowspan="3">Sig. (2-tailed)</td></tr><tr><td rowspan="2">Mean</td><td rowspan="2">Std. Deviation</td><td rowspan="2">Std. Error Mean</td><td colspan="2">95% Confidence Interval</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td>Phase-based vs. Random</td><td>-0.17</td><td>0.11</td><td>0.04</td><td>-0.26</td><td>-0.09</td><td>-4.65</td><td>0.00</td></tr><tr><td>Phase-based vs. Content-based</td><td>-0.09</td><td>0.14</td><td>0.05</td><td>-0.21</td><td>0.02</td><td>-1.92</td><td>0.00</td></tr><tr><td>Phase-based vs. Collaborative-based</td><td>-0.08</td><td>0.16</td><td>0.06</td><td>-0.22</td><td>0.06</td><td>-1.39</td><td>0.00</td></tr><tr><td>Phase-based vs. Social-based</td><td>0.03</td><td>0.13</td><td>0.05</td><td>-0.08</td><td>0.14</td><td>0.66</td><td></td></tr></table>
