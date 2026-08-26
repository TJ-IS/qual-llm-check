---
otero_id: 27669
otero_key: "4WUBVYAF"
title: "Rewards or Upgrades? Incentive Designs in Referral Programs"
authors: "Chenguang (Allen) Wu; Chen Jin; Ying-Ju Chen"
year: "2026"
journal: "MIS Quarterly"
doi: "10.25300/misq/2025/19540"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# REWARDS OR UPGRADES? INCENTIVE DESIGNS IN REFERRAL PROGRAMS<sup>1</sup>

Chenguang (Allen) Wu Department of Industrial Engineering and Decision Analytics, Hong Kong University of Science and Technology HONG KONG {allenwu@ust.hk}

Chen Jin

Department of Information Systems and Analytics, School of Computing, National University of Singapore SINGAPORE {disjinc@nus.edu.sg}

Ying-Ju Chen School of Business and Management (ISOM), Hong Kong University of Science and Technology HONG KONG {imchen@ust.hk}

Referral programs are widely used for customer acquisition. Traditionally, these programs adopt a referral-reward approach, offering monetary incentives for successful referrals. However, many firms, especially in digital industries, have embraced an alternative—referral-upgrade programs that reward successful referrers with product upgrades such as premium features or enhanced services. Despite their growing use, little is known about when such programs can outperform the traditional referral-reward approach. This paper develops a stylized model to compare these two referral mechanisms. We address two questions: (1) when referral-upgrade programs are more (or less) profitable than referral-reward programs, and (2) how key factors such as referral costs and referral reachability, captured by multiple referrals and the degree of overlap among referred friends, affect firms’ decisions and customer behaviors. We find that referral-upgrade programs are generally more profitable than referral-reward programs, and this profit dominance remains robust to various extensions such as marginal costs or boundedly rational customers but may reverse when referral costs are correlated with customer valuations or when referral reachability expands via multiple referrals. Our findings offer managerial insights into when firms should adopt upgrade-based incentives to manage their referral programs.

Keywords: Referral-upgrade, referral-reward, product line design, versioning, pricing

## Introduction

Referral programs are widely used as a popular customer acquisition strategy across industries. Firms face a managerial choice when implementing referral programs: whether to incentivize customers to make referrals through monetary rewards or non-monetary upgrades. Specifically, under a traditional referral-reward program, firms provide customers with monetary or monetary-equivalent rewards for each successful referral. Under a referral-upgrade program, firms stimulate referrals by offering free product or service upgrades such as premium features or enhanced benefits.

Firms usually adopt one of these referral programs across industries. Monetary-based referral programs are widely observed among financial institutions such as American Express and Discover, which offer cash-back rewards for successful referrals. They also appear broadly across retail, travel, and even digital industries. Referral-upgrade programs, while common in digital contexts such as Dropbox and Spotify, which provide extra storage space and ad-free music streaming experiences, respectively, as referral incentives, also increasingly appear in non-digital industries, such as Anytime Fitness gyms<sup>2</sup> and Sephora cosmetics<sup>3</sup>, where successful referrals are rewarded with enhanced membership experiences or exclusive gift packages.

Interestingly, some firms may simultaneously utilize both referral mechanisms. Examples include those from the gaming industry: World of Tanks,<sup>4</sup> World of Warships,<sup>5</sup> and Caliber<sup>6</sup> operate referral-upgrade programs by offering players premium in-game items or enhanced game accounts; they also embrace referral-reward programs by offering referral incentives in the form of in-game currency. This notable dual adoption in the gaming industry suggests that firms may experimentally execute both referral mechanisms to assess their relative effectiveness.

The widespread use of referral-upgrade programs across digital and non-digital industries underscores their practical significance as an alternative to monetary-based incentives. Moreover, the coexistence of both referral programs in certain industries suggests that understanding how these two mechanisms compare is a practically important question for both researchers and practitioners.

Despite their growing use, the design of referral incentives through quality improvements in referral-upgrade programs has received less attention in the academic literature. To the best of our knowledge, most of the existing literature has exclusively considered referral incentives in the form of monetary benefits (see e.g., Biyalogorsky et al., 2001; Libai et al., 2003; Kornish & Li, 2010; Jing & Xie, 2011; Xiao et al., 2011; Lobel et al., 2017). However, in the context of Dropbox, referrals bring customers increased storage space, and in the context of Spotify, customers with successful referrals can enjoy ad-free listening. In these contexts, referral benefits are not directly monetary; instead, they come in the form of higher product quality (more space or longer duration of ad-free privileges).

In this paper, we conduct the first analytical study of referral programs with quality-based referral incentives. We set up a stylized model in which a monopoly firm sells a product to customers with heterogeneous valuations. We consider two referral mechanisms: referral-reward and referral-upgrade. Under both programs, each customer, upon purchasing a product, is invited to refer a friend. Making a referral incurs a cost, and to motivate referrals, the firm promises certain benefits provided that the referral is successful and generates a new purchase. Under the referral-reward mechanism, the firm sells a full-version product to each customer, and each referring customer receives a monetary reward conditioned on (1) the customer making a referral, and (2) the referral being successful. Alternatively, under the referral-upgrade mechanism, the firm sells a basic version of the product to each customer, and each purchasing customer can receive a free upgrade to a full-version product if the referral leads to a new purchase of the product.

In this paper, we focus on understanding two fundamental questions:

Under what conditions are referral-upgrade programs more (or less) profitable than traditional referral-reward programs?

How do key factors such as referral costs and referral reachability, captured by multiple referrals and the degree of overlaps among referred friends, affect customer behaviors and the firm’s optimal design of referral incentives?

We consider a market composed of two types of customers: base customers, who are aware of the product by the time the referral program is launched, and referred customers, who are not aware of the product until they are referred by their friends. Our analysis begins with a benchmark setting where base customers can refer at most one friend. This setup is representative of real-world scenarios where referral programs are implemented as short-term promotional campaigns with limited duration. We compare the profitability of two referral programs in this setting. We show that the referral-upgrade program can unambiguously outperform the traditional referral-reward program. We argue that referral-upgrade induces heterogeneous referral incentives among base customers driven by their heterogeneous valuations. This, in conjunction with properly pulled price-and-quality levers, leads to enhanced efficiency in managing customer referrals.

Beyond the benchmark model, we develop a series of extensions to examine the robustness of our main result and provide additional insights. First, we consider base customers with bounded rationality: they are myopic and do not anticipate future referral benefits when making their purchase decisions. Under this behavioral limitation, we show that referral-upgrade continues to outperform referral-reward, as the advantage of referral-upgrade stems not from customers’ forward-looking behavior but from its capability to leverage customer heterogeneity to create heterogeneous referral incentives. Second, we consider positive marginal costs, and this is particularly relevant for non-digital goods such as cosmetics (e.g., Sephora) and fitness services (e.g., Anytime Fitness). We find that as long as the marginal cost does not escalate too rapidly with quality, referral-upgrade remains more profitable. Put together, these extensions demonstrate that the comparative advantage of referral-upgrade is robust to the bounded rationality and marginal-cost variations commonly encountered in real-world markets.

Two additional extensions, however, reveal the boundaries of the referral-upgrade mechanism. Both point to a structural limitation of this mechanism. First, when referral costs are heterogeneous and positively correlated with customer valuations, as may often arise when higher-valuation customers face greater psychological or opportunity costs of making referrals, the referral-upgrade approach may be less effective. Because the total product quality is bounded (i.e., the total upgrade size cannot exceed the full product quality), using upgrade-based benefits to stimulate referrals may fail to offer sufficiently strong incentives to high-valuation customers who also bear higher referral costs. In contrast, the referral-reward mechanism provides monetary incentives with essentially no nominal cap; it is better equipped to match referral incentives with costs and can potentially outperform referral-upgrade. Second, when base customers are allowed to make multiple referrals, effectively expanding the breadth of the referral structure, the referral-upgrade program may again fall short, as it suffers from an incentive-dilution effect. Specifically, the total available upgrade must be divided across multiple referrals, thereby diluting the strength of each individual incentive. In contrast, referral-reward compensates each successful referral with a separate monetary reward, and it is immune to this dilution.

## Literature Review

Our paper contributes to the burgeoning literature on customer referrals, which predominantly comprises empirical studies. For example, Hong et al. (2017) utilized laboratory and field experiments to investigate the joint effect of social distance between referrers and referees and the distribution format of monetary incentives on the outcome of referral programs. Sun et al. (2021) conducted a large-scale online experiment to study how promotional incentives can effectively engage consumers as both purchasers and sharers through their social connections. Jung et al. (2020) examined different types of calls-to-action (CTAs) in online referral programs with the objective of understanding how prosocial framing can be used to facilitate referrals. Belo and Li (2022) used data from an online dating platform to study the optimal design of social referral programs that balance growth, engagement, and revenue. Fernández-Lorıa et al. (2023) analyzé d how a referring customer’s behavior on a ride-sharing platform evolves over the customer’s lifecycle.

Analytical research on referral programs started with Biyalogorsky et al. (2001), which laid out the first framework of referral-reward programs. Later, Libai et al. (2003) incorporated richer informational structures and examined the benefit of personalized referral incentives. Kornish and Li (2010) considered the case of unknown product quality and suggested that referrals can be used to signal quality to referred customers. Jing and Xie (2011) compared the referral-reward program with group-buying and showed that the former can be more efficient in creating discrimination based on customers referral outcomes. Xiao et al. (2011) suggested decoupling the referral reward between referrers and referees, and Lobel et al. (2017) analyzed nonlinear referral rewards (total rewards not necessarily proportional to the number of successful referrals). Notably, referral incentives in this literature are primarily made in the form of monetary rewards. In this paper, we propose referral incentives in the quality dimension; our differentiation from this literature is thus clear.

Yang and Debo (2019) studied referral mechanisms similar to ours. The authors examined referral programs in a queueing setting wherein base customers who successfully refer their friends are offered priority admission to a service. Because customers prefer shorter waiting and value priority admission, referrals can lead to a non-monetary improvement in service acquisition in this queueing context. However, Yang and Debo (2019) assumed that priority can only be obtained through referrals and cannot be purchased directly, whereas customers in our model can purchase incremental upgrades even if their referrals are unsuccessful. We show that this distinction is important, making the referral-upgrade program broadly more profitable than the traditional referral-reward approach. In Table 1, we highlight other model differences between our work, Yang and Debo (2019), and key references in the referral literature.

In our model, base customers and referred customers are heterogeneous in their awareness of the product; in this sense, our work is broadly related to the literature on customers limited attention, i.e., individuals cannot process all available information due to cognitive constraints (Simon, 1955; Iyengar & Lepper, 2000). The concept of limited attention has significant implications in economics and business and can profoundly influence customer behaviors and firms’ marketing strategies (Tucker, 2014). Despite a broad connection to this literature, our work also differs from it in that we do not model customers’ endogenous information acquisition; instead, we assume that heterogeneous product awareness is an exogenous market feature. This facilitates a tractable and insightful analysis of our referral programs.

<table><tr><td colspan="4">Table 1. Key Modeling Differences Between Our Paper and Existing Referral Literature</td></tr><tr><td></td><td>Endogenous price</td><td>Endogenous quality differentiation</td><td>Allowing pay-to-upgrade</td></tr><tr><td>Our paper</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Yang and Debo (2019)</td><td>✓</td><td>X</td><td>X</td></tr><tr><td>Lobel et al. (2017)</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Biyalogorsky et al. (2001)</td><td>✓</td><td>X</td><td>X</td></tr><tr><td>Kornish and Li (2010)</td><td>✓</td><td>X</td><td>X</td></tr></table>

Referral-upgrade programs create incentive discrimination differentiated by customer valuations; this connects our work to the extensive literature on vertical differentiation and, more broadly, product line design and versioning. Early works on product line design include the continuous-valuation model (Mussa & Rosen, 1978) and the discrete-valuation model (Moorthy, 1984). Villas-Boas (1998) and Shi et al. (2013) extended these models to examine product line design in distribution channels. Desai (2001) considered horizontal differentiation (customers’ taste preference) in addition to vertical differentiation and found that firms may sell products with varied qualities to all customers on the market. Mendelson and Parlaktürk (2008) studied the customization strategies of competitive firms. Bhargava and Choudhary (2008) applied the continuous-valuation model in Mussa and Rosen (1978) to study the versioning strategies of digital goods. Lahiri and Dey (2018) examined when offering a base product alongside a fully featured version can be beneficial to the firm. These authors showed that versioning can be effective when there exists a segment of customers already familiar with their true valuations of the products. Chellappa and Mehra (2018) analyzed how different costs (e.g., development costs, usage costs, and versioning costs) affect both the quantity and quality of versions, and Qu et al. (2022) investigated customers’ optimal upgrading strategies in the presence of successive product generations.

## The Model

We consider a monopoly firm evaluating two referral mechanisms as part of its selling and customer acquisition strategy to maximize its expected profit. Under both programs, each customer, upon purchasing the firm’s product, is invited to refer a friend. Making a referral incurs a cost, and to incentivize this costly action, the firm offers rewards, the format of which may vary depending on the firm’s chosen referral program, provided that the referral is successful, i.e., it leads to a new purchase from the referred friend. In practice, referral programs are often used to boost public awareness of a new product, thereby assisting the firm in reaching new customers who are initially unaware of it. To model the heterogeneity in product awareness, we follow Yang and Debo (2019) and assume that the market consists of two types of customers. Base customers, whose population is normalized to 1, are aware of the product when the referral program is launched and strategize their purchase decisions, taking into account the referral option following their purchase. Referred customers are not aware of the product until they are referred by base customers. Upon receiving a referral, referred customers observe their valuation of the product and decide whether to purchase it. In our base model, we assume that when base customers make referrals, they can make, at most, one referral.<sup>7</sup>

We assume that each customer, regardless of whether she is a base customer or a referred customer, demands, at most, one unit of the product. Both base and referred customers are heterogeneous in their valuations, denoted by ??, which follows a uniform distribution over [0,1]. A customer of type ?? derives a utility of ???? from consuming a product with quality ?? ∈ [0,1]. Let ??(??) denote the cumulative distribution function (cdf) of customer types, and let $F ^ { c } ( v ) \triangleq 1 - F ( v )$ denote the complementary cdf. Following Lobel et al. (2017) and Yang and Debo (2019), we assume that each customer incurs a referral cost ?? > 0 whenever she makes a referral,<sup>8</sup> regardless of whether the referral succeeds or fails. Such a cost must be compensated by proper incentives to facilitate referrals. Finally, we assume zero marginal production costs in the base model.<sup>9</sup> This is representative of certain digital industries wherein additional units or qualities can be produced and distributed at negligible costs.

