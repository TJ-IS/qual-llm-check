---
otero_id: 20873
otero_key: "5ABSUJAF"
title: "Collaborative reputation mechanisms for electronic marketplaces"
authors: "Giorgos Zacharia; Alexandros Moukas; Pattie Maes"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00084-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Collaborative reputation mechanisms for electronic marketplaces

Giorgos Zacharia<sup>)</sup>, Alexandros Moukas, Pattie Maes

MIT Media Laboratory, 20 Ames Street, E15-305, Cambridge, MA 02139, USA

## Abstract

Members of electronic communities are often unrelated to each other, they may have never met and have no information on each other’s reputation. This kind of information is vital in Electronic Commerce interactions, where the potential counterpart’s reputation can be a significant factor in the negotiation strategy. Collaborative reputation mechanisms can provide personalized evaluations of the various ratings assigned to each user to predict their reliabilities. While these reputation mechanisms are developed in the context of electronic commerce, they are applicable in other types of electronic communities such as chatrooms, newsgroups, mailing lists, etc. q 2000 Published by Elsevier Science B.V.

Keywords: Reputation mechanisms; Collaborative filtering; Rating systems; Electronic marketplaces

## 1. Introduction

Online communities bring together people geographically and sociologically unrelated to each other. Online communities have traditionally been created in the context of discussion groups, in the form of newsgroups, mailing lists or chatrooms. Online communities are usually either goal or interest-oriented. But, other than that, there is rarely any other kind of bond or real life relationship among the members of communities before the members meet each other online. The lack of information about the background, the character and especially the reliability of the members of these communities cause a lot of suspicion and mistrust among their members.

When a newcomer joins a chatroom, a newsgroup or a mailing list, he<sup>r</sup>she does not know how seriously he<sup>r</sup>she should take each participant until he<sup>r</sup>she has formed an opinion about the active members of the group. Likewise, the old members of the group do not know how seriously they should take a newcomer until he<sup>r</sup>she establishes him<sup>r</sup>herself in the group. If the group has a lot of traffic, the noise to signal ratio becomes too high, and the process of filtering out the interesting messages becomes increasingly difficult for a newcomer or an occasional reader of the group. If users did have an indication for the reputation of the author of each message, they could prioritize the messages according to their predicted quality.

Similar problems are encountered in other kinds of online communities as well. The recent development of online auction sites, and other forms of electronic marketplaces has created a new kind of online community, where people meet each other to bargain and transact goods. Online marketplaces like Kasbah 2 , MarketMaker 24 , eBay 6 and OnSale <sup>w x</sup> <sup>w</sup> <sup>x</sup> <sup>w x</sup> Exchange 18 introduce two major issues of trust. <sup>w</sup> <sup>x</sup>

Potential buyers have no physical access to the product of interest while they are bidding or negotiating. Therefore, sellers can easily misrepresent the condition or the quality of their products.

Additionally, sellers or buyers may decide not to abide by the agreement reached at the electronic marketplace, asking later to renegotiate the price, or even refuse to commit the transaction. Even worse, they may receive the product and refuse to send the money for it, or the other way around.

One way of solving the above mentioned problems would be to incorporate in the system a reputation brokering mechanism, so that each user can customize his<sup>r</sup>her pricing strategies according to the risk implied by the reputation values of his<sup>r</sup>her potential counterparts.

Reputation is usually defined as the amount of trust inspired by a particular person in a specific setting or domain of interest 17 . In <sup>w</sup> <sup>x</sup> ATrust in a Cryptographic EconomyB <sup>w</sup> <sup>x</sup> 19 , reputation is regarded as asset creation and it is evaluated according to its expected economic returns.

Reputation is conceived as a multidimensional value. An individual may enjoy a very high reputation for his<sup>r</sup>her expertise in one domain, while having a low reputation in another. For example, a Unix guru will probably have a high rank regarding Linux questions, while he may not enjoy as high a reputation for questions regarding Microsoft’s operating systems. These individual reputation standings are developed through social interactions among a loosely connected group that shares the same interest. Also, each user has his<sup>r</sup>her personal and subjective criteria for what makes a user reputable. For example, in the context of a discussion group, some users prefer polite mainstream postings while others engage in flame wars. Through this interaction, the users of online communities form subjective opinions of each other. These opinions may differ greatly between different users, and their variance is most of the time large enough to make the average opinion a rather unreliable prediction.

We have developed methods through which we can automate the social mechanisms of reputation for electronic marketplaces. We have already implemented an early version of these reputation mechanisms in Kasbah 2 . Kasbah is an ongoing research <sup>w</sup> <sup>x</sup> project to help realize a fundamental transformation in the way people transact goods — from requiring constant monitoring and effort, to a system where software agents do much of the bidding and negotiating on a user’s behalf. A user wanting to buy or sell a good creates an agent, gives it some strategic direction, and sends it off into the agent marketplace. Kasbah agents pro-actively seek out potential buyers or sellers and negotiate with them on their creator’s behalf. Each agent’s goal is to make the Abest dealB possible, subject to a set of user-specified constraints, such as a desired price, a highest or lowestŽ . acceptable price, and a date to complete the transaction 2 . In Kasbah, the reputation values of the<sup>w</sup> <sup>x</sup> individuals trying to buy<sup>r</sup>sell books<sup>r</sup>CDs are major parameters of the behavior of the buying, selling or finding agents of the system.

Section 1 of this paper outlines the problem we are trying to solve and the problems we faced during the initial implementation of the system in Kasbah. Section 2 describes related work and Section 3 outlines specific problems inherent in online marketplaces. Finally, Sections 4 and 5 describe the proposed solutions.

## 2. Related work

We can divide the related work on reputation systems into two major categories: non-computational reputation systems like the Better Business Bureau Online 3 and computational ones. The Bet-<sup>w</sup> <sup>x</sup> ter Business Bureau Online is a centralized repository of consumer and business alerts. They mainly provide information on how well businesses handle disputes with their clients. They also keep records of the complaints about local or online companies and even publish consumer warnings against some of them. They do not provide any kind of numerical ratings for business or consumer trustworthiness.

The computational methods cover a broad domain of applications, from rating of newsgroup postings and webpages, to rating people and their expertise in specific areas. This section focuses on the related computational methods and a comparison of their major features Table 1 .Ž .

One way of building a reputation mechanism involves having a central agency, which keeps records of the recent activities of the users of the system, very much like the scoring systems of credit history agencies. The credit history agencies use customized evaluation mechanisms provided by the software of Fair Isaak 9 in order to assess the risk<sup>w</sup> <sup>x</sup> involved in giving a loan to an end-consumer. The ratings are collected from the previous lenders of the consumers, and consumers are allowed to dispute those ratings if they feel they have been treated unfairly. The resolution of a rating dispute is a responsibility of the end consumer and the party that rated the particular consumer.

Table 1  
Comparison of online reputation systems. In the APairwise ratingB column, we indicate whether the ratings are bi-directional or one-directional, and who submits ratings. In the APersonalized EvaluationB column, we indicate whether the ratings are evaluated in a subjective way, based on who makes the query

