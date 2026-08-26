---
otero_id: 16162
otero_key: "B88A9SDB"
title: "A Friend Like Me: Modeling Network Formation in a Location-Based Social Network"
authors: "Gene Moo Lee; Liangfei Qiu; Andrew B. Whinston"
year: "2016"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2016.1267523"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Friend Like Me: Modeling Network Formation in a Location-Based Social Network

Gene Moo Lee, Liangfei Qiu & Andrew B. Whinston

To cite this article: Gene Moo Lee, Liangfei Qiu & Andrew B. Whinston (2016) A Friend Like Me: Modeling Network Formation in a Location-Based Social Network, Journal of Management Information Systems, 33:4, 1008-1033, DOI: 10.1080/07421222.2016.1267523

To link to this article: http://dx.doi.org/10.1080/07421222.2016.1267523

![](/api/attachments/B88A9SDB/fulltext/images/b7934046d74c272287dad9e9621ced3856cbda7614fe5857527b2fcab86e4606.jpg)

View supplementary material

![](/api/attachments/B88A9SDB/fulltext/images/7f382ca3b8f10eb1b585a82b78d3a094e63a888973c5d9fb877bcfd14428f0ea.jpg)

Published online: 10 Feb 2017.

![](/api/attachments/B88A9SDB/fulltext/images/da7584ee768b394c94a529f1c885eebdd5051273dbabc0d74aa178acdc2b0943.jpg)

Submit your article to this journal

![](/api/attachments/B88A9SDB/fulltext/images/0c90f2ecbd0ceb21bab3dfe78f0aa20c6f9f242491d614f77fce6646e2727a16.jpg)

Article views: 8

![](/api/attachments/B88A9SDB/fulltext/images/b2859303b5fc8dc13197bc34ce682c0d5e1598ce0472fdba5b8b598dd78f3e39.jpg)

View related articles

![](/api/attachments/B88A9SDB/fulltext/images/90fae89eabd4a9adf8556217366135b2dfb54480ff5a442d32e9e96e1aeee115.jpg)

View Crossmark data

# A Friend Like Me: Modeling Network Formation in a Location-Based Social Network

GENE MOO LEE, LIANGFEI QIU, AND ANDREW B. WHINSTON

GENE MOO LEE (gene.lee@uta.edu; corresponding author) is an assistant professor in the Department of Information Systems and Operations Management at the University of Texas at Arlington. He received his Ph.D. in computer science from the University of Texas at Austin. His research interests are in Big Data Analytics with applications on mobile ecosystems, social network analysis, and cybersecurity. His work has appeared in MIS Quarterly and Journal of Cybersecurity and in various conference proceedings. He has extensive industry experience at Samsung, AT&T, Intel, and Goldman Sachs. He holds 10 patents in mobile technology.

LIANGFEI QIU (liangfeiqiu@ufl.edu) is an assistant professor in the Department of Information Systems and Operations Management at the Warrington College of Business, University of Florida. He received his Ph.D. in economics from the University of Texas at Austin. His research focuses on economics of information systems, prediction markets, social media, and telecommunications policy. His research has appeared in Decision Support Systems, Information Systems Research, Journal of Management Information Systems, and MIS Quarterly.

ANDREW B. WHINSTON (abw@uts.cc.utexas.edu) is the Hugh Cullen Chair Professor in the Information, Risk, and Operation Management Department at the McCombs School of Business at the University of Texas at Austin. He is also director of the Center for Research in Electronic Commerce. His recent work has appeared in Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Management Science, Marketing Science, Journal of Marketing, and Journal of Economic Theory. He has published over 300 papers in the major economic and management journals and has coauthored 27 books. His Erdös number is 2.

ABSTRACT: This article studies the strategic network formation in a location-based social network. We build an empirical model of social link creation that incorporates individual characteristics and pairwise user similarities. Specifically, we define four user proximity measures from biography, geography, mobility, and short messages. To construct proximity from unstructured text information, we build topic models using Latent Dirichlet Allocation. Using Gowalla data with 385,306 users, 3 million locations, and 35 million check-in records, we empirically estimate the model to find evidence on the homophily effect on network formation. To cope with possible endogeneity issues, we use exogenous weather shocks as our instrumental variables and find the empirical results are robust: network formation decisions are significantly affected by our proximity measures.

KEY WORDS AND PHRASES: homophily, location-based service, network formation, social networks, topic modeling, user proximity.

Social networks have long been regarded as a driving force in shaping individual behavior. A large body of literature explored the role of social networks in product adoption [5, 35], peer-to-peer (P2P) lending [30], financial markets [14], technology usage [53], prediction markets [38, 39]), music and video consumption [6, 17, 50], and online dating [7]. In most of the previous literature, social networks are treated as exogenously given and remain fixed for the duration of the studies. However, this assumption ignores the effects of the dynamic nature of network formation in real-world social networks [20]. Therefore, it is critical to understand the determinants of network formation.

In the study, we examine the main determinants of network formation in a location-based social network. Recently, various mobile devices (e.g., smartphones, smart watches, activity trackers) offer geographic localization capabilities via GPS and Wi-Fi technologies [19]. This enabled location-based social networks, where users can share their location information with their friends [25, 41] via check-in activities. People can check in at restaurants using a mobile website, text messaging, or a device-specific application in order to have their check-ins posted on their social network accounts (e.g., Foursquare, Facebook Place, or Google+). In this study, we focus on estimating an empirical model for network formation based on individual choices motivated by utility maximization.<sup>1</sup> This approach is on the basis of game-theoretic models of network formation, also known as strategic network formation models [13, 21, 22, 44], actor-based models [48], or utilitybased link formation [28] in the literature. In our empirical model, we assume that a pair of users forms a link if both individuals view the link as beneficial and that the social network is the equilibrium outcome of strategic interactions among users.<sup>2</sup> Essentially, the process of our network formation is a stable matching [42].

In the computer science and statistical physics literature, network formation has been studied as a link prediction problem rather than statistical inference. Pioneer work from Liben-Nowell and Kleinberg [29] explored various pairwise node proximity measures constructed from graph structures to predict future links in online social networks. For link prediction in a location-based social network, Scellato et al. [43] used co-check-in records to extract common interests of two users, and Allamanis et al. [2] incorporated the geographic distance between users. Our work takes one step forward to use a machine learning approach to build user proximity from users’ unstructured text information.

The contribution of this study is threefold: we build an empirical model for strategic network formation, introduce various user similarity measures to support the model, and empirically estimate the statistical significance of the introduced variables. As a result, we find evidence on homophily effect in friendship creation of location-based social networks.

First, from the modeling perspective, we propose a model of strategic network formation in location-based social networks. Compared with other empirical approaches of network formation, such as exponential random graph models [18], our empirical model has several advantages. (1) Strategic network formation has solid microfoundations: the links are the results of individual choices, and the rule for forming a link requires that both potential partners derive positive net utility from the link. The utility function for each user is defined by individual characteristics as well as dyadic user similarity measures. Therefore, an empirical model based on strategic network formation is more useful for policy evaluation and counterfactual analysis [44], which we demonstrate in this study. The estimated parameters of our strategic network formation model are consistent by using the method of maximum likelihood estimation. In contrast, some other empirical approaches of network formation do not consider the underlying economic incentives. Thus it is not clear why the parameters of these models should remain the same in new settings with a different number of nodes, or a different distribution of characteristics [13]. (2) The estimation using other approaches may not be computationally feasible or consistent even in a network with hundreds of nodes [11]. In the case of an exponential random graph model, the estimation requires exhaustive enumeration of all possible graphs given a set of nodes.

The second contribution is to build four dyadic user similarity measures to capture various aspects of location-based social networks: unstructured biography texts, geographic location, common check-in activities, and short messages (i.e., tweets). We leverage a machine learning technique called topic modeling to extract latent topics from unstructured text data.

The first similarity measure is based on user biography texts. Many social networks allow users to describe their interests in plain sentences. The issue is how we incorporate the unstructured text information and produce similarity metrics between users. Our novel approach is to apply Latent Dirichlet Allocation [10] topic modeling to the text corpus of user biography texts. With a topic model, each user can be presented as a topic vector, where each topic is an automatically generated user feature dimension that can be easily understood. Then pairwise user similarity is constructed with the cosine similarity between topic vectors. Joseph et al. [23] constructed topic models of Foursquare check-in data to identify different user groups such as tourists and local communities. Wu [54] computed the diversity of information content using the dissimilarities of the topics. Singh et al. [47] analyzed the key words that occur in blog articles using a topic-modeling approach.

The next user proximity measure is based on geographic location of users to capture the unique feature of location-based social networks. Specifically, we calculate pairwise user distances based on the coordinates of the users’ home cities. Many studies of social networks have found the evidence of correlation between geographic distance and the likelihood of friendship creation [2, 9]. Pool et al. [37] constructed a distance measure using residential addresses to proxy for social interaction among fund managers. Zheng et al. [55] used GPS trajectory data to get user similarities to better recommend friends and places.

Besides the home locations, the check-in records are used to construct our third proximity measure. The locations at which a user checks in implicitly indicate the user’s taste [52]. And the commonality of check-in points of a pair of users can be a good predictor of link formation [43]. Actually, this way of measuring common activities between users is the basis for collaborative filtering-based recommender systems [31]. We use a simple normalized check-in intersection measure to identify users with similar tastes.

