---
otero_id: 4508
otero_key: "RHTYH2ZE"
title: "Gazing at the stars is not enough, look at the specific word entropy, too!"
authors: "Jorge E. Fresneda; David Gefen"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103388"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Gazing at the stars is not enough, look at the specific word entropy, too!

![](/api/attachments/RHTYH2ZE/fulltext/images/c80cca48553a1ec605acbeb3666d08ee89e0daa2769af67df4d36bc0995ef83e.jpg)

Jorge E. Fresneda <sup>a,</sup>\*, David Gefen <sup>b</sup>

<sup>a</sup> Martin Tuchman School of Management – New Jersey Institute of Technology, 184 Central Avenue, Newark, NJ 07102, United States <sup>b</sup> LeBow College of Business – Drexel University, 3220 Market Street, Philadelphia, PA 19104, United States

## A R T I C L E I N F O

Keywords: Online consumer reviews Ecommerce Review helpfulness Latent semantic analysis Text-mining

## A B S T R A C T

The helpfulness of online reviews depends on their textual portion. Using the information provided by the seller as a baseline, this study applies latent semantic analysis (LSA) to assess what parts of that textual portion contribute to helpfulness by separating the text into three categories of high entropy words: (1) unique (i.e. does not appear in previous reviews) corroboration entropy, (2) recommendation entropy, and (3) unique opinion entropy. Unique corroboration entropy is calculated based on the number of words in this review that describe the product on the seller’s site, confirming the seller’s claims, which did not appear in previous reviews. Recom mendation entropy is based on the number of words that are associated with explicit recommendations. Unique opinion, referred as “regular opinions” in the literature, entropy is based on the number of all the other words in the review that provide positive or negative evaluations of products as well as other additional informational elements that did not appear in previous reviews. The results show that both recommendation and unique opinion entropies (only marginally) increase review helpfulness evaluations, while greater unique corroboration entropy is insignificant.

## 1. Introduction

Online consumer reviews revolutionized the way consumers gather information about products and services [1]. They complement and even substitute for other types of business-to-consumer and consumer-to-consumer communications [2,3]. Online reviews provide opinions from previous customers, performing the role of free “sales assistants” [4]. In turn, this information helps other customers identify those products or services that best match their needs and preferences. The helpfulness rating that customers assign a review is a commonly used measure of its information value [e.g. 5], and represents a public endorsement by peer consumers [6]. Online product reviews impact sales [2,7–,8,9,10], especially helpful reviews [11]. As a reflection of this, Forbes recently titled one of their articles “Online Reviews Are The Best Thing That Ever Happened To Small Businesses” [12]. The strategic value of online reviews is acknowledged by academicians and practi tioners [e.g. 13]. Clearly, online reviews are important, as is their textual portion. But what exactly in those words do readers look for?

This study sets out to answer that question by analyzing the textual portions of online reviews, classifying the high entropy words in the text into words that deal with (1) unique corroboration by repeating key words the seller used to describe the product, (2) recommendations, and (3) unique opinion information. This is done using latent semantic analysis (LSA). The importance of these information types is suggested in the previous literature [e.g. 14–16]. Unique corroboration informa tion are high entropy words that appear in the seller’s site and are mentioned by reviewers and that are not mentioned in previous reviews. The uniqueness of information in this category is associated with corroborating seller's claims that were not corroborated by another reviewer before. Examples of this could include in the case of light bulbs terms, such as “100 W” and “Dimmable” (see Appendix A). This infor mation category allows reviewers to address features and characteristics already described by the seller to confirm the seller’s claims. Recom mendations are high entropy words that suggest the reader should take a specific action (e.g. buy or not a product). Examples of this could include such as “Recommend” and “Buy” a product. This category includes recommendation words that appear in previous reviews. Unique opin ions, somehow similar to “general opinions” in the work of Qazi et al. [16], are all the other high entropy words not mentioned in previous reviews. This information category provides assessments of products and additional information elements, such as transactional processes or service quality provided by the retailer. Information entropy allows our analysis to contrast new information provided in reviews against the information provided by sellers, measuring the argument that information in reviews is more relevant in those contexts in which the in formation from the seller is original and scarce. This is a unique characteristic of our analysis that differs from employing more simplistic approaches such as word counts.

Putting this study into context, the early literature on what makes online reviews helpful focused on numeric variables that were easily accessible by researchers, such as the valence (also referred as the number of stars), volume of total reviews, or the raw number of words included in the text of each review [e.g. 5,17,18]. The content of the textual portion of online consumer reviews, and specifically the amount of additional information comprised, has received less attention—to the best of our knowledge, only Singh et al. [19] studied how the amount of (general) information impacts the helpfulness assessment of the review.

Differing from previous literature that employed manual annotation in the methodology [e.g. 16,20] or context-dependent lexicons [20], this research suggests an automatic approach to label different types of in formation. The methodology presented adds the capability of gaining real-time insights, highlighted as an important area of research [21,22]. Adding a textual analysis of the kind proposed in this study is important because research suggests that the content of the textual part of product reviews may allow for richer descriptions of the interaction of buyers with the product [23]. Furthermore, this research not only analyzes the content, but also the content in context, by considering the information provided in previous reviews as well as in the product description of the seller.

The hypotheses were tested on product reviews of 16 types of light bulbs (LEDs and incandescent light bulbs) available for purchase at Amazon.com. The results show that unique opinion and recommenda tion entropies contributed to review helpfulness. Contrary to this, corroboration entropy, which addresses information already contained in the product description from the seller when this information was not addressed in previous reviews, was insignificant. The product type (LEDs versus incandescent light bulbs) adds relevant nuances to these results, as discussed in subsequent sections.

The contributions of this study are in: (1) showing how the three types of high entropy words provide different types of information in online reviews, (2) proposing an automatic approach to identify and quantify those different types of information, and (3) showing that the relative importance of those information types differs depending on the review context (i.e. on the scarcity and the originality of the informa tion). The next sections introduce the theoretical background and hy potheses, followed by sections on the conceptual model, methodology, and data analysis, and conclude with a discussion of the findings, limi tations, and future research.

## 2. Theoretical Development

## 2.1. Word-of-mouth, electronic word-of-mouth, and review helpfulness

Online consumer reviews are a particular form of word-of-mouth (WOM). WOM is a broad type of informal communications among consumers. These informal communications range in coverage from products to services, brands or even full companies [9]. WOM provides potential new customers with information generated by previous con sumers that may influence their future behavior [1,24,25]. The non-commercial nature of WOM may be the cause of why this form of communication is considered as reliable and valid by consumers [26–, 27,28]. Consumers generally trust peer consumers more than they trust marketers or corporate communications [29].

Specifically, online reviews pertain to the electronic counter part of WOM (e-WOM). E-WOM is defined as “any positive or negative state ment made by potential, actual or former consumers about a product or company, which is made available to a multitude of people and in stitutions via the Internet” [30], p.39]. Not only online consumer re views, but many other elements, such as blogs, online forums, or electronic bulletins are types of e-WOM [8]. Differing from traditional WOM, e-WOM communications take place among customers and po tential customers with no previous connection or relationship [31].

Table 1  
Frequency and Percentage Number of Helpfulness Evaluations per Product Type.

<table><tr><td rowspan="2">Range of number of evaluations</td><td colspan="2">Frequency of Number of Evaluations per Review (%)</td></tr><tr><td>Incandescent light bulbs</td><td>LEDs</td></tr><tr><td>0</td><td>263 (61.0)</td><td>140 (42.7)</td></tr><tr><td>1–10</td><td>157 (36.4)</td><td>160 (48.8)</td></tr><tr><td>11–20</td><td>9 (2.1)</td><td>14 (4.2)</td></tr><tr><td>21–30</td><td>0 (0)</td><td>7 (2.1)</td></tr><tr><td>31–40</td><td>2 (0.4)</td><td>7 (2.1)</td></tr></table>

Different sites hosting online review decide on their format and structure. Therefore, there is no standard format for this form of e-WOM, although online consumer reviews usually include several elements such as: (1) review valence (also referred to as “number of stars”); (2) review text (reviewer provided summary and description of their evaluation); (3) the actual verification that the reviewer bought the product or ser vice; (4) information about the reviewer (ranging from the number of reviews completed to accomplishments and recognitions, such as badges); and (5) a summary of the helpfulness evaluation of the review. The helpfulness of a review is evaluated by people who read it, not those who posted it. In the case of Amazon.com this helpfulness evaluation is implemented by answering the question “was this review helpful to you?” with a dichotomous “yes” or “no” answer (thumb up/thumb down).<sup>1</sup> These helpfulness evaluations are the basis for calculating the dependent variable in the conceptual model of this study.

Review helpfulness is “the extent to which consumers perceive the product review as being capable of facilitating judgment or purchase decisions” [32, p.103]. Helpful product reviews provide potential buyers with pertinent information from previous customers with the purpose of informing the purchasing decision process. Review helpfulness can be understood as the principal tool to assess how potential customers evaluate the quality of the information provided in a review [1,5]. This is important because helpfulness ratings can impact sales [4,11,33], adding even more value to online reviews [34]. Previous literature acknowledged the strategic and economic value of online reviews [e.g. 5,13]. Spool [35] estimated that Amazon.com added \$2.7 billion to its annual revenue by just requesting customers to assess the helpfulness ratings of online reviews. Helpfulness ratings may also help potential customers reduce information overload by concentrating on only the most helpful reviews [36,37]. The focus of this research is online product reviews and the next section addresses what can be found in the textual portion of these reviews.

## 2.2. What do people write in online reviews?

Online consumer reviews contain different types of information. Li and Huang [32] and Mudambi and Schuff [5] found that reviews described the experiences of previous buyers and discussed product features. Likewise, Lee and Bradlow [15], Ghose et al. [33], and Sanchez-Franco et al. [38] looked at product features elicited from on line reviews. (See Table 1 in Moon and Kamakura [39] for a complete list of studies focused on product features elicited from online consumer reviews.) Moe and Trusov [40] and Min and Park [41] observed that the textual portion of online reviews describes the customers’ personal experience with both the product that was bought and with the whole purchase process (i.e. including broad elements, such as shipping, packaging, or customer service interactions). The textual portions of online reviews have also been studied as recommendations to potential new buyers [42,43]. Packard and Berger [44] found that explicit endorsement (e.g. “I recommend it”) in online reviews is very persuasive and increases purchase intent, highlighting the relevance of this type of information, and arguably, its helpfulness.

