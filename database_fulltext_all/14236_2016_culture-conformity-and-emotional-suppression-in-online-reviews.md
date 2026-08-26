---
otero_id: 14236
otero_key: "WQPRCQ67"
title: "Culture, Conformity, and Emotional Suppression in Online Reviews"
authors: "Yili Hong; Ni Huang; Gordon Burtch; Chunxiao Li"
year: "2016"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00443"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
11-30-2016

# Culture, Conformity, and Emotional Suppression in Online Reviews

Yili Hong
Arizona State University, hong@asu.edu

Ni Huang
Temple University, nina.huang@temple.edu

Gordon Burtch
University of Minnesota, gburtch@umn.edu

Chunxiao Li
Arizona State University, chunxiao.li@asu.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

Research Paper

ISSN: 1536-9323

# Culture, Conformity, and Emotional Suppression in Online Reviews

Yili Hong
Department of Information Systems, W. P. Carey School of Business, Arizona State University
hong@asu.edu

Gord Burtch
Department of Information and Decision Sciences,
Carlson School of Management, University of Minnesota
gburtch@umn.edu

Ni Huang
Department of Marketing and Supply Chain
Management, Fox School of Business, Temple University
nina.huang@temple.edu

Chunxiao Li
Department of Information Systems, W. P. Carey School of Business, Arizona State University
chunxiao.li@asu.edu

Abstract:

In this study, we examine consumers' cultural background as an antecedent of online review characteristics. We theoretically propose and empirically examine the effect of cultural background (specifically individualism (versus collectivism)) on consumers' tendency to conform to prior opinion and review texts' emotionality. We also examine how conformity and emotionality relate to review helpfulness. We test our hypotheses using a unique dataset that combines online restaurant reviews from TripAdvisor with measures of individualism/collectivism values. We found that consumers from a collectivist culture were less likely to deviate from the average prior rating and to express emotion in their reviews. Moreover, individuals perceived those reviews that exhibited high conformity and intense emotions to be less helpful. We also present several important implications for managing online review platforms in light of these findings, which reflect the previously unidentified drivers of systematic differences in the characteristics of online reviews.

Keywords: Culture, Online Reviews, Individualism Value, Rating Deviation, Review Emotion.

## 1 Introduction

Much research in various business disciplines, particularly information systems and marketing, has focused on online reviews. Several studies have noted that the effect of online reviews greatly depends on their characteristics. Specifically, negative reviews tend to be more influential than positive reviews (Chevalier & Mayzlin, 2006), whereas an author who expresses emotion in a review can affect the perceived helpfulness of the review (Yin, Bond, & Zhang, 2014) and consumer conversion (Ludwig et al., 2013). Moreover, the disagreement among prior reviews (e.g., higher variance in star ratings) can have varying effects on product sales and the characteristics of subsequent reviews (Nagle & Riedl, 2014; Sun, 2012). Interestingly, few studies have explored the characteristics of review authors as possible antecedents of review content.

To extend prior literature on the antecedents of online reviews (Goes, Lin, & Yeung, 2014; Huang, Burtch, Hong, & Polman, 2016), we focus on the potential role of the cultural background of reviewers (particularly individualism vs. collectivism values) $^{1}$ . In the process, we answer the recent calls for research on the cross-cultural differences in the production of electronic word of mouth (eWOM) (King, Racherla, & Bush, 2014). Anecdotal and scientific evidence jointly suggest that cultural differences have significant potential to explain the variations in review characteristics. By evaluating the Amazon marketplaces in the United Kingdom (UK), Japan, Germany, and the United States (US), Danescu-Niculescu-Mizil, Kossinets, Kleinberg, and Lee (2009) observed “noticeable differences between reviews” in terms of their average helpfulness and rating variance. Other studies that have examined the cross-cultural differences in the production and consumption of online reviews have also reported similar results (Chung & Darke 2006; Fang, Zhang, Bao, and Zhu, 2013; Koh, Hu, & Clemons, 2010). For instance, consumers from collectivist cultures are less likely to write reviews with low valence (i.e., one-star ratings) (Fang et al., 2013). Underreporting biases, which refer to an author’s tendency to write reviews following extreme experiences, are more prevalent among consumers from individualist cultures (Koh et al., 2010). Consumers from individualist cultures are more likely to write reviews for products or services that enable self-expression (Chung & Darke, 2006). However, many questions remain despite these contributions to our understanding of the role of culture in the review process. According to King et al. (2014, p.175), “Understanding these differences and being able to adapt the review process to meet these needs are critical to retailers, so that they can design systems that provide this information in the best manner possible.”.

The majority of the studies on individualism versus collectivism values have focused on their implications on individuals' tendency to conform or stand out. Accordingly, we focus on the following characteristics of online reviews that are directly linked to conformity and are likely to be influenced by an author's individualist or collectivist cultural values: 1) conformity to (or deviation from) prior opinion and 2) emotional suppression (or expression). We address the following questions:

RQ1: How does individualism (collectivism) influence deviation from (conformity to) prior opinion in online reviews?

RQ2: How does individualism (collectivism) influence emotional expression (suppression) in online reviews?

RQ3: In turn, how do these cultural influences affect the perceived helpfulness of online reviews?

While Americans say, “the squeaky wheel gets the grease”, the Japanese say, “the nail that stands out gets pounded down” (Goleman, 1990). Such variation in cultural values is not merely anecdotal: much research has established that it exists. For example, researchers in cultural psychology (Hofstede, 2001; House, Hanges, Javidan, Dorfman, & Gupta, 2004) have systematically documented that individuals from collectivist cultures are more likely to exhibit conformity to group opinion (Bond and Smith 1996, Ng et al. 2000) and are less likely to express emotion (Butler, Lee, & Gross, 2007, Niedenthal, Krauth-Gruber, & Ric, 2006). These observations suggest that online reviews that consumers from collectivist cultures write are less likely to deviate from prior opinion and less likely to include emotional expressions than those from individualistic cultures.

In this paper, we empirically evaluate these expectations to extend the literature and answer the calls for research into cross-cultural differences in eWOM (King et al., 2014). First, our work builds on the small body of literature that addresses the cultural differences in the production of online reviews by using data on users from various countries and cultural backgrounds. This technique contrasts those of the majority of previous studies, which have mostly relied on two-country designs (e.g., comparing American and Chinese consumers), which limits the generalizability of their findings (Fang et al., 2013; Koh et al., 2010). Second, previous studies have considered the role of cultural differences in determining the volume and valence of reviews in an absolute sense (Fang et al., 2013). We extend such work by considering the self-group differences in online reviews (i.e., relative valence in terms of deviation from prior opinion) and emotional expression.

Drawing on the cultural psychology literature, we formulated and evaluated several hypotheses using a unique dataset that integrates online restaurant reviews from TripAdvisor.com with country-level measures of individualism/collectivism values (House et al., 2004). We then estimated the effects of these values on the measures of review conformity and emotional suppression. We also examined the subsequent effect of the characteristics of reviews on their perceived helpfulness. We obtained three key findings. First, we found that consumers from countries with a higher level of individualism were more likely to deviate from the prior average rating when writing a review. Second, these reviewers were more likely to express their emotions in the review text. Third, conformity and emotional expression generally had a negative relationship with review helpfulness $^{2}$ .

Our work offers important practical implications for online review platforms. First, recent studies suggest that the approaches that many leading review websites use to aggregate reviews (e.g., averaging) tend to ignore reviewer-specific differences in producing reviews (Dai, Jin, Lee, & Luca, 2012). However, our findings reveal previously undocumented systematic differences in reviewer culture that review websites should consider when aggregating reviews. Second, several features that improve or damage the perceived helpfulness of online reviews (in terms of “helpful” votes) are more likely to systematically manifest when consumers come from a particular culture. Therefore, online practitioners, who are cognizant of these issues, must consider approaches that encourage or deter certain review characteristics. For example, Yelp offers mobile users with “example” reviews to encourage them to produce longer and informative content. Based on an individual’s location or review history, one may propose a similar strategy to encourage individuals to include or exclude textual features that do or do not contribute to a “helpful” review.

This paper proceeds as follows. In Section 2, we review the previous studies on online reviews and particularly those that focus on conformity and emotional suppression. We specifically focus on the cultural psychology literature that deals with conformity, language use, and emotional suppression. In Section 3, we propose several hypotheses for empirical examination. In Section 4, we present the research methodology and report our results. In Section 5, we discuss the implications and limitations of our work.

## 2 Literature Review

## 2.1 Online Reviews

Relative to traditional mass communication, online reviews uniquely feature bi-directionality, which emphasizes the need to study both the consumers who created the reviews and effects of these reviews on other consumers (Dellarocas, 2003; Goes et al., 2014). Online reviews enable consumers to share their evaluations and opinions of products or services to an extremely large audience (Dellarocas, 2003; Lee & Bradlow, 2011; Lu, Ba, Huang, & Feng, 2013). Following the pioneering works of Ba and Pavlou (2002) and Dellarocas (2003), many studies from the information systems field have begun to investigate the downstream effects of reviews in terms of sales (Li & Hitt, 2008), helpfulness (Mudambi & Schuff, 2010), and market competition (Kwark, Chen, & Raghunathan, 2014). More recently, researchers have begun to look at how to better design review systems (Liu, Chen, & Hong, 2014) and what factors stimulate online reviews (Burtch, Hong, Bapna, & Griskevicius, forthcoming). We consider the antecedents of review characteristics, which have received relatively less attention in the literature (Goes et al., 2014), by focusing on reviews' textual characteristics and reviewers' conformity to (or deviation from) the prior average ratings.

