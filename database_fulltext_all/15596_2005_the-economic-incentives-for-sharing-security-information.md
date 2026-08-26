---
otero_id: 15596
otero_key: "FWEJ39DG"
title: "The Economic Incentives for Sharing Security Information"
authors: "Esther Gal-Or; Anindya Ghose"
year: "2005"
journal: "Information Systems Research"
doi: "10.1287/isre.1050.0053"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Economic Incentives for Sharing Security Information

Esther Gal-Or

Katz Graduate School of Business, 368 A Mervis Hall, University of Pittsburgh, Pittsburgh, Pennsylvania 15260, esther@katz.pitt.edu

Anindya Ghose

Leonard Stern School of Business, New York University, New York, New York 10012, aghose@stern.nyu.edu

iven that information technology (IT) security has emerged as an important issue in the last few years, the Gsubject of security information sharing among firms, as a tool to minimize security breaches, has gained the interest of practitioners and academics. To promote the disclosure and sharing of cyber security information among firms, the U.S. federal government has encouraged the establishment of many industry-based Informa tion Sharing and Analysis Centers (ISACs) under Presidential Decision Directive (PDD) 63. Sharing security vulnerabilities and technological solutions related to methods for preventing, detecting, and correcting security breaches is the fundamental goal of the ISACs. However, there are a number of interesting economic issues that will affect the achievement of this goal. Using game theory, we develop an analytical framework to investigate the competitive implications of sharing security information and investments in security technologies. We find that security technology investments and security information sharing act as “strategic complements” in equi librium. Our results suggest that information sharing is more valuable when product substitutability is higher, implying that such sharing alliances yield greater benefits in more competitive industries. We also highlight tha the benefits from such information-sharing alliances increase with the size of the firm. We compare the levels of information sharing and technology investments obtained when firms behave independently (Bertrand-Nash) to those selected by an ISAC, which maximizes social welfare or joint industry profits. Our results help us predic the consequences of establishing organizations such as ISACs, Computer Emergency Response Team (CERT), or InfraGard by the federal government.

Key words: security technology investment; information sharing; security breaches; externality benefit; social welfare; spillover effect

History: C. Kemerer and V. Sambamurthy, Senior Editors; M. Van Alstyne, Associate Editor. This paper was received on August 29, 2003, and was with the authors 5 <sup>1</sup> months for 4 revisions.

## 1. Introduction

The increasing ubiquity of the Internet provides cyber attackers more opportunities to misappropriate or corrupt an organization’s data resources. According to Jupiter Media Metrix, computer security breaches could potentially cost e-businesses almost \$25 billion by 2006—up from \$5.5 billion in 2001.<sup>1</sup> There are many well-known examples of cyber hacking. Egghead.com faced a massive backlash from its customers after being hacked in 2000, which contributed to its eventual bankruptcy filing. A security breach at Travelocity in 2001 exposed the personal information of thousands of customers who had participated in a promotion. Established firms like Citibank, Microsoft, and NASA, among others have been targeted too. Hence both the federal government and the private sector have recognized a strong need to improve their cyber security and to treat the security of critical infrastructure assets like a strategic initiative, rather than a compliance burden.

For awhile now, it has been recognized that a key factor required to improve computer security is the gathering, analysis, and sharing of information related to successful, as well as unsuccessful, attempts at computer security breaches. This has led the U.S. federal government to encourage the establishment of industry-based Information Sharing and Analysis

Centers (ISACs) under PDD 63.<sup>2</sup> Further, in February 2003, the President also issued The National Strategy to Secure Cyberspace. ISACs are meant to facilitate the sharing of security information to enhance and protect critical cyber infrastructure. In January 2001, 19 of the nation’s leading high-tech companies announced the formation of a new Information Technology Information Sharing and Analysis Center (IT-ISAC) to cooperate on cyber security issues in the private sector. Using the shared information, the IT-ISAC disseminates an integrated view of relevant information system vulnerabilities, threats, and incidents to its members. It also shares the best security practices and solutions among its members, and thus provides an impetus for continuous improvement in the effectiveness of security products.<sup>3</sup> Obviously, such mutual collaboration is intended to increase the technological effectiveness of IT security products, thereby increasing their demand.

Revealing information about security breaches to an information-sharing alliance (ISA) results in both costs and benefits for the revealing firm. Losses can occur when a competing firm or a third party hacks the database of the ISA itself and leverages the shared information to make competitive gains. Further, it could malign the reputation of the breachrevealing firm, by anonymously reporting it to the public. In January 2003, Next Generation Software Services (NGSS) claimed that Computer Emergency Response Team (CERT), the government-sponsored Internet security reporting center, passed vulnerability information to third parties about which NGSS had notified CERT. NGSS felt that this was a direct violation of trust, because the information was leaked to potential competitors of NGSS. Eventually, NGSS severed ties with CERT.<sup>4</sup> Another recent incident involved leakage of information on a fatal flaw in a Sun Microsystems Internet software package to a public mailing list. The hacker intercepted the documents from CERT and posted an advisory containing the bug’s specifics to the full disclosure security mailing list.<sup>5</sup>

The potential costs of sharing security information can have a snowball effect, accruing from the resultant loss of market share and stock market value from negative publicity (Cavusoglu et al. 2004, Campbell et al. 2003). In a 2002 report by Jupiter Media Metrix, IT executives revealed that they were more concerned with the ripple effects of online security breaches on consumer confidence and trust in e-business than the actual financial losses of physical infrastructure. Negative exposure and loss of reputation as a result of reports of information infrastructure violations could be a threat to consumer confidence in a firm’s products. Diminished customer confidence and a tarnished reputation can lead to reduced revenues at an increasing rate.

However, there are several positive aspects to sharing security information. Formally, the benefit from mutual sharing of actual or attempted security breach information can be partitioned into a private firmspecific benefit and an external industry-level benefit. This private benefit includes both the prevention of further security breaches in the future (e.g., identifying and repairing vulnerabilities in their information security systems) as well as increased sales resulting from more effective security products and better security reputation among consumers.<sup>6</sup> Schechter and Smith (2003) show that information sharing by firms can act as a deterrent for hackers, thereby indirectly increasing the effectiveness of security technologies.

One reason for entering information security alliances is cost reduction by minimizing security breaches. In fact, in many cases, this might be the main motive for forming the alliance. However, there exist strong arguments for indirect, demand-side benefits as well. In business-to-business markets, firms that join an ISAC often have big corporations as customers. For instance, in the IT-ISAC, the customers of security vendors like Symantec and Computer Associates include big corporations like Procter & Gamble, Lockheed Martin, and Citibank, among others. As customers perceive improvement in the effectiveness of cyber security products—accruing from the information-sharing behavior of security vendors (which members of the IT-ISAC)—their overall confidence increases, leading to increased demand for IT security products. Hence security technology investments and security information sharing can involve demand-side spillovers, which result in positive externalities for the industry as a whole. One of the main purposes of this paper is to focus on such demandenhancing benefits of security information-sharing alliances, while still keeping in mind the importance of cost side benefits.

## 1.1. Research Questions and Results

For any organization focused on the reporting and dissemination of information related to security breaches, there are a number of interesting economic issues that will affect its behavior. We seek to address the following questions in this paper. (i) What are the economic incentives for competing firms in a given industry to share security information through an information-sharing organization like an ISA? (ii) How do market characteristics such as the degree of intraindustry competitiveness, firm size, and mode of conduct impact such sharing behavior among competing firms? (iii) Do spillover effects on demand side or cost side discourage firms from sharing security information and result in suboptimal levels of security technology investment? (iv) What is the impact of such sharing alliances on social welfare when firms individually engage in profit maximization, when the ISA dons the role of a social planner, and when it acts as a joint profit maximizer?

We find that security information sharing and security technology investments can act as “strategic complements” in that an increase in information sharing or technology investments by one firm will induce the other firm to increase its own level of information sharing or technology investments. In fact, this inclination to share information and invest in security technologies increases as the degree of competitiveness in an industry increases. The extent of information sharing and investment levels of firms introduce two effects in our model: (i) a “direct effect” of expanding demand in the product market and (ii) a “strategic effect” of alleviating price competition among suppliers of competing products. We demonstrate that these two effects increase with the size of the firm. We extend our model to show that the nature of security technology cost plays a pivotal role in determining whether cost-based spillovers boost information sharing or subdue it. In particular, the incentives for sharing and investment are weakened if sales volume-related cost spillovers are present, in comparison to spillovers on fixed costs. We further show that information-sharing levels and technology investments are higher when firms join an ISA sequentially than when firms compete simultaneously. This happens because of the tacit collusion that is induced by the first entrant’s precommitment to share a given level of security information and invest a given amount in security technology. This leads to higher profits for both firms. Finally, we point out that if a federally funded ISA were to don a social planner’s role, it would need to provide higher incentives for firms to share welfare-maximizing levels of security information, rather than the individual or joint profit-maximizing levels. In Appendix B, we also allude to an incentive mechanism designed by the government for fostering socially optimal levels of disclosure.

## 1.2. Prior Literature

Questions on information sharing, economic incentives, and social welfare, similar to those noted above, have been previously studied in the context of other organizations. Of particular relevance is the extensive literature on trade associations (TAs). Previous relevant work includes that on information sharing (e.g., Gal-Or 1985a, Shapiro 1986, Vives 1990).<sup>7</sup> The second stream of literature relevant to our work is that on mode of conduct and strategic effects (Bulow et al. 1985, Gal-Or 1985b). More recently, Parker and

Van Alstyne (2001) show how free strategic complements can raise a firm’s own profits. Of course, because an organization must expend resources to develop technology, methods, and procedures to deal with information security breaches, sharing of this information will be qualitatively different than sharing the type of information modeled in the TA literature.<sup>8</sup> Finally, our model considers spillovers from security technology investments. Spillovers have been addressed in the extensive economics-based literature on research joint ventures (d’Aspremont and Jacquemin 1988, Kamien et al. 1992).

Recent papers dealing with the economics of information security and protection of critical infrastructure include Anderson (2001) who discusses various distorted incentives in the information security domain implied by the existence of moral hazard and adverse selection problems. Gordon and Loeb (2002) present a framework to determine the optimal amount of investment to protect a given set of information and Gordon et al. (2003) discuss the importance of security information sharing. The focus of Gordon et al. (2003) is on how information sharing affects the overall level of information security. They highlight the trade-off that firms face between improved information security and the potential for free riding, which can lead to underinvestment in security expenditures. While Gordon et al. (2003) focus on the cost side effects of security breaches and information sharing, our paper focuses on the demand side effects. In particular, we highlight the strategic implication of competition in the product market on information sharing- and security technology investment levels.<sup>9</sup> As we proceed through this paper, we clearly identify how our results are related to Gordon et al. (2003) wherever relevant.

The rest of this paper is organized as follows. Section 2 describes the model in detail and presents the main results under simultaneous competition (Bertrand-Nash) mode. We contrast these with a social planner’s level of information sharing and technology investments. In §3, we analyze the equilibrium under a sequential mode of entry. Section 4 considers the scenario when technology costs are influenced by the volume of sales. We conclude with some implications in §5. All proofs are relegated to Appendix A.

## 2. Model

We consider a market consisting of two firms producing a differentiated product in a two-stage noncooperative game. In the first stage, firms i and j simultaneously choose optimal levels of security technology investment, which we denote as $( t _ { i } , t _ { j } )$ and security information-sharing levels, which we denote as $( s _ { i } , s _ { j } )$ . In the second stage, they choose prices $( p _ { i } , p _ { j } )$ simultaneously. We consider a subgameperfect equilibrium of this game using backward induction. In this paper, we interchangeably use the words Bertrand-Nash and simultaneous, to denote this mode of firm conduct.<sup>10</sup>

We normalize the amount of security information being shared so that it always lies between 0 and 1, i.e., $s _ { i } \in [ 0 , 1 ]$ . If $s _ { i } = 0$ , no information is shared; if $s _ { i } = 1 ,$ , all information is shared. The variable $t _ { i }$ is an aggregate measure of the extent of investment in security technology. Because such investment entails allocating resources to possibly multiple technologies measured in terms of different physical units, we measure $t _ { i }$ in terms of one selected technology as a numeraire.

We assume that the cost of investing in improved security technology depends on the firm’s own investment level as well as the level of security chosen by the competitor and the extent to which the competitor is willing to share information about its vulnerabilities. Essentially, the intuition is that the disclosure of vulnerabilities in a particular type of security technology by one firm leads the other firm to invest less in that technology or procure a smaller amount of that product. For instance, if firm i were to report a higher number of security breaches because of a particular kind of firewall, firm j would invest less in that specific technology. A direct consequence of such information sharing would be preemptive cost savings in technology investment.<sup>11</sup>

Incorporating the existence of positive cost spillovers, we specify the costs of investing in security technology in terms of the function $f ^ { i } ( t _ { i } , y _ { j } )$ where $y _ { j } = \lambda _ { c } t _ { j } s _ { j } , \ \partial f ^ { i } / \partial t _ { i } > 0 .$ , and $\partial f ^ { i } / \partial y _ { j } < 0 .$ . Hence each firm’s costs rise with its own aggregate investment, but decline with the competitor’s aggregate investment and its willingness to share information. The coefficient $\lambda _ { c }$ is a cost spillover parameter that we normalize to be in the unit interval. (Gordon et al. 2003 use a similar formulation.) We also assume that $\partial f ^ { i } ( 0 , y _ { i } ) / \partial t _ { i } = 0 , \ \partial ^ { 2 } f ^ { i } / \partial t _ { i } \partial y _ { j } < 0 ,$ and $\partial ^ { 2 } f ^ { i } / \partial t _ { i } ^ { 2 } > 0$ That is, the marginal cost of increased security investment is zero when no such investment is made. The marginal cost is decreasing when the competitor increases its investment in security technologies or shares more information about its security vulnerabilities, and this marginal cost is increasing with the firm’s own investment level.<sup>12</sup> For simplicity, we assume that firms’ do not incur any production costs other than those stemming from investments in improved security technology.

We assume that the demand facing each product is linear in self and cross-price effects (see McGuire and Staelin 1983).

$$
q _ {i} = a _ {i} - b _ {1} p _ {i} + b _ {2} p _ {j} + B _ {i} \quad i, j = 1, 2; i \neq j,\tag{1}
$$

where $0 \leq b _ { 2 } < b _ { 1 }$ . From this point onward, we will continue to designate the firm under consideration as firm i and its competitor as firm $j .$ As well, in describing the behavior of both firms in terms of a system of equations, as expressed in (1), we will drop the qualification, $i , j = 1 , 2 ; i \neq j$ for brevity.

The variable $a _ { i }$ in (1) is the initial intercept of demand facing i. This intercept may shift upward because of the firms’ investments in improving security as well as sharing information about their vulnerabilities. The variable $B _ { i }$ in (1) measures the potential shift of the demand intercept facing firm i. We describe it in detail subsequently in Equation (3). The slope $b _ { 1 }$ can be interpreted as the extent to which consumers are price sensitive or “disloyal” to a firm’s product, and the slope $b _ { 2 }$ provides a measure of the degree of product substitutability. Thus, $b _ { 2 } = 0$ implies that firms act as local monopolists, whereas $b _ { 1 } = b _ { 2 }$ corresponds to the case when products are perfectly homogenous.

