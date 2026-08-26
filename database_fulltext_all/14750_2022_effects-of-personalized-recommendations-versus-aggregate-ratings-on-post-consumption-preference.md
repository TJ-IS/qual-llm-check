---
otero_id: 14750
otero_key: "JU7R533C"
title: "Effects of Personalized Recommendations Versus Aggregate Ratings on Post-Consumption Preference Responses"
authors: "Gediminas Adomavicius; Jesse C. Bockstedt; Shawn P. Curley; Jingjing Zhang"
year: "2022"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/16301"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# EFFECTS OF PERSONALIZED RECOMMENDATIONS VERSUS AGGREGATE RATINGS ON POST-CONSUMPTION PREFERENCE RESPONSES<sup>1</sup>

Gediminas Adomavicius Information and Decision Sciences, Carlson School of Management, University of Minnesota, 321 19<sup>th</sup> Avenue South, Minneapolis, MN 55455 U.S.A. {gedas@umn.edu}

Jesse C. Bockstedt Information Systems and Operations Management, Goizueta Business School, Emory University, 1300 Clifton Road, Atlanta, GA 30322 U.S.A. {bockstedt@emory.edu}

Shawn P. Curley Information and Decision Sciences, Carlson School of Management, University of Minnesota, 321 19<sup>th</sup> Avenue South, Minneapolis, MN 55455 U.S.A. {curley@umn.edu}

Jingjing Zhang Operations and Decision Technologies, Kelley School of Business, Indiana University, 1309 East Tenth Street, Bloomington, IN 47405 U.S.A. {jjzhang@indiana.edu}

Online retailers use product ratings to signal quality and help consumers identify products for purchase. These ratings commonly take the form of either non-personalized, aggregate product ratings (i.e., the average rating a product received from a number of consumers such as “the average rating is 4.5/5 based on 100 reviews”), or personalized predicted preference ratings for a product (i.e., recommender-system-generated predictions for a consumer’s rating of a product such as “we think you’d rate this product 4.5/5”). Ratings in either format can provide decision aid to the consumer, but the two formats convey different types of product quality information and operate with different psychological mechanisms. Prior research has indicated that each recommendation type can significantly affect consumer’s post-experience preference ratings, constituting a judgmental bias, but has not compared the effects of these two common product-rating formats. Using a laboratory experiment, we show that aggregate ratings and personalized recommendations create similar biases on post-experience preference ratings when shown separately. Shown together, there is no cumulative increase in the effect. Instead, personalized recommendations tend to dominate. Our findings can help retailers determine how to use these different types of product ratings to most effectively serve their customers. Additionally, these results help to educate the consumer on how product-rating displays influence their stated preferences.

Keywords: Online product ratings, recommender systems, personalized ratings, aggregate ratings, recom mendation bias, laboratory experiments

## Introduction

Online retail environments often present consumers with an overwhelmingly large number of product options. Information overload and the paradox of choice can negatively impact consumer decision making in these environments (Schwartz 2004). As a result, online retailers employ decision aids to help consumers effectively make product choices (Ansari et al. 2000; Bodapati 2008; Chevalier and Mayzlin 2006). Two commonly used decision aids in online retail environments are personalized product recommendations and aggregate user ratings of products.

Personalized product recommendations derive from recommender systems that typically take the user’s preference ratings of previously experienced items as inputs, along with information about other users and/or the items of interest, and use computational techniques to predict the user’s preferences for unexperienced items (Adomavicius and Tuzhilin 2005; Ricci et al. 2015). These predictions can then be displayed as estimated system predictions that serve as personalized product recommendations.<sup>2</sup> Users complete the cycle by submitting their preference ratings for the experienced items. The system uses these post-experience<sup>3</sup> user ratings to analyze its accuracy and improve future recommendations.

User ratings can also be used by online retailers to display an aggregate (or average) user rating next to a product listing. Aggregate user ratings are non-personalized recommendations (i.e., the same for all users) that may derive from peer ratings or from aggregating other user behaviors, such as sales, downloads, or clicks. Like personalized recommendations, aggregate ratings are supplied as a quality indicator that plays an important role in consumers’ research and decision-making (Sun 2012; Tucker and Zhang 2011; Zhu and Zhang 2010).

As inputs to these systems, recommendation providers explicitly or implicitly expect that consumers’ self-reported post-experience judgments are indicative of consumer preferences. But, these judgments can be significantly distorted by observing the recommendations, constituting a judgmental bias (Adomavicius et al. 2013; Cosley et al. 2003). Yet, despite the fact that aggregate and personalized recommendation ratings are often presented in an identical or nearly identical manner to users (e.g., as numeric values or star ratings), the underlying information conveyed by the two ratings is very different. Personalized predicted ratings represent a recommender system’s estimated preferences of an individual user and are calculated using machine learning algorithms with no apparent social component. Even in cases where other users’ preferences are used by the system to predict a focal user’s rating (and not all recommender systems do that), this connection to other users typically is not explicit in the display. What is apparent is that the personalized ratings are tailored to each individual user’s unique tastes, that is, they predict how much a specific user is expected to like the corresponding items. Aggregate user ratings, on the other hand, are non-personalized representations of the populationlevel judgment. They are a social communication provided by other consumers regarding product quality (Amblee and Bui 2011).

Since both are in common (and often simultaneous) use, understanding the comparable and contrasting effects of predicted preference ratings and aggregate user ratings will help online retailers make better strategic decisions about investing in, developing, and deploying these decision aid systems. To this end, we explore two primary issues related to the impact of aggregate user ratings and personalized predicted ratings on consumer preferences:

(1) The relative effect size issue: Which type of information results in a higher effect size: aggregate user ratings or personalized predicted ratings?

(2) The combination issue: Retailers sometimes provide both personalized predicted ratings and aggregate user ratings as aids to the consumer. As such, we also ask: What is the combined effect of receiving both aggregate and personalized ratings, as compared to receiving one alone?

We conduct a series of laboratory experiments to answer these research questions. The specific hypotheses, and their theoretical foundations, are discussed in the next section.

## Background and Hypotheses

In this section, we identify the notion of a judgmental bias and its manifestation within a preference setting in which the consumer is receiving recommendations. In addition, we contrast personalized predicted ratings and aggregate user ratings as a motivation for the hypotheses.

## Recommendation Bias

In lay usage, the term bias has a negative connotation. In behavioral economics and decision research, however, the word bias is used in a more agnostic manner to represent a systematic pattern of deviation from a norm or rational standard of judgment (Haselton et al. 2015). The term highlights predictable tendencies that judgments follow under certain decision conditions. In the context of individual users responding to recommendations, we define bias relative to a rational standard that is at least implicit, if not explicit, in realworld instances of their use. The presumption is that the consumer’s stated rating (provided after consuming the product or service) is an unadulterated expression of their preference for the product or service, as tailored to the provided scale. We highlight two aspects of this treatment of bias in the recommendation context.

First, it is important to recognize the timing of the display of a recommendation (which may be a personalized predicted or aggregate rating) and the consumers’ submitted preference rating (compare the related distinction between pre-purchase and post-purchase evaluations; Moe and Schweidel 2012). Prior to experiencing the item, consumers seek and receive recommendations as a way of guiding their judgments, choices, and/or purchases of the item. At this preconsumption stage, the recommendations represent a highly valuable service to consumers, helping them to find and select relevant items and to manage the potential information overload in many online settings. However, the recommendation is not presumed to continue providing value once a consumer experiences the item. This is particularly true immediately after item consumption, that is, when there is no potential uncertainty about the experience due to recall effects (e.g., as compared to trying to recall one’s preference for a movie seen a year ago). In other words, recommendations are designed to provide value at the pre-consumption stage; if they affect post-consumption preferences as well, this represents a bias relative to the standard of unpolluted preference.