Recent studies have reported evidence on reviewers' broad conformity (Muchnik, Aral, & Taylor, 2013; Lee, Hosanagar, & Tan, 2015; Wang, Zhang, & Hann, forthcoming). Muchnik et al. (2013) experimentally demonstrate that individuals exposed to a positive prior rating have an increased probability of submitting a positive rating. Similarly, Wang et al. (forthcoming) and Lee et al. (2015) report that individuals' opinions correlate positively with those of their friends. However, contrary to reactance theory (Brehm & Brehm, 1981), a related stream of research (Wu & Huberman 2008; Moe & Schweidel, 2012; Godes & Silva, 2012) has revealed that some individuals are motivated to "stand out" from the crowd by deviating from others' opinions. Conditional on a purchase, a consumer will decide whether to post a review. Wu and Huberman (2008) argue that consumers are motivated, at least in part, by the expected influence of their reviews on the average rating and, implicitly, on the actions or preferences of others. These researchers have empirically revealed that buyers are most likely to post reviews when the expected effect is high (i.e., when only few reviews are present or when their experience extensively deviates from the prevailing average).

Only a handful of studies have investigated reviews' textual characteristics, and the majority of these works have focused on the consequences of textual features. Several textual features affect review helpfulness and product sales. For example, Goes et al. (2014) show that consumers who are more popular in a review community tend to write highly objective reviews. Yin et al. (2014) demonstrate that individuals are likely to perceive certain types of negative emotions (i.e., anxiety) as more helpful than other emotions (i.e., anger). In their study, Ahmad and Laroche (2015) considered the relationship between different types of expressed emotions (i.e., hope, happiness, anxiety, and disgust) and the perceived helpfulness of reviews and observed differential effects across each emotion. Ghose et al. (2011) report that spelling mistakes and review subjectivity are negatively associated with helpfulness and product sales. Huang et al. (2015) examine the effect of anonymity and social presence on review characteristics. We build on the review text literature by considering the antecedent of review emotion (namely, the individualism value of the review author). In Section 2.2, we review the literature on cultural values, conformity, and language use.

## 2.2 Cultural Values, Conformity, and Language Use

Researchers have used national cultural dimensions such as those that Robert House (House et al., 2004) and Geert Hofstede (Hofstede, 2001) introduced to study various phenomena in information systems (Leidner & Kayworth, 2006). However, few studies have explored the role of cultural values in online reviews (Chung & Darke, 2006; Koh et al., 2010; Fang et al., 2013). These researchers contrast the review authorship or consumption between individuals residing in a collectivist country and those residing in an individualist country. Chung and Darke (2006) found that self-relevance has a greater effect on the user-generated content in individualist cultures than that in collectivist cultures. Koh et al. (2010) found that underreporting is more prevalent among U.S. customers than among Chinese or Singaporean customers. Fang et al. (2013) report on a number of several descriptive differences between American and Chinese reviewers. For example, Chinese reviewers provide more positive reviews and place a higher weight on negative reviews.

Although previous studies have explored the differences in the behavior of individuals from various cultures, scholars have yet to consider two notable aspects: opinion conformity and emotional suppression. Both aspects tend to differ across cultures, particularly with respect to collectivism versus individualism. First, with respect to conformity, many studies have reported that individuals from collectivist cultures are more likely to conform in judgment and evaluation (Bond & Smith, 1996), behavior (Cialdini, Wosinska, Barrett, Butnet, & Gornik-Durose, 1999), and opinion (Huang, 2005). Second, with respect to emotional expression, several studies have determined that people from individualist cultures are more likely to express emotions (Takahashi, Ohara, Antonucci, & Akiyama, 2002), while those from collectivist cultures are more likely to suppress emotion (Niedenthal, 2006) (particularly negative ones) (Butler et al., 2007).

## 3 Hypothesis Development

We propose several research hypotheses that we empirically test. We divide the research framework into several components. We examine the antecedents in the first stage in which we propose the formal hypotheses about the effects of consumers' cultural backgrounds (countries that exhibit higher levels of individualism versus collectivism) on review characteristics (rating deviation and review textual characteristics). We empirically examine in the second stage the potential relationships between review characteristics and perceived review helpfulness. Figure 1 presents the research framework.

![](/api/attachments/WQPRCQ67/fulltext/images/337bd64a2ecf8fa52816f7fe429ff008777c6dfeb96fec2e783a5544d39494b3.jpg)  
Figure 1. Research Framework

## 3.1 Cultural Background and Review Characteristics

By considering the effects of cultural background on dissenting opinions and emotion expression, we focus on the distinction between individualism and collectivism values and on behaviors that are relevant to 1) online review authorship and 2) individualist/collectivist cultural values.

Collectivist values generally feature a preference for preserving harmony, avoiding confrontation, and promoting conformity; as such, such values discourage individual initiatives and deviations from the dominant opinion of the group (Hofstede, 2001; House et al., 2004). Researchers have documented conformity to group pressure in experiments since the 1950s (Asch, 1955). Through a meta-analysis of 133 conformity studies similar to Asch (1955), scholars have also systematically verified that conformity effects are much stronger among individuals from collectivist cultures (Bond & Smith, 1996). Similarly, other studies have observed greater conformity among individuals from collectivist cultures in terms of actual behavior (Cialdini et al., 1999) and opinion formation (Huang, 2005). These findings have a direct bearing on our study context through their suggestions that those reviews written by individuals from collectivist (individualist) cultures are more likely to conform to (deviate from) prior opinions.

In the online reviews context, when a consumer writes a review about a merchant, the consumer may feel pressured to “conform” (Muchnik et al., 2013; Lee et al., 2015; Wang et al., forthcoming) to the group opinion as expressed in previous reviews about the same merchant. This behavior tends to emerge because the webpage of a review website prominently shows a merchant’s current average rating, which may serve as an anchor for subsequent consumers (Adomavicius, Bockstedt, Curley, & Zhang, 2013). Yaveroglu and Donthu (2002) argue that individuals from collectivist cultures (e.g., China and Japan) are more likely to conform to the views of others to fit in, gain social understanding, and be accepted by others in a group. Those societies that espouse collectivist values encourage social harmony and bonding in groups (Triandis, 1995; Lam, Lee, & Mizerski, 2009). Therefore, we anticipate that consumers from collectivist cultures will more likely demonstrate review conformity.

In some cases, a consumer may also observe and deviate from prior opinion (Moe & Schweidel, 2012; Wu & Huberman, 2008). As we discuss when reviewing the cultural psychology literature, countries with high individualism values encourage individual autonomy and individualist behavior and discourage conformity. Therefore, individuals from individualist cultures will likely be more “opinionated” because they want to stand out from the others or to have their voices heard. Accordingly, we expect individuals from countries with high individualist values to deviate from prior opinion. Thus, we propose the following:

H1A: On average, those ratings that consumers from individualist (versus collectivist) cultural backgrounds submit are more likely to deviate from (less likely to conform to) the prior average rating.

Several studies in the information systems literature have also examined the role of online review text. Early studies in this line of research have reported the influence of textual content over and above numerical ratings (Pavlou & Dimoka, 2006; Chevalier & Mayzlin, 2006). Recent studies have considered the effects of basic textual features, such as readability and spelling mistakes (Ghose & Ipeirotis 2011; Goes et al., 2014), on review helpfulness. Other studies have explored highly nuanced features, such as semantic style (Cao, Duan, & Gan, 2011) and objectivity versus subjectivity (Ghose & Ipeirotis, 2011).

Scholars have recently examined review texts to identify their emotional and affective content (Ludwig et al., 2013; Yin et al., 2014). They have revealed that such content can strongly affect the perceived helpfulness of a review and its influence on customer conversion. One natural extension is to explore a review author's individualist/collectivist cultural background as a potential antecedent of emotional content in a review.

The cultural psychology literature includes several studies that suggest a strong relationship between culture and emotion. The literature has reported that the tendency toward emotional expression differs according to an individual's cultural background. Previous studies have shown that individuals from individualist cultures tend to be more vocal and expressive, whereas those from collectivist cultures speak in ways intended to maintain harmony and avoid controversy (e.g., using indirect language) (Holtgraves, 1997). Some studies have demonstrated that people from collectivist cultures tend to suppress or withhold their emotions when communicating with others (Butler et al., 2007; Niedenthal et al., 2006), whereas those from individualist cultures are more likely to express their emotions (particularly negative emotions) (Takahashi et al., 2002). These tendencies manifest early in life because children are socialized to meet the standards of their culture (Friedlmeier, Corapci, & Cole, 2011).

Individuals in individualist cultures generally consider expressing emotions publicly to be acceptable, but individuals in collectivist cultures generally frown on it. Tsai, Miao, Seppala, Fung, and Yeung (2007) found that American culture typically supports high arousal states, such as excitement and enthusiasm, because these emotions are more effective in influencing others. By contrast, collectivist cultures espouse low arousal states, such as calmness, which better suit adapting to and accommodating others. When writing an online review, a consumer expresses an opinion and performs an evaluation, which often involves a public display of emotion (Yin et al., 2014). Accordingly, these studies have suggested that the reviews written by individuals from individualist cultures are more likely to contain emotions. Therefore, we propose the following:

H1B: Consumers from individualist cultural backgrounds tend to express more emotions in their reviews.

## 3.2 Review Characteristics and Helpfulness

Review helpfulness (generally measured by “helpful” votes) has important implications for both review curators and consumers. To draw practical implications from our study, one must understand how the systematic differences in reviewer behavior may be associated with the perceived helpfulness of reviews. Consumers generally seek different opinions toward the same restaurant prior to consumption to assess whether such establishment can match their tastes (Sun, 2012; Hong, Chen, Hitt, 2013; Liu et al., 2014). Ratings that deviate (either positively or negatively) from prior opinion are likely to stand out and offer unique information by presenting the “other side of the argument” (Cao et al., 2011). Indeed, previous studies have presented consistent evidence that negative reviews, in particular, are likely to be perceived as more helpful because of a “negativity bias”; that is, negative reviews tend to be seen as more informative (Mudambi & Schuff, 2010; Chen & Lurie, 2013). Similarly, we anticipate that rating deviation (i.e., extreme valence relative to past reviews) will result in the higher perceived helpfulness of the review. Therefore, we propose the following:

## H2A: Rating deviation is positively associated with review helpfulness.

Several pioneering studies have also employed text mining techniques vis-à-vis the effect of review content. Lee, Hosanagar, and Nair (2013) determine that the presence of informational content in a message may be more or less useful depending on the type of product one considers. Ghose and Ipeirotis (2006) found that objective content is more helpful than subjective content. Considering these past studies and the idea that emotions tend to be perceived as less rational or objective, consumers may perceive reviews that contain greater expressions of emotion as less helpful. Therefore, we propose the following:

H2B: Review emotion is negatively associated with review helpfulness.

## 4 Research Methodology

## 4.1 Data

We collected data from several archival data sources (Table 1).

Table 1. Archival Data Sources

<table><tr><td>Data</td><td>Source</td></tr><tr><td>Review, reviewer data</td><td>TripAdvisor</td></tr><tr><td>Review emotion</td><td>TripAdvisor reviews processed by Linguistic Inquiry and Word Count (LIWC)</td></tr><tr><td>Cultural values</td><td>House et al. (2004), World Value Survey</td></tr></table>

First, we collected online reviews (posted between 2003 and 2014) from a leading review platform, TripAdvisor (www.tripadvisor.com), using a Web crawler. Our data included online reviews for approximately 3,750 restaurants located in six major U.S. cities (namely, Chicago, Houston, Los Angeles, New York, Phoenix, Philadelphia, and Seattle). We ensured data accuracy by manually verifying a randomly selected set of 150 reviews. Figure 2 presents a screenshot of a review in TripAdvisor.

![](/api/attachments/WQPRCQ67/fulltext/images/3f2bab271b2d781c287a68dffd854d0368926b25f944f1f0b12446eeff058f93.jpg)  
Figure 2. Screenshot of a Sample TripAdvisor Review

We constructed our panel by collecting the entire review history of each restaurant and ordering the reviews based on their time stamps. From each review, we obtained the star rating, sequence (order) position, time stamp, and actual review text. We also obtained data on the characteristics of the review authors, including their historical reviewing activity, website registration date, and country of residence. We then measured emotional expression by examining the review text in an automated fashion using the text-mining tool Linguistic Inquiry and Word Count (LIWC), which we describe further in Section 4.2.

Second, we collected data on cultural values from several sources based on prior literature. Several scholars and institutions have attempted to measure national cultural values over the years. Researchers from various fields have extensively used the cultural value data that Hofstede (2001) collected; however, these data are subject to severe limitations because Hofstede collected them from a selected group of IBM employees, which biases them. House et al. (2004) provide a more detailed set of cultural value measures that includes collectivism versus individualism. Researchers have widely used these latest measures in recent years (e.g., Schoorman, Mayer, & Davis, 2007).

Researchers in other disciplines have also operationalized cultural values based on the World Values Survey (WVS) (e.g., Giannetti & Yafeh, 2012; Burtch, Ghose, & Wattal, 2014; Hong & Pavlou, 2014) $^{3}$ . By analyzing the results of WVS, Inglehart and Welzel (2010) observed that two factors can explain more than 70 percent of the variance in responses, one of which is survival versus self-expression (the extent to which a society emphasizes values related to survival as opposed to self-expression); these factors capture much of the same information that House et al.'s (2004) the collectivism/individualism measure captures (Inglehart & Oyserman, 2004).

Many researchers consider House et al.'s (2004) culture measure as the most up-to-date and comprehensive because this measure builds on Hofstede (2001), Inglehart and Oyserman (2004), and several other cultural studies. Therefore, we focused on this measure in our primary analysis and subsequently performed a series of robustness checks using the measures from WVS that Inglehart and Welzel (2010) propose. We assigned a consumer (review author) with an individualism value score based on the consumer's self-reported country of residence.

## 4.2 Key Measures

## 4.2.1 Dependent Variables:

Rating deviation: we measured rating deviation as the absolute difference between the rating of a focal review and the average prior rating. TripAdvisor uses a half-star average rating system; therefore, the published average ratings fall in the set (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5). To compute for deviation, we reconstructed the average restaurant rating at the time immediately before the focal review ( $n^{\text{th}}$ position in the sequence) as follows: $\bar{r}_n = \frac{1}{n-1} * \sum_{i=1}^{n-1} r_i$ . Afterward, we obtained the observed average rating $\hat{r}_n$ by rounding $\bar{r}_n$ to the nearest half star. For example, for $\bar{r}_n = 3.24$ , $\hat{r}_n = 3$ (3 stars); for $\bar{r}_n = 3.26$ , $\hat{r}_n = 3.5$ (three and a half stars); and for $\bar{r}_n = 3.76$ , $\hat{r}_n = 4$ (four stars). In cases where $\bar{r}_n = 3.25$ , we rounded the value to 3.5. One can write rating deviation (distance between the $n^{\text{th}}$ rating $r_n$ and the observed prior average rating $\hat{r}_n$ ) as follows:

$$
R a t i n g D e v i a t i o n _ {n} = a b s (r _ {n} - \hat {r} _ {n})\tag{1}
$$

As a robustness check, we considered the unrounded prior average and formulated an alternative measure of deviation; we obtained almost identical results using the unrounded measure (in terms of the magnitudes and statistical significance of the parameter estimates). However, we expected this result because the actual and observed (rounded) deviation have a 99 percent correlation.

Review emotion: we used LIWC, text-analysis software that identifies sentiment and emotion in textual content, to obtain the measures of emotion (e.g., happy, cried, and abandon), positive emotion (e.g., love, nice, and sweet), and negative emotion (e.g., hurt, ugly, and nasty) (Pennebaker, Francis, & Booth, 2001). LIWC has recently attracted frequent use in the information systems and marketing literatures (Sridhar & Srinivasan, 2012; Yin et al., 2014; Goes et al., 2014). Before calculating the textual measures, we cleaned the textual data to remove special characters. Using LIWC, we operationalized the review emotion measures as the percentage of emotional (overall, positive, and negative) words out of the total number of words.

Review helpfulness: in line with prior literature (Mudambi & Schuff, 2010; Chen & Lurie, 2013), we measured review helpfulness in terms of the total number of “helpful” votes received by a review. Given the highly skewed distribution of votes, we used the log transformation of the raw value in our analyses.

## 4.2.2 Independent Variables

Individualism/collectivism values: we used the collectivism/individualism data from House et al. (2004). These data (from survey responses from 17,300 individuals) are highly consistent with the “survival versus self-expression” measure of WVS and the individualism measure from Hofstede (2001). The collectivism data from House et al. measure the degree to which individuals express pride, loyalty, and cohesiveness in their organizations or families. We employed the negative value of collectivism to measure its polar opposite, individualism. Therefore, higher values of collectivism indicate a greater individualism or lesser collectivism. We plotted the data from House et al. and the self-expression measure of Inglehart and Welzel (2010) based on the most recent wave of WVS. Figure 3 shows that Sweden, the Netherlands, New Zealand, the UK, Denmark, Germany, and the US rank highly on individualism, whereas Russia, China, Georgia, Morocco, Zimbabwe, Hungary, and Albania rank low on individualism. Note that researchers often assume that cultural values are country-level constructs that a country’s members inherit. For example, the Chinese or Japanese are generally less assertive and more prone to conformity than Americans. However, the cultural values of individuals in a country may vary because of individual heterogeneity and immigration. Nonetheless, similar to prior literature, we assumed that the inheritance of cultural values holds for the majority of a country’s residents because that society embraces those values. Therefore, to avoid confusion with respect to the level of measurement and the ecological fallacy, we referred to subjects’ cultural backgrounds instead of their cultural values.

![](/api/attachments/WQPRCQ67/fulltext/images/059e6f8016ee5259566c8359fbe2ea70c42517a44598c0046adc51676db04318.jpg)  
Figure 3. Individualism (versus Collectivism) Value by Countries

Travel experience: we measured a consumer's travel experience as the number of countries that the consumer had traveled to as reflected in the TripAdvisor data. Travel experience indicates an individual's exposure to different cultures. Traveling to different countries allows an individual to encounter people of different cultural backgrounds, which makes the individual more receptive to other cultures and exhibit only few of the systematic differences that we have hypothesized. Given its skewness, we log-transformed the travel experience variable.