Under the commonly used referral-reward program (Biyalogorsky et al., 2001; Kornish & Li, 2010; Lobel et al., 2017), each referring customer receives a monetary reward ?? conditioned on: (1) the customer making a referral, and (2)

the referral being successful. No reward will be given out if a referral is made but fails to result in a new purchase. In our base model, because the product has zero marginal costs, the firm always sells a full-version product with the highest quality achievable to all customers, and we normalize this quality to 1.

In parallel to the referral-reward program, we propose a referral-upgrade mechanism, as exemplified by digital products such as Dropbox and Spotify. Under this new mechanism, the firm sells a basic version of the product (with quality $\theta < 1 )$ to base customers. A purchasing base customer will receive a free upgrade to the full-version product if she refers a friend and her referral leads to a new purchase of the product.

We focus on analyzing referral programs where the referral benefit to a referring customer is private rather than social. For instance, Spotify users may refer friends to obtain a premium subscription upgrade, primarily to enhance their own listening experience (e.g., ad-free streaming and offline playback) rather than to engage socially by sharing music. While incorporating network-based externalities could extend the scope of our model by capturing broader social benefits from referrals, we leave this to future research. Focusing on private referral benefits allows us to obtain clean insights into the fundamental trade-off inherent in each referral program. Table 2 summarizes the key notations in this paper.

## Analysis of Referral Programs

We begin by analyzing our base model, where only base customers can make referrals. This applies to scenarios in which referral programs are implemented as promotional campaigns with a limited duration. Despite its simplicity, the base model provides key insights into how quality-based incentives can drive customer referrals and how they compare, in terms of profitability, to the widely adopted monetary reward programs. In later sections, we show that these insights are largely robust to various realistic extensions.

## Referral-Reward Program

We first analyze the referral-reward program, a widely adopted mechanism in practice. In this setting, the firm sells the full-quality product (with quality normalized to one) at a price ??. Each base customer who makes a successful referral receives a monetary reward ??. The payoff of a base customer of type ?? from purchasing the product, taking into account the referral option, is

$$
U _ {B} (v) = v - p + (q r - c) ^ {+},\tag{1}
$$

where $( \cdot ) ^ { + } = \operatorname* { m a x } \{ \cdot , 0 \}$ and ?? denotes the probability that the referral will succeed. Because referred customers do not make further referrals, they simply purchase the product if their valuation exceeds the price, i.e., with probability $q = F ^ { c } ( p )$

<table><tr><td colspan="2">Table 2. Notation Summary</td></tr><tr><td>Notation</td><td>Description</td></tr><tr><td>v</td><td>Customer&#x27;s valuation type, uniformly distributed on [0, 1]</td></tr><tr><td>F(·)</td><td>Cumulative distribution function (cdf) of v</td></tr><tr><td>Fc(·)</td><td>Complementary cdf of v, i.e., 1 - F(·)</td></tr><tr><td>c</td><td>Referral cost incurred by a base customer</td></tr><tr><td>r</td><td>Monetary reward under the referral-reward program</td></tr><tr><td>θ</td><td>Quality of the basic product (0 ≤ θ ≤ 1)</td></tr><tr><td>pB</td><td>Price of the basic product</td></tr><tr><td>pU</td><td>Upgrade price (paid on top of pB to obtain the full-version product)</td></tr><tr><td>UB(v)</td><td>Expected utility of a v-type base customer from purchasing the basic product</td></tr><tr><td>Ur(v)</td><td>Expected utility of a v-type base customer from making a referral after purchasing the basic product</td></tr><tr><td>Uu(v)</td><td>Expected utility of a v-type base customer from directly paying for the upgrade after purchasing the basic product</td></tr><tr><td>qRb</td><td>Purchase probability of the basic product among referred customers</td></tr><tr><td>qRf</td><td>Purchase probability of the full-version product among referred customers</td></tr><tr><td>q</td><td>Probability that a referred customer will purchase the product</td></tr><tr><td>qB</td><td>Purchase probability of a base customer (demand from base customers)</td></tr><tr><td>α</td><td>Probability that a base customer will choose to make a referral</td></tr><tr><td>β</td><td>Probability that a base customer will choose to directly purchase the upgrade</td></tr><tr><td>γ</td><td>Probability that a base customer will purchase the upgrade after an unsuccessful referral</td></tr></table>

![](/api/attachments/4WUBVYAF/fulltext/images/35c9aa9bdb46b24f00d912ceca55e38e9cf258c677d9fad424a69fb990eaae19.jpg)  
Figure 1. Decision Tree of a Base Customer Under the Referral-Reward Program

In the above formulation, we assume that base customers are forward-looking and form rational expectations of their referral outcomes, following the common approach in the referral literature (Lobel et al., 2017; Yang & Debo, $2 0 1 9 ) ^ { 1 0 } .$ Figure 1 illustrates the sequence of outcomes for a ??-type base customer under the referral-reward program. In Equation (1), $v - p$ represents the direct utility from purchasing the product, and $( q r - c ) ^ { + }$ represents the expected utility from making a referral. Specifically, if $q r - c > 0$ , making a referral yields a strictly positive expected utility, and all purchasing base customers will refer their friends. In contrast, if $q r - c < 0$ , no base customers will refer. When $q r - c = 0 ,$ , we assume that all base customers will make referrals, thus selecting the firm’s most preferred equilibrium, which maximizes its profit.

Note that the expected utility from making referrals does not depend on a customer’s valuation ??. Therefore, all purchasing base customers will make referrals or none of them will, irrespective of their type. Consequently, a base customer will purchase the product if $U _ { B } ( v ) \geq 0$ , and the demand from base customers is $q _ { _ B } = F ^ { c } ( p - ( q r - c ) ^ { + } )$ .

The firm’s expected profit comprises profits from both base and referred customers. The firm optimally selects $( p , r )$ to maximize its expected total profit:

$$
\begin{array}{r l} \underset {p, r} {\max} & \Pi (p, r) = q _ {B} p + (p - r) q _ {B} q \cdot \mathbf {1} _ {\{q r \geq c \}} \\ \text {s.t.} & q _ {B} = F ^ {c} (p - (q r - c) ^ {+}), \text {and} q = F ^ {c} (p). \end{array}
$$

Note that in the second term of $\Pi ( p , r )$ , the monetary reward is counted as the firm’s cost only when it compensates for a successful referral that results in a new purchase. The firm earns a profit margin of $p - r$ from such a successful referral. The probability of a successful referral is determined by two sequential events: (1) a purchasing base customer makes a referral (with probability $q _ { B } ) ,$ , and (2) the referred customer accepts the referral and purchases the product (with probability ??).

Proposition 1: Under the referral-reward program:

i. $f 0 < c < 1 / 4 _ { \mathrm { : } }$ , all base customers will make referrals upon purchasing. The firm’s optimal decisions and profit are

$$
r ^ {*} = c + 1 / 4, p ^ {*} = 1 / 2, \Pi (p ^ {*}, r ^ {*}) = (5 / 4 - c) ^ {2} / 4.
$$

ii. $H c \geq 1 / 4 ,$ , no base customers will make referrals. The firm’s optimal decisions and profit are ??<sup>∗</sup> < 2??, ??<sup>∗</sup> = 1/2, Π(??<sup>∗</sup>, ??<sup>∗</sup>) = 1/4.

Intuitively, when the referral cost ?? is high, compensating base customers with overly generous monetary incentives to motivate referrals will be prohibitively expensive, and the firm will choose to abandon the referral program. In this case, any reward $r < 2 c$ will deter referrals, and the firm will sell to base customers exclusively at the monopoly price. Thus, the referral program is only effective when the referral cost is sufficiently low. In this case, the firm sets the reward to ensure that base customers receive a strictly positive expected utility from referring. This implies $q _ { B } > q ,$ , i.e., thanks to the referral opportunity, base customers are more likely to purchase the product than their referred friends. The firm’s optimal referral reward increases with the referral cost, as a larger referral cost must be compensated by a stronger monetary incentive. As a result, the firm’s profit decreases with the referral cost. In the extreme case where referrals are costless $( c = 0 )$ , the firm will achieve a profit of $2 5 / 6 4 \approx 0 . 3 9 1$ under the referral-reward program, marking a significant profit improvement, as opposed to the monopoly profit of 0.25 without any referrals. This points to the critical role of the referral program in customer acquisition, expanding market reach, and enhancing profitability.

## Referral-Upgrade Program

We now introduce a new referral mechanism that provides incentives through the quality dimension—a mechanism we refer to as the referral-upgrade program. This mechanism bears a resemblance to the classic versioning strategy, but with a key distinction. Traditional versioning relies on customer heterogeneity by offering multiple versions of a product (differentiated by qualities and prices), allowing customers to self-select based on their types. Despite its solid microeconomic foundation and intuitive appeal, the profitability of versioning is shown to heavily depend on the format of customer heterogeneity and the cost of versioning (Bhargava & Choudhary, 2008). In particular, when customers’ types are uniformly distributed and the marginal cost of producing each product is zero, Bhargava and Choudhary (2008) showed that versioning can do no better than selling a stand-alone fullversion product. In other words, the classic versioning framework is unable to exploit the underlying customer heterogeneity to deliver profitable discrimination. Our model integrates versioning with referrals. Specifically, we assume that the firm sells a basic version of the product to base customers, who can obtain a free upgrade to the high-quality version if their referrals are successful. As we show shortly, our proposed mechanism, representing a combination of versioning and referrals, can generate significant material benefits.

Formally, the firm sells a basic version of the product with quality $\theta \in [ 0 , 1 ]$ at a price $p _ { B } .$ Customers who purchase the basic product are offered an optional upgrade to the fullversion product, with a quality increment of 1 − ??, at an additional price $p _ { U } .$ Base customers can also receive this upgrade for free if they make a successful referral.

Before we conduct a formal analysis of this referral-upgrade mechanism, it is instructive to clarify how it differs from the traditional referral-reward approach in incentive design. In the upgrade program, successful referrals are compensated with a free quality improvement, whose value depends on the referring customer’s type. In other words, the referral-upgrade program introduces heterogeneous referral incentives among base customers, and such heterogeneity, in conjunction with properly pulled pricing levers, has the potential to create better market segmentation. In contrast, the referral-reward program sets an identical compensation scheme for all successful referrals, irrespective of the referring customer’s type, and it may fall short of exploiting the underlying customer heterogeneity. As we will show, this distinction is important, and it allows the referral-upgrade program to unlock new profit opportunities unavailable under traditional monetary reward schemes.

We now formally analyze the referral-upgrade program. Figure 2 shows the sequence of outcomes for a ??-type base customer under this program.

Consider a base customer with valuation ?? who has purchased the basic product. She has three follow-up options: (1) pay directly to upgrade, (2) attempt a referral, or (3) neither refer nor upgrade. The customer evaluates these options through backward induction. Specifically, after she has purchased the basic product and obtained utility $\theta v - p _ { B } ,$ if she does not refer, her (additional) utility is 0; if she pays to upgrade immediately (without referring), her utility is

$$
U ^ {u} (v) = v (1 - \theta) - p _ {U};\tag{2}
$$

if she attempts a referral, the expected utility is

$$
U ^ {r} (v) = q v (1 - \theta) + (1 - q) \mathrm{max} \{0, U ^ {u} (v) \} - c,\tag{3}
$$

where ?? is the probability that her referral will be successful (i.e., the referred customer purchases a product, whether it is a basic product or a full-version product), which will be defined later. The formulation in Equation (3) captures an important nuance: even if a referral fails, the customer can return to obtaining an upgrade by paying $p _ { { U } ^ { 9 } }$ and will do so whenever it is beneficial. To explain Equation (3), note that if the referral is successful, the base customer receives a free upgrade, corresponding to an expected utility $q v ( 1 - \theta )$ ; otherwise, the base customer contemplates whether to purchase the upgrade, with an expected utility $( 1 -$ $q ) \mathrm { m a x } \{ 0 , U ^ { u } ( v ) \}$ . Consequently, the total expected payoff from purchasing the basic product is

$$
U _ {B} (v) = \theta v - p _ {B} + \max \{0, U ^ {u} (v), U ^ {r} (v) \}.
$$

This payoff is strictly increasing in ??, so there exists a unique cutoff $v _ { 0 }$ (if any) such that $U _ { B } ( v _ { 0 } ) = 0$ . The demand from base customers is then $q _ { B } = F ^ { c } ( v _ { 0 } )$

![](/api/attachments/4WUBVYAF/fulltext/images/60af98bfe3c508f8f5069d748474ce965a8676b3dd7724cd6ba65288efa274ed.jpg)  
Figure 2. Decision Tree of a Base Customer Under the Referral-Upgrade Program

We next derive a referred customer’s purchasing probability ??. The payoffs of a ??-type referred customer from purchasing a basic product and a full-version product (the basic version plus the upgrade) are $U _ { R } ^ { b } ( v ) \triangleq \theta v - p _ { B }$ and $U _ { R } ^ { f } ( v ) \triangleq v -$ $p _ { B } - p _ { U } ,$ respectively. Let $U _ { R } ( v ) \triangleq \operatorname* { m a x } \{ U _ { R } ^ { b } ( v ) , U _ { R } ^ { f } ( v ) \}$ . The referral is successful if $U _ { R } ( v ) \geq 0$ . Thus,

$$
\begin{array}{r} q = \mathbb {P} \{U _ {R} (v) \geq 0 \} = \mathbb {P} \bigl \{U _ {R} ^ {b} (v) \geq \max \bigl \{0, U _ {R} ^ {f} (v) \bigr \} \bigr \} \\ + \mathbb {P} \bigl \{U _ {R} ^ {f} (v) \geq \max \{0, U _ {R} ^ {b} (v) \} \bigr \} \triangleq q _ {R} ^ {b} + q _ {R} ^ {f}. \end{array}
$$

The firm’s expected total profit under the referral-upgrade program can be formulated as

