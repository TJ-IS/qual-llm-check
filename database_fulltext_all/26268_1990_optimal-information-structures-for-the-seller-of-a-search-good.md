---
otero_id: 26268
otero_key: "XHPS89BW"
title: "Optimal Information Structures for the Seller of a Search Good"
authors: "Terence Barron; A. N. Saharia"
year: "1990"
journal: "Information Systems Research"
doi: "10.1287/isre.1.2.188"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/XHPS89BW/fulltext/images/cd734f1b94191a5f99e27f5bbc6f72d38b339bd3cf9bfee26c5cbf3747abfb61.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Optimal Information Structures for the Seller of a Search Good

Terence Barron, A. N. Saharia,

To cite this article:

Terence Barron, A. N. Saharia, (1990) Optimal Information Structures for the Seller of a Search Good. Information Systems Research 1(2):188-204. http://dx.doi.org/10.1287/isre.1.2.188

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1990 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/XHPS89BW/fulltext/images/b7f52ce86fd6b7648721f1ca8e40c92059a66527eb6972c492a9b0d04cdac936.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Optimal Information Structures for the Seller of a Search Good

Terence Barron

H'ittiam E. Simon Graduate School of Business Admini

University of Rocheste

Rochesier. New York 1462

A. N. Saharia

School and Graduate School of Business Administ

University of Washington. DJ

Seattle. Washington 9819

This paper examines an information system design problem faced by the seller of a search good who sells his product in a competitive market to well-informed consumers. The formulation results in a nonlinear optimization problem having a special structure which can be exploited in solving the first-order conditions. Closed-form solutions and comparative statics results are given in the case of a uniformly-distributed attribute, and we provide a numerical example in the case of a normally-distributed attribute.

Economics of mrurmHtiiin s>Mi'ms —Desiun of informaiion 'iyslems—l>tsiBn iif inforniation struclures—Information economies—Oplimal measure men I

## 1. Introduction

ow do the characteristics of a firm's products and the markets in which it operates determine the nature of its information systems? In this paper we study, using a specific microeconomic model, how the nature of a product's "quality" works to determine an optimal information system for a firm which faces wellinformed customers and a competitive market in which its product is sold.

Given our economic framework, the term "information system" in this paper has its customary information economics meaning of a mechanism whose signals bear some statistical relationship to the state of the world that is of interest to a decision maker. More specifically, we are concerned with the design of the "information structure" aspect of an information system, that is. the way in which it partitions the possible states ofthe world (see McGuire 1972 for more details.) The effects of all other design decisions are summarized by a cost function. C. discussed in §2. Thus we will refer to "information structures" rather than "information systems" in the sequel.

Information economics models have been criticized hy some for requiring difficult mathematics to solve unrealistic problems. However, the approach has strong appeal since it is the only well-developed method for studying the economic value of alternative information systems. The well-known difficulties in quantifying the value of information systems together with the fact that existing work using this approach treats simplified problems both argue in favor of developing a body of basic research via the identification and solution of simplified problems in order to attack progressively more realistic ones. This paper is intended as such a contribution; in §9 w discuss some ways of extending the work presented here.

In addition, the information economics approach yields two kinds of specific results: normative (i.e., management science) results which tell us what an optimal solution is. and positive results in the form of potentially testable implications from the comparative statics ofthe model. This paper contains results of both types.

How precisely data should be measured is an aspect ofthe determination of data requirements in system analysis and design and database design that at present is treated in an ad hoc way if it is explicitly treated at all. We show how a particular class of such problems can be attacked and explicit results produced. Thus it can be seen as a companion to the paper by Mendelson and Saharia {1986). They employ an information economics model in studying the effects ofthe tradeoff between the value of the data and data-related costs on data requirements. They deal with issues of substitution between attributes and the possibility of not storing one or more attributes, but they do not consider the issue of how finely to measure the attributes in the first plaee, effectively assuming perfect measurement. If the incomplete information costs due to imprecise measurement can be characterized by the loss function we use in this paper (see §2) and the cost of measurement function is suitably interpreted, then our results are directly relevant to determining the fineness of measurement when the attributes are independent. (If there are statistical dependencies between attributes, then intuition suggests that the dependency could be exploited to reduce the value of finer measurement in other attributes.) This paper can be extended by considering other loss functions and by considering cases where attributes are not independent of one another.

The specific situation we study here is exemplified by (but not necessarily limited to) a seller of "products of nature." for example produce such as vegetables and fruits. Christmas trees, and so on, which come to the seller with the values of some attributes being uncertain. Consumers typically evaluate the quality of such products along several dimensions, such as ripeness, lack of bruises, and size. In this paper we abstract from al! but one of these dimensions of quality and study questions of how the seller should optimally measure a single attribute.

Since such products exhibit randomness in their attributes for both buyer and seller, each has an information structure selection problem. This raises the issue of how consumers' information structure choices and their resulting knowledge of quality affects the information structure choice ofthe seller, and vice versa. In this paper we deal with this issue by restricting the problem to .search goods (Wilde 1980, p 1265-1266). By definition, search goods are goods about which the consumer is certain of his utility at the time of purchase. Thus for search goods the buyer has already acquired sufficient information about the product, making his or her informationstructure decisions exogenous to the model. This simplification can be looked at in several ways.

I. Buyers find that their unaided senses are sufficient to allow them to determine the utility a product yields, while sellers are ignorant ofthe details of buyers' utilities but face market prices/>(/0 which depend on the value ofthe attribute. This appears to correspond closely to the case of produce mentioned above since in practice one sees very little investment in information systems by consumers of such goods, whereas sellers do invest in a variety of measurement, recording, and storage and retrieval devices, or

2. Consumers have already made their information system decisions, while the seller in question is a new entrant into the market and has to make an information structure decision based on observable market conditions and assumptions about relevant but unobservable conditions, or

3. These assumptions are simplifications that allow the derivation of concrete and informative results which can be used as approximations for more general problems. (We will treat more general forms ofthe problem in future work.)

§2 below introduces the assumptions and notation used in the rest ofthe paper, §3 discusses the effects of an information structure in the model and introduces the optimization problem that results from §2 and §3. In §4 we present and discuss the first-order conditions ofthe problem, and in §5 we present a method for determining the solutions ofthe first-order conditions. In §6 we discuss the determination of an optimal information structure in the general case. In §7 we treat the ease in which the attribute is uniformly distributed and price is linearly increasing in the attribute. This case yields simple and interesting closed-form solutions to the optimization problem involving the fineness-of-measurement variable, leading to easily calculated solutions and comparative statics results. In §8 we present a specific numerical example for a normally distributed attribute and a price function which is linear in the attribute. The normal distribution case does not yield simple closed-form results ofthe type seen in §7, so the algorithmic approach of §5 must be used. Finally, in §9 we present some comments and conclusions.

