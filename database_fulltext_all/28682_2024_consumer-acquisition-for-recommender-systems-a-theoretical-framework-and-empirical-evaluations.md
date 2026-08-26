---
otero_id: 28682
otero_key: "2NAG6CY8"
title: "Consumer Acquisition for Recommender Systems: A Theoretical Framework and Empirical Evaluations"
authors: "Xuan Bi; Mochen Yang; Gediminas Adomavicius"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.1229"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Consumer Acquisition for Recommender Systems: A Theoretical Framework and Empirical Evaluations

Xuan Bi,<sup>a</sup> Mochen Yang,<sup>a,</sup>\* Gediminas Adomavicius<sup>a</sup>

<sup>a</sup> Information and Decision Sciences, Carlson School of Management, University of Minnesota, Minneapolis, Minnesota 55455 \*Corresponding author

Contact: xbi@umn.edu, https://orcid.org/0000-0002-4683-1411 (XB); yang3653@umn.edu, https://orcid.org/0000-0001-5101-9041 (MY); gedas@umn.edu, https://orcid.org/0000-0001-5251-5098 (GA)

Received: October 6, 2021 Revised: July 10, 2022; December 15, 2022; March 21, 2023 Accepted: April 10, 2023 Published Online in Articles in Advance: May 15, 2023

https://doi.org/10.1287/isre.2023.1229

Copyright: © 2023 INFORMS

Abstract. We consider a marketplace where a recommender system provider (the firm) offers incentives to acquire prospective consumers by leveraging information that a market intermediary collects about these consumers. We investigate a model of consumer acquisition that incorporates several factors affecting acquisition decisions, including the value that a consumer contributes to the recommender system, the cost of participation to the consumer (e.g., privacy loss), and the value that a consumer can derive from the system due to network externality created by existing consumers. Our model is dynamic in nature, where the firm iteratively decides the next acquisition target based on previously realized acquisition outcomes. We propose flexible data-driven procedures to estimate some of the key parameters in the model using consumers’ data collected by the market intermediary, for example their historical consumption data or the consumption data of other similar consumers. We also design an algorithm to compute the dynamic acquisition sequence and the corresponding incentives to offer. We conduct simulation-based empirical evaluations on two canonical recommendation tasks: movie recommendation based on numerica ratings and product offer recommendation based on browsing (clicking) behaviors and benchmark our acquisition model with random acquisition sequences with respect to (i) firm utility, (ii) recommender system performance, and (iii) consumer surplus. We find nuanced relationships between the firm’s choice of incentive strategies and acquisition outcomes. Specifically, neither a constant strategy (setting the same incentive for all consumers) nor a fully greedy strategy (extracting all cumulative network externality) is optimal on all acquisition outcomes. Under a moderately greedy strategy, where the firm only partially extracts the cumulative network externality from consumers, the dynamic acquisition sequence can outperform random sequences on three acquisition outcomes simultaneously. Our work contributes a novel theoretical framework, practical insights, and design artifacts to facilitate effective consumer acquisition in recommender systems.

History: Giri Kumar Tayi, Senior Editor; Maytal Saar-Tsechansky, Associate Editor. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2023.1229.

Keywords: consumer acquisition • recommender systems • network externality • personalization • algorithm design

## 1. Introduction

Personalization technologies such as recommender systems play an increasingly important role in informing the consumption decisions for a variety of products and services (Adomavicius and Tuzhilin 2005). To build a successful recommender system, having a sufficient number of consumers (with valuable data) is indispensable. Real-world recommender systems offered by companies such as Netflix, Spotify, and Amazon all rely on large-scale and fine-grained data to learn consumer preferences and make useful recommendations (Gomez-Uribe and Hunt 2015, Smith and Linden 2017). Meanwhile, there are extensive debates among researchers, practitioners, and regulators over the issues of data privacy, ownership, and how consumers should be acquired in general (Acquisti et al. 2015, 2016; Mohallick et al. 2018).

Accordingly, market mechanisms (e.g., “data markets”) have been proposed where service providers (e.g., recommender system providers) can potentially offer incentives to acquire consumers and encourage their participation (Kleinberg et al. 2001, Dandekar et al. 2014, Spiekermann et al. 2015b, Nget et al. 2017). The idea is intuitively appealing, and a key prerequisite to creating such a marketplace is having a systematic consumer acquisition incentive strategy that is based on the value of consumer participation to the service provider. Although many existing data markets adopt a uniform incentive strategy (e.g., setting a flat price to acquire each consumer), it may not be optimal because different consumers likely have different values to the service provider.

We study this value-driven consumer acquisition problem in the specific context of recommender systems. We consider a marketplace with three types of players: the recommender system provider (the “firm”), the prospective consumers, and the market intermediary. The firm invites consumers to participate (e.g., sign up to use the system) by sending acquisition offers with certain incentives. Each consumer decides whether to join the system by weighing the benefits and costs of participation. The market intermediary mediates the information exchanges: It collects consumer data and provides the firm with information (e.g., estimated consumer values) to make acquisition decisions.

The problem of value-driven consumer acquisition is nontrivial, as it depends on joint consideration of several factors. First, consumer participation generates value to the firm (e.g., improving the quality of the recommender system and creating advertising revenue), which needs to be compensated for. Second, consumers also derive value from having access to the recommender system (e.g., receiving beneficial recommendations and better consumption experiences), which adds to their incentive to participate. Third, there are costs associated with consumer participation (e.g., privacy loss due to data disclosure or opportunity cost of using a particular service). Previous research in similar contexts typically considers only a subset of these factors as the basis for consumer acquisition, for example, quantifying the value of users consumption data to a recommender system based on Shapley value (Kleinberg et al. 2001) or based on the privacy cost of participation (Dandekar et al. 2014). In contrast, we propose a consumer acquisition model that simultaneously accounts for all three factors, thereby offering a more comprehensive theoretical framework.

Two important features of our model add to its practical utility. First, the model explicitly considers the sequence of consumer acquisitions. The value that a specific consumer contributes to, and derives from, the recommender system can vary depending on when the consumer joins the system. For instance, having an additional consumer may result in large improvement of the recommender system if there is only a small number of consumers in the system. Meanwhile, a consumer may naturally want to participate in a recommender system with many existing consumers than one with few, by virtue of network externality. Therefore, the firm may benefit from acquiring prospective consumers in a particular order (rather than randomly). Second, because the firm generally does not have perfect information of the consumers $( \mathrm { e . g . }$ , individuals’ participation costs are private information), any predetermined acquisition sequence may not be precisely realized. Therefore, our proposed model dynamically adjusts whom to acquire next, based on the realized previous acquisition outcomes.

To solve the dynamic acquisition model, we first develop a data-driven procedure that leverages consumers’ historical consumption data (potentially gathered by the market intermediary from a different recommendation platform) to estimate the values of their participation to the quality of a recommender system. If consumption data of the prospective consumers are unavailable, the procedure instead relies on an external set of consumers whose consumption records are available to the intermediary (e.g., anonymous consumers in a public data set) for value estimation, then predict the value of each prospect via supervised machine learning approaches based on observed attributes $( \mathrm { e . g . } ,$ demographics). We also discuss how the firm can set other parameters of the acquisition model that may not be estimated from consumption data. Following parameter estimations, we design an algorithm to compute the (dynamic) acquisition sequence and acquisition incentives under a given incentive strategy chosen by the firm. We consider a family of incentive strategies with varying levels of “greediness,” ranging from a constant strategy (setting a uniform incentive for all consumers) to a fully greedy strategy (similar to first-degree price discrimination), and examine their impact on acquisition outcomes.

We empirically evaluate the model by applying it on two distinct real-world data sets, namely the Movie-Lens 100K data (Harper and Konstan 2015) and the Kelkoo consumer data (Sidana et al. 2017). The two data sets differ in data sparsity and consumer types. They also represent two canonical types of recommen dation tasks: The former predicts movie ratings (on an ordinal or continuous scale), whereas the latter predicts consumers’ interactions with discount offers (click or no click, on a binary scale). Evaluations are carried out under two different schemes. The first scheme evalu ates how consumers’ historical consumption data can inform the focal firm’s acquisition decisions. The sec ond scheme instead assumes that no consumption data for the prospective consumers are available, and tests how auxiliary information (e.g., demographics) can be used for acquisition. Under both datasets and evaluation schemes, we compare the performance of our model against a random acquisition benchmark on three outcomes: (i) firm utility, (ii) recommender system performance, and (iii) consumer surplus. We find a nuanced relationship between incentive strategies and acquisition outcomes. As the firm sets increasingly greedy incentives (i.e., extracts larger portions of network externality), its utility grows at the expense of consumer surplus and recommender system performance. Under the fully greedy strategy, specifically, the firm accumulates high utility as it extracts all network externality from acquired consumers, but doing so also reduces the probability of successful acquisition, which leads to fewer acquired consumers and lower recommender system performance. A moderately-greedy strategy turns out to outperform the random acquisition benchmark on all three acquisition outcomes.

We conduct several additional evaluations to demonstrate the robustness of our dynamic acquisition model with respect to different parameter specifications, an alternative deep learning–based recommender system algorithm, as well as a different acquisition setting with arrivals of organic consumers. We also explore how the acquisition model affects recommendation diversity (i.e., another important consideration of recommendation performance, in addition to accuracy), and find that the accuracy-driven dynamic consumer acquisition does not inadvertently lead to a substantial reduction of recommendation diversity. Furthermore, we evaluate our model under cross-domain settings using an Amazon Review data set, where consumers’ historical consumption data from a different domain are used to inform the acquisition decisions in the focal domain to understand the cross-domain performance of our approach.

Our work makes several notable contributions. First, we present a comprehensive theoretical framework of consumer acquisition that simultaneously accounts for multiple tradeoffs faced by the consumers and the recommender system provider. The proposed dynamic acquisition model jointly considers consumer value, network externality, and participation cost to make acquisition decisions. Second, our empirical evaluations of different incentive strategies reveal informative trade-offs that are practically relevant for recommender system providers. Interestingly, a fully greedy strategy generally does not result in the best-performing recommender system, and a less aggressive strategy can achieve more advantageous acquisition outcomes. Third, the data-driven parameter estimation procedures and the dynamic acquisition algorithm represent useful design artifacts that can facilitate successful deployment of the acquisition model in practice. Finally, our work gives rise to a number of future research directions in enhancing the robustness and practicality of dynamic consumer acquisition.

## 2. Literature Review

Our work is informed by and contributes to several bodies of literature, which we briefly discuss in this section.

## 2.1. Data Markets

Data markets are marketplaces where consumers’ personal information and data can be disclosed in exchange for proper compensation (Kleinberg et al. 2001, Spiekermann et al. 2015b). On the one hand, personal data are valuable and indispensable for businesses and organizations in digital economy (Heimbach et al. 2015, Roeber et al. 2015, The Economist 2017). On the other hand, consumers and regulators are becoming increasingly cognizant about data privacy and ownership (Goldfarb and

Tucker 2011, Mohallick et al. 2018). Market mechanisms that facilitate transactions over data are regarded as a viable solution to this tension.

Much of the research on data markets has primarily focused on the issues of privacy and trust, which are at the heart of data market design and adoption (Spiekermann et al. 2015a). Consumers are generally willing to participate in data markets if they perceive that their data are protected and their privacy loss from disclosing the data are properly compensated, and that the organizations can be trusted not to use the acquired data in unintended ways, for example, sharing data with a third-party outside the terms of exchange (Roeber et al. 2015). Accordingly, a number of studies have focused on economic or technical solutions to protect privacy and enhance trust, such as pricing the individual data based on privacy loss (Dandekar et al. 2014, Li et al. 2014, Gkatzelis et al. 2015) and developing encryption, privatization, and anonymization techniques (Jain et al. 2016).

In addition to privacy and trust considerations, a prerequisite for operating and clearing data markets is to have a valuation scheme that properly quantifies the value of individual data for both consumers and firms. Data valuation is a nontrivial task for at least two impor tant reasons. First, the value of data tends to be context dependent (Berthold and Bo¨hme 2010), in that the same data can have very different value for different stakeholders and for different applications. Second, when the value of data has to be solicited from its owner, such self valuation may not be reliable as individuals’ judgments are prone to biases and manipulations. For example, Acquisti et al. (2013) find that individuals assign drastically different values to the worth of their private information when asked to consider (i) how much they would accept to disclose their information versus (ii) how much they would pay to protect their information. Therefore, pricing schemes that rely on self-reported pri vacy loss may not capture the true value of data. Because of these difficulties in developing context-specific personalized pricing schemes, many general-purpose data markets adopt a uniform batch pricing method, essentially treating data from different individuals as identical.<sup>1</sup>

In this paper, we propose a model of consumer acquisition in the specific context of recommender systems. Instead of trying to come up with a generic valuation of consumer data solely based on privacy loss, we consider the value of consumer participation in the recommender systems. In particular, we ask: how much would a consumer be willing to accept or pay to participate in a recommender system, deriving value from accessing the system and bearing the cost of participation at the same time? This broader view of valuation that we take, in line with the work of Kleinberg et al. (2001), has been under-represented in the privacy-centric data valuation literature.

## 2.2. Network Externality

A unique characteristic of our work is that we consider not only what consumers give up by participating in a recommender system, but also what they gain from having access to the system. Similar to many other online platforms, the benefits for consumers to join a recommender system are substantially affected by network externality.

When the utility that a consumer derives from using a product also depends on the number of other consumers using it, the consumption demonstrates “network externality” (Katz and Shapiro 1985). The magnitude of network externality plays a critical role in determining the adoption of new technologies (Katz and Shapiro 1986, Kauffman et al. 2000, Van Alstyne and Parker 2017). If the network externality is sufficiently strong, new consumers are drawn to the product that has gathered a critical mass of existing consumers and can be unwilling to switch even when offered a superior product, thereby creating a “winner-take-all” market outcome for the first-mover product (Katz and Shapiro 1986). Not surprisingly, firms are highly motivated to take advantage of network externality, by strategically offering some products for free to attract consumers for other premium products (Parker and Van Alstyne 2005) or by licensing certain technologies without charge to benefit complementary technologies (Economides 1996).

We expect network externality to be an important factor in consumers’ decisions to use recommender systems. A recommender system with a larger current consumer base tends to be more attractive to prospective consumers. This is because the value that a consumer can derive from having access to a recommender system depends on the quality of recommendations for that consumer, which increases if the recommender system is built on a larger and more diverse set of consumption data (Brynjolfsson et al. 2011, Adomavicius and Zhang 2012). In other words, the acquisition of a given consumer can in fact exert positive externalities to future potential consumers. We explicitly account for such network externality in our consumer acquisition model.

## 2.3. Recommender Systems

