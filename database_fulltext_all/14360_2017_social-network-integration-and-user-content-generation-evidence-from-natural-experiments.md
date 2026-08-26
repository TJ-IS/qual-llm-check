---
otero_id: 14360
otero_key: "3M9QE3DQ"
title: "SOCIAL NETWORK INTEGRATION AND USER CONTENT GENERATION: EVIDENCE FROM NATURAL EXPERIMENTS"
authors: "Ni Huang; Yili Hong; Gordon Burtch"
year: "December 2017"
journal: "MIS Quarterly"
doi: "10.25300/misq/2017/41.4.02"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# SOCIAL NETWORK INTEGRATION AND USER CONTENT GENERATION: EVIDENCE FROM NATURAL EXPERIMENTS<sup>1</sup>

Ni Huang W. P. Carey School of Business, Arizona State University, 300 E. Lemon Street, Tempe, AZ 85287 U.S.A. {ni.huang@asu.edu}

Yili Hong W. P. Carey School of Business, Arizona State University, 300 E. Lemon Street, Tempe, AZ 85287 U.S.A. {hong@asu.edu}

Gordon Burtch Carlson School of Management, University of Minnesota, 321 19<sup>th</sup> Avenue South, Minneapolis, MN 55455 U.S.A. {gburtch@umn.edu}

This study examines how social network integration (i.e., integration of online platforms with other social media services, for example, with Facebook or Twitter) can affect the characteristics of user-generated content (volume and linguistic features) in the context of online reviews. Building on the social presence theory, we propose a number of hypotheses on how social network integration affects review volume and linguistic features of review text. We consider two natural experiments at leading online review platforms (Yelp.com and TripAdvisor.com), wherein each implemented a social network integration with Facebook. Constructing a unique panel dataset of online reviews for a matched set of restaurants across the two review sites, we estimate a difference-in-differences (DID) model to assess the impact of social network integration. We find that integration with Facebook increased the production of user-generated content and positive emotion in review text, while simultaneously decreasing cognitive language, negative emotion, and expressions of disagreement (negations) in review text. Our findings demonstrate that social network integration works as a double-edged sword. On the one hand, integration provides benefits in terms of increased review quantity. On the other hand, these benefits appear to come at the cost of reduced review quality, given past research which has found that positive, emotional reviews are perceived by users to be less helpful. We discuss the implications of these results as they relate to the creation of sustainable online social platforms for user content generation.

Keywords: Social network integration, online reviews, natural experiment, difference-in-differences, text analytics

“Humans are different in private than in the presence of others. While the private persona merges into the social persona in varying degrees, the union is never complete. Something is always held back.”

– Brian Herbert, House Corrino, 2001

## Introduction

Many online platforms have sought to supplement their homegrown communities by integrating with prominent social networking sites like Facebook, Twitter, and Google+, a practice known as social network integration (Blanchard 2011). Examples of social network integration include social login (Kontaxis et al. 2012), Facebook Connect (Holliday 2009), and instant personalization (Kincaid 2010). Social login allows a new user to register an account with an online platform using an existing account at a social networking service, for example, Facebook (Frutiger et al. 2014). Once a user grants a platform access to their existing social networking account, Facebook Connect enables automatic or user-controlled social sharing of the user’s activities on the platform, back to the social networking site (for instance, sharing Yelp reviews on Facebook pages). Facebook’s instant personalization option enables even greater levels of integration, because it allows the partner platform to access and make use of Facebook profile information, including the user’s name, geographic location, and social connections (Rapp et al. 2013). In sum, social network integration facilitates convenient user account creation and login, provides for a more personalized user experience, and promotes a greater perception of social presence (e.g., cognizance of one’s audience, typically their friends).

The objective of this study is to examine how social network integration affects the volume and characteristics of user content generation, particularly in the context of online reviews. We explore how social network integration influences review volumes and the linguistic features of review text. In terms of linguistic features, we place a specific focus on the occurrence of (1) affective content, that is, words indicative of feelings and emotion, such as happy, sad, or cried (Epstein 1993; Gill et al. 2008), which may vary in both valence (positive versus negative) and intensity (Gilovich et al. 2002; Shiv and Fedorikhin 1999); (2) cognitive content, that is, words suggestive of reasoning and information processing, such as cause, know, or ought (O’Neill 2002; Pennebaker and Francis 1996); and (3) negative language, that is, words related to negation and disagreement, such as no, not, or never (Horn 2010; Lasersohn 2005). Formally, we seek to investigate the following research question:

How does social network integration affect user content generation (online reviews), in terms of volume, the exhibition of affective and cognitive language, and use of negative language?

We propose that social network integration may instigate changes in the volume and linguistic features of reviews by increasing social presence on a website. For example, in terms of the volume of content produced, there are two plausible countervailing mechanisms by which social network integration may cause differences. On the one hand, social network integration may result in more content production because it leads to increased social interaction, which provides a greater opportunity for individuals to gain social benefits from the content they produce (Dellarocas 2003; Lampel and Bhalla 2007; Zhang and Zhu 2011).<sup>2</sup> On the other hand, social integration may cause a decrease in content production, because it may lead users to tailor or even cease their content generation (Das and Kramer 2013; Sleeper et al. 2013), out of fear of social disapproval by the newly (socially) proximal audience.

Social network integration may also impact the characteristics of content that is produced, for at least two reasons. First, social network integration may drive a shift in the composition of the user base by inducing selection into the platform; by facilitating the entry of a new group of individuals, who might then produce systematically different content because they hold inherently different personal traits. Second, social network integration may cause existing users to change the nature of the content they produce. Specifically, social network integration, by increasing social presence, may trigger existing users to exhibit feelings and emotions with greater intensity when authoring reviews (Gilovich et al. 2002; Shiv and Fedorikhin 1999), at the expense of cognitive processing (De Martino et al. 2006; Kahneman 2011). Additionally, social integration, by increasing social presence, may reduce individuals’ tendency to employ negations, which are indicative of negativity or disagreement (Davis et al. 2002; Moor et al. 2010).

Grounded in social presence theory (Short 1974; Short et al. 1976), we propose several hypotheses relating social network integration to the quantity and linguistic features of online reviews. We analyze a unique data set comprised of online reviews for a set of matched restaurants across two comparable, leading online review websites. We code the linguistic features of the review text using Linguistic Inquiry and Word Count (LIWC), a tool we describe in greater detail in the methodology section. Our econometric identification strategy hinges on two natural experiments: temporally staggered social network integrations on Yelp.com and TripAdvisor. com. These natural experiments allow us to infer the causal effects of social network integration via a difference-indifferences model (Fricke 2015; Frohlich 2004).

Our results show that social network integration increases the volume of online reviews that are authored, due to a combination of more rapid user entry and an increase in average reviewing activity amongst existing users. Moreover, we find that integration leads to changes in the linguistic features of reviews; we observe that emotional, affective language increases while cognitive language declines. Further, we observe a decline in users’ tendency to employ negation terms, indicative of disagreement. Finally, a series of subsequent user-level analyses demonstrate that the changes we observe are driven primarily by shifts in user behavior, rather than shifts in user composition (i.e., self-selection).

Our study contributes to the literature on user content generation and the design of online review systems. While past research has primarily focused on the consequences of online reviews, our study provides a pioneering effort in understanding how an important system design feature—social network integration—affects review volumes and linguistic features of review text, by increasing social presence. Given the recent trend of online platforms toward promoting social network integration, it is crucial that we improve our understanding of the collateral consequences.

The findings of our study also carry important implications for the design of IT platforms that host and heavily rely upon user-generated content. On the one hand, social network integration appears to be a boon for online review sites. Social network integration appears to increase content production, which is likely to be desirable to online review platforms, which are known to face an under-provisioning problem (Avery et al. 1999; Burtch et al. 2017). On the other hand, social network integration also has its downsides. Considering the past literature’s observation that consumers’ perceive negative reviews to be more helpful (Chen and Lurie 2013; Rozin and Royzman 2001), and emotional reviews as less helpful (Baumeister et al. 2001; Hong et al. 2016; Yin et al. 2014), the fact that we see (1) a shift away from cognitive language toward emotional language, (2) that the latter manifests primarily as positive emotions, and (3) that consumers employ fewer negations, suggests that, despite the apparent benefits of greater review volumes, social network integration may lead to content that is perceived to be less helpful, and thus of lower quality. In sum, our findings demonstrate that social network integration, and thus the associated increases in social presence, can be a double-edged sword, providing benefits in terms of increased review quantity, possibly at the cost of perceived review quality.

## Prior Literature

## Social Presence and Anonymity

Social presence was originally defined as “the degree of salience of the other person in the interaction and the consequent salience of the interpersonal relationships” (Short et al. 1976, p. 65). Modern definitions in the context of computermediated social networks refer to social presence as individuals’ awareness of their social connections in a communication interaction (Cobb 2009; Gunawardena 1995; Kehrwald 2008). The degree of social presence depends on the level of interpersonal interactions that a communication medium supports. For example, face-to-face communication tends to have the most social presence, whereas text-based communication has relatively less social presence (Cui et al. 2012; Lowenthal 2009). Social presence has been found to be a significant predictor of user behavior in computer-mediated interactions (Gunawardena and Zittle 1997; Richardson and Swan 2003). In online contexts, increased social presence has been shown to make individuals less divergent or disagreeable in their thinking (Sia et al. 2002), to facilitate “deeper” information processing, to promote a lesser breadth of information sharing (Miranda and Saunders 2003), and to lead to more socially fulfilling experiences (Jiang et al. 2013).

Prior research on social presence focuses on outcomes that largely pertain to transactions, such as trust (Ou et al. 2014), purchase intentions (Animesh et al. 2010), and product choice (Rhue and Sundararajan 2013). In contrast, the present study examines users’ possible shifts in consumers’ online reviewing behavior (in terms of volume and linguistic features) as novel outcomes that may be driven by increases in social presence on online platforms. Recent developments in social media have created the potential to increase social presence on the Internet (Kaplan and Haenlein 2010) by connecting individuals in social networks (Kane et al. 2014). In particular, online platforms have begun to implement social network integration (integration with social media services) to improve social interaction (Kontaxis et al. 2012; Wright-Porto 2011). Social network integration leads to increases in social presence on the adopting platforms (Rhue and Sundararajan 2013). As a platform changes from a relatively anonymous environment to a social environment, users are likely to adapt their behaviors to their newly proximal, salient audience (Acquisti and Gross 2006; Daughety and Reinganum 2010; Jones and Linardi 2014).

Of course, the corollary of increased social presence is the loss of anonymity. Anonymity refers to a state in which identifying information for an acting party is unknown (Hoffman et al. 1999; Pfitzmann and Köhntopp 2001). There are two sides to the argument about anonymity’s role in the literature. On one hand, anonymity is an important element in preserving information privacy (Acquisti et al. 2013; Ayyagari et al. 2011; Ba 2001; Pavlou 2011). On the other hand, anonymity contributes to online incivility, producing behaviors ranging from racism and hatred (Reader 2012; Santana 2014) to Internet trolling (Hardaker 2010; Phillips 2011) and cyber bullying (Campbell 2005). Scott and Orlikowski (2014) have recently summarized these points, arguing that anonymity is likely to be an important issue in online reviews because it may lead users to feel more comfortable and secure, resulting in more frequent contributions, while at the same time raising concerns about user regulation.

Prior studies on anonymity indicate that the presence or absence of anonymity leads individuals to adjust their information sharing behavior. For instance, with the loss of anonymity, users are more likely to publicize socially desirable information (Huberman et al. 2005). When prompted to consider their anonymity, users may become self conscious and subsequently more conservative in their information sharing (Burtch et al. 2015; John et al. 2009). Dissociative anonymity leads users to intensify their information sharing behavior, a phenomenon known as the online disinhibition effect (Suler 2004). Building on prior research, this study discusses how the loss of anonymity due to increased social presence may impact users’ engagement with online platforms and, in particular, their content contributions.

## Online Reviews and Social Interactions

The extensive literature of online reviews can be classified into two broad categories. One body of work has focused on the consequences of online reviews, conditional on their characteristics, namely volume, valence and linguistic features (e.g., Ba and Pavlou 2002; Chevalier and Mayzlin 2006; Dellarocas et al. 2007; Duan et al. 2008; Kwark et al. 2014; Mudambi and Schuff 2010; Yin et al. 2014; Zhu and Zhang 2010), whereas a second has focused on the antecedents of, and processes the underlying, review generation (e.g., Godes and Huang et al. 2016; Luca and Zervas 2016; Silva 2012). Our study aims to contribute to the latter category, considering the influence of social aspects on review generation.

Past work suggests that social factors significantly influence users’ authorship of online reviews (e.g., Aral 2014; Muchnik et al. 2013; Wang 2010; Wang et al. 2017). First, Wang (2010) observed that, given the opportunity to establish social image, consumers tend to write more reviews and give less extreme ratings. This finding suggests that users do respond to an audience. Similarly, Zhang and Zhu (2011) leveraged a natural experiment at Chinese Wikipedia to demonstrate that a larger audience size incentivizes users to contribute public content, due to potential social benefits. Other work, by Chen et al. (2010), provides further evidence for an audience effect. Those authors conducted a randomized experiment and found that providing information about the average rate of review authorship in the community could significantly increase a subject’s own rate of authorship, if they perceived that they were lagging behind that average. However, Chen et al. also found the opposite effect for individuals who were initially contributing above the average; high contributors became less engaged once they realized they were doing more than their fair share. Finally, other work suggests that individuals seek to maintain social approval, once it has been obtained. For example, Goes et al. (2014) showed that after attracting subscribers (or followers), individuals begin to author reviews more objectively, and with greater negativity and variance in valence; features that are known to be perceived as helpful.

The present study advances our understanding of the effects of social network integration, and thus social presence, on users’ authorship of online reviews. Prior work has examined the impact of social factors on contribution quantity (Chen et al. 2010; Huberman et al. 2009), rating negativity and extremity (Goes et al. 2014; Wang 2010). Here, we begin by considering the impact of social presence on review volume, but we also go further, investigating the impact on linguistic features of review content. Specifically, we provide a first consideration of the impact of social presence implemented by platform social network integration on review authors psychological processes (affect and cognition) and their use of negative language (negations).

## Hypothesis Development

In this section, we hypothesize the effects of social network integration on online review production in terms of volume and linguistic features. First, we focus on review volumes, noting that sustainable platforms require a healthy volume of content, and online reviews are subject to an underprovisioning problem (Avery et al. 1999; Burtch et al. 2017). Second, we consider reviewers’ mental processes reflected in language, that is, the use of affective (emotional) language and, conversely, cognitive language, noting prior research which has found that emotional expression can generally reduce the perceived helpfulness of online reviews (Hong et al. 2016; Yin et al. 2014). Third, and last, we consider individuals’ use of negations—words such as no, not, never— which are indicative of negativity or disagreement.

## Volume Effect

Review volumes reflect the level of user engagement and thus the sustainability of a content-based platform. Social network integration, by increasing users’ social presence and decreasing anonymity, may affect whether a user chooses to write a review. In particular, we consider multiple possible mechanisms, which may countervail one another.

First, social network integration, in the form of Facebook Connect or Instant Personalization, may lead to greater social presence, exposing a user’s reviews to his or her friends and thereby increasing the perceived relevance of the audience who may ultimately read the reviews. As such, because users are likely to be aware that their friends may benefit from their contributions to the review platform, they may believe that there is a potential for social benefits or reputational gains (Zhang and Zhu 2011). This, in turn, may stimulate users to contribute larger volumes of reviews. However, we also must consider a countervailing mechanism. Users may fear social disapproval, given a relative loss of anonymity (Kang et al. 2013). This suggests that users’ willingness to share their experiences on the review platform may decline, especially when they have had very negative experiences. This countervailing mechanism is supported by the findings of Leshed (2009), who observed that a loss of anonymity was associated with a decline in the number of comments users made in online discussion forums. Further, past research has noted that individuals often create and maintain an alternate identity in online spaces (Froomkin 1999). When individuals’ online anonymity is compromised, they may lose the ability to maintain their alternate persona (Scott and Orlikowski 2014). Although it is possible that a user could simply construct a secondary user account, from which they could post their negative experience, this would require a new added cost of time and effort, which many users may not wish to absorb.

Second, social network integration typically comes with a social login feature (e.g., login via Facebook). Such features make registration and login less time consuming. Consequently, social integration may lead to greater user enrollment and user involvement in a platform (Drebes 2011; Kontaxis et al. 2012). In turn, this may produce an increase in the volume of reviews being authored on the platform.

