---
otero_id: 11774
otero_key: "GQHFWFWG"
title: "A novel GSP auction mechanism for ranking Bitcoin transactions in blockchain mining"
authors: "Juanjuan Li; Yong Yuan; Fei-Yue Wang"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113094"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel GSP auction mechanism for ranking Bitcoin transactions in blockchain mining

![](/api/attachments/GQHFWFWG/fulltext/images/cabf6c6b3421c4180d8c752bac705dab15f27c011c38498a4357db7a79b17c7a.jpg)

Juanjuan Li<sup>a,b,c</sup>, Yong Yuan<sup>b,c,\*</sup>, Fei-Yue Wang<sup>b,c</sup>

<sup>a</sup> School of Automation, Beijing Institute of Technology, Beijing 100081, China <sup>b</sup> The State Key Laboratory for Management and Control of Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China <sup>c</sup> Qingdao Academy of Intelligent Industries, Qingdao 266109, China

## A R T I C L E I N F O

Keywords: Blockchain Generalized Second Price auction Transaction fee Quality score Virtual fee

## A B S T R A C T

Bitcoin is gaining ground in recent years. In the Bitcoin system, miners provide computing power to confirm transactions and mine blocks in pursuit of transaction fees, while users compete by bidding transaction fees for faster confirmation. This process is in essence analogous to online ad auctions, where advertisers bid for more prominent ad slots. Therefore, inspired by the Generalized Second Price (GSP) mechanism dominantly used in online ad auctions, we propose to adopt the GSP auction model in the Bitcoin transaction confirmation game. Also, we use weighted fees as the new ranking basis, which can be calculated by user-submitted fees, transaction size, quality scores and virtual fees accumulated from the waiting time. We show that the formulated static GSP transaction fee auction with complete information has a unique Pure Strategy Nash Equilibrium. Then, we discuss the impacts of quality scores and virtual fees on users' equilibrium fee decisions and payofs. Finally, computational experiments are designed to validate our theoretical models and analysis. Our research findings indicate that this novel GSP mechanism is superior to the currently adopted GFP mechanism, and can help users save fees. Besides, quality scores and virtual fees are also proven to be efective on reducing users' paid fees. Moreover, the design of virtual fees allows all transactions to be processed more eficiently in a uniform pipeline, and the interests of transactions with and without associated fees are taken into consideration.

## 1. Introduction

Blockchain technology has attracted intensive research interests and witnessed phenomenal development in recent years [18,22,12], thanks to its desirable features including peer-to-peer decentralization, trustlessness and tamper-resistance [5, 29]. The first and most successful blockchain system so far is widely known as Bitcoin, which creates a multi-billion dollar online economy and opens the new cryptocurrency era [15]. Bitcoin uses the Nakamoto consensus protocol to secure and update its underlying ledger of linked blocks. Typically, new blocks are created via miners repeatedly solving proof-of-work mining puzzles, that is, finding a random number that satisfies specific dificulty requirements using a brute force approach [4]. This process is called mining. The miner who finally wins the consensus competition has the right to confirm his/her packaged transactions and record them into the new block. The new block will then be appended to the main chain of previously agreed blocks, and the miner will get paid the block reward (i.e., 12.5 bitcoins currently) and transaction fees [9, 19].

In this process, transaction fees play the key role as the economic incentive to stimulate miners contributing their computing power so as to confirm transactions [27]. As a result, revenue-maximizing miners will preferentially confirm those transactions with higher fees, forcing Bitcoin users to increase their transaction fees for faster confirmation. or otherwise queue and wait. Since both the block generation rate and the size of Bitcoin blocks are restricted by the predetermined designs, the transaction confirmation rate is also constrained, which forces users to be faced with fierce competition and in turn high required fees if there is a transaction surge.

Therefore, there is a critical need in the individual-level for Bitcoin users to optimize their transaction fees, and also in the system-level for Bitcoin blockchain to improve its transaction ranking mechanism, with the aim of reducing the inflating transaction fees and enhancing the system eficiency. However, several features make this transaction ranking problem unique and challenging. First, transaction fees should be decided by users simultaneously with transaction submissions; and once determined, it is almost impossible for them to adjust any more according to current rules. Second, users are competing for perishable block space rather than storable objects. If no user submits transactions or miners choose to strategically mine an empty new block, the block space will be wasted. Third, unlike in the centralized markets, miners have the right to confirm any group of transactions they like to maximize their revenues, and apparently diferent miners have diferent mining costs. From the research perspective, it is better to model the transaction ranking problem with the game-theoretic analysis [8].

Currently, a large majority of Bitcoin transactions are processed in a pipeline with an order defined by the “rank-by-fee” mechanism, and the payment rule defined by the “pay-its-bid” mechanism, which is known as “Generalized First Price (GFP)” auction. That is, transactions with higher fees usually will be confirmed first and users need to pay their submitted fees. This simple rule will lead users to pay unnecessarily high fees to maintain a desirable ranking for their transactions. Generally, the higher is the required transaction fee, the longer a transaction might reside in the memory pool before being considered dormant [3]. In particular, when the memory pool encounters transaction congestions, users need to pay extra high fees for faster confirmation [16]. For example, in December 2017, the Bitcoin memory pool was stufed with over 180,000 transactions, which leads to severe transaction congestion. Under that situation, users even need to wait for several days to get their transaction confirmed, and the required transaction fee per transaction surpassed 5 dollars <sup>1</sup>. Transaction fees usually account for only a small percentage of the bitcoins transferred by transactions. However, it is possible that transaction fees might reach or even exceed the trading bitcoins, especially in micro-payment scenarios. For this consideration, the exorbitant transaction fees resulting from the GFP mechanism will render the system uneconomical for micro payments [11, 25].

Moreover, the GFP mechanism has been proven to be unstable in many scenarios due to the dynamic environment [7]. It may encourage ineficient investments in gaming the system. Under certain conditions, users will be engaging in cyclical fee adjustments, and equilibrium fees may follow a cyclical pattern with price-escalating phases interrupted by price-collapsing phases [30]. As such, it generates volatile prices that in turn causes allocative ineficiencies. In the Bitcoin system, each block is very likely to be created by diferent miners, and unstable fees cannot guarantee reliable incentives for them to keep mining as well as confirming transactions. As such, the GFP mechanism will lead to ineficiency of managing the transaction confirmation in this perspective.

Due to the aforementioned inherent demerits, the GFP mechanism fails to be a well-applicable auction mechanism for the Bitcoin transaction confirmation game. In this paper, we are motivated to deal with these problems resulting from the currently adopted GFP mechanism in the Bitcoin system. Existing online ad auction practices, especially the sponsored search auctions (SSA), have provided us with good reference models. In the SSA market, advertisers bid for prominent ad slots, which is essentially similar to the auction process of the Bitcoin trans action fee. The GFP mechanism was the original design for SSA since 1998, but has been replaced by the Generalized Second Price (GSP) mechanism in 2002, due to its ineficiency and high volatility shown in the market practice. The GSP mechanism was introduced by Google, and it earns over 90% of its revenues from the keyword auctions based on the GSP mechanism each year. Currently, almost all the online ad auctions, including SSA, real-time bidding and header bidding, etc., adopt the GSP mechanism, and it has created a considerably large global market of about 88 billion dollars in 2017<sup>2</sup>. The GSP mechanism has been proven to be much more user-friendly and less susceptible to gaming, and thus is more stable and has higher allocative eficiency [2]. Inspired by the evolution of the SSA market from the GFP mechanism to the GSP mechanism, we propose to apply the GSP mechanism in the

Bitcoin system. Actually, it can be tailored to the unique characteristics of the Bitcoin transaction fee auction. GSP insists that users ofer a single fee for each transaction; consequently, even though users participate in the multi-objective game, their valuations can be properly represented by one-dimensional types [7]. Diferent from online ad auctions, one fee per transaction can be suficiently expressive to fully convey Bitcoin users' preferences, because they need to independently determine the transaction fee for each transaction.

In the Bitcoin system, active users contribute a lot to maintain the high-quality sustainable development of the system. In practice, accompanied by the number of active users decreasing in 2018, the price of bitcoin dropped, the market size shrunk and miners' revenues decreased<sup>3</sup>. This shows that active users can influence the long-term interests of both the system and miners. Therefore, we should view high of active users. It is reasonable to assume that users having good experience in Bitcoin transactions will participate more frequently. In the SSA market, the user experience improvement is realized through the implementation of a weighted factor named “quality score” since 2008. The quality score is used in ranking ads, in order to ensure that the priority ads are shown in more prominent positions so as to encourage the quality advertising content [28]. Typically, ads with higher quality scores are accompanied with more impressions, better positions, and lower prices. Analogously, we also propose to use quality scores to reward those premium active users, so as to improve their probabilities to get higher ranks or alleviate the pressures of some micro-payment transactions to a certain extent via reducing paid fees.

In practice, transaction fees are not mandatory to Bitcoin transactions. In early stages of Bitcoin, 50KB in each block was reserved for high-priority transactions without fees, and their ranks are mainly determined by the waiting time<sup>4</sup>. That means the transaction confirmations are conducted in two separate pipelines, where the one is for transactions with fees, and the other is for priority transactions without fees. However, as the average transaction size grows, the reserved 50KB becomes insuficient to deal with the confirmation of those priority transactions. Besides, since Bitcoin Core v0.12 was launched, the priority rule was not performed by default any more<sup>5</sup>. Then, some users with priority transactions deviate to submit fees aiming to compete for better ranks in the fee pipeline. If we keep the ranking rule in the fee pipeline regulated uniformly by transaction fees, on the one hand, the priority rule will not work any more, which is not in favor of the priority transactions' benefits; on the other hand, transactions originally with fees are faced with more fierce competition, and those users with low fees will be ranked lower and thus experience longer delay. Therefore, we consider to deal with these two kinds of transactions through one uniform pipeline, and propose a new ranking basis incorporating both transaction fees and the waiting time. Inspired by the coupon designed to compensate customers' waiting time in the serviceproducing process [6], we use the “virtual fee” accumulated from the waiting time to compensate the over-long retention of transactions.