Prior review volume: prior review volume may affect rating deviation because late arrivals (in terms of the sequence of reviews written for a restaurant) may have different motivations and preferences than the early adopters. For example, a late arriver may have a higher motivation to deviate from prior opinion to make his/her review “stand out”.

Average rating: we controlled for the average rating of a consumer because prior research has noted that some consumers are systematically more positive or negative in their reviewing behavior (Dai et al. 2012).

Consumer tenure: we controlled for consumer tenure (number of months since website registration) for several reasons. First, consumers may grow more positive or negative as they accumulate review experience. We log-transformed this variable in our analyses because of its skewed distribution.

Review age: we controlled for review age (number of days since the review became live and available for consumer voting) because older reviews are exposed to more viewers and have a greater opportunity to accrue helpful votes.

Time effects: we controlled for time effects by employing monthly dummy variables. The reviews written at different periods may be systematically different because of unobserved shocks or trends (e.g., degradation in restaurant quality).

Tables 2 and 3 present the descriptive statistics and correlation matrix of our key variables, respectively.

Table 2. Descriptive Statistics

<table><tr><td>Variable</td><td>Mean</td><td>St.d.</td><td>Min</td><td>Max</td><td>Median</td></tr><tr><td>1. Rating deviation</td><td>0.79</td><td>0.67</td><td>0</td><td>4.50</td><td>0.5</td></tr><tr><td>2. Review emotion</td><td>8.72</td><td>6.52</td><td>0</td><td>100</td><td>7.41</td></tr><tr><td>3. Positive emotion</td><td>7.96</td><td>6.53</td><td>0.00</td><td>100</td><td>6.67</td></tr><tr><td>4. Negative emotion</td><td>0.74</td><td>1.73</td><td>0.00</td><td>100</td><td>0</td></tr></table>

Table 2. Descriptive Statistics

<table><tr><td>5. Prior volume</td><td>181.46</td><td>269.40</td><td>1.00</td><td>2561</td><td>83</td></tr><tr><td>6. Individualism</td><td>-4.32</td><td>0.35</td><td>-6.37</td><td>-3.46</td><td>-4.22</td></tr><tr><td>7. Experience</td><td>9.52</td><td>11.23</td><td>1</td><td>207</td><td>5</td></tr><tr><td>8. Average rating</td><td>3.77</td><td>1.27</td><td>1</td><td>5</td><td>4.1</td></tr><tr><td>9. Consumer tenure</td><td>28.57</td><td>27.79</td><td>0</td><td>139</td><td>21</td></tr></table>

Table 3. Correlation Matrix

<table><tr><td>Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1.Rating deviation</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2.Review emotion</td><td>-0.11</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3.Positive emotion</td><td>-0.16</td><td>0.96</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4.Negative emotion</td><td>0.21</td><td>0.11</td><td>-0.15</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5.Prior volume</td><td>-0.05</td><td>-0.03</td><td>-0.03</td><td>-0.01</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>6.Individualism</td><td>0.01</td><td>0.04</td><td>0.04</td><td>0.02</td><td>-0.01</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>7.Experience</td><td>-0.05</td><td>0.01</td><td>0.01</td><td>0.00</td><td>-0.01</td><td>-0.14</td><td>1.00</td><td></td><td></td></tr><tr><td>8.Average rating</td><td>-0.15</td><td>-0.07</td><td>-0.05</td><td>-0.07</td><td>0.06</td><td>0.00</td><td>0.11</td><td>1.00</td><td></td></tr><tr><td>9.Consumer tenure</td><td>-0.06</td><td>-0.05</td><td>-0.05</td><td>-0.01</td><td>0.05</td><td>0.03</td><td>0.22</td><td>0.22</td><td>1.00</td></tr></table>

## 4.3 Empirical Model

Although we operationalized cultural values at the country level, assigning these values to consumers is reasonable in this scenario for several reasons. First, those consumers who are born and raised in a particular country are likely to inherit that country's cultural values. Second, the interaction between country-level cultural values and consumer-level travel experience can help one further identify the effects of cultural values.

We identified the effects of cultural values, travel experience, and the interaction between these two by examining within-restaurant variance in reviews via within transformation (i.e., a standard fixed effect estimation $(FE:\delta_{j})$ ) while controlling for time effects via dummy variables $(\sum_{T}\tau_{t}*M_{t})$ . Additionally, we controlled for consumer-level heterogeneity using the abovementioned controls. We formulated the estimation equations for rating deviation and votes as follows: in these two equations, i indexes consumers, j indexes restaurants, and t indexes time; $\delta_{j}$ is the restaurant fixed effect that controls for restaurant-level, time-invariant unobserved factors; and $\sum_{T}\tau_{t}*M_{t}$ is the vector of monthly time dummies. The key parameters of interest are $\alpha,\beta,$ and $\gamma$ .

$$
\text { Rating   Deviation } _ {i j t} = \alpha_ {1} * \text { individualism } _ {i} + \alpha_ {2} * \ln (\text { experience } _ {i}) + \alpha_ {3} * (\text { individualism } *
$$

$$
\ln (e x p e r i e n c e)) _ {i} + \alpha_ {4} * \text {review emotion} _ {i t j} + \delta_ {j} + \sum_ {T} \tau_ {t} * M _ {t} + c o n t r o l _ {i j t} + \varepsilon_ {i j t}\tag{2}
$$

$$
\text { Review   Emotion } _ {i j t} = \beta_ {1} * \text { individualism } _ {i} + \beta_ {2} * [ [ \ln (\text { experience }) ] _ {i}) + \beta_ {3} * (\text { individualism } *\tag{3}
$$

$$
\ln (e x p e r i e n c e)) _ {i} + \beta_ {4} * \mathrm{ratingdeviation} _ {i t j} + \delta_ {j} + \sum_ {T} \tau_ {t} * M _ {t} + c o n t r o l _ {i j t} + \varepsilon_ {i j t}
$$

$\ln (helpfulness)_{ij} = \gamma_1 * Rating Deviation_{ij} + \gamma_2 * lnwords_{ij} + \gamma_3 * Rating Deviation_{ij} *$

$$
l n w o r d s _ {i j} + \gamma_ {4} * R e v i e w E m o t i o n _ {i j} + \gamma_ {5} * R e v i e w A g e _ {i j} + \delta_ {j} + C o n t r o l _ {i j} + \varepsilon_ {i j}\tag{4}
$$

## 4.4 Estimation Results and Hypotheses Testing

In this section, we report the estimation results of our main analyses. Following the structure of the hypothesis development, we began by examining the effects of individualism on rating deviation. As Table 4 shows, individualism values significantly increased rating deviation, which offers clear support for Hypothesis 1a.

Table 4. Effect of Individualism Value on Rating Deviation

<table><tr><td>DV:</td><td>(1) Rating deviation</td><td>(2) Rating deviation</td><td>(3) Rating deviation</td></tr><tr><td>Individualism</td><td>0.026***(0.004)</td><td>0.015***(0.005)</td><td>0.036***(0.014)</td></tr><tr><td>In(experience)</td><td></td><td>-0.032***(0.002)</td><td>-0.069***(0.022)</td></tr><tr><td>Individualism*ln(experience)</td><td></td><td></td><td>-0.009*(0.005)</td></tr><tr><td>In(prior volume)</td><td></td><td>0.000(0.007)</td><td>0.000(0.007)</td></tr><tr><td>Average rating</td><td></td><td>-0.066***(0.002)</td><td>-0.066***(0.002)</td></tr><tr><td>In(consumer tenure)</td><td></td><td>-0.004***(0.001)</td><td>-0.004***(0.001)</td></tr><tr><td>Review emotion</td><td></td><td>-0.014***(0.000)</td><td>-0.014***(0.000)</td></tr><tr><td>Constant</td><td>1.498*(0.832)</td><td>0.000(0.007)</td><td>0.036***(0.014)</td></tr><tr><td>Restaurant FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>256,810</td><td>256,810</td><td>256,810</td></tr><tr><td>R-squared (within)</td><td>0.015</td><td>0.057</td><td>0.061</td></tr><tr><td># of restaurants</td><td>3,735</td><td>3,735</td><td>3,735</td></tr><tr><td colspan="4">Notes: robust standard errors are enclosed in parentheses. Std. err. is adjusted for clusters in restaurants.The coefficients are significant at levels *** p &lt; 0.01, ** p &lt; 0.05, and * p &lt; 0.1.</td></tr></table>

Although consumers in countries that promote individualist values tend to deviate from the prior average rating, a variation may still exist among consumers in the same country. For example, some consumers from the US may be more conformist, whereas some consumers from China may be more individualistic. One may attribute this variation in cultural values to travel experience, which potentially exposes people to different cultural values. Such exposure makes people more tolerant of other worldviews. Therefore, we further examined the potential moderating role of consumer travel experience on the relationship between individualism values and rating deviation. In particular, we calculated the marginal effects and conducted a spotlight analysis (Spiller, Fitzsimons, Lynch, & McClelland, 2013) to assess both the main and interaction effects. As Figure 4 shows, first, the main effect of individualism on rating deviation remained positive across the spectrum of values for different travel experiences. Second, travel experience significantly moderated the effect of individualism on rating deviation. In sum, as individuals gain travel experience, they are potentially exposed to different cultures and become less affected by their own cultural backgrounds.

