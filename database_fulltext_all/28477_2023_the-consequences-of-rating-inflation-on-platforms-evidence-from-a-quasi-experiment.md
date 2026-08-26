---
otero_id: 28477
otero_key: "57YWUSQX"
title: "The Consequences of Rating Inflation on Platforms: Evidence from a Quasi-Experiment"
authors: "Arslan Aziz; Hui Li; Rahul Telang"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1134"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Consequences of Rating Inflation on Platforms: Evidence from a Quasi-Experiment

Arslan Aziz,<sup>a,</sup>\* Hui Li,<sup>b</sup> Rahul Telang<sup>c</sup>

<sup>a</sup> Sauder School of Business, The University of British Columbia, Vancouver, British Columbia V6T 1Z2, Canada; <sup>b</sup> HKU Business School, The University of Hong Kong, Hong Kong; <sup>c</sup>Heinz College of Information Systems and Public Policy, Carnegie Mellon University, Pittsburgh Pennsylvania 15213 \*Corresponding author

Contact: arslan.aziz@sauder.ubc.ca, https://orcid.org/0000-0003-3257-7130 (AA); huil1@hku.hk, https://orcid.org/0000-0003-0914-8098 (HL); rtelang@andrew.cmu.edu (RT)

Received: January 26, 2020 Revised: November 10, 2020; September 28, 2021; March 4, 2022 Accepted: March 25, 2022 Published Online in Articles in Advance: June 10, 2022

https://doi.org/10.1287/isre.2022.1134

Copyright: © 2022 INFORMS

Abstract. Informative online ratings enable digital platforms to reduce the search cost for buyers to <sup>fi</sup>nd good sellers. However, rating in<sup>fl</sup>ation, a phenomenon in which average rating increases and rating variance across listings decreases, threatens the informativeness of ratings. We empirically identify the consequences of rating in<sup>fl</sup>ation by conducting a quasi-experiment with a digital platform that exogenously changed its rating display rule in a treated neighborhood, which resulted in rating in<sup>fl</sup>ation. Using a differences-in-differences approach, we <sup>fi</sup>nd that platforms bene<sup>fi</sup>t from one aspect of rating in<sup>fl</sup>ation: user purchases and seller sales increase because of the increased average rating. However, they also face negative consequences: rating in<sup>fl</sup>ation causes a decrease in user trial and a greater concentration of sales among popular restaurants. Overall, our results illustrate the potential consequences of rating in<sup>fl</sup>ation that platforms need to consider when designing and managing their rating system.

History: Xiaoquan (Michael) Zhang, Senior Editor; Gordon Burtch, Associate Editor. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2022.1134.

Keywords: rating in<sup>fl</sup>ation <sub>•</sub> online marketplace <sub>•</sub> quasi-experiment <sub>•</sub> economics of IS

## 1. Introduction

Online ratings and reviews are pervasive and in<sup>fl</sup>uential; more than four of <sup>fi</sup>ve U.S. adults consult online ratings and reviews before making purchases (Center 2016). Online ratings reduce the cost of searching for highquality products and improve product <sup>fi</sup>t (Hong and Pavlou 2014) by allowing consumers to learn from other consumer’s past experiences (Duan et al. 2008a, Tadelis 2016). The effectiveness of such social learning depends on the informativeness of online ratings. In this paper, we investigate how a threat to rating informativeness (rating in<sup>fl</sup>ation) impacts platforms and their users.

Rating in<sup>fl</sup>ation manifests as a combination of high ratings and a low rating variance across sellers. For instance, on eBay, the median seller has a 100% positive rating and the bottom 10th percentile seller has a 98% positive rating (Nosko and Tadelis 2015). Not only are these exceptionally high positive ratings, but more importantly, there is very little variation between good and mediocre sellers, making these ratings less informative for consumers. One of the earliest works discussing the possibility of in<sup>fl</sup>ated ratings was in the information systems (IS) literature and identi<sup>fi</sup>ed selfselection as a possible mechanism (Li and Hitt 2008). Such rating in<sup>fl</sup>ation is common; it has been observed across a variety of digital marketplaces such as online labor markets (Filippas et al. 2022), e-commerce platforms (Nosko and Tadelis 2015), and sharing economy platforms (Zervas et al. 2021). In some settings, rating averages decrease with time (Li and Hitt 2008, Godes and Silva 2012, Dai et al. 2018). However, although rating averages may increase or decrease, in this paper, we focus on an important associated phenomenon: the decrease in rating variance across sellers on the platform. Such a decrease in rating variance results in more sellers having identical or similar ratings, making ratings less informative. This can have an impact on the likelihood of users trying a seller for the <sup>fi</sup>rst time, which we de<sup>fi</sup>ne as trial, and which in turn may affect the sales concentration across sellers.

Despite the importance of examining the impact of rating in<sup>fl</sup>ation, empirical evidence is limited. A major reason is that quantifying the consequences of rating in<sup>fl</sup>ation is challenging. Observational data are not suitable because rating in<sup>fl</sup>ation often manifests gradually over time, making it dif<sup>fi</sup>cult to eliminate all other unobservable temporal confounds, such as improvements in quality, that also in<sup>fl</sup>uence consumer choices. Recent IS studies have used randomized experiments or natural experiments to investigate the motivations, mechanisms, and impact of user gener ated content in a variety of settings (Burtch et al. 2018;

Huang et al. 2019a, b; Shukla et al. 2021). In our context, a randomized experiment is not feasible because it would pose a risk to the platform’s credibility with both sellers and users if ratings were randomly altered. Randomization would also violate the stable unit treatment value assumption (SUTVA) required for identi<sup>fi</sup>cation, because randomly assigning sellers to treatment and control groups would result in the same customer viewing both treated and control sellers affecting each other’s outcomes. A natural experiment is also not ideal because they usually do not withhold a control group from being treated that can be used to control for temporal confounds.

In this paper, we conduct a quasi-experiment to empirically examine the impact of rating in<sup>fl</sup>ation on user purchases, trial, and sales concentration in the context of choosing restaurants on a food delivery platform. We overcome the identi<sup>fi</sup>cation challenges discussed previously by designing and running an experiment with a food delivery platform that induced a rating in<sup>fl</sup>ation shock for a treated geographic region while keeping ratings unchanged in other regions. To prevent the treated users from being exposed to both treated and untreated restaurants at the same time, we selected the treated restaurants from a geographically contiguous region that is relatively isolated from the rest of the city.

The experiment and the transaction-level data provide us a unique opportunity to study the consequences of rating in<sup>fl</sup>ation on users, restaurants, and the platform. We use the differences-in-differences approach to estimate the effect of rating in<sup>fl</sup>ation and its impact on user purchases, trial, and sales concentration. The geographical selection of the treated group may lead to the presence of systematic differences in the characteristics of treated and control users and restaurants. We validate our results by checking for pre-experiment parallel trends and running robustness checks using randomization inference and synthetic controls.

Rating in<sup>fl</sup>ation is composed of an increase in the rating of the average seller and a decrease in the rating variance across sellers. The increase in average ratings is likely to increase purchases. However, the impact of the decrease in rating variance can be more nuanced. The decrease in rating variance may increase both the risk and the reward of trial. The risk increases because rating in<sup>fl</sup>ation makes ratings a less informative signal of restaurant quality and increases the uncertainty associated with trial. The reward increases because when ratings are less informative, users rely more on trial to learn about restaurant quality. We empirically investigate whether risk or reward dominates by estimating whether trial decreases or increases using the differences-in-differences method with data generated from the experiment. In addition, because of rating in<sup>fl</sup>ation, users rely more on their prior beliefs and experiences in choosing restaurants. They are thus more likely to purchase from more popular restaurants for which they have such signals, resulting in an increase in sales concentration.

We <sup>fi</sup>nd that, although platforms bene<sup>fi</sup>t from one aspect of rating in<sup>fl</sup>ation (the increase in mean rating) through increased purchases, they may face negative consequences from the other (the decrease in rating variance) through reduced trial and increased sales concentration. The increase in trial risk dominates the increase in trial reward so that consumer trial de creases because of rating in<sup>fl</sup>ation. At the same time, rating in<sup>fl</sup>ation concentrates sales toward more popular restaurants, increasing such restaurants’ market power relative to the platform. Thus, rating in<sup>fl</sup>ation makes consumers less willing to try new restaurants and con<sup>fi</sup>ne themselves to more popular restaurants.

Our <sup>fi</sup>ndings have important managerial implications on rating system design and platform management. We <sup>fi</sup>nd that, although rating in<sup>fl</sup>ation makes sellers appear of higher quality and may boost total purchases, it can potentially hurt the platform’s long term growth in two ways: it can discourage consumers from trying new sellers, and it may increase the market power of popular restaurants. Overall, our results illustrate the consequences and tradeoffs of rating in<sup>fl</sup>ation, which can be helpful for platforms when designing and managing their rating system.

## 2. Related Literature

Our study relates to the stream of IS literature that has examined the factors in<sup>fl</sup>uencing the creation of usergenerated content. Online reviews have been shown to have a role in reducing product <sup>fi</sup>t uncertainty (Hong and Pavlou 2014), and the difference between expectations and actual experience has been shown to affect user’s rating decisions (Ho et al. 2017). Similarity of personality traits have been shown to increase the in<sup>fl</sup>uence of word-of-mouth on consumers (Adamopoulos et al. 2018).

Our work relates methodologically to the stream of IS literature conducting randomized or quasi-experiments or exploiting natural experiments to uncover the mechanisms by which online ratings and review systems in<sup>fl</sup>u ence consumers. Randomized experiments have been used to show that <sup>fi</sup>nancial incentives increase the volume of reviews given by users, whereas social incentives motivate users to leave longer reviews (Burtch et al. 2018), and that cooperatively framed feedback is most effective at motivating female subjects, whereas competitively framed feedback is effective at motivating male subjects (Huang et al. 2019b). The impact of the implementation of a word-of-mouth system has been investigated through <sup>fi</sup>eld experiments in an e-commerce setting (Huang et al. 2019a), through a quasi-experiment in a social network setting (Wang et al. 2018), and through natural experiments in healthcare settings (Khurana et al. 2019, Shukla et al. 2021). Our work contributes to this literature by inducing rating in<sup>fl</sup>ation through an experiment, on a hyper-local food delivery platform, and presenting its impact on user purchases, trial, and sales concentration.