$$
\begin{array}{r l} \underset {\theta , p _ {B}, p _ {U}} {\text {Max}} & \Pi (p _ {B}, p _ {U}, \theta) = q _ {B} p _ {B} + q _ {B} p _ {U} [ \beta + \alpha (1 - q) \gamma ] + q _ {B} \alpha [ p _ {B} q _ {R} ^ {b} + (p _ {B} + p _ {U}) q _ {R} ^ {f} ] \\ \text {s.t.} & \theta v _ {0} - p _ {B} + \max \{0, U ^ {u} (v _ {0}), U ^ {r} (v _ {0}) \} = 0, \\ & q _ {B} = F ^ {c} (v _ {0}), \\ & q = q _ {R} ^ {b} + q _ {R} ^ {f}, \\ & \alpha = \mathbb {P} \{U ^ {r} (V) \geq \max \{U ^ {u} (V), 0 \} | V \geq v _ {0} \}, \\ & \beta = \mathbb {P} \{U ^ {u} (V) \geq \max \{U ^ {r} (V), 0 \} | V \geq v _ {0} \}, \\ & \gamma = \mathbb {P} \{U ^ {u} (V) \geq 0 | U ^ {r} (V) \geq \max \{U ^ {u} (V), 0 \}, V \geq v _ {0} \}, \end{array} \tag {4}
$$

where $U ^ { u } ( v )$ and $U ^ { r } ( v )$ are defined in Equations (2) and (3), respectively.

In the formulation of Equation (4), ?? denotes the probability that a purchasing base customer will make a referral (attempting to get a free upgrade), ?? represents the probability that a purchasing base customer will directly pay to upgrade (without referring), and ?? represents the conditional probability that a base customer who attempted a referral but failed and will pay to upgrade later. The following lemma reveals a structural property of ?? and ?? under the firm’s optimal pricing and quality decisions.

Lemma 1: Under the referral-upgrade program, it holds that either ?? = 0 or $\beta = 0$ under the firm’s optimal pricing and quality decisions.

Lemma 1 suggests that it is never optimal to simultaneously induce some base customers to refer and others to pay to upgrade. Indeed, the firm contemplates two candidate approaches to jointly manage referrals and versioning: a referral-driven approach $( \alpha > 0 )$ focusing on expanding market reach, and a direct-upgrade approach $( \beta > 0 )$ aiming to extract immediate profit from existing customers through upgrade purchases. These approaches are reflective of fundamentally different segmentation logics, and mixing them (i.e., ?? > 0 and $\beta > 0 )$ undermines the effectiveness of each. The firm thus prioritizes one approach at a time, ensuring that all base customers make a clear and consistent upgrade choice.

Although directly solving Equation (4) is not analytically tractable, the following result demonstrates the superior performance of the referral-upgrade program to the referralreward program, complemented by Figure 3 that provides a graphical illustration of how these two referral programs compare in profits.

Proposition 2: The referral-upgrade program always yields a weakly higher profit than the referral-reward program. In particular, the profit is strictly higher under the referralupgrade program when $c < 1 / 4$

![](/api/attachments/4WUBVYAF/fulltext/images/9a9e07efb584f863d5b7e0fd59d3c3c8e6f231ec4c5e4508204d84784dfd94ae.jpg)  
Figure 3. Profit Comparison Between the Referral-Reward and Referral-Upgrade Programs

In proving Proposition 2, we consider a linear pricing scheme under the referral-upgrade program, i.e., $p _ { B } = p \theta$ and $p _ { U } =$ $p ( 1 - \theta )$ , where ?? denotes the price of the full-version product, and show that it (weakly) outperforms the referralreward program in terms of expected total profit. Specifically, we construct a feasible solution with $p = 1 / 2$ and $\theta =$ $\sqrt { 2 - 4 c } - 1$ for $c < 1 / 4$ , and show this always generates referrals and yields a strictly higher profit than the referralreward program.

To explain Proposition 2, especially on the profitability of fine-tuned quality incentives, recall that the referral-upgrade program induces heterogeneous referral incentives among base customers differentiated by their types. In general, customers who purchase the basic product have higher valuations for both the basic product and the optional upgrade. In this way, the purchase decision of the basic product serves as a screening mechanism to price out low-valuation customers, and this creates room for designing efficient referral incentives. Specifically, only high-valuation customers will survive this screening, and they become the firm’s favorable targets to generate referrals. Their highvaluation nature suggests that giving out a free upgrade equivalent to a portion of quality is sufficient to compensate for these customers’ referral costs and justify their referral actions.

In addition, the referral-upgrade program benefits from the opportunity of selling the incremental upgrade to customers whose referral attempts have failed, but this also creates a direct pay-to-upgrade option that adversely affects base customers’ referral incentives. To stimulate referrals, the quality of upgrades must be adjusted upward so that the referral option has sufficient appeal and can dominate nonreferral options. Hence, for a referral-upgrade program to be profitable, it must balance two opposing effects that arise simultaneously from an affordable pay-to-upgrade option. Nevertheless, by properly pulling the price-and-quality levers, it is possible to achieve better profits under the referralupgrade program.

Our result resonates with some real-world observations. For certain digital products or services (e.g., Dropbox or Spotify), firms often link referral incentives to product upgrades rather than cash rewards, likely because customers with higher valuations, such as those with larger storage needs or heavier usage demands, can be more easily motivated by upgrade benefits. The referral-upgrade program naturally targets these high-valuation customers to generate referrals, enabling firms to selectively stimulate referrals without offering identical incentives to low-valuation users. Our analysis sheds light on why such non-monetary referral mechanisms can be more profitable in practice.

## Comparative Statics of Referral-Upgrade Program

To deepen our understanding of the referral-upgrade program, we next examine how the firm and customers adjust their decisions in response to different referral costs. On the demand side, customers’ responses are reflected in their purchasing probability and referral behavior. On the supply side, the firm’s responses are reflected in its price-and-quality design.

![](/api/attachments/4WUBVYAF/fulltext/images/838ae7b6e3088c0ebf544e5daacf623db5e9ef39809a1e1e42389e9836307b49.jpg)  
Figure 4. Firm’s Pricing and Quality Decisions and Customer Behavior Under the Referral-Upgrade Program

For the firm, Figures 4a-4c present its pricing and quality decisions $\left( p _ { B } ^ { * } , p _ { U } ^ { * } , \theta ^ { * } \right)$ as functions of the referral cost ??. These results show that as ?? increases from 0 to 0.2, the quality of the basic product $\boldsymbol { \theta } ^ { * }$ decreases. This occurs because customers are forward-looking and factor the referral benefit into their purchase decisions. A higher referral cost will reduce the net benefit from referrals, and the firm has to increase the quality of the upgrade $1 - \theta ^ { * }$ to attract referrals; accordingly, the firm lowers the quality of the basic product $\boldsymbol { \theta } ^ { * }$ . This leads to a higher price $p _ { U } ^ { * }$ charged for the incremental upgrade and a lower price $\boldsymbol { p } _ { B } ^ { * }$ charged for the basic product. Interestingly, $\theta ^ { * } , ~ p _ { B } ^ { * } ,$ and $p _ { U } ^ { * }$ exhibit nonmonotonic patterns as ?? grows above 0.2 before reaching 0.25 (note that base customers do not refer at all for $c \geq 0 . 2 5 )$ .

The firm’s optimal strategy shifts as the referral cost ?? lies in this regime. When the referral cost is slightly above $0 . 2 ,$ as fewer customers attempt to refer, the firm chooses to partially reverse its earlier strategy. Indeed, only high-valuation customers will attempt to refer due to the high referral cost (a selection effect), and they are willing to upgrade even if their referral attempts have failed. Anticipating this, the firm focuses on extracting value from the basic product—it slightly raises the basic quality $\boldsymbol { \theta } ^ { * }$ , thus tempering the incremental price $p _ { U } ^ { * }$ relative to the monotonic trend. This adjustment, however, disappears as the referral cost further grows; this leads to the observed uptick in $\theta ^ { * }$ and $\boldsymbol { p } _ { B } ^ { * }$ for ?? in the 0.20-0.25 range. In other words, as referral participation dwindles at very high $c ,$ the optimal design transitions towards a no-referral regime, and in this process, it generates a brief reversal in the firm’s quality and pricing choices.

For customers, Figures 4d-4f plot their purchase and referral behavior under different referral costs ??. We numerically find that referrals only occur when the referral cost is low $( \mathrm { i } . \mathrm { e } . , c <$ 0.25). In this case, the firm incentivizes all base customers who purchase the product to make a referral rather than to directly pay to upgrade $( \mathrm { i . e . , } \alpha = 1 , \beta = 0 )$ . Referred customers, on the other hand, consistently opt to purchase the full-version product $( \mathrm { i } . \mathrm { e } . , q _ { R } ^ { b } = 0 )$ . As the referral cost increases, the demand from base customers, $q _ { B } ,$ inevitably declines. However, the probability that base customers will choose to upgrade after unsuccessful referrals, $\gamma ,$ increases with the referral cost. This is due to the aforementioned selection effect: Higher referral costs deter low-valuation customers from making referrals. Only high-value customers make referrals, and their inherent high valuations suggest a higher chance of upgrading even if their referral attempts have failed. We also find that $q _ { R } ^ { f } ,$ , the probability that referred customers will choose to purchase the full-version product, increases with the referral cost.

## Extensions

To comprehensively examine the robustness of our main result on the profitability of upgrade-based incentives, we consider four model extensions, each relaxing one assumption of the base model while fixing the others. Some confirm our main result, whereas others generate new insights that complement our main result. In the Boundedly Rational Customers section, Marginal Costs section, and Heterogeneous Referral Costs section, we maintain the assumption that each base customer can refer only once, but relax other assumptions concerning customer rationality, marginal costs, and referral costs. In the Multiple Referrals section, we expand the referral structure’s breadth by allowing each base customer to refer multiple friends with possible overlapping friends. These extensions enabled us to assess the robustness of our main result across a variety of realistic settings.

## Boundedly Rational Customers

In the base model, we assume that base customers are fully rational, i.e., they are forward-looking and form rational expectations of their referral outcomes (Lobel et al., 2017; Yang & Debo, 2019). This assumption allows base customers to potentially purchase a product even if the immediate payoff from purchasing this product is negative, as it can be outweighed by future referral benefits. In this extension, we relax this assumption and consider base customers who are boundedly rational. Specifically, customers are myopic, i.e., they purchase a product if and only if their stand-alone valuations of the product meet or exceed the price, without factoring in potential gains from future referrals. In other words, referral decisions are only made post-purchase. With myopic customers, under the referral-reward program, the demand from base customers is revised to: $q _ { B } = \mathbb { P } \{ V \geq p \} = F ^ { c } ( p )$ (recall this demand is $q _ { B } = F ^ { c } ( p - ( q r - c ) ^ { + } )$ in the base model). Under the referral-upgrade program, the demand from base customers is revised $\mathrm { t o } \colon ^ { 1 1 } q _ { B } = \mathbb { P } \{ \theta V \geq p _ { B } \} = F ^ { c } ( p _ { B } / \theta )$ (recall that this demand is $q _ { B } = F ^ { c } ( v _ { 0 } )$ in the base model, where $v _ { 0 }$ solves $\theta v _ { 0 } - p _ { B } + \operatorname* { m a x } \{ 0 , U ^ { u } ( v _ { 0 } ) , U ^ { r } ( v _ { 0 } ) \} = 0 )$

Proposition 3: When base customers are boundedly rational in anticipating their referral decisions, the referral-upgrade program yields a weakly higher profit than the referralreward program.

Proposition 3 shows that the profitability of the referral-upgrade program does not hinge on customers’ forward-looking purchase and referral behaviors. Instead, it arises from this program’s capacity to induce heterogeneous referral incentives. By rewarding successful referrals with a quality-based upgrade whose value depends on the referring customer’s type, the referral-upgrade program can target high-valuation customers exclusively to generate referrals. This targeting remains viable even when base customers are myopic. In contrast, the referralreward program offers a fixed monetary incentive, independent of customer valuations, thus failing to exploit the underlying customer heterogeneity. Because customers’ referrals occur after their purchase under both programs, the relative advantage of the upgrade program will persist.

This extension has clear practical relevance. In many markets, especially those of low-cost digital goods, customers often purchase impulsively, without factoring in future benefits that arise from referrals or upgrades. Our finding that referralupgrade programs remain more profitable under such bounded rationality of customers suggests that firms in these markets can still rely on quality-based incentives to design referral programs, without requiring their customers to be fully forwardlooking. This also suggests that firms need not invest heavily to educate their customers upfront about future referral benefits.

## Marginal Costs

In the base model, we assume the firm has a negligible marginal cost of offering each product, regardless of its quality—a common feature of many digital products or services such as Spotify (removing built-in ads to enhance quality). In other contexts, such as CloudMe,<sup>12</sup> Hivenet,<sup>13</sup> or Dropbox, offering a product or service, however, may involve positive marginal costs (e.g., offering additional online storage can generate nonnegligible costs). Motivated by such contexts, we extend our base model to incorporate marginal costs. For simplicity, we assume a linear cost structure, that is, the marginal cost of offering a product with quality ?? is ???? for some $k \geq 0$ . This assumption also aligns in spirit with cloud storage platforms, where service quality generally scales with storage consumption. We aim to understand how marginal costs will affect the profit comparison between the two referral programs.

Under the referral-reward program, due to the marginal costs, the firm optimally chooses the product quality (i.e., the quality ?? is a decision variable). We present the firm’s optimal priceand-quality decisions in Proposition B1 in Appendix B.

![](/api/attachments/4WUBVYAF/fulltext/images/a7c32da9f3ea6f52cca67495d248188fe3de90f0b795273a1297ac6ad51010a8.jpg)  
Figure 5. Profit Comparison Between Referral-Reward and Referral-Upgrade Programs under Linear Marginal Costs: Relative Difference (%), Referral-Upgrade to Referral-Reward

Under linear marginal costs, we find that the firm continues to sell the full-version product $( \mathrm { i } . \mathsf { e } . , \theta ^ { * } = 1 )$ to all customers under the referral-reward program. In this setting, increasing the quality leads to a proportional increase in both customers’ willingness to pay for a product and its production cost. Because customers’ willingness to pay scales linearly with quality, the firm can adjust prices accordingly to offset the extra cost from increased quality, while maintaining sufficient profitability. This ensures that there is no diminishing return from increased product quality; the firm thus optimally sets the highest quality level.

