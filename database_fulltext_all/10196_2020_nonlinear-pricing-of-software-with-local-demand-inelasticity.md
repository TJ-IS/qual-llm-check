---
otero_id: 10196
otero_key: "U8SD4BPS"
title: "Nonlinear Pricing of Software with Local Demand Inelasticity"
authors: "Mingdi Xin; Arun Sundararajan"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0940"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/U8SD4BPS/fulltext/images/bf0e87381d4864205eaefb31a13c3877567318fe2ac3ade76b98dc1a1e97ad89.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Nonlinear Pricing of Software with Local Demand Inelasticity

Mingdi Xin, Arun Sundararajan

To cite this article:

Mingdi Xin, Arun Sundararajan (2020) Nonlinear Pricing of Software with Local Demand Inelasticity. Information Systems Research

Published online in Articles in Advance 17 Sep 2020

https://doi.org/10.1287/isre.2020.0940

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Nonlinear Pricing of Software with Local Demand Inelasticity

Mingdi Xin,<sup>a</sup> Arun Sundararajan<sup>b</sup>

<sup>a</sup> Paul Merage School of Business, University of California, Irvine, California 92697; <sup>b</sup> Stern School of Business, New York University, New York, New York 10012

Contact: mingdi.xin@uci.edu, https://orcid.org/0000-0001-6905-0151 (MX); arun@stern.nyu.edu (AS)

Received: Revised: Accepted: Published Online in Articles in Advance: September 17, 2020

https://doi.org/10.1287/isre.2020.0940

Copyright:

Abstract. Nonlinear usage-based pricing is applied extensively in software markets. Different from other products, customers of software products usually cannot vary their required usage volume, a property we label local demand inelasticity. For instance, a client firm that needs a sales force automation software either buys one user license for every salesperson in its organization or does not buy at all. It is unlikely to buy licenses for some salespersons but not the others. This demand feature violates a critical assumption of the standard nonlinear pricing literature that consumers are flexible with their usage volume, and their valuation changes smoothly with usage volume. Consequently, standard non linear pricing solutions are inapplicable to many software products. This paper studies the optimal nonlinear usage-based pricing of software when customers’ demand is locally inelastic. This unique demand feature necessitates a new approach to solve the nonlinear pricing problem. We provide the solution to a complicated nonlinear pricing problem with discontinuous and inelastic individual demand functions, with virtually no restriction on demand distribution, and no single-crossing restriction on valuation functions. We show that under a weak ordering condition of customer types, this complex pricing problem can be decomposed into a set of much simpler subproblems with known solutions. Our pricing solution is easily implementable and applicable to a broad range of demand systems, including those described by the families of exponential and normal distributions. More over, local demand inelasticity has a critical impact on key efficiency results. Although in standard nonlinear pricing models, the optimal pricing schedule typically involves distortion (deviation from the first best) at all but one point, this is no longer the case with local demand inelasticity. We characterize the conditions under which the optimal nonlinear pricing strategy involves quantity discounts and compare nonlinear usage-based pricing with flat-fee (for unlimited usage) pricing strategies.

History: D. J. Wu, Senior Editor; Juan Feng, Associate Editor.

Keywords: nonlinear pricing • usage-based pricing • software pricing • local demand inelasticity • discontinuous utility function piecewise linear utility function

## 1.Introduction

Nonlinear usage-based pricing refers to pricing models in which the price of a product may change nonlinearly with consumption quantity. That is, the per-unit price of a product is not constant but depends on the total quantity that a customer desires to buy. Nonlinear pricing models have been applied extensively in markets where products can be consumed in variable quantities by heterogeneous consumers: for instance, in the electricity and telecommunication markets (Wilson 1993). This form of price discrimination is particularly prevalent in software markets. For instance, it is common for software vendors to offer quantity discounts: the unit price of a software product (e.g., price per user license) decreases with consumption volume. A PwC survey of software vendors shows that about 80% of the respondents offer quantity discounts (PwC 2015). On the other hand, many software vendors charge quantity premiums: the unit price of a software product increases with consumption volume. Salesforce.com, a prominent Software-as-a-Service (SaaS) vendor, prices its customer relationship management software at \$25 per user license for up to five licenses. For more than five licenses, customers need to pay higher prices per user license, indicating a quantity premium. Therefore, determining the optimal nonlinear pricing schedule is of particular importance to software vendors.

There is an extensive literature on nonlinear usagebased pricing. A critical assumption in the standard nonlinear pricing literature is that consumers’ valuation of a product changes smoothly with their usage volume. Figure 1 shows a typical example of consumers’ value function in this literature with two types of consumers (e.g., Maskin and Riley 1984). Consumers are flexible with their usage volume. Given the vendor’s usage-based pricing schedule, consumers choose whichever consumption level maximizes their utility.

Figure 1. Standard Value Function Assuming Consumers Valuation (V) Changes Smoothly with Consumption Volume (q)  
![](/api/attachments/U8SD4BPS/fulltext/images/b0bf5a1ca4ef69628470cf2d748d5ff08d3a1df65198665b0742a2d28799a585.jpg)

In contrast, customers of software products often cannot easily vary their required usage volume. For instance, a customer who adopts Salesforce.com’s software for sales support requires one user license for every salesperson in its organization. A school that needs a learning management software (e.g., Blackboard) either buys licenses for every faculty and student or does not buy the software at all. It is unlikely that the school would buy licenses for some faculty and students but not the others. In these cases, individual customers are not flexible with their required usage volume (i.e., number of user licenses), and their valuation of a software product does not vary smoothly with their usage volume. Instead, it involves a binary adoption decision: either adopt at the required usage volume or do not adopt at all. Put simply, usage does not vary continuously at the individual customer level, a phenomenon we label local demand inelasticity. This violates the critical assumption of the standard nonlinear pricing literature.

This paper studies the optimal nonlinear usagebased pricing of software when customers’ demand is locally inelastic. We demonstrate that the solution to standard nonlinear pricing models no longer applies if customers’ demand is locally inelastic. This unique demand characteristic necessitates a new approach to solve the nonlinear pricing problem. We provide a first step toward this approach and characterize the solution to a complicated nonlinear pricing problem with discontinuous and inelastic individual demand functions, with virtually no restriction on demand distribution, and no single-crossing restriction on value functions. Our pricing solution is easily implementable and applicable to a broad range of demand systems. In addition, we show that local demand inelasticity has a critical impact on key efficiency results.

The rest of the paper is organized as follows. After a literature review, we first discuss standard nonlinear pricing solutions (Section 3). The objective is to highlight the demand features that are essential for solving standard nonlinear pricing models. Next, we show that these essential demand features are no longer valid when customers’ demand is locally inelastic, and so, the standard solutions do not apply to our pricing problem at hand. We then present our solution to this pricing problem and compare the key efficiency results given local demand inelasticity with those of standard nonlinear pricing models (Section 4). Finally, we compare nonlinear pricing with flat-fee pricing (for unlimited usage) in terms of price levels and welfare implications. We discuss this paper’s contributions in Section 5.

## 2. Literature Review

This paper is related to two streams of prior literature: (1) the literature on usage-based pricing of information goods and (2) the literature that studies piecewise linear utility functions.

There is a fairly extensive literature on usage-based pricing of information goods such as software. One substream of the literature confirms our observation that software customers are often inflexible with their required usage volume. This literature assumes that consumers demand a fixed quantity of software, and so, their utility function is locally inelastic. However, this literature restricts itself to linear pricing (i.e., the per-unit price does not change with consumption volume) and focuses on comparing the profitability of linear pricing with that of flat-fee pricing, which charges a fixed fee for unlimited usage. For instance, Choudhary (2010) examines software vendors’ choice between a linear pricing schedule and flat-fee pricing in a duopoly setting when each customer demands a fixed quantity of a software product. Consumers differ in their required quantity and valuation of the software. Balasubramanian et al. (2015) study a similar pricing problem. Different from Choudhary (2010), in their model, buying on a pay-per-use basis invokes a psychological cost associated with the well-known “ticking meter” effect. Ma and Seidmann (2015) model the competition between a software vendor that follows flat-fee pricing and an SaaS vendor that follows a linear usage-based pricing schedule, assuming that users have fixed quantity demand for the software service.

A different substream of the literature allows the per-usage price to change depending on customers total consumption volume (i.e., nonlinear pricing) However, this literature thus far has preserved the standard assumption that consumers are flexible with their usage volume, and their valuation changes continuously with usage volume (or no local demand inelasticity). For instance, Sundararajan (2004) studies nonlinear pricing of information goods when the cost of administering usage-based pricing is positive and shows that in this case, offering fixed-fee pricing in addition to nonlinear usage-based pricing is profit improving. Huang and Sundararajan (2011) study optimal usage-based pricing of digital goods with discontinuous supply functions. Jain and Kannan (2002) compare the profitability of connect-time pricing, per-search pricing, and subscription-fee pricing of online information services. More recently, Lahiri et al. (2013) compare service pricing (or pricing by the type of service used) and traffic pricing (or pricing by the traffic transmitted) of wireless services and find that discriminatory pricing across services may increase social welfare. Our paper expands this literature by focusing on a new demand characteristic that distinguishes software pricing from pricing of other products and services: the presence of local demand inelasticity.

When consumers’ demand is locally inelastic, their value function is piecewise linear. It consists of one value for adoption at the required or a higher consumption level and one value (zero) for no adoption. Piecewise linear value functions have been studied in a variety of contexts: for instance, optimization problems with loss-averse agents $( \mathrm { e . g . }$ , Tversky and Kahneman 1991, Schweitzer and Cachon 2000, Barberis and Huang 2001), multiunit auctions in which bidders can demand multiple units (Milgrom 2004), and dynamic pricing of indivisible storable goods (Berbeglia et al. 2019).

Bansal and Maglaras (2009) study a product design problem in a market with satisficing consumers who seek to buy the cheapest product with quality level above a certain type-specific threshold. The monopoly vendor needs to decide which quality levels to offer and the associated prices, subject to capacity constraints. The product design and pricing problem shares some technical properties with the pricing problem examined in this paper. However, in this paper, we assume fully rational consumers who seek to maximize their utility, whereas Bansal and Maglaras (2009) assume boundedly rational consumers. Moreover, in Bansal and Maglaras (2009), the pricing problem given each product line design resembles a special case of the pricing problem studied in this paper with stricter assumptions. Therefore, this paper studies a broader set of pricing problems and presents more generalizable solutions.

## 3. Standard Nonlinear Pricing Solutions

In this section, we discuss the standard nonlinear pricing solutions. The objective is to highlight two sets of demand features (or assumptions) that are essential for solving standard nonlinear pricing models: continuity of consumers’ value functions and the single-crossing property. These two demand features are no longer valid when customers’ demand is locally inelastic.

For expository purposes, we first consider a simple nonlinear pricing problem with two consumer types and illustrate the role that these two sets of demand assumptions play in solving the pricing problem. Second, we extend this example to consider a more complex nonlinear pricing problem with two-dimensional and continuous consumer types, which may be a more comparable benchmark to our main model. We show that the same two demand assumptions play similar roles in solving the pricing problem with multidimensional and continuous consumer types as those with two consumer types. In both examples, we discuss the key properties of the optimal nonlinear pricing schedule, which will be compared with those of the optimal nonlinear pricing schedule given local demand inelasticity in the next section.

## 3.1. Standard Nonlinear Pricing Model with Two Consumer Types