Supporting the importance of the proposed opinion type of infor mation in online reviews, in a content analysis of text reviews about digital cameras on Taobao.com, Lu et al. [14] found that an over whelming 86.4 % of the reviews included information about what the reviewer learned from the whole transaction process. This type of in formation also included service attitude, congruity between seller’s claims and real products, shipping, and order fulfillment time. The focus on information about the transaction process has also been suggested in the microeconomics literature [45]. Of the reviews on Taobao, 7.1 % included content related to interactive cues, such as tips or recommen dations to other buyers [14].

Given this stream of literature, this research suggests, and empiri cally tests, a methodological approach that classifies words in the text of reviews into three types of information: corroboration, recommenda tion, and opinion (unique corroboration and unique opinion in this study). This approach is, to some extent, close to Qazi et al. [16]. Unique corroboration terms are words that are originally employed by the seller to describe the product—covering its most relevant features and char acteristics—and that also appears in this review, but not in previous reviews of the same product. Therefore, corroboration are unique terms addressing seller’s provided information, and are related to literature that found that product characteristics is one of the major components of the content of reviews [e.g. 15]. This category is somehow related to comparative opinions in the work of Qazi et al. [16]. While opinions (or regular opinions) have a single focus, which is the object or product reviewed (i.e. provide good or bad opinions about one specific product), comparative opinions have more than one focus, as comparing objects A with B [46]. In this study, the comparison is established between informational elements provided by the seller or manufacturer (e.g. the color temperature of a light bulb the manufacturer claims) and the experience of the reviewer (e.g. the color temperature reported by the reviewer).

Recommendations are terms associated with explicit recommenda tions from reviewers to potential new buyers. This term category is theoretically connected to literature that identified explicit recommendations as a relevant element in online reviews [e.g. 43]. The recom mendation category corresponds conceptually to suggestive opinions in the work of Qazi et al. “as directing someone to do something in a polite manner” [16, p. 75]. Recommendations are scarce compared with the other two information types and, therefore, this is the only information category that is not contrasted against previous product reviews—85 % of the review in our dataset do not in fact contain recommendations, similar to the low prevalence suggested in previous literature [14].

Unique opinion terms are other high entropy words in the review that address positive or negative aspects of a particular product. This category is meant to address them in a broad manner—but excluding both recommendation and corroboration terms. The unique opinion category corresponds conceptually to regular opinions in the study of Qazi et al. [16] or simply opinion in previous literature [47]. Fig. 1 summarizes the conceptualization and operationalization of the three types of entropies.

Although comparative opinions, regular opinions, and suggestive opinions are in some way conceptually similar to the three types of entropies previously introduced, our theoretical approach significantly differs from the work of Qazi et al. [16] in the unit of analysis. While these authors applied this framework to whole reviews (labeling entire reviews as either regular, comparative, or suggestive opinions), our study applies a finer level of granularity by labeling terms included in each review. This finer granularity allows reviews to contain several of these informational elements simultaneously (e.g. reviews can contain recommendation information together with opinion information simultaneously). Reviews containing several types of informational el ements simultaneously might be perceived as being more helpful, since they address more than one facet of product information.

## 2.3. Theoretical model development

The model developed in this section incorporates the three types of information discussed above, together with other known contributors to online review helpfulness. (Note that the data employed in this study do not include reviewer-related factors, although recent literature [48] suggests that review-related factors are more relevant antecedents of review helpfulness than reviewer-related ones.) Filieri et al. [1] and Hong et al. [18] provided an extensive review of antecedents of review helpfulness. Capitalizing on that work, this study incorporates the three types of information as discussed above in the textual portion of the review measured through information entropy.

The textual part could arguably allow for richer description [23] and may also convey additional helpful information that may have nothing to do with the actual interaction with the product itself, such as the interaction with the firm’s customer service, shipping, packaging, etc. —captured in this study through opinion entropy. Moreover, analyzing a numeric value, such as the number of stars, rather than analyzing its related textual review ignores the possibility that the textual data may deal with more than one aspect of the quality construct or the uniformity of consumer preferences [49]. Information entropy, discussed next, could serve as the theoretical foundation to automatically quantify the impact of the three different types of information.

## 2.4. Information entropy as a measure of review uniqueness relative to previous reviews

Entropy is a well-known measure of disorder (i.e. unpredictability). Information entropy was suggested by Shannon [50]. Within informa tion systems, entropy was defined as a “measure of the amount of in formation the system contains” [51, p.301]. Applied to the context of online reviews, the more the message included in an online review can be predicted based on other reviews, the lower its entropy.<sup>2</sup> The rarer it is compared with other messages in other reviews, the higher its en tropy.<sup>3</sup> In the case of an online consumer review, entropy is the expected mean value that the words in the review contribute to making that re view unique, and therefore, less predictable based on other previous reviews. If a review has words that can be predicted based on other existing reviews, then that review has low entropy because its word content can be predicted. On the other hand, if there are words that are relatively unique to that review, then the probability of predicting that word content is smaller, and its entropy—and the entropy of those words, in particular—will be higher. In other words, high entropy words are rarer and therefore contribute more value to the review because it is more unique.

Entropy also allows this study to put review information in the context of the information provided by sellers, differing from analyses that employ simple word count. Considering the exact same number of rare words, entropy is higher in those contexts in which existing infor mation about a product, such as its description, features, and charac teristics is limited or scarce. In contrast, contexts in which sellers offer

<sup>3</sup> Tossing dice is a good example of entropy. The result of tossing a true dice cannot be predicted based on other tossing events because the probability of any side is always 1 in 6, so its entropy is high. Analogously, in our case, if each review is totally unique and non-overlapping with other reviews, then past reviewers cannot predict its word content, and its entropy will be high. In contrast, the result of a false dice is more predictable, and hence its entropy lower. Analogously, in our case, if a review uses the same words as other re views, then its content can be predicted to some extent, and its entropy therefore lowers.

![](/api/attachments/RHTYH2ZE/fulltext/images/724962a564b470a7bf93e292f4f7f7fc3a048ce9b95388802193f8266e23588e.jpg)  
Fig. 1. Summary of the Conceptualization/Operationalization of Entropies.

abundant information would yield smaller entropy, for the same number of rare words (see second example in Appendix A). This characteristic enables the analysis to weight terms differently according to the preexisting information environment. Arguably, review information might be more important when existing information from the seller is scarce.

We expect that the entropy of each of the three word-categories will be a good predictor of helpfulness because entropy brings into account also the total number of words in the text. If a review is more helpful when it provides more opinion, corroboration, and recommendation information, as shall be argued in hypotheses 1–3, then, arguably, that increased helpfulness should be stronger when there are fewer words because then it is easier for a potential consumer reading that review to extract that information. Entropy plays a role here also because merely repeating the information in previous reviews may actually be a nuisance to a potential consumer reading that review who is seeking new information.

One of the most relevant features of entropy theory is its additive rule. The information content of a message that contains statistically independent elements can be calculated as the sum of the information content of those individual elements [50,52]. Shannon’s entropy of a categorical random variable with size p and with associated probabili ties $\theta _ { 1 } , . . . , \theta _ { \mathrm { p } }$ with $\theta _ { \mathrm { k } } > 0$ and $\sum _ { \mathrm { k } } \theta _ { \mathrm { k } } = 1$ in natural units is given by Hausser and Strimmer [53] as:

$$
\mathrm{H} = - \sum_ {\mathrm{k} = 1} ^ {\mathrm{p}} \Theta_ {\mathrm{k}} \log (\Theta_ {\mathrm{k}})\tag{1}
$$

Ross [54] defines information as “knowledge, after which one re ceives and processes, that changes, in an uncertainty changing way, their ex ante probability distribution regarding a set of propositions or states” (p. 5). Therefore, information entropy is closely related to the concept of uncertainty reduction [55]. More information leads to less uncertainty [50,56], and the amount of information that a system pro vides can be measured by the amount of uncertainty that it reduces [51]. Notice that the argument for entropy is that a unique review, measured through the uniqueness of its words, is more helpful, as suggested in hypotheses 1–3.

## 2.5. LSA and identifying high entropy terms by category

Entropy can relate also to words by category. This section discusses the categories applied in this study and how LSA was used to identify the high entropy words that will be classified into those categories. To recap, the information in online reviews often corroborates the claims made by the seller [14]. In the case of this study that information relates to specific words that repeat the technical details of a light bulb, such as the color temperature of a light bulb being “2,700K” or the wattage being “150-watt.” We label this kind of information as corroboration. “Comparative opinions” in previous literature [16] referred to the comparison of two objects, and it is somehow similar to the conceptu alization of the corroboration category in this study. We adapted this concept to the comparison between informational elements provided by the seller or manufacturer of the product and the actual experience of the reviewer with that product.

Also, to recap, another type of information conveyed in online re views is recommendations. This is what Lu et al. [14] labeled as “interactive cues” and Qazi et al. [16] referred to as “suggestive opin ions.” Examples from the data in this study are “I would recommend staying away from the 100 W [light bulb]” or “I highly recommend this bulb for its economy and quality.” This paper labeled this type of in formation as recommendation.

A third type of information we are classifying is opinions. Opinion words define a broad information category that replicates previous ap proaches in the literature, such as “regular opinions” in the works of Qazi et al. [16] and Jindal and Liu [47], and that reflects assessments of products in a broad way—and excludes corroboration and recommen dation words. Similarly, Lu et al. [14] define a “Information Quality dimension” as a broad product information category that not only contains products evaluations, but also includes additional informa tional elements, such as service quality of the retailer or shipping and order fulfillment, and excludes other information categories, such as interactive cues (tips and recommendations). Specific examples of this type of information may include testimonials about how pleasant the light produced by a light bulb is, how it allowed the person writing the review to see nuanced colors in paintings better, or how long the light bulb lasted until it stopped working. Entropy deals with opinions not mentioned by previous reviews.

Before discussing the hypotheses, some background on LSA is necessary to clarify operationally what constitutes opinion, corroboration, and recommendation in this context. What LSA does, more on that in the next sections, is to identify through singular value decomposition (SVD), a process somewhat equivalent to a two-way principal component analysi (PCA), what terms (e.g. words) and what documents (in this case, online product reviews) factor together in a terms-to-document matrix (TDM). Terms that factor together are assumed to carry some latent shared meaning, much as factors are assumed to do in a PCA. And, as in a PCA, only those factors that explain high degrees of the variance are typically retained. The resulting retained factors identify the words that carry the most weight in explaining the variance in the TDM.

