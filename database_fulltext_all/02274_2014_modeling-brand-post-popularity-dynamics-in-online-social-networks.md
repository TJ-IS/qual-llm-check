---
otero_id: 2274
otero_key: "4ZTSBXXC"
title: "Modeling brand post popularity dynamics in online social networks"
authors: "Amir Hassan Zadeh; Ramesh Sharda"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.05.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Amir Hassan Zadeh ⁎, Ramesh Sharda

Spears School of Business, Oklahoma State University, Stillwater, OK 74078, USA

a r t i c l e i n f o

Available online 13 May 2014

Keywords: Online social networks Social media marketing Crowdsourcing Brand post popularity Brand-generated content Hawkes point process

## a b s t r a c t

Today's social media platforms are excellent vehicles for businesses to build and foster relationship with customers. Companies create of<sup>fi</sup>cial fan pages on social network websites to provide customers with information about their brands, products, promotions, and more. Customers can become fans of these pages, and like, reply, share or mark the brand post as favorite. Marketing departments are using these activities to crowdsource marketing and increase brand awareness and popularity. Understanding how crowdsourcing oriented marketing and promotion evolves would be helpful in managing such campaigns. In this paper, we adopt a multidimensional point process methodology to study crowd engagement activities and interactions. Speci<sup>fi</sup>cally, we investigate the brand post popularity as a joint probability function of time and number of followers. One-dimensional and two-dimensional Hawkes point process models are calibrated to simulate popularity growth patterns of brand post contents on Twitter. Our results suggest that the two-dimensional point process model provides a good model for understanding such crowdsourcing behavior.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

The emergence of Internet-based social media has started a new kind of conversation among consumers and companies, challenging traditional ideas about marketing and brand management while creating new opportunities for organizations to understand customers and connect with them instantly [56]. Research <sup>fi</sup>rm Chadwick Martin Bailey in partnership with Constant Contact conducted a study that analyzed the behavior of 1491 consumers ages 18 and older throughout the U.S., and revealed that a whopping 77% of consumers interact with brands on Twitter or Facebook primarily through reading posts and updates from the brands. They also noted that 60% of social customers are more likely to recommend a brand to a friend after following the brand on Twitter or Facebook, and 50% of them are more likely to buy from that brand as well. When it comes to “Liking” brand posts on Facebook, the reasons are varied, but for the most part, respondents said they like a brand on Facebook because they are a customer (58%) or because they want to receive discounts and promotions (57%) [21].

Today, the customer experience shared through social media, blogs and discussion forums is becoming a major driver of purchasing decisions, because these platforms provide consumers a more in<sup>fl</sup>uential voice in effecting changes in their own customer care [15]. Barnes research [9] indicates that 70% of consumers use social media platforms “at least some of the time” to learn about the customer care offered by a company before they make a purchase. Furthermore, of them, 74% of customers choose companies based on customer care experience shared by others in online forums.

Over the past few years, big brands have started taking social media seriously, and social media marketing has been an inevitable part of their marketing plan. For example, Coca-Cola, one of the world's most recognizable brands, had 800 fans on Facebook in 2007, 16.5 million in 2010, and it has currently crossed over 62.3 million “likes”. In 2012, in honor of the Coca-Cola Facebook page becoming the <sup>fi</sup>rst retailer brand to receive 50 million “likes”, Coca-Cola developed a new Facebook application to identify and support individuals developing, in<sup>fl</sup>uencing and shaping ideas and ask them to collaborate with the Facebook community to spread them globally. Through this application, Coca-Cola teaches the world to sing in perfect harmony, mobilizes millions of people behind their favorite cause, and encourage them to become more active and socially involved. As an end result, consumers become involved in suggesting modi<sup>fi</sup>cations of products and services and the distribution of these innovations [11,12].

Starbucks, as one of the top ten most followed brands on Twitter, uses tweets to share knowledge with customers and promote their latest products, campaigns and events [20]. With an average of ten tweets per day on Twitter, Starbucks extracts relevant knowledge from a network of current and prospective customers around the globe who express their expectations, likes and dislikes about the brand [20,48].

In 2010, Delta Airlines launched the <sup>fi</sup>rst social media “ticket window” on Facebook which allows customers to book a <sup>fl</sup>ight without having to go to any other website. Delta pointed out Facebook is being used by more customers while in <sup>fl</sup>ight than any other Web site, making it a “natural launching point” for its initiative [8]. Access to OSNs on mobile devices has certainly accelerated the popularity of OSNs.

As more and more major brands have established their communities and fan pages within online social networks (OSNs) and started offering commerce opportunities delivered through social media platforms, crowdsourcing applications have become some of the most engaging tools in digital marketing realm, enabling brands to realize the potential for their fans' input into the product development and the market development processes [36]. Such innovative and creative initiatives enable businesses to improve their products, get brand recommendations, increase brand awareness and popularity, <sup>fi</sup>nd new customers or even excite a speci<sup>fi</sup>c demographic. In many cases where fans within social media are particularly passionate about a brand and its products, there will be a clear desire to become part of the product itself, have input as a group and energize the brand and its product lines [57].

Today's openness and <sup>fl</sup>exibility of OSNs provide brands with a huge opportunity to get in touch with customers, crowdsource marketing tasks and enhance brand awareness. Understanding the structure and behavior of the fans on OSNs is important to the content providers to enable better organization of brand post information, design of effective online communities and for implementing successful marketing campaigns. In examining the online social interaction structures, the formation of relationships and interactions, how information moves on social media platforms, and how users respond to various stimuli like video, contests, or posts are not clearly understood. The answers to these questions will offer a more complete picture of the social dynamics of networking and how individuals manage their virtual relationships and follow their favorites or brand communities, or how they in<sup>fl</sup>uence their friends to become followers as well. In this paper, we model the spread of information across Twitter, the most popular and widely used micro-blogging online social network [37] and analyze the data from a number of brand posts to discover what rules might govern the spread of information online. By understanding these behaviors, companies can become more effective in designing marketing campaigns. Being able to analyze a social network of customers, how customers interact on this type of platforms, and what rhythm and timing of the most engaging postings look like provides brands a competitive advantage through forecasting the spread of brand in<sup>fl</sup>uence, and intervening at times with promotions to foster relationship with customers.

The timing pattern of human communication in online social networks is not random. It has been shown that the communication is explained by emergent statistical laws such as non-trivial correlations and clustering [55]. With the possibility of analyzing the multivariate distribution of the occurrences of activity on OSNs, we can add to our understanding of these interactions.

Standard models assume a Poisson distribution for events occurrence, which is an unrealistic assumption in many social systems. Point process has shown promise for modeling social event patterns where the occurrence of an event increases the likelihood of subsequent events [22]. It is a novel way of modeling and clustering high frequency and irregular data in time. It uses a branching structure that corresponds to background events and offspring events and is able to capture bursts of activity, dynamics and reactions over time.