We contribute to the literature on rating in<sup>fl</sup>ation, in which ratings become less informative and useful over time because of a decrease in their variance (Filippas et al. 2022). Most studies on this topic focus on the reasons why the rating averages change over time, some of which are as follows: self-selection (L and Hitt 2008), reciprocity (Dellarocas and Wood 2008, Bolton et al. 2013, Fradkin et al. 2021, Proserpio et al. 2018) and the related concept of “re<sup>fl</sup>ected” costs (Filippas et al. 2022), herding behavior (Salganik et al. 2006, Muchnik et al. 2013, Aral 2014), and social nudging (Wang et al. 2018). Our study differs from prior studies because instead of investigating the various causes of rating average changes, we focus on identifying the consequences of rating in<sup>fl</sup>ation on user choices. Rating variance has been studied within a product and has been shown to be correlated with higher demand for low-rated products (Sun 2012), whereas our focus is on how rating variance across sellers impacts user purchases, trial, and sales concentration.

Our work builds on several recent studies that have focused on improving the design of online rating systems to make them more useful to users. Although Chen et al. (2018) show that multidimensional rating systems can be more informative to users, Dai et al. (2018) argue that since most users are inattentive, the aggregation of ratings into a single metric is optimal. Similarly, Nosko and Tadelis (2015) demonstrate that adjusting a single metric of seller reputation to make it more informative can improve consumer outcomes signi<sup>fi</sup>cantly. Kokkodis (2019) recommends a rating de<sup>fl</sup>ation method to counteract the loss of informativeness because of rating in<sup>fl</sup>ation. Our study provides evidence of the need for platform designers to build informativeness into the design of rating systems and estimates the potential consequences if rating in<sup>fl</sup>ation were left unaddressed.

More broadly, our work relates to the vast literature that has examined the impact of digital word-ofmouth on sales and found a largely positive effect (Chevalier and Mayzlin 2006, Duan et al. 2008b, Zhu and Zhang 2010, Anderson and Magruder 2012, Lu et al. 2013, Mayzlin et al. 2014, Lewis and Zervas 2016, Tadelis 2016, Song et al. 2019). These studies mostly used observational and often aggregated data to measure the effects of digital word-of-mouth, whereas we use transaction-level data from an experiment to identify the impact of rating in<sup>fl</sup>ation on purchase, trial, and sales concentration. In particular, we contribute to literature that investigates the mechanism of social learning through digital word-of-mouth (Cai et al. 2009, Cabral and Hortacsu 2010, Zhao et al. 2013, Wu et al. 2015, Huang et al. 2016, Acemoglu et al. 2017, Wang et al. 2018, Fang 2022).

## 3. Data

For this study, we partnered with a large hyper-local food delivery platform in Asia. Our data consist of every transaction made on the chosen food delivery platform in a large Asian city over a period of about 16 weeks. During the observation period, we conducted an experiment in which the rating aggregation rule on the platform was exogenously changed, which resulted in rating in<sup>fl</sup>ation. The experiment occurred in a subarea of the city in April 2017, in the 11th week of our observation period. We drop observations for that week to allow for clear demarcation of pre- and postexperiment periods. We also drop observations from the <sup>fi</sup>rst and last week for which we have incomplete data. All together, we use 9 weeks of pre-experiment data (weeks 2–10) and 4 weeks of postexperiment data (weeks 12–15).

We further re<sup>fi</sup>ned the data set in two ways. First, users continued to join the platform during the observation period, but because our approach is to measure changes in behavior because of the experiment, we focused on users who made at least one purchase on the platform one month before the experiment. In Online Appendix B, we analyze new users who join during the observation period, before and after the experiment. Second, we dropped user accounts that have more than three purchases from the same restau rant on the same day. These are likely shared group accounts and as such behave differently than individual users. In Online Appendix C, we report results from robustness checks with different thresholds. After dropping such users, we were left with 198,044 users who placed 1,510,739 transactions from 2,244 distinct restaurants as summarized in Table 1.

Our main dependent variables for the user-level analysis are weekly purchases (n\_purchase) and trials (n\_trial). Weekly purchases are a count of the number of purchases made by a user on the platform each week. We measure a user’s trial by counting the number of restaurants a user tries for the <sup>fi</sup>rst time in our observation period each week. We calculate this metric by generating a cumulative count of the number of distinct restaurants a user has tried each week and denoting the increase in this number as n\_trial for that week. For example, if a user makes <sup>fi</sup>ve purchases in a week, three of which are from restaurants they have previously purchased from, and the remaining two are from distinct restaurants they are purchasing from for the <sup>fi</sup>rst time within the observation period, then n\_purchase 5 and n\_trial 2 for that user-week. Note that n\_trial is de<sup>fi</sup>ned conditional on purchasing. If n\_purchase 0, then n\_trial is unde<sup>fi</sup>ned.

Table 1.

<table><tr><td>Description</td><td>N</td></tr><tr><td>Number of users</td><td>198,044</td></tr><tr><td>Number of restaurants</td><td>2,244</td></tr><tr><td>Number of transactions</td><td>1,510,739</td></tr><tr><td>Number of full pre-experiment weeks</td><td>9</td></tr><tr><td>Number of full postexperiment weeks</td><td>4</td></tr></table>

Table 2 describes the variables and presents summary statistics for the weekly aggregated data. In our sample, an average user made approximately 0.64 transactions per week. Conditional on making a purchase, the average user trials 0.92 restaurants per week. This relatively high frequency of trial is a consequence of the fact that in our data, we do not observe each user’s entire transaction history on the platform; instead, we observe only transactions made within the observation period. To improve the identi<sup>fi</sup>cation of trials, we used the <sup>fi</sup>rst four weeks of data to generate a history for each user and used the next <sup>fi</sup>ve weeks before the experiment as our pretreatment data in our analysis. Doing this improves the accuracy of our count of trial.

The average restaurant has 67.28 transactions per week on the platform, which we denote as their sales. Before the experiment, the average restaurant rating on the platform was 3.53.

## 4. Institutional Setting

## 4.1. App, Ratings, and User Feedback

When registered users open the platform’s mobile app or visit their website, they can view restaurants within a 5-km (3.1-mile) radius of their delivery location. Most users, around 85%, transact with the platform through its mobile app, whereas the rest transact through the desktop website. On the home screen of the app or the desktop website, users view a list of available restaurants and their rating, estimated time to deliver, and their price range. An illustrative diagram of the mobile app’s user interface is shown in Figure 1. Selecting a restaurant displays its full menu from which users select items and complete their order.

Figure 1. Delivery Platform’s Mobile App  
![](/api/attachments/57YWUSQX/fulltext/images/9b1850715a5752361ea55fb3880e8745d38e4214ff1dc9c3fcbe99cefdf78eac.jpg)  
Notes. The restaurant rating is displayed in the bottom center of each listing. To the left of the rating is the price range of the restaurant, and to its right is the estimated time to delivery based on the user’s location.

Ratings are calculated by aggregating user feedback. Users provide a feedback score for their previous transaction on a scale of zero to <sup>fi</sup>ve stars for restaurant quality before they can initiate a new transaction on the platform. The online platform aggregates these user feedback scores into a numerical rating displayed for each restaurant. Ratings are updated daily to include new user feedback scores received each day.

To allow a restaurant’s rating to re<sup>fl</sup>ect its current quality, the platform multiplies each user feedback score with a recency-weight. The recency-weight is one for feedback received in the most recent 15 days and this weight is reduced by 0.1 for each previous 15-day duration. Therefore, feedback scores received 15–30 days ago are weighted by 0.9, those received 30–45 days ago are weighted by 0.8, and so on. Feedback scores received over 150 days ago are discarded. This weighted-average rating is then rounded off to the nearest one decimal place.

Table 2. Summary Statistics (per Week)

<table><tr><td>Variable</td><td>Description</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td>n_purchase</td><td>Purchases by user</td><td>0.64</td><td>1.23</td><td>0</td><td>29</td></tr><tr><td>n_trial</td><td>New restaurants tried by user</td><td>0.92</td><td>1.00</td><td>0</td><td>14</td></tr><tr><td>sales</td><td>Number of transactions per restaurant</td><td>67.28</td><td>99.87</td><td>0</td><td>1,777</td></tr><tr><td>pre_rating</td><td>Average restaurant rating pre-experiment</td><td>3.53</td><td>0.28</td><td>2.1</td><td>4.40</td></tr></table>

## 4.2. Rating Informativeness and Deflation

The rounding-off of calculated ratings to the nearest one decimal place may lead to a situation where several restaurants have the same displayed numerical rating. For example, all restaurants with calculated ratings between 3.85 and 3.94 are rounded off to have a displayed rating of 3.9. To appreciate the severity of this issue, consider that, of 48 restaurants in one neighborhood, 13 had the same rating of 4.3, another 13 had a rating of 4.2, and 9 had a rating of 4.1. Together, almost three-fourths of all restaurants in the neighborhood had ratings in the narrow range of 4.1 and 4.3. For users residing in this neighborhood, ratings provided limited information to differentiate between available restaurants. Because of their high mean and low variance, we refer to these as “in<sup>fl</sup>ated” ratings.

With this context, we consider rating informativeness to be determined by the variance of the rating distribution. A rating system is informative to the extent that it helps users differentiate between restaurants; distinct ratings are more informative than identical ratings. The greater the rating variance, the lower the number of restaurants with identical ratings, making ratings more informative for users. In Online Appendix A, we provide a brief overview of commonly used rating systems on other platforms and their respective informativeness.

The platform, about 14 months before the observation period of this study, recognized the problem of less informative ratings, and sought to ameliorate it by increasing the variance of the rating distribution. This change reduced the number of restaurants having identical ratings. At the same time, to accommodate the higher rating variance after redistribution, the platform also decreased the mean of the rating distribution. Thus, ratings were arti<sup>fi</sup>cially deflated by the platform to make them more informative 14 months before the observation period of this study. This approach of adjusting ratings to make them more informative is recommended by Dai et al. (2018), Nosko and Tadelis (2015), and Kokkodis (2019).

## 4.3. Experiment: Rating Inflation

