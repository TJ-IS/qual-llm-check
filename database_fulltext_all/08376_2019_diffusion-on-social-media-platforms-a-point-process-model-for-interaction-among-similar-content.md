---
otero_id: 8376
otero_key: "5QZ8VNTD"
title: "Diffusion on Social Media Platforms: A Point Process Model for Interaction among Similar Content"
authors: "Eunae Yoo; Bin Gu; Elliot Rabinovich"
year: "2019"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1661096"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Diffusion on Social Media Platforms: A Point Process Model for Interaction among Similar Content

Eunae YooEUNAE YOO, Bin GuBIN GU & Elliot RabinovichELLIOT RABINOVICH

To cite this article: Eunae YooEUNAE YOO, Bin GuBIN GU & Elliot RabinovichELLIOT RABINOVICH (2019) Diffusion on Social Media Platforms: A Point Process Model for Interaction among Similar Content, Journal of Management Information Systems, 36:4, 1105-1141, DOI: 10.1080/07421222.2019.1661096

To link to this article: https://doi.org/10.1080/07421222.2019.1661096

![](/api/attachments/5QZ8VNTD/fulltext/images/3cf9368fed5bcb438357c25f767822dcbb9aa24c54d7c35474053fd6c9f7176e.jpg)

Published online: 09 Oct 2019.

![](/api/attachments/5QZ8VNTD/fulltext/images/d259f268d887c49a052563b5c9d4524f6eb4b1c5b025fb7f3d59bfdad93ee59f.jpg)

Submit your article to this journal

![](/api/attachments/5QZ8VNTD/fulltext/images/25aedc4633b4fcf49706403f48a7a3cdb7e93f6b4907c7d1901a8ac155c01cbb.jpg)

Article views: 10

![](/api/attachments/5QZ8VNTD/fulltext/images/8be645229a7dd23199c811518d0f4f3d77aef0afb6cf00f44f16f7aaeb179f0c.jpg)

View related articles

![](/api/attachments/5QZ8VNTD/fulltext/images/1c9813a38d78368d6b7f96a534760b594287d0cc604bf12fee323267c257b8d3.jpg)

View Crossmark data

# Diffusion on Social Media Platforms: A Point Process Model for Interaction among Similar Content

EUNAE YOO, BIN GU, AND ELLIOT RABINOVICH

EUNAE YOO (eyoo@utk.edu; corresponding author) is an Assistant Professor of Supply Chain Management at the Haslam College of Business at the University of Tennessee. She received her Ph.D. from the W. P. Carey School of Business at Arizona State University. Dr. Yoo’s research interests lie at the intersection of information systems and supply chain management, and include social media, online information diffusion, and humanitarian operations management. Her work has previously been published in the Journal of Operations Management.

BIN GU (Bin.Gu@asu.edu) is the Earl and Gladys Davis Distinguished Professor and Associate Dean of China Programs at the W. P. Carey School of Business at Arizona State University. He received his Ph.D. degree from the Wharton School of Business at the University of Pennsylvania. Dr. Gu’s research interests are in online digital platforms, future of work, AI and fintech, digital healthcare, online social media, and social networks, and IT-enabled business models. His work has appeared in Management Science, MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Production and Operations Management, Journal of Retailing, and other leading academic journals.

ELLIOT RABINOVICH (Elliot.Rabinovich@asu.edu) is the AVNET Professor of Supply Chain Management at the W. P. Carey School of Business, Arizona State University and the Co-Director of the Internet-edge Supply Chain Management Lab. His Ph.D. is from the University of Maryland. Dr. Rabinovich’s research has focused on the effects that Internet technology applications have on supply chain and operations management. His work has been published in California Management Review, Decision Sciences, Journal of Business Logistics, Journal of Operations Management, Sloan Management Review, and other journals. As part of his research, he has worked with such companies as Cooking.com, eBags.com, Intel, PetSmart, Walmart, and Twitter. His research has been recognized by the University of Maryland with the Nash Outstanding Doctoral Alumni Award, with fellowships from the Institute of Supply Management, and with awards from the Council of Supply Chain Management Professionals. He has recently published a book, Internet Retail Operations: Integrating Theory and Practice for Managers (Taylor & Francis).

ABSTRACT: Social media platforms disseminate a massive volume of user-generated content, some of which convey similar and overlapping information. We study how the diffusion of a given piece of content (called a cascade) is influenced by the diffusion of other cascades carrying similar content (called parallel cascades). We theorize that the diffusion of a cascade can be inhibited or amplified by that of parallel cascades containing similar content. To study this phenomenon, we formulate a generalized version of the self-exciting point process model and showcase a novel approach to evaluating the parallel diffusion of similar social media content. We estimate the model using Twitter data. We observe that, on average, the diffusion of a cascade is inhibited by the concurrent diffusion of parallel cascades with similar content. We further identify an asymmetry among content producers as the diffusion of content contributed by those with larger networks is more likely to be amplified by the diffusion of similar content. Our study underscores the importance of accounting for content similarity as failing to do so may overestimate assessments of a cascade’s diffusion. Our results also suggest that smaller, individual social media content contributors should avoid publishing repetitive content and channel their efforts towards developing novel content, while this is not a concern for larger content contributors.

KEY WORDS AND PHRASES: cascade, content diffusion, competition for attention, parallel cascade, point process, social media, media platforms, social media content.

## Introduction

Social media platforms allow users to produce and share large volumes of information at very low cost. This, in turn, generates an overabundance of content vying for the limited attention of users. The ability of a social media content producer to heighten exposure to her content is dependent on how many other users help diffuse the content [59]. On social media platforms, the diffusion of content is facilitated by the platforms’ sharing functions (“retweets” on Twitter, “shares” on Facebook, “regrams” on Instagram). Prior literature has examined how producers can increase the diffusion of their social media content. However, the majority of this work treats each piece of content as an isolated entity, assuming the diffusion of content is independent of the diffusion of other concurrent content.<sup>1</sup> Our goal is to fill this gap by assessing how the diffusion of similar content may be interdependent.<sup>2</sup>

Our approach allows the diffusion of content to be influenced by the dissemination of other content conveying similar information. We leverage the literature on social media and competition for attention to develop research conjectures on the relationship between the diffusion of a piece of content and the diffusion of other pieces of similar content. Because they offer equivalent informational value, we conjecture that the spread of a specific piece of content can be crowded out by the diffusion of other similar content. Thus, the diffusion of content can be inhibited as other strains of similar information propagate. At the same time, however, multiple pieces of content carrying a similar message can signal to users the importance of the message. This will help strengthen the spread of content for this message and result in the amplification of diffusion. We aim to identify whether an inhibiting or amplifying dynamic emerges among similar content and understand the conditions under which one of these dynamics overpowers the other.

Our study is rooted in the recognition that social media content producers benefit from reaching a wider audience through the diffusion of their content [33]. For example, producers of content that diffuses successfully enjoy higher reputations and earn other tangible benefits, such as larger networks of followers or subscribers and higher revenues on social media platforms like YouTube [68]. To improve the dissemination of their social media content, it is important for producers to understand the interplay of similar content. Under an inhibiting dynamic, producers should avoid publishing similar content as other producers and, instead, focus on developing novel content or presenting overlapping content in a unique manner. In contrast, an amplifying dynamic suggests that producers may benefit from the spread of similar content and do not have to be concerned that the redundancy of their content will dampen diffusion. By examining the interaction of the diffusion of similar content, our study sheds light on how a producer can enhance the diffusion of her content in the presence of similar content from other producers.

To analyze social media content diffusion, we formulate a generalized version of the self-exciting point process [29]. The origins of the self-exciting point process are the areas of Statistics and Probability theory. The underlying logic of the self-exciting point process is that occurrences of an event are interdependent such that an occurrence increases the probability of future occurrences. Furthermore, the self-exciting point process is flexible and can be modified to evaluate the interdependence of the diffusion of similar content. For these reasons, we adopted the self-exciting point process as the foundation for our point process model. In doing so, we showcase an interdisciplinary perspective and demonstrate how this novel model can be used to investigate IS phenomena and research questions that involve the dependence of events.

The self-exciting point process in our work relies on mapping the diffusion of content on a social media platform through the shares generated by the platform’s sharing function. Based on when and how many times a piece of content is shared, the selfexciting point process calculates the content’s intensity of sharing, or diffusion rate. Each time a piece of content is shared, its intensity increases. This implies that a share raises the likelihood of another share. We extend the original self-exciting point process by incorporating the diffusion of other strands of content carrying similar information. These shares can impose a positive or a negative effect on the intensity to model an amplifying or inhibiting interaction, respectively. Hence, our model accounts for the propagation of peripheral content when measuring the diffusion rate of a piece of social media content. To the best of our knowledge, ours is the first point process model to measure the spread of social media content as a byproduct of not only its own shares but also the shares of similar content.

We estimated the model using Twitter data. We refer to a tweet and its series of retweets as a cascade in line with prior studies [24, 39, 78]. A cascade is initiated by a tweet and diffuses as it is retweeted over time. The producer of a cascade is the user that published the tweet that launched the cascade. Our sample consists of 24,070 cascades that were generated by 14,362 distinct producers and retweeted 138,106 times. These data were from four large sudden disasters that required relief efforts by humanitarian organizations. By studying the diffusion of social media content in these emergencies, our study adds to the nascent literature on the application of social media platforms during crisis events.

We used advanced text-mining techniques to identify cascades carrying similar information. A cascade’s content was represented by the text in its corresponding tweet. We adopted near-duplicate detection techniques to organize cascades and their content into fine-grained topics. We identified for each cascade a set of other cascades pertaining to the same topic and conveying similar content (called parallel cascades).

The estimation of our point process model confirms that the diffusion of each cascade is the result of its own retweets as well as the retweets of its parallel cascades. On average, a cascade’s spread is inhibited by the contemporaneous diffusion of other cascades that communicate a similar message. This shows that content similarity typically impedes diffusion and makes it more difficult to gain users’ attention [15]. At the same time, our results reveal that the diffusion of cascades experiences an amplifying relationship at times. Specifically, the diffusion of approximately 30 percent of parallel cascades across all cascades in our sample amplifies the diffusion of their corresponding cascades. This suggests that the propagation of redundant content can act as repeated signals of the information’s value, which enhances diffusion of all content related to the same topic [9, 47]. Thus, we contribute evidence of variation in the dynamics shared between the diffusion of a piece of content and other pieces of content with equivalent informational value.

Our results also demonstrate that the size of a producer’s network on social media impacts whether the diffusion of her cascades experiences an inhibiting versus an amplifying relationship with the diffusion of parallel cascades. We find that the diffusion of a producer’s cascade increasingly benefits from the spread of parallel cascades as the size of her network increases. This highlights an asymmetry between large and small producers with regards to their content diffusion.<sup>4</sup> This also carries important implications for smaller producers, such as individual social media content creators, that aim to increase the diffusion of their content and build their social media presence. Our results suggest that smaller producers should concentrate on developing unique content and avoid publishing content that is equivalent to other producers’ content.

Finally, our study adds to the burgeoning research stream of Computational Social Science research [12]. We analyze a large Twitter data set using an interdisciplinary statistical model and text analysis techniques from Computer Science. We derive insights on the inner workings of content diffusion at the micro-level of the cascade and also draw actionable implications that can improve the diffusion and online presence of social media content producers. Moreover, causal inference is a core part of Computational Social Science [54], and our study presents an effort to achieve causal inference regarding content diffusion.

## Related Literature

Our study is informed by four research streams: (1) diffusion of social media content; (2) social media and competition for attention; (3) social media during crises; and (4) self-exciting point process models.

## Diffusion of Social Media Content

Researchers have found that the diffusion of social media content is affected by a variety of factors, including features of the content. Social media content that evokes stronger emotional responses tends to be shared more frequently and quickly [5, 65]. Likewise, social media content that appeals to emotions and communicates humor promotes user engagement [38]. In the context of news distribution, Shore et al. [64] found that politically moderate news sources are more likely to be disseminated by users. The quality of content, too, can spur diffusion. Higher-quality content draws more engagement and spreads more effectively [32]. Thus, learning from signals by peers about the quality of content can heighten diffusion [56].

Attributes of the user network underlying social media platforms can also significantly affect the spread of content. Content by well-connected users tends to experience greater diffusion since such producers are better equipped to broadcast their information to a wider audience. This applies to content producers with large networks of direct connections [4, 67] as well as both direct and indirect connections [77]. While producers’ network size is important, Goel et al. [24] observed that success in content diffusion depends on broadcast size — whether achieved by the producer or other users that helped share it.

## Social Media and Competition for Attention

Social media play a role in defining the competition for attention between firms. As social media chatter related to a firm increases, content associated with the same firm’s competitors declines. Firms can thus cannibalize social media attention from competing firms [40]. This impacts performance measures, such that an increase in social media content about a firm diminishes rival firms’ stock performance [41].<sup>6</sup> Attention on social media toward one entity can alternatively enhance attention for competitors. A blog that directs readers to rival blogs can actually grow its own audience: this signals the blog’s ability to quickly provide its readers with news, albeit indirectly [43]. Dellarocas et al. [21] demonstrated that news aggregators can substitute for original content producers but also help direct attention toward a producer’s articles.

At a more granular level, authors have examined how individual pieces of social media content compete for attention. Multiple threads of content on social media platforms compete for users’ limited amount of attention [33, 63, 73], and the successful diffusion of a strand of content is often at the expense of the diffusion of other pieces of content [2]. This is reminiscent of the cannibalization effect again [40]. For content to successfully propagate, its information should be novel [15, 16, 70]. In addition, social media content that is disseminated by users with large networks is more likely to outperform competitors [73]. While social media content can display competitive dynamics with regard to diffusion, Myers and Leskovec [47] observed instances of a supportive relationship such that the spread of content at times strengthens the spread of other related content.

## Social Media During Crises

