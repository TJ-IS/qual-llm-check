---
otero_id: 4900
otero_key: "QGR77UYQ"
title: "Advertising Versus Brokerage Model for Online Trading Platforms1"
authors: "Jianqing Chen; Ming Fan; Mingzhi Li"
year: "2016"
journal: "MIS Quarterly"
doi: "10.25300/misq/2016/40.3.03"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Advertising versus Brokerage Model for Online Trading Platforms\*

Jianqing Chen
Jindal School of Management
The University of Texas at Dallas
Email: chenjq@utdallas.edu

Ming Fan

Foster School of Business

University of Washington

Email: mfan@uw.edu

Mingzhi Li

School of Economics and Management

Tsinghua University

Email: mingzhith@gmail.com

Forthcoming in MIS Quarterly

# Advertising versus Brokerage Model for Online Trading Platforms

## Abstract

The two leading online consumer-to-consumer platforms use very different revenue models: eBay.com in the United States uses a brokerage model in which sellers pay eBay on a transaction basis, whereas Taobao.com in China uses an advertising model in which sellers can use the basic platform service for free and pay Taobao for advertising services to increase their exposure. This paper studies how the chosen revenue model affects a platform's revenue, buyers' payoffs, sellers' payoffs, and social welfare. We find that when little space can be dedicated to advertising under the advertising model, the brokerage model generates more revenue for the platform than the advertising model. When a significant proportion of space is dedicated to advertising under the advertising model, matching probability on a platform plays a critical role in determining which revenue model can generate more revenue: If the matching probability is high, the brokerage model generates more revenue; otherwise, the advertising model generates more revenue. Buyers are always better off under the advertising model because of larger participation by the sellers for the platform's free service. Sellers are better off under the advertising model in most scenarios. The only exception is when the matching probability is low and the platform dedicates a large space to advertising. Under these conditions, the sellers with payoffs similar to the marginal advertiser who is indifferent about advertising can be worse off under the advertising model. Finally, the advertising model generates more social welfare than the brokerage model.

## 1 Introduction

eBay.com, the leading online consumer-to-consumer platform in the United States, has been establishing its business for almost two decades. Individual buyers can shop on the eBay platform without any fee, and sellers pay eBay on a transaction basis. Arguably, eBay was one of the biggest innovations and successes in the early e-commerce period. In contrast, Taobao.com, the leading online consumer-to-consumer platform in China, started its business in 2003. While Taobao and eBay share many similar design features, Taobao adopted a radically different revenue model. In addition to providing free service to individual buyers, Taobao offers the basic platform service to sellers for free as well. Meanwhile, Taobao offers an advertising/promotion service to monetize the traffic, and sellers can pay to participate. In other words, in a manner different from eBay but similar to Google search result pages, Taobao provides two lists: One is an “organic” listing, typically on the left of each page, in which sellers are listed for free, and the other is a “paid” listing, typically on the right of each page, in which sellers pay Taobao to increase their exposure to potential buyers. The differences between the revenue models associated with the two largest and most successful online marketplaces raise several questions: Which revenue model is more suitable for an online platform? How should a platform choose and design a revenue model? How does the revenue model affect buyers’ and sellers’ payoffs? This paper aims to answer these questions.

Founded in 1995, eBay’s total transaction volume, or gross merchandise volume, was nearly \$62 billion in 2010, according to its annual report. eBay’s marketplace charges sellers insertion fees and final value fees. The insertion fee ranges from \$0.10 to \$2 for auction-style listings at eBay and is \$0.50 for fixed-price listings. Depending on the sale format and product category, the final value fees at eBay can range from 7% to 13% of the total buyer cost, including price and shipping costs. $^{1}$ Taobao was launched by Alibaba Group in 2003 and has grown remarkably since then. Its sales volume was about \$61 billion in 2010. $^{2}$

Taobao offers basic market services for free to both buyers and sellers. Its main source of revenue is the advertising paid for by the sellers. Despite the success of Taobao, no formal analysis of its revenue model has been conducted. This study fills this gap and sheds some light on the choice and design of a platform's revenue models.

To do so, we develop a game-theoretic model in which a platform faces a group of potential buyers on the one side and a group of potential sellers on the other. We assume the platform can choose either the brokerage model or the advertising model. Under the brokerage model, the platform charges sellers a transaction fee for each sale. Under the advertising model, the platform offers the basic service for free and, meanwhile, provides paid advertising service by which sellers can participate to increase their exposure. The platform's choice of the revenue model affects potential sellers' participation decisions. Potential buyers do not have to pay to participate but have different opportunity costs to use the platform. Buyers' participation decisions are affected by the number of participating sellers and the matching probability. The number of participating sellers indicates how likely buyers' trading partners are on the platform: As more sellers participate in the platform, the likelihood that a buyer's trading partner is on the platform increases. The matching probability measures the likelihood of a buyer actually finding his or her trading partner (given the partner's being on the platform). Under this framework, we compare the platform's revenues, sellers' payoffs, buyers' payoffs, and social welfare under the two revenue models.

We identify both the space dedicated to advertising and the matching probability as key factors in comparing the two revenue models. Not surprisingly, when little space can be dedicated to advertising under the advertising model, the brokerage model generates more revenue for the platform than the advertising model. When a significant proportion of space is dedicated to advertising under the advertising model, matching probability on a platform plays a critical role in determining which revenue model can generate more revenue: If the matching probability is high, the brokerage model generates more revenue; otherwise, the advertising model generates more revenue. In the presence of a free basic platform service, when the matching probability is low, the advertising space becomes more valuable, which allows the platform to charge a higher price and potentially to make more revenue under the advertising model.

Buyers are always better off under the advertising model because of greater participation by sellers in the platform's free service. Sellers are better off under the advertising model in most scenarios. The only exception is that, when the matching probability is low and the platform dedicates a large space to advertising, the sellers having payoffs similar to the marginal advertiser (i.e., the advertiser who is indifferent about advertising) can be worse off under the advertising model. Finally, the advertising model generates more social welfare than the brokerage model because of the increased number of trading pairs.

Our study is mainly related to two streams of research. The first related stream looks at different business and revenue models. A number of papers focus on one type of revenue model and study the optimal strategies under that model (Anderson and Coate, 2005; Casadesus-Masanell and Zhu, 2012; Niculescu and Wu, 2014; Cheng and Liu, 2012). For example, Anderson and Coate (2005) examine equilibrium advertising levels in broadcasting, and Niculescu and Wu (2014) investigate when software firms should commercialize new products via freemium business models. Other papers compare different revenue models. For instance, Casadesus-Masanell and Zhu (2010) analyze the optimal business model choice for a high-quality incumbent facing a low-quality, ad-sponsored competitor in a product market. Among the four business models considered—a subscription-based model, an ad-sponsored model, a mixed model incorporating both subscriptions and advertising, and a dual model in which one product uses the ad-sponsored model and the other uses the mixed model—they find the incumbent prefers the subscription-based or the ad-sponsored model. Lin et al. (2012) consider settings in which online service providers might offer an ad-free service, an ad-supported service, or a combination of these services. They find that in a monopoly case, offering both ad-free and ad-supported services is optimal, and in a duopoly case, exactly one firm offers both services when the ad revenue rate is sufficiently high. Our study differs from theirs in that we compare the advertising model and the brokerage model for online trading platforms. In addition, in our setting, the basic platform service and the advertising service serve the same purpose of presenting relevant sellers to potential buyers and, by their nature, are substitutes; thus, our analysis and insights depart from theirs.

The second related stream involves the studies on two-sided markets (Gallaugher and Wang, 2002; Rochet and Tirole, 2003; Parker and Alstyne, 2005; Bhargava and Choudhary, 2004; Economides and Katsamakas, 2006; Jullien, 2006; Hagiu, 2009). Two-sided markets refer to the situations where “platforms” provide services to facilitate interactions and the operation of exchanges between two types of trading partners (Jullien, 2006). Examples of two-sided markets include credit card systems (cardholders and merchants), health maintenance organizations (patients and doctors), shopping malls (buyers and merchants), travel reservation services (travelers and airlines), video game consoles (gamers and game developers), and online trading platforms (buyers and sellers). In a typical two-sided market, the users’ benefit from joining the platform on one side is increasing in the number of users adopting the platform on the other side. For example, an online trading platform that provides services to enable interactions between buyers and sellers is a two-sided market, in which the users on one side (e.g., sellers) are more likely to find their trading partners if more users join the platform on the other side (e.g., buyers). Rochet and Tirole (2003) study platform competition and optimal price allocation between buyers and sellers. They consider a brokerage intermediary that charges prices or registration fees from market participants to be on a marketplace. The market has (indirect) network externalities, and the demand on one side of the market depends on the demand from the other side. Bhargava and Choudhary (2004) study the optimal quality and pricing strategies for information intermediaries with aggregation benefits (positive indirect network externalities) and find that intermediaries have strong incentives to provide quality-differentiated versions of services. Gallaugher and Wang (2002) empirically investigate the effects on software price of different factors, including network externalities, in the context of the two-sided market for Web server software.

In contrast to these papers, we compare two different revenue models for an online trading platform and examine the effect of the platform's revenue model choice on the players.

Our research is also loosely related to the growing literature on design science and mechanism design (e.g., Hevner et al., 2004; March and Storey, 2008; Chellappa and Shivendu, 2010) in information systems. Researchers in information systems not only design and evaluate new systems in a business context (e.g., Nault and Dexter, 2006; Chen et al., 2013), but also develop new ways to conduct business to leverage the advancement of information technologies. For example, studies have examined new trading mechanisms for distributed resource allocation (Guo et al., 2012), new business models for the software industry (Niculescu and Wu, 2014), and different mechanisms for online personalization services (Chellappa and Shivendu, 2010). The focus of this work is on understanding the effect on the individual users, platform, and society of different revenue model designs for an online trading platform. Similar to other papers on design science, our paper is “aimed at improving the performance of business organizations” (March and Storey, 2008), but we focus on the revenue model of an online trading platform.

The rest of the paper is organized as follows. In the next section, we set forth our baseline model. In Section 3 we provide an equilibrium analysis, and in Section 4 we compare the publisher's revenue, buyers' payoffs, sellers' payoffs, and social welfare under the two revenue models. In Section 5, we extend the baseline model in various directions. We show that the qualitative results derived from the baseline model stay the same when buyers have heterogeneous search skills, when the total exposure level under the advertising model is slightly different from that under the brokerage model, when buyers are averse to advertising, and when sellers compete with each other. In addition, we provide some discussion about platform competition and dynamics. Section 6 concludes the paper.

## 2 The Baseline Model

We consider an online platform with multiple sellers on one side and multiple buyers on the other. The platform provides matching as well as other necessary services to facilitate transactions between sellers and buyers. Consistent with popular online platform practices, such as in eBay and in Taobao, buyers can participate without any cost. For sellers, we consider two different business models: a brokerage model and an advertising model. Under the brokerage model, sellers pay a transaction fee $\tau$ for each sale. Under the advertising model, sellers can participate in the basic platform service for free, and, in addition, they can pay $\theta$ to participate in an advertising or promotion service provided by the platform to increase their exposure to potential buyers. The brokerage model resembles eBay's practice, and the advertising model resembles Taobao's practice.

A mass of sellers with measure 1 may sell their products through the platform. Consistent with the many existing studies on two-sided markets (e.g., Jullien, 2006), each seller is seen as selling a different product, and thus the competition among sellers is not considered in this paper. Sellers have different fixed costs, k, of providing their products through the platform. A mass of buyers with measure 1 may buy products through the platform. As in Jullien (2006), we assume that accessing the platform involves different opportunity costs, c, for the buyers. The opportunity cost can be viewed as, for example, the value that a buyer derives from using an alternative channel. More generally, the opportunity cost measures the relative attractiveness of this platform to buyers, compared to the alternative channel that they may use. We assume that both k and c satisfy uniform distributions with support [0, 1].

Depending on their costs and the platform's business model, some buyers and sellers participate in the platform and the others do not. We denote $m$ as the mass of buyers and $n$ as the mass of sellers participating in the platform. Notice that both $m$ and $n$ are endogenously determined based on users' self-section behavior, and their values vary under the two different business models. A buyer's probability of finding her trading partner on the platform depends on whether her selling partner is on the platform, and, if so, whether the buyer can find the selling partner. In general, as the number of sellers participating in the platform increases, so does the likelihood that a buyer's trading partner is on the platform. We assume that the probability that a buyer's trading partner is on the platform is equal to the mass of participating sellers n. This assumption simplifies the mathematical expressions while capturing the essential idea that a buyer's trading partner is more likely to be on the platform if more sellers participate in the platform, as has been used often in the existing literature (e.g., Jullien, 2006). This assumption can also be understood as each buyer has one unique trading partner in the seller pool and the trading partners' costs are independent. Therefore, the probability of a buyer's trading partner being on the platform is the proportion of participating sellers out of the seller pool; that is n.

Under the brokerage model, we assume that sellers are listed without differentiation, and each seller receives the same exposure level p, which determines the likelihood that her product is noticed by buyers. In other words, a buyer can find her trading partner or the ideal product that meets her need with probability $p, p \in (0,1)$ , conditional on the partner's being on the platform. For ease of exposition, we simply assume that when a potential buyer finds her trading partner or ideal product, the trade occurs. Introducing a trading probability or a conversion rate adds an additional parameter and does not change the results. We call p the buyers' base probability of finding their ideal products, or the matching probability. The base probability depends on the quality of the search function provided by the platform and buyers' overall online skill and experience, among other factors. Even with powerful platform search function, buyers may not be able to find their ideal products. As in a typical product "discovery" process, buyers are often not sure about what are the ideal products that meet their needs. Therefore, when buyers explore products on the platform, even if their ideal products are on the platform, they might not be able to locate them, because of the limited number of search they conduct (Johnson et al., 2004) due to positive search cost (Stahl, 1989). In the extension, we also consider the case in which buyers have heterogeneous search

skills.