In Appendix A, we demonstrate that the linear demand model is implied by a quadratic, and separable of income, utility function. When consumers decide upon the consumption of two products,<sup>13</sup> subject to their budget constraints, the above linear demand is implied. The linear demand model has been used extensively in marketing and economics, and there is some research suggesting that comparative statics derived from simpler models may often hold for more general formulations (Milgrom 1994).

We now proceed to explain how the variable $B _ { i } ,$ which measures the potential shift of the demand intercept of i, depends upon the investments in security and the extent of information sharing by the firms. We start by evaluating the possible consequences of firms’ decisions to share information about their security breaches. We designate the “leakage costs” that might be inflicted on firm i as a result of such sharing by $g ^ { i } ( s _ { i } , s _ { j } )$ . Hence the level of these costs to firm i depends on whether or not firm $j \neq i$ has also revealed information about its security breaches to the ISA. This specification is similar to the loss function $L _ { i }$ assumed in Gordon et al. (2003), which measures the cost of a security breach incurred by firm i, including, in particular, the value of profits lost from sales. In our formulation though, those losses are a function of the extent of sharing by the firms instead of being a fixed amount.

We assume that $g ^ { i } ( s _ { i } , s _ { j } )$ is increasing in $s _ { i }$ but decreasing in $s _ { j } .$ As the extent of sharing by i increases, it is more likely that there could be a leakage of the security breach information that this firm has experienced. This, in turn, would increase consumers’ apprehension of transacting with this firm, and thereby reduce its demand intercept. However, as the competitor’s sharing level increases as well, some consumers may find it optimal to switch from firm $j$ to firm $i ,$ given that $j ^ { \prime } \mathbf { s }$ security breaches are more likely to be revealed. We assume that the rate at which these leakage costs increase in $s _ { i }$ and decrease in $s _ { j }$ is increasing. Specifically, $\partial ^ { 2 } g ^ { i } / \partial s _ { i } ^ { 2 } > 0$ and $\partial ^ { 2 } g ^ { i } / \partial s _ { j } ^ { 2 } <$ 0. This assumption is consistent with the possible deleterious ripple effects of a security breach information leak on firms’ own market share, as cited in the Introduction. We also assume that $\partial ^ { 2 } g _ { i } / \partial s _ { i } \partial s _ { j } \leq$ $0 ,$ implying that intensified sharing by the competitor reduces the marginal leakage cost incurred by the firm.<sup>14</sup>

To guarantee that own effects of sharing on leakage costs exceed cross effects of sharing, we assume that when $s _ { 1 } = s _ { 2 } , \ | \partial g _ { i } / \partial s _ { i } | > | \partial g _ { i } / \partial s _ { j } | .$ , and $\vert \partial ^ { 2 } g _ { i } / \partial s _ { i } ^ { 2 } \vert >$ $| \partial ^ { 2 } g _ { j } / \partial s _ { i } ^ { 2 } |$ . The rationale for this assumption relates to the two types of consumers who may face each firm: loyal consumers and switchers. This distinction has been widely used in the marketing literature. (See, for instance, Narasimhan 1988.) While loyal customers buy either product i or nothing at all, switchers can be induced to purchase the competing brand $j .$ When $s _ { i }$ increases around a symmetric equilibrium, firm i loses both the loyal consumers and the switchers because of the reduced utility they face from the possibility of increased leakage costs. However, when $s _ { j }$ increases around this equilibrium, firm i gains only the switchers. Hence, any changes in its own level of sharing affects leakage costs more than changes in the level of sharing by the competitor.<sup>15</sup> The following example satisfies all of the above-mentioned properties of the function $g ( s _ { i } , s _ { j } )$

$$
\begin{array}{c} g ^ {i} (s _ {i}, s _ {j}) = \phi_ {1} s _ {i} ^ {2} - \phi_ {2} s _ {j} ^ {2} - \phi_ {3} s _ {i} s _ {j}, \\ \text {where} \phi_ {1} > \phi_ {2} + \phi_ {3}. \end{array}\tag{2}
$$

The willingness of the competitor to share information about its security breaches may have another positive implication on the demand facing the firm. When the consumers know that the firm is cooperating with a competitor as part of the ISA, to identify the most effective ways to prevent breaches, they are more confident that the firm’s efforts will indeed be successful.<sup>16</sup> We measure this additional benefit derived by firm i in terms of the decision variables chosen by its competitor, firm $j ,$ as $\lambda _ { d } t _ { j } s _ { j }$ . Such a specification captures the fact that the extent of benefit to firm i from information sharing by firm j depends on what firm j has to share, which, in turn, depends on the amount that firm j spends on information security technology.<sup>17</sup> This positive externality that accrues to the firm depends on the value of the spillover parameter $\lambda _ { d } .$ As with the cost spillover parameter, here as well, we assume that $\lambda _ { d }$ lies in the unit interval.

Note that the term $t _ { j } s _ { j }$ in the above formulation coincides with the variable $y _ { j }$ in Gordon et al. (2003). While in Gordon et al. (2003), this term affects the probability of a security breach, in the present model it affects the size of the demand. In both cases though, sharing information results in a positive externality conferred on competitors. Information on threats, vulnerabilities, and incidents experienced by others can help firms identify trends, better understand the risks faced, and determine what preventive measures should be implemented (Dacey 2003b). ISACs also seek to promote the sharing of technology related to detecting and stopping information security breaches, as well as ways to repair damage caused by such breaches. Having access to information about security vulnerabilities and the proposed solutions of the competitor can lead to more effective investments in security technologies by the firm.<sup>18</sup>

Finally, the demand intercept facing each firm may shift because of the investments undertaken by both firms, even in the absence of any information sharing between them. When a given firm increases its investment in security technology to prevent security breaches or enhance the effectiveness of security products, and consumers become informed of this increase, their level of anxiety about transacting with the firm declines, thus enhancing their expected utility and willingness to pay for the product. In contrast, if the competitor increases its level of investment and consumers become aware of it, the firm may experience a negative demand shock and lose some customers (for example, the switchers) because the competitor may now be considered the more reliable and secure source of supply. We summarize this net effect of the firms’ investments on the demand intercept of firm i in terms of the difference $( t _ { i } - \alpha t _ { j } )$ where $0 \leq \alpha < 1$ . Once again, since  is a fraction, own effects of investment exceed cross-effects.

Combining the benefits and costs of investments in security technology as well as information sharing yields the following net benefit function that can shift the demand intercept of firm $i ^ { 1 9 }$ :

$$
B _ {i} = t _ {i} - \alpha t _ {j} + \lambda_ {d} t _ {j} s _ {j} - g ^ {i} (s _ {i}, s _ {j}).\tag{3}
$$

Note that the competitor’s level of investment has both positive and negative implications on firm $i ^ { \prime } \mathrm { s }$ demand. On the positive side, consumers are reassured that i’s membership in the ISA is more beneficial to it, given that j reveals information concerning a larger level of investment. On the negative side, the competitor now appears a more attractive option to consumers. Since the former effect depends on the extent of sharing by $j ,$ the positive spillover expression depends on the product $t _ { j } s _ { j }$

## 2.1. Analysis

At the second stage, firm i chooses its price $p _ { i }$ to maximize its objective. The profit function of firm i can be

written as

$$
\Pi_ {i} = p _ {i} q _ {i} - f ^ {i} (t _ {i}, y _ {j}).
$$

From the first-order conditions (FOCs) for profit maximization, we derive the second-stage equilibrium prices, which are summarized in Appendix A. These become the starting point for deriving comparative statics to examine how changes in the exogenous and endogenous variables affect firm strategies and profits under different market conditions. In deriving some of the comparative statics, we will need the following assumptions:

Assumption 1.

$$
\alpha \leq \left(\lambda_ {d} \min \{s _ {1}, s _ {2} \} + \frac {b _ {2}}{2 b _ {1}}\right) = \bar {\alpha}.
$$

Assumption 2.

$$
\left[ - \left(2 b _ {1} \frac {\partial g ^ {i}}{\partial s _ {i}} + b _ {2} \frac {\partial g ^ {j}}{\partial s _ {i}}\right) _ {s _ {i} = s _ {j} = 0} + b _ {2} \lambda_ {d} t _ {i} \right] > 0
$$

$$
\left[ - \left(2 b _ {1} \frac {\partial g ^ {i}}{\partial s _ {i}} + b _ {2} \frac {\partial g ^ {j}}{\partial s _ {i}}\right) _ {s _ {i} = s _ {j} = 1} + b _ {2} \lambda_ {d} t _ {i} \right] <   0.
$$

Assumption 1 asserts that the negative implications of increased security investment by the competitor on the firm’s demand is not “too large.” This assumption is more likely to be valid when the demand spillover parameter $\lambda _ { d }$ or the degree of substitutability between products, $b _ { 2 } ,$ is relatively high. Assumption 2 consists of two parts. The first relates to the possibility that both firms share no information with each other and the second relates to the case that they share full information. In the former case, Assumption 2 asserts that the negative consequences of increasing the extent of sharing, as measured by the “marginal leakage costs,” are outweighed by the positive impact of such sharing, as measured by the marginal “demand spillover effect.” The second part of Assumption 2 asserts that the opposite is the case when both firms share full information with each other.

Proposition 1. (i) A firm’s price increases with an increase in its own investment in security technology. As well, under Assumption 1, price also increases with the competitor’s level of investment. Hence, ${ d p _ { i } } / { d t _ { i } } > 0$ and $d p _ { i } / d t _ { i } > 0$

(ii) Under Assumption 2, each firm’s price follows an inverted U-shaped curve with an increase in security information sharing, $i . e . , \ \partial p _ { i } / \partial s _ { i } > 0 \ f o r \ s _ { i } \in ( 0 , s _ { i } ^ { c } )$ and $\partial p _ { i } / \partial s _ { i } < 0 f o r s _ { i } \in ( s _ { i } ^ { c } , 1 )$ , where $0 < s _ { i } ^ { c } < 1$

Increased investment in security technology by the firm shifts its demand outward and raises its price reaction function. As a result, the firm chooses to raise its prices. When the competitor increases its security investment level, the competitor’s price reaction function shifts up. With upward sloping reaction functions, this shift leads the firm to raise its own price as well, as long as the parameter  is not “too large.” Recall that this parameter measures the negative consequences of the competitor’s investment level on the firm’s demand intercept.

When the firm intensifies its extent of sharing, there are two countervailing effects on its own demand and that of its competitor. Intensified sharing of security information increases the firm’s own leakage costs, thus reducing the demand facing it. On the other hand, because of spillover effects and reduced leakage costs of the competitor, the demand facing the competitor shifts outward. Because of the former, direct effect, the firm has an incentive to reduce its price. However, because of the latter, strategic effect, the competitor has an incentive to raise its price, which with upward sloping reaction functions, provides an incentive for the firm to raise its own price as well. The second part of Proposition 1 states that for small values of $s _ { i } < s _ { i } ^ { c } .$ , the latter strategic effect dominates and for large value of $s _ { i } > s _ { i } ^ { c }$ , the former direct effect dominates. Assumption 2 guarantees that perfect information sharing can never arise in equilibrium, thus leading to an interior solution, so that $s _ { i } ^ { c }$ is a fraction. Basically, because the marginal leakage cost with perfect information sharing is relatively large compared to positive spillovers on demand, full information sharing cannot be an equilibrium; and conversely, since the marginal leakage costs with no information sharing is relatively small in comparison to the positive demand spillovers, some information sharing does arise at the equilibrium.

Substituting the second-stage prices back into each firm’s objective function, we can obtain the first-stage payoff function in reduced form as

$$
\Pi_ {i} = b _ {1} p _ {i} ^ {2} - f ^ {i} (t _ {i}, y _ {j}),\tag{4}
$$

where $p _ { i }$ solve the FOCs. Differentiating with respect to the first-stage decision variables yields the

following two FOCs.<sup>20</sup>

$$
\frac {d \Pi_ {i}}{d s _ {i}} = 2 b _ {1} p _ {i} \frac {\partial p _ {i}}{\partial s _ {i}} = 0.\tag{5}
$$

$$
H _ {i} = \frac {d \Pi_ {i}}{d t _ {i}} = 2 b _ {1} p _ {i} \frac {\partial p _ {i}}{\partial t _ {i}} - \frac {\partial f ^ {i}}{\partial t _ {i}} = 0.\tag{6}
$$

Lemma 1. (i) Under Assumption 2, full information sharing is inconsistent with a symmetric equilibrium. Specifically, the optimal levels of information sharing and security technology investment are given as the solution to

$$
\left[ 2 b _ {1} \bigg (\frac {\partial g ^ {i}}{\partial s _ {i}} \bigg) + b _ {2} \bigg (\frac {\partial g ^ {j}}{\partial s _ {i}} \bigg) \right] = b _ {2} \lambda_ {d} t _ {i},
$$

$$
\frac {\partial f ^ {i}}{\partial t _ {i}} = 2 b _ {1} p _ {i} \bigg (\frac {2 b _ {1} + b _ {2} (\lambda_ {d} s _ {i} - \alpha)}{(4 b _ {1} ^ {2} - b _ {2} ^ {2})} \bigg).
$$

(ii) The reaction functions of both firms with respect to the extent of security information sharing are upward sloping, $i . e . , \ \partial s _ { i } / \partial s _ { i } > 0$ and $\partial t _ { i } / \partial s _ { j } > 0$ . As well, under Assumption 1, the reaction functions of both firms with respect to the extent of security investment are also upward sloping, i.e., $\partial s _ { i } / \partial t _ { j } > 0 , \partial t _ { i } / \partial t _ { j } > 0 .$

A direct interpretation of the results reported in Lemma 1 is provided in Proposition 2.

Proposition 2. (i) A higher level of security information sharing by one firm leads to a higher level of information sharing and security investment by its competitor. As well, $i f \alpha \leq \overline { { \alpha } } ,$

(ii) A higher level of security technology investment by one firm leads to a higher level of information sharing and security investment by its competitor.

(iii) Security technology investment and security information sharing act as strategic complements in this case.

Our analysis reveals that the reaction functions are upward sloping; that is, an increase in security technology investment by firm i induces a higher level of information sharing by firm $j$ and vice versa. The two inputs act as strategic complements. This is evident from the fact that $\partial ^ { 2 } \Pi _ { i } / \partial s _ { i } \partial t _ { j } > 0 .$ , i.e., the increase in profits with increased information sharing for firm i is higher for higher levels of technology investment by firm j and vice versa. Further, $\partial ^ { 2 } \Pi _ { i } / \partial s _ { i } \partial s _ { j } > 0 .$ , i.e., the increase in profits with increased information sharing for firm i is higher for higher levels of information sharing by firm j and vice versa. Hence, as we observed in Lemma 1, firm i responds to less aggressive play by firm j by being less aggressive itself. The same intuition applies to the change in a firm’s profits with a change in security technology investment by the other firm, where we find that $\partial ^ { 2 } \Pi _ { i } / \partial t _ { i } \partial t _ { j } > 0 ,$ when  is sufficiently small.

Note that the upper bound on  that is stated in Proposition 2 is stronger than necessary. To guarantee that the slopes $\partial s _ { i } / \partial t _ { j }$ and $\partial t _ { i } / \partial t _ { j }$ are positive, the parameter  cannot be too large, but a weaker condition than the one stated in Proposition 2 is sufficient (a higher upper bound on ).