In this paper, we model the popularity of a brand post or more generally an online content on online social networks. The popularity of an online content is not a well-de<sup>fi</sup>ned, but a highly subjective term [39]. Brand post popularity can be de<sup>fi</sup>ned as a mixture of various factors such as vividness, interactivity, the content of the brand post (information, entertainment), and number of times the brand post is mentioned by fans [25]. We take the position of an individual user's eyes who conjectures the popularity of a brand's tweet from publicly observable data by associating the number of impressions it has received (including total number of retweets, replies, favorites) or the lifespan of threads over its entire timeline. A tweet is considered a popular tweet if it receives a certain amount of retweets, replies, and favorites that are no less than a certain threshold over its lifespan [40,43]. Our goal is to develop a mechanism for capturing the evolution of the online content popularity posted by brands on OSNs. In our approach, a model is speci<sup>fi</sup>ed via the conditional intensity for each event. This provides a powerful and more natural modeling framework for multivariate social network event data. Speci<sup>fi</sup>cally, the current study examines the in<sup>fl</sup>uence of user activities on the timing and frequency of a brand post. The self-exciting Hawkes point process and the ETAS (Epidemic Type Aftershock Sequences) models are used to analyze data on brand posts popularity. Unlike Poisson processes, Self-exciting Hawkes point process and ETAS are classi<sup>fi</sup>ed as counting processes which are basically a continuous-time non-Markov chain due to the dependence on the history of the process (i.e. H ) to the extent to which having states 0, $1 , 2 , \ldots$ . moving from state n to state n + 1, where $n \geq 0 .$ . In case of the content popularity problem, each state indicates total number of users who hit the content by time t, and λ(t) is the transition rate of moving from one state to another state.

The remainder of the paper is organized as follows. The next section starts with a discussion of online social networks (OSNs). We also review literature about stochastic point processes and their many uses. The following section describes how we map the content popularity to the point processes framework. Also, we introduce brand post data collected from Twitter and the assumptions necessary to proceed with analysis. In Section 4, we <sup>fi</sup>t competing models to data and then compare the accuracy and complexity of models in capturing the burst of activity on OSNs. The managerial implications of our <sup>fi</sup>ndings, limitations and possible directions for future work are discussed in Section 5. The <sup>fi</sup>nal section presents a general conclusion of the paper.

## 2. Review of the literature

## 2.1. Online social networks

During the past few years, millions of people have used social media applications (Facebook, Twitter, YouTube, Google+, etc.) as a part of their daily online activities [30]. In 2011, more than half of social media users followed brands on social media sites, and brands are increasingly investing in social media to crowdsource marketing activities, indicated by worldwide marketing spending on social networking sites of about \$4.3 billion [25].

Today companies develop of<sup>fi</sup>cial fan pages and online communities within online social networks to understand customers, connect with them instantly and provide them with information about their brands, products, promotions and more. Meanwhile, brand fans can like, comment and share brand posts. Users of Twitter can retweet, which is much like a Facebook share. Followers retweet the tweets of those they are following to propagate information to other people. People respond to popular users by “replying” and/or “mentioning” [7]. Followers can also mark the content as favorite which is functionally similar to the “like” action on Facebook. The “like” and “retweet” buttons are the easiest ways for Facebook and Twitter users respectively to join in on the brand conversation and give feedback. Comments/ replies on brand posts can be positive, neutral or negative. In most cases, social media users who choose to become fans of a product are those who are particularly passionate about a brand and its products and enjoy having input or being a member of a group of like-minded fans. The brand bene<sup>fi</sup>ts from these fans because they help communicate with a diverse audience of other consumers.

Such individual activities associated with a brand post are visible to network friends and many times in<sup>fl</sup>uence friends to retweet, like, or mention. If a company produces fan page updates that earn high quality scores, they will reap the bene<sup>fi</sup>ts of greater exposure and possibly an increased fan base because other network members will see in their news feed. Jansen et al. [38] discuss OSNs as a form of electronic word of mouth (eWOM) for sharing consumer opinions concerning brands and as a part of an organization's marketing strategy. This openness and <sup>fl</sup>exibility of social media provides businesses a great opportunity to bring together a group of people, or “crowd”, to solve a problem or engage in an activity and achieve powerful social engagement and activation.

In many ways, the interactivity of social media supports “crowdsourcing”. Crowdsourcing is a term coined by journalist Jeff Howe [34] to mean “taking advantage of the talent of the public” [46]. Social media provide platforms for existing and potential customers to engage, learn, and entertain. It enables content marketers to crowdsource their marketing, reaching vast audiences via word of mouth. For example, Starbucks developed the “My Starbucks Idea” campaign, an online customer community, where customers are asked to contribute their views and ideas about the company. It keeps customers in the loop on what business ideas Starbucks is currently implementing on both the brand and product level. Through linking this platform to Facebook, Twitter and other social media websites, customers are able to see what others are suggesting, vote on ideas and check out the results [49].

Internet service providers, content creators, and online marketers would like to be able to predict how many views and actions an individual item might create on a given website [58]. This is true for companies as well who bene<sup>fi</sup>t from aspects of online social networks by utilizing fan pages and web advertising. Leveraging the social networking sites to understand what is most popular helps e-commerce providers decide what content to promote on their website. E-commerce providers can leverage these social signals to ensure the products or services people are talking about appear higher in their product listings.

Over the last few years, much effort has been devoted to exploring the statistical features of content popularity in online social networks (OSNs). Most previous empirical analyses of OSNs have treated such networks as static [29,61]. They analyze the social networks on a single data snapshot [3,28,45]. However, such social network systems are inherently dynamic, characterized by a high burstiness and a strong positive correlation between two users' activities and consist of a set of dyadic, directed, time-stamped, cross-affected and sometimes weighted events. To the best of our knowledge, only a few studies have analyzed popularity growth patterns of content on OSNs using prediction models [16,22,29,44,58]. Crane and Sornette [22] propose contagion models as models of YouTube video viewing dynamics to understand how popularity bursts can be described. They differentiate four classes of popularity dynamics (memoryless, viral, quality and junk) which are all explained by properties of Hawkes point process. Szabo and Huberman [58] <sup>fi</sup>nd a strong linear correlation between early and later times of the content popularity on YouTube and Digg networks. This correlation con<sup>fi</sup>rms that if the content is popular when new, it will continue to be popular as it ages. Another interesting work on social media mining is reported by Chatzopoulou et al. [17]. They <sup>fi</sup>nd a strong correlation between total number of comments (or favorites) and total view count in YouTube. There are relatively few studies in the literature which explore the capability of online social networks to predict real-world outcomes such as the revenue or release time of a product on the market. Sadikov et al. [62], Abel et al. [1] and Rui and Whinston [54] present case studies in which blogosphere content can be used as a predictor of movie and music success. They show that the number of microblog views of content related to the music or movie (such as FB posts, tweets, YouTube videos, etc.) can provide an accurate prediction of the movie's or music's success.

While previous studies build popularity models based on a onedimensional function of time, we suggest that the content popularity can be a joint probability function of time and the number of followers. We focus more on incorporating the number of followers as an in<sup>fl</sup>uential metric into predictive models of the content popularity, explicitly looking at the impact of in<sup>fl</sup>uential users on their followers to persuade them to contribute to brand post popularity. In this paper, we adapt a mathematical framework based on self-exciting point process to study brand post popularity on online social networks. Speci<sup>fi</sup>cally, we calibrate one-dimensional and two-dimensional self-exciting point process models to estimate popularity growth patterns of brand post contents on Twitter.

## 2.2. Stochastic point processes

In this section we present the statistical theory underlying our approach. First, we de<sup>fi</sup>ne the conditional intensity function for a point process. A point process is a stochastic model commonly used to describe the occurrence of discrete events in time and space. It can be viewed in terms of a list of times $t _ { 1 } , t _ { 2 } , . . . , t _ { n }$ at which corresponding events $1 , 2 , \ldots$ n occur [27]. Intuitively, a point process is characterized by its conditional intensity $\lambda ( t )$ , which represents the mean spontaneous rate at which events are expected to occur given the history of the process up to time t [50]. In particular, a version of the conditional intensity may be given by the process

