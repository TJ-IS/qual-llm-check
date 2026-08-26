---
otero_id: 28410
otero_key: "7C5YXCJR"
title: "Emotions in Online Content Diffusion"
authors: "Yifan Yu; Shan Huang; Yuchen Liu; Yong Tan"
year: "2026"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0611"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Emotions in Online Content Diffusion

Yifan Yu,<sup>a</sup> Shan Huang,<sup>b,</sup>\* Yuchen Liu,<sup>c</sup> Yong Tan<sup>d</sup>

<sup>a</sup> Department of Information, Risk, and Operations Management, McCombs School of Business, The University of Texas at Austin, Austin, Texas 78712; <sup>b</sup> Faculty of Business and Economics, The University of Hong Kong, University Dr, Lung Fu Shan, Hong Kong; <sup>c</sup> Information Systems & Operations Management Department, Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>d</sup> Department of Information Systems and Operations Management, Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195

\*Corresponding author

Contact: yifan.yu@mccombs.utexas.edu, https://orcid.org/0000-0002-8959-3169 (YY); shanhh@hku.hk, https://orcid.org/0000-0002-0276-127 (SH); yuchen.liu@warrington.ufl.edu, https://orcid.org/0000-0001-5043-4411 (YL); ytan@uw.edu (YT)

Received: November 6, 2022 Revised: December 12, 2023; October 1, 2024; March 31, 2025 Accepted: April 6, 2025 Published Online in Articles in Advance: August 4, 2025

https://doi.org/10.1287/isre.2022.0611

Copyright: © 2025 INFORMS

Abstract. This study examines the impact of discrete emotional expression (i.e., expression of anxiety, sadness, anger, disgust, love, joy, surprise, and anticipation) on the differential diffusion of online content in social media networks. We conducted an analysis on a random sample of 387,486 online articles and their corresponding diffusion cascades, involving more than six million unique individuals, on a major online social networking platform. Our investigation focused on the relationships between discrete emotional expression and the diffusion of online articles, specifically the structural properties of diffusion cascades, such as size, depth, maximum breadth, and structural virality. We employed various econometric model specifications, and our results robustly demonstrate that articles expressing higher levels of anxiety, love, and surprise reach a larger number of individuals and diffuse more deeply, broadly, and virally. In contrast, expression of anger, sadness, and joy exhibit the opposite effect. Additionally, we find that articles with different emotional expression tend to spread differently based on individual characteristics and social ties. Our findings offer valuable insights into the diffusion and regulation of online content from the perspectives of emotional expression and social networks.

History: Xiaoquan Zhang, Senior Editor; Jingjing Zhang, Associate Editor. Funding: This work was supported by the Seed Fund for Basic Research for New Staff by the University of Hong Kong [Project 104006417]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0611 Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0611

Keywords: information diffusion • online content • emotion detection • social networks • social media

## 1. Introduction

Social media networks, such as Twitter, Facebook, and WeChat, have fundamentally changed the way information spreads. Emotionally charged content can propagate rapidly and extensively through these networks, often leading to large-scale information cascades. Such content can influence our perspectives and behaviors on various aspects, including morality and ideology (Brady et al. 2017), politics, terrorism (Vosoughi et al. 2018), and financial markets (Gorodnichenko et al. 2023). This influence is especially evident during major global events such as the COVID-19 pandemic and the Russia–Ukraine conflict. Understanding the role of emotional expression in the diffusion of online content through social media networks is, therefore, critically important.

The existing literature emphasizes cognitive aspects of content diffusion more than affective aspects, such as emotional expression (Vosoughi et al. 2018). This disparity primarily arises from the complexity associated with detecting emotional expression, especially in large amounts of content. Furthermore, characterizing the peer-to-peer diffusion process of online content in social media networks often presents empirical challenges. Prio research mainly focuses on the impact of emotions on the overall popularity of news or tweets or from a dyadic per spective (e.g., whether to share or not) (e.g., Berger and Milkman 2012, Brady et al. 2017) using laboratory data.

Therefore, we provide some of the first large-scale, comprehensive empirical evidence on how the expression of various discrete emotions influences information cascading structures and processes on a major social media platform. Specifically, we analyze a representative sample of 387,486 online articles along with their corresponding diffusion cascades on WeChat, China’s largest social networking platform. We rigorously quan tify and characterize the structural properties of these cascades, including size, depth, maximum breadth, and structural virality. Additionally, we examine the characteristics of more than six million individuals (e.g., age, gender, and network degree) and the strength of their social ties (e.g., strong and weak ties) involved in the cascading process.

We identify the expression of eight discrete emotions (i.e., surprise, joy, anticipation, love, anxiety, sadness, anger, and disgust) to unpack the complexity of emotions in online content. Discrete emotions are relatively independent and can capture human emotions more effectively than valence and arousal (Lerner et al. 2004, Yin et al. 2017, Yu et al. 2023). According to discrete emotion theory (Tomkins 1962), a limited set of core emotions forms the foundation for more complex emotions. For example, awe may result from a combination of anxiety and love. Understanding discrete emotions enables us to better comprehend these intricate emotional states (Tomkins 1962; Lerner et al. 2004, 2015). These eight discrete emotions are also identified as the most prevalent in Chinese articles (Quan and Ren 2010). To detect these discrete emotions in our sampled articles, we developed a domain-specific and up-to-date emotion lexicon, employing a state-of-the-art lexicongeneration approach (Xue et al. 2014, Yu et al. 2023), and verified it through human annotation.

We focus on word-level emotional expression in online articles (i.e., a WeChat article) (Berger and Milkman 2012, Yin et al. 2014, Brady et al. 2017, Yu et al. 2023). Word-level emotional expression is defined as the linguistic expression of discrete emotions, including emotional keywords or phrases, degree words, and negation words (Kahn et al. 2007, Quan and Ren 2010). This focus ensures objective and standardized measurements, addressing potential issues associated with the subjective interpretation of emotional expression in longer texts (Berger and Milkman 2012, Yin et al. 2014), and offers practical implications for management (Kahn et al. 2007).

To identify the impact of emotional expression on online content diffusion, we mainly utilize a partial linear instrumental variable (IV) approach with a double machine learning (DML) framework (Chernozhukov et al. 2018). This framework allows us to effectively control for potential nonlinear effects of observable accountand article-level characteristics by integrating machine learning methods. We use the emotional expression of the articles published by the same account (author) most recently as the instrumental variable, aiming to address endogeneity concerns. Our results show that expression of anxiety, love, and surprise have a significant and positive impact on cascade depth, size, breadth, and structural virality. Conversely, expression of anger, sadness, and joy negatively influence these cascade metrics. The expression of anticipation has a significantly negative effect on cascade size and structural virality, whereas the expression of disgust has a significant positive effect on structural virality. Additionally, we find that all eight types of discrete emotional expression significantly influence the cascading process when considering the demographic characteristics (i.e., age and gender) and network properties (i.e., individuals network degree and the social ties between them) of the cascade participants. Further, we demonstrate the robustness of our results through various model specifications.

These findings highlight the differential effects of various discrete emotions on content diffusion, emphasizing the importance of understanding the interplay between emotional expression and information diffusion processes in social media networks. Theoretically, our work advances the current understanding of arousal or valence driving content sharing (Berger and Milkman 2012, Stieglitz and Dang-Xuan 2013). We show that emotions with similar valence and arousal levels (e.g., anger versus anxiety, love versus joy) can still exhibit opposite effects on content diffusion outcomes, highlighting the importance of understanding content diffusion from a discrete emotion lens. Additionally, the existing literature focuses on the number of retweets or which news articles are the most popular (Berger and Milkman 2012, Stieglitz and Dang-Xuan 2013, Brady et al. 2017). These measures cannot adequately describe the link between emotions and content diffusion processes. We empirically show that discrete emotions are associated with diffusion structures, individual characteristics, and social ties. By presenting one of the first empirical results on these diffusion outcomes, our work has the potential to inspire future research into emotions and content diffusion processes. Practically, our work offers valuable insights for content creators, marketers, and policymakers, enabling them to tailor strategies for creating, disseminating, or regulating online content more effectively.

## 2. Literature

We review the relevant literature on discrete emotions, emotions in online content diffusion, and the measurement of emotional expression in content and information diffusion.

## 2.1. Discrete Emotions

Current management research on the impact of emotional expression embedded in online content on user behavior predominantly draws upon dimensional emotion theory that uses dimensions such as valence (posi tive or negative) and arousal (level of activation) (e.g., Rui et al. 2013, Hennig-Thurau et al. 2015, Yin et al. 2017). However, recent psychological studies indicate that emotions with comparable valence and arousal can yield distinct effects on individual decision making and judgment (Lerner et al. 2015). For instance, even though anger and anxiety share similarities in both valence and arousal, anxiety embedded in online reviews tends to exhibit higher perceived helpfulness compared with anger (Yin et al. 2014). Such observations underscore that the dimensions of valence and arousal may not fully capture the nuanced effects of emotions (Plutchik 2001, Lerner et al. 2015).

A growing body of recent research has started to adopt discrete emotion theory to understand and measure emotional expression embedded in online content (e.g., Malik and Hussain 2017, Nguyen et al. 2020, Yu et al. 2023). Discrete emotion theory identifies specific basic and independent emotions that are distinct from one another (Tomkins 1962). These discrete emotions have evolutionary origins and manifest consistently in expression and recognition across individuals regardless of ethnic or cultural differences (Plutchik 2001). Prior management research indicates that the expression of discrete emotions embedded in online word of mouth has more predictive power than valence and arousal when it comes to perceived review helpfulness (Yin et al. 2014, Malik and Hussain 2017), consumers’ purchase decisions or sales performance (Yin et al. 2021, Yu et al. 2023), and stock market returns (Nguyen et al. 2020).

## 2.2. Emotions in Online Content Diffusion

