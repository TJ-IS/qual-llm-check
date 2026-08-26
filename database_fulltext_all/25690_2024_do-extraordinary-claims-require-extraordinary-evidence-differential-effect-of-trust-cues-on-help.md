---
otero_id: 25690
otero_key: "H2T92A7X"
title: "Do extraordinary claims require extraordinary evidence? Differential effect of trust cues on helpfulness by review extremity: an empirical study using big data"
authors: "Hoon S. Choi"
year: "2024"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2022.2104665"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Do extraordinary claims require extraordinary evidence? Differential effect of trust cues on helpfulness by review extremity: an empirical study using big data

Hoon S. Choi

To cite this article: Hoon S. Choi (2022): Do extraordinary claims require extraordinary evidence? Differential effect of trust cues on helpfulness by review extremity: an empirical study using big data, European Journal of Information Systems, DOI: 10.1080/0960085X.2022.2104665

To link to this article: https://doi.org/10.1080/0960085X.2022.2104665

![](/api/attachments/H2T92A7X/fulltext/images/a83f6de028d5f7172672018001115538448479aff9bd5f09e121d612436da9ae.jpg)

Published online: 03 Aug 2022.

![](/api/attachments/H2T92A7X/fulltext/images/245deb79bc3583e320ba38e483c4f6d07b01f42a6301e824f07bd1ad5aa92edf.jpg)

Submit your article to this journal

![](/api/attachments/H2T92A7X/fulltext/images/4be665c7ddfbc75f49638806ebb97f92265ac2fe093454afe317587a67a76048.jpg)

Article views: 147

![](/api/attachments/H2T92A7X/fulltext/images/1344fb07f32b18bd6412d8fbc001dfdb5348c4174f609d23bac7fdb87b6847a3.jpg)

View related articles

![](/api/attachments/H2T92A7X/fulltext/images/97c5d5ae326192eba51113ad8464650532cc648015448f1eec40f0464cfa7f69.jpg)

View Crossmark data

EMPIRICAL RESEARCH

Check for updates

# Do extraordinary claims require extraordinary evidence? Diferential efect of trust cues on helpfulness by review extremity: an empirical study using big data

Hoon S. Choi

Department of Computer Information Systems, Appalachian State University

## ABSTRACT

This study examines whether the efect of trust cues, such as verified purchase badges and user-provided photos, on review helpfulness difers by review extremity, on which Sagan’s standard and the theory of confirmation bias suggest contradictory predictions. Adopting large empirical data with approximately 31 million online reviews from Amazon.com, this study finds that the efect of trust cues on review helpfulness is significantly larger for moderate reviews, although the diference is negated for highly helpful reviews, and the efect is more considerable for extremely positive reviews than extremely negative reviews. The findings also disclose that the efect is more substantial for extreme reviews on search products and those on tangible products, suggesting that the diferential efect depends on product attributes.

ARTICLE HISTORY Received 12 January 2022 Accepted 13 July 2022

KEYWORDS Online reviews; eWOM; review helpfulness; confirmation bias; trust cues; search/experience products tangible/intangible products; Amazon.com; big data

## 1. Introduction

It has long been established that helpful online reviews, also known as electronic word of mouth (eWOM), play a vital role in promoting transactions on ecommerce platforms (Hong et al., 2017; Lee & Choeh, 2018), assisting consumers to conveniently evaluate the potential quality of products. The managerial importance of helpful reviews has attracted great attention from scholars in the ecommerce research domain, examining determinants of their helpfulness. One of the prevalently investigated factors in the studies is review extremity (Lee & Choeh, 2018; Siering et al., 2018), indicating either extremely positive or negative opinions. According to Schoenmueller et al. (2020), extreme reviews comprise approximately 70% of online reviews available in the major review communities. They tend to have a greater efect on purchase decisions than moderate reviews, because they garner more attention from consumers (Cao et al., 2011) and provide firm suggestions (Choi & Leon, 2020; Forman et al., 2008). Due to their superior efect, however, review extremity is often found in deceptive reviews to manipulate the average rating of products and to create favourable or unfavourable reputations in the market. The prevalence of such unethical reviews has increased over time, particularly in contested markets (Luca & Zervas, 2016), which could be a reason for the dominance of extreme reviews in the communities.

As the concern about deceptive reviews increases, major ecommerce platforms have adopted trust cues to ensure the reliability of their online reviews (Sacha et al., 2015), including verified purchase badges, which indicate a review is created by an actual buyer (Kim et al., 2018) and user-provided photos, which are visual cues for the buyer’s real experience with the products (Ma et al., 2018). Many recent studies have investigated the impact of trust cues on review helpfulness (Carbonell et al., 2019; He et al., 2020; Lu et al., 2018; Ma et al., 2018; Petrescu et al., 2018; Zhao et al., 2021). However, the studies reported mixed results, which confuse both scholars and practitioners in the realm of ecommerce. Some research found that trust cues have a proportional relationship with review helpfulness, attracting more attention from consumers as an eye-catcher and granting more credibility to the reviews (Carbonell et al., 2019; He et al., 2020; Ma et al., 2018; Petrescu et al., 2018). This discrepancy is notable, because it is found even between studies for the same product category, such as tablet PCs (He et al., 2020; Lu et al., 2018) and beauty products (Petrescu et al., 2018; Zhao et al., 2021).

One of the plausible reasons for the inconclusive findings could be the fact that the extant literature failed to consider the interaction efect of review extremity on the relationship between trust cues and review helpfulness. Given that perfect satisfaction (i.e., extremely positive) or dissatisfaction (i.e., extremely negative) with products or services infrequently happens (Hu et al., 2009), extreme reviews can be considered extraordinary claims. Therefore, as Carl Sagan’s wellknown phrase – “Extraordinary claims require extraordinary evidence”. – argues (Gillispie et al., 1999), extreme reviews may require compelling evidence, like trust cues, to support their extraordinariness (Tressoldi, 2011). However, extraordinariness is also concerned with rarity of event (Levine, 2012) and hence, a claim with less frequency in a community has more extraordinariness. This implies that extreme reviews may not be extraordinary but ordinary claims, because they are more common than moderate reviews in online communities (Schoenmueller et al., 2020). In this case, trust cues could be less critical or negligible in evaluating and accepting extreme reviews. To bridge the gaps, this study investigates the interaction efect of extremity on the relationship between trust cues and review helpfulness. In particular, this study aims to address the following questions: (1) “Does review extremity moderate the relationship between trust cues and review helpfulness?” (2) “Which extreme reviews, either extremely positive or negative reviews, require more trust cues?”, and (3) “Does the efect of trust cues on the helpfulness of extreme reviews difer by product attributes?”

This research adopts the theoretical lens of confirmation bias, which has supported varying behaviours of ecommerce consumers in information search (Lallement et al., 2020; Park et al., 2013) and purchase decisions (Park et al., 2013; Shin et al., 2020) to address the research questions. According to the theory, consumers tend to search for online reviews that confirm their pre-existing intention, rather than look for objective, balanced information (Pentina et al., 2018). Therefore, consumers would perceive extreme reviews as more helpful even without suficient evidence, in that extreme reviews tend to provide firm confirmation on their beliefs, weakening the efect of trust cues on review helpfulness. Analysing large, comprehensive online review data from Amazon.com, including 30,890,231 reviews in 26 product categories, this study finds (1) a negative interaction of review extremity, (2) a more substantial interaction of negative extremity, and (3) a more prominent interaction of review extremity for the reviews on search or tangible products. These findings add novel knowledge to the theory of confirmation bias: consumers tend to consider supportive evidence (i.e., trust cues) less impor tant when evaluating information corresponding to their pre-existing beliefs (i.e., extreme reviews) due to the bias, and the strength of confirmation bias difers by direction of extremity and product attributes. The remainder of this paper is organised as follows: Theoretical Foundations; Literature Review; Hypothesis Development; Research Methodology; Analysis Results; Discussions and Contributions; and Limitations and Future Research.

## 2. Theoretical foundations

This section introduces the theoretical foundation, which is confirmation bias, and the key concepts, including trust cues and review extremity, for the hypotheses of this study.

## 2.1. Confirmation bias

Confirmation bias refers to the tendency of people to prefer information that corresponds to and supports their pre-existing beliefs but to underestimate or ignore evidence that refutes the beliefs (Yin et al., 2016). People tend to process such congenial information more eficiently (Talluri et al., 2018) and perceive it as more reliable, even in the absence of suficient source credibility (Metzger & Flanagin, 2015). Confirmation bias inevitably occurs in selecting, processing, and recalling information, because it is an unconscious behaviour, rather than a strategic action (Hergovich et al., 2010).

Confirmation bias has been evidenced in the studies of diferent business disciplines. In finance, investors tend to show asymmetric reactions towards positive and negative news according to their beliefs; investors with an optimistic view on a stock underestimate the value of negative news about the stock, yet overreact to positive news (Duong et al., 2014; Park et al., 2013). In human resource management, supervisors often evaluate their employees as either good or bad and then look for evidence to solidify their judgement (Gabris & Mitchell, 1988). Confirmation bias is known to afect the executives who examine recommendations from their teams (Kahneman et al., 2011) and data analysts interpreting data (Lehner et al., 2008) in that they prefer ideas corresponding to their beliefs. In consumer behaviour, confirmation bias afects the information-seeking behaviour of consumers. When consumers have a positive impression of a product, they tend to continue the search for information supporting the impression (Lallement et al., 2020; Park et al., 2013). The bias is often amplified in information search and purchase decisions if consumers are confident in their knowledge about the product. As consumers perceive themselves as wellinformed, they tend to view details of the congenial reviews and make decisions accordingly (Park et al., 2013).

## 2.2. Trust cues

Trust cues generally indicate any evidence to enhance the reliability of an entity, including both individuals and organisations. Kramer and Lewicki (2010) categorise them into presumptive and personal trust cues; the former refers to heuristic cues built by a rule, role, or group identification, while the latter centres on the trustworthiness dimensions of individuals, including competence and integrity (Van der Werf & Buckley, 2017). At the beginning of a relationship between parties (e.g., businesses, employees), presumptive trust cues are regarded as important, while the importance shifts towards personal trust cues in building a long-term relationship.

Due to inherent trust issues between consumers and vendors in ecommerce, the presence of trust cues is critical for the success of e-retailers (Beldad et al., 2010). In ecommerce platforms, trust cues are the features that online websites or vendors use to signal their trustworthiness (Bauman, 2016). They include accredited third-party certification (Aiken, 2006), which is generally presented in visual glyphs (Sacha et al., 2015) to assist consumers in recognising the credibility of the business (Bente et al., 2012; Hesse, 2021), as a presumptive trust cue. For online reviews, likewise, such visual elements as verified purchase badges (He et al., 2020), user-provided photos (Ma et al., 2018), and review videos (Pfeufer & Phua, 2021) act as trust cues, not only supporting presented information in the reviews but also distinguishing them from deceptive reviews (Barbu et al., 2019).

## 2.3. Review extremity

Extremity in communications refers to the tendency to contain excessively positive or negative ideas in information delivered to the target (Brummelman et al., 2016; Van Dijk et al., 2009). For instance, praise extremity in education stands for the degree of overly positive, inflated evaluation (Brummelman et al., 2016), and extremity in advertising denotes the extent to which an advertisement exaggerates a product’s features without significant evidence (Zhang et al., 2017).

In online reviews, review extremity indicates either the highest or the lowest rating in the review rating system (Lee & Choeh, 2018; Siering et al., 2018), indicating the situation that a consumer is highly satisfied or dissatisfied with the experienced product or service (Li et al., 2020). As illustrated in many customer surveys, such situations are less likely to occur in reality (Hutagaol & Basbeth, 2021; Jauhari, 2018) and in the review communities where ratings are actively collected from a major population of consumers (e.g., Netflix; Tan & Netessine, 2009). Accordingly, consumers often consider extreme reviews as questionable opinions (Filieri, 2016) but perceive balanced reviews as more trustworthy (Pfeufer & Phua, 2021). In terms of their rarity and questionability, extreme reviews can thus be considered “extraordinary claims”, like hardto-believe news on media (Bivens-Tatum, 2021), scientific information (Arndt & Jones, 2018; Unger & Rollins, 2021), or postings on social networks (Hauter, 2021). In the major review communities, however, extreme reviews are more prevalent, constituting approximately 70% of the reviews submitted to the primary review communities, including Amazon (68%), Airbnb (72%), and Google Restaurants 65%; (Schoenmueller et al., 2020), because consumers with an extreme experience more actively report their reviews than those with moderate experience do (Hu et al., 2009; Lafky, 2014). This implies that consumers may consider extreme reviews as ordinary claims frequently found in the communities and, hence, they might accept them without significant evidence. Given the dominance of extreme reviews and the potential controversy, the helpfulness of extreme reviews deserves further inquiry.

## 3. Literature review

## 3.1. Efect of trust cues on review helpfulness

As the amount of online reviews has exponentially increased, so have deceptive reviews (Luca & Zervas, 2016). Ecommerce platforms, in turn, have adopted trust cues for online reviews, such as verified purchase badges (He et al., 2020) and user-provided photos (Ma et al., 2018), to help consumers identify reliable information in the crowd. The literature on online reviews commonly supports the positive influence of trust cues to review helpfulness, willingness to purchase, and product sales. Concerning the efect of verified purchase badges, researchers maintain that reviews with these badges are perceived as more helpful, because they assure the reviews are based on actual experience (Carbonell et al., 2019; Ma et al., 2018; Petrescu et al., 2018). Further, the presence of verified purchase reviews positively afects purchase probability on ecommerce platforms. Consumers are 15% more likely to purchase a product when they read verified purchase reviews than when they are only exposed to reviews from anonymous reviewers (Kim et al., 2018). As a result, products with more verified purchase reviews can enjoy higher sales (Kaushik et al., 2018). However, some recent studies reported an insignificant efect of trust cues (Wang, 2020; Zhao et al., 2021). Consumers may not consider trust cues in estimating review helpfulness, if (1) they pay little attention to whether a review is based on an actual purchase at the ecommerce platform (Wang & Song, 2020), (2) they consider online reviews as credible information source per se, or (3) they believe textual information of reviews provide enough cues to judge whether reviewers have actually experienced the products (Fresneda & Gefen, 2020). Therefore, the efect of verified purchase badges on review helpfulness remains inconclusive.

Concerning the efect of user-provided photos, prior studies commonly found their positive efect on review helpfulness due to trustworthiness and usefulness enhanced by the photos (An et al., 2020; Fan & Zhang, 2020; Sun et al., 2019). In addition to their direct efect on review helpfulness, several studies suggest the photos’ interaction efect on the relationship between diverse review factors and review helpfulness. For instance, user-provided photos are found to moderate the relationship between review length and helpfulness (An et al., 2020; Fan & Zhang, 2020) or to have a significant interaction efect only on the relationship between quality textual reviews and their helpfulness (Ma et al., 2018). Whereas, Fan and Zhang (2020) found a negative interaction of user-provided photos on the relationship between review length and helpfulness, which could occur due to excessive, diverse types of information in the reviews. However, it should be noted that these studies examined the efect of user-provided photos on the helpfulness of hotel reviews (An et al., 2020; Ma et al., 2018; Sun et al., 2019) or the helpfulness of reviews on products from a single manufacturer (i.e., Huawei mobile phones; Fan & Zhang, 2020), weakening the applicability of their findings to other product categories.