$$
\lambda (t) = \lim _ {\Delta t \rightarrow 0} \frac {E [ N [ t , t + \Delta t ] | H _ {t} ]}{\Delta t}
$$

where $H _ { t }$ denotes the history of events prior to time t, and the expectation represents the number of events $N [ t , t + \Delta t ]$ occurring between time t and $t + \Delta t$ . The Poisson process is a special case of a point process where the interval times between two arrivals are independent, identically distributed exponential random variables. The conditional intensity of a Poisson process is deterministic which means that events are linked causally to the conditional intensity. In other words, a point process is classi<sup>fi</sup>ed as a Poisson process if events occurring at two different times are statistically independent of one another, meaning that an event at time $t _ { 1 }$ neither increases nor decreases the probability of an event occurring at any subsequent time [27]. Since a homogeneous Poisson process indicates complete randomness, it is most commonly used as a suitable benchmark for assessing self-exciting process models.

A point process is called self-excited if any one event increases the likelihood of the future events [32]. A self-exciting or Hawkes point process is a versatile point process which has been extensively studied from a theoretical and practical point of view. It is de<sup>fi</sup>ned by its conditional intensity function

$$
\begin{array}{l} \lambda (t) = \mu + \int_ {- \infty} ^ {t _ {i}} \phi (t - t _ {i}) d Z (u) = \mu + \beta \sum_ {\{t _ {i} <   t \}} \phi (t - t _ {i}) \\ \int_ {0} ^ {\infty} \phi (v) d v = 1, \phi (v) \leq 1, \forall v \geq 0 \end{array}\tag{1}
$$

where $Z$ is the normal counting measure [33]. The rate of events $\lambda ( t )$ is decomposed into the sum of a Poisson background rate which in most applications is assumed to be constant in time [33] and a self-exciting component in which events trigger an increase in the rate of the process. The self-exciting part of the process has two components: β and ϕ. β is a constant which re<sup>fl</sup>ects the magnitude of self-excitation and ϕ is a density function describing the waiting time (lag) distribution between excited and exciting events. A proper skewed distribution in which the overall shape re<sup>fl</sup>ects a long time dependency should be introduced for the triggering density.

In the Hawkes-based analysis, the events can be viewed as the realization of a multivariate point process. That is, every single event is characterized by the occurrence time and the event's type. Notationally, $\{ T _ { i } , Z _ { i } \} _ { i } \in \{ 1 , 2 , . . \}$ are random variables where $T _ { i }$ is the occurrence time of the $i ^ { t h }$ event and $Z _ { i } \in \{ 1 , 2 , . . . , M \}$ indicates the ith event's type [13]. A point process is said to be mutually-exciting if any one event from a speci<sup>fi</sup>c event's type at time $t _ { 1 }$ increases the likelihood of an event in another event's type stream occurring at time $t _ { 2 } .$ Mutuallyexciting Hawkes process is used to capture cross interactions and mutual information between one sequence of events and another. Similar to the self-exciting Hawkes process, a mutually-exciting Hawkes process with n event type(s) is de<sup>fi</sup>ned by its conditional intensity functions

$$
\begin{array}{l} \lambda_ {k} (t) = \mu_ {k} + \sum_ {j = 1} ^ {n} \sum_ {\{t _ {i} <   t \}} \beta_ {i j} \phi_ {i j} (t - t _ {i}) \qquad k = 1, 2,... n \\ \int_ {0} ^ {\infty} \phi_ {i j} (v) d v = 1, \quad \phi_ {i j} (v) \leq 1, \quad \forall v \geq 0 \end{array}\tag{2}
$$

where the rate of event type k, $\lambda _ { k } ( t )$ , is partitioned into the sum of a Poisson background rate and mutual-exciting components in which events trigger an increase in the rate of the process. $\beta _ { i j }$ is a constant which re<sup>fl</sup>ects the strength of self-excitation for $( i = j )$ and the strength of mutual-excitation for $( i \neq j )$ and $\phi _ { i j }$ is a density function describing the triggering distribution between excited event type i and exciting event type j.

Hawkes-based analysis has long been used in seismology to recognize similar clustering patterns in earthquakes occurrence data and to predict subsequent earthquakes, or aftershocks. [2,51,59,60]. It has been applied to many other areas such as <sup>fi</sup>nance [10,13], neurophysiology [19], ecology, social networks [5,27,47] and online social networks [22,41].

Engle and Lunde [26]; Bowsher [13] present a bivariate Hawkes process model to jointly analyze the timing of trades and quote arrivals in stock markets. Chavez-Demoulin et al. [18] and Bacry et al. [6] use Hawkes process structure to estimate value at risk for portfolios of traded assets over a given holding period of time. Dassios and Zhao [24] present dynamic contagion process as a generalization of the Cox process and Hawkes process and use it to model risk process with the arrival of claims.

Mohler et al. [47], Egesdal et al. [63], and Erik et al. [27] use selfexciting point process models to predict violent events and security threats. Erik et al. [27] utilize step functions parameterized by various values, linear functions and non-parametric approaches as nonstationary background rates (μ) of the point process.

Alexey et al. [5] use a self-exciting point process to discover missing data in the series of interaction events between agents in a social network. They apply this model to the Los Angeles gang network to predict af<sup>fi</sup>liation of the unknown offenders.

Recently, this approach has been used to analyze the dynamics of online social networks. Crane and Sornette [22] and Mitchell and Cates [64] analyze a family of self-exciting point processes to model correlated event timing of viewing YouTube videos. They deploy a Pareto distribution (power law) as a distribution of waiting times between cause and action, describing the cascade of in<sup>fl</sup>uences on the online social network. It is shown that a Hawkes process enclosing power law distributions offers many capabilities to calibrate the model to characteristics of the YouTube views. These characteristics are classi<sup>fi</sup>ed by a combination of endogenous/exogenous user interactions and the ability of viewers to in<sup>fl</sup>uence others to respond across the network (critical/subcritical).

Howison et al. [35] deploy a mutually excited Hawkes process to understand the dynamics of the user generated contents over open contribution platforms such as Wikipedia and Linux. They study the in<sup>fl</sup>uence of visible activity of others on the timing and amount of participation in Wikipedia environment. They model the time at which a response to an event occurs as a log-normal distribution. But this analysis has not yet been conducted on social media activities, in particular on Twitter postings and follow-up actions. Also the role of the in<sup>fl</sup>uential users within OSNs has not been yet considered in such predictive models.

In this paper, we provide a more realistic investigation of the bene<sup>fi</sup>ts of stochastic point processes for predicting the brand post popularity on OSNs. To the best of our knowledge, there are relatively few studies in the literature which explore the capability of point processes on online social networks to model dynamics and growth patterns. We use the ETAS model, one of the most widely used point process in the literature, to shed light on how the content popularity on OSNs can be described by a function of time and the number of followers. The number of followers is one of the best metrics to demonstrate the role of the in<sup>fl</sup>uential users within OSNs.

## 3. Problem formulation

Understanding rules governing collective human behavior, especially as they affect social interactions on internet-based social media, is a dif<sup>fi</sup>cult task in the <sup>fi</sup>eld of social media analytics. Our main objective is to analyze how the popularity of individual brand posts evolves when the posts are shared with people on social media outlets. We examine how fans' sequential interactions with network friends contribute to the popularity of a brand post. The majority of brand posts experience few hits and can be well described by a Poisson process. In such a case of little activity, popularity oscillation is quite steady. In contrast, some brand posts experience bursts of activity and word of mouth growth through friend sharing features of OSNs. A standard stochastic process (i.e. Poisson process) fails to address the burst of popularity; since it is based on the assumption of independence about arrivals, which is unrealistic in case of future activities arising from a speci<sup>fi</sup>c tweet/post/etc. Clustering point processes and epidemic type models are a good <sup>fi</sup>t for modeling such phenomena.

