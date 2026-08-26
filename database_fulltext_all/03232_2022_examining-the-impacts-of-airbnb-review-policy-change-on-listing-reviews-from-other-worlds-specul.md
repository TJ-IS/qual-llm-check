---
otero_id: 3232
otero_key: "DCCYV7F8"
title: "Examining the Impacts of Airbnb Review Policy Change on Listing Reviews From Other Worlds: Speculative Engagement Through Digital Geographies"
authors: "Reza Mousavi; Kexin Zhao"
year: "2022"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00720"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2022

# Examining the Impacts of Airbnb Review Policy Change on Listing Reviews

Reza Mousavi

, mousavi@virginia.edu

Kexin Zhao

, kzhao@uncc.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Examining the Impacts of Airbnb’s Review Policy Change on Listing Reviews

Reza Mousavi<sup>1</sup>, Kexin Zhao<sup>2</sup>

<sup>1</sup>Mclntire School of Commerce, University of Virginia, USA, mousavi@virginia.edu <sup>2</sup>Belk College of Business, University of North Carolina at Charlotte, USA, kzhao@uncc.edu

## Abstract

In July 2014, Airbnb, one of the biggest firms in the sharing economy, decided to change the way that guests and hosts reviewed each other on the platform. Prior to this change, guests/hosts could pos reviews about their experiences asynchronously—the guest/host would be able to see the other party’s review whenever it was posted. In contrast, the new review policy rolled out a simultaneous review system, making reviews viewable only after both the guest/host post their own reviews. This study empirically evaluates the impacts of this new review policy on the informativeness of guest reviews, measured by both informational content (semantic diversity and objectivity) and personal opinions (sentiment and sentiment heterogeneity). Using regression discontinuity design and a variety of techniques in the text analytics domain including a novel adaptation of BERT, we demonstrate that Airbnb’s review policy change enhanced the informational content of guest reviews in terms of semantic diversity and objectivity. We also show that review sentiment was reduced but became more diverse. Subgroup analysis revealed that low-quality listings were subject to more changes than high quality listings. We further explore the short-term and long-term effects of the review policy change and demonstrate that the simultaneous review system has had a long-lasting impact on the informativeness of guest reviews.

Keywords: Sharing Economy, Airbnb, Online Reviews, Regression Discontinuity in Time (RDiT), Bidirectional Encoder Representations from Transformers (BERT), Parallel Coordinates, Text Analytics

Zhenhui Jiang was the accepting senior editor. This research article was submitted on March 8, 2019 and underwent three revisions.

## 1 Introduction

A new player in the digital economy, the sharing economy or gig economy, has emerged and thrived in recent years, significantly affecting how people live and make a living. These internet-based, open, and collaborative platforms make the sharing of skills and assets cheaper and easier than ever (Bhappu & Schultze 2018). Underutilized resources can be collectively consumed, generating extra income for their owners. People can access a wide variety of assets in the sharing economy, such as lodging (Airbnb), ride sharing (Uber), everyday chores (TaskRabbit), pet sitting (Rover), and countless others. According to a recent survey published by eMarketer, the number of US sharing economy users is expected to grow from 81 million in 2019 to 101.9 million in 2023 (Droesch, 2020). While the COVID-19 pandemic has caused huge disruptions to the sharing economy, necessary changes strengthening community-based collaboration and efficiency “will help it survive the pandemic and thrive afterwards” (Lees, 2020).

For the sharing economy to be sustained, building interpersonal trust is pivotal to facilitating decentralized peer-to-peer exchanges (Sundararajan, 2016). The sharing economy can flourish if and only if people feel comfortable exchanging goods or services with total strangers. Therefore, reputation systems have been established by sharing economy platforms to cultivate trust within their user communities (Abrahao et al., 2017). User-generated reviews need to be informative in order to facilitate consumers’ decisionmaking (Burtch et al., 2018; Chen et al., 2018; Hong et al., 2016; Sun et al., 2019). Yet people sometimes do not truly or freely share their experiences for various reasons, such as fear of social isolation, fear of retaliation, or selection bias (Bolton et al., 2013; Dellarocas et al., 2006; Hu et al., 2009; Li & Hitt, 2008). Consequently, a J-shaped distribution of online user reviews has been observed in many empirical settings, where a small number of highly negative reviews are mixed with overwhelmingly positive ratings (Hu et al., 2009). For instance, a 2015 survey conducted by Zervas et al. (2017) revealed that nearly 95% of Airbnb listings had average user ratings of 4.5 stars or higher (on a 5- star rating system). Since it is difficult for consumers to differentiate products/services if they all receive similar reviews, it is important to continuously make design and policy changes to improve review informativeness, enabling consumers to access sufficient and factual details and allowing them to consider diverse opinions from fellow reviewers. Table 1 illustrates various types of review systems adopted by sharing economy platforms in terms of review direction (i.e., unidirectional reviews from customers to service providers vs. bidirectional reviews between the two sides), aggregation (i.e., anonymous and aggregated reviews vs. individual reviews with identity information), and simultaneity.

Our research focuses on the simultaneity of reviews and investigates its impact on review informativeness. In bidirectional review systems, where reviewers’ identities are known to each other, excess reciprocity can distort online reputation (Livan et al., 2017). One proposed design that previous research claims can prevent such excess reciprocity is the double-blind or simultaneous review system, where “conventional feedback would only be revealed after both traders submitted feedback or after the deadline for feedback submission expired.” (Bolton et al., 2013, pp. 270). In contrast, the asynchronous review system publishes reviews to everyone immediately after its submission. The asynchronous review system potentially biases reviews by manipulating positive and negative reciprocity (Malmendier et al., 2014). People may first leave an inflated review to encourage positive reciprocity from the other party, or they may choose to eschew leaving negative reviews to avoid triggering potential retaliation because of negative reciprocity.

There is some evidence that, compared to the asynchronous system, the simultaneous review policy can better manage reciprocity to mitigate biases in the review process (Bolton et al., 2013; Fradkin et al., 2018; Preserpio et al., 2018). However, the impacts of the simultaneous review system have not been tested via large-scale observational data over an extended period of time. In July 2014, Airbnb changed its review system from an asynchronous design to a simultaneous review mechanism in order to “help build this trust, and to help our community share and receive honest feedback.” <sup>1</sup> This event provides us with a rare opportunity to empirically quantify the effect of the review policy change in enhancing review informativeness over time. Review informativeness predicts review helpfulness (Ghose & Ipeirotis, 2011) and can be represented by multidimensional attributes of review content (Singh & Tucker, 2017; Sun et al., 2019). We assess review informativeness based on the comprehensive analyses of the textual features of reviews, which are further categorized into two dimensions. The first dimension focuses on the informational content embedded in the review, which includes its semantic diversity and objectivity. The second dimension captures personal opinions shared by reviewers and is reflected by sentiment as well as sentiment heterogeneity in the review.

Based on regression discontinuity in time, we found that the simultaneous review system enhances the informational content of reviews because, under this system, reviews offer more semantic meaning and become more objective. Furthermore, our findings indicate that the simultaneous review system both deflates and diversifies personal opinions. In our study, such impacts were moderated by product quality, where lower quality listings were subject to more changes. Our analyses further reveal why sentiment is lower in the new review system. We conducted polarity classification and used positive and negative emotions to differentiate effects associated with positive and negative reciprocity. Under the simultaneous review system, we found that people are less likely to pretend to be nice in that they use fewer words that are associated with positive emotions. Meanwhile, our findings indicate that negative emotions were not affected by this policy change. Supplementary panel analysis suggests that changes associated with the simultaneous review system are sustained over time. Our research sheds light on the impact of review simultaneity on the multidimensional textual attributes of guest reviews.

We organize our paper as follows. We first review the prior literature, identify the research gap, and propose hypotheses. Then, we discuss our research setting, data sources, and empirical analyses. Finally, we present the results, summarize our contributions, and point out directions for future research.

Table 1. Examples of Review Systems Adopted by Sharing Economy Platforms

<table><tr><td>Sharing platforms</td><td>Bidirectional review system</td><td>Aggregated review system</td><td>Simultaneous review system</td></tr><tr><td>Rover (pet sitting)</td><td>N</td><td rowspan="3" colspan="2">Not applicable in unidirectional systems</td></tr><tr><td>JustPark (parking)</td><td>N</td></tr><tr><td>Zaayly (chores)</td><td>N</td></tr><tr><td>Uber (ride)</td><td>Y</td><td>Y</td><td rowspan="3">Not applicable in aggregated review systems</td></tr><tr><td>Lyft (ride)</td><td>Y</td><td>Y</td></tr><tr><td>Getaround (ride)</td><td>Y</td><td>Y</td></tr><tr><td>TaskRabitt (chores)</td><td>Y</td><td>N</td><td>N</td></tr><tr><td>Airbnb (lodging)</td><td>Y</td><td>N</td><td>Y</td></tr><tr><td>Turo (ride)</td><td>Y</td><td>N</td><td>Y</td></tr><tr><td>Upwork (freelancing)</td><td>Y</td><td>N</td><td>Y</td></tr></table>

## 2 Literature Review

Two streams of research—the sharing economy literature and research on reciprocity and review biases—are closely relevant to our current study. Because of the rapid development of sharing economy platforms over the past decade, hundreds of studies have been conducted by academia, industry experts, and policy makers to understand the theoretical foundations and impacts of the sharing economy (Alyakoob & Rahman, 2019; Chen et al., 2019; Sundararajan, 2016; Zervas et al., 2017). For instance, Bivens (2019) provided an extensive review of studies on the economic costs and benefits of Airbnb. Using co-citation analysis and content analysis, Cheng reviewed 66 sharing economy papers published between 2010 and 2015 and identified five clusters of sharing economy research, including lifestyle and social movement, consumption practice, sharing paradigm, trust, and innovation (2016). Among those five research topics, trust emerged as a central issue in overcoming uncertainty and facilitating transactions in the sharing economy. Huurne et al. (2017) qualitatively synthesized 45 articles to summarize the antecedents of trust in the sharing economy. Reputation systems have been identified as one of the most important tools in building trust in the sharing economy (Sundararajan, 2016; Abrahao et al., 2017; Huurne et al., 2017; Proserpio et al., 2018). However, reciprocity naturally arises in the sharing economy, which can potentially distort user ratings (Proserpio et al., 2018).

User-generated online reviews are biased if they do not reflect the true quality of the underlying products/services. Prior literature has identified different types of review bias, such as underreporting bias (Askay, 2015; Hu et al., 2009), selection bias (Li & Hitt, 2008), social influence bias (Muchnik et al., 2013; Piramuthu et al., 2012), and bias based on strategic manipulation (Dellarocas, 2006; Mayzlin et al., 2014). Lin et al. (2019) offer a more detailed discussion of mechanisms leading to review biases. Some factors, such as selection bias, trend following, and expectation confirmation, reflect the dynamic aspects of user ratings (Li & Hitt, 2008; Hu et al., 2009; Godes & Silva, 2012). Other factors, including selfpresentational concerns, social influence, as well as reciprocal behavior, are based on users’ social concerns (Askay, 2015; Muchnik et al., 2013; Wang et al., 2018).

For sharing economy platforms using bidirectional review systems, exchanges and reviews are reciprocal in nature. The existence of reciprocity in a social context is associated with higher than normal user ratings (Bolton et al., 2013; Dellarocas & Wood, 2008; Lin et al., 2019; Livan et al., 2017; Proserpio et al., 2018). Consequently, many of these platforms feature overwhelmingly positive reviews. Zervas et al. (2017, p. 4) compared properties listed on both Airbnb and TripAdvisor and found that “14% more of these crosslisted properties have a 4.5-star or higher rating on Airbnb than on TripAdvisor.” If all or most reviews are similar and highly positive, they become uninformative for users seeking to evaluate and differentiate the underlying products. Therefore, platforms should carefully design reputational systems to manage reciprocity and enhance review informativeness.

