---
otero_id: 4872
otero_key: "HJWGCQVE"
title: "A social endorsing mechanism for target advertisement diffusion"
authors: "Lien-Fa Lin; Yung-Ming Li; Wen-Hsiang Wu"
year: "2015"
journal: "Information & Management"
doi: "10.1016/j.im.2015.07.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: A Social Endorsing Mechanism for Target Advertisement Diffusion

Author: Lien-Fa Lin Yung-Ming Li Wen-Hsiang Wu

![](/api/attachments/HJWGCQVE/fulltext/images/762cc36e27325b5a05fff2e1f1db4f9d8ae80bff49545d1f692df86b06ced913.jpg)

PII: S0378-7206(15)00072-5

DOI: http://dx.doi.org/doi:10.1016/j.im.2015.07.004

Reference: INFMAN 2825

To appear in: INFMAN

Received date: 30-11-2012

Revised date: 19-5-2015

Accepted date: 4-7-2015

Please cite this article as: L.-F. Lin, Y.-M. Li, W.-H. Wu, A Social Endorsing Mechanism for Target Advertisement Diffusion, Information and Management (2015), http://dx.doi.org/10.1016/j.im.2015.07.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A Social Endorsing Mechanism for Target Advertisement Diffusion

Lien-Fa Lin<sup>a</sup> • Yung-Ming Li<sup>b</sup> • Wen-Hsiang Wu<sup>b</sup>

<sup>a</sup> Department of Information Communication, Kao Yuan University, Kaohsiung, 821, Taiwan lienfa0704@gmail.com

<sup>b</sup> Institute of Information Management, National Chiao Tung University, Hsinchu, 300, Taiwan yml@mail.nctu.edu.tw • sezuru@gmail.com

\*Corresponding author: Yung-Ming Li (yml@mail.nctu.edu.tw)

E-mail: Lien-Fa Lin (lienfa0704@gmail.com), Wen-Hsiang Wu (sezuru@gmail.com)

## ABSTRACT

Social media play an increasingly important role in people’s daily lives and attract companies to conduct marketing activities. How to effectively utilise this new media for distributing promotional advertisements to suitable customers is thus an important issue. In this research, an endorser-based social diffusing mechanism, which considers the factors of preferences, influence, and the diffusion power of users, is proposed to enhance the effectiveness of target advertising by discovering the most appropriate endorsers that can propagate the ads to the identified target users. Our experimental results show the proposed model can appropriately enhance satisfaction as well as target delivered rate.

Keywords: Social media, Social endorsement, Diffusion mechanism, Target advertising, Influence analysis

#

## 1. Introduction

Social media are playing a more and more important role in people’s daily lives. As a functional definition, social media refers to the interaction of people and also to creating, sharing, exchanging, and commenting contents in virtual communities and networks [64]. Social media (e.g., Twitter, Plurk, Facebook) has become a popular space for marketers to promote products and customers share their opinions about product or store. One business survey pointed out that the number of social media users will increase to 1.43 billion in 2012. This number will be an increase of about 20% compared with the previous year. It is also forecasted that more than 70% of Internet users will visit social media sites at least once a week in the next three years. Further, the user rate of social media will rise from 20% to 25% by 2014 [16]. This growing user population of social media shows their increasing importance and promising business opportunity.

Social media are an important source for people to get information. According to the study of [26], about 70% of people use social media to receive updated information on a company, brand, or product. In addition, about 45% of people use social media to distribute information. Sensis [56] reports that keeping connections with friends and family, sharing information, and coordinating social events are the main purposes for which people use social media. This situation indicates that social media have become major platforms in personal information exchanging and communicating.

Besides personal usage, companies have also increasingly conducted many activities on social media. According to the report by Stelzner [61], the majority (93%) of companies use social media as a marketing tool and half of marketers have experience of applying social media in marketing for at least one year. Further, at least 73% of these marketers plan to increase their use of social media, such as YouTube, Facebook, and Twitter. Meanwhile, half of B2C (business to customer) companies conduct marketing and advertising activities using the Internet and social media (e.g. email marketing, search engine optimisation, social marketing).

With this rising trend, how to apply social media to create value in business is becoming a great issue for enterprises. Advertising is one of the most common commercial activities implemented using social media. With social media, the advertiser can exploit the power of social influence to deliver advertising messages via word-of mouth. However, while marketers are increasingly launching advertisements on social media, the effectiveness of this new advertising approach is advertising sponsors’ main concern.

Target advertising and social advertising are two important ways to improve the effectiveness of advertisements. Target advertising focuses on identifying the right (targeted) receivers of the advertisement, while social advertising emphasises finding the right (influential) endorsers to propagate the advertisement. Both advertising strategies can enhance the effectiveness of the advertisement, as people like an advertisement to fit their preferences and enjoy sharing them with friends. Therefore, to improve the effectiveness of social media advertising advertisers face three main issues.

(1) The objectives of advertising: There are several main purposes of advertising, including informing, evoking emotions, and triggering actions [47]. The purposes of advertising can also be categorised into informative and persuasive functions in general [5,46,48]. The informative function of advertising focuses on delivering the information of an advertisement. Marketers can carry out informative advertising to deliver product-related and promotional information to consumers. They can inform consumers when and where a sale will be held. Advertising information is generally timecritical and/or location-sensitive. For example, when jewellery is auctioned for a limited period of time, the auction information should be time-critical and more attractive to women than it is to men. Contrastingly, persuasive advertising aims to affect the tastes of consumers and offer customers perceived product value and brand loyalty. It offers less (and less direct) information on product promotions than informative advertising. The different objectives and approaches of advertising also affect its effectiveness. A good advertising mechanism should have the adaptive capability to improve advertising performance according to the advertising objective and mission.

(2) The audience of advertising: The targeted audience is also a critical factor that affects the effectiveness of advertising. How to attract the audience and make them feel entertained with the received advertising messages is an important issue. To meet the advertising objective the target audience should be correctly identified. Kelly et al. [32] note the important issue of advertising avoidance. This suggests that media users resist accepting the unfavourable information delivered by advertisements [60]. They become unfit receivers and might have negative emotions about annoying advertisements. This suggests that the audience of advertising should be chosen carefully or advertising effectiveness might diminish. The main objective of target advertising is to identify the right audience to receive the advertisement.

(3) The distribution of advertising: Selecting a proper medium to advertise is important for marketers. Traditional advertising mediums, such as print and television, have their limitations. Because of its greater communicating capability, the Internet has become a popular medium for advertising. However, proper advertising strategies on this medium still vary with the objectives of advertising. Advertising messages can be directly distributed by firms or the advertising agent to target customers. While this type of advertising approach is cost saving, most users may feel disturbed and have negative impressions due to unfavourable ads and senders. Social advertising, utilising the inherent power of the endorsing and filtering feature of social networks, can alleviate this problem and improve the value of the advertising delivered.

In this research, by analysing preferences, influence, and diffusing power, we combine the advantages of the target and social advertising approaches and develop a novel social endorsing mechanism to enhance effectiveness as well as the target coverage of advertising, which is an emerging research avenue for using social media in the context of online advertising. The proposed mechanism can feasibly distribute various types of advertisements (such as branding and product promotions) by considering the following three aspects. Firstly, from a targeting aspect, suitable receivers can be found based on the content and characteristics of individual information. Stockman [62] argues that “making sure the right ads reach the right demographic is the first step towards smart marketing”. Evaluating the fit between the content of advertisements and receivers should be considered first before advertising activities are launched. Secondly, from an endorsing aspect, endorsement by friends is a powerful advertisement distributing strategy to reduce negative reactions during advertising. In particular, when endorsers are selected from the friends of receivers, the advertisement will be accepted by receivers more easily. This helps overcome the issues on the advertising audience, fosters information propagation, and reduces advertising avoidance. Thirdly, from a synthesising aspect, the proposed mechanism combines the power of both target and social

#

advertising. When targeted receivers are identified and clustered by preference analysis, then the system can further understand the most influential endorsers to deliver advertising messages. Filtering targeted users helps scale down the scope of advertising and discovers endorsers effectively. Marketers can thus meet their expected outcomes based on the objective of advertising by utilising this synthesised target and a social advertising strategy. The proposed mechanism is validated by experiments conducted in Plurk, one of the most popular micro-blog services. Our experimental results show that the proposed model can effectively enhance advertising campaigns (particularly promotional and time-critical advertisements) in terms of advertisement relevance and target delivered rate (TDR).

The remaining sections are organised as follows. Section 2 discusses the related literature. In Section 3, the research model is demonstrated, while the experiments are presented in Section 4. The experiment results and evaluation are discussed in Section 5. Finally, Section 6 concludes this study and presents directions for future research.

## 2. Related Works

## 2.1 Social Media and Online Advertising