The rich literature of recommender systems, although traditionally focusing on the technical aspects of designing and evaluating recommender system algorithms, also increasingly concerns the economic and behavioral aspects. For example, Xiao and Benbasat (2007) evaluate how the use and characteristics of recommender systems influence consumers’ decision making, Hosanagar et al. (2014) study whether recommender systems fragment online consumer populations, Komiak and Benbasat (2006) and Panniello et al. (2016) investigate how recommendations affect consumers’ trust, Adomavicius et al. (2018) explore whether and how consumers willingness to pay can change based on the recommendations they receive, and Lee and Hosanagar (2020) investigate how recommender systems are moderated by product attributes and reviews. We contribute to this literature by studying the impact of different incen tive strategies on outcomes of consumer acquisition.

The benchmark recommender systems used in our work rely on collaborative filtering, a popular and widely adopted class of recommendation techniques. The basic principle of collaborative filtering is to make recommendations for a focal consumer based on consumers with similar behaviors. A large variety of collaborative filtering methods have been developed, including singular-value decomposition-based approaches (Funk 2006, Koren et al. 2009), factorization machines (Rendle 2012, Juan et al. 2016), nearest-neighbor-based approaches (Resnick et al. 1994, Breese et al. 1998, Sarwar et al. 2001, Bell and Koren 2007), restricted Boltzman machines (Salakhutdinov et al. 2007), and hidden Markov models (Sahoo et al. 2012). In the empirical evaluation of our consumer acquisition model, singular value decomposition and binary matrix factorization are, respectively, used in two common recommendation scenarios: explicit feedback (numeric movie rating) and implicit feedback (binary product clicking). Our findings are also replicated under a deep learning–based recommendation algorithm known as neural collaborative filtering (He et al. 2017).

## 2.4. Active Learning

Our consumer acquisition model allows a recommender system provider to identify valuable prospective consumers whose participation can most effectively increase the provider’s utility. From this perspective, our work is connected to, but distinct from, the literature of active learning.

One prevalent type of active learning refers to a class of machine learning strategies that can actively query an oracle (e.g., a human) to label data instances to effectively improve their predictive performance (Settles 2009). As an example, uncertainty sampling is a particular type of active learning strategy, where the learning algorithm queries an oracle (e.g., a human labeler) for labels of the data instances that it is least confident about (Lewis and Gale 1994). Because of this curated learning process, active learning has the potential to achieve good predic tive performance with less training data (Settles 2009). Beyond label acquisition, there is a rich set of variations in active learning that more broadly deal with information acquisition, such as feature-value acquisition (Melville et al. 2005, Saar-Tsechansky et al. 2009), decision-centric active learning (Saar-Tsechansky and Provost 2007), and collaborative information acquisition (Kong and Saar-Tsechansky 2014).

Another relevant stream of literature investigates the incentive problems involved in active learning. Research in this stream goes beyond the conventional active learning setup where oracle labelers are always available to provide ground truths without cost (or at a fixed cost), and instead considers more realistic settings where different labelers can have different degrees of quality (e.g., ability to provide accurate labels) and varying costs (Donmez and Carbonell 2008; Huang et al. 2017; Wang et al. 2017; Zhang et al. 2018, 2019; Geva et al. 2019; Sheng and Zhang 2019; Gao and Saar-Tsechansky 2020). For example, Huang et al. (2017) designed an algorithm to select the most cost-effective labeler for a data instance based on a joint consideration of the quality and cost of a labeler as well as the usefulness of the data instance $( \mathrm { i . e . , }$ if labeled, how much performance improvement can be expected). Geva et al. (2019) further created an adaptive labeling payment scheme that select the most costeffective payment level for each label.

Active learning has also been applied in the context of recommender systems. Several studies seek to use active or online learning techniques to improve recommendation performance (Huang 2007, Rubens et al. 2011, Deodhar et al. 2017, Liebman et al. 2019). For instance, Huang (2007) discussed a rating acquisition problem and proposed an active learning algorithm to query specific ratings that most effectively improve predictive performance. Our work is consistent with the spirit of incentive-aware active learning, in that we try to acquire heterogeneous consumers with differential values and costs, with the objective to maximize firm utility.

However, our work differs from this literature in several important ways. First, in our model, the contribution of a consumer’s participation to the firm is not solely determined by the performance improvement it brings to the recommender system. Rather, it is a function of several factors, including other sources of utility it can generate and the network externality it creates. The acquisition decisions are collectively affected by all these factors. In other words, our model is inherently different from a performance-driven machine learning model. Second, the cost of each labeler is typically assumed to be known in cost-aware active learning (Donmez and Carbonell 2008, Huang et al. 2017, Gao and Saar-Tsechansky 2020), whereas the participation cost of each individual consumer is private information and fundamentally unknown to the firm. Such uncertainty gives rise to a family of incentive strategies (which we discuss later) with nuanced impact on acquisition outcomes. Third, in our market-based consumer acquisition problem, acquiring a consumer affects the willingness to participate for remaining prospective consumers via cumulative network externality. Such an externalityinduced dependency among consumers has unique implications on acquisition outcomes, for example, it is possible to simultaneously achieve higher firm utility and consumer surplus (two often competing objectives) under some incentive strategies. These market dynamics are not fully captured in a typical active learning problem.

## 3. Model of Dynamic Consumer Acquisition

We consider a market with one firm and N prospective consumers indexed by $s \in \{ 1 , \ldots , N \}$ . The firm offers a recommender system and extracts value from consumer participation. The consumers, upon participation, derive value from having access to the recommender system, but also experience the cost of participation (e.g., due to opportunity cost or privacy risk).

Personal information of the prospective consumers is typically needed to gauge the value of these consumers to the firm and to make informed acquisition decisions. However, the firm typically does not have access to this external information, and we therefore consider a market intermediary that mediates the information exchanges (i.e., an “infomediary”). The intermediary collects consumers’ personal information, estimate their values to the focal firm, and sells the list of consumers (e.g., their contact information) and their estimated values to the focal firm for a service fee. The firm then reaches out to the consumers in a particular order (we discuss how the order is determined later) and invites them to join and use the recommender system by offering certain incentives (e.g., the firm may send a personalized invitation link with a signing bonus to a prospective consumer). Finally, each individual consumer decides whether to join by weighing the benefits and costs of participation. We visualize this market structure in Figure 1.

Such a market structure is common in the marketing (e.g., direct mail) industry, where data vendors often serve as intermediaries that collect and curate con sumer information, build predictive machine learning models for their business clients (e.g., retailers), and then sell the lists of consumers (often ranked based on predicted probability of purchase, a measure of consumer value) to the clients. The client firms then reach out to these prospective consumers and try to acquire them, for example, by sending direct mail pieces that contain coupons or discount codes. The consumers, upon receiving the acquisition offers, decide whether to purchase the firms’ products or services. Several examples of such intermediaries and their services are listed in Online Appendix A. We adopt this general market structure and focus on designing and evaluating different acquisition strategies for recommender systems.<sup>2</sup>

## 3.1. Decisions of Each Market Player

Next, we lay out the decisions made by each market player in detail, starting with the market intermediary. Suppose that the market intermediary possesses information of each consumer $s \in \{ 1 , \ldots , \dot { N } \}$ in the form of a feature vector X(s) that may contain various user characteristics, interests and preferences, past transactions, and online traces. These features may have been collected and compiled from multiple sources, for example, public records, credit agencies, social media, and other online platforms (Neumann et al. 2019). In our context, the intermediary uses X(s) to estimate the value of consumer s, v(s), to the focal firm’s recommender system. Details about the estimation of v(s) are discussed in Section 4.1. Then, the intermediary sells the consumer list (e.g., the contact information of consumers) and their

Figure 1. (Color online) Market Structure  
![](/api/attachments/2NAG6CY8/fulltext/images/a1032be47bd2fefe500825d3cad4e7449a69e11bd26dee53241bd82d3607ba1a.jpg)  
Note. The market intermediary collects information of prospective consumers (step 1), estimates consumer values and sells them to the firm for a service fee (step 2), and the firm then reaches out to acquire the consumers (step 3).

For the focal firm (i.e., the recommender system provider), we consider two mechanisms through which it benefits from the acquisition of a consumer. First, acquiring a consumer can improve the quality of the firm’s recommender system, because the system can learn from the consumer’s activities and interactions (e.g., the ratings generated by the consumer). This is reflected in the value v(s) of consumer $s ,$ which the firm procures from the market intermediary. Meanwhile, a consumer’s actual value contribution to the recommender system also depends on when this consumer joins the system. To model this, we weigh the system values by a set of order-specific parameters. In particular, if consumer s joins the recommender system as the ith consumer, then the weighted value of this consumer is modeled as $\alpha _ { i } v ( s )$ . In the case where $\alpha _ { i } \in ( 0 , 1 ]$ and decreases in $i ,$ this models the observation that, for a given consumer, joining later generally brings smaller value to the recommender system than joining earlier. Second, in addition to the direct benefits associated with the recommender system, the firm can also generate value from consumers via other venues (potentially unrelated to the recommender system), such as showing ads to consumers or selling products/services to them.

We denote it as h(s) for consumer s, and it is not subject to order-related weighting. The firm determines the value of h(s) based on its domain expertise or internal data; for example, it can retrieve the average ad revenue of its existing consumers and assign it to h(s) for all s. The firm can also assign more granular values of h(s) by querying the intermediary for relevant information on consumer s; for example, it can assign the average ad revenue for different occupations or income levels. To differentiate the two types of consumer values, we refe to v(s) as the system value of consumer s and to h(s) as the consumer’s value potential.<sup>4</sup>

At the same time, to incentivize consumer participation, the firm pays p(s) for consumer s as the acquisition offer. We allow p(s) to be positive, zero, or even negative, to represent the possible scenarios where a consumer is willing to participate with compensation, without compensation, or even pay to participate (if the benefit of participation is sufficiently high).

Finally, from the consumers’ perspective, the primary benefit of participation is to gain access to the recommender system, which can be valuable for their future consumption decisions. The value of the recommender system to a consumer, in turn, depends on the existing consumers that are already using the system. We use function w(s) to model the value that a participating consumer s brings to other consumers who are yet to participate. This value captures the network externality (Katz and Shapiro 1985, 1986; Parker and Van Alstyne 2005) generated by consumer s. It is reasonable to expect that acquiring a consumer with higher system value (i.e., higher v(:)) benefits other consumers more than one with lower system value. Therefore, we write $w ( s ) = \gamma v ( s )$ , where $\gamma \geq 0$ is a scaling parameter that controls the dependency of w(s) on v(s). Similar to the firm’s decision problem, we weigh w(s) by a set of order-specific parameters $\beta _ { i } ,$ such that, for consumer s joining as the ith consumer, the actual network externality generated is modeled as $\beta _ { i } w ( s )$

For consumer s who is deciding whether to participate, the value that s can derive from accessing the recommender system is associated with the cumulative network externality generated by all consumers who have participated before s. In addition, consumer s also receives incentive of $p ( s )$ from the firm and experiences a cost of c(s) for participation. The cost is private information of the focal consumer, and may be associated with privacy loss from revealing one’s data and opportunity cost of using one firm’s service. We also assume that each consumer rationally makes a decision of whether to participate based on a comparison between the benefit and cost of participation.

## 3.2. Dynamic Consumer Acquisition Mode

We now formally write down the dynamic consumer acquisition model. Intuitively, the firm’s objective is to acquire consumers in a particular sequence to maximize its total utility. If the firm had complete knowledge of consumers’ willingness to participate, it could set the acquisition incentives accordingly and, as a result, realize the globally optimal acquisition sequence. However, this is hardly realistic because a specific consumer’s cost of participation (which is a determinant of willingness to participate) is private information and not available to the firm. Therefore, rather than treating consumer acquisition as a (global) optimization problem over all possible acquisition sequences, we instead consider a dynamic acquisition process. Specifically, the firm reaches out to individual consumers in a particular order, and sequentially decides whom to acquire next based on the realized acquisition outcomes of the previous consumers.

Suppose the firm has made n acquisition attempts so far and acquired z consumers $( 0 \bar { \leq } z \leq n \leq N )$ . Denote T(n) as the “attempted sequence”, that is, the sequence of consumers that the firm has attempted acquiring that has cardinality $| T ( n ) | = n$ . Denote S(n) as the “realized sequence,” that is, the sequence of consumers who have accepted the firm’s acquisition offers, which has cardinality $| S ( n ) | = z .$ . We further write $S ( n ) = \langle s _ { 1 } , \ldots , s _ { z } \rangle , i \neq$ $j \Longleftrightarrow s _ { i } \neq s _ { j } , { } ^ { 5 }$ and $S ( n ) \subseteq T ( n ) \subseteq \{ 1 , \dots , N \} . ^ { 6 }$ Finally, for notational completeness, let $T ( 0 ) = S ( 0 ) = \langle \rangle$ to be an empty sequence. Given the realized sequence S(n), the firm’s utility can be expressed as

$$
\begin{array}{l} U _ {F} (S (n)) \\ = \underbrace {\sum_ {s _ {i} \in S (n)} \alpha_ {i} v (s _ {i})} _ {\text { Utility from Recommender System}} + \underbrace {\sum_ {s _ {i} \in S (n)} h (s _ {i})} _ {\text { Value Potentials }} - \underbrace {\sum_ {s _ {i} \in S (n)} p (s _ {i})} _ {\text { Incentives}}. \end{array}\tag{1}
$$

Then, from the set of remaining consumers $\{ 1 , \dots , N \} \backslash$ $T ( n )$ , the firm picks the next one to attempt acquiring based on the following one-step look-ahead maxi mization:

$$
s ^ {*} = \underset {s \in \{1, \ldots , N \} \setminus T (n)} {\arg \max} U _ {F} (S (n) \oplus s) - U _ {F} (S (n)),\tag{2}
$$

where $S ( n ) \oplus _ { S } \doteq \langle s _ { 1 } , \ldots , s _ { z } , s \rangle$ , that is, the additional consumer is appended to the end of S(n). In other words, the firm sequentially picks its acquisition target in a dynamic fashion by maximizing the marginal utility increase that would be achieved with the next con sumer given the realized acquisition sequence. The consumer surplus of $s ^ { * }$ , that is, of the consumer that maximizes marginal utility given S(n), can be written as

$$
\begin{array}{l} U _ {C} (s ^ {*}) = \underbrace {\sum_ {s _ {i} \in S (n)} \beta_ {i} w (s _ {i})} _ {\text { Utility   from   Recommender   System   (Network   Externality) }} \\ + \underbrace {p (s ^ {*})} _ {\text { Incentive }} - \underbrace {c (s ^ {*})} _ {\text { Cost   of   Participation }}. \end{array}\tag{3}
$$

