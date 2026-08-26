---
otero_id: 3194
otero_key: "7KDVBBB3"
title: "Input online review data and related bias in recommender systems"
authors: "Selwyn Piramuthu; Gaurav Kapoor; Wei Zhou; Sjouke Mauw"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.02.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Input online review data and related bias in recommender systems

Selwyn Piramuthu <sup>a,c,</sup>⁎, Gaurav Kapoor <sup>a</sup>, Wei Zhou <sup>b,c</sup>, Sjouke Mauw <sup>d</sup>

<sup>a</sup> Information Systems and Operations Management, University of Florida Gainesville, Florida 32611-7169, USA

<sup>b</sup> ESCP Europe, Paris, France

<sup>c</sup> RFID European Lab, Paris, France

<sup>d</sup> Université du Luxembourg, Faculté des Sciences, de la Technologie et de la Communication (FSTC), 6, rue Richard Coudenhove-Kalergi, L-1359, Luxembourg

## a r t i c l e i n f o

Article history: Received 19 January 2011 Received in revised form 1 November 2011 Accepted 12 February 2012 Available online 17 February 2012

Keywords: Sequential bias Online reviews Recommender system

## a b s t r a c t

A majority of extant literature on recommender systems assume the input data as a given to generate recommendations. Both implicit and/or explicit data are used as input in these systems. The existence of various challenges in using such input data including those associated with strategic source manipulations, sparse matrix, state data, among others, are sometimes acknowledged. While such input data are also known to be rife with various forms of bias, to our knowledge no explicit attempt is made to correct or compensate for them in recommender systems. We consider a speci<sup>fi</sup>c type of bias that is introduced in online product reviews due to the sequence in which these reviews are written. We model several scenarios in this context and study their properties.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Potential customers sometimes have the option of using recommender systems (e.g., amazon.com, buzzillions.com, consumersearch.- com, digg.com, Google AdSense, Net<sup>fl</sup>ix challenge, prorevs.com, slashdot.com) as convenient (although not completely reliable) automated sources of information in situations where there is a lack of other alternatives. These systems are for the most part used to supplement rather than to supplant the real thing which is recommendation from a known and completely reliable expert source.

Source of input for recommender systems include (implicit) past behavior (e.g., consumer transaction data, bookmark, page view time, from and to link for a Web page, social network) and (explicit) customer reviews. Both implicit and explicit data complement each other in terms of information content since the former records the behavior (i.e., customer A bought widget X) while the latter records details of this customer's (dis-)satisfaction with this purchase. Recommendations are generated based on (dis-)similarity between the characteristics of the user being recommended to and others in the database as well as (dis-)similarity between item of interest and related items. Several methods are used in the process including collaborative <sup>fi</sup>ltering (e.g., amazon.com) and content <sup>fi</sup>ltering (e.g., Music Genome Project used in pandora.com). Collaborative <sup>fi</sup>ltering uses the (dis-)similarity information across users and items (e.g., [15]). Content <sup>fi</sup>ltering, on the other hand, is based on the characteristics of users and items.

Adomavicius and Tuzhilin ([1]) provide an excellent overview of this general area.

Given the popularity of recommender systems, several facets of such systems have been extensively studied including mining usergenerated review data for implicit as well as explicit patterns, attacks, interface design, among others (e.g., [5,6,8,16]). Other than attacks, which explicitly manipulate input data to achieve an intended recommendation (e.g., manipulate reviews so an item of interest enters or leaves the set of highly recommended items), other aspects of input data (e.g., bias) have not received their fair share of attention from researchers in this area.