## 4. Efect of extremity review helpfulness

The efect of review extremity on review helpfulness has been extensively investigated due to its prevalence in ecommerce platforms, though the studies have reached mixed findings. The majority of the literature supports that review extremity has a positive efect on the helpfulness because the extremity attracts more attention and provides explicit suggestions for purchase (Lee & Choeh, 2014; Wu et al., 2021). However, Siering and Muntermann (2013) found its detrimental efect and some studies reported its negligible impact on review helpfulness (Huang et al., 2013; Lee & Choeh, 2018).

Confusion about the efect of review extremity on helpfulness could be the result of diferent ways to operationalise the extremity. Some studies defined extremity as the diference between an individual review’s rating for a product and the mean of all the ratings for the product (Lee & Choeh, 2014; Siering & Muntermann, 2013). However, this operationalisation may be improper because the operationalised variable represents the diference of an individual’s idea from the overall opinion, describing the inconsistency of an individual review (Baek et al., 2012; Choi & Leon, 2020). The other definition centres on whether a review has either an extremely positive (i.e., 5 out of 5) or negative (i.e., 1 out of 5) rating, which has been more widely adopted in the extant literature (Baek et al., 2012; Choi & Leon, 2020; Mudambi & Schuf, 2010) in that it more closely addresses the definition of extremity in communications: whether an opinion conveys excessively positive or negative claim (Brummelman et al., 2016; Van Dijk et al., 2009).

Another possible explanation for the inconsistent findings is truncated data, only including a few product categories for short periods. Forman et al. (2008) examined the influence of review extremity on the helpfulness of book reviews submitted for eight months, which should be insuficient to generalise their findings to other products. Siering and Muntermann (2013) used review data for 20 bestsellers in several product categories, where individual reviews are less likely to be helpful due to their quality guaranteed by the market popularity (Choi & Leon, 2020).

## 4.1. Efect of confirmation bias on review helpfulness

In the literature on online review helpfulness, the theory of confirmation bias holds that consumers are inclined to vote for congenial reviews (Yin et al., 2016). Because an initial impression of a product can be constructed by the average rating of the product, consumers tend to perceive reviews with similar ratings to the average as more helpful (Ezechukwu, 2020). Consumers could have pre-existing intentions even before visiting review platforms and thus, may consider reviews strongly supporting their intentions (i.e., extremely positive or negative ratings) as more helpful (Pentina et al., 2018). Tang and Wu (2021) also revealed that consumers perceive congenial reviews as more reliable, with the belief that the reviews contain more objective information.

## 4.2. Summary of literature review

Although there have been studies on trust cues, review extremity, and confirmation bias, continued research in this area is warranted for the following reasons. First, as confirmation bias asserts, people prefer congenial opinions that consolidate their prior beliefs, even in the absence of concrete evidence (Klayman & Ha, 1987; Trope & Bassok, 1982). Therefore, the influence of trust cues on review helpfulness could be less for extreme reviews, which are regarded as providing more concrete support to the pre-existing attitude towards products (Pentina et al., 2018). Conversely, the importance of trust cues could be more significant for extreme reviews, if consumers perceive extreme reviews as extraordinary claims or deceptive reviews in that the reviews provide unusually strong support or opposition to products (Filieri, 2016). However, few studies have investigated the interaction efect of review extremity on the relationship between trust cues and review helpfulness, which could be one of the reasons for the mixed results from the studies. Second, because the reliance of consumers on online reviews difers by product attributes (Abd-Elaziz et al., 2015; Babić Rosario et al., 2016), the interaction efect of review extremity also could so (e.g., search vs. experience, tangible vs. intangible). For instance, consumers may consider verified purchase badges and user-provided photos more important in extreme reviews on search or tangible products, because information credibility that is enhanced by trust cues could be more essential in extreme reviews on search or tangible products. Third, another significant gap in the extant literature is concerned with the datasets used in the studies. They used online review data for a specific product category, such as books (Kokkodis & Lappas, 2016), hotels (An et al., 2020; Sun et al., 2019), beauty (Zhao et al., 2021), tablet PCs (He et al., 2020; Lu et al., 2018), light bulbs (Fresneda & Gefen, 2020), and mobile phones (Fan & Zhang, 2020) but rarely examined the efect of trust cues for more than two product categories. In addition, regarding their sample size and time period of data, many of the studies adopted highly truncated data, covering a few months of online reviews including fewer than 10,000 reviews (Fresneda & Gefen, 2020; He et al., 2020; Li et al., 2021; Zhao et al., 2021). This could be a primary reason for the contradictory findings, having weaker generalisability for other product categories. Lastly, little research attempted to clarify the diferential efect of review extremity on helpfulness by product attributes, which should contribute to the knowledge on review helpfulness and confirmation bias.

## 5. Hypothesis development

The primary purpose of this study is to investigate the interaction efect of review extremity on the relationship between trust cues and review helpfulness. Given that consumers prefer online reviews corresponding to their beliefs (Ezechukwu, 2020) and extreme reviews tend to meet their needs (Choi & Leon, 2020), confirmation bias should have a significant efect on the relationship between trust cues and review helpfulness. Hence, this study employs confirmation bias as the theoretical foundation to develop hypotheses.

## 5.1. Diferential efect of trust cues on helpfulness by review extremity

According to the theory of confirmation bias, people prefer information consistent with their initial beliefs (Lehner et al., 2008; Yin et al., 2016) and process the information more eficiently (Talluri et al., 2018). Thus, they are likely to view congenial information as more credible, regardless of its coherence and source credibility (Metzger & Flanagin, 2015), and are less likely to require evidence to verify the congenial information.

As numerous extant studies have afirmed, consumers favour extreme reviews due to their eye-catching attributes and firm suggestion for purchase decisions (Cao et al., 2011; Lee & Choeh, 2014; Wu et al., 2021), and trust cues enhance the credibility of presented claims in the reviews (Bjering et al., 2015). In terms of confirmation bias, therefore, consumers should consider trust cues in extreme reviews less important in determining the helpfulness of online reviews, because extreme reviews would be accepted and perceived as helpful even with less support from trust cues due to the bias. This discussion leads to the following hypotheses:

H1a. The efect of verified purchase badges on review helpfulness is less significant for extreme reviews than moderate reviews.

H1b. The efect of user-provided photos on review helpfulness is less significant for extreme reviews than moderate reviews.

## 5.2. Diferential efect of trust cues on helpfulness by direction of extremity

Although the importance of trust cues should be less considerable for extreme reviews, it could depend on the direction of the extremity. As the literature on online news difusion alleges, negative news travels faster than positive news due to the higher interest of the public in bad news (Fang & Ben-Miled, 2017; Hornik et al., 2015). In addition, negative news delivering critical messages is preferred and considered more important, which is known as negativity bias (Knobloch-Westerwick et al., 2020). This is consistent with the literature advocating a more profound efect of negative reviews due to their higher credibility (Chang & Wu, 2014), acceptability (Lee & Koo, 2012), usefulness (Liu et al., 2010), and impact on purchase decisions (Chen et al., 2011).

The higher credibility and acceptability of negative reviews should afect the relationship between trust cues and review helpfulness. Trust cues in extremely negative reviews should have a less significant impact on their helpfulness than in extremely positive reviews, because the negative reviews inherently have the aforementioned advantages. Moreover, consumers are more likely to use online reviews to understand risks and reduce potential losses than to enhance their gains (Park & Nicolau, 2015). This implies that consumers should consider trust cues less important in evaluating review helpfulness of extremely negative reviews, which should warn about potential risks and losses. Therefore, the following hypotheses are introduced:

H2a. The efect of verified purchase badges on review helpfulness is less significant for extremely negative reviews than extremely positive reviews.

H2b. The efect of user-provided photos on review helpfulness is less significant for extremely negative reviews than extremely positive reviews.

## 5.3. Diferential efect of trust cues on helpfulness for search and experience products

Previous research has classified products into search and experience in terms of their evaluability. Search products difer from experience products in that consumers can evaluate product quality before actual consumption, whereas consumers have more dificulties in assessing the quality of experience products before direct experience (Liu et al., 2016). The product attribute is known to interact the relationship between online review factors (e.g., review length) and helpfulness (Sun et al., 2019), purchase intention (Christodoulides et al., 2012), and product sales (Cui et al., 2012). The efect of online reviews is generally greater for search products, because reviews on search products tend to convey objective information that assists consumers to predict product quality.

Concerning the diferential efect of trust cues, it is expected that their efect on review helpfulness is larger for extreme reviews on search products, because consumers evaluate online reviews more carefully when purchasing search products (Luan et al., 2016). Thus, they should weigh the credibility of extreme reviews on search products, which can be supplemented by trust cues. In addition, since consumers are likely to expect rational and factual information in search product reviews (Huang et al., 2013), the objectivity of information should be more critical for search product reviews. Given that extreme reviews are often considered biased opinions (Koh et al., 2010; Salehan & Kim, 2016), the importance of trust cues, which intensify the objectivity of information, should be greater for search product reviews, introducing the following hypotheses:

H3a. The efect of verified purchase badges on review helpfulness is more significant for extreme reviews on search products than those on experience products.

H3b. The efect of user-provided photos on review helpfulness is more significant for extreme reviews for search products than those for experience products.

## 5.4. Diferential efect of trust cues on helpfulness for tangible and intangible products

Product tangibility refers to the palpability of a product and the extent to which a consumer can experience it through the senses (Hellén & Gummerus, 2013). As a product has more tangibility, consumers tend to have less perceived uncertainty in their purchase decision, because they can scrutinise more details of the product (Abd-Elaziz et al., 2015). Prior online review studies consistently reported the significant efect of product tangibility on review helpfulness but have reached mixed conclusions. The research, which defined intangible products as servicecentred products (e.g., accommodation, education, dining services), found a more profound efect of online reviews on sales for intangible products, because these products inevitably have greater uncertainty and risks due to their intangibility and online reviews help consumers lessen their concerns about the uncertainty and risks (Yen & Tang, 2015). On the contrary, some studies reported that the efect is weaker for intangible products, which are operationalised as digital products (Babić Rosario et al., 2016), because portraying intangible features and benefits in the reviews is more arduous. Therefore, reviews on intangible products are less likely to be perceived as helpful.

In terms of the efect of trust cues on the helpfulness of extreme reviews, the impact should be greater for tangible products, because reviews on tangible products tend to describe fact-oriented traits of the items (Rossmann et al., 2016), which can be substantiated by trust cues, whereas the substantiation should be less for intangible product reviews, mainly describing personal feelings and experiences of reviewers. For instance, although a five-star review on a movie has a verified purchase badge and screen shots for the movie, the trust cues may not provide significant support if the review mostly describes subjective feelings (e.g., fun, sad, exciting). In addition, this current study focuses on the online review platform of an ecommerce website (i.e., Amazon.com), which does not ofer service-oriented products but does ofer digital products. Given that the efect of online reviews tends to be weaker for digital products (Babić Rosario et al., 2016), consumers should care less about trust cues when evaluating the helpfulness of reviews on digital products. Therefore, the efect of trust cues on the helpfulness of extreme reviews should be weaker for digital products, which are regarded as intangible products in this study. This discussion introduces the following hypotheses:

![](/api/attachments/H2T92A7X/fulltext/images/b2fd9f0e505c8a9ddd504ff416568bbf2dd41d15fc89bc793fb26a8573aeb7a2.jpg)  
Figure 1. Research model.

H4a. The efect of verified purchase badges on review helpfulness is more significant for extreme reviews on tangible products than those for intangible products.

H4b. The efect of user-provided photos on review helpfulness is more significant for extreme reviews on tangible products than those for intangible products.

The proposed hypotheses are summarised in Figure 1 below.

## 6. Research methodology

## 6.1. Data preparation

This study adopts online review data collected from Amazon.com, which was used for Ni et al. (2019). This dataset had 208,533,788 reviews for 26 product categories, which were submitted to Amazon.com from May 1996 to October 2018, approximately 23 years. The initial dataset contained the variables collected from Amazon.com, including reviewer ID, product ID, the number of helpfulness votes, textual review, rating score from 1 to 5, verified purchase, and URLs of user-provided photos in the JSON data format. Because this semi-structured data was ineficient to prepare necessary variables and conduct analysis, the data was converted to CSV format first with jq (stedolan.github.io/jq/), which is a JSON file processor in Python. This data processing was conducted on a Windows 10 workstation with 64GB of RAM and 2TB of SSD, running a Debian Linux virtual machine that efectively supports jq. Next, due to its extraordinary size (83.4 GB), data preparation was performed in a cloud environment supported by the server computers of an educational institution. The CSV file was imported into a MySQL database, and primary variables for hypothesis tests were created with Python scripts based on the variables available in the initial dataset aforementioned (See Operationalisation of Constructs for more details). Data cleansing was administered to remove duplicated rows and observations with missing values, deleting 137 reviews and remaining 208,533,651 reviews from the initial dataset. Lastly, reviews with fewer than two helpfulness votes, the minimum threshold for review helpfulness prediction (Sun et al., 2019), were removed, dropping 177,643,420 reviews and remaining 30,890,231 reviews for the hypothesis test of this study (See, Appendix A for more details). This dataset including a large number of cases is expected to have sound representativeness for online reviews (Hoferth, 2005) and to help understand consumer behaviours concerning review helpfulness vote, ruling out potential bias by respondent perceptions or data collection process (Calantone & Vickery, 2010; Roth et al., 2015). Due to these advantages, online review studies have increasingly employed secondary data to validate their hypotheses (Liang et al., 2021).

## 6.2. Operationalisation of constructs

Review Helpfulness, which is the target variable, is operationalised as the number of helpfulness votes that a review has received since it was submitted (Qazi et al., 2016; Hu et al., 2017; Zhu et al., 2014). Two independent variables, Verified Purchase and User-Provided Photo, are operationalised as binary variables. If a review has one or more than one userprovided photo, it is coded as “1” and otherwise “0” for User-Provided Photo. Similarly, if a review has a verified purchase badge, it is coded as “1” and if not “0” for Verified Purchase.

Review Extremity is operationalised as a binary variable. If a review has either a 1- or 5-star rating score, which respectively represents extremely negative and extremely positive reviews, it is coded as “1”, while as coded “0” if it has a moderate rating including 2, 3, or 4 (Mudambi & Schuf, 2010). To define search and experience products, the categorisation schemes are adopted from the extant literature (Appendix B for more details). Although most of the product categories are available in the literature, few studies discuss the categories of Gift Cards and Magazine Subscriptions. They are defined as search products in this study because consumers can evaluate their quality prior to purchase (Mudambi & Schuf, 2010). For example, consumers can know the financial value of gift cards and purchasable products with the gift cards before they buy the products. Search Product is coded as “1”; experience product as “0”. Concerning product tangibility, digital products are defined as intangible products (Babić Rosario et al., 2016; Choi & Leon, 2020) in that their core value is completely intangible to consumers (Mittal, 1999). On Amazon.com, digital products are Instant Videos, Mobile Apps, Digital Music, Kindle eBooks, Movies, and Video Games. They are coded as “0” for Tangible Product, and the rest of the product categories are coded as “1”.