A monopolist sells a product that can be consumed in variable quantities. Consumers are heterogeneou and indexed by a type parameter, $v ,$ where $v = v _ { 1 } ,$ , or $v = v _ { 2 } ,$ , and $0 < v _ { 1 } < v _ { 2 } . \mathrm { ~ A ~ }$ fraction $\beta$ of the consumers has $v = v _ { 1 } .$ , and the remaining $1 - \beta$ of the consumers have $v = v _ { 2 }$ . The utility that consumer v gains from using quantity $q$ of the monopolist’s product at the price of T is ${ \dot { V ( q ; v ) } } - T ,$ , or the difference between her valuation and the price.

The monopolist’s objective is to determine a set of quantity-price schedule $( ( q _ { 1 } , T _ { 1 } ) , ( q _ { 2 } , T _ { 2 } ) )$ , which maximizes his profit. The monopolist does not know consumers’ types, and thus, both quantity-price options have to be available to all consumers. The revelation principle ensures that the monopolist can restrict his attention to the set of quantity-price pairs such that each pair is designed for one type of consumers, and it is optimal and rational for those consumers to choose the quantity-price pair that is designed for them (i.e., direct mechanism). This implies that the optimal quantity-price schedule has to satisfy the following incentive constraints. Consumers’ incentive compatibility (IC) constraints ensure that consumers of each type prefer the quantityprice pair designed for them to the alternative option. IC constraints can be specified as

$$
\begin{array}{l} V (q _ {2}; v _ {2}) - T _ {2} \geq V (q _ {1}; v _ {2}) - T _ {1}, \text { and } \\ V (q _ {1}; v _ {1}) - T _ {1} \geq V (q _ {2}; v _ {1}) - T _ {2}. \end{array}
$$

Consumers’ individual rationality (IR) constraints ensure that consumers receive nonnegative utility from buying the product.<sup>1</sup> IR constraints can be specified as $\bar { V ( q _ { 1 } ; v _ { 1 } ) } \ge \bar { T _ { 1 } }$ , and $V ( q _ { 2 } ; v _ { 2 } ) \ge T _ { 2 }$ . Assume the marginal cost of producing the product is constant at zero. The monopolist’s objective function can be formulated as

$$
\max _ {q _ {1}, q _ {2}, T _ {1}, T _ {2}} \beta T _ {1} + (1 - \beta) T _ {2},
$$

subject to consumers’ IR and IC constraints.

The timing of interaction between the monopolist and consumers is as follows. First, the monopolist announces his quantity-price schedule $( ( q _ { 1 } , T _ { 1 } ) , ( q _ { 2 } , T _ { 2 } ) )$ Second, consumers observe the schedule and decide whether to buy the product and if they buy, at which quantity level. Trade takes place, and the monopolist’s profit is materialized.

Standard nonlinear pricing models require that consumers’ value function satisfies the following two assumptions (e.g., Maskin and Riley 1984, assumption 1(i)–(iii)).

Assumption 1. (i) $\partial V ( q ; v ) / \partial q$ is twice continuously differentiable. (ii) For each v, there exists $q ^ { e } ( v )$ such that $\partial V ( q ; v ) / \partial q \geq 0 ,$ , if and only $i f q \le q ^ { e } ( v )$ , and $\partial V ( q ; v ) / \partial q$ is decreasing in $q f o r \ q \leq q ^ { e } ( v )$

Assumption 2 (The Single-Crossing Property or Spence– Mirrlees Property). $\partial V ( q ; v ) / \partial q$ is strictly increasing in v, or

$$
\frac {\partial V (q ; v _ {1})}{\partial q} <   \frac {\partial V (q ; v _ {2})}{\partial q},
$$

whenever $\partial V ( q ; v ) / \partial q$ is positive.

Assumption 1 requires that the value that consumers gain from using the product changes smoothly with the quantity consumed. In addition, for each consumer type, there is an efficient consumption level $q ^ { e } ( v )$ for which consumers’ marginal value is equal to the product’s marginal cost (zero). Assumption 2 requires that the marginal value of consumption increases with consumer types. That is, high-type consumers are willing to pay more for each additional unit of consumption than low-type consumers. This is a well-known necessary condition for the existence of a quantity-price schedule that induces a complete sorting of consumer types.

To solve the vendor’s pricing problem, we first simplify the four incentive constraints. The following lemma shows that given Assumptions 1 and 2, the four incentive constraints in the monopolist’s pricing problem can be reduced to two binding conditions and one constraint only. That is, type 1 consumers’ IR constraint and type 2 consumers’ IC constraint are binding, and in equilibrium, type 2 consumers buy a higher quantity than type 1 consumers $( q _ { 2 } ^ { * } \ge q _ { 1 } ^ { * } )$ ). This finding is key to solving the monopolist’s pricing problem. All proofs are in the appendix.

Lemma 1. Given Assumptions 1 and 2, an optimal pricing schedule $\{ ( q _ { 1 } ^ { * } , T _ { 1 } ^ { * } ) , ( q _ { 2 } ^ { * } , T _ { 2 } ^ { * } ) \}$ satisfies the following conditions:

$$
\begin{array}{l} q _ {2} ^ {*} \geq q _ {1} ^ {*}, a n d \\ T _ {1} ^ {*} = V (q _ {1} ^ {*}; v _ {1}), a n d \\ T _ {2} ^ {*} = V (q _ {2} ^ {*}; v _ {2}) - V (q _ {1} ^ {*}; v _ {2}) + V (q _ {1} ^ {*}; v _ {1}). \end{array}
$$

Moreover, these three conditions are sufficient for both type-1 and type-2 consumers’ IC and IR constraints..

Because the optimal prices $( T _ { 1 } ^ { * } , \ T _ { 2 } ^ { * } )$ satisfy the binding conditions in Lemma 1, one can substitute $T _ { 1 }$ and $T _ { 2 }$ in the monopolist’s objective function with these binding conditions and transform a complex high-dimensional optimization problem into a tractable variational problem. Moreover, because the conditions in Lemma 1 are also sufficient for all of consumers’ IC and IR constraints, we can reduce the number of pricing constraints from four incentive constraints to just one constraint. In particular, the monopolist’s objective function now becomes

$$
\begin{array}{l} \max _ {q _ {1}, q _ {2}} \pi (q _ {1}, q _ {2}) = \max _ {q _ {1}, q _ {2}} \beta \cdot V (q _ {1}; v _ {1}) + (1 - \beta) (V (q _ {2}; v _ {2}) \\ \qquad \qquad \qquad - V (q _ {1}; v _ {2}) + V (q _ {1}; v _ {1})) \\ \text {s.t.} q _ {2} \geq q _ {1}. \end{array}
$$

Because by Assumption 1, the marginal value function is twice continuously differentiable with respect to $q ,$ this variational problem can be solved with standard methods (e.g., first- and second-order conditions).

One can show that the optimal nonlinear pricing schedule has two important properties.

1. It involves quantity distortion at all but one point: only consumers of the highest type buy at their efficient consumption volume (the quantity level at which the marginal value equals the marginal cost). All remaining consumers buy at a quantity below their efficient consumption levels if they find it optimal to adopt. To see this, note that first-order conditions give

$$
\begin{array}{l} \frac {\partial \pi (q _ {1} , q _ {2})}{\partial q _ {2}} = (1 - \beta) \frac {\partial V (q _ {2} ; v _ {2})}{\partial q _ {2}} = 0, \\ \frac {\partial \pi (q _ {1} , q _ {2})}{\partial q _ {1}} = \frac {\partial}{\partial q _ {1}} V (q _ {1}; v _ {1}) - (1 - \beta) \frac {\partial}{\partial q _ {1}} V (q _ {1}; v _ {2}) = 0. \end{array}
$$

Recall that the marginal cost is zero. The first equation implies that in equilibrium, high-type consumers buy at the efficient consumption level. Nonetheless, the second equation implies that low-type consumers buy at a quantity level below the efficient consumption level. This is because the single-crossing property requires that $\partial V ( q _ { 1 } ; v _ { 1 } ) / \partial q _ { 1 } < \partial V \overset { \smile } { ( } q _ { 1 } ; v _ { 2 } ) / \partial q _ { 1 }$ . Hence, the second equation implies that $\partial V ( q _ { 1 } ; v _ { 1 } ) / \partial q _ { 1 } > 0$ , or the marginal value is higher than the marginal cost, a deviation from the first best.

2. For all but the lowest-type consumers, the price that consumers pay to adopt the product is less than the monopoly price given only the segment of consumers with the same efficient consumption level. That is, according to Lemma 1, $T _ { 1 } ^ { * } = V \big ( q _ { 1 } ^ { * } ; v _ { 1 } \big )$ , and $T _ { 2 } ^ { * } = V ( q _ { 2 } ^ { * } ; v _ { 2 } ) - V \check { ( } q _ { 1 } ^ { * } ; v _ { 2 } ) + V ( q _ { 1 } ^ { * } ; v _ { 1 } ) \dot { < } V ( q _ { 2 } ^ { * } ; \check { v } _ { 2 } )$

One can easily generalize the above results to show the same conclusions with more than two discrete consumer types. Maskin and Riley (1984) show that these two properties also apply to nonlinear pricing models with continuous consumer types.

Therefore, consumers’ continuous and smooth value functions (Assumption 1) and the single-crossing property (Assumption 2) are critical for solving this nonlinear pricing problem. As Lemma 1 shows, the single-crossing property helps reduce the number of constraints in the monopolist’s pricing problem. It also helps transform the monopolist’s pricing problem from one that involves solving for both a quantity schedule and a price schedule for heterogeneous consumers, or $( q _ { i } , T _ { i } ) , \mathrm { f o r } i = 1 , 2$ into one that involves just solving for the optimal quantity schedule, or q v<sub>i</sub> , $\dot { i } = 1 , 2$ . A continuous and smooth value function ensures that one can apply properties of differential equations to solve for the optimal quantity schedule (or $q ( v _ { i } ) , \ i = 1 , 2$ in our example). As we shall see, neither Assumption 1 nor Assumption 2 holds when consumers’ demand is locally inelastic. Therefore, the solution to standard nonlinear pricing models does not apply to our pricing problem at hand.

## 3.2. Standard Nonlinear Pricing Model with Two-Dimensional and Continuous Consumer Types

The key insights of the simple model with two consumer types continue to hold in a more complex setting with two-dimensional and continuous consumer types. Consumers are indexed by two type parameters $w = ( w _ { 1 } , w _ { 2 } ) \in R ^ { 2 }$ . The distribution of consumer types in the population is described by $H ( w )$ which is assumed to have a continuously differentiable density $h ( w )$ over a convex region $\dot { D } \subseteq R ^ { 2 }$ . The product can be consumed in variable quantities. The utility that a consumer gains from consuming quantity q of the product at the price of T is denoted by $U \dot { ( } q , w , T ) = \hat { V } ( q , w ) - T .$ . Subscripts of functions represent derivatives with respect to the corresponding variable. For instance, $V _ { q } ( q , w )$ represents the derivative of $V ( q , w )$ with respect to $q .$

The monopolist’s objective is to determine a quantityprice schedule $( q ( w ) , \dot { T } ( w ) )$ , which maximizes his total profit. Because the monopolist does not know each consumer’s type, the entire menu of quantity-price options has to be available to all consumers. The revelation principle ensures that we can simply focus on those quantity-price schedules that satisfy all incentive compatibility constraints. That is, for $\forall s , w \in D$

$$
U \big (q (s), w, T (s) \big) \leq U \big (q (w), w, T (w) \big).
$$

Assumptions 1 and 2 in the two-type example can be adapted in the current setting as follows (McAfee and McMillan 1988).