The consumer would accept the acquisition offer and participate in the recommender system if $U _ { C } ( s ^ { * } ) \geq 0$ and would deny the offer otherwise.<sup>7</sup> Accordingly, the attempted sequence would be updated as $T ( \bar { n } + 1 ) =$ $T ( n ) \bar { \oplus } s ^ { * } ,$ , and the realized acquisition sequence would be updated as

$$
S (n + 1) = \left\{ \begin{array}{l l} S (n) \oplus s ^ {*} & \text {if} U _ {C} (s ^ {*}) \geq 0 \\ S (n) & \text {if} U _ {C} (s ^ {*}) <   0. \end{array} \right.\tag{4}
$$

## 3.3. Incentive Strategy

The firm’s incentive strategy, that is, how it sets the incentive p(s) for consumer s, clearly plays an important role in determining the acquisition outcomes. Based on Equation (3), the marginal incentive that extracts all consumer surplus for a given consumer s is $p ( s ^ { * } ) = c ( s ^ { * } )$ $\textstyle - \sum _ { s _ { i } \in S ( n ) } { \bar { \beta _ { i } } } w ( s _ { i } )$ : However, as we discussed before, it is not realistic to assume that the firm has complete knowledge of individual consumer’s (private) cost of participation. Therefore, the firm has to develop feasible incentive strategies based on its limited knowledge or assumptions about c(:). Here we discuss several different incentive strategies, and we empirically investigate how different strategies affect acquisition outcomes in later sections.

First, setting a constant incentive for all consumers is a common strategy when the firm has little knowledge of consumers’ willingness to participate. Setting a reasonably large constant incentive can indeed facilitate acquisition. However, as more consumers are acquired, the cumulative network externality would naturally attract future participation. A constant incentive does not attempt to extract such externality, making it inefficient to the firm. Meanwhile, the firm may also set $p ( s ) = 0$ for all consumers, and Equation (3) indicates that a prospective consumer would participate only if the cumulative network externality outweighs the cost of participation. This may be a reasonable strategy if the firm’s recommender system already has a sufficiently large number of users (e.g., people would be willing to join the platform without any compensation, and maybe even willing to pay premium fees for better experience). However, if the recommender system has only a small user base, then offering no incentive generally deters acquisition.

Second, although the firm does not know the precise value of c(s) for consumer $s ,$ it may nonetheless have aggregate knowledge of participation costs, based on its domain expertise, market research, or consumer surveys. For example, consumers’ valuation of their own personal data may be inferred based on their revealed preferences in online behaviors (Anderson and Moore 2006, Acquisti et al. 2016), and prior studies have developed models to estimate the price of privacy based on individuals revealed choices (Sandikc¸i et al. 2008). Suppose the firm can estimate an expected value, ${ \overline { { c } } } ,$ of its consumers’ cost of participation, then it can consider a family of incentive strategies with varying degrees of greediness, which we term as ε-greedy strategies and define as

$$
p (s ^ {*}) = \overline {{c}} - \varepsilon \cdot \sum_ {s _ {i} \in S (n)} \beta_ {i} w (s _ {i}),\tag{5}
$$

where $\varepsilon \in [ 0 , 1 ]$ . Setting $\varepsilon = 0$ gives a special case of constant incentive strategy $( \forall s ^ { * } , p ( s ^ { * } ) = \overline { { c } } )$ . Setting $\varepsilon = 1$ instead, corresponds to a fully greedy strategy where the firm intends to extract the entirety of cumulative network externality to offset the participation costs. Notably, under the fully greedy strategy, the acquisition outcome for consumer s<sup>∗</sup> depends only on the comparison between c and $c ( s ^ { * } ) ;$ ; this can be seen by replacing p(s<sup>∗</sup>) in Equation (3) with $\begin{array} { r } { \overline { { c } } - \sum _ { s _ { i } \in S ( n ) } \beta _ { i } w ( s _ { i } ) } \end{array}$

If the firm can obtain more granular knowledge of participation costs, then it can further refine the incentives for different consumers. For example, consumers who belong to the same demographic group may have similar costs of participation (e.g., they may share similar privacy preferences; Van den Broeck et al. 2015). Therefore, if the firm can estimate the average participation costs in different demographic groups, it can readily customize its incentive strategy by replacing c with the expected participation cost associated with the demographic group of consumer $s ^ { * }$ . However, we acknowledge that granular information on participation costs may be very hard or expensive to acquire, and thus omit this scenario in our empirical evaluations.

## 4. Solving the Dynamic Consumer Acquisition Model

In this section, we first discuss how different parameters of the consumer acquisition model can be estimated or assigned and then propose an efficient algorithm to solve the model (i.e., to compute the dynamic acquisition sequence and incentives). In Table 1, we provide an overview of different parameters that need to be obtained.

## 4.1. Estimation of Consumer System Values

In this part, we discuss a data-driven procedure for estimating the system values v(:) and the associated weighting factors $\alpha _ { i } .$ The estimation procedure uses the consumption data (e.g., product choices or ratings) of consumers, which gives rise to an important problem: how can we estimate a consumer’s system value when the focal consumer is (by definition) not yet acquired by the firm? As mentioned earlier, we propose to leverage market intermediaries that can use either (i) the focal consumers’ historical consumption data, potentially gathered from a different (but relevant) consumption context or (ii) the consumption data of a different set of consumers with similar characteristics.

Table 1. Parameters of the Consumer Acquisition Model

<table><tr><td>Parameter</td><td>Description</td><td>Estimation</td></tr><tr><td> $v(s), \alpha_i$ </td><td>System value of consumer s and the sequence-specific weights.</td><td>Estimated by the intermediary based on consumption data of consumer s or data of similar consumers.</td></tr><tr><td> $h(s)$ </td><td>Value potential of consumer s.</td><td>Assigned by the firm based on its internal data and potentially by querying the intermediary for relevant features on s.</td></tr><tr><td> $\gamma, \beta_i$ </td><td>Dependency of network externality w(.) on v(.) and the sequence-specific weights.</td><td>Estimated by the firm based on market research and experimentation.</td></tr><tr><td> $c(s)$ </td><td>Participation cost of consumer s.</td><td>Private information of the consumer. The firm may obtain aggregate or distributional characteristics of c(.) based on market research.</td></tr></table>

Note. The incentive for consumer $s , p ( s ) ,$ is determined by the above parameters and the firm’s incentive strategy.

First, the intermediary may collect a very rich set of consumer features (denoted as $X ( s )$ for consumer $s ) ,$ including not only demographic and socioeconomic information but also interests, preferences, transactions, and various online activities (Acquisti et al. 2016). This is evident in the examples summarized in Online Appendix A. Therefore, it is reasonable to expect that X(s) may contain consumption data that are relevant to the focal firm’s recommender task. For example, if the focal firm offers a movie recommender system, then our procedure can leverage the movie consumption data in X(s) (e.g., movie ratings on other platforms) to 8 estimate the consumer’s system value.

Second, if no relevant consumption data are available in X(s), we propose to estimate the system value indirectly, by leveraging a different (nonoverlapping) set of consumers, M $( { \mathrm { i . e . , ~ } } M \cap \{ 1 , \ldots , N \} = \emptyset )$ , via a k-nearestneighbor approach. Suppose the consumption data of those in M are relevant for the focal firm and can be collected,<sup>9</sup> their system values can be estimated using the same procedure discussed later. Then, for a focal consumer $s \in \{ 1 , \ldots , N \}$ , we find k consumers in M with the most similar characteristics (e.g., demographics), then assign v(s) to be the average system value of these k neighbors. This is consistent with one of the standard approaches in recommender system literature for dealing with the cold-start problem, that is, making recommendations for new users based on other users who share similar characteristics (Schein et al. 2002, Lam et al. 2008, Park and Chu 2009, Gantner et al. 2010, Bi et al. 2017).

We now discuss the procedure to estimate system values, consisting of three steps, in Sections 4.1.1–4.1.3.

4.1.1. Compute Performance Change. Intuitively, a consumer’s contribution to the quality of a recommender system can be measured as the difference between the predictive performance with and without that consumer. Notably, quantifying the value of data by computing the marginal performance improvement is a well-established idea (Roy and McCallum 2001, Melville et al. 2005, Geva et al. 2019). To also account for the value weighting effect, we rewrite the weighting factor $\alpha _ { i } = f ( \alpha | i )$ to highlight the fact that all consumers share the same weighting factor given a fixed position i in the consumer acquisition sequence. As an example, setting $f ( \alpha | i ) = \alpha ^ { i - 1 }$ represents exponential discounting. For consumer s at position i in a sequence $S ( i ) ,$ , the marginal contribution of this consumer to the firm’s recommender system can be written as

$$
\Delta U _ {F} ^ {R S} (S (i)) \doteq U _ {F} ^ {R S} (S (i)) - U _ {F} ^ {R S} (S (i - 1)) = v (s) f (\alpha | i),\tag{6}
$$

where $U _ { F } ^ { R S } ( S ( i ) )$ represents firm’s utility that originates from the recommender system, that is, the first term of

Equation (1). Depending on the specific recommendation task, this utility can be quantified using any relevant performance metrics (subject to certain normalization if necessary). For instance, for numeric prediction tasks (e.g., movie rating prediction), we can measure $\Delta U _ { F } ^ { R S }$ (S(i)) as the marginal change in the root mean square error (RMSE). For classification tasks $( \mathrm { e . g . }$ , product click prediction), we can use accuracy, precision, recall, or other performance metrics. Intuitively, greater improvement in predictive performance with the inclusion of consumer s implies larger value of v(s).

4.1.2. Permutation. In a given acquisition sequence, for a consumer who arrives at the ith position, we can only observe the performance change $\Delta U _ { F } ^ { R S } ( S ( i ) )$ caused by the consumer’s participation, which is insufficient to isolate the position-agnostic but consumer-specific system value v(s). We propose to use a permutation-based approach to resolve this issue.

More specifically, we randomly permute the order of all consumers and generate multiple sequences. For each permuted sequence, we recalculate the changes in predictive performance for every consumer in that sequence. Because consumers’ system values $v ( . )$ by design are invariant with respect to permutations, we have effectively placed any given consumer s (with sys tem value v(s)) at different positions in different permu tations. Suppose we generate K permutations in total, then for the kth permutation, let $\boldsymbol { u } _ { s i _ { k } }$ be the observed value of $\Delta U _ { F } ^ { R S } ( S ( \hat { i _ { k } } ) )$ ) where consumer s is placed at position $i _ { k } .$ Using the observed values of $u _ { s i _ { k } } \ ( k \in \{ 1 , \ldots , K \} )$ ), we can then estimate the system values and weighting factors.

The total number of possible permutations for a sequence of length N is N!. Analyzing all possible permutations is computationally too expensive for large N. Following the literature on permutation tests (Knijnenburg et al. 2009, Ojala and Garriga 2010, Winkler et al. 2016), a few hundred permutations can typically produce a precise set of parameter estimates in practice.

4.1.3. Compute Parameter Estimates. For concrete ness, we adopt an exponential weighting function in the following discussions, that is $, f ( \alpha | i ) = \alpha ^ { i - 1 } , \alpha \in ( 0 , 1 ]$ , for position i. Such a functional form is commonly used to characterize temporal discounting (Frederick et al. 2002), and it reduces the number of weighting factors that need to be estimated (from a set of parameters $\alpha _ { i }$ to a single parameter α). We later consider different weighting functions in Section 7.1. Recall that $\boldsymbol { u } _ { s i _ { k } }$ is the observed value of $\Delta U _ { F } ^ { R S } ( S ( i _ { k } ) )$ . Based on Equation (6), we have

$$
u _ {s i _ {k}} = v (s) \alpha^ {i _ {k} - 1} + \varepsilon_ {s i _ {k}},\tag{7}
$$

for each consumer $s \in \{ 1 , \ldots , N \}$ , where $\varepsilon _ { s i _ { k } }$ is a noise term of mean 0 and finite variance.<sup>10</sup>

We first estimate α. For each position i, we take the average of $u _ { s i _ { k } }$ for all K consumers who have $i _ { k } = i$ $( k = 1 , \ldots , K )$ . In other words, we average over the marginal utility contributions of consumers occupying a particular position i across all K permutations. This leads to $\begin{array} { r } { u . _ { i } = \frac { 1 } { K } \sum _ { \{ s : i _ { k } = i \} } u _ { s i _ { k } } } \end{array}$ , and an estimate of α can be obtained as

$$
\alpha \leftarrow \frac {1}{N - 1} \sum_ {i = 2} ^ {N} u _ {. i} / u _ {. (i - 1)}.\tag{8}
$$

We include detailed derivations of this estimate in Online Appendix C.

Given the estimate of α, we next estimate v(:) using a linear mixed model (LMM). We choose to use LMM for two reasons. First, by treating each v(:) as a random effect, LMM generates individual estimation of $v ( s )$ for each consumer s (as opposed to the same constant across all consumers). Second, LMM achieves a desirable statistical property known as the best linear unbiased prediction (BLUP; Robinson 1991). Specifically, recall that a linear mixed model with one independent variable assumes $y _ { s i } = ( \beta _ { 0 } + b _ { s 0 } ) + x _ { s i } ( \beta _ { 1 } + b _ { s 1 } ) + \varepsilon _ { s i } ,$ where $y _ { s i } ,$ x<sub>si</sub>, and $\varepsilon _ { s i }$ correspond to the response variable, independent variable, and error term of the ith repeated measure of the sth individual, respectively. Here $\beta _ { 0 } , \beta _ { 1 } , b _ { s 0 . }$ , and $b _ { s 1 }$ are fixed intercept, fixed slope, random intercept, and random slope, respectively. In Equation (7), we consider $\boldsymbol { u } _ { s i _ { k } }$ as the response variable, where each s is an independent individual, and $i _ { 1 } , \dots , i _ { K }$ are K repeated measurements (obtained via permutations). If we further consider $\alpha ^ { i _ { k } - 1 }$ as the independent variable $( \mathrm { i . e . , }$ $x _ { s i } \equiv \alpha ^ { i _ { k } - 1 }$ , where the value of $\alpha ^ { i _ { k } - 1 }$ is the same across all s), then Equation (7) becomes an LMM with zero intercept, zero fixed slope, and only a random slope v(s) to be estimated. We use the $\mathrm { \Omega } ^ { \prime \prime } \mathrm { l m e r } ^ { \prime \prime }$ function within the R software to estimate the LMM via a restricted maximum likelihood approach.

## 4.2. Estimation of Other Parameters

The other parameters of the consumer acquisition model, including $h ( . ) , \gamma , \beta _ { i } , \overline { { c } } ,$ are highly firm specific and need to be determined by the focal firm based on its domain expertise or market research. Here we discuss examples of how each parameter may be obtained.