<table><tr><td>System</td><td>Pair-wise rating</td><td>Personalized evaluation</td><td>Textual comments</td></tr><tr><td>Firefly</td><td>Rating of recommendations</td><td>Yes</td><td>Yes</td></tr><tr><td>GroupLens</td><td>Rating of articles</td><td>Yes</td><td>No</td></tr><tr><td>Web of Trust</td><td>Transitive ratings</td><td>Yes</td><td>No</td></tr><tr><td>eBay</td><td>Buyers and sellers rate each other</td><td>No</td><td>Yes</td></tr><tr><td>Amazon</td><td>Buyers and sellers rate each other</td><td>No</td><td>Yes</td></tr><tr><td>OnSale</td><td>Buyers rate sellers</td><td>No</td><td>Yes</td></tr><tr><td>Credit history</td><td>Lenders rate customers</td><td>No</td><td>Yes</td></tr><tr><td>PICS</td><td>Self-rating</td><td>No</td><td>No</td></tr><tr><td>Elo and Glicko</td><td>Result of game</td><td>No</td><td>No</td></tr><tr><td>Bizrate</td><td>Consumers rate businesses</td><td>No</td><td>Yes</td></tr></table>

However useful a centralized approach may be, it requires a lot of overhead on behalf of the service providers of the online community. Furthermore, the centralized solutions ignore possible personal affinities, biases and standards that vary across various users.

Other proposed approaches like Yenta 10 , <sup>w</sup> <sup>x</sup> Weaving a web of Trust 14 , and the Platform for<sup>w</sup> <sup>x</sup> Internet Content Selection PICS such as theŽ . Ž Recreational Software Advisory Council 20 are <sup>w</sup> <sup>x</sup>. more distributed. However, they require the users to rate themselves and to have either a central agency or other trusted users verify their trustworthiness. One major problem with these systems is that no user would ever label him<sup>r</sup>herself as an untrustworthy person. Thus, all new members would need verification of trustworthiness by other trustworthy users of the system. In consequence, a user would evaluate his<sup>r</sup>her counterpart’s reputation by looking at the numerical value of his<sup>r</sup>her reputation as well as the trustworthiness of his<sup>r</sup>her recommenders.

Yenta and Weaving a Web of Trust introduce computational methods for creating personal recommendation systems, the former for people and the latter for webpages. Weaving a Web of Trust relies on the existence of a connected path between two users, while Yenta clusters people with common interests according to recommendations of users who know each other and can verify the assertions they make about themselves. Both systems require prior existence of social relationships among their users, while in online marketplaces, deals are brokered among people who may have never met each other.

Collaborative filtering is a technique for detecting patterns among the opinions of different users, which then can be used to make recommendations to people, based on opinions of others who have shown similar taste. This technique basically automates Aword of mouthB to produce an advanced and personalized marketing scheme. Examples of collaborative filtering systems are HOMR, Firefly 23 and<sup>w</sup> <sup>x</sup> GroupLens 21 . GroupLens is a collaborative filter-<sup>w</sup> <sup>x</sup> ing solution for rating the contents of Usenet articles and presenting them to the user in a personalized manner. In this system, users are clustered according to the ratings they give to the same articles. These ratings are used for determining the average ratings of articles for that cluster.

The Elo 7 and the Glicko 13 systems are<sup>w x</sup> <sup>w</sup> <sup>x</sup> computational methods used to evaluate the player’s relative strengths in pairwise games. After each game, the competency score of each player is updated based on the result and the previous scores of the two users. The basic principle behind ratings in pairwise games is that the ratings indicate which player is most likely to win a particular game. The probability that the stronger player will win the game is positively related to the difference in the abilities of the two users. In general, the winner of a game earns more points for his<sup>r</sup>her rating, while the defeated player loses points from his rating. The changes in the ratings of the two users depend on their rating difference before the game takes place. If the winner is the player who had a higher score before the game, the change in the ratings of the two users is negatively related to their rating difference before the game. If however the winner of the game is the player who had a lower score before the game took place, the changes in the scores of the two players are positively related to their rating difference before the game.

Bizrate 4 is an online shopping guide that pro- <sup>w</sup> <sup>x</sup> vides ratings for the largest 500 companies trading online. The ratings are collected in two different ways. If Bizrate has an agreement with an online company, the company provides Bizrate with transaction information so that Bizrate can independently survey the satisfaction of every customer who makes a purchase from its web site. The surveys measure the customer satisfaction in several categories, and Bizrate provides an overall, as well as detailed report on the performance of the rated company. If a company does not have an agreement with Bizrate, then the staff of Bizrate reviews the company and provides a report based on the editorial assessment of Bizrate. Bizrate rates different features for different categories of companies, based on Bizrate’s hierarchical ontology of online businesses. The scores in each category are computed as the average of the collected ratings, and they are given on a scale of 1 to 5. The consumer reviews are presented separately from the editorial reviews, and the companies that agree to have their customers rate them are labeled as ACustomer Certified MerchantsB.

In the context of electronic marketplaces, the most relevant computational methods are the reputation mechanism of online auction sites like OnSale Exchange 18 , eBay 6 and Amazon 1 . OnSale<sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> Exchange was later transformed to Yahoo Auctions, and Yahoo implemented the same rating mechanism as eBay. In OnSale, which used to allow its users to rate sellers, the overall reputation value of a seller was calculated as the average of all his<sup>r</sup>her ratings through his<sup>r</sup>her usage of the OnSale system. In eBay, sellers receive <sup>q</sup>1, 0 or <sup>y</sup>1 as feedback for their reliability in each auction and their reputation value is calculated as the sum of those ratings over the last 6 months. In OnSale, newcomers had no reputation until someone eventually rated them, while in eBay they start with zero feedback points. Bidders in the OnSale Exchange auction system were not rated at all.

OnSale tried to ensure the bidders’ integrity through a rather psychological measure: bidders were required to register with the system by submitting a credit card number. OnSale believed that this requirement helped to ensure that all bids placed were legitimate, which protected the interests of all bidders and sellers. However, the credit card submission method does not solve the multiple identities, problem, because users can have multiple credit cards in their names. In both the eBay and the OnSale systems, the reputation value of a seller is available, with any textual comment that may exist, to the potential bidders. The mechanism at Amazon auctions is exactly the same as OnSale’s, with the improvement that both the buyers and the sellers are rated after each transaction.

In online marketplaces like the auction sites, it is very easy for a user to misbehave, receive low reputation ratings, and then leave the marketplace, obtain another online identity and come back without having to pay any consequence for the previous behavior. Therefore, newcomers to online marketplaces are treated with suspicion until they have been around long enough with a consistent trustworthy behavior. Thus, newcomers receive less attractive deals, than older users that are equally trustworthy. However, this poor treatment to the newcomers creates an economic inefficiency, because transactions with newcomers are underpriced, or even do not take place at all. This economic inefficiency could be removed if the online sites disallowed anonymity, or alleviated if newcomers were allowed to pay fees for higher initial reputation values and those users could be committed to lifetime pseudonyms, so that anonymity is preserved, but identity switching is eliminated 11 .<sup>w</sup> <sup>x</sup>

Recently, both Amazon and eBay allowed their users to become AeBay registeredB users, or AAmazon registeredB users, respectively. What that means is that, they can provide to the marketplace provider enough personal data, so that the marketplace provider can find out their real identities in case of a fraud. Therefore, the users can transact online using pseudonymous identities, whose link to their real identities is held by the marketplace provider alone. Thus, at the expense of their total anonymity, the newly registered users can enjoy increased levels of trust towards them, despite the fact that they do not have any transaction history to prove themselves. This approach makes transactions more efficient from a microeconomic perspective, because the pseudonymous users can achieve better deals than totally anonymous users since they are trusted more 11 .

## 3. The problem of trust in Consumer-to-Consumer Electronic Marketplaces