Post-experience biases produced by personalized recommendations can be harmful in several ways (Adomavicius et al. 2013; Cosley et al. 2003). From the consumers’ perspective, recommendation biases can manipulate their preferences and their purchasing behavior, leading to distortions in their submitted preference ratings and suboptimal product choices. From the recommending firm’s perspective, these biases may allow third-party agents to manipulate the recommender system to operate in their favor, reducing consumers’ trust in the system and decreasing its value in the long term. From the system designers’ perspective, the distorted user preference ratings that are submitted as consumers’ feedback can pollute the inputs of the recommender system, reducing the system’s effectiveness and calling its value into question.

Second, we follow the behavioral decision literature in defining bias for individuals’ judgments and choices. Biases at the individual level can also lead to impacts at a macro level, as well. The market, macro-level perspective investigates the effects of recommendations in the form of both personalized ratings and aggregate user information upon sales, downloads, or other aggregate outcomes of interest to retailers. The study of market outcomes has been an active area of research investigation in recent years, particularly on the effects of providing aggregate ratings (e.g., Chevalier and Mayzlin 2006; Duan et al. 2008; Sun 2012; Zhu and Zhang 2010). The effects of personalized recommendations on market factors has been less-studied, but also present (e.g., Fleder and Hosanagar 2009).

In common with all of these studies is the focus on the corporate, macro viewpoint. In contrast, the focus of the current study is upon the influence of recommendations on postexperience bias defined at an individual, micro-level of analysis. In this light, the next two subsections will review past research related to the use of two general forms of recommendations and their effects upon users’ stated preferences: How do personalized system-predicted ratings and aggregate user ratings influence the bias in individual consumers’ post-experience reactions?

## Preference Bias with Personalized Recommender Systems

A few studies have explored how personalized predicted ratings from recommender systems influence post-experience online consumer behavior. These studies provide strong and consistent evidence that consumers’ post-consumption ratings are biased toward observed system-generated recommendations. For example, Cosley et al. (2003) found that when users re-rated a movie while being shown a value that was altered upward or downward from their system’s actual prediction by one point (i.e., providing a higher or lower prediction), users tended to give higher or lower ratings, respectively, as compared to a control group receiving the system’s actual predictions.

More recently, Adomavicius et al. (2013) examined system effects in three laboratory studies in which preference ratings were elicited at the time of item consumption, thereby removing possible explanations deriving from the uncertainty that can be present for an item that may have been experienced long ago. In this setting, consumers should arguably base their preferences solely on the immediate experience of the item; no uncertainty is present. Still, the observed systemgenerated personalized recommendations consistently influenced consumers’ post-experience ratings. The effect was observed across different content domains (TV shows and jokes), and the effect obtained whether the recommendation was seen before or after watching a TV show.

Overall, the prior research has shown that biases resulting from personalized system recommendations on postexperience preference judgments are extremely robust. Personalized recommendations consistently introduce bias across a variety of digital goods, including movies, TV shows, jokes, and songs. The bias occurs both for rating responses, as well as for willingness-to-pay judgments where there are real economic consequences (Adomavicius et al. 2018).

## Preference Bias with Aggregate User Ratings

Besides personalized, system-predicted ratings, nonpersonalized, aggregate user ratings can provide an alternate source of information about item quality of potential relevance to forming users’ product judgements. Product ratings and reviews shared by an online community provide added quality information that significantly influences a consumer’s decisions (e.g., Benlian et al. 2012; Godinho de Matos et al. 2016; Lee et al. 2015; Muchnik et al. 2013; Schlosser 2005; Sridhar and Srinivasan 2012; Surowiecki 2004). Laboratory and field studies have shown significant pre-experience effects of aggregate information on user behavior and sales (e.g., Hu et al. 2014; Moe and Trusov 2011; Wu and Gaytán 2013).

More to the point, post-experience effects have been observed. For example, Lee et al. (2015) found that one’s personal ratings for an item can be influenced by the aggregate ratings of friends and strangers on a social movie website. Ho et al. (2017), although primarily interested in determinants of whether to post a review, also showed evidence of an effect of aggregate ratings on post-experience ratings for a variety of consumer products. Muchnik et al. (2013) used a field experiment on a social news site to demonstrate the differential effects of positive and negative social influence of aggregate ratings on a user’s individual ratings. They show that the biases resulting from personalized system recommendations on post-experience preference judgments have a counterpart in a biasing effect of aggregate ratings.

On a cautionary note, though, Salganik and Watts (2008) supported the effect that aggregate popularity feedback had upon individual-level responses in terms of choices to listen to and download songs, also supporting an effect of this social influence on market factors. However, the effect was only clearly positive where the aggregate ratings were accurate in indicating popularity. When the songs were manipulated so that lower-rated songs were presented as having higher aggregate ratings than they actually had; that is, where popularity and the presentation did not correspond, the positive benefits were lessened. This suggests that any user-level effects of aggregate ratings may be less stable than those that have been observed with personalized ratings.

## Comparing Personalized and Aggregate User Ratings

Benlian et al. (2012), using a factorial experimental design, demonstrated that provider recommendations (i.e., “customers who bought this item also bought…”) and consumer reviews (text reviews) both affected the users’ trust and judged acceptability of consumer products, but in markedly different ways. This highlights the importance of studying the joint impacts of the two forms of recommendation—aggregate and personalized ratings—and their relative effects on users’ judgments. Despite the common identification of the biasing effects of recommendations on post-experience judgments and behavior, there has been little research that has explicitly compared the effects of aggregate user ratings with the effects of personalized recommendations on users’ preference construction, solely or in tandem. The issue is of particular interest since the rating types operate via different psychological mechanisms, suggesting differing effects.

The effect of aggregate ratings derives from social motivations (Aral 2014). The general dynamic is one in which the consumer engages in a form of observational learning of how to behave based on the behavior of others. In contrast, personalized recommendations do not arise from social comparison. Depending on the specific recommendation algorithm, the personalized system-predicted rating for a given user may not even have any connections with other users’ behavior (Ricci et al. 2015), for example, as in the case of content-based algorithms. Even algorithms that incorporate preferences of other users (e.g., collaborative filtering techniques) generally do not make the connection explicit or obvious to the consumers. Rather, personalized ratings are believed to have an impact on user preferences as informative individualized pieces of knowledge to be integrated into the users’ judgments, which is precisely the role that personalized recommendations are intended to have pre-experience. The results indicate that actual experience does not remove this effect, and the ratings continue to have an influence through the operation of fundamental, information integration mechanisms (e.g., as discussed by Adomavicius et al. 2018; Kahneman 2011; Mussweiler and Strack 1999; Tversky et al. 1988).

In sum, personalized predicted ratings incorporate information related to the preferences of individual users and are presumed to affect users’ judgments through a process of integrating relevant information in a cognitive assessment of personal quality. Aggregate user ratings represent preference consensus information and are presumed to operate via social comparison, identification, and learning from others. The differences in underlying mechanisms suggest potentially differing impacts for the effects of recommendations on users’ post-experience judgments. Aggregate ratings have no personalized element. In addition, aggregate ratings come from an anonymous aggregate to which the user has no in-group or other apparent affiliation. Upon immediate consumption of an item, there is no compelling argument for users to believe that the aggregate information applies to them. Conveying no personalized information, one might thus expect that the aggregate rating data is much easier to minimize postexperience. Thus, we hypothesize a lesser biasing effect of aggregate ratings:

Hypothesis 1 (Relative Effect Size with Independent Presentation): The post-experience preference ratings of users receiving personalized predicted ratings will be more biased (i.e., preference ratings will be more pulled toward displayed recommendations) than those of users receiving aggregate user ratings.

As any cursory viewing of online retail confirms, it is not unusual for a site to offer both aggregate rating information and personalized ratings in tandem. The second hypothesis can be considered a direct corollary of Hypothesis 1, as a refinement for the situation of joint presentation of the two kinds of information. Specifically, we expect the relative effect size difference to persist when the two rating types appear together:

Hypothesis 2 (Relative Effect Size with Joint Presentation): When both recommendation types (personalized predicted ratings and aggregate user ratings) are presented together, users postexperience preference ratings will be more affected by the personalized predicted rating than the aggregate user rating.

In addition to the individual effects when presented together, the joint impact of the ratings is of interest. Three general patterns of a combined effect can be identified: additive, multiplicative, or substitutive. An additive relationship is one where both recommendation types have a significant main effect with no interaction. A multiplicative relationship is one with a significant positive interactive relationship in addition to the main effects (i.e., the combined effect is greater than the sum of the individual effects). A substitutive relationship is one in which the main effect of adding a second recommendation is eliminated in the presence of the stronger recommendation. Given the differing mechanisms involved with the two types of recommendation, we hypothesize:

Hypothesis 3 (Combined Effect): The combined effect of receiving both a personalized predicted rating and an aggregate user rating will be consistent with an additive combination of their individual effects.

## Methods

We manipulate the availability of recommendations presented to participants in the form of aggregate averages and/or personalized ratings, singly and together. Participants read a number of jokes, reporting their preference ratings immediately after reading each joke. For identifying bias, we manipulate the recommendations presented to users to be either randomly high or low (Tversky and Kahneman 1974). By randomizing the recommendations, we avoid issues of underlying quality and are able to isolate the causal impact of the displayed recommendations on user preferences. In addition, we present both system-predicted personalized ratings and mean aggregate user ratings to users in the form of numerical values on a 1–5 scale. Using a common interface mechanism allows us to isolate the effects strictly due to the type of recommendation—personalized or aggregate—and compare them directly.

## Participants

Participants were 173 recruits from a U.S. college’s research participant pool paid a fixed \$10 fee for completing the study. Table 1 summarizes the demographic features of the sample for each of the four conditions of the between-subjects component of the design. Participant characteristics are comparable among the treatment groups.<sup>4</sup> The mean time for completing the study was 29 minutes, which suggests subjects invested ample time and that fatigue was not an issue.

Table 1. Demographic Characteristics of Participants, by Treatment Group

<table><tr><td></td><td colspan="2">Single Recommendation</td><td colspan="2">Both Recommendations</td></tr><tr><td>Treatment groups →</td><td>Aggregate Only</td><td>Personalized Only</td><td>Personalized First</td><td>Aggregate First</td></tr><tr><td># Participants</td><td>59</td><td>59</td><td>28</td><td>27</td></tr><tr><td>% Female</td><td>47.5%</td><td>45.8%</td><td>35.7%</td><td>48.2%</td></tr><tr><td>Age: Mean (SD)</td><td>24.0 (9.03)</td><td>23.6 (8.70)</td><td>24.1 (7.07)</td><td>25.7 (12.26)</td></tr><tr><td>% Native English Speaker</td><td>61.0%</td><td>50.9%</td><td>67.9%</td><td>70.4%</td></tr><tr><td>% Undergrad</td><td>55.7%</td><td>64.5%</td><td>55.4%</td><td>56.78%</td></tr></table>

## Stimuli