First, value potential $h ( s )$ reflects the value that can be extracted from consumer s by means other than the improvement of recommender system quality, such as advertising revenue or purchases of the firm’s other product or service offerings. Therefore, the value of $h ( s )$ should be assigned based on the firm’s private information on its consumers’ (lifetime) values. As an illustration, the music streaming platform Spotify made \$878 million from its 190 million ad-supported users in $2 0 2 0 , ^ { 1 1 }$ which means that an average user generated \$4.62 ad revenue. If advertising is the only source of value potential for the firm, then it can set $h ( s ) = \$ 4.62$ for all consumers (subject to normalization based on the scale of system values, if necessary) as a coarse estimation of value potentials. If the firm has more granular information on value potentials $( \mathrm { e . g . }$ , different ad revenues for consumers in different demographic groups), it can assign h(s) accordingly, by querying the intermediary for relevant information on consumer s (e.g., the demographic features of s).

Second, the parameters related to network externality $( \gamma$ and $\beta _ { i } )$ and participation cost (c) are associated with consumers’ perceptions or preferences, and the firm can seek to estimate them via market research, fo example, by surveying consumers. Specifically for γ and $\beta _ { i } ,$ if the firm does not have any external information to estimate them, it can always make certain simplifying assumptions about their values. For example, to represent the scenario where the system values of acquired consumers fully determine the network externality to prospective consumers, the firm would set $\gamma = 1$ and $\beta _ { i } = \alpha _ { i }$

## 4.3. Algorithm Design

We now discuss an algorithm that implements the dynamic consumer acquisition model to compute the acquisition sequence and incentives. As discussed in Section 3.2, based on the system values obtained from the intermediary, the focal firm reaches out to the “next best” consumer (i.e., the prospective consumer that brings the largest marginal utility increase given the already-acquired consumer sequence) and offers an acquisition incentive that is determined by the firm’s incentive strategy.

We first show in the following theorem that, under any ε-greedy strategy, finding the optimal marginal consumer to acquire depends only on consumers’ system values and value potentials. Consumers’ cost of participation and cumulative network externality do not affect the choice of optimal marginal consumer, although they are needed to compute the incentive.

Theorem 1. Given an acquired consumer sequence S(n), under any particular ε-greedy incentive strategy, the optimal marginal consumer $s ^ { * }$ is determined by

$$
s ^ {*} = \underset {s \in \{1, \ldots , N \} \setminus S (n)} {\operatorname{argmax}} \alpha_ {| S (n) | + 1} v (s) + h (s).\tag{9}
$$

The proof of Theorem 1 is included in Online Appendix B. In the case of exponential discounting where $\alpha _ { i } = \alpha ^ { i - 1 }$ the maximand is equivalent to $\alpha ^ { | S ( n ) | } v ( s ) + h ( s )$ ). This theorem naturally gives rise to Algorithm 1 for computing the acquisition sequence and incentives (based on Equation (5)).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 (Algorithm for Computing Dynamic Acquisition Sequence and Incentives)
Input: Estimated values of $\alpha, \beta, \gamma, \overline{c}$, and $\forall s \in \{1, \ldots, N\}$, $v(s)$, $h(s)$.
Initialize set $R \leftarrow \{1, \ldots, N\}$ to store remaining prospective consumers;
Initialize array $S \leftarrow \langle \rangle$ to store the sequence of acquired consumers;
Initialize scalar $m \leftarrow 0$ to store the number of acquired consumers;
Initialize scalar $NE \leftarrow 0$ to store the realized cumulative network externality;
while length(R) &gt; 0 do
    //Iterate over remaining consumers to find optimal marginal consumer
    maxUtility $\leftarrow 0$; maxConsumerID $\leftarrow 0$;
    foreach $s \in R$ do
    if maxUtility &lt; $\alpha^m v(s) + h(s)$ then
    maxUtility $\leftarrow \alpha^m v(s) + h(s)$;
    maxConsumerID $\leftarrow s$;
    end
    end
    $R \leftarrow R \setminus maxConsumerID$;
    //Compute the incentive to offer
    $p = \overline{c} - \varepsilon \cdot NE$ //ε-greedy incentive strategy
    if Consumer accepts acquisition offer with incentive p then
    $S \leftarrow S \oplus maxConsumerID$;
    $NE \leftarrow NE + \beta^m \gamma v(maxConsumerID)$;
    $m \leftarrow m + 1$;
    end
end
Output: S, the realized acquisition sequence.
</div>

Finally, although we have described the dynamic acquisition model and its solution at the individual consumer level, the model can readily be adapted for group-level acquisitions (e.g., when there is a large number of consumers and acquiring them one by one is not practical or necessary). The groups can be specified by the firm based on geographies, demographics, or other features at a desired granularity. We discuss the details in Online Appendix D.

## 5. Evaluation on MovieLens 100K Data Set

In this section, we evaluate our dynamic consumer acquisition model in a numeric rating prediction context. Specifically, we consider movie recommendation and use the publicly available MovieLens 100K data set for illustration.<sup>12</sup> Collected from September 1997 to April 1998, it is one of the oldest and most widely used datasets to benchmark the performance of collaborative filtering algorithms (Harper and Konstan 2015). It contains 100,000 movie ratings, each ranging from one to five, given by 943 users to 1,682 movies. Each observation includes UserID, ItemID, Rating, and Timestamp, where Timestamp corresponds to the time when a rating was assigned by a user to an item (i.e., a movie). Because theoretically any user can rate any movie, a total of 943 × 1,682 ≈ 1.6 million ratings can be collected, whereas the observed ratings account for only 6.3%.

The recommendation of movies based on the predictions of unobserved ratings is among the main tasks of a movie recommender system. To build such a recommender system, we adopt singular value decomposi tion (SVD; Funk 2006) because of its stability and efficiency (Koren et al. 2009). SVD is one of the most widely used and effective procedures for classic recommender system problems (Feuerverger et al. 2012). We use the SVD implementation offered in the R package “recosystem,” set the number of latent factors dim � 30, and rely on cross-validation to select other hyperparameters. To measure predictive performance, we adopt a commonly used metric of numeric predictive accu racy: root mean squared error (RMSE).

## 5.1. Evaluation Schemes

We evaluate the dynamic consumer acquisition model under two different schemes, respectively, representing the cases where X(s) contains relevant historical consumption data or not.

In the first scheme, we split the data set into two partitions {A, B} based on Timestamp, where A contains the earliest 50% of each user’s ratings (50,240 ratings in total) and B contains the latest 50% of each user’s ratings (49,760 ratings in total). We use partition A to estimate the system values of all users and to compute the dynamic acquisition sequence based on Algorithm 1, then use partition B to evaluate the acquisition outcomes, measured by RMSE, firm utility, and consumer surplus (i.e., total surplus of acquired consumers). This evaluation scheme is designed to simulate the case where consumers’ historical consumption data (partition A) are taken to estimate their values and make acquisition decisions, and their realized consumption data (partition B) are used for evaluation.<sup>13</sup> We refer to it as the “warm-start” evaluation scheme.

In the second scheme, we instead split the data set into two partitions {A, B} based on UserID, such that A contains the earliest 50% of users (determined by thei first timestamp) and B contains the latest 50% of users.<sup>1</sup> We estimate the system values of all users in partition A and use the k-nearest-neighbor approach discussed in Section 4.1 to assign system values for users in partition B (i.e., actual rating data in partition B are never used for system value estimation; they are later used for evaluation). We set k � 3 and calculate the similarity between two users based on all available demographic features, namely age, gender, occupation, and zip code. Then, we use the assigned system values in partition B to compute the acquisition sequence and use the actual/realized ratings in that partition to evaluate the acquisition outcomes. This scheme seeks to simulate the case where no consumption data for the prospective consumers (those in partition B) are available up front, and the acquisition decisions are made based on consumption data of similar consumers (those in partition A). We refer to it as the “cold-start” evaluation scheme.

Under both evaluation schemes, we benchmark the dynamic acquisition sequence against 200 randomly generated acquisition sequences. For each random sequence, we simply assume that the firm sends acquisition offers to prospective consumers in a random order.

## 5.2. Evaluation Results Under the Warm-Start Scheme

As discussed before, we take the earliest 50% of each user’s ratings and follow the parameter estimation procedure described in Section 4.1 to obtain estimates of v(:) and α. We generate 1,000 permutations in total and carry out the parameter estimation based on how RMSE changes as more users are included. We provide a visual illustration of the RMSE changes associated with the permuted sequences in Online Appendix E. Following our parameter estimation procedure, we obtain an estimated $\alpha = 0 . 7 2 1$ . The estimated system value, v(:), of each user is summarized in a histogram in Figure 2 (in base-10 log scale). The distribution of system values in the MovieLens data set shows a bimodal pattern, where users’ system values concentrate around 0 and 0.5, respectively. Meanwhile, a small number of users have large negative system values.

We further examine the relationships between the estimated v(:) and different characteristics of users’ rating patterns and find that high-value users tend to have larger rating standard deviation, larger rating deviations from the global average rating, and larger number of rated movie genres, than low-value users. However, the positive relationship between system value and rating standard deviation or rating deviations from the global average only holds up to a certain degree, beyond which the relationship becomes negative. We do not observe a significant association between number of ratings and v(:). In other words, users with high system values do not necessarily consume more; instead, they tend to have more varying preferences, more idiosyncratic tastes, and exposure to a greater variety of product categories. However, having preferences that are too unstable or too idiosyncratic is associated with lower system values.

Figure 2. Histogram (in Base-10 Log Scale) of Estimated System Values v(:) of Users (MovieLens Data)  
![](/api/attachments/2NAG6CY8/fulltext/images/10ad2ee74258e7c324653b2dc6e8b6e81ed2784c4545905a59fcc58b8a993483.jpg)

For other parameters in the consumer acquisition model, we are not able to leverage firm-specific data to set their values due to the firm-agnostic nature of the MovieLens data set. Accordingly, for parameters related to network externality, we set $\gamma = 1 \ \mathrm { ( i . e . }$ , the network externality generated by a participating user equals the system value of that user) and $\beta = \alpha \ ( \mathrm { i . e . }$ ., the network externality and system value share the same discount rate). Second, we set the value potential of each user, $h ( . )$ , to be 0.348, which equals the average system value of all users. We choose to specify a constant value potential consistent with the practice among online movie platforms $( \mathrm { e . g . }$ , Hulu and Peacock) to charge a fixed fee to remove ads. We use the average system value to parameterize the value potential so that the two types of user values have comparable magnitudes and both can have meaningful impact on acquisition outcomes.<sup>1</sup> Finally, we simulate users’ participation costs by randomly drawing from a uniform distribution [0, max $\textstyle \sum _ { j = 1 } ^ { i } \alpha ^ { j - 1 } v ( s _ { j } ) ]$ ]. We cap participation cost by $\textstyle \operatorname* { m a x } _ { i } \sum _ { j = 1 } ^ { i }$ $\alpha ^ { j - 1 } v ( s _ { j } )$ (i.e., the largest cumulative network externality), to reflect the realistic scenario where users are naturally willing to participate in the recommender system when it is sufficiently attractive. Consistent with our discussions earlier in the paper, we assume that the firm cannot estimate participation costs at an individual level and can only obtain the average participation cost, $\overline { { c } } = 1 . 5 7 1$ . The firm determines acquisition incentives based on c, cumulative network externality, and its choice of a greediness level ε.

Next, we follow Algorithm 1 to compute the dynamic acquisition sequence. In Table 2, we report the RMSE, firm utility, and consumer surplus associated with the dynamic acquisition sequence and the average random acquisition sequence, for five different levels of ε. All metrics are calculated based on users’ latest 50% of rat ings. In the same table, we further report the total num ber of acquired consumers (i.e., those consumers who accept the acquisition offers) and the total amount of incentive paid out by the firm: These measures can help explain some of our findings. For each metric, we also conduct one-sided t tests to compare the dynamic sequence with random sequences.

We make several observations based on the results. First, when $\varepsilon < 1$ , the dynamic acquisition sequence achieves significantly lower RMSE and higher consumer surplus than an average random sequence, suggesting that our proposed acquisition approach can consistently benefit the firm’s recommender system as well as consumers. The dynamic sequence is able to acquire significantly more consumers than random sequences, which partly explains the performance improvement and greater consumer surplus. When ε � 1 (i.e., the fully greedy strategy), the acquisition outcome only depends on a comparison between c and c(s) for any consumer s (as discussed in Section 3.3), and therefore both the dynamic and the random sequences end up acquiring the same set of consumers (albeit in different orders), leading to the same RMSE and consumer surplus.

Table 2. Evaluation Results Under the Warm-Start Scheme (MovieLens Data)

<table><tr><td rowspan="2">ε</td><td colspan="2">RMSE</td><td colspan="2">Firm utility</td><td colspan="2">Consumer surplus</td><td colspan="2">No. of consumers</td><td colspan="2">Total incentive</td></tr><tr><td colspan="2">Dyn &lt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &lt; Rand</td></tr><tr><td>0</td><td>1.0056</td><td>1.0338***(0.028)</td><td>-1,148.97</td><td>-1,028.19(123.13)</td><td>2,886.15</td><td>1,218.00***(310.99)</td><td>942</td><td>841.76***(100.98)</td><td>1,480.12</td><td>1,322.62(158.66)</td></tr><tr><td>0.25</td><td>1.0056</td><td>1.0564***(0.026)</td><td>-427.50</td><td>-677.29***(17.47)</td><td>2,164.68</td><td>956.25***(209.54)</td><td>942</td><td>756.19***(90.92)</td><td>758.64</td><td>941.91***(47.18)</td></tr><tr><td>0.5</td><td>1.0134</td><td>1.0859***(0.015)</td><td>293.03</td><td>-377.62***(87.57)</td><td>1,443.21</td><td>725.85***(120.74)</td><td>939</td><td>651.55***(56.02)</td><td>37.07</td><td>605.79***(67.95)</td></tr><tr><td>0.75</td><td>1.0765</td><td>1.1047***(0.006)</td><td>737.72</td><td>-154.44***(149.27)</td><td>813.05</td><td>531.01***(52.90)</td><td>687</td><td>560.77***(30.38)</td><td>-495.39</td><td>350.99***(138.38)</td></tr><tr><td>1.0</td><td>1.1238</td><td>1.1238(0)</td><td>852.85</td><td>11.68***(181.67)</td><td>370.41</td><td>370.41(0)</td><td>476</td><td>476(0)</td><td>-684.04</td><td>155.35***(181.28)</td></tr></table>

Notes. The Dyn columns contain results of the dynamic acquisition sequence, and the Rand columns contain results of the average random sequence and its standard deviation (across 200 sequences) in parentheses. Comparisons based on one-sided t tests (with alternative hypothese specified in the second row) are reported.  
\*\*\*p < 0.001.