![](/api/attachments/WQPRCQ67/fulltext/images/8d555e37e7b27cb911bf247a69f1fa107e7c81cf2f84950cf4af2b1678c61e6b.jpg)  
Figure 4. Spotlight Analysis of the Interaction Effect on Rating Deviation

Table 5. Effect of Individualism Value on Review Emotion

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td></tr><tr><td>DVs:</td><td>Overall emotion</td><td>Overall emotion</td><td>Overall emotion</td><td>Positive emotion</td><td>Positive emotion</td><td>Positive emotion</td><td>Negative emotion</td><td>Negative emotion</td><td>Negative emotion</td></tr><tr><td>Individualism</td><td>0.518***(0.052)</td><td>0.553***(0.052)</td><td>1.452***(0.128)</td><td>0.440***(0.051)</td><td>0.480***(0.050)</td><td>1.295***(0.122)</td><td>0.086***(0.011)</td><td>0.081***(0.011)</td><td>0.177***(0.026)</td></tr><tr><td>ln(experience)</td><td></td><td>0.014(0.013)</td><td>-1.585***(0.194)</td><td></td><td>-0.002(0.013)</td><td>-1.452***(0.188)</td><td></td><td>0.017***(0.004)</td><td>-0.153***(0.044)</td></tr><tr><td>Individualism* ln(experience)</td><td></td><td></td><td>-0.375***(0.045)</td><td></td><td></td><td>-0.340***(0.044)</td><td></td><td></td><td>-0.040***(0.010)</td></tr><tr><td>ln(prior volume)</td><td></td><td>0.240***(0.046)</td><td>0.241***(0.046)</td><td></td><td>0.225***(0.045)</td><td>0.226***(0.045)</td><td></td><td>0.018(0.011)</td><td>0.018(0.011)</td></tr><tr><td>Average rating</td><td></td><td>-0.094***(0.014)</td><td>-0.095***(0.014)</td><td></td><td>-0.041***(0.014)</td><td>-0.042***(0.014)</td><td></td><td>-0.053***(0.004)</td><td>-0.053***(0.004)</td></tr><tr><td>ln(consumer tenure)</td><td></td><td>-0.151***(0.009)</td><td>-0.150***(0.009)</td><td></td><td>-0.160***(0.009)</td><td>-0.160***(0.009)</td><td></td><td>0.010***(0.002)</td><td>0.011***(0.002)</td></tr><tr><td>Rating deviation</td><td></td><td>-0.971***(0.020)</td><td>-0.972***(0.020)</td><td></td><td>-1.410***(0.021)</td><td>-1.410***(0.020)</td><td></td><td>0.439***(0.007)</td><td>0.439***(0.007)</td></tr><tr><td>Constant</td><td>13.370***(0.220)</td><td>10.456***(1.682)</td><td>14.286***(1.741)</td><td>12.466***(0.215)</td><td>10.527***(1.436)</td><td>13.997***(1.503)</td><td>0.954***(0.047)</td><td>-0.048(0.316)</td><td>0.360(0.331)</td></tr><tr><td>Restaurant FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>256,810</td><td>256,810</td><td>256,810</td><td>256,810</td><td>256,810</td><td>256,810</td><td>256,810</td><td>256,810</td><td>256,810</td></tr><tr><td>R-squared (within)</td><td>0.042</td><td>0.049</td><td>0.049</td><td>0.039</td><td>0.060</td><td>0.060</td><td>0.013</td><td>0.043</td><td>0.043</td></tr><tr><td># of restaurants</td><td>3,735</td><td>3,735</td><td>3,735</td><td>3,735</td><td>3,735</td><td>3,735</td><td>3,735</td><td>3,735</td><td>3,735</td></tr><tr><td colspan="10">Notes: robust standard errors are enclosed in parentheses. Std. err. is adjusted for clusters in restaurants. The coefficients are significant at levels *** p&lt; 0.01, ** p&lt; 0.05, and * p&lt; 0.1.</td></tr></table>

We then examined the effects of cultural background on review emotion and, specifically, overall emotion (Column 1 of Table 5), positive emotion (Column 3), and negative emotion (Column 5). First, consumers from individualistic cultures were more likely to express both positive and negative emotions, which supports Hypothesis 1b. Travel experience attenuated all these estimated direct effects of cultural values on review text (Figure 5 visualizes the main and interaction effects). Table 5 and Figure 5 show that consumers from an individualist cultural background always expressed a higher level of overall, positive, and negative emotions and that travel experience attenuated the positive effects. Interestingly, we observed that rating deviation was positively correlated with the presence of negative emotion yet negatively correlated with the presence of positive emotion.

(a) Overall Emotion  
![](/api/attachments/WQPRCQ67/fulltext/images/8454df261994d6bddbe2f5b2b1079cbba5b66f1110d74f9c712320dfd7c8c787.jpg)

(b) Positive Emotion  
![](/api/attachments/WQPRCQ67/fulltext/images/ea68c846320fb72a44f04a2542ee5be0520ae2dcac668e4d4d5e05857a74c183.jpg)  
Figure 5. Spotlight Analysis of the Interaction Effect on Review Emotion

(c) Negative Emotion  
![](/api/attachments/WQPRCQ67/fulltext/images/d2b5a73f797b48c06ee214e4c5da553ac65d0d3989f37582d546abe8a6369eb0.jpg)

Table 6. Effect of Review Characteristics on Review Helpfulness

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Rating deviation</td><td>-0.044***(0.005)</td><td>-0.049***(0.005)</td><td>-0.029***(0.007)</td><td>-0.025***(0.007)</td><td></td></tr><tr><td>In(words)</td><td>0.048***(0.002)</td><td>0.047***(0.002)</td><td>0.050***(0.002)</td><td>0.051***(0.002)</td><td></td></tr><tr><td>Rating deviation * In(words)</td><td>0.022***(0.001)</td><td>0.023***(0.001)</td><td>0.020***(0.002)</td><td>0.019***(0.002)</td><td></td></tr><tr><td>Emotion</td><td>-0.000**(0.000)</td><td></td><td>0.000**(0.000)</td><td></td><td></td></tr><tr><td>Rating deviation * emotion</td><td></td><td></td><td>-0.001***(0.000)</td><td></td><td></td></tr><tr><td>Positive emotion</td><td></td><td>-0.000***(0.000)</td><td></td><td>0.001***(0.000)</td><td></td></tr><tr><td>Negative emotion</td><td></td><td>0.003***(0.000)</td><td></td><td>-0.001**(0.001)</td><td></td></tr><tr><td>Rating deviation * positive emotion</td><td></td><td></td><td></td><td>-0.002***(0.000)</td><td></td></tr><tr><td>Rating deviation * negative emotion</td><td></td><td></td><td></td><td>0.003***(0.000)</td><td></td></tr><tr><td>Individualism</td><td></td><td></td><td></td><td></td><td>0.005*(0.003)</td></tr><tr><td>Review age</td><td>0.000***(0.000)</td><td>0.000***(0.000)</td><td>0.000***(0.000)</td><td>0.000***(0.000)</td><td>0.000***(0.000)</td></tr><tr><td>Constant</td><td>-0.139***(0.011)</td><td>-0.133***(0.011)</td><td>-0.152***(0.011)</td><td>-0.155***(0.011)</td><td>0.120***(0.013)</td></tr><tr><td>Restaurant FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>298,458</td><td>298,458</td><td>298,458</td><td>298,458</td><td>298,458</td></tr><tr><td>R-squared</td><td>0.070</td><td>0.070</td><td>0.070</td><td>0.071</td><td>0.040</td></tr><tr><td># of restaurants</td><td>3,747</td><td>3,747</td><td>3,747</td><td>3,747</td><td>3,747</td></tr><tr><td colspan="6">Notes: robust standard errors are enclosed in parentheses, Std. err. is adjusted for clusters in restaurants. The coefficients are significant at levels *** p &lt; 0.01, ** p &lt; 0.05, and * p &lt; 0.1.</td></tr></table>

![](/api/attachments/WQPRCQ67/fulltext/images/ab1293c8f77c318f809a4153e9258baef331979162ce76d2b48649f9d7075afa.jpg)  
Figure 6. Interaction Effect of Rating Deviation and Review Length on Helpfulness

We then examined the effects of review characteristics (rating deviation and review emotion) on review helpfulness in terms of “helpful” votes. As the regression results in Table 6 and the plot in Figure 6 show, rating deviation increased the perceived helpfulness of a review, which supports Hypothesis 2a. We also found a positive interaction between rating deviation and review length (see Figure 6), which suggests that deviation exerts a greater influence when the textual content conveys more information.

(a) Overall Emotion  
![](/api/attachments/WQPRCQ67/fulltext/images/b0d9e38cb033b184dbc1b41ca827a1645d578a0c95e0665fcd6ad567e671918c.jpg)

(b) Positive Emotion  
![](/api/attachments/WQPRCQ67/fulltext/images/9ed612f8cd70efdf66000d899316d49fb2815973e4e7b0ba4abd095d16886859.jpg)  
(c) Negative Emotion

![](/api/attachments/WQPRCQ67/fulltext/images/54ff384dfadf7529c862a3fae45c3bdc1ed797ac4b2507abe8cf559418a7ab92.jpg)  
Figure 7. Interaction Effect of Rating Deviation and Review Emotion on Helpfulness

