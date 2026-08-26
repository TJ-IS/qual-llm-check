---
otero_id: 2702
otero_key: "DN8JMTSZ"
title: "A social referral appraising mechanism for the e-marketplace"
authors: "Cheng-Yang Lai; Yung-Ming Li; Lien-Fa Lin"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2016.07.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A social referral appraising mechanism for the e-marketplace

Cheng-Yang Lai<sup>a</sup>, Yung-Ming Li<sup>a,</sup>\*, Lien-Fa Lin<sup>b</sup>

<sup>a</sup> Institute of Information Management, National Chiao Tung University, Hsinchu, 300, Taiwan

<sup>b</sup> Department of Information Communication, Kao Yuan University, Kaohsiung, 821, Taiwan

## A R T I C L E I N F O

Article history: Received 20 March 2015 Received in revised form 1 June 2016 Accepted 10 July 2016 Available online xxx

Keywords: Social network Social referral Trust fraud Electronic commerce

## A B S T R A C T

With the popularity of social media, in order to achieve word-of-mouth marketing, many marketers and individual sellers are actively engaged in achieving positive ratings in the e-marketplace. Although many seller review mechanisms have been developed, e-commerce market operators and consumers still face trust fraud issues. Trust is one of the major issues that confuse online purchase activities. In this paper, we develop a social referral mechanism to verify sellers based on the experiences of friends within a buyer’s social network. The proposed framework estimates the trust values of sellers from the perspective of the social network in order to stop buyers from making transactions with fraudulent sellers in the online marketplace.

ã 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

With the advance of the Internet, social media allows users to seek and share information among them. Customers rate and share experiences on all aspects of electronic commerce (EC), such as the quality of products or services and transaction experiences with vendors (individual sellers or enterprises) [27]. Online reputation is de<sup>fi</sup>ned as the collective measurement of the trustable ratings given by the members in a community [27] to help other customers select a superior target such as seller, product, service, and shop. In recent years, word-of-mouth (WOM) marketing has become one of the most signi<sup>fi</sup>cant and best-known marketing strategies. In order to use the power of WOM, many marketers pay for high ratings or positive reviews to increase sales. According to the business report provided by Gartner [16], enterprises continue to increase marketing spending on modeling online ratings and reviews. Analysts also predict that approximately 15% of all online ratings and reviews will be fake by 2014, implying that ratings and reviews are purposely modeled by companies.

To facilitate commercial activities, most EC platforms manage trust among buyers and sellers by adopting three-level ratings (positive, neutral, and negative) and opinion feedback. After transactions are completed, buyers can leave their ratings and opinions on sellers. Intuitively, positive and negative ratings would change the trust scores of sellers. However, most existing reputation systems quantify the reputational value of users or items by accumulating rating records without taking the trust concept for raters into account. That is, the overall trust score of a seller is simply calculated by the accumulation of rating records. Although many seller review mechanisms have been developed, EC market operators are still facing a trust fraud challenge. For example, fraudulent sellers on eBay enhance their reputations by trading positive seller ratings [6,11]. In addition, Zhang et al. [55] use the Taobao, which is now in the prime position in China’s EC market, as an example to present the generations of development of trust fraud techniques for faking the trustworthiness of sellers. This means that trust fraud issues have existed for many years and put buyers at the risk of making transactions with fraudulent sellers. Therefore, it is necessary to de<sup>fi</sup>ne and measure the seller’s reputation by considering the trustworthiness of raters, which makes the online rating system more reliable for buyers. In other words, how to design a referral mechanism to effectively overcome the phenomenon and diminish this effect of feedback manipulation by sellers is an important issue.

Nielsen [38] shows that approximately 70% of consumers trust online product reviews. At the same time, the report also shows that 92% of consumers trust the reviews and recommendations of their friends and family members. Trust is one of the major issues that confuse online purchases because of distrust [36]. The plausibility of the evaluation of reputation of sellers provided by the public evaluation system on the EC platform is one of the major concerns of buyers when they want to make an online transaction. In order to increase sales, sellers may attempt to improve their reputations. For example, sellers on eBay may launch an auction at a very low price and include some speci<sup>fi</sup>c words, for example

C.-Y. Lai et al. / Information & Management xxx (2016) xxx–xxx

“feedback,” in the title or product description, which hints at positive feedback [6,11]. It was easy and cheap to manipulate the trust values until eBay prohibited sellers from including any words when they raised auctions [13]. Another example is Taobao in China, where a third-party platform emerged to help sellers obtain positive feedback ratings at the end of 2006 [54]. A seller purposely sells a product at a low price (e.g., RMB 10) and publishes the offer on a third-party platform, and then the platform deducts RMB 10 from the seller. One registered member of the platform would purchase the product, con<sup>fi</sup>rm the receipt of the product, and offer a positive rating on Taobao. Finally, the third-party platform would transfer RMB 10 to this member. Currently, because fraudulent sellers manipulate fraud in careful and secret ways [4,55], fraud strategies are very hard to detect. The aim of this research is to use the power of social networks of speci<sup>fi</sup>c buyers to help them prevent trust fraud issues in the online marketplace.

In this research, instead of merely relying on the feedback from the public, which is possibly manipulated by sellers, we use the opinions expressed by the close and trusted friends extracted from a buyer’s social network to build a new reputation system – a social referral mechanism (SRM). Most existing public reputation systems aggregate the evaluations of sellers without taking the trustworthiness of the evaluators into consideration. The proposed framework identi<sup>fi</sup>es the feedback given by trustworthy evaluators (i.e., friends) to evaluate the credibility of sellers and to avoid the risk of loss on purchasing a product from a bad seller, who may have a good public reputation. Further, from a practical perspective, to our knowledge, most social network-based EC mechanisms focus on the evaluation of products rather than on sellers. Therefore, it would be helpful to consumers and expedite EC activities if a more plausible seller evaluation mechanism could be equipped in the electronic market. In this paper, we aim to develop an SRM to verify the credibility of sellers based on the experiences of friends within a buyer’s social network.

The remainder of this paper is organized as follows. The basic concepts and literature related to our research topics are provided in Section 2. In Section 3, we present the social referral model combined with social tie analysis and expertise level analysis. Section 4 describes the processes of the experiment and discusses the empirical results. Section 5 provides several concluding remarks and future research directions.

## 2. Literature review

## 2.1. Social referral

In the new world of consumer-driven content and reliance of customers on the recommendations of others, the referral engine prescribes an approach to generate and harness customer WOM for competitive advantage [48]. Product-buying decisions of customers are in<sup>fl</sup>uenced by friends. In EC, most applications of social referral programs are used for end-to-end marketing strategies. For example, Buzz Referrals [7] is an interactive marketing agency focused on referral marketing and email acquisition. Referral Rock [43] is an online customer referral service for small businesses, which could build a customer referral marketing program in minutes and get more referrals. Discovering in<sup>fl</sup>uential social nodes for expediting the diffusion of marketing information is a common referral program [12,29]. For example, Cho et al. [9] take diffusion speed and the cumulative number of adopters into account to select the opinion leaders from a social network for marketing. Kiss and Bichler [29] provide a wide review of the general centrality measures used to select in<sup>fl</sup>uencers from customer networks for online marketing. Recommender systems are another usage of social referral programs. Kautz et al. [28] combine social networks and collaborative <sup>fi</sup>ltering (CF) to recommend personalized experts and generate referral paths from a user to a recommended expert. Amin et al. [1] leverage the connections between users and their reputations to generate content recommendations. It is much more effective if content providers generate recommendations according to the reputation information consolidated from the social networks of target users [2,34]. In this paper, we develop an SRM to verify the credibility of sellers according to the experiences of friends within a buyer’s social network. The proposed framework estimates the trust values of sellers from the perspective of the social network in order to stop buyers from making transactions with fraudulent sellers in the online marketplace.

## 2.2. Source credibility theory

Credibility refers to a person’s perception of the truth of a piece of information. Source credibility theory has been proposed in WOM communication studies of consumer psychology and marketing [14,45,46]. For decades, marketers, professionals, and researchers of various <sup>fi</sup>elds have found that if information is given by a high credibility source, it has a higher impact on changing the beliefs, attitudes, or behaviors of the audience [42]. According to source credibility theory, the credibility of an information source has been commonly identi<sup>fi</sup>ed to consist of expertise, trustworthiness, co-orientation, and attraction [10,14,24,42,48]. Each factor is described in Table 1.

The basic idea of the trust and reputation system is to derive a score for users. The concept of source credibility theory is commonly used for building collaborative systems. Kwon et al. [30] employ the credibility attributes of expertise and calculate the similarity between users to estimate the trust for building a collaborative neighbor selection recommendation. Cho et al. [10] propose a collaborative reputation system based on expertise and co-orientation factors to compute a trust score. Xiong and Liu [52,53] use feedback records, similarity, and the relational context to compare the trustworthiness of peers. The aim of this research is to appropriately quantify each credibility factor for raters to adjust an online reputation system and make it more reliable for users. This is expected to decrease transaction risk for buyers.