Assumption 1g. (i) Consumers’ value function $( V ( q , w ) )$ is twice continuously differentiable. Define $p ( q , w ) = V _ { q } ( q , w )$ or type w consumer’s marginal valuation at quantity q. (ii) For each w, there exists $q ^ { e } ( w )$ such that $\partial V ( q , \dot { w } ) / \partial q \geq 0 ,$ if and only $i f q \le q ^ { e } ( w )$ , and $\partial V ( q , w ) / \partial q$ is decreasing in q for $q \leq q ^ { e } ( w )$

Assumption 2g (Generalized Single-Crossing Property). For all $s , w , q , T ,$ , there exists $\lambda > 0$ such that

$$
p (q, w) - p (q, s) = \lambda p _ {w} (q, s) (w - s).
$$

Assumption $2 \mathrm { g }$ ensures that the direction in which the marginal valuation changes with consumer types locally $( { \mathrm { i . e . } }$ , the sign for $p _ { w } ( q , s ) )$ ) holds the same globally. Assumptions 1g and 2g play similar roles in solving the nonlinear pricing problem with two-dimensional consumer types as Assumptions 1 and 2 in the model with two consumer types. In particular, given ${ \mathrm { A s } } -$ sumptions $1 \mathrm { g }$ and ${ 2 } \mathrm { g } ,$ , one can simplify the set of incentive compatibility constraints and show that the following two conditions are necessary and sufficient for a pricing schedule to be globally incentive compatible:

$$
T ^ {\prime} (w) = p \bigl (q (w), w \bigr) q ^ {\prime} (w),
$$

and

(<sup>1</sup>)

$$
q ^ {\prime} (w) = C p _ {w} \bigl (q (w), w \bigr),\tag{2}
$$

for some $C > 0$ (which generally depends on w).

(1) ensures that incentive compatibility is satisfied locally, or

$$
\frac {\partial}{\partial s} U \big (q (s), w, T (s) \big) | _ {s = w} = 0.
$$

In addition, it establishes a mapping between the optimal quantity schedule and the optimal price schedule. This allows one to replace $\bar { T } ( w )$ with a function of q w derived from (1) and reduce the vendor’s decision problem from one that involves determining two schedules, one for quantity and one for price or $( q ( w ) , T ( w ) )$ , to one that involves determining just a quantity schedule. Moreover, (2) provides a condition for the optimal quantity schedule such that incentive compatibility is satisfied globally A formal proof of these results can be found in McAfee and McMillan (1988, theorems 1 and 2).

After replacing $T ( w )$ with a function of $q ( w )$ derived from (1), one can rewrite the vendor’s objective function simply as a function of the quantity schedule:

$$
\max _ {(q (w), T (w))} \int_ {D} T (w) h (w) d w = \max _ {q (w)} \int_ {D} I (q (w), w) d w,
$$