In addition to the aforementioned variables, there are many other determinants of online review helpfulness. They are included as control variables in the models for hypothesis tests, which can be categorised into review factors, reviewer factors, and context factors (Hlee et al., 2018). Review factors are Review Inconsistency, Review Extremity, Review Depth, and Days Lapsed. Reviewer factors include Reviewer Expertise and Reviewer Experience. Lastly, context factors are Product Satisfaction and Product Popularity (See, Appendix C for more details).

## 6.3. Analysis method

This study uses econometrics to test the proposed hypotheses based on the estimated parameters in the models (Wooldridge, 2015). This approach has been popularly adopted not only in the empirical analysis of consumer behaviour presented in quantitative data (Koop, 2005; Nevo, 2011) but also in online review studies (Luo et al., 2021). In terms of analysis design, this study adopts the simple slopes approach, testing diferences between regression coeficients for diferent groups (Robinson et al., 2013). Although it is common to test interaction efects using interaction terms in a regression model, the approach is known to be less powerful than the analysis of simple slopes (Robinson et al., 2013). Furthermore, the regression with interaction terms is inadequate for this study, because both predictors for an interaction term would be binary variables (e.g., Extreme Review\*Verified Purchase, Extreme Review\*User-Provided Photo). When an interaction term has two binary variables, it is ambiguous to interpret which one has an interaction efect on the other (Yip & Tsang, 2007). For instance, when an interaction term, Extreme Review\*Verified Purchase, is positive and statistically significant, it can be interpreted in two ways: when a review has extremity, the efect of verified purchase badges on review helpfulness is greater, or when a review has a verified purchase badge, the efect of review extremity on helpfulness is greater. Lastly, the model would have three terms for Extreme Reviews in a model (e.g., Extreme Reviews,

Extreme Reviews\*Verified Purchase, Extreme Reviews\*User-Provided Photo), if adding the two interaction terms. Because the additional interaction terms afect the main efect of a variable (Mudambi & Schuf, 2010), they distract understanding of its true main efect. To address this issue, many review helpfulness studies employed the simple slopes to test interaction efects or to check their robustness (Choi & Leon, 2020; Huang et al., 2018; Reimer & Benkenstein, 2016). Empirical models testing the proposed hypotheses are illustrated as below;

## Model 1 Testing H1a, H1b, H2a, and H2b

LnðReview HelpfulnessÞ ¼ α þ α Verified Purchase þ α User   Provided Photo þα Tangible Product þ α Search Product þ α Review Depth þα Review Inconsistency þ α Days Lapsed þ α LnðReviewer Experience þα LnðReviewer ExpertiseÞ þ α Product Satisfaction þα Product Popularity þ ε

## Model 2 Testing H3aand H3b

LnðReview HelpfulnessÞ ¼ β þ β VerifiedPurchase þ β User   ProvidedPhoto þβ Tangible Product þ β Review Depth þ β Review Inconsistency þβ Days Lapsed þ β LnðReviewer Experience þβ LnðReviewer ExpertiseÞ þ β Product Satisfaction þβ Product Popularity þ ε

Model 3 Testing H4a and H4b

LnðReview HelpfulnessÞ ¼ δ þ δ Verified Purchase þ δ User   Provided Photo þδ Search Product þ δ Review Depth þ δ Review Inconsistency

þδ<sub>6</sub>Days Lapsed þ δ<sub>7</sub>LnðReviewer ExperienceÞ

þδ LnðReviewer ExpertiseÞ þ δ Product Satisfaction

þδ Product Popularity þ ε

Because several variables have skewed distributions, a log transformation is applied to these variables, including Review Helpfulness, Review Depth, Days Lapsed, Reviewer Expertise, and Reviewer Experience. Model 1 tests Hypothesis 1a, 1b, 2a, and 2b, adopting diferent datasets for the two groups of hypotheses. For Hypothesis 1a and 1b, Model 1 is applied to the data with extreme reviews and that with moderate reviews to compare the coeficients of Verified Purchase and User-Provided Photo. For Hypothesis 2a and 2b, it is applied to the data with extremely positive reviews (i.e., 5-star rating) and that with extremely negative reviews (i.e., 1-star rating) to examine the coeficient diference between the two predictors. Model 2 testing Hypothesis 2a and 2b is similar to Model 1 but does not include Search Product, because the hypotheses examine how the efect of trust cues on the helpfulness of extreme reviews difer by search and experience products. Model 2 is applied to the data with extreme reviews on search products and data with extreme reviews on experience products. Model 3 omits a predictor, Tangible Product from Model 1 because it compares how the impact of trust cues on the helpfulness of extreme reviews changes by product tangibility. Model 3 is applied to two datasets: data with extreme reviews on tangible products and data with extreme reviews on intangible products.

## 7. Analysis results

## 7.1. Descriptive statistics

As illustrated in Table 1, 68.7% of online reviews in the dataset (21,213,846) are either extremely positive or negative, substantiating the prevalence of extreme reviews at Amazon.com. Regarding trust cues, 67.6% of the entire reviews (20,894,840) have verified purchase badges, while 5.4% (1,676,801) have one or more than one user-provided photo. Regarding product attributes, search products have 66.8% of the reviews (20,623,514) and tangible products have 87.5% (27,040,313).

As illustrated in the correlation matrix (Table 2), most of the correlation coeficients are below 0.2, while the correlation between two control variables, Reviewer Experience and Reviewer Expertise, are somewhat high (0.8). Even though a high correlation between control variables is not an issue, Variance Inflation Factor (VIF) tests are conducted to test multicollinearity (Mansfield & Helms, 1982). As expected, the largest VIF value is 2.83, which is far below 10 (Naser et al., 2013), and the mean VIF is 1.44, confirming no multicollinearity in the variables.

## 7.2. Hypothesis test results

Before testing the proposed hypotheses, a base model is estimated to examine the efect of verified purchase badges and user-provided photos, adopting the entire Table 1. Descriptive statistics.

dataset including 30,890,093 reviews. The R-squared of this model is 0.378, and test results indicate that both verified purchase badges $( \mathbf { a } _ { 1 } = 0 . 0 6 0 , \ \mathrm { p } < 0 . 0 1 )$ and user-provided photos $( \mathbf { a } _ { 2 } = 0 . 3 7 3 , \mathbf { p } < 0 . 0 1 )$ have a positive efect on review helpfulness. The efect of trust cues on review helpfulness is compared between extreme reviews and moderate reviews for testing Hypothesis 1a and 1b. While both Verified Purchase and User-Provided Photo are positive and statistically significant for the two groups, their efects are more substantial for moderate reviews. The coeficient of Verified Purchase for moderate reviews (α<sub>1\_moderate</sub> $= 0 . 0 8 3 , \ \mathsf { p } \ < \ 0 . 0 1 )$ is greater than that for extreme reviews $( \mathbf { a } _ { 1 \_ { \mathrm { e x t r e m e } } } = 0 . 0 5 1 , \mathrm { p } < 0 . 0 1 )$ and the diference is significant $( \mathbf { a } _ { 1 \_ { \mathrm { d i f f e r e n c e } } } = 0 . 0 3 2 , \mathtt { p } < 0 . 0 1 )$ ). Likewise, the coeficient of User-Provided Photo for moderate reviews $( \mathbf { a } _ { 2 \_ { \mathrm { m o d e r a t e } } } = 0 . 3 9 3 , \ \mathrm { p } < 0 . 0 1 )$ is larger than that for extreme reviews $( \mathbf { a } _ { 2 \_ \mathrm { e x t r e m e } } = 0 . 3 6 0 , \mathrm { p } < 0 . 0 1 )$ with significant diference $\begin{array}{c} \begin{array} { l l l } { \left( \mathbf { a } _ { 2 } \mathbf { \Psi } _ { \mathrm { d i f f e r e n c e } } \right.} & { = } & { 0 . 0 3 3 } \end{array}   \end{array}$ $\mathrm { ~ \tt ~ { ~ P ~ } ~ } < \mathrm { ~ 0 . 0 1 } )$ . Therefore, Hypothesis 1a and 1b are supported.

Hypothesis 2a and 2b are examined, comparing the efect of trust cues on helpfulness between extremely positive and negative reviews. The coeficient of Verified Purchase for extremely positive reviews is positive and statistically significant $( \mathrm { a _ { 1 \_ e x t . p o s } } = 0 . 0 7 2$ $\mathrm { p } < 0 . 0 1 )$ , while that for extremely negative reviews is negative and statistically not significant $\begin{array} { r } { ( \mathsf { a } _ { 1 \_ \mathrm { e x t . n e g } } = \mathsf { \Pi } _ { - 0 } . } \end{array}$ $0 0 1 , \mathrm { p } = 0 . 5 8 4 )$ . This indicates that the positive efect of verified purchase badges on review helpfulness is significant for extremely positive reviews but not for extremely negative reviews, confirming Hypothesis 2a. In terms of the efect of user-provided photos, there is a significant diference between the two groups. Each coeficient is significant, and extremely positive reviews have a higher coeficient for User-Provided Photo $( \mathrm { a } _ { 2 \_ \mathrm { e x t . p o s } } = 0 . 3 8 2 , \ \mathrm { p } \ < \ 0 . 0 1 )$ than extremely negative reviews $( \mathbf { a } _ { 2 \_ \mathrm { e x t . n e g } } = 0 . 3 1 2 , \ \mathrm { p } \ < \ 0 . 0 1 )$ . The coeficient diference is found to be significant $( \mathsf { a } _ { 2 \_ { \mathrm { e x t } } } \mathsf { \Pi } _ { \mathrm { d i f f e r e n c e } } ~ = ~ 0 . 0 7 0 , ~ \mathsf { p } ~ < ~ 0 . 0 1 )$ and, hence, Hypothesis 2b is supported. The test results for Hypothesis 1a, 1b, 2a, and 2b are summarised in Table 3.

<table><tr><td>Variable</td><td>Mean</td><td>Standard Deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td>Review Helpfulness</td><td>7.701</td><td>37.684</td><td>2</td><td>58206</td></tr><tr><td>Review Inconsistency</td><td>0.964</td><td>1.0442</td><td>0</td><td>4</td></tr><tr><td>Review Depth</td><td>130.719</td><td>165.625</td><td>0</td><td>7171</td></tr><tr><td>Days Lapsed</td><td>2101.314</td><td>1534.300</td><td>0</td><td>8134</td></tr><tr><td>Reviewer Expertise</td><td>269.653</td><td>1956.293</td><td>2</td><td>87934</td></tr><tr><td>Reviewer Experience</td><td>41.4488</td><td>211.372</td><td>1</td><td>13078</td></tr><tr><td>Product Satisfaction</td><td>4.085</td><td>0.773</td><td>1</td><td>5</td></tr><tr><td>Product Popularity</td><td>135.656</td><td>645.922</td><td>1</td><td>57767</td></tr><tr><td colspan="5">Frequency (n = 30,890,093)</td></tr><tr><td>Review Extremity</td><td></td><td>21,213,846 (68.7%)</td><td></td><td></td></tr><tr><td>Verified Purchase</td><td></td><td>20,894,840 (67.6%)</td><td></td><td></td></tr><tr><td>User-Provided Photo</td><td></td><td>1,676,801 (5.4%)</td><td></td><td></td></tr><tr><td>Search Product</td><td></td><td>20,623,514 (66.8%)</td><td></td><td></td></tr><tr><td>Tangible Product</td><td></td><td>27040313 (87.5%)</td><td></td><td></td></tr></table>

Table 2. Correlation matrix.

<table><tr><td>-</td><td>RH</td><td>RE1</td><td>VP</td><td>UP</td><td>RD</td><td>RI</td><td>DL</td><td>RE2</td><td>RE3</td><td>TP</td><td>SP</td><td>PS</td><td>PP</td></tr><tr><td>RH</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RE1</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>VP</td><td>-0.04</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>UP</td><td>0.04</td><td>0.03</td><td>0.08</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RD</td><td>0.12</td><td>-0.09</td><td>-0.25</td><td>-0.02</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RI</td><td>0.01</td><td>0.01</td><td>0.05</td><td>0.02</td><td>-0.04</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DL</td><td>0.06</td><td>-0.04</td><td>-0.51</td><td>-0.18</td><td>0.17</td><td>-0.12</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RE2</td><td>0.01</td><td>-0.03</td><td>-0.11</td><td>-0.01</td><td>0.19</td><td>-0.05</td><td>-0.01</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RE3</td><td>0.05</td><td>-0.03</td><td>-0.11</td><td>-0.01</td><td>0.21</td><td>-0.04</td><td>0.06</td><td>0.80</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>TP</td><td>0.01</td><td>0.01</td><td>0.18</td><td>0.08</td><td>-0.08</td><td>0.03</td><td>-0.23</td><td>-0.05</td><td>-0.04</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>SP</td><td>0.01</td><td>0.01</td><td>-0.05</td><td>-0.06</td><td>0.06</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.01</td><td>0.38</td><td>1.00</td><td></td><td></td></tr><tr><td>PS</td><td>-0.01</td><td>0.06</td><td>0.08</td><td>0.03</td><td>0.01</td><td>-0.04</td><td>-0.09</td><td>0.01</td><td>0.01</td><td>0.03</td><td>0.06</td><td>1.00</td><td></td></tr><tr><td>PP</td><td>0.01</td><td>0.01</td><td>0.06</td><td>0.04</td><td>0.01</td><td>0.11</td><td>-0.10</td><td>-0.01</td><td>-0.01</td><td>0.01</td><td>0.02</td><td>0.03</td><td>1.00</td></tr></table>

\* RH: Review Helpfulness, RE1: Review Extremity, VP: Verified Purchase, UP: User-Provided Photo, RI: Review Inconsistency, RD: Review Depth, DL: Days Lapsed, RE2: Reviewer Experience, RE3: Reviewer Expertise, TP: Tangible Product, SP: Search Product, PS: Product Satisfaction, PP: Product Popularity.

Table 3. Test results for hypothesis 1a, 1b, 2a, and 2b $( ^ { \ast } \mathfrak { p } < 0 . 0 5 , ^ { \ast \ast } \mathfrak { p } < 0 . 0 1 )$

