---
otero_id: 14346
otero_key: "Z7FT5HDV"
title: "Finding a Needle in the Haystack: \nRecommending Online Communities on Social Media Platforms Using Network and Design Science"
authors: "Srikar Velichety; Sudha Ram"
year: "2021"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00694"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 22 Issue 5

Article 7

2021

# Finding a Needle in the Haystack: Recommending Online Communities on Social Media Platforms Using Network and Design Science

Srikar Velichety , svlchety@memphis.edu

Sudha Ram , sram@arizona.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Finding a Needle in the Haystack: Recommending Online Communities on Social Media Platforms Using Network and Design Science

Srikar Velichety<sup>1</sup>, Sudha Ram<sup>2</sup>

<sup>1</sup>Fogelman College of Business and Economics, University of Memphis, USA, svlchety@memphis.edu <sup>2</sup>Eller College of Management, University of Arizona, USA, sram@arizona.edu

## Abstract

We address the problem of recommending online communities on social media platforms using design science. Our method is grounded in network science and leverages the random surfer model of the web, small-world networks, strength of weak connections, and connectivity to analyze three types of large-scale networks. In doing so, we design features for structural hole assortativity and local clustering coefficient rank to capture both the diversity and evolution of user interests. We also extract general online community features such as size and overlap. Experiments conducted on a large dataset of 34,000 lists created and subscribed to by 1,600 active Twitter users over a six-month period showed that our network features outperform the general and content features in terms of recommending communities at the top position. In addition, a combination of general and network features generated the best results in the top position with a significant performance improvement over using only the content features. A combination of all three types of features gave the best results in the top-5 and top-10 positions while improving the quality of recommendations at every other position. Our work outperforms the latest work on community recommendations on social media platforms and has major implications for the design of online community recommenders.

Keywords: Social Media Platforms, Online Communities, Recommender Systems, Explainable AI, Network Science and Design Science

Giri Kumar Tayi was the accepting senior editor. This research article was submitted on October 7, 2019 and underwent three revisions.

## 1 Introduction

Online communities are defined as groups of individuals who come together around a shared purpose, interest, or goal (Koh et al., 2007; Preece & Maloney-Krichmar, 2005) where the interaction and information sharing among and between the community members is facilitated by technology (Rothaermel & Sugiyama, 2001). Today, millions of users regularly post content to these communities on wide-ranging topics related to their interests (Butler, 2001; Faraj et al., 2011; Ray et al., 2014). Social media platforms have provided the digital tracks for popularizing these communities by letting users create their own communities of interest or subscribe to them (Rakesh et al., 2014; Ray et al., 2014; Sundararajan, 2016). They are called by different names on each platform—e.g., “lists” on Twitter, “groups” on Flickr and Facebook, and “boards” on Pinterest. Using these communities, social media platform users can consume the latest content related to their interests, thus helping them narrow the scope of their attention (Abiragi, 2019).

Previous research (Yamaguchi et al., 2011) has found that on Twitter, lists are much more representative of user interests than tweet content. Another survey of social media users (de la Rouviere & Ehlers, 2013) confirms that lists enable users to keep track of the activities of more users than following them directly. On Pinterest, the introduction of boards has helped the platform deliver much better search results than Google in terms of high-quality relevant content across different segments, including fashion, lifestyle, health, and recipes (McCollum, 2013).

Figure 1 shows an example of a Twitter list titled “Security.” Note that this is a public list, is curated by the user “Robert Scoble” and includes the description: “Chief Security Officers and others who are keeping our technology lives safe.” The list has 48 members and 81 subscribers. Members of a list are users that the curator has added whose tweets are visible on the list’s home page. The curator typically creates the list and adds users to keep track of their tweets, i.e., content. A public list may have one or more subscribers, i.e., users, who voluntarily subscribe to a list to follow the tweets of its members. In other words, curators, members, and subscribers are different types of platform users associated with the community (a list in this case). This list can provide a set of advertising leads to firms like Norton, McAfee, and Kaspersky who can target ads related to their security products to the members and subscribers of this list (Goldman, 2015; Dopson, 2018; DePhillips, 2019). Similarly, on Pinterest, content boards help users find relevant pins while on Facebook and Flickr groups help them find relevant content and photographs, respectively. In summary, these communities have helped social media platforms curate millions of pieces of content and present them at the right time to the appropriate users. For marketers and advertisers, they help avoid huge time and cost inefficiencies, which often result in several years of wasted advertising efforts and millions of dollars spent on targeting the wrong audience.

While previous research has investigated the use of content and interactions among social media platform users to recommend relevant online communities (Kamath et al., 2013; Yang et al., 2015), there has been very little attention paid to the structure of relationships between and among these users and communities (Rakesh et al., 2014). Ray et al. (2014) argue that online communities are social structures built on modern-day information technology infrastructures such as social media platforms (Sundararajan, 2016). Users belong and subscribe to these communities. Therefore, all social media platform users are embedded in a network of relationships between and among communities and their users. We evaluate how examining the different kinds of relationships among and between communities, their subscribers, and members to derive structural features could be used to build a communitysubscription recommender. Moreover, considering the deficit of user attention on social media platforms because of the large volumes of continually updated content (Bessi et al., 2014; Davenport & Beck, 2001; Rui & Whinston, 2012), we argue that features such as community size and overlap can help suggest user subscriptions to online communities. In summary, there is a need to derive features related to subscription and membership (both network and nonnetwork) for the purpose of building a community-subscription recommender. A combination of these network, general, and content-related features could comprehensively quantify user preferences for communities, which could lead to more accurate and higher quality recommendations. In view of this, we pose the following research questions

(1) What types of relationships exist between and among online communities and different types of social media platform users and what features of these relationships can help recommend these communities for subscription?

(2) What general features of communities, such as their size and overlap, may help recommend them for subscription?

(3) How do features from (1) and (2) compare with the content features from the communities? How do they supplement them?

In this paper, we answer these questions by designing a method that identifies and leverages three types of networks (between and among various users and communities). We used various aspects of network science such as small-world networks (Watts & Strogatz, 1998a; Watts & Strogatz, 1998b), strength of weak connections (Burt, 2004), random surfer model of the web (Page et al., 1999), and connectivity (Borgatti, 2005; Freeman, 1977) to design and extract relevant features. We built a model using these features and show that it outperforms content features in terms of generating recommendations at the top position. We also extracted general community features such as size and community overlap and show that they provide the best results in the top position when combined with network features. In addition, we also provide evidence showing that a combination of all three types of features gives overall best results in the top-5 and top-10 positions. Finally, we compare our approach with the five common state-of-the-art techniques used in recommender systems (Huang & Zeng, 2011) and the latest work on recommending Twitter lists using network and deep learning approaches (Han et al., 2016; Rakesh et al., 2014; Yin et al., 2019). Using text features as another baseline (Yang et al., 2015), we demonstrate that our method substantially outperforms all these approaches across most of the evaluation metrics. Our feature-building process and models comprehensively account for and correct possible data leakage issues, and we demonstrate that our results are stable and significant.

![](/api/attachments/Z7FT5HDV/fulltext/images/ecb3f38737ffc391baeef437cf46c4f333f24e2a4716b84051519e3c8c11c0a6.jpg)  
Figure 1. Sample List

To conduct this research, we used the nominal process model for design science research proposed by Peffers et al. (2007) with Twitter as the context and mapped the steps in our design to the stages in this framework. In doing so, we propose a new design science framework to leverage large-scale network, text, and general community data to build robust recommender systems for online communities. Given that Twitter is one of the most used social media platforms (Moreau, 2017) and that most other platforms have communities like Twitter lists and allow their users to publicly share content, we believe that our proposed design, features, and models could be customized and reused for generating online community recommendations on different platforms. Thus, we not only demonstrate the power of networkrelated features in suggesting useful online communities but also propose features that can be used and reused to not only analyze preferential attachment but also to assign importance to a node using the ego network structure in social networks. We also provide efficient algorithms for calculating these metrics.

## 2 Literature Review

Online communities allow social media platform users to create distinct categories of information sources and consume the content posted. While there has been research on the usage of these communities as a means of inferring latent user characteristics and interests (Ghosh et al., 2012; Kamath et al., 2013; Pochampally & Varma, 2011; Sharma et al., 2012) and on the evolution of closures among these communities on Twitter (Zhao & Ram, 2011), little research has been conducted that evaluates how to recommend these communities to users (Kamath et al., 2013; Rakesh et al., 2014; Yang et al., 2015).

The earliest work in this area employed the content posted to these communities to build recommenders.

Ronen et al. (2014) built a system to recommend outside content to community owners on enterprise social media platforms. They found that their system outperformed content-based, item-based, and hybrid recommenders in terms of generating useful recommendations to community owners. Using a similar approach, Kamath et al. (2013) proposed a board recommender system for Pinterest using the content posted. They found that content posted to boards is a better representative of user interests than the user-assigned Pinterest categories. Based on this research, Yang et al. (2015) proposed a cross-platform approach where they built a Pinterest board recommendation system for Twitter users. However, all these studies are based on the content of communities only rather than the relevant social network features. Rakesh et al. (2014) proposed an approach for recommending Twitter lists based on lists to which the followers of a user subscribe. Along similar lines, Han et al. (2016) proposed a community similarity degree (CSD) metric to estimate the degree of interest similarity among multiple users in a community and found that selecting communities using this metric achieved higher recommendation precision for Facebook communities. Recently, Xiao et al. (2017) proposed a fairness-aware group recommender that maximizes the utility of each community member and thus achieves superior accuracy. More recently, Yin et al. (2019) proposed a deep learning-based bipartite graph embedding model to build a social influence- based community recommender and found that this system outperformed all the existing state-of-the-art recommenders. However, these approaches do not consider the structural and positional characteristics of the network (Borgatti, 2005) in which a community and different types of social media platform users are embedded.

Because users consume content from multiple communities and because each community has multiple users interested in consuming its content (Rakesh et al., 2014; Yamaguchi et al., 2011), we believe that a network of users and communities can be used to quantify user preferences for subscription and recommend appropriate additional communities for content consumption. We combined the existing literature on preferential attachment in networks (Capocci et al., 2006; Newman, 2002) with work on the strength of weak connections (Burt, 2002; Burt, 2004) to design additional assortativity features of user preference and found that they are useful for recommending communities. Also, multiple users might have an interest in consuming content from the same set of communities (Bhattacharya & Ram, 2012; Wang et al., 2012; Zeng & Wei, 2013), in which case the properties of a network of common subscriptions among users can be used to suggest additional communities. In this regard, we combined the existing literature on random-surfer model of the web (Page et al., 1999) with properties of small-world networks (Watts & Strogatz, 1998a; Watts & Strogatz, 1998b) to design a feature called the local clustering coefficient rank (LCCR).

Since two communities with the same name and description might have different network characteristics, we also argue that positional network characteristics can be used to overcome operational issues associated with collaborative filtering in community recommendations (Huang & Zeng, 2005; Rakesh et al., 2014). We therefore also refer to the literature on centrality and connectivity (Borgatti, 2005; Freeman, 1977). Finally, we also argue that general community features such as size and overlap provide significant value in recommending appropriate communities of interest in social media environments (Rakesh et al., 2014; Rui & Whinston, 2012). Using lists on Twitter as a context, we evaluate the power of these network and general features both in terms of generating high-quality recommendations and complementing the existing baseline features to generate better recommendations.