According to Bolton et al. (2013), simultaneous review systems can be more effective in managing reciprocity than asynchronous systems. When both parties of a transaction can write reviews to each other, the timing of reviews becomes a crucial issue, leading to key distinctions between asynchronous review systems and simultaneous review systems. In an asynchronous review system, one party can wait to respond to a review after reading its content, and reciprocal behavior is expected to be triggered and induced. People may leave inflated positive comments in order to encourage positive reciprocity from the other party. They may hesitate to leave negative comments because of concerns of negative reciprocity, where “reputation builders retaliate for negative reviews.” (Bolton et al., 2013, p. 265). In contrast, the simultaneous review design, where comments are visible only after both parties of the transaction have submitted their reviews, can effectively alleviate biases associated with reciprocal behavior. Bolton et al. (2013) conducted a controlled lab experiment and found that feedback blindness reduces the correlation between sellers’ and buyers’ reviews and increases negative feedback. In addition, simultaneous reviews are more informative than asynchronous reviews because they can better signal sellers’ quality. Fradkin et al. (2018) collected data from a field experiment conducted on Airbnb between May 10, 2014, and June 12, 2014. They found that simultaneous review design led to a 1.6% reduction in the percentage of 5-star ratings. Both studies suggest that reviews tend to be more negative immediately after the implementation of a simultaneous review system.

Our research extends prior literature in several ways. First, we collect and analyze long-term field observational data and investigate the impacts of the simultaneous review system over time. While the impact of simultaneous review systems has been studied via controlled lab experiments (Bolton et al., 2013) and field experiments (Fradkin et al., 2018), our findings offer important empirical evidence based on a large data set of naturally occurring behavior. Second, we use review informativeness, captured by a comprehensive list of textual features, to quantify the impact of simultaneous review systems in a more nuanced way. Prior literature focuses on either star ratings or binary positive/negative review classification (Bolton et al., 2013; Fradkin et al., 2018). In addition to sentiment, we examine other major features of the reviews suggested by text analytics research: semantic diversity, objectivity, and sentiment dispersion. Third, our analyses are conducted at the product level by aggregating reviews received by each property listing. While individual reviews reflect a traveler’s unique experiences based on a single trip, they are subject to influences from individual reviewer and trip characteristics that are unobservable because of data limitations. Thus, we focus on the collective intelligence of a product by analyzing aggregate guest reviews (Muchnik et al., 2013). More importantly, this unit of analysis enables us to apply dispersion measures to assess reviews’ semantic diversity and sentiment dispersion across users of a single product. Rating dispersion is a useful indicator for product differentiation, especially in the context of experience goods (Clemons et al., 2006; Hong et al., 2014).

## 3 Hypotheses

Consumers use reviews to overcome problems related to product uncertainties and transaction risks associated with online shopping. Hence, informative reviews should help consumers effectively infer product quality (Chen & Xie, 2008; Sun et al., 2019). To do so, informative reviews provide consumers with both information and opinions about a product. Information refers to content that describes the facts and attributes of a product learned via consumption, while opinions signify attitudes, feelings, and emotions experienced by individual reviewers (Liu, 2012). Therefore, we propose measuring review informativeness along the two dimensions of informational content and personal opinions. Advances in natural language processing (NLP) and deep learning helped us extract informational content, including semantic diversity and objectivity, and opinion mining, or sentiment analysis, enabled us to collect, categorize, and discover personal sentiments (Aggarwal & Zhai, 2012; Pang & Lee, 2008).

In an asynchronous review system (such as the one used by Airbnb prior to July 2014), rational reviewers consider the potential response of the counterparty while writing their own comments. They expect the counterparty to reciprocate or retaliate if they submit a review first. Alternatively, they may strategically wait and construct their reviews after reading the counterparty’s review. Therefore, providers’ and consumers’ feedback tends to be highly correlated in an asynchronous review system such as eBay’s (Bolton et al., 2013), suggesting a pattern of reciprocity (Resnick & Zeckhauser, 2002). The reciprocity of asynchronous review systems likely results in strategic considerations. The consequences of these strategic considerations (e.g., waiting for the counterparty to post a review first or posting a very positive review early on to benefit from counterparty reciprocity) include information loss (Fradkin et al., 2018), reduction of informativeness (Bolton et al., 2013), and lower accuracy (Güth et al., 2007) of the review.

The simultaneous review system, however, removes such reciprocal opportunities and strategic considerations because both guest and host reviews are confidential until both parties submit their reviews or until the review deadline passes (Bolton et al., 2013; Güth et al., 2007). According to the results of a field experiment reported in Fradkin et al.’s work (2018, p. 1), the “simultaneous reveal review system, which eliminated strategic considerations from reviews, … made the reputation system more informative.” Fradkin et al. argue that switching from an asynchronous review system to a simultaneous review system mitigates the information loss caused by strategic considerations. Similar findings have been reported in other platforms such as eBay (Bolton et al., 2013) and in other online markets (Güth et al., 2007).

We expect the simultaneous review system to enhance the informativeness of reviews (i.e., informational content) in two ways. First, the amount of information, measured by the semantic diversity of reviews, may increase in a simultaneous review system. Semantic diversity summarizes differences in terms of semantic meaning, concepts, or themes presented in the review, indicating the breadth of review content (Aggarwal & Zhai, 2012). Semantic diversity has been shown to be a valuable measure for the information abundance of a review (Son et al., 2019). The simultaneous review system alleviates several constraints associated with review reciprocation and encourages reviewers to provide a variety of content (Montini, 2014). Our research focuses on guest reviews on the Airbnb website. In Airbnb’s asynchronous review system (prior to the policy change in July 2014), guests could post their reviews either before or after hosts. If guests posted their reviews before their host, they tended to avoid controversial or sensitive themes or topics that might elicit retaliatory responses from the host (fear of retaliation). Such reviews would hence be expected to contain less informational content. If guests post reviews after hosts, prior research has shown that guest reviews are highly correlated with host reviews (Bolton et al., 2013). Given that the hosts often provide reviews for many guests and that writing many reviews may be a time-consuming effort for them, they may avoid posting detailed and diverse reviews for each guest they accommodate. In fact, many hosts likely reuse and customize templates for their reviews. <sup>2</sup> Given the lack of informational content in host reviews, guest reviews that are posted after host reviews, according to Bolton et al. (2013), will likely be less informative and contain less semantic diversity. If the simultaneous review system indeed increases review informativeness, we would that after Airbnb’s switch to the new review system, guests would write reviews with increased semantic variation and a greater variety of topics describing the property and the trip. Thus, we hypothesize:

H1a: Compared to the focal asynchronous review system, the simultaneous review system increases informational content, measured by the semantic diversity of textual reviews.

Second, review simultaneity may encourage information objectivity provided by user comments. User textual reviews are a mixture of objective and subjective sentences (Ghose & Ipeirotis, 2011). While subjective comments reflect individual reviewers’ private beliefs, objective comments benefit consumers by allowing them to access factual product descriptions, signaling the quality of informational content (Lee & Lee, 2009; Montoyo et al., 2012; Zhang et al., 2019). In an asynchronous review system, the two sides of the business transaction can start a conversation when the second mover replies to the first mover’s comments. However, such human interactions during the review process are no longer possible in a simultaneous review system. The interplay between individuals develops a person’s subjectivity by reinforcing the relation and engagement between individuals (de Sousa, 2004; Kehrwald, 2010). Simultaneous review systems may reduce subjectivity by eliminating possible dyad communications between the two sides of the review. Furthermore, social presence, defined as the feeling of being together (Short et al., 1976), promotes the subjectivity of perspective (Kehrwald, 2010). Simultaneous review systems would be expected to reduce social presence because the guest recognizes that the potential for talking to the host during the review process is minimal. Consequently, we would expect review subjectivity to manifest less in a simultaneous review system and anticipate that reviewers are more likely to focus on objective attributes of their prior transactions rather than on subjective or private beliefs induced by feedback reciprocation. Therefore, we posit:

H1b: Compared to the focal asynchronous review system, the simultaneous review system increases informational content, measured by the objectivity of textual reviews.

We expect simultaneous review systems to affect the personal opinions of reviewers by reducing sentiment scores in their comments (Bolton et al., 2013; Fradkin et al., 2018). In contrast to asynchronous review systems, in simultaneous review systems, there is no need for reviewers to write overly positive comments in anticipation of positive reciprocity from their transaction partners.

Inversely, synchronous review systems would be expected to increase the amount of negative feedback reported because of reduced fear of retaliation. Fear of retaliation is a key reason underlying individuals reluctance to share negative opinions in various environments. For instance, in institutions, whistleblowing is less likely to occur in retaliatory climates (Mesmer-Magnus & Viswesvaran, 2005). Similarly, in online review systems, “the removal of the threat of retaliation appears to embolden a dissatisfied buyer who is, then, more likely to post negative feedback for the seller” (Dellarocas & Wood, 2008, p. 470).

Moreover, mitigated reciprocity can contribute to increased sentiment heterogeneity, which is measured by the dispersion of reviews’ sentiment scores. Simultaneous review systems remove the possibility of strategic timing that allows second movers to align their opinions with first movers. Individual reviewers thus have the freedom to express their opinions and emotions about their experience more truthfully in a simultaneous system. Moreover, in the Airbnb context, this sharing economy platform supplies niche lodging options from a large number of private homeowners, and the associated lodging experience can be highly personal. While some people might love a particular home, others may feel like it is a mismatch. In a simultaneous review system, we would expect reviewers to be less hesitant to speak out and would anticipate that their real and varied opinions would be less likely to be suppressed. Such sentiment dispersion is linked to improved informativeness of the feedback mechanism (Bolton et al., 2013), especially for niche products (Sun, 2012). Therefore, we hypothesize that:

H2a: Compared to the focal asynchronous review system, the simultaneous review system reduces the sentiment scores of reviews.

H2b: Compared to the focal asynchronous review system, the simultaneous review system increases the dispersion of the sentiment scores of reviews.

While we expect review simultaneity to be beneficial to review informativeness, its impact may vary, depending on the quality of the underlying products. Prior studies have found that the interplay between product quality and review characteristics influences subsequent sales. Specifically, the informational role of product ratings depends on product quality, and the variance of product ratings is less influential for highquality products (Sun, 2012). Similarly, we argue that product quality moderates the impact of review simultaneity and the improvement of review informativeness because review simultaneity is less apparent for high-quality products. In our case, highquality properties offer superior features, amenities, services, and location convenience, and guests are more likely to enjoy their lodging experiences and remain satisfied. The need to suppress negative reciprocity in asymmetric review systems would be expected to decrease with high-quality properties. Since the transaction process tends to be smooth and uneventful for high-quality properties, people’s desire to inflate reviews to trigger positive reciprocity would also be expected to diminish. Consequently, we anticipate that the review platform’s switch from an asynchronous system to a simultaneous system would impact high-quality properties less. Thus, we propose:

H3: Review textual content changes associated with review simultaneity are diminished in the context of high-quality products.

## 4 Empirical Setting and Data

## 4.1 Airbnb Policy Change

When it began in August 2008, Airbnb instituted a conventional asynchronous review mechanism. Guests and hosts could leave reviews about the other party immediately after the transaction took place. Under this review scheme, one party could wait until the other party left a review and then post their own review. On July 10, 2014, Airbnb rolled out its new review system, which is in effect to date. The new system allows reviewers (both guests and hosts) to view the other party’s review only after they left their own review. Alternatively, they can view the other party’s review 14 days past the trip date but are longer able to post their own review. This change in policy ensures review simultaneity since neither hosts nor guests are aware of the other party’s review when they post their own review. Therefore, we examine the extent to which this change of policy altered certain features of guest reviews.