To summarize, social network integration may lead to multiple countervailing effects. On the one hand, review volumes may increase (1) because the greater social presence that results from social network integration creates a greater opportunity for users to pursue social image and reputational gains, and (2) because social login is likely to facilitate higher enrollment of new users and stimulate greater involvement of existing users. On the other hand, a relative loss of anonymity may cause individuals to fear social disapproval from their peers, driving them to contribute less. Bearing in mind that (1) a majority of mechanisms (social presence and social login) speak to a likely increase in review volumes, and (2) social disapproval might be avoided by creating throwaway accounts, it is more likely that the positive effects of social network integration on review volumes will dominate. Accordingly, we propose the following hypothesis:

H1: Social network integration leads to more reviews.

## Mental Process Effects

The ability of a platform to support social connections and interactions heightens perceived social presence and users awareness of other users, for example, the audience for their reviews (Cobb 2009; Kehrwald 2008). Here, we argue that increased social presence deriving from social network integration is likely to affect how users author reviews, in terms of their reliance on affective versus cognitive mental processes. Affective (emotional) processes incorporate feelings associated with the entity being evaluated, whereas cognitive (rational) processes incorporate attributes and beliefs about the entity (Millar and Tesser 1986). In the social psychology literature, it has frequently been suggested that affect and cognition are negatively correlated (Briggs 1977; Pervin and John 1999); that when affect dominates, cognition recedes, and vice versa. Recent neurophysiological evidence supports this belief, having shown that affective processes and cogni tive processes are supported by different areas of the brain (Finucane et al. 2003), that is, the anterior insula supports emotion while the dorsolateral prefrontal cortex supports cognition (Sanfey et al. 2003). Because affective and cognitive mental processes are largely associated with two opposing neural systems, when people draw on affective mental processes, they are less likely to draw on cognitive mental processes, and vice versa (De Martino et al. 2006; Talmi and Frith 2007). Bearing the above in mind, when crafting reviews, users might be expected to rely on one type of mental process (affective or cognitive) at the expense of the other. Thus, when users exhibit affective mental processes in crafting their reviews, they are likely to express their emotions in the text of their reviews (e.g., words like happy, sad, cried). When this happens, we might expect to observe a decline in cognitive mental processes, and thus a reduction in users’ application of logic and analytical thought (e.g., words like because, therefore, think). Similarly, when cognitive mental processes take hold, we might expect to observe an increase in words associated with logical and analytical thought, and a commensurate decline in words associated with emotions.

The emotional broadcaster theory of social sharing argues that individuals have an intrinsic drive to share experiences in a psychologically arousing manner (Harber and Cohen 2005). In a social environment, individuals’ emotions are activated and, therefore, they are more likely to share their feelings and emotions, a behavior commonly known as emotional leakage (Kraut 1982). Supporting this theory, Wagner and Smith (1991) and Buck et al. (1992) both found that closer social relationships (e.g., friends versus strangers) facilitate emotional expressiveness. It has also been found that, with respect to the expression of emotion, similar patterns emerge in both face-to-face communication and computer-mediated communication (Derks et al. 2008). In the context of online reviews, social network integration increases social presence on the platform, which can be expected to stimulate users emotional expressiveness, or even trigger emotional leakage. As a result, following social network integration, users are more likely to draw on affective processes when authoring reviews, and less likely to rely on cognitive processes. Therefore, we propose the following two hypotheses:

H2a: Social network integration leads to more language reflecting affective processes in review text.

H2b: Social network integration leads to less language reflecting cognitive processes in review text.

## Inhibition Effect

Increases in social presence reduce user anonymity, which has both benefits and pitfalls. A variety of studies in the group decision support systems (GDSS) literature have consistently reported that anonymity can provide the conditions necessary for the production of innovative, creative ideas (Connolly et al. 1990), and that users may exhibit a decline in social desirability concerns, as well as higher levels of self-esteem (Joinson 1999). However, online anonymity has also been shown to produce an “online disinhibition effect” (Cho et al. 2012; Suler 2004), in which individuals exhibit a greater willingness to reveal their true, uncensored opinions, thoughts, and preferences. Accordingly, individuals may be more critical, disagreeable, and argumentative when they are in an anonymous environment, with a low level of social presence (Jessup et al. 1990). Under anonymity, individuals have also been known to engage in a variety of behaviors that would otherwise meet with social disapproval, ranging from free-riding (Andreoni and Bernheim, 2009) to racism (Reader 2012; Santana 2014), Internet trolling (Hardaker 2010; Phillips 2011), and cyber bullying (Campbell 2005).

In the context of online reviews, review authors, once subject to increased social presence, may become concerned about their audience (now more likely to be comprised of offline friends) disapproving of their tone (Lee et al. 2015). Individ uals generally strive to achieve a positive social identity (Jackson et al. 1996; Oldmeadow and Fiske 2010) because they derive utility from being judged positively by others (Gneezy et al. 2012). As an anonymous interviewee reported to Kang et al. (2013, p. 2660): “I posted a very bad review [of a restaurant]. And I guess I did that [anonymously]. I live in a small town, so I certainly didn’t want to put my real name....” With increases in social presence (i.e., a decline in anonymity), we therefore expect a decline in users’ application of negative language and negations, due to an increased desire to establish a positive social identity. This leads us to our final formal hypothesis:

## H3: Social network integration leads to fewer negations in review text.

It is worth noting that the implementation of a social network integration can vary substantially, in many respects. An interesting example of this, which bears relevance to our context, is the opt-in versus opt-out nature of the integration event and the associated services and functionality made available to users. In particular, Facebook Connect was an opt-in (optional) feature, requiring that individual users explicitly choose to accept it, whereas Instant Personalization was an opt-out (mandatory) feature, imposed on users by default. To opt out of Instant Personalization, users would have been required to go through a series of steps to disable the feature. Prior literature has suggested that opt-out designs result in significantly higher likelihood of participation than opt-in designs (Johnson et al. 2002; Johnson and Goldstein 2003). This tends to happen because individuals prefer to stick with the status quo, rather than exert effort to make a change (Samuelson and Zeckhauser 1988; Thaler and Sunstein 2008), they are reference dependent, anchoring on the default option (Dinner et al. 2011; Kressel et al. 2007), and they tend to view the default choice as having the implicit endorsement of the product designer (Chapman and Johnson 1999). We might therefore expect that Instant Personalization, a mandatory integration, would have a greater impact on reviewing activity than Facebook Connect, an optional integration.

However, to reliably identify the role of such moderating conditions, it would be necessary to observe repeated treatment events under each condition. That is, a research would need to observe repeated social network integrations of an opt-in nature, as well as repeated events of an opt-out nature, to isolate the moderating influence of this particular feature.

Notably, as we detail in subsequent sections, we observe only two integration events in our sample, one each of opt-in and opt-out. As such, we are unable to draw meaningful inferences about moderation effects related to nuances of social network integration.

From an identification standpoint, we must also acknowledge that multiple mechanisms may exist which would produce the same pattern of results we have hypothesized. For example, social network integration, by increasing social presence, may stimulate greater user activity by increasing the potential for reputational gains. At the same time, it is plausible that social network integration might lead to an influx of new users, particularly those who are most active on, or comfortable with, Facebook. In turn, such active new users might also contribute to the growth in review volumes, over and above any increases in the average contributions of existing users.

Similarly, existing users might change their language use patterns (e.g., using more affective language and expressing less disagreement, as reflected by a decline in negative language and negations) in response to greater social presence on the platforms. At the same time, newly entered users, arriving as a result of social network integration, may be systematically different from existing users in their language usage, and thus may also introduce changes in the linguistic features of reviews. Ultimately, distinguishing between these various mechanisms poses a difficulty; however, in the “Secondary Analysis” section, we report on a number of secondary analyses that enable us to unravel and eliminate some of the mechanisms (most notably those related to self-selection). We also report several falsification tests, which further strengthen the identification of our study.

## Research Methodology

## Background

Our study considers two comparable online review platforms: Yelp.com and TripAdvisor.com, both of which implemented social network integrations with Facebook at different points in time. First, we consider Yelp.com’s adoption of the Facebook Connect feature on July 2, 2009 (Holliday 2009; O’Neill 2009). Facebook Connect allows users to log into a website using their Facebook account and to share reviews with friends on Facebook. Facebook Connect is an opt-in feature, in that it is up to the user to decide whether he or she would like to adopt the feature. In other words, the implementation of Facebook Connect did not require that users share their reviews on Facebook; users could choose whether or not to share their reviews, and could readily adjust the review content conditional on that decision. Figure 1 shows the review page with the Facebook Connect feature enabled for a Yelp.com user.

Second, we consider TripAdvisor.com’s adoption of Facebook’s Instant Personalization feature on December 21, 2010 (Kincaid 2010; TripAdvisor 2010). With Instant Personalization, if a user visits TripAdvisor’s website while logged into Facebook (or having logged into Facebook at any time in the prior 30 days, with cookies enabled), TripAdvisor will gain access to the user’s Facebook account information. Instant Personalization then automatically presents users with personalized website content on TripAdvisor.com that shows their Facebook friends’ travel and reviewing activities, such as recently authored restaurant and hotel reviews, and a list of Facebook friends’ most popular destinations. Instant Personalization is an opt-out feature, in that the feature is enabled by default and requires that users take a series of cumbersome actions to disable it. Although users can choose to opt out of Instant Personalization through Facebook’s privacy controls, this is reportedly challenging to do.<sup>3</sup> After Instant Personalization, users will be aware that their Facebook friends can read their reviews on TripAdvisor, and thus they are likely to change their reviewing behavior (e.g., modify their review content). Figure 2 illustrates the webpage with the Instant Personalization feature for a TripAdvisor.com user.

## Data and Measures

We collected data on restaurant reviews from Yelp.com and TripAdvisor.com for a matched set of restaurants, selected at random, located in five major cities across the United States (New York City, Los Angeles, Chicago, Philadelphia and Phoenix). The data contained all reviews of these restaurants on these two websites.<sup>4</sup> Notably, restaurant reviews have received considerable attention in the extant literature (Lu et al. 2013; Luca and Zervas 2016). The data contains time stamps and review content (ratings and text), in addition to reviewer profile and restaurant information. We created an indicator variable to mark reviews collected from Trip Advisor.com versus those collected from Yelp.com, and we then pooled the data.

![](/api/attachments/3M9QE3DQ/fulltext/images/e1f4260da1e73a913c7c05f756ed08994d51c2a8b00f89bdbace4992f9067972.jpg)  
Figure 1. Review Page with Facebook Connect Features on Yelp.com

![](/api/attachments/3M9QE3DQ/fulltext/images/b30a0d05cfeb494309b919458bd63b06923ddf3a1facac6b04b115e687a3da92.jpg)  
Figure 2. Web Page with Instant Personalization Features on TripAdvisor.com

Review volume was measured as the monthly total volume of reviews submitted to the platform about a given restaurant. To construct measures of linguistic content, we leveraged the latest version of Linguistic Inquiry and Word Count (LIWC), a text analytics tool. LIWC calculates the prevalence of different categories of words in a text document based on the percentage of words that are matched to predefined keyword dictionaries (Pennebaker et al. 2007). LIWC has frequently been used in the psychology literature, and has also recently seen increased use in the Information Systems (Goes et al. 2014; Hong et al. 2016; Yin et al. 2014) and Marketing literature (Lurie et al. 2014; Sridhar and Srinivasan 2012). We focused on LIWC’s measures of emotional, cognitive and negative language. Table 1 provides examples of words in the LIWC dictionaries for the linguistic categories we consider in this study. In addition, Table 2 presents examples of review text containing highly emotional, cognitive, or negative language on TripAdvisor.com.

We first measured the linguistic features of each review, then averaged them across reviews for each restaurant, aggregating to the monthly level, to avoid issues of sparsity (i.e., to ensure each observation included a reasonable amount of text). For the final measures used for analyses, we take two approaches and report results for them respectively. First, we use the raw data that results from LIWC, including those reviews where no words were matched with the LIWC dictionaries. This approach has the advantage of including reviews. At the same time, this approach has disadvantages, because it results in issues of sparsity. Accordingly, second, to establish robustness, we follow the approach of Snefjella and Kuperman (2015), trimming our data, and retaining only those monthly observations where at least one review comprising the observation contained at least one word that could be matched to an LIWC dictionary. Because there are no zeros in this second sample of data, it is straightforward to then log transform the dependent variables, to further address skewness in the variable distributions. Log transforming the dependent variables also has the benefit of enabling percentage interpretations of the parameter estimates. Table 3 presents the descriptive statistics of the variables in our raw data, and Table 4 provides a correlation matrix of the main variables.

Table 1. Sample Words in LIWC’s Dictionaries

<table><tr><td>Language Characteristics</td><td>Examples</td><td>Words in Category</td></tr><tr><td>Affective Processes</td><td>Happy, cried, abandon</td><td>915</td></tr><tr><td>Positive Emotion</td><td>Love, nice, sweet</td><td>406</td></tr><tr><td>Negative Emotion</td><td>Hurt, ugly, nasty</td><td>499</td></tr><tr><td>Cognitive Processes</td><td>Cause, know, ought</td><td>730</td></tr><tr><td>Negation</td><td>No, not, never</td><td>57</td></tr></table>

Notes: Table 1 is adopted from the “LIWC2007 Output Variable Information” table, retrieved from http://liwc.net/descriptiontable1.php. More information on LIWC and the entire list of words that are used for matching to obtain the linguistic measures can be obtained from http://www.liwc.net.

<table><tr><td colspan="2">Table 2. Examples of Review Text</td></tr><tr><td>Language Characteristics</td><td>Example Reviews</td></tr><tr><td>Affective Processes</td><td>“The coffee is good a Cappuccino in this case, the place is super busy, super popular, super packed, a cute fun nice ambiance on the sidewalk in Zamalek. Cute”</td></tr><tr><td>Positive Emotion</td><td>“Love, love, love The Oinkster! Great patio, great burgers, yummy shakes and malts, relaxed atmosphere. My favorite place along a great strip of eateries.”</td></tr><tr><td>Negative Emotion</td><td>“Terrible overall. Location right by the highway, terrible noise isolation, the worst unhealthy breakfast ever, outdated rooms, disgusting shower curtain, overpriced. Best to avoid all together.”</td></tr><tr><td>Cognitive Processes</td><td>“Worn out place, trying to make it charming without really succeeding. Food was boring, sandwiches and chips - nothing to remember at all. Did not manage to make that little extra feel, neither with food, service or surroundings. The cottages looked as worn out as the restaurant, would not stay here.”</td></tr><tr><td>Negation</td><td>“No big deal, I wouldn’t highly recommend it unless you have nothing else to do. Not a lot of parking. Food, nothing special.”</td></tr></table>

Notes: Table 2 provides examples of review text that are measured as having a high value in the corresponding linguistic category. The underlined text are the words matched to the LIWC dictionary for the respective categories.

<table><tr><td colspan="6">Table 3. Descriptive Statistics</td></tr><tr><td>Variables</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td><td>Median</td></tr><tr><td>Review Volume</td><td>4.273</td><td>4.753</td><td>1</td><td>98</td><td>3</td></tr><tr><td>Rating</td><td>3.734</td><td>0.887</td><td>1</td><td>5</td><td>4</td></tr><tr><td>Words</td><td>123.782</td><td>57.929</td><td>27</td><td>281</td><td>116</td></tr><tr><td>Affective Processes</td><td>7.679</td><td>2.843</td><td>0</td><td>52.815</td><td>7.31</td></tr><tr><td>Positive Emotion</td><td>6.719</td><td>2.908</td><td>0</td><td>52.440</td><td>6.342</td></tr><tr><td>Negative Emotion</td><td>0.936</td><td>0.961</td><td>0</td><td>26.670</td><td>.772</td></tr><tr><td>Cognitive Processes</td><td>15.333</td><td>3.470</td><td>0</td><td>41.987</td><td>15.317</td></tr><tr><td>Negation</td><td>1.158</td><td>1</td><td>0</td><td>25.770</td><td>.989</td></tr></table>

<table><tr><td>Variables</td><td>Review Volume</td><td>Rating</td><td>Words</td><td>Affective Processes</td><td>Positive Emotion</td><td>Negative Emotion</td><td>Cognitive Process</td><td>Negation</td></tr><tr><td>Review Volume</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rating</td><td>0.036</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Words</td><td>0.175</td><td>-0.135</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Affective Processes</td><td>0.042</td><td>0.230</td><td>-0.307</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>Positive Emotion</td><td>0.039</td><td>0.351</td><td>-0.319</td><td>0.943</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>Negative Emotion</td><td>0.007</td><td>-0.382</td><td>0.054</td><td>0.100</td><td>-0.233</td><td>1.000</td><td></td><td></td></tr><tr><td>Cognitive Process</td><td>-0.012</td><td>-0.050</td><td>0.098</td><td>-0.070</td><td>-0.077</td><td>0.026</td><td>1.000</td><td></td></tr><tr><td>Negation</td><td>-0.045</td><td>-0.230</td><td>-0.035</td><td>-0.062</td><td>-0.127</td><td>0.202</td><td>0.224</td><td>1.000</td></tr></table>

