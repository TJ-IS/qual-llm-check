---
otero_id: 14858
otero_key: "6EC8QF27"
title: "USING FORUM AND SEARCH DATA FOR SALES PREDICTION OF HIGH-INVOLVEMENT PROJECTS"
authors: "Tomer Geva; Gal Oestreicher-Singer; Niv Efron; Yair Shimshoni"
year: "2017"
journal: "MIS Quarterly"
doi: "10.25300/misq/2017/41.1.04"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# USING FORUM AND SEARCH DATA FOR SALES PREDICTION OF HIGH-INVOLVEMENT PROJECTS<sup>1</sup>

Tomer Geva and Gal Oestreicher-Singer

The Coller School of Management, Tel Aviv University, P.O. Box 39040,

Tel Aviv 6997801, ISRAEL

{tgeva@tau.ac.il} {galos@tau.ac.il}

Niv Efron and Yair Shimshoni

Google, Tel Aviv, ISRAEL

{niv@google.com} {shimsh@google.com}

A large body of research uses data from social media websites to predict offline economic outcomes such as sales. However, recent research also points out that such data may be subject to various limitations and biases that may hurt predictive accuracy. At the same time, a growing body of research shows that a new source of online information, search engine logs, has the potential to predict offline outcomes. We study the relationship between these two important data sources in the context of sales predictions. Focusing on the automotive industry, a classic example of a domain of high-involvement products, we use Google’s comprehensive index of Internet discussion forums, in addition to Google search trend data. We find that adding search trend data to models based on the more commonly used social media data significantly improves predictive accuracy. We also find that predictive models based on inexpensive search trend data provide predictive accuracy that is comparable, at least, to that of social media data-based predictive models. Last, we show that the improvement in accuracy is considerably larger for “value” car brands, while for “premium” car brands the improvement obtained is more moderate.

Keywords: Search trends, forums, social media, word-of-mouth, consumers’ interest, sales prediction, online data, high involvement products

## Introduction

The availability, scale, and richness of detail of social media data have encouraged researchers as well as practitioners to explore means of using such data to explain and predict offline economic outcomes. As a result, a dominant stream of research has emerged that focuses on abstracting data from social media websites such as blogs or Internet discussion forums as a measure for the word of mouth (WOM) a product enjoys. Previous work in this stream has repeatedly provided evidence that the number of mentions that a product receives in social media, as well as the sentiment expressed in such data, can predict offline outcomes (Choi and Varian 2009; Wu and Brynjolfsson 2009).

Social media monitoring, whereby companies obtain information by sifting through data from social media websites, has also become a widespread practice in industry. Industry reports estimate that in 2014 companies spent 620 million dollars on social media monitoring, which is expected to grow to more than 2.7 billion dollars in 2019.<sup>2</sup> Social media monitoring is considered less expensive than traditional market research, which involves surveys or focus groups. In practice, however, it is often costly to collect and process social media data, especially when implementing more complex content processing procedures such as sentiment analysis.<sup>3</sup>

Cost is not the only challenge to companies attempting to exploit online social media data to predict economic outcomes. In fact, industry reports suggest that very few consumers actually contribute actively to social media discussions. Reports show that, on typical social media websites, only about 10% of website users are active participants, and that most of the content is contributed by only 1% of users.<sup>4</sup> Thus, most users remain quiet observers or “lurkers,” a phenomenon known as participation inequality. While it is not uncommon to use small sample sizes (e.g., in surveys) to capture consumers’ intentions for predictive purposes, such samples are typically selected with care, with the aim of ensuring representation of the opinions of the general consumer base. However, recent work has pointed out that social media data has significant biases and limitations, including insufficient and skewed representativeness of the consumer population; biased representation of the true underlying product/brand evaluation; biases due to differences across brand and products as well as temporal variations; and potential intentional manipulation (most recently, Lovett et al. 2013; Moe and Schweidel 2012; Moe and Trusov 2011). Moreover, many of these biases have complex dynamics that are difficult to mitigate using modeling procedures.

Interestingly, a common factor that underlies, or contributes to, many of the reported biases associated with social media data is the visibility of social media posts. Previous research has shown that the fact that social media mentions are visible to others affects users’ willingness to participate in online discussions, causes users to express views that differ from their true opinions, and can also lead firms and even customers to attempt to manipulate online content.

A common practice in the context of predictive research is to mitigate flaws in imperfect data by enriching the data with additional, meaningful, information. Nevertheless, it is important that the additional data will not be subject to the specific biases and flaws that the researcher is trying to alleviate. Herein, we focus on search trend data as an online data source that can potentially enrich social media data. Search engine logs, aggregating billions of individual search engine queries, have been made publicly available through tools such as Google Trends. It has been argued that search data actually reflect the “true intentions” of consumers (Wu and Brynjolfsson 2009) and can serve as a proxy for consumers’ interest in a product (Hu et al. 2014). Most importantly for our context, search trend data are very different in nature from social media data. Unlike social media postings, search is done in private. As consumers search in private, they have no self-presentation concerns, have no (or very limited) awareness of other searchers’ activity, and no potential to influence sales. Additionally, search is conducted by a much larger sample of the population compared with active participation in social media discussions. While notably search trend data cannot mitigate all the known biases and limitations of social media, its private nature and widespread use render this data as a promising candidate to be added to social media databased prediction models.

Interestingly, the interplay between these two online data sources and its relationship to sales prediction has received very little research attention thus far. This raises an important question that lies at the core of the current paper: Can search trend data successfully augment social media data for sales prediction? Specifically, our first research question examines whether predictive models based on a combination of search trend data and social media data are superior to those based on either social media or search trend data alone. If search trend data offer useful predictive information that supplements social media data, and vice versa, the combination of both data sources may yield more accurate sales prediction models. Nevertheless, the risk of adding a second source of data is that if the additional data do not contain additional valuable information, it may potentially lead to over-fitting and ultimately reduce out-of-sample predictive accuracy. Therefore, superiority of a model combining the two data sources would show that the two data sources contain nonoverlapping, useful, information.

Although search trend information constitutes a potentially useful data source that can be accessed at low cost and might alleviate some of the biases associated with social media data, it is important to note that search trend data also has some downsides of its own. In particular, search trend data is not as rich as social media data; for example, it has very little capacity to reflect user sentiment. While search volume indicates users’ level of interest in a product, it may not be clear whether an increase in interest is due to positive or negative circumstances (e.g., launching of a new car model or a car model recall). See the “Related Literature” and “Research Context” sections for more details on search trend data.

The fact that search trend data and social media data have different advantages and limitations provides the setting for our second research question. This question examines whether sales prediction models using search trend data can obtain similar or better accuracy compared with more commonly used sales prediction models that are based on the sentiment and volume of social media data. If sales prediction models using inexpensive search trend data (available for free on Google trends) can be shown to yield predictive accuracy that is comparable to or better than the predictive accuracy obtained using social media data, then managers might be encouraged to consider replacing social media data with search trend data in applied prediction settings.<sup>5</sup>

Finally, previous research on WOM has provided evidence that consumers’ motivation to engage in online WOM differs across brands, and that consumers may be particularly inclined to converse about highly regarded or high-quality brands, about luxury goods, or about brands with a high degree of differentiation (Lovett et al. 2013). Such differences in online WOM activity may naturally affect the informativeness of social media data for prediction. Therefore, our third research question explores whether the benefits of augmenting social media data with search trend data vary across brands. Specifically, we compare between premium and value brands.

Notably, evidence suggests that the answers to our research questions depend on the specific product context in which data are being collected. In fact, information-search behaviors have been shown to vary for different levels of product involvement. Product involvement refers to consumers interest in a product and their perceptions regarding its importance (Blackwell et al. 2001) and the perceived risk associated with it (Dholakia 2001). For instance, durable products such as cars or consumer electronics are typical examples of high-involvement products, whereas consumable products, such as groceries, movies, and music, are typical examples of low-involvement products (Moorthy et al. 1997; Viswanathan et al. 2007). Simply stated, the more important the product is to a consumer, the more motivated the consumer is to search and be involved in the decision. Gu et al. (2012) observed that for a high-involvement product (digital cameras) consumers did not suffice with the WOM available on the retailer’s website (Amazon.com) and actively searched for external sources of information online (consumer forums and opinion websites). The authors empirically showed that such external sources of WOM and their sentiment have a strong effect on sales of such products. This observation highlights two key premises of our work: consumers of high involvement products actively search for information, which implies that they leave “footprints” in search logs; and at the same time, they are strongly influenced by the WOM available on social media. Therefore, in this work we will limit our discussion to high-involvement products, for which both search and social media are expected to influence purchase decisions.

Specifically, in studying the interplay between search trend data and social media data, we will focus on the automotive industry, a classic example of a domain of high-involvement products. Given that, for most consumers, the purchase of a car is a substantial financial expense and an informationintensive decision, we expect both social media and search to have important roles in the purchase decision. Moreover, the automotive industry provides us with the opportunity to answer our third research question, as it includes both premium and value brands. Additionally, the automotive industry’s vast marketing budget (estimated to spend \$15.1 billion on advertising in 2015 alone), as well as its importance to the economy, render this industry an interesting test-bed with important practical implications.<sup>6</sup>

To represent search trend data, we use information from Google search query logs. To represent social media data, we rely on Google’s comprehensive index of Internet discussion forums (hereafter referred to as “forum data”). The latter is, to the best of our knowledge, the most comprehensive forum data set that has been made available for any academic research. The modeling methodology in this study is predictive, rather than explanatory (Shmueli and Koppius 2011). The substantial differences between predictive and explanatory methodologies, their use cases, and the justifications for using each approach are thoroughly detailed by Shmueli (2010) and Shmueli and Koppius (2011). Specifically, Shmueli and Koppius state that predictive methodology is particularly useful for “assessment of the predictability of empirical phenomena” (p. 553). Indeed, assessment of inherent predictability of sales given different online data sources is at the core of this study’s research questions. Once the predictive capabilities of the data have been assessed, subsequent studies can generate new theories on the basis of the obtained outcomes. Additionally, accurate sales forecasting has considerable practical implications and is a critical factor in a variety of key business processes, including inventory control, manufacturing decisions, and marketing activities.

We find that forecasting models that incorporate both forum data and search trend data provide significantly more accurate sales predictions compared with models using forum-based data alone, suggesting that the two data sources contain nonoverlapping, useful, information. We also find that predictive models based on inexpensive search trend data provide predictive accuracy that is at least comparable to that of more commonly used forum-data-based predictive models. Finally, we show that when adding search trend-based data to forumbased data, prediction results outperform the results of using forum-data, for both value and premium brands. Nevertheless, this difference is considerably larger for value car brands, while for premium car brands the improvement obtained by adding search trend data is more moderate.

## Related Literature

In this work we draw mainly on two main streams of research. The first studies the predictive and explanatory power of modeling using social media data, and the second includes a smaller but growing body of work that documents the predictive power of search trend data.

## Modeling Using Social Media Data