When Airbnb implemented the simultaneous review system in July 2014, it also introduced two other relatively minor changes. We argue that review simultaneity is the main driver behind the differences observed from public guest comments before and after the policy change. The first change was to shorten the review period from 21 days to 14 days. However, this reduced time window would only affect a small percentage of reviews, since 90% of Airbnb reviews were submitted within two weeks even before the policy change.<sup>3</sup> With review simultaneity, the potential impact from the reduced time window would be even more negligible. People submit reviews faster in the simultaneous review system than in the asynchronous system since they are eager to read the counterparty’s comments. This phenomenon has been empirically observed in Fradkin et al.’s field experiment (2018), which indicated that guests took an average of 4.3 days to leave a review under the simultaneous system (Fradkin et al., 2018). The second change was the introduction of private feedback that guests could leave hosts, which we anticipate would reduce the potential effect associated with review simultaneity. Many guests do not leave any comments via the optional private feedback channel, since they already have many other channels, such as Airbnb messages, to communicate with their hosts privately. However, some users might write additional comments, especially opinionated ones, via the private feedback channel, which may reduce the informational content and negative emotions viewable from the public comment section. We empirically quantify the changes associated with review simultaneity with the introduction of the private feedback channel and expect the impacts to be even stronger without the private feedback channel. Observational data from naturally occurring events are noisy, and we recognize the inability to fully control the other two changes as a limitation of our data.

## 4.2 Airbnb Data

We obtained data about listings and guest reviews from insideairbnb.com, which periodically collects data from Airbnb.com. From the list of cities available, we collected data from a northeast city (Boston), a midwestern city (Nashville), a southern city (Austin), and a western city (San Francisco). Our data include all the listings and their guest reviews from the beginning of July 2012 until the end of June 2016 (two years before the policy change and two years after). It is worth noting that between April and July of 2014, Airbnb was running experiments related to the review policy. The details of the experiments and their results are reported in Fradkin et al. (2018), who state: “The experiments were conducted between April and July of 2014 and consisted of all trips to non-reviewed listings for which the guest did not leave a review within 9 days.” (Fradkin et al., 2018, p. 11) Therefore, we excluded all listings that did not have a review prior to April 2014 from our analysis and kept only listings that had at least one review before April 2014. This exclusion ensured that we only retained listings that were not included in the Airbnb experiments. Overall, the data set included 2,399 listings and 116,464 guest reviews. Table 2 provides information about the number of listings and the number of guest reviews before and after the policy change.

## 4.3 Textual Features of Online Reviews

To gauge the potential changes in the reviews before and after the policy change, we first needed to determine and measure the textual features of the reviews based on the extant literature on online reviews. Table 3 summarizes the textual features obtained from the representative literature. These textual features can be broadly grouped into three categories: semantic diversity, objectivity, and sentiment. Given the widespread use of these textual features in the online review literature, we decided to deploy all three features in our study. We grouped these three features into two dimensions: informational content and personal opinion. As discussed earlier, the informational content is related to the factual information that is covered in guest reviews. Whereas the personal opinion dimension is related to reviewers’ individual opinions about their experience, the diversity of semantic themes and objectivity is embedded in the informational dimension, as they focus on objective language. Sentiment is embedded in the personal opinion dimension as it distinguishes opinion-oriented language from objective language. In the following, we report the process of measuring the textual features of Airbnb’s guest reviews.

## 4.3.1 Information Content

## 4.3.1.1 Semantic Diversity

To understand the breadth of information contained in the reviews, we measured the diversity of semantic meaning in guest reviews. As reported in Table 3, IS scholars have already done this in a variety of contexts. Given that natural language processing (NLP) is a fastevolving domain, we identified the applications of deep learning in NLP as one of the most useful areas for our research. The essential role of deep learning in NLP is the transformation of text data into vector representations. Well-known models such as Word2Vec from Google (Mikolov et al., 2013), GloVe from Stanford University (Pennington et al., 2014), and BERT from Google (Devlin et al., 2018) have made significant changes to NLP-related tasks in recent years. The last one, BERT (i.e., bidirectional encoder representations from transformers), is currently considered the state-of-the-art model for many NLP tasks (Tenney et al., 2019). Therefore, we decided to use BERT to measure the semantic diversity of Airbnb guest reviews. Below, we explain how BERT works for creating representations of text data. Then, we explain our use of a modified BERT model to measure the diversity of semantic meaning in guest reviews.

BERT is an open source language representation model that was introduced by Google in 2018. BERT is a pretrained deep learning model that could be fine-tuned for a variety of NLP tasks and based on a variety of text data (Devlin et al., 2018). It uses a transformer, which is an attention mechanism that can learn contextual relationships between tokens (e.g., words) in a text document. Essentially, transformers are models that process words in relation to all the other words in a sentence, rather than one-by-one in order. BERT models can therefore consider the full context of a word by looking at the words that come before and after it (Nayak, 2019).