## 2. Preliminaries and Assumptions

The term "quality" has connotations which are more specific than is necessary or useful for our purposes, so we will use "attribute" instead in the sequel. The central point is that the attribute is some feature that gives utility to the product's consumers and is priced.

We assume the following:

• The seller has A' items already on hand. The seller sees the attribute as having values drawn from a distribution with density/(/;) and cumulative distribution function F{h). The range ofh in the population is the interval $( h _ { L } , h _ { U } )$ (it could be closed or open), so that/( //) = 0 outside of this interval. It may be that $h _ { L } = - \infty \mathrm { o r } h _ { U } = + \infty$ or both.

• Prices in the market are related to values ofthe attribute hby a function p{h) which is monotonically increasing and differentiable in h. The seller knows the function p(h) and assumes his customers do too.'

• The seller assumes demand is perfectly elastic at each value of h, so that he expresses his loss per item in terms of/z (the true attribute value) and an estimate of that value. //, as:^

<table><tr><td rowspan="2"></td><td colspan="2"> $H_1$ </td><td colspan="2"> $H_2$ </td><td colspan="2"> $H_K$ </td></tr><tr><td> $\uparrow$ </td><td> $\hat{h}_1$ </td><td> $\uparrow$ </td><td> $\hat{h}_2$ </td><td> $\uparrow$ </td><td> $\hat{h}_{K-1}$ </td></tr><tr><td> $h_0 = h_L$ </td><td></td><td></td><td> $h_1$ </td><td></td><td> $h_2$ </td><td> $\cdots$ </td></tr></table>

FIGURE I. This Illustrates the Notation Used for Categories, Category Boundaries, and Optimal Estimates Within Each Category.

$$
L (\hat {h}, h) = \left\{ \begin{array}{l l} p (h) & \text { if } \quad \hat {h} > h \quad \text {(i.e.,} p (\hat {h}) > p (h)) \\ p (h) - p (\hat {h}) & \text { if } \quad \hat {h} <   h \quad \text {(i.e.,} p (\hat {h}) <   p (h)). \end{array} \right.
$$

• Feasible information structures and pricing policies have the form: partition $( h _ { L }$ $h _ { U } )$ into K subintet^als, $H _ { 1 } , H _ { 2 } , \dots , H _ { K }$ , then charge a single price $\hat { p _ { i } }$ for all items whose values fall in $H _ { i }$ . The set of interval endpoints for a design is denoted by $\left. h _ { i } \right.$ where $H _ { i } = [ h _ { i - 1 } , h _ { i } )$ ; see Figure 1. Note that, for each $H _ { i } ,$ our assumptions imply that all items in $H _ { i }$ will sell out when $\hat { p _ { i } } \le p ( h _ { i - 1 } )$ ). Thus the seller will never charge a price which is lower than that for the lowest attribute value in $H _ { i } . ^ { 3 }$

We are assuming that measurement is "noiseless" but "imprecise," that is, ifthe information system reports that an item falls into $H _ { i }$ then that report is correct with probability equal to 1. but no finer information is obtainable from that information structure. The more general problem of noisy structures is clearly of interest since they introduce the possibility of tradeoffs between precision and noise, but the gen eral form ofthis problem lacks sufficient structure to be analytically tractable (see Appendix A for a brief discussion), requiring treatment of special cases ofthe behavior ofthe measurement technology. (We are currently working on some specific characterizations.)

• Costs of measurement and data storage are $C ( K ; N )$ per item, incremental to th null information structure, and are assumed to be increasing in $K . ^ { 4 }$

The seller's goal is to select an information structure and pricing policy which will minimize expected loss. There are two questions of interest which we will proceed to answer below:

1. For a given fineness of me^urement, A^, what is the optimal information struc ture?

2. What is the optimal AT?

## 3. The Effects of an Information Structure

A given information structure tells the seller at the time of sale which $H _ { i }$ an item falls into, implying the conditional distributio $f ( h | H _ { i } )$ on its attribute value. In order to determine the price to charge for the item, the seller needs to make an optimal estimate, $\hat { h } _ { i } ,$ , of its value, h, so he faces the decision problem:^

$$
\min _ {\hat {h} _ {i}} E _ {h | H _ {i}} L (\hat {h} _ {i}, h).\tag{1}
$$

Let $L ^ { * } ( i , \langle h _ { j } \rangle )$ denote the value ofthe above objective at an optimal $\hat { h } _ { i }$ for the information structure defined by $\left. h _ { j } \right.$ . Note that $\hat { h } _ { i }$ depends only on $H _ { i } = [ h _ { i - 1 } , h _ { i } )$ for a given $p ( h )$ and $f ( h )$ ., so it can be written as $\hat { h } _ { i } ( h _ { i - 1 } , h _ { i } )$ . Thus it will be the same for each item in $H _ { i }$ . Therefore the seller will charge $p ( h _ { i } )$ for all items in $H _ { i \cdot } ^ { 6 }$

Information structure selection occurs prior to any sales. Thus for fixed A^the seller has the problem:^

$$
\min _ {\langle h _ {j} \rangle} \sum_ {i = 1} ^ {K} \operatorname{prob} (H _ {i}) L ^ {*} (i, \langle h _ {j} \rangle)\tag{2}
$$

where prob $\begin{array} { r } { ( H _ { i } ) = \int _ { h _ { i - 1 } } ^ { h _ { i } } f ( h ) d h } \end{array}$

Recalling that $F ( h )$ '\s the cumulative distribution of/, (2) can be rewritten as:

$$
\min _ {\langle h _ {i} \rangle} E _ {h} L = E _ {h} p (h) - \sum_ {i = 1} ^ {K} p (\hat {h} _ {i} (h _ {i - 1}, h _ {i})) [ F (h _ {i}) - F (\hat {h} _ {i} (h _ {i - 1}, h _ {i})) ]\tag{3}
$$

where $h _ { 0 } \equiv h _ { L }$ and $h _ { K } \equiv h _ { U } . ^ { 8 }$ ^ The value of equation (3) at an optimal design for categories will be called $L ^ { * } ( K )$ ).

## 4. Determining Optimal Categories for a Given K

Equation (3) is equivalent to:

$$
\max _ {\langle h _ {i} \rangle} \sum_ {i = 1} ^ {K} p (\hat {h} _ {i} (h _ {i - 1}, h _ {i})) [ F (h _ {i}) - F (\hat {h} _ {i} (h _ {i - 1}, h _ {i})) ].\tag{4}
$$

