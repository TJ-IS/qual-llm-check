---
otero_id: 868
otero_key: "FEDPKHZH"
title: "Incorporating the Time-Order Effect of Feedback in Online Auction Markets through a Bayesian Updating Model"
authors: "Michael Chau; Wenwen Li; Boye Yang; Alice J. Lee; Zhuolan Bao"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/15324"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# INCORPORATING THE TIME-ORDER EFFECT OF FEEDBACK IN ONLINE AUCTION MARKETS THROUGH A BAYESIAN UPDATING MODEL<sup>1</sup>

Michael Chau Faculty of Business and Economics, The University of Hong Kong Pokfulam, HONG KONG {mchau@business.hku.hk}

Wenwen Li School of Management, Fudan University Shanghai, CHINA {liwwen@fudan.edu.cn}

Boye Yang Zhejiang Provincial Development and Reform Institute Hangzhou, CHINA {284028561@qq.com}

Alice J. Lee Faculty of Business and Economics, The University of Hong Kong Pokfulam, HONG KONG {alice226@connect.hku.hk}

Zhuolan Bao School of Management and Economics, The Chinese University of Hong Kong, Shenzhen Shenzhen, CHINA {baozhuolan@cuhk.edu.cn}

Online auction markets host a large number of transactions every day. The transaction data in auction markets are useful for understanding the buyers and sellers in the market. Previous research has shown that sellers with different levels of reputation, as shown by the ratings and comments left in feedback systems, enjoy different levels of price premiums for their transactions. Feedback scores and feedback texts have been shown to correlate with buyers’ level of trust in a seller and the price premium that buyers are willing to pay (Ba and Pavlou 2002; Pavlou and Dimoka 2006). However, existing models do not consider the time-order effect, which means that feedback posted more recently may be considered more important than feedback posted less recently. This paper addresses this shortcoming by (1) testing the existence of the time-order effect, and (2) proposing a Bayesian updating model to represent buyers’ perceived reputation considering the time-order effect and assessing how well it can explain the variation in buyers’ trust and price premiums. In order to validate the time-order effect and evaluate the proposed model, we conducted a user experiment and collected real-life transaction data from the eBay online auction market. Our results confirm the existence of the time-order effect and the proposed model explains the variation in price premiums better than the benchmark models. The contribution of this research is threefold. First, we verify the timeorder effect in the feedback mechanism on price premiums in online markets. Second, we propose a model that provides better explanatory power for price premiums in online auction markets than existing models by incorporating the time-order effect. Third, we provide further evidence for trust building via textual feedback in online auction markets. The study advances the understanding of the feedback mechanism in online auction markets.

Keywords: Auction markets, price premium, Bayesian updating, game theory, time-order effect, trust

## Introduction

With the rise of the internet and information technology, ecommerce has been growing quickly around the world. Online auction markets represent a popular form of ecommerce, thanks to their high efficiency in spreading information and low advertising and inventory costs. By lowering buyers’ search costs in terms of price and product features, online auction markets not only enhance competition and reduce sellers’ ability to profit from monopolies but also reduce transaction costs (Bakos 1997).

Given the large number of transactions they host, online auction markets offer an interesting test bed for analysis. By accessing information about particular products, buyers, and sellers, companies and customers can better understand the overall market environment of a product. One mechanism that provides a vast amount of data about online stores and sellers is the reputation mechanism. Most online auction market platforms, such as eBay, have electronic feedback systems. For instance, eBay’s “Feedback Forum” allows market participants to leave ratings (e.g., positive or negative) and text comments following each transaction, which are then posted as public information for future buyers. The system provides simple statistics on the ratings and lists the text comments in reverse chronological order.

It has been suggested that implementing feedback systems that record large amounts of information helps sustain trust in online auction markets (Resnick and Zeckhauser 2002). The feedback score, which is often a simple percentage of positive ratings, may provide insufficient information about the seller, whereas detailed text comments may seem overwhelming to buyers and require time and effort to review. Therefore, a more efficient means of interpreting feedback information would be beneficial to both buyers and sellers.

There is a great deal of information systems (IS) research on online auction markets (e.g., Hinz et al. 2016 and Carter et al., 2017). For example, there are many studies devoted to the relationship between feedback information and price premiums. Ba and Pavlou (2002, p. 248) argue that “buyers are willing to compensate reputable sellers with price premiums to assure safe transactions,” and suggest a concave function for price premiums based on the logarithm of the number of positive ratings and negative ratings. However, the regression does not sufficiently explain the volatility of price premiums, with an average R<sup>2</sup> of 0.14. Pavlou and Dimoka (2006) classified feedback text comments into five categories and discovered a greater impact of text comments on price premiums, with R<sup>2</sup> values as high as 0.50.

Some studies use asymmetric information economic theory and game theory to model the online reputation system. For example, Nurmi (2006) introduced a Bayesian framework to model the online reputation system, setting the belief of the reputation game to the percentage of positive ratings. Li (2010) improved the framework to represent the online reputation system as a repeated game with imperfect information—a model that is supported by many solid game theories and fits the interaction between buyers and sellers. However, neither of these two models has been evaluated using field data, which invokes doubt in terms of their applicability. Another shortcoming is that these models ignore the timeorder effect, which means that feedback posted recently may be considered more important than feedback posted a long time ago. Thus, in this paper, we propose the use of Bayesian updating to model the bidding price as a summative value of the feedback information. Our Bayesian updating model is based on asymmetric information economic theory and extensively models games with imperfect information (EGII) (Osborne 2004) while incorporating the time-order effect.

Our research has two major objectives. First, we aim to verify the existence of the time-order effect on price premiums in online auction markets through a user experiment. Second, we aim to assess the explanatory power of the time-order effect on price premiums through a Bayesian updating model. The remainder of the paper is organized as follows. We first examine the literature and theoretical background of information asymmetry theory, repeated games with imperfect information in game theory, trust, and price premiums. We then discuss our hypotheses, propose our Bayesian updating model and present a user experiment designed to verify the time-order effect. Next, we report a study using field data from eBay that compares the Bayesian updating model with benchmark models. In the final section, we discuss the implications and limitations of our research and suggest some directions for future research.

## Literature Review and Theoretical Background

Sellers and buyers in online auction markets do not have the same information—the sellers always possess more information about the quality of the product than the buyers. This condition, called information asymmetry, often results in problems such as adverse selection (e.g., a buyer making a purchase decision based on misrepresented seller or product attributes) and moral hazard (e.g., a buyer encountering issues such as contract default or fraud following purchase) (Pavlou et al. 2007). Information asymmetry theory models this situation and suggests some constraints to prevent market failure. Feedback mechanisms enabling buyers to leave feedback about transactions and assisting potential buyers in evaluating whether sellers are trustworthy represent one of the most popular mechanisms in online markets for mitigating information asymmetry.

Trust is a bridge that links sellers and buyers and is one of the most important concepts in e-commerce research. Research shows that trust can be built based on ratings and text comments left by previous buyers who have transacted with the seller (Ba and Pavlou 2002; Pavlou and Dimoka 2006). It has also been shown that the level of trust can predict the price premiums that buyers are willing to pay (Ba and Pavlou 2002). The following subsections examine some related research work in these areas, which provide the theoretical background of the hypotheses and model presented subsequently.

## Information Asymmetry Theory and Game Theory

Many studies in information economics involve asymmetric information situations, meaning that one agent has more information about something than the other. Information asymmetry can lead to adverse selection issues—for example, when sellers manipulate transactions based on their information about product quality. Buyers can protect themselves from adverse selection by identifying signals about sellers prior to making transactions. Feedback systems can help alleviate the adverse selection problem in online auction markets (Pavlou et al. 2007) by allowing the less informed side (i.e., buyers) to access additional information. The feedback system is based on signaling theory. The signal from one type of seller is difficult for other types of sellers to imitate in a successful signaling mechanism (Spence 1973).

Reputation is the signal used in online auction markets (Zhou 2004) that can help buyers infer the quality of the targeted seller based on previous transactions. Feedback systems allow buyers to leave their feedback after each transaction. Combined, this buyer feedback forms the rating profile of each seller. Dellarocas (2005) undertook a systematic exploration of reputation mechanism design in online markets based on opportunistic sellers of “common known cost and ability parameters, [and] imperfect monitoring of a seller’s actions” (p. 209).

Dellarocas postulated two possible effort levels (high vs. low) of a seller and investigated whether the objective of the reputation mechanism—i.e., to induce the sellers to expend the highest level of effort possible—in such a pure moral hazard environment is satisfied by examining the impact of various market efficiency parameters, including “the granularity of solicited feedback, the format of the public reputation profile, the policy regarding missing feedback, and the rules for admitting new sellers” (Dellarocas 2005, p. 210). They reported an interesting and profound finding that the maximum efficiency may be reduced by the probability that even obliging sellers may unfairly receive bad ratings.

Repeated transactions in online auction markets resemble an extensive game with imperfect information (EGII) (Osborne 2004). One of the most important elements in EGII is the belief function. The belief of a buyer is the probability that the buyer mentally constructs, based on historic information, that the subject is of a certain type— for example, a good car in a used car market or a seller who expends high levels of effort to ensure the quality of the product in an online auction market. Assuming that positive and negative feedback represent the signals in online auction markets, it is possible to construct a belief function based on Bayesian theory (Li 2010). However, such models have not been validated by empirical data in previous research.

