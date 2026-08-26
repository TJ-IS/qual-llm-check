---
otero_id: 26802
otero_key: "AGS42M8A"
title: "An Economic Analysis of the Introduction of an Electronic Data Interchange System"
authors: "Anitesh Barua; Byungtae Lee"
year: "1997"
journal: "Information Systems Research"
doi: "10.1287/isre.8.4.398"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR Agriomatic Systems Research

![](/api/attachments/AGS42M8A/fulltext/images/59e9d4a24bd3408a31073ea5ca9834d66c88456f20bafd664a3f20614e49da1a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# An Economic Analysis of the Introduction of an Electronic Data Interchange System

Anitesh Barua, Byungtae Lee,

## To cite this article:

Anitesh Barua, Byungtae Lee, (1997) An Economic Analysis of the Introduction of an Electronic Data Interchange System. Information Systems Research 8(4):398-422. http://dx.doi.org/10.1287/isre.8.4.398

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1997 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/AGS42M8A/fulltext/images/1ae3a451594b071cc3fd679926cacf7de243c1213b15ac0ffd9407c772ca45cb.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Economic Analysis of the Introduction of an Electronic Data Interchange System

Anitesh Barua • Byungtae Lee

Department of Management Science and Information Systems, Graduate School of Business,

The University of Texas at Austin, Austin, Texas 78712

barua@mail.utexas.edu

Department of Management Information Systems, Karl Eller Graduate School of Management,
The University of Arizona, Tucson, Arizona 85721
blee@arizona.edu

Although electronic data interchange (EDI) holds the promise of significantly increasing the efficiency of business transactions, an installed base of proprietary implementations has been detrimental to the widespread acceptance of the technology. Thus, an important research issue involves strategies for facilitating EDI adoption. We analyze the introduction of an EDI system in a vertical market involving one manufacturer and two suppliers. The manufacturer initiates an EDI network, and penalizes a supplier for not joining the system by reducing its volume of business with the supplier. Along with a “stick,” the manufacturer can also use a “carrot” in the form of a subsidy to partially offset a supplier’s setup cost.

The competition between the suppliers is characterized by incentive types for joining the EDI system (“motivating” or “threatening”) and the Information Technology (IT) efficiency (“efficient” or “inefficient”). We show that regardless of its cost structure, a supplier may have to join the EDI network out of “strategic necessity,” due to the presence of an IT-efficient supplier. Our analysis further shows that depending on the supplier competition structure, the EDI system may prove to be a “beneficial” strategic necessity for a large supplier and an “unfortunate” strategic necessity for a small supplier. Another key result is that by increasing the severity of the penalty, both the manufacturer and the follower supplier can be worse off under certain conditions. The analysis of subsidy strategies reveals that unless leadership and followership positions are reversed due to a subsidy, subsidizing a supplier has no impact on the joining time of its competitor. Thus the EDI initiator cannot induce both suppliers to join earlier by subsidizing one supplier. Also, the larger the slack capacity of the leader, the higher (lower) the manufacturer’s incentive to subsidize the leader (follower). These results offer insights for initiators and adopters regarding penalty and subsidy strategies, impact on competition structure, joining decisions and network growth.

(EDI; Beneficial and Unfortunate Strategic Necessity; Incentives; Efficiency; Subsidy; Penalty Mechanisms)

## 1. Introduction

EDI holds the promise of increasing the efficiency of business transactions and improving coordination between trading partners. While the EDI marketplace continues to grow, estimates (e.g., Major 1993) suggest that a relatively small fraction of all business transactions are conducted through EDI. The EDI market is characterized by the presence of multiple (often

INFORMATION SYSTEMS RESEARCH
398 Vol. 8, No. 4, December 1997

proprietary) standards (e.g., Taylor 1993, Bonney 1994), new software requirements and substantial reorganization of business processes (Major 1993). Industry surveys also show that large organizations are the strongest proponents of EDI, and that they often exert pressure on their suppliers to use EDI (e.g., Taylor 1993, Major 1993, and Newburger 1993). Therefore, one of the key research issues involves strategies that the initiators of EDI networks can use to facilitate the expansion of the technology base. For example, what penalty systems (if any) should initiators use to induce early adoption? Should such a penalty system be used in conjunction with a subsidy? Another important and related issue involves the impact of EDI adoption on the trading partners' bargaining power and competition structure. For example, which (if any) suppliers are likely to improve their competitive position through an early adoption of the technology?

In this paper, we address several questions relating to the introduction of an EDI system by analyzing a market with one large manufacturer and two suppliers. As often observed in practice (e.g., Hwang et al. 1993), the manufacturer initiates an EDI network and demands that its suppliers conduct transactions through the network. The suppliers decide when to join the network based on the nature of the competition, their efficiency with respect to the proposed technology and the penalty for not joining the system. The manufacturer penalizes a supplier for not joining EDI immediately by reducing its business volume with the supplier, provided its competitor joins the network, in which case it gains the business lost by the unwilling supplier. When the unwilling supplier joins the system, its business volume is determined according to the restoration policy of the manufacturer. Along with the penalty, the manufacturer can also subsidize the suppliers for joining the system earlier.

We analyze the EDI adoption decisions both from the manufacturer's (initiator) and suppliers' (adopters) standpoints. The manufacturer's interest lies in facilitating the adoption of the technology, while the suppliers want to make adoption timing decisions which maximize their net payoff. Two key concepts in the model involve the suppliers' IT efficiency (defined as "efficient" or "inefficient") and incentives ("motivating" or "threatening") to join the EDI. An important feature of the model is that the suppliers' incentives and efficiency types are endogenously determined (rather than being exogenously specified) by the manufacturer's policy regarding the network adoption, and also by the competing supplier's parameters.

Several interesting results are obtained from the analysis. We show that regardless of its cost structure, a supplier may have to join the EDI network out of "strategic necessity" due to the presence of an IT-efficient supplier. Further, the EDI system may be a "beneficial" strategic necessity for a relatively large supplier, while it may be an "unfortunate" strategic necessity for a small supplier. $^{1}$ A large supplier is more likely than a small supplier to have a motivating incentive to join the EDI system, and a motivating incentive leads to the beneficial nature of the strategic necessity. With a threatening incentive created by a large competitor, a small supplier is in an unfortunate situation, and in this case EDI brings an unfortunate necessity. Thus, the differential impacts of EDI on the suppliers' market position depend on their incentives and IT efficiency.

We also show that if the follower has a motivating incentive with a given restoration policy of the manufacturer, a more severe policy makes both the manufacturer and the follower worse off. For a supplier with a threatening incentive, a more severe policy may or may not increase the manufacturer's benefits. Thus, there is no monotonic relationship between the severity of the manufacturer's policy and its payoff; the manufacturer must analyze the incentive of a supplier in setting its restoration policy. In analyzing the manufacturer's "carrot," we find that unless a subsidy level changes the leadership and followership positions of the suppliers, a subsidy to a supplier does not change the competing supplier's joining time. Thus, a manufacturer cannot induce both suppliers to join the network sooner by subsidizing only one supplier. Another finding implies that the higher the capacity of the leader, the higher (lower) the incentive of the manufacturer to subsidize the leader (follower). This is unfortunate for the follower firm.

Several results relating to the impact of slack capacity of the suppliers are derived. For example, it is shown that the leader's joining time depends on its own slack capacity, while the follower's joining time depends on its competitor's slack capacity. The larger the slack capacity of the leader, the earlier the joining times for both suppliers.

This paper provides a theoretical basis for analyzing the economic impacts of EDI introduction from the standpoints of both initiators and adopters. By considering the network initiator's "stick" and "carrot," and by endogenizing the adopters' incentives and technology efficiency, it offers insights into some key issues such as EDI related surplus sharing and resulting changes in the competition structure, and strategies for facilitating EDI acceptance.

The balance of the paper is organized as follows. The relevant prior literature and the motivation for the study are discussed in § 2. Section 3 describes the scenario analyzed in the paper. The model assumptions and their justification are also provided in this section. Section 4 constitutes the core of the paper. The notions of IT efficiency and incentives of the suppliers, the EDI joining decisions, sensitivity analysis, and related propositions are presented in this section. Future research issues are outlined in § 5. Section 6 contains concluding remarks.

## 2. Prior Research and Motivation

## 2.1. Literature on Interorganizational Systems

Interorganizational systems (IOS) have drawn considerable attention from IS researchers because of their strategic significance (e.g., Bakos and Treacy 1986, Clemons and McFarlan 1986, Clemons and Kimbrough 1986, Johnston and Vitale 1988, Cash and Konsynski 1985, Ives and Learmonth 1984). These studies focus on the possibility of gaining competitive advantage (e.g., Bakos and Treacy 1986, Johnston and Vitale 1988), or on the impacts of IOS on market structure (e.g., Cash and Konsynski 1985). In a seminal paper, Clemons and Kimbrough (1987) developed a model for assessing the strategic impacts of IT investments. They suggested that most IT investments are likely to become “strategic necessities” over time. They further distinguished between “beneficial” and “unfortunate” necessities, which are used as key concepts in this paper. The concept of strategic necessity was developed further by Clemons and Row (1988).

Some researchers have addressed specific IOS problems through the development of formal economic models (e.g., Bakos 1987, Clemons and Kleindorfer 1992, Nault 1993, Nault and Dexter 1994, Seidmann and Wang 1995, Whang 1993, Bakos and Brynjolfsson 1993, Clemons et al. 1993). Bakos (1987) provides the motivation for using the economic approach: "Economic theory offers a rich research tradition in areas central to the study of industry-level impacts of IOS." The economic approach focuses on efficiency implications of interorganizational information links, market implications of reduced search costs and better information, and certain aspects of the introduction of new technologies. Bakos (1987) studies IOS in terms of economic efficiency and strategic manipulation. He proposes a general framework using noncooperative game theoretic models to explain the behavior of IOS participants. One of his key findings suggests that the exchange of information in vertical markets and the level of inventory are economic substitutes. Clemons and Kleindorfer (1992) develop a bargaining model of IOS investment and show that opportunism leads to under-investment in IOS. Nault (1993) investigates the role of IOS in product quality enhancement, and suggests that pricing an IOS could take the form of a subsidy. He further shows that firms can differentiate themselves by supporting only IOS or non-IOS based products. Nault and Dexter (1994) study the interplay between adoption, marketing effort and payment systems in a franchise network with positive externalities. They show that interfranchise transfer payments in the presence of positive externalities in advertising effort increases investments by franchises. An IOS to keep track of transactions occurring throughout the franchise network would be critical in the implementation of the proposed transfer payment system.

Meier and Chismar (1991) examine the impact of EDI introduction by a manufacturer on the manufacturer-supplier relationship. They distinguish between process and efficiency benefits, and formulate EDI decision rules for both the manufacturer and suppliers in terms of their costs and benefits. In a related paper, Chismar and Meier (1992) develop a model of competition between the providers of IOS, and discuss its application to airline reservation systems.

Riggins et al. (1989) study the EDI network expansion process with participants who differ in terms of their “willingness-to-pay” function and setup cost. They consider both positive and negative externalities, and show that a “stalling” problem will be encountered. In another paper, Riggins et al. (1990) extend their earlier model by incorporating certain dynamic aspects of the setup cost function.

Seidmann and Wang (1995) investigate the role of externalities (both positive and negative) in EDI implementation/adoption. They show that EDI adoption by a supplier can generate positive externalities for the buyer and negative externalities for competing suppliers. Seidmann and Wang also derive conditions under which it is optimal for the buyer to subsidize a supplier's adoption of EDI, and discuss EDI generated surplus sharing issues. While Meier and Chismar (1991), Riggins et al. (1989, 1990), and Seidmann and Wang (1995) study issues in joining EDI, Whang (1993) investigates the incentives of a firm to share information with its EDI partners.

The above studies provide the motivation for this paper. One of the main objectives of this research is to examine the competitive structure among suppliers. We believe that EDI systems (or IOS in general) affect the very nature of competition between the suppliers. Therefore, we analyze the problem from a game theoretic standpoint, which enables us to examine the competitive responses of the suppliers. Thus, the network joining times are endogenously determined, rather than being exogenously specified. In fact, our analysis shows that in many situations, both the high and low cost suppliers join the network at the same time.

## 2.2. Relevant Studies from the Economics Literature

Many studies in economics have modeled technology adoption and innovation among competing firms (e.g., Reinganum 1981a, 1981b, 1982; Katz and Shapiro 1985,

1986). Barua et al. (1991) and Nault (1993) provide reviews of other studies in the economics/game theory literature dealing with strategic aspects of technology investments. The game theoretic approach for this study is provided by Reinganum (1981a), who analyzes the adoption of a new technology by two competing firms. The competitors decide when to adopt a new cost-saving technology, where there is a first mover advantage, and where the cost of the technology declines over time. Reinganum (1981a) characterizes the Nash equilibrium, and shows that there is a diffusion effect even when the firms are identical. In another line of research involving R&D rivalry, Reinganum (1981b, 1982) analyzes a scenario where two rival firms invest in R&D activity to develop a new product, and where the firm which innovates first will have distinct advantages due to the award of a patent. The first mover advantage is the common thread which runs through the three studies by Reinganum.

We use Reinganum's (1981a) technology adoption model in the context of EDI introduction, along with the additional features of the manufacturer's substitution/restoration policy, subsidy decisions, and the suppliers' slack capacity and IT efficiency. We use Reinganum's (1981a) characterization of the outcome(s) of the game, with the key difference that Reinganum does not consider the case where the opportunity cost of adopting the technology second is higher than the benefit of adopting first. This is particularly important for a relatively small supplier in the EDI setting, where the manufacturer can impose a severe penalty for joining the system late (i.e., the opportunity cost may be very high), while joining first may not bring an equally high benefit due to the small scale of operation. $^{2}$ We show that this situation, combined with a low IT efficiency, can lead to the absence of an equilibrium, and that the manufacturer should consider other strategies such as providing a subsidy under such circumstances. More importantly, we incorporate in Reinganum's general technology adoption model an external agent (the manufacturer) who, depending on the suppliers' slack capacity and IT efficiency, can manipulate the outcome of the game through a "stick" and/or "carrot." The impact of the manufacturer's penalty system and subsidy policy on the efficiency and incentives of the suppliers (and hence their joining times) constitutes the main theme of our paper. Further, we divide the supplier benefits from joining EDI into two parts: one dealing with the first mover advantage or disadvantage for the follower, and the other representing the efficiency benefits which accrue to anyone joining the system at any time. This feature allows us to understand the “strategic necessity” aspect of EDI as well as investigate conditions under which the network may prove to be “beneficial” or “unfortunate” for a supplier.

Katz and Shapiro (1985) study the dominance of two competing products in the presence of positive externalities, and show the importance of consumers' expectations regarding the market position of the sellers. In another paper involving positive externalities, Katz and Shapiro (1986) analyze the adoption of two rival technologies. They show that adoption depends on whether or not the technology is "sponsored," and that a sponsored but inferior technology may be adopted over a superior technology which has not been sponsored. Our model focuses on the adoption of a single technology (EDI) with negative externalities among suppliers, who are competing for a fixed amount of business from a manufacturer, and is therefore closer to the work of Reinganum (1981a).

## 3. The Model

We analyze a vertical market involving one large manufacturer and two suppliers. While the case of more than two suppliers is certainly more general, using a duopoly for suppliers enables us to model explicitly the impact of one supplier's network joining decision on the other's joining time and profitability. The duopoly model also makes it analytically tractable to analyze the endogenous nature of supplier incentives and IT efficiency, which are two important concepts for this paper. From the manufacturer's perspective, it is a case of "backward integration." The manufacturer intends to replace existing communication linkages with an EDI system. The optimal joining times of the suppliers may depend on many factors, including their IT efficiency, the penalty for not joining the system, and the potential benefits of EDI adoption.

## 3.1. Model Assumptions and Variable Definitions

3.1.1. Business Volume. Let $v_{i}^{t}$ be the business volume between supplier i and the manufacturer at time t. We assume that total volume, $v^{0}$ , is not affected by the introduction of EDI, and that it remains constant over time. This assumption of constant volume over time allows us to focus on the impacts of the competition structure of the suppliers on their joining times. In § 4.2, however, we study the effect of business volume on the suppliers' joining decisions through comparative statics.

3.1.2. Business Profit Flow. Let $\pi_{i}^{t}(\nu_{i}^{t})$ denote firm i's profit flow at time t, prior to EDI implementation. EDI improves the efficiency of transactions through the elimination of manual processes and paper work, and through increased coordination between trading partners. As in Meier and Chismar (1991), we assume that these efficiency benefits are proportional to the transaction volume. The suppliers incur some variable costs (e.g., document preparation and transmission) for using the EDI system. Thus, the net efficiency benefit from the EDI is the difference between the efficiency benefits and the variable (marginal) costs. Let $\epsilon_{i}(\nu_{i}^{t})$ denote the net efficiency benefit flow to supplier i resulting from transaction volume $\nu_{i}^{t}$ .

3.1.3. Setup Cost. An important cost component of EDI is a large setup cost. As noted by Bakos (1987), "An IOS-based intermediation system will experience a large fixed cost component, while it will enjoy very low marginal costs for handling an additional transaction." Setup cost includes new hardware and software acquisition/development, and changes in internal business processes in order to interface with EDI. The latter usually involves a significant investment. Major (1993) suggests: "To effectively use EDI you almost have to re-engineer your existing systems. This is because existing data routines have to be modified to give EDI what it does and does not want." If supplier i joins the system at time T, let the EDI setup cost be given by $C_{i}(T) = C_{i}^{0} e^{-\lambda_{i} T}$ , where $\lambda_{i} (\lambda_{i} > \gamma$ , the interest rate) determines the rate at which the cost declines, and where $C_{i}^{0}$ is cost incurred if the supplier joins the network as soon as it is announced. $^{3}$ In the advanced technology market, technological advances generally support the idea that cost decreases substantially over time (e.g., Katz and Shapiro 1987). There is another important reason why we model the setup cost as a decreasing function of time. A supplier joining a proprietary system of a particular manufacturer rather than a system based on a forthcoming industry standard incurs a high opportunity cost. For example, global standards like X.12 and EDIFACT (EDI document format standards) and Message Transfer Agent (MTA) X.400 (transfer standard for electronic mail) will achieve widespread implementation over time, reducing the opportunity cost. However, industry surveys indicate that “majority of EDI traffic today is based on industry specific application protocols” (Taylor 1993). The decreasing cost of technology and the evolution of global communication standards and protocols are the technological factors driving the firms to accept the system.

3.1.4. Bargaining Power. We assume a relatively strong bargaining power of the manufacturer. This implies that the suppliers only decide when they will join the system. Future research will focus on the development of a cooperative bargaining model of supplier-manufacturer relationship.

## 3.2. A Model of EDI Adoption

When the manufacturer announces the EDI system, it may not be attractive to supplier j because its current setup cost may be higher than the net benefits. As global EDI document standards and “middleware” for format translation become increasingly popular, the cost of doing business through EDI will decline significantly over time. In that case, j may wish to wait until it is economically feasible to join the EDI network. Suppose the manufacturer has a policy of substituting j with i, if i is willing to join the system earlier. Let $\alpha_{j}^{\prime}$ be the fraction of $j$ 's business that the manufacturer transfers to $i$ , when the latter joins first. This fraction depends on the severity of the manufacturer's policy and on the slack capacity of $i$ . Corresponding to $j$ 's loss of business volume $\nu_j^0\alpha_i'$ , there will be gain of $\alpha_i\nu_i^0$ for $i$ , where $\alpha_i\nu_i^0 = \nu_j^0\alpha_j'$ . We call $\alpha_i$ the substitution gain factor for $i$ . The manufacturer has three strategies with respect to the restoration of $j$ 's business volume after it joins as a follower: First, the manufacturer can restore $j$ 's business volume as soon as $j$ joins the system. Second, the restoration may be gradual. Third, the manufacturer may decide not to restore the business volume as a penalty for joining late. If firms $i$ and $j$ join the system at $T_i$ and $T_j$ respectively ( $T_i \leq T_j$ ), then, depending on the manufacturer's restoration policy, $i$ 's transaction volume will change at times $T_i$ and $T_j$ (as shown in Appendix A.1).

We first investigate the case where the restoration of business volume is instantaneous. Later, we discuss the implications of more severe restoration policies and derive an interesting result involving the impact of the severity of the policy. In order to determine the payoffs to i and j, we use the following profit flow functions. Let

$\pi_t^0 = i$ 's profit flow before anyone has joined the system,

$\pi_i^1 = i$ 's profit flow when only $i$ joins the system, $\pi_i^2 = i$ 's profit flow when only $j$ joins the system, $\pi_t^3 =$ steady state profit flow of firm $i$ , after both the suppliers join the system.

These profit flows are defined in terms of the model parameters in Appendix A.2. Note that the manufacturer's restoration strategy for the business volume of the follower only affects the steady state profit flow, $\pi_{i}^{3}$ , because only the steady state volume (i.e., after both suppliers have joined the system) is dependent on these policies. The payoff function for firm i depends on the joining times of both the suppliers, and is given by

$\Pi_{i}(T_{i}, T_{j}) = \begin{pmatrix} L_{i}(T_{i}, T_{j}) & \text{if } T_{i} \leq T_{j} \text{ i.e., if } i \text{ is the leader,} \\ F_{i}(T_{i}, T_{j}) & \text{if } T_{i} \geq T_{j} \text{ i.e., if } j \text{ is the leader,} \end{pmatrix}$

where $L_{i}(T_{i}, T_{j})$ and $F_{i}(T_{i}, T_{j})$ are i's payoffs as a leader and a follower respectively. The expressions for the leadership and followership payoff functions are provided in Appendix A.3.

## 4. Analysis and Results

## 4.1. Competition Structure and Optimal Joining Times

To find the optimal joining times of the suppliers, we use a noncooperative Nash equilibrium. A pair of joining times constitutes a Nash equilibrium, if given the joining time of any supplier, the competing supplier cannot increase its net payoff by choosing a joining time other than the equilibrium value. The Nash equilibrium (or equilibria) is (are) determined from the intersection(s) of the best response functions of the suppliers. In the current context, supplier i's best response function determines the joining time $T_{i}$ , which provides i the maximum net payoff for any given joining time $T_{j}$ , which the competing supplier j might have chosen.

As mentioned earlier, EDI adoption is a costly process, primarily because of changes in business processes and company specific standards. Therefore, one of the key factors that a supplier must consider in its joining decision is its efficiency in the proposed technology. We define an efficiency measure as a ratio of profit change and cost savings at t = 0. A firm is efficient (inefficient) in the EDI system if its profit change due to the system is greater than or equal to (less than) the marginal EDI cost. Since a supplier can be either a leader or a follower, and since the benefit depends on the leadership or followership position of a supplier, we define “leadership” and “followership” efficiency ratios as follows:

DEFINITION 1 (IT Efficiency).

(a) Leadership IT efficiency ratio: $r_i^l = \frac{\pi_i^1 - \pi_i^0}{-C_i'(0)}$ ,

(b) Followership IT efficiency ratio: $r_i^f = \frac{\pi_i^3 - \pi_i^2}{-C_i'(0)}$ ,

where the denominator is the first derivative of the setup cost at time 0, adjusted with a negative sign. The numerators in the leadership and followership efficiency ratios represent the flow of benefit and the opportunity cost of being a leader and a follower respectively. The denominator is the decrease in the setup cost at time 0. Since the cost derivative is negative, the negative sign ensures that the efficiency is positive.

Another important aspect of a supplier's joining decision involves the endogenous incentives resulting from the presence of a competing supplier, and the manufacturer's penalty and restoration policy. Each supplier firm must consider the benefit and the opportunity cost of being a leader and a follower respectively. The benefit flow resulting from joining first is given by $\pi_i^1 - \pi_i^0$ , while the opportunity cost flow of being a follower is $\pi_i^3 - \pi_i^2$ . If the benefit outweighs the opportunity cost, then the supplier is "motivated" to join the system. On the other hand, a supplier is "threatened" when the opportunity cost is higher. Thus, we define "motivating" and "threatening" incentives as follows:

DEFINITION 2 (Incentives for joining EDI).

(a) Motivating incentive: $\pi_i^2 -\pi_i^3 +\pi_i^1 -\pi_i^0 >0,$

(b) Threatening incentive: $\pi_i^2 -\pi_i^3 +\pi_i^1 -\pi_i^0 < 0$

Note that a motivating incentive does not imply that a supplier will immediately join the EDI system. It must consider its IT efficiency to determine the exact joining time. Next, we use the concepts of efficiency and incentive types to characterize the suppliers' best response functions and the Nash solution. Let $T_{i}^{l}$ and $T_{i}^{f}$ represent the optimal leadership and followership joining times respectively of supplier $i$ . That is, if $i$ chooses to be a leader, then joining at $T_{i}^{l}$ maximizes its net payoff. Similarly if it decides to be the follower, then it should join at $T_{i}^{f}$ . Also, let $\tilde{T}_{j}$ be the joining time of $j$ , which makes $i$ indifferent between being a leader or a follower. We refer to this joining time of $j$ as supplier $i$ 's indifference point. As seen in Lemma 1 below, the optimal response of $i$ to $j$ 's choice of a joining time is critically dependent on this indifference point. In order to derive the best response functions, we need to characterize the notion of an EDI-efficient supplier.

DEFINITION 3 (EDI-efficient supplier).

Supplier $i$ is efficient if $\min (r_i^l,r_i^f)\geq 1$

This definition implies that to be considered as efficient with respect to the proposed EDI system, both the marginal benefit of being the leader and the marginal opportunity cost of being a follower must outweigh the marginal EDI setup cost. $^{4}$ Thus, with a motivating incentive, a supplier will be considered efficient if its followership efficiency ratio is greater than or equal to 1. This is due to the fact that for a motivating incentive (where the marginal benefit of being the leader is higher than the opportunity cost of being the follower), the leadership efficiency ratio is always greater than the followership efficiency. Therefore, a followership efficiency greater than or equal to 1 will guarantee that the leadership ratio is also greater than 1. Similarly, for a supplier with a threatening incentive, a leadership efficiency ratio greater than or equal to 1 ensures that the supplier is efficient (since then the followership ratio will also be greater than 1). In Lemma 1 below, we show how a supplier should respond to its competitor's choice of a joining time.

LEMMA 1. (Characterization of the Best Response Function). (a) If supplier i has a motivating incentive, and is inefficient (i.e., has a followership efficiency less than 1), its best response, $\Phi_{i}(T_{j})$ , to supplier j's choice, $T_{j}$ , is given as follows:

$$
\Phi_ {i} (T _ {j}) = \left( \begin{array}{l l} T _ {i} ^ {f} & \text { for } T _ {j} <   \tilde {T} _ {j}, \\ T _ {i} ^ {l} \text { or } T _ {i} ^ {f} & \text { for } T _ {j} = \tilde {T} _ {j} \text { where } 0 \leq T _ {i} ^ {l} <   T _ {i} ^ {f}, \\ T _ {i} ^ {l} & \text { for } T _ {j} > \tilde {T} _ {j}, \end{array} \right.
$$

otherwise (i.e., if $i$ is efficient), $\Phi_i(T_j) = 0$ .

(b) If i is has a threatening incentive, and is inefficient (i.e., has a leadership efficiency less than 1), its best response is given as follows:

$$
\Phi_ {i} (T _ {j}) = \left( \begin{array}{l l} T _ {i} ^ {l} & \text { for } T _ {j} <   \tilde {T} _ {j}, \\ T _ {i} ^ {l} \text { or } T _ {i} ^ {f} & \text { for } T _ {j} = \tilde {T} _ {j} \text { where } 0 \leq T _ {i} ^ {f} <   T _ {i} ^ {l}, \\ T _ {i} ^ {f} & \text { for } T _ {j} > \tilde {T} _ {j}, \end{array} \right.
$$

otherwise (i.e., if $i$ is efficient), $\Phi_i(T_j) = 0$ .

If the two firms are identical, then Lemma 1a follows Reinganum's (1981a) characterization of the best response function. However, as we mentioned earlier, Reinganum does not consider the case of opportunity costs being higher than first mover benefit, which is addressed in Lemma 1b. The expressions for the leadership and followership joining times ( $T_i^l$ and $T_i^f$ ) are provided in Lemma 3 in Appendix B. Lemma 1 brings out the importance of the indifference point defined above. With a motivating incentive, supplier $i$ 's best response switches from a followership to a leadership position as $j$ 's joining time exceeds $i$ 's indifference point. The reverse switch takes place when $i$ has a threatening incentive. Also note that as $i$ 's incentive changes from motivating to threatening, the relationship between $T_i^l$ and $T_i^f$ gets reversed (i.e., $T_i^l$ occurs later than $T_i^f$ for the case of threatening incentive). Of course, this does not imply that the leader joins later than the follower. Even if $i$ 's leadership joining time $T_i^l$ occurs later than its followership joining time $T_i^f$ , the follower $j$ still joins after the leader $i$ (i.e., $T_j^f > T_i^l$ ).

The best response functions under various combinations of incentive and efficiency types are plotted in Figure 1. In Figure 1(a), supplier i's leadership joining time $T_{i}^{l}$ will be at 0 if its leadership efficiency ratio is greater than or equal to 1. However, this does not suggest that the supplier will join the system at time 0; the optimal joining time is determined by the Nash equilibrium, which is obtained from the intersection of the best response functions of the suppliers. Similarly, in Figure 1(b), i's followership joining time will be equal to zero if its followership efficiency is greater than or equal to 1 (refer to Lemma 4 in Appendix B for a proof of these assertions).

Note that the best response function depends critically on the incentive and efficiency types. For example, if supplier i is IT-efficient, then its best response to any choice by j is to join the EDI network immediately, regardless of its incentive type. This scenario is shown in graph (c). Graphs (a) and (b) represent the best response function of an IT-inefficient supplier firm for “motivating” and “threatening” incentives, respectively. Table 1 summarizes the best response of supplier i as a function of the competition structure. Now we are in a position to derive the Nash solution and analyze some of its interesting properties.

PROPOSITION 1. (a) If one supplier has a threatening incentive and a leadership efficiency less than 1, there is no Nash equilibrium, regardless of the other supplier's efficiency and incentive.

Figure 1 Supplier / 's Best Response Functions  
![](/api/attachments/AGS42M8A/fulltext/images/e48ba23b2139672446c846e2b4f93248151453107abf2f7fe85a3a54f751a06c.jpg)

![](/api/attachments/AGS42M8A/fulltext/images/a95b52eecf82c502b3d117a6e30a59deb70852341b35dc2728cf4ecf97601561.jpg)

Table 1 Competition Structure and the Best Response Function

<table><tr><td>Incentive</td><td>IT-efficiency</td><td>Best Response</td></tr><tr><td rowspan="2">Motivating</td><td>Efficient ( $r'_{i} \geq 1$ )</td><td>(c)</td></tr><tr><td>Inefficient ( $r'_{i} < 1$ )</td><td>(a)</td></tr><tr><td rowspan="2">Threatening</td><td>Efficient ( $r'_{i} \geq 1$ )</td><td>(c)</td></tr><tr><td>Inefficient ( $r'_{i} < 1$ )</td><td>(b)†</td></tr></table>

(b) When no supplier has a combination of threatening incentive and inefficiency (as in 1(a)), other combinations of supplier incentive and efficiency lead to a total of five Nash equilibria.

The proofs of Proposition 1 and all subsequent propositions are provided in Appendix B. The absence of a

![](/api/attachments/AGS42M8A/fulltext/images/3adb950cd1fb7e12e74beec7243387922e58398940aa569142f49c84ee7677f2.jpg)

Nash equilibrium for a supplier with a threatening incentive and inefficiency (i.e., leadership efficiency less than 1, from Definition 3 applied to the threatening case) in Proposition 1(a) suggests that the manufacturer has to consider other strategies such as providing a subsidy, or reducing the amount of business taken away from the unwilling supplier. A subsidy will increase a supplier's efficiency, which in turn may benefit both the supplier and the manufacturer. We take up this issue in detail later in the paper. Similarly, imposing a less harsh substitution penalty may change the supplier's incentive from threatening to motivating. Excluding the threatening and inefficient case, Table 2 shows possible combinations of the incentive type and IT-efficiency ratio of the suppliers, as well as the associated Nash equilibria.

INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 4, December 1997

Table 2 Nash Equilibria for Combinations of Incentive Type and IT-efficiency

<table><tr><td rowspan="2">Case No.</td><td colspan="2">Firm i</td><td colspan="2">Firm j</td><td rowspan="2">Nash Equilibria</td></tr><tr><td>Incentive</td><td>IT Efficiency</td><td>Incentive</td><td>IT Efficiency</td></tr><tr><td>1</td><td>Motivating</td><td>Inefficient</td><td>Motivating</td><td>Inefficient</td><td> $(T_i, T_j')$  or  $(T_i', T_j')^{14}$ </td></tr><tr><td>2</td><td>Motivating</td><td>Efficient</td><td>Motivating</td><td>Inefficient</td><td> $(0, T_j')$ </td></tr><tr><td>3</td><td>Motivating</td><td>Efficient</td><td>Motivating</td><td>Efficient</td><td> $(0, 0)$ </td></tr><tr><td>4</td><td>Motivating</td><td>Inefficient</td><td>Threatening</td><td>Efficient</td><td> $(T_i', 0)$ </td></tr><tr><td>5</td><td>Motivating</td><td>Efficient</td><td>Threatening</td><td>Efficient</td><td> $(0, 0)$ </td></tr><tr><td>6</td><td>Threatening</td><td>Efficient</td><td>Threatening</td><td>Efficient</td><td> $(0, 0)$ </td></tr></table>

$^{14}$ Multiple equilibria are feasible when both suppliers are inefficient and have motivating incentives. However, specific functional forms for profit flows will provide an equilibria refinement, and may lead to a unique outcome.

For Proposition 1(b), which of the five equilibria will be realized depends on the combination of the suppliers' incentives and efficiency. Note that regardless of its incentive, an IT-efficient supplier will join the system at 0, as long as its competitor does not have the combination of threatening incentive and inefficiency as in Proposition 1(a). Of course, an efficient supplier joining the system at 0 exerts a competitive necessity related pressure on an IT-inefficient competitor. Efficiency with respect to a proposed EDI system can come from a variety of factors. For example, a large supplier, who can gain a significant portion of a competing supplier's business by joining first, will have a large benefit flow from being the leader. This can make its leadership efficiency greater than or equal to 1. High efficiency can also come from a match between the IT platforms and internal data formats of the supplier and the manufacturer. Similarly, if the supplier is already using EDI with other manufacturers through third party EDI providers, then its marginal setup cost for conducting business through the proposed EDI network should be low, leading to a high efficiency. A low rate of the EDI cost reduction over time (i.e., a low $\lambda$ ) also increases the efficiency of a supplier.

## 4.2. Business Volume, Slack Capacity, Economies of Scale and Joining Time

In this section we analyze the impact of factors such as slack capacity and economies of scale on the suppliers' optimal joining times. We consider a scenario where both suppliers are IT-inefficient and have motivating incentives. $^{5}$ For analytical tractability, we assume differentiability of the profit and the efficiency benefit flow functions.

4.2.1. Impact of the Manufacturer's Substitution Policy and Supplier Competition.

PROPOSITION 2. (a) Without the substitution policy of the manufacturer, each supplier behaves as a monopolist with respect to joining time.

(b) The leading supplier joins earlier with an increase in its own substitution gain factor or slack capacity. The follower also joins earlier with an increase in the leader's substitution gain factor or slack capacity.

Without the substitution policy of the manufacturer, technological change is the only factor that drives a supplier's joining decision; since there is no substitution gain or loss from joining early or late respectively, a supplier will join at a time when the marginal setup cost will equal the marginal efficiency benefit from EDI. A penalty imposed by the manufacturer forces both the leader and the follower to join earlier (than a monopolist supplier).

Proposition 2b brings out the importance of slack capacity and the severity of the manufacturer's substitution policy. A higher slack capacity or a larger substitution gain factor motivates the leader and forces its competitor to join sooner.

## 4.2.2. Business Volume and Economies of Scale.

PROPOSITION 3. (a) If there are positive or zero economies of scale, both the leader and the follower join earlier with an increase in business volume.

(b) Both the leader and the follower join earlier with an increase in economies of scale.

An increase in business volume helps offset the EDI setup cost more easily, thereby speeding up the adoption process. Thus, larger suppliers should adopt the technology earlier, ceteris paribus. This finding is supported by the business literature: "Most large organizations are now using, implementing or trialing EDI. However, . . . small and medium-sized enterprises are showing much more resistance than was expected to the adoption of EDI." (Taylor 1993). The result holds even if there are zero economies of scale, whereby the marginal profit remains the same for all levels of business volume. Of course, the presence of positive economies of scale will make EDI attractive even sooner. By the same reasoning, an increase in the level of economies of scale for a given business volume will lead to an earlier adoption by both the leader and the follower.

4.2.3. Implications of the Manufacturer's Restoration Policy. Two factors determine the penalty system of the manufacturer. The first is the level of substitution of one supplier's business with that of another. We scrutinized this effect in Proposition 2, and showed that a higher substitution gain factor leads to an earlier adoption by both the suppliers. The second factor involves the business volume restoration policy (after the follower joins the system). This was described in § 3.2, where we considered three potential policies with respect to the post-EDI business volume. We denote these policies by P1, P2 and P3:

(P1): Instantaneous restoration, where the manufacturer restores the follower's business volume as soon as it joins the system.

(P2): Gradual recovery, where the manufacturer gradually restores the follower's business volume

(P3): Punishment, where the manufacturer does not restore the old business volume of the follower.

PROPOSITION 4. If the follower has a motivating incentive with a particular policy, a more severe policy makes both the manufacturer and the supplier worse off.

From the viewpoint of the follower, P3 is the most severe policy, followed by P2 and P1. The intuition behind the proposition is that rather than occurring earlier, the follower's joining is delayed even more due to a more severe restoration policy. This is attributed to the fact that the followership efficiency is reduced with an increase in the severity of the restoration policy. This Proposition suggests that the manufacturer must consider the incentive of the follower in choosing a restoration policy, since a motivating incentive with a particular policy implies that the manufacturer will be worse off with a more severe policy. What is the impact of the severity of the restoration policy on the manufacturer's payoff if the supplier has a threatening incentive? From Proposition 1a, there is no Nash equilibrium for an inefficient supplier with a threatening incentive. That is, in the Nash framework, the supplier will not join the EDI system. If the manufacturer increases the severity of the restoration policy, the threatening incentive of the supplier, given by $(\pi_{k}^{1}-\pi_{k}^{0})-(\pi_{k}^{3}-\pi_{k}^{2})<0$ for supplier k in Definition 2, moves toward motivating due to a reduction in $\pi_{k}^{3}$ . Note that the other profit flows are not affected by the severity of the restoration policy. If the reduction in $\pi_{k}^{3}$ actually switches the incentive from threatening to motivating, then the supplier will join the system according to a Nash outcome, thereby increasing the payoff to the manufacturer.

## 4.3. Slack Capacity versus IT Efficiency

From the Nash equilibrium and the comparative statics, we find that the manufacturer's substitution policy makes supplier firms join earlier, and that IT efficiency makes a difference in a firm's decision regarding the joining time. Thus, intuitively it appears that an IT-inefficient firm will attempt to resist joining the system as long as possible. The literature supports the notion that smaller firms try to resist the adoption of EDI. Newburger (1993) notes: "... for smaller suppliers, and agents, adopting EDI rarely nets enough direct savings to justify its cost.... Ford surveyed 250 of its EDI trading partners only to find that only five percent could identify any direct cost savings associated with EDI. Why, then, did they adopt EDI? Plain and simple, adopting EDI enabled Ford's suppliers to continue doing business with Ford." This observation leads to questions involving resistance and willingness of suppliers in joining the network depending on how much business the suppliers can take away from a competitor by joining earlier. It relates to the important notion of “beneficial” and “unfortunate” strategic necessity (Clemons and Kimbrough 1987, Clemons and Row 1988) as applied to the case of EDI.

For analytical tractability, we assume that the profit and the efficiency benefit flow functions increase linearly with the business volume. That is, the unit price and the unit efficiency benefit are assumed to be constant. These assumptions are used only in Proposition 5.

We analyze a setting where supplier j is IT efficient. If i does not join the system, the manufacturer will transfer a portion of i's business volume to j, if the latter joins first. The amount of transfer is limited only by the competitor's capacity. If the manufacturer chooses to transfer only a certain percentage of i's business, which can be less than what the competitor j can absorb, then the same analysis can be done in terms of the manufacturer's substitution policy instead of the slack capacity. $^{6}$

We first establish some threshold values of i's substitution gain factor and j's slack capacity, which determine i's incentive and efficiency types, and hence its EDI joining time. We show that these threshold values define four distinct regions with the efficient supplier j's slack capacity and i's substitution gain factor as the axes. Supplier i's behavior can be studied from the region it falls in, depending on its competitor's slack capacity and its own substitution gain factor. $^{7}$

PROPOSITION 5. Under the assumption of constant unit price and unit efficiency benefit, we have the following results:

(a) For a given slack capacity level of the IT-efficient supplier j, there is a threshold value of the IT-inefficient supplier i's substitution gain factor above (below) which i has a motivating (threatening) incentive.

(b) When supplier i has a motivating incentive, there is a threshold slack capacity of the IT-efficient supplier j, above which supplier i joins the EDI network at time 0.

(c) When supplier i has a threatening incentive, there is a threshold substitution gain factor above which it joins the EDI network at time 0. When its substitution gain factor is smaller than this threshold value, supplier i does not join the system.

For an interpretation of these results, it is useful to plot four distinct regions created by the threshold values of i's substitution gain factor and j's slack capacity. The threshold values corresponding to Propositions 5a, 5b and 5c are shown in Figures 2a, 2b, and 2c, respectively. Figure 2d shows the superimposed diagram, where four distinct areas have different implications for the joining decision of supplier i. The expressions for these threshold values are derived in Appendix B.

Proposition 5(a) implies that if the IT-inefficient supplier itself has a sufficiently high slack capacity (or equivalently, a high substitution gain factor), then it has a motivating incentive to join the system. In other words, an IT-inefficient but large supplier with significant slack capacity will be motivated to join the system because of the possibility of taking away some business from its competitor. This threshold substitution gain factor depends on the efficient supplier j's slack capacity, $\nu_{j}^{m}$ , and is shown in Figure 2a as the line $\alpha_{i} = \alpha(\nu_{j}^{m})$ . It separates motivating and threatening regions in the diagram. Thus, in Figure 2d, areas 2 and 3 have threatening incentives, while the remaining areas 1 and 4 have motivating incentives for i. Of course, the exact joining time of i is determined by its efficiency. For example, if it is inefficient and has a motivating incentive, it will adopt EDI sometime after the system is announced, when the setup cost has been reduced sufficiently. On the other hand, with a threatening incentive and inefficiency, the supplier will not join the system, as shown in proposition 1a. Thus, the slack capacity of a supplier (which determines its incentive type) is an important factor in its joining decision, and should also be taken into consideration by the manufacturer in deciding on its "stick" and "carrot."

Figure 2 /s Joining Time as a Function of Its Substitution Gain Factor and /s Slack Capacity  
![](/api/attachments/AGS42M8A/fulltext/images/4171c2796ddb393add3da46d4d44c82f5cfb50e8becd70fbf70fb0d075b9246f.jpg)

![](/api/attachments/AGS42M8A/fulltext/images/20a7d5a1ac02c510e461279106c3747e5194ec556315af3776b670ca5b15578b.jpg)

![](/api/attachments/AGS42M8A/fulltext/images/45fa7492f6987dd58383b27b78ddd7aa5c221b05463aee76762644d8151ec162.jpg)

![](/api/attachments/AGS42M8A/fulltext/images/c65792db372f7df0dfa514572b713ec96ac76cf4f3c522eca5c7bd5ff05e4568.jpg)

Area 4 in Figure 2d represents the case of "beneficial" strategic necessity (Clemons and Kimbrough 1987). The "beneficial" nature of the EDI impact arises from the motivating incentive of supplier $i$ . The competing IT-efficient supplier has enough slack capacity (as stated in Proposition 5(b)) to make supplier $i$ 's followership (and hence leadership) efficiency to be greater than or equal to 1, and supplier $i$ joins the network at time 0. If the slack capacity of the IT-efficient supplier $j$ is below the threshold level (as in area 1), then supplier $i$ 's followership efficiency ratio will be less than 1, whereby the latter will join the system some time after it is announced. Thus, it is the threshold slack capacity level of the competitor that makes joining the system a necessity for supplier i. Since both the suppliers join the system at time zero, they both enjoy the efficiency benefits associated with EDI. However, since they are not able to take away any business from each other, they do not derive any strategic advantage out of the EDI. Thus, in this case, the industry is better off due to EDI related efficiency gains.

A threatening incentive is created when i's substitution gain factor is less than the level specified in proposition 5(a). This level, in turn, depends on the slack capacity of the competing supplier. A threatening incentive creates an unfortunate necessity for a supplier, since its benefit from joining EDI early is less than the opportunity cost of not joining the system.

Proposition 5(c) implies that if the substitution gain factor of supplier i is above a threshold (as shown in Figure 2c and 2d), then the leadership (and hence followership) efficiency will be greater than or equal to 1. Hence, in area 3 in Figure 2d, the supplier will join the system at time 0 with a threatening incentive. If the substitution factor is below the threshold (area 2 in Figure 2d), then the supplier will be inefficient, and will not join the system, because of the unfortunate combination of threatening incentive and inefficiency. As we have suggested earlier, in this case the supplier should consider providing a subsidy, which could benefit both the manufacturer and the supplier. The interdependency between the parameters of one supplier and the incentive and the efficiency of the competing supplier allows us to study the “strategic necessity” aspect of EDI introduction.

In summary, in this section we established the existence of threshold slack capacity and substitution gain factor levels, which endogenously determine the impact of the proposed EDI system on the competition structure (i.e., incentive and efficiency types) of the suppliers.

## 4.4. Subsidizing the Suppliers' Setup Costs

To this point, we have analyzed the manufacturer's "stick" in the form of a substitution/restoration policy. While such a penalty system induces earlier adoption of the network, in Proposition 4 we also showed that a more severe policy makes both the manufacturer and the follower worse off under certain conditions. In this section, we analyze the manufacturer's "carrot" in the form of a subsidy to partially offset the setup cost of a supplier. The subsidy can be provided in conjunction with the substitution/restoration policy, and we show that this combination of subsidy and penalty increases the payoff to the manufacturer.

For Proposition 6 below, we assume that supplier i has slack capacity and that it is IT-efficient for the proposed EDI, while its competitor j is IT-inefficient. In order to promote j's joining the system earlier, the manufacturer may share j's setup cost at the joining time. $^{8}$ That is, the manufacturer provides a subsidy $\theta C_{j}(t)$ , where $0 \leq \theta \leq 1$ is the fraction of the setup cost shared by the manufacturer. The subsidy increases the EDI related efficiency of the supplier. The manufacturer can induce supplier j to join as soon as the EDI network is announced by providing a subsidy level which makes the supplier efficient. We show in Appendix A.7 that there is a subsidy level $\bar{\theta} < 1$ which makes the supplier efficient in the proposed EDI. It implies that the manufacturer need not subsidize over the level $\bar{\theta}$ to induce j into joining the system immediately. In other words, the manufacturer's subsidy level has an upper bound of $\bar{\theta}$ .

4.5. The Impact of the Subsidy on Joining Times
Say the manufacturer gains an additional payoff, $a\nu$ (a is a constant), when transaction volume $\nu$ is conducted through the EDI system. For example, the manufacturer could operate in the just-in-time (JIT) mode with volume $\nu$ , and in the non-JIT mode with $\nu^{0} - \nu$ . However, in this situation, the manufacturer has two sets of bookkeeping activities, one for EDI and the other for paper based transactions. Hence, as the EDI volume $\nu$ increases, the benefit to the manufacturer also increases. Therefore, a subsidy strategy which will induce the follower to join the network early is of key importance to the manufacturer. The optimal subsidy level depends on the incentive and the efficiency of the follower, as stated in Proposition 6 below.

PROPOSITION 6. If the followership efficiency of a follower (say j) with a motivating incentive is above a threshold, $\tau$ , then the manufacturer provides the maximum subsidy level, $\bar{\theta}$ , which makes the follower efficient to join at time zero. Otherwise, the subsidy is below the maximum level. For an inefficient supplier j with a threatening incentive, when $\frac{1}{\gamma}a(\nu_j^0 + \nu_i^0) > \bar{\theta}\mathbf{C}_j(0)$ , the manufacturer provides the maximum subsidy level, $\bar{\theta}$ . Otherwise the subsidy is zero.

We first discuss the case of motivating incentive. The manufacturer will optimize its net benefit in subsidizing a supplier by weighing the benefits of earlier network expansion against the subsidy costs as described in the proof of this proposition (in Appendix B). If a supplier is too inefficient (either due to a small size or a lack of IT infrastructure), whereby the costs incurred by the manufacturer are not offset by a correspondingly large benefit, the manufacturer will not try to make the supplier join the system at time zero. Therefore, a supplier must have a minimum efficiency level in order to attract the maximum subsidy from the manufacturer. Thus, it is possible that the manufacturer will choose not to subsidize small suppliers (who may not bring enough benefits, and who cost more to subsidize) to the maximum level.

The case of threatening incentive deserves special mention. Without a subsidy, there is no Nash equilibrium because of the presence of the inefficient supplier with a threatening incentive. The only way to induce this supplier to join (and thereby achieve a Nash equilibrium) is to provide the maximum subsidy level. The term on the left hand side of the inequality in Proposition 6 is the manufacturer's benefit from providing the maximum subsidy. To see why, note that i is already efficient, and that by inducing j to join at 0, the entire volume of business transactions, $\nu_{j}^{0} + \nu_{i}^{0}$ , occurs over the EDI network from time 0. The term on the right hand side is the cost of the subsidy. If the cost exceeds the benefit, the manufacturer provides no subsidy at all, in which case there is no Nash equilibrium.

4.5.1. Whom to Subsidize. In this section we address the following questions: (1) How does subsidizing one supplier affect the other's joining decision? (2) From which supplier and under what conditions does the manufacturer derive higher benefits for a given subsidy level?

Figure 3 shows an interesting aspect of providing a subsidy to a supplier. A subsidy $\theta$ shifts $i$ 's best response function, $\Phi_i(\theta)$ , downward. $^9$ However, unless $T_f(\theta)$ shifts below $j$ 's indifference point, $\tilde{T}_i$ , there is no change in $j$ 's best response. Thus, the manufacturer's subsidy to either the leader or the follower does not change the competitor's best response function. The intuition behind this result is that a subsidy to a supplier does not affect its competitor's marginal benefit and cost, and that the best response (to the competitor's choice of a joining time) is a point where the marginal benefit and cost intersect.

$^{10}$ We thank the associate editor for pointing out this possibility.

However, there is a threshold level of subsidy above which the number of Nash equilibria can change. For example, if there is a unique Nash solution without the subsidy, then a "high" subsidy level can lead to multiple equilibria. The reverse case, where multiple solutions without a subsidy get reduced to a unique solution due to subsidy, is also possible. The threshold subsidy level which can change the joining times so drastically is derived in Appendix A. $^{10}$ If the subsidy to a supplier is below this threshold, then it has no impact on the competitor's joining time.

Figure 3 Impact of a Subsidy on the Supplier's Best Response Functions  
![](/api/attachments/AGS42M8A/fulltext/images/2cc6b43c300e0b9528171c6c9ba0317dc3fc3a1c246bda5e2be37445f9cbe572.jpg)  
INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 4, December 1997

PROPOSITION 7. Unless a change in the number of Nash equilibria takes place, the manufacturer's subsidy to either the leader or the follower does not change the competitor's joining time.

This proposition implies that the manufacturer cannot, in general, induce both suppliers to join earlier by providing a subsidy to only one supplier. The proposition is counterintuitive in the sense that a subsidy to a supplier should exert competitive pressure on the other supplier. However, as long as a subsidy level to a supplier is not large enough (as derived in Appendix A) to reverse leadership and followership positions, it does not affect the competing supplier's marginal benefit and cost (and hence the joining time).

Does the manufacturer obtain higher benefits by subsidizing the supplier who would be a leader without a subsidy, instead of the follower? The answer depends on the slack capacity of the leader. As the leader's slack capacity increases, the manufacturer obtains higher (lower) benefits by subsidizing the leader (follower). This leads to Proposition 8.

PROPOSITION 8. The larger the slack capacity of the leader, the higher (lower) the manufacturer's incentive to invest in the leader (follower).

The intuition behind this result is that the volume of business transactions conducted over the EDI network (and hence the manufacturer's benefits) increases with the slack capacity of the leader. Since we considered a non-differentiated product in this model, the manufacturer is indifferent between buying the product from one supplier versus the other, provided the transaction takes place through EDI. While the manufacturer and the leader are better off with increasing slack capacity of the leader, this is a Pareto inferior case from the follower's standpoint.

## 5. Future Research

An important issue not addressed in this paper involves the possibility of a cooperative relationship between the trading partners. Given the notion that EDI will become a strategic necessity for doing business (e.g., see Clemons and Kimbrough 1986, 1987; Clemons and Kleindorfer 1992), a cooperative solution between the manufacturer and individual suppliers may provide interesting implications for the way in which the benefits of the technology may be divided among the partners. Of course, such a framework applies to the case where the suppliers have sufficient bargaining power. This model will involve the notion of asset specificity of the EDI investment, and will investigate the role of EDI standards and network externalities in the sharing of EDI related surplus. The relevant research questions include the following: How can we explain the formation of coalitions between suppliers and manufacturers through EDI linkages? What are the impacts of asset specificity, EDI standards and network externalities on the competition structure and profitability of the trading partners? Two key recent papers which offer insights into the nature of these problem are Bakos and Brynjolfsson (1993) and Clemons, Reddi and Row (1993). Both papers suggest (although from different viewpoints) that IOS will lead to fewer suppliers and closer trading relationships.

A bargaining model may be used to explain the phenomenon of “quasi-integration” between manufacturers and suppliers. The impact of asset specificity and IOS standards on the system ownership decisions of the trading partners will also be investigated. Similarly, the joint effects of ownership and asset specificity on the post bargaining power of the players will be assessed. These issues can be modeled by using a variation of the general framework suggested by Hart and Moore (1990) and by building on the results of Clemons and Kleindorfer (1992). The model will also help address the important question of sustainability of the surplus generated through the IOS.

## 6. Conclusion

The ability to measure the economic impacts of strategic IOS is crucial to successful IT investment decisions. IOS initiators need to assess the potential barriers to the widespread acceptance of the system, as well as strategies to facilitate the adoption process. The potential adopters of the IOS must evaluate the impacts of their decisions on their competitive position and bargaining power, and analyze whether the proposed system will become an “unfortunate” or “beneficial” necessity. In addition to the issue of strategic necessity, the potential adopters need insights into operational issues regarding optimal joining times, and how such times are affected by IOS setup costs, efficiency and business volume gains, and the opportunity costs of joining late. This research adds to the MIS literature by developing a theory-based model for understanding the above issues in the context of EDI technology. It also augments a small but growing body of economics of IS research by building on the results of prior studies in this domain.

For a manufacturer developing an EDI system, our model provides a basis to analyze its suppliers' incentives, and also specifies guidelines regarding the policies that may be adopted to induce the suppliers to join the system. From the suppliers' standpoint, the study presents decision guidelines regarding the timing and the magnitude of investment in EDI. The insights obtained for EDI systems may be generalized to other forms of IOS. $^{11}$

Appendix A. Mathematical Formulations

A.1. Change in Supplier i's Business Volume Due to the Manufacturer's Substitution Policy

$$
v _ {t} ^ {0} = \left( \begin{array}{l} v _ {t} ^ {0}, \quad t <   T _ {t}, \\ v _ {t} ^ {0} + \alpha_ {t} v _ {t} ^ {0}, T _ {t} \leq t \leq T _ {j}, \text {where} 0 \leq \alpha_ {t} \leq v _ {j} ^ {0} / v _ {t} ^ {0}, \\ \left\{ \begin{array}{l} v _ {t} ^ {0} \quad (\text {instantaneous restoration}), \\ \max (v _ {t} ^ {0} + \alpha_ {t} v _ {t} ^ {0} - \beta_ {j} \Delta t, v _ {t} ^ {0}) \\ (\text {gradual recovery}) \text {where} \Delta t = t - T _ {j} \\ v _ {t} ^ {0} + \alpha_ {t} v _ {t} ^ {0} \quad (\text {punishment}), \end{array} \right. \end{array} \right\}, \quad t > T _ {j}.
$$

The positive coefficient $\beta_{j}$ determines the rate of restoration of j's business volume. The corresponding volume of the competing supplier j is given by

$$
v _ {j} ^ {t} = \left( \begin{array}{l} v _ {j} ^ {0}, \quad t <   T _ {1}, \\ v _ {j} ^ {0} - \alpha_ {j} ^ {\prime} v _ {j} ^ {0}, \quad T _ {1} \leq t \leq T _ {j},   0 \leq \alpha_ {j} ^ {\prime} <   1, \\ \left\{ \begin{array}{l} v _ {j} ^ {0} \\ \min (v _ {j} ^ {0} - \alpha_ {j} ^ {\prime} v _ {j} ^ {0} + \beta_ {j} \Delta t, v _ {j} ^ {0}. \Delta t = t - T _ {j} \\ v _ {j} ^ {0} - \alpha_ {j} ^ {\prime} v _ {j} ^ {0} \end{array} \right\}, \quad t > T _ {j}. \end{array} \right.
$$

A.2. Profit Flow Functions for Supplier i

$\pi_{i}^{0} = \pi_{i}^{0}(v_{i}^{0}), 0 \leq t \leq \min(T_{i}, T_{j})$ , i.e., $i$ 's profit flow before anyone has joined the system,

$$
\pi_ {i} ^ {1} = \pi_ {i} ^ {0} (v _ {i} ^ {0} + \alpha_ {i} v _ {i} ^ {0}) + \varepsilon_ {i} (v _ {i} ^ {0} + \alpha_ {i} v _ {i} ^ {0}), T _ {i} \leq t \leq T _ {j},
$$

$\pi_{i}^{2} = \pi_{i}^{0}(v_{i}^{0} - \alpha_{i}^{\prime}v_{i}^{0}), T_{j} \leq t \leq T_{i},$ i.e., $i$ 's profit flow when only $j$ joins the system,

$\pi_{i}^{3} = \pi_{i}^{0}(v_{i}^{0}) + \varepsilon_{i}(v_{i}^{0}), \max(T, T_{j}) \leq t, \text{ i.e., steady state profit flow of firm } i, \text{ after both the suppliers join the system.}$

## A.3. Leadership and Followership Payoff Functions for Supplier i

$$
\begin{array}{r l} L _ {i} (T _ {i}, T _ {j}) & = \int_ {0} ^ {T _ {i}} \pi_ {i} ^ {0} e ^ {- \gamma t} d t + \int_ {T _ {i}} ^ {T _ {j}} \pi_ {i} ^ {1} e ^ {- \gamma t} d t \\ & \quad + \int_ {T _ {j}} ^ {\infty} \pi_ {i} ^ {3} e ^ {- \gamma t} d t - C _ {i} ^ {0} e ^ {- \lambda_ {i} T _ {i}} \\ & = \int_ {0} ^ {T _ {i}} \pi_ {i} ^ {0} (v _ {i} ^ {0}) e ^ {- \gamma t} d t \\ & \quad + \int_ {T _ {i}} ^ {T _ {j}} (\pi_ {i} ^ {0} (v _ {i} ^ {0} + \alpha_ {i} v _ {i} ^ {0}) + \varepsilon_ {i} (v _ {i} ^ {0} + \alpha_ {i} v _ {i} ^ {0})) e ^ {- \gamma t} d t \\ & \quad + \int_ {T _ {j}} ^ {\infty} (\pi_ {i} ^ {0} (v _ {i} ^ {0}) + \varepsilon_ {i} (v _ {i} ^ {0})) e ^ {- \gamma t} d t - C _ {i} ^ {0} e ^ {- \lambda_ {i} T _ {i}}. \end{array}\tag{1}
$$

$$
\begin{array}{r l} F _ {i} (T _ {i}, T _ {j}) & = \int_ {0} ^ {T _ {j}} \pi_ {i} ^ {0} e ^ {- \gamma t} d t + \int_ {T _ {j}} ^ {T _ {i}} \pi_ {i} ^ {2} e ^ {- \gamma t} d t \\ & \quad + \int_ {T _ {i}} ^ {\infty} \pi_ {i} ^ {3} e ^ {- \gamma t} d t - C _ {i} ^ {0} e ^ {- - \lambda_ {i} T _ {i}} \\ & = \int_ {0} ^ {T _ {j}} \pi_ {i} ^ {0} (v _ {i} ^ {0}) e ^ {- \gamma t} d t + \int_ {T _ {j}} ^ {T _ {i}} \pi_ {i} ^ {0} (v _ {i} ^ {0} - \alpha_ {i} ^ {\prime} v _ {i} ^ {0}) e ^ {- \gamma t} d t \\ & \quad + \int_ {T _ {i}} ^ {\infty} (\pi_ {i} ^ {0} (v _ {i} ^ {0}) + \varepsilon_ {i} (v _ {i} ^ {0})) e ^ {- \gamma t} d t - C _ {i} ^ {0} e ^ {- \lambda_ {i} T _ {i}} \end{array}\tag{2}
$$

For identical suppliers, the general form of the payoff functions above (the first line of equations (1) and (2)) is the same as that of Reinganum (1981a), except for the cost components. However, the strategic (penalty related) and the efficiency components of the profit flows introduced in our model (lines 2 and 3 of both equations (1) and (2)) lead to interesting results involving the severity of the penalty system and the slack capacity of the suppliers (e.g., Propositions 2, 4, and 5).

## A.4. First and Second Derivatives of the Leadership and Followership Payoff Functions for Supplier i

For fixed $T_{j}, \forall T_{i} \leq T_{j}$

$$
L _ {i} ^ {\prime} (T _ {i}, T _ {j}) = \frac {\partial L _ {i} (T _ {i} , T _ {j})}{\partial T _ {i}} = (\pi_ {i} ^ {0} - \pi_ {i} ^ {1}) e ^ {- \gamma T _ {i}} + C _ {i} ^ {0} \lambda_ {i} e ^ {- \lambda_ {i} T},\tag{3}
$$

$$
L _ {t} ^ {\prime \prime} (T _ {1}, T _ {j}) = \frac {\partial^ {2} L _ {t} (T _ {1} , T _ {j})}{\partial T _ {t} ^ {2}} = - \gamma (\pi_ {t} ^ {0} - \pi_ {t} ^ {1}) e ^ {- \gamma T _ {t}} - C _ {t} ^ {0} \lambda_ {t} ^ {2} e ^ {- \lambda_ {t} T}.\tag{4}
$$

For fixed $T_{j}, \forall T_{i} \geq T_{j}$

$$
F _ {i} ^ {\prime} (T _ {i}, T _ {j}) = \frac {\partial F _ {i} (T _ {i} , T _ {j})}{\partial T _ {i}} = (\pi_ {i} ^ {2} - \pi_ {i} ^ {3}) e ^ {- \gamma T _ {i}} + C _ {i} ^ {0} \lambda_ {i} e ^ {- \lambda_ {i} T},\tag{5}
$$

$$
F _ {i} ^ {\prime \prime} (T _ {i}, T _ {j}) = \frac {\partial^ {2} F _ {i} (T _ {i} , T _ {j})}{\partial T _ {i} ^ {2}} = - \gamma (\pi_ {i} ^ {2} - \pi_ {i} ^ {3}) e ^ {- \gamma T _ {i}} - C _ {i} ^ {0} \lambda_ {b} ^ {2} e ^ {- \lambda_ {i} T}.\tag{6}
$$

A.5. Best Response Functions and Nash Equilibrium Using Definitions 4 and 5 below, we can compute $i$ 's joining time in response to $j$ 's choice, $T_j$ , as described in Lemma 1.

DEFINITION 4. The best response function of supplier i to j's joining time, $T_{j}$ , is:

$$
\Phi_ {i} (T _ {j}) = \{T _ {i} \in [ 0, \infty) \mid \Pi_ {i} (T _ {i}, T _ {j}) \geq \Pi_ {i} (T, T _ {j}) \forall T \in [ 0, \infty) \}.
$$

The joining times $T_{i}^{\mathrm{N}}, T_{j}^{\mathrm{N}} \in [0, \infty)$ constitute a Nash equilibrium if

$\Pi_{i}(T_{i}^{N}, T_{j}^{N}) \geq \Pi_{i}(T_{i}, T_{j}^{N}) \forall T_{i}$ and $\Pi_{j}(T_{i}^{N}, T_{j}^{N}) \geq \Pi_{j}(T_{i}^{N}, T_{j}) \forall T_{j}$ .

From Definition 4, it follows that $T_{i}^{N} = \Phi_{i}(T_{j}^{N})$ and $T_{j}^{N} = \Phi_{j}(T_{i}^{N})$ .

DEFINITION 5. For a fixed $T_{j'}$ let $T_{i}^{l}$ and $T_{i}^{l}$ be the times that maximize $L_{i}(t, T_{j})$ and $F_{i}(t, T_{j})$ , respectively. Let $g(t) = L_{i}(T_{i}^{l}) - F_{i}(T_{i}^{f}, t)$ . $T_{j}$ is defined as the time for which $g(\bar{T}_{j}) = 0$ .

## A.6. Multiple Equilibria with High Subsidy Levels

Let $\dot{\theta}_i$ be the subsidy level such that $T_i^i (\dot{\theta}_i) = \tilde{T}_i$ . That is, $\dot{\theta}_i$ is the subsidy to $i$ which makes $j$ indifferent between being a leader or a follower. $\theta_{i}$ is the maximum subsidy level for firm $i$ defined by equation (10), and let $\theta_{min} = \min (\ddot{\theta}_i,\bar{\theta}_i)$ . Then, the Nash equilibrium $(T_1^*,T_j^*)$ is given as:

$$
(T _ {i} ^ {\star}, T _ {j} ^ {\star}) = \left( \begin{array}{l} \left\{(T _ {i} ^ {l} (\theta_ {i}), T _ {j} ^ {l}) \text {or} (T _ {i} ^ {l} (\theta_ {i}), T _ {j} ^ {l}, 0 \leq \theta_ {i} <   \bar {\theta} _ {i}, \\ (0, T _ {j} ^ {l}), \quad \theta_ {i} \geq \bar {\theta} _ {i}, \end{array} \right), \text {where} \theta_ {i} > \bar {\theta} _ {i}, \\ \left\{ \begin{array}{l} (T _ {i} ^ {l} (\theta_ {i}), T _ {j} ^ {l}) \text {or} (T _ {i} ^ {l} (\theta_ {i}), T _ {j} ^ {l}), 0 \leq \theta_ {i} <   \theta_ {i}, \\ (T _ {i} ^ {l} (\theta_ {i}), T _ {j} ^ {l}), \quad \theta_ {i} \leq \theta_ {i} \leq \bar {\theta} _ {i}, \end{array} \right), \text {where} \theta_ {i} \leq \bar {\theta} _ {i}. \end{array} \right.\tag{7}
$$

That is, there exists a subsidy level, $\theta_{min}$ , which changes the number of Nash equilibria (from multiple equilibria to a unique solution, or vice versa).

## A.7. Maximum Subsidy to Induce Immediate Joining

Let $r_{j}^{l}(\theta)$ and $r_{j}^{f}(\theta)$ denote the new leadership and followership IT-efficiency ratios respectively, with a subsidy $\theta C_{j}(t)$ . Then, from Definition 1,

$$
r _ {j} ^ {l} (\theta) = \frac {\pi_ {j} ^ {1} - \pi_ {j} ^ {0}}{\lambda_ {j} C _ {j} ^ {0} (1 - \theta)} = \frac {1}{1 - \theta} r _ {j} ^ {l},\tag{8}
$$

$$
r _ {j} ^ {f} (\theta) = \frac {\pi_ {l} ^ {3} - \pi_ {l} ^ {2}}{\lambda_ {l} C _ {l} ^ {0} (1 - \theta)} = \frac {1}{1 - \theta} r _ {j} ^ {f},\tag{9}
$$

where $r_j^l$ and $r_j^f$ are the leadership and the followership IT efficiencies, respectively, without any subsidy. By setting $r_j^l(\theta) = 1$ and $r_j^f(\theta) = 1$ , we note that:

$$
\bar {\theta} = \left\{ \begin{array}{l l} 1 - r _ {j} ^ {f} = 1 - \frac {\pi_ {I} ^ {3} - \pi_ {J} ^ {2}}{\lambda_ {J} C _ {J} ^ {0}} & (\text { for   the   case   of   motivating   incentive }) \\ 1 - r _ {J} ^ {I} = 1 - \frac {\pi_ {I} ^ {1} - \pi_ {J} ^ {2 0}}{\lambda_ {J} C _ {J} ^ {0}} & (\text { for   the   case   of   threatening   incentive }). \end{array} \right.\tag{10}
$$

Since a subsidy level $\geq\bar{\theta}$ makes the supplier IT-efficient, it joins the system at t=0.

## Appendix B. Mathematical Proofs

In order to prove Lemma 1, we need to derive the following additional lemmas.

LEMMA 2. $L_{t}(t,t) = F_{t}(t,t)\forall t$

PROOF. When $T_{i} = T_{j} = t$ , the second integral in both Equations (1) and (2) becomes zero. Hence, the leadership payoff for i equals its followership payoff when $T_{i} = T_{j}$ . ☐

LEMMA 3. (a) If $C_{i}(0) < \pi_{i}^{0} - \pi_{i}^{1}$ , then

$$
T _ {i} ^ {l} = \frac {1}{\lambda_ {i} - \lambda} \ln \frac {\lambda_ {i} C _ {i} ^ {0}}{\pi_ {i} ^ {1} - \pi_ {i} ^ {0}},\tag{11}
$$

otherwise, $T_{i}^{f} = 0$ .

(b) If $C_l^l (0) < \pi_l^2 -\pi_l^3$ , then

$$
T _ {i} ^ {f} = \frac {1}{\lambda_ {i} - \lambda} \ln \frac {\lambda_ {i} C _ {i} ^ {0}}{\pi_ {i} ^ {3} - \pi_ {i} ^ {2}},\tag{12}
$$

otherwise, $T_{i}^{f} = 0$ .

PROOF. Taking the derivative of the leadership payoff with respect to $T_{i}$ (as in equation (3)) and setting to zero, we have the first order condition $L_{i}^{\prime}(\hat{T}, T_{j}) = 0$ , where $\hat{T}$ is the value of $T_{i}$ which satisfies the first order condition. Since $C_{i}^{\prime}(0) = -\lambda_{i}C_{i}^{0}$ , from Equation (3),

$$
\hat {T} = \frac {1}{\lambda_ {i} - \gamma} \ln \frac {\lambda_ {i} C _ {i} ^ {0}}{\pi_ {i} ^ {1} - \pi_ {i} ^ {0}}.
$$

Also, the second derivative $L_{i}^{\prime \prime}(\hat{T}, T_{j}) < 0$ satisfies the condition for a maximum. Hence, $L_{i}(T_{i}, T_{j})$ has its maximum at $\hat{T}$ provided $\hat{T} \in (0, \infty)$ . When $C_{i}'(0) < \pi_{i}^{0} - \pi_{i}^{1}$ , $\lambda_{i}C_{i}^{0}/(\pi_{i}^{1} - \pi_{i}^{0}) > 1$ . Then $\ln (\lambda_{i}C_{i}^{0}/(\pi_{i}^{1} - \pi_{i}^{0})) > 0$ , implying that $\hat{T} \in (0, \infty)$ . Therefore,

$$
\hat {T} _ {i} ^ {l} = \hat {T} = \frac {1}{\lambda_ {i} - \gamma} \ln \frac {\lambda_ {i} C _ {i} ^ {0}}{\pi_ {i} ^ {1} - \pi_ {i} ^ {0}}.
$$

Now suppose $C_i'(0) \geq \pi_i^0 - \pi_i^1$ , which implies that $\lambda_i C_i^0 \leq \pi_i^1 - \pi_i^0$ . Then we have

$$
\begin{array}{r l} L _ {t} ^ {\prime} (T _ {t}, T _ {j}) & = (\pi_ {t} ^ {0} - \pi_ {t} ^ {1}) e ^ {- \gamma T _ {t}} + \lambda_ {t} C _ {t} ^ {0} e ^ {- \lambda_ {t} T _ {t}} \leq (\pi_ {t} ^ {0} - \pi_ {t} ^ {1}) e ^ {- \gamma T _ {t}} + (\pi_ {t} ^ {1} - \pi_ {t} ^ {0}) e ^ {- \lambda_ {t} T _ {t}} \\ & = (\pi_ {t} ^ {1} - \pi_ {t} ^ {0}) (e ^ {- \lambda_ {t} T _ {t}} - e ^ {- \gamma T _ {t}}) <   0 \quad (\text { because } \lambda_ {t} > \gamma) \end{array}
$$

That is, $L_{i}(T_{i},\cdot)$ is decreasing over $T_{i}\in [0,\infty)$ and has its maximum at $T_{i} = 0$ . We can apply the same procedure to the functions $F_{i}(T_{i},T_{j})$ , $F_{i}^{\prime}(T_{i},T_{j})$ and $F_{i}^{\prime \prime}(T_{i},T_{j})$ .

LEMMA 4. (a) With $i$ having a motivating incentive, if $C_i'(0) < \pi_i^2 - \pi_i^3$ , then $T_i^l < T_i^f$ . Otherwise, $T_i^l = T_i^f = 0$ .

(b) With $i$ having a threatening incentive, if $C_i'(0) < \pi_i^0 - \pi_i^1$ , then $T_i^l > T_i^f$ . Otherwise, $T_i^l = T_i^f = 0$ .

PROOF. A motivating incentive implies that

$$
(\pi_ {i} ^ {0} - \pi_ {i} ^ {1}) <   (\pi_ {i} ^ {2} - \pi_ {i} ^ {3}).\tag{13}
$$

Further, if $C_{i}^{\prime}(0) < \pi_{i}^{2} - \pi_{i}^{3}$ , then either relationship (14) or (15) will hold true:

$$
C _ {i} ^ {\prime} (0) <   \pi_ {i} ^ {0} - \pi_ {i} ^ {1},\tag{14}
$$

$$
\pi_ {i} ^ {0} - \pi_ {i} ^ {1} \leq C _ {i} ^ {\prime} (0) <   \pi_ {i} ^ {2} - \pi_ {i} ^ {3}.\tag{15}
$$

If the relationship (14) holds, there exists $T_{i}^{l}$ as defined by (11), and if (15) holds, $T_{i}^{l} = 0$ by Lemma 3(a). Also, with $C_{i}'(0) < \pi_{i}^{2} - \pi_{i}^{3}$ , by Lemma 3(b), there exists $T_{i}^{f}$ as defined in (12). Having established the existence of $T_{i}^{l}$ and $T_{i}^{f}$ , a comparison of (11) and (12) shows that $T_{i}^{l} < T_{i}^{f}$ .

If $C_i'(0) \geq \pi_i^2 - \pi_i^3$ , then $T_i^f = 0$ by Lemma 3(b). For a motivating incentive, $C_i'(0) \geq \pi_i^2 - \pi_i^3$ also implies that it is greater than $\pi_i^0 - \pi_i^1$ (by (13)). Hence, $T_i^l = 0$ by Lemma 3(a).

PROOF. A threatening incentive implies that

$$
(\pi_ {i} ^ {0} - \pi_ {i} ^ {1}) > (\pi_ {i} ^ {2} - \pi_ {i} ^ {3}).\tag{16}
$$

Further, if $C_{i}^{\prime}(0) < \pi_{i}^{0} - \pi_{i}^{1}$ , then either relationship (17) or (18) will hold true:

$$
C _ {i} ^ {\prime} (0) <   \pi_ {i} ^ {2} - \pi_ {i} ^ {3},\tag{17}
$$

$$
\pi_ {i} ^ {2} - \pi_ {i} ^ {3} \leq C _ {i} ^ {\prime} (0) <   \pi_ {i} ^ {0} - \pi_ {i} ^ {1}.\tag{18}
$$

If relationship (17) holds, there exists $T_{i}^{f}$ as defined by (12), and if (18) holds, $T_{i}^{f} = 0$ by Lemma 3(b). Also, with $C_{i}^{\prime}(0) < \pi_{i}^{0} - \pi_{i}^{1}$ , by Lemma 3(a), there exists $T_{i}^{l}$ as defined in (11). Having established the existence of $T_{i}^{f}$ and $T_{i}^{l}$ , a comparison of (11) and (12) shows that $T_{i}^{f} < T_{i}^{l}$ .

If $C_t'(0) \geq \pi_i^0 - \pi_i^1$ , then $T_t^l = 0$ by Lemma 3(a), and $T_i^f = 0$ by Lemma 3(b), since $C_t'(0) \geq \pi_i^0 - \pi_i^1 > \pi_i^2 - \pi_i^3$ by (16).

For the case of identical firms, Lemmas 5a, 6, 7, and 8a below follow Reinganum's (1981a) characterization of the best response function (5b and 8b deal with the case of threatening incentive, which Reinganum does not consider).

LEMMA 5. (a) If $i$ has a motivating incentive, $L_{i}(T_{i}, T_{j}) \lessgtr F_{i}(T_{i}, T_{j})$ if $T_{i} \gtrless T_{j}$ .

(b) If $i$ has a threatening incentive, $L_{i}(T_{i}, T_{j}) \lessgtr F_{i}(T_{i}, T_{j})$ if $T_{i} \gtrless T_{j}$ .

PROOF. Through suitable change of integral limits in Equations (1) and (2),

$$
L _ {t} (T _ {\nu}, T _ {j}) - F _ {t} (T _ {\nu}, T _ {j}) = (- \pi_ {t} ^ {0} + \pi_ {t} ^ {1} + \pi_ {t} ^ {2} - \pi_ {t} ^ {3}) \int_ {T _ {t}} ^ {T _ {j}} e ^ {- \gamma t} d t.
$$

With a motivating incentive, the term $-\pi_{t}^{0} + \pi_{t}^{1} + \pi_{t}^{2} - \pi_{t}^{3}$ is positive. Further, when $T_{t}T_{j}, \int_{T_{t}}^{T_{j}} e^{-\gamma t} dt0$ . Hence the result of 5(a) follows. 5(b) can be proved in a similar manner, noting that the term $-\pi_{t}^{0} + \pi_{t}^{1} + \pi_{t}^{2} - \pi_{t}^{3}$ is negative for the case of threatening incentive. ☐

LEMMA 6. If $i$ has either a motivating or a threatening incentive, $L_{i}(T_{i}^{l}, T_{i}^{f}) > F_{i}(T_{i}^{f}, T_{i}^{f})$ .

PROOF. From the definition of $T_{i}^{l}$ (Definition 5), $L_{i}(T_{i}^{l}, T_{i}^{f}) > L_{i}(T_{i}^{f}, T_{i}^{f})$ . Further, by Lemma 2, $L_{i}(T_{i}^{f}, T_{i}^{f}) = F_{i}(T_{i}^{f}, T_{i}^{f})$ . Therefore, $L_{i}(T_{i}^{l}, T_{i}^{l}) > F_{i}(T_{i}^{l}, T_{i}^{l})$ .

LEMMA 7. If $i$ has either a motivating or a threatening incentive, $F_{i}(T_{i}^{f}, T_{i}^{l}) > L_{i}(T_{i}^{l}, T_{i}^{l})$ .

PROOF. From the definition of $T_{i}^{f}$ (Definition 5), $F_{i}(T_{i}^{f}, T_{i}^{l}) > F_{i}(T_{i}^{l}, T_{i}^{l})$ . Also, by Lemma 2, $F_{i}(T_{i}^{l}, T_{i}^{l}) = L_{i}(T_{i}^{l}, T_{i}^{l})$ . Therefore, $F_{i}(T_{i}^{l}, T_{i}^{l}) > L_{i}(T_{i}^{l}, T_{i}^{l})$ .

LEMMA 8. (a) If $i$ has a motivating incentive, there exists $\tilde{T}_{j} \in (T_{i}^{l}, T_{i}^{f})$ s.t. $L_{i}(T_{i}^{l}, T_{j})F_{i}(T_{i}^{f}, T_{j})$ as $T_{j}\tilde{T}_{j}$ .

(b) If $i$ has a threatening incentive, there exists $\tilde{T}_j \in (T_i^l, T_i^l)$ s.t. $L_i(T_i^l, T_j)F_i(T_i^l, T_j)$ as $T_j\tilde{T}_j$ .

PROOF. Let $g(t) = L_{t}(T_{i}^{l}, t) - F_{t}(T_{i}^{f}, t)$ . Then, according to Lemma 7, $g(T_{i}^{l}) < 0$ . Also, according to Lemma 6, $g(T_{i}^{f}) > 0$ . From Equations (1) and (2),

$$
\begin{array}{r l} L _ {t} (T _ {t} ^ {l}, t) - F _ {t} (T _ {t} ^ {f}, t) = & \int_ {0} ^ {T _ {t} ^ {l}} \pi_ {t} ^ {0} e ^ {- \gamma x} d x + \int_ {T _ {t} ^ {l}} ^ {t} \pi_ {t} ^ {1} e ^ {- \gamma x} d x \\ & + \int_ {t} ^ {\infty} \pi_ {t} ^ {3} e ^ {- \gamma x} d x - C _ {t} (T _ {t} ^ {l}) \\ & - \int_ {0} ^ {t} \pi_ {t} ^ {0} e ^ {- \gamma x} d x - \int_ {t} ^ {T _ {t} ^ {l}} \pi_ {t} ^ {2} e ^ {- \gamma x} d x \\ & - \int_ {T _ {t} ^ {l}} ^ {\infty} \pi_ {t} ^ {3} e ^ {- \gamma x} d x + C _ {t} (T _ {t} ^ {l}). \end{array}\tag{19}
$$

Differentiating with respect to $t$ , we obtain

$$
\frac {\partial g (t)}{\partial t} = (- \pi_ {t} ^ {0} + \pi_ {t} ^ {1} + \pi_ {t} ^ {2} - \pi_ {t} ^ {3}) e ^ {- \gamma t}.
$$

Thus $\partial g(t)/\partial T_{j}$ is positive for the case of motivating incentive. Hence, by the intermediate value theorem and the monotonicity of $g(.)$ in $t$ , there exists a unique $\tilde{T}_{j} \in (T_{i}^{l}, T_{i}^{f})$ s.t. $g(t)0$ as $T_{j}\tilde{T}_{j}$ . Similarly when $i$ has a threatening incentive, $\partial g(t)/\partial t < 0$ , i.e., $g(t)$ decreases monotonically. Now we are in a position to prove Lemma 1. $\square$

PROOF OF LEMMA 1(a). With a motivating incentive, if $r_i^f \geq 1$ (i.e., if $C_i'(0) \geq \pi_i^2 - \pi_i^3$ ), Lemma 4 implies that $T_i^l = T_i^f = 0$ . Hence, $\Phi_i(T_j) = 0$ . If $r_i^f < 1$ , by Lemma 4, there exist $T_i^l$ and $T_i^f$ such that $T_i^l < T_i^f$ . There are three possible cases:

Case I. $T_{j} < \tilde{T}_{j}$ .

$\forall T_{i}\leq T_{j}$ and $T_{i}\neq T_{i}^{l}$ $\Pi_t(T_i^f,T_j) = L_i(T_i^f,T_j)\geq F_i(T_i^f,T_j) > L_i(T_i^l,T_j)\geq L_i(T_i,T_j).$ Since $\Pi_t(T_i,T_j) = L_i(T_i,T_j)$ for $T_{i}\leq T_{j}$ (as defined in § 3.2), we have $\Pi_t(T_i^f,T_j) > \Pi_t(T_i,T_j)$ .

$\forall T_{i}\geq T_{j}$ and $T_{i}\neq T_{i}^{f}$ , Definition5 $\Pi_i(T_i^f,T_j) = F_i(T_i^f,T_j) > F_i(T_i,T_j)$ . Since $\Pi_i(T_i,T_j) = F_i(T_i,T_j)$ for $T_{i}\geq T_{j}$ (as defined in §3.2), we have $\Pi_i(T_i,T_j) > \Pi_i(T_i,T_j)$ .

Combining the above results, $\forall T_{i} \neq T_{i}^{f}$ , $\Pi_{i}(T_{i}^{f}, T_{j}) > \Pi_{i}(T_{i}, T_{j})$ . Therefore, when $T_{j} < \tilde{T}_{j}$ , the best response function is $\Phi_{i}(T_{j}) = T_{i}^{f}$ .

INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 4, December 1997

Case II. $T_{j} = \tilde{T}_{j}$ .

$\forall T_{i}\leq \tilde{T}_{j},$ and $T_{i}\neq T_{i}^{t},\Pi_{i}(T_{i}^{t},\tilde{T}_{j}) = L_{i}(T_{i}^{t},\tilde{T}_{j}) > L_{i}(T_{i},\tilde{T}_{j}).$ Since $\Pi_t(T_i,\tilde{T}_j) = L_t(T_i,\tilde{T}_j)$ for $T_{i}\leq \tilde{T}_{j}$ (as defined in § 3.2), we have $\Pi_t(T_i',\tilde{T}_j) > \Pi_t(T_i,\tilde{T}_j)$ .

$\forall T_{i}\geq \tilde{T}_{j},$ and $T_{i}\neq T_{i}^{f},\pi_{i}(T_{i}^{f},\tilde{T}_{j}) = F_{i}(T_{i}^{f},\tilde{T}_{j}) > F_{i}(T_{i},\tilde{T}_{j}).$ Since $\Pi_t(T_i,\tilde{T}_j) = F_i(T_i,\tilde{T}_j)$ for $T_{i}\geq \tilde{T}_{j}$ , we have $\Pi_t(T_i^f,\tilde{T}_j)$ $>\Pi_t(T_\nu ,\tilde{T}_j)$ . Combining the above results, $\Phi_i(T_j) = T_i^f$ or $T_{i}^{f}$ when $T_{j} = \tilde{T}_{j}$ .

$$
\text { Case   III. } T _ {j} > \tilde {T} _ {j}.
$$

$$
\forall T _ {i} \leq T _ {j}, \text {   and   } T _ {i} \neq T _ {\nu} ^ {l}, \Pi_ {i} (T _ {\nu} ^ {l}, T _ {j}) = L _ {i} (T _ {\nu} ^ {l}, T _ {j}) > L _ {i} (T _ {\nu}, T _ {j}).
$$

$$
\Pi_ {i} (T _ {\nu} ^ {l}, T _ {j}) > \Pi_ {i} (T _ {\nu}, T _ {j}).
$$

$\forall T_{i} \geq T_{j}, \text{ and } T_{i} \neq T_{\nu}^{i}, \Pi_{i}(T_{\nu}^{i}, T_{j}) = F_{i}(T_{\nu}^{i}, T_{j}) \geq L_{i}(T_{\nu}^{i}, T_{j})$ Definition5 $> L_{i}(T_{\nu}, T_{j}).$

Thus, $\Pi_{i}(T_{\nu}^{l}, T_{j}) > \Pi_{i}(T_{\nu}, T_{j})$ .

Combining the above results, $\forall T_{i} \neq T_{i}^{l}, \Pi_{i}(T_{i}^{l}, T_{j}) > \Pi_{i}(T_{i}, T_{j})$ . Thus $\Phi_{i}(T_{j}) = T_{i}^{l}$ when $T_{j}) > \tilde{T}_{j}$ .

PROOF OF LEMMA 1(b). We can prove 1(b) by following the same procedure as above. □

PROOF OF PROPOSITION 1. First we prove 1(b). Table 1 summarizes the competition structure and the corresponding best response functions from Lemma 1 (as shown in Figure 1).

The cell marked $\dagger$ in the Table 1 involves an IT-inefficient firm with a “threatening” incentive (i.e., $\pi_{t}^{1}-\pi_{t}^{0}+\pi_{t}^{2}-\pi_{t}^{3}<0$ and $\gamma_{t}^{1}<1$ ). As shown below, there is no Nash equilibrium in this case. $^{12}$ There are six cases of interest involving various combinations of incentives

$^{12}$ We restrict the joining time to a finite time horizon.

Figure 4 Possible Scenarios for Case 1 in Table 2  
![](/api/attachments/AGS42M8A/fulltext/images/56757fbc582adfae74f1db29ed1c8ead68714784e8c1c3985f275ed5dd2e4bb1.jpg)  
INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 4, December 1997

and efficiency types. We first summarize the five possible Nash equilibria in Table 2, and then provide a graphical proof.

## Best Response Functions and Nash Equilibria

Let $(T_{i}^{N}, T_{j}^{N})$ be a Nash equilibrium, which is an intersection point of the best response functions, $\Phi_{i}$ and $\Phi_{j}$ , for i and j respectively.

There are three possible scenarios for Case 1 in Table 2, as shown in Figure 4. From these graphs, the Nash equilibria are as follows:

4(a) multiple equilibria: $(T_{i}^{N}, T_{j}^{N}) = (T_{i}^{l}, T_{j}^{l})$ or $(T_{i}^{f}, T_{j}^{f})$ if $T_{i}^{l} \leq \tilde{T}_{i} \leq T_{i}^{f}$ and $T_{j}^{l} \leq \tilde{T}_{j} \leq T_{j}^{f}$ .

4(b) firm $i$ is the leader: $(T_i^N, T_j^N) = (T_i^l, T_j^l)$ if $T_i^l \leq \tilde{T}_i \leq T_i^f$ and $\tilde{T}_j \leq T_j^l$ .

4(c) firm $j$ is the leader: $(T_i^N, T_j^N) = (T_i^f, T_j^f)$ if $T_j^t \leq \tilde{T}_j \leq T_j^f$ and $\tilde{T}_i \leq T_i^t$ .

The Nash equilibria for Cases (2), (3), (4), (5), and (6) in Table 2 are shown in Figure 5.

To show that there is no Nash equilibrium for the case where one supplier (say, j) has a threatening incentive and is inefficient (i.e., a leadership efficiency less than 1 in this case), we have to consider 4 possible cases for competitor i: (i) motivating incentive and inefficiency (i.e., followership efficiency less than 1), (ii) threatening incentive and inefficiency, (iii) motivating incentive and efficient, and (iv) threatening incentive and efficient.

When i is inefficient with a motivating incentive, from Figure 6(a), the intersection points of the two best response functions are $(T_{i}^{f}, T_{j}^{f})$ and $(T_{i}^{l}, T_{j}^{l})$ . I.e., both firms try to be either leaders or followers. When both firms try to be followers, an equilibrium can be attained only if $T_{i}^{f} = T_{j}^{f}$ . Similarly, when both try to be leaders, an equilibrium can exist only if $T_{i}^{l} = T_{j}^{l}$ . However, we show that neither of these cases is feasible.

From Lemma 8(b) applied to supplier $j$ (instead of supplier $i$ ) with a threatening incentive, there exists a $\tilde{T}_i$ such that $T_j^f < \tilde{T}_i < T_j^l$ . However, $\tilde{T}_i < T_i^f$ , because $T_j^f$ is $j$ 's best response when $i$ chooses a joining time later than $\tilde{T}_i$ . Therefore, $T_j^f < \tilde{T}_i < T_i^f$ , implying that $T_j^f \neq T_i^f$ . Similarly it can be shown that $T_j^l \neq T_i^l$ . Thus there is no equilibrium associated with Figure 6(a).

![](/api/attachments/AGS42M8A/fulltext/images/215f4ad96f0b142d318f235b27e9b047ea439365e6f5aa4fe892207f4960dda9.jpg)

![](/api/attachments/AGS42M8A/fulltext/images/e89d5ec2a04e45fb46d113777cbf3e72030ed48d46c76524a8ef84a8da94e83b.jpg)

## Figure 5 Scenarios for Cases 2, 3, 4, 5, and 6 in Table 2

![](/api/attachments/AGS42M8A/fulltext/images/6beb4b2825d9c7fa1925cfa238ca360e45b09f54526359219dd186f162f157b2.jpg)

![](/api/attachments/AGS42M8A/fulltext/images/26a2edbcc4070e03747eea3475af58553fd63bf7df04c28502df652930e5c248.jpg)

Figure 6 Scenarios with No Nash Equilibrium  
![](/api/attachments/AGS42M8A/fulltext/images/4e8422458a2a89626258993190a945b35901b102ae608b54e61d508a2da84b29.jpg)  
6(a) i has motivating incentive

When i is inefficient with a threatening incentive, Figure 6(b) shows that the intersection points of the two best response function are $X_{1} = (T_{1}^{l}, T_{j}^{l})$ and $X_{2} = (T_{i}^{l}, T_{j}^{l})$ . From Lemma 1 (b), i's best response is given as:

$$
\Phi_ {i} (T _ {j}) = T _ {i} ^ {l} \quad \text { for } T _ {j} \leq \tilde {T} _ {j}\tag{20}
$$

$$
= T _ {i} ^ {f} \quad \text { for } T _ {j} \geq \tilde {T} _ {j},\tag{21}
$$

and from Lemma 8,

$$
T _ {i} ^ {f} <   \tilde {T} _ {j} <   T _ {i} ^ {l}.\tag{22}
$$

From Equation (20), $X_{1} = (T_{i}^{l}, T_{j}^{f})$ implies that $T_{j}^{f} \leq \tilde{T}_{j}$ . Along with Equation (22), it implies that $T_{j}^{f} < T_{i}^{l}$ , which contradicts the definition of the leader and the follower.

By the same token, from Equation (21), $X_{2} = (T_{i}^{f}, T_{j}^{l})$ implies that $T_{j}^{l} \geq \tilde{T}_{j}$ . Along with Equation (22), this implies that $T_{j}^{l} > \tilde{T}_{j} > T_{i}^{f}$ . Therefore, $T_{j}^{l} > T_{i}^{f}$ , which also violates the leadership and followership definitions.

When $i$ is efficient (cases (iii) and (iv)), regardless of its incentive, its best response is $T_{i} = 0$ . Further, $j$ 's best response function (same as shown in Figures 6(a) and 6(b)) intersects $i$ 's best response function at $(0,T_{j}^{l})$ . However, since $T_{j}^{l}>0$ , this intersection (with $j$ as the leader) violates the definition of a leader and a follower. Thus, there is no equilibrium for cases (iii) and (iv). $\square$

![](/api/attachments/AGS42M8A/fulltext/images/f4a577be53b26c878df7ff84e02b6126cc7ca4b830ac597587dbf4a1beb24aff.jpg)

![](/api/attachments/AGS42M8A/fulltext/images/2d2f8ba5541824ac2669eeb6524f7e74125401c5fb4b2f048f2618ec1f2020d0.jpg)

PROOF OF PROPOSITION 2(a). When both suppliers $i$ and $j$ are ITinefficient and have motivating incentives at $t = 0$ , their optimal joining times are either $(T_{i}^{l}, T_{j}^{f})$ or $(T_{i}^{f}, T_{j}^{l})$ (refer to Table 2), where for $k = i$ or $j$ ,

$$
\begin{array}{r l} T _ {k} ^ {l} & = \frac {1}{\lambda_ {k} - \gamma} \ln \frac {\lambda_ {k} C _ {k} ^ {0}}{\pi_ {k} ^ {1} - \pi_ {k} ^ {0}} \\ & = \frac {1}{\lambda_ {k} - \gamma} \ln \left\{\frac {\lambda_ {k} C _ {k} ^ {0}}{\pi_ {k} ^ {0} (v _ {k} ^ {0} + \alpha_ {k} v _ {k} ^ {0}) + \epsilon_ {k} (v _ {k} ^ {0} + \alpha_ {k} v _ {k} ^ {0}) - \pi_ {k} ^ {0} (v _ {k} ^ {0})} \right\}, \end{array}\tag{23}
$$

$$
\begin{array}{r l} T _ {k} ^ {f} & = \frac {1}{\lambda_ {k} - \gamma} \ln \frac {\lambda_ {k} C _ {k} ^ {0}}{\pi_ {k} ^ {3} - \pi_ {k} ^ {2}} \\ & = \frac {1}{\lambda_ {k} - \gamma} \ln \left\{\frac {\lambda_ {k} C _ {k} ^ {0}}{\pi_ {k} ^ {0} (v _ {k} ^ {0}) + \epsilon_ {k} (v _ {k} ^ {0}) - \pi_ {k} ^ {0} (v _ {k} ^ {0} - \alpha_ {k} ^ {\prime} v _ {k} ^ {0})} \right\}. \end{array}\tag{24}
$$

Without the substitution policy of the manufacturer, $\alpha_{k}$ and $\alpha_{k}^{\prime}$ will be zero. Using this fact in Equations (23) and (24), supplier k will join the system at

$$
T _ {k} = \frac {1}{\lambda_ {k} - \gamma} \ln \frac {\lambda_ {k} C _ {k} ^ {0}}{\pi_ {k} ^ {0} (v _ {k} ^ {0})}.
$$

This is the optimal joining time of an IT-inefficient monopolist supplier. To see why, note that a monopolist supplier has a profit flow $\pi_{k}^{0}(v_{k}^{0})$ before joining EDI; after joining the network, the flow increases to $\pi_{k}^{0}(v_{k}^{0}) + \epsilon_{k}(v_{k}^{0})$ . Thus, the efficiency improvement is the only benefit that will accrue to the monopolist supplier from EDI. Therefore, the monopolist will join at a time when technological progress makes the marginal cost of joining equal to the marginal efficiency gains. ☐

PROOF OF PROPOSITION 2(b). Expanding on the log terms in Equations (23) and (24), we have

$$
\begin{array}{r} T _ {k} ^ {t} = \frac {1}{\lambda_ {k} - \gamma} \{\ln (\lambda_ {k} C _ {k} ^ {0}) - \ln (\pi_ {k} ^ {0} (v _ {k} ^ {0} + \alpha_ {k} v _ {k} ^ {0}) \\ + \epsilon_ {k} (v _ {k} ^ {0} + \alpha_ {k} v _ {k} ^ {0}) - \pi_ {k} ^ {0} (v _ {k} ^ {0})) \}, \end{array}\tag{25}
$$

$$
\begin{array}{l} T _ {k} ^ {f} = \frac {1}{\lambda_ {k} - \gamma} \left\{\ln (\lambda_ {k} C _ {k} ^ {0}) - \ln (\pi_ {k} ^ {0} (v _ {k} ^ {0}) \right. \\ \quad + \epsilon_ {k} (v _ {k} ^ {0}) - \pi_ {k} ^ {0} (v _ {k} ^ {0} - \alpha_ {k} ^ {\prime} v _ {k} ^ {0})) \}. \end{array}\tag{26}
$$

Note that the terms $\pi_{k}^{0}(v_{k}^{0} + \alpha_{k}v_{k}^{0})$ and $\epsilon_{k}(v_{k}^{0} + \alpha_{k}v_{k}^{0})$ denote the fact that the profit and efficiency flows $\pi_{k}^{0}$ and $\epsilon_{k}$ respectively are functions of the business volume $v_{k}^{0} + \alpha_{k}v_{k}^{0}$ . Differentiating the leadership and followership joining times in Equations (25) and (26) with respect to $\alpha_{k}$ and $\alpha_{k}^{\prime}$ respectively, we have

$$
\begin{array}{r l} & {\frac {\partial T _ {k} ^ {l}}{\partial \alpha_ {k}} = \frac {- 1}{(\lambda_ {k} - \gamma) (\pi_ {k} ^ {1} - \pi_ {k} ^ {0})} \left\{\frac {\partial \pi_ {k} ^ {0} (v _ {k} ^ {0} + \alpha_ {k} v _ {k} ^ {0})}{\partial \alpha_ {k}} + \frac {\partial \epsilon_ {k} ^ {0} (v _ {k} ^ {0} + \alpha_ {k} v _ {k} ^ {0})}{\partial \alpha_ {k}} \right\},} \\ & {\frac {\partial T _ {k} ^ {l}}{\partial \alpha_ {k} ^ {\prime}} = \frac {- 1}{(\lambda_ {k} - \gamma) (\pi_ {k} ^ {3} - \pi_ {k} ^ {2})} \left\{- \frac {\partial \pi_ {k} ^ {0} (v _ {k} ^ {0} - \alpha_ {k} ^ {\prime} v _ {k} ^ {0})}{\partial \alpha_ {k} ^ {\prime}} \right\},} \end{array}
$$

Since both $\partial\pi_{k}^{0}(v_{k}^{0}+\alpha_{k}v_{k}^{0})/\partial\alpha_{k}$ and $\partial\epsilon_{k}^{0}(v_{k}^{0}+\alpha_{k}v_{k}^{0})/\partial\alpha_{k}$ are positive, $\partial T_{k}^{l}/\partial\alpha_{k}$ is negative, implying that as a leader, supplier k joins earlier with an increase in its substitution gain factor.

Since $\partial \pi_k^0 (v_k^0 -\alpha_k'v_k^0) / \partial \alpha_k'$ is negative, $\partial T_k^f /\partial \alpha_k'$ is also negative. From §3.2, $\alpha_{k}^{\prime}v_{k}^{0}$ , the business volume lost by supplier $k$ , is equal to $\alpha_{k}v_{k}^{0}$ , the corresponding gain for its competitor, say $\tilde{k}$ . Since $\alpha_{k}^{\prime}$ is proportional to $\alpha_{k}$ (competitor $\tilde{k}$ 's substitution gain factor) for constant $v_{k}^{0}$ and $v_{k}^{0}$ , the sign on $\partial T_k^f /\partial \alpha_k$ is the same as the (negative) sign on $\partial T_k^f /\partial \alpha_k'$ . Therefore a follower joins earlier with an increase in the competitor's substitution gain factor. Also, since the slack capacities corresponding to substitution gain factors $\alpha_{k}$ and $\alpha_{k}$ are $\alpha_{k}v_{k}^{0}$ and $\alpha_{k}v_{k}^{0}$ respectively (where $v_{k}^{0}$ and $v_{k}^{0}$ are constant initial business volumes of the two suppliers at $t = 0$ ), we infer that both the leader and the follower join earlier with an increase in the leader's slack capacity.

PROOF OF PROPOSITION 3(a). If the profit function has zero or positive economies of scale, the first derivatives at two volumes $v_{1}$ and $v_{2}$ have the following relationship: $\pi_k^{0'}(v_1) \geq \pi_k^{0'}(v_2)$ if $v_{1} \geq v_{2}$ . Differentiating supplier $k$ 's leadership and followership joining times with respect to its business volume, and using the definitions of $\pi_k^0, \pi_k^1, \pi_k^2$ and $\pi_k^3$ from Appendix A.2, we have

$$
\begin{array}{r l} & {\frac {\partial T _ {k} ^ {l}}{\partial v _ {k} ^ {0}} = \frac {- 1}{(\lambda_ {k} - \gamma) (\pi_ {k} ^ {1} - \pi_ {k} ^ {0})} \{\pi_ {k} ^ {0 \prime} (v _ {k} ^ {0} + \alpha_ {k} v _ {k} ^ {0})} \\ & {\qquad + \epsilon_ {k} ^ {0 \prime} (v _ {k} ^ {0} + \alpha_ {k} v _ {k} ^ {0}) - \pi_ {k} ^ {0 \prime} (v _ {k} ^ {0}) \} \leq 0,} \\ & {\frac {\partial T _ {k} ^ {l}}{\partial v _ {k} ^ {0}} = \frac {- 1}{(\lambda_ {k} - \gamma) (\pi_ {k} ^ {3} - \pi_ {k} ^ {2})} \{\pi_ {k} ^ {0 \prime} (v _ {k} ^ {0}) + \epsilon_ {k} ^ {0 \prime} (v _ {k} ^ {0})} \\ & {\qquad - \pi_ {k} ^ {0 \prime} (v _ {k} ^ {0} - \alpha_ {k} ^ {\prime} v _ {k} ^ {0}) \} \leq 0.} \end{array}
$$

Thus, a supplier with larger business transactions joins the system earlier. Note that even if there are zero economies of scale, the results hold from the positive first derivative of the efficiency benefit with respect to volume. □

PROOF OF PROPOSITION 3(b). For a given business volume, both profit flow differences, $\pi_{k}^{1} - \pi_{k}^{0}$ and $\pi_{k}^{3} - \pi_{k}^{2}$ , increase with the degree of economies of scale. Thus, the impact of economies of scale on joining times (for given business volume) can be analyzed by differentiating the optimal leadership and followership joining times with respect to the profit flow differences:

$$
\begin{array}{l} \frac {\partial T _ {k} ^ {l}}{\partial (\pi_ {k} ^ {1} - \pi_ {k} ^ {0})} = \frac {- 1}{(\lambda_ {k} - \gamma) (\pi_ {k} ^ {1} - \pi_ {k} ^ {0})} \leq 0 \quad \text { and } \\ \frac {\partial T _ {k} ^ {l}}{\partial (\pi_ {k} ^ {3} - \pi_ {k} ^ {2})} = \frac {- 1}{(\lambda_ {k} - \gamma) (\pi_ {k} ^ {3} - \pi_ {k} ^ {2})} \leq 0, \end{array}
$$

since $\lambda_{k} > \lambda$ .

PROOF OF PROPOSITION 4. Let $V(X, P)$ be a function which denotes the value of $X$ for policy $P$ . Since policy $P3$ is the harshest, followed by $P2$ , and $P1$ , we have: $V(v_k^3, P1) \geq V(v_k^3, P2) \geq V(v_k^3, P3)$ . That is, the instantaneous restoration of business volume (policy $P1$ ) provides the maximum business volume to follower when it joins the network. Note that the restoration policy has no impact on $v_k^1$ and $v_k^2$ . Since $\pi_k^3$ depends only on $v_k^3$ , we have $V(\pi_k^3, P1) \geq V(\pi_k^3, P2) \geq V(\pi_k^3, P3)$ .

From Equation (12) in Lemma 3(b), as $\pi_k^3$ reduces with increasing severity of the manufacturer's restoration policy, the follower's joining time $T_{k}^{f}$ gets further delayed. Therefore, the manufacturer will be worse off, since business transactions through the EDI network contribute more to the manufacturer's benefits than paper based transactions.

PROOF OF PROPOSITION 5(a). From Lemma 1, the best response function of the efficient supplier $j$ is $\Phi_j(T_i) = 0$ for all $T_i$ . The incentive of firm $i$ was defined as $I_t = \pi_t^1 - \pi_t^0 + \pi_t^2 - \pi_t^3$ . Let $v_j^m$ represent the maximum slack capacity of firm $j$ ( $0 \leq v_j^m \leq v_t^0$ ). Since the profit and efficiency flow functions were assumed to be linear in volume, let $\pi_i^0(v) = p_i v$ and $\epsilon_i(v) = \epsilon_i v$ , where $p_i$ and $\epsilon_i$ are positive constants. For given constants, $p_i, \epsilon_i, v_i^0$ , and $v_j^0$ , the incentive of firm $i$ is given by:

$$
I _ {i} \left(\alpha_ {i}, v _ {j} ^ {m}\right) = \alpha_ {i} \left(p _ {i} + \epsilon_ {i}\right) v _ {i} ^ {0} - p _ {i} v _ {j} ^ {m},\tag{27}
$$

where $0 \leq \alpha_{i} \leq v_{j}^{0} / v_{i}^{0}$ . Let $\tilde{\alpha}(v_{j}^{m})$ be a substitution gain factor of firm $i$ for a given $v_{j}^{m}$ (i.e., the maximum slack capacity of $j$ ) such that

$$
I _ {i} (\bar {\alpha} (v _ {j} ^ {m}), v _ {j} ^ {m}) = 0.\tag{28}
$$

Therefore, for a given $v_{j}^{m}$ , if $\alpha_{i} > \alpha(v_{j}^{m})$ , then $I_{i}(\alpha_{i}, v_{j}^{m}) > 0$ (i.e., firm i has a “motivating” incentive). If $\alpha_{i} < \alpha(v_{j}^{m})$ , then $I_{i}(\alpha_{i}, v_{j}^{m}) < 0$ (i.e., firm i has a “threatening” incentive). Thus, we get a linear function of $v_{j}^{m}$ :

$$
\bar {\alpha} (v _ {j} ^ {m}) = \frac {p _ {i} v _ {j} ^ {m}}{(p _ {i} + \epsilon_ {i}) v _ {i} ^ {0}}.\tag{29}
$$

PROOF OF PROPOSITION 5(b). In order to assess the impact of $j$ 's slack capacity on a competitor with a motivating incentive, we choose a constant capacity $\bar{v}_j$ , such that

$$
\bar {v} _ {j} = \frac {1}{p _ {i}} (\lambda_ {i} C _ {i} ^ {0} - \epsilon_ {i} v _ {i} ^ {0}).\tag{30}
$$

When the slack capacity of the efficient supplier $j$ , $v_{j}^{m}$ , is $\geq \bar{v}_{j}$ , the followership IT-efficiency ratio of the supplier $i$ , $r_{i}^{f} = (p, v_{j}^{m} + \epsilon_{i} v_{i}^{0}) / \lambda_{i} C_{i}^{0} \geq 1$ , i.e., the proposed system promises positive net profit. The leadership efficiency is also greater than 1 (because of the motivating incentive). Therefore, supplier $i$ will join the system at time 0. Similarly, consider the case where firm $j$ does not have "sufficient" slack capacity. For area 1 in Figure 2d, $r_{i}^{f} < 1$ (i.e., $i$ is inefficient), and firm $i$ will not join the system at time 0. The Nash equilibrium is given by $(T_{i}^{\mathrm{N}}, T_{j}^{\mathrm{N}}) = (T_{i}^{f}, 0)$ .

PROOF OF PROPOSITION 5(c). With a threatening incentive, let $\tilde{\alpha}_{i}$ be a substitution gain factor satisfying

$$
\tilde {\alpha} _ {i} = \frac {\lambda_ {i} C _ {i} ^ {0} - \epsilon_ {i} v _ {i} ^ {0}}{(p _ {i} + \epsilon_ {i}) v _ {i} ^ {0}}\tag{31}
$$

When $\alpha_{i} \geq \tilde{\alpha}_{i}$ , the leadership IT efficiency ratio, $r_{i}^{l} = (p_{i} + \epsilon_{i})v_{i}^{0}\alpha_{i} + \epsilon_{i}v_{i}^{0}) / \lambda_{i}C_{i}^{0} \geq 1$ . The followership ratio is also greater than 1 due to the threatening incentive. Thus, supplier $i$ will join the system at time 0. When the substitution factor is below the threshold, the leadership efficiency is less than 1 (i.e., $i$ is inefficient) and supplier $i$ will not join the system.

PROOF OF PROPOSITION 6. For the case of motivating incentive, let $\mathcal{B}(\theta)$ denote the manufacturer's benefit from subsidizing, and let $\mathcal{S}(\theta)$ be the cost of subsidizing level $\theta$ . In addition, let $v_{i}^{a} = \alpha_{i}v_{i}^{0}$ be the slack capacity of supplier $i$ . Unless $i$ has sufficient slack capacity to substitute whole business volume of its competitor $j$ , the manufacturer's decision problem can be formulated as follows: $^{13}$

$\mathcal{B}(\theta) =$

$$
\left\{ \begin{array}{l} \int_ {T _ {j} ^ {f} (\theta)} ^ {T _ {j} ^ {f}} a (v _ {j} ^ {0} - v _ {t} ^ {a}) e ^ {- \gamma t} d t = \frac {1}{\gamma} a (v _ {j} ^ {0} - v _ {t} ^ {a}) e ^ {- \gamma T _ {j} ^ {f}} \{(1 - \theta) ^ {- \gamma / (\lambda_ {j} - \gamma)} - 1 \} \\ \text {for} 0 \leq \theta \leq \bar {\theta}, \\ \int_ {0} ^ {T _ {i} ^ {f}} a (v _ {j} ^ {0} - v _ {t} ^ {a}) e ^ {- \gamma t} d t = \frac {1}{\gamma} a (v _ {j} ^ {0} - v _ {t} ^ {a}) (1 - (r _ {j} ^ {f}) ^ {\gamma / (\gamma_ {j} - \gamma)}) \quad \text {for} \theta > \bar {\theta}, \end{array} \right.\tag{32}
$$

$^{13}$ If i has sufficient capacity to absorb all of j's business, the manufacturer provides no subsidy to j.

$$
\mathscr {S} (\theta) = \theta C _ {j} (T _ {j} ^ {f} (\theta)) = C _ {j} ^ {0} e ^ {\lambda_ {j} T _ {j} ^ {l}} \theta (1 - \theta) ^ {- \lambda_ {j} / (\gamma_ {j} - \gamma)} \quad \text { for } 0 \leq \theta \leq \bar {\theta}.\tag{33}
$$

Note that the benefit function $\mathcal{B}(\theta)$ has its maximum at $\theta \geq \bar{\theta}$ and does not improve for $\theta >\bar{\theta}$ , and that $\mathcal{S}(\theta)$ is an increasing function of $\theta$ . Thus, the manufacturer's optimal subsidizing decision can be stated as

$$
\theta^ {*} = \arg \max _ {\theta \in [ 0, \bar {\theta} ]} (\mathcal {R} (\theta) - \mathcal {S} (\theta)).
$$

Let $\mathcal{P}(\theta) = \mathcal{B}(\theta) - \mathcal{S}(\theta)$ . Then, for $0 \leq \theta \leq \bar{\theta}$ , the first order condition (after arranging terms) is obtained as

$$
\frac {1}{\gamma} a \left(v _ {j} ^ {0} - v _ {i} ^ {a}\right) e ^ {- \lambda T _ {j} ^ {c}} \frac {\gamma}{\lambda_ {j} - \gamma} = C _ {j} ^ {0} e ^ {- \lambda_ {j} T _ {j} ^ {c}} + \frac {\theta}{1 - \theta} \frac {\lambda_ {j}}{\lambda_ {j} - \gamma} C _ {j} ^ {0} e ^ {- \lambda_ {j} T _ {j} ^ {c}}.\tag{34}
$$

From the first order condition, we obtain a unique solution for the optimal subsidy, $\tilde{\theta}$ :

$$
\tilde {\theta} = 1 - \frac {C _ {j} ^ {0} \lambda}{a (v _ {j} ^ {0} - v _ {i} ^ {a}) e ^ {(A _ {j} - \gamma) T _ {j} ^ {t}} + C _ {j} ^ {0} \gamma} = 1 - r (\text { say }).\tag{35}
$$

Further, the second derivative of $\mathcal{P}(\theta)$ at $\tilde{\theta}$ is given (after simplification) by

$$
\begin{array}{r l} (1 - \tilde {\theta}) ^ {- \lambda_ {j} / (\lambda_ {j} - \gamma) - 1} \frac {\lambda_ {j}}{\lambda_ {j} - \gamma} \bigg [ \frac {\tilde {\theta}}{1 - \tilde {\theta}} \frac {\lambda_ {j}}{\lambda_ {j} - \gamma} C _ {j} ^ {0} e ^ {- \lambda_ {j} T _ {j} ^ {t}} \\ & - \frac {\tilde {\theta}}{1 - \tilde {\theta}} \Big (\frac {\lambda_ {j}}{\lambda_ {j} - \gamma} + 1 \Big) C _ {j} ^ {0} e ^ {- \lambda_ {j} T _ {j} ^ {t}} \bigg ] \\ = & - (1 - \tilde {\theta}) ^ {- \lambda_ {j} / (\lambda_ {j} - \gamma) - 1} \frac {\lambda_ {j}}{\lambda_ {j} - \gamma} \frac {\tilde {\theta}}{1 - \tilde {\theta}} C _ {j} ^ {0} e ^ {- \lambda_ {j} T _ {j} ^ {t}} <   0. \end{array}
$$

From Equation (35), $\tilde{\theta} < 1$ . From Equations (35) and (10), $\tilde{\theta} > \bar{\theta}$ if $r_{j}^{f} > r$ for firm j with a motivating incentive. In that case, the manufacturer will provide the subsidy level $\bar{\theta}$ . Otherwise, $\tilde{\theta}$ is the optimal solution for manufacturer's decision. Therefore,

$$
\theta^ {*} = \min (\tilde {\theta}, \bar {\theta}).\tag{36}
$$

If the follower has a threatening incentive and is inefficient (which is why the manufacturer considers a subsidy), it does not join the system (i.e., $T_{j}^{f} = \infty$ ). Note that in the absence of a Nash equilibrium, the efficient supplier i does not join the system either in this Nash framework. Also, unless the manufacturer provides the maximum subsidy $\bar{\theta}$ (as shown in Equation (10)), which makes j efficient, it will not join the system. Therefore, the manufacturer's benefit from inducing a supplier who will not join the system into doing so immediately is obtained as

$$
\mathcal {B} (\bar {\theta}) = \int_ {0} ^ {\infty} a (v _ {j} ^ {0} + v _ {i} ^ {0}) e ^ {- \gamma t} d t = \frac {1}{\gamma} a (v _ {j} ^ {0} + v _ {i} ^ {0}).\tag{37}
$$

Thus, the manufacturer will provide a subsidy only when its benefit, $1/\gamma a(v_{j}^{0} + v_{i}^{0})$ , exceeds its subsidy cost, $\bar{\theta}C_{j}(0)$ . Since a subsidy level below $\bar{\theta}$ keeps the supplier inefficient, and fails to induce joining, the manufacturer's strategy is either to subsidize $\bar{\theta}$ (when the benefit exceeds the cost as shown above), or not to subsidize at all. ☐

PROOF OF PROPOSITION 7. From Equations (11) and (12),

$$
T _ {j} ^ {l} (\theta) = \left\{ \begin{array}{l l} T _ {j} ^ {l} + \frac {1}{\lambda_ {j} - \gamma} \ln (1 - \theta), & \text { where } 0 \leq \theta <   \bar {\theta}, \\ 0, & \text { where } \bar {\theta} \leq \theta \leq 1. \end{array} \right.\tag{38}
$$

$$
T _ {j} ^ {f} (\theta) = \left\{ \begin{array}{l l} T _ {j} ^ {f} + \frac {1}{\lambda_ {j} - \gamma} \ln (1 - \theta), & \text { where } 0 \leq \theta <   \bar {\theta}, \\ 0, & \text { where } \bar {\theta} \leq \theta \leq 1. \end{array} \right.\tag{39}
$$

Then, the best response function for firm j with a subsidy $\theta$ is

$$
\Phi_ {j} (\theta) = \left\{ \begin{array}{l l} \Phi_ {j} + \frac {1}{\lambda_ {j} - \gamma} \ln (1 - \theta), & \text { where } 0 \leq \theta <   \bar {\theta} \\ 0, & \text { where } \bar {\theta} \leq \theta \leq 1. \end{array} \right.\tag{40}
$$

Thus, the subsidy only serves to shift the best response function of the subsidized supplier, and does not affect its competitor's best response function. □

PROOF OF PROPOSITION 8. If the manufacturer subsidizes the leader (say i), the resulting benefits and costs are given by

$$
\begin{array}{r l} \mathcal {B} _ {t} (\theta_ {t}) & = \int_ {T _ {t} (\theta_ {t})} ^ {T _ {t} ^ {t}} a (v _ {t} ^ {0} + v _ {t} ^ {s}) e ^ {- \gamma t} d t \\ & = \frac {1}{\gamma} a (v _ {t} ^ {0} + v _ {t} ^ {s}) e ^ {- \gamma T _ {t} ^ {t}} \{(1 - \theta_ {t}) ^ {- \gamma / (\lambda_ {t} - \gamma)} - 1 \}, \\ \mathcal {S} _ {t} (\theta_ {t}) & = \theta_ {t} C _ {t} (T _ {t} (\theta_ {t})) = \theta_ {t} C _ {t} ^ {0} e ^ {- \lambda_ {t} (T _ {t} ^ {t} + (1 / (\lambda_ {t} - \gamma)) \ln (1 - \theta_ {t}))} \\ & = C _ {t} ^ {0} e ^ {- \lambda_ {t} T _ {t} ^ {t}} \theta_ {t} (1 - \theta_ {t}) ^ {- \lambda_ {t} / (\lambda_ {t} - \gamma)}. \end{array}
$$

If the manufacturer shares the setup cost of the follower, it gains $\mathcal{B}_{j}(\theta_{j})$ with an investment of $\mathcal{S}_{j}(\theta_{j})$ , as defined in Equations (32) and (33). Let

$$
\begin{array}{l} \mathcal {P} _ {i} (\theta_ {i}) = \mathcal {B} _ {i} (\theta_ {i}) - \mathcal {S} _ {i} (\theta_ {i}), \\ \mathcal {P} _ {j} (\theta_ {j}) = \mathcal {B} _ {j} (\theta_ {j}) - \mathcal {S} _ {j} (\theta_ {j}). \end{array}
$$

$\mathcal{P}_j(\theta_j)$ decreases over $v_{i}^{s}$ , while $\mathcal{P}_i(\theta_i)$ increases over $v_{i}^{s}$ .

## References

Bakos, J. Y. and E. Brynjolfsson, "Information Technology, Incentives and the Optimal Number of Suppliers," J. MIS, 10, 2 (1993), 37–53.

—, Interorganizational Information Systems: Strategic Implications for Competition and Cooperation, Ph.D. Thesis, Sloan School of Management, MIT, Cambridge, MA, 1987.

— and M. E. Treacy, "Information Technology and Corporate Strategy: A Research Perspective," MIS Quarterly, 10, 2(1986), 107–119.

Barua, A., C. H. Kriebel, and T. Mukhopadhyay, "An Economic Analysis of the Strategic Impacts of Information Technology Investments," MIS Quarterly, 15, 3(1991), 313–331.

Bonney, J., "Plunging Deeper into EDI," American Shipper, March (1994).

Cash, J. I., and B. R. Konsynski, "IS Redraws Competitive Boundaries," Harvard Business Rev. March (1985), 134–142.

Chismar, W. G., and J. Meier, "A Model of Competing Interorganizational Systems and its Application to Airline Reservation Systems," Decision Support Systems, 8, 5(1992), 447–458.

Clemons, E. K. and F. W. McFarlan, "Telecom: Hook Up or Lose Out," Harvard Business Rev. July (1986), 91–94.

— and S. O. Kimbrough, "Information Systems, Telecommunications and Their Effects on Industrial Organization," Proc. Seventh International Conf. on Information Systems, December (1986), 98–108.

— and —, "Information Systems and Business Strategy: A Review of Strategic Necessity," Working Paper, The Wharton School, Philadelphia, PA, 1987.

— and M. C. Row, "McKesson Drug Company: A Case Study of Economost," J. MIS, 5, 1(1988), 36–50.

— and P. Kleindorfer, "An Economic Analysis of Interorganizational Information Technology," Decision Support Systems, 8, 5(1992) 431–446.

——, S. Reddi, and M. Row, "The Impact of Information Technology on the Organization of Economic Activity: The Move to the Middle Hypothesis," J. MIS, 10, 2(1993), 9–35.

Hart, O. and J. Moore, "Property Rights and the Nature of the Firm," J. Political Economy, 98, 6(1990), 1119–1158.

Hwang, K. T., C. C. Pegels, H. R. Rao, and V. Sethi, "Electronic Data Interchange Systems—State of the Art," J. Systems Management, 44, 12 (1993).

Ives, B. and G. P. Learmonth, "The Information System as A Competitive Weapon," Comm. ACM, 27, 12 (1984).

Johnston, H. and M. Vitale, "Creating Competitive Advantage with Interorganizational Information Systems," MIS Quarterly, 12(1988), 153–165.

Katz, M. L. and C. Shapiro, "Network Externalities, Competition, and Compatibility," American Economic Rev., 75, 3(1985), 424–440.

— and —, "Technology Adoption in the Presence of Network Externalities," J. Political Economy, 94, 4(1986), 424–440.

— and —, "R&D Rivalry with Licensing or Imitation," American Economic Rev., 77, 3(1987), 402–420.

Major, M. J., "Two Sides to Every Story," MIDRANGE Systems, July 27, 1993.

Meier, J. and W. G. Chismar, "A Formal Model of the Integration of a Vertical EDI System," in Proc. 24th Hawaii International Conf. on System Sciences, vol. 4, 1991.

Nault, B. R., "Quality Differentiation and Adoption Costs: The Case for Interorganizational Information System Pricing," Working Paper, University of Alberta, Canada, 1993.

— and A. S. Dexter, "Adoption, Transfers, and Incentives in a Franchise Network with Positive Externalities," Marketing Sci., 13, 4(1994), 412–423.

Newburger, B., "Agents and EDI: Threat or Opportunity?" Agency Sales Magazine, March 1993.

Reinganum, J. F., "On the Diffusion of New Technology: A Game Theoretic Approach," Rev. Economic Studies, 48(1981a), 395–405.

——, "Dynamic Games of Innovation," J. Economic Theory, 25(1981b), 21–24.

——, "A Dynamic Game of R and D: Patent Protection and Competitive Behavior," Econometrica, 50(1982), 671–688.

Riggins, F., C. H. Kriebel, and T. Mukhopadhyay, "A Model of

Network Externalities with Competing Participants," Working Paper, Carnegie Mellon University, Pittsburgh, PA, 1989.

——, ——, and ——, "Dynamic Properties of Network Externalities with Competing Participants," Working Paper, Carnegie Mellon University, Pittsburgh, PA, 1990.

Seidmann, A. and E. Wang, "Electronic Data Interchange:

Competitive Externalities and Strategic Implementation Policies," Management Sci. 41, 3 (1995), 401–418.

Taylor, P., "Electronic Data Interchange and Electronic Mail," Financial Times, October 26, 1993.

Whang, S. "An Analysis of Inter-organizational Information Sharing," J. Organizational Computing, 3, 3 (1993), 257–277.

Seungjin Whang, Associate Editor. This paper was received on May 6, 1993, and has been with the authors 16 months for 2 revisions.