In the specific analysis run in this study, some of those factors con tained words that were the same words that were used in the manu facturers’ websites to describe products. Those words were classified in this study as corroboration terms. Terms that appeared in previous re views of the same product (arranged in posting order) were discarded, leaving only unique words (unique corroboration terms). The corrobo ration entropy of each review was calculated through the entropy of those unique words that did not appear in previous reviews of the product. Note that LSA was set to drop commonly used words (called stopwords), such as “the,” so the retained words in this category are primarily technical in nature. After also removing recommendation words—explained in detail in the “Methodology” section—the remain ing words were treated as opinion terms. Similarly to corroboration, opinion terms that appeared in previous reviews of the same product (arranged in posting order) were discarded, leaving unique words (unique opinion terms). The opinion entropy of each review was calculated through those unique opinion words. Conceptually, this process could be thought of as the equivalent of asking human raters to identify the most influential words in the online product reviews, and then estimate the entropies of opinion, recommendation, and corrobo ration terms of the review based on those words. This study does so automatically.

## 2.6. The importance of entropy of opinion type words

Exploring product information allows consumers to make better purchase decisions [57]. Online reviews can contribute to making more informed decisions by providing additional information from what is delivered by sellers and manufacturers in ecommerce sites. At least, part of that information can be conveyed through single words. Previous literature [19] established that information entropy is a strong ante cedent of review helpfulness and as part of its contributions, this study intends to provide a more nuanced view of what specific informational elements contributes so.

The unique opinion information category contains evaluations of products [16,47] and additional informational elements that refer, not only to the assessment of the product itself, but also to additional elements, such as transactional processes or service quality provided by the retailer [14]. Reviews with high entropy of these words show that the review is more unique, and, hence, presumably more valuable than a review that merely repeats what other reviews say (low entropy). Considering that informa tion entropy is a strong antecedent of review helpfulness [19], we contend that more information of this category might increase the helpfulness rate of a review. To recap, review readers might be interested in finding additional facets of product information not provided by sellers or manu facturers and they might value the effort of addressing new aspects not covered in previous reviews. Captured through review entropy, unique opinion information might have an even greater positive impact on review helpfulness in those contexts in which information provided on the site is scarce. That is, entropy captures the information context (i.e. its scarcity) in the available product description, as a consumer considers the information provided by reviews. Consistent with that argument, research has shown that early reviews, which are more likely to contain words that do not appear in previous reviews, might have a more important positive impact on review helpfulness [58,59]. That higher opinion entropy results in more helpfulness is based on the argument that potential consumers are looking for more information than only that which appears in the seller’s site. That is obvious, or else they would not bother to read reviews. However, those potential consumers are not looking for just more information but, rather, for more information than has not appeared in previous reviews. That is what entropy measures. True, not all new information is indeed valuable, but arguably, at least some of it probably is, or else people would not seek additional reviews. If the same information, including opinion information, keeps on appearing in one review after the other then it is hardly helpful. Accordingly, it is hypothesized that:

H1. The higher the opinion entropy in a review, the more it will be rated as helpful.

## 2.7. The importance of entropy of corroboration type words

Repeating keywords used by the seller in its website can partially support the claims the seller is making, such as repeating that a light is “dimmable.” Offering an evaluation of the closeness of the product description to the reality of the product may be a reasonable piece of in formation to share in a review [60]. Unique corroboration entropy calcu lates entropy based on the number of words mentioned in the description of the product by the seller or manufacturer that are also mentioned in the review, but that were not mentioned in previous reviews. A review that contains many words used in the seller’s site that were not mentioned in previous reviews has high entropy (see Appendix A).

Allowing also that people pay more attention to new information than to what has been written many times before (where they might just skim over it), then a repetition of as seller’s claims that did not appear in previous reviews should be more valuable. To demonstrate, if a seller wrote that the light bulb is “warm” and “bright,” and the word “warm” appears over and over again in related reviews, but the word “bright” appears in this review for the first time, then, arguably, this infrequent “bright” should carry more value than the frequent “warm” because consumers got used to reading “warm” and might just skip over it. En tropy accounts for that repetition. Again, clearly not all new information is indeed valuable, but arguably at least some of it probably is, or else people would not seek additional reviews. In the case of corroboration, this means new information that repeats what appeared in the seller’s site, but has not been corroborated in reviews previous to this one. Accordingly, increased entropy, measuring the first-time repetition of the claims the seller makes, could provide increased value to consumers looking for new information and skipping what they read previously. Applying the same logic as in the previous hypothesis, if review users seek additional information from what is delivered by sellers (in this case, corroborating or confirming that seller’s claims are accurate) to make a purchase decision, then unique information should be more helpful.

H2. The higher the corroboration entropy in a review, the more it will be rated as helpful.

## 2.8. The importance of entropy of explicit recommendations from reviewers

Previous literature found that potential buyers assign much value to recommendations from peer buyers because potential customers perceive those recommendation to be less biased and because they find other buyers’ recommendations easier to relate to [26]. Potential buyers employ these recommendations as decision-making heuristics, irrespective of the reviewer’s personal characteristics [61]. Recommendations are potentially helpful also because relying on them can reduce information overload [62], especially overload created by the prevalence of many other, non-recommendation, words in the review. Recommendations in reviews are also rare [14] and therefore their value as easing purchase decision can increase because of their scarcity. In fact, 85 % of the reviews in this dataset contained no recommendations. As such, when a recommendation word does appear, it should have high entropy as well as conveying unique in formation. It will have high entropy because of the way entropy is calcu lated based also on the lack of prevalence of that word in previous reviews. That is because the entropy of any of the three word-categories increases when a word in that category is rare, because it is less likely to have appeared in a previous review when it hardly ever appears, compared to when it is very common, and hence has a high probability of having appeared in a previous review. And, such a message will convey unique information if only because most reviews do not have that kind of recommendation information. This study also applies information entropy for recommendations not only for consistency with opinion and corrobo ration information, but also to capture the value of information in context. (Again, entropy captures the information context (i.e. its scarcity) in the available product description, as a consumer considers the information provided by reviews.) Arguably, recommendations might be more helpful in those contexts in which information about the product provided by the seller is scarce. Hence, considering that information entropy is a strong predictor of review helpfulness [19], we posit that also higher entropy of recommendation information should increase the helpfulness of the review.

H3. The higher the recommendation entropy in a review, the more it will be rated as helpful.

## 2.9. Other sources of information in individual consumer reviews

Customer ratings, such as the number of stars, are known to be important quantitative informational elements of e-WOM, assisting po tential customers in learning about the quality of a product [63]. Pan and Zhang [17] found that positive ratings are more influential than negative ones and are rated as more helpful. If that is the case, then the number of stars might be considered as a surrogate recommendation [64]. Furthermore, from a practical standpoint, the existence of a market for artificially inflating ratings and fake reviews [e.g. 65] also suggests that there should be a positive relationship between the number of stars and helpfulness. The number of stars is added to our model as a control variable because its impact is well established in previous literature, and yet it is not the focus of this study.

Potential customers are not perfectly informed about all the avail able product or service choices in the market [66]. The literature sug gests that this problem can be lessened by the provision of product information by third parties [67]. Product reviews are suitable to miti gate this lack of market knowledge if their information is pertinent, but only if their source is believable [68]. Filieri [63] found that if the in formation source in e-WOM is assessed as credible, it will be perceived as more helpful. Credibility can be at least partly indicated if the person posting the online product review actually bought the product. Conversely, if that person did not buy the product, the credibility in making claims about it may be questionable. Many sites include a verification that the reviewer purchased the product to somehow indi cate source credibility. Consequently, it might be expected that a veri fication that the review writer bought the product should increase the helpfulness of the review. Similarly to the number of stars. the confir. mation that the reviewer purchased the product is included as a control variable in our model without being the focus of the study.

## 3. Conceptual Model

Summarizing the hypotheses, the conceptual model (Fig. 2) expands on previous research about what determines the helpfulness of a review [e.g. 5,17] by integrating these three types of proposed information entropy available in online reviews and adding control variables related to other sources of information in product reviews.

Three additional control variables, not directly related to the content of online reviews, were also added at this point. The number of times that the helpfulness of each review was evaluated (number of evaluations in Fig. 2) is the first one of the three additional control variables. The algorithm employed by Amazon.com to rank the most helpful reviews is based on the aggregated number of evaluations that each review received. This feature has an “anchoring effect,” leading to more helpful reviews receiving more votes, since they are made more salient for potential buyers [36,69] who rely on such recommendations when making purchasing decisions [e.g. 68, 70]. This social persuasion may also impact the helpfulness assessment of a review. The number of previous helpfulness assessments can have an impact on the subsequent evaluations too [71,72]. Additionally, previous literature also controlled for the number of helpfulness evaluations [5] and therefore, to put the results of the study in contexts the decision was made to incorporate this variable.

The second control is product type. As explained in the “Methodol ogy” section, this study employs data on 16 different products pertaining to two product categories that elicit different levels of interest in con sumers: light-emitting diode (LED) and incandescent light bulbs. Literature suggests that consumers may seek more information about products that they are relatively less familiar with (in this case, LED in 2015, when they were relatively new) than for well-established products (in this case, incandescent light bulbs) [73–,74,75,76]. Allowing that customers may seek more information in the case of relatively new products, the study controls for product type.

The third control is review posting order. Posting order is included in the model to discard alternative explanations to our findings such as the “early bird bias” (the earlier that an online review is posted, the more helpfulness votes it will receive) [58,59]. If posting order has a signifi cant impact on review helpfulness, then we would expect that review helpfulness should decrease with increasing order (i.e. the later that a review is posted, the less helpful it is). The model also includes the total number of words in the textual portion (number of words) as a weighting criterion. Previous research suggested that a longer textual part increases review helpfulness [e.g. 2].<sup>4</sup> Fig. 3 shows the variables included in the conceptual model as they were extracted from each of the product reviews in the database:

## 4. Methodology

Analyzing the text portion of the online reviews was performed with LSA. LSA is a fully automatic statistical method that determines the similarity of meanings across words (named “terms” in LSA) and docu ments (in this case, online consumer reviews) by analyzing large bodies of text. Because LSA applies SVD, terms can be associated with each other even if they do not co-occur together. It is enough for two terms to both co-occur with a third term to make the former two terms close in meaning [77,78]. LSA has been argued to approximate some aspects of human learning from vast amounts of text, as well as identifying syno nyms [79]. Those characteristics make it especially suitable for the kind of analysis performed in this study. Another advantage of LSA is that it allows for the analysis of many documents, in this case, product reviews, with minimal human intervention. This ability to analyze large amounts of textual data have been highlighted in previous literature as a relevant area for further research [e.g. 22,33,49]. The application of LSA in this study was to identify factors that best describe corroboration and opinion terms.