Google has released two versions of BERT—BERT Base and BERT Large. Both models are developed based on deep neural networks. In the Base model, there are 12 hidden layers while there are 24 hidden layers in the Large model. BERT is a pretrained model, which means it has already been trained and built using text data. Google used two text data sets to train BERT—2.5B words from Wikipedia and 800M words from BookCorpus (Devlin et al., 2018). BERT Base returns a vector representation length of 768 while BERT Large returns a vector representation length of 1028 for each token. These vector representations can then be used in NLP tasks such as text classification, question answering, and natural language inference. The details of BERT, how it is trained, and how it can be used in NLP tasks are discussed in (Devlin et al., 2018) and its GitHub repository (https://github. com/google-research/bert).

Table 2. The Number of Airbnb Listings and Guest Reviews

<table><tr><td>City</td><td>Listings active before and after change</td><td>Reviews before change</td><td>Reviews after change</td><td>All reviews</td></tr><tr><td>Austin</td><td>961</td><td>9,152</td><td>25,679</td><td>34,831</td></tr><tr><td>Nashville</td><td>134</td><td>3,077</td><td>8,076</td><td>11,153</td></tr><tr><td>Boston</td><td>262</td><td>3,560</td><td>10,127</td><td>13,687</td></tr><tr><td>San Francisco</td><td>1,042</td><td>17,737</td><td>39,056</td><td>56,793</td></tr><tr><td>Total</td><td>2,399</td><td>33,526</td><td>82,938</td><td>116,464</td></tr></table>

Table 3. The Use of Text-Based Constructs in IS Research<sup>4</sup>

<table><tr><td>Dimension</td><td>Text-based features</td><td>Source(s)</td><td>Type of text</td></tr><tr><td rowspan="7">Informational content</td><td rowspan="4">Semantic diversity</td><td>Larsen &amp; Bong (2016)</td><td>Literature reviews</td></tr><tr><td>Li et al. (2017)</td><td>Online reviews and profile descriptions</td></tr><tr><td>Mihalcea et al. (2006)</td><td>Short snippets of text (paraphrase data)</td></tr><tr><td>Islam &amp; Inkpen (2008)</td><td>Microsoft paraphrase corpus</td></tr><tr><td rowspan="3">Objectivity</td><td>Ghose et al. (2012)</td><td rowspan="3">Product reviews</td></tr><tr><td>Ghose &amp; Ipeirotis (2011)</td></tr><tr><td>Goes et al. (2014)</td></tr><tr><td rowspan="14">Personal opinion</td><td rowspan="14">Sentiment</td><td>Aggarwal &amp; Singh (2013)</td><td>Blog posts</td></tr><tr><td>Lau et al. (2012)</td><td>Text from the Web 2.0 environment</td></tr><tr><td>Abbasi et al. (2014)</td><td>Group discussion messages</td></tr><tr><td>Cao et al. (2013)</td><td>Firms’ 10-k forms</td></tr><tr><td>Luo et al. (2017)</td><td>Blog posts</td></tr><tr><td>Huang et al. (2017)</td><td>Online reviews</td></tr><tr><td>Li et al. (2017)</td><td>Online reviews and profile descriptions</td></tr><tr><td>Das &amp; Chen (2007)</td><td>Investors’ messages on Yahoo!</td></tr><tr><td>Stieglitz &amp; Dang-Xuan (2013)</td><td>Tweets</td></tr><tr><td>Goh et al. (2013)</td><td>Content generated on fan page brand community</td></tr><tr><td>Singh et al. (2014)</td><td>Blog posts</td></tr><tr><td>Goes et al. (2014)</td><td>Product reviews</td></tr><tr><td>Moreno &amp; Terwiesch (2014)</td><td>Comments on an online service marketplace</td></tr><tr><td>Gu et al. (2007)</td><td>Users’ posts on an online community</td></tr></table>

In our study, we were interested in obtaining a vector representation for each review in our Airbnb data set. These vectors are essentially numeric representations of the semantic meaning of each guest review. For this task, we chose the BERT Base model using the Python package “spaCy-transformers.”<sup>5</sup> BERT Base returns a vector length of 768 for each token (e.g., word) in each sequence (e.g., sentence).<sup>6</sup> These vectors represent the semantic meaning of the tokens. To obtain the semantic representation of the review (sequence of words), one could either take the mean of the vector representations of the tokens in the review or obtain the vector representation of a special token that is automatically added to the beginning of each sequence before applying BERT. This token is called [CLS] and its vector representation can be used as the vector representation of the whole sequence (sentence/review). Although these two approaches are viable, research shows that they both result in poor sentence embeddings (Reimers & Gurevych, 2019). Therefore, we decided to use a modified version of BERT that is designed for sentence embeddings. This model is called “Sentence-BERT” and is based on Siamese BERT networks (Reimers & Gurevych, 2019).<sup>7</sup> We report our approach for examining the quality of the embeddings in the Appendix.

Using “Sentence-BERT,” we obtained a vector representation with 768 coordinates for each guest review (e.g. [i<sub>1</sub>, i<sub>2</sub>, i<sub>3</sub>, …i<sub>768</sub>] where i<sub>s</sub> is a real number). To determine the semantic diversity of guest reviews for a listing for a specific time period (e.g., one month), we had to calculate some form of deviation among these vectors. To overcome this problem, borrowing from a parallel coordinates technique (Inselberg, 2009), we suggest a novel approach. We use the following example, presented in Figure 1, to explain this approach.

![](/api/attachments/DCCYV7F8/fulltext/images/66c68c435bd647cad7fdebb74908918321b718747d17f6b384308487ad3e2212.jpg)  
Figure 1. Sample Parallel Coordinates of Guest Review Embeddings

Assume there are three documents (guest reviews)—i, j, and k—that are posted for a listing within a certain period of time. Given that we used BERT Base, each review was represented by a vector length of 768. Therefore, there will be 768 coordinates to be considered in our example. In Figure 1, we used Inselberg’s parallel coordinates to visualize vectors i, j, and k. Since we were interested in measuring the semantic diversity of guest reviews for the listing, with respect to each coordinate, we measured the distance of each review’s value to the mean of all values for the listing for the focal coordinate. In other words, we measured the diversity of guest reviews with respect to Coordinate 1 using the following specification:

$$
S D ^ {1} = \sum_ {d} | V _ {d} ^ {1} - M e a n ^ {1} |,\tag{Specification 1}
$$

Where d is the index for the guest review and $M e a n ^ { 1 }$ is the mean value of all reviews for the focal listing within the period of time with respect to Coordinate 1. Conceptually, if the guest reviews have very diverse values with respect to Coordinate $1 , S D ^ { 1 }$ will have a large value. On the other hand, if the documents have similar values with respect to Coordinate 1, then $S D ^ { 1 }$ will have a small value. To measure the diversity of documents with respect to all 768 coordinates in our data, we used this Semantic\_Diversity specification:

$$
\sum_ {n} \sum_ {d} | V _ {d} ^ {n} - M e a n ^ {n} |,\tag{Specification 2}
$$

Where $d$ is the index for the guest review and n is the index for the coordinates from BERT output (max(n) = 768). To ensure that we gave each coordinate an equal chance to contribute to Semantic\_Diversity, we made sure that the coordinates were scaled. Using Specification 2, we calculated the diversity of informational content in guest reviews for each listing for each period if the listing had more than one review.

## 4.3.1.2 Objectivity

According to Liu (2012), “an objective sentence presents some factual information about the world, while a subjective sentence expresses some personal feelings, views or beliefs.” For instance, “Dave’s apartment is close to downtown Austin” is an objective sentence, as it provides a fact about Dave’s apartment. On the other hand, “I did not feel safe in Dave’s apartment” conveys a subjective feeling about Dave’s apartment. To measure the extent to which a review is objective, we used a Python 2.7 package called “TextBlob.”<sup>8</sup> This package uses a naive Bayes analyzer that was developed using Stanford University’s Natural Language Toolkit (NLTK). <sup>9</sup> According to Loria (2017), TextBlob first determines which words would carry any sentiment (positive or negative). For instance, adjectives such as angry or cheerful would have a higher level of sentiment. Then, it determines the likelihood of the sentence being more subjective (having more sentiment) or objective (having less sentiment). TextBlob has been used in empirical research previously (Rajesh & Gandy, 2016; Sahni et al., 2017). TextBlob’s subjectivity scores range from 0 to 1, with 0 being the least subjective and 1 being the most subjective document. Given that we are interested in measuring the objectivity of guest reviews, we converted subjectivity scores obtained from TextBlob to objectivity scores using the following formula: ?????????????????????? = 1 − ???????????????????????? . Therefore, our objectivity score also ranged from 0 to 1 with 0 being the least objective text and 1 being the most objective text.

## 4.3.2 Personal Opinions

Another important dimension of guest reviews is the extent to which they reflect guests’ personal opinions. According to our literature review summarized in

Table 3, personal opinions can be measured using sentiment analysis or opinion mining.

We measured guests’ sentiments cascaded in their reviews by performing sentiment analysis using an R package called “sentimentr”<sup>10</sup> after applying necessary preprocessing, such as removing stop words and stemming. The package “sentimentr” is designed to calculate the polarity of the text at the sentence level. It then allows those sentence-level polarity scores to be aggregated at another level (e.g., paragraph or entire review). Using this approach, we calculated a single sentiment score for each guest review.

We use coefficient of variation (CV) to measure sentiment dispersion (Ghose & Yao, 2011) for a listing within the period of time. Coefficient of variation (CV) is the ratio of standard deviation of sentiment scores to the mean sentiment for each listing.

Along with the sentiment score and CV of sentiments, we measured the positive emotions and negative emotions reflected in the guest reviews using another R package called “Syuzhet,”<sup>11</sup> which uses the NRC Word-Emotion Association Lexicon.<sup>12</sup> This allowed us to examine whether the positive or negative emotions (rather than overall sentiment) were different after the policy change.

## 4.4 Variables

To prepare our data for further analysis, we needed to aggregate each listing’s data according to a unit of time. Given the length of time period in our data (4 years), we decided to use month as the unit of time. This resulted in a data set with a maximum of 48 observations per listing. Table 4 provides information about the variables in our study, their definitions, and summary statistics. The table reports the mean of the variable before and after the policy change for the time-varying variables. It also reports the percentage difference in the mean of those variables before and after the policy change. The values of sentiment and the variables related to emotions all decreased on average after the policy change. On the other hand, the values of the variables Semantic\_Diversity, objectivity, and CV\_Sentiment, increased on average after the policy change.

In addition to the key textual features discussed in the hypotheses, we explore review depth measured as the number of words in a review. Table 4 suggests that guests used slightly fewer words in reviews after the policy change (40.3 words was the average length before the policy change and 38.6 words was the average length after the policy change). Our results indicate that review simultaneity encourages guests to freely talk about many different things/themes, as reflected by our Semantic\_Diversity findings; however, they may do so in more or less detail. Furthermore, in the asynchronous review system, guests might have attempted to please hosts by using especially positive language. Such an effect is diminished in the simultaneous review system, as shown by our empirical analysis, revealing that Positive\_Emotion decreased after the policy change. Thus, the impact of the review policy change on depth remains uncertain.<sup>13</sup>

As shown in Table 4, Review\_Rating ranges from 64 to 100 with a mean of over 95. It is worth noting that the scale of the overall rating for the listings in Airbnb ranges from 0 to 100. The high value of the mean of Review\_Rating indicates that the majority of the guests who left a review had a pleasant experience.

## 5 Methods and Results

We choose regression discontinuity in time (RDiT) analysis as the main method to test the first two hypotheses in our study. Additional sensitivity analysis was conducted to examine the robustness of our results. After testing the first two hypotheses using RDiT methodology, we further explored the extent to which the impact of the policy change on guest reviews endured over time. Similar to Cavusoglu et al. (2016), we used panel data analysis to compare the short-term and long-term effects of the policy change on guest reviews. Finally, we performed subgroup analysis with RDiT to study the moderating role of the quality of the listings on the impact of policy change in terms of the target variables (H3).

## 5.1 Regression Discontinuity in Time (RDiT) Analysis

To examine the potential impacts of policy changes on the target variables, we deployed a quasi-experimental setting informed by the regression discontinuity design (RDD) approach. Given that our data set includes time series of target variables captured before and after the policy change, we used a single-group interrupted time-series experimental design (Cook & Campbell, 1979) that allows for comparison of the patterns of dependent variables before and after an event. In the RDD literature, this method is known as regression discontinuity in time (RDiT).

Table 4. Variable Descriptions and Summary Statistics

<table><tr><td>Variable</td><td>Definition</td><td>Min</td><td>Max</td><td>SD</td><td>Mean before</td><td>Mean after</td><td>Difference in mean (%)</td></tr><tr><td>Semantic_Diversity</td><td>The semantic diversity of guest reviews (as represented by BERT-generated embeddings) per listing per month</td><td>0</td><td>16.626</td><td>0.429</td><td>0.418</td><td>0.509</td><td>19.633</td></tr><tr><td>Objectivity</td><td>The average objectivity of guest reviews per listing per month</td><td>0</td><td>1</td><td>0.162</td><td>0.387</td><td>0.396</td><td>22.988</td></tr><tr><td>Sentiment</td><td>The average sentiment of guest reviews per listing per month</td><td>-0.978</td><td>3.542</td><td>0.452</td><td>0.959</td><td>0.893</td><td>-7.127</td></tr><tr><td>CV_Sentiment</td><td>The coefficient of variation of sentiment per listing per month</td><td>0</td><td>15.580</td><td>0.451</td><td>0.434</td><td>0.515</td><td>17.071</td></tr><tr><td>Negative_Emotion</td><td>The average negative emotion in guest reviews per listing per month</td><td>0</td><td>1</td><td>0.024</td><td>0.015</td><td>0.015</td><td>-0.417</td></tr><tr><td>Positive_Emotion</td><td>The average positive emotion in guest reviews per listing per month</td><td>0</td><td>1</td><td>0.076</td><td>0.138</td><td>0.132</td><td>-4.444</td></tr><tr><td>Depth</td><td>The average number of words in guest review per listing per month</td><td>0</td><td>476</td><td>28.313</td><td>40.310</td><td>38.630</td><td>-4.256</td></tr><tr><td>Review_Rating</td><td>The overall rating of the listing at the time of data collection</td><td>64</td><td>100</td><td>4.052</td><td colspan="2">95.196</td><td>NA</td></tr></table>

In this setting, the observations of the dependent variables prior to the policy change (control) are used as a baseline to assess the impact on the same outcomes after the policy change (treated). The treatment effect is shown if the pattern of post-treatment outcomes differs from the pattern of pre-treatment outcomes. If a sufficiently large number of observations for the dependent variables are available, this setting would also be useful in identifying the timing of impacts (delayed or right after the policy change) as well as the permanence of the impacts (longterm impact or short-term impact) (Cook & Campbell, 1979; Gillings et al., 1981). This approach is even more suitable in our case, given that Fradkin et al. (2018) used a randomized experiment setting to study the instantaneous impact of policy change on sentiment and user ratings but did not study the potential long-term or delayed impacts of the policy change.

Furthermore, RDiT is capable of producing unbiased estimates because it compares reviewing behaviors in a relatively short window of time right after the policy change with reviewing behaviors in a short window of time right before the policy change. For our context, RDiT assumes that listings and reviewers do not change in a short window of time (or at least any changes are uncorrelated with the policy change). According to previous research (Cavusoglu et al., 2016; Glass, 1997; Lee & Lemieux, 2010), interrupted time series design (which includes RDiT) is a viable alternative to true experiments since it has many pre- and post-intervention observations (in our case, many listings/reviews), thus allowing it to distinguish true intervention effects from time trends or seasonality. Furthermore, Glass (1997) points out that this design has become the standard method of causal analysis in applied behavioral research.

We note that a similar research design has been used in Cavusoglu et al.’s (2016) examination of a platform-wide policy change regarding Facebook’s privacy policy.

The basic idea behind this research design is that subjects with the assignment variable just below the cutoff (i.e., those who did not receive the treatment) are good comparisons $^ { \mathrm { t o , } }$ and therefore serve as a valid counterfactual for, those just above the cutoff (i.e., those who did receive the treatment) (Lee & Lemieux, 2010). If indeed there is a discontinuous jump in the target variable at the cutoff point, given the reasoning above, the discontinuity can be attributed to the causal effect of the treatment. In our context, the assignment variable is a deterministic function of time, and every Airbnb listing is treated precisely at the time of the policy change. Following the reasoning in RDiT, we compared guest reviews’ textual features around the policy change to see if this change had any causal effect. Our goal here was to compare the difference between the actual features of guest reviews after the policy change with the features of guest reviews had there been no policy change. Before running the RDD analysis, we first adjusted our target variables to account for the heterogeneity of the listings. This adjusting approach has been used in Cavusoglu et al. (2016) and Gottlieb et al. (2016). To adjust the target variable $( y _ { i t }$ , where i refers to listing i and t refers to month t), we first calculated the mean of the target variable $( \overline { { y _ { \imath } ^ { p r e } } } )$ for each listing i for the duration of study prior to the policy change. Then we calculated the adjusted target variable $( y _ { i t } ^ { a d j } )$ using the following equation:

$$
y _ {i t} ^ {a d j} = y _ {i t} - \overline {{y _ {\iota} ^ {p r e}}}
$$

(Specification 3)

After adjusting the target variables, we needed to determine the specification for the RDiT model. In RDD studies there are two primary strategies for model specification: (1) parametric/global strategy, and (2) non-parametric strategy. We used both methods to study the impact of the policy change on guest reviews (Table 5 reports the results of the parametric specification and Table 6 reports the results of nonparametric specification).

For the parametric specification, we used the following regression with different slopes on left and right of the cutoff point:

$$
\begin{array}{l} y _ {i t} ^ {a d j} = \alpha + \beta \left(A f t e r _ {\text { Policy } _ {t}} \mid R e v i e w _ {\text { Count } _ {i t}}\right) + \sum_ {n = 1} ^ {p} \gamma_ {n} \text { Month } _ {t} ^ {n} \\ + \sum_ {n = 1} ^ {p} \delta_ {n} \text { Month } _ {t} ^ {n} \times (A f t e r _ {\text { Policy } _ {t}} | R e v i e w _ {-} \text { Count } _ {i t}) + \varepsilon_ {i t} \\ (\text { Specification   4 }) \end{array}
$$

where ?????????? $P o l i c y _ { t }$ is the binary variable that is equal to 1 if month t is after the policy change (July 1, 2014) and 0 otherwise. ???????????? ${ C o u n t } _ { i t }$ (number of reviews for listing i at time t) is the covariate. $\beta$ in Specification 4 is the coefficient of interest for us. A significant and positive $\beta$ indicates a positive jump in the target variable after the policy change, whereas a significant and negative $\beta$ indicates a decline in the target variable after the policy change. When $\beta$ is insignificant, the analysis suggests no effect on the target variable because of the policy change. In Specification $^ { 4 , }$ ?? is the order of the polynomial regression model. We used the Bayesian information criterion (BIC) to determine the best value for ??. We started with $p = 1$ and increased it until we determined the value of $p$ that resulted in the smallest value of BIC. We report the final values of $p$ for each target variable in Table 5.

Another important decision in RDiT regards the bandwidth (the number of months before and after the policy change to be included) in the regression. We limited our RDiT analysis to 24 months before and 24 months after the policy change. This means that we used monthly data from July 2012 through June 2016 for RDiT analysis. The data from July 2012 to June 2014 were generated before the policy change and the data from July 2014 to June 2016 were generated after the policy change. Although we included 24 months of data before the policy change and 24 months of data after the policy change in the RDiT analysis, we used the Imbens-Kalyanaraman method (Imbens & Kalyanaraman, 2009) to determine the optimal bandwidth for local regression in our RDiT analysis. For each RDiT model (each target variable), the Imbens-Kalyanaraman method selects the optimal bandwidth to be used in RDiT analysis (reported in Table

5). For instance, if the selected bandwidth was 15, we used guest reviews posted 15 months before and 15 months after the policy change. RDiT fits a linear $( \mathrm { i f } p =$ 1) or polynomial regression model $( \mathrm { i f } p > 1 )$ for the data before the policy change (cutoff point) and another linear or polynomial regression model for the data after the policy change (as noted earlier we allow different slopes for left and right of the cutoff point). Since we used two separate models to fit the left and the right side of the cutoff point, RDiT teased out the effect of potential seasonality in the data (Glass, 1997).

Before reporting the RDiT results, we visually inspected the impact of the policy change on guest reviews for each of our target variables for the full 48-month window in the study. To create the visualizations, we used the R package “rdrobust.” For the polynomial order for the approximations in the visualizations, we used the values reported in Table 5.

## 5.2 Data

The blue lines in Figure 2 represent the fitted regression model for before and after the cutoff point data. As mentioned before, we used the Imbens-Kalyanaraman approach to determine the optimal bandwidth for RDiT analysis. In the plots in Figure 2, the fitted blue lines are based on those bandwidths. That is, the fitted lines are created based on the months that the Imbens-Kalyanaraman method suggested for the analysis. According to these visualizations, the interruption in time series is visually observable for all target variables except for Negative\_Emotion.

After visually inspecting our data, we ran the RDiT models. Table 5 reports the results. Primarily, we were interested in the value and significance of the estimates for coefficient After\_Policy. The coefficient was significant and positive when the target variable was Semantic\_Diversity, Objectivity, or CV\_Sentiment. <sup>14</sup> This indicates that the policy change resulted in a positive increase in these target variables. That is, the policy change resulted in more diverse reviews in terms of semantic meaning, more objective reviews, and more diverse reviews in terms of review sentiment. On the other hand, the coefficient for After\_Policy was significant and negative when the target variable was Sentiment or Positive\_Emotion. This means that the policy change resulted in reviews that were less positive as compared to the reviews submitted prior to the policy change. The coefficient was not statistically significant for Negative\_Emotion, indicating that the reduction in positive emotions explains the decrease in guest review sentiment.

![](/api/attachments/DCCYV7F8/fulltext/images/324feaf148ddbde96ca9039aae5523e3375d3689f8c3470d838631c324162cdd.jpg)

![](/api/attachments/DCCYV7F8/fulltext/images/d24ee90080e82e6566abcbd33e57d80349820cfa942e68969661a15da0e1134b.jpg)

![](/api/attachments/DCCYV7F8/fulltext/images/d7b8d77508f77c0de64594c87dfd3e9d75dc86f4b3ac044b7f3bb9d120258447.jpg)

![](/api/attachments/DCCYV7F8/fulltext/images/f3cd6d9af436e7cb4a4c9df0416e6eb6e863a9ac73ab56320ff50f8536596d20.jpg)

![](/api/attachments/DCCYV7F8/fulltext/images/761f68b04cec8029c51758ca98db5cfbfd70990d3247738b14cec64087c4a5e3.jpg)

![](/api/attachments/DCCYV7F8/fulltext/images/c7d3c488a7cb30950486e78602e9cb214a7e0dbd1ce970fa61824ac2cd948bb8.jpg)  
Figure 2. Regression Discontinuity in Time (RDiT) Plots Based on Monthly Data

Table 5. The Results of Parametric RDiT Specification

<table><tr><td></td><td>Semantic_Diversity</td><td>Objectivity</td><td>Sentiment</td><td>CV_Sentiment</td><td>Negative_Emotion</td><td>Positive_Emotion</td></tr><tr><td>After_Policy</td><td>0.003** (&lt;0.001)</td><td>0.015*** (0.002)</td><td>-0.010*** (0.001)</td><td>0.001* (&lt;0.001)</td><td>0.001 (&lt;0.001)</td><td>-0.005*** (0.001)</td></tr><tr><td>Month</td><td>0.002*** (0.001)</td><td>&lt;0.001 (&lt;0.001)</td><td>&lt;0.001* (&lt;0.001)</td><td>&lt;0.001 (&lt;0.001)</td><td>&lt;0.001 (&lt;0.001)</td><td>&lt;0.001* (&lt;0.001)</td></tr><tr><td> $Month^2$ </td><td>0.001*** (&lt;0.001)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Month^3$ </td><td>0.001*** (&lt;0.001)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Month × After_Policy</td><td>-0.004*** (&lt;0.001)</td><td>&lt;0.001** (&lt;0.001)</td><td>&lt;0.001 (&lt;0.001)</td><td>&lt;0.001 (&lt;0.001)</td><td>&lt;0.001 (&lt;0.001)</td><td>&lt;0.001** (&lt;0.001)</td></tr><tr><td> $Month^2 \times After_Policy$ </td><td>0.001*** (&lt;0.001)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Month^3 \times After_Policy$ </td><td>0.001*** (&lt;0.001)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>F-stat [p-value]</td><td>48.561 [&lt;0.001]</td><td>26.340 [&lt;0.001]</td><td>90.880 [&lt;0.001]</td><td>17.397 [&lt;0.001]</td><td>1.570 [0.194]</td><td>32.950 [&lt;0.001]</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.076</td><td>0.036</td><td>0.128</td><td>0.011</td><td>&lt;0.001</td><td>0.045</td></tr><tr><td>Polynomial order (p)</td><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Bandwidth (time window)</td><td>21</td><td>22</td><td>19</td><td>17</td><td>19</td><td>23</td></tr><tr><td colspan="7">Note: *significant at 0.05; **significant at 0.01; ***significant at 0.001</td></tr></table>

In the non-parametric specification, if $y ^ { a d j }$ denotes the target variable, ?? is the forcing variable (time in RDiT), with ??̅ being the threshold above which there is treatment (e.g., month 25), we can define the limiting values of the target variable as follows:

$$
y _ {+} ^ {a d j} = \lim _ {\lambda \rightarrow 0} \mathbb {E} [ y ^ {a d j} | t = \bar {t} + \lambda ], \quad (\text { Specification   5 })
$$

$$
y _ {-} ^ {a d j} = \lim _ {\lambda \rightarrow 0} \mathbb {E} [ y ^ {a d j} | t = \bar {t} - \lambda ] \quad (\text { Specification   6 })
$$

Then, the local average treatment effect is given by

$$
d = y _ {+} ^ {a d j} - y _ {-} ^ {a d j}.\tag{Specification 7}
$$

To implement the non-parametric RDiT, we found these limiting values nonparametrically using a local linear regression (Narayanan & Kalyanam, 2015) within a prespecified bandwidth ?? of the threshold ?? and then assessing the sensitivity of the bandwidth. As noted before, we use the Imbens-Kalyanaraman method to determine the optimal bandwidth for local regression. Table 6 reports the results for the nonparametric RDiT analysis. The results from this analysis are consistent with the results from the parametric RDiT analysis.

Based on our analysis using the RDiT method, we observe that the policy change made the reviews more diverse in terms of semantic meaning and sentiment, more objective, and less positive. Thus, H1a, H1b, H2a, and H2b are all supported.

## 5.2.1 RDiT Robustness Check

One way to test whether our results are robust is to randomly simulate the time of the policy change in the RDiT models and test whether the same results are returned. For instance, instead of using the actual time of policy change (July 2014), we ran RDiT models assuming that the policy changed in February 2015. Then we obtained RDiT coefficients based on a hypothetical policy change in February 2015. If the coefficients we obtained using these hypothetical time stamps were similar to the coefficients we obtained using the actual time of policy change, then this indicates that our results may not have been caused by the actual policy change. But if the coefficients we obtained using hypothetical time stamps were different from the coefficients we obtained from the actual time stamp of the policy change, this analysis would support our main findings. In other words, the assumption is that the treatment effect only occurred at the cutoff point (July 2014 in our study) and not at any other time. Hence, the sensitivity analysis would ideally show that the coefficients for placebo cutoff points are insignificant. This would indicate that the treatment effects are only present when using the real cutoff point and would disappear if we changed the cutoff. To test this assumption, we performed placebo tests by reestimating the treatment effects for different cutoff points. In the original data, the cutoff point in RDiT was Month 25 (during which the policy changed). To perform the sensitivity analysis, for every target variable in our data, we let the cutoff point in RDiT be equal to Month 7, Month 13, Month 19, Month 31 (we skipped Month 25, as it was the actual cutoff point), Month 37, and Month 43. Figure 3 visualizes the coefficients and the 95% confidence intervals for each of the target variables in our study. We also display the results for both parametric and non-parametric sensitivity analysis. Furthermore, we present the results on the sensitivity of the results based on the polynomial order (p) in parametric RDiT and based on different bandwidths for the non-parametric RDiT model.

In Figure 3 plots, the horizontal axis represents the cutoff point (month) and the vertical axis displays the estimate and the confidence interval for the treatment effect (i.e., β). For instance, in Figure 3(a), the estimated coefficient for the real cutoff point (Month 25) for Semantic\_Diversity is near 0.004, which is close to the coefficient reported in Table 5 and Table 6. According to this plot, except for the actual cutoff point, all the other cutoff points (placebo) resulted in insignificant coefficients (the confidence intervals overlap with zero). This observation indicates that the effect that we observe on the actual cutoff point (Month 25) is not based on some random phenomenon. Rather, the effect can only be observed exactly when Airbnb changed the review policy. Overall, the robustness test results further support our main RDiT analysis.

## 5.3 Short-Term vs. Long-Term Effects

In this section, we study whether the impact of the policy change on guest reviews is short-lived or longterm. For this purpose, we use a fixed-effect panel data analysis (Specification 8) to estimate the effect of policy change on Airbnb reviews. To study the shortterm impact, we only included reviews posted six months before and six months after the date of the policy change. For the long-term study, we included reviews posted within two years before and two years after the date of the policy change.

$$
\begin{array}{r l} & y _ {i t} ^ {a d j} = \beta_ {1} A f t e r _ {P o l i c y _ {i t}} + \beta_ {2} R e v i e w _ {C o u n t _ {i t}} \\ & + \alpha Z _ {i} + \theta T _ {t} + u _ {i t} \qquad \qquad \qquad \qquad \qquad \text {(Specification 8)} \end{array}
$$

In Specification 8, ???????????? $\_ C o u n t _ { i t }$ is the count of reviews posted by guests for listing i at time $t , Z _ { i }$ is listing i’s fixed effects, $T _ { t }$ is the time-fixed effects and ${ { u } _ { i t } }$ is the error term. In this specification, $\beta _ { 1 }$ captures the impact of the policy change on the target variables while $\beta _ { 2 }$ controls for the potential impact of the number of reviews.

Table 6. The Results of Non-parametric RDiT Specification

<table><tr><td></td><td>Semantic_Diversity</td><td>Objectivity</td><td>Sentiment</td><td>CV_Sentiment</td><td>Negative_Emotion</td><td>Positive_Emotion</td></tr><tr><td>After_Policy</td><td>0.004*** (&lt;0.001)</td><td>0.015*** (0.002)</td><td>-0.012*** (0.001)</td><td>0.003** (&lt;0.001)</td><td>0.001 (0.001)</td><td>-0.005*** (0.001)</td></tr><tr><td>Bandwidth (time window)</td><td>21</td><td>22</td><td>19</td><td>17</td><td>19</td><td>23</td></tr><tr><td colspan="7">Note: *significant at 0.05; **significant at 0.01; ***significant at 0.001</td></tr></table>

![](/api/attachments/DCCYV7F8/fulltext/images/db78626ac1b69785fdae0b52ad1e7680864d0d6998aafbe14c4c1d6366ae6232.jpg)  
(a) Semantic\_Diversity

![](/api/attachments/DCCYV7F8/fulltext/images/758594d57f23311cff2359663dc015759a30a69b29aaade944cdc7c3e2124b7a.jpg)  
(b) Objectivity

![](/api/attachments/DCCYV7F8/fulltext/images/dd0a26d3803aa861afd627353a5e535157ebfda7bff6468ac83dffdccc8ef002.jpg)  
(c) Sentiment \*

![](/api/attachments/DCCYV7F8/fulltext/images/c6ac5ec59f3b3eea32b7d73945c4fbfe8b44ad02f96d06d8d090dba0bd85651c.jpg)  
(d) CV\_Sentiment

![](/api/attachments/DCCYV7F8/fulltext/images/c4ea2ada9b2e84ca6b1990ee7dd03eaffb1acd8ee78b451c06b851bc3893989a.jpg)  
(e) Negative\_Emotion

![](/api/attachments/DCCYV7F8/fulltext/images/fbf64be82ddb0b063b7652092bb8ea4e2978512b464d7d69660e8638d5e9ef2a.jpg)  
(f) Positive\_Emotion  
\* The coefficients for cutoff point at month 37 are significant. To examine if our main results reported in Table 5 and Table 6 are not influenced by observations from this period (month 37 and beyond), we replicated our analysis by reducing the bandwidth to 11 months (so that we exclude data generated after month 36) for Sentiment. Our results reported in Table 5 and Table 6 did not change with respect to sign and significance of the coefficients.  
Figure 3. The Results of the Placebo Tests with Hypothetical Cutoff Points

Table 7. The Results of Fixed Effects Regression Analysis (Short-Term)

<table><tr><td></td><td>Semantic_Diversity</td><td>Objectivity</td><td>Sentiment</td><td>CV_Sentiment</td><td>Negative_Emotion</td><td>Positive_Emotion</td></tr><tr><td>After_Policy</td><td>0.004***(&lt;0.001)</td><td>0.016***(0.001)</td><td>-0.012***(0.001)</td><td>0.001***(&lt;0.001)</td><td>&lt;0.001(&lt;0.001)</td><td>-0.006***(0.001)</td></tr><tr><td>Robust</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>F-stat[p-value]</td><td>153.495[&lt;0.001]</td><td>47.390[&lt;0.001]</td><td>68.784[&lt;0.001]</td><td>47.058[&lt;0.001]</td><td>2.011[0.156]</td><td>30.872[&lt;0.001]</td></tr></table>

Note: We employed Eicker-Huber-White robust standard errors (reported in parentheses). \*significant at 0.05; \*\*significant at 0.01; \*\*\*significant at 0.001

Table 8. The Results of Fixed Effects Regression Analysis (Long-term)

<table><tr><td></td><td>Semantic_Diversity</td><td>Objectivity</td><td>Sentiment</td><td>CV_Sentiment</td><td>Negative_Emotion</td><td>Positive_Emotion</td></tr><tr><td>After_Policy</td><td>0.003***(&lt;0.001)</td><td>0.011***(0.002)</td><td>-0.015***(0.001)</td><td>0.001***(&lt;0.001)</td><td>&lt;0.001(&lt;0.001)</td><td>-0.005***(0.001)</td></tr><tr><td>Robust</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>F-stat[p-value]</td><td>226.834[&lt;0.001]</td><td>66.365[&lt;0.001]</td><td>346.278[&lt;0.001]</td><td>22.201[&lt;0.001]</td><td>0.212[0.645]</td><td>66.028[&lt;0.001]</td></tr><tr><td colspan="7">Note: We employed Eicker-Huber-White robust standard errors (reported in parentheses). *significant at 0.05; **significant at 0.01; ***significant at 0.001</td></tr></table>

Table 9. The Results of RDiT Analysis for Subgroups

<table><tr><td></td><td>Semantic_Diversity</td><td>Objectivity</td><td>Sentiment</td><td>CV_Sentiment</td><td>Negative_Emotion</td><td>Positive_Emotion</td></tr><tr><td>High quality (parametric)</td><td>0.002*** (&lt;0.001)</td><td>0.013** (0.004)</td><td>-0.002 (0.003)</td><td>&lt;0.001** (&lt;0.001)</td><td>0.001 (&lt;0.001)</td><td>&lt;0.001 (&lt;0.001)</td></tr><tr><td>High quality (non-parametric)</td><td>0.002*** (&lt;0.001)</td><td>0.012** (0.004)</td><td>-0.002 (0.003)</td><td>&lt;0.001*** (&lt;0.001)</td><td>0.001 (&lt;0.001)</td><td>&lt;0.001 (&lt;0.001)</td></tr><tr><td>Low quality (parametric)</td><td>0.004*** (0.001)</td><td>0.016* (0.006)</td><td>-0.018*** (0.003)</td><td>0.001** (&lt;0.001)</td><td>&lt;0.001 (&lt;0.001)</td><td>-0.012*** (0.003)</td></tr><tr><td>Low quality (non-parametric)</td><td>0.004*** (0.001)</td><td>0.018** (0.006)</td><td>-0.016*** (0.004)</td><td>0.001*** (&lt;0.001)</td><td>&lt;0.001 (&lt;0.001)</td><td>-0.011*** (0.003)</td></tr><tr><td>Polynomial order (p)</td><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Bandwidth (time window)</td><td>21</td><td>22</td><td>19</td><td>17</td><td>19</td><td>23</td></tr><tr><td colspan="7">Note: Standard errors are reported in parentheses. *Significant at 0.05: **Significant at 0.01: ***Significant at 0.001</td></tr></table>

Note: Standard errors are reported in parentheses. \*Significant at 0.05; \*\*Significant at 0.01; \*\*\*Significant at 0.001.

Table 7 reports the results of the short-term analysis. The sign and significance of the estimate for coefficient After\_Policy is identical to those reported in RDiT results, thus supporting the presence of the short-term effects. Basically, this coefficient is significant and positive when the target variable is Semantic\_Diversity, Objectivity, or CV\_Sentiment, and significant and negative for Sentiment and Positive\_Emotion. These findings confirm our previous results obtained by RDiT analysis. Table 8 reports the results for the long-term effects (two years before and two years after the policy change). The results continue to align with our previous results.

## 5.4 The Role of the Listing’s Quality

To examine whether the policy change impacted highquality and low-quality listings differently, we performed RDiT analysis using subgroups of listings. We created two subgroups based on the overall rating score of the listings:

Group 1—high\_quality listings: Listings with an overall review rating score above the third quartile of the data.

Group 2—low\_quality listings: Listings with an overall review rating score below the first quartile of the data.

We ran both parametric and non-parametric RDiT for each group. Table 9 reports the results of our analysis. According to Table 9, Semantic\_Diversity increased for both high-quality and low\_quality listings. However, the size of the coefficient was bigger for low\_quality listings than high\_quality listings. That is, in both parametric and non-parametric models, the coefficients for the low\_quality listing subgroup were equal to 0.004, while they were equal to 0.002 for the high\_quality subgroup. This indicates that, with respect to Semantic\_Diversity, low\_quality listings were more impacted by the policy change. With respect to Objectivity, again low\_quality listings had a larger coefficient, indicating that these listings were more strongly impacted by the policy change than were high\_quality listings. Our results regarding Sentiment and Positive\_Emotion are consistent; although high\_quality listings were not impacted by the policy change, low\_quality listings were impacted significantly (decreases in sentiment and Positive\_Emotion). The policy change did not have any significant impact on Negative\_Emotion for either low\_quality or high\_quality listings.

According to our results, listings with higher review ratings were less impacted by the policy change (in support of H3). For lesser quality listings with lower ratings, the impacts may be greater. Intuitively, lowquality listings would have more flaws that could be freely discussed by guests in the simultaneous system.

## 6 Discussion and Conclusion

Building a reliable reputation system among stakeholders is crucial for the sharing economy to create and sustain its collaborative ecosystem. Therefore, sharing economy platforms need to continuously explore mechanisms driving more accurate and informative reviews within their user communities. One common challenge faced by many sharing platforms is inflated user reviews, where reviews tend to be skewed toward overly favorable assessments. This skewness and lack of diversity in the reviews is indeed more troublesome on sharing economy platforms because they rely on reputational data to function properly. The lack of variation in reviews makes it consequently difficult for users to differentiate and select among products/services.

Scholars have proposed the simultaneous review system as a way to manage reciprocity, mitigate bias, and produce more reliable and diverse reputation signals (Bolton et al., 2013). A simultaneous review system was implemented by Airbnb on July 10, 2014, as a remedy for retaliation fears, induced reciprocity, and discomfort in posting reviews (Montini, 2014). This policy change offered a unique opportunity to empirically examine the extent to which a newly introduced simultaneous review system resulted in more diverse reviews on both semantic and emotional levels. Our analyses and results suggest that immediately after the new policy implementation, the reviews became more diverse in terms of semantic meaning and sentiment scores, more objective, and less positive. Such reviews can better help consumers to make purchasing decisions since they provide more heterogeneous content and greater diversity in opinion. Therefore, we provide strong empirical evidence that Airbnb’s new policy does encourage more informative reviews and, to some extent, mitigates overinflated reviews.

While many of our results are consistent with prior findings, we also offer several novel insights into the simultaneous review system and its impact on textual review features. First, by analyzing a comprehensive list of textual features over an extended time period, our research reveals how review simultaneity affects two types of signals (informational content and personal opinions) embedded in user reviews. We apply novel cutting-edge text mining techniques to extract the semantic meaning of user comments, which more accurately reflects the breadth of reviews informational content. Immediately after the policy change, informational content increased and personal opinions became less positive yet more diverse. More importantly, such changes persist over time. By reducing reciprocity opportunities, people enjoy more freedom to provide recommendations.

Second, our in-depth analyses demonstrate how the simultaneous review system reduces overall sentiment. While some literature suggests that negative reviews tend to be suppressed (Askay, 2015; Bolton et al., 2013), we found that negative sentiments remained the same while positive sentiments were deflated in the simultaneous review system. This indicates that the change in sentiment is most likely caused by less frequent use of positive words rather than more frequent use of negative words in the reviews. That is, after the policy change, guests did not use more negative words such as “bad” or “terrible”; rather, they decreased their use of positive words such as “good” or “great.” If customers are truly dissatisfied and choose to provide feedback, they are likely to lash out with negative comments regardless of potential retaliation from the other party. If customers are neutral or positive, they may act strategically in the asynchronous review system to take advantage of the norm of reciprocity. They may say something overly positive in anticipation of or to encourage the other party to do the same. Such positive reciprocity is no longer helpful in the simultaneous review system, as the parties write reviews knowing that the other party is not aware of the content of their review when they write their own review. In addition, we adopted dispersion measures to quantify sentiment changes and demonstrate that sentiment becomes more diverse in the simultaneous review system.

Third, we explore how the impacts of the policy change varied based on product quality. In general, we found that high-quality properties were less affected by the change in the review policy. Given that such listings are genuinely good and are likely to get positive reviews regardless of the simultaneity of the review system, it is not surprising that the changes in the review policy did not significantly impact highquality listings.

From a theoretical perspective, our research extends the literature on fear of retaliation in online reviews. Prior research has shown that the simultaneous review system can mitigate the fear of retaliation. These studies (Bolton et al., 2013; Fradkin et al., 2018) provide evidence that the mitigation of retaliation fears results in reviews with lower sentiment scores or reviews with lower user ratings. Our research, extending these findings, suggests that the mitigation of retaliation fears through a simultaneous review system not only results in reviews with lower sentiment scores (already known from previous studies), but also reviews that are more diverse in terms of informational content (H1a and H1b) and personal opinions (H2a and H2b). Furthermore, our study suggests that the impacts of a simultaneous review system on informational content and personal opinions cascaded in user reviews are moderated by the quality of the product/service. That is, higher quality products/services (in our case listings) are less impacted by changes in the review system (H3). The three sets of hypotheses that we propose and test provide new insights into the consequences of enforcing a simultaneous review system. Using observational data collected over an extended period of time, our research is some the first to demonstrate that changes associated with review simultaneity are sustainable over time.

From a practitioner’s perspective, our results reveal promising consequences for enforcing a simultaneous review system. As explained above, our findings suggest that simultaneous review systems result in more diverse reviews both in terms of informational content as well as personal opinions. Given that sharing economy platforms such as Airbnb operate based on reputational information, such review diversity may strengthen the usefulness of the reputational platform data. Review diversity can help future users (e.g., guests) learn more about the product/service (e.g., listing). Such additional information may result in a better match between the consumer and the product/service. Better matching, in turn, may result in higher levels of satisfaction with the product/service and the platform, and therefore a higher likelihood of repeated use. Hence, simultaneous review systems may result in the expanded use of sharing economy platforms because of more satisfied customers. Practitioners may also be interested in our third hypothesis, which indicates that the simultaneous review system has less impact on high-quality products/services. This finding should motivate practitioners to try a simultaneous review system without worrying about unintended consequences for genuinely high-quality products/services.

## 7 Limitations

We acknowledge that there are certain limitations of our study. Because of data limitations, we only observed and analyzed public comments provided by Airbnb guests. We do not know how the review policy changes may have affected review response rates or users’ willingness to provide reviews in long term. Prior literature shows conflicting results related to reviewers’ response rates, which have been shown to decrease in the context of a controlled lab experiment (Bolton et al., 2013) but increase in a one-month field experiment (Fradkin et al., 2018). Future research could work with sharing economy platforms to obtain booking information to investigate other aspects of user behavior associated with review policy changes. Since our data set only includes reviews posted by guests, it would also be interesting to collect additional information about hosts’ reviews to examine potential host behavior changes associated with the review policy change. Although we believe that RDiT approach was the right choice of methodology for our study, other study designs based on controlled or natural experimental settings could be explored. For instance, the difference-in-difference method could be deployed if a policy change were enforced over time with some listings being impacted before other listings. Our selected samples are all located in US cities. It would be interesting to extend our research into international cities, which could help generalize our results to other cultural settings.

Despite the aforementioned limitations, our study makes unique contributions to and extends the understanding of online user reviews generated on sharing economy platforms. We provide useful insights into the benefits and nuances of simultaneous review systems and their effects for managing reciprocity. We show that the impact of this simultaneous review system on user reviews is prolonged (as opposed to temporary). We further show that this simultaneous review system resulted in more diverse user reviews, both in terms of semantic meaning and sentiment.

## References

Abbasi, A., Zhou, Y., Deng, S., & Zhang, P. (2014). Text analytics to support sense-making in social media: A language-action perspective. MIS Quarterly, 42(2), 427-464.

Abrahao, B., Parigi, P., Gupta, A., & Cook, K. S. (2017). Reputation offsets trust judgements based on social biases among Airbnb users. Proceedings of the National Academy of Sciences of the United States of America, 114(37), 9848-9853.

Aggarwal, C., & Zhai, C. (2012). Mining text data, Springer.

Aggarwal, R., & Singh, H. (2013). Differential influence of blogs across different stages of decision making: The case of venture capitalists. MIS Quarterly, 37(4), 1093-1112.

Alyakoob, M. and Rahman, M.S. (2019). Shared prosperity (or lack thereof) in the sharing economy. Available at https://papers.ssrn.com/ sol3/papers.cfm?abstract\_id=3180278

Askay, D. A. (2015). Silence in the crowd: The spiral of silence contributing to the positive bias of opinions in an online review system. New Media and Society, 17(11), 1811-1829.

Bhappu, A., & Schultze, U. (2018). Implementing an organization-sponsored sharing platform to build employee engagement. MIS Quarterly Executive, 17(2), 112-121.

Bivens, J. (2019). The economic costs and benefits of Airbnb, Economic Policy Instrucute Report, https://www.epi.org/publication/the-economiccosts-and-benefits-of-airbnb-no-reason-forlocal-policymakers-to-let-airbnb-bypass-taxor-regulatory-obligations/

Bolton, G., Greiner, B., & Ockenfels, A. (2013). Engineering trust: Reciprocity in the production of reputation information. Management Science, 59(2), 265-285.

Burtch, G., Hong, Y., Bapna, R., & Griskevicius, V. (2018). Stimulating online reviews by combining financial incentives and social norm. Management Science, 64(5), 2065-2082.

Cao, Q., Thompson, M. A., & Yu, Y. (2013). Sentiment analysis in decision sciences research: An illustration to IT governance. Decision Support Systems, 54(2), 1010-1015.

Cavusoglu, H., Phan, T. Q., Cavusoglu, H., & Airoldi, E. M. (2016). Assessing the impact of granular privacy controls on content sharing and disclosure on Facebook. Information Systems Research, 27(4), 848-879.

Chen, P. Y., Hong, Y., & Liu, Y. (2018). The value of multi-dimensional rating systems: Evidence from a natural experiment and lab experiments. Management Science, 64(10), 4471-4965.

Chen, W., Wei, Z., and Xie, K. (2019). The battle for homes: how does home sharing disrupt local residential markets. Available at https://papers.ssrn.com/sol3/papers.cfm?abstra ct\_id=3257521

Cheng, M. (2016). Sharing economy: A review and agenda for future research, International Journal of Hospitality Management, 57, pp. 60- 70.

Cook, T. D., & Campbell, D. T. (1979). Quasiexperimentation: Design & analysis issues for field settings. Houghton Mifflin.

Das, S. R., & Chen, M. Y. (2007). Yahoo! for Amazon: Sentiment extraction from small talk on the web. Management Science, 53(9), 1375-1388.

de Sousa, R. (2004). Twelve varieties of subjectivity: Dividing in hopes of conquest. In J. M. Larrazabal & L. A. Pérez Miranda (Eds.), Language, knowledge, and representation: Proceedings of the 6th International Colloquium on Cognitive Science (ICCS-99) (pp. 147-164) Springer.

Dellarocas, C. (2006). Strategic manipulation of internet opinion forums: Implications for consumers and firms. Management Science, 52(10), 1577-1593.

Dellarocas, C., & Wood, C. A. (2008). The sound of silence in online feedback: Estimating trading risks in the presence of reporting bias. Management Science, 54(3), 460-476.

Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of deep bidirectional transformers for language understanding. Available at http://arxiv.org/abs/1810.04805

Droesch, B. (2020). US sharing economy 2020. eMarketer. https://www.emarketer.com/content/ us-sharing-economy-2020

Fradkin, A., Grewal, E., & Holtz, D. (2018). The determinants of online review informativeness: Evidence from field experiments on Airbnb. Available at https://www.semanticscholar.org/ paper/The-Determinants-of-Online-Review-Informativeness%3A-Fradkin-Grewal/b543dc1d2e233c61dffb16dc8c9a9d57f b4b2ad1

Fradkin, A., Grewal, E., Holtz, D., & Pearson, M. (2015). Bias and reciprocity in online reviews: evidence from field experiments on Airbnb.

Proceedings of the 16th ACM Conference on Economics and Computation.

Ghose, A., & Ipeirotis, P. G. (2011). Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions on Knowledge and Data Engineering, 23(10), 1498-1512.

Ghose, A., Ipeirotis, P. G., & Li, B. (2012). Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Marketing Science, 31(3), 493-520.

Ghose, A., & Yao, Y. (2011). Using transaction prices to re-examine price dispersion in electronic markets. Information Systems Research, 22(2), 269-288.

Gillings, D., Makuc, D., & Siegel, E. (1981). Analysis of interrupted time series mortality trends: An example to evaluate regionalized perinatal care. American Journal of Public Health, 71(1), 38- 46.

Glass, G. V. (1997). Interrupted time-series quasiexperiments. In R. M. Jaeger (Ed.), Complementary methods for research in education (2nd ed., pp. 589-609). American Educational Research Association.

Godes, D. and Silva, J.C. (2012). Sequential and temporal dyanmics of online opinion, Marketing Science, 31(3), 448-473.

Goes, P. B., Lin, M., & Au Yeung, C. (2014). “Popularity effect” in user-generated content: evidence from online product reviews. Information Systems Research, 25(2), 222-238.

Goh, K.-Y., Heng, C.-S., & Lin, Z. (2013). Social media brand community and consumer behavior: Quantifying the relative impact of user- and marketer-generated content. Information Systems Research, 24(1), 88-107.

Gottlieb, J., Townsend, R., & Xu, T. (2016). Experimenting with entrepreneurship: The effect of job-protected leave [NBER Working Paper]. https://www.nber.org/system/files/ working\_papers/w22446/w22446.pdf

Gu, B., Konana, P., Rajagopalan, B., & Chen, H.-W. M. (2007). Competition among virtual communities and user valuation: The case of investing-related communities. Information Systems Research, 18(1), 68-85.

Güth, W., Mengel, F., and Ockenfels, A. (2007). An evolutionary analysis of buyer insurance and seller reputation in online markets, Theory and Decision, 63(3), 265-282.

Hong, Y., Huang, N., Burtch, G., & Li, C. (2016). Culture, conformity and emotional suppression in online reviews. Journal of the Association for Information Systems, 17(11), 308-329.

Hu, N., Zhang, J., & Pavlou, P. A. (2009). Overcoming the J-shaped distribution of product reviews. Communications of the ACM, 52(10), 144-147.

Huang, N., Hong, Y., & Burtch, G. (2017). Social network integration and user content generation: Evidence from natural experiments. MIS Quarterly, 41(4), 1035-1058.

Huurne, M., Ronteltap, A., Corten, R., and Buskens, V. (2018). Antecedents of trust in the sharing economy: A systematic review, Journal of Consumer Behavior, 16(6), 485-498

Imbens, G., & Kalyanaraman, K. (2009). Optimal bandwidth choice for the regression discontinuity estimator [NBER Working Paper]. https://www.nber.org/system/files/working\_pa pers/w14726/w14726.pdf

Inselberg, A. (2009). Parallel Coordinates. In Ling Liu & M. Tamer Özsu (Eds.), Encyclopedia of Database Systems (pp. 2018-2024). Springer.

Islam, A., & Inkpen, D. (2008). Semantic text similarity using corpus-based word similarity and string similarity. ACM Transactions on Knowledge Discovery from Data, 2(2), 1-25.

Kehrwald, B. (2010). Being online: Social presence as subjectivity in online learning, London Review of Education, 8(1), 39-50.

Larsen, K. R. T., & Bong, C. H. (2016). A tool for addressing construct identity in literature reviews and meta-analyses. MIS Quarterly, 40(3), 529-551.

Lau, R. Y. K., Liao, S. S. Y., Wong, K. F., & Chiu, D. K. W. (2012). Web 2.0 environmental scanning and adaptive decision support for business mergers and acquisitions. MIS Quarterly, 36(2), 1239-1268.

Lee, D., & Lemieux, T. (2010). Regression discontinuity designs in economics. Journal of Economic Literature, 48(2), 281-355.

Lee, J., & Lee, J. N. (2009). Understanding the product information inference process in electronic word-of-mouth: An objectivity-subjectivity dichotomy perspective. Information & Management, 46(5), 302-311.

Lees, N. (2020). The sharing economy will have to change. The Economist. https://www. economist.com/business/2020/06/04/thesharing-economy-will-have-to-change

Li, W., Chen, H., & Nunamaker, J. F. (2017). Identifying and profiling key sellers in cyber carding community: AZSecure text mining system. Journal of Management Information Systems, 33(4), 1059-1086.

Li, X., & Hitt, L. M. (2008). Self-selection and information role of online product reviews. Information Systems Research, 19(4), 456-474.

Lin, Z., Zhang, Y., and Tan, Y. (2019). An empirical study of free product sampling and rating bias. Information Systems Research, 30(1), 260-275.

Liu, B. (2012). Sentiment analysis and opinion mining. Synthesis Lectures on Human Language Technologies, 5(1), 1-167.

Livan, G., Caccioli, F., & Aste, T. (2017). Excess reciprocity distorts reputation in online social networks. Scientific Reports, 7, Article 3551.

Loria, S. (2017). TextBlob documentation. TextBlob. https://textblob.readthedocs.io/en/dev/.

Lu, Y., Tsaparas, P., Ntoulas, A., and Polanyi, L. (2010). Exploiting social context for review quality prediction. Proceedings of the 19th International Conference on World Wide Web (pp. 691-791).

Luo, X., Gu, B., Zhang, J., & Phang, C.-W. (2017). Expert Blogs and general consumer perceptions of competing brands. MIS Quarterly, 41(2), 371-395.

Malmendier, U., Velde, V. L., & Weber, R. A. (2014). Rethinking reciprocity. Annual Review of Economics, 6, 849-874.

Mayzlin, D., Dover, Y., & Chevalier, J. (2014). Promotional reviews: An empirical investigation of online review manipulation. American Economic Review, 104(8), 2421- 2455.

Mesmer-Magnus, J. R., & Viswesvaran, C. (2005). Whistleblowing in organizations: An examination of correlates of whistleblowing intentions, actions, and retaliation. Journal of Business Ethics, 62(3), 277-297.

Mihalcea, R., Corley, C., & Strapparava, C. (2006). Corpus-based and knowledge-based measures of text semantic similarity. Proceedings of the National Conference on Artificial Intelligence.

Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). Distributed representations of words and phrases and their compositionality. Advances in Neural Information Processing Systems, 2, 3111-3119.