To summarize, our major contribution in this paper is to design a novel GSP auction mechanism for the Bitcoin transaction confirmation game, and also propose a new transaction ranking basis calculated by user-submitted fees, transaction size, quality scores and virtual fees. Also, we analyze the equilibrium of our proposed mechanism, and investigate the impacts of quality scores and virtual fees on users' fee decisions as well as allocative results of the limited block space.

The remainder of this paper is organized as follows. Section 2 briefly reviews the related literature. Section 3 establishes the static GSP auction model for the transaction confirmation game with complete information, and analyzes its pure strategy Nash equilibrium (PSNE). Also, we discuss the influences of quality scores and virtual fees.

Section 4 conducts computational experiments to validate our theore tical models and analysis. Section 5 summarizes this paper and dis cusses the future work.

## 2. Literature review

Currently, the research eforts devoted to understanding the transaction confirmation game in the Bitcoin system are still quite limited. In view that the fixed transaction fee is equivalent to setting a maximum block size instead [8], the auction-based mechanism could be a better choice. However, Lavi et al. [13] argued that Bitcoin's current fee market based on the GFP auction does not extract revenue well for miners when blocks are not congested. Also, according to Houy [8], if transaction fees are totally determined by a decentralized market and the maximum block size is not constrained, transaction fees will eventually go to zero and miners will not have the suficient incentives to keep mining, and hence to keep Bitcoin viable. Huberman et al. [9] analyzed the implied congestion queueing game, calculated each user's trade-of between transaction fees and delay costs, and concluded that each user's equilibrium transaction fee equals the externality imposed by his/her transaction. Thus, equilibrium transaction fees coincide with the payments that result from selling the priority of service in a VCG (Vickrey-Clarke-Groves) auction. Lavi et al. [13] proposed two alternative auction mechanisms: the monopolistic price mechanism, and the random sampling optimal price mechanism. They proved that the monopolistic price mechanism extracts revenue better from users, and that it is nearly incentive compatible.

In the theoretical research, multiple advantages of the GSP me chanism have already been documented. Conceived as a natural extension of the Vickrey-Clarke-Groves (VCG) auction, GSP allows bidders to pay at the minimum price that can maintain the current rank [10]. The first economic analysis of GSP is formulated by Edelman et al. [7] and Varian [23], and they proposed the Locally Envy-Free Equilibrium and the Symmetric Nash Equilibrium for the GSP auction with complete information, respectively. In both equilibria, bidders' positions and payments are equal to the counterparts in the dominant-strategy equilibrium of VCG auctions, respectively. However, the multi-object GSP auction lacks some desirable properties of the VCG auctions. In particular, the GSP mechanism proves to be not incentive compatible, and truth-telling is not an equilibrium strategy [23]. VCG is a more theoretically efective mechanism encouraging bidders to bid their true valuations. Sano [21] categorized the complete-information Nash Equilibrium in a much more general setting, and pointed out that every Vickrey-reserve auction has the same Nash equilibrium in the core. However, VCG is very hard to use in practice due to its high computing complexity, especially for the multi-object auction scenarios [1]. As such, GSP surpasses VCG to become the mainstream auction mechanism in practice.

Considering the good applicability of the GSP mechanism to the Bitcoin transaction confirmation game, as well as its advantages proven in both theoretical researches and online auction practices, we believe that employing the GSP auction model to replace the currently adopted GFP auction model is a timely and meaningful research innovation. In the following sections, we will establish the GSP model for Bitcoin transaction fee auctions, and also analyze users' equilibrium decisions on transaction fees.

## 3. The GSP auction model in transaction confirmation games

## 3.1. The basic model

The GSP auction process of Bitcoin transactions can be briefly described by Fig. 1. First, new transactions pending for confirmation with associated fees are submitted by users, and they will enter the memory pool. Then, miners scan the relevant information of these unconfirmed transactions, and select a group of preferred transactions ranked in top positions as their mining basis. In this paper, we use weighted fees to determine transactions' ranks, which can be calculated by user-sub mitted fees, transaction size, quality scores and also virtual fees accumulated from the waiting time. The miner who successfully digs out the new block wins the right to confirm the packaged transactions and record them into the new block. Correspondingly, the confirmed transactions should transfer a certain amount of fees to miners, which are equal to the next highest fee under the GSP mechanism.

In this paper, we focus on analyzing the static GSP auction on Bitcoin transaction confirmation. In the Bitcoin system, all information regarding each transaction will be broadcasted in public as soon as it is submitted, which includes size, fee, input amount, output amount, address, and submission time, etc. After each block is mined, we are free to access the information of confirmed transactions in the block, which means the auction results are public information. Besides, Bitcoin transactions are basically transfer transactions; thus it is natural to use the transfer amount to represent the transaction's value to the user. As the transfer amount is public information, we can then consider that the transaction's value is also public information. As such, we study the Bitcoin transaction confirmation game in the complete-information setting. Notations of this paper are listed in Table 1.

We consider that there is only one public memory pool for all miners in the Bitcoin system. In the memory pool, the transaction submission rate is assumed to exceed the transaction confirmation rate; otherwise there might be no user willing to submit fees for their transaction confirmation.

Suppose there are n risk-neutral users from the set $N = \{ 1 , 2 , . . . , n \}$ and each user submits only one transaction pending for confirmation. Let $\nu _ { i }$ denote user i’s valuation on his/her transaction. As mentioned above, we use the weighted fee $b _ { i } ^ { ' }$ calculated by compound factors to rank these transactions, including the transaction fee $b _ { i } ,$ the block size $s _  i , $ the quality score $q _ { i }$ and the virtual fee $w _ { i } .$

Usually, the user submits a transaction with an associated fee $b _ { i } \geq 0 ,$ indicating the maximum price that he/she is willing to transfer to miners for their confirmation service. Notice that, the fee $b _ { i }$ doesn’t need to be the same as his/her true valuation $\nu _ { i } ,$ and normally we have $b _ { i } \leq \nu _ { i }$ to consider that all users are conservative [14]. Users rely on submitting fees to get their transactions ranked in desired orders, which will help them shorten the waiting time in the transaction confirmation. Besides, users are asymmetric with diferent transaction size $s _ { i \cdot }$ In the Bitcoin system. each block has the upper-limit, and transactions with larger size take up more block space and thus restrict the number of transactions that can be recorded into each block. As such, we also view the transaction size as an important factor to formulate the transaction ranking basis.

In online ad auctions, the quality score is closely correlated to the click-through-rate of ads, which is used to evaluate the quality advertisements [28]. Inspired by this, we here determine quality scores mainly by the historical transaction frequency $h _ { i }$ and the cumulative paid fees $\alpha _ { i s }$ which can represent users' contributions to maintain a sustainable Bitcoin system. The historical transaction frequency is used to evaluate the user's vitality, and more frequent transactions indicate higher user vitality, which is good for the system's sustainability. The cumulative paid fees represent the users' capability to provide economic incentives for miners to ensure the necessary security and stability of the system. In general, a higher quality score will lead to a better rank as well as a lower paid fee. Besides, we propose to define the virtual fee $\boldsymbol { z } _ { i }$ by the waiting time w of each transaction. Generally, the longer is the waiting time, the higher is the virtual fee. Without loss of generality, we do not give the detailed formulations of quality scores and virtual fees. However, diferent formulations can be established according to the specific design targets, and they will not influence the correctness of the following analysis.

Based on the above discussions, we first assign each user with a number i according to the descending order of their weighted valuations $\nu _ { i } \overset { \prime } { _ { i } }$ , that is, $\nu _ { 1 } ^ { ' } > \nu _ { 2 } ^ { ' } , . . . , > \nu _ { n }$ , where we establish

![](/api/attachments/GQHFWFWG/fulltext/images/020a17702daf50af057f30f5a59735d91e8e294ce1a625319110afd342f905e3.jpg)  
Fig. 1. The basic process of the Bitcoin transaction confirmation.

$$
v _ {i} ^ {\prime} = \frac {q _ {i} (v _ {i} + z _ {i})}{s _ {i}}.\tag{1}
$$

Similarly, the user's weighted fee ${ b _ { i } } ^ { ' }$ is then formulated by the following function

$$
b _ {i} ^ {\prime} = \frac {q _ {i} (b _ {i} + z _ {i})}{s _ {i}}.\tag{2}
$$

In the game, we sort b<sup>′</sup> by the descending order to get $b _ { 1 } ^ { ' } \geq . . . b _ { j } ^ { ' } \geq . . . \geq$ $b _ { n } ,$ that is, the higher weighted fee corresponds to the higher rank. Let j be the user i’s rank. Miners confirm transactions according to the rank until the upcoming new block is filled up. If there exist users having the same weighted fees, we assign them the same rank and determine their transaction confirmation orders randomly.

Bitcoin users usually pay close attention to whether their transactions can be confirmed and recorded into the upcoming new block. Let S be the block size, the user i satisfying the following condition will naturally get his/her transaction confirmed, and we call him/her “full winner”.

$$
\sum_ {k = 0} ^ {j _ {i}} s _ {k} \leq S\tag{3}
$$

Also, the user i is defined as “partial winner”, if he/she satisfies the following condition

$$
\sum_ {k = 0} ^ {j _ {i} - 1} s _ {k} <   S <   \sum_ {k = 0} ^ {j _ {i}} s _ {k}.\tag{4}
$$

## Table 1

Under the GSP mechanism, users generally pay miners at the prices that can just maintain their current ranks, and only winners need to pay. As such, the user i’s payment is