The prevalence of social media platforms in which users can publicly communicate product information to one another (platforms such as discussion groups, forums and even product reviews on online sellers’ websites) has led to an increase in publicly available WOM. This WOM is different from traditional person-to-person communication, which is often between familiar parties and limited in reach. Marketing and information systems researchers have devoted substantial attention to the effects of social media data on sales. For example, posts on websites such as Yahoo! Movies have been linked to box office revenues (Duan et al. 2008a; Liu 2006); music blog buzz has been shown to impact music listening (Dewan and Ramaprasad 2012) and sales (Dewan and Ramaprasad 2009; Dhar and Chang 2009); book reviews published on a seller’s own website were shown to impact the sales of reviewed books (Chevalier and Mayzlin 2006); and conversations on Usenet have been shown to explain TV ratings (Godes and Mayzlin 2004). Researchers have also studied the interplay between online social media mentions and critics’ reviews (Chakravarty et al. 2010) and its usefulness for predicting movie revenues (Dellarocas et al. 2007); as well as the impact of internal (the firm’s own website) and external (other websites) mentions on sales (Gu et al. 2012). Other researchers evaluated the positive feedback effect of sales on social media mentions (Duan et al. 2008b) and the optimal response of firms to social media data (Chen and Xie 2008; Dellarocas 2006). In addition, several studies have evaluated various moderating factors that affect the influence of social media data-based mentions on sales; these factors include product and consumer characteristics (Zhu and Zhang 2010) as well as reviewer characteristics (Hu et al. 2008) and identity exposure (Forman et al. 2008). Hill et al. (2012) study the real-time social media response to TV advertisements aired during the Super Bowl. In the context of the automotive industry, social media mentions of car brands have been used to study the market structure and competitive landscape of the industry (Netzer et al. 2012).

The valence, or sentiment, of social media mentions has been shown to carry importance for predictions. However, findings on this topic are somewhat varied. For instance, Liu (2006) and Duan et al. (2008b) have found that a product’s sales are affected by the volume of its social media mentions but not by the valence of these mentions or by user ratings. In contrast, more recent studies such as those of Rui et al. (2012) and Chintagunta et al. (2011) report valence as an important factor in explaining sales. Rui et al. suggest that the difference between their outcomes and prior findings may have resulted from their use of an automated classifier, rather than reported user ratings, to measure valence. Chintagunta et al. attribute the difference in valence results to their improved modeling, which takes into account various complications of using a national-level data set that was not considered in previous studies.

## The Predictive Power of Search Trends

The second stream of research we draw from focuses on the use of search engine logs, commonly known as search trends, for predicting a variety of economic and social events. While search is conducted privately, tools such as Google Trends have made search logs publicly available at the aggregate level. These logs have been used for prediction by various studies in different contexts. For instance, Choi and Varian (2009, 2011) used search trend data to demonstrate contemporaneous predictive capabilities in various fields, including sales of motor vehicle parts, initial claims for unemployment benefits, travel, consumer confidence index, and automotive sales. Wu and Brynjolfsson (2009) utilized Google search data to predict future house sales and price indices as well as home appliance sales. Vosen and Schmidt (2011) used Google search data to predict private consumption, while Ginsberg et al. (2008) used Google search query data to build an early detection system for influenza epidemics. Du and Kamakura (2012) developed a method for extracting latent dynamic factors in multiple time series and demonstrated their method by utilizing search trend data and predicting automotive sales. Seebach et al. (2011) also used Google data to predict automotive sales. Hu et al. (2014) constructed a model that uses search trend data and automotive sales data to decompose the impact of advertising into two components: generating consumer interest in information search and converting the interest into sales. They showed that search trend data are not merely predictors but can also represent the level of interest in different products. Goel et al. (2010) used Yahoo!’s search engine data to predict various outcomes, including weekend box office revenues for feature films, video game sales, and song ranks. The latter study points to several factors that can affect predictions based on search data, including variability in the predictive power of search in different domains and possible difficulties in finding suitable query terms. It also discusses the need to utilize benchmark data when available. An explanation of why web search data are useful in predicting future sales is offered by Wu and Brynjolfsson, who suggest that web search logs constitute “honest signals of decision-makers’ intentions” (p. 13). That is, if buyers reveal their true intentions to purchase, future sales levels are expected to correspond to these intentions.

To the best of our knowledge, the interplay between social media data and search trend logs has not been previously studied in the context of sales prediction. In fact, only one previous paper has contrasted these two sources of data: Luo et al. (2013) combined social media data (using web blogs and consumer ratings), Google searches, and web traffic data in a model of firm equity value. However, their paper focused on a substantially different domain (firm equity value versus automotive sales), raised different research questions, and used a different methodology. Given the work of Luo et al., our paper makes the following novel contributions for better understanding the predictive potential of search trends and social media data: (1) our paper is the first to evaluate the interplay and complementarity of search trends data and social media data in predictive research settings; (2) Luo et al. modeled the two data sources jointly, thus capturing the marginal informativeness of each source given that the other source exists; our paper not only looks at the marginal informativeness of the two sources but also offers useful insights by evaluating the two sources as substitutes, and (3) finally, our paper provides additional insights regarding the effect of augmenting social media data with search trend data given different brand and product characteristics.

## Research Context

This paper focuses on the predictive capacity of data. One critical requirement of predictive modeling is that the available data represent the underlying phenomena. Recent literature has pointed to various aspects of social media data that create incomplete or biased representations of the underlying phenomena of interest. Those biases may impact the predictive power of social media data and their correction may require the introduction of new sources of data. In what follows, we first detail the known concerns and biases of social media data, and proceed to discuss how search trend data can be used to mitigate some of those biases and improve predictive performance. We also discuss the use of search trend and social media data for predictive purposes with respect to the level of consumer involvement with the product, and the specific case of automotive sales prediction.

## Biases and Limitations Associated with the Use of Social Media Data for Prediction

## Representativeness of the Consumer Population

A first potential source of bias relates to the question of who chooses to participate in social media discussions, and whether these individuals represent the general population. As mentioned above, industry reports suggest that relatively few consumers of social media content (approximately 10% of all social media website users) actually contribute actively to online social media discussions, and that the majority of content is produced by only 1% of the users. While the large absolute volume of social media users may mitigate the sample size problem, another concern is whether the sample of active participants constitutes a good representation of the entire population.

Indeed, there is evidence that the minority of consumers who do participate in social media discussions are not a random representation of the general consumer population or even of the population of social media users. For example, Dellarocas and Narayan (2006) show that individuals with extreme opinions, both positive and negative, are more likely to post opinions online compared with individuals with more moderate opinions. Moreover, this biased representation may involve complex social dynamics: Moe and Schweidel (2012) report that a user’s decision regarding whether to participate in an online discussion is strongly dependent on opinions that were previously posted in that discussion, and that different users are affected in different ways by the types of opinions posted. Specifically, the authors show that preexisting discussions characterized by consensus encourage participation from more positive and less-involved consumers, whereas disagreement encourages participation from more-involved consumers.

## Biased Representation of Product Evaluation

Recent research shows that even when users choose to participate in online discussions, their stated preferences and opinions may differ from their true underlying product evaluations. That is, the online social interaction may bias what they write. For instance, Schlosser (2005) shows in an experimental setting that users who post opinions online are influenced by the negative opinions of others because of selfpresentational concerns. Moreover, in addition to showing that different types of preexisting discussions encourage subsequent participation from different types of users, Moe and Schweidel (2012) suggest that users tailor their posts in accordance with the content of those pre-existing discussions. In particular, customers who join a discussion characterized by consensus are likely to exhibit bandwagon behavior. In contrast, users who join discussions characterized by disagreement exhibit more differentiating behavior. Similarly, Moe and Trusov (2011) show that consumers’ online product ratings are influenced by previously posted ratings and quantify the sales impact of observed social dynamics.

## Temporal Shifts in Online Reviews

Social media information has also been shown to be subject to shifts in review content over time. Li and Hitt (2008) show that product reviews decline over time, and suggest that this trend can be attributed to product life-cycle. Godes and Silva (2012) observe a similar downward trend in product ratings over time and associate it with the number of reviews that a product accumulates. In particular, they suggest an order bias, according to which a product’s average rating declines as it attracts additional reviews. Hong et al. (2014) show that, in the case of pure search products, the variance of product ratings decreases with the number of ratings; for experience products, however, the variance of ratings may remain constant or increase, depending on the importance of the experience attributes in determining consumer utility.

## Intentional Manipulation

Several recent works (Dellarocas 2006; Mayzlin et al. 2014) have pointed to the potential of intentional manipulation of online reviews by individuals or firms. Luca and Zervas (2015) show that a large percentage of reviews on the Yelp website (16%) are suspected to be manipulated, and that the likelihood of review manipulation may vary substantially in accordance with various factors such as level of competition and initial reputation. Furthermore, Anderson and Simester (2014) find that 5% of reviews are posted by customers who, on the one hand, have no financial incentive to influence product ratings, yet, on the other hand, show no record of ever purchasing the product they reviewed. (These reviews are also significantly more negative than other reviews.) The authors’ findings suggest that the phenomena of product rating manipulation may be far more prevalent than expected.

## Effects of Product Characteristics

Recent work has shown that different products and brands have substantially different representations in social media. These differences in online representation involve complex dynamics that go beyond the simple differences in mean and variance that have typically been addressed in studies thus far<sup>.</sup> For instance, Lovett et al. (2013) relate brand characteristics to online and offline WOM patterns. They find that contribution to online discussions is mostly influenced by social drivers (such as the level of differentiation, esteem, and relevance) as well as by functional drivers (such as complexity and familiarity). For example, they find that in the online environment, people tend to talk about less complex brands, and also less about brands with a lower level of differentiation. In the context of this paper, cars can be considered highly complex brands, and hence are expected to be mentioned less frequently in social media outlets, which consequently may impact the predictive power of the associated social media data. Hong et al. (2014) discuss how rating dynamics vary across product types, specifically distinguishing between experience and search products. Furthermore, they show that online reviews can help infer product type (experience or search product). Berger and Schwartz (2011) show that, compared with less interesting products, interesting products stimulate higher levels of immediate WOM but, contrary to intuition, do not receive more ongoing WOM over multiple months or overall. Also, products that are more publicly visible receive more WOM both immediately after being experienced and over time.

Additionally, several recent studies have compared online mentions associated with hedonic versus utilitarian products. Kronrod and Danziger (2013) show that the language that consumers use when sharing experiences about hedonic consumption differs from the language used to describe utilitarian consumption. Berger and Milkman (2012) show that high or low emotional involvement, often linked to hedonic and utilitarian features, respectively, shapes consumers’ sharing behaviors. Schulze et al. (2014) also show that hedonic and utilitarian products are associated with different viral marketing mechanisms.<sup>7</sup> In the “Results” section, we contrast predictive accuracy for high-end and low-end automotive brands, which vary across the hedonic/utilitarian spectrum.

## Addressing Social-Media-Driven Data Biases

Modeling and data handling techniques can be used to mitigate some of the social media-driven data biases. For instance, de-trending techniques may adjust for certain timedependent changes in the volume and sentiment of social media mentions. The use of per-product dummy variables, or per-product normalization, may account for some of the differences across different products<sup>.</sup> However, most of the biases discussed above involve complex dynamics that need to be addressed through complex modeling processes that are difficult to come by (e.g., adjusting for factors such as previous postings and user personality, which influence user participation levels and distort users’ stated product evaluations). Moreover, in some cases, the current level of understanding of process dynamics is limited (e.g., why do individual users with no clear vested interest post fake reviews?), thereby hindering researchers’ capacity to account for these dynamics in their modeling. In other cases, process dynamics are time-dependent, and it may not be clear to what extent they continue to influence economic outcomes after the model training period is over. In sum, the complex and sometimes unclear characteristics of social-media-driven bias may limit corrective modeling efforts, especially when there is a need to adjust for multiple biases or data limitations simultaneously. Indeed, social media data is used in most cases without any modeling adjustments or only with minor adjustments.

Alongside modeling choices, another common means of alleviating the effect of flaws in imperfect data is to enrich the data with additional, meaningful, information. We suggest that search trend data can supplement social media data in this manner, as elaborated below.

## Combining Search Trend and Social Media Data

