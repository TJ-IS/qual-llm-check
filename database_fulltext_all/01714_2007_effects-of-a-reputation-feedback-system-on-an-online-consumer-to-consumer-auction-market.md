---
otero_id: 1714
otero_key: "DDJPAZFV"
title: "Effects of a reputation feedback system on an online consumer-to-consumer auction market"
authors: "Jian Yang; Xiaorui Hu; Han Zhang"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.03.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 44 (2007) 93– 105

www.elsevier.com/locate/dss

# Effects of a reputation feedback system on an online consumer-to-consumer auction market

Jian Yang <sup>a,1</sup>, Xiaorui Hu <sup>b,2</sup>, Han Zhang c,⁎

<sup>a</sup> Department of Industrial and Manufacturing Engineering, New Jersey Institute of Technology Newark, NJ 07102, United States <sup>b</sup> John Cook School of Business St. Louis University, St. Louis, MO 63108, United States <sup>c</sup> College of Management, Georgia Institute of Technology, Atlanta, GA 30332, United States

Received 23 February 2006; received in revised form 26 February 2007; accepted 11 March 2007 Available online 21 March 2007

## Abstract

This research establishes a dynamic game-theoretic model that interprets the mechanism of reputation feedback systems in online consumer-to-consumer (C2C) auction markets. Based on the model, a numerical study is conducted to reveal the effects of feedback systems on auction markets. The study shows that the existence of feedback systems greatly improves the performance of online C2C auction markets: buyers are more willing to trade and gain more benefit from the transactions; sellers' honest behavior is encouraged, as honest sellers' gains are increased and dishonest sellers' gains are reduced. It also offers practical insights on the design of a feedback system: rewarding an honestly-behaving seller is less effective on promoting market performance than punishing a cheating seller. © 2007 Elsevier B.V. All rights reserved.

Keywords: Gaming; Internet; Auction/bidding; Feedback system

## 1. Introduction

We study, from both theoretical and numerical angles, reputation feedback systems (hence-forward feedback systems) in online consumer-to-consumer (C2C) auction markets. Our purpose is to show that reasonably-designed feedback systems can promote trust and mitigate fraud, and help ensure the healthy development of the online markets. We also intend our numerical study to offer managerial insights on the market impacts of feedback systems' design features.

While online C2C auction markets have been growing rapidly in recent years, fraud in these markets is also on the rise. The average loss per claim in online auction frauds jumped from \$895 in 2004 to \$1917 in 2005 [14]. In online markets, interacting with strangers is inevitable, and most transactions between buyers and sellers are one-time deals. Meanwhile, auction sites serve as market makers for buyers and sellers to meet, but claim no liability for any fraudulent transactions. For example, eBay claims that they “have no control over the quality, safety or legality of the items advertised, the truth or accuracy of the listings” [10]. Thus, online auction participants have to face a market where goods are purchased before one can assure the quality. Therefore, promoting trust between strangers and reducing the uncertainty and risk for online traders are the critical issues facing current online C2C auction markets.

Various mechanisms have been designed and utilized in C2C auction markets to promote trust and reduce risk. Specific online payment systems (e.g., PayPal) have been implemented to provide secure and instantaneous online transactions for small online merchants and auction buyers. Online auction sites (e.g., eBay) have also been offering limited insurance or guarantees to protect auction participants and create a safer environment to trade. Feedback systems have also been offered by most of the C2C auction sites to reduce online traders' uncertainties and the risks associated with online trading. For instance, eBay's “Feedback Forum” is a form of community enforcement. In eBay, after each trade, both buyers and sellers are encouraged to leave comments about their trading partners based on their experience. Comments about traders are kept under each trader's profile, and can be accessed by everyone who visits eBay. This way, the system tries to deter dishonest behavior by conveying facts and opinions about past trades.

Does the feedback system work as advertised? There is substantial research that says it does. Kollock [15] conceptually summarizes online reputation systems and concludes that their effectiveness to manage the risks of unsecured trades seems to be impressive. Resnick et al. [20] review the online reputation systems and argue that the reputation systems appear to perform reasonably well despite their theoretical and practical difficulties. Resnick and Zeckhauser [19] empirically examine a large data set from eBay and claim that the reputation system appears to be effective. Ba and Pavlou [1] empirically explore the extent to which trust can be induced by proper feedback mechanisms in electronic markets and find that feedback systems can generate price premiums for reputable sellers. Resnick et al. [21] conduct a controlled experiment on eBay to assess returns to reputation.

In the related economics literature on repeated games involving reputation, most papers deal with a situation where players are not strangers to each other and a player's reputation is equivalent to the entire history of his actions. The reader may refer to Kreps and Wilson [16], Milgrom and Roberts [17], Fudenberg and Levine [11,12], Cripps and Thomas [6], Celentani et al. [5], Battigali and Watson [3], etc. for a glimpse of this body of literature. In an online C2C auction market, players are strangers to each other, and without a proper mechanism being installed, they know very little about each other when they trade. Moreover, it is unrealistic for any mechanism to require that every trader's entire history be remembered (stored). A feedback system, on the other hand, offers a platform where merely a function, usually many-to-one, of every trader's entire history needs to be stored.

Dellarocas and Bakos have recently studied feedback systems from a theoretical perspective. Dellarocas [7] provides an overview of relevant past research on reputation mechanisms based on the repeated-game setting, and points out several future research directions concerning online feedback systems. Bakos and Dellarocas [2] study a trading system involving a single seller who repeatedly trades with buyers. The authors show that even the most primitive feedback system, as incarnated by the binary score, can provide an economically more efficient solution than the threat of litigation. Dellarocas [9] examines a similar model with a more sophisticated scoring system. The author is able to obtain a closed-form solution to the problem, which shows that sustainable cooperations between buyers and the seller are achievable as long as the return–cost ratio to the seller is high enough. Dellarocas [8] shows that in a certain environment, the combination of listing fees and binary-score feedbacks can induce sellers to announce the true quality of their products and at the same time maximize the average social welfare. From another angle, Miller, Resnick, and Zeckhauser [18] examine the elicitation of proper buyers' feedback writing behavior that makes a feedback system function.

As Bakos and Dellarocas [2] and Dellarocas [9] have done, this paper studies the merits of online feedback systems in a repeated-game setting where buyers' reputation score updating behavior is made exogenous, and sellers are assumed to be of different types, with each type pertaining to a specific tendency towards cheating. It differs from the two aforementioned papers most saliently in two aspects: 1) multiple seller types are considered, so that the score associated with a seller infers his type in addition to his future behavior. Because of this, features of Bayesian learning and the marriage of perceived and actual seller distributions appear in the formulation; and 2) it contains a general, as opposed to stylized, feedback system and speculates that a set of stochastic ordering relationships in its evolution is what makes the system work.

Specifically, we propose a dynamic game-theoretic framework to model the mechanism of a feedback system in an online C2C auction market. In the framework, we assume that all buyers are honest while sellers are of different types with different propensities for cheating. The feedback system is comprised of scores associated with sellers, which are updated by their respective trading partners in ways that are dependent on the treatment the partners have received. As the trading game is played over a sufficiently long period of time, buyers will form associations between sellers' scores and their types on the basis of Bayesian learning from past experiences. For example, a seller with more cheating history (higher score) is considered more prone to cheating than one with less cheating history, and buyers will treat sellers with different scores differentially. Knowing the different possible treatments from buyers, sellers will weigh their decisions about cheating/playing honestly based not only on their immediate one-time gain but also on their future business opportunities, which are affected by how their scores are updated by their respective trading partners.

Following the theoretical analysis, a numerical study is presented. The numerical results verify the benefits introduced by the feedback system. Our results also show that even with feedback systems in place, dishonest behavior from traders with excellent reputation ratings occurs, but at the same time, feedback systems do enhance the overall level of honesty in online auction markets.

The rest of this paper is structured as follows: in Section 2 we establish the dynamic game-theoretic model; in Section 3 we discuss the anticipated properties of various market performances; in Section 4 we conduct a numerical study based on the model and analyze the findings from the study; and in Section 5 we conclude the paper. We have relegated materials of secondary importance to our appendices. The latter will be available upon request.

## 2. Problem formulation

For the reader to better understand our formulations, we have compiled a list of symbols used in the general model in Appendix A.

## 2.1. The stage-game setting

Each seller is characterized by a prone-to-cheating factor $z { \ge } 0$ , which reflects his average gain while cheating in a transaction. Buyers are all of the same type in terms of their payoff functions and they never cheat. Each transaction is characterized by a size parameter $x \ge 0 .$ which can be viewed as the trading surplus from the trade. A more realistic model may allow buyers to cheat as well. However, current online C2C auction markets allow buyers less chance to cheat, as they are required to pay before goods are shipped. Thus our model offers a reasonable approximation. Miller, Resnick, and Zeckhauser [18] offer similar arguments on why a seller's reputation is more important than a buyer's.

In a size-x transaction that involves a type-z seller, if the seller plays honestly, his average gain will be $g _ { \mathrm { S X } } ^ { \mathrm { H } } ( x )$ and the buyer's (his trading partner's) average gain will be $g _ { \mathrm { B X } } ^ { \mathrm { H } } ( x )$ . However, if the seller cheats, his average gain will be $\boldsymbol { g } _ { \mathrm { S X Z } } ^ { \mathrm { C } } ( \boldsymbol { x } , z )$ while the buyer's average gain will be $\begin{array} { r l } {  { g _ { \mathrm { B X Z } } ^ { \mathrm { C } } ( x , z ) } } \end{array}$ . Both gains depend on the level of the cheating which is captured by the factor z. Reasonably, we should have the following assumptions.

A seller with a larger z gains more from cheating:

$$
g _ {\mathrm{SXZ}} ^ {\mathrm{C}} (x, z + \Delta z) \geq g _ {\mathrm{SXZ}} ^ {\mathrm{C}} (x, z) \text { for } \Delta z \geq 0.\tag{1}
$$

A seller always benefits from trading, and in a single stage, he gains more from cheating than behaving honestly:

$$
g _ {\mathrm{SXZ}} ^ {\mathrm{C}} (x, 0) \geq g _ {\mathrm{SX}} ^ {\mathrm{H}} (x) > 0.\tag{2}
$$