## 3 Research Design and Process: Framework

Peffers et al. (2007) proposed a nominal process model for design science research that has seven stages: identifying the problem and motivation, defining the objectives of the solution, design and development, demonstration, evaluation, and communication. Figure 2 maps the steps in our research to the stages in this process. We address the problem of suggesting a high-quality user community of interest (Twitter list in this case) that a social media platform user/marketer could subscribe to. The objectives are to leverage (1) the relationships among and between communities and different types of social media platform users, and (2) general community characteristics such as size and overlap to identify relevant features for the subscription recommender (using network science and data-driven exploration).

The design phase identified the three types of networks that can be used to answer the research questions. We used different aspects of network science such as preferential attachment (Capocci et al., 2006; Newman, 2002), strength of weak connections (Burt, 2004), connectivity (Freeman, 1977), small-world networks (Watts & Strogatz, 1998a), and the random surfer model of the web (Page et al., 1999), along with temporal variation of user interests on social media platforms (Hong & Davison, 2010; Rakesh et al., 2014) to identify features that could be used as inputs to the recommender. In doing so, we also built algorithms that are capable of efficiently extracting these features from large-scale networks. We also explored the general properties of communities (lists in this case) to extract features useful for building a subscription recommender and used the features from content (tweets) posted to these communities as a baseline to compare the recommender performance with the identified two sets of features. Finally, we corrected for possible train-test data leakage in designing these features.

The artifact we created is a combination of a method, based on network and general community analysis used to identify the appropriate features for recommendation, and the process used to efficiently extract these features from large-scale datasets and evaluate the recommenders and the importance of these features. Hevner et al. (2004) define artifacts as “constructs, models, methods, instantiations or new properties of technical, social and or informational sources.” This research began by employing the existing work in network science (Borgatti, 2005; Burt, 2004; Freeman, 1977; Page et al., 1999; Watts & Strogatz, 1998a) and the temporal variation of user interests on social media platforms (Hong & Davison, 2010; Rakesh et al., 2014) to propose new features in network analysis that quantify user preferences to consume content posted to online communities on social media platforms. We also provide the relevant algorithms to efficiently extract these preferences.

The demonstration phase built models that used the features identified in the design phase. During this phase, we articulated the choice of the technique used for generating the recommendations and corrected for possible target data leakage. The evaluation phase compared the performance of these models with that of the baseline recommender system that uses only the content features. We compared how well our network and general community features complement content features to provide good quality recommendations at various positions. We also quantified the value that each of the identified features add to improving the performance of the recommenders.

![](/api/attachments/Z7FT5HDV/fulltext/images/7858146947d37585e284eb6373e3ad605be8d3e28919a94f5301295776f15155.jpg)  
Figure 2. Design Science Framework

Finally, we compared the performance of our approach with five existing state-of-the-art recommender algorithms (Huang & Zeng, 2011) and the latest work on recommending online communities on social media platforms using network science and deep learning approaches (Han et al., 2016; Rakesh et al., 2014; Yang et al., 2015; Yin et al., 2019). In the communication phase, we identified how results from this research could be used by practitioners to build recommender systems on other social media platforms, and how the networks constructed and metrics formulated in this research could be used to derive insights on other social media platforms. Finally, we also demonstrate how network science can be leveraged to analyze large online networks.

## 4 Data Description

To conduct this study, we collected an initial dataset of Twitter lists and their members from listorious.com. Twitter is one of the top social media platforms in existence and has more than 330 million monthly active users (Omnicore, 2020). First, we generated a random sample of lists using keywords derived from the categorization of news articles in the New York Times. Based on the search keywords we chose, Listorious suggested additional relevant keywords. The description of keywords used to search for lists in each category is shown in Table 1.

We initially collected 200 lists from each of the categories. We collected the curators for each of these lists resulting in 1600 users (some of the lists showed up in the search results of multiple categories. For example, a list on “digital health” showed up in both the “technology” and “health” categories). Using the Tweepy module<sup>1</sup> in Python, we collected the set of all the lists that these users have created, as well as the members and the subscribers to those lists, and the set of all the people these users were following. We also collected the curator’s tweets and those of the lists they created or subscribed to using the Twitter REST API. We collected these details continuously every month for a period of six months between September 2014 and February 2015. We removed suspended users from our dataset and those users whose Tweets were not in English. Table 2 provides a summary of our dataset.

Table 1. Keywords Used for Searching on Listorious

<table><tr><td>Category</td><td>Keywords</td></tr><tr><td>World</td><td>Worldwide, China, India, Europe, Asia, Australia</td></tr><tr><td>US</td><td>America, New York, United States, Boston, Chicago</td></tr><tr><td>Politics</td><td>Politician, government, liberal, progressive, veteran</td></tr><tr><td>Business</td><td>Organization, management, marketing, advertising</td></tr><tr><td>Dealbook</td><td>Mergers, private equity, banking, investment, venture capital, finance</td></tr><tr><td>Technology</td><td>Tech, technology, techie</td></tr><tr><td>Sports</td><td>Sports, basketball, football, athletes, golf, Olympics, rugby</td></tr><tr><td>Science</td><td>Science, scientists, museums, animals, plants, birds, ecology, climate</td></tr><tr><td>Health</td><td>Healthcare, fitness, diet, health, medicine</td></tr><tr><td>Arts</td><td>Art, music, singing, dancing</td></tr><tr><td>Style</td><td>Style, fashion, beauty</td></tr><tr><td>Opinion</td><td>Opinion, sentiment, critics</td></tr></table>

Table 2. Descriptive Statistics

<table><tr><td></td><td>Count</td><td>Average (per curator)</td><td>Median</td><td>Standard deviation</td></tr><tr><td>Lists curated</td><td>34812</td><td>17.4</td><td>11</td><td>20.5</td></tr><tr><td>Members*</td><td>1656991</td><td>828.49</td><td>790</td><td>3210</td></tr><tr><td>Curator friends** (following)</td><td>5949336</td><td>2974.66</td><td>1660</td><td>13600</td></tr><tr><td>Curator subscriptions***</td><td>19115</td><td>11.08</td><td>5</td><td>24.5</td></tr><tr><td>Subscribed members****</td><td>1305112</td><td>806.12</td><td>780</td><td>3770</td></tr><tr><td>Tweets</td><td>506700</td><td>335.72</td><td>215</td><td>356.59</td></tr><tr><td colspan="5">* indicates the number of unique members in all the lists of all the curators. ** indicates cumulative number of users followed by all curators. *** indicates cumulative number of lists to which all the curators have subscribed. **** indicates the cumulative number of people in all the lists to which curators have subscribed.</td></tr></table>

## Design: Network, General Interest Group, and Baseline Feature Identification

We used Twitter lists as a context to identify network, general, and content-related features. Our design involves determining the appropriate networks and feature engineering to extract the relevant features. We also identified general features of the lists such as membership and subscription size and overlap using this approach. Finally, we determined the properties of content that are used as a baseline for comparison of recommender performance with the identified sets of features. We used a discovery-driven approach grounded in various aspects of network science and large-scale data analysis to determine all these features. Figure 3 shows the details of the three comprehensive sets of features identified in the design phase.

## 5.1 Identification of Relevant Networks for Analysis

To identify the possible networks from which to extract features, we needed to answer the question: “What types of relationships exist between and among online communities and different types of social media platform users and what features of these relationships are helpful for recommending these communities for subscription?”

We used two types of entities for our analyses: users (includes the list curators) and lists (both subscription and membership lists). For Twitter, we employed three types of users: curators, members, and subscribers. Two-mode networks were used to analyze the relationships between different types of entities (Borgatti & Halgin, 2011) while single-mode networks were used to analyze relationships among the same types of entities.

The curator of one list can subscribe to or become a member of another, so there is a possible “subscribed to” or “member of” relationship between entities of the same type (if a user is a subscriber to a list, then that user is not a member and vice versa). In addition, two users can subscribe to multiple common lists, meaning that there is a network that represents common subscriptions/memberships among curators (again between entities of the same type). Finally, users can subscribe to multiple lists and each list can have multiple subscribers/members, i.e., relationships between entities of different types. Thus, there are three possible types of networks in total. Table 3 shows the types of networks used for our analyses (in the context of Twitter). The next few paragraphs discuss these networks in detail.

![](/api/attachments/Z7FT5HDV/fulltext/images/cd05937489ed27eb52f3f9014212d42e9dcb95c054ded3a22271257da881e40b.jpg)  
Figure 3. List of All Identified Features

Table 3. Types of Networks

<table><tr><td></td><td>Membership</td><td>Subscription</td></tr><tr><td>List-list</td><td>List-list network for membership</td><td>List-list network for subscription</td></tr><tr><td>User-user</td><td>User-user network for membership</td><td>User-user network for subscription</td></tr><tr><td>List-user</td><td>List-user network for membership</td><td>List-user network for subscription</td></tr></table>

List-list network: In this network, a node jointly represents a list and its curator. In a membership network, there is a directed link from node i to node j if the curator of list i is a member of list j. Thus, a link represents the “member of” relationship. In a subscription network, there is a directed link from node i to node j if the curator of list i subscribes to list j. In short, the link represents a “subscribed to” relationship. Since each user can create multiple lists, to construct this network, we used the largest list of each curator, which we assumed to be representative of that curator’s interests (Zhao & Ram, 2011). Multiple memberships and subscriptions were examined using a two-mode network. Figure 4 shows a sample of this type of network.

User-user network: Nodes in this network are curators and the link between them indicates that they have subscribed to a common list with the edge weight representing the number of common lists. In the membership network, the edge weight represents the number of common lists of which they are members. Figure 5 shows a sample of this type of network.

Subscribed to / member of list network: There are two types of nodes here: the user (i.e., member/subscriber) and the list. There is an undirected edge between the user and a list if the user subscribes to a list. Here we consider only subscribers of the list, not the members. The users are represented as ovals while the Lists are represented as squares as shown in Figure 6. In the case of a member-list network, users represent members instead of subscribers.

Subscribing to a list or adding a member to a list is a preference determined by the user (Zhao & Ram, 2011).

In addition, groups of users who have common interests subscribe to similar lists and their patterns can be analyzed to extract relevant features for the recommender. Finally, the positions within a list, its members, and its subscribers impact list subscription (Rakesh et al., 2014) (for example, if a User A has subscribed to List B, User A observes the members of the list and the other lists that they have subscribed to and can in turn end up subscribing to those lists); therefore, it is useful to extract the positional characteristics and use them for recommendation. We answer the following three research questions to extract network- related features:

1. What preferences do users have for community subscriptions?

2. What patterns of co-subscription to communities exist among social media platform users?

3. How do the positional characteristics of communities and social media platform users in a network determine subscription?