Contrary to our results, when Gordon et al. (2003) use the “restricted cost” function, $f ^ { i } ( t _ { i } , y _ { j } ) = f ( t _ { i } - y _ { j } )$ they find that when firms share information, each firm has reduced incentives to invest in information security. The main reason for the different result is the existence of the demand-enhancing effects of information security sharing and technology investments in our model.<sup>21</sup>

It is important to note that the existence of positive demand spillovers $\left( \mathrm { i . e . , ~ } \lambda _ { d } > 0 \right)$ is essential to obtain a certain degree of sharing between the firms in our model. If $\lambda _ { d } < 0 ,$ so that there are negative demand spillovers, the only possible symmetric equilibrium is for firms not to share any information at all; namely, $s _ { i } = s _ { j } = 0$ . To see it, note that

$$
\left. \frac {\partial p _ {i}}{\partial s _ {i}} \right| _ {s _ {1} = s _ {2} = s} \equiv \left[ - \left(2 b _ {1} \frac {\partial g ^ {i}}{\partial s _ {i}} + b _ {2} \frac {\partial g ^ {j}}{\partial s _ {i}}\right) \Bigg | _ {s _ {1} = s _ {2} = s} + b _ {2} \lambda_ {d} t _ {i} \right].
$$

Hence, if $\lambda _ { d } < 0$ , the above is negative for all values of $s \in [ 0 , 1 ] ,$ given our assumption that their own effects always dominate cross-effects. From Equation (5), therefore, no information sharing is the only possible outcome. However, even in this case, security investment reaction functions may still slope upward $( \mathrm { i . e . , ~ } \partial t _ { i } / \partial t _ { j } > 0 )$ provided that the parameter  is sufficiently small $( { \mathrm { i . e . , ~ } } \alpha \leq b _ { 2 } / 2 b _ { 1 } )$

Proposition 3. (i) A lower level of firm loyalty leads to lower levels of security information sharing and security technology investment, $i . e . , \ \partial s _ { i } / \partial b _ { 1 } < 0 , \partial t _ { i } / \partial b _ { 1 } < 0$

(ii) When $\alpha \leq \overline { { \alpha } } ,$ the extent of information sharing and amount of security technology investment by both firms increase when the degree of product substitutability increases, $i . e . , \ \partial s _ { i } / \partial b _ { 2 } > 0 , \partial t _ { i } / \partial b _ { 2 } > 0 .$

We highlight that a steeper demand schedule, $b _ { 1 } ,$ lowers a firm’s propensity to invest in security technology and share security information. A steeper slope implies that each firm sells fewer units of the product for a given level of the equilibrium prices.<sup>22</sup> Smaller quantities imply, in turn, that the marginal return to any kind of technology investment is more limited. As a result, the firms have reduced incentives to invest in enhanced security technology. Further, the strategic complementarity between technology investment and information sharing implies also that the extent of sharing declines when demand schedules are steeper.

Quite interestingly, to the extent that product substitutability is indicative of the degree of competition in an industry, we find that a higher level of intraindustry competitiveness may lead to higher levels of security information sharing and increased investment in security technologies by both firms, when  is sufficiently small. Firms generally respond to increased competition with aggressive price cuts. To alleviate such aggressive price competition, firms have greater incentives to invest in mechanisms that alleviate price competition.<sup>23</sup> Because increases in s and t may help in mitigating price competition, both firms may decide to raise the extent of information sharing and investments when the degree of substitutability between the firms’ products increases.

We would like to point out that the intuition for our comparative statics results with respect to parameters $b _ { 1 }$ and $b _ { 2 }$ follows from the existence of two effects: a direct effect and a strategic effect. This is evident when optimizing the objective function in Stage 1 with respect to the decision variables $s _ { i }$ and $t _ { i }$ . Differentiating w.r.t. $s _ { i }$ and $t _ { i }$ separately, yields the following

equations:

$$
\frac {d \Pi_ {i}}{d s _ {i}} = \frac {\partial \Pi_ {i}}{\partial s _ {i}} + \frac {\partial \Pi_ {i}}{\partial p _ {j}} \frac {\partial p _ {j}}{\partial s _ {i}} + \frac {\partial \Pi_ {i}}{\partial p _ {i}} \frac {\partial p _ {i}}{\partial s _ {i}}.\tag{7}
$$

$$
\frac {d \Pi_ {i}}{d t _ {i}} = \frac {\partial \Pi_ {i}}{\partial t _ {i}} + \frac {\partial \Pi_ {i}}{\partial p _ {j}} \frac {\partial p _ {j}}{\partial t _ {i}} + \frac {\partial \Pi_ {i}}{\partial p _ {i}} \frac {\partial p _ {i}}{\partial t _ {i}}.\tag{8}
$$

Because the prices selected in the second stage solve the condition $\partial \Pi _ { i } / \partial p _ { i } = 0 .$ , in equilibrium the third term in both Equations (7) and (8) is equal to 0 (by the envelope theorem). The first terms in Equations (7) and (8) measure the direct effect of increased information sharing, and the second terms in the equations measure the strategic effect. The degree of substitutability, $b _ { 2 } ,$ affects primarily the magnitude of the strategic effect and the degree of disloyalty, $b _ { 1 } ,$ , affects primarily the magnitude of the direct effect. Note that the sign of the strategic effect is positive since from Proposition 1, the competitor raises prices when the firm shares more security information or increases security technology investment $( \partial p _ { j } / \partial s _ { i } > 0$ and $\partial p _ { j } / \partial t _ { i } > 0 )$

When $b _ { 2 }$ increases, the importance of alleviating price competition becomes especially pronounced, and as a result firms are willing to share more information and invest more in security technology. In contrast, when $b _ { 1 }$ increases the magnitude of the direct effect declines because each producer sells smaller volumes as a result of the increase in disloyalty of consumers. With smaller volumes, firms have lower incentives to make any kind of investment, including in improving information security. Because security technology and information sharing are complementary, they also cut back on their extent of sharing. In general, in all the comparative statics, the two effects mentioned above are present. Changes that reduce size (quantity) reduce the direct effect and, therefore, the incentives to invest in technology and share security information. On the other hand, changes that intensify price competition increase the strategic effect and, therefore, the incentives to invest and share.

Proposition 4. (i) Security information sharing and security technology investment levels increase with firm size.

(ii) A lower level of demand spillover and cost spillover discourages security information sharing and technology investments, i $. e . , \ \partial s _ { i } / \partial \lambda _ { d } > 0 , \ \partial s _ { i } / \partial \lambda _ { c } > 0 , \ \partial t _ { i } / \partial \lambda _ { d } > 0 ,$ $\partial t _ { i } / \partial \lambda _ { c } > 0$

(iii) A bigger value of  discourages security information sharing and technology investments, $i . e . , \ \partial s _ { i } / \partial \alpha < 0$ and $\partial t _ { i } / \partial \alpha < 0$

Proposition 4(i) suggests that investing in security information is more valuable to larger firms, because the marginal return to investment is directly related to the volume of sales of the firms. This conclusion is consistent with the well-known result that a monopolist benefits more from cost-reducing innovations than a firm competing in a duopoly, given that it can extract a higher proportion of the surplus from the market.<sup>24</sup> Because information sharing and technology investment act as strategic complements, this increased security investment also leads to higher security information sharing by the larger firm.

The result stated in Proposition 4(ii) implies that higher demand-side spillovers promote higher levels of information sharing and technology investment. Increased spillovers shift the demand curve outward, which enable firms to increase their prices and, as a result, their profits. Similarly, increased cost spillovers imply that the marginal cost of investment declines, thus providing greater incentives for the firm to intensify security investments and information sharing. Note that the latter result is implied by our assumption that the cost of investing in security information is independent of the firm’s volume of sales. In $\ S 4 ,$ we demonstrate that cost spillovers have an opposite effect to that described in the above proposition when the cost of investment is volume dependent. This opposing effect was also derived in Gordon et al. (2003).

As pointed out earlier, the results reported in Proposition 4(ii) rely on the existence of positive demand spillovers that lead to some information sharing at the equilibrium. Since in our model spillovers exist only if firms communicate with each other, the investment in security technology is independent of the values of $\lambda _ { d }$ and $\lambda _ { c }$ when $\lambda _ { d } < 0 \ ( \mathrm { i . e . }$ , $\partial t / \partial \lambda _ { d } = \partial t / \partial \lambda _ { c } = 0 )$

Proposition 4(iii) evaluates the parameter $\alpha ,$ which measures the adverse implications of the competitor’s security investment on the demand intercept of a given firm. According to this part, bigger values of discourage technology investments and information sharing. This result is quite intuitive, as bigger values of  imply lower volumes of sales and, as explained before, reduced incentives to invest.

## 2.2. Social Welfare

We now consider the case that the ISA dons the role of a federally funded social planner. From the demand expressions, one can derive the inverse demand functions in terms of prices such that $p _ { i } = F _ { i } ( q _ { i } , q _ { j } )$ . Let $q _ { 1 } =$ $q _ { 2 } = q ^ { * }$ denote the equilibrium quantity determined by the market. Focusing on a symmetric environment, where the social planner sets $t _ { 1 } = t _ { 2 } = t , s _ { 1 } = s _ { 2 } = s ,$ and $F _ { 1 } ( q , q ) = F _ { 2 } ( q , q ) = F ( q , q )$ , social welfare can be written as follows:

$$
\begin{array}{c} S W = 2 \int_ {0} ^ {q ^ {*}} F (q, q) d q - 2 f ^ {i} (t, \lambda_ {c} t s) \\ = 2 \int_ {0} ^ {q ^ {*}} \frac {a + B - q}{b _ {1} - b _ {2}} d q - 2 f ^ {i} (t, \lambda_ {c} t s), \end{array}\tag{9}
$$

where

$$
B = t (1 - \alpha) + \lambda_ {d} t s - g ^ {i} (s, s).\tag{10}
$$

In Appendix A, we show that the social welfare maximizing level of information sharing is higher than the solution to $\partial B / \partial s = 0$ . This last condition implies that the direct net marginal benefit of information sharing on each firm’s demand is equal to zero. Using Equation (10),

$$
\frac {\partial B}{\partial s} = \lambda_ {d} t - \left(\frac {\partial g ^ {i}}{\partial s _ {i}} + \frac {\partial g ^ {i}}{\partial s _ {j}}\right) = 0.\tag{11}
$$

When each firm maximizes its own profits under a Nash equilibrium, it chooses the extent of information sharing to satisfy $\partial p _ { i } / \partial s _ { i } = 0 .$ . Hence the optimal level of information chosen at the market equilibrium, $s ^ { N E * }$ satisfies the following condition:

$$
\lambda_ {d} t - \left(\frac {2 b _ {1}}{b _ {2}} \frac {\partial g ^ {i}}{\partial s _ {i}} + \frac {\partial g ^ {i}}{\partial s _ {j}}\right) = 0.\tag{12}
$$

Because $2 b _ { 1 } / b _ { 2 } > 1$ , it follows from comparing Equation (12) with (11), that for a fixed level of security technology investment, the socially optimal level of information shared is higher than that chosen under the Bertrand-Nash market equilibrium where firms are engaged in individual profit maximization.

Next, we consider the case where the ISA coordinates the choices of its members, in terms of their security technology investments and extent of information sharing, to maximize joint industry profits. In spite of this coordination on the choice of s and $t ,$ we assume that the ISA is prohibited from facilitating price coordination among its members. Prices are still given, therefore, by Equation (21) (in Appendix A), which at the symmetric equilibrium reduces to

$$
p ^ {*} = \frac {a + B}{2 b _ {1} - b _ {2}}.
$$

Because $q ^ { * } = b _ { 1 } p ^ { * }$ , joint industry profits can be expressed as follows:

$$
\Pi^ {I P} = \Pi_ {1} + \Pi_ {2} = \frac {2 b _ {1} (a + B) ^ {2}}{(2 b _ {1} - b _ {2}) ^ {2}} - 2 f ^ {i} (t, \lambda_ {c} t s).
$$

The ISA chooses s and t to maximize the above payoff function. The optimization with respect to s and t yields the conditions, respectively.

$$
\frac {\partial \Pi^ {J P}}{\partial s} = \frac {4 b _ {1} (a + B)}{(2 b _ {1} - b _ {2}) ^ {2}} \frac {\partial B}{\partial s} - 2 \lambda_ {c} t \frac {\partial f ^ {i}}{\partial y _ {j}} = 0.\tag{13}
$$

$$
\frac {\partial \Pi^ {I ^ {P}}}{\partial t} = \frac {4 b _ {1} (a + B)}{(2 b _ {1} - b _ {2}) ^ {2}} \frac {\partial B}{\partial t} - 2 \left[ \frac {\partial f ^ {i}}{\partial t _ {i}} + \lambda_ {c} s \frac {\partial f ^ {i}}{\partial y _ {j}} \right] = 0.\tag{14}
$$

A comparison of Equations (13) and (14) with (27) and (28) (from Appendix A) implies that maximizing social welfare yields higher levels of sharing and security technology investment than that chosen under joint profit maximization. A similar comparison of Equations (13) and (14) with (12) and (29) (in Appendix A), yields that joint profit maximization yields higher levels of sharing and security investment than that obtained at the market equilibrium. In Proposition 5, we summarize the comparison of the extent of information sharing and technology investment under the three regimes discussed above: welfare maximization, joint profit maximization, and individual profit maximization.

Proposition 5. (i) Social welfare at the symmetric Bertrand equilibrium is higher with security information sharing than with no sharing.

(ii) When $\alpha \leq { \overline { { \alpha } } } ,$ the level of security information sharing and security technology investment that are socially optimal are higher than those selected by an ISA whose objective is to maximize joint industry profits. Moreover, a joint profit maximizing ISA chooses higher levels of information sharing and technology investment than those selected at the market equilibrium, when firms are engaged in individual profit maximization.

The comparison presented in Proposition 5 can be explained by recalling the different objectives of the social planner, the joint profit maximizing ISA, and the individual firms. While the ISA’s objective is to maximize total industry profits, the social planner aims to maximize the sum of the consumer and producer surplus. Hence, the joint profit maximizing ISA implements lower levels of technology investment and security information sharing than the social planner, because it does not incorporate the added benefit to consumers from enhanced technology investments. The reason the joint profit maximizing ISA wishes to implement higher levels of information sharing and security technology investment than firms that choose these decision variables independently, stems from the fact that individual firms do not fully internalize the positive externality that the investment confers on their competitors. Hence, this decreases the marginal return from information sharing and technology investment.

Once again, it is important to note that the comparison conducted in Proposition 5 depends on our assumption that $\lambda _ { d } > 0 .$ . With negative demand spillovers, a social planner may also wish to prevent any information sharing among firms if the extent of adverse demand spillovers is relatively big, in comparison to the extent of positive cost spillovers. From Equation (27) in Appendix $\scriptstyle \mathbf { A } ,$ it follows that if the magnitude of $\lambda _ { d }$ (when negative) is relatively big in comparison to the magnitude of $\lambda _ { c } ,$ a social planner will choose $s _ { i } = s _ { j } = 0 .$ , similar to firms that act as Nash competitors.