A buyer hurts more when a seller with a larger z cheats:

$$
g _ {\mathrm{BXZ}} ^ {\mathrm{C}} (x, z + \Delta z) \leq g _ {\mathrm{BXZ}} ^ {\mathrm{C}} (x, z) \text { for } \Delta z \geq 0.\tag{3}
$$

A buyer benefits from trading when his trading partner behaves honestly and hurts from trading when his trading partner cheats:

$$
g _ {\mathrm{BX}} ^ {\mathrm{H}} (x) \geq 0 > g _ {\mathrm{BXZ}} ^ {\mathrm{C}} (x, z) \text {   when   } z \text {   is   sufficiently   large. }\tag{4}
$$

Other than the above four assumptions, we allow our gain functions to be of any particular form. Also, they can be realized by the online auction process as well as other trading mechanisms.

Each transaction involves two stages. In the first stage, both the seller and the buyer observe the transaction size $x ,$ and the buyer decides whether to proceed with the transaction or to withdraw from it. If the former is the answer, then there is a second stage. Otherwise, both parties receive zero gains. If the buyer decides to proceed, then in the second stage, the seller decides whether to play honestly or to cheat, and subsequently both parties receive their corresponding gains.

Suppose in each transaction, a buyer faces a randomly drawn seller whose type he does not know. Then by the four assumptions, we can easily see that as long as the random distribution of sellers is sufficiently tilted toward the more dishonest types $( \mathrm { l a r g e r } z ^ { , } \mathrm { s } )$ , any Nash equilibrium of the stage game of any transaction size results in no trading. On the other hand, folk theorems in the economics literature suggest that when the stage games are repeatedly played, players might use credible threats and rewards to induce each other to adopt otherwise unacceptable strategies in their stagegame plays. However, these theorems require that either the same set of players keep on playing with each other forever, or any long-run player's past behavior is either publicly known or sufficiently discernible (see $\mathrm { e . g . }$ [13], Theorem 5.4 on Page 157, Theorem 5.10 on Page 171, and Theorem 5.11 on Page 196). There is no known folk theorem that readily applies to the situation where any two players have no chance of playing more than once with each other and any player's past history is in no way recorded.

However, in a bare-bone online C2C auction market, buyers have to repeatedly deal with random sellers who have different propensities for cheating and whose true types and past histories are unknown to the buyers. Hence by the above observation, without any proper mechanism, it seems unlikely that the market participants can entice and discipline themselves into mutually beneficial tradings. Therefore, the implementation of feedback systems can be very crucial in such markets.

Probably the ideal feedback mechanism is the one that records each seller's entire history of past behavior. The economics literature on reputation effects often assumes that this mechanism is implementable (e.g., [11]). Due to limited space (memory), however, this ideal version usually cannot be implemented in reality. On the other hand, real online feedback systems try to use limited space to store information which to some extent reflects the past behavior of sellers.

## 2.2. The reputation feedback system

We view a reputation feedback system as a system where every seller is associated with a score, which is constantly being updated by each of his trading partners in response to the treatment the latter has received. Upon making the assumption that buyers behave fairly rationally, we expect the score to serve as a mirror of a seller's past behavior and to indicate his true type. In order for all sellers' scores to reveal their types, which are ranked from the morally strongest to the morally weakest, we need the scores to fall into an ordered set, wherein one score is always lower than the other given any two scores in the set. By further assuming that a cheated buyer tends to increase his partner's score while a well treated buyer tends to reduce his partner's score, we expect that once trading has gone on long enough to allow all behavior and beliefs to fall into steady states, a seller who is prone to cheating will more likely have a high score.

For example, eBay's feedback system allows buyers to write comments about their trading partners. There are several ways to translate the comments that are stored in a seller's account into a sortable score. We may categorize the comments stored in a seller's account into good comments and bad comments. Then we may let the score of a seller whose account contains $n _ { \mathrm { G } }$ number of good comments and $n _ { \mathrm { B } }$ number of bad comments be $( - n _ { \mathrm { G } } , { n _ { \mathrm { B } } } )$ , and let any two arbitrary scores be ordered lexicographically with either $- n _ { \mathrm { G } }$ or $n _ { \mathrm { B } }$ being the dominant component. Or, we may assign to each comment a real value and make the summation of all values assigned to the comments stored in a seller's account as this seller's score. Here, two scores may be ranked as two real numbers.

In this paper, we make the buyers' feedback writing behavior exogenous so that it is described by certain reasonable random variables. Research has found that the reasonable behavior on the buyers' part can be elicited (see e.g., [18]). In our feedback model, each seller is associated with a score, say w, out of a totally ordered set W. After each trade, w will be updated by the buyer to a random new score $( \boldsymbol { W } ^ { \mathrm { H } } | _ { \boldsymbol { w } } )$ or $( \boldsymbol { W } ^ { \dot { \mathrm { C } } } | _ { \boldsymbol { w } } )$ depending on whether the buyer has been treated honestly or has been cheated. For brevity, from now on we assume that $\mathcal { W }$ is a subset of nonnegative real numbers. The random variables $( \boldsymbol { W } ^ { \mathrm { H } } | _ { \mathcal { W } } )$ and $( W ^ { \mathbf { C } } | { \boldsymbol w } )$ need to meet two types of requirements.

First, all of them should be increasing in w in some stochastic sense, so that the new score memorizes a seller's past behavior.

Second, at the same $w ,$ in some stochastic sense $( \boldsymbol { W } ^ { \mathrm { H } } | _ { \boldsymbol { w } } )$ should be smaller than the degenerate random variable $W { \equiv } w$ and $( W ^ { \mathbf { C } } | \boldsymbol { w } )$ should be larger than the degenerate random variable $W { \equiv } w ,$ so that a positive correspondence will likely be formed between a seller's type and his score after enough transactions have taken place.

There are several possible ways to mathematically express that one random variable, say $W ^ { 1 }$ , is smaller than another, say $W ^ { 2 } ;$ in the likelihood ratio (lr) sense, in the stochastic (st) sense, or in the average sense [22].

From now on, we use $f _ { \mathrm { W W } } ^ { \mathrm { H } } ( w , \bar { w } ^ { \prime } )$ and $f _ { \mathrm { W W } } ^ { \mathrm { C } } ( w , w ^ { \prime } )$ to respectively denote the distributions of $( \boldsymbol { W } ^ { \mathrm { H } } | _ { \mathcal { W } } )$ and $( \bar { W } ^ { \mathrm { C } } | _ { \mathcal { W } } )$ when they are continuous random variables, and use $p _ { \mathrm { W W } } ^ { \mathrm { H } } ( w , w ^ { \prime } )$ and $p _ { \mathrm { W W } } ^ { \mathrm { C } } ( w , w ^ { \prime } )$ to respectively denote the probability masses of them.

Here is an example of a stylized feedback system. Each seller's account stores up to $\dot { \bar { W } }$ comments. A score-w seller is a seller whose account contains $\bar { W } - w$ good comments and w bad comments. If the seller's trading partner has been honestly treated, then with probability $p _ { \mathrm { H } }$ the partner will overwrite a randomly-chosen existing comment with a good comment and with probability $1 - p _ { \mathrm { H } } ,$ he will do nothing. If the seller's trading partner has been cheated, then with probability $p _ { \mathrm { { C } } } ,$ , the partner will overwrite a randomly chosen existing comment with a bad comment and with probability $1 - p _ { \mathrm { { C } } } ,$ he will do nothing.

After translating such a description of a buyer's scoreupdating behavior into the corresponding $p _ { \mathrm { W W } } ^ { \mathrm { H } } ( w , w ^ { \prime } ) ^ { \ast } \mathbf { s }$ and $p _ { \mathrm { W W } } ^ { \mathrm { C } } ( w , w ^ { \prime } ) ^ { \ast } \mathbf { s }$ , we have

$$
\begin{array}{l} p _ {\mathrm{WW}} ^ {\mathrm{H}} (0, 0) = 1, \\ p _ {\mathrm{WW}} ^ {\mathrm{H}} (w, w - 1) = \frac {w}{\overline {{W}}} p _ {\mathrm{H}} \text {and} p _ {\mathrm{WW}} ^ {\mathrm{H}} (w, w) \\ \qquad = 1 - \frac {w}{\overline {{W}}} p _ {\mathrm{H}} \text {for} w = 1, 2, \ldots , \overline {{W}}, \\ p _ {\mathrm{WW}} ^ {\mathrm{C}} (w, w) = 1 - \frac {\overline {{W}} - w}{\overline {{W}}} p _ {\mathrm{C}} \text {and} p _ {\mathrm{WW}} ^ {\mathrm{C}} (w, w + 1) \\ \qquad = \frac {\overline {{W}} - w}{\overline {{W}}} p _ {\mathrm{C}} \text {for} w = 0, 1, \ldots , \overline {{W}} - 1, \\ p _ {\mathrm{WW}} ^ {\mathrm{C}} (\overline {{W}} | \overline {{W}}) = 1, \end{array}\tag{5}
$$

and that these probabilities at all other unmentioned elements are 0. For this example, we found that the aforementioned two requirements are met in the strongest lr-sense.

Since the situation without a feedback system can be viewed as when the cardinality of W is merely 1 or when

$$
(W ^ {\mathrm{H}} | w) = (W ^ {\mathrm{C}} | w) \equiv w,
$$

we do not have to separately delineate the decisionmaking processes under this situation. In later sections, we will use $\mathrm { ~ a ~ } ^ { 6 6 } 0 ^ { \circ }$ superscript to signify values pertaining to the without-feedback situation.

## 2.3. The repeated game setting