The advents of the Internet and communications technology have facilitated the rise in social media. Social media can be interpreted as an Internet-based platform that emphasises human interactions [58]. According to the categorisation of Kaplan and Haenlein [29], collaborative projects, blogs, content communities, social networking sites, virtual game worlds, and virtual social worlds are all kinds of social media. Furthermore, Heinonen [22] points out that social media activities can be categorised by motivation. The features of social media are generally divided into three categories: information processing, entertainment activities, and social connections. These categories of functionality imply that social media provide an open platform for mutual communication, information diffusion, and social interaction. With the emerging trends and the promising popularity, researchers have attempted to analyse the characteristics and enhance the practical applications of social media [30]. Kim et al. [35] investigate the factors influencing the adoption of social media from the viewpoint of information needs in order to realize each user's behavior regarding information adoption. To better figure out users' behavior, many researchers analyze social interaction, social

#

influence, and information diffusion in social media [12].

With this rising new media, enterprises are exploring business opportunities, with online advertising one of the most popular commercial ventures. Online advertising has several different implementation forms and strategies. The contextual ads on search engines [42], banner ads [31], affiliated marketing [49], and traditional e-mail marketing are all branches of online advertising. Luo et al. [42] investigate how search advertisement placement affects search users’ brand recall and recognition. Kazienko and Adamski [31] propose a system that takes web usage, content mining techniques, certain advertising policies, and important factors for both publishers and advertisers into consideration for personalising web banner advertising. Ngai [49] presents an application that adopts a multi-criteria approach for the analysis and comparison of websites for online advertising. importance, advertising effectiveness, and branding attitudes.

Hinz and Spann [24] argue for the importance of the relationship between information diffusion and advertising. Some research points out that web-based advertising without interactivity would be more like traditional print advertising [63]. This suggests that focusing on the behaviours of users is a way to leverage the advantages of online advertising. Since interactions among people are a characteristic of social media, conducting online advertising activities on social media can overcome the drawbacks of traditional web advertising, which lacks interactivity.

Customer targeting is a basic concept in marketing. The concept of customer targeting is opposite to mass marketing. By specialising and segmenting the market, specific users and customers can be identified [10]. However, even though the target advertising approach can effectively identify the end customer, an effective distribution channel is required to ensure marketing success. For example, when target advertising is applied in the form of direct marketing, the audience could feel offended and refuse to accept the advertisements due to the unfavorable sender and ads. Kelly et al. [32] notes this important issue of advertising avoidance. The study of advertising avoidance suggests the media users resist accepting the unfavorable information that advertisements delivered [60]. They become unfit receivers and might have negative emotions on the annoying advertisements. This diminishes the effectiveness of the advertisement. Social advertising, which utilizes the inherent power of endorsing and filtering features in social networks, can alleviate this problem and improve the value of advertising delivered.

Regarding the distribution channel of advertisements, Fiorillo [18] notes that social advertising can distribute appropriate advertisements through the social networks of users. Many researchers have proposed several available online advertising models of social media websites [15,39]. This indicates that using online advertising on social media is important and implementable. Bagherjeiran and Parekh [4] point out that the social relations and social interactions between users are critical factors in realising social advertising activities. In the present research, we also utilise these two factors to design a social advertising strategy and develop a social endorsing mechanism to enhance the value of target advertising.

## 2.2 Information Diffusion

The issue of information diffusion initially appeared in the area of complex networks. Computer scientists have proposed a number of models, including the linear threshold model [33,66], independent cascade model [33], and incremental chance model [50], to simulate information diffusion. In these models, the chance that each node is influenced increases with the number of its influenced neighbours. In recent years, with the rising popularity of social media, information diffusion in social networks has become a promising and important issue. Several diffusion models have been proposed to analyse the diffusion of innovation in social networks. Hsueh and Chen [25] propose a peer-generated coupon sharing scheme on a mobile platform that sends coupons to targeted influential members and encourages them to forward these onto friends for increasing business opportunities. Hinz and Spann [23] develop a decision support system that enables sellers to assess the impact of information diffusion including analysing the effects of different network structures and the profitability of different seller strategies. These widely studied models can be generalised into the categories of threshold models and cascade models [13].

Generally, diffusion models can be categorised into two approaches: econometric and explanatory [57]. Econometric approaches principally address forecasting product growth [43]. When market scale and the market growth rate are insufficient, econometric modelling is the most applicable method [54]. The other approach, the explanatory approach, is also known as the “consumer diffusion

Researchers have studied information diffusion in various contexts using social network analysis. In order to examine how friends affect one’s decision to be vaccinated against the flu Rao et al. [52] combine information on social networks with medical records and survey data. Kuandykov and Sokolov [38] suggest that when the total population and initial adopters stay the same, the spreading speed of innovation through a clustered random network will be faster than that through a uniform cluster.

Influence is applied in broad contexts of information diffusion in social networks [19]. Richardson and Domingos [53] study the influence maximisation problem and propose a probabilistic solution. Kempe et al. [33] formulate the problem of finding a set of influential individuals as an optimisation problem and develop an algorithm for a diffusion model.

Finding a subset of influential individuals has many applications [34]. Iribarrena and Moro [27] propose an affinity path mechanism and validate that the affinity between spreaders’ preferences and the message content drives the propagation of viral marketing. This suggests that matching the attributes of the messages with the preferences of spreaders would also affect the efficiency of diffusion. For developing an effective marketing strategy, matching spreaders and receivers should be a critical issue.

In recent studies, influence diffusion in social networks has been investigated from a decisionmaking point of view [11,68,70]. For example, how to exploit word-of-mouth marketing may first consider different types of business objectives, such as value creation (e.g. maximising the number of ultimately influenced nodes and the expected lift in profit) and cost reduction (e.g. minimising the seed endorsers that can guarantee complete diffusion coverage and the expected time to complete diffusion). In this research, we design a social endorsing mechanism to appropriately balance the diverse objectives of online advertising, namely coverage and the satisfaction rates of target users.

## 2.3 Social Influence

Social influence refers to how individuals change their decisions as a result of interactions with others who have interests similar to their own [55]. Social influence can change users’ thoughts and actions. For example, customers’ purchasing decisions may be affected by buying experiences shared by other users with strong social influence [36], which tells us about the impact of social influence in consumers’ decision-making process. Social actions are powerful because they act as trusted referrals and reinforce the fact that people influence people. Different users’ characteristics, preference, relations, and actions on the network lead to individuals’ various infection probability. Some researchers measure the influential strength by analyzing the number of network links and users relation and interaction in the network to identify the influential nodes for social advertising [67]. Others exploit social network analysis techniques, to evaluate the influential nodes from the aspect of the node's structural position or a temporal notion of “node's distance”, such as degree centrality, and closeness centrality [37]. Studying social influence can help us better understand why certain information are transmitted faster than others and how we could help advertisers and marketers design more effective campaigns [9]. By revealing influential factors and realizing the processes of the information diffusion, marketers can predict when and how the information spreads over social networks to maximize the expected spreading performance [33]. In this paper, we consider the factors of user’s popularity (measure influential strength in [67]) and centrality degree (measure influence node in [37]) to measure the social influence of an endorser. Incorporating the factors of user preference, social influence, and propagation capability, we propose a social diffusing mechanism to identify the appropriate endorsers with high diffusion power from the social network to deliver relevant advertisements broadly.

## 2.4 Endorser Marketing Strategy

Marketing with endorsers is a common and useful strategy. The person who influences a certain individual or group is called the endorser [17,44]. Kiss and Bichler [37] widely review the general

#

centrality measures for selecting influencers/endorsers from a customer network for online marketing. An endorsed advertising message can affect the behaviours of customers. Endorser marketing can be categorised into celebrity endorsement and non-celebrity endorsement. A celebrity endorser is a person who uses their public recognition on behalf of a consumer good by appearing with it in an advertisement. In other words, a celebrity endorser has a special influence on people’s behaviours. Previous studies show that celebrity endorsement brings lots of advantages such as image polishing, brand introducing, brand repositioning, attention increasing, producing positive attitudes towards advertising, and increasing purchase intentions [3,71]. Advertising researchers note that a positive emotional attitude is important in advertising and can be viewed as an indicator of advertising effectiveness [1,8]. Lee et al. [40] also indicate that greater pleasure and rousal emotions significantly lead consumers to have more positive attitudes when Internet shopping. This suggests that endorsement strategy, especially the celebrity endorser approach, is helpful to conduct advertising and can be expected to have better effectiveness. Since endorsers can influence the behaviours of customers, the endorsement mechanism would be helpful for advertising. The power of endorserbased advertisement has been examined statistically in many researches [65], but the development of feasible systems is still in its infancy. Existing proposed systems (e.g. Beloff and Pandya [7], Mitra and Baid [45]) do not take social relation and interaction into consideration. The experimental studies conducted by Lim et al. [41] also find that with the endorsement of satisfied customers who are similar in characteristic to the potential buyers, consumers’ trusting beliefs about the store increase. People who share common characteristics tend to perceive each other more positively and hence are more likely to trust each other. Besides the power of social influence, endorsers are often trusted by the people that they can affect.This suggests that the endorsement mechanism can enhance customer acceptance of advertising and decrease advertising avoidance. In this research, we adopt the concept of endorser marketing to develop a social endorsing mechanism to enhance the value of the advertisement received.

## 3. System Framework

#