The emergence of large Consumer-to-Consumer Electronic Marketplaces has highlighted several problems regarding issues of trust and deception in these marketplaces. Unlike discussion oriented online communities, like mailing lists, WWW message boards and chatrooms, in these online marketplaces there is a financial cost when users are deceived. The major marketplace providers like eBay, OnSale, Yahoo and Amazon, tried to tackle the problem by introducing simple reputation mechanisms. These reputation mechanisms try to give an indication of how trustworthy a user is, based on his<sup>r</sup>her performance in his<sup>r</sup>her previous transactions. Although there are several kinds of possible frauds, or deceptions in online marketplaces, the users’ trustworthiness is typically abstracted in one scalar value, called the feedback rating, or reputation. The fact that users’ trustworthiness is abstracted in this one-dimensional value has been instrumental in the success of these mechanisms, because it minimizes the raters overhead from a time–cost and usability perspective.

## 4. Desiderata for online reputation systems

While the above discussed reputation mechanisms have some interesting qualities, we believe they are not perfect for maintaining reputations in online communities and especially in online marketplaces.

This section describes some of the problems of online communities and their implications for reputation mechanisms.

In online communities, it is relatively easy to change one’s identity 8,11,15 . Thus, if a user ends<sup>w</sup> <sup>x</sup> up having a reputation value lower than the reputation of a beginner, he<sup>r</sup>she would have an incentive to discard his<sup>r</sup>her initial identity and start from the beginning. Hence, it is desirable that while a user’s reputation value may decrease after a transaction, it will never fall below a beginner’s value. However, with such a positive reputation mechanisms, the beginners are subject to mistreatment by the rest of the community because nobody knows if they are in fact new users or bad ones who just switched identi ties. Hence, trustworthy beginners will have to accept less attractive deals in the context of an ecommerce community, or the information they provide on a discussion community will be undervalued until they establish themselves. Therefore, the mistreat ment of newcomers creates an inherent economic inefficiency, because the monetary, or information transactions of the newcomers are undervalued. This economic inefficiency can be faced either by disallowing anonymity, or by allowing users to purchase reputation points for a monetary value 11 . How-<sup>w</sup> <sup>x</sup> ever, in such a model we need to charge for names in the first place and enforce persistent pseudonymous identities 11 . Despite the benefits of this model, we<sup>w</sup> <sup>x</sup> decided against it because of the requirement for persistent pseudonymous identities. In some forms of online communities, it is desirable to allow users to have multiple personalities and<sup>r</sup>or switch identities. For example, in political discussion forums, like the Cyprus List 5 , it is very important to allow some<sup>w</sup> <sup>x</sup> users to maintain different personalities, than the ones they use on their respective Greek or Turkish community mailing lists. Because of these reasons, we decided to a first desideratum for online reputation mechanisms, namely that it is desirable that a beginner cannot start with a reputation above the minimum allowed by the system.

In addition, users who have very low reputation ratings should be able to improve their ratings at almost the same rate as a beginner. This implies that the reputation value of users should not be the arithmetic average of all of their ratings since this would give the users who perform relatively poor in the beginning an incentive to get rid of their bad reputation history by adopting a new identity.

Therefore, a successful online reputation mechanism has to be based on a positive reputation system. However, having the users start with minimum reputation is not necessarily the only viable solution. An alternative approach 11 would be to allow newcom-<sup>w</sup> <sup>x</sup> ers to pay entry fees in order to be considered trustworthy. This approach would be very applicable in online marketplaces, where the interaction is clearly monetary based. However, it would probably be unwelcome in other more casual forms of online communities, like newsgroups or mailing lists.

Another problem with systems like Kasbah and online auction sites is that the overhead of performing fake transactions is fairly low. This makes it possible for people to perform fake transactions with their friends, rating each other with perfect scores each time, so as to increase their reputation value. Likewise in an online group, the marginal cost of sending a new message is zero. So a group of users may exchange messages for the sake of creating fresh unique ratings for each other. Notice that prohibiting each user from rating others more than once would not solve this problem since a user can still falsely improve his<sup>r</sup>her ratings by creating multiple fake identities, which can then rate the user’s real identity with perfect scores. A good reputation system should avoid both of these problems.

In order to do this, we have to ensure that the ratings given by users with an established high reputation in the system are weighted more than the ratings given by beginners or users with low reputations. In addition, the reputation values of the users should not be allowed to increase ad infinitum as is the case with eBay, where a seller can cheat 20% of the time but still maintain a monotonically increasing reputation value.

Reputation mechanisms have to be able to quantify the subjective expectations 4 of the users, based<sup>w</sup> <sup>x</sup> on their past experiences on the online community. Therefore, it is desirable that the reputation mechanisms can provide personalized evaluations, based on the subjective criteria of the users engaged in an online interaction.

Finally, we have to consider the memory of the reputation system 17 . We know that the larger the<sup>w</sup> <sup>x</sup> number of ratings used in the evaluation of reputation values, the better the predictability of the mechanism. However, since the reputation values are associated with human individuals and humans change their behavior over time, it is desirable to disregard very old ratings. Thus, it is desirable that the predicted reputation values are closer to the current behavior of the individuals rather than their overall performance.

The desiderata described here are by no means universally applicable to any kind of online community. For example, the requirement for minimal initial reputations can be relaxed if our online community consists of people who know each other 25 .

## 5. Sporas: a reputation mechanism for loosely connected online communities

Keeping in mind the discussion presented above, Sporas provides a reputation service based on the following principles:

1. New users start with a minimum reputation value, and they buildup reputation during their activity on the system Fig. 1 .Ž .

2. The reputation value of a user never falls below the reputation of a new user.

3. After each transaction, the reputation values of the involved users are updated according to the feedback provided by the other parties, which reflect their trustworthiness in the latest transaction.

4. Two users may rate each other only once. If two users happen to interact more than once, the system keeps the most recently submitted rating.

5. Users with very high reputation values experience much smaller rating changes after each update. This approach is similar to the method used in the Elo 7 and the Glicko 13 systems for pairwise <sup>w x</sup> <sup>w</sup> <sup>x</sup> ratings.

6. The algorithm adapts to changes in the users’ behaviors. Thus, ratings must be discounted over time so that the most recent ratings have more weight in the evaluation of a user’s reputation.

From an algorithmic perspective, our system has to satisfy the following requirements:

1. It has to require small computational space and time for the updates of the reputation predictions.

![](/api/attachments/5ABSUJAF/fulltext/images/7368a0211121868cb6178228f861f630b997faaf182d3e3f74624ce32167db06.jpg)  
Fig. 1. Buildup of reputation simulation with 10 different users over 100 ratings with $\theta = 1 0 ^ { \circ }$

2. The system has to be adaptively controlled, predicted and supervised using the accuracy of the rating predictions. The ratings submitted after each interaction have to be compared with the predicted ones, and their difference used as an input to the recursive function.

3. Old predictions have to be discounted and the system has to be a biased estimator of the most recent behavior.

Based on these requirements, we propose to estimate the time varying reputation of a user using the following algorithm.