Our last user proximity metrics are based on tweets, which are short messages users generate to express themselves. Recent studies show that researchers can extract useful information from the content of tweets [36]. The hypothesis is that if a pair of users “say” similar words and post about the same topics, they are likely to be actual friends. We operationalize the tweet-based proximity by following the same approach used in biography-based metric.

The third contribution of the study is to empirically estimate the model using a large data sample of a location-based social network: Gowalla. The data include more than 35 million check-in activities of 385,306 users at 3 million different locations worldwide. The empirical analyses show statistical significance of proposed similarity measures to the network formation. This is reminiscent of the importance of homophily [4, 16]: people with similar backgrounds are more likely to form links with each other. Our empirical estimation goes beyond location-based service and applies to other settings of social network formation. For example, ResearchGate, a social network for scientists and researchers, can use topic modeling to process titles and abstracts of research papers, and can recommend new possible coauthorship links based on our empirical estimation [12, 51]. In the context of online dating, biographic information can be used in estimating a similar network formation model. The present study is potentially useful for practitioners in understanding how to predict and affect network formation. The business value of information technology has been documented in the literature [8, 33]. Our research highlights the role of a tight integration of topic modeling and location-based technology in providing friend recommendation.

## Empirical Model for Link Formation

In this section, we present an empirical model for strategic network formation. Users are linked to each other according to a location-based social network. The undirected social graph $\Gamma = \left( N , L \right)$ is given by a finite set of nodes $N = \{ 1 , 2 , . . . , n \}$ and a set of links $L \subseteq N \times N$ . Each node represents a user using location-based services. The social connections between the users are described by an $n \times n$ dimensional matrix denoted by $g \in \{ 0 , 1 \} ^ { n \times n }$ such that:

$$
g _ {i j} = \left\{ \begin{array}{l l} 1, & \text { if } (i, j) \in L \\ 0, & \text { otherwise } \end{array} \right..
$$

In other words, $g _ { i j } = 1$ if and only if users i and j are friends; otherwise, $g _ { i j } = 0$ . Let $N _ { i } ( g ) = \left\{ j \in N : g _ { i j } = 1 \right\}$ represent the set of friends of user .

Given the current state of the location-based social network Γ, the utility of user  is:

$$
U _ {i} = \sum_ {j = 1} ^ {n} g _ {i j} u _ {i j},\tag{1}
$$

where $u _ { i j }$ is the utility user i obtained if a link between users i and j is formed. The utility $u _ { i j }$ is given by a linear functional form:

$$
u _ {i j} = \alpha_ {0} + \alpha_ {1} ^ {\prime} X _ {i} + \alpha_ {2} ^ {\prime} S _ {i j} + \varepsilon_ {i j},\tag{2}
$$

where $X _ { i }$ represents individual characteristics of user (e.g., home city), and $\varepsilon _ { i j }$ is individual taste heterogeneity when users i and j form a link, and is independent across all pairs $( i , j )$ . We assume that $\varepsilon _ { i j }$ follows a type I extreme value distribution. Each user can observe his or her own taste heterogeneity $\varepsilon _ { i j } ,$ but the researcher cannot. The vector $S _ { i j }$ captures the similarity between users i and $j ,$ and it is symmetric—that is, $S _ { i j } = S _ { j i }$ . The parameter $\alpha _ { 2 }$ measures the effect of homophily: the tendency of individuals to associate with others who are similar [4, 16]. In our context, the quantifiable similarity measures include the geographical distance between individuals’ hometowns, the user biography similarity constructed by topic models, the user preference similarity exploited from the users’ check-in information, and the tweet-based proximity. It is worth noting that although users’ check-in information could be a good predictor for network formation,<sup>3</sup> constructing similarity measures using check-in data should be done with care. The endogeneity concern arises when the current state of social network structures can also affect users’ check-in behavior. In other words, a user is more likely to check in at the restaurants her friends have visited before because of observational learning [41]. We will describe how to construct this measure in detail, together with other similarity measures below.

For notation simplicity, we denote $U _ { i } = U _ { i } \big ( g _ { i j } , g _ { - i j } , X _ { i } , \varepsilon _ { i } \big )$ , where $g _ { - i j }$ is the network by removing link ij. The individual heterogeneity $\varepsilon _ { i } = ( \varepsilon _ { i 1 } , \varepsilon _ { i 2 } , \ldots , \varepsilon _ { i , i - 1 } , \varepsilon _ { i , i + 1 } , \ldots , \varepsilon _ { i n } )$ The marginal utility of user of forming a link with user j is given by:

$$
\Delta U _ {i j} = U _ {i} \left(g _ {i j} = 1, g _ {- i j}, X _ {i}, \varepsilon_ {i}\right) - U _ {i} \left(g _ {i j} = 0, g _ {- i j}, X _ {i}, \varepsilon_ {i}\right) = u _ {i j}.\tag{3}
$$

Following the literature on strategic network formation [22, 44], the decision of forming a link in a location-based social network is based on the marginal utility derived from the link. Users and j will form a link if both of them obtain positive utility from the link: $\Delta \mathrm { U _ { i j } } \ge 0 ,$ , and $\Delta \mathrm { U _ { j i } } \ge 0$ . This equilibrium concept comes from pairwise stability [22]. Note that the concept of pairwise stability is different from a Nash equilibrium. Even if $\Delta \mathrm { U _ { i j } } \geq 0 _ { \mathrm { : } }$ , and $\Delta \mathrm { U _ { j i } } \ge 0$ , a user could choose not to form a link in a Nash equilibrium. The reason is that rejection is always a weakly dominant strategy given the partner chooses not to form a link. In the present study, we focus on the case that the individual utility obtained from forming a link is not transferable. In other words, the link formation rule requires the agreement of both users. Christakis et al. [13] discussed the transferable case that allows for cooperative behavior through the possibility of transfers. More specifically, in order to form a link, a user can use his or her surplus to compensate his or her partner for the loss.<sup>4</sup> It is also worth noting that Comola and Fafchamps [15] pointed out a potential issue in many empirical studies relying on self-reported survey questions to elicit social networks: when two individuals are asked about the friendship link between them, their responses might be discordant, that is, person A cites person B but B does not cite A. It is not clear whether the underlying link formation process is bilateral or unilateral. In contrast, an advantage of our location-based social network data is that it does not suffer from a lack of clarity on link formation rule: a bilateral network formation process generates links.

Combining Equations (2) and (3), we obtain:

$$
\Delta U _ {i j} = u _ {i j} = \alpha_ {0} + \alpha_ {1} ^ {\prime} X _ {i} + \alpha_ {2} ^ {\prime} S _ {i j} + \varepsilon_ {i j}.\tag{4}
$$

Because $\varepsilon _ { i j }$ follows a type I extreme value distribution,

$$
\ln \frac {\operatorname* {P r} \left(\Delta U _ {i j} \geq 0\right)}{1 - \operatorname* {P r} \left(\Delta U _ {i j} \geq 0\right)} = \alpha_ {0} + \alpha_ {1} ^ {\prime} X _ {i} + \alpha_ {2} ^ {\prime} S _ {i j}.
$$

Therefore,

$$
\operatorname * {P r} \left(\Delta U _ {i j} \geq 0\right) = \frac {\exp \left[ \alpha_ {0} + \alpha_ {1} ^ {\prime} X _ {i} + \alpha_ {2} ^ {\prime} S _ {i j} \right]}{1 + \exp \left[ \alpha_ {0} + \alpha_ {1} ^ {\prime} X _ {i} + \alpha_ {2} ^ {\prime} S _ {i j} \right]}.
$$

The probability of forming a link between users i and j is given by:

$$
\begin{array}{c} \operatorname * {P r} \bigl (\Delta U _ {i j} \geq 0 \bigr) \cdot \operatorname * {P r} \bigl (\Delta U _ {j i} \geq 0 \bigr) = \frac {\exp \bigl [ a _ {0} + a _ {1} ^ {\prime} X _ {i} + a _ {2} ^ {\prime} S _ {i j} \bigr ]}{1 + \exp \bigl [ a _ {0} + a _ {1} ^ {\prime} X _ {i} + a _ {2} ^ {\prime} S _ {i j} \bigr ]} \\ \cdot \frac {\exp \bigl [ a _ {0} + a _ {1} ^ {\prime} X _ {j} + a _ {2} ^ {\prime} S _ {i j} \bigr ]}{1 + \exp \bigl [ a _ {0} + a _ {1} ^ {\prime} X _ {j} + a _ {2} ^ {\prime} S _ {i j} \bigr ]}. \end{array}
$$

We construct the log likelihood function to estimate the empirical model for strategic network formation:

$$
\begin{array}{l} \ln L (\theta) = \ln \prod_ {i = 1} ^ {n - 1} \prod_ {j = i + 1} ^ {n} \left[ \operatorname * {P r} \bigl (\Delta U _ {i j} \geq 0 \bigr) \cdot \operatorname * {P r} \bigl (\Delta U _ {j i} \geq 0 \bigr) \right] ^ {g _ {i j}} \\ \quad \cdot \left[ 1 - \operatorname * {P r} \bigl (\Delta U _ {i j} \geq 0 \bigr) \cdot \operatorname * {P r} \bigl (\Delta U _ {j i} \geq 0 \bigr) \right] ^ {1 - g _ {i j}}, \end{array}
$$

where $g _ { i j } = 1$ if users i and j are friends; otherwise, $g _ { i j } = 0$ . Our estimates of the parameters are chosen to satisfy:

$$
\hat {\theta} = (\hat {\alpha} _ {0}, \hat {\alpha} _ {1}, \hat {\alpha} _ {2}) = \operatorname{argmax} _ {\alpha_ {0}, \alpha_ {1}, \alpha_ {2}} \ln L (\theta).\tag{5}
$$

To summarize, the parameters to estimate include a vector of coefficients of individual characteristics, $\hat { a } _ { 1 }$ , a vector of coefficients estimating the effects of similarity measures (homophily), $\hat { \boldsymbol { a } } _ { 2 }$ , and a constant term $\hat { \boldsymbol { a } } _ { 0 }$

## User Proximity

In this section, we describe how various user similarity measures in the model are operationalized in the context of location-based social networks. In a social network, the characteristics of a focal user can be captured in various ways. Specifically, four similarity or distance measures are defined with the following user features: biography text, hometown location, check-in spots, and tweets.

First, we introduce a user proximity measure based on topic models of user biography texts, which is one of the novel contributions in the study. We hypothesize that a pair of users with similar biographies is likely to form a link. The challenge is how we quantify the similarity of unstructured texts. Our approach is to use Latent Dirichlet Allocation [10] to construct topic models with users’ biographies as the input corpus. Among various text analysis algorithms, we use a topic modeling approach because it transfers documents into vectors of topics, where each topic is an automatically defined user feature dimension that can be easily interpreted.

Once the topic model is built, each user’s biography text can be transformed to a vector where each entry represents the weight associated to a specific topic. Given two users’ biography texts, a pairwise proximity value can be calculated by cosine similarity of the topic vectors from biographies (bio\_topicsim). Shi et al. [45] used a similar approach to quantify business proximity between firms. The resulting similarity values range from 0 to 1, where larger values indicate that two user have similar biographies. Our expectation is that this similarity has positive impacts on link formation. Lee et al. [24] also adapted a topic-model–based proximity measure to quantify mobile app similarity.

The second covariate takes advantage of geographic location, which is a unique feature of location-based social services. Specifically, we measure the geographical distance in kilometers between two users’ hometowns (home\_distance).<sup>5</sup> We expect this distance to have a negative impact on link formation model, especially in case of intercity relationships. Thus we use this covariate only when the user data is in the state, region, or national level.

Common check-in information is used to construct the third similarity measure. If two users share many check-in spots, the likelihood of link formation is expected to increase for the following two reasons: (1) sharing more spots increases the chance of meeting, and (2) the fact that they share spots means that they share common interests. Some may argue that shared spots are affected by the existing friendships. More specifically, previous friends’ check-ins at a spot, such as a restaurant, may lead to herding/observational learning behaviors of focal users [41, 46]. Thus we try to avoid a potential endogeneity issue by considering only the check-in records that took place before the social graph snapshot time. In addition, we exploit exogenous variations of weather shocks in different cities as instrumental variables (IV) for the number of shared check-ins in the empirical analysis. Given two users’ check-in spots, we calculate the similarity by the ratio between the intersecting spots and the union of two spot sets (co\_checkin). We use the ratio for normalization. The values range from 0 to 1, where 1 indicates that two users checked in at exactly the same spots. A similarity approach is widely used in other social networks with users and items. For example, a co-liked page can be used on Facebook and co-purchased items can be used on Amazon. Note that both bio\_topicsim and co\_checkin reveal the common interests between users. However, bio\_topicsim is a static measure, which is more likely to reflect the time-invariant interest similarity; and co\_checkin is a dynamic measure, which may reflect the change of users’ interests.

The last user similarity is calculated by another source that reveals a user’s interests: tweets. Location-based social networks encourage users to connect their accounts to external social networks like Twitter. Following a similar approach with biography similarity, we first build topic models with tweets, then calculate cosine similarity between two tweet topic vectors (tweet\_topicsim). One thing to note is that all the tweets from one user are combined to form a single document in the topic model.

## Data

Gowalla is the main data source for the empirical analysis of strategic network formation. It was a location-based social network service, launched in 2009 and closed in 2012 after Facebook’s acquisition. With its mobile apps available on major platforms, Gowalla allowed mobile users to “check in” at spots that they visited and to share their check-in activities with friends.<sup>6</sup> Competitive services have included Foursquare, Brightkite, and Loopt (note that Foursquare is the only one still available in the market). Larger social networks such as Facebook and Google+ have also adopted check-in features.

Check-in is an on-demand event created by a user only when he or she likes to share it with others. Thus a check-in reveals a lot about the individual. For example, the category of the location (e.g., restaurant) can be used to infer the user’s taste. Also, the geographic locations of the check-in points show the user’s mobility pattern such as home, workplace, and frequently visited places. Lastly, check-in times may reveal the diurnal and weekly patterns of users.

Gowalla’s social graph is undirected, as each friendship link is formed with mutual agreements. This is different from the case of Twitter, where users can follow others’ tweets even without the opponent’s approvals. Link formation can be affected by individual characteristics, which can be observed by check-in histories and user profiles. Conversely, the social network creates an environment of observational learning: people can explore previously unknown places by observing friends’ check-in activities.

## Data Collection

We used Gowalla’s application program interface (API) to collect data about users, spots, check-ins, and the social graph. First, we collected data of 385,306 users. Each user data includes first and last name, hometown (city, state, and country), text biography, website, Facebook identifier, Twitter identifier, friends count, and various activity counts. Note that there are missing values because the user gives the data voluntarily. For users without explicit home information, we approximate the hometown by the location with the highest check-in count.

Second, we have a total of 3,101,620 spots in the database. Each record consists of spot identifier, name, category, street address, city, state, country, latitude, and longitude. Again, missing fields do exist but we observed that spots in the United States mostly have complete information. Thus we focus on U.S.-based users and locations in the analysis.

To our surprise, we were able to collect the whole trajectory of check-ins in Gowalla. The very first check-in was by Gowalla’s cofounder on January 21, 2009, at his house and the last event took place in Bangkok, Thailand, on January 1, 2012. We collected 35,691,059 check-in records that created a three-year time span.<sup>7</sup> Each check-in entry indicates user identifier, spot identifier, spot name, latitude, longitude, and check-in time stamp. On average, each user checked in 92 times and each spot was visited more than 11 times.

Third, the social network, which is the dependent variable in our empirical analysis, consists of 63,982 user nodes and 95,974 friendship edges. The snapshot was taken over the course of May 2011.<sup>8</sup> The graph has a density of 0.0047 percent, in that as there are more than 2 billion possible pairs.

In addition to the Gowalla data, we collected tweets from Gowalla users to obtain richer text information. A total of 100,946 Gowalla users linked their accounts to Twitter to share their check-ins as tweets. At the time of Twitter data collection, 79,979 of them were still available.<sup>9</sup> We collected 200 recent tweets from each user. After filtering out non-English tweets, tweets from 58,436 users are used in the analysis. The time windows of tweets and Gowalla’s check-ins do not exactly match, thus we do not make causal claims about tweet-related variables.

## Topic Models and User Proximity

We calculate four proximity measures based on the definitions in the User Proximity section. First, for biography topic similarity, we construct topic models with 22,139 users’ biography texts as the input document collection. We vary the number of topics (10, 20, 30, 50, 100, 200) to find that the 100-topic model yields the best topics. Note that we did not remove the stop words from the raw corpus to avoid bias issues. In the online Appendix, Table 1A gives a partial list of the resulting 100 topics along with the related keyword in each topic.<sup>10</sup> Then the geographic distance (home\_distance) between users’ hometowns coordinates ranges from 0.0 km but does not have the upper bounds. Large values observed are farther than 3,000 km. For co-check-in similarity (co\_checkin) measure, we consider only check-in records before 2011 because the social graph snapshot was taken in May 2011. This is to avoid potential reverse causality issues where check-ins are influenced by friendship. Lastly, in the online Appendix, Table 2A shows a partial list of topics and keywords from Gowalla users’ recent tweets.<sup>11</sup>

To illustrate the relationship between our proposed topic-based user similarities and friendship, we present two pairs of users who are friends and share similar topics in terms of biography and tweets, as listed in Figure 1. As in the first example, user #143496 and user #8122 are friends who show high similarity values in both topic models (60 percent in biography and 42 percent in tweets). The specific topics that

Table 1. Summary Statistics of City-Level Samples

<table><tr><td>Variables</td><td>Austin, TX</td><td>San Francisco, CA</td><td>New York, NY</td></tr><tr><td colspan="4">Nodal variables</td></tr><tr><td># of users</td><td>336</td><td>129</td><td>146</td></tr><tr><td># of spots</td><td>27,271</td><td>21,007</td><td>20,320</td></tr><tr><td># of check-ins</td><td>110,880</td><td>50,267</td><td>44,218</td></tr><tr><td># of spots per user</td><td>185.5 (std = 524.7)</td><td>260.3 (std = 916.7)</td><td>198.8 (std = 882.8)</td></tr><tr><td># of check-ins per user</td><td>330.0 (std = 780.8)</td><td>389.6 (std = 1306.6)</td><td>302.8 (std = 1118.5)</td></tr><tr><td colspan="4">Dyadic variables</td></tr><tr><td># of user pairs</td><td>49,770</td><td>6,670</td><td>8,128</td></tr><tr><td># of friendships</td><td>251</td><td>21</td><td>52</td></tr><tr><td>friend (0 or 1)</td><td>0.005 (std = 0.70)</td><td>0.003 (std = 0.05)</td><td>0.006 (std = 0.07)</td></tr><tr><td>co_checkin [0~1]</td><td>0.061 (std = 0.10)</td><td>0.035 (std = 0.69)</td><td>0.029 (std = 0.07)</td></tr><tr><td>bio_topicsim [0~1]</td><td>0.034 (std = 0.12)</td><td>0.032 (std = 0.11)</td><td>0.031 (std = 0.11)</td></tr><tr><td>home_distance (km)</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>tweet_topicsim [0~1]</td><td>0.42 (std = 0.23)</td><td>0.36 (std = 0.24)</td><td>0.31 (std = 0.22)</td></tr></table>

Table 2. Summary Statistics of State-Level Samples

<table><tr><td>Variables</td><td>Illinois</td><td>Georgia</td><td>California (50%)</td><td>Texas (50%)</td></tr><tr><td colspan="5">Nodal variables</td></tr><tr><td># of users</td><td>118</td><td>98</td><td>286</td><td>399</td></tr><tr><td># of spots</td><td>12,079</td><td>18,666</td><td>41,121</td><td>52,931</td></tr><tr><td># of check-ins</td><td>28,266</td><td>41,003</td><td>106,581</td><td>158,623</td></tr><tr><td># of spots per user</td><td>124.2 (std = 221.9)</td><td>239.3 (std = 1108)</td><td>204.6 (std = 650.2)</td><td>226.4 (std = 901.8)</td></tr><tr><td># of check-ins per user</td><td>239.5 (std = 439.0)</td><td>418.3 (std = 1,603)</td><td>372.6 (std = 1,076)</td><td>397.5 (std = 1,247)</td></tr><tr><td colspan="5">Dyadic variables</td></tr><tr><td># of user pairs</td><td>5,995</td><td>6,670</td><td>33,670</td><td>70,876</td></tr><tr><td># of friendships</td><td>12</td><td>26</td><td>30</td><td>130</td></tr><tr><td>friend (0 or 1)</td><td>0.002 (std = 0.04)</td><td>0.006 (std = 0.08)</td><td>0.0008 (std = 0.02)</td><td>0.001 (std = 0.04)</td></tr><tr><td>co_checkin [0~1]</td><td>0.015 (std = 0.04)</td><td>0.023 (std = 0.06)</td><td>0.010 (std = 0.04)</td><td>0.022 (std = 0.07)</td></tr><tr><td>bio_topicsim [0~1]</td><td>0.035 (std = 0.12)</td><td>0.036 (std = 0.12)</td><td>0.030 (std = 0.10)</td><td>0.032 (std = 0.11)</td></tr><tr><td>home_distance (km)</td><td>788.8 (std = 1,612)</td><td>625.6 (std = 864.8)</td><td>1,143 (std = 1,863)</td><td>838.6 (std = 1,602)</td></tr><tr><td>tweet_topicsim [0~1]</td><td>0.38 (std = 0.26)</td><td>N/A</td><td>0.32 (std = 0.22)</td><td>0.38 (std = 0.23)</td></tr></table>

![](/api/attachments/B88A9SDB/fulltext/images/50ef63abd91daf3b38a0fc15daf2cca2992c7fb37c913f89afb20282d1078e6d.jpg)  
Figure 1. Examples of Friends with Similar Topics in Biography and Tweets

contribute to the high similarity values are topic #187 (open, source, advocate, software) for biography and topic #17 (code, web, javascript) and topic #45 (right, did, pretty, better) in tweets. One can expect this friendship to be related to web development and open software. The second pair of user #39875 and user #5279 has 42 percent similarity in biography and 62 percent in tweets. Sharing topics are topic #177 (manager, community, founder, group, CEO, startup) in biography and topic #2 (win, enter, free, giveaway) and topic #91 (Twitter, news, journalism, story).

## User Sampling

User data are sampled in the link formation analysis to achieve computational feasibility.<sup>12</sup> In the analysis, we need to consider all possible user pairs, comparing to the realized friendship. The number of pairs is quadratic to the number of users, meaning that more than 74 billion pairs need to be analyzed if we consider all the users in the analysis. Leskovec and Faloutsos [27] showed that simple, uniform random node selection works well in graph sampling, and we follow this direction in user sampling.

We construct the sample data in city, state, region, and national levels. For the city-level data (Austin, Texas; New York, New York; San Francisco, California), we actually include all the users without sampling. In the state-level analysis, we use the whole user samples for the states of Georgia and Illinois. Fifty percent sampling is used for the states of California and Texas. User samples in regional divisions are constructed by combining multiple states according to the definition from the United States Census Bureau.<sup>13</sup> For regions 1 (Northeast) and 2 (Midwest), the sampling rate is 50 percent, whereas the number is 20 percent for regions 3 (South) and 4 (West), due to large population in the data. Lastly, 10 percent sampling is used to construct U.S. national level data.

Table 1 shows the summary statistics on three city-level samples from Austin, San Francisco, and New York. As Gowalla was founded at Austin, we observe very active data from the area. A total of 336 users have created 110,880 check-in records in 27,271 unique locations in the pre-2011 data set. On average, each user visited 185 unique places and checked in 330 times, but, as seen by the large standard deviation, there is a significant variation among users. Among the dyadic variables, the values of co\_checkin, bio\_topicsim, and tweet\_topicsim range from 0 to 1, where 0 indicates no commonality and 1 complete overlap. Note that the number of observations of tweet\_topicsim is smaller than the other three dyadic variables because not all Gowalla users shared their Twitter accounts. We do not report home distances for the city-level samples because all users reported their home to be the focal city. As the dependent variable, there are 251 friend relationships formed among the 336 users. We observe comparable sample sizes from the cities of San Francisco and New York, except for the smaller number of friendships.

Table 2 reports the description on four state-level samples: Illinois, Georgia, California, and Texas. For computational feasibility, we have 50 percent random samples for California and Texas. The summary statistics of the region-level samples are given in Table 3 and those of U.S. national-level samples are shown in Table 4. Note that statistics on the home distance variable are reported in the state, region, and national samples. As expected, the mean home distance from the nation-level samples is the longest, followed by the region samples, then the state samples.

## Empirical Results

## Main Results

In this section, we present the empirical results estimated from our empirical model of strategic network formation. Tables 5–8 show the main estimation results. As we introduced in the previous section, 10 percent sampling is used to construct U.S. national-level data in column 1 of Table 5. It is worth noting that the number of observations in our empirical model is the number of all possible pairs in a given location-based network. We find that the effect of bio topic similarity, bio\_topicsim, on network formation is significant and positive. This result confirms homophily in location-based social networks: People with similar topic vectors from biographies are more likely to form links with each other. In the estimation, we use the robust z-statistics to deal with the concerns about the failure to meet standard econometrics assumptions, such as unknown heteroskedasticity and possible correlations in error terms. Column 1 of Table 5 also shows that the geographical distance between two users’ hometowns, home\_distance, has a negative impact on link formation. This result implies that physical distance matters in the case of intercity relationships and is consistent with the results shown in the prior literature: Allamanis et al. [2] showed that the geographic distance is critical in predicting online social network formation. Lastly, we find that the similarity measure based on co-check-in activities, co\_checkin, has a positive impact on network formation. The interpretation of this result is that users who share similar location histories are likely to have common interests and behavior, and therefore are more likely to become friends. In our case, the similarity between users’ interests and behavior can be inferred from their check-in location

Table 3. Summary Statistics of Region-Level Samples

<table><tr><td>Variables</td><td>Region 1 (50%)</td><td>Region 2 (50%)</td><td>Region 3 (20%)</td><td>Region 4 (20%)</td></tr><tr><td colspan="5">Nodal variables</td></tr><tr><td># of users</td><td>230</td><td>291</td><td>323</td><td>238</td></tr><tr><td># of spots</td><td>35,149</td><td>26,263</td><td>46,621</td><td>31,674</td></tr><tr><td># of check-ins</td><td>73,569</td><td>68,487</td><td>102,953</td><td>74,628</td></tr><tr><td># of spots per user</td><td>183.5 (std = 821.8)</td><td>112.0 (std = 232.5)</td><td>184.0 (std = 601.5)</td><td>168.6 (std = 539.6)</td></tr><tr><td># of check-ins per user</td><td>319.8 (std = 1,265)</td><td>235.3 (std = 504.5)</td><td>318.7 (std = 792.0)</td><td>313.5 (std = 885.1)</td></tr><tr><td colspan="5">Dyadic variables</td></tr><tr><td># of user pairs</td><td>21,945</td><td>36,315</td><td>45,150</td><td>23,220</td></tr><tr><td># of friendships</td><td>38</td><td>24</td><td>21</td><td>30</td></tr><tr><td>friend (0 or 1)</td><td>0.001 (std = 0.04)</td><td>0.0006 (std = 0.02)</td><td>0.0004 (std = 0.02)</td><td>0.001 (std = 0.03)</td></tr><tr><td>co_checkin [0~1]</td><td>0.008 (std = 0.04)</td><td>0.004 (std = 0.02)</td><td>0.007 (std = 0.03)</td><td>0.006 (std = 0.03)</td></tr><tr><td>bio_topicsim [0~1]</td><td>0.031 (std = 0.11)</td><td>0.031 (std = 0.11)</td><td>0.030 (std = 0.11)</td><td>0.029 (std = 0.10)</td></tr><tr><td>home_distance (km)</td><td>888.9 (std = 1,236)</td><td>1,055 (std = 1,427)</td><td>1,438 (std = 1,507)</td><td>1,789 (std = 2,007)</td></tr><tr><td>tweet_topicsim [0~1]</td><td>0.34 (std = 0.23)</td><td>0.35 (std = 0.23)</td><td>0.37 (std = 0.23)</td><td>0.37 (std = 0.22)</td></tr></table>

Table 4. Summary Statistics of U.S. Samples

<table><tr><td>Variables</td><td>U.S. Sample 1(10%)</td><td>U.S. Sample 2(10%)</td><td>U.S. Sample 3(10%)</td></tr><tr><td colspan="4">Nodal variables</td></tr><tr><td># of users</td><td>381</td><td>412</td><td>393</td></tr><tr><td># of spots</td><td>53,919</td><td>51,177</td><td>50,412</td></tr><tr><td># of check-ins</td><td>117,757</td><td>123,523</td><td>106,937</td></tr><tr><td># of spots per user</td><td>163.1 (std = 628.5)</td><td>154.7 (std = 527.4)</td><td>146.6 (std = 452.2)</td></tr><tr><td># of check-ins per user</td><td>309.0 (std = 926.1)</td><td>299.8 (std = 1107.8)</td><td>272.1 (std = 781.2)</td></tr><tr><td colspan="4">Dyadic variables</td></tr><tr><td># of user pairs</td><td>62,128</td><td>71,253</td><td>66,430</td></tr><tr><td># of friendships</td><td>97</td><td>80</td><td>28</td></tr><tr><td>friend (0 or 1)</td><td>0.001 (std = 0.03)</td><td>0.001 (std = 0.03)</td><td>0.0004 (std = 0.02)</td></tr><tr><td>co_checkin [0~1]</td><td>0.003 (std = 0.02)</td><td>0.004 (std = 0.26)</td><td>0.002 (std = 0.01)</td></tr><tr><td>bio_topic_sim [0~1]</td><td>0.028 (std = 0.10)</td><td>0.029 (std = 0.10)</td><td>0.029 (std = 0.10)</td></tr><tr><td>home_distance (km)</td><td>1,979 (std = 1,381.1)</td><td>2,113 (std = 1,600.1)</td><td>2,049 (std = 1,676.4)</td></tr><tr><td>tweet_topicsim [0~1]</td><td>0.36 (std = 0.22)</td><td>0.39 (std = 0.23)</td><td>0.39 (std = 0.24)</td></tr></table>

Table 5. Estimated Parameters of the Model of Strategic Network Formation

<table><tr><td>Variables</td><td>(1)Baseline model: U.S. Users 10% Sample 1</td><td>(2)New York, NY</td><td>(3)San Francisco, CA</td><td>(4)Austin, TX</td><td>(5)Illinois</td><td>(6)Georgia</td></tr><tr><td>co_checkin</td><td>3.861***[4.791]</td><td>1.421***[2.993]</td><td>3.124***[4.747]</td><td>2.543***[23.79]</td><td>4.359***[3.644]</td><td>3.360***[5.444]</td></tr><tr><td>bio_topicsim</td><td>1.353***[3.035]</td><td>1.351***[2.643]</td><td>1.773***[2.774]</td><td>0.479*[1.728]</td><td>2.101***[2.606]</td><td>2.108***[3.760]</td></tr><tr><td>home_distance</td><td>-0.000138***[-3.787]</td><td></td><td></td><td></td><td>-5.87e-05*[-1.737]</td><td>-3.27e-05[-0.214]</td></tr><tr><td>region2</td><td>-1.926***[-6.483]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>region3</td><td>-1.694***[-8.338]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>region4</td><td>-0.854***[-4.351]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Constant</td><td>-1.848***[-12.86]</td><td>-2.540***[-31.74]</td><td>-3.089***[-23.05]</td><td>-2.844***[-77.69]</td><td>-3.263***[-18.48]</td><td>-2.663***[-17.44]</td></tr><tr><td>Observations</td><td>62,128</td><td>8,128</td><td>6,670</td><td>49,770</td><td>5,995</td><td>3,828</td></tr><tr><td colspan="7">Notes: Robust z-statistics in brackets, ***p&lt;0.01; **p&lt;0.05; *p&lt;0.1.</td></tr></table>

Table 6. Instrumental Variable Estimation of Strategic Network Formation

<table><tr><td>Variables</td><td>(1)U.S. users 10% Sample 1</td><td>(2)U.S. users 10% Sample 2</td><td>(3)California 50% Sample</td><td>(4)Texas 50% Sample</td><td>(5)Illinois</td><td>(6)Georgia</td></tr><tr><td>co_checkin</td><td>3.034***[3.025]</td><td>3.346***[7.427]</td><td>3.145***[5.338]</td><td>2.434***[12.52]</td><td>4.134***[3.354]</td><td>3.042***[3.872]</td></tr><tr><td>bio_topicsim</td><td>1.156***[2.774]</td><td>0.752**[1.992]</td><td>1.425***[2.746]</td><td>0.793**[2.031]</td><td>2.045***[2.542]</td><td>1.842***[3.227]</td></tr><tr><td>home_distance</td><td>-0.000124***[-3.045]</td><td>-0.000118***[-2.532]</td><td>-0.000152*[-1.763]</td><td>-7.58e-05**[-2.024]</td><td>-5.61e-05*[-1.722]</td><td>-2.34e-05[-0.118]</td></tr><tr><td>region2</td><td>-1.745***[-5.324]</td><td>-0.422[-1.354]</td><td></td><td></td><td></td><td></td></tr><tr><td>region3</td><td>-1.424***[-6.327]</td><td>-0.212[-1.043]</td><td></td><td></td><td></td><td></td></tr><tr><td>region4</td><td>-0.535***[-3.279]</td><td>0.551**[2.132]</td><td></td><td></td><td></td><td></td></tr><tr><td>Constant</td><td>-1.545***[-10.32]</td><td>-2.458***[-11.24]</td><td>-3.204***[-25.33]</td><td>-2.745***[-40.23]</td><td>-3.054***[-16.39]</td><td>-2.238***[-12.86]</td></tr><tr><td>Observations</td><td>62,128</td><td>71,253</td><td>33,670</td><td>70,876</td><td>5,995</td><td>3,828</td></tr><tr><td colspan="7">Notes: Robust z-statistics in brackets, ***p&lt;0.01; **p&lt;0.05; *p&lt;0.1.</td></tr></table>

Table 7. Robustness Checks of the Empirical Estimation: National and State Levels

<table><tr><td>Variables</td><td>(1)U.S. users 10%Sample 2</td><td>(2)U.S. users 10%Sample 3</td><td>(3)California 50%Sample</td><td>(4)Texas 50%Sample</td></tr><tr><td>co_checkin</td><td>4.959***[9.679]</td><td>5.357***[4.706]</td><td>3.707***[7.502]</td><td>3.106***[22.02]</td></tr><tr><td>bio_topicsim</td><td>0.828**[1.987]</td><td>1.685***[2.777]</td><td>1.723***[3.016]</td><td>0.793*[1.841]</td></tr><tr><td>home_distance</td><td>-0.000103***[-2.705]</td><td>-0.000129[-0.833]</td><td>-0.000187*[-1.767]</td><td>-9.32e-05**[-2.059]</td></tr><tr><td>region2</td><td>-0.612[-1.562]</td><td>0.171[0.291]</td><td></td><td></td></tr><tr><td>region3</td><td>-0.320[-1.108]</td><td>0.634[1.231]</td><td></td><td></td></tr><tr><td>region4</td><td>0.670***[2.661]</td><td>0.0217[0.0363]</td><td></td><td></td></tr><tr><td>Constant</td><td>-3.326***[-13.08]</td><td>-4.139***[-6.957]</td><td>-3.518***[-28.45]</td><td>-3.266***[-60.53]</td></tr><tr><td>Observations</td><td>71,253</td><td>66,430</td><td>33,670</td><td>70,876</td></tr><tr><td colspan="5">Notes: Robust z-statistics in brackets, ***p&lt;0.01; **p&lt;0.05; *p&lt;0.1.</td></tr></table>

Table 8. Robustness Checks of the Empirical Estimation: Regional Level

<table><tr><td>Variables</td><td>(1)Region 1(Northeast) 50%Sample</td><td>(2)Region 2(Midwest) 50%Sample</td><td>(3)Region 3(South) 20%Sample</td><td>(4)Region 4(West) 20%Sample</td></tr><tr><td>co_checkin</td><td>2.017***[4.227]</td><td>4.393***[5.229]</td><td>2.912***[7.917]</td><td>5.571***[6.077]</td></tr><tr><td>bio_topicsim</td><td>1.538***[3.244]</td><td>1.349**[2.042]</td><td>1.484**[2.333]</td><td>1.324**[2.173]</td></tr><tr><td>home_distance</td><td>0.000143***[3.521]</td><td>-0.00112[-1.468]</td><td>-1.85e-05[-0.202]</td><td>-1.80e-05[-0.453]</td></tr><tr><td>Constant</td><td>-3.384***[-30.29]</td><td>-3.191***[-10.08]</td><td>-3.893***[-24.52]</td><td>-3.440***[-29.20]</td></tr><tr><td>Observations</td><td>21,945</td><td>36,315</td><td>45,150</td><td>23,220</td></tr><tr><td colspan="5">Notes: Robust z-statistics in brackets, ***p&lt;0.01; **p&lt;0.05; *p&lt;0.1.</td></tr></table>

histories [43]. For instance, people who enjoy the same museum or hiking the same mountain can connect with each other to share their experiences. Oestreicher-Singer and Sundararajan [35] examined the effect of a co-purchase relation on sales in product networks. Our co-check-in similarity measure is conceptually similar to the copurchase relation described in Oestreicher-Singer and Sundararajan [35]. It is worth noting that we cannot completely avoid the endogeneity issue due to a lack of information on the time of each link formation: the link formation between two users could also increase future co-check-in activities. However, because we use only the check-in records that took place far ahead of the time of our social graph snapshot to construct the measure, co\_checkin, the endogeneity problem would be a lesser concern.

In column 1 of Table 5, we also add U.S. regional dummies, which take the value 1 if the hometown of a user is in a corresponding region, and 0 otherwise, as individual characteristics. In the analysis of city-level and state-level samples, columns 2–6 of Table 5 show that our main results are robust.

## Instrumental Variables: Exogenous Weather Shock

In order to further address the concern of the endogeneity of the number of cocheck-ins (co\_checkin), we use an instrumental variable (IV) to correct possible biases in our estimation. Following the prior literature on weather instruments [3, 32, 40], our empirical strategy is to instrument for the number of co-check-ins with exogenous weather shocks.

The intuition is that if the weather in a city is more severe (e.g., heavy rain, heavy snow, etc.), the number of co-check-ins will be less because severe weather can significantly reduce people’s willingness to go out. It is worth noting that, for our IV analysis, we focus on the U.S. level and state-level data, which allows us to exploit the exogenous variation of weather in different cities. For the exogenous weather to be a valid IV for the number of co-check-ins in our model, it has to be (1) correlated with the number of co-check-ins, and (2) uncorrelated with the error term so that the exogenous variation of weather influences network formation only through the number of co-check-ins. Condition (2) is plausible because conditional on the controls included in our empirical model, these weather shocks are orthogonal to the unobserved factors that can potentially affect network formation. In our context, weather is an exogenous source of variation, which can avoid many possible confounds. The exclusion restriction is plausible: the weather shocks should affect our dependent variable, network formation, only indirectly, through the correlation with the number of co-check-ins. Following Angrist and Krueger [3] and Acemoglu et al. [1], we conduct a test on the concern of the exclusion restriction by including the weather shocks in Equation (2), and the coefficient is not statistically significant after controlling for the number of co-check-ins. These results are encouraging and generate no evidence for a direct effect of weather shocks on network formation. The intuition is that assuming the only impact of weather shocks on network formation is through the number of co-check-ins, then the weather shocks should be insignificant in Equation (2), which also includes the number of co-check-ins. It is also well-known that if the correlation specified in condition (1) is weak, IV methods can be ill-behaved and can cause severe inconsistency [49]. To address this concern, we test whether our IVs are weak instruments by calculating the first-stage F-statistics based on the method proposed by Stock et al. [49] later in this section.

Although weather instruments are widely used in the literature [3, 32, 40], constructing an effective weather instrument should be done with care in our context. We obtain the U.S.-city-level weather data from Weather Underground and focus on weather measures, minimum temperature, precipitation, and snowfall to characterize four severe weather events on each day in each city: a cold day, a hot day, a heavy rain day, and a heavy snow day.<sup>14</sup> We define a day to be a cold day or a hot day if the minimum temperature on that day is below 0 ºC (32 ºF) or the maximum temperature on that day is above $3 5  ^ { \mathrm { ~ o } } \mathrm { C } \left( 9 5 ^ { \mathrm { ~ o } } \mathrm { F } \right)$ , and define a day to be a heavy rain day/a heavy snow day if the precipitation rate is greater than 4 mm per hour/4 cm per hour.<sup>15</sup> Because we consider only check-in records before 2011 for co-check-in similarity measure (far ahead of the snapshot of our social network), we construct our weather shock variables using the same time period: we calculate the accumulative number of severe weather days in 2009–2010 and construct four weather instruments based on the number of cold days, the number of hot days, the number of heavy rain days, and the number heavy snow days.

We also test whether our four weather measures are weak instruments by calculating the first-stage F-statistic. A high F-statistic (28.42) suggests that the weather shocks are not weak instruments. The IV estimation results are robust and are presented in Table 6.<sup>16</sup> It confirms that network formation decisions are significantly affected by our proximity measures.

## Robustness Checks

A variety of additional robustness checks on the sample of state, region, and national levels are provided in Tables 7 and 8. Almost all of the results are consistent with our expectation. The only exception is that the coefficient on the geographic measure, home\_distance, in column 1 of Table 8 is positive, implying that the physical distance actually increases the likelihood of link formation in region 1 (Northeast). A possible explanation is that most of the users in this region are from the northeast megalopolis, the most heavily urbanized region of the United States, and population mobility is high within the megalopolis.

In Table 9, we further explore the effect of the tweet-wise similarity measure based on topic models. As described earlier, we extract similarity information from each user’s 200 recent tweets. Table 9 shows that the effect of the tweet-wise similarity measure, tweet\_topicsim, is positive. Two points are worth noting. First, the sample size in Table 9 has been significantly decreased because only one-fifth of Gowalla users linked their accounts to Twitter. Second, because of the restriction of the Twitter API, we can only collect the most recent tweets instead of specifying the time window of tweets. Therefore, the estimation of the effect of the tweet-wise similarity measure might suffer from an endogeneity problem similar to the one we discussed before: network formation between users can affect the content of their future tweets. In this sense, we do not claim that the coefficients on tweet\_topicsim in Table 9 are estimated causal effects. These estimation results in Table 9 just provide an additional robustness check.

Table 9. Estimated Parameters of Strategic Network Formation: Tweet Topic Modeling

<table><tr><td>Variables</td><td>(1)U.S. users 10% Sample</td><td>(2)San Francisco, CA</td><td>(3)Austin, TX</td><td>(4)California 50% Sample</td><td>(5)Texas 50% Sample</td></tr><tr><td>co_checkin</td><td>3.928***[3.325]</td><td>3.375***[3.192]</td><td>3.210***[14.40]</td><td>5.116***[8.256]</td><td>3.262***[12.75]</td></tr><tr><td>bio_topicsim</td><td>2.407***[3.236]</td><td>2.257***[2.915]</td><td>0.775**[2.281]</td><td>2.179***[4.005]</td><td>0.141[0.308]</td></tr><tr><td>home_distance</td><td>-0.000619*[-1.933]</td><td></td><td></td><td>-3.48e-05[-0.326]</td><td>-3.99e-05[-1.226]</td></tr><tr><td>tweet_topicsim</td><td>0.232[0.547]</td><td>1.075**[2.277]</td><td>2.014***[8.378]</td><td>1.017*[1.742]</td><td>0.762***[2.945]</td></tr><tr><td>region2</td><td>-0.416[-0.372]</td><td></td><td></td><td></td><td></td></tr><tr><td>region3</td><td>0.184[0.322]</td><td></td><td></td><td></td><td></td></tr><tr><td>region4</td><td>0.00215[0.00268]</td><td></td><td></td><td></td><td></td></tr><tr><td>Constant</td><td>-3.228***[-4.434]</td><td>-3.689***[-10.74]</td><td>-3.682***[-24.61]</td><td>-3.942***[-11.44]</td><td>-3.036***[-22.58]</td></tr><tr><td>Observations</td><td>15,576</td><td>2,211</td><td>17,205</td><td>11,325</td><td>22,155</td></tr><tr><td colspan="6">Notes: Robust z-statistics in brackets, ***p&lt;0.01; **p&lt;0.05; *p&lt;0.1.</td></tr></table>

Like Christakis et al. [13], we compare the predicted networks with the actual networks to evaluate the goodness of fit. First, we look at the number of links formed by users. In columns 1 and 2 of Table 10, we compare the number of formed links in the actual networks with the predicted number. Note that in our model, the error terms $\varepsilon _ { i j }$ and $\varepsilon _ { j i }$ are drawn from a type I extreme value distribution, so the predicted number of formed links is affected by the randomness of the error terms. In order to compare with the actual networks, we calculate the average predicted number of formed links by drawing the error terms 100 times. The results in Table 10 show that our empirical model can predict accurately the mean number of formed links.

Next, we compare the degree distribution. The results are presented in Table 11. Although the predicted degree distribution is a little less skewed than the actual degree distribution, the prediction works well in general.

A major advantage of the structural approach is that it allows for interesting counterfactual analysis that is simply not possible with reduced-form regressions by recovering fundamental structural parameters [34]. A tight integration of structural modeling and location-based technology allows us to identify the parameters of the underlying individual choice model and conduct counterfactual analysis on the effect of homophily. If homophily is important in network formation, we would like to know what would happen if people do not care about the proximity measures based on biography topics and check-in records (no homophily exists), and evaluate the role of homophily. Column 3 of Table 10 shows the counterfactual number of formed links generated from our empirical model when the coefficients on bio\_topicsim and on co\_checkin are 0. We find that the number of formed links has been

Table 10. Comparison between the Actual Number and Predicted Number of Formed Links

<table><tr><td>Estimation models</td><td>(1)Actual number of formed links</td><td>(2)Average predicted number of formed links</td><td>(3)Counterfactual number (no homophily)</td></tr><tr><td>Column 1 in Table 5</td><td>97</td><td>98.030</td><td>80.766</td></tr><tr><td>Column 1 in Table 7</td><td>80</td><td>78.378</td><td>64.970</td></tr><tr><td>Column 2 in Table 5</td><td>52</td><td>52.019</td><td>43.340</td></tr><tr><td>Column 3 in Table 5</td><td>21</td><td>21.344</td><td>13.030</td></tr></table>

Notes: Column 3 shows the counterfactual number of formed links generated from our empirical model when the coefficients on bio\_topicsim and on co\_checkin are zero.

Table 11. Actual Degree Distribution and Predicted Degree Distribution  
(a) The Social Network Shown in Column 1 of Table 5

<table><tr><td>Degree</td><td>Actual</td><td>Predicted</td></tr><tr><td>0</td><td>280</td><td>219.16</td></tr><tr><td>1</td><td>52</td><td>92.03</td></tr><tr><td>2</td><td>6</td><td>28.12</td></tr><tr><td>3</td><td>6</td><td>9.28</td></tr><tr><td>4</td><td>2</td><td>2.92</td></tr><tr><td>5</td><td>1</td><td>0.89</td></tr><tr><td>6</td><td>1</td><td>0.44</td></tr><tr><td>7</td><td>0</td><td>0.11</td></tr><tr><td>8</td><td>1</td><td>0.04</td></tr><tr><td>9</td><td>0</td><td>0.01</td></tr><tr><td>10</td><td>1</td><td>0</td></tr><tr><td>≥11</td><td>3</td><td>0</td></tr><tr><td>Average degree of users</td><td>0.550</td><td>0.555</td></tr></table>

(b) The Social Network Shown in Column 1 of Table 7

<table><tr><td>Degree</td><td>Actual</td><td>Predicted</td></tr><tr><td>0</td><td>304</td><td>254.51</td></tr><tr><td>1</td><td>54</td><td>93.43</td></tr><tr><td>2</td><td>11</td><td>23.32</td></tr><tr><td>3</td><td>4</td><td>5.26</td></tr><tr><td>4</td><td>1</td><td>1.25</td></tr><tr><td>5</td><td>0</td><td>0.17</td></tr><tr><td>6</td><td>0</td><td>0.04</td></tr><tr><td>7</td><td>2</td><td>0.02</td></tr><tr><td>8</td><td>1</td><td>0</td></tr><tr><td>≥ 9</td><td>1</td><td>0</td></tr><tr><td>Average degree of users</td><td>0.423</td><td>0.429</td></tr></table>

(c) The Social Network Shown in Column 2 of Table 5

<table><tr><td>Degree</td><td>Actual</td><td>Predicted</td></tr><tr><td>0</td><td>95</td><td>56.76</td></tr><tr><td>1</td><td>16</td><td>46.41</td></tr><tr><td>2</td><td>5</td><td>18.32</td></tr><tr><td>3</td><td>4</td><td>5.41</td></tr><tr><td>4</td><td>2</td><td>0.89</td></tr><tr><td>5</td><td>2</td><td>0.2</td></tr><tr><td></td><td></td><td>(continues)</td></tr><tr><td colspan="3">(c) The Social Network Shown in Column 2 of Table 5</td></tr><tr><td>Degree</td><td>Actual</td><td>Predicted</td></tr><tr><td>6</td><td>0</td><td>0.01</td></tr><tr><td>8</td><td>2</td><td>0</td></tr><tr><td>14</td><td>1</td><td>0</td></tr><tr><td>Average degree of users</td><td>0.813</td><td>0.812</td></tr></table>

(d) The Social Network Shown in Column 3 of Table 5

<table><tr><td>Degree</td><td>Actual</td><td>Predicted</td></tr><tr><td>0</td><td>90</td><td>81.07</td></tr><tr><td>1</td><td>19</td><td>28.25</td></tr><tr><td>2</td><td>2</td><td>5.64</td></tr><tr><td>3</td><td>3</td><td>0.89</td></tr><tr><td>4</td><td>1</td><td>0.13</td></tr><tr><td>5</td><td>0</td><td>0.02</td></tr><tr><td>6</td><td>1</td><td>0</td></tr><tr><td>Average degree of users</td><td>0.362</td><td>0.369</td></tr></table>

decreased by about 20 percent if the effect of homophily does not exist. In other words, 20 percent of links are formed because of homophily.

## Conclusion and Managerial Implications

In this article, we studied the strategic network formation in a location-based social network. We built an empirical model for network formation considering individual characteristics and pairwise user similarity. To construct the dyadic user similarity values from unstructured text data, we constructed topic models from two sets of text corpus—biography and tweets—that can reveal the users’ interest. In addition, geography-based proximity measures were used to incorporate the unique nature of a location-based social network. Based on the empirical analysis on Gowalla social network, we found evidence of the homophily effect on network formation.

The processes of network formation and peer influence are interconnected. First, without full understanding of the process of network formation, the observed relationship between network structure and influence could be spurious [6]. Second, the interconnected nature of network formation and peer influence has important managerial implications. If, for example, an individual’s dining decision is significantly influenced by the characteristics and behaviors of his or her friends, then social recommendation based on our model of strategic network formation would have implications on the implementation of restaurants’ seeding strategies.

Our user proximity measures constructed by topic modeling are statistically and economically relevant in friend recommendation in location-based social networks.

Our study is not without limitations. One limitation in our empirical study is that in reality the benefit of forming a link may depend on the presence of other links in the network—that is, the current network structure [13].<sup>17</sup> In our model, the formation of links depends only on individual user characteristics and pairwise user similarity measures. In other words, we assume pairwise independence between network links: the latent utility of forming each pairwise link is separable. Therefore, in our maximum-likelihood estimation, the likelihood of the whole social network is the product of likelihoods from all pairwise links. As a future research direction, we can further examine the role of current network structures on the dynamic formation of links.

Another future research direction is to estimate peer effects and network formation jointly under a unified model. When examining peer effects given an exogenous social network, researchers need to correct for possible endogeneity biases due to friendship selection [4]. Our present model provides a basis for understanding friendship selection, and a natural extension is to study a more complete structural framework of peer effects with endogenous network formation that can correct friendship selection biases.

Acknowledgments: All authors contributed equally to the study. We thank Swati Rallapalli and Yi-Chao Chen for help on Gowalla data collection. We also thank the participants from the Hawaii International Conference on Systems Sciences (HICSS) 2016, Workshop on Information Technologies and Systems (WITS) 2014, and Workshop on Information Systems and Economics (WISE) 2014 for constructive feedback. The authors are grateful to the special issue editors and the two anonymous reviewers for their helpful comments. The authors are responsible for any inaccuracies in the study.

## Supplemental File

Supplemental data for this article can be accessed on the publisher’s website at http://dx.doi.org/10.1080/07421222.2016.1267523

## NOTES

1. We use network formation, link formation, and friendship formation interchangeably.

2. The equilibrium concept we use is pairwise stability [22]. A social network is pairwise stable if no pair of individuals has incentives to form a new link, and no individual has an incentive to sever an existing link.

3. Scellato et al. [43] found that about 30 percent of all new links appear among users that check in at the same places.

4. The recent popularity of social media attracts advertisers to purchase Facebook friends or Twitter followers [26]. In this case, the transferable link formation rule would apply.

5. Great circular distance is calculated given a pair of geographic coordinates.

6. Gowalla used the term “spots” to indicate locations. We use spots, locations, and venues interchangeably.

7. Note that we could only collect public check-ins, not private ones that are protected by users.

8. Instant snapshot was not feasible due to the API limitation.

9. Some Twitter accounts are not available now due to account closure or privacy settings.

10. For the full list of topics and keywords from the user biography, see http://goo.gl/ Qt5YRb.

11. For the full list of topics and keywords from user tweets, see http://goo.gl/hj6Dmk.

12. In case of user sampling, we test five different samples to check consistency.

13. See http://en.wikipedia.org/wiki/List\_of\_regions\_of\_the\_United\_States.

14. See www.wunderground.com/

15. See www.metoffice.gov.uk/media/pdf/4/1/No.\_03\_-\_Water\_in\_the\_Atmosphere.pdf.

16. In Table 6, we select several data samples to report, but the IV estimation results based on other samples are consistent.

17. This type of externality may generate multiple equilibria of network formation [44].

## ORCID

Gene Moo Lee http://orcid.org/0000-0003-0657-6898

Liangfei Qiu http://orcid.org/0000-0002-8771-9389

## REFERENCES

1. Acemoglu, D.; Johnson, S.; and Robinson, J.A. The colonial origins of comparative development: An empirical investigation. American Economic Review, 91, 5 (2001), 1369–1401.

2. Allamanis M.; Scellato S.; and Mascolo C. Evolution of a location-based online social network: Analysis and models. Proceedings of the 2012 ACM Internet Measurement Conference, Boston, MA, 2012, pp. 145–158.

3. Angrist, J.D., and Krueger, A.B. Instrumental variables and the search for identification: From supply and demand to natural experiments. Journal of Economic Perspectives, 15, 4 (2001), 69–85.

4. Aral, S.; Muchnik, L.; and Sundararajan A. Distinguish influence-based contagion from homophily driven diffusion in dynamic networks. Proceedings of the National Academy of Sciences, 106, 51 (2009), 21544–21549.

5. Aral, S., and Walker, D. Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Science, 57, 9 (2011), 1623–1639.

6. Bapna, R., and Umyarov. A. Do Your Online Friends Make You Pay? A Randomized Field Experiment in an Online Music Social Network, Management Science, 61, 8 (2014), 1902–1920.

7. Bapna, R.; Ramaprasad, J.; Shmueli, G.; and Umyarov, A. One-way mirrors in online dating: A randomized field experiment. Management Science, 62, 11 (2016), 3100–3122.

8. Bardhan, I.; Krishnan, V.; and Lin, S. Business value of information technology: Testing the interaction effect of IT and R&D on Tobin’s Q. Information Systems Research, 24, 4 (2013), 1147–1161.

9. Blackstrom, L.; Sun E.; and Marlow C. Find me if you can: Improving geographical prediction with social and spatial proximity. Proceedings of the 19th International Conference on World Wide Web, Raleigh, NC, 2010, pp. 61–70.

10. Blei D.B.; Ng A.Y.; and Jordan M.I. Latent Dirichlet Allocation. Journal of Machine Learning Research, 3 (2003), 993–1022.

11. Chandrasekhar, A. and Jackson, M.O. Tractable and consistent random graph models. Working paper, Stanford University, 2012.

12. Chen, H., and Zhao, J.L. ISTopic: Understanding information systems research through topic models. Proceedings of International Conference on Information Systems, Fort Worth, TX, 2015.

13. Christakis, N.A.; Fowler, J.H.; Imbens, G.W.; and Kalyanaraman, K. An empirical model for strategic network formation. Working paper, National Bureau of Economic Research, 2010

14. Cohen, L.; Frazzini, A.; and Malloy, C. The small world of investing: Board connections and mutual fund returns. Journal of Political Economy, 116, 5 (2008), 951–979.

15. Comola, M., and Fafchamps, M. Testing unilateral and bilateral link formation. Economic Journal, 124, 579 (2014), 954–976.

16. Currarini, S.; Jackson, M.O.; and Pin, P. An economic model of friendship: Homophily, minorities, and segregation. Econometrica, 77, 4 (2009), 1003–1045.

17. Garg, R.; Smith, M.D.; and Telang, R. Measuring information diffusion in an online community. Journal of Management Information Systems, 28, 2 (2011), 11–38.

18. Goldenberg, A.; Zheng, A.X.; Fienberg, S.E.; and Airoldi, E.M. A survey of statistical network models. Foundations and Trends in Machine Learning, 2, 2 (2010), 1–117.

19. Gonzalez M.C.; Hidalgo C.A.; and Barabasi A.L. Understanding individual human mobility patterns. Nature, 453, 7196 (2008), 779–782.

20. Hinz, O.; Skiera, B.; Barrot, C.; and Becker, J.U. Seeding strategies for viral marketing: An empirical comparison. Journal of Marketing, 75, 6 (2011), 55–71.

21. Jackson, M.O., and Rogers, B.W. Meeting strangers and friends of friends: How random are social networks? American Economic Review, 97, 3 (2007), 890–915.

22. Jackson, M.O., and Wolinsky, A. A strategic model of social and economic networks. Journal of Economic Theory, 71, 1 (1996), 44–74.

23. Joseph, K.; Tan C.H.; and Carley K.M. Beyond “local,” “categories” and “friends”: Clustering Foursquare users with latent “topics.” Proceedings of the 2012 ACM Conference on Ubiquitous Computing, Pittsburgh, PA, 2012, pp. 919–926.

24. Lee, G.M.; He, S.; Lee, J.; and Whinston, A.B. Matching mobile applications for cross promotion. Working paper, University of Texas at Austin, 2016.

25. Lee, G.M.; Rallapalli, S.; Dong W.; Chen Y.; Qiu, L.; and Zhang Y. Mobile video delivery via human movement. Proceedings of the IEEE International Conference on Sensing, Communication, and Networking, New Orleans, LA, 2013, pp. 415–423.

26. Lee, S.; Qiu, L.; and Whinston, A.B. Manipulation: Online platforms’ inescapable fate. Working paper, University of Texas at Austin, 2014.

27. Leskovec, J., and Faloutsos, C. Sampling from large graphs. Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Philadelphia, PA, 2006. pp. 631–636.

28. Li, Z.; Fang, X.; Bai, X.; and Sheng, O.R.L. Utility-based link recommendation for online social networks. Management Science, forthcoming.

29. Liben-Nowell, D., and Kleinberg, J. The link prediction problem for social networks. Journal of the American Society for Information Science and Technology, 58, 7 (2007), 1019–1031.

30. Lin, M.; Prabhala, N.R.; and Viswanathan, S. Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. Management Science, 59, 1 (2013), 17–35.

31. Linden, G.; Smith, B.; and York, J. Amazon.com recommendations: Item-to-item collaborative filtering. IEEE Internet Computing, 7, 1 (2003), 76–80.

32. Miguel, E.; Satyanath, S.; and Sergenti, E. Economic shocks and civil conflict: An instrumental variables approach. Journal of Political Economy, 112, 4 (2004), 725–753.

33. Mithas, S.; Tafti, A.; Bardhan, I.; and Goh, J.M. Information technology and firm profitability: Mechanisms and empirical evidence. MIS Quarterly, 36, 1 (2012), 205–224.

34. Nevo, A., and Whinston, M.D. Taking the dogma out of econometrics: Structural modeling and credible inference. Journal of Economic Perspectives, 24, 2 (2010), 69–82.

35. Oestreicher-Singer, G., and Sundararajan, A. The visible hand? Demand effects of recommendation networks in electronic markets. Management Science, 58, 11 (2012), 1963–1981.

36. Oh, O.; Agrawal, M.; and Rao, R. Community intelligence and social media services: A rumor theoretic analysis of tweets during social crises. MIS Quarterly, 37, 2 (2013), 407–426.

37. Pool, V.K.; Stoffman, N.; and Yonker, S.E. The people in your neighborhood: Social interactions and mutual fund portfolios. Journal of Finance, 70, 6 (2015), 2679–2732.

38. Qiu, L.; Rui, H.; and Whinston, A.B. Effects of social networks on prediction markets: Examination in a controlled experiment. Journal of Management Information Systems, 30, 4 (2014), 235–268.

39. Qiu, L.; Rui, H.; and Whinston, A.B. The impact of social network structures on prediction market accuracy in the presence of insider information. Journal of Management Information Systems, 31, 1 (2014), pp. 145–172.

40. Qiu, L.; Tang, Q.; and Whinston, A.B. Two formulas for success in social media: Learning and network effects. Journal of Management Information Systems, 32, 4 (2015), 78–108.

41. Qiu, L.; Shi, Z.; and Whinston, A.B. Learning from your friends’ repeated check-ins: An empirical study of location-based social networks. Working paper, University of Texas at Austin, 2016.

42. Roth, A.E.; Sönmez, T.; and Ünver, M.U. Efficient kidney exchange: Coincidence of wants in markets with compatibility-based preferences. American Economic Review, 97, 3 (2007), 828–851.

43. Scellato S.; Noulas A.; and Mascolo C. Exploiting place features in link prediction on location-based social networks. Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Diego, CA, 2011, pp. 1046– 1054.

44. Sheng, S. Identification and estimation of network formation games. Working paper, University of Southern California, 2012.

45. Shi Z.; Lee G.M.; and Whinston A.B. Toward a better measure of business proximity: Topic modeling for industry intelligence. MIS Quarterly, 40, 4 (2016), 1035–1056.

46. Shi, Z., and Whinston, A.B. Network structure and observational learning: Evidence from a location-based social network. Journal of Management Information Systems, 30, 2 (2013), 185–212.

47. Singh, P.V.; Sahoo, N.; and Mukhopadhyay, T. How to attract and retain readers in enterprise blogging? Information Systems Research, 25, 1 (2014), 35–52.

48. Snijders, T.A.; Koskinen, J.; and Schweinberger, M. Maximum likelihood estimation for social network dynamics. Annals of Applied Statistics, 4, 2 (2010), 567–588.

49. Stock, J.H.; Wright, J.H.; and Yogo, M. A survey of weak instruments and weak identification in generalized method of moments. Journal of Business and Economic Statistics, 20, 4 (2002), 518–529.

50. Susarla, A.; Oh, J.H.; and Tan, Y. Social networks and the diffusion of user-generated content: Evidence from YouTube. Information Systems Research, 23, 1 (2012), 23–41.

51. Wang, C., and Blei, D.B. Collaborative topic modeling for recommending scientific articles. Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Diego, CA, 2011, pp. 448–456.

52. Wang, L.; Gopal, R.; Sankaranarayanan, R.; and Pancras, J. On the brink: Predicting business failure with mobile location-based checkins. Decision Support Systems, 76 (2015), 3–13.

53. Wattal, S.; Racherla, P.; and Mandviwalla, M. 2010. Network externalities and technology use: A quantitative analysis of intraorganizational blogs. Journal of Management Information Systems, 27, 1 (2010), 145–174.

54. Wu, L. Social network effects on productivity and job security: Evidence from the adoption of a social networking tool. Information Systems Research, 24, 1 (2013), 30–51.

55. Zheng, Y.; Zhang, L.; Ma, Z.; Xie, X.; and Ma, W. Recommending friends and locations based on individual location history. ACM Transactions on Web, 5, 1 (2011), 1–44.