To improve positive impressions through a successful TDR we should first find out the right target audience to receive an advertisement (e.g. product promotions) and utilise the social endorsement approach to identify the right people to propagate the advertisement to do so. These advertisements would be mainly spread within a specified scope and realise the spirit of “distributing the right advertisement to the right people via the right endorsers (friends).” Figure 1 depicts the processes involved in this proposed system.

1. The system identifies targeted customers according to the product and promotion characteristics of the advertisement the advertiser is planning to distribute.

2. The system constructs a network of candidate endorsers by combining the close friends linked by the customers who are included in the set of targeted customers. The friends included in the candidate network should be also interested in the advertisement to be distributed.

3. The system discovers the most appropriate endorsers from the network of candidate endorsers (“seed endorsers”). These seed endorsers should be active themselves and influential among their friends.

4. The system sends the advertisement to the seed endorsers included in the final set of selected endorsers. They serve as the initial endorsing nodes for diffusing the advertisement.

5. Endorsers share the advertising message with their friends spontaneously and the message is further propagated by the friends of friends to reach the targeted customers.

![](/api/attachments/HJWGCQVE/fulltext/images/5204884818961d2217e16afdb453c10d227b4c8e9d119fc3a58790c91fcf43cd.jpg)  
Figure 1 Process flow of targeted social advertising

Figure 1 shows that a distant endorser with a high degree of connection may cover a wide scope of users in the social network, but uncertainty in information diffusion also increases due to propagation distance. Contrarily, a nearby endorser knows the preferences of his or her friend and can deliver information to target users successfully. However, this kind of endorser may propagate information only within a limited range due to a low degree of connection. The issue when selecting ideal endorsers is thus to balance the trade-off between node coverage and TDR. To meet the objective of distributing target advertisement using the social endorsing approach several techniques are required. The components considered in the system framework include the target discovering mechanism, endorser candidate network reconstructing mechanism, and seed endorser identifying mechanism. The system framework is depicted in Figure 2.

![](/api/attachments/HJWGCQVE/fulltext/images/cbd5e60f77169bfe8094d0b57643979c22436d09c9e717072d2e6a4a7f614161.jpg)  
Figure 2 Framework of the targeted social advertising mechanism

The three main components used in the different stages of process in the system are:

(1) Target discovering mechanism: In the first stage, the target discovering mechanism will discover the group of target users by conducting customer preference analysis and advertisement attribute analysis. Users whose preferences match the advertisement will be selected as target users.

(2) Endorser candidate network constructing mechanism: In the next stage, the system will construct the endorser candidate network through network expanding and filtering processes. Expanding from target users, the friends of target users with an interest in the advertisement will be filtered and selected as the candidates of endorsers.

(3) Seed endorser identifying mechanism: Finally, the seed endorser identifying mechanism will find out the final set of appropriate endorsers by analysing the influence and diffusing power of the nodes included in the endorser candidate network.

## 3.1 Target Discovering Mechanism

The target discovering mechanism analyses the fit degree between the preferences of users and the type of advertisement to promote. Target users will be discovered by measuring the similarity between the categories of their preferences and the category of the advertisement.

## 3.1.1 Customer Preference Analysis Module

As the property of a user group is considered to be a crucial factor, using preference analysis techniques to identify target users is essential. This module is designed to analyse the preferences of users and categorise them. The basic measurement is to analyse the profiles and posts of users. This helps find the keywords that represent the main characteristics and tendencies of users.

Static Preference Identification. The static preferences of users are the information explicitly discovered from their profiles. As profile data will not be updated frequently, it is viewed as “static”. These data can be collected from commonly self-reported information.

Dynamic Preference Identification. The interests of users are not always consistent. As noted above, user profiles will not be updated frequently and this makes it impossible to ascertain changes in their interests from their profiles. However, their changes in interests can be found from their recent conversations. What they mention frequently in recent conversations might indicate their new focuses and interests. The information mined and discovered from users’ posts is defined as “dynamic”. Dynamic preferences are used to assist and enrich the static preferences discovered from user profiles. According to the frequently used keywords discovered from the messages of interactions, we can categorise them by matching them with the keywords described in the product categories developed in subsection 3.1.2. According to the preferences of users, they can be grouped into different categories.

## 3.1.2 Advertisement Attribute Analysis Module

The advertisement attribute analysis module is designed to develop a category tree for positioning a given advertisement. Target users are discovered and identified by analysing the similarities between users’ preference categories and the advertisement’s category. We use the distance in the tree hierarchy to measure the similarity between user preferences and advertisement types.

Category Tree Construction. A category tree will be built for calculating the matching levels between user preferences and an advertisement. In this research, the category tree is built by referring to the common categories of products used in well-known e-commerce websites (e.g. Amazon and eBay). In this tree structure, the closer a node is to the root, the more general the category is. In other words, when a node is located in a leaf position, this suggests that it represents a more specific category.

Similarity Computation. As mentioned above, user preferences will be defined by keyword categories. All users will be allocated to proper category nodes in the category tree. Utilising the concept of the distance between two nodes in a graph [69], the distance of the first mutual category node from the category nodes they are located under is calculated. For example, user u is allocated under category $C _ { 1 } \ ( \Phi C a t e ( u ) = C _ { 1 } )$ and product $p$ is under category $C _ { 2 } \ ( \Phi C a t e \ l ( p ) = C _ { 2 } )$ $C _ { m }$ represents the first mutual node of $C _ { 1 }$ and $C _ { 2 }$ . Therefore, the distance from $C _ { 1 }$ to $C _ { m }$ and $C _ { 2 }$ to $C _ { m }$ will be used to measure their similarity based on the category tree. We denote the length of the path from nodes $C _ { 1 }$ and $C _ { 2 }$ to node $C _ { m }$ as $D _ { I }$ and $D _ { 2 }$ respectively and the length of the path from $C _ { m }$ to the root node in the category tree as $D _ { r m } .$ . This similarity degree, which stands for the matching level of u ’s preference about a product advertisement $p$ , is formulated as:

$$
\operatorname{Sim} \left(C _ {1}, C _ {2}\right) = \frac {2 D _ {r m}}{D _ {1} + D _ {2} + 2 D _ {r m}}.\tag{1}
$$

![](/api/attachments/HJWGCQVE/fulltext/images/fee19d9ebc6160fefedca755e345036ac4e2c6980ac20cf485de612162d8034d.jpg)  
Figure 3 The similarity concept in the category tree

As a user may have multiple preferences, we can further calculate the average fitness score using the following formula:

$$
\operatorname{Fitness} (u, p) = \frac {1}{\left| \Phi \operatorname{Cate} (u) \right|} \cdot \sum_ {C _ {u} \in \Phi \operatorname{Cate} (u)} \left(\operatorname{Sim} \left(C _ {u}, \Phi \operatorname{Cate} (p)\right)\right).\tag{2}
$$

where $\Phi C a t e ( u )$ denotes the set of categories user u’s preferences belong to. By utilising the fitness computation formula, we can identify the set of targeted customers that have an interest (i.e. high similarity with the advertisement) in the advertising message the sponsor would like distribute. We denote the set of target customers as $\Theta _ { _ { T } } . \Theta _ { _ { T } } = \left\{ u \ : | \ : F i t n e s s ( u , p ) > \varepsilon _ { s } \right\}$ , where $p$ is the product to promote and $\varepsilon _ { s }$ is the threshold for fitness acceptance level.

## 3.2 Endorser Candidate Network Constructing Mechanism

After target users are discovered, an endorser candidate network can be constructed and continuously expanded from them. A targeted user can also be selected as an endorser for message propagating. Therefore, targeted users should be included in the endorser candidate set $\Theta _ { E }$ (i.e. $\Theta _ { \ / T } \subset \Theta _ { \ / E } )$ .

As people tend be influenced by close friends and similar people, the endorser candidate filtering criteria can be evaluated according to a user’s friendship and similarity with targeted users. However, people are only likely to share information they feel is interesting with their close friends and people that have the same interests. Thus, we denote $\Phi C a t e { \left( u _ { i } \right) }$ as the set of categories user $u _ { i }$ is categorised into. Using Jaccard index, the user preference category similarity between user $u _ { i }$ and user $u _ { j }$ is computed as:

$$
U P C a t e _ {s i m i} \left(u _ {i}, u _ {j}\right) = \frac {\left| \Phi C a t e \left(u _ {i}\right) \cap \Phi C a t e \left(u _ {j}\right) \right|}{\left| \Phi C a t e \left(u _ {i}\right) \cup \Phi C a t e \left(u _ {j}\right) \right|}.\tag{3}
$$

Further, we denote $R C \left( u _ { i } , u _ { j } \right)$ as the relation closeness intensity function between users $u _ { i }$ and $u _ { j }$ . $R C \left( u _ { i } , u _ { j } \right)$ can be formulated as

$$
R C \left(u _ {i}, u _ {j}\right) = F d \left(u _ {i}, u _ {j}\right) \times U P C a t e _ {\text { simi }} \left(u _ {i}, u _ {j}\right) \times I n t e r a c t \left(u _ {i}, u _ {j}\right),\tag{4}
$$