New users start with reputation values equal to 0 and can advance up the maximum of 3000, so lets call our reputation range $D = 3 0 0 0$ . The reputation ratings, $W _ { i } ,$ , vary from 0.1 for terrible to 1 for perfect. The minimum reputation rating, $W _ { i } ,$ is set to be above 0, unlike the beginners’ reputations $R _ { \mathrm { o } } = 0 \mathrm { : }$ so that once a user has received at least one rating, then the users reputation value will be necessarily greater than zero, even if that rating was the minimum one. That way, a user is always worse off if he<sup>r</sup>she switches identities. Suppose that at time $t = i ,$ , a user with reputation $R _ { i - 1 }$ is rated with a score $W _ { i }$ by another user with reputation $R _ { i } ^ { \mathrm { { o t h e r } } }$ . Let $E _ { i } = R _ { i - 1 } / D$ At equilibrium, $E _ { i }$ can be interpreted as the expected value of $W _ { i } .$ , though early in a user’s activity it will be an underestimate. Let $\theta > 1$ be the effective number of ratings considered in our reputation evaluation. We then propose the Sporas formula Eq. 1 ,Ž Ž .. which is a recursive estimate of the reputation value of a user at time $t = i ,$ , given the user’s most recent reputation, $R _ { i - 1 }$ , the reputation of the user giving the rating, $R _ { i } ^ { \mathrm { { o t h e r } } }$ , and the rating $W _ { i } \mathbf { \mathrm { : } }$

$$
\begin{array}{l} R _ {i} = R _ {i - 1} + \frac {1}{\theta} \Phi (R _ {i - 1}) R _ {i} ^ {\text {other}} (W _ {i} - E _ {i}) \\ \Phi (R _ {i - 1}) = 1 - \frac {1}{1 + \mathrm{e} ^ {\frac {- (R _ {i - 1} - D)}{\sigma}}} \\ E _ {i} = R _ {i - 1} / D, \end{array}\tag{1}
$$

Sporas formulae. Recursive computation of the Reputation value at time<sup>s</sup>t and computation of the damping function $\varPhi$

The parameter is the acceleration factor of the damping function $\varPhi .$ , which slows down the changes for very reputable users. The smaller the value of $\sigma ,$ the steeper the damping factor $\varPhi$ is. The behavior of the damping function $\varPhi$ with different values of $\sigma$ is shown in Fig. 2, which plots $\varPhi$ for 10 equidistant values of $\sigma$ , ranging from $D / 1 0 0 .$ , to $1 0 D / 1 0 0$ The value of $\sigma$ is chosen so that the $\Phi ,$ , remains above 0.9 for all users whose reputation is below $3 / 4$ of $D .$ Therefore, it can be calculated that $\sigma \leq$ $( 0 . 2 5 / \ln 9 ) D = 0 . 1 1$

Dumping Function  
![](/api/attachments/5ABSUJAF/fulltext/images/8f6cf1786131e6b5c67c4f52e83618231132a2a541526946d7361bfa5a3eee1d.jpg)  
Fig. 2. Damping function. The behavior of the damping function $\varPhi$ with 10 different values of  , ranging from $D / 1 0 0$ to 10D<sup>r</sup>100.

Eq. 1 shows that the incremental change in theŽ . reputation value of a user receiving a rating of $W _ { i }$ from user $R _ { i } ^ { \mathrm { { o t h e r } } }$ , is proportional to the reputation value $R _ { i } ^ { \mathrm { { o t h e r } } }$ of the rater.

$$
R _ {i} = R _ {i - 1} + \frac {1}{\theta} \varPhi \big (R _ {i - 1} \big) R _ {i} ^ {\mathrm{other}} \big (W _ {i} - E _ {i} \big)
$$

$$
R _ {i} > R _ {i - 1} - \frac {1}{\theta} \Phi (R _ {i - 1}) R _ {i} ^ {\text { other }} R _ {i - 1} / D,
$$

$$
\text { since } \frac {1}{\theta} \Phi (R _ {i - 1}) R _ {i} ^ {\text { other }} W _ {i} > 0
$$

$$
R _ {i} > R _ {i - 1} - \frac {1}{\theta} \Phi (R _ {i - 1}) D R _ {i - 1} / D, \text { since } R _ {i} ^ {\text { other }} \leq D
$$

$$
R _ {i} > R _ {i - 1} - \frac {1}{\theta} R _ {i - 1} = \frac {\theta - 1}{\theta} R _ {i - 1},
$$

$$
\text { since } \Phi (R _ {i - 1}) \leq 1
$$

$$
R _ {i} > 0, \text { since } \theta > 1
$$

$$
\text { Also,   if   } R _ {i - 1} = D - x, \text {   and   } x \geq 0
$$

$$
R _ {i} = D - x + \frac {1}{\theta} \Phi (R _ {i - 1}) R _ {i} ^ {\text {other}} (W _ {i} - (D - x) / D)
$$

$$
R _ {i} \leq D - x + \frac {1}{\theta} \Phi (R _ {i - 1}) R _ {i} ^ {\text { other }} (1 - (D - x) / D),
$$

$$
\mathrm{since} W _ {i} \leq 1
$$

$$
R _ {i} \leq D - x + \frac {1}{\theta} \Phi (R _ {i - 1}) D x / D, \text { since } R _ {i} ^ {\text { other }} \leq D
$$

$$
R _ {i} \leq D - x + \frac {x}{\theta}, \text { since } \Phi (R _ {i - 1}) \leq 1
$$

$$
R _ {i} \leq D, \text { since } \theta > 1, \text { and } x \geq 0.\tag{2}
$$

Proof of lower and upper bounds of the recursive estimates of $R _ { i }$

In addition, as we can see from Eq. 2 , theŽ . recursive estimates of $R _ { i }$ are always positive, thus no user can have a rating value lower than that of a beginner, and those estimates have an upper bound of D.

The predicted rating of a user is expressed as the current reputation value over the maximum reputation value allowed in the system. Thus, if the submitted rating for a user is less than his<sup>r</sup>her desired rating value, the reputation value of the user decreases.

Eq. 1 is a simple machine learning algorithm Ž . that guarantees that if $W _ { i }$ is stationary time series of observations, then it will give asymptotic convergence of $R _ { i }$ to the actual R and the speed of the convergence is controlled by the learning factor $1 / \theta$ <sup>w</sup> <sup>x</sup> 22 .

The value of $1 / \theta$ determines how fast the reputation value of the user changes after each rating. The smaller the value of $1 / \theta$ the longer the memory of the system. Thus, just like credit card history 9 ,<sup>w</sup> <sup>x</sup> even if a user enters the system with a very low reputation, if his<sup>r</sup>her reliability improves, his<sup>r</sup>her reputation value will not suffer forever from the past poor behavior.

## 6. Reliability of the reputation value predictions

Using a similar approach to the Glicko system, we have incorporated into the system a measure of the reliability of the users’ reputations. The reliability is measured by the reputation deviation RD ofŽ . the estimated reputations. The recursively estimated RD of the algorithm is an indication of the predictive power of the algorithm for a particular user. Therefore, a high RD can mean either that the user has not been active enough to be able to make a more accurate prediction for his<sup>r</sup>her reputation, or that the user’s behavior has indeed a lot of variation, or even that the user’s behavior is too controversial to be evaluated the same way by his<sup>r</sup>her raters. As we explained in the previous sections, we assume that the user’s reputation is also an indication of how reputable the user’s opinion about others is. Therefore, the change in the reputation of a person receiving a rating is positively related to the reputation of a user who submits the rating Eq. 1 . Thus, the RDŽ Ž ..

of a user’s reputation indicates the reliability of that user’s opinion for the users he<sup>r</sup>she rates.

Since the reputation update function is computed according to Eq. 1 , if we ignore the damping factorŽ . $\varPhi .$ , then RD can be computed as a weighted LS problem 16 defined by: <sup>w</sup> <sup>x</sup>

$$
\mathrm{RD} _ {i} ^ {2} = \left\lfloor \lambda \mathrm{RD} _ {i - 1} ^ {2} + \left(R _ {i} ^ {\text { other }} (W _ {i} - E _ {i})\right) ^ {2} \right\rfloor / T _ {0}.\tag{3}
$$