This can be simplified as a result ofthe following observation. Consider any category $H _ { i } = [ h _ { i - 1 } , h _ { i } )$ ^) whose optimal estimat $\hat { h } _ { i } ,$ h,, is greater tha $h _ { i - 1 }$ \_,. The price for a items in $H _ { i }$ isthen $p ( \hat { h } _ { i } )$ which implies that all items in that category having $h < \hat { h } _ { i }$ will go unsold. However, this loss can be avoided by increasing $h _ { i - 1 }$ to $\hat { h } _ { i } ,$ , so that the previously unsold items will now be sold at the price for items in category $H _ { i - 1 }$ $p ( \hat { h } _ { i - 1 } )$ resulling in a larger value of (4). Thus we have the following:

LEMMA. NO optimal design can have $\hat { h } _ { i } ( h _ { i - 1 } , h _ { i } ) > h _ { i - 1 } f o r i = 2 \ t o K .$

Therefore we need to consider only designs having $\hat { h } _ { i } = h _ { i - 1 }$ , for $i = 2$ to $K ,$ so equation (4) becomes:

$$
\max _ {\langle h _ {i} \rangle} p (\hat {h} _ {1} (h _ {0}, h _ {1})) [ F (h _ {1}) - F (\hat {h} _ {1} (h _ {0}, h _ {1})) ] + \sum_ {i = 1} ^ {K - 1} p (h _ {i}) [ F (h _ {i + 1}) - F (h _ {i}) ].\tag{5}
$$

As we remarked above, equation (5) is constrained by having $h _ { U } \geq h _ { i } \geq h _ { L }$ ^ for each /. In addition, the preceding discussion implies the constraint $\hat { h } _ { 1 } \ge h _ { L }$ . As shown beiow. the first-order conditions to equation (5) yield explicit expressions for $h _ { 2 }$ through $h _ { K - 1 }$ as a function of $h _ { 1 }$ , and also an implicit expression for $\hat { h } _ { 1 }$ as a function of $h _ { 1 }$ . Further, those expressions imply $h _ { 2 } < h _ { 3 } < \cdots < h _ { K - 1 } < h _ { K } equiv h _ { U }$ Asa result, the solution procedure given at the end of §6 accounts for $h _ { U } \geq h _ { 1 } \geq h _ { L }$ simply by using this range to restrict the search for $h _ { 1 }$ . and also tests whether $\hat { h } _ { 1 } \ge h _ { L }$ is met. If the latter constraint is binding then the following simpler problem results:

$$
\max _ {\langle h _ {i} \rangle} p (h _ {L}) [ F (h _ {1}) - F (h _ {L}) ] + \sum_ {i = 1} ^ {K - 1} p (h _ {i}) [ F (h _ {i + 1}) - F (h _ {i}) ].\tag{6}
$$

As it turns out, the first-order conditions for equation (6) are identical to those for equation (5) except for the condition resulting from the partial derivative with respect to $h _ { 1 }$ . Thus the solution procedure is only slightly modified when the constraint is binding.

The complete set of first-order conditions can be found in Appendix B. Here we present a particular rearrangement of them which gives some insight into their meaning. Rearranging the first-order conditions for $i = 2$ 2 to $K - 1$ I. equation (B4), give

$$
\boxed {p ^ {\prime} \left(h _ {i}\right) \left[ F \left(h _ {i + 1}\right) - F \left(h _ {i}\right) \right]} = \boxed {f \left(h _ {i}\right) \left[ p \left(h _ {i}\right) - p \left(h _ {i - 1}\right) \right]}
$$

Marginal benefit

Marginal cost

Marginal benefit |: $p ^ { \prime } ( h _ { i } )$ is the increment in price resulting from an increase in $h _ { i } ,$ and it is applied to the fraction of items lying in $H _ { i + 1 } , F ( h _ { i + 1 } ) - F ( h _ { i } )$

\ Marginal cost : the cost of an increase i $h _ { i }$ ?, is that we now charg $p ( h _ { i - 1 } )$ ,) instead o $p ( h _ { i } )$ on those items that move out of $H _ { i + 1 }$ and into $H _ { i } ,$ At the margin the fraction of such items $f ( h _ { i } )$

Similarly rearranging equation (Bl) gives:

$$
\boxed { \begin{array}{l} p ^ {\prime} (h _ {1}) [ F (h _ {2}) - F (h _ {1}) ] \\ + p ^ {\prime} (h _ {1}) \frac {d \hat {h} _ {1}}{d h _ {1}} [ F (h _ {1}) - F (\hat {h} _ {1}) ] \end{array} } = \boxed {f (h _ {1}) [ p (h _ {1}) - p (\hat {h} _ {1}) ] + p (\hat {h} _ {1}) f (\hat {h} _ {1}) \frac {d \hat {h} _ {1}}{d h _ {1}}}
$$

Marginal benefit

Marginal cost

The first terms in both the marginal benefit and marginal cost expressions have the same interpretation as above. However, since $\hat { h } _ { 1 }$ is a function of $h _ { 1 } , h _ { 1 }$ 's effect on it must be accounted for, giving rise to the second terms. Thus $p ^ { \prime } ( \hat { h } _ { 1 } ) [ F ( h _ { 1 } ) - F ( \hat { h } _ { 1 } ) ]$ is the incremental revenue for a unit increase in $\hat { h } _ { 1 }$ , but a unit increase in $h _ { 1 }$ gives rise to a change o' $d \hat { h } _ { 1 } / d h _ { 1 }$ in $\hat { h } _ { 1 }$ |. Hence the product of these two gives the term in th marginal benefit expression.

Similarly, $p ( \hat { h } _ { 1 } ) f ( \hat { h } _ { 1 } )$ is the marginal cost for a unit increase in $\hat { h } _ { 1 }$ accounting for those items which now fall below $\hat { h } _ { 1 }$ and which will not be sold {i.e. their new price is effectively zero). However, the change in $\hat { h } _ { 1 }$ is not necessarily a unit change but dh $_ 1 / d h _ { _ 1 }$ ^, giving rise to the marginal cost term

## 5. Solving the First-Order Conditions for a Given K

The first-order conditions have a special structure which makes their solution comparatively easy. The implication ofthe results in Appendix C is that finding all solutions to the first-order conditions can be done by a search over the feasible values of $h _ { 1 }$ By definition, $h _ { 1 } \geq h _ { L }$ ^.sothesearchisboundedbelowby $h _ { \iota }$ ^. Further, there ma be an $h _ { \operatorname* { m i n } }$ such that $p ( h ) = 0$ for all $h \leq h _ { \operatorname* { m i n } }$ ^, in which case the search can begin at th larger of $h _ { \operatorname* { m i n } }$ and $h _ { \cal L }$ . Thus we have the following algorithm:'