Obviously, we have $\begin{array} { r } { 0 < ( S - \sum _ { k = 0 } ^ { j _ { i } - 1 } s _ { k } ) / s _ { j _ { i } } < 1 . } \end{array}$

$$
\theta_ {i} = \left\{ \begin{array}{c c} 1, & \text {if} \sum_ {k = 0} ^ {j _ {i}} s _ {k} \leq S \\ \frac {S - \sum_ {k = 0} ^ {j _ {i} - 1} s _ {k}}{s _ {j _ {i}}}, & \text {if} \sum_ {k = 0} ^ {j _ {i} - 1} s _ {k} <   S <   \sum_ {k = 0} ^ {j _ {i}} s _ {k} \\ 0, & \text {if} \sum_ {k = 0} ^ {j _ {i} - 1} s _ {k} \geq S \end{array} \right.\tag{6}
$$

In this case, the user also has a certain chance to get his/her transaction confirmed, because he/she can alternatively utilize the Segregated Witness (Segwit) to reduce the transaction size. Segwit is implemented by splitting the transaction into two segments, removing the unlocking signature (“witness” data) from the original portion and appending it as a separate structure at the end. However, we also consider the discounted payof of the partial winner to identify its diference from full winners [26], and the discount factor is established as:

It is easy to find that there is at most one partial winner in the game. Based on the above consideration, we formulate the user i’s discount factor $\theta _ { i }$ as follows.

$$
\theta_ {i} = \frac {S - \sum_ {k = 0} ^ {j _ {i} - 1} s _ {k}}{s _ {j _ {i}}}.\tag{5}
$$

List of notations.

<table><tr><td>Notations</td><td>Definitions</td><td>Notations</td><td>Definitions</td></tr><tr><td> $n$ </td><td>The number of users</td><td> $N$ </td><td>The user  $i$ &#x27;s valuation on the transaction</td></tr><tr><td> $b_i$ </td><td>The user  $i$ &#x27;s submitted fee</td><td> $b_i'$ </td><td>The user  $i$ &#x27;s weighted fee</td></tr><tr><td> $s_i$ </td><td>The user  $i$ &#x27;s transaction size</td><td> $q_i$ </td><td>The user  $i$ &#x27;s quality score</td></tr><tr><td> $w_i$ </td><td>The waiting time of user  $i$ &#x27;s transaction</td><td> $z_i$ </td><td>The user  $i$ &#x27;s virtual fee</td></tr><tr><td> $v_i'$ </td><td>The user  $i$ &#x27;s weighted valuation</td><td> $j_i$ </td><td>The user  $i$ &#x27;s rank in the uniform game</td></tr><tr><td> $p_i'$ </td><td>The user  $i$ &#x27;s payment in the uniform game</td><td> $u_i$ </td><td>The user  $i$ &#x27;s payoff in the uniform game</td></tr><tr><td> $S$ </td><td>The block size</td><td> $\theta_i$ </td><td>The user  $i$ &#x27;s discount factor in the uniform game with quality scores</td></tr><tr><td> $\gamma_i$ </td><td>The user  $i$ &#x27;s threshold fee</td><td> $\Gamma$ </td><td>The threshold weighted fee in the uniform game</td></tr><tr><td> $B_i$ </td><td>The user  $i$ &#x27;s minimal threshold fee</td><td> $\lambda_i$ </td><td>The user  $i$ &#x27;s discount factor in the uniform game without quality scores</td></tr><tr><td> $U_i^t$ </td><td>The user  $i$ &#x27;s farsighted payoff at time  $t$ </td><td> $q_i^t$ </td><td>The user  $i$ &#x27;s quality score at time  $t$ </td></tr><tr><td> $j_i^{1}$ </td><td>The user  $i$ &#x27;s rank in the separate game-1</td><td> $\lambda_i^{1}$ </td><td>The user  $i$ &#x27;s discount factor in the separate game-1</td></tr><tr><td> $j_i^{2}$ </td><td>The user  $i$ &#x27;s rank in the separate game-2</td><td> $\theta_i^{2}$ </td><td>The user  $i$ &#x27;s discount factor in the separate game-2</td></tr><tr><td> $p_i^{2'}$ </td><td>The user  $i$ &#x27;s payment in the separate game-2</td><td> $u_i^{2}$ </td><td>The user  $i$ &#x27;s payoff in the separate game-2</td></tr></table>

$$
p _ {i} ^ {\prime} = \left\{ \begin{array}{c c c} \frac {b _ {j _ {i} + 1} ^ {\prime} s _ {i}}{q _ {i}} - z _ {i} + \varepsilon , & \text {if} & 0 <   \theta_ {i} \leq 1 \\ 0, & \text {if} & \theta_ {i} = 0 \end{array} \right.\tag{7}
$$

Here, $\varepsilon$ is the minimum increment. In general, we have $p _ { i } ^ { ' } \geq ~ 0$ Furthermore, we calculate the user $i \gamma _ { s }$ payof by his/her transaction's discounted net value, that is

$$
u _ {i} = \theta_ {i} (v _ {i} - p _ {i} ^ {\prime}).\tag{8}
$$

## 3.2. Equilibrium analysis

In this section, we focus on analyzing Bitcoin users' equilibrium fee decisions in our formulated static GSP auction with complete in formation.

In the Bitcoin system, users should submit the deterministic fees and be unable to make further adjustments on submitted fees. It is dificult for them to pick a distribution over multiple fee strategies (i.e., a mixed strategy). As such, we care more about whether the pure strategy equilibrium exists in the aforementioned game.

Let $b _ { i } ^ { * }$ be the equilibrium fee of user i and $b _ { - i } ^ { * }$ be the equilibrium fee of his/her competitors. Supposing the game has a PSNE, we can derive the following condition:

$$
u _ {i} (b _ {i} ^ {*}, b _ {- i} ^ {*}) \geq u _ {i} (b _ {i}, b _ {- i} ^ {*}), \forall i \in N,\tag{9}
$$

which is equivalent to

$$
u _ {i} (b _ {i} ^ {\prime *}, b _ {- i} ^ {\prime *}) \geq u _ {i} (b _ {i} ^ {\prime}, b _ {- i} ^ {\prime *}), \forall   i \in N.\tag{10}
$$

Lemma 1. Under the PSNE, if there is $\theta _ { i } = \theta ,$ there must $b e b _ { i } ^ { * } = \nu _ { i }$

Proof. Submitting a fee exceeding the true valuation, i.e, $b _ { i } > \nu _ { i } ,$ , is not the feasible choice for the conservative users. Therefore, there must be $b _ { i } ^ { * } \leq \nu _ { i }$

Accordingly, suppose $b _ { i } ^ { * } \neq \nu _ { i } ,$ there $\mathrm { i s } \qquad b _ { i } ^ { * } < \nu _ { i } .$ Let $\zeta = \mathrm { m i n } \{ b _ { i } | \theta ( b _ { i } ) > 0 \}$ , and because $\theta ( b _ { i } ^ { * } ) = 0 .$ , we obtain $b _ { i } ^ { * } < \zeta .$ . If $b _ { i } ^ { * } < \nu _ { i } < \zeta ,$ we obtain $u _ { i } ( b _ { i } ^ { * } , b _ { - i } ^ { * } ) = u _ { i } ( \nu _ { i } , b _ { - i } ^ { * } ) ;$ and if $b _ { i } ^ { * } < \zeta \leq \nu _ { i } ,$ we obtain $u _ { i } ( b _ { i } ^ { * } , b _ { - i } ^ { * } ) < u _ { i } ( \nu _ { i } , b _ { - i } ^ { * } )$ Consequently, there is $u _ { i } ( b _ { i } ^ { * } , b _ { - i } ^ { * } ) \leq u _ { i } ( \nu _ { i } , b _ { - i } ^ { * } )$ under the case of $b _ { i } ^ { * } \neq \nu _ { i } ,$ , which is contradictory with the aforementioned condition of PSNE.

$$
0 <   \theta_ {i} \leq 1,
$$

$$
<   v _ {i}
$$

Proof. First, we discuss the case of $\theta _ { i } = 1$ . Let $\delta = \operatorname* { m a x } \{ b _ { i } | \theta ( b _ { i } ) < 1 \}$ and because $\theta ( b _ { i } ^ { * } ) = 1$ we have $b _ { i } ^ { * } > \delta .$ . Suppose $b _ { i } ^ { * } > \nu _ { i } , \mathrm { i f } b _ { i } ^ { * } > \nu _ { i } > \delta ,$ submitting the fee equal to the valuation, i.e, $b _ { i } ^ { * } = \nu _ { i } ,$ , is a better choice; and if $b _ { i } ^ { * } > \delta \geq \nu _ { i } .$ , we have $u _ { i } ( b _ { i } ^ { * } , b _ { - i } ^ { * } ) < 0 ,$ , which is contrary to individual rationality. Therefore, there must be $b _ { i } ^ { * } \leq \nu _ { i } .$

Next, we suppose the condition of $b _ { i } ^ { * } = \nu _ { i }$ holds to conduct the fol. lowing analysis. Under the PSNE, there is $b _ { j _ { i } ^ { * } + 1 } ^ { \prime } < { b _ { i } ^ { \prime } } ^ { * }$ , where $j _ { i } ^ { * }$ is the transaction's rank under the fee $b _ { i } ^ { * }$ . Then, we obtain

$$
b _ {i} ^ {*} > \frac {b _ {j _ {i} ^ {*} + 1} ^ {\prime} s _ {i}}{q _ {i}} - z _ {i}.
$$

Submitting a lower alternative fee $\widehat { b } _ { i }$ can guarantee the user to maintain the current rank ${ j _ { i } ^ { * } } ,$ that is

$$
\hat {b} _ {i} \in \left(\frac {b _ {j _ {i} ^ {*} + 1} ^ {\prime} s _ {i}}{q _ {i}} - z _ {i}, v _ {i}\right)
$$

Therefore, there must be $b _ { i } ^ { * } < \nu _ { i } .$

Then, we discuss the case of $0 < \theta _ { i } < 1$ . Let $\delta = \operatorname* { m a x } \{ b _ { i } | \theta ( b _ { i } ) = 0 \}$ we will have $b _ { i } ^ { * } > \delta$ . Similar with the case of $\theta _ { i } = 1$ , we can easily prove $b _ { i } ^ { * } < \nu _ { i }$

To conclude, Lemma 1 indicates that users losing the game must have equilibrium fees equal to their valuations; while Lemma 2 shows that winners in the game must have equilibrium fees less than their valuations.

Lemma 3. Under the PSNE, the full winner cannot improve the payof through submitting a higher fee; while the partial winner cannot improve the payof through submitting a lower fee.

Proof. For the full user with $\theta _ { i } = 1 _ { : }$ , a higher fee will not change $\theta _ { i \cdot }$ Therefore, his/her payof cannot be improved through submitting a higher fee.

For the partial user with $\begin{array} { r } { \theta _ { i } = ( S - \sum _ { k = 0 } ^ { j _ { i } - 1 } s _ { k } ) / s _ { j _ { i } } , } \end{array}$ a lower fee will lead to an unchanged or lower rank. $\mathbb { f } \ j _ { i }$ stays unchanged, then ${ . p _ { i } }$ and $\theta _ { i }$ stay unchanged, thus the payof will not change. If the lower fee makes $j _ { i }$ become lower to zero, then the payof will be zero too. As such, his/her payof cannot be improved through submitting a lower fee.

Theorem 4. There exists a unique PSNE in our formulated static GSP game with complete information, which $i s b ^ { * } = ( b _ { i ( \theta _ { i } = 0 ) } = \nu _ { i } , b _ { i ( \theta _ { i } = 1 ) } = B _ { i } , b _ { i ( 0 < \theta _ { i } < 1 ) } = B _ { i } - \varepsilon )$

Proof. Following the above assumption that the transaction submission rate exceeds the transaction confirmation rate, there must exist users who fail to get their transactions confirmed. According to Lemma 1, these users with $\theta = 0$ have the equilibrium strategy as $\boldsymbol { b } ^ { * } = \boldsymbol \nu .$ Then, we focus on discussing users with $0 < \theta \leq 1$ in what follows.

Considering that all users submit fees equal to their true valuations, there is

$$
\bar {v} _ {j _ {i} + 1} = \frac {v _ {j _ {i} + 1} ^ {\prime} s _ {i}}{q _ {i}} - z _ {i},
$$

where

$$
v _ {j _ {i} + 1} ^ {\prime} = \frac {q _ {j _ {i} + 1} (v _ {j _ {i} + 1} + z _ {j _ {i} + 1})}{s _ {j _ {i} + 1}}.
$$

Accordingly, the user i’s fee will be in the interval $( { \bar { \nu } } _ { j _ { i } + 1 } , \nu _ { i } ] ,$

For the user submitting the true valuation to be a winner, if there exists $\gamma _ { i } \in ( \bar { \nu } _ { j _ { i } + 1 }$ , ]v to obtain the following equation, we define it as the threshold fee for the user.

$$
\begin{array}{l} \theta (1) _ {i} (v _ {i} - (\bar {v} _ {j _ {i} + 1} + \varepsilon)) = \theta (2) _ {i} (v _ {i} - \gamma_ {i}) \\ \text { Here } \qquad \theta (1) _ {i} = g (\gamma_ {i} - \varepsilon | b _ {- i} = \gamma_ {- i}, v _ {- i} > \gamma_ {- i}), \qquad \text { and } \qquad \theta (2) _ {i} = g \\ (\gamma_ {i} | b _ {- i} = \gamma_ {- i} - \varepsilon , v _ {- i} > \gamma_ {- i}), \text { where } \\ \gamma_ {- i} = \frac {(\gamma_ {i} + z _ {i}) q _ {i} s _ {- i}}{s _ {i} q _ {- i}} - z _ {- i}, \end{array}
$$

and − i represents the user's competitors. From above, we have $0 < \theta ( 1 ) _ { i } < 1 ,$ , and $\theta ( 2 ) _ { i } = 1$

If $: 1 < j _ { i } \le m ,$ we have

$$
\begin{array}{l} \theta (1) _ {i} (v _ {i} - (\bar {v} _ {j _ {i} + 1} + \varepsilon)) = \theta (2) _ {i} (v _ {i} - \gamma_ {i}). \\ \text { Accordingly, } \\ \gamma_ {i} = (1 - \theta (1) _ {i}) v _ {i} + \theta (1) _ {i} (\bar {v} _ {j _ {i} + 1} + \varepsilon). \end{array}
$$

Because $\nu _ { i } > \bar { \nu } _ { j _ { i } + 1 } + \varepsilon ,$ we then obtain $\bar { \nu } _ { j _ { i } + 1 } < \gamma _ { i } < \nu _ { i } .$

I ${ \textsf { f } } j _ { i } = 1 ,$ , there must be $\theta = 1$ according to the Bitcoin system's practice. Then, the user can adjust the fee to be $b _ { i } \in ( \bar { \nu } _ { x + 1 } , \nu _ { x } ] , x > i , x \in N$ , aiming to get $0 < \theta _ { i } < 1$ . Then, we can also get the threshold fee $\gamma _ { i } ,$ following the aforementioned analysis process.

The above discussions have proven the existence of $\gamma _ { i }$ for the user submitting the true valuation to be the full winner or partial winner. Furthermore, we establish the threshold weighted fee Γ of the game as follows.

$$
\Gamma = \min _ {i \in N} \left(\frac {q _ {i} (\gamma_ {i} + z _ {i})}{s _ {i}} \Big | 0 <   \theta_ {i} \leq 1\right).
$$

Then, we define B to represent the user i’s individual minimal threshold fee, where

$$
B _ {i} = \frac {\Gamma s _ {i}}{q _ {i}} - z _ {i}.
$$

For the full winner with $\theta _ { i } = 1$ , a fee higher than B is not desirable according to Lemma $^ { 3 , }$ and a fee lower than $B _ { i }$ leads to $\theta _ { i } < 1$ and will not generate a higher payof. Therefore, B<sub>i</sub> is the equilibrium fee for the full winner. For the partial winner with $0 < \theta _ { i } < 1$ , a fee higher than $B _ { i } - \varepsilon$ will not generate a higher payof according to the above analysis, and a fee lower than $B _ { i } - \varepsilon$ makes the user lose the game. Therefore, $B _ { i } - \varepsilon$ is the equilibrium fee for the partial winner.

As such, we can conclude that our formulated static GSP game with complete information in the Bitcoin system has the PSNE of $b ^ { * } = ( b _ { i ( \theta _ { i } = 0 ) } = \nu _ { i } , b _ { i ( \theta _ { i } = 1 ) } = B _ { i } , b _ { i ( 0 < \theta _ { i } < 1 ) } = B _ { i } - \varepsilon ) .$

Considering there exists another PSNE $\ddot { b } \neq b ^ { * }$ , under which the user $j \neq i$ with $\theta _ { j } \in ( 0 , 1 ]$ has the minimal threshold fee as $B _ { k } .$ Then, there wil be $B _ { k } \ \geq \ B _ { i } .$ Under $B _ { k } ,$ the user i will get $\theta _ { i } = 1$ , and win the payof as $\ddot { \mathrm { u } } _ { i } = \nu _ { i } - B _ { k }$

We have $\ddot { \mathrm { u } } _ { i } \le u _ { i } ^ { * }$ , where $u _ { i } ^ { * } = \nu _ { i } - B _ { i }$ . Accordingly, the user has the incentive to change the fee to get a higher payof under the equilibrium profile b. Therefore, there does not exist another PSNE. That $\mathrm { i } s , b ^ { * }$ is the unique PSNE of the game.

## 3.3. Quality scores

In this section, we aim to investigate the influence of quality scores on users' fee decisions and payofs in the uniform transaction con firmation game played by all n users, through comparative analysis of the case without considering quality scores.

In the uniform game without quality scores, we consider $q _ { i } = 1 ( \forall i \in$ N) to calculate the threshold fee $\gamma _ { i } ,$ and obtain

$$
\Gamma = \min _ {i \in N} (\frac {\gamma_ {i} + z _ {i}}{s _ {i}} | 0 <   \lambda_ {i} \leq 1),\tag{11}
$$

where $\lambda _ { i }$ is the discount factor in the uniform game without quality scores. Then, we establish the user's payof function as

$$
u _ {i} = \lambda_ {i} (v _ {i} - p _ {i}),\tag{12}
$$

where, we have

$$
p _ {i} = b _ {j _ {i} + 1} ^ {\prime} s _ {i} - z _ {i} + \varepsilon\tag{13}
$$

For simplicity, we suppose all users have the same waiting time of 0 and the same transaction size of 1 to conduct the following analysis. Similar to the equilibrium analysis in Section 3.2, we can then derive the equilibria under the uniform game with and without quality scores as shown in Table 2.

Proposition 5. For the user with $\lambda _ { i } = 0 ,$ a high quality score will not encourage him/her to submit a higher fee, but may improve his/her payof.

Proof. In the uniform game without quality scores, the user with $\lambda _ { i } = 0$ fails to get the transaction confirmed, and does not need to pay. Following the discussions in Section 3.2, there is $\nu _ { i } < \Gamma - \varepsilon$ for the user.

Introducing quality scores into the uniform game, if a high quality score leads to $B _ { i } - \varepsilon < \nu _ { i } < \Gamma - \varepsilon ,$ the user can submit a fee lower than the true valuation to get a payof exceeding 0, but he/she needs to transfer a certain payment to miners.

Under the case of $\Gamma - \varepsilon \leq B _ { i } ,$ there is $\nu _ { i } < B _ { i } .$ . Because $b _ { i } \leq \nu _ { i } ,$ the user cannot aford the fee $B _ { i } .$ . As such, the user will submit a lower fee

Table 2  
Equilibria in the uniform game without and with quality scores.

<table><tr><td>Uniform game</td><td>Discount factor</td><td>Equilibrium fee</td><td>Payoff</td></tr><tr><td rowspan="3">Without quality scores</td><td>1</td><td> $\Gamma$ </td><td> $v_i - \Gamma$ </td></tr><tr><td> $S - (j_i - 1)$ </td><td> $\Gamma - \varepsilon$ </td><td> $[S - (j_i - 1)](v_i - p_i)$ </td></tr><tr><td>0</td><td> $v_i$ </td><td>0</td></tr><tr><td rowspan="3">With quality scores</td><td>1</td><td> $B_i$ </td><td> $v_i - B_i$ </td></tr><tr><td> $S - (j_i - 1)$ </td><td> $B_i - \varepsilon$ </td><td> $[S - (j_i - 1)](v_i - p_i')$ </td></tr><tr><td>0</td><td> $v_i$ </td><td>0</td></tr></table>

$B _ { i } - \varepsilon$ so as to be a partial winner, and get the corresponding payof $[ S - ( j _ { i } - 1 ) ] ( \nu _ { i } - p _ { i } ^ { ' } )$

Under the case of $\Gamma - \varepsilon > B _ { i } , \mathrm { i f } \nu _ { i } \le B _ { i } \nonumber$ , the user will reduce the fee to $\boldsymbol { B } _ { i } - \boldsymbol \varepsilon { } ;$ and if $\nu _ { i } > B _ { i } ,$ the user can reduce the fee to $B _ { i } - \varepsilon \mathrm { o r } B _ { i } ,$ and the payof of the latter case is $\nu _ { i } - B _ { i }$

If $\nu _ { i } \leq B _ { i } - \varepsilon ,$ there is no incentive for the user to change the fee, because a higher fee is not afordable while a lower fee cannot generate a higher payof.

Proposition 6. For the users with $\lambda _ { i } > 0 , $ a low quality score may encourage him/her to submit a higher fee, and will reduce his/her payof.

Proof. In the uniform game without quality scores, if the user submits the fee $\Gamma - \varepsilon$ to be a partial winner, there is $\nu _ { i } > \Gamma - \varepsilon .$

Introducing quality scores into the game, if $\begin{array} { r } { \Gamma - \varepsilon < \nu _ { i } < B _ { i } - \varepsilon , } \end{array}$ , the user cannot aford the fee $B _ { i } - \varepsilon .$ . Hence, he/she will increase the fee to be equal to his/her valuation $\nu _ { i } ,$ and then get the payof equal to 0.

If $\nu _ { i } \geq B _ { i } - \varepsilon ,$ a fee equal to the true valuation will not be the user's most beneficial choice. Under this situation, if

$$
v _ {i} <   \frac {B _ {i} - [ S - (j _ {i} - 1) ] p _ {i} ^ {\prime}}{1 - [ S - (j _ {i} - 1) ]},
$$

the user will deviate from the equilibrium fee in the uniform game without quality scores, and submit the fee $B _ { i } - \varepsilon$ to be a partial winner. Alternatively, if

$$
v _ {i} \geq \frac {B _ {i} - [ S - (j _ {i} - 1) ] p _ {i} ^ {\prime}}{1 - [ S - (j _ {i} - 1) ]},
$$

the user will submit the fee $B _ { i }$ to be a full winner.

Similarly, for the user submitting the fee Γ to get $\lambda _ { i } = 1$ in the uniform game without quality scores, if a low q produces $\begin{array} { r } { \Gamma < \nu _ { i } < B _ { i } - \varepsilon , } \end{array}$ he/she will raise the fee to v and get the payof equal to 0; otherwise, the user will submit the $\begin{array} { r l } { { \sf f e e } } & { { } \ B _ { i } - \varepsilon } \end{array}$ if $\nu _ { i } < ( B _ { i } - [ S - ( j _ { i } - 1 ) ] p _ { i } ^ { ' } ) / ( 1 - [ S - ( j _ { i } - 1 ) ] )$ and submit the fee B if $\nu _ { i } \ge ( B _ { i } - [ S - ( j _ { i } - 1 ) ] p _ { i } ^ { \prime } ) / ( 1 - [ S - ( j _ { i } - 1 ) ] )$

As follows, we make a simple extension to consider a farsighted user who realizes that current quality score can influence the follow-up game. In view of this, we consider that the user's fee decision not only depends on the net value in the current transaction confirmation game, but also on the generated quality score. Accordingly, we establish the extended payof function of the farsighted user as follows.

$$
\begin{array}{r l r} {U _ {i} ^ {t}} & = & {u _ {i} ^ {t} + \delta q _ {i} ^ {t}} \\ & = & {\theta_ {i} ^ {t} (v _ {i} ^ {t} - p _ {i} ^ {\prime t}) + \delta q _ {i} ^ {t},} \end{array}\tag{14}
$$

where δ is the weighted coeficient. Here, $q _ { i } ^ { t - 1 }$ has already been determined by the previous game at time $t - 1$ . Inspired by the quality score formulation in online ad auctions [28], we formulate the following function to calculate the user i’s quality score at time t as an example,

$$
q _ {i} ^ {t} = \frac {q _ {i} ^ {t - 1} h _ {i} ^ {t} (\alpha_ {i} ^ {t - 1} + p _ {i} ^ {\prime t})}{h _ {i} ^ {t - 1} \alpha_ {i} ^ {t - 1}}\tag{15}
$$

For this formulation, we have $\mathrm { d } q _ { i } ^ { t } / \mathrm { d } t \geq 0$ and $\mathrm { d } ^ { 2 } q _ { i } ^ { t } / \mathrm { d } t ^ { 2 } \leq 0 .$

Supposing that transaction confirmation games are independent over time, we obtain

$$
q _ {i} ^ {t} = \frac {q _ {i} ^ {t - 1} (h _ {i} ^ {t - 1} + \theta_ {i} ^ {t}) (\alpha_ {i} ^ {t - 1} + \theta_ {i} ^ {t} p _ {i} ^ {' t})}{h _ {i} ^ {t - 1} \alpha_ {i} ^ {t - 1}},\tag{16}
$$

$$
b _ {i} ^ {\prime t} = \frac {q _ {i} ^ {t - 1} (b _ {i} ^ {t} + z _ {i} ^ {t})}{s _ {i} ^ {t}}.\tag{17}
$$

Theorem 7. If the uniform game with quality scores has all users to farsightedly maximize the payofU<sup>t</sup> shown in Eq. (14), it will not cause users to submit lower fees compared to that under the payof u described by Eq (8).

Proof. When there is $b _ { i } ^ { * } = B _ { i }$ in the original uniform game with the payof function $u _ { i } ,$ the user does not have the motivation to ofer a diferent fee in the extended uniform game with the payof function $U _ { i } ^ { t }$ Because compared with the fee $b _ { i } ^ { t } = B _ { i } ,$ a higher fee cannot generate a higher $u _ { i } ^ { t }$ or a higher $\boldsymbol q _ { i } ^ { t } ;$ , while a lower fee will result in a lower $u _ { i } ^ { t }$ as well as a lower $q _ { i } ^ { t } .$

When there is $b _ { i } ^ { * } = B _ { i } - \varepsilon$ in the original uniform game, the user will not be willing to ofer a lower fee in the extended uniform game, since the fee b<sup>t</sup> lower than $B _ { i } - \varepsilon$ not only results in $u _ { i } ^ { t } = 0$ but also produces a lower $q _ { i } ^ { t }$ . If the user keeps to submit the fee $B _ { i } - \varepsilon ,$ he/she will get the payof as

$$
U _ {i} ^ {t} = \theta_ {i} ^ {t} [ v _ {i} ^ {t} - p _ {i} ^ {\prime t} (q _ {i} ^ {t - 1}) ] + \delta q _ {i} ^ {t},
$$

where,

$$
q _ {i} ^ {t} = \frac {q _ {i} ^ {t - 1} (h _ {i} ^ {t - 1} + \theta_ {i} ^ {t}) (\alpha_ {i} ^ {t - 1} + \theta_ {i} ^ {t} p _ {i} ^ {\prime t})}{h _ {i} ^ {t - 1} \alpha_ {i} ^ {t - 1}}.
$$

This case happens when $U _ { i } ^ { t } ( B _ { i } - \varepsilon ) > U _ { i } ^ { t } ( B _ { i } )$ , that is

$$
v _ {i} ^ {t} > \frac {h _ {i} ^ {t - 1} \alpha_ {i} ^ {t - 1} - \delta q _ {i} ^ {t - 1}}{(1 - \theta_ {i} ^ {t}) h _ {i} ^ {t - 1} \alpha_ {i} ^ {t - 1}} (B _ {i} - \theta_ {i} ^ {t} p _ {i} ^ {\prime t}) - \frac {\delta (\theta_ {i} ^ {t} p _ {i} ^ {\prime t} + \alpha_ {i} ^ {t - 1})}{h _ {i} ^ {t - 1} \alpha_ {i} ^ {t - 1}}.
$$

Otherwise, the user will increase the fee to $B _ { i }$ and get the corresponding payof as

$$
U _ {i} ^ {t} = v _ {i} ^ {t} - B _ {i} + \delta q _ {i} ^ {t},
$$

where,

$$
q _ {i} ^ {t} = \frac {q _ {i} ^ {t - 1} (h _ {i} ^ {t - 1} + 1) (\alpha_ {i} ^ {t - 1} + B _ {i})}{h _ {i} ^ {t - 1} \alpha_ {i} ^ {t - 1}}.
$$

When there is $b _ { i } ^ { * } = \nu _ { i }$ in the original uniform game, the user has no incentive to submit a lower fee in the extended uniform game, because a lower fee cannot generate a higher payof. On the contrary, submit ting a higher fee exceeding $\nu _ { i }$ becomes a feasible strategy when

$$
v _ {i} ^ {t} > B _ {i} - \frac {\delta}{h _ {i} ^ {t - 1}} \Bigg [ q _ {i} ^ {t - 1} \bigg (1 + \frac {(h _ {i} ^ {t - 1} + 1) B _ {i}}{\alpha_ {i} ^ {t - 1}} \bigg) \Bigg ],
$$

or

$$
v _ {i} ^ {t} > p _ {i} ^ {\prime t} - \frac {\delta}{h _ {i} ^ {t - 1}} \Bigg [ q _ {i} ^ {t - 1} \Bigg (1 + \frac {(h _ {i} ^ {t - 1} + \theta_ {i} ^ {t}) p _ {i} ^ {\prime t}}{\alpha_ {i} ^ {t - 1}} \Bigg) \Bigg ].
$$

According to the above analysis, we can conclude that in the transaction confirmation game under the farsighted payofs taking quality scores into account, the user will submit the fee at least as high as that in the case when taking transactions' net values as users' payofs.

From Theorem 7. we can also obtain that users will not get the lower $\boldsymbol { u } ^ { t ^ { * } }$ if they do not submit lower equilibrium fees, and because $q ^ { t } > 0$ and $\delta > 0 _ { : }$ , they will get higher payofs in the game under the farsighted payof function.

## 3.4. Virtual fees

In this section, we mainly discuss the influence of virtual fees. For comparison, we first consider that transactions with and without fees are lined up separately, where those transactions with fees are ranked mainly according to user-submitted fees while those without transaction fees are ranked on the basis of the waiting time. In general, users will decide to participate in which separate game according to com parisons of payofs generated from these two games.

In the separate transaction confirmation game played by users submitting no fees (separate game-1 for short), the system reserves a certain space $S ^ { 1 }$ of each block for them. In general, we have $s ^ { 1 }$ ≪ $S - S ^ { 1 }$ . Transactions in separate game-1 are ranked by $w _ { i } / s _ { i } ,$ and we use $j _ { i } ^ { 1 }$ to define the rank of the user $i \in N ^ { 1 }$

If the user's transaction can be confirmed and recorded into the upcoming new block in the separate game-1, the payof will be equal to his/her valuation; otherwise, the payof will be zero. Analogous to the discussions in Section 3.1, we calculate the discount factor of user $i \in N ^ { 1 }$ in the separate game-1 by the following equation:

$$
\lambda_ {i} ^ {1} = \left\{ \begin{array}{c c} 1, & \text {if} \quad \sum_ {k = 0} ^ {j _ {i} ^ {1}} s _ {k} \leq S ^ {1} \\ \frac {S ^ {1} - \sum_ {k = 0} ^ {j _ {i} ^ {1} - 1} s _ {k}}{s _ {j _ {i} ^ {1}}}, & \text {if} \quad \sum_ {k = 0} ^ {j _ {i} ^ {1} - 1} s _ {k} <   S ^ {1} <   \sum_ {k = 0} ^ {j _ {i} ^ {1}} s _ {k} \\ 0, & \text {if} \quad \sum_ {k = 0} ^ {j _ {i} ^ {1} - 1} s _ {k} \geq S ^ {1} \end{array} \right.\tag{18}
$$

In the separate transaction confirmation game played by users submitting fees (separate game-2 for short), their ranks depend on the weighted fees without considering the waiting time, that is, ${ b _ { i } } ^ { ' } = b _ { i } q _ { i } / s _ { i }$ $b _ { 1 } ^ { \prime } \geq b _ { 2 } ^ { \prime } \geq . . . \geq b _ { n - n } ^ { \prime } 1$ . We use ${ j _ { i } ^ { 2 } }$ to represent the rank of user i ∈ $N ^ { 2 } ,$ where $N ^ { 2 } = N - N ^ { 1 }$ . Also, the space in the upcoming new block allocated to this game is $S - S ^ { 1 }$

Similar with the analysis in Section 3.1, we can then obtain the discount factor of user $i \in N ^ { 2 }$ in the separate game-2 as

$$
\theta_ {i} ^ {2} = \left\{ \begin{array}{c c} 1, & \text {if} \quad \sum_ {k = 0} ^ {j _ {i} ^ {2}} s _ {k} \leq S - S ^ {1} \\ \frac {S - S ^ {1} - \sum_ {k = 0} ^ {j _ {i} ^ {2} - 1} s _ {k}}{s _ {j _ {i} ^ {2}}}, & \text {if} \quad \sum_ {k = 0} ^ {j _ {i} ^ {2} - 1} s _ {k} <   S - S ^ {1} <   \sum_ {k = 0} ^ {j _ {i} ^ {2}} s _ {k} \\ 0, & \text {if} \quad \sum_ {k = 0} ^ {j _ {i} ^ {2} - 1} s _ {k} \geq S - S ^ {1} \end{array} \right.\tag{19}
$$

Also, in the separate game $^ { - 2 , }$ we can figure out the threshold fee $\gamma _ { i }$ to get

$$
\Gamma^ {2} = \min _ {i \in N ^ {2}} \left(\frac {\gamma_ {i} q _ {i}}{s _ {i}} | 0 <   \theta_ {i} ^ {2} \leq 1\right).\tag{20}
$$

In addition, the user's payof function in the separate game-2 is given as

$$
u _ {i} ^ {2} = \theta_ {i} ^ {2} (v _ {i} - p _ {i} ^ {2 ^ {\prime}}),\tag{21}
$$

where, the user's payment under the GSP mechanism is

$$
p _ {i} ^ {2 ^ {\prime}} = \frac {b _ {j _ {i} + 1} ^ {\prime} s _ {i}}{q _ {i}} + \varepsilon .\tag{22}
$$

For simplicity, we consider the case where all users have the same quality score of 1 and the same transaction size of 1 to derive the equilibria of these two separate games as well as the uniform game, which are described in Table 3.

Proposition 8. Compared with that in the separate games, a high virtual fee in the uniform game does not necessarily encourage the user to submit the fee but will improve his/her payof.

## Table 3

Equilibria in the separate games and the uniform game.

<table><tr><td>Game type</td><td>Discount factor</td><td>Equilibrium fee</td><td>Payoff</td></tr><tr><td>Separate</td><td>1</td><td>0</td><td> $v_i$ </td></tr><tr><td rowspan="2">Game-1</td><td> $S^1 - (j_i^1 - 1)$ </td><td>0</td><td> $[S^1 - (j_i^1 - 1)]v_i$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>Separate</td><td>1</td><td> $\Gamma^2$ </td><td> $v_i - \Gamma^2$ </td></tr><tr><td rowspan="2">Game-2</td><td> $S - S^1 - (j_i^2 - 1)$ </td><td> $\Gamma^2 - \varepsilon$ </td><td> $[S - S^1 - (j_i^2 - 1)](v_i - p_i^{2'})$ </td></tr><tr><td>0</td><td> $v_i$ </td><td>0</td></tr><tr><td>Uniform</td><td>1</td><td> $B_i$ </td><td> $v_i - B_i$ </td></tr><tr><td rowspan="2">Game</td><td> $S - (j_i - 1)$ </td><td> $B_i - \varepsilon$ </td><td> $[S - (j_i - 1)](v_i - p_i)$ </td></tr><tr><td>0</td><td> $v_i$ </td><td>0</td></tr></table>

![](/api/attachments/GQHFWFWG/fulltext/images/0a84be242b02e057a0a3efc242706172b733d519a7fe107e08f9fa1204371993.jpg)  
Fig. 2. Users' fee saving proportion by the GSP mechanism.

![](/api/attachments/GQHFWFWG/fulltext/images/4e5c23ec45210715630fdca4fda747fbd837c47afefcf5892b8025bccc73723b.jpg)  
Fig. 3. Transactions' equilibrium ranks in the uniform game without and with quality scores.

Proof. As follows, we study the influence of virtual fees through comparing users' fee decisions in separate games and the uniform game.

For the user originally participating in the separate game-1, there occurs either the case of $\nu _ { i } < { p _ { i } ^ { 2 ^ { \prime } } }$ or the case of $\nu _ { i } \ge p _ { i } ^ { 2 ^ { \prime } } , u _ { i } ^ { 1 } ( w _ { i } ) \ge u _ { i } ^ { 2 } ( b _ { i } ^ { * } )$

Under the case of $\nu _ { i } < { p _ { i } ^ { 2 } } ^ { \prime }$ , there is $\theta _ { i } ^ { 2 } = 0$ in the separate game-2. If a high $\mathfrak { z } _ { i }$ leads to $B _ { i } - \varepsilon \le { \nu } _ { i } < { p } _ { i } ^ { 2 ^ { \prime } }$ , the user can submit a fee less than his/her valuation to be a partial winner; and if $\begin{array} { r } { v _ { i } < { p _ { i } ^ { 2 ^ { \prime } } } \le B _ { i } - \varepsilon , } \end{array}$ , the user's optimal choice is to submit a fee equal to the true valuation according to Lemma 1.

Under the case of $\nu _ { i } \ge p _ { i } ^ { 2 ^ { \prime } } , u _ { i } ^ { 1 } ( w _ { i } ) \ge u _ { i } ^ { 2 } ( b _ { i } ^ { * } )$ , if a high z leads to $\nu _ { i } \geq$ $B _ { i } - \varepsilon ,$ , the user can submit a fee less than his/her valuation to be a winner; if $B _ { i } - \varepsilon > \nu _ { i } \geq p _ { i } ^ { 2 ^ { \prime } }$ , the user cannot aford a fee to win the game, and his/her optimal strategy is ofering a fee equal to the true valuation according to Lemma 1.

• If the user originally participates in the separate game-2, there is $\nu _ { i } \ge p _ { i } ^ { 2 ^ { \prime } } , u _ { i } ^ { 1 } ( w _ { i } ) \le u _ { i } ^ { 2 } ( b _ { i } ^ { * } )$ . Furthermore, if $\Gamma ^ { 2 } - \varepsilon > \nu _ { i } \geq { p } _ { i } ^ { 2 ^ { \prime } }$ , there is $\theta _ { i } ^ { 2 } = \lambda _ { i } ^ { 1 } = 0$ . which means the user has short waiting time and low transaction valuation; and if $\nu _ { i } \geq \Gamma ^ { 2 } - \varepsilon ,$ there must be $\theta _ { i } ^ { 2 } > \lambda _ { i } ^ { 1 }$ Similarly, in the uniform game, a high z will lead to $\nu _ { i } \geq B _ { i } - \varepsilon ,$ , the user can be a winner; and if $B _ { i } - \varepsilon > \nu _ { i } \geq { p _ { i } ^ { 2 ^ { \prime } } }$ , the user cannot be a winner, and his/her optimal strategy is to submit the true valuation according to Lemma 1.

From the above analysis, if an extremely high z results in $B _ { i } - \varepsilon = 0$ or $B _ { i } = 0 ,$ , the user can submit no fee but obtain a positive payof in the uniform game; and if a high z leads to $0 < B _ { i } - \varepsilon \le \nu _ { i } ,$ , the user needs to submit a positive fee to get a payof exceeding zero in the uniform game. As such, we can conclude that a high z does not necessarily encourage the user to ofer a fee but will improve his/her payof.

![](/api/attachments/GQHFWFWG/fulltext/images/4cec1b74e664e48ea1d7ad963799536bc0510952f3b7718182272fa8c2da3f64.jpg)

![](/api/attachments/GQHFWFWG/fulltext/images/d17b7c52814b8c6553424bec7f5c23c665110b0d70bb1a6ff35ddc762e9b50bb.jpg)  
(a) Payments

![](/api/attachments/GQHFWFWG/fulltext/images/fc0a2bd305e4fa0b1eef3616cd3b41114113e099bb1ed9146407c567f76cfeaf.jpg)

![](/api/attachments/GQHFWFWG/fulltext/images/aef2d2885ab6c0c28d2b1b5475b81df972fc400ccf20a2413adf0ceb0f399260.jpg)  
(b) Payoffs

Fig. 4. Equilibrium payments and payofs in the uniform game without and with quality scores.  
![](/api/attachments/GQHFWFWG/fulltext/images/c7a6ff945a70730afc99097d4faa3b314ba6e69eecc0ddd8746330ad74aa1a20.jpg)  
Fig. 5. Transactions' equilibrium ranks in the uniform game and separate games.

## 4. Computational experiments

In this section, we randomly choose the real transactions in block #567948 as the dataset of our experiments. This block was mined at 04:13 PM on March 20, 2019, and it is a full block with the size of 1,258,958 bytes. It collects total transaction fees of 0.22994263 bitcoins (BTC) from 2589 transactions<sup>6</sup>. Keeping the user-submitted fees and the existing allocation result under the GFP mechanism unchanged, the GSP mechanism can lead a saving of 5.12% on the payment for all winning users. Besides, the payment saving proportion for each user is described in Fig. 2, from which we can see that some users can even get their payment reduced by about 20%. If the transaction confirmation game under the GSP mechanism can reach the equilibrium described in Theorem 4, the proportion of saved payment for users will be up to 94.5%. On March 20. 2019. the total transaction fees collected by 156 blocks is 27.19979230 BTC and each BTC values about 4020 USD, then we can simply predict that the GSP mechanism can help Bitcoin users save 103.33 thousand USD per day.

In what follows, we design computational experiments to probe the influences of quality scores and virtual fees in the transaction confirmation game adopting the GSP mechanism. Computational experiments are the applicable method for the case without perfect real-world data [24]. It has been proven that the work using synthetic data usually has no significant diference when compared with real-data-based work by data scientists [17]. We use the real-world data of 2589 transactions as the basic dataset, which mainly includes the transaction size $( \mu = 4 8 6 . 1 4 2 1$ bytes and $\sigma = 1 9 2 3 . 2 9 )$ and the waiting time $( \mu = 3 3 . 5 6 3 2$ seconds and $\sigma = 1 8 . 4 4 9 6 )$ . Here, we restrict the block size to 1,048,576 bytes. Quality scores and virtual fees are randomly generated. Especially, the generated virtual fees should meet two conditions: they increase as transactions' waiting time get longer; and they can adiust transactions' ranks but not act as the decisive factor. To ensure the reliability of experiments, we run 5000 independent ex periments with randomly generated parameters. All these experiments can validate our proposed mechanism; as such, we randomly select one as an illustrative example to conduct the following analysis [20].

![](/api/attachments/GQHFWFWG/fulltext/images/c879ec70315aeea30fdfd94b97ff1e0897842ca76cae4919856ebe93aeec04f2.jpg)

(a) Payments  
![](/api/attachments/GQHFWFWG/fulltext/images/d05c6633e9515d32488afe7cd40cbb30699d4a09ee4fa0f0e78dda23763a9ce1.jpg)  
(b) Payoffs  
Fig. 6. Equilibrium payments and payofs in the uniform game and separate games.

First, we analyze the computational experiments on quality scores, and the results are described by Figs. 3 and 4. In these experiments, we set all transactions to have the same waiting time.

In the uniform game without quality scores, the block can record 2397 transactions and collect the fees of 0.0570 BTC; while in the uniform game with quality scores, the transaction count is 2307 and the total fees are 0.0451 BTC. Quality scores reduce users' average payments by 17.8%, that is, from 0.00002381 BTC to 0.00001957 BTC. These results demonstrate positive efects of quality scores on saving users' fees.

As shown in Fig. 3, there are 99.85% of those transactions having their equilibrium ranks changed by quality scores; but 91.86% of confirmed transactions can still maintain their positions as the winning ones in the game with quality scores. According to Fig. 4, these two games show a similar overall trend of equilibrium payments and payofs, respectively. However, winners with quality scores higher than the one ranked at 2307 can transfer lower payments and win higher payofs. These results indicate that although quality scores exert great influences on users' equilibrium ranks and payments, they will not dis tinctly change the allocative results of the limited block space to transactions.

Then, we conduct the computational experiments on virtual fees, and the results are shown in Figs. 5 and 6. In these experiments, we set all transactions to have the same quality scores.

In the separate games, the block can record 2402 transactions, among which 221 are from the separate game-1 and 2181 are from the separate game-2. The fees collected from the separate game-2 are 0.0544 BTC, and this game achieves an average payment of 0.00002494 BTC per transaction. In the uniform game, the total payments are 0.04907 BTC collected from 2476 transactions, and the average fee per transaction is 0.00001982 BTC. These results confirm that the design of virtual fees can help users reduce payments transferred to miners.

According to Fig. 5, transactions' equilibrium ranks are distinctly diferent in the separate games and the uniform game. In detail, 95.93% of winning transactions in the separate game-1 are ranked lower in the uniform game; however, 99.1% of them still successfully get confirmed in the uniform game. 99.58% of transactions participating in the separate game-2 have their equilibrium ranks changed due to virtual fees introduced into the uniform game; however, 99.72% of winning transactions in the separate game-2 still win the confirmation chance in the uniform game. From Fig. 6, we can see that no winner needs to pay in the separate game-1 and their average payof is 0.00004461 BTC; while all winners transfer fees to miners in the separate game-2 and their average payof is 0.00007257 BTC. The uniform game achieves an average payof of 0.00006993 BTC for all winners. As such, we can conclude that the design of virtual fees aiming to process all transactions in a uniform pipeline can improve the confirmation eficiency while taking into account the interests of both types of transactions.

## 5. Conclusions and future work

Considering unique features of transaction fee auctions in the Bitcoin system, we propose a novel GSP auction mechanism to be tailored to its practical requirements of dealing with the problems caused by the currently-used GFP mechanism, which has been maturely employed in the practical online ad auctions.

In our proposed GSP auction, we introduce quality scores and virtual fees accumulated from the waiting time to formulate the weighted fees as the transaction ranking basis. The proposed GSP mechanism in this paper has been proven to have the unique PSNE. Also, the influences of quality scores and virtual fees on users' equilibrium decisions and payofs are investigated, and some interesting properties are obtained. Besides, we make a small extension to consider the farsighted users who take the generated quality scores as a part of their payofs, and find that it can guarantee users' fees at least as high as that in the case taking transactions' net values as users' payofs. Finally, we con duct computational experiments to validate the theoretical models and analysis.

Our research has confirmed the superiority of the GSP mechanism on saving users' fees, compared with the currently adopted GFP mechanism. Besides, both quality scores and virtual fees can help users reduce paid fees. Although they cause significant changes to users' equilibrium ranks but exert very limited efects on the final allocative results, and thus will not generate great disturb to the current Bitcoin transaction ecosystem. Using our proposed mechanism in this paper, all transactions can be processed more eficiently in a uniform pipeline, and the interests of both types of transactions are taken into con sideration.

In the future work, we plan to address the limitations of current research. First, the transaction confirmation game is intrinsically dy namic, and the unconfirmed transactions in the current round keep participating in the next round of the game, which will lead users' fee decision to be diferent from that in the static game. In view of this, we plan to study the dynamic multi-round transaction confirmation games. Second, we will try to relax the assumption of complete information to consider the transaction confirmation game with incomplete information, and also analyze the corresponding Bayes-Nash Equilibrium.

ready to revolutionize online advertising? IEEE Access. 6 (2018) 54884–54899.

[19] M. Pisa, M. Juden , Blockchain and Economic Development: Hype vs. Reality, Center for Global Development Policy Paper, 2017

[20] R. Qin, Y. Yuan, F. Wang , A novel hybrid share reporting strategy for blockchain miners in PPLNS pools, Decis. Support. Syst. 118 (2019) 91–101.

[21] R. Sano, Vickrey-Reserve Auctions and an equilibrium equivalence, Math. Soc. Sci. 65 (2) (2013) 112–117.

[22] K. Toyoda, P.T. Mathiopoulos, I. Sasase, et al., A novel Blockchain-based product ownership management system (POMS) for anti-counterfeits in the post supply chain, IEEE Access 5 (2017) 17465–17477.

[23] H.R. Varian, Position auctions, Int. J. Ind. Organ. 25 (6) (2007) 1163–1178

[24] F. Wang, Y. Yuan, C. Rong, J. Zhang, R. Qin, M.H. Smith , Blockchainized internet of minds: a new opportunity for Cyber-Physical-Social systems, IEEE Trans. Comput. Soc. Syst. 5 (4) (2018) 897–906.

[25] Wong J., New study: low bitcoin transaction fees unsustainable, http://www. coindesk.com/new-study-low-Bitcoin-transaction-fees-unsustainable accessed Oct 13, 2014

[26] H. Yu, Yang De, J. Wang , Equilibrium analysis of GSP keyword auctions with budget constraints, Oper. Res. Manag, Sci, 23 (4) (2014) 144–157.

[27] Y. Yuan, F. Wang , Blockchain cryptocurrencies: model, architecture and applications, IEEE Trans. Syst. Man Cybern. Syst. 48 (9) (2018) 1421–1428

[28] Y. Yuan, D. Zeng, H. Zhao, et al., Analyzing positioning strategies in sponsored search auctions under CTR-based quality scoring, IEEE Trans. Syst. Man Cybern. Syst. 45 (4) (2015) 688–701.

[29] Y. Zhang, R.H. Deng, X. Liub, D. Zheng , Blockchain based eficient and robust fair payment for outsourcing services in cloud computing, Inf. Sci. 462 (2018) (2018) 262–277.

[30] X. Zhang, J. Feng , Cyclical bid adjustments in search-engine advertising, Manag. Sci. 57 (9) (2011) 1703–1719.

## Acknowledgments

## References

We gratefully acknowledge the funding supports from the National Natural Science Foundation of China (#61533019, #71702182).

[1] L. Ausubel, P. Milgrom, The lovely but lonely Vickrey Auction, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, 2005.

[2] T. Borgers, I. Cox, M. Pesendorfer, et al., Equilibrium bids in sponsored search auctions: theory and evidence, Am. Econ, J. Macroecon, 5 (4) (2013) 163–187.

[3] K. Chalkias, I. Dionysiou, Going beyond the coinbase transaction fee: alternative reward schemes for miners in blockchain systems. Pan-Hellenic Conference on Informatics. ACM. 2016. p. 35

[4] L.W. Cong, Z. He , Blockchain Disruption and Smart Contracts, Social Science Electronic Publishing, 2017

[5] P. Cska, P.J. Herings , Decentralized clearing in financial networks, Manag. Sci. (2017). https://doi.org/10.1287/mnsc.2017.2847

[6] M.M. Davis, T.E. Vollmann , A framework for relating waiting time and customer satisfaction in a service Operation[J], J. Serv. Mark. 4 (1) (1990) 61–69.

[7] B. Edelman. M. Ostroysky. M. Schwarz . Internet advertising and the generalized second-price auction: selling billions of dollars worth of keywords, Am. Econ, Rey. 97 (1) (2007) 242–259.

[8] N. Houy, The Economics of Bitcoin Transaction Fees, Social Science Electronic Publishing, 2014.

[9] G. Huberman, J. Leshno, C. Moallemi , Monopoly Without a Monopolist: An Economic Analysis of the Bitcoin Payment System, Social Science Electronic Publishing, 2017.

[10] Y. Kamijo, Bidding behaviors for a keyword auction in a sealed-bid environment, Decis, Support, Syst, 56 (1) (2013) 371–378.

[11] K. Kaskaloglu, Near zero bitcoin transaction fees cannot last forever, The International Conference on Digital Security and Forensics, 2014, pp. 91–99.

[12] N. Kshetri, Blockchains roles in meeting key supply chain management objectives, Int. J. Inf. Manag. 39 (2018) (2018) 80–89.

[13] R. Lavi, O. Sattath, A. Zohar , Redesigning Bitcoin's Fee Market, (2017) https:// arxiv.org/abs/1709.08881.

[14] R.P. Leme, E. Tardos, Pure and Bayes-Nash price of anarchy for Generalized Second Price auction, IEEE 51st Annual Symposium on Foundations of Computer Science, IEEE, 2010, pp. 735–744.

[15] X. Li, C. Wang , The technology and economic determinants of cryptocurrency exchange rates: the case of bitcoin, Decis. Support. Syst. 95 (2017) 49–60.

[16] M. Moser, R. Bohme, Trends, tips, tolls. A longitudinal study of Bitcoin transaction fees, International Conference on Financial Cryptography and Data Security, Springer, Berlin Heidelberg, 2015, pp. 19–33.

[17] N. Patki, R. Wedge, K. Veeramachaneni, The synthetic data vault, Proceedings of the Third IEEE International Conference on Data Science and Advanced Analytics (DSAA2016). 2016, pp. 399–410 Montreal, Canada

[18] M. Parssinen. M. Kotila. R.C. Rumin. A. Phansalkar. J. Manner, Is Blockchain

![](/api/attachments/GQHFWFWG/fulltext/images/63c2a8ffddb0adf56d71c008380d4fde5c2fe3e81659f9d71c1ca720a8e45c34.jpg)

Juanjuan Li received her B.S. and M.S. degrees in Economics from Renmin University of China in 2008 and 2010, respectively, and she is a Ph.D. student with Beijing Institute of Technology since 2017. Currently, she is an Assistant Professor with the State Key Laboratory for Management and Control of Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing, China. Her current research interests include blockchain, computational advertising and business intelligence

![](/api/attachments/GQHFWFWG/fulltext/images/788d0b151e735e14e78a9db87b1798bf7d311ea96dcf669fdc9996323b4fc866.jpg)

Yong Yuan received the B.S., M.S., and Ph.D. degrees from the Shandong University of Science and Technology, Qingdao, China, in 2001, 2004, and 2008, respectively, all in computer software and theory. He is currently an Associate Professor with the State Key Laboratory for Management and Control of Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing, China. He is also with the Qingdao Academy of Intelligent Industries, Qingdao. His current research interests include social computing, blockchain, computational advertising and smart contracts.

![](/api/attachments/GQHFWFWG/fulltext/images/69451d24b5c3800ef18ff18998a0d8bc19f9c57104cfc664c7e6f729387cc4a6.jpg)

Fei-Yue Wang received the Ph.D. degree in computer and systems engineering from Rensselaer Polytechnic Institute, Troy, NY. USA. in 1990. He joined the University of Arizona, Tucson, AZ, USA, in 1990, and became a Professor and the Director of the Robotics and Automation Laboratory and the Program in Advanced Research for Complex Systems. In 1999, he founded the Intelligent Control and Systems Engineering Center, Institute of Automation, Chinese Academy of Sciences (CAS), Beijing, China, under the support of the Outstanding Overseas Chinese Talents Program from the State Planning Council and “100 Talent Program” from CAS. In 2002, he joined the Lab of Complex Systems and Intelligence Science, CAS, as the Director. where he was the Vice President for Research

Education, and Academic Exchanges with the Institute of Automation from 2006 to 2010 In 2011, he was named as the State Specially Appointed Expert and Director of the State Key Laboratory for Management and Control of Complex Systems, Beijing, China. His current research interests include methods and applications for parallel systems, blockchain, social computing, parallel intelligence, and knowledge automation.

Dr. Wang has been the general or program chair of more than 30 IEEE, INFORMS, ACM, and ASME conferences. He was the President of the IEEE ITS Society during 2005–2007, the Chinese Association for Science and Technology, USA, in 2005, and the American Zhu Kezhen Education Foundation during 2007–2008. He was the Vice President of the ACM China Council during 2010–2011, and chair of IFAC TC on Economic and Social Systems from 2008 to 2011. Currently. he is the President-Elect of JEEE Council on RFID. Since 2008, he has been the Vice President and the Secretary General of the Chinese Association of Automation. He was the Founding Editor-in-Chief of the International Journal of Intelligent Control and Systems during 1995–2000 and the IEEE ITS MAGAZINE during 2006–2007. He was the EiC of the IEEE INTELLIGENT SYSTEMS during 2009-2012 and the IEEE TRANSACTIONS ON ITS during 2009–2016. He is currently the EiC of the IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, and the Founding EiC of the

JEEE/CAA JOURNAL. OF AUTOMATICA SINICA and the Chinese Journal of Command and Control. He was elected as a fellow of IEEE, INCOSE, IFAC, ASME, and AAAS. In 2007, he was a recipient of the National Prize in Natural Sciences of China and was awarded the Outstanding Scientist by ACM for his research contributions in intelligent control and social computing. He was a recipient of the IEEE INTELLIGENT TRANSPORTATION SYSTEMS (ITS) Outstanding Application and Research Awards in 2009, 2011, and 2015, and the IEEE SMC Norbert Wiener Award in 2014.