![](/api/attachments/RHTYH2ZE/fulltext/images/f5c849a75d162e21743ed4a8e78ade9a80439f11972328f3d82a56125c962d21.jpg)  
Fig. 2. Conceptual Model.

The dataset analyzed consisted of 759 product reviews relating to 16 types of light bulbs available for purchase at Amazon.com (eight in candescent light bulb packs and eight LED light bulbs). The selection of this specific category is based on two main reasons: (1) lack of season ality and (2) fewer reviews than other popular products, which may increase the relevance of each individual review. Having fewer review in that product category means that we could conceivably analyze the entire set of reviews in a specific period of time. Indirectly, having the entire set could avoid sampling biases. The two types of products, LED and incandescent light bulbs, differ in that LEDs were relatively un common at the period of the data collection. The dataset was purposely selected to reflect a dichotomy between two product types that raise different levels of interest in consumers, as it was collected in 2015. LEDs were introduced in the market only after 2008 [80] and they represented less than 8% of the market at the time of the data collection, with a growing market share trend and growing interest from consumers [81]. Incandescent light bulbs are an established, mostly functionally equivalent product with a relevant decreasing trend in market share [81], representing a different, arguably less interesting product for consumers. LED light bulbs have a greater percentage of reviews eval uated on their helpfulness than non-evaluated (see Table 1 below). The growing interest in LEDs at that time is suggested by the higher number of their helpfulness evaluations. These different levels of interest are also suggested in Table 2, where the value of the variable “Number of Helpfulness Evaluations” varies from an average of 1.30 for the incan descent product category to 3.27 for the LED product category.

![](/api/attachments/RHTYH2ZE/fulltext/images/0f373a30eb6d54448e2027176a9c1770e641c5bbacf80087685d2c7ea51a1841.jpg)  
Fig. 3. Variables Extracted from Reviews Included in the Conceptual Model.

Table 2 Descriptive Statistics.

<table><tr><td colspan="2"></td><td>Model 1(Full Model)</td><td>Incandescent Product Category</td><td>LED Product Category</td></tr><tr><td rowspan="3">Helpfulness Score</td><td>Mean</td><td>1.28</td><td>0.57</td><td>2.20</td></tr><tr><td>Std.</td><td>4.51</td><td>3.31</td><td>5.58</td></tr><tr><td>N</td><td>759</td><td>431</td><td>328</td></tr><tr><td rowspan="3">Unique Opinion Entropy</td><td>Mean</td><td>0.24</td><td>0.20</td><td>0.29</td></tr><tr><td>Std.</td><td>0.19</td><td>0.17</td><td>0.21</td></tr><tr><td>N</td><td>759</td><td>431</td><td>328</td></tr><tr><td rowspan="3">Unique Corroboration Entropy</td><td>Mean</td><td>0.09</td><td>0.06</td><td>0.12</td></tr><tr><td>Std.</td><td>0.14</td><td>0.12</td><td>0.17</td></tr><tr><td>N</td><td>759</td><td>431</td><td>328</td></tr><tr><td rowspan="3">Recommendation Entropy</td><td>Mean</td><td>0.02</td><td>0.02</td><td>0.03</td></tr><tr><td>Std.</td><td>0.06</td><td>0.05</td><td>0.07</td></tr><tr><td>N</td><td>759</td><td>431</td><td>328</td></tr><tr><td rowspan="3">Number of Stars in the Review</td><td>Mean</td><td>4.09</td><td>4.26</td><td>3.87</td></tr><tr><td>Std.</td><td>1.39</td><td>1.28</td><td>1.50</td></tr><tr><td>N</td><td>759</td><td>431</td><td>328</td></tr><tr><td rowspan="3">Verification of Purchase</td><td>Mean</td><td>0.85</td><td>0.96</td><td>0.72</td></tr><tr><td>Std.</td><td>0.35</td><td>0.21</td><td>0.45</td></tr><tr><td>N</td><td>759</td><td>431</td><td>328</td></tr><tr><td rowspan="3">Posting Order</td><td>Mean</td><td>93.63</td><td>119.00</td><td>60.29</td></tr><tr><td>Std.</td><td>87.84</td><td>100.13</td><td>52.33</td></tr><tr><td>N</td><td>759</td><td>431</td><td>328</td></tr><tr><td rowspan="3">Log (Number of Words)</td><td>Mean</td><td>3.42</td><td>3.16</td><td>3.76</td></tr><tr><td>Std.</td><td>1.11</td><td>0.91</td><td>1.24</td></tr><tr><td>N</td><td>759</td><td>431</td><td>328</td></tr><tr><td rowspan="3">Number of Helpfulness Evaluations</td><td>Mean</td><td>2.15</td><td>1.30</td><td>3.27</td></tr><tr><td>Std.</td><td>5.26</td><td>3.66</td><td>6.65</td></tr><tr><td>N</td><td>759</td><td>431</td><td>328</td></tr></table>

For each of these 16 products, the variables collected were product ID, review ID, review valence, review text, number of words included in the review text, verified purchase, number of helpfulness evaluations, posting order, and the helpfulness rating of the review. At the time of the data collection, these 759 reviews were rated by 1632 potential buyers on their helpfulness. Additionally, a helpfulness score was calculated for each review by summing the number of positive votes minus the number of negative votes. For instance, a review with “1 of 3 people found this helpful” received a score of –1 (+1 for one potential buyer assessing the review as helpful, –2 for two potential buyers assessing the review as non-helpful).<sup>5</sup> See the Review Helpfulness clause in Fig. 3.

Recommendations terms were identified by looking for synonyms in the lexical database WordNet [82]. WordNet provided synonyms for the words “recommendation” and “recommend” (such as “advise”) and “buy” (such as “acquire”). Potentially conflicting words were discarded, e.g. “get” as one of the synonyms suggested for “buy.” Past tense forms of the verbs suggested by WordNet were discarded as well, e.g. “acquired” was discarded—as potentially narrating the interaction with the pro duct—but the present tense “acquire” was kept—as it potentially sug gests buying the product. “Acquire,” “advise,” “buy,” “procure,” “propose,” “recommend,” “suggest,” “tip,” and “warn” and all the remaining terms associated with them after the filtering process were assigned to the list of recommendation words. This list of words was used to identify recommendation words.

Product descriptions provided by the seller/manufacturer were collected (as shown in Fig. 4). This was done to identify the corrobo ration type of information included in the textual portion of the reviews. Standard text-mining techniques were applied to those descriptions. Stopwords (such as “the” or “a”) that are irrelevant for the analysis and punctuation marks were removed from the body of the text. Then, a TDM was constructed from the remaining words in the product description, and a standard term frequency–inverse document frequency (Tf–idf) transformation run. This is a standard procedure that gives more weight to less used words [79,83]. This generated a list of potential corroboration terms.

The textual portion of the online reviews was then analyzed. The same process of Tf–idf transformation was run. But, in addition, a reduced-rank SVD was calculated for the TDM. It was necessary in this case to run a reduced rank SVD because there are many more unique words in the online reviews than either corroboration or recommenda tion words. The SVD retained the k-largest singular values of this matrix and the remainders were set to 0. This resulted in a reduced-dimension SVD representation, with the best k-dimensional approximation to the original matrix. After applying SVD, each document and each term is represented as a k-dimensional vector in a semantic space. Specifically, in this study, this was a vector of 121 dimensions (the number of di mensions was automatically selected by the R function lsa).

From this semantic space, cosine measures of “closeness in meaning” were computed by collecting the 20 terms closest to every one of the original 759 reviews. This generated a pool of terms from the online reviews in the dataset.

Recommendation and corroboration words were identified in the pool of terms from the recommendation and corroboration lists gener ated previously. Specifically, 6 recommendation and 269 corroboration terms were identified as mentioned in the reviews. The number of times that any of the six recommendation terms appeared in the text of the review was calculated and added for each review. Recommendation words are rare and it is the only information category for which no further processing was implemented. The number of times that any of the 269 corroboration terms was included in the text of the review was counted for each review. Reviews were classified by product and or dered by posting order. Corroboration words that appeared in previous reviews of the same product were identified and not counted in following reviews of the same product. The words remaining after this filtering process were added per each review. After removing from the pool of terms of online reviews all of those terms that were previously assigned to the recommendation or the corroboration information category, the 1048 terms remaining were classified as opinion terms. The number of times that any of those opinion terms appeared in the textual portion of each review and not appeared in previous reviews of the same product was calculated and summed for each of them.

The entropy values of the recommendation, unique corroboration, and unique opinion terms for each review were calculated as the number of words for each review in these categories added beyond the number of words provided by the seller/manufacturer in the product description. This provides a degree of contribution of terms by the review to each of those three categories and allows to put them in the context of what information is already available from the seller (its scarcity). The en tropy for each category in each review was then estimated using the maximum likelihood (ML) method [53]. This method does not assume any prior distribution of the variable and it estimates entropy from discrete counts. The underlying probability mass function of a discrete random variable is in practice unknown, hence H and $\theta _ { \mathrm { k } }$ in Eq. (1) are estimated from observed counts $\mathrm { { y } } _ { \mathrm { { k } } } \geq 0 .$ The ML estimator derived from Eq. (1) is:

![](/api/attachments/RHTYH2ZE/fulltext/images/07597882ca8651827e8af6785094bf8c03deada54238a32342bde87515c5eccb.jpg)  
Fig. 4. Operationalization of Corroboration Terms.

$$
\widehat {\mathrm{H}} ^ {\mathrm{ML}} = - \sum_ {\mathrm{k} = 1} ^ {\mathrm{p}} \widehat {\theta} _ {\mathrm{k}} ^ {\mathrm{ML}} \log (\widehat {\theta} _ {\mathrm{k}} ^ {\mathrm{ML}})\tag{2}
$$

Eq. (2) is constructed by plugging the ML frequency estimates

$$
\widehat {\Theta} _ {\mathrm{k}} ^ {\mathrm{ML}} = \frac {\mathbf {y} _ {\mathrm{k}}}{\mathbf {n}}\tag{3}
$$