1. Set $h _ { 1 } = \operatorname* { m a x } ( h _ { \operatorname* { m i n } } , h _ { L } )$

2. While $h _ { 1 } \leq h _ { U }$ (j and the argument o $F ^ { - 1 }$ in equations {C2) and (C4)is $\leq 1 .$ ,do: 2.1. Solve equation (C5) for $\hat { h } _ { 1 } ;$

2.2. If $\hat { h } _ { 1 } \ge h _ { L }$ then

$$
\begin{array}{l} \text { Evaluate   equation(C6); } \\ \text { Find h_{2} from equation(C4);} \\ \text { else   Find h_{2} from equation(C7);} \end{array}
$$

2.3. Values for $h _ { 3 }$ through $h _ { K - 1 }$ , are found from equations (C2);

2.4. Check equation (C3) to see ifthe values calculated above yield a feasible solution to the first-order conditions.

2.5. Increment $h _ { 1 }$ .

3. A maximum can be determined by evaluating the objective, equation (5), at all ofthe solutions found from this process.

## 6. Determining an Optimal K

Recall from §3 that $L ^ { * } ( K )$ ) is the value of equation (3) for an optimal design for A categories, and that $C ( K )$ is the measurement cost per item. In order to choose an optimal number of categories, we must select AT with maximum net value per item (incremental to the null information structure) where the net value is:

$$
N V (K) = (L ^ {*} (1) - L ^ {*} (K)) - C (K).\tag{7}
$$

The term $( L ^ { * } ( 1 ) - L ^ { * } ( K ) )$ ) is called the ;?ra.9.?va/«e of an optimal information structure having AT categories and is denote $G V ( K )$ )

The solutions developed in the preceding sections have not directly minimized L in equation (3) but have instead maximized the summation term in equation (3), i.e. equation (5) or equation (6). Calhng the value ofthe objective (5) at an optimal solution G{K) we have:

$$
L ^ {*} (K) = E _ {h} p (h) - G (K)
$$

or

$$
G V (K) = G (K) - G (1).
$$

Although it is intuitively plausible that GK is in general concave in K, we are at present unable to show this for the general case considered to this point. (In the next section we examine a case which yields a closed-form expression for 6'K which is easily shown to be concave.) In the general case then search over successive values of A" is required in order to determine a value of A: that is sufiiciently good

In some cases the nature of measurement technology may be such that beyond a modest number of categories, say K^j, it is at least as cheap to measure exactly as it is $K _ { U } ,$ to measure approximately. In such a situation it suffices to evaluate equation (7) for $K = 1$ through $K _ { U } ,$ (,, and then for exact measurement. This is becaus $G V ( K )$ ) is strictly increasing in $K , ^ { 1 0 }$ "making $N V ( \infty ) > N V ( K )$ )for $\begin{array} { r } { \infty > K \ge K _ { U } . \quad } \end{array}$

## 7. General Resnlts When Attribute Values Are Uniformly

## Distributed and Price Is Affine

In this case it is possible to derive succinct and interesting closed form expressions for the category boundaries and $G V ( K )$ ). As a result, it is possible to derive useful properties of $G V ( K )$ and also to solve in a direct way for the optimal A: when a cost function, $C ( K )$ , is specified. Assume:

1. Attribute values are uniformly distributed $\implies f ( h ) = 1 / ( c - b )$

2. Price is affine in the attribute value $\implies p ( h ) = a h + d .$ We will assume $d$ is such that $a b + d \geq 0$ , that is, the price of an item having the minimum attribute value is non-negative, and $a > 0$

## 7.1. The Constraint on^ hj Is Not Bindi $\hat { h } _ { r }$

When the constraint $\hat { h } _ { 1 } \geq b$ is not binding the first-order conditions yield the following explicit solutions for $\hat { h } _ { 1 }$ and the $h _ { i }$ .

$$
\hat {h} _ {1} = \frac {c - K \left(\frac {d}{a}\right)}{K + 1};\tag{8}
$$

$$
h _ {i} = \left(\frac {i + 1}{K + 1}\right) c - \frac {2 (K - i)}{K + 1} \left(\frac {d}{a}\right) \quad \text { for } \quad i = 1 \text {   to   } K - 1.\tag{9}
$$

Substituting these into the objective ( 5 ) yields:

$$
G (K; a, b, c, d) = \frac {(a c + d) ^ {2} K}{2 a (c - b) (K + 1)}.\tag{10}
$$

$H _ { \kappa } ^ { * }$ ^ the set of interval endpoints of an optimal solution of the /I'-category problem. Pick any interval $H _ { i }$ from this solution and add a point $h _ { K + 1 }$ to it. Clearly $H _ { K } ^ { * } \cup \{ h _ { K + 1 } \}$ [ is a candidate solution for the $K + 1$ category probiem. in general suboplimal. If we set price $p ( h _ { K + 1 } )$ for category $[ h _ { K + 1 } , h _ { i } )$ -we add the positive increment $( p ( h _ { K + 1 } ) - p ( h _ { i - 1 } ) ) [ F ( h _ { i } ) - F ( h _ { K + 1 } ) ]$ to the summation term o $L ^ { * } ( K )$ ). Thus an optimal solution to the $K + 1$ I-category problem will add at least as large an increment to Ihe summation tennof $L ^ { * } ( K )$

" Here x is used loosely to denote an arbitrarily large but finite value of A'since it is not clear that the required limit necessarily exists.

Relaxing the integer constraint on $K$ and differentiating $G ( K )$ with respect to K gives:

$$
\frac {\partial G}{\partial K} = \frac {(a c + d) ^ {2}}{2 a (c - b) (K + 1) ^ {2}} > 0 \quad \text { for   all } \quad K > 0.\tag{11}
$$

This is of course no surprise since we know $G$ to be increasing in K from footnote 10, but it does give an explicit expression for the incremental gross value of an additional category. More importantly

$$
\frac {\partial^ {2} G}{\partial K ^ {2}} = \frac {- (a c + d) ^ {2}}{a (c - b) (K + 1) ^ {3}} <   0 \quad \text { for   all } \quad K > 0\tag{12}
$$

Hence $G$ is concave in $K ,$ , making $G V ( K )$ concave in $K .$

Given equation (10), GKitself is:

$$
G V (K; a, b, c, d) = G (K; a, b, c, d) - G (1; a, b, c, d) = \frac {(a c + d) ^ {2} (K - 1)}{4 a (c - b) (K + 1)}
$$

so that $N V ( K ; a , b , c , d )$ is:

$$
N V (K; a, b, c, d) = \frac {(a c + d) ^ {2} (K - 1)}{4 a (c - b) (K + 1)} - C (K).
$$

In what follows we will assume that $C ( K )$ is twice differentiable in $K ,$ increasing in K (i.e. $\partial C / \partial K > 0 )$ , and weakly convex (i.e. $\partial ^ { 2 } C / \partial K ^ { 2 } \geq 0 . )$ The first and second derivatives of NI' are:

$$
\frac {\partial N V}{\partial K} = \frac {(a c + d) ^ {2}}{2 a (c - b) (K + 1) ^ {2}} - \frac {\partial C}{\partial K},
$$

$$
\frac {\partial^ {2} N V}{\partial K ^ {2}} = \frac {- (a c + d) ^ {2}}{a (c - b) (K + 1) ^ {3}} - \frac {\partial^ {2} C}{\partial K ^ {2}}.
$$

Setting $\partial N V / \partial K = 0$ yields $K ^ { * } ( a , b , c , d )$ . At this point, we must check equation (8) lo see whether $\hat { h } _ { 1 } \geq b$ { so. $K ^ { * }$ is a maximum since $\partial ^ { 2 } N V / \partial K ^ { 2 } < 0$ . If not, then the results ofthe next subsection pertain.

When the constraint is nonbinding the first- and second-order conditions above yield the following comparative statics results. In the interests of clarity we will firs review the meaning of each ofthe four partial derivatives involved.

$\partial K ^ { * } /$ da is the change in $K ^ { * }$ \*, the optimal fineness of measurement, as the value of an incremental unit ofthe attribute increases.

$\partial K ^ { * } / \partial b$ is the change in $K ^ { * }$ as the lower bound of attribute values is increased.

$\partial K ^ { * } / \partial c$ is the change in $K ^ { * }$ as the upper bound of attribute values is increased.

$\partial K ^ { * } / \partial d$ is the change in $K ^ { * }$ due to a parallel shift upward in the price-attribute relationship.

The values and signs of these expressions are as follows:

$$
\frac {\partial K ^ {*}}{\partial a} = \frac {- \frac {(a c - d) (a c + d)}{2 a ^ {2} (c - b) (K ^ {*} + 1) ^ {2}}}{\frac {- (a c + d) ^ {2}}{a (c - b) (K ^ {*} + 1) ^ {3}} - \frac {\partial^ {2} C (K ^ {*})}{\partial K ^ {2}}} \geqslant 0.
$$

The sign of $\partial K ^ { * } /$ da depends on the sign of $( a c - d )$ in the numerator. We can rewrite $( a c - d ) \operatorname { a s } { ( a c + d ) } - 2 ( a ( 0 ) + d )$ ), which is read as "the price of an item having the highest attribute value less twice the price of an item having a value of zero." (Note that the latter would be an extrapolation if zero lies outside of $[ b , c ] . )$ Thus we can interpret this condition as one of sufficient variability in product price. Ifthe price of an item having the highest attribute value is at least twice the price of an item having a value equal to zero, the optimal fineness is increasing with the value of an incremental unit ofthe attribute, otherwise it is decreasing.

The fact that $\partial K ^ { * } /$ da can have either sign is mildly surprising. Intuition suggests that the larger the variation in price among items of different attribute values (i.e. the larger is $^ { a ) }$ the more valuable it would be to know such differences, suggesting that $\partial K ^ { * } / \partial a$ would always be positive. Cleariy matters are somewhat more subtle than (our) intuition suggests.

$$
\frac {\partial K ^ {*}}{\partial b} = \frac {- \frac {(a c + d) ^ {2}}{2 a (c - b) ^ {2} (K ^ {*} + 1) ^ {2}}}{\frac {- (a c + d) ^ {2}}{a (c - b) (K ^ {*} + 1) ^ {3}} - \frac {\partial^ {2} C (K ^ {*})}{\partial K ^ {2}}} > 0.
$$

This expression says that the optimal number of categories is unambiguously increasing in the minimum attribute value. This is a rather counterintuitive result since as b increases, the range ofthe attribute, $c - b$ , decreases, so this implies subdividing a smaller interval into more categories. However, see the last paragraph ofthis subsection for additional remarks.

$$
\frac {\partial K ^ {*}}{\partial c} = \frac {- \frac {(a c + d) (a c - 2 a b - d)}{2 a (c - b) ^ {2} (K ^ {*} + 1) ^ {2}}}{\frac {- (a c + d) ^ {2}}{a (c - b) (K ^ {*} + 1) ^ {3}} - \frac {\partial^ {2} C (K ^ {*})}{\partial K ^ {2}}} \geqslant 0.
$$

Somewhat surprisingly, given the unambiguous result for $\partial K ^ { * } / \partial b$ j this says that the optimal number of categories can either increase or decrease as the maximum attribute value increases. The sign of $\partial K ^ { * } / \partial$ c depends on the sign of $( a c - 2 a b - d )$ ), which can be rewritten as $( a c + d ) - 2 ( a b + d )$ . The first term is the price ofthe maximum attribute value item, while the second is twice the price ofthe minimum attribute value item. Thus ifthe price ofthe maximal item is at least twice as large as the price ofthe minimal item, the optimal number of categories will be increasing in c. Otherwise the optimal number of categories is decreasing in c. Thus as was the case with $\partial K ^ { * } / \partial a$ , prices must satisfy a minimal variability property in order for it to be worthwhile to measure more finely when the maximum attribute value increases.

$$
\frac {\partial K ^ {*}}{\partial d} = \frac {- \frac {(a c + d)}{a (c - b) (K ^ {*} + 1) ^ {2}}}{\frac {- (a c + d) ^ {2}}{a (c - b) (K ^ {*} + 1) ^ {3}} - \frac {\partial^ {2} C (K ^ {*})}{\partial K ^ {2}}} > 0.
$$

As d increases, the price-attribute relationship makes a parallel upward shift. Unlike the situation with a, the slope of that relationship, $\partial K ^ { * } / \partial d$ shows that there is an unambiguous increase in the optimal fineness of measurement as d increases.

It is well to remember that these comparative statics results stem from infinitesimal changes in the parameters in question. The presence ofthe constraint on $\hat { h } _ { 1 }$ means we must be cautious in generalizing these conclusions because the constraint may become binding if a. h. c, or d is changed sufficiently. As will be seen below, the situation is somewhat different (and. fortunately, simpler) in the presence of a binding constraint. In particular, the sign of $\partial K ^ { * } /$ db is reversed from the result in this subsection, d disappears from the scene entirely, and both $\partial K ^ { * } /$ da and $\partial K ^ { * } / \partial c$ become unambiguously positive!