Social media platforms have proven to be a valuable tool during emergency situations, such as natural disasters. Many humanitarian organizations are actively involved on social media and communicate important updates on available resources and services via this channel [76]. Moreover, social media platforms help the general public cope with stressful crisis situations by facilitating collective information gathering and processing and helping organize crisis response activities [49, 51]. Researchers have started to investigate the contribution and diffusion of social media content during crises. In general, social media activity escalates once a disaster occurs, especially in areas that are impacted by a disaster [36]. Users within a disaster zone tend to post greater amounts of content and ramp up their communication with other users in their networks [53]. Vieweg et al. [69] also found that users prefer to share social media content that provides updates about crisis situations, such as evacuation information and changes in weather conditions. Finally, during Hurricane Sandy, the production of Twitter cascades increased as the hurricane approached landfall [78]. The authors observed that during these times of higher social media traffic, the diffusion speed for a cascade decreases due to crowdedness and more intense competition for attention.

## Applications of Self-Exciting Point Process Models

A self-exciting point process model facilitates an examination of how the occurrence of an event raises the likelihood of future occurrences [29]. Self-exciting point processes have been applied to understand phenomena in a variety of contexts, including Seismology [50] and Criminology [46]. In the Marketing literature, Xu et al. [75] developed a multivariate self-exciting point process model and analyzed how a consumer’s history of clicks on online advertisements for a product impacts her decision to purchase the product. Researchers in Finance have also applied selfexciting point processes to understand dependence between high-frequency financial market events, such as trades and mid-price changes [3, 6].

Self-exciting point process models are relevant to research topics related to the IS discipline.<sup>7</sup> Related to our work, researchers have developed self-exciting point process models to predict diffusion and popularity of social media content, such as the number of views for YouTube videos [17] and retweet counts for Twitter cascades [79]. This research builds on that work with new analyses and results.

## Research Conjectures on the Interaction of Social Media Content

Topics are subject to intense competition on social media platforms. When one wins the attention of users and propagates through the platform, it negatively impacts the spread of others [2]. A comparable phenomenon exists within a topic due to a crowding out effect of a cascade by the diffusion of other parallel cascades on the same topic. Because similar information is presented in a cascade and in parallel cascades with redundant content, they can be viewed as substitutes. This raises the likelihood that a cascade will be pushed aside and that, instead, users will share the parallel cascades [27]. Supporting this, Shen et al. [63] found that online reviewers prefer to avoid posting reviews for products that are already congested with reviews. The crowdedness of the reviewing space signals more severe competition for attention and makes it more difficult for a review to be noticed and earn votes. This has also been observed in the context of expert blogs devoted to discussing consumer brands. As expert blogs increasingly focus on one brand, this diminishes the blogs’ capacity to discuss competing brands [40]. For a cascade on social media, the propagation of parallel cascades implies that users’ attention for its content is being crowded out and apportioned elsewhere. Thus, a cascade’s diffusion will be inhibited by the dissemination of other cascades relaying similar content. This leads to our first conjecture:<sup>8</sup>

## ● Conjecture 1a (The Diffusion Inhibition Conjecture): A cascade’s diffusion is inhibited by the diffusion of parallel cascades containing similar content.

Conversely, the diffusion of a cascade may be strengthened by the spread of parallel cascades with similar content due to a reinforcement effect. An individual that receives repeated indicators that her peers are adopting a behavior is more likely to adopt the same behavior [9]. Such a phenomenon is known as complex contagion [10]. Each notification of adoption of a behavior leads to an increase in the subsequent rate of adoption, such as for a new application on Facebook [1], usage of a hashtag in one’s social media posts [60], and sharing of content on Twitter and Digg [31]. Likewise, since a cascade and its parallel cascades convey equivalent information, the sharing of parallel cascades may serve as repeated signals that a cascade deserves to be shared. This effect may be more pronounced during a significant and newsworthy event, which typically leads to a flood of similar content being produced and shared. Users may interpret this surge as a signal that cascades containing such content are meaningful and worth sharing [21, 47]. As such, the distribution of parallel cascades may reinforce users’ motivation to share a cascade. This will amplify, rather than inhibit, the cascade’s diffusion. Conjecture 1b formalizes this alternate conjecture.

● Conjecture 1b (The Diffusion Amplification Conjecture): A cascade’s diffusion is amplified by the diffusion of parallel cascades containing similar content.

According to Conjecture 1a (C1a) and Conjecture 1b (C1b), cascades pertaining to the same topic may exert an inhibiting or amplifying effect based on each other’s diffusion. We conjecture that the number of users following a cascade’s producer can determine the direction of this interaction. On social media platforms, a user’s followers constitute other users that connect with her and subscribe to receiving her content. Producers with higher counts of followers are “larger” since they are directly connected to a bigger audience. They are capable of generating stronger and more extensive information signals. This increases their ability to tap into a substantial pool of attention resources and overcome detractions in their audience’s attention caused by parallel cascades [23]. Larger producers also tend to have superior reputations partly because they typically publish content of higher quality [25, 68]. Thus, users generally favor sharing content by reputable producers [20]. Due to this preference, the diffusion of parallel cascades is more likely to lend credibility to cascades by larger producers. This difference in perceived quality may emerge despite the similarity of content released by larger and smaller producers. For these reasons, we anticipate larger producers are more likely to experience amplification for the propagation of their cascades than smaller ones:

● Conjecture 2 (The Larger Producer Advantage Conjecture): The diffusion of cascades by larger producers is more likely to be amplified by the diffusion of parallel cascades.

## Point Process Model for the Diffusion of Cascades on Twitter

To test our conjectures, we begin by formulating a model that measures the diffusion of individual cascades on Twitter.<sup>9</sup> We focus on Twitter for several reasons. First, Twitter is a highly visible and widely adopted social media platform. Second, Twitter’s focus on providing users with real-time content has made this platform a widely-regarded source of up-to-date information. Third, Twitter also provides accessibility to rich metadata on the tweet and retweets that make up a cascade as well as the users involved in initiating and sharing the cascade. Finally, content producers on Twitter range from individual content creators to prominent organizations. Studying the diffusion of content on Twitter, therefore, allows us to deliver managerial implications and actionable recommendations for a range of social media content producers.

When a Twitter user produces content from a tweet, this content is immediately transmitted to her network of followers. This tweet can be further disseminated through retweets, which instantly forward the tweet to the followers of the users that issued the retweets. These users who choose to retweet are referred to as “retweeters.” All retweets preserve a tweet’s content and clearly assign credit for the content to the original user that generated the tweet being shared. A cascade on Twitter comprises a tweet and its retweets, and the producer for a cascade is the user that published the tweet at the start of the cascade. Tracing the path of a cascade reveals how the original content in a tweet diffuses through retweets on Twitter.

Retweets exert a positive reinforcement effect on a cascade’s diffusion. This is because as a cascade earns more retweets, it increases the exposure to its content, which can stimulate additional retweets [74]. In order to capture this dynamic, we propose a model for the diffusion of Twitter cascades based on the self-exciting point process, or the Hawkes process [29]. We next describe a basic self-exciting point process for a Twitter cascade and then present our model.

A point process is a series of points that denotes the occurrence of an event along a finite and nonnegative timeline. A cascade’s retweets are the events of interest; therefore, a retweet can be marked as a point along a timeline. A point process can be characterized through a counting measure, $R ^ { i } ( t )$ , which corresponds to the number of retweets that cascade i has accumulated by time t. $R ^ { i } ( t )$ is rightcontinuous, increasing, and integer-valued, making it a step function that increases by a value of 1 every time a retweet occurs [18]. For example, suppose the first retweet for cascade i occurs at $t _ { 1 }$ and the second at $t _ { 2 }$ . This means that $R ^ { i } ( t _ { 1 } ) = 1$ and that $R ^ { i } ( t _ { 2 } ) = 2$ . Thus, $R ^ { i } ( t _ { 2 } ) - R ^ { i } ( t _ { 1 } )$ corresponds to the number of retweets for i between $\left( t _ { 1 } , t _ { 2 } \right]$ . For any time prior to $t _ { 1 }$ , the count measure is equal to 0.

In our study, the events (retweets) do not occur independently as each retweet for a cascade raises the likelihood of future retweets for the same cascade [74]. Hence, we utilize a self-exciting point process since this model allows the arrival of a cascade’s retweets to be influenced by the prior arrival of earlier retweets. The self-exciting point process is able to handle dependence among retweets by specifying the intensity as a conditional function of time and the history of the point process [29]. The history of the point process until t has information about all retweets prior to t and is expressed for cascade i as $\mathcal { H } _ { t } ^ { i }$ [18]. Its intensity is the likelihood that a cascade is retweeted anytime, conditional on past retweets. Intensity can be interpreted as a cascade’s diffusion rate [79]. The conditional intensity function for cascade i is defined as:

$$
\lambda^ {i} (t | \mathcal {H} _ {t} ^ {i}) = \lim _ {\Delta t \rightarrow 0} \frac {\left\{R ^ {i} (t + \Delta t) - R ^ {i} (t) > 0 \mid \mathcal {H} _ {t} ^ {i} \right\}}{\Delta t},\tag{1}
$$

where $\lambda ^ { i } \left( t | \mathcal { H } _ { t } ^ { i } \right) { > } 0$ and $t + \Delta t > t .$ According to Equation 1, the conditional probability of observing a retweet for cascade i between $( t , t + \Delta t ]$ is equal to $\lambda ^ { i } \big ( t | \mathcal { H } _ { t } ^ { i } \big ) * \Delta t$

In the self-exciting point process by Hawkes [29], every event increases the conditional intensity function in an additive (or “exciting”) fashion. Thus, the arrival of a retweet enhances a cascade’s diffusion speed and makes the arrival of the next retweet come faster. Cascades with higher intensity are more likely to be retweeted than cascades with lower intensity. The self-exciting point process consists of two parts. The first term $( \mu ^ { i } )$ represents the baseline intensity for cascade i, which can be interpreted as the generally expected rate of occurrence for retweets of i [30]. Since not all cascades are created equal, we allow the baseline intensity to vary across cascades. This modeling decision enables us to account for the heterogeneity of cascade characteristics, such as the size of cascade producers that contribute to differences in baseline intensities across cascades. The second term captures the exciting effect of a retweet issued at time s on cascade i’s diffusion speed at time t. Eq. 2 presents this point process, where $\mu ^ { i } > 0$ and $s < t { : }$

$$
\lambda^ {i} \big (t | \mathcal {H} _ {t} ^ {i} \big) = \mu^ {i} + \int_ {- \infty} ^ {t} g ^ {i} (t - s) d R ^ {i} (s),\tag{2}
$$

The exciting effects of retweets for cascade i are not permanent but wear off over time. In line with other studies containing point processes [75], we specify the exciting effect of retweets to decay exponentially. This is shown in Equation 3:

$$
g ^ {i} (t - s) = \alpha^ {i} e ^ {- \beta^ {i} (t - s)},\tag{3}
$$

where $\alpha ^ { i } , \beta ^ { i } > 0$ . We also enforce the restriction $\alpha ^ { i } < \beta ^ { i }$ [29]. The parameter $a ^ { i }$ represents the magnitude of the exciting effect, or the increase in intensity, attributed to a retweet of cascade i that occurred earlier at time s. Additionally, $\beta ^ { i }$ reveals how quickly the exciting effect measured by $\boldsymbol { a } ^ { i }$ dissipates over time. Note that $a ^ { i }$ and $\beta ^ { i }$ are cascade-specific to model the heterogeneity of exciting effects and their deterioration across cascades, respectively. Given the notation, the self-exciting point process in Equation 2 is:

$$
\lambda^ {i} (t | \mathcal {H} _ {t} ^ {i}) = \mu^ {i} + \int_ {- \infty} ^ {t} a ^ {i} e ^ {- \beta^ {i} (t - s)} d R (s)\tag{4}
$$

Equation 4 presents a basic and widely adopted self-exciting point process. Using this as a foundation, we now turn our attention towards specifying a point process that specifically reflects content diffusion on Twitter. Table 1 provides a summary of the notation in our model. We consider Twitter cascades indexed by $i = 1 , \dots , I$ during the observation interval $[ 0 , T ]$ . Cascade i is launched when the tweet for i is published. We label the time that the cascade was initiated relative to the starting point of the observation interval as $t _ { 0 } ^ { i }$ , where $t _ { 0 } ^ { i } \geq 0$ . Cascade i comprises $k = 1 , \ldots , K ^ { i }$ retweets, and the times that these retweets arrived are denoted as $t _ { 1 } ^ { i } , \ldots , t _ { K ^ { i } } ^ { i }$ , where $t _ { K ^ { i } } ^ { i } \leq T$ Therefore, the time that retweet k of cascade i occurred is equal to $t _ { k } ^ { i }$

With this notation, Equation 4 can be rewritten as:

$$
\lambda^ {i} (t | \mathcal {H} _ {t} ^ {i}) = \mu^ {i} + \sum_ {t _ {k} ^ {i} <   t} \alpha^ {i} e ^ {- \beta^ {i} (t - t _ {k} ^ {i})}\tag{5}
$$

From Equation 5, it is clear that the diffusion speed for a cascade at time t depends on the entire history of the cascade up until t. That is, the intensity for i at any time t is a function of the cumulative sum of the exciting effects by all the retweets that occurred prior to t.

Figure 1 illustrates an example of a cascade’s self-exciting point process. The first panel portrays the arrival of retweets as a point process, a series of points along a line that represents time. The second panel depicts the intensity over time when $\mu ^ { i } = 4 , \alpha ^ { i } = 1 . 2$ ; and $\beta ^ { i } = 3$

We first expand the term representing the baseline intensity for a cascade. We expect that the baseline intensity varies across time and capture this with two additional modifications. The first modification accounts for the overall level of chatter on Twitter at time t related to the general subject or event presented in i. A high volume of relevant Twitter activity suggests that users are interested in the subject or event, raising the baseline retweet rate for i. Accordingly, we specified the baseline intensity for a cascade i to increase with the logged level of chatter at t for the general subject or event that i pertains to $( \omega _ { t } ^ { i } )$ . We applied a log-transformation to the volume of activity at t in case of skewness and to limit the scale of the variable. The second modification to the baseline intensity accounts for the natural decay of interest in content over time [58, 74]. We incorporated this in our point process by allowing the baseline intensity to decay exponentially over time. The decay rate is parametrized by $\gamma ^ { i } .$