## Trust

Sellers always possess more information about the quality of the service or products they provide than buyers in an asymmetric information situation (Mishra et al. 1998). The low barrier to enter online auction markets and the ease of registering new accounts using self-reported information may give rise to a particular kind of opportunism defined as “self-interest seeking with guile” (Williamson 1987). Opportunism can exacerbate the mistrust of buyers toward sellers and even jeopardize the online auction market itself (Jarvenpaa and Tractinsky 1999; Whinston et al. 1997). The lack of trust in a market could destroy it (Granovetter 1985), while a high level of trust could help make it more sustainable (Adler 2001). Therefore, trust is a critical factor impacting online market efficiency. Given the existence of asymmetric information, trust may play a more significant role than price in influencing demand (Zhou 2004).

In the field of information systems, trust is considered to be as significant for building e-commerce markets as it is in the development of traditional markets (Ba et al. 2003). Two types of trust are recognized in the literature (Doney and Cannon 1997; Ganesan 1994): namely, benevolence and credibility. According to Ba and Pavlou (2002, p. 246), benevolence is the belief that “one partner is genuinely interested in the other partner’s welfare and has intentions and motives beneficial to the other party” without any prefixed commitment and regardless of the potential for opportunism. Credibility is the belief that the “counterparty is honest, reliable, and competent” to fulfill any explicit and implicit requirements of the transaction. Ba and Pavlou argue that credibility is the main source of trust in online auction markets.

In addition to the individual-based trust of the seller, institution-based trust (i.e., the buyer’s perception that the marketplace possesses effective third-party institutional mechanisms to facilitate transaction success) is commensurately significant for engendering buyers’ trust in the online auction market (Pavlou and Gefen 2004). In particular, it has been suggested that three institutional mechanisms lead to institution-based trust: feedback mechanisms, third-party escrow services, and credit card guarantees. Furthermore, the buyer’s trust toward the entire community of sellers as a group also reduces the perceived risk associated with online transactions. Pavlou and Gefen’s (2004) empirical study demonstrates the effectiveness of institutional mechanisms using longitudinal data. Their study provides evidence that these mechanisms boost trust in the entire community of sellers and explains why online marketplaces are proliferating in spite of the uncertainties associated with online transactions (Pavlou and Gefen 2004).

Research has demonstrated that the interaction of social preferences and a cleverly designed reputation system can address the trust issue in online auction markets (Bolton et al. 2004b). Feedback systems can lead to obvious improvements in transaction efficiency (Bolton et al. 2004a) and are recognized as a technology that can build trust and inspire cooperation in online markets (Dellarocas 2003). It has been suggested that the costs involved in giving reliable feedback determine the trade gains that are achieved in equilibrium. However, buyers’ insurance, which is offered by some online auction markets, would affect trading dynamics and thus the ultimate equilibrium. In certain cases, buyers’ insurance may be even more important than established trust in online auction markets (Güth et al. 2007).

## Price Premium

The price premium is defined as the price that yields an above-average profit (Klein and Leffler 1981; Shapiro 1983). In online auction markets, the price premium is the monetary amount above the average price received by sellers for a certain homogenous product (Ba and Pavlou 2002). One of the major sources of price premiums is the buyer’s willingness to compensate reliable sellers for the likelihood of reduced risk (Ba and Pavlou 2002).

According to game theory, positive feedback induces trust from buyers toward sellers, who have an intrinsic motivation to protect their reputation (Greif 1989; Milgrom et al. 1990), whereas negative feedback has a damaging effect (Li and Hitt 2008; Webster and Sundaram 1998). Specifically, negative ratings lead to lower bidding prices in online auctions (Lee et al. 2000). As discussed above, buyers expect sellers with excellent reputations to be less likely to risk damaging their reputations by exploiting a single transaction (Scott and Derlaga 1983). Ba and Pavlou (2002) proposed a model to investigate the relationship between ratings and price premiums. Their experiment on field data from eBay confirmed the favorable effect of positive ratings on price premiums; however, their testing left the negative impact of negative ratings on price premiums unclear. Dellarocas (2003) posits that the impact of feedback profiles on price premiums is relatively higher for riskier transactions and more expensive products, while the overall number of positive ratings and negative ratings appears to be the most influential factor for all feedback information published on eBay.

Research also suggests that a single-point estimation based on ratings or feedback scores might be insufficient to predict the true quality of the seller because of the underreporting of moderate reviews (Hu et al. 2006). Therefore, Pavlou and Dimoka (2006) examined finegrained feedback information such as text comments to determine the significance of such feedback for engendering buyers’ trust in a seller’s benevolence and credibility. By dichotomizing text comments along two dimensions—i.e., outstanding vs. abysmal / credibility vs. benevolence—Pavlou and Dimoka revealed the significance of text comments for explaining greater variance in price premiums, thus suggesting that the success of online auction markets is primarily reliant on text comments that enable buyers to distinguish good sellers from bad sellers.

In addition to bidding price and seller reputation, another factor that is indispensable for the robustness of online markets is understanding the true quality of the product. Some findings indicate that while online seller reputation is effective for identifying good-faith sellers, reputable sellers do not necessarily sell products of better quality. Jin and Kato (2006) ascribe this strange data pattern to two features of the eBay rating system: i.e., “universal ratings” and “costless switching of anonymous online identities,” which infer the significance of text comments in order to complement the rating system. A number of empirical studies have delved into eBay data sets to identify the influence of reputation systems on bidding price. Most of these studies report that higher seller reputations result in higher transaction prices (e.g., Houser and Wooders 2006; McDonald and Slawson 2002. For a more detailed review, see Resnick et al. 2006).

## Time-Order Effect

One shortcoming of existing models is that they do not differentiate between feedback submitted at different times. For example, under existing models, a seller who has 2 negative ratings from a long time ago followed by 50 positive ratings would have the same reputation as a seller who has 50 positive ratings followed by 2 recent negative ratings. A buyer would probably perceive higher risk associated with the seller with 2 recent problematic transactions because the recent ratings may be a better indicator of the seller’s future performance. To make judgments on the probability of a future event (e.g., whether the seller will satisfactorily complete the transaction), individuals often rely on heuristics. One heuristic often used is the representativeness heuristic, which is the degree to which a current event “is similar in essential characteristics to its parent population” (Kahneman and Tversky 1972). Since recent past events have greater temporal similarity to current events, a buyer will likely assume that a seller with recent negative feedback would be more likely to perform poorly in subsequent transactions. Similarly, since distant past events have less temporal similarity with current events, buyers will likely consider negative feedback about a seller that was left a long time ago to be less relevant to the current transaction. Therefore, the impact of negative feedback posted a long time ago is likely to be weaker than feedback posted recently. We call this the “timeorder effect.”

In this study, we focus on the time-order effect in the online auction context and seek to understand the impact of the time order of review feedback. Our research thus fills a significant research gap by examining whether consumer behaviors are influenced by the time-order effect. To the best of our knowledge, our study is the first to incorporate the time-order effect into the Bayesian updating model to measure this effect empirically.

## Hypotheses Development

## Existence of the Time-Order Effect

Our first hypothesis suggests that a time-order effect exists in the feedback mechanisms of online auction markets. As discussed above, when buyers make judgments, they likely rely on representativeness heuristics to assess how the current transaction is similar to previous transactions. Since more recent transactions are temporally similar to the current transaction, we expect that recent feedback has a higher impact on price premiums. Therefore, we posit a time-order effect for the ratings left as feedback in online auction markets. Since seller profiles primarily consist of positive feedback and buyers are much more sensitive to negative feedback (Lee et al. 2000), we focus on the time-order effect of negative feedback and hypothesize the following:

Time-Order Effect Hypothesis (H1): A time-order effect exists for online feedback. Specifically, more-recent negative feedback on the seller has a larger negative impact than less-recent negative feedback on the buyer’s trust (H1a), purchase intention (H1b), and price premium (H1c).

In addition, another effect may appear with the feedback mechanism. Feedback is typically presented as a list on online auction sites. Previous studies have shown that, when presented with a list of items, people tend to rank items that appear near the top of list higher, a phenomenon known as the primacy effect (Becker 1954; Cabanac and Preuss 2013). Thus, if a buyer browses a list of comments from top to bottom in chronological order, a negative comment near the top of the list may induce a larger reduction in trust than a comment further down. We call this the “display-order effect.” We carefully designed our experiment to separate the display-order effect from the time-order effect in the analysis.

## Bayesian Updating Model

In addition to verifying the existence of the time-order effect, we further examine how the time-order effect explains buyers’ trust and price premiums in online auction markets by presenting an empirical model. We developed our Bayesian updating model by applying a model based on information asymmetry theory and revising the Bayesian belief function in terms of an extensive game with imperfect information to fit into the feedback system in online auction markets. We also incorporated the time-order effect into the model.