## Econometric Identification

As noted above, our econometric identification hinges on two natural experiments related to social network integrations that occurred on Yelp.com and TripAdvisor.com, which we treat as exogenous shocks to the platform users, in the form of system changes.<sup>5</sup> We employ difference-in-differences (DID) estimation to identify the effects of social network integration on the volume and linguistic features of online reviews on each platform. The DID estimator attempts to identify causal relationships by mimicking an experimental design in observational data (Angrist and Pischke 2008). DID is a common estimation approach, frequently used to establish causal relationships in data where experimental manipulation is generally difficult to implement (Card and Krueger 1994; Di Tella and Schargrodsky 2004).

Yelp.com introduced a Facebook Connect feature on July 2, 2009, and TripAdvisor.com implemented Instant Personalization on December 21, 2010. Because Facebook Connect is an opt-in feature while Instant Personalization is an opt-out feature, the two social network integrations are ordered in terms of increasing magnitude of their effects. The observation period spans from July 2008 to July 2012. We retain a 12-month pretreatment period, in advance of Yelp’s integration event. Notably, the results we present in the following sections are not sensitive to this choice; expanding the window to 18 months or 24 months produces very similar results.

Yelp.com’s integration with Facebook constitutes the first treatment, with activity on TripAdvisor.com at the same point in time acting as the control group. TripAdvisor.com’s integration is the second treatment, with activity on Yelp.com at the same point in time acting as the control group. Although our work is not the first to employ a DID estimation in analyzing online reviews, prior research has typically employed a single-shock DID estimation (Chevalier and Mayzlin 2006; Liu et al. 2014; Mayzlin et al. 2014; Zhang and Zhu 2011). For example, Liu et al. (2014) employed a single-shock DID to identify the effect of introducing a multidimensional rating system on the characteristics of online reviews.

Finally, it is worth noting that a key assumption underlying the validity of the DID specification, more generally, is the parallel trends assumption, that is, that the trend of reviewing activity on the untreated platform can serve as a valid control for the trend of activity on the treated platform. Following Angrist and Pishke (2008), we assess this parallel trends assumption empirically in Appendix A via a dynamic difference-in-differences specification, around the Trip

Advisor social network integration event. We also report the results of separate, single-shock DID analyses in the for each of the natural experiments in Appendix B.

## Estimation Model

We estimate the two-treatment DID models reflected by Equations (1) through (4). Our estimation incorporates restaurant-level fixed effects via a within transformation, which allow us to effectively control for restaurant-level unobserved heterogeneity.

ln(Review Volume)<sub>ipt</sub> = β<sub>0</sub>Trip<sub>p</sub> + β<sub>1</sub>Trip\_Change<sub>t</sub> + β<sub>2</sub>Trip<sub>p</sub> ∗ Trip\_Change<sub>t</sub> + β<sub>3</sub>Yelp\_Change<sub>t</sub> + β<sub>4</sub>Yelp<sub>p</sub> ∗ Yelp\_Change<sub>t</sub> + β<sub>5</sub>ln(words<sub>ipt</sub>) + β<sub>6</sub> rating<sub>ipt</sub> + α<sub>i</sub> + ε<sub>ipt</sub> (1)

Review Volume<sub>ipt</sub> = β<sub>0</sub>Trip<sub>p</sub> + β<sub>1</sub>Trip\_Change<sub>t</sub> + β<sub>2</sub>Trip<sub>p</sub> ∗ Trip\_Change<sub>t</sub> + β<sub>3</sub>Yelp\_Change<sub>t</sub> + β<sub>4</sub>Yelp<sub>p</sub> ∗ Yelp\_Change<sub>t</sub> + β<sub>5</sub>ln(words<sub>ipt</sub>) + β<sub>6</sub> rating<sub>ipt</sub> + α<sub>i</sub> + ε<sub>ipt</sub> (

(2)

ln(Linguistic Characteristics) $) _ { i p t } = \beta _ { 0 } T r i p _ { p } + \beta _ { 1 } T r i p _ { . }$ \_Change<sub>t</sub> + β<sub>2</sub>Trip<sub>p</sub> ∗ Trip\_Change<sub>t</sub> + β<sub>3</sub>Yelp\_Change<sub>t</sub> + β<sub>4</sub>Yelp<sub>p</sub> ∗ Yelp\_Change<sub>t</sub> + β<sub>5</sub>ln(words<sub>ipt</sub>) + β<sub>6</sub> rating<sub>ipt</sub> + α<sub>i</sub> + ε<sub>ipt</sub> (3)

Linguistic Characteristi $z s _ { i p t } = \beta _ { 0 } T r i p _ { p } + \beta _ { 1 } T r i p \_ C h a n g e _ { t } +$ β<sub>2</sub>Trip<sub>p</sub> ∗ Trip\_Change<sub>t</sub> + β<sub>3</sub>Yelp\_Change<sub>t</sub> + β<sub>4</sub>Yelp<sub>p</sub> ∗ Yelp\_Change<sub>t</sub> + β<sub>5</sub>ln(words<sub>ipt</sub>) + β<sub>6</sub> rating<sub>ipt</sub> + α<sub>i</sub> + ε<sub>ipt</sub>

(4)

In these equations, i indexes restaurants, p denotes platforms and t indexes months. Yelp is a dummy variable which is equal to 1 if the observation pertains to reviews on Yelp.com and 0 if the observation pertains to reviews on TripAdvisor. com.<sup>6</sup> Yelp\_Change is a dummy variable which is equal to 1 for observations that take place following the introduction of Facebook Connect on Yelp.com, and 0 for observations prior. Trip\_Change is a dummy variable that is equal to 1 for observations that take place following the introduction of Instant Personalization on TripAdvisor.com, and 0 for observations prior. Because the linguistic features of a review might be affected by the reviewer’s opinion about the quality of the restaurant, we also control for the average star rating (valence) of reviews in each restaurant-month. Additionally, because a lengthier review may provide greater opportunity for a reviewer to express certain linguistic patterns, we also control for the number of words appearing in the reviews.

The key parameters of interest in these models are $\beta _ { 2 }$ and $\beta _ { 4 } ,$ our DID estimates, which capture the effects of system changes on the treatment site compared to the control site (Angrist and Pischke 2008). In particular, $\beta _ { 4 }$ estimates the effects of Yelp’s Facebook Connect on outcome variables relative to TripAdvisor without social network integration, and $\beta _ { 2 }$ captures the effects of TripAdvisor’s Instant Personalization on our outcome measures comparing to Yelp over the time period before TripAdvisor’s social network integration. For example, in Equation (1), a positive coefficient for $\beta _ { 2 }$ would suggest that TripAdvisor’s Instant Personalization has a positive effect on review volume, compared with the control site Yelp. Similarly, a positive coefficient for $\beta _ { 4 }$ would imply that Yelp’s Facebook Connect has a positive effect on Yelp’s review volume, compared with the control site TripAdvisor, which had not yet implement social network integration. As $\beta _ { 2 }$ reflects solely a conservative estimate of the treatment effect of TripAdvisor’s Instant Personalization on outcome measures, a more readily interpretable estimate of TripAdvisor’s social network integration can be achieved by separate DID analysis. Thus, we have also reported the separate, independent DID analyses for each social network integration in our supplementary appendix, where the coefficients are more readily interpretable as the true treatment effects on each platform.

## Main Findings

In this section, we report the results of our DID estimations. We test our hypotheses and then discuss the economic significance of the key estimates. Because the distributions of our dependent variables are skewed, we report estimation results using both raw and log-transformed outcome variables, as well as a Poisson regression, to assess the robustness of the findings. Further, we provide estimations based on alternative specifications in Appendix A and B, respectively, where we report (1) a dynamic specification around the TripAdvisor integration, and (2) separate single-shock DID estimates of each natural experiment. The dynamic specification provides us with the dynamic effects of social network integration on our outcome variables, over the months that follow, as well as a means of evaluating the parallel trends assumption.<sup>7</sup>

## Volume Effect

First, we tested the effect of social network integration on the volume of user-generated content (DV = ln (Review Volume) or Review Volume). Overall, our results reported in Table 5 suggest that social network integration is positively associated with the volume of user-generated content. We observe that both Yelp’s Facebook Connect feature and TripAdvisor’s Instant Personalization feature increased review volumes. This result indicates that both ease of use and reputational benefits seem to play a role in driving up review volumes and that their combined impacts dominate any possible negative effects deriving from the relative loss of anonymity.

In terms of effect sizes, based on the DID estimates of the raw review volume (Column 2 of Table 5), compared with the average monthly review volume of all restaurants in the sample (mean = 4.273), TripAdvisor’s Instant Personalization increased review volumes by 1.275 (29.84%) and Yelp’s Facebook Connect increased review volumes by 0.873 (20.43%). These estimates are largely consistent with those we obtain in our log specification (Column 1 of Table 5). We therefore find evidence in support of Hypothesis 1 that the social integration led to increases in review volumes.

Interestingly, our result is different from Frutiger et al. (2014), who found that social login leads to decreases in user registration. We surmise that the different findings may be attributable to the differences in both the study context (Frutiger and his colleagues studied a virtual gaming platform, and it is possible users in that setting would not want their social connections to know that they are playing games) and the type of social network integration (Frutiger et al. solely focused on the social login feature). Moreover, in general, having others know that one is playing games does not provide the reputational or social benefits as in the case of a review platform, where a user’s friends may observe that he or she has contributed a review to help others in their purchase decisions.

As noted earlier, social network integration also involves the introduction of a social login feature, making platform registration and login easier for users. In turn, an increase in the rate of new user entry may contribute to increases in review volumes, and possible self-selection on the part of heavy Facebook users. As such, for the moment, we interpret our results as the combined effect of new user entry and changes in user behavior. However, in the “Secondary Analysis” section, we will provide empirical evidence showing that the bulk of these results are in fact attributable to changes in user behavior, and not the entry of systematically different users.

## Mental Process Effects

Table 6 reports our findings related to affective and cognitive processes. We observe that social network integration leads to an increase in the use of language related to affective mental processes, while leading to a decline in language related to cognitive mental processes, supporting Hypotheses 2a and 2b. Table 7 presents our findings related to positive and negative emotions. Note that although social network integration leads to more affective processes in general (more emotions), when we explore different types of emotion, we observe that integration leads to more positive emotions, yet fewer negative emotions. These results support the idea that social presence increases following social network integration, because users may not want their friends to perceive them as being overly negative. The fact that we observe increases in affective processes along with simultaneous declines in cognitive processes also supports our theory, in that the prior literature has suggested repeatedly that each mental process tends to receive focus at the expense of the other.

In terms of effect sizes, the DID estimates for the raw measures (Columns 2 and 4 of Table 6; Columns 2 and 4 of Table 7) indicate that, compared to the average occurrence of affective processes (mean = 7.679) and cognitive processes (mean = 15.333), amongst all reviews in our sample, Trip Advisor’s Instant Personalization increased language usage related to overall affective processes by 0.078 (1.02%), while decreasing cognitive processes by 0.115 (0.75%). Similarly, Yelp’s Facebook Connect increased language usage associated with overall affective processes by 0.776 (9.98%), while decreasing cognitive processes by 0.386 (2.52%). Further, compared to the average occurrence of positive emotions (mean = 6.719) and negative emotions (mean = 0.936) in our sample, TripAdvisor’s Instant Personalization increased language usage reflecting positive emotions by 0.128 (1.91%), but decreased negative emotions by 0.047 (5.02%). And Yelp’s Facebook Connect increased positive emotions by 0.811 (12.07%), and decreased negative emotions by 0.038 (4.06%), respectively.

## Inhibition Effect

Finally, we consider the inhibition effect of social network integration (and thus social presence) on the use of words indicating disagreement or conflict, namely negations (i.e., no, not, never). Table 8 reports our findings. Overall, we observe that both Facebook Connect and Instant Personali zation lead to fewer negations. This finding provides support for Hypothesis 3. In terms of effect sizes, the DID estimates for the raw measures (Column 2 of Table 8) show that compared to the average linguistic score of negation in all reviews (mean = 1.158), TripAdvisor’s Instant Personalization decreased negations by 0.086 (7.43%), and Yelp’s Facebook Connect decreased negations by 0.058 (5.01%).

<table><tr><td>Variables</td><td>(1) In(Review Volume)</td><td>(2) Review Volume</td></tr><tr><td>Trip</td><td>-0.649***(0.019)</td><td>-2.543***(0.132)</td></tr><tr><td>Trip_Change</td><td>0.261***(0.006)</td><td>1.230***(0.037)</td></tr><tr><td>Trip * Trip_Change</td><td>0.376***(0.014)</td><td>1.275***(0.111)</td></tr><tr><td>Yelp_Change</td><td>0.043**(0.014)</td><td>0.209**(0.076)</td></tr><tr><td>Yelp * Yelp_Change</td><td>0.194***(0.015)</td><td>0.873***(0.084)</td></tr><tr><td>In(words)</td><td>0.184***(0.004)</td><td>0.733***(0.023)</td></tr><tr><td>Rating</td><td>0.014***(0.003)</td><td>0.075***(0.012)</td></tr><tr><td>Constant</td><td>-0.075**(0.023)</td><td>-0.429**(0.135)</td></tr><tr><td>Observations</td><td>139,239</td><td>139,239</td></tr><tr><td>Within R-squared</td><td>0.220</td><td>0.146</td></tr><tr><td>Number of Restaurants</td><td>3,968</td><td>3,968</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses; \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

<table><tr><td colspan="5">Table 6. Affective and Cognitive Processes</td></tr><tr><td>Variables</td><td>(1)In(Affective Process)</td><td>(2)Affective Process</td><td>(3)In(Cognitive Process)</td><td>(4)Cognitive Process</td></tr><tr><td>Trip</td><td>-0.083***(0.010)</td><td>-0.184***(0.053)</td><td>0.026***(0.005)</td><td>0.342***(0.064)</td></tr><tr><td>Trip_Change</td><td>0.043***(0.002)</td><td>0.307***(0.018)</td><td>0.005***(0.001)</td><td>0.077***(0.022)</td></tr><tr><td>Trip * Trip_Change</td><td>0.022***(0.006)</td><td>0.078*(0.038)</td><td>-0.007***(0.003)</td><td>-0.115*(0.046)</td></tr><tr><td>Yelp_Change</td><td>-0.036***(0.011)</td><td>-0.489***(0.055)</td><td>0.022***(0.006)</td><td>0.374***(0.067)</td></tr><tr><td>Yelp * Yelp_Change</td><td>0.075***(0.011)</td><td>0.766***(0.060)</td><td>-0.023***(0.006)</td><td>-0.386***(0.073)</td></tr><tr><td>In(words)</td><td>-0.220***(0.002)</td><td>-1.959***(0.015)</td><td>0.041***(0.001)</td><td>0.793***(0.018)</td></tr><tr><td>Rating</td><td>0.090***(0.001)</td><td>0.605***(0.009)</td><td>-0.012***(0.001)</td><td>-0.201***(0.011)</td></tr><tr><td>Constant</td><td>2.651***(0.013)</td><td>14.422***(0.086)</td><td>2.564***(0.007)</td><td>12.158***(0.104)</td></tr><tr><td>Observations</td><td>137,158</td><td>137,479</td><td>135,043</td><td>137,479</td></tr><tr><td>R-squared</td><td>0.146</td><td>0.162</td><td>0.016</td><td>0.019</td></tr><tr><td>Number of Restaurants</td><td>3,963</td><td>3,965</td><td>3,958</td><td>3,965</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses; \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

<table><tr><td>Variables</td><td>(1)In(PositiveEmotion)</td><td>(2)PositiveEmotion</td><td>(3)In(NegativeEmotion)</td><td>(4)Negative Emotion</td></tr><tr><td>Trip</td><td>-0.102***(0.011)</td><td>-0.152**(0.052)</td><td>0.087***(0.021)</td><td>-0.022(0.018)</td></tr><tr><td>Trip_Change</td><td>0.048***(0.002)</td><td>0.303***(0.018)</td><td>-0.045***(0.005)</td><td>0.006(0.006)</td></tr><tr><td>Trip * Trip_Change</td><td>0.035***(0.007)</td><td>0.128***(0.037)</td><td>-0.200***(0.014)</td><td>-0.047***(0.013)</td></tr><tr><td>Yelp_Change</td><td>-0.043***(0.012)</td><td>-0.509***(0.054)</td><td>0.061**(0.021)</td><td>0.017(0.019)</td></tr><tr><td>Yelp * Yelp_Change</td><td>0.093***(0.012)</td><td>0.811***(0.059)</td><td>-0.123***(0.022)</td><td>-0.038+(0.021)</td></tr><tr><td>In(words)</td><td>-0.255***(0.003)</td><td>-1.948***(0.015)</td><td>-0.257***(0.005)</td><td>-0.013*(0.005)</td></tr><tr><td>Rating</td><td>0.183***(0.002)</td><td>1.020***(0.009)</td><td>-0.283***(0.003)</td><td>-0.416***(0.003)</td></tr><tr><td>Constant</td><td>2.308***(0.015)</td><td>11.836***(0.084)</td><td>2.248***(0.029)</td><td>2.570***(0.029)</td></tr><tr><td>Observations</td><td>136,760</td><td>137,479</td><td>109,450</td><td>137,479</td></tr><tr><td>R-squared</td><td>0.233</td><td>0.221</td><td>0.124</td><td>0.127</td></tr><tr><td>Number of Restaurants</td><td>3,963</td><td>3,965</td><td>3,936</td><td>3,965</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses; \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.1