We used jokes from the Jester Online Joke Recommender System repository (http://eigentaste.berkeley.edu/dataset), which has been extensively used in prior literature (e.g., Adomavicius et al. 2013; Goldberg et al. 2001). We used Dataset 2, which contains 150 jokes, trimming the dataset to a final pool of 100 jokes for use in the experiment.<sup>5</sup>

The effects of personalized ratings on biasing post-experience judgments and economic choices have been robust and regular across various stimuli, including jokes as well as traditional consumer items like music, TV shows, and movies, arguing for a generalizability of our results. Jokes were selected as a set of stimuli that is appropriate for our subject population and affords the ability for users to experience multiple items within a manageable time period in a single laboratory session using a within-subjects component for the experimental design. Jokes also allow us to observe preference responses separate from the other economic factors that may come into play with products in a field setting (e.g., users’ budgetary constraints). We gathered participants’ preference ratings immediately after the reading of each joke, so that there was no uncertainty of preference due to memory effects. As noted, the standard assumption in such a situation is that the user’s rating should provide an unadulterated expression of their preference for the joke at the time of consumption. To control for the potential issue that participants may have preexisting preferences for the jokes in the study, we asked participants to indicate whether they had heard each joke before.

## Procedure

In Phase 1 of the session, participants evaluated 50 jokes using a 5-star rating scale (allowing half-star ratings). The 50 jokes were randomly selected from the pool of 100 and randomly ordered. These jokes were presented without any additional recommendations or information. The process of rating these initial jokes provided a guise of collecting data from which to derive personalized recommendations and aggregate user ratings. The process also allowed us to calculate preference estimations that we used as a control for individual differences in joke preferences in our analysis.

In Phase 2, the subjects received 45 jokes displayed with rating-based recommendations. The jokes were randomly selected from those not seen by that user in Phase 1. The recommendations (i.e., ratings) were all generated randomly, though presented to the subjects as personalized and/or aggregate recommendations. As a between-subjects manipulation, roughly a third of the subjects (Aggregate Only) received the recommendations as aggregate user ratings displayed as “Average user rating of this joke is: X (out of 5),” a third (Personalized Only) saw the display that “Our system thinks you would rate the joke as: X (out of 5),” and a third were given both recommendations. To control for order effects, we randomly assigned participants in the latter group into one of two between-subjects treatment groups. The first group received the purported aggregate rating above the personalized rating (Both-Aggregate First); the second group saw the reverse ordering (Both-Personalized First). Appendix A provides examples of the rating displays.

For experimental control, in actuality the recommendations for the 45 jokes in Phase 2 were generated randomly at one of three value levels: high, low, and medium. For the jokes given high ratings, the ratings were randomly generated values between 3.5 and 4.5 stars; the low values were randomly generated between 1.5 and 2.5 stars; and the medium values were randomly generated between 2.5 and 3.5 stars. We drew rating values from uniform distributions in order to increase the credibility (i.e., realism) of the presented recommendations. For example, if every high (low) recommendation was set at 4.5 (1.5) stars, the bimodal distribution would likely draw attention and undermine the treatments. The high-low comparison is the test of bias in this setting, the central dependent variable of interest. This measure has been used in prior research (Adomavicius et al. 2018; Adomavicius et al. 2019; Tversky and Kahneman 1974). If there is no biasing effect, the ratings of participants should not differ because of the presented recommendation values. If a significant difference between the ratings of participants manifests for jokes displayed with high and low recommendation ratings, it will indicate that their preferences have been affected by the displayed ratings. The medium value ratings are included so that the presented ratings cover the entire spectrum of the 1–5 rating scale, helping to provide better credibility as well. We do not use the medium ratings in subsequent analyses in the paper.

For the single recommendation groups (Aggregate Only and Personalized Only), the 45 jokes were distributed into 3 within-subjects joke groups varying the magnitude of the random recommendation: 20 high, 20 low, and 5 medium. For the “Both” groups (Aggregate First and Personalized First), the 45 jokes were randomly assigned into five conditions. Forty of the jokes occupied a 2 × 2 within-subjects design crossing high and low values of personalized and aggregate recommendations: 10 jokes were assigned to the HighP-HighA condition that consisted of high values for both personalized and aggregate ratings; 10 jokes to the LowP-LowA condition that consisted of low values for both ratings; 10 jokes to the LowP-HighA condition with low personalized and high aggregate ratings; and 10 jokes to the reversed HighP-LowA condition. The remaining five jokes were in a MediumP-MediumA condition, included to provide a credible representation of ratings across the entire spectrum of the 1–5 rating scale.

Finally, in Phase 3, users completed a survey that collected demographic and other individual information for use in the analyses (see Table 1 and the control variables used in Table 2).

## Independent Presentation

The average user preference ratings for the high and low treatments and the pairwise t-test comparisons for the treatments are illustrated by Figure 1. Both aggregate user ratings and personalized predicted ratings generate substantial biases in post-consumption preference ratings (high-low difference of more than a half-star on average, overall), even though the two types of recommendation represent very different information. We also note that the two low conditions (personalized vs. aggregate) do not significantly differ, and neither do the two high conditions. Thus, there is no evidence that aggregate and personalized ratings, when presented individually, generate different levels of preference bias, contrary to H1.

As a more comprehensive test of H1, we employed regression analysis. The repeated-measures design of the experiment, wherein each participant was exposed to both high and low ratings in a random fashion, allows us to model the relationship between shown ratings (either personalized or aggregate) and user’s submitted post-experience preference ratings while controlling for participant differences. The random effects GLS model<sup>6</sup> using robust standard errors, clustered by participant, and using participant-level controls is (Model 4 in Table 2):

$$
\begin{array}{l} \text {UserRating} _ {i j} = b _ {0} + b _ {1} \text {High} _ {i j} + b _ {2} \text {PredictionGp} _ {i j} + \\ b _ {3} (\text {PredictionGp} _ {i j} \times \text {High} _ {i j}) + b _ {4} \text {Controls} _ {i j} + u _ {i} + \varepsilon_ {i j} \end{array}\tag{1}
$$

The study utilized a repeated-measures design with a balanced number of observations on each participant. To control for participant-level heterogeneity, the composite error term $( u _ { i }$ $+ \ \varepsilon _ { i j } )$ includes the individual participant effect $u _ { i }$ and the standard disturbance term $\varepsilon _ { i j } .$ UserRating is the submitted post-experience rating for participant i on joke j. $H i g h _ { i j }$ is a binary variable that indicates whether the shown rating for participant i on joke j is a high or low artificial rating. To the extent that users are influenced by the observed information, their submitted preference ratings will be shifted up when seeing high ratings and shifted down when seeing low ratings (manipulated within-subjects). Thus, the high/low difference captured by the coefficient on $H i g h _ { i j }$ is an indicator of the bias created. PredictionGp, is a binary variable, taking the value

## Results

The first subsection reports the results for the single recommendation treatments, testing H1. The following subsections address the effects of simultaneous recommendations related to H2 and H3.

Table 2. Regression Analyses for Comparing the Two Single Recommendation Treatment Groups

<table><tr><td>DV: UserRating</td><td>Model 1:(main effects only)</td><td>Model 2:(main effects only)</td><td>Model 3:(with interaction)</td><td>Model 4:(with interaction)</td></tr><tr><td></td><td>Coefficient (SE)</td><td>Coefficient (SE)</td><td>Coefficient (SE)</td><td>Coefficient (SE)</td></tr><tr><td>High</td><td>0.637 (0.046)***</td><td>0.634 (0.046)***</td><td>0.720 (0.064)***</td><td>0.717 (0.06)***</td></tr><tr><td>PredictionGp</td><td>-0.023 (0.083)</td><td>-0.013 (0.079)</td><td>0.060 (0.091)</td><td>0.051 (0.091)</td></tr><tr><td>PredictionGp × High</td><td></td><td></td><td>-0.166 (0.091)†</td><td>-0.165 (0.091)†</td></tr><tr><td>Control</td><td></td><td></td><td></td><td></td></tr><tr><td>RatingDev</td><td></td><td>0.352 (0.044)***</td><td></td><td>0.351 (0.044)***</td></tr><tr><td>ifSeenJokeBefore</td><td></td><td>-0.064 (0.041)</td><td></td><td>-0.064 (0.041)</td></tr><tr><td>jokeFunniness</td><td></td><td>0.903 (0.062)***</td><td></td><td>0.903 (0.062)***</td></tr><tr><td>Age</td><td></td><td>-0.012 (0.005)*</td><td></td><td>-0.012 (0.005)**</td></tr><tr><td>Male</td><td></td><td>0.144 (0.09)</td><td></td><td>0.144 (0.09)</td></tr><tr><td>Undergrad</td><td></td><td>-0.146 (0.1)</td><td></td><td>-0.146 (0.1)</td></tr><tr><td>Native</td><td></td><td>-0.125 (0.084)</td><td></td><td>-0.125 (0.084)</td></tr><tr><td>Constant</td><td>2.564 (0.072)***</td><td>0.006 (0.265)</td><td>2.522 (0.076)***</td><td>-0.037 (0.2465)</td></tr><tr><td>N</td><td>118</td><td>118</td><td>118</td><td>118</td></tr><tr><td>R2 within-subject</td><td>.1178</td><td>.2070</td><td>.1198</td><td>.2089</td></tr><tr><td>R2 between-subject</td><td>.0007</td><td>.0943</td><td>.0007</td><td>.0943</td></tr><tr><td>R2 overall</td><td>.0955</td><td>.1852</td><td>.0971</td><td>.1868</td></tr><tr><td>X2</td><td>194.88, p &lt; .0001</td><td>578.74, p &lt; .0001</td><td>204.51, p &lt; .0001</td><td>622.58, p &lt; .0001</td></tr></table>

\*\*\*p < .001; \*\*p < .01; \*p < .05; <sup>†</sup>p < 0.10.

Pairwise t-test comparisons of mean user preference ratings:  
![](/api/attachments/JU7R533C/fulltext/images/d69495ef024a35dde6da56400715bee47a0bbb6c49780b9aafe0a50af5633770.jpg)

$$
^ {* * *} p <  . 0 0 1; [ - - ] p >. 1 0
$$

Note: All tests are one-tailed except for the tests represented by the horizontal lines in the figure. Unlike the others, these tests have no prior hypothesized direction, so two-tailed tests are performed. Also, all tests are unpaired t-tests except for the tests represented by the vertical lines in the figure. These are within-subject comparisons and are done using pairwise t-tests.

Figure 1. Mean (Standard Deviation) of Self-Reported Ratings after Observing Either High or Low Aggregate Ratings or Personalized Predictions, Single Recommendation Conditions

1 if the response is from a participant receiving personalized predictions and 0 if receiving aggregate ratings. Thus, the interaction term PredictionGp × High provides a direct test of Hypothesis 1. A significant interaction effect would support a difference in bias between the two types of ratings. The variables in the vector Controls are described in Appendix B. In Table 2, Models 1 and 3 only include independent variables, and Models 2 and 4 include control variables.

As observed in Table 2, the data substantiate a significant bias, as indicated by the High variable in both models. However, neither the main effect (PredictionGp in Models 1 and 2) nor the interaction effect (PredictionGp×High in Models 3 and 4) attain traditional levels of significance. In addition, the marginally significant interaction terms in Models 3 (b = $- 0 . 1 6 6 , p = 0 . 0 7 )$ and 4 $( b = - 0 . 1 6 5 , p = 0 . 0 7 )$ ) are opposite to what is predicted by Hypothesis 1. The marginal possibility of concluding a reverse relationship to that expressed in Hypothesis 1 can be checked for Hypothesis 2 within the joint presentation of aggregate and personalized ratings in the next section. If the pattern were established there, then Hypothesis 1 would need further study. However, based on the analysis of recommendations provided singly, Hypothesis 1 is not supported. When presented alone, both recommendations bias the user ratings at levels that are largely comparable in magnitude, despite their different underlying mechanisms.