Emotional expression is pivotal in the social dissemination of online information. From a theoretical perspective, the prevailing understanding is arousal activating sharing. For example, Berger and Milkman (2012) show that readers share digital news because they are stimulated by the high-arousal expression in it. Another perspective is negativity activating sharing. For example, Stieglitz and Dang-Xuan (2013) find that individuals share tweets when they contain more negative expression. However, the discrete emotions approach can provide new insights, emphasizing an understanding of individual behaviors affected by emotions that goes beyond valence and arousal (Yin et al. 2014, 2021; Yu et al. 2023).

From an empirical standpoint, the existing literature on the relationship between emotional expression and online content diffusion primarily consists of observational studies using predictive models (Berger and Milkman 2012, Stieglitz and Dang-Xuan 2013, Brady et al. 2017, Wang and Lee 2020) as well as laboratory experiments (Heath et al. 2001, Berger and Milkman 2012). For instance, Berger and Milkman (2012) examine the correlation between emotional expression and the virality of news articles shared via email, employing laboratory experiments to establish causal relationships between emotions and information sharing. Brady et al. (2017) uses a multilevel regression model to investigate the association between moral–emotional words in tweets and the number of retweets. Similarly, Stieglitz and Dang-Xuan (2013) and Wang and Lee (2020) utilize ordinary least squares (OLS) regression models to predict the total number of retweets based on emotional expression. Although these studies have significantly advanced our understanding of the role of emotional expression in online content diffusion, there are areas for improvement. These include more advanced measurements of emotional expression and information diffusion, empirical identification with greater rigor, and enhanced sample representativeness as these studies often focus on specific topics or particular content outlets.

## 2.3. Measurements of Emotional Expression in Content

There are two primary methods for understanding emotional expression: subjective document-level interpretation and objective word-level representation. Subjective document-level interpretation involves individuals identifying the overall emotional tone of a document. For instance, Yin et al. (2014) and Berger (2011) asked online review readers to evaluate the emotional state of the reviewer at the time of writing the review. However, asking readers to gauge emotions in extensive documents or on a continuous scale (e.g., how positive is it?) as opposed to a binary scale (e.g., is it positive?) leads to significantly lower agreement among readers (Pang and Lee 2005). Given the inherent subjectivity of these assessments, such inconsistencies are expected. Conse quently, for discrete emotions in extensive texts, document-level emotional expression remains, to our knowledge, vaguely defined.

Psychology literature emphasizes the meaningful use of emotional words to understand a document’s emotional impact, leading to the concept of objective wordlevel representation (Kahn et al. 2007). By focusing on word-level emotional expression, we can achieve more objective and standardized measurements across various texts and contexts, addressing the issues associated with subjective document-level interpretation. Moreover, relying on word-level emotional expression can lead to more actionable managerial implications compared with subjective document-level measures. Writers often find it challenging to determine the subjective judgments of readers about the emotions expressed in their content. Subjective interpretations can vary widely among readers. In contrast, word-level representation provides a more concrete and quantifiable approach to understanding emotional expression, allowing managers and researchers to draw clearer insights and make more informed decisions based on their effects. We, thus, focus on word-level emotional expression in online articles (Quan and Ren 2010, Yin et al. 2014, Yu et al. 2023). Specifically, we adopt a scalable and computational approach to identify word-level emotional expression (Yu et al. 2023). This addresses the limitations of earlier studies that rely on laboratory surveys and self-report measurements in large-scale data sets (Heath et al. 2001, Berger and Milkman 2012).

## 2.4. Measurements of Information Diffusion

The general popularity of content is a frequently used measure of online content diffusion in existing literature.

It is determined by indicators such as whether an article makes The New York Times’ most e-mailed list (Berger and Milkman 2012) or by the number of retweets (Stieglitz and Dang-Xuan 2013; Brady et al. 2017, 2019; Wang and Lee 2020). Additionally, self-report measures from a dyadic perspective, such as reporting whether or what to share, are often used in laboratory studies to measure individuals’ intention to share content (Heath et al. 2001, Berger and Iyengar 2013, He and Bond 2013, Berger 2014). However, these measures cannot adequately describe the information diffusion process in large-scale social media networks. Instead, the cascade structural properties can reflect the diffusion patterns and processes and are represented by four dimensions: size, depth, maximum breadth, and structural virality in the literature (Goel et al. 2015, Vosoughi et al. 2018).

Size represents the general popularity of an article without specifying its diffusion structure. Depth refers to the number of generations within a cascade, indicating the maximum degree of contacts that the information can reach from the root node. Information with a cascade of greater depth is more likely to penetrate different social communities. Maximum breadth offers insight into how broad or wide the cascade is, often resulting from broadcast structures. A broad but not deep cascade implies that the content is spread within the same large social community. Structural virality quantifies the distinction between single broadcast and viral diffusion (Goel et al. 2015). Higher structural virality indicates that the cascade is driven more by decentralized, peer-to-peer sharing than by broadcasting. Broadcasting and viral diffusion are two typical approaches that enable information to reach large audiences (Van den Bulte et al. 2018). The structure of cascades can be influenced by these approaches, such as whether the diffusion process is driven more by mass media or high-centrality users to broadcast content or whether rewards are used to encourage peer-to-peer diffusion.

Furthermore, evidence on how emotional expression affects the individual characteristics of diffusion cascades—such as users’ gender, age, network degree, and the strength of their social ties (strong versus weak)—are scarce in the literature. These metrics can provide valuable insights into the interplay between specific types of emotional expression and the individuals and social ties through which emotionally charged content is disseminated.

## 3. Theory

To understand the impact of discrete emotional expression on individuals’ spread of content in social networks, it is crucial to recognize that different emotions can influence behavior through distinct pathways (e.g., Lerner et al. 2004, Yin et al. 2014, Lerner et al. 2015, Yu et al. 2023). Drawing on the emotions as social information (EASI) framework, we discuss how each type of discrete emotional expression affects readers’ inferential processes and affective reactions, ultimately influencing content diffusion. We first introduce the EASI framework and then discuss its relationship with the impact of emotional expression on content diffusion.

## 3.1. EASI Framework

The EASI framework stands as a prominent theory that sheds light on the influence of emotional expression on social interactions (Van Kleef 2009). Sharing online content has become a vital form of social interaction among users. Furthermore, this framework emphasizes discrete emotions, which aligns with the focus of our study (Van Kleef 2010). Researchers have increasingly turned to this framework to elucidate the effects of explicit word-level emotional expression (such as emotional keywords or phrases in online reviews) on content viewers’ behaviors, such as review readers’ behaviors (Yin et al. 2017, 2021).

Based on the EASI framework, emotional expression in content can influence readers’ behavior through two primary mechanisms: inferential processes and affective reactions (Van Kleef 2009). When writers express their emotions through content, readers often make cognitive inferences about the content (Keltner and Haidt 1999). Moreover, a writer’s emotional expression can elicit affective reactions in readers (Clark and Taraban 1991). These affective reactions can occur through two specific mechanisms. First, there is the operation of emotional contagion, by which the emotions expressed by writers tend to provoke similar emotions in readers (Hatfield et al. 1993). Second, an individual’s emotional expression can shape others’ impressions and interpersonal attraction to the person expressing the emotion (Van Kleef 2009). For example, if a leader consistently exhibits anger, employees may form unfavorable impressions of them (Van Kleef 2010). These inferences and affective reactions, in turn, guide readers’ decisions to share the content.

## 3.2. Discrete Emotional Expression on Online Content Diffusion

Enabled by the EASI model, our work contributes a key theoretical insight: emotions with similar arousal and valence levels can still evoke distinct inferential processes and affective reactions, thereby leading to opposite effects on content diffusion.

Although the EASI framework guides us to focus on important theoretical constructs and pathways to the impact of emotional expression, it does not directly predict the effects of discrete emotions on content diffusion. Therefore, we rely on prior theories and empirical evidence to develop our predictions. Table 1 summarizes the literature that points out the key differences in inferential processes and affective reactions for similar emotional pairs (anger versus anxiety, love versus joy, and sadness versus disgust), thereby leading to the prediction of their opposite effects. We also predict that the related emotional pair, that is, surprise and anticipation, can have a distinct impact on content sharing. See the detailed theoretical discussion in Online Appendix EC.1.1.

Table 1. Discrete Emotions, Key Mechanisms, and Effects on Content Diffusion

<table><tr><td>Emotion</td><td>Inferential processes</td><td>Affective reactions</td><td>Effect on diffusion</td><td>Key references</td></tr><tr><td>Anger</td><td>Implies the author&#x27;s low cognitive effort or irrationality; perceived hostility in anger evokes social distance</td><td>Develops negative impression and avoidance tendency toward the author and content</td><td>Decreases</td><td>Van Kleef (2010), Yin et al. (2014, 2021), Xiao et al. (2018), Heerdink et al. (2019)</td></tr><tr><td>Anxiety</td><td>Signals the author&#x27;s vigilance, high cognitive effort, and perceived trustworthiness</td><td>Highly contagious; prompts emotional impulse to seek advice and social support</td><td>Increases</td><td>Heath et al. (2001), Rimé (2009), Yin et al. (2014, 2017)</td></tr><tr><td>Sadness</td><td>A reader may connote loss and vulnerability and avoid public sharing to protect privacy</td><td>A reader&#x27;s harbored low arousal may suppress the action of sharing</td><td>Decreases</td><td>Finkenauer (1998), Van Kleef (2010), Berger and Milkman (2012)</td></tr><tr><td>Disgust</td><td>Can spark relative relief or gloating; some share for hedonic gain; others deterred by norms</td><td>May trigger an avoidance tendency and reduce sharing intention</td><td>Context dependent</td><td>Heath et al. (2001), Berger and Milkman (2012)</td></tr><tr><td>Love</td><td>Suggests commitment, trust, prosocial bonding, aligns with prosocial norms</td><td>Elicits warmth and empathy</td><td>Increases</td><td>Lapinski and Rimal (2005), Jiang et al. (2019)</td></tr><tr><td>Joy</td><td>Often viewed as self-focused; perceived as lacking in competence, authenticity, or reliability</td><td>Can trigger a negative impression because of social comparison</td><td>Decreases</td><td>Festinger (1954), Jiang et al. (2019)</td></tr><tr><td>Surprise</td><td>Signals novelty and unexpectedness; heightens curiosity</td><td>Stimulates excitement; draws attention</td><td>Increases</td><td>Scherer (2001), Luna and Renninger (2015), Vosoughi et al. (2018)</td></tr><tr><td>Anticipation</td><td>Implies predictability; may reduce perceived urgency</td><td>Lower emotional impact leading to less incentive to share</td><td>Decreases</td><td>Plutchik (2001)</td></tr></table>