subject to incentive compatibility constraints. $( h ( w )$ is incorporated in $I ( q ( w ) , \bar { w } ) . )$ Note that this optimization problem generally does not have closed form solutions. Nonetheless, when I q w , w is strictly quasiconcave for each $w ,$ there exists a q w that maximizes the pointwise profit function $I ( q ( w )$ , w for each w. This quantity schedule $\overline { { q } } ( w )$ would also maximize the overall profit function if q w satisfies all the incentive compatibility constraints. From early analysis, we know that if $\overline { { q } } ( w )$ satisfies (2), then this quantity schedule and the associated price schedule, which can be recovered by integrating (1), satisfy incentive compatibility constraints globally. Therefore, when I q w , w is strictly quasiconcave for each w, q w is the solution to the vendor’s decision problem if it also satisfies (2) (Maskin and Riley 1984, McAfee and McMillan 1988).

If q w is the solution to the vendor’s decision problem, then one can show that the optimal nonlinear pricing schedule given two-dimensional and continuous consumer types shares similar properties as that given two consumer types. Specifically, the optimal nonlinear pricing schedule involves distortion at all but one point $( \mathrm { i . e . , }$ the highest-type consumers), and the price that consumers pay to adopt the product is generally not equal to the monopoly price given only the segment of consumers with the same efficient consumption level. The proofs are quite complex and beyond the scope of a benchmark discussion. We refer readers to McAfee and McMillan (1988) for official proofs and to Laffont et al. (1987) for an example with a specific utility function and demand distribution.

## 4. Pricing with Local Demand Inelasticity

In this section, we consider the seller’s pricing problem when customers’ demand is locally inelastic. A monopoly vendor sells a software product that may be used by customers in varying quantities, $q \geq 0 .$ Customers’ software usage volume can be measured by metrics such as the number of users or the number of installed devices. Customers are heterogeneous and indexed by a type parameter $\theta . \mathrm { A t y p e } \theta$ customer demands a fixed quantity $q _ { \theta }$ units of the software and is willing to pay up to $v _ { \theta }$ for this quantity. Thus, the value that a customer of type $\theta$ derives from using q units of the software is defined as

$$
V (q; \theta) = \left\{ \begin{array}{l l} 0 & \text {for} 0 \leq q <   q _ {\theta} \\ v _ {\theta} & \text {for} q \geq q _ {\theta}. \end{array} \right.\tag{3}
$$

A customer does not treat a consumption level greater than $q _ { \theta }$ as inferior to a consumption level of $q _ { \theta }$ if she does not need to pay more for the additional units. Neither does she treat it as superior if it costs at least as much as the consumption level $q _ { \theta }$ . Figure 2 illustrates a customer’s value function. Assume the marginal production cost of software is constant at zero.

The monopolist does not observe each customer’s type but knows the distribution of types within the population. Denote by $f ( q _ { \theta } , v _ { \theta } )$ the probability density function and by $F ( q _ { \theta } , v _ { \theta } )$ the cumulative density function of this distribution. $( q _ { \theta } , v _ { \theta } )$ is distributed in the rectangle $[ q _ { L } , q _ { H } ] \times [ 0 , \overline { { { v } } } ] . ^ { 2 }$ The monopolist needs to decide on a pricing schedule $T ( q )$ that specifies the price for supplying any $q$ units of the software, which maximizes his overall profit.

Clearly, Assumption 1 or 1g in the standard nonlinear pricing model is not satisfied when customers demand is locally inelastic because their value function is neither continuous nor differentiable. In ad dition, the single-crossing property (Assumption 2 or $_ { 2 \mathrm { g } } )$ does not hold either because marginal value is not well defined everywhere in this case $( \mathrm { e . g . } ,$ , when $q = q _ { \theta } )$ ). Therefore, the standard method for solving nonlinear pricing models is not applicable to our problem at hand. Next, we show that local demand inelasticity requires a new approach to solve the monopolist’s pricing problem.

The following Assumption 3 on the distribution of customer types mirrors similar distributional assumptions in standard nonlinear pricing models (e.g., Maskin and Riley 1984, assumption 2). Similar assumptions are also used in Mussa and Rosen (1978) and McAfee and McMillan (1988). Applying the same assumption allows our results to be comparable with theirs. Nonetheless, we shall show later that the main findings of this paper, the optimal nonlinear pricing algorithm, continue to hold if consumer types (θ) are discrete.

Figure 2. A Customer’s Value Function when Demand Is Locally Inelastic  
![](/api/attachments/U8SD4BPS/fulltext/images/cc5505d5ffdc0322dcaedfee9f96ace06753b304275626d17bb9a4bdc5f08b80.jpg)

Assumption 3. (i) $f ( q _ { \theta } , v ) > 0$ for any $q _ { \theta } \in [ q _ { L } , q _ { H } ]$ such that $\begin{array} { r } { \int _ { 0 } ^ { \overline { { v } } } f ( q _ { \theta } , x ) d x > 0 . \ \mathrm { ( i i ) } \ f ( q , v ) } \end{array}$ is twice continuously differentiable with respect to both arguments.

## 4.1. Optimal Pricing Strategy Given Local Demand Inelasticity

Consider customers’ decision: given a pricing schedule $T ( q )$ , a customer seeks to maximize her surplus by choosing the optimal level of quantity to buy, or

$$
\max _ {q \geq 0} V (q; q _ {\theta}, v _ {\theta}) - T (q).
$$

Because a customer does not treat a consumption level greater than $q _ { \theta }$ as inferior to a consumption level of $q _ { \theta } ,$ the solution to her optimization problem is simply to buy at price $T ( \widehat { q } )$ for quantity ${ \widehat { q } } , { \mathrm { i f } } { \widehat { q } } \geq q _ { \theta _ { \cdot } }$ $T ( \widehat { q } ) \check { \leq } v _ { \theta } ,$ , and $T ( \hat { \hat { q } } ) = \operatorname* { m i n } \{ T ( q ) , \forall \hat { q } \geq q _ { \theta } \}$ . That is, if a customer buys the software, she chooses the quantityprice plan that covers her required usage volume $\left( q _ { \theta } \right)$ at the lowest price.

The monopolist’s objective is to determine a pricing schedule $T ( q )$ that maximizes his overall profit. Again, because the monopolist does not observe customers’ types, the revelation principle ensures that the monopolist can simply focus on those pricing schedules that satisfy customers’ incentive constraints. The IC constraint for a type $\theta$ customer can be specified as

$$
V (q _ {\theta}; q _ {\theta}, v _ {\theta}) - T (q _ {\theta}) \geq V (q; q _ {\theta}, v _ {\theta}) - T (q),
$$

for any $q \neq q _ { \theta } , q \in [ q _ { L } , q _ { H } ]$ . The IR constraint for a type θ customer can be specified as $V ( q _ { \theta } ; q _ { \theta } , v _ { \theta } ) - T ( q _ { \theta } ) \overset { \cdot } { \geq } 0$ Therefore, the monopolist needs to determine a pricing schedule $T ( q )$ , which maximizes his profit and satisfies the incentive constraints of those customers who buy the software.

This is a very complex pricing problem that involves specifying a pricing function subject to a large (infinite) number of incentive constraints. The following lemma shows that the necessary and sufficient condition for all IC constraints to be satisfied among customers who buy the software is that $T ( q )$ is nondecreasing in $q .$ This result allows us to reduce the number of constraints and simplify the pricing problem.

Lemma 2. Given local demand inelasticity, the necessary and sufficient condition for all IC constraints to be satisfied among customers who buy the software is that $T ( q )$ is nondecreasing in $q .$

Next, we proceed to formulate the monopolis $\mathrm { \Delta } \cdot \mathrm { \Delta }$ pricing problem. If all customers who require the same usage volume $( \mathrm { e . g . }$ , all customers who require 100 user licenses) have identical valuation of the software, then the optimal pricing policy trivially involves setting the price $T ( q _ { \theta } ) = v _ { \theta }$ for each usage level $q _ { \theta } ,$ , assuming a nondecreasing $T ( q )$ . This pricing policy leads to efficient consumption by customers and also, the monopolist extracting all of the surplus created from the consumption. It is quite possible, however, that customers who require the same usage volume derive different values from this consumption. For instance, two client firms having the same number of salespersons may differ in their willingness to pay (WTP) for a sales force automation software depending on which industry they are in. Two schools with the same number of faculty and students are likely to have different valuations for a learning management software, depending on their budget and computing needs. One can, therefore, define for any type distribution $F ( q _ { \theta } , v _ { \theta } ) , \ g ( v ; q )$ as the conditional probability that a customer has $v _ { \boldsymbol { \theta } } = v$ given her $q _ { \theta } = q$ . Formally, this transformation is simply

$$
g (v; q) \underset {\text { def }} {=} \frac {f (q , v)}{\int_ {\left\{\theta : q _ {\theta} = q \right\}} f (q , x) d x}.
$$

Also, define

$$
G (v; q) = \int_ {0} ^ {v} g (x; q) d x
$$

as the fraction of customers with required usage level $q$ whose valuation for that level of usage is at most v.

Given a nondecreasing pricing function, $T ( q )$ , the monopolist’s profit from customers with required usage level $q _ { \theta }$ can be characterized as

$$
T (q _ {\theta}) \bigl (1 - G (T (q _ {\theta}); q _ {\theta}) \bigr) \left(\int_ {\{\theta : q = q _ {\theta} \}} f (q _ {\theta}, x) d x\right).
$$

Therefore, the monopolist’s objective function can be formulated as

$$
\max _ {T (q)} \int_ {q _ {L}} ^ {q _ {H}} T (q) (1 - G (T (q); q)) \left(\int_ {\{\theta : q _ {\theta} = q \}} f (q _ {\theta}, x) d x\right) d q,\tag{4}
$$

subject to the constraint that $T ( q )$ is nondecreasing. This is still a complex optimization problem involving finding an optimal pricing function that maximizes an integration with an arbitrary distribution of customer types and subject to the constraint that the pricing function is nondecreasing. We show that under a weak ordering condition in customer types, which we define in Assumption $^ { 4 , }$ , there is a strikingly simple solution to this complex pricing problem.

Assumption 4. For each $q _ { 1 } < q _ { 2 }$ , where $q _ { 1 } , q _ { 2 } \in [ q _ { L } , q _ { H } ] .$ $G ( v ; q _ { 2 } )$ stochastically dominates $G ( v ; q _ { 1 } )$ according to the hazard rate order, or mathematically,

$$
\frac {g (v ; q _ {2})}{1 - G (v ; q _ {2})} \leq \frac {g (v ; q _ {1})}{1 - G (v ; q _ {1})}.
$$

Let $I ( T ; q ) = T ( 1 - G ( T ; q ) )$ . The following theorem characterizes the optimal pricing strategy.

Theorem 1. Given Assumptions 3 and 4, if there is a unique $\overline { T }$ that satisfies

$$
\overline {{T}} (q) = \frac {1 - G (\overline {{T}} ; q)}{g (\overline {{T}} ; q)}\tag{5}
$$

for each $q$ and $\partial ^ { 2 } I / \partial T ^ { 2 } | _ { T = \overline { { { T } } } } < 0 .$ , then $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ is the monopolist’s optimal pricing strategy.

This result is interesting for several reasons.

Theoretically, it characterizes a strikingly simple solution to a complicated pricing problem. We show that under a fairly weak ordering restriction on customers’ demand distribution (Assumption 4), the seller’s pricing problem has a simple solution. Note that $\overline { { T } } ( \overset { \cdot } { q } )$ is the revenue-maximizing (monopoly) price if the market is composed of only those customers whose required consumption level is $q .$ Therefore, our results demonstrate that the seller’s complex pricing problem can be decomposed into a set of much simpler local optimization problems with known solutions. That ${ \mathrm { i } } \mathbf { s } ,$ the seller can treat customers with different required consumption levels as separate markets, and the monopoly price in each market together constitutes the optimal pricing schedule for all customers. This transformation does not typically work because a pricing schedule composed of the optimal price in each submarket may not satisfy customers’ IC constraints globally. We show that under a weak ordering condition, these locally optimal prices together form a quantity-price schedule that satisfies all of customers’ IC constraints and thus, is the globally optimal solution.

The conditions in Theorem 1 are fairly weak compared with the conditions necessary for solving standard nonlinear pricing problems. These conditions can be satisfied by a broad range of demand systems. Specifically, as we have discussed in the benchmark model, standard nonlinear pricing theories require the seller’s pointwise profit function to be strictly quasiconcave (Maskin and Riley 1984). In contrast, Theorem 1 only requires that $\partial ^ { 2 } I { \dot { / } } \partial T ^ { 2 } < 0 \mathrm { a t } T = \overline { { T } }$ and has no requirement for any $T \neq { \overline { { T } } }$ . Moreover, hazard rate dominance in Assumption 4 is a fairly weak ordering condition. Intuitively, it requires customers with a higher required usage level to be probabilistically more likely to have a higher valuation of the software. One could think of many software markets in which larger customers (by required usage volume) tend to be willing to pay more for the software.

The conditions in Theorem 1 are satisfied by a broad range of demand distributions. For instance, the families of exponential and normal distributions are widely ap plied to describe demand systems in many markets $( \mathrm { e . g . }$ , Scarf 1959, Azoury 1985, Perloff and Salop 1985, Gavirneni et al. 1999, Segal 2003). We shall show in Section 4.1.2 that Theorem 1 can be applied to the family of exponential distributions. Alternatively, if $g ( \cdot )$ follows a normal distribution, or

$$
g (v; q) = \frac {1}{\sqrt {2 \pi \sigma_ {q} ^ {2}}} \mathrm{exp} \left(- \frac {(v - \mu_ {q}) ^ {2}}{2 \sigma_ {q} ^ {2}}\right),
$$

then a sufficient condition that $G ( v ; q _ { 2 } )$ hazard rate dominates $G ( v ; q _ { 1 } )$ for each $q _ { 1 } < q _ { 2 }$ is that $\mu _ { q _ { 2 } } > \mu _ { q _ { 1 } } ,$ , and $\sigma _ { q _ { 1 } } ^ { 2 } = \sigma _ { q _ { 2 } } ^ { 2 } .$ , where $q _ { 1 } , q _ { 2 } \in [ q _ { L } , q _ { H } ] . ^ { 3 }$ One can show that $I ( T ; q )$ is not quasiconcave in $T$ everywhere given a normal distribution, but there is a unique solution to $\partial I / \partial T = 0 .$ , which we denote by $T = { \overline { { T } } } .$ , and $\partial ^ { 2 } I / \partial T ^ { 2 } < 0$ when $T = { \overline { { T } } } . ^ { 4 }$ Therefore, one can apply Theorem 1 to solve for the seller’s optimal pricing schedule.

With slight modification, our proposed nonlinear pricing algorithm continues to be optimal if the distribution of consumer types is discrete. In particular, assume a type $\theta$ consumer’s demand is described by $( q _ { \theta } , v _ { \theta } ) \in \{ \bar { q _ { 1 } } , \dots , q _ { n } \} \times \{ v _ { 1 } , \dots , v _ { m } \}$ , where n and m are integers, and $n , m \geq 1$ . Without loss of generality, assume $q _ { i } < q _ { j }$ for any $i < j .$ The following theorem shows that our optimal nonlinear pricing algorithm also applies to the cases with discrete consumer types.

Theorem 2. For each $q _ { i } ,$ where $i = 1 , \ldots , n ,$ if there exists a unique $\overline { { T _ { i } } }$ that maximizes the vendor’s profit if the market is composed of only those customers whose required consumption level is $q _ { i . }$ , or

$$
\overline {{T _ {i}}} = \underset {T \in \{v _ {1}, \dots , v _ {m} \}} {\arg \max} T \sum_ {v \geq T} g (v; q _ {i}),
$$

and $\overline { { T _ { i } } }$ is nondecreasing in $i ,$ then the vendor’s optima nonlinear pricing strategy is $\{ ( \overline { { T _ { i } } } , q _ { i } ) , i = 1 , \dots , n \}$

4.1.1. Comparison: Optimal Nonlinear Pricing Strategy With or Without Local Demand Inelasticity. We examine two properties of the optimal nonlinear pricing schedule with local demand inelasticity: (1) the consumption level that the optimal nonlinear pricing strategy induces consumers to choose and (2) the pricing levels. We compare these properties with those of the standard nonlinear pricing schedule without local demand inelasticity and highlight the impact of local demand inelasticity on key efficiency results.

First, with local demand inelasticity, a consumer’s efficient consumption level, the consumption quantity that yields the highest total surplus, is equal to her required quantity of consumption. The following corollary shows that with local demand inelasticity, all consumers who adopt the software buy at their required (efficient) consumption level.

Corollary 1. With local demand inelasticity, when the conditions in Theorem 1 are satisfied, given the seller’s optimal pricing strategy $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ , all consumers that adopt the software buy at their required (efficient) consumption level.

In contrast, in standard nonlinear pricing models without local demand inelasticity, the optimal pricing schedule typically involves distortion at all but one point: all but the highest-type consumers buy at a quantity below their efficient consumption levels if they find it optimal to adopt (Maskin and Riley 1984, McAfee and McMillan 1988). Because consumers marginal valuation decreases with consumption volume (Assumption 1 or 1g), this means most consumers buy at a quantity level at which their marginal valuation exceeds the marginal cost, a deviation from the first best.

This difference occurs because with local demand inelasticity, consumers would not buy at any quantity levels below their required (efficient) consumption level but may buy at a higher quantity level if the price is lower. In contrast, in standard nonlinear pricing models without local demand inelasticity, consumers valuation changes smoothly with consumption quantity, and so, they may buy at a quantity level below, at, or above their efficient consumption level depending on the pricing schedule. Without knowing each consumer’s type, to maximize overall profit, the vendor opts for an optimal pricing schedule that maximizes consumption by the highest-type consumers to be equal to their efficient consumption level. Nonetheless, to create incentives for the highest-type consumers to buy at the highest instead of any lower quantity levels, the vendor has to introduce distortions to all other consumers’ consumption—all other consumers buy at a quantity below their efficient consumption level (Maskin and Riley 1984).

Next, with local demand inelasticity, the seller’s optimal pricing strategy is such that all consumers with the same required (efficient) consumption level buy the software at the same price if they find it optimal to adopt, and this price is equal to the monopoly price given only the segment of consumers who have the same required consumption level. The following corollary summarizes this finding.

Corollary 2. With local demand inelasticity, when the conditions in Theorem 1 are satisfied, given the seller’s optimal pricing strategy T q , all consumers with the same required (efficient) consumption level buy the software at the same price if they find it optimal to adopt. This price is equa to the monopoly price given only the segment of consumers who have the same required consumption level.

In contrast, without local demand inelasticity, given single-dimensional consumer types, all consumers who have the same efficient consumption level also buy at the same price if they find it optimal to adopt. However, for all but the lowest-type consumers, this price is less than the monopoly price given only the segment of consumers who have the same efficient consumption level. Given multidimensional consumer types, consumers who have the same efficient consumption level generally do not buy at the same quantity or price under the optimal nonlinear pricing schedule.

This difference occurs because, although consumers would not buy at any quantity levels below their required (efficient) consumption level when their demand is locally inelastic, in standard nonlinear pricing models without local demand inelasticity, consumers of all types have the option to buy a lower quantity and pay a lower price, except for consumers of the lowest type. Thus, to induce the higher-type consumers to buy at the designated (higher) quantity-price level, the vendor has to give up some surplus (information rent). As a result, given single-dimensional consumer types, the price for each segment of consumers with the same efficient consumption level is less than the monopoly price if this segment of consumers could be isolated from the remaining consumers, except for consumers of the lowest type. When consumer types are multidimensional, consumers with the same efficient consumption level generally have different valuations for consumption at each quantity level depending on their actual types. Therefore, the optimal pricing for consumers with the same efficient consumption level is a nonlinear pricing schedule instead of a single price (e.g., Laffont et al. 1987).

4.1.2. An Example with an Exponential Distribution of Consumer Types. To illustrate how our optimal nonlinear pricing algorithm can be applied in a specific context, let us consider an example in which consumer types within the population follow an exponential distribution with a probability density function,

$$
f (q _ {\theta}, v _ {\theta}) = \frac {1}{q _ {H} - q _ {L}} \frac {\beta}{q _ {\theta} ^ {\alpha}} e ^ {- \beta v _ {\theta} / q _ {\theta} ^ {\alpha}},\tag{6}
$$

and a cumulative density function,

$$
F \big (q _ {\theta}, v _ {\theta} \big) = \frac {1}{q _ {H} - q _ {L}} \left(1 - e ^ {- \beta v _ {\theta} / q _ {\theta} ^ {\alpha}}\right),
$$

where $0 < q _ { L } \leq q _ { \theta } \leq q _ { H } , \ v _ { \theta } \geq 0 , \ \alpha > 0 ,$ , and $\beta > 0$ . The exponential distribution implies that given each efficient consumption level, a small fraction of the customers have relatively high WTP for the software, and customers with higher required consumption levels are likely to be willing to pay more for the software. Exponential demand distribution is widely used in the economics literature to study demand learning and optimal pricing or inventory policies (e.g., Scarf 1959, Iglehart 1964, Perloff and Salop 1985, Segal 2003, Rossi et al. 2014).

Consider customers’ software adoption decision: given a pricing schedule $T ( q )$ , a customer seeks to maximize her surplus by choosing the optimal level of quantity to buy, or

$$
\max _ {q \in \left[ q _ {L}, q _ {H} \right]} V (q; \theta) - T (q).
$$

Thus, a customer either buys the software at quantity q <sub></sub> arg max ${ \cal V } ( q ; \theta ) - T ( q )$ if $V ( \widehat { q } ; \theta ) - T ( \widehat { q } )$ 0 or does not buy the software at all.

The vendor needs to determine a quantity-price schedule $( q , T ( q ) )$ to maximize his overall profit. With individual customers’ demand specified, we can compute the vendor’s total demand at any quantity leve ${ \widehat { q } } ,$ given a pricing schedule $T ( q )$ , by aggregating across the customer population. That is, for $\forall \widehat { q } \in \left[ q _ { L } , q _ { H } \right]$ , the vendor’s demand at quantity $\widehat { \boldsymbol { q } }$ is

$$
D (\widehat {q}) = \iint_ {\Omega} f (q _ {\theta}, v _ {\theta}) d q _ {\theta} d v _ {\theta},
$$

where $\Omega = \{ \theta | \widehat { q } = \arg \operatorname* { m a x } \bigl [ V ( q ; \theta ) - T ( q ) \bigr ] \wedge V ( \widehat { q } ; \theta ) -$ $T \big ( \widehat { q } \big ) \geq 0 \}$ . Hence, the vendor’s decision problem can be described as

$$
\max _ {T (q)} \int_ {q _ {L}} ^ {q _ {H}} T (q) D (q) d q.
$$

This is a complex optimization problem even if the distribution of consumer types is specified. Lemma 2 helps simplify this optimization problem by showing that the necessary and sufficient condition for all customers to buy the software at their required quantity, or for all incentive compatibility constraints to be satisfied, is that $T ( q )$ is nondecreasing. In this case, the vendor’s demand at any quantity level ${ \widehat { q } } ,$ given a nondecreasing pricing schedule $\check { T } ( q )$ , can be described as

$$
D (\widehat {q}) = \int_ {T (\widehat {q})} ^ {\infty} f (\widehat {q}, x) d x = \frac {1}{q _ {H} - q _ {L}} e ^ {- \beta T (\widehat {q}) / \widehat {q} ^ {\alpha}}.
$$

Thus, the vendor’s optimization problem can be simplified as

$$
\begin{array}{l} \max _ {T (q)} \int_ {q _ {L}} ^ {q _ {H}} \frac {1}{q _ {H} - q _ {L}} T (q) e ^ {- \beta T (q) / q ^ {\alpha}} d q \\ \text { s.t. } T (q) \text { is   nondecreasing   in } q. \end{array}
$$

Although we have simplified the vendor’s objective function, the optimization problem is still quite complex and involves finding a nondecreasing pricing function $T ( q )$ that maximizes an integration.

We apply Theorem 1 to solve this pricing problem. Note that Assumption 3 is satisfied given the distribution of consumer types specified in (6). Moreover,

$$
\begin{array}{r} g (v; q) = \frac {f (q , v)}{\int_ {0} ^ {\infty} f (q , x) d x} = \frac {\beta}{q ^ {\alpha}} e ^ {- \beta v / q ^ {\alpha}}, \\ G (v; q) = \int_ {0} ^ {v} g (x; q) d x = 1 - e ^ {- \beta v / q ^ {\alpha}}. \end{array}
$$

Thus, Assumption 4 is also satisfied because for each $q _ { 1 } < q _ { 2 }$ , where $q _ { 1 } , q _ { 2 } \in [ q _ { L } , q _ { H } ] .$ , one can show that $G ( v ; q _ { 2 } )$ stochastically dominates $G ( v ; q _ { 1 } )$ according to the hazard rate order, or mathematically,

$$
\frac {g (v ; q _ {2})}{1 - G (v ; q _ {2})} = \frac {\beta}{q _ {2} ^ {\alpha}} \leq \frac {g (v ; q _ {1})}{1 - G (v ; q _ {1})} = \frac {\beta}{q _ {1} ^ {\alpha}}.
$$

Note that given an exponential distribution, $I ( T ; q )$ is not quasiconcave in $\hat { T }$ everywhere, but $\overline { { T } } ( q ) = q ^ { \alpha } / \beta$ is the unique solution to

$$
\overline {{T}} (q) = \frac {1 - G (\overline {{T}} ; q)}{g (\overline {{T}} ; q)},
$$

and $I ( T ; q ) = T ( 1 - G ( T ; q ) ) = T e ^ { - \beta T / q ^ { \alpha } }$ . Hence, we have

$$
\frac {\partial^ {2} I}{\partial T ^ {2}} \Big | _ {T = \overline {{T}}} = - \frac {\beta}{q ^ {\alpha} e} <   0.
$$

Therefore, we can apply Theorem 1 to solve the vendor’s optimal nonlinear pricing strategy. Indeed the optimal pricing policy is surprisingly simple: $\overline { { T } } ( q ) = q ^ { \alpha } / \beta ,$ , for $q \in [ q _ { L } , q _ { H } ]$

Clearly, the price of the software $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ increases with consumption quantity q. When $\alpha > 1$ , the nonlinear pricing schedule is a convex function of consumption quantity, and the vendor charges a quantity premium, or the marginal price increases with total consumption. Business software markets are espe cially suitable for enforcing quantity premiums because customers cannot easily acquire a large number of software licenses by successively buying small quantities under different guises, and there are no competing vendors offering the same software. When $\alpha < \hat { 1 }$ , the nonlinear pricing schedule is a concave function of consumption quantity, and the vendor offers a quantity discount, or marginal price decreases with total consumption. Figure 3 illustrates the optimal nonlinear pricing schedule given different values of α. The vendor’s optimal profit given this pricing strategy is $( q _ { H } ^ { \alpha + 1 } - q _ { L } ^ { \bar { \alpha + 1 } } ) / ( ( q _ { H } - q _ { L } ) \bar { \beta } e ( \alpha + 1 ) )$ .

This example shows that given the optimal nonlinear pricing schedule, the unit price $( \mathrm { i } . \mathrm { e } . , T ( q ) / q )$ may increase (quantity premium) or decrease (quantity discount) with greater consumption (q). As we have discussed in Section 1, both quantity premiums and quantity discounts are common among software products. Next, we generalize this result and characterize the conditions under which it is optimal for the vendor to offer quantity discounts.

Figure 3. Optimal Nonlinear Pricing Strategy Given Local Demand Inelasticity and Exponential Demand Distribution $( \mathrm { f o r } \ \beta = 1 , q _ { L } = 1 , q _ { H } = 8 )$  
![](/api/attachments/U8SD4BPS/fulltext/images/f39e5b073d431da6c9aaf065fca791f85d8e9f1355231a0f71df64d690c2119b.jpg)

4.1.3. Quantity Discounts. For simplicity of exposition, we restrict ourselves to the case in which $\overline { { { T } } } ( \bar { q } ) .$ , as defined in (5), is continuous and differentiable for $q \in [ q _ { L } , q _ { H } ]$ . The following theorem shows that given a mild restriction on the demand distribution, it is optimal for the vendor to offer quantity discounts everywhere. Therefore, our results suggest that offering quantity discounts can be optimal for a broad range of cases, consistent with the prevalence of 5 quantity discounts in software markets (PwC 2015).

Theorem 3. Given the conditions in Theorem 1 are satisfied, the vendor finds it optimal to offer quantity discounts, or $\overline { { T } } ( q ) / q$ decreases with $q ,$ if the demand distribution is such that the following condition is satisfied for $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ defined in (5):

$$
I _ {T q q} I _ {T T} ^ {2} - \big (I _ {T q T} + I _ {T T q} \big) I _ {T q} I _ {T T} + I _ {T T T} I _ {T q} ^ {2} <   0.
$$

Intuitively, $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ as defined in (5) is an optimal pricing strategy if customers with higher required usage levels are probabilistically more likely to have higher valuation of the software (Assumption 4). The monopolist offers quantity discounts if this improvement in demand distribution is relatively gradual with q.

## 4.2. Comparison: Nonlinear Usage-Based Pricing vs. Flat-Fee Pricing

Another popular pricing scheme in software markets is flat-fee pricing under which a customer pays a fixed fee in exchange for unlimited usage of the software. For instance, Oracle offers Unlimited License Agreement for select software products, and many software vendors forgo usage-based pricing and sell site licenses for their software products. In this section, we compare nonlinear usage-based pricing with flat-fee pricing given local demand inelasticity.<sup>6</sup> We are interested in two sets of questions.

1. How does the optimal pricing strategy under flat-fee pricing compare with that under nonlinear usage-based pricing? Do these results differ with or without local demand inelasticity?

2. How does nonlinear usage-based pricing compare with flat-fee pricing in terms of optimizing social welfare?

First, we examine the optimal flat-fee pricing strategy. Given a fixed price $\scriptstyle { \dot { T } } ,$ any customer with $v _ { \boldsymbol { \theta } } \geq T$ buys the software. The seller’s objective function becomes

$$
\max _ {T} T \int_ {q _ {L}} ^ {q _ {H}} \int_ {T} ^ {\overline {{v}}} f (q, x) d x d q.
$$

Note that

$$
\begin{array}{l} T \int_ {q _ {L}} ^ {q _ {H}} \int_ {T} ^ {\overline {{v}}} f (q, x) d x d q \\ = \int_ {q _ {L}} ^ {q _ {H}} I (T; q) \cdot \left(\int_ {\{\theta : q _ {\theta} = q \}} f (q _ {\theta}, x) d x\right) d q. \end{array}
$$

Let $T _ { f }$ denote the solution to this optimization problem.

The following theorem shows that the optimal flatfee price is within the range of prices under usagebased pricing, or $\overline { { T } } ( q _ { L } ) \leq \overline { { T } } _ { f } \leq \overline { { T } } ( \dot { q } _ { H } )$ . Recall that the optimal usage-based pricing schedule $T ( q )$ is nondecreasing in q. Therefore, customers with relatively high required usage volume are better off under flatfee pricing: they pay less, and more customers in this segment buy the software under flat-fee pricing than under usage-based pricing. In contrast, customers with relatively low required usage volume are worse off under flat-fee pricing: they pay more, and fewer customers in this segment buy the software under flatfee pricing than under usage-based pricing. Figure 4 compares the adoption basis under flat-fee pricing with that under usage-based pricing. In particular, under nonlinear usage-based pricing, customers in Regions I and II buy the software, whereas under flatfee pricing, customers in Regions I and III buy the software. Customers in Region IV do not buy the software under either pricing scheme.

This result is in contrast to that of the standard nonlinear pricing model in which consumers are flexible with their usage volume. In standard nonlinear pricing models, some high-type consumers always pay a higher price under flat-fee pricing than under usage-based pricing (Sundararajan 2004). This is because when consumers are flexible with their usage volume, and their valuation changes continuously with usage, nonlinear pricing causes almost all consumers to “underconsume” in the sense that they buy at a usage level below their efficient consumption level. Under flat-fee pricing, however, consumers do not pay for each additional usage and hence, consume as much as they need if they decide to buy. In particular, they would consume until their marginal value is equal to zero. This increase in consumption volume improves their valuation of the product, leading to a higher price for (some) high-type consumers under flat-fee pricing compared with usagebased pricing. On the other hand, when customers required usage volume is inflexible (i.e., local demand inelasticity), their valuation for the product does not change whether they adopt the product through flatfee pricing or usage-based pricing. As a result, customers with higher required usage volume always pay less under flat-fee pricing compared with usagebased pricing.

Figure 4. Adoption Basis Under Flat-Fee vs. Usage-Based Pricing  
![](/api/attachments/U8SD4BPS/fulltext/images/8fdc6c44a17aa3c574ca1576b0d19f7038365b0630e1e202fa1585d9fdc13a38.jpg)

Theorem 4. Given the conditions in Theorem 1 are satisfied so that the seller’s optimal nonlinear usage-based pricing strategy is $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ , the optimal flat-fee price $T _ { f }$ is within the range of prices under nonlinear usage-based pricing, or $\overline { { T } } ( q _ { L } ) \leq \dot { T _ { f } } \leq \overline { { T } } ( q _ { H } )$

Second, can social surplus be improved if the software vendor employs flat-fee instead of nonlinear usage-based pricing? Because the marginal cost of software is constant at zero, this depends on the cumulative consumer surplus under flat-fee pricing compared with that under usage-based pricing.

The answer to this question is not immediately clear. When customers are heterogeneous in their valuation of the software, usage-based pricing allows the monopolist to offer a menu of options with each option customized for a separate segment of customers. This may allow the monopolist to sell to more consumers, which can improve social surplus (Sundararajan 2004). On the other hand, to maximize his profit, the seller may focus on the utility of higher-type customers and exclude some low-type customers from participating or distort the pricing menu so that not all customers buy at their efficient consumption level, which would hurt social surplus (Maskin and Riley 1984).

The following theorem suggests a simple criterion that social planners can use to determine when flat-fee instead of usage-based pricing is socially optimal:

given local demand inelasticity, if flat-fee pricing leads to a larger adoption basis than nonlinear usagebased pricing, then it also yields higher social surplus.

Theorem 5. With local demand inelasticity, given the conditions in Theorem 1 are satisfied, social surplus is higher under flat-fee pricing, if the software adoption basis is larger under flat-fee pricing than under nonlinear usagebased pricing.

Intuitively, if we compare the adoption basis under nonlinear usage-based pricing with that under flatfee pricing (see Figure 4), under flat-fee pricing, the added adoption basis comes from customers who have high demand quantities and intermediate WTP for the software (e.g., Region III in Figure 4), whereas the lost adoption basis comes from customers who have low demand quantities and low WTP for the software (Region II in Figure 4). Indeed, all customers in the added adoption basis have higher WTP for the software than the customers in the lost adoption basis. If the overall adoption basis is higher under flatfee pricing than under nonlinear usage-based pricing, then the added adoption basis not only represents higher WTP for the software but also contains more customers compared with the lost adoption basis. This leads to an overall improvement in social surplus under flat-fee pricing.

## 5. Conclusion

Customers often cannot vary their required usage volume of a software product, a property we label local demand inelasticity. This unique demand feature violates a critical assumption of the standard nonlinear pricing literature and renders the standard pricing solutions inapplicable in many software markets. This paper studies the optimal nonlinear usage-based pricing of software when customers demand is locally inelastic. This paper makes several key contributions.

First, we demonstrate that this unique demand feature necessitates a new approach to solve the nonlinear pricing problem. We provide a first step toward this approach and characterize the solution to a complicated nonlinear pricing problem with discontinuous and inelastic individual demand functions, with virtually no restriction on demand distribution and no single-crossing restrictions on the value functions. We show that under a weak ordering condition of customer types, this complex pricing problem can be decomposed into a set of strikingly simple local optimization problems with known solutions. Specifically, the monopolist can segment customers into submarkets according to their required usage levels, and the revenue-maximizing (monopoly) price from each submarket constitutes the monopolist’s optimal pricing schedule for all customers. For instance, for a sales force automation software whose price is based on the number of user licenses that a client firm requires, our theory suggests that the software vendor can determine the optimal pricing schedule by separating all customers according to the sizes of their sales team (i.e., required usage volume). The revenuemaximizing (monopoly) price for each customer segment (characterized by client firms having the same number of salespersons) together forms the optimal pricing schedule.

This transformation does not typically work because a pricing schedule composed of the optimal price in each submarket may not satisfy customers global incentive constraints. We show that under a weak ordering condition of customer types, these locally optimal prices together form a quantity-price schedule that satisfies all of customers’ incentive constraints and thus, is also globally optimal. This pricing solution requires very few restrictions on the underlying demand distribution. Thus, it is applicable to a broad range of demand systems, including those described by the families of exponential or normal distributions, two widely used demand distributions in prior literature.

Second, we demonstrate that local demand inelasticity has a critical impact on the equilibrium outcome and key efficiency results. In particular, without local demand inelasticity, the optimal nonlinear pricing schedule typically involves distortion (or deviation from the first best) at all but one point: all but the highest-type consumers buy at a quantity below their efficient consumption level, the quantity that maximizes total surplus. In contrast, when demand is locally inelastic, all consumers who adopt the software buy at their required (efficient) consumption level.

Moreover, local demand inelasticity affects the optimal pricing levels. With local demand inelasticity, under the optimal pricing schedule, all consumers with the same required (efficient) consumption level buy the software at the same price equal to the monopoly price given only the segment of consumers who have the same required consumption level. In contrast, without local demand inelasticity, given single-dimensional consumer characteristics, consumers with the same efficient consumption level pay the same price if they adopt. However, for all but the lowest-type consumers, this price is less than the monopoly price given only the segment of consumers who have the same efficient consumption level. Given multidimensional consumer characteristics, consumers who have the same efficient consumption level generally do not buy at the same quantity or price under the optimal nonlinear pricing schedule. In the paper, we explain how local demand inelasticity causes these differences.

Third, flat-fee pricing (i.e., a fixed price for unlimited usage) is a popular alternative pricing scheme to nonlinear usage-based pricing. We demonstrate that local demand inelasticity impacts the trade-off between nonlinear usage-based pricing and flat-fee pricing. With local demand inelasticity, customers with relatively high required usage volume are better off under flat-fee pricing than nonlinear (usagebased) pricing: they pay less under flat-fee pricing, and more customers in this segment buy the software. Customers with relatively low required usage volume are worse off under flat-fee pricing: they pay more under flat-fee pricing, and fewer customers in this segment buy the software. In contrast, in standard nonlinear pricing models without local demand inelasticity, some high-type consumers always pay a higher price under flat-fee pricing than under usagebased pricing (Sundararajan 2004). Furthermore, our findings suggest a simple criterion that social planners can use to determine when flat-fee instead of nonlinear usage-based pricing is socially optimal. Given local demand inelasticity, if flat-fee pricing leads to more customers adopting the software, then social surplus is higher under flat-fee pricing than under nonlinear usage-based pricing.

Managerially, this paper proposes a practical pricing solution that can be easily implemented by software vendors. Specifically, given local demand inelasticity, if a vendor knows the distribution of customers’ required usage volume and WTP for the software, then Theorems 1 and 2 provide an easy algorithm for calculating the optimal nonlinear pricing schedule and for ensuring that all of customers incentive compatibility constraints are satisfied. The pricing algorithm breaks down a complex nonlinear pricing problem into a set of much easier subproblems, each with known solutions. The only condition to ensure that the aggregate solution satisfies all customers’ incentive compatibility constraints and thus, is globally optimal is that the nonlinear pricing schedule is nondecreasing in consumption quantity, which is easy to verify. Finally, the information re quired for these calculations—customers’ required usage volume and WTP for a software product—is quite practical to gather.<sup>7</sup> Therefore, our pricing solution may make the real-world use of the nonlinear pricing model more viable.

## Appendix. Proofs

Proof of Lemma 1. First, we show that these three condi tions are necessary for an optimal pricing schedule. One can show that given an optimal pricing schedule, $q _ { 2 } ^ { * }$ <sub>≥</sub>q∗. Suppose this is not the case, or $q _ { 2 } ^ { * } < \grave { q } _ { 1 } ^ { * } ;$ then, given the single-crossing property, we have

$$
V \big (q _ {1} ^ {*}; v _ {2} \big) - V \big (q _ {2} ^ {*}; v _ {2} \big) > V \big (q _ {1} ^ {*}; v _ {1} \big) - V \big (q _ {2} ^ {*}; v _ {1} \big).
$$

However, the IC constraint of type 1 consumers (with $v = v _ { 1 } )$ implies

$$
T _ {1} ^ {*} - T _ {2} ^ {*} \leq V (q _ {1} ^ {*}; v _ {1}) - V (q _ {2} ^ {*}; v _ {1}),
$$

whereas the IC constraint of type 2 consumers (with $v = v _ { 2 } )$ implies

$$
T _ {1} ^ {*} - T _ {2} ^ {*} \geq V (q _ {1} ^ {*}; v _ {2}) - V (q _ {2} ^ {*}; v _ {2}).
$$

Contradiction. Thus, we have $q _ { 2 } ^ { * } \geq q _ { 1 } ^ { * }$

Given $q _ { 2 } ^ { * } \geq q _ { 1 } ^ { * }$ , it is easy to see that at optimum, $T _ { 1 } ^ { * } = V ( q _ { 1 } ^ { * } ; \overline { { v _ { 1 } } } )$ because increasing $T _ { 1 }$ only makes the first option, $\left( q _ { 1 } , T _ { 1 } \right)$ , less appealing to type 2 consumers, and the most that type 1 consumers are willing to pay for $q _ { 1 } ^ { * }$ units of the product is $V ( q _ { 1 } ^ { * } ; v _ { 1 } )$ . Furthermore, one can show that given an optimal pricing schedule, the IC constraint of type 2 consumers is binding. Suppose this is not the case, or $\begin{array} { r } { \bar { V } ( q _ { 2 } ^ { * } ; v _ { 2 } ) - T _ { 2 } ^ { * } > V ( q _ { 1 } ^ { * } ; v _ { 2 } ) - \breve { T } _ { 1 } ^ { * } } \end{array}$ . Note the right-hand side of the inequality

$$
V \big (q _ {1} ^ {*}; v _ {2} \big) - T _ {1} ^ {*} > V \big (q _ {1} ^ {*}; v _ {1} \big) - T _ {1} ^ {*} \geq 0,
$$

given the single-crossing property. In this case, the monopolist can improve his profit by increasing $T _ { 2 } ^ { * }$ to $T _ { 2 } ^ { * } + \delta ,$ for an arbitrarily small $\delta > 0 ,$ , such that none of the IC or IR constraints would be violated. This is contradictory to the fact that $T _ { \gamma } ^ { \ast }$ is optimal. Therefore, given an optimal pricing schedule $\{ ( q _ { 1 } ^ { * } , T _ { 1 } ^ { * } ) , ( q _ { 2 } ^ { * } , T _ { 2 } ^ { * } ) \}$ , we have $V ( q _ { 2 } ^ { * } ; v _ { 2 } { \dot { ) } } - T _ { 2 } ^ { * } = { \bf \ddot { \Gamma } } V ( q _ { 1 } ^ { * } ; v _ { 2 } ) - T _ { 1 } ^ { * } .$ or $T _ { 2 } ^ { * } = \bar { V ( q _ { 2 } ^ { * } ; v _ { 2 } ) } \bar { - } V ( q _ { 1 } ^ { * } ; v _ { 2 } ) + V ( q _ { 1 } ^ { * } ; v _ { 1 } )$

Second, we show that these three conditions are suffi cient for both the two IC constraints and the two IR con straints. Clearly, the IC constraint of type 2 consumers with $v = v _ { 2 }$ is satisfied because

$$
V (q _ {2} ^ {*}; v _ {2}) - V (q _ {1} ^ {*}; v _ {2}) = T _ {2} ^ {*} - T _ {1} ^ {*}.
$$

Consider the IC constraint of type 1 consumers with $v = v _ { 1 }$ One can show that $T _ { 2 } ^ { * } - T _ { 1 } ^ { * } = \bar { V } ( q _ { 2 } ^ { * } ; v _ { 2 } ) - V ( q _ { 1 } ^ { * } ; v _ { 2 } ) \geq V ( q _ { 2 } ^ { * } ; v _ { 1 } ) -$ $V ( q _ { 1 } ^ { * } ; v _ { 1 } )$ , given the single-crossing property, and $q _ { 2 } ^ { * } \geq q _ { 1 } ^ { * }$ Thus, the IC constraint of type 1 consumers is satisfied. Clearly, the IR constraint of type 1 consumers with $v = v _ { 1 }$ is satisfied. Consider the IR constraint of type 2 consumers with $v = v _ { 2 } ;$

$$
V \big (q _ {2} ^ {*}; v _ {2} \big) - T _ {2} ^ {*} = V \big (q _ {1} ^ {*}; v _ {2} \big) - V \big (q _ {1} ^ {*}; v _ {1} \big),
$$

which is positive given the single-crossing property.

Therefore, these three conditions are both the necessary conditions of an optimal pricing schedule and sufficient conditions for all incentive constraints to be satisfied. This concludes the proof.

Proof of Lemma 2. Recall that $V ( q ; q _ { \theta } , v _ { \theta } ) = 0$ , for any $q < q _ { \theta }$ Thus, a type θ customer never buys at a quantity lower than q . In addition, $V ( q ; q _ { \theta } , v _ { \theta } ) = v _ { \theta } ,$ , for any $\jmath \geq q _ { \theta }$ . Therefore, if $T ( q )$ is nondecreasing in q, then $V ( q _ { \theta } ; q _ { \theta } , v _ { \theta } ) - T ( q _ { \theta } ) \geq V ( q ; q _ { \theta } , v _ { \theta } ) - T ( q )$

for $q \geq q _ { \theta } .$ . On the other hand, if $V ( q _ { \theta } ; q _ { \theta } , v _ { \theta } ) - T ( q _ { \theta } ) \geq V ( q ;$ ${ q _ { \theta } , v _ { \theta } ) - T ( q ) }$ , for $q \geq q _ { \theta . }$ , then $T ( q _ { \theta } ) \leq { \dot { T } } ( q )$ , for $q \geq q _ { \theta }$ . That is, $T ( q )$ is nondecreasing in q. This concludes the proof.

Proof of Theorem 1. Given Assumption $^ { 3 , }$ one can show that $I ( T ; q )$ is twice continuously differentiable for $T \in [ 0 , { \overline { { v } } } ] .$ This is because $I ( T ; q ) = T ( 1 - \dot { G } ( T ; q ) )$ <sub>)</sub>, and