<table><tr><td rowspan="2">Dependent: Ln(Review Helpfulness)</td><td colspan="3">H1a &amp; H1b</td><td colspan="3">H2a &amp; H2b</td></tr><tr><td>Moderate Reviews</td><td>Extreme Reviews</td><td></td><td>Ext. Positive Reviews</td><td>Ext. Negative Reviews</td><td></td></tr><tr><td>Sample Size</td><td>9,676,237</td><td>21,213,706</td><td></td><td>16,740,410</td><td>4,473,296</td><td></td></tr><tr><td>R-Square</td><td>0.343</td><td>0.398</td><td>-</td><td>0.379</td><td>0.479</td><td>-</td></tr><tr><td></td><td>Coefficient</td><td></td><td>Diff.</td><td>Coefficient</td><td></td><td>Diff.</td></tr><tr><td>Verified Purchase</td><td>0.083**</td><td>0.051**</td><td>0.032*</td><td>0.072**</td><td>-0.001</td><td>0.073*</td></tr><tr><td>User-Provided Photo</td><td>0.393**</td><td>0.360**</td><td>0.033*</td><td>0.382**</td><td>0.312**</td><td>0.070*</td></tr><tr><td colspan="7">Control Variables</td></tr><tr><td>Ln(Review Depth)</td><td>0.095**</td><td>0.071**</td><td>-</td><td>0.079**</td><td>0.064**</td><td>-</td></tr><tr><td>Review Inconsistency</td><td>0.043**</td><td>0.031**</td><td>-</td><td>-0.016**</td><td>0.016**</td><td>-</td></tr><tr><td>Ln(Days Lapsed)</td><td>0.011**</td><td>0.004**</td><td>-</td><td>0.005**</td><td>0.012**</td><td>-</td></tr><tr><td>Ln(Reviewer Experience)</td><td>-0.364**</td><td>-0.381**</td><td>-</td><td>-0.368**</td><td>-0.403**</td><td>-</td></tr><tr><td>Ln(Reviewer Expertise)</td><td>0.378**</td><td>0.435**</td><td>-</td><td>0.412**</td><td>0.523**</td><td>-</td></tr><tr><td>Tangible Product</td><td>0.096**</td><td>0.088**</td><td>-</td><td>0.104**</td><td>0.033**</td><td>-</td></tr><tr><td>Search Product</td><td>0.006**</td><td>-0.001</td><td>-</td><td>-0.019**</td><td>0.058**</td><td>-</td></tr><tr><td>Product Satisfaction</td><td>-0.015**</td><td>-0.025**</td><td>-</td><td>-0.039**</td><td>-0.004**</td><td>-</td></tr><tr><td>Product Popularity</td><td>0.001**</td><td>0.001**</td><td>-</td><td>0.001**</td><td>0.001**</td><td>-</td></tr><tr><td>Constant</td><td>0.382**</td><td>0.554**</td><td>-</td><td>0.618**</td><td>0.378**</td><td>-</td></tr></table>

The efect of trust cues on the helpfulness of extreme reviews is compared between search and experience products. The coeficient of Verified Purchase is higher in the regression model for search products $( \beta _ { 1 \_ s e a r c h } = 0 . 0 5 4 , \mathrm { ~ p ~ < ~ 0 . 0 1 ) }$ than that for experience product $( \beta _ { 1 _ { - } \mathrm { e x p e r i e n c e } } = 0 . 0 4 1 , \ \mathrm { p ~ < ~ } 0 . 0 1 )$ The significant diference between the two coeficients provides support to Hypothesis 3a $( \beta _ { 1 \_ \mathrm { d i f f e r e n c e } } = 0 . 0 1 4 ,$ $\Upsilon ^ { < } < 0 . 0 1 )$ . Next, the efect of user-provided photos is compared between search and experience products. The coeficient of User-Provided Photo is lower for search products $( \beta _ { 2 \mathrm { { \_ s e a r c h } } } = 0 . 3 6 2 , \mathrm { p } < 0 . 0 1 )$ than that for experience products $( \beta _ { 2 \mathrm { { \_ e x p e r i e n c e } } } = 0 . 3 6 4 , \mathrm { p } < 0 . 0 1 )$ but the diference is not significant (β<sub>2\_diference</sub> $= ~ 0 . 0 0 2 , \mathrm { ~ p ~ } = ~ 0 . 2 2 5 )$ . Thus, Hypothesis 3b is not supported.

Concerning the efect of product tangibility, Hypothesis 4a is supported, because the coeficient of Verified Purchase for tangible products $( \delta _ { 1 \mathrm { \_ t a n g i b l e } }$ $= 0 . 0 5 5 , \mathtt { p } < 0 . 0 1 )$ is greater than that for intangible products $( \delta _ { \mathrm { 1 \_ i n t a n g i b l e } } ~ = ~ 0 . 0 1 9 , ~ \mathrm { p ~ < ~ 0 . 0 1 ) }$ with the statistically significant diference $( \delta _ { 1 \_ \mathrm { d i f f e r e n c e } } = 0 . 0 3 6 ,$ $\mathsf { p } < 0 . 0 1 )$ . Lastly, the coeficients of User-Provided Photo are compared for testing Hypothesis 4b. The coeficient for tangible products is larger $( \delta _ { 2 \mathrm { \_ t a n g i b l e } }$ $= 0 . 3 6 5 , \mathrm { ~ p ~ < ~ } 0 . 0 1 )$ than that for intangible products $( \delta _ { 2 \mathrm { - i n t a n g i b l e } } = 0 . 2 1 0 , \mathrm { p < 0 . 0 1 ) }$ . The coeficient diference is statistically significant $( \delta _ { 2 \_ \mathrm { d i f f e r e n c e } } = 0 . 1 5 5 ,$ $\mathsf { p } < 0 . 0 1 )$ , supporting Hypothesis 4b. Table 4 summarises the test results for Hypothesis 3a, 3b, 4a, and 4b.

Table 4. Test results for hypothesis 3a, 3b, 4a, and 4b (\*\*p < 0.01).

<table><tr><td rowspan="2">Dependent: Ln(Review Helpfulness)</td><td colspan="3">H3a &amp; H3b</td><td colspan="3">H4a &amp; H4b</td></tr><tr><td>Ext. Review for Search</td><td>Ext. Review for Experience</td><td></td><td>Ext. Review for Tangible</td><td>Ext. Review for Intangible</td><td></td></tr><tr><td>Sample Size</td><td>14,192,753</td><td>7,020,953</td><td></td><td>18,599,195</td><td>2,614,511</td><td></td></tr><tr><td>R-Square</td><td>0.408</td><td>0.374</td><td>-</td><td>0.401</td><td>0.379</td><td>-</td></tr><tr><td></td><td>Coefficient</td><td></td><td>Diff.</td><td>Coefficient</td><td></td><td>Diff.</td></tr><tr><td>Verified Purchase</td><td>0.054**</td><td>0.041**</td><td>0.014**</td><td>0.055**</td><td>0.019**</td><td>0.036**</td></tr><tr><td>User-Provided Photo</td><td>0.362**</td><td>0.364**</td><td>0.002</td><td>0.365**</td><td>0.210**</td><td>0.155**</td></tr><tr><td colspan="7">Control Variables</td></tr><tr><td>Ln(Review Depth)</td><td>0.069**</td><td>0.078**</td><td>-</td><td>0.071**</td><td>0.076**</td><td>-</td></tr><tr><td>Review Inconsistency</td><td>0.039**</td><td>0.012**</td><td>-</td><td>0.031**</td><td>0.028**</td><td>-</td></tr><tr><td>Ln(Days Lapsed)</td><td>-0.001**</td><td>0.009**</td><td>-</td><td>0.011**</td><td>-0.053**</td><td>-</td></tr><tr><td>Ln(Reviewer Experience)</td><td>-0.395**</td><td>-0.350**</td><td>-</td><td>-0.375**</td><td>-0.418**</td><td>-</td></tr><tr><td>Ln(Reviewer Expertise)</td><td>0.450**</td><td>0.403**</td><td>-</td><td>0.435**</td><td>0.442**</td><td>-</td></tr><tr><td>Tangible Product</td><td>0.081**</td><td>0.082**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Search Product</td><td>-</td><td>-</td><td>-</td><td>-0.001**</td><td>-0.011**</td><td>-</td></tr><tr><td>Product Satisfaction</td><td>-0.025**</td><td>-0.023**</td><td>-</td><td>-0.022**</td><td>-0.035**</td><td>-</td></tr><tr><td>Product Popularity</td><td>0.000**</td><td>0.000**</td><td>-</td><td>0.000**</td><td>0.000**</td><td>-</td></tr><tr><td>Constant</td><td>0.588**</td><td>0.539**</td><td>-</td><td>0.571**</td><td>1.094**</td><td>-</td></tr></table>

Table 5. Test results from OLS and Negative Binomial (✓: supported, -: not supported).

<table><tr><td rowspan="2">Hypothesis</td><td colspan="2">Votes ≥ 2</td><td colspan="2">Votes ≥ 5</td><td colspan="2">Votes ≥ 10</td></tr><tr><td>OLS</td><td>Binomial</td><td>OLS</td><td>Binomial</td><td>OLS</td><td>Binomial</td></tr><tr><td>H1a</td><td>√</td><td>√</td><td>√</td><td>√</td><td>-</td><td>-</td></tr><tr><td>H1b</td><td>√</td><td>√</td><td>√</td><td>√</td><td>-</td><td>√</td></tr><tr><td>H2a</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>H2b</td><td>√</td><td>√</td><td>√</td><td>√</td><td>-</td><td>-</td></tr><tr><td>H3a</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>H3b</td><td>-</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>H4a</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>H4b</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>-</td></tr></table>

## 7.3. Robustness check

Additional analyses are administered to check robustness of the hypothesis test results. First, supplementary tests are performed with higher thresholds for helpfulness votes: at least five and ten votes (Siering et al., 2018), allowing to further test proposed hypotheses with fine-grained helpful reviews (Sun et al., 2019). In this robustness test, Hypothesis 2a, 3a, 4a, and 4b are supported in all the analyses. However, Hypothesis 1a and 1b are not supported in the analyses for the reviews with at least ten helpfulness votes. Hypothesis 2b is not supported in the analyses with the reviews with at least ten votes, although it is supported in the other analyses with at least five votes. Concerning Hypothesis 3b, the diference for User-Provided Photo is significant in the tests adopting the reviews with at least five and ten helpfulness votes, though it was not supported in the initial analysis with the review with at least two votes (See, Appendix D for more details).

Second, even though an ordinary least squares regression has been popularly used to examine predictors of review helpfulness in prior studies (Choi & Leon, 2020; Ghose & Ipeirotis, 2011; Mudambi & Schuf, 2010; Wu, 2013), some may claim that ordinary least squares regression is inadequate for the target variable of this study, Review Helpfulness because it is a count variable with larger variance than its mean that can be subject to an overdispersion issue (Zhou & Guo, 2017). Although the issue should be resolved in the logtransformed Review Helpfulness, which is the actual target variable of this study, some could question this issue. Therefore, the negative binomial regression is applied to the models, which lessens not only the over-dispersion concern but also the concern about omitted variable bias (Zhou & Guo, 2017), adopting Review Helpfulness as the dependent and diferent thresholds for helpfulness votes (Table 5). Most of the test results are identical to those from the OLS models. However, the result with at least ten helpfulness votes for Hypothesis 1b and that with at least two votes for Hypothesis 3b, which were not significant in the OLS models, are significant in the negative binomial regression; and Hypothesis 4b, which was supported in the OLS model, is not supported in the negative binomial model with at least ten votes (See, Appendix E for more details).

Table 6. Test results in two diferent terms (✓: supported, -: not supported).

<table><tr><td rowspan="2">Hypothesis</td><td colspan="2">Dataset from May 1996 to July 2007</td><td colspan="2">Dataset from August 2007 to October 2018</td></tr><tr><td>OLS</td><td>Binomial</td><td>OLS</td><td>Binomial</td></tr><tr><td>H1a</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>H1b</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>H2a</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>H2b</td><td>-</td><td>-</td><td>√</td><td>√</td></tr><tr><td>H3a</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>H3b</td><td>-</td><td>-</td><td>√</td><td>√</td></tr><tr><td>H4a</td><td>-</td><td>√</td><td>√</td><td>√</td></tr><tr><td>H4b</td><td>-</td><td>-</td><td>√</td><td>√</td></tr></table>

Table 7. Conclusion of Hypothesis Tests (S: supported, SS: strongly supported).

<table><tr><td colspan="2">Hypothesis</td><td>Result</td></tr><tr><td>H1a</td><td>The effect of a verified purchase badge on review helpfulness is less significant for extreme reviews than moderate reviews.</td><td>S</td></tr><tr><td>H1b</td><td>The effect of user-provided photos on review helpfulness is less significant for extreme reviews than moderate reviews.</td><td>S</td></tr><tr><td>H2a</td><td>The effect of a verified purchase badge on review helpfulness is less significant for extremely negative reviews than extremely positive reviews.</td><td>SS</td></tr><tr><td>H2b</td><td>The effect of user-provided photos on review helpfulness is less significant for extremely negative reviews than extremely positive reviews.</td><td>S</td></tr><tr><td>H3a</td><td>The effect of a verified purchase badge on review helpfulness is more significant for extreme reviews on search products than those for experience products.</td><td>SS</td></tr><tr><td>H3b</td><td>The effect of user-provided photos on review helpfulness is more significant for extreme reviews on search products than those for experience products</td><td>S</td></tr><tr><td>H4a</td><td>The effect of a verified purchase badge on review helpfulness is more significant for extreme reviews on tangible products than those for intangible products.</td><td>SS</td></tr><tr><td>H4b</td><td>The effect of user-provided photos on review helpfulness is more significant for extreme reviews on tangible products than those for intangible products.</td><td>S</td></tr></table>

Lastly, because the dataset adopted in this study spans for 23 years, it is possible that the perception of consumers on trust cues could have changed over that time. To examine this potential diference, the proposed hypotheses are tested with two terms of datasets: from May 1996 to July 2007 and from August 2007 to October 2018. As summarised in Table 6, although most of the hypothesis test results remain consistent in the analyses using the two terms of datasets, some notable diferences are observed: the hypotheses related to the efect of user-provided photos, including Hypothesis 2b, Hypothesis 3b, and Hypothesis 4b, are not supported in the test with the first term dataset but are supported with the second term dataset (See, Appendix F for more details).

Given all the hypothesis test results above, it is concluded that Hypothesis 2a, 3a, and 4a are strongly supported, while Hypothesis 1a, 1b, 2b, 3b, and 4b are supported. Table 7 summarises the conclusion for hypothesis test results.

## 8. Discussions and contributions

## 8.1. Summary of findings

This study examined how the efect of trust cues like verified purchase badges and user-provided photos on helpfulness difers by review extremity and how the interaction efect changes by product attributes. The support of Hypotheses 1a and 1b suggests that trust cues are less critical in determining the helpfulness of extreme reviews than that of moderate reviews, although the diferential efect is found to be insignificant for highly helpful reviews with at least ten helpfulness votes. However, the hypotheses should have adequate generalisability, because the reviews with at least ten votes are only 2% of the entire reviews (i.e., 4,332,115 out of 208,533,788). In the comparison between extremely positive and negative reviews, the strong support of Hypothesis 2a suggests that verified purchase badges have a larger efect on the helpfulness of extremely positive reviews than that of extremely negative reviews. As the support of Hypothesis 2b indicates, the efect of user-provided photos on helpfulness is generally greater for extremely positive reviews than extremely negative reviews, even though the diference is negligible for the top 2% of highly helpful reviews.

Concerning the interaction of product types, the efect of trust cues on the helpfulness of extreme reviews is more profound for search products. In particular, Hypothesis 3a, which predicted a more significant efect of verified purchase badges on the helpfulness of extreme reviews on search products, is strongly supported in all the analyses. Even though Hypothesis 3b, postulating a more significant efect of user-provided photos for extreme reviews on search products, is not supported in the initial analysis, the efect is found to be significant in all the robustness check tests with both OLS and negative binomial regressions. Product tangibility is also found to have a positive interaction efect on the relationship between trust cues and the helpfulness of extreme reviews, strongly supporting Hypothesis 4a and supporting Hypothesis 4b. This suggests that when an extreme review is on a tangible product, the positive efect of both types of trust cues is larger than when it is on an intangible product.