## 7.2. The Constraint on $\hat { h } _ { I }$ Is Binding

Examination of equation (8) shows that as /C grows, the constraint $\hat { h } _ { 1 } \geq b$ will eventually become binding. In fact, it is easy to calculate from equation (8) when this occurs, namely when'^

$$
K > \frac {a (c - b)}{(a b + d)}.
$$

When the constraint is binding, i.e.. $\hat { h } _ { 1 } = b ,$ .we have:

$$
\begin{array}{l} \hat {h} _ {1} = b, \\ h _ {i} = \frac {i (c - b)}{K} + b \quad \text { for } \quad i = 1 \text {   to   } K - 1. \end{array}
$$

Substituting these into the objective equation (6) gives

$$
G (K; a, b, c, d) = \frac {a}{2} \left(\frac {b - c}{K} + (b + c)\right) + d.\tag{13}
$$

Again relaxing the integer constraint on K and differentiating with respect to K gives:

$$
\frac {\partial G}{\partial K} = \frac {a (c - b)}{2 K ^ {2}} > 0 \quad \text { for   all } \quad K > 0 \quad \text { and }
$$

$$
\frac {\partial^ {2} G}{\partial K ^ {2}} = \frac {- 2 a (c - b)}{2 K ^ {3}} <   0 \quad \text { for   all } \quad K > 0,
$$

so $G$ is concave in K.

Equation (13) can be rewritten in an interesting form. The mean, $\mu ,$ and standard deviation, $\sigma ,$ for the uniform distribution are (Bury 1975, p. 340):

$$
\mu = \frac {b + c}{2}, \quad \sigma = \frac {(c - b)}{2 \sqrt {3}}.
$$

Thus equation (13) can be rewritten in terms of $\mu$ and $\sigma ;$

$$
G (K; a, b, c, d) = G (K; a, d, \mu , \sigma) = a \left(\mu - \frac {\sigma \sqrt {3}}{K}\right) + d.\tag{14}
$$

This gives

$$
G V (K; a, \mu , \sigma) = G (K; a, d, \mu , \sigma) - G (1; a, d, \mu , \sigma) = a \sigma \sqrt {3} \left(1 - \frac {1}{K}\right).\tag{15}
$$

This says that for a given fineness of measurement $K ,$ the gross value ofthe information structure is directly proportional to a and to the slope ofthe price-attribute relationship. Both of these results have intuitive appeal. In the limit, if every instance of a product has the same attribute value, $\mathrm { i } . \mathrm { e } _ { \cdot \mathrm { , ~ } \sigma } = 0$ , then intuitively all information structures should have zero gross value because there is no uncertainty about the attribute. As the attribute becomes more variable it is intuitively plausible that an information structure should have larger gross value. Similarly, if the product market is such that an added unit ofthe attribute has low value, that is, a is small, then there is little motivation to distinguish between units ofthe product. If a is large, then there is a substantial payoff in being able to distinguish variations.

Next consider $N V ,$ equation (7), where $G V$ is given by equation (14) and as before $C ( K )$ is twice differentiable in $K ,$ increasing in $K \left( \mathrm { i . e . , ~ } \partial C / \partial K > 0 \right)$ , and weakly convex $( \mathrm { i } . \mathrm { e } . , \partial ^ { 2 } C / \partial K ^ { 2 } \geq 0 )$ . Thus we have

$$
N V (K; a, \sigma) = a \sigma \sqrt {3} \left(1 - \frac {1}{K}\right) - C (K).
$$

The first and second derivatives are

$$
\frac {\partial N V}{\partial K} = \frac {a \sigma \sqrt {3}}{K ^ {2}} - \frac {\partial C}{\partial K},
$$

$$
\frac {\partial^ {2} N V}{\partial K ^ {2}} = \frac {- 2 a \sigma \sqrt {3}}{K ^ {3}} - \frac {\partial^ {2} C}{\partial K ^ {2}}.
$$

Setting $\partial N V / \partial K = 0$ yields $K ^ { * } ( a , \sigma )$ ), and since $\partial ^ { 2 } N V / \partial K ^ { 2 } < 0$ it is a maximum. These first- and second-order conditions yield the following comparative statics results; '^

$$
\frac {\partial K ^ {*}}{\partial a} = \frac {- \sigma \sqrt {3}}{K ^ {* 2} \left(\frac {- 2 a \sigma \sqrt {3}}{K ^ {* 3}} - \frac {\partial^ {2} C}{\partial K ^ {2}}\right)} > 0,
$$

$$
\frac {\partial K ^ {*}}{\partial \sigma} = \frac {- a \sqrt {3}}{K ^ {* 2} \left(\frac {- 2 a \sigma \sqrt {3}}{K ^ {* 3}} - \frac {\partial^ {2} C}{\partial K ^ {2}}\right)} > 0,
$$

Since

$$
\frac {\partial K ^ {*}}{\partial b} = \frac {\partial K ^ {*}}{\partial \sigma} \frac {\partial \sigma}{\partial b} \quad \text { and } \quad \frac {\partial K ^ {*}}{\partial c} = \frac {\partial K ^ {*}}{\partial \sigma} \frac {\partial \sigma}{\partial c},
$$

we have

$$
\frac {\partial K ^ {*}}{\partial b} <   0 \quad \text { and } \quad \frac {\partial K ^ {*}}{\partial c} > 0.
$$

As we noted at the end ofthe previous subsection, this is the opposite sign for $\partial K ^ { * } / \partial b$ and $\partial K ^ { * } / \partial c$ is no longer ambiguous.

June 1990

That is, the optimal fineness of measurement is increasing in the variability ofthe attribute, a, and increasing in the marginal value of a unit ofthe attribute, a. The simplicity of these expressions and the definiteness of their signs is a significant contrast to the results at the end ofthe previous subsection.

## 8. Numerical Example: Normally Distributed Attribute, Price Is Linear in tbe Attribute and Measurement Cost Is Linear in K

It would be rewarding to present results similar to those in $\ S 7$ for the case of a normally distributed attribute, but the mathematics involved does not readily yield such results. Hence we will present a specific numerical example in this section. To add concreteness we will consider a seller of Christmas trees. We assume:

1. Price is linearly increasing in $h , p ( h ) = a h$ , where h is the height of a tree

2. Tree heights are normally distributed with a mean of 6 feet, and a standard deviation of 2.5 feet.

3. $C ( K ) = b ( K - 1 )$ ). (Recall $C ( K )$ is incremental to the null information structure, i.e. K ^ 1, so C{ I) must equal 0.)