into Eq. (1), with $\displaystyle \boldsymbol { \mathsf { n } } = \sum _ { \boldsymbol { \mathsf { k } } = 1 } ^ { \boldsymbol { \mathsf { p } } } \mathbf { y } _ { \boldsymbol { \mathsf { k } } }$ being the total number of counts. Note that despite there being only a few recommendation terms, the recommen dation entropy could be high if an individual review contains many words ascribed to the recommendation information category, such as “recommend” or “suggest” (i.e. if an individual review contains many recommendations). For example, if the fifth review contained 2 recommendation words, 3 corroboration words, and 16 opinion words, and the product description of the fifth light bulb contains 51 words, then the entropy values of the fifth review in the dataset are recommendation entropy(51, 2) = 0.16, corroboration entropy(51, 3) = 0.21, opinion entropy(51, 16) = 0.55. See Appendix A for an annotated calculation. Fig. 5 summarizes the methodology for the text analysis of the reviews in this study.

The following linear model was run to test the research hypotheses<sup>6</sup>

$$
\begin{array}{r l} \text { helpfulness   score } & = \beta_ {0} + \beta_ {1} \text { opinion   entropy } + \beta_ {2} \text { corroboration   entropy } \\ & \quad + \beta_ {3} \text { recommendation   entropy } + \beta_ {4} \text { number   of   stars } \\ & \quad + \beta_ {5} \text { verification   of   purchase   (1 } \\ & = \text { yes,   0   =   no) } + \beta_ {6} \text { product   novelty   (LED } \\ & = 1, \text { incandescent } \\ & = 0) + \beta_ {7} \text { posting   order } + \beta_ {8} \text { number   of   evaluations } \end{array}\tag{4}
$$

The weighting criterion, number of words $( \mathbf { w _ { i } } ) ,$ , is the minimized weighted sum of squares:

$$
\sum_ {i - 1} ^ {n} w _ {i} (y _ {i} - x _ {i} \beta) ^ {2}\tag{5}
$$

## 5. Analysis

Descriptive statistics are shown in Table 2. Model 1 includes all the independent variables in $\operatorname { E q . }$ . (4) as well as the weighting criterion (Log (Number of Words)). The descriptive statistics in Table 2 are also shown by product type. LED reviews were more helpful, had more words, and higher entropies, but fewer stars. LED, however, had fewer confirmed purchases.

The research model in Fig. 2 was tested with linear regression, adding the logarithm of the number of words as a weight. Results are shown in Model 1 in Table 3. To test for endogeneity, statistically measured as a significant correlation between the regression error terms and any of the independent variables, we extracted the residuals in Model 1 and correlated them with each of the independent variables. All the resulting rho values were highly insignificant,<sup>7</sup> except with the control number of evaluations with rho= –0.0793 and p-value = 0.03. Checking the distribution of the number of evaluations showed that only 348 of the datapoints had a number greater than 0. Accordingly, as an extra test, we reran the analysis only on those datapoints. That is shown in Model 2, producing equivalent results, except that $\mathrm { H } _ { 1 }$ was not even marginally significant. (It was not possible to run a model in which the Number of Evaluations is zero because there were no Helpfulness scores for those.) All the resulting rho values in Model 2 were highly insignif icant, with a p-value above 0.63. Significant coefficients in Table 3 are emphasized in bold. Running Model 2 separately for each product type produced a nuanced picture where only among LED datapoints was any

![](/api/attachments/RHTYH2ZE/fulltext/images/ba8c204a00d2ff6c9feb39c1278fd7c0505af9ddf8a498e65de4ab138b06abc6.jpg)  
Fig. 5. Summary of the Text Analysis Process.

of the hypotheses significant.

As shown, overall, in Model 1, the higher the unique opinion entropy in a review, marginally, the more helpful the review was, marginally supporting H . Contrary to this, greater unique corroboration entropy does not contribute to helpfulness, not supporting H . Higher recom mendation entropies increased the helpfulness of the review, supporting H , but not so with incandescent light bulbs maybe because consumers know those already. As might be expected, more stars and higher eval uations increased helpfulness. However, we caution against making any issue of that because the number of stars is a significant predictor of helpfulness score in Table 3 despite being insignificantly correlated in Appendix B. This is apparently because of its interplay with the number of helpfulness evaluations because when the number of helpfulness evaluations is removed from any of the models in Table 3 then the number of stars ceases to be a significant predictor of helpfulness. The verification of purchase does not contribute to make a review more helpful. The results of the analysis for the variable posting order suggest that, at least in our data, there is no “early bird bias” effect. The dis cussion section will elaborate on all of this.

## 6. Discussion

Online reviews are clearly important to consumers and their help fulness scores do increase as their number of stars increases. as Pan and Zhang [17] suggested, but, at least in our data that is because of the interplay of the number of stars and the number of evaluations. The results of this study, however, do not support the importance of verifi cation of purchase. It may be that if there are sufficient cues in the re view about the actual interaction with the product, reporting this element could be irrelevant. Adding to theory and practice beyond previous studies of online reviews. this study shows that the written component of the online reviews can contribute to their helpfulness, but in a perhaps less than an obvious manner. Importantly, the results also show that, overall, entropy, and specifically recommendation entropy (and unique opinion only marginally) contribute to helpfulness, but in a nuanced manner. This is not the case of unique corroboration entropy. The analysis suggests that it is only recommendation entropy, and only with LEDs where more information is sought by the consumers, that contributes to helpfulness. According to our results, entropy is not a predictor for more established and of lesser interest incandescent lightbulbs. The “Limitations” section of this piece suggests that, since product type may play an important role in the analysis, future research might replicate this study with a broader scope of products. The pro posed classification of the written portion of the reviews into recommendations, corroboration, and opinion entropy thus adds nuanced insight into what type of entropy increases helpfulness. This suggests that encouraging reviewers to express their unique and specific opinions should be considered. It seems that people access online re views because they want to learn from other consumers, but, apparently, selectively. Recommendations are decision making heuristics [61] that review readers value positively and therefore, including explicit rec ommendations in the review should be encouraged. However, telling these readers what they can learn directly from the manufacturer, has little impact, at least in these data.

## 6.1. Contribution to theory

Online reviews are clearly helpful. Discovering what exactly makes them helpful is the topic of this study. Specifically, what is the contri bution of different types of review entropy that makes it helpful to customers. The approach this study took, analyzing opinion, corrobo ration, and recommendation entropies, rather than number of words as done by previous research, sheds new light on that question. Putting this approach into context, past research that looked at the written portion of online reviews examined text length [17], the impact of linguistic styles [84], the role of emotions [e.g. 70,85], the influence of very specific features of the product in the text of the review [e.g. 49,86], or the in fluence of concepts (e.g. “dimmable light bulb”) included in the text [16, 20]. This study focused on the entropy of the words based on their category in online reviews. The methodological approach in this research is automatic and is virtually applicable to all types of contexts (including both products and services). This allows gaining instant in sights from the textual portion of reviews to make real-time predictions of the helpfulness of new reviews. By looking at specific words, the study applies a finer level of granularity than previous literature [e.g. 16], allowing reviews to contain several of these informational element simultaneously, arguably a more realistic approach.

The study of entropy could shed new light on ecommerce research. To the best of our knowledge, only Singh et al. [19] studied the impact of information entropy on review helpfulness, and only general informa tion entropy at that. Classifying terms into recommendation, unique opinion, and unique corroboration entropy types and quantifying their contribution to helpfulness adds new insight into what makes reviews helpful. The data also show that LED product reviews have more recommendation, unique corroboration, and unique opinion entropy, suggesting that the reviews differ more in their choice of words than established product reviews do (see Table 2). Less predictability on what words are used in the review, i.e. entropy, might be because more words are needed for describing products that are less widely accepted in the market than more established products, such as incandescent light bulbs.

Table 3 Linear Regression Results.

<table><tr><td colspan="2">Hypothesis</td><td>Model 1Estimate Std. Estimate (Std.Error)</td><td>Model 2Estimate Std. Estimate (Std.Error)</td><td>Model 2 IncandescentEstimate Std. Estimate (Std.Error)</td><td>Model 2 LEDEstimate Std. Estimate (Std.Error)</td></tr><tr><td></td><td></td><td>-2.41</td><td>-3.81</td><td>-0.46</td><td>-2.64</td></tr><tr><td></td><td>Intercept</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td></td><td></td><td>(0.57)***</td><td>(1.07)***</td><td>(2.22)*</td><td>(0.76)***</td></tr><tr><td></td><td></td><td>1.40</td><td>2.27</td><td>4.87</td><td>1.88</td></tr><tr><td rowspan="3"> $H_1$ </td><td rowspan="3">Unique Opinion Entropy</td><td>0.05</td><td>0.07</td><td>0.16</td><td>0.05</td></tr><tr><td>(0.77)a</td><td>(1.46)</td><td>(2.85)</td><td>(1.20)</td></tr><tr><td>-1.67</td><td>-2.08</td><td>-0.18</td><td>-2.84</td></tr><tr><td rowspan="3"> $H_2$ </td><td rowspan="3">Unique Corroboration Entropy</td><td>-0.04</td><td>-0.05</td><td>-0.0042</td><td>-0.07</td></tr><tr><td>(0.96)</td><td>(1.81)</td><td>(4.09)</td><td>(1.44)</td></tr><tr><td>4.68</td><td>6.82</td><td>-0.09</td><td>5.24</td></tr><tr><td rowspan="3"> $H_3$ </td><td rowspan="3">Recommendation Entropy</td><td>0.06</td><td>0.07</td><td>-0.0009</td><td>0.06</td></tr><tr><td>(1.90)*</td><td>(3.33)*</td><td>(7.28)</td><td>(2.64)*</td></tr><tr><td>0.50</td><td>0.70</td><td>0.78</td><td>0.58</td></tr><tr><td rowspan="2">Control</td><td rowspan="2">Number of Stars</td><td>0.14</td><td>0.16</td><td>0.22</td><td>0.12</td></tr><tr><td>(0.08)***</td><td>(0.15)***</td><td>(0.26)**</td><td>(0.13)***</td></tr><tr><td rowspan="4">Control</td><td rowspan="4">Verification of Purchase (Bought=1)</td><td>-0.49</td><td>-0.48</td><td>0.20</td><td>-0.27</td></tr><tr><td>-0.04</td><td>-0.03</td><td>0.0087</td><td>-0.02</td></tr><tr><td>(0.34)</td><td>(0.62)</td><td>(1.70)</td><td>(0.46)</td></tr><tr><td>0.0011</td><td>0.0021</td><td>0.0073</td><td>-0.0056</td></tr><tr><td rowspan="3">Control</td><td rowspan="3">Posting Order</td><td>0.0189</td><td>0.03</td><td>0.16</td><td>-0.04</td></tr><tr><td>(0.0015)</td><td>(0.0031)</td><td>(0.0043)</td><td>(0.0045)</td></tr><tr><td>0.66</td><td>0.66</td><td>0.24</td><td>0.81</td></tr><tr><td rowspan="3">Control</td><td rowspan="3">Number of Evaluations</td><td>0.77</td><td>0.73</td><td>0.25</td><td>0.93</td></tr><tr><td>(0.02)***</td><td>(0.03)***</td><td>(0.07)**</td><td>(0.03)***</td></tr><tr><td>0.44</td><td>0.95</td><td></td><td></td></tr><tr><td rowspan="2">Control</td><td rowspan="2">Product Type (LED = 1)</td><td>0.04</td><td>0.07</td><td></td><td></td></tr><tr><td>(0.27)</td><td>(0.57)</td><td></td><td></td></tr><tr><td></td><td>R square</td><td>0.64</td><td>0.61</td><td>0.14</td><td>0.87</td></tr></table>