Some noteworthy diferences are observed in the hypothesis tests with the two diferent time periods of datasets. The greater efect of user-provided photos on extremely positive reviews (Hypothesis 2b) is not significant for the reviews submitted from May 1996 to July 2007, while significant in those from August 2007 to October 2018. This diference may indicate that at the beginning of the ecommerce age, consumers considered such photos equally important regardless types of online reviews; however, as the number of online reviews available at ecommerce platforms increased, they could have changed their behaviour in evaluating review helpfulness, considering the photos as a more critical trust cue for extremely positive reviews, which are inherently less credible (Metzger & Flanagin, 2015) and acceptable (K. K. Lee & Koo, 2012) than negative reviews. Likewise, the diferential efect of the photos by product types (i.e., Hypothesis 3b and Hypothesis 4b) is found only in the online reviews created between August 2007 and October 2018. This could result from the diversification of product categories in ecommerce platforms. As the product diversity grew in the market, consumers would have realised that the photos are more critical in understanding the potential quality of search or tangible products.

## 8.2. Theoretical contributions

The overall findings of this study confirm that review extremity has a substantial interaction efect on the relationship between trust cues and review helpfulness. The hypothesis test results suggest a weaker influence of trust cues on the helpfulness of extreme reviews than that of moderate reviews. This finding is consistent with the theory of confirmation bias in that consumers are less likely to require evidence for extreme reviews that provide evident support for their pre-existing decisions (Pentina et al., 2018), either to buy or not to buy. Although the finding may be contradictory to the Sagan standard – “Extraordinary claims require extraordinary evidence” – this infers that consumers do not consider extreme reviews as extraordinary, but as ordinary claims in online review communities. This could be plausible in that extreme reviews are more common than moderate reviews, comprising approximately 70% of the entire online reviews (Schoenmueller et al., 2020), and extraordinariness depends on rarity of event (Levine, 2012). Thus, consumers should perceive extreme reviews as common, ordinary claims and accept them with fewer trust cues. This tendency is found to be more profound in extremely negative reviews; trust cues are less influential in determining the helpfulness of extremely negative reviews than that of extremely positive reviews. This corresponds to the extant literature reporting higher perceived credibility (Chang & Wu, 2014) and acceptability (Lee & Koo, 2012) of negative reviews. Due to such inherent advantages, consumers may perceive extremely negative reviews as helpful, even when the reviews have insuficient trust cues.

The primary findings of this study extend the theory of confirmation bias in online review research. First, although a few studies considered the efect of confirmation bias on the perceived helpfulness of online reviews (Sengo Furtado et al., 2021; Yin et al., 2016), research on its possible interaction efect on the relationship between trust cues and review helpfulness is scant. The findings of this study show that confirmation bias would afect the relationship in that consumers consider both types of trust cues as less critical in determining the helpfulness of extreme reviews, which more efectively confirm pre-existing beliefs of consumers. Second, confirmation bias should arise more significantly when consumers confirm their negative initial beliefs because the efect of trust cues on review helpfulness is less substantial for extremely negative reviews than extremely positive reviews. Lastly, with regard to product attributes, the findings of this study suggest that confirmation bias is weaker for extreme reviews on search or tangible products. More specifically, they reveal that consumers consider trust cues more important for the extreme reviews on search products or tangible products, extending the prior studies reporting greater helpfulness of reviews on search products (Sun et al., 2019) and tangible products (Babić Rosario et al., 2016; Choi & Leon, 2020). Consumers should less rely on their initial belief and, hence, pay more attention to trust cues when they read extreme reviews on search products or tangible products, because they evaluate search products more carefully (Luan et al., 2016) and focus more on factual attributes of tangible products (Rossmann et al., 2016).

## 8.3. Practical contributions

This study delivers several important implications for managers and online reviewers of ecommerce platforms. For the managers of ecommerce platforms, the findings suggest practical ideas to cultivate helpful reviews and discover potentially helpful reviews in the platforms. First, the practitioners ought to adopt trust cues and encourage the use of trust cues in their online review system. For instance, they may ofer some rewards or incentives for reviewers who actually purchase the product for review and provide its photos, regardless of product attributes (i.e., search vs. experience, tangible vs. intangible) because trust cues enhance review helpfulness across diferent product categories. Second, review platforms need to encourage the reviewers who rate items at moderate ratings to provide trust cues, because the cues are more important for moderate reviews, which are likely to be less helpful for consumers due to their vagueness (Lee & Choeh, 2014; Wu et al., 2021). For example, the platforms may consider ofering more incentives for moderate reviews with verified purchase badges and user-provided photos. Third, the platforms also may consider displaying only moderate reviews with enough trust cues, because consumers would be less likely to perceive them as helpful when they have no trust cue. Fourth, the efect of trust cues on review helpfulness is weaker for extremely negative reviews than that of extremely positive reviews. This implies that consumers would more likely believe extremely negative reviews than extremely positive reviews even without suficient evidence. Given the higher acceptability (Lee & Koo, 2012) and larger impact on purchase decisions of extremely negative reviews (Chen et al., 2011), online review platforms need to carefully examine the validity of extremely negative reviews. Lastly, product types should be considered in collecting consumer reviews, because trust cues are more influential to the helpfulness of extreme reviews on search or tangible products. For instance, the practitioners ought to solicit reviews from buyers of search or tangible products and provide more rewards for the search or tangible product reviews with user-provided photos.

For online reviewers who want to establish their reputation in online review communities by attaining more helpfulness votes, the greater efect of trust cues on the helpfulness of moderate reviews suggests that adding trust cues is more important for moderate reviews to gain helpfulness votes. In particular, experienced or professional reviewers who tend to contribute moderate reviews (Choi & Maasberg, 2021) should understand this importance. Even when submitting extreme reviews, which are intrinsically perceived as more helpful, reviewers need to include trust cues to support their opinions, if they submit extremely positive reviews or if the reviews are on search or tangible products. However, the efect of trust cues on helpfulness does not significantly difer by review extremity for the reviews with at least ten helpfulness votes, which belong to the top 2% of reviews at Amazon.com. Thus, if reviewers want to create a highly helpful review, simply adding trust cues may not be suficient to make a significant diference between their moderate and extreme reviews.

## 9. Limitations and future research

Although this study contributes to both academia and industry, it has several limitations that can be opportunities for future studies. First, although reviewers’ experience described in textual reviews can be a trust cue providing credibility to the reviews (Fresneda & Gefen, 2020), this study had to limit trust cues to verified purchase badges and userprovided photos, because it was extremely dificul to analyse 31 million textual reviews to determine whether they contain such a textual trust cue. Second, this study was not able to include predictors related to sentiment from textual reviews, which are known to afect review helpfulness (Krishnamoorthy, 2015), due to the extraordinary size of the dataset. Accordingly, this study had to use ratings to define the extremity of reviews, although reviews with mod erate ratings could contain extreme claims in their textual reviews. This could be one of the reasons for the diferent hypothesis test results for the highly helpful reviews with at least ten helpfulness votes. Third, this study used online review data from a single online review platform, Amazon.com. Even though Amazon.com is one of the most representative ecommerce websites with a well-established review system, the findings may not be applicable to other review platforms, such as Yelp.com and Trustpilot.com, which have diferent review ecosys tems. Future research may test similar research ques tions using data from other platforms and compare their findings with those of this study. Fourth, the findings of this study are based on the comparison of correlation coeficients for diferent groups of online reviews, using large secondary data. Future studies may verify the findings of this study with diferen methodologies, such as experiments, to confirm whether consumers consider trust cues diferently in determining review helpfulness. Fifth, regarding user-provided photos, this study examined their efect on review helpfulness only given their pre sence, based on the assumption that the efect of userprovided photos is identical regardless of the quantity or quality of photos. This could be a reason for the insignificant diferential efect of user-provided photos found in the online reviews submitted from 1996 to 2007, when it was more laborious not only to take and upload photos but also to present their features in the photos. Lastly, even though online reviews with user-provided videos are highly rare, there are reviews with the videos in the Amazon reviews. However, this study could not consider the video as another type of trust cue, because it was highly dificult to distinguish them from the videos provided by merchants or manufacturers. Future studies may take account of user-provided videos to tes their efect on review helpfulness and whether review extremity interacts their efect on the helpfulness.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Notes on contributor

Hoon S. Choi is an assistant professor of the Department of Information Technology and Decision Sciences (ITDS) at the University of North Texas. He received his Ph.D. in Business Administration with a concentration in Information Technology at the University of Texas at San Antonio. His research interests include e-commerce, online reviews, digita video games, mobile apps, mobile payment, data analytics, and behavioural information security. Dr. Choi published his papers in the major business journals, such as Journal of Management Information Systems (JMIS), Decision Support Systems (DSS), Information Systems Frontiers, Electronic Markets, Journal of Consumer Marketing, and Journal of Computer Information Systems.

## ORCID

Hoon S. Choi http://orcid.org/0000-0002-0287-206X

## References

Abd-Elaziz, M. E., Aziz, W. M., Khalifa, G. S., & Abdel-Aleem, M. (2015). Determinants of Electronic word of mouth (EWOM) influence on hotel customers’ purchasing decision. International Journal of Heritage, Tourism, and Hospitality, 9(2/2), 194-223. https:// www.researchgate.net/profile/Magdy-Mayouf/publica tion/295551680\_Determinants\_of\_Electronic\_word\_ of\_mouth\_EWOM\_influence\_on\_hotel\_customers'\_ purchasing\_decision/links/56d729f608aebe4638af1901/ Determinants-of-Electronic-word-of-mouth-EWOMinfluence-on-hotel-customers-purchasing-decision.pdf

Aiken, K. D. (2006). Trustmarks, objective-source ratings, and implied investments in advertising: Investigating online trust and the context-specific nature of internet signals. Journal of the Academy of Marketing Science, 34 (3), 308–323. https://doi.org/10.1177/0092070304271004

An, Q., Ma, Y., Du, Q., Xiang, Z., & Fan, W. (2020). Role of user-generated photos in online hotel reviews: An analytical approach. Journal of Hospitality and Tourism Management, 45, 633–640. https://doi.org/10.1016/j. jhtm.2020.11.002

Arndt, S., & Jones, D. S. (2018). Preventing sensationalistic science and fake news about substance use. BioMed Central. 13, 1–3.

Babić Rosario, A., Sotgiu, F., De Valck, K., & Bijmolt, T. H. (2016). The efect of electronic word of mouth on sales: A meta-analytic review of platform, product, and metric factors. Journal of Marketing Research, 53(3), 297–318. https://doi.org/10.1509/jmr.14.0380

Baek, H., Ahn, J., & Choi, Y. (2012). Helpfulness of online consumer reviews: Readers‘ objectives and review cues. International Journal of Electronic Commerce, 17(2), 99–126. https://doi.org/10.2753/ JEC1086-4415170204

Bao, Z., & Chau, M. (2016). A schema-oriented product clustering method using online product reviews. Thirty Seventh International Conference on Information Systems, Dublin, Ireland, (Ed.),^(Eds.). https://core.ac.uk/down load/pdf/301370356.pdf

Barbu, C.-M., Carbonell, G., & Ziegler, J. (2019). The influence of trust cues on the trustworthiness of online reviews for recommendations. Proceedings of the 34th ACM/ SIGAPP symposium on applied computing, (Ed.),^(Eds.).

Bauman, A. A. (2016). Online trust cues: Perceptions and application. Journal of International Technology and Information Management, 25(4), 51–74. https://scholar works.lib.csusb.edu/jitim/vol25/iss4/4/

Beldad, A., De Jong, M., & Steehouder, M. (2010). How shall I trust the faceless and the intangible? A literature review on the antecedents of online trust. Computers in Human Behavior, 26(5), 857–869. https://doi.org/10.1016/j.chb. 2010.03.013

Bente, G., Baptist, O., & Leuschner, H. (2012). To buy or not to buy: Influence of seller photos and reputation on buyer trust and purchase behavior. International Journal of Human-Computer Studies, 70(1), 1–13. https://doi.org 10.1016/j.ijhcs.2011.08.005

Bivens-Tatum, W. (2021). Scholarly conversations, intellectual virtues, and virtue information literacy. Library Philosophy and Practice, 1–30. https://www.proquest. com/docview/2506600091?pq-origsite=gscholar&fromo penview=true

Bjering, E., Havro, L. J., & Moen, Ø. (2015). An empirical investigation of self-selection bias and factors influencing review helpfulness. International Journal of Business and Management, 10(7), 16–30. https://doi.org/10.5539/ijbm. v10n7p16

Brummelman, E., Crocker, J., & Bushman, B. J. (2016). The praise paradox: When and why praise backfires in children with low Self-Esteem. Child Development Perspectives, 10(2), 111–115. https://doi.org/10.1111 cdep.12171

Calantone, R. J., & Vickery, S. K. (2010). Introduction to the special topic forum: Using archival and secondary data sources in supply chain management research. Journal of Supply Chain Management, 46(4), 3. https://doi.org/10. 1111/j.1745-493X.2010.03202.x

Cao, Q., Duan, W., & Gan, Q. (2011). Exploring determinants of voting for the “helpfulness” of online user reviews: A text mining approach. Decision Support Systems, 50(2), 511–521. https://doi.org/10.1016/j.dss. 2010.11.009

Carbonell, G., Barbu, C.-M., Vorgerd, L., Brand, M., & Molnar, A. (2019). The impact of emotionality and trust cues on the perceived trustworthiness of online reviews. Cogent Business & Management, 6(1), 1–14. https://doi. org/10.1080/23311975.2019.1586062

Chang, H. H., & Wu, L. H. (2014). An examination of negative e-WOM adoption: Brand commitment as a moderator. Decision Support Systems, 59, 206–218. https://doi.org/10.1016/j.dss.2013.11.008

Chang, W. S. (2014). The adoption of tech-art in cultural creative derivatives influences on customers’ repurchase behavior. Journal of Convergence Information Technology, 9(2), 181–193. https://www.researchgate.net/publication 266970992\_The\_Adoption\_of\_Tech-Art\_in\_Cultural\_ Creative\_Derivatives\_Influences\_on\_Customers'\_ Repurchase\_Behavior

Chen, Y., Wang, Q., & Xie, J. (2011). Online social interactions: A natural experiment on word of mouth versus observational learning. Journal of Marketing Research, 48(2), 238–254. https://doi.org/10.1509 jmkr.48.2.238

Choi, H. S., & Leon, S. (2020). An empirical investigation of online review helpfulness: A big data perspective. Decision Support Systems, 139, 1–12. https://doi.org/10. 1016/j.dss.2020.113403

Choi, H. S., & Maasberg, M. (2021). An empirical analysis of experienced reviewers in online communities: What, how, and why to review. Electronic Markets, 31(3), 1–18 doi:https://doi.org/10.1007/s12525-021-00499-8 .

Christodoulides, G., Michaelidou, N., & Argyriou, E. (2012). Cross-national diferences in e-WOM influence. European Journal of Marketing, 46(11/12), 1689–1707. https://doi.org/10.1108/03090561211260040