where $F d ( u _ { i } , u _ { j } )$ represents whether users $u _ { i }$ and $u _ { j }$ are mutual friends or not. $F d \left( u _ { i } , u _ { j } \right) = 1$ indicates users $u _ { i }$ and $u _ { j }$ are mutual friends and $F d \left( u _ { i } , u _ { j } \right) = 0$ otherwise. $I n t e r a c t ( u _ { i } , u _ { j } )$ represents whether users $u _ { i }$ and $u _ { j }$ have interacted recently. Interact $\left( u _ { i } , u _ { j } \right) = 1$ indicates users $u _ { i }$ and $u _ { i }$ have interacted recently (e.g. at least seven times during the past week) and Interact $\left( u _ { i } , u _ { j } \right) = 0$ otherwise.

Starting from target users, the endorser candidate network is constructed by including users who are friends of and have preference similarities with a target user. Further, the users to be recruited as candidate endorsers should have interacted with the target user recently. The endorser candidate network will then be expanded continuously from these newly recruited users by including other users, using the same criteria. Specifically, we denote $E C N ( l )$ as the set of nodes included in the endorser candidate network, which is constructed by nodes expanding for l layers. The network expanding

process can be formulated as

$$
\Theta_ {E} (l + 1) = \Theta_ {E} (l) \bigcup \left\{u _ {i} \mid u _ {i} \notin \Theta_ {E} (l), u _ {j} \in \Theta_ {E} (l), R C \left(u _ {i}, u _ {j}\right) > \varepsilon_ {c} \right\},\tag{5}
$$

where $\Theta _ { E } ( l )$ denotes endorser candidate set for l layers , $\Theta _ { T }$ denotes the target users set. $\Theta _ { _ { E } } \left( 0 \right) = \Theta _ { _ { T } }$ $ { \varepsilon } _ { c }$ is the threshold of relation closeness level. In this research, we construct the network of endorser candidates after expanding three layers (l=3). For simplicity, in the rest of the manuscript, we omit the parameter l and use only $\Theta _ { E }$

## 3.3 Seed Endorser Identifying Mechanism

After the endorser candidate network is constructed, the system will identify suitable seed endorsers from the network and delegate them to deliver the advertisement. In this research, users’ social factors (influence and diffusing power) are analysed to find out suitable seed endorsers. The following modules are designed to identify suitable seed endorsers.

## 3.3.1 Influence Analysis Module

Excellent endorsers should have a great influence on their friends. The greater the influence, the more people he or she can influence. In this sense, the influence of all candidate users should be analysed. Users’ relation and interaction in the network can be used to analyse the influence strength and identify the influential nodes for social advertising [67]. Highly connected nodes, the hubs, play important roles in information propagation in networks [7,71]. When a person has many neighbours in the network, he/she actually plays the role of a hub and has great importance and controllability in message spreading. The combination of interaction (popularity degree) and connection structure of users is treated as the metric of social influence in social network.

Popularity Computation. Popularity influence is used to measure the popularity degree of a user’s posts. The messages posted by a user might be responded to, forwarded, or even just marked as ‘like’. These three kinds of feedback actions from friends are collected to calculate the popularity degree of a user. Note that postings, replies, forwards, and mark messages are the basic communication functions supported by most of the popular social networking sites such as Facebook, twitter, LinkedIn, Pinterest, and Google Plus+. We denote $\Phi p o ( u _ { i } )$ as the set of messages posted by user $i ,$ while $\Phi r p ( u _ { i } ) , \Phi f w d ( u _ { i } )$ , and $\Phi m k ( u _ { i } )$ represent the sets of $u _ { i }$ ’s posted messages that are responded to, forwarded, and marked by other users respectively. The formula for the popularity influence of user $u _ { i }$ is represented below:

$$
P I (u _ {i}) = \frac {\left| \Phi r p (u _ {i}) \bigcup \Phi f w d (u _ {i}) \bigcup \Phi m k (u _ {i}) \right|}{\left| \Phi p o (u _ {i}) \right|}.\tag{6}
$$

Note that a message posted by user $u _ { i }$ can be responded to, forwarded, and marked by other users at the same time.

Centrality Computation. After the endorser candidate network is selected, the positions of candidates in the social network will be very important. It is anticipated that information can be received and spread over the network quickly. Therefore, users’ positions in their social network structures will be crucial. The social network analysis provides lots of measures such as centrality degree and betweenness degree to analyse network structure. In this research, the connection structure of users is considered. It is believed that the degree of connection symmetry is a presupposition of smooth information delivery. Highly connected nodes, the hubs, play important roles in information propagation in networks [6,14]. When a person has many neighbours in the network, he or she actually plays the role of a hub and has great importance and controllability in message spreading. The connection degree ratio can be represented by the following formula:

$$
C D R \left(u _ {i}\right) = \frac {\sum_ {u _ {j} \in \Theta_ {E}} U _ {i j}}{\sum_ {u _ {j} \in \Theta_ {E}} D _ {i j} + \sum_ {u _ {j} \in \Theta_ {E}} U _ {i j}},\tag{7}
$$

where $\Theta _ { E }$ denotes the endorsers set, $U _ { i j }$ represents the mutual connections between node $u _ { i }$ and node $u _ { j }$ . If node $u _ { i }$ and node $u _ { j }$ are mutually connected, $U _ { i j } = 1$ , otherwise $U _ { i j } = 0 . \ D _ { i j }$ stands for the one-way connection between node $u _ { i }$ and node $u _ { j }$ . $D _ { i j } = 1$ if a direct connection exists between node $u _ { i }$ and node $u _ { j }$ without a mutual connection. Otherwise, $D _ { i j } = 0$

The influence degree of user i in his or her social network is measured by the summation of the connection degree ratio $C D R ( u _ { i } )$ and popularity Pop $( u _ { i } ) \mathrm { : }$

$$
\operatorname{Inf} \left(u _ {i}\right) = P I \left(u _ {i}\right) + \frac {1}{\left| F \left(u _ {i}\right) \right|} \times \sum_ {u _ {j} \in F \left(u _ {i}\right)} C D R \left(u _ {j}\right),\tag{8}
$$

where $F ( u _ { i } )$ is the set of friends of user $u _ { i }$

## 3.3.2 Diffusing Power Analysis Module

Social Activity. Social activity is important when considering information delivery. This is used to measure the activity strength of a user. It is believed that a good endorser does not only have high social activity himself/herself but also so do his/her friends. Therefore, the goal of this measure is to discover users who not only have a long list of friends but also have a crowd of active friends. An available method is measure a user’s social activity is to count the number of messages he/she has posted. To be recognised as ‘active’ users should frequently post a certain number of messages within a period of time, In other words, a good endorser should post continuously to keep his/her activity on social media sites. The social activity score of user $u _ { i }$ can be measured by the formula below:

$$
S A \left(u _ {i}\right) = \frac {\left| \Phi p o \left(u _ {i}\right) - \Phi p o \varsigma \left(u _ {i}\right) \right|}{t} + \frac {1}{\left| F \left(u _ {i}\right) \right|} \times \sum_ {u _ {j} \in F \left(u _ {i}\right)} \frac {\left| \Phi p o \left(u _ {j}\right) - \Phi p o \varsigma \left(u _ {j}\right) \right|}{t},\tag{9}
$$

where the $\Phi p o \bigl ( u _ { i } \bigr )$ and $\Phi p o \varsigma ( u _ { i } )$ represent the set of messages posted by user $u _ { i }$ and the set of the messages synchronised from other social media accounts owned by user i respectively. Parameter t denotes a period of time. The calculated outcome of equation (9) is affected by t and expresses the idea that social activity decays within a period of time. Note that as social media become more and more popular, a user might use more than one social media site to maintain relationships among friends. Therefore, the synchronised set should be excluded. The social scope of user $u _ { i }$ is measured by summarising $u _ { i }$ ’s personal social activity and the average social activity of $u _ { i }$ ’s friends.

Social Interaction. The strength of user relationships can be measured by their interaction intensity. This research adopts responses and forwarding as interaction activities among users. The ratio that a user responds to (forwards) the messages posted by other users can be used as a proxy for interaction intensity. Thus, interaction intensity between two users $u _ { i }$ and $u _ { j }$ is formulated as

$$
\begin{array}{l} S I (u _ {i}, u _ {j}) = \frac {\left| \Phi r p (u _ {i}) \cap \Phi p o (u _ {j}) \right|}{\left| \Phi r p (u _ {i}) \right|} \times \frac {\left| \Phi p o (u _ {i}) \cap \Phi r p (u _ {j}) \right|}{\left| \Phi r p (u _ {j}) \right|} \\ + \frac {\left| \Phi f w d (u _ {i}) \cap \Phi p o (u _ {j}) \right|}{\left| \Phi f w d (u _ {i}) \right|} \times \frac {\left| \Phi p o (u _ {i}) \cap \Phi f w d (u _ {j}) \right|}{\left| \Phi f w d (u _ {j}) \right|}, \end{array}\tag{10}
$$