Under the advertising model, advertised sellers get more exposure than unadvertised ones and their products are more likely to be noticed by potential buyers. If we denote $p_{1}$ as the exposure that an unadvertised seller receives and $p_{2}$ as the exposure that an advertised seller receives, we generally have $p_{1} < p_{2}$ . We denote $n'$ as the mass of sellers who participate in the advertising service. For the purpose of a fair comparison, we assume that, were the numbers of participating sellers under the two business models the same, the total exposure under the advertising model (i.e., $(n - n')p_{1} + n'p_{2}$ ) should equal the total exposure under the brokerage model (i.e., np); that is,

$$
(n - n ^ {\prime}) p _ {1} + n ^ {\prime} p _ {2} = n p\tag{1}
$$

In other words, if the numbers of participating sellers under the two business model were the same, compared with the brokerage model, the advertising model would not increase or reduce the overall exposure. In a sense, advertising acts as an exposure reallocation device: the advertising shifts the exposure toward the advertised sellers from the unadvertised sellers. As a result, the products from advertised sellers are more likely to be noticed by buyers than the products from unadvertised sellers. In the extension, we also consider the case in which the total exposure under the advertising model is not equal to that under the brokerage model.

Because $p_{1} < p_{2}$ , by Equation (1), we have $p_{1} < p$ , and, without loss of generality, we can let $p_{1} = (1 - a)p$ , where $a \in [0, 1]$ reflects the proportion of space dedicated to advertising. For example, when a = 0, we have $p_{1} = p_{2} = p$ , which indicates all sellers receive the same exposure and are equally likely to be noticed by potential buyers with the base matching probability p, and thus this case is equivalent to the one in which no advertising space is offered. By simple algebra, from Equation (1), we can derive

$$
p _ {2} - p _ {1} = \frac {a p n}{n ^ {\prime}}\tag{2}
$$

which measures the additional exposure gained from advertising. Clearly, a larger space dedicated to advertising (i.e., a larger $a$ ) increases the additional exposure, given the number of sellers who participate in the advertising service. By substituting in $p_1$ , we have $p_2 = (1 - a)p + \frac{apn}{n'}$ . When considerable space is dedicated to advertising (i.e., $a$ is large) or when a relatively small number of sellers participates in the advertising service (i.e., $n'/n$ is small), $p_2$ , as previously defined, would technically go above 1. In this case, the advertised sellers are “overexposed” to buyers—they are noticed by potential buyers with probability 1, and in fact are exposed more than what is necessary for them to be noticed by potential buyers with probability 1. We call this case excessive advertising. Therefore, while an unadvertised seller is noticed by buyers with probability $p_1$ , an advertised seller is noticed by buyers with probability $\min\{p_2, 1\}$ . We call the case with $p_2 \leq 1$ regular advertising. In the regular advertising case, Equation (1) can also be interpreted to mean that the (weighted) average matching probability is the same under the two revenue models. In the excessive advertising case, some “attention” from buyers is wasted, and the (weighted) average matching probability in this case is lower than that under the regular advertising case.

We denote by s the expected surplus that a buyer derives from finding her trading partner and by $\pi$ the expected revenue that a seller derives from finding her trading partner. We assume $s \leq 1$ and $\pi \leq 1$ to exclude some less interesting cases. For instance, if $\pi > 1$ , under the advertising model, all sellers participate in the basic platform service (because their fixed costs, being in the range [0, 1], are less than 1) and the mass of participating sellers is simply 1.

Under the brokerage model, a buyer's expected payoff from participating in the platform is

$$
n p s - c\tag{3}
$$

and a seller's expected payoff from participating in the platform is

$$
m p (\pi - k - \tau)\tag{4}
$$

where $k$ is the seller's fixed cost and $\tau$ is the transaction fee paid to the platform.

Under the advertising model, a buyer's expected payoff from participating in the platform is

$$
[ (n - n ^ {\prime}) p _ {1} + n ^ {\prime} \min \{p _ {2}, 1 \} ] s - c,\tag{5}
$$