Our game is an infinitely repeated game with nature, buyers, and sellers as players. Buyers form the set $[ 0 , 1 ]$ and sellers form the set $[ 0 , + \infty )$ . Each seller is associated with a score $w \in \mathcal { W } .$ Nature continuously draws pairs of sellers and buyers to play the stage game introduced earlier in such a way that every buyer $y \in [ 0 , 1 ]$ gets to play an infinite and countable number of times; every seller $z \in [ 0 , + \infty )$ gets to play an infinite and countable number of times; to a seller in each of his stage game, the type of the paired buyer is known; and to a buyer in each of his stage game, the paired seller seems to be randomly drawn from $[ 0 , + \infty )$ ) according to distribution $f _ { Z } ( z )$ . Also, we let $\beta _ { \mathrm { B } } { \in } ( 0 , 1 )$ and $\beta _ { \mathrm { { S } } } { \in } ( 0 , 1 )$ be each buyer's and seller's discount factor per stage, respectively.

In every stage game, after the involved players have been decided, nature proceeds to randomly draw the transaction size x from distribution $f _ { \mathrm { X } } ( x )$ on $[ 0 , + \infty )$ Then, the selected buyer moves by deciding whether to trade with the currently paired seller whose type he does not know and whose score he knows. If the buyer decides to proceed, the seller gets to move by deciding whether to play honestly or to cheat, and the buyer moves last to update the seller's score according to the random scoreupdating rule specified in the last subsection. Otherwise, none of the players move. Nature's payoff is not our concern and it has one strategy after all. For sellers and buyers, their payoffs in the current stage are the same as those of the stage game introduced earlier. We introduce different buyer types only to facilitate the aforementioned play frequencies and the actual buyer payoffs do not differentiate over different types.

We use $H _ { \mathrm { B n } } ( y )$ to denote the set of all possible histories that buyer y can have at his nth play which consist of his past observations of transaction sizes and opponents' scores along with the past treatments he received. Any of buyer y's mixed strategy is specified by an infinite array of functions: $B ( y ) = \{ p _ { \mathrm { B n } } ^ { \mathrm { P } } ( y , \ h _ { \mathrm { B n } } ( y ) ) | n = 1 , 2 , . . . , h _ { \mathrm { B n } } ( y ) \in H _ { B n }$ $( y ) \}$ , where $p _ { \mathrm { B n } } ^ { \mathrm { P } } ( y , h _ { \mathrm { B n } } ( y ) )$ stands for the probability that buyer y will proceed to trade in his nth stage game when his history is $h _ { \mathrm { B n } } ( \nu )$ . Similarly, we use $H _ { \mathrm { S n } } ( z )$ to denote the set of all possible histories that seller z can have at his nth play which consist of his observations of transaction sizes, his own scores, and his opponent's types along with the past treatments he received. Any of seller z's mixed strategy is specified by an array of functions $S ( z ) { = } \{ p _ { \mathrm { { S n } } } ^ { \mathrm { { H } } } ( z ,$ $h _ { \mathrm { S n } } ( z ) ) | n { = } 1 , 2 , . . . , h _ { \mathrm { S n } } ( z ) { \in } H _ { \mathrm { S n } } ( z ) \}$ , where $p _ { \mathrm { S n } } ^ { \mathrm { H } } ( z , h _ { \mathrm { S n } } ( z ) )$ stands for the probability that seller z, when his history is $h _ { \mathrm { S n } } ( z )$ , will play honestly if given the chance to play in his nth stage game.

Given any initial seller score profile, nature's strategy, buyers' strategy profile $\mathcal { B } = \{ B ( y ) | y { \in } [ 0 , 1 ] \}$ , and sellers' strategy profile $\mathcal { S } = \{ S ( z ) | z { \in } [ 0 , + \infty ) \}$ buyer $y ^ { \star } \mathbf { s }$ <sup>S ¼ f ð Þj</sup>total discounted expected payoff is

$$
\begin{array}{l} \overline {{g}} _ {\mathrm{B}} (y, \mathcal {B}, \mathcal {S}) \\ = \sum_ {n = 1} ^ {+ \infty} \beta_ {\mathrm{B}} ^ {n - 1} E _ {h _ {\mathrm{Bn}} (y) \in H _ {\mathrm{Bn}} (y)} [ p _ {\mathrm{Bn}} ^ {\mathrm{P}} (y, h _ {\mathrm{Bn}} (y)) \\ \times \sum_ {m = 1} ^ {+ \infty} \int_ {0} ^ {+ \infty} \mathrm{d} z E _ {h _ {\mathrm{Sm}} (z) \in H _ {\mathrm{Sm}} (z)} \\ [ f _ {\mathrm{Sm} | \mathrm{Bn}} (z, h _ {\mathrm{Sm}} (z) \mid y, h _ {\mathrm{Bn}} (y)) \\ \times (p _ {\mathrm{Sm}} ^ {\mathrm{H}} (z, h _ {\mathrm{Sm}} (z)) g _ {\mathrm{BX}} ^ {\mathrm{H}} (x _ {\mathrm{Bn}} (y)) \\ + (1 - p _ {\mathrm{Sm}} ^ {\mathrm{H}} (z, h _ {\mathrm{Sm}} (z))) g _ {\mathrm{BXZ}} ^ {\mathrm{C}} (x _ {\mathrm{Bn}} (y), z)) ] ], \end{array}\tag{6}
$$