The firm’s optimal strategy under the referral-upgrade program is analytically intractable; we solve it numerically. We find that the referral-upgrade program continues to outperform the referral-reward program in profits. Figure 5 presents the relative profit difference between these two referral programs under different marginal costs ??. The numerical results show that when the referral cost is low, a higher marginal cost can lead to a significant profit advantage from the referral-upgrade program. With a high marginal cost, the referral-upgrade program lowers the quality of the basic product; this enhances the quality differentiation between the two versions of the products and partially mitigates the adverse effect of higher marginal costs. However, when the referral cost is high, a higher marginal cost can result in a lower relative profit gain. In this case, referrals occur less often, weakening the profitability of both referral programs. The advantage of the upgrade program attenuates more, particularly when marginal costs are high, because upgrade-based differentiation becomes prohibitively costly.

This extension highlights the practical significance of marginal costs in designing referral programs. For digital products such as mobile apps and streaming services, incremental quality improvements (e.g., removing ads, unlocking premium features) are almost costless, making referral-upgrade programs particularly attractive. However, for products where higher quality entails real costs, the firm should consider balancing upgrade generosity against costs. Our results can help managers tailor referral incentives to their product’s cost nature, necessitating or avoiding generous upgrades in environments featuring different cost structures.

## Heterogeneous Referral Costs

In the base model, we assume a homogeneous referral cost across base customers. In practice, people with higher valuations (e.g., those with higher incomes) are likely to feel relatively higher psychological costs from making referrals, i.e., there can be a positive correlation between customers valuations and their referral costs. To capture this correlation, in this extension, we consider a ??-type base customer’s referral cost in the form of $c ( v ) = \eta v + c _ { 0 } .$ , where $\eta \in [ 0 , 1 ]$ captures the degree of heterogeneity in base customers’ mental or psychological costs of making referrals, and $c _ { 0 } > 0$ represents a fixed cost driven by the intrinsic nature of the referral program (e.g., the convenience of making a referral and receiving referral rewards). Note that when $\eta = 0$ , this model reduces to the base model with homogeneous referral costs.

(a) η =0.1  
![](/api/attachments/4WUBVYAF/fulltext/images/f2e33d30bcadc550ec665bce25c2ffdd7193fe9c3c77a6eae7a4c445c7a0af24.jpg)

(c) η =0.5  
![](/api/attachments/4WUBVYAF/fulltext/images/a83006e9b1189cdf6aef9590251f216e1181ac1b58c4c1a2b98938dd91133e6d.jpg)

(b) η =0.3  
![](/api/attachments/4WUBVYAF/fulltext/images/83ae7f77e213c9065f33db14dd4b6e9981f9672c2e7873c46d646e5f2b4e6dc3.jpg)

(d) η =0.7  
![](/api/attachments/4WUBVYAF/fulltext/images/6d1ac82f6b487348c7c29199ae2493b596d150a6089219344d0b5abee3098b8a.jpg)

Figure 6. Profit Comparison Between the Referral-Reward and Referral-Upgrade Programs Under Heterogeneous Referral Costs

We numerically solve for the firm’s optimal decisions under both the referral-reward and referral-upgrade programs. Figure 6 shows the profit comparison between these two programs under varying degrees of heterogeneity $\eta$ and fixed referral costs $c _ { 0 } .$ . The results show that when heterogeneity in referral costs is limited (i.e., small ??), the referral-upgrade program consistently outperforms the referral-reward program across all levels of $c _ { 0 } .$ , echoing the key result from the base model.

As a departure from the base model, we find that the advantage of the referral-upgrade program diminishes as the degree of heterogeneity ?? increases. Specifically, under large ??, referralupgrade remains superior when $c _ { 0 }$ is low, but it can fall short when $c _ { 0 }$ is high. Recall from the base model that referralupgrade unambiguously dominates referral-reward, as the former can efficiently exploit customer heterogeneity in valuations to design quality-based incentives. The referralreward program, however, provides an identical monetary incentive independent of customer valuation, thus not fully capturing the inherent valuation heterogeneity. However, when the referral cost is correlated with the customer valuation, the referral-reward program is able to utilize the heterogeneity in customer valuation (through the referral cost).

When both the degree of heterogeneity ?? and the fixed referral cost $c _ { 0 }$ are large, the referral costs rise substantially, especially for high-valuation customers. Under these circumstances, the referral-upgrade program encounters structural limitations, as its incentive scheme is capped by product design constraints (i.e., the total product quality is bounded, $\theta \leq 1 )$ . This may fail to offer sufficiently strong incentives to high-valuation customers who also bear higher referral costs under the referral-upgrade program. In contrast, the referral-reward program gains a relative advantage due to its flexibility in monetary incentives (all $r \geq 0$ are feasible). Thus, referral incentives can be better designed to match referral costs. Figures 6c and 6d further indicate that, when ?? is high, the referral-reward program can maintain referrals under a wider range of $c _ { 0 }$

These findings suggest that while the referral-upgrade program can be effective when referral costs exhibit small variations across customers, its advantage may diminish when referral costs are sufficiently heterogeneous and highly correlated with customer valuations. In this latter case, the firm may find monetary-based referral incentives more robust and resilient; they can be tailored to offset the growing referral burden faced by high-valuation customers.

This extension underscores an important practical nuance: In some markets, customers who value upgrades the most may also face the highest barriers to referring others. Examples include enterprise software clients restricted by procurement rules or luxury brand customers who are reluctant to share exclusive experiences. Our analysis suggests that in such settings, the profit advantage of referral-upgrade programs may erode, and monetary rewards could be more effective. Indeed, managers should diagnose referral frictions across customer segments: If high-valuation users are unlikely to refer, a hybrid or monetary scheme may better capture referrals from this group. This insight helps firms avoid overreliance on upgrade incentives in markets where key segments are less likely to participate in referrals.

## Multiple Referrals

Our base model assumes that each base customer can make at most one referral. In this extension, we relax this assumption by allowing each base customer to make up to ?? referrals, where ?? can be interpreted as the number of a base customer’s friends available for referrals. This effectively expands the breadth of the referral structure in the base model. We continue to assume that only base customers can make referrals and that each referral attempt incurs a separate cost ??. A new factor considered in this setting is that base customers’ social circles may overlap, leading to redundant referrals. To capture this redundancy, we follow Kornish and Li (2010) and let the parameter $\delta \in ( 0 , 1 ]$ represent the probability that a referral will reach a friend who has not already been referred (i.e., degree of nonoverlapping). A larger value of ?? reflects broader, less overlapping social networks, whereas a smaller ?? indicates greater redundancy among potential referrals. Naturally, this setting subsumes the base model as a special case with ?? = 1 and ?? = 1.

## Referral-Reward Program

Under the referral-reward program, the firm sells a fullversion product (with quality 1) to all customers and provides each base customer with a fixed monetary reward ?? for every successful referral.<sup>14</sup> For a purchasing base customer, the utility of making each referral is $\delta q r - c ,$ as ?? denotes the probability that the referral will reach a friend who is unaware of the product, and $q = F ^ { c } ( p )$ represents the probability that the friend will buy the product. Because this utility is independent of the customer’s type and the number of referrals the customer has made, each base customer will make ?? referrals, if any. Thus, a base customer’s payoff from purchasing the full-version product is $U _ { B } ( v ) = v -$ $p + D ( \delta q r - c ) ^ { + }$ . Those with $U _ { B } ( v ) \geq 0$ will purchase. The firm solves

$$
\begin{array}{r l} \underset {p, r} {\max} & \Pi (p, r) = q _ {B} p + (p - r) q _ {B} D \delta q \cdot \mathbf {1} _ {\{\delta q r \geq c \}} \\ \mathrm{s.t.} & q _ {B} = F ^ {c} (p - D (\delta q r - c) ^ {+}), \mathrm{and} q = F ^ {c} (p). \end{array}
$$

## Referral-Upgrade Program

Under the referral-upgrade program, the firm sells a basic product with quality $\theta _ { B }$ at price $p _ { B }$ to base customers and invites each purchasing customer to make up to ?? referrals. Let $\pmb { \theta } \triangleq ( \theta _ { 1 } , \theta _ { 2 } , \ldots , \theta _ { D } )$ and $\pmb { p } \triangleq ( p _ { 1 } , p _ { 2 } , \hdots , p _ { D } )$ denote the quality of the increments and their prices associated with the first to the last $D ^ { t h }$ successful referrals. Base customers can upgrade to a full-version product for free only if all their ?? referrals have succeeded. Alternatively, base customers who have purchased the basic product may selectively purchase incremental upgrades at a price $p _ { i }$ for $1 \leq i \leq D$ , and this decision can occur either before or after her referral attempts.

In principle, the optimal referral-upgrade program would require jointly optimizing over qualities and prices of each incremental upgrade (that are not necessarily proportional to each other). This would significantly increase the model’s complexity. To gain tractable and actionable insights, we choose to analyze a special pricing scheme and study its performance numerically. Under this scheme, the firm sets the basic product at a quality $\theta _ { B }$ and price $p _ { B } .$ . All incremental upgrades have equal size in price and quality: each of them has quality $( 1 - \theta _ { B } ) / D$ and is priced at $p _ { U } / D$ . Under this scheme, a ??-type base customer’s expected utility of making one referral is $\delta q ( 1 - \theta _ { B } ) v / D - c + ( 1 - \delta q ) [ ( 1 - \theta _ { B } ) v -$ $p _ { U } ] ^ { + } / D$ , where ?? denotes the probability that the referred friend will make a purchase. The utility of directly paying for an incremental upgrade is $\big [ ( 1 - \theta _ { B } ) v - p _ { U } \big ] / D$ . Because both utilities depend on the customer’s type ??, irrespective of the number of referral attempts she has made, each base customer will make ?? referral attempts provided that she is willing to make the first referral. We remark that key insights obtained under this simple pricing scheme can carry over to more general pricing schemes, as will be explained shortly.

We compare the firm’s profits under two referral programs as we vary $c \in \{ 0 . 0 3 , 0 . 0 5 \}$ and report their relative difference in Table 3. Interestingly, we observe a non-negligible portion of parameter space in which either referral strategy can dominate the other under both referral costs.<sup>15</sup> We observe that the referral-upgrade program generally outperforms referralreward when the number of referrals ?? is low, the referral cost ?? is small, and the non-overlapping degree ?? is high. The referral-reward program may outperform otherwise. Moreover, the relative profit difference between these two referral programs is non-monotone in ??, and gains from referralupgrade are most salient under intermediate values of ??. This suggests that firms may consider capping the number of referrals allowable to each referring customer when offering upgrade-based referral incentives. Indeed, consistent with such a prescription, the music streaming platform Spotify originally did not set any limit on the number of its users’ referrals but later changed its policy and restricted this number to five.<sup>16</sup>

Although the above results are established under the assumption that each incremental upgrade has an equal size in quality and price, we believe that the insight that the referralreward program may outperform the referral-upgrade program in the multi-referral case can extend to other more sophisticated pricing schemes. The reasoning is that under referral-upgrade, each referral attempt must be compensated by sufficient upgrade incentives. This is especially the case when ?? is large and ?? is small, both making referrals costly to maintain. When the referral cap ?? is large, the total available upgrade (with quality $1 - \theta _ { B } )$ must be divided across multiple referrals, thereby diluting the strength of each individual incentive. In contrast, referral-reward compensates for each successful referral with a separate monetary reward and thus remains immune to this dilution.

Our results in this section shed light on the discrepancy in referral programs observed in real-world contexts. For digital goods such as software and cloud services (e.g., Spotify and Dropbox), the referral cost is relatively low because referral requests can be conveniently made in seconds using emails or text messages that include all self-contained information. Under low referral costs, firms tend to use the referral-upgrade program, which is particularly useful at the product launch stage, when the product is less known to the public and there are small overlaps in base customers’ friends (i.e., high ??). In contrast, the credit card business is relatively saturated, and base customers are less likely to find friends who are not familiar with such a business. Moreover, unlike digital products for which both referral requests and compensations can be made instantly, the referral procedure of credit cards is generally more time-consuming and relies on interpersonal word-of-mouth communication for information dissemination (i.e., high ??). In this case, referral-reward may emerge as a better strategy if customers are allowed to refer multiple friends.

This extension has practical relevance. Multi-referral strategies are typically adopted by companies aiming for rapid customer acquisition, especially in early-stage markets or for products where customer networks do not significantly overlap. Singlereferral (or better interpreted as “highly limited referrals”) strategies are commonly observed in mature or saturated markets, where extensive customer-network overlap diminishes returns from additional referrals. In general, they represent different real-world promotional strategies depending on a firm’s growth stage, customer-network characteristics, and market saturation.

Table 3. Profit Comparison Between the Referral-Reward and Referral-Upgrade Programs Under Multiple Referrals

<table><tr><td> $\delta/D$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>1</td><td>+3.85</td><td>+15.17</td><td>+19.68</td><td>+21.13</td><td>+22.10</td><td>+22.86</td><td>+22.39</td><td>+20.83</td></tr><tr><td>0.8</td><td>+3.22</td><td>+12.83</td><td>+16.13</td><td>+17.59</td><td>+18.62</td><td>+18.69</td><td>+17.11</td><td>+14.36</td></tr><tr><td>0.6</td><td>+2.44</td><td>+9.66</td><td>+11.86</td><td>+13.09</td><td>+13.77</td><td>+12.10</td><td>+8.65</td><td>+3.87</td></tr><tr><td>0.4</td><td>+1.46</td><td>+5.22</td><td>+6.60</td><td>+7.38</td><td>+5.20</td><td>+0.20</td><td>-7.23</td><td>-19.31</td></tr><tr><td>0.2</td><td>+0.30</td><td>+0.77</td><td>+0.59</td><td>-7.90</td><td>-17.12</td><td>-19.92</td><td>-22.55</td><td>-25.02</td></tr></table>

?? = ??. ????

<table><tr><td>δ/D</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>1</td><td>+3.30</td><td>+12.15</td><td>+14.17</td><td>+15.13</td><td>+15.51</td><td>+13.27</td><td>+9.10</td><td>+3.60</td></tr><tr><td>0.8</td><td>+2.63</td><td>+9.30</td><td>+10.87</td><td>+11.88</td><td>+10.62</td><td>+6.30</td><td>-0.13</td><td>-8.10</td></tr><tr><td>0.6</td><td>+1.80</td><td>+5.81</td><td>+6.98</td><td>+7.05</td><td>+2.71</td><td>-5.15</td><td>-18.00</td><td>-36.08</td></tr><tr><td>0.4</td><td>+0.81</td><td>+2.23</td><td>+2.72</td><td>-1.63</td><td>-17.57</td><td>-38.96</td><td>-42.77</td><td>-46.14</td></tr><tr><td>0.2</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>