The result reported in Proposition 5 implies that the government should encourage industry participants to cooperate in setting their security investments and information sharing levels. Even if their coordination does not result in socially optimal levels of investment and sharing, it still yields an improvement over the outcome attained in the absence of coordination. This conclusion is valid, however, only if members of the ISA do not use those coordination activities as a vehicle to collude on prices. If formation of the joint profit maximizing ISA facilitates such collusion, the members may raise prices above the Bertrand-Nash level and, consequently, reduce social welfare. Whereas prices at the Bertrand-Nash equilibrium are equal to $p ^ { N E } = ( a + B ) / ( 2 b _ { 1 } - b _ { 2 } )$ , price under collusion is the monopoly price $p ^ { J P } = ( a + B ) / ( 2 ( b _ { 1 } - b _ { 2 } ) )$ For a fixed level of security technology investment, the higher prices selected under collusion result in reduced quantities demanded by consumers, since $q ^ { J P } = ( a + B ) / 2 < ( b _ { 1 } ( a + B ) ) / ( 2 b _ { 1 } - b _ { 2 } ) = q ^ { N E }$ . Given that quantities at the Bertrand-Nash equilibrium $q ^ { N E * }$ fall short of the socially optimal level of production $q ^ { S W ^ { * } }$ the further decline of quantities because of collusion in pricing reduces social welfare. This points out the need for legislation, which would allow an ISA to choose levels of security information sharing but prevent members from colluding in prices.

Our result that information sharing is social welfare enhancing is also consistent with the findings of Gordon et al. (2003) who posit that at the Nash equilibrium, a small increase in expenditures on information security by either firm would increase social welfare. They also point out that the socially optimal expenditure levels for each firm are greater than the Nash equilibrium levels. However, they highlight that this may not hold true for both firms simultaneously, if there is asymmetry among firms in terms of IT security productivity.

## 3. Sequential Entry

Analytical modelers have recognized that the qualitative insights regarding market equilibria often depend on the sequence in which firms in an industry choose their strategies. While the simultaneous mode of conduct is more common in fragmented industries, there are numerous examples where one firm acts as a leader and others act as followers in a given industry. Firms may understandably be reluctant to share sensitive proprietary information on security practices, intrusions, and actual crimes with either government agencies or competitors. To many firms, information sharing is a risky proposition with less than clear benefits. Specifically, concerns have been raised that a firm’s information could be subject to the Freedom of Information Act, or face potential liability concerns for information shared in good faith (Dacey 2003b). These actions could potentially jeopardize a firm’s market share or customer base. This may be especially true when some firms are more likely to be pioneering in their approach to disclosing critical information while others adopt a “wait and watch policy.”<sup>25</sup> It may be interesting, therefore, to compare the amount of security information sharing and technology investment when firms join an ISA in a sequential manner, with the case when they make their choices simultaneously.

Hence, we consider a scenario where an incumbent firm has already committed to sharing information and investing in technology, anticipating the entry and similar sharing behavior of another firm. In Stage 1, the incumbent chooses $( s _ { i } , t _ { i } ) .$ , and in Stage 2, the entrant chooses $( s _ { j } , t _ { j } )$ . In Stage 3, both firms choose prices $( p _ { i } , p _ { j } )$ simultaneously. With sequential choices, the FOCs for firm i (incumbent) are as follows:

$$
G _ {i} = \frac {d \Pi_ {i}}{d s _ {i}} = 2 b _ {1} p _ {i} \frac {\partial p _ {i}}{\partial s _ {i}} + 2 b _ {1} p _ {i} \frac {\partial p _ {i}}{\partial s _ {j}} \frac {\partial s _ {j}}{\partial s _ {i}} + 2 b _ {1} p _ {i} \frac {\partial p _ {i}}{\partial t _ {j}} \frac {\partial t _ {j}}{\partial s _ {i}}\tag{15}
$$

$$
H _ {i} = \frac {d \Pi_ {i}}{d t _ {i}} = 2 b _ {1} p _ {i} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial p _ {i}}{\partial t _ {j}} \frac {\partial t _ {j}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial p _ {i}}{\partial s _ {j}} \frac {\partial s _ {j}}{\partial t _ {i}} - \frac {\partial f ^ {i}}{\partial t _ {i}}\tag{16}
$$

Note, however, that the FOCs for the follower will be similar to those in the simultaneous mode, given by Equations (5) and (6).

Proposition 6. The optimal amount of shared security information and security technology investment by firm i (incumbent) will be higher in the sequential mode than in the simultaneous mode, provided that $\alpha \leq { \overline { { \alpha } } } .$

Comparing FOCs given by Equations (15) and (16) with (5) and (6), implies that with sequential entry, each FOC of the leader includes an additional positive term that reflects the “Stackelberg effect.” This effect occurs because the leader incorporates the implication of its own investment t<sub>i</sub>	 and sharing $\left( { { s _ { i } } } \right)$ on the choice of the levels of investment $( t _ { j } )$ and sharing s 	 made subsequently by the follower. The leader

## 4. Impact of Volume-Related Costs

knows, in particular, that such a precommitment to increase the security technology investment or shared security information will induce the entrant to do the same.<sup>26</sup> Because increased information sharing and technology investment leads to softening of price competition, both firms’ profits will be strictly higher in the sequential mode than in the simultaneous mode game. Proposition 6 suggests that security information sharing and security technology investment are indeed higher in the former than in the latter mode, leading to higher profits because of further alleviation of price competition.<sup>27</sup>

Many firms believe that increased efficiency may be attained by outsourcing the information security function. Hence, some firms have outsourced their security and network management to an external entity like a managed security services provider (MSSP). This entity engages in modulation of security resources and services, depending on control/variability.<sup>28</sup> During the course of outsourcing, an MSSP often provides different levels of quality of security service (QoSS) based on the size of the firm. Given that the payment to the MSSP may depend on the firm size, it would be appropriate to modify our model by including some additional technology costs, which are affected by the volume of sales. Even if the firm manages its own security, as demand and the corresponding IT infrastructure grows, so would costs related to installation of additional servers, QoSS license fees, dynamic security service agreements, increasing utilization of associated security weapons like firewalls, intrusion detection systems (IDS), virtual private networks, content filters, access control systems, etc. In this section, we analyze the impact of sales volume-related costs of technology on firms optimal sharing and investment strategies.

Having considered cost spillovers on fixed costs, we now consider only spillovers on security technology costs, which are influenced by the volume of sales. We model the new marginal cost function as $( c - \hat { \lambda } t _ { j } s _ { j } ) \delta ( t _ { i } )$ and assume that $\delta ^ { \prime } > 0 , \delta ^ { \prime \prime } > 0$ The parameter $\hat { \lambda }$ is the “volume-related cost side” spillover from information sharing. In this new environment, the first-stage profit equation in reduced form is

$$
\Pi_ {i} = b _ {1} (p _ {i} - (c - \hat {\lambda} t _ {j} s _ {j}) \delta (t _ {i})) ^ {2} - f (t _ {i}),
$$

where, for simplicity, we assume the nonexistence of fixed cost spillovers $( \mathrm { i } . \mathrm { e } . , \lambda _ { c } = 0 )$ . Designating the term $( c - \hat { \lambda } t _ { i } s _ { i } ) \delta ( t _ { i } ) = F _ { i } .$  the FOCs can now be written as:

$$
G _ {i} = \frac {d \Pi}{d s _ {i}} = 2 b _ {1} (p _ {i} - F _ {i}) \frac {\partial p _ {i}}{\partial s _ {i}} = 0.\tag{17}
$$

$$
H _ {i} = \frac {d \Pi}{d t _ {i}} = 2 b _ {1} (p _ {i} - F _ {i}) \left(\frac {\partial p _ {i}}{\partial t _ {i}} - \frac {\partial F _ {i}}{\partial t _ {i}}\right) - f ^ {\prime} (t _ {i}) = 0.\tag{18}
$$

From conditions (17) and (18), we can assess how cost side spillovers impact firms’ incentives to share information and invest in technology. We formally show the following:

Proposition 7. When the costs of security technology investment are affected by the volume of sales, and there are “volume-related cost side spillovers” as captured by the parameter $\hat { \lambda }$ ,

(i) An increase in $\hat { \lambda }$ has ambiguous implications on the propensity to share security information or invest in security technology for both firms.

(ii) Volume-related spillovers reduce incentives to share information in comparison to an environment, where no such spillovers exist.

Changes in the spillover parameter $\hat { \lambda }$ introduce two countervailing effects. An increase in $\hat { \lambda }$ makes firm i’s competitor more efficient by reducing its unit cost $c - \hat { \lambda } t _ { i } s _ { i }$ . This enables $j$ to price more aggressively. If firm i increases its level of information shared, it further increases the cost efficiency of the competitor, which acts to the disadvantage of the firm. Because the improved cost efficiency precipitates further price competition, both firms respond strategically by reducing their levels of information sharing. On the other hand, an increase in $\hat { \lambda }$ increases the profit margin of each firm, thus providing greater incentives for increased investment in technology and information sharing. In Appendix $\mathbf { A } ,$ we demonstrate that the relative size of the above-mentioned effects depends on the ratio of the two parameters measuring demand and volume-related cost spillovers, $( \lambda _ { d } / \hat { \lambda } )$ The smaller this ratio, the bigger the former effect, implying that increased volume-related cost spillovers reduce the incentives to share information.

It may also be interesting to investigate what happens to the slope of the information-sharing reaction functions. We demonstrate that the informationsharing reaction function, $\partial s _ { i } / \partial s _ { j } ,$ , is not necessarily increasing, unlike in the case when there are no volume-related costs of investing in security technology. In particular, the sign of the slope of this reaction function is determined by the size of the parameter $\hat { \lambda } .$ For small values of $\hat { \lambda } ,$ $\partial s _ { i } / \partial s _ { j } > 0 ,$ , and for large, $\partial s _ { i } / \partial s _ { j } < 0$ . Thus, only if volume-related cost spillovers are sufficiently small, information sharing by one firm induces the other firm to share more information. While a higher level of information sharing fosters greater opportunities for tacit collusion, as derived in earlier sections, it also leads to a more efficient competitor who faces lower variable costs. Such a competitor tends to price more aggressively. When the value of $\hat { \lambda }$ is sufficiently big, the latter effect is significant, thus reversing the result we have derived in the absence of volume-related cost spillovers.

Volume-related spillovers costs yield, therefore, predictions that are more consistent with the free-riding behavior described in Gordon et al. (2003) or in the R&D literature (d’Aspremont and Jacquemin 1988, Kamien et al. 1992).<sup>29</sup>

## 5. Implications, Conclusion, and Extensions

The U.S. federal government has encouraged the formation of ISACs, with the goal of helping protect critical infrastructure assets that are largely owned and operated by the private sector. This has been witnessed in industries such as banking and finance, IT, chemicals, oil and gas, electricity, etc. The underlying assumption is that such centrally coordinated information-sharing organizations would facilitate the alignment of goals for both the private sector and the federal government, which, in turn, would improve the security of cyber infrastructure assets. However, all sectors do not have a fully established ISAC, and in those sectors that do, there is mixed participation. Specifically, five recently reviewed ISACs showed different levels of progress in implementing the PDD 63 suggested activities.<sup>30</sup> Hence, the government felt the importance to identify economic incentives to encourage the desired information-sharing behavior in IT security (Dacey 2003a).

We develop a model to investigate the benefits to firms from joining such security information-sharing alliances. Our results point out that if information sharing among members of the alliance had sufficiently large positive implications on the demand facing the firms, there are, indeed, strong economic incentives for firms to engage in sharing security information. Increase in security information sharing may yield two benefits for the firms: a “direct effect,” which increases demand and a “strategic effect,” which alleviates price competition. These incentives become stronger with increases in the firm size and the degree of competition. Because such alliances can give rise to positive spillover effects, we investigate their impact on sharing and security investment levels. Importantly, we demonstrate that the nature of the security technology cost function plays a pivotal role in determining whether spillovers are beneficial or detrimental to firms’ incentives to join the ISA. We also point out that joining the ISA may not be beneficial to the firm if it loses its competitive advantage in the marketplace, when competing against a rival whose product is perceived to be more secure by consumers. To support the existence of incentives for information sharing, the extent of positive demand spillovers should be sufficiently large to more than offset this adverse implication on the competitive position of the firm.<sup>31</sup>

We find that an increase in security information sharing and security technology investment levels lead to higher social welfare, compared to the no-sharing regime. However, the equilibrium levels vary depending on whether an ISA enacts the role of a social planner or a joint profit maximizer. The levels of security information sharing and technology investment obtained under a market equilibrium fall short of those that maximize social welfare. Even when the members of an ISA coordinate their information sharing and technology investment decisions to maximize joint industry profits, the extent of sharing and investment falls short of socially desirable levels. Joint profit maximization yields, however, higher levels of sharing than those obtained at the market (Bertrand-Nash) equilibrium, implying that coordination among firms on technology security should actually be encouraged by the federal government.<sup>32</sup> Even if their coordination does not result in socially optimal levels of technology investment and information sharing, it still yields an improvement over the outcome attained in the absence of coordination.

Our model shows that when firms face volumerelated costs, increased spillover effects do not necessarily encourage firms to share security information. In our analysis, we have only considered symmetric cost side spillovers, implying that both firms are equally efficient in utilizing the shared security information in reducing their marginal costs of technology investment. In future research, we plan to extend the model to allow for asymmetries among firms in utilizing the cost side spillover benefit. A preliminary investigation indicates that if firms differ in their intrinsic ability to utilize the shared information, the more efficient firm may have stronger incentives to underinvest in security technology and have lower incentives to share information, compared to the less efficient firm. The total effect of a change in the spillover parameter is not driven by the direct effect of this change alone, but also by the competitor’s reaction to it. This opens up the possibility of indirect freeriding behavior by the more efficient firm. Gordon et al. (2003) also point out such a possibility in their model.

ISACs do not seem to have well-designed incentives to prevent firms from free riding. Additionally, firms that join such alliances are often concerned about providing competitive advantage to other member firms. Thus, there is a possibility that even after entering an alliance, firms might renege on sharing security breach information with other member firms. To mitigate such concerns, the Chemical Industry Cyber-Security Information Sharing Network has put in place standards for authentication and verification of the security information being shared.

While PDD 63 encouraged the creation of ISACs, it left the actual design and function of the ISACs to be determined by the private sector in consultation with the federal government (Dacey 2003a). A significant implication of our model is that rigorous empirical studies of the structure and activities of such information-sharing organizations are needed. These studies would not only determine the actual levels of information sharing occurring among members of ISACs, but could provide deep insights into the appropriate incentives that may be required to facilitate such sharing, without causing excessive price increases.<sup>33</sup> These incentives may include various public policy tools related to tax benefits, subsidies, or specific legislation protecting firms from antitrust actions. In addition, empirical studies could address the role of government intervention in the form of optimal incentives or subsidies to prevent firms from reneging on their information-sharing commitments.