Two attributes of online search account for the importance of search trend data for our context: (1) the widespread use of online search and (2) the fact that online search is conducted in private. These aspects combined with the ease of obtaining search trend data render this source of information a promising candidate to mitigate various predictive biases associated with social media data. As discussed above, one way to improve predictive accuracy and alleviate biases in available data is to overlay the data with additional data that is not subject to the same biases. In our context, this could be achieved by augmenting social media data with search trend data that is not subject to social media data’s biases and limitations. Specifically, as consumers’ individual search behavior is not revealed to others, many of the factors that bias the behaviors of social media users do not apply to search behavior. For example, many of the biases discussed above in the “Representativeness of the Consumer Population” and “Biased Representation of Product Evaluation” sections are consequences of users’ self-presentation concerns and awareness of other users’ activities. In contrast, when performing online search, users have no self-presentation concerns and have very limited awareness of other searchers’ activity. As a result, search trend data are resilient to many of the factors and complex dynamics that often affect and skew social media data. Additionally, the widespread use of online search makes it much more robust to sample size issues that potentially affect social media data and are caused by low participation levels. Furthermore, as individual search behavior cannot normally be used to manipulate or influence sales, search trend data are unaffected by the intentional manipulation biases reported above.

Although search trend information has successfully been used in previous studies for prediction and is not expected to suffer from the biases that affect social media data, it is important to note that this data source also has limitations and downsides. First, as mentioned above, compared with social media, search trend information is relatively poor in terms of content and does not reflect user sentiment. Thus, search trend data may not reflect whether interest in a product is due to positive or negative circumstances. Second, search trend information, such as that provided by the Google Trends tool, is typically available only at an aggregate level, and raw searches are generally not made available to researchers. Therefore, search trend data are not as rich and granular as social media data, which commonly include individual-level postings.<sup>8</sup> Moreover, the inability to access raw searches hinders researchers’ capacity to detect and analyze additional possible biases and limitations that may characterize search trend data.

This tradeoff between the useful properties of search trend data and their potential limitations as a means of improving social media data-based predictions, and as an alternative source to social media data, is the background for our first two research questions mentioned above: Are predictive models based on a combination of search trend data and social media data superior to those based on social media or search trends data alone? Can sales prediction models using search trend data obtain similar or better accuracy compared with more commonly used sales prediction models that are based on social media sentiment and volume?

Finally, social media WOM data are reportedly subject to variations in representation dynamics across products and brands. As mentioned earlier, one of the fundamental differences between our two data sources—social media and search trends—is in their visibility: While search is conducted in private, social media mentions are publicly visible. Specifically, previous work suggests that, because of their visibility, social media mentions may trigger biases (as discussed above) and may also be associated with different outcomes in the cases of premium versus value brands. In effect, research in the context of online as well as offline WOM has provided much evidence that consumers’ motivation to engage in WOM is impacted by social drivers such as the need for self enhancement, and that WOM behavior is used for social signaling (Sundaram et al. 1998). Hence, consumers might be more inclined to converse about highly regarded or highquality brands (Amblee and Bui 2008), about luxury goods that signal high social status, or about brands with a high degree of differentiation to express uniqueness (Lovett et al. 2013). In the context of social media mentions, this suggests that premium brands will be better represented in the data. (Indeed, our data show that, controlling for sales volume, premium brands have 2.1 times more social media mentions on average than do value brands.) We therefore expect that adding search trend data to social media data-based information when predicting sales volume will have a stronger impact on improving prediction accuracy for value brands than for premium brands (which are already better represented in social media data). This provides the background for our third research question, which explores the extent to which search trend data can mitigate the effect of these biases on predictive accuracy for different types of brands and products. Specifically, we explore whether the benefits of augmenting social media data with search trend data varies for premium and value brands.

## Consumer Involvement and Automotive Sales Prediction

Users’ online behavior patterns are known to be affected by consumer involvement and perceived risk. Involvement levels range from low to high, and the degree of involvement associated with a product is determined by how important consumers perceive the product to be (Blackwell et al. 2001). Dholakia (2001) defines product involvement as an internal state variable that indicates the amount of arousal, interest or drive evoked by a product class, and suggests that involvement is strongly linked to consumer risk perception. Involvement includes both enduring factors and situational factors (the level of interest evoked in a specific situation; Bloch and Richins 1983).

As indicated above, when a consumer feels more involved with a product, he or she is more likely to act with deliberation to minimize the risk and maximize the benefits gained from purchase and use. That is, the extent to which a product is “important” to a consumer influences the degree to which the consumer is motivated to be involved in the purchase decision (e.g., by seeking out information regarding the product).

Aspects of consumer search behavior that are influenced by product involvement include the volume of search conducted, the extent to which search is active or passive, and the quantity of information the consumer is able to process (Laurent and Kapferer 1985; Zaichkowsky 1985). Nevertheless, the effects of high involvement are not limited to search behavior; high involvement with a product has been shown to serve as a motivation for spreading WOM (Lovett et al. 2013) as well as for seeking out WOM and being influenced by it (Gu et al. 2012). Thus, in this work we focus on the context of high-involvement products, where we expect both publicly available social media mentions and search trend logs to be predictive of sales. Specifically, the data used in this study relates to the automotive industry, as it is a classic example of an industry with high involvement products.

Focusing on the automotive industry, our study also draws on and contributes to the specific field of automotive sales prediction and modeling, which has received extensive coverage in different contexts in previous literature. For example, Hymans et al. (1970) focused on the context of automotive expenditures to demonstrate the importance of including baseline information such as consumer sentiment index in modeling durable goods sales. Carlson (1978) used seemingly unrelated regressions to model the demand for different sizes of automobiles. Urban et al. (1990) developed a behavioral state model for pre-launch market prediction in which customers move between different behavioral states toward making an automotive purchase decision. This model was later extended by Urban et al. (1993), who added additional behavioral factors such as categorization and elimination of alternatives. Greenspan and Cohen (1999) developed a macroeconomic model for forecasting aggregate new car sales in the United States; their model considered the stock of vehicles and vehicle scrappage. Recently, Wang et al. (2011) applied a nonlinear method, using an adaptive network-based fuzzy inference system. Landwehr et al. (2011) adopted a somewhat different perspective on the automotive sales prediction problem, incorporating visual car design parameters such as design prototypicality and design complexity into the prediction model. Most relevant to our context are papers that use Google Trends data in the context of automotive sales prediction. For instance, Choi and Varian (2009, 2011) predicted automotive sales and automotive parts sales in the United States; Seebach et al. (2011) predicted automotive sales for two car manufacturers in Germany; and Du and Kamakura (2012) demonstrated their modeling method in conjunction with U.S. automotive sales. In this regard, our paper contributes to the automotive prediction literature as our paper not only uses search trend data, as reported by Choi and Varian (2009, 2011), Seebach et al. (2011), and Du Kamakura (2012), but also employs social media data to explore the complimentarily and interplay between the two sources.

## Data and Representation

This research uses monthly data for 23 car brands (all brands with average sales above 5,000 cars per month) sold in the United States over the 4-year period between 2007 and 2010. We use three different sources of data, described below: sales, search, and forums. Note that following common practice (for example, Choi and Varian 2009; Du and Kamakura 2012; Seebach et al. 2011), we focus on brandlevel sales rather than specific car model sales (e.g., the BMW car brand, rather than the 528i car model).<sup>9</sup> See Appendix B for the list of brands. Nevertheless, for robustness, we also report on predicting car-model-level sales (see Appendix G), reaching similar findings.

## Sales Data

We utilize data on U.S. unit sales of new cars and light trucks, obtained from the Automotive News website (www.autonews. com/). Automotive News provides sales data at a monthly level of aggregation. This is a well-known source for automotive sales information that has been used in various related studies such as Choi and Varian (2009) and Du and Kamakura (2012). In what follows, we use Sales to denote the sales volume of brand i during month t.

## Search Data