Note: relative difference (%) from referral-upgrade to referral-reward

<sup>15</sup> The relative difference of 0% under ?? = 0.05 corresponds to the case in which neither referral program generates referrals so that the firm achieves the usual monopoly profit under both programs.

<sup>16</sup> See the article, “Spotify: Why They Changed Their Referral Program” (https://www.osiaffiliate.com/marketing/spotify-referral-program). As Spotify starts to gain market dominance, it has shifted its promotion strategy and discontinued its referral program.

Our results support this intuition: In environments where customer networks are largely distinct and non-overlapping, allowing multiple referrals can significantly boost profitability by efficiently expanding customer reach. However, in high-overlap markets, where friend circles are tightly interconnected or the audience is largely saturated, excessive referrals dilute incentive power and lead to sharply diminishing incremental returns. This insight informs important managerial tradeoffs: firms targeting untapped or emerging networks should embrace generous multiplereferral schemes, while those in mature or overlap-heavy sectors should carefully consider limited referrals to maintain effectiveness.

In practice, referral limits can help mitigate diminishing returns, as observed with Spotify<sup>17</sup> and Dropbox.<sup>18</sup> Indeed, managers should closely monitor the incremental performance of referrals: if the value derived from each additional referral begins to decline significantly, it indicates a need to tighten referral caps. Carefully diagnosing the degree of network overlap and referral saturation before program launch can ensure that referral designs align effectively with both growth objectives and cost efficiency.

To further deepen our understanding of the multi-referral strategy proposed in this section, we analyzed its comparative statics under the referral-upgrade program, relegating the full details to Appendix C for brevity.

## Conclusion

This paper developed a theoretical framework to compare two commonly used referral programs in practice: the traditional referral-reward program, which offers monetary compensation for successful referrals, and the increasingly popular referral-upgrade program, which incentivizes referrals through non-monetary upgrade rewards. Our analysis revealed that the referral-upgrade program can outperform the referral-reward program by leveraging customer heterogeneity for better design of referral incentives. Specifically, when customers are heterogeneous in their valuations, upgrade-based incentives induce incentive discrimination, naturally encouraging highvaluation customers—who value upgrades more—to make referrals, enabling better market segmentation.

We extended our base model to incorporate several practically relevant factors, including bounded rationality, positive marginal costs, heterogeneous referral costs, and multiple referrals. Our results indicated that the superiority of referral-upgrade programs is robust to these behavioral, structural, and cost-related variations in real-world markets. We also identified boundary conditions under which referral-upgrade programs can actually fall short. Specifically, when referral costs are highly correlated with customer valuations, or when the firm invites each customer to make too many referrals, referral-upgrade programs must be exercised with caution due to their inherent limitations.

Overall, this paper provides a new perspective on the incentive design in referral programs, highlighting how firms should adapt referral incentives to environments characterized by customer heterogeneity and different levels of referral reachability.

## Managerial Implications

Our findings translate into several managerial implications. First, firms with highly heterogeneous customer bases, particularly those offering digital products with low marginal costs, can significantly benefit from implementing referral-upgrade programs. This is because upgrade incentives naturally encourage self-selection—customers who value the product’s premium features more highly are especially motivated to refer friends in exchange for an upgrade. This built-in incentive discrimination means that firms with a tiered product (or freemium model) can leverage referral-upgrade programs to tap their most enthusiastic, high-value customers as “evangelists,” achieving more efficient market segmentation without incurring the higher direct monetary costs associated with referral-reward programs. However, our findings also suggest caution: Managers should carefully monitor situations where referral costs strongly correlate with customer valuations (e.g., high-valuation customers face high costs to refer), as the advantage of upgrade incentives can erode. In such cases, firms might need to supplement upgrade incentives with other encouragement or consider monetary incentives for harder-to-reach customer segments. Additionally, firms should avoid overly broad referral schemes that encourage excessive referrals from individual customers—the incremental referrals may overlap or dilute the incentive effect, a phenomenon of “incentive dilution” where additional referral opportunities yield diminishing returns. Managers should thus consider capping the number of referrals per customer.

## Future Research Directions

Our study opens several avenues for future research. First, our model focused on settings where customers’ benefits from referrals are private—their payoffs only depend on their own consumption. However, in many markets, especially those involving digital services and platforms, customer utilities may also depend on the total number of adopters—a phenomenon commonly known as network effects. Integrating this effect with the incentive design in referral programs presents a promising direction for future research.

Second, this paper focused on referral programs where each successful referral generates a deterministic reward (either monetary or upgrade-based). In practice, some platforms adopt more complex, goal-oriented referral schemes, such as groupbuying types of programs. In these programs, customers are compensated only when they have accumulated multiple successful referrals to reach a specific target, often under uncertain or dynamic contribution rules. Exploring how such cumulative and probabilistic referral mechanisms will affect customer incentives and the firm’s profit would be an interesting direction for future research.

Finally, extending our monopoly model to competitive settings, where multiple firms simultaneously deploy referral programs, may yield new insights. The role of referral-upgrade programs as a differentiation strategy against competitors’ referral-reward programs, or vice versa, may have surprising effects that are moot in a monopoly analysis. Capturing such effects in a competitive model constitutes another important and practically relevant direction for future study.

## Acknowledgments

We would like to thank the senior editor, the associate editor, and the three anonymous reviewers for their constructive comments and suggestions. The first two authors contributed equally to this research and are thus co-first authors. C. Jin received financial support from the Singapore Ministry of Education Academic Research Fund Tier 1 (T1251RES2101). Y.-J. Chen received financial support from the Hong Kong Research Grants Council (C6020-21GF) and General Research Fund (16501722 and 16204521).

## References

Belo, R., & Li, T. (2022). Social referral programs for freemium platforms. Management Science, 68(12), 8933-8962. https://doi.org/10.1287/mnsc.2022.4301

Bhargava, H. K., & Choudhary, V. (2008). Research note—When is versioning optimal for information goods? Management Science, 54(5), 1029-1035. https://doi.org/10.1287/mnsc.1070.0773

Biyalogorsky, E., Gerstner, E., & Libai, B. (2001). Customer referral management: Optimal reward programs. Marketing Science, 20(1), 82-95. https://doi.org/10.1287/mksc.20.1.82.10195

Chellappa, R. K., & Mehra, A. (2018). Cost drivers of versioning: Pricing and product line strategies for information goods. Management Science, 64(5), 2164-2180. https://doi.org/10.1287/ mnsc.2016.2698

Desai, P. S. (2001). Quality segmentation in spatial markets: When does cannibalization affect product line design? Marketing Science, 20(3), 265-283. https://doi.org/10.1287/mksc.20.3.265. 9767

Fernández-Loría, C., Cohen, M. C., & Ghose, A. (2023). Evolution of referrals over customers’ life cycle: Evidence from a ride-sharing platform. Information Systems Research, 34(2), 698-720. https://doi.org/10.1287/isre.2022.1138

Hong, Y., Pavlou, P. A., Shi, N., & Wang, K. (2017). On the role of fairness and social distance in designing effective social referral systems. MIS Quarterly, 41(3), 787-809. https://doi.org/10.25300/ MISQ/2017/41.3.06

Iyengar, S. S., & Lepper, M. R. (2000). When choice is demotivating: Can one desire too much of a good thing? Journal of Personality and Social Psychology, 79(6), 995-1006. https://doi.org/10.1037/ 0022-3514.79.6.995

Jing, X., & Xie, J. (2011). Group buying: A new mechanism for selling through social interactions. Management Science, 57(8), 1354- 1372. https://doi.org/10.1287/mnsc.1110.1366

Jung, J., Bapna, R., Golden, J. M., & Sun, T. (2020). Words matter! Toward a prosocial call-to-action for online referral: Evidence from two field experiments. Information Systems Research, 31(1), 16-36. https://doi.org/10.1287/isre.2019.0873

Kornish, L. J., & Li, Q. (2010). Optimal referral bonuses with asymmetric information: Firm-offered and interpersonal incentives. Marketing Science, 29(1), 108-121. https://doi.org/ 10.1287/mksc.1080.0484

Lahiri, A., & Dey, D. (2018). Versioning and information dissemination: A new perspective. Information Systems Research, 29(4), 965-983. https://doi.org/10.1287/isre.2017.0763

Libai, B., Biyalogorsky, E., & Gerstner, E. (2003). Setting referral fees in affiliate marketing. Journal of Service Research, 5(4), 303-315. https://doi.org/10.1177/1094670503005004003

Lobel, I., Sadler, E., & Varshney, L. R. (2017). Customer referral incentives and social media. Management Science, 63(10), 3514- 3529. https://doi.org/10.1287/mnsc.2016.2476

Mendelson, H., & Parlaktürk, A. K. (2008). Product-line competition: Customization vs. proliferation. Management Science, 54(12), 2039-2053. https://doi.org/10.1287/mnsc.1080.0935

Moorthy, K. S. (1984). Market segmentation, self-selection, and product line design. Marketing Science, 3(4), 288-307. https://doi.org/10.1287/mksc.3.4.288

Mussa, M., & Rosen, S. (1978). Monopoly and product quality. Journal of Economic Theory, 18(2), 301-317. https://doi.org/ 10.1016/0022-0531(78)90085-6

Qu, X., Lotfi, A., Jain, D. C., & Jiang, Z. (2022). Predicting upgrade timing for successive product generations: An exponential-decay proportional hazard model. Production and Operations Management, 31(5), 2067-2083. https://doi.org/10.1111/poms. 13665

Shi, H., Liu, Y., & Petruzzi, N. C. (2013). Consumer heterogeneity, product quality, and distribution channels. Management Science, 59(5), 1162-1176. https://doi.org/10.1287/mnsc.1120.1604

Simon, H. A. (1955). A behavioral model of rational choice. The Quarterly Journal of Economics, 69(1), 99-118. https://doi.org/ 10.2307/1884852

Sun, T., Viswanathan, S., Huang, N., & Zheleva, E. (2021). Designing promotional incentives to embrace social sharing: Evidence from field and online experiments. MIS Quarterly, 45(2), 789-820. https://doi.org/10.25300/MISQ/2021/15352

Tucker, C. E. (2014). Social networks, personalized advertising, and privacy controls. Journal of Marketing Research, 51(5), 546-562. https://doi.org/10.1509/jmr.10.0355

Villas-Boas, J. M. (1998). Product line design for a distribution channel. Marketing Science, 17(2), 156-169. https://doi.org/ 10.1287/mksc.17.2.156

Xiao, P., Tang, C. S., & Wirtz, J. (2011). Optimizing referral reward programs under impression management considerations. European Journal of Operational Research, 215(3), 730-739. https://doi.org/10.1016/j.ejor.2011.05.042

Yang, L., & Debo, L. (2019). Referral priority program: Leveraging social ties via operational incentives. Management Science, 65(5), 2231-2248. https://doi.org/10.1287/mnsc.2018.3034

## About the Authors

Chenguang (Allen) Wu is an associate professor in the Department of Industrial Engineering and Decision Analytics, Hong Kong University of Science and Technology. He received his Ph.D. from the Department of Industrial Engineering and Management Sciences at Northwestern University. Dr. Wu’s research interests include service operations, bundling, search, and operations and information systems interface. His papers have appeared in journals such as Management Science, Operations Research, Manufacturing & Service Operations Management, Production and Operations Management, and Journal of Management Information Systems. ORCiD: https://orcid.org/0000- 0002-2528-0286

Chen Jin is an associate professor in the Department of Information Systems and Analytics at the School of Computing,

National University of Singapore. He received his Ph.D. from the Department of Industrial Engineering and Management Sciences at Northwestern University. His research focuses on technologydriven consumer behavior and the information systems-operations interface. His work has been published in leading journals such as Management Science, Information Systems Research, Manufacturing & Service Operations Management, Journal of Management Information Systems, and Production and Operations Management. ORCiD: http://orcid.org/0000-0001-9940-0757

Ying-Ju Chen is the Crown Worldwide Professor of Business and a chair professor at HKUST. Previously, he was a faculty member in the Department of IEOR at UC Berkeley. He earned his Ph.D. in operations management from the Stern School of Business at New York University in 2007 and holds master’s and bachelor’s degrees in electrical engineering from National Taiwan University. He is a recipient of the Franklin Prize for Teaching Excellence at HKUST, the NYU Teaching Excellence Award, the “Most Influential Service Operations” and “Best Not-for-Profit Operations Management” paper awards from Production and Operations Management, the Harold W. Kuhn Award from Naval Research Logistics, second place in the INFORMS Junior Faculty Interest Group paper competition, the Higher Education Outstanding Scientific Research Output Award (social science, third prize), and the Harold MacDowell Award from the Stern School. He is ranked No. 3 among operations management researchers worldwide, according to an article in Production and Operations Management (2025). His editorial roles include department editor for Naval Research Logistics and Service Science, and senior/associate editor for Operations Research, Manufacturing & Service Operations Management, and Production and Operations Management. His research interests encompass network economics, socially responsible operations, the operations-marketing interface, and supply chain management. His work has been published in leading journals across various fields. ORCiD: https://orcid.org/0000- 0002-5712-1829

## Appendix A

## Proof of Main Results

## Proof of Proposition 1

Proposition 1 follows from Proposition B.1 by setting $k = 0 .$ . ∎

Proof of Lemma 1

Note that

$$
\begin{array}{l} U ^ {u} (v) = v (1 - \theta) - p _ {U} \geq 0 \Leftrightarrow v \geq \frac {p _ {U}}{1 - \theta} \\ U ^ {r} (v) = q v (1 - \theta) + (1 - q) [ v (1 - \theta) - p _ {U} ] ^ {+} - c \geq 0 \Leftrightarrow \left\{ \begin{array}{l l} v \geq \frac {c}{q (1 - \theta)}, & \text {if} v <   \frac {p _ {U}}{1 - \theta}, \\ v \geq \frac {c + p _ {U} (1 - q)}{1 - \theta}, & \text {if} v \geq \frac {p _ {U}}{1 - \theta}. \end{array} \right. \\ U ^ {u} (v) \leq U ^ {r} (v) \Leftrightarrow \left\{ \begin{array}{l l} v \leq \frac {p _ {U} - c}{(1 - \theta) (1 - q)}, & \text {if} v <   \frac {p _ {U}}{1 - \theta}, \\ q p _ {U} \geq c, & \text {if} v \geq \frac {p _ {U}}{1 - \theta}. \end{array} \right. \end{array}
$$

Hence,

$$
\begin{array}{r l} {U _ {B} (v)} & {= \theta v - p _ {B} + \max \{0, U ^ {u} (v), U ^ {r} (v) \}} \\ & {= \left\{ \begin{array}{l l} {\left\{ \begin{array}{l l} {\theta v - p _ {B},} & {\mathrm{if} v <   \frac {p _ {U}}{1 - \theta},} \\ {v - p _ {U} - p _ {B},} & {\mathrm{if} v \geq \frac {p _ {U}}{1 - \theta},} \end{array} \right.} & {\mathrm{if} p _ {U} <   \frac {c}{q},} \\ {\left\{ \begin{array}{l l} {\theta v - p _ {B},} & {\mathrm{if} v \leq \frac {c}{q (1 - \theta)},} \\ {q v (1 - \theta) + \theta v - p _ {B} - c,} & {\mathrm{if} \frac {c}{q (1 - \theta)} \leq v <   \frac {p _ {U}}{1 - \theta},} \\ {v - p _ {B} - c - p _ {U} (1 - q),} & {\mathrm{if} v \geq \frac {p _ {U}}{1 - \theta}.} \end{array} \right.} & {\mathrm{if} p _ {U} \geq \frac {c}{q}.} \end{array} \right.} \end{array}
$$

When $p _ { U } \ge c / q$ , we have $U ^ { r } ( v ) \geq U ^ { u } ( v )$ for all $\begin{array} { r } { v \ge \frac { c } { q ( 1 - \theta ) } . } \end{array}$ Thus, $\beta = 0$ . When $p _ { U } < c / q$ , it is clear that $\alpha = 0$ . Therefore, we must have either $\alpha = 0$ or $\beta = 0$ under the firm’s optimal pricing and quality decisions. ∎

## Proof of Proposition 2

It suffices to consider linear pricing of quality under referral-upgrade, i.e., $p _ { B } = p \theta$ and ${ p _ { U } = p ( 1 - \theta ) }$ , where ?? is the price of the fullversion product, and show that it outperforms referral-reward. Under linear pricing, we have $U ^ { u } ( v ) = ( v - p ) ( 1 - \theta ) \geq 0 \Leftrightarrow v \geq p$ and $U _ { R } ( v ) \geq 0 \Leftrightarrow v \geq p$ . One can verify that $q = 1 - p = q _ { R _ { 2 } } , q _ { R _ { 1 } } = 0$ , and

$$
U ^ {r} (v) \geq 0 \Leftrightarrow \left\{ \begin{array}{l l} v \geq \frac {c}{q (1 - \theta)}, & \mathrm{if} v <   p, \\ v \geq \frac {c}{1 - \theta} + p (1 - q), & \mathrm{if} v \geq p. \end{array} \right.
$$

Hence,

$$
U ^ {u} (v) \leq U ^ {r} (v) \Leftrightarrow \left\{ \begin{array}{l l} v \leq \frac {p (1 - \theta) - c}{(1 - \theta) (1 - q)}, & \text {if} v <   p, \\ q p (1 - \theta) \geq c, & \text {if} v \geq p. \end{array} \right.
$$

This implies

$$
U _ {B} (v) = \left\{ \begin{array}{l l} \left\{ \begin{array}{l l} \theta (v - p), & \text {if v <   p ,} \\ v - p, & \text {if v\geq p ,} \end{array} \right. & \text {if p<   \frac {c}{q(1 - \theta)} ,} \\ \left\{ \begin{array}{l l} \theta (v - p), & \text {if v\leq\frac {c}{q(1- \theta)} ,} \\ q v (1 - \theta) + \theta (v - p) - c, & \text {if \frac {c}{q(1- \theta)}\leq v <   p ,} \\ v - \theta p - c - (1 - \theta) p (1 - q), & \text {if v\geq p ,} \end{array} \right. & \text {if p\geq\frac {c}{q(1- \theta)}.} \end{array} \right.
$$

Case $\operatorname { 1 : } p \geq { \frac { c } { q ( 1 - \theta ) } } .$ . In this case, note that

$$
\begin{array}{l} q v (1 - \theta) + \theta (v - p) - c \geq 0 \Leftrightarrow v \geq \frac {c + \theta p}{\theta + q (1 - \theta)}, \\ \frac {c + \theta p}{\theta + q (1 - \theta)} > \frac {c}{q (1 - \theta)} \Leftrightarrow p > \frac {c}{q (1 - \theta)} \Leftrightarrow \frac {c + \theta p}{\theta + q (1 - \theta)} <   p. \end{array}
$$

Thus, $\begin{array} { r } { v _ { 0 } = \frac { c + \theta p } { \theta + q ( 1 - \theta ) } \in \left( \frac { c } { q ( 1 - \theta ) } , p \right) } \end{array}$ . This implies that $\alpha = 1 , \beta = 0 .$ , and

$$
\gamma = \mathbb {P} \{U ^ {u} (V) \geq 0 \mid U ^ {r} (V) \geq \max \{0, U ^ {u} (V) \}, V \geq v _ {0} \} = \mathbb {P} \{U ^ {u} (V) \geq 0 \mid V \geq v _ {0} \} = \frac {1 - p}{q _ {B}}.
$$

The firm’s profit is

$$
\begin{array}{r l} \underset {p, \theta} {\max} & \Pi (p, \theta) = p (1 - p + \theta) \left(1 - \frac {c + \theta p}{1 - p + p \theta}\right) + (1 - \theta) p ^ {2} (1 - p) \\ \mathrm{s.t.} & q = 1 - p, q _ {B} = 1 - \frac {c + \theta p}{\theta + q (1 - \theta)}, \mathrm{and} p \geq \frac {c}{q (1 - \theta)}. \end{array}\tag{5}
$$

The last constraint $\begin{array} { r } { p \ge \frac { c } { q ( 1 - \theta ) } } \end{array}$ implies that Problem (5) is feasible only when $c \leq 1 / 4$ . Under $c \leq 1 / 4$ , one can verify that $p = 1 / 2$ and $\theta =$ $\sqrt { 2 - 4 c } - 1$ is a feasible solution to Problem (5), and it generates profit $3 / 4 - c - \sqrt { 2 ( 1 - 2 c ) } / 4$ . Comparing this profit to $( 5 / 4 - c ) ^ { 2 } / 4$ , the optimal profit under referral-reward, we have

$$
\begin{array}{r l} {3 / 4 - c - \sqrt {2 (1 - 2 c)} / 4 > (5 / 4 - c) ^ {2} / 4} & {\Leftrightarrow 3 - 4 c - (5 / 4 - c) ^ {2} > \sqrt {2 (1 - 2 c)}} \\ & {\Leftrightarrow (1 - 4 c) ^ {2} (1 6 c ^ {2} + 5 6 c + 1 7) / 2 5 6 > 0,} \end{array}
$$

which holds trivially for all $c < 1 / 4$

Case $2 \colon p < \frac { c } { q ( 1 - \theta ) } .$ . In this case, we have $U _ { B } ( v ) = \theta ( v - p ) \mathbf { 1 } _ { \{ v < p \} } + ( v - p ) ^ { + }$ . Thus, $v _ { 0 } = p$ so that $\alpha = 0$ and $\beta = 1$ . The firm’s profit is

$$
\begin{array}{r l} \max _ {p, \theta} & \Pi (p, \theta) = p (1 - p) \\ \text {s.t.} & q = 1 - p \text {and} p \leq \frac {c}{q (1 - \theta)}. \end{array}\tag{6}
$$

It is clear that when $c < 1 / 4$ , the firm’s profit is no more than 1/4, so it is dominated by the profit in Case 1. When $c \ge 1 / 4$ , the optima $p ^ { * } = 1 / 2$ generating profit 1/4.

To sum up, when $0 < c < 1 / 4 ,$ the firm’s profit is strictly higher under the referral-upgrade program than under the referral-reward program. When $c \ge 1 / 4$ , the firm has identical profits under the referral-upgrade and referral-reward programs. ∎

## Proof of Proposition 3

Referral-reward: A ?? −type customer will purchase a product if and only if $v \geq p$ and will refer after purchase if and only if $q r - c \geq 0$ , where $q = 1 - p$ . So the firm solves

$$
\begin{array}{r l} & {\underset {0 \leq r \leq p \leq 1} {\max} \Pi (p, r) = q _ {B} \big [ p + (p - r) q \mathbf {1} _ {\{q r \geq c \}} \big ]} \\ & {\mathrm{s.t.} q _ {B} = 1 - p = q.} \end{array}
$$

Case 1: $\pmb { q } = \pmb { 1 } - \pmb { p } \geq c / r$ . In this case, the firm solves max $_ { \cdot c / r } ( 1 - p ) [ p + ( p - r ) ( 1 - p ) ]$ ]. This problem is feasible if and only $\mathrm { i f } r < 1 -$ 0≤??≤??≤1− $c / r \Leftrightarrow r ^ { 2 } - r + c < 0 \Leftrightarrow \big [ 1 - \sqrt { 1 - 4 c } \big ] / 2 < r < \big [ 1 + \sqrt { 1 - 4 c } \big ] / 2 .$ . This requires $c \leq 1 / 4$ . Thus, Case 1 is vacuous if ?? $> 1 / 4$ . For $c \leq 1 / 4 ,$ it is clear that $\Pi ( p , r )$ is decreasing in ??. The constraint $r \leq p \leq 1 - c / r$ implies $\frac { c } { 1 - p } \leq r \leq p .$ This further implies the optimal $\textstyle r ^ { * } = { \frac { c } { 1 - p } }$ . Plugging it into $\Pi ,$ we have $\Pi ( p ) = ( 1 - p ) ( 2 p - c - p ^ { 2 } )$ . The constraint on ?? becomes $\begin{array} { r } { \frac { c } { 1 - p } < p \Leftrightarrow \big [ 1 - \sqrt { 1 - 4 c } \big ] / 2 < p < \big [ 1 + \sqrt { 1 - 4 c } \big ] / 2 } \end{array}$ . First order condition yields $\begin{array} { r } { \frac { d \Pi ( p ) } { d p } = 0 \Rightarrow p _ { 1 } = 1 - \sqrt { 3 ( 1 - c ) } / 3 } \end{array}$ and $p _ { 2 } = 1 + \sqrt { 3 ( 1 - c ) } / 3$ . One can verify that $\left[ 1 - \sqrt { 1 - 4 c } \right] / 2 < p _ { 1 } <$ $\left[ 1 + { \sqrt { 1 - 4 c } } \right] / 2$ for all $c < 1 / 4 ;$ thus, $p _ { 1 }$ is a local maximum and $p _ { 2 }$ is a local minimum

Therefore, in Case 1, for $c \leq 1 / 4 ,$ , we have $\hat { p } = p _ { 1 } \mathrm { a n d } \Pi ( \hat { p } ) = ( 1 - \hat { p } ) ( 2 \hat { p } - c - \hat { p } ^ { 2 } ) = 2 t ^ { 3 } / 2 7 , \mathrm { w h e r e } t \triangleq \sqrt { 3 ( 1 - c ) } .$

Case 2: $\pmb { q } = \pmb { 1 } - \pmb { p } < \pmb { c } / r$ . In this case, the firm solves $\operatorname* { m a x } _ { \operatorname* { m a x } \{ 1 - c / r , r \} \leq p \leq 1 } p ( 1 - p )$ . He can always set $r = 0$ and $p = 1 / 2$ , leading to profit $1 / 4$ Case 2. Recall that $\Pi ( { \hat { p } } ) = 2 t ^ { 3 } / 2 7$ in Case 1 is increasing in ?? and thus decreasing in ??. Further, when $c = 1 / 4 , \Pi ( \hat { p } ) = 1 / 4$

Combining Cases 1 and $^ { 2 , }$ we obtain the firm’s optimal price, reward, and profit as follows

$$
(p ^ {*}, r ^ {*}, \Pi^ {*}) = \left\{ \begin{array}{l l} \left(1 - \sqrt {3 (1 - c)} / 3, c \sqrt {\frac {3}{1 - c}}, 2 (1 - c) \sqrt {3 (1 - c)} / 9\right), & \text { if } 0 \leq c <   1 / 4, \\ (1 / 2, 0, 1 / 4), & \text { if } c \geq 1 / 4. \end{array} \right.
$$

Referral-upgrade: We consider linear pricing of quality under referral-upgrade, i.e., $p _ { B } = \theta p$ and $p _ { U } = ( 1 - \theta ) p$ , where ?? is the price of the fullversion product, and show that it outperforms referral-reward. Under linear pricing, $q = 1 - p = q _ { R _ { 2 } }$ and $q _ { R _ { 1 } } = 0$ . Following a similar analysis in the proof of Proposition 2, we discuss two cases.

Case 1: $\begin{array} { r } { p \ge \frac { c } { q ( 1 - \theta ) } , } \end{array}$ , then $\alpha = \gamma = 1$ and $\beta = 0 . 5 \mathrm { o } ,$ the firm solves

$$
\begin{array}{l} \max _ {p, \theta} \Pi (\theta , p) = (1 - p) p [ 1 + \theta (1 - p) ] \\ \text {s.t.} \theta \leq 1 - \frac {c}{p (1 - p)}. \end{array}
$$

For the feasible set to be non-empty, it must hold that $c \leq 1 / 4 ;$ otherwise, the problem is infeasible.

For $c \leq 1 / 4 .$ with a feasible $\begin{array} { r } { \theta = 1 - \frac { c } { p ( 1 - p ) } , \Pi ( \theta , p ) = ( 1 - p ) p [ 1 + 1 - p - c / p ] = ( 1 - p ) ( 2 p - c - p ^ { 2 } ) } \end{array}$ . Thus, the optimal $\Pi ( \theta ^ { * } , p ^ { * } ) \geq$ $( 1 - p ) ( 2 p - c - p ^ { 2 } )$ . Recall that with $p = p _ { 1 }$ , the latter is the optimal profit under referral-reward. We show $p _ { 1 }$ is a feasible solution under referral-upgrade as it induces $\begin{array} { r } { \theta = 1 - \frac { c } { p _ { 1 } ( 1 - p _ { 1 } ) } \geq 0 } \end{array}$ for $c \leq 1 / 4$ . Indeed, $\begin{array} { r } { 1 - \frac { c } { p ( 1 - p ) } \geq 0 \Leftrightarrow p \in \left[ \left( 1 - \sqrt { 1 - 4 c } \right) / 2 , \left( 1 + \sqrt { 1 - 4 c } \right) / 2 \right] } \end{array}$ . As we plug in $p _ { 1 \cdot }$ , we find

$$
p _ {1} > \left[ 1 - \sqrt {1 - 4 c} \right] / 2 \Leftrightarrow \sqrt {1 - 4 c} > (4 c - 1) / 3 \text {and} p _ {1} <   \left[ 1 + \sqrt {1 - 4 c} \right] / 2 \Leftrightarrow \sqrt {1 - 4 c} <   3.
$$

Both hold trivially as $c \leq 1 / 4$

Case 2: $\begin{array} { r } { p < \frac { c } { q ( 1 - \theta ) } , } \end{array}$ , then $\alpha = \gamma = 0 , \beta = 1$ . So the firm solves

$$
\max _ {p, \theta} \Pi (\theta , p) = (1 - p) p
$$

$$
\mathrm{s.t.} p (1 - p) <   \frac {c}{1 - \theta}.
$$

Note that $\theta = 1 , p = 1 / 2$ is always a feasible solution and generates profit $1 / 4$

To sum up, in both Cases 1 and 2, we can find feasible solutions of linear pricing under referral-upgrade that generate exactly the same profits as those under referral-reward. ∎

## Appendix B

## Results of Referral-Reward Programs Under Linear Marginal Costs

Proposition B1: Under the referral-reward program, with linear marginal costs, the firm’s optimal decisions and profit are

$$
(\theta^ {*}, p ^ {*}, r ^ {*}, \Pi^ {*}) = \left\{ \begin{array}{l l} \bigg (1, \frac {1 + k}{2}, \frac {1 - k}{4} + \frac {c}{1 - k}, \frac {(4 c - 5 + 6 k - k ^ {2}) ^ {2}}{6 4} \bigg), & \mathrm{if} c \leq \frac {(1 - k) ^ {2}}{4}, \\ \bigg (1, \frac {1 + k}{2}, 0, \frac {(1 - k) ^ {2}}{4} \bigg), & \mathrm{if} c > \frac {(1 - k) ^ {2}}{4}. \end{array} \right.\tag{7}
$$

Proof: It is clear that $p \ge \theta \Rightarrow \Pi = 0$ . Thus, we only need to consider $p \leq \theta .$ . With $q = 1 - p / \theta$ , we consider two cases.

Case $\mathbf { 1 } \colon ( p , r , \theta )$ induces $q r < c .$ . The firm can always set $r = 0$ to ensure $q r < c$ for all $c > 0 .$ . In this case, $q _ { B } = ( 1 - p / \theta ) ^ { + } = q$ and $\Pi ( p , \theta ) = ( 1 - p / \theta ) ( p - k \theta )$ . The optimal $\hat { p } = \operatorname* { m i n } \{ \theta ( 1 + k ) / 2 , \theta \}$ . So

$$
\Pi (\theta) = \left\{ \begin{array}{l l} \theta (1 - k) ^ {2} / 4, & \text {if} k <   1, \\ 0, & \text {if} k \geq 1. \end{array} \right. \Rightarrow (\theta^ {*}, p ^ {*}, r ^ {*}, \Pi^ {*}) = \left\{ \begin{array}{l l} (1, (1 + k) / 2, 0, (1 - k) ^ {2} / 4), & \text {if} k <   1, \\ (0, 0, 0, 0), & \text {if} k \geq 1. \end{array} \right.
$$

Case $\smash { 2 \colon ( p , r , \theta ) }$ induces $q r \geq c .$ In this case, $q _ { B } = \mathbb { P } \{ V \geq [ p - ( q r - c ) ] ^ { + } / \theta \}$ . Because $q r \geq c ,$ we have $1 - [ p - ( q r - c ) ] / \theta =$ $[ \theta - p + ( q r - c ) ] / \theta = [ q ( \theta + r ) - c ] / \theta \geq 0$ . Thus, $q _ { B } = \operatorname* { m i n } \{ 1 , [ q ( \theta + r ) - c ] / \theta \}$ . We further discuss two sub-cases.

Case $2 . 1 \colon [ q ( \pmb { \theta } + \pmb { r } ) - c ] / \pmb { \theta } \geq \mathbf { 1 }$ . In this case, $q _ { B } = 1$ and thus, $q r \geq c .$ . The firm solves

$$
\begin{array}{r l} & {\underset {\theta , p, r} {\max} \Pi (\theta , p, r) = (p - k \theta) + (p - k \theta - r) (1 - p / \theta)} \\ & {\quad \mathrm{s.t.} r \geq [ \theta (1 - q) + c ] / q = \frac {p + c}{1 - p / \theta}.} \end{array}
$$

Because the objective function is decreasing in ??, the optimal $\hat { r } = [ \theta ( 1 - q ) + c ] / q$ . Plugging it into Π, we rewrite $\Pi ( p , \theta ) =$ $( p - k \theta ) ( 2 - p / \theta ) - p - c$ . The optimal $\hat { p } = \operatorname* { m i n } \{ \theta ( 1 + k ) / 2 , \theta \}$ . Plugging it into Π, we have

$$
\Pi (\theta) = \left\{ \begin{array}{l l} \theta [ 1 - k (6 - k) ] / 4 - c, & \text {if} k <   1, \\ - k \theta - c, & \text {if} k \geq 1. \end{array} \right.
$$

Because $1 - k ( 6 - k ) > 0 \Leftrightarrow 0 < k < 3 - 2 \sqrt { 2 } = 0 . 1 7 1 6 ,$ we have

$$
(\theta^ {*}, p ^ {*}, r ^ {*}, \Pi^ {*}) = \left\{ \begin{array}{l l} \left(1, \frac {1 + k}{2}, \frac {p ^ {*} + c}{1 - p ^ {*}}, \frac {1 - k (6 - k)}{4} - c\right), & \text {if 0 <   k <   3 - 2\sqrt {2}}, \\ (0, 0, + \infty , - c), & \text {if k\geq 3 - 2\sqrt {2}}, \end{array} \right.
$$

Case 2.2: $[ q ( \pmb { \theta } + \pmb { r } ) - \pmb { c } ] / \pmb { \theta } < \pmb { 1 }$ . In this case, $q _ { B } = [ q ( \theta + r ) - c ] / \theta$ . So the firm solves

$$
\begin{array}{l} \max _ {\theta , p, r} \Pi (\theta , p, r) = [ (p - k \theta) (1 + q) - r q ] [ q (\theta + r) - c ] / \theta \\ \text {s.t.} c / q \leq r <   [ \theta (1 - q) + c ] / q. \end{array}
$$

The constraint $c / q \leq r \leq ( p - k \theta ) ( 1 + q ) / q \Rightarrow c \leq ( p - k \theta ) ( 2 - p / \theta )$ . The latter $( p - k \theta ) ( 2 - p / \theta )$ achieves a global maximum at $p =$ $\theta + k \theta / 2 > \theta .$ . Because we focus on $p \leq \theta _ { : }$ , it holds that $( p - k \theta ) ( 2 - p / \theta ) \leq ( \theta - k \theta ) ( 2 - \theta / \theta ) = \theta ( 1 - k )$ . Thus, $c \leq \theta ( 1 - k ) \leq 1$

The objective function is concave in ?? and achieves a global maximum at $\begin{array} { r } { \hat { r } = \frac { c - q \theta + ( 1 + q ) ( p - k \theta ) } { 2 q } } \end{array}$ . Note that

$$
\left\{ \begin{array}{l l} \hat {r} <   [ \theta (1 - q) + c ] / q & \Leftrightarrow (2 - p / \theta) (p - k \theta) - \theta - p - c <   0, \\ \hat {r} > c / q & \Leftrightarrow (2 - p / \theta) (p - k \theta) - \theta + p - c \geq 0. \end{array} \right.
$$

We first show the first inequality always holds, and then examine the second inequality.

Define $g _ { 1 } ( p , \theta ) \triangleq ( 2 - p / \theta ) ( p - k \theta ) - \theta - p - c .$ . It is clear that $g _ { 1 } < 0$ for all $\theta \in [ 0 , 1 ] , p \in [ 0 , \theta ]$ . Fixing $\theta , g _ { 1 } ( p , \theta )$ is concave in ?? with the global maximum achieved at $\hat { p } = \theta ( 1 + k ) / 2$ . This gives $g _ { 1 } ( \hat { p } , \theta ) = - c + ( - 3 k / 2 + k ^ { 2 } / 4 - 3 / 4 ) \theta$ . Define $g _ { 2 } ( k ) \triangleq - 3 k / 2 +$ $k ^ { 2 } / 4 - 3 / 4$ . It is convex in ??. Because $g _ { 2 } ( 0 ) = - 3 / 4 < 0$ and $g _ { 2 } ( 1 ) = - 2 < 0$ , it follows that $g _ { 2 } ( k ) < 0$ for all $k \in [ 0 , 1 ]$ . Thus, $g _ { 1 } ( \hat { p } , \theta )$ is decreasing in ?? and its maximum $g _ { 1 } ( \hat { p } , 0 ) = - c < 0$

Now,

$$
\begin{array}{r l} & (2 - p / \theta) (p - k \theta) - \theta + p - c \geq 0 \\ \Leftrightarrow & \theta \left[ 3 + k - \sqrt {5 + k ^ {2} - 2 k - 4 c / \theta} \right] / 2 \leq p \leq \theta \left[ 3 + k + \sqrt {5 + k ^ {2} - 2 k - 4 c / \theta} / 2 \right]. \end{array}
$$

Because $c \leq \theta ( 1 - k )$ , we have $5 + k ^ { 2 } - 2 k - 4 c / \theta \geq 5 + k ^ { 2 } - 2 k - 4 ( 1 - k ) = ( 1 + k ) ^ { 2 } \geq 0 ,$ . This further implies $\theta \lceil 3 + k +$ $\sqrt { 5 + k ^ { 2 } - 2 k - 4 c / \theta } \big ] / 2 > \theta > \theta \big [ 3 + k - \sqrt { 5 + k ^ { 2 } - 2 k - 4 c / \theta } \big ] / 2 > 0 .$ . Because $p \leq \theta , p \leq \theta \Big [ 3 + k + \sqrt { 5 + k ^ { 2 } - 2 k - 4 c / \theta } / 2 \Big ]$ holds trivially. We only need to analyze whether $p \ge \theta \big [ 3 + k - \sqrt { 5 + k ^ { 2 } - 2 k - 4 c / \theta } \big ] / 2 \triangleq p _ { 0 }$ holds.

For $\pmb { p } \geq \pmb { p _ { 0 } } ,$ the optimal $r ^ { * } = { \hat { r } }$ ̂ and $\begin{array} { r } { \Pi ( p , \theta ) = \frac { \left( p ^ { 2 } - p \theta - k p \theta + c \theta - \theta ^ { 2 } + 2 k \theta ^ { 2 } \right) ^ { 2 } } { 4 \theta ^ { 3 } } } \end{array}$ . Fixing ??, one can show that the only local maximum is achieved at $\hat { p } =$ $\theta ( 1 + k ) / 2$ . Then $\begin{array} { r } { \hat { p } \ge p _ { 0 } \Leftrightarrow \theta \ge \frac { 4 c } { ( 2 - k ) ^ { 2 } } . } \end{array}$ . Because $\begin{array} { r } { c \leq \theta ( 1 - k ) \Leftrightarrow \theta \geq c / ( 1 - k ) \mathrm { ~ a n d ~ } \frac { c } { 1 - k } \geq \frac { 4 c } { ( 2 - k ) ^ { 2 } } \Leftrightarrow k ^ { 2 } \geq 0 } \end{array}$ (the latter holds trivially), we plug in $\hat { p }$ and obtain

$$
\Pi (\theta) = \frac {(4 c - 5 \theta + 6 k \theta - k ^ {2} \theta) ^ {2}}{6 4 \theta} \text {   for   } \frac {c}{1 - k} \leq \theta \leq 1.
$$

One can verify that $\frac { ( 4 c - 5 \theta + 6 k \theta - k ^ { 2 } \theta ) ^ { 2 } } { 6 4 \theta }$ has a unique local maximum achieved at $\begin{array} { r } { \theta _ { 1 } = - \frac { 4 c } { ( 1 - k ) ( 5 - k ) } } \end{array}$ and a unique local minimum achieved at $\begin{array} { r } { \theta _ { 2 } = \frac { 4 c } { ( 1 - k ) ( 5 - k ) } } \end{array}$ . Because $k \leq 1 ,$ , it holds that $\begin{array} { r } { \theta _ { 2 } \le \frac { c } { 1 - k } . } \end{array}$ So Π(??) is increasing for $\textstyle \theta \geq { \frac { c } { 1 - k } }$ and thus, achieves maximum at $\theta ^ { * } = 1 \mathrm { w i t h } \Pi ^ { * } =$ $\frac { ( 4 c - 5 + 6 k - k ^ { 2 } ) ^ { 2 } } { 6 4 } .$

For $\begin{array} { r } { p < p _ { \mathbf { 0 } } , } \end{array}$ the optimal $r ^ { * } = c / q$ and $\Pi ( p , \theta ) = [ ( p - k \theta ) ( 2 - p / \theta ) - c ] ( 1 - p / \theta )$ . With fixed $\begin{array} { r } { \theta \in \big [ \frac { c } { 1 - k } , 1 \big ] . } \end{array}$ it has a unique local minimum achieved at $p _ { 1 } \triangleq \theta \big [ 3 + k + \sqrt { - 3 c / \theta - ( 3 k - k ^ { 2 } - 3 ) } \big ] / 3$ and a unique local maximum achieved at $p _ { 2 } \triangleq \theta \big [ 3 + k - \sqrt { - 3 c / \theta - ( 3 k - k ^ { 2 } - 3 ) } \big ] / 3$ Because $- 3 c / \theta - ( 3 k - k ^ { 2 } - 3 ) > - 3 ( 1 - k ) - ( 3 k - k ^ { 2 } - 3 ) > k ^ { 2 } ,$ it holds that $0 < p _ { 2 } < \theta < p _ { 1 }$ . Further, note that

$$
\begin{array}{r l} {p _ {0} > p _ {2}} & {\Leftrightarrow \theta \left[ 3 + k - \sqrt {5 + k ^ {2} - 2 k - 4 c / \theta} \right] / 2 > \theta \left[ 3 + k - \sqrt {- 3 c / \theta - (3 k - k ^ {2} - 3)} \right] / 3} \\ & {\Leftrightarrow 3 + k + 2 \sqrt {- 3 c / \theta - (3 k - k ^ {2} - 3)} > 3 \sqrt {5 + k ^ {2} - 2 k - 4 c / \theta}} \\ & {\Leftrightarrow \frac {c}{1 - k} <   \theta <   \frac {4 c}{(1 - k) ^ {2}}.} \end{array}
$$

This leads to

$$
\Pi (\theta) = \left\{ \begin{array}{l l} \Pi_ {1} (\theta) \triangleq [ (p _ {0} - k \theta) (2 - p _ {0} / \theta) - c ] (1 - p _ {0} / \theta), & \text {if} \frac {c}{1 - k} <   \theta <   \frac {4 c}{(1 - k) ^ {2}}, \\ \Pi_ {2} (\theta) \triangleq [ (p _ {2} - k \theta) (2 - p _ {2} / \theta) - c ] (1 - p _ {2} / \theta), & \text {if} \frac {4 c}{(1 - k) ^ {2}} \leq \theta \leq 1. \end{array} \right.
$$

We can rewrite $\Pi _ { 1 } ( \theta ) = \theta \big ( k + 1 - \sqrt { k ^ { 2 } - 2 k + 5 - 4 c / \theta } \big ) ^ { 2 } / 4$ . Let $z \triangleq \sqrt { k ^ { 2 } - 2 k + 5 - 4 c / \theta }$ . Then $\begin{array} { r } { \theta = \frac { 4 c } { k ^ { 2 } - 2 k + 5 - z ^ { 2 } } } \end{array}$ and we further rewrite $\begin{array} { r } { \Pi _ { 1 } ( \theta ) = \theta ( k + 1 - z ) ^ { 2 } / 4 = \frac { c ( k + 1 - z ) ^ { 2 } } { k ^ { 2 } - 2 k + 5 - z ^ { 2 } } \triangleq h ( z ) } \end{array}$ . Note that $\begin{array} { r } { \frac { c } { 1 - k } < \theta < \frac { 4 c } { ( 1 - k ) ^ { 2 } } \Leftrightarrow z \in ( k + 1 , ~ 2 ) } \end{array}$ . Also, $h ^ { \prime } ( z ) = 0$ has two roots $z _ { 1 } = 1 + k$ and $\begin{array} { r } { z _ { 2 } = \frac { 5 - 2 k + k ^ { 2 } } { 1 + k } > 2 . } \end{array}$ . One can verify that $\begin{array} { r } { h ^ { \prime \prime } ( z _ { 1 } ) = \frac { c } { 2 ( 1 - k ) } > 0 } \end{array}$ . Thus, $h ( z )$ is increasing for $z \in ( k + 1 , 2 )$ . Equivalently, $\Pi _ { 1 } ( \theta )$ is increasing for $\begin{array} { r } { \frac { c } { 1 - k } < \theta < \frac { 4 c } { ( 1 - k ) ^ { 2 } } . } \end{array}$

$\mathrm { I f } \frac { 4 c } { ( 1 - k ) ^ { 2 } } \geq 1 \Leftrightarrow c \geq ( 1 - k ) ^ { 2 } / 4$ , then the optimal $\theta ^ { * } = 1$ . Plugging it into $\Pi _ { 1 }$ and comparing the resulting profit with the one under $p \geq p _ { 0 } .$ we obtain $\Pi _ { 1 } ( 1 ) \le ( 4 c - 5 + 6 k - k ^ { 2 } ) ^ { 2 } / 6 4 \Leftrightarrow ( 2 k - k ^ { 2 } - 1 + 4 c ) ^ { 2 } \ge 0$ (the latter holds trivially). If $c < ( 1 - k ) ^ { 2 } / 4$ , then the optimal $\theta ^ { * }$ lies in $\left[ { \frac { 4 c } { ( 1 - k ) ^ { 2 } } } , 1 \right]$ . Let $x \triangleq \sqrt { - 3 c / \theta - ( 3 k - k ^ { 2 } - 3 ) }$ . Then $\begin{array} { r } { \theta = \frac { 3 c } { 3 - 3 k + k ^ { 2 } - x ^ { 2 } } , \Pi _ { 2 } ( \theta ) = \frac { c } { 9 } \Big [ 3 + k + \frac { \left( x ^ { 2 } - 3 \right) \left( x ^ { 4 } + 2 k - 3 \right) } { ( x ^ { 2 } - k ^ { 2 } + 3 k - 3 ) } \Big ] \triangleq g ( x ) } \end{array}$ , and $\begin{array} { r } { \theta \in \left[ \frac { 4 c } { ( 1 - k ) ^ { 2 } } , 1 \right] } \end{array}$ implies $\sqrt { k ^ { 2 } - 3 k + 3 - 3 ( 1 - k ) ^ { 2 } / 4 } < x < \sqrt { k ^ { 2 } - 3 k + 3 - 3 c }$ . We compute $\begin{array} { r } { g ^ { \prime } ( x ) = \frac { 2 c x } { 9 } \Big [ 2 x ^ { 2 } + k ^ { 2 } - 3 k + \frac { k ( 3 - k ) ( 1 - k ) ^ { 2 } \left( 6 - 4 k + k ^ { 2 } \right) } { ( 3 k - k ^ { 2 } + x ^ { 2 } - 3 ) ^ { 2 } } \Big ] } \end{array}$ . Because $6 - 4 k + k ^ { 2 } > 0$ for all $k \in [ 0 , 1 ]$ and $2 x ^ { 2 } + k ^ { 2 } - 3 k \ge 2 ( k ^ { 2 } - 3 k + 3 - 3 ( 1 - k ) ^ { 2 } / 4 ) + k ^ { 2 } - 3 k = 3 ( 1 - k ) ( 3 - k ) / 2 > 0 ,$ it follows that $g ^ { \prime } ( x ) > 0$ . Thus, $g ( x )$ is increasing in ?? and the optimal $x ^ { * } = \sqrt { k ^ { 2 } - 3 k + 3 - 3 c }$ . Plugging it into $^ { g , }$ , we next show $g \big ( \sqrt { k ^ { 2 } - 3 k + 3 - 3 c } \big ) \leq ( 4 c - 5 + 6 k - k ^ { 2 } ) ^ { 2 } / 6 4 .$ Define $G ( c , k ) \triangleq ( 4 c - 5 + 6 k - k ^ { 2 } ) ^ { 2 } / 6 4 - g \big ( \sqrt { k ^ { 2 } - 3 k + 3 - 3 c } \big ) .$ . Fixing ??, one can show that it has two stationary points $c _ { 1 } = 3 / 4 - k +$ $k ^ { 2 } / 3 - \sqrt { 3 / 4 - k + k ^ { 2 } / 2 } / 6$ and $c _ { 2 } = 3 / 4 - k + k ^ { 2 } / 3 + \sqrt { 3 / 4 - k + k ^ { 2 } / 2 } / 6 > c _ { 1 }$ . One can further verify that $c _ { 1 }$ is a local minimum and $c _ { 2 }$ is a local maximum. So it suffices to show $G ( 0 , k ) = ( 5 - 6 k + k ^ { 2 } ) ^ { 2 } / 6 4 - k ( 1 - k ) ^ { 2 } ( 3 - k ) ( 6 - 4 k + k ^ { 2 } ) / 2 7 \geq 0$ . We compute $G ^ { \prime } ( 0 , k ) =$ $- ( 1 - k ) ( 2 3 1 - 5 5 2 k + 5 0 5 k ^ { 2 } - 2 0 8 k ^ { 3 } + 3 2 k ^ { 4 } ) / 1 4 4$ . Let $J ( k ) \triangleq 2 3 1 - 5 5 2 k + 5 0 5 k ^ { 2 } - 2 0 8 k ^ { 3 } + 3 2 k ^ { 4 }$ and one can show it is positive and decreasing for $k < 1$ . Because $J ^ { \prime \prime } ( k ) \propto 5 0 5 - 6 2 4 k + 1 9 2 k ^ { 2 } > 0 , J ^ { \prime } ( k )$ is increasing in ??. Because $J ^ { \prime } ( 1 ) = - 3 8 < 0 , J ( k )$ ) is decreasing in ??. Because $J ( 1 ) = 8 > 0 , G ^ { \prime } ( 0 , k ) < 0$ for all $k \in [ 0 , 1 ]$ and $G ( 0 , k )$ is decreasing in ??. Because $G ( 0 , 0 ) = 2 5 / 6 4 > 0 , G ( 0 , k ) > 0$ for all $k \in [ 0 , 1 ]$ Therefore, $p < p _ { 0 }$ is never better than $p \geq p _ { 0 }$

We next compare profits achieved in Cases 1, 2.1, and 2.2.

$$
\left\{ \begin{array}{l l} & (4 c - 5 + 6 k - k ^ {2}) ^ {2} / 6 4 > (1 - k) ^ {2} / 4 \Leftrightarrow c <   (1 - k) ^ {2} / 4 \\ & (4 c - 5 + 6 k - k ^ {2}) ^ {2} / 6 4 - [ 1 - k (6 - k) / 4 - c ] = (3 + 6 k - k ^ {2} + 4 c) ^ {2} / 6 4 \geq 0. \end{array} \right.
$$

The final solutions are given in Equation (7). ∎

## Appendix C

## Comparative Statics of Referral-Upgrade: Single Referral vs. Multiple Referrals

In this section, we compare the firm’s optimal pricing and quality decisions, as well as customer behavior under the referral-upgrade program between the base model, where each base customer refers at most one friend, and the multi-referral model, where each base customer refers up to ?? friends. We fix $\delta = 1$ to carry out such a comparison (recall that the base model assumes $\delta = 1 )$ . This analysis shows how the breadth of the referral structure affects the firm’s strategy and customer behaviors. Results are presented in Figure C1, where we only report results when referrals are sustained.

(a): Profit  
![](/api/attachments/4WUBVYAF/fulltext/images/35a0f79f1202b74e7d50f7aae7a0e6250191cb79879c7e3e653c2b1895090d2d.jpg)

(b): pB  
![](/api/attachments/4WUBVYAF/fulltext/images/538efbd121c00076ed07d82c5da3f63f68794201ab71fa1b47479183fcd998a4.jpg)

(c): pU  
![](/api/attachments/4WUBVYAF/fulltext/images/43b5dd2b815fb651f96e0fec4f78465b56b1d4b3a712ce4667b2fcdeae792487.jpg)

![](/api/attachments/4WUBVYAF/fulltext/images/221978dbd421aa6659b861533f74ab4879e3bdbcfb8d2d31dabe009ab1cc79a2.jpg)

![](/api/attachments/4WUBVYAF/fulltext/images/07592451be0dddc183267c1bf827bfac8afef6a47e5123dcfaac326dd777b457.jpg)

![](/api/attachments/4WUBVYAF/fulltext/images/d1fcab5a5b8f31a4022d20a86b9435b266a289715a24b46f68c5d7192b992aa8.jpg)

![](/api/attachments/4WUBVYAF/fulltext/images/d64d201be63c1299a644ff8a064cc6d2edd2c337425584eb75a1a87ac85a8a95.jpg)

![](/api/attachments/4WUBVYAF/fulltext/images/54ab61b6f05766ead3227f70ef13469dc13b67a95f9de81bd7985be161c64f8b.jpg)

![](/api/attachments/4WUBVYAF/fulltext/images/fd357abce5742007c5213b21f1e13e83a13a710048039cf5c377d688f0aced35.jpg)  
Figure C1. Comparison Between Single Referrals and Multiple Referrals under Referral-Upgrade Program

First, we observe that as the referral cap ?? increases, referrals can only be sustained under lower referral costs. This is because the total product quality is fixed at one, and a higher ?? dilutes the value of each upgrade option, thereby requiring a lower referral cost to maintain referral actions. We numerically find that under $D = 1$ and 2, referrals will be maintained when the referral cost $c < 0 . 2 5 ;$ under $D = 3 ,$ referrals exist when $c < 0 . 2 1$ , and under $D = 4 ,$ , referrals exist when $c < 0 . 1 8$ . Focusing on low referral costs for referrals to sustain, we find that when ?? is sufficiently small, enabling more referrals (i.e., higher ??) can help the firm reach more customers; this effectively boosts profits. However, as the referral cost grows, enabling multiple referrals may actually hurt the firm’s profit because customers are less inclined to refer and the firm has to offer sufficient upgrade incentives to reward each referral attempt; see Figure C1a.

Second, Figure C1d shows that the basic product’s quality $\theta ^ { * }$ becomes negligible when $D > 1$ . This may result from the special pricing and referral scheme we choose to analyze; under this scheme, the firm is unable to tailor incentives across multiple referrals. Recall that under this scheme, the firm sets the basic product’s quality at ?? and distributes the remaining quality $1 - \theta$ equally across ?? referrals. When ?? is large, because each incremental upgrade has quality $( 1 - \theta ) / D$ , the firm has to set the basic product’s quality ?? sufficiently low to stimulate referrals, effectively making the basic product a low-cost and low-quality “entry ticket” to the full-version product.

Third, customer behaviors under multiple referrals are qualitatively different from those under single referrals; see Figures C1e-C1i. Specifically, unlike the base model in which all base customers purchasing the basic product will make referrals $( \mathrm { i } . \mathsf { e } . , \alpha = 1$ when $D = 1 )$ only some of these customers will do so when they make multiple referrals (i.e., ?? < 1 when $D > 1 )$ . Moreover, under multiple referrals, the demand from base customers is non-monotone in the referral cost, referred customers may possibly buy the basic product only $( \mathrm { i } . \mathrm { e } . , q _ { R } ^ { b } > 0 )$ and the probability that referred customers will buy the full-version product $q _ { R } ^ { f }$ can be non-monotone in the referral cost.

These ramifications from the base model suggest that the referral and versioning mechanisms under multiple referrals can be very different from those under single referrals. Moreover, the profit comparison in Figure C1a shows how the breadth of referral reach (via ??) affects the firm’s design of upgrade-based incentives. Specifically, while increasing ?? may initially improve the firm’s reachability to potential users and enhance profitability, abusively doing so may even backfire due to incentive dilution. These insights highlight a fundamental trade-off inherent in upgrade-based referral programs.