Rating de<sup>fl</sup>ation by the platform about 14 months before the observation period of this study was an attempt to counteract rating in<sup>fl</sup>ation. Fourteen months is a relatively long time, so we do not expect that the rating de<sup>fl</sup>ation shock has an impact on our study. We used this unique opportunity to exogenously induce a rating in<sup>fl</sup>ation shock for this study. We dropped the <sup>fi</sup>rst week’s data because it was incomplete. After nine weeks of pre-experiment data, we rolled back the rating de<sup>fl</sup>ation imposed by the platform for a treated neighborhood in week 11 while retaining the arti<sup>fi</sup>cially de<sup>fl</sup>ated ratings for the rest of the city as a contro group. Thus, the treated group experienced a rating in<sup>fl</sup>ation shock, whereas the control group did not. Rolling back the rating de<sup>fl</sup>ation caused a temporary platform-wide disruption to the service for two days that decreased orders on the platform from all restaurants. This disruption was quickly <sup>fi</sup>xed, and order volume reached normal levels within two days. Because the disruption was platform-wide, it does not have an impact on our identi<sup>fi</sup>cation strategy. We drop the data from week 11 for our analysis to conservatively exclude the period around the disruption. We observe postexperiment data for four full weeks after the experiment. The timeline of rating changes relative to the observation period is illustrated in Figure 2.

The treated neighborhood had 48 restaurants on the platform from which 3,753 distinct users made purchases in the pre-experiment observation period. To prevent the treated users from being exposed to both treated and untreated restaurants at the same time, we selected the treated restaurants from a geographically contiguous region that is relatively isolated from the rest of the city. Although such geographical selection of the treated group may lead to the presence of systematic differences in the characteristics of treated and control users and restaurants, we validate our results by checking for pre-experiment parallel trends and running robustness checks with randomization inference and synthetic controls. More details are discussed in Sections 6.2.3 and 7.4.

Figure 2. (Color online) Timeline for Rating Changes  
![](/api/attachments/57YWUSQX/fulltext/images/672b2c2b7633d1f530d095233c363b83192a754aae9d1551c5cf8b6e5287181a.jpg)  
Notes. Original in<sup>fl</sup>ated ratings were changed to de<sup>fl</sup>ated ratings 14 months before the observation period. First week’s data are dropped for being incomplete. Ratings were in<sup>fl</sup>ated for the treated region in week 11 of the observation period. During the experiment, in<sup>fl</sup>ated ratings wer displayed for the treated neighborhood, whereas de<sup>fl</sup>ated ratings continued to be displayed for control neighborhoods.

For treated group restaurants, the experiment increased the average rating by 0.71 stars on a 5-star rating scale, going from 3.45 stars to 4.16 stars. At the same time, the variance of the rating distribution decreased by 55%, dropping from 0.060 to 0.027. Together, these changes can be viewed as rating in<sup>fl</sup>ation. The decrease in rating variance is re<sup>fl</sup>ected in the reduced range of ratings for the 48 treated restaurants: the ratings take 12 distinct values before the treatment and only 8 distinct values after. Therefore, more restaurants have identical ratings after the rating in<sup>fl</sup>ation, making ratings less informative. The rating distributions are shown in Figure 3.

Because, as discussed earlier, treatment cannot be randomized, there are some differences in the activity levels of users in the treated and control groups. In Figure 4, we show how the proportion of users at various levels of purchase and trial varied over the observation period. We see that the trends are largely similar for purchases, whereas the experiment has a discernible impact on trials for treated users after the experiment. We provide a more formal check of parallel pre-experiment trends in Section 6.2.3. Besides user activity levels, we further compare neighborhood totals (total weekly purchases and trials) of the treated and control groups in Online Appendix D.

Figure 3. (Color online) Rating Distribution Before and After the Experiment for Treated and Control Groups  
![](/api/attachments/57YWUSQX/fulltext/images/b9f0720a24bb2c12dac55583b7e47f4c2b207a0a4fee8e3690d53e413303c34c.jpg)  
Note. Treated group experiences rating in<sup>fl</sup>ation, whereas the control group does not.

## 5. Hypotheses Development

The rating in<sup>fl</sup>ation shock induced by the experiment can be decomposed into an increase in the average rating and a decrease in the variance of ratings for treated restaurants. Here we describe how these two changes affect treated users’ perception of restaurant quality, and consequently, their choices.

The increase in average rating because of rating in<sup>fl</sup>ation results in treated users perceiving restaurants on the platform to be of higher average quality than before. The decrease in rating variance reduces the informativeness of rating signals that increases the uncertainty of a user’s perception of restaurant qual ity. Because the rating signal is less certain, it becomes less important in shaping a user’s quality perception. Correspondingly, the importance of other signals, such as prior beliefs and prior usage experience increase. Therefore, because of rating in<sup>fl</sup>ation, users rely less on ratings, and more on their prior beliefs and use experiences. In this section, we connect the changes in user quality perception because of rating in<sup>fl</sup>ation with the expected observable effects on user purchases and trial, and correspondingly, on restaurant sales and sales concentration.

## 5.1. Effect on User Purchases and Restaurant Sales

Our study examines the effect of rating in<sup>fl</sup>ation on experiential service of restaurant and food delivery. Other studies have examined similar effects in online retail. E-commerce websites saw a higher likelihood of products being added to carts when a larger number of word-of-mouth comments were seen by buyers (Huang et al. 2019a). Books on Amazon.com and Barnesandnoble.com sold more copies when ratings were raised (Chevalier and Mayzlin 2006).

In the context of restaurants, studies have found that restaurant sales increase merely by being listed on review platforms (Lu et al. 2013), and this value can be quanti<sup>fi</sup>ed (Wu et al. 2015). Furthermore, higher ratings have been shown to increase sales in a variety of settings. On Yelp.com, restaurants with a half-star higher rating sell out 19 percentage points more often, and the effect is even greater when customers only have information from this platform (Anderson and Magruder 2012).

In our context, the increase in mean rating because of rating in<sup>fl</sup>ation increases the perceived quality of restaurants on the platform. Assuming the perceived utility of the outside option does not change, we expect users to purchase more often on the platform after rating in<sup>fl</sup>ation and the restaurant sales to increase. The decrease in rating variance may make it harder for users to choose between restaurants and thus may shift their consumption patterns across restaurants, but overall, we expect that the increase in mean rating boosts the overall sales on the platform so that rating in<sup>fl</sup>ation increases user purchases and restaurant sales.

Figure 4. (Color online) User Activity Levels  
![](/api/attachments/57YWUSQX/fulltext/images/8196b9e03c2bef4565cdb15f2c4b53f26eae66a215547d9bea2c55860336bc32.jpg)

![](/api/attachments/57YWUSQX/fulltext/images/7b0ae47f2e379849fc3f3a22f79ce8230f2667395180ea015800d6af5c883a12.jpg)  
Notes. The experiment occurs in week 11 and pre-experiment trends are parallel for treatment and control group users. (a) Top row shows the proportion of users who make no purchase or one, two, or three or more purchases each week. (b) Bottom row shows the proportion of users who have no trial, one trial, or two or more trials each week. For the treated group, the proportion of users with no trial increases and the propor tion of users with one or more trials decreases after the experiment, indicating that trials decrease on average after the experiment.

Hypothesis 1. Rating inflation increases user purchases and restaurant sales.

## 5.2. Effect on User Trial

Users rely more on ratings when trying a new restaurant because of the absence of any direct experience with the restaurant. In<sup>fl</sup>ated ratings can be de<sup>fl</sup>ated to create more accurate estimates of a seller’s quality, allowing customers to make better judgements (Kokkodis 2019). Although the literature has made it clear that in<sup>fl</sup>ated ratings reduce informativeness of ratings, we further conjecture that this results in fewer user trials. In particular, rating in<sup>fl</sup>ation can affect both the risk of trial and the reward from trial, as we discuss later.

5.2.1. Increase in Risk of Trial. With rating in<sup>fl</sup>ation, rating variance decreases, and rating signals become less informative. Users <sup>fi</sup>nd it more dif<sup>fi</sup>cult to distinguish between restaurants and are less certain about restaurant quality (Nosko and Tadelis 2015, Dai et al. 2018). This is especially signi<sup>fi</sup>cant for restaurants they have not tried previously. Reviews have been shown to increase the sales of high-quality independent restaurants and facilitate user learning about restaurant quality, especially for tourists and travelers who are more likely to engage in trial than locals (Fang 2022). Similarly, rating in<sup>fl</sup>ation, by increasing the uncertainty of restaurant quality, increases the risk of trial.

5.2.2. Increase in Reward from Trial. At the same time, the decrease in rating variance leads to an increase in reward from trial. We consider the reward from trial to be the value of the information gained by trial. In general, consumers can gain information about new restaurants either through the ratings and reviews or by trying the restaurants themselves. When rating in<sup>fl</sup>ation occurs, the value of the information from the rating system decreases, so the value of the information from trial becomes relatively more valuable (i.e., the reward of trial becomes larger; Acemoglu et al. 2017). To see how this works, consider an extreme case of rating in<sup>fl</sup>ation, where all restaurants have the same rating on a platform. Now, to make better choices, users must engage in trial to gather usage signals about restaurant quality. This gathering of use signals has become more important, and hence more valuable, when ratings are uninformative. Therefore, trial becomes more valuable because of rating in<sup>fl</sup>ation.

The increase in reward from trial can be explained by the cue diagnosticity theory (Feldman and Lynch 1988, Dimoka et al. 2012): The degree to which consumers rely on and use a speci<sup>fi</sup>c cue in a decision depend on the cue’s diagnosticity. If a cue is nondiag nostic, consumers will turn to alternative cues that they <sup>fi</sup>nd to be diagnostic. When rating in<sup>fl</sup>ation hap pens, rating becomes a less diagnostic cue, so consumers will engage in trial to gain own experience as an alternative cue (Yi et al. 2017) or may even limit thei adoption (Cenfetelli and Schwarz 2011).

Overall, both the risk of trial and the reward from trial increase because of rating in<sup>fl</sup>ation. Which of these two effects dominates, that is, whether trial decreases or increases, is tested empirically through the experiment. We expect that the increase in risk from trials dominates the increase in reward from trials, so consumers will reduce trials after the experiment.

Hypothesis 2. Rating inflation decreases user trial.

## 5.3. Effect on Restaurant Sales Concentration