Montini, L. (2014). How Airbnb Solved the Bizarre Problem of Too Many Positive Reviews. Inc.

https://www.inc.com/laura-montini/thepsychology-of-a-positive-review-according-toairbnb.html

Montoyo, A., Martinez-Barco, P., and Balahur, A. (2012). Subjectivity and sentiment analysis: An overview of the current state of the area and envisaged developments, Decision Support Systems, 53(4), pp. 675-679.

Moreno, A., & Terwiesch, C. (2014). Doing business with strangers: reputation in online service marketplaces. Information Systems Research, 25(4), 865-886.

Muchnik, L., Aral, S., & Taylor, S. J. (2013). Social influence bias: A randomized experiment. Science, 341(6146), 647-651.

Mudambi, S. M., and Schuff, D. (2010). What makes a helpful online review? a study of customer reviews on Amazon.com, MIS Quarterly 34(1), 185-200.

Narayanan, S., & Kalyanam, K. (2015). Position effects in search advertising and their moderators: A regression discontinuity approach. Marketing Science, 34(3), 388-407.

Nayak, P. (2019). Understanding searches better than ever before. Google Blog. https://www.blog. google/products/search/search-languageunderstanding-bert/

Pang, B., & Lee, L. (2008). Opinion mining and sentiment analysis. Foundations and Trends in Information Retrieval, 2(1-2), 1-135.