Although markets differ in a number of ways, we consider only a limited number of market characteristics in our research. For instance, in our social welfare analysis, we focus on only one industry. In reality, a security breach in a critical infrastructure industry, such as banking, may adversely affect producers and consumers in other industries. Ideally, a social welfare function should recognize such crossindustry spillover effects. Another limitation of our model is that we implicitly assume that whatever security information a firm is willing to share, it shares it truthfully. However, in the absence of additional incentives, truthtelling may not be an equilibrium outcome as has been shown by Ziv (1993) in the context of trade associations.<sup>34</sup> Despite these limitations, we believe that our model addresses an important issue, and hope that the proposed approach may be used as a starting point for additional research in this area.

## Acknowledgments

The authors are grateful to seminar participants at the 2005 International Industrial Organization Conference, 2003 Workshop on Economics and Information Security, Heinz School of Public Policy, and Tepper School at Carnegie Mellon University for useful suggestions. They also thank Ross Anderson, John Caulkins, Anthony Dukes, Ramayya Krishnan, and Uday Rajan for helpful comments. Finally, the authors thank the associate editor and two anonymous referees for their substantive suggestions, which have improved this paper.

## Appendix A. Proofs

## Derivation of Benefit Function

Assume that the utility of a representative consumer when consuming $q _ { 1 }$ and $q _ { 2 }$ units of the two products is

$$
\begin{array}{c} {U (q _ {1}, q _ {2}) = (r _ {1} q _ {1} + r _ {2} q _ {2}) - \frac {d _ {1} q _ {1} ^ {2}}{2} - \frac {d _ {2} q _ {2} ^ {2}}{2} - z q _ {1} q _ {2}} \\ {+ (Y - p _ {1} q _ {1} - p _ {2} q _ {2}),} \end{array}
$$

where $d _ { j } > z$ and the last bracketed term is the consumer’s utility from the consumption of other products. Then,

$$
\frac {\partial U}{\partial q _ {j}} = r _ {j} - d _ {j} q _ {j} - z q _ {i} - p _ {j} = 0, \quad i, j = 1, 2, i \neq j.\tag{19}
$$

Hence the marginal utility from consuming product j increases with $r _ { j }$ and declines with the quantity that the consumer buys of product j as well as the quantity he buys of the competing product $i .$ The parameter $r _ { j }$ reflects the consumer’s appreciation of $j ^ { \prime } \mathbf { s }$ product, which is inversely related to his expectations concerning security breaches that firm j might experience.

From (19), we get the following two equations:

$$
\begin{array}{l} q _ {1} = \frac {(d _ {2} r _ {1} - z r _ {2})}{(d _ {1} d _ {2} - z ^ {2})} - \frac {d _ {2} p _ {1}}{(d _ {1} d _ {2} - z ^ {2})} + \frac {z p _ {1}}{(d _ {1} d _ {2} - z ^ {2})}, \\ q _ {2} = \frac {(d _ {1} r _ {2} - z r _ {1})}{(d _ {1} d _ {2} - z ^ {2})} - \frac {d _ {1} p _ {2}}{(d _ {1} d _ {2} - z ^ {2})} + \frac {z p _ {2}}{(d _ {1} d _ {2} - z ^ {2})}. \end{array}\tag{20}
$$

Define

$$
a _ {i} + B _ {i} = \frac {d _ {j} r _ {i} - z r _ {j}}{d _ {1} d _ {2} - z ^ {2}}, \qquad b _ {1} = \frac {d _ {j}}{d _ {1} d _ {2} - t ^ {2}}, \qquad b _ {2} = \frac {z}{d _ {1} d _ {2} - t ^ {2}}.
$$

Hence, from the definition of $B _ { i } ,$ it follows that

$$
g ^ {i} (s _ {i}, s _ {j}) = a _ {i} + t _ {i} - \alpha t _ {j} + \lambda_ {d} s _ {j} t _ {j} - \frac {d _ {j} r _ {i} - z r _ {j}}{d _ {1} d _ {2} - z ^ {2}}.
$$

For simplicity, assume that the consumer $' \mathrm { s }$ appreciation of product $i ,$ as measured by $r _ { i } ,$ depends on $s _ { i }$ but is independent of the value of $s _ { j } .$ . Hence $\partial r _ { i } / \partial s _ { i } < 0$ but $\partial r _ { i } / \partial s _ { j } = 0$ . As well, assume that this appreciation declined at an increasing pace when $s _ { i }$ increases, thus $\partial ^ { 2 } r _ { i } / \partial s _ { i } ^ { 2 } < 0 .$ . As a result,

$$
\frac {\partial g ^ {i}}{\partial s _ {i}} = \frac {- d _ {j} \partial r _ {i} / \partial s _ {i}}{d _ {1} d _ {2} - z ^ {2}} > 0, \quad \frac {\partial g ^ {i}}{\partial s _ {j}} = \lambda_ {d} t _ {j} + \frac {z \partial r _ {j} / \partial s _ {j}}{d _ {1} d _ {2} - z ^ {2}}.
$$

Hence $\partial g ^ { i } / \partial s _ { i } < 0 \mathrm { i f } \lambda _ { d } t _ { i } < - ( z \partial r _ { i } / \partial s _ { i } ) / ( d _ { 1 } d _ { 2 } - z ^ { 2 } )$ . As well, $\vert \partial g ^ { i } / \partial s _ { i } \vert > \vert \partial g ^ { i } / \partial s _ { j } \vert$ by our assumption that $d _ { j } > z$

$$
\begin{array}{r} \frac {\partial^ {2} g ^ {i}}{\partial s _ {i} ^ {2}} = \frac {- d _ {j} \partial^ {2} r _ {i} / \partial s _ {i} ^ {2}}{d _ {1} d _ {2} - z ^ {2}} > 0, \quad \frac {\partial^ {2} g ^ {i}}{\partial s _ {i} \partial s _ {j}} = 0, \\ \frac {\partial^ {2} g ^ {i}}{\partial s _ {j} ^ {2}} = \frac {z \partial^ {2} r _ {j} / \partial s _ {j} ^ {2}}{d _ {1} d _ {2} - z ^ {2}} <   0. \end{array}
$$

Since $z < d _ { j } , \ | \partial ^ { 2 } g ^ { i } / \partial s _ { i } ^ { 2 } | > | \partial ^ { 2 } g ^ { i } / \partial s _ { j } ^ { 2 } |$ . The above specification yields all the restrictions we have imposed on the “leakage costs” function $g ^ { i } ( s _ { i } , s _ { j } )$

Proof of Proposition 1. From the profit function of firm $i ,$ we first derive the reduced form version of firm $i \prime \mathrm { s }$ profit function given by Equation (4). From Equations (1) and (3), the profit function of firm i is

$$
\Pi_ {i} = p _ {i} q _ {i} - f ^ {i} (t _ {i}, y _ {j}) = p _ {i} (a _ {i} - b _ {1} p _ {i} + b _ {2} p _ {j} + B _ {i}) - f ^ {i} (t _ {i}, y _ {j}),
$$

implying that

$$
\frac {d \Pi_ {i}}{d p _ {i}} = a _ {i} - 2 b _ {1} p _ {i} + b _ {2} p _ {j} + B _ {i}.
$$

The optimal price is then $p _ { i } = ( a _ { i } - b _ { 1 } p _ { i } + b _ { 2 } p _ { j } + B _ { i } ) / b _ { 1 }$ . This then implies that $q _ { i } = b _ { 1 } p _ { i }$ . Hence

$$
\Pi = q _ {i} p _ {i} - f ^ {i} (t _ {i}, y _ {j}) = b _ {1} p _ {i} ^ {2} - f ^ {i} (t _ {i}, y _ {j}).
$$

From Equation (4), the FOC for the second-stage decision variable; that is, the price leads to the following reaction function:

$$
p _ {i} (p _ {j}) = \frac {a _ {i} + b _ {2} p _ {j} + B _ {i}}{2 b _ {1}}.
$$

By solving these two equations simultaneously, we get the following optimal prices:

$$
p _ {i} = \frac {(2 b _ {1} a _ {i} + b _ {2} a _ {j}) + (2 b _ {1} B _ {i} + b _ {2} B _ {j})}{4 b _ {1} ^ {2} - b _ {2} ^ {2}}.\tag{21}
$$

From Equation (21), we then have

$$
\frac {\partial p _ {i}}{\partial t _ {i}} = \frac {2 b _ {1} + b _ {2} (\lambda_ {d} s _ {i} - \alpha)}{(4 b _ {1} ^ {2} - b _ {2} ^ {2})} > 0, i, j = 1, 2, i \neq j.
$$

The above inequality holds since $\alpha \ : < 1$ and $b _ { 1 } > b _ { 2 }$ From (21), we also have

$$
\frac {\partial p _ {i}}{\partial t _ {j}} = \frac {(2 b _ {1} (\lambda_ {d} s _ {j} - \alpha) + b _ {2})}{(4 b _ {1} ^ {2} - b _ {2} ^ {2})}.
$$

Under Assumption 1, the above is positive.

Differentiating further the optimal price w.r.t. s yields

$$
\frac {\partial p _ {i}}{\partial s _ {i}} = \frac {2 b _ {1} (- \partial g ^ {i} / \partial s _ {i}) + b _ {2} (- \partial g ^ {j} / \partial s _ {i}) + b _ {2} \lambda_ {d} t _ {i}}{(4 b _ {1} ^ {2} - b _ {2} ^ {2})}.\tag{22}
$$

Evaluating the above derivative at $s _ { i } = 0$ implies that $\vert \partial p _ { i } / \partial s _ { i } \vert _ { s _ { i } = 0 } > 0$ and evaluating the above derivative at $s _ { i } =$ $s _ { j } = 1$ implies that $\lvert \partial p _ { i } / \partial s _ { i } \rvert _ { s _ { i } = s _ { i } = 1 } < 0$ from Assumption 2. As well, since $\partial ^ { 2 } g _ { i } / \partial s _ { i } \partial s _ { j } \leq 0 ,$ the derivative $\partial { p _ { i } } / \partial { s _ { i } }$ is strictly increasing in $s _ { j } .$ . Hence, if $\lvert \partial p _ { i } / \partial s _ { i } \rvert _ { s _ { i } = s _ { i } = 1 } < 0 ,$ , it follows that $| \partial p _ { i } / \partial s _ { i } | _ { s _ { i } = 1 } < \acute { 0 }$ for any value of $s _ { i } ^ { \prime } < 1$ as well. By our assumption that $\vert \partial ^ { 2 } g _ { i } / \bar { \partial ^ { } } s _ { i } ^ { 2 } \vert > \vert \partial ^ { 2 } g _ { i } / \partial s _ { i } ^ { 2 } \vert$ , it follows that $\partial { p _ { i } } / \partial { s _ { i } }$ is a strictly decreasing function of $s _ { i } .$ . Hence, there exists s<sup>c</sup> <sub>∈</sub> 0 1	, where $\partial p _ { i } / \partial s _ { i } = 0 ,$ and the proposition follows. <sup></sup>

Proof of Lemma 1. The proof for the first part follows from Equations (5), (6), and (22). The proof for the second part is embedded in the following proof of Proposition 2. <sup></sup>

## Proof of Proposition 2.

(i) Because we do not get closed-form solutions for the first-stage decision variables, we adopt the implicit function approach to present our results and gain insights. We want to perform comparative statics of the firm i’s decision variables $s _ { i }$ and $t _ { i }$ w.r.t. that of the second firm decision variables; say, $s _ { j } .$ . Upon total differentiation of Equations (5) and (6), we get the following set of equations:

$$
\frac {\partial^ {2} p _ {i}}{\partial s _ {i} ^ {2}} d s _ {i} + \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial t _ {i}} d t _ {i} + \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial s _ {j}} d s _ {j} = 0,\tag{23}
$$

$$
\frac {\partial H _ {i}}{\partial s _ {i}} d s _ {i} + \frac {\partial H _ {i}}{\partial t _ {i}} d t _ {i} + \frac {\partial H _ {i}}{\partial s _ {j}} d s _ {j} = 0, \quad i, j = 1, 2, i \neq j.\tag{24}
$$

The set of two simultaneous equations for each firm leads us to the following solution for the derivatives $d s _ { i } / d s _ { j }$ and $d t _ { i } / d s _ { j }$ :

$$
\binom{\frac {d s _ {i}}{d s _ {j}}}{\frac {d t _ {i}}{d s _ {j}}} = - M ^ {- 1} \binom{\frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial s _ {j}}}{\frac {\partial H _ {i}}{\partial s _ {j}}},
$$

where

$$
M = \left( \begin{array}{c c} \frac {\partial^ {2} p _ {i}}{\partial s _ {i} ^ {2}} & \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial t _ {i}} \\ \frac {\partial H _ {i}}{\partial s _ {i}} & \frac {\partial H _ {i}}{\partial t _ {i}} \end{array} \right).
$$

Here,

$$
\frac {\partial H _ {i}}{\partial s _ {j}} = 2 b _ {1} \frac {\partial p _ {i}}{\partial t _ {i}} \frac {\partial p _ {i}}{\partial s _ {j}} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial s _ {j}} - \lambda_ {c} t _ {j} \frac {\partial^ {2} f ^ {i}}{\partial t _ {i} \partial y _ {j}},
$$

$$
\frac {\partial H _ {i}}{\partial s _ {i}} = 2 b _ {1} \frac {\partial p _ {i}}{\partial s _ {i}} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial s _ {i}},
$$

$$
\frac {\partial H _ {i}}{\partial t _ {i}} = 2 b _ {1} \bigg (\frac {\partial p _ {i}}{\partial t _ {i}} \bigg) ^ {2} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial t _ {i} ^ {2}} - \frac {\partial^ {2} f ^ {i}}{\partial t _ {i} ^ {2}}.
$$

From the expression for the optimal prices given in the Proof of Proposition 1, we derive the following:

$$
\begin{array}{r} \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial s _ {i}} = \frac {b _ {2} \lambda_ {d}}{(4 b _ {1} ^ {2} - b _ {2} ^ {2})} > 0, \\ \frac {\partial^ {2} p _ {i}}{\partial s _ {i} ^ {2}} = - \frac {2 b _ {1} \partial^ {2} g ^ {i} / \partial s _ {i} ^ {2} + b _ {2} \partial^ {2} g ^ {j} / \partial s _ {i} ^ {2}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} <   0. \end{array}
$$

To satisfy the second-order conditions and ensure global concavity, the determinant of M must be positive and $\partial H _ { i } / \partial t _ { i } < 0$ . Further in equilibrium, $\partial p _ { i } / \partial s _ { i } = 0 .$ , implying that $\partial H _ { i } / \partial s _ { i } > 0$ since $\partial ^ { 2 } p _ { i } / \dot { \partial } t _ { i } \partial s _ { i } > 0 .$

As well, we proceed to prove that the following expression is positive:

$$
\frac {\partial p _ {i}}{\partial s _ {j}} = \frac {2 b _ {1} (\lambda_ {d} t _ {j} - \partial g ^ {i} / \partial s _ {j}) + b _ {2} (- \partial g ^ {j} / \partial s _ {j})}{4 b _ {1} ^ {2} - b _ {2} ^ {2}}.
$$

From the FOC $\partial p _ { j } / \partial s _ { j } = 0$ , we have that

$$
- \frac {\partial g ^ {j}}{\partial s ^ {j}} = \frac {b _ {2}}{2 b _ {1}} \bigg (\frac {\partial g ^ {i}}{\partial s _ {j}} - \lambda_ {d} t _ {j} \bigg).
$$