## Joint Presentation: Relative Magnitude

In some instances, retailers can or do provide both pieces of information (personalized predicted and aggregate ratings) as aids to the consumer. We begin with Hypothesis 2 regarding the relative effect sizes for the two types of ratings when seen together.

Figure 2 illustrates the t-test comparisons for treatment groups when aggregate ratings are shown first (Figure 2a) and when personalized ratings are shown first (Figure 2b). Starting with the vertical line in each diagram, we see a significant difference between HighP–HighA (when both ratings are high) vs. LowP–LowA (when both ratings are low), indicating a clear bias effect with simultaneous presentation, which is consistent with our results for single recommendations.

Relevant to Hypothesis 2, the horizontal line in each figure indicates a stronger impact of personalized predicted ratings compared to aggregate user ratings when both appear together and signal in opposite directions (one with a high recommendation and the other low). Thus, when both types of ratings are present and conflict, personalized recommendations seem to impact users more strongly (generating greater bias) than aggregate ratings regardless of the presentation order.

The diagonal lines in Figure 2 also support this pattern. Beginning with the negatively sloped diagonals in the figures, when the aggregate rating goes from low to high, holding the valence of the personalized prediction fixed, the effect is variable. In each case, one of the comparisons is statistically significant, and the other is not. In contrast, from the comparisons indicated by the positively sloped diagonals in the figure, when the personalized prediction goes from low to high, holding the valence of the aggregate ratings fixed, we always see a clear, consistent, statistically significant biasing effect.

To test across conditions and to control for possible confounding factors, we conduct regression analyses, applying a similar random effects GLS model using robust standard errors, clustered by participant, and using participant-level controls:

$$
\begin{array}{c} \text {UserRating} _ {i j} = b _ {0} + b _ {1} \text {HighAggregate} _ {i j} + \\ b _ {2} \text {HighPersonalized} _ {i j} + b _ {3} \text {HighAggregate} _ {i j} \times \\ \text {HighPersonalized} _ {i j} + b _ {4} \text {Order} _ {i} + b _ {5} \text {Controls} _ {i j} + u _ {i} + \varepsilon_ {i j} \end{array}\tag{2}
$$

In the model, UserRating is as defined in Equation 1. All participants in the two “Both” treatment groups saw both an aggregate and personalized rating for each joke. The order effect variable Order captures whether the aggregate or personalized rating was shown above the other (consistent within participant), and the variables in Controls<sub>ij</sub> are described in Appendix B. HighAggregate<sub>ij</sub> and HighPersonalized are binary variables that indicate whether the shown aggregate user rating and personalized predicted rating for participant i on joke j had a high or low value, respectively. The relative magnitudes of the coefficients for these variables indicate the relative strength of the main effects of the two types of recommendation, but now in the situation with combined recommendations (Hypothesis 2).

Table 3 indicates that both of the main effects are significant (i.e., HighAggregate and HighPersonalized ) and the interaction is insignificant. Each type of rating introduces bias into users’ reported preference when shown together. Showing both high aggregate and personalized ratings at the same time does not strengthen (compound) each other’s effects. This is regardless of order; that is, the presentation order of aggregate and personalized ratings did not influence the magnitude of bias in users’ post-consumption preference ratings, based on the non-significance of the main order effect and interaction terms in the model.

![](/api/attachments/JU7R533C/fulltext/images/7a1a2e8b61c0f660f4a2d7feb3bd789c611b6b30f843497113bc88f9d5faff66.jpg)

![](/api/attachments/JU7R533C/fulltext/images/060cb8293916ebb22f4284b2621553014c05e40b16e67e3f568cbcd619c0e26e.jpg)  
Note: All tests are one-tailed except for the tests represented by the horizontal lines in the figure. Unlike the others, these tests have no prior hypothesized direction, so two-tailed tests are performed.

Figure 2. Pairwise Comparisons of Mean User Preference Ratings When Both Personalized and Aggregate Ratings Were Displayed

For Hypothesis 2, we compare the relative magnitudes of the two effects, for HighAggregate and HighPersonalized. When the two recommendations are shown together, personalized predicted ratings have a greater impact, inducing larger bias than aggregate user ratings $( \chi ^ { 2 } = 5 . 4 3 , p < 0 . 0 1 )$ This is consistent with the patterns discussed in Figure 2. When the two ratings appear together, the personalized predicted ratings have a greater impact, leading to a greater bias in postexperience user preference ratings. This is different from the single-recommendation results reported in Table 2, where we observed that, when presented alone, personalized ratings are not indicated as having a stronger impact than aggregate ratings (Hypothesis 1 not supported).

## Joint Presentation: Combined Effect

Turning to Hypothesis 3, we consider the joint impact of the two recommendation types when shown together. By comparing Figures 1 and 2, the high vs. low effect magnitudes are in the range 0.55-0.72 when ratings are displayed individually, and in the range 0.55–0.6 when displayed together. In other words, the cumulative effect of both ratings is not significantly greater than the effect of either rating individually, suggesting a substitutive relationship.

As a direct test of Hypothesis 3, we compare the observations for which either recommendation type is received alone to the cases with both high personalized and high aggregate ratings (i.e., HighP–HighA) and both low personalized and low aggregate ratings (i.e., LowP–LowA). We fit two models with these data and analyze each separately (see Table 4). Models 7 and 8 compare the aggregate ratings alone to the responses with both recommendations, and Models 9 and 10 compare the personalized ratings alone to the responses with both recommendations. In each case, the random-effects GLS model using robust standard errors, clustered by participant, and using participant-level controls represents our model for the analysis:

<table><tr><td>DV: UserRating</td><td>Model 5:(no controls)</td><td>Model 6:(with controls)</td></tr><tr><td></td><td>Coefficient (SE)</td><td>Coefficient (SE)</td></tr><tr><td>HighAggregate</td><td>0.219 (0.073)*</td><td>0.271 (0.073)***</td></tr><tr><td>HighPersonalized</td><td>0.43 (0.085)***</td><td>0.472 (0.085)***</td></tr><tr><td>HighAggregate × HighPersonalized</td><td>-0.049 (0.08)</td><td>-0.108 (0.074)</td></tr><tr><td>Order Effects</td><td></td><td></td></tr><tr><td>PersonalizedFirst</td><td>0.117 (0.131)</td><td>0.119 (0.134)</td></tr><tr><td>PersonalizedFirst × HighAggregate</td><td>0.0002 (0.103)</td><td>0.021 (0.102)</td></tr><tr><td>PersonalizedFirst × HighPersonalized</td><td>-0.057 (0.11)</td><td>-0.07 (0.106)</td></tr><tr><td>Control</td><td></td><td></td></tr><tr><td>AggregateDev</td><td></td><td>0.194 (0.056)***</td></tr><tr><td>PersonalizedDev</td><td></td><td>0.084 (0.064)</td></tr><tr><td>ifSeenJokeBefore</td><td></td><td>0.007 (0.004)</td></tr><tr><td>jokeFunniness</td><td></td><td>0.088 (0.112)</td></tr><tr><td>Age</td><td></td><td>-0.055 (0.112)</td></tr><tr><td>Male</td><td></td><td>-0.141 (0.12)</td></tr><tr><td>Undergrad</td><td></td><td>-0.802 (0.341)*</td></tr><tr><td>Native</td><td></td><td>0.271 (0.073)***</td></tr><tr><td>Constant</td><td>2.593 (0.091)***</td><td>0.271 (0.073)***</td></tr><tr><td>N</td><td>55</td><td>55</td></tr><tr><td> $R^2$  within-subject</td><td>.0505</td><td>.1492</td></tr><tr><td> $R^2$  between-subject</td><td>.0127</td><td>.1033</td></tr><tr><td> $R^2$  overall</td><td>.045</td><td>.1423</td></tr><tr><td> $X^2$ </td><td>52.19, p&lt;.0001</td><td>280.59, p&lt;.0001</td></tr></table>