Pennington, J., Socher, R., & Manning, C. (2014). Glove: Global vectors for word representation. Proceedings of the Conference on Empirical Methods in Natural Language Processing (pp. 1532-1543).

Piramuthu, S., Kapoor, G., Zhou, W., & Mauw, S. (2012). Input online review data and related bias in recommender systems. Decision Support Systems, 53(3), 418-424.

Preserpio, D., Xu, W., & Zervas, G. (2018). You get what you give: Theory and evidence of reciprocity in the sharing economy. Quantitative Marketing and Economics, 16, 371-407

Rajesh, N., & Gandy, L. (2016). CashTagNN: Using sentiment of tweets with CashTags to predict stock market prices. Proceedings of the 11th International Conference on Intelligent Systems: Theories and Applications.

Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. Association for Computational

Linguistics (ACL). Availabe http://arxiv.org/abs/1908.10084

Resnick, P., & Zeckhauser, R. (2002). Trust among Strangers in internet transactions: Empirical analysis of eBay’s reputation system. Advances in Applied Microeconomics, 11, 127-157.

Sahni, T., Chandak, C., Chedeti, N. R., & Singh, M. (2017). Efficient Twitter sentiment classification using subjective distant supervision. Proceedings of the 9th International Conference on Communication Systems and Networks (pp. 548-553).