Table 1. Summary of Notation in Point Process Model

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $\lambda^{i}(t|\mathcal{H}_{t}^{i})$ </td><td>Conditional intensity, or diffusion speed, for cascade  $i$  at time  $t$ </td></tr><tr><td> $t_{k}^{i}$ </td><td>Time that the  $k$ th retweet for cascade  $i$  was published</td></tr><tr><td> $t_{l}^{ij}$ </td><td>Time that the  $l$ th retweet for parallel cascade  $j$  of cascade  $i$  was published</td></tr><tr><td> $\mu^{i}$ </td><td>Baseline intensity for cascade  $i$ </td></tr><tr><td> $\omega_{t}^{i}$ </td><td>Logged level of activity on Twitter for the event associated with  $i$  at time  $t$ </td></tr><tr><td> $\gamma^{i}$ </td><td>Rate of decay of interest in cascade  $i$ </td></tr><tr><td> $\alpha_{1}^{i}$ </td><td>Magnitude of self-exciting effect from cascade  $i$ &#x27;s own retweets</td></tr><tr><td> $\beta_{1}^{i}$ </td><td>Rate of decay of  $\alpha_{1}^{i}$ </td></tr><tr><td> $\alpha_{2j}^{i}$ </td><td>Magnitude of effect from retweets of cascade  $i$ &#x27;s  $j$ th parallel cascade</td></tr><tr><td> $\beta_{2}^{i}$ </td><td>Rate of decay of  $\alpha_{2j}^{i}$ </td></tr><tr><td> $\phi_{t_{k}^{i}}$ </td><td>Logged count of followers for the retweeter of the  $k$ th retweet for cascade  $i$ </td></tr><tr><td> $\phi_{t_{l}^{ij}}$ </td><td>Logged count of followers for the retweeter of the  $l$ th retweet of the  $j$ th parallel cascade for cascade  $i$ </td></tr></table>

(a) Arrival of retweets  
![](/api/attachments/5QZ8VNTD/fulltext/images/31e7da9007bb118935c43cf07c7828a79f301c1eecbd18ca8be0d68e7b74e09d.jpg)

(b) Intensity over time $( \mu ^ { i } = 4 , \alpha ^ { i } = 1 . 2 , \beta ^ { i } = 3 )$  
![](/api/attachments/5QZ8VNTD/fulltext/images/86f44df2b3fae71b83daf9173f83f746391716d5fe23e3c07e647ec0edf0fa7d.jpg)  
Figure 1. Self-Exciting Point Process

In line with prior point process models for the diffusion of social media content [17, 79], we also incorporated a retweeter’s count of followers as a variable that influences the magnitude of the self-exciting effect $( a ^ { i } )$ . In the point process literature, variables that affect the size of the self-exciting effect are referred to as marks. Our model, hence, can be classified as a marked point process. We represent the logged number of followers that a retweeter of $k$ had at $t _ { k } ^ { i }$ with $\phi _ { t _ { k } ^ { i } }$ . The log counts of followers address skewness. We specified the self-exciting effect to be magnified by $\phi _ { t _ { k } ^ { i } }$ to account for the change in intensity from retweeters with higher follower counts exposing a larger audience to the cascade’s content [17]. The modifications to the baseline intensity and self-exciting effect are in Equation $^ { 6 , }$ with $\omega _ { t } ^ { i } , \gamma ^ { i } { > } 0$ and $\phi _ { t _ { k } ^ { i } } \geq 0$

$$
\lambda^ {i} (t | \mathcal {H} _ {t} ^ {i}) = \mu^ {i} \omega_ {t} ^ {i} e ^ {- \gamma^ {i} t} + \sum_ {t _ {k} ^ {i} <   t} \left(\alpha^ {i} \phi_ {t _ {k} ^ {i}} e ^ {- \beta^ {i} (t - t _ {k} ^ {i})}\right),\tag{6}
$$

Our model contains $J + 1$ point processes that model the arrival of retweets for a cascade and retweets for the same cascade’s group of <sup>J</sup> parallel cascades. This is similar to a mutually exciting point process, which also contains multiple point processes but models the intensity of each point process as a function of the arrivals for the other point processes under consideration [29]. Our model is not a mutuallyexciting point process in a strict sense since we only evaluate the intensity of a cascade and exclude evaluating the intensity for each of the j parallel cascades as a function of i and all other $j .$ However, we note that each parallel cascade also belongs to the set of I cascades. Thus, we do eventually evaluate the intensity of j as a function of itself and its own parallel cascades (which may or may not include i and all other j depending on how parallel cascades are determined).

With <sup>J</sup> 1 point processes, we also have $J + 1$ counting measures for a cascade $i \colon R ^ { i } ( t ) = \left\lceil R _ { 1 } ^ { i } ( t ) , \ldots , R _ { j + 1 } ^ { i } ( t ) , \ldots , R _ { J + 1 } ^ { i } ( t ) \right\rceil$ , where $R _ { 1 } ^ { i } ( t )$ is the counting measure for retweets belonging to cascade i and $R _ { j + 1 } ^ { i } ( t )$ is the counting measure for retweets across the $j ^ { \mathrm { t h } }$ parallel cascade of i. The retweets of parallel cascades are indexed by $l = 1 , \dots , L ^ { i j }$ , and the time that retweet <sup>l</sup> for parallel cascade j occurred is marked as $t _ { l } ^ { i j }$ . The time that $L ^ { i j }$ was issued is $t _ { L ^ { i j } } ^ { i j }$ , and $t _ { L ^ { i j } } ^ { i j } \le T$ . Equation 7 presents the full model:

$$
\begin{array}{c} \lambda^ {i} (t | \mathcal {H} _ {t} ^ {i}) = \mu^ {i} \omega_ {t} ^ {i} e ^ {- \gamma^ {i} t} + \sum_ {t _ {k} ^ {i} <   t} \left(\alpha_ {1} ^ {i} \phi_ {t _ {k} ^ {i}} e ^ {- \beta_ {1} ^ {i} (t - t _ {k} ^ {i})}\right) \\ + \sum_ {j = 1} ^ {J} \sum_ {t _ {l} ^ {i j} <   t} \left(\alpha_ {2 j} ^ {i} \phi_ {t _ {l} ^ {i j}} e ^ {- \beta_ {2} ^ {i} (t - t _ {l} ^ {i j})}\right), \end{array}\tag{7}
$$

where $\alpha _ { 1 } ^ { i } , \beta _ { 1 } ^ { i } , \beta _ { 2 } ^ { i } { > } 0 , \phi _ { t _ { \prime } ^ { i j } } \geq 0 , \alpha _ { 1 } ^ { i } { < } \beta _ { 1 } ^ { i }$ , and $\alpha _ { 2 j } ^ { i } { < } \beta _ { 2 } ^ { i }$