$$
G (T; q) = \int_ {0} ^ {T} g (x; q) d x = \frac {1}{\int_ {\{\theta : q _ {\theta} = q \}} f (q , y) d y} \int_ {0} ^ {T} f (q, x) d x,
$$

which is twice continuously differentiable in $T$ given Assumption 3.

Given $\overline { { T } } ( q ) = ( 1 - G ( \overline { { T } } ; q ) ) / g ( \overline { { T } } ; q )$ , clearly $\partial I / \partial T | _ { T = \overline { { T } } } = 0 .$ We first show that T is the solution to the pointwise opti mization problem, or mathematically,

$$
\overline {{T}} (q) = \underset {T} {\arg \max} I (T; q).
$$

Suppose this is not true; then, there exists a $\widehat { T } \in [ 0 , \overline { { v } } ] .$ , such that $\overset { \bullet } { I } ( \overset {  } { T } ; q ) > I ( \overline { { T } } ; q )$ . If ${ \widehat { T } } < { \overline { { T } } } ,$ , then because $I ( T ; q )$ is twice continuously differentiable fo $T \in [ 0 , { \overline { { v } } } ]$ , and $\partial ^ { 2 } I / \partial \dot { T } ^ { 2 } | _ { T = \overline { { { T } } } } < 0 ,$ we have σ $> 0 ,$ such that $I ( T ; q ) < I ( \overline { { T } } ; q )$ for $\forall T \in [ { \overline { { T } } } - \sigma , { \overline { { T } } } ) .$ and $\widehat { T } < \overline { { T } } - \sigma$ . Given that $I ( T ; q )$ is continuous, $\exists \widetilde { T } \in [ \widehat { T } , \overline { { T } } - \sigma ]$ such that $I ( \widetilde { T } ; q ) = I ( \overline { { T } } ; q )$ . Now apply Rolle’s theorem, and we have $\exists T \in ( \widetilde { T } , \overline { { T } } )$ , such that $\partial I / \partial T = 0 ,$ , or