where $E _ { a \in A } [ \cdot ]$ denotes the expectation over a random variable a in its support $A , f _ { \mathrm { S m | B n } } ( z , h _ { \mathrm { S m } } ( z ) | y , h _ { \mathrm { B n } } ( y ) )$ is the conditional probability density at seller $z ' s$ mth game with history $h _ { \mathrm { S m } } ( z )$ given that he is the opponent of buyer y with history $h _ { \mathrm { B n } } ( y )$ in the buyer's nth game $\begin{array} { r } { \big ( \sum _ { m = 1 } ^ { + \infty } \int _ { 0 } ^ { + \infty } \mathrm { ~ d } z E _ { h _ { \mathrm { S m } } } \left( z \right) \in H _ { \mathrm { S m } } \left( z \right) ~ \big [ \ f _ { \mathrm { S m } \mid \mathrm { B n } } \left( z , h _ { \mathrm { S m } } \left( z \right) \mid \boldsymbol { y } , \right. \big . } \end{array}$ hB $_ 1 ( y ) ) = 1 )$ <sup>ð Þ ð Þ</sup>, which is part of $h _ { \mathrm { B n } } ( y )$ . Similarly, seller $z ^ { \prime } \mathrm { s }$ total discounted expected payoff is

$$
\begin{array}{l} \overline {{g}} _ {\mathrm{S}} (z, \mathcal {B}, \mathcal {S}) \\ = \sum_ {n = 1} ^ {+ \infty} \beta_ {\mathrm{S}} ^ {n - 1} E _ {h _ {\mathrm{Sn}} (z) \in H _ {\mathrm{Sn}} (z)} [ (p _ {\mathrm{Sn}} ^ {\mathrm{H}} (z, h _ {\mathrm{Sn}} (z)) g _ {\mathrm{SX}} ^ {\mathrm{H}} (x _ {\mathrm{Sn}} (z)) \\ + (1 - p _ {\mathrm{Sn}} ^ {\mathrm{H}} (z, h _ {\mathrm{Sn}} (z))) g _ {\mathrm{SXZ}} ^ {\mathrm{C}} (x _ {\mathrm{Sn}} (z), z)) \\ \times \sum_ {m = 1} ^ {+ \infty} E _ {h _ {\mathrm{Bm}} (y _ {\mathrm{Sn}} (z)) \in H _ {\mathrm{Bm}} (y _ {\mathrm{Sn}} (z))} \\ [ f _ {\mathrm{Bm} | \mathrm{Sn}} (h _ {\mathrm{Bm}} (y _ {\mathrm{Sn}} (z)) | z, h _ {\mathrm{Sn}} (z)) \\ \times p _ {\mathrm{Bm}} ^ {\mathrm{P}} (y _ {\mathrm{Sn}} (z), h _ {\mathrm{Bm}} (y _ {\mathrm{Sn}} (z))) ] ], \end{array}\tag{7}
$$

where $x _ { \mathrm { S n } } ( z )$ and $y _ { \mathrm { S n } } ( z )$ are respectively the transaction size and buyer type in seller $z ' \mathrm { s }$ nth stage game, which are parts of history $h _ { \mathrm { S n } } ( z )$ , and $f _ { \mathrm { B m } | \mathrm { S n } } ( h _ { \mathrm { B m } } ( y _ { \mathrm { S n } } ( z ) ) | z ,$ $h _ { \mathrm { S n } } ( z ) )$ is the conditional probability density at buyer $y _ { \mathrm { S n } } ( z )  { \mathrm { ^ { \circ } s } }$ mth game with history $h _ { \mathrm { B m } } ( y _ { \mathrm { S n } } ( z ) )$ given that he is the opponent of seller z with history $h _ { \mathrm { S n } } ( z )$ in the seller's nth game, which is learned in the Bayesian fashion by the seller.

Given any initial seller score distribution profile and nature's strategy, a strategy profile $( \boldsymbol { B } ^ { * } , \boldsymbol { S } ^ { * } )$ will be a Nash Equilibrium when for any $y \in [ 0 , \ 1 ) , \ B ^ { * } ( y )$ maximizes buyer $y ^ { \bullet } \mathbf { s }$ total discounted expected payoff given that other players all play according to $B ^ { * }$ and $S ^ { * }$ , and when for any $z { \in } [ 0 , \ 1 ) , \ S ^ { * } ( z )$ <sup>B S</sup>maximizes seller z's total discounted expected payoff given that other players all play according to $B ^ { * }$ and $\boldsymbol { S } ^ { * }$ . The profile will further be perfect Bayesian if the above is true when everything starts from any possible play history.

Note that there might be multiple nature strategies that fit the above descriptions. Also, we have not specified in the above how much each player knows about the marginal seller score distribution $f _ { \mathrm { W } } ( \boldsymbol { w } )$ (An eBay buyer may only pay attention to his current seller's comments or may compare his seller's comments with many other sellers', and an eBay seller may or may not be aware of his fellow sellers' comments). So the above repeated game will not be exactly specified until all these details have been settled. However, we need not consider these details if our focus is on the steady-state behavior of the game.

## 2.4. Analysis of the repeated game

Since it seems very unlikely to identify Nash or perfect Bayesian strategy profiles for the repeated game, we now proceed to analyze the game when static strategies lead it to a steady state. Once in this state, buyers of different types will have statistically the same experience and therefore are no longer required to be distinguished from each other, and the seller's score distribution profile $f _ { \mathrm { W } | Z }$ $( w | z )$ will become static and publicly known. Each buyer will use this distribution and the current-opponent-score portion of his history to infer about his current opponent. Also, since a buyer's current action will not impact the profile and his own expected future payoff, the buyer will only be concerned with his stage-game payoff in each transaction. Consequently, sellers will learn nothing about their opponents using their own histories. In addition, different nature strategies will not lead to different longrun expected payoffs.

Now we define $\overline { { g _ { \mathrm { S Z W } } } } ( z , w )$ to be the long-run <sup>ð Þ</sup>expected gain for a type-z score-w seller (seller z if he happens to have score w) right before a transaction starts. Then, in a size-x transaction, if the seller has the chance to play and plays honestly, his long-run expected gain will be

$$
\begin{array}{l} \overline {{g _ {\mathrm{SXZW}} ^ {\mathrm{H}}}} (x, z, w) \\ = g _ {\mathrm{SX}} ^ {\mathrm{H}} (x) + \beta_ {\mathrm{S}} \int_ {w ^ {\prime} \in \mathcal {W}} \overline {{g _ {\mathrm{SZW}}}} (z, w ^ {\prime}) f _ {\mathrm{WW}} ^ {\mathrm{H}} (w, w ^ {\prime}) \mathrm{d} w ^ {\prime}, \end{array}\tag{8}
$$

while if he has the chance to play and cheats, his longrun expected gain will be

$$
\begin{array}{l} \overline {{g _ {\mathrm{SXZW}} ^ {\mathrm{C}}}} (x, z, w) \\ = g _ {\mathrm{SXZ}} ^ {\mathrm{C}} (x, z) + \beta_ {\mathrm{S}} \int_ {w ^ {\prime} \in \mathcal {W}} \overline {{g _ {\mathrm{SZW}}}} (z, w ^ {\prime}) f _ {\mathrm{WW}} ^ {\mathrm{C}} (w, w ^ {\prime}) \mathrm{d} w ^ {\prime}. \end{array}\tag{9}
$$

A type-z score-w seller will play honestly with a certain probability $p _ { \mathrm { S X Z W } } ^ { \mathrm { H } } ( x , z , w )$ and cheat with probability $\bar { 1 } - p _ { \mathrm { S X Z W } } ^ { \mathrm { H } } ( x , z , w )$ . We may assume that

$$
p _ {\mathrm{SXZW}} ^ {\mathrm{H}} (x, z, w) = P _ {\mathrm{S}} (\overline {{g _ {\mathrm{SXZW}} ^ {\mathrm{H}}}} (x, z, w) - \overline {{g _ {\mathrm{SXZW}} ^ {\mathrm{C}}}} (x, z, w))\tag{10}
$$

for a certain function $P _ { \mathrm { S } } ( u )$ which satisfies $0 \leq P _ { \mathrm { S } } ( u ) \leq 1$ and

$$
P _ {\mathrm{S}} (u + \Delta u) \geq P _ {\mathrm{S}} (u) \text {   for   } \Delta u \geq 0.\tag{11}
$$

In each transaction, a buyer believes that the distribution of a seller's score is some $f _ { \mathrm { W } } ( \boldsymbol { w } )$ and that the conditional distribution of a seller's type with respect to his score is some $f _ { Z | \mathrm { W } } ( z | w )$ . So in a size-x transaction, a buyer will on average gain $g _ { \mathrm { B X W } } ^ { \mathrm { P } } ( x , w )$ if he proceeds with the transaction, where

$$
\begin{array}{l} g _ {\mathrm{BXW}} ^ {\mathrm{P}} (x, w) \\ = \int_ {z = 0} ^ {+ \infty} [ p _ {\mathrm{SXZW}} ^ {\mathrm{H}} (x, z, w) g _ {\mathrm{BX}} ^ {\mathrm{H}} (x) \\ \qquad + (1 - p _ {\mathrm{SXZW}} ^ {\mathrm{H}} (x, z, w)) g _ {\mathrm{BXZ}} ^ {\mathrm{C}} (x, z) ] f _ {Z | \mathrm{W}} (z \mid w) \mathrm{d} z. \end{array}\tag{12}
$$

There is a certain $p _ { \mathrm { B X W } } ^ { \mathrm { P } } ( x , w )$ chance that the buyer will proceed with the transaction and therefore there is a $1 - p _ { \mathrm { B X W } } ^ { \mathrm { \Delta p } } ( x , w )$ chance that he will walk away from it. We may assume that

$$
p _ {\mathrm{BXW}} ^ {\mathrm{P}} (x, w) = P _ {\mathrm{B}} (g _ {\mathrm{BXW}} ^ {\mathrm{P}} (x, w))\tag{13}
$$

for a certain function $P _ { \mathrm { B } } ( u )$ which satisfies $0 \leq P _ { \mathrm { B } } ( u ) \leq 1$ and

$$
P _ {\mathrm{B}} (u + \Delta u) \geq P _ {\mathrm{B}} (u) \text {   for   } \Delta u \geq 0.\tag{14}
$$

For instance, we may use positive real numbers $\varDelta _ { \mathrm { B } }$ and $\varDelta _ { \mathrm { { S } } }$ to represent respectively the fuzziness of the buyer's and the seller's decision-making processes under the current situation. On one hand, their existence is necessary for the stability of the results; on the other hand, they reflect the difficulty of behaving exactly rationally on the part of the decision makers inside very complex systems. To model the fuzziness, we introduce function $A ( a , b , c )$ so that it equals the medium value of $- 1 , ( a - b ) / c ,$ , and +1. For instance, we let $A ( 4 , 2 , 3 ) = 2 / 3$ and $\varLambda ( 4 , 0 , 3 ) = 1$ . Then, we may let

$$
P _ {\mathrm{S}} (u) = \frac {1}{2} + \frac {1}{2} \varLambda (u, 0, \varDelta_ {\mathrm{S}}),\tag{15}
$$

and

$$
P _ {\mathrm{B}} (u) = \frac {1}{2} + \frac {1}{2} \Lambda (u, 0, \Delta_ {\mathrm{B}}).\tag{16}
$$

From the way buyers and sellers make their decisions, we also obtain the transitional kernel $T _ { \mathrm { W W } | Z } ( w , w ^ { \prime } | z )$ for $f _ { \mathrm { W } | Z } ( w | z )$

$$
\begin{array}{l} T _ {\mathrm{WW|Z}} (w, w ^ {\prime} \mid z) \\ = \int_ {x = 0} ^ {+ \infty} [ p _ {\mathrm{SXZW}} ^ {\mathrm{H}} (x, z, w) f _ {\mathrm{WW}} ^ {\mathrm{H}} (w, w ^ {\prime}) \\ \quad + (1 - p _ {\mathrm{SXZW}} ^ {\mathrm{H}} (x, z, w)) f _ {\mathrm{WW}} ^ {\mathrm{C}} (w, w ^ {\prime}) ] f _ {\mathrm{X}} (x) \mathrm{d} x. \end{array}\tag{17}
$$

Then, we have

$$
\int_ {w ^ {\prime} \in \mathcal {W}} f _ {\mathrm{W} | \mathrm{Z}} (w ^ {\prime} \mid z) T _ {\mathrm{WW} | \mathrm{Z}} (w ^ {\prime}, w \mid z) \mathrm{d} w ^ {\prime} = f _ {\mathrm{W} | \mathrm{Z}} (w \mid z).\tag{18}
$$

Now comes the marriage of perceived and real seller distributions. In reality, the score distribution $f _ { \mathrm { W } } ( \boldsymbol { w } )$ and the seller type distribution conditioned on score $f _ { Z | \mathrm { W } } ( z |$ w) are determined through the following expressions by $f _ { Z } ( z )$ and $f _ { \mathrm { W } | Z } ( w | z )$

$$
f _ {\mathrm{W}} (w) = \int_ {z = 0} ^ {+ \infty} f _ {\mathrm{W} | Z} (w \mid z) f _ {Z} (z) \mathrm{d} z\tag{19}
$$

and

$$
f _ {\mathrm{Z} | \mathrm{W}} (z \mid w) = \frac {f _ {\mathrm{W} | \mathrm{Z}} (w \mid z) f _ {\mathrm{Z}} (z)}{f _ {\mathrm{W}} (w)}.\tag{20}
$$

The expected gain $\overline { { g _ { \mathrm { S Z W } } } } ( z , w )$ for a type-z score-w <sup>ð Þ</sup>seller right before a transaction starts is determined by the following implicit equation:

$$
\begin{array}{l} \overline {{g _ {\mathrm{SZW}}}} (z, w) \\ = \int_ {x = 0} ^ {+ \infty} \left\{p _ {\mathrm{BXW}} ^ {\mathrm{P}} (x, w) \left[ p _ {\mathrm{SXZW}} ^ {\mathrm{H}} (x, z, w) \overline {{g _ {\mathrm{SXZW}} ^ {\mathrm{H}}}} (x, z, w) \right. \right. \\ \left. + \left(1 - p _ {\mathrm{SXZW}} ^ {\mathrm{H}} (x, z, w)\right) \overline {{g _ {\mathrm{SXZW}} ^ {\mathrm{C}}}} (x, z, w) \right] \\ \left. + \beta_ {\mathrm{S}} \left(1 - p _ {\mathrm{BXW}} ^ {\mathrm{P}} (x, w)\right) \overline {{g _ {\mathrm{SZW}}}} (z, w) \right\} f _ {X} (x) \mathrm{d} x. \end{array} \tag {21}
$$

Note that the last term on the right-hand side corresponds to the outcome in which the buyer withdraws from the current transaction and therefore involves $\overline { { g _ { \mathrm { S Z W } } } } ( z , w )$ itself (for the next transaction).

<sup>ð Þ</sup>Once the equations in this subsection have been solved, all market performances can be calculated. We list the expressions of the most relevant performances in Appendix B.

## 3. Some discussion

We have established a repeated-game-theoretical model that has the potential to interpret the role of a feedback system in an online market where transactions take place between strangers. Key elements of the model include: the peculiar forms of the stage-game gain functions which condone incentives for sellers to cheat and buyers to shun away from trading; the feedback updating mechanism, exogenously and probabilistically reflecting buyers' feedback writing behavior, which leads each seller's score to two opposite directions depending on his behavior; and the infinite-horizon, multi-seller, multi-buyer, repeated-game setting where every player seeks to maximize his total discounted expected payoff.

We have not been able to make theoretical claims out of the general model. The major difficulties we face involve multiple dimensions and implicit equations. In the finite-horizon version of the game, each player's strategy is implicitly contingent on the seller score distribution profile, whose number of dimensions is even uncountable; while in the steady-state analysis of the game, we encounter equations where the same functions are involved on both sides.

Naturally, we should expect the following properties from the repeated game model:

$$
\overline {{g _ {\mathrm{B}}}} \geq \overline {{g _ {\mathrm{B}} ^ {0}}},\tag{22}
$$

and

$$
\begin{array}{c} \overline {{g _ {\mathrm{SZ}}}} (z + \Delta z) - \overline {{g _ {\mathrm{SZ}}}} (z) \leq \overline {{g _ {\mathrm{SZ}} ^ {0}}} (z + \Delta z) \\ - \overline {{g _ {\mathrm{SZ}} ^ {0}}} (z) \text {for} \Delta z \geq 0. \end{array}\tag{23}
$$

That is, the feedback system benefits buyers and honest sellers.

In Section 2.2, we have speculated the advent of the tendency for a more honest seller to have a lower score. This tendency will serve as one link in a cycle of benevolent effects that a feedback system can bring to the online markets. When this tendency does materialize, a buyer will, through his personal experience, form a belief that a lower score announces a seller less prone to cheating, and therefore he will be more willing to trade with the owner of such a score. Because of this, a seller with a lower score will have more chances for trading and will probably fare better in the long run. Being aware of this, even when cheating brings more short-term gain, a seller will be more reluctant to do so fearing that an unfavorable updating of his score by the antagonized buyer will jeopardize his future. However, the temptation for short-term gain is still stronger among the morally weaker sellers than among the morally stronger ones. Therefore in the long run, we will still observe the trend that those sellers more prone to cheating do cheat more often and receive higher scores than those less prone to cheating. Now, we have come back to the starting link of the cycle, which means that this chain of effects is self-sustainable.

Therefore, we should expect $( W | z )$ to be increasing in z in some sense and $( Z | w )$ to be increasing in w in some sense which prove that the first link in the above cycle does emerge. We should also expect to have $p _ { \mathrm { S X Z } } ^ { \mathrm { H } ^ { - } } ( x , z ) { \geq } p _ { \mathrm { S X Z } } ^ { \mathrm { H 0 } } ( x , z )$ or to have at least $p _ { \mathrm { S X } } ^ { \bar { \mathrm { H } } } ( x ) \geq$ $p _ { \mathrm { S X } } ^ { \mathrm { H 0 } } ( x )$ and $p _ { \mathrm { S } Z } ^ { \mathrm { H } } ( z ) { \geq } p _ { \mathrm { S } Z } ^ { \mathrm { H 0 } } ( z )$ at the aggregate levels so that a seller will be more reluctant to cheat with a feedback system than without a feedback system.

For the without-feedback situation, it can be shown easily that $p _ { \mathrm { S X Z } } ^ { \mathrm { H 0 } } ( x , z )$ decreases in both x and z due to Inequality Eq. (3) (refer to Eqs. (10) and (15)). Now for the with-feedback situation, we should still expect $p _ { \mathrm { S X Z } } ^ { \mathrm { H } } ( x , z )$

to decrease in z so that sellers with higher z will still cheat more than sellers with lower z.

In Appendix C, we give a complete analysis of a simple example. In the example, there are only two types of sellers as well as two types of scores; transactions are all of the same size; and, Eqs. (15) and (16) are adopted as the expressions for $P _ { \mathrm { S } } ( u )$ and $P _ { \mathrm { B } } ( u )$ , respectively, and it is assumed that $\scriptstyle A _ { \mathrm { B } } = A _ { \mathrm { S } } = 0$ . Through the analysis, the benefit of the feedback system is clearly demonstrated.

## 4. A numerical study

With the help of computers, we conduct a numerical study on the effects brought forth by the stylized feedback system introduced in Section 2.2. We adopt Eqs. (15) and (16) as the basis for the players' decision-making mechanism. Here, all distributions are assumed to be discrete. We assume that transaction sizes x can be $1 , 2 , . . . , \bar { X }$ and the probability for the realization of any x is 1/X<sup>¯</sup>. We assume that the seller types z can be $0 , 1 , . . . , \overline { { Z } } - 1$ and the distribution of z follows the geometric distribution with a tail cutoff. That is, there is a parameter $R _ { Z } \in [ 0 , 1 )$ such that the probability for the realization of z is $( R _ { Z } ) ^ { z } ( 1 - R _ { Z } ) \mathrm { f o r } z { = } 0$ 2 $1 , . . . , \overline { { Z } } - 2$ and is $( R _ { Z } ) ^ { { \bar { Z } } - 1 }$ for $z { = } \overline { { Z } } { - } 1$ . We let the gain functions be such that $g _ { \mathrm { S X } } ^ { \mathrm { H } } ( x ) { = } g _ { \mathrm { B X } } ^ { \mathrm { H } } ( x ) { = } x , g _ { \mathrm { B X Z } } ^ { \mathrm { C } } ( x , z ) { = } x ( 1 -$ $z ^ { - } 2 z / ( \overline { { Z } } - 1 ) ) + C \ ( x z ) ^ { \alpha }$ , and $g _ { \mathrm { s X Z } } ^ { \mathrm { C } } ( x , \ z ) { = } x ( 1 + z ) { - } D ( x z ) ^ { \alpha }$ for some positive C and D with $C { < } D$ and some $\alpha \in [ 0 , 1 ]$ The rationale for such gain functions is given in Appendix D.

In the first round of the experiment, we let $\stackrel { \_ } { X } = 1 0 .$ $\overline { { Z } } = 1 0 , R _ { Z } = 0 . 5 , C = 1 . 0 , D = 1 . 5 , \alpha = 0 . 5 , \beta _ { \mathrm { B } } = 0 . 9$ $\beta _ { \mathrm { S } } = 0 . 9 9 , ~ \bar { W } = 1 0 , ~ p _ { \mathrm { H } } = 0 . 5 ,$ , and $p _ { \mathrm { C } } { = } 0 . 8$ . We let $\varDelta _ { \mathrm { B } } ^ { 0 } =$ $\textstyle A _ { \mathrm { S } } ^ { 0 } = A ^ { 0 } = 0 . 1$ to capture the uncertainty the decision makers face in the without-feedback situation. On the other hand, the iterative process for the with-feedback situation will not converge unless $\varDelta _ { \mathrm { B } }$ and $\varDelta _ { \mathrm { { S } } }$ are both large enough. If they are to be the same, the smallest multiple of 0.1 that they need to be is 0.7. In this round, we let $\varDelta _ { \mathrm { B } } = \varDelta _ { \mathrm { S } } = 0 . 7$ . We present our computational findings in the following.

Finding #1: Buyers are better off with the existence of a reputation feedback system in an online C2C auction market. We obtain $\overline { { g _ { \mathrm { B } } ^ { 0 } } } \simeq 3 . 5 3$ while $\overline { { g _ { \mathrm { B } } } } \simeq 4 7 . 0 2$ . Hence, Inequality Eq. (22) is indeed satisfied. This is consistent with the finding of Bolton, Katok, and Ockenfels [4]. At the same time, we find that on average a seller is worse off with a feedback system, in that $\overline { { g _ { \mathrm { S } } ^ { 0 } } } \simeq 6 8 7 . 9 9$ while $\overline { { g _ { \mathrm { S } } } } \simeq 5 6 3 . 1 5$ . Also, the existence of a feedback system <sup>g</sup>makes cheating less attractive. To see how different sellers fare differently, we draw a figure (Fig. 1) of curve $\overline { { g _ { \mathrm { S Z } } } } ( z )$ vs. curve $\overline { { g _ { \mathrm { S Z } } ^ { 0 } } } ( z )$

<sup>ð Þ ð Þ</sup>From Fig. 1, we see that $\overline { { g _ { \mathrm { S Z } } } } ( z )$ rises slower than $\overline { { g _ { \mathrm { S Z } } ^ { 0 } } } ( z )$ <sup>ð Þ</sup>. Hence, Inequality Eq. (23) is satisfied. Moreover, we see in this example that the most honest sellers, the type-0 sellers, gain more when a feedback system is introduced: $\overline { { g _ { \mathrm { S Z } } } } ( 0 ) \simeq 5 3 9 . 5 6 > \overline { { g _ { \mathrm { S Z } } ^ { 0 } } } ( 0 ) \simeq 4 3 9 . 1 0$

<sup>ð Þg ð Þg</sup>Finding #2: Buyers are more willing to trade with lower-scored sellers, i.e., more reputable sellers are more likely to sell their items. We draw the curve of $p _ { \mathrm { B W } } ^ { \mathrm { P } } ( w )$ in Fig. 2. We see that $p _ { \mathrm { B W } } ^ { \mathrm { P } } ( w )$ has a distinct decreasing trend over w. This observation is in agreement with the findings of Bolton, Katok, and Ockenfels [4] and Resnick and Zeckhauser [19]. The case where $\bar { p } _ { \mathrm { B W } } ^ { \mathrm { P } } ( 0 ) { < } p _ { \mathrm { B W } } ^ { \mathrm { P } } ( 1 )$ might be interpreted as sellers become complacent and less willing to play honestly once their scores have reached the best possible level. Hence, a buyer has to be more cautious while dealing with such sellers.

Finding #3: Buyers are more willing to trade when the auction market has a reputation feedback system than without. We note that $p _ { \mathrm { B } } ^ { \mathrm { P } } \simeq 0 . 9 7 3 \mathrm { > } p _ { \mathrm { B } } ^ { \mathrm { P 0 } } \simeq 0 . 8 8 6$ . This <sup>g g</sup>is also verified by Bolton, Katok, and Ockenfels [4].

Finding #4: Sellers are more willing to trade honestly when a reputation feedback system is in place. We find that $p _ { \mathrm { S X Z } } ^ { \mathrm { H } } ( x , z )$ almost always dominates $p _ { \mathrm { S X Z } } ^ { \mathrm { H 0 } } ( x , z )$ but for a few $x { - } z$ pairs. In Figs. 3 and 4, we draw respectively the curves $p _ { \mathrm { S X } } ^ { \mathrm { H } } ( x ) \mathbf { \bar { v s } } . p _ { \mathrm { S X } } ^ { \mathrm { H 0 } } ( x )$ and $p _ { \mathrm { S } Z } ^ { \mathrm { H } } ( z ) \ \mathrm { v s } .$ $p _ { \mathrm { S Z } } ^ { \mathrm { H } \hat { 0 } } ( z )$ . Clearly, we have both $p _ { \mathrm { S X } } ^ { \mathrm { H } } ( x ) { \geq } p _ { \mathrm { S X } } ^ { \mathrm { H 0 } } ( x )$ for any x and $p _ { \mathrm { S Z } } ^ { \mathrm { H } } ( z ) \overset { \cdot } { = } \dot { p } _ { \mathrm { S Z } } ^ { \mathrm { H 0 } } ( z )$ for any z. Again, this result is consistent with the finding of Bolton, Katok, and Ockenfels [4]. Note also that $p _ { \mathrm { S } } ^ { \mathrm { H } } \simeq 0 . 9 2 7 { > } p _ { \mathrm { S } } ^ { \mathrm { H 0 } } \simeq 0 . 3 2 1$ <sup>g g</sup>The fact that a seller becomes more complacent and starts to cheat more once his score reaches 0 is again confirmed by the fact that $p _ { \mathrm { S W } } ^ { \mathrm { H } } ( 0 ) \simeq 0 . 1 9 6$ is much smaller than $p _ { \mathrm { S W } } ^ { \mathrm { H } } ( w )$ for all other $w ^ { \prime } \mathbf { s } ,$ <sup>Þg</sup>, which are all very close to 1.0.

From Fig. 3, we also see that sellers cheat more with larger sales, while the trend is less apparent when a feedback system is in place. Note also that $p _ { \mathrm { S } Z } ^ { \mathrm { H } } ( z )$ is almost always decreasing in z. So sellers more prone to cheating will still cheat more with a feedback system.

![](/api/attachments/DDJPAZFV/fulltext/images/383d3340de0eb23e8f2dca42bc48f2b68a8ef41f184f364b2030efdfa6d6df71.jpg)  
Fig. 1. $\overline { { g _ { \mathrm { S Z } } } } \left( z \right)$ vs. $\overline { { g _ { \mathrm { S Z } } ^ { 0 } } }$ z .

![](/api/attachments/DDJPAZFV/fulltext/images/60f2495ef27d0691cdf3048a87740d791991e5da40597d91f3e88fb53d0d42c8.jpg)  
Fig. 2. p<sub>BW</sub><sup>P</sup> (w).

In our next round of experiments, we consider the <sub>important</sub> <sub>market</sub> <sub>performance</sub> <sub>indicators,</sub> <sub>i.e., gB,</sub> P<sub>g ,</sub> $\bar { \overline { { g _ { \mathrm { S Z } } } } } ( 0 ) , p _ { \mathrm { B } } ^ { \mathrm { P } }$ , and $p _ { \mathrm { { S } } } ^ { \mathrm { { \dot { H } } } }$ , while allowing $\bar { W } , p _ { \mathrm { H } } , p _ { \mathrm { C } } , \varDelta _ { \mathrm { B } }$ and $\varDelta _ { \mathrm { { S } } }$ <sup>ð Þ</sup>to vary and fixing other parameters. In Table 1, we present the results when $\bar { W }$ is fixed at 10, $p _ { \mathrm { H } }$ is at either 0.5 or 0.0, and $\varDelta _ { \mathrm { B } }$ and $\varDelta _ { \mathrm { { S } } }$ are fixed to be 0.9.

From Table 1, regardless of the $p _ { \mathrm { H } }$ value, we see that there is a certain level $p _ { \mathrm { { C 0 } } }$ of $p _ { \mathrm { { C } } }$ (between 0.3727 and 0.3728 when $p _ { \mathrm { H } } { = } 0 . 5$ and between 0.3281 and 0.3282 when $p _ { \mathrm { H } } { = } 0 . 0 )$ such that the market performance indicators which favor the buyers, $g _ { \mathrm { B } }$ and $p _ { \mathrm { S } } ^ { \mathrm { H } }$ , keep improving as $p _ { \mathrm { { C } } }$ increases from 0 to $p _ { \mathrm { { C 0 } } } ,$ , and there are no discernible trends for them as $p _ { \mathrm { { C } } }$ increases beyond $p _ { \mathrm { { C 0 } } }$ . Also, these performance indicators are at their best when $p _ { \mathrm { { C } } }$ is just below $p _ { \mathrm { { C 0 } } }$ . Therefore, the intuition that a higher level of buyer unforgiveness induces more honest behavior and more gains for the buyers is only true when the level does not go beyond a certain point.

<sub>On the other hand, the average seller's gain</sub> P<sub>gS</sub> decreases when $p _ { \mathrm { { C } } }$ increases from 0 to $p _ { \mathrm { { C 0 } } } ,$ encounters an upward jump, and then mildly fluctuates when $p _ { \mathrm { { C } } }$ increases beyond $p _ { \mathrm { { C 0 } } }$ . Since the gain of an honest seller $\overline { { g _ { \mathrm { S Z } } } } ( 0 )$ is almost unaffected by the change in $p _ { \mathrm { { C } } }$ , the <sup>ð Þ</sup>gains of less honest sellers will change in similar fashion as $\overline { { g _ { \mathrm { S } } } }$ . Comparing results for the two $p _ { \mathrm { H } }$ values, we see that the market does not perform better when $p _ { \mathrm { H } }$ changes from 0 to 0.5, and that sellers become more honest when $p _ { \mathrm { H } }$ takes the smaller value, i.e., rewarding honest behavior does not seem to benefit the buyers and honest sellers.

![](/api/attachments/DDJPAZFV/fulltext/images/c3215cbe8ea7795a9483563866d66b0c421852576f0206beb17d2ca7671f4eed.jpg)  
Fig. 3. $p _ { \mathrm { S X } } ^ { \mathrm { H } } ( x )$ vs. $p _ { \mathrm { S X } } ^ { \mathrm { H 0 } } ( x )$

Table 1  
![](/api/attachments/DDJPAZFV/fulltext/images/f3b0e913858d44eccb15a35bf99d112623526ba6358b44ea21c6b48655994aca.jpg)  
Fig. 4. $p _ { \mathrm { S } Z } ^ { \mathrm { H } } ( z )$ vs. $p _ { \mathrm { S Z } } ^ { \mathrm { H 0 } } ( z )$

Next, we fix $p _ { \mathrm { { C } } }$ at 0.3, keep all other parameters the same as before, and allow $p _ { \mathrm { H } }$ to vary. The results are contained in Table 2.

Finding #5: Rewarding an honestly-behaving seller is less effective on promoting market performances than punishing a cheating seller. Note that we have not included the results for $p _ { \mathrm { H } } { = } 0 . 1$ in Table 2 because it requires much larger $\varDelta _ { \mathrm { B } }$ and $\varDelta _ { \mathrm { { S } } }$ for the iterative procedure to converge. We see from the table that the market performances fluctuate mildly as $p _ { \mathrm { H } }$ increases.

Results when $\begin{array} { r } { \bar { W } = 1 0 , } \end{array}$ $p _ { \mathrm { H } } { = } 0 . 5$ or 0.0, and $\varDelta _ { \mathrm { B } } = \varDelta _ { \mathrm { S } } = 0 . 9$

<table><tr><td> $p_{\text{H}}$ </td><td> $p_{\text{C}}$ </td><td> $g_{\text{B}}$ </td><td> $\overline{g_{\text{S}}}$ </td><td> $\overline{g_{\text{SZ}}} (0)$ </td><td> $p_{\text{B}}^{\text{P}}$ </td><td> $p_{\text{S}}^{\text{H}}$ </td></tr><tr><td rowspan="9">0.5</td><td>0.1</td><td>39.57</td><td>580.08</td><td>550.00</td><td>0.947</td><td>0.920</td></tr><tr><td>0.2</td><td>47.88</td><td>556.32</td><td>550.00</td><td>0.969</td><td>0.971</td></tr><tr><td>0.3</td><td>51.60</td><td>551.48</td><td>550.00</td><td>0.984</td><td>0.989</td></tr><tr><td>0.3727</td><td>54.06</td><td>549.70</td><td>550.00</td><td>0.995</td><td>0.998</td></tr><tr><td>0.3728</td><td>43.28</td><td>608.31</td><td>550.00</td><td>0.985</td><td>0.885</td></tr><tr><td>0.4</td><td>43.79</td><td>605.06</td><td>550.00</td><td>0.985</td><td>0.891</td></tr><tr><td>0.6</td><td>46.10</td><td>591.37</td><td>550.00</td><td>0.988</td><td>0.917</td></tr><tr><td>0.8</td><td>45.74</td><td>587.78</td><td>550.00</td><td>0.984</td><td>0.919</td></tr><tr><td>1.0</td><td>43.80</td><td>598.46</td><td>549.92</td><td>0.983</td><td>0.868</td></tr><tr><td rowspan="9">0.0</td><td>0.1</td><td>49.15</td><td>491.50</td><td>540.63</td><td>0.894</td><td>0.998</td></tr><tr><td>0.2</td><td>49.86</td><td>498.58</td><td>538.14</td><td>0.907</td><td>1.000</td></tr><tr><td>0.3</td><td>51.22</td><td>512.16</td><td>543.18</td><td>0.931</td><td>1.000</td></tr><tr><td>0.3281</td><td>50.89</td><td>508.93</td><td>538.33</td><td>0.925</td><td>1.000</td></tr><tr><td>0.3282</td><td>54.76</td><td>547.58</td><td>549.99</td><td>0.996</td><td>1.000</td></tr><tr><td>0.4</td><td>54.92</td><td>549.18</td><td>549.98</td><td>0.999</td><td>1.000</td></tr><tr><td>0.6</td><td>54.56</td><td>545.60</td><td>549.50</td><td>0.992</td><td>1.000</td></tr><tr><td>0.8</td><td>54.36</td><td>543.57</td><td>549.39</td><td>0.988</td><td>1.000</td></tr><tr><td>1.0</td><td>53.20</td><td>532.02</td><td>546.13</td><td>0.967</td><td>1.000</td></tr></table>

Table 2  
Results when $\overline { { W } } = 1 0 , p _ { \mathrm { C } } = 0 . 3 ,$ and $\varDelta _ { \mathrm { B } } = \varDelta _ { \mathrm { S } } = 0 . 9$

<table><tr><td> $p_{\text{H}}$ </td><td> $g_{\text{B}}$ </td><td> $\overline{g_{\text{S}}}$ </td><td> $\overline{g_{\text{SZ}}} (0)$ </td><td> $p_{\text{B}}^{\text{P}}$ </td><td> $p_{\text{S}}^{\text{H}}$ </td></tr><tr><td>0.0</td><td>51.22</td><td>512.16</td><td>543.18</td><td>0.931</td><td>1.000</td></tr><tr><td>0.2</td><td>47.36</td><td>549.94</td><td>532.27</td><td>0.963</td><td>0.928</td></tr><tr><td>0.3</td><td>44.28</td><td>567.95</td><td>535.17</td><td>0.962</td><td>0.896</td></tr><tr><td>0.4</td><td>53.69</td><td>549.00</td><td>550.00</td><td>0.992</td><td>0.997</td></tr><tr><td>0.5</td><td>51.60</td><td>551.48</td><td>550.00</td><td>0.984</td><td>0.989</td></tr><tr><td>0.6</td><td>49.82</td><td>553.44</td><td>550.00</td><td>0.974</td><td>0.983</td></tr><tr><td>0.7</td><td>48.94</td><td>556.45</td><td>550.00</td><td>0.972</td><td>0.979</td></tr><tr><td>0.8</td><td>47.78</td><td>558.78</td><td>550.00</td><td>0.971</td><td>0.972</td></tr><tr><td>0.9</td><td>47.19</td><td>561.92</td><td>550.00</td><td>0.970</td><td>0.969</td></tr><tr><td>1.0</td><td>46.89</td><td>565.25</td><td>550.00</td><td>0.971</td><td>0.967</td></tr></table>

Last, we fix $p _ { \mathrm { H } }$ at $0 . 0 , p _ { \mathrm { C } }$ at 0.3, and $\varDelta _ { \mathrm { B } }$ and $\varDelta _ { \mathrm { { S } } }$ at 0.9, and allow $\bar { W }$ to vary. The results are recorded in Table 3.

Note that market performance at $\bar { W } { = } 0$ is even worse than when there is no feedback system. But $\bar { W } { = } 0$ is indeed equivalent to there being no feedback system. The difference is that we have allowed more fuzziness here than when we obtained the results for the case without a feedback system.

Finding #6: The existence of even the most primitive reputation feedback system makes a market perform much better. From the results, we see that market performance improves dramatically from $\bar { W } { = } 0$ to $\bar { W } = 1$ . As W<sup>¯</sup> increases further, we see that market performance keeps on improving, though not quite as impressively, and after W<sup>¯</sup> reaches about 14, the performance starts to fluctuate mildly.

In his single-seller model, Dellarocas [9] finds that market efficiency cannot be improved by simply expanding each seller's feedback account. So the above empirical result seemingly contradicts his finding. However, in understanding the difference in these outcomes, we should take into account the difference in our respective assumptions about the number of seller types and their repercussions. In Dellarocas' single-seller model, a buyer uses his trading partner's score only to infer the partner's future behavior; while in our multi-type model, a buyer more importantly uses the score to infer the partner's type. A larger score space may help perform the inference better. Meanwhile, our outcome is also related to our specific assumption about the seller type distribution. A more realistic model may even allow sellers of different types to enter and exit online markets at different rates based on the different rewards from the markets, and let the seller type distribution to gradually converge to an equilibrium. With such a system, it may be that only the most honest sellers eventually remain in the market, not much seller-type inference is needed from the scores, and the score space needs only to be minimal.

Table 3  
Results when $p _ { \mathrm { H } } { = } 0 . 0 , p _ { \mathrm { C } } { = } 0 . 3 ,$ and $\varDelta _ { \mathrm { B } } { = } \varDelta _ { \mathrm { S } } { = } 0 . 9$

<table><tr><td> $\overline{W}$ </td><td> $g_B$ </td><td> $\overline{g_S}$ </td><td> $\overline{g_{SZ}}(0)$ </td><td> $p_B^P$ </td><td> $p_S^H$ </td></tr><tr><td>0</td><td>2.73</td><td>537.85</td><td>343.18</td><td>0.693</td><td>0.310</td></tr><tr><td>1</td><td>37.73</td><td>381.85</td><td>456.61</td><td>0.712</td><td>0.981</td></tr><tr><td>2</td><td>47.41</td><td>474.70</td><td>526.30</td><td>0.865</td><td>0.998</td></tr><tr><td>3</td><td>49.58</td><td>495.75</td><td>538.20</td><td>0.901</td><td>0.999</td></tr><tr><td>4</td><td>49.53</td><td>495.26</td><td>539.45</td><td>0.900</td><td>0.998</td></tr><tr><td>5</td><td>50.54</td><td>505.44</td><td>541.44</td><td>0.919</td><td>1.000</td></tr><tr><td>6</td><td>50.61</td><td>506.14</td><td>540.73</td><td>0.920</td><td>1.000</td></tr><tr><td>8</td><td>51.12</td><td>511.18</td><td>543.08</td><td>0.929</td><td>1.000</td></tr><tr><td>10</td><td>51.22</td><td>512.16</td><td>543.18</td><td>0.931</td><td>1.000</td></tr><tr><td>12</td><td>54.88</td><td>548.76</td><td>549.98</td><td>0.998</td><td>1.000</td></tr><tr><td>14</td><td>54.89</td><td>548.94</td><td>549.98</td><td>0.998</td><td>1.000</td></tr><tr><td>16</td><td>54.88</td><td>548.79</td><td>549.96</td><td>0.998</td><td>1.000</td></tr><tr><td>18</td><td>54.81</td><td>548.05</td><td>549.91</td><td>0.996</td><td>1.000</td></tr><tr><td>20</td><td>50.97</td><td>509.67</td><td>538.99</td><td>0.927</td><td>1.000</td></tr><tr><td>25</td><td>53.85</td><td>538.52</td><td>548.63</td><td>0.979</td><td>1.000</td></tr><tr><td>30</td><td>53.16</td><td>531.58</td><td>548.27</td><td>0.967</td><td>1.000</td></tr></table>

Throughout the study, we find that $( W | z )$ is always stincreasing in z and $( Z | w )$ is always st-increasing in w.

## 5. Concluding remarks

In this paper, we have established a dynamic gametheoretic model for the mechanism of reputation feedback systems in online C2C auction markets. We have also conducted a numerical study based on the game-theoretic model.

Our results confirm the following widely-held and yet previously unproved beliefs that the existence of a feedback system improves the well-being of buyers and enhances their willingness to trade, and it deters dishonest behavior from sellers. Thus with the feedback system, the online C2C auction market as a whole becomes more healthy and attractive to buyers and honest sellers alike. Our findings also confirm that a feedback system does establish a positive correlation between a seller's tendency to cheat and his reputation score; that is, the higher the seller's propensity for cheating, the more likely he will have a high reputation score.

There are interesting findings that may bear implications to real practice: A buyer's willingness to punish illbehaved sellers has a greater impact on the market performances than their willingness to reward wellbehaved sellers. Also, the mere existence of a feedback system, no matter how simple it is, helps to improve the market performance.

We note that there are many viable ways to mathematically model online markets in which feedback systems work, and ours is merely one of them. For instance, in Dellarocas [8], sellers differ not in their cheating propensities but in their efficiencies of delivering quality goods, and also there exists a fee and reward mechanism in the market. Besides leading to the universal conclusion that feedback systems improve performances of markets, the different models inevitably reach conclusions that differ in such subtleties as what the optimal size of a feedback account for each seller should be. We believe, however, that it is out of the scope of the current paper to investigate the extent to which these conclusions hinge upon the specific assumptions as opposed to common features of feedback systems. Future research on feedback systems may shed more light on this issue.

One limitation of this paper is its lack of an explicit theoretical derivation. Even though we believe that there exists some correspondence between the orderings of the buyer score-updating behavior and the orderings of buyer beliefs, due to the complex nature of the underlying problem, we could not tackle it with an explicit solution mathematically. Another limitation is that we rely on the existence of the fuzziness in the decision-making processes to guarantee the repeated game's convergence to a steady state. Although the fuzziness itself has a fairly satisfactory interpretation in real situations, its convergence-guaranteeing threshold has been unpredictable to us.

Further numerical experiments can be conducted based on our existing model. Feedback systems other than the good–bad-comment system can be tested. Different payoff structures and various distribution assumptions suitable for different markets can also be applied and tested under the current model structure.

## Appendix A. Symbols Used in the General Model

$\beta _ { \mathrm { { S } } }$ discount factor per transaction for a seller;

$\beta _ { \mathrm { B } }$ discount factor per transaction for a buyer;

$z$ a seller's prone-to-cheating factor;

$f _ { Z } ( z )$ the distribution function of sellers' types;

$x$ a transaction's size;

$f _ { \mathrm { X } } ( x )$ the distribution function of transaction sizes;

$g _ { \mathrm { S X } } ^ { \mathrm { H } } ( x )$ a seller's gain in a size-x transaction when he plays honestly;

$g _ { \mathrm { B X } } ^ { \mathrm { H } } ( x )$ a buyer's gain in a size-x transaction when his trading partner plays honestly;

$\ g _ { \mathrm { S X Z } } ^ { \mathrm { C } } ( x , z )$ a type-z seller's gain in a size-x transaction when he cheats;

$\ g _ { \mathrm { B X Z } } ^ { \mathrm { C } } ( x , z )$ a buyer's gain in a size-x transaction when his trading partner is of type-z and cheats;

$\mathcal { W }$ the set of all possible scores;

$W$ a generic random score;

w a generic score realization;

$( \boldsymbol { W } ^ { \mathrm { H } } | _ { \mathcal { W } } )$ the random score updated from the initial score w by a buyer whose trading partner has played honestly;

$( W ^ { \mathbf { C } } | \boldsymbol { w } )$ the random score updated from the initial score w by a buyer whose trading partner has cheated;

$f _ { \mathrm { W W } } ^ { \mathrm { H } } ( w , w ^ { \prime } )$ the distribution function for $( \boldsymbol { W } ^ { \mathrm { H } } | _ { \boldsymbol { w } } )$

$f _ { \mathrm { W W } } ^ { \mathrm { C } } ( w , w ^ { \prime } )$ the distribution function for $( \boldsymbol { W } ^ { \mathrm { C } } | \boldsymbol { w } ) ;$

$h _ { \mathrm { B n } } ( \nu )$ a generic history of buyer y in his nth stage game; $H _ { \mathrm { B n } } ( y )$ the set of histories of buyer y in his nth stage game;

$h _ { \mathrm { S n } } ( z )$ a generic history of seller z in his nth stage game;

$H _ { \mathrm { S n } } ( z )$ the set of histories of seller z in his nth stage game;

$p _ { \mathrm { B n } } ^ { \mathrm { P } } ( y , h _ { \mathrm { B n } } ( y ) )$ buyer $y ^ { \star } \mathbf { s }$ probability of proceeding with a trade in his nth stage game when he is with history $h _ { \mathrm { B n } } ( \nu ) ;$

$p _ { \mathrm { S n } } ^ { \mathrm { H } } ( z , \ : h _ { \mathrm { S n } } ( z ) )$ seller z's probability of playing honestly when given the chance to play in his nth game and when he is with history $h _ { \mathrm { S n } } ( z ) ;$

B the buyer strategy profile;

$s$ the seller strategy profile;

$g _ { \mathrm { B } } ( y , B , S )$ buyer y's total discounted expected payoff <sup>SÞ</sup>when buyer strategy profile is and seller strategy profile is $s ;$

$g _ { \mathrm { S } } ( z , B , S )$ seller $z ^ { \prime } \mathrm { s }$ <sup>S</sup>total discounted expected payoff <sup>SÞ</sup>when buyer strategy profile is and seller strategy profile is ;

$f _ { \mathrm { W } } ( \boldsymbol { w } )$ <sup>S</sup> the aggregated distribution of scores;

$f _ { Z | \mathrm { W } } ( z | w )$ the conditional distribution of seller types while the seller's score is given;

$g _ { \mathrm { S Z W } } ( z , w )$ the long-run expected gain for a type-z score-<sup>Þ</sup>w seller right before a transaction starts;

$\overline { { g _ { \mathrm { S X Z W } } ^ { \mathrm { H } } } } ( x , z , w )$ the long-run expected gain for a type-z <sup>Þ</sup>score-w seller in a size-x transaction if he opts to play honestly;

$\bar { g _ { \mathrm { S X Z W } } ^ { \mathrm { C } } }$ x; z; w the long-run expected gain for a type-z <sup>Þ</sup>score-w seller in a size-x transaction if he opts to cheat;

$p _ { \mathrm { S X Z W } } ^ { \mathrm { H } } ( x , z , w )$ the probability that a type-z score-w seller will play honestly in a size-x transaction;

$P _ { \mathrm { S } } ( u )$ the function being used to calculateP P $p _ { \mathrm { S X Z W } } ^ { \mathrm { H } } ( x , z ,$ w) from $\overline { { g _ { \mathrm { S X Z W } } ^ { \mathrm { H } } } } ( x , z , w )$ and $\overline { { g _ { \mathrm { S X Z W } } ^ { \mathrm { C } } } } ( x , z , w )$ ;

$g _ { \mathrm { B X W } } ^ { \mathrm { P } } ( x , w )$ <sup>ð Þ ð Þ</sup>a buyer's average gain while dealing with a score-w seller in a size-x transaction if the buyer proceeds with the transaction;

$p _ { \mathrm { B X W } } ^ { \mathrm { P } } ( x , w )$ the probability that a buyer will proceed with a size-x transaction involving a score-w seller;

$P _ { \mathrm { B } } ( u )$ the function being used to calculate $p _ { \mathrm { B X W } } ^ { \mathrm { P } } ( x , w )$ from $g _ { \mathrm { B X W } } ^ { \mathrm { P } } ( x , w )$ ;

$T _ { \mathrm { W W } | Z } ( w , w ^ { \prime } | z )$ the score transition kernel for a type-z seller after each transaction;

$f _ { \mathrm { W } | Z } ( w | z )$ the conditional distribution of seller scores while the seller's type is given.

Appendices B to D will be available from the authors upon request.

## References

[1] S. Ba, P. Pavlou, Evidence of the effect of trust building technology in electronic markets: price premiums and buyer behavior, MIS Quarterly 26 (3) (2002) 243–268.

[2] Y. Bakos, C. Dellarocas, Cooperation without Enforcement? A comparative analysis of litigation and online reputation quality assurance mechanism, Proceedings of the 23rd International Conference on Information Systems, Barcelona, Spain, Decem ber 15–18, 2002.

[3] P. Battigali, J. Watson, On “reputation” refinements with heterogeneous beliefs, Econometrica 65 (2) (1997) 369–374.

[4] G. Bolton, E. Katok, A. Ockenfels, How effective are online reputation mechanisms? An experimental investigation, Management Science 50 (11) (2004) 1587–1602.

[5] M. Celentani, D. Fudenberg, D.K. Levine, W. Pesendorfer, Maintaining a reputation against a long-lived opponent, Econometrica 64 (3) (1996) 691–704.

[6] M.W. Cripps, J.P. Thomas, Reputation and commitment in twoperson repeated games without discounting, Econometrica 63 (6) (1995) 1401–1419.

[7] C. Dellarocas, The digitization of word-of-mouth: promise and challenges of online reputation mechanisms, Management Science 49 (10) (2003) 1407–1424.

[8] C. Dellarocas, Efficiency through feedback-contingent fees and rewards in auction marketplaces with adverse selection and moral hazard, Proceedings of the 4th ACM Conference on Electronic Commerce, June 9–13, 2003. Association for Computing Machin ery, San Diego, California, USA.

[9] C. Dellarocas, Reputation mechanism design in online trading environments with pure moral hazard, Information Systems Research 16 (2) (2005) 209–230.

[10] eBay's User Agreement, http://pages.ebay.com/help/policies/ user-agreement.html. Available: (2003).

[11] D. Fudenberg, D.K. Levine, Reputation and equilibrium selection in games with a patient player, Econometrica 57 (4) (1989) 759–778.

[12] D. Fudenberg, D.K. Levine, Maintaining a reputation when strategies are imperfectly observed, Review of Economic Studies 59 (3) (1992) 561–579.

[13] D. Fudenberg, J. Tirole, Game Theory, MIT Press, Cambridge, Massachusetts, 1991.

[14] Internet Fraud Watch, http://www.fraud.org/2005\_Internet\_- Fraud\_Report.pdf. Available: (2005).

[15] P. Kollock, The production of trust in online markets, in: E.J. Lawler, M. Macy, S. Thyne, H.A. Walker (Eds.), Advances in Group Processes, vol. 16, JAI Press, Greenwich, Connecticut, 1999, pp. 99–123.

[16] D.M. Kreps, R. Wilson, Reputation and imperfect information, Journal of Economic Theory 27 (2) (1982) 253–279.

[17] P. Milgrom, J. Roberts, Predation, reputation, and entry deterrence, Journal of Economic Theory 27 (2) (1982) 280–312.

[18] N. Miller, P. Resnick, R. Zeckhauser, Eliciting informative feedback: the peer-prediction method, Management Science 51 (9) (2005) 1359–1373.

[19] P. Resnick, R. Zeckhauser, Trust among strangers in internet transactions: empirical analysis of eBay's reputation system, in: M.R. Baye (Ed.), The Economics of the Internet and E-Commerce, Advances in Applied Microeconomics, vol. 11, Elsevier Science, Amsterdam, Holland, 2002.

[20] P. Resnick, R. Zeckhauser, E. Friedman, K. Kuwabara, Reputation systems: facilitating trust in internet interactions, Communications of the ACM 43 (12) (2000) 45–48.

[21] P. Resnick, R. Zeckhauser, J. Swanson, K. Lockwood, The value of reputation on eBay: a controlled experiment, Experimental Economics 9 (2) (2006) 79–101.

[22] M. Shaked, J.G. Shanthikumar, Stochastic Orders and their Applications, Academic Press, Boston, Massachusetts, 1994.

Jian Yang obtained his Ph.D. in Management Science from the University of Texas at Austin in 2000. He is currently an associate professor in the Department of Industrial and Manufacturing Engineering at New Jersey Institute of Technology. His research interest is in the application of operations research techniques to real-life problems emerging from supply chain management, logistics, and electronic commerce. His articles have appeared in Operations Research, Naval Research Logistics, IIE Transactions, European Journal of Operational Research, and others.

Xiaorui Hu is an associate professor of Management Information Systems at the John Cook School of Business, Saint Louis University. She received her Ph.D. in Economics from the University of Texas at Austin. Her research focuses on trust related issues in electronic commerce, business-to-business markets, telecommunication market, and culture impact on international business. She has published in Information Systems Research, Journal of Organizational Computing and Electronic Commerce, IEEE Computer, and other academic journals.

Han Zhang is an associate professor of Information Technology Management at the College of Management, Georgia Institute of Technology. He received his Ph.D. in Information Systems from the University of Texas at Austin in 2000. His research focuses on online trust and reputation related issues, trusted third parties or intermediaries, the evolution of electronic markets, and online payment methods. He has published in Information Systems Research, Journal of Management Information Systems, Decision Support Systems, and other academic journals.