Short, J., Williams, E., and Christie, B. (1976). The social psychology of telecommunications. Wiley.

Singh, A.S. and Tucker, C.S. (2017). A Machine learning approach to product review disambiguation based on function, form, and behavior classification, Decision Support Systems, 97, 81-91

Singh, P. V., Sahoo, N., & Mukhopadhyay, T. (2014). How to attract and retain readers in enterprise blogging? Information Systems Research, 25(1), 35-52.

Smith, A. (2016). Shared, collaborative and on demand: The new digital economy. Urbanism Next. https://www.urbanismnext.org/resources/ shared-collaborative-and-on-demand-the-newdigital-economy

Son, J., Negahban, A., and Chiang, D.T. (2019). Topic diversity of online consumer reviews and its effect on review helpfulness. Proceedings of the 25th Americas Conference on Information Systems.

Stieglitz, S., & Dang-Xuan, L. (2013). Emotions and information diffusion in social media: Sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29(4), 217-248.

Sun, M. (2012). How does the variance of product ratings matter? Management Science, 58(4), 696-707.

Sun, X., Han, M., and Feng, J. (2019). Helpfulness of online reviews: Examining review informativeness and classification thresholds by search products and experience products, Decision Support Systems, 124, Article 113099.

Sundararajan, A. (2016). The sharing economy: The end of employment and the rise of crowd-based capitalism. MIT Press.