Given the influence of review emotion, we observed that overall emotion had a negative effect on review helpfulness, which supports Hypothesis 2b. When we further broke down the positive and negative emotions, we found that positive emotions led to lower review helpfulness, whereas negative emotions increased review helpfulness. This finding is consistent with the “negativity bias” in online reviews that prior research has demonstrated (Chen & Lurie, 2013). Beyond the main effects, we observed significant interaction effects between rating deviation and review emotion (Figure 7), which indicates that positive emotion and rating deviation have a significant negative interaction effect (substitutive effect) on review helpfulness and that negative emotion and rating deviation have a positive interaction effect (complementary effect) on review helpfulness. Column 5 of Table 6 shows that individuals generally perceive those reviews written by consumers from individualist cultural backgrounds to be more helpful.

## 4.5 Robustness Checks

We validated the robustness of our results in several ways. We first considered alternative measures of cultural values by re-running our analyses using data from WVS (see Section 4.5.1). The first set of robustness checks aimed to demonstrate that the measurement of cultural values did not drive the observed results. We also considered an alternative estimation approach (seemingly unrelated regression (SUR)) by allowing the error terms of Equations (2) and (3) to correlate with each other (see Section 4.5.2).

## 4.5.1 Robustness Check 1: Alternative Measures of Cultural Background

We obtained an additional dataset on cultural values from WVS and re-estimated our models to confirm the stability of our results. We observed a high correlation between the measures of House et al. (2004) and WVS ( $\rho = 0.90$ ) in our sample $^{4}$ . Given the lack of temporal variation in the WVS data, we used the most recent set of survey responses. Our main results remained stable regardless of our chosen measure (see Table 7).

## 4.5.2 Robustness Check 2: Alternative Estimation Approach

We also obtained results using the SUR model, which controls for the possibility that review deviation and emotion are co-determined. SUR allows one to correlate the error terms of Equations (2) and (3) and jointly estimates these equations. The estimation results, as Table 8 shows, are consistent with our main results, which indicates their robustness.

Table 7. Robustness Check: Estimation Using Alternative Measure

<table><tr><td>DVs:</td><td>(1) Rating deviation</td><td>(2) Overall emotion</td><td>(3) Positive emotion</td><td>(4) Negative emotion</td></tr><tr><td>Individualism</td><td>0.027***(0.010)</td><td>0.917***(0.110)</td><td>0.803***(0.107)</td><td>0.117***(0.019)</td></tr><tr><td>ln(experience)</td><td>-0.017***(0.006)</td><td>0.446***(0.067)</td><td>0.376***(0.066)</td><td>0.070***(0.014)</td></tr><tr><td>Individualism*ln(experience)</td><td>-0.009**(0.004)</td><td>-0.255***(0.039)</td><td>-0.224***(0.038)</td><td>-0.032***(0.008)</td></tr><tr><td>ln(prior volume)</td><td>0.001(0.007)</td><td>0.240***(0.046)</td><td>0.223***(0.045)</td><td>0.019*(0.011)</td></tr><tr><td>Average rating</td><td>-0.066***(0.002)</td><td>-0.096***(0.014)</td><td>-0.042***(0.014)</td><td>-0.054***(0.004)</td></tr><tr><td>ln(consumer tenure)</td><td>-0.004***(0.001)</td><td>-0.154***(0.009)</td><td>-0.163***(0.009)</td><td>0.010***(0.002)</td></tr><tr><td>Review emotion</td><td>-0.014***(0.000)</td><td></td><td></td><td></td></tr><tr><td>Rating deviation</td><td></td><td>-0.973***(0.020)</td><td>-1.412***(0.020)</td><td>0.440***(0.007)</td></tr><tr><td>Constant</td><td>1.663***(0.640)</td><td>6.547***(1.664)</td><td>7.124***(1.411)</td><td>-0.593*(0.318)</td></tr><tr><td>Restaurant FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>259,460</td><td>259,460</td><td>259,460</td><td>259,460</td></tr><tr><td>R-squared (within)</td><td>0.046</td><td>0.049</td><td>0.060</td><td>0.042</td></tr><tr><td># of restaurants</td><td>3,736</td><td>3,736</td><td>3,736</td><td>3,736</td></tr><tr><td colspan="5">Notes: Robust standard errors are enclosed in parentheses. Std. Err. is adjusted for clusters in restaurants. The coefficients are significant at levels *** p&lt; 0.01, ** p&lt; 0.05, and * p&lt; 0.1.</td></tr></table>

Table 8. Robustness Check: SUR Estimation

<table><tr><td>DVs:</td><td>(1) Rating deviation</td><td>(2) Overall emotion</td><td>(3) Rating deviation</td><td>(4) Negative emotion</td><td>(5) Positive emotion</td></tr><tr><td>Individualism</td><td>0.102***(0.012)</td><td>2.238***(0.099)</td><td>0.068***(0.012)</td><td>0.207***(0.027)</td><td>2.045***(0.099)</td></tr><tr><td>In(experience)</td><td>-0.153***(0.020)</td><td>-2.565***(0.167)</td><td>-0.117***(0.020)</td><td>-0.187***(0.045)</td><td>-2.386***(0.166)</td></tr><tr><td>Individualism *In(experience)</td><td>-0.028***(0.005)</td><td>-0.601***(0.039)</td><td>-0.020***(0.005)</td><td>-0.053***(0.010)</td><td>-0.551***(0.039)</td></tr><tr><td>Emotion</td><td>-0.029***(0.000)</td><td></td><td></td><td></td><td></td></tr><tr><td>Rating deviation</td><td></td><td>-2.003***(0.016)</td><td></td><td>0.843***(0.004)</td><td>-2.758***(0.016)</td></tr><tr><td>Negative emotion</td><td></td><td></td><td>0.145***(0.001)</td><td></td><td></td></tr><tr><td>Positive emotion</td><td></td><td></td><td>-0.033***(0.000)</td><td></td><td></td></tr><tr><td>In(prior volume)</td><td>-0.018***(0.001)</td><td>-0.064***(0.009)</td><td>-0.019***(0.001)</td><td>0.016***(0.002)</td><td>-0.078***(0.009)</td></tr><tr><td>Average rating</td><td>-0.068***(0.001)</td><td>-0.160***(0.009)</td><td>-0.054***(0.001)</td><td>-0.025***(0.003)</td><td>-0.128***(0.009)</td></tr><tr><td>In(consumer tenure)</td><td>-0.007***(0.001)</td><td>-0.148***(0.009)</td><td>-0.009***(0.001)</td><td>0.011***(0.002)</td><td>-0.158***(0.009)</td></tr><tr><td>Constant</td><td>2.303***(0.376)</td><td>19.197***(3.127)</td><td>2.130***(0.368)</td><td>-0.235(0.839)</td><td>19.336***(3.125)</td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>256,810</td><td>256,810</td><td>256,810</td><td>256,810</td><td>256,810</td></tr><tr><td>R-squared</td><td>0.038</td><td>0.041</td><td>0.050</td><td>0.016</td><td>0.043</td></tr><tr><td colspan="6">Notes: standard errors are enclosed in parentheses. The coefficients are significant at levels *** p &lt; 0.01, ** p &lt; 0.05, and * p &lt; 0.1.</td></tr></table>

## 5 Discussion

## 5.1 Key Findings

This study is the first to theoretically conceptualize and empirically test the effect of cultural values on rating deviation and review emotion in online restaurant reviews. First, we demonstrate that consumers from an individualist cultural background are more likely to deviate from prior opinion. Second, consumers from an individualist cultural background are more likely to express emotion in their reviews. Third, these two characteristics of online reviews can have important implications for review helpfulness.

## 5.2 Implications

This study offers several theoretical implications. Our work is the first to consider that cultural differences may affect consumers' tendency to deviate from (or conform to) past reviews. Recent work has suggested that the present review aggregation approach employed by many leading platforms (e.g., Yelp) tends to ignore the systematic differences in reviewer behavior and conformity in the review-generation process (Dai et al., 2012). Our findings point to a previously undocumented driver of the systematic differences in review characteristics. This driver relates to reviewers' cultural background, which not only has the potential to exacerbate or mitigate herding in review generation but also has similar negative implications for the optimality of existing review aggregation techniques.

Our work is also the first to consider how cross-cultural differences manifest in reviews' textual characteristics beyond their length. Consumers from individualist cultural backgrounds express more emotion in their reviews. In turn, both conformity (lacking rating deviation) and review emotion lead to lower review helpfulness. Our work is among the first to draw a connection between the cultural background (values) of authors and the perception of audiences toward the quality of the review content. These results imply that the operators of online review sites must recognize the systematic, cross-cultural differences in the produced content and that they must consider some approaches to mitigate biases whenever they damage a review's perceived helpfulness. For instance, review platforms may offer examples of “helpful” reviews to consumers that consider the reviewer's reviewing history or country of residence. Alternatively, review platforms may seek and solicit reviews from individuals with a particular cultural background to elicit helpful reviews for others.

Online review aggregators, such as those presented in this study, are likely to be of greatest use for products and services that cater to various customer segments; namely, consumers from different cultural backgrounds. If one aggregates reviews based on the reviewing tendencies of consumers (e.g., weighting reviews based on the cultural background of authors and their anticipated likelihood of under- or over-stating divergent opinions), one may improve the consumer search process, reduce search costs, and expect better purchase decisions.