In the online social networks analysis, the social activity event data can be viewed as the realization of a multivariate point process. Each event is characterized by its occurrence time (t ), the magnitude of in<sup>fl</sup>uence (number of followers) (m ) with an additional mark attached to it representing the event's type (z ). Retweeting, replying, tagging and marking a brand post as a favorite, etc. are different types of user activities. For the purpose of this paper, we combine these three types of events into one common set of events.

The beauty of major OSN platforms is that they are structurally isomorphic. Their similar features, while labeled with site-speci<sup>fi</sup>c vocabulary, operate in the same way, making studies of their data easier. For the purposes of this paper, we will utilize Twitter notations to explain properties of OSNs.

In order to build our two-dimensional point process, we de<sup>fi</sup>ne $\{ T _ { i } , M _ { i } , Z _ { i } \} _ { i } \in \{ 1 , 2 , . . \}$ as random variables where $T _ { i }$ is the occurrence time, $M _ { i }$ the magnitude of the ith triggering event and $Z _ { i } \in \{ 1 , 2 , . . . \}$ indicates the type of $i ^ { t h }$ event. Any event of a speci<sup>fi</sup>c type at time $t _ { 1 }$ increases the likelihood of an event of any type stream occurring at time $t _ { 2 } .$ Now, we formulate the problem using Hawkes process properties and discuss how those mechanisms work on the time line.

## 3.1. Candidate models

First, we formulate one sequence of events using a self-exciting point process to measure the likelihood that individuals are talking about the brand regardless of the type of events. This model lets us aggregate the popularity content from across Twitter into a single stream of information. It concurrently captures the idea that any given activity on a brand post can causally correspond to a background Poisson process μ (in this case constant) and foreground self-exciting process as follows:

$$
\lambda (t) = \Lambda (t | H _ {t}) = \mu + \sum_ {\{i: t _ {i} <   t \}} \beta \phi (t - t _ {i})\tag{3}
$$

The summation component indicates the in<sup>fl</sup>uence of users' activity on the stream. It describes how past events at times $t _ { i }$ in<sup>fl</sup>uence the current event rate. Parameter $\beta$ indicates the amount of excitation an event contributes to the stream. In behavioral terms, it can be described as the number of potential users in<sup>fl</sup>uenced directly by individuals in the past who retweeted or replied to the brand post tweet at time $t _ { i \cdot }$ As mentioned earlier, function ϕ is a triggering function describing distribution of waiting time between a trigger and the response from users who in<sup>fl</sup>uenced to recommend the brand. Mining of our data on the life cycles of various brand posts in Twitter indicates that unlike

YouTube, a brand's tweet gets most of its hits within the <sup>fi</sup>rst days – even hours – of its life cycle and quickly becomes obsolete. Since most responses occur almost immediately in the Twitter case, we need a distribution that enforces the highest intensity at the most immediate possible time. Furthermore, it should be skewed and long tailed to re<sup>fl</sup>ect a long time dependency and burstiness.

## 3.1.1. Model 1

First, we use an exponential distribution for the response density, giving the conditional intensity

$$
\lambda (t) = \mu + \sum_ {\{i: t _ {i} <   t \}} \beta e ^ {- \alpha (t - t _ {i})}\tag{4}
$$

where $t - t _ { i }$ is the time elapsed since event i, and α re<sup>fl</sup>ects a rate of decay for the triggering density which controls how long selfexcitation takes following a tweet. If α is large, mentioning the brand post by users will last only a short while and a few events (retweet or reply) will be only added above a background rate after the initial brand's tweet over a short period of time. Conversely, if α is small, self-excitation will last for a much longer period of time and then many more events will be added to the background rate.

## 3.1.2. Model 2

There is another characteristic of events in OSNs that should be taken into consideration. We suggest that the amount of users' contributions to future events is not only dependent on the occurrence time, but that the number of followers he/she has is an important factor as well. Therefore, our second model takes into consideration two parameters: the occurrence time and the magnitude of triggering event (number of friends and followers). It means that the event does not scale just with the occurrence time, but also the magnitude of the triggering event as well.

One particular form of a self-exciting point process is the ETAS model (space–time–magnitude Hawkes process), which is widely used to describe spatial–temporal patterns. This model takes more parameters (inputs) into account. We use an early form of this model (i.e. time–magnitude Hawkes process), similar to [50], to quantify the popularity of a brand tweet. This model incorporates magnitudes and occurrence time of triggering events concurrently. The conditional intensity for the ETAS model is given by

$$
\lambda (t) = \Lambda (t | H _ {t}) = \mu + \sum_ {\{i: t _ {i} <   t \}} \phi (t - t _ {i}, m _ {i})\tag{5}
$$

where the history of the process $H _ { t } = \{ ( t _ { i } , m _ { i } ) : t _ { i } < t \}$ also includes magnitudes m , μ is the arrival rate of new users and ϕ is a triggering function. The ETAS uses a combination of the exponential distribution and the Pareto distribution for the triggering density ϕ, giving the conditional intensity

$$
\lambda (t) = \mu + \sum_ {\{i: t _ {i} <   t \}} \phi (t - t _ {i}, m _ {i}) = \mu + \sum_ {\{i: t _ {i} <   t \}} \frac {\beta}{(t - t _ {i} + c) ^ {1 + p}} e ^ {\alpha (m _ {i} - M _ {0})}\tag{6}
$$

where the power law term governs temporal distribution of subsequent triggered events and the exponential term explains the factor by which the user's magnitude $m _ { i }$ in<sup>fl</sup>ates expected number of in<sup>fl</sup>uencers. The term t t denotes the time elapsed since event i. β is the amplitude coef<sup>fi</sup>cient indicating the amount of direct excitations triggered by event i. The exponent $p$ is the decay rate, α is interpreted as the productivity rate to control the number of potential users in<sup>fl</sup>uenced by individuals in the past, and c is the time offset that will be empirically determined from the dataset under consideration. Furthermore, $M _ { 0 }$ is the lowest magnitude (number of followers) that will be substituted from the dataset (rescaled to the appropriate range).

## 3.2. Empirical testing of the models on Twitter datasets