## 3.3. Discrete Emotional Expression on

Characteristics of Individuals and Social Ties The EASI framework suggests that the impact of emotional expression is deeply intertwined with social and relational contexts (Van Kleef 2009). Various emotional expression can spread through social ties of varying degrees of closeness and among individuals in different network positions. Additionally, individuals with diverse demographic characteristics may interpret a given emotional expression in distinct ways. However, the literature and theories in this area are still in their early stages. In Table 2, we provide a summary of relevant studies and offer exploratory predictions. We hope our exploration will inspire future theoretical advancements and inform strategies for targeting the diffusion of content embedded with different emotional expression. See more detailed theoretical discussions in Online Appendix EC.1.2.

## 4. Empirical Strategy

We collected data from WeChat, a major social media platform on which users can read articles published by official accounts and share them with their contacts. Figure 1 illustrates an example of the reading and sharing process for a WeChat article. Figure 3 illustrates the empirical framework for this study.

## 4.1. Sampling

Our sampling process aims to ensure a representative sample, guaranteeing a sufficient number of articles collected for each account, offering benefits for empirical identification. Specifically, our sampling process consists of the following steps: First, we randomly select 100,000 official accounts from WeChat. This random selection ensures the sample representativeness and a large sample size. Second, we filter out inactive accounts that posted fewer than 10 articles during our observation period (August 31 to November 30, 2018), resulting in 38,839 official accounts. This step is necessary to ensure that each account in our sample has a substantial number of articles available for collection. Third, we proceed to randomly collect 10% of the articles published by each of the sampled accounts during the observation period, collecting a total of 387,486 online articles for analysis. This approach allows us to obtain a representative and diverse set of articles from each account.

This sampling process resulted in a total of 6,823,576 unique individuals sharing these 387,486 online articles with their first degree friends (i.e., strong tie contacts) or their acquaintances (i.e., non–first degree friends, weak tie contacts) through all available viral channels on WeChat.<sup>1</sup> We collected data on the demographic (i.e., age and gender) and network characteristics (i.e., network degree) of all the users involved in the cascades as well as the tie strength between every pair of sender and receiver (whether they were first degree friends) in each cascade.

Table 2. Discrete Emotional Expressions, Individual Characteristics, and Social Ties

<table><tr><td>Dimension</td><td>Key argument</td><td>Relevant emotional expression and potential impacts</td><td>Key references</td></tr><tr><td>Age</td><td>Older adults respond more to anger and anxiety (reflecting inner age-related turmoil) and may share love to compensate for fewer in-person interactions</td><td>Anger, anxiety: high engagement because of life experiences. Love: fosters socioemotional connections</td><td>Carstensen et al. (2003), Kensinger (2008), Cotten et al. (2022)</td></tr><tr><td>Gender</td><td>Women emphasize social image management and relationship maintenance; men focus on entertainment</td><td>Women: share love for bonding and avoid sadness to maintain a positive image. Men: share joy to provide entertainment</td><td>Anderson (2015), Lin and Wang (2020)</td></tr><tr><td>Network centrality</td><td>High-degree users value rationality and prosocial image; low-degree users seek attention</td><td>High-degree: prefer anxiety over anger; share love to reinforce social bonds; share anticipation to showcase confidence. Low-degree: share surprise to gain visibility</td><td>Plutchik (2001), Lapinski and Rimal (2005), Yin et al. (2014), Vosoughi et al. (2018), Xiao et al. (2018), Jiang et al. (2019)</td></tr><tr><td>Social ties</td><td>Strong ties allow more sensitive emotional sharing; weak ties serve for engagement or novelty</td><td>Strong ties: more likely to see anger, anxiety, and love (close or urgent). Weak ties: share surprise for attention and strengthening relationships</td><td>Yin et al. (2014), Xiao et al. (2018), Jiang et al. (2019)</td></tr></table>

Our sample covers a wide range of topics, including politics, economics, business, society, sports, and technology, among others. The sample comprises both short texts (fewer than 100 characters, akin to tweets) and long articles (exceeding 100,000 characters, comparable to newspaper and magazine articles or book chapters). The average article length is 1,164.60 characters with a standard deviation of 2,060.98 characters. Whereas WeChat primarily hosts text-based content, it allows articles to include images and videos. We recorded the quantity of images and videos in each article. For official accounts, we recorded the average number of followers during our observation period (indicating an account’s popularity), the average number of daily posts (reflecting an account’s proactivity), and the type of account (individual, media, business enterprises, government, or other organizations).

## 4.2. Mapping Cascades

Our data set uniquely circumvents the cascade mapping problem, a common issue in Twitter retweet cascade mapping. Retweet cascades are typically deduced based on timing and relations (Shi et al. 2014, Vosoughi et al. 2018). Our context enables us to accurately chronicle the diffusion cascades of each article in our sample by recording the exact account ID of all individuals who shared the article, the source from whom they accessed the article, and the time stamp of each sharing event.

An article cascade commences when an article is posted to an account’s followers, who then disseminate the article within their local social networks. Users at the cascade’s terminus are those who shared the article, after which the article wasn’t shared by anyone else for the subsequent week. According to our data, if an article is not shared again within the following seven days, it is highly unlikely (less than 1% probability based on historical data) for the article to be shared again. Figure 1 illustrates an example of a large article cascade from our sample.

## 4.3. Measuring Cascades’ Structural Properties

We measured the cascades through four dimensions: size (the total number of users involved in sharing the article), depth (the maximum number of sharing hops from the original article, in which a hop represents a sharing action by a new unique user), maximum breadth (the maximum number of users involved in the cascade at any depth), and structural virality (the average length of the shortes paths between all pairs of nodes in a diffusion tree) (Goel et al. 2015, Vosoughi et al. 2018). These four measures are succinct representations of the shape and dynamics of a cascading process. Specifically, structural virality is defined as $\textstyle { \widehat { \frac { 1 } { n ( n - 1 ) } } } \sum _ { i = 1 } ^ { n } { \widehat { \sum } } _ { j = 1 } ^ { n } d _ { i j } ,$ , where n represents the number of individuals involved in a cascade and $d _ { i j }$ represents the shortest distance between individual i and individual j involved in the cascade. Structural virality denotes the average shortest distance between each pair of nodes in a cascade. Provided the same level of cascade size, higher structural virality indicates that the cascade is driven more by decentralized and peer-to-peer sharing than by broadcasting.

Figure 1. (Color online) An Example of a Large Cascade  
![](/api/attachments/7C5YXCJR/fulltext/images/eb59555b066f18e7a7f31cf2951902b62a5c5fff38c54a7ddb5d2435c55c7d51.jpg)  
Notes. The cascade involves 7,225 unique individuals (represented by nodes). The article documented a scandal that involved certain individua bloggers and journalists who illegally blackmailed a number of real estate firms. The bloggers and journalists threatened to spread negativ online articles about the firms unless they received a large payment.

Figure 2, (a) through (d), provides descriptions of the empirical distributions of cascade size, depth, maximum breadth, and structural virality of the articles in our sample. It is apparent that only a small fraction of the articles exhibits high values in every cascade dimension. To understand the relationships among these cascade dimensions, we present the correlation matrix in Online Table EC.12.1. A strong relationship exists between cascade size and maximum breadth (0.974) and between cascade depth and structural virality (0.921) as we observe that, in our sample, 41% of the articles’ cascades end at the first level.

4.4. Measuring Emotional Expression in Content We focus on surprise, joy, anticipation, love, anxiety, sadness, anger, and disgust in our analysis. Our choice of emotions is consistent with the IS literature on discrete emotion analysis of Chinese texts.<sup>2</sup> We first adopted a state-of-the-art lexicon-generation approach (Yu et al. 2023) and constructed a new domain-specific and up-to-date emotion lexicon by extending a basic lexicon constructed by Quan and Ren (2010). We then lev eraged the newly constructed lexicon to construct discrete emotion variables for each article. Then, we removed emotion words from the articles and ran a topic model to construct topic variables. These variables summarize nonemotional information of the content and are used as control variables.

First, we use an existing emotion lexicon, Ren-CECps (Quan and Ren 2010), as the basic lexicon, denoted as $L _ { 0 } .$ Each word $w _ { i }$ in the lexicon is mapped to an eightdimension vector $\pmb { v } _ { i } = ( I _ { 1 } ^ { i } , I _ { 2 } ^ { i } , \ldots , I _ { 8 } ^ { i } )$ , where $I _ { k } ^ { i } \in [ 0 , \breve { 1 } ]$ is

Figure 2. (Color online) Cumulative Distribution Functions (CDFs) of Cascade Scales and the Level of Intensity of Eight Types of Discrete Emotional Expression for an Average Article

(a)  
![](/api/attachments/7C5YXCJR/fulltext/images/01d0409ccb76c69a1d9bb81fd8e88a13230f0fb3b76bd5ac7d6ec33383bd0679.jpg)