The final purpose of answering these questions is to identify features that can be leveraged to build a recommender for online communities. However, performing these analyses on the complete dataset could result in data leakage. Therefore, we identified all the features on the training dataset, generated using 90% of the data in every period. These features were subsequently used to train prediction algorithms, thus preventing any train-test leakage. Moreover, the algorithms were trained separately for each of the periods to avoid target data leakage.

![](/api/attachments/Z7FT5HDV/fulltext/images/c7911ffbf50b63b91b928e8921183e2bf2daa6f543926925529e09c65f649c06.jpg)  
Figure 4. List-List Link

![](/api/attachments/Z7FT5HDV/fulltext/images/e54bb6268d36c1feb90a99148f2a4ea08966c8b417c7b76997dde8927682a75d.jpg)  
Figure 5. User-User Link

![](/api/attachments/Z7FT5HDV/fulltext/images/8c7cd8192cfe57b4928747a88b9a47902365b74692c8c1ebc3b86f37f3b35ea0.jpg)  
Figure 6. List-User Link

## 5.1.1 Quantifying User Preferences for Subscription

In this section, we answer the question: “What preferences do users have for community subscriptions?” Adding a user as a member to a list or subscribing to a list, i.e., consuming content from the community, is a choice made by the curator. To understand user preferences for subscription, the largest subscribed list can be assumed to be representative of user interests (Zhao & Ram, 2011). Therefore, we used the list-list networks to explore how membership and subscription links form. To understand the social graph in which a list and its curator are embedded, we used the concept of assortativity.

Assortativity is a feature of social networks that refers to the tendency of nodes with a certain property (like degree, in or out degree, etc.) to connect to other nodes with a similar property (Newman, 2002). Since listmembership and subscription are representative of a user’s intention to keep track of the activities of other users (Kim et al., 2010; Myers et al., 2014; Velichety & Ram, 2013), we extend this concept to lists and their curators. We calculated the four measures of directed assortativity proposed in Foster et al. (2010), for the membership and subscription networks. To calculate the statistical significance of each of these measures, we used the z-score which compares the assortativity of our network with that of a set of 100 randomly generated networks with the same degree distribution. To compare networks of different sizes, z-scores are normalized using the assortativity significance profile (ASP) defined as:

$$
\begin{array}{c} A S P (\alpha , \beta) = \frac {Z (\alpha , \beta)}{[ \sum_ {\alpha , \beta} Z (\alpha , \beta) ^ {2} ] ^ {1 / 2}} \\ \text { where } (\alpha , \beta) \in \{\text { in, out } \}. \end{array}\tag{1}
$$

While the directed assortativity metrics give us an idea about the implicit preferences in the subscription and membership of curators (egos), they do not tell us anything about how the contacts between their alters (nodes to which they are connected) impact their behavior. The structure of the community in which the ego is embedded spans far beyond the edges involving only the ego. If the alters are connected to each other, it means that the ego is embedded in a closely-knit community. In such a case, the behavior of the curator can be expected to be different from a case in which the curator is embedded in a loosely connected community (Coleman, 1988; Coleman & Coleman, 1994). Moreover, prior studies have shown that ignoring the edge direction misses some key features of community structure (Kim et al., 2010).

Structural holes measure the redundancy among alters of an ego (Burt, 2002). If the alters are well connected to each other, then the ego is embedded in a dense community of relationships, which in turn means that the ego’s view of the outside network is constrained. Similarly, betweenness centrality and closeness centrality measure the importance of a node in connecting every other node in the network (Freeman, 1977). Therefore, to accommodate these measures, we proposed and used additional measures based on structural holes, betweenness centrality, and closeness centrality. Tables 4 and 5 presents the values of assortativity profiles for subscription and membership networks based on these measures.

We found that all four components of structural holes are significant in determining subscription. Since structural holes measure sparsity in the ego network, they tell us that preference for subscription is strongly influenced by the sparsity in both in- and out-degree components—i.e., the lists of curators who subscribe to lists that are not connected to each other tend to be subscribed to by both similar and dissimilar curators. However, the z-score for the in-in component is negative, indicating that curators whose lists have been subscribed to by people who subscribe to each other’s lists, tend to subscribe to lists whose curators do not subscribe to each other’s lists. For betweenness centrality, we found no statistically significant relationship on any of the four measures indicating that this metric does not affect the preference for subscription. Finally, only the in-in and out-in components of closeness centrality were found to be significant, suggesting that curators who subscribe to a variety of lists prefer to subscribe to more common lists.

To conclude, we found that the structure of the network around a list, using the largest list as representative of user interests, can determine subscription. However, social media platforms allow users to subscribe to multiple communities. When pairs of users subscribe to multiple common lists, they form a common subscription network. Analysis on this network can provide insight into how pairs of users subscribe to the same list so that this information can be used to recommend subscriptions. In other words, we need to answer the research question: “What patterns of cosubscription to communities exist among social media platform users?” We do so in the next section.

## 5.1.2 Analysis of Patterns of Co-Subscription

Two users co-subscribe to the same community if they have similar interests. However, a user might have similarities with more than one user, and hence all the alters with whom a user has similarities could possibly cluster together—i.e., every user may be embedded in a community of common subscriptions because of varied interests, which can vary over time and in magnitude (Hong & Davison, 2010; Rakesh et al., 2014). We therefore need to quantify these preferences for subscription in terms of the common subscription community in which they are embedded and how that community evolves over time (Zhang et al., 2016). Similarly, membership in the same community of interest indicates that users post about similar topics and hence there is also a cluster of common membership relationships (and their temporal evolution) that can be leveraged for subscription. The local clustering coefficient (LCC) is a measure of how close the neighbors of a node are to being a complete graph (network in which every node is connected to every other node) (Watts & Strogatz, 1998a; Watts & Strogatz, 1998b). We therefore define a metric, the local clustering coefficient rank (LCCR), that uses temporal variation of LCC (in both the subscription and membership communities) to capture these properties.

To summarize, the intuition behind the local clustering coefficient rank (LCCR) is that users who are embedded in a closely knit network of common subscriptions (interests) with other users, who by themselves are in turn embedded in a similar tightly knit network, should have a higher rank, which indicates varied interests. This can be thought of as modeling the behavior of a random social media platform surfer, who has a certain set of interests and subscribes to communities that indicate these interests (Page et al., 1999). However, the user simultaneously explores other communities to which the subscribers or members of a community have subscribed. Hence, the strength and structure of these common subscriptions with other social media users varies over time and is captured using LCCR. To define LCCR, we first need to determine (1) the number of top users with whom a focal user is most similar, and (2) how membership communities are related to subscription communities in terms of LCC and temporal evolution. This is done using top-k analysis and by comparing the evolution of membership and subscription in these communities.

Top-k analysis: We looked at the clustering of top-k edges, by weighted-degree, incident on a node (a curator in this case). In this network, edges indicate the set of curators with whom a curator has the most similarity. Since the edges vary in weight, we looked at how the top-k edges identified evolve over time. Since we consider the LCC of a node, the minimum value of k is two. We found that the degree distribution of the network follows a power law where approximately 50% of the edges are covered at k = 10. We therefore calculated the LCC values for the subset of networks for k values between 2 and 10. For each node i and month m  {1, 2, 3, 4, 5, 6}, we calculated a nine-component vector as follows

$$
L C C _ {m} ^ {i} = <   L C C 2 ^ {i}, L C C 3 ^ {i}, L C C 4 ^ {i} \dots .. L C C 1 0 ^ {i} >\tag{2}
$$

where LCCK<sup>i</sup> is the value of LCC for a network for the top-k edges around a node. We therefore identified clusters of users who have a similar ego network of common subscriptions for their top-k edges. Figure 7 shows the results of the clustering.

Table 4. Assortivity Patterns (Subscription)

<table><tr><td rowspan="2"></td><td colspan="3">Degree</td><td colspan="3">Structural holes</td><td colspan="3">Betweenness centrality</td><td colspan="3">Closeness centrality</td></tr><tr><td>Assortativity</td><td>ASP</td><td>Z-score</td><td>Assortativity</td><td>ASP</td><td>Z-score</td><td>Assortativity</td><td>ASP</td><td>Z-score</td><td>Assortativity</td><td>ASP</td><td>Z-score</td></tr><tr><td>In-in</td><td>0.038</td><td>0.284</td><td>1.108</td><td>-0.038</td><td>-0.058</td><td>-3.078</td><td>0.031</td><td>0.502</td><td>0.087</td><td>-0.111</td><td>-0.202</td><td>-3.147</td></tr><tr><td>In-out</td><td>-0.006</td><td>-0.044</td><td>-0.11</td><td>0.029</td><td>0.044</td><td>1.723</td><td>0.029</td><td>0.528</td><td>0.223</td><td>0.007</td><td>0.013</td><td>0.115</td></tr><tr><td>Out-in</td><td>0.088</td><td>0.656</td><td>2.185</td><td>0.654</td><td>0.984</td><td>8.812</td><td>0.029</td><td>0.496</td><td>0.209</td><td>0.537</td><td>0.974</td><td>7.795</td></tr><tr><td>Out-out</td><td>0.094</td><td>0.696</td><td>2.693</td><td>0.107</td><td>0.161</td><td>2.575</td><td>0.027</td><td>0.471</td><td>0.085</td><td>-0.0503</td><td>-0.091</td><td>0.291</td></tr></table>

Table 5. Assortivity Patterns (Membership)

<table><tr><td rowspan="2"></td><td colspan="3">Degree</td><td colspan="3">Structural holes</td><td colspan="3">Betweenness centrality</td><td colspan="3">Closeness centrality</td></tr><tr><td>Assortativity</td><td>ASP</td><td>Z-score</td><td>Assortativity</td><td>ASP</td><td>Z-score</td><td>Assortativity</td><td>ASP</td><td>Z-Score</td><td>Assortativity</td><td>ASP</td><td>Z-score</td></tr><tr><td>In-In</td><td>0.103</td><td>0.387</td><td>19.264</td><td>0.259</td><td>0.347</td><td>-1.674</td><td>0.178</td><td>0.284</td><td>1.108</td><td>0.164</td><td>0.463</td><td>44.448</td></tr><tr><td>In-Out</td><td>0.049</td><td>0.184</td><td>8.011</td><td>0.203</td><td>0.272</td><td>-1.674</td><td>0.165</td><td>-0.044</td><td>-0.11</td><td>0.083</td><td>0.236</td><td>3.648</td></tr><tr><td>Out-In</td><td>0.2</td><td>0.755</td><td>44.961</td><td>0.544</td><td>0.729</td><td>-1.674</td><td>0.266</td><td>0.656</td><td>2.185</td><td>0.228</td><td>0.643</td><td>20.515</td></tr><tr><td>Out-Out</td><td>0.131</td><td>0.495</td><td>21.566</td><td>0.39</td><td>0.522</td><td>-1.69</td><td>0.247</td><td>0.696</td><td>2.693</td><td>0.198</td><td>0.56</td><td>13.312</td></tr></table>

![](/api/attachments/Z7FT5HDV/fulltext/images/3d5906ce7c2badc007b1844266c2ff129aebe6822be6a1c3881113fac8547bb1.jpg)  
Figure 7. LCC Clusters for Top-K Edges