$$
T = \frac {1 - G (T ; q)}{g (T ; q)}.
$$

This contradicts with the fact that $\overline { T }$ is the unique solution to the first-order condition. Applying the same logic, one can reach a contradiction assuming $\widehat { T } > \overline { { T } }$ . Therefore, $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ maximizes $I ( T ; q )$ . Moreover, given Assumption 4, T q is a nondecreasing function of q. This concludes the proof.

Proof of Theorem 2. Clearly, if $\overline { { T _ { i } } }$ maximizes the vendor’s profit among customers whose required consumption level is $q _ { i } ,$ then the price-quantity schedule $\{ ( \overline { { T _ { i } } } , q _ { i } ) , i = 1 , \dots , n \}$ maximizes the vendor’s overall profit if this schedule also satisfies all the incentive compatibility constraints. One can show that given $\overline { { T _ { i } } }$ is nondecreasing in i, all incentive com patibility constraints are satisfied. This is because a consumer with required quantity $q _ { i }$ would not buy at a quantity $q _ { j } < q _ { i }$ because she receives no value from such consumption. For $q _ { j } > q _ { i }$ , we have

$$
v _ {i} - \overline {{T _ {i}}} \geq v _ {i} - \overline {{T _ {j}}}
$$

because $\overline { { T _ { i } } }$ is nondecreasing in i. Therefore, the vendor’s optimal nonlinear pricing strategy is $\{ ( \overline { { T _ { i } } } , q _ { i } ) , i = 1 , \dots , n \}$ This concludes the proof.