Significance levels \*\*\* 0.001, \*\* 0.01, \* 0.05.  
<sup>a</sup> Unique opinion entropy is marginally significant, p-value = 0.07.

The results also suggest that is not only the raw number of words, i.e. how much is written, that increases the helpfulness perception of the review—an approach common in the early literature [e.g. 2]—but, rather, how unique the words that are used in the review are. It is not that previous research did not recognize the importance of “what” versus “how much,” but rather that apparently previous research did not have the tools to objectively do so. Indeed, Filieri [63] suggested that potential buyers are more influenced by the quality of the information (information quality being defined by information depth and breadth, relevance, credibility, and factuality) than by information quantity. Mudambi and Schuff [5] also suggested that information depth is an important predictor of review helpfulness. Cao et al. [36] found that semantic characteristics (related to the “substance” of the text) are the most important in determining helpfulness votes. Entropy allows the analysis of the text portion through perhaps more nuanced lenses.

As to product type, the analyses, at least in these data, suggest that LED have higher assessed review helpfulness. LED was at the time a product category of growing interest among consumers as reflected by a growing market share trend [81] and, in Table 2, as the average number of helpfulness evaluations. At the time of the data collection, LEDs still represented a very small portion of the market (specifically, less than 8% [81]). It might be therefore that, possibly, readers were less familiar with this product type at the time of the data collection, 2015, than with the incandescent light bulbs category, and therefore found the infor mation to be more unique and therefore, more helpful. That is consistent with previous research that suggested that when buyers lack an ability to evaluate what characteristics of a product are relevant, they rely more heavily on the opinions and recommendations from other buyers [26].

Table 3 also suggests the lack of an “early bird bias,” which would make early reviews more influential on review helpfulness due to their posting order, instead of their actual content. Although this can be arguably a product category or a sample effect, the lack of this effect highlights the relevance of the actual content of the textual portion in determining the helpfulness of a review, and specifically the different impacts of the three types of information entropy identified in this study.

In our data, more explicit recommendations, and marginally more unique opinion entropy, of previous customers increased the helpfulness ratings of the review. However, the inclusion in the review of the terms used by the seller, such as referring to essential features and charac teristics, was unrelated to helpfulness. It may be that the inclusion of corroborating words is perceived as some kind of manipulation of the reviews by the vendor or manufacturer, as has been suggested [21,87], and so it does not contribute to helpfulness. The data, however, support that potential customers may expect reviewers to express their opinions about the product, as previously suggested [88], as well as recommen dations [14,16].

Verified purchase does not contribute to review helpfulness. That helpfulness is not significantly impacted by the validation that the reviewer purchased the product may be because (1) online reviews are considered a trustworthy source of purchase information per se [89], (2) customers trust other peer consumers’ information more than the in formation provided by marketers and advertisers [29] and (3) the tex tual portion can provide enough cues and signals about the product itself and the purchase experience that can assure the user that it was actually bought by the reviewer.

## 6.2. Contribution to methodology

Another contribution of this study is in suggesting a new method ology to automatically assess the textual component of online reviews through their entropy and showing that aspects of that entropy con tributes to helpfulness. To the best of our knowledge, this is also the first study that incorporates the information context through entropy in its methodology, both considering the information provided by sellers and opinion and corroboration words provided in previous reviews. High entropy words are words that are used infrequently, i.e. words whose use cannot be as readily predicted as low entropy words. Having rela tively unique opinion and recommendation words in the review makes the review more helpful, presumably by introducing content that is relatively more unique, especially in a context in which sellers’ infor mation is scarce. The methodology proposed allows performing an automatic and objective detection, quantification, and analysis of the impact of words on review helpfulness. Differing from previous litera ture that employed manual annotation in their methodology [e.g. 16, 20], this study suggests an automatic approach (only possible through entropy quantification). Expanding the work of Singh et al. [19], our methodology distinguishes different types of entropies, puts them in context of preexisting information, and applies a finer granularity by looking at individual high entropy words.

This methodological framework might have potential beyond the context of online consumer reviews and ecommerce. Social scientists may be able to apply this methodology to study considerably larger bodies of text than the traditional qualitative approaches [e.g. 20], especially as it requires no human coders or raters. Social sciences have extensively employed external independent raters to code textual in formation from individuals. This textual information is usually provided in a great variety of forms, such as open-ended responses, descriptions, or thoughts after a marketing stimulus [90]. Despite being widely used, previous research [91] questioned the internal validity of research de signs based on independent raters due to the “moderate to poor agree ment” (p. 160). The methodology presented in this study could constitute a potential objective and automatic alternative for social scientists. A similar methodology as the one presented in this paper could be applied to analyze other sources of online data, such as social media or specialized blog data.

## 6.3. Limitations

The data analyzed dealt with 16 products from two different cate gories that were deliberately chosen because they are essentially func tionally equivalent: both product categories are used for the same purpose of producing artificial light. As research suggests that product type may play an important role in determining the helpfulness rating of online reviews [e.g. 5,17,92], replicating the study with a broader scope of products may reveal new insight. This may be especially relevant in the case of the opinion type of information, which may be much contextualized. What is perceived as helpful within a specific setting may not be perceived as such within a different one. In this sense, practitioners may be interested in characterizing and making more accessible those reviews that are considered more helpful. A potential way to achieve this goal is through an extensive characterization of how the informational elements impact the helpfulness rating of reviews across different product categories.

The methodology presented in this paper is focused on word entropy and the different sources of information available in individual online reviews. It does not address other non-strictly informational variables that may impact review helpfulness, such as sentiments. Another limi tation is that the study does not address claims of expertise or social cues that may appear in online reviews, as the data employed contains no reviewer-related factors. While Hong et al. [18] found that both reviewer information disclosure and reviewer expertise positively impact review helpfulness, Malik and Hussain [48] suggested that review-related factors are more important antecedents of review help fulness than reviewer ones. Our research can be extended to study the impact of reviewer-related factors, together with the three types of in formation entropy.

## 6.4. Conclusions

New automatic methodological approaches are needed to achieve a comprehensive understanding of the role of the different informational elements available online, especially in the case of textual data that, nowadays, is ubiquitous for online users. Textual data are readily available to influence the purchase intentions of potential customers anytime. As an example, it is currently estimated that 511,200 tweets, 18,100,000 texts, and 188,000 emails are sent per minute [93]. This study proposes an application of entropy that could open new avenues into studying what elements of such information are more important.

## CRediT authorship contribution statement

Jorge E. Fresneda: Writing - original draft, Conceptualization, Methodology. David Gefen: Writing - review & editing, Formal analysis, Software.

## Declaration of Competing Interest

The authors report no declarations of interest.

## Appendix A

## Entropy Calculation Illustration