Across different months, we consistently found three clusters: low, medium, and high LCC clusters. Also, the value of LCC monotonously increased with the value of k; in other words, common subscriptions with less similar users tended to get more similar over time. To investigate the temporal evolution of these clusters, we formulated an LCC evolution vector as follows

$$
\begin{array}{l} L C E V ^ {i} = <   D i f f \_ L C C 2 _ {1 2} ^ {i}, D i f f \_ L C C 3 _ {1 2} ^ {i}, D i f f \_ L C C 4 _ {1 2} ^ {i}, \\ \ldots , D i f f \_ L C C 1 0 _ {1 2} ^ {i}, D i f f \_ L C C 2 _ {2 3} ^ {i}, \\ D i f f \_ L C C 3 _ {2 3} ^ {i}, \ldots . D i f f \_ L C C 1 0 _ {5 6} ^ {i} > \end{array}\tag{3}
$$

Each component is the difference between the LCC values for two consecutive periods at a given k value.

We again used clustering to identify nodes whose topk edges evolved similarly.

We found an alternating pattern of increasing and decreasing values of LCC with the magnitude of difference increasing continuously. Since LCC is a measure of the density of the ego network, it indicates that common subscriptions between nodes continuously evolve indicating changing interests of pairs of users. However, we found that the greater the value of k, the greater the variation. This tells us that communities involving the largest weights of edges on a node do not fluctuate much while those of smaller edge weights fluctuate greatly. We found a similar pattern for bottom-k edges around a node. Analyses of comembership networks showed an alternating pattern between memberships and subscriptions indicating that whenever the top-k LCC increases for membership in a month, there is a corresponding decrease in the value for subscription and vice-versa.

We combined these observations with the proposition that clustering of the ego networks of nodes to which a focal node is connected can impact the subscription of a node to define the local clustering coefficient rank (LCCR) of a node, which is like page rank (Page et al., 1999), as follows

$$
\begin{array}{l} L C C R (c) = (1 - \boldsymbol {\beta}) + \boldsymbol {\beta} ^ {*} \sum_ {j \in N e i g h b o r h o o d (c)} L C C R (j) \\ * [ \sum_ {k = 2} ^ {1 0} \frac {1}{k} * \{(L C C _ {T o p k (j)}) / L C C _ {-} T o p k _ {-} M e m (j)) + \\ (L C C _ {-} B o t t o m k (j) / L C C _ {-} B o t t o m k _ {-} M e m (j)) ] \end{array}\tag{4}
$$

where

$\pmb { \beta }$ is the damping factor set at 0.85

LCC\_Topk(j) is the LCC value for the top-k edges around a node in the subscription network

LCC\_Topk\_Mem(j) is the LCC value for the topk edges around a node in the membership network

LCC\_Bottomk(j) is the LCC value for the bottomk edges around a node in the subscription network

LCC\_Bottomk\_Mem(j) is the LCC value for the bottom-k edges around a node in the membership network

Higher values of LCCR suggest that the node is connected to highly clustered nodes across the whole network in addition to being highly clustered in its own ego network. Because our sample had curators who created lists on various topics, it suggests that we could recommend a greater variety of lists to curators with a high value for this metric. The recursive algorithm for calculating LCCR is provided below. We found that for most of the periods, this algorithm converges in less than 30 iterations.

$$
\begin{array}{l} \text { Initialize:   } L C C R (i, t = 0) = L C C (i) \forall i \in \{1, 2, 3,... \\ 1 6 0 0 \} \end{array}
$$

$$
\begin{array}{l} \text {Update: LCCR(i, t + 1) = (1 - \boldsymbol{\beta}) +} \\ \boldsymbol {\beta} ^ {*} \sum_ {j \in N e i g h b o r h o o d (i)} L C C R (j, t) ^ {*} [ \sum_ {k = 2} ^ {1 0} \frac {1}{k} * \\ \{(L C C \_ T o p k (j, t)) / L C C \_ T o p k \_ M e m (j, t)) + \\ (L C C \_ B o t t o m k (j, t) / L C C \_ B o t t o m k \_ M e m (j, t)) \} ] \end{array}
$$

$$
\boldsymbol {E n d} \colon | L C C R (i, t + 1) - L C C R (i, t) | <   \varepsilon
$$

To summarize the assortativity and common subscription community analysis, for each curator $c \in$ U, we created a nine-component row-vector of network characteristics as follows:

$$
\begin{array}{c} n c _ {c} = [ L C C R _ {c} i n \_ d e g _ {c} o u t \_ d e g _ {c} s h \_ i n _ {c} s h \_ o u t _ {c} \\ b w \_ i n _ {c} b w \_ o u t _ {c} c c \_ i n _ {c} c c \_ o u t _ {c} 1 ] \end{array}
$$

We kept the last component as 1 because we multiply it with the eigen vector centrality of the two-mode network in the next section, where we create the final matrix of preferences for the network characteristics. We created this vector for all the curators and called this matrix $\mathrm { N C } _ { \mathrm { U } }$

While the assortativity and community analyses give us an idea of how the structural characteristics of the network around a curator and list can predict subscription, we do not know how the positional characteristics, in the overall network of lists and their members and subscribers, can predict subscription. This is investigated in the next section.

## 5.1.3 Quantifying the Impact of Positional Characteristics

In this section, we answer the research question “How do the positional characteristics of communities and social media platform users in a network determine $s u b s c r i p t i o n ? ^ { , }$ Here we measure the correlation between the various centralities (betweenness, closeness, and the eigen vector) and the member and subscriber count of lists. We use the two-mode networks of membership and subscription. The intuition is that more central lists might be subscribed to by more users. On average, we found that there is substantial correlation between subscriber count and betweenness centrality, and there is a strong correlation between membership count and closeness centrality, as shown in Table 6. We also found that eigen vector centrality has a moderately weak correlation to both membership and subscription.

For each list $l { \in } \mathrm { L } ,$ , we create a nine-component columnvector of two-mode network characteristics as follows:

$$
n c _ {l} = \left[ \begin{array}{c} 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ b c _ {l} \\ b c _ {l} \\ c c _ {l} \\ c c _ {l} \\ e c _ {l} \end{array} \right]
$$

where b $\therefore l , { \mathrm { c c } } _ { l } ,$ ec<sub>l</sub> represent the betweenness, closeness, and eigen vector centralities, respectively, in the twomode subscription network. Note that the first five components are 1s because when we multiply this matrix with a row in $\mathrm { N C } _ { \mathrm { U } } ,$ , it gives the components for LCC rank, in and out degree, and structural holes based on the common subscription and list-list networks. These components do not exist in the list-user network since it is undirected.

Table 6. Network Metrics Correlation

<table><tr><td></td><td>Betweenness centrality</td><td>Closeness centrality</td><td>Eigen vector centrality</td></tr><tr><td>Member count</td><td>0.001</td><td>0.451</td><td>0.045</td></tr><tr><td>Subscriber count</td><td>0.381</td><td>0.016</td><td>0.031</td></tr></table>

We created this vector for all the lists and called this matrix $\mathrm { N C _ { L } }$ . To get the curator preference for a certain list in terms of the network characteristics, we multiplied these two matrices as follows

$$
\mu = \mathrm{NC} _ {\mathrm{U}} \times \mathrm{NC} _ {\mathrm{L}}\tag{5}
$$

## 5.2 General Community Features

Here, we discuss the user preferences for list membership and subscription in terms of the general characteristics of the lists. Because millions of communities exist on social media platforms and new ones are created daily, there is a deficit of user attention on these platforms (Bessi et al., 2014; Davenport & Beck, 2001; Rakesh et al., 2014; Rui & Whinston, 2012). Thus, we argue that simple general properties of communities such as size and overlap can help users determine which communities to subscribe to. In other words, we answer the question “What general features of online communities, such as their size and overlap, help recommend them for subscription?”

## 5.3 Analysis on Curated and Subscribed List Sizes

We investigated whether users have a certain preference for community size. Since we used Twitter as a context for this work, we calculated the average member size for all the curated and subscribed lists of a user. The curated list size distribution has a mean of 118 and a standard deviation of 257 indicating sufficient heterogeneity in terms of preferred list size. The subscribed list size distribution has a mean of 393 and a standard deviation of 616, indicating that there is also sufficient heterogeneity in terms of preferred subscribed list size. A longitudinal analysis of the average list sizes revealed that the distribution remained the same throughout our data collection period of six months. We thus expected the subscriber size of the list to be a predictor for subscription. We observed that lists with more members also tend to have more subscribers, so we also expected membership size to be a predictor for subscription. Given the fact that users can create or subscribe to multiple lists, it would be useful to explore the extent of overlap (common members) among these lists. This is examined in the next section.

## 5.4 Analysis on List Overlaps

To determine the extent of membership overlap across all the created public lists of a curator $j ,$ we defined a new metric as follows:

$$
M e m b e r s h i p O v e r l a p _ {j} = \frac {\sum_ {i \in S \_ M e m b e r s} \frac {N _ {l i s t e d \_ i}}{N _ {l i s t s \_ j}}}{n (S \_ M e m b e r s)} (6)
$$

where $N _ { l i s t e d \_ i }$ is the number of lists to which a member i belongs across all of curator $j ^ { \circ } \mathbf { s }$ public lists, $N _ { l i s t s \_ j }$ is the number of public lists for curator $j ,$ and ??\_?????????????? is the set of all the distinct members across curator $j ^ { \circ } \mathbf { s }$ public lists. Higher values of this metric indicate a large overlap among a curator’s lists. We similarly defined a metric to calculate the overlap among the lists to which a curator subscribes (using the members of the subscribed lists).

We observed that there is little overlap in terms of both membership and subscription (the mean for both was close to zero). However, there were clearly visible patterns that suggest heterogeneity among users in terms of subscription and membership overlap (the standard deviations were 0.2 and 0.3 respectively). We also found that these overlaps remained consistent throughout the data collection period. Hence, this can serve as a predictor for subscription.

To conclude this analysis, for each curator cU, we defined a four-component vector of general characteristics (gc<sub>c</sub>) as follows:

$$
\begin{array}{c} g c _ {c} = [ l i s t \_ s i z e \_ m e m _ {c} l i s t \_ s i z e \_ s u b _ {c} \\ m e m \_ o v e r l a p _ {c} s u b s \_ o v e r l a p _ {c} ] \end{array}
$$

$l i s t \_ s i z e \_ s u b _ { c }$ indicates the average member count and subscriber count of the lists for a curator, and ??????\_?????????????? and ????????\_???????? $\cdot l a p _ { c }$ represent the membership and subscription overlaps among the curated and subscribed lists for the curator. Thus, matrix (GC<sub>C</sub>) has four components for each curator in our dataset.

Similarly, for each list l that belongs to the set of lists $L ,$ we define a four-component column vector gc<sub>l</sub> as follows:

$$
g c _ {l} = \left[ \begin{array}{c} l i s t \_ s i z e \_ m e m _ {l} \\ l i s t \_ s i z e \_ s u b _ {l} \\ a v g \_ m e m \_ o v e r l a p _ {l} \\ a v g \_ s u b \_ o v e r l a p _ {l} \end{array} \right]
$$