Cui, G., Lui, H.-K., & Guo, X. (2012). The efect of online consumer reviews on new product sales. International Journal of Electronic Commerce, 17(1), 39–58. https:// doi.org/10.2753/JEC1086-4415170102

Desrocher, C., Léger, P.-M., Sénécal, S., Pagé, S.-A., & Mirhoseini, S. (2015). The influence of product type, mathematical complexity, and visual attention on the attitude toward the website: The case of online grocery shopping, Fourteenth Pre-ICIS SIG-HCI Workshop, December 13, 2015, Fortworth, TX USA

Duong, C., Pescetto, G., & Santamaria, D. (2014). How value–glamour investors use financial information: UK evidence of investors’ confirmation bias. The European Journal of Finance, 20(6), 524–549. https://doi.org/10. 1080/1351847X.2012.722117

Engler, T. H., Winter, P., & Schulz, M. (2015). Understanding online product ratings: A customer satisfaction model. Journal of Retailing and Consumer Services, 27, 113–120. https://doi.org/10.1016/j.jretcon ser.2015.07.010

Ezechukwu, N. V. (2020). Consumer-generated reviews: Time for closer scrutiny? Legal Studies, 40(4), 630–650. https://doi.org/10.1017/lst.2020.15

Fan, L., & Zhang, X. (2020). the combination signaling efect of text and image on mobile phone review Helpfulness - The moderating efect of signaling environment. IEEE Access, 8, 122736–122746. https://doi.org/10.1109/ ACCESS.2020.3005951

Fang, A., & Ben-Miled, Z. (2017). Does bad news spread faster? 2017 International Conference on Computing, Networking and Communications (ICNC), (Ed.), ^(Eds.).

Fernandez, J. E. F. (2017). Three Papers on the Role of Information in Online Consumer Reviews. Drexel University.

Filieri, R. (2016). What makes an online consumer review trustworthy? Annals of Tourism Research, 58, 46–64. https://doi.org/10.1016/j.annals.2015.12.019

Forman, C., Ghose, A., & Wiesenfeld, B. (2008). Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Information Systems Research, 19(3), 291–313. https:// doi.org/10.1287/isre.1080.0193

Franke, G. R., Huhmann, B. A., & Mothersbaugh, D. L. (2004). Information content and consumer readership of print ads: A comparison of search and experience products. Journal of the Academy of Marketing Science, 32(1), 20–31. https://doi.org/10.1177/0092070303257856

Fresneda, J. E., & Gefen, D. (2020). Gazing at the stars is not enough, look at the specific word entropy, too! Information & Management, 57(8), 103388. https://doi. org/10.1016/j.im.2020.103388

Gabris, G. T., & Mitchell, K. (1988). The impact of merit raise scores on employee attitudes: The Matthew efect of performance appraisal. Public Personnel Management, 17 ( 4 ) , 3 6 9 – 3 8 6 . h t t p s : / / d o i . o r g / 1 0 . 1 1 7 7 / 009102608801700403

Gao, B., Hu, N., & Bose, I. (2017). Follow the herd or be myself? An analysis of consistency in behavior of reviewers and helpfulness of their reviews. Decision Support Systems, 95, 1–11. https://doi.org/10.1016/j.dss.2016.11.005

Ghose, A., & Ipeirotis, P. G. (2011). Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions on Knowledge and Data Engineering, 23(10), 1498–1512. https://doi.org/10.1109/TKDE.2010.188

Gillispie, C. C., Gratton-Guinness, I., & Fox, R. (1999). Pierre Simon Laplace, A Life in Exact Science. Princeton University Press.

Girard, T., & Dion, P. (2010). Validating the search, experience, and credence product classification framework. Journal of Business Research, 63(9–10), 1079–1087. https://doi.org/10.1016/j.jbusres.2008.12.011

Hansen, T., & Jensen, J. M. (2009). Shopping orientation and online clothing purchases: The role of gender and purchase situation. European Journal of Marketing, 43(9/ 1 0 ) , 1 1 5 4 – 1 1 7 0 . h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 / 03090560910976410

Hao, Y., Ye, Q., Li, Y., & Cheng, Z. (2010). How does the valence of online consumer reviews matter in consumer decision making? Diferences between search goods and experience goods. 2010 43rd Hawaii international conference on system sciences, (Ed.),^(Eds.).

Hauter, J. (2021). Forensic conflict studies: Making sense of war in the social media age. Media, War & Conflict, 17506352211037325 https://doi.org/10.1177/ 17506352211037325 .

He, J., Wang, X., Vandenbosch, M. B., & Nault, B. R. (2020). Revealed preference in online reviews: Purchase verification in the tablet market. Decision Support Systems, 132, 1–10. https://doi.org/10.1016/j.dss.2020.113281

Hellén, K., & Gummerus, J. (2013). Re-investigating the nature of tangibility/intangibility and its influence on consumer experiences. Journal of Service Management, 2 4 ( 2 ) , 1 3 0 – 1 5 0 . h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 09564231311323935

Hergovich, A., Schott, R., & Burger, C. (2010). Biased evaluation of abstracts depending on topic and conclusion: Further evidence of a confirmation bias within scientific psychology. Current Psychology, 29(3), 188–209. https:// doi.org/10.1007/s12144-010-9087-5

Hesse, M. (2021). Essays on trust and reputation portability in digital platform ecosystems (Technische Universität Berlin). https://www.depositonce.tu-berlin.de/handle/11303/12879

Hilton, B., Choi, C. J., & Chen, S. (2004). The ethics of counterfeiting in the fashion industry: Quality, credence and profit issues. Journal of Business Ethics, 55(4), 343–352. https://doi.org/10.1007/s10551-004-0989-8

Hlee, S., Lee, H., & Koo, C. (2018). Hospitality and tourism online review research: A systematic analysis and heuristic-systematic model. Sustainability, 10(4), 1141. https://doi.org/10.3390/su10041141

Hoferth, S. L. (2005). Secondary data analysis in family research. Journal of Marriage and Family, 67(4), 891–907. https://doi.org/10.1111/j.1741-3737.2005.00182.x

Hong, H., Xu, D., Wang, G. A., & Fan, W. (2017). Understanding the determinants of online review helpfulness: A meta-analytic investigation. Decision Support Systems, 102, 1–11. https://doi.org/10.1016/j.dss.2017.06.007

Hornik, J., Satchi, R. S., Cesareo, L., & Pastore, A. (2015). Information dissemination via electronic word-ofmouth. Good News Travels Fast, Bad News Travels Faster! Computers in Human Behavior, 45, 273–280. https://doi.org/10.1016/j.chb.2014.11.008

Hu, N., Pavlou, P. A., & Zhang, J. J. (2009). Why do online product reviews have a J-shaped distribution? Overcoming biases in online word-of-mouth communication. Communications of the ACM, 52(10), 144–147. https://doi.org/10.1145/1562764.1562800

Hu, Y.-H., Chen, K., & Lee, P.-J. (2017). The efect of user-controllable filters on the prediction of online hote reviews. Information & Management, 54(6), 728–744. https://doi.org/10.1016/j.im.2016.12.009

Huang, P., Lurie, N. H., & Mitra, S. (2009). Searching for experience on the web: An empirical examination of consumer behavior for search and experience goods. Journal of Marketing, 73(2), 55–69. https://doi.org/10.1509/jmkg.73.2. 55

Huang, J., Boh, W. F., & Goh, K. H. (2011). From A Social Influence Perspective: The Impact Of Social Media On Movie Sales. PACIS. (Ed.),^(Eds.).

Huang, L., Tan, C.-H., Ke, W., & Wei, -K.-K. (2013). Comprehension and assessment of product reviews: A review-product congruity proposition. Journal of Management Information Systems, 30(3), 311–343. https://doi.org/10.2753/MIS0742-1222300311

Huang, Y., Li, C., Wu, J., & Lin, Z. (2018). Online customer reviews and consumer evaluation: The role of review font. Information & Management, 55(4), 430–440. https://doi. org/10.1016/j.im.2017.10.003

Hutagaol, R. M., & Basbeth, F. (2021). The relationship between service quality and consumer satisfaction link: does perceived value have a mediating efect?: An evidence from mutual fund company in Jakarta. Emerging Markets: Business and Management Studies Journal, 8(2), 125–135. https://doi.org/10.33555/embm.v8i2.183

Jauhari, M. T. (2018). The impact of website quality on consumer satisfaction and purchase intention (study case of e-commerce Lazada Indonesia in Malang city). Universitas Brawijaya.

Kahneman, D., Lovallo, D., & Sibony, O. (2011). Before you make that big decision Harvard Business Review 51–60 .

Kaushik, K., Mishra, R., Rana, N. P., & Dwivedi, Y. K. (2018). Exploring reviews and review sequences on e-commerce platform: A study of helpful reviews on Amazon. Journal of Retailing and Consumer Services, 45, 21–32. https://doi.org/10.1016/j.jretconser.2018.08. 002

Kim, S. J., Maslowska, E., & Malthouse, E. C. (2018). Understanding the efects of diferent review features on purchase probability. International Journal of Advertising, 37(1), 29–53. https://doi.org/10.1080/02650487.2017. 1340928

Klayman, J., & Ha, Y.-W. (1987). Confirmation, disconfirmation, and information in hypothesis testing. Psychological Review, 94(2), 211–228. https://doi.org/10. 1037/0033-295X.94.2.211

Klein, L. R. (1998). Evaluating the potential of interactive media through a new lens: Search versus experience goods. Journal of Business Research, 41(3), 195–203. https://doi.org/10.1016/S0148-2963(97)00062-3

Knobloch-Westerwick, S., Mothes, C., & Polavin, N. (2020). Confirmation bias, ingroup bias, and negativity bias in selective exposure to political information. Communication Research, 47(1), 104–124. https://doi. org/10.1177/0093650217719596

Koh, N. S., Hu, N., & Clemons, E. K. (2010). Do online reviews reflect a product’s true perceived quality? An investigation of online movie reviews across cultures. Electronic Commerce Research and Applications, 9(5), 374–385. https://doi.org/10.1016/j.elerap.2010.04.001

Kokkodis, M., & Lappas, T. (2016). The relationship between disclosing purchase information and reputation systems in electronic markets. Thirty Seventh international conference on information systems, Dublin, Ireland, (Ed.),^(Eds.).

Koop, G. (2005). Analysis of economic data. John Wiley & Sons. Kramer, R. M., & Lewicki, R. J. (2010). Repairing and enhancing trust: Approaches to reducing organizational trust deficits. Academy of Management Annals, 4(1), 245–277. https://doi.org/10.5465/19416520.2010.487403

Krishnamoorthy, S. (2015). Linguistic features for review helpfulness prediction. Expert Systems with Applications, 42(7), 3751–3759. https://doi.org/10.1016/j.eswa.2014.12.044

Lafky, J. (2014). Why do people rate? Theory and evidence on online ratings. Games and Economic Behavior, 87, 554–570. https://doi.org/10.1016/j.geb.2014.02.008

Lallement, J., Dejean, S., Euzéby, F., & Martinez, C. (2020). The interaction between reputation and information search: Evidence of information avoidance and confirmation bias. Journal of Retailing and Consumer Services, 53, 1–10. https://doi.org/10.1016/j.jretconser. 2019.03.014

Lee, K., & Koo, D. (2012). Efects of attribute and valence of e-WOM on message adoption: Moderating roles of subjective knowledge and regulatory focus. Computers in Human Behavior, 28(5), 1974–1984. https://doi.org/10. 1016/j.chb.2012.05.018

Lee, E.-J., & Shin, S. Y. (2014). When do consumers buy online product reviews? Efects of review quality, product type, and reviewer’s photo. Computers in Human Behavior, 31, 356–366. https://doi.org/10.1016/j.chb.2013.10.050

Lee, S., & Choeh, J. Y. (2014). Predicting the helpfulness of online reviews using multilayer perceptron neural networks. Expert Systems with Applications, 41(6), 3041–3046. https://doi.org/10.1016/j.eswa.2013.10.034

Lee, S., & Choeh, J. Y. (2018). The interactive impact of online word-of-mouth and review helpfulness on box ofice revenue. Management Decision, 56(4), 849–866. https://doi.org/10.1108/MD-06-2017-0561

Lehner, P. E., Adelman, L., Cheikes, B. A., & Brown, M. J. (2008). Confirmation bias in complex analyses. IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans, 38(3), 584–592. https://doi.org/10. 1109/TSMCA.2008.918634

Levine, M. (2012). Hume and the problem of miracles: A solution. Springer Netherlands.

Li, H., Xie, K. L., & Zhang, Z. (2020). The efects of consumer experience and disconfirmation on the timing of online review: Field evidence from the restaurant business. International Journal of Hospitality Management, 84, 102344. https://doi.org/10.1016/j.ijhm.2019.102344

Li, C., Kwok, L., Xie, K. L., Liu, J., & Ye, Q. (2021). Let photos speak: The efect of user-generated visual content on hotel review helpfulness. Journal of Hospitality & Tourism Research, 10963480211019113. https://doi.org 10.1177/10963480211019113

Liang, T.-P., Cheng, J. C., Saini, V., & Hsu, J. S.-C. (2021). Is being helpful good enough for online reviews? Exploring the role of information credibility and data source throught meta-analysis. Journal of Electronic Commerce Research, 22(4), 336–362 http://www.jecr.org/sites default/files/2021vol22no4\_Paper5.pdf .

Liu, T. C., Wang, C. Y., & Wu, L. W. (2010). Moderators of the negativity efect: Commitment, identification, and consumer sensitivity to corporate social performance. Psychology & Marketing, 27(1), 54–70. https://doi.org/10.1002/mar.20319

Liu, Q., Huang, S., & Zhang, L. (2016). The influence of information cascades on online purchase behaviors of search and experience products. Electronic Commerce Research, 16(4), 553–580. https://doi.org/10.1007/ s10660-016-9220-0

Lu, S., Wu, J., & Tseng, S.-L. A. (2018). How online reviews become helpful: A dynamic perspective. Journal of Interactive Marketing, 44, 17–28. https://doi.org/10.1016/j. intmar.2018.05.005

Luan, J., Yao, Z., Zhao, F., & Liu, H. (2016). Search product and experience product online reviews: An eye-tracking study on consumers’ review search behavior. Computers in Human Behavior, 65, 420–430. https://doi.org/10.1016/j.chb.2016. 08.037

Luca, M., & Zervas, G. (2016). Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Science, 62(12), 3412–3427. https://doi.org/10. 1287/mnsc.2015.2304

Luo, L., Duan, S., Shang, S., & Pan, Y. (2021). What makes a helpful online review? Empirical evidence on the efects of review and reviewer characteristics. Online Information Review, 45(3), 614–632. https://doi.org/10.1108/OIR-05- 2020-0186

Ma, Y., Xiang, Z., Du, Q., & Fan, W. (2018). Efects of user-provided photos on hotel review helpfulness: An analytical approach with deep leaning. International Journal of Hospitality Management, 71, 120–131. https:// doi.org/10.1016/j.ijhm.2017.12.008

Mansfield, E. R., & Helms, B. P. (1982). Detecting multicollinearity. The American Statistician, 36(3a), 158–160. https://doi.org/10.1080/00031305.1982. 10482818