Recursive computation of the RD at time $t = i .$ Where $\lambda < 1$ is a constant and $T _ { 0 }$ is the effective number of observations. Since is a constant, $T _ { 0 }$ Ž Ž .. which we will set equal to of Eq. 1 can be calculated as:

$$
T _ {0} = \sum_ {i = 0} ^ {\infty} \lambda^ {i} = \frac {1}{1 - \lambda},\tag{4}
$$

computation of the effective number of observations with a forgetting factor of .

Eq. 3 is a generic recursive estimation algorithmŽ . of Recursive Least Squares RLS with a forgetting Ž . factor of , which can be used for online estimations <sup>w</sup> <sup>x</sup> 16 . So Eq. 3 estimates recursively the average Ž . square deviation of the predictions of Eq. 1 , over Ž . the last $T _ { 0 }$ ratings. In fact, if <sup>s</sup> 1 and $T _ { 0 } = \mathrm { i }$ , then $\mathrm { R D } _ { i } ^ { 2 }$ is precisely the average square deviation of the predictions of Eq. 1 , over the lastŽ . $T _ { 0 }$ ratings. However, we incorporate the forgetting factor in order to ensure that the most recent ratings have more weight than the older ones. Note that Eq. 1 isŽ . not the solution to the RLS Eq. 3 , as would be theŽ . case if we were trying to minimize RD for a given . However, Eq. 3 is a recursive estimator of theŽ . RD, given Eq. 1 .Ž .

With the proper choice of the initial values of a RLS algorithm, with or without a forgetting factor, the algorithm’s predictions will coincide with the predictions of an offline Least Square fitting of the user’s data, if the user’s behavior has a stationary, non-periodic mean and standard deviation 16 . In<sup>w</sup> <sup>x</sup> our case though, we will deliberately choose initial conditions that estimate a beginner’s reputation to be minimal with a maximum standard deviation. We need these initial conditions so that there is no incentive for a user to switch identities. So the beginners start with a RD of $D / 1 0$ and the minimum RD is set to $D / 1 0 0 ,$ , and, as it was explained above, their initial reputation value is set to 0.

With these initial values, we ensure that the reputation value of any user will always be strictly higher than the reputation value of a beginner Eq. 2 .Ž Ž .. Therefore, user A, for example, who has been consistently receiving poor scores will end up having both a low reputation and a low RD, but the reputation value of A will always be higher than a beginners reputation.

However, the low RD of user A identifies him<sup>r</sup>her as an established untrustworthy person. Therefore, the combination of a low reputation value and a low RD may incite user A to switch identities. However, it is not clear that A will be better off by switching identities, because although he will start with a larger RD, due to the uncertainty about his<sup>r</sup>her trustworthiness, A’s reputation will be lower than before switching identities. Therefore, if A intends to improve him<sup>r</sup>herself, he<sup>r</sup>she is better off by preserving his identity, because he<sup>r</sup>she can grow it faster. If A intends to keep behaving improperly, he<sup>r</sup>she does not really have a big incentive to switch identities, because as a beginner, he<sup>r</sup>she will be treated equally unfavorably.

The major limitation of Sporas is that it treats very unfavorably all the new users. This unfavorable treatment is a necessary trade off, if we want to allow total anonymity for the users of an online community.

## 7. Histos: a reputation mechanism for highly connected online communities

Sporas, described in Section 6, provides a global reputation value for each member of an online community. This information is associated with the users as a part of their identity. However, different people groups have different standards and they tend to trust the opinions of the people who have the same standards with themselves. For example, if I am about to transact online with someone I have never interacted before, if a trusted friend of mine has transacted with the same user before, I am probably willing to trust my friend’s opinion about that user more than the opinions of a few people I have never interacted with before. Likewise, the PGP web of Trust 12 uses the<sup>w</sup> <sup>x</sup> idea that we tend to trust someone trusted by someone we trust more than we trust a total stranger.

Following a similar approach, we decided to build Histos, which is a more personalized reputation system compared to Sporas. In Weaving a Web of Trust <sup>w</sup> <sup>x</sup> 14 , entities are trusted if there is a connected path of PGP signed webpages between every pair of users. In the case of Histos, which is a pairwise rating system, we also have to consider the reputation ratings connecting the users of the system. So unlike Sporas, the reputation of a user in Histos, depends on who makes the query, and how that person rated other users in the online community.

We can represent the pairwise ratings in the system as a directed graph Fig. 3 , where nodes repre-Ž . sent users and weighted edges represent the most recent reputation rating given by one user to another, with the arrow pointing towards the rated user. If there exists a connected path between two users, say from A to $\mathbf { A } _ { \mathrm { L } }$ , then we can compute a more personalized reputation value for $\mathbf { A } _ { \mathrm { L } }$

When user $\mathbf { A } _ { \mathbf { o } }$ submits a query for the Histos reputation value of user $\mathbf { A } _ { \mathrm { L } }$ , we perform the following computation.

The system uses a Breadth First Search algorithm to find all the directed paths connecting $\mathbf { A } _ { \mathbf { o } }$ to $\mathbf { A } _ { \mathrm { L } }$ that are of length less than or equal to N. As described above, we only care about the chronologically $q$ most recent ratings given to each user. Therefore, if we find more than $q$ connected paths taking us to user $\mathbf { A } _ { \mathrm { L } }$ , we are interested only in the most recent $q$ paths with respect to the last edge of the path.

We can evaluate the personalized reputation value of $\mathbf { A } _ { \mathrm { L } }$ if we know all of the personalized reputation ratings of the users connecting to $\mathbf { A } _ { \mathrm { L } }$ in the path. Thus, we create a recursive step with at most $q$ paths with length at most N<sup>y</sup>1.

![](/api/attachments/5ABSUJAF/fulltext/images/51410f38d9eba8043bb51b69e993b56cbf4adcaf7d7878e568df706b2d2e91b7.jpg)  
Fig. 3. Rating paths between users $\mathbf { A } _ { 1 }$ and $\mathbf { A } _ { 1 1 } .$

If the length of the path is only 1, it means that the particular user, $\mathbf { A } _ { \mathrm { L } }$ , was rated by $\mathbf { A } _ { \mathrm { o } }$ directly. Then, the direct rating given to user $\mathbf { A } _ { \mathrm { L } }$ is used as the personalized reputation value for user $\mathbf { A } _ { \mathbf { o } }$ . Thus, the recursion terminates at the base case of length 1.

For the purpose of calculating the personalized reputation values, we use a slightly modified version of the reputation function of Sporas Eq. 1 . ForŽ Ž .. each user $\mathbf { A } _ { k }$ , with $m _ { k } ( n )$ connected paths going from $\mathbf { A } _ { \mathrm { o } }$ to $\mathbf { A } _ { k }$ , we calculate the reputation of $\mathbf { A } _ { k }$ as follows.

Let $W _ { j k } ( n )$ denote the rating of user $\mathbf { A } _ { j }$ for user $\mathbf { A } _ { k } ( n )$ at a distance n from user $\mathbf { A } _ { \mathbf { o } } ,$ , and $R _ { k } ( n )$ denote the personalized reputation of user $\mathbf { A } _ { k } ( n )$ from the perspective of user $\mathbf { A } _ { \mathbf { o } } .$

At each level n away from user $\mathbf { A } _ { \mathbf { o } } ,$ , the users $\mathbf { A } _ { k } ( n )$ have a reputation value given by:

$$
R _ {k} (n) = D \sum_ {j} \left(R _ {j} (n - 1) W _ {j k} (n)\right) / \sum_ {j} R _ {j} (n - 1)
$$

;jk, such that $W _ { j k } \big ( n \big ) \ge 0 . 5$

$$
m _ {k} (n) = \deg \left(\mathrm{A} _ {k} (n)\right) = | W _ {j k} (n) |,\tag{5}
$$

Histos formulae. Where $\deg ( \mathsf { A } _ { k } ( n ) )$ is the number of connected paths from $\mathbf { A } _ { \mathrm { o } }$ to $\mathbf { A } _ { k } ( n )$ and D is the range of reputation values Eq. 1 . The usersŽ Ž .. $\mathbf { A } _ { k } ( n )$ who have been rated directly by user $\mathbf { A } _ { \mathrm { o } }$ with a rating $W _ { 1 k } ( 1 )$ have a reputation value equal to:

$$
R _ {k} (0) = D W _ {1 k} (0),\tag{6}
$$

Histos formulae.

As we explained above, we are interested only in the $q$ most recent ratings for each user, so if $m _ { k } ( n )$ is larger than q, we pick from those edges the subset with the $q$ most recent ratings.

Consider, for example, Fig. 4, at level 2. The personalized reputation of user $\mathbf { A } _ { 1 } ( 3 )$ , will be:

$$
\begin{array}{l} R _ {1} (3) = D \big (R _ {1} (2) W _ {1 1} (2) + R _ {2} (2) W _ {2 1} (2) \\ \qquad + R _ {3} (2) W _ {3 1} (2) \big) / \big (R _ {1} (2) + R _ {2} (2) \\ \qquad + R _ {3} (2) \big), \end{array}\tag{7}
$$

Histos query for user $\mathbf { A } _ { 1 } ( 3 )$ in Fig. 4.

Since, all the paths at both Level 0 and Level 1, have rating contributions from only one source per target, it means that the personalized reputation of $\mathbf { A } _ { 1 } ( 3 )$ is:

![](/api/attachments/5ABSUJAF/fulltext/images/9f0f6a81644cb565d5494bdec338a958a96c3b650094ec13ed746a7ac55f140f.jpg)  
Fig. 4. Example of a Histos query.

$$
\begin{array}{l} R _ {1} (3) = D \big (W _ {1 1} (1) W _ {1 1} (2) + W _ {2 2} (1) W _ {2 1} (2) \\ \qquad + W _ {3 3} (1) W _ {3 1} (2) \big) / \big (W _ {1 1} (1) + W _ {2 2} (1) \\ \qquad + W _ {3 3} (1) \big), \end{array}\tag{8}
$$

result of a Histos query for user $\mathbf { A } _ { 1 } ( 3 )$ in Fig. 4.

Histos needs a highly connected graph. If a path from $\mathbf { A } _ { \mathrm { o } }$ to $\mathbf { A } _ { \mathrm { L } }$ with length less than or equal to N does not exist, we fall back to the simplified Sporas reputation mechanism.

User $\mathbf { A } _ { \mathbf { o } }$ makes a Histos query for user $\mathbf { A } _ { 1 } ( 3 )$ The query finds three unique paths of reputable ratings and evaluates the personalized reputation of $\mathbf { A } _ { 1 } ( 3 )$ from the perspective of $\mathbf { A } _ { \mathbf { o } } .$

## 8. Implementation

The Reputation Server was implemented as a plug-in Fig. 5 to the MarketMaker 24 , a Con-Ž . <sup>w</sup> <sup>x</sup> sumer-to-Consumer Ecommerce site at MIT. As described above, MarketMaker is a web-based Agent Mediated Marketplace. Whenever two agents make a deal on the marketplace, the users are notified about

![](/api/attachments/5ABSUJAF/fulltext/images/ab833a60fa296746abe0631f1677d6f8d7101ff5de456b7cb373a07fc32ad5ed.jpg)  
Fig. 5. MarketMaker. A user browses a category of CD products being sold on MarketMaker. The reputation of each user is included with the description of the product. A colored bar coding is used to visually represent the relative trustworthiness of each user. The length of the blue bar is proportional to the reputation of the user, and the length of the yellow bar is what that user is missing to achieve a perfect reputation.

the terms of the deal and the contact information of their counterpart and the buyer and the seller are then asked to rate each other based on their performance in the particular deal. The ratings may be submitted within 30 days from the moment the deal was reached, and the two users are prompted to rate each other whenever they log-in on the marketplace. The user may rate his<sup>r</sup>her counterpart as Horrible, Difficult, Average, Good or Great. The ratings are translated to their respective numerical values of 0.2, 0.4, 0.6, 0.8 and 1 and are submitted to the backend database.

When the user browses the marketplace, he can see the various buying or selling agents with the reputation values of their owners Fig. 5 . The repu-Ž . tation values are presented both as numerical values and as colored bars. Since the number of users of MarketMaker is still very small, the personalized reputation values are evaluated in real time, through a wrapper called by the CGI script, which generates the html of the webpage. However, if we had more users the calculation of the personalized reputation values might become too slow to be done in real time. In that case, we would use a daemon, which updates the reputations of all users who are affected by a newly submitted rating, and caches the results in the database so that it can return the requests faster. When the user clicks on the image giving the reputation score, he<sup>r</sup>she is given a directed graph Ž . Fig. 6 with which he<sup>r</sup>she can visualize the ratings structure used to evaluate the reputation of the user he is looking at. The global Sporas reputationŽ . values can always be calculated in real time, because of the recursive nature of its update functions.

![](/api/attachments/5ABSUJAF/fulltext/images/e05305db321df5c85023418982b87f7d5c7e28e3f35afb6a6a2dc1348045fad6.jpg)  
Fig. 6. Histos visualization. User A with reputation makes a query about the reputation of user B. The query is broadcasted across A’s network of trusted users.

The backend and the interface of the reputation server were implemented in Visual C<sup>qq</sup> and the reputation values are stored in a Microsoft SQL server. The html of MarketMaker is created on the fly using servlets. Therefore, the queries about the user’s reputations are passed from the servlet being called to the reputation database. Likewise, the submissions of fresh ratings are made through calls in the servlet code. The reputation data for different marketplaces were stored in a standalone database, so a separate table was maintained with the necessary authentication and identification information of the transactions of each marketplace.

## 9. Evaluation with simulations

To evaluate the reputation mechanisms, we applied the algorithms in four simulations. In the first simulation, we evaluate the convergence speed of the algorithm. We have 100 users with uniformly distributed real reputations. Each user starts with minimum reputation at 300, initial RD of 300 and can have a minimum RD of 30. The users are matched randomly in each period of the simulation and get rated by each other according to their actual performance. Each user’s performance is drawn from a normal distribution with a mean equal to its real reputation and a standard deviation of 100. We assume that we have reached equilibrium when the average square error of the reputation scores of users from their real reputations falls below 0.01. In this specific simulation, the system reached equilibrium after 1603 ratings, in other words after each user has made on average 16 transactions. Fig. 7 shows the reputation values for users 0, 1 and 8 over time until the average square error becomes $0 . 0 1 D ^ { 2 }$ . At the time of equilibrium, users 0, 1 and 8 with real reputations 327.1, 1458.1 and 746.8, respectively, had reached reputation values of 691.6, 1534.1 and 991.0, with RDs 116.5, 86.7 and 103.4, respectively. The equilibrium was reached after receiving 15, 21 and 18 ratings, respectively. Therefore, our system can reach equilibrium very quickly. As we can see from the results of the three users and Fig. 7, the users with high reputations are estimated with a better precision than users with low reputations.