We next apply these models to real data. As mentioned earlier, a basic analysis of our data on the life cycle of various brand posts in Twitter using Topsy API and Twitter search API indicates that the majority of a brand's tweet gets most of its activity within the <sup>fi</sup>rst days – even hours – of its life cycle and hence quickly becomes obsolete. Since we focus on the brand post popularity, we take brand posts that experience bursts of activity and electronic word of mouth growth through the friend sharing features of Twitter. Using Twitter's publicly available API, we crawled Twitter information streams of more than 120 major brands that were among the top 500 most valuable global brands [14]. These brands were among the most followed brands and were actively posting tweets at their fan pages on Twitter. These brands are from different product and service categories including clothing, cosmetics, electronics, accessories, foods, beverages, automotive, credit cards, airlines, etc. Together, these brands published more than 26,500 tweets in a typical period of one week to provide information to their customers and promote their latest products, campaigns and events. We downloaded information of all subsequent activities (retweets, replies, and marks as favorite) on a brand post for all these 26,500 brand post tweets. We observed that the majority of brand posts tweets experience few hits and therefore as mentioned earlier, can be modeled by a Poisson process. However, there are brand posts that became a major topic (“trending” in Twitter parlance), are frequently mentioned by the brand's followers, and experience bursts of activity. For the purpose of this paper, we searched through the downloaded tweets to isolate those tweets that are original tweets from the brands and where the tweets have been mentioned (retweeted, replied, marked as favorite) at least 300 times. A number of 221 such brand post tweets followed by many hits and bursts of activity were identi<sup>fi</sup>ed. At this stage, 125,861 twitter activities including information on original tweets, all subsequent retweets, replies and marked as favorite to the original tweet were processed. The data were divided into individual datasets. Each dataset contains a corpus of an individual brand post tweet, its subsequent activities (retweets, replies, and marks as favorite), along with their timestamps, user ids and number of followers of the user who contributes to the tweet stream. We take into consideration only the timestamp of events and the number of followers, while aggregating the events “retweet”, “reply”, and “mark as favorite” into a single stream of information

We investigated the content of these 221 most popular brand tweets and note that the primary topic was the brand campaigns on Twitter (44%). Some of these campaigns use Twitter to communicate with fans and followers. Several campaigns use Twitter hashtags to deliver rewards and sweepstakes to customers. Other campaigns have interactive competitions to create buzz with fans. The second most engaging brand tweet category is related to the events held by the brands on Twitter (36%) including surveys etc. The rest of the most popular brand tweets were related to the information and entertainment posted by brands on Twitter.

## 3.3. Parameter estimation, goodness-of-fit, and model comparison

Given a brand post data collected from Twitter, we utilize maximum likelihood estimation (MLE) methods to estimate the parameters of candidate self-exciting point process models. While numerical optimization routines such as the quasi-Newton method, the conjugate gradient method, the simplex algorithm of Nelder and Mead and the simulated annealing procedure [23,50,52] are often used to compute maximum log-likelihood estimation of self-exciting point process models, we use the expectation-maximization (EM) algorithm provided by Veen and Schoenberg [59] to estimate parameters. Veen and Schoenberg [59] have demonstrated that the EM algorithm as the estimation method of choice for incomplete data problems is extremely robust and accurate compared to traditional methods. The brand post popularity can be viewed as an incomplete data problem in which the unobservable or latent variables ascertain whether an activity belongs to a background event or whether it is a foreground event and was triggered by a preceding activity.

![](/api/attachments/4ZTSBXXC/fulltext/images/e6dcab83d6c4149b34ef57149f9848e680369a2000a7c929040ed0d31a712571.jpg)  
Fig. 1. The methodology used in predicting the online content popularity on Twitter.

Finally, the reliability of each model is statistically tested using the Kolmogorov–Smirnov (K–S) statistic to assess the extent to which the model <sup>fi</sup>ts the data. This criterion provides useful information of the absolute goodness-of-<sup>fi</sup>t of candidate models. Furthermore, the relative ability of each model to describe the data is measured by computing the Akaike information criteria (AIC) [4]. The Akaike statistic provides germane numerical comparisons of the global <sup>fi</sup>t of competing models. The required package functions in R software are used for <sup>fi</sup>tting both above models to the datasets (Ptproc package [53], Ptprocess [31], ETAS package (Jalilian, [65]), and R code [59]).

![](/api/attachments/4ZTSBXXC/fulltext/images/80c7affa40209f2312fca9971e4172e5555f404053aa8ca4aa8859ddb0b3974c.jpg)  
Fig. 2. Frequency of different types of events.

![](/api/attachments/4ZTSBXXC/fulltext/images/2760b447161bae35d2035b0515721f772d16d123f0fde6fb635799c600bf01c9.jpg)  
Fig. 3. A histogram of the number of events per minute.

Furthermore, we employ autoregressive integrated moving average (ARIMA) models as benchmarks which have been regarded as the closest framework to point processes for event data [23]. We used an R package “Forecast” (Hyndman et al. [66]) to perform the time series analysis. This package allows <sup>fi</sup>tting of time series and linear models. The functions available in this package conduct a search over possible models within the order constraints provided and return the best ARIMA model for a univariate time series according to AIC values. In the next section, we will <sup>fi</sup>rst present our results for one of our crawled datasets to illustrate how our approach works and then we discuss goodness-of-<sup>fi</sup>t of the candidate models by computing their average AIC values across all the datasets that we compiled from Twitter.

In summary, Fig. 1 illustrates the methodology used for modeling the content popularity on Twitter in this paper. At each stage, the inputs, the required R-packages used to produce the results and the output are speci<sup>fi</sup>ed clearly.

![](/api/attachments/4ZTSBXXC/fulltext/images/8da44397b1aeb830e27a9a8e1445ba8e8c9715e241e4dd3c07f26bb32188ae42.jpg)  
Fig. 4. Simulated conditional intensity function for model #1

Table 1  
Speci<sup>fi</sup>cation of the self-exciting Hawkes process model (1) used for simulation.

<table><tr><td>Parameter</td><td>μ</td><td>α</td><td>β</td></tr><tr><td>Value</td><td>0.05673</td><td>12.14027</td><td>2.91944</td></tr></table>

## 4. Results and analysis

In this section, we focus on one particular dataset to demonstrate how models work in practice. We set Δt = 1 min for the bin width in order to control the amount of data through parameter t. From this speci<sup>fi</sup>c dataset there are 751 events spanning 10,080 min (one week). Figs. 2 and 3 provide frequency of different types of hits and a histogram of the frequency of all events per minute respectively. The most events occurring in a single minute is 15 and the mean number of events in a single minute is 0.074. Out of a possible 751 events, 278 events occurred during the <sup>fi</sup>rst two days. Thus, we reason that people respond to a brand post tweet immediately. Therefore, we would expect that the distributions to be selected should impose the largest probability mass at the most immediate possible response time.

Table 1 summarizes the parameter estimates for the <sup>fi</sup>rst candidate model.

The <sup>fi</sup>t for the data with self-exciting point process model is plotted in Fig. 4.

The parameter estimate for β denotes that immediately after an event occurs, the conditional intensity is ampli<sup>fi</sup>ed by about 3 events per minute. The parameter estimate for α indicates an event related to the brand post tweet is talked about for up to 12 min after posting.

Now let us look at the ETAS model that takes into account the occurrence time and the number of followers for every single triggering event. Fig. 5 provides a snapshot of the number of followers for those users who appear to have been in<sup>fl</sup>uenced by the brand post tweet either spontaneously or in response to the certain triggers.

Table 2 summarizes the parameter estimates for the ETAS model. Simulated data with the corresponding ETAS point process model are shown in Fig. 6.

Our hypothesis is that the greater the number of followers per event, the greater the in<sup>fl</sup>uence. Therefore incorporating the number of followers into our predictive model as another dimension presumably provides better results. Fig. 6 reveals that the ETAS model is much more able to capture jumps and leaps of the process compared to our dataset.

Utilizing statistical tests such as the K–S goodness-of-<sup>fi</sup>t test and AIC test allows us to test whether the number of followers impacts the model. Table 3 summarizes the results for a two sample K–S test demonstrating how well both models perform in terms of the original data. It contains the p-values and the values of the K–S test statistic (D) corresponding to each model.

These results support our hypothesis that incorporating the number of followers into the predictive models provides a better simulation for understanding such phenomena.

