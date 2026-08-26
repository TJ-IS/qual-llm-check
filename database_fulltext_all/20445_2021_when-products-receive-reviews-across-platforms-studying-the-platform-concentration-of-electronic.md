---
otero_id: 20445
otero_key: "GSCJUS39"
title: "When products receive reviews across platforms: Studying the platform concentration of electronic word-of-mouth"
authors: "Hong Chen; Wenjing Duan; Wenqi Zhou"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103532"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# When products receive reviews across platforms: Studying the platform concentration of electronic word-of-mouth

![](/api/attachments/GSCJUS39/fulltext/images/0642d441475b11a5d82c6b7591f9af80e0e0ea1a689bea69ef56c83048f8d06b.jpg)

Hong Chen <sup>a,1</sup>, Wenjing Duan <sup>b,1</sup>, Wenqi Zhou <sup>c,1,\*</sup>

<sup>a</sup> Department of Information Sciences and Technology, Penn State University at New Kensington, Conference Center B015B, 3550 Seventh Street Road, New Kensington, Pennsylvania, 15068-1765, United States

<sup>b</sup> Department of Information System & Technology Management, School of Business, George Washington University, Funger Hall, Suite 515, 2201 G Street, NW, Washington, DC 20052, United States

<sup>c</sup> Department of Accounting, Information Systems & Technology, and Supply Chain Management, Palumbo-Donahue School of Business, Duquesne University, Rockwel Hall 901, 600 Forbes Avenue, Pittsburgh, PA 15282, United States

## A R T I C L E I N F O

Keywords: Electronic word-of-mouth User-generated content Volume equality Valence equality Online retail sales Platform concentration

## A B S T R A C T

A product can receive Electronic Word-of-Mouth (eWOM), e.g., user reviews, at both retail and review platforms, with considerable variance in volume and valence. We define such eWOM variation across platforms as the platform concentration of eWOM. A lower platform concentration is measured by a higher level of volume equality and valence equality, i.e., a more comparable number of user reviews and more consistent average ratings among multiple platforms, respectively. Results from multiple models over software data from retail and review plat forms shows that volume equality and valence equality positively interact to affect online users’ product adoption decisions.

## 1. Introduction

The Internet and electronic commerce have accumulated and distributed electronic word-of-mouth (eWOM) information at an un precedented rate. Most of the retail platforms provide online user review systems to encourage users and consumers to share their experiences, while many review platforms, as a relatively more independent source, often host both user reviews and expert opinions. Accordingly, mar keters in a variety of industries have widely embraced the eWOM mar keting strategy as an alternative to traditional advertising [10, 15, 35, 38], such as building online user communities and offering user mone tary and non-monetary incentives to contribute to eWOM. To quantify the market outcome of the eWOM strategy, significant attention has been paid toward understanding the eWOM effect [51]. Among eWOM literature. the two most widely discussed quantitative metrics are review volume which measures the total amount of user conversation and re view valence which measures average customer evaluation [34, 44]. Review volume and review valence are shown to influence user awareness of the product and imply product quality, respectively [27], thereby playing different roles in online user’s decision-making [3, 6, 9, 14, 28, 32, 33, 37].

Presently, with the growing prosperity of e-commerce and the digital world, it is common for a product to simultaneously receive hundreds of user feedbacks and product reviews from multiple platforms. For example, the software program Norton Security Deluxe receives approx imately 3800 customer reviews at Amazon and 700 at CNET download (download.cnet.com; CNETD). Just like Norton software, products may receive a disproportionately high or low volume of reviews and/or more favorable reviews at one platform than at the others. This phenomenon is defined as the platform concentration of eWOM. For example, a low platform concentration describes that a product receives comparable eWOM in volume and valence across multiple platforms.

It is natural to ask the question of how such platform concentration of eWOM affects a user’s decision of adopting products. Does it make a difference to retail sales if one platform reviewed a product more heavily and more positively than other platforms, all else being equal? The answer can provide marketers a more holistic view of designing their eWOM marketing strategy beyond a single platform. It also suggests to marketers that the return of eWOM investment on a single platform can vary, depending on eWOM hosted by other platforms. The literature on eWOM hosted by multiple platforms is not able to offer a direct answer. The extant literature shows a common theme of comparing the relative importance of eWOM volume and valence among different platforms. The underlying rationale is that the source identity of eWOM varies with different types of platforms, such as retailer hosted vs. third-party hosted eWOM [22]. Differentiating from previous research, the current work does not attempt to add to those discussions. Instead, we introduce a new perspective of platform concentration to this research line regarding eWOM hosted by different types of platforms.

We propose two new quantitative metrics to measure platform con centration: volume equality and valence equality, across the retail and review platforms. Retail and review platforms are two distinct types of platforms with different service purposes and serving different user populations [44]. Online consumers purchase products on a retail platform, but people mainly visit a review platform to look for product information and interact with others without directly placing orders. Among a variety of available eWOM metrics, we choose to focus on volume and valence, given that they are most widely available at nearly every platform and are found to influence user’s decision-making [14, 34]. Our proposed metrics are built upon them and are thus easy to implement in the practice.

We define volume equality of eWOM as the extent to which distinct platforms host online user-generated conversations equally in volume [19]. Greater volume equality implies a more uniform volume of eWOM dispersed across several platforms. Total volume is generally believed to reflect the overall size of the user population being aware of the product [34]. We inherit the spirit of Godes and Mayzlin’s work (2004) to further propose the informational role of volume equality as the heterogeneity of online users being aware of the product: Greater volume equality captures more diverse user populations discussing and becoming aware of the product. Valence equality captures the consistency of average product evaluations among different platforms. Greater valence equality indicates a more consistent valence of eWOM across platforms. And valence equality is related to cognitive costs for online users to reconcile inconsistent user opinions and thus can potentially affect user decisions.

To examine the effects of these two platform concentration metrics, we constructed a panel dataset on software programs at both Amazon and CNETD over 33 weeks. To the best of our knowledge, the current study is the first to uncover that the platform concentration of eWOM across different types of platforms, in both volume and valence, has a significant impact on online user decisions of adopting products. In our specific context, we operationalize online users’ software adoption de cisions at Amazon as software sales and at CNETD as software downloads. We find that greater volume equality of eWOM across retail and review platforms is associated with greater Amazon sales and more CNETD software downloads. In addition, we also find evidence that greater valence equality of eWOM (i.e., more consistent user ratings) across platforms is positively associated with online retail sales and software downloads. Volume equality is also shown to further magnify such impact of valence equality. When a product gets adversely impacted by small valence equality, greater volume equality can make it more detrimental.

The rest of this paper is organized as follows. We discuss the differ ence of our work from relevant literature in the next section, followed by our proposed research hypotheses. We then describe the research context and variables. Afterward, we present our empirical models and discuss the estimations and robustness tests. Finally, we make conclu sions and discuss the theoretical and practical implications of the cur rent study, as well as identify areas for future research.

## 2. Related Literature and Hypotheses

## 2.1. Related Literature

Recently a growing stream of eWOM literature has been trying to understand the differential impact of eWOM information from multiple sources on user choices [2, 4, 7, 20, 22, 36, 40, 44, 45, 54]. Overall, there are two approaches to differentiate eWOM sources. The more common approach, which is remotely related to ours, is to differentiate the reviewer identity and study the eWOM hosted by a single platform. In essence, this approach compares the trustworthiness and information quality of eWOM information according to reviewer type [2, 7, 29, 30, 55]. For example, Amblee and Bui [2] compared the magnitude of the impact of online user reviews and professional reviews and found no significant difference. Zhou and Duan [55] found that eWOM origi nating from multiple reviewer identities are not independent of each other. They identified a mediation mechanism that professional-generated reviews influence online user choices through user-generated reviews.

The other approach to differentiate eWOM sources is by dis tinguishing types of hosting platforms, which is closer to our work [19, 22, 44]. In this line of research, a small number of researchers have worked on analyzing review texts to comparing the information quality of reviews hosted by multiple sources [52]. Xiang et al. [52] examined review data from TripAdvisor, Expedia, and Yelp to demonstrate the discrepancy in review linguistic features, topics, and sentiments as well as their relationships to review ratings and usefulness. Other studies have focused on numerical metrics of eWOM, including volume and valence. Gu et al. [22] pointed out the difference between internal and external eWOM by comparing the impact magnitude of the eWOM hosted by review and retail platforms. They found that eWOM from the retail platform (internal eWOM) is more influential than eWOM from the review platform (external eWOM). In recent years, several scholars have conducted meta-analyses to summarize and synthesize the findings in eWOM literature [11, 44]. Those works compared the effect of eWOM from different platforms, as well as from different reviewer identities. Their conclusions underlined the need for more studies on eWOM hosted by distinct types of platforms.

Being different from those two directions of prior works, we do not intend to compare the relative impact and the differential information quality of eWOM hosted by different platforms. Instead, we propose a new perspective of studying eWOM from different types of platforms: platform concentration, based on readily available metrics of volume and valence. Godes and Mayzlin’s work appears to be the only study that touches on the idea of eWOM distribution across platforms (2004). They reported that the entropy of eWOM volume across Usenet newsgroups influences user’s decisions on TV shows. The volume entropy deter mined the degree to which the volume of user conversations is dispersed equally across groups, given that each newsgroup has a different user population [19]. Their work inspires us to define volume equality and valence equality to quantify platform concentration, measured by en tropy towards volume and valence, respectively. Following prior studies [44], we look into two specific platform types: review platform and retail platform. As compared to multiple communities of Usenet newsgroup in the work of Godes and Mayzlin [19], online users from two different types of platforms in our context should be more diverse, given different service objectives of platforms. Therefore, applying entropy to eWOM from reviewer and retail platforms is promising to produce valid metrics for platform concentration in this work. Godes and Mayzlin [19] have also successfully demonstrated the advantages of employing en tropy over the commonly used variance in quantifying the platform concentration in volume. Extended to our context, measuring volume equality by entropy can allow us to include both volume equality and total volume of eWOM across platforms as covariates in the model while using variance would have resulted in multicollinearity issues. This advantage also exists in applying entropy to measure valence equality, so that valence equality and the average valence of eWOM across plat forms in our models remain independent of each other. More details are included in Section 3.