## 2.3. Social network and recency, frequency, and monetary (RFM) analysis

Social network analysis is one of the most important mathematical and graphical analyses for identifying tie strength by investigating social interactions. The connections between people are generally built up by information exchange, for example daily chatting, sharing, and discussing [19]. Reciprocal interactions enhance interpersonal tie strength, which means that friendships go deeper if a lot of information is exchanged between two individuals. If a person has stronger ties, it indicates that the person might be more trustworthy [17,40]. In this work, tie strength between a speci<sup>fi</sup>c buyer and referral candidates is estimated by using the buyer’s interaction network and social network analysis.

The key factor descriptions of source credibility theory.

<table><tr><td>Factor</td><td>Description</td></tr><tr><td>Attractiveness</td><td>The extent to which a source elicits positive feelings from audience members, such as a desire to emulate the source in some way</td></tr><tr><td>Expertise</td><td>The extent to which a source is perceived as being capable of providing correct information</td></tr><tr><td>Co-orientation</td><td>The degree to which a source is similar to the target audience members or is depicted as having similar problems or other characteristics relating to the use of a</td></tr><tr><td>Trustworthiness</td><td>The degree to which a source is perceived of as providing information that reflects the source&#x27;s actual feelings or opinions</td></tr></table>

Recency, frequency, and monetary (RFM) analysis is a wellknown and powerful method [50] for measuring customer lifetime value according to their prior purchasing histories [20]. It is also a behavior-based analysis. Some customer information can be investigated in accordance with the extracted behaviors [25,54]. For example, Chen et al. [8] use RFM analysis to discover the sequential purchasing patterns of customers from their purchasing data. The pattern segmentation framework analyzes purchasing behaviors of customers in the <sup>fi</sup>eld of EC for managerial decision making. In this work, RFM analysis is used to estimate the expertise level of referral candidates in the speci<sup>fi</sup>c product category according to their purchase history records.

## 3. System framework

In this section, an SRM is proposed to help buyers refer to the reputations of possible sellers via their social networks. Buyers usually rely on online evaluation systems to select sellers to make transactions [27,55]. However, trust fraud issues still exist, as there are many ways to manipulate online evaluations. This increases online transaction risk for buyers. Hence, those who want to make a transaction with a seller and mistrust the of<sup>fi</sup>cial evaluation system might rather rely on the evaluations of friends if they have made transactions with the same seller. Recently, most EC platforms have linked their services with other social networking services to drive more traf<sup>fi</sup>c to their marketplaces. For example, Yahoo! Auctions in Taiwan allow users to sign into the online marketplace using their Facebook accounts. Although most current EC platforms operate without social networking services, with the advantage of linking platforms, the proposed SRM could refer to a target seller’s reputation through friends.

As shown in Fig.1, the buyer wants to make a transaction with $s _ { 1 }$ and there are four connected and experienced users $( r c _ { 1 , } r c _ { 2 } , r c _ { 3 } ,$ $r c _ { 4 } ,$ , and $r c _ { 5 } )$ that could be the target referral candidates. Although $r c _ { 3 }$ and $r c _ { 6 }$ are also experienced users, they are strangers to the buyer because they are not connected. The SRM would like them to refer the reputation of $s _ { 1 }$ for the buyer to select the reliable seller. Firstly, the attractiveness analysis module analyzes the explicit (direct connection, e.g., the connection between buyer and $r c _ { 1 }$ and $r c _ { 2 } )$ and implicit (indirect connection, $\mathbf { e . g . }$ , the connection between buyer and $r c _ { 4 }$ and $r c _ { 5 } )$ tie strength using the daily interactions. Secondly, the expertise analysis module uses purchase histories to evaluate the expertise of $r c _ { 1 , } r c _ { 2 } , r c _ { 4 } ,$ and $r c _ { 5 } .$ The ratings are more trustable, if he/she has higher expertise in a speci<sup>fi</sup>c product category. Thirdly, the co-orientation analysis module derives the co-orientation of $r c _ { 1 , } \ r c _ { 2 } , \ r c _ { 4 } ,$ and $r c _ { 5 }$ according to their rating histories. Finally, the analyzed attractiveness, expertise, and coorientation of referral candidates would be fed into the trustworthiness analysis module to estimate the credibility value of $s _ { 1 } .$

![](/api/attachments/DN8JMTSZ/fulltext/images/34719434bc74c7535681d9d6d620f6a3e7a3ad504bf2ca8b3686348cafbe8412.jpg)  
Fig. 1. Illustration of social referral mechanism.

Fig. 2 brie<sup>fl</sup>y presents the concept and architecture of our proposed mechanism. When a buyer would like to purchase a product from an online marketplace, he/she would search the possible sellers. Then the buyer would sequentially feed target sellers into the social referring mechanism. The proposed seller referral mechanism will discover the possible referral candidates of the speci<sup>fi</sup>c buyer. The referral candidate is de<sup>fi</sup>ned as the one who has transaction experience and rating records of the target seller in the social network.

The proposed model comprises four main modules: attractiveness analysis module, expertise analysis module, co-orientation analysis, and trustworthiness analysis module. Previous studies indicate that the tie strength between two people and expertise of a person have impacts on social trust [18,31]. The purpose of the attractiveness analysis module is to identify the tie strength between the buyer and each referral candidate. We apply the technique of social network analysis to derive social ties. The purpose of the expertise analysis module is to estimate the expertise of referral candidates. Speci<sup>fi</sup>cally, RFM analysis is applied to derive the expertise of referral candidates. The purpose of co-orientation analysis module is to estimate the co-orientation between a buyer and referral candidates. Speci<sup>fi</sup>cally, the statistical Z-score and Pearson correlation coef<sup>fi</sup>cient are applied to derive the rating tendency and perception similarity between a buyer and referral candidates. Finally, the trust scores of referral candidates are aggregated by a linear combination method and the credibility value is estimated by a weighted voting method in the trustworthiness analysis module.

## 3.1. Attractiveness analysis module

The purpose of this module is to identify tie strength based on the interactions between the buyer and referral candidates. If a person <sup>fi</sup>nds others favorable to develop friendship or interact with them, this person might recognize the attractiveness level of his/ her personal characteristics [5,44]. The in<sup>fl</sup>uence of personal attractiveness on social networks could be extensively studied by life interactions [44].

The social interactions are used to construct a social network for identifying tie strength. Two social actors have a deeper acquaintanceship if there is a stronger tie between them [40]. That is, the opinions or ratings given by these two social actors might make them more trustable to each other than others. Therefore, the goal of attractiveness analysis module is to estimate the tie strength between the buyer and the referral candidates in order to represent the social acquaintanceship degree.

## 3.1.1. Interaction network construction

According to [11], social interaction tie strength is a combination of the amount of time, the emotional intensity, the intimacy (mutual con<sup>fi</sup>ding), and the reciprocal services that characterize the tie. Intuitively, people would interact more frequently with friends with a stronger tie strength and they would have a greater impact on us.

![](/api/attachments/DN8JMTSZ/fulltext/images/35b7d54489fbaeedfde6d26b5345e5f951f96cb29baeae9169b77f6340b4aedc.jpg)  
Fig. 2. Seller referral mechanism.

On social media, social interactions can be captured from the online posts and reply behaviors. For example, as shown in Fig. 3- (a), a buyer $b _ { \mathrm { i } }$ posted a message and a referral candidate $r c _ { \mathrm { j } }$ replied to $b _ { \mathrm { i } } .$ rc posted a message and another referral candidate $r c _ { \mathrm { k } }$ replied to $r c _ { \mathrm { j } } .$ There is a direct/explicit interaction connection between $b _ { \mathrm { i } }$ and $r c _ { \mathrm { j } }$ and between $r c _ { \mathrm { j } }$ and $r c _ { \mathbf { k } } .$ We could easily observe that there is indirect/implicit connection between b and $r c _ { \mathrm { k } }$ (the dotted line), because they indirectly connected through $r c _ { \mathrm { j } }$ (the friend-of-friend relationship). For constructing the interaction network, we collect social interaction data from social media. This could discover the stably maintained friendships. Then we could get an interaction network of referral candidates.

## 3.1.2. Tie strength estimation

After obtaining the interaction connections of buyer and referral candidates, it can be easily observed that explicit tie strength and implicit tie strength exist in the interaction network.

3.1.2.1. Explicit tie strength. In this study, the explicit tie strength, which is measured by the interaction frequency in a time period, is used to represent the attractiveness between the members of the social media. The average number of interactions per week is used as the indicator of the explicit tie strength between nodes. The following formulation was used to determine the attractiveness (at):