Previous studies that have considered cross-cultural differences in online reviews have almost exclusively employed a two-country design to explore cross-cultural differences in the production and consumption of reviews (Chung & Darke, 2006; Koh et al., 2010; Fang et al., 2013). By contrast, this study leverages a large observational dataset of reviews that consumers from 52 countries wrote. Therefore, our findings have external validity.

## 5.3 Limitations and Opportunities

Similar to other studies, our work is subject to some limitations. First, we measured cultural values at the national level and then ascribed them to individuals based on their country of residence. A more accurate measure should employ a survey of each consumer based on the original measures of Hofstede (2001) or House et al. (2004). However, this approach entails surveying a large number of TripAdvisor users, which is impractical because of our limited access. We acknowledge this limitation and interpret the observed effects as derived from consumers' “cultural backgrounds” rather than their “cultural values” $^{5}$ . Future research may employ a different research design to address this limitation. For example, researchers may recruit reviewers, survey their cultural values at the individual level, and then ask them to complete a review task.

Second, a person may be born and raised in one country but immigrate to another country. Unfortunately, we cannot observe this behavior in our archival data. Nevertheless, this limitation is unlikely a prevalent issue in our sample and considering it would introduce noise into our estimations, which would prevent us from identifying the hypothesized effects. Given that we have observed significant estimates in our regressions, this limitation does not pose a significant problem for this study. We infer that our estimates are conservative.

Third, we could not measure the dynamics of helpful votes for each review (i.e., we lacked time stamps on helpful votes and could only observe the total number of votes that had accrued as of the data-collection period). Implicitly, our analyses assume that all helpful votes arrive immediately after one publishes a review. Ideally, we prefer to analyze the arrival of helpful votes dynamically because a review's conformity or deviation will vary over time as others write other, subsequent reviews. In other words, after its writing, a review may be in high or low agreement with all prior reviews but begin to agree with the overall body of opinion as subsequent reviews appear and, thus, affect the rate at which helpful votes arrive. However, this limitation does not pose a serious concern for our analyses. First, we observed a strong positive correlation (rho = 0.89) between the conformity of the author at the time of authorship (i.e., agreement with prior reviews) and the author's conformity to the overall body of reviews that were authored during the data-collection period (i.e., agreement with prior and subsequent reviews). This finding indicates that review deviation and conformity are relatively static values. Second, after repeating our analyses, we observed similar results in terms of signs and significance even after limiting our sample of data to those reviews that were published in the previous two weeks. Therefore, our inability to identify the dynamics of helpful vote arrival unlikely affected our results.

Fourth, we could not determine the degree to which self-selection in review authorship versus the compositional differences that emerged drove the variation in online review characteristics associated with authors' cultural background. In other words, consumers from collectivist cultures are more likely to opt out of reviewing when they are emotionally charged or hold a “different” opinion from prior reviewers. However, this limitation is a serious concern for our study. First, social psychology presents evidence that individuals from collectivist cultures are more susceptible to the opinions of peers and are more likely to conform to such opinions (see Bond and Smith (1996) for a review of this topic). Therefore, differences in the reviewing behavior may exist over and above the decision of whether or not to write a review. Second, despite its presence, self-selection does not have substantive implications for our results or estimates. Our hypotheses and empirical estimations draw relationships between cultural backgrounds and the characteristics of published reviews written by individuals from such backgrounds. We observed systematic differences in the review content regardless of whether one attributes such differences to deviations in opinion conditional on authorship or self-selection into authorship.

This study offers several opportunities for future research. First, future research may investigate different U.S. states as a source of heterogeneity to examine the effect of individualism on online reviews. Second, future studies may examine whether other dimensions of cultural values (e.g., uncertainty avoidance) can affect consumer behavior when producing or consuming online reviews. For example, future research could delve into cross-cultural differences in review consumption under different levels of product uncertainty (Dimoka, Hong & Pavlou, 2012; Hong & Pavlou, 2014). Third, our analyses of perceived helpfulness abstract away the possibility that the effects are moderated by the cultural values of the primary audience for a service provider. For instance, a recent work has provided early evidence of cross-cultural differences in online review consumption by reporting that individuals from collectivist cultures place greater value on negative reviews (Fang et al., 2013). Future studies may explore other differences in perceived helpfulness across cultures, such as whether individuals from collectivist or individualist cultures exhibit a similar preference for review deviation or conformity.

## References

Adomavicius, G., Bockstedt, J. C., Curley, S. P., & Zhang, J. (2013). Do recommender systems manipulate consumer preferences? A study of anchoring effects. Information Systems Research, 24(4), 956-975.

Ahmad, S. N., & Laroche, M. (2015). How do expressed emotions affect the helpfulness of a product review? Evidence from reviews using latent semantic analysis. International Journal of Electronic Commerce, 20(1), 76-111.

Asch, S. E. (1955). Opinions and social pressure. Scientific American, 193, 35-35.

Ba, S., & Pavlou, P. A. (2002). Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior. MIS Quarterly, 26(3), 243-268.

Bond, R., & Smith, P. B. (1996). Culture and conformity: A Meta-analysis of studies using Asch's (1952b, 1956) line judgment task. Psychological Bulletin, 119(1), 111-137.

Brehm, S., & Brehm, J. W. (1981). Psychological reactance: A theory of freedom and control. New York, NY: Academic Press.

Burtch, G., Ghose, A., & Wattal, S. (2014). Cultural differences and geography as determinants of online pro-social lending. MIS Quarterly, 38(3), 773-794.

Burtch, G., Hong, Y., Bapna, R., & Griskevicius, V. (Forthcoming). Stimulating online reviews by combining financial incentives and social norms. Management Science.

Butler, E. A., Lee, T. L., & Gross, J. J. (2007). Emotion regulation and culture: Are the social consequences of emotion suppression culture-specific? Emotion, 7, 30-48.

Cao, Q., Duan, W. J., & Gan, Q. W. (2011). Exploring determinants of voting for the “helpfulness” of online user reviews: A text mining approach. Decision Support Systems, 50(2),511-521.

Chen, Z., & Lurie, N. H. (2013). Temporal contiguity and negativity bias in the impact of online word of mouth. Journal of Marketing Research, 50(4), 463-476.

Chevalier, J., & Mayzlin, D. (2006). The effect of word of mouth online: Online book reviews. Journal of Marketing Research, 43(3), 345-354.

Chung, C. M., & Darke, P. R. (2006). The consumer as advocate: Self-relevance, culture, and word-of-mouth. Marketing Letters, 17(4), 269-279.

Cialdini, R., Wosinska, W., Barrett, D. W., Butner, J., & Gornik-Durose, M. (1999). Compliance with a request in two cultures: The differential influence of social proof and commitment/consistency on collectivists and individualists. Personality and Social Psychology Bulletin, 25(10), 1242-1253.

Dai, W., Jin, G., Lee, J., & Luca, M. (2012). Optimal review aggregation of consumer ratings: An application to Yelp.com (NBER working paper).

Danescu-Niculescu-Mizil, C., Kossinets, G., Kleinberg, J., & Lee, L. (2009). How opinions are received by online communities: A case study on Amazon.com helpfulness votes. In Proceedings of the 18th international Conference on World Wide Web (pp. 141-150). ACM.

Dellarocas, C. (2003). The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Science, 49(10), 1407-1424.

Dimoka, A., Hong, Y., & Pavlou, P. A. (2012). On product uncertainty in online markets: Theory and evidence. MIS Quarterly, 36(2), 395-426

Fang, H., Zhang, J., Bao, Y., & Zhu, Q. (2013). Towards effective online review systems in the chinese context: A cross-cultural empirical study. Electronic Commerce Research and Applications, 12(3), 08-220.

Friedlmeier, W., Corapci, F., & Cole, P. M. (2011). Socialization of emotions in cross-cultural perspective. Social and Personality Psychology Compass, 5(7), 410-427.

Giannetti, M., & Yafeh, Y. (2012). Do cultural differences between contracting parties matter? Evidence from syndicated bank loans. Management Science, 58(2), 365-383.

Ghose, A., & Ipeirotis, P. G. (2011). Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions on Knowledge and Data Engineering, 23(10), 1498-1512.

Godes, D., & Silva, J. C. (2012). Sequential and temporal dynamics of online opinion. Marketing Science, 31(3), 448-473.

Goes, P. B., Lin, M., & Yeung, C. M. A. (2014). “Popularity effect” in user-generated content: Evidence from online reviews. Information Systems Research, 25(2), 222-238.

Goleman, D. (1990). The group and the self: New focus on a cultural rift. The New York Times. Retrieved from http://www.nytimes.com/1990/12/25/science/the-group-and-the-self-new-focus-on-a-cultural-rift.html

Hofstede, G. H. (2001). Culture's consequences: International differences in work-related values. Thousand Oaks, CA: Sage.

Holtgraves, T. (1997). Styles of language use: Individual and cultural variability in conversational indirectness. Journal of Personality and Social Psychology, 73(3), 624-637.

Hong, Y., Chen, P., & Hitt, L. (2013). Measuring product type with dynamics of online review variance. In Proceedings of International Conference on Information Systems.