(b)  
![](/api/attachments/7C5YXCJR/fulltext/images/bf32d063471c329a5f1576bc91d9eb4e3ddbbf079f1fcbf21747e8d9ea3c3113.jpg)

(c)  
![](/api/attachments/7C5YXCJR/fulltext/images/e1218cb2eedf5c657f648b3599003ad6d17cb75265ad256ddd265c0da5815e52.jpg)

![](/api/attachments/7C5YXCJR/fulltext/images/0d8b9f30cb51e87e5f33e8cc4d7549110bc915f010fe64a3c3124d6a5c0ffc30.jpg)

![](/api/attachments/7C5YXCJR/fulltext/images/51cc47f3fd09db47cced293d17ea7baa62f19d0a181851d6b5507d5de8f9a6aa.jpg)  
Notes. (a–d) The CDF of the four cascade scales. Because of the nondisclosure agreement with Tencent, we cannot disclose the specific magni tudes of content diffusion in the figures. (e) The average level of intensity of eight discrete emotional expression for an article. The values ar taken directly from our emotion detection analysis and have not been normalized to a standard distribution (so that we can compare the mean values of different types of emotions). The differences between all pairs of the eight emotions are statistically significant $( p \mathbf { s } < 0 . 0 0 1 { \dot { ) } }$ ).

manually annotated and represents the intensity of the kth discrete emotions expressed by w . That is, ${ \cal L } _ { 0 } = \{ ( w _ { i } , v _ { i } ) \} _ { i = 1 } ^ { N } ,$ , where $N = \bar { 1 6 } { , } 0 1 7$ is the total number of words in $L _ { 0 } .$ . Second, we retrieve word vectors that contain words’ semantic information. Statistical language models can derive the word vectors (e.g., Word2- Vec by Mikolov et al. 2013). We used pretrained word vectors by Song et al. (2018), who provided 200- dimension word vectors for more than eight million common Chinese words and phrases. These word vectors are trained on up-to-date, large-scale, and highquality Chinese online content and have been validated through various natural language processing tasks (Song et al. 2018). Then, the similarity between the two words can be measured by the cosine similarity of the two corresponding word vectors (Mikolov et al. 2013). Third, using the basic lexicon and word vectors as input, we follow the approach proposed by Yu et al. (2023) (algorithms 1–3 proposed in their work) to extend the basic lexicon to a domain-specific and up-to-date lexicon (see Online Appendix EC.3 for technical details).

A total of 16,921 new words were found after this process, and the extended lexicon contains a total of 28,969 words. This result confirms the necessity of constructing a domain-specific lexicon, without which 58.4% of unique emotion words (16,921 out of 28,969) would be ignored if only the basic lexicon was used. Formally, we denote the new lexicon as $L ,$ where $L = L _ { 0 } \cup L _ { 1 }$ (with

$L _ { 0 } \cap L _ { 1 } = \emptyset )$ and ${ \cal L } _ { 1 } = \{ ( w _ { j } ^ { \prime } , v _ { j } ^ { \prime } ) \} _ { j = 1 } ^ { N ^ { \prime } }$ is the set of newly mined emotion words $\boldsymbol { w _ { j } ^ { \prime } }$ and their associated emotion intensity vectors $\mathbf { } v _ { i } ^ { \prime } .$ . The cardinality of $L _ { 1 }$ is denoted as $N _ { \mathrm { ~ \it ~ \ / ~ } } ^ { \prime }$ , and $N ^ { \prime } = 1 6 { , } 9 2 1$ . Table EC.3.1 in Online Appendix EC.3 shows a list of the top words (in terms of intensity) in each emotion category. Five raters were recruited to annotate the emotional intensities of the newly mined words for the eight discrete emotions. There is no statistically significant difference between the results generated by the algorithms and by the raters, confirming the validity of our new lexicon (see Online Appendix EC.4).