Where ????????\_????????\_??????<sub>??</sub> and $l i s t \_ s i z e \_ s u b _ { l }$ indicate the member and subscriber counts, respectively, for the list l and ??????\_??????\_??????????????<sub>??</sub> and ??????\_??????\_??????????????<sub>??</sub> indicate the average membership and subscription overlap with the curated and the subscribed lists respectively. Thus matrix $( \mathrm { G C _ { L } } )$ has these four components for each of the lists.

To compute user preference for subscription to a list in terms of these characteristics, we created a matrix by multiplying the two matrices, $\mathrm { G C _ { C } }$ and $\mathrm { G C _ { L } } ,$ as follows:

$$
\triangle = G C _ {C} X G C _ {L}\tag{7}
$$

## 5.5 Baseline Feature Extraction: Content Analysis

A survey of Twitter users found that they use lists to filter their tweets into topics (de la Rouviere and Ehlers, 2013). Previous work has also found that tags extracted from the list names are representative of a user’s topical interests (Yamaguchi et al., 2011). Here we propose using the topic of the list tweets and those of the curators as a baseline for performance comparison. We describe how we derive these topics below.

## 5.6 Deriving User Interest Topics

The topical interest of curators $\{ \mathbf { c } _ { 1 } , \mathbf { c } _ { 2 } , \mathbf { c } _ { 3 } , . . . \mathbf { c } _ { 1 6 0 0 } \} \in \mathrm { U }$ and topics $\{ \mathrm { t } _ { 1 } , \ \mathrm { t } _ { 2 } , \ \mathrm { t } _ { 3 } , \ \hdots \ \mathrm { t } _ { n } \} \ \in \mathrm { T }$ is modeled using a matrix as follows. Following Rakesh et al. (2014), the topics were derived from the curator tweets using a discrete dynamic topic model (DDTM)—previous research has shown that simple LDA has poor performance on short text (Hong & Davison, 2010). We found that the optimal number of topics was 10. For each curator cU, the set of topics was modeled as a ten-component row vector as follows

$$
\begin{array}{c} t w _ {c} = \left[ t w _ {c 1} t w _ {c 2} t w _ {c 3} t w _ {c 4} t w _ {c 5} t w _ {c 6} t w _ {c 7} t w _ {c 8} \right. \\ \left. t w _ {c 9} t w _ {c 1 0} \right] \end{array}
$$

Each entry in this matrix indicates the number of tweets of the curator for that topic. We created this row-vector for all the curators (U) and combined them to create a matrix $\mathrm { T W _ { U } }$

## 5.7 Deriving List Topics

We used the tweets of each list to get the list topics. For each list lL, we created a ten-component column vector of tweets as follows

$$
t w _ {l} = \left[ \begin{array}{c} t w _ {l 1} \\ t w _ {l 2} \\ t w _ {l 3} \\ t w _ {l 4} \\ t w _ {l 5} \\ t w _ {l 6} \\ t w _ {l 7} \\ t w _ {l 8} \\ t w _ {l 9} \\ t w _ {l 1 0} \end{array} \right]
$$

Each entry in this matrix indicates the number of tweets in the list for that topic. We then created this column vector for each list lL and combined them to create a matrix $\mathrm { T W } _ { \mathrm { L } } .$ To get the user preference for a certain list in terms of the tweet topics, we multiplied these two matrices as follows:

$$
\Omega = T W _ {U} X T W _ {L}\tag{8}
$$

## 6 Demonstration and Evaluation: Results

In the design phase, we identified many features for recommending lists for subscription. Here we demonstrate how we leveraged these features to build models that generate recommendations and describe the metrics we use to evaluate them.

## 6.1 Models for Subscription

Following Rakesh et al. (2014), for curator cU and list lL, we generated the recommendation score for subscription as follows

$$
P (c, l) = \alpha \varDelta + \beta \mu + \gamma \varOmega\tag{9}
$$

In this equation, we call the first component the general characteristics, the second one the network characteristics and the third one the tweet characteristics. For this study, we used a rich set of features that encompass general, textual, and networkrelated metrics. Therefore, we argue that neural network methods offer the best results because of their ability to combine a diverse set of inputs and capture their complex relationship to the output (Frosst & Hinton, 2017; Graves et al., 2013; Szegedy et al., 2015). In addition, neural networks provide better results when used on large datasets like ours. We used a variety of other techniques including generalized additive models, logistic, Ridge and Lasso regressions, sparse LDA, SVM, decision trees, random forests etc., and found that neural networks provide the best results (across all the evaluation metrics discussed in the next section). To avoid overfitting, we used ten-fold crossvalidation. We also used a comprehensive set of hyperparameter optimization techniques to derive the optimal values for the size of the neural network, number of hidden layers, and learning and dropout rates. To overcome the lack of interpretability associated with neural network methods, we used a variety of metrics from explainable AI, including feature importance, feature permutations, Shapley values, and feature interactions (Fisher et al., 2018; Friedman, 1997; Štrumbelj & Kononenko, 2014).

## 6.2 Evaluation Metrics

For evaluating the quality of recommendations generated by our model, we used a comprehensive set of six metrics: overall accuracy, precision, recall, and $f -$ score at rank k, mean reciprocal rank (MRR), and discounted cumulative gain (DCG). Each of these metrics is calculated as follows:

Overall accuracy: This metric gives the fraction of recommendations that are correct.

Precision at rank k (k=1, 5, 10): This is the fraction of the recommendations in the top-k positions generated by our model that resulted in a subscription.

Recall at rank k (k=1, 5, 10): This is the fraction of top-k subscribed lists that were recommended by our model.

F-score at rank k (k=1, 5, 10): This is the harmonic mean of precision and recall at rank k.

Mean reciprocal rank (MRR): Our recommendation is correct if the list suggested by our model is subscribed to by the curator. Mean reciprocal rank (Craswell, 2009) is the inverse of the position of the first correct recommendation in the set generated by our model. For a given set S of recommendations generated by our model, we calculate the mean reciprocal rank as follows:

$$
M R R = \frac {1}{n (U)} \sum_ {i = 1} ^ {n (U)} \frac {1}{r a n k _ {i}}\tag{10}
$$

where ?????? $k _ { i }$ is the rank of the first relevant document for the $i ^ { \mathrm { { t h } } }$ query (recommendation for the $i ^ { \mathrm { { t h } } }$ user in this case) and U is the set of curators in the sample.

Discounted cumulative gain (DCG): This metric is based on two assumptions: highly relevant lists are more useful when they appear at the top of a given set of recommendations, and highly relevant lists are more useful than marginally relevant lists. The discounted cumulative gain (Järvelin $\&$ Kekäläinen, 2000) at a particular rank position p (here $p = 1 0 )$ was calculated as follows

$$
D C G _ {p} = \frac {1}{n (U)} \sum_ {j = 1} ^ {n (U)} \sum_ {i = 1} ^ {p} \frac {2 ^ {r e l _ {i} ^ {j}} - 1}{l o g _ {2} (i + 2)}\tag{11}
$$