Our study is also related to prior research on the valence variance of eWOM. These prior works focus on eWOM hosted by a single platform. For instance, a few recent studies have adopted rating variance within a single platform as a unique eWOM metric [16, 44, 48, 56]. Sun [48] reported that the variance of Amazon rating influences sales, depending on the corresponding average rating. Zhu and Zhang [56] found that variance of Gamespot.com ratings has a negative impact on sales of less popular video games. Rosario et al. [44] adopted valence variance within the platform to capture the heterogeneity of eWOM valence. To some extent, our measure of valence equality also captures the valence heterogeneity of eWOM. However, it is applied towards eWOM that are hosted by different types of platforms, instead of a single platform. In addition, we adopt a more robust measure, i.e., entropy, than the sta tistic of variance used in prior studies to remove the measure’s inde pendence on valence. Therefore, valence equality in our work has a distinct value from the metric of valance variance in the literature, complementing this line of research.

Table 1  
Comparison with Most Relevant eWOM Studies

<table><tr><td rowspan="2">Literature</td><td rowspan="2">Multiple platforms</td><td rowspan="2">Volume equality across the platforms</td><td colspan="2">Valence equality</td><td rowspan="2">Product/Service</td><td rowspan="2">Related focus</td></tr><tr><td>Within platform</td><td>Across platforms</td></tr><tr><td>Chevalier &amp; Mayzlin [10]</td><td>Y</td><td></td><td></td><td></td><td>Book</td><td>A difference-in-difference approach to study the sales impact of online user reviews.</td></tr><tr><td>Moon et al. [40]</td><td>Y</td><td></td><td></td><td></td><td>Movie</td><td>The dynamics between eWOM, including professional and user reviews, and product financial performance.</td></tr><tr><td>Gu et al. [22]</td><td>Y</td><td></td><td></td><td></td><td>Camera</td><td>Compare the magnitude of the impact of Amazon eWOM with eWOM from three review platforms.</td></tr><tr><td>Zhou &amp; Duan [54]</td><td>Y</td><td></td><td></td><td></td><td>Software</td><td>The moderation effect of eWOM hosted by the review platform on the sales impact of retailer-hosted eWOM.</td></tr><tr><td>Phillips et al. (2015)</td><td>Y</td><td></td><td></td><td></td><td>Hotel</td><td>The explanatory power on hotel performance from the total number of reviews and the percentage of positive reviews based on a pooled review data set from 69 online resources.</td></tr><tr><td>Godes &amp; Mayzlin [19]</td><td>Y</td><td>Y</td><td></td><td></td><td>TV show</td><td>The impact of volume entropy across Usenet newsgroups.</td></tr><tr><td>Zhu &amp; Zhang [56]</td><td></td><td></td><td>Y</td><td></td><td>Video game</td><td>The moderation effect of contextual factors on eWOM metrics, one of which is rating variance within the platform.</td></tr><tr><td>Sun [48]</td><td>Y</td><td></td><td>Y</td><td></td><td>Book</td><td>The impact of rating variance within the platform on online consumer decisions.</td></tr><tr><td>Rosario et al. [44]</td><td>Y</td><td></td><td>Y</td><td></td><td>Various</td><td>A meta-analysis of over 96 prior studies synthesizes different platform characteristics, product characteristics, and eWOM metrics.</td></tr><tr><td>Figini et al. [16]</td><td>Y</td><td></td><td>Y</td><td></td><td>Hotel</td><td>Compare the rating variance between verified and non-verified review hosting platforms</td></tr><tr><td>This study</td><td>Y</td><td>Y</td><td></td><td>Y</td><td>Software</td><td>The impact of volume equality and valence equality across retail and review platforms.</td></tr></table>

In Table 1, we highlight the distinctive features and advantages of the current study compared with the most relevant eWOM literature.

## 2.2. Research Hypotheses

In online platforms, people frequently resort to user-generated eWOM as one of the major and trustworthy sources to research prod uct features and quality without physical trials. Therefore, eWOM is generally believed to influence online user decisions of adopting prod ucts/services [10, 12, 13, 19, 24, 34]. At retail platforms, online user decisions of adopting a product are cumulatively captured by the retail sales of the product; at third-party platforms that offer free trials, online user decisions of adopting a product are generally defined as the total number of free trials experienced by the users. Among all the eWOM metrics, the most widely studied is the total volume of eWOM. It refers to the overall amount of user discussions accumulated at platforms. Prior studies have identified its informational role in indicating consumer awareness [34]. Specifically, a larger volume signals more active user discussions on the product, helping attract more people to notice the product. Being aware of the product is the first step in the decision-making of adopting a product. As a result, the total volume of eWOM has a positive impact on online user decisions. We proposed that volume equality across the platform, as a new measure of eWOM volume, captures the heterogeneity of users being aware of the product, based on Godes and Mayzlin’s application of social tie theory in an online com munity (2004). We will develop our arguments in detail in the following paragraphs.

Based on social tie theory [21], Godes and Mayzlin [19] interpreted the volume entropy of eWOM across the Usenet newsgroup as an indi cator of product awareness of diverse consumers. Social tie theory cat egorizes different relationships between people as either strong ties or weak ties. People who have strong ties among them are generally within groups and homogeneous; people between groups are more heteroge neous and thus have weak ties among them. Information spreads more quickly through strong ties than weak ties [21]. By applying this well-known theory in online communities, Godes and Mayzlin pointed out that each newsgroup is an individual online community (2004). Users of multiple newsgroups are thus heterogeneous and are connected with weak ties, while users of the same newsgroup are generally ho mogeneous and have strong ties among them. Accordingly, it is a lot easier for users to learn about the television show from those within the same newsgroup through strong ties than from those in different newsgroups through weak ties. This leads to the authors’ claim that conditional on the total volume of user discussions if more diverse users from different newsgroups are aware of the television show, user dis cussions about this television show should be more equally taking place in those newsgroups. This argument is supported by their empirical findings that the volume entropy of eWOM across Usenet newsgroups has a positive impact on user decisions about television shows.

Following Godes and Mayzlin’s (2004) theoretical development, it is the weak social tie that connects people from the retail platform and people from the review platform. Online retail and review platforms host two different user groups, similar to multiple Usenet newsgroups in Godes and Mayzline’s work (2004). The distinction between them can even be greater than the distinction between Usenet newsgroups, given that newsgroups are essentially instances of the same community type and retail and reviews platforms are not of the same type [44]. A retail platform mainly provides an online commercial channel for users to purchase products, whereas a review platform focuses on fostering active user feedback, providing expert opinions, offering free samples, etc. without direct selling. Because of such differences in platform’s service purposes, users of those two platforms can vary considerably, thereby having weak ties between them.

Given the weak ties among users of retail and review platforms, users are more easily aware of the product through eWOM generated at their own platforms than through eWOM generated at the other platforms. When more diverse users from both retail and review platforms are aware of the product, eWOM conservations are expected to occur more equally at those platforms, conditional on the total volume of eWOM. We define greater volume equality to describe the scenario where online user conversations on a product are more equally disseminated across platforms. As a result, volume equality captures the heterogeneity of users being aware of the product. Since user awareness of a product is a necessary condition for choosing the product, we expect that it is beneficial to have more diverse users being aware of the product, captured by greater volume equality across platforms. We propose our first hypothesis as below:

H1: Greater volume equality of eWOM across retail and review platforms has a positive impact on online users’ product adoption decisions. eWOM valence reflects users’ average evaluation of their product experiences. Smaller valence equality in this study refers to a large disagreement in product experiences between users of retail and review platforms. Prior studies suggest that evaluative disagreement regarding product information would deliver ambivalence in con sumers’ attitudes towards the corresponding products [25, 41, 42]. Faced with disagreeing information, consumers would generally try to reconcile the information and achieve an integrated evaluation of their own [23, 39, 46]. Therefore, smaller valence equality either turns away potential users for being overwhelmed with inconsistent product eval uations or poses higher cognitive costs for online users to process the inconsistency. Neither case is favorable to online users for making their adoption decisions. Therefore, we propose:

H2: Greater valence equality of eWOM across retail and review platforms has a positive impact on online users’ product adoption decisions.

Volume equality can further strengthen the positive impact of valence equality on online user decisions to adopt products. Let’s compare two hypothetical scenarios with distinct levels of volume equality yet with the same low level of valence equality, e.g., 5-star average valence from one platform, and 1-star average valence from the other platform. H2 suggests that such low valence equality dis courages user decisions. In the first scenario, conditional on the total volume of eWOM across platforms, the product receives eWOM with an equal split in volume at two platforms. In the second scenario, the product has much lower volume equality across platforms that it re ceives the majority of eWOM from one platform and a very small number of eWOM from the other platform. Although the valence equality is at the same low level in both scenarios, online users find the first scenario more difficult to reconcile such polarized opinions in equal amount at each platform and arrive at their evaluations. Instead, in the second scenario, a disproportionately large amount of eWOM at one platform dominates. Greater volume equality increases the cognitive costs for online users to process different user opinions across platforms, thereby magnifying the negative impact of low valence equality. In other words, volume equality and valence equality have a positive interaction effect on online user decisions

H3: There is a positive interaction effect between volume equality and valence equality on online users’ product adoption decisions.

## 3. Data

## 3.1. Research Context

We conducted our empirical analysis in the online software market by using data from Amazon and CNETD. In recent years, the product variety of software programs offered through the online channel has been increasing tremendously [53]. Consumers often face difficulties with evaluating software quality before consumption. Meanwhile, con sumers who intend to adopt software programs generally have technical knowledge and experience in accessing multiple platforms. This makes the online software market an appropriate context to study the impact of platform concentration of eWOM on online user decisions of adopting products.