Maslowska, E., Malthouse, E. C., & Viswanathan, V. (2017). Do customer reviews drive purchase decisions? The moderating roles of review exposure and price. Decision Support Systems, 98, 1–9. https://doi.org/10.1016/j.dss.2017.03.010

Metzger, M. J., & Flanagin, A. J. (2015). Psychological approaches to credibility assessment online. The Handbook of the Psychology of Communication Technology, 32, 445–466. https://doi.org/10.1002/ 9781118426456.ch20

Mittal, B. (1999). The advertising of services: Meeting the challenge of intangibility. Journal of Service Research, 2(1), 98–116. https://doi.org/10.1177/ 109467059921008

Mudambi, S. M., & Schuf, D. (2010). Research note: What makes a helpful online review? A study of customer reviews on Amazon. com. MIS Quarterly, 34(1), 185–200. https://doi.org/10.2307/20721420

Nakayama, M., Sutclife, N., & Wan, Y. (2010). Has the web transformed experience goods into search goods? Electronic Markets, 20(3–4), 251–262. https://doi.org/10. 1007/s12525-010-0041-z

Naser, K., Nuseibeh, R., & Al-Hadeya, A. (2013). Factors influencing corporate working capital management: Evidence from an emerging economy. Journal of Contemporary Issues in Business Research, 2(1), 11–30. https://citeseerx.ist.psu.edu/viewdoc/download?doi=10. 1.1.278.4754&rep=rep1&type=pdf

Nevo, A. (2011). Empirical models of consumer behavior. Annual Review of Economics, 3(1), 51–75. https://doi.org/ 10.1146/annurev-economics-061109-080402

Ni, J., Li, J., & McAuley, J. (2019). Justifying recommendations using distantly-labeled reviews and fine-grained aspects. Proceedings of the 2019 conference on empirical

methods in natural language processing and the 9th inter national joint conference on natural language processing (EMNLP-IJCNLP), (Ed.),^(Eds.).

Park, J., Konana, P., Gu, B., Kumar, A., & Raghunathan, R. (2013). Information valuation and confirmation bias in virtual communities: Evidence from stock message boards. Information Systems Research, 24(4), 1050–1067. https://doi.org/10.1287/isre.2013.0492

Park, S., & Nicolau, J. L. (2015). Asymmetric efects of online consumer reviews. Annals of Tourism Research, 50, 67–83. https://doi.org/10.1016/j.annals.2014.10.007

Pentina, I., Bailey, A. A., & Zhang, L. (2018). Exploring efects of source similarity, message valence, and receiver regulatory focus on yelp review persuasiveness and purchase intentions. Journal of Marketing Communications, 24(2), 125–145. https://doi.org/10.1080/13527266.2015.1005115

Petrescu, M., O’Leary, K., Goldring, D., & Mrad, S. B. (2018). Incentivized reviews: Promising the moon for a few stars. Journal of Retailing and Consumer Services, 41, 288–295. https://doi.org/10.1016/j.jretconser.2017.04.005

Pfeufer, A., & Phua, J. (2021). Stranger danger? Cue-based trust in online consumer product review videos. International Journal of Consumer Studies, 46, 3. https:/ doi.org/10.1111/ijcs.12740

Qazi, A., Syed, K. B. S., Raj, R. G., Cambria, E., Tahir, M., & Alghazzawi, D. (2016). A concept-level approach to the analysis of online review helpfulness. Computers in Human Behavior, 58, 75–81. https://doi.org/10.1016/j.chb.2015.12. 028

Racherla, P., & Friske, W. (2012). Perceived ‘usefulness’ of online consumer reviews: An exploratory investigation across three services categories. Electronic Commerce Research and Applications, 11(6), 548–559. https://doi. org/10.1016/j.elerap.2012.06.003

Reimer, T., & Benkenstein, M. (2016). When good WOM hurts and bad WOM gains: The efect of untrustworthy online reviews. Journal of Business Research, 69(12), 5993–6001. https://doi.org/10.1016/j.jbusres.2016.05.014

Robinson, C. D., Tomek, S., & Schumacker, R. (2013). Tests of moderation efects: Diference in simple slopes versus the interaction term. Multiple Linear Regression Viewpoints, 39 (1), 16–24. http://www.glmj.org/archives/articles/Robinson\_ v39n1.pdf

Rossmann, A., Ranjan, K. R., & Sugathan, P. (2016). Drivers of user engagement in eWoM communication. Journal of Services Marketing, 30(5), 541–553. https://doi.org/10.1108 JSM-01-2015-0013

Roth, A., Gray, J., Shockley, J., & Weng, -H.-H. R. (2015). The use of secondary source data for measuring performance in operations management research. Available at SSRN 2271202.

Sacha, D., Senaratne, H., Kwon, B. C., Ellis, G., & Keim, D. A. (2015). The role of uncertainty, awareness, and trust in visual analytics. IEEE Transactions on Visualization and Computer Graphics, 22(1), 240–249. https://doi.org/10.1109/TVCG.2015.2467591

Salehan, M., & Kim, D. J. (2016). Predicting the performance of online consumer reviews: A sentiment mining approach to big data analytics. Decision Support Systems, 81, 30–40. https://doi.org/10.1016/j. dss.2015.10.006

Schoenmueller, V., Netzer, O., & Stahl, F. (2020). The polarity of online reviews: Prevalence, drivers and implications. Journal of Marketing Research, 57(5), 853–877. https://doi.org/10.1177/0022243720941832

Sengo Furtado, F., Reutterer, T., & Schröder, N. (2021). The carrot and the stick in online reviews: Determinants of un-/ helpfulness voting choices. Journal of Business Economics, 92, 1–26. https://doi.org/10.1007/s11573-021-01044-x

Shin, E., Chung, T., & Damhorst, M. L. (2020). Are negative and positive reviews regarding apparel fit influential? Journal of Fashion Marketing and Management: An International Journal, 25, 1. https://doi.org/10.1108/JFMM-02-2020-0027

Siering, M., & Muntermann, J. (2013). What drives the helpfulness of online product reviews? From stars to facts and emotions. Eleventh international conference on wirtschaftsinformatik, Leipzig, Germany. (Ed.),^(Eds.).

Siering, M., Muntermann, J., & Rajagopalan, B. (2018). Explaining and predicting online review helpfulness: The role of content and reviewer-related signals. Decision Support Systems, 108, 1–12. https://doi.org/10.1016/j.dss. 2018.01.004

Sun, X., Han, M., & Feng, J. (2019). Helpfulness of online reviews: Examining review informativeness and classification thresholds by search products and experience products. Decision Support Systems, 124, 1–11. https://doi.org/10.1016/ j.dss.2019.113099

Talluri, B. C., Urai, A. E., Tsetsos, K., Usher, M., & Donner, T. H. (2018). Confirmation bias through selective overweighting of choice-consistent evidence. Current Biology, 28(19), 3128–3135. e3128. https://doi.org/10.1016/ j.cub.2018.07.052

Tan, T. F., & Netessine, S. (2009). Is Tom Cruise threatened? Using Netflix Prize data to examine the long tail of electronic commerce. In Wharton business schoollUniversity of Pennsylvania, Philadephia, 1–37. https://citeseerx.ist.psu. edu/viewdoc/versions?doi=10.1.1.190.8007

Tang, M.-C., & Wu, P.-M. (2021). Reconciling the efects of positive and negative electronic word of mouth: Roles of confirmation bias and involvement. Online Information Review, 46(1), 114–133. https://doi.org/10.1108/OIR-01- 2020-0026

Tressoldi, P. E. (2011). Extraordinary claims require extraordinary evidence: The case of non-local perception, a classical and Bayesian review of evidences. Frontiers in Psychology, 2(117), 1–5. https://doi.org/10.3389/fpsyg. 2011.00117

Trope, Y., & Bassok, M. (1982). Confirmatory and diagnosing strategies in social information gathering. Journal of Personality and Social Psychology, 43(1), 22–34. https:// doi.org/10.1037/0022-3514.43.1.22

Unger, S., & Rollins, M. (2021). Do not believe everything about science online: Revisiting the fake pacific northwest tree octopus in an introductory biology college course. Science Education International, 32(2), 159–163. https:// doi.org/10.33828/sei.v32.i2.9

van der Werf, L., & Buckley, F. (2017). Getting to know you: A longitudinal examination of trust cues and trust development during socialization. Journal of Management, 43(3), 742–770. https://doi.org/10.1177/ 0149206314543475

Van Dijk, T. K., Datema, F., Welten, S., & Van de Vijver, F. J. (2009). Acquiescence and extremity in cross-national surveys: Domain dependence and country-level correlates. The international association for cross-cultural psychology conferences, (Ed.),^ (Eds.).

Wan, Y., Nakayama, M., & Sutclife, N. (2012). The impact of age and shopping experiences on the classification of search, experience, and credence goods in

online shopping. Information Systems and e-Business Management, 10(1), 135–148. https://doi.org/10.1007 s10257-010-0156-y

Wang, Q. (2020). A study of amazon customer review helpfulness using machine learning. https://cdr.lib.unc.edu concern/masters\_papers/p5547x83n

Wang, Y., & song, J. (2020). Image or Text: Which one is more influential? A deep-learning approach for visual and textual data analysis in the digital economy. Communications of the Association for Information Systems, 47(1), 165–187. https:// doi.org/10.17705/1CAIS.04708

Wooldridge, J. M. (2015). Introductory econometrics: A modern approach. Cengage learning.

Wu, P. F. (2013). In search of negativity bias: An empirical study of perceived helpfulness of online reviews. Psychology & Marketing, 30(11), 971–984. https://doi.org/10.1002/mar. 20660

Wu, R., Wu, H. H., & Wang, C. L. (2021). Why is a picture ‘worth a thousand words’? Pictures as information in perceived helpfulness of online reviews. International Journal of Consumer Studies, 45(3), 364–378. https://doi.org/10.1111 ijcs.12627

Yen, C.-L. A., & Tang, C.-H.-H. (2015). Hotel attribute performance, eWOM motivations, and media choice. International Journal of Hospitality Management, 46, 79–88. https://doi.org/10.1016/j. ijhm.2015.01.003

Yin, D., Mitra, S., & Zhang, H. (2016). Research note —When do consumers value positive vs. negative reviews? An empirical investigation of confirmation bias in online word of mouth. Information Systems Research, 27(1), 131–144. https://doi.org/10.1287/isre. 2015.0617

Yip, P. S., & Tsang, E. W. (2007). Interpreting dummy variables and their interaction efects in strategy research. Strategic Organization, 5(1), 13–30. https://doi. org/10.1177/1476127006073512

Zhang, H., Gursoy, D., & Xu, H. (2017). The efects of associative slogans on tourists’ attitudes and travel intention: The moderating efects of need for cognition and familiarity. Journal of Travel Research, 56(2), 206–220. https://doi.org/10.1177/0047287515627029

Zhao, C., Wang, C. A., Wang, Z., & Song, J. (2021). The efect of sentiment across dimensions on the review helpfulness. Peking University.

Zhou, S., & Guo, B. (2017). The order efect on online review helpfulness: A social influence perspective. Decision Support Systems, 93, 77–87. https://doi.org/10.1016/j.dss. 2016.09.016

Zhu, L., Yin, G., & He, W. (2014). Is this opinion leader’s review useful? Peripheral cues for online review helpfulness. Journal of Electronic Commerce Research, 15(4), 267–280. http://www.jecr.org/sites/default/files/15\_4\_ p01.pdf

## Appendix A. Summary of the Number of Reviews by Product Category

Table A1. The number of reviews by product category.

<table><tr><td>Product</td><td>Number of Reviews</td><td>Product</td><td>Number of Reviews</td></tr><tr><td>Automotive</td><td>750,062</td><td>Kindle Store</td><td>760,761</td></tr><tr><td>Beauty</td><td>90,909</td><td>Movies &amp; TV</td><td>1,376,998</td></tr><tr><td>Luxury Beauty</td><td>93,886</td><td>Musical Instruments</td><td>246,463</td></tr><tr><td>Books</td><td>10,155,115</td><td>Office Products</td><td>395,446</td></tr><tr><td>Cell phones &amp; Accessories</td><td>854,146</td><td>Industrial &amp; Scientific</td><td>197,656</td></tr><tr><td>Fashion</td><td>2,585,722</td><td>Pet Supplies</td><td>703,680</td></tr><tr><td>Digital Music</td><td>1,159,629</td><td>Sports &amp; Outdoors</td><td>1,599,920</td></tr><tr><td>Electronics</td><td>2,633,192</td><td>Tools &amp; Home Improvement</td><td>1,056,646</td></tr><tr><td>Appliance</td><td>38,729</td><td>Video Games</td><td>387,948</td></tr><tr><td>Grocery &amp; Gourmet Food</td><td>604,260</td><td>Toys &amp; Games</td><td>927,766</td></tr><tr><td>Prime Pantry</td><td>37,457</td><td>Gift Cards</td><td>5,932</td></tr><tr><td>Home &amp; Kitchen</td><td>3,787,447</td><td>Magazine Subscriptions</td><td>21,526</td></tr><tr><td>Arts, Crafts, &amp; Sewing</td><td>281,933</td><td>Software</td><td>137,002</td></tr></table>

## Appendix B. Product Categorisation Scheme

Table B1. Search and Experience Products (S: Search, E: Experience).

<table><tr><td>Product</td><td>Type</td><td>Reference</td><td>Product</td><td>Type</td><td>Reference</td></tr><tr><td>Automotive</td><td>E</td><td>Huang et al. (2009)</td><td>Kindle Store</td><td>S</td><td>Nakayama et al. (2010)</td></tr><tr><td rowspan="2">Beauty</td><td rowspan="2">E</td><td>Huang et al. (2009)</td><td>Movies &amp; TV</td><td>E</td><td>J. Huang et al. (2011)</td></tr><tr><td>Hao et al. (2010)</td><td></td><td></td><td></td></tr><tr><td>Luxury Beauty</td><td>E</td><td>Huang et al. (2009)</td><td>Musical Instruments</td><td>E</td><td>Nakayama et al. (2010)</td></tr><tr><td>Books</td><td>S</td><td>Wan et al. (2012)</td><td>Office Products</td><td>S</td><td>Wang (2020)</td></tr><tr><td rowspan="2">Cell phones &amp; Accessories</td><td rowspan="2">E</td><td>Wan et al. (2012)</td><td>Industrial &amp; Scientific</td><td>S</td><td>Fernandez (2017)</td></tr><tr><td>Girard and Dion (2010)</td><td></td><td></td><td></td></tr><tr><td>Fashion</td><td>E</td><td>Hansen and Jensen (2009)</td><td>Pet Supplies</td><td>E</td><td>Franke et al. (2004)</td></tr><tr><td>Digital Music</td><td>E</td><td>Mudambi and Schuff (2010)</td><td>Sports &amp; Outdoors</td><td>S</td><td>Bao and Chau (2016)</td></tr><tr><td>Electronics</td><td>S</td><td>Mudambi and Schuff (2010) Klein (1998)</td><td>Tools &amp; Home Improvement</td><td>S</td><td>Bao and Chau (2016)</td></tr><tr><td>Appliance</td><td>S</td><td>Klein (1998)</td><td>Video Games</td><td>E</td><td>Mudambi and Schuff (2010) Lee et. al. (2014)</td></tr><tr><td>Grocery &amp; Gourmet Food</td><td>E</td><td>Desrocher et al. (2015)</td><td>Toys &amp; Games</td><td>E</td><td>Hilton et al. (2004)</td></tr><tr><td>Prime Pantry</td><td>E</td><td>Desrocher et al. (2015)</td><td>Gift Cards</td><td>S</td><td>N/A</td></tr><tr><td>Home &amp; Kitchen</td><td>S</td><td>Huang et al. (2009)</td><td>Magazine Subscriptions</td><td>S</td><td>N/A</td></tr><tr><td>Arts, Crafts, &amp; Sewing</td><td>E</td><td>Chang (2014)</td><td>Software</td><td>E</td><td>Klein (1998)</td></tr></table>