$$
\begin{array}{l} \text {where} r e l _ {i} ^ {j} = \\ \left\{ \begin{array}{l l} 1 & \text {if the recommendation at position i is correct} \\ 0 & \text {if the recommendation at position i is wrong} \end{array} \right. \end{array}
$$

All these metrics were calculated on a test sample using the standard 10-fold cross-validation. Considering that the temporal dataset we used may be prone to data leakage issues (both target leakage and train-test leakage), we performed the training and testing only within a certain time. The features for our design phase were also formulated using only the results from the training set. In addition, to avoid issues associated with the overrepresentation of a majority class (not subscribed to a list in this case), we used the synthetic minority oversampling technique (SMOTE) for our dataset. To reduce the upward bias associated with cross-validation, we used bootstrapping with 1000 samples on the training datasets to estimate the standard errors (reported in the parenthesis in Table 7).

## 6.3 Results

Since network and general features form the core of the contribution in this research, we used textual (content) features (Yang et al., 2015) as the baseline for comparing the performance of these two sets of features. We also used the five common state-of-the-art algorithms in recommender systems as another baseline. In addition, we used the latest existing work on recommending lists on Twitter for another set of three baselines (Han et al., 2016; Rakesh et al., 2014; Yin et al., 2019). Finally, we also evaluated how well the identified sets of features complemented the textual features, i.e., we investigated all possible combinations of the three types of features. We thus answered the question: “How do features from networks and general properties compare with the content features from the communities? How do they supplement them?”

Table 7 shows the results of the subscription recommenders. These results are aggregated across the six-month period, as we did not find any difference in the evaluation metrics from month to month. Figure 8 shows the precision, recall, and f-score values for the top 1, 5, and 10 recommendations. We observe that network characteristics outperform both the general and textual characteristics in terms of precision at the top position, meaning that at any given point of time, network features are preferable to any other type of features at generating useful list recommendations at the top. In addition, a combination of network and general features offers the best results (for the top position) among all possible combinations of features, suggesting that these two types of features complement each other to produce highquality outcomes.

However, among the models that use only one type of feature, textual features provide better results in the top-5 and top-10 positions along with better MRR and DCG values, indicating that the topics of the tweets alone, while not able to provide good recommendations at the top, are nevertheless useful in generating good recommendations overall. But a combination of general and network features outperforms the textual characteristics across all evaluation metrics and all positions, suggesting that this combination carries more useful and relevant information than the topic of the tweet. The precision values in the top-5 and top-10 positions increased by 10% and 5%, respectively, with a 12.4% increase in MRR and 10% increase in DCG, indicating that this combination of features provides very good utility in terms of high-quality recommendations in the top positions. While the overall accuracy dropped down, considering that for any given user, most of the lists in the sample were neither recommended by our models nor actually subscribed by users, we argue that overall accuracy is not relevant here. Moreover, the recall values were the same for both models suggesting that all the relevant subscriptions were suggested in both cases, while more relevant ones were revealed with the combination of general and network features.

Table 7. Results

<table><tr><td></td><td colspan="3">Precision</td><td colspan="3">Recall</td><td colspan="3">F-score</td><td rowspan="2">MRR</td><td rowspan="2">DCG</td><td rowspan="2">Overall accuracy</td></tr><tr><td></td><td>1</td><td>5</td><td>10</td><td>1</td><td>5</td><td>10</td><td>1</td><td>5</td><td>10</td></tr><tr><td>Textual</td><td>0.7(0.008)</td><td>0.82(0.002)</td><td>0.9(0.004)</td><td>1(0.001)</td><td>1(0.002)</td><td>1(0.003)</td><td>0.82(0.08)</td><td>0.9(0.02)</td><td>0.95(0.03)</td><td>0.876(0.0)</td><td>3.52(0.012)</td><td>98.43(0.006)</td></tr><tr><td>General</td><td>0.3(0.0)</td><td>0.22(0.003)</td><td>0.25(0.001)</td><td>0.3(0.002)</td><td>0.36(0.001)</td><td>0.35(0.002)</td><td>0.3(0.0)</td><td>0.27(0.0)</td><td>0.29(0.0)</td><td>0.3(0.012)</td><td>0.944(0.061)</td><td>95.61(0.002)</td></tr><tr><td>Network</td><td>0.8(0.005)</td><td>0.76(0.001)</td><td>0.68(0.002)</td><td>0.8(0.007)</td><td>0.92(0.001)</td><td>0.75(0.002)</td><td>0.8(0.009)</td><td>0.83(0.02)</td><td>0.71(0.03)</td><td>0.727(0.015)</td><td>2.565(0.11)</td><td>95.66(0.001)</td></tr><tr><td>Textual+General</td><td>0.8(0.001)</td><td>0.92(0.022)</td><td>0.96(0.003)</td><td>1(0.001)</td><td>1(0.002)</td><td>1(0.003)</td><td>0.89(0.005)</td><td>0.96(0.02)</td><td>0.98(0.03)</td><td>0.883(0.029)</td><td>3.288(0.052)</td><td>96.03(0.002)</td></tr><tr><td>Textual+Network</td><td>0.3(0.0)</td><td>0.22(0.002)</td><td>0.25(0.003)</td><td>0.3(0.001)</td><td>0.36(0.002)</td><td>0.33(0.003)</td><td>0.3(0.009)</td><td>0.27(0.02)</td><td>0.28(0.03)</td><td>0.3(0.015)</td><td>0.944(0.019)</td><td>98.43(0.007)</td></tr><tr><td>Network+General</td><td>0.97(0.001)</td><td>0.92(0.002)</td><td>0.95(0.003)</td><td>1(0.001)</td><td>1(0.002)</td><td>1(0.003)</td><td>1(0.01)</td><td>0.96(0.02)</td><td>0.97(0.03)</td><td>1(0.0)</td><td>3.88(0.0)</td><td>96.25(0.002)</td></tr><tr><td>All</td><td>0.8(0.008)</td><td>0.94(0.002)</td><td>0.97(0.003)</td><td>1(0.001)</td><td>1(0.002)</td><td>1(0.003)</td><td>0.89(0.008)</td><td>0.97(0.02)</td><td>0.98(0.03)</td><td>0.95(0.024)</td><td>3.967(0.037)</td><td>96.04(0.009)</td></tr><tr><td colspan="13">State-of-the-art algorithms</td></tr><tr><td>User-based</td><td>0.0201(0.001)</td><td>0.0040(0.001)</td><td>0.0020(0.002)</td><td>0.226(0.01)</td><td>0.328(0.02)</td><td>0.319(0.02)</td><td>0.0369(0.003)</td><td>0.0079(0.001)</td><td>0.004(0.001)</td><td>0.0201(0.002)</td><td>0.0127(0.002)</td><td>97.1(0.039)</td></tr><tr><td>List-based</td><td>0.0201(0.001)</td><td>0.0040(0.001)</td><td>0.0020(0.002)</td><td>0.226(0.01)</td><td>0.328(0.02)</td><td>0.319(0.02)</td><td>0.0369(0.003)</td><td>0.0078(0.001)</td><td>0.004(0.001)</td><td>0.0201(0.002)</td><td>0.0127(0.002)</td><td>97.1(0.04)</td></tr><tr><td>Dimensionality-reduction</td><td>0.0201(0.0)</td><td>0.0040(0.002)</td><td>0.00002(0.0)</td><td>0.847(0.09)</td><td>0.001(0.0)</td><td>0.0001(0.0)</td><td>0.0393(0.001)</td><td>0.0016(0.0)</td><td>0.00003(0.0)</td><td>0.0201(0.001)</td><td>0.0127(0.002)</td><td>98.9(0.09)</td></tr><tr><td>Generative-mixture model(GMM)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.112(0.002)</td><td>0.114(0.003)</td><td>0.124(0.002)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>99.8(0.13)</td></tr><tr><td>Link-analysis</td><td>0.0201(0.002)</td><td>0.0040(0.001)</td><td>0.0020(0.001)</td><td>0.203(0.01)</td><td>0.302(0.002)</td><td>0.286(0.003)</td><td>0.0365(0.002)</td><td>0.0079(0.001)</td><td>0.0039(0.002)</td><td>0.0201(0.001)</td><td>0.0127(0.001)</td><td>98.9(0.12)</td></tr><tr><td colspan="13">Existing methods</td></tr><tr><td>List PageRank</td><td>0.84(0.05)</td><td>0.82(0.001)</td><td>0.89(0.002)</td><td>1(0.001)</td><td>1(0.003)</td><td>1(0.002)</td><td>0.84(0.01)</td><td>0.9(0.02)</td><td>0.91(0.03)</td><td>0.833(0.02)</td><td>3.46(0.01)</td><td>92.62(0.008)</td></tr><tr><td>Community similarity degree(CSD)</td><td>0.53(0.05)</td><td>0.67(0.01)</td><td>0.68(0.02)</td><td>0.8(0.01)</td><td>0.9(0.02)</td><td>0.75(0.02)</td><td>0.63(0.005)</td><td>0.27(0.018)</td><td>0.407(0.003)</td><td>0.74(0.001)</td><td>1.74(0.09)</td><td>95.59(0.001)</td></tr><tr><td>Bipartite graph embedding model(BGEGM)</td><td>0.74(0.01)</td><td>0.82(0.02)</td><td>0.88(0.03)</td><td>0.4(0.01)</td><td>0.45(0.02)</td><td>0.31(0.03)</td><td>0.519(0.02)</td><td>0.189(0.03)</td><td>0.227(0.04)</td><td>0.45(0.001)</td><td>2.23(0.02)</td><td>95.67(0.002)</td></tr><tr><td colspan="13">Note: The values in the parenthesis indicate standard errors calculated using 1000 bootstrap samples across different time periods. The bold characters indicate the combination of features that give the best results across all metrics</td></tr></table>

![](/api/attachments/Z7FT5HDV/fulltext/images/1cbe4d4ef02d2a8ce260e4f820f957904b14a750dee09a7a0a4b762134831ca1.jpg)

![](/api/attachments/Z7FT5HDV/fulltext/images/68d42bb024fdfd8a7d603c149580858095f5291f44da9a83ea45d395f4e0db92.jpg)

![](/api/attachments/Z7FT5HDV/fulltext/images/19630b312d5cfa610d832aa9bf616453a4cfed041b98210d8ab8e5531678a0b6.jpg)  
Figure 8. Precision, Recall, and F-Score Values

A comparison of the feature importance (using the reduction in classification error rates when permuting the feature values; see Fisher et al., 2018) for a model that uses a combination of general and network features with one that uses textual features only reveals that features in the former contribute more (on average) to reducing the error rates (see Figures B1 and B2 in the Appendix). Moreover, a comparison of Shapley values (Štrumbelj & Kononenko, 2014), which measure the average marginal contribution of each feature over all possible combinations of the rest, suggest that each of the features in the model that combine general and network features offer higher contributions to the precision of the models, when compared to the model that uses only textual features (see Figures B3 and B4 in the Appendix). These results reinforce and supplement findings from the previous literature—i.e., list features (a combination of general and network features, in this case) are much more indicative of user interests than tweet topics (Yamaguch et al., 2011).

A combination of textual and network characteristics provides inferior results when compared to using only one set of these features. An examination of feature importance values reveals that, in this combination of features, network characteristics do not contribute anything to reducing the classification error, thus creating the “curse of dimensionality” (Friedman, 1997) in the combined model. Finally, a combination of all three types of features, while offering lower performance in the first position, generates good quality recommendations overall, thus suggesting not only the utility of this combination but also the value of network and general characteristics in supplementing the existing baseline.

Comparison of the performance with state-of-the-art algorithms indicates that while these algorithms help generate accurate recommendations by weeding out irrelevant recommendations, our models substantially outperformed all these models on the remaining metrics, thus helping to generate relevant recommendations at the top. In addition, our models also outperformed the existing work on recommending Twitter lists that uses content, network analysis, or deep learning methods. To summarize, we propose using a combination of general and network features if the purpose is to generate goodquality recommendations in the first position and using a combination of all the three if the purpose is to generate good recommendations overall in all top 10 positions.

## 7 Communication: Conclusion and Contributions

This research proposes a design science-based method to recommend communities of interest on social media platforms. Leveraging the networks among and between communities and different types of platform users, we propose several new features related to subscription behavior. Using these features, we built recommenders that can suggest communities to which a user may subscribe. Our results suggest that networkrelated variables not only outperform the existing baseline features, in terms of generating high-quality recommendations in the top position, but also complement these features to generate substantially better results. These results have implications for building recommender systems for community subscription on social media platforms. Our work also has implications for social media marketers because it could help them locate the right audience for their target products, helping them reduce time and cost inefficiencies in advertising. Finally, our research also contributes significantly to the literature on using big data analytics in design science. To the best of our knowledge, this is the first work that uses network, content, and general community features to build subscription recommenders, which allows us to contribute on theoretical, methodological, and practical levels.

## 7.1 Theoretical Contributions

Our work contributes to design science frameworks using big data analytics that combine multiple types of datasets. We propose a design science method (Figure 2) that combines network, content, and general community characteristics, to understand subscription behavior on social media platforms. In areas where there is a lack of appropriate social science and economic theory, but large datasets about various aspects of behavior are available (Provost & Fawcett, 2013; Shmueli, 2010; Shmueli & Koppius, 2011; Velichety et al., 2019), insights from performing this kind of analysis may provide features for recommendations on other social media platforms. Evaluation of models built using these features shows that they are both useful and robust. Even though not all platforms have the option of subscribing explicitly to communities of interest, they nevertheless always provide a feature for creating these communities. Therefore, it would help users if platforms could suggest relevant communities with interesting content. Platforms could leverage the appropriate network structure (and the metrics we propose here) along with general community properties to suggest such communities. Our research provides a way to identify appropriate networks between and among users and communities, which can in turn be used to quantify user preferences. Thus, we provide an overarching approach to employing network, nonnetwork, and textbased analysis to understand human behavior on social media platforms, which can lead to the design and evaluation of recommenders. Abbasi et al. (2016) posit that one of the opportunities for big data in design science research is “leveraging volume and variety to develop novel artifacts for prediction or description.” A recent article discusses how recommender systems enhance entrenched biases in existing data and why more exploration (with new features) is needed to overcome these biases (Tufekci, 2019). Our work constitutes a step forward in these directions that allows us to contribute significantly to the work on using design science frameworks for big data analytics research (Abbasi et al., 2010; Chau & Xu, 2012; Dong et al., 2018; Hu et al., 2012; Kitchens et al., 2018).

## 7.2 Methodological Contributions

Our research also contributes to the literature on using social network methods for quantifying user preferences for content consumption on social media platforms. We propose several network features, and relevant efficient algorithms, which incorporate preferences for consuming content from online communities. To formulate these features, we combine previous literature from several areas including small-world phenomena (Watts & Strogatz, 1998a; Watts & Strogatz, 1998b), connectivity in networks (Freeman, 1977), strength of weak connections (Burt, 2004), random surfer model of the web (Page et al., 1999), and temporal variation of user interests on social media platforms (Hong & Davison, 2010; Rakesh et al., 2014). We also provide efficient algorithms to calculate these metrics.

These features were shown to provide superior recommender performance over the existing network and deep learning-related features but at the same time are more interpretable. They could be customized and extended to build recommenders on other social media platforms like Facebook, LinkedIn, Pinterest etc., For example, the common subscription network in this case used lists to construct the network. We could translate this network into a common boards network in the case of Pinterest or common groups network in the case of Facebook. Similarly, because the creators of Facebook groups or Pinterest boards also simultaneously consume content from other groups or boards, we could translate the list-list network to either a group-group network or a board-board network. In addition, the network metrics for assortativity and the local clustering coefficient rank (LCCR) could be used not only to understand the impact of diversity and its evolution on subscription behavior but also to study how the structural, positional, and community characteristics of networks may impact link attachment. This in turn could inform marketers about how their social media targeting strategies can evolve over time. Finally, these metrics have greater interpretability than either metrics like Metapath (Sun et al., 2011), used to capture similarity in heterogenous networks, or neural network embeddings that project network data into high-dimensional space.

## 7.3 Practical Contributions

Our work contributes significantly to the research on building recommender systems for online communities on social media platforms (Kamath et al., 2013; Rakesh et al., 2014; Ronen et al., 2014; Xiao et al., 2017; Yang et al., 2015; Yin et al., 2019). We propose new features using network science and design a method for generating recommendations using these features. Existing literature in this area relies heavily on either the content posted to these communities (Kamath et al., 2013; Yamaguchi et al., 2011; Yang et al., 2015) or the characteristics of the relationships among users for recommendation (Han et al., 2016; Rakesh et al., 2014). In this study, we argue for the role of structural network characteristics of the communities, propose new features that quantify user preferences in terms of these features, and show that they are useful for recommending online communities.

## 8 Limitations and Future Work

In this paper, we propose and evaluate a recommender system for online community subscription on social media platforms using network and design science. Our work has certain limitations that also open doors for several areas of research on online communities, network analysis, design science, and recommender systems.

First, network analysis revealed preferences for subscription and membership using the positional, structural, and community characteristics of the network in which a list and its curators, members, and subscribers are embedded. This research leveraged the first-degree connections in determining subscription and membership. However, as shown in Rakesh et al. (2014), there may also be an impact from seconddegree connections—i.e., lists to which the members of a list subscribe or the other lists that these users belong to. Such research would require the collection of larger datasets. Given the increasing availability of such datasets (Ransbotham et al., 2012; Zhang et al., 2016), we hope to expand our work in the future to assess the impact of second-degree network characteristics. Such work could open doors for formulating more network-related metrics to quantify user preferences.

Second, while our analysis revealed some relationships between membership and subscription and used these for prediction, the interplay between these two behaviors—i.e., information production and consumption behavior—should be explored more broadly. Previous studies in marketing and information systems have studied the relationship between the two using economic models (Ransbotham et al., 2012; Zhao et al., 2018). However, the impact of structural network characteristics, which quantify user preferences for information production and consumption, has not yet been examined. Our study opens doors for future studies involving combining membership and subscription networks using criteria such as common members, subscribers, or a weighting scheme to measure the importance of the two networks.

Third, we collected comprehensive data about the subscription behaviors of 1600 Twitter users, analyzed the patterns, extracted relevant features, and built a recommender using these features. However, most social media platforms have millions of active daily users. We collected a comprehensive set of lists spanning multiple areas from sports to healthcare and economics to religion, thus making our results applicable to platform users with a variety of interests. However, the rate limitations of Twitter API make it difficult to implement our solution at scale. In the future, we hope to continue working on this aspect by collaborating with several upcoming platforms to gain access to such data and test our solution at scale.

Finally, while our work uses a large dataset from Twitter lists to demonstrate how to build recommender systems, in the future, we hope to collect datasets from other platforms, such as groups on Facebook and LinkedIn, and apply contextual information about user behavior on these platforms to assess the feasibility of building recommender systems.

## References

Abbasi, A., Sarker, S., & Chiang, R. H. (2016). Big data research in information systems: Toward an inclusive research agenda. Journal of the Association for Information Systems, 17(2), ixxxii.

Abbasi, A., Zhang, Z., Zimbra, D., Chen, H., & Nunamaker Jr, J. F. (2010). Detecting fake Websites: The contribution of statistical learning theory. MIS Quarterly, 34(3), 435-461.

Abiragi, C. (2019). Using targeted Twitter lists to finetune your online monitoring. Ragan’s PR Daily. https://www.prdaily.com/how-to-use-twitterlists-to-become-a-social-listening-rock-star/

Bessi, A., Scala, A., Rossi, L., Zhang, Q., & Quattrociocchi, W. (2014). The economy of attention in the age of (mis)information. Journal of Trust Management, 1(1), 1-13.

Bhattacharya, D., & Ram, S. (2012). Sharing news articles using 140 characters: A diffusion analysis on Twitter. Proceedings of the 2012 IEEE/ACM International Conference On Advances in Social Networks Analysis and Mining, 966-971.

Borgatti, S. P. (2005). Centrality and network flow. Social Networks, 27(1), 55-71.

Borgatti, S. P., & Halgin, D. S. (2011). Analyzing affiliation networks. The Sage Handbook of Social Network Analysis. SAGE.

Burt, R. S. (2002). The social capital of structural holes. In M. F. Guillen, R. Collins, P. England, & M. Meyer (Eds.), The New Economic Sociology: Developments in an Emerging Field (pp. 148- 190). The Russell Sage Foundation.

Burt, R. S. (2004). Structural holes and good ideas. American Journal of Sociology, 110(2), 349- 399.

Butler, B. S. (2001). Membership size, communication activity, and sustainability: A resource-based model of online social structures. Information Systems Research, 12(4), 346-362.

Capocci, A., Servedio, V. D. P., Colaiori, F., Buriol, L. S., Donato, D., Leonardi, S., & Caldarelli, G. (2006). Preferential attachment in the growth of social networks: The internet encyclopedia Wikipedia. Physical Review E, 74(3), Article 036116.

Chau, M., & Xu, J. (2012). Business intelligence in blogs: Understanding consumer interactions and communities. MIS Quarterly, 36(4), 1189- 1216.

Coleman, J S. (1988). Social capital in the creation of human capital. American Journal of Sociology, 95-120.

Coleman, James S., & Coleman, J. S. (1994). Foundations of social theory. Harvard University Press.

Craswell, N. (2009). Mean reciprocal rank. In L. Liu, Ling & M. T. Özsu, (Eds.), Encyclopedia of Database Systems (pp. 1703-1703). Springer.

Davenport, T. H., & Beck, J. C. (2001). The attention economy. Ubiquity (May), Article 6.

de la Rouviere, S., & Ehlers, K. (2013). Lists as coping strategy for information overload on Twitter. Proceedings of the 22nd International Conference on World Wide Web Companion, 199-200.

DePhillips, Kari (2019). How to use Twitter lists to market your business. https://contefac.com/ create-use-twitter-lists-market-business

Dong, W., Liao, S., & Zhang, Z. (2018). Leveraging financial social media data for corporate fraud detection. Journal of Management Information Systems, 35(2), 461-487.

Dopson, E. (2018). How to use Twitter lists for lead generation, influencer marketing and beyond. sendible. https://www.sendible.com/insights/ twitter-lists-for-lead-generation

Faraj, S., Jarvenpaa, S. L., & Majchrzak, A. (2011). Knowledge collaboration in online communities. Organization Science, 22(5), 1224-1239.

Fisher, A., Rudin, C., & Dominici, F. (2018). Model class reliance: Variable importance measures for any machine learning model class, from the. Rashomon” perspective. https://arxiv.org/pdf/ 1801.01489v1.pdf

Foster, J. G., Foster, D. V, Grassberger, P., & Paczuski, M. (2010). Edge direction and the structure of networks. Proceedings of the National Academy of Sciences, 107(24), 10815-10820.

Freeman, L. C. (1977). A set of measures of centrality based on betweenness. Sociometry, 40(1), 35- 41.

Friedman, J. H. (1997). On bias, variance, 0/1: Loss, and the curse-of-dimensionality. Data Mining and Knowledge Discovery, 1(1), 55-77.

Frosst, N., & Hinton, G. (2017). Distilling a neural network into a soft decision tree. Presented at the 16th International Conference of the Italian Association for Artificial Intelligence.

Ghosh, S., Sharma, N., Benevenuto, F., Ganguly, N., & Gummadi, K. (2012). Cognos: Crowdsourcing search for topic experts in microblogs. Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval, 575-590.

Goldman, J. (2015). 9 ways you can take advantage of Twitter lists. Inc.com. https://www.inc.com/ jeremy-goldman/9-ways-you-can-takeadvantage-of-twitter-lists.html

Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360- 1380.

Graves, A., Mohamed, A., & Hinton, G. (2013). Speech recognition with deep recurrent neural networks. Proceedings of the 2013 IEEE International Conference on Acoustics, Speech and Signal Processing, 6645-6649.

Han, X., Wang, L., Farahbakhsh, R., Cuevas, Á., Cuevas, R., Crespi, N., & He, L. (2016). CSD: A multi-user similarity metric for community recommendation in online social networks. Expert Systems with Applications, 53, 14-26.

He, J., Lan, M., Tan, C.-L., Sung, S.-Y., & Low, H.-B. (2004). Initialization of cluster refinement algorithms: A review and comparative study. Proceedings of 2004 IEEE International Joint Conference On Neural Networks.

Hevner, R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Hong, L., & Davison, B. D. (2010). Empirical study of topic modeling in Twitter. Proceedings of the First Workshop on Social Media Analytics, 80- 88.

Hu, D., Zhao, J. L., Hua, Z., & Wong, M. C. (2012). Network-based modeling and analysis of systemic risk in banking systems. MIS Quarterly, 36(4), 1269-1291.

Huang, Z., & Zeng, D. D. (2005). Why does collaborative filtering work? Recommendation model validation and selection by analyzing bipartite random graphs. Presented at the Annual Workshop on Information Technolgies & Systems.

Huang, Z., & Zeng, D. D. (2011). Why does collaborative filtering work? Transaction-based recommendation model validation and selection by analyzing bipartite random graphs. INFORMS Journal on Computing, 23(1), 138- 152.

Järvelin, K., & Kekäläinen, J. (2000). IR evaluation methods for retrieving highly relevant documents. Proceedings of the 23rd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 41-48.

Kamath, K. Y., Popescu, A.-M., & Caverlee, J. (2013). Board recommendation in Pinterest. Presented at UMAP Workshops.

Kim, D., Jo, Y., Moon, I. C., & Oh, A. (2010). Analysis of Twitter lists as a potential source for discovering latent characteristics of users. Proceedings of the 2010 ACM CHI Workshop on Microblogging.

Kitchens, B., Dobolyi, D., Li, J., & Abbasi, A. (2018). Advanced Customer Analytics: Strategic Value Through Integration of Relationship-Oriented Big Data. Journal of Management Information Systems, 35(2), 540-574.

Koh, J., Kim, Y.-G., Butler, B., & Bock, G.-W. (2007). Encouraging participation in virtual communities. Communications of the ACM, 50(2), 68-73.

McCollum, A. (2013). Pinterest accidentally built a better search engine than Google. BuzzFeed News. https://www.buzzfeednews.com/article/ ashleym36/pinterest-accidentally-built-abetter-search-engine-that-goo

Moreau, E. (2017). The top social networks people are using today. Lifewire. https://www.lifewire. com/top-social-networking-sites-people-areusing-3486554

Myers, S. A., Sharma, A., Gupta, P., & Lin, J. (2014). Information network or social network? The structure of the Twitter follow graph. Proceedings of the 23rd International Conference on World Wide Web, 493-498.

Newman, M. E. J. (2002). Assortative mixing in networks. Physical Review Letters, 89(20), Article 28701.

Omnicore (2020). Twitter by the numbers (2020): Stats, demographics & fun facts. https://www. omnicoreagency.com/twitter-statistics/

Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). The PageRank citation ranking: Bringing order to the web (Technical report, Stanford Info Labs). http://ilpubs.stanford.edu:8090/422/

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77.