We constructed a weekly data set of observations on bestselling software programs hosted by both Amazon and CNETD from June 2011 through January 2012. Amazon is one of the leading online retailers and has been widely chosen by previous researchers to examine online market outcomes [10, 18, 22]. We also collected weekly eWOM data of the same software programs hosted by CNETD. CNETD is a representa tive review platform notable for its large collection of user-generated eWOM and expert opinions on software programs. Being different from a retail platform like Amazon, CNETD does not sell software pro grams. Instead, it provides free and free-to-try software sampling on four system platforms, namely Windows, Mac, mobile devices, and webware, to encourage users to experience products and share feedback. As a well-known review platform hosting software information, CNETD is often displayed at the top of search results when online consumers use search engines to look for software program information. Many expe rienced software consumers also directly resort to CNETD as a reliable source for software information.

We implemented a two-stage matching process by using CNETD’s search functionality as well as a manual check. In the initial round, for each collected Amazon software program, every week we searched the exact software name using the search function on the CNETD homepage and collected data on the first 50 most relevant CNETD software pro grams of the search results. Accordingly, one Amazon software program has 50 candidates for its matched CNETD product. However, the algo rithm of the CNETD search function cannot assure that the highest po sition in the search results is precisely matched to the collected Amazon software program. Several software program suppliers on Amazon may not even upload the free-trial versions to CNETD. Therefore, as a second step, we conducted a manual screening on the first-week data over those approximately matched pairs collected from Amazon and CNETD. We chose only one out of 50 possibly matched CNETD software programs as the precise match to each collected Amazon software program, if any. From the first-week data, we extracted 43 Amazon software programs with their exactly matched CNETD products. We then kept only the observations on those 43 pairs from the originally collected Amazon and CNETD samples<sup>2</sup>. This matching process helped us obtain high-quality data with moderate efforts and led to a dataset of 43 software pro grams over 33 weeks for the empirical analysis.

Specifically, we collected the following data from Amazon on a weekly basis, including sales rank, the number of online consumer re views, average consumer rating, price, release date, eligibility for free shipping service, and software category for each software program. On the same date of each week, we also collected the total number of online user reviews, average user rating, and weekly and overall downloads fo the matched software program on CNETD.

## 3.2. Variables

This study attempts to investigate the impact of the platform con centration of eWOM on online users’ decisions to adopt products. In the retail context, sales data, an ideal outcome measure for online purchase decisions, are generally not open to the public and are inaccessible in our study as well. Alternatively, we follow the literature to use Amazon sales rank as the proxy for Amazon sales. Prior studies have widely applied the log-linear relationship between Amazon sales and sales rank to infer online market outcomes [8, 10, 18, 22]. Ghose and Sundrararajan [18] designed an experiment on the Amazon software market and provided an empirical estimation on the negative linear relationship between log value of sales rank and log value of sales as ΔLn(AmazonSales)=0.828\* [-ΔLn(AmazonSalesRank)]. We thus adopt their finding to use Amazon sales rank with a negative log transformation to approximately measure the log value of actual sales. On CNETD, we follow the prior studies to adopt weekly software downloads, $C n e t d D o w n _ { i , t } ,$ as the outcome variable to capture user downloading decisions at the software review platform [14].

One of the key independent variables is the volume equality of eWOM. Following Godes and Mayzlin’s study (2004), we use entropy to measure volume equality $( V o l E q u a l i t y _ { i , t } ) .$ . In this context, volume equality of eWOM captures the level to which Amazon and CNETD equally host eWOM conversations in volume. We follow the literature to use the number of online user reviews in platform j to measure its eWOM volume $\begin{array} { r } { ( V o l _ { i , t } j ) \ [ 1 4 ] , } \end{array}$ , where j denotes each platform $( \mathrm { i } . \mathrm { e } . , A$ for Amazon and C for CNETD). Accordingly, the total eWOM volume of those two websites $( T o t a l V o l _ { i , t } )$ is simply the summation of eWOM volume from each platform. Applying entropy calculation in our context thus leads to the measure of our VolEqaulity as below:

$$
V o l E q u a l i t y _ {i, t} = \left\{ \begin{array}{c c} - \sum_ {j} \frac {V o l _ {i , t} ^ {j}}{\text { TotalVol } _ {i , t}} \ln \left(\frac {V o l _ {i , t} ^ {j}}{\text { TotalVol } _ {i , t}}\right) & \text { if   both   Vol } _ {i, t} ^ {A} \text {   and   Vol } _ {i, t} ^ {C} > 0 \\ 0 & \text { if   Vol } _ {i, t} ^ {A} \text {   or   Vol } _ {i, t} ^ {C} = 0 \end{array} \right.\tag{1}
$$

The entropy of volume mainly depends on the ratio of eWOM vol umes among different platforms as shown by the above $\operatorname { E q . } ( 1 )$ . Unlike variance, entropy does not depend on the total volume of online user reviews at Amazon and CNETD $( T o t a l V o l _ { i , t } )$ , which will be included as a control variable in our following empirical analysis. Therefore, using entropy to make volume equality independent of $\boldsymbol { T o t a l V o l } _ { i , t }$ helps cope with the multicollinearity issue and provides robust model examinations.

The larger value of $V o l E q u a l i t y _ { i , t }$ indicates a higher degree of equality in review volume on the given product contributed to by Amazon and CNETD. This implies that reviews are less concentrated towards any individual platform in terms of volume. For example, if product i re ceives the same volume of user reviews on Amazon and CNETD, VolE $q a u l i t y _ { i , t }$ reaches its maximum value, 0.693 in the two-platform case. If this product is reviewed eight times more at one website than the other, $V o l E q a u l i t y _ { i , t }$ is lowered to 0.325. When software program i receives all its user reviews on a single platform, VolEqaulity reaches the minimum value, zero, i.e. the lowest level of volume equality. In addition, if a

$$
V a l E q u a l i t y _ {i, t} = \left\{ \begin{array}{c l} - \sum_ {j} \frac {V a l _ {i , t} ^ {j}}{V a l _ {i , t} ^ {A} + V a l _ {i , t} ^ {C}} \ln \left(\frac {V a l _ {i , t} ^ {j}}{V a l _ {i , t} ^ {A} + V a l _ {i , t} ^ {C}}\right) & \text { if   both } V a l _ {i, t} ^ {A} \text { and } V a l _ {i, t} ^ {C} \text { are   available } \\ 0 & \text { if } V a l _ {i, t} ^ {A} \text { or } V a l _ {i, t} ^ {C} \text { is   not   available } \end{array} \right.
$$

software program is not reviewed on any site, the platform concentra tion of eWOM does not exist at all. Thus, our final data set will exclude this kind of product.

The other main independent variable is the valence equality of eWOM. It captures the extent to which users of Amazon and CNETD express consistent overall opinions. We use average rating as the eWOM valence for each platform $( V a l _ { i , t } j ) [ 1 3 ]$ , where j denotes each platform. Due to the same reason, the entropy of valence is more appropriate than variance to measure valence equality of eWOM (ValEquality ). Specif ically, the advantage of entropy over variance allows us to safely include the average consumer evaluation over Amazon and CNETD, Mean Rating , measured by $( V a l _ { i , t } ^ { \ A } + V a l _ { i , t } ^ { \ C } ) / 2$ , as a control variable [10]. As one of the contributions of this paper, we include MeanRating as the valence measure in our models to shed light on mixed conclusions regarding eWOM valence in earlier studies. Its impact is compared with that of valence equality. Several prior studies find evidence that eWOM valence influences consumer decisions ([17]; Teng et al., 2017; [50,

Table 2  
Description of Key Variables

<table><tr><td>Variables</td><td>Descriptions</td></tr><tr><td> $AmazonSalesRank_{i,t}$ </td><td>Sales rank of software  $i$  at week  $t$  at Amazon</td></tr><tr><td> $CnetdDown_{i,t}$ </td><td>Weekly number of downloads of software  $i$  at week  $t$  at CNETD</td></tr><tr><td> $TotalVol_{i,t}$ </td><td>Total number of Amazon and CNETD reviews software  $\underline{i}$  receives at week  $t$ </td></tr><tr><td> $VolEquality_{i,t}$ </td><td>Volume equality over Amazon and CNETD reviews of software  $i$  at week  $t$ </td></tr><tr><td> $ValEquality_{i,t}$ </td><td>Valence equality over Amazon and CNETD reviews of software  $i$  at week  $t$ </td></tr><tr><td> $DummyVol_{i,t}$ </td><td>A dummy variable measuring whether software  $i$  receives more reviews at week  $t$  at Amazon than at CNETD</td></tr><tr><td> $MeanRating_{i,t}$ </td><td>Mean value of Amazon and CNETD average ratings of software  $i$  at week  $t$ </td></tr><tr><td> $Age_{i,t}$ </td><td>Days since Amazon has released software  $i$  by week  $t$ </td></tr><tr><td> $AmazonPrice_{i,t}$ </td><td>Price offered by Amazon for software  $i$  at week  $t$ </td></tr><tr><td> $CnetdLicense_{i,t}$ </td><td>A dummy variable measuring whether software  $i$  is free with limited functionalities at week  $t$  at CNETD</td></tr></table>

Summary Statistics of Key Variables

<table><tr><td></td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td> $AmazonSalesRank_{i,t}$ </td><td>45</td><td>28</td><td>1</td><td>100</td></tr><tr><td> $VolEquality_{i,t}$ </td><td>0.280</td><td>0.239</td><td>0</td><td>0.693</td></tr><tr><td> $ValEquality_{i,t}$ </td><td>0.525</td><td>0.283</td><td>0</td><td>0.693</td></tr><tr><td> $TotalVol_{i,t}$ </td><td>357</td><td>547</td><td>10</td><td>5109</td></tr><tr><td> $DummyVol_{i,t}$ </td><td>0.782</td><td>0.413</td><td>0</td><td>1</td></tr><tr><td> $MeanRating_{i,t}$ </td><td>3.342</td><td>0.730</td><td>1.400</td><td>4.800</td></tr><tr><td> $Age_{i,t}$ </td><td>731</td><td>589</td><td>151</td><td>3042</td></tr><tr><td> $AmazonPrice_{i,t}$ </td><td>62.644</td><td>58.447</td><td>0</td><td>249.980</td></tr><tr><td> $CnetdDown_{i,t}$ </td><td>7993</td><td>4391</td><td>0</td><td>47895</td></tr><tr><td> $CnetdLicense_{i,t}$ </td><td>0.047</td><td>0.211</td><td>0</td><td>1</td></tr></table>

53]). On the contrary, other studies report the irrelevance of online user ratings to user choices [5, 14, 34].

Given the statistical attributes of entropy, a larger entropy value denotes greater valence equality of eWOM across platforms. The full calculation of ValEquality is illustrated below.

(2)

ValEquality reaches its maximum value of 0.693, when the average user rating of product i on Amazon equals its CNETD average rating, indicating the greatest valence equality.

In addition, we also include Amazon product prices, product age, whether Amazon receives more reviews than CNETD, download license, product fixed effect, and time fixed effect as control variables [10, 31, 54]. Table 2 describes the key variables used in our empirical analysis, and Table 3 presents the summary statistics for these variables. We find that, in any week of the data collection period, all products were at least reviewed by one of the two sites, if not both, as indicated by the mini mum value of Total $V o l _ { i , t }$ being greater than 0 in Table 3. Therefore, all samples in our data set can be used properly to capture the platform concentration of eWOM. Table 3 also shows that online user reviews are far from being equally distributed over Amazon and CNETD in both volume and valence. For instance, the mean value of VolEquality indicates that, on average, products receive user reviews at one platform about ten times as often as at another platform. The mean statistic of Dummy $V o l _ { i , t }$ further shows that nearly 80% of the software programs receive more user reviews on Amazon than on CNETD.

## 4. Empirical Analysis

To test our proposed hypotheses, we develop a series of models, each of which will be presented below.

## 4.1. Base Model

We start with the following Base Model of Ordinary Lease Square regression to explore the sales impact of key independent variables on Amazon and collect initial evidence to study the platform concentration of eWOM across platforms. Specifically, we estimate the following model to test our hypotheses:

$$
\begin{array}{l} - L n \left(A m a z o n S a l e s R a n k _ {i, t}\right) \\ = \beta_ {0} + \beta_ {1} * V o l E q u a l i t y _ {i, t} + \beta_ {2} * V a l E q u a l i t y _ {i, t} + \beta_ {3} * V a l E q u a l i t y _ {i, t} * V o l E q u a l i t y _ {i, t} \\ + \beta_ {4} * L n \left(T o t a l V o l _ {i, t}\right) + \beta_ {5} * D u m m y V o l _ {i, t} + \beta_ {6} * M e a n R a t i n g _ {i, t} + \beta_ {\mathrm{x}} * C o n t r l _ {i, t} ^ {A, x} + \mu_ {i} + \rho_ {t} + \varepsilon_ {i, t} \end{array}
$$

We use -Ln(AmazonSalesRank ) as the dependent variable that measures the negative log value of Amazon sales rank of product i at week t. As introduced earlier, given the negative log-linear relationship between the sales rank and sales, this model can estimate the sales impact of independent variables. We first include $V o l E q u a l i t y _ { i , t }$ and $V a l E q u a l i t y _ { i , i }$ to test H1 and H2, respectively. Accordingly, the coefficient on $V o l E q u a l i t y _ { i , t } \left( \beta _ { 1 } \right)$ captures the sales impact of volume equality, and the coefficient on ValEquality $\cdot \left( \beta _ { 2 } \right)$ captures the sales impact of valence equality of eWOM across Amazon and CNETD. According to H1 and ${ \mathrm { H } } 2 ,$ those two coefficients $( \beta _ { 1 } , \beta _ { 2 } )$ are expected to be positive. H3 suggests a positive interplay between volume equality and valence equality so that as free sampling has been shown to influence online sales [47, 54]. CnetdLicense is a dummy variable to indicate the license difference of CNETD software [30, 53]. Finally, we include product fixed effects $\mu _ { i }$ and time fixed effects ρ to control for time-invariant product hetero geneity, such as products’ idiosyncratic characteristics and intrinsic quality, and other omitted time-variant variables, respectively [13]. Rather than using product-specific dummies, we choose to use 27 category-specific dummies to represent product fixed effects. Our sam ple consists of 665 observations on 43 software programs. Including 42 product-specific dummies would significantly reduce the degree of freedom for estimating the above equation, leading to low statistical power and incorrect insignificant estimations. Instead, we use category differences to approximately capture the time-invariant product differ ences. Amazon applies a very detailed categorization on its listed soft ware programs. For instance, those 43 software programs belong to 28 distinct categories. Therefore, we believe that category-specific dummies can well reflect those uncaptured product attributes,

(3)

enabling us to efficiently estimate the regression model in the meantime. To control for the time fixed effect, we add 32-week dummies $\rho _ { t }$ in the equation to capture the common demand shocks $( \mathbf { e . g . }$ , web site-wide promotion event).

## 4.2. CNETD Model

Our hypotheses suggest that the platform concentration of eWOM should also affect online user decisions of downloading CNETD free-trial software. Following this inference, we estimate the model below and expect to observe results on key independent variables similar to those from the above Base Model.

$$
\begin{array}{l} L n \big (C n e t d D o w n _ {i, t} \big) = \alpha_ {0} + \alpha_ {1} * V o l E q u a l i t y _ {i, t} + \alpha_ {2} * V a l E q u a l i t y _ {i, t} + \alpha_ {3} * V a l E q u a l i t y _ {i, t} * \\ V o l E q u a l i t y _ {i, t} + \alpha_ {4} * L n \big (T o t a l V o l _ {i, t} \big) + \alpha_ {5} * D u m m y V o l _ {i, t} + \alpha_ {6} * M e a n R a t i n g _ {i, t} + \alpha_ {x} * C o n t r l _ {i, t} ^ {C, x} + \sigma_ {i} + \tau_ {t} + \in_ {i, t} \end{array}\tag{4}
$$

the impact of valence equality is strengthened by volume equality. Therefore, we include an interaction term, $\beta _ { 3 } ^ { * } V a l E q u a l i t y _ { i , t } ^ { * }$ VolEquality<sub>i,</sub> , and expect to observe a positive estimation of $\beta _ { 3 } .$

We also include three other eWOM-related independent variables. We first add $T o t a l V o l _ { i , t } \left( \beta _ { 4 } \right)$ with a log transformation to represent the total number of Amazon and CNETD user reviews on software i by week t. As discussed earlier, H1 is proposed conditional on total volume $( T o t a l V o l _ { i , t } ) ,$ , i.e., the overall size of user populations who may become aware of the product. $D u m m y V o l _ { i , t } \left( \beta _ { 5 } \right)$ is included to take account of whether having more eWOM activities on Amazon than on CNETD im pacts Amazon sales. We also include MeanRating to measure the mean of Amazon and CNETD average user ratings. Its coefficient (β ) thus controls for the sales impact of average consumer evaluation from Amazon and CNETD.

We include several additional control variables indicated by Contrl $_ t ^ { A , x }$ in Eq. (3). Specifically, we include product age $A g e _ { i , t }$ to control fo product diffusion [14]. We also control for price effect by AmazonPrice of software i at week t [12]. In addition, we add the log value of weekly downloads LnCnetdDown that software i receives at week t at CNETD,

The dependent variable is changed to CNETD weekly downloads with an applied log transformation. This captures online user decisions of adopting free or free-to-try software programs at CNETD. All of the key independent variables are the same as presented in $\operatorname { E q . } ( 3 )$ ). Control variables are modified as $C o n t r l _ { i , t } C , ^ x$ We keep three control variables from the Base Model, product age $( A g e _ { i , t } ) _ { : }$ , product price $( A m a z o n P r i c e _ { i , t } ) ,$ and the dummy variable $C n e t d L i c e n s e _ { i , t } .$ . We also add two new control variables into $C o n t r l _ { i , t } C , ^ x$ . The negative value of Amazon sales rank, -Ln $( A m a z o n S a l e s R a n k _ { i , t } ) ,$ , is added to replace CNETD weekly downloads in Eq.(3). We include CNETD total downloads, Ln(CnetdTotalDow $\iota _ { i , t } ) .$ , to control for the network effect [14].

## 4.3. Week-Lagged Model

In this subsection, we specifically look into possible endogeneity is sues in the Base Model. In particular, we check two common endoge neity issues in this line of research: unobserved omitted variables, e.g., product quality, and simultaneity.

Table 4 Base Model Estimations

<table><tr><td></td><td>Model W/O eWOM platform concentration</td><td>Base Model (with eWOM platform concentration)</td></tr><tr><td>Intercept</td><td>-3.817***</td><td>-4.595***</td></tr><tr><td> $VolEquality_{i,t}$ </td><td></td><td>17.759***</td></tr><tr><td> $ValEquality_{i,t}$ </td><td></td><td>1.735***</td></tr><tr><td> $ValEquality_{i,t} * VolEquality_{i,t}$ </td><td></td><td>26.816***</td></tr><tr><td> $Ln(TotalVol_{i,t})$ </td><td>0.340***</td><td>0.2292***</td></tr><tr><td> $DummyVol_{i,t}$ </td><td>0.605***</td><td>0.604***</td></tr><tr><td> $MeanRating_{i,t}$ </td><td>-0.248**</td><td>-0.187</td></tr><tr><td> $Contrl_{i,t}^{A,x}$ </td><td></td><td></td></tr><tr><td> $Age_{i,t}$ </td><td>-0.001***</td><td>-0.001***</td></tr><tr><td> $AmazonPrice_{i,t}$ </td><td>0.002</td><td>-0.001</td></tr><tr><td> $Ln(CnetdDown_{i,t})$ </td><td>-0.056***</td><td>-0.210***</td></tr><tr><td> $CnetdLicense_{i,t}$ </td><td>-1.558***</td><td>-2.686***</td></tr><tr><td>Product fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>665</td><td>665</td></tr><tr><td> $R^2$ </td><td>0.642</td><td>0.667</td></tr><tr><td>***p&lt;0.01</td><td></td><td></td></tr></table>

Unobserved product quality can potentially cause the correlation between the error term and the independent variables. In the Base Model in Eq. (3), one of the independent variables is the average value of Amazon and CNETD ratings (MeanRating ), which has been used by prior studies to reflect product quality [26, 34, 43]. Therefore, this variable poses the risk of correlating with the error term if product quality is not fully controlled for by other independent variables and left in the error term. This concern is addressed through three different approaches. First, weekly software downloads in the control variables of our Eq. (3), Ln(CnetdDown ), help control for product quality. A frequently downloaded product tends to have superior quality. Another assurance in Eq. (3) resides in category-specific dummies, which can control for intrinsic product characteristics, including product quality difference. Third, we take a more formal approach by running Durbin, Hausman, and Wu specification test. In doing so, we must remove all those dummies in Eq.(3). Otherwise, the overwhelming number of in dependent variables will cause the under-identification of instrumental variables. We will report this test result in the next section.

Regarding the endogeneity issue caused by simultaneity, we address this concern through the below week-lagged model and the Seemingly Unrelated Model (SUR) explained in the next subsection. Prior studies have shown eWOM volume being the sales influencer and at the same time being the sales outcome [10]. In essence, there is a loop of causality between eWOM volume and sales. In the current study, it implies that the total review volume from CNETD and Amazon at week t, Ln(Total $V o l _ { i , t } ) ,$ as an independent variable in the Base Model Eq. (3), can be partly determined by the dependent variable, sales rank, at the same week t. To address the dual role of total volume, we first follow the literature [10] to use a one-week lag in this total volume variable and all the rest of eWOM-related independent variables. By doing so, the time lag assures that the sales, which are proxied by the dependent variable -Ln(AmazonSalesRank<sub>i,t</sub>), cannot affect either of those eWOM-related variables. To estimate this model specification, we exclude observa tions of software programs that only appear in one standalone week and can include 536 observations for this week-lagged model. Those 536 observations still account for the majority of the original samples, more than 80% of all the original observations. Accordingly, this week-lagged model is specified as below:

$$
\begin{array}{l} - L n \left(A m a z o n S a l e s R a n k _ {i, t}\right) = \\ \mu_ {0} + \mu_ {1} * V o l E q u a l i t y _ {i, t - 1} + \mu_ {2} * V a l E q u a l i t y _ {i, t - 1} + \mu_ {3} * V a l E q u a l i t y _ {i, t - 1} \\ * V o l E q u a l i t y _ {i, t - 1} + \mu_ {4} * L n \left(T o t a l V o l _ {i, t - 1}\right) + \mu_ {5} * D u m m y V o l _ {i, t - 1} \\ + \mu_ {6} * M e a n R a t i n g _ {i, t - 1} + \mu_ {x} * C o n t r l _ {i, t} ^ {C, x} + \pi_ {i} + \nu_ {t} + \xi_ {i, t} \end{array}\tag{5}
$$

The second approach to deal with the simultaneity is to adopt a more advanced SUR model, which is explained in the next subsection.

## 4.4. SUR Model

Here we propose our final model that brings the Base Model in $\operatorname { E q . } ( 3 )$ and CNETD Model in Eq.(4) together as a model system specified in Eqs. (6) and (7) shown below. In addition, we estimate it as a SUR. The Base Model captures the impact of eWOM platform concentration on Amazon sales rank and is thus adapted to as Amazon Eq. in this SUR Model. Similarly, Eq.(7) is referred to as CNETD Equation. We allow error terms of Amazon Equation (ε ) and CNETD Equation’s ( ) to be correlated. This setting helps address the concern on simultaneity and account for unknown factors that affect user decisions on both Amazon and CNETD. This SUR model not only provides efficient estimations but also best presents the spirit of our hypotheses: platform concentration of eWOM affects online user decisions of adopting products. This impact is not limited to the retail website only.

Amazon Equation

Table 5 Full Model Estimations

<table><tr><td></td><td>CNETD Model</td><td>Week-Lagged Model</td><td>SUR ModelAmazon Equation</td><td>CNETD Equation</td></tr><tr><td>Intercept</td><td>-5.481***</td><td>-4.167***</td><td>-4.930***</td><td>-5.802***</td></tr><tr><td> $VolEquality_{i,t}$ </td><td>24.437***</td><td>10.437***</td><td>22.142***</td><td>25.885***</td></tr><tr><td> $ValEquality_{i,t} *VolEquality_{i,t}$ </td><td>36.14***</td><td>16.661**</td><td>32.826***</td><td>38.290***</td></tr><tr><td> $ValEquality_{i,t}$ </td><td>1.395***</td><td>1.403***</td><td>2.390***</td><td>1.590***</td></tr><tr><td> $LnTotalVol_{i,t}$ </td><td>0.082**</td><td>0.223***</td><td>0.325***</td><td>0.112***</td></tr><tr><td> $DummyVol_{i,t}$ </td><td>-0.132</td><td>0.604***</td><td>0.540***</td><td>-0.073</td></tr><tr><td> $MeanRating_{i,t}$ </td><td>0.678</td><td>-0.045</td><td>-0.325</td><td>0.690</td></tr><tr><td>Control Variables</td><td> $Contrl_{i,t}^{C,x}$ </td><td> $Contrl_{i,t}^{A,x}$ </td><td> $Contrl_{i,t}^{A,x}$ </td><td> $Contrl_{i,t}^{C,x}$ </td></tr><tr><td> $Age_{i,t}$ </td><td>0.001***</td><td>-0.001***</td><td>-0.001***</td><td>0.001***</td></tr><tr><td> $AmazonPrice_{i,t}$ </td><td>0.002**</td><td>-0.001</td><td>-0.002</td><td>0.002***</td></tr><tr><td> $-Ln(AmazonSalesRank_{i,t})$ </td><td>0.034</td><td></td><td></td><td>0.133***</td></tr><tr><td> $Ln(CnetdDown_{i,t})$ </td><td></td><td>-0.122***</td><td>-0.314***</td><td></td></tr><tr><td> $CnetdLicense_{i,t}$ </td><td>-0.097</td><td>-2.623***</td><td>-2.773***</td><td>-0.371</td></tr><tr><td> $Ln(CnetdTotalDown_{i,t})$ </td><td>0.629***</td><td></td><td></td><td>0.610***</td></tr><tr><td>Product fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td></td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td></td></tr><tr><td>Observations</td><td>665</td><td>536</td><td>665</td><td></td></tr><tr><td>R2</td><td>0.980</td><td>0.662</td><td>0.963</td><td></td></tr><tr><td></td><td></td><td></td><td colspan="2">Cross-model correlation: 0.145</td></tr></table>

\*\*p<0.05; \*\*\*p <0.01

![](/api/attachments/GSCJUS39/fulltext/images/e2b1f8c5a28e494f7f2218c84e7e05ec25317815f11aa69186ec1607905c413b.jpg)  
Fig. 1. The Total Impact of Decreasing Valence Equality. Note: The decrease in product adoptions is caused by decreasing valence equality from 0.693 (receiving the same average rating on two sites) to 0.673 (receiving a 2-star and a 3-star average rating on two sites respectively).

CNETD Equation

coefficient on the interaction term ValEquality \* VolEquality in col umn (2) is also significantly positive, supporting H3. Volume equality

$$
\begin{array}{l} - L n \big (A m a z o n S a l e s R a n k _ {i, t} \big) \\ = \beta_ {0} + \beta_ {1} * V o l E q u a l i t y _ {i, t} + \beta_ {2} * V a l E q u a l i t y _ {i, t} + \beta_ {3} * V a l E q u a l i t y _ {i, t} * V o l E q u a l i t y _ {i, t} \\ + \beta_ {3} * V a l E q u a l i t y _ {i, t} * V o l E q u a l i t y _ {i, t} + \beta_ {4} * L n \big (T o t a l V o l _ {i, t} \big) + \beta_ {5} * D u m m y V o l _ {i, t} + \beta_ {6} * M e a n R a t i n g _ {i, t} + \beta_ {\mathrm{x}} * C o n t r i t _ {i, t} ^ {A, x} \\ + \mu_ {i} + \rho_ {t} + \varepsilon_ {i, t} \end{array}\tag{6}
$$

$$
\begin{array}{l} L n \big (C n e t d D o w n _ {i, t} \big) = \alpha_ {0} + \alpha_ {1} * V o l E q u a l i t y _ {i, t} + \alpha_ {2} * V a l E q u a l i t y _ {i, t} + \alpha_ {3} * \\ V a l E q u a l i t y _ {i, t} * V o l E q u a l i t y _ {i, t} + \alpha_ {4} * L n \big (T o t a l V o l _ {i, t} \big) + \alpha_ {5} * D u m m y V o l _ {i, t} + \\ \alpha_ {6} * M e a n R a t i n g _ {i, t} + \alpha_ {x} * C o n t r l _ {i, t} ^ {C, x} + \sigma_ {i} + \tau_ {t} + \in_ {i, t} \end{array}\tag{7}
$$

, Where $\varepsilon _ { i , t }$ and $\in _ { i , t }$ are correlated; Contr $\cdot l _ { i , t } ^ { A , \ x }$ include $A g e _ { i , t }$ AmazonPri ${ \bf \dot { \varepsilon } } e _ { i , t } ,$ Ln(CnetdDown ), and CnetdLicense , Cont $\cdot l _ { i , t } ^ { C , \ x }$ include $A g e _ { i , t }$ AmazonPri $\boldsymbol { \mathbf { \rho } } _ { i , t }$ CnetdLicense , Ln(AmazonSalesRan $\begin{array} { r } { \dot { \bf c } _ { i , t } \partial , } \end{array}$ , and Ln(CnetdTo talDown ).

## 5. Results

## 5.1. Base Model Estimation

Table 4 summarizes the estimation results of the Base Model in Eq. (3). To highlight the contribution of eWOM platform concentration to online retail sales, we compare two specifications. As shown in the first column of Table 4, we estimate a model that removes metrics related to platform concentration from the Base Model. Specifically, the model in the first column only includes three commonly used eWOM measures: the total volume of eWOM from Amazon and CNETD, whether Amazon receives more eWOM, and the mean of Amazon and CNETD eWOM valence. The second column of Table 4, on the other hand, presents the estimations of our Base Model that adds key metrics of platform con centration of eWOM: volume equality and valence equality.

Overall, the estimation results of the Base Model summarized in Table 4 support all three hypotheses. Both coefficients on VolEquality and $V a l E q u a l i t y _ { i , t }$ in column (2) are significantly positive. H1 and H2 are thus supported that the platform concentration of eWOM makes a dif ference in users’ decisions to adopt products. Better equality in both volume and valence is associated with greater Amazon sales. The strengthens the impact of valence equality. The impact of valence equality is even more positive when receiving a comparable number of user reviews on each site than receiving a varying number of reviews on each site. In other words, when online consumers face more divergent opinions across sites, having an equal volume of eWOM on each site makes this decrease of valence equality discourage product adoption decisions to a greater degree than having most eWOM occurred at a single site.

In addition, a comparison between the two columns of Table 4 in dicates the unique information value of eWOM platform concentration. The main difference in common independent variables between them lies with the coefficient on MeanRating , the mean value of Amazon and CNETD valence. It is significantly negative in column (1) but becomes insignificant in our Base Model in column (2). Along with this change from column (1) to column (2) is an increased value of $R ^ { 2 } .$ . At the same time, some variables (e.g., product age) irrelevant to eWOM are quali tatively similar between those two columns. Therefore, we believe that the explanatory power of eWOM platform concentration in our Base Model in column (2) comes within the eWOM, instead of the potential correlation with other control variables irrelevant to eWOM. This result highlights a significant role of valence equality of eWOM across plat forms in influencing sales, rather than the overall average consumer evaluation. If ignored, it can be misleading to conclude that the overall average rating of Amazon and CNETD influences Amazon sales.

We also find satisfactory results from Durbin, Hausman, and Wu specification test towards the aforementioned potentially endogenous variable, MeanRating . We fail to reject the null hypothesis that the asymptotic estimation is consistent and efficient. This empirically sup ports implies that our Base Model in $\operatorname { E q } .$ . (3) unlikely suffer from the endogeneity issue caused by the unobserved product quality.

Given the above results and discussions, we find initial evidence for supporting our hypotheses. In the following subsection, we further es timate advanced models to offer empirical results for rigorously

answering our research questions.

## 5.2. Full Model Estimations

Table 5 summarizes estimation results of the rest models, including the CNETD Model in 5.2, the week-lagged Model in 5.3, and the SUR Model in 5.4. Estimations of all these proposed models show qualita tively similar results on our two equality metrics and their interaction term as those of the Base Model results. We, therefore, find sufficient support for all three hypotheses with robust empirical results. In the following subsections, we focus on interpreting the magnitudes of the identified impacts and their implications based on the SUR Model esti mations. In particular, the correlation between its Eqs. (6) and (7) is estimated as 0.145, significantly different from zero, as empirical evi dence supportive to our choice of SUR model. It controls for any missing factors that can affect both Amazon sales and CNETD downloads simultaneously.

SUR Model results support the main effect of volume equality on user decisions at both Amazon and CNETD (H1). Meanwhile, the coefficient on total volume $( L n T o t a l V o l _ { i , t } )$ is also significantly positive. These find ings support our arguments that volume equality and the total volume of eWOM have different information values. Greater volume equality across two sites increases the consumer awareness of a more diversified population of users (Godes & Mayzlin, 2006), promoting more user adoptions of the product.

The results also show that the positive interaction effect between volume equality and valence equality (H3) is not trivial, as estimated by $3 2 . 8 2 6 ~ ( \beta _ { 2 } )$ and $3 8 . 2 9 0 \ \left( \alpha _ { 2 } \right)$ on Amazon and CNETD, respectively. Increasing volume equality from 0.056 to 0.693 can magnify the mar ginal impact of a 0.1 increase in valence equality by up to 3.5 times greater on Amazon sales $( e ^ { 0 . 8 2 8 ^ { * } \beta 2 ^ { * } ( 0 . 6 9 3 - 0 . 0 5 \hat { 6 } ) ^ { * } 0 . 1 } { - 1 } )$ , and by nearly ten times greater on CNETD weekly downloads $( e ^ { \alpha 2 ^ { * } ( 0 . \dot { 6 } 9 3 - 0 . 0 5 6 ) ^ { * } 0 . 1 } - 1 )$ . This increase in volume equality describes the change from the scenario where one platform receives user reviews 99 times as many as the other platform $( V o l E q u a l i t y _ { i , t } { = } 0 . 0 5 6 )$ to the case where each platform receives the same amount of user reviews $( V o l E q u a l i t y _ { i , t } { = } 0 . 6 9 3 )$ . It is highlighted that, to map the sales rank to sales at Amazon, we adopt 0.828 from the experimental study of Ghose and Sundararajan [18] as the scaling co efficient for the negative log-linear relationship between sales rank and sales, as discussed earlier.

The total impact of valence equality has two components: its main effect as estimated by $\beta _ { 3 } \ : ( 2 . 3 9 0 )$ on the Amazon site and $\alpha _ { 3 } \ : ( 1 . 5 9 0 )$ on CNETD (H2), and its interaction effect with volume equality (H3). We take Norton 360 as an example and find the magnitude of this impact quite remarkable. Its volume equality is calculated as 0.039, based on its review volume of 456 on Amazon and 3 on CNETD. We hypothetically compare two extreme cases of valence equality, while all else are equal. In Scenario I, Norton 360 receives the same average 3-star user rating at both two platforms, resulting in a high level of valence equality (ValE $q u a l i t y _ { i , t } { = } 0 . 6 9 3 )$ . In Scenario II, it receives a 1-star average rating on Amazon and a 5-star average rating on CNETD, leading to a much lower level of valence equality $( V a l E q u a l i t y _ { i , t } { = } 0 . 4 5 1 )$ . All else being equal, the greater valence equality in Scenario I can double the Amazon sales of Norton 360 in Scenario II, estimated by $e ^ { 0 . 8 2 8 ^ { \ast } ( 0 . 6 9 3 - 0 . 4 5 1 ) ^ { \ast } ( \beta 2 ^ { \ast } 0 . 0 3 9 + \beta 3 ) } . 1$

We further illustrate the total impact of a decrease in valence equality in the following Fig. 1. Specifically, valence equality is initially set as 0.693, when Amazon and CNETD receive user reviews of the same average valence, e.g., 3-star average rating. Hypothetically, we decrease this value to 0.673, so that Amazon and CNETD receive reviews of 2-star and 3-star average ratings. The resulted decreases in Amazon sales and CNETD downloads are plotted against volume equality that ranges from 0.1- 0.6. As shown by the figure, this 0.02 decrease in valence equality $( 0 . 6 9 3  0 . 6 7 3 )$ adversely affects Amazon sales and CNETD downloads more significantly when volume equality increases. This impact can be amplified by up to two times on Amazon, from 9% to 31%, and three times on CNETD, from 10% to 40%. When online users face different opinions from eWOM across sites, having the majority of reviewers agreed on one side of the arguments provides a clearer and more dominating voice on product experiences. This is a favorable scenario to promote product adoptions than having an equal number of reviewers on both sides of the arguments.

Furthermore, there are some other interesting observations from the rest of eWOM related variables. First, receiving more volume on one site than the others $( D u m m y V o l _ { i , t } )$ only affects Amazon sales but not CNETD downloads. This echoes the findings of prior studies as well as our un derlying assumption that retail websites and reviewing websites are two distinct platforms. A potential reason for this result could be that Amazon users are more sensitive to the convenience of accessing the majority of eWOM directly on their decision-making site than CNETD users. In addition, compared to the Base Model, the coefficient of the average valence of Amazon and CNETD eWOM (MeanRating ) remains insignificant, adding to the robustness of our finding that valence equality is more influential than the valence itself. The total volume $( L n T o t a l V o l _ { i , t } )$ is also significantly positive in presence of volume equality, similar to our observation in Base Model, supporting the distinct information value of volume equality.

## 6. Discussion and Conclusions

In this paper, we study how the platform concentration of eWOM across retail and review platforms influences online product adoption decisions by focusing on two metrics: volume equality and valence equality. We find that it is beneficial for a product to receive a compa rable number of consistent user feedbacks from platforms of different types. In addition, receiving inconsistent feedback across platforms be comes more harmful, when the volume of user feedbacks received at each platform is more comparable.

## 6.1. Theoretical Contributions

This research answers the recent call for more studies on eWOM hosted by different types of platforms [44]. It offers empirical evidence for the potential of a new perspective in this line of research: platform concentration of eWOM. Several meta-analysis studies on eWOM research have unanimously found a relatively small number of works on eWOM hosted by different types of platforms, despite the large body of overall eWOM work [11, 44]. The focus of those related studies is to compare the magnitude of eWOM effect on online user decisions among different platforms [19, 22, 44]. Our work does not intend to continue this direction of identifying the most influential eWOM hosting platform based on the difference in reviewer identity (professionals vs. users) or platform category (retail vs. review platforms). Instead, we show that the answer depends on the platform concentration of eWOM. Receiving a new user review at an individual platform will most likely change the platform concentration of eWOM. And the size of this change is asso ciated with the precedent eWOM distribution. We believe that the addition of this new perspective along with two proposed new metrics contribute to this line of research.

In particular. this study highlights the unique information role that the platform concentration of eWOM volume plays in influencing online users’ decisions to adopt products: the heterogeneity of online users being aware of the product. We find evidence that volume equality of eWOM across platforms indicates consumer awareness of the product in a different angle from the widely discussed total volume. The total volume captures the overall consumer awareness, indicating the number of consumers being aware of the product [22, 54]; our proposed new metric, volume equality, captures the heterogeneity of users being aware of the product. Specifically, the higher volume equality across distinct platforms reflects a more diverse user population who are dis cussing the product and spreading their words to others.

This study also offers a potential explanation to reconcile the divergent findings in prior studies on the economic impact of eWOM valence, varying between the insignificant impact and the positive impact ([5, 14]; Teng et al., 2017; [50, 53]). There can be two varying factors in the contexts of those prior studies: the indefinite change of valence equality brought by a valence increase at an individual plat form, and the impact of valence equality being dependent on volume equality. A valence increase can lead to an indefinite change of valence equality, depending on the valence at each platform prior to that in crease. For example, a one-star increase in valence from 4-star to 5-star on Amazon leads to an increase of 0.006 in valence equality if CNETD valence is 5-star. However, the same one-star increase from 2-star to 3-star on Amazon leads to a much larger increase in valence equality, 0.02, if CNETD valence is 3-star. Moreover, the impact of valence equality also depends on volume equality. When online users face more divergent opinions across platforms (i.e., a decrease in valence equality), higher volume equality will make the situation worse. This explanation receives support from our empirical finding that valence equality across sites better explains user decisions of adopting software programs than the valence.

## 6.2. Practical Implications

Our findings have valuable practical implications for product ven dors. First, vendors can utilize the informational role of volume equality to help reach a diversified body of potential customers. This is especially important for launching a new product for the mass market. Being aware of the product is the first step to adopt it. Hence, our results on volume equality suggest the vendors split budgets towards platforms of different types to encourage discussions and feedbacks from diversified users. Second, we caution vendors to make alert and delicate responses to any surge of incoming negative user feedbacks at an individual platform, especially when the product used to be well received uniformly across platforms. Those negative reviews may hurt product sales more than expected, beyond the lowered valence. They would bring down valence equality and thus compromise the product/firm reputation gained from favorable reviews not only hosted by this platform itself but also by other platforms. To cope with the arrival of negative feedbacks, our findings offer two strategies. The first strategy is consistent with the conventional wisdom: soliciting positive reviews on that particular site to improve valence equality across platforms. The other one is less straightforward: soliciting reviews at another platform that has received the most user discussions so far. The second strategy will reduce volume equality. This will help mitigate the negative impact of the decrease in valence equality caused by those incoming negative feedbacks, given the positive interaction effect between volume equality and valence equality. In addition, we also suggest the vendors be mindful of the adverse impact of inconsistent user reviews. Prior studies have empha sized soliciting positive feedbacks at a single platform. Our results show that it can turn harmful if such efforts towards boosting more favorable reviews contribute to the lower valence equality across platforms.

In addition, our results also offer some suggestions to platforms. We show the value of displaying valence equality and volume equality directly at the platform for customer convenience, along with other existing eWOM summary metrics. It is not difficult to make available those two new metrics, because they are determined by the aggregated eWOM numerical data from platforms. In this sense, our findings also promote a relatively new business model of review aggregators, e.g., testseek.com, that offer brands, retailers and platforms paid services of collecting and aggregating eWOM on the requested product around the web. Their services can be more valuable if they go beyond simply listing the volume and valence from each collected review platform and include our proposed two metrics.

## 6.3. Limitations and Future Research

There are several limitations of this research as well as a few promising directions for future research. First, future research can benefit from including more platforms. The current study selected only one website each to represent retail platforms and review platforms, respectively. A richer sample collected from more platforms would have added to the robustness of our results. Second, the data used in the empirical analysis is not the most up-to-date. Fortunately, Amazon and CNETD are two well-established leading platforms in the online software market, and neither of them has had any significant changes in their platform design. As a result, we are comfortable with utilizing this data to examine our hypotheses. Nevertheless, more recent data on emerging platforms may provide another piece of evidence to our conclusions. Third, this study uses a sample of top-selling products on Amazon, which may raise concerns about applying our conclusions to the whole spec trum of products in the online market. Conducting empirical in vestigations on products with a wider range of popularities may help extend the validity of our findings. Last, there could be more attributes of eWOM that influence online user decisions, in addition to the plat form concentration of eWOM. For instance, the perceived review help fulness and informativeness of review contents may also play a role [1, 33, 49]. As we briefly browse reviews on Amazon and CNETD, we note that some reviews are much more structured and informative than others. It would thus be interesting to apply text mining techniques to compare the discrepancy and distribution of review quality across platforms in future research.

## CRediT authorship contribution statement

Hong Chen: Data curation, Methodology, Formal analysis, Writing – review & editing. Wenjing Duan: Conceptualization, Methodology, Supervision, Writing – review & editing. Wenqi Zhou: Conceptualiza tion, Formal analysis, Writing – original draft, Writing – review & editing.

## Declarations of Competing Interest

None

## Acknowledgements

The authors thank participants at the Workshop on e-Business and the International Conference on Information Systems reviewer team for valu able comments on this research. All errors are our own.

## Appendix A

Table A.1

## Table A1

```txt
Microsoft Works 9.0
iWork '09
Mavis Beacon Teaches Typing 18
Mac OS X version 10.6.3 Snow Leopard
Roxio Easy VHS to DVD
Manga Studio Debut 4 (Win/Mac)
Typing Instructor For Kids Platinum (Windows/Mac)
Adobe Photoshop Lightroom 3
Microsoft Outlook 2010
Microsoft Publisher 2010
Expression Studio 4 Web Professional
Malwarebytes Anti-Malware Lifetime
Sony Vegas Movie Studio HD Platinum 10 Suite
Trend Micro Titanium Internet Security 2011 - 3 User
McAfee Total Protection 2011
McAfee AntiVirus Plus 2011 3-User
McAfee Total Protection 2011 3-User
Kaspersky Anti-Virus 2011 3-User
```

Table A1 (continued )

Kaspersky Internet Security 2011 3-User PDF Converter Professional 7.0 Kaspersky Internet Security 2011 1-User Adobe Photoshop Elements 9 (Win/Mac) Ouicken Deluxe 2011 Quicken Essentials for Mac QuickBooks Pro 2011 Quicken Premier 2011 Quicken Home & Business 2011 QuickBooks 2011 for Mac Dragon Dictate 2.0 Adobe Premiere Elements 9 (Win/Mac) Norton Antivirus 2011 - 1 User/3 Pc Parallels Desktop 6 for Mac Autodesk Sketchbook Pro 2011 Adobe Acrobat X Standard Kaspersky Pure 3-User Norton Internet Security 2011 1PC Norton 360 5.0 1-User/3PCs Microsoft Streets & Trips 2011 Microsoft Windows 7 Professional Upgrade Microsoft Windows 7 Home Premium Microsoft Windows 7 Home Premium Upgrade Microsoft Windows 7 Anytime Upgrade [Home Premium to Professional] Microsoft Windows 7 Home Premium Upgrade Family Pack (3-User)

## References

[1] S.N. Ahmad, M. Laroche, Analyzing electronic word of mouth: A social commerce construct, Int. J. Inf. Manage. 37 (3) (2017) 202–213.

[2] Amblee, N., & Bui, T. (2007). Freeware downloads: An empirical investigation into the impact of expert and user reviews on demand for digital goods. Proceedings of Americas Conference on Information Systems.

[3] N. Amblee, T. Bui, Harnessing the influence of social proof in online shopping: The effect of electronic Word of Mouth on sales of digital microproducts, Int. J. Electronic Commerce 16 (2) (2011) 91–113.

[4] H. Baek, S. Oh, H.D. Yang, J.H. Ahn, Electronic word-of-mouth, box office revenue and social media, Electronic Commerce Res. Appl. 22 (2017) 13–23. March-April.

[5] D. Baum, M. Spann, The interplay between online consumer reviews and recommender systems: An experimental analysis, Int. J. Electronic Commerce 19 (1) (2014) 129–162.

[6] A. Benlian, R. Titah, T. Hess, Differential effects of provider recommendations and consumer reviews in e-commerce transactions: An experimental study, J. Manage. Information Syst. 29 (1) (2012) 237–272.

[7] B. Bickart, R.M. Schindler, Internet forums as influential sources of consumer information, J. Interactive Marketing 15 (3) (2001) 31–40.

[8] E. Brynjolfsson, Y. Hu, M.D. Smith, Consumer surplus in the digital economy: Estimating the value of increased product variety at online booksellers, Manage. Sci. 49 (11) (2003) 1580–1596.

[9] F.A. Carrillat, R. Legoux, A.L Hadida, Debates and assumptions about motion picture performance: a meta-analysis, J. Academy of Marketing Sci 46 (2) (2018) 273-299.

[10] J.A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: Online book reviews, J. Marketing Sci. 43 (3) (2006) 345–354

[11] S.C. Chu, J. Kim, The current state of knowledge on electronic word-of-mouth in advertising research. Int. J. Advertising 37 (1) (2018) 1–13

[12] Dhanasobhon, S, Chen, P., & Smith, M. D. (2007). An Analysis of the Differential Impact of Reviews and Reviewers at Amazon.com. Proceedings of International Conference on Information Systems.

[13] W. Duan, B. Gu, A.B. Whinston, The dynamics of online word-of-mouth and product sales—An empirical investigation of the movie industry, J. Retailing 84 (2) (2008) 233–242.

[14] W. Duan. B. Gu, A.B. Whinston, Informational cascades and software adoption on the Internet: An empirical investigation, MIS O. 33 (1) (2009) 23–48.

[15] I. Erkan, C. Evans, Social media or shopping websites? The influence of eWOM on consumers’ online purchase intentions, J. Marketing Commun. 24 (6) (2018)

[16] P. Figini, L. Vici, G. Viglia, A comparison of hotel ratings between verified and nonverified online review platforms. Int. J. Culture. Tourism and Hospitality Res., 14 (2) (2020) 157–171, https://doi,org/10.1108/LJCTHR-10-2019-0193.

[17] D. Gavilan, M. Avello, G. Martinez-Navarro, The influence of online ratings and reviews on hotel booking consideration. Tourism Manage, 66 (2018) 53–61. https://doi.org/10.1016/i.tourman.2017.10.018.

[18] A. Ghose, A. Sundararajan, Software versioning and quality degradation? An exploratory study of the evidence, CEDER, New York, 2005. Working Paper No. CeDER-05-20.

[19] D. Godes, D. Mayzlin, Using online conversation to study word of mouth communications, Marketing Sci. 23 (4) (2004) 545–560.

[20] K. Goh, C. Heng, Z. Lin, Social media brand community and consumer behavior: Quantifying the relative impact of user- and marketer-generated content, Inf. Syst. Res. 24 (1) (2013) 88–107

[21] M.S. Granovetter, The strength of weak ties, Am. J. Sociol. 78 (6) (1973) 1360-1380

[22] B. Gu, J. Park, P. Konana, The impact of external word-of-mouth sources on retailer sales of high-involvement products. Inf, Syst. Res. 23 (1) (2012) 182–196

[23] R. Hastie, Memory for information which confirms or contradicts a general impression. Person memory: The cognitive basis of social perception, Lawrence Erlbaum, Hillsdale, 1980, pp. 155–177.

[24] P. Huang, N.H. Lurie, S. Mitra, Searching for experience on the web: An empirical examination of consumer behavior for search and experience goods, J. Marketing 73 (22) (2009) 55–89.

[25] K.J. Kaplan, On the ambivalence-indifference problem in attitude theory and measurement: A suggested modification of the semantic differential technique, Psychol. Bull. 77 (5) (1972) 361–372.

[26] J. Kim, P. Gupta, Emotional expressions in online user reviews: How they Influence consumers' product evaluations, J. Bus. Res. 65 (7) (2012) 985–992

[27] J. Lee, J.N. Lee, Understanding the product information inference process in electronic word-of-mouth: An objectivity-subjectivity dichotomy perspective, Information & Management 46 (2009) 302–311.

[28] L.Y. Leong, T.S. Hew, K.B. Ooi, B. Lin, Do electronic word-of-mouth and elaboration likelihood model influence hotel booking? J. Computer Information Syst. 59 (2) (2019) 146–160.

[29] M. Li, L. Huang, C. Tan, K. Wei, Helpfulness of online product reviews as seen by consumers: Source and content features, Int. J. Electronic Commerce 17 (4) (2013) 101–136.

[30] S. Li, F. Li, The interaction effects of online reviews and free samples on consumers downloads: An empirical analysis, Information Processing & Manage. 56 (6) (2019), 102071.

[31] X. Li. LM. Hitt. Self-selection and information role of online product reviews. Inf

[32] X. Li, L.M. Hitt, Z.J. Zhang, Product reviews and competition in markets for repeat purchase products, J. Management Information Syst. 27 (4) (2011) 9–41.

[33] X. Li, C. Wu, F. Mai, The effect of online reviews on product sales: A join sentiment-topic analysis, Information & Manage. 56 (2) (2019) 172–184.

[34] Y. Liu, Word of mouth for movies: Its dynamics and impact on box office revenue, J. Marketing 70 (3) (2006) 74–89.

[35] J. Liu, C. Li, Y.G. Ji, M. North, F. Yang, Like it or not: The Fortune 500<sup>′</sup>s Facebook strategies to generate users’ electronic word-of-mouth, Comput. Hum. Behav. 73 (2017) 605–613. August.

[36] X. Lu. S. Ba. L. Huang, Y. Feng, Promotional marketing or word-of-mouth?

[37] X. Luo, J. Zhang, How do consumer buzz and traffic in social media marketing predict the value of the firm? J. Manage. Information Syst. 30 (2) (2013) 213–238

[38] X. Ma, L. Khansa, Yu. Deng, S.S. Kim, Impact of prior reviews on the subsequent review process in reputation systems, J. Manage. Information Syst. 30 (3) (2014) 279–310.

[39] W.J. McGuire, The probabilogical model of cognitive structure and attitude change. Cognitive responses in persuasion, Lawrence Erlbaum, Hillsdale, 1981, pp. 291–307.

[40] S. Moon, P.K. Bergey, D. Lacobucci, Dynamic effects among movie ratings, movie revenues, and viewer satisfaction, J. Marketing 74 (1) (2010) 108–121.

[41] J.R. Priester, R.E. Petty, The gradual threshold of model of ambivalence: Relating the positive and negative bases of attitudes to subjective ambivalence, J. Pers. Soc Psychol. 71 (3) (1996) 431–449.

[42] J.R. Priester, R.E. Petty, Extending the bases of subjective attitudinal ambivalence: Interpersonal and intrapersonal antecedents of evaluative tension, J. Pers. Soc. Psychol, 80 (1) (2001) 19–34

[43] H. Rui, Y. Liu, A. Whinston. Whose and what chatter matters? The impact of tweets on movie sales, Decision Support Syst. 55 (4) (2013) 863–870.

[44] A.B. Rosario, F. Sotgiu, K.D. Valck, T.H.A. Bijmolt, The effect of electronic word of mouth on sales: A meta-analytic review of platform, product, and metric factors, J. Marketing Res. 53 (3) (2016) 297–318.

[45] S. Senecal, J. Nantel, The influence of online product recommendations on customers’ online choices, J. Retailing 80 (2) (2004) 159–169.

[46] T.K. Srull, R.S. Wyer, Person memory and judgment, Psychol. Rev. 96 (1) (1989)

[47] M.D. Smith, R. Telang, Competing with free: The impact of movie broadcasting on DVD sales and Internet piracy, MIS Q. 33 (2) (2008) 321–338.

[48] M. Sun, How does variance of product ratings matter? Manage. Sci. 58 (4) (2012) 696–707.

[49] Wang, J. N., Du, J., & Chiu, Y.L. (2020). Can online user reviews be more helpful? Evaluating and improving ranking approaches. Information & Management, available online 13 February 2020.

[50] A.E. Wilson, M.D. Giebelhausen, M.K. Brady, Negative word of mouth can be a positive for consumers connected to the brand, J. Academy of Marketing Sci. 45 (4) (2017) 534–547.

[51] Word of Mouth Marketing Association, 2014. The state of word of mouth marketing, A survey of marketers, Last Accessed on June 9. 2020. https://www slideshare.net/WOMMAChicago/the-state-of-word-of-mouth-marketing-surve

[52] Z. Xiang, Q. Du, Y. Ma, W. Fan, A comparative analysis of major online review platforms: Implications for social media analytics in hospitality and tourism, Tourism Manage. 58 (2017) 51–65, https://doi.org/10.1016/j tourman.2016.10.001.

[53] W. Zhou, W. Duan, Online user reviews, product variety, and the long tail: An empirical investigation on online software downloads, Electronic Commerce Res. Appl. 11 (3) (2012) 275–289.

[54] W. Zhou, W. Duan, An empirical study of how third-party websites influence the feedback mechanism between online word-of-mouth and retail sales. Decisior Support Syst. 76 (2015) 14–23.

[55] W. Zhou, W. Duan, Do professional reviews affect online user choices through user reviews?: An empirical study. J. Manage Information Syst. 33 (1) (2016) 202–228.

[56] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics, J. Marketing 74 (2) (2010) 133–148.

Hong Chen is currently an Assistant Professor of Information Sciences and Technology at Penn State University of New Kensington. He received the PhD degree from the University of Rhode Island in 2012. Prior to his current position, Dr. Chen was Visiting Assistant Professor of Information Systems Management in Palumbo-Donahue School of Business at Duquesne University, and, subsequently, Assistant Professor of Computer and Information Science at Siena Heights University. His research is interdisciplinary, and spans Infor mation Systems and Analytics. His recent research examines the impact of online User Generated Content and cyber fraud on Internet market outcome.

Wenjing Duan is currently an Associate Professor of Information Systems & Technology Management at School of Business, The George Washington University. She received her Ph.D. in Information Systems from University of Texas at Austin in 2006. Wenjing’s research interests glide the intersections between Information Systems, Economics, and Marketing. Among her primary research interests are the economics of e-commerce, online communities and social networks, the Internet marketing, and online Intermediaries. Wenjing has published in MIS Quarterly, Information Systems Research, Journal of Man agement Information Systems, Communications of ACM, Journal of Retailing, and Decision Support Systems. She received Emerald Management Reviews Citations of Excellence Awards in 2012 and 2014. She is also the recipient of the NET Institute Research Grant and serves on the Editorial Board of the Decision Support Systems.

Wengi Zhou is currently David Warco Faculty Fellow and an Associate Professor in In formation Systems & Technology at Palumbo-Donahue School of Business, Duquesne University. She received her Ph.D. in Information Systems from The George Washington University in 2013. Her research primarily focuses on understanding social, economic and managerial aspects of information technology and the Internet by analyzing large-scale online data. Her works have been published in Journal of Management Information Sys tems, Decision Support Systems, IEEE Computer, Electronic Commerce Research and Applica tions, and ICIS proceedings, among others. She received several Best Paper Award at various conferences, including Workshop on e-Business and Academy of Management Annual Meeting.