$$
a t (i, j) = \frac {| s i _ {i , j} |}{| w |},
$$

where $| s i _ { i , j } |$ denotes the total number of social interactions between referral candidates i and j and w denotes the number of data collection periods (weeks).

Then the obtained tie strength would be normalized by min– max normalization as follows:

$$
a t _ {n o r} (i, j) = \frac {a t (i , j) - \min _ {a t}}{\max _ {a t} - \min _ {a t}},
$$

where the max and min , respectively, denote the maximum and minimum attractiveness in the whole network.

![](/api/attachments/DN8JMTSZ/fulltext/images/bc2f2274e114ca6e8e5009f2e6e14376afe7dedc8d5f04ad76fa04fb60c3f457.jpg)  
(a) Example for network construction (b) Example for tie strength estimation  
Fig. 3. Illustration of an interaction network.

Please cite this article in press as: C.-Y. Lai, et al., A social referral appraising mechanism for the e-marketplace, Inf. Manage. (2016), http://dx. doi.org/10.1016/j.im.2016.07.001

3.1.2.2. Implicit tie strength. When a buyer tries to refer a seller through their social network, the referral mechanism would refer the target seller from the buyer’s indirect and indirect friends who have experiences on making transactions with the seller. In practice, the explicit tie strengths among the social nodes could be directly observed through the social interactions and the implicit tie strengths between two nodes could indirectly be evaluated from the explicit connections. The calculation of the attractiveness of implicit connection such as $b _ { \mathrm { i } }$ and $r c _ { \mathbf { k } }$ in the above example is de<sup>fi</sup>ned as follows:

$$
a t _ {n o r} (i, k) = a t _ {n o r} (i, j) \times a t _ {n o r} (j, k)
$$

Note that multiple connections between two nodes are likely to appear because people may connect to indirect friends via different paths. If implicit tie strength is evaluated by multiple explicit connection paths, we use the maximum value as the implicit tie strength [21]. For example, in Fig. 3-(b), there are two explicit connection paths between $b _ { \mathrm { i } }$ and $r c _ { \mathrm { k } } .$ The implicit tie strength evaluated by $b _ { i } \to r c _ { m } \to r c _ { n } \to r c _ { k }$ (0.504) is greater than the strength evaluated by $b _ { i } \to r c _ { j } \to r c _ { k }$ (0.42). The implicit tie strength between $b _ { \mathrm { i } }$ and $r c _ { \mathrm { k } }$ is evaluated as 0.504.

## 3.2. Expertise analysis module

The purpose of this module is to estimate the expertise of referral candidates. The purpose of the RFM model is applied to provide a simple framework for quantifying the customer behavior. A referral candidate with a higher RFM value in a speci<sup>fi</sup>c category can infer that he/she has spent a lot of effort (i.e., time and money) on the related products. Also, it implies that he/she might have more transaction experiences with sellers and higher expertise. That is, his/her ratings are more trustable. This study adopts the RFM value of the referral candidate to represent his/her expertise in a product category. Here, we follow the treatment of Hughes [26] to perform RFM analysis.

## 3.2.1. Purchasing behavior analysis

From the perspective of R (recency), it represents that the buyer has currently made transactions in the product category, which means that he/she has the experience for con<sup>fi</sup>rming the current quality of the seller. In this research, the value of R is de<sup>fi</sup>ned as the last date of purchase in the product category. From the perspective of F (frequency), if a buyer has repeatedly made transactions in the product category, it would mean he/she is an experienced buyer who could evaluate the sustained quality of the seller. The value of F is de<sup>fi</sup>ned as the average products purchased in a certain time period. From the perspective of M (monetary), it represents the risk the buyer is willing to bear with for making transaction in the product category. For example, a buyer purchased a product at a price of 1000 dollars and gave the seller a rating, and another buyer purchased a product at a price of 10 dollars and gave the seller a rating. The effort in surveying reliable sellers and the risks associated with these two given ratings are greatly different. In most purchase behaviors, buyers would carefully scrutinize and select sellers to purchase products at a high price, but they would not carefully select sellers before purchasing products at a low price [55]. In this research, we modify the common de<sup>fi</sup>nition of M (the amount of money spent on the total purchases) as the average amount money spent on one product.

The referral candidate’s R, F, and M variable values in the category of buyer’s target products are de<sup>fi</sup>ned as follows:

Recency the last date of pruchase in the category

$$
F r e q u e n c y = \frac {\text { total   of   purchased   products   in   the   category }}{\text { total   of   months }}
$$

$$
\text { Monetary } = \frac {\text { total   of   spent   money   in   the   category }}{\text { total   of   bought   products }}
$$

## 3.2.2. Expertise level estimation

The purpose of RFM scoring is to translate the customer behaviors into numbers that can be further analyzed. Generally, the most common RFM scoring method is the customer quintile method [25,26]. Sorting the values of R, F, and M variables in descending order, we assign them with <sup>fi</sup>ve scoring intervals from 5 to 1. The top 20% is assigned the value of 5. The value of 4 is given to the next 20% and so on. The customer quintile method has the advantage of convenience in segmenting equal numbers of customers into different groups. However, the customer quintile method does encounter some scoring challenges in the area of the F value [50]. In most marketplaces, a high percentage of the customers only order once. If more than 20% of the customers do only one-time shopping, then the lowest frequency group would not hold all of the customers having only one-time shopping behavior; some of them will be segmented into the two score groups.

The mean scoring method, introduced by Miglautsch [37], overcomes the problem of frequency scoring mentioned above. While scoring the value of F, the customers doing one-time shopping are <sup>fi</sup>rst given a score of 1. Then the scoring system averages the remaining customer records to determine the mean. If a customer’s shopping frequency falls below the mean, he/she receives a score of 2. This process is repeated for giving a score of 3, 4, and 5 to the remaining customers.

In this study, the quintile method is used for scoring R and M and the mean scoring method is used for scoring F. Then the scores of R, F, and M are summed up. The higher score indicates a higher expertise level. The expertise level (el) of the referral candidate (rc ) in the category (c) is de<sup>fi</sup>ned as follows:

$$
e l ^ {c} \left(r c _ {i}\right) = w _ {r} \times \operatorname{Score} \left(R _ {i} ^ {c}\right) + w _ {f} \times \operatorname{Score} \left(F _ {i} ^ {c}\right) + w _ {m} \times \operatorname{Score} \left(M _ {i} ^ {c}\right),
$$

where $w _ { \mathrm { r } } , w _ { \mathrm { f } }$ , and $w _ { \mathrm { m } } ,$ , respectively, indicate the scoring weightings of R, F, and M. The weighting strategies are discussed in Section 5.1.

Then the obtained expertise level would be normalized by min– max normalization as follows:

$$
e l \frac {c}{n o r} (r c _ {i}) = \frac {e l ^ {c} (r c _ {i}) - \min _ {e l}}{\max _ {e l} - \min _ {e l}},
$$

where $\operatorname* { m a x } _ { e l }$ and $\mathrm { m i n } _ { e l } ,$ respectively, denote the maximum and minimum expertise level among all of the referral candidates.

## 3.3. Co-orientation analysis module

The purpose of this module is to estimate the co-orientation between the referral candidate and the buyer. It is common that biases exist, when humans create ranking or assess the performance of others [35]. These biases would give the referred sellers unfair advantage or disadvantage. In this section, the co-orientation of referral candidates is analyzed by their rating tendency and grading standards (perceptions of criteria). If there is no special rating tendency (e.g., used to give higher or lower ratings) and grading standards are more <sup>fi</sup>t in our mind, the reliability of the ratings given by the referral candidate should be higher than the others.

## 3.3.1. Perception similarity estimation

Co-orientation, one of the factors of the source credibility theory, is de<sup>fi</sup>ned in Table 1. In this research, co-orientation is further depicted as having similar perceptions of criteria to evaluate a target, such as seller, product, and service.

A seller rating (positive, neutral, or negative) re<sup>fl</sup>ects the aggregation of evaluations of decision criteria, such as the quality of item, seller’s service, and shipping time of the transaction. Although everyone uses the same criteria to evaluate sellers, the perception varies from person to person for the decision criteria. For example, the shipping time of a seller is 3 days. But a buyer gives a negative rating to the seller because his/her perception of the shipping time is 1 day and another buyer gives a positive rating to this seller because his/her perception of the shipping time is 7 days. However, if the rating is given by the one who has similar perceptions of criteria as us, it is a more referable rating.

The perception similarity (ps) could be estimated by comparing rating records of buyer (b) and referral candidate (rc) for the corated sellers (s). That is, only the rating records that are rated on the same seller by the buyer and the referral candidate could be used to estimate the perception similarity (ps). Pearson correlation coef<sup>fi</sup>cient [3], one of the most widely used coef<sup>fi</sup>cients in CF methods, is adapted as follows:

$$
p s (b, r c) = \sum_ {i = 1} ^ {n} (r _ {b} ^ {s _ {i}} - \overline {{r _ {b} ^ {s}}}) (r _ {r c} ^ {s _ {i}} - \frac {\overline {{r _ {r c} ^ {s}}})}{\sqrt {\sum_ {i = 1} ^ {n} (r _ {b} ^ {s _ {i}} - \overline {{r _ {b} ^ {s}}}) ^ {2} \sqrt {\sum_ {i = 1} ^ {n} (r _ {r c} ^ {s _ {i}} - \overline {{r _ {r c} ^ {s}}}) ^ {2}}}},
$$

where $r _ { b } ^ { s _ { i } }$ and $r _ { r c } ^ { s _ { i } } ,$ , respectively, indicate the rating of b and rc for the co-rated seller $s _ { \mathrm { i } }$ and $\overline { { r _ { b } ^ { s } } }$ and $\overline { { r _ { r c } ^ { s } } }$ , respectively, indicate the average rating of b and rc for s. Note that, $s _ { i } \in s .$

## 3.3.2. Rating tendency estimation

Leniency error indicates that a rater’s tendency is to rate all alternatives at the high end of the scale or at the low end of the scale [35], which means that the rater overemphasizes either positive or negative behaviors. Under the concept of rating tendency, if a rater has the tendency of giving higher or lower ratings, it represents that the reliability of these ratings from the rater could be decreased or increased.

Z-score measure is applied to measure the rating tendency of a reviewer. Different raters have different rating tendencies. Some people tend to give higher scores, and some people tend to give relatively low scores. By using the Z-score, a more accurate relative preference re<sup>fl</sup>ecting the tendency of a user’s ratings can be acquired [22]. Here, we apply Z-score measures to calculate the rating tendency of a referral candidate. The rating tendency of a referral candidate (rt(rc)) is measured as

$$
r t (r c) = r _ {r c} ^ {s i} - \frac {\overline {{r _ {u} ^ {s i}}}}{\sigma_ {r _ {u} ^ {s i}}},
$$

where the $r _ { r c } ^ { s _ { i } }$ indicates the past rating of the referral candidate for the co-rated seller $s _ { i } , \overline { { r _ { u } ^ { s _ { i } } } }$ is the average rating of the general user for $s _ { i } ,$ and $\sigma _ { r _ { u } ^ { s _ { i } } }$ is the standard deviation of the rating of the general users for s .

After we know the rating tendency (i.e., the bias) of someone, if the rating score is higher or smaller than the general users, then we need to adjust the rating score to be consistent with the rating standard of general users. When the rating score is higher than the rating standard of general users, then the rating score needs to increase. In contrast, if the rating score is higher than the rating of general users, then the rating score needs to decrease. Bias adjustment mechanism in [32] can be used to adjust the rating score. After analyzing the perception similarity and rating tendency, the following formulation is used to calculate the coorientation of the referral candidate for the buyer (co(b,rc)).