where $\Phi p o ( u _ { i } )$ and $\Phi r p ( u _ { i } )$ represents the set of messages posted by user $u _ { i }$ and the set of the messages $u _ { i }$ responded to the messages posted by other users respectively, while $\Phi f w d ( u _ { i } )$ denotes the set of messages $u _ { i }$ forwarded the messages posted by other users. The larger the value of $S I ( u _ { i } , u _ { j } )$ is, the more likely it is that user $u _ { j }$ will be influenced by user $u _ { i }$ . A user’s diffusing power (DP) can be measured by summarising his or her social activity (SA) and social interaction (SI):

$$
D P \left(u _ {i}\right) = S A \left(u _ {i}\right) + \frac {1}{\left| F \left(u _ {i}\right) \right|} \times \sum_ {u _ {j} \in F \left(u _ {i}\right)} S I \left(u _ {i}, u _ {j}\right).\tag{11}
$$

When we select a suitable endorser, both diffusing power and influence degree are important factors to be considered. For this reason, these two scores are multiplied to gain an overall score for the endorser. The endorser score (ES) of a typical user $u _ { i }$ can be defined as below:

$$
E S (u _ {i}) = D P (u _ {i}) \times I n f (u _ {i}).\tag{12}
$$

We use the endorser score ES to rank all users in the endorser candidate network and the top K-ranked users are selected as endorsers to spread advertising information.

## 4. Experiments