Lemma A.1. Given the conditions in Theorem 1 are satisfied, $\overline { { T } } ( q ) / q$ decreases with $q \ i f \ d ^ { 2 } \overline { { T } } ( q ) / d q ^ { 2 } < 0 .$

Proof of Lemma A.1. Given any $q _ { 1 } < q _ { 2 } ,$ , where $q _ { 1 } , q _ { 2 } \in$ q , q , if $d \overline { { T } } ( q ) / d q$ 0 and $d ^ { 2 } \overline { { T } } ( q ) / \dot { d q } ^ { 2 } < 0 ,$ , one can show tha

$$
\frac {\int_ {q _ {1}} ^ {q _ {2}} \overline {{T}} ^ {\prime} (x) d x}{q _ {2} - q _ {1}} <   \frac {\int_ {0} ^ {q _ {1}} \overline {{T}} ^ {\prime} (x) d x}{q _ {1}}.
$$

Thus, we have

$$
\begin{array}{c} \frac {\int_ {0} ^ {q _ {2}} \overline {{T}} ^ {\prime} (x) d x}{q _ {2}} = \frac {\int_ {q _ {1}} ^ {q _ {2}} \overline {{T}} ^ {\prime} (x) d x + \int_ {0} ^ {q _ {1}} \overline {{T}} ^ {\prime} (x) d x}{q _ {2} - q _ {1} + q _ {1}} \\ <   \frac {\int_ {0} ^ {q _ {1}} \overline {{T}} ^ {\prime} (x) d x}{q _ {1}}, \end{array}
$$

which implies $\overline { { T } } ( q _ { 2 } ) / q _ { 2 } < \overline { { T } } ( q _ { 1 } ) / q _ { 1 }$ . This concludes the proof.

Proof of Theorem 3. We just need to show that the condition is sufficient for $d ^ { 2 } \overline { { T } } ( q ) / d \bar { q ^ { 2 } } < 0$ and then apply Lemma $_ { \mathrm { A . 1 } }$ Given Assumptions 3 and $4 , \partial I / \partial T = 0 .$ , for $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ defined in (5). Totally differentiate on both sides, we have

$$
\frac {\partial^ {2} I}{\partial T \partial q} + \frac {\partial^ {2} I}{\partial T ^ {2}} \frac {d T}{d q} = 0,\tag{A.1}
$$

or

$$
\frac {d T}{d q} = - \frac {\partial^ {2} I}{\partial T \partial q} / \frac {\partial^ {2} I}{\partial T ^ {2}}.
$$

Totally differentiate $( \mathrm { A . 1 } ) ,$ , and substitute dT/dq as defined in the equation; we have

$$
\begin{array}{r l} & {- \left(\frac {\partial^ {2} I}{\partial T ^ {2}}\right) ^ {2} \frac {\partial^ {2} I}{\partial T ^ {2}} \frac {d ^ {2} T}{d q ^ {2}} = \frac {\partial^ {3} I}{\partial T \partial q ^ {2}} \left(\frac {\partial^ {2} I}{\partial T ^ {2}}\right) ^ {2} - \left(\frac {\partial^ {3} I}{\partial T \partial q \partial T} \right.} \\ & {\qquad + \left. \frac {\partial^ {3} I}{\partial T ^ {2} \partial q}\right) \frac {\partial^ {2} I}{\partial T \partial q} \frac {\partial^ {2} I}{\partial T ^ {2}} + \left. \frac {\partial^ {3} I}{\partial T ^ {3}} \left(\frac {\partial^ {2} I}{\partial T \partial q}\right) ^ {2} \right.} \\ & {\qquad = I _ {T q q} I _ {T T} ^ {2} - (I _ {T q T} + I _ {T T q}) I _ {T q} I _ {T T} + I _ {T T T} I _ {T q} ^ {2}.} \end{array}
$$

We know that $\partial ^ { 2 } I / \partial T ^ { 2 } < 0 \mathrm { a t } \overline { { T } }$ . Therefore, $d ^ { 2 } T / d q ^ { 2 }$ is negative given the optimal pricing strategy (T) if

$$
I _ {T q q} I _ {T T} ^ {2} - \big (I _ {T q T} + I _ {T T q} \big) I _ {T q} I _ {T T} + I _ {T T T} I _ {T q} ^ {2} <   0.
$$

Applying the previous Lemma A.1, we conclude that $\overline { { T } } ( q ) / q$ decreases with q given these conditions. <sup>□</sup>