\*\*\*p < .001; \*\*p < .01; \*p < .05; <sup>†</sup>p < 0.10

$$
\begin{array}{l} \text {UserRating} _ {i j} = b _ {0} + b _ {1} (H i g h _ {i j}) + b _ {2} (G r o u p _ {i}) + \\ b _ {3} (H i g h _ {i j} \times G r o u p _ {i}) + b _ {4} (C o n t r o l s _ {i j}) + u _ {i} + \varepsilon_ {i j} \end{array}\tag{3}
$$

The variables UserRating and $H i g h _ { i j }$ are as defined in Equation 1 for participant i on joke j. The Controls are described in Appendix B. Group denotes different betweensubject conditions varying information displays. The main effects of Group represent the mean differences in user ratings between the baseline group (i.e., AggregateOnly) and the two order conditions when Both recommendations are shown (i.e., AggregateFirst and PersonalizedFirst), when Low information is displayed. The interaction term (i.e., $H i g h _ { i j } \times G r o u p _ { i } )$ examines whether the effect size of showing high vs. low information differs between treatment and baseline groups beyond the High effect. For example, High × AggregateFirst represents the effect of showing high information in the combined ratings AggregateFirst condition compared with showing low information in the baseline AggregateOnly condition beyond the High effect, that is, the added effect of the combined information. Models 9 and 10 have a similar setup as Models 7 and 8, respectively, only that the AggregateOnly condition is replaced by the PersonalizedOnly condition.

Table 4 summarizes the regression results. First, the statistically significant effect of the High variable in both models corroborates the existence of bias (high-low difference) generally, as noted in earlier analyses. Interestingly, in both models, there is no evidence that adding a second rating (either personalized or aggregate) increases the bias. None of the Group main effects nor the High\*Group interaction terms are statistically significant. Thus, the effect of a second recommendation is not additive, as stated by Hypothesis 3, but rather substitutive.

Table 4. Regression Analyses Comparing Single and Both Recommendation Conditions

<table><tr><td>DV: UserRating</td><td>Model 7: AggregateOnly and Both</td><td>Model 8: AggregateOnly and Both</td><td>Model 9: PersonalizedOnly and Both</td><td>Model 10: PersonalizedOnly and Both</td></tr><tr><td></td><td>Coefficient (SE)</td><td>Coefficient (SE)</td><td>Coefficient (SE)</td><td>Coefficient (SE)</td></tr><tr><td>High</td><td>0.720 (0.064)***</td><td>0.717 (0.060)***</td><td>0.555 (0.0655)***</td><td>0.551 (0.068)***</td></tr><tr><td>Group</td><td></td><td></td><td></td><td></td></tr><tr><td>Baseline:</td><td></td><td>AggregateOnly</td><td></td><td>PersonalizedOnly</td></tr><tr><td>AggregateFirst</td><td>0.020 (0.120)</td><td>0.005 (0.123)</td><td>-0.040 (0.106)</td><td>-0.02 (0.108)</td></tr><tr><td>PersonalizedFirst</td><td> $0.236 (0.132)^{\dagger}$ </td><td>0.198 (0.103)</td><td>0.177 (0.120)</td><td>0.168 (0.122)</td></tr><tr><td>High × Group</td><td></td><td></td><td></td><td></td></tr><tr><td>High × AggregateFirst</td><td>-0.120 (0.140)</td><td>-0.08 (0.138)</td><td>0.045 (0.141)</td><td>0.07 (0.142)</td></tr><tr><td>High × PersonalizedFirst</td><td>-0.177 (0.139)</td><td>-0.13 (0.137)</td><td>-0.012 (0.140)</td><td>0.023 (0.141)</td></tr><tr><td>Control</td><td></td><td></td><td></td><td></td></tr><tr><td>AggregateDeviation</td><td></td><td>0.251 (0.048)***</td><td></td><td></td></tr><tr><td>PersonalizedDeviation</td><td></td><td></td><td></td><td>0.262 (0.056)***</td></tr><tr><td>ifSeenJokeBefore</td><td></td><td>-0.077 (0.054)</td><td></td><td>-0.109 (0.047)*</td></tr><tr><td>jokeFunniness</td><td></td><td>0.997 (0.069)***</td><td></td><td>0.856 (0.075)***</td></tr><tr><td>Age</td><td></td><td>-0.002 (0.006)</td><td></td><td>-0.0002 (0.004)</td></tr><tr><td>Male</td><td></td><td>0.088 (0.102)</td><td></td><td>0.149 (0.074)*</td></tr><tr><td>Undergrad</td><td></td><td>-0.032 (0.109)</td><td></td><td>-0.102 (0.079)</td></tr><tr><td>Native</td><td></td><td>-0.091 (0.102)</td><td></td><td>-0.228 (0.074)**</td></tr><tr><td>Constant</td><td>2.522 (-0.076)***</td><td>-0.619 (0.311)*</td><td>2.582 (0.0511)***</td><td>0.291 (0.268)</td></tr><tr><td>N</td><td>114</td><td>114</td><td>114</td><td>114</td></tr><tr><td> $R^2$  within-subject</td><td>0.1256</td><td>.2205</td><td>0.0923</td><td>.1690</td></tr><tr><td> $R^2$  between-subject</td><td>0.0216</td><td>.0264</td><td>0.0338</td><td>.1833</td></tr><tr><td> $R^2$  overall</td><td>0.1021</td><td>.1762</td><td>0.0816</td><td>.1764</td></tr><tr><td> $X^2$ </td><td></td><td>547.85, p &lt; .0001</td><td></td><td>385.05, p &lt; .0001</td></tr></table>

\*\*\*p < .001; \*\*p < .01; \*p < .05; <sup>†</sup>p < 0.10

## General Discussion

The use of both aggregate user ratings and personalized predicted ratings has become commonplace among online retailers. However, they also lead to a bias in post-experience ratings (even immediately following the experience), when such an effect is not expected nor desired. We study these effects within an experimental setting that allows us to compare these two forms of recommendation directly in a way that prior research has not done, despite that both forms of recommendation can be and are commonly used singly and together in actual practice. We observed an average increase in postexperience preference of approximately 0.5 to 0.7 stars on a 1-to-5 star rating scale (approximately 12.5 to 17.5%) when displaying high-valued ratings compared to low-valued ones, either of an aggregate or personalized form, singly or together.

Despite their different underlying theoretical mechanisms, aggregate and personalized ratings have effect sizes on postexperience bias that are not discernibly different in magnitude when presented singly. And, the overall effect on preference ratings does not increase when aggregate user ratings and personalized predicted ratings are presented together. Instead, there is a substitutional relationship between personalized predicted ratings and aggregate user ratings with regards to the biasing effect they have on consumer responses. Furthermore, personalized ratings appear to dominate when both types of recommendations are presented together.

## Implications

Our focus in this research is on the comparison of the postconsumption bias produced by aggregate and personalized ratings. The comparison is of significance because of the sharply different psychological mechanisms posited for these two forms of recommendation. Aggregate user ratings represent consensus judgments on item quality, involving social information promoting observational learning from others. Through observational learning, users watch others’ behaviors (i.e., other people’s ratings) and then later use the observed behaviors as a guide for their own behavior. Personalized predicted ratings represent individualistic information with little or no social meaning, but with preference meaning targeted to the users’ processes of information integration, as discussed in prior work.