The first portion of this appendix illustrates how unique corrobora tion, unique opinion, and recommendation entropies are calculated in this study with a small example of one product description and two reviews. Table 4 shows a product description extracted from our dataset as well as two reviews of the same product, following their posting order (i.e. Review #1 was posted before Review #2). Table 4 uses a color code to identify unique corroboration (red), unique recommendation (green), and opinion (blue) words the same way that they were identified in the paper. Their entropies are shown on the right side, calculated consid ering the number of words in the product description. This approach allows the study to consider the context of information provided by both sellers and also previous reviews. Double-strikethrough words are corroboration or opinion terms that appear in the previous review.

Table 5 shows the results of an experiment of the two different values of entropy (in the example, unique corroboration entropy) for the same number of matching words in a review (“2700 K” and “white”) with regard to a context in which the product description provided contains 71 words (Product Description #1) versus a context of only 28 words (Product Description #2). This further illustrates the differential impact of the seller information context on the entropy calculation. (Note that Review #1 is associated in the dataset to Product Description #1 and not to Product Description #2. Review #1 was contrasted against Product Description #2 just for illustration purposes. Note as well that the entropy value in the 28-word context almost doubles the entropy value in the 71-word one.)

Corroboration, Recommendation, Opinion Entropy Calculation Example. (For interpretation of the references to colour in this table, the reader is referred to the web version of this article).

<table><tr><td>Product Description</td><td colspan="2">Philips 432211 19-watt (100-Watt) A21 LED 2700K (Warm White) Light Bulb, Dimmable Philips 19-Watt A21 LED replaces your 100-Watt A21, saving you up to $223 in energy costs ideal for residential use in kitchens, living rooms and dining rooms and commercial use in offices and retail spaces Fully dimmable, instant-on and will not fade fabrics or colors Extra long life - lasts at least 22.8 years Philips Internal Model # 9290002596</td><td>Word Count = 71</td></tr><tr><td rowspan="3">Review #1</td><td rowspan="3">All were the 2700K soft white color. All were about the same, less orangey yellow than incandescent but far from that blue green jewelry store color. Would highly recommend.</td><td>Unique Corroboration Words = 2</td><td>Unique Corroboration Entropy (71, 2) = 0.13</td></tr><tr><td>Recommendations = 1</td><td>Recommendation Entropy (71, 1) = 0.07</td></tr><tr><td>Unique Opinion Words = 13</td><td>Unique Opinion Entropy (71, 13) = 0.43</td></tr><tr><td>Review #2</td><td>I highly recommend this bulb for its economy and quality. It only comes in 2700K or the equivalent</td><td>Unique Corroboration Words = 3</td><td>Unique Corroboration</td></tr><tr><td rowspan="3"></td><td rowspan="3">of a soft white color, approximately 100-Watt equivalent of incandescent. Provides ample lighting in my living room for most evenings.</td><td></td><td>Entropy (71, 3) = 0.17</td></tr><tr><td>Recommendations = 1</td><td>Recommendation Entropy (71, 1) = 0.07</td></tr><tr><td>Unique Opinion Words = 12</td><td>Unique Opinion Entropy (71, 12) = 0.41</td></tr></table>

Impact of Product Description Length in Entropy Calculation. (For interpretation of the references to colour in this table, the reader is referred to the web version of this article).

<table><tr><td>Product Description # 1</td><td colspan="2">Philips 432211 19-watt (100-Watt) A21 LED 2700K (Warm White) Light Bulb, Dimmable Philips 19-Watt A21 LED replaces your 100-Watt A21, saving you up to $223 in energy costs ideal for residential use in kitchens, living rooms and dining rooms and commercial use in offices and retail spaces Fully dimmable, instant-on and will not fade fabrics or colors Extra long life - lasts at least 22.8 years Philips Internal Model # 9290002596</td><td>Word Count = 71</td></tr><tr><td>Product Description # 2</td><td colspan="2">Feit A/OM2200R/LED A19 Performance LED 150W Equivalent, 2700k Lasts 22.8 years/25,000 Hours Fully Dimmable and instant brightness 150 Watt Equivalent. Warm white Uses up to 79% less energy</td><td>Word Count = 28</td></tr><tr><td rowspan="2">Review #1</td><td rowspan="2">All were the 2700K soft white color. All were about the same, less orangey yellow than incandescent but far from that blue green jewelry store color. Would highly recommend.</td><td rowspan="2">Unique Corroboration Words = 2</td><td>Unique Corroboration Entropy (71, 2) = 0.13</td></tr><tr><td>Unique Corroboration Entropy (28, 2) = 0.24</td></tr></table>

Appendix B. Correlation Matrix

<table><tr><td></td><td>Help. Score</td><td>Unique Opinion Entropy</td><td>Unique Corr. Entropy</td><td>Recom. Entropy</td><td>#  $Stars^a$ </td><td>Verified Purchase</td><td>Posting Order</td><td># Help. Evals.</td><td>Product Type</td><td>Log (#words)</td><td>Unique Opinion Words</td><td>Unique Corr. Words</td><td>Recom. Words</td></tr><tr><td>Help. Score</td><td>1.00</td><td>0.14***</td><td>0.01</td><td>0.25***</td><td>0.02</td><td>-0.23***</td><td>0.09</td><td>0.69***</td><td>0.19***</td><td>0.33***</td><td>0.10***</td><td>0.01</td><td>0.01</td></tr><tr><td>Unique Opinion Entropy</td><td></td><td>1.00</td><td>0.61***</td><td>0.19***</td><td>-0.10</td><td>-0.32***</td><td>-0.36***</td><td>0.11*</td><td>0.22***</td><td>0.66***</td><td>0.67***</td><td>0.44***</td><td>0.18***</td></tr><tr><td>Unique Corr. Entropy</td><td></td><td></td><td>1.00</td><td>0.15***</td><td>-0.05</td><td>-0.18***</td><td>-0.40***</td><td>-0.03</td><td>0.18***</td><td>0.46***</td><td>0.63***</td><td>0.78***</td><td>0.21***</td></tr><tr><td>Recom. Entropy</td><td></td><td></td><td></td><td>1.00</td><td>-0.10*</td><td>-0.19***</td><td>0.03</td><td>0.23***</td><td>0.11*</td><td>0.33***</td><td>0.22***</td><td>0.15***</td><td>0.43***</td></tr><tr><td># Stars</td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.25***</td><td>0.14**</td><td>-0.19***</td><td>-0.11*</td><td>-0.06</td><td>-0.06</td><td>-0.03</td><td>-0.03</td></tr><tr><td>Verified Purchase</td><td></td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.09</td><td>-0.26***</td><td>-0.37***</td><td>-0.42***</td><td>-0.29***</td><td>-0.16***</td><td>0.01</td></tr><tr><td>Posting Order</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.10</td><td>-0.40***</td><td>-0.003</td><td>-0.27***</td><td>-0.28***</td><td>-0.14***</td></tr><tr><td># Help Evals</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.17***</td><td>0.33***</td><td>0.11**</td><td>0.004</td><td>0.02</td></tr><tr><td>Product Type</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.27***</td><td>0.25***</td><td>0.18***</td><td>0.06</td></tr><tr><td>Log (#words)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.57***</td><td>0.38***</td><td>0.11**</td></tr><tr><td>Unique Opinion Words</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.81***</td><td>0.19***</td></tr><tr><td>Unique Corr. Words</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.21***</td></tr><tr><td>Recom. Words</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.00</td></tr></table>

\*\*\* Significant at 0.001.

\*\*Significant at 0.01.

\*Significant at 0.05.

The number of stars is a significant predictor of helpfulness score in Table 3 despite being insignificantly correlated in this appendix is apparently because of its interplay with the number of helpfulness evaluations. When the number of helpfulness Evaluations is removed from any of the models in Table 3, then the number of stars ceases to be a significant predictor of helpfulness.

## References

[1] R. Filieri, F. McLeay, B. Tsui, Z. Lin, Consumer perceptions of information helpfulness and determinants of purchase intention in online consumer reviews of services, Inf. Manag. 55 (2018) 956–970.

[2] J.A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book

[3] Y. Wang, J. Wang, T. Yao, What makes a helpful online review? A meta-analysis of review characteristics, Electron. Commer. Res. (2018).

[4] Y. Chen, J. Xie, Online consumer review: word-of-mouth as a new element of marketing communication mix, Manage. Sci. 54 (2008) 477–491.

[5], S.M. Mudambi. D. Schuff, What makes a helpful online review? A study of customer reviews on Amazon.com, Mis O. 34 (2010) 185–200.

[6] MJ. Metzger. AJ. Flanagin. R.B. Medders, Social and heuristic approaches to credibility evaluation online, J. Commun, 60 (2010) 413–439.

[7] P.K. Chintagunta, S. Gopinath, S. Venkataraman, The effects of online user reviews on movie box office performance: accounting for sequential rollout and aggregation across local markets, Mark. Sci. 29 (2010), 944+.

[8] K. Floyd, R. Freling, S. Alhoqail, H.Y. Cho, T. Freling, How online product reviews affect retail sales: a meta-analysis, J. Retail. 90 (2014) 217–232.

[9] Y. Liu, Word of mouth for movies: its dynamics and impact on Box office revenue, J. Mark, 70 (2006) 74–89

[10] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating role

[11] P.-Y. Chen, S. Dhanasobhon, M.D. Smith, All Reviews Are Not Created Equal: the Disaggregate Impact of Reviews and Reviewers at Amazon. Com. Available at SSRN: 2008 http://ssrn com/abstract=918083

[12] C. Capoccia, Online reviews are the Best thing that ever happened to small businesses, Forbes. 2018. Forbes.com

[13] S. Zhou, Z. Qiao, Q. Du, G.A. Wang, W. Fan, X. Yan, Measuring customer agility from online reviews using big data text analytics, J. Manag. Inf. Syst. 35 (2018) 510-539.

[14] X. Lu, Y. Li, Z. Zhang, B. Rai, Consumer learning embedded in electronic word of mouth, J. Electron. Commerce Res. 15 (2014) 300–316

[15] T.Y. Lee, E.T. Bradlow, Automated marketing research using online customer reviews, J. Mark. Res. 48 (2011) 881–894.

[16] A. Qazi, K.B. Shah Syed, R.G. Raj, E. Cambria, M. Tahir, D. Alghazzawi, A conceptlevel approach to the analysis of online review helpfulness, Comput. Human Behav. 58 (2016) 75–81

[17] Y. Pan, J.Q. Zhang, Born unequal: a study of the helpfulness of user-generated

[18] H. Hong, D. Xu, G.A. Wang, W. Fan, Understanding the determinants of online review helpfulness: a meta-analytic investigation, Decis. Support Syst. 102 (2017) 1–11.

[19] J.P. Singh, S. Irani, N.P. Rana, Y.K. Dwivedi, S. Saumya, P. Kumar Roy, Predicting

[20] T.L. Ngo-Ye, A.P. Sinha, A. Sen, Predicting the helpfulness of online reviews using a scripts-enriched text regression model Expert Syst Appl 71 (2017) 98–110

[21] J. Qi, Z. Zhang, S. Jeon, Y. Zhou, Mining customer requirements from online reviews: a product improvement perspective, Inf, Manag, 53 (2016) 951–963

[22] J.E. Fresneda, D. Gefen, A semantic measure of online review helpfulness and the importance of message entropy, Decis. Support Syst. 125 (2019) 113117.

[23] R.A. King, P. Racherla, V.D. Bush, What we know and don’t know about online word-of-mouth: a review and synthesis of the literature. J. Interact. Mark. 28 (2014) 167–183.

[24] D.L. McFadden, K.E. Train, Consumers’ evaluation of new products: learning from

[25] J.J. Brown, P.H. Reingen, Social ties and word-of-mouth referral behavior,

[26] B. Bickart. R.M. Schindler. Internet forums as influential sources of consumer information, J. Interact, Mark, 15 (2001) 31–40

[27] D. Godes. D. Mavzlin. Using online conversations to study word-of-mouth communication, Mark, Sci, 23 (2004), 545+.

[28] D. Mavzlin. Promotional chat on the internet, Mark, Sci. 25 (155–163) (2006) 201

[29] S. Sen, D. Lerman, Why are you telling me this? An examination into negative consumer reviews on the Web, J. Interact. Mark. 21 (2007) 76–94.

[30] T. Hennig-Thurau, K.P. Gwinner, G. Walsh, D.D. Gremler, Electronic word-of mouth via consumer-opinion platforms: What motivates consumers to articulate themselves on the Internet? J. Interact. Mark. 18 (2004) 38

[31] C. Dellarocas, The digitization of word of mouth: promise and challenges of online feedback mechanisms, Manage. Sci. 49 (2003) 1407–1424.

[32] M. Li, L. Huang, C.-H. Tan, K.-K. Wei, Helpfulness of online product reviews as seen by consumers: source and content features, Int. J. Electron. Commer. 17 (2013) 101–136.

[33] A. Ghose, P.G. Ipeirotis, B. Li, Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content, Mark. Sci. 31 (2012) 493–520.

[34] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Trans. Knowl. Data Eng. 23 (2011) 1498–1512.

[35] J.M. Spool. The magic behind Amazon's 2.7 billion dollar question. User Interface Engineering. 2009.

[36] Q. Cao, W. Duan, Q. Gan, Exploring determinants of voting for the “helpfulness” of online user reviews: a text mining approach, Decis. Support Syst. 50 (2011)

[37] P.-J. Lee, Y.-H. Hu, K.-T. Lu, Assessing the helpfulness of online hotel reviews: a classification-based approach, Telemat. Inform. 35 (2018) 436–445.

[38] M.J. S´anchez-Franco, A. Navarro-García, F.J. Rond´an-Cataluna, ˜ Online customer service reviews in urban hotels: a data mining approach, Psychol. Mark. 33 (2016) 1174-1186.

[39] S. Moon, W.A. Kamakura, A picture is worth a thousand words: translating product reviews into a product positioning map, Int. J. Res. Mark. (2016).

[40] W.W. Moe, M. Trusov, The value of social dynamics in online product ratings forums, J. Mark. Res. 48 (2011) 444–456.

[42] W. Duan, B. Gu, A.B. Whinston, Do online reviews matter? — an empirica investigation of panel data, Decis. Support Syst. 45 (2008) 1007–1016.

[43] I.E. Vermeulen, D. Seegers, Tried and tested: the impact of online hotel reviews on consumer consideration, Tour. Manag. 30 (2009) 123–127.

[44] G. Packard, J. Berger, How language shapes word of mouth’s impact, J. Mark. Res. 54 (2017) 572–588.

[45] P. Resnick, R. Zeckhauser, Trust among strangers in internet transactions: empirical analysis of eBay’s reputation system. Advances in Applied Microeconomics, Emerald Group Publishing, Bingley, UK, 2002, pp. 127–157.

[47] N. Jindal, B. Liu, Mining Comparative Sentences and Relations, AAAI, 2006, pp. 9.

[46] N. Jindal, B. Liu, Identifying comparative sentences in text documents, in: 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. ACM. 2006, pp. 244–251

[48] M.S.I. Malik, A. Hussain, An analysis of review content and reviewer variables that contribute to review helpfulness. Inf. Process. Manag. 54 (2018) 88–104.

[49] N. Archak, A. Ghose, P.G. Ipeirotis, Deriving the pricing power of product features by mining consumer reviews, Manage, Sci, 57 (2011) 1485–1509.

[50] C.E. Shannon, A mathematical theory of communication, Bell Syst. Tech. J. 27 (379-423) (1948) 623–656.

[51] J. Belzer, Information theory as a measure of information content, J. Am. Soc. Inf Sci. 24 (1973) 300–304.

[52] J. Machta, Entropy, information, and computation, Am. J. Phys. 67 (1999)

[53] J. Hausser, K. Strimmer, Entropy inference and the James-Stein Estimator, with application to nonlinear gene association networks, J. Mach. Learn. Res. 10 (2009) 1469-1484.

[54] J. Ross, The information content of accounting reports: an information theory perspective, Information 7 (2016) 48.

[55] G.J. Klir, Generalized information theory: aims, results, and open problems, Reliab Eng. Syst. Saf. 85 (2004) 21–38.

[56] L.A. Zadeh, Toward a generalized theory of uncertainty (GTU)––an outline, Inf. Sci.

[57] R. Kohli, S. Devaraj, M.A. Mahmood, Understanding determinants of online consumer satisfaction: a decision process perspective, J. Manag. Inf. Syst. 21 (2004) 115–135.

[58] S. Lu, J. Wu, S.-L. Tseng, How online reviews become helpful: a dynamic perspective, J. Interact. Mark. 44 (2018) 17–28.

[59] J. Liu, Y. Cao, C.-Y. Lin, Y. Huang, M. Zhou, Low-Quality Product Review Detection in Opinion Summarization, EMNLP-CoNLL, 2007, pp. 334–342.

[60] J. Lee, J.-N. Lee, B.C.Y. Tan, Antecedents of cognitive trust and affective distrust and their mediating roles in building customer loyalty, Inf. Syst. Front. 17 (2015) 159–175.

[61] D. Smith, S. Menon, K. Sivakumar, Online peer and editorial recommendations, trust, and choice in virtual markets. J. Interact. Mark. 19 (2005) 15–37.

[62] C. Shapiro, H.R. Varian, Information Rules, Harvard Business School Publications Boston, MA. 1999.

[63] R. Filieri. What makes online reviews helpful? A diagnosticity-adoption framework to explain informational and normative influences in e-WOM. J. Bus. Res. 68 (2015)1261-1270.

[64] S.L.T. Alex, G. Prendergast, Is a "star" worth a thousand words? Eur. J. Mark. 43 (2009) 1269–1280.

[65] B. News, Samsung probed in Taiwan over’ fake web reviews’. BBC News Technology, 2013.

[66] D. Biswas, Economics of information in the Web economy: towards a new theory? J. Bus. Res. 57 (2004) 724–733.

[67] G.R. Faulhaber, D.A. Yao, Fly-by-night" firms and the market for product reviews, J. Ind. Econ. 38 (1989) 65–77.

[68] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Inf. Syst. Res, 19 (291–313) (2008) 393–395

[69] Y. Wan, M. Nakayama, The reliability of online review helpfulness, J. Electron. Commerce Res. 15 (2014) 179.

[70] J. Li, L. Zhan, Online Persuasion, How the written word drives WOM, J. Advert Res, 51 (2011) 239–257.

[71] R.B. Cialdini, N.J. Goldstein, Social influence: compliance and conformity, Annu. Rev, Psychol, 55 (2004) 591–621.

[72] M. Deutsch. H.B. Gerard. A study of normative and informational social influences upon individual judgment, J. Abnorm. Soc. Psychol. 51 (1955) 629.

[73] G.R. Dowling, R. Staelin, A model of perceived risk and intended risk-handlin activity, J. Consum. Res. 21 (1994) 119–134.

[74] D.I. Hawkins, D.L. Mothersbaugh, Consumer Behavior. Building Marketing Strategy, 11th ed., McGraw-Hill/Irwin, New York, NY, 2010.

[75] C.R. Wasson, Dynamic Competitive Strategy & Product Life Cycles, Press, Austin, 1978.

[76] Y. Wind, T.S. Robertson, Marketing strategy: new directions for theory and research, J. Mark. (1983) 12–25.

[77] T.K. Landauer, P.W. Foltz, D. Laham, An introduction to latent semantic analysis. Discourse Proceses 25 (1998) 259–284.

[78] D. Gefen, J.E. Endicott, J.E. Fresneda, J. Miller, K.R. Larsen, A Guide to Text Analysis with Latent Semantic Analysis in R with Annotated Code Studying Online Reviews and the Stack Exchange Community, Communications of the Association for Information Systems, 2017.

[79] T.K. Landauer, D.S. McNamara, S. Dennis, W. Kintsch, Handbook of Latent Semantic Analysis, Psychology Press, New York, NY, 2013.

[80] U.D.o. Energy, The History of the Light Bulb, 2013.

[81] N. Popovich, America’s light bulb revolution. The New York Times, 2019.

[82] P. University, WordNet, Princeton University, 2010.

[83] S.T. Dumais, Latent semantic analysis, Annu. Rev. Inf. Sci. Technol. 38 (2004) 188–230.

[84] S. Ludwig, K. de Ruyter, M. Friedman, E.C. Brüggen, M. Wetzels, G. Pfann, More than words: the influence of affective content and linguistic style matches in online reviews on conversion rates. J. Mark. 77 (2013) 87–103

[85] A. Felbermayr. A. Nanopoulos, The role of emotions for the perceived usefulness in online customer reviews. J. Interact. Mark. 36 (2016) 60–76.

[86] X. Sun, M. Han, J. Feng, Helpfulness of online reviews: examining review informativeness and classification thresholds by search products and experience products, Decis. Support Syst. 124 (2019), 113099.

[87] V.K. Singh, R. Nishant, P.J. Kitchen, Self or simulacra of online reviews: an empirical perspective, Psychol, Mark, 33 (2016) 1112–1118.

[88] N. Hu, I. Bose, N.S. Koh, L. Liu, Manipulation of online reviews: an analysis of ratings, readability, and sentiments, Decis. Support Syst. 52 (2012) 674–684.

[89] Nielsen, Consumer Trust in Online, Social and Mobile Advertising Grows, Nielsen,

[90] K. Braunsberger, R.B. Buckler, D.J. Ortinau, Categorizing cognitive responses: an empirical investigation of the cognitive intent congruency between independent raters and original subiect raters J Acad Mark Sci 33 (2005) 620–632

[91] P.L. Wright, Message-evoked thoughts: persuasion research using thought verbalizations, J. Consum. Res. 7 (1980) 151–175.

[92] S.G. Moore, Attitude predictability and helpfulness in online reviews: the role o explained actions and reactions, J. Consum. Res. 42 (2015) 30–44.

[93] DOMO, Data Never Sleeps 7.0, DOMO, 2019.

Dr Jorge Fresneda is an Assistant Professor of Digital Marketing and Marketing Analytics in the Martin Tuchman School of Management at New Jersey Institute of Technology. He has 10 years of industry experience prior to taking his doctoral degree. His lectures and workshops are focused on practical applications of artificial intelligence. text mining, and big data analytics tools. His main research focus is on the role of online information in ecommerce consumer decision-making. He holds a PhD in Marketing from the LeBow College of Business at Drexel University, an MS in Applied Statistics from UNED, and an MA in Marketing and Sales Management from EAE Business School.

David Gefen, gefend@drexel.edu, is a Professor of MIS and the Provost Distinguished Research Professor at Drexel University. Philadelphia. PA. He teaches business analytics. advanced statistical methods, management and outsourcing of information systems, and the role of interpersonal trust and its management in ecommerce and IT management. He was a senior editor at MISO and is on the editorial board of JMIS. He has authored some of the most cited papers in MIS on trust management in information systems, ecommerce, and online markets management. His research findings have been published in some of the leading journals, including MISQ, ISR, IEEE TEM, JMIS, and Omega. He is also an author of a textbook on VB.NET Programming and a book on the Art of IS Outsourcing.