Bias in user-generated reviews can take several forms including personal (based on past experience, interest, attitude), extreme reviews (overly positive or negative), context (e.g., review of a camera's resolution characteristics can be positively or negatively biased based on its use – pictures for high-resolution printing vs. posting low-resolution pictures online), temporal (early vs. late adopters of a product may have different perspectives on the same product), awareness effect ([7]), herd behavior ([3]), and con<sup>fi</sup>rmation bias ([2]).

Sequential bias is a variant of <sup>fi</sup>rst-impression bias (e.g., primacy– recency effect) and is also in<sup>fl</sup>uenced by pre-existing (positive, negative) bias. Thus, the role played by <sup>fi</sup>rst impression bias cannot be overestimated ([4,14]). Therefore, the review that is <sup>fi</sup>rst seen by a prospective customer of the product of interest plays a signi<sup>fi</sup>cant role in purchase decisions that follow. These reviews are quite in<sup>fl</sup>uential since prospective purchasers of reviewed products rely heavily on these reviews in making their purchase decisions (e.g., [20]). The sequence in which reviews are written play an appreciable role in how the reviews that follow later in the sequence are written. For example, if a reviewer is favorable to the product reviewed, she might be biased to write stronger reviews to somehow compensate for the effects of existing negative reviews and vice versa. The reviews thus written are biased, in part, due to their position in the sequence of reviews. In turn, the recommender systems that use these biased reviews to generate their recommendations will clearly generate biased recommendations due, in part, to this sequential bias.

We purport to <sup>fi</sup>ll this gap in extant literature by speci<sup>fi</sup>cally considering sequential bias present in consumer reviews and the consequence of this bias on resulting recommendations generated. In other words, while recommender systems use user-generated data as-is, we believe there is a need to rid this data of sequential bias to provide better or less-biased recommendations. By explicitly acknowledging the existence of sequential bias and actively employing means to remove it from input data to recommender systems, one can alleviate its effect in the recommendations. We are, therefore, interested in the scenario where a customer purchases/experiences a product and then proceeds to provide a written review of this product online. During this process, the customer also has a chance to read existing reviews on this product before writing a review. It is precisely these existing reviews that causes sequential bias in the next review that is written.

The remainder of the paper is organized as follows. We discuss related background information and literature in the next section. We study the dynamic associated with sequential bias and its effect on recommender systems in Section 3. Section 4 concludes this paper with a brief discussion.

## 2. Background and related literature

A generic framework of a recommender system is given in Fig. 1. Both implicit and explicit data are used as input to the system, which uses these to generate (i.e., learn and store explicit knowledge in) the knowledge-base. The knowledge-base essentially comprises both explicit and implicit patterns extracted from (implicit & explicit) input data. The recommender system then waits for a user to enter the system. Upon arrival of a user, who could be a potential customer, the system takes a snap-shot of this user's characteristics and matches this with learned knowledge to generate appropriate recommendations in a timely manner. In what follows, the recommendations would be used to update system con<sup>fi</sup>guration either automatically or via human interference. Consequently, these new updates would eventually alter online users' behavior towards pricing and recommendation. The closed loop assures that normal system performance can be maintained at a stabilized level according to the theory of automation.

Although it is generally assumed that what consumers do (i.e., implicit or past behavior data) provides better information for recommender systems than what they say (explicit or consumer review data), both these data provide complementary information that are bene<sup>fi</sup>cially utilized in recommender systems. While both explicitly and implicitly generated data are used in recommender systems, we are interested in only explicit (i.e., user-generated reviews) input data in recommender systems. The use of user-generated explicit recommendation data has its associated challenges. We provide a brief overview of several such challenges and then some related literature in this area.

## 2.1. Some challenges

Recommender systems face several challenges when dealing with explicit input data. A list of a selected few of these challenges include: (a) strategic source manipulations (e.g., pro<sup>fi</sup>le injection attacks such as sybil, shill, random, sampling, average, bandwagon), (b) those associated with equally weighted input (e.g., user-generated reviews for a computer and a pack of chewing gum are not treated differently), (c) the endemic sparse matrix and the dif<sup>fi</sup>culty in generating useful patterns from such a matrix, cold start problem that arises when a user or product is new to the system and the absence of historical data on these entities and their characteristics, (d) differences in user risk tolerance levels, (e) staleness of data used in generating recommendations, (f) seasonality and trends in consumer preferences and their effect on user-generated reviews, and (g) general input data bias. We are interested in the bias which occurs due to the characteristics of the reviewed item (e.g., price, familiarity, stake to the customer, whether this item was purchased as a gift to someone else, the relationship of the purchaser to the giftee), the presence of extraneous stimulus whereby the item would not have been explicitly purchased had it not been for promotions and bundling, the highly self-selective nature of providing reviews and the sequential manner in which reviews are written. We are speci<sup>fi</sup>cally interested in the latter – i.e., the sequence in which reviews are written and the (mostly unintended) bias that is introduced in these reviews resulting from its position in the sequence.

When perusing existing reviews on the product of interest, the intensity/magnitude of the reviewer's sentiment as well as the positivity (or negativity) of reviews on various product features/characteristics (as well as the overall review of this product) certainly affect the reader. Several studies in the social sciences suggest that people often assign more weight to negative information than positive information of equal intensity (e.g., [9,17]). Mizerski ([12]) found that product attributes rated unfavorably exert greater in<sup>fl</sup>uence than those rated favorably on consumers' attributions, beliefs and attitudes. This phenomenon has been termed the negativity effect (bias). Ahluwalia ([17]) found that highly committed consumers showed positivity effect (bias) where they weigh positive information more than negative information. I.e., there is evidence for both positivity and negativity effect depending on consumer as well as product characteristics.

In addition to the introduction of unintentional bias in usergenerated product reviews, there also exists bias that are intentionally introduced due to professional relationships and friendships ([21]) and others with ulterior motives (e.g., [19,22,23]). Buzz marketing (e.g., [18]) is a variation on the same theme with the explicit intention of promoting a product, service, or idea.

## 2.2. Related literature

The literature on recommender systems is extensive and covers a wide spectrum of related issues. We list a few from among these here. Since online product reviews are not strictly regulated, there are opportunities for the introduction of ‘fake’ or intentionally biased reviews. A popular approach to mediating this risk is through self-regulation in the form of ratings and comments. Examples of this include x of y people found the following review helpful on amazon.com, x of y customers found this review helpful on buzzillions.com, diggs on digg.com, and Karma on slashdot.org. There are also commercial service providers such as eModeration.com where content moderation issues are evaluated in a neutral environment and KwikChex.com where negative reviews are contested.

![](/api/attachments/7KDVBBB3/fulltext/images/8360e867e36b9c498771fbf1ea0c8384c599bb303aa8fdd2db94dbca4897b399.jpg)  
Fig. 1. A generic recommender system framework.

Several studies have been reported in the literature on variations of both unintentional and intentional bias introduced in reviews. Lauw, Lim, and Wang ([10]) investigate how deviation in evaluation activities may reveal bias on the part of reviewers and controversy on the part of evaluated objects. They claim that signi<sup>fi</sup>cant deviation may help reveal bias of reviewers or controversy of objects. They de<sup>fi</sup>ne bias as the deviation in a user-assigned score from the mean score for a ‘less controversial’ object. They measure controversy as the deviation of user-assigned scores for that object.

Staddon and Chow ([21]) use association rule mining to identify bias introduced by book reviewers and authors of books they review. Specifically, they look for associations between these reviewers and authors in Web documents. When these two are present in a signi<sup>fi</sup>cant number of Web documents where either of them is present, there is a valid reason demanding closer scrutiny. They consider 300 books on amazon.- com that are categorized under ‘cryptography’ and observe that this method results in high precision (few false positives)

Using data on book reviews from amazon.com, Li and Hitt ([11]) <sup>fi</sup>nd that earlier reviews in<sup>fl</sup>uence the item's quality perception and have a positive bias on sales volume of the item considered. Moreover, they <sup>fi</sup>nd that prospective customers do not take this bias into consideration when making their decisions. In practice, reviews along with other online consumer behavior are aggregated to develop effective recommendations. A common practice is to use collaborative <sup>fi</sup>ltering that incorporates multiple data sources to predict consumer preference and behavior, such as those that are used at Amazon and Net<sup>fl</sup>ix.

## 3. Effect of sequential bias in recommender systems

We consider several variations of bias introduced in user-generated reviews. We assume reviewers rate a product as well as its attributes. For example, a reviewer may assign an overall rating for a car as positive while assigning negative rating to its fuel ef<sup>fi</sup>ciency, very positive rating to its cup holders, neutral rating to its maintenance cost, etc. I.e., although the overall rating is a function of the ratings for each of its characteristics, this function is highly likely to vary among reviewers based primarily on their individual and aggregate derived utility. For the remainder of this paper, when we refer to a review as biased or unbiased we are referring only to sequential bias. The absence of sequential bias does not in any way signify the presence or absence of other types of biases. However, given that we concern ourselves only with sequential bias, other types of biases are irrelevant to this work and are hence not considered.

We consider reviews written for a speci<sup>fi</sup>c product of interest. We assume that this product is unique and that it does not have any substitutes. Since we are not interested in content analysis of written reviews, we only consider a single numerical score that is assigned by each reviewer. The modeling exercise is kept distribution-free on purpose to facilitate general applicability. Reviews written after the <sup>fi</sup>rst review do not assume knowledge of the existence of sequential bias. I.e., the occurrence of sequential bias is implicit and unintentional on the part of the reviewer and any given reviewer is unaware of the presence of sequential bias in earlier as well as the current review. The following notations are used in this paper:

R′i

$R _ { i }$ (true) online review written by reviewer i (without sequential bias)

online review written by reviewer i (with sequential bias)

$$
\begin{array}{l l} \text { We   assume } R _ {1} = R _ {1} ^ {\prime} \\ \beta & (\text { bias }) \text { discount   factor } (0 <   \beta <   1) \\ B _ {i j} & \text { bias   of   review } R _ {i} ^ {\prime} \text { on   review } R _ {j} (B _ {i j} = 1 \text { for } i = j) \\ s _ {i j} - \text { direction   (sign)   of   bias } = & \left\{ \begin{array}{l l} 0 & \text { if } R _ {i} ^ {\prime} \& R _ {j} \text { are   both   positive / negative / neutral } \\ - 1 & \text { if } R _ {i} ^ {\prime} \text { is   positive } \& R _ {j} \text { is   not   positive } \\ - 1 & \text { if } R _ {i} ^ {\prime} \text { is   negative } \& R _ {j} \text { is   not   negative } \\ 0 & \text { if } R _ {i} ^ {\prime} \text { is   neutral } \end{array} \right. \\ \text { where } s _ {i j} = 0 \text { for } R _ {i} = 0 \\ U () & \text { Utility   function } \\ a, b & \text { Minimum   and   maximum   review   scores } \\ k & \text { Risk   tolerance   model   parameter } (k > 1) \\ u _ {i} & \text { Review } R _ {i} ^ {\prime} \text { 's   usefulness   score } (0 \leq u _ {i} \leq 1) \end{array}
$$

The $s _ { i j }$ term directly represents sequential bias where i represents an earlier review and j represents the current review. I.e., $s _ { i j }$ determines the sign of the effect of j on i. When both reviewers i and j are positive, negative, or neutral, there is no friction between their reviews and s equals zero. However, when reviewer i is positive or neutral and reviewer j is not positive or negative respectively reviewer i's review exerts negative friction on reviewer j's review due to sequential bias and this is represented by a negative $s _ { i j } .$ Similarly when reviewer i is negative or neutral and reviewer tj is not negative or positive respectively, reviewer i's review exerts positive friction on reviewer j's review due to sequential bias and this is represented by a positive $s _ { i j } .$

The <sup>fi</sup>rst scenario we consider includes two entities of interest: the reviewer and the online review written by this reviewer on a given product of interest. We consider the case where the potential reviewer purchases a product, experiences this product <sup>fi</sup>rst-hand, and then decides to write an online review of this product. Without loss of generality, we consider the reviewer to have assigned a single numerical value (for R ) from a pre-de<sup>fi</sup>ned range representing very negative, negative, neutral, positive, and very positive reviews on the product of interest. Clearly, any given product may have anywhere from zero through several reviews written by (presumably) different reviewers over time. We assume that each of these online reviews is independent of one another. I.e., a reviewer is unaffected/unin<sup>fl</sup>uenced by existing online reviews on the same product to abstain from intentionally/unintentionally modifying his/her (absolute) review. This is the base case where independence of each review is assumed.

The second scenario we consider is given in Fig. 2. Here, we introduce sequential bias on reviews $\left( R _ { 2 } \cdots R _ { n } \right)$ that is a direct (unintentional) result of perusing reviews (previously) written by other reviewers. Of course, when there is only one existing online review for a product, the previous scenario would apply because of the sheer lack of opportunity for this review to be biased based on other (nonexistent) reviews.

In this scenario (Fig. 2), the reviews written by reviewers $i = 1 , 2$ and 3 are:

$$
\begin{array}{l} R _ {1} \\ R _ {2} + R _ {1} (B _ {1 2} \times s _ {1 2}), \text { and } \\ R _ {3} + R _ {2} ^ {'} (B _ {3 3} \times s _ {2 3}) + R _ {1} (B _ {1 3} \times s _ {1 3}) \end{array}
$$

respectively. The <sup>fi</sup>rst reviewer is unbiased by previous reviews of this product by other reviewers. Therefore, the review provided by the <sup>fi</sup>rst reviewer is an absolute (unbiased) review by this reader (i.e., reviewer 1 provides unbiased review $R _ { 1 } )$ . The second reviewer, however, is biased by the <sup>fi</sup>rst reviewer's review. The second reviewers review is a composite of this reviewer's unbiased review $( \mathrm { i } . \mathrm { e } . , R _ { 2 } )$ and the bias due to the <sup>fi</sup>rst reviewer's review $( \mathrm { i } . \mathsf { e } . , R _ { 1 }$ times the bias represented by $B _ { 1 2 }$ times the direction of the bias). The magnitude of the bias $\left( \ \mathrm { i } . e . , \ B _ { 1 2 } \right)$ only provides the absolute value of the bias. When both the reviews are overall positive or both the reviews are overall negative, we assume the absence of any sequential bias since bias in this sense occurs as a compensation for friction between or negation of existing review(s) and the new review. Similarly, when the <sup>fi</sup>rst review is neutral, we assume this review to exert no friction (and, therefore, no compensatory pressure) on the following reviews. However, when the <sup>fi</sup>rst review is overall positive while the second review is overall negative, the second reviewer (unintentionally) compensates for existing positive review by being more negative resulting in negatively biased second review and vice versa. We assume additive relationship between each pair of new review and every existing review since the in<sup>fl</sup>uence from each of the existing reviews on the new review are independent of one another. A squashing function could be used to keep the review value within a prespeci<sup>fi</sup>ed range if necessary. We do not attempt this since it does not affect the results or resulting insights.

![](/api/attachments/7KDVBBB3/fulltext/images/3915a5ca59c753b036e560332861977be0f5013ece7963b892f7963f1a0ba7c4.jpg)  
Fig. 2. Previous reviews + addition of a new review on a product.

The review by the third reviewer is similarly biased by all preceding reviews (here, reviews 1 & 2). The third reviewer's review is therefore a composite of this reviewer's unbiased review $( \mathrm { i } . \mathsf { e } . , R _ { 3 } )$ and the bias due to the <sup>fi</sup>rst reviewer's review (i.e., $R _ { 1 } ( B _ { 1 3 } \times s _ { 1 3 } ) )$ and the second reviewer's review (i.e., $R ^ { \prime } { } _ { 2 } ( B _ { 2 3 } \times S _ { 2 3 } ) )$ . The general expression for the review written by the nth reviewer is:

$$
R _ {n} + \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times B _ {i n} \times s _ {i n}
$$

Assuming the bias is some form of discounting comprising a discount factor of the linear distance between the two reviews, we can represent $B _ { i j } \ : \mathsf { a s } \ : \beta ^ { j - i }$ and the general expression can be written as:

$$
R _ {n} + \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {'} \times \beta^ {n - i} \times s _ {i n}
$$

This can be justi<sup>fi</sup>ed by the generally accepted observation that (1) most perusers of existing reviews do not deal with the entire set of existing reviews but rather a manageable subset, and (2) the most recent review read is, ceteris paribus, likely to be more in<sup>fl</sup>uential than the one that was read a few reviews earlier. Some form of discounting factor discounts away the reviews that are assumed to be unread and the same discounting factor assigns more weight to recent rather than earlier reviews among those that were perused.

The next scenario (Fig. 3) incorporates the risk tolerance level or the risk attitude of the reviewer into the picture. By risk tolerance we signify or represent the extent to which this reviewer is riskseeking, risk-neutral, or risk-averse. We model the risk tolerance level of the new reviewer using a standard power utility function:

$$
U (x) = \frac {(x - a) ^ {k}}{(b - a) ^ {k}} \quad \text { where } 0 \leq U (x) \leq 1
$$

Here, a and b are the minimum and maximum review scores respectively and k is a model parameter. Risk aversion is characterized by a concave utility function and risk seeking behavior is characterized by a convex function. The parameter k can be varied to obtain different levels of concavity and correspondingly different levels of risk aversion. To model risk seeking behavior using a convex utility function, we set $k > 1 ,$ . The general expression can now be written as follows:

$$
R _ {n} + \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times \beta^ {n - i} \times s _ {i n} \frac {(R _ {n} - a) ^ {k}}{(b - a) ^ {k}}
$$

![](/api/attachments/7KDVBBB3/fulltext/images/18d301473059a0aa22cfbda0d75aa4ec02107e567a0b361410c583713812e289.jpg)  
Fig. 3. Previous reviews + risk tolerance + addition of a new review.

The above expression is modeled with the risk tolerance level as a multiplicative factor and not as the overall utility loss or gain in response to uncertainty. We decided on this form to enable discounting of the remaining expression by this fraction since, for example, β does not directly affect risk tolerance of any given review.

Several online stores (e.g., amazon.com) provide means to rate individual online reviews based on its usefulness to perusers of such reviews. These reviews are given a score, which is a ratio of the number of users who found a review useful vs. the number of users who perused that review. This is a crude measure of the belief (or, disbelief) placed by the new reviewer on any given (existing) review. In other words, previous perusers' evaluation of any given review's usefulness provides a proxy for the trust that one can place on that review. We include this usefulness score (i.e., u for review R ) as a multiplicative factor in the new review where $0 { \leq } u _ { i } { \leq } 1 . \mathrm { W e }$ assign $u _ { i } = 0$ for the extreme case where none of the previous perusers of review $R _ { i }$ found this review to be useful and $u _ { i } = 1$ for the other extreme case where all of the previous perusers of review $R _ { i }$ found it to be useful. The range in-between $\left( \mathrm { i . e . , ~ } 0 { < } u _ { i } { < } 1 \right)$ represents the case where some $( \mathrm { i } . \mathrm { e } . , \geq 1 )$ of the previous perusers of review $R _ { i }$ found this review to be useful.

The next scenario considered incorporates this information (Fig. 4). The new reviewer's review is now

$$
R _ {n} + \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times \beta^ {n - i} \times s _ {i n} \times u _ {i}
$$

The last model (Fig. 5) incorporates sequential bias based on previous reviews, previous reviews' usefulness measure scores, and the new reviewer's risk tolerance level in determining the characteristics of the new review. Here, the newest reviewer's review is given by:

$$
R _ {n} + \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times^ {n - i} \times s _ {i n} \times \frac {(R _ {n} - a) ^ {k}}{(b - a) ^ {k}} \times u _ {i}
$$

Lemma 3.1. Overall, in the presence of sequential bias, risk-averse reviewers are biased to write more positive reviews than risk-seeking reviewers.

Proof. Only (sequentially) biased reviews are of interest here. We have:

$$
\sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times \beta^ {n - i} \times s _ {i n} \times \frac {(R _ {n} - a) ^ {k}}{(b - a) ^ {k}} \times u _ {i} \geq \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times \beta^ {n - i} \times s _ {i n} \times \frac {(R _ {n} - a) ^ {k ^ {\prime}}}{(b - a) ^ {k ^ {\prime}}} \times u _ {i}
$$

Here, risk-averse reviewers are represented on the left hand side and are associated with $0 < k < 1$ and risk-seeking reviewers (represented on the right hand side) are associated with $k ^ { \prime } > 1$ . Clearly, the expression on the left hand side is at least as much as that on the right hand side. □

Lemma 3.1 refers to the cases represented in Figs. 3 and 5 where the risk tolerance of the new reviewer are modeled.

![](/api/attachments/7KDVBBB3/fulltext/images/ba0901bf40eb2efdeba5152f6797e3b0d6ab310939f94eaff9035505c736b60a.jpg)  
Fig. 4. Previous reviews with score + addition of a new review.

Lemma 3.2. When the reviewers are all positive (or all neutral, or all negative), the reviews written are free of sequential bias.

Proof. This is a direct consequence of the sign of the bias term being equal to zero $( \mathrm { i } . \mathrm { e } . , s _ { i j } = 0 )$ when the reviewers are all oriented in the same direction. I.e., when reviewer#1 is positive and reviewe $\# 2$ is also positive, reviewer#2 does not have a need to compensate for reviewer#1's review. The same applies when every review is neutral or every review is negative. In the expression we have, when $s _ { i j } = 0$ the entire expression becomes zero. □

Theorem 3.3. The magnitude of new review provided by reviewer n $( i . e . , R _ { n } )$ when sequential bias is present is always at least as much as that provided in the case when sequential bias is absent. $I . e . ,$ , in the last model (Fig. 5) considered,

$$
| \text { unbiased } - R _ {n} | \leq | R _ {n} + \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times \beta^ {n - i} \times s _ {i n} \times \frac {(R _ {n} - a) ^ {k}}{(b - a) ^ {k}} \times u _ {i} |
$$

Proof. We represent the un(sequential)biased review by reviewer n $\left( \operatorname { I . e . , } R _ { n } \right)$ by ‘unbiased $\mathrm { ~ - ~ } R _ { n } . ^ { \prime }$ The right hand side of this expression includes (sequential) biased R values.

$$
| \text { unbiased } - R _ {n} | \leq | R _ {n} + \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times \beta^ {n - i} \times s _ {i n} \times \frac {(R _ {n} - a) ^ {k}}{(b - a) ^ {k}} \times u _ {i} |
$$

We show this proof by separately considering the three different possible cases depending on whether the new review with sequential bias $\left( R _ { n } \right)$ is positive, negative, or neutral.

Case 1: $R _ { n }$ is positive

Now, for any ${ R ^ { \prime } } _ { i } \left( 1 \leq i \leq n - 1 \right)$ , when ${ R ^ { \prime } } _ { i }$ is positive, $s _ { i n } = 0$ (since $s _ { i j } = 0$ when $R _ { i }$ and $R _ { j }$ are both positive) and the entire expression $( \mathrm { i . e . , } R _ { i } ^ { ' } \times \beta ^ { n - i } \times s _ { i n } \times \frac { ^ { - } ( R _ { n } - a ) ^ { k } } { ^ { ( h \mathrm { - } a ) ^ { k } } } \times u _ { i } )$ equals zero. When ${ R ^ { \prime } } _ { i }$ is negative, $s _ { i n }$ is negative $( \mathrm { i . e . , ~ } \stackrel { \scriptscriptstyle \mathrm { ( ) } } { - 1 } )$ and the entire expression is positive.

![](/api/attachments/7KDVBBB3/fulltext/images/be00c63deb57980cff39256336d875d4f1533c267bbc7e64c0f32136142ef17a.jpg)  
Fig. 5. Previous reviews with score + risk tolerance + addition of a new review.

When ${ { R } ^ { \prime } } _ { i }$ is neutral $( \mathrm { i } . { \bf e } . , R ^ { \prime } { } _ { i } = 0 ) , s _ { i n }$ is zero and the entire expression equals zero.

$$
\therefore \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times \beta^ {n - i} \times s _ {i n} \times \frac {(R _ {n} - a) ^ {k}}{(b - a) ^ {k}} \times u _ {i} \geq 0
$$

Case 2: R<sub>n</sub> is negative

For any ${ R ^ { \prime } } _ { i } \left( 1 \leq i \leq n - 1 \right)$ , when ${ R ^ { \prime } } _ { i }$ is negative, $s _ { i n } = 0$ (since $s _ { i j } = 0$ when $R _ { i }$ and $R _ { j }$ are both negative) and the entire expression equals zero. When ${ R ^ { \prime } } _ { i }$ is positive, $s _ { i n }$ is negative $( \mathrm { i } . \mathsf { e } _ { \cdot } , - 1 )$ and the entire expression is negative. When ${ R ^ { \prime } } _ { i }$ is neutral, $s _ { i n }$ is negative $( \mathrm { i } . \mathrm { e } _ { \cdot } , - 1 )$ and the entire expression equals zero.

$$
\therefore \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times \beta^ {n - i} \times s _ {i n} \times \frac {(R _ {n} - a) ^ {k}}{(b - a) ^ {k}} \times u _ {i} \leq 0
$$

Case 3: $R _ { n }$ is neutral $( \mathrm { i } . \mathbf { e } . , R _ { n } { = } 0 )$

For any ${ R ^ { \prime } } _ { i } \left( 1 \leq i \leq n - 1 \right)$ , when ${ R ^ { \prime } } _ { i }$ is neutral, $s _ { i n } = 0$ (since $s _ { i j } = 0$ when $R _ { i }$ and $R _ { j }$ are both neutral) and the entire expression equals zero. When ${ R ^ { \prime } } _ { i }$ is positive, $s _ { i n }$ is negative $( \mathrm { i } . \mathsf { e } _ { \cdot } , - 1 )$ and the entire expression is negative. When ${ { R } ^ { \prime } } _ { i }$ is negative, $s _ { i n }$ is positive $( \mathrm { i } . \mathsf { e } _ { \ast } , + 1 )$ and the entire expression is negative.

$$
\therefore \sum_ {i = 1} ^ {n - 1} R _ {i} ^ {\prime} \times \beta^ {n - i} \times s _ {i n} \times \frac {(R _ {n} - a) ^ {k}}{(b - a) ^ {k}} \times u _ {i} \leq 0
$$

□

Although we speci<sup>fi</sup>cally considered only the last model $\left( \mathrm { F i g . } \ 5 \right)$ in Theorem 3.3, this theorem applies to all the models considered in this paper. It should be noted that this theorem applies regardless of the degree of risk tolerance (i.e., risk-averse, risk-neutral, or risk-seeking perspective) of the reviewers. Theorem 3.3 is signi<sup>fi</sup>cant from a recommender system's perspective since the written reviews (here, assigned scores in new reviews) must be appropriately augmented to remove sequential bias. On the other hand, the reviews can be considered to be a lower-bound for generating recommendations.

Lemma 3.4. In the presence of sequential bias, a negative fake review has more positive effect when included earlier in the sequence.

Proof. We assume that the recommender system averages the review scores to obtain the recommendation.

Ignoring the effects of risk tolerance and scores on previous reviews to simplify notation, the reviews can be written as:

$$
R _ {1}, R _ {1} \beta s _ {1 n} + R _ {2}, R _ {1} \beta^ {2} s _ {1 n} + R _ {2} ^ {\prime} \beta s _ {2 n} + R _ {3}, \dots , R _ {1} \beta^ {n - 1} s _ {1 n} + R _ {2} ^ {\prime} \beta^ {n - 2} s _ {2 n} + \dots + R _ {n}
$$

The difference in the average when the fake review (say, R) is placed at position p vs. q, where $p { < } q ,$ is

$$
\begin{array}{l} \frac {1}{n} \times \sum_ {j = n - q} ^ {n - p - 1} R \times \beta^ {j} \times s _ {p n} \times \frac {(R - a) ^ {k}}{(b - a) ^ {k}} \times u _ {p} \\ i. e., \frac {1}{n} \times R \times \frac {\beta^ {n - q} - \beta^ {n - p}}{1 - \beta} \times s _ {p n} \times \frac {(R - a) ^ {k}}{(b - a) ^ {k}} \times u _ {p} \geq 0 \end{array}
$$

Here, $R , s _ { p n } \ ( = s _ { q n } )$ , and $u _ { p } \ ( = u _ { q } )$ are the same for this review regardless of its position in the sequence (of n reviews). The sign term $( \mathrm { i . e . , } \ s _ { p n } )$ is negative for negative $R _ { i } .$ Therefore, the earlier in the sequence of reviews the fake review is introduced, the more positive effect it has on the overall average. □

Lemma 3.5. In the presence of sequential bias, a positive fake review has more negative effect when included earlier in the sequence.

Proof. The proof is similar to Lemma 3.4. The difference in the average when the fake review (say, R) is placed at position p vs. q, where $p { < } q ,$ is the same as that in Lemma 3.4

$$
\frac {1}{n} \times R \times \frac {\beta^ {n - q} - \beta^ {n - p}}{1 - \beta} \times s _ {p n} \times \frac {(R - a) ^ {k}}{(b - a) ^ {k}} \times u _ {p} \leq 0
$$

Here, $R , s _ { p n } ,$ and $u _ { p }$ are the same for this review regardless of its position in the sequence. The sign term $( \mathrm { i } . \mathsf { e } . , s _ { p n } )$ is negative for positive R. Therefore, the earlier in the sequence of reviews the fake review is introduced, the more negative effect it has on the overall average. □

Lemmas 3.4 & 3.5 signify that regardless of its type (i.e., positive or negative), a fake review has a stronger effect when placed earlier in the sequence. $\mathrm { I . e . , }$ to enhance the recommendation of an item, the fake review is better off earlier or later in the sequence and vice versa depending on whether it is negative or positive respectively. When using such data as input to a recommender system, the earlier (or later) reviews in the sequence must be scrutinized for such effects depending on the overall recommendation generated.

Theorem 3.6. In the presence of sequential bias, assuming the magnitude of all previous reviews $( i . e . , R )$ are the same, the case where all positive reviews are stacked together and listed first results in a better (i.e., more positive and less negative)new review than otherwise when $\beta ^ { n - k - 1 } ( 2 - \beta ^ { k } ) < 1$

Proof. Ignoring the effects of risk tolerance and scores on previous reviews to simplify notation, the reviews can be written as:

$$
R _ {1}, R _ {1} \beta s _ {1 n} + R _ {2}, R _ {1} \beta^ {2} s _ {1 n} + R _ {2} ^ {\prime} \beta s _ {2 n} + R _ {3}, \dots , R _ {1} \beta^ {n - 1} s _ {1 n} + R _ {2} ^ {\prime} \beta^ {n - 2} s _ {2 n} + \dots + R _ {n}
$$

Consider a scenario where there are k positive reviews followed by $( n - 1 - k )$ negative reviews. The nth review can either be positive or negative.

Case 1: The nth review is positive. The <sup>fi</sup>rst k reviews are irrelevant (from a sequential bias perspective) since $s _ { i n } = 0$ (for $1 { \le } i { \le } k )$ in this scenario. The nth review is

$$
R _ {k + 1} ^ {'} \beta^ {n - k - 1} s _ {(k + 1) n} + R _ {k + 2} ^ {'} \beta^ {n - k - 2} s _ {(k + 2) n} + \dots + R _ {n - 1} ^ {'} \beta s _ {(n - 1) n} + R _ {n}
$$

The bias part is given by the above expression minus $R _ { n } .$ For the simpli<sup>fi</sup>ed case where all R values are the same, the resulting bias is:

$$
R \beta \frac {1 - \beta^ {n - k - 1}}{1 - \beta} s \geq 0
$$

Case 2: The nth review is negative. The last $( n - 1 - k )$ reviews are irrelevant (from a sequential bias perspective) since $s _ { i n } = 0$ (for k+ 1≤i≤n) in this scenario. The nth review is

$$
R _ {1} ^ {'} \beta^ {n - 1} s _ {1 n} + R _ {2} ^ {'} \beta^ {n - 2} s _ {2 n} + \dots + R _ {k} ^ {'} \beta^ {n - k} s _ {k n} + R _ {n}
$$

Similarly, for the simpli<sup>fi</sup>ed case where all R and s values are the same, the bias is:

$$
R \beta^ {n - k} \frac {1 - \beta^ {k}}{1 - \beta} s \leq 0
$$

We are interested in the scenario where the positive bias is more than the negative bias. I.e., the absolute value of the bias in Case

1 is more than the absolute value of the bias in Case 2. The former case is better than the latter when the expression in Case 1 is greater than that in Case 2. I.e.,

$$
\beta \frac {1 - \beta^ {n - k - 1}}{1 - \beta} > \beta^ {n - k} \frac {1 - \beta^ {k}}{1 - \beta}
$$

which, upon simpli<sup>fi</sup>cation, results in the given expression. □

The policy implication of Theorem 3.6 is that for an online retailer, with the facility for reviewers to write their reviews, to improve the overall recommendation of the product or service, it helps to list all the positive reviews <sup>fi</sup>rst followed by all other reviews.

Corollary 3.7. When sequential bias is present, the average bias in the new review when stacking all existing reviews of the same type together (all positives together or all negatives together) and listing them first (or last) is independent of the number of existing reviews of each type.

Proof. This is a direct consequence of Theorem 3.6. Consider the case where there are k positive reviews and $( n - 1 - k )$ negative reviews where $k { > } ( n { - } 1 { - } k )$ . When the k positive reviews are placed <sup>fi</sup>rst followed by the n−1−k negative reviews, the effect of this arrangement on the next review written from a sequential bias perspective depends on the type (i.e., positive or negative) of the new (i.e., nth) review.

Case 1: The nth review is positive. Here, the effect due to sequential bias is given (from Theorem 3.6) by

$$
R \beta \frac {1 - \beta^ {n - k - 1}}{1 - \beta} s
$$

Case 2: The nth review is negative. Again, the effect due to sequential bias is given (from Theorem 3.6) by

$$
R \beta^ {n - k} \frac {1 - \beta^ {k}}{1 - \beta} s
$$

On average, the effect of sequential bias on the next review is

$$
\frac {R s}{2 (1 - \beta)} \left(\beta - \beta^ {n - k} + \beta^ {n - k} - \beta\right) = \frac {R s}{2 (1 - \beta)} \left(\beta - \beta^ {n}\right)
$$

which is independent of k. □

## 4. Discussion & conclusion

We considered the effect of sequential bias in online product reviews from the perspective of recommender systems. To our knowledge, none of the existing recommender systems consider the existence of sequential bias. We modeled the bias by taking into account existing reviews, the usefulness of existing reviews as determined by the number of perusers of those reviews who found them to be useful, and the risk tolerance of reviewers who write such reviews. We then studied its dynamic and formulated a model using theoretical means. Our analysis shows that in<sup>fl</sup>uence due to sequential bias on subsequent reviews can be appreciable depending on the values of the modeled parameters. Developers or recommender systems therefore cannot ignore the existence of sequential bias in their input data. Given the popularity of recommender systems, there is an urgent need to develop means to remove in<sup>fl</sup>uences due to sequential bias. This will alleviate its deleterious effects on the quality and accuracy of recommendations generated by recommender systems.

In our analysis, we only consider the overall review in the form of a numerical value. Considering evaluations of individual characteristics in addition to the overall review could provide additional insights and, therefore, better recommendations by a recommender system.

We assumed that a reader goes through the reviews one at a time from top to bottom of the list of existing reviews. We also assumed that the new review is written after the perusal of the entire set of existing reviews. However, when the number of reviews for an item of interest is large it is not reasonable to expect anyone to peruse the entire set (e.g., [13]). Modeling this would involve knowing (1) the exact set of reviews perused by the new reviewer, and (2) the order in which this selected set of reviews are read by this new reviewer. Some online stores (e.g., amazon.com) allow the user to sort existing reviews in several different ways (e.g., most recent review <sup>fi</sup>rst, most useful reviews <sup>fi</sup>rst, most negative reviews <sup>fi</sup>rst) and this complicates the analysis even further.

While we considered the effect of sequential bias on recommender systems from a theoretical perspective, a few critical questions still remain and these can be addressed only through rigorous and strictly controlled <sup>fi</sup>eld experiments with human subjects. Does sequential bias signi<sup>fi</sup>cantly in<sup>fl</sup>uence recommendations made by recommender system by modifying the average and/or correlation values? If yes, does it matter? I.e., does it lead to signi<sup>fi</sup>cantly different recommendations? Under what conditions does this happen? And, what can the developer of a recommender system do about it? Given that sequential bias does exist in online product reviews, can we remove existing bias in reviews in such real-world databases so recommendations generated by recommender systems are more reliable and trust-worthy? We also did not explicitly model the scenario where the reviewers are mixed – i.e., some reviewers are in<sup>fl</sup>uenced by sequential bias whereas some others are not simply because they do/did not read reviews by other reviewers. What in<sup>fl</sup>uence do such mixed set of reviews have on the performance of recommender systems? This can be easily modeled by modifying R to R<sup>c</sup> where c=1 when review i is perused by the current reviewer and c=0 otherwise. We leave these as exercises for future studies.

## References

[1] Gediminas Adomavicius, Alexander Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions IEEE Transactions on Knowledge and Data Engineering 17 (6) (June 2005) 734–749.

[2] Linden J. Ball, Does Positivity Bias Explain Patterns of Performance on Wason's 2-4-6 task? in: Wayne D. Gray, Christian D. Schunn (Eds.), Proceedings of the Twenty-Fourth Annual Conference of the Cognitive Science Society, Routledge, 2002, p. 340.

[3] Yi-Fen Chen, Herd behavior in purchasing books online,, Computers in Human Behavior 24 (5) (2008) 1977–1992.

[4] Guillaume Deffuant, Sylvie Huet, Collective increase of <sup>fi</sup>rst impression bias, Complexity 15 (5) (2009) 25–33.

[5] Chrysanthos Dellarocas, Reputation mechanism design in online trading environments with pure moral hazard. Information Systems Research 16 (2) (2005) 209–230.

[6] Chrysanthos Dellarocas, Charles Wood, The sound of silence in online feedback: estimating trading risks in the presence of reporting bias. Management Science 54 (3)(2008) 460–476.

[7] Wenjing Duan, Gu. Bin, Andrew B. Whinston, Do online reviews matter? – an empirical investigation of panel data, Decision Support Systems 45 (4) (2008) 1007–1016.

[8] Ming Fan, Yong Tan, Andrew Whinston, Evaluation and design of online cooperative feedback mechanisms for reputation management. IEEE Transactions on Knowledge and Data Engineering 17 (2) (2005) 244–254.

[9] Jill G. Klein, Negativity effects in impression formation: a test in the political arena, Personality and Social Psychology Bulletin 17 (4) (1991) 412–418.

[10] Hady W. Lauw, Ee-Peng Lim, Ke Wang, Bias and controversy in evaluation systems, IEEE Transactions on Knowledge and Data Engineering 20 (11) (2006) 1490–1504 November 2008.

[11] Xinxin Li, Lorin Hitt, Self-selection and information role of online product reviews, Information Systems Research 19 (4) (December 2008) 456–474.

[12] Richard W. Mizerski, An attribution explanation of the disproportionate in<sup>fl</sup>uence of unfavorable information, The Journal of Consumer Research 9 (3) (1982) 301–310.

[13] Selwyn Piramuthu, Sequential Bias, Online Product Review, and Recommender Systems, Proceedings of the Workshop on Data Mining in Marketing (DMM'2010) at the Industrial Conference on Data Mining (ICDM), IbAI Publish ing, 2010, pp. 5–13.

[14] Matthew Rabin, Joel L. Schrag, First impressions matter: a model of con<sup>fi</sup>rmatory bias, Quarterly Journal of Economics (1999) 37–82.

[15] Paul Resnick, Neophytos Iacovou, Mitesh Suchak, Peter Bergstrom, John Riedl, GroupLens: An Open Architecture for Collaborative Filtering of Netnews, Proceedings of the Conference on Computer Supported Cooperative Work, Chapel Hill, NC, 1994, pp. 175–186.

[16] Paul Resnick, Richard Zeckhauser, John Swanson, Kate Lockwood, The value of reputation on eBay: a controlled experiment. Experimental Economics 9 (2) (2006) 79–101.

[17] Rohini Ahluwalia. 1996. “An Integrative Model of Market-Related Negative Information Processing," PhD Dissertation, Department of Marketing, Ohio State University.

[18] G. Ruskin, Commercial Alert asks FTC to Investigate Buzz Marketers for Deception, http://www.commercialalert.org/news/news-releases/2005/10/commercial-alertasks-ftc-to-investigate-buzz-marketers-for-deception (2005).

[19] G. Sandoval, Digg continues to battle phony stories, CNET.com(2006).

[20] Sylvain Senecal, Jacques Nantel, The in<sup>fl</sup>uence of online product recommendations on consumers' online choices, Journal of Retailing 80 (2004) 159–169.

[21] Jessica Staddon, Richard Chow, Detecting reviewer bias through web-based association mining, Proceeding of the 2nd ACM workshop on Information credibility on the web, 2008, pp. 5–10.

[22] The Guardian, Historian Orlando Figes admits posting Amazon reviews that trashed rivals, , April 23 2010http://www.guardian.co.uk/books/2010/apr/23/ historian-orlando-figes-amazon-reviews-rivals (retrieved on 16 June 2010).

[23] Robert Verkaik, The law is catching up with those who use the Internet to defame, The Independent, April 20 2010 (2010).

Selwyn Piramuthu is a Professor of information systems at the University of Florida. He is a member of the RFID European Lab in Paris and an Associate Researcher of Information Systems and Technologies at ESCP-Europe (Paris). His research interests include RFID systems, pattern recognition and its application in supply chain management, computer-aided manufacturing, and <sup>fi</sup>nancial credit-risk analysis.

Dr. Gaurav Kapoor graduated from the University of Florida in 2008, with a Ph.D. in Information Systems. His primary research interests include Security and Privacy protocols for RFID as well as bias in user reviews. His work has been published in multiple journals including Decision Support Systems and the European Journal of Information Systems.

Wei Zhou received his Ph.D. in Information Systems from the University of Florida. His research interests include RFID-enabled item-level information visibility, Internet advertising, and knowledge-based learning systems. His work has appeared in Annals of Operations Research, European Journal of Information Systems, European Journal on Operational Research, IEEE Transactions on Geosciences and Remote Sensing International Journal of Electronic Commerce, Journal of Organizational Computing and Electronic Commerce, and Optical Engineering.

Sjouke Mauw is professor in computer security at the University of Luxembourg. He is head of the SaToSS (Security and Trust of Software Systems) research group, which focuses on the application of formal methods to the design and analysis of secure systems. His research interests include security protocols, e-voting, security assessment, trust and risk management, privacy, non-repudiation protocols, attack trees, digital rights management, RFID security, and forensics.
