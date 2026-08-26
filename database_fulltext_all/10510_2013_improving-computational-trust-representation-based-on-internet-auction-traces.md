---
otero_id: 10510
otero_key: "QSJ3CDTK"
title: "Improving computational trust representation based on Internet auction traces"
authors: "Adam Wierzbicki; Tomasz Kaszuba; Radoslaw Nielek; Paulina Adamska; Anwitaman Datta"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.09.016"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving computational trust representation based on Internet auction traces<sup>☆</sup>

Adam Wierzbicki <sup>a,</sup>⁎, Tomasz Kaszuba <sup>a</sup>, Radoslaw Nielek <sup>a</sup>, Paulina Adamska <sup>a</sup>, Anwitaman Datta <sup>b</sup>

<sup>a</sup> Polish-Japanese Institute of Information Technology, Warsaw, Poland

<sup>b</sup> Nanyang Technological University, Singapore

## a r t i c l e i n f o

Article history: Received 18 May 2011 Received in revised form 8 June 2012 Accepted 23 September 2012 Available online 28 September 2012

Keywords: Trust management Reputation system Text mining Natural language processing Sentiment analysis Classi<sup>fi</sup>cation Taxonomy Reference Point methodology Detailed Seller Rating

## a b s t r a c t

Computational trust representations are used by Trust Management (TM) systems to elicit information from users about the behavior of others. In most practically used TM systems, simple computational trust representations dominate, such as the three-valued discrete scale of “negative”, “neutral” and “positive” used in reputation systems of Internet auctions. This paper asks the question: what is the appropriate system for computational representation of human trust? In order to <sup>fi</sup>nd an answer, we study a large trace of feedbacks and textual comments from a reputation system of an Internet auction. We discover that users systematically try to add information in the textual comments. Text-mining and NLP approaches reveal a taxonomy of non-positive feedbacks and an importance order on the categories of non-positive behavior. This importance order is further supported by survey data. Based on these observations, we propose and evaluate a complete, new computational trust representation system inspired by the work of Yager. This system is complemented by operators that can be used to produce rankings of most trusted agents. The operator used to create rankings selects Pareto-optimal agents with respect to the multiple criteria revealed by our trace analysis. The proposed system takes into account all criteria utilized by auction users to evaluate behavior, and the relative importance of these criteria. The proposed system is compared to the Detailed Seller Rating system introduced by eBay.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Trust is crucial for many social and commercial interactions. In online and virtual world settings, one may often interact with other unfamiliar individuals or entities. A comprehensive Trust Management (TM) system can facilitate decision support in such situations.

Most current TM systems use simple computational representations of trust. For instance, many internet auction sites use a three-valued discrete scale of “negative”, “neutral” and “positive” (with the notable exception of the new system used by e-Bay). The epinions recommendation system [12] likewise uses a three-valued scale. The FilmTrust [5] recommendation system uses a 10-valued discrete scale. Other theoretical reputation systems often use a continuous scale from [0,1] or [−1,1] [11,16], while a more complex system has been proposed by Josang [9] which uses a two-dimensional scale with uncertainty representation. However, even Josang's system only uses a simple scale for the actual representation of trust expressed by users. In practice, there are multiple aspects, some (perceived) more important than others, which cumulatively and subjectively determine one's trustworthiness. For instance, in an online auctioning scenario, whether the product being sold is genuine (w.r.to what was advertised) is important, but so may be other issues, for instance: whether it was delivered on time and undamaged, and if not, whether the seller was seen to be responsive in amending the situation or not, etc.