Hence

$$
\begin{array}{c} \frac {\partial p _ {i}}{\partial s _ {j}} = \frac {2 b _ {1} (\lambda_ {d} t _ {j} - \partial g ^ {i} / \partial s _ {j}) + (b _ {2} / 2 b _ {1}) (b _ {2} \partial g ^ {i} / \partial s _ {j} - b _ {2} \lambda_ {d} t _ {j})}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} \\ = \frac {\lambda_ {d} t _ {j} - \partial g ^ {i} / \partial s _ {j}}{2 b _ {1}} > 0. \end{array}
$$

Next, from Equation (21), we show that

$$
\frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial s _ {j}} = 0 \quad \text { and } \quad \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial s _ {j}} = \frac {- 2 b _ {1} \partial^ {2} g ^ {i} / \partial s _ {i} \partial s _ {j} - b _ {2} \partial^ {2} g ^ {j} / \partial s _ {i} \partial s _ {j}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} \geq 0,
$$

where the last inequality follows since $\partial ^ { 2 } g ^ { i } / \partial s _ { i } \partial s _ { j } \leq 0$ . Hence $\partial H _ { i } / \partial s _ { j } > 0$ since ${ \bar { \partial ^ { 2 } } } f ^ { i } / { \bar { \partial t _ { i } } } { \partial y _ { j } } { \le 0 }$ . The above derivatives help us establish the comparative statics results with respect to $s _ { j } .$

(ii), (iii) In a similar manner, total differentiation of Equations (5) and (6) with respect to $t _ { j }$ yields

$$
\binom{\frac {d s _ {i}}{d t _ {j}}}{\frac {d t _ {i}}{d t _ {j}}} = - M ^ {- 1} \binom{\frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial t _ {j}}}{\frac {\partial H _ {i}}{\partial t _ {j}}}.
$$

It is easy to show that $\partial ^ { 2 } p _ { i } / \partial s _ { i } \partial t _ { j } = 0$ and

$$
\frac {\partial H _ {i}}{\partial t _ {j}} = 2 b _ {1} \frac {\partial p _ {i}}{\partial t _ {j}} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial t _ {j}} - \lambda_ {c} s _ {j} \frac {\partial^ {2} f ^ {i}}{\partial t _ {i} \partial y _ {j}}.
$$

Since $\partial ^ { 2 } p _ { i } / \partial t _ { i } \partial t _ { i } = 0$ and $\partial ^ { 2 } f ^ { i } / \partial t _ { i } \partial y _ { j } \leq 0 ,$ a sufficient condition for $\partial H _ { i } / \partial t _ { j } ^ { ' } > 0$ is that $\partial p _ { i } / \partial t _ { j } > 0$ . Further,

$$
\frac {\partial p _ {i}}{\partial t _ {j}} = \frac {(2 b _ {1} (\lambda_ {d} s _ {j} - \alpha) + b _ {2})}{4 b _ {1} ^ {2} - b _ {2} ^ {2}}.
$$

Hence the above is nonnegative as long as $\alpha \leq \lambda _ { d } s _ { j } +$ $b _ { 2 } / ( 2 b _ { 1 } )$ . By requiring that $\alpha \ \leq \ \bar { \alpha } ,$ , we guarantee that $\partial p _ { i } / \partial t _ { i } > 0$ for both firms. As a result, $\partial H _ { i } / \partial t _ { j }$ is positive for both firms, and reaction functions are upward sloping w.r.t. $t _ { i } ~ ( \mathrm { i . e . } , ~ \partial s _ { i } / \partial t _ { i } > 0$ and $\partial t _ { i } / \partial t _ { i } > 0 )$ . Note that the condition $\omega \leq \overline { { \alpha } }$ is stronger than necessary since $\partial H _ { i } / \partial t _ { j }$ can be positive even when $\partial p _ { i } / \partial t _ { j } < 0$ . 

Proof of Proposition 3. (i) Similar to the Proof of Proposition 2, upon total differentiation of Equations (5) and (6), we get the following set of equations:

$$
\frac {\partial^ {2} p _ {i}}{\partial s _ {i} ^ {2}} d s _ {i} + \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial t _ {i}} d t _ {i} + \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial b _ {1}} d b _ {1} = 0,\tag{25}
$$

$$
\frac {\partial H _ {i}}{\partial s _ {i}} d s _ {i} + \frac {\partial H _ {i}}{\partial t _ {i}} d t _ {i} + \frac {\partial H _ {i}}{\partial b _ {1}} d b _ {1} = 0.\tag{26}
$$

The set of two simultaneous equations for each firm yields

$$
\binom{\frac {d s _ {i}}{d b _ {1}}}{\frac {d t _ {i}}{d b _ {1}}} = - M ^ {- 1} \binom{\frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial b _ {1}}}{\frac {\partial H _ {i}}{\partial b _ {1}}}.
$$

$$
\frac {\partial H _ {i}}{\partial b _ {1}} = 2 p _ {i} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} \frac {\partial p _ {i}}{\partial b _ {1}} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial b _ {1} \partial t _ {i}}.
$$

Now

$$
\begin{array}{c} \frac {\partial p _ {i}}{\partial t _ {i}} = \frac {2 b _ {1} + b _ {2} (\lambda_ {d} s _ {i} - \alpha)}{4 b _ {1} ^ {2} - b _ {2} ^ {2}}, \\ \frac {\partial p _ {i}}{\partial b _ {1}} = - \frac {2 (4 b _ {1} p _ {i} - (a _ {i} + B _ {i}))}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} <   0, \\ \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial b _ {1}} = \frac {2 (4 b _ {1} ^ {2} - b _ {2} ^ {2}) - 8 b _ {1} (2 b _ {1} + b _ {2} (\lambda_ {d} s _ {i} - \alpha))}{(4 b _ {1} ^ {2} - b _ {2} ^ {2}) ^ {2}} <   0. \end{array}
$$

The above expressions imply that

$$
\frac {\partial H _ {i}}{\partial b _ {1}} <   0.
$$

In addition, $\partial ^ { 2 } p _ { i } / \partial s _ { i } \partial b _ { 1 } = - 2 \partial g ^ { i } / \partial s _ { i } < 0 .$ . As a result, the comparative statics with respect to $b _ { 1 }$ are determined unambiguously $( \mathrm { i . e . , ~ } \partial s _ { i } / \partial b _ { 1 } < 0 , \partial t _ { i } / \partial b _ { 1 } < 0 )$

(ii) For the comparative statics with respect to $b _ { 2 } ,$ we need to establish the signs of $\partial H _ { i } / \partial b _ { 2 }$ and $\partial ^ { 2 } p _ { i } \bar { / } \partial s _ { i } \partial b _ { 2 }$ . Here,

$$
\begin{array}{c} \frac {\partial H _ {i}}{\partial b _ {2}} = 2 b _ {1} \frac {\partial p _ {i}}{\partial b _ {2}} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial b _ {2} \partial t _ {i}}, \quad \text { where } \\ \frac {\partial p _ {i}}{\partial b _ {2}} = \frac {a _ {j} + B _ {j}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} + \frac {2 b _ {2} p _ {i}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} > 0. \end{array}
$$

Similarly, from (21), the expressions for the derivatives of the equilibrium prices evaluated at the symmetric equilibrium are given as follows:

$$
\begin{array}{c} \frac {\partial p _ {i}}{\partial t _ {i}} = \frac {2 b _ {1} + b _ {2} (\lambda_ {d} s _ {i} - \alpha)}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} > 0, \\ \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial b _ {2}} = \frac {\lambda_ {d} s _ {i} - \alpha}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} + \frac {2 b _ {2} (2 b _ {1} + b _ {2} (\lambda_ {d} s _ {i} - \alpha))}{(4 b _ {1} ^ {2} - b _ {2} ^ {2}) ^ {2}} \\ = \frac {4 b _ {1} b _ {2} + (4 b _ {1} ^ {2} + b _ {2} ^ {2}) (\lambda_ {d} s _ {i} - \alpha)}{(4 b _ {1} ^ {2} - b _ {2} ^ {2}) ^ {2}}. \end{array}
$$

Under the assumption that $\alpha \leq \bar { \alpha } ,$ the above second derivative is positive. In addition,

$$
\begin{array}{r l} \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial b _ {2}} = \frac {\lambda_ {d} t _ {i} - \partial g ^ {j} / \partial s _ {i}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} \\ & + \frac {(- 2 b _ {1} \partial g ^ {i} / \partial s _ {i} - b _ {2} \partial g ^ {j} / \partial s _ {i} + b _ {2} \lambda_ {d} t _ {i}) 2 b _ {2}}{(4 b _ {1} ^ {2} - b _ {2} ^ {2}) ^ {2}} > 0, \end{array}
$$

because at the equilibrium, the second term vanishes from Equation (22). The comparative statics with respect to $b _ { 2 }$ are implied by the above derivatives. Note, once again, that the assumption $\alpha \leq \overline { { \alpha } }$ is stronger than necessary, since $\partial H _ { i } / \partial b _ { 2 }$ can be positive even when $\partial ^ { 2 } p _ { i } / \partial t _ { i } \partial b _ { 2 }$ is negative. <sup></sup>

Proof of Proposition 4. Proof of Proposition 4 is similar to 2 and 3 above, and hence it is not repeated for brevity. We only show the relevant expressions.

$$
\begin{array}{r} \frac {\partial H _ {i}}{\partial a _ {i}} = 2 b _ {1} \frac {\partial p _ {i}}{\partial a _ {i}} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial a _ {i}}, \\ \frac {\partial H _ {i}}{\partial a _ {j}} = 2 b _ {1} \frac {\partial p _ {i}}{\partial a _ {j}} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial a _ {j}}. \end{array}
$$

Here, $\partial p _ { i } / \partial a _ { i } = 2 b _ { 1 } / ( 4 b _ { 1 } ^ { 2 } - b _ { 2 } ^ { 2 } )$ and $\partial p _ { i } / \partial a _ { j } = b _ { 2 } / ( 4 b _ { 1 } ^ { 2 } - b _ { 2 } ^ { 2 } )$ This implies that

$$
\frac {\partial p _ {i}}{\partial a _ {i} \partial t _ {i}} = \frac {\partial^ {2} p _ {i}}{\partial a _ {j} \partial t _ {i}} = 0.
$$

Hence

$$
\frac {\partial H _ {i}}{\partial a _ {i}} = 2 b _ {1} \frac {\partial p _ {i}}{\partial a _ {i}} \frac {\partial p _ {i}}{\partial t _ {i}} > 0
$$

and

$$
\frac {\partial H _ {i}}{\partial a _ {j}} = 2 b _ {1} \frac {\partial p _ {i}}{\partial a _ {j}} \frac {\partial p _ {i}}{\partial t _ {i}} > 0.
$$

(i)

$$
\frac {\partial H _ {i}}{\partial \lambda_ {d}} = 2 b _ {1} \frac {\partial p _ {i}}{\partial \lambda_ {d}} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial \lambda_ {d}}.
$$

Now

$$
\frac {\partial p _ {i}}{\partial \lambda_ {d}} = \frac {2 b _ {1} s _ {j} t _ {j} + b _ {2} t _ {i} s _ {i}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}},
$$

$$
\frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial \lambda_ {d}} = \frac {b _ {2} t _ {i}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} > 0,
$$

$$
\frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial \lambda_ {d}} = \frac {b _ {2} s _ {i}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} > 0.
$$

Hence $\partial s _ { i } / \partial \lambda _ { d } > 0 , \partial t _ { i } / \partial \lambda _ { d } > 0$ . In a similar manner, it can be shown that $\partial s _ { i } / \partial \lambda _ { c } > 0 , \partial t _ { i } / \partial \lambda _ { c } > 0$ since

$$
\frac {\partial H _ {i}}{\partial \lambda_ {c}} = - \left[ \frac {\partial^ {2} f ^ {i}}{\partial t _ {i} \partial y _ {j}} \right] t _ {j} s _ {j} > 0.\tag{ii}
$$

$$
\begin{array}{c} \frac {\partial H _ {i}}{\partial \alpha} = 2 b _ {1} \frac {\partial p _ {i}}{\partial \alpha} \frac {\partial p _ {i}}{\partial t _ {i}} + 2 b _ {1} p _ {i} \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial \alpha}, \quad \text {where} \\ \frac {\partial p _ {i}}{\partial \alpha} = \frac {- (2 b _ {1} t _ {j} + b _ {2} t _ {i})}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} <   0, \\ \frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial \alpha} = - \frac {b _ {2}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} <   0, \\ \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial \alpha} = 0. \end{array}
$$

The above inequalities imply that $\partial s _ { i } / \partial \alpha ~ < ~ 0$ and $\partial t _ { i } / \partial \alpha < 0 .$ 

Proof of Proposition 5. Solving for the inverse demand functions from (1) and (3),

$$
p _ {i} = \frac {b _ {1} a _ {i} + b _ {2} a _ {j} - (b _ {1} q _ {i} + b _ {2} q _ {j}) + b _ {1} B _ {i} + b _ {2} B _ {j}}{b _ {1} ^ {2} - b _ {2} ^ {2}}.
$$

At the symmetric equilibrium we have

$$
p = \frac {(a + B - q)}{(b _ {1} - b _ {2})},
$$

where $B = t ( 1 - \alpha ) + \lambda _ { d } t s - g ^ { i } ( s , s )$ . Hence, total welfare is equal to

$$
S W = \int_ {0} ^ {q ^ {*}} 2 \frac {(a + B - q)}{b _ {1} - b _ {2}} d q - 2 f ^ {i} (t, \lambda_ {c} t s),
$$

where $q ^ { * }$ is the quantity at the market equilibrium. Taking the derivative w.r.t. $s ,$ the optimal $s ^ { S W }$ is given by the solution to

$$
\begin{array}{r l} \frac {\partial S W}{\partial s} = & \frac {\partial}{\partial s} \bigg (\int_ {0} ^ {q ^ {*}} 2 \frac {(a + B - q)}{b _ {1} - b _ {2}} d q - 2 f ^ {i} (t, \lambda_ {c} t s) \bigg) = 0 \\ \Leftrightarrow & \frac {2}{b _ {1} - b _ {2}} \int_ {0} ^ {q ^ {*}} \frac {\partial B}{\partial s} d q + 2 \bigg (\frac {a + B - q ^ {*}}{b _ {1} - b _ {2}} \bigg) \frac {\partial q ^ {*}}{\partial s} - 2 \lambda_ {c} t \frac {\partial f ^ {i}}{\partial y _ {j}} = 0, \end{array}
$$

by using Leibnitz theorem.

At the symmetric equilibrium, $q ^ { * } = b _ { 1 } p ^ { * } = b _ { 1 } ( a + B ) /$ $( 2 b _ { 1 } - b _ { 2 } )$ and $\partial q ^ { * } / \partial s = \bar { b } _ { 1 } / ( 2 b _ { 1 } - b _ { 2 } ) \dot { ( \partial B / \partial s ) } .$ , where $\partial B / \partial s =$ $\lambda _ { d } t - ( \partial g ^ { i } / \partial s _ { i } + \partial \dot { g } ^ { i } / \partial s _ { j } )$