## Appendix C. Control Variables

Table C1. Control variables.

<table><tr><td>Category</td><td>Variable</td><td>Operationalisation</td><td>Reference</td></tr><tr><td rowspan="3">Review Factor</td><td>Review Depth</td><td>Number of words in a review without counting spaces and special characters</td><td>Siering et al. (2018)</td></tr><tr><td>Review Inconsistency</td><td>Absolute difference of a rating from the average rating of the product</td><td>Forman et al. (2008)</td></tr><tr><td>Days Lapsed</td><td>Number of days a review has been available for consumers</td><td>Racherla and Friske (2012)</td></tr><tr><td rowspan="2">Reviewer Factors</td><td>Reviewer Expertise</td><td>Cumulative helpfulness votes attained by a reviewer</td><td>Choi and Leon (2020)</td></tr><tr><td>Reviewer Experience</td><td>Number of reviews generated by a reviewer</td><td>Gao et al. (2017)</td></tr><tr><td rowspan="2">Context Factors</td><td>Product Satisfaction</td><td>Average star rating of a product</td><td>Engler et al. (2015)</td></tr><tr><td>Product Popularity</td><td>Number of ratings for a product</td><td>Maslowska et al. (2017).</td></tr></table>

## Appendix D. Robustness Check – OLS Regressions

Table D1. OLS Regression for Hypothesis 1a, 1b, 2a, and 2b (\*\* $\mathsf { p } < 0 . 0 1 , \mathsf { \Phi } ^ { \ast } \mathsf { p } < 0 . 0 5 ) .$

<table><tr><td rowspan="2" colspan="2">Dependent: Ln(Review Helpfulness)</td><td colspan="3">H1a &amp; H1b</td><td colspan="3">H2a &amp; H2b</td></tr><tr><td>Moderate Reviews</td><td>Extreme Reviews</td><td>Diff.</td><td>Ext. Positive Reviews</td><td>Ext. Negative Reviews</td><td>Diff.</td></tr><tr><td rowspan="2">Vote ≥ 2</td><td>Verified Purchase</td><td>0.083**</td><td>0.051**</td><td>0.032*</td><td>0.072**</td><td>-0.001</td><td>0.073*</td></tr><tr><td>User-Provided Photo</td><td>0.393**</td><td>0.360**</td><td>0.033*</td><td>0.382**</td><td>0.312**</td><td>0.070*</td></tr><tr><td rowspan="2">Vote ≥ 5</td><td>Verified Purchase</td><td>0.075**</td><td>0.063**</td><td>0.012**</td><td>0.081**</td><td>0.023**</td><td>0.058**</td></tr><tr><td>User-Provided Photo</td><td>0.233**</td><td>0.213**</td><td>0.020**</td><td>0.221**</td><td>0.196**</td><td>0.025**</td></tr><tr><td rowspan="2">Vote ≥ 10</td><td>Verified Purchase</td><td>0.069**</td><td>0.071**</td><td>0.002</td><td>0.082**</td><td>0.041**</td><td>0.041**</td></tr><tr><td>User-Provided Photo</td><td>0.148**</td><td>0.142**</td><td>0.006</td><td>0.141**</td><td>0.140**</td><td>0.001</td></tr></table>

Table D2. OLS Regression for Hypothesis 3a, 3b, 4a, and 4b $( ^ { \ast \ast } \mathfrak { p } < 0 . 0 1 , ^ { \ast } \mathfrak { p } < 0 . 0 5 )$

<table><tr><td rowspan="2" colspan="2">Dependent: Ln(Review Helpfulness)</td><td colspan="3">H3a &amp; H3b</td><td colspan="3">H4a &amp; H4b</td></tr><tr><td>Ext. Review for Search</td><td>Ext. Review for Experience</td><td>Diff.</td><td>Ext. Review for Tangible</td><td>Ext. Review for Intangible</td><td>Diff.</td></tr><tr><td rowspan="2">Vote ≥ 2</td><td>Verified Purchase</td><td>0.054*</td><td>0.041*</td><td>0.014*</td><td>0.055*</td><td>0.019*</td><td>0.036*</td></tr><tr><td>User-Provided Photo</td><td>0.362*</td><td>0.364*</td><td>0.002</td><td>0.365*</td><td>0.210*</td><td>0.155*</td></tr><tr><td rowspan="2">Vote ≥ 5</td><td>Verified Purchase</td><td>0.066**</td><td>0.049**</td><td>0.017**</td><td>0.070**</td><td>0.022**</td><td>0.048**</td></tr><tr><td>User-Provided Photo</td><td>0.225**</td><td>0.201**</td><td>0.023**</td><td>0.215**</td><td>0.127**</td><td>0.088**</td></tr><tr><td rowspan="2">Vote ≥ 10</td><td>Verified Purchase</td><td>0.073**</td><td>0.051**</td><td>0.021**</td><td>0.078**</td><td>0.025**</td><td>0.053**</td></tr><tr><td>User-Provided Photo</td><td>0.158**</td><td>0.119**</td><td>0.038**</td><td>0.142**</td><td>0.105**</td><td>0.037**</td></tr></table>

## Appendix E. Robustness Check – Negative Binomial Regressions

Table E1. Negative Binomial Regression for Hypothesis 1a, 1b, 2a, and 2b (\*\* $\mathsf { p } < 0 . 0 1 , \mathsf { \Phi } ^ { \ast } \mathsf { p } < 0 . 0 5 ) .$

<table><tr><td rowspan="2" colspan="2">Dependent: Review Helpfulness</td><td colspan="3">H1a &amp; H1b</td><td colspan="3">H2a &amp; H2b</td></tr><tr><td>Moderate Reviews</td><td>Extreme Reviews</td><td>Diff.</td><td>Ext. Positive Reviews</td><td>Ext. Negative Reviews</td><td>Diff.</td></tr><tr><td rowspan="2">Vote ≥ 2</td><td>Verified Purchase</td><td>0.123**</td><td>0.113**</td><td>0.010**</td><td>0.113**</td><td>0.020**</td><td>0.094**</td></tr><tr><td>User-Provided Photo</td><td>0.462**</td><td>0.442**</td><td>0.020**</td><td>0.442**</td><td>0.328**</td><td>0.114**</td></tr><tr><td rowspan="2">Vote ≥ 5</td><td>Verified Purchase</td><td>0.099**</td><td>0.085**</td><td>0.014**</td><td>0.103**</td><td>0.040**</td><td>0.063**</td></tr><tr><td>User-Provided Photo</td><td>0.261**</td><td>0.233**</td><td>0.028**</td><td>0.238**</td><td>0.208**</td><td>0.030**</td></tr><tr><td rowspan="2">Vote ≥ 10</td><td>Verified Purchase</td><td>0.083**</td><td>0.086**</td><td>0.003</td><td>0.097**</td><td>0.052**</td><td>0.045**</td></tr><tr><td>User-Provided Photo</td><td>0.156**</td><td>0.147**</td><td>0.009*</td><td>0.144**</td><td>0.141**</td><td>0.003</td></tr></table>

Table E2. Negative Binomial Regression for Hypothesis 3a, 3b, 4a, and 4b $( ^ { * * } \mathfrak { p } < 0 . 0 1 , ^ { * } \mathfrak { p } < 0 . 0 5 ) .$

<table><tr><td rowspan="2" colspan="2">Dependent: Review Helpfulness</td><td colspan="3">H3a &amp; H3b</td><td colspan="3">H4a &amp; H4b</td></tr><tr><td>Ext. Review for Search</td><td>Ext. Review for Experience</td><td>Diff.</td><td>Ext. Review for Tangible</td><td>Ext. Review for Intangible</td><td>Diff.</td></tr><tr><td rowspan="2">Vote ≥ 2</td><td>Verified Purchase</td><td>0.092**</td><td>0.062**</td><td>0.030**</td><td>0.093**</td><td>0.033**</td><td>0.060**</td></tr><tr><td>User-Provided Photo</td><td>0.419**</td><td>0.411**</td><td>0.008**</td><td>0.413**</td><td>0.275**</td><td>0.138**</td></tr><tr><td rowspan="2">Vote ≥ 5</td><td>Verified Purchase</td><td>0.091**</td><td>0.061**</td><td>0.030**</td><td>0.092**</td><td>0.029**</td><td>0.063**</td></tr><tr><td>User-Provided Photo</td><td>0.252**</td><td>0.214**</td><td>0.038**</td><td>0.231**</td><td>0.175**</td><td>0.056**</td></tr><tr><td rowspan="2">Vote ≥ 10</td><td>Verified Purchase</td><td>0.091**</td><td>0.059**</td><td>0.032**</td><td>0.092**</td><td>0.030**</td><td>0.062**</td></tr><tr><td>User-Provided Photo</td><td>0.171**</td><td>0.119**</td><td>0.052**</td><td>0.145**</td><td>0.129**</td><td>0.016</td></tr></table>

## Appendix F. Robustness Check – Comparison between Two Time Periods

Table F1. OLS Regression for Hypothesis 1a, 1b, 2a, and 2b $( ^ { * * } \mathfrak { p } < 0 . 0 1 , ^ { * } \mathfrak { p } < 0 . 0 5 )$

<table><tr><td rowspan="2" colspan="2">Dependent: Ln(Review Helpfulness)</td><td colspan="3">H1a &amp; H1b</td><td colspan="3">H2a &amp; H2b</td></tr><tr><td>Moderate Reviews</td><td>Extreme Reviews</td><td>Diff.</td><td>Ext. Positive Reviews</td><td>Ext. Negative Reviews</td><td>Diff.</td></tr><tr><td rowspan="2">Verified Purchase</td><td>96–07</td><td>0.075**</td><td>0.033**</td><td>0.042**</td><td>0.039**</td><td>0.018**</td><td>0.021**</td></tr><tr><td>07–18</td><td>0.078**</td><td>0.066**</td><td>0.012**</td><td>0.087**</td><td>0.024**</td><td>0.063**</td></tr><tr><td rowspan="2">User-Provided Photo</td><td>96–07</td><td>0.232**</td><td>0.059**</td><td>0.173**</td><td>0.057**</td><td>0.059</td><td>0.002</td></tr><tr><td>07–18</td><td>0.245**</td><td>0.218**</td><td>0.027**</td><td>0.222**</td><td>0.207**</td><td>0.015**</td></tr></table>

Table F2. OLS Regression for Hypothesis 3a, 3b, 4a, and 4b $( ^ { * * } \mathfrak { p } < 0 . 0 1 , ^ { * } \mathfrak { p } < 0 . 0 5 )$

<table><tr><td rowspan="2" colspan="2">Dependent: Ln(Review Helpfulness)</td><td colspan="3">H3a &amp; H3b</td><td colspan="3">H4a &amp; H4b</td></tr><tr><td>Ext. Review for Search</td><td>Ext. Review for Experience</td><td>Ext. Review for Search</td><td>Ext. Review for Experience</td><td>Ext. Review for Search</td><td>Diff.</td></tr><tr><td rowspan="2">Verified Purchase</td><td>96–07</td><td>0.039**</td><td>0.029**</td><td>0.009**</td><td>0.038**</td><td>0.034**</td><td>0.004</td></tr><tr><td>07–18</td><td>0.071**</td><td>0.046**</td><td>0.025**</td><td>0.073**</td><td>0.007**</td><td>0.066**</td></tr><tr><td rowspan="2">User-Provided Photo</td><td>96–07</td><td>0.047**</td><td>0.078**</td><td>0.031</td><td>0.051**</td><td>0.069**</td><td>0.018</td></tr><tr><td>07–18</td><td>0.228**</td><td>0.210**</td><td>0.018**</td><td>0.219**</td><td>0.158**</td><td>0.061**</td></tr></table>

Table F3. Negative Binomial Regression for Hypothesis 1a, 1b, 2a, and 2b $( ^ { \ast \ast } \mathfrak { p } < 0 . 0 1 , ^ { \ast } \mathfrak { p } < 0 . 0 5 )$

<table><tr><td rowspan="2" colspan="2">Dependent: Review Helpfulness</td><td colspan="3">H1a &amp; H1b</td><td colspan="3">H2a &amp; H2b</td></tr><tr><td>Moderate Reviews</td><td>Extreme Reviews</td><td>Diff.</td><td>Ext. Positive Reviews</td><td>Ext. Negative Reviews</td><td>Diff.</td></tr><tr><td rowspan="2">Verified Purchase</td><td>96–07</td><td>0.099**</td><td>0.056**</td><td>0.043**</td><td>0.063**</td><td>0.035**</td><td>0.028**</td></tr><tr><td>07–18</td><td>0.102**</td><td>0.088**</td><td>0.014**</td><td>0.110**</td><td>0.040**</td><td>0.070**</td></tr><tr><td rowspan="2">User-Provided Photo</td><td>96–07</td><td>0.261**</td><td>0.085**</td><td>0.176**</td><td>0.087**</td><td>0.076</td><td>0.011</td></tr><tr><td>07–18</td><td>0.275**</td><td>0.234**</td><td>0.041**</td><td>0.239**</td><td>0.212**</td><td>0.027**</td></tr></table>

Table F4. Binomial Regression for Hypothesis 3a, 3b, 4a, and 4b (\*\* $\mathsf { p } < 0 . 0 1 , \mathsf { \Pi } ^ { * } \mathsf { p } < 0 . 0 5 )$

<table><tr><td rowspan="2" colspan="2">Dependent: Review Helpfulness</td><td colspan="3">H3a &amp; H3b</td><td colspan="3">H4a &amp; H4b</td></tr><tr><td>Ext. Review for Search</td><td>Ext. Review for Experience</td><td>Ext. Review for Search</td><td>Ext. Review for Experience</td><td>Ext. Review for Search</td><td>Diff.</td></tr><tr><td rowspan="2">Verified Purchase</td><td>96–07</td><td>0.062**</td><td>0.049**</td><td>0.013**</td><td>0.061**</td><td>0.052**</td><td>0.009**</td></tr><tr><td>07–18</td><td>0.097**</td><td>0.059**</td><td>0.038**</td><td>0.095**</td><td>0.018**</td><td>0.077**</td></tr><tr><td rowspan="2">User-Provided Photo</td><td>96–07</td><td>0.061**</td><td>0.129**</td><td>-0.067**</td><td>0.073**</td><td>0.111**</td><td>-0.038*</td></tr><tr><td>07–18</td><td>0.250**</td><td>0.220**</td><td>0.030**</td><td>0.238**</td><td>0.189**</td><td>0.043**</td></tr></table>