An online auction per se can be interpreted as an extensive game with imperfect information because it meets the characteristics of such a game: from the perspective of the buyer, the type of the seller is determined by chance, and buyers can leave feedback after each transaction<sup>2</sup> so that successive buyers can update their perceptions of the seller’s reputation. As discussed above, the outcome of the transaction is probabilistic depending on the seller (Osborne 2004). We assume two types of sellers—good sellers and bad sellers (Li 2010). Good sellers fulfill their commitments and exert high levels of effort to ensure the quality of transactions, whereas bad sellers exert low levels of effort in guaranteeing the quality of transactions. However, even good sellers cannot fully guarantee the outcome of transactions because random factors always exist, e.g., shipping delays and unintentional errors. Without loss of generality, we assume two types of outcomes—positive feedback and negative feedback. By simply observing the feedback, a buyer can conclude that the seller receiving positive feedback is a good seller and a seller receiving negative feedback is a bad seller because these are probabilistic events.

To set up our model, let  be the set of the types of sellers;  be the set of all types of feedback information (signals); $P ( \delta \mid { \mathbf { \Omega } } { \omega } )$ be the probability that the subject is of type $\delta$ conditional on signal $\omega ;$ $P ( \omega | \delta )$ be the prior probability that a signal is  if the subject is of type $\delta ;$ and $P _ { t } \left( \delta \right)$ be the probability that the seller is of type at time t. When $t = 0 , P o \left( \delta \right)$ means the unconditional probability that the seller is of type $\delta$ at the beginning. Then, with the appearance of every new signal $\omega ,$ the buyer’s belief about the seller’s reputation will be updated based on the feedback information according to Bayesian theory (Li 2010):

$$
\begin{array}{l} P _ {t + 1} (\delta \mid \omega) = \frac {P (\omega \mid \delta) P _ {t} (\delta)}{\sum_ {\delta \in \Delta} P (\omega \mid \delta) P _ {t} (\delta)} \\ \text { subject   to } \sum_ {\delta \in \Delta} P _ {t} (\delta) = 1 \\ \sum_ {\omega \in \Omega} P (\omega \mid \delta) = 1 \\ \text { where } \Delta = \{G, B \} \end{array}\tag{1}
$$

Here is a new signal at time $t { + } 1$ . In many online auction sites, buyers can leave two types of information after a transaction: a numerical rating and a text comment. The feedback profile is established based on these two “building blocks.” This study examines the impact of these two different types of information. When based on ratings, the belief function is appended by one condition, $\Omega _ { \mathrm { r a t i n g } } = \{ \mathrm { P o s i t i v e } .$ , Negative}. Our study ignores neutral and withdrawn ratings. In line with Pavlou and Dimoka (2006), when based on the category of text comments, the above condition is replaced by the following set consisting of the categories of text comments:

$$
\Omega_ {\text { text }} = \{\mathrm{OC}, \mathrm{AC}, \mathrm{OB}, \mathrm{AB}, \mathrm{Ord} \},
$$

where OC stands for outstanding credibility, AC for abysmal credibility, OB for outstanding benevolence, AB for abysmal benevolence, and Ord for ordinary (Pavlou and Dimoka 2006). Table 1 lists some examples of each category extracted from Pavlou and Dimoka’s study.

We compute the reputation level $R _ { t } ,$ which represents buyers’ perceived reputation level of a seller at period $t ,$ through the Bayesian updating model, using the input of all ratings left by buyers prior to the transaction under examination. For a seller without a ratings profile, let the reputation of the seller be the unconditional probability that the seller is of type $d$ at the beginning and let it be a constant γ:

$$
\begin{array}{c} R _ {0} = P _ {0} (\delta = G) \\ = \gamma \end{array}\tag{2}
$$

<table><tr><td>Table 1. Examples of Text Comments in each Category (Pavlou and Dimoka 2006)</td></tr><tr><td>Examples of Outstanding Credibility text comments</td></tr><tr><td>1. Extremely prompt seller. I was thrilled with the speed of the service I received.</td></tr><tr><td>2. Super fast transaction and delivery. Excellent Seller!</td></tr><tr><td>3. Lightening fast delivery. Got product one day after auction ended!</td></tr><tr><td>Examples of Abysmal Credibility text comments</td></tr><tr><td>1. Overnight shipping took 2 weeks! Useless seller.</td></tr><tr><td>2. Product was damaged during shipping because of bad packaging. Inept seller.</td></tr><tr><td>3. Seller decided to default auction because she miscalculated products in hand.</td></tr><tr><td>Examples of Outstanding Benevolence text comments</td></tr><tr><td>1. Seller went out of his way to proactively accommodate my own bidding error!</td></tr><tr><td>2. Seller went the extra distance to resolve several recurring issues with Paypal.</td></tr><tr><td>3. Seller was really tolerant and did not take advantage of my bidding error.</td></tr><tr><td>Examples of Abysmal Benevolence text comments</td></tr><tr><td>1. Seller collects payment and does not send expensive items. Buyer Beware!</td></tr><tr><td>2. Product&#x27;s condition profoundly misrepresented; this is a copied CD, not original;</td></tr><tr><td>3. Fraud! Seller never shipped the palm pilot after receiving my full payment.</td></tr><tr><td>Examples of Ordinary text comments</td></tr><tr><td>1. Nice seller, great job.</td></tr><tr><td>2. Very good customer service. Great Seller.</td></tr><tr><td>3. Nice product, smooth transaction, pleasure to deal with this seller all the time.</td></tr></table>

Let be the probability of a good seller receiving a positive rating $( \mathrm { i . e . , } P ( \omega { = } P o s i t i \nu e / \delta { = } G ) )$ , and $\beta$ be the probability of a bad seller receiving a positive rating $( \mathrm { i . e . }$ $P ( \omega { = } P o s i t i \nu e / \delta { = } B ) )$ . For a new rating ω (positive rating or negative rating) received at time t, the formula to calculate an updated reputation level $R _ { t }$ from the feedback rating and the reputation level $R _ { t - I }$ right before receiving the feedback can be derived based on Bayesian updating as follows:

$$
R _ {t} = \left\{ \begin{array}{l l} \frac {\alpha R _ {t - 1}}{\alpha R _ {t - 1} + \beta (1 - R _ {t - 1})} & \text { if } \omega = \text { Positive } \\ \frac {(1 - \alpha) R _ {t - 1}}{(1 - \alpha) R _ {t - 1} + (1 - \beta) (1 - R _ {t - 1})} & \text { if } \omega = \text { Negative } \end{array} \right.\tag{3}
$$

$$
\begin{array}{c} \text { where } \alpha = P (\omega = \text { Positive } \mid \delta = G), \\ \beta = P (\omega = \text { Positive } \mid \delta = B). \end{array}
$$

When text comments are used as the input, each comment is manually classified based on its content. As discussed above, we use the five categories of text comment types defined in Pavlou and Dimoka (2006): namely, outstanding credibility (OC), abysmal credibility (AC), outstanding benevolence (OB), abysmal benevolence (AB), and ordinary (Ord) comments. The compact formula to derive reputation level from these five text comment categories is:

$$
R _ {t} = \left\{ \begin{array}{l l} \frac {\alpha_ {O C} R _ {t - 1}}{\alpha_ {O C} R _ {t - 1} + \beta_ {O C} (1 - R _ {t - 1})} & \text { if } \omega = \mathrm{OC} \\ \frac {\alpha_ {A C} R _ {t - 1}}{\alpha_ {A C} R _ {t - 1} + \beta_ {A C} (1 - R _ {t - 1})} & \text { if } \omega = \mathrm{AC} \\ \frac {\alpha_ {O B} R _ {t - 1}}{\alpha_ {O B} R _ {t - 1} + \beta_ {O B} (1 - R _ {t - 1})} & \text { if } \omega = \mathrm{OB} \\ \frac {\alpha_ {A B} R _ {t - 1}}{\alpha_ {A B} R _ {t - 1} + \beta_ {A B} (1 - R _ {t - 1})} & \text { if } \omega = \mathrm{AB} \\ \frac {\alpha_ {O r d} R _ {t - 1}}{\alpha_ {O r d} R _ {t - 1} + \beta_ {O r d} (1 - R _ {t - 1})} & \text { if } \omega = \mathrm{Ord} \\ \text { where } \alpha_ {O C} = P (\omega = \mathrm{OC} | \delta = G), \\ \beta_ {O C} = P (\omega = \mathrm{OC} | \delta = B), & \text { and } \\ \alpha_ {A C}, \alpha_ {O B}, \alpha_ {A B}, \alpha_ {O r d}, \beta_ {A C}, \beta_ {O B}, \beta_ {A B}, \beta_ {O r d} \end{array} \right.\tag{4}
$$

Equations (3) and (4) can be generalized as follows for any given feedback ω':

$$
\begin{array}{c} R _ {t} = \frac {\alpha_ {\omega^ {\prime}} R _ {t - 1}}{\alpha_ {\omega^ {\prime}} R _ {t - 1} + \beta_ {\omega^ {\prime}} (1 - R _ {t - 1})} \\ \text { where } \alpha_ {\omega^ {\prime}} = P (\omega = \omega^ {\prime} \mid \delta = G), \\ \beta_ {\omega^ {\prime}} = P (\omega = \omega^ {\prime} \mid \delta = B). \end{array}\tag{5}
$$

To incorporate the time-order effect into the Bayesian updating model, we introduce a time-order coefficient λ into the model. The reputation level of a seller can be calculated as follows:

$$
\begin{array}{r} R _ {t} = \lambda \frac {\alpha_ {\omega^ {\prime}} R _ {t - 1}}{\alpha_ {\omega^ {\prime}} R _ {t - 1} + \beta_ {\omega^ {\prime}} (1 - R _ {t - 1})} + (1 - \lambda) R _ {0} \\ \mathrm{where} \alpha_ {\omega^ {\prime}} = P (\omega = \omega^ {\prime} | \delta = G), \\ \beta_ {\omega^ {\prime}} = P (\omega = \omega^ {\prime} | \delta = B), \\ 0 \leq \lambda \leq 1. \end{array}\tag{6}
$$

The time-order factor λ determines the weight of the reputation score according to the order of the feedback. The value of λ indicates how much information will be retained as time goes on. The larger the value, the less the information is discounted. From another point of view, since the reputation level of a seller is calculated by iterating from $R _ { 1 }$ , introducing λ to Equation (5) can result in an exponential decay of $R _ { t } .$ To address the issue, we introduce $( 1 - \lambda ) R _ { 0 }$ as a correction term. Therefore, we now smooth the conditional seller reputation (given feedback) by interpolating it with the unconditional seller reputation $R _ { 0 }$ . The smoothing helps compensate for information loss and possible inaccuracies in the original conditional probability, mainly in terms of buyers’ neglecting to review feedback information.

## Price Premium

Thus far, we have hypothesized the existence of the timeorder effect in consumers’ online review consumption and presented a model of the sellers’ reputation, as perceived by buyers. Next, we discuss how buyers react to perceived reputation, taking the time-order effect into account. After the reputation is calculated by the Bayesian updating model with the time-order effect in Equation (6), regression analysis can be performed with price premiums (PP) as the dependent variable:

$$
P P = \theta_ {0} + \theta_ {1} R _ {t} + \varepsilon\tag{7}
$$

The independent variable is the reputation level from the Bayesian updating model calculation. The reputation level can be calculated based on either feedback ratings or text comments. We call these two models BU-Ratings and BU-Text, respectively.

The second hypothesis is related to the impact of the timeorder effect on the price premium. Auction markets provide a pricing mechanism that allows buyers to compete to determine the bidding price; this mechanism involves buyers’ sensitivity to the sellers’ reputations (Ba and Pavlou 2002). In other words, the higher the reputation level of the seller, the more significant the price premium is expected to be. Based on this, we propose our second hypothesis:

Positive Effect Hypothesis (H2): A higher seller reputation—computed using the proposed model, based on feedback ratings (H2a) or on the categories of text comments (H2b)—correlates with a larger price premium for the seller.

In addition, we expect that seller reputation computed using the proposed model better explains variation in price premium, as compared to the benchmark regression models—i.e., regression models based on the number of positive and negative ratings (Ba and Pavlou 2002) and on the number of different categories of text comments (Pavlou and Dimoka 2006). This motivates our third hypothesis.

Explanatory Power Hypothesis (H3): The regression model on seller reputation derived from the proposed model—which incorporates the time-order effect, based on feedback ratings (H3a) or on the categories of text comments (H3b)—explains the variation in price premium better than benchmark regression models.

## Study 1: User Experiment

We conducted two studies to test our hypotheses. Study 1 utilizes a user experiment to verify the existence of the timeorder effect hypothesized in H1, and Study 2 uses field data from eBay.com to examine whether integrating the timeorder effect would cause buyers to perceive a higher seller reputation and thus lead to a larger price premium. In addition, we also assessed the reliability of our proposed model using field data.

Four products were chosen for our user experiment: two expensive and two inexpensive products, following the practice in previous research (Ba and Pavlou 2002). For the two expensive products, we chose a Canon EOS 70D digital SLR camera (\$1,099.00) and an Apple Watch Sport (\$310.00). For the two inexpensive products, we chose a book, The 7 Habits of Highly Effective People (\$10.40), and a set of 5 DVDs entitled True Blood: The Complete First Season (\$12.99).

## Experiment Setup

On web pages showing seller profiles, buyer feedback is often presented in a list, with more-recent feedback displayed at the top of the list and less-recent feedback displayed at the bottom. This results in the confounding of the display-order effect and the time-order effect, as we cannot determine whether a buyer considers a piece of feedback important because it is displayed on top or because it is recent. Therefore, we designed a 2 by 2 experiment to test the time-order effect while controlling for the display-order effect. The design has two values for each of the two factors. One factor is time order with two possible values (more recent vs. less recent). The other factor is display order with two possible values (top vs. bottom). As such, we designed four types of sellers’ profiles for the four groups in the experiment. We measured trust, purchase intention, and the price that customers would be willing to pay for the product.

We recruited 261 users from Amazon Mechanical Turk to participate in the experiment (Hibbeln et al. 2017; Kane and Ransbotham 2016; Moreno and Terwiesch 2014). After discarding 21 invalid responses, we collected a total of 240 valid responses for use in our analysis. Participants were evenly randomly assigned to four different groups. In each group, a participant was presented with four products in randomized order. For each product, a seller profile and the product’s suggested market price were shown to the participant. The most recent 25 ratings for each profile were shown to the participant and included 24 positive ratings and 1 negative rating.<sup>3</sup>

These 25 ratings had different time and display orders for different groups. In other words, the four groups were shown four different types of seller profile displays: (1) the negative rating is the most recent in time (among the 25 ratings) and is displayed on the top of the feedback list; (2) the negative rating is the most recent and is displayed at the bottom of the feedback list; (3) the negative rating is the least recent and is displayed on the top of the feedback list; and (4) the negative rating is the least recent and is displayed at the bottom of the feedback list. Other than these manipulations, the user interfaces used in the experiment were the same as those used by eBay. An example is shown in Figure 1. In this figure, the negative rating is the most recent in time and is displayed at the top of the feedback list. It should be noted that, while there are four tabs in the interface, the participants were not allowed to navigate to the other tabs.

For each product, the participants were asked to answer questions regarding their trust toward the seller and their purchase intention. Our three questions on trust (from Ba and Pavlou 2002) were measured using a 5-point Likert scale (Cronbach’s alpha = 0.928). The participants were asked to give the price they would be willing to pay for the product based on the suggested price. We then measured the price premium by subtracting the suggested price for each product from the price that the participant was willing to pay, divided by the suggested price.

## Results

Sixty valid responses were collected for each of the four groups. To determine whether the randomized groups had balanced characteristics, we ran ANOVA tests on five control variables. The results show no significant differences among the four groups in age (p = 0.934), gender (p = 0.604), income (p = 0.341), previous experience with online auctions (p = 0.445), and previous experience with eBay purchases (p = 0.550).

Our analyses first focused on the time-order effect. We compared the two groups for which the negative rating was the most recent rating (Groups 1 and 2) with the two groups for which the negative rating was the least recent rating (Groups 3 and 4). The mean of each of the dependent variables (i.e., trust, purchase intention, and price premium) of the four products was determined for each participant in the analysis. The results are summarized in Table 2. Table 2 shows that buyers exhibited an overall lower level of trust (3.808) toward sellers with more-recent negative feedback versus those with less-recent negative feedback (4.208).

<table><tr><td colspan="3">Feedback received (viewing 1-25)</td></tr><tr><td></td><td colspan="2">Period: All</td></tr><tr><td>Feedback</td><td>From/price</td><td>Date/time</td></tr><tr><td>First watch was broken and shipped to wrong address. The 2nd watch never came (#120866871251)</td><td>Buyer: jp666 (120 ★)US $145.00</td><td>During past monthView Item</td></tr><tr><td>best price fast fast shipping (#120863127791)</td><td>Buyer: zachary6502 (817 ★)US $148.00</td><td>During past monthView Item</td></tr><tr><td>Fast shipping, easy to work with!!! Thanks (#120864590973)</td><td>Buyer: waynejm194z (850 ★)US $152.00</td><td>During past monthView Item</td></tr><tr><td>No damage. Good transaction. No problems. (#120862770157)</td><td>Buyer: gkw1972 (83 ★)US $121.00</td><td>During past 6 monthsView Item</td></tr><tr><td>fast shipping . Great price, Thanks! (#120848616148)</td><td>Buyer: markwait440 (538 ★)US $115.50</td><td>During past 6 monthsView Item</td></tr><tr><td>Item as advertised. (#120865560808)</td><td>Buyer: rkiyomoto (2968 ★)US $100.00</td><td>During past 6 monthsView Item</td></tr><tr><td>Shipped promptly and as expected! Excellent transaction! (#120862162665)</td><td>Buyer: rubyandjethro (373 ★)US $130.00</td><td>During past 6 monthsView Item</td></tr><tr><td>Fast shipping, good deal, thanks! (#120862765239)</td><td>Buyer: finditfaster (6229 ★)US $123.00</td><td>During past 6 monthsView Item</td></tr><tr><td>Great Ebay Seller. Thanks. (#120858238527)</td><td>Buyer: lonxon1978 (119 ★)US $120.00</td><td>During past 6 monthsView Item</td></tr><tr><td>This package came amazingly fast, perfect condition, works beautifully (#120856081925)</td><td>Buyer: kzoocarpenter (16 ★)US $125.00</td><td>During past 6 monthsView Item</td></tr><tr><td>received in good time (#120854229301)</td><td>Buyer: recycle_world (786 ★)US $126.00</td><td>During past 6 monthsView Item</td></tr><tr><td>Hi thanks for the fast and quick delivery, seller recommended. (#120849635082)</td><td>Buyer: asmadaghar (282 ★)US $130.00</td><td>During past 6 monthsView Item</td></tr><tr><td>easy transaction and fast postage (#120852252580)</td><td>Buyer: anaeh5 (109 ★)US $132.00</td><td>During past 6 monthsView Item</td></tr></table>

Figure 1. An Example of the User Interfaces Used in the Experiment

<table><tr><td colspan="4">Table 2. Buyer's Trust, Purchase Intention, and Price Premium (n=240)</td></tr><tr><td></td><td>Seller with more-recent negative feedback</td><td>Seller with less-recent negative feedback</td><td>p-value of t-test</td></tr><tr><td>Trust</td><td>3.808</td><td>4.208</td><td>&lt; 0.001</td></tr><tr><td>Purchase intention</td><td>3.766</td><td>4.125</td><td>&lt; 0.001</td></tr><tr><td>Price premium</td><td>-22.6%</td><td>-7.1%</td><td>&lt; 0.001</td></tr><tr><td colspan="4">Table 3. ANOVA Test Results</td></tr><tr><td></td><td>Source of variation</td><td>F</td><td>p-value</td></tr><tr><td rowspan="2">Trust</td><td>Time order</td><td>20.466</td><td>&lt; 0.001</td></tr><tr><td>Display order</td><td>3.553</td><td>0.061</td></tr><tr><td rowspan="2">Purchase intention</td><td>Time order</td><td>11.885</td><td>&lt; 0.001</td></tr><tr><td>Display order</td><td>2.320</td><td>0.129</td></tr><tr><td rowspan="2">Price premium</td><td>Time order</td><td>24.785</td><td>&lt; 0.001</td></tr><tr><td>Display order</td><td>0.084</td><td>0.772</td></tr></table>

Similarly, our results show that buyers are less likely (3.766) to buy from sellers with more-recent negative feedback than those with less-recent negative feedback (4.125). In addition, we found that the price buyers were willing to pay was lower (i.e., a more negative price premium, -22.6%) for products sold by sellers with morerecent negative feedback than for products sold by sellers with less-recent negative feedback (-7.1%). We ran t-tests for the comparisons and the differences are statistically significant $( p < 0 . 0 0 1 )$ in all cases, thus confirming H1. In order to separate the display-order effect from the timeorder effect in the analysis, we conducted a two-way ANOVA test based on these two factors. The results (summarized in Table 3) show that the time-order effect is significant (p < 0.001) while the display-order effect is insignificant (p > 0.05) for all three dependent variables. Therefore, the results again indicate the significant impact of the time-order effect, confirming H1.

Since the participants provided responses to four products, they could potentially learn about the display pattern of the reviews based on previously viewed products, potentially affecting participants’ responses in the experiment. Because of this concern, we conducted a robustness test that avoided the “learning effect” of participants by using only their responses on the first randomly assigned product. More specifically, although each of our 240 participants provided four sets of responses, we only used the first set of responses for this robustness test. The test results are consistent with our original findings and all statistically significant relationships remain significant at the 0.001 level.

## Study 2: Field Data from eBay

This section assesses the proposed model and tests H2 and H3 by using field data collected from eBay. We discuss the data collection procedure, present descriptive statistics, and elaborate the regression model that is designed to examine the impact of perceived reputation calculated from our Bayesian updating model. Since eBay offers two types of feedback information, we ran the regression model on the feedback ratings and text comments, respectively. In addition, we used benchmark regression models on the same data set to evaluate the effectiveness of our proposed model.

## Data Collection and Data Set

Since the data analysis aims to examine the effectiveness of the proposed model, we needed a list of transactions, including the bidding price and feedback information. The data were collected from eBay.com, one of the most popular online auction markets. Beyond the four products used in Study 1, we added eleven new products for Study 2, for a total of 15 products. These products were chosen based on two criteria: (1) sufficient popularity in the online market to ensure a large enough sample size of transactions, and (2) a sufficiently specific product description to ensure that products sold by different sellers were actually identical products.

To prepare the data set, we used the search function provided by the eBay API to find the list of current sellers for each of the fifteen products. We used a program written in Java to read the list of seller IDs and retrieve the transaction history and feedback information of each seller. We also extracted details of each transaction, including buyer ID, item title, transaction price, rating scores, numbers of positive and negative ratings, and text comments. Following Ba and Pavlou (2002), we examined the item title to ensure that each item was exactly the same as the target product in order to exclude product-related variation in the bidding price.

For each seller, only the most recent 25 transaction records were used. Table 4 shows the product lists and the number of sellers for each product. Price premium has different measurements in different fields but basically infers the same thing—i.e., an above-average benefit. Price is influenced by a number of factors. Other than reputation, one of the most important factors is demand and supply equilibrium. The average price is thus assumed to represent the equilibrium. Since the equilibrium is volatile in the market, we used the daily average to measure a more precise and fine-grained premium than that of the entire sample average.

To calculate the price premium, we used the daily average bidding price that is published and updated every day on eBay. Since the variations among the daily average prices can be significant, the price premium is more instructive to potential buyers if it is based on daily average prices rather than the average price of the entire data set. We thus use the following formula:

$$
P P = \frac {\text { Bidding Price } - \text { Daily Average Price }}{\text { Daily Average Price }} \times 100\tag{8}
$$

We also collected the feedback ratings and text comments, which are necessary input for the proposed model. While processing the ratings is straightforward, the text comments need to be categorized through content analysis. Each text comment was assigned to one of the five categories discussed earlier. Theoretically, credibility and benevolence are two different characteristics of the seller and are not mutually exclusive. Credibility refers to the buyer’s trust in the seller’s ability to fulfill the transaction obligation, whereas benevolence refers to the buyer’s trust in the seller’s goodwill toward buyers’ interests (Yamagishi and Yamagishi 1994; Ba and Pavlou 2002). However, the percentage of text comments that belong to both of these categories is very low (< 1%), which is consistent with previous research reporting that all outstanding text comments followed a unimodal distribution (Pavlou and Dimoka 2006). Thus, every text comment was assigned to only one category. For example, when a comment belonged to both OB and OC, the comment was assigned as OB since OB is rare in text comments and may cast a stronger influence on the reputation level.

According to Pavlou and Dimoka (2006), buyers seldom read beyond one page of text comments, i.e., 25 text comments on eBay. Thus, in the belief-updating procedure, we used only the most recent 25 text comments as the input. A total of 11,050 text comments were used. We recruited two raters to code the text comments independently. The raters decided on different categories for 84 comments; they were then asked to discuss these comments and agree on a single category for each of them. This final category label was used in our study. We calculated two reliability scores for intercoder reliability—Krippendorff’s alpha (Krippendorff 2004) and Cohen’s kappa (Cohen 1968)—and obtained the values of 0.9474 and 0.9481, respectively. Both values exceed the recommended value of 0.80, showing a high level of agreement between the raters. Table 5 shows the summary of the different types of text comments.

## Parameter Setting

As shown above, Equation (6) involves four parameters: α, β, γ, and λ. To estimate the values of these parameters, we randomly selected 4,068 sellers on eBay and collected their platform information. We focused on information related to reputation level, including star level, the percentage of positive feedback in the last 12 months, and detailed seller ratings (e.g., item as described, communication, shipping times, and shipping and handling charges). We also collected data on the number of positive ratings, negative ratings, and neutral ratings in the last 1 month, 6 months, and 12 months, respectively. The data are summarized in Table 6.

To simplify the problem, we divided the sellers into two categories: good sellers and bad sellers. The statistical criteria for classification were determined based on the summary statistics of the data set and the literature. Figure 2 shows the seller distribution in terms of positive feedback percentage. More than 95% of our sellers had a positive feedback percentage above 98%. Previous studies also suggest that seller feedback on eBay is overwhelmingly positive (Dellarocas 2003). For instance, Lucking-Reiley et al. (2007) studied 134 unique sellers on eBay and showed that the average positive feedback percentage is around 99.5%. Other studies similarly report average positive feedback percentages of over 98% (Cabral and Hortacsu 2010; Dellarocas 2003). Based on the data distribution, we considered a seller with over 98% of positive feedback in the last 12 months to be a good seller. Otherwise, the seller was regarded as a bad seller.

<table><tr><td colspan="2">Table 4. Products Used in the Field Data from eBay</td></tr><tr><td>Product name</td><td>No. of sellers</td></tr><tr><td>iPod Touch with silver back, 8GB volume and  $2^{nd}$  generation</td><td>21</td></tr><tr><td>Nintendo Wii package including a console, two controllers and five games</td><td>21</td></tr><tr><td>A set of 5 DVDs titled “True Blood – The Complete First Season”</td><td>19</td></tr><tr><td>Apple Watch Black Sport 42mm space gray</td><td>42</td></tr><tr><td>GARMN NUVI 255w 4.3” widescreen</td><td>18</td></tr><tr><td>1 box comic lot of 50</td><td>22</td></tr><tr><td>Apple TV  $3^{rd}$  Generation Digital HD</td><td>39</td></tr><tr><td>Canon 70D camera body</td><td>30</td></tr><tr><td>Beats Solo 2 Black New</td><td>34</td></tr><tr><td>Timberland Men’s 6-inch Premium Wheat Waterproof Boots 10061 New with Box</td><td>37</td></tr><tr><td>TaylorMade R15 460 Right-Handed</td><td>25</td></tr><tr><td>Microsoft Surface Pro 3, 128GB, Core i5</td><td>35</td></tr><tr><td>Samsung Gear Virtual Reality Headset</td><td>22</td></tr><tr><td>iPhone 6s 64GB Gold</td><td>46</td></tr><tr><td>Garmin Fenix 3 Sapphire Training Watch</td><td>31</td></tr><tr><td>Total</td><td>442</td></tr></table>

<table><tr><td colspan="6">Table 5. Descriptive Statistics of the Categories of Text Comments</td></tr><tr><td>Comment type</td><td>OC</td><td>AC</td><td>OB</td><td>AB</td><td>Ordinary</td></tr><tr><td>Percentage</td><td>7.15%</td><td>1.62%</td><td>0.35%</td><td>0.05%</td><td>90.83%</td></tr></table>

<table><tr><td colspan="4">Table 6. Data Collection for Parameter Setting</td></tr><tr><td></td><td>Item</td><td>Content</td><td>Descriptive summary</td></tr><tr><td>1</td><td>Recent feedback ratings</td><td>The number of positive, neutral, and negative overall feedback ratings the member has received in the last 12 months.</td><td>Positive: 99.47%Neutral: 0.29%Negative: 0.24%</td></tr><tr><td>2</td><td>Feedback score</td><td>+1 point for each positive ratingNo points for each neutral rating-1 point for each negative rating</td><td>Min: 9Max: 552,139Mean: 4899.28</td></tr><tr><td>3</td><td>Detailed seller ratings</td><td>Star ratings (ranging from one to five) in the following aspects:Item as describedCommunicationShipping timeShipping and handling charges</td><td>Mean rating:Item as described: 4.92Communication: 4.93Shipping time: 4.93Shipping and handling charges: 4.88</td></tr></table>

![](/api/attachments/FEDPKHZH/fulltext/images/99d639a1bb53fd0ad82d7ec56f85e48f861a69646e03ed4c2f9b80cb4c03f1f2.jpg)

## Figure 2. Frequency of Positive Feedback Percentage

Then, we estimated the probability of a good seller receiving a positive rating (α) and the probability of a bad seller receiving a positive rating (β), represented as follows:

$$
\alpha = \frac {\# G o o d S e l l e r s ^ {\prime} P o s i t i v e R e v i e w s}{T o t a l \# G o o d S e l l e r s ^ {\prime} R e v i e w s}\tag{9}
$$

$$
\beta = \frac {\# B a d S e l l e r s ^ {\prime} P o s i t i v e R e v i e w s}{T o t a l \# B a d S e l l e r s ^ {\prime} R e v i e w s}\tag{10}
$$

Based on our data, the value of α and β is set to 0.996 and 0.952, respectively. In addition, γ is set to 0.5 because we assume that the unconditional probability that the seller is a good seller is 50%.

Among the fifteen products studied, we selected three products (Apple Watch, 1 box comic lot of 50, and Apple TV) to estimate the value of λ. In our research, the Bayesian updating model is designed to estimate seller reputation, so we should ideally estimate λ by using the value that best estimates seller reputation. However, seller reputation cannot be directly observed in the field data and can only be observed indirectly through the price premium. Therefore, we take the value of λ that can best explain price premium as our estimation.

As shown in Equation (6), the range of λ is from 0 to 1. The one-dimensional grid search method was adopted for parameter tuning. Grid search is a method in machine learning used to configure optimal parameters for a given model. A one-dimensional grid search builds a model on each possible value of the parameter iterated through the range and chooses the best one. More specifically, we used a set of values of λ, ranging from 0 to 1, with the step value being 0.01. Each value was used in Equation (6) to calculate the seller’s reputation, which was then used in Equation (7) to predict price premiums.

The result shows that when λ is 0.99, the model performs best. λ accounts for the information retained by buyers as time goes by. Theoretically, λ brings in an exponential decay to reputation level at time t in Equation (7). It is reasonable that λ, as an exponential parameter, remains larger in order to retain information after iterations. In addition, intuitively, λ should not be too small because buyers need to inform themselves through reading ratings and comments. A small λ would indicate that little information is being retained by buyers when they make price-bidding decisions, which is unlikely.

## Benchmark Models

As discussed earlier, we aim to compare the proposed Bayesian updating models (i.e., BU-Ratings and BU-Text) against benchmark models. Therefore, we chose two simple regression models that do not consider Bayesian updating and the time-order effect as our benchmark models for comparison. The first benchmark model, called Simple-Ratings, is based on the regression model proposed in Ba and Pavlou’s study (2002):

$$
P P = \beta_ {0} + \beta_ {1} \log (P R) + \beta_ {2} \log (N R) + \varepsilon
$$

where is the number of positive ratings,PR

(11)

is the number of negative ratings.NR

There is some possibility that the seller has not yet received any negative ratings. Therefore, in the above log(PR) is replaced by log(PR + 1) and log(NR) by log(NR + 1).

The second benchmark model, called Simple-Text, is based on the model proposed in Pavlou and Dimoka’s study (2006), which examines the effect of the category of text comments:

$$
P P = \beta_ {0} + \beta_ {1} O C + \beta_ {2} A C + \beta_ {3} O B + \beta_ {4} A B + \beta_ {5} O r d + \varepsilon\tag{12}
$$

where OC, AC, OB, AB, and Ord are the number of text comments in the corresponding categories.

In addition, to further demonstrate the impact of the timeorder effect on our model, we also incorporate another two regression models that consider Bayesian updating but not the time-order effect as the benchmark models called PlainBU (i.e., the reputation level is calculated by Equation 5).

In sum, the benchmark models utilize the same inputs (i.e., ratings and text comments, respectively) as the proposed models but do not consider the Bayesian updating or the order effect. This allows us to evaluate and compare the effectiveness of the proposed model.

## Results

In this section, we examine the performance of the proposed models that consider the time-order effect in influencing the price premium and compare them with the benchmark models. Figures 3 to 6 show the regression results, including the coefficients of the variables in the regression model, the corresponding p-value, R<sup>2</sup>, and the adjusted R<sup>2</sup>.

Figure 3 shows the results based on the first benchmark model. Figure 4 shows the regression results based on the proposed BU-Ratings model. The results of the second benchmark, Simple-Text are shown in Figure 5, while the results of the proposed BU-Text model are shown in Figure 6. All the relationships in the two proposed models are significant. Table 7 summarizes the adjusted $\mathbf { R } ^ { 2 }$ values of the regressions.

The significant correlations shown in Figures 4 and 6 provide support for H2a and H2b, respectively, confirming the significant positive impact of reputation level on price premium. Furthermore, the adjusted R<sup>2</sup> values of the proposed models are larger than those of the benchmark models (as shown in Figures 3 and 5), thus supporting H3a and H3b. The data show a stronger effect of text comments in determining the price premium than simple feedback ratings for all models and products. In addition, the proposed models lead to a larger adjusted R<sup>2</sup> than the simple regression models. We believe that this is mainly because the Simple-Ratings and Simple-Text models do not distinguish between feedback occurring at different points in time.

To demonstrate the contribution of the time-order effect, we further compared our BU models with the PlainBU models, which are Bayesian updating models without the time-order factor . The adjusted R<sup>2</sup> of the PlainBU model incorporating numerical ratings is 0.1659 and the one incorporating text comments is 0.3553. Both values are lower than the adjusted R<sup>2</sup> of the respective BU model (i.e., 0.2280 for numerical ratings and 0.4206 for text). The result shows that our models incorporating the timeorder factor explained the variance in price premium to a larger extent than the ones without the time-order effect (i.e., =1) for both numerical ratings and text models.

## Discussion and Conclusion

Online auction markets provide sophisticated feedback systems that allow consumers to search for preferred sellers and leave feedback information after completing transactions. However, consumers are often confused by the overwhelming amount of information. Therefore, it is developing a method to efficiently utilize this information is a worthwhile endeavor.

![](/api/attachments/FEDPKHZH/fulltext/images/269c83a8e4f3f347e90ad3b873b0d0595d366cd6daaedfb2b1524ed4f9333f7a.jpg)

![](/api/attachments/FEDPKHZH/fulltext/images/fa7a039fe04dec87b743253cb389eb07a59e7d28e8ce69107df9591d5292a241.jpg)  
Figure 3. Benchmark Regression Model Based on Ratings (Simple-Ratings)

![](/api/attachments/FEDPKHZH/fulltext/images/935434ecd265678e45cdb7c9fbcb03b4e2d3b950c53e5d82eed77cbfe5fc597b.jpg)  
Figure 4. Bayesian Updating Model Based on Ratings (BU-Ratings)  
Figure 5. Benchmark Regression Model Based on Text Comments (Simple-Text)

![](/api/attachments/FEDPKHZH/fulltext/images/f4209c3a18d107bed3d30d8c2fb2c4c19da1c45200f2df304bff4aa1e4f1bd24.jpg)  
Figure 6. Bayesian Updating Model Based on Text Comments (BU-Text)

<table><tr><td colspan="5">Table 7. Adjusted R2 of Regressions for the Twelve Products</td></tr><tr><td>Product description</td><td>Simple-Ratings</td><td>BU-Ratings</td><td>Simple-Text</td><td>BU-Text</td></tr><tr><td>iPod Touch with silver back, 8GB volume and 2nd generation</td><td>0.0525</td><td>0.1543</td><td>0.4646</td><td>0.5403</td></tr><tr><td>Nintendo Wii package including a console, two controllers and five games</td><td>0.0667</td><td>0.1019</td><td>0.1537</td><td>0.2621</td></tr><tr><td>A set of 5 DVDs titled True Blood: The Complete First Season</td><td>0.1959</td><td>0.271</td><td>0.3981</td><td>0.4340</td></tr><tr><td>GARMN NUVI 255w 4.3” widescreen</td><td>0.1139</td><td>0.3771</td><td>0.3834</td><td>0.5434</td></tr><tr><td>Canon 70D camera body</td><td>0.1400</td><td>0.4282</td><td>0.4577</td><td>0.5677</td></tr><tr><td>Beats Solo 2 Black New</td><td>0.0503</td><td>0.1111</td><td>0.3641</td><td>0.4397</td></tr><tr><td>Timberland Men’s 6-inch Premium Wheat Waterproof Boots 10061 New with Box</td><td>0.1398</td><td>0.3278</td><td>0.2258</td><td>0.3578</td></tr><tr><td>TaylorMade R15 460 Right-Handed</td><td>0.1900</td><td>0.2879</td><td>0.1827</td><td>0.3086</td></tr><tr><td>Microsoft Surface Pro 3, 128GB, Core i5</td><td>0.0136</td><td>0.3394</td><td>0.4040</td><td>0.5366</td></tr><tr><td>Samsung Gear Virtual Reality Headset</td><td>0.0155</td><td>0.0403</td><td>0.2128</td><td>0.2857</td></tr><tr><td>iPhone 6s 64GB Gold</td><td>0.0326</td><td>0.2258</td><td>0.5202</td><td>0.5225</td></tr><tr><td>Garmin Fenix 3 Sapphire Training Watch</td><td>0.0724</td><td>0.0887</td><td>0.3596</td><td>0.4607</td></tr><tr><td>All products</td><td>0.0423</td><td>0.2280</td><td>0.3776</td><td>0.4206</td></tr></table>

This paper tests the time-order effect hypothesis in feedback ratings (H1) and proposes a Bayesian updating model that confirms the positive effect hypothesis (H2) and explanatory power hypothesis (H3) for both numeric and textual feedback. In other words, the proposed model provides an alternative to measure sellers’ reputation and can explain the auction price premium better, in terms of high values of adjusted R<sup>2</sup>.

## Theoretical Implications

This paper makes three primary theoretical contributions.

1. We found that temporal similarity of feedback, rather than the display order of feedback, dominates buyers’ decision-making process. Although there is research on the time-order effect in the review generation process (Godes and Silva 2012; Li and Hitt 2008), the effect of the time-order effect on consumers’ decision-making and trust-building processes has not been examined in previous online auction market studies. In this paper, we verify the time-order effect of feedback in seller profiles and show that buyers consider recently posted feedback to be more important than feedback posted a long time ago.

In our first study, we examined both time-order and display-order effects in a user experiment. We found only the time-order effect in buyers’ decision-making processes, indicating that buyers place higher importance on the temporal similarity of feedback, rather than the mere display order of the feedback, when assessing the current transaction.

2. In our second study, we proposed an integrated model that employs the Bayesian updating model to incorporate the time-order effect of feedback information in the trustbuilding process. Our evaluation results show that the proposed model can explain price premiums from real-life transactions on eBay better than benchmark models that do not consider the time-order effect.

By including the time-order effect, we extend the extant literature that examines feedback in online auction markets. Whereas previous research has treated all feedback equally in terms of its effect on buyers’ assessment of current transactions, we demonstrate in this paper that both buyers’ assessment of sellers and price premiums are significantly impacted by the time order of feedback information.

3. We provide evidence for trust building via textual feedback. Our analysis provides support for the benchmark model presented by Pavlou and Dimoka (2006). Specifically, our results show that text comments have a stronger effect on building trust and shaping price premiums than simple feedback ratings. Following previous research (Ba and Pavlou 2002; Pavlou and Dimoka 2006), we depict the process through which text comments determine price premiums using reputation levels that incorporate the time-order effect. Our model integrates text comments and thus better accounts for the significantly higher variance in price premiums than models considering numeric ratings alone.

## Practical Implications

Our findings suggest that the time order of feedback information can shape buyers’ assessment and price premiums for the current transaction. This has important implications for platform managers and market participants. Based on our findings, we make the following suggestions from different perspectives.

Suggestions for platform managers: Our results suggest that online auction markets should not only maintain a complete feedback profile database but should also display feedback profiles in a way that can help buyers more quickly evaluate sellers. Reputation levels generated by the proposed model could serve as a means of ranking seller feedback profiles and may offer a good indication of the average price premium in real-life online markets. In addition, our price premium model could also provide managers with information on seller assessment and bidding price.

Suggestions for sellers: If sellers receive a negative comment, we recommend that they should not be too aggressive in the starting bid price of their next product. Instead, the seller may consider rebuilding buyers’ trust and trying to obtain more positive feedback in order to mitigate the effect of the negative feedback, which will fade away as new feedback is posted. In contrast, sellers with no recent negative feedback might consider raising their starting bid prices for new transactions.

Suggestions for buyers: Buyers should note that, given two sellers with the same average rating, if one has recent negative feedback, that seller may be more likely to offer lower initial bid prices; thus, buyers may be able to more easily win bids from that seller at a lower price. Similarly, higher prices may be necessary to win bids from sellers with no recent negative feedback. This knowledge can help buyers can place their bids more efficiently.

The implications of this study can also be extended to other online market platforms. For instance, highly competitive online retailing platforms could incorporate the time-order effect of negative reviews in dynamic pricing models (Fisher et al. 2017) in order to better capture consumers’ choices among products from multiple retailers.

## Limitations and Future Directions

One limitation of this study is our inability to separately identify the time-order effect and the display-order effect in our field data study (Study 2). Therefore, our findings do not guarantee that the time-order effect is the mechanism in play. Although we demonstrated the existence of the timeorder effect in Study 1, caution is still needed when interpreting the results of the field data study. Another limitation of our study is the manual categorization of text comments. Since it is tedious to read and categorize high volumes of text comments, designing a machine learning algorithm to automatically categorize text comments would be a worthwhile endeavor.

In our research, to ensure a large enough sample of transactions, we intentionally selected popular products for Study 2. It is possible that differences in product categories would result in a stronger or weaker time-order effect because buyers’ bidding behaviors may be affected by product features or price levels (Liu et al. 2012). A product with a higher price level, or one with complex product features, may require consumers to spend more time to inform themselves, which may amplify the significance of the time effect. Future research could analyze the proposed model across more product categories. Finally, there are other factors that may affect buyers’ perception of the importance of feedback, such as the display of the website. It would be interesting to study how various factors affect buyers’ trust and price premiums.

## Acknowledgments

This project was supported in part by a grant from the General Research Fund of the Hong Kong Research Grants Council (project number: 17500514B). We thank the senior editor, associate editor, and the reviewers for their invaluable comments and suggestions throughout the review process.

## References

Adler, P. S. 2001. “Market, Hierarchy, and Trust: The Knowledge Economy and the Future of Capitalism,” Organization Science (12:2), pp. 215-234.

Ba, S., and Pavlou, P. A. 2002. “Evidence of the Effect of Trust Building Technology in Electronic Markets: Price Premiums and Buyer Behavior,” MIS Quarterly (26:3), pp. 243-268.

Ba, S., Whinston, A. B., and Zhang, H. 2003. “Building Trust in Online Auction Markets through an Economic Incentive Mechanism,” Decision Support Systems (35:3), p. 273.

Bakos, J. Y. 1997. “Reducing Buyer Search Costs: Implications for Electronic Marketplaces,” Management Science (43:12), pp. 1676-1692.

Becker, S. L. 1954. “Why an Order Effect,” Public Opinion Quarterly (18:3), pp. 271-278.

Bolton, G. E., Katok, E., and Ockenfels, A. 2004a. “How Effective Are Electronic Reputation Mechanisms? An Experimental Investigation,” Management Science (50:11), p. 1587-1602.

Bolton, G. E., Katok, E., and Ockenfels, A. 2004b. “Trust among Internet Traders: A Behavioral Economics Approach,” Analyse und Kritik (26:1), p. 185-202.

Cabanac, G., and Preuss, T. 2013. “Capitalizing on Order Effects in the Bids of Peer‐Reviewed Conferences to Secure Reviews by Expert Referees,” Journal of the American Society for Information Science and Technology (64:2), pp. 405-415.

Carter, M., Tams, S., and Grover, V. 2017. “When Do I Profit? Uncovering Boundary Conditions on Reputation Effects in Online Auctions,” Information & Management (54:2), pp. 256-267.

Cohen, J. 1968. “Weighted Kappa: Nominal Scale Agreement Provision for Scaled Disagreement or Partial Credit,” Psychological Bulletin (70:4), p. 213-220.

Dellarocas, C. 2003. “The Digitization of Word of Mouth: Promise and Challenges of Online Feedback Mechanisms,” Management Science (49:10), pp. 1407-1424.

Dellarocas, C. 2005. “Reputation Mechanism Design in Online Trading Environments,” Information Systems Research (16:2), pp. 209-231.

Doney, P. M., and Cannon, J. P. 1997. “An Examination of the Nature of Trust in Buyer-Seller Relationships,” Journal of Marketing (61:2), p. 35.

Fisher, M., Gallino, S., and Li, J. 2017. “Competition-Based Dynamic Pricing in Online Retailing: A Methodology Validated with Field Experiments,” Management Science (64:6), pp. 2496-2514.

Ganesan, S. 1994. “Determinants of Long-Term Orientation in Buyer-Seller Relationships,” The Journal of Marketing (58:2), pp. 1-19.

Godes, D., and Silva, J. C. 2012. “Sequential and Temporal Dynamics of Online Opinion,” Marketing Science (31:3), pp. 448-473.

Granovetter, M. 1985. “Economic Action and Social Structure: The Problem of Embeddedness,” The American Journal of Sociology (91:3), pp. 481-510.

Greif, A. 1989. “Reputation and Coalitions in Medieval Trade: Evidence on the Maghribi Traders,” The Journal of Economic History (49:4), pp. 857-882.

Güth, W., Mengel, F., and Ockenfels, A. 2007. “An Evolutionary Analysis of Buyer Insurance and Seller Reputation in Online Markets,” Theory and Decision (63:3), pp. 265-282.

Hibbeln, M. T., Jenkins, J. L., Schneider, C., Valacich, J., and Weinmann, M. 2017. “How Is Your User Feeling? Inferring Emotion through Human-Computer Interaction Devices,” MIS Quarterly (41:1), pp. 1-21.

Hinz, O., Hill, S., and Kim, J.-Y. 2016. “TV’s Dirty Little Secret: The Negative Effect of Popular Tv on Online Auction Sales,” MIS Quarterly (40:3), pp. 623-644.

Hu, N., Pavlou, P. A., and Zhang, J. 2006. “Can Online Reviews Reveal a Product’s True Quality?: Empirical Findings and Analytical Modeling of Online Word-of-Mouth Communication,” in Proceedings of the 7th ACM Conference on Electronic Commerce, Ann Arbor, MI.

Jarvenpaa, S. L., and Tractinsky, N. 1999. “Consumer Trust in an Internet Store: A Cross-Cultural Validation,” Journal of Computer-Mediatied Communication (5:2).

Jin, G. Z., and Kato, A. 2006. “Price, Quality, and Reputation: Evidence from an Online Field Experiment,” The Rand Journal of Economics (37:4), p. 983.

Kane, G. C., and Ransbotham, S. 2016. “Research Note— Content and Collaboration: An Affiliation Network Approach to Information Quality in Online Peer Production Communities,” Information Systems Research (27:2), pp. 424-439.

Klein, B., and Leffler, K. B. 1981. “The Role of Market Forces in Assuring Contractual Performance,” The Journal of Political Economy (89:4), pp. 615-641.

Krippendorff, K. 2004. Content Analysis: An Introduction to Its Methodology. Thousand Oaks, CA: SAGE.

Lee, Z., Im, I., and Lee, S. J. 2000. “The Effect of Negative Buyer Feedback on Prices in Internet Auction Markets,” in Proceedings of the Twenty-First International Conference on Information Systems, Brisbane, Australia.

Li, L. 2010. “Reputation, Trust, and Rebates: How Online Auction Markets Can Improve Their Feedback Mechanisms,” Journal of Economics & Management Strategy (19:2), pp. 303-331.

Li, X., and Hitt, L. M. 2008. “Self-Selection and Information Role of Online Product Reviews,” Information Systems Research (19:4), pp. 456-474.

Liu, Y., Feng, J., and Wei, K. K. 2012. “Negative Price Premium Effect in Online Market: The Impact of Competition and Buyer Informativeness on the Pricing Strategies of Sellers with Different Reputation Levels,” Decision Support Systems (54:1), pp. 681-690.

Milgrom, P. R., North, D. C., and Weingast, B. R. 1990. “The Role of Institutions in the Revival of Trade: The Law

Merchant, Private Judges, and the Champagne Fairs,” Economics and Politics (2:1), pp. 1-23.

Mishra, D. P., Heide, J. B., and Stanton, G. C. 1998. “Information Asymmetry and Levels of Agency Relationships,” Journal of Marketing Research (35:3), pp. 277-295.

Moreno, A., and Terwiesch, C. 2014. “Doing Business with Strangers: Reputation in Online Service Marketplaces,” Information Systems Research (25:4), pp. 865-886.

Nurmi, P. 2006. “A Bayesian Framework for Online Reputation Systems,” in Proceedings of the Advanced International Conference on Telecommunications and International Conference on Internet and Web Applications and Services.

Osborne, M. J. 2004. An Introduction to Game Theory. New York: Oxford University Press.

Pavlou, P. A., and Dimoka, A. 2006. “The Nature and Role of Feedback Text Comments in Online Marketplaces: Implications for Trust Building, Price Premiums, and Seller Differentiation,” Information Systems Research (17:4), pp. 392-414.

Pavlou, P. A., and Gefen, D. 2004. “Building Effective Online Marketplaces with Institution-Based Trust,” Information Systems Research (15:1), pp. 37-59.

Pavlou, P. A., Liang, H., and Yajiong, X. 2007. “Understanding and Mitigating Uncertainty in Online Exchange Relationships: A Principal-Agent Perspective,” MIS Quarterly (31:1), pp. 105-136.

Resnick, P., and Zeckhauser, R. 2002. “Trust Among Strangers in Internet Transactions: Empirical Analysis of Ebay’s Reputation System,” Advances in Applied Microeconomics (11).

Scott, W., and Derlaga, V. J. 1983. “Attributions in T-Groups: A Test of Kelley’s Anova Model,” Small Group Behavior (14), pp. 50-62.

Shapiro, C. 1983. “Premiums for High Quality Products as Returns to Reputations,” The Quarterly Journal of Economics (98:4), pp. 659-680.

Spence, M. 1973. “Job Market Signaling,” The Quarterly Journal of Economics (87:3), pp. 355-374.

Webster, C., and Sundaram, D. S. 1998. “Service Consumption Criticality in Failure Recovery,” Journal of Business Research (41:2), pp. 153-159.

Whinston, A. B., Choi, S. Y., and Stahl, D. O. 1997. The Economics of Electronic Commerce. Macmillan Technical Publishing.

Williamson, O. E. 1987. The Economic Institutions of Capitalism: Firms, Markets, Relational Contracting. New York: Free Press.

Yamagishi, T., and Yamagishi, M. 1994. “Trust and Commitment in the United States and Japan,” Motivation and Emotion (18:2), pp. 129-166.

Zhou, M. 2004. “The Effectiveness of Seller Credibility Systems in the Online Auction Market: Modeling the Seller’s Point of View,” unpublished doctoral dissertation, University of Maryland, College Park, MD.

## About the Authors

Michael Chau is an associate professor in the Faculty of Business and Economics (HKU Business School) at the University of Hong Kong. His research focuses on the cross-disciplinary intersection of information systems, computer science, business analytics, and information science, with an emphasis on the applications of data, text, and web mining in various business, education, and social domains. He is particularly interested in text mining and data analytics research, and his research has resulted in over 150 publications in high-quality journals and conferences. He is the recipient of the HKU Outstanding Young Research Award (2014) and Knowledge Exchange Award (2013, 2016), and he is highly ranked in several research productivity studies. He was the program co-chair of the International Conference on Information Systems 2013 and the founding co-chair of the Pacific Asia Workshop on Intelligence and Security Informatics series, served as an associate editor at MIS Quarterly from 2014-2017, and is a member of the AIS College of Senior Scholars. He received his Ph.D. degree in management information systems from the University of Arizona and his B.Sc. degree in computer science and information systems from the University of Hong Kong.

Wenwen Li is an assistant professor in information systems at Fudan University. She received her Ph.D. in information systems from the University of Hong Kong. She is interested in the research areas of business analytics and business intelligence, health analytics and mobile health, machine learning, deep learning, natural language processing.

Boye Yang is a senior economics analyst at the Zhejiang Provincial Development and Reform Institute in China, focusing primarily on development economics planning and institution design. He supports the provincial and local governments as well as NGOs in economics forecast, policy evaluation and advising, institution design, and regional development planning. He holds a master’s in information systems from the University of Hong Kong and a bachelor’s degree from Fudan University. His research interests include game theory, mechanism design, and real estate market analysis and macroeconomics.

Alice J. Lee is a management consultant at Deloitte Consulting, focusing primarily on business and digital transformation. She supports clients by designing and advising strategic project management direction and transformations in partnership with organizational leaders to help improve client operational efficiency. She holds a Ph.D. degree in management from the University of St.Gallen. She completed her M.Sc. degree in computer science at the Technical University of Munich, and holds a BEng degree in computer science and a BBA degree in information systems from the University of Hong Kong. Her research interests include project management, organization design, consumer behavior, and decision-making.

Zhuolan Bao is an assistant professor of information systems at the Chinese University of Hong Kong, Shenzhen. She received her B.A. from Nankai University and her Ph.D. in information systems from the University of Hong Kong. Her current research interests include e-commerce, social media analytics, crowdfunding, and online fandom behaviors.