Hence, we can write this equation as

$$
\frac {\partial S W}{\partial s} = 2 \bigg [ \frac {b _ {1} (a + B) (3 b _ {1} - 2 b _ {2})}{(2 b _ {1} - b _ {2}) ^ {2} (b _ {1} - b _ {2})} \bigg ] \frac {\partial B}{\partial s} - 2 \lambda_ {c} t \frac {\partial f ^ {i}}{\partial y _ {j}} = 0.\tag{27}
$$

Because the last term is always positive, it follows that for a fixed $t , \ s ^ { S W }$ is bigger than the value satisfying $\partial B / \partial s = 0 .$ . When $\partial B / \partial s = 0 , \ \lambda _ { d } t - ( \partial g ^ { i } / \partial s _ { i } + \partial g ^ { j } / \partial s _ { i } ) = 0 .$ Recall from (22) that in the market equilibrium the condition, which determines the optimal amount of sharing, is given by $\lambda _ { d } t - ( ( 2 b _ { 1 } / b _ { 2 } ) ( \partial g ^ { i } / \partial s \stackrel { . } { _ { i } } ) + \partial g ^ { j } / \partial s _ { i } ) = 0$ . Since $2 b _ { 1 } > b _ { 2 } ,$ it follows that for a fixed $t , \ s ^ { N E }$ is smaller than the value satisfying $\partial B / \partial S = 0$ . Hence $s ^ { N E } < s ^ { S W }$

In a similar manner, differentiating SW with respect to t as above, we obtain

$$
\frac {\partial S W}{\partial t} = \frac {\partial}{\partial t} \left(\int_ {0} ^ {q ^ {*}} 2 \frac {(a + B - q)}{b _ {1} - b _ {2}} d q - 2 f ^ {i} (t, \lambda_ {c} t s)\right).
$$

By using Leibnitz theorem and then rearranging terms, we obtain the following FOC for t

$$
\frac {b _ {1} (3 b _ {1} - 2 b _ {2}) (a + B)}{(2 b _ {1} - b _ {2}) ^ {2} (b _ {1} - b _ {2})} \frac {\partial B}{\partial t} - \left(\frac {\partial f ^ {i}}{\partial t _ {i}} + \lambda_ {c} s \frac {\partial f ^ {i}}{\partial y _ {j}}\right) = 0,\tag{28}
$$

where $\partial B / \partial t = 1 - \alpha + \lambda _ { d } s ,$ . The solution to this equation determines the optimal level of security technology investment. Compare this to the optimal level of technology investment under the firms’ individual profit maximization that solves the following equation:

$$
2 b _ {1} p \frac {\partial p _ {i}}{\partial t _ {i}} = \frac {\partial f ^ {i}}{\partial t _ {i}}.
$$

At the symmetric equilibrium, $p = ( a + B ) / ( 2 b _ { 1 } - b _ { 2 } )$ and $\partial p _ { i } / \partial t _ { i } = ( 2 b _ { 1 } + b _ { 2 } ( \lambda _ { d } s - \alpha ) ) / ( 4 b _ { 1 } ^ { 2 } - b _ { 2 } ^ { 2 } )$ . Hence the FOC at the market equilibrium reduces to

$$
\frac {2 b _ {1} (a + B) (2 b _ {1} + b _ {2} (\lambda_ {d} s - \alpha))}{(2 b _ {1} - b _ {2}) (4 b _ {1} ^ {2} - b _ {2} ^ {2})} - \frac {\partial f ^ {i}}{\partial t _ {i}} = 0.\tag{29}
$$

When $\alpha \leq \overline { { \alpha } } ,$ , it can be shown that $( 3 b _ { 1 } - 2 b _ { 2 } ) ( 2 b _ { 1 } + b _ { 2 } ) ( 1 - \alpha +$ $\lambda _ { d } s ) > 2 ( b _ { 1 } - b _ { 2 } ) ( 2 b _ { 1 } + b _ { 2 } ( \lambda _ { d } s - \alpha ) )$ . Hence, a comparison of Equations (28) and (29) implies that for a fixed level of $s ,$ the socially optimal level of technology investment $t ^ { S W }$ exceeds that obtained at the market equilibrium under individual profit maximization, $t ^ { N E }$ . When both s and t are chosen optimally, the above inequalities are reinforced since s and t are strategic complements when $\alpha \leq \overline { { \alpha } }$

From Equations (13) and (14), we have the following:

$$
\frac {\partial \Pi^ {J P}}{\partial s} = \frac {4 b _ {1} (a + B)}{(2 b _ {1} - b _ {2}) ^ {2}} \left[ \lambda_ {d} t - \left(\frac {\partial g ^ {i}}{\partial s _ {i}} + \frac {\partial g ^ {i}}{\partial s _ {j}}\right) \right] - 2 \lambda_ {c} t \frac {\partial f ^ {i}}{\partial y _ {j}} = 0.\tag{30}
$$

$$
\frac {\partial \Pi^ {J P}}{\partial t} = \frac {4 b _ {1} (a + B) (1 - \alpha + \lambda_ {d} s)}{(2 b _ {1} - b _ {2}) ^ {2}} - 2 \left[ \frac {\partial f ^ {i}}{\partial t _ {i}} + \lambda_ {c} s \frac {\partial f ^ {i}}{\partial y _ {j}} \right] = 0.\tag{31}
$$

A comparison of (30) with Equations (12, 27) and (31) with Equations (28) and (29) when $\alpha \leq \overline { { \alpha } } ,$ , implies that the security technology investment and security informationsharing levels under joint profit maximization lies in between social welfare maximization and the market (Bertrand-Nash) equilibrium. Hence, it follows that $t ^ { N E } <$ $\dot { t } ^ { J P } < t ^ { S P }$ and $\begin{array} { r } { s ^ { N \dot { E } } < \dot { s } ^ { J P } < s ^ { S P } } \end{array}$ 

Proof of Proposition 6. The proof follows from comparing Equations (15) and (16) with Equations (5) and (6), respectively. The additional terms in Equations (15) and (16) are the Stackelberg effects and prove the result. Since $( \partial p _ { i } / \partial s _ { i } ) ( \partial s _ { i } / \partial s _ { i } ) > 0$ and when $\alpha \leq \bar { \alpha } , ( \partial p _ { i } / \partial t _ { j } ) ( \partial t _ { j } / \partial t _ { i } ) > 0$ at the levels of simultaneous mode game, to get to the optimum, $( s _ { i } ^ { * } , ~ s _ { j } ^ { * } )$ and $( t _ { i } ^ { * } , ~ t _ { j } ^ { * } )$ must be higher. <sup></sup>

Proof of Proposition 7. (i) The optimal price in this case is given by

$$
p _ {i} = \frac {2 b _ {1} (a _ {i} + B _ {i}) + b _ {2} (a _ {j} + B _ {j}) + 2 b _ {1} ^ {2} F _ {i} + b _ {1} b _ {2} F _ {j}}{(4 b _ {1} ^ {2} - b _ {2} ^ {2})};
$$

We first derive the relevant expressions here.

$$
\begin{array}{r l r} & {\frac {\partial B _ {i}}{\partial t _ {i}} = 1, \quad} & {\frac {\partial B _ {j}}{\partial t _ {i}} = \lambda_ {d} s _ {i} - \alpha , \quad \frac {\partial B _ {i}}{\partial s _ {i}} = - \frac {\partial g ^ {i}}{\partial s _ {i}},} \\ & & {\frac {\partial B _ {j}}{\partial s _ {i}} = \lambda_ {d} t _ {i} - \frac {\partial g ^ {j}}{\partial s _ {i}}.} \end{array}
$$

Next,

$$
\begin{array}{r l r} & {\frac {\partial F _ {i}}{\partial s _ {i}} = 0, \quad} & {\frac {\partial F _ {i}}{\partial s _ {j}} = - \hat {\lambda} t _ {j} \delta (t _ {i}), \quad} & {\frac {\partial F _ {i}}{\partial t _ {i}} = (c - \hat {\lambda} t _ {j} s _ {j}) \delta^ {'} (t _ {i}),} \\ & & {\frac {\partial F _ {j}}{\partial s _ {i}} = - \hat {\lambda} t _ {i} \delta (t _ {j}), \quad} & {\frac {\partial F _ {j}}{\partial t _ {i}} = - \hat {\lambda} s _ {i} \delta (t _ {j}).} \end{array}
$$

As well,

$$
\frac {\partial p _ {i}}{\partial s _ {i}} = \frac {2 b _ {1} (- \partial g ^ {i} / \partial s _ {i}) + b _ {2} (\lambda_ {d} t _ {i} - \partial g ^ {j} / \partial s _ {i}) - b _ {1} b _ {2} \hat {\lambda} t _ {i} \delta (t _ {j})}{4 b _ {1} ^ {2} - b _ {2} ^ {2}}.
$$

Comparing this to Equation (22), it is immediate that spillovers on the marginal cost side reduce willingness to share compared to spillovers on the fixed cost side.

(ii) Next, we have the following:

$$
\begin{array}{c} \frac {\partial p _ {i}}{\partial t _ {i}} = \frac {2 b _ {1} + b _ {2} (\lambda_ {d} s _ {i} - \alpha) + 2 b _ {1} ^ {2} (c - \hat {\lambda} s _ {j} t _ {j}) \delta^ {'} (t _ {i}) - b _ {1} b _ {2} \hat {\lambda} s _ {i} \delta (t _ {j})}{4 b _ {1} ^ {2} - b _ {2} ^ {2}}, \\ \frac {\partial p _ {i}}{\partial \hat {\lambda}} = \frac {- (2 b _ {1} ^ {2} t _ {j} s _ {j} \delta (t _ {i}) + b _ {1} b _ {2} t _ {i} s _ {i} \delta (t _ {j}))}{4 b _ {1} ^ {2} - b _ {2} ^ {2}}, \\ \frac {\partial F _ {i}}{\partial \hat {\lambda}} = - s _ {j} t _ {j} \delta (t _ {i}). \end{array}
$$

From the FOCs (17) and (18), we can derive the following set of simultaneous implicit equations:

$$
\left( \begin{array}{c} \frac {d s _ {i}}{d \hat {\lambda}} \\ \frac {d t _ {i}}{d \hat {\lambda}} \end{array} \right) = - M ^ {- 1} \left( \begin{array}{c} \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial \hat {\lambda}} \\ \frac {\partial H _ {i}}{\partial \hat {\lambda}} \end{array} \right),
$$

where

$$
M = \left( \begin{array}{c c} \frac {\partial^ {2} p _ {i}}{\partial s _ {i} ^ {2}} & \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial t _ {i}} \\ \frac {\partial H _ {i}}{\partial s _ {i}} & \frac {\partial H _ {i}}{\partial t _ {i}} \end{array} \right).
$$

The respective terms within the matrix and their signs are shown below. First, we have

$$
\begin{array}{r} \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial \hat {\lambda}} = \frac {- b _ {1} b _ {2} t _ {i} \delta (t _ {j})}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} <   0, \\ \frac {\partial H _ {i}}{\partial \hat {\lambda}} = 2 b _ {1} \bigg [ \bigg (\frac {\partial p _ {i}}{\partial \hat {\lambda}} - \frac {\partial F _ {i}}{\partial \hat {\lambda}} \bigg) \bigg (\frac {\partial p _ {i}}{\partial t _ {i}} - \frac {\partial F _ {i}}{\partial t _ {i}} \bigg) \\ + 2 b _ {1} (p _ {i} - F _ {i}) \bigg (\frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial \hat {\lambda}} - \frac {\partial^ {2} F _ {i}}{\partial t _ {i} \partial \hat {\lambda}} \bigg) \bigg ]. \end{array}
$$

Now

$$
\left(\frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial \hat {\lambda}} - \frac {\partial^ {2} F _ {i}}{\partial t _ {i} \partial \hat {\lambda}}\right) = \left[ 2 b _ {1} ^ {2} t _ {j} s _ {j} \delta^ {'} (t _ {i}) - b _ {1} b _ {2} s _ {i} \delta (t _ {j}) - b _ {2} ^ {2} t _ {j} s _ {j} \delta^ {'} (t _ {i}) \right]
$$

$$
\cdot (4 b _ {1} ^ {2} - b _ {2} ^ {2}) ^ {- 1} > 0,\tag{32}
$$

$$
\frac {\partial p _ {i}}{\partial t _ {i}} - \frac {\partial F _ {i}}{\partial t _ {i}} = \left[ 2 b _ {1} + b _ {2} (\lambda_ {d} s _ {i} - \alpha) - (2 b _ {1} ^ {2} + b _ {2} ^ {2}) (c - \hat {\lambda} s _ {j} t _ {j}) \delta^ {'} (t _ {i}) \right.
$$

$$
\left. \left. - b _ {1} b _ {2} \hat {\lambda} s _ {i} \delta (t _ {j}) \right] \cdot \left(4 b _ {1} ^ {2} - b _ {2} ^ {2}\right) ^ {- 1}. \right.\tag{33}
$$

Next, we show that

$$
\begin{array}{c} \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial s _ {j}} = \frac {- 2 b _ {1} \partial^ {2} g ^ {i} / \partial s _ {i} \partial s _ {j} - b _ {2} \partial^ {2} g ^ {j} / \partial s _ {i} \partial s _ {j}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} > 0, \\ \frac {\partial^ {2} p _ {i}}{\partial s _ {i} \partial t _ {j}} = \frac {- b _ {1} b _ {2} t _ {i} \hat {\lambda} \delta^ {\prime} (t _ {j})}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} <   0, \\ \frac {\partial H _ {i}}{\partial s _ {i}} = 2 b _ {1} (p _ {i} - F _ {i}) \bigg (\frac {\partial^ {2} p _ {i}}{\partial t _ {i} \partial s _ {i}} - \frac {\partial^ {2} F _ {i}}{\partial t _ {i} \partial s _ {i}} \bigg) \\ + 2 b _ {1} \bigg (\frac {\partial p _ {i}}{\partial s _ {i}} - \frac {\partial F _ {i}}{\partial s _ {i}} \bigg) \bigg (\frac {\partial p _ {i}}{\partial t _ {i}} - \frac {\partial F _ {i}}{\partial t _ {i}} \bigg). \end{array}
$$

From the FOC (17), we have $\partial p _ { i } / \partial s _ { i } = 0 = \partial F _ { i } / \partial s _ { i }$ and $\partial ^ { 2 } p _ { i } / \partial t _ { i } \partial s _ { i } = b _ { 2 } ( \lambda _ { d } - b _ { 1 } \hat { \lambda } \delta ( t _ { j } ) )$ . Hence

$$
\frac {\partial H _ {i}}{\partial s _ {i}} = 2 b _ {1} (p _ {i} - F _ {i}) b _ {2} (\lambda_ {d} - b _ {1} \hat {\lambda} \delta (t _ {j})).
$$

Under the restriction of the second-order conditions, $\partial H _ { i } / \partial t _ { i } < 0$ and the determinant <sub></sub>M<sub></sub> must be positive. However, because we are unable to sign $( \lambda _ { d } - b _ { 1 } \hat { \lambda } \delta ( t _ { j } ) )$ unambiguously, we do not have the signs of all the terms in the matrix. As is immediate, it depends on the relative ratio of the spillovers parameters, $\lambda _ { d } / \hat { \lambda }$ 