To verify its effectiveness and efficiency the proposed social endorsing mechanism for diffusing target advertisement is implemented and experimented on a micro-blogging site (Plurk), which provides features for users to release instant messages and share information in real time. According to Alex’s statistic (http://www.alexa.com/topsites/countries/TW), the Plurk is the most popular micro-blog site in Taiwan (Plurk ranks 68th in the top website in Taiwan, while Twitter is 98rd). Furthermore, according to Google’s traffic trend statistics, the number of daily unique visitors we thus select Plurk as the experimental platform.

In the experiments, an advertising message is briefly described with a hyperlink. When participants click on the hyperlink, they are redirected to the webpage of a product with detailed information. The category tree of the advertisement used in the experiment is built according to the product category of Amazon. The category tree has three general categories and 18 leaf nodes (Table 1).

Table 1 Elements of the category tree

<table><tr><td rowspan="3"></td><td colspan="6">Category</td></tr><tr><td colspan="2">Entertainment &amp; Living</td><td colspan="2">Consumer Products</td><td colspan="2">Computer, Communication, &amp; Consumer Electronics</td></tr><tr><td>Sports &amp; Outdoor</td><td>Movies, Reading, &amp; Music</td><td>Health &amp; Beauty</td><td>Apparel, Shoes, &amp; Accessories</td><td>Electronics</td><td>Computers</td></tr><tr><td rowspan="3">Term</td><td>Extreme Sports</td><td>Books &amp; Magazines</td><td>Cosmetics</td><td>Clothing</td><td>Cameras</td><td>Office Products &amp; Supplies</td></tr><tr><td>Exercise</td><td>Music</td><td>Food</td><td>Shoes</td><td>Cell Phones &amp; Apps</td><td>Software &amp; Support Services</td></tr><tr><td>Travel</td><td>Movies &amp; TV</td><td>Grocery</td><td>Jewellery</td><td>Mobile Electronics</td><td>Computers &amp; Accessories</td></tr></table>

This category tree is used to categorise an advertisement’s type as well as a user’s preferences. The higher level the position, the more general is the category. For instance, when a users’ preference is positioned as the parent root, “Entertainment & Living”, it might indicate that the user is interested in all the products located in the child categories such as “Music”, “Exercise”, or “Travel”. The required product information for the advertisements used in the experiment is collected from or referred to from well-known websites such as Amazon, Best Buy, and IMDB. These provide various kinds of advertisements for the experiment in this research.

## 4.1 Data Description

The profile of participants. Consumers’ lifestyle information is a popular instrument in making advertising management decisions. Kamakura and Wedel [28] indicate that lifestyle characteristics provide practical information for advertisers to use in meeting the demands of the marketplace. The lifestyle segmentation approach classifies consumers into lifestyle clusters with identifiable and specific characteristics. Therefore, in our research, we adopt this technique to categorize the participants into three different groups of social networks (Students, Office Workers, and Other).

Due to the privacy constraint, we can only collect the social information from those users who are willing to authorize us to do that. To resolve this issue, we use a snowball sampling method to recruit the participants and construct the sampled social network. Snowball sampling has been proved to be a feasible method to study the issue of social networks [2]. Hence, it was used to construct the network structure of the experiments. Snowball sampling starts from a random sample of individuals drawn from a given population. Each one in the sample is asked to name N different persons. Those who are named and are not in the random sample form the first-stage network. Each one in the firststage network is then asked to do the same thing for S times of repeating in order to complete the sampling process. Initially, we invited 15 Plurk users, who are willing to authorize us to collect their social information. With their help, we further invited their friends and friends-of-friends. Handcock and Gile [21] indicated that sampled networks are not “biased” but can be representative if analyzed correctly. Exponential random graph model (EGRM) has been demonstrated to be capable of capturing some of the key structural of networks such as the degree of clustering, the degree of distribution, and feature of network connectively [59]. To prevent sample selection bias, we adopt the conditional estimation of EGRM from snowball sampling design approach proposed by Phillippa et al [51] as our sampling approach. We include different users from different background (Student, Office Worker and Others) and control the ration of females to males (6:4) to approaching the Plurk’s gender population distribution at the initially sampling step. From February 15, 2014 to August 15, 2014, total 415 participants were generated through the snowball sampling with 3 (S) stages and 4 (N) name settings. After removing the people who were not interested in our experiment, we left with a total of 337 unique participants (female: 59% men: 41%) who formed the initial experimental social networks.

The characteristics of the extracted networks are shown and summarized in Table 2.The network connection structure is explained as follows.

(1) Clustering coefficient: The clustering coefficient of a vertex indicates how concentrated the neighborhood of that vertex is. The clustering coefficient is defined as the ratio of the number of actual edges between neighbors to the number of potential edges between neighbors.

(2) Average distance: The distance between any two vertices is defined as the least number of edges required to connect the two. It is a measure of the efficiency of information or mass transport on a network.

(3) Average degree centrality: Degree centrality is defined as the number of links incident upon a vertex. It is a measure of network positions of actors in respect of the connections with their immediate neighbors.

Table 2 Characteristics of the experimental network

<table><tr><td colspan="2">Statistics of the experiment network</td></tr><tr><td>Number of participants</td><td>337</td></tr><tr><td>Age</td><td>20–45</td></tr><tr><td>Gender</td><td>Male: 41%Female: 59%</td></tr><tr><td>Clustering coefficient</td><td>0.752</td></tr><tr><td>Average distance</td><td>1.873</td></tr><tr><td>Average degree centrality</td><td>34.925</td></tr></table>

In this research, we traced the posts published in the past three months to analyse users’ profiles and activities. According to the statistics, the average number of daily posts of these users in the past three months is 1.46. Although micro-blogs allow users to communicate instantly, individual profile information is generally unobtainable. In order to keep the advantages of micro-blogs and decrease the limitation of unavailable individual profile information participants are requested to select at most

#

five types of interesting information when they first join the experiment. This information is then taken as the static preferences of users. Dynamic preferences are discovered by CKIP, a system for Chinese word segmenting. The posts shared during the past three months are processed by CKIP to filter frequently appearing words. In the experiments, we establish a product categories database that contains product category terms from Amazon’s existing categories and product term categories database automatically by the system. The matched categories are added as a user’s preferences. Dynamic preferences help capture user preferences in a more comprehensive way.

The profile of advertisements. In this research, information on advertisements is collected from the official websites of electronic retailers such as Amazon, Best Buy, PC Home, books.com, and Lonely Planet. This provides various kinds of advertisements for the experiment. Moreover, in order to examine the effectiveness of the proposed mechanism with respect to different advertising objectives, we distribute advertisements with promotional and branding purposes. The promotional advertisements will provide detailed product-related information both in text and picture (see Figure 4). However, the brand advertisements are more abstractive and provide less textual information in the experiment of this research (see Figure 5). After advertisement receivers visited the web site, they can click the hyperlink under the pictures to provide their feedbacks on the advertisements received.

![](/api/attachments/HJWGCQVE/fulltext/images/4c1c3f3a40c4e8ddb85bc74895f1d4f30a348d147863b2fecf447ed40bf09c25.jpg)  
Figure 4 Example of the promotional advertisement web page

![](/api/attachments/HJWGCQVE/fulltext/images/ab13eb5d77ac8e72897fea9ba483fccb31dfb35c619f03af637e12907e7ab5f6.jpg)  
Figure 5 Example of the brand advertisement web page

Altogether, 450 advertisements are designed based on the information obtained. In the research, a category tree with three general categories, six subcategories, and 18 leaf nodes is built. All advertisements are categorised into the relevant leaf nodes. Advertisements are divided into 90 sets of experiments used for five advertising strategy approaches.

## 4.2 Advertising Strategies

In this research, besides the direct advertising (DA) approach, in which advertisements were sent to the target users directly from the sponsors, four endorser selecting strategies are designed to identify seed endorsers:

(1) Targeted social advertising approach (TSA): This advertising approach is based on the proposed architecture. Targeted users are identified first and then an endorser candidate network is constructed by expanding the friend nodes from targeted users. Final seed endorsers are selected from the endorser candidate network by evaluating their diffusing power and influence strength.

(2) Diffusing power approach strategy (DPA): This approach is a kind of celebrity advertising approach that identifies seed endorsers by directly evaluating the diffusing power of all participating users.

(3) Influence approach (IA): This approach is also a kind of celebrity advertising approach that identifies seed endorsers by directly evaluating the influence strength of all participating users.

(4) Random selection approach: In this approach, seed endorsers are selected at random.

## 4.3 Experiment Procedures

The advertisements would be mainly spread within a specified scope and realize the spirit of “distributing the right advertisement to the right people via the right endorses (friends)”. The advertisement was sent to suitable endorsers from the advertiser, and then the endorsers deliver this message to target users in a private channel spontaneously. The endorsers appointed the message receivers (target users), and only the appointed receivers (target users) can read the message. The advertisement delivered by endorsers in a private can not only control the information resource to alleviate negative impression due to the unfavorable sender, but also understand the diffusing path and whether the target users are touched or not. The experiment is conducted by the following procedures:

(1) The advertisement to be distributed is selected. Targeted audiences are identified according to their preferences about advertisement type.

(2) Selecting endorsers for spreading advertisements via different approaches. The TSA selects endorsers according to targeted users that are expected to receive the advertisement. The other approaches select endorsers according to a user’s propagating power or influence strength, or just randomly.

(3) The advertisement is sent to the selected seed endorsers. It is expressed in a short advertising text with a URL. Endorsers who receive the advertisement can click on the URL and visit the webpage for detailed information.

(4) After receivers visit the webpage of the advertisement, they provide feedback on it via online questionnaires. These questionnaires are designed to evaluate advertising effectiveness such as its relevance.

To evaluate and compare the effectiveness of various advertising approaches the following information and feedbacks of receivers are collected from questionnaires (See Appendix): (1) degree of preference matching, (2) satisfaction about the content of advertisement, (3) appropriateness of the message sender, and (4) purchase willingness inspired by the sender. For each kind of evaluation, a Likert scale is used to rate the levels from 1 to 5 (offensive/very low: 1; irrelevant/ low: 2; moderate: 3; relevant/high: 4; and favourable/very high: 5).

The settings of experiment parameters are summarized in Table 3.

Table 3 Setting of the experiment parameters

<table><tr><td>Participant Segments</td><td>Total ads</td><td>Benchmarks</td><td>Ads&#x27; categories</td><td>Ad&#x27;s group setting</td><td>Ad&#x27;s types for each group</td></tr><tr><td>Students:109Office Workers:115Others:113</td><td>450</td><td>TSA DPA IA Random DA</td><td>18 leaf nodes</td><td>A group with 90 ads</td><td>Promotional ads: 72Brand ads: 18</td></tr></table>

In the experiments, 450 advertisements are designed based on the information obtained. The advertisements are divided into five sets, each of which includes 90 advertisements. The advertisements of each set belong to 18 leaf nodes and each leaf node has five advertisements (one brand type advertisement and four promotional type advertisements). As we will compare five advertising strategies, one set of advertisements, which is randomly selected from these five advertisement sets, are exposed to the experiment of one advertising strategy.

## 5. Results and Evaluation

In this section, we discuss the experimental results and insights discovered. In the experiments, the ad effectiveness level and TDR are measured to compare the performances of various advertising approaches.

## 5.1 Ad Effectiveness

We first examine the feedback ratings collected from users to verify the effectiveness of various advertising approaches. Three indicators, information satisfaction, sender appropriateness, and purchase willingness, are used to measure ad effectiveness. The distributions of these three indicators among the three strategies are depicted in Figure 6.

![](/api/attachments/HJWGCQVE/fulltext/images/52a92689b3455828d9963f0a949b64ff9da6d918e57fbcf3345db12c354fa0ce.jpg)  
Figure 6 Average rating score of different advertising approaches.

We can observe that the proposed TSA has higher average rating scores than the other strategy approaches in all three indicators. This result indicates that TSA can effectively enhance the fit between the preferences of users and advertisements. Further, TSA can effectively identify the suitable message spreaders favoured by receivers, while the purchase intention of ad receivers also rises. Our research problem can make research hypothesis as follows.

H1: The information satisfaction of our proposed target-reaching based social advertising approach (TSA) is better than diffusing power approach (DPA) and influence approach (IA).

H2: The sender appropriateness of our proposed target-reaching based social advertising approach (TSA) is better than diffusing power approach (DPA) and influence approach (IA).

H3: The purchase willingness of our proposed target-reaching based social advertising approach (TSA) is better than diffusing power approach (DPA) and influence approach (IA).

Table 4. Statistical verification results of TSA approach on information satisfaction

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>t</td><td>df</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="2">TSA</td><td>DPA</td><td>.32727</td><td>.90379</td><td>.12187</td><td>2.685</td><td>109</td><td>.010</td></tr><tr><td>IA</td><td>.48889</td><td>.62603</td><td>.09332</td><td>5.239</td><td>109</td><td>.002</td></tr></table>

Table 5. Statistical verification results of TSA approach on sender appropriateness

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>t</td><td>df</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="2">TSA</td><td>DPA</td><td>.18182</td><td>.64092</td><td>.08642</td><td>2.104</td><td>109</td><td>0.40</td></tr><tr><td>IA</td><td>.66667</td><td>.63960</td><td>.09535</td><td>6.992</td><td>109</td><td>.000</td></tr></table>

Table 6. Statistical verification results of TSA approach on purchase willingness

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>t</td><td>df</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="2">TSA</td><td>DPA</td><td>.21818</td><td>.62925</td><td>.08485</td><td>2.571</td><td>109</td><td>.013</td></tr><tr><td>IA</td><td>.57778</td><td>.49949</td><td>.07446</td><td>7.760</td><td>109</td><td>.001</td></tr></table>

Table 4, Table 5 and Table 6 list the results of the paired t-tests between TSA and DPA (IA). According to the tests, all the significances of all pairs are smaller than the p-value of 0.05. This indicates that the performance differences between TSA and DPA (IA) are statistically significant. These results support the Hypothesis H1, H2 and H3.

## 5.2 TDR

Target users are those users whose preferences match the advertisement to be distributed. The TDR is defined as the ratio of target users who actually received the advertisement and it can be calculated as

$$
T D R = \frac {\left| \Theta_ {T} \cap \Theta_ {r} \right|}{\left| \Theta_ {T} \right|},\tag{13}
$$

where $\Theta _ { r }$ is the set of users who received the advertisement. The TDRs of different advertising approaches are shown in Figure 7.

![](/api/attachments/HJWGCQVE/fulltext/images/925938aea47f3559a8a388e8fcf1b99e5453901fa3aed273845b837a5d661253.jpg)  
Figure 7 Average TDRs of advertising strategies

On average, the TDR of TSA is 69.03% and that of DPA is 41.23%. The average TDR of IA is 37.85%. The average TDR of random approach is 12.14%. The DA approach is 8.45%. These results suggest that TSA performs better than the other advertising approaches in diffusing messages to targeted users.

## 5.3 Performance comparisons of various ad types

The advertisements of leaf nodes in the category tree generally provide richer product-related information in advertisements. When the hierarchy level lifts, the product information attached to the advertisements becomes less detailed. We evaluate and compare the effectiveness of distributing advertisements at various levels. In practice, in order to attract customers to purchase product promotion advertisements, which are generally located at a lower category level, include detailed product-related information (such as prices, quality, and so on) and they are presented with text and pictures. By contrast, product brand advertisements, which are generally located at higher category levels, provide less detailed information about product characteristics and they are generally presented with less textual information on the conceptual product brand. In the experiment, “Cameras”, “Cell Accessories” are selected for the categories at the leaf node level. All the advertisements located under these categories have detail product-related information. The parent categories of these advertisements are “Electronics” and “Computers”. The grandparent category of the advertisements is “Computer, Communication & Consumer Electronics (the 3Cs)”.

Figures 8–10 show the average effectiveness rating of advertisements in the leaf, parent, and grandparent categories. From the “Camera” category to the “3Cs” category, the conceptual level becomes higher. In other words, the information that the advertisements provide changes from being product-related to being conceptual. We can observe that the effectiveness rating of TSA deteriorates as the category level moves up. While TSA outperforms other advertising approaches for the advertisements of different levels, it performs better than the DPA and IA approaches, particularly in distributing promotional advertisements at the leaf level.

![](/api/attachments/HJWGCQVE/fulltext/images/9417115bf48cdf25425320b57cbb19898932ac11d04ccff2f2d87d53b729b008.jpg)  
Figure 8 Ad effectiveness of leaf categories

![](/api/attachments/HJWGCQVE/fulltext/images/45b0f0f9520b8acb13b9cd085a35c10fa3bdd6c98f6c948f977e29d5df18d7ba.jpg)

Figure 9 Ad effectiveness of parent categories  
![](/api/attachments/HJWGCQVE/fulltext/images/07442526c0d30ae90017077f9397f013fc0fc93ac0eafcfd676e917de199f956.jpg)  
Figure 10 Ad effectiveness of grandparent category  
Figure 11 shows the TDRs of different category levels. The results also verify that the proposed TSA advertising mechanism has the best performance in delivering promotional ads in leaf categories.

![](/api/attachments/HJWGCQVE/fulltext/images/a18173f08007842ca51e8db7647d72fa01011fd934dda5c0e1dcdb3a2b0f58ce.jpg)  
Figure 11 Average TDRs of different category levels

## 6. Discussion and Conclusion

Nowadays, social media has become a part of human life. Social media empower users to spread and share information instantly and widely. This phenomenon provides great opportunities to implement online advertising on these new communicating platforms. However, how to enhance and balance the efficiency and effectiveness of online advertising over social media is still a significant issue to be calibrated. For example, the traditional target advertising approach can efficiently distribute advertisements to targeted users via advertising agents or sponsors directly. However, it still has the problem of disturbance due to unfavourable senders. By combining the techniques of target and social advertising approaches, this research proposed TSA architecture to diffuse advertising information (e.g. product promotions) via social endorsing to specific target users. The experimental results show that the proposed TSA architecture performs better (TDR and ad effectiveness) than traditional social advertising approaches.

## 6.1 Research Contributions

Firstly, from a methodological perspective, we synthesise the features and target and social advertising approaches, comprehensively considering individual and social factors, to develop a novel

#

mechanism that could significantly enhance advertisement effectiveness. The synthesised preference targeting and friend endorsing features allow us not only to decrease the negative impressions of the advertisement received but also to propagate the advertisement to their friends. Secondly, the proposed targeted social advertising mechanism can diffuse information to targeted users with a higher TDR. This makes the proposed advertising meet the goals of diffusion in a shorter period of advertising disturbance and ensure information is delivered to audiences in a satisfactory manner. Thirdly, from a practical perspective, the proposed mechanism can be implemented to support the promotional and informative function of advertising (product promotions). For example, it can be applied to diffuse sensitive messages, such as time-critical or location-oriented product promotion information, to particular customers. This can enhance the effectiveness of advertising and increase the sales of products. Finally, this research provides a profitable outlook for social advertising. As social media websites rise, marketers are absorbed in discovering the best platform for conducting advertising in the next generation. This research provides several useful empirical experiment results to tell marketers how to implement advertising activities on social media websites. With these experiences, they can develop their social advertising businesses more easily.

## 6.2 Limitations and Future Studies

Several limitations and research issues can be further studied. Firstly, in this research advertisements are distributed by endorsers spontaneously without path selection support. The diffusing path from a user to another user can be tracked to enhance the accuracy of social endorsing. Secondly, the effectiveness of target advertising is significantly affected by the obtainable individual preference information. While we have proposed a feasible approach to collect user preferences, analytical techniques could consider the more comprehensive and dynamic data of personal activities to gain more accurate analysis. Thirdly, the primary design of micro-blogging text might limit the presentation form of advertisements. Pictures and multimedia are generally more attractive to users. It would thus be interesting to analyse the impact of advertisement format and elements on carrying out targeted social advertising. Fourthly, snowball sampling has been proved to be a feasible method to

#

study the issue of social networks. However, the way that the sample is chosen by target people still makes it liable to various forms of bias. How to prevent the selection bias by using survey for evaluation in a large scale social network is a desirable issue for future study. Finally, the trend of using synchronised messages in social media should be further examined. This phenomenon encourages the idea of a joint social sphere. Therefore, it would be a new issue to measure and manage the social activity among different social media sites. This issue also affects the nature o advertising information distribution.

## Acknowledgement

This research was supported by the National Science Council of Taiwan (Republic of China) under the grant NSC 101-2410-H-009-009-MY3.

## References

[1] D.A. Aaker, D.M. Stayman, Measuring audience perceptions of commercials and relating them to ad impact, J. of Advert. Res. 30 (4) (1990) 7–17.

[2] Y.Y. Ahn, S. Han, H. Kwak, S. Moon,H. Jeong, Analysis of topological characteristics of huge online social networking services. In C. Williamson, M.E. Zurko, P. Patel-Schneider, and P. Shenoy (eds.), Proc. of the 16th Int. Con. on World Wide Web. New York: ACM Press, 2007, pp. 835–844.

[3] C. Atkin, M. Block, Effectiveness of Celebrity Endorsers, J. of Advert. Res. 23 (1) (1983) 57–61.

[4] A. Bagherjeiran, R. Parekh, Combining Behavioral and Social Network Data for Online Advertising, In Proc. of the IEEE Int. Conf. on Data Min. Workshops (2008) 837–846.

[5] K. Bagwell, The Economic Analysis of Advertising, Handb. of Ind. Organ. 3 (2007) 1701–1844.

[6] A.L. Barabasi, R. Albet, H. Jeong, Scale-free characteristics of random networks: the topology of the world-wide web, Phys. A 281 (2000) 69–77

[7] N. Beloff, P. Pandya, Advertising models on social networks for SMEs—An advertising methodology. In Y. He (ed.), Proc. of the 2010 Int. Con. on Int. Tech. and Applications. Los Alamitos, CA IEEE Computer Society Press, 2010, pp. 1–6

[8] S.P. Brown, D.M. Stayman, Antecedents and Consequences of Attitude Toward the Ad: A Meta-Analysis, J. of Consum. Res. 19 (1992) 34–51.

[9] M. Cha, H. Haddadi, F. Benevenuto, K.P. Gummadi, Measuring user influence in twitter: the million follower fallacy, Proc. of the 4th Int. Con. on Weblogs and Social Media, Washington, 2010.

[10] T. Dalgic, M Leeuw, Niche Marketing Revisited: Concept, Applications and Some European Cases, Eur. J. of Mark. 28 (4) (1994) 39–55.

[11] C.K.W. De Dreu, B.A. Nijstad, D.V. Knippenberg, Motivated Information Processing in Group

Judgment and Decision Making, Pers. and Soc. Psychol. Rev. 12 (1) (2008) 22–49.

[12] S.A. Delre, W. Jager, T.H.A Bijmolt, M.A Janssen, Will it spread or not? The effects of social influences and network topology on innovation diffusion. J of Prod. Innovation. on Manage. (2010) 267 - 282

[13] D. Easley, J. Kleinberg, Networks, crowds, and markets: Reasoning about a highly connected world, Camb. Univ. Press, Camb., 2010.

[14] H. Ebel, L.I. Mielsch, S. Bornholdt, Scale-free topology of e-mail networks, Phys. Rev. E 66 (2002) 035103(R).

[15] A. Enders, H. Hungenberg, H.P. Denker, S. Mauch, The long tail of social networking. Revenue models of social networking sites, Eur. Manag. J. 26 (2008) 199–211.

[16] Facebook Helps Get One in Five People Worldwide Socializing on Online Networks, Available at:[http://www.emarketer.com/Article.aspx?R=1008903], Accessed in: May 2012.

[17] Federal Trade Commission, Guides Concerning the Use of Endorsements and Testimonials in Advertising, Available at:[http://ftc.gov/os/2009/10/091005revisedendorsementguides.pdf], Accessed in: May 2012.

[18] J. Fiorillo, Twitter Advertising: Pay-Per-Tweet, Available at:[http://www.wikinomics.com/blog/index.php/2009/04/22/twitter-advertising-pay-per-tweet/], Accessed in: May, 2009.

[19] R. Garg, M.D. Smith, R. Telang, Measuring Information Diffusion in an Online Community, J. of Manag. Inf. Syst. 28 (2) (2011) 11–37.

[20] R.E. Goldsmith, B.A. Lafferty, Consumer response to Web sites and their influence on advertising effectiveness, Internet Res. 12 (4) (2002) 318–328.

[21] M.S. Handcock, K.J. Gile, Modelling networks from sampled data, Ann. of Applied Statistic., 4 (2010) 5–25.

[22] K. Heinonen, Consumer activity in social media: Managerial approaches to consumers' social media behavior, J.of Consume. Behave. 10 (6) (2011) 56–64.

[23] O. Hinz, M. Spann, Managing information diffusion in Name-Your-Own-Price auctions, Decis. Support Syst. 49 (4) (2010) 474–485.

[24] O. Hinz, M. Spann, The Impact of Information Diffusion on Bidding Behavior in Secret Reserve Price Auctions, Inf. Syst. Res. 19 (3) (2008) 351–368.

[25] S.C. Hsueh, J.M. Chen, Sharing secure m-coupons for peer-generated targeting via eWOM communications, Electron. Commerce. Res. and Applica. 9 (4) (2010) 283–293.

[26] The Impact of Social Media on Purchasing behaviour, Available at:[http://themarketingguy.wordpress.com/2008/12/30/the impact of social media-on purchasing behavior], Accessed in: May 2012.

[27] J.L. Iribarrena, E. Moro, Affinity Paths and information diffusion in social networks, Soc. Network. 33 (2) (2011) 134–142.

[28] W.A. Kamakura, W. Michel, Life-Style Segmentation with Tailored Interview, J. of Mark. Res., 32(1995) 308-317.

[29] A.M . Kaplan, M. Haenlein, Users of the world, unite! The challenges and opportunities of Social Media. Bus. Horiz. 53 (1) (2010) 59–68.

[30] H. Kwak, C. Lee, H. Park, S. Moon, What is Twitter, a Social Network or a News Media? 2010.

[31] P. Kazienko, M. Adamski, AdROSA-Adaptive personalization of web advertising, Inf. Sci. 177 (11) (2007) 2269–2295.

[32] L. Kelly, G. Kerr, J. Drennan, Avoidance of Advertising in Social Networking Sites: the Teenage Perspective, J. of Interact. Advert. 10 (2) (2010) 16–27.

[33] D . Kempe, J. Kleinberg, E. Tardos, Maximizing the spread of influence through a social network, In Proc. of the ninth ACM SIGKDD Int. Conf. on Knowl. Discov. and Data Min., New York, NY, USA, (2003) 137–146.

[34] D. Kempe, J. Kleinberg, E. Tardos, Influential nodes in a diffusion model for social networks, In Proc. of Int. Colloq. on Autom., Lang. and Program., Verlag Berlin, Heidelberg, (2005) 1127– 1138.

[35] Y. Kim, M. Kim, K. Kim, Factors Influencing the Adoption of Social Media in the Perspective of Information Needs, In Proc. of the iConference(2010).

[36] Y.A. Kim, J. Srivastava, Impact of social influence in e-commerce decision making. In M. Gini and R.J. Kauffman (eds.), In Proc. of the Ninth Int. Conf. Electronic Commerce. New York: ACM Press, 2007, pp. 293–302.

[37] C. Kiss, M. Bichler, Identification of influencers - Measuring influence in customer networks, Deci. Support Syst. (46) (1) (2008) 233–253.

[38] L. Kuandykov , M. Sokolov, Impact of social neighborhood on diffusion of innovation S-curve, Decis. Support Syst. 48 (4) (2010) 531–535.

[39] K.C. Laudon, C.G. Traver, E-Commerce: Business, Technology, Society, Pearson Prentice Hall, New Jersey, 2007.

[40] M.B. Lee, K.S. Suh, J.H. Whang, The impact of situation awareness information on consumer attitudes in the Internet shopping mall, Electron. Commer. Res. and Applica. 2 (3) (2003) 254– 265.

[41] K.H. Lim, C.L. Sia, M.K.O., I. Benbasat, Do I trust you online, and if so, will I buy? An empirical study of two trust-building strategies. J. of Manage. Inf. Sys., 23, 2 (2006), 233–266.

[42] W.H. Luo, D. Cook, E.J. Karson, Search advertising placement strategy: Exploring the efficacy of the conventional wisdom, Inf. & Manag. 48 (8) (2011) 404–411.

[43] V. Mahajan, E. Muller, F.M. Bass, New product diffusion models in marketing: a review and directions for research, J. of Mark. 54 (1) (1990) 1–26.

[44] G. McCracken, Who is the Celebrity Endorser? Cultural Foundation of the Endorsement Process, J. of Consum. Res. 16 (3) (1989) 310–321.

[45] P. Mitra, K. Baid, Targeted advertising for online social networks. In V. Snasel and J. Pokorny (eds.), Proc. of the First Int. Con. on Networked Digital Technologies. Los Alamitos, CA: IEEE Computer Society, 2009, pp. 366–372.

[46] D.C. Muelle, T. Stratmann, Informative and persuasive campaigning, Public Choice 81 (1,2) (1994) 55–77.

[47] J. Muller, F. Alt, D. Michelis, Pervasive Advertising, Human–Computer Interaction Series, Springer Publishing Company, 2011.

[48] J. Murphy, Branding, Mark. Intell. & Plan. 6 (4) (1988) 4–8.

[49] E.W.T. Ngai, Selection of web sites for online advertising using the AHP, Inf. & Manag. 40 (4) (2003) 233–242.

[50] Y. Ni, L. Xie, Z.Q. Liu, Minimizing the expected complete influence time of a social network, Inf. Sci. 180 (13) (2010) 2514–2527.

[51] E.P. Phillippa, L.R. Garry, T.A.B. Snijders, W. Peng, Conditional estimation of exponential random graph models from snowball sampling design, J. of Math. Psych., 57 (2013) 284-296.

[52] N. Rao, M. Mobius, T. Rosenblat, Social networks and vaccination decisions, Federal Reserve Bank of Boston Working Paper No. 07–12. 2007. Nov 6, Available at:[http://ssrn.com/abstract=1073143], Access in: May, 2012.

[53] M. Richardson, P. Domingos, Mining knowledge-sharing sites for viral marketing, In Proc. of Int. Conf. on Knowl. Discov. and Data Min., New York, NY, USA, (2002) 61–70.

[54] J.H. Roberts, G.L. Urban, Modeling multiattribute utility, risk, and belief dynamics for new consumer durable brand choice, Manag. Sci. 34 (2) (1988) 167–185.

[55] G. Robins, P. Pattison, P. Elliott, Network models for social influence processes. Psychometrika, 66, 2 (2001), 161–189.

[56] Sensis, Social Media Report: What Australian people and businesses are doing with social media, Available at:[http://about.sensis.com.au/ignitionsuite/uploads/docs/sensis%20social%20media%20report.p df], Accessed in: May 2012.

[57] M.E. Schramm, K.J. Trainor, M. Shanker, M.Y. Hu, An agent-based diffusion model with consumer and brand agents, Decis. Support Syst. 50 (2010) 234–242.

[58] H.S. Shin, J.H. Lee, Impact and degree of user sociability in social media, Inf. Sci. 196 (2012) 28–46.

[59] T.A.B. Snijders, P. Pattison, G.L. Robins, M. Handcock, New specifications for exponential random graph models, Soc. Methodology., 36 (2006) 99–153.

[60] P.S. Speck, M.T. Elliot, Predictors of Advertising Avoidance in Print and Broadcast Media, J. of Advert. 26 (3) (1997), 61–76.

[61] M. Stelzner, Social Media Marketing Industry Report, Available at:[http://www.socialmediaexaminer.com/social-media-marketing-industry-report-2012/], Accessed in: May, 2012.

[62] S. Stockman, Advertising in Online Social Networks: A Comprehensive Overview, Honors Scholar Theses, 2010.

[63] S. Sundar, J. Kim, Interactivity and persuasion: influencing attitudes with information and involvement, J. of Interact. Advert. 5 (2) (2005) 5–18.

[64] S. Toivonen, Web on the Move. Landscapes of Mobile Social Media. Espoo:VTT Tiedotteita . Research Notes 2403. 56 p. + app. 3 p.http://www.vtt.fi/inf/pdf/tiedotteet/2007/T2403.pd

[65] A. Wang, The effects of expert and consumer endorsements on audience response. J. of Advert Research, 45, 4 (2005), 402–412.

[66] D.J. Watts, A simple model of global cascades on random networks, In Proc. of the Natl. Acad. of Sci. 99 (9) (2002) 5766–5771.

[67] C. Wen, B.C.Y. Tan, K.T.T. Chang, Advertising effectiveness on social network sites: an investigation of tie strength, endorser expertise and product type on consumer purchase intention, Proc. of the Int. Con. on Inf. Sys. (ICIS), Phoenix, Arizona, United States, 2009, pp. 15–18.

[68] A. Winterbottoma, H.L. Bekkerb, M. Connera, A. Mooney, Does narrative information bias individual's decisionmaking? A systematic review, Soc. Sci. & Med. 67 (12) (2008) 2079–2088.

[69] Z. Wu, M. Palmer, Verbs semantics and lexical selection, In Proc. of the Annu. Meet. on Assoc. for Comput. Linguist. (1994) 133–138.

[70] S.A. Yoon, Using Social Network Graphs as Visualization Tools to Influence Peer Selection Decision-Making Strategies to Access Information About Complex Socioscientific Issues, J. of the Learn. Sci. 20 (4) (2011) 549–588.

[71] B. Zafer Erdogan, Celebrity Endorsement: A Literature Review, J. of Mark. Manage. 15 (4) (1999) 291–314.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Very Low</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○ Very High</td></tr></table>

## Appendix

## User rating Questionnaire

What’s your thinking about the matching degree between your preference and the advertisement information? 1 2 3 4 5 Very Low ○ ○ ○ ○ ○ Very High

What’s your thinking about acceptance level of the advertisement information delivery method?

What’s your thinking about satisfaction level of the content that advertisement presents? 1 2 3 4 5 Very Low ○ ○ ○ ○ ○ Very High

What’s your thinking about appropriateness level of the advertisement’s sender? 1 2 3 4 5 Very Low ○ ○ ○ ○ ○ Very High

What’s your thinking about purchase willingness level inspired by the advertisement sender? 1 2 3 4 5 Very Low ○ ○ ○ ○ ○ Very High