The changes in user choices can have an impact on the distribution of sales across restaurants on the platform. Understanding how rating in<sup>fl</sup>ation affects sales concentration is important for the platform because if sales concentrate among the top few restaurants on the platform because of rating in<sup>fl</sup>ation, the platform’s market power relative to these top restaurants may decrease. Such restaurants may be able to negotiate a lower commission to be paid to the platform for each transaction. Conversely, greater sales concentration may lower operational costs for the platform by combining multiple orders for delivery. In either case, it is important for the platform to understand the factors affecting sales concentration.

Rating in<sup>fl</sup>ation, by making rating signals less informative, makes users rely more on substitute signals, namely their prior beliefs and use experience. Assuming of<sup>fl</sup>ine and online restaurant popularity are correlated, popular restaurants are more likely to have been heard of (i.e., prior beliefs) or experienced by users (i.e., use experience) online or of<sup>fl</sup>ine. Therefore, users are more likely to have informative prior beliefs and usage experience signals for more popular restaurants, and as a result, their quality perception would be more precise for popular restaurants. As such, in response to rating in<sup>fl</sup>ation, users are likely to shift their consumption to more popular restaurants, and we expect the sales concentration to increase.

The differential impact of rating system on heterogeneous sellers has recently been examined by other studies. It was found that by giving consumers access to a rating system such as that of Yelp.com, highquality restaurants saw an increase in sales, whereas low-quality restaurants experienced a decrease (Fang 2022). Hotels with higher ratings on Yelp or Trip Advisor had higher demand and were able to charge higher prices (Lewis and Zervas 2016). In another study on a doctor appointment booking platform, it was found that doctors who were highly rated bene<sup>fi</sup>ted at the expense of unrated doctors (Shukla et al. 2021). These studies focus on how rating system affects different sellers and <sup>fi</sup>nd that popular or higher-rated sellers bene<sup>fi</sup>t more. Our study focuses on how a change in the rating system (i.e., rating in<sup>fl</sup>ation) affects different sellers. We expect a similar effect: rating in<sup>fl</sup>ation bene-<sup>fi</sup>ts popular restaurants the most and increases sales concentration on the platform.

Hypothesis 3. Rating inflation increases restaurant sales concentration.

## 6. Methodology

## 6.1. Empirical Model

6.1.1. For Users. For platform users, the dependent variables we are interested in analyzing, n\_purchases and $n \_ t r i a l ,$ are count variables. As such, we conduct our analysis using the pseudo-maximum likelihood <sup>fi</sup>xed-effects Poisson regression model (Silva and Tenreyro 2006, 2011; Ciani and Fisher 2019) for its several desirable properties: suitability for nonnegative but skewed data (Azoulay et al. 2010), consistency (Wooldridge 2010), and robustness to arbitrary patterns of serial correlation (Wooldridge 1999). The last property allows us to use weekly aggregated data rather than aggregating at the pre/postexperiment level (Bertrand et al. 2004). This helps in further controlling for temporal trends in our data (Wang and Goldfarb 2017). An additional bene<sup>fi</sup>t of using the Poisson estimator is that it does not suffer from the incidental parameters problem (Wooldridge 2010, Cameron and Trivedi 2013, Fernandez-Val and Martin´ 2016). We estimate the coef<sup>fi</sup>cients using the PPMLHDFE command in Stata (Correia et al. 2020), which allows for fast estimation of pseudo-Poisson regression models with high-dimensional <sup>fi</sup>xed effects. It is robust to statistical separation (Correia et al. 2019) and singletons (Correia 2015) that are present in our data.

We estimate the following equation to get the average treatment effect of the rating in<sup>fl</sup>ation experiment:

$$
Y _ {i s t} \sim \mathrm{Poisson} [ \mu_ {i} e x p (\beta D _ {s t} + \tau_ {t}) ],\tag{1}
$$

where $Y _ { i s t } \in \{ n \_ p u r c h a s e _ { i s t } , n \_ t r i a l _ { i s t } \}$ is the dependent variable for user $i ,$ group $s \in$ treated, control , and week $t ; \mu _ { i }$ is the user <sup>fi</sup>xed effect, $\tau _ { t }$ captures the week <sup>fi</sup>xed effects, $D _ { s t }$ is the treatment indicator equal to one for treated groups after the experiment and zero otherwise, and $\beta$ is the coef<sup>fi</sup>cient of interest. Cognizant of the challenges in interpreting interaction term coef<sup>fi</sup>- cients in nonlinear models (Ai and Norton 2003, Puhani

2012), we interpret this result as a difference-in-semielasticity (DIS), de<sup>fi</sup>ned as “the second explanatory variable’s impact on the dependent variable with respect to the <sup>fi</sup>rst explanatory variable” (Shang et al. 2018).

6.1.2. For Restaurants. The dependent variable of interest when analyzing restaurants on the platform is the number of weekly transactions: sales. We identify the average treatment effect on sales with the following equation:

$$
s a l e s _ {j s t} = \alpha + \beta D _ {s t} + \lambda_ {j} + \tau_ {t} + \epsilon_ {j s t},\tag{2}
$$