Second, the dynamic acquisition sequence results in significantly higher firm utility than an average random sequence when $\varepsilon > 0 ,$ and the utility gains are especially large when $\varepsilon \ge 0 . 5 ,$ , which indicates that a sufficiently aggressive incentive strategy that leverages network externality to offset acquisition incentive can greatly increase firm utility. Comparisons of total incentive further supports this observation: When $\varepsilon > 0 ,$ , the firm pays much smaller incentives under the dynamic sequence. Notably, the total incentives are negative for $\varepsilon \in \{ 0 . 7 5 , 1 . 0 \}$ , suggesting that many users are willingly paying to join the system. When $\varepsilon = 1$ , although the dynamic and random sequences acquire the same set of consumers, the former results in much higher utility and lower total incentive because it incentivizes high-value users to join early, which “kick starts” the cumulative network externality. In the case of $\varepsilon = 0$ (i.e., constant incentive strategy), the firm does not take advantage of the cumulative network externality to attract consumers at all. As a result, both the dynamic and random sequences lead to substantially negative firm utility, with the dynamic sequence being even more inferior.

Third, comparisons across different ε levels reveal interesting trade-offs between incentive strategies and acquisition outcomes. Specifically, as ε increases, the firm sets incentives more greedily to extract larger portions of cumulative network externality. While the firm pays smaller incentives in total (and thereby generating greater utility and less consumer surplus), it also ends up acquiring fewer consumers because those with large participation costs become more likely to decline the acquisition offers. Such a reduction in the number of acquired consumers turns out to hurt the recommender system performance: Indeed, the fully greedy strategy (ε � 1) leads to a worse-performing recommender system than less greedy strategies.

## 5.3. Evaluation Results Under the Cold-Start Scheme

Under the cold-start evaluation scheme, we perform system value estimation using all ratings of the earliest 50% of users. We obtain an estimated $\alpha = 0 . 9 0 4$ , and we plot the estimated system values, v(:), in the left panel of Figure 3. Then, for each of the remaining 50% of users, we assign the system value via a three-nearest-neighbo approach (neighbors identified based on age, gender, occupation, and zip code). We plot the assigned system values in the right panel of Figure 3.

We can see that the distribution of system values assigned via the three-nearest-neighbor approach has a similar range as those directly estimated from rating data but does not show a strong bimodal pattern. In other words, the k-nearest-neighbor assignment approach ap pears to “smooth out” the estimated system values.

We set the values of other parameters in the same way as discussed in the previous section, and compute the dynamic acquisition sequence afterward. In Table 3, we report the RMSE, firm utility, and consumer surplus associated with the dynamic acquisition sequence and the average random acquisition sequence, for five different levels of ε. All metrics are calculated based on the actual/realized ratings of prospective users. Similarly, we also report the total number of acquired consumers and the total amount of incentive paid out by the firm.

Figure 3. Histograms (in Base-10 Log Scale) of Estimated and Assigned System Values v(:) of Users (MovieLens Data)  
![](/api/attachments/2NAG6CY8/fulltext/images/ad8e69befb3bf4eefd5b06d6ffe798ece7e50a70a8f200f3a1412fa62b29cef2.jpg)

![](/api/attachments/2NAG6CY8/fulltext/images/90f8bcae925869de389c12cfb82073c97efa5e6556a24e1577cbe30de68f5bac.jpg)  
Notes. The left panel plots the estimated system values associated with the earliest 50% of users. The right panel plots the assigned system value associated with the remaining 50% of users via the three-nearest-neighbor approach.

The results are highly consistent with those under the warm-start evaluation scheme. The dynamic sequence achieves a significantly lower RMSE and larger surplus than an average random sequence when ε < 1; it also produces significantly higher firm utility when ε > 0. As ε increases, the dynamic sequence acquires fewer users with decreasing (even negative) total incentives.

Overall, our empirical evaluations under both schemes have demonstrated a nuanced relationship between the greediness of incentive strategies and the acquisition outcomes. Neither a fully greedy strategy (ε � 1) nor a constant strategy $( \varepsilon = 0 )$ is optimal on all three acquisition outcomes. Although a fully greedy strategy leads to high firm utility and minimizes the total incentives paid out to prospective consumers, it also tends to acquire fewer consumers than less greedy strategies, which ends up hurting the predictive performance of the recommender system.

On the flip side, a constant incentive strategy can acquire more consumers in total and result in a better recom mender system, at the expense of being costly for the firm. Meanwhile, the dynamic sequence can in fact achieve simultaneously more advantageous recommender system performance, firm utility, and consumer surplus (as compared with a random acquisition sequence) under a moderately greedy strategy. These tradeoffs highlight a need for the firm to choose the incentive strategy that best serves its business objectives and priorities, and a strategy that is neither too greedy nor too uniform might be more desirable overall.

## 6. Evaluation on the Kelkoo Data Set

In many real-world applications, binary decisions such as click-throughs in web page viewing or purchases in online shopping are often of great interest to advertisers and e-commerce companies. In these applications, recommender systems typically focus on predicting the probability of a consumer clicking/purchasing an item. We now evaluate the performance of the dynamic consumer acquisition model in such a scenario, using the Kelkoo data set,<sup>16</sup> which includes consumers’ interactions with product offers (click or not click) on Kelkoo.com.

Table 3. Evaluation Results Under the Cold-Start Scheme (MovieLens Data)

<table><tr><td rowspan="2">ε</td><td colspan="2">RMSE</td><td colspan="2">Firm utility</td><td colspan="2">Consumer surplus</td><td colspan="2">No. of consumers</td><td colspan="2">Total incentive</td></tr><tr><td colspan="2">Dyn &lt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &lt; Rand</td></tr><tr><td>0</td><td>1.0088</td><td>1.0116***(0.004)</td><td>-463.25</td><td>-462.66(2.57)</td><td>1,000.61</td><td>696.89***(42.81)</td><td>468</td><td>466.74***(2.61)</td><td>533.55</td><td>532.12(2.97)</td></tr><tr><td>0.25</td><td>1.0088</td><td>1.0140***(0.005)</td><td>-213.64</td><td>-286.67***(8.92)</td><td>750.99</td><td>523.28***(32.03)</td><td>468</td><td>463.14***(5.65)</td><td>283.94</td><td>355.60***(8.62)</td></tr><tr><td>0.5</td><td>1.0146</td><td>1.0402***(0.008)</td><td>34.28</td><td>-97.00***(15.25)</td><td>499.46</td><td>360.91***(17.92)</td><td>464</td><td>395.63***(11.43)</td><td>35.43</td><td>156.12***(13.59)</td></tr><tr><td>0.75</td><td>1.0877</td><td>1.1086***(0.005)</td><td>198.28</td><td>37.52***(21.22)</td><td>280.26</td><td>231.54***(6.91)</td><td>339</td><td>301.37***(3.75)</td><td>-146.78</td><td>7.88***(20.66)</td></tr><tr><td>1.0</td><td>1.1442</td><td>1.1422(0)</td><td>246.79</td><td>111.34***(20.47)</td><td>132.79</td><td>132.79(0)</td><td>230</td><td>230(0)</td><td>-211.16</td><td>-76.32***(20.38)</td></tr></table>

Notes. The Dyn columns contain results of dynamic acquisition sequence, and the Rand columns contain results of an average random sequenc and its standard deviation (across 200 sequences) in parentheses. Comparisons based on one-sided t tests (with alternative hypotheses specified in the second row) are reported.  
\*\*\*p < 0.001.

Kelkoo is a large e-commerce marketing platform that leverages personalization techniques to recommend the best product offers to visitors. In this data set, we observe ConsumerID, OfferID, Category of the product offer, Merchant, consumer-offer Interaction, and Timestamp of the interaction. The data set represents all interactions from 2 a.m., June 1, 2016, to 2 a.m., July 1, 2016. An interaction is defined as one if a consumer has clicked on an offer at least once in the data collection period and zero if an offer has been shown to the consumer but the consumer has never clicked on it.

Compared with the MovieLens 100K data set, the Kelkoo data set is substantially larger and contains more than 520,000 consumers, 2.3 million offers, and 9.2 million unique interactions (i.e., views or clicks). Given the large number of consumers and offers in the Kelkoo data set, we have a highly sparse data matrix with $7 . 7 \times 1 0 ^ { - 6 }$ observation rate. Meanwhile, the average click-through rate among all interactions (percentage of ones) is around 9.8%. It is not surprising that many offers have rarely been clicked, and a lot of consumers visited Kelkoo very sporadically. As such, the Kelkoo data set offers an opportunity to evaluate our model when consumer data are extremely large and sparse.

The goal of a recommender system in this setting is to predict the probability that a consumer would click through a given offer, so that offers of high clickthrough probabilities may be strategically displayed in more advantageous positions. We use the binary matrix factorization algorithm (Zhang et al. 2007), a common matrix factorization approach for binary data, to build a recommender system for click-through prediction.<sup>1</sup>

We use area under the ROC curve (AUC) as the primary performance metric of the recommender system model, because AUC is independent of the prediction threshold of binary classification, and properly captures the model’s capability of assigning higher probabilities to offers that are more likely to be clicked. The AUC measure is used in the parameter estimation of the consumer acquisition model. In addition, we also report two other performance metrics, namely sensitivity (i.e., true positive rate or recall of class 1) and accuracy (i.e., the percentage of correctly classified data across both classes) in order to obtain a more comprehensive view of the model’s performance. Having a high sensitivity means that the model is capable of identifying most of the offers that a consumer is interested in, and having a high accuracy means the model’s predictions are generally accurate across both click and nonclick classes. The prediction threshold is set to 0.5 for these two metrics (i.e., a predicted probability higher than 0.5 is classified as a click).

## 6.1. Evaluation Schemes

As with the MovieLens data set, we carry out evaluations on the Kelkoo data set under two different schemes. The warm-start scheme aims to test the model’s performance when consumers’ historical interactions are collected by the market intermediary (potentially from a different platform) and used for estimating their system values. We split the data set based on Timestamp into two partitions that contain the earliest and the latest 50% of interactions of each consumer, respectively, used for parameter estimation and performance evaluation.<sup>18</sup> In contrast, the cold-start scheme considers the case where no detailed interaction data of the prospective consumers (i.e., which specific offers they have interacted with) are available: only their interests in broad offer categories are observed.<sup>19</sup> Their system values are assigned based on information of another set of consumers (e.g., anonymous consumers from a public data set or previous consumers of the firm or the intermediary) via a three-nearest-neighbor approach. We split the data set based on ConsumerID into two partitions, containing the earliest and the latest 50% of consumers (based on their first Timestamp), respectively, for parameter estimation and performance evaluation.

Because of the large number of consumers in the Kelkoo data set, it is computationally expensive to estimate system values of every individual consumer.<sup>2</sup> Instead, we carry out a group-level estimation. Specifically, we apply k-Means clustering on the data partition used for parameter estimation, and compute the similarity between two consumers as the Euclidean distance between their interaction frequencies with 273 different offer categories. Next, we treat consumers in a given cluster as indistinguishable from each other, and permute the order of different clusters. This allows us to estimate a “total” system value for the whole cluster, which is then divided by the cluster size to obtain the system value of each consumer within that cluster. Although the system values estimated at such a group-level are “coarsened,” doing so enables parameter estimation for very large data sets with limited computational resources.

## 6.2. Evaluation Results Under the Warm-Start Scheme

The group-level estimation (with 200 groups discovered by k-Means and 250 sequence permutations) produces a system value distribution shown in Figure 4 and an estimated $\alpha = 0 . 8 3 0$ . We simulate the other parameters of the acquisition model at an individual consumer level, in the same way as the evaluations on MovieLens data.

Figure 4. Histogram (in Base-10 Log Scale) of Estimated System Values v(:) of Users (Kelkoo Data)  
![](/api/attachments/2NAG6CY8/fulltext/images/e176ce13689ee4ada1b092d8224c3d5dff7f0fa42a9dd1d7761b039edc598b7e.jpg)

In Table 4, we summarize the benchmarking results comparing our proposed dynamic acquisition model with 200 random acquisition sequences on predictive performance of the recommender system (AUC, sensitivity, accuracy), firm utility, and consumer surplus.

The evaluation results are consistent with those obtained on MovieLens data. Under less greedy acquisition strategies (smaller ε), our model acquires significantly more consumers than under random acquisition, leading to higher predictive performance of the recommender system as well as higher consumer surplus. In contrast, under more greedy strategies (larger ε), the firm pays much smaller incentives and extracts significantly more utility. It is worth noting that our model not only outperforms random acquisition on AUC (the metric used to estimate system values), but also on sensitivity and accuracy, indicating that it leads to an overall better recommender system.

## 6.3. Evaluation Results Under the Cold-Start Scheme

We apply the same group-level estimation procedure (with 200 groups discovered by k-Means and 250 permutations) on the data of the earliest 50% of all consu mers to obtain their system values. For the other 50% of consumers (whose interaction data are taken to be unobservable by the firm), we assign their system values using the three-nearest-neighbor approach based on their interaction frequencies with offer categories. The estimated and assigned system values are respectively plotted in Figure 5. The benchmarking results are summarized in Table 5 and are again consistent with the key findings from the previous evaluations.

## 7. Additional Evaluations

In addition to the main evaluation results reported thus far, we also conducted six other sets of evaluations that highlight the robustness of our proposed approach and provide additional insights about its performance.

## 7.1. Alternative Discounting Functions

Throughout our main evaluations, we parameterize the sequence-specific weighting factors (i.e., α<sub>i</sub> and β<sub>i</sub>) using an exponential discounting function. Although being a common choice, it represents very fast discounting. In this part, we consider two alternative choices of slower discounting functions, namely hyperbolic discounting and power-law discounting.

The hyperbolic discounting function is widely used in behavioral economics literature (Ainslie and Haslam 1992, Laibson 1997, Rubinstein 2003, Dasgupta and Maskin 2005) to describe temporal preferences, with the unique characteristic that discounting becomes slower over time (rather than constant discounting under the exponential function). In the context of consumer acquisition, this means late-coming consumers can still bring sizable changes in both recommender system’s performance and cumulative network externality. Specifically, we consider a standard hyperbolic discounting function: $\begin{array} { r } { \alpha _ { i } = \frac { 1 } { 1 + \alpha ( i - 1 ) } , } \end{array}$ where i is the position in the acquisition sequence and α is a constant scalar that affects the speed of discounting (larger α indicates faster discounting). Although the parameter estimation procedures largely remain the same, we need to revise how α is estimated, due to the change in the functional form. We discuss the details in Online Appendix H.1. We rerun the warmstart evaluation scheme on the MovieLens 100K data set. The results, which are highly consistent with those under exponential discounting, are reported in Online Appendix H.1.