We use Google search engine query logs. These are the same raw data that Google uses to display search engine query trends on the Google Trends website (http://www.google. com/trends/). Specifically, we collect the reported volume of monthly Google search queries for each of the car brands. We limit our data to searches originating from the United States and to searches related to the automotive industry by selecting the relevant category options in Google Trends. In what follows, we use Search to denote the search volume of brand i during month t.<sup>10</sup>

## Forum Data

To represent forum data, we use Google’s vast scan of the Internet. To the best of our knowledge, this is the most comprehensive scan of forum data that has been made available for any academic research. Specifically, we extracted data from all English-language forums indexed by Google’s discussion forum search.<sup>11</sup> This index includes dedicated websites in addition to websites that include sections in which users can publicly post opinions and reviews, as well as relate to previous content. (Examples include townhall-talk.edmunds.com, forums.motortrend.com, answers.yahoo.com, etc.)

Following recent literature on this topic, we extracted two aspects of forum data for each car brand: the number of times the brand was mentioned in forums (forum mentions) and the overall sentiment (valence) of these forum mentions (forum sentiment). To represent brand i’s forum mentions in month t (denoted forum\_mentions ), we used the number of new forum posts mentioning brand i during month t. To represent forum sentiment for brand i in month t (denoted forum\_ sentiment ), we used the ratio between the sums of “positive mentions” and “negative mentions” for brand i in month t. To label forum postings as positive or negative, we used a dictionary-based sentiment analysis approach that is popular in the literature (see, for instance, Berger and Milkman 2012). Specifically, we utilized the extended positive and negative word dictionaries from the well-known Harvard IV-4 psychological dictionary<sup>12</sup> and summed the number of new forum posts mentioning “positive words” and posts mentioning “negative words” alongside brand i during month t. The advantages of using this dictionary approach are its generalizability and reproducibility (in contrast to the case of proprietary or “black box” types of sentiment analysis solutions).<sup>13</sup>

## Keywords

In order to collect search data and forum data, it was necessary to specify keywords that could be used to identify searches or forum mentions associated with each brand. This section elaborates on the design decisions we made regarding keyword selection.

Let K denote a set of keywords and B denote a given brand. We use the term accuracy to denote the ratio between the number of search queries (or forum posts) that specify (any word in) K and that actually relate to brand B, and the total number of search queries (or forum posts) specifying any word in K. We use the term coverage to denote the ratio between the number of searches (forum posts) using any word in K, and the hypothetical, full number of searches (forum posts) referring to brand B (using any keyword).

In general, when selecting a set of keywords to identify a given brand, there is a tradeoff between accuracy and coverage. Clearly, inclusion of a larger number of keywords can increase coverage, but it may introduce noise and decrease accuracy. On the other hand, if we choose a limited set of terms for a given car brand and obtain high accuracy, we may not fully capture the brand’s online presence. For example, if one wishes to capture search queries pertaining to the Chevrolet car brand, one will most likely use the term Chevrolet. Next, one can increase coverage by adding car model names such as Malibu (capturing additional searches for Chevrolet Malibu) or Spark (capturing additional searches for Chevrolet Spark). However, adding search terms such as Malibu or Spark may also introduce a large number of irrelevant queries (e.g., queries relating to the city of Malibu, California). Note that there is no point in adding the more specific, two-word term Chevrolet Malibu (or Chevrolet Spark), to the set of keywords, as a search using this term is a subset of the searches using the keyword Chevrolet.

To the best of our knowledge, the literature does not offer a methodology for optimal selection of keywords with the aim of achieving best predictive performance using both search and forum data, for different domains. Therefore, in this study we utilized brand-level keywords (e.g., Chevrolet for the Chevrolet brand), similarly to Seebach et al. (2011).<sup>14</sup> (See Appendix B for a detailed list of the keywords we used.)

While brand-level keywords can naturally provide high accuracy in capturing brand-related search queries (or forum mentions), we also adapted our modeling procedures to mitigate coverage concerns. First, as mentioned above, we expected that brand-level keywords (e.g., Chevrolet) would be considerably more commonplace than model-level keywords (e.g., Spark), for most car brands. Thus, the initial level of coverage was already expected to be relatively high.

Second, we note that when a prediction model is constructed for each car brand, as long as the keyword coverage is sufficiently representative of the brand, to the point that the ratio between the volume of searches (or forum mentions) captured by the brand-level keyword and the hypothetical, unknown, full volume of relevant searches (or forum mentions) remains stable over time; there is actually no need to fully capture the hypothetical, unknown, full coverage. Even simple models such as linear regression can overcome this problem by simply adjusting the coefficient values. As we are generally interested in predictive capability, rather than specific coefficient values, scaled coefficient values are not a concern.

Third, to control for different levels of baseline coverage across multiple brands, we converted the dependent and independent variables into per-brand, normalized variables and utilized the distance, in term of standard deviations, from the brand’s mean, rather than the original values.

For the reasons mentioned above, in what follows, in the main body of this paper we report on predictions at the brand level, using brand-level keywords. Nevertheless, in the appendices, we also report about car-model-level sales predictions (see Appendix G). Additionally, for robustness we examined a different keyword methodology involving a combination of brand-level and car-model-level keywords for predicting brand-level sales. This analysis is also reported in the Appendix H. In all robustness checks, we obtained similar findings.

## Modeling

## Setup

Our dependent variable is $S a l e s _ { i , t } ,$ automotive sales for brand i in month t. To make a prediction for each brand’s sales in month t, we use data that are available at month t – 1. Predictors include sales in previous months, forum data, and search trend data (as elaborated above), as well as benchmark data. Modeling was carried out on a monthly basis, beginning with one lag of historical data (month t – 1) and gradually incorporating additional lags (up to five lags of data, months: t – 1, $\ldots , t - 5 ) . ^ { 1 5 }$

Following previous research in this domain, we utilized the following benchmark data:

Seasonality: sales in the same month, in the previous year $( \mathrm { i . e . , } S a l e s _ { i , t - I 2 } ) .$ Usage of such data to represent seasonality is common in autoregressive models in this domain (see, for example, Choi and Varian 2009, 2011) due to the cyclic variation in customer automotive purchase patterns.

Consumer sentiment index (see, for example, Hu et al. 2014; Hymans et al. 1970): This is a U.S. national economic indicator based on a survey of a representative sample of the US population. It is designed to depict how consumers view their own financial situation and short/long-term economic conditions; thus, it has high relevance for consumer car purchase decisions. Consumer sentiment index is reported by the University of Michigan and Thompson Reuters.

Gasoline prices (see, for example, Hu et al. 2014): This national average price information is collected and reported by the U.S. Energy Information Administration and is based on the retail prices provided by a sample of approximately 800 gasoline stations. As gasoline prices influence the total cost of vehicle ownership, this economic indicator is expected to be associated with consumer car purchase decisions.

Having collected the data, we defined a benchmark model as a model that utilizes consumer sentiment, gasoline price, seasonality $( S a l e s _ { i , t - I 2 } ) ,$ , and previous sales data. Subsequently, in order to gauge the informativeness of forum-based data and search trend data, as well as the benefit of augmenting forumbased data with search trend data, we defined several additional models incorporating different sets of data, as follows: The forum-based model utilizes the benchmark model data in addition to forum mentions; the extended forum-based model adds forum sentiment data to the forum-based model; the search trends-based model utilizes both benchmark information and search trend data; and the combined search and forum-based model utilizes all the sets of information mentioned above. Table 1 summarizes the different sets of data utilized in each prediction model.

## Prediction and Evaluation

We utilized the popular least-squares linear regression (LR) algorithm. This method has been used in the vast majority of related studies seeking to predict economic outcomes on the basis of either forum data or search trend data. For robustness, we repeated our analysis with nonlinear methods such as neural networks (NN), support vector machines (SVM), and random forest, and obtained similar findings. We report the NN results in Appendix C.

Following common practice in predictive research, we measured the model’s performance “out-of-sample,” that is, we used one set of data to train the model and another set to measure its performance. Specifically, we used the moving window approach. Implementing this method, we followed common practice and used one-third of our data as an independent validation set. We report performance on the basis of the entire out-of-sample validation period (months t = 25, …, 36). That is, for each validation month t, we measure performance while applying the model trained during the 24 preceding months (months t – 24 to t – 1). We note that month t = 1 is January 2008 and month t = 25 is January 2010.<sup>16</sup> For robustness, we carried out a similar analysis using the expanding window approach, and obtained similar findings. These results are provided in Appendix D.

We used the mean absolute percentile error (MAPE) as our performance criterion. We made this choice for two main reasons: First, MAPE controls for volume differences across brands. For example, using MAPE, a 10% error in prediction for a large manufacturer is treated similarly to a 10% error in prediction for a small manufacturer. Second, MAPE is indifferent to the direction of the error (either overestimation or underestimation). This is appropriate for our approach, as we are interested in evaluating the predictive capacity of the

<table><tr><td colspan="6">Table 1. Data Included in Each Model</td></tr><tr><td></td><td>Benchmark Model</td><td>Forum-Based Model</td><td>Extended Forum-Based Model</td><td>Search Trends-Based Model</td><td>Combined Search and Forum-Based Model</td></tr><tr><td> $Sales_{i,t-1},...,Sales_{i,t-n}$ </td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Consumer  $Sentiment_{t-1}$ </td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td> $Gasoline price_{t-1}$ </td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td> $Sales_{i,t-12}$ </td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td> $Forum\_mentions_{i,t-1},...,Forum\_mentions_{i,t-n}$ </td><td></td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td> $Forum\_sentiment_{i,t-1},...,Forum\_sentiment_{i,t-n}$ </td><td></td><td></td><td>√</td><td></td><td>√</td></tr><tr><td> $Search_{i,t-1},...,Search_{i,t-n}$ </td><td></td><td></td><td></td><td>√</td><td>√</td></tr></table>

Figure 1 displays the results obtained using the different data representations (i.e., the different model types defined in Table 1). Table 2 presents the differences in MAPE values between models utilizing different sets of data and the corresponding significance values, using a bootstrap confidence interval (in this table, a positive difference between the MAPE values indicates that Model A’s predictive accuracy is better than Model B’s predictive accuracy). The results reported include models with one lag of data and with two

## Results

Finally, we note that we transformed each of the variable representations into normalized values (for each brand). There are two motivations for normalization at the brand level. First, normalization controls for differences in sales volume across different brands. Second, as discussed in the “Data and Representation” section, normalization is a key component in our keyword handling methodology. Nevertheless, we note that while our models use normalized variables in order to provide interpretable results, we calculated the MAPE according to the actual, “de-normalized” numbers. We further note that in deriving the results reported below, in order to avoid information leakage from the validation set data, we used normalization/de-normalization procedures in which the normalization factors (sample mean and standard deviation) were calculated solely on the basis of the specific training set data used in each moving window iteration.

data (i.e., the extent to which reliance on the data can reduce prediction error, regardless of a brand’s sales volume or the direction of the error). For robustness, we repeated the analysis using mean square error (MSE) criteria and reached similar findings. These results are provided in Appendix H.

lags of data. Notably, although we tested prediction models using up to five lags of data, we found that adding data from lag 3 or higher actually degraded predictive accuracy for all the models.

Recall that our first research question examines whether predictive models based on a combination of search trend data and forum data can obtain more accurate sales predictions compared with models based on each source of data alone. Our first core finding is that the combined model is superior to models based on forum data alone. Specifically, we find that augmenting forum data with search trend data significantly improves prediction accuracy: When using one lag of data, the combined model yields an improvement in MAPE of 0.55% compared with the forum-based model, and when using two lags of data, the combined model yields an improvement in MAPE of 0.58%. Similarly, when comparing the results of the combined model versus the more elaborate extended forum-based model (which uses forum sentiment scores in addition to forum mentions), we observe that with one lag of data the combined model yields an improvement in MAPE of 0.42%, and with two lags of data it yields an improvement in MAPE of 0.37%. These findings are significant and suggest that search trend data contain additional valuable information not available in forum data. We obtain similar significant findings when using a nonlinear NN algorithm (see Appendix C).

We also note that the combined model significantly improves predictive accuracy compared to a model based exclusively on search trend data (see Table 2). This result is consistent across one and two lags of data. With one lag of data, the combined model yields an improvement in MAPE of 0.34%, and with two lags of data, it yields an improvement in MAPE of 0.4%. However, when using a nonlinear NN algorithm (see Appendix C) the combined model outperforms search

![](/api/attachments/6EC8QF27/fulltext/images/32908c7e62181e28503ef7748ac62fc9471f1bb233c3d65a95cc0b052a6987be.jpg)  
Figure 1. Prediction Results (LR)

Table 2. MAPE Differences and One-Sided Confidence Intervals for the Difference in MAPE Values Using LR Method

<table><tr><td></td><td></td><td colspan="2">MAPE(Model B) – MAPE(Model A)</td></tr><tr><td>Model A</td><td>Model B</td><td>LR – Lag 1</td><td>LR – Lag 1,2</td></tr><tr><td>Forum-Based Model</td><td>Benchmark Model</td><td>0.11%**</td><td>0.13%**</td></tr><tr><td>Extended Forum-Based Model</td><td>Benchmark Model</td><td>0.25%**</td><td>0.34%**</td></tr><tr><td>Search Trends-Based Model</td><td>Benchmark Model</td><td>0.32%***</td><td>0.31%**</td></tr><tr><td>Combined Model</td><td>Benchmark Model</td><td>0.67%***</td><td>0.71%***</td></tr><tr><td>Search Trends-Based Model</td><td>Forum-Based Model</td><td>0.21%*</td><td>0.17%</td></tr><tr><td>Search Trends-Based Model</td><td>Extended Forum-Based Model</td><td>0.08%</td><td>-0.03%</td></tr><tr><td>Combined Model</td><td>Forum-Based Model</td><td>0.55%***</td><td>0.58%***</td></tr><tr><td>Combined Model</td><td>Extended Forum-Based Model</td><td>0.42%***</td><td>0.37%***</td></tr><tr><td>Combined Model</td><td>Search Trends-Based Model</td><td>0.34%**</td><td>0.40%**</td></tr></table>

Table 2 reports the difference in MAPE using two models (Model A and Model B - each based on different data inputs) while considering 1 or 2 lags with the LR algorithm.  
Specifically, the table reports the difference: diff = MAPE(Model B) - MAPE(Model A). Therefore, a positive value associated with the comparison between Model A and Model B indicates better predictive accuracy of Model A over Model B.  
Lower confidence interval bounds for diff were calculated using 2000 iterations of the BCA bootstrapping confidence interval calculation method implemented in R software. A lower confidence interval bound for diff, with a positive value, provides confidence that MAPE(Model A) is indeed better than MAPE(Model B).  
We report the following lower confidence bounds:

0.9 lower confidence bound for diff is positive

\*\* 0.95 lower confidence bound for diff is positive

\*\*\* 0.99 lower confidence bound for diff is positive

trend data only with two lags of data, and this improvement is not significant.

Our second core finding relates to the second research question, which examines whether predictive models using search trend data obtain similar or better accuracy compared to predictive models utilizing forum-based data (either forum mention volume or forum mention volume combined with forum sentiment). We find that the performance of search trend-based models is, at least, comparable to that of forumdata-based models. Specifically, with one lag of data, the search trend-based model obtained an improvement in MAPE of 0.21% compared with the forum-based model, and with two lags of data it yielded a smaller improvement in MAPE of 0.17%. Compared with the more elaborate extended forum-based model (i.e., the model that incorporates both forum mentions and sentiment scores), the search trend-based model obtained a small improvement in MAPE of 0.08% with one lag of data, and with two lags of data it yielded a minor deterioration in MAPE of -0.03%. The observation that the predictive performance of models based on search trend data is, at least, comparable to that of models based on forum data is also consistent with our robustness check using the nonlinear NN algorithm. In fact, when using NN, we find that models based on search data not only obtain comparable results to models based on forum and extended forum data, but also significantly outperform them (see Appendix C).

## Prediction Results According to Brand Characteristics

Our third research question explores further aspects of adding search trend data to forum data. Specifically, we focus on premium (luxury) car brands (i.e., brands with higher pricing or higher perceived quality or brands that elicit higher willingness to recommend) versus value car brands. As discussed, we expect to find that adding search trend data to forum-based data will have a stronger impact on improving sales prediction accuracy for value brands rather than for premium brands (which are already better represented in forum data).

In what follows, the car brands are split into two subsets to represent the value and premium segments. Specifically, we split the car brands based on price, perceived quality, or willingness to recommend, as follows: Car brands for which the list price for the least expensive car model of each brand was more than \$20,000 were referred to as “high price,” and the rest of the car brands were referred to as “low price.”<sup>17</sup> Next, we obtained survey data about perceived quality and willingness to recommend each brand. These data were obtained from YouGov plc, a market research firm that monitors a panel of 5,000 people in the United States, on a daily basis, and reports on brand-related perceptions. See Appendix F for more details about these survey data. For this analysis, we refer to the 12 brands with lower perceived quality as brands with “low perceived quality” and the remaining 11 brands as brands with “high perceived quality.” Similarly, we refer to the 12 brands associated with lower willingness to recommend as brands with “low willingness to recommend” and the remaining 11 brands as brands with “high willingness to recommend.”<sup>18</sup>

Figure 2 shows a comparison between the performance of the combined model and that of the extended-forum-based model in predicting the sales of high price (premium) versus low price (value) brands, with one lag of data.

The results show that for both premium and value brands, adding search trend data to the extended forum data yielded better (lower) MAPE values compared with the extended forum-based model. Interestingly, for value brands, the combined model significantly outperformed the extended forum-based model, yielding an improvement in MAPE of 0.41%. In contrast, for premium brands, the difference was smaller (the combined model yielded an improvement in MAPE of only 0.2% as compared with the extended forumbased model) and was not significant. These results support the conjecture that, when attempting to predict car sales, adding search trend data to forum-based data will have a stronger impact on improving prediction accuracy for value brands rather than for premium brands.

For robustness, we repeated the analysis splitting the brands according to perceived quality or willingness to recommend metrics (see Appendix E), using a model with two lags of data (see Appendix E), and with car model level data (see Appendix G). In all analyses, we obtained similar findings, namely, that adding search trend data to forum data improves predictive accuracy to a greater extent in the case of value brands than in the case of premium brands.

## Conclusions

In this paper we empirically studied the interplay between search trend data and publicly available social media mentions from social media websites in the context of sales prediction. While social media data have been used extensively for sales predictions, previous literature has pointed to various limitations and biases associated with this source of data. One possible method of improving the predictive accuracy of this data source is to overlay it with search trend data. However, thus far, the two data sources have largely been investigated in disparate literature streams and for separate purposes.

Prior literature suggests that, when attempting to obtain evidence related to customers’ decision making processes, it is necessary to distinguish between different types of products. Specifically, consumers are more likely to engage in extensive and active information search in the case of high-involvement products than in the case of low-involvement products. Therefore, in this paper, we focused on high-involvement products.

![](/api/attachments/6EC8QF27/fulltext/images/81fffc79178d9dc919e58935fbc20e4a4cdb9f74c9fdbc3b1e45313c93df2d55.jpg)  
Figure 2. Prediction Results for Premium Versus Value Brands (Split by Price)

Using data from the automotive industry, we have provided first evidence that augmenting forum-based models with search trend data significantly improves predictive accuracy. This evidence indicates that the sales-relevant information embedded in search data is external and nonoverlapping to the corresponding information embedded in forum data. From a practical perspective, this finding suggests that companies that have already invested in collecting forum-based data for modeling purposes can significantly improve forecasting accuracy with a relatively small additional investment in collecting search trend data. Our findings further suggest that the prediction accuracy that can be achieved using search trend data alone is comparable to that associated with the more commonly used forum-based data. This finding could encourage managers to evaluate using search trend data as a low-cost replacement for social media data. Finally, we find that adding search trend data to forum-based data has a stronger impact on improving prediction accuracy for value brands rather than for premium brands.

Our work carries managerial implications for car manufacturers and, more broadly, for manufacturers of highinvolvement products. Moreover, the advantage of our method is that it does not require proprietary data available only to the manufacturer. Hence, it can be used by upstream and downstream players, as well as by stock market investors. Furthermore, car manufacturers can use this approach to evaluate the expected sales of their competitors. More accurate sales prediction models can, in turn, drive better decision making in various domains such as marketing expenditure, competitive analysis, inventory management, and supply chain optimization. For the specific case of automotive sales, these decisions involve the allocation of extremely large funds and, therefore, even small improvements in forecasting accuracy are expected to have a considerable effect.

We expect that our findings may be generalizable to a wide array of purchase decisions regarding high-involvement products, such as housing purchases and travel planning. In the case of low-involvement products, such as music, mobile applications, and movie tickets, consumers do not conduct extensive and active search, and decisions are made more lightheartedly. The predictive power of search trends in this context is therefore unclear. This raises an interesting direction for future research.

Other possible avenues of future work include incorporating information about the popularity of different discussion forum websites in the prediction models. Additionally, it is possible to analyze the predictive value of search trend and forum data according to additional brand characteristics and model characteristics, such as vintage. It would also be interesting to study how the incorporation of predictions based on the investigated data sources into the managerial decision making process interacts with these data and affects their predictive capacity over time. Additionally, from a methodological perspective, it would be interesting to compare predictions based on publicly available information to industry experts forecasts using proprietary data. Finally, this study demonstrated that search trend data can successfully complement forum data in the context of sales prediction. Nevertheless, forum data have been used for other purposes such as detecting changes in consumer interest in products. Therefore, it would be interesting to evaluate the effectiveness of using search trend data for augmenting forum-based data in this context.

## Acknowledgments

We would like to thank the senior editor, the associate editor, and two reviewers for their constructive and insightful comments and suggestions. Tomer Geva and Gal Oestreicher-Singer acknowledge financial support from Marketing Science Institute and the Henry Crown Institute for Business Research. Tomer Geva acknowledges financial support from Israel Science Foundation (ISF grant 1443/14) and a post-doctoral research scientist fellowship at Google.

## References

Amblee, N., and Bui, T. 2008. “Can Brand Reputation Improve the Odds of Being Reviewed On-Line?,” International Journal of Electronic Commerce (12:3), pp. 11-28.

Anderson, E. T., and Simester, D. I. 2014. “Reviews Without a Purchase: Low Ratings, Loyal Customers, and Deception,” Journal of Marketing Research (51:3), pp. 249-269.

Berger, J., and Milkman, K. L. 2012. “What Makes Online Content Viral?,” Journal of Marketing Research (49:2), pp. 192-205.

Berger, J., and Schwartz, E. M. 2013. “What Drives Immediate and Ongoing Word of Mouth?,” Journal of Marketing Research (48:5), pp. 869-880.

Blackwell, D., Miniard P. W., and Engel, J. F. 2001. Consumer Behavior (9<sup>th</sup> ed.), Orlando, FL: Harcourt.

Bloch, P. H., and Richins, M. L. 1983. “A Theoretical Model for the Study of Product Importance Perceptions,” Journal of Consumer Research (47), pp. 69-81.

Carlson, R. L. 1978. “Seemingly Unrelated Regression and the Demand for Automobiles of Different Sizes, 1965-75: A Disaggregate Approach,” Journal of Business (51:2), pp. 243-262.

Chakravarty, A., Yong, L., and Mazumdar, T. 2010. “The Differential Effects of Online Word-of-Mouth and Critics’ Reviews on Pre-Release Movie Evaluation,” Journal of Interactive Marketing (24: 3), pp. 185-197.

Chen, Y., and Xie, J. 2008. “Online Consumer Reviews: A New Element of Marketing Communications Mix,” Management Science (54:3), pp. 477-491.

Chevalier, J., and Mayzlin, D. 2006. “The Effect of Word of Mouth on Sales: Online Book Reviews,” Journal of Marketing Research (43:3), pp. 345-354.

Chintagunta, P. K., Gopinath, S., and Venkataraman, S. 2011. “The Effect of Online User Reviews on Movie Box Office Performance: Accounting for Sequential Rollout and Aggregation across Local Markets,” Marketing Science (29:5), pp. 944-957.

Choi, H., and Varian, H. 2009. “Predicting the Present with Google Trends,” working paper.

Dellarocas, C. 2006. “Strategic Manipulation of Internet Opinion Forums: Implications for Consumers and Firms,” Management Science (52:10), pp. 1577-1593.

Dellarocas, C., Awad, N., and Zhang, X. 2007. “Exploring the Value of Online Product Reviews in Forecasting Sales: The Case of Motion Pictures,” Journal of Interactive Marketing (21:4), pp. 23-45.

Dellarocas, C., and Narayan, R. 2006. “A Statistical Measure of a Population’s Propensity to Engage in Post-Purchase Online Word-of-Mouth,” Statistical Science (21:2), pp. 277-285.

Dewan, S., and Ramaprasad, J. 2009. “Chicken and Egg? Interplay between Music Blog Buzz and Album Sales,” in PACIS 2009 Proceedings, Paper 87 (http://aisel.aisnet.org/pacis2009/97).

Dewan, S., and Ramaprasad, J. 2012. “Music Blogging, Online Sampling, and the Long Tail,” Information Systems Research (23:3), pp. 1056-1067.

Dhar, V., and Chang, E. A. 2009. “Does Chatter Matter? The Impact of User-Generated Content on Music Sales,” Journal of Interactive Marketing (23:4), pp. 300-307.

Dholakia, U. M. 2001. “A Motivational Process Model of Product Involvement and Consumer Risk Perception,” European Journal of Marketing (35:11), pp. 1340-1360.

Du, R. Y., and Kamakura, W. A. 2012. “Quantitative Trendspotting,” Journal of Marketing Research (49:4), pp. 514-536.

Duan, W., Gu, B., and Whinston, A. B. 2008a. “The Dynamics of Online Word-of-Mouth and Product Sales—An Empirical Investigation of the Movie Industry,” Journal of Retailing (84:2), pp. 233-242.

Duan, W., Gu, B., and Whinston, A. B. 2008b. “Do Online Reviews Matter? An Empirical Investigation of Panel Data,” Decision Support Systems (45:4), pp. 1007-1016.

Forman, C., Ghose, A., and Wiesenfeld, B. 2008. “Examining the Relationship Between Reviews and Sales: The Role of Reviewer Identity Disclosure in Electronic Markets,” Information Systems Research (19:3), pp. 291-313.

Ginsberg, J., Mohebbi, M. H., Patel, R. S., Brammer, L., Smolinski, M. S., and Brilliant, L. 2008. “Detecting Influenza Epidemics Using Search Engine Query Data,” Nature (457:7232), pp. 1012-1014.

Godes, D., and Mayzlin, D. 2004. “Using Online Conversations to Study Word-of-Mouth Communication,” Marketing Science (23:4), pp. 545-560.

Godes, D., and Silva, J. C. 2012. “Sequential and Temporal Dynamics of Online Opinion,” Marketing Science (31:3), pp. 448-473.

Goel, S., Hofman, J. M., Lahaie, S., Pennock, D. M., and Watts, D. J. 2010. “Predicting Consumer Behavior with Web Search,” Proceedings of the National Academy of Sciences (107:41), pp. 17486-17490.

Greenspan, A., and Cohen, D. 1999. “Motor Vehicle Stocks, Scrappage, and Sales,” The Review of Economics and Statistics (81:3), pp. 369-383.

Gu, B., Park, J., and Konana, P. C. 2012. “The Impact of External Word-of-Mouth Sources on Retailer Sales for High Involvement Products,” Information Systems Research (23:1), pp. 182-196.

Hill, S., Nalavade, A., and Benton, A. 2012. “Social TV: Real-Time Social Media Response to TV Advertising,” in Proceedings of the Sixth International Workshop on Data Mining for Online Advertising and Internet Economy, Article 4.

Hong, Y., Chen, P.-Y., and Hitt, L. M. 2014. “Measuring Product Type with Dynamics of Online Product Review Variances: A Theoretical Model and the Empirical Applications,” working paper.

Hu, N., Liu, L., and Zhang, J. 2008. “Do Online Reviews Affect Product Sales? The Role of Reviewer Characteristics and Temporal Effects,” Information Technology Management (9:3), pp. 201-214.

Hu, Y, Du, R. Y., and Damangir, S. 2014. “Decomposing the Impact of Advertising: Augmenting Sales with Online Search Data,” Journal of Marketing Research (51: 3), pp. 300-319.

Hymans, S. H., Ackley, G., and Juster, F. T. 1970. “Consumer Durable Spending: Explanation and Prediction,” Brookings Papers on Economic Activity, pp. 173-206.

Kronrod, A., and Danziger, S. 2013. “‘Wii Will Rock You!’ The Use and Effect of Figurative Language in Consumer Reviews of Hedonic and Utilitarian Consumption,” Journal of Consumer Research (40), pp. 726-739.

Landwehr, J. R., Labroo, A. A., and Herrmann, A. 2011. “Gut Liking for the Ordinary: Incorporating Design Fluency Improves Automobile Sales Forecasts,” Marketing Science (30:3), pp. 416-429.

Laurent, G., and Kapferer, J. 1985. “Measuring Consumer Involvement Profiles,” Journal of Marketing Research (22:1), pp. 41-53.

Lazer , D., Kennedy, R., King, G., and Vespignani, A. 2014. “The Parable of Google Flu: Traps in Big Data Analysis,” Science (343:6176), pp. 1203-1205.

Li, X., and Hitt, L. M. 2008. “Self Selection and Information Role of Online Product Reviews,” Information Systems Research (19:4), pp 456-474.

Liu, Y. 2006. “Word of Mouth for Movies: Its Dynamics and Impact on Box Of ce Revenue,” Journal of Marketing (70:3), pp. 74-89.

Lovett, M., Peres, R., and Shachar, R. 2013. “On Brands and Word of Mouth,” Journal of Marketing Research (50:4), pp. 427-444.

Luca, M., and Zervas, G. 2015. “Fake it Till You Make it: Reputation, Competition, and Yelp Review Fraud,” Harvard Business School NOM Unit Working Paper No. 14-006 (SSRN:http://ssrn.com/abstract=2293164).

Luo, X., Zhang, J., and Duan, W. 2013. “Social Media and Firm Equity Value,” Information Systems Research (24:1), pp. 146-163.

Mayzlin, D., Dover, Y., and Chevalier, J. 2014. “Promotional Reviews: An Empirical Investigation of Online Review Manipulation,” American Economic Review (104:8), pp. 2421-55.

Moe, W. W., and Schweidel, D. A. 2012. “Online Product Opinions: Incidence, Evaluation and Evolution,” Marketing Science (31:3), pp. 372-386.

Moe, W. W., and Trusov, M. 2011. “The Value of Social Dynamics in Online Product Ratings Forums,” Journal of Marketing Research (48:3), pp. 444-456.

Moorthy, S., Ratchford, B. T., and Talukdar, D. 1997. “Consumer Information Search Revisited: Theory and Empirical Analysis,” Journal of Consumer Research (23:4), pp. 263-277.

Netzer, O., Feldman, R., Goldenberg, J., and Fresko, M. 2012. “Mine Your Own Business: Market-Structure Surveillance Through Text Mining,” Marketing Science (31:3), pp. 521-543.

Pöyry, E., Parvinen, P., and Malmivaara, T. 2013. “Can We Get from Liking to Buying? Behavioral Differences in Hedonic and Utilitarian Facebook Usage,” Electronic Commerce Research and Applications (12:4), pp. 224-235.

Preis, T., Moat, H. S., and Stanley, H. E. 2013. “Quantifying Trading Behavior in Financial Markets Using Google Trends, Scientific Reports, 3, Article Number 1684.

Rui, H., Liu, T., and Whinston, A. 2012. “Whose and What Chatter Matters? The Impact of Tweets on Movie Sales,” working paper.

Schlosser A. E. 2005. “Posting Versus Lurking: Communicating in a Multiple Audience Context,” Journal of Consumer Research (32), pp. 260-265.

Schulze, C., Schöler L., and Skiera, B. 2014. “Not All Fun and Games: Viral Marketing for Utilitarian Products,” Journal of Marketing (78:1), pp. 1-19.

Schweidel, D. A., and Moe, W. W. 2014. “Listening in on Social Media: A Joint Model of Sentiment and Venue Format Choice,” Journal of Marketing Research (51:4), pp. 387-402.

Seebach, C., Pahlke, I., and Beck, R. 2011. “Tracking the Digital Footprints of Customers: How Firms Can Improve Their Sensing Abilities to Achieve Business Agility,” in ECIS 2011 Proceedings, Paper 258 (http://aisel.aisnet.org/ecis2011/258).

Shmueli, G. 2010. “To Explain or to Predict?,” Statistical Science (25:3), pp. 289-310.

Shmueli, G., and Koppius, O. 2011. “Predictive Analytics in Information Systems Research,” MIS Quarterly (35:3), pp. 553-572.

Sundaram, D. S., Mitra, K., and Webster, C. 1998. “Word-of-Mouth Communications: A Motivational Analysis,” Advances in Consumer Research (25), pp. 527-531.

Sridhar, S., and Srinivasan, R. 2013. “Social Influence Effects in Online Product Ratings,” Journal of Marketing (76:5), pp. 70-88.

Urban, G. L., Hauser, J. R., and Roberts, J. H. 1990. “Prelaunch Forecasting of New Automobiles,” Management Science (36:4), pp. 401-21.

Urban, G. L., Hulland, J. S., and Weinberg, B. D. 1993. “Premarket Forecasting for New Consumer Durable Goods: Modeling Categorization, Elimination, and Consideration Phenomena,” Journal of Marketing (57:2), pp. 47-63.

Viswanathan, S., Gosain, S., Kuruzovich, J., and Agarwal, R. 2007. “Online Infomediaries and Price Discrimination: Evidence From the Auto-Retailing Sector,” Journal of Marketing (71:3), pp. 89-107.

Vosen, S., and Schmidt, T. 2011. “Forecasting Private Consumption: Survey-Based Indicators vs. Google Trends,” Journal of Forecasting (30:6), pp. 565-578.

Wang, F.-K., Chang, K.-K., and Tzeng, C.-W. 2011. “Using Adaptive Network-Based Fuzzy Inference System to Forecast Automobile Sales,” Expert Systems with Applications (38:8), pp. 10587-10593.

Wu, L., and Brynjolfsson, E. 2009. “The Future of Prediction: How Google Searches Foreshadow Housing Prices and Quantities,” in Proceedings of the 30<sup>th</sup> International Conference on Information Systems, Phoenix, AZ pp. 1-14.

Zaichkowsky, J. L. 1985. “Measuring the Involvement Construct,” Journal of Consumer Research (12:3), pp. 341-352.

Zhu, F., and Zhang, X. M. 2010. “Impact of Online Consumer Reviews on Sales: The Moderating Role of Product and Consumer Characteristics,” Journal of Marketing (74:2), pp. 113-148.

## About the Authors

Tomer Geva is an assistant professor at Tel Aviv University, Coller School of Management, where he heads the Business Analytics Program. Previously he was a visiting scholar at New York University’s Stern School of Business and a post-doctoral research scientist at Google. His research interests include using large-scale data for business decision making, and the effective use of crowdbased information for predictive modeling. His research has been published in MIS Quarterly, Information Systems Research, and Decision Support Systems. Prior to his Ph.D. studies, he held various engineering and management positions in the high-tech industry. Tomer holds a Ph.D. and an MBA (cum laude) from Tel-Aviv University and a B.Sc. (cum laude) in Industrial Engineering from the Technion— Israel Institute of Technology.

Gal Oestreicher-Singer is an associate professor at Tel Aviv University’s Coller School of Management and the chair of the Technology and Information Management department. Her research focues on the effects of social media, consumer engagement and peer influence on electronic commerce outcomes, and on the business model of content websites. Her work has been published in the top journals in the fields of both Information Systems and Marketing. She is the recipient of several prestigious awards, most recelty the AIS Sandy Slaughter Early Career Award. She serves on the editorial boards of MIS Quarterly, Information Systems Research, and Management Science. She received her Ph.D. from New York University in 2008, and holds degrees in law and electrical engineering from the Hebrew University in Jerusalem and Tel Aviv University.

Niv Efron is an engineering director at Google, where he works on Search and Big Data analysis technologies. Niv holds a B.Sc. and M.Sc. in Computer Science from Tel-Aviv University, with research focusing on the areas of machine learning and high dimensional statistics.

Yair Shimshoni is a senior quantitative analyst and a researcher in the Google R&D center in Tel-Aviv, where he specializes in search trends analysis, business intelligence, and data mining since 2008. His research studies the predictability and characteristics of search trends. Prior to joining Google, Yair was a researcher, consultant and lecturer in data mining and machine learning, both in the academia and in the industry for over 15 years. He holds an MBA, M.Sc. in CS, and B.Sc. in Statistics, from Tel-Aviv University.

# USING FORUM AND SEARCH DATA FOR SALES PREDICTION OF HIGH-INVOLVEMENT PROJECTS

Tomer Geva and Gal Oestreicher-Singer

The Coller School of Management, Tel Aviv University, P.O. Box 39040,

Tel Aviv 6997801, ISRAEL

{tgeva@tau.ac.il} {galos@tau.ac.il}

Niv Efron and Yair Shimshoni

Google, Tel Aviv, ISRAEL

{niv@google.com} {shimsh@google.com}

## Appendix A

## List of Main Robustness Checks

<table><tr><td>Robustness Check</td><td>Appendix</td></tr><tr><td>Predictive capacity using NN algorithm</td><td>C</td></tr><tr><td>Predictive capacity using Expanding Window approach</td><td>D</td></tr><tr><td>Predictive capacity according to “premium” and “value” car brand characteristics based on price, perceived quality, and willingness to recommend metrics. Using one or two lags of data.</td><td>E</td></tr><tr><td>Car model-level Analysis</td><td>G</td></tr><tr><td>Predictive capacity using extended keyword selection</td><td>H</td></tr><tr><td>Predictive capacity using MSE criteria</td><td>H</td></tr></table>

## Appendix B

List of Brands and Grouping by Price, Perceived Quality, and Willingness to Recommend

Table B1 provides details about the brands included in this study. The list of brands includes all car brands with average U.S. sales exceeding 5,000 cars per month during the period 2007–2010 (source: Automotive News).<sup>1</sup> Quality and willingness to recommend rankings are based on the YouGov BrandIndex product. (See additional details in Appendix F.)

<table><tr><td colspan="5">Table B1. List of Brands and Grouping by Price, Perceived Quality, and Willingness to Recommend</td></tr><tr><td>Brand</td><td>Keyword(s)</td><td>Price</td><td>Average Quality Ranking</td><td>Average Recommend Ranking</td></tr><tr><td>Acura</td><td>acura</td><td>high price</td><td>high</td><td>high</td></tr><tr><td>Audi</td><td>audi</td><td>high price</td><td>high</td><td>low</td></tr><tr><td>BMW</td><td>bmw</td><td>high price</td><td>high</td><td>high</td></tr><tr><td>Buick</td><td>buick</td><td>high price</td><td>low</td><td>low</td></tr><tr><td>Cadillac</td><td>cadillac</td><td>high price</td><td>high</td><td>low</td></tr><tr><td>Chevrolet</td><td>chevrolet, chevy</td><td>low price</td><td>low</td><td>high</td></tr><tr><td>Chrysler</td><td>chrysler</td><td>low price</td><td>low</td><td>low</td></tr><tr><td>Dodge</td><td>dodge</td><td>low price</td><td>low</td><td>low</td></tr><tr><td>Ford</td><td>for</td><td>low price</td><td>low</td><td>high</td></tr><tr><td>GMC</td><td>gmc</td><td>low price</td><td>low</td><td>low</td></tr><tr><td>Honda</td><td>honda</td><td>low price</td><td>high</td><td>high</td></tr><tr><td>Hyundai</td><td>hyundai</td><td>low price</td><td>low</td><td>low</td></tr><tr><td>Infiniti</td><td>infiniti</td><td>high price</td><td>high</td><td>low</td></tr><tr><td>Jeep</td><td>jeep</td><td>low price</td><td>low</td><td>low</td></tr><tr><td>Kia</td><td>kia</td><td>low price</td><td>low</td><td>low</td></tr><tr><td>Lexus</td><td>lexus</td><td>high price</td><td>high</td><td>high</td></tr><tr><td>Lincoln</td><td>lincoln</td><td>high price</td><td>low</td><td>low</td></tr><tr><td>Mazda</td><td>mazda</td><td>low price</td><td>low</td><td>low</td></tr><tr><td>Mercedes Benz</td><td>mercedes</td><td>high price</td><td>high</td><td>high</td></tr><tr><td>Nissan</td><td>nissan</td><td>low price</td><td>high</td><td>high</td></tr><tr><td>Subaru</td><td>subaru</td><td>low price</td><td>low</td><td>high</td></tr><tr><td>Toyota</td><td>toyota</td><td>low price</td><td>high</td><td>high</td></tr><tr><td>Volkswagen</td><td>volkswagen</td><td>low price</td><td>high</td><td>high</td></tr></table>

## Appendix C

## Analysis Using the NN Algorithm

In addition to evaluating the performance of models based on the linear regression algorithm (LR), for robustness we repeat the analysis using the back-propagation neural network (NN) algorithm. This is a nonlinear method that is estimated by the backprop algorithm (Werbos 1974). One of the strongest properties of the NN algorithm is that it inherently accounts for nonlinear relationships and complex interactions between variables (Bishop 1995). (See Appendix I for more details about the NN algorithm.) Such a method may have the capacity to capture (potentially complex, or unexpected) interactions and relations that underlie the real-life data generating process, without the need for the researcher to formally specify (or even be aware of) all existing relations. Thus, the NN approach can potentially “extract” more predictive power out of the data compared with linear methods, as it is not constrained by linearity and prespecified interactions. To implement the NN algorithm we used the “nnet” package in R software. This implementation involves one layer of hidden nodes, and the minimization of a sum of-square-errors criterion. In specifying the network architecture, one must choose the number of nodes in the hidden layer. While the literature does not offer clear rules about the optimal complexity of the network in terms of hidden nodes, it proposes general guidelines (Zhang et al. 1998); for instance, the number of hidden nodes should be proportional to the number of inputs. Following this guideline, we employed an NN model architecture in which the number of hidden nodes was equal to the number of inputs multiplied by 0.5.<sup>2</sup> Finally, while NNs are well-known for their ability to “learn” complex relations, in practice NN results may sometimes produce unstable predictions, overfit the data, or converge to a local optimum. As a safeguard against these problems, our specific implementation utilized the median prediction of an ensemble of 100 NNs, each using a different random seed.

Figure C1 displays the results obtained with NN using the different data representations (i.e., the different model types defined in Table 1, in the main body of the paper). Table C1 presents the differences in MAPE values between models utilizing different sets of data and the corresponding significance values, using a bootstrap confidence interval. In sum, we reach findings that are similar to those reported in the main body of the paper regarding the relative performance of the different prediction models using search trend data and forum data (as defined in Table 1).  
![](/api/attachments/6EC8QF27/fulltext/images/68ae5d70df8146017734828f7b97163939ed5630a8b8dd225f88a85d7a0caa5e.jpg)  
Figure C1. Prediction Results Using the NN Algorithm

Table C1. MAPE Differences and One-Sided Confidence Intervals for the Difference in MAPE Values Using the NN algorithm for Each Model

<table><tr><td>Model A</td><td>Model B</td><td>NN – Lag 1</td><td>NN – Lag 1,2</td></tr><tr><td>Forum-Based Model</td><td>Benchmark Model</td><td>-0.07%</td><td>0.34%**</td></tr><tr><td>Extended Forum-Based Model</td><td>Benchmark Model</td><td>-0.01%</td><td>0.26%</td></tr><tr><td>Search Trends-Based Model</td><td>Benchmark Model</td><td>0.65%***</td><td>0.55%***</td></tr><tr><td>Combined Model</td><td>Benchmark Model</td><td>0.44%**</td><td>0.73%***</td></tr><tr><td>Search Trends-Based Model</td><td>Forum-Based Model</td><td>0.72%***</td><td>0.21%*</td></tr><tr><td>Search Trends-Based Model</td><td>Extended Forum-Based Model</td><td>0.65%***</td><td>0.28%*</td></tr><tr><td>Combined Model</td><td>Forum-Based Model</td><td>0.51%**</td><td>0.39%***</td></tr><tr><td>Combined Model</td><td>Extended Forum-Based Model</td><td>0.44%**</td><td>0.47%***</td></tr><tr><td>Combined Model</td><td>Search Trends-Based Model</td><td>-0.21%</td><td>0.18%</td></tr></table>

Table C1 reports the difference in MAPE using two models (Model A and Model B - each based on different data inputs) while considering 1 or 2 lags with the NN algorithm. Specifically, the table reports the difference: diff = MAPE(Model B) - MAPE(Model A). Therefore, a positive value associated with the comparison between Model A and Model B indicates better predictive accuracy of Model A over Model B. Lower confidence interval bounds for diff were calculated using 2000 iterations of the BCA bootstrapping confidence interval calculation method implemented in R software. A lower confidence interval bound for diff, with a positive value, provides confidence that MAPE(Model A) is indeed better than MAPE(Model B).

We report the following lower confidence bounds:

★ 0.9 lower confidence bound for diff is positive

\*\* 0.95 lower confidence bound for diff is positive

\*\*\* 0.99 lower confidence bound for diff is positive

## Appendix D

## Analysis Using Expanding Window Approach

In addition to using the moving window validation methodology, for robustness we also evaluated an expanding window approach using 24 months of expanding training data. Implementing this method, we followed common practice and used (at least) two-thirds of our data as training set and one-third of our data as validation. We therefore report performance based on the entire out-of-sample validation period (months t = 25, …, 36). That is, for each validation month t we measure performance while applying the model trained during the preceding months (months 1 to t – 1). We note that month t = 1 is January 2008 and month t = 25 is January 2010.<sup>3</sup>

Figure D1 displays the results obtained with LR using the different data representations. Table D1 presents the differences in MAPE values (performance differences) between models utilizing different sets of data and the corresponding significance values using a bootstrap confidence interval. Overall, the findings obtained using the “expanding window” approach are similar to those obtained using the “moving window” approach.

![](/api/attachments/6EC8QF27/fulltext/images/5856eaf9c51ea77deccd67ef16e4498eca157b229d703303015debbf2ff5889a.jpg)

Table D1. MAPE Differences and One-Sided Confidence Intervals for the Difference in MAPE Values Using the LR algorithm for Each Model (Using Expanding Window Validation)

<table><tr><td>Model A</td><td>Model B</td><td>LR – Lag 1</td><td>LR – Lag 1,2</td></tr><tr><td>Forum-Based Model</td><td>Benchmark Model</td><td>-0.06%</td><td>-0.07%</td></tr><tr><td>Extended Forum-Based Model</td><td>Benchmark Model</td><td>0.32%*</td><td>0.48%**</td></tr><tr><td>Search Trends-Based Model</td><td>Benchmark Model</td><td>0.62%***</td><td>0.57%***</td></tr><tr><td>Combined Model</td><td>Benchmark Model</td><td>0.96%***</td><td>0.99%***</td></tr><tr><td>Search Trends-Based Model</td><td>Forum-Based Model</td><td>0.68%***</td><td>0.64%***</td></tr><tr><td>Search Trends-Based Model</td><td>Extended Forum-Based Model</td><td>0.30%</td><td>0.09%</td></tr><tr><td>Combined Model</td><td>Forum-Based Model</td><td>1.02%***</td><td>1.06%***</td></tr><tr><td>Combined Model</td><td>Extended Forum-Based Model</td><td>0.65%***</td><td>0.51%***</td></tr><tr><td>Combined Model</td><td>Search Trends-Based Model</td><td>0.34%*</td><td>0.42%*</td></tr></table>

Table D1 reports the difference in MAPE using two models (Model A and Model B - each based on different data inputs) while considering 1 or 2 lags with the LR algorithm. Specifically, the table reports the difference: diff = MAPE(Model B) - MAPE(Model A). Therefore, a positive value associated with the comparison between Model A and Model B indicates better predictive accuracy of Model A over Model B. Lower confidence interval bounds for diff were calculated using 2000 iterations of the BCA bootstrapping confidence interval calculation method implemented in R software. A lower confidence interval bound for diff, with a positive value, provides confidence that MAPE(Model A) is indeed better than MAPE(Model B). We report the following lower confidence bounds:

0.9 lower confidence bound for diff is positive

\*\* 0.95 lower confidence bound for diff is positive

\*\*\* 0.99 lower confidence bound for diff is positive

## Appendix E

## Analysis According to Car Brand Characteristics

In this appendix, we provide additional results and robustness checks regarding the predictive accuracy of the extended forum-based model and the combined model. Specifically, Figures E1 and E2 provide an additional graphic illustration of different models’ predictive accuracy in the cases of premium and value brands, where a brand’s affiliation with either category is based on its perceived quality (Figure E1) and on the extent to which it is associated with willingness to recommend (Figure E2). This analysis was carried out using one lag of data. For robustness we repeated the comparisons between value and premium brands (Figures E3–E5) using two lags of data. In sum, we observe similar findings to those reported in the main body of the paper. Specifically, for value brands, the combined model significantly outperforms the extended forum-based model, whereas for premium brands differences are smaller and not significant. (In Appendix F we provide more details regarding the YouGov data that were used for the perceived quality and willingness to recommend measurements.)

![](/api/attachments/6EC8QF27/fulltext/images/1c113405941b0ab49522015fc5e8ff592b6a064a3f72ee0233f06e2f16147388.jpg)

Figure E1. Prediction Results for Low- Versus High-Perceived Quality Brands Using LR and One Lag of Data

![](/api/attachments/6EC8QF27/fulltext/images/558d9be0ce6b3dbbe18b9752acc367e4fc6163fa3e792eb48d51797d5d0b6037.jpg)

Figure E2. Prediction Results for Low- Versus High-Willingness-to-Recommend Brands Using LR and One Lag of Data

![](/api/attachments/6EC8QF27/fulltext/images/4d957e0629d3be4961496e54d9b1f3c5116df9054e594f0a1cefd74d00fcb109.jpg)  
Figure E3. Prediction Results for Low- Versus High-Price Brands Using LR and One Lag of Data

![](/api/attachments/6EC8QF27/fulltext/images/e3e201ed2b174ac378731452c44274f8e88b4edec0b4a1040758e631f265b95c.jpg)

![](/api/attachments/6EC8QF27/fulltext/images/43a14b4c3f9161c747a6301044a8614fbd5f1e82982b4e0fa7b3157640effe41.jpg)

Figure E5. Prediction Results for Low- Versus High-Willingness-to-Recommend Brands Using LR and Two Lags of Data

## Appendix F

## YouGov Survey Data

In this work we utilized customer perception data obtained from YouGov plc. YouGov monitored a panel of 5,000 people in the United States, on a daily basis, and reported on brand-related perceptions. Our data regarding perceived quality and willingness to recommend were based on survey participants’ average ratings for the period 2008–2010.<sup>4</sup> Regarding product quality, panel participants were presented with the following questions on a daily basis:

Which of the following brands do you think represents good quality?

• Now which of the following do you think represents poor quality?

Daily quality scores were calculated according to the following formula:

$$
\text { Perceived   Quality } = \frac {\text { PositiveCount } - \text { NegativeCount }}{\text { PositiveCount } + \text { NegativeCount } + \text { NeutralCount }}
$$

Regarding willingness to recommend, panel participants were presented the following questions on a daily basis:

• Which of the following brands would you recommend to a friend or colleague?

Which of the following brands would tell a friend or colleague to avoid?

Daily willingness-to-recommend scores were calculated in a similar manner to the quality scores, according to the following formula:

$$
\text { Willingness   to   Recommend } = \frac {\text { PositiveCount } - \text { NegativeCount }}{\text { PositiveCount } + \text { NegativeCount } + \text { NeutralCount }}
$$

To avoid question biases, YouGov utilizes different respondents for each question. During the relevant time period, the average number of daily respondents for the quality question was 130 (s.d. 25.2). The average number of daily respondents for the willingness-to-recommend questions was 126 (s.d. 23.7).<sup>5</sup>

<sup>4</sup>For the Hyundai and Kia brands, data are available only for 2010.

## Appendix G

## Car Model-Level Analysis

The main body of the paper reports on predictions of car brand sales. In this appendix we present a robustness check that involves prediction of car model sales. To evaluate predictive accuracy at the car model level, we created a data set consisting of all the car models whose annual sales exceeded 10,000 units in the United States, and that were sold continuously (and not replaced by a new model with the same name) during the years 2007–2010 (a total of 78 car models).

## Main Analysis

Figure G1 displays the car model-level results obtained with LR using the different data representations. Table G1 presents the differences in MAPE values (performance differences) between models utilizing different sets of data and the corresponding significance values using a bootstrap confidence interval. The results reported include models with one lag of data and with two lags of data. Notably, although we tested prediction models using up to five lags of data, we found that adding data from lag 3 or higher actually degraded predictive accuracy for all the models. (In effect, this degradation actually begins at lag 2 for all models except for the forum-based models, which display a minor improvement at lag 2.) Overall, the car-model-level results are in line with the car-brand-level results reported in the main body of the paper: Specifically, the combined model significantly improves predictive accuracy as compared with models based on forum data alone, and models based on search trend data alone obtain comparable (or superior) results to those of forum-based and extended forum-based models.

![](/api/attachments/6EC8QF27/fulltext/images/71e9439be3801b68eb5d7998ff7e3d597442329bd388a33f4c0df40a912b1ed8.jpg)

<table><tr><td colspan="4">Table G1. MAPE Differences and One-Sided Confidence Intervals for the Difference in MAPE Values</td></tr><tr><td>Model A</td><td>Model B</td><td>LR – Lag 1</td><td>LR – Lag 1,2</td></tr><tr><td>Forum-Based Model</td><td>Benchmark Model</td><td>-0.04%</td><td>0.19%***</td></tr><tr><td>Extended Forum-Based Model</td><td>Benchmark Model</td><td>-0.14%</td><td>0.09%</td></tr><tr><td>Search Trends-Based Model</td><td>Benchmark Model</td><td>0.46%***</td><td>0.09%</td></tr><tr><td>Combined Model</td><td>Benchmark Model</td><td>0.33%***</td><td>0.25%**</td></tr><tr><td>Search Trends-Based Model</td><td>Forum-Based Model</td><td>0.5%***</td><td>-0.10%</td></tr><tr><td>Search Trends-Based Model</td><td>Extended Forum-Based Model</td><td>0.6%***</td><td>0.00%</td></tr><tr><td>Combined Model</td><td>Forum-Based Model</td><td>0.37%***</td><td>0.06%</td></tr><tr><td>Combined Model</td><td>Extended Forum-Based Model</td><td>0.47%***</td><td>0.15%*</td></tr><tr><td>Combined Model</td><td>Search Trends-Based Model</td><td>-0.13%</td><td>0.15%*</td></tr></table>

Table G1 reports the difference in MAPE using two models (Model A and Model B - each based on different data inputs) while considering 1 or 2 lags with the LR algorithm. Specifically, the table reports the difference: diff = MAPE(Model B) - MAPE(Model A). Therefore, a positive value associated with the comparison between Model A and Model B indicates better predictive accuracy of Model A over Model B. Lower confidence interval bounds for diff were calculated using 2000 iterations of the BCA bootstrapping confidence interval calculation method implemented in R software. A lower confidence interval bound for diff, with a positive value, provides confidence that MAPE(Model A) is indeed better than MAPE(Model B). We report the following lower confidence bounds:

0.9 lower confidence bound for diff is positive

\*\* 0.95 lower confidence bound for diff is positive

\*\*\* 0.99 lower confidence bound for diff is positive

## Premium Versus Value Models

For robustness we compared the performance of the combined model with that of the extended forum-based model for different car characteristics at the car model level. Figure G2 presents the prediction results for high price (premium) versus low price (value) car models (defined, as in the main body of the paper, using a price threshold of \$20,000, and one lag of data). Results are consistent with the brand-level results in that the difference in predictive accuracy between the combined model (adding search trends over forums data) and the extended forum-based model is larger for low-price car models

![](/api/attachments/6EC8QF27/fulltext/images/b3cb6330cbc7f137638946b9a3f0204352294e915b7bd62848cf3947684854fa.jpg)

Figure G2. Prediction Results for High-Price Versus Low-Price Car Models

## Appendix H

## Additional Robustness Checks Based on Extended Keyword Selection and MSE Criteria

## Extended Keyword Selection

To test the robustness of our results to the keyword selection process, we repeated the analysis using a different keyword selection method. Specifically, we added predictors (explanatory variables) to the models described in the main body of the paper, based on search and forum data derived from additional keywords: specifically, keywords associated with the top selling car model for each brand. Figure H1 displays the results obtained with LR models. Overall, the findings obtained using this keyword approach are similar to those obtained using the keyword approach reported in the main body of the paper.

![](/api/attachments/6EC8QF27/fulltext/images/0ebed21148d5fb8d7551d4e8cea1880f7050743ed631671efb660a6d6e6387c6.jpg)  
Figure H1. Prediction Results for Extended Keyword Selection

## MSE Results

In this section we provide results using Mean Squared Error (MSE) criteria rather than MAPE, which was used in the main body of the paper. Figure H2 displays the results obtained with LR using the different data representations. Analyses carried out using the MSE criteria yielded similar results to those reported in the main body of the paper using the MAPE criteria.

![](/api/attachments/6EC8QF27/fulltext/images/da2b15edc4adaab37439d8c23991a70081c6d26ef0d1ec42da725f22510624e8.jpg)

Figure H2. Prediction Results (MSE)

## Appendix I

## Additional Information on Neural Networks

The neural network is a biologically inspired model that attempts to learn patterns from data directly (Rumelhart et al. 1986). The NN is represented by a weighted directed graph containing three types of nodes (or neurons) organized in layers: the input nodes, the hidden nodes and the output node(s). A neuron receives input signals from a previous layer, aggregates those signals based on an input function, and generates an output signal based on an output (or transfer) function. The output signal is then routed to the other nodes in the network according to the network configuration. Each link connecting any two nodes is characterized by a weight. These weights are determined through a training process in which the NN repeatedly receives examples of past data instances for which the actual output is known, thereby allowing the system to adjust the weights.

Finding the values of these weights requires solving an optimization problem. Perhaps the most common method is the backpropagation algorithm (see, for instance, Bishop 1995). This method consists of two phases: feed-forward and backward-propagation. In the feed-forward phase, outputs are generated for each node on the basis of the current weights and are propagated to the output nodes to generate predictions. Then, in the backward-propagation phase, “prediction errors” are propagated back, layer by layer, and the weights of the connections between the nodes are adjusted for error minimization. The feed-forward and backward-propagation phases are executed iteratively, until convergence.

Figure I1. An Illustration of a Simple NN

## Appendix J

## Forum Data Characteristics

In order to represent forum data we used Google’s vast scan of the Internet. To the best of our knowledge, this is the most comprehensive scan of forum data that has been made available for any academic research. Figure J1 provides a distribution of the relative volume of forum mentions per brand. Figures J2 and J3 provide distributions of the volume of forum mentions with positive or negative sentiment, respectively.

![](/api/attachments/6EC8QF27/fulltext/images/eb5c456daf9bc47158e0666414faaabf6904e92635d0974d85c02ea639b367da.jpg)

## Figure J1. Brand Forum Mention Average Volume (by Decile)

Figure J1 presents a distribution of scaled forum mention volume for the 23 different brands. To preserve data confidentiality, the volume of forum mentions for each brand is scaled using the following method: (brand mention volume) / [(volume for the most mentioned brand) – (volume for the least mentioned brand)]

![](/api/attachments/6EC8QF27/fulltext/images/76b7327045eaae3a026a225c061c35acc51c1c11711408f0862af17f73002b83.jpg)  
Figure J2. Brand Forum Positive Sentiment Average Volume (by Decile)

Figure J2 presents a distribution of scaled positive sentiment mentions for the 23 different brands. To preserve data confidentiality, the volume of positive mentions for each brand is scaled using the following method: (brand positive mentions volume)/[(positive mentions for the brand with the highest volume of positive mentions) – (positive mentions for the brand with the lowest volume of positive mentions)]

![](/api/attachments/6EC8QF27/fulltext/images/14081e1dd56e9bb72254468c5bfa0dddb80f0e1a0d2077801d2ef5ab7ade6d26.jpg)

## Figure J3. Brand Forum Negative Sentiment Average Volume (by Decile)

Figure J3 presents a distribution of scaled negative sentiment mentions for the 23 different brands. To preserve data confidentiality, the volume of negative mentions for each brand is scaled using the following method: (brand negative mentions volume)/[(negative mentions for the brand with the highest volume of negative mentions) – (negative mentions for the brand with the lowest volume of negative mentions)]

## References

Bishop, C. . 1995. Neural Networks for Pattern Recognition, Oxford, UK: Clarendon Press.

Rumelhart, D. E., McClelland, J. L., and Williams, R. J. 1986. “Learning Internal Representation by Error Propagation,” in Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Cambridge, MA: MIT Press, pp. 318-362.

Werbos, P. J. 1974. “Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences,” unpublished Ph.D. dissertation, Harvard University.

Zhang, G., Patuwo, B. E., and Hu, M. Y. 1998. “Forecasting with Artificial Neural Networks: The State of the Art,” International Journal of Forecasting (14:1), pp. 35-62.