In Equation 7, we differentiated the effects of i’s own retweets and the retweets of parallel cascades by having $a _ { 1 } ^ { i }$ and $\beta _ { 1 } ^ { i }$ characterize the former and $a _ { 2 j } ^ { i }$ and $\beta _ { 2 } ^ { i }$ characterize the latter. The parameter $a _ { 1 } ^ { i }$ represents the self-exciting effect of cascade $i \mathbf { \ ' } _ { \mathbf { S } }$ retweets, and $\beta _ { 1 } ^ { i }$ measures the decay rate of the self-exciting effect. Moreover, $a _ { 2 j } ^ { i }$ denotes the effect of retweets belonging to parallel cascade j on the intensity of i. Unlike for $\boldsymbol { a } _ { 1 } ^ { i } ,$ , we do not restrict $a _ { 2 j } ^ { i }$ to be positive-valued. A negative value for $a _ { 2 j } ^ { i }$ reduces cascade $i \ ' \mathrm { s }$ intensity, implying that the arrival of retweets for parallel cascade j inhibits a cascade’s diffusion rate [6, 44]. On the other hand, a positive value for $a _ { 2 j } ^ { i }$ augments i’s intensity in a similar fashion to the selfexciting effect in $a _ { 1 } ^ { i }$ . If $a _ { 2 j } ^ { i }$ is positive, this suggests that a cascade’s intensity benefits from retweets of the jth parallel cascade. Depending on the value of $a _ { 2 j } ^ { i }$ our model allows the effects of parallel cascades’ retweets on a cascade’s intensity to be inhibiting as well as amplifying as argued in C1a and C1b, respectively. The effect of parallel cascades on i’s intensity declines at a rate controlled by $\boldsymbol { \beta } _ { 2 } ^ { i }$ . To keep our model parsimonious, we assume that $\beta _ { 2 } ^ { i }$ is equivalent for all $a _ { 2 j } ^ { i }$

## Data

We describe the data in this study. We also detail the near-duplicate detection techniques that we applied to identify the collection of parallel cascades that contain similar content for each cascade.

## Sample

We collected Twitter data from WeLink, a social media data services firm with access to the Twitter firehose. The Twitter data were generated immediately after the occurrence of four disaster events. We identified these events from a database of disasters, EM-DAT (www.embat.be). Table 2 presents information on the sampled disasters, including casualties, affected populations, and data collection period.<sup>10</sup>

Our data comprise all tweets and retweets that were issued within the data timeline and contained relevant keywords.<sup>11</sup> The data set also provides rich metadata about the tweets and retweets, such as timestamps and profile statistics for the users that issued the tweets and retweets. We organized each tweet and its chain of retweets into cascades [39]. To qualify for our study, a cascade was required to have gained at least one retweet. We identified a tweet’s set of retweets as those messages that were created through Twitter’s official retweet function. We did not include retweets that were manually created by copying a tweet and adding “RT” at the beginning to signal a retweet. Additionally, we eliminated any cascades with text containing less than five words as tweets with too few words are difficult to extract meaning from [19]. Based on these considerations, we obtained a total of 106,609 cascades across all of the events in our sample. In each of the panels in Figure 2, we illustrate the number of cascades initiated over time for a specific disaster event.

Table 2. Sampled Disasters

<table><tr><td>Disaster</td><td>Location</td><td>Event Time (UTC)</td><td>End of Data (UTC)</td><td>Deaths*</td><td>Affected*</td></tr><tr><td>Joplin tornado</td><td>Joplin, MO, USA</td><td>5/22/2011 22:34</td><td>5/29/2011 23:59</td><td>176</td><td>1,150</td></tr><tr><td>Black Forest fire</td><td>Black Forest, CO, USA</td><td>6/11/2013 19:00</td><td>6/21/2013 23:59</td><td>2</td><td>1,617</td></tr><tr><td>Lac-Megantic rail disaster</td><td>Quebec, Canada</td><td>7/6/2013 05:15</td><td>7/10/2013 23:59</td><td>47</td><td>2,000</td></tr><tr><td>2014 Iquique earthquake</td><td>Iquique, Chile</td><td>4/1/2014 23:46</td><td>4/6/2014 23:59</td><td>6</td><td>513,837</td></tr></table>

Notes: \* Source: EM-DAT.

## Identifying Parallel Cascades

For each of the 106,609 cascades, we detected the parallel cascades from among all the other cascades in our data. To reiterate, a cascade’s set of parallel cascades constitutes other cascades conveying similar content. A cascade was not qualified to be a part of its own collection of parallel cascades. When identifying a cascade’s set of parallel cascades, it is possible that some of the parallel cascades started prior to the launch of the focal cascade. We allowed for this contingency as it is conceivable that the diffusion of a cascade is affected even before it begins by the spread of other cascades with similar content.

The content presented in a cascade and its parallel cascades should not vary greatly. We were interested in a narrow view of similarity so that each cascade and its associated parallel cascades represent fine-grained rather than broad topics. To build fine-grained topics, we applied near-duplicate detection techniques. Specifically, we utilized the SimHash algorithm developed by Charikar [13] to locate parallel cascades. SimHash has been applied previously to identify near-duplicates among Twitter content [72, 81]. We ran a Python implementation of SimHash (https://github.com/seomoz/simhash-py) for each disaster’s collection of cascades. This implementation generated a 64-bit fingerprint for each cascade in our sample to represent the content expressed in the cascade. For each cascade, its set of parallel cascades were cascades other than itself with fingerprints that differed from its own by 8 bits or less. Appendix A provides a technical discussion of SimHash and more details on our algorithm application. Table 3 provides examples of a cascade and one of its parallel cascades identified by the SimHash algorithm for each disaster.

(i)  
![](/api/attachments/5QZ8VNTD/fulltext/images/020b978640412cef8ff58363beef8f6e3b04481ddc68f51f486bcab7c69a2bea.jpg)

(ii)  
![](/api/attachments/5QZ8VNTD/fulltext/images/7b7f71ac762961d75ae3dd24828b6b2d396343ec151a4c958f3dfc9e865aeaa9.jpg)

(iii)  
![](/api/attachments/5QZ8VNTD/fulltext/images/becf464de538735e8facb83997c5d32ab314c6fd200c1dc996c5b99da52f1025.jpg)

(iv)  
![](/api/attachments/5QZ8VNTD/fulltext/images/31f2e39e1bec9dcf510500edb7957f4d88a0eca7af112ec1d637272ee104cee3.jpg)  
Figure 2. Count of Cascades Over TimeNotes: (i) Joplin tornado: 41,686 cascades. (ii) Black Forest fire: 15,772 cascades.(iii) Lac-Megantic rail disaster: 10,579 cascades. (iv) Iquique earthquake: 38,572 cascades.

Within a cascade’s group of parallel cascades, we also included any other cascades containing the exact same text. While not common, it is possible that users publish tweets that are exact-duplicates. Detecting perfect duplicates among cascades is a simple process that does not require the application of an algorithm like SimHash. Hence, a cascade’s collection of parallel cascades was composed of other cascades with near-duplicate content (if any) and exact-duplicate content (if any). Since our study is concerned with interactions between a cascade and its parallel cascades, we only retained cascades that matched with at least one parallel cascade. This reduced our sample from 106,609 cascades to 26,259 cascades. On average, a cascade in the reduced sample was associated with 6.962 parallel cascades.

## Model Estimation and Results

## Main Variables and Controls

We use the Twitter data from the four disasters and adopt the term $d = 1 , \ldots , D _ { \mathrm { { f } } }$ , where D = 4, for disasters. Cascades are exclusively associated with one event. The vector of parameters for cascade i to be estimated is $\boldsymbol { \theta } ^ { i } = \left( \mu ^ { i } , \gamma ^ { i } , \alpha _ { 1 } ^ { i } , \beta _ { 1 } ^ { i } , \dots , \alpha _ { 2 j } ^ { i } , \dots , \alpha _ { 2 J } ^ { i } , \beta _ { 2 } ^ { i } \right)$

Table 3. Examples of Parallel Cascades Identified by SimHash

<table><tr><td>Disaster</td><td>Cascade Text</td><td>Parallel Cascade Text</td></tr><tr><td>Joplin tornado</td><td>Help out my home state! You can text REDCROSS to 90999 to donate $10 to American Red Cross Disaster Relief in Joplin, MO</td><td>Please donate $10 to Disaster Relief efforts in Joplin, MO by texting REDCROSS to 90999</td></tr><tr><td>Black Forest fire</td><td>Sheriff now says about 38,000 people are evacuated from the #blackforestfire zone</td><td>Sheriff: 38,000 people evacuated, 13,000 homes</td></tr><tr><td>Lac-Megantic rail disaster</td><td>Train Carrying Crude Oil Derails in Quebec</td><td>Crude Oil-Carrying Train Derails And Explodes in Quebec Town</td></tr><tr><td>2014 Iquique earthquake</td><td>Earthquake strikes off the coast of Chile with a magnitude of 8.0.</td><td>There was an 8.0 magnitude earthquake off the coast of Chile just now</td></tr></table>

We estimated the parameters using maximum likelihood estimation. The parameters were estimated individually for each of the 26,259 cascades in our sample.

We treated time as a continuous variable since a continuous-time framework enables us to account for potential time effects [75]. The interval $[ 0 _ { d } ^ { i } , T _ { d } ^ { i } ]$ represents the observation period, or the data collection period for disaster d associated with cascade i. The term $0 _ { d } ^ { i }$ is evaluated as the value of zero and corresponds to the time when event $d$ transpired. We then measured $T _ { d } ^ { i }$ as the number of hours between $0 _ { d } ^ { i }$ and the end of data collection for the disaster d that cascade i is associated with (see Table 2 for details). The time that cascade i started $( t _ { 0 } ^ { i } )$ was computed as the difference in hours from when the tweet for i was released and $0 _ { d } ^ { i }$ . The times that the retweets materialized are summarized by $t _ { k } ^ { i }$ and $t _ { l } ^ { i j }$ . From the timestamp data provided for each retweet, we measured $t _ { k } ^ { i }$ as the number of hours elapsed between when retweet k for cascade i occurred and $t _ { 0 } ^ { i }$ . Similarly, $t _ { l } ^ { i j }$ was evaluated as the difference in hours from when retweet l for parallel cascade j transpired and $t _ { 0 } ^ { i } .$ .

Our model also controls for the time-varying level of chatter on Twitter for the disaster event associated with $\ : i \ : \left( \omega _ { t } ^ { i } \right) \ :$ . For this variable, we adopted a piecewise constant function where each spline is constant over one hour. The value of each spline was calculated as the natural log of the total number of tweets and retweets in our sample for the event $d$ that cascade i was associated with. Our approach is similar to Bowsher [6] and Lallouache and Challet [37], who also utilized a piecewise function as a part of their specification of the time-varying baseline intensity. Thus, we evaluated $\omega _ { t } ^ { i }$ as the logged level of chatter on Twitter for the relevant disaster during the hour that t occurred in. Our data also record the number of followers that retweeters possessed at the moment that they issued any retweets. We relied on the natural log of these counts to measure $\phi _ { t _ { k } ^ { i } }$ and $\phi _ { t _ { l } ^ { j } }$

## Estimation Procedure

We created counting measures $R ^ { i } ( t ) = \left\lceil R _ { 1 } ^ { i } ( t ) , \dots , R _ { j + 1 } ^ { i } ( t ) , \dots , R _ { J + 1 } ^ { i } ( t ) \right\rceil$ based on arrivals of retweets for i and each of $i \mathbf { \ ' } _ { \mathbf { S } }$ <sup>þ þ</sup>parallel cascades. Because the observation interval covered the entire data collection timeline, the counting measures for parallel cascades may have included points that arrived between $0 _ { d } ^ { i }$ and $t _ { 0 } ^ { i }$ or points that arrived after $t _ { K ^ { i } } ^ { i }$ . We maintained such realizations to account for the influence of parallel cascades’ retweets not only during but also before and after $i \ ' \mathrm { s }$ lifetime. The conditional intensity function for $i ,$ however, is technically null prior to $t _ { 0 } ^ { i }$ . Thus, we evaluated the conditional intensity function from $[ t _ { 0 } ^ { i } , T _ { d } ^ { i } ]$ . Given the realizations of $R ^ { i } ( t )$ during $[ t _ { 0 } ^ { i } , T _ { d } ^ { i } ]$ , the log-likelihood function for cascade i is:

$$
\overline {{\mathcal {L L}}} _ {i} = - \int_ {t _ {0} ^ {i}} ^ {T _ {d} ^ {i}} \tilde {\lambda} ^ {i} (t ^ {i} | \mathcal {H} _ {t} ^ {i}) d t + \sum_ {k = 1} ^ {K ^ {i}} \log \tilde {\lambda} ^ {i} (t _ {k} ^ {i} | H _ {t _ {k} ^ {i}} ^ {i}) - \rho \sum (\theta^ {i}) ^ {2},\tag{8}
$$

where $\tilde { \lambda } ^ { i } \left( t ^ { i } | \mathcal { H } _ { t } ^ { i } \right)$ is a nonlinear transformation of $\lambda ^ { i } \left( t | \mathcal { H } _ { t } ^ { i } \right)$ to guarantee that the conditional intensity is always positive. The third term in Eq. 8 is a penalty known as the L2 regularization element [28]. We incorporated a penalty to decrease the dimensions of the functional space that the parameters can be estimated from. Please refer to Appendix B for details regarding the likelihood and log-likelihood functions.

We maximized the penalized log-likelihood function for each of the cascades in Python. The tuning parameter for the penalty $( \rho )$ was set equal to the value of 0.01. To avoid local maxima, we provided five different vectors of starting values. We optimized the penalized log-likelihood function using the trust-region constrained algorithm developed by Byrd et al. [8]. The constraints for the optimization mirror those listed in the formulation of our model. Depending on the coefficients and data, it was sometimes hard to solve the integral analytically. In those cases, we approximated the integral with a quadrature rule.

## Estimation Results

Under this approach, we obtained estimates for the parameters of interest for every cascade. Due to space constraints, we do not present the parameter estimates for each cascade, but these are available upon request. The optimization algorithm was unable to converge or obtain parameter estimates within a reasonable amount of time for 1,011 cascades. This affected only 3.85 percent of the total number of cascades and reduced our sample to 25,248 cascades. Table 4 gives the descriptive statistics for the parameter estimates in $\theta ^ { i }$ across the 25,248 cascades. Appendix C breaks down the descriptive statistics in Table 4 by disaster. We also show descriptive statistics for variables in the point process model in Table 5.

According to Table 4, the mean value of $a _ { 1 } ^ { i }$ is 0.191 (standard error of the mean = $0 . 6 9 2 / \sqrt { 2 5 , 2 4 8 } = 0 . 0 0 4 )$ and the mean value of $a _ { 2 j } ^ { i }$ is -0.186 (standard error of the $\mathrm { m e a n } { = } 1 . 0 1 8 / \sqrt { 1 4 9 , 2 7 9 } = 0 . 0 0 3 )$ . These parameters respectively represent the effects of retweets for a cascade and for its parallel cascades on the cascade’s diffusion speed, controlling for the logged count of retweeters’ followers. The mean value of $a _ { 2 j } ^ { i }$ demonstrates that the effect of parallel cascades’ retweets on the intensity of a cascade tends to be negative. On average, a cascade’s diffusion rate is inhibited by the arrival of retweets for other cascades belonging to the same topic.

Table 4. Descriptive Statistics for Point Process Model Parameter Estimates

<table><tr><td></td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td><td>Obs.</td></tr><tr><td> $\alpha_{1}^{i}$ </td><td>0.191</td><td>4.6E-04</td><td>0.692</td><td>9.2E-14</td><td>38.855</td><td>25,248</td></tr><tr><td> $\beta_{1}^{i}$ </td><td>1.418</td><td>0.290</td><td>2.970</td><td>2.9E-06</td><td>74.509</td><td>25,248</td></tr><tr><td> $\alpha_{2j}^{i}$ </td><td>-0.186</td><td>-0.043</td><td>1.018</td><td>-14.767</td><td>21.478</td><td>149,279</td></tr><tr><td> $\beta_{2}^{i}$ </td><td>1.945</td><td>1.233</td><td>2.391</td><td>2.1E-05</td><td>36.768</td><td>25,248</td></tr><tr><td> $\mu^{i}$ </td><td>3.638</td><td>2.204</td><td>4.801</td><td>5.3E-13</td><td>116.565</td><td>25,248</td></tr><tr><td> $\gamma^{i}$ </td><td>3.660</td><td>3.356</td><td>2.546</td><td>4.4E-09</td><td>19.285</td><td>25,248</td></tr></table>

Table 5. Descriptive Statistics for Point Process Model Variables

<table><tr><td></td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td></tr><tr><td> $\omega_{t}^{i}$ </td><td>6.508</td><td>6.604</td><td>1.428</td><td>0.693</td><td>11.609</td></tr><tr><td> $\phi_{t_k}^{i}$ </td><td>5.513</td><td>5.521</td><td>1.682</td><td>0</td><td>16.332</td></tr><tr><td> $\phi_{t_l}^{i}$ </td><td>5.430</td><td>5.442</td><td>1.656</td><td>0</td><td>16.332</td></tr></table>

Thus, we find support for the Diffusion Inhibition Conjecture (C1a) and confirm the existence of an inhibiting interaction among cascades carrying similar content. However, the range for $a _ { 2 j } ^ { i }$ in Table 4 suggests that the parameter is positive for some parallel cascades. This indicates that the diffusion of some cascades is amplified by the spread of other cascades carrying similar content. We, consequently, also find support for the Diffusion Amplification Conjecture (C1b) and detect evidence of the existence of a positive interaction among cascades and their parallel cascades. The results from Table 4 reveal that the absolute value of the average value of $a _ { 2 j } ^ { i }$ is slightly smaller than that of $a _ { 1 } ^ { i }$ . Hence, the inhibiting effect of parallel cascades’ retweets on cascade intensity is weaker than the exciting effect of the cascade’s own retweets.

In Figures 3 and 4, we illustrate examples of cascades and their estimated intensities over time to visually represent an inhibiting and amplifying interaction. Both of the cascades were initiated during the Joplin tornado event and were linked with one parallel cascade each. The top panel of Figures 3 and 4 show the arrivals of retweets for the example’s cascade and its parallel cascade. The bottom panel of these figures depicts the conditional intensity over time based on the estimated parameters. Figure 3 demonstrates an inhibiting relationship. It can be clearly seen that the arrivals of retweets for the parallel cascade impose a negative and downward shift on the intensity.

(a) Arrival of retweets  
![](/api/attachments/5QZ8VNTD/fulltext/images/4ffd06aeb15361e4e408a4b7937be695092df6fe87db87204063c88aa9330634.jpg)

(b) Intensity over time based on estimated parameters  
![](/api/attachments/5QZ8VNTD/fulltext/images/19168af4e506eccf7a1341024241c2f04bd84540207dd5f5a08f49dfdb3c4a3f.jpg)  
Figure 3. Example of an Inhibiting Interaction

(a) Arrival of retweets  
![](/api/attachments/5QZ8VNTD/fulltext/images/ebfe3c09abd608a75e245c63ba98c5a0dd33a5ea01b358cce8c828a5dd1f066d.jpg)

(b) Intensity over time based on estimated parameters  
![](/api/attachments/5QZ8VNTD/fulltext/images/4ba36a31a1fb17544e5d75e7b2f62648bbce8bfea3222dbc19bf98a2cab4e578.jpg)  
Figure 4. Example of an Amplifying Interaction

This may be attributed to retweets for the parallel cascade occurring when retweets for the cascade are declining. In contrast, Figure 4 portrays an amplifying interaction. The cascade’s intensity experiences a small bump when retweets for the parallel cascade materialize. The interaction for this example may be positive as it appears that the arrivals of retweets for the parallel cascade help to usher in retweets for the cascade.

## Goodness-of-Fit Checks

We evaluated the goodness-of-fit of the estimated parameters from our point process model. For cascade $i ,$ this involved calculating for the series of retweet times $\left\{ t _ { 1 } ^ { i } , \dots , t _ { K ^ { i } } ^ { i } \right\}$ the time-deformed series of durations $\left\{ \xi _ { 1 } ^ { i } , \ldots , \xi _ { t _ { K ^ { i } } } ^ { i } \right\}$ (or residuals) as: $\xi _ { t _ { k } } ^ { i } = \int _ { t _ { k - 1 } i } ^ { t _ { k } ^ { i } } \hat { \lambda } ^ { i } ( u ) d u$ , where $\hat { \lambda } ^ { i }$ is the estimated intensity. The distribution of the residuals should be exponential with unit rate if our point process model accurately describes the data. This can be tested using the Kolmogorov-Smirnov (K-S) test, which is a hypothesis test for determining if a variable follows a given distribution. The null hypothesis of the K-S test states that the variable does follow the given distribution. Therefore, the null hypothesis of the K-S test that we used to evaluate the residuals states that the residuals are distributed exponentially with unit rate [37]. We calculated the residuals and ran the K-S test for each of the cascades in our sample. Figure 5 depicts the boxplot of p-values obtained from the K-S tests. It shows that for the vast majority of the cascades, we failed to reject the null hypothesis, which lends support to our fitted models. The p-value from the K-S test was less than 0.05, leading to rejection of the null hypothesis, for 1,178 cascades (or 4.67 percent of the total number of cascades). Given that nearly all of the fitted models demonstrated a good fit, we are confident that the specification of our model and the estimated parameters are valid.

![](/api/attachments/5QZ8VNTD/fulltext/images/8ade8b1dd63c222a251f8609866dff9970b1e791e34bc5651260eb313a35f8d1.jpg)  
Figure 5. Boxplot of p-Values from K-S Tests

As an additional check of the goodness-of-fit, we plotted the residuals against the exponential distribution with unit rate using a quantile-quantile (Q-Q) plot [37]. While we captured the p-values of each cascade’s K-S test in Figure 5, we are unable to show the Q-Q plots for each cascade due to the large sample size. As such, in Figure 6, we display the Q-Q plots of residuals for the ten largest cascades that passed the K-S test with a p-value greater than 0.05. The Q-Q plots in the figure generally demonstrate that the residuals follow an exponential distribution with unit rate. Any deviations from the exponential distribution appear to be driven by a very small minority of the residuals. Thus, we conclude that the Q-Q plots also support the goodness-of-fit of our models.

## Analysis of the Size of Cascade Producers

We proposed in the Larger Producer Advantage Conjecture (C2) that the diffusion of cascades by larger producers is more likely to be amplified by the diffusion of parallel cascades. In this section, we will focus on results we obtained related to C2. We tested C2 by running a regression model with the estimated parameter coefficients for $a _ { 2 j } ^ { i }$ as the dependent variable and the size of cascade producers as a predictor. For this analysis, our sample consisted of the 24,070 cascades with estimated parameters that demonstrated goodness-of-fit with a K-S test p-value greater than 0.05. Our data contain multiple observations within each cascade because a cascade can be associated with more than one parallel cascade. Producers can also initiate more than one cascade, resulting in repeated observations by the same producer. We utilized a random coefficient model due to the nested structure of our data. Because this model allows coefficients to vary across higher levels, it enables us to draw inferences about the relationships between the predictors and the dependent variable within and between cascades and producers [80].

![](/api/attachments/5QZ8VNTD/fulltext/images/e821b22b4d34ed5bb703d1b64d5ceb666f74ae3a5182ae1dcd9d4b1fa6f8f738.jpg)  
Figure 6. Q-Q Plots of Residuals for the Ten Largest Cascades

Overall, our data involve parallel cascades (Level-1) nested within cascades (Level-2), which are nested within producers (Level-3). Due to the disasters occurring during non-overlapping time periods, we treated producers participating in multiple disasters as separate. This affected 377 producers that generated cascades belonging to multiple disasters. As a result, the 24,070 cascades in our sample were created by 14,362 producers. As before, we denote cascades by $i = 1 , \ldots , I ,$ where I = 24,070 and the parallel cascades for i by $j = 1 , \dots , J .$ We now index producers by $h = 1 , \ldots , H ,$ , where $H = 1 4 { , } 3 6 2$

## Main Effects and Control Variables

The dependent variable is the effect of retweets for parallel cascade j on the spread of cascade i generated by producer h (now denoted as $\boldsymbol { a } _ { 2 _ { h i j } } )$ . We previously defined a producer’s size as the magnitude of her network of followers. As a result, we operationalized a producer’s size $( S i z e _ { h i } )$ as the count of followers that she was connected to at the time she initiated cascade i. To address nonlinearity, we applied a natural log transformation to producers’ counts of followers.

While the size of a producer may help determine $\boldsymbol { a } _ { 2 _ { h i j } }$ , it is important to also take into consideration the size of producers of the parallel cascades discussing similar content. In the context of apps, imitation apps of high-quality are capable of drawing consumers away from the original app [71]. Similarly, users may be more likely to favor and diffuse parallel cascades published by large producers since such producers are associated with releasing high-quality content [68]. Accordingly, we expect that the size of parallel cascades’ producers is negatively associated with the direction of the relationship between the diffusion of a cascade and the diffusion of its parallel cascades. To control for this, we included another independent variable that captures the size of parallel cascades’ producers. This variable $( S i z e P a r a l l e l _ { h i j } )$ was measured as the number of followers linked to the producer of cascade $i ^ { \flat } \mathbf { s } ~ j ^ { \mathrm { t h } }$ parallel cascade at the time j was launched. Due to potential nonlinearity, we also applied a natural log transformation to the follower counts of producers of parallel cascades.

Additionally, we controlled for the number of parallel cascades tied to a cascade $( V o l u m e _ { h i } )$ . The count of a cascade’s set of parallel cascades is important since parallel cascades may signal legitimacy of the content and induce an amplifying relationship [47]. At some point, however, a large amount of parallel cascades can overpower a cascade’s dissemination and lead to an inhibiting effect [26]. We captured this nonlinear effect by including a linear and a quadratic term for $V o l u m e _ { h i }$ . We meancentered $V o l u m e _ { h i }$ prior to creating the quadratic term to reduce multicollinearity. The next control variable accounts for the time when a producer releases a cascade relative to its parallel cascades. Producers are more successful at attracting attention towards content that is issued during, rather than before, the period of peak interest in a topic [14]. A first-mover advantage, therefore, may not exist. We controlled for this effect with a binary variable $( F i r s t M o \nu e r _ { h i } )$ that is set to 1 if the cascade is the first to be retweeted among its parallel cascades and 0 otherwise. Finally, we controlled for when in relation to the disaster the cascade was launched [78]. We measured this variable $( T i m e _ { h i } )$ as the number of hours between the time that cascade i was initiated and the time that the associated disaster materialized.

## Multi-Level Random Coefficients Model

Our random coefficient model is presented in Eq. 9. The size of producers for parallel cascades is a Level-1 variable since its values vary for each parallel cascade. The other predictors, including cascade producers’ size, are Level-2 variables because they are cascade-specific. That is, these predictors’ values change for each cascade. To aid in interpretation, we centered the continuous variables at their means.

$$
\begin{array}{l} \text {Level 1:} \alpha_ {2 _ {h i j}} = \gamma_ {h i 0} + \gamma_ {h i 1} L N \big (S i z e P a r a l l e l _ {h i j} \big) + \varepsilon_ {h i j} \\ \text {Level 2:} \gamma_ {h i 0} = \pi_ {h 0 0} + \pi_ {h 1 0} L N (S i z e _ {h i}) + \pi_ {h 2 0} V o l u m e _ {h i} + \pi_ {h 3 0} V o l u m e _ {h i} ^ {2} \\ \qquad + \pi_ {h 4 0} F i r s t M o v e r _ {h i} + \pi_ {h 5 0} T i m e _ {h i} + u _ {h i 0} \end{array}
$$

$$
\begin{array}{c} \text { Level   3 }: \pi_ {h 0 0} = \delta_ {0 0 0} + _ {h 0 0} \\ \pi_ {h 1 0} = \delta_ {0 1 0} + \in_ {h 1 0}, \end{array}\tag{9}
$$

$$
\text { where } \varepsilon_ {h i j} \sim N \big (0, \sigma_ {\varepsilon} ^ {2} \big), u _ {h i 0} \sim N \big (0, \sigma_ {u} ^ {2} \big), \text { and } \epsilon_ {h 0 0}, \epsilon_ {h 1 0} \sim N \bigg (0, \left[ \begin{array}{c c} \sigma_ {\epsilon_ {h 0 0}} ^ {2} & \sigma_ {\epsilon_ {h 1 0} \epsilon_ {h 0 0}} \\ \sigma_ {\epsilon_ {h 0 0} \epsilon_ {h 1 0}} & \sigma_ {\epsilon_ {h 1 0}} ^ {2} \end{array} \right] \bigg).
$$

In our random coefficient model from Eq. 9, the Level-1 equation includes the intercept $( \gamma _ { h i 0 } )$ , the Level-1 predictor, and an error term for the residual at the level of the parallel cascade $( \varepsilon _ { h i j } )$ . We allowed the intercept to be a random effect to capture differences across cascades regarding how their diffusion is affected by the spread of parallel cascades, on average. Thus, the Level-2 equation specifies the intercept as a function of two components: $\pi _ { h 0 0 }$ and $u _ { h i 0 }$ . The first term represents the overall cascade-level mean of $\alpha _ { 2 _ { h i j } }$ when parallel cascades’ producers are of average size. The second component is the variance of each cascade’s mean around the overall mean.

The Level-2 equation also includes the Level-2 predictors. The coefficients for these predictors represent the partial effects of a one unit change in the corresponding variables on the average $\alpha _ { 2 _ { h i j } }$ across a cascade’s set of parallel cascades. Finally, we allowed the Level-2 intercept and slope for $L n ( S i z e _ { h i } )$ to vary across producers. This is reflected in the Level-3 equations. The term δ<sub>000</sub> represents the overall producer-level mean of $\alpha _ { 2 _ { h i j } }$ when the Level-1 and Level-2 variables equal zero, or the means of continuous variables due to centering. The variable $\delta _ { 0 1 0 }$ represents the mean slope for $L n ( S i z e _ { h i } )$ across producers. Additionally, $\epsilon _ { h 0 0 }$ and $\epsilon _ { h 1 0 }$ capture the variance of producer-specific intercepts and slopes, respectively.

## Model Estimation and Robustness Checks for Producer Size Results

We provide descriptive statistics for the predictors in the random coefficient model in Table 6. Furthermore, we present the results from our random coefficient model in the first column of Table 7. We report the marginal $R ^ { 2 }$ and the conditional $R ^ { 2 }$ statistics for the random coefficient model in Table 7 as well. The marginal $R ^ { 2 }$ measures the proportion of variance explained by the fixed effects, and the conditional $R ^ { 2 }$ measures the proportion of variance explained by the full model, or the fixed plus random effects [34, 48].

The descriptive statistics in Table 6 show that the logged follower counts of the producers in our sample vary from 0 to 16.326. Thus, our sample comprises smaller, individual producers with limited audiences as well as larger producers with millions of followers. According to the first column of Table 7, the overall mean of $\boldsymbol { a } _ { 2 _ { h i j } }$ across producers is equal to −0.131. This result implies that producers’ cascades tend to suffer from an inhibiting relationship with their parallel cascades and supports the results from the estimation of our point process model. Our results also indicate that the intercepts vary significantly across producers with a variance of $\sigma _ { \epsilon _ { h 0 0 } } ^ { 2 } = 0 . 0 1 3$ and across cascades with a variance of $\sigma _ { u } ^ { 2 } = 0 . 0 7 3$

Table 6. Descriptive Statistics for Predictors

<table><tr><td>Variable</td><td>Description</td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td></tr><tr><td colspan="7">Parallel Cascade Level (137,613 observations)</td></tr><tr><td> $LN(SizeParallel_{ij})$ </td><td>Logged follower count for  $j$ &#x27;s producer</td><td>8.387</td><td>8.239</td><td>2.550</td><td>0</td><td>16.599</td></tr><tr><td colspan="7">Cascade Level (24,070 observations)</td></tr><tr><td> $LN(Size_i)$ </td><td>Logged follower count for  $i$ &#x27;s producer</td><td>8.111</td><td>7.957</td><td>2.395</td><td>0</td><td>16.326</td></tr><tr><td> $Volume_i$ </td><td>Count of parallel cascades</td><td>5.717</td><td>2</td><td>8.934</td><td>1</td><td>123</td></tr><tr><td> $FirstMover_i$ </td><td>Retweeted before parallel cascades</td><td>0.280</td><td>0</td><td>0.449</td><td>0</td><td>1</td></tr><tr><td> $Time_i$ </td><td>Hours away from start of disaster</td><td>31.239</td><td>18.121</td><td>36.921</td><td>0.056</td><td>244.024</td></tr></table>

<table><tr><td rowspan="2">Variable</td><td colspan="2">(1)Original Sample</td><td colspan="2">(2)Robustness Check #1</td><td colspan="2">(3)Robustness Check #2</td></tr><tr><td>Coeff.</td><td>SE</td><td>Coeff.</td><td>SE</td><td>Coeff.</td><td>SE</td></tr><tr><td>Intercept ( $\delta_{000}$ )</td><td>-0.131***</td><td>0.006</td><td>-0.169***</td><td>0.005</td><td>-0.148***</td><td>0.006</td></tr><tr><td> $LN(Size_{hi}) (\delta_{010})$ </td><td>0.018***</td><td>0.002</td><td>0.012***</td><td>0.001</td><td>0.016***</td><td>0.002</td></tr><tr><td> $LN(SizeParallel_{hij}) (\gamma_{hi1})$ </td><td>-0.023***</td><td>0.001</td><td>-0.012***</td><td>5.2E-04</td><td>-0.014***</td><td>0.001</td></tr><tr><td> $Volume_{hi} (\pi_{h20})$ </td><td>0.007***</td><td>3.6E-04</td><td>0.005***</td><td>2.5E-04</td><td>0.019***</td><td>8.0E-04</td></tr><tr><td> $Volume_{hi}^{2} (\pi_{h30})$ </td><td>-1.3E-04***</td><td>1.0E-05</td><td>-6.6E-05***</td><td>7.8E-06</td><td>-0.002***</td><td>1.2E-04</td></tr><tr><td> $FirstMover_{hi} (\pi_{h40})$ </td><td>-0.155***</td><td>0.010</td><td>0.055***</td><td>0.006</td><td>-0.112***</td><td>0.011</td></tr><tr><td> $Time_{hi} (\pi_{h50})$ </td><td>7.9E-04***</td><td>1.1E-04</td><td>9.2E-04***</td><td>6.7E-05</td><td>9.2E-04***</td><td>1.1E-04</td></tr><tr><td>Level-3 intercept var. ( $\sigma_{\epsilon_{h00}}^{2}$ )</td><td>0.013***</td><td>0.002</td><td>0.010***</td><td>9.9E-04</td><td>0.011***</td><td>0.002</td></tr><tr><td>Level-3 slope var. ( $\sigma_{\epsilon_{h10}}^{2}$ )</td><td>7.1E-04***</td><td>2.1E-04</td><td>4.3E-05***</td><td>2.3E-05</td><td>9.0E-04***</td><td>2.4E-04</td></tr><tr><td>Level-3 intercept-slope cov. ( $\sigma_{\epsilon_{h00}} \epsilon_{h10}$ )</td><td>0.003**</td><td>4.6E-04</td><td>-6.4E-04**</td><td>1.8E-04</td><td>0.003**</td><td>4.4E-04</td></tr><tr><td>Level-2 intercept var. ( $\sigma_{u}^{2}$ )</td><td>0.073***</td><td>0.003</td><td>0.054***</td><td>0.001</td><td>0.056***</td><td>0.003</td></tr><tr><td>Level-1 residual var. ( $\sigma_{\varepsilon}^{2}$ )</td><td>0.804***</td><td>0.003</td><td>0.141***</td><td>6.2E-04</td><td>0.893***</td><td>0.004</td></tr><tr><td>Observations</td><td>137,613</td><td></td><td>123,853</td><td></td><td>94,639</td><td></td></tr><tr><td>Marginal  $R^{2}$ </td><td>0.020</td><td></td><td>0.026</td><td></td><td>0.017</td><td></td></tr><tr><td>Conditional  $R^{2}$ </td><td>0.119</td><td></td><td>0.330</td><td></td><td>0.091</td><td></td></tr><tr><td colspan="7">Notes: Continuous variables are centered at their means. *p&lt; 0.1. **p&lt; 0.05. ***p&lt; 0.01.</td></tr></table>

Table 7. Results of Random Coefficient Model

Furthermore, the coefficient for $L n ( S i z e _ { h i } )$ is positive and significant. Holding all else constant, a cascade producer’s size is positively related to the average effect of parallel cascades’ retweets on the diffusion of her content. This implies that as the size of a producer’s network expands, she can increasingly expect the diffusion of her content to be boosted by the spread of similar content. Consequently, we find evidence that larger producers are more likely to enjoy amplification of their cascades’ diffusion by the spread of parallel cascades. This confirms the Larger Producer Advantage Conjecture (C2). The model results also suggest that the relationship between $\boldsymbol { a } _ { 2 _ { h i j } }$ and producers’ size at the time they launched each of their cascades differs across producers. The producers’ slopes for $L n ( S i z e _ { h i } )$ vary from the average slope $( \delta _ { 0 1 0 } = 0 . 0 1 8 )$ with a statistically significant variance of $\sigma _ { \epsilon _ { h 1 0 } } ^ { 2 } = 7 . 1 \mathrm { E } { - } 0 4$ (or a standard deviation of 0.027).

As a robustness check, we ensured that our results were not driven by extreme values for the dependent variable. We dropped observations where $\alpha _ { 2 _ { h i j } }$ was outside of the $5 ^ { \mathrm { t h } }$ and $9 5 ^ { \mathrm { t h } }$ percentile of the range for $\alpha _ { 2 _ { h i j } } .$ . This procedure reduced our sample from 137,613 to 123,853 observations. We reran the random coefficient model using the sample without outliers for $\alpha _ { 2 _ { h i j } } ,$ and the results of this robustness check are shown in the second column of Table 7. The results of the robustness check are mostly consistent with the results from the original sample. The only difference is that the coefficient for <sup>FirstMover</sup>i became positive and significant. So, producers that publish cascades that are first to be retweeted among those on the same topic are more likely to be amplified. Given the stability of the results from the original sample and the robustness check, our model seems robust to the removal of outliers for the dependent variable.

We conducted a second robustness check to verify that our results are not determined by the importance of the topic that a cascade belongs to. If a cascade discusses an important event or story, it is likely that there are many other users talking about the same topic. A cascade that discusses this topic will, thus, be associated with a higher number of parallel cascades. Consequently, the importance of the event or story behind a cascade may drive the number of its parallel cascades. This, in turn, may influence the effect that the diffusion of parallel cascades has on that of a cascade because, as argued in the development of C1a and C1b, the presence of parallel cascades can crowd out or reinforce a cascade’s diffusion.

For cascade i by producer h, we measured its number of parallel cascades with the variable $V o l u m e _ { h i }$ . To check that our results are not biased by the importance of the topic that a cascade belongs to, we eliminated the cascades with exceptionally high values for <sup>Volume</sup>hi. Specifically, we dropped the 1,145 cascades with values of $V o l u m e _ { h i }$ that exceeded the 95<sup>th</sup> percentile of this cascade-level variable. This reduced our sample to 94,639 observations. We then reran the random coefficient model specified in Equation 9. The results of this analysis are reported in the third column of Table 7 and are consistent with those reported from the original random coefficient model in the first column of Table 7. Therefore, our results do not appear to be driven by the importance of the topic that a cascade pertains to.

## Discussion

## Key Findings and Contributions

An inhibiting relationship for social media content emerges when a producer’s content diffusion is hindered by the successful propagation of similar content by competing producers. In contrast, an amplifying dynamic exists when content diffusion is elevated by the spread of other content on the topic. We evaluated the diffusion of similar content posted on social media platforms using Twitter data. We measured the diffusion of a cascade using the self-exciting point process model, which stipulates that the diffusion rate for a cascade increases each time the cascade is retweeted and decays as time passes between retweets. We expanded this model by incorporating additional point processes that represent the arrival of retweets for parallel cascades to evaluate how the dissemination of a cascade is affected by that of other cascades with similar content. We also allowed the effect of parallel cascades’ retweets on a cascade’s diffusion to hold positive and negative values to reflect an amplifying and inhibiting relationship.

The parameter estimates from our point process model reveal that a cascade’s diffusion is affected by the spread of similar content. On average, the interaction between a cascade and its parallel cascades is negative. This means that the spread of parallel cascades generally inhibits a cascade’s own diffusion. Our result contributes to the literature on the diffusion of social media content. For every cascade, we modeled the magnitude of influence from the diffusion of each parallel cascade with similar content. Our findings underscore the importance of accounting for the interaction among similar content. Because our results indicate the direction of the interplay is generally negative, assessments of cascade’s diffusion without incorporating parallel cascades may overestimate diffusion.

Moreover, we find variation with regard to a positive or a negative interaction among similar content since the spread of some cascades was amplified by their parallel cascades. Through a random coefficient model, we observe that cascade producers connected with larger networks on social media platforms are more likely to benefit from parallel cascades. This reveals an asymmetry between larger and smaller producers regarding the benefits from circulating similar content. Larger producers can be less concerned with publishing repetitive content. These producers include news organizations, government agencies, and humanitarian groups. In contrast, smaller producers, such as individual content creators and local organizations, should channel their efforts towards publishing distinct content. This may involve developing innovative content or presenting content that overlaps with other producers in a novel manner.

## Contributions for Humanitarian Organizations

Our setting of social media platforms during crises is important since these platforms have become critical communication tools in emergencies for disaster relief and the public. We offer several managerial implications for humanitarian organizations. First, our estimation results suggest the average magnitude of the selfexciting effect from a cascade’s own retweets is larger than that of retweets for parallel cascades. Therefore, humanitarian groups can enhance the diffusion of their cascades by sharing their social media content. The American Red Cross, with its digital volunteers (https://redcrosschat.org/digitalvolunteer/) may consider prioritizing the distribution of content among volunteers’ responsibilities. Also, diffusion of a piece of content tends to be inhibited by the diffusion of other similar content. Accordingly, a humanitarian organization that wants to increase the diffusion and visibility of its social media content should coordinate with others to minimize redundant content. This may be relevant to organizations that collaborate for relief efforts and tend to discuss related issues, such as humanitarian agencies belonging to the same United Nations cluster or a parent humanitarian organization and its local chapters.

## Limitations

Our study is not without limitations. We focused solely on retweets to assess the diffusion of a Twitter cascade. When our data were generated, retweets were the only user activity (other than tweets) consistently reported in a user’s followers’ feeds. Twitter now notifies users of other forms of user engagement, such as likes and replies. Future research can include other types of engagement when exploring diffusion of Twitter cascades using our point process model. Another limitation is that the magnitude of a cascade’s own retweets and parallel cascades’ retweets are marked only by retweeters’ counts of followers. However, the distance between a cascade’s producer and retweeters can affect a retweet’s effect on diffusion since cascades with a deeper network of retweeters are often perceived to be more viral [24]. Due to data limitations, we could not incorporate a measure of the distance between a cascade’s producer and retweeters.

The scope of our study’s analyses can be further broadened. Our model can be reestimated as a mutually exciting point process to measure cross-excitation and potential cross-inhibition effects between similar social media content. Future research can also investigate how publishing similar content affects other measures of a producer’s success, such as online revenues and number of followers. Our study does not perform content analysis outside of assessing similarity. For Twitter data related to humanitarian events, content can be classified as being informative and actionable (pertaining to donations, volunteering) versus informative and non-actionable (presenting damage and weather reports) [76]. After classifying cascades’ content, future research can determine what categories of content tend to experience inhibition versus amplification from the diffusion of similar content. We ran regression models to identify what factors are associated with the effects on a cascade’s diffusion by retweets of parallel cascades $( a _ { 2 j } ^ { i } )$ . A similar analysis can be performed for other parameters from our point process model, such as the baseline intensity $( \mu ^ { i } )$ and the self-exciting effect of a cascade’s own retweets $( a _ { 1 } ^ { i } )$ ). Such analysis will deepen our understanding of how a cascade’s properties facilitate its successful diffusion.

Finally, our data were obtained from the context of Twitter during sudden-onset humanitarian events. In this context, information expires rapidly due to the extreme uncertainty surrounding a disaster [45]. As a result, users may react urgently and retweet disaster-related content quickly. As the events in our sample occurred without warning, the shock coupled with the social impact may also drive a surge in users’ attention for related content. Prior studies have observed this pattern after an unexpected crisis [49]. The disasters in our sample were newsworthy events as well since they affected many individuals. Thus, large organizations (news organizations, humanitarian agencies) were among the cascade producers in our sample. These attributes of our context may limit the generalizability of our results to contexts with the same conditions.

## Conclusions

In this study, we examine how the diffusion for social media content is affected by the concurrent diffusion of other similar content. Our goal is to understand whether producers should release redundant information or avoid doing so in order to enhance the diffusion of their content. To evaluate the diffusion of a piece of content, we expanded the self-exciting point process in a novel manner to include additional point processes for retweets of other strands of similar content. By doing so, we recognize that content does not diffuse in isolation on social media platforms and add to the emerging literature on the interdependence of the diffusion of social media content. We find that content similarity tends to inhibit diffusion and that content producers connected with smaller networks should be especially wary of releasing repetitive content. Therefore, our study sheds light on the competitive dynamics related to the diffusion of social media content and highlights the importance of assessing content similarity when measuring diffusion.

Our point process model development approach can be used in other contexts that demonstrate a competitive dynamic. For example, Xu et al. [75] investigated the cumulative effect of clicking online advertisements for a product on purchase decisions. Supplemental point processes can be added to reflect clicks on ads for competing products to analyze how consumers’ purchase decisions are impacted by their interests, via clicks, for competing products. Instead of clicks on online ads, a point process model can also be developed for price changes and promotions for a product and its rivals. Researchers can then analyze how consumers react to price changes and estimate the extent to which purchase decisions are a function of price for a product and its competitors. Overall, our extension of the self-exciting point process can be generalized to a variety of contexts that exhibit competitive dynamics.

Acknowledgements: We would like to thank the guest editors of this Special Section, Rob Kauffman and Thomas Weber, for their invaluable feedback and guidance through the review process. We would also like to acknowledge and thank three anonymous reviewers for their insightful comments. We are grateful to seminar participants at Boston College (2019), Boston University (2019), Hong Kong University of Science and Technology (2019), Pennsylvania State University (2019), Shanghai Jiaotong University (2019), Singapore Management University (2019), University of Texas at Dallas (2019), and Tel Aviv University (2019). We also thank the conference participants at CIST 2018 and the SITES minitrack at HICSS 2019, as well as three anonymous reviewers for HICSS 2019. This work was supported by the Center for Services Leadership, the Office of Knowledge Enterprise Development at Arizona State University, and the AWS Cloud Credits for Research Program.

## NOTES

1. In reality, multiple producers often publish similar content. In such cases, a piece of content cannot be viewed in isolation as its information overlaps with that presented in other pieces of content.

2. This is an important objective: if diffusion of a piece of content is influenced by the diffusion of similar content, then prior evaluations of content diffusion may be incomplete. Our study recognizes that social media content does not exist in a vacuum, a perspective that better mirrors the reality of social media platforms as an online space teeming with usergenerated content.

3. We focus on this compelling context for the following reasons. During these events, information is perishable due to extreme environmental uncertainty and volatility where the events unfold [45]. Therefore, it is critical to understand the factors that facilitate rapid diffusion of information. Second, due to their sudden nature, the amount of relevant social media content surges and competition for users’ attention to event-related content becomes particularly acute.

4. Larger producers are more immune to negative impacts on the diffusion of their content from that of similar content and are more likely to benefit from redundant content diffusion. The advantage of being a large, well-connected producer has been documented [67]. We offer nuanced insights by showing that content diffusion of larger producers may be superior due to these producers’ credibility and reputation and their ability to profit from the propagation of similar content. For smaller producers, however, our results indicate that the diffusion of their content is more susceptible to inhibition by the spread of similar content.

5. Our point process model is not precisely a causal model, but it examines content sharing across time and assesses how a user sharing a piece of social media content impacts other users’ decisions to also share in the future. Thus, our study infers causality in the sense of Granger causality and deepens our understanding of social media content diffusion over time.

6. For cable news shows, greater amounts of social media activity about one show leads to a reduction in viewership for competing shows [61]. Therefore, social media can serve to reinforce and intensify competition for attention among organizations.

7. For example, the self-exciting point process is conducive to analyzing activity by developers on open source projects. This is because developer activity tends to be correlated such that a change to a project’s source code can trigger additional changes [62]. The selfexciting point process is also appropriate to model online auction bidding on sites like eBay since a user’s submission of a bid often motivates other users to submit bids as well [11].

8. We would like to thank Rob Kauffman, co-editor of this Special Section, for the recommendation to refer more appropriately to our arguments as conjectures. Because the theoretical underpinnings are still developing, we argue for both directions of the effect of the diffusion of parallel cascades on the diffusion of a cascade. Therefore, it is premature to label our arguments as hypotheses and is more proper to refer to them as conjectures.

9. Our model can be applied to diffusion of content on other social media platforms that promote content sharing as a feature too.

10. We specified the date ranges that we were interested in as starting from the time the disaster materialized to approximately the end of the initial response period. Humanitarian organizations normally view the first 72 hours after an emergency as the most critical response period. Hospitals are suggested to be prepared for up to 96 hours as the initial response period following a disaster [66]. Therefore, we estimated the end of the initial response period as four days after the date EM-DAT recorded as the end of the disaster. The only exception to this rule was the Black Forest fire event. Because this event was relatively more protracted than the other three events, we ended data collection on the date that the fire was publicly reported to be 100 percent contained.

11. We submitted to WeLink a set of queries specific to each disaster event. These queries contained keywords and phrases that were commonly present in hashtags and content associated with the emergencies as well as combinations of the location of the disaster and event name [52].

## REFERENCES

1. Aral, S.; and Walker, D. Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Science, 57, 9 (August 2011), 1623–1639.

2. Asur, S.; Huberman, B.A.; Szabo, G.; and Wang, C. Trends in social media: Persistence and decay. In Proc. Fifth Intl. AAAI Conference on Weblogs and Social Media. Barcelona, Spain: The AAAI Press, 2011, pp. 434–437.

3. Bacry, E.; and Muzy, J.-F. Hawkes model for price and trades high-frequency dynamics. Quantitative Finance, 14, 7 (July 2014), 1147–1166.

4. Bakshy, E.; Hofman, J.M.; Mason, W.A.; and Watts, D.J. Everyone’s an influencer: Quantifying influence on Twitter. In Proc. Fourth ACM Intl. Con. on Web Search and Data Mining. Hong Kong: Association for Computing Machinery, 2011, pp. 65–74.

5. Berger, J.; and Milkman, K.L. What makes online content viral? Journal of Marketing Research, 49, 2 (April 2012), 192–205.

6. Bowsher, C.G. Modelling security market events in continuous time: Intensity based, multivariate point process models. Journal of Econometrics, 141, 2 (December 2007), 876–912.

7. Bremaud, P.; and Massoulie, L. Stability of nonlinear Hawkes processes. The Annals of Probability, 24, 3 (July 1996), 1563–1588.

8. Byrd, R.; Schnabel, R.; and Shultz, G. A trust region algorithm for nonlinearly constrained optimization. SIAM Journal on Numerical Analysis, 24, 5 (October 1987), 1152–1170.

9. Centola, D. The spread of behavior in an online social network experiment. Science, 329, 5996 (September 2010), 1194–1197.

10. Centola, D.; and Macy, M. Complex contagions and the weakness of long ties. American Journal of Sociology, 113, 3 (November 2007), 702–734.

11. Chan, N.H.; Li, Z.R.; and Yau, C.Y. Forecasting online auctions via self-exciting point processes. Journal of Forecasting, 33, 7 (November 2014), 501–514.

12. Chang, R.M.; Kauffman, R.J.; and Kwon, Y. Understanding the paradigm shift to computational social science in the presence of big data. Decision Support Systems, 63, (July 2014), 67–80.

13. Charikar, M.S. Similarity estimation techniques from rounding algorithms. In Proc. Thirty-fourth ACM Symp. on Theory of Computing. Montreal: Association for Computing Machinery, 2002, pp. 380–388.

14. Ciampaglia, G.L.; Flammini, A.; and Menczer, F. The production of information in the attention economy. Scientific Reports, 5, (May 2015), 9452.

15. Coscia, M. Average is boring: How similarity kills a meme’s success. Scientific Reports, 4, (September 2014), 6477.

16. Coscia, M. Popularity spikes hurt future chances for viral propagation of protomemes. Communications of the ACM, 61, 1 (January 2018), 70–77.

17. Crane, R.; and Sornette, D. Robust dynamic classes revealed by measuring the response function of a social system. Proc. of the National Academy of Sciences, 105, 41 (October 2008), 15649–15653.

18. Daley, D.J.; and Vere-Jones, D. An Introduction to the Theory of Point Processes: Volume I: Elementary Theory and Methods. New York: Springer-Verlag, 2003.

19. Davidov, D.; Tsur, O.; and Rappoport, A. Enhanced sentiment learning using Twitter hashtags and smileys. In Proc. 23rd Intl. Con. on Computational Linguistics: Posters. Stroudsburg, PA: Association for Computational Linguistics, 2010, pp. 241–249.

20. Dellarocas, C. The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Science, 49, 10 (October 2003), 1407–1424.

21. Dellarocas, C.; Sutanto, J.; Calin, M.; and Palme, E. Attention allocation in information-rich environments: The case of news aggregators. Management Science, 62, 9 (September 2015), 2543–2562.

22. Dumais, S.T. Latent semantic analysis. Annual Rev. Info. Sci. Tech., 38, 1 (September 2004), 188–230.

23. Falkinger, J. Attention economies. Journal of Economic Theory, 133, 1 (March 2007), 266–294.

24. Goel, S.; Anderson, A.; Hofman, J.; and Watts, D.J. The structural virality of online diffusion. Management Science, 62, 1 (January 2016), 180–196.

25. Goes, P.B.; Lin, M.; and Au Yeung, C. “Popularity effect” in user-generated content: Evidence from online product reviews. Information Systems Research, 25, 2 (January 2014), 222–238.

26. Haas, M.R.; Criscuolo, P.; and George, G. Which problems to solve? Online knowledge sharing and attention allocation in organizations. Academy of Management Journal, 58, 3 (June 2015), 680–711.

27. Hansen, M.T.; and Haas, M.R. Competing for attention in knowledge markets: Electronic document dissemination in a management consulting company. Admin. Sci. Qtrly., 46, 1 (March 2001), 1–28.

28. Hastie, T.; Tibshirani, R.; and Friedman, J. The Elements of Statistical Learning: Data Mining, Inference, and Prediction. New York: Springer Science & Business Media, 2009.

29. Hawkes, A.G. Spectra of some self-exciting and mutually exciting point processes. Biometrika, 58, 1 (September 1971), 83–90.

30. Hawkes, A.G.; and Oakes, D. A cluster process representation of a self-exciting process. Journal of Applied Probability, 11, 3 (September 1974), 493–503.

31. Hodas, N.O.; and Lerman, K. The simple rules of social contagion. Scientific Reports, 4, (March 2014), 4343.

32. Huang, N.; Burtch, G.; Gu, B.; Hong, Y.; Liang, C.; Wang, K.; Fu, D.; and Yang, B. Motivating user-generated content with performance feedback: Evidence from randomized field experiments. Management Science, 65, 1 (February 2018), 327–345.

33. Iyer, G.; and Katona, Z. Competing for attention in social communication markets. Management Science, 62, 8 (May 2015), 2304–2320.

34. Johnson, P.C.D. Extension of Nakagawa & Schielzeth’s R2GLMM to random slopes models. Methods in Ecology and Evolution, 5, 9 (September 2014), 944–946.

35. Kajiwara, T.; Bollegala, D.; Yoshida, Y.; and Kawarabayashi, K. An iterative approach for the global estimation of sentence similarity. PLOS One, 12, 9 (September 2017), e0180885.

36. Kryvasheyeu, Y.; Chen, H.; Obradovich, N.; Moro, E.; Van Hentenryck, P.; Fowler, J.; and Cebrian, M. Rapid assessment of disaster damage using social media activity. Science Advances, 2, 3 (March 2016), e1500779.

37. Lallouache, M.; and Challet, D. The limits of statistical significance of Hawkes processes fitted to financial data. Quantitative Finance, 16, 1 (January 2016), 1–11.

38. Lee, D.; Hosanagar, K.; and Nair, H.S. Advertising content and consumer engagement on social media: Evidence from Facebook. Management Science, 64, 11 (January 2018), 5105–5131.

39. Lerman, K.; and Ghosh, R. Information contagion: An empirical study of the spread of news on Digg and Twitter social networks. In Proceedings of the Fourth International AAAI Conference on Weblogs and Social Media. Washington, DC: The AAAI Press, 2010, pp. 90–97.

40. Luo, X.; Gu, B.; Zhang, J.; and Phang, C.W. Expert blogs and consumer perceptions of competing brands. MIS Quarterly, 41, 2 (June 2017), 371–395.

41. Luo, X.; and Zhang, J. How do consumer buzz and traffic in social media marketing predict the value of the firm? Journal of Management Information Systems, 30, 2 (Fall 2013), 213–238.

42. Manku, G.S.; Jain, A.; and Das Sarma, A. Detecting near-duplicates for web crawling. In Proceedings of the 16th International Conference on World Wide Web. Banff, Canada: Assoc. for Computing Machinery, 2007, pp. 141–150.

43. Mayzlin, D.; and Yoganarasimhan, H. Link to success: How blogs build an audience by promoting rivals. Management Science, 58, 9 (July 2012), 1651–1668.

44. Mei, H.; and Eisner, J.M. The neural Hawkes process: A neurally self-modulating multivariate point process. In Advances in Neural Info. Processing Systems 30. Long Beach, CA: 2017, pp. 6754–6764.

45. Meier, P. Digital Humanitarians: How Big Data Is Changing the Face of Humanitarian Response. Boca Raton: CRC Press, 2015.

46. Mohler, G.O.; Short, M.B.; Brantingham, P.J.; Schoenberg, F.P.; and Tita, G.E. Selfexciting point process modeling of crime. Journal of the American Stat. Assoc., 106, 493 (March 2011), 100–108.

47. Myers, S.A.; and Leskovec, J. Clash of the contagions: Cooperation and competition in information diffusion. In Proceedings of the 2012 IEEE 12th International Conference on Data Mining. Brussels: IEEE, 2012, pp. 539–548.

48. Nakagawa, S.; and Schielzeth, H. A general and simple method for obtaining R2 from generalized linear mixed-effects models. Methods in Ecology and Evolution, 4, 2 (February 2013), 133–142.

49. Nan, N.; and Lu, Y. Harnessing the power of self-organization in an online community during organizational crisis. MIS Quarterly, 38, 4 (December 2014), 1135–1157.

50. Ogata, Y. Statistical models for earthquake occurrences and residual analysis for point processes. Journal of the American Statistical Association, 83, 401 (March 1988), 9–27.

51. Oh, O.; Agrawal, M.; and Rao, H.R. Community intelligence and social media services: A rumor theoretic analysis of tweets during social crises. MIS Quarterly, 37, 2 (June 2013), 407–426.

52. Olteanu, A.; Vieweg, S.; and Castillo, C. What to expect when the unexpected happens: Social media communications across crises. In Proceedings of the 18th ACM Conference on Computer Supported Cooperative Work & Social Computing. Vancouver, Canada: Association for Computing Machinery, 2015, pp. 994–1009.

53. Phan, T.Q.; and Airoldi, E.M. A natural experiment of social network formation and dynamics. Proceedings of the National Academy of Sciences, 112, 21 (May 2015), 6595–6600.

54. Phang, D.C.W.; Wang, K.; Wang, Q.; Kauffman, R.J.; and Naldi, M. How to derive causal insights for digital commerce in China? A research commentary on Computational Social Science methods. Electronic Commerce Research and Applications, 33 (January-February 2019), 100837.

55. Pi, B.; Fu, S.; Wang, W.; and Han, S. SimHash-based effective and efficient detecting of near-duplicate short messages. In Proceedings of the Second Symposium International

Computer Science and Computational Technology. Huangshan China: Academy Publisher, 2009, pp. 20–25.

56. Qiu, L.; Tang, Q.; and Whinston, A.B. Two formulas for success in social media: Learning and network effects. Journal of Management Information Systems, 32, 4 (Fall 2015), 78–108.

57. Reynaud-Bouret, P.; and Schbath, S. Adaptive estimation for Hawkes processes: Application to genome analysis. The Annals of Statistics, 38, 5 (October 2010), 2781–2822.

58. Rishika, R.; Kumar, A.; Janakiraman, R.; and Bezawada, R. The effect of customers’ social media participation on customer visit frequency and profitability: An empirical investigation. Information Systems Research, 24, 1 (December 2012), 108–127.

59. Romero, D.M.; Galuba, W.; Asur, S.; and Huberman, B.A. Influence and passivity in social media. In D. Gunopulos; T. Hofmann; D. Malerba; and M. Vazirgiannis (eds.), Machine Learning and Knowledge Discovery in Databases. Berlin, Heidelberg: Springer, 2011, pp. 18–33.

60. Romero, D.M.; Meeder, B.; and Kleinberg, J. Differences in the mechanics of information diffusion across topics: Idioms, political hashtags, and complex contagion on Twitter. In Proceedings of the 20th International Conference on World Wide Web. New York, NY: Association for Computing Machinery, 2011, pp. 695–704.

61. Sabnis, G.; and Grewal, R. Cable news wars on the internet: Competition and user-generated content. Information Systems Research, 26, 2 (June 2015), 301–319.

62. Saichev, A.; Maillart, T.; and Sornette, D. Hierarchy of temporal responses of multivariate self-excited epidemic processes. The European Physical Journal B, 86, 4 (April 2013), 124.

63. Shen, W.; Hu, Y.J.; and Rees Ulmer, J. Competing for attention: An empirical study of online reviewers’ strategic behavior. MIS Quarterly, 39, 3 (September 2015), 683–696.

64. Shore, J.; Baek, J.; and Dellarocas, C. Network structure and patterns of information diversity on Twitter. MIS Quarterly, 42, 3 (September 2018), 849–872.

65. Stieglitz, S.; and Dang-Xuan, L. Emotions and information diffusion in social media— Sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29, 4 (Spring 2013), 217–248.

66. Stratton, S.J.; and Tyler, R.D. Characteristics of medical surge capacity demand for sudden-impact disasters. Academic Emergency Medicine, 13, 11 (November 2006), 1193–1197.

67. Susarla, A.; Oh, J.H.; and Tan, Y. Social networks and the diffusion of user-generated content: Evidence from YouTube. Information Systems Research, 23, 1 (April 2011), 23–41.

68. Tang, Q.; Gu, B.; and Whinston, A.B. Content contribution for revenue sharing and reputation in social media: Dynamic structural model. Journal of Management Information Systems, 29, 2 (Fall 2012), 41–76.

69. Vieweg, S.; Hughes, A.L.; Starbird, K.; and Palen, L. Microblogging during two natural hazards events: What Twitter may contribute to situational awareness. In Proc. SIGCHI Conference on Human Factors in Computing Systems. Atlanta, GA: Association for Computing Machinery, 2010, pp. 1079–1088.

70. Vosoughi, S.; Roy, D.; and Aral, S. The spread of true and false news online. Science, 359, 6380 (March 2018), 1146–1151.

71. Wang, Q.; Li, B.; and Singh, P.V. Copycats vs. original mobile apps: A machine learning copycat-detection method and empirical analysis. Information Systems Research, 29, 2 (April 2018), 273–291.

72. Wang, Y.; Wu, C.; Zheng, K.; and Wang, X. Social bot detection using tweets similarity. In R. Beyah; B. Chang; Y. Li; and S. Zhu (eds.), Security and Privacy in Communication Networks. Singapore: Springer International Publishing, 2018, pp. 63–78.

73. Weng, L.; Flammini, A.; Vespignani, A.; and Menczer, F. Competition among memes in a world with limited attention. Scientific Reports, 2, (March 2012), 335.

74. Wu, F.; and Huberman, B.A. Novelty and collective attention. Proceedings of the National Academy of Sciences, 104, 45 (November 2007), 17599–17601.

75. Xu, L.; Duan, J.A.; and Whinston, A.B. Path to purchase: A mutually exciting point process model for online advertising and conversion. Management Science, 60, 6 (April 2014), 1392–1412.

76. Yan, L.; and Pedraza-Martinez, A.J. Social media for disaster management: Operational value of the social conversation. Production and Operations Management, Forthcoming (2019).

77. Yoganarasimhan, H. Impact of social network structure on content propagation: A study using YouTube data. Quantitative Marketing and Economics, 10, 1 (March 2012), 111–150.

78. Yoo, E.; Rand, W.; Eftekhar, M.; and Rabinovich, E. Evaluating information diffusion speed and its determinants in social media networks during humanitarian crises. J. Ops. Mgmt., 45, (July 2016), 123–133.

79. Zhao, Q.; Erdogdu, M.A.; He, H.Y.; Rajaraman, A.; and Leskovec, J. SEISMIC: A self-exciting point process model for predicting tweet popularity. In Proc. 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, Sydney, Australia, 2015, pp. 1513–1522.

80. Zheng, Z.; Pavlou, P.A.; and Gu, B. Latent growth modeling for information systems: Theoretical extensions and practical applications. Information Systems Research, 25, 3 (August 2014), 547–568.

81. Zhu, X.; Huang, J.; Zhou, B.; Li, A.; and Jia, Y. Real-time personalized Twitter search based on semantic expansion and quality model. Neurocomputing, 254, (September 2017), 13–21.

## Appendix A SimHash Algorithm

We utilized the SimHash algorithm, a near-duplicate detection technique, to identify for each cascade a set of parallel cascades with similar content. SimHash is a dimensionality reducing algorithm that creates one B-bit fingerprint to represent a document. A document was the text of the tweet that started a cascade. To implement the algorithm, we did this for each cascade. First, we maintained a vector V of length B, and each element of this vector was initialized to 0. The subsequent step of the algorithm was to calculate a B-bit binary hash for every document feature. We tokenized cascades’ text into words and submitted word tokens as features. Binary hash values equal to 1 were treated as 1, and binary hash values equal to 0 were treated as equal to -1. For <sup>b</sup> 1; . . . ; <sup>B</sup>, we summed the hash values in the bth bit across the tokens, and we set the bth element of V equal to this sum. Negative sums in V were recorded as 0 while positive sums in V were marked as 1. The fingerprint of the cascade’s text is equal to V.

Before applying the SimHash algorithm, we preprocessed the text from each cascade using standard natural language processing techniques. First, we converted the cascade’s text to lowercase and removed all punctuation marks. We stripped the text of URLs and emojis, but preserved hashtags as long as they did not match the keywords and phrases that we used in our data collection queries. Also, we eliminated stop words, common, short function words (“and,” “the,” “which”). We reduced variation in producers’ spelling by modifying words with characters repeated more than three times to having the characters repeated only three times in a row (“hahaaaa” to “hahaaa”).

The algorithm is fast and scales linearly with the number of cascades. This algorithm is useful for finding near-duplicates because it produces similar hashes for similar content. Textual similarity can be efficiently evaluated by comparing a cascade’s fingerprint with that of another cascade using the Hamming distance. The Hamming distance is measured as the number of differing bits between two cascade’s fingerprints [42]. For each cascade, its set of parallel cascades constituted cascades other than itself with a Hamming distance of 8 bits or less.

A concern is the performance of SimHash given that some tweets contain short and noisy text. SimHash is well-known for successfully detecting near-duplicates among longer documents, as evidenced by Google’s usage of SimHash to find nearduplicate web pages [42]. Researchers have also found that SimHash is an effective algorithm for detecting near-duplicates for short text, such as short online messages in Chinese [55] and individual sentences [35]. The SimHash algorithm has been used to identify near-duplicate tweets as well [72, 81]. In particular, Wang et al. [72] compare the performance of SimHash at detecting similar tweets against that of two other algorithms. The authors found that SimHash is slightly less accurate at this task than the best-performing algorithm, which relies on latent semantic analysis. However, latent semantic analysis is known to be computationally expensive and difficult to scale [22]. Because SimHash has been shown to be capable of handling near-duplicate detection for tweets and other short text, we leveraged this algorithm to identify the parallel cascades of each cascade in our study.

Another limitation of SimHash is that this algorithm analyzes the similarity of text but does not account for semantics. There may be cases where two pieces of text are phrased similarly but a difference of one or two words causes the two pieces of text to have a different meaning and address two different topics. Because SimHash is designed to assess the similarity of text, the algorithm may identify such cases as being similar and belonging to the same topic. As noted previously, SimHash is a fast and scalable algorithm, and this is in part due to the algorithm not parsing differences in semantics. Nevertheless, we would like to raise awareness about this issue as a potential limitation of SimHash when identifying similar content.

## Appendix B Likelihood and Log-Likelihood Functions for the Point Process Model

Given the realizations of $R ^ { i } ( t )$ during $\left[ t _ { 0 } ^ { i } , T _ { d } ^ { i } \right]$ , the likelihood function for cascade i is [18]:

$$
\mathcal {L} _ {i} = \left[ \sum_ {k = 1} ^ {K ^ {i}} \lambda^ {i} \left(t _ {k} ^ {i} | \mathcal {H} _ {t _ {k} ^ {i}} ^ {i}\right) \right] * \exp \left(- \int_ {t _ {0} ^ {i}} ^ {T _ {d} ^ {i}} \lambda^ {i} (t | \mathcal {H} _ {t} ^ {i}) d t\right)
$$

Recall that we extended the traditional self-exciting point process by including additional point processes for retweets of parallel cascades and by permitting $a _ { 2 j } ^ { i }$ to impose a negative effect on the intensity. After summing over the history of the cascade, it is possible that the intensity at t becomes negative if at least one $a _ { 2 j } ^ { i }$ takes on a negative value. By definition, $\lambda ^ { i } \left( t | \mathcal { H } _ { t } ^ { i } \right)$ must be positive [18]. We guaranteed that the intensity is always non-negative by executing the following nonlinear specification of our model that was also applied in Bremaud and Massoulie [7] and Reynaud-Bouret and Schbath [57]: $\widetilde { \lambda } ^ { i } \left( t | \mathcal { H } _ { t } ^ { i } \right) = \operatorname* { m a x } \left( \lambda ^ { i } \left( t | \mathcal { H } _ { t } ^ { i } \right) , \eta \right)$ , where η equals the smallest positive decimal number in Python. Under the nonlinear specification, the likelihood function for i is:

$$
\tilde {\mathcal {L}} _ {i} = \left[ \sum_ {k = 1} ^ {K ^ {i}} \tilde {\lambda} ^ {i} \left(t _ {k} ^ {i} | \mathcal {H} _ {t _ {k} ^ {i}} ^ {i}\right) \right] * \exp \left(- \int_ {t _ {0} ^ {i}} ^ {T _ {d} ^ {i}} \tilde {\lambda} ^ {i} (t | \mathcal {H} _ {t} ^ {i}) d t\right)
$$

The log-likelihood to estimate $\theta ^ { i }$ given the observed data for cascade i is:

$$
\begin{array}{c} \mathcal {L L} _ {i} = - \int_ {t _ {0} ^ {i}} ^ {T _ {d} ^ {i}} \tilde {\lambda} ^ {i} (t ^ {i} | \mathcal {H} _ {t} ^ {i}) d t + \int_ {t _ {0} ^ {i}} ^ {T _ {d} ^ {i}} \log \tilde {\lambda} ^ {i} (t _ {k} ^ {i} | \mathcal {H} _ {t _ {k} ^ {i}} ^ {i}) d R _ {1} (t) \\ = - \int_ {t _ {0} ^ {i}} ^ {T _ {d} ^ {i}} \tilde {\lambda} ^ {i} (t ^ {i} | \mathcal {H} _ {t} ^ {i}) d t + \sum_ {k = 1} ^ {K ^ {i}} \log \tilde {\lambda} ^ {i} (t _ {k} ^ {i} | \mathcal {H} _ {t _ {k} ^ {i}} ^ {i}) \end{array}
$$

To reduce the dimensions of the functional space that the parameters can be estimated from, we used a penalized maximum likelihood function [57]. We imposed the L2 regularization technique, which is also known as a ridge regression. The L2 regularization technique shrinks estimations of parameters as it penalizes the parameters based on their size. The penalty is equal to the tuning parameter, $\rho ,$ multiplied by the sum of the squared coefficients. The tuning parameter controls the amount of the penalty such that a larger tuning parameter leads to a higher penalty and more shrinkage [28]. The penalized log-likelihood function we estimated for i is:

$$
\overline {{{{\mathcal {L L}}}}} _ {i} = - \int_ {t _ {0} ^ {i}} ^ {T _ {d} ^ {i}} \tilde {\lambda} ^ {i} (t ^ {i} | \mathcal {H} _ {t} ^ {i}) d t + \sum_ {k = 1} ^ {K ^ {i}} \log \tilde {\lambda} ^ {i} (t _ {k} ^ {i} | \mathcal {H} _ {t _ {k} ^ {i}} ^ {i}) - \rho \sum^ {(\theta^ {i}) ^ {2}}
$$

Appendix C Breakdown of Parameter Estimates by Disaster

<table><tr><td>Disaster</td><td>Parameter</td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td><td>Obs.</td></tr><tr><td rowspan="6">Joplin tornado</td><td> $\alpha_{1}^{i}$ </td><td>0.158</td><td>2.7E-04</td><td>0.445</td><td>3.6E-13</td><td>9.880</td><td>8,954</td></tr><tr><td> $\beta_{1}^{i}$ </td><td>1.240</td><td>0.215</td><td>1.972</td><td>1.5E-05</td><td>37.177</td><td>8,954</td></tr><tr><td> $\alpha_{2j}^{i}$ </td><td>-0.186</td><td>-0.045</td><td>0.989</td><td>-10.746</td><td>12.013</td><td>47,742</td></tr><tr><td> $\beta_{2}^{i}$ </td><td>1.857</td><td>1.179</td><td>2.275</td><td>2.3E-05</td><td>26.475</td><td>8,954</td></tr><tr><td> $\mu^{i}$ </td><td>2.993</td><td>1.651</td><td>3.962</td><td>5.3E-13</td><td>57.043</td><td>8,954</td></tr><tr><td> $\gamma^{i}$ </td><td>3.401</td><td>3.097</td><td>2.494</td><td>5.7E-09</td><td>13.030</td><td>8,954</td></tr><tr><td rowspan="6">Black Forest fire</td><td> $\alpha_{1}^{i}$ </td><td>0.285</td><td>0.005</td><td>0.878</td><td>9.2E-14</td><td>14.778</td><td>2,275</td></tr><tr><td> $\beta_{1}^{i}$ </td><td>1.607</td><td>0.885</td><td>1.896</td><td>9.1E-05</td><td>16.297</td><td>2,275</td></tr><tr><td> $\alpha_{2j}^{i}$ </td><td>-0.328</td><td>-0.133</td><td>1.290</td><td>-7.583</td><td>9.174</td><td>6,639</td></tr><tr><td> $\beta_{2}^{i}$ </td><td>1.987</td><td>1.720</td><td>1.826</td><td>4.9E-04</td><td>12.414</td><td>2,275</td></tr><tr><td> $\mu^{i}$ </td><td>4.488</td><td>4.101</td><td>3.777</td><td>1.5E-12</td><td>41.373</td><td>2,275</td></tr><tr><td> $\gamma^{i}$ </td><td>3.771</td><td>3.544</td><td>2.313</td><td>1.4E-05</td><td>10.757</td><td>2,275</td></tr><tr><td rowspan="6">Lac-Megantic rail disaster</td><td> $\alpha_{1}^{i}$ </td><td>0.073</td><td>2.7E-06</td><td>0.370</td><td>4.9E-13</td><td>12.355</td><td>1,927</td></tr><tr><td> $\beta_{1}^{i}$ </td><td>0.902</td><td>0.058</td><td>2.147</td><td>7.3E-05</td><td>28.500</td><td>1,927</td></tr><tr><td> $\alpha_{2j}^{i}$ </td><td>-0.213</td><td>-0.055</td><td>1.023</td><td>-9.124</td><td>12.244</td><td>8,007</td></tr><tr><td> $\beta_{2}^{i}$ </td><td>1.552</td><td>0.683</td><td>1.951</td><td>4.9E-04</td><td>12.313</td><td>1,927</td></tr><tr><td> $\mu^{i}$ </td><td>3.048</td><td>1.601</td><td>4.554</td><td>1.8E-12</td><td>44.473</td><td>1,927</td></tr><tr><td> $\gamma^{i}$ </td><td>3.073</td><td>2.547</td><td>2.434</td><td>6.6E-08</td><td>12.974</td><td>1,927</td></tr><tr><td rowspan="6">2014 Iquique earthquake</td><td> $\alpha_{1}^{i}$ </td><td>0.216</td><td>0.001</td><td>0.826</td><td>9.8E-14</td><td>38.855</td><td>12,092</td></tr><tr><td> $\beta_{1}^{i}$ </td><td>1.596</td><td>0.360</td><td>3.744</td><td>2.9E-06</td><td>74.509</td><td>12,092</td></tr><tr><td> $\alpha_{2j}^{i}$ </td><td>-0.172</td><td>-0.039</td><td>1.009</td><td>-14.767</td><td>21.478</td><td>86,891</td></tr><tr><td> $\beta_{2}^{i}$ </td><td>2.064</td><td>1.272</td><td>2.613</td><td>2.1E-05</td><td>36.768</td><td>12,092</td></tr><tr><td> $\mu^{i}$ </td><td>4.049</td><td>2.509</td><td>5.463</td><td>2.4E-12</td><td>116.565</td><td>12,092</td></tr><tr><td> $\gamma^{i}$ </td><td>3.924</td><td>3.634</td><td>2.609</td><td>4.4E-09</td><td>19.285</td><td>12,092</td></tr></table>