## Appendix B. Fostering Optimal Levels of Information Sharing

Our derivation so far indicates that even though some sharing of information arises at the market equilibrium, its level falls short of the one that maximizes social welfare. It is possible, however, for the government to design a Vickrey-Clarke-Groves (VCG) mechanism (Vickrey 1961, Clarke 1971, Groves 1973) that will provide incentives to market participants to select the socially optimal levels of sharing and investment, derived in the previous section.

Suppose that the government provides a subsidy to firm i equal to the total consumer surplus generated from product $i , C S _ { i }$ as well as the total social welfare (sum of consumer and producer surplus) generated from product $j , T S _ { j } .$ Note that this subsidy represents the components of welfare surpluses that a firm neglects to consider when it maximizes its own profits. The subsidy $B _ { i }$ is evaluated at the Bertrand levels of prices and quantities, calculated from (21) as follows:

$$
p _ {i} ^ {*} = \frac {a}{2 b _ {1} - b _ {2}} + \frac {2 b _ {1} B _ {i} + b _ {2} B _ {j}}{4 b _ {1} ^ {2} - b _ {2} ^ {2}} \quad \text { and } \quad q _ {i} ^ {*} = b _ {1} p _ {i} ^ {*}.\tag{34}
$$

Hence

$$
\begin{array}{r l} & B ^ {i} (s _ {i}, t _ {i}, s _ {j}, t _ {j}) = C S _ {i} + T S _ {j} \\ & \qquad = \bigg [ \int_ {0} ^ {q _ {j} ^ {*}} \int_ {0} ^ {q _ {i} ^ {*}} F _ {i} (q _ {i}, q _ {j}) d q _ {i} d q _ {j} - p _ {i} ^ {*} q _ {i} ^ {*} \bigg ] \\ & \qquad + \bigg [ \int_ {0} ^ {q _ {i} ^ {*}} \int_ {0} ^ {q _ {j} ^ {*}} F _ {j} (q _ {i}, q _ {j}) d q _ {j} d q _ {i} - f (t _ {j}, y _ {i}) \bigg ]. \end{array}\tag{35}
$$

To raise revenues to finance the subsidy, the government imposes also a fixed tax on each firm equal to the above subsidy expression evaluated at the social welfare maximizing extent of sharing and security investment. The fixed tax T for each firm is equal, therefore, to

$$
T = B ^ {i} (s ^ {S W}, t ^ {S W}, s ^ {S W}, t ^ {S W}).\tag{36}
$$

The above mechanism induces welfare-maximizing behavior without costing anything to the government, because at the equilibrium the levels of the subsidy and tax are identical (a similar scheme is proposed in Gordon et al. 2003).

The above mechanism assumes that the government has access to the same information as do the firms. In particular, in designing the subsidy tax schedule, it is fully informed of the values of the intercept of the demand a and the spillover parameters $\lambda _ { d }$ and $\lambda _ { c }$ . With full information it is well known that a regulator can implement the “first-best” outcome because it does not have to utilize any “revelation mechanism.” In fact, the government can simply choose the optimal level of security investment itself and dictate it to the firms. We have introduced the more complex mechanism described above as a benchmark to be modified as needed when the government has only partial information about the environment.

To investigate whether inducing welfare maximization is feasible with asymmetric information, we consider now the possibility that the firms have private information about the values of the parameters. For simplicity, assume that the cost spillover parameter $\lambda _ { c }$ is the only one that is privately observed by the firms. Specifically, each firm can privately observe the extent to which the information revealed by its competitor is conducive to reducing its costs of investment in security technology. Let $\lambda _ { c } ^ { i }$ designate the cost spillover parameter benefiting firm i, implying that its costs of investment are $f ^ { i } ( t _ { i } , y _ { j } )$ , where $y _ { j } = \lambda _ { c } ^ { i } s _ { j } t _ { j }$ . Assume also that $\lambda _ { c } ^ { 1 }$ and $\lambda _ { c } ^ { 2 }$ are uncertain and that their values are determined independently of each other according to an identical uniform distribution defined over the support $[ \underline { { \lambda } } _ { c } , \bar { \lambda } _ { c } ]$ . Using a direct mechanism, as proposed by Vickrey (1961), Clarke (1971), and Groves (1973), assume that in the first stage the firms deliver messages about the spillover parameters, that we designate by $\hat { \lambda } _ { c } ^ { i } ,$ and in the second stage the government designs the subsidy tax mechanism contingent upon those messages.

Note that the expression we derived above for the subsidy awarded to firm i depends upon the costs incurred by firm $j ,$ which, in turn, depends on the value of $\lambda _ { c } ^ { j }$ . Hence with asymmetric information, the government will have to rely on the report $\hat { \lambda } _ { c } ^ { j }$ delivered by $j$ about its spillover parameter. Designate by $\hat { f } ^ { j } ( t _ { j } , y _ { i } )$ the reported costs of firm $j$ as implied by the message $\hat { \lambda } _ { c } ^ { j }$ . Similarly, designate by $\hat { B } ^ { i } ( s _ { i } , \textbf { } t _ { i } , \textbf { } s _ { j } , \textbf { } \bar { t } _ { j } )$ the subsidy awarded to firm i when reported costs of j replace actual costs.

The expression for the tax imposed on i will have to be modified as well, because the social welfare levels of sharing and investment are now functions of the reports delivered by the firms (specifically, $\hat { s } _ { i } ^ { S W } = s _ { i } ^ { S W } ( \hat { \lambda } _ { c } ^ { i } , \hat { \lambda } _ { c } ^ { j } )$ and $\hat { T } _ { i } ^ { S W } = t _ { i } ^ { S W } ( \mathcal { \tilde { \lambda } } _ { c } ^ { i } , \mathcal { \hat { \lambda } } _ { c } ^ { j } ) ;$ . We designate by

$$
\widehat {T} _ {i} = \widehat {B} ^ {i} (\widehat {s} ^ {S W}, \widehat {T} ^ {S W}, \widehat {s} ^ {S W}, \widehat {T} ^ {S W})\tag{37}
$$

the fixed tax imposed on firm i as a function of the messages delivered by the firms. Firm i chooses its levels of sharing and investment as well as its report to the government to maximize its objective defined as follows:

$$
\begin{array}{c} \max _ {s _ {i}, t _ {i}, \hat {\lambda} _ {c} ^ {i}} V ^ {i} (s _ {i}, t _ {i}, \hat {\lambda} _ {c} ^ {i}, s _ {j}, t _ {j}) \\ = b _ {1} (p _ {i} ^ {*}) ^ {2} + E _ {\hat {\lambda} _ {c} ^ {j}} \bigl \{\widehat {B} ^ {i} (s _ {i}, t _ {i}, s _ {j}, t _ {j}) - \widehat {T} ^ {i} \bigr \}, \end{array}\tag{38}
$$

where $p _ { i } ^ { * }$ remains as defined in (34) for an environment with symmetric information (since the value of $\lambda _ { c } ^ { i }$ affects only fixed costs, it does not influence pricing decisions for fixed levels of sharing and investments by the firms). Note that firm i cannot observe the message $\hat { \lambda } _ { c } ^ { j }$ delivered by its competitor, given that this message depends on the realization of the stochastic variable $\lambda _ { c } ^ { j } .$ . As a result, we include the expected value operator in $V ^ { i }$ to evaluate the net subsidy that i can expect.

The above maximization problem is constrained by individual rationality (IR) and incentive compatibility (IC) constraints. The individual rationality constraint requires that each firm is willing to participate in the subsidy tax scheme, and the incentive compatibility constraint implies that each firm has an incentive to truthfully reveal its private information. In stating the former constraint, it is important to explicitly define the “outside option” of each firm. Assuming that the firm can decline to participate in the subsidy tax scheme and still compete freely in the market under consideration, the IR constraint becomes

$$
b _ {1} (p _ {i} ^ {*}) ^ {2} + E _ {\hat {\lambda} _ {c} ^ {j}} \{\widehat {B} ^ {i} (s _ {i}, t _ {i}, s _ {j}, t _ {j}) - \widehat {T} ^ {i} \} \geq b _ {1} (p _ {i} ^ {*}) ^ {2},
$$

or

$$
E _ {\hat {\lambda} _ {c} ^ {j}} \{\widehat {B} ^ {i} (s _ {i}, t _ {i}, s _ {j}, t _ {j}) - \widehat {T} ^ {i} \} \geq 0.\tag{IR1}
$$

In contrast, assuming that the firm is required to be subject to the subsidy tax scheme, its “outside option” is defined by the profits it can generate outside of the market under consideration, which we normalize to be equal to zero. The IR constraint in this case becomes

$$
b _ {1} (p _ {i} ^ {*}) ^ {2} + E _ {\hat {\lambda} _ {c} ^ {j}} \{\widehat {B} ^ {i} (s _ {i}, t _ {i}, s _ {j}, t _ {j}) - \widehat {T} ^ {i} \} \geq 0.\tag{IR2}
$$

Borrowing terminology that was used in the mechanism design literature, the IR constraints defined above characterize “interim individual rationality” rather than “ex post individual rationality” constraints (for every possible value of $\lambda _ { c } ^ { j } )$

To guarantee that truthful revelation is a weakly dominant strategy, the following IC constraint is implied:

$$
\begin{array}{c} V ^ {i} (s _ {i}, t _ {i}, \lambda_ {c} ^ {i}, s _ {j}, t _ {j}) \geq V ^ {i} (s _ {i}, t _ {i}, \hat {\lambda} _ {c} ^ {i}, s _ {j}, t _ {j}); \\ \text { for all } \hat {\lambda} _ {c} ^ {i}, \lambda_ {c} ^ {i} \in [ \underline {{\lambda}} _ {c}, \bar {\lambda} _ {c} ]. \end{array}\tag{IC}
$$

It is noteworthy that the objective of firm i is not a direct function of the true realization of $\lambda _ { c } ^ { i } .$ , only of its report. Specifically, $\partial V ^ { i } / \partial \lambda _ { c } ^ { i } = 0 .$ . As a result, the government can design a mechanism with truthful revelation that will leave each firm without any informational rents. Hence the interim individual rationality constraints (IR1) or (IR2) are binding irrespective of the realization of $\lambda _ { c } ^ { i }$ (see Myerson 1979, 1981). This implies that the government can, once again, implement the budget balancing, “first-best” outcome in spite of asymmetric information.

It is important to note that the above result is valid only if the government can prevent collusion between the two firms. Achieving the “first-best” outcome with the VCG mechanism (Vickrey 1961, Clarke 1971, Groves 1973) is not feasible when a firm can communicate with its competitor to influence the report it delivers to the government. As well, when firms have access to private information about other parameters of the model except $\lambda _ { c } ^ { i } \ ( a _ { i }$ and $\lambda _ { d } ^ { i } ,$ for instance), the “first-best” outcome is not attainable even when collusion can be prevented. With private information about those other parameters, the objective of each firm depends on its report as well as the true value of its private information. The latter dependence results in the existence of informational rents and possible distortions in the optimal values of sharing and investment that the government can implement with a mechanism that induces truthful revelation. In addition, if interim individual rationality constraints are replaced by ex post rationality constraints, distortions may arise even in our environment when private information pertains only to $\lambda _ { c } ^ { i }$ (this relates to the impossibility theorem derived by Myerson and Satterthwaite 1983).

## References

Anderson, R. 2001. Why information security is hard: An economic perspective. Proc. 17th Annual Comput. Security Appl. Conf. (December).

Bulow, J., J. Geanakoplos, P. Klemperer. 1985. Multimarket oligopoly: Strategic substitutes and complements. J. Political Econom. 93(3) 488–511.

Campbell, K., L. Gordon, M. Loeb, L. Zhou. 2003. The economic cost of publicly announced information security breaches: Empirical evidence from the stock market. J. Comput. Security 11(3) 431–448.

Cavusoglu, H., B. Mishra, S. Raghunathan. 2004. The effect of Internet security breach announcements on market value: Capital market reaction for breached firms and Internet security developers. Internat. J. Electronic Commerce 9(1) 69–105.

Clarke, E. 1971. Multipart pricing of public goods. Public Choice (11) 17–33.

d’Aspremont, C., A. Jacquemin. 1988. Cooperative and noncooperative R&D in a duopoly with spillovers. Amer. Econom. Rev. 78(5) 1133–1137.

Dacey, R. 2003a. Information security: Progress made, but challenges remain to protect federal systems and the nation’s critical infrastructures. U.S. General Accounting Office (GAO), GAO-36-564T (April) 1–75.

Dacey, R. 2003b. Critical infrastructure protection: Challenges for selected agencies and industry sectors. U.S. General Accounting Office (GAO), GAO-03-233 (February) 1–72.

Gal-Or, E. 1985a. Information sharing in oligopoly. Econometrica 53(2) 329–343.

Gal-Or, E. 1985b. First mover and second mover advantages. Internat. Econom. Rev. 26(3) 649–653.

Gordon, L., M. Loeb. 2002. The economics of information security investment. ACM Trans. Inform. System Security 5(4) 438–457.

Gordon, L. A., M. Loeb, W. Lucyshyn. 2003. Sharing information on computer systems security: An economic analysis. J. Accounting Public Policy 22(6) 461–485.

Groves, T. 1973. Incentives in teams. Econometrica 41(4) 617–663.

Groves, T., M. Loeb. 1975. Incentives and public inputs. J. Public Econom. (4) 211–226.

Kamien, M., E. Muller, I. Zhang. 1992. Research joint ventures and R&D cartels. Amer. Econom. Rev. 82(5) 1293–1306.

McGuire, T., R. Staelin. 1983. An industry equilibrium analysis of downstream vertical integration. Marketing Sci. 2(2) 161–192.

Milgrom, P. 1994. Comparing optima: Do simplifying assumptions affect conclusions? J. Political Econom. 102(3) 607–615.

Myerson, R. 1979. Incentive compatibility and bargaining problem. Econometrica 47(1) 61–73.

Myerson, R. 1981. Optimal auction design. Math. Oper. Res. 6 58–73.

Myerson, R., M. Satterthwaite. 1983. Efficient mechanisms for bilateral trading. J. Econom. Theory 29(2) 265–281.

Narasimhan, C. 1988. Competitive promotional strategies. J. Bus. 61(4) 427–449.

Parker, G., M. Van Alstyne. 2001. Information complements, substitutes, and strategic product design. Working paper, University of Michigan, Ann Arbor, MI.

Schechter, S., M. Smith. 2003. How much security is enough to stop a thief? Proc. Financial Cryptography Conf., Le Gosier, Guadeloupe (January) 122–137.

Schenk, M., M. Schenk. 2002. Defining the value of strategic security. Secure Bus. Quart. 1(1) 1–6.

Shapiro, C. 1986. Exchange of cost information in oligopoly. Rev. Econom. Stud. 53(3) 433–446.

Vickrey, W. 1961. Counterspeculation, auctions, and competitive sealed tenders. J. Finance 16(1) 8–37.

Vives, X. 1990. Trade association disclosure rules, incentives to share information, and welfare. RAND J. Econom. 21(3) 409–430.

Ziv, A. 1993. Information sharing in oligopoly: The truth-telling problem. RAND J. Econom. 24(3) 455–465.