Table 4. Evaluation Results Under the Warm-Start Scheme (Kelkoo Data)

<table><tr><td rowspan="2">ε</td><td colspan="2">AUC</td><td colspan="2">Sensitivity</td><td colspan="2">Accuracy</td><td colspan="2">Firm utility</td><td colspan="2">Consumer surplus</td><td colspan="2">No. of consumers</td><td colspan="2">Total incentive</td></tr><tr><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &lt; Rand</td></tr><tr><td>0</td><td>0.69</td><td>0.56***(0.0029)</td><td>0.18</td><td>0.07***(0.0009)</td><td>0.932</td><td>0.925***(&lt;0.0001)</td><td>-1,337.49</td><td>-669.11(6.01)</td><td>2,407.93</td><td>333.63***(6.15)</td><td>209,994</td><td>105,053***(944.23)</td><td>1,337.83</td><td>669.27(6.02)</td></tr><tr><td>0.25</td><td>0.69</td><td>0.56***(0.0004)</td><td>0.18</td><td>0.07***(0.0006)</td><td>0.932</td><td>0.925***(&lt;0.0001)</td><td>-735.51</td><td>-668.81(2.97)</td><td>1,805.95</td><td>333.47***(4.57)</td><td>209,994</td><td>10,5030***(711.36)</td><td>735.85</td><td>668.97(2.97)</td></tr><tr><td>0.5</td><td>0.68</td><td>0.56***(0.0003)</td><td>0.17</td><td>0.07***(0.0005)</td><td>0.930</td><td>0.925***(&lt;0.0001)</td><td>-189.05</td><td>-668.51***(0.09)</td><td>1,140.59</td><td>333.32***(3.02)</td><td>194,292</td><td>10,5007***(474.97)</td><td>189.37</td><td>668.67***(0.09)</td></tr><tr><td>0.75</td><td>0.64</td><td>0.56***(0.0002)</td><td>0.12</td><td>0.07***(0.0003)</td><td>0.928</td><td>0.925***(&lt;0.0001)</td><td>254.07</td><td>-668.23***(3.04)</td><td>675.39</td><td>333.15***(1.50)</td><td>149,441</td><td>10,4982***(235.14)</td><td>-253.83</td><td>668.4***(3.04)</td></tr><tr><td>1.0</td><td>0.56</td><td>0.56(0)</td><td>0.07</td><td>0.07(0)</td><td>0.925</td><td>0.925(0)</td><td>449.69</td><td>-667.94***(5.92)</td><td>333.01</td><td>333.01(0)</td><td>104,962</td><td>10,4962(0)</td><td>-449.51</td><td>668.11***(5.92)</td></tr></table>

Notes. The Dyn columns contain results of the dynamic acquisition sequence, and the Rand columns contain results of the average random sequence and its standard deviation (across 200 sequences) in parentheses. Comparisons based on one-sided t tests (with alternative hypothese specified in the second row) are reported.  
\*\*\*p < 0.001.

Figure 5. Histograms (in Base-10 Log Scale) of Estimated and Assigned System Values v(:) of Users (Kelkoo Data)  
![](/api/attachments/2NAG6CY8/fulltext/images/74279db21a8fb014791d552dcae336edcda7526aad90ae79c5994c5b800f6578.jpg)

![](/api/attachments/2NAG6CY8/fulltext/images/06ea9f6197ecb80100dfb09f953b9a2e062b772c09f46d10ef2828e6988a1bf0.jpg)  
Notes. The left panel plots the estimated system values associated with 50% of consumers. The right panel plots the assigned system values asso ciated with the remaining 50% of consumers via the three-nearest-neighbor approach.

Next, we consider the power-law discounting. Unlike hyperbolic discounting, power-law discounting is not defined by a single function, but rather by its “long-tail” property. We operationalize power-law discounting as $\hat { \alpha } _ { i } \stackrel {  } { = } i ^ { - 2 } \stackrel { \cdot } { , }$ that is, the discount rate is quadratic with respect to the position in an acquisition sequence.<sup>2</sup> Under this discounting function, we rerun the warmstart evaluation scheme on the MovieLens 100K data set and report the results in Online Appendix H.1. Again, we obtain qualitatively similar findings as before.

## 7.2. Alternative Parameter Distributions and Values

In our main evaluations, we set consumers’ value potential h(:) to be a constant (i.e., reflecting the average system value) and simulate their participation cost c(:) by drawing from a uniform distribution. To test the robustness of the acquisition model under alternative distributional settings, we simulate both $h ( . )$ and c(:) based on normal distributions. In addition, rather than setting γ � 1 and $\beta = \alpha ,$ we also consider setting $\gamma \in$ {0:5, 1:5} and either $\beta > \alpha$ or $\beta < \alpha .$ . Details about the simulation setup and evaluation results are summarized in Online Appendix H.2. The findings are highly consistent with the main evaluations, indicating the robustness of our model under alternative parameter distributions and values.

Table 5. Evaluation Results Under the Cold-Start Scheme (Kelkoo Data)

<table><tr><td rowspan="2">ε</td><td colspan="2">AUC</td><td colspan="2">Sensitivity</td><td colspan="2">Accuracy</td><td colspan="2">Firm utility</td><td colspan="2">Consumer surplus</td><td colspan="2">No. of consumers</td><td colspan="2">Total incentive</td></tr><tr><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &gt; Rand</td><td colspan="2">Dyn &lt; Rand</td></tr><tr><td>0</td><td>0.79</td><td>0.61***(0.0009)</td><td>0.57</td><td>0.24***(0.0019)</td><td>0.92</td><td>0.89***(&lt;0.0001)</td><td>-295.87</td><td>-148.09(0.91)</td><td>591.04</td><td>73.96***(0.86)</td><td>260,842</td><td>130,557***(798.16)</td><td>296.03</td><td>148.17(0.91)</td></tr><tr><td>0.25</td><td>0.79</td><td>0.61***(0.0003)</td><td>0.57</td><td>0.24***(0.0006)</td><td>0.92</td><td>0.89***(&lt;0.0001)</td><td>-148.11</td><td>-148.01(0.10)</td><td>443.28</td><td>73.94***(0.14)</td><td>260,842</td><td>130,548***(125.26)</td><td>148.27</td><td>148.09(0.10)</td></tr><tr><td>0.5</td><td>0.79</td><td>0.61***(0.0005)</td><td>0.57</td><td>0.24***(0.0010)</td><td>0.92</td><td>0.89***(&lt;0.0001)</td><td>-4.63</td><td>-147.89***(0.02)</td><td>291.22</td><td>73.92***(0.49)</td><td>259,210</td><td>130,536***(425.32)</td><td>4.79</td><td>147.97***(0.02)</td></tr><tr><td>0.75</td><td>0.76</td><td>0.61***(0.0006)</td><td>0.40</td><td>0.24***(0.0013)</td><td>0.90</td><td>0.89***(&lt;0.0001)</td><td>97.45</td><td>-147.65***(1.43)</td><td>162.14</td><td>73.86***(0.68)</td><td>193,382</td><td>130,481***(584.40)</td><td>-97.33</td><td>147.73***(1.43)</td></tr><tr><td>1.0</td><td>0.61</td><td>0.61(0)</td><td>0.24</td><td>0.24(0)</td><td>0.89</td><td>0.89(0)</td><td>128.09</td><td>-147.60***(0.27)</td><td>73.74</td><td>73.74(0)</td><td>130,376</td><td>130,376(0)</td><td>-128.01</td><td>147.68***(0.27)</td></tr></table>

Notes. The Dyn columns contain results of the dynamic acquisition sequence, and the Rand columns contain results of the average random sequence and its standard deviation (across 200 sequences) in parentheses. Comparisons based on one-sided t tests (with alternative hypothese specified in the second row) are reported.  
\*\*\*p < 0.001.

## 7.3. Alternative Recommender System Algorithm

We have used two widely adopted matrix factorization algorithms, namely SVD and binary matrix factorization, to build the recommender systems for the main evaluations; we further demonstrate in this part that our findings remain robust for other modern recommendation algorithms, including some of the recent developments based on deep learning architectures. In particular, we consider the neural collaborative filtering (NCF) algorithm developed by He et al. (2017). We repeat the warm-start evaluation scheme on the Movie-Lens data set using NCF. The results are summarized in Online Appendix H.3, and the general findings once again remain consistent.

## 7.4. Impact on Recommendation Diversity

Thus far, we have evaluated the impact of different consumer acquisition strategies on the firm’s recommender system by examining its predictive accuracy. However, maximizing predictive accuracy is not always the sole goal of a recommender system. Other considerations such as recommendation diversity, novelty, and unexpectedness may also be important in practice (Adomavicius and Tuzhilin 2005, Jannach and Jugovac 2019), but the system designers are often faced with inherent tradeoffs when trying to improve several objectives simultaneously (Adomavicius and Kwon 2011). In this part, we evaluate how the proposed consumer acquisition approach affects the recommendation diversity because diversity is commonly regarded as an important objective for recommender systems besides accuracy (Jannach and Jugovac 2019, Lee and Hosanagar 2019).

We carry out the same acquisition process on the MovieLens data set under the cold-start evaluation scheme, where the data set is split into partitions A and $B ,$ each containing 50% of all users. We choose this evaluation scheme because users in partition B (i.e., the prospective users) are assumed to have no prior ratings observed by the firm, making them natural candidates to evaluate the diversity of future recommendations. Under the dynamic and random acquisition sequences, respectively, we examine the recommendations made for acquired users in partition B to quantify the recommendation diversity. For a given acquired user in partition $B ,$ we recommend the top-k items $( k \in \{ 5 , 1 0 \} )$ ranked by the predicted rating. Recommendation diversity is measured by the Gini coefficient. Both the top-k recommendation method and diversity metric are commonly used in the literature (Adomavicius and Kwon 2011, 2014). We report the results in Online Appendix H.4.

Overall, we find preliminary evidence that the accuracy-driven dynamic acquisition model does not inadvertently lead to a substantial reduction of recommendation diversity. Meanwhile, the proposed acquisition approach can generally accommodate different desired objectives (e.g., accuracy, diversity, unexpectedness, or some weighted combination of several metrics). The performance objective that is important for the firm in making acquisition decisions can be explicitly specified as part of the acquisition problem formulation.

## 7.5. Arrival of Organic Participants

Outside of the target pool of N prospective consumers, it is certainly possible that some other consumers may willingly participate without firm incentives—We refer to them as “organic participants.” Having organic participants does not affect the estimation of system values for target prospective consumers $s \in \{ 1 , \ldots , N \}$ because the data about organic participants are not available to the market intermediary. However, the arrival of organic participants during the firm’s acquisition process can affect the acquisition outcomes, because their participation can increase the cumulative network externality, thereby making the platform more attractive to prospective consumers.

To understand the impact of organic participants on different acquisition outcomes, we conduct an additional set of warm-start evaluations on the MovieLens data set. The evaluation setup is as follows. Outside of the 943 users in the MovieLens data set, we assume there are 100 organic participants in total, arriving randomly during the acquisition process. Each organic participant $j \in \{ 1 , \ldots , 1 0 0 \}$ has a system value v(j), which is unobservable to the focal firm. We generate $v ( j )$ by sampling with replacement from the estimated v(s) of the target consumers $( s \in \{ 1 , . . . , 9 4 3 \} )$ ). In other words, we assume that organic participants come from the same population as target consumers. The firm can carry out the dynamic acquisition process in at least two ways. First, the firm can proceed with acquisition in the same way as before, as if the organic participants do not exist. Alternatively, the firm can adjust its acquisition prices as organic participants join its platform. Although $v ( j )$ of organic participant j is not observable to the firm, it can assign the average estimated system value to participant j (i.e., $\forall j \in \{ 1 , \ldots , 1 0 0 \} , \widehat { v ( j ) }  \textstyle { \frac { 1 } { 9 4 3 } } \sum _ { s = 1 } ^ { 9 4 3 } v ( s ) )$ and then compute the adjusted acquisition price for the next consumer accordingly. Meanwhile, regardless of the firm’s acquisition strategy, the actual cumulative network externality for a prospective consumer is the sum of network externality contributed by both target consumers and organic consumers that have joined before. When the dynamic acquisition process terminates, we compute and report the firm utility, consumer surplus, and recommender system performance associated with acquired target consumers. We do not count the utility or surplus of organic participants in the reported results because their arrival is independent of the firm’s acquisition efforts.

The results are reported in Online Appendix H.5 and are again consistent with our main findings, indicating that our method is robust to the arrival of organic participants.

## 7.6. Evaluations using the Amazon Review Data Set

In the main evaluations, because of the difficulty of locating two data sources with a common set of users, we split the same data set (either by consumption time or by consumer) into two partitions $A$ and ${ \hat { B } } .$ In this section, we carry out additional (warm-start) evaluations using the Amazon Review data set (McAuley et al. 2015), which contains a large number of Amazon reviews and ratings across 24 different product categories. This data set allows us to identify users who have rated products across different categories and, thus, provides an additional opportunity for realistic evaluation.

We conduct two sets of warm-start evaluations, respectively considering a “near-domain” scenario and a “far-domain” scenario. In the near-domain scenario, we choose two product categories, namely Musical Instruments and Digital Music, that belong to highly related (i.e., music-related) consumption domains. We then randomly selected 1,500 users who had rated at least one product in each of the two categories, treated their rating data in Musical Instruments as partition A (i.e., data that are available to market intermediary), and treated their data in Digital Music as partition B $( \mathrm { i . e . , }$ data related to the focal firm). In contrast, in the far-domain scenario, we choose two product categories, namely Video Games and Health and Personal Care, that belong to different consumption domains with no obvious connection. We again randomly selected 1,500 users who rated products in both categories and treated their data in the two categories as partition A and $B ,$ respectively. In each scenario, we then carry out the acquisition and evaluation in the same way as before.

We report evaluation results in Online Appendix H.6, which are largely consistent with our main findings with one important difference. Under moderate values of $\varepsilon ,$ although the dynamic acquisition sequence achieves better recommender system performance than random sequences under the near-domain scenario, the opposite is true under the far-domain scenario. This suggests that system values estimated in one consumption domain may have limited usefulness to inform acquisition decisions in another unrelated domain, potentially because consumer preferences and consumption behaviors across these domains can be quite different.

## 8. Discussion

As personal information becomes increasingly indispensable for the success of various products and services in the digital economy, so is the need to design marketbased mechanisms, such as data markets, to facilitate consumer acquisition. In this paper, we take a step toward designing a model of dynamic consumer acquisition for recommender systems that makes acquisition decisions based on the value of consumer participation.

## 8.1. Key Findings and Implications