The slope, a. in the linear price function has no effect on the choice of category boundaries since it divides out ofthe first-order conditions. Thus ifwe let $L ^ { * } ( K ; a )$ denote $L ^ { * }$ for a particular £/, $L ^ { * } ( K ; a ) = a L ^ { * } ( K ; 1 )$ ), soit suffices to calculat $L ^ { * } ( K ;$ 1) when $p ( h )$ is linear. Figure 2 shows a graph of $L ^ { * } ( K ; 1 )$ as a function of A^ for th distribution in question.

Given these remarks, we can determine $K ^ { * }$ from $L ^ { * } ( K ; 1 )$ if we rescale C{K) by dividing it by fl. Thus let $C \dag ( K ) \equiv C ( K ) / a$ . Figures 3 and 4 show graphs o $L ^ { * } ( K ; 1 )$ $C \dag ( K ) = ( b / a ) ( K - 1 )$ ), and the resulting $N V ( K )$ ) for two values o $b / a .$ allowing $K ^ { * }$ to be easily determined.

Assume trees sell for \$5.00 per foot, so that a 6-foot tree retails for about \$30. Figure 3 indicates that a seller facing measurement costs of $5 \times \mathbb { S } 0 . 0 5 = \mathbb { S } 0 . 2 5$ per additional category should select 11 categories, while Figure 4 indicates that measure ment costs of \$0.50 per additional category leads to 6 categories as being optimal, assuming the linear cost function.

![](/api/attachments/XHPS89BW/fulltext/images/3042ac2863f3cc82d12db9ae4d47e875cbbabefb1c86c4bfaf5d8c672e0ce252.jpg)  
FIGURE 2, A P!oto $L ^ { * } ( K ) \vee \mathbf { S } .$ A" for A'- I to 100 when p(/i) = A and/(/i) is a Normal Density with Me $= 6 . 0 \AA$ , Standard Deviation = 2.5.

![](/api/attachments/XHPS89BW/fulltext/images/079250d1d072044155e5cfae022d89609b5ee973637290121bdb130bf63b9391.jpg)  
F I G U R E 3, A Plot of $L ^ { * } ( K ) , N V _ { \kappa } ,$ and $C _ { K } ,$ where $C _ { \kappa } = 0 . 0 5 ( K - 1 )$

The figures also include the category boundaries and $\hat { h } _ { 1 }$ for the optimal designs. Intuition suggests that the finest measurement should be done in that part ofthe distribution where $p ( h ) \times f ( h )$ is relatively large. Given the nature of $p ( h )$ and the normal distribution used in this example, it is not surprising that most ofthe catego ries lie between the mean and one standard deviation above the mean, 6 to 8.5 here.

![](/api/attachments/XHPS89BW/fulltext/images/d943ac13be4e0a2493bb5e582bc41acbb0d620f58f6a7abeb13c85ce355c6633.jpg)  
FIGURE 4. A Plot or $L ^ { * } ( K )$ $N V _ { \kappa }$ and $C _ { K } ,$ where $C _ { K } = 0 . 1 0 \left( K - 1 \right)$

## 9. Comments and Concluding Remarks

In order to answer with any confidence questions of how the nature of a firm's information systems is affected by features of its environment we feel rigorous model ing of such problems is required and can produce useful insights. As the results in §7 indicated, the relationships can be complicated and subtle; far more work along this line is needed. Further, the results here suggest that such efforts can yield testable implications, giving information systems research a dimension that at present is largely lacking.

There are many ways this work can be extended. Some ofthe more interesting ones include:

• Studying the case of noisy information structures. As we mentioned earlier, this introduces the possibility of additional tradeoffs., but it requires some assumptions about the nature of measurement technology in order to make sense of how the likelihood depends on the structure, and it considerably complicates the mathematics.

• Will firms measure less finely when customers are less well informed? Intuitively, if customers are less able to discriminate, we would expect the value of measurement to the firm to be less, hence an optimal information structure to be less fine

• Will they measure less finely when the good is not a pure search good? In this situation we can consider two cases. For some kinds of goods customers can improve their assessment of quaiity by investing in information gathering before buying, while for others the quality, and therefore utility, can only be revealed by use. In the first case there is clearly a gaming issue that needs to be modeled since both buyer and seller information system decisions are relevant and are likely to be interrelated. In the second case, interesting issues such as the relationship between warranties and seller investment in information systems arise.

• lf firms do not measure exactly then $p ( h )$ will not be observable for each h, only for particular values determined by the categories they choose. How does this affect the equilibrium set of categories, or is there an equilibrium?

• As we mentioned earlier, the fineness of measurement problem is a general issue in determining data requirements. The results in this paper can be extended to broader classes of loss function describing the incomplete information costs and to cases in which there are statistical dependencies among attributes.

Acknowledgements. This research was supported by the IBM Program of Support for Fducation in the Management of Information Systems.

We wish to thank Professors Haim Mendelson and Jerold Zimmerman and three anonymous referees for helpful comments on earlier versions of this paper.\*

• Charles H. Kriebel. Associate Editor. This paper was received on September 12, 1988, and has been with the authors 3 months for 2 revisions.

## Appendix A: Noisy Information Structures

the form