![](/api/attachments/5ABSUJAF/fulltext/images/d70f1dd65793e4f9cadfef66c6bf9d692834aea3f1c5b70aa90e6fe48f8ee00a.jpg)  
Fig. 7. Bootstrapping. Simulation of 100 users with uniformly distributed reputations. The simulation achieves an average square error in 1603 ratings. The dotted lines around each one of the three curves show the RD of that user.

In the second simulation, we show a user who joins the marketplace, behaves reliably until he<sup>r</sup>she reaches a high reputation value and then starts abusing his<sup>r</sup>her reputation to commit fraud. Thus, the user’s ratings start dropping because of his<sup>r</sup>her unreliable behavior. During the first $1 / 3$ of his<sup>r</sup>her interactions, the user performs with a reputation of 0.8 D. During the last 2<sup>r</sup>3 of his<sup>r</sup>her interactions, the user behaves with a reputation of 0.3. The user receives ratings, which are normally distributed around his<sup>r</sup>her actual performance, with a standard deviation of 0.1. The reputations of the raters of the user are drawn from a uniform distribution with a range D. The effective number of ratings in Sporas is $\theta = 3 0$ . We plot on the same graph the reputation values that the user would have if he<sup>r</sup>she received the same ratings in a simplistic reputation system where the reputations are evaluated as the average of all the ratings given to the user, as is the case with the reputation mechanism of Amazon auctions. As we can see from the graph, although the user keeps receiving consistently lower scores for a time period twice as long his<sup>r</sup>her reputable period, he<sup>r</sup>she still preserves a reputation of 0.6 D, if he is evaluated using the averages method of Amazon.com. Hence, in this case, the user can take advantage of his<sup>r</sup>her past good ratings for a quite long time and keep deceiving people about his<sup>r</sup>her actual reliability. However, as we can see in Fig. 8, if the user is evaluated using Sporas, it takes less than 20 ratings to adjust the reputation of the user to his<sup>r</sup>her new performance.

In the third simulation, we present the effect of collusion by two users. In this experiment, both users get rated every other time by one of their friends with a perfect score. Like the previous experiment, we plot the reputations of both users evaluated on our system and on a system like Amazon’s. The actual performance of the two users is 900 and 600 Ž . out of 3000 , respectively. As we can see in Fig. 9, on the simplistic reputation system they actually manage to raise their reputations to 1781 and 1921, respectively, while with our algorithms, their reputations reflect their actual performance by letting them achieve reputation values of 619 and 960, respectively. The reputations of the other users and the ratings they submit are created the same way as in the previous experiment Fig. 8 .Ž .

![](/api/attachments/5ABSUJAF/fulltext/images/227c533db2e58ee3e5c8878679761a865d5e366566ca618e2c0886d1d680fea4.jpg)  
Fig. 8. Abuse of prior performance. The curve A, shows the computed average reputation value of a user who starts very reputable and then starts behaving as an untrustworthy person. The curve B shows the effect of the same behavior using the Sporas reputation mechanism.

![](/api/attachments/5ABSUJAF/fulltext/images/aa6002e87984cc7231dbbe8ccc46c29758637dc3b672569c744ef89d83f12bc5.jpg)  
Fig. 9. Collusion between two users. A and B collude and rate each other perfectly every other transaction. User A has a real reputation of 900 and User B a reputation of 600. With simple averages, they achieve reputations of 1921 and 1781, while with Histos, for a user who has never interacted with them before directly they achieve reputations of 960 and 619, respectively.

## 10. Evaluating Sporas on eBay user data

To evaluate the Sporas algorithm with real user data, we decided to spider the Feedback Forum of eBay, and use the actual eBay ratings with our algorithm. We spidered feedback pages for 7269 eBay users using a recursive spidering tool. We initiated the spidering process from the most recent feedback page of a random eBay user, and from there on it recursively downloaded the feedback pages of everyone who rated that user and kept going like that until we terminated the process.

The spidering tool, kept in its memory a queue of the extracted feedback URLs, and explored those URLs in a Breadth First Search manner. Due to the design of the eBay feedback forum, for many of these users we only managed to spider only a fraction of their actual feedback forum data, because the additional pages were considered one level below in the tree structure. Therefore, instead of using eBay’s summary data, we recomputed the total number of transactions, positive, neutral and negative comments, based on the data we managed to collect through the spidering process. Thus, in our calculations, we are missing some of the old data for several of our users, because the feedback pages on eBay are sorted in reverse chronological order. Each feedback page on eBay has a at most 25 comments, and our incomplete data are for users with more than one

## Joint distribution of estimator differences

![](/api/attachments/5ABSUJAF/fulltext/images/7f0d5bed1a5479c48e2e2190e2349f8de89446260e7d7dff417cda682ed73dec.jpg)  
Fig. 10. Joint distributions of estimated differences. The difference of the estimated reputations from the computed reputations, and the <sub>estimated vs. RDs and computed RDs for each one of the eBay users.</sub>ˆ

page; therefore, even without the missing data we had at least 25 ratings for each one of those users. In the evaluation process below, the effective number of observations was set to 10, so the 25 most recent ratings of the users with missing data was a good enough sample for their most recent behavior.

Since users on eBay are rated with either 1 or 0 or <sup>y</sup>1, we had to scale the ratings to a 0,1 interval so<sup>w</sup> <sup>x</sup> we replaced them with 1, 0.5 and 0, respectively. For each one of the users, we calculated the mean and the standard deviation of his<sup>r</sup>her performance in the data we have collected. Then for each one of those

Reputation comparison  
![](/api/attachments/5ABSUJAF/fulltext/images/0de4cfc3c0bce27c25c7ae23931256e46773d86c012ea97d1ebb71a6b6e16b9d.jpg)  
Fig. 11. Estimated vs. computed reputation values for the eBay users.

## Reputation Deviation comparison

![](/api/attachments/5ABSUJAF/fulltext/images/dc4f5421655c4fabead476822a7d7b438f3e86cb12a73f1b4223439cb08b8cab.jpg)  
Fig. 12. Estimated vs. computed RD for the eBay users.

users, we applied the Sporas algorithm and tried to predict the Reputation and RD in a recursive manner as described in the previous sections.

Fig. 10 shows the joint distribution of $\hat { R } { - } \overline { { R } }$ \$and ${ \widehat { R D } } { - } { \overline { { R D } } }$ , where $\hat { R }$ is the Reputation value and $\overline { { R D } }$ the Reputation Deviation estimated using Sporas, and $\overline { { R } }$ is the average Reputation value and $\overline { { R D } }$ the Reputation Deviation computed from the sampled transactions of the same user. Fig. 11 shows \$ $\hat { R }$ vs. $\overline { { R } }$ and Fig. 12 shows $\widehat { R D }$ vs. RD.

As we can see from Figs. 10 and 11, the Sporas algorithm, in general, underestimates the sampled Reputation of a user. This is clearly seen in Fig. 11, where we can see that users with the same sampled reputation ${ \overline { { R } } } ,$ end up having different estimations for ${ \hat { R } } .$ This difference depends on how recently the user committed his<sup>r</sup>her transactions with low scores. Therefore, the time dependency of our recursive estimation, ensures that users who have been trustworthy in their latest transactions, rather than their earliest ones, will have higher scores than others who performed well in the past, but started getting low feedback scores lately, even if their linear average is exactly the same.