where $[(n-n')p_{1}+n'\min\{p_{2},1\}]$ is the probability that the buyer can find her trading partner—the probability of finding the partner among the unadvertised sellers plus the probability of finding the partner among the advertised sellers. Notice that when $p_{2}\leq1$ , the above equation is simply $(nps-c)$ because of Equation (1).

A seller's expected payoff from participating in the platform is

$$
m \left[ p _ {1} + I \left(\min \{p _ {2}, 1 \} - p _ {1}\right) \right] (\pi - k) - I \theta ,\tag{6}
$$

where $I, I \in \{0, 1\}$ , indicates whether the seller participates in the advertising service. When the seller chooses not to participate in the advertising service (i.e., I = 0), the seller's expected payoff from participating in the platform is $mp_{1}(\pi - k)$ . When the seller chooses to participate in the advertising service (i.e., I = 1), the seller's expected payoff from participating in the platform is $[m \min\{p_{2}, 1\}(\pi - k) - \theta]$ . The benefit of participating in the advertising service is the additional exposure $(\min\{p_{2}, 1\} - p_{1})$ , at the cost of $\theta$ .

The sequence of events in the game is as follows. First, the platform owner announces its business model and fee structure (i.e., transaction fee $\tau$ under the brokerage model or advertising fee $\theta$ under the advertising model). Then, the potential sellers and buyers decide whether to participate in the platform simultaneously (which determines n and m, respectively). Under the advertising model, at the same time the participating sellers decide whether to participate in the advertising service (which determines $n'$ ). Finally, transactions take place between sellers and buyers. Table 1 summarizes the main notations used in the paper.

We next derive and compare the equilibrium outcome under the brokerage and advertising models, considering the complete parameter space of advertising space a and matching

Table 1: Summary of Notations

<table><tr><td>Notation</td><td>Definition and Comments</td></tr><tr><td>τ</td><td>transaction fee for each sale under the brokerage model</td></tr><tr><td>θ</td><td>advertising fee under the advertising model</td></tr><tr><td>k</td><td>a seller&#x27;s cost of providing his product</td></tr><tr><td>c</td><td>a buyer&#x27;s opportunity cost</td></tr><tr><td>m</td><td>the mass of participating buyers</td></tr><tr><td>n</td><td>the mass of participating sellers</td></tr><tr><td>p</td><td>the exposure that each participating seller receives under the brokerage model, also called “matching probability”</td></tr><tr><td>p1</td><td>the exposure that each participating but unadvertised seller receives under the advertising model</td></tr><tr><td>p2</td><td>the exposure that each advertised seller receives under the advertising model</td></tr><tr><td>n&#x27;</td><td>the mass of sellers who participate in advertising service under the advertising model</td></tr><tr><td>a</td><td>proportion of space dedicated to advertising under the advertising model</td></tr><tr><td>s</td><td>buyers&#x27; expected surplus from trading</td></tr><tr><td>π</td><td>sellers&#x27; expected revenue from trading</td></tr></table>

probability p.

## 3 Equilibrium Analysis

In this section, we examine the participation decisions of the potential buyers and sellers in equilibrium, and we derive the equilibrium payoffs of both participating players and the platform under the brokerage model and under the advertising model.

## 3.1 Equilibrium Under the Brokerage Model

Given the structure of the problem, we can expect monotonicity in both sellers' and buyers' participation decisions because the players with lower costs generally derive higher payoff than their counterparts with higher costs. More specifically, if a buyer (seller) with a certain cost participates in the platform, the buyers (sellers) with lower costs also participate. We summarize this observation in Lemma 1 with the proof in the appendix.

Based on this monotonicity, we next can characterize the marginal buyer who is indifferent about participating or not. We denote $c_{B}$ as the cost of the marginal buyer, which satisfies $nps - c_{B} = 0$ , based on the payoff in Equation (3). By the monotonicity, the buyers with costs lower than $c_{B}$ participate in the platform and those with costs higher than $c_{B}$ do not participate. Because we assume that the opportunity costs of buyers are uniformly distributed over [0,1], the mass of participating buyers is $m = c_{B}$ . Similarly, we denote $k_{B}$ as the cost of the marginal seller who is indifferent about participating or not; that is, $mp(\pi - k_{B} - \tau) = 0$ , based on the payoff in Equation (4). The sellers who have costs lower than $k_{B}$ participate in the platform, and thus the mass of participating sellers is $n = k_{B}$ . Together, we can derive

$$
k _ {B} = \pi - \tau\tag{7}
$$

$$
c _ {B} = k _ {B} p s = (\pi - \tau) p s\tag{8}
$$

Clearly, $\tau$ should be less than $\pi$ ; otherwise, no sellers participate.

Notice that the total number of transactions is the probability that each buyer can find her trading partner times the number of participating buyers; that is, the total number of transactions is $mnp = c_B k_B p$ . The platform's owner maximizes its revenue $\Pi_B$ by optimally choosing its transaction fee:

$$
\max _ {0 <   \tau <   \pi} c _ {B} k _ {B} p \tau = \max _ {0 <   \tau <   \pi} p ^ {2} s \tau (\pi - \tau) ^ {2}
$$

By the first-order condition, we conclude the optimal solution as follows.

Proposition 1. The optimal transaction fee that the platform should charge is $\tau^{*} = \frac{\pi}{3}$ , and the maximum revenue is $\Pi_B^* = \frac{4p^2s\pi^3}{27}$ .

Proof. All proofs are in the appendix, unless indicated otherwise.

The above results are derived in a fashion similar to the balance between price and demand. If the transaction fee $\tau$ (i.e., “price”) is high, the participating players and thus the number of transactions is low (i.e., “demand”). The optimal value as derived is the result of the balance. Note that if the number of participating buyers was fixed (such that m was not a function of $\tau$ ), the optimal transaction fee would be $\pi/2$ by maximizing the platform’s revenue $mp(\pi - \tau)\tau$ . In contrast, considering the effect of $\tau$ on the number of participating buyers via the number of participating sellers, or considering the two-sided market effect, the optimal transaction fee $\pi/3$ is lower than when considering the effect of $\tau$ on the number of sellers only. The lower transaction fee in the two-sided market occurs because lowering the transaction fee not only increases the number of participating sellers, but also increases the number of participating buyers. This additional benefit induces the platform to lower the transaction fee.

Based on the optimal transaction fee and Equation (7), the mass of the participating sellers in equilibrium is

$$
n _ {B} ^ {*} = k _ {B} ^ {*} = \frac {2}{3} \pi\tag{9}
$$

By Equation (8), the mass of the participating buyers in equilibrium is

$$
m _ {B} ^ {*} = c _ {B} ^ {*} = \frac {2}{3} p s \pi\tag{10}
$$

Thus, we can conclude the participation of sellers and buyers as follows.

Corollary 1. Under the brokerage model, the sellers who have costs in $[0, k_{B}^{*}]$ and the buyers who have opportunity costs in $[0, c_{B}^{*}]$ participate in the platform in equilibrium.

By substituting $n_{B}^{*}$ , $m_{B}^{*}$ , and $\tau^{*}$ into Equations (3) and (4), we can formulate the payoffs of the participating buyers and the payoffs of the participating sellers in equilibrium.

## 3.2 Equilibrium Under the Advertising Model

Similar to the brokerage model, in the advertising model, we have monotonicity in both sellers' and buyers' participation decisions. In particular, if a buyer (seller) with a certain cost participates in the platform, the buyers (sellers) with lower costs also participate. In addition, if a seller with a certain cost participates in the advertising service, the sellers with lower costs also participate in the advertising service. The latter is because the advertising fee is the same to all sellers and the sellers with lower costs have higher profit margins and benefit more from additional exposure provided by advertising. We summarize this observation in Lemma 2 with proof in the appendix.

Similar to our approach under the brokerage model, we denote $c_{A}$ as the cost of the marginal buyer who is indifferent about participating or not. The buyers with costs lower than $c_{A}$ participate in the platform, and the mass of participating buyers thus is $m = c_{A}$ . We denote $k_{A}$ as the cost of the marginal seller who is indifferent about participating in the platform or not, and $k_{A}^{\prime}$ as the cost of the marginal advertiser who is indifferent about participating in the advertising service or not. By Equation (6), if a seller derives a positive payoff from participating in the advertising service (paying advertising cost $\theta$ ), her payoff from participating in the basic platform service without cost should be positive, which implies $k_{A}^{\prime} < k_{A}$ . Therefore, the sellers with costs lower than $k_{A}$ participate in the platform, and the mass of participating sellers is $n = k_{A}$ . Among these participating sellers, those with costs lower than $k_{A}^{\prime}$ participate in the advertising service, and the mass of advertised sellers thus is $n^{\prime} = k_{A}^{\prime}$ .

In settings similar to a two-sided market, a “pessimistic” equilibrium exists in which neither side participates. Because such an equilibrium can be easily excluded, we next focus on the equilibrium with positive participation. For internal solutions, we derive the following relationship among these marginal users:

$$
[ (k _ {A} - k _ {A} ^ {\prime}) p _ {1} + k _ {A} ^ {\prime} \min \{p _ {2}, 1 \} ] s - c _ {A} = 0\tag{11}
$$

$$
c _ {A} p _ {1} (\pi - k _ {A}) = 0\tag{12}
$$

$$
c _ {A} \min \{p _ {2}, 1 \} (\pi - k _ {A} ^ {\prime}) - \theta = c _ {A} p _ {1} (\pi - k _ {A} ^ {\prime})\tag{13}
$$

Equation (11) is the condition for the marginal buyer who is indifferent about participating in the platform or not, derived by substituting $n = k_{A}$ and $n' = k'_{A}$ into Equation (5). Equation (12) is the condition for the marginal seller who is indifferent about participating in the platform or not, derived by letting I = 0 and $m = c_{A}$ in Equation (6). Equation (13) is the condition for the marginal advertiser who is indifferent about participating in the advertising service or not: The left-hand side is her payoff for using advertising (by letting I = 1 and $m = c_{A}$ in Equation (6)), and the right-hand side is her payoff for not using advertising (by letting I = 0 and $m = c_{A}$ in Equation (6)).

From Equation (12), we derive $k_{A} = \pi$ , and therefore, only sellers with fixed costs less than $\pi$ participate. When the advertising is mild, such that $p_{2} < 1$ , from Equation (11), we have $c_{A} = k_{A}ps = \pi ps$ , where the first equality is because of Equation (1) and the second equality is because of $k_{A} = \pi$ . In addition, $\min\{p_{2}, 1\} - p_{1} = \frac{apk_{A}}{k_{A}^{\prime}}$ by Equation (2). From Equation (13), we can then derive $\theta k_{A}^{\prime} = \pi^{2}p^{2}sa(\pi - k_{A}^{\prime})$ . First, we notice that $k_{A}^{\prime}$ is monotonically decreasing in $\theta$ , which makes intuitive sense in that a higher advertising cost leads to participation by fewer sellers in advertising. Second, the equation implies that the platform's advertising revenue $\theta k_{A}^{\prime}$ is simply $p^{2}\pi^{2}sa(\pi - k_{A}^{\prime})$ . To increase its revenue, the platform has incentive to lower $k_{A}^{\prime}$ by charging a higher advertising price. Notice that, by Equation (2), $p_{2} = p_{1} + \frac{apn}{n^{\prime}} = p_{1} + \frac{ap\pi}{k_{A}^{\prime}}$ . Lowering $k_{A}^{\prime}$ increases the exposure level for advertised sellers and ultimately gives with probability of 1 the notice of advertised sellers by buyers; that is, $\min\{p_{2}, 1\} = 1$ . In other words, $p_{2} < 1$ cannot be the platform's optimal choice.

We next analyze the case with $p_{2} \geq 1$ . We denote

$$
\delta \equiv 1 - (1 - a) p,\tag{14}
$$

which is the (maximum) increase in the probability of a seller's being noticed by potential buyers through advertising (because $(1 - a)p = p_1$ ). By substituting in $p_1 = (1 - a)p$ and $\min \{p_2,1\} = 1$ , Equations (11) and (13) change to

$$
{c _ {A}} = {\left[ (1 - a) p (\pi - k _ {A} ^ {\prime}) + k _ {A} ^ {\prime} \right] s = \left[ (1 - \delta) \pi + \delta k _ {A} ^ {\prime} \right] s}\tag{15}
$$

$$
\theta = c _ {A} [ 1 - (1 - a) p ] (\pi - k _ {A} ^ {\prime}) = c _ {A} \delta (\pi - k _ {A} ^ {\prime})\tag{16}
$$

where the second equality in each equation is achieved by substituting in the definition of $\delta$ .

By the monotonicity of their participation (summarized in Lemma 2 in the appendix), all sellers with cost lower than $k_A'$ participate in the advertising service, and $k_A'$ also measures the mass of sellers who advertise, or the demand for the platform advertising service given the advertising price $\theta$ . Equations (15) and (16) define the relationship between the demand $k_A'$ and advertising price $\theta$ . By substituting $c_A$ in Equation (15) into Equation (16), we can derive the inverse demand function as $\theta = \delta \pi s(\pi - k_A') - \delta^2 s(\pi - k_A')^2$ . The platform maximizes its revenue $\Pi_A = \theta k_A'$ by choosing the advertising fee $\theta$ (i.e., price) or, equivalently, by choosing the marginal seller who is indifferent about participation in the advertising service (i.e., demand); that is,

$$
\max _ {0 <   k _ {A} ^ {\prime} <   \pi} \delta s \left[ \pi (\pi - k _ {A} ^ {\prime}) - \delta (\pi - k _ {A} ^ {\prime}) ^ {2} \right] k _ {A} ^ {\prime}\tag{17}
$$

$$
\mathrm{s.t.} p _ {2} = (1 - a) p + \frac {a p \pi}{k _ {A} ^ {\prime}} \geq 1\tag{18}
$$

Solving the above optimization problem, we can conclude the optimal advertising fee and the maximum revenue that the platform can generate as follows.

Proposition 2. Denote $\hat{p}(a) \equiv \frac{1 + a}{1 + 2a}$ . Given $a$ ( $a \in (0,1)$ ), the optimal advertising fee that the platform should charge is

$$
\theta^ {*} = \left\{ \begin{array}{l l} s \pi^ {2} \left[ \frac {1 + 2 \delta - 2 \delta^ {2} + (2 \delta - 1) \sqrt {1 - \delta + \delta^ {2}}}{9} \right] & i f p > \hat {p} (a) \\ p (1 - p) s \pi^ {2} & i f p \leq \hat {p} (a) \end{array} \right.\tag{19}
$$

The platform's maximum revenue is

$$
\Pi_ {A} ^ {*} = \left\{ \begin{array}{l l} \frac {s \pi^ {3}}{2 7 \delta} \left[ - 2 + 3 \delta + 3 \delta^ {2} - 2 \delta^ {3} + 2 (1 - \delta + \delta^ {2}) ^ {\frac {3}{2}} \right] & i f p > \hat {p} (a) \\ \frac {(1 - p) a}{\delta} p ^ {2} s \pi^ {3} & i f p \leq \hat {p} (a) \end{array} \right.
$$

Similar to the effects of fee increases under the brokerage model, increasing the advertising fee decreases the number of participating advertisers, which in turn affects the number of participating buyers. The optimal advertising fee derived above is the result of the balance between the price and the number of participating players, including both the buyers and the sellers. Depending on the relative value between p and a, we have two scenarios with different results that are segmented by $\hat{p}(a)$ . Figure 1 depicts curve $\hat{p}(a)$ in the $(a,p)$ space. When the matching probability p is large (i.e., $p > \hat{p}(a)$ ), from the proof of the proposition, the constraint in Inequality (18) does not bind, and the equilibrium $p_{2}$ thus is above 1, which indicates excessive advertising. When p is small (i.e., $p < \hat{p}(a)$ ), the constraint binds, and in equilibrium $p_{2} = 1$ , which indicates non-excessive advertising. Notice that what distinguishes excessive and non-excessive advertising is whether advertised sellers are “overexposed.” In the excessive advertising case, the advertised sellers are overexposed to buyers—the advertised sellers are exposed more than what is needed for them to be noticed by potential buyers with probability 1; therefore, some exposure is wasted. In the non-excessive advertising case, no exposure is wasted, although advertised sellers are also noticed by potential buyers with probability 1.

Corollary 2. When $p > \hat{p}(a)$ , the equilibrium advertising is excessive (i.e., $p_2^* > 1$ ); when $p < \hat{p}(a)$ , the equilibrium advertising is non-excessive.

Notice that a seller's benefit from advertising is $\delta (\pi - k)$ , the additional exposure multiplied by the profit margin from each sale. Clearly, the benefit is decreasing in sellers' costs. Given any $a$ , when $p$ is large—which means the exposure from the free listing is large—the additional exposure (by Equation (14)) is small and the benefit from advertising thus is small. As a result, only those with very low fixed costs participate in the advertising service, and the advertising might be excessive. Figure 1 shows the scenarios in which equilibrium advertising is excessive and the scenarios in which advertising is regular. The two scenarios are segmented by the cut-off curve $\hat{p}(a)$ , above which the advertising is excessive. Note that the cut-off curve $\hat{p}(a)$ decreases in $a$ . Intuitively, with a larger $a$ , or with more space dedicated to advertising, the platform has more exposure to be allocated to advertised sellers and the advertising is therefore more likely to be excessive (even though more sellers are induced to participate in the advertising service).

![](/api/attachments/QGR77UYQ/fulltext/images/cddc3405012e57edea351d3f07d66c3fd04c055b89d6d0d9d092258b10b66ff7.jpg)  
Figure 1: Excessive vs. Regular Advertising

Based on the optimal advertising fee, the mass of the participating seller and the mass of the participating advertisers in equilibrium are

$$
n _ {A} ^ {*} = k _ {A} ^ {*} = \pi \text { and } n _ {A} ^ {\prime *} = k _ {A} ^ {\prime *}\tag{20}
$$

where $k_A'$ , the cost of the marginal advertiser in equilibrium, is

$$
k _ {A} ^ {\prime *} = \left\{ \begin{array}{l l} \frac {(2 \delta - 1) + \sqrt {1 - \delta + \delta^ {2}}}{3 \delta} \pi & \text { if } p > \hat {p} (a) \\ \frac {a p \pi}{\delta} & \text { if } p \leq \hat {p} (a). \end{array} \right.\tag{21}
$$

(The derivation of $k_A'$ can be found in the proof of Proposition 2.) By Equation (15), the mass of the participating buyers in equilibrium is

$$
m _ {A} ^ {*} = c _ {A} ^ {*} = [ (1 - \delta) \pi + \delta k _ {A} ^ {\prime *} ] s\tag{22}
$$

Based on the monotonicity of their participation (summarized in Lemma 2 in the appendix), we can conclude the participation of sellers and buyers as follows.

Corollary 3. Under the advertising model, the sellers with costs in $[0, k_A^*]$ and the buyers with opportunity costs in $[0, c_A^*]$ participate in the platform in equilibrium. Among the participating sellers, the ones with costs in $[0, k_A'']$ participate in the advertising service, and the ones with costs in $[k_A'*, k_A^*]$ do not participate in the advertising service.

By substituting $n_{A}^{*}$ , $n_{A}^{\prime*}$ , $m_{A}^{*}$ , and $\theta^{*}$ into Equations (5) and (6), we can formulate the pay-offs of the participating buyers and the payoffs of the participating sellers (with advertising and without advertising) in equilibrium.

## 4 Equilibrium Comparison

In this section, we compare the platform's revenues under the two revenue models and study the conditions under which the advertising model can generate more revenue than the brokerage model. We also examine the sellers' payoffs, the buyers' payoffs, and the social welfare under the two revenue models.

## 4.1 The Platform's Revenue

We first consider the platform's revenues under the two revenue models. The following proposition summarizes the results of comparing the equilibrium revenues derived in Propositions 1 and 2.

Proposition 3. When $p > \bar{p}(a)$ , the brokerage model generates more revenue for the platform than the advertising model; when $p < \bar{p}(a)$ , the advertising model generates more revenue. The cutoff curve $\bar{p}(a)$ is defined as

$$
\bar {p} (a) = \left\{ \begin{array}{l l} 0 & \text { if } a \in \left[ 0, \frac {4}{2 7} \right] \\ \frac {2 7 a - 4}{3 1 a - 4} & \text { if } a \in \left[ \frac {4}{2 7}, \frac {8}{2 3} \right] \\ p ^ {*} (a) & \text { if } a \in \left[ \frac {8}{2 3}, 1 \right] \end{array} \right.\tag{23}
$$

in which $p^*(a)$ is determined by $\left[-2 + 3\delta + 3\delta^2 - 2\delta^3 + 2(1 - \delta + \delta^2)^{\frac{3}{2}}\right] = 4\delta p^2$ , and $\delta$ is defined in Equation (14).

Figure 2a shows the curve $\bar{p}(a)$ and illustrates the comparison results. When the space dedicated to advertising $a$ is very small, the brokerage model always generates more revenue than the advertising model. The reason is that, under the advertising model, the platform's revenue comes from the advertising space $a$ , and the organic space is offered for free. When the space dedicated to advertising is very small, the revenue generated from advertising is limited. As a result, the advertising model generates less revenue than the brokerage model, in which each transaction is charged by the platform.

![](/api/attachments/QGR77UYQ/fulltext/images/46d472e1d135d91f6bfabc709ce27465d5a659a3867dff155480661cc7f57841.jpg)  
(a) Platform's Revenue

![](/api/attachments/QGR77UYQ/fulltext/images/8507aaf82084ddfa8b596cbece1537c30ae494300cbe9ec5538e4cb702ba0951.jpg)  
(b) Sellers' Payoffs

![](/api/attachments/QGR77UYQ/fulltext/images/2cbff4726bb53c4a1435b2e7f6234d35eb4a8ac8158009089cc8a373b871e4f2.jpg)  
(c) Social Welfare  
Figure 2: Equilibrium Comparison under the Two Revenue Models

This finding indicates that when a significant proportion of space is dedicated to advertising, the matching probability with which buyers find sellers plays a critical role in determining which revenue model is better. If the matching probability is high, the brokerage model generates more revenue than the advertising model; otherwise, the advertising model generates more revenue. The intuition is as follows. Under the brokerage model, when the matching probability that buyers will find their trading partner is low, buyers' payoffs are low, and a small number of buyers participate. In addition, even if a trading pair is on the platform, a low matching probability indicates that the likelihood of a trade is low. Therefore, the matching probability that trading partners will find one another monotonically affects the platform's revenue: The higher the probability is, the greater the platform's revenue. Under the advertising model, the probability on the buyer side has a similar effect—high matching probability tends to induce more buyers to participate in the platform. However, in sharp contrast to the brokerage model, when the probability of the seller's being noticed by buyers is low, the advertising service is highly valuable to sellers; the platform thus can charge a high price and earn high revenue. This difference—the change in the platform's revenue that occurs with the change in probability that the sellers are noticed by buyers—explains the existence of the cutoff: Once the matching probability falls below a certain threshold, the advertising model generates more revenue than the brokerage model.

This finding might also be used to explain the different business practices established by Taobao in China and by eBay in America. When Taobao started its business in 2003, its matching function, enabled by the underlying search function and categorizations, was in a less advanced stage than eBay's. More importantly, e-commerce was a relatively new phenomenon, and consumers were less experienced and less skillful in shopping online. These factors all contribute to a lower probability that buyers can find trading partners on the platform. Therefore, Taobao's use of the advertising model made—and makes—economic sense.

## 4.2 Sellers' Payoffs

We next examine sellers' payoffs under the two revenue models.

Under the brokerage model, the sellers with costs in $[0, k_{B}^{*}]$ participate in the platform. By Equation (4), we can formulate the equilibrium payoff of a participating seller with cost k as

$$
m _ {B} ^ {*} p (\pi - k - \tau^ {*}) = \frac {2}{3} p ^ {2} s \pi (\frac {2}{3} \pi - k)\tag{24}
$$

where the equality is achieved by substituting in both the optimal transaction fee $\tau^{*}$ derived in Proposition 1 and the equilibrium mass of participating buyers outlined in Equation (10).

Under the advertising model, the sellers with costs in $[k_{A}^{\prime*}, k_{A}^{*}]$ participate in the platform for the basic service only (without advertising), and the sellers with costs in $[0, k_{A}^{\prime*}]$ participate in the advertising service in addition to the basic service. By letting I = 0 in Equation (6), we can formulate the equilibrium payoff of a participating seller with cost k in $[k_{A}^{\prime*}, k_{A}^{*}]$ as

$$
m _ {A} ^ {*} (1 - a) p (\pi - k)\tag{25}
$$

where the equilibrium mass of participating buyers is outlined in Equation (22). By letting I = 1 in Equation (6), we can formulate the equilibrium payoff of a participating advertiser with cost k in $[0, k_{A}^{\prime*}]$ as

$$
m _ {A} ^ {*} (\pi - k) - \theta^ {*}\tag{26}
$$

where the optimal advertising fee $\theta^{*}$ is outlined in Equation (19).

One important feature of the advertising model is that it offers a two-tiered service: the free basic service and the paid advertising service. Because of the free basic service, the advertising model generally attracts more sellers to participate in the platform than the brokerage model. In particular, $k_{B}^{*} = \frac{2}{3}\pi < \pi = k_{A}^{*}$ by Equations (9) and (20). Meanwhile, we can verify that the number of sellers who opt to advertise under the advertising model is less than the number of participating sellers under the brokerage model; that is, $k_{A}^{\prime *} < k_{B}^{*}$ .

The sellers with costs in $(k_{B}^{*}, k_{A}^{*})$ are all better off under the advertising model. These sellers do not participate in the platform under the brokerage model because their low profit margins (resulting from high costs) cannot compensate for the transaction fee charged by the platform. In contrast, under the advertising model, they have an incentive to participate because the basic service is free and they can reap their profit from sales on the platform. Therefore, they are better off under the advertising model.

For the sellers with costs in $[0, k_{B}^{*}]$ , we need to compare their payoffs under the two revenue models to determine who is better off under which model.

Proposition 4. (a) The sellers with costs in $(k_{B}^{*}, k_{A}^{*})$ are better off under the advertising model.

(b) For sellers with costs in $[0, k_B^*]$ , if $p > \tilde{p}(a)$ , all these sellers are better off under the advertising model; if $p < \tilde{p}(a)$ , the sellers with cost $k \in \left(\frac{5\pi p}{3(3 - 2p)}, \frac{9a - 5}{9a - 3}\pi\right) \subset [0, k_B^*]$ are worse off under the advertising model, and other sellers are better off, where

$$
\tilde {p} (a) = \left\{ \begin{array}{l l} 0 & \text {   if   } a \in \left[ 0, \frac {5}{9} \right] \\ \frac {9 a - 5}{1 1 a - 5} & \text {   if   } a \in \left[ \frac {5}{9}, 1 \right] \end{array} \right.\tag{27}
$$

Figure 2b shows the $\tilde{p}(a)$ curve and illustrates the results. The intuition for (b) is as follows. First, the seller with cost $k_B^*$ is better off under the advertising model, because under the brokerage model she is the marginal seller who is indifferent about participating in the market or not and who earns zero payoff, whereas under the advertising model, she earns positive payoff (by participating in the basic platform service for free). Because of the continuity in their payoff functions, the sellers with costs close to $k_B^*$ are also better off under the advertising model. Second, the sellers with costs close to zero are also better off under the advertising model. Compared to the brokerage model, advertised sellers under the advertising model benefit from the increased exposure. Under the brokerage model, all the sellers get the same exposure. Under the advertising model, advertised sellers receive more exposure than they would under the brokerage model because advertising essentially shifts buyers' attention toward the advertised sellers from the unadvertised sellers. The sellers with very low fixed costs who participate in the advertising service (by Lemma 2) benefit more than their high-cost counterpart advertisers because of their different profit margins. As the optimal advertising fee is established on the basis of the average benefit from advertising for different sellers, the advertisers with very low costs benefit more than average and are better off under the advertising model.

Sellers with intermediate costs might be worse off under the advertising model when the space left for organic listing is limited and matching probability is low. First, when the organic space is small (and advertising space is large), the value of free organic listing is limited because of the limited exposure. As a result, the payoff of sellers under the free organic service might not be as good as their payoff under the brokerage model, even though sellers pay transaction fees for each sale. Second, when the matching probability is low, the advertising service is very valuable, and in equilibrium the advertising fee is not proportionally low and could even be high. As a result, when sellers with intermediate costs participate in the advertising service, they might not benefit a lot because of relatively high advertising fees. Thus, their payoff from advertising might not be as good as their payoff under the brokerage model.

It is worth noting that when the advertising space is small, leaving significant space for organic listing, all sellers are better offer under the advertising model, including the sellers with intermediate costs (by Figure 2b). This is because the significant organic listing presents all sellers a valuable option by its nature of being free. Some of sellers with intermediate costs continue to pay to be listed in the advertising space in equilibrium. Different from the case with limited organic listing space, their choice to pay the advertising fee comes after considering the valuable organic listing.

These days “being free” or being free to some extent has become a popular practice in the digital world. For example, software firms often use freemium business models (Niculescu and Wu, 2014), in which software firms offer basic versions for free and charge for advanced versions. The advertising model adopted by online C2C platforms shares a similar spirit and has shown promise. For instance, based on free basic service and paid advertising service, Taobao has attracted more than 500 million users in China. Canada's most popular local classifieds site, www.kijiji.ca (owned by eBay), uses a similar model: it offers a free online listing service for people in the same city to trade and help each other out in areas such as goods, services, housing, and jobs; Meanwhile, Kijiji also provides an advertising service to sellers who are willing to pay Kijiji to be listed in prominent positions for a certain period. The essential ideal of the advertising model for a C2C trading platform is that sellers can self-select to use the free service only or participate into the advertising service. With a valuable free service (e.g., organic space being not too small), sellers embrace the platform regardless of whether they choose to pay for advertising, because at least all of them have to option to use the basic service for free.

## 4.3 Buyers' Payoffs

We can similarly examine buyers' payoffs under the two revenue models. Under the brokerage model, the buyers with costs in $[0, c_B^*]$ participate in the platform. By Equation (3), we can formulate the equilibrium payoff of a participating buyer with cost $c$ as

$$
n _ {B} ^ {*} p s - c = \frac {2}{3} p \pi s - c\tag{28}
$$

where the equality is achieved by substituting in the equilibrium mass of participating sellers outlined in Equation (9). Under the advertising model, the sellers with costs in $[0, c_{A}^{*}]$ participate in the platform. By Equation (5), we can formulate the equilibrium payoff of a

participating buyer with cost $c$ as

$$
[ (n _ {A} ^ {*} - n _ {A} ^ {\prime *}) p _ {1} + n _ {A} ^ {\prime *} ]   s - c = \left\{ \begin{array}{l l} \frac {2 - \delta + \sqrt {1 - \delta + \delta^ {2}}}{3} \pi s - c & \text { if } p > \hat {p} (a) \\ p \pi s - c & \text { if } p \leq \hat {p} (a), \end{array} \right.\tag{29}
$$

where the equality is achieved by substituting in $\delta = 1 - p_{1}$ and the equilibrium mass of participating sellers outlined in Equation (20).

Because consumers have the same opportunity cost under the two revenue models, whether they are better off under one model simply depends on the probability that they can find their trading partners (i.e., the mass of participating sellers times the matching probability). Under regular advertising (when $p < \hat{p}(a)$ ), buyers derive a higher benefit from the advertising model because more sellers participate in the advertising platform (i.e., $n_{A}^{*} = \pi > n_{B}^{*} = \frac{2}{3}\pi$ ), while the average matching probability is the same under the two revenue models.

Under excessive advertising, the average matching probability under the advertising model is lower than the probability under the brokerage model (but the number of participating sellers is larger in the former). With an arbitrarily high advertising fee (such that only few sellers participate in the advertising service), buyers might be worse off because of a significant decrease in the average matching probability resulting from excessive advertising. However, in choosing the optimal advertising fee, the platform considers not only the direct effect of the advertising fee on the number of participating advertisers, but also the indirect effect on buyers' participation, driven by the benefit that buyers derive from the platform. As a result, we can verify that even with excessive advertising in equilibrium, buyers are better off under the advertising model.

Proposition 5. Buyers are better off under the advertising model.

Also, because the benefits for buyers under the advertising model are higher than they are under the brokerage model, in equilibrium more buyers participate in the platform under

the advertising model.

## 4.4 Social Welfare

We next examine the social welfare under the two revenue models. In our setting, social welfare is the value created by the platform, which can be measured by the total value realized by the transactions on the platform net the costs associated with both the sellers and buyers.

Under the brokerage model, the number of transactions is $m_{B}^{*}n_{B}^{*}p$ , and the value created from each transaction is $s + \pi$ . The average cost on the seller side is $k_{B}^{*}/2$ , and the average opportunity cost on the buyer side is $c_{B}^{*}/2$ . Therefore, the social welfare under the brokerage model is

$$
W _ {B} = m _ {B} ^ {*} n _ {B} ^ {*} p \left(s + \pi - \frac {k _ {B} ^ {*}}{2}\right) - m _ {B} ^ {*} \frac {c _ {B} ^ {*}}{2} = \frac {2}{3} p s \pi \frac {2}{3} \pi p \left(s + \pi - \frac {\pi}{3}\right) - \frac {2}{9} (p s \pi) ^ {2}\tag{30}
$$

where the equality is achieved by substituting in $(m_{B}^{*}, k_{B}^{*})$ and $(n_{B}^{*}, c_{B}^{*})$ from Equations (9) and (10). Similarly, we can formulate social welfare under the advertising model as

$$
W _ {A} = m _ {A} ^ {*} \left[ (n _ {A} ^ {*} - n _ {A} ^ {\prime *}) p _ {1} \left(s + \pi - \frac {k _ {A} ^ {*} + k _ {A} ^ {\prime *}}{2}\right) + n _ {A} ^ {\prime *} \left(s + \pi - \frac {k _ {A} ^ {\prime *}}{2}\right) \right] - m _ {A} ^ {*} \frac {c _ {A} ^ {*}}{2}\tag{31}
$$

where $(n_{A}^{*}, k_{A}^{*})$ , $(n_{A}^{\prime*}, k_{A}^{\prime*})$ , and $(m_{A}^{*}, c_{A}^{*})$ are specified in Equations (20), (21), and (22), respectively. Comparing the social welfare under the two revenue models as derived leads to the following conclusion.

Proposition 6. The advertising model generates more social welfare than the brokerage model.

The intuition is as follows. First, compared with the brokerage model, more buyers participate in the trading platform under the advertising model, as explained in the previous section, because the probability (i.e., the mass of participating sellers times the matching (probabilities) that they find their trading partners is higher under the advertising model. As a result of the greater participation by buyers and the higher trading probability, more transactions take place under the advertising model. Second, the lower cost sellers participate in the advertising service and receive more attention from buyers. Therefore, a product from a lower cost seller is more likely to be sold than a product of a high-cost counterpart under the advertising model, and lower cost products are sold more often under the advertising model than under the brokerage model. Both the increased volume of transactions and the increased transactions of low-cost products under the advertising model increase social welfare, compared to the brokerage model.

Note that, compared to the brokerage model, the advertising model may lead to a win-win-win result in equilibrium; that is, the platform, the (participating) sellers, and the (participating) buyers might all be better off under the advertising model at the same time. Figure 2c depicts the win-win-win area in the $(a,p)$ space; that is, $\tilde{p}(a) < p < \bar{p}(a)$ . By Proposition 3, when $p < \bar{p}(a)$ , the platform is better off under the advertising model, and by Proposition 4, when $p > \tilde{p}(a)$ , all participating sellers are better off as well. Meanwhile, by Proposition 5, buyers are always better off under the advertising model. Therefore, when both conditions $p < \bar{p}(a)$ and $p > \tilde{p}(a)$ are satisfied, the win-win-win outcome occurs. The win-win-win result is possible because the advertising model generates more social welfare, so that the total “pie” is bigger under the advertising model. We summarize this result in the following corollary.

Corollary 4. When $\tilde{p}(a) < p < \bar{p}(a)$ , the platform, the sellers, and the buyers are all (weakly) better off under the advertising model at the same time, where $\tilde{p}(a)$ and $\bar{p}(a)$ are defined in Equations (23) and (27), respectively.

It is worth highlighting that “being free” under the advertising model plays a critical role in driving the above result. Because of its free basic platform service under the advertising model, compared to the brokerage model, the platform is able to induce more sellers (i.e., the sellers with low profit margins) to participate, which in turn induces more buyers to participate due to the nature of the two-sided market. The increased participation increases the number of transactions, which in turn makes it possible that each involved player gain from the advertising model.

## 5 Extensions and Discussion

In this section, we extend the baseline model by considering cases when buyers have heterogeneous search skills, when the total exposures under the two business models are unequal, when buyers are averse to advertising, and when sellers compete with each other. Finally, we also include some discussion about platform competition.

## 5.1 Buyers with Heterogeneous Search Skills

In the baseline model, we assume that if a buyer's trading partner is on the platform, the buyer can find her partner with probability $p$ , and this probability is the same across different buyers. In general, the probability that a buyer can find her partner can be affected by both the platform's search and categorization technologies and buyers' online search skills. While the platform's technologies are the same for all buyers, buyers might have different search skills in general. In this section, we extend the baseline model to the case in which buyers have heterogeneous search skills.

We here assume that the probability that a buyer can find her trading partner (given her partner being on the platform) is determined by the platform's technologies and her own search skill. In particular, we assume the probability equal to $\mu p$ , where $\mu$ measures each buyer's own search skill and $p$ , as in the baseline model, is the same for all buyers and here measures the platform's technologies. We assume that at the aggregate level $\mu$ follows a distribution $f(\mu)$ over support [0, 1] and is independent of her opportunity cost. Everything else follows the baseline model.

Under this setting, the marginal buyers that we define in Equations (8) and (11), $c_{B}$ for the brokerage model and $c_{A}$ for the advertising model, are the marginal buyers with search skill 1 (the highest search skill). As in the baseline model, the buyers with opportunity costs higher than $c_{i}, i \in \{A, B\}$ , do not participate. Different from the baseline model, some buyers with opportunity costs less than $c_{i}$ do not participate either, because of their low search skills. Among the buyers with a certain level of search skill $\mu$ , we can similarly define the marginal buyer $c_{i}(\mu)$ who is indifferent in participating in the platform or not. The buyers with opportunity costs less than $c_{i}(\mu)$ participate in the platform and the buyers with higher cost do not. Under the brokerage model, for example, similar to Equation (8), the marginal buyer is defined by

$$
c _ {B} (\mu) = k _ {B} \mu p s = (\pi - \tau) \mu p s\tag{32}
$$

Combining with (8), we can derive $c_{B}(\mu) = \mu c_{B}$ . Similarly, under the advertising model we have $c_{A}(\mu) = \mu c_{A}$ . These marginal buyers segment the buyer group and define the participating buyers. The line $c_{i}(\mu)$ in Figure 3 illustrates the marginal buyers and the gray area shows the participating buyers.

![](/api/attachments/QGR77UYQ/fulltext/images/a71deaa3e7f0d45388cbd27b5e86d619a21a805e7f52a017a3d8e6e805daea2d.jpg)  
Figure 3: Marginal Buyers and Participating Buyers

Based on these redefined marginal users, we can duplicate the results in the baseline model. For example, we can derive the platform's revenue under the brokerage model as

$$
\int_ {0} ^ {1} \int_ {0} ^ {c _ {B} (\mu)} (\pi - \tau) \mu p \tau f (\mu) d c d \mu = \int_ {0} ^ {1} (\pi - \tau) ^ {2} \mu^ {2} p ^ {2} s \tau f (\mu) d c d \mu = \bar {\bar {\mu}} p ^ {2} s \tau (\pi - \tau) ^ {2}\tag{33}
$$

where $(\pi - \tau)$ on the left-hand side is the mass of the participating sellers, the first equality is because of Equation (32), and the second equality is by defining $\bar{\mu} \equiv \int_{0}^{1} \mu^{2} f(\mu) d\mu$ . As we can see, the platform's revenue in this case differs from the revenue in the baseline case only in the constant $\bar{\mu}$ . Therefore, the optimal transaction fee is the same as in the baseline model and the platform's maximum revenue is $\bar{\mu}$ times the revenue in the baseline mode.

Under the advertising model, we can reformulate the condition for marginal advertiser in Equation (13) as follows, considering that buyers have different search skills:

$$
\theta = \int_ {0} ^ {1} \int_ {0} ^ {c _ {A} (\mu)} \mu [ \min \{p _ {2}, 1 \} - p _ {1} ] (\pi - k _ {A} ^ {\prime}) f (\mu) d c d \mu = \bar {\bar {\mu}} c _ {A} [ \min \{p _ {2}, 1 \} - p _ {1} ] (\pi - k _ {A} ^ {\prime})\tag{34}
$$

Notice that $\theta k_A'$ is the platform's revenue. As under the brokerage model, the platform's revenue in this case differs from the revenue in the baseline case only in the constant $\bar{\mu}$ . Based on an optimization problem similar to Equation (19), we can verify that the optimal marginal advertiser chosen is the same as in the baseline model, and the optimal advertising fee and platform's maximum revenue is $\bar{\mu}$ times that in the baseline mode.

Based on this framework, we can verify that the main results in the baseline model carry over to this extension and the insights derived in the baseline model continue to hold. For example, Proposition 3 about the platform's revenue comparison stays the same because, as illustrated in Equations (33) and (34), the revenues in this extension are simply scaled by the same constant $\bar{\mu}$ from the baseline model. We can also show Proposition 4 about the sellers' payoffs remains the same because, similar to what is shown in Equations (24), (25), and (26), we can derive sellers' payoffs under the brokerage model and advertising model and verify they are also scaled by the same constant $\bar{\mu}$ from the baseline model. Similarly, we can verify that the results in Propositions 5 and 6 remain valid.

## 5.2 When the Total Exposure is Unequal

In the baseline model, we assume that, given the same number of participating sellers, the total exposure under the advertising model is equal to the total exposure under the brokerage model. Such an assumption is for fair comparison purposes and the results under this assumption serve as a baseline. When the total exposure is unequal, the comparison might tip toward the business model that can more effectively expose participating sellers to buyers. The total exposure might differ because the platform under the two business models, for example, might have different designs of web pages displaying sellers. While the brokerage model displays all the sellers in one place, the advertising model has to distinguish advertised sellers and unadvertised sellers and thus typically displays sellers in two differentiated blocks (e.g., two columns on Taobao, with the left side column displaying unadvertised sellers and right side displaying advertised sellers).

We next illustrate that when the total exposure is unequal, we can duplicate the analysis, and as long as the exposure levels under the two business models are comparable, all the results continue to hold qualitatively and the insights delivered by the baseline model carry over. In this extension, we use the case with the total exposure under the advertising model less than that under the brokerage model to illustrate; that is, $(n - n')p_{1} + n'p_{2} < np$ . The other case can be similarly analyzed. Given the same number of participating sellers, we define an exposure ratio of the total exposure under the advertising and brokerage models $\gamma, \gamma \in (0,1]$ , such that $(n - n')p_{1} + n'p_{2} = \gamma np$ . The case with $\gamma = 1$ corresponds to the baseline model. Noticing that the equilibrium under the brokerage model remains the same as in the baseline model, we next analyze the equilibrium under the advertising model.

Similar to the baseline model, we let $p_{1} = \gamma(1 - a)p$ , in which a reflects the space dedicated to advertising. As in Equation (2), we can derive the additional exposure gained from advertising: $p_{2} - p_{1} = \frac{\gamma apn}{n'}$ . Similarly, we define the maximum increase in the probability of a seller being noticed by potential buyers: $\delta \equiv 1 - \gamma(1 - a)p$ . Based on this newly defined $\delta$ , after the reasoning similar to that in the baseline model, we can formulate the platform's

optimization problem as follows:

$$
\max _ {0 <   k _ {A} ^ {\prime} <   \pi} \delta s \left[ \pi (\pi - k _ {A} ^ {\prime}) - \delta (\pi - k _ {A} ^ {\prime}) ^ {2} \right] k _ {A} ^ {\prime}\tag{35}
$$

$$
\mathrm{s.t.} p _ {2} = \gamma (1 - a) p + \frac {\gamma a p \pi}{k _ {A} ^ {\prime}} \geq 1\tag{36}
$$

Note that the objective function (35) takes the same form as in the baseline model (Equation (17)) except the difference in the definitions of $\delta$ . Constraint (36) is similar to the constraint in the baseline model, Equation (18), but adjusted by $\gamma$ . Solving this optimization problem, we can derive the optimal advertising fee ( $\theta^{*}$ ) and the platform's maximum revenue ( $\Pi^{*}$ ) as in Proposition 2. We can show that now the cutoff curve $\hat{p}(a)$ becomes $\hat{p}(a) = \frac{1 + a}{\gamma(1 + 2a)}$ (compared to $\hat{p}(a) = \frac{1 + a}{1 + 2a}$ in the baseline model). When $p > \hat{p}(a)$ , $\theta^{*}$ and $\Pi^{*}$ take the same form as in Proposition 2. When $p \leq \hat{p}(a)$ ,

$$
\theta^ {*} = \gamma p (1 - \gamma p) s \pi^ {2} \mathrm{and} \Pi^ {*} = \frac {(1 - \gamma p) a}{\delta} \gamma^ {2} p ^ {2} s \pi^ {3}
$$

which, again, are similar to that in Proposition 2, but adjusted by $\gamma$ .

Based on the equilibrium outcome, we can similarly compare the two business models in terms of the platform's revenue, sellers' and buyers' payoffs, and social welfare. We can show, as long as $\gamma$ is close to 1, all the results continue to hold qualitatively and the insights are the same. For example, as in Proposition 3, we can derive the cutoff curve above which the brokerage model generates more revenue for the platform owner than the advertising model. The cutoff curve $\bar{p}(a)$ now becomes a function of $\gamma$ :

$$
\bar {p} (a) = \left\{ \begin{array}{l l} 0 & \text {if} a \in \left[ 0, \frac {4}{2 7 \gamma^ {2}} \right] \\ \frac {2 7 a \gamma^ {2} - 4}{\gamma (2 7 a \gamma^ {2} - 4 + 4 a)} & \text {if} a \in \left[ \frac {4}{2 7 \gamma^ {2}}, \frac {8}{2 7 \gamma^ {2} - 4} \right] \\ p ^ {*} (a) & \text {if} a \in \left[ \frac {8}{2 7 \gamma^ {2} - 4}, 1 \right] \end{array} \right.
$$

where $p^{*}(a)$ is as defined in Proposition 3. As in the baseline model, when the space dedicated to advertising is small, the brokerage model outperforms the advertising model for the platform owner. When the advertising space is significant, which business model generates more revenue depends on the matching probability $p$ : if the matching probability is low, the advertising model can generate more revenue; otherwise, the brokerage model generates more revenue. Therefore, the pattern of the cutoff curve is the same as in the baseline model and the insights continue to be valid. The main difference from the baseline model is that the cutoff curve now depends on $\gamma$ . In the extreme, when $\gamma$ is very small (i.e., when $\gamma^2 < \frac{4}{27}$ ), the brokerage model always generates more revenue than the advertising model for the platform owner. Such an effect is intuitive: if the advertising model is ineffective at exposing the participating sellers to the buyers (compared to the brokerage model), the platform's revenue is hurt because, after all, the exposure is the platform's revenue source.

## 5.3 Buyers' Advertising Aversion

In the baseline model, we assume that advertising increases an advertised seller's exposure and advertising has no negative effects on buyers. This assumption is sensible in our setting because, unlike traditional media, such as magazines or TV, on which advertising could be intrusive or distractive and thus negatively affects the audience, in our setting the platform is a dedicated C2C trading platform and buyers come to this platform to seek sellers. Advertising on this platform is simply to give the sellers who participate in the advertising service more exposure and to make them more likely to be noticed by potential buyers.

We next illustrate that even if buyers are indeed averse to advertising for some reason, we can still duplicate the analysis, and as long as the extent of aversion is mild, all the results continue to hold qualitatively and the insights delivered by the baseline model carry over. We model this negative effect of advertising by introducing different conversion rates for the organic listing and the advertising list. In particular, we normalize the conversion rate from the organic listing to 1 (as in the baseline model), but now we consider the conversion rate from the advertising list is not necessarily the same as that from the organic listing.

We denote the conversion rate from the advertising list as $\rho$ , $\rho \in (0,1]$ . Notice that given the conversion rate for organic listing being normalized to 1, $\rho$ measures buyers' aversion to advertising. The case with $\rho = 1$ corresponds to the baseline model in which buyers are not averse to advertising.

Noticing that the equilibrium under the brokerage model remains the same as in the baseline model, we next analyze the equilibrium under the advertising model. Similar to Equations (11), (12), and (13) in the baseline model, we can characterize buyers' and sellers' participation conditions as follows:

$$
\left[ k _ {A} p _ {1} + \rho k _ {A} ^ {\prime} (\min \{p _ {2}, 1 \} - p _ {1}) \right] s - c _ {A} = 0\tag{37}
$$

$$
c _ {A} p _ {1} (\pi - k _ {A}) = 0\tag{38}
$$

$$
c _ {A} \rho (\min \{p _ {2}, 1 \} - p _ {1}) (\pi - k _ {A} ^ {\prime}) - \theta = 0\tag{39}
$$

The main difference from the baseline model is that now even if a participating buyer finds his trading partner from the advertising list, the buyer does not necessarily purchase from the seller because of advertising aversion. With the same reasoning as in the baseline model, we can simplify the above conditions to $c_A = [(1 - \delta)\pi + \rho\delta k_A'] s$ and $\theta = c_A\rho\delta(\pi - k_A')$ , and we can formulate the platform's optimization problem as follows:

$$
\max _ {0 <   k _ {A} ^ {\prime} <   \pi} \rho \delta s \left[ (1 - \delta + \rho \delta) \pi (\pi - k _ {A} ^ {\prime}) - \rho \delta (\pi - k _ {A} ^ {\prime}) ^ {2} \right] k _ {A} ^ {\prime}\tag{40}
$$

$$
\mathrm{s.t.} p _ {2} = (1 - a) p + \frac {a p \pi}{k _ {A} ^ {\prime}} \geq 1\tag{41}
$$

Note that the objective function (40) takes a form similar to that in the baseline model (Equation (17)) except that now the coefficients contain $\rho$ . Solving this optimization problem, we can derive the optimal advertising fee ( $\theta^{*}$ ) and the platform's maximum revenue ( $\Pi^{*}$ ) as in Proposition 2. We can show that now the cutoff curve $\hat{p}(a)$ becomes $\hat{p}(a) = \frac{1 + a(2\rho - 1)}{1 + 2a\rho + a^2(\rho - 1)}$ (compared to $\hat{p}(a) = \frac{1 + a}{1 + 2a}$ in the baseline model).

Based on the equilibrium outcome, we can similarly compare the two business models in terms of the platform's revenue, sellers' and buyers' payoffs, and social welfare. We can show that, as long as $\rho$ is close to 1, all the results continue of hold qualitatively and the insights are the same. For example, as in Proposition 3, we can derive the cutoff curve above which the brokerage model generates more revenue for the platform owner than the advertising model. The cutoff curve $\bar{p}(a)$ now becomes a function of $\rho$ :

$$
\bar {p} (a) = \left\{ \begin{array}{l l} 0 & \text {if} a \in \left[ 0, \frac {8}{2 7 \rho + 3 \sqrt {8 1 \rho^ {2} + 4 8 \rho (\rho - 1)}} \right] \\ \frac {2 7 a ^ {2} \rho (\rho - 1) + 2 7 a \rho - 4}{2 7 a ^ {2} \rho (\rho - 1) + (2 7 \rho + 4) a - 4} & \text {if} a \in \left[ \frac {8}{2 7 \rho + 3 \sqrt {8 1 \rho^ {2} + 4 8 \rho (\rho - 1)}}, a ^ {*} \right] \\ p ^ {*} (a) & \text {if} a \in [ a ^ {*}, 1 ] \end{array} \right.
$$

where $a^{*}$ is determined by $\frac{27a^{2}\rho(\rho-1)+27a\rho-4}{27a^{2}\rho(\rho-1)+(27\rho+4)a-4}=\frac{1+a(2\rho-1)}{1+2a\rho+a^{2}(\rho-1)}$ , and $p^{*}(a)$ is similarly defined as in Proposition 3 by equaling the revenues under the two business models. As in the baseline model, when the space dedicated to advertising is small, the brokerage model outperforms the advertising model for the platform owner. When the advertising space is significant, which business model generates more revenue depends on the matching probability p: if the matching probability is low, the advertising model can generate more revenue; otherwise, the brokerage model generates more revenue. Therefore, the pattern of the cutoff curve is the same as in the baseline model and the insights remain valid. The main difference from the baseline lies in that the cutoff curve now depends on $\rho$ . For instance, as $\rho$ goes down, the range $\left[0,\frac{8}{27\rho+3\sqrt{81\rho^{2}+48\rho(\rho-1)}}\right]$ expands, in which the brokerage model always generates more revenue than the advertising model for the platform owner. Such an effect is intuitive: if the buyers are very averse to advertising, the value of advertising to sellers is very limited and so is the platform's revenue under the advertising model, and therefore the brokerage model outperforms the advertising model.

## 5.4 Seller Competition

In our baseline model we assume that each seller is seen as selling a different product, and thus the competition among sellers is not considered. This assumption is sensible for C2C platforms, because most sellers are either individuals or small business that typically sell no-brand products which could be very different from each other and unique. For example, on Taobao a large number of sellers sell apparel and most apparel items are no-brand. Some other platforms are even dedicated to trading unique products. For example, Etsy is a marketplace focusing on handmade or vintage items and supplies, as well as unique factory-manufactured items. Etsy highlights the uniqueness of products in its statement: "Etsy is a marketplace where people around the world connect to buy and sell unique goods" (https://www.etsy.com/about). Similar to Etsy, DaWanda, a Germany-based marketplace "where you can buy unique, customised and handmade products made by talented people, and sell your own creations" (http://en.dawanda.com/info/show/faq\_general#dawanda1), also emphasizes the uniqueness of products on its platform.

In addition, when it comes to two-sided markets (particularly C2C markets) and users' participation in the two-sided markets, the first-order consideration for each seller should be the likelihood that she can sell the product (and for each buyer should be the likelihood that he can find the product he needs). It is true that the number of sellers who sell substitute products could affect the competition and sellers' profitabilities, but this should be their second-order consideration.

In a general sense, different products are substitutes to some extent and sellers compete with each other. When the number of sellers is higher on a platform, the competition among them is higher. Although it is difficult to make a comprehensive and rigorous analysis for the general seller competition case, we believe the insights we deliver in this paper are robust. Intuitively, compared to the brokerage, under the advertising model, because of its free basic service, the platform is able to attract more sellers (even if they realize the competition), and sellers with relatively high profit margins are more likely to participate in the advertising service. The increased number of sellers in turn attracts more buyers. As in our base model, the social welfare should be increased because of increased number of transactions and these transactions more toward the sellers with lower costs. Buyers are better off because of the large number of sellers on the platform. Sellers with high costs are again better off under the advertising model, because now they benefit from the free basic service and they could have either not participated or have made little profit under the brokerage model. Sellers with medium costs might be worse off, for the same reason as in the base model—the free service is not attractive but the advertising is too costly. The same insight for the platform should also remain the same as long as the same-side competition is not devastating.

We next use a native model to illustrate the points explained above. As in the baseline model, we denote $\pi$ as the expected profit that a seller derives from finding her trading partner under the brokerage model, which can also be viewed as a seller's expected profit under the equilibrium number of sellers under the brokerage model ( $n_{B}^{*}$ ). Unlike the baseline model, under the advertising model we assume that a seller's expected profit is linearly decreasing in the additional participating sellers beyond $n_{B}^{*}$ , because of the presumed increased competition resulting from the increased number of participating sellers. That is, we assume that the expected profit is $\pi\left[1-\beta(n_{A}-n_{B}^{*})\right]$ , where $\beta$ is positive and captures the competition effect.

Similar to the baseline model, we can characterize buyers' and sellers' participation conditions under the advertising model:

$$
\left[ k _ {A} p _ {1} + k _ {A} ^ {\prime} \left(\min \{p _ {2}, 1 \} - p _ {1}\right) \right] s - c _ {A} = 0\tag{42}
$$

$$
c _ {A} p _ {1} \left[ \pi \left[ 1 - \beta (n _ {A} - n _ {B} ^ {*}) \right] - k _ {A} \right] = 0\tag{43}
$$

$$
c _ {A} \left(\min \{p _ {2}, 1 \} - p _ {1}\right) \left[ \pi \left[ 1 - \beta (n _ {A} - n _ {B} ^ {*}) \right] - k _ {A} ^ {\prime} \right] - \theta = 0\tag{44}
$$

Notice that when $\beta = 0$ , this case reduces to the baseline case. From the seller's partici-

pation condition, we can derive that

$$
n _ {A} = k _ {A} = \frac {\pi (1 + \beta n _ {B} ^ {*})}{1 + \beta \pi}
$$

We denote $\pi^{\prime}$ as

$$
\pi^ {\prime} \equiv \pi \left[ 1 - \beta (n _ {A} - n _ {B} ^ {*}) \right] = \pi \left(1 - \beta \frac {\pi - n _ {B} ^ {*}}{1 + \beta \pi}\right) = \pi \left(1 - \beta \frac {\pi - n _ {B} ^ {*}}{1 + \beta \pi}\right) = \pi \left(\frac {1 + \beta n _ {B} ^ {*}}{1 + \beta \pi}\right)
$$

With the same reasoning as in the baseline model, similarly we can simplify the above conditions to $c_{A} = [(1 - \delta)\pi' + \delta k_{A}'] s$ and $\theta = c_{A}\delta(\pi' - k_{A}')$ , and we can formulate the platform's optimization problem as follows:

$$
\max _ {0 <   k _ {A} ^ {\prime} <   \pi} \delta s \left[ \pi^ {\prime} (\pi^ {\prime} - k _ {A} ^ {\prime}) - \delta (\pi^ {\prime} - k _ {A} ^ {\prime}) ^ {2} \right] k _ {A} ^ {\prime}\tag{45}
$$

$$
\mathrm{s.t.} p _ {2} = (1 - a) p + \frac {a p \pi^ {\prime}}{k _ {A} ^ {\prime}} \geq 1\tag{46}
$$

Note that the above objective function takes the same form as in the baseline model except that we now have $\pi'$ instead $\pi$ because of the same-side competition effect. Similarly, we can derive the optimal advertising fee that the platform should charge as

$$
\theta^ {*} = \left\{ \begin{array}{l l} s \pi^ {2} \left(\frac {1 + \beta n _ {B} ^ {*}}{1 + \beta \pi}\right) ^ {2} \left[ \frac {1 + 2 \delta - 2 \delta^ {2} + (2 \delta - 1) \sqrt {1 - \delta + \delta^ {2}}}{9} \right] & \text {if} p > \hat {p} (a) \\ p (1 - p) s \pi^ {2} \left(\frac {1 + \beta n _ {B} ^ {*}}{1 + \beta \pi}\right) ^ {2} & \text {if} p \leq \hat {p} (a) \end{array} \right.
$$

The platform's maximum revenue is

$$
\Pi_ {A} ^ {*} = \left\{ \begin{array}{l l} \frac {s \pi^ {3}}{2 7 \delta} \left(\frac {1 + \beta n _ {B} ^ {*}}{1 + \beta \pi}\right) ^ {3} \left[ - 2 + 3 \delta + 3 \delta^ {2} - 2 \delta^ {3} + 2 (1 - \delta + \delta^ {2}) ^ {\frac {3}{2}} \right] & \text {if} p > \hat {p} (a) \\ \frac {(1 - p) a}{\delta} p ^ {2} s \pi^ {3} \left(\frac {1 + \beta n _ {B} ^ {*}}{1 + \beta \pi}\right) ^ {3} & \text {if} p \leq \hat {p} (a) \end{array} \right.
$$

Based on the equilibrium outcome, we can similarly compare the two business models in terms of the platform's revenue, sellers' and buyers' payoffs, and social welfare. We can show that as long as $\beta$ is mild, all of the results continue to hold qualitatively and the insights remain the same. For example, as in Proposition 3, we can derive the cutoff curve above which the brokerage model generates greater revenue for the platform owner than the advertising model. The cutoff curve $\bar{p}(a)$ now becomes a function of $\beta$ :

$$
\bar {p} (a) = \left\{ \begin{array}{l l} 0 & \text {if} a \in \left[ 0, \frac {4}{2 7 \left(\frac {3 + 2 \beta \pi}{3 + 3 \beta \pi}\right) ^ {3}} \right] \\ \frac {2 7 \left(\frac {3 + 2 \beta \pi}{3 + 3 \beta \pi}\right) ^ {3} a - 4}{\left[ 2 7 \left(\frac {3 + 2 \beta \pi}{3 + 3 \beta \pi}\right) ^ {3} + 4 \right] a - 4} & \text {if} a \in \left[ \frac {4}{2 7 \left(\frac {3 + 2 \beta \pi}{3 + 3 \beta \pi}\right) ^ {3}}, \frac {8}{\left[ 2 7 \left(\frac {3 + 2 \beta \pi}{3 + 3 \beta \pi}\right) ^ {3} - 4 \right]} \right] \\ p ^ {*} (a) & \text {if} a \in \left[ \frac {8}{\left[ 2 7 \left(\frac {3 + 2 \beta \pi}{3 + 3 \beta \pi}\right) ^ {3} - 4 \right]}, 1 \right] \end{array} \right.
$$

where $p^{*}(a)$ is similarly defined as in Proposition 3 by equaling the revenues under the two business models. As in the baseline model, when the space dedicated to advertising is small, the brokerage model outperforms the advertising model for the platform owner. When the advertising space is significant, which business model generates greater revenue depends on the matching probability p: if the matching probability is low, the advertising model can generate more revenue; otherwise, the brokerage model generates more revenue. Therefore, the pattern of the cutoff curve is the same as in the baseline model and the insights remain valid.

The main difference from the baseline lies in that the cutoff curve now depends on the $\beta$ . For instance, as $\beta$ increases, the range $\left[0, \frac{4}{27\left(\frac{3+2\beta\pi}{3+3\beta\pi}\right)^{3}}\right]$ expands, in which the brokerage model always generates more revenue than the advertising model for the platform owner. Such an effect is intuitive: if the sellers' payoffs are very sensitive to the increase in the number of participating sellers, the sellers' payoffs are significantly lower under the advertising model than under the brokerage model. Therefore, their incentives to participating in the advertising service under the advertising model are low and the resulting revenue for the platform owner is low, which explains why the brokerage model outperforms the advertising model.

## 5.5 Platform Competition and Dynamics

So far, we consider the platform as a monopolist choosing its revenue model and study the implications of that choice. Next, we use the example of eBay and Taobao to illustrate competition between platforms. eBay entered China in 2003 and was the first mover in the Chinese C2C sector. Taobao was founded in 2003 and appeared as a new entrant to this sector then. eBay China lost its market leader position to Taobao in 2006 as the result of competition, and ever since Taobao has played a dominant role in the Chinese C2C sector.

When it entered the Chinese market in 2003, eBay adopted the same brokerage revenue model as it used in the U.S. market—which by then had already been well established and successful in the United States. When Taobao launched its platform, it offered its service totally free to both buyers and sellers (and later it provided advertising service in addition to the free organic listing). We next consider an incumbent platform with the brokerage model and an entrant platform employing the advertising model. We focus on the competition when the entrant platform enters the market. For illustrative purpose, we assume that the incumbent platform does not price strategically to deter potential entry; that is, the incumbent simply charges the optimal monopoly transaction fee, as discussed in Section 3.1. The incumbent platform might act like this, because, for example, it mistakenly assumes there are no strong potential competitors, as in the case of eBay in China. Thus, before the entry, the incumbent platform charges the optimal transaction fee $\tau^{*} = \frac{\pi}{3}$ , as prescribed in Section 3.1. In equilibrium, the sellers who have costs in $[0, k_{B}^{*}]$ and the buyers who have opportunity costs in $[0, c_{B}^{*}]$ participate in the platform, where $k_{B}^{*}$ and $c_{B}^{*}$ are defined as in Equations (9) and (10).

When the entrant platform comes to the market, consistent with the case of Taobao and for ease of exposition, we consider the case in which the entrant dedicates mild space to advertising (e.g., $a < \frac{1}{2}$ ). We next show that, even if the entrant simply employs its monopoly pricing strategy as prescribed in Section 3.2, the entrant could win over the incumbent's installed sellers and buyers in the competition. We explain the dynamics from both the seller and buyer sides. From the seller side, first, because of its free service, the entrant can attract the sellers with medium costs (i.e., the sellers with costs in $[k_{B}^{*}, \pi]$ ) to its platform, which are additional sellers beyond those using the incumbent platform. These sellers do not participate in the incumbent's platform because their expected benefit from participating in its platform is lower than the transaction fee charged due to their intermediate costs. Second, as shown in Proposition 4(b), when the advertising space is mild (such that $\tilde{p}(a) = 0$ ), all installed sellers on the incumbent's platform could be better off by switching to the entrant's platform. From the buyer side, first, expecting the increased seller base on the entrant's platform, the installed buyers would be better off by switching to the new platform, which can also be seen from the comparison of their payoffs under the two revenue models in Proposition 5. Second, because of the expanded seller base on it, the entrant platform could attract additional buyers to its platform as well. As a result, the equilibrium described in Corollary 2 can be sustained as the outcome of the competition, which implies that the entrant could win the competition against the incumbent and the typical winner-takes-all outcome in the competition for two-sided markets can also occur in our setting.

The above analysis illustrates that even if the entrant simply adopts the monopoly pricing strategy, it can win the competition and leave the incumbent with no market share. When the entrant prices strategically, the entrant can undoubtedly win the competition. What happened in the competition between eBay China and Taobao for the first couple of years was that Taobao opened its platform totally for free (i.e., a = 0), which is a special case of the above analysis. Under this special case, it is intuitive to see that, on one side, the installed sellers on eBay had incentive to switch to Taobao and meanwhile Taobao attracted additional sellers because of being free. On the other side, installed buyers on eBay had incentive to switch to Taobao because of the shift on the seller side, and meanwhile Taobao also attracted additional buyers because of the expanded seller base.

## 6 Conclusion

In this paper, we study how the choice of revenue model—between the brokerage model and the advertising model—affects the platform’s revenue, sellers’ payoffs, buyers’ payoffs, and social welfare. We find that both the size of the advertising space and matching probability play critical roles in the comparison. We also find that when a significant proportion of space is dedicated to advertising, if the matching probability is low, the advertising model generates more revenue; otherwise, the brokerage model generates more. Sellers are better off under the advertising model in most scenarios. The only exception is that when a limited space is left for organic listing and matching probability is low, some sellers with intermediate costs might be worse off under the advertising model. Buyers are always better off and social welfare is higher under the advertising model.

## 6.1 Managerial Implications

Our research has several implications. First, we underscore the importance of platform owners' tailoring their revenue models according to the platform design and technologies as well as and user experience with online platform shopping. The rule of thumb of choosing a revenue model for a C2C platform is that it should consider the space that can be dedicated to advertising and the platform's matching probability. Our analysis thus illustrates that the choice of revenue model should be assessed in line with technology development and user experience.

When the space that can be dedicated to advertising is small, the advertising model cannot beat the brokerage model and the platform should adopt the brokerage model. The space that can be dedicated to advertising should be determined based on various factors. For example, with a commonly used two-column page structure, if the space dedicated to advertising (typically in one column, such as in the case of Taobao) is too big and not balanced with the organic listing (typically in another column), the platform should investigate whether the resulting structure affects readability and the efficiency of displaying the information. If consumer experience is seriously affected, the platform should not risk dedicating much space to advertising and, more generally, should not risk using the advertising model. In addition, consumers' attitudes toward advertising also critically affect the desirability of the advertising model, because, after all, the revenue under the advertising model is solely from advertising. If the advertising model is used, the platform should minimize any possible negative effect of advertising on consumers by, for example, displaying equally relevant sellers in the both listings and by educating consumers that the advertising provides relevant information. If consumers are very averse to advertising and cannot be convinced about the role of advertising, the platform is better off using the brokerage model.

When a significant space can be dedicated to advertising, the matching probability, or how likely buyers can locate what they seek on the platform, plays a key role in determining which model can generate more revenue. If the platform has solid platform technologies (e.g., search and categorization technologies) and consumers have good search skills in general such that it is easy for buyers to locate the products, the platform should consider the brokerage model; Otherwise, the platform should consider the advertising model instead. In mature markets such as in the United States, where products and product descriptions are standardized, platform search and categorization technologies are advanced, and users have rich experience with online shopping, it is easy for buyers to find their purchase matches and complete the transactions and thus the brokerage model is more desirable. In contrast, matching probability could be lower in China, especially in early days of the e-commerce era, where products and product descriptions were highly heterogeneous, platform technologies were relatively rudimentary, and users were less experienced. In this case, the advertising model could outperform the brokerage model. Our result thus sheds light on why the two business models, represented by eBay in the United States and Taobao in China, are successful in their respective markets. This result is also consistent with the fact that the brokerage model has become a popular practice in mature markets. For example, in the United States, besides eBay, another popular platform Etsy.com uses the brokerage model as well. Etsy is a marketplace focusing on handmade or vintage items and supplies, as well as unique factory-manufactured items. Etsy charges a 3.5% fee on the sale price.

We also highlight the different effects of matching probability on the platform owners under the advertising and brokerage models. Under the brokerage model, the platform should always strive to improve the matching technology, for example, by making the platform easy to navigate and providing necessary help for users to locate products, because increased matching technologies mean increased number of transactions and hence increased revenue. In contrast, under the advertising model, the platform does not necessarily reap much benefit from improving technologies.

One caveat of the above discussion on business model choice is the cost associated with each model. The cost of running an online trading platform includes an one-time setup cost for hardware and software, as well as ongoing costs of providing matching and other services. Incorporating such costs, which we do not consider in this paper, will tip the balance further in favor of the business model with a lower cost.

Second, our analysis indicates that the advertising model generally benefits the users and increases user participation. With the basic service being free, the advertising model is able to attract a large number of sellers, which benefits the buyers and in turn induces more buyers to participate. Buyers should welcome the advertising model, as long as they are convinced that the advertising/promotion service delivers seller information as relevant as the organic listing and thus have the same receptiveness toward the sellers displayed in the organic listing and in advertising list. Sellers generally embrace the advertising model, because the sellers with low profit margins enjoy the free basic service and the sellers with high profit margins benefit from the additional exposure gained by advertising. The only exception is when the space left for organic listing is limited and matching probability is low. In this case, as indicated by our analysis, sellers with intermediate costs might be worse off under the advertising model and the platform should expect them to resist the advertising model. To prevent the sellers from leaving the platform (e.g., by establishing their own direct-sell websites), the platform could consider offering some special term for their business on its platform.

Finally, our research also has implications for social planners. As we illustrated in the analysis, the advertising model could generate more social welfare than the brokerage model. When the platform voluntarily adopts the advertising model, the allocation efficiency is naturally achieved. More importantly, in many cases, all the involved players, including the platform itself, the sellers, and the buyers, are better off, which leads to a win-win-win outcome. Of course, the choice of a platform owner is not always aligned with that of the social planner. When misalignment occurs, social planners might need to subsidize platform owners to induce socially advantageous revenue model choices. Again, another concern with the advertising model is the cost of implementation. In calibrating the net benefit from advertising model, such costs should be taken into account. When the cost becomes negligible compared to the benefit realized as the technology advances, advertising model should be promoted, and social planners may even consider subsidizing or facilitating the switch to advertising model.

## 6.2 Limitations and Future Research

This paper has several limitations that suggest directions for future research. As a future research direction, we can consider the competition between the two platforms using different business models. In the extension, we discuss the competition between eBay China and Taobao and illustrate how Taobao won the competition over eBay China. It will be interesting to consider a full-fledged competition model and systematically study the equilibrium outcome of competition. After all, the dominant role that Taobao holds in China can be viewed as the result of the competition. Also, although Google does not offer a trading platform, the competition between eBay and Google for certain sellers bears a similar flavor as the competition between eBay and Taobao because Google, similar to Taobao, offers a basic search service for free and a sponsored search service for sellers to purchase. Competitive positioning has long been discussed in the literature (e.g., Adner et al., 2012). We believe that a study of the competition between platforms would reveal additional insights beyond the extant literature. In addition, in the current model, we assume that sellers sell different products and do not compete with each other. Further systematic investigation of competition among sellers in this two-sided market framework may generate more insights. Finally, we do not examine the optimal advertising space that should be offered by the platform under the current framework. We believe that the optimal advertising space should be determined based on a number of various factors, including the other factors not considered in this paper. A systematic investigation on the optimal advertising space will complement our study.

## References

Adner, Ron, Felipe A. Csaszar, Peter B. Zemsky. 2012. Positioning on a multi-attribute landscape. Working Paper.

Anderson, Simon P., Stephen Coate. 2005. Market provision of broadcasting: A welfare analysis. The Review of Economic Studies 72(4) 947–972.

Bhargava, Hemant K., Vidyanand Choudhary. 2004. Economics of an information intermediary with aggregation benefits. Information Systems Research 15(1) 22–36.

Casadesus-Masanell, Ramon, Feng Zhu. 2010. Strategies to fight ad-sponsored rivals. Management Science 56(9) 1484–1499.

Casadesus-Masanell, Ramon, Feng Zhu. 2012. Business model innovation and competitive imitation: The case of sponsor-based business models. Strategic Management Journal forthcoming.

Chellappa, Ramnath K., Shivendu Shivendu. 2010. Mechanism design for “free” but “no free disposal services”: The economics of personalization under privacy concerns. Management Science 56(10) 1766–1780.

Chen, Rui, Raj Sharman, Raghav Rao, Shambhu J. Upadhyaya. 2013. Data model development for fire related extreme events: An activity theory approach. Management Information Systems Quarterly 37(1) 125–147.

Cheng, Hsing Kenneth, Yipeng Liu. 2012. Optimal software free trial strategy: The impact of network externalities and consumer uncertainty. Information Systems Research 23(2) 488–504.

Economides, Nicholas, Evangelos Katsamakas. 2006. Two-sided competition of proprietary vs. open source technology platforms and the implications for the software industry. Management Science 52(7) 1057–1071.

Gallaugher, John M., Yu-Ming Wang. 2002. Understanding network effects in software markets: Evidence from web server pricing. MIS Quarterly 26(4) 303–327.

Guo, Zhiling, Gary J. Koehler, Andrew B. Whinston. 2012. A computational analysis of bundle trading markets design for distributed resource allocation. Information Systems Research 23(3) 823–843.

Hagiu, Andrei. 2009. Two-sided platforms: Product variety and pricing structures. Journal of Economics & Management Strategy 18(4) 1011–1043.

Hevner, Alan R., Salvatore T. March, Jinsoo Park, Sudha Ram. 2004. Design science in information systems research. Management Information Systems Quarterly 28(1) 75–105.

Johnson, Eric J., Wendy W. Moe, Peter S. Fader, Steven Bellman, Gerald L. Lohse. 2004. On the depth and dynamics of online search behavior. Management Science 50(3) 299–308.

Jullien, Bruno. 2006. Two-sided markets and electronic intermediaries. Gerhard Illing, Martin Peitz, eds., Industrial Organization and the Digital Economy. The MIT Press, 273–302.

Lin, Mei, Xuqing Ke, Andrew B. Whinston. 2012. Vertical differentiation and a comparison of online advertising models. Journal of Management Information Systems 29(1) 195–236.

March, Salvatore T., Veda C. Storey. 2008. Design science in the information systems discipline: An introduction to the special issue on design science research. Management Information Systems Quarterly 32(4) 725–730.

Nault, Barrie R., Albert S. Dexter. 2006. Agent-intermediated electronic markets in international freight transportation. Decision Support Systems 41(4) 787–802.

Niculescu, Marius Florin, Dong Jun Wu. 2014. Economics of free under perpetual licensing: Implications for the software industry. Information Systems Research 25(1) 173–199.

Parker, Geoffrey G., Marshall W. Van Alstyne. 2005. Two-sided network effects: A theory of information product design. Management Science 51(10) 1494–1504.

Rochet, Jean-Charles, Jean Tirole. 2003. Platform competition in two-sided markets. Journal of the European Economic Association 1(4) 990–1029.

Stahl, Dale O., II. 1989. Oligopolistic pricing with sequential consumer search. The American Economic Review 79(4) 700–712.

## A Appendix

## A.1 Monotonicity in Buyers' and Sellers' Participation Decisions

Lemma 1. Let $c < c'$ and $k < k'$ . Under the brokerage model, if a buyer with cost $c'$ participates in the platform, the buyer with cost $c$ also participates in the platform. If a seller with cost $k'$ participates in the platform, the seller with cost $k$ also participates in the platform.

Proof. The buyer with $c'$ participates if her payoff, specified in Equation (3), is positive (i.e., if $nps - c' \geq 0$ ). Because $c < c'$ , we have $nps - c \geq 0$ , which indicates that the buyer with c also has an incentive to participate. Similar reasoning applies to the participation decision for sellers. □

Lemma 2. Let $c < c'$ and $k < k'$ . Under the advertising model, if a buyer with cost $c'$ participates in the platform, the buyer with cost $c$ also participates in the platform. If a seller with cost $k'$ participates in the platform, the seller with cost $k$ also participates in the platform. Moreover, if the seller with $k'$ participates in the advertising service, the seller with $k$ also participates in the advertising service.

Proof. The proof of buyers' and sellers' decisions of participating in the platform is the same as that of Lemma 1. We next show sellers' decisions about participating in the advertising service. The seller with $k'$ participates in the advertising service if her payoff with advertising is greater than her payoff without advertising; that is, if

$$
m \min \{p _ {2}, 1 \} (\pi - k ^ {\prime}) - \theta > m p _ {1} (\pi - k ^ {\prime})
$$

by Equation (6). Because $k < k'$ , if the above inequality is true, $[m \min\{p_{2}, 1\}(\pi - k) - \theta] > [mp_{1}(\pi - k)]$ must be true because $\min\{p_{2}, 1\} > p_{1}$ , which indicates that the seller with c also has incentive to participate in the advertising service. □

## A.2 Proof of Proposition 1

Proof. Notice that the objective function $p^{2}st(\pi-\tau)^{2}$ crosses zero at $\tau=0$ and $\tau=\pi$ , and it is positive over $[0,\pi]$ . Its first-order derivative $p^{2}s[(\pi-\tau)^{2}-2t(\pi-\tau)] = p^{2}s(\pi-\tau)(\pi-3\tau)$ is positive over $(0,\pi/3)$ and is negative over $(\pi/3,\pi)$ . Therefore, the objective function reaches the maximum at $\tau^{*}=\pi/3$ . Substituting $\tau^{*}$ into the objective function results in the maximum revenue.

## A.3 Proof of Proposition 2

Proof. Notice that the objective function $\delta s\left[\pi(\pi-k_{A}^{\prime})-\delta(\pi-k_{A}^{\prime})^{2}\right]k_{A}^{\prime}$ crosses zero three times at $k_{A}^{\prime}=\pi-\pi/\delta$ , $k_{A}^{\prime}=0$ , and $k_{A}^{\prime}=\pi$ . We can verify that the objective function is positive over $[0,\pi]$ .

By letting the first-order derivative of the objective function be zero, we have (after removing the constant term $\delta s$ )

$$
\left[ \pi (\pi - k _ {A} ^ {\prime}) - \delta (\pi - k _ {A} ^ {\prime}) ^ {2} \right] + \left[ - \pi + 2 \delta (\pi - k _ {A} ^ {\prime}) \right] k _ {A} ^ {\prime} = 0
$$

which can be reorganized as

$$
- 3 \delta k _ {A} ^ {\prime 2} - 2 (1 - 2 \delta) \pi k _ {A} ^ {\prime} + (1 - \delta) \pi^ {2} = 0
$$

Because $\frac{(1 - \delta)\pi^2}{-3\delta} < 0$ , one root of the above equation is negative and the other is positive. The positive one is

$$
k _ {A} ^ {\prime +} = \frac {2 (1 - 2 \delta) \pi - \sqrt {4 (1 - 2 \delta) ^ {2} \pi^ {2} + 1 2 \delta (1 - \delta) \pi^ {2}}}{- 6 \delta} = \frac {(2 \delta - 1) + \sqrt {1 - \delta + \delta^ {2}}}{3 \delta} \pi
$$

which can be verified to be less than $\pi$ because $\sqrt{1-\delta+\delta^{2}}<1+\delta$ . Therefore, its first-order derivative is positive over $(0,k_{A}^{\prime+})$ and is negative over $(k_{A}^{\prime+},\pi)$ , which indicates that the objective function is increasing over $(0,k_{A}^{\prime+})$ and decreasing over $(k_{A}^{\prime+},\pi)$ .

Notice that the constraint in Inequality (18) is equivalent to $k_{A}^{\prime} \leq \frac{ap\pi}{\delta}$ . Therefore, if $\frac{ap\pi}{\delta} \geq k_{A}^{\prime+}$ , the objective function reaches the maximum at $k_{A}^{\prime*} = k_{A}^{\prime+}$ ; otherwise, it reaches the maximum at $k_{A}^{\prime*} = \frac{ap\pi}{\delta}$ (when the constraint binds). The condition $\frac{ap\pi}{\delta} \geq k_{A}^{\prime+}$ can be rewritten as

$$
\frac {a p \pi}{\delta} > \frac {(2 \delta - 1) + \sqrt {1 - \delta + \delta^ {2}}}{3 \delta} \pi
$$

which is equivalent to $(\delta - 2 + 3p) > \sqrt{1 - \delta + \delta^2}$ . By substituting in $\delta = 1 - (1 - a)p$ , the above condition can be simplified to $p > \frac{1 + a}{1 + 2a} = \hat{p}(a)$ .

Therefore, if $p < \hat{p}(a)$ , substituting $k_A' = \frac{ap\pi}{\delta}$ into $\theta^*$ , we have

$$
\theta^ {*} = \delta \pi s (\pi - k _ {A} ^ {\prime}) - \delta^ {2} s (\pi - k _ {A} ^ {\prime}) ^ {2} = s \pi^ {2} \left[ (\delta - a p) - (\delta - a p) ^ {2} \right] = p (1 - p) s \pi^ {2}
$$

and thus $\Pi_A^* = \theta^* k_A'^* = \frac{a}{\delta} p^2 (1 - p)s\pi^3.$

If $p > \hat{p}(a)$ , substituting $k_A' = k_A' + \theta^*$ , we have

$$
\theta^ {*} = s \pi^ {2} \left[ (\delta - \frac {- (1 - 2 \delta) + \sqrt {1 - \delta + \delta^ {2}}}{3}) - (\delta - \frac {- (1 - 2 \delta) + \sqrt {1 - \delta + \delta^ {2}}}{3}) ^ {2} \right] = s \pi^ {2} \left[ \frac {1 + 2 \delta - 2 \delta^ {2} + (2 \delta - 1) \sqrt {1 - \delta + \delta^ {2}}}{9} \right]
$$

and thus

$$
\Pi_ {A} ^ {*} = \theta^ {*} k _ {A} ^ {\prime *} = s \pi^ {2} \left[ \frac {1 + 2 \delta - 2 \delta^ {2} + (2 \delta - 1) \sqrt {1 - \delta + \delta^ {2}}}{9} \right] \frac {(2 \delta - 1) + \sqrt {1 - \delta + \delta^ {2}}}{3 \delta} \pi
$$

which can be simplified to the one in the proposition.

## A.4 Proof of Corollary 2

Proof. From the proof of Proposition 2, if $p > \hat{p}(a)$ , the constraint in Inequality (18) does not bind, and therefore $p_2^* > 1$ ; otherwise, the constraint binds and $p_2^* = 1$ .

## A.5 Proof of Proposition 3

Proof. We denote $\Delta \equiv \Pi_B^* -\Pi_A^*$ . When $p < \hat{p} (a)$ (in which $\hat{p} (a)$ is as defined in Proposition 2),

$$
\Delta = \frac {4 p ^ {2} s \pi^ {3}}{2 7} - \frac {(1 - p) a}{\delta} p ^ {2} s \pi^ {3} = p ^ {2} s \pi^ {3} \left(\frac {4}{2 7} - \frac {(1 - p) a}{\delta}\right) = \frac {p ^ {2} s \pi^ {3}}{2 7 \delta} [ p (3 1 a - 4) - (2 7 a - 4) ]\tag{47}
$$

For any $a \in [0, \frac{4}{27}]$ , $\Delta > 0$ because when $a < \frac{4}{31}$ , 4 - 27a > 4 - 31a, and when $a > \frac{4}{31}$ , 31a - 4 > 0 and 27a - 4 < 0. For any $a \in [\frac{4}{27}, 1]$ , $\Delta = 0$ defines a curve $p(a) = \frac{27a - 4}{31a - 4}$ on the $(a, p)$ space, which intersects with $\hat{p}(a)$ at $a^{*} = \frac{8}{23}$ . When $a < a^{*}$ , we can verify $\frac{27a - 4}{31a - 4} < \hat{p}(a)$ , and therefore if $p > \frac{27a - 4}{31a - 4}$ , $\Delta > 0$ ; otherwise, $\Delta < 0$ . When $a > a^{*}$ , $\frac{27a - 4}{31a - 4} > \hat{p}(a)$ , and therefore, within $p < \hat{p}(a)$ , $\Delta < 0$ .

When $p > \hat{p} (a)$ ,

$$
\Delta = \frac {s \pi^ {3}}{2 7 \delta} \left[ 4 p ^ {2} \delta - \left(- 2 + 3 \delta + 3 \delta^ {2} - 2 \delta^ {3} + 2 (1 - \delta + \delta^ {2}) ^ {\frac {3}{2}}\right) \right]
$$

Notice that $\Delta = 0$ defines a curve $p^*(a)$ on the $(a,p)$ space, which intersects with $\hat{p}(a)$ at $a^* = \frac{8}{23}$ . When $a < a^*$ , we can verify $p^*(a) < \hat{p}(a)$ , and therefore, within $p > \hat{p}(a)$ , $\Delta > 0$ . When $a > a^*$ , $p^*(a) > \hat{p}(a)$ , and therefore if $p > p^*(a)$ , $\Delta > 0$ ; otherwise, $\Delta < 0$ .

To summarize, for $a \in [0, \frac{4}{27}]$ , we have $\Delta > 0$ . For $a \in [\frac{4}{27}, \frac{8}{23}]$ , if and only if $p > \frac{27a - 4}{31a - 4}$ , $\Delta > 0$ . For $a \in [\frac{8}{23}, 1]$ , if and only if $p > p^{*}(a)$ , $\Delta > 0$ . Then $\bar{p}(a)$ in the proposition follows.

## A.6 Proof of Proposition 4

Proof. (a) The payoffs of these sellers under the advertising model, by Equation (25), are positive because the marginal seller with $k_{A}^{*}$ derives zero payoff, and these sellers have lower costs than the marginal sellers. These sellers do not participate under the brokerage model and derive zero payoff. Therefore, they are all better off under the advertising model.

(b) For sellers in $[k_{A}^{\prime*}, k_{B}^{*}]$ , when $p > \hat{p}(a)$ (in which $\hat{p}(a)$ is defined as in Proposition 2), sellers are better off under the advertising model if

$$
\frac {2 - \delta + \sqrt {1 - \delta + \delta^ {2}}}{3} \pi s (1 - a) p (\pi - k) > \frac {2}{3} p ^ {2} s \pi (\frac {2}{3} \pi - k)\tag{48}
$$

where the term in the left-hand side is the sellers' payoffs under the advertising model by substituting $m_{A}^{*}$ from Equation (22) into Equation (25), and the term in the right-hand side is the sellers' payoff under the brokerage model from Equation (24). We can verify that Inequality (48) is true for all $p > \hat{p}(a)$ and that these sellers are better off under the advertising model.

Similarly, when $p < \hat{p}(a)$ , sellers are better off under the advertising model if

$$
p s \pi (1 - a) p (\pi - k) > \frac {2}{3} p ^ {2} s \pi (\frac {2}{3} \pi - k)
$$

The condition can be simplified to $k(a - \frac{1}{3}) > (a - \frac{5}{9})\pi$ . For $a \in [0, \frac{1}{3}]$ , the condition is satisfied because $k \leq \frac{2\pi}{3} = k_{B}^{*}$ . For $a \in [\frac{1}{3}, \frac{5}{9}]$ , the condition is satisfied because the right-hand side is non-positive. When $a > \frac{5}{9}$ , the inequality condition reduces to

$$
k > \frac {9 a - 5}{9 a - 3} \pi\tag{49}
$$

We next examine the condition for $\frac{9a-5}{9a-3}\pi > k_{A}^{\prime*} = \frac{ap\pi}{\delta}$ . Substituting $\delta$ in, by simple algebra, the condition is equivalent to $p < \frac{9a-5}{11a-5}$ . Therefore, if $p > \frac{9a-5}{11a-5}$ , $\frac{9a-5}{9a-3}\pi < k_{A}^{\prime*}$ and all $k \in [k_{A}^{\prime*}, k_{B}^{*}]$ satisfy Equation (49) and sellers are better off; otherwise, sellers with $k > \frac{9a-5}{9a-3}\pi$ are better off under the advertising model and other sellers are worse off.

For sellers in $[0, k_A'^*]$ , when $p > \hat{p}(a)$ , sellers are better off under the advertising model if

$$
\frac {2 - \delta + \sqrt {1 - \delta + \delta^ {2}}}{3} \pi s (\pi - k) - s \pi^ {2} \left[ \frac {1 + 2 \delta - 2 \delta^ {2} + (2 \delta - 1) \sqrt {1 - \delta + \delta^ {2}}}{9} \right] > \frac {2}{3} p ^ {2} s \pi (\frac {2}{3} \pi - k)\tag{50}
$$

where the term in the left-hand side is sellers' payoffs under the advertising model by substituting $m_{A}^{*}$ from Equation (22) and $\theta^{*}$ from Equation (19) into Equation (26), and the term in the right-hand side is sellers' payoff under the brokerage model from Equation (24). We can verify that Inequality (50) is true for all $p > \hat{p}(a)$ and these sellers are better off under the advertising model.

Similarly, when $p < \hat{p}(a)$ , sellers are better off under the advertising model if

$$
p s \pi (\pi - k) - p (1 - p) s \pi^ {2} > \frac {2}{3} p ^ {2} s \pi (\frac {2}{3} \pi - k)
$$

By simple algebra, the condition can be reduced to $(1 - \frac{2}{3}p)k < \frac{5}{9}p\pi$ . Therefore, any $k < \frac{5p\pi}{3(3-2p)}$ satisfies the condition. We next check the condition for $\frac{5\pi p}{3(3-2p)} < k_{A}^{\prime*} = \frac{ap\pi}{\delta}$ . Substituting $\delta$ in, by simple algebra, the condition is equivalent to $p < \frac{9a-5}{11a-5}$ . Therefore, if $p > \frac{9a-5}{11a-5}$ , $\frac{5\pi p}{3(3-2p)} > k_{A}^{\prime*}$ and all $k \in [0, k_{A}^{\prime*}]$ satisfy $k < \frac{5\pi p}{3(3-2p)}$ and sellers are better off; otherwise, sellers with $k < \frac{5p\pi}{3(3-2p)}$ are better off under the advertising model and other sellers are worse off.

All together, we can summarize the results using function $\tilde{p}(a)$ specified in the proposition.

## A.7 Proof of Proposition 5

Proof. When $p < \hat{p}(a)$ , the result follows because $p\pi s - c > \frac{2}{3}p\pi s - c$ by Equations (28) and (29). When $p > \hat{p}(a)$ , the result can be established if

$$
\frac {2 - \delta + \sqrt {1 - \delta + \delta^ {2}}}{3} \pi s - c > \frac {2}{3} p \pi s - c
$$

or, equivalently, if $2 - \delta + \sqrt{1 - \delta + \delta^{2}} > 2p$ . Furthermore, the condition is equivalent to $1 - \delta + \delta^{2} > (2p - 2 + \delta)^{2}$ , which reduces to $3 + a - 4ap > 0$ by substituting into $\delta$ . Because a and p are in [0, 1], the inequality $3 + a - 4ap > 0$ is true.

## A.8 Proof of Proposition 6

Proof. When $p \leq \hat{p}(a)$ , the average matching probability under the advertising model is the same as under the brokerage model; that is, $[(n_{A}^{*} - n_{A}^{\prime *})p_{1} + n_{A}^{\prime *}] = pn_{A}^{*}$ (which can also be seen from Equation (29)). Notice that $m_{B}^{*} < m_{A}^{*}$ and $n_{B}^{*} < n_{A}^{*}$ . We check the social welfare under the brokerage model generated by the low-cost buyers with a mass $m_{B}^{*}$ (among $m_{A}^{*}$ ) and the low-cost sellers with a mass $n_{B}^{*}$ (among $n_{A}^{*}$ ). These segments of buyers and sellers under the advertising model generate the same total value $m_{B}^{*}n_{B}^{*}p(s+\pi)$ as under the brokerage model. The total fixed cost on the seller side is lower than the fixed cost under the brokerage model because, among $m_{B}^{*}$ , the lower cost sellers participate in the advertising and sell their products more often. The total opportunity costs on the buyer side are the same under the two models. Therefore, these segments of buyers and sellers under the advertising model generate more social welfare than that under the brokerage model. Other participating buyers and sellers generate additional social welfare because their decisions to participate means that the expected benefits are greater than their costs.

When $p > \hat{p}(a)$ , we can also verify that the advertising model generates more social welfare than the brokerage model. □