$$
c o (b, r c) = \left\{ \begin{array}{l} p s (b, r c) \times (1 - r t (r c), i f r t (r c)) > 0 \\ p s (b, r c) \times (1 + | r t (r c) |, i f r t (r c)) <   0 \end{array} \right..
$$

Then the obtained co-orientation would be normalized by min– max normalization as

$$
c o (b, r c) = \frac {c o (b , r c _ {i}) - \min _ {c o}}{\max _ {c o} - \min _ {c o}},
$$

where $\boldsymbol { \mathrm { I m } } \partial \mathbf { X } _ { c o }$ and mi $^ { 1 } c o \cdot$ respectively, denote the maximum and minimum co-orientation among all of the referral candidates.

## 3.4. Trustworthiness analysis module

The purpose of this module is to estimate the credibility value of the target seller. Most of the online evaluation systems on the EC platform calculate the trust score of a seller by simply accumulating the rating records. This means each rating record has an equal impact on the buyer-selecting seller. However, the ratings given by different voters should have different capacities and impacts on the evaluation of searching of sellers by buyers.

## 3.4.1. Trustworthiness estimation

“Reputation” can be de<sup>fi</sup>ned as a collective measure of “trust” based on the ratings assigned by the members in a community [27]. Tsai and Ghoshail [49] indicate social interaction may stimulate trust and perceive trustworthiness. Zingler and Golbeck [56] claim that trust should be derived from user similarity and trust is the basis of social interaction. Strong ties are the people you really trust (Gilbert and Karahalios 2009). Cho et al. [10] proposed a collaborative reputation system based on expertise and coorientation factors to compute trust score. Xiong and Liu [52,53] compare the trustworthiness of peers based on feedback records, similarity, and relation context. The aim of this paper is to appropriately quantify each credibility factor for referral candidates to adjust an online reputation system and make it more reliable for users. Inspired by the above studies, it would be reasonable to measure the trust value by using attractiveness, coorientation, and expertise. The linear combination method is used for estimating the trust score of referral candidates as attractiveness, co-orientation, and expertise level are positively correlated with trustworthiness. The trustworthiness of a referral candidate is de<sup>fi</sup>ned as follows:

$$
t w (r c _ {i}) = a t _ {n o r} (b, r c _ {i}) + e l _ {n o t} ^ {c} (r c _ {i}) + c o _ {n o t} (b, r c)
$$

The purpose of the trustworthiness is to adjust the impact of rating given by the other user on the seller selection. The obtained trustworthiness would be normalized to the interval of [0,2] by min–max normalization as follows:

$$
t w _ {n o r} (r c _ {i}) = \frac {t w (r c _ {i}) - \min _ {t w}}{\max _ {t w} - \min _ {t w}} \times 2,
$$

where $\mathbf { \ m a x } _ { t w }$ and min $. t w ,$ respectively, denote the maximum and minimum trustworthiness among all of the referral candidates.

If the voter’s trustworthiness is within the interval of (0,1), the impact of his/her rating on the seller selection should be decreased. If the trustworthiness of the voter is within the interval of (1,2), the impact should be increased. Note that if the trustworthiness is equal to 0 and 1, it indicates, respectively, that the rating cannot be trusted and the rating has no impact on seller selection. The larger the trustworthiness value of a referral candidate, the higher the reputation of this referral candidate. If a referral candidate has high trustworthiness, then his/her rating for a seller will cause a higher scaling effect on the seller’s credibility value. In contrast, if a referral candidate has low trustworthiness, then his/her rating for the seller will cause a less scaling effect on a seller’s credibility. If the positive rating is given by a user with high trustworthiness, the impact on the seller selection for the target buyer would be greater than 1. On the contrary, if it is given by a user with low trustworthiness, the impact would be smaller than 1. Also, the impact of negative ratings should be adjusted by trustworthiness to make it greater or smaller than 1. Furthermore, the impact of a <sup>-</sup>rating should be adjusted to 0, if it is given by a distrusted voter. Note that if a referral candidate’s trustworthiness is 1, his/her trustworthiness is neutral and has no scaling effect on the seller selection.

## 3.4.2. Credibility value estimation

Currently, most of the reputation systems provide e-marketplace reputation for sellers by simply accumulating the buyers’ ratings. Although the seller reputations could be adjusted according to the obtained social tie strength and expertise level of raters, the seller reputations should not only be adjusted by the information of raters but also dynamically adjusted by continuous passage of time. Randy Farmer and Bryce Glass [15] state that “ratings become stale over time as their target reputable entities change or become unfashionable businesses change ownership, <sup>-</sup>technology becomes obsolete, cultural mores shift.” For example, a rating given 1 month ago should get a greater reference value than the rating given 6 months ago due to the sellers changing their operation strategies, business partner, etc.

A general approach for compensating for time in reputation values is to apply a decay function: subtract the value from the older reputations as time goes on, at a rate that is appropriate to the context. For example, digital camera ratings for resolution probably lose half their value every year, whereas restaurant reviews only lose 10% of their value in the same interval. Thus, instead of using the exponential decay function, we utilize an alternative power time decay function for adjusting the reputation estimation. We utilize the basic power function to obtain the time decay rate (td( )) for a speci<sup>fi</sup>c time and formulate as follows:

$$
t d (d _ {p}) = \alpha^ {- \left(\left(\frac {d _ {c} - d _ {p}}{3 0}\right), \right.}
$$

where $d _ { c }$ denotes the current date, $d _ { p }$ denotes the past date on which the rating is given by the referral candidate, $\frac { d _ { c } - d _ { p } } { 3 0 }$ is used to estimate the difference of months between $d _ { c }$ and $d _ { p } ,$ and the variable a is a constant parameter of the time decay function. We are able to obtain different decay effects by adjusting the value of a. The value of a can be determined by a sequential test and practical experience. Fig. 4 shows the decay effects of different values of a. The smaller the value, the slower is the decay of reputation; on the contrary, the greater the value, the quicker is the decay of reputation. The value of a could be adjusted according to the real situation of e-marketplaces.

Finally, the weighted voting method is performed for estimating the credibility value of the target seller. The credibility value (cv ( )) of a target seller $\left( { { s } _ { t } } \right)$ is de<sup>fi</sup>ned as follows:

$$
c v (s _ {t}) = \sum_ {i = 1} ^ {n} \sum_ {p = 1} ^ {n} t w (r c _ {i}) \times t d (t _ {p}) \times r _ {r c _ {i}} ^ {s _ {t}, p}
$$

where the $r _ { r c _ { i } } ^ { s _ { t } , p }$ denotes the rating of $s _ { t } ,$ which is given by $r c _ { i }$ in time period p. Note that $r _ { r c _ { i } } ^ { s _ { t } } = 1 \mathrm { i f } r c _ { i }$ gives a positive rating $r _ { r c _ { i } } ^ { s _ { t } } = - 1 \mathrm { i f } r c _ { i }$ gives a negative rating, and $r _ { r c _ { i } } ^ { s _ { t } } = 0$ if $r c _ { i }$ gives a neutral rating.

## 4. Experiments

In this section, we conduct experiments to evaluate the proposed SRM. To implement the mechanism, user information on the social network (e.g., social interactions) and online marketplace (e.g., purchase behaviors and seller ratings) is needed. However, most current social networking platforms, such as Facebook and Twitter, and EC platforms, such as Amazon and Yahoo! Shopping, are independently operated. The experimental data have to be independently collected. We constructed the experiment using Facebook, which is the most famous social networking site around the world for constructing social factors, and Yahoo! Auction, which is the largest online auction site in Taiwan for constructing marketplace factors.

![](/api/attachments/DN8JMTSZ/fulltext/images/4ee600a3a17c29d170cde98c323ffa05de3db979d7eba4861190e8bdbe3fddca.jpg)  
Fig. 4. Time decay effects.

Although a social network is a good place to collect consumer data, these data pools cannot just be tapped into. Social network users are more wary of sharing their own pro<sup>fi</sup>les, and due to the privacy constraint, we can only collect the social interactions (wall postings in Facebook) and EC behaviors (purchase histories on Yahoo! Auction) from those users who are willing to authorize us to do that. Hence, it is dif<sup>fi</sup>cult to recruit a large pool of participants in the experiments.

Participants were invited to be involved through snowball sampling. Snowball sampling has been proved to be a feasible method to study the issue of social networks [18,41]. Hence, it was used to construct the network structure of the experiments. Snowball sampling starts from a random sample of individuals drawn from a given population. Each one in the sample is asked to name N different persons. Those who are named and are not in the random sample form the <sup>fi</sup>rst-stage network. Each one in the <sup>fi</sup>rststage network is then asked to do the same thing for S times by repeating in order to complete the sampling process. In our experiment, S was set to 3 and N was set to 10. Initially, we invited 10 Facebook users, who were willing to authorize us to collect their social information. With their help, we further invited their friends and friends of friends. Handcock and Gile [23] stated that sampled networks are not “biased” but can be representative if analyzed correctly. An exponential random graph model (EGRM) has been demonstrated to be capable of capturing the key structure of a social network such as the degree of clustering, the degree of distribution, and feature of network connectivity [47]. To prevent sample selection bias, we adopt the conditional estimation of EGRM from the snowball sampling design approach proposed by Phillippa et al. [40] as our sampling approach. In total, 313 participants were generated through the snowball sampling process. After removing the people who were not interested in our experiment, we were left with a total of 187 unique participants who formed the initial experimental social networks. There were a total of 730 online transaction records in six categories (c1: cell phone and communications, c2: beauty products and makeup, c3: sports, c4: men’s clothes and accessories, c5: women’s bags and shoes, c6: women’s clothes and accessories). These transactions were made with 145 sellers and each seller received an average rating of 5.03. There were a total of 14,721 social interactions between participants. We think the structure of the sampled network should appropriately re<sup>fl</sup>ect the main characteristics of the real network structure. The characteristics of the extracted network are summarized in Table 2.

First, to construct the interaction network for analyzing tie strength, we collected and analyzed the past 6 months’ wall postings, which is one of the most popular methods of user interactions [51], from Facebook. Second, to perform the RFM analysis for obtaining the expertise level, we requested participants to provide purchase history in the recent 6 months, including seller, purchase date, product name, product category, and seller’s rating. After acquiring this social and historical information about participants, the experiment sequentially tested each transaction record, assuming that a buyer would like to make transaction with a speci<sup>fi</sup>c seller. In addition, the buyer used the proposed mechanism to refer to the credibility value of the seller from his/her social network.

## 5. Results and evaluations

## 5.1. Comparisons based on private evaluations

The referral results are then compared with the real ratings of buyers for sellers. For example, if the seller referral result is positive and the real rating from the transaction record is positive, it means our mechanism can correctly refer to the evaluation of the online seller for the speci<sup>fi</sup>c buyer. The accuracy rate of each category is calculated as the indicator. The optimal cutoff points are determined based on the statistics distribution on the rating prediction. Rating prediction is generated based on the historical data available at a moment in time.

After acquiring social and historical information about the participants, the experiment sequentially tested each transaction record, assuming that a buyer would like to make a transaction with a speci<sup>fi</sup>c seller. In addition, the buyer used the proposed mechanism to refer to the credibility value of the seller from his/ her social network. Each actual transaction was considered as a data point that we wanted to predict. The data point tells us what the buyer bought, from which seller, and his/her three-level ratings (positive, neutral, and negative) on this seller. Then we compared the consistency of the buyer’s rating with the proposed rating on this seller to evaluate the accuracy performance of our proposed mechanism. In order to compare with the buyer’s three-level ratings, we transform the credibility values from numerical data to three-level ratings (positive, neutral, and negative) based only on the data (historical transactions) that were available at that moment in time. The credibility values are then sorted in decreasing order. Then the threshold values of 0.88 (percentiles of 33%) and 0.62 (percentiles of 66%) are used for transforming. <sup>-</sup>The evaluation of $s _ { t }$ (evaluation(s )) is set as

Data descriptions of the experimental network.

<table><tr><td>Attributes</td><td>Social Networks</td></tr><tr><td>Number of participants</td><td>187</td></tr><tr><td>Age</td><td>18 ~ 46</td></tr><tr><td>Gender</td><td>Male: 47%Female: 53%</td></tr><tr><td>Average degree centrality</td><td>17.907</td></tr><tr><td>Clustering coefficient</td><td>0.247</td></tr><tr><td>Average distance</td><td>1.749</td></tr><tr><td>Total number of collected purchase histories</td><td>730</td></tr><tr><td>Total number of sellers for social referrals</td><td>187</td></tr><tr><td>Average rating per seller</td><td>5.03</td></tr><tr><td>Average number of purchase behaviors per participant (6 months)</td><td>3.90</td></tr><tr><td>Average number of interactions per participant (6 months)</td><td>78.72</td></tr></table>

$$
e v a l u a t i o n (s _ {t}) = \left\{ \begin{array}{l} 1, \text {   if   } r v (s _ {t}) \geq 0. 8 8 \\ 0, \text {   if   } 0. 8 8 <   r v (s _ {t}) <   - 0. 6 2 \\ - 1, \text {   if   } r v (s _ {t}) \leq - 0. 6 2 \end{array} \right.
$$

The credibility result is set to positive if evaluation s 1, to negative if evaluation $( s _ { t } ) = - 1$ , and to neutral if evaluation s 0. Finally, we utilize the following formulation to calculate the social referral accuracy rate according to the user ratings of the target sellers:

$$
\text {Accuracy} = \frac {\text {total of seller referral results matching buyers' ratings}}{\times 100 \% \text {total of seller referral results}}
$$

## 5.2. Comparisons of the time delay rate and scoring weighting selections

In the proposed mechanism, the RFM scoring weightings and time delay functions $( t d ( \cdot ) )$ are important factors for estimating the <sup>ðÞ</sup>credibility values of sellers. According to Hughes [26], each measure of R, F, and M has the same weight $\left( ( w _ { r } , w _ { f } , w _ { m } ) = ( 1 , 1 , 1 ) \right)$ ) when calculating a composite score. Libey [33] indicates that a different weight may be given to each measurement of RFM. This research points out that the scoring weighting set $( w _ { r } , w _ { f } , w _ { m } ) = ( 3 , 2 , 1 )$ could show a better performance for computing a composite score. Furthermore, Miglautsch [37] states that $( w _ { r } , w _ { f } , w _ { m } ) = ( 9 . 9 , 6 . 6 , 3 . 3 )$ is another scoring weighting setting for computing a composite score. The value of a in td directly affects the delay effects. A suitable avalue can be <sup>ðÞ</sup>determined by practical experience or sequential testing.

In order to determine the most appropriate values of factors with a better performance, we compare the performances of the experiments according to different combinations of RFM scoring weightings and values of a. Table 3 shows the mean absolute error (MAE) results under six different word expansion levels and various trust delay rates. Here, we compare performance with the different settings of $( w _ { r } , w _ { f } , w _ { m } ) =$ 1; 1; 1 ; 3; 2; 1 ; 9:9; 6:6; 3:3 and <sup>fð Þ ð Þ ð Þg</sup>a 1:1; 1:2; 1:3; 1:8; 2:5 . The effectiveness performance is <sup>¼ f g</sup>evaluated based on the MAE:

$$
M A E = \frac {1}{n} \sum_ {t = 1} ^ {n} | e v a l u a t i o n (s _ {t}) - r _ {b _ {i}} ^ {s _ {t}} |
$$

where $r _ { b _ { i } } ^ { s _ { t } }$ indicates the real rating by buyer $b _ { i }$ of seller $s _ { t } .$

As a smaller MAE represents a more accurate result, we can observe that a 1:1 and $( w _ { r } , w _ { f } , w _ { m } ) = ( 3 , 2 , 1 )$ has the best MAE

Table 3  
Comparisons of appropriate factors.

<table><tr><td></td><td> $\alpha = 1$ </td><td> $\alpha = 1.1$ </td><td> $\alpha = 1.3$ </td><td> $\alpha = 1.5$ </td><td> $\alpha = 1.7$ </td></tr><tr><td> $(w_{r},w_{f},w_{m})=(1,1,1)$ </td><td>0.511</td><td>0.453</td><td>0.401</td><td>0.394</td><td>0.504</td></tr><tr><td> $(w_{r},w_{f},w_{m})=(3,2,1)$ </td><td>0.453</td><td> $\underline{0.308}$ </td><td>0.646</td><td>0.730</td><td>0.796</td></tr><tr><td> $(w_{r},w_{f},w_{m})=(9.9,6.6,3.3)$ </td><td>0.434</td><td>0.438</td><td>0.668</td><td>0.745</td><td>0.799</td></tr><tr><td></td><td> $\alpha = 1.9$ </td><td> $\alpha = 2.1$ </td><td> $\alpha = 2.3$ </td><td> $\alpha = 2.5$ </td><td> $\alpha = 2.7$ </td></tr><tr><td> $(w_{r},w_{f},w_{m})=(1,1,1)$ </td><td>0.595</td><td>0.704</td><td>0.755</td><td>0.799</td><td>0.814</td></tr><tr><td> $(w_{r},w_{f},w_{m})=(3,2,1)$ </td><td>0.803</td><td>0.839</td><td>0.854</td><td>0.876</td><td>0.898</td></tr><tr><td> $(w_{r},w_{f},w_{m})=(9.9,6.6,3.3)$ </td><td>0.810</td><td>0.836</td><td>0.861</td><td>0.876</td><td>0.898</td></tr></table>

Please cite this article in press as: C.-Y. Lai, et al., A social referral appraising mechanism for the e-marketplace, Inf. Manage. (2016), http://dx. doi.org/10.1016/j.im.2016.07.001

performance in the experiments. Thus, in the following experiments, $\alpha = 1 . 1$ and $( w _ { r } , w _ { f } , w _ { m } ) = ( 3 , 2 , 1 )$ are used. From the results, we can also observe that when a > 1:1, the MAE values of each RFM scoring weighting becomes larger. This <sup>fi</sup>nding implies that the time impact of the seller’s reputation for buyers might not delay very quickly (when $\alpha = 1 . 1$ , the time delay rate approx-<sup>¼</sup>imates to 0.909 for each 1-month period).

## 5.3. Comparisons of referral effectiveness

To evaluate whether the proposed SRM can help customers select superior sellers and prevent them from making transactions with fraudulent sellers in the online marketplace, we compare our mechanism with three benchmark methods. The four approaches used in the experiments are described as follows:

1. SRM (our approach): The SRM considers factors from the perspectives of social, expertise, co-orientation, and trustworthiness to refer to a seller’s credibility value.

2. EO: Expertise and co-orientation are two important factors for evaluating source credibility [24,45]. In this model, the EO model is treated as a basic referral method that exploits only the estimation of expertise analysis and co-orientation.

3. CF: The basic concept of the CF model is that if the ratings are given by users that share similar tastes with us, these ratings would be more trustable [27]. In this model, only the interaction-based tie strength is taken into consideration to refer to the seller’s credibility value.

4. Public: The current public seller’s reputation is extracted from the online marketplace.

## 5.3.1. Comparisons based on public evaluations

Here, the results are compared with the public evaluations of sellers given by the of<sup>fi</sup>cial evaluation system using the MAE method. In the experiment, the proposed SRM correctly referred to 578 of 730 seller evaluations. That is, as shown in Figs. 5 and 6, the proposed mechanism showed a 79.24% accuracy rate and 0.303 MAE in the overall categories.

Finally, the result of the overall performance of the different benchmark methods is further evaluated by using a two-paired sample t-test, as shown in Table 4. At the 95% signi<sup>fi</sup>cance level, all the test results show that the proposed SRM signi<sup>fi</sup>cantly outperforms the other baseline seller referral approaches.

Detailed information is shown in Fig. 7. In this <sup>fi</sup>gure, we can observe that the accuracy rate of c6 (women’s clothes and accessories) is 85.18% and the accuracy rate of c1 (cell phone and communications) is 71.55%, which are the highest and lowest rates, respectively. According to our survey, around 38% of the collected purchase history records belong to c6. This might be attributed to fashion trends: most customers who bought similar products are likely to recommend sellers to their friends. As a result, the sellers in this category could be referred to by many more buyers than from other categories and accuracy is statistically improved. In c1, most purchase records are one-time shopping trips for peripheral products for mobile devices. These kinds of products highly depend on personal preferences, so they are more dif<sup>fi</sup>cult to make seller referrals. The MAE comparison results are shown in Fig. 8. The results verify that the seller evaluation based on the buyer’s social network is closer to the buyer’s real evaluation than public evaluations.

![](/api/attachments/DN8JMTSZ/fulltext/images/c32e0867b5f76f1db22549335d17bd4f709de12d0ab4d76d60f8d0a1b165331a.jpg)  
Fig. 5. Accuracy rates in overall experiments.

![](/api/attachments/DN8JMTSZ/fulltext/images/f715da8df9e547e160e2b4ff51a38ff738a704a9d6003511d646c8bb4d119832.jpg)  
Fig. 6. MAE rates in overall experiments

## 5.4. Additional comparisons in seller recommendation

In this section, we build additional experiments in the seller recommendation scenario. The proposed SRM can be used not only to help the buyer refer to the reputation of a target seller via their social networks but also to recommend superior sellers to the buyer. We assume that the participating buyer does not know which seller’s reputation he/she would like to refer to and make a transaction with. Then the system recommends some sellers in a speci<sup>fi</sup>c category to the buyer. Finally, the results are compared with the real purchase histories of buyers.

The experiments recommend three sellers to a buyer according to the values of cv s rather than the transformed three-level <sup>ð Þ</sup>ratings. Sellers are ranked by the values of $c v ( s _ { t } )$ and the system <sup>ð Þ</sup>recommends sellers ranked in the <sup>fi</sup>rst three ranking positions. Then the results are compared with the real seller selections that buyers decide to make transactions with and the ratings of sellers by buyers. For example, if the system recommends $s _ { a } , s _ { b } ,$ and $s _ { c }$ to the buyer and from the transaction records the buyer makes a transaction with $s _ { b }$ and gives him/her a positive rating, it means our mechanism can correctly recommend online sellers for a speci<sup>fi</sup>c buyer. Detailed comparison rules are listed in Table 5.

According to [39], the precision, recall, and $F _ { 1 }$ measure rates of the seller recommender are de<sup>fi</sup>ned as follows:

$$
p r e c i s i o n = \frac {R P}{R P + R N}
$$

$$
r e c a l l = \frac {R P}{R P + N R P}
$$

$$
F _ {1} = \frac {2 \times \text { precision } \times \text { recall }}{\text { precision } + \text { recall }}
$$

Table 4  
Statistical veri<sup>fi</sup>cation of the seller’s referral results with different methods.

<table><tr><td>Paired Group</td><td></td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T value</td><td>Sig. (two-tailed)</td></tr><tr><td rowspan="3">SRM V.S.</td><td>EO</td><td>-0.02312</td><td>0.98656</td><td>0.05960</td><td>-0.388</td><td>0.031</td></tr><tr><td>CF</td><td>-0.01015</td><td>1.05133</td><td>0.06351</td><td>-0.160</td><td>0.013</td></tr><tr><td>Public</td><td>-0.73120</td><td>1.04026</td><td>0.06284</td><td>-11.635</td><td>0.000</td></tr></table>

![](/api/attachments/DN8JMTSZ/fulltext/images/ad041c8f374b9537652507b55846120b4abafe45ee4ab0d4ebf07f3877987e3d.jpg)  
Fig. 7. Accuracy rates in different categories.

![](/api/attachments/DN8JMTSZ/fulltext/images/030c623d8a72115b1d021a457fee74a73e6436f5370aa8d5a316fb829d795289.jpg)  
Fig. 8. MAE rates in different categories

The results in Fig. 9 show that the proposed SRM is more effective than other benchmark methods. The SRM received approximately 70% precision, 58% recall, and 63% for the F1 measure rate in the seller recommender scenario. This is because the outputted reputation values by the SRM are adjusted according to the attractiveness, expertise, and co-orientation factors that are essential credibility factors of raters. If it recommends a seller using the current public seller’s reputation, it receives the lowest effectiveness because most sellers’ reputations are similar and this leads the mechanism to fail in recommending the correct sellers to buyers. Detailed information on each product category of the SRM is shown in Fig. 10.

Further, the results of the overall seller recommender performance of the benchmark methods are further evaluated by using a two-paired sample t-test, as shown in Table 6. At the 95% signi<sup>fi</sup>cance level, all the test results show that the proposed SRM signi<sup>fi</sup>cantly outperforms the benchmark methods in this scenario.

## 6. Discussion and conclusion

In this research, a framework of designing an SRM composed of an attractiveness analysis, expertise analysis, co-orientation analysis, and credibility value analysis is proposed. In the social attractiveness analysis, the network is formed according to the message post and response interactions on social networking sites. We obtain the strength of explicit and implicit social ties to identify the attractiveness between the buyer and referral candidates. RFM analysis is utilized to estimate the expertise level of referral candidates from their purchase history records. In the coorientation analysis, the perception similarity evaluated by the Pearson correlation and rating tendency measured by the Z-score are combined to estimate the rating co-orientation of referral candidates. To successfully refer to the most trustable seller’s evaluation from a buyer’s social network, we aggregate the attractiveness, expertise, and co-orientation of referral candidates to weigh the evaluation of the seller that they gave. The experimental results show that the proposed SRM outperforms the other baseline benchmark methods.

## 6.1. Research contributions

The contributions and managerial implications of this paper are summarized as follows. From the perspective of an EC platform provider, the proposed SRM could help buyers prevent trust fraud in the online marketplace and thus improve the transaction environment. From the perspective of buyers, the proposed SRM veri<sup>fi</sup>es the credibility of sellers according to trustworthy ratings, which could stop buyers from making transactions with fraudulent sellers in the online marketplace. From the perspective of a seller, the system can reduce the risk of business transaction uncertainty, attract more buyers to be involved in the market platform, and signi<sup>fi</sup>cantly increase the revenue of a seller. From the perspective of online marketplaces, a more reliable reputation system is proposed, which is helpful to deal with online trust fraud issues.

Table 5 Evaluation rule table.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">User evaluation</td></tr><tr><td>Positive rating</td><td>Negative rating</td></tr><tr><td rowspan="2">System recommendation</td><td>Recommended</td><td>RP (Recommended with positive rating)</td><td>RN (Recommended with negative rating)</td></tr><tr><td>Not recommended</td><td>NRP (Not recommended with positive rating)</td><td>NRN (Not recommended with negative rating)</td></tr></table>

Please cite this article in press as: C.-Y. Lai, et al., A social referral appraising mechanism for the e-marketplace, Inf. Manage. (2016), http://dx. doi.org/10.1016/j.im.2016.07.001

![](/api/attachments/DN8JMTSZ/fulltext/images/303aeb5592fe50d49a69d5c2a6dab033d1d2d299f673e97fae4172ce02a815d3.jpg)  
Fig. 9. Additional comparison results in the seller recommender scenario.

![](/api/attachments/DN8JMTSZ/fulltext/images/ebda7acd5cfb76fd7d2b7afa978eb532f3975298ca4df19503584e09bbdabed2.jpg)  
Fig. 10. Detailed comparison results in the seller recommender scenario.

Table 6  
Statistical veri<sup>fi</sup>cation of the seller’s referral results with the different methods.

<table><tr><td>Paired Group</td><td></td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T value</td><td>Sig. (two-tailed)</td></tr><tr><td rowspan="3">SRM V.S.</td><td>EO</td><td>0.02054</td><td>0.40736</td><td>0.01421</td><td>1.446</td><td>0.015</td></tr><tr><td>CF</td><td>-0.01158</td><td>0.40785</td><td>0.01423</td><td>-0.814</td><td>0.042</td></tr><tr><td>Public</td><td>0.51442</td><td>0.28372</td><td>0.00990</td><td>51.984</td><td>0.000</td></tr></table>

## 6.2. Limitations and future studies

There are several limitations and future works to this research. First, owing to privacy issues, it is dif<sup>fi</sup>cult to extract personal transaction data online. Therefore, we invited participants to join the experiments. If more users could be recruited and engaged, the accuracy of the proposed mechanism would improve and this could help buyers more effectively in avoiding making transactions with fraudulent sellers. Second, in the current paper, wall postings on Facebook are used as social interactions for analyzing tie strengths. Tie strength analysis would be more comprehensive if more interaction ways (e.g., messaging, applications, photo uploads, chat) could be considered. Third, the trustworthiness of referral candidates is only considered from the perspective of social networks. In the electronic marketplace, not only can buyers evaluate the reputations of sellers but also sellers can evaluate the reputations of buyers. It would also be interesting to evaluate the trustworthiness of referral candidates from the perspective of sellers in the marketplace. Fourth, the credibility values of sellers are currently estimated by only considering the evaluations given by close friends. However, good feedback might also be contributed by people who are strangers to the buyer. How to further consider these trusty evaluations and balance the impacts of public ratings and friend’s ratings is a desirable research direction.

## References

[1] M.S. Amin, B. Yan, S. Sriram, A. Bhasin, C. Posse, Social referral: leveraging network connections to deliver recommendations, Proceeding of 6th ACM Conference on Recommender Systems, New York, NY USA, 2012, pp. 273–276

[2] J. Bao, Y. Zheng, D. Wilki, M. Mokbel, Recommendations in location-based social networks: a survey, GeoInformatica 19–3 (2015) 525–565.

[3] J. Benesty, J. Chen, Y. Huang, I. Cohen, Pearson correlation coef<sup>fi</sup>cient, Noise Reduction in Speech Processing, 2, Springer Topics in Signal Processing, 2009 pp. 1–4.

[4] BlackHatWorld.com, eBay feedback change anyone? Available at: http://www. blackhatworld.com/blackhat-seo/ebay/483376-ebay-feedback-exchangeanyone.html (accessed 20.02.13).

[5] D. Boyd, N.B. Ellison, Social network sites: de<sup>fi</sup>nition, history, and scholarship, J. Computer-Mediated Commun. 13–1 (2008) 210–230.

[6] J. Brown, J. Morgan, Reputation in Online Markets: Some Negative Feedback, Department of Agricultural and Resource Economics, University of California, Berkeley CA, 2006.

[7] Buzz Referrals, BuzzReferrals.com, http://www.capterra.com/referralsoftware/spotlight/123871/Buzz%20%20Digital/BuzzReferrals%20com.

[8] Y.L. Chen, M.H. Kuo, S.Y. Wu, K. Tang, Discovering recency, frequency, and monetary (RFM) sequential patterns from customers’ purchasing data, Electron. Comm. Res. Appl. 8–5 (2009) 241–251.

[9] Y. Cho, J. Hwang, D. Lee, Identi<sup>fi</sup>cation of effective opinion leaders in the diffusion of technological innovation: a social network approach, Technol. Forecasting Social Change 79–1 (2012) 97–106.

[10] J.Y. Cho, K.S. Kwon, Y.T. Park, Q-rater. A collaborative reputation system based on source credibility theory, Expert Syst. Appl. 36 (2–2) (2009) 3751–3760.

[11] F. Dini, G. Spagnolo, Buying reputation on eBay: do recent changes help? Int. J. Electron, Bus. 7–6 (2009) 581–598

[12] W. Duan, B. Gu, A.B. Whinston, Do online reviews matter? An empirical investigation of panel data, Decis. Support Syst. 45–4 (2008) 1007–1016.

[13] eBay, Feedback Manipulation Policy, Available at: http://pages.ebay.com/help policies/feedback-manipulation.html (accessed 20.12.12).

[14] M. Eisend, Source credibility dimensions in marketing communication—A generalized solution, J. Empirical General. Market. 10 (2006) 1–33.

[15] R. Farmer, B. Glass, Building Web Reputation Systems, 1st ed., Yahoo! Press, USA, 2010.

[16] Gartner Says, Percent of Social Media Reviews to Be Fake, Paid for By Companies, Available at: http://www.gartner.com/newsroom/id/2161315, (accessed 20.12.12).

[17] E. Gilbert, K. Karahalios, Predicting tie strength with social media, Proceeding of SIGCHI Conference on Human Factors in Computing Systems, New York, NY, USA, 2009, pp. 211–220.

[18] L.A. Goodman, Snowball sampling, Ann. Math. Stat. 32–1 (1961) 148–170.

[19] M. Granovetter, The strength of weak ties, Am. J. Sociol. 78–6 (1973) 1360– 1380.

[20] C. Gronroos, From marketing mix to relationship marketing: toward a paradigm shift in marketing, Manage. Decis. 32–2 (1994) 4–20

[21] M. Gupte, T. Eliassi-Rad, Measuring tie strength in implicit social networks, Proceedings of the 4th Annual ACM Web Science Conference, ACM, New York, NY, USA, 2012, pp. 109–118

[22] J. Ha, S.H. Kwon, S.W. Kim, C. Faloutsos, S. Park, Top-N recommendation through belief propagation, Proceedings of the 21st ACM International Conference on Information and Knowledge Management (CIKM ‘12), ACM, New York NY USA 2012 pp. 2343-2346

[23] M.S. Handcock, K.J. Gile, Modelling networks from sampled data, Ann. Appl. Stat. 4 (2010) 5–25.

[24] D. Hawkins, R. Best, K. Coney, Consumer Behavior: Building Marketing Strategy, McGraw-Hill, Boston, USA, 2004.

[25] A.M. Hughes, Strategic Database Marketing—The Master Plan for Starting and Managing a Pro<sup>fi</sup>table, Customer-based Marketing Program, McGraw-Hill Professional, 2005.

[26] A.M. Hughes, Strategic Database Marketing, Probus Publishing, Chicago, 1994

[27] A. Josang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decis, Support Syst, 43–2 (2007) 618–644

[28] H. Kautz, B. Selman, M. Shah, Referral Web: combining social networks and collaborative filtering, Commun, ACM 40–3 (1997) 63-65.

[29] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers – measuring in<sup>fl</sup>uence in customer networks. Decis, Support Syst, 46–1 (2008) 233–253

[30] K.S. Kwon, J.H. Cho, Y.T. Park, Multidimensional credibility model for neighbor selection in collaborative recommendation, Expert Syst. Appl. 36 (3–2) (2009) 7114–7122.

[31] M.K.O. Lee, E. Turban, A trust model for consumer Internet shopping, Int. J. Electron. Comm. 6–1 (2001) 75–91.

[32] A. Levi, O. Mokryn, C. Diot, N. Taft, Proceedings of the Sixth ACM Conference on Recommender Systems (RecSys ‘12), ACM, New York, NY, USA, 2016, pp. 115– 122.

[33] D.R. Libey, Libey on RFM, e-RFM.com (1998), Available at: http://www.e-rfm. com/libey/, (accessed: 25.04.13).

[34] L.F. Lin, Y.M. Li, W.H. Wu, A social endorsing mechanism for target advertisement diffusion, Inform. Manage. 52–8 (2015) 982–997.

[35] P. Lotich, Smart Church Management: A Quality Guide to Church Administration, CreateSpace Independent Publishing Platform, 2012 (July 3).

[36] Y.B. Lu, L. Zhao, B. Wang, From virtual community members to C2C ecommerce buyers: trust in virtual communities and its effect on consumers purchase intention, Electron. Comm. Res. Appl. 9–4 (2010) 346–360.

[37] R.J. Miglautsch, Thoughts on RFM scoring, J. Database Market. 8–1 (2000) 67– 72.

[38] Nielsen Global Consumers’ Trust in ‘Earned’ Advertising Grows in Importance Available at: http://www.nielsen.com/us/en/insights/press-room/2012 nielsen-global-consumers-trust-in-earned-advertising-grows.html, (accessed: 2013).

[39] D.L. Olson, D. Delen, Advanced Data Mining Techniques, 1st edition, Springer, 2008.

[40] J.P. Onnela, J. Saramaki, J. Hyvonen, G. Szabo, D. Lazer, K. Kaski, J. Kertesz, A.L. Barabasi, Structure and tie strengths in mobile communication networks, Proc. Natl. Acad. Sci. U. S. A. 104–18 (2007) 7332–7336.

[41] E.P. Phillippa, G.L. Robins, T.A.B. Snijders, P. Wang, Conditional estimation of exponential random graph models from snowball sampling design, J. Math. Psychol, 57 (2013) 284–296.

[42] C. Pornpitakpan, The persuasiveness of source credibility: a critical review of <sup>fi</sup>ve decades' evidence, J. Appl. Soc. Psychol. 34–2 (2004) 243–281.

[43] Referral Rock, Referral Rock, http://www.capterra.com/referral-software/ spotlight/139089/Referral%20Rock/Referral%20Rock.

[44] S.G.B. Roberts, R. Wilson, P. Fedurek, R.I.M. Dunbar, Individual differences and personal social network size and structure, Personal. Indiv. Differences 44 (4) (2008) 954–964.

[45] T. Robertson, J. Zielinski, S. Ward, Consumer Behavior Scott, Foresman and Company, 1984.

[46] D. Schweitzer, A note on Whitehead’s factors of source credibility, Quarter. J. Speech 55 (1969) 308–310.

[47] T.A.B. Snijders, P.E. Pattison, G.L. Robins, M.S. Handcock, New speci<sup>fi</sup>cations for exponential random graph models, Sociol. Methodol. 36 (2006) 99–153.

[48] A.J.S. Stanaland, The referral engine: teaching your business to market itself, J. Consum. Market. 28–7 (2011) 550–551.

[49] W. Tsai, S. Ghoshal, Social capital and value creation the role of intra<sup>fi</sup>rm networks, Acad. Manage. J. 41–4 (1998) 464–476.

[50] J.T. Wei, S.Y. Lin, H.H. Wu, The review of the application of RFM model, Afr. J. Bus. Manage. 4–19 (2010) 4199–4206.

[51] C. Wilson, B. Boe, A. Sala, K.P.N. Puttaswamy, B.Y. Zhao, User interactions in social networks and their implications, Proceeding of 4th ACM European Conference on Computer Systems, ACM, New York, NY USA, 2009, pp. 205–218

[52] L. Xiong, L. Liu, A reputation-based trust model for peer-to-peer ecommerce communities, Proceedings of the 2003 IEEE International Conference on E-Commerce, Newport Beach, CA, IEEE Computer Society Press, Los Alamitos CA, 2003, pp. 275–284.

[53] L. Xiong, L. Liu, Peer Trust: supporting reputation-based trust for peer-to-peer electronic communities, IEEE Trans. Knowl. Data Eng. 16–7 (2004) 843–857.

[54] I.C. Yeh, K.J. Yang, T.M. Ting, Knowledge discovery on RFM model using Bernoulli sequence, Expert Syst. Appl. 36–3 (2008) 5866–5871.

[55] Y. Zhang, J. Bian, W.X. Zhu, Trust fraud: a crucial challenge for China’s ecommerce market, Eectron. Comm. Res. Appl. (2016) Available online 13 December 2012.

[56] C.N. Ziegler, J. Golbeck, Investigating interactions of trust and interest similarity, Decis. Support Syst. 43–2 (2007) 460–475

Cheng-Yang Lai received his Ph.D. from the Institute of Information Management, National Chiao Tung University, Taiwan. His research interests include electronic commerce and business intelligence. His research has appeared in Decision Support Systems, Electronic Commerce Research and Applications, and Information Sciences.

Yung-Ming Li is a professor at the Institute of Information Management, National Chiao Tung University, Taiwan. He received his Ph.D. in Information Systems from the University of Washington. His research interests include network science, Internet economics, and business intelligence. His research has appeared in IEEE/ ACM Transactions on Networking, INFORMS Journal on Computing, Decision Sciences, International Journal of Electronic Commerce, Information and Management, Decision Support Systems, European Journal of Operational Research, International Conference on Information Systems (ICIS), Workshop on Information Technology and Systems (WITS), among others.

Lienfa Lin is an associate professor at the Department of Information Communication, Kao Yuan University, Taiwan. He received his Ph.D. degree in information management from National Chiao Tung University. His research interests include electronic commerce, mobile computing, and network economics. His research has appeared in Decision Support Systems, International Journal of Electronic Commerce, and Information and Management.