Many existing studies use a privacy-centric approach and assign value of consumer participation to be the cost of privacy lost as a result of data disclosure, whereas our proposed model adopts a more comprehensive view to characterize the market dynamics of a recommender system provider (the firm) incentivizing consumers to participate in the system. First, the value of a consumer’s participation to the firm depends on how much performance improvement to the recommender system can be expected from acquiring the consumer. This allows for data-driven estimation (rather than self-reporting) of consumer values. Second, by participating in the system, a consumer also derives value from having access to personalized recommendations, which can offset the cost of participation (e.g., privacy loss due to data disclosure). Third, consumer participation not only benefits the firm, but also creates positive network externality to prospective consumers. Incorporating network externality has important impli cations on the firm’s incentive strategies and acquisition outcomes. For example, the firm can leverage part of the cumulative network externality created by participating consumers to attract prospective consumers: This gives rise to a family of ε-greedy incentive strategies that we investigate in empirical evaluations as part of this study.

Our dynamic consumer acquisition model consists of three key components. First, we theoretically characterize the decision problems faced by each market player, including the firm, the market intermediary, and the prospective consumers. Based on the theoretical framework, the firm’s acquisition decisions are formulated as a step-wise dynamic optimization problem, where the firm decides whom to acquire next based on the realized previous acquisition outcome. Second, we propose datadriven procedures to estimate consumers’ value to the recommender system, based on either their historical consumption data (if available) or other auxiliary information (e.g., demographics). For the parameters of the acquisition model that cannot be estimated based on consumption data, we discuss how their values may be assigned by the firm. Third, we design an algorithm to iteratively compute the dynamic acquisition sequence and the corresponding incentives to offer.

We evaluate the model on two real-world datasets, namely the MovieLens 100K data set and the Kelkoo data set, which represent two canonical types of recommendation tasks, that is, movie recommendation based on numeric ratings and product recommendation based on binary clicking behaviors. Furthermore, we carry out evaluations under two different schemes. The first scheme evaluates the model’s performance when consumers’ historical consumption data can be collected (potentially from a different but relevant platform), and the second scheme instead tests the model when only auxiliary information is available. Across both data sets and both evaluation schemes, we benchmark the dynamic acquisition sequence against the average random acquisition sequence, comparing them on firm utility, recommender system performance, and consumer surplus.

The evaluation results reveal a nuanced relationship between the firm’s choice of incentive strategy and the acquisition outcomes. Neither the fully greedy strategy (ε � 1) nor the constant strategy (ε � 0, where the firm extracts no externality) is optimal on all three acquisition outcomes. A fully greedy strategy allows the firm to extract more network externality from acquired consumers, which leads to higher firm utility and lower consumer surplus, but it also reduces the total number of acquired consumers, resulting in worse performance of the recommender system. A constant strategy, on the other hand, produces higher consumer surplus and higher recommender system performance at the cost of lower firm utility, because it misses the opportunity to extract utility from cumulative network externality. In fact, a moderately greedy strategy may strike an advantageous balance: We observe that the dynamic acquisition sequence outperforms random sequences on recommender system performance, firm utility, and consumer surplus simultaneously. Notably, these findings remain robust under alternative parameter specifications, distributional settings, recommender system algorithms, and the consideration of organic consumer participation. We also show that the accuracy-driven dynamic consumer acquisition does not inadvertently lead to a substantial reduction of recommendation diversity. Finally, evaluations under two cross-domain settings suggests that our dynamic acquisition method remains advantageous if consumer preferences and consumption behaviors are reasonably related across the domains (e.g., under the “near-domain” setting).

Our work contributes practical insights to dynamic consumer acquisition in recommender systems. The tradeoffs between different acquisition outcomes highlight a need for the firm to choose the incentive strategy that best serves its business objective. For example, if market expansion or recommender system quality is the top priority of consumer acquisition, then a less greedy incentive strategy may be preferred, despite incurring higher costs (i.e., total incentives) to the firm. In contrast, if the firm is financially more constrained and prioritizes immediate utility, then a more greedy strategy may be appropriate. In addition, the design artifacts proposed in this paper, including the datadriven parameter estimation procedure and the dynamic acquisition algorithm, also contribute toward practical deployment of the model.

## 8.2. Limitations and Future Research Directions

Our work represents a first step in developing the theoretical framework and design artifacts for dynamic consumer acquisition. In this part, we discuss several limitations of our approach, which give rise to several interesting future research directions that are worth pursuing.

First, the value of an acquired consumer can be highly fluid and dynamic, changing over time and as a result of various consumer activities both within and outside a particular recommender system. As a result, the system values estimated based on static data collected by the market intermediary are intended to serve as a “proxy” for the actual realized values of the consumers after acquisition. The discrepancy between realized values and estimated ones may be attributed to multiple factors. For instance, depending on the timing and frequency of the market intermediary’s data collection effort, the static data used for system value estimation may not be the most up-to-date. As another example, once a consumer is acquired, their realized system value is affected by how they interact with the firm’s recommender system (which is also time-variant) as well as the firm’s other product/service offerings.<sup>22</sup> We conduct additional exploratory analyses to gauge the impact of having outdated historical consumption data (Online Appendix I.1) and to understand how deviations between consumers’ realized and estimated values may affect acquisition outcomes (Online Appendix I.2). These analyses have produced highly consistent findings as those in our main evaluations. Nevertheless, we advocate for future research to design novel estimation methods that can leverage real-time consumption data to account for time-varying dynamics of consumer values. In the same vein, in addition to acquiring new consumers, retaining existing ones and promoting their engagement (e.g., interactions with the recommender system) are also important considerations. A joint analysis of acquisition and retention can offer more comprehensive insights into consumers’ lifetime values.

Second, when historical consumption data of the prospective consumers are not available (i.e., in the cold-start scheme), we have relied on a k-nearest neigh bor approach to predict their system values based on the (estimated) system values and auxiliary information (e.g., demographics, interests, interaction patterns) of existing consumers accessible to the market intermediary. This is essentially a supervised prediction problem. In Online Appendix J, we explore two alternative techniques, namely a neural network and a Lasso regression, for this problem. We report both the performance of system value predictions using k-NN and these two additional methods and the final acquisition outcomes. The obtained findings are similar. We believe that understanding which techniques in combination with what kinds of auxiliary information, are most predictive of consumers’ system values represents an important future research direction. Understanding the predictive power of auxiliary information also has significant practical value for the market intermediary that is often responsible for collecting such information.

Third, in the cold-start setting, we have assumed that the market intermediary has access to the consumer auxiliary information needed to estimate system values for new consumers. This assumption may not always be accurate, due to regulations, such as GDPR, that restricts the ability to collect personal data. Meanwhile, another challenge is that the consumer data collected by the market intermediary may not be fully representative of the target consumer population of the focal firm. For example, certain types of consumers may be systematically under-represented because they have higher privacy concerns. We again conduct additional evaluations to demonstrate the robustness of our approach (1) when some key consumer features are unobservable (Online Appendix K.1) and (2) when the intermediary collects a biased sample of consumers (Online Appendix K.2). We also advocate for future research to design novel acquisition algorithms that can deal with missing features or biased samples in a principled manner.

Finally, acquisition in a “far-domain” setting, where consumers’ historical data are collected from a very different consumption domain, remains a challenge. Future research may consider applying techniques from transfer learning or cross-domain recommendation to better understand and further improve acquisition performance in various cross-domain scenarios. Meanwhile, researchers can extend the proposed theoretical framework of dynamic consumer acquisition to incorporate other important market conditions, for example, the existence of multiple recommender systems providers and the competition among them, or to go beyond the context of recommender systems and consider other domains and use cases.

## Endnotes

<sup>1</sup> For example: https://www.towerdata.com/pricing and https:// datacoup.com/.

the intermediary as an “information source” (because purchasing and curating prospective consumer data are typically very costly). However, our proposed dynamic acquisition model is broadly applicable: The same exact approach for estimation and acquisition can be used by either the firm or the intermediary.

<sup>3</sup> As is the convention in the direct marketing industry, the contract between a focal firm and a market intermediary typically follows a “subscription” model—The intermediary charges a fixed rate fo each consumer list sold, which is unaffected by the firm’s subsequent consumer acquisition decisions and outcomes. Therefore, the service fee is omitted from our acquisition model.

<sup>4</sup> If the firm’s sole concern is the predictive performance of its recommender system, then its acquisition decisions are not affected by consumers’ value potentials. However, if the firm’s objective is to maximize total utility, then it is important to consider both system values and value potentials.

<sup>5</sup> Throughout this paper, we use notation s to index IDs of specific consumers, and notation i to index position of consumers in a sequence. The notation s<sub>i</sub> represents the ID of the consumer that occupies the ith position in sequence S(n).

<sup>6</sup> Although T(n) and S(n) are both sequences of consumer IDs with immutable order, we slightly abuse notation and treat them as sets when there is no confusion

<sup>7</sup> Practically speaking, the focal firm may signal the network externality to prospective consumers in different ways, which enable them to make participation decisions. For example, the firm can display aggregate statistics/trends of existing users’ activities on its front page (a practice of many online content platforms). In addition, the firm can personalize its acquisition offers with sample recommendations made based on consumers’ historical data (collected by market intermediary) to showcase the value of its recommendations.

Whether system values estimated based on historical consumption data collected from other platforms are useful for the focal firm’s acquisition decisions remain to be evaluated: We empirically test it later.

<sup>9</sup> They may be anonymous consumers in public consumption datasets (e.g., MovieLens data for movie consumptions) or previou consumers of the firm or the intermediary.

<sup>10</sup> The noise in u<sub>si</sub> can be attributed to random noise in data and randomness in the recommender system learning algorithm (e.g., random initial values).

<sup>11</sup> Revenue data: https://www.statista.com/statistics/245125/revenuedistribution-of-spotify-by-segment/; number of ad-supported users: https://www.businessofapps.com/data/spotify-statistics/.

<sup>12</sup> See https://grouplens.org/datasets/movielens/100k.

<sup>13</sup> Ideally, partition A should be collected from a different source (e.g., a different movie platform). However, users in public consumption datasets are usually anonymized, which prevents us from locating two data sources with a common set of users. We partially address this limitation using the Amazon Review Data set (Section 7.6).

<sup>16</sup> See http://archive.ics.uci.edu/ml/datasets/KASANDR.

<sup>2</sup> In practice, there are other possible ways to organize this market. For example, some intermediaries even take charge of acquiring the consumers on behalf of their client firms (e.g., they print and send offers and track acquisition outcomes). Alternatively, for a large firm with many existing consumers, it can directly purchase data of prospective consumers from data vendors to carry out value estimation and acquisitions all by itself, in order to properly account for informa tion of its existing consumers. The example setting we consider in this paper is where the focal firm executes the acquisitions (because acquisition decisions also rely on internal information of the firm that is unavailable to an intermediary, as will be discussed later), and uses <sup>15</sup> In practice, the firm can assign different weights to system values and value potentials, if they anticipate that one factor would be more important than the other in driving utility.

<sup>18</sup> Consumers who had only one interaction are included in the “early” partition. In practice, the historical data of such consumers with few activities may not be observed at all: This is considered under the cold-start evaluation scheme.

<sup>19</sup> Unlike the MovieLens data, there is no demographic information in the Kelkoo data. We instead rely on the aggregated interactions at the offer category level as a proxy for consumers’ interests in different product categories.

<sup>20</sup> With N consumers and K permutations, our estimation procedure (discussed in Section 4.1) involves building NK recommender system models to compute the performance change for each marginal consumer. Although different permutations are independent can be dealt with in parallel, having a large number of consumers and can lead to time-consuming estimations.

<sup>21</sup> In addition, we have tried (1) a cubic discounting function α<sub>i</sub> � i<sup>�3</sup> and (2) a general form $\alpha _ { i } = i ^ { - \alpha }$ where α is estimated from data. Our main findings remain qualitatively the same under both cases. See Online Appendix H.1 for details.

22 Although our proposed permutation-based method can, in principle, also be applied to update system value estimations as acquired consumers engage with the focal firm, doing so in practice faces at least two additional nontrivial challenges: (1) it requires the focal firm to constantly transmit data from acquired consumers to the market intermediary (that is responsible for system value estimation), which incurs heavy communication costs and privacy-related risks; and (2) it requires hefty computational resources, especially when there is a large number of consumers with active consumptions.

## References

Acquisti A, Brandimarte L, Loewenstein G (2015) Privacy and human behavior in the age of information. Science 347(6221):509–514.

Acquisti A, John LK, Loewenstein G (2013) What is privacy worth. J. Legal Stud. 42(2):249–274.

Acquisti A, Taylor C, Wagman L (2016) The economics of privacy. J. Econom. Literature 54(2):442–492.

Adomavicius G, Kwon Y (2011) Improving aggregate recommendation diversity using ranking-based techniques. IEEE Trans. Knowledge Data Engrg. 24(5):896–911.

Adomavicius G, Kwon Y (2014) Optimization-based approaches for maximizing aggregate recommendation diversity. INFORMS J. Comput. 26(2):351–369.

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6):734–749.

Adomavicius G, Zhang J (2012) Impact of data characteristics on recommender systems performance. ACM Trans. Management Inform. Systems 3(1):1–17.

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2018) Effects of online recommendations on consumers’ willingness to pay. Inform. Systems Res. 29(1):84–102.

Ainslie G, Haslam N (1992) Hyperbolic discounting. Loewenstein G, Elster J, eds. Choice Over Time (Russell Sage Foundation, New York), 57–92.

Anderson R, Moore T (2006) The economics of information security. Science 314(5799):610–613.

Bell RM, Koren Y (2007) Scalable collaborative filtering with jointly derived neighborhood interpolation weights. Proc. 7th IEEE Internat. Conf. on Data Mining (IEEE, Piscataway, NJ), 43–52.

Berthold S, Bo¨hme R (2010) Valuating privacy with option pricing theory. Economics of Information Security and Privacy (Springer, Berlin), 187–209.

Bi X, Qu A, Wang J, Shen X (2017) A group-specific recommender system. J. Amer. Statist. Assoc. 112(519):1344–1353.

Breese JS, Heckerman D, Kadie C (1998) Empirical analysis of predic tive algorithms for collaborative filtering. Proc. 14th Conf. on

Uncertainty in Artificial Intelligence (Morgan Kaufmann Publishers Inc., San Francisco), 43–52. https://cds.cern.ch/record/406734.

Brynjolfsson E, Hu Y, Simester D (2011) Goodbye pareto principle, hello long tail: The effect of search costs on the concentration of product sales. Management Sci. 57(8):1373–1386.

Dandekar P, Fawaz N, Ioannidis S (2014) Privacy auctions for recommender systems. ACM Trans. Econom. Comput. 2(3):12.

Dasgupta P, Maskin E (2005) Uncertainty and hyperbolic discount ing. Amer. Econom. Rev. 95(4):1290–1299.