Several things are apparent from this illustrative example. Firstly, a simple scale is inadequate to capture the multi-faceted nature of interactions, which cumulatively determine the trustworthiness. Secondly, one can potentially come up with any arbitrary list of criteria, and moreover, different application domains will have different set of criteria. One size does not <sup>fi</sup>t all, and an arbitrary multi-dimensional scale will also be inadequate. Ultimately, the set of criteria should be application speci<sup>fi</sup>c, and driven by data (users' perceived needs and priorities).

To that end, the questions motivating this paper are: what is an appropriate system for computational representation of human trust (in the context of internet auctions)? Are the simpler systems used so-far (in)adequate for this purpose? And if they are not, can we propose a better computational representation and ways to process it in a Trust Management system for Internet auctions?

In our attempt to answer the above posed questions, it is necessary to use information on how real users evaluate trust or distrust. One important challenge here is that most available datasets are obtained from TM systems that use a simpler computational trust representation. Nonetheless, these systems, probably in order to account for the limitations introduced by the simplistic computational trust representation, often allow users also to add an accompanying textual comment. The crux of our approach is to dig into such textual comments from data obtained from a real auction site to identify the various issues that the users perceive are important. Speci<sup>fi</sup>cally, we will investigate the following questions: do users systematically try to add more information than is allowed by the computational trust scale used by the reputation system? What kind of information is being added by users? How are the quantitative reports (using the current computational trust scale) related to the additional information in textual comments? In order to answer these and like questions, we employ Natural Language and Sentiment analysis of the textual comments that extracts their emotional content, as well as a classi<sup>fi</sup>cation of comments that reveals an implicit, more complex preference structure of behavior valuations. This preference structure forms a partial order, because it is a dominance structure established by the simultaneous use of many diverse criteria to evaluate behavior.

Based on the analysis of the dataset, we will attempt to propose a trust representation system that is adapted to the implicit user requirements revealed by our analysis. The proposed system is inspired by the work of Yager [26] and Sabater-Mir [21]. It is also in some respects similar to eBay's new Detailed Seller Rating system.<sup>1</sup> Therefore, we will review the DSR system and discuss some of its de<sup>fi</sup>ciencies. We will also introduce operators that allow us to process the new computational trust. In this aspect, we go beyond the work of Sabater-Mir, introducing new operators and demonstrating how the proposed computational trust can be used to create rankings of sellers or buyers in Internet auctions, which is crucial for decision support.

The most important discovery from the analysis of our dataset is that auction site users utilize multiple criteria simultaneously to evaluate behavior of others, which in turn leads to a new requirement for the selection operator used to create rankings of buyers or sellers. This operator should choose agents that are Pareto-optimal with respect to the multiple evaluation criteria. We de<sup>fi</sup>ne such an operator based on the Reference Point methodology and compare the rankings it produces to DSR rankings.

Our new computational trust representation, designed for Internet auctions, can be generalized for other applications based on the observation that our proposed criteria are related to norms of behavior. The operator used to create rankings selects agents that are most compliant with multiple norms of behavior, i.e., Pareto-optimal with respect to procedural fairness. Even the importance order of our criteria can be expressed in norms using modal logic.

The rest of this paper is organized as follows: in the next section, we discuss in more detail the research hypotheses of the paper and their contribution to the research questions outlined in the introduction. In Section 3, we introduce the Internet auction dataset and present the relevant results of its analysis that demonstrate that users systematically try to add new information to the system. This information is present in the non-positive feedback and can be categorized into a taxonomy that can be fully expressed using the proposed new computational trust representation. Categories of feedbacks are related to norms of behavior that are the basis of criteria for behavior evaluation. In Section 4, we validate hypothesis 6 by showing that the data supports a second conclusion about the new trust representation: the various categories of non-positive behavior are not equally important to users. Users distinguish that some norms of behavior are more important than others. This information should be re<sup>fl</sup>ected in the way the reputation system processes the new proofs. Therefore, in Section 5 we introduce a new computational trust representation that generalizes eBay's DSR system, and new operators that can process the new proofs in a way that takes into account the importance of applied evaluation criteria. In Section 6, we evaluate the new proposed operators using simple simulations that compare them against the ranking used by eBay's DSR system. This evaluation validates hypothesis 7 by showing that it is possible to create a seller ranking based on the proposed proofs in a way that takes into account the importance of behavior evaluation criteria. In Section 7, we present related work on computational trust representation. Section 8 concludes the paper and discusses future work.

## 2. Hypotheses about usage of reputation systems in internet auctions

In this paper we will investigate the following hypotheses:

1. Users systematically add signi<sup>fi</sup>cant information in non-positive feedbacks in reputation systems for Internet auctions.

2. The non-positive feedbacks can be categorized into a taxonomy.

3. Each of the leaf categories speci<sup>fi</sup>es a criterion for behavior evaluation.

4. Each of the leaf categories is related to a norm of behavior.

5. The criteria of behavior evaluation speci<sup>fi</sup>ed by non-positive feedback categories can be used independently.

6. The criteria for behavior evaluation speci<sup>fi</sup>ed by non-positive feedback categories are not equally important to users.

7. It is possible design a reputation system so that it takes into account more criteria of behavior evaluation and ranks sellers taking into account criteria importance.

In the rest of this paper, the hypotheses listed here will be investigated sequentially, as the validation of the previous hypotheses is usually a condition for the consideration of the next one.

Hypothesis 1 can be veri<sup>fi</sup>ed by an investigation of a large set of feedbacks from a reputation system for an Internet auction. If it can be found that the non-positive feedbacks contain meaningful information that enhances or even changes the interpretation of the feedback value, the hypothesis will be positively validated. This hypothesis is a basic step to consider whether the enhancement of the reputation system is actually required.

Hypothesis 2 can be veri<sup>fi</sup>ed if most non-positive feedbacks from a large set can be assigned to a category of feedbacks, and if the categories form a taxonomy of more general non-positive categories. The leaf categories of the taxonomy should be associated with classi<sup>fi</sup>cation rules (for example, based on regular expressions) that can be used to assign each non-positive feedback into a category.

This hypothesis concerns the organization of the new proposed reputation system. If the non-positive feedbacks would be largely unrelated, it would not be possible to help users to report behavior in a systematic manner. It would also be very hard to predict the content of the future non-positive feedbacks. On the other hand, the existence of a taxonomy of non-positive feedbacks suggests that the types behavior reported by users follow a pattern that can be exploited in the new reputation system.

Hypotheses 3 and 4 can be veri<sup>fi</sup>ed by an investigation of the leaf categories of the taxonomy. Each of these leaf categories should be suf-<sup>fi</sup>ciently speci<sup>fi</sup>c in order to constitute of criterion of behavior evaluation that can be applied by the user (so that the user can evaluate his satisfaction with respect to that criterion). If this hypothesis would not hold, it would not be possible to associate each of the leaf categories with a rating in the proposed new reputation system.

For hypothesis 4 to hold, each leaf category should specify a type of behavior that can be described by a single sentence using modular logic operators such as “must”, “must not”. This hypothesis is not directly required for the design of the new reputation system, but has an interesting theoretical meaning, as it gives empirical support to the notion of normative trust: the de<sup>fi</sup>nition of trust as an expectation to follow social norms that apply in a certain social context [24].

Hypothesis 5 can be veri<sup>fi</sup>ed if a signi<sup>fi</sup>cant portion of non-positive feedbacks from a large set cannot be classi<sup>fi</sup>ed into a single category of the taxonomy, but can be classi<sup>fi</sup>ed into two or more such categories. If this hypothesis holds, it has an important consequence for the design of the reputation system. Previous work [26] has focused on systems that used multiple criteria that were dependent (increasing the value of one criterion reduced the value of the others). If the criteria are independent, the entire processing of reports by the reputation system should be redesigned.

Hypothesis 6 holds if there exists a preference relation (importance relation) on the criteria for behavior evaluation speci<sup>fi</sup>ed by non-positive feedback categories. To verify the hypothesis, the existence of the importance relation should be established using datamining of the set of non-positive feedbacks (in other words, using behavioral data) and also using a survey of users of Internet auctions (declarative data). The hypothesis will hold if signi<sup>fi</sup>cant differences in the importance of categories can be discovered. Note that the preference relation could be different for each individual user. However, the new proposed reputation system can allow the user to change his preferences regarding the importance of categories of non-positive behavior.

This hypothesis has a very important impact on the design of the new reputation system. If the hypothesis holds, the system should be able to express the importance relation and to use this information in the recommendation of transaction partners in the Internet auction system. This feature has not been proposed so far for reputation system in Internet auctions and is a new contribution.

Hypothesis 7 concerns a proof-of-concept of the proposed new reputation system. The <sup>fi</sup>nal output of such a system can be the recommendation of sellers in the form of a ranking. In order to verify the hypothesis, a method for constructing such a ranking should be proposed. This method should base on the design of reports in the proposed new reputation system and should process these reports taking into account the importance relation of the various criteria of behavior evaluation. The ranking method should also take into account the non-exclusive nature of criteria.

## 3. Analysis of feedbacks in Internet auctions

The analysis in Sections 3 and 4 proceeds as follows: <sup>fi</sup>rst, we verify whether users add more information in comments that can be represented using a simple scalar computational trust value (validation of hypothesis 2). Second, we verify whether the information can be divided into separate categories, and whether these categories correspond to independent criteria of behavior evaluation (hypotheses 2, 3, 5). Third, we verify whether there exists a preference relation on these categories (hypothesis 6).

The validated hypotheses will be a basis of the design of a new computational trust representation (see Section 5).

Along the way, we also verify whether the discovered criteria of behavior evaluation correspond to norms of behavior (hypothesis 4).

## 3.1. The Internet auction trace used in this study

The dataset used in this study has been acquired from www.allegro.pl which is a leading Eastern European online auction provider (over 70% market share in Poland). In this service, each auction has an explicit deadline and all current bids are exposed to all participants. Moreover, all information about all participants is accessible. In most auctions the bidders can specify a maximum price that they want to pay for an item and the proxy bid system automatically raises the bid, using only as much of the bid as is necessary to maintain the top position. Bidders can also increase their maximum price at any moment. When the auction terminates, the bidder with the highest bid wins. There are also multi-item (Buy now!)-type auctions in which sellers can sell more than one item (and hence there is more than one winner). In such an auction, every bid is a winning bid.

We have selected a subset of 9500 sellers and buyers, and their 285K auctions listed in 16K categories during 6 months. Our study has been performed on the subset of 1700K positive and 15K (about 0.9%) nonpositive feedbacks. The unequal amount of auctions and feedbacks is caused by the existence of multi-item auctions. The unequal amount of positive and non-positive reports is a typical feature in reputation systems for Internet auctions [8,13,19,20] and is caused partially by the design of the reputation system and by social phenomena like the spiral of hatred between reporting users [22].

## 3.2. Linguistic properties of reports

Our <sup>fi</sup>rst investigation concerns the amount of information contained in the textual comments. It is an attempt to validate hypothesis 1 by answering the basic question: do users include signi<sup>fi</sup>cant information in their comments that can be used as a basis for our reasoning? By signi<sup>fi</sup>- cant we mean information that can change the interpretation of the report that would be based just on the scalar rating.

Fig. 1 shows the result of a very simple experiment: for every user category (buyers and sellers) and every feedback type (negative, neutral and positive), distinctive text comments have been counted and compared with the number of all collected comments. For the sake of this experiment the strongest possible de<sup>fi</sup>nition of similarity was applied. Every string was compared character-by-character and only texts which have all characters identical were marked as non-distinctive. This experiment essentially identi<sup>fi</sup>es a copy–paste habit.

As can be observed in Fig. 1, all users of the auction house are more willing to devote time to write unique and informative comments when they have experienced harmful — either fraudulent (negative) or not perfectly honest (neutral) behavior. Due to the asymmetry of the positive and non-positive comments, virtually all users left only positive evaluations. Hence, they do not have any prepared sentences which they can re-use as an out-of-a-box comment. Thus, we can conclude that the high percentage of distinct texts for negative and neutral evaluations is an effect of a necessity rather than intentional choice. Positive comments are less informative than negative.

Most of the professional sellers who generate the vast majority of transactions in the eBay like auction houses have only one or two versions of positive comments and they re-use them for every non-negative auction. The most popular comment appears 33K times in our dataset (it is slightly less than 4% of all positive comments). Despite the unique buyers to unique sellers ratio, which is more than ten to one in the collected dataset, sellers are even less creative than buyers. Among the top 50 most popular comments left by buyers over 40 are constructed by combinations (with different order and punctuation) of only three words: “wszystko” (English “everything”), “ok” (English “ok”), “polecac” (English “recommend”).

Observations described in the previous paragraphs are further con-<sup>fi</sup>rmed by the data presented in Fig. 2. Firstly, the corpus of positive comments is characterized by a much lower vocabulary growth pace than the corpus of negative comments. Secondly, all types of comments written by buyers are more linguistically creative (thus informative) than comments written by sellers. Labels used in Fig. 2 are explained below:

• NegNeuForBuyers: negative and neutral comments left by sellers,

• NegNeuForSellers: negative and neutral comments left by buyers,

• PosForBuyers: positive comments left by sellers,

• PosForSellers: positive comments left by buyers,

![](/api/attachments/QSJ3CDTK/fulltext/images/f1bc046d6d9708d373b48f7384a8f2360ffa6adc6d2d958b4b8a74286af05e7a.jpg)  
Fig. 1. The percentage of the unique comments left by sellers and buyers in the auction house presented separately for the positive and neutral/negative evaluation.

We conclude that information added by users in positive feedbacks is systematic, but too simple to be considered a signi<sup>fi</sup>cant addition to the simple reputation system. On the other hand, information in nonpositive feedbacks is also systematically added, but is much more complex and can be considered a signi<sup>fi</sup>cant addition to the reputation system, since it is even possible for the comments to have a meaning which is contrary to the evaluation in the report.

## 3.3. Categories of negative and neutral reports

Existing reputation systems do not distinguish between different causes and hence kinds of negative or neutral user feedback. However if every nonpositive feedback is treated equally, then one cannot distinguish deliberate misbehavior from accidental misbehavior. For example, there is a great difference between sending the wrong color or size of a T-shirt with respect to not sending it at all.

In our previous research [10], we have mined the information from the users' comments using two independent classi<sup>fi</sup>cation rules for the buyers and for the sellers. We have partitioned all negative and neutral feedbacks into a detailed taxonomy of complaint types using regular expressions. These results validate hypothesis 2 of this paper.

Two approaches have been used to create the taxonomy: a top-down approach that relied on regular expressions, and a bottom-up approach that applied the Newman–Girvan algorithm for community detection [17] to cluster comments by content similarity. This approach is based on the measures of shortest path and betweenness centrality calculated for edges. The results of the two approaches have been merged, resulting in taxonomies (separate for comments about the seller and about the buyer) where each complaint type has its own meaning and also a unique set of regular expression patterns. The classi<sup>fi</sup>cation rules incorporated in our proposed taxonomy classify about 62% of non-positive feedbacks in our dataset. The remaining feedbacks usually contain too little information in order to be classi<sup>fi</sup>ed. This indicates a potential for improvement of the reputation system by enabling users a simple choice of multiple categories of behavior evaluation — a large number of users who do not include enough meaningful information in textual comments may <sup>fi</sup>nd such an interactive feedback system more appealing.

We have created a tree structure of complaints against buyers and sellers, similar to [6]. We have observed two types of harmful activity reported by auction users: user behavior related and item related.

The <sup>fi</sup>rst group includes the following user behavior:

• No response. Communications with the user after the auction was impossible. The user did not answer phone calls and did not respond to e-mails. The meaning of this behavior is equal for sellers and buyers.

• Odd behavior. The user behaved in a completely unpredictable manner, communication with the seller was possible but handicapped. If the user has the seller role, she has sent the item with a delay or has not de<sup>fi</sup>ned the payment method and shipping price. If the user is a buyer, she seemed not to follow the auction rules, or did not read the information provided by the seller. Sometimes a buyer even tries to force the seller to choose a particular payment method.

![](/api/attachments/QSJ3CDTK/fulltext/images/50f6900a4f7397740953951342c527d382a38d82c2456410abf68b5369f73678.jpg)  
Fig. 2. Vocabulary growth curve for four comment types.

• Delivery not accepted. The buyer did not accept the delivery which should be paid for by cash on delivery. The seller must pay the round trip shipping charges, which is sometimes a signi<sup>fi</sup>cant amount of money. This is the only type of complaint against the buyer related to loss of money.

• No intention to buy. The buyer did not pay for the item, and did not inform the seller about her plans. Sellers call such behavior childish or bidding for fun.

• Reneged on buying. The buyer contacts the seller and declares that she will not buy the item. From the seller side, the category ‘No product to sell’ is very similar to this behavior.

• Overpriced shipping or shill bidding. We consider only explicitly formulated accusations concerning shill bidding or shipping overcharge, not those computed from historical auction data. Such behavior is related only to the seller.

The second group of complaints is related strictly to the item (and thereby to the seller) and consists of:

• Item not sent or lost. The item was not sent to the recipient. Sometimes the seller argues that the item was lost by the courier or post of<sup>fi</sup>ce.

• No product to sell. The seller declares that the item was already sold to another buyer, or the item is no longer on sale. In this case the item is not sent to the buyer.

• Careless packing. The seller did not take care about the packaging of the items. This type also includes the situation when the received item was damaged. It is not possible to verify whether the seller has sent a damaged item or the item has been damaged during shipment.

• Wrong item. The seller made a mistake and sent a wrong item (wrong color or type) or the received item was not complete.

• Item not as expected. The item seems to be illegal goods (a fake, or a pirate copy of software) or just does not satisfy the buyer.

Notice that all of the described categories are related to speci<sup>fi</sup>c kinds of unfair behavior in the auction or transaction. Hence, the categories specify criteria for behavior evaluation, which validates hypothesis 3 of this article.

Moreover, the described varieties of behavior do not form a set of mutually exclusive possibilities: for example, an item may be wrong but carefully packed. (On the other hand, if the item is not sent or lost, then its packing cannot be evaluated.) Using our classi<sup>fi</sup>cation rules, over 33% of feedbacks have been classi<sup>fi</sup>ed into more than one category (and over 6% into more than two). Feedbacks that have been classi<sup>fi</sup>ed into multiple categories included textual comments that described various kinds of behavior. This indicates that the categories are related to independent criteria that can be used simultaneously by auction users and validates hypothesis 5.

The identi<sup>fi</sup>ed criteria for evaluating behavior are related to norms of procedural fairness in Internet auctions. These norms are of the form: “A seller must send an item after it has been paid for by the buyer who has won the auction”, or “A seller should pack the item carefully before shipment”. Notice that such norms can be expressed using modal logic that uses modality operators such as “must, should, can” and their negations. This observation validates hypothesis 4 of the paper.

## 4. Ranking the importance of report categories

We have proven that there exists a taxonomy of the categories of feedback related to non-positive forms of behavior of auction users. It is now possible to pose the question: do users attach the same importance to all categories of misbehavior? Or instead, does there exist some kind of relation that allows one to compare the importance of various misbehavior categories? In this section, we shall validate hypothesis 6 of the paper.

## 4.1. Automatic sentiment extraction

For the sentiment analysis task we have used a hybrid approach [3] which combines a dictionary containing 1580 positive and 1870 negative Polish words prepared by Zetema<sup>2</sup> and a shallow parsing engine called Spejd<sup>3</sup> which has been developed in the Institute of Computer Science Polish Academy of Science. Similar dictionaries to the one used in this research, but containing much more categories, can be also found for English and the most recognized is the General Inquirer [18]. To boost precision and address issues speci<sup>fi</sup>c to short, usergenerated comments a number of rules recognizing multiword opinion patterns and sentiment-modifying operators (e.g. “the only problem” or negations) have been crafted. Additionally, a diacrit guesser was added to cope with the careless manner of writing that is often used in the auction comments. In-depth veri<sup>fi</sup>cation of the sentiment extraction precision can be found in [22] but it is worth noting here that for a balanced set of positive and negative comments the reclassi<sup>fi</sup>cation precision exceeded 90% (in other words, using our sentiment analysis algorithm on Internet auction comments, it was possible to correctly classify the feedback value associated with the comment in over 90% of the cases).

## 4.2. Importance of report categories

The existence of a set of categories of reports that describe different forms of unfair behavior leads to a natural questions: can these categories be compared with each other? Do all categories describe equally harmful behavior?

A simple computational method can be used to rate the types of complaints along their harmfulness. The method is based on the percentages of negative and neutral comments in each complaint category. The balance between the negative and neutral comments serves as a measure of the harmfulness of this type of complaint.

In order to verify the correctness of this method, we have also conducted an opinion poll among real Internet auction users. We have received 208 responses from Internet auction users (between the ages of 19 and 59). 148 of the respondents have declared that they have sold goods on auction systems, and 193 of them declared that they have bought goods on auctions. This implies that a large number of the respondents have been both buyers and sellers. Respondents have been asked about their subjective opinion on the harmfulness of each complaint category.

In addition, we have included an evaluation of the emotional content of feedback description. All values for the computational and emotional methods have been generated from nonpositive (negative or neutral) feedbacks. We have juxtaposed the results from all three methods in Figs. 4 and 5 (for sellers and buyers respectively). The Figures show the harmfulness of behavior described by each complaint category as calculated by all three methods. The length of the bar indicates the position of the particular category in a ranking created by the particular evaluation method.

## 4.2.1. Activities of sellers

Results obtained from the opinion poll demonstrate that the more frequently used types of complaints are not necessarily the most harmful as considered by our respondents. Users seem to be more tolerant to lack of response from the seller or to a situation in which the seller declares after the auction that there is no item to sell. According to our respondents, the most harmful behaviors concern the condition of the item, such as sending a damaged, incomplete or different item — each of which essentially involve a loss of money, or a poorer value for money than expected.

From the emotional point of view, buyers are more irritated when there is a communication problem with the seller (odd behavior or lack of response). Buyers get more emotional when the seller declares that there is no product to sell, or the product is damaged.

## 4.2.2. Activities of buyers

From the seller's point of view, the most harmful behavior is related to the lack of response and lack of payment (no intention to buy). There is a minor disagreement between the computational method and the opinion poll. Odd behavior of the buyer is not a serious problem for the seller as long as the buyer still pays before receiving the item. Results from the emotional method show that most irritating behaviors are not accepting the delivery and lack of response. Both of these groups are again related to the loss of money. Lack of response is connected to the loss of time, which (in case of the e-market) is very closely connected to the loss of money.

Basing on the three harmfulness rankings of the report categories, it is possible to create an assignment of the categories to importance classes (the more harmful categories should be considered the more important). The problem here is that each of the methods has certain advantages and drawbacks:

• the balance of neutral and negative reports is based on a large amount of declarative information. Yet, this method by itself is not enough to compare all categories conclusively. The differences between the amounts of neutral and negative reports are sometimes not suf<sup>fi</sup>ciently large. Moreover, the difference between the signi<sup>fi</sup>- cance of a neutral and negative report is not very large.

• the analysis of emotional content is based on a similar amount of information than the previous method and adds a clear interpretation to the reports in different categories. Yet, the computation of emotional content may be biased by some error in the method of evaluating emotional content. Moreover, even if the method is completely correct, the emotional reaction of users to some reported forms of behavior may not be the right way to evaluate the harmfulness of this behavior (for example, the “Odd behavior” category causes a strong emotional reaction, but is not necessarily very harmful.)

• the results of the opinion poll have the advantage that respondents have been asked to compare categories of behavior directly with respect to harmfulness. However, the obtained sample is much smaller than the amount of data used by the previous two methods. Moreover, the respondents were usually both buyers and sellers on the Internet auction; the survey lacks responses from auction users that are only sellers. Therefore, it is hard to use the survey results for comparing the harmfulness of buyer behavior.

When all evaluation methods are considered jointly (which is possible for categories of reports about sellers), the problem is that the resulting evaluations are sometimes strongly con<sup>fl</sup>icting (as for the “No response” or “Odd behavior” categories). A mechanism is required that can reconcile and combine the rankings from the three methods into one, joint ranking of the harmfulness of report categories.

Let us assume that there are 5 importance classes, least important, less important, important, more important and most important. The problem of assigning the report categories to importance classes basing on the three different rankings is really a problem of merging social valuations. The computational methods of the theory of equitable optimality can be used for such a problem; notably, the Ordered Weighted Averaging (OWA) and Weighted OWA (WOWA) methods are particularly suitable [24]. The WOWA method uses two sets of weights: the priority (or entitlement) weights that are assigned to individual criteria (or agents' outcomes), and the OWA weights that are assigned to the ordered criteria. Consider a WOWA aggregation of the three rankings that will have the following priority weights: $v _ { c } = 2$ $\nu _ { e } = 1$ , and $\scriptstyle v _ { o } = 1$ , where $\nu _ { c }$ is the weight of the computational ranking, $\nu _ { e }$ is the weight of the emotional ranking and $\boldsymbol { v } _ { o }$ is the weight of the opinion poll. This means that the computational method can be counted double, because it is based on the largest set of declarative responses (the emotional method is computed from the contents of the comments, and is therefore not declarative, and the opinion poll is based on a smaller set of responses). This can be achieved by simply cloning the computational ranking, so as a result we obtain 4 rankings where the computational ranking is repeated. For these 4 rankings, we can specify a set of OWA weights: $w _ { 4 } = 0 . 5 , w _ { 3 } = 0 . 2 5 , w _ { 2 } = 0 . 2 5$ and $w _ { 1 } = 0 ,$ , where w is the weight of the ith worst position in the four rankings. This set of weights can be interpreted as follows: we consider only the three best positions in the four rankings, and the <sup>fi</sup>rst position is twice as important as the second and third. If the best position is from the computational ranking, it will occur twice in this computation because the ranking is repeated.

![](/api/attachments/QSJ3CDTK/fulltext/images/c6af67420ad3d9bab380f25c52604f0c03926df1dc9c996c4e75790a7157dcc2.jpg)  
Fig. 3. Typology of complaints against seller.

This method produces a joint ranking for the report categories. The construction of this synthetic ranking does not imply that we consider it the best ranking for all users. However, our results support the conclusion that for a majority of users, report categories are not equally important, which validates hypothesis 6. The importance relation on categories may be different for various users, but in a practical application, it is possible to allow each user to change the default importance ranking of categories to express her preferences.

![](/api/attachments/QSJ3CDTK/fulltext/images/f9a29ec44f53b48d3f6d58c6861739f96c29072b66be950c7d971f34224094aa.jpg)  
Fig. 4. Harmfulness grading of sellers' activities. Results on a scale from 0 (least harmful) to 8 (most harmful).

The joint ranking can be partitioned into <sup>fi</sup>ve classes using threshold values that are selected so that all <sup>fi</sup>ve importance classes will be used to compare the report categories. Using this method and the previously mentioned weights, we obtain the following assignment of categories of reports about sellers (Table 1).

This assignment will be used in the next section in order to design a method of comparing reports that takes into account their importance.

Notice that if we express norms for procedurally fair behavior in auctions using modal logic, we can incorporate the importance ranking using various degrees of modality operators. For example, the assignment of norms into importance classes may be accomplished by using <sup>fi</sup>ve modality operators (or their negations): “can”, “should”, “SHOULD”, “must” and “MUST”, corresponding to the least important, less important, important, more important and most important classes respectively. This new conclusion shows that the norms postulated by hypothesis 4 can also express relative importance.

![](/api/attachments/QSJ3CDTK/fulltext/images/1b7882074dda2a2a1097ee36757aa8cf91e0101b61ac11072fc44ebbfeae6ddb.jpg)  
Fig. 5. Harmfulness grading of buyers' activities

## 5. A new computational trust management system for internet auctions

In this section, we <sup>fi</sup>rst outline the computational trust representation proposed in this paper. Next, we describe the design of a computational trust management system (the term reputation system does not apply well to our design, because we do not explicitly calculate a reputation value. In the new system, rankings of sellers can be created without calculating a value that can be interpreted as reputation).

## 5.1. New computational trust representation

The computational trust representation proposed in this paper attempts to take into account the information about user behavior gained through the analysis of Internet auction traces. We shall refer to such information as a proof. In Internet auctions, proofs are in the form of reports about the behavior of an agent (seller or buyer). The proposed computational trust representation then consists of a de<sup>fi</sup>nition of proof and of operators for processing proofs in order to propagate computational trust.

A proof can be de<sup>fi</sup>ned as follows:

$$
p ^ {A B} = \left\{c, \{l _ {i}, s _ {i} \} _ {i = 1} ^ {m} \right\}
$$

where A and B are agents: A is the trustor and B is the trustee; c is the proof context. In Internet auctions, contexts can be the categories of products, the price ranges, and the role of the user (buyer or seller).

l is a set of labels that are used to describe the behavior of a user. m is the number of labels. One can think of the labels as criteria used to evaluate behavior. Using multiple criteria in the proofs is justi<sup>fi</sup>ed by the positive validation of hypothesis 3. A concrete list of criteria can be determined from the comment categories proposed in Section 3.3.

As stated by the validated hypothesis 6, there exists a preference relation that represents the “degree of importance” of criteria (in the case of non-positive reports, the degree of importance can be identi-<sup>fi</sup>ed with the harmfulness of the reported behavior), as indicated by our analysis. We shall denote this by $l _ { i } \prec l _ { j } ,$ , whenever l is considered as more important than l by the trustor.

Each proof includes also for each label a related strength value, $s _ { i \cdot }$

Contrary to the work of Yager and Sabater-Mir (where label strengths are interpreted as the degree to which the label applies to the agent), in our system the strength represents an evaluation of the trustee's behavior with respect to the criterion represented by the label (this approach is similar to DSR). This approach is justi<sup>fi</sup>ed by a validation of hypothesis 5 which states that the criteria used for behavior evaluation are independent, and hence the strengths in our proof need not to add up to 1, as proposed by Yager and Sabater-Mir.

Initial strength values should be on an intuitive scale that is easy to use by buyers and sellers on Internet auctions. For example, an integer scale of $0 , 1 , . . . , 5$ can be used, where a higher value is interpreted as a better behavior with respect to this criterion. However, strengths can later be aggregated by the trust management system (for example, using an average), so that it can be assumed that strengths will be real numbers in the range of [0,5].

Assignment of report categories to importance classes basing on WOWA aggregation of rankings.

<table><tr><td>Report category</td><td>Importance class</td></tr><tr><td>No response</td><td>Most important</td></tr><tr><td>Item not sent or lost</td><td>Most important</td></tr><tr><td>Careless packaging</td><td>More important</td></tr><tr><td>No product to sell</td><td>Important</td></tr><tr><td>Overpriced shipping</td><td>Less important</td></tr><tr><td>Item wrong</td><td>Less important</td></tr><tr><td>Item not as expected</td><td>Least important</td></tr><tr><td>Odd behavior</td><td>Least important</td></tr></table>

We have shown that the proposed proof structure is well supported by the actual use of Internet reputation systems, as revealed by our analysis of available traces. Now we turn to the validation of hypothesis 7 of the paper by considering a question: is it possible to design a practical Trust Management system for Internet auctions that uses the proposed new trust representation?

## 5.2. New proof processing operators

A trust management system should be capable of utilizing the above discussed proofs to make a more reliable trust recommendation about any speci<sup>fi</sup>c agent for a potential interaction/transaction. For example, consider a buyer who has never before bought from a certain seller on an Internet auction. The trust management system should produce a recommendation for that buyer that is based on available proofs. Current reputation systems on Internet auctions use a simple average of scores given in available reports.

Based on such information, a trust management system can produce a ranking of agents. For example, consider a buyer who has searched for products and found a set of sellers that offer similar products in comparable price ranges. The buyer wants to rank theses sellers according to their computational trust measures. In a simple reputation system, these sellers would be sorted using the reputation value.

Following the work of [7], we shall de<sup>fi</sup>ne two operators that are suf<sup>fi</sup>cient to implement simple to sophisticated algorithms that ful<sup>fi</sup>ll the requirements described above. These operators are: the aggregation operator oplus and the selection operator ⊲. Both operators are applied to a set of proofs, $p _ { i } ^ { A B }$ . Before formally introducing these operators, let us discuss what should be their desirable properties.

The aggregation operator should return a single proof that represents a summary of the information available in a set of proofs. Usually it is applied to summarize the proofs available from different agents about a single trustee B or even for a single relation between a trustor A and trustee B. In a simple reputation system, where reports are on a scale of −1,0,1, the aggregation operator could return a ratio of nonnegative reports (0,1) to all reports. Using the proposed new computational trust representation, the aggregation operator will have to be more complex. Since the aggregation operator produces a single proof, the job is to create the new strengths for that proof. The <sup>fi</sup>rst possibility is to calculate average values for each label l from the strengths of that label in the aggregated set of proofs. However, as more proofs will be aggregated, this algorithm would converge to the average of strengths used for each label by the entire population of agents. Also, experience with the DSR system shows that users tend to utilize only a very narrow range of the values on the scale (typical ratings in DSR are between 4 and 5 stars) [2]. In order to increase the sensitivity of the system to such small changes in ratings, it may be desirable to allow the more extreme opinions to have more impact on the result. This approach is consistent with <sup>fi</sup>ndings that the more extreme opinions are more useful for a correct recommendation based on computational trust [5].

The job of the selection operator is to choose the most relevant proofs from a set of proofs. Usually it is applied to select a single proof from a set of aggregated proofs about various trustees. This operation can be applied iteratively to produce a ranking of trustees. Also, the selection operator can be applied before aggregation, in order to select the more extreme opinions. Such a selection has been shown to improve the quality of trust recommendation [5]. The reason for this is that excluding less relevant proofs reduces the noise of the trust recommendation. A simple way of judging relevance is based on the strengths of opinions. Proofs with extremely high or low strengths should be preferred. In a simple reputation system, the selection operator could just return reports that have values of 1 and 1, ignoring the neutral values.

In our system, the selection operator can return proofs that are weakly Pareto-optimal with respect to scaled strengths (in other words, the selection operator will not include a proof if it has all strengths less or equal than another proof in the set, and one inequality is strict: it is weakly Pareto-dominated by another proof), where the scaling function should take into account the mean strength value for each label. Selecting Pareto-optimal proofs will return the most positive opinions; this process can be repeated using negated criteria, so that the most negative opinions will be selected, as well. The number of selected proofs should be a parameter. Last but not least, the selection should take into account the preference relation that establishes the relative importance of labels.

Transitive trust propagation cannot be applied in Internet auctions because the buyer and seller roles are asymmetric, and information about the credibility trust in other buyers' opinions is not available. Hence, we do not include a composition operator (postulated in [7] in order to enable transitive trust propagation) in our system.

## 5.3. Aggregation operator

The aggregation operator can be de<sup>fi</sup>ned as follows. Let

$$
p _ {\text { agg }} ^ {A B} = \oplus \left(p ^ {X _ {1} B}, \dots , p ^ {X _ {n} B}\right)
$$

where $p _ { \mathrm { a g g } } ^ { A B } = \{ c , \{ l _ { i } , s _ { i } ^ { \mathrm { a g g } } \} \}$ and $p ^ { X _ { j } B } = \{ c , \{ l _ { i } , s _ { i } ^ { j } \}$ for all j.

<sup>¼ g</sup>The trust management system should record the empirical distribution of strengths used for each label. This empirical distribution can be used to determine the average user valuations for each label, denoted by ${ \overline { { s } } } _ { i } .$ Other important values are the maximum and minimum strength values used for this label: $s _ { i } ^ { m a x }$ and $s _ { i } ^ { m i n }$

The new strengths of the aggregated proof are given by:

$$
s _ {i} ^ {\text { agg }} = \frac {1}{n} \sum_ {k = 1} ^ {n} \mu \left(s _ {i} ^ {j}\right).
$$

The function μ is designed to increase the impact of extreme values on strength of the aggregated proof. This can be achieved by the following function shape. Let $\delta = \overline { { { s } } } _ { i } - s _ { i } ^ { j }$ and $\delta _ { i } ^ { m a x } = ( s _ { i } ^ { m a x } - s _ { i } ^ { m i n } ) / 2 .$ . Then, let

$$
\mu \left(s _ {i} ^ {j}\right) = s _ {i} ^ {j} - \delta^ {3} / \left(\delta_ {i} ^ {\text { max }}\right) ^ {2}.
$$

The proposed aggregated strength may, in extreme cases, be outside of the range [0,5]. In such a case, the aggregated strength may be cut off to 0 or 5. However, note that the selection operator does not require that the strength should be in this range.

## 5.4. Selection operator

The selection operator can be de<sup>fi</sup>ned as follows. Let

$$
p ^ {A Y _ {s e l}} = \triangleleft \left(p ^ {A Y _ {1}}, \dots , p ^ {A Y _ {n}}\right).
$$

The selection of proofs can be done using a real-valued scaling function that should be maximized. Therefore, $p ^ { A Y _ { s e l } }$ is determined by choosing the proof $p ^ { A Y _ { k } }$ that maximizes this scaling function, denoted by $\bar { \sigma ( p ^ { A Y _ { k } } ) }$ . This function, on the other hand, will use scaling functions that operate on the strength values for any label. The scaling function (maximized) on proofs can be de<sup>fi</sup>ned as follows:

$$
\sigma \left(p ^ {A Y _ {k}}\right) = \min _ {i} \left\{\sigma_ {i} \left(s _ {i} ^ {k}\right) \right\} + \epsilon / m \sum_ {i = 1} ^ {m} \sigma_ {i} \left(s _ {i} ^ {k}\right)
$$

where $p ^ { A Y _ { k } } = \Big \{ c , \Big \{ l _ { i } , s _ { i } ^ { k } \Big \}$ for all k.

The scaling function of strengths is based on the partial achievement function of the reference-point approach to multi-criteria optimization [23]. This approach guarantees the selection of Pareto-optimal proofs (or aggregated proofs, if aggregation for each seller is applied <sup>fi</sup>rst).

The values of the scaling function can be interpreted as satisfaction levels for criteria (strength) values. The scaling function is piecewise linear, but changes its slope at two special points (strength values). These are the so-called reservation $( s _ { i } ^ { r } )$ and aspiration (s<sup>a</sup>) points. These points can be determined from the empirical distribution of strength values, as follows: $s _ { i } ^ { r } = \overline { { s } } _ { i } / 2$ and $s _ { i } ^ { a } = ( 5 + \overline { { s } } _ { i } ) / 2$ , for each label l<sub>i</sub>.

The scaling function of strengths is given by:

$$
\sigma_ {i} (s _ {i}) = \left\{ \begin{array}{l l} \alpha s _ {i} / s _ {i} ^ {r}, & \text { for } s _ {i} \leq s _ {i} ^ {r} \\ \alpha + 2 / 5 (\beta - \alpha) (s _ {i} - s _ {i} ^ {r}), & \text { for } s _ {i} ^ {r} \leq s _ {i} \leq s _ {i} ^ {a} \\ \beta + (5 - \beta) \frac {s _ {i} - s _ {i} ^ {a}}{5 - s _ {i} ^ {a}} & \text { for } s _ {i} ^ {a} \leq s _ {i} \end{array} \right..\tag{1}
$$

The parameters α and $\beta$ of the scaling function are the values of the scaling function at the reservation and aspiration points, respectively. For example, $\alpha { = } \sigma _ { i } ( s _ { i } ^ { r } ) { = } 2$ and $\beta = \sigma _ { i } ( s _ { i } ^ { a } ) = 4 .$ . These values will be varied for various labels $l _ { i }$ in order to take into account the preference structure on the importance of labels.

The preference structure on the labels can be used to classify them into importance classes. Let us assume that there are 5 importance classes, least important, less important, important, more important and most important. The parameters of the scaling function should change so that it returns smaller values for the more important labels. This can be formalized as follows:

$$
l _ {i} \prec l _ {j} \Rightarrow \sigma_ {i} (x) > \sigma_ {i} (x), x \in [ 0, 5 ].
$$

The rationale for such a design is as follows: if a label is least important, then the agent should be satis<sup>fi</sup>ed if the value of the strength of that label is only at its lower reservation level. On the other hand, if another label is most important, then the agent will have a similar level of satisfaction as for the least important one only if the strength for that label is at its higher aspiration level. As reservation and aspiration levels depend on the distribution of strengths for a label, this reasoning is valid even if different labels have different strength distributions.

Basing on [23], the following values of the parameters of the scaling function for various importance classes of labels have been proposed in Table 2. Fig. 6 shows the shape of scaling functions for various importance classes of labels. As intended, the values of the scaling function are smallest for labels of highest importance.

The design of the new trust management system presented in this section demonstrates that it is possible to effectively utilize the rich information available in our proposed new computational trust representation. This validates hypothesis 7. In the next section, we present a simple comparison of the new trust management system with eBay's DSR system. The comparison also serves as an initial analysis of the sensitivity of the proposed system to changes in criteria importance or to small changes in the initial report values.

Parameter values for scaling function depending on importance class of the label.

<table><tr><td>Importance class</td><td>Least imp.</td><td>Less imp.</td><td>Important</td><td>More imp.</td><td>Most imp.</td></tr><tr><td>α (value of scaling function at reservation level)</td><td>3</td><td>2.5</td><td>2</td><td>1.5</td><td>1</td></tr><tr><td>β (value of scaling function at aspiration level)</td><td>5</td><td>4.5</td><td>4</td><td>3.5</td><td>3</td></tr></table>

![](/api/attachments/QSJ3CDTK/fulltext/images/b9a57d78f1520c3365f1363b02bf9584d3338911b3f143771a0e18969920550d.jpg)  
Fig. 6. Shape of scaling functions for labels of various importance.

## 6. A comparison with eBay's DSR scale

The Detailed Seller Rating is a new system introduced by eBay for buyers to rate sellers using 4 different criteria:

• product description accuracy

• communication between seller and buyer

• shipping time

• shipping charge.

Buyers can leave one to <sup>fi</sup>ve stars for each criterion. The DSR system could therefore be expressed using the computational trust representation proposed in this paper for Internet auctions. However, we propose to use a different list of criteria. The DSR criteria have been marked in Fig. 3 with stars near the complaint type. In comparison to our model, the criteria used by DSR cover most of the user-related problems but do not take into consideration item-related complaints (only one criterion concerns the item description). Moreover, DSR does not introduce a context for the report, like the price range or product category.

Since the system has been designed to be simple to use, eBay does not instruct buyers on how to use DSR. This results in misunderstandings of the proposed rating scale. Also, eBay expects very high average rating results for all criteria for sellers. Therefore, when a buyer submits a report that has a valuation of four stars on some scale, she may think that the report represents a positive feedback; however, to the seller the report is really negative, because the expected averages for higher seller status are above 4. Moreover, there exist concerns that the introduction of the DSR system together with the new status hierarchy for sellers can have an adverse affect on low-volume sellers [8] that have usually lower feedback averages.

Another, more signi<sup>fi</sup>cant difference lies in the processing of the reports. eBay does not compute any value beyond the simple averages of received reports for each criterion (and the number of reports. A report that contains valuations for only a subset of the criteria is counted only for these criteria). This means that buyers who want to compare sellers based on the DSR criteria must compare vectors of values together with information on the number of reports for each value. This is a complex task for an ordinary auction user. In contrast, using our proposed system, it is possible to create rankings of sellers (using the selection operator).

The DSR system is also unable to take into consideration a preference relation of the buyers on the proposed criteria. All four DSR criteria are considered as equally important. On the other hand, our system takes into account such a preference relation and allows the auction user to specify his own subjective preferences on the criteria.

In order to compare the new proposed reputation system to DSR, we have performed the following experiment. Consider three sellers who are evaluated using reports as proposed in our new system. There are three labels used by these reports: $L _ { 1 } , L _ { 2 }$ and $L _ { 3 } .$ We have simulated the comparison of the three sellers using a simple average of label strengths (such as in DSR) and using our system (in this simulation, the proof available for each seller can be thought of as the aggregated proof. The selection operator will be applied to create a ranking of sellers based on aggregated proofs). The results are presented in Tables 3, 4, and 5.

Table 3 shows a scenario where $L _ { 2 }$ is considered “most important”, while label $L _ { 1 }$ and $L _ { 3 }$ are considered “least important”. The table shows the average values of report strengths received by each seller for each label. The strengths of reports for label L are lower than for the other labels in this scenario. The table also shows the rank received if a simple average (DSR) is used to compare the sellers, and the rank received by using the new selection operator. Table 4 shows, for the same reports as in the scenario shown in Table 3, the effect of changing the importance of labels. In the scenario shown in Table 4 L is still most important, but $L _ { 1 }$ is “more important” than L . The effect is a reversal of the rankings for the two top sellers.

Table 5 shows a scenario where the importance of labels is similar as in the scenario shown in Table 4, but the distribution of label strengths is more “DSR-like”: the majority of reports include very positive opinions. This scenario shows that even for subtle differences in label strengths, our aggregation and selection operators are able to rank sellers taking into account the importance structure of the labels. Such a ranking in turn makes the decision making for end users much easier. This observation also justifies the design of our aggregation operator.

## 7. Related work

The question of adequate computational representation of trust has been frequently considered in the literature on trust management; yet, previous works lacked a way of evaluating the simpler trust representations, and have therefore opted for simplicity or introduced reputation measures designed to support specialized algorithms [1,14,15]. Another reason for this choice is that the consequences of introducing a new computational trust representation for the TM system are not simple. A simple representation makes it easier to develop meaningful algorithms for processing trust. One of the most important types of algorithm used by a TM system is the trust propagation algorithm. A simple representation of trust makes it easy to compute a propagated trust value (for example, using multiplicative trust propagation). Therefore, in order to answer our question constructively, in this paper we have not only proposed a suitable trust representation, but also de<sup>fi</sup>ned how the new computational trust could be processed by the TM system.

Much related work has been devoted to an analysis of eBay's reputation system [8,13,19,20]. This work has usually focused on an evaluation of the effectiveness of the erstwhile reputation system used by eBay. However, the question of whether this simple reputation system is suf<sup>fi</sup>cient to express all information conveyed by users has not been considered in detail before.

In particular, the work of Bolton, Greiner and Ockenfels [2] studies the design of the DSR in detail, using experimental methods (a specially designed game played by about 200 users who tested two different designs of DSR). However, their work focuses on the question of whether feedback in DSR should be blind or asymmetric (given only by buyers about sellers). Our work complements this research by focusing on the question of what is an appropriate computational trust representation for DSR.

The work of Gavish and Gucci [4] contains an attempt to create a taxonomy of comments that is based on a dataset from eBay. The taxonomy in this work has been constructed manually, while we have used the Newman–Girvan algorithm (bottom-up classi<sup>fi</sup>cation) together with manual (top-down) classi<sup>fi</sup>cation that has created regular expressions for each category.

Table 3  
L — most important, $L _ { 1 }$ and $L _ { 3 } \ \cdot$ — least important.

<table><tr><td rowspan="2">Seller</td><td colspan="3">Proof</td><td colspan="2">DSR</td><td colspan="2">Operator</td></tr><tr><td> $L_1$ </td><td> $L_2$ </td><td> $L_3$ </td><td>Average</td><td>Rank</td><td>Scaling function</td><td>Rank</td></tr><tr><td>S1</td><td>4,69</td><td>2,65</td><td>4,80</td><td>4,05</td><td>1</td><td>3,56</td><td>2</td></tr><tr><td>S2</td><td>2,46</td><td>4,85</td><td>1,79</td><td>3,03</td><td>3</td><td>4,76</td><td>1</td></tr><tr><td>S3</td><td>4,86</td><td>1,43</td><td>4,62</td><td>3,64</td><td>2</td><td>2,57</td><td>3</td></tr></table>

Table 4  
L<sub>2</sub> — most important, $L _ { 1 }$ — more important, $L _ { 3 } \mathrm { ~ - ~ }$ important.

<table><tr><td rowspan="2">Seller</td><td colspan="3">Proof</td><td colspan="2">DSR</td><td colspan="2">Operator</td></tr><tr><td> $L_1$ </td><td> $L_2$ </td><td> $L_3$ </td><td>Average</td><td>Rank</td><td>Scaling function</td><td>Rank</td></tr><tr><td>S1</td><td>4,69</td><td>2,65</td><td>4,80</td><td>4,05</td><td>1</td><td>3,51</td><td>1</td></tr><tr><td>S2</td><td>2,46</td><td>4,85</td><td>1,79</td><td>3,03</td><td>3</td><td>3,35</td><td>2</td></tr><tr><td>S3</td><td>4,86</td><td>1,43</td><td>4,62</td><td>3,64</td><td>2</td><td>2,52</td><td>3</td></tr></table>

The proposed computational trust representation is inspired by the work of Yager [25,26] and resembles the representation used by Sabater-Mir et al. [21]. However, the processing of the representations by the proposed operators is signi<sup>fi</sup>cantly different due to a fundamentally different interpretation of the values. First, the labels used in the representation are interpreted by Yager and Sabater-Mir as exclusive alternatives that are comparable by a total order (even though the representation makes it possible to specify non-zero strengths for various labels. Still, the labels without strengths can only be interpreted as exclusive alternatives). In the representation proposed in this paper, labels are interpreted as criteria for the description of behavior. These criteria are not mutually exclusive. In addition, there exists a preference relation that describes the importance of the criteria to users.

Consequently, Yager proposed a completely different treatment of opinions represented by his system. First, the strengths used by Yager are normalized so they add up to 1 for the different labels. Such a normalization makes sense for exclusive alternatives, but not for non-exclusive criteria. Furthermore, Yager's aggregation operator is based on strength multiplication and is not similar to the aggregation operator as proposed here. This is motivated by the fact that a ‘unit’ opinion in Yager's system is an opinion that has equal strengths for all labels. Such an opinion should not change the aggregated result. In our system, a unit opinion does not exist, but the aggregation operator ensures that opinions that have strengths far from the mean will have a larger impact on the aggregated proof.

Sabater-Mir introduces additionally a con<sup>fi</sup>dence measure (called “strength of belief in the representation of trust about an agent”). This con<sup>fi</sup>dence measure is really a measure of trust in the context of credibility of opinions received from another agent. The con<sup>fi</sup>dence measure is therefore used in a form of transitive trust propagation that combines credibility trust with a trust rating in another context. However, since Sabater-Mir does not explicitly identify contexts, the con<sup>fi</sup>dence measure is added to every credibility rating. A composition operator could be used instead that would explicitly calculate transitively propagated trust in the context of opinion credibility. However, in Internet auctions, such transitive propagation is not useful, and therefore we have not included such an operator or a con<sup>fi</sup>- dence measure in our system.

Another difference to the work of Sabater-Mir is the introduction of the selection operator. This operator can be used to create rankings of agents or to reduce the amount of noise in the aggregation by selecting the most extreme opinions to be aggregated (ignoring the others). An important feature of our selection operator is that it selects weakly Pareto-optimal proofs from the available set of proofs. This property is a consequence of our computational trust representation that utilizes multiple criteria to describe behavior.

Table 5  
L — most important, $L _ { 1 } \cdot$ — more important, $L _ { 3 } \mathrm { ~ - ~ }$ important.

<table><tr><td rowspan="2">Seller</td><td colspan="3">Proof</td><td colspan="2">DSR</td><td colspan="2">Operator</td></tr><tr><td> $L_1$ </td><td> $L_2$ </td><td> $L_3$ </td><td>Average</td><td>Rank</td><td>Scaling function</td><td>Rank</td></tr><tr><td>S1</td><td>4,69</td><td>4,40</td><td>4,80</td><td>4,63</td><td>1</td><td>4,67</td><td>1</td></tr><tr><td>S2</td><td>3,95</td><td>4,85</td><td>3,92</td><td>4,24</td><td>3</td><td>4,62</td><td>2</td></tr><tr><td>S3</td><td>4,91</td><td>3,96</td><td>4,62</td><td>4,50</td><td>2</td><td>4,19</td><td>3</td></tr></table>

## 8. Conclusions

We have formulated and validated several hypotheses regarding the evaluation and expression of trust by users of simple reputation systems for Internet auctions. Some of these hypotheses have a theoretical signi<sup>fi</sup>cance. However, the main contribution of this article is the proposal of a new computational trust management system for Internet auctions that generalizes and extends the DSR reputation system used currently by major Internet auction providers. The proposed system is based on the validated hypothesis and at the same time is a proof that the discovered additional information provided by users in simple reputation systems can be constructively used to build a more sophisticated system.

In order to summarize the contributions of this article, we repeat the listing of the validated hypotheses:

1. Users systematically add signi<sup>fi</sup>cant information in non-positive feedbacks in reputation systems for Internet auctions.

2. The non-positive feedbacks can be categorized into a taxonomy.

3. Each of the leaf categories speci<sup>fi</sup>es a criterion for behavior evaluation.

4. Each of the leaf categories is related to a norm of behavior.

5. The criteria of behavior evaluation speci<sup>fi</sup>ed by non-positive feedback categories can be used independently.

6. The criteria for behavior evaluation speci<sup>fi</sup>ed by non-positive feedback categories are not equally important to users.

7. It is possible design a reputation system so that it takes into account more criteria of behavior evaluation and ranks sellers taking into account criteria importance.

The investigation of linguistic richness of comments in Section 3.2 leads to the conclusion that hypothesis 1 holds for non-positive feedbacks, but does not hold for positive feedbacks. The analysis of categories of non-positive comments in Section 3.3 demonstrates that hypotheses 2 and 3 are valid. Internet auction users express detailed information about the non-positive (harmful) behavior of their transaction partners. This information can be organized into a taxonomy of categories.

Each of the categories constitutes a speci<sup>fi</sup>c criterion for evaluating the behavior of a transaction partner. This observation validates hypothesis 3 and is the basis of the design of our TM system that uses a multicriteria approach to rank sellers (by selecting Pareto-optimal aggregated proofs).

Further observation of the taxonomy of non-positive comments leads to the conclusion that these criteria are independent (two or more criteria can be used independently to describe behavior). This observation validates hypothesis 5 and is the justi<sup>fi</sup>cation for our design of the new TM system that does not follow the design of Yager (where label strengths were not independent, because they added to 1).

The observation that each of the discovered categories of nonpositive reports is related to a different norm of behavior validates hypothesis 4, which has a theoretical signi<sup>fi</sup>cance as it gives empirical support to the notion that trust is an expectation of conformance to a set of norms dictated by the social context [24]. This notion of trust can be easily operationalized and is different from trust as an expectation of competence or goodwill. The notion of normative trust also generalizes the concept of trust in the situation of indirect reciprocity (by using the reciprocity norm).

One of the most signi<sup>fi</sup>cant contributions of this paper is, in our view, the validation of hypothesis 6. The criteria for behavior evaluation speci-<sup>fi</sup>ed by categories of nonpositive reports used by Internet auction buyers and sellers concern behavior that has differing degrees of harmfulness. The harmfulness of a behavior is partially indicated by the use of negative or neutral reports. The emotional content of nonpositive comments varies strongly among the different report categories. Even if it is hard or impossible to create one ranking of criteria harmfulness that <sup>fi</sup>ts all users, this does not mean that users are indifferent to the relative importance of criteria.

A proposal of a TM system cannot just specify a new format for expressing user reports. These reports must be meaningfully processed by the TM system, usually with the goal of creating a ranking of most (or least) trusted users. We have shown that it is possible to define operators that process the proposed new reports in order to create rankings. Moreover, we have demonstrated how these rankings can take into account the importance of criteria for behavior evaluation. These <sup>fi</sup>ndings validate the hypothesis 7 of this work. The proposed new trust management system can provide users with a default ranking of criteria harmfulness or importance, but can also allow each user to change the importance ranking to re<sup>fl</sup>ect his individual preference. The importance ranking is then used to create a speci<sup>fi</sup>c ranking of sellers. This feature extends the capabilities of DSR.

The design of the TM system described in this paper has been based entirely on the observable behavior of users that we have studied from Internet auction traces. The new TM system addresses user needs by allowing them to use criteria that are meaningful and important in evaluating behavior, and by taking into account the relative importance of these criteria. Moreover, the new system generalizes the DSR system used by eBay by enlarging the set of used criteria and taking into account criteria importance.

In the evaluation of the proposed TM system, we have been mostly concerned with checking whether the system would be suf<sup>fi</sup>ciently sensitive to the relative importance of the evaluation criteria. In a simple experiment, we have shown how changing the importance of labels changes the ranking of sellers in an expected manner. This experiment con<sup>fi</sup>rms that the proposed selection operator has the desired properties. Our future work will aim to conduct a detailed evaluation of the proposed trust management system on a new dataset from a reputation system that uses DSR.

## References

[1] Sulin Ba, Andrew B. Whinston, Han Zhang, Building trust in online auction markets through an economic incentive mechanism, Decision Support Systems 35 (2003) 273-286

[2] Gary E. Bolton, Ben Greiner, Axel Ockenfels, Engineering trust — reciprocity in the production of reputation information, in: UNSW Australian School of Business Research Paper, No. 2009 ECON 02, 2009.

[3] Aleksander Buczyñski, Aleksander Wawer, Shallow parsing in sentiment analysis of product reviews, in: Proceedings of the Partial Parsing workshop at LREC 2008, 2008, pp. 14–18.

[4] B. Gavish, C.L. Tucci, Reducing internet auction fraud, Communications of the ACM 51 (5) (2008) 89–97.

[5] Jennifer Golbeck. Computing and Applying Trust in Web-based Social Networks. PhD thesis, University of Maryland, 2005.

[6] Dawn G. Gregg, Judy E. Scott, A typology of complaints about ebay sellers, Communications of the ACM 51 (4) (2008) 69–74.

[7] Chung-Wei Hang, Yonghong Wang, Operators for propagating trust and their evaluation in social networks, in: Proceedings of the 8th International Joint Conference on Autonomous Agents and Multiagent Systems, 2009.

[8] Daniel Houser, John Wooders, Reputation in internet auctions: theory and evidence from ebay, Technical report, University of Arizona, 2001.

[9] Audun Josang, Roslan Ismail, The beta reputation system, in: Proceedings of the 15th Bled Electronic Commerce Conference, 2002.

[10] Tomasz Kaszuba, Albert Hupa, Adam Wierzbicki, Comment classi<sup>fi</sup>cation for internet auction platforms, in: Associated Workshops and Doctoral Consortium of the 13th East European Conference, ADBIS 2009, Riga, Lativia, September 7–10, 2009, Revised Selected Papers, volume Information Systems and Applications incl Internet/Web and HCI, Vol. 5968 of Lecture Notes in Computer ScienceSpringer-Verlag, 2010.

[11] Stephen Paul Marsh. Formalising trust as a computational concept. PhD thesis University of Stirling, April 1994.

[12] Paolo Massa, Downloaded epinions dataset, 2003.

[13] Mikhail I. Melnik, James Alm, Does a seller's ecommerce reputation matter? Evidence from ebay auctions, The Journal of Industrial Economics (L(3)) (September 2002).

[14] MikoÅaj Morzy , Density-based measure of reputation of sellers in online auctions, in: ADMKD 2005, 1st ADBIS Workshop on Data Mining and Knowledge Discovery, 15–16 September 2005, Tallinn, Estonia, 2005.

[15] MikoÅaj Morzy , Marek Wojciechowski, Maciej Zakrzewicz, Intelligent reputation assessment for participants of web-based customer-to-customer auctions, in: Advances in Web Intelligence Third International Atlantic Web IntelligenceConference, AWIC 2005, Lodz, Poland, June 6–9, 2005.

[16] Lik Mui. Computational Models of Trust and Reputation: Agents, Evolutionary Games, and Social Networks. PhD thesis, Massachusetts Institute of Technology, December 2002.

[17] M.E.J. Newman, M. Girvan, Finding and evaluating community structure in networks, Physical Review E: Statistical, Nonlinear, and Soft Matter Physics 69 (026113) (2004).

[18] J. Philip, et al., The General Inquirer: A Computer Approach to Content Analysis, MIT Press, 1966.

[19] Paul Resnick, Richard Zeckhauser, Trust among strangers in internet transactions: empirical analysis of ebay's reputation system, Advances in Applied Microeconomics 11 (2002).

[20] Paul Resnick, Richard Zeckhauser, John Swanson, Kate Lockwood, The value of reputation on ebay: a controlled experiment, Technical report, School of Information, University of Michigan, 2004.

[21] J. Sabater-Mir, M. Paolucci, On representation and aggregation of social evaluations in computational trust and reputation models, International Journal of Approximate Reasoning 46 (2007) 458–483.

[22] Aleksander Wawer Radoslaw Nielek, Adam Wierzbicki, Spiral of hatred: social effects in internet auctions. between informativity and emotion, Electronic Commerce Research 10 (3–4) (2010) 313–330.

[23] A.P. Wierzbicki, The problem of objective ranking: foundations, approaches and applications, Journal of Telecommunications and Information Technology 3 (2008) 15–23.

[24] Adam Wierzbicki, Trust and fairness in open, Distributed Systems, volume 298, Springer Verlag, 2010.

[25] R. Yager, On the determination of strength of belief for decision support under uncertainty — part I: generating strengths of belief, Fuzzy Sets and Systems 142 (2004) 117–128.

[26] R. Yager, On the determination of strength of belief for decision support under uncertainty — part II: fusing strengths of belief, Fuzzy Sets and Systems 142 (2004) 129–142.

![](/api/attachments/QSJ3CDTK/fulltext/images/7779ac1415a50c78f5948d89569904dfe5d38efb6ed232f6b4726da49ad3874f.jpg)

Adam Wierzbicki received his B.S. in mathematics and M.S. in informatics from the University of Warsaw in 1997 and 1998. In June 2003, he received a Ph.D. degree from the Institute of Telecommunications of the Warsaw University of Technology. His Ph.D. thesis titled “Content Distribution and Streaming Media Communication on the Internet” concerned design of content delivery networks for improved quality and performance of streaming media communication.

Adam Wierzbicki is an expert in Peer-to-Peer computing. He has published several research papers on this subject and is a member of the Steering Committee of the International IEEE Peer-to-Peer Conference. He has acted as a co-editor of several journal issues on this subject (including Elsevier “Computer

Communications” and Springer “P2P Networking and Applications”). Dr. Wierzbicki has collaborated with professor Henning Schulzrinne's team on the development of the emerging standard of the P2P Protocol (P2PP). The team of Dr. Wierzbicki at PJIIT is preparing a P2P middleware for mobile devices, based on P2PP.

Apart from Peer-to-Peer computing, Dr. Wierzbicki is a specialist in the <sup>fi</sup>eld of social informatics. His current research interests focus on trust management and fairness in distributed systems. Dr. Wierzbicki heads the project mTeam (Mobile Team), <sup>fi</sup>nanced by a research grant of the Polish-Singaporian research program. See mTeam.pjwstk.edu.pl/ for further details. Dr. Wierzbicki also heads the project uTrust (Universal Trust), <sup>fi</sup>nanced by a research grant of the Polish Ministry of Science and Higher Education. See uTrust.pjwstk.edu.pl/ for further details. Dr. Wierzbicki has published several papers on applications of the theory of equity to providing fairness in open distributed systems, and is the author of a Springer book titled “Trust and Fairness in Open, Distributed Systems”. He is also interested in knowledge management and e-learning.

His professional experience includes a research contract with Philips, Natlab and a two-year employment as a systems designer for Suntech, Ltd, a software company that specializes in telecom management. He was also a team member of the European 6th Framework Research project “eGov-Bus”. Adam Wierzbicki is currently employed at the Polish-Japanese Institute for Information Technology, where he has the position of Vice-Dean of the Department of Informatics. At PJIIT, he has started a new major in Social Informatics for graduates of the social sciences.

Contact info: adamw@pjwstk.edu.pl.

Polish-Japanese Institute of Information Technology, Ul. Koszykowa 86, 02-008 Warsaw, Poland.

Web page: http://in<sup>fl</sup>acja.net/adamw/home/index\_en.php.

![](/api/attachments/QSJ3CDTK/fulltext/images/5ae3bd2f14d10b6fd104526887afae0ee7b9efb71cfd0955974f51d95d7829a6.jpg)  
Tomasz Kaszuba, M.Sc. is a research assistant in the Computer Networks Department at Polish Japanese Institute of Information Technology, Warsaw. Poland, His research interests include distributed computing, web mining, peerto-peer networks. Internet auction platforms , reputation and trust management systems. He works as an IT specialist in the Interactive Research Center.

![](/api/attachments/QSJ3CDTK/fulltext/images/0bd961a48d93493e0389ce6aefaa0dc52c4b01016312dc7e41df15ece32f7e71.jpg)

![](/api/attachments/QSJ3CDTK/fulltext/images/68d6953ea6c2342f1d3489aa1be8c5c96a3bfd295cd9916eca887cfab3a633c3.jpg)

Radoslaw Nielek received his Ph.D. degree from Polish-Japanese Institute of Information Technology (PJIIT) Warsaw, Poland. His Ph.D. thesis is titled "Designing Algorithms for Realising Social Goals". He held a Bachelor's Degree in Production Engineering and Management of Szczecin University of Technology and Master's Degree in Computer Science of PJIIT. His research interests include social simulation, trust management and opinion mining.

Paulina Adamska holds an M.Sc. degree in Computer Science (Mobile Networking, System and Network Programming) from Polish-Japanese Institute of Information Technology (PJIIT). She is a research assistant at PJIIT. As part of the mTeam project, she has designed and developed an overlayagnostic, topology-independent publish-subscribe algorithm. She was also co-author of the middleware based on the generic Peer-to-Peer Protocol. Currently as a member of the Reconcile project she is involved in modeling and simulating user strategies in digg-like systems, as well as analyzing their in<sup>fl</sup>uence on the information truthfulness and presentation. Her main areas of interest are P2P networks, news aggregation/recommender systems and cloud platforms (PaaS).

![](/api/attachments/QSJ3CDTK/fulltext/images/4ca9be47294eb4b48cc13368c5215ea3b2a2c1bbc969b15d94f60a0bc882b210.jpg)

Anwitaman Datta is an associate professor in the School of Computer Engineering at the Nanyang Technological University, Singapore. He is interested in large-scale networked distributed information systems and social collaboration networks, self-organization and algorithmic issues of these systems and networks and their scalability, resilience and performance. He leads the S\* and algorithmic aspects of Networked Distributed Systems (SANDS) research group at NTU.