$$
\mathcal {L} (i | h) = \left\{ \begin{array}{l l} 1 & \text { if } \quad h \in H _ {i}, \\ 0 & \text { otherwise }, \end{array} \right.
$$

for each That is, the information system alwaysreportscorrectly as to the interva $H _ { i }$ in which A falls, bu the measurement's precision is limited by the coarseness ofthe structure. Allowing more general forms for $\mathcal { L }$ considerably complicates the resulting optimization problem. The formulation in expression (2) re mains valid, but its simplification to expression (3) fails to hold for two reasons. First, prob $H _ { i } )$ in ( I ) no longer simplifies to $( F ( h _ { i } ) - F ( h _ { i - 1 } ) )$ but rather is a function of $\mathcal { L }$ as well. Since the interval endpoints $h _ { j }$ are decision variables, some specification ofthe way in which $\mathcal { L }$ behaves as a function ofthe $h _ { j }$ is required. In the general case prob( $\textstyle H _ { i } )$ is not going to depend simply on the endpoints of $H _ { i }$ as it does with a noiseless $\mathcal { L }$ but upon the entire set of $h _ { r } ,$ so the first-order conditions arc significantly more complex. In order to generate concrete results, specific assumptions as to the nature ofthe measurement technology are required, an issue which we are presently studying. Second, the $\hat { h } _ { i }$ will in general no longer be a function just of the endpoints of $H _ { r }$ either, because the likelihood enters into the Bayesian updating required for expression (1). This also adds to the complexity ofthe first order conditions.

## Appendix B: First-Order Conditions

The first-order conditions for equation (5) are:

$$
G _ {h _ {1}} = p ^ {\prime} (h _ {1}) [ F (h _ {2}) - F (h _ {1}) ] - p (h _ {1}) f (h _ {1})
$$

$$
+ p ^ {\prime} (\hat {h} _ {1}) \frac {d \hat {h} _ {1}}{d h _ {1}} [ F (h _ {1}) - F (\hat {h} _ {1}) ] + p (\hat {h} _ {1}) \left[ f (h _ {1}) - f (\hat {h} _ {1}) \frac {d \hat {h} _ {1}}{d h _ {1}} \right] = 0,\tag{B1}
$$

$$
G _ {h _ {i}} = p ^ {\prime} \left(h _ {i}\right) \left[ F \left(h _ {i + 1}\right) - F \left(h _ {i}\right) \right] - f \left(h _ {i}\right) \left[ p \left(h _ {i}\right) - p \left(h _ {i - 1}\right) \right] = 0 \quad \text { for } \quad i = 2 \text { to } K - 1.\tag{B2}
$$

The first-order conditions for equation (6) are

$$
G _ {h _ {1}} = p ^ {\prime} \left(h _ {1}\right) \left[ F \left(h _ {2}\right) - F \left(h _ {1}\right) \right] - f \left(h _ {1}\right) \left[ p \left(h _ {1}\right) - p \left(h _ {L}\right) \right] = 0,\tag{B3}
$$

$$
G _ {h _ {i}} = p ^ {\prime} \left(h _ {i}\right) \left[ F \left(h _ {i + 1}\right) - F \left(h _ {i}\right) \right] - f \left(h _ {i}\right) \left[ p \left(h _ {i}\right) - p \left(h _ {i - 1}\right) \right] = 0 \quad \text { for } \quad i = 2 \text { to } K - 1.\tag{B4}
$$

## Appendix C: Solving the First-Order Conditions

For $i \geq 2 ,$ , i.e. for equations (B2) and (B4). we can rewrite the conditions as:

$$
F (h _ {i + 1}) = F (h _ {i}) + \frac {f (h _ {i}) [ p (h _ {i}) - p (h _ {i - 1}) ]}{p ^ {\prime} (h _ {i})}.\tag{C1}
$$

Assuming the cumulative distribution function $F$ is strictly increasing, there is a unique explicit solution for $h _ { i + 1 }$ in terms of $h _ { i }$ and $h _ { i - 1 }$ :

$$
h _ {i + 1} = F ^ {- 1} \left(F (h _ {i}) + \frac {f (h _ {i}) [ p (h _ {i}) - p (h _ {i - 1}) ]}{p ^ {\prime} (h _ {i})}\right) \quad \text { for } \quad i = 2 \text {   to   } K - 2.\tag{C2}
$$

Note $i = K - 1$ is a special case since by definition $h _ { K } = h _ { U } ,$ so $F ( h _ { K } ) = 1$ , yielding the condition:

$$
1 = F (h _ {K - 1}) + \frac {f (h _ {K - 1}) [ p (h _ {K - 1}) - p (h _ {K - 2}) ]}{p ^ {\prime} (h _ {K - 1})}.\tag{C3}
$$

Calculation of $h _ { 2 }$ in the case of equations (Bl) and ( B2) is similar but slightly more complicated since i stems from $G _ { h _ { 1 } } \mathrm { : }$

$$
h _ {2} = F ^ {- 1} \left(F (h _ {1}) + \frac {p (h _ {1}) f (h _ {1}) - p ^ {\prime} (\hat {h} _ {1}) \frac {d \hat {h} _ {1}}{d h _ {1}} [ F (h _ {1}) - F (\hat {h} _ {1}) ] - p (\hat {h} _ {1}) \left[ f (h _ {1}) - f (\hat {h} _ {1}) \frac {d \hat {h} _ {1}}{d h _ {1}} \right]}{p ^ {\prime} (h _ {1})}\right)\tag{C4}
$$

Thus $h _ { 2 }$ is a function of $h _ { 1 } , { \hat { h } } _ { 1 }$ , and $d \hat { h } _ { 1 } / d h _ { 1 }$ However, we can solve for $\hat { h } _ { r }$ in terms of $h _ { 1 }$ because $\bar { h } _ { 1 }$ is a solution of equation (1) for $H _ { 1 }$ . The first-order conditions of that problem lead to the following implicit specification of $\hat { h } _ { 1 }$ , in terms o $h _ { 1 } .$

$$
\frac {p (\hat {h} _ {1}) f (\hat {h} _ {1})}{p ^ {\prime} (\hat {h} _ {1})} + F (\hat {h} _ {1}) = F (h _ {1}).\tag{C5}
$$

Further, $d \hat { h } _ { 1 } / d h _ { 1 }$ can be determined from equation (C5) via the implicit function theorem and chain rule:

$$
\frac {d \hat {h} _ {1}}{d h _ {1}} = - \frac {p ^ {\prime} (\hat {h} _ {1}) f (h _ {1})}{p ^ {\prime \prime} (\hat {h} _ {1}) [ F (h _ {1}) - F (\hat {h} _ {1}) ] - 2 p ^ {\prime} (\hat {h} _ {1}) f (\hat {h} _ {1}) - p (\hat {h} _ {1}) f ^ {\prime} (\hat {h} _ {1})}.\tag{C6}
$$

As a result, $\hat { h } _ { 1 }$ is a function of $h _ { 1 } ,$ making $h _ { 2 }$ a function of $h _ { 1 }$ only. Equations (C2) imply that each of $h _ { 3 }$ through $h _ { K - 1 }$ is also a function of $h _ { 1 }$ only.

Finding $h _ { 2 }$ in the case of equation (B3) is essentially identical to equation (C2)

$$
h _ {2} = F ^ {- 1} \left(F (h _ {1}) + \frac {f (h _ {1}) [ p (h _ {1}) - p (h _ {L}) ]}{p ^ {\prime} (h _ {1})}\right).\tag{C7}
$$

## References

Bury, Karl, Statistical Models in Applied Science, John Wiley and Sons, New York, 1975.

McGuire, C. B., "Comparisons of Information Structures." in C, B. McGuire and R. Radner. Decision and Organization, North-Holland, Amsterdam, 1972

Mendelson, H. and A. Saharia,"Incomplete Information Costs and Database Design,"ACM Trans. Database Systems. l l , 2 ( J u n e , 1986). 159-185.

Wilde, Louis. "On the Formal Theory of Inspection and Evaluation in Product Markets," Econometrica,

Copyright 1990, by INFORMS, all rights reserved. Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