Deodhar M, Ghosh J, Saar-Tsechansky M, Keshari V (2017) Active learning with multiple localized regression models. INFORMS J. Comput. 29(3):503–522

Donmez P, Carbonell JG (2008) Proactive learning: Cost-sensitive active learning with multiple imperfect oracles. Lim E-P, Winslett M, eds. Proc. 17th ACM Conf.on Inform. and Knowledge Man agement (Association for Computing Machinery, New York) 619–628.

Economides N (1996) Network externalities, complementarities, and invitations to enter. Eur. J. Political Econom. 12(2):211–233.

Feuerverger A, He Y, Khatri S (2012) Statistical significance of the Netflix challenge. Statist. Sci. 27(2):202–231

Frederick S, Loewenstein G, O’donoghue T (2002) Time discounting and time preference: A critical review. J. Econom. Literature 40(2): 351–401.

Funk S (2006) Netflix update: Try this at home. Accessed May 6, 2023, http://sifter.org/˜simon/journal/20061211.html.

Gantner Z, Drumond L, Freudenthaler C, Rendle S, Schmidt-Thieme L (2010) Learning attribute-to-feature mappings for cold-start recommendations. Webb GI, Liu B, Zhang C, Gunopulos D, Wu X, eds. Proc. IEEE Internat. Conf. on Data Mining (IEEE, Piscataway, NJ), 176–185. https://ieeexplore.ieee.org/xpl/conhome/ 5690658/proceeding.

Gao R, Saar-Tsechansky M (2020) Cost-accuracy aware adaptive labeling for active learning. Rossi F, Conitzer V, Sha F, eds. Proc. AAAI Conf. on Artificial Intelligence (AAAI Press, Palo Alto CA), 2569–2576.

Geva T, Saar-Tsechansky M, Lustiger H (2019) More for less: Adaptive labeling payments in online labor markets. Data Mining Knowledge Discovery 33(6):1625–1673.

Gkatzelis V, Aperjis C, Huberman BA (2015) Pricing private data. Electronic Marketing 25(2):109–123.

Goldfarb A, Tucker CE (2011) Privacy regulation and online advertising. Management Sci. 57(1):57–71

Gomez-Uribe CA, Hunt N (2015) The netflix recommender system: Algorithms, business value, and innovation. ACM Trans. Man agement Inform. Systems 6(4):1–19.

Harper FM, Konstan JA (2015) The movielens datasets: History and context. ACM Trans. Interactive Intelligent Systems 5(4):19.

He X, Liao L, Zhang H, Nie L, Hu X, Chua TS (2017) Neural collaborative filtering. Barrett R, Cummings R, Agichtein E, Gabrilovich E, eds. Proc. 26th Internat. Conf. on World Wide Web (International World Wide Web Conferences Steering Committee, Republic and Canton of Geneva, Switzerland), 173–182.

Heimbach I, Gottschlich J, Hinz O (2015) The value of user’s Facebook profile data for product recommendation generation. Elec tronic Marketing 25(2):125–138.

Hosanagar K, Fleder D, Lee D, Buja A (2014) Will the global villag fracture into tribes? Recommender systems and their effects on consumer fragmentation. Management Sci. 60(4):805–823.

Huang SJ, Chen JL, Mu X, Zhou ZH (2017) Cost-effective active learning from diverse labelers. Sierra C, ed. Proc. 26th Internat. Joint Conf. Artificial Intelligence (International Joint Conferences on Artificial Intelligence, California), 1879–1885.

Huang Z (2007) Selectively acquiring ratings for product recommendation. Gini M, Kauffman RJ, Sarppo D, Dellarocas C, Dignum F, eds. Proc. 9th Internat. Conf. on Electronic Commerce (Association for Computing Machinery, New York), 379–388.

Jain P, Gyanchandani M, Khare N (2016) Big data privacy: A tech nological perspective and review. J. Big Data 3(1):25.

Jannach D, Jugovac M (2019) Measuring the business value of recom mender systems. ACM Trans. Management Inform. Systems 10(4):1–23.

Juan Y, Zhuang Y, Chin WS, Lin CJ (2016) Field-aware factorization machines for CTR prediction. Sen S, Geyer W, Freyne J, Castells P, eds. Proc. 10th ACM Conf. on Recommender Systems (Association for Computing Machinery, New York), 43–50.

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Katz ML, Shapiro C (1986) Technology adoption in the presence of network externalities. J. Political Econom. 94(4):822–841.

Kauffman RJ, McAndrews J, Wang YM (2000) Opening the “black box” of network externalities in network adoption. Inform. Systems Res. 11(1):61–82.

Kleinberg J, Papadimitriou CH, Raghavan P (2001) On the value of private information. van Benthem J, ed. Proc. 8th Conf. on Theoretical Aspects of Rationality and Knowledge (Morgan Kaufmann Publishers Inc., San Francisco), 249–257.

Knijnenburg TA, Wessels LF, Reinders MJ, Shmulevich I (2009) Fewer permutations, more accurate p-values. Bioinformatics 25(12): i161–i168.

Komiak SY, Benbasat I (2006) The effects of personalization and familiarity on trust and adoption of recommendation agents. Management Inform. Systems Quart. 30(4):941–960.

Kong D, Saar-Tsechansky M (2014) Collaborative information acquisition for data-driven decisions. Machine Learn. 95(1):71–86.

Koren Y, Bell R, Volinsky C (2009) Matrix factorization techniques for recommender systems. Computer 42(8):30–37.

Laibson D (1997) Golden eggs and hyperbolic discounting. Quart. J. Econom. 112(2):443–478.

Lam XN, Vu T, Le TD, Duong AD (2008) Addressing cold-start problem in recommendation systems. Kim W, Choi HJ, eds. Proc. 2nd Internat. Conf. on Ubiquitous Inform. Management and Comm. (Association for Computing Machinery, New York), 208–211.

Lee D, Hosanagar K (2019) How do recommender systems affec sales diversity? A cross-category investigation via randomized field experiment. Inform. Systems Res. 30(1):239–259.

Lee D, Hosanagar K (2020) How do product attributes and reviews moderate the impact of recommender systems through pur chase stages? Management Sci. 67(1):524–546.

Lewis DD, Gale WA (1994) A sequential algorithm for training text classifiers. Bruce Croft W, van Rijsbergen CJ, eds. Proc. 17th Annual Internat. ACM-SIGIR Conf. Res. Development Inform., vol. 94 (Springer-Verlag, Berlin), 3–12.

Li C, Li DY, Miklau G, Suciu D (2014) A theory of pricing private data. ACM Trans. Database Systems 39(4):1–28.

Liebman E, Saar-Tsechansky M, Stone P (2019) The right music at the right time: Adaptive personalized playlists based on sequence modeling. Management Inform. Systems Quart. 43(3):765–786.

McAuley J, Targett C, Shi Q, Van Den Hengel A (2015) Image-based recommendations on styles and substitutes. Gey F, Hearst M, Tong R, eds. Proc. 38th Internat. ACM SIGIR Conf. on Res. and Devel opment in Inform. (Association for Computing Machinery, New York), 43–52.

Melville P, Saar-Tsechansky M, Provost F, Mooney R (2005) An expected utility approach to active feature-value acquisition. Han J, Wah BW, Raghavan V, Wu X, Rastogi R, eds. Proc. 5th IEEE Internat. Conf. on Data Mining (IEEE, Piscataway, NJ), 4.

Mohallick I, De Moor K, O<sup>¨</sup> zgo¨bek O<sup>¨</sup> , Gulla JA (2018) Toward new privacy regulations in Europe: Users’ privacy perception in recom mender systems. Wang G, Chen J, Yang LT, eds. Proc. Internat. Conf. on Security, Privacy and Anonymity in Comput., Comm. and Storage (Springer, Berlin), 319–330.

Neumann N, Tucker CE, Whitfield T (2019) Frontiers: How effective is third-party consumer profiling? Evidence from field studies. Marketing Sci. 38(6):918–926.

Nget R, Cao Y, Yoshikawa M (2017) How to balance privacy and money through pricing mechanism in personal data market. Degenhardt J, Kallumadi S, de Rijke M, Si L, Trotman A, Xu Y, eds. Proc. SIGIR 2017 eCom Workshop, vol. 15 (CEUR-WS.org, Aachen, Germany).

Ojala M, Garriga GC (2010) Permutation tests for studying classifier performance. J. Machine Learn. Res. 11(6):1833–1863.

Panniello U, Gorgoglione M, Tuzhilin A (2016) Research note—In CARSs we trust: How context-aware recommendations affect customers’ trust and other business performance measures of recommender systems. Inform. Systems Res. 27(1):182–196.

Park ST, Chu W (2009) Pairwise preference regression for cold-start recommendation. Bergman L, Tuzhilin A, Burke R, Felfernig A, Schmidt-Thieme L, eds. Proc. 3rd ACM Conf. on Recommende Systems (Association for Computing Machinery, New York), 21–28.

Parker GG, Van Alstyne MW (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10):1494–1504.

Rendle S (2012) Factorization machines with libfm. ACM Trans Intelligent Systems Tech. 3(3):1–22.

Resnick P, Iacovou N, Suchak M, Bergstrom P, Riedl J (1994) Grouplens: An open architecture for collaborative filtering of netnews. Smith JB, Don Smith F, Malone TW, eds. Proc. ACM Conf. on Comput. Supported Cooperative Work (Association for Computing Machinery, New York), 175–186.

Robinson GK (1991) That blup is a good thing: The estimation of random effects. Statist. Sci. 6(1):15–32.

Roeber B, Rehse O, Knorrek R, Thomsen B (2015) Personal data: How context shapes consumers’ data sharing with organizations from various sectors. Electronic Marketing 25(2):95–108.

Roy N, McCallum A (2001) Toward Optimal Active Learning Through Monte Carlo Estimation of Error Reduction (ICML, Williamstown, MA).

Rubens N, Kaplan D, Sugiyama M (2011) Active learning in recommender systems. Kantor P, Ricci F, Rokach L, Shapira B, eds Recommender Systems Handbook (Springer, Berlin), 735–767.

Rubinstein A (2003) “Economics and psychology”? The case of hyperbolic discounting. Internat. Econom. Rev. 44(4):1207–1216.

Saar-Tsechansky M, Provost F (2007) Decision-centric active learning of binary-outcome models. Inform. Systems Res. 18(1):4–22.

Saar-Tsechansky M, Melville P, Provost F (2009) Active feature value acquisition. Management Sci. 55(4):664–684.

Sahoo N, Singh PV, Mukhopadhyay T (2012) A hidden Markov model for collaborative filtering. Management Inform. Systems Quart. 36(4): 1329–1356.

Salakhutdinov R, Mnih A, Hinton G (2007) Restricted Boltzmann machines for collaborative filtering. Ghahramani Z, ed. Proc. 24th Internat. Conf. on Machine Learn. (Association for Comput ing Machinery, New York), 791–798.

Sandikc¸i B, Maillart LM, Schaefer AJ, Alagoz O, Roberts MS (2008) Estimating the patient’s price of privacy in liver transplantation. Oper. Res. 56(6):1393–1410.

Sarwar B, Karypis G, Konstan J, Riedl J (2001) Item-based collaborative filtering recommendation algorithms. Shen VY, Saito N, Lyu MR Zurko ME, eds. Proc. 10th Internat. Conf. on World Wide Web (Asso ciation for Computing Machinery, New York), 285–295.

Schein AI, Popescul A, Ungar LH, Pennock DM (2002) Methods and metrics for cold-start recommendations. Proc. 25th Annual Internat. ACM SIGIR Conf. on Res. and Development in Inform. (Association for Computing Machinery, New York), 253–260.

Settles B (2009) Active learning literature survey. Technical report, Department of Computer Sciences, University of Wisconsin-Madison, Madison, WI.

Sheng VS, Zhang J (2019) Machine learning with crowdsourcing: A brief summary of the past research and future directions. Proc. AAAI Conf. on Artificial Intelligence (AAAI Press, Palo Alto, CA), 9837–9843.

Sidana S, Laclau C, Amini MR, Vandelle G, Bois-Crettez A (2017) Kasandr: A large-scale data set with implicit feedback for

recommendation. Kando N, Sakai T, Joho H, Li H, de Vries AP, White RW, eds. Proc. 40th Internat. ACM SIGIR Conf. on Res. and Development in Inform. Retrieval (Association for Computing Machinery, New York), 1245–1248.

Smith B, Linden G (2017) Two decades of recommender systems at amazon. com. IEEE Internet Comput. 21(3):12–18.

Spiekermann S, Acquisti A, Bo¨hme R, Hui KL (2015a) The challenges of personal data markets and privacy. Electronic Marketing 25(2): 161–167.

Spiekermann S, Bo¨hme R, Acquisti A, Hui KL (2015b) Personal data markets. Electronic Marketing 25(2):91–93.

The Economist (2017) The world’s most valuable resource is no lon ger oil, but data. The data economy demands a new approach to antitrust rules. Leaders, The Economist (May 6), https://www. economist.com/leaders/2017/05/06/the-worlds-most-valuable resource-is-no-longer-oil-but-data.

Van Alstyne M, Parker G (2017) Platform business: From resources to relationships. GfK Marketing Intelligence Rev. 9(1):24–29.

Van den Broeck E, Poels K, Walrave M (2015) Older and wiser? Facebook use, privacy concern, and privacy protection in the life

stages of emerging, young, and middle adulthood. Soc. Media Soc. 1(2):2056305115616149.

Wang J, Ipeirotis PG, Provost F (2017) Cost-effective quality assur ance in crowd labeling. Inform. Systems Res. 28(1):137–158.

Winkler AM, Ridgway GR, Douaud G, Nichols TE, Smith SM (2016) Faster permutation inference in brain imaging. Neuroimage 141:502–516.

Xiao B, Benbasat I (2007) E-commerce product recommendation agents: Use, characteristics, and impact. Management Inform. Systems Quart. 31(1):137–209.

Zhang Y, Zhao P, Cao J, Ma W, Huang J, Wu Q, Tan M (2018) Online adaptive asymmetric active learning for budgeted imbalanced data. Guo Y, Farooq F, eds. Proc. 24th ACM SIGKDD Internat. Conf. on Knowledge Discovery & Data Mining (Association for Computing Machinery, New York), 2768–2777.

Zhang Y, Zhao P, Niu S, Wu Q, Cao J, Huang J, Tan M (2019) Online adaptive asymmetric active learning with limited budgets. IEEE Trans. Knowledge Data Engrg. 33(6):2680–2692.

Zhang Z, Li T, Ding C, Zhang X (2007) Binary matrix factorization with applications. Proc. 7th IEEE Internat. Conf. on Data Mining (IEEE, Piscataway, NJ), 391–400.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