Pochampally, R., & Varma, V. (2011). User context as a source of topic retrieval in Twitter. Proceedings of the ACM Workshop on Enriching Information Retrieval.

Preece, J., & Maloney-Krichmar, D. (2005). Online communities: Design, theory, and practice. Journal of Computer-Mediated Communication, 10(4), Article JCMC10410.

Provost, F., & Fawcett, T. (2013). Data science and its relationship to big data and data-driven decision making. Big Data, 1(1), 51-59.

Rakesh, V., Singh, D., Vinzamuri, B., & Reddy, C. K. (2014). Personalized Recommendation of Twitter Lists Using Content and Network Information. Proceedings of the Eighth AAAI Conference on Weblogs and Social Media, 416- 425.

Ransbotham, S., Kane, G. C., & Lurie, N. H. (2012). Network characteristics and the value of collaborative user-generated content. Marketing Science, 31(3), 387-405.

Ray, S., Kim, S. S., & Morris, J. G. (2014). The central role of engagement in online communities. Information Systems Research, 25(3), 528-546.

Ronen, I., Guy, I., Kravi, E., & Barnea, M. (2014). Recommending social media content to community owners. Proceedings of the 37th International ACM SIGIR Conference on Research & Development in Information Retrieval, 243-252.

Rothaermel, F. T., & Sugiyama, S. (2001). Virtual internet communities and commercial success: Individual and community-level theory grounded in the atypical case of TimeZone. com. Journal of Management, 27(3), 297-312.