<table><tr><td>Variables</td><td>(1) In(Negation)</td><td>(2) Negation</td></tr><tr><td>Trip</td><td>0.394***(0.014)</td><td>0.523***(0.019)</td></tr><tr><td>Trip_Change</td><td>-0.018***(0.005)</td><td>0.028***(0.007)</td></tr><tr><td>Trip * Trip_Change</td><td>-0.113***(0.010)</td><td>-0.086***(0.014)</td></tr><tr><td>Yelp_Change</td><td>0.079***(0.015)</td><td>0.058**(0.020)</td></tr><tr><td>Yelp * Yelp_Change</td><td>-0.106***(0.016)</td><td>-0.058**(0.022)</td></tr><tr><td>Inwords</td><td>-0.235***(0.004)</td><td>-0.020***(0.006)</td></tr><tr><td>Rating</td><td>-0.192***(0.002)</td><td>-0.327***(0.003)</td></tr><tr><td>Constant</td><td>1.851***(0.023)</td><td>2.331***(0.031)</td></tr><tr><td>Observations</td><td>118,205</td><td>137,479</td></tr><tr><td>R-squared</td><td>0.135</td><td>0.094</td></tr><tr><td>Number of Restaurants</td><td>3,944</td><td>3,965</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses; \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

## Secondary Analysis

## User-Level Analysis

We elaborate on our findings, with the objective of further identifying the multiple mechanisms underlying our observed effects. In particular, we consider that the increase in review volumes, as well as the shifts in language use, might plausibly have arisen from changes in the composition of the user base, changes in user behavior, or some combination of the two. In order to assess these three possibilities, we collected additional data at the user level from TripAdvisor.com. In doing so, we identified every user who contributed at least one review in our initial sample on TripAdvisor. We then collected every review ever written by these users, including the reviews they may have written about restaurants that did not appear in our initial sample. We used these data to construct a user-level panel of reviewing activity.

Here, we examine whether the users who entered TripAdvisor after the social network integration were systematically different from the preexisting users in their language use, focusing on reviews authored after the integration had taken place. To answer this question, we conducted an additional analysis, assessing the relationship between language use and user tenure. We operationalized user tenure via an indicator of whether a user registered before or after the social network integration. Table 9 reports our findings on the relationship between language use and user tenure. The results show that the reviewers’ language use does not depend on whether the authors had registered before or after social network integration took place, providing null evidence for users’ selfselection. We report an additional analysis in Appendix C using an alternative operationalization of tenure, namely a continuous measure (number of months since the user registered on the platform), which produces consistent results.

Acknowledging that an absence of evidence on self-selection does not constitute evidence that our results are entirely attributable to changes in behavior, we report an additional analysis looking at within-user changes in behavior, before and after TripAdvisor’s social network integration, in Appendix C. However, because all of the data in question is obtained from a single platform, those results constitute pre/ post comparisons, and thus provide only correlational evidence that the observed effects related to changes in language might be caused by changes in user behavior, rather than selfselection. Exploring these mechanisms might thus be a fruitful avenue for future work to explore.

## Falsification Tests

We conduct a number of falsification tests, intended to help rule out spurious correlation. Because there is no theoretical reason to expect that a website feature like social network integration would bear a relationship with the occurrence of common words, such as articles (e.g., a, an, the), filler content (e.g., I mean, you know), or numbers (e.g., second, thousand), we would not expect to observe a significant effect on these measures. Thus, if we were to observe a significant effect, it would raise questions about the validity of our main results. Fortunately, as the results in Table 10 demonstrate, we observe no significant effects of social network integration on these outcome variables, lending further credence to our identification strategy.

## Additional Robustness Checks

We conclude our analyses with a set of robustness checks. First, due to the fact that some of the depedent variables might be codetermined, it is likely that the error terms are correlated in the separate models for each dependent variable. Therefore, we validate the robustness of our main findings by reestimating the main models (Equations 1–4) using seemingly unrelated regression (SUR). In particular, we demeaned all dependent variables to enable within estimation. We then jointly estimate the demeaned dependent variables, allowing error terms to be correlated. The results of SUR are reported in Table 11. As reported in Table 11, the SUR estimates are consistent with the main results, further indicating robustness of main results.

Second, because the dependent variables in our study are count (review volume) or quasi-count (linguistic features) in nature, we have conducted another robustness check by using fixed effects Poisson with Quasi-Maximum Likelihood estimation. The results are reported in Table 12, and the estimates are largely consistent with our main findings.

Third, although not a serious concern, because the time window of our analyses spans over two years, it is possible that there are seasonal trends for which our DID analyses did not account. Here we further conduct the analyses by further controlling for seasonal trends (with 11 dummy variables, i.e., February, March, April, ..., December). The results presented in Table 13 are largely consistent with our main findings.

Table 9. Effects of User Tenure on Review Language Characteristics

<table><tr><td>Variables</td><td>(1) Affective Process</td><td>(2) Positive Emotion</td><td>(3) Negative Emotion</td><td>(4) Cognitive Process</td><td>(5) Negation</td></tr><tr><td>Reg_after_change</td><td>-0.062 (0.048)</td><td>-0.076 (0.047)</td><td>0.011 (0.014)</td><td>-0.104 (0.068)</td><td>-0.029 (0.018)</td></tr><tr><td>In(words)</td><td>$ -3.064^{***}(0.047) $</td><td>$ -3.079^{***}(0.048) $</td><td>0.009 (0.012)</td><td>$ 0.936^{***}(0.043) $</td><td>$ 0.046^{**}(0.014) $</td></tr><tr><td>Rating</td><td>$ 0.634^{***}(0.020) $</td><td>$ 1.037^{***}(0.021) $</td><td>$ -0.406^{***}(0.011) $</td><td>$ -0.185^{***}(0.026) $</td><td>$ -0.444^{***}(0.010) $</td></tr><tr><td>Constant</td><td>$ 18.327^{***}(0.247) $</td><td>$ 15.960^{***}(0.244) $</td><td>$ 2.368^{***}(0.094) $</td><td>$ 12.150^{***}(0.292) $</td><td>$ 3.116^{***}(0.099) $</td></tr><tr><td>Observations</td><td>46,355</td><td>46,355</td><td>46,355</td><td>46,355</td><td>46,355</td></tr><tr><td>R-squared</td><td>0.259</td><td>0.290</td><td>0.088</td><td>0.022</td><td>0.064</td></tr><tr><td>Number of Restaurants</td><td>2,755</td><td>2,755</td><td>2,755</td><td>2,755</td><td>2,755</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses; \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

<table><tr><td>Variables</td><td>(1) Article</td><td>(2) Filler</td><td>(3) Numbers</td></tr><tr><td>Trip</td><td>0.354***(0.064)</td><td>-0.065***(0.010)</td><td>0.085***(0.022)</td></tr><tr><td>Trip_Change</td><td>-0.074***(0.014)</td><td>-0.013***(0.003)</td><td>-0.011*(0.005)</td></tr><tr><td>Trip * Trip_Change</td><td>0.054(0.041)</td><td>0.007(0.006)</td><td>-0.003(0.014)</td></tr><tr><td>Yelp_Change</td><td>-0.072(0.070)</td><td>-0.004(0.011)</td><td>-0.025(0.023)</td></tr><tr><td>Yelp * Yelp_Change</td><td>-0.012(0.072)</td><td>-0.013(0.011)</td><td>0.021(0.024)</td></tr><tr><td>In(words)</td><td>0.103***(0.017)</td><td>0.018***(0.003)</td><td>0.102***(0.006)</td></tr><tr><td>Rating</td><td>0.150***(0.009)</td><td>-0.036***(0.002)</td><td>-0.022***(0.003)</td></tr><tr><td>Constant</td><td>7.468***(0.093)</td><td>0.303***(0.017)</td><td>0.316***(0.031)</td></tr><tr><td>Observations</td><td>137,479</td><td>137,479</td><td>137,479</td></tr><tr><td>R-squared</td><td>0.012</td><td>0.013</td><td>0.005</td></tr><tr><td>Number of Restaurants</td><td>3,965</td><td>3,965</td><td>3,965</td></tr><tr><td>Restaurant FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses; \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

<table><tr><td>Variables</td><td>(1) Review Volume</td><td>(2) Affective Process</td><td>(3) Positive Emotion</td><td>(4) Negative Emotion</td><td>(5) Cognitive Process</td><td>(6) Negation</td></tr><tr><td>Trip</td><td>-2.282***(0.068)</td><td>-0.170***(0.052)</td><td>-0.185***(0.052)</td><td>0.025(0.018)</td><td>0.277***(0.062)</td><td>0.455***(0.019)</td></tr><tr><td>Trip_Change</td><td>1.146***(0.023)</td><td>0.299***(0.018)</td><td>0.288***(0.018)</td><td>0.013*(0.006)</td><td>0.044*(0.021)</td><td>0.022***(0.007)</td></tr><tr><td>Trip*Trip_Change</td><td>1.263***(0.050)</td><td>0.104**(0.038)</td><td>0.178***(0.038)</td><td>-0.072***(0.013)</td><td>-0.117**(0.045)</td><td>-0.083***(0.014)</td></tr><tr><td>Yelp_Change</td><td>0.108(0.073)</td><td>-0.519***(0.056)</td><td>-0.536***(0.055)</td><td>0.014(0.019)</td><td>0.363***(0.066)</td><td>0.055**(0.020)</td></tr><tr><td>Yelp*Yelp_Change</td><td>0.857***(0.079)</td><td>0.794***(0.061)</td><td>0.831***(0.060)</td><td>-0.030*(0.021)</td><td>-0.399***(0.072)</td><td>-0.055*(0.022)</td></tr><tr><td>In(words)</td><td>0.823***(0.019)</td><td>-1.785***(0.014)</td><td>-1.807***(0.014)</td><td>0.020***(0.005)</td><td>0.706***(0.017)</td><td>0.000(0.005)</td></tr><tr><td>Rating</td><td>0.071***(0.011)</td><td>0.540***(0.008)</td><td>0.881***(0.008)</td><td>-0.342***(0.003)</td><td>-0.182***(0.010)</td><td>-0.272***(0.003)</td></tr><tr><td>Constant</td><td>-4.895***(0.104)</td><td>5.724***(0.080)</td><td>4.530***(0.079)</td><td>1.200***(0.027)</td><td>-2.612***(0.095)</td><td>0.880***(0.029)</td></tr><tr><td>Observations</td><td>137,479</td><td>137,479</td><td>137,479</td><td>137,479</td><td>137,479</td><td>137,479</td></tr><tr><td>Chi-squared</td><td>21688.440</td><td>22725.120</td><td>32621.130</td><td>16163.490</td><td>2379.630</td><td>11750.890</td></tr><tr><td>R-squared</td><td>0.136</td><td>0.142</td><td>0.192</td><td>0.105</td><td>0.017</td><td>0.079</td></tr><tr><td>Number of Restaurants</td><td>3,968</td><td>3,968</td><td>3,968</td><td>3,968</td><td>3,968</td><td>3,968</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Standard errors in parentheses; \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.15

Table 12. Estimation Using Fixed Effects Poisson

<table><tr><td>Variables</td><td>(1) Review Volume</td><td>(2) Affective Process</td><td>(3) Positive Emotion</td><td>(4) Negative Emotion</td><td>(5) Cognitive Process</td><td>(6) Negation</td></tr><tr><td>Trip</td><td>-0.862***(0.026)</td><td>-0.030**(0.011)</td><td>-0.037**(0.012)</td><td>-0.092**(0.028)</td><td>0.022***(0.006)</td><td>0.382***(0.020)</td></tr><tr><td>Trip_Change</td><td>0.265***(0.007)</td><td>0.040***(0.002)</td><td>0.046***(0.002)</td><td>0.013*(0.006)</td><td>0.005***(0.001)</td><td>0.027***(0.006)</td></tr><tr><td>Trip*Trip_Change</td><td>0.607***(0.021)</td><td>0.014*(0.006)</td><td>0.025***(0.006)</td><td>-0.035*(0.018)</td><td>-0.007*(0.004)</td><td>-0.041**(0.013)</td></tr><tr><td>Yelp_Change</td><td>0.078***(0.021)</td><td>-0.062***(0.011)</td><td>-0.073***(0.013)</td><td>0.020(0.030)</td><td>0.024***(0.006)</td><td>0.049*(0.020)</td></tr><tr><td>Yelp*Yelp_Change</td><td>0.207***(0.022)</td><td>0.100***(0.012)</td><td>0.122***(0.013)</td><td>-0.036(0.032)</td><td>-0.025***(0.006)</td><td>-0.047*(0.022)</td></tr><tr><td>In(words)</td><td>0.194***(0.005)</td><td>-0.250***(0.002)</td><td>-0.282***(0.003)</td><td>-0.003(0.007)</td><td>0.052***(0.002)</td><td>-0.016*(0.006)</td></tr><tr><td>Rating</td><td>0.017***(0.004)</td><td>0.083***(0.001)</td><td>0.165***(0.002)</td><td>-0.389***(0.004)</td><td>-0.013***(0.001)</td><td>-0.247***(0.003)</td></tr><tr><td>Observations</td><td>139,189</td><td>137,427</td><td>137,427</td><td>137,396</td><td>137,427</td><td>137,410</td></tr><tr><td>Wald Chi-squared</td><td>7306.120</td><td>18765,460</td><td>28033.220</td><td>12483.610</td><td>1735.680</td><td>9850.850</td></tr><tr><td>Number of Restaurants</td><td>3,918</td><td>3,914</td><td>3,914</td><td>3,901</td><td>3,914</td><td>3,907</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Standard errors in parentheses; \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

<table><tr><td>Variables</td><td>(1) Review Volume</td><td>(2) Affective Process</td><td>(3) Positive Emotion</td><td>(4) Negative Emotion</td><td>(5) Cognitive Process</td><td>(6) Negation</td></tr><tr><td rowspan="2">Trip</td><td>-2.532***</td><td>-0.180***</td><td>-0.147**</td><td>-0.022</td><td>0.343***</td><td>0.523***</td></tr><tr><td>(0.132)</td><td>(0.053)</td><td>(0.052)</td><td>(0.018)</td><td>(0.064)</td><td>(0.019)</td></tr><tr><td rowspan="2">Trip_change</td><td>1.111***</td><td>0.301***</td><td>0.294***</td><td>0.008</td><td>0.079***</td><td>0.027***</td></tr><tr><td>(0.037)</td><td>(0.019)</td><td>(0.018)</td><td>(0.006)</td><td>(0.023)</td><td>(0.007)</td></tr><tr><td rowspan="2">Trip * Trip_Change</td><td>1.291***</td><td>0.079*</td><td>0.129***</td><td>-0.047***</td><td>-0.117*</td><td>-0.087***</td></tr><tr><td>(0.111)</td><td>(0.038)</td><td>(0.037)</td><td>(0.013)</td><td>(0.046)</td><td>(0.014)</td></tr><tr><td rowspan="2">Yelp_change</td><td>0.282***</td><td>-0.489***</td><td>-0.508***</td><td>0.016</td><td>0.375***</td><td>0.060**</td></tr><tr><td>(0.076)</td><td>(0.056)</td><td>(0.055)</td><td>(0.019)</td><td>(0.067)</td><td>(0.020)</td></tr><tr><td rowspan="2">Yelp * Yelp_Change</td><td>0.881***</td><td>0.770***</td><td>0.816***</td><td>-0.038+</td><td>-0.385***</td><td>-0.058**</td></tr><tr><td>(0.084)</td><td>(0.060)</td><td>(0.059)</td><td>(0.021)</td><td>(0.073)</td><td>(0.022)</td></tr><tr><td rowspan="2">In(words)</td><td>0.719***</td><td>-1.959***</td><td>-1.948***</td><td>-0.013*</td><td>0.794***</td><td>-0.019***</td></tr><tr><td>(0.023)</td><td>(0.015)</td><td>(0.015)</td><td>(0.005)</td><td>(0.018)</td><td>(0.006)</td></tr><tr><td rowspan="2">Rating</td><td>0.074***</td><td>0.606***</td><td>1.020***</td><td>-0.416***</td><td>-0.201***</td><td>-0.327***</td></tr><tr><td>(0.012)</td><td>(0.009)</td><td>(0.009)</td><td>(0.003)</td><td>(0.011)</td><td>(0.003)</td></tr><tr><td rowspan="2">Constant</td><td>0.061</td><td>14.458***</td><td>11.864***</td><td>2.577***</td><td>12.127***</td><td>2.338***</td></tr><tr><td>(0.132)</td><td>(0.089)</td><td>(0.087)</td><td>(0.031)</td><td>(0.107)</td><td>(0.033)</td></tr><tr><td>Observations</td><td>139,239</td><td>137,479</td><td>137,479</td><td>137,479</td><td>137,479</td><td>137,479</td></tr><tr><td>R-squared</td><td>0.151</td><td>0.163</td><td>0.221</td><td>0.127</td><td>0.020</td><td>0.094</td></tr><tr><td>Number of Restaurants</td><td>3,968</td><td>3,965</td><td>3,965</td><td>3,965</td><td>3,965</td><td>3,965</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Seasonality</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses; \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