Yet, when we presented these two types of information separately, we observed effects on post-experience preference ratings that did not significantly differ in magnitude. Presenting the two together, however, highlights the contrast in the information they convey: the personalized predicted ratings drove the results. The socially grounded aggregate information, with no clear tie to the users’ individual preferences, was arguably easier to discount and showed a substitutability of its biasing effect compared to the more personalized ratings. The observed dominance of the personalized information over the social information in creating preference bias represents an important nuance that has not yet been identified in prior research.

Our findings also have practical implications for online retailers, marketing managers, and system managers. Online retailers should consider the effects of displaying ratings and recommendations on consumer behavior, which may be positive or negative from the retailer’s perspective and may differ depending on what is displayed. When evaluating the costs and benefits associated with these systems, marketers must realize the important role of the displayed item ratings, either aggregate or personalized, as well as the manner in which recommendations can significantly distort a consumer’s response to an item.

Results like these can significantly influence the design of retail displays in the online space. Online consumers have come to expect review and rating information for products, and market research has suggested that the more reviews and ratings the better.<sup>7</sup> Given that the display of aggregate user ratings and personalized predicted ratings impact postexperience preferences, these effects may manifest in unexpected changes to the ratings and reviews that become the input to customer feedback management and recommender systems.

## Further Research

Our research opens up several directions for future research. First, we do not differentiate aggregate ratings based on friends’ vs. strangers’ ratings. It is possible that ratings provided by people with strong social ties can have higher impact on a consumer’s decision making than ratings from the general online population. Further research is needed to compare other socially based recommendations against the aggregate and personalized recommendations studied here. Generally, better understanding of the differing dynamics of personalized and aggregated recommendations is warranted.

Looking beyond, we can consider different forms of the presentation of recommendations. We focused on recommendations that are presented to users as numeric ratings on a 1–5 star scale. However, this is just one form of item recommendation. Another common form is to compile and display lists of top-N items to each user (e.g., most-recommended, best-selling, or highest-rated). Future research is needed to examine the impact of recommendations presented in listbased, non-rating forms on users’ preferences and economic behavior. For aggregate ratings, also, the presentation of the rating is also accompanied by the number of users whose ratings are being aggregated. This presentation aspect may warrant attention in its own right.

One also can extend the research beyond the joke stimuli used in this study. Although the post-experience biasing effects for personalized and aggregate ratings have been robust across a variety of settings, the current comparative examination has not been widely done. One interesting distinction that has shown differences in decision processing is between experiential goods (whose utility arises through a transitory experience, like a vacation) and material goods (whose utility arises from possession over time, like a computer) (Gallo et al. 2017). Exploring the generality of the results across different types of goods would be illustrative of the decision processes and their effects.

Finally, given the prevalence of recommendation biases stemming from both aggregate and personalized ratings (presented separately or together), the design of bias-aware (or bias-resistant) recommendation models constitutes an important direction for future research.

## References

Adomavicius, G., Bockstedt, J. C., Curley, S. P., and Zhang, J. 2013. “Do Recommender Systems Manipulate Consumer Preferences? A Study of Anchoring Effects,” Information Systems Research (24:4), pp. 956-975.

Adomavicius, G., Bockstedt, J. C., Curley, S. P., and Zhang, J. 2018. “Effects of Online Recommendations on Consumers’ Willingness to Pay,” Information Systems Research (29:1), pp. 84-102.

Adomavicius, G., Bockstedt, J. C., Curley, S. P., and Zhang, J. 2019. “Reducing Recommender Systems Biases: An Investigation of Rating Display Designs,” MIS Quarterly (43:4), pp. 1321-1341.

Adomavicius, G., and Tuzhilin, A. 2005. “Toward the Next Generation of Recommendation System: A Survey of the Stateof-the-Art and Possible Extensions,” IEEE Transactions on Knowledge and Data Engineering (17:6), pp. 734-749.

Amblee, N., and Bui, T. 2011. “Harnessing the Influence of Social Proof in Online Shopping: The Effect of Electronic Word of Mouth on Sales of Digital Microproducts,” International Journal of Electronic Commerce (16:2), pp. 91-114.

Ansari, A., Essegaier, S., and Kohli, R. 2000. “Internet Recommendation Systems,” Journal of Marketing Research (37:3), pp. 363-375.

Aral, S. 2014. “The Problem with Online Ratings,” MIT Sloan Management Review (55:2), pp. 47-52.

Benlian, A., Titah, R., and Hess, T. 2012. “Differential Effects of Provider Recommendations and Consumer Reviews in E-Commerce Transactions: An Experimental Study,” Journal of Management Information Systems (29:1), pp. 237-272.

Bodapati, A. V. 2008. “Recommendation Systems with Purchase Data,” Journal of Marketing Research (45:1), pp. 77-93.

Campbell, I. 2007. “Chi Squared and Fisher–Irwin Tests of Two by Two Tables with Small Sample Recommendations,” Statistics in Medicine (26:19), pp. 3661-3675.

Chevalier, J. A., and Mayzlin, D. 2006. “The Effect of Word of Mouth on Sales: Online Book Reviews,” Journal of Marketing Research (43:3), pp. 345-354.

Cosley, D., Lam, S., Albert, I., Konstan, J. A., and Riedl, J. 2003. “Is Seeing Believing? How Recommender Interfaces Affect Users’ Opinions,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, New York: ACM, pp. 585-592.

Duan, W., Gu, B., and Whinston, A. B. 2008. “The Dynamics of Online Word-of-Mouth and Product Sales—an Empirical Investigation of the Movie Industry,” Journal of Retailing (84:2), pp. 233-242.

Fleder, D., and Hosanagar, K. 2009. “Blockbuster Culture’s Next Rise or Fall: The Impact of Recommender Systems on Sales Diversity,” Management Science (55:5), pp. 697-712.

Gallo, I., Sood, S., Mann, T. C., and Gilovich, T. 2017. “The Heart and the Head: On Choosing Experiences Intuitively and Possessions Deliberatively,” Journal of Behavioral Decision Making (30:3), pp. 754-768.

Godinho de Matos, M., Ferreira, P., Smith, M. D., and Telang, R. 2016. “Culling the Herd: Using Real-World Randomized Experiments to Measure Social Bias with Known Costly Goods,” Management Science (62:9), pp. 2563-2580.

Goldberg, K., Roeder, T., Gupta, D., and Perkins, C. 2001. “Eigentaste: A Constant Time Collaborative Filtering Algorithm,” Information Retrieval (4:2), pp. 133-151.

Haselton, M. G., Nettle, D., and Andrews, P. W. 2015. “The Evolution of Cognitive Bias,” in The Handbook of Evolutionary Psychology (2<sup>nd</sup> ed.), D. M. Buss (ed.), New York: John Wiley & Sons, Inc., pp. 724-746.

Ho, Y.-C., Wu, J., and Tan, Y. 2017. “Disconfirmation Effect on Online Rating Behavior: A Structural Model,” Information Systems Research (28:3), pp. 626-642.

Hu, N., Koh, N. S., and Reddy, S. K. 2014. “Ratings Lead You to the Product, Reviews Help You Clinch It? The Mediating Role of Online Review Sentiments on Product Sales,” Decision Support Systems (57), pp. 42-53.

Kahneman, D. 2011. Thinking, Fast and Slow, New York: Farrar, Straus and Giroux.

Lee, Y.-J., Hosanagar, K., and Tan, Y. 2015. “Do I Follow My Friends or the Crowd? Information Cascades in Online Movie Ratings,” Management Science (61:9), pp. 2241-2258.