Rui, H., & Whinston, A. (2012). Information or attention? An empirical study of user contribution on Twitter. Information Systems and E-Business Management, 10, 309-324.

Sharma, N. K., Ghosh, S., Benevenuto, F., Ganguly, N., & Gummadi, K. (2012). Inferring who-is-who in the Twitter social network. Proceedings of the 2012 ACM Workshop on Workshop on Online Social Networks, 55-60.

Shmueli, G. (2010). To explain or to predict? Statistical Science, 25(3), 289-310.

Shmueli, G., & Koppius, O. R. (2011). Predictive analytics in information systems research. MIS Quarterly, 35(3), 553-572.

Štrumbelj, E., & Kononenko, I. (2014). Explaining prediction models and individual predictions

with feature contributions. Knowledge and Information Systems, 41(3), 647-665.

Sun, Y., Han, J., Yan, X., Yu, P. S., & Wu, T. (2011). PathSim: Meta path-based top-k similarity search in heterogeneous information networks. Proceedings of the VLDB Endowment, 4(11), 992-1003.

Sundararajan, A. (2016). The sharing economy: The end of employment and the rise of crowd-based capitalism. MIT Press.

Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., Erhan, D., Vanhoucke, V., & Rabinovich, A. (2015). Going deeper with convolutions. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition.

Tufekci, Z. (2019). How recommendation algorithms run the world. Wired. https://www.wired.com/story/ howrecommendation-algorithms-run-theworld/?fbclid=IwAR0GsjiWGdq-RaPPy5rQd8 \_RbI0Z5b8KCo6nXjtHjKaVfS4TgoV8LArVA

Velichety, S., & Ram, S. (2013). A Cross-Sectional and Temporal Analysis of Information Consumption on Twitter, Proceedings of the 34th International Conference on Information Systems.

Velichety, S., Ram, S., & Bockstedt, J. (2019). Quality Assessment of Peer-Produced Content in Knowledge Repositories using Development and Coordination Activities. Journal of Management Information Systems, 36(2), 478- 512.

Wang, J., Zhao, Z., Zhou, J., Wang, H., Cui, B., & Qi, G. (2012). Recommending Flickr groups with social topic model. Information Retrieval, 15(3- 4), 278-295.

Watts, D. J, & Strogatz, S. H. (1998a). Collective dynamics of “small-world” networks. Nature, 393(6684), 440-442.

Watts, D., & Strogatz, S. (1998b). The small world problem. Collective Dynamics of Small-World Networks, 393, 440-442.

Xiao, L., Min, Z., Yongfeng, Z., Zhaoquan, G., Yiqun, L., & Shaoping, M. (2017). Fairness-aware group recommendation with pareto-efficiency. Proceedings of the 11th ACM Conference on Recommender Systems, 107-115.

Yamaguchi, Y., Amagasa, T., & Kitagawa, H. (2011). Tag-based User Topic Discovery using Twitter Lists. Proceedings of the 2011 IEEE

International Conference on Advances in Social Network Analysis and Mining, 13-20.

Yang, X., Li, Y., & Luo, J. (2015). Pinterest board recommendation for Twitter users. Proceedings of the 23rd ACM International Conference on Multimedia, 963-966.

Yin, H., Wang, Q., Zheng, K., Li, Z., Yang, J., & Zhou, X. (2019). Social influence-based group representation learning for group recommendation. Proceedings of the 2019 IEEE 35th International Conference on Data Engineering, 566-577.

Zeng, X., & Wei, L. (2013). Social ties and user content generation: Evidence from Flickr. Information Systems Research, 24(1), 71-87.

Zhang, K., Bhattacharyya, S., & Ram, S. (2016). Large-Scale Network Analysis for Online Social Brand Advertising. MIS Quarterly, 40(4), 849-868.

Zhao, J., & Ram, S. (2011). Examining the evolution of networks based on lists in Twitter. 2011 Proceedings of the IEEE 5th International Conference on Internet Multimedia Systems Architecture and Application.

Zhao, K., Zhang, B., & Bai, X. (2018). Estimating Contextual Motivating Factors in Virtual Interorganizational Communities of Practice: Peer Effects and Organizational Influences. Information Systems Research, 29(4), 910-927.

## Appendix A: Determining the Optimal Value for Number of Clusters (k)

For each value of k (ranging from 2 to 10), we first evaluated the quality of the clustering results using evaluation functions proposed in He et al. (2004) that measure the cluster compactness (Cmp), cluster separation (Sep), and combined measure of overall cluster quality (Ocq). The definitions of these functions are given below.

$$
\mathrm{Cmp} = \frac {1}{c} \sum_ {\mathrm{i}} ^ {c} \frac {\mathrm{v} (C _ {\mathrm{i}})}{\mathrm{v} (\mathrm{X})}\tag{12}
$$

where C is the number of clusters generated by dataset X, v(C<sub>i</sub>) is the standard deviation of the cluster Ci and $\mathbf { v } ( \mathbf { \boldsymbol { X } } )$ is the standard deviation of the dataset X. $\begin{array} { r } { \mathrm { v ( X ) } = \sqrt { \frac { 1 } { \mathrm { N } } \sum _ { \mathrm { i = 1 } } ^ { \mathrm { N } } \mathrm { d } ^ { 2 } ( \mathrm { x } _ { \mathrm { i } } , \mu ) } } \end{array}$ where d() is the Euclidean distance between two vectors, N is the number of members in X, and $\mu$ is the mean of X.

$$
\mathrm{Sep} = \frac {1}{c (c - 1)} \sum_ {i = 1} ^ {c} \sum_ {j = 1} ^ {c} \sum_ {j \neq i} \exp \left(- \frac {d ^ {2} (x _ {c _ {i}} , x _ {c _ {j}})}{2 \sigma^ {2}}\right)\tag{13}
$$

where C is the number of clusters, σ is the standard deviation of the dataset X, $\boldsymbol { x } _ { c _ { i } }$ is the centroid of cluster $\mathrm { c _ { i } }$ , and $d \Big ( \boldsymbol { x } _ { c _ { i } } , \boldsymbol { x } _ { c _ { j } } \Big )$ is the distance between the centroids of $\mathrm { c _ { i } }$ and ${ \mathrm { c } } _ { \mathrm { j } } .$

To calculate the overall quality of clusters obtained, we give equal importance to both Compactness (Cmp) and Separation (Sep) and calculate a measure of overall quality as follows:

$$
\mathrm{Ocq} = 0. 5 * \mathrm{Cmp} + 0. 5 * \mathrm{Sep}\tag{14}
$$

The lower the value of Ocq, the better the quality of clusters.

## Appendix B: Machine Learning Model Interpretability Metrics

![](/api/attachments/Z7FT5HDV/fulltext/images/4396a1c36f2efb2520ca20569bd0e56d4759aa10670bf557ed568c7bd299bcd5.jpg)  
Figure B1. Feature Importance<sup>2</sup> with Network and General Features

![](/api/attachments/Z7FT5HDV/fulltext/images/8dbed01601b27a2720b36afa22cd9e69fae063582583444151ab73617f54daba.jpg)  
Figure B2. Feature Importance<sup>2</sup> with Content Features

![](/api/attachments/Z7FT5HDV/fulltext/images/74a666934bc6551f92cb32e935289efa398e7df07da5074f179ae37c58a8c39d.jpg)  
Figure B3. Shapley Values with Network and General Features

![](/api/attachments/Z7FT5HDV/fulltext/images/3860bfd8dba4679387b2604f2a2580b8f71b710598fa5893ac4c058104705669.jpg)  
Figure B4. Shapley Values with Textual Features

## About the Authors

Srikar Velichety is an assistant professor of business information and technology at the Fogelman College of Business and Economics at the University of Memphis. Velichety received his PhD in management information systems from the Eller College of Management, University of Arizona in 2016. His research interests are in big data analytics, social media and social networks, explainable AI, user-generated content, recommender systems, and predictive analytics. His research has been published in major outlets including Journal of Management Information Systems, Journal of the Association for Information Systems, and Data Base for Advances in Information Systems.

Sudha Ram is Anheuser-Busch Chair in MIS, Entrepreneurship, and Innovation and professor of management information systems in the Eller College of Management, University of Arizona. Ram got her PhD from the University of Illinois Urbana-Champaign in 1985. Her research interests are in explainable artificial intelligence, business intelligence and web analytics, social media analytics, enterprise data management, data provenance, and interoperability. She has raised more than 20 million USD worth of grants from several federal agencies including NSF, NIH, GSA, and organizations including IBM, Parkland Center for Clinical Innovation, and the I3FOR Institute. Her research has been published in several top outlets including Management Science, Marketing Science, Management Information Systems Quarterly, Information Systems Research, Journal of Management Information Systems, and Journal of the Association for Information Systems.