Next, we construct discrete emotion variables for each article (document). In addition to emotion words matched by L, we also consider the negation and degree words (if any) associated with these emotion words. We map each online article d into an eight-dimensional vector: $d \to ( e _ { 1 } , \dots , e _ { k } , \dots , e _ { 8 } )$ . Each element $e _ { k }$ represents the intensity score of one type of discrete emotional expression in the article (Quan and Ren 2010). $e _ { k }$ is jointly determined by emotion words matched by $L ,$ and negation words $( \mathrm { { { e . g . } , \mathrm { { ' n o t } ^ { \prime \prime } ) } } }$ ) and degree words $( \mathrm { e . g . , }$ “very”) associated with these emotion words, following the approach by Yu et al. (2023).<sup>3</sup> Specifically, if the algorithm finds an emotion word in the article, it checks the three words before the emotion words and captures any negation and degree words. Then, $e _ { k }$ is determined as $e _ { k } \overset { \smile } { = } \Sigma _ { i = 1 } ^ { n } ( - 1 ) ^ { m _ { i } } \times \mathsf { \bar { D } } e g V _ { i } \times I _ { k } ( w _ { i } )$ , where $\left\{ w _ { i } \right\} _ { i = 1 } ^ { n }$ are the emotion words in both article d and our lexicon L. If $n =$

$0 ,$ then $e _ { k } ( d )$ is set to zero. $I _ { k } ( w _ { i } )$ refers to the kth discrete emotion intensity of w $( k \in \{ 1 , 2 , \ldots , 8 \} )$ . $m _ { i }$ is the total number of negative words that appear in the sliding window of $w _ { i } .$ . Finally, $D e g V _ { i }$ is the average degree value of all degree words that appear in the sliding window of $w _ { i }$ . The degree values are obtained from the degree word dictionary (Quan and Ren 2010, Yu et al. 2023). Intuitively speaking, $e _ { k }$ is the summarized intensity expressed by all emotion words and is reasonably adjusted by their associated degree and negation words. We used the same procedure and analyzed eight discrete emotions in the comments.

In Online Appendix EC.4.2, we provide specific examples demonstrating how our method operates in detecting distinct emotions. In Online Appendix EC.4.3, we validate our approach for document-level emotion detection. We recruited three annotators to independently rate the most expressed emotion in article titles. We show that only 32.2% of titles received consistent annotation, confirming that the subjective document-level approach for emotion analysis may not be entirely feasible in our context. For the titles receiving a consistent annotation, our approach achieves comparable performance to the stateof-the-art large language model, the ChatGPT-4o model.

We present the average intensities of emotional expression at the article level in Figure 2(e) and show their respective distributions in Online Figure EC.12.1. We find that anger and sadness are the least expressed emotions, whereas love, anticipation, and anxiety are the most common. Further, to check their independence, we present the correlation matrix of the eight discrete emotions in Online Table EC.12.2. The correlations of all pairs of discrete emotions are below 0.44, whereas most of the correlations are below 0.20. The result implies that the correlations among the eight discrete emotions are low, indicating the independence of these eight discrete emotions.

## 5. Model

We utilize a partially linear random-effects instrumental variable model to examine the impact of emotional expression on online content diffusion. Selection bias for emotional expression may arise at two levels: the account level and the article level. Because articles are nested within accounts, articles from the same accounts may share common characteristics, such as topics or writing styles, and may not be independent of one another. Our model addresses such an account-level selection by explicitly modeling it as random effects. Additionally, it considers a comprehensive set of account-level and article-level control variables. To further account for article-level selection, we incorporate both linear and nonlinear effects of article-level control variables in our model. Adding a linear combination of article-level control variables may not be sufficient as the omission of nonlinear terms of these control variables—such as their interactions and higher order relationships—can still lead to omitted variable bias. Examples of these nonlinear relationships include the interaction between topics and timing (e.g., some topics are more likely to be published on weekends) and the inverted U-shaped effects of article length (articles that are either too short or too long may not diffuse effectively). To address this, we employ a DML specification that leverages the capabilities of machine learning to account for both linear and nonlinear effects of control variables.

Even when incorporating nonlinear terms of articlelevel observables, we may not fully address selection based on article-level unobservables or the measurement errors present in the variables of interest. For example, articles about natural disasters typically contain a higher degree of anxiety and tend to be widely shared. Whereas incorporating articles’ latent topic controls and contextual variables in our models can mitigate potential endogeneity, concerns may still arise about the sufficiency of this remedy, and the possibility of reverse causality issues remains. To address this, we integrate an instrumental variable approach, commonly used in estimating the effects of online content characteristics (Dev et al. 2019), into the DML framework. Specifically, we use the intensity scores of emotional expression found in the most recent article preceding the current article from the same account (i.e., lagged emotional expression intensity scores) as our instrumental variable in the analysis.

The intensity scores of the emotional expression from the most recent article (i.e., the article immediately preceding the current one) posted by the same account could serve as valid instruments. The use of lagged independent variables as instrumental variables is a well-established practice in economic literature (Villas-Boas and Winer 1999). On one hand, these scores are likely correlated with the emotional expression in the current article because an account’s emotional states may carry over from one context to another (Lerner et al. 2004, 2015). On the other hand, these lagged emotional expression scores are unlikely to directly impact the diffusion of the current article. As evidence, the correla tions between these lagged emotional expression intensities and the structural properties of the cascade for the current article are all less than 0.03 as shown in Online Table EC.12.11. Furthermore, our survey results suggest that users typically do not view the lagged emotional expression as a significant factor when deciding to share an article (see Online Section EC.9 for more details).

Meanwhile, the instrumental variable approach can also address concerns regarding measurement errors in emotional expression intensity scores (Wooldridge 2002) even though measurement errors should not be a significant issue in our identification.<sup>4</sup> Given that the measurement errors are unlikely to be systematic across articles, errors in intensity scores of the focal article are unlikely to correlate with our instrumental variable. Because of this orthogonality, the measurement errors are unlikely to bias the estimation results (Wooldridge 2002, Chernozhukov et al. 2018).

Furthermore, both the weak instrument test and the Sargan test validate our instrumental variable. The $p \mathrm { - }$ values of the F-statistics in the weak instrument test are all below 0.001, suggesting that our instrument is strong (Stock and Yogo 2005). Additionally, the p-values of the J-statistics in the Sargan test all exceed 0.950, implying that we cannot reject the hypothesis of our instrumental variable being exogenous (Sargan 1958). Additionally, to better account for potential correlations among articles published by the same publishers, we incorporate clustered standard errors (CSEs) in our model.

Formally, our model is shown as follows:

$$
y _ {i j} = \boldsymbol {\beta} ^ {\prime} \text {emotion} _ {i j} + g _ {0} (\text {article} _ {i j}, \text {account} _ {i}) + A c c o u n t _ {R E i} + \epsilon_ {i j},\tag{1a}
$$

$$
\mathbf {z} _ {i j} = m _ {0} \left(\text { article } _ {i j}, \text { account } _ {i}\right) + \boldsymbol {\mu} _ {i j},\tag{1b}
$$

where $y _ { i j }$ indicates one of the four cascades’ structural properties of the jth article published by the ith account, emotion indicates the intensity scores of (discrete) emotions of the jth article published by the ith account, articl $\mathbf { e } _ { i j }$ indicates the article-level control variables of the jth article published by the ith account, account indicates the account-level control variables of the ith account, Accoun $\cdot _ { R E i }$ indicates the account random effects that capture each account’s specific effect on the outcomes, and $\mathbf { z } _ { i j }$ indicates the instrumental variables that we incorporate (i.e., lagged intensity scores of emotions or average intensity scores of emotions in concurrent articles published by other accounts) that may affect the cascades’ structural properties through shifting intensity scores of emotions in the jth article published by the ith account conditional on article characteristics. $\epsilon _ { i j }$ and ${ \pmb { \mu } } _ { i j }$ are stochastic errors. $\mathbf { z } _ { i j }$ can shift $y _ { i j }$ through affecting emotion $\mathbf { \rho } _ { \mathrm { i } j } ,$ conditional on article , but is uncorrelated with $\epsilon _ { i j } .$ . In this model, we use $\pmb { \beta }$ to capture the effect of the emotion, the nonlinear function $g _ { 0 }$ to capture how article and account characteristics affect the cascades dimensions, and the nonlinear function m to capture how the article and account characteristics affect instrumental variables.

For the account-level control variables, we include account type<sup>5</sup> and the number of fans (followers). For the article-level control variables, we first control for an article’s nonemotional content, which may confound the relationship between emotional expression and article diffusion. We estimate a latent dirichlet allocation model (Blei et al. 2003) based on all sampled articles and controlled for the latent topic distribution of an article using a 30-dimension vector (see Online Appendix EC.5 and Online Figure EC.5.1 for more details). This model is widely adopted and considered the standard model for summarizing the topics of article content. Second, we incorporate two crucial variables to control for articles’ special contexts: specifically, whether the articles are advertisements or clickbait. These two types of articles may strategically leverage certain emotional expression to attract readers. Once readers figure out that an article is an advertisement or clickbait, they are unlikely to share it. In other words, these two article types may confound the effects of emotions on diffusion. We employ supervised learning to predict whether an article is an advertisement and whether it is clickbait. The detailed procedures are provided in Online Appendix EC.8. Additionally, we include article length (log-transformed number of characters), the number of images and videos embedded in the article (media richness), whether the account requested monetary rewards from readers (a content quality indicator), whether the article was posted during a weekend (time effect), and the number of comments in our model. To estimate our partial linear model, we then follow the DML framework developed by Chernozhukov et al. (2018) (see Online Appendix EC.6 for details) and perform a two-stage least squares regression on the estimated residuals to estimate $\mathbf { \delta } \mathbf { \cdot } \mathbf { \delta } \mathbf { \alpha } \mathbf { \beta }$

We further explore the effects of discrete emotional expression on the demographics $( \mathrm { i . e . , }$ , age, gender, and network degree) of all users and the social ties $( \mathrm { i . e . , }$ weak versus strong ties) involved in the cascades. Speci fically, we focus on the average age, the proportion of females, the network degree of individuals (measured by the average number of friends during the observation period), and the proportion of weak ties involved in the cascades. We employ the same partial linear instrumental variable approach for this analysis. In this context, $y _ { i j }$ in Equation (1) represents the demographics and social ties associated with the cascade of the jth article published by the ith account.

## 6. Results

In this section, we present our results on the effects of emotional expression on content diffusion measured by the four structural properties of cascades. Specifically, we show the findings based on our model derived in Section 5 and discuss their relationships with the theory developed in Section 2. Additionally, we provide evidence on how emotional expression in content affect the characteristics of individuals and social ties involved in the diffusion process. We acknowledge that, whereas the models address various selection biases, the relationships identified may not be fully causal without formal randomization of different emotional expression. Despite this limitation, our analysis uncovers robust and significant associations between emotional expression in content and the characteristics of the content diffusion process.

## 6.1. Effects of Discrete Emotional Expression on Cascades’ Structural Properties

We present our results from the random-effects IV model under the DML framework in Table 3 and further illustrate them in Figure 4. Our findings suggest that articles expressing higher levels of anxiety, love, and surprise are associated with larger expected cascade depth, size, breadth, and structural virality. In contrast, articles expressing higher levels of anger, sadness, and joy tend to produce cascades that are shallower, smaller, narrower, and less viral. Hence, content expressing more anxiety, love, and surprise (as opposed to anger, sadness, and joy) can spread not only more (less) broadly but also more (less) deeply into the networks, exhibiting more (less) peer-to-peer viral diffusion relative to broadcasting. Additionally, articles with more expression of anticipation are associated with decreased expected cascade depth and structural virality. This suggests that anticipation discourages peer-topeer diffusion relative to broadcasting. Further, these results are consistent with the observation that love and anxiety are the most expressed, whereas anger and sadness are the least expressed emotions by writers in our sample of online content (see Figure 2(e)). Our main findings are also generally consistent with the theoretical predictions derived from the EASI framework (Van Kleef 2009) as discussed in Section 3.1.

## 6.2. Effects of Discrete Emotional Expression on Individuals and Social Ties

We then provide some of the first empirical evidence on the effects of emotional expression on the characteristics of the content diffusion process. In particular, we focus on the effects on the average age, the proportion of females, and the network degree of individuals as well as on social ties, measured by the proportion of weak ties involved in the cascades. We applied the same random-effects IV model in this analysis, and the findings are detailed in Online Table EC.12.3 and Online Figure EC.12.2.

The results indicate that all eight types of discrete emotional expression significantly affect cascade demographics and social ties. First, our analysis shows that articles with higher levels of anger, anxiety, and surprise tend to involve older individuals in their cascades. Second, our model shows that articles with higher levels of sadness and joy involve a greater proportion of males in the cascades. In contrast, articles with more expression of love engage a significantly higher percentage of female users in the cascades.

Third, we examined the influence of emotional expression on the network degree of individuals

Table 3. Main Results: Emotional Expression

<table><tr><td>Emotional expression</td><td>Depth</td><td> $Size^a$ </td><td> $Breadth^a$ </td><td>Structural virality</td></tr><tr><td>Anger</td><td>-0.068***(0.021) $^c$ </td><td>-0.008***(0.003)</td><td>-0.007**(0.003)</td><td>-0.042***(0.013)</td></tr><tr><td>Anxiety</td><td>0.029***(0.003)</td><td>0.005***(0.0004)</td><td>0.005***(0.001)</td><td>0.019***(0.002)</td></tr><tr><td>Sadness</td><td>-0.277***(0.023)</td><td>-0.046***(0.003)</td><td>-0.039***(0.003)</td><td>-0.195***(0.015)</td></tr><tr><td>Disgust</td><td>0.0003(0.005)</td><td>-0.001(0.001)</td><td>-0.001*(0.001)</td><td>-0.00002(0.003)</td></tr><tr><td>Joy</td><td>-0.010***(0.004)</td><td>-0.002***(0.0004)</td><td>-0.002***(0.001)</td><td>-0.007***(0.002)</td></tr><tr><td>Love</td><td>0.014***(0.001)</td><td>0.002***(0.0001)</td><td>0.001***(0.0002)</td><td>0.008***(0.001)</td></tr><tr><td>Surprise</td><td>0.018***(0.007)</td><td>0.003***(0.001)</td><td>0.003***(0.001)</td><td>0.011**(0.005)</td></tr><tr><td>Anticipation</td><td>-0.007***(0.003)</td><td>-0.0003(0.0003)</td><td>-0.0002(0.0004)</td><td>-0.003*(0.002)</td></tr><tr><td>Account-level controls+ account random effects + CSE</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td> $Article-level\ characteristics^b$ </td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

Notes. The F-statistics of the first stage regression are shown in Online Table EC.12.15. The full table with control variables is shown in Onlin Table EC.12.16. The results of the first stage regression are shown in Online Table EC.12.17.  
<sup>a</sup>Given the right-skewed distributions of size and maximum breadth, we did a log-transformation on these two variables  
<sup>b</sup>All of the article-level variables (i.e. article length, number of images and videos embedded in the article, whether the article has a monetary rewarding feature, whether the article was posted during a weekend, number of comments, and topic distribution of the article) are controlled.  
<sup>c</sup>Standard error of estimation.  
Significance level: \*p < 0:05; \*\*p < 0:01; \*\*\*p < 0:001.

Figure 3. Empirical Framework  
![](/api/attachments/7C5YXCJR/fulltext/images/ad37dcf0b633a66c9c0a7166a1e94a133acb8947847e80bf2a93e7e867844b93.jpg)  
Notes. (1) Adopted from Quan and Ren (2010). (2) See algorithms 1–3 in Yu et al. (2023). (3) Adopted from Song et al. (2018).

Figure 4. (Color online) The Effects of Eight Discrete Emotional Expressions Embedded in Content on Article Cascade (a) Depth, (b) Size, (c) Maximum Breadth, and (d) Structural Virality

(a)  
![](/api/attachments/7C5YXCJR/fulltext/images/2b42ab1771cbb4597492ed307ef14ac8d51c7cd88e14d50c044073872ce557b6.jpg)

(b)  
![](/api/attachments/7C5YXCJR/fulltext/images/55ffbbb051d69fd9bfc0e2cdd5316890ea91e0ddaa334c406d46ac5894d2cb9c.jpg)

(c)  
![](/api/attachments/7C5YXCJR/fulltext/images/967e6f9b3e40e5edfea6703cc20eebcd3d4bbb639bbe763e988d7ce91c7b933c.jpg)

(d)  
![](/api/attachments/7C5YXCJR/fulltext/images/5929cf080aa06279f81d52fc29de8d8b2e4d127f7eb40d5ff56ec3d04c3dfca4.jpg)

Notes. The x-axis displays the size of model coefficients. The u-axis displays eight discrete emotional expression. The squares in the middle of the intervals represent mean values. The intervals covered by dashed lines represent 90% confidence intervals. The intervals covered by solid line represent mean values plus or minus one unit of their standard deviations.

measured by the average number of friends during the observation period. Our results indicate that higher levels of expression of anxiety, disgust, anticipation, and love are all associated with a greater average number of friends among users participating in the cascades. Conversely, increased expression of anger and surprise are associated with cascades involving individuals with fewer friends on average. Lastly, our findings indicate that articles expressing higher levels of anger, anxiety, and love lead to a smaller proportion of weak ties among users participating in the cascades. In contrast, expression of sadness and surprise have a significant positive impact on the proportion of weak ties among such users.

The results are generally aligned with our theoretical discussion in Section 3.3. However, there are some new insights in the results. High-degree individuals are more likely to share content that conveys disgust. This seems to contradict their motivation of managing prosocial images. However, research also shows that disgust can make content viral because of gloating effect (Heath et al. 2001). Hence, sharing such content can be a strategy for high-degree individuals to maintain their social impact. Furthermore, older users are more likely to share content expressing surprise, and content with sad expression diffuses more through weak ties. These results open new opportunities for future research to explore the psychological and behavioral processes behind the relationships.

## 7. Robustness Checks

To check the robustness of our findings, we devised a series of alternative model specifications and compare their results with our main findings. We first employ a random effects model (Baltagi and Baltagi 2008) as specified below:

$$
\begin{array}{l} y _ {i j} = \boldsymbol {\beta} ^ {\prime} \text {emotion} _ {i j} + \gamma^ {\prime} \text {article} _ {i j} + \eta^ {\prime} \text {account} _ {i} \\ \quad + A c c o u n t _ {R E i} + \epsilon_ {i j}, \end{array}\tag{2}
$$

where, in this model, we retain the term Account to capture the account-level random effects on the outcomes, assuming linear relationships between diffusion outcomes and regressors in contrast to the partial linear relationships in our proposed model.

Second, although the random effects model addresses the issue of dependent articles within the same account, it may still suffer from endogeneity concerns. For instance, unobserved account features may be correlated with both the outcomes and the input variables. To mitigate these concerns, we implemented a fixed effects model as shown in Model (3) (Baltagi and Baltagi 2008). As with the random effects model, this specification assumes linear relationships between diffusion outcomes and regressors:

$$
y _ {i j} = \boldsymbol {\beta} ^ {\prime} \text { emotion } _ {i j} + \boldsymbol {\gamma} ^ {\prime} \text { article } _ {i j} + A c c o u n t _ {F E i} + \epsilon_ {i j},\tag{3}
$$

where $A c c o u n t _ { F E i }$ indicates the account fixed effects.

Lastly, as discussed in Section 5, the assumption of linear relationships between the regressors and the outcome in the previous two models may be contentious given the potential for interaction effects and higher order effects, such as U-shaped effects. Thus, as the third alternative model, we applied a partially linear framework, following the approach outlined in our main model, to the random effects model, as detailed in Model (4):

$$
y _ {i j} = \boldsymbol {\beta} ^ {\prime} \text {emotion} _ {i j} + g _ {0} (\text {article} _ {i j}, \text {account} _ {i}) + A c c o u n t _ {R E i} + \epsilon_ {i j},\tag{4}
$$

where, in this model, we employ the nonlinear function $g _ { 0 }$ to represent the impact of article and account characteristics on the cascade dimensions. $\epsilon _ { i j }$ denotes independent and stochastic errors.

We then report the results of the above three alternative model specifications along with those from our main model in Online Table EC.12.4.<sup>6</sup> Our results show that, whereas estimates across linear and nonlinear model specifications largely align, discrepancies emerge in the impact of the expression of surprise and anticipa tion. This divergence likely arises from the nonlinear relationship between control variables and outcome variables, which the DML framework addresses. After relaxing the linear constraints using the DML framework, our findings regarding the effects of surprise and anticipation expression align more closely with our the oretical predictions and existing literature (Vosoughi et al. 2018). Moreover, there is a slight variance in the magnitude of estimates across linear and partial linear specifications, further suggesting the existence of nonlinear relationships.

Meanwhile, between the two nonlinear specifications, we observe that the magnitudes of our main model’s coefficients are greater than those in models without the instrument. This difference could be attributed to several reasons. First, if we assume that the relationship between emotional expression and diffusion is purely correlational and influenced by unobserved factors (such as both being driven by uncontrolled topics), we expect to see insignificant or smaller coefficients in the IV model. However, the increased magnitude in the IV model contradicts this assumption and suggests that the effects of our interest are not merely correlational. Second, the difference between models with and without IV may result from a negative relationship between the omitted variables and the cascades’ structural proper ties (Wooldridge 2002) or from a measurement error in the intensity scores of emotional expression (Yang et al. 2018), both of which are addressed through the implementation of the instrument.

Third, it is possible that such a gap is introduced by the weakness of the IV (Lal et al. 2024), as elaborated in Section 5, and we conduct the weak instrument test to mitigate this concern. Fourth, with the IV method, a local average treatment effect (LATE) is estimated rather than an average treatment effect (ATE) as estimated by an OLS method. Because LATE focuses on the treatment effect on the effectively treated population, whereas ATE focuses on the whole population, there could be a difference in the estimated coefficients. Lastly, although the gap may theoretically be attributed to the misspecification of the model’s functional form, in our case, DML makes few assumptions about the functional relationship between regressors and outcomes.

However, it is important to acknowledge that our IV approach is not without limitations. Whereas our model may not provide an entirely unbiased estimate of the effect size, we focus more on interpreting the direction of the treatment effects in this paper, particularly when statistically significant effects of emotional expression are consistently observed across models.

To further ensure the robustness of our findings, we performed a series of additional analyses, detailed in Online Appendix EC.10. First, we analyze the consistency between the emotions expressed in articles and in reader comments, particularly focusing on articles in which one emotion is statistically dominant (see Online Appendix EC.10.1). The results show a strong alignment between article and comment emotions, offering evidence for the existence of the affective reaction pathway (possibly driven by emotional contagion) suggested by the EASI framework. Second, we use alternative sets of emotional words: those less dependent on context. Specifically, the emotional words were rated by participants in online surveys for context independence, and we reran our main model, finding qualitatively consistent results except that disgust shows a positive effect on the maximum breadth of articles’ cascades (see Online Appendix EC.10.2). As such, we further mitigate the concern that the estimates are confounded by contextual factors. Third, we replicate our analysis on several alternative samples: (i) excluding articles with videos and shorter texts, (ii) excluding the top 10% most diffused articles, (iii) focusing on emotions expressed in the first 200 words of articles,<sup>7</sup> and (iv) retaining only frequently occurring emotion words (see Online Appendix EC.10.3). Across all these samples, our findings remain generally consistent. Notably, when presented in the first 200 words of an article, disgust shows a positive impact on the maximum breadth of articles’ cascades. These analyses address the issues of sample selection and the fact that readers may have limited attention and sometimes not complete reading an article before sharing it.

Additionally, we tested alternative model specifications: (i) removing topic-related control variables to demonstrate that the instrument approach has sufficiently addressed the confounding effects of topics, (ii) using the simulation-based SIMEX method to correct for potential measurement errors Yang et al. (2018), (iii) controlling for article originality, (iv) applying an OLS model with CSEs, and (v) accounting for the time of day when articles were posted. Furthermore, we implemented a fixed-effects instrumental variable model to vali date the effects of discrete emotional expression on demographics and social ties of the cascades and employed a robustness check of our IV using the method of Lal et al. (2024) (see Online Appendix EC.10.4). Across all these robustness checks, the results remain qualitatively consistent with our main findings (note that a decrease in the statistical significance of the estimates generated by the last analysis, i.e., applying the fixed effects IV model to the demographics and social ties data, is observed, because of the factor that random effects models produce more efficient estimators than fixed effects ones do).

Further, to better motivate our focus on the discrete emotions, we employ an additional analysis to compare the predictive power of discrete emotion with that of valence and arousal as detailed in Online Appendix EC.7. Our analysis results show that the discrete emotions possess predictive power comparable to valence and arousal in predicting the cascade’s structural properties. This further motivates our study to examine the underexplored causal effects of discrete emotions on online content diffusion.

Lastly, we conducted a placebo test by randomly assigning emotion vectors to articles and found no significant results, further confirming that our observed effects are not artifacts of a large sample size (see Online Appendix EC.10.5).

## 8. Discussions and Implications

We present some of the first comprehensive, large-scale empirical evidence demonstrating that eight discrete emotional expression significantly influence diffusion patterns and processes. On one hand, our findings show consistencies with existing studies that utilize small scale data sets or laboratory settings. For instance, in line with Berger and Milkman (2012), we find that anxiety and surprise can lead to more social transmissions of articles, whereas sadness exhibits a negative impact on transmission. We observe that negative emotions are associated with larger negative impacts than positive emotions on article transmissions.

On the other hand, our study enhances the understanding of emotional expression in content diffusion in the following ways. First, previous research suggests that valence and arousal influence content-sharing deci sions (Berger and Milkman 2012, Stieglitz and Dang-Xuan 2013). For example, Berger and Milkman (2012) find that positive and high-arousal emotions are more viral. However, our study provides a more nuanced understanding by demonstrating that emotions with similar valence and arousal levels (e.g., anxiety versus anger, love versus joy) can have significantly different impacts on content diffusion. We observe that content with more expression of anxiety and love is associated with deeper, larger, broader, and more viral diffusion in social networks, which is the opposite of what is observed with anger and joy.<sup>8</sup> These findings show that it is necessary to delve into the level of specific discrete emotions and go beyond valence and arousal when investigating the impacts of emotions in content diffusion.

Further, previous research primarily focuses on individuals’ sharing decisions and the general popularity of content without delving into diffusion dynamics from a network perspective (Goel et al. 2015, Vosoughi et al. 2018). By utilizing a unique, large-scale, and detailed data set, we investigate the impact of specific discrete emotional expression embedded in content on the individuals who disseminate content in social networks, the social relationships involved, and the structural properties of diffusion cascades. Current theories in social psychology and IS may not fully address these outcomes, thus presenting new opportunities for future theoretical and empirical investigations.

Additionally, our research builds upon existing studies through its empirical strategy. Leveraging recent advancements in discrete emotion detection methods (Yu et al. 2023), we can identify emotional expression in content on a very large scale, accounting for domain specificity and the evolution of emotional expression. Further, our econometric approach improves upon past studies that relied on ordinary linear models (Berger and Milkman 2012, Stieglitz and Dang-Xuan 2013, Brady et al. 2017, Wang and Lee 2020) by addressing random effects, nonlinearity, measurement errors, and selection bias because of unobservables. Our work, thus, represents a more reliable field test although we acknowledge that the method can be potentially improved through randomized experiments or natural experiments with exogenous shocks. However, such experiments in field contexts might be rare.

For practitioners, our study provides valuable insights for content creators and platforms. Our method of measuring an article’s emotional expression based on objective word-level emotional expression enables straightforward interpretations and actionable strategies. First, content creators can be more informed about the implications of their expression of emotions in their writing. For example, by leveraging our emotiondetection methodology and empirical findings, platforms can formulate content-generation guidelines and develop intelligent writing support systems that provide real-time feedback on the prospective effects of emotional expression (Yin et al. 2017). It is crucial that such systems do not intentionally promote manipulative or inauthentic emotional expression.

Second, from a platform design perspective, new knowledge of emotions and cascade structures helps us to predict the impact of platform design on content diffusion. For example, our work identifies how emotions are associated with structural virality in diffusion. Practitioners may leverage these findings to predict which types of discrete emotional expression may be more commonly seen in content diffusion if the platform strengthens the viral features (platforms built-in tools and functionalities that facilitate the rapid peer-to-peer spread of content). Similarly, the effects of emotional expression that are likely to impact cascade breadth would be moderated if managers implement new information broadcasting tools on platforms.

Third, platform managers can leverage our results to regulate content with emotional expression that may lead to undesirable information diffusion. Our work implies that emotional expression may be strategically leveraged by content creators to manipulate information diffusion. Relatedly, previous research suggests that surprising content contributes to the social transmission of fake news (Vosoughi et al. 2018). Using ou models, platforms can detect content with excessive emotional expression and anticipate its likely diffusion pattern, allowing for timely interventions. Our results imply that practitioners seeking to regulate the diffusion of social media content should pay more attention to love, surprise, and especially anxiety as these emotions can contribute to large information cascades. Finally, whereas one might believe that it is sufficient to focus on key opinion leaders’ broadcasting behaviors to regulate diffusion, our work shows that the impact of most emotional expression on content diffusion may be both through broadcasting (breadth) and peer-to-peer diffusion (structural virality).

## 9. Limitations and Future Research

Limitations of our work may pave the way for future research. First, existing psychological research has not reached a consensus on the fundamental categories of discrete emotions in humans. Although our study uses a relatively comprehensive set of discrete emotions, future research may consider examining the impact of other emotions, such as contempt, fear, shame, and guilt, on the information-cascading process. The interactions of these emotions with various social and psychological processes also warrant exploration.

Second, although we performed a series of robustness checks to validate the use of our instrumental variables, we acknowledge that our IV approach, using the lagged emotional intensities of previous articles posted by the same publishers as the instruments, is not without potential limitations. Although the use of lagged explanatory variables as IV is a well-established practice and recommended by previous literature (Villas-Boas and Winer 1999, Reed 2015), this approach is inherited with assumptions, including the strength of instruments and the absence of serial correlation among the unobservables. To address the first concern, we conducted a weak instrument test, and the results suggest that our instrument is strong. The latter assumption, however, is hardly testable. Whereas we have incorporated the CSEs and the random effects in our model to mitigate this and our results remain qualitatively consistent through a battery of robustness checks, we acknowledge the potential limitations of our approach, which may introduce bias in the estimated effect sizes. As a result, this paper focuses on interpreting the direction of the effects rather than the magnitudes. Future research could further explore and address the potential biases in the estimation process. Further, our models are based on existing research (Berger and Milkman 2012, Nguyen et al. 2020) that assumes the effects of discrete emotional expression are linear and additive. Future studies may go beyond this assumption and investigate nonlinear relationships.

Third, whereas our empirical investigation delves into the impact of emotional expression on various dimensions of structural properties, including breadth, size, depth, and structural virality, we do not make such distinctions in our theory development. The current literature also falls short in this regard. Addressing this gap presents an avenue for future research. Fourth, an area our paper does not address, and which presents a valuable opportunity for future research, is the impact of different viral channels (direct messaging and newsfeed broadcasting) in disseminating online content with varied emotional expression. Whereas our data tracks the transmission of online articles through various social ties and individuals, it does not distinguish between the specific channels of transmission. Fifth, the leading-edge emotion analysis method in empirical research operates at the word level, and our study is grounded in this technique. Analyzing at the word level provides more direct and actionable insights for authors compared with an entire document-level emotional analysis. Nonetheless, the development of large-scale emotion analysis at the level of entire documents stands as a crucial direction for forthcoming research in natural language processing.

Finally, whereas our supplementary analysis using only the first 200 words of the articles reveals qualitative consistency with most of our main full-article results, we observe that a higher degree of disgust in the article’s opening paragraphs has a significant positive impact on its cascade’s maximum breadth. Future research could further investigate this discrepancy and explore the effects of emotional words across different sections of an article. Moreover, future research could investigate how the impact of emotional expression on content diffusion varies across different topics.

## Acknowledgments

Yifan Yu and Shan Huang contributed equally to this work. The data used in this analysis is de-identified and anonymous. The authors thank the senior editor, associate editor, and reviewers for insightful comments and constructive suggestions.

## Endnotes

<sup>1</sup> Viral channels on WeChat include direct messaging (chat and group chat) and Moments (Newsfeed) broadcasting. These viral channels are typical for social media platforms, similar to Facebook. Our setting aligns closely with practice, in which different channels are always available for individuals to spread information. On WeChat, chat and Moments occur among first degree friends, direct contacts. Group chats can happen among acquaintances, individuals who are not first degree friends but participate in the same group chats. This relationship qualifies as a tie because it enables information diffusion within the group chat. It is considered weak as these users are not direct contacts and are unlikely to be close to each other.

<sup>2</sup> More detailed discussion is shown in Online Appendix EC.11.

<sup>3</sup> Negation and degree words are frequently used in Chinese and, thus, are helpful for accurate emotion analysis (Quan and Ren 2010). We adopt a negation word dictionary provided by TextMind, a Chinese language psychological analysis system developed by the Chinese Academy of Sciences. The dictionary contains 31 frequently used negation Chinese words. We used 60<sup>◦</sup> words provided by Ren-CECps as our degree-word dictionary and annotated their degree values. For example, the degree value of the word meaning “the most” in Chinese is annotated as 1.5, and that of the word meaning “kind of” is annotated as 0.8.

Online Appendix EC.4 demonstrates that the measurements generated by the algorithm are not statistically different from those developed by human coders.

The accounts in our context are categorized as individual, media, corporation, government, and unknown.

<sup>6</sup> The results from the three alternative models are reported in the first three sections of the table, respectively. Our main results are reported in the last section.

<sup>7</sup> The median length of the articles is 593 words. Hence, we choose the first 200 words as a proxy for the opening paragraphs of an article.

8 Anger is found to be negatively associated with article transmission in our study, whereas Berger and Milkman (2012) find positive impacts instead. It is worth noting the differences in sampl and methodologies between the two studies. For example, our sampl is drawn from large-scale and diverse information sources (official accounts), whereas Berger and Milkman (2012) examines only New York Times articles. Methodologically, we focus on word-level emotional expression using a computational approach, whereas they pri marily rely on human raters to measure article-level emotions.

## References

Anderson M (2015) Men catch up with women on overall social media use. Pew Research Center (August 28), https://www. pewresearch.org/short-reads/2015/08/28/men-catch-up-withwomen-on-overall-social-media-use/

Baltagi BH, Baltagi BH (2008) Econometric Analysis of Panel Data, vol. 4 (Springer, Cham, Switzerland).

Berger J (2011) Arousal increases social transmission of information Psych. Sci 22(7):891-893

Berger J (2014) Word of mouth and interpersonal communication: A review and directions for future research. J. Consumer Psych. 24(4):586–607.

Berger J, Iyengar R (2013) Communication channels and word of mouth: How the medium shapes the message. J. Consumer Res. 40(3):567–579.

Berger J, Milkman KL (2012) What makes online content viral? J. Marketing Res. 49(2):192–205.

Blei DM, Ng AY, Jordan MI (2003) Latent dirichlet allocation. J. Machine Learn. Res. 3:993–1022.

Brady WJ, Wills JA, Burkart D, Jost JT, Van Bavel JJ (2019) An ideological asymmetry in the diffusion of moralized content on social media among political leaders. J. Experiment. Psych. General 148(10):1802–1813.

Brady WJ, Wills JA, Jost JT, Tucker JA, Van Bavel JJ (2017) Emotion shapes the diffusion of moralized content in social networks. Proc. Natl. Acad. Sci. USA 114(28):7313–7318.

Carstensen LL, Fung HH, Charles ST (2003) Socioemotional selectivity theory and the regulation of emotion in the second half of life. Motivation Emotion 27:103–123.

Chernozhukov V, Chetverikov D, Demirer M, Duflo E, Hansen C, Newey W, Robins J (2018) Double/debiased machine learning for treatment and structural parameters. Econometrics J. 21(1): C1–C68.

Clark MS, Taraban C (1991) Reactions to and willingness to express emotion in communal and exchange relationships. J. Experi ment. Soc. Psych. 27(4):324–336.

Cotten SR, Schuster AM, Seifert A (2022) Social media use and well being among older adults. Current Opinion Psych. 45:101293.

Dev H, Karahalios K, Sundaram H (2019) Quantifying voter biases in online platforms: An instrumental variable approach. Lampinen A, Gergle D, Shamma DA, eds. Proc. ACM Human-Comput. Interaction, vol. 3 (Association for Computing Machinery, New York), 1–27.

Festinger L (1954) A theory of social comparison processes. Human Relations 7(2):117–140.

Finkenauer C (1998) Secrets: Types, determinants, functions, and consequences. Unpublished doctoral dissertation, University of Louvain at Louvain-la-Neuve, Belgium.

Goel S, Anderson A, Hofman J, Watts DJ (2015) The structural viral ity of online diffusion. Management Sci. 62(1):180–196.

Gorodnichenko Y, Pham T, Talavera O (2023) The voice of mone tary policy. Amer. Econom. Rev. 113(2):548–584.

Hatfield E, Cacioppo JT, Rapson RL (1993) Emotional contagion. Current Directions Psych. Sci. 2(3):96–100.

He Y, Bond SD (2013) Word-of-mouth and the forecasting of con sumption enjoyment. J. Consumer Psych. 23(4):464–482.

Heath C, Bell C, Sternberg E (2001) Emotional selection in memes: The case of urban legends. J. Personality Soc. Psych. 81(6): 1028–1041.

Heerdink MW, Koning LF, Van Doorn EA, Van Kleef GA (2019) Emotions as guardians of group norms: Expressions of anger and disgust drive inferences about autonomy and purity viola tions. Cognition Emotion 33(3):563–578.

Hennig-Thurau T, Wiertz C, Feldhaus F (2015) Does Twitter matter? The impact of microblogging word of mouth on consu mers’ adoption of new movies. J. Acad. Marketing Sci. 43(3): 375–394.

Jiang L, Yin D, Liu D (2019) Can joy buy you money? The impact of the strength, duration, and phases of an entrepreneur’s peak displayed joy on funding performance. Acad. Management J. 62(6):1848–1871.

Kahn JH, Tobin RM, Massey AE, Anderson JA (2007) Measuring emotional expression with the linguistic inquiry and word count. Amer. J. Psych. 120(2):263–286.

Keltner D, Haidt J (1999) Social functions of emotions at four levels of analysis. Cognition Emotion 13(5):505–521.

Kensinger EA (2008) Age differences in memory for arousing and nonarousing emotional words. J. Gerontology Ser. B Psych. Sci. Soc. Sci, 63(1):P13-P18

Lal A, Lockhart M, Xu Y, Zu Z (2024) How much should we trust instrumental variable estimates in political science? Practical advice based on 67 replicated studies. Political Anal. 32(4):521–540.

Lapinski MK, Rimal RN (2005) An explication of social norms. Comm. Theory 15(2):127–147.

Lerner JS, Small DA, Loewenstein G (2004) Heart strings and purse strings: Carryover effects of emotions on economic decisions Psych. Sci. 15(5):337–341.

Lerner JS, Li Y, Valdesolo P, Kassam KS (2015) Emotion and deci sion making. Annual Rev. Psych. 66:799–823.

Lin X, Wang X (2020) Examining gender differences in people’s information-sharing decisions on social networking sites. Internat. J. Inform. Management 50:45–56.

Luna T, Renninger L (2015) Surprise: Embrace the Unpredictable and Engineer the Unexpected (TarcherPerigee, New York).

Malik M, Hussain A (2017) Helpfulness of product reviews as a function of discrete positive and negative emotions. Comput Human Behav.

Mikolov T, Chen K, Corrado G, Dean J (2013) Efficient estimation of word representations in vector space. Preprint, submitted January 16, https://arxiv.org/abs/1301.3781.

Nguyen H, Calantone R, Krishnan R (2020) Influence of social media emotional word of mouth on institutional investors decisions and firm value. Management Sci. 66(2):887–910.

Pang B, Lee L (2005) Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales. Knight K, Ng HT, Oflazer K, eds. Proc. 43rd Annual Meeting Assoc. Com put. Linguistics (Association for Computational Linguistics, Ann Arbor, MI), 115–124.

Plutchik R (2001) The nature of emotions: Human emotions have deep evolutionary roots, a fact that may explain their complexity and provide tools for clinical practice. Amer. Sci. 89(4):344–350.

Quan C, Ren F (2010) A blog emotion corpus for emotional expression analysis in Chinese. Comput. Speech Language 24(4): 726–749.

Reed WR (2015) On the practice of lagging variables to avoid simultaneity. Oxford Bull. Econom. Statist. 77(6):897–905.

Rime ´ B (2009) Emotion elicits the social sharing of emotion: Theory and empirical review. Emotion Rev. 1(1):60–85.

Rui H, Liu Y, Whinston A (2013) Whose and what chatter matters? The effect of tweets on movie sales. Decision Support Systems 55(4):863–870.

Sargan JD (1958) The estimation of economic relationships using instrumental variables. Econometrica 26(3):393–415.

Scherer KR (2001) Appraisal considered as a process of multilevel sequential checking. Scherer KR, Schorr A, Johnstone T, eds. Appraisal Processes in Emotion: Theory, Methods, Research (Oxford University Press, Oxford, UK), 92–120.

Shi Z, Rui H, Whinston AB (2014) Content sharing in a social broadcasting environment: Evidence from Twitter. MIS Quart. 38(1):123–142.

Song Y, Shi S, Li J, Zhang H (2018) Directional skip-gram: Explicitly distinguishing left and right context for word embeddings. Walker M, Ji H, Stent A, eds. Proc. 2018 Conf. North Amer. Chap ter Assoc. Comput. Linguistics Human Language Tech. Vol. 2 (Short Papers) (Association for Computational Linguistics, New Orleans, LA), 175–180.

Stieglitz S, Dang-Xuan L (2013) Emotions and information diffusion in social media—Sentiment of microblogs and sharing behavior. J. Management Inform. Systems 29(4):217–248.

Stock J, Yogo M (2005) Testing for Weak Instruments in Linear IV Regression (Cambridge University Press, New York), 80–108.

Tomkins SS (1962) Affect Imagery Consciousness: Volume I: The Positive Affects (Springer Publishing Company, New York).

Van den Bulte C, Bayer E, Skiera B, Schmitt P (2018) How customer referral programs turn social capital into economic capital. J. Marketing Res. 55(1):132–146.

Van Kleef GA (2009) How emotions regulate social life: The emotions as social information (EASI) model. Current Directions Psych. Sci. 18(3):184–188.

Van Kleef GA (2010) The emerging view of emotion as social infor mation. Soc. Personality Psych. Compass 4(5):331–343.

Villas-Boas JM, Winer RS (1999) Endogeneity in brand choice mod els. Management Sci. 45(10):1324–1338.

Vosoughi S, Roy D, Aral S (2018) The spread of true and false news online. Science 359(6380):1146–1151.

Wang X, Lee EW (2020) Negative emotions shape the diffusion of cancer tweets: Toward an integrated social network–text analytics approach. Internet Res. 31(2):401–418.

Wooldridge JM (2002) Econometric Analysis of Cross Section and Panel Data, 2nd ed. (The MIT Press, Cambridge, MA).

Xiao Y, Zhang H, Cervone D (2018) Social functions of anger: A competitive mediation model of new product reviews. J. Prod uct Innovation Management 35(3):367–388.

Xue B, Fu C, Shaobin Z (2014) A study on sentiment computing and classification of Sina Weibo with Word2vec. IEEE Internat. Congress Big Data (IEEE, Piscataway, NJ), 358–363.

Yang M, Adomavicius G, Burtch G, Ren Y (2018) Mind the gap: Accounting for measurement error and misclassification in variables generated via data mining. Inform. Systems Res. 29(1):4–24.

Yin D, Bond S, Zhang H (2014) Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. MIS Quart. 38(2):539–560.

Yin D, Bond S, Zhang H (2017) Keep your cool or let it out: Nonlinear effects of expressed arousal on perceptions of consumer reviews. J. Marketing Res. 54(3):447–463.

Yin D, Bond SD, Zhang H (2021) Anger in consumer reviews: Unhelpful but persuasive? MIS Quart. 45(3):1059–1086.

Yu Y, Yang Y, Huang J, Tan Y (2023) Unifying algorithmic and theoretical perspectives: Emotions in online reviews and sales. MIS Quart. 47(1):127–160.

Copyright of Information Systems Research (INFORMS) is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