## Discussion

## Key Findings

The aim of this paper is to examine the effects of social network integration on the volume and linguistic features of online reviews. First, we find that social network integration with Facebook increased the volume of reviews on both Yelp.com and TripAdvisor.com. Second, we find that social network integration generally increased the prevalence of emotional language in review text, but a parallel decline in cognitive language. Breaking down emotional language into positive and negative, we further observe that the increase is largely attributable to an increase in positive emotions. Third, and last, we observe a significant decline in the use of negations, indicating a decline in disagreement or negativity.

Subsequent analyses at the user level demonstrate that the observed effects of social network integration on both volume and language use are driven at least in part by changes in user behavior, rather than mere self selection, as we observe significant changes in average reviewing activity and language characteristics within users who had registered prior to the social integration event on TripAdvisor.com.

Taken together, although social network integration delivers apparent benefits, in terms of increases in review volumes and a decline in disagreement, when we consider that past work has found that emotional, positive, and conforming reviews tend to be perceived as less helpful (Chen and Lurie 2013; Hong et al. 2016; Yin et al. 2014), it seems that social network integration constitutes a double-edged sword, providing some benefits in terms of review quantity, possibly at the cost of perceived quality.

## Implications

This study contributes to several important streams of IS research. First, this study adds to recent discussion on the potential value and impact of social media (Huang et al. 2015; Kane 2014; Kane et al. 2014; Luo et al. 2013). While prior studies examined the effect of social media on firm value (Luo et al. 2013), and the influence of social media on workrelated content (versus leisure-related content) sharing behavior within the firm’s working environment (Huang et al. 2015), we unravel the effects of online review platforms’ integration with social media websites (social network integration) on user content generation.

Second, this study also extends prior research on social presence, anonymity, and online reviews in several ways. Past work on social presence has focused on limited outcomes such as trust (Ou et al. 2014), purchase intentions (Animesh et al. 2011), and consumer product choices (Rhue and Sundararajan 2013). We expand prior research by considering another outcome, users’ authorship of online reviews, considering their volumes and linguistic features. In addition, prior studies on anonymity have mainly emphasized privacy implications (Acquisti et al. 2013; Ayyagari et al. 2011) and online disinhibition effects (Reader 2012; Santana 2014; Suler 2004). We present empirical evidence that anonymity (or its absence) can affect language use as well.

Finally, previous research on the social aspects of online reviews, and user-generated content more broadly, have focused on outcomes such as contribution quantity (Chen et al. 2010; Huberman et al. 2009), evaluation negativity, and extremity (Goes et al. 2014; Wang 2010). This study considers a novel aspect: the linguistic features of review content. Our study provides the first empirical evidence suggesting increases in the social elements of an online review platform may cause existing reviewers to write more often, with more emotional language and less cognitive language, as well as to employ less negative language.

This study carries important practical implications for firms operating IT platforms that host and heavily rely upon user generated content. Given the recent trend toward social network integration by various online platforms, it is crucial that we improve our understanding of the possible unintended consequences of social integration and, in turn, social presence and anonymity (Kane 2015). Specifically, we have found that social presence increases the contribution volume of online reviews. This result suggests that social network integration is likely to be most useful for online review websites (or websites that host other forms of user-generated content) that face challenges of under-provision (Avery et al. 1999; Burtch et al. 2017). In addition, our results also show that integration leads to decreases in cognitive language, along with increases in the use of (primarily positive) emotional language. Past work has noted that emotional, positive reviews are perceived by consumers to be less helpful (Chen and Lurie 2013; Hong et al. 2016; Yin et al. 2014). Thus, our results suggest that review platforms, if implementing social network integration, should consider pairing the system change with attempts to nudge users to be less emotional and more logical when authoring their reviews, in an effort to maintain or enhance review quality.

## Limitations

Our work is subject to a number of limitations. First, our measures are relatively simplistic and the accuracy of the results depends on how comprehensive the LIWC dictionaries are. However, LIWC has recently been successfully applied by a number of scholars in Information Systems (Goes et al. 2014; Yin et al. 2014) and Marketing (Lurie et al. 2014; Sridhar and Srinivasan 2012).

Second, due to the observational nature of our data, although multiple empirical tests suggest that self-selection is not a serious issue, we are not able to completely rule out selection as a partial explanation for our results. This is primarily because users had the ability to opt-in or opt-out of the social network integration. In turn, this may suggest that our results are driven in large part by a subset of users who chose to accept the integration, or users who had Facebook accounts. Although our data does not enable us to identify which users accepted the integration features, or which users have Facebook accounts, we do not believe this should be a significant concern. Again, as noted previously, opting out of the Trip Advisor integration, while feasible, was reportedly difficult for users to perform. Additionally, our user-level analyses suggest no evidence that users who entered the platform following TripAdvisor’s integration were systematically different from preexisting users. That said, future work that disentangles behavioral change from self-selection in the setting of social network integration is warranted. Similarly, because we examine only two platforms and treatment events, we are not able to estimate a relative time model that simultaneously controls for platform-specific time trends, while separately estimating the dynamics of treatment effects.

Third, as noted in our hypothesis development, even though we have argued that TripAdvisor’s opt-out implementation might have been expected to have stronger effects than Yelp’s opt-in implementation, we are unable to draw robust conclusions from the relative magnitude of the two treatment effects. Again, this is because the two treatments are likely to have been heterogeneous in a variety of respects, beyond the opt-in versus opt-out aspect. Future work might therefore look to disentangle moderating factors that can exacerbate or attenuate the strength of effects of these treatments have on various outcome measures.

Fourth, although we have empirically evaluated the parallel assumption via a dynamic DID specification, underlying differences may still exist between the two platforms we have studied that we have not considered here. As such, in keeping with other prior studies that have employed a similar research design (Mayzlin et al. 2014), our results should be interpreted with some caution. Finally, to the question of generalizability, given that we have studied integration events involving a particular type of social network, namely Facebook, it is conceivable that our findings would not generalize outside of the Facebook population. However, even if this were the case, Facebook now boasts more than 1.5 billion users. Accordingly, such users are unlikely to be representative of the broader user population (that is, users who lack a Facebook account would quite possibly constitute a minority). Taken together, the above deliberation suggests that our results are likely to be both generalizable and not driven predominantly by self-selection.

## Future Research Directions

There is significant potential for future work in this space. First, it would be useful to explore other text mining techniques, such as topic modeling, to undertake a more nuanced textual analysis in an automated fashion. Second, we have merely focused on a few aspects that social network integration may impact. Future research can extend our study by exploring other outcomes of social network integration. For example, researchers can examine the impact of integration on psychological distance. Social network integration might change the perceived social distance among users on the online platforms, which in turn may affect word usage (Holtgraves 2003). Additionally, our results suggest that social network integration functions as a double-edged sword that increases review quantity yet decreases review quality. Yet, in this paper, we were not able to provide direct evidence of review quality or the net benefit of social network integration for users. Future work might thus explore the net impact on social welfare from social network integration. Third, this study assumes that online friends in social networks are likely to overlap with offline friends. Future work could extend our study by collecting data on small markets where people actually know each other offline. Fourth, as we articulated earlier, there are a variety of moderating factors which might amplify or attenuate the magnitude of the observed treatment effects. One example of particular interest that we have highlighted is the opt-in versus opt-out nature of the implementation. It might be fruitful for scholars to empirically evaluate the differences between opt-in and opt-out implementations in this context going forward. Finally, future studies could further improve causal inference of the effect of social presence on user content generation via experimental manipulations of reviewer social presence or anonymity.

## Acknowledgments