Hong, Y., & Pavlou, P. A. (2014). Product fit uncertainty in online markets: Nature, effects, and antecedents. Information Systems Research, 25(2), 328-344.

Hong, Y., & Pavlou, P. A. (2014). Is the world truly “flat”? Empirical evidence from online labor markets (Research paper no. 15-045). Fox School of Business.

House R. J., Hanges, P. J., Javidan, M., Dorfman, P. W., & Gupta, V. (Eds.). (2004). Culture, leadership, and organizations: The GLOBE study of 62 societies. Thousand Oaks, CA: Sage.

Huang, H. (2005). A cross-cultural test of the spiral of silence. International Journal of Public Opinion Research, 17(3), 324-345.

Huang, N., Burtch, G., Hong, Y., & Polman, E. (2016). Effects of multiple psychological distances on construal and consumer evaluation: A field study of online reviews. Journal of Consumer Psychology, 26(4), 474-482.

Huang, N., Hong, Y., & Burtch, G. (2015). Anonymity and language usage: A natural experiment of social network integration. In Proceedings of the 35 $^{th}$ International Conference on Information Systems.

Liu, Y., Chen, P. Y., & Hong, Y. (2014). Value of multi-dimensional rating systems: An information transfer view. In Proceedings of the 35 $^{th}$ International Conference on Information Systems.

Inglehart, R., & Welzel, C. (2010). Changing mass priorities: The link between modernization and democracy. Perspectives on Politics, 8(2), 551–567.

Inglehart, R., & Oyserman, D. (2004). Individualism, autonomy, self-expression. The human development syndrome. In International studies in sociology and social anthropology (pp. 74-96). Institute for Research on Intercultural Cooperation.

King, R. A., Racherla, P., & Bush, V. D. (2014). What we know and don't know about online word-of-mouth: A review and synthesis of the literature. Journal of Interactive Marketing, 28(3), 167-183.

Koh, N. S., Hu, N., & Clemons, E. K. (2010). Do online reviews reflect a product's true perceived quality? An investigation of online movie reviews across cultures. Electronic Commerce Research and Applications, 9(5), 374-385.

Kwark, Y., Chen, J., & Raghunathan, S. (2014). Online product reviews: Implications for retailers and competing manufacturers. Information Systems Research, 25(1), 93-110.

Lam, D., Lee, A., & Mizerski, R. (2009). The effects of cultural values in word-of-mouth communication. Journal of International Marketing, 17(3), 55-70.

Lee, D., Hosanagar, K., & Nair, H. (2013). The effect of advertising content on consumer engagement: Evidence from Facebook.

Lee, T. Y., & Bradlow, E. T. (2011). Automated marketing research using online customer reviews. Journal of Marketing Research, 48(5), 881-894.

Lee, Y. J., Hosanagar, K., & Tan, Y. (2015). Do I follow my friends or the crowd? Information cascades in online movie ratings. Management Science, 61(9), 2241-2258.

Leidner, D. E., & Kayworth, T. (2006). Review: A review of culture in information systems research: Toward a theory of information technology culture Conflict. MIS Quarterly, 30(2), 357-399.

Li, X., & Hitt, L. (2008). Self-selection and information role of online reviews. Information Systems Research, 19(4), 456-474.

Liu, Y., Chen, P., & Hong, Y. (2014). Value of multi-dimensional rating systems: An information transfer view. In Proceedings of the 35th International Conference on Information Systems.

Lu, X., Ba, S., Huang, L., & Feng, Y. (2013). Promotional marketing or word-of-mouth? Evidence from online restaurant reviews. Information Systems Research, 24(3), 596-612.

Ludwig, S., De Ruyter, K., Friedman, M., Brüggen, E. C., Wetzels, M., & Pfann, G. (2013). More than words: The influence of affective content and linguistic style matches in online reviews on conversion rates. Journal of Marketing, 77(1), 87-103.

Moe, W., & Schweidel, D. (2012). Online product opinions: Incidence, evaluation, and eevolution. Marketing Science, 31(3), 372-386.

Muchnik, L., Aral, S., & Taylor, S. J. (2013). Social influence bias: A randomized experiment. Science, 341(6146), 647-651.

Mudambi, S. M., & Schuff, D. (2010). What makes a helpful online review? A study of customer reviews on Amazon.com. MIS Quarterly, 34(1), 185-200.

Nagle, F., & Riedl, C. (2014). Online word of mouth and product quality disagreement. In Proceedings of the Academy of Management Annual Meeting.

Niedenthal, P., Krauth-Gruber, S., & Ric, F. (2006). Psychology of emotion interpersonal, experimental, and cognitive approaches. New York, NY: Psychology Press.

Pavlou, P., & Dimoka, A. (2006). The nature and role of feedback text comments in online marketplaces: Implications for trust building, price premiums, and seller differentiation. Information Systems Research, 17(4), 392-414.

Pennebaker, J. W., Francis, M. E., & Booth, R. J. (2001). Linguistic inquiry and word count: LIWC 2001. Mahway: Lawrence Erlbaum Associates.

Schoorman, F. D., Mayer, R. C., & Davis, J. H. (2007). An integrative model of organizational trust: Past, present, and future. Academy of Management Review, 32(2), 344-354.

Spiller, S. A., Fitzsimons, G. J., Lynch Jr, J. G., & McClelland, G. H. (2013). Spotlights, floodlights, and the magic number zero: Simple effects tests in moderated regression. Journal of Marketing Research, 50(2), 277-288.

Sridhar, S., & Srinivasan, R. (2012). Social influence effects in online product ratings. Journal of Marketing, 76(5), 70-88.

Sun, M. (2012). How does the variance of product ratings matter? Management Science, 58(4), 696-707.

Takahashi, K., Ohara, N., Antonucci, T., & Akiyama, H. (2002). Commonalities and differences in close relationships among the Americans and Japanese: A comparison by the individualism/collectivism concept." International Journal of Behavioral Development, 26(5), 453-465.

Triandis, H. C. (1995). Individualism and collectivism. Boulder, CO: Westview Press.

Tsai J. L., Miao F. F., Seppala E., Fung H. H., & Yeung D. Y. (2007). Influence and adjustment goals: Sources of cultural differences in ideal affect. Journal of Personality and Social Psychology, 92(6), 1102-1117

Wang, C., Zhang, X., & Hann, I. H. (Forthcoming). Socially nudged: A quasi-experimental study of friends' social influence in online product ratings. Information Systems Research.

Wu, F., & Huberman, B. (2008). How public opinion forms. In Proceedings of the 4th International Workshop on Internet and Network Economics (pp. 334-341) Berlin: Springer.

Yaveroglu, I. S., & Donthu, N. (2002). Cultural influences on the diffusion of new products. Journal of International Consumer Marketing, 14(4), 49-63.

Yin, D., Bond, S., & Zhang, H. (2014). Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. MIS Quarterly, 38(2), 539-560.

## About the Authors

Yili Hong is an Assistant Professor and co-director of the Digital Society Lab in the Department of Information Systems at the W. P. Carey School of Business of Arizona State University. He obtained his PhD in Management Information Systems at the Fox School of Business, Temple University. His research interests are in the areas of Sharing Economy, Online Platforms and User-generated Content. His research has been published in journals such as Information Systems Research, Management Information Systems Quarterly, Management Science, Journal of the Association for Information Systems, and Journal of Consumer Psychology. He is the winner of the ACM SIGMIS Best Dissertation Award and runner-up of the INFORMS ISS Nunamaker-Chen Dissertation Award. His papers have won best paper awards at the International Conference on Information Systems and America's Conference on Information Systems. He is an external research scientist for a number of high-profile tech companies, including Freelancer, fits.me, Yamibuy, and Meishijie.

Nina (Ni) Huang is a PhD Candidate of Business Administration at Fox School of Business, Temple University. Her research focuses on user generated content, online and mobile platforms, and electronic commerce. Her research approaches include econometric modeling, text analytics, and field experimentation. Her work has been published in journals and conferences, such as Journal of Consumer Psychology, the International Conference on Information Systems, Conference on Information Systems and Technology, the Statistical Challenges in eCommerce Research, NET Institution Conference, and CODE@MIT. Her research has received funding from the NET Institute, Amazon Web Services (AWS) Cloud Credits for Research Program.

Gord Burtch is an Assistant Professor of Information & Decision Sciences at the University of Minnesota's Carlson School of Management. He holds a PhD from Temple University's Fox School of Business. His research, which employs empirical analyses rooted in econometrics and field experimentation to identify and quantify the drivers of individual behavior in online social contexts, has been published in various top IS journals, including MIS Quarterly, Information Systems Research, Management Science and the Journal of the Association for Information Systems. His work has been recognized with financial support from a number of granting agencies, including the Kauffman Foundation, 3M Foundation and NET Institute, and has been cited by a variety of major outlets in the popular press, including The New York Times, NPR, Time Magazine, Forbes, Vice, Wired, the LA Times, Pacific Standard and PC Magazine. He recently received the Distinguished Service Award from Management Science, he has repeatedly served as an Associate Editor and Track Chair at the International Conference on Information Systems, and he is Co-Chair of the 2016 Workshop on Information Systems and Economics.

Chunxiao Li is a PhD student in W. P. Carey School of Business, Arizona State University. Her research interests include economics of IS, online markets, business value of social media, social influence, and social networks.

Copyright © 2016 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints or via e-mail from publications@aisnet.org