In addition, as we can see from Figs. 10 and 12, the Sporas algorithm, in general, underestimates the sampled RD of a user, compared to the RD computed from the sample of the user’s transactions. We expected to observe this result, because the recursive estimation of the RD discounts older deviations and tries to make its predictions based on the most recent performance. However, in some cases we do estimate a larger RD than the one observed over the whole sample. This happens when the user exhibits a varying performance during his<sup>r</sup>her most recent transactions rather than his<sup>r</sup>her earlier ones. Since we are trying to make our predictions based more on the recent data, the overestimation of the RD in these cases is the desired behavior.

## 11. Conclusion

Collaborative filtering methods have been around for some years now, but they have focused on content rating and selection. We have developed two collaborative reputation mechanisms that establish reputation ratings for the users themselves. The proposed solutions are able to face all the problems and fulfill all the desiderata described in Section 3. Incorporating reputation mechanisms in online communities may induce social changes in the way users participate in the community.

## References

<sup>w</sup> <sup>x</sup> 1 Amazon.com Auctions. http:<sup>rr</sup>auctions.amazon.com.

<sup>w</sup> <sup>x</sup> 2 A. Chavez, P. Maes, An agent marketplace for buying and selling goods,Proceedings of the First International Conference on the Practical Application of Intelligent Agents and Multi-Agent Technology PAAM ’96 . London, UK, April, Ž . 1996.

<sup>w</sup> <sup>x</sup> 3 Better Business Bureau. http:<sup>rr</sup>www.bbb.org.

<sup>w</sup> <sup>x</sup> 4 Bizrate. http:<sup>rr</sup>www.bizrate.com.

<sup>w</sup> <sup>x</sup> 5 The Cyprus List. http:<sup>rr</sup>kypros.org<sup>r</sup>lists<sup>r</sup>cyprus.

<sup>w</sup> <sup>x</sup> 6 eBay. http:<sup>rr</sup>www.ebay.com.

<sup>w</sup> <sup>x</sup> 7 A.E. Elo, The Rating of Chessplayers, Past and Present, Arco Publishing, New York, 1978.

<sup>w</sup> <sup>x</sup> 8 J. Donath, Identity and deception in the virtual community, in: P. Kollock, M. Smith Eds. , Communities in Cyberspace, Ž . Routledge, London, 1998.

<sup>w</sup> <sup>x</sup> 9 Fair Isaak. http:<sup>rr</sup>www.fairisaac.com.

<sup>w</sup> <sup>x</sup> 10 L. Foner, Yenta: a multi-agent, referral based matchmaking system,First International Conference on Autonomous Agents Ž . Agents ’97 , Marina del Rey, California, February, 1997.

<sup>w</sup> <sup>x</sup> 11 E. Friedman, P. Resnick, The social cost of cheap pseudonyms: fostering cooperation on the internet, Proceedings of the 1998 Telecommunications Policy Research Conference, 1998.

<sup>w</sup> <sup>x</sup> 12 S. Garfinkel, PGP: Pretty Good Privacy, O’Reilly and Associates, 1994.

<sup>w</sup> <sup>x</sup> 13 M.E. Glickman, Paired Comparison Models with Time-Varying Parameters, PhD Thesis, Harvard University, May 1993.

<sup>w</sup> <sup>x</sup> 14 R. Khare, A. Rifkin, Weaving a web of trust, World Wide Web Journal 2 3 1997 77–112, summer.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 P. Kollock, The production of trust in online markets, in: E.J. Lawler, M. Macy, S. Thyne, H.A. Walker Eds. , AdvancesŽ . in Group Processes vol. 16 JAI Press, Greenwich, CT, 1999.

<sup>w</sup> <sup>x</sup> 16 H. Madsen, J. Holst, Lecture Notes in Non-linear and Nonstationary Time Series Analysis, IMM, DTU,1998.

<sup>w</sup> <sup>x</sup> 17 S.P. Marsh, Formalising Trust as a Computational Concept, PhD Thesis, University of Stirling, April 1994.

<sup>w</sup> <sup>x</sup> 18 OnSale Exchange. http:<sup>rr</sup>www.onsale.com<sup>r</sup>exchange.htm.

<sup>w</sup> <sup>x</sup> 19 J.M. Reagle Jr., Trust in a Cryptographic Economy and Digital Security Deposits: Protocols and Policies, Master Thesis, Massachusetts Institute of Technology, May 1996.

<sup>w</sup> <sup>x</sup> 20 Recreational Software Advisory Council: http:<sup>rr</sup>www. rsac.org<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 21 P. Resnick, N. Iacovou, M. Suchak, P. Bergstrom, J. Riedl, GroupLens: an open architecture for collaborative filtering of netnews,Proceedings of ACM 1994 Conference on Computer Supported Cooperative Work, Chapel Hill, NC,1994, pp. 175–186.

<sup>w</sup> <sup>x</sup> 22 D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning internal representations by error propagation,Parallel Distributed

Processing, in: D.E. Rumelhart, J.L. McClelland Eds. ,Ž . Foundations vol. 1 MIT Press Bradford Books, Cambridge MA, 1986, pp. 318–362.

<sup>w</sup> <sup>x</sup> 23 U. Shardanand, P. Maes, Social information filtering: algorithms for automating ‘word of mouth’,Proceedings of the CHI-95 Conference, Denver, CO, ACM Press, May,1995.

<sup>w</sup> <sup>x</sup> 24 D. Wang, Market Maker: an Agent-Mediated Marketplace Infrastructure, MEng Thesis, Massachusetts Institute of Technology, May, 1999.

<sup>w</sup> <sup>x</sup> 25 W. Mike, The role of trust and security mechanisms in an agent-based peer help system, workshop in deception, fraud and trust in agent societies,Third International Conference on Autonomous Agents Agents ’99 , Seattle, WA, May 1–4,Ž . 1999.

## Biographies

Giorgos Zacharia is a co-founder and Chief Scientist of Open Ratings, Inc. and a Telecom Italia Fellow and doctoral candidate at MIT Media Laboratory’s Software Agents Group on leave .Ž . His research focuses on reputation mechanisms, dynamic pricing and negotiation strategies for ecommerce. He holds an MS from the MIT Media Laboratory, a BS in Mathematics and a BS in Computer Science with a minor in Economics, from the Massachusetts Institute of Technology MIT . He was a FulbrightŽ . scholar throughout his undergraduate studies.

Alexandros Moukas is a co-founder of Frictionless Commerce and an AT&T Fellow and doctoral candidate at MIT Media Laboratory’s Software Agents Group on leave. He holds a BS degree inŽ . Business Administration from the American College of Greece, an MS degree in Artificial Intelligence from the University of Edinburgh, and an MS degree from MIT. Moukas has published more than 25 journal and referred conferences articles and has served as a co-chair in the Agent-mediated Electronic Commerce AmEC98Ž and 99 workshops held in Korea during ICEC-98 and Stock-. Ž . holm during IJCAI-99 .Ž .

Pattie Maes is an Associate Professor at MIT’s Media Laboratory, where she founded and directs the Software Agents Group, and is principal investigator of the e-markets Special Interest Group. She currently holds the Sony Corporation Career Development Chair. Previously, she was a visiting Professor and a Research Scientist at the MIT Artificial Intelligence Laboratory. She holds a Bachelor’s degree and PhD degree in Computer Science from the Vrije Universiteit Brussel in Belgium. Her areas of expertise are Artificial Intelligence, Artificial Life, Human Computer Interaction, Computer Supported Collaborative Work, Information Filtering and Electronic Commerce.