Tenney, I., Das, D., & Pavlick, E. (2019). BERT rediscovers the classical NLP pipeline. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics.

Wang, J., Ghose, A., and Ipeirotis, P. G. (2012). Bonus, disclosure, and choice: what motivates the creation of high-quality paid reviews? Proceedings of 33rd International Conference on Information Systems.

Zervas, G., Proserpio, D., & Byers, J. (2015). A first look at online reputation on Airbnb, where every stay is above average. Available at https://papers.ssrn.com/sol3/papers.cfm?abstra ct\_id=2554500

Zhang, P., Lee, H.M., Zhao, K., and Shah, V. (2019). An empirical investigation of eWOM and used video game trading: The moderation effects of product features, Decision Support Systems, 123, Article 113076.

## Appendix

To obtain document embeddings from BERT, we first performed the routine text preprocessing steps. We removed non-English characters, stemmed all the words in the text, and then removed the stop-words such as “is,” “am,” and “the.” We created home-brew codes in Python programming language to perform these tasks. In addition to the routine text preprocessing steps, we needed to further process our text for BERT because our data set is a collection of guest reviews that contain many proper names (e.g., hosts’ names). Including proper names (e.g., John or Alex) would cause issues for our embeddings. To resolve this issue caused by proper names, we decided to identify and replace proper names with the word “hostx.” This ensured that each single proper name would be treated the same way anytime the guests mention proper names in their reviews. To implement this approach, we used an R package known as “gender.”<sup>15</sup> This package includes a comprehensive collection of proper names known as “genderdata.” This collection is based on resources such as “Social Security Administration’s baby names by year,” “IPUMS Census data,” and “North Atlantic Population Project.” We therefore created a home-brew R code to use this package to identify the proper names and then replace them with the word “hostx.” After cleaning the text data, we used “Sentence-BERT” (Reimers & Gurevych, 2019) to obtain the embeddings for each guest review.

To evaluate the quality of the embeddings, we decided to use those embeddings to cluster guest reviews. If the guest reviews within each cluster are related to each other yet different from guest reviews in the other clusters, this could indicate that the embeddings were useful in properly identifying the clusters. We first used the elbow method to determine the optimal number of clusters in guest reviews. According to the plot in Figure A1, we decided to use 10 as the number of clusters (k) in k-means.

Figure A2 visualizes the clusters of guest reviews using a two-dimensional space that we created using the first two principal components. According to Figure A2, the clusters seem to be unique even in two-dimensional space. To further study these clusters, we decided to create word clouds based on the most frequent words in each cluster. Figure A3 visualizes the word clouds. As observed in Figure A3, the most frequent word in each cluster is unique. This observation, along with the visualization in Figure A2, signals a good-quality clustering of the guest reviews based on the document embeddings from “Sentence-BERT.”

Elbow Method For Optimal k  
![](/api/attachments/DCCYV7F8/fulltext/images/f9a8ee42827066a6a98b6344f92960d68360ac91909b0da911da4bdcd98657ec.jpg)  
Figure A1. Finding the Optimal Value of K in K-Means Using the Elbow Method

![](/api/attachments/DCCYV7F8/fulltext/images/b37383516695bc05ffa8db8f3043c6e9761dda5600ada5d85c842dfbd5a8a2bc.jpg)  
Figure A2. Clusters of Guest Reviews Visualized in Two-Dimensional Space

<table><tr><td><img src="/api/attachments/DCCYV7F8/fulltext/images/756ebe4e3c4c59a2cea8be4630c5d5e45a09f8f5b2d9004e7a452948d193da17.jpg"/></td><td><img src="/api/attachments/DCCYV7F8/fulltext/images/cef35c8be9e5c413d2d30e5253b89e6d97040206686f23de2eca14e43812180f.jpg"/></td></tr><tr><td><img src="/api/attachments/DCCYV7F8/fulltext/images/89b2bc6fded9e4a3da3ab2c348ccfafeae5b3471d940d17bd11be2d4f3ad835b.jpg"/></td><td><img src="/api/attachments/DCCYV7F8/fulltext/images/6a4318bb6160cc0419f62234dff37bf82bd32c9bfe20fdeb3896c48d9789f286.jpg"/></td></tr><tr><td><img src="/api/attachments/DCCYV7F8/fulltext/images/482441f42ceaf4a71d2abd5eac8c0968e5cf80d6c0d7137148180cb0a93cd6ab.jpg"/></td><td><img src="/api/attachments/DCCYV7F8/fulltext/images/28ccf2dfa1543ad2ca3b87205f5020250eb4f796d6ffdff6e53aa97cf5edaf1e.jpg"/></td></tr><tr><td><img src="/api/attachments/DCCYV7F8/fulltext/images/783bc47895369105a5ad1a877c6513d1f9f5e69b784f843d28f40b8a593d0e55.jpg"/></td><td><img src="/api/attachments/DCCYV7F8/fulltext/images/2f34c7da5eeb04be93f5bd9f26f9a771584011da96ebc888e771f3523c7c82bb.jpg"/></td></tr><tr><td><img src="/api/attachments/DCCYV7F8/fulltext/images/ab47b0dc5d2096a3be707efd169c794d50d6220b431316ccbc0937545c86b20c.jpg"/></td><td><img src="/api/attachments/DCCYV7F8/fulltext/images/d2de1411c797a1b361c68a69d1f2bc5cf7443464645759d1eb7210a30cb19d5a.jpg"/></td></tr></table>

Figure A3. Word Clouds for Each Cluster of Guest Reviews

## About the Authors

Reza Mousavi is an assistant professor in the McIntire School of Commerce at the University of Virginia. His research interests include the societal impacts and economics of social media, artificial intelligence (AI) and business analytics, user-generated content, and healthcare information systems. Dr. Mousavi received his PhD in business administration from Arizona State University and his research has appeared in leading IS journals such as Information Systems Research and Journal of Management Information Systems.

Kexin Zhao is a professor of management information systems in the Belk College of Business at the University of North Carolina at Charlotte. Her current research focuses on electronic commerce, virtual communities, and business analytics. Dr. Zhao received her PhD from the University of Illinois at Urbana-Champaign. She is an associate editor at Decision Support Systems. Her papers have been published in several leading academic journals, including Information Systems Research, Journal of the Association for Information Systems, Journal of Management Information Systems, Journal of Retailing, Decision Sciences, and many others.

Copyright © 2022 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