The authors thank the senior editor, Sulin Ba, and the review team for a most constructive and developmental review process. The authors also thank Paul Pavlou, Susan Mudambi, and participants at the NET Institute Conference and International Conference on Information Systems for valuable feedback. The authors acknowledge financial support from the NET Institute (#15-04) and the Young Scholar’s Forum of Fox School of Business, Temple University.

## References

Acquisti, A., and Gross, R. 2006. “Imagined Communities: Awareness, Information Sharing, and Privacy on the Facebook,” in Lecture Notes in Computer Science (Volume 4258), G. Danezis and P. Golle (eds.), Berlin: Springer, pp. 36-58.

Acquisti, A., John, L., and Loewenstein, G. 2013. “What Is Privacy Worth?,” The Journal of Legal Studies (42:2), pp. 249-274.

Andreoni, J., and Bernheim, B. D. 2009. “Social Image and the 50– 50 Norm: A Theoretical and Experimental Analysis of Audience Effects,” Econometrica (77:5), pp. 1607-1636.

Angrist, J. D., and Pischke, J. S. 2008. Mostly Harmless Econometrics: An Empiricist’s Companion, Princeton, NJ: Princeton University Press.

Animesh, A., Pinsonneault, A., Yang, S. B., and Oh, W. 2011. “An Odyssey into Virtual Worlds: Exploring the Impacts of Technological and Spatial Environments on Intention to Purchase Virtual Products,” MIS Quarterly (35:3), pp. 789-810.

Aral, S. 2014. “The Problem with Online Ratings,” Sloan Management Review, Winter (retrieved from: http://sloanreview.mit.edu/ article/the-problem-with-online-ratings-2/).

Avery, C., Resnick, P., and Zeckhauser, R. 1999. “The Market for Evaluations,” The American Economic Review (89:3), pp. 564-584.

Ayyagari, R., Grover, V., and Purvis, R. 2011. “Technostress: Technological Antecedents and Implications,” MIS Quarterly (35:4), pp. 831-858.

Ba, S., 2001. “Establishing Online Trust Through a Community Responsibility System,” Decision Support Systems (31:3), pp. 323-336.

Ba, S., and Pavlou, P. A. 2002. “Evidence of the Effect of Trust Building Technology in Electronic Markets: Price Premiums and Buyer Behavior,” MIS Quarterly (26:3), pp. 243-268.

Baumeister, R. F., Bratslavsky, E., Finkenauer C., and Vohs K. D. 2001, “Bad Is Stronger Than Good,” Review of General Psychology (5:4), pp. 323-70.

Blanchard, O. 2011. Social Media ROI: Managing and Measuring Social Media Efforts in Your Organization, Upper Saddle River, NJ: Pearson Education.

Briggs, K. C. 1977. Myers-Briggs Type Indicator, Palo Alto, CA: Consulting Psychologist Press, Inc.

Buck, R., Losow, J. I., Murphy, M. M., and Costanzo, P. 1992. “Social Facilitation and Inhibition of Emotional Expression and Communication,” Journal of Personality and Social Psychology (63:6), pp. 962-968.

Burtch, G., Ghose, A., and Wattal, S. 2015. “The Hidden Cost of Accommodating Crowdfunder Privacy Preferences: A Randomized Field Experiment,” Management Science (61:5), pp. 949-962.

Burtch, G., Hong, Y., Bapna, R., and Griskevicius, V. 2017. “Stimulating Online Reviews by Combining Financial Incentives and Social Norms,” Management Science, forthcoming.

Campbell, M. A. 2005. “Cyber Bullying: An Old Problem in a New Guise?,” Australian Journal of Guidance and Counselling (15:1), pp. 68-76.

Card, D., and Krueger, A. B. 1994. “Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania,” American Economic Review (84:4), pp. 772-793.

Chapman, G. B., and Johnson, E. J. 1999. “Anchoring, Activation, and the Construction of Values,” Organizational Behavior and Human Decision Processes (79:2), pp. 115-153.

Chen, Y., Harper, F. M., Konstan, J., and Li, S. X. 2010. “Social Comparisons and Contributions to Online Communities: A Field Experiment on MovieLens,” American Economic Review (100:4), pp. 1358-1398.

Chen, Z., and Lurie, N. H. 2013. “Temporal Contiguity and Negativity Bias in the Impact of Online Word of Mouth,” Journal of Marketing Research (50:4), pp. 463-476.

Chevalier, J. A., and Mayzlin, D. 2006. “The Effect of Word of Mouth on Sales: Online Book Reviews,” Journal of Marketing Research (43:3), pp. 345-354.

Cho, D., Kim, S., and Acquisti, A. 2012. “Empirical Analysis of Online anonymity and User Behaviors: the Impact of Real Name Policy,” in Proceedings of the 45<sup>th</sup> Hawaii International Conference on System Science, Los Alamitos, CA: IEEE Press.

Cobb, S. C. 2009. “Social Presence and Online Learning: A Current View from A Research Perspective,” Journal of Interactive Online Learning (8:3), pp. 241-254.

Connolly, T., Jessup, L. M., and Valacich, J. S. 1990. “Effects of Anonymity and Evaluative Tone on Idea Generation in Computer-Mediated Groups,” Management Science (36:6), pp. 689-703.

Cui, G., Lockee, B., and Meng, C. 2012. “Building Modern Online Social Presence: A Review of Social Presence Theory and its Instructional Design Implications for Future Trends,” Education and Information Technologies (18:4), pp. 661-685.

Das, S., and Kramer, A. 2013. “Self-Censorship on Facebook,” in Proceedings of the 7<sup>th</sup> International AAAI Conference on Weblogs and Social Media, Palo Alto, CA: AIII Press, pp. 120-127.

Daughety, A. F., and Reinganum, J. F. 2010. “Public Goods, Social Pressure, and the Choice Between Privacy and Publicity,” American Economic Journal: Microeconomics (2:2), pp. 191-221.

Davis, J. P., Farnham, S., and Jensen, C. 2002. “Decreasing Online ‘Bad’ Behavior,” in CHI’02 Extended Abstracts on Human Factors in Computing Systems, New York: ACM, pp. 718-719.

Dellarocas, C. 2003. “The Digitization of Word of Mouth: Promise and Challenges of Online Feedback Mechanisms,” Management Science (49:10), pp. 1407-1424.

Dellarocas, C., Zhang, X. M., and Awad, N. F. 2007. “Exploring the Value of Online Product Reviews in Forecasting Sales: The Case of Motion Pictures,” Journal of Interactive Marketing (21:4), pp. 23-45.

De Martino, B., Kumaran, D., Seymour, B., and Dolan, R. J. 2006. “Frames, Biases, and Rational Decision-making in the Human Brain,” Science (313:5787), pp. 684-687.

Derks, D., Fischer, A. H., and Bos, A. E. 2008. “The Role of Emotion in Computer-mediated Communication: A Review,” Computers in Human Behavior (24:3), pp. 766-785.

Dinner, I., Johnson, E. J., Goldstein, D. G., and Liu, K. 2011. “Partitioning Default Effects: Why People Choose Not to Choose,” Journal of Experimental Psychology: Applied, (17:4), pp. 332-341.

Di Tella, R., and Schargrodsky, E. 2004. “Do Police Reduce Crime? Estimates Using the Allocation of Police Forces After a Terrorist Attack,” The American Economic Review (94:1), pp. 115-133.

Drebes, L. 2011. “Social Login Offers New ROI from Social Media,” Harvard Business Review (retrieved from http://blogs. hbr.org/cs/2011/10/social\_login\_offers\_new\_roi\_fr.html).

Duan, W., Gu, B., and Whinston, A. B. 2008. “Do Online Reviews Matter? An Empirical Investigation of Panel Data,” Decision Support Systems (45:4), pp. 1007-1016.

Epstein, S. 1993. “Emotion and Self-Theory,” in Handbook of Emotions, M. Lewis and J. M. Haviland (eds.), New York: Guilford, pp. 313-326.

Finucane, M. L., Peters, E., and Slovic, P. 2003. “Judgment and Decision Making: The Dance of Affect and Reason,” in Emerging Perspectives on Judgment and Decision Research, S. Schneider and J. Shanteau (eds.), New York: Cambridge University Press, pp. 327-357.

Fricke, H. 2015. “Identification Based on Difference-in-Differences Approaches with Multiple Treatments,” University of St. Gallen, School of Economics and Political Science Economics Working Paper Series No. 1510.

Frolich, M. 2004. “Programme Evaluation with Multiple Treatments,” Journal of Economic Surveys (18:2), pp. 181-224.

Froomkin, M. A. 1999. “Legal Issues in Anonymity and Pseudonymity,” Information Society (15:2), pp. 113-127.

Frutiger, M., Overby, E., and Wu, D. 2014. “Is Social Network Platform Integration Valuable for an Online Service? A Randomized Field Experiment and Archival Data Analysis,” in Proceedings of the 35<sup>th</sup> International Conference on Information Systems, Auckland.

Gill, A. J., French, R. M., Gergle, D., and Oberlander, J. 2008. “The Language of Emotion in Short Blog Texts,” in Proceedings of the 2008 ACM Conference on Computer Supported Cooperative Work, New York: ACM, pp. 299-302.

Gilovich, T., Griffin, D., and Kahneman, D. 2002. Heuristics and Biases: The Psychology of Intuitive Judgment, New York: Cambridge University Press.

Gneezy, A., Imas, A., Brown, A., Nelson, L. D., and Norton, M. I. 2012. “Paying to Be Nice: Consistency and Costly Prosocial Behavior,” Management Science (58:1), pp. 179-187.

Godes, D., and Silva J. C. 2012. “Sequential and Temporal Dynamics of Online Opinion,” Marketing Science (31:3), pp. 448-473.

Goes, P. B., Lin, M., and Au Yeung, C.-M. 2014. “Popularity Effect in User-Generated Content: Evidence from Online Product Reviews,” Information Systems Research (25:2), pp. 222-238.

Gunawardena, C. N. 1995. “Social Presence Theory and Implications for Interaction Collaborative Learning in Computer Conferences,” International Journal of Educational Telecommunications (1:2/3), pp. 147-166.

Gunawardena, C. N., and Zittle, F. J. 1997. “Social Presence as a Predictor of Satisfaction within a Computer Mediated Conferencing Environment,” American Journal of Distance Education (11:3), pp. 8-26.

Harber, K. D., and Cohen, D. J. 2005. “The Emotional Broadcaster Theory of Social Sharing,” Journal of Language and Social Psychology (24:4), pp. 382-400.

Hardaker, C. 2010. “Trolling in Asynchronous Computer-Mediated Communication: From User Discussions to Theoretical Concepts,” Journal of Politeness Research (6:2), pp. 215-242.

Hoffman, D., Novak, T., and Peralta, M. A. 1999. “Information Privacy in the Market-Space: Implications for the Commercial Use of Anonymity on the Web,” Information Society (15:4), pp. 129-139.

Holliday, M. 2009. “Yelp Integrates Facebook Connect, Online Reviews Becoming Increasingly Social,” Adweek, July 3 (retrieved from http://www.adweek.com/socialtimes/Yelpintegrates-facebook-connect-online-reviews-becomingincreasingly-social/224427).

Holtgraves, T. M. 2013. Language as Social Action: Social Psychology and Language Use, Abingdon, UK: Psychology Press.

Hong, Y., Huang, N., Burtch, G., and Li, C. 2016, “Culture, Conformity and Emotional Suppression in Online Reviews,” Journal of the Association for Information Systems (17:11), pp. 737-758.

Horn, L. R. (ed.). 2010. The Expression of Negation, Berlin: Walter de Gruyter.

Huang, N., Burtch, G., Hong, Y., and Polman, E. 2016, “Effects of Multiple Psychological Distances on Construal Level: A Field Study of Online Reviews,” Journal of Consumer Psychology (26:4), pp. 474-482.

Huang, Y., Singh, P. V., and Ghose, A. 2015. “A Structural Model of Employee Behavioral Dynamics in Enterprise Social Media,” Management Science (61:12), pp. 2825-2844.

Huberman, B. A., Adar, E., and Fine, L. 2005. “Valuating Privacy,” IEEE Security and Privacy (3:5), pp. 22-25.

Huberman, B. A., Romero, D. M., and Wu, F. 2009. “Crowdsourcing, Attention and Productivity,” Journal of Information Science (35:6), pp. 758-765.

Jackson, L. A., Sullivan, L. A., Harnish, R., and Hodge, C. N. 1996. “Achieving Positive Social Identity: Social Mobility, Social Creativity, and Permeability of Group Boundaries,” Journal of Personality and Social Psychology (70:2), pp. 241-254.

Jessup, L. M., Connolly, T., and Galegher, J. 1990. “The Effects of Anonymity on GDSS Group Process with an Idea-Generating Task,” MIS Quarterly (14:3), pp. 313-321.

Jiang, Z., Heng, C. S., and Choi, B. C. 2013. “Research Note— Privacy Concerns and Privacy-Protective Behavior in Synchronous Online Social Interactions,” Information Systems Research (24:3), pp. 579-595.

John, L. K., Acquisti, A., and Loewenstein, G. 2009. “The Best of Strangers: Context Dependent Willingness to Divulge Personal Information” (available at SSRN: http://ssrn.com/abstract= 1430482).

Johnson, E. J., Bellman, S., and Lohse, G. L. 2002. “Defaults, Framing, and Privacy: Why Opting In…Opting Out,” Marketing Letters (13:1), pp. 5-15.

Johnson, E. J., and Goldstein, D. 2003. “Do Defaults Save Lives?,” Science (302:5649), pp. 1338-1339.

Joinson, A. 1999. “Social Desirability, Anonymity, and Internet-Based Questionnaires,” Behavior Research Methods, Instruments, and Computers (31:3), pp. 433-438.

Jones, D., and Linardi, S. 2014. “Wallflowers: Experimental Evidence of an Aversion to Standing Out,” Management Science (60:7), pp. 1757-1771.

Kahneman, D. 2011. Thinking, Fast and Slow, London: Macmillan.

Kane, G. C. 2014. “Enterprise Social Media: Current Capabilities and Future Possibilities,” MIS Quaterly Executive (14:1), pp. 1- 16.

Kane G. C. 2015. “Digital Transparency and Performance,” MIT S l o a n M a n a g e m e n t R e v i e w ( r e t r i e v e d f r o m : http://sloanreview.mit.edu/article/digital-transparency-andpermanence/?utm\_source=linkedin&utm\_medium=social&utm \_campaign=sm-direct).

Kane, G. C., Alavi, M., Labianca, G., and Borgatti, S. 2014. “What’s Different about Social Media Networks? A Framework and Research Agenda,” MIS Quarterly (38:1), pp. 275-304.

Kang, R., Brown, S., and Kiesler, S. 2013. “Why Do People Seek Anonymity on the Internet? Informing Policy and Design,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, New York: ACM, pp. 2657-2666.

Kaplan, A. M., and Haenlein, M. 2010. “Users of the World, Unite! The Challenges and Opportunities of Social Media,” Business Horizons (53:1), pp. 59-68.

Kehrwald, B. 2008. “Understanding Social Presence in Text-Based Online Learning Environments,” Distance Education, (29:1), pp. 89-106.

Kincaid, J. 2010. “Facebook Launches Instant Personalization on TripAdvisor,” TechCrunch, December 21 (retrieved from http://techcrunch.com/2010/12/21/facebook-launches-instantpersonalization-on-TripAdvisor/).

Kontaxis, G., Polychronakis, M., and Markatos, E.P. 2012. “Minimizing Information Disclosure to Third Parties in Social Login Platforms,” International Journal of Information Security (11:5), pp. 321-332.

Kraut, R. E. 1982. “Social Presence, Facial Feedback, and Emotion,” Journal of Personality and Social Psychology (42:5), pp. 853-863.

Kressel, L. M., Chapman, G. B., and Leventhal, E. 2007. “The Influence of Default Options on the Expression of End-of-Life Treatment Preferences in Advance Directives,” Journal of General Internal Medicine (22:7), pp. 1007-1010.

Kwark, Y., Chen, J., and Raghunathan, S. 2014. “Online Product Reviews: Implications for Retailers and Competing Manufacturers,” Information Systems Research (25:1), pp. 93-110.

Lampel, J., and Bhalla, A. 2007. “The Role of Status Seeking in Online Communities: Giving the Gift of Experience,” Journal of Computer Mediated Communication (12:2), pp. 434-455.

Lasersohn, P. 2005. “Context Dependence, Disagreement, and Predicates of Personal Taste,” Linguistics and Philosophy, (28:6), pp. 643-686.

Lee, Y. J., Hosanagar, K., and Tan, Y. 2015. “Do I Follow My Friends or the Crowd? Information Cascades in Online Movie Ratings,” Management Science, (61:9), pp. 2241-2258.

Leshed, G. 2009. “Silencing the Clatter: Removing Anonymity from a Corporate Online Community,” in Online Deliberation: Design, Research, and Practice, T. Davies and S. P. Gangadharan (eds.), Chicago: University of Chicago Press, pp. 243-251.

Liu, Y., Chen, P.-Y., and Hong, Y. 2014. “Value of Multi-Dimensional Rating Systems: An Information Transfer View,” in Proceedings of the 35<sup>th</sup> International Conference on Information Systems, Auckland, New Zealand.

Lowenthal, P. R. 2009. “The Evolution and Influence of Social Presence Theory on Online Learning,” in Online Education and Adult Learning: New Frontiers for Teaching Practices, T. T. Kidd (ed.), Hershey, PA: IGI Global, pp. 124-139.

Lu, X., Ba, S., Huang, L., and Feng, Y., 2013. “Promotional Marketing or Word-of-Mouth? Evidence from Online Restaurant Reviews,” Information Systems Research (24:3), pp. 596-612.

Luca, M., and Zervas, G. 2016. “Fake It Till You Make It: Reputation, Competition, and Yelp Review Fraud,” Management Science (62:12), pp. 3412-3427

Luo, X., Zhang, J., and Duan, W. 2013. “Social Media and Firm Equity Value,” Information Systems Research (24:1), pp. 146-163.

Lurie, N., Ransbotham, S., and Liu, H. 2013. “The Content and Impact of Mobile Versus Desktop Reviews,” in NA – Advances in Consumer Research (Volume 41), S. Botti and A. Labroo (eds.), Duluth, MN: Association for Consumer Research.

Mayzlin, D., Dover, Y., and Chevalier, J. 2014. “Promotional Reviews: An Empirical Investigation of Online Review Manipulation,” American Economic Review (104:8), pp. 2421-2455.

Miranda, S. M., and Saunders, C. S. 2003. “The Social Construction of Meaning: An Alternative Perspective on Information Sharing,” Information Systems Research (14:1), pp. 87-106.

Millar, M. G., and Tesser, A. 1986. “Effects of Affective and Cognitive Focus on the Attitude–Behavior Relation,” Journal of Personality and Social Psychology (51:2), pp. 270-276.

Moor, P. J., Heuvelman, A., and Verleur, R. 2010. “Flaming on YouTube,” Computers in Human Behavior (26:6), pp. 1536-1546.

Muchnik, L., Aral, S., and Taylor, S. J. 2013. “Social Influence Bias: A Randomized Experiment,” Science (341:6146), pp. 647-651.

Mudambi, S. M., and Schuff, D. 2010. “What Makes a Helpful Review? A Study of Customer Reviews on Amazon.com,” MIS Quarterly (34:1), pp. 185-200.

Oldmeadow, J. A., and Fiske, S. T. 2010. “Social Status and the Pursuit of Positive Social Identity: Systematic Domains of Intergroup Differentiation and Discrimination for High-and Low-Status Groups,” Group Processes and Intergroup Relations (13:4), pp. 425-444.

O’Neill, H. 2002. “Cognitive – Cognitive What?,” The British Journal of Occupational Therapy (65:6), pp. 288-290.

O’Neill, N. 2009. “Yelp Launches Facebook Connect,” Adweek, July 2 (retrieved from http://www.adweek.com/socialtimes/Yelplaunches-facebook-connect/309713).

Ou, C. X., Pavlou, P. A., and Davison, R. 2014. “Swift Guanxi in Online Marketplaces: The Role of Computer-Mediated Communication Technologies,” MIS Quarterly (38:1), pp. 209-230.

Pavlou, P. A. 2011. “State of the Information Privacy Literature: Where Are We Now and Where Should We Go?,” MIS Quarterly (35:4), pp. 977-988.

Pennebaker, J. W., and Francis, M. E. 1996. “Cognitive, Emotional, and Language Processes in Disclosure,” Cognition and Emotion (10:6), pp. 601-626.

Pennebaker, J. W., Chung, C. K., Ireland, M., Gonzales, A., and Booth, R. J. 2007. “The Development and Psychometric Properties of LIWC2007,” Austin, TX: LIWC.net.

Pervin, L. A., and John, O. P. 1999. Handbook of Personality: Theory and Research, Amsterdam: Elsevier.

Pfitzmann, A., and Köhntopp, M. 2001. “Anonymity, Unobservability, and Pseudonymity – A Proposal for Terminology,” in Designing Privacy Enhancing Technologies, H. Federrath (ed.), Berlin: Springer, pp. 1-9.

Phillips, W. 2011. “LOLing at Tragedy: Facebook Trolls, Memorial Pages and Resistance to Grief Online,” First Monday (16:12).

Rapp, A., Beitelspacher, L. S., Grewal, D., and Hughes, D. E. 2013. “Understanding Social Media Effects Across Seller, Retailer, and Consumer Interactions,” Journal of the Academy of Marketing Science (41:5), pp. 547-566.

Reader, B. 2012. “Free Press vs. Free Speech? The Rhetoric of ‘Civility’ in Regard to Anonymous Online Comments,” Journalism and Mass Communication Quarterly (89:3), pp. 495-513.

Rhue, L., and Sundararajan, A. 2013. “How Digital Social Visibility Shapes Consumer Choice” (available at SSRN: http://ssrn.com/abstract=2347793).

Richardson, J. C., and Swan, K. 2003. “Examining Social Presence in Online Courses in Relation to Students’ Perceived Learning and Satisfaction,” Journal of Asynchronous Learning Networks (7:1), pp. 68-88.

Rozin, P., and Royzman, E. B. 2001. “Negativity Bias, Negativity Dominance, and Contagion,” Personality and Social Psychology Review (5:4), pp. 296-320.

Samuelson, W., and Zechhauser, R. 1988. “Status Quo Bias in Decision Making,” Journal of Risk and Uncertainty (1:1), pp. 7-59.

Sanfey, A. G., Rilling, J. K., Aronson, J. A., Nystrom, L. E., and Cohen, J. D. 2003. “The Neural Basis of Economic Decision-Making in the Ultimatum Game,” Science (300:5626), pp. 1755-1758.

Santana, A. D. 2014. “Virtuous or Vitriolic: The Effect of Anonymity on Civility in Online Newspaper Reader Comment Boards,” Journalism Practice (8:1), pp. 18-33.

Scott, S. V., and Orlikowski W. J. 2014. “Entanglements in Practice: Performing Anonymity Through Social Media,” MIS Quarterly (38:3), pp. 873-893.

Shiv, B., and Fedorikhin, A. 1999. “Heart and Mind in Conflict: The Interplay of Affect and Cognition in Consumer Decision Making,” Journal of Consumer Research, (26:3), pp. 278-292.

Short, J. A. 1974. “Effects of Medium of Communication on Experimental Negotiation,” Human Relations (27:3), pp. 325-334.

Short, J. A., Williams, E., and Christie, B. 1976. The Social Psychology of Telecommunications, New York: John Wiley and Sons.

Sia, C. L., Tan, B. C., and Wei, K. K. 2002. “Group Polarization and Computer-Mediated Communication: Effects of Communication Cues, Social Presence, and Anonymity,” Information Systems Research (13:1), pp. 70-90.

Sleeper, M., Balebako, R., Das, S., McConahy, A. L., Wiese, J., and Cranor, L. F. 2013. “The Post That Wasn’t: Exploring Self-Censorship on Facebook,” in Proceedings of the 2013 Conference on Computer Supported Cooperative Work, New York: ACM, pp. 793-802.

Snefjella, B., and Kuperman, V. 2015. “Concreteness and Psychological Distance in Natural Language Use,” Psychological Science (26:2), pp. 159-169.

Sridhar, S., and Srinivasan, R. 2012. “Social Influence Effects in Online Product Ratings,” Journal of Marketing (76:5), pp. 70-88.

Suler, J. 2004. “The Online Disinhibition Effect,” Cyberpsychology and Behavior (7:3), pp. 321-326.

Talmi, D., and Frith, C. 2007. “Neurobiology: Feeling Right About Doing Right,” Nature (446:7138), pp. 865-866.

Thaler, R. H., and Sunstein, C. R. 2008. Nudge: Improving Decisions About Health, Wealth, and Happiness, New Haven, CT: Yale University Press.

TripAdvisor. 2010. “TripAdvisor Launches Facebook® Integration, Making Travel Planning More Social for Millions” (retrieved from http://www.TripAdvisor.com/PressCenter-i4470- c1-Press\_Releases.html).

Wagner, H. L., and Smith, J. 1991. “Facial Expression in the Presence of Friends and Strangers,” Journal of Nonverbal Behavior (15:4), pp. 201-214.

Wang, Z. 2010. “Anonymity, Social Image, and the Competition for Volunteers: A Case Study of the Online Market for Reviews,” The BE Journal of Economic Analysis and Policy (10:1), pp. 1-34.

Wang, A., Zhang, M., and Hann, I.-H. 2017. “Socially Nudged: A Quasi-Experimental Study of Friends’ Social Influence in Online Product Ratings,” Information Systems Research, Forthcoming.

Wright-Porto, H. 2011. “Social Network Integration,” Creative Blogging, pp. 207-237.

Yin, D., Bond, S., and Zhang, H. 2014. “Anxious or Angry? Effects of Discrete Emotions on the Perceived Helpfulness of Online Reviews,” MIS Quarterly (38:2), pp. 539-560.

Zhang, M., and Zhu, F. 2011. “Group Size and Incentives to Contribute: A Natural Experiment at Chinese Wikipedia,” The American Economic Review (101:4), pp. 1601-1615.

Zhu, F., and Zhang, X. 2010. “Impact of Online Consumer Reviews on Sales: The Moderating Role of Product and Consumer Characteristics,” Journal of Marketing (74:2), pp. 133-148.

## About the Authors

Ni (Nina) Huang is an assistant professor in the Department of Information Systems, W. P. Carey School of Business at Arizona State University. She obtained her Ph.D. in Business Administration at the Fox School of Business, Temple University. Her research focuses on the behavioral and economic aspects of online and mobile platforms. Nina’s research has been published in premier journals, including MIS Quarterly, Journal of the Association for Information Systems, and Journal of Consumer Psychology. Her work has also been presented at premier conferences, such as the International Conference on Information Systems, Conference on Information Systems and Technology, Statistical Challenges in eCommerce Research, NET Institute Conference, and CODE@MIT. Her research has received funding from the NET Institute, the Fox School Young Scholar’s Forum, and Amazon Web Services (AWS). Nina is currently a external researcher and closely works with a number of companies, including Yamibuy, Meishi, and XuetangX.

Yili (Kevin) Hong is an assistant professor and codirector of the Digital Society Initiative in the Department of Information Systems at the W. P. Carey School of Business of Arizona State University. He obtained his Ph.D. in Business Administration at the Fox School of Business, Temple University. Kevin’s research focuses on areas of the sharing economy, online platforms and user-generated content. His research has been published in premier journals such as Management Science, Information Systems Research, MIS Quarterly, Journal of the Association for Information Systems, and Journal of Consumer Psychology. He is the winner of the ACM SIGMIS Best Dissertation Award and runner-up of the INFORMS ISS Nunamaker-Chen Dissertation Award. His papers have won best paper awards at the International Conference on Information Systems, Hawaii International Conference on System Sciences, and the America’s Conference on Information Systems. Kevin’s research has received funding from a number of agencies, including the Robert Wood Johnson Foundation, NET Institute, and the Department of Education. He is an external research scientist for a number of high profile tech companies, including Freelancer, Fits.me, Yamibuy, and Meishi.

Gordon Burtch is an assistant professor of Information and Decision Sciences at the University of Minnesota’s Carlson School of Management, and a Consulting Researcher with Microsoft Research, NYC. He holds a Ph.D. from Temple University’s Fox School of Business. His research has been published in various top journals, including MIS Quarterly, Information Systems Research, Management Science, and the Journal of Consumer Psychology. Gord’s work has been recognized with financial support from a number of granting agencies, including the Kauffman Foundation, 3M Foundation and NET Institute, and has been cited by a variety of major outlets in the popular press, including The New York Times, NPR, Time Magazine, Forbes, Vice, Wired, The Los Angeles Times, Pacific Standard, and PC Magazine. Gord was the recipient of the Information Systems Society’s Information Systems Research best paper award in 2014, the Distinguished Service Award from Management Science in 2016 and the Best Reviewer award from Information Systems Research in 2016. He served as cochair for the 2016 Workshop on Information Systems and Economics (WISE).

# SOCIAL NETWORK INTEGRATION AND USER CONTENT GENERATION: EVIDENCE FROM NATURAL EXPERIMENTS

Ni Huang W. P. Carey School of Business, Arizona State University, 300 E. Lemon Street, Tempe, AZ 85287 U.S.A. {ni.huang@asu.edu}

Yili Hong W. P. Carey School of Business, Arizona State University, 300 E. Lemon Street, Tempe, AZ 85287 U.S.A. {hong@asu.edu}

Gordon Burtch Carlson School of Management, University of Minnesota, 321 $1 9 ^ { \mathfrak { t h } }$ Avenue South, Minneapolis, MN 55455 U.S.A. {gburtch@umn.edu}

## Appendix A

## Assessing Pretreatment Trends Using a Dynamic Difference-in-Differences Model

A key identifying assumption of the DID specification is the existence of parallel trends between the treatment and control group, leading up to the treatment. Under a dynamic difference-in-differences specification, it is possible to test the assumption of parallel trends explicitly. In particular, by interacting the treatment indicator with time dummies, we can explore relative changes in the trends of our dependent variables across the treatment and control groups around the time of treatment. Our aim in doing so is to assess whether the treatment effects recovered in the traditional DID analyses were plausibly due to a preexisting dynamic, which began before the treatment took place (i.e., a failure of the parallel trends assumption). Specifically, the DID’s assumption of parallel trends would be violated if we were to observe a pretreatment trend in the same direction as the post-treatment effect; such an observation would imply that the effect began to manifest prior to the treatment.

As we discuss in the main text of the paper, TripAdvisor’s Instant Personalization is an opt-out feature and the effect is presumably more salient than Yelp’s Facebook Connect (an opt-in feature), therefore we use the time window around TripAdvisor’s exogenous shock to examine the relative difference in differences in our dependent variables, between TripAdvisor and Yelp, across multiple periods of time, both before and after the treatment event. We implement the approach suggested by Angrist and Pishke (2009), interacting our platform dummy, Trip, with our time (monthly) dummies. Notably, this sort of approach has seen extensive use in recent IS work (Burtch et al. 2016; Chan and Ghose 2014; Greenwood and Wattal 2017).

We estimate a platform fixed effect, Trip, a set of absolute time (monthly) dummies τ<sub>t</sub> (e.g., January 2011, February 2011), their interactions, and a vector of restaurant fixed effects. Our econometric specification is thus as detailed in Equation A1. We plot the coefficients associated with each month\*Trip interaction, omitting the month of integration (December 2010) from the estimation (i.e., the coefficients reflect difference-in-differences estimates relative to the month of treatment).

$$
D V _ {i p t} = T r i p _ {p} + \tau_ {t} + T r i p _ {p} * \tau_ {t} + \gamma_ {1} \ln (w o r d s _ {i p t}) + \gamma_ {2} r a t i n g _ {i p t} + \alpha_ {i} + \varepsilon_ {i p t}\tag{A1}
$$

![](/api/attachments/3M9QE3DQ/fulltext/images/8522ae656d83f5a28380cc92cb39f18133bca0e827e8fa86b2a9796066d8b688.jpg)  
(a) Review Volume

![](/api/attachments/3M9QE3DQ/fulltext/images/9f32970a859e1752408bef8f3afc81d83d6c46d2a85f336d2d94dec2b0bfcab5.jpg)  
(b) Affective Process

![](/api/attachments/3M9QE3DQ/fulltext/images/6dc60b417d398c17031477f3e27ec1f9c8c64caa8a994231bcdafebf3b749871.jpg)  
(c) Positive Emotion

![](/api/attachments/3M9QE3DQ/fulltext/images/23b11f94c239b6f439d8b48289c3dd79e41479f60fbb8d95f4593024cd07aa0c.jpg)  
(d) Negative Emotion

![](/api/attachments/3M9QE3DQ/fulltext/images/31f53ae01e4458dd053fd4a700f4a3b0820b4cde4c7786fe273c176863f03300.jpg)  
(e) Cognitive Process

![](/api/attachments/3M9QE3DQ/fulltext/images/e4ce3502290127b6adca217ecddde4b385f7f698976e455ae27949fb725b815d.jpg)  
(f) Negation  
Figure A1. Visualization of Treatment Effects Over Time on DVs

In the above equation, i denotes restaurants, p indexes platforms and t indicates months. Figure A1 presents visualizations the coefficient estimates associated with our time dummy interactions for our DVs. As shown, we observe no evidence of pre-treatment trends (i.e., trends beginning prior to the date of treatment that lie in the same direction as the post-treatment trend). Accordingly, although the pre-treatment trends are not strictly parallel, the fact that the treatment drives a near immediate reversal in the difference in differences suggest that we have identified the true treatment effect. Moreover, over our period of study, we do not observe a peak in any of the treatment effects, suggesting that the effects continue to progress in magnitude beyond our window of observation.

Beyond the above, to further rule out the possibility that some other significant event (e.g., system changes) confounded the Instant Personalization treatment, we scoured TripAdvisor’s press releases<sup>1</sup> and Google News for articles related to Yelp. We found no mention of any significant changes to the TripAdvisor or Yelp interfaces between December 2010 and April 2011, indicating that our results are unlikely driven by spurious relationships

## References

Angrist, J. D., and Pischke, J. S. 2008. Mostly Harmless Econometrics: An Empiricist’s Companion, Princeton, NJ: Princeton University Press.

Burtch, G., Carnahan, S., and Greenwood, B. N. 2016. “Can You Gig It? An Empirical Examination of the Gig-Economy and Entrepreneurial Activity,” Working Paper, Carlson School of Management, University of Minnesota.

Chan, J., and Ghose, A. 2014. “Internet’s Dirty Secret: Assessing the Impact of Online Intermediaries on HIV Transmission,” MIS Quarterly (38:4), pp. 955-976.

Greenwood, B. N., and Wattal, S. 2017. “Show Me the Way to Go Home: An Empirical Investigation of Ride-Sharing and Alcohol Related Motor Vehicle Fatalities,” MIS Quarterly (41:1), pp. 163-187.

## Appendix B

## Separate DID Analyses

As an additional robustness check, we report separate/single-shock DID analyses for the two exogenous shocks, to evaluate the robustness of our main findings, which were obtained via a double DID specification. We estimate the following models, where the parameter of interest (i.e., the DID estimate) is β

$$
\ln (R e v i e w V o l u m e) _ {i p t} = \beta_ {0} T r i p _ {p} + \beta_ {1} T r i p \_ C h a n g e _ {t} + \beta_ {2} T r i p _ {p} * T r i p \_ C h a n g e _ {t} + \beta_ {3} \ln (w o r d s _ {i p t}) + \beta_ {4} r a t i n g _ {i p t} + \alpha_ {i} + \varepsilon_ {i p t}\tag{1}
$$

$$
\text { ReviewVolume } _ {i p t} = \beta_ {0} \text { Trip } _ {p} + \beta_ {1} \text { Trip\_Change } _ {t} + \beta_ {2} \text { Trip } _ {p} * \text { Trip\_Change } _ {t} + \beta_ {3} \ln (\text { words } _ {i p t}) + \beta_ {4} \text { rating } _ {i p t} + \alpha_ {i} + \varepsilon_ {i p t}\tag{2}
$$

$$
\ln (R e v i e w V o l u m e) _ {i p t} = \beta_ {0} Y e l p _ {p} + \beta_ {1} Y e l p \_ C h a n g e _ {t} + \beta_ {2} Y e l p _ {p} * Y e l p \_ C h a n g e _ {t} + \beta_ {3} \ln (w o r d s _ {i p t}) + \beta_ {4} r a t i n g _ {i p t} + \alpha_ {i} + \varepsilon_ {i p t}\tag{3}
$$

ReviewVolum $_ { \cdot i p t } = \beta _ { 0 } \ : Y e l p _ { p }$ + β<sub>1</sub> Yelp\_Change<sub>t</sub> + β<sub>2</sub> Yelp<sub>p</sub> ∗ Yelp\_Change<sub>t</sub> + β<sub>3</sub> ln(words<sub>ipt</sub>) + β<sub>4</sub> rating<sub>ipt</sub> + α<sub>i</sub> + ε<sub>ipt</sub>

(4)

$$
\ln (\text {Linguistic Characteristic}) _ {i p t} = \beta_ {0} \text {Trip} _ {p} + \beta_ {1} \text {Trip\_Change} _ {t} + \beta_ {2} \text {Trip} _ {p} * \text {Trip\_Change} _ {t} + \beta_ {3} \ln (\text {words} _ {i p t}) + \beta_ {4} \text {rating} _ {i p t} + \alpha_ {i} + \varepsilon_ {i p t}\tag{5}
$$

Linguistic Characteristi $c _ { i p t } = \beta _ { 0 } T r i p _ { p } + \beta _ { 1 }$ Trip\_Change<sub>t</sub> + β<sub>2</sub> Trip<sub>p</sub> ∗ Trip\_Change<sub>t</sub> + β<sub>3</sub> ln(words<sub>ipt</sub>) + β<sub>4</sub> rating<sub>ipt</sub> + α<sub>i</sub> + ε<sub>ipt</sub>

(6)

$$
\ln (\text { Linguistic   Characteristic }) _ {i p t} = \beta_ {0} \text { Yelp } _ {p} + \beta_ {1} \text { Yelp\_Change } _ {t} + \beta_ {2} \text { Yelp } _ {p} * \text { Yelp\_Change } _ {t} + \beta_ {3} \ln (\text { words } _ {i p t}) + \beta_ {4} \text { rating } _ {i p t} + \alpha_ {i} + \varepsilon_ {i p t}\tag{7}
$$

$$
\text { Linguistic   Characteristic } _ {i p t} = \beta_ {0} \text { Yelp } _ {p} + \beta_ {1} \text { Yelp\_Change } _ {t} + \beta_ {2} \text { Yelp } _ {p} * \text { Yelp\_Change } _ {t} + \beta_ {3} \ln (\text { words } _ {i p t}) + \beta_ {4} \text { rating } _ {i p t} + \alpha_ {i} + \varepsilon_ {i p t}\tag{8}
$$

First, we report the separate DID analyses results for review volume in Table B1 and Table B2, where we observe that, compared with Yelp, the review volume of TripAdvisor increased by 38.8% after implementing Instant Personalization. Similarly, compared to TripAdvisor, the review volume of Yelp increased by 18.2% after integrating Facebook Connect.

Second, we present the separate DID results for mental processes. Based on Tables B3 and Table B4, we observe that, compared with Yelp, affective processes on TripAdvisor increased by 1.8%, whereas cognitive processes decreased by 0.9% after implementing Instant Personalization. Additionally, positive emotion on TripAdvisor increased by 3% while negative emotion decreased by 21%. According to Table B5 and Table B6, compared with TripAdvisor, affective processes on Yelp increased by 6.4%, while cognitive processes declined by 2.4% after implementing Facebook Connect. Further, positive emotion on Yelp increased by 7.8% but negative emotion decreased by 10.2%.

Third, we show separate DID analyses results for the inhibition effect in Table B7 and Table B8. We observe that, compared with Yelp as the baseline control group, the use of negations on TripAdvisor decreased by 11.9% after implementing Instant Personalization. Similarly, compared with TripAdvisor, language references to negation on Yelp decreased by 8.1% after integrating with Facebook Connect.

<table><tr><td colspan="3">Table B1. TripAdvisor DID Volume Effect</td></tr><tr><td>Variables</td><td>(1) In(Review Volume)</td><td>(2) Review Volume</td></tr><tr><td>Trip</td><td>-0.841***(0.018)</td><td>-3.482***(0.132)</td></tr><tr><td>Trip_Change</td><td>0.257***(0.006)</td><td>1.210***(0.037)</td></tr><tr><td>Trip * Trip_Change</td><td>0.388***(0.014)</td><td>1.377***(0.116)</td></tr><tr><td>In(words)</td><td>0.247***(0.005)</td><td>0.952***(0.027)</td></tr><tr><td>Rating</td><td>0.014***(0.003)</td><td>0.082***(0.015)</td></tr><tr><td>Constant</td><td>-0.124***(0.026)</td><td>-0.353*(0.143)</td></tr><tr><td>Observations</td><td>112,262</td><td>112,262</td></tr><tr><td>R-squared</td><td>0.220</td><td>0.140</td></tr><tr><td>Number of restaurants</td><td>3,964</td><td>3,964</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.1

Table B3. TripAdvisor DID Affective and Cognitive Processes

<table><tr><td colspan="3">Table B2. Yelp DID Volume Effect</td></tr><tr><td>Variables</td><td>(1) In(Review Volume)</td><td>(2) Review Volume</td></tr><tr><td>Yelp</td><td>0.612***(0.021)</td><td>2.117***(0.119)</td></tr><tr><td>Yelp_Change</td><td>0.006(0.015)</td><td>-0.010(0.067)</td></tr><tr><td>Yelp * Yelp_Change</td><td>0.182***(0.016)</td><td>0.858***(0.078)</td></tr><tr><td>In(words)</td><td>0.149***(0.006)</td><td>0.573***(0.029)</td></tr><tr><td>Rating</td><td>0.006(0.003)</td><td>0.026*(0.013)</td></tr><tr><td>Constant</td><td>-0.462***(0.041)</td><td>-1.570***(0.231)</td></tr><tr><td>Observations</td><td>47,151</td><td>47,151</td></tr><tr><td>R-squared</td><td>0.195</td><td>0.150</td></tr><tr><td>Number of restaurants</td><td>3,178</td><td>3,178</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.1

<table><tr><td>Variables</td><td>(1) In(Affective Process)</td><td>(2) Affective Process</td><td>(3) In(Cognitive Process)</td><td>(4) Cognitive Process</td></tr><tr><td>Trip</td><td>-0.160***(0.006)</td><td>-0.967***(0.033)</td><td>0.051***(0.003)</td><td>0.739***(0.056)</td></tr><tr><td>Trip_Change</td><td>0.042***(0.002)</td><td>0.294***(0.017)</td><td>0.004**(0.001)</td><td>0.067**(0.022)</td></tr><tr><td>Trip * Trip_Change</td><td>0.018**(0.006)</td><td>0.095*(0.037)</td><td>-0.009*(0.003)</td><td>-0.115+(0.059)</td></tr><tr><td>In(words)</td><td>-0.235***(0.003)</td><td>-1.797***(0.017)</td><td>0.039***(0.002)</td><td>0.855***(0.028)</td></tr><tr><td>Rating</td><td>0.094***(0.002)</td><td>0.593***(0.009)</td><td>-0.012***(0.001)</td><td>-0.198***(0.015)</td></tr><tr><td>Constant</td><td>2.745***(0.015)</td><td>13.971***(0.096)</td><td>2.571***(0.009)</td><td>11.860***(0.154)</td></tr><tr><td>Observations</td><td>110,337</td><td>110,669</td><td>108,368</td><td>110,669</td></tr><tr><td>R-squared</td><td>0.152</td><td>0.143</td><td>0.015</td><td>0.020</td></tr><tr><td>Number of restaurants</td><td>3,958</td><td>3,961</td><td>3,953</td><td>3,961</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.1

Table B4. TripAdvisor DID Positive and Negative Affective Processes

<table><tr><td>Variables</td><td>(1) In(Positive Emotion)</td><td>(2) Positive Emotion</td><td>(3) In(Negative Emotion)</td><td>(4) Negative Emotion</td></tr><tr><td>Trip</td><td>-0.196***(0.006)</td><td>-1.016***(0.043)</td><td>0.225***(0.014)</td><td>0.025(0.015)</td></tr><tr><td>Trip_Change</td><td>0.047***(0.003)</td><td>0.292***(0.018)</td><td>-0.044***(0.005)</td><td>0.006(0.007)</td></tr><tr><td>Trip * Trip_Change</td><td>0.030***(0.007)</td><td>0.096*(0.047)</td><td>-0.210***(0.015)</td><td>-0.053**(0.016)</td></tr><tr><td>In(words)</td><td>-0.270***(0.003)</td><td>-2.154***(0.024)</td><td>-0.300***(0.007)</td><td>-0.020*(0.008)</td></tr><tr><td>Rating</td><td>0.188***(0.002)</td><td>1.101***(0.011)</td><td>-0.295***(0.003)</td><td>-0.436***(0.006)</td></tr><tr><td>Constant</td><td>2.410***(0.016)</td><td>12.815***(0.126)</td><td>2.425***(0.033)</td><td>2.656***(0.054)</td></tr><tr><td>Observations</td><td>109,966</td><td>110,669</td><td>86,307</td><td>110,669</td></tr><tr><td>R-squared</td><td>0.236</td><td>0.228</td><td>0.129</td><td>0.128</td></tr><tr><td>Number of restaurants</td><td>3,958</td><td>3,961</td><td>3,929</td><td>3,961</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.1

<table><tr><td>Variables</td><td>(1) In(Affective Process)</td><td>(2) Affective Process</td><td>(3) In(Cognitive Process)</td><td>(4) Cognitive Process</td></tr><tr><td>Yelp</td><td>0.076***(0.011)</td><td>0.083(0.089)</td><td>-0.013*(0.006)</td><td>-0.389***(0.087)</td></tr><tr><td>Yelp_Change</td><td>-0.035**(0.012)</td><td>-0.443***(0.098)</td><td>0.025***(0.007)</td><td>0.346***(0.104)</td></tr><tr><td>Yelp * Yelp_Change</td><td>0.064***(0.013)</td><td>0.650***(0.100)</td><td>-0.024**(0.007)</td><td>-0.354***(0.107)</td></tr><tr><td>In(words)</td><td>-0.193***(0.004)</td><td>-1.620***(0.030)</td><td>0.063***(0.003)</td><td>0.646***(0.036)</td></tr><tr><td>Rating</td><td>0.076***(0.002)</td><td>0.474***(0.015)</td><td>-0.011***(0.001)</td><td>-0.172***(0.021)</td></tr><tr><td>Constant</td><td>2.498***(0.024)</td><td>13.174***(0.181)</td><td>2.458***(0.015)</td><td>13.151***(0.206)</td></tr><tr><td>Observations</td><td>46,767</td><td>46,821</td><td>46,807</td><td>46,821</td></tr><tr><td>R-squared</td><td>0.103</td><td>0.114</td><td>0.022</td><td>0.015</td></tr><tr><td>Number of restaurants</td><td>3,174</td><td>3,174</td><td>3,174</td><td>3,174</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.1

<table><tr><td>Variables</td><td>(1) In(Positive Emotion)</td><td>(2) Positive Emotion</td><td>(3) In(Negative Emotion)</td><td>(4) Negative Emotion</td></tr><tr><td>Yelp</td><td>0.097***(0.012)</td><td>0.063(0.088)</td><td>-0.052*(0.022)</td><td>0.036(0.022)</td></tr><tr><td>Yelp_Change</td><td>-0.040**(0.013)</td><td>-0.433***(0.096)</td><td>0.049*(0.024)</td><td>0.038(0.023)</td></tr><tr><td>Yelp * Yelp_Change</td><td>0.078***(0.014)</td><td>0.662***(0.098)</td><td>-0.102***(0.025)</td><td>-0.047+(0.026)</td></tr><tr><td>In(words)</td><td>-0.226***(0.005)</td><td>-1.622***(0.029)</td><td>-0.231***(0.009)</td><td>-0.024**(0.009)</td></tr><tr><td>Rating</td><td>0.171***(0.003)</td><td>0.862***(0.014)</td><td>-0.253***(0.005)</td><td>-0.434***(0.006)</td></tr><tr><td>Constant</td><td>2.118***(0.027)</td><td>10.768***(0.178)</td><td>2.054***(0.050)</td><td>2.650***(0.048)</td></tr><tr><td>Observations</td><td>46,670</td><td>46,821</td><td>38,299</td><td>46,821</td></tr><tr><td>R-squared</td><td>0.191</td><td>0.175</td><td>0.112</td><td>0.101</td></tr><tr><td>Number of restaurants</td><td>3,173</td><td>3,174</td><td>3,108</td><td>3,197</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, + p < 0.1

<table><tr><td colspan="3">Table B7. TripAdvisor DID Inhibition Effect</td></tr><tr><td>Variables</td><td>(1) In(Negation)</td><td>(2) Negation</td></tr><tr><td>Trip</td><td>0.509***(0.010)</td><td>0.576***(0.018)</td></tr><tr><td>Trip_Change</td><td>-0.018***(0.005)</td><td>0.026***(0.007)</td></tr><tr><td>Trip * Trip_Change</td><td>-0.119***(0.011)</td><td>-0.068***(0.019)</td></tr><tr><td>In(words)</td><td>-0.265***(0.006)</td><td>-0.006(0.009)</td></tr><tr><td>Rating</td><td>-0.200***(0.003)</td><td>-0.351***(0.005)</td></tr><tr><td>constant</td><td>1.993***(0.030)</td><td>2.355***(0.053)</td></tr><tr><td>Observations</td><td>93,870</td><td>110,669</td></tr><tr><td>R-squared</td><td>0.143</td><td>0.093</td></tr><tr><td>Number of restaurants</td><td>3,937</td><td>3,961</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="3">Table B8. Yelp DID Inhibition Effect</td></tr><tr><td>Variables</td><td>(1) ln(Negation)</td><td>(2) Negation</td></tr><tr><td>Yelp</td><td>-0.389***(0.017)</td><td>-0.543***(0.030)</td></tr><tr><td>Yelp_Change</td><td>0.061***(0.017)</td><td>0.042(0.033)</td></tr><tr><td>Yelp * Yelp_Change</td><td>-0.081***(0.018)</td><td>-0.038+(0.024)</td></tr><tr><td>ln(words)</td><td>-0.231***(0.008)</td><td>-0.047***(0.012)</td></tr><tr><td>rating</td><td>-0.170***(0.004)</td><td>-0.285***(0.007)</td></tr><tr><td>constant</td><td>2.138***(0.044)</td><td>2.855***(0.071)</td></tr><tr><td>Observations</td><td>40,877</td><td>46,821</td></tr><tr><td>R-squared</td><td>0.121</td><td>0.098</td></tr><tr><td>Number of restaurants</td><td>3,139</td><td>3,174</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.1

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.1

## Appendix C

## Additional Analyses

Table C1 reports changes in user-level monthly reviewing volumes and language characteristics over the two year period surrounding TripAdvisor’s social network integration (12 months before and after the event). This simple pre/post user-level data enables us to gain some sense of whether behavior appeared to change within users as a result of the treatment. For review volumes, we estimate the effect of TripAdvisor social network integration on users’ average monthly number of reviews. For the linguistic features, due to limited scalability of the LIWC software to process large amounts of textual data, we randomly sampled a subset of users who jointly authored a total of approximately 750,000 reviews. Amongst these reviews, 96,356 were authored within our two year time window. Considering the results in Table C1, we observe that the social network integration is significantly associated with changes in all of our outcome variables, suggesting that our results may be attributable to within-user changes in behavior. One caveat of this analysis, however, is that we are unable to account for underlying time trends and other factors, because there is no true control group (all data comes from a single platform). Thus, this evidenc is merely correlational, and thus circumstantial. Future work might therefore explore the relative roles of selection versus within-user changes in behavior.

Table C2 reports an additional analysis using a continuous measure (number of months since the user registered on the platform) of user tenure. This analysis yields similar results for the binary user tenure variable.

Table C3 reports robustness checks of our main analyses (log-transformed DVs) while controlling for seasonal trends (with 11 dummy variables, i.e. February, March, April, ..., December). These results are largely consistent with our main findings.

<table><tr><td colspan="7">Table C1. Effect of Social Network Integration on Within User Review Volume and Language Characteristics</td></tr><tr><td>Variables</td><td>(1)ReviewVolume</td><td>(2)AffectiveProcess</td><td>(3)PositiveEmotion</td><td>(4)NegativeEmotion</td><td>(5)CognitiveProcess</td><td>(6)Negation</td></tr><tr><td>Trip_Change</td><td>0.792***(0.017)</td><td>0.103*(0.044)</td><td>0.139***(0.041)</td><td>-0.033*(0.013)</td><td>-0.165**(0.219)</td><td>-0.036*(0.014)</td></tr><tr><td>Constant</td><td>2.288***(0.012)</td><td>6.480***(0.036)</td><td>5.501***(0.034)</td><td>0.748***(0.010)</td><td>7.927***(0.044)</td><td>1.304***(0.011)</td></tr><tr><td>Observations</td><td>244,978</td><td>96,356</td><td>96,356</td><td>96,356</td><td>96,356</td><td>96,356</td></tr><tr><td>F-Statistic</td><td>2164.85***</td><td>5.44*</td><td>11.34***</td><td>6.64**</td><td>7.05***</td><td>6.63**</td></tr><tr><td>Number of Users</td><td>70,450</td><td>5,174</td><td>5,174</td><td>5,174</td><td>5,174</td><td>5,174</td></tr><tr><td>User Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

Table C2. Effects of Continuous User Tenure on Review Language Characteristics

<table><tr><td>Variables</td><td>(1) Affective Process</td><td>(2) Positive Emotion</td><td>(3) Negative Emotion</td><td>(4) Cognitive Process</td><td>(5) Negation</td></tr><tr><td>In(tenure)</td><td>0.019(0.016)</td><td>0.029(0.016)</td><td>-0.008(0.005)</td><td>0.030(0.019)</td><td>0.010(0.006)</td></tr><tr><td>In(words)</td><td>-3.065***(0.047)</td><td>-3.081***(0.048)</td><td>0.010(0.012)</td><td>0.935***(0.043)</td><td>0.045**(0.014)</td></tr><tr><td>Rating</td><td>0.634***(0.020)</td><td>1.036***(0.021)</td><td>-0.406***(0.011)</td><td>-0.185***(0.026)</td><td>-0.444***(0.010)</td></tr><tr><td>Constant</td><td>18.270***(0.249)</td><td>15.883***(0.245)</td><td>2.386***(0.093)</td><td>12.053***(0.293)</td><td>3.088***(0.100)</td></tr><tr><td>Observations</td><td>46,341</td><td>46,341</td><td>46,341</td><td>46,341</td><td>46,341</td></tr><tr><td>R-squared</td><td>0.259</td><td>0.290</td><td>0.088</td><td>0.022</td><td>0.064</td></tr><tr><td>Number of Restaurants</td><td>2,755</td><td>2,755</td><td>2,755</td><td>2,755</td><td>2,755</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05

Table C3. Estimation with Adjustment for Seasonality (Log-Transformed Outcomes)

<table><tr><td>Variables</td><td>(1)In(Review Volume)</td><td>(2)In(Affective Process)</td><td>(3)In(Positive Emotion)</td><td>(4)In(Negative Emotion)</td><td>(5)In(Cognitive Process)</td><td>(6)In(Negation)</td></tr><tr><td>Trip</td><td>-0.647***(0.019)</td><td>-0.083***(0.007)</td><td>-0.101***(0.008)</td><td>0.087***(0.017)</td><td>0.007(0.005)</td><td>0.394***(0.014)</td></tr><tr><td>Trip_change</td><td>0.238***(0.006)</td><td>0.041***(0.002)</td><td>0.046***(0.003)</td><td>-0.040***(0.005)</td><td>0.008***(0.002)</td><td>-0.016***(0.005)</td></tr><tr><td>Trip * Trip_Change</td><td>0.379***(0.014)</td><td>0.025***(0.005)</td><td>0.040***(0.006)</td><td>-0.200***(0.012)</td><td>-0.004(0.003)</td><td>-0.114***(0.010)</td></tr><tr><td>Yelp_change</td><td>0.059***(0.014)</td><td>-0.035***(0.007)</td><td>-0.042***(0.008)</td><td>0.057**(0.019)</td><td>0.033***(0.005)</td><td>0.078***(0.015)</td></tr><tr><td>Yelp * Yelp_Change</td><td>0.195***(0.015)</td><td>0.076***(0.008)</td><td>0.094***(0.009)</td><td>-0.123***(0.020)</td><td>-0.031***(0.005)</td><td>-0.106***(0.016)</td></tr><tr><td>In(words)</td><td>0.182***(0.004)</td><td>-0.220***(0.002)</td><td>-0.255***(0.002)</td><td>-0.257***(0.005)</td><td>0.077***(0.001)</td><td>-0.234***(0.004)</td></tr><tr><td>Rating</td><td>0.014***(0.003)</td><td>0.090***(0.001)</td><td>0.183***(0.001)</td><td>-0.283***(0.003)</td><td>-0.012***(0.001)</td><td>-0.192***(0.002)</td></tr><tr><td>Constant</td><td>0.001(0.024)</td><td>2.655***(0.012)</td><td>2.311***(0.013)</td><td>2.254***(0.027)</td><td>2.377***(0.008)</td><td>1.855***(0.024)</td></tr><tr><td>Observations</td><td>139,239</td><td>137,158</td><td>136,760</td><td>109,450</td><td>137,272</td><td>118,205</td></tr><tr><td>R-squared</td><td>0.224</td><td>0.146</td><td>0.234</td><td>0.125</td><td>0.030</td><td>0.135</td></tr><tr><td>Number of Restaurants</td><td>3,968</td><td>3,963</td><td>3,963</td><td>3,936</td><td>3,962</td><td>3,944</td></tr><tr><td>Restaurant Fixed Effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Seasonality</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Cluster-robust standard errors in parentheses. \*\*\*p < 0.001, \*\*p < 0.01, \*p < 0.05, +p < 0.1