where sale $\dot { \beta } _ { j s t }$ is the number of transactions on the plat form for restaurant $j ,$ belonging to group $s \in$ <sub>{</sub>treated, control , in week $t ;$ α is a constant, $\beta$ is the estimate of the average treatment effect, $D _ { s t }$ is the treatment indicator equal to one for treated restaurants after the experiment and zero otherwise, $\lambda _ { j }$ and $\tau _ { t }$ are the restaurant and week <sup>fi</sup>xed effects, and $\epsilon _ { j s t }$ is the error term.

Next, to identify the change in sales concentration on the platform, we estimate the heterogeneous treatment effect of the rating in<sup>fl</sup>ation experiment on restaurants according to their popularity using the following equation:

$$
\begin{array}{c} s a l e s _ {j s t} = \alpha_ {0} + \alpha_ {1} a f t e r _ {t} \times p r e \_ s a l e s _ {j} + \beta_ {1} D _ {s t} + \beta_ {2} D _ {s t} \\ \times p r e \_ s a l e s _ {j} + \lambda_ {j} + \tau_ {t} + \epsilon_ {j s t}, \end{array}\tag{3}
$$

where sale $\dot { \gamma } _ { j s t }$ is the number of transactions on the plat form for restaurant $j ,$ belonging to group $s \in$ <sub>{</sub>treated, $c o n t r o l \} ,$ , in week $t ;$ after is a binary variable that equal one after the experiment and zero prior to it, pre\_sales is the total pre-experiment sales for restaurant $j , D _ { s t }$ is the treatment indicator that equals one for treated groups after the experiment and zero otherwise, $\beta _ { 2 }$ is the coef<sup>fi</sup>cient of interest; a positive value implies that more popular restaurants experience a larger increase in sales, suggesting an increase in sales concentration on the platform, $\lambda _ { j }$ and $\tau _ { t }$ are the restaurant and week <sup>fi</sup>xed effects, and $\epsilon _ { j s t }$ is the error term.

## 6.2. Identification Strategy

Two key assumptions are required for credible identi-<sup>fi</sup>cation using diferences-in-differences: (i) stable unit treatment value assumption (SUTVA) and (ii) parallel trends. In this section, we discuss our approach to minimize violations of SUTVA and check for preexperiment parallel trends of our dependent variables. However, <sup>fi</sup>rst, we describe how we <sup>fi</sup>lter our data sample to improve the accuracy of our measure of trial.

6.2.1. Data Sample. Our data span nine pre-experiment weeks and four postexperiment weeks. Because of this limited observation period, we do not observe each user’s entire history of purchases on the platform. We consider the <sup>fi</sup>rst time a user purchases from a restaurant in our observation period as a “trial,” even if they have purchased from that restaurant before the observation period began. This could lead to an in<sup>fl</sup>ation in the trial count. For instance, the <sup>fi</sup>rst purchase of every user in our observation period is always considered a trial in our data set.

We minimize potential identi<sup>fi</sup>cation problems from this issue in two ways: First, we perform our main analysis on a sample that excludes the initial four weeks of data (weeks 2–5), which are mostly likely to over-count trial. Second, we emphasize that our estimation strategy does not require an accurate count of trial but instead relies on changes in trends of trial between treated and control groups. We have the same issue of overcounted trials for both treated and control groups, so we do not expect this issue to affect our diff-in-diff estimate. We validate this assumption by checking whether the trends for trial for treated and control groups were parallel in the preexperiment period in Section 6.2.3. These steps alleviate the concern for potential bias in our estimates.

6.2.2. Stable Unit Treatment Value Assumption. Our experiment was designed to minimize potential violations of SUTVA by choosing a relatively isolated contiguous geographic area for treatment so that few users view restaurants from both the treated and control groups. If a user is shown restaurants from both the treated and control groups, they have an intermediate level of treatment, which is a violation of SUTVA. Given that our treatment is imposed at the restaurantlevel and not users, we expect some users will see restaurants from both the treated and control groups.

Seeing restaurants with ratings calculated by two different methods might cause users to have unpredictable reactions. Some may shift their purchase toward the treated restaurants, whereas others might question the reliability of the ratings on the platform, especially if it contradicts their prior knowledge about the quality of the restaurants. For example, if a restaurant renowned for its quality is displayed with a low rating because of the method by which it has been calculated, whereas if a mediocre restaurant is displayed with a high rating, users might disregard the rating entirely or may even distrust the platform. We attempted to mitigate this risk by selecting the treated restaurants from a geographically contiguous region that is relatively isolated from the rest of the city. With such a strategy, we attempted to minimize the number of users for whom the 5-km radius contained restaurants from both treated and control groups. Although we could not observe the list of restaurants each customer had available to them, we observed their transactions. We found that only 280 users, or about 0.14% of the total, transacted with restaurants from both the treated and control groups. This sug gests that the strategy for isolating the treated users from control group ratings was largely successful. We dropped these users from our analysis.

6.2.3. Parallel Trends Assumption. Although implementing the treatment condition on a geographic basis minimizes potential SUTVA violations, it could lead to violations of the parallel trend assumption. Different geographic regions may have different kinds of users and restaurants that re<sup>fl</sup>ect that region’s socioeconomic and demographic factors. To rule out this possibility, we checked whether the pre-experiment trends for users and restaurants in the treated and control groups were parallel for our dependent variables of interest.

Recall that we dropped the <sup>fi</sup>rst four weeks of data to allow for a more accurate measure of trial. We also dropped the week of the rating change, which is the 11th week in our data, to get clear pre- and posttreatment periods. We are left with <sup>fi</sup>ve weeks of pretreatment observations (weeks 6–10) and four weeks of posttreatment (weeks 12–15). We estimate the lead and lag coef<sup>fi</sup>cients of the treatment effect by estimating the following equation:

$$
Y _ {i s t} \sim \text { Poisson } \left[ \mu_ {i} \exp \left(\sum_ {t = 6, \dots , 1 0} ^ {1 2, \dots , 1 5} \beta_ {t} w e e k _ {t} \times t r e a t e d _ {s}\right) \right],\tag{4}
$$

where $Y _ { i s t }$ is the dependent variable for user $i ,$ $t = \{ 6 , \dots , 1 0 \} \cup \{ 1 2 , \dots , \hat { 1 } 5 \}$ are weeks, and $s \in \{ t r e a t e d ,$ control is the group; $\mu _ { i }$ are the user <sup>fi</sup>xed effects, week is the indicator variable for week $t ,$ treated is the indi cator variable for the treated group, $\beta _ { t }$ with $t \in$ $\{ 6 , \ldots , 1 0 \}$ are the “lead” estimates of the treatment effect, and $\beta _ { t }$ with $t \in \{ 1 2 , \ldots , 1 5 \}$ are the “lag” estimates of the treatment effect.

We plot the estimated coef<sup>fi</sup>cients for user purchase (n\_purchase) and user trial (n\_trial) in Figure 5(a) and <sup>fi</sup>nd that almost all lead coef<sup>fi</sup>cients are statistically insigni<sup>fi</sup>cant. Thus, we conclude that trends are parallel for the treated and control users prior to the experiment.

To check for parallel trends for restaurant sales, we estimate the lead and lag coef<sup>fi</sup>cients of the average treatment effect (β<sub>t</sub>) on sales in the following equation:

$$
s a l e s _ {j s t} = \alpha + \sum_ {t = 6, \dots , 1 0} ^ {1 2, \dots , 1 5} \beta_ {t} w e e k _ {t} \times t r e a t e d _ {s} + \lambda_ {j} + \epsilon_ {j s t},\tag{5}
$$

where $s a l e s _ { j s t }$ is the number of transactions on the platform for restaurant $j ,$ belonging to group $s \in \{ t r e a t e d , c o n t r o l \}$ , in week $t ;$ week is the indicator variable for week $t ,$ treated is the indicator variable for the treated group, $\beta _ { t }$ with $t \in$ $\{ 6 , \ldots , 1 0 \}$ are the lead estimates of the average treatment effect, and $\beta _ { t }$ with $t \in \{ 1 2 , \ldots , 1 5 \}$ are the lag estimates of the average treatment effect.

Figure 5. (Color online) Coef<sup>fi</sup>cient Plots of User Purchases, Trial, Restaurant Sales, and Sales Concentration  
![](/api/attachments/57YWUSQX/fulltext/images/551f259c9acece9a5f7c6f8bee8830a5c8f50503081c049f2205eb48769bc0e9.jpg)

(b) Restaurant  
![](/api/attachments/57YWUSQX/fulltext/images/d1039243dcd77acead31d8ed1ebecfd86af1cdd54697bb26084400e05cd634ad.jpg)  
Notes. (a) User purchases and trial: Coef<sup>fi</sup>cient plot of Equation (4) for $\beta _ { t } , t \in \{ 6 , . . . , 9 \} \cup \{ 1 2 , . . . , 1 5 \}$ . (b) Restaurant sales: Coef<sup>fi</sup>cient plot of Equa tion (5) for $\beta _ { t } , t \in \{ 6 , \ldots , 9 \} \cup \{ 1 2 , \ldots , 1 5 \}$ . Restaurant sales concentration: Coef<sup>fi</sup>cient plot of Equation (6) for $\gamma _ { t } , t \in \{ 6 , \dotsc , 9 \} \cup \{ 1 2 , \dotsc , 1 5 \}$ . Week t 10 is the baseline and its coef<sup>fi</sup>cient is normalized to zero. Displays the 95% con<sup>fi</sup>dence intervals.

Similarly, for checking parallel trends for restaurant sales concentration, we estimate the lead and lag coef-<sup>fi</sup>cients of the heterogeneous treatment effect $( \gamma _ { t } )$ in the following equation:

$$
\begin{array}{l} s a l e s _ {j s t} = \alpha_ {0} + \alpha_ {1}   a f t e r _ {t} \times p r e \_ s a l e s _ {j} \\ \qquad + \sum_ {t = 6, \ldots , 1 0} ^ {1 2, \ldots , 1 5} \beta_ {t}   w e e k _ {t} \times t r e a t e d _ {s} \\ \qquad + \sum_ {t = 6, \ldots , 1 0} ^ {1 2, \ldots , 1 5} \gamma_ {t}   w e e k _ {t} \times t r e a t e d _ {s} \times p r e \_ s a l e s _ {j} \\ \qquad + \lambda_ {j} + \epsilon_ {j s t}, \end{array}\tag{6}
$$

where pre\_sales is the total pre-experiment sales for restaurant $j ; \gamma _ { t }$ with $t \in \left\{ 6 , \ldots , 1 0 \right\}$ are the lead estimates of the heterogeneous treatment effect, and $\gamma _ { t }$ with $t \in \{ 1 2 , \ldots , 1 5 \}$ are the lag estimates of the heterogeneous treatment effect.

We plot the coef<sup>fi</sup>cients $\beta _ { t }$ in Equation (5) and $\gamma _ { t }$ in Equation (6) in Figure 5(b) and conclude that the preexperiment trends for both restaurant sales and sales concentration are parallel for treated and control restaurants.

To summarize, we <sup>fi</sup>nd that pre-experiment trends for the dependent variables, user purchases, trial, restaurant sales, and restaurant sales concentration, are parallel for treated and control units. We assume that these trends would have remained parallel in the absence of the rating in<sup>fl</sup>ation treatment, and we can use the control units to estimate the counterfactual for the treated units in the absence of rating in<sup>fl</sup>ation. This allows us to have a causal interpretation of the results in the next section.

## 7. Results

## 7.1. User Purchases and Restaurant Sales Increase

We expect that users would purchase more often on the platform when faced with in<sup>fl</sup>ated ratings. We <sup>fi</sup>rst show some model-free evidence of user purchases in Figure 6(a). We observe a small relative increase in the average purchases per week for treated users compared with control users after the experiment<sup>1</sup>.

We estimate Equation (1) using n\_purchases as the dependent variable and present the differences-indifferences (DD) estimates in Table 3. Columns (1) and (2) show the results with either week <sup>fi</sup>xed effects or user <sup>fi</sup>xed effects; column (3) show the results with both week and user <sup>fi</sup>xed effects as in Equation (1). We <sup>fi</sup>nd that user purchases increase by approximately 3:5% because of rating in<sup>fl</sup>ation. Although the direction of this effect is as expected, we note that this is a shortterm effect in response to a sudden rating in<sup>fl</sup>ation. Two caveats are worth noting. First, if rating in<sup>fl</sup>ation were to manifest more gradually, as is usually the case, we cannot conclude from these results that a similar increase in user purchases would happen. Second, over time, this increase may taper as users recalibrate their expectations of what high ratings signify on the platform. Nevertheless, in the setting of this experiment, we <sup>fi</sup>nd evidence that rating in<sup>fl</sup>ation causes an increase in user purchases in the short term.

Figure 6. (Color online) User Average Weekly Purchases and Trials  
![](/api/attachments/57YWUSQX/fulltext/images/f430ea9a7377aa02b303b7f815a2379327f4023d7c9a933fd638a9c363032203.jpg)

![](/api/attachments/57YWUSQX/fulltext/images/0a89fdbb34ecf249ed081a076c9af1389c59a65fc3546d9321f6090e61dac81d.jpg)  
Notes. (a) User average weekly purchases by group. (b) User average weekly trial by group. Pre-experiment trends are parallel for treated and control users. Compared with the decline in the control users postexperiment, the treated user purchases do not decline as much, whereas treated user trials decline more relative to the control users.

Because of rating in<sup>fl</sup>ation, the restaurants on the platform appear more attractive than the outside option, so we expect that restaurant sales increase after the experiment. In Table 4, columns (1) and (2) show the DD estimates of Equation (2), without and with week <sup>fi</sup>xed effects. We <sup>fi</sup>nd that restaurant weekly sales increase because of the experiment. This is consistent with our previous <sup>fi</sup>nding that user purchases increase after the experiment.

## 7.2. User Trial Decreases

Users face an increased risk of trying a new restaurant as a result of rating in<sup>fl</sup>ation. At the same time, users face an increased reward from trying a new restaurant as rating in<sup>fl</sup>ation makes information from trial more valuable. We expect that the increase in risk dominates the increase in reward so that user trials decrease after the experiment. The model-free evidence in Figure 6(b) supports this conjecture: there is a relatively steeper decrease in the average trial per week for treated users compared with control users after the experiment.

Table 3. User Purchases Increase Because of Rating In<sup>fl</sup>ation

<table><tr><td>Dependent variable = n_purchase</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td> $D_{st}$ </td><td>0.0345(0.0283)</td><td>0.0345*(0.0204)</td><td>0.0345*(0.0204)</td></tr><tr><td>Week fixed effects</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>User fixed effects</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>1,782,396</td><td>1,351,863</td><td>1,351,863</td></tr></table>

Note. Cluster-robust standard errors in parentheses.  
\*p < 0:1; \*\*p < 0:05; \*\*\*p < 0:01.

We estimate Equation (1) using n\_trial as the dependent variable and present the DD estimates in Table 5. Columns (1) and (2) show the results with either week <sup>fi</sup>xed effects or user <sup>fi</sup>xed effects; column (3) show the results with both week and user <sup>fi</sup>xed effects as in Equation (1). We <sup>fi</sup>nd that users reduced their trial in response to rating in<sup>fl</sup>ation. This implies that the increase in risk of trial outweighs the increase in reward from trial. The DD estimates in column (3) show that the number of new restaurants an average user tries decreased by approximately 7% because of rating in<sup>fl</sup>ation.

Table 4. Restaurant Sales Increase Because of Rating In<sup>fl</sup>ation

<table><tr><td rowspan="2">Dependent variable = sales</td><td colspan="2">All customers</td><td colspan="2">Only repeat customers</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $D_{st}$ </td><td>9.937***(1.546)</td><td>9.937***(1.540)</td><td>11.81***(1.355)</td><td>11.81***(1.220)</td></tr><tr><td>Week fixed effects</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>29,198</td><td>29,198</td><td>27,183</td><td>27,183</td></tr></table>

Note. Cluster-robust standard errors in parentheses.  
\*p < 0:1; \*\*p < 0:05; \*\*\*p < 0:01.

Given that user trials decrease after the experiment, we expect that restaurant sales come more from repeat customers rather than from new customers. To see whether this is the case, we re-estimate Equation (2) using sales from only repeat customers as the dependent variable and present the DD estimates in columns (3) and (4) of Table 4. We <sup>fi</sup>nd that restaurant weekly sales from repeat customers increase because of the experiment. The result supports our previous <sup>fi</sup>nding that user trials decrease after the experiment.

The decrease in user trial happened in conjunction with the increase in purchases by users. Thus, although rating in<sup>fl</sup>ation induced users to purchase more often, they were reluctant to try new restaurants because of less informative ratings. To the extent that the platform seeks to enable users to try new restaurants and discover new favorites, rating in<sup>fl</sup>ation inhibits that goal.

## 7.3. Popular Restaurants Benefit

The decrease in rating informativeness because of rating in<sup>fl</sup>ation is expected to result in increase in sales concentration. Users have fewer other signals for less popular restaurants and, as such, might be expected to prefer purchasing from better known and popular restaurants. We provide model-free evidence of this effect in Figure 7. Figure 7(a) presents the distribution of restaurant sales for the control and treated groups before and after the experiment. We <sup>fi</sup>nd that, although the density of the average weekly sales does not shift for the control group after the experiment, it shifts to more popular restaurants for the treated group. Figure 7(b) presents how the Her<sup>fi</sup>ndahl-Hirschmann index (HHI), a measure of market concentration, changes over time for the control and treated neighborhoods. We <sup>fi</sup>nd that HHI increases for the treated neighborhood after the experiment, again suggesting that restaurant sales concentrate more on the popular restaurants for the treated neighborhood after the experiment.

Table 5. User Trial Decreases Because of Rating In<sup>fl</sup>ation

<table><tr><td>Dependent variable = n_trial</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td> $D_{st}$ </td><td>0.00245(0.0289)</td><td>-0.0664**(0.0301)</td><td>-0.0670**(0.0301)</td></tr><tr><td>Week fixed effects</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>User fixed effects</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>564,634</td><td>513,136</td><td>513,136</td></tr></table>

\*p < 0:1; \*\*p < 0:05; \*\*\*p < 0:01.  
Note. Cluster-robust standard errors in parentheses.

We estimate Equation (3) using restaurant sales as the dependent variable and present the coef<sup>fi</sup>cient estimates in Table 6. The variable pre\_sales is the total sales of a restaurant prior to the experiment and captures restaurant popularity. The negative coef<sup>fi</sup>cients of $D _ { s t }$ show that rating in<sup>fl</sup>ation reduces the sales of less popular restaurants, whereas the positive coef<sup>fi</sup>cients of $D _ { s t } \times p r e _ { - }$ \_sales implies that sales increase for more popular restaurants. Taken together, the results suggest a shift of sales from less popular restaurants to more popular restaurants, increasing sales concentration.

We interpret the results in Table 6 as a differencein-semielasticity (DIS) as exp 0:438 0:0216 exp $( - 0 . 4 3 8 ) = 1 . 4 \%$ as in Shang et al. (2018). This implies that the experiment increased sales by 1:4% for each additional unit of total pre-experiment sales.

The increase in market concentration can be explained by two observations. As rating in<sup>fl</sup>ation makes ratings less informative, users rely more on other signals, in particular their prior experience, which explains why sales shift toward more popular restaurants. In addition, we <sup>fi</sup>nd that trial decreases because of rating in<sup>fl</sup>ation, so users make repeat purchases from the most popular restaurants.

## 7.4. Robustness Checks

Our main results thus far have relied on the paralleltrend assumption, evidence of which we <sup>fi</sup>nd by checking for pre-experiment trends in Section 6.2.3. However, because the treatment and control regions are geographically separated regions in a large city, it is possible that there is a difference in the quality and quantity of restaurant options available to users in control and treatment regions. This fact, by itself, does not pose a challenge for identi<sup>fi</sup>cation as long as the parallel trends assumption holds. We, nevertheless, perform two robustness checks: (i) randomization inference and (ii) synthetic controls. A third robustness check as a pre-experiment placebo test is reported in Online Appendix C2.

7.4.1. Randomization Inference. We check the robustness of our estimates by calculating empirical p values using randomization inference (Imbens and Rubin 2015). For each model, we generate a randomized treatment vector and estimate the regression equation. We perform the randomization 1,000 times for each model and plot the generated coef<sup>fi</sup>cient estimates with the actual estimate of the coef<sup>fi</sup>cient in Figure 8. The empirical $p$ value is the proportion of generated coef<sup>fi</sup>cients with as or more extreme values than the actual coef<sup>fi</sup>cient. Table 7 shows the results of the randomization inference, with mean values of the randomization estimates, its standard deviation, and the empirical p value. The empirical p values are evidence that our estimates are robust.

Figure 7. (Color online) Restaurant Sales Distribution and Her<sup>fi</sup>ndahl–Hirschman Index  
(a) Restaurant Sales Distributior  
![](/api/attachments/57YWUSQX/fulltext/images/af0f914b36f20a547818d2060e8b8c32304b5b9eb5b190555fd627d080af1a65.jpg)

(b)Average Region HHI Index  
![](/api/attachments/57YWUSQX/fulltext/images/9ecab2e4428f5703299c668b4b771f17b676217b185bf04a466785e7b072c7de.jpg)  
Notes. (a) Sales distribution across restaurants before and after the experiment for the control and treated groups. The sales distribution does no change for the control group, whereas sales shift to more popular restaurants in the treated group. (b) HHI for treated and similar control neighborhoods. Pre-experiment trends for sales concentration are parallel. Sales concentration increases for the treated neighborhood after the experiment.

7.4.2. Synthetic Controls. We perform another robustness check of our results by creating synthetic control units to estimate the treatment effect. Our treatment is localized to one neighborhood. We use neighborhoodand user-level characteristics to create synthetic control users that are similar to the treated users. Although the user-level characteristics match user behavior, the neighborhood-level characteristics match the environment in which the users <sup>fi</sup>nd themselves in. For the neighborhood-level characteristics, we calculate the average daily sales and ratings of restaurants in the neigh borhood and the average transaction amount. These variables capture the average popularity, quality, and price tier of restaurants in the neighborhood that are available to the user. For the user-level characteristics, we include the average amount spent by the user prior to the experiment to create synthetic units that spend similarly on the platform. We also include the weekly values of the variables of interest, n\_purchase and n\_trials, for the pre-experiment period. The results are shown in Figure 9 and Table 8. We <sup>fi</sup>nd that purchases increase and trials decrease after the experiment when using synthetic control units to run the analysis.

Table 6. Sales of More Popular Restaurants Increase Because of Rating In<sup>fl</sup>ation

<table><tr><td>Dependent variable = sales</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>after</td><td></td><td>3.018***(0.645)</td><td></td></tr><tr><td>treated</td><td>0.226(0.886)</td><td></td><td></td></tr><tr><td>pre_sales</td><td>0.101***(0.000447)</td><td></td><td></td></tr><tr><td>after × pre_sales</td><td>-0.00438***(0.00124)</td><td>-0.00438***(0.00109)</td><td>-0.00438***(0.00109)</td></tr><tr><td>treated × pre_sales</td><td>0.0000136(0.00230)</td><td></td><td></td></tr><tr><td> $D_{st}$ </td><td>-0.438(1.952)</td><td>-0.438(1.778)</td><td>-0.438(1.767)</td></tr><tr><td> $D_{st} \times pre\_sales$ </td><td>0.0216***(0.00470)</td><td>0.0216***(0.00440)</td><td>0.0216***(0.00436)</td></tr><tr><td>constant</td><td>1.167***(0.279)</td><td>67.18***(0.155)</td><td>68.10***(0.251)</td></tr><tr><td>Week fixed effects</td><td>Yes</td><td>—</td><td>Yes</td></tr><tr><td>Restaurant fixed effects</td><td>—</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>29,198</td><td>29,198</td><td>29,198</td></tr></table>

Note. Cluster-robust standard errors in parentheses.  
\*p < 0:1; \*\*p < 0:05; \*\*\*p < 0:01.

Together, the randomization inference and synthetic control results add further con<sup>fi</sup>rmation to the robustness of our results.

7.4.3. Mechanism Check. The experiment exogenously induced rating in<sup>fl</sup>ation in the treated restaurants. Consumers in that neighborhood were exposed to in<sup>fl</sup>ated ratings and responded by marginally increasing purchases and signi<sup>fi</sup>cantly decreasing trial. However, it is possible that restaurants also responded to the experiment and made changes to their offerings. If this were the case, we cannot be certain whether our results re<sup>fl</sup>ect changes in consumer behavior or changes made by restaurants in response to rating in<sup>fl</sup>ation. In this section, we describe the reasons why the observed results are likely driven by consumer responses rather than restaurant responses to rating in<sup>fl</sup>ation.

First, to rule out potential responses by the restaurant, we conduct additional analysis on the restaurants by checking whether the average amount spent per transaction from a restaurant changes because of the experiment. If the restaurant were to raise their prices or make changes to their menu, we could expect to see a change in the average amount spent per transaction at the treated restaurants. However, we <sup>fi</sup>nd that there is no statistically signi<sup>fi</sup>cant difference in the average amount spent per transaction at treated restaurants as shown in Table 9.

Furthermore, our postexperiment period is about a month, which is a relatively short duration. Although the restaurant can potentially change their pricing and menu options in response to rating in<sup>fl</sup>ation, these changes are likely to take a longer time period to manifest.

Figure 8. (Color online) Randomization Inference for (a) User Purchases, (b) Trials, (c) Restaurant Sales, and (d) Sales Concentration  
![](/api/attachments/57YWUSQX/fulltext/images/d87c80c814da7bc50a011ac7a3bc2217a2118b4b6102c93d5a73908fa024f082.jpg)

(b) Randomization Inference for DD Coefficient of Trials  
![](/api/attachments/57YWUSQX/fulltext/images/ff1532fda8de0d29cfe9480ef5fb3a73273805fb3454614d8571f433acdaeaa9.jpg)

![](/api/attachments/57YWUSQX/fulltext/images/39c956d3e6bec5fe4760f82d6be5791c2ba4e4ac3e3423f2f708436cfccf4178.jpg)

(d) Randomization Inference for DD Coefficient of Sales Concentratior  
![](/api/attachments/57YWUSQX/fulltext/images/90870dff7db51373cb37dde023b25e8d770d39edce08ede7fd5b48c759958d55.jpg)  
Note. The empirical p values are 0.054 for purchases, 0.001 for trials, 0.017 for sales, and 0.005 for sales concentration.

Table 7. Results from Randomization Inference with Empirical p Values

<table><tr><td rowspan="2"></td><td colspan="2">Users</td><td colspan="2">Restaurants</td></tr><tr><td>(a) Purchase</td><td>(b) Trial</td><td>(c) Sales</td><td>(d) Sales_conc</td></tr><tr><td>Mean of random β</td><td>0.00119</td><td>0.000721</td><td>-0.1225</td><td>-0.000415</td></tr><tr><td>Standard deviation of random β</td><td>0.0215</td><td>0.0219</td><td>3.914</td><td>0.00914</td></tr><tr><td>Replications</td><td>1,000</td><td>1,000</td><td>1,000</td><td>1,000</td></tr><tr><td>Estimated β</td><td>0.0345</td><td>-0.0670</td><td>9.937</td><td>0.0216</td></tr><tr><td>Empirical p value</td><td>0.054</td><td>0.001</td><td>0.017</td><td>0.005</td></tr></table>

We also note that all the restaurants on the platform have a physical presence as a brick-and-mortar restaurant, with only a fraction of their total sales being generated through the food delivery app. Therefore, we believe the change in ratings on a food delivery app is unlikely to cause them to change their pricing or menu options, at least in the short term. Finally, we note that many restaurants are listed on other food delivery apps as well, which further diminishes the probability of them making signi<sup>fi</sup>cant changes based on the ratings system of one food delivery app. The empirical result and these arguments boost our con<sup>fi</sup>dence that the observed effects are unlikely to be driven by restaurant responses of changes in price or menu.

Figure 9. (Color online) Synthetic Control Estimates for User Purchases and Trials  
![](/api/attachments/57YWUSQX/fulltext/images/8f40915278887357989cd60cb5ee25ca925ae2b3684057ca4476714024fee3fc.jpg)

![](/api/attachments/57YWUSQX/fulltext/images/22f65ff081e94073c0f7ee426d38cc45dab792627a965ebf7518de1214775148.jpg)

![](/api/attachments/57YWUSQX/fulltext/images/95b218544d31884421ccd1f1ac429df747898aa2e9a892aea18c7a5346f1ac4a.jpg)

![](/api/attachments/57YWUSQX/fulltext/images/1bc03eb78aabff5e2be801942087ebffa9688caecc21bb25f3a256a9e62d4016.jpg)  
Notes. (a) Synthetic control for user purchases. The treatment and synthetic control units match well in the pre-experiment period, and purchase increase for the treatment units after the experiment. (b) Synthetic control for user trials. The treatment and synthetic control units match well in the pre-experiment period, and trials decrease for the treatment units after the experiment

Table 8. Results from Synthetic Control User Analysis

<table><tr><td></td><td>Percent change</td><td>p value</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td>n_purchase</td><td>5.9%</td><td>0.434</td><td>-6.0%</td><td>19.2%</td></tr><tr><td>n_trial</td><td>-24.9%</td><td>0.039</td><td>-40.3%</td><td>-5.6%</td></tr></table>

## 8. Discussion and Conclusion

We study the consequences of rating in<sup>fl</sup>ation in a quasi-experiment setting. The results lead to several important insights for managers, designers, and developers of digital platforms that use ratings to help users choose between numerous sellers.

First, rating in<sup>fl</sup>ation should be viewed not just as an increase in average ratings but also as a decrease in the informativeness of ratings because of lowering of the variance across ratings. Both these factors in<sup>fl</sup>uence users in different ways. High average ratings lead to greater user purchases, while lower rating variance reduces how much users trial new restaurants. Combined, these two effects lead to greater sales concentration as sales shift toward more popular restaurants.

Second, rating in<sup>fl</sup>ation can potentially hurt platform growth in two ways.

(a) Rating in<sup>fl</sup>ation may hurt the platform by reducing the informativeness of the rating system. Facilitating discovery and trial of new restaurants is an important component of the value proposition of digital platforms. Ratings reduce the search cost to <sup>fi</sup>nd quality restaurants by allowing the consumer to leverage and learn from other’s experiences. When rating in<sup>fl</sup>ation reduces the extent of trials by users, it erodes an important source of the value it provides to users: facilitating discovery and trial.

(b) Increased sales concentration because of rating in<sup>fl</sup>ation can hurt platform growth by reducing the market power of the platform relative to popular sellers on the platform. Most platforms negotiate the terms of a seller’s participation on the platform based on their relative market power. A rating system that increases sales concentration would harm the market power of the platform relative to the most popular sellers. In the context of this study, the participating platform negotiates the commission it receives from each restaurant per order based on the restaurant’s relative market power. The most popular restaurants pay little or no commission to the platform, whereas the less popula restaurants pay a larger commission. With these considerations, platforms have an incentive to reduce excess sales concentration on the platform.

Table 9. Average Amount Spent per Transaction Does Not Change

<table><tr><td>Dependent variable =  $avg\_bill$ </td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td> $D_{st}$ </td><td>-6.047(9.229)</td><td>-4.361(4.700)</td><td>-4.322(4.695)</td></tr><tr><td>Week fixed effects</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Restaurant fixed effects</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>26,927</td><td>26,924</td><td>26,924</td></tr></table>

Note. Cluster-robust standard errors in parentheses.  
\*p < 0:1; \*\*p < 0:05; \*\*\*p < 0:01.

Overall, our <sup>fi</sup>ndings demonstrate that managers and designers need to account for and strategize to minimize rating in<sup>fl</sup>ation on their platform to ensure its health and growth. Our discussions with the managers of the platform partners for this study revealed that managers are cognizant of the possibility of the strategic implications of rating in<sup>fl</sup>ation. As one consequence of this study, the platform decided to remove the rating de<sup>fl</sup>ation they had imposed to all users in the focal city, and eventually nationally as they prioritized increasing purchases at their stage of growth.

Our work contributes to the growing stream of the IS literature that has used randomized, natural, or quasi-experiments to uncover the mechanisms by which online ratings and review systems in<sup>fl</sup>uence consumers (Burtch et al. 2018; Huang et al. 2019a, b; Shukla et al. 2021).

Although this study identi<sup>fi</sup>es and expands our understanding of the impacts of rating in<sup>fl</sup>ation, it has a few limitations. First, because our observation period extends one month after the rating change, we are unable to investigate the long-term effects of rating in<sup>fl</sup>ation. The effects may attenuate over time as users recalibrate their expectations of what a high rating and a low variance represent compared with their outside option (Ho et al. 2017). Second, our partner platform does not collect textual reviews to maintain ease-of-use of their platform. As such, we are unable to measure if textual reviews alleviate the problem of rating in<sup>fl</sup>ation. Third, the role of culture in how users respond to rating in<sup>fl</sup>ation cannot be determined through this study as we have data from a single city. These areas can be promising directions for future research.

We also note the limits of generalizability of our <sup>fi</sup>ndings given the speci<sup>fi</sup>c institutional context in which the experiment was performed. First, although rating in<sup>fl</sup>ation in practice usually manifests endogenously and gradually over time, rating in<sup>fl</sup>ation in our study happens exogenously at once because of the platform’s action. Therefore, the results from the current experiment may not incorporate factors in practice that endogenously drive rating in<sup>fl</sup>ation. We also note that here was a temporary platform-wide disruption during the roll-out of the experiment that we have attempted to account for in our analysis by dropping data from the week of the experiment roll-out. The current experiment setting is still valuable because it provides a unique and feasible opportunity to understand the direct in<sup>fl</sup>uence of an exogenous change in rating mean and variance, without being confounded by endogenous causes of rating in<sup>fl</sup>ation in practice. The current experiment setting, although challenging and costly to conduct for the platform, exogenously induces rating in<sup>fl</sup>ation so that we could get causal estimates of the effect. It serves as the <sup>fi</sup>rst step toward understanding the effect of rating in<sup>fl</sup>ation in practice.

Finally, the effect of rating in<sup>fl</sup>ation may be different under two scenarios: (1) the platform does not curate the sellers (e.g., Yelp) and rating in<sup>fl</sup>ation happens by changing ratings only, without changing the types of sellers on the platform; and (2) the platform curates the sellers and rating in<sup>fl</sup>ation is driven by changing the types of sellers on the platform. In our context, although the platform has the ability to strategically curate the sellers in the long run, it did not change the selection of the sellers during our sample period. Therefore, our results represent the scenario in which rating in<sup>fl</sup>ation is only driven by changes in the ratings, given the same set of sellers. Our results may not be generalizable to the case in which rating in<sup>fl</sup>ation is caused by platforms’ strategically selection of the sellers; this would be an interesting avenue for future research.

## Acknowledgments

The authors appreciate the valuable feedback from the senior editor, associate editor, and anonymous reviewers. This research was made possible through the cooperation of the collaborating <sup>fi</sup>rm who has chosen to remain anonymous. The authors would like to thank the participants of INFORMS Annual Meeting, Conference on Digital Experimentation, and Conference on Information Systems and Technology for their helpful comments.

## Endnote

<sup>1</sup> Although we are unable to definitively determine the source of the declining trend of the control group in Figure 6(a), we conjecture that this could potentially be because of the technical disruption at the rollout of the experiment that affected both the treatment and control groups. As such, the control group still acts as the counterfactual for the treatment groups’ trend.

## References

Acemoglu D, Makhdoumi A, Malekian A, Ozdaglar A (2017) Fast and slow learning from reviews. NBER Working Paper No. w24046, National Bureau of Economic Research, Cambridge, MA.

Adamopoulos P, Ghose A, Todri V (2018) The impact of user per sonality traits on word of mouth: Text-mining social media platforms. Inform. Systems Res. 29(3):612–640.

Ai C, Norton EC (2003) Interaction terms in logit and probit models. Econom. Lett. 80(1):123–129.

Anderson M, Magruder J (2012) Learning from the crowd: Regression discontinuity estimates of the effects of an online review database. Econom. J. (London) 122(563):957–989.

Aral S (2014) The problem with online ratings. MIT Sloan Manage ment Rev. 55(2):47.

Azoulay P, Zivin JSG, Wang J (2010) Superstar extinction. Quart. J. Econom. 125(2):549–589.

Bertrand M, Du<sup>fl</sup>o E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1):249–275.

Bolton G, Greiner B, Ockenfels A (2013) Engineering trust: Reciprocity in the production of reputation information. Management Sci. 59(2):265–285

Burtch G, Hong Y, Bapna R, Griskevicius V (2018) Stimulating online reviews by combining <sup>fi</sup>nancial incentives and social norms. Management Sci. 64(5):2065–2082.

Cabral L, Hortacsu A (2010) The dynamics of seller reputation: Evi dence from ebay. J. Industrial Econom. 58(1):54–78.

Cai H, Chen Y, Fang H (2009) Observational learning: Evidence from a randomized natural <sup>fi</sup>eld experiment. Amer. Econom. Rev. 99(3):864–882.

Cameron AC, Trivedi PK (2013) Regression Analysis of Count Data, vol. 53 (Cambridge University Press, Cambridge, UK).

Cenfetelli RT, Schwarz A (2011) Identifying and testing the inhibitors of technology usage intentions. Inform. Systems Res. 22(4): 808–823.

Center PR (2016) Online shopping and e-commerce (Pew Research Center, Washington, D.C), 3. https://www.pewresearch.org/ internet/2016/12/19/online-shopping-and-e-commerce/.

Chen PY, Hong Y, Liu Y (2018) The value of multidimensional rating systems: Evidence from a natural experiment and randomized experiments. Management Sci. 64(10):4629–4647.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Ciani E, Fisher P (2019) Dif-in-dif estimators of multiplicative treatment effects. J. Econom. Methods 8(1):20160011.

Correia S (2015) Singletons, Cluster-Robust Standard Errors and Fixed Effects: A Bad Mix. Technical Note (Duke University, Durham, NC).

Correia S, Guimaraes P, Zylkin T (2019) Verifying the existence of˜ maximum likelihood estimates for generalized linear models. Preprint, submitted March 5, https://arxiv.org/abs/1903.01633.

Correia S, Guimaraes P, Zylkin T (2020) Fast Poisson estimation˜ with high-dimensional <sup>fi</sup>xed effects. Stata J. 20(1):95–115.

Dai W, Jin G, Lee J, Luca M (2018) Aggregation of consumer ratings: An application to yelp.com. Quant. Marketing Econom. 16(3): 289–339.

Dellarocas C, Wood CA (2008) The sound of silence in online feedback: Estimating trading risks in the presence of reporting bias. Management Sci. 54(3):460–476.

Dimoka A, Hong Y, Pavlou PA (2012) On product uncertainty in online markets: Theory and evidence. Management Inform. Sys tems Quart. 36(2):395–426.

Duan W, Gu B, Whinston AB (2008a) Do online reviews matter? An empirical investigation of panel data. Decision Support Systems 45(4):1007–1016.

Duan W, Gu B, Whinston AB (2008b) The dynamics of online wordof-mouth and product sales: An empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Fang L (2022) The effects of online review platforms on restaurant revenue, consumer learning, and welfare. Management Sci., ePub ahead of print February 1, https://doi.org/10.1287/mnsc. 2021.4279

Feldman JM, Lynch JG (1988) Self-generated validity and other effects of measurement on belief, attitude, intention, and behavior. J. Appl. Psych. 73(3):421.

Fernandez-Val I, Martin W (2016) Individual and time effects in´ nonlinear panel models with large n, t. J. Econometrics 192(1): 291–312.

Filippas A, Horton JJ, Golden J (2022) Reputation in<sup>fl</sup>ation. Management Sci., ePub ahead of print May 3, https://doi.org/10.1287/ mksc.2022.1350.

Fradkin A, Grewal E, Holtz D (2021) Reciprocity and unveiling in two-sided reputation systems: Evidence from an experiment on Airbnb. Marketing Sci. 40(6):1013–1029.

Godes D, Silva JC (2012) Sequential and temporal dynamics of online opinion. Marketing Sci. 31(3):448–473.

Ho YC, Wu J, Tan Y (2017) Discon<sup>fi</sup>rmation effect on online rating behavior: A structural model. Inform. Systems Res. 28(3): 626–642.

Hong YK, Pavlou PA (2014) Product <sup>fi</sup>t uncertainty in online markets: Nature, effects, and antecedents. Inform. Systems Res. 25(2):328–344.

Huang N, Burtch G, Hong Y, Polman E (2016) Effects of multiple psychological distances on construal and consumer evaluation: A <sup>fi</sup>eld study of online reviews. J. Consumer Psych. 26(4): 474–482.

Huang N, Sun T, Chen PY, Golden JM (2019a) Word-of-mouth system implementation and customer conversion: A randomized <sup>fi</sup>eld experiment. Inform. Systems Res. 30(3):805–818.

Huang N, Burtch G, Gu B, Hong Y, Liang C, Wang K, Fu D, Yang B (2019b) Motivating user-generated content with performance feedback: Evidence from randomized <sup>fi</sup>eld experiments. Management Sci. 65(1):327–345.

Imbens GW, Rubin DB (2015) Causal Inference in Statistics, Social, and Biomedical Sciences (Cambridge University Press, Cambridge, UK).

Khurana S, Qiu L, Kumar S (2019) When a doctor knows, it shows: An empirical analysis of doctors’ responses in a q&a forum of an online healthcare portal. Inform. Systems Res. 30(3):872–891.

Kokkodis M (2019) Reputation de<sup>fl</sup>ation through dynamic expertise assessment in online labor markets. Proc. World Wide Web Conf. (Association for Computing Machinery, New York), 896–905.

Lewis G, Zervas G (2016) The welfare impact of consumer reviews: A case study of the hotel industry. Unpublished manuscript. https://conference.nber.org/confer/2016/SI2016/PRIT/Lewis\_ Zervas.pdf.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Lu X, Ba S, Huang L, Feng Y (2013) Promotional marketing or word-of-mouth? Evidence from online restaurant reviews. Inform. Systems Res. 24(3):596–612.

Mayzlin D, Dover Y, Chevalier J (2014) Promotional reviews: An empirical investigation of online review manipulation. Amer. Econom. Rev. 104(8):2421–2455.

Muchnik L, Aral S, Taylor SJ (2013) Social in<sup>fl</sup>uence bias: A random ized experiment. Science 341(6146):647–651.

Nosko C, Tadelis S (2015) The Limits of Reputation in Platform Markets: An Empirical Analysis and Field Experiment (National Bureau of Economic Research, Cambridge, MA).

Proserpio D, Xu W, Zervas G (2018) You get what you give: Theory and evidence of reciprocity in the sharing economy. Quant. Marketing Econom. 16(4):371–407.

Puhani PA (2012) The treatment effect, the cross difference, and the interaction term in nonlinear “difference-in-differences” models. Econom. Lett. 115(1):85–87.

Salganik MJ, Dodds PS, Watts DJ (2006) Experimental study of inequality and unpredictability in an arti<sup>fi</sup>cial cultural market. Science 311(5762):854–856.

Shang S, Nesson E, Fan M (2018) Interaction terms in poisson and log linear regression models. Bull. Econom. Res. 70(1): 89–96.

Shukla AD, Gao G, Agarwal R (2021) How digital word-of-mouth affects consumer decision making: Evidence from doctor appointment booking. Management Sci. 67(3):1329–1992.

Silva JS, Tenreyro S (2006) The log of gravity. Rev. Econom. Statist. 88(4):641–658.

Silva JS, Tenreyro S (2011) Further simulation evidence on the performance of the poisson pseudo-maximum likelihood estimator. Econom. Lett. 112(2):220–222.

Song T, Huang J, Tan Y, Yu Y (2019) Using user- and marketergenerated content for box of<sup>fi</sup>ce revenue prediction: Differences between microblogging and third-party platforms. Inform. Systems Res. 30(1):191–203.

Sun M (2012) How does the variance of product ratings matter? Management Sci. 58(4):696–707.

Tadelis S (2016) Reputation and feedback systems in online platform markets. Annu. Rev. Econom. 8:321–340.

Wang CA, Zhang XM, Hann IH (2018) Socially nudged: A quasi experimental study of friends’ social in<sup>fl</sup>uence in online prod uct ratings. Inform. Systems Res. 29(3):641–655.

Wang K, Goldfarb A (2017) Can of<sup>fl</sup>ine stores drive online sales? J Marketing Res. 54(5):706–719.

Wooldridge JM (1999) Quasi-likelihood methods for count data. Pesaran MH, Schmidt P, eds. Handbook of Applied Econometrics, vol. 2, Microeconomics (Blackwell Publishers Ltd., New Jersey), 352–406.

Wooldridge JM (2010) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge, MA).

Wu C, Che H, Chan TY, Lu X (2015) The economic value of onlin reviews. Marketing Sci. 34(5):739–754.

Yi C, Jiang Z, Benbasat I (2017) Designing for diagnosticity and serendipity: An investigation of social product-search mechanisms. Inform. Systems Res. 28(2):413–429.

Zervas G, Proserpio D, Byers J (2021) A <sup>fi</sup>rst look at online reputation on Airbnb, where every stay is above average. Marketing Lett. 32(1):1–16.

Zhao Y, Yang S, Narayan V, Zhao Y (2013) Modeling consumer learning from online product reviews. Marketing Sci. 32(1): 153–169.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