Since the ETAS model has more parameters in comparison to the self-exciting Hawkes process, AIC values are used to analyze parsimony, complexity and accuracy of the models. The homogeneous Poisson model is also often used as a reference model for comparison of competing point process models. Table 4 summarizes the AIC values for candidate models.

Table 2  
Speci<sup>fi</sup>cation of the self-exciting point process model (2) used for simulation.

<table><tr><td>Parameter</td><td> $\mu$ </td><td> $\beta$ </td><td> $\alpha$ </td><td> $p$ </td><td> $c$ </td><td> $m_0$ </td></tr><tr><td>Value</td><td>0.5886</td><td>0.01376837</td><td>2.1254544</td><td>1.157623</td><td>0.01343711</td><td>0.3</td></tr></table>

The AIC values show that the ETAS model is the one with the minimum AIC value. Therefore, the ETAS model provides a better <sup>fi</sup>t than a homogeneous Poisson model or self-exciting Hawkes process or the benchmark ARIMA time series model.

We next estimate the self-exciting Hawkes process model, ETAS model, the benchmark Poisson process model and the benchmark ARIMA model and compare their goodness-of-<sup>fi</sup>t by computing their average AIC values across all datasets.

According to Table 5, the ETAS model has the lowest average AIC value. The proposed ETAS model outperforms the three benchmarks, which indicates that it can capture the in<sup>fl</sup>uence network better than other models. The benchmark homogeneous Poisson process and the benchmark ARIMA time series model seem to fare much lower than the ETAS and the self-exciting Hawkes process. The Poisson process model fails to capture any exciting effects among user activities to make the prediction. Also, the ARIMA time series model appears to fail to capture the dependency between the current event and the past events on the time line. Recall that, in the online content popularity context where the occurrence of an event increases the likelihood of subsequent events, whether slightly or greatly, it is imperative to account for exciting effects among users' activities.

Our result implies that the impact of the number of followers on brand post popularity is an important issue in OSNs. It is necessary to consider the event occurrence time and the number of followers as two major factors in modeling of online social dynamics.

We found that ETAS model provides much more accuracy to predict popularity of brand posts. It allows us to consider the role of the in<sup>fl</sup>uential users in amplifying the brand post popularity and secondarily proposing the brand to their friends and followers networks. It implies that in<sup>fl</sup>uential users with a high number of followers can have a signi<sup>fi</sup>cant in<sup>fl</sup>uence in spreading the content of the brand post to others.

## 5. Discussion and limitations

We have adapted a powerful approach for modeling the content popularity in OSNs. In contrast to the previous studies that focused on a one-dimensional function of time, the model recommended in this paper allows us to characterize and quantify the content popularity as a joint probability function of time and the number of followers. The self-exciting Hawkes process and ETAS models have been calibrated to simulate popularity growth patterns of brand post contents on Twitter and as expected, the ETAS model outperforms the other models to capture bursts of activity over time.

![](/api/attachments/4ZTSBXXC/fulltext/images/b460b5080210384564b5a394982aec2fc8f3da8fe9307f6d3ca9dac9ac328072.jpg)  
Fig. 5. Number of followers over time.

![](/api/attachments/4ZTSBXXC/fulltext/images/ff53069366dd244bdfff1b84c7dd42dafa09ca305c21200fe82a7a506ba6a8d1.jpg)  
Fig. 6. Simulated conditional intensity function for model #2.

This model can enable brand marketing managers to observe how often their fans respond to their posts within OSNs, and gauge the response for different types of content such as news, contests, applications, video, pictures, product information, brand's history, testimonials, etc. They will also have the ability to see how these brand posts move through the Internet. These predictive models can help companies decide how often and when a new brand post should be posted, and how many times the same piece of content can be shared in order to engage more fans and followers. Certainly there is no magic number for the ideal number of posts within OSNs; it is important for brands to post enough content while refraining from posting too much at the same time. The mathematical con<sup>fi</sup>guration of ETAS model also con<sup>fi</sup>rms that if the time difference between two consecutive events is big enough, most likely the brand post will become obsolete and suggests that it is time to post a new content to keep a connection opened with fans.

As another managerial implication of this study, the mathematical formulation of the ETAS model reveals that the greater the number of followers per event, the greater the in<sup>fl</sup>uence. This means that a high number of followers improve activity in posting tweets and being more often retweeted. It highlights the role of in<sup>fl</sup>uential users who signi<sup>fi</sup>cantly affect the engagement of a brand post, even if they are involved later. Thus, if companies identify and increase the number of in<sup>fl</sup>uential users within their online social networks, they should experience an increase of brand recommendations and awareness. Engaging more users that are in<sup>fl</sup>uential during the early life of the brand post could cause viral effects, which is likely to in<sup>fl</sup>uence potential consumers for a longer period. Many approaches have been proposed to <sup>fi</sup>nd in<sup>fl</sup>uential users within OSNs. The simplest approach is to count the number of followers, but there are other ef<sup>fi</sup>cient techniques based on mining link structure along with the temporal order of information adoption [42].

Table 3  
The K–S goodness-of-<sup>fi</sup>t test output.