Proof of Theorem 4. Given Assumption 3, $I ( T ; q )$ is twice continuously differentiable. Because $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ is the unique solution to $\partial I ( T ; q ) / \partial T = 0 ,$ , and $\partial ^ { 2 } I / \partial T ^ { 2 } | _ { T = \overline { { T } } } < 0 .$ , one can show that for each $\phantom { } , \partial I ( T ; q ) / \partial T > 0$ for $T \in [ 0 , \overline { { T } } )$ , and $\partial I ( T ; q ) / \partial T <$ 0 for $T > { \overline { { T } } } .$ Next, we show that $\overline { { T } } ( q _ { L } ) \leq T _ { f } \leq \overline { { T } } ( q _ { H } )$ . Suppose this is not true. If $T _ { f } > \overline { { T } } ( q _ { H } )$ , then because $I ( T ; q )$ is twice continuously differentiable, and $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ is the unique solution to $\partial I / \partial T = 0 ,$ , we have $\partial I ( T ; q ) / \partial T | _ { T = T _ { f } } < 0$ for every q. Therefore, the seller can improve his profit by decreasing $T _ { f }$ . This contradicts the fact that $T _ { f }$ is optimal. If $T _ { f } < \overline { { T } } ( q _ { L } )$ , applying the same logic, one can also reach a contradiction. Therefore, $\overline { { T } } ( q _ { L } ) \leq T _ { f } \leq \overline { { T } } ( q _ { H } )$ □

Proof of Theorem 5. Because $\overline { { \boldsymbol { T } } } ( \boldsymbol { q } )$ is nondecreasing with $q ,$ applying Theorem 4, we have that there exists $\overline { { q } } \in \left[ q _ { L } , q _ { H } \right]$ such that $\overline { { T } } ( q ) \leq T _ { f }$ for $q \in [ q _ { L } , \overline { { q } } ]$ , and $\overline { { T } } ( q ) \geq T _ { f }$ , for $q \in [ \overline { { q } } , q _ { H } ] .$

The social surplus under flat-fee pricing is

$$
\int_ {q _ {L}} ^ {q _ {H}} \int_ {T _ {f}} ^ {\overline {{v}}} x f (q, x) d x d q.
$$

The social surplus under nonlinear usage-based pricing is

$$
\int_ {q _ {L}} ^ {q _ {H}} \int_ {\overline {{T}} (q)} ^ {\overline {{v}}} x f (q, x) d x d q.
$$

The difference in social surplus between the two pricing strategies is equal to

$$
\begin{array}{l} \int_ {q _ {L}} ^ {q _ {H}} \int_ {T _ {f}} ^ {\overline {{v}}} x f (q, x) d x d q - \int_ {q _ {L}} ^ {q _ {H}} \int_ {\overline {{T}} (q)} ^ {\overline {{v}}} x f (q, x) d x d q \\ = - \int_ {q _ {L}} ^ {\overline {{q}}} \int_ {\overline {{T}} (q)} ^ {T _ {f}} x f (q, x) d x d q + \int_ {\overline {{q}}} ^ {q _ {H}} \int_ {T _ {f}} ^ {\overline {{T}} (q)} x f (q, x) d x d q \\ > - \int_ {q _ {L}} ^ {\overline {{q}}} \int_ {\overline {{T}} (q)} ^ {T _ {f}} T _ {f} f (q, x) d x d q \\ + \int_ {\overline {{q}}} ^ {q _ {H}} \int_ {T _ {f}} ^ {\overline {{T}} (q)} T _ {f} f (q, x) d x d q, \end{array}
$$

which is positive if

$$
\int_ {\overline {{q}}} ^ {q _ {H}} \int_ {T _ {f}} ^ {\overline {{T}} (q)} f (q, x) d x d q > \int_ {q _ {L}} ^ {\overline {{q}}} \int_ {\overline {{T}} (q)} ^ {T _ {f}} f (q, x) d x d q.
$$

Note that

$$
\begin{array}{l} \int_ {q _ {L}} ^ {q _ {H}} \int_ {T _ {f}} ^ {\overline {{v}}} f (q, x) d x d q = \int_ {q _ {L}} ^ {\overline {{q}}} \int_ {T _ {f}} ^ {\overline {{v}}} f (q, x) d x d q \\ \qquad + \int_ {\overline {{q}}} ^ {q _ {H}} \int_ {T _ {f}} ^ {\overline {{T}}} f (q, x) d x d q \\ \qquad + \int_ {\overline {{q}}} ^ {q _ {H}} \int_ {\overline {{T}}} ^ {\overline {{v}}} f (q, x) d x d q, \end{array}
$$

and

$$
\begin{array}{l} \int_ {q _ {L}} ^ {q _ {H}} \int_ {\overline {{T}} (q)} ^ {\overline {{v}}} f (q, x) d x d q = \int_ {q _ {L}} ^ {\overline {{q}}} \int_ {\overline {{T}}} ^ {T _ {f}} f (q, x) d x d q \\ \qquad + \int_ {q _ {L}} ^ {\overline {{q}}} \int_ {T _ {f}} ^ {\overline {{v}}} f (q, x) d x d q \\ \qquad + \int_ {\overline {{q}}} ^ {q _ {H}} \int_ {\overline {{T}}} ^ {\overline {{v}}} f (q, x) d x d q. \end{array}
$$

Therefore,

$$
\begin{array}{c} \int_ {q _ {L}} ^ {q _ {H}} \int_ {T _ {f}} ^ {\overline {{v}}} f (q, x) d x d q > \int_ {q _ {L}} ^ {q _ {H}} \int_ {\overline {{T}} (q)} ^ {\overline {{v}}} f (q, x) d x d q \Leftrightarrow \\ \int_ {\overline {{q}}} ^ {q _ {H}} \int_ {T _ {f}} ^ {\overline {{T}} (q)} f (q, x) d x d q > \int_ {q _ {L}} ^ {\overline {{q}}} \int_ {\overline {{T}} (q)} ^ {T _ {f}} f (q, x) d x d q. \end{array}
$$

This concludes the proof.

## Endnotes

<sup>1</sup> For simplicity of exposition, in this example, we assume that it is optimal for the monopolist to set the prices such that both types of consumers buy.

<sup>2</sup> Our results continue to hold if $\overline { { v } } = \infty$

<sup>3</sup> One can prove this by showing that G(v; $q 2 )$ dominates $G ( v ; q 1 )$ according to the likelihood ratio order, which implies hazard rate dominance.

<sup>4</sup> One can show the existence of a unique solution to the first order condition by applying the monotonicity property of Mills’ ratio, i.e., convex and strictly decreasing (Baricz 2008). To derive the result on the second order condition, one can show that I is equal to zero and increasing at T = 0 and approaches zero as T approaches infinity, since Mills’ ratio is less than 1/x (Baricz 2008). Using properties of continuous and differentiable functions, one can prove this result.

<sup>5</sup> Theorem 3 characterizes a sufficient condition for quantity discounts. When this condition is violated, the optimal pricing schedule may require a quantity premium, or it may offer quantity discounts only within a certain range of quantities, but not across all quan tity levels.

<sup>6</sup> Given local demand inelasticity, the vendor generally does not find it optimal to offer a pricing schedule that includes both fixed-fee and usage-based pricing, unless it emerges as a special case of the optimal usage-based pricing schedule. For instance, when the optimal pricing schedule T q is such that for q  q, q<sub>H</sub> , T q  T q .

<sup>7</sup> For instance, many software products are priced based on the number of user licenses (i.e., usage based). In the United States, the distribution of enterprises’ employment sizes across all industries is publicly available through U.S. Census Bureau. In addition, in formation technology (IT) analysts routinely conduct surveys and case studies on the value of software adoption (e.g., Band et al. 2010, Tan 2011).

## References

Azoury KS (1985) Bayes solution to dynamic inventory models under unknown demand distribution. Management Sci. 31(9): 1150–1160.

Balasubramanian S, Bhattacharya S, Krishnan VV (2015) Pricing information goods: A strategic analysis of the selling and payper-use mechanisms. Marketing Sci. 34(2):218–234.

Band W, Hamerman PD, Magarie A (2010) Benchmarks for CRM Selection and Deployment: Size Up Your CRM Initiative Compared against 99 Projects (Forrester Research, Inc., Cambridge, MA).

Bansal M, Maglaras C (2009) Product design in a market with satisficing consumers. Netessine S, Tang CS, eds Consumer-Driven Demand and Operations Management Models (Springer, Boston). 37–62.

Barberis N, Huang M (2001) Mental accounting, loss aversion, and individual stock returns. J. Finance 56(4):1247–1292.

Baricz A (2008) Mills’ ratio: Monotonicity patterns and functional inequalities. J. Math. Anal. Appl. 340(2):1362–1370.

Berbeglia G, Rayaprolu G, Vetta A (2019) Pricing policies for selling indivisible storable goods to strategic consumers. Ann. Oper. Res. 274(2019):131–154.

Choudhary V (2010) Use of pricing schemes for differentiating information goods. Inform. Systems Res. 21(1):78–92.

Gabszewicz JJ, Thisse J-F (1979) Price competition, quality and in come disparities. J. Econom. Theory 20(3):340–359.

Gavirneni S, Kapuscinski R, Tayur S (1999) Value of information in capacitated supply chains. Management Sci. 45(1):16–24.

Huang K-W, Sundararajan A (2011) Pricing digital goods: Discon tinuous costs and shared infrastructure. Inform. Systems Res. 22(4):721–738.

Iglehart DL (1964) The dynamic inventory problem with unknown demand distribution. Management Sci. 10(3):429–440.

Jain S, Kannan PK (2002) Pricing of information products on online servers: Issues, models, and analysis. Management Sci. 48(9): 1123–1142.

Laffont J-J, Maskin E, Rochet J-C (1987) Optimal nonlinear pricing with two-dimensional characteristics. Groves T, Radner R, Reiter S, eds. Information, Incentives and Economic Mechanisms: Essays in Honor of Leonid Hurwicz (University of Minnesota Press, Minneapolis), 256–266

Lahiri A, Dewan RM, Freimer M (2013) Pricing of wireless services: Service pricing vs. traffic pricing. Inform. Systems Res. 24(2): 418–435.

Ma D, Seidmann A (2015) Analyzing software as a service with per transaction charges. Inform. Systems Res. 26(2):360–378

Maskin E, Riley J (1984) Monopoly with incomplete information. RAND J. Econom. 15(2):171–196.

McAfee RP, McMillan J (1988) Multidimensional incentive compat ibility and mechanism design. J. Econom. Theory 46(2):335–354.

Milgrom P (2004) Putting Auction Theory to Work (Cambridge Uni versity Press, Cambridge, UK).

Mussa M, Rosen S (1978) Monopoly and product quality. J. Econom. Theory 18(2):301–317.

Perloff JM, Salop SC (1985) Equilibrium with product differentiation. Rev. Econom. Stud. 52(1):107–120.

PwC (2015) The Software Industry: Pricing Benchmark Results. Accessed June 5, 2020, https://www.pwc.com/us/en/technology publications/assets/pwc-technology-institute-software-industry -pricing-report.pdf.

Rossi R, Prestwich S, Tarim SA, Hnich B (2014) Confidence-based optimisation for the newsvendor problem under binomial, Poisson and exponential demand. Eur. J. Oper. Res. 239(3):674–684.

Scarf H (1959) Bayes solutions of the statistical inventory problem Ann. Math. Statist. 30(2):490–508.

Schweitzer ME, Cachon GP (2000) Decision bias in the newsvendo problem with a known demand distribution: Experimental ev idence. Management Sci. 46(3):404–420.

Segal I (2003) Optimal pricing mechanisms with unknown demand. Amer. Econom. Rev. 93(3):509–529.

Sundararajan A (2004) Nonlinear pricing of information goods Management Sci. 50(12):1660–1673.

Tan S (2011) Lessons from 169 SAP Implementations Using Servic Providers in North America (Gartner Inc., Stamford, CT).

Tversky A, Kahneman D (1991) Loss aversion in riskless choice: A reference-dependent model. Quart. J. Econom. 106(4):1039–1061.

Wilson RB (1993) Nonlinear Pricing (Oxford University Press on Demand, Oxford, UK).