Moe, W. W., and Schweidel, D. A. 2012. “Online Product Opinions: Incidence, Evaluation, and Evolution,” Marketing Science (31:3), pp. 372-386.

Moe, W. W., and Trusov, M. 2011. “The Value of Social Dynamics in Online Product Ratings Forums,” Journal of Marketing Research (48:3), pp. 444-456.

Muchnik, L., Aral, S., and Taylor, S. J. 2013. “Social Influence Bias: A Randomized Experiment,” Science (341:6146), pp. 647-651.

Mussweiler, T., and Strack, F. 1999. “Hypothesis-Consistent Testing and Semantic Priming in the Anchoring Paradigm: A Selective Accessibility Model,” Journal of Experimental Social Psychology (35:2), pp. 136-164.

Ricci, F., Rokach, L., and Shapira, B. 2015. Recommender Systems Handbook (2<sup>nd</sup> ed.), New York: Springer.

Salganik, M. J., and Watts, D. J. 2008. “Leading the Herd Astray: An Experimental Study of Self-Fulfilling Prophecies in an Artificial Cultural Market,” Social Psychology Quarterly (74:4), pp. 338-355.

Schlosser, A. E. 2005. “Posting Versus Lurking: Communicating in a Multiple Audience Context,” Journal of Consumer Research (32:2), pp. 260- 265.

Schwartz, B. 2004. The Paradox of Choice: Why More Is Less, New York: Harper Collins.

Sridhar, S., and Srinivasan, R. 2012. “Social Influence Effects in Online Product Ratings,” Journal of Marketing (76:5), pp. 70-88.

Sun, M. 2012. “How Does the Variance of Product Ratings Matter?,” Management Science (58:4), pp. 696-707.

Surowiecki, J. 2004. The Wisdom of Crowds : Why the Many Are Smarter Than the Few and How Collective Wisdom Shapes Business, Economies, Societies, and Nations, New York: Doubleday.

Tucker, C., and Zhang, J. 2011. “How Does Popularity Information Affect Choices? A Field Experiment,” Management Science (57:5), pp. 828-842.

Tversky, A., and Kahneman, D. 1974. “Judgment under Uncertainty: Heuristics and Biases,” Science (185), pp. 1124-1131.

Tversky, A., Sattath, S., and Slovic, P. 1988. “Contingent Weighting in Judgement and Choice,” Psychological Review (95:3), pp. 371-384.

Wu, J., and Gaytán, E. A. A. 2013. “The Role of Online Seller Reviews and Product Price on Buyers’ Willingness-to-Pay: A Risk Perspective,” European Journal of Information Systems (22:4), pp. 416-433.

Zhu, F., and Zhang, X. 2010. “Impact of Online Consumer Reviews on Sales: The Moderating Role of Product and Consumer Characteristics,” Journal of Marketing (74:2), pp. 133-148.

## About the Authors

Gediminas Adomavicius is a professor of Information and Decision Sciences at the University of Minnesota, where he also holds the Larson Endowed Chair for Excellence in Business Education. He received his Ph.D. in Computer Science from New York University. His research interests include recommender systems, machine learning, and electronic market mechanisms. His work has been published in leading Information Systems and Computer Science journals. He received the NSF CAREER Award for his research on recommender systems, has served as senior editor for Information

Systems Research and MIS Quarterly, and is a Distinguished Fellow of the INFORMS Information Systems Society.

Jesse Bockstedt is a professor of Information Systems and Operations Management in the Goizueta Business School at Emory University. He received his Ph.D. in business administration with a focus on Information Systems from the University of Minnesota. He studies user behavior and economic issues in environments that rely on information technology. His research has appeared in a variety of journals, including Information Systems Research, MIS Quarterly, Journal of MIS, Journal of Operations Management, and Production and Operations Management.

Shawn P. Curley is a professor of Information and Decision Sciences at the Carlson School of Management, University of Minnesota. He received his Ph.D. in Psychology from the University of Michigan. His research interests are in behavioral decision theory and include user behavior with recommender systems and user acceptance of complex auction mechanisms. Recent research outlets include Information Systems Research, Management Science, MIS Quarterly, and Journal of Operations Management.

Jingjing Zhang is an associate professor of Operations and Decision Technologies at the Kelley School of Business, Indiana University. She received her Ph.D. in business administration with an Information Systems concentration from the University of Minnesota. Her research interests include personalization techniques, recommender systems, and human-computer interactions. Her research has appeared in journals including MIS Quarterly, Information Systems Research, INFORMS Journal on Computing, IEEE Transactions on Knowledge and Data Engineering, and ACM Transactions on Information Systems.

## Appendix A

Example Rating Displays for Each Experimental Condition  
![](/api/attachments/JU7R533C/fulltext/images/32823c2b6ac2d94df9738643e7fd195d7d04bb7228343b97217b10ddc364429c.jpg)

Figure A1. Example Rating Displays in Which Only Personalized Ratings Was Shown

<table><tr><td>Treatment Group</td><td>Example Rating Displays and Post-Experience Preference Collection</td></tr><tr><td>AggregateOnly</td><td>Average user rating of this joke is: ★★★★☆ 1.9 (out of 5)</td></tr><tr><td>PersonalizedOnly</td><td>Our system thanks you would rate the joke as: ★★★★☆ 3.2 (out of 5)</td></tr><tr><td>Both-AggregateFirst</td><td>Average user rating of this joke is: ★★★★☆ 4.5 (out of 5) Our system thanks you would rate the joke as: ★★★★☆ 1.5 (out of 5)</td></tr><tr><td>Both-PersonalizedFirst</td><td>Our system thanks you would rate the joke as: ★★★★☆ 1.9 (out of 5) Average user rating of this joke is: ★★★★☆ 1.8 (out of 5)</td></tr></table>

## Appendix B

## Control Variables Used in the Regression Analyses

<table><tr><td colspan="2">Table B1. Control Variables Used in Regression Analyses</td></tr><tr><td>Variable Name</td><td>Description</td></tr><tr><td>ifSeenJokeBefore</td><td>Whether the participants indicated they had seen the joke before (yes/no binary)</td></tr><tr><td>jokeFunniness</td><td>Average joke rating in the Jester dataset (continuous between 1 and 5)</td></tr><tr><td>Age</td><td>Participant age (integer)</td></tr><tr><td>Male</td><td>Sex (male/female binary)</td></tr><tr><td>Undergrad</td><td>School level (undergrad, yes/no binary)</td></tr><tr><td>native</td><td>Whether they are native speakers of English (yes/no binary).</td></tr><tr><td>RatingDev</td><td>A derived variable that captures the deviation (i.e., difference) between the shown rating (i.e., the personalized or aggregate rating) and the expected value for the rating in the corresponding condition. I.e., expected value for the rating is:= 4 for High rating values (generated uniformly at random from [3.5, 4.5]);= 2 for Low rating values (generated uniformly at random from [1.5, 2.5]).This variable controls for the small deviations in shown ratings that arise from using uniform distributions to generate the shown ratings.</td></tr><tr><td>AggregateDev</td><td>A derived variable that captures the deviation between the shown aggregate rating and the expected value for the rating. Same logic as for RatingDev.</td></tr><tr><td>PersonalizedDev</td><td>A derived variable that captures the deviation between the shown personalized rating and the expected value for the rating. Same logic as for RatingDev.</td></tr><tr><td>PersonalizedFirst</td><td>Binary variable capturing the between-subjects order factor:= 1 if the personalized rating appeared first= 0 if the aggregate rating was shown firstThis variable along with its associated interaction terms provide a check for any order effects in presenting the two types of rating.</td></tr></table>