<table><tr><td>Self-exciting Hawkes process (Model #1)</td><td>ETAS model (Model #2)</td></tr><tr><td>D = 0.3993, p-value = 0.03135</td><td>D = 0.1223, p-value = 0.02216</td></tr></table>

Table 4  
AIC test results.

<table><tr><td>Time series model (ARIMA (3, 1, 3))</td><td>Homogeneous Poisson model</td><td>Self-exciting Hawkes process (Model #1)</td><td>ETAS model (Model #2)</td></tr><tr><td>9787.670</td><td>5401.592</td><td>4473.017</td><td>4012.011</td></tr></table>

Also, since fans' reactions and response time to different types of the brand post content are dissimilar, it is important for brands to look carefully at the performance of their various brand post contents and see which of them during their lifecycle have similar looking stationary/non-stationary background rates. If they do not follow the same growth pattern, each category needs an individual point process to represent it.

Our work proposes a mechanism for capturing the evolution of the online content popularity posted by brands on Twitter. It facilitates the early prediction of a tweet behavior on Twitter and the simulation of the rhythm and timing of the most engaging postings. Through the simulation and the early prediction of a brand's tweet, brands have a better view of timing promotions to foster relationship with customers.

Our research can be extended to determine a peak release time for products of consumer interest on the market through analyzing aggregative/collective brand posts from OSNs. If brand posts are not propagating further on OSNs, it could indicate that the brand is losing its fans' awareness and popularity, so improvement actions should be taken.

Several limitations of our study deserve mention. First, we assume that all users follow the same response time distribution for their own activities. However, individual activity burst shows a sequence of discrete events. This is unlikely to be a single distribution for the purposes of <sup>fi</sup>tting exponential or Pareto distributions to the long term dependency. Another limitation is that the various types of events are aggregated. Multivariate self and mutual-exciting point process models should be developed to deal with different streams of information and measure cross interactions and mutual information between one sequence of events and another.

Furthermore, even though we chose a small time increment, i.e. Δt = 1 min for the bin width in order to control the amount of data through parameter t, we cannot determine if events occurring in the same minute are correlated with one another. This means that the events recorded on the same minute are assumed to be statistically independent.

While we consider the same importance for fan's response times, we can track down brand's most engaging minutes, hours and days of the week to determine real effective time windows that should be taken into computation in order to provide a better prediction.

In summary, our analysis indicates that a stationary Poisson process for the background rate of spontaneous events is a rather unlikely assumption in many social systems. The ETAS model and self-exciting point process can be considered a more reliable underlying process.

## 6. Conclusion and directions for future research

This paper adopts a stochastic point process framework for analysis of the dynamic microstructure of online social networks (OSNs). Especially, we investigate the possibility of using crowdsourcing on OSNs as a marketing mechanism to enhance brand awareness and popularity. Such crowdsourcing activities help brands spur innovation and drive brand awareness across OSNs platforms. We describe such dynamics in terms of the stochastic occurrence times and number of followers. One-dimensional and two-dimensional self-exciting point process models are adjusted to simulate popularity growth patterns of brand post contents on Twitter. Our <sup>fi</sup>ndings indicate that point models are able to describe the cascade of in<sup>fl</sup>uencers on the online social networks. Our results suggest that incorporating the number of followers into predictive models as another dimension of input provides a better understanding of the content popularity. Our future work focuses on applying a full package of multivariate point processes to different streams of events within OSNs.

Table 5  
Models' comparative average AIC values.

<table><tr><td>Time series model (ARMIA (p,q,r))</td><td>Homogeneous Poisson model</td><td>Self-exciting Hawkes process (Model #1)</td><td>ETAS model (Model #2)</td></tr><tr><td>13,398.661</td><td>9047.397</td><td>7143.110</td><td>6415.187</td></tr></table>

## References

[1] F. Abel, E. Diaz-Aviles, et al., Analyzing the blogosphere for predicting the success of music and movie products, International Conference on Advances in Social Networks Analysis and Mining (ASONAM), IEEE, 2010, pp. 276–280.

[2] L. Adamopoulos, Cluster models for earthquakes: regional comparisons, Mathematical Geology 8 (4) (1976) 463–475.

[3] Y.-Y. Ahn, S. Han, et al., Analysis of topological characteristics of huge online social networking services, Proceedings of the 16th international conference on World Wide Web, ACM, Banff, Alberta, Canada, 2007, pp. 835–844

[4] H. Akaike, Information theory and an extension of the maximum likelihood principle, 2nd Inter. Symp. on Information Theory, 1, 1992, pp. 610–624.

[5] S. Alexey, B.S. Martin, et al., Reconstruction of missing data in social networks based on temporal patterns of interactions, Inverse Problems 27 (11) (2011) 115013.

[6] E. Bacry, S. Delattre, et al., Modelling microstructure noise with mutually exciting point processes, Quantitative Finance (2012) 1–13.

[7] Y. Bae, H. Lee, A sentiment analysis of audiences on twitter: who is the positive or negative audience of popular twitterers? Proceedings of the 5th international conference on Convergence and hybrid information technology, Springer-Verlag, Daejeon, Korea, 2011, pp. 732–739.

[8] C.H. Baird, G. Parasnis, From social media to social customer relationship management, Strategy & Leadership 39 (5) (2011) 30–37.

[9] N.G. Barnes, Exploring the link between customer care and brand reputation in the age of social media, in: S. f. NC Research (Ed.), Society for New Communication Research, 2008.

[10] L. Bauwens, N. Hautsch, Modelling <sup>fi</sup>nancial high frequency data using point processes, in: T. Mikosch, J.-P. Kreiß, R.A. Davis, T.G. Andersen (Eds.), Handbook of Financial Time Series, Springer, Berlin Heidelberg, 2009, pp. 953–979.

[11] P.R. Berthon, When customers get clever: managerial approaches to dealing with creative consumers, Strategic Direction 23 (8) (2007).

[12] P.R. Berthon, L.F. Pitt, et al., Marketing meets Web 2.0, social media, and creative consumers: implications for international marketing strategy. Business Horizons 55 (3) (2012) 261–271.

[13] C.G. Bowsher, Modelling security market events in continuous time: intensity based multivariate point process models, Journal of Econometrics 141 (2) (2007) 876–912.

[14] Brand Directory, “BrandFinance Banking 500 2013” [online], [Accessed 07/01/2013] Available from http://www.brandirectory.com 2013.

[15] L. Capozzi, L.B. Zipfel, The conversation age: the opportunity for public relations, Corporate Communications: An International Journal 17 (3) (2012) 336–349.

[16] M. Cha, H. Kwak, et al., Analyzing the video popularity characteristics of large-scale user generated content systems, IEEE/ACM Transactions on Networking 17 (5) (2009) 1357–1370.

[17] G. Chatzopoulou, S. Cheng, et al., A <sup>fi</sup>rst step towards understanding popularity in youtube, INFOCOM IEEE Conference on Computer Communications Workshops, 2010.

[18] V. Chavez-Demoulin, A.C. Davison, et al., Estimating value-at-risk: a point process approach, Quantitative Finance 5 (2) (2005) 227–234.

[19] E. Chornoboy, L. Schramm, et al., Maximum likelihood identi<sup>fi</sup>cation of neural point process systems, Biological Cybernetics 59 (4) (1988) 265–275.

[20] A.Y.K. Chua, S. Banerjee, Customer knowledge management via social media: the case of Starbucks, Journal of Knowledge Management 17 (2) (2013) 237–249.

[21] Constant Contact, Report on consumer behavior highlights the need for small businesses to be active on Facebook, Constant Contact Inc. 2011

[22] R. Crane, D. Sornette, Robust dynamic classes revealed by measuring the response function of a social system Proceedings of the National Academy of Sciences 105 (41) (2008).15649–15653

[23] D.J. Daley, D. Vere-Jones, Conditional intensities and likelihoods, An Introduction to the Theory of Point Processes, , Springer, New York, 2003. 211–287.

[24] A. Dassios, H. Zhao, Ruin by dynamic contagion claims, Insurance: Mathematics and Economics 51 (1) (2012) 93-106

[25] L. de Vries, S. Gensler, et al., Popularity of brand posts on brand fan pages: an investigation of the effects of social media marketing Journal of Interactive Marketing 26 (2) (2012) 83–91.

[26] R.F. Engle, A. Lunde, Trades and quotes: a bivariate point process, Journal of Financial Econometrics 1 (2) (2003) 159–188.

[27] L. Erik, M. George, et al., Self-exciting point process models of civilian deaths in Iraq, 2010.

[28] F. Benevenuto, T. Rodrigues, V. Almeida, J. Almeida, K. Ross, Video interactions in online video social networks ACM Transactions on Multimedia Computing Communi: cations, and Applications (TOMCCAP) 5 (4) (2009) 30.

[29] F. Figueiredo, Fabr, et al., The tube over time: characterizing popularity growth of youtube videos, Proceedings of the fourth ACM international conference on Web search and data mining, ACM, Hong Kong, China, 2011, pp. 745–754.

[30] I. Guy, M. Jacovi, et al., Same places, same things, same people?: mining user similarity on social media, Proceedings of the 2010 ACM conference on Computer supported cooperative work, ACM, Savannah, Georgia, USA, 2010, pp. 41–50

[31] D. Harte, PtProcess: an R package for modelling marked point processes indexed by time, Journal of Statistical Software 35 (8) (2010) 1–32.

[32] A.G. Hawkes, Spectra of some self-exciting and mutually exciting point processes, Biometrika 58 (1) (1971) 83–90.

[33] A.G. Hawkes, D. Oakes, A cluster process representation of a self-exciting process, Journal of Applied Probability 11 (3) (1974) 493–503.

[34] J. Howe, The rise of crowdsourcing, Wired Magazine 14 (6) (2006) 1–4.

[35] J. Howison, J.F. Olson, A. Kittur, K.M. Carley, Motivation through visibility in open contribution systems, http://repository.cmu.edu/isr/493/ 2011 (accessed May 19, 2014).

[36] B.A. Huberman, Crowdsourcing and attention, Computer 41 (11) (2008) 103–105.

[37] L.B. Jabeur, L. Tamine, et al., Uprising microblogs: a bayesian network retrieval model for tweet search, Proceedings of the 27th Annual ACM Symposium on Applied Computing, ACM, Trento, Italy, 2012, pp. 943–948.

[38] B.J. Jansen, M. Zhang, et al., Twitter power: tweets as electronic word of mouth, Journal of the American Society for Information Science and Technology 60 (11) (2009) 2169–2188.

[39] L. Jong Gun, M. Sue, et al., An approach to model and predict the popularity of online contents with explanatory factors, Web Intelligence and Intelligent Agent Technology (WI-IAT), 2010 IEEE/WIC/ACM International Conference on, 2010.

[40] S. Kong, L. Feng, et al., Predicting lifespans of popular tweets in microblog, Proceedings of the 35th international ACM SIGIR conference on Research and development in information retrieval, ACM, Portland, Oregon, USA, 2012, pp. 1129–1130.

[41] M. Lawrence, E.C. Michael, Hawkes process as a model of social interactions: a view on video dynamics, Journal of Physics A: Mathematical and Theoretical 43 (4) (2010) 045101.

[42] C. Lee H. Kwak et al. Finding influentials based on the temporal order of information adoption in twitter, Proceedings of the 19th International Conference on World Wide Web, ACM, Raleigh, North Carolina, USA, 2010, pp. 1137–1138.

[43] J.G. Lee, S. Moon, K. Salamatian, Modeling and predicting the popularity of online contents with Cox proportional hazard regression model, Neurocomputing 76 (1) (2012) 134–145.

[44] K. Lerman, T. Hogg, Using a model of social dynamics to predict popularity of news, Proceedings of the 19th International Conference on World wide Web, ACM, Raleigh, North Carolina, USA, 2010, pp. 621–630

[45] J. Leskovec, K.J. Lang, et al., Statistical properties of community structure in large social and information networks, Proceedings of the 17th international conference on World Wide Web, ACM, Beijing, China, 2008, pp. 695–704.

[46] W.B. Lober, J.L. Flowers, Consumer empowerment in health care amid the internet and social media, Seminars in Oncology Nursing 27 (3) (2011) 169–182.

[47] G.O. Mohler, M.B. Short, et al., Self-exciting point process modeling of crime, Journal of the American Statistical Association 106 (493)(2011) 100–108.

[48] A. Noff, Learning from Starbucks — one tweet at a time, available at: http://www. blonde20.com/blog/2009/11/19/learning-from-starbucks-one-tweet-at-a-time/ 2009 (accessed August 25, 2012).

[49] A. Noff, The Starbucks formula for social media success, URL:http://thenextweb. com/2010/01/11/starbucks-formula-social-media-success/ 2011.

[50] Y. Ogata, Statistical models for earthquake occurrences and residual analysis for point processes, Journal of the American Statistical Association 83 (401) (1988) 9–27.

[51] Y. Ogata, D. Vere-Jones, Inference for earthquake models: a self-correcting model, Stochastic Processes and their Applications 17 (2) (1984) 337–347.

[52] T. Ozaki, Maximum likelihood estimation of Hawkes' self-exciting point processes, Annals of the Institute of Statistical Mathematics 31 (1) (1979) 145–155.

[53] R.D. Peng, Multi-dimensional point process models in r, 2002

[54] H. Rui, A. Whinston, Designing a social-broadcasting-based business intelligence system, ACM Transactions on Management Information Systems 2 (4) (2012) 1–19.

[55] D. Rybski, S.V. Buldyrev, et al., Communication activity in a social network: relation between long-term correlations and inter-event clustering, Scienti<sup>fi</sup>c Reports 2 (2012).

[56] SAS Harvard Business Review Analytic Services, The New Conversation: TakingSocial Media from Talk to Action, Harvard Business School Publishing, 2010.

[57] C.M. Sashi, Customer engagement, buyer–seller relationships, and social media, Management Decision 50 (2) (2012) 253–272.

[58] G. Szabo, B.A. Huberman, Predicting the popularity of online content, Communications of the ACM 53 (8) (2010) 80–88.

[59] A. Veen, F.P. Schoenberg, Estimation of space–time branching process models in seismology using an EM-type algorithm, Journal of the American Statistical Association 103 (482) (2008) 614-624

[60] T. Wang, M. Bebbington, et al., Markov-modulated Hawkes process with stepwise decay, Annals of the Institute of Statistical Mathematics 64 (3) (2012) 521–544.

[61] W. Willinger, R. Rejaie, et al., Research on online social networks: time to face the real challenges, SIGMETRICS Performance Evaluation Review 37 (3) (2010) 49–54.

[62] E. Sadikov, A.G. Parameswaran, P. Venetis, et al., Blogs as Predictors of Movie Success, International AAAI Conference on Weblogs and Social Media (ICWSM) (2009).

[63] M. Egesdal, C. Fathauer, K. Louie, J. Neuman, G. Mohler, E. Lewis, Statistical and stochastic modeling of gang rivalries in Los Angeles SIAM Undergraduate Research On: line 3 (2010) 72–394

[64] L. Mitchell, M.E. Cates, Hawkes process as a model of social interactions: a view on video dynamics, Journal of Physics A: Mathematical and Theoretical 43 (4) (2010) 045101.

[65] A. Jalilian, ETAS: Modeling earthquake data using Epidemic Type Aftershock Sequence model, 2012.

[66] R.J. Hyndman, Y. Khandakar, Automatic time series for forecasting : the forecast package for R, 2007.

![](/api/attachments/4ZTSBXXC/fulltext/images/10759a2012f3485086c8fceab12aead14cb3d5f64f29b2653c8ce014304e07fe.jpg)

Amir Hassan Zadeh is a PhD student in the Management Science and Information Systems Department within the Spears School of Business at Oklahoma State University. He received his master's in Industrial and Systems Engineering from Amirkabir University of Technology, and his bachelor's from Department of Mathematics and Computer Science, Shahed University, Tehran, Iran. He has been published in the Journal of Production Planning and Control, Annals of Information Systems, Advances in Intelligent and Soft Computing, African Journal of Business Management, and also conference proceedings of DSI, INFORMS and IEEE. His current research interests include big data and analytics, social networks and recommender systems. His research also involves decision support systems, data mining and knowledge discovery

and system analysis and design. Other areas of interest include supply chain management, product design, and healthcare.

![](/api/attachments/4ZTSBXXC/fulltext/images/28b94861074a112fca9b103d12ff8161735c8f7698200577f71df8d7f27e22dc.jpg)

others. He is a member of the editorial boards of journals such as the Decision Support Systems and Information Systems Frontiers. He is currently serving as the Executive Director of Teradata University Network and received the 2013 INFORMS HG Computing Society Lifetime Service Award.

Ramesh Sharda is the interim Vice Dean of the Watson Graduate School of Management, Watson/ConocoPhillips Chair and a Regents Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University. He also serves as the Executive Director of the PhD in Business for Executives Program. He has coauthored two textbooks (Business Intelligence and Analytics: Systems for Decision Support, 10th edition, Prentice Hall and Business Intelligence: A Managerial Perspective on Analytics, 3rd Edition, Prentice Hall). His research has been published in major journals in management science and information systems including Management Science, Operations Research, Information Systems Research, Decision Support Systems, Interfaces, INFORMS Journal on Computing, and man
