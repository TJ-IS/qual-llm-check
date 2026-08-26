---
otero_id: 2116
otero_key: "SAHZ4EZ9"
title: "Convex cone-based partial order for multiple criteria alternatives"
authors: "Akram Dehnokhalaji; Pekka J. Korhonen; Murat Köksalan; Nasim Nasrabadi; Jyrki Wallenius"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.019"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Convex cone-based partial order for multiple criteria alternatives<sup>☆,☆☆</sup>

Akram Dehnokhalaji <sup>a,b</sup>, Pekka J. Korhonen <sup>a,</sup>⁎, Murat Köksalan <sup>a,c</sup>, Nasim Nasrabadi <sup>a,b</sup>, Jyrki Wallenius <sup>a</sup>

<sup>a</sup> Aalto University, School of Economics, Department of Business Technology, P.O. Box 21220, 00079 Aalto, Helsinki, Finland

<sup>b</sup> Tarbiat Moallem University, Department of Mathematics, Tehran, Iran

<sup>c</sup> Middle East Technical University, Department of Industrial Engineering, Ankara, Turkey

## a r t i c l e i n f o

Available online 25 November 2010

Keywords: Strict partial order Discrete alternative Convex cone Evaluation Multiple criteria

## a b s t r a c t

In this paper, we consider the problem of <sup>fi</sup>nding a preference-based strict partial order for a <sup>fi</sup>nite set of multiple criteria alternatives. We develop an approach based on information provided by the decision maker in the form of pairwise comparisons. We assume that the decision maker's value function is not explicitly known, but it has a quasi-concave form. Based on this assumption, we construct convex cones providing additional preference information to partially order the set of alternatives. We also extend the information obtained from the quasi-concavity of the value function to derive heuristic information that enriches the strict partial order. This approach can as such be used to partially rank multiple criteria alternatives and as a supplementary method to incorporate preference information in, e.g. Data Envelopment Analysis and Evolutionary Multi-Objective Optimization.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

The purpose in Multiple Criteria Decision Making (MCDM) is to <sup>fi</sup>nd the most preferred solution among a set of implicitly or explicitly de<sup>fi</sup>ned alternatives characterized by several criteria, or to rank such alternatives. The problems where alternatives are implicitly de<sup>fi</sup>ned using constraints are called multiple criteria design problems and the problems where alternatives are explicitly given are called multiple criteria evaluation problems. In this paper, we consider multiple criteria evaluation problems where a Decision Maker (DM) evaluates the explicitly given alternatives.

Which kind of approach is most suitable to solving evaluation problems is heavily dependent on the characteristics of the problem. The outranking approach [21], the multi-attribute value function approach [6], the analytic hierarchy process [22], the regime method [4], the hierarchical interactive approach [7], the visual reference direction approach [8], the aspiration-level interactive method (AIM) [18,19], and the hybrid method [17] are typical examples of approaches developed to solve evaluation problems.

A class of methods is based on implicitly known value functions. No attempt is made to construct the value function, but assumptions of its functional form are used to structure the search process. Typical assumptions are linearity, Chebyshev-type min–max function, quasiconcavity, pseudo-concavity, etc. of the value function. Examples of such methods are presented in Refs. [10–13,15,26]. There are also approaches to <sup>fi</sup>nd which form of value function the DM's preferences are consistent with [14,24].

Various interaction styles have been proposed for interactive approaches in general. Examples include requiring pairwise comparison of alternatives [27], local tradeoff ratios [2], interval local tradeoff ratios [23], comparative tradeoff ratios [5], reference points [25], and reference directions [9]. A good interactive approach does not waste the DM's time, and its communication language is easy. Furthermore, it is a good idea to increase the intelligence of the system, but it is important to remember that the DM wants to keep the control of the system in his/her own hands. There are several ways to implement a dialogue between an interactive approach and the DM. In this paper we require pairwise comparison information as we think it is easy and relevant for a DM to compare pairs of alternatives.

Our aim in this paper is to produce a preference-based strict partial order for a <sup>fi</sup>nite set of multiple criteria alternatives. We try to create the strict partial order by making maximum use of the available preference information in the form of pairwise comparisons. We assume that the DM's value function is unknown to us, but it has a quasi-concave form. Based on the available preference information and exploiting the implications of a quasi-concave value function, we construct convex cones [10] and polyhedrons to provide additional preference relations that enrich the strict partial order of alternatives. We also introduce heuristics to extract further approximate preference relations that can be used in the partial order

This paper unfolds as follows. Section 2 provides preliminary considerations. Section 3 develops the main idea and formulations.

Section 4 includes an illustrative example and <sup>fi</sup>nally Section 5 concludes the paper.

## 2. Preliminary considerations

Consider a discrete, <sup>fi</sup>nite, deterministic multiple criteria evaluation problem where a single DM compares a set of n alternatives with respect to p criteria. The set S of alternatives includes vectors $X _ { i } \in \Re ^ { p }$ $i { \in } N { = } \{ 1 , ~ . . . , ~ n \}$ , with elements $x _ { i j } > 0$ for all j. Without loss of generality, assume that for each criterion more is better. We de<sup>fi</sup>ne the dominance in $\Re ^ { p }$ in the usual way.

De<sup>fi</sup>nition 1. A vector $X ^ { \ast } \in \Re ^ { p }$ is non-dominated iff (if and only if) there does not exist another $X { \in } { \mathfrak { R } } ^ { p }$ such that $X { \geq } X ^ { * }$ and $X \neq X ^ { * }$

De<sup>fi</sup>nition 2. The function $f \colon \Omega \to \Re , \Omega \subseteq \Re ^ { p }$ , is called a value function if it has the following properties:

1. $f ( X ^ { * } ) { \mathrm { { > } } } f ( X ) , { \mathrm { { i f } } } X ^ { * }$ dominates X.

2. $f ( X ^ { ^ { * } } ) { > } f ( X ) , \operatorname { i f f } X ^ { ^ { * } }$ is preferred to X.

3. $f ( X ^ { * } ) { \geq } f ( X ) , \operatorname { i f } X ^ { * }$ is at least as preferred as $X .$

Property 1 implies that function f is also strictly increasing in set $\Omega ,$ where Ω consists of all points at which the value function evaluation is needed. Hence forward, we assume that the DM's value function is quasi-concave and that we only know of its form.

In the following we use the symbol $" \succ "$ to indicate the relationship ${ } ^ { \mathfrak { a } } \mathrm { i } s$ preferred $\left. { t o } _ { \ast } ^ { \ast } \right.$ When needed, we also use the symbol $" \succeq "$ to indicate “is at least as good as.” It can be seen that both relations are transitive. The DM's preferences are expressed by the set $P { = } \{ ( X _ { r } , X _ { s } ) |$ $X _ { r } { \succ } X _ { s } , r , s { \in } N \}$ . Thus P de<sup>fi</sup>nes a strict partial order in S (an asymmetric transitive binary relation over S).

The ef<sup>fi</sup>ciency of interactive procedures is heavily dependent on what kind of and how much information the DM is required to provide. The assumptions that are made about the value function facilitate the convergence of an interactive procedure. However, such assumptions should be as realistic as possible. For example, a linear value function assumption produces a fast convergence, but none of the convex dominated alternatives can be most preferred [28]. The quasi-concavity assumption of the value function is quite general, yet powerful in constructing a strict partial order for alternatives. Moreover, convex dominated alternatives can be most preferred. When assuming that the value function is quasi-concave, based on pairwise preference information, we may construct so called convex cones, characterizing the vertex of the cones by inferior alternatives.

To be more precise, assume that we have m (distinct) points $X _ { 1 } , . . . ,$ $X _ { k - 1 } , X _ { k } , . . . , X _ { m }$ such that $X _ { i } \succ X _ { k }$ for $i { = } 1 , { \ldots } , m$ and $i \neq k .$ Then by De<sup>fi</sup>nition $2 , f ( X _ { k } ) { < } f ( X _ { i } ) , \ i { = } 1 , \ . . . , \ m _ { \mathrm { { \scriptsize ~ 1 } } }$ , and $i \neq k .$ The subset of S including m different points $X _ { 1 } , . . . , X _ { k - 1 } , X _ { k } , . . . , X _ { m }$ such that $X _ { i } \succ X _ { k }$ for $i = 1 , . . . ,$ m and $i \neq k$ is called a preference subset and is denoted by $\{ X _ { 1 } , . . . , X _ { m } ; X _ { k } \}$

Based on this preference subset, we may construct a cone where alternative $X _ { k }$ is the vertex of the cone. We de<sup>fi</sup>ne the cone $\mathrm { C } ( X _ { 1 } , . . . ,$ $X _ { m } ; X _ { k } ~ )$ with vertex $X _ { k }$ as follows:

$$
C (X _ {1}, \dots , X _ {m}; X _ {k}) = \{X | X = X _ {k} + \sum_ {i \neq k} \mu_ {i} (X _ {k} - X _ {i}), \mu_ {i} \geq 0, i = 1, \dots , m, i \neq k \}.
$$

Based on the quasi-concavity assumption of our value function f, for any $Z { \in } C ( X _ { 1 } , . . . , X _ { m } ; X _ { k } )$ , we have shown ([10]) that $f ( X _ { i } ) { > } f ( X _ { k } ) \geq$ f(Z) for $i = 1 , . . . ,$ m and i ≠k which means that $X _ { k } \succeq Z .$ Each point $\begin{array} { r } { Z { \in } C ( X _ { 1 } , . . . , X _ { m } ; X _ { k } ) , Z { \neq } X _ { k } , } \end{array}$ or any point V dominated by Z, is called cone dominated.

Moreover, we may de<sup>fi</sup>ne a polyhedron spanned by the points $X _ { 1 } , . . . , X _ { m }$ as follows:

$$
H (X _ {1}, \dots , X _ {m}) = \{X | X = \sum_ {i = 1} ^ {m} \mu_ {i} X _ {i}, \sum_ {i = 1} ^ {m} \mu_ {i} = 1, \mu_ {i} \geq 0, i = 1, \dots , m \}.
$$

If $Y { \in } H \ ( X _ { 1 } , . . . , X _ { m } )$ , then from the de<sup>fi</sup>nition of quasi-concavity it follows that $f ( Y ) { = } f { \biggl ( } \sum _ { i = 1 } ^ { m } \mu _ { i } X _ { i } { \biggr ) } \geq \operatorname* { m i n } _ { i } f ( X _ { i } ) { = } f ( X _ { k } )$ which means that $Y \succeq X _ { k }$

In fact for each preference subset $\{ X _ { 1 } , . . . , X _ { m } ; X _ { k } \}$ we may de<sup>fi</sup>ne a convex cone and a polyhedron. Based on the structure of these two sets and the assumptions made about the value function, it is possible to extract more preference information about other points not belonging to the corresponding preference set with respect to $X _ { k }$ by checking whether or not the point belongs to the convex cone $C ( X _ { 1 } , . . . , X _ { m } ; X _ { k } )$ or falls under it, or belongs to the polyhedron $H ( X _ { 1 } , . . . , X _ { m } )$ or lies above it.

Without loss of generality, let the DM's preference set P be expressed as the union of several preference subsets—each one characterized by its worst point as the vertex. Different preference subsets yield different convex cones and polyhedrons which enable us to extract more information to update the preference set P by adding new preference comparisons.

In Fig. 1, we illustrate how the quasi-concavity assumption brings additional information to the preference-based ranking of alternatives.

Consider alternative $X _ { 2 } .$ In case we have no preference information, we can use only dominance. For any $Y _ { 1 }$ in the region dominating X<sub>2</sub>(region $\mathsf { E } _ { 3 }$ in Fig. 1) we have $Y _ { 1 } \ge X _ { 2 } , \ Y _ { 1 } \ne X _ { 2 }$ which implies that $Y _ { 1 } { \succ } X _ { 2 }$ . Similarly, for any $Y _ { 2 }$ in the region dominated by X (region $\mathsf { A } _ { 1 }$ in $\mathrm { F i g } . \ 1 )$ we have $X _ { 2 } \geq Y _ { 2 } ,$ X ≠Y which implies that $X _ { 2 } \succ Y _ { 2 } .$ . Finally, if $( X _ { 1 } , X _ { 2 } ) \in { \cal P }$ then for any $Y _ { 3 }$ in the region dominating X (region $\mathsf { E } _ { 2 }$ in Fig. 1), we have $Y _ { 3 } { \succ } X _ { 1 } { \succ } X _ { 2 }$

When we use the quasi-concavity assumption, we can exploit the available preference information further, as we will show in detail in the next section. Speci<sup>fi</sup>cally, we may use a convex cone to conclude that for any $Y _ { 4 }$ in region $\mathsf { A } _ { 2 }$ in Fig. 1 we have $X _ { 2 } \succeq Y _ { 4 }$ and we may use a polyhedron to conclude that for any $Y _ { 5 }$ in region $\mathrm { E } _ { 1 }$ in Fig. 1 we have $Y _ { 5 } \succeq X _ { 2 }$

## 3. The method

The goal is to implement the above concepts from [12] to de<sup>fi</sup>ne a strict partial order for set S. Moreover, Prasad et al. [20] proposed an approach extending the idea of convex cones heuristically. They developed the concept of p-cone ef<sup>fi</sup>ciency, providing a measure to <sup>fi</sup>nd out how close an alternative is from being dominated by the cone under consideration. The smaller the measure, the closer the alternative is to being dominated.

![](/api/attachments/SAHZ4EZ9/fulltext/images/370bcc95432f6236cfd8bebc6f7bc8ea29daa295e64b60a182fba19a0f55f2e0.jpg)  
Fig. 1. Illustration of additional information provided by quasi-concavity.

We generalize the Prasad et al.'s model [22] for de<sup>fi</sup>ning a strict partial order. Considering an arbitrary preference subset, our model will classify the alternatives $X \in S ,$ with respect to the cone and the polyhedron under consideration. By applying the model for each alternative $X \in S ,$ it would be classi<sup>fi</sup>ed as surely better than the vertex, surely worse than the vertex, or possibly better/possibly worse than the vertex of the cone. In the latter case, it provides a measure indicating how close the alternative is from being dominated by the cone and how much the alternative dominates some parts of the polyhedron. We then de<sup>fi</sup>ne two threshold values for that measure in order to classify the alternatives that are possibly better or worse than the vertex. We heuristically classify those alternatives whose measures are beyond one of the thresholds.

## 3.1. Illustration

Consider a case with two criteria and two alternatives $X _ { 1 }$ and $X _ { 2 }$ such that $X _ { 1 } \succ X _ { 2 }$ . Such a case is illustrated in Fig. 2.

Recalling that the value function f is quasi-concave and strictly increasing in set $\Omega \subseteq { \mathfrak { R } } ^ { p } ,$ , the indifference curve of f passing through X $\mathrm { i } s \ ^ { \mathrm { * } } \mathrm { b e l o w } ^ { \mathrm { * } }$ that passing through $X _ { 1 }$ (as shown in Fig. 2). Because the exact value function is unknown, we are not able to precisely characterize the indifference curve. We are interested in <sup>fi</sup>nding out the region containing the alternatives that are at least as good as $X _ { 2 } .$ Consider the polyhedron $H ( X _ { 1 } , X _ { 2 } )$ which corresponds to the convex combinations of $X _ { 1 }$ and $X _ { 2 }$ in this case. Regarding the assumptions on the value function, the indifference curve passing through an alternative which belongs to the polyhedron is “not below” the one passing through $X _ { 2 } .$ . Hence, all alternatives in region E (the light shaded region in Fig. 2) are at least as good as $X _ { 2 } ,$ because they belong to $H ( X _ { 1 } , X _ { 2 } )$ or dominate some parts of it.

On the other hand, consider the convex cone $\mathsf C ( X _ { 1 } , X _ { 2 } ; X _ { 2 } )$ which is represented by the broken line starting at $X _ { 2 } .$ . An alternative located on this line is not better than $X _ { 2 }$ and is worse than X . This fact along with the domination concept leads us to conclude that alternatives belonging to region A (the dark shaded region in Fig. 2) are worse than $X _ { 1 }$ and not better than $X _ { 2 } .$

For alternatives located in regions B and D, there does not exist enough information to indicate whether they are preferred to $X _ { 2 }$ or not. For instance, Y could be better than or worse than $X _ { 2 }$ depending on the indifference curve of the precise value function. The same is true about point Z. In fact we can measure the distance of such points from the regions whose relative preferences to $X _ { 1 }$ and $X _ { 2 }$ are known (that is, regions E and $\pmb { \Lambda } )$ . For a given point $Y ,$ its status can be determined by comparing it to $X _ { 2 } .$ For example, in Fig. 2, considering a radial measure, Y is “close” to region A. Hence Y is possibly worse than $X _ { 2 } .$ Similarly, Z is possibly better than $X _ { 2 } ,$ because it is $" c l o s e "$ to region E. In the following, we generalize the idea of Prasad et al. [22] to determine how close Y is to the convex cone. Then, we develop another model that measures the distance of Y from the polyhedron. Finally we introduce a scaled measure to check out whether the point is possibly better/possibly worse than the vertex of a cone and by how much.

![](/api/attachments/SAHZ4EZ9/fulltext/images/c7a4a2844c2ed6223247d0cd8bf7d73df2caeb2c07c85cdbff0fee189400b95c.jpg)  
Fig. 2. Illustration of the polyhedron and the cone.

## 3.2. Model formulation

Assume that the preference subset $\{ X _ { 1 } , . . . , X _ { m } ; X _ { k } \}$ is constructed based on the DM's preferences. Considering an arbitrary alternative $X _ { o } { \in } S | \{ X _ { 1 } , . . . , X _ { m } \}$ , the purpose is to determine the status of $X _ { o }$ with respect to $X _ { k } .$ . This can be accomplished by introducing a measure $\theta _ { o } ( X _ { k } )$ with the property $0 \le \theta _ { o } ( X _ { k } ) \le 1$ , where $\theta _ { o } ( X _ { k } ) = 1$ identi<sup>fi</sup>es $X _ { o }$ as at least as good as $X _ { k } ,$ and $\theta _ { o } ( X _ { k } ) = 0$ identi<sup>fi</sup>es $X _ { o }$ as at most as good as $X _ { k } .$ . For the alternatives that are possibly better or possibly worse than $X _ { k } ,$ we de<sup>fi</sup>ne $0 { < } \theta _ { o } ( X _ { k } ) { < } 1$ . The smaller (larger) the value of $\theta _ { o } ( X _ { k } )$ , the closer $X _ { o }$ is to the at most (at least) as good region. Recall that we assume $X _ { i } { > } 0$ for all $X _ { i } \in S$

In the following, we present a two-stage procedure which provides the basics for the measure $\theta _ { o } ( X _ { k } )$ for an arbitrary $\textstyle X _ { o } \in S .$ The procedure includes solving two Linear Programming (LP) problems that measure the distance of the alternative from the at most and at least as good as regions, respectively.

Stage 1. We check whether X<sub>o</sub> is located in the cone dominated region (region A in Fig. 2) or not, by solving the following LP model:

$$
\begin{array}{l} \text {Max} \rho \\ \text {s.t.} X _ {k} + \sum_ {i \neq k} \mu_ {i} (X _ {k} - X _ {i}) \geq (1 + \rho) X _ {o} \\ \mu_ {i} \geq 0 \quad i = 1, \ldots , m, i \neq k \end{array}\tag{1}
$$

Let $\rho _ { o }$ be the optimal value of model $( 1 ) . \mathrm { I f } \rho _ { o } { \geq } 0 ,$ , then $X _ { o }$ is in or dominated by the cone and therefore $X _ { k } \succeq X _ { o }$ . Hence, we set $\theta _ { o } ( X _ { k } ) = 0$ and stop the procedure since the status of $X _ { o }$ is known for sure. On the other hand, $\rho _ { o } { < } 0$ means that $X _ { o }$ should radially be decreased to reach $C ( X _ { 1 } , . . . , X _ { m } ; X _ { k } )$ . In this case $X _ { o }$ is not surely worse than $X _ { k } ,$ i.e. it may be surely better or possibly better/possibly worse than $X _ { k } .$ Its status might be identi<sup>fi</sup>ed in Stage 2.

Stage 2. We check whether $X _ { o }$ is in region E or it is located in possibly better/possibly worse regions B or D than $X _ { k }$ in Fig. 2 by solving the following LP model:

$$
\begin{array}{l} \text {Min} \varphi \\ \text {s.t.} \sum_ {i = 1} ^ {m} \mu_ {i} X _ {i} \leq (1 + \varphi) X _ {o} \\ \sum_ {i = 1} ^ {m} \mu_ {i} = 1 \\ \mu_ {i} \geq 0 \qquad i = 1, \dots , m \end{array}\tag{2}
$$

Assume that $\varphi _ { o }$ is the optimal value of model (2). If $\varphi _ { o } { \leq } 0 , X _ { o }$ is either in the polyhedron or dominates at least one alternative in the polyhedron and is at least as good as $X _ { k } .$ Hence, we set $\theta _ { o } ( X _ { k } ) = 1$ and stop the procedure since the status of $X _ { o }$ is known for sure. Otherwise, $\varphi _ { o } > 0$ means that $X _ { o }$ should be radially expanded to reach a point V dominating at least one point of the polyhedron $H ( X _ { 1 } , . . . , X _ { k } )$ . This case corresponds to possibly better/possibly worse alternatives for which we de<sup>fi</sup>ne $0 { < } \theta _ { o } ( X _ { k } ) { < } 1$ next.

## 3.3. Defining the measure $\theta _ { o } ( X _ { k } )$

We assume that different criteria are measured on approximately similar scales. Otherwise, we scale each criterion, say in the interval (0,1), in order to transform them into the same scale.

For possibly better/worse points we have $\rho _ { o } { < } 0$ and $\varphi _ { o } > 0$ . Note that $( 1 + \rho _ { o } ) X _ { o } { \leq } X _ { o } { \leq } ( 1 + \phi _ { o } ) X _ { o }$ , because $X _ { o } > 0 .$ . Furthermore, the inequalities are strict for positive components of $X _ { o }$ and at least one component is positive. In this case we transform the interval $( 1 +$ $\rho _ { o } , 1 + \varphi _ { o } )$ onto (0, 1). The value 1, which associates with $X _ { o }$ in $( 1 +$ $\rho _ { o } , 1 + \varphi _ { o } )$ corresponds to value $\frac { - \rho _ { o } } { \varphi _ { o } - \rho _ { o } }$ in the interval (0, 1). We de<sup>fi</sup>ne

$$
\theta_ {o} (X _ {k}) = \frac {1 - (1 + \rho_ {o})}{(1 + \varphi_ {o}) - (1 + \rho_ {o})} = \frac {- \rho_ {o}}{\varphi_ {o} - \rho_ {o}}
$$

as a measure of the preference relation between $X _ { o }$ and $X _ { k } .$ That is, $0 { < } \theta _ { o } ( X _ { k } ) { < } 1$ indicates the possibly better or possibly worse status of point $X _ { o }$ . Note that when the interval $( 1 + \rho _ { o } , 1 + \varphi _ { o } )$ is wide, $\theta _ { o } ( X _ { k } )$ may not be very informative. The closer $\theta _ { o } ( X _ { k } )$ is to 0, the more likely is $X _ { o }$ to be at most as preferred as $X _ { k } .$ . The closer $\theta _ { o } ( X _ { k } )$ is to 1, the more likely is $X _ { o }$ to be at least as preferred as $X _ { k }$

Let $t _ { 1 } { < } 0 . 5$ and $t _ { 2 } \geq 0 . 5$ denote the lower and upper thresholds to categorize an alternative relative to $X _ { k } ,$ respectively. We may conclude that $X _ { k }$ is approximately better than $X _ { o }$ when $\theta _ { o } ( X _ { k } ) \le t _ { 1 }$ and $X _ { o }$ is approximately better than $X _ { k }$ when $\theta _ { o } ( X _ { k } ) \geq t _ { 2 } .$ . We may conclude that the measure is inconclusive when $t _ { 1 } { < } \theta _ { o } ( X _ { k } ) { < } t _ { 2 }$

## 3.4. Algorithm for multiple cones

We now develop an algorithm to form a strict partial order among the available set of alternatives, S, combining the information from multiple cones. Assume that $C _ { 1 } , . . . , C _ { l }$ are the convex cones extracted from preference set $P { = } \{ ( X _ { r } , X _ { s } ) \mid X _ { r } { \succ } X _ { s } , r , s { \in } N \}$ , where $C _ { j } = C ( X _ { j _ { 1 } } , \ldots ,$ $X _ { j _ { m } } ; X _ { j _ { k } } )$ and $X _ { j _ { k } }$ is the vertex of cone $C _ { j } .$

To visualize the preferences among alternatives, we form a graph. Let alternative $X _ { i }$ correspond to node i for each $\textstyle X _ { i } \in S ,$ and preference relation $X _ { r } { \succ } X _ { s }$ correspond to an arc $( r , s )$ directed from node r to node s for each $( X _ { r } , X _ { s } ) \in P$ . We denote the resulting directed graph by $G ( S , P )$

We next present the steps of our algorithm:

Step 1. Set j=1.

Step 2. Consider cone $C _ { j } .$ For each node $X _ { i } \in S$ that is not in cone $C _ { j }$ and there does not exist any path from $X _ { i }$ to $X _ { j _ { k } }$ or from $X _ { j _ { k } }$ to $X _ { i }$ in $G ,$ perform the two-stage procedure to calculate $\theta _ { i } ( X _ { j _ { k } } )$

Step 3. If $\theta _ { i } ( X _ { j _ { k } } ) = 0 ,$ then add arc $( j _ { k } , i )$ to graph G and pair $( X _ { j _ { k } } , X _ { i } )$ to preference set P.

If $\theta _ { i } ( X _ { j _ { k } } ) = 1$ , then add arc $( i , j _ { k } )$ to G and pair $( X _ { i } , X _ { j _ { k } } )$ to P.

If $\theta _ { i } ( X _ { j _ { k } } ) \leq t _ { 1 }$ then add dotted arc $( j _ { k } , i )$ to G and pair $( X _ { j _ { k } } , X _ { i } )$ to P. $\mathrm { I f } \ \theta _ { i } ( X _ { j _ { k } } ) \geq t _ { 2 }$ then add dotted arc $( i , j _ { k } )$ to G and pair $( X _ { i } , X _ { j _ { k } } )$ to P.

Step 4. Set $j = j + 1 . \operatorname { I f } j \leq l$ then go to Step 2, otherwise stop.

Numerical example (all criteria are given on the same scale 0–100).

<table><tr><td>Alternatives</td><td> $x_1$ </td><td> $x_2$ </td><td> $x_3$ </td><td>Value</td><td>Preference-based order</td></tr><tr><td> $X_1$ </td><td>88</td><td>50</td><td>8</td><td>-2718.3</td><td>5</td></tr><tr><td> $X_2$ </td><td>68</td><td>80</td><td>32</td><td>-2652.0</td><td>3</td></tr><tr><td> $X_3$ </td><td>56</td><td>32</td><td>92</td><td>-2652.6</td><td>4</td></tr><tr><td> $X_4$ </td><td>44</td><td>86</td><td>86</td><td>-2584.7</td><td>1</td></tr><tr><td> $X_5$ </td><td>35</td><td>5</td><td>95</td><td>-2740.2</td><td>7</td></tr><tr><td> $X_6$ </td><td>50</td><td>50</td><td>35</td><td>-2736.2</td><td>6</td></tr><tr><td> $X_7$ </td><td>40</td><td>100</td><td>60</td><td>-2615.2</td><td>2</td></tr></table>

![](/api/attachments/SAHZ4EZ9/fulltext/images/17378c0165eaeb04a08063227eb2e325dc70ab3e6bc556a5dfefc33d6d005382.jpg)  
Fig. 3. The initial preference graph

It can be shown that the strict partial order de<sup>fi</sup>ned by models (1) and (2) is consistent. That ${ \mathrm { i } } s ,$ if $X _ { o }$ is cone dominated then $X _ { o }$ cannot dominate any point in the polyhedron. Towards this end we prove the following theorem.

Theorem 1. $I f \rho _ { o }$ is the solution of model (1) and $\varphi _ { o }$ the solution of model (2), then either $\rho _ { o } \geq 0 \Rightarrow \varphi _ { o } \geq 0 \ o r \ \varphi _ { o } \leq 0 \Rightarrow \rho _ { o } \leq 0 .$

Proof. Assume that $\rho _ { o } 2 0$ and $\varphi _ { o } < 0$ , then

$$
X _ {k} + \sum_ {i \neq k} \mu_ {i} ^ {*} (X _ {k} - X _ {i}) \geq (1 + \rho_ {o}) X _ {o} \geq X _ {o} \geq (1 + \varphi_ {0}) X _ {o} \geq \sum_ {i = 1} ^ {m} \lambda_ {i} ^ {*} X _ {i}
$$

where $\sum _ { i = 1 } ^ { m } \lambda _ { i } ^ { * } = 1$ and $\lambda _ { i } ^ { * } \ge 0$ for $i { = } 1 , { \ldots } , m$ and $\mu _ { i } ^ { * } { \geq } 0 , i { = } 1 , { \ldots } , m , i \neq k .$ Because f is strictly increasing and because $X _ { o } \neq 0$ and $\varphi _ { o } < 0 ,$ , it follows that

$$
f \left(X _ {k} + \sum_ {i \neq k} \mu_ {i} ^ {*} \left(X _ {k} - X _ {i}\right)\right) > f \left(\sum_ {i = 1} ^ {m} \lambda_ {i} ^ {*} X _ {i}\right).
$$

However, this contradicts the assumption that f is quasi-concave since quasi-concavity implies

$$
f \left(\sum_ {i = 1} ^ {m} \lambda_ {i} ^ {*} X _ {i}\right) \geq f \left(X _ {k} + \sum_ {i \neq k} \mu_ {i} ^ {*} (X _ {k} - X _ {i})\right).
$$

The proof that if the solution of model (2) yields $\varphi _ { o } \leq 0$ then the solution of model (1) must yield $\rho _ { o } \leq 0 ,$ , is similar. □

In the next section, we illustrate the algorithm by a simple numerical example.

## 4. Numerical example

Consider a discrete evaluation problem in which seven alternatives $X _ { 1 } , X _ { 2 } , . . . , X _ { 7 }$ are non-negative vectors in ℜ<sup>3</sup>. Assume that $P =$ $\{ ( X _ { 2 } , X _ { 3 } ) , ( X _ { 7 } , X _ { 3 } ) , ( X _ { 6 } , X _ { 5 } ) , ( X _ { 7 } , X _ { 1 } ) \}$ represents the DM's preferences and the individual's true (implicit) value function to be maximized is of the form:

$$
f (X) = f \left(\mathrm{x} _ {1}, \mathrm{x} _ {2}, \mathrm{x} _ {3}\right) = - \frac {\left(\mathrm{x} _ {1} - 1 0 0 0\right) ^ {2} + \left(\mathrm{x} _ {2} - 1 0 0 0\right) ^ {2} + \left(\mathrm{x} _ {3} - 1 0 0 0\right) ^ {2}}{1 0 0 0}.
$$

The data are provided in Table 1.

Regarding DM's preferences P, three convex cones $C _ { 1 } = C ( X _ { 2 } , X _ { 3 } ,$ $X _ { 7 } ; ~ X _ { 3 } ) , ~ C _ { 2 } = C ( X _ { 5 } , ~ X _ { 6 } ; ~ X _ { 5 } )$ and $C _ { 3 } = C ( X _ { 1 } , X _ { 7 } ; X _ { 1 } )$ are extracted. We apply the multiple cone algorithm to obtain a strict partial order. The initial preference graph is shown in Fig. 3.

Considering the <sup>fi</sup>rst convex cone $C _ { 1 } { = } C ( X _ { 2 } , X _ { 3 } , X _ { 7 } ; X _ { 3 } )$ , we apply the above mentioned two-stage procedure for alternatives $X _ { 1 } , X _ { 4 } , X _ { 5 }$ and $X _ { 6 }$ to obtain new preferences. For alternative $X _ { 1 } ,$ the following formulation is derived from model (1) in step 1:

Table 2  
Results for cone C =C(X , X , X ; X ).

<table><tr><td>Alternatives</td><td> $\rho$ </td><td> $\varphi$ </td><td> $\theta$ </td><td>Preferences</td></tr><tr><td> $X_{1}$ </td><td>-0.3600</td><td>3.000</td><td>0.1071</td><td> $X_{1}$  possibly worse than  $X_{3}$ </td></tr><tr><td> $X_{4}$ </td><td>-0.6279</td><td>-0.0110</td><td>1</td><td> $X_{4}$  surely better than  $X_{3}$ </td></tr><tr><td> $X_{5}$ </td><td>0.3037</td><td></td><td>0</td><td> $X_{5}$  surely worse than  $X_{3}$ </td></tr><tr><td> $X_{6}$ </td><td>-0.3600</td><td>0.3538</td><td>0.4424</td><td> $X_{6}$  possibly worse than  $X_{3}$ </td></tr></table>

$$
s. t. 5 \dot {6} + \mu_ {1} (5 6 - 6 8) + \mu_ {2} (5 6 - 4 0) \geq (1 + \rho) 8 8
$$

$$
3 2 + \mu_ {1} (3 2 - 8 0) + \mu_ {2} (3 2 - 1 0 0) \geq (1 + \rho) 5 0
$$

$$
9 2 + \mu_ {1} (9 2 - 3 2) + \mu_ {2} (9 2 - 6 0) \geq (1 + \rho) 8
$$

The optimal value of $\rho$ of the above model is equal to $\rho _ { 1 } =$ −0.3600. Hence, $X _ { 1 }$ is not surely worse than $X _ { 3 }$ and we proceed to the next step and solve the following linear programming model:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Min $\varphi$

s.t. $68\mu_{1} + 56\mu_{2} + 40\mu_{3}\leq 88(1 + \varphi)$ $80\mu_{1} + 32\mu_{2} + 100\mu_{3}\leq 50(1 + \varphi)$ $32\mu_{1} + 92\mu_{2} + 60\mu_{3}\leq 8(1 + \varphi)$ $\mu_1 + \mu_2 + \mu_3 = 1$ $\mu_1,\mu_2,\mu_3\geq 0$
</div>

The optimal value of $\varphi$ is equal to $\varphi _ { 1 } = 3 .$ . The score of $\theta _ { 1 } ( X _ { 3 } ) =$ 0.1071 is obtained, implying that $X _ { 1 }$ is possibly worse than $X _ { 3 } .$ For the alternatives $X _ { 4 } , X _ { 5 }$ and $X _ { 6 }$ a similar procedure leads us to additional preference information. The values of the optimal solutions of models (1) and (2) and the score θ for all alternatives are shown in Table 2.

For alternative $X _ { 4 } , \rho _ { 4 } = - 0 . 6 2 7 9 \le 0$ and $\varphi _ { 4 } = - 0 . 0 1 1 0 < 0 .$ . Hence, $X _ { 4 }$ is surely better than the vertex $X _ { 3 }$ and the ordered pair $( X _ { 4 } , X _ { 3 } )$ is identi<sup>fi</sup>ed. For alternative $X _ { 5 } , \rho _ { 5 } = 0 . 3 0 3 7 { > } 0$ , shows that $X _ { 5 }$ is surely worse than the vertex $X _ { 3 }$ and the ordered pair $( X _ { 3 } , X _ { 5 } )$ is identi<sup>fi</sup>ed to extend the preference set $P .$ There is no need to solve model (2) as we know its solution will yield $\varphi _ { 5 } { > } 0$ by Theorem 1. Also $\theta _ { 6 } ( X _ { 3 } ) = 0 . 4 4 2 4$ implies that $X _ { 6 }$ is possibly worse than $X _ { 3 } .$ At the end of this step, the updated strict partial order is obtained as follows:

$$
P = \{(X _ {2}, X _ {3}), (X _ {7}, X _ {3}), (X _ {6}, X _ {5}), (X _ {7}, X _ {1}), (X _ {3}, X _ {5}), (X _ {4}, X _ {3}) \}.
$$

So far, we only used the exact preference relations stated by the DM or implied by theory. Now we incorporate the approximate preference relations using the thresholds. Let $t _ { 1 } = 0 . 1$ and $t _ { 2 } = 0 . 9$ Table 2 shows that $\theta _ { 1 } ( X _ { 3 } ) = 0 . 1 0 7 1 \geq 0 . 1$ and ${ \theta } _ { 6 } ( X _ { 3 } ) = 0 . 4 4 2 4 \leq 0 . 9 .$ These do not satisfy the thresholds and set P remains unchanged. The current binary preferences can be represented by the directed graph in Fig. 4.

![](/api/attachments/SAHZ4EZ9/fulltext/images/deb087090822be72bb5bd1ed9814d7e21c6d2a0208c2a4baa4758c2f5b65ead4.jpg)  
Fig. 4. The updated preference graph after using $C _ { 1 } { = } C ( X _ { 2 } , X _ { 3 } , X _ { 7 } ; X _ { 3 } )$

Table 3  
Results for cone $C _ { 2 } { = } C ( X _ { 5 } , X _ { 6 } ; X _ { 5 } ) .$

<table><tr><td>Alternatives</td><td> $\rho$ </td><td> $\varphi$ </td><td> $\theta$ </td><td>Preferences</td></tr><tr><td> $X_{1}$ </td><td>-0.9</td><td>3.3750</td><td>0.2105</td><td> $X_{1}$ possibly worse than  $X_{5}$ </td></tr></table>

Results for cone $C _ { 3 } = C ( X _ { 1 } , X _ { 7 } ; X _ { 1 } ) .$

<table><tr><td>Alternatives</td><td> $\rho$ </td><td> $\varphi$ </td><td> $\theta$ </td><td>Preferences</td></tr><tr><td> $X_{2}$ </td><td>-0.7500</td><td>-0.0221</td><td>1</td><td> $X_{2}$ surely better than  $X_{1}$ </td></tr><tr><td> $X_{3}$ </td><td>-0.9130</td><td>0.5683</td><td>0.6164</td><td> $X_{3}$ possibly better than  $X_{1}$ </td></tr><tr><td> $X_{4}$ </td><td>-0.9070</td><td>0.0746</td><td>0.9240</td><td> $X_{4}$ possibly better than  $X_{1}$ </td></tr><tr><td> $X_{5}$ </td><td>-0.9158</td><td>9.0000</td><td>0.0924</td><td> $X_{5}$ possibly worse than  $X_{1}$ </td></tr><tr><td> $X_{6}$ </td><td>-0.7714</td><td>0.3878</td><td>0.6655</td><td> $X_{6}$ possibly better than  $X_{1}$ </td></tr></table>

Considering the second convex cone $C _ { 2 } { = } C ( X _ { 5 } , ~ X _ { 6 } ; ~ X _ { 5 } )$ and applying the two-stage procedure for alternatives $X _ { 1 } , X _ { 2 } , X _ { 3 } , X _ { 4 }$ and $X _ { 7 }$ we obtain new preferences. Since there is a path from $X _ { 2 } , X _ { 3 } , X _ { 4 }$ and $X _ { 7 }$ to $X _ { 5 } ,$ we ignore them. The score $\theta _ { 1 } ( X _ { 5 } )$ for alternative $X _ { 1 }$ is determined by solving models (1) and (2) and is shown in Table 3.

It can be seen that ${ \theta _ { 1 } ( X _ { 5 } ) = 0 . 2 1 0 5 \le 0 . 9 }$ . Hence, the strict partial order in this step remains unchanged and the preference graph is exactly the same as the graph in Fig. 4.

Finally, for the third cone $C _ { 3 } { = } C ( X _ { 1 } , X _ { 7 } ; X _ { 1 } )$ , we apply the two-step procedure for alternatives $X _ { 2 } , X _ { 3 } , X _ { 4 } , X _ { 5 }$ and $X _ { 6 } .$ The results are reported in Table 4.

Table 4 shows that for alternative $X _ { 2 } , \ \rho _ { 2 } = - 0 . 7 5 \leq 0$ and $\varphi _ { 2 } =$ $- 0 . 0 2 2 1 { < } 0 .$ . Hence, X is surely better than the vertex $X _ { 1 }$ and the ordered pair $( X _ { 2 } , X _ { 1 } )$ is identi<sup>fi</sup>ed. Furthermore, $\theta _ { 4 } ( X _ { 1 } ) = 0 . 9 2 4 0 > 0 . 9$ and $\theta _ { 5 } ( X _ { 1 } ) = 0 . 0 9 2 4 < 0 . 1$ . Therefore, the approximate preference relations $( X _ { 4 } , X _ { 1 } )$ and $( X _ { 1 } , X _ { 5 } )$ can be added to the set of preferences and the <sup>fi</sup>nal strict partial order is

$$
\begin{array}{c} P = \{(X _ {2}, X _ {3}), (X _ {7}, X _ {3}), (X _ {6}, X _ {5}), (X _ {7}, X _ {1}), (X _ {3}, X _ {5}), (X _ {4}, X _ {3}), (X _ {2}, X _ {1}), \\ (X _ {4}, X _ {1}), (X _ {1}, X _ {5}) \} \end{array}
$$

which is shown in the following preference graph.

In Fig. 5, the dotted nodes represent the approximate preferences. The above graph corresponds to an asymmetric transitive binary relation over the set of alternatives which is the strict partial order. Note that in our illustrative example none of the approximate preferences is in con<sup>fl</sup>ict with the rank order speci<sup>fi</sup>ed by our hypothetical value function $( X _ { 4 } { > } X _ { 7 } { > } X _ { 2 } { > } X _ { 3 } { > } X _ { 1 } { > } X _ { 6 } { > } X _ { 5 } )$

![](/api/attachments/SAHZ4EZ9/fulltext/images/b70bf6cc29be282002801aaee0417faba6df9b068ef178a2559f0a668a90f65b.jpg)  
Fig. 5. The <sup>fi</sup>nal preference graph.

## 5. Conclusions

Exploiting the properties of a quasi-concave value function, we developed an approach to <sup>fi</sup>nd a preference-based strict partial order for a <sup>fi</sup>nite set of multiple criteria alternatives. It can be used as an exact or an approximate approach by adjusting the threshold parameters. The degree of approximation can also be adjusted through these parameters.

This approach can as such be used to partially rank multiple criteria alternatives or as a supplementary method to incorporate preference information in, e.g. Data Envelopment Analysis and Evolutionary Multi-Objective Optimization. For prior research on these topics, see Refs. [1,3,16].

The approach can also be extended into an interactive approach that iterates between obtaining preference information from the DM and updating the approximate strict partial order until a satisfactory result is reached. Developing such an interactive approach is a subject of future research.

## Acknowledgement

The authors thank Banu Lokman from the Industrial Engineering Department, Middle East Technical University for her helpful comments on an earlier version of the manuscript.

## References

[1] J. Fowler, E. Gel, P. Korhonen, M. Köksalan, J. Marquis, J. Wallenius, Interactive evolutionary multi-objective optimization for quasi-concave preference func tions, European Journal of Operational Research 206 (2010) 417–425.

[2] A. Geoffrion, J. Dyer, A. Feinberg, An interactive approach for multi-criterion optimization, with an application to the operation of an academic department, Management Science 19 (1972) 357–368.

[3] M. Halme, T. Joro, P. Korhonen, S. Salo, J. Wallenius, Value ef<sup>fi</sup>ciency approach to incorporating preference information in data envelopment analysis, Management Science 45 (1999) 103–115.

[4] E. Hinloopen, P. Nijkamp, P. Rietveld, The regime method: a new multicriteria technique, in: P. Hansen (Ed.), Essays and Surveys on Multiple Criteria Decision Making, Springer, 1983, pp. 146–155.

[5] I. Kaliszewski. W. Michalowski. Efficient solutions and bounds on tradeoffs. Journal of Optimization Theory and Applications 94 (1997) 381–394.

[6] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preference and Value Trade-offs, Wiley, New York, 1976.

[7] P. Korhonen, A hierarchical interactive method for ranking alternatives with multiple qualitative criteria, European Journal of Operational Research 24 (2) (1986) 265-276.

[8] P. Korhonen, A visual reference direction approach to solving discrete multiple criteria problems, European Journal of Operational Research 34 (1988) 152–159.

[9] P. Korhonen, J. Laakso, A visual interactive method for solving the multiple criteria problem, European Journal of Operational Research 24 (1986) 277–287.

[10] P. Korhonen, J. Wallenius, S. Zionts, Solving the discrete multiple criteria problem using convex cones, Management Science 30 (11) (1984) 1336–1345

[11] M. Köksalan, Identifying and ranking a most preferred subset of alternatives in presence of multiple criteria, Naval Research Logistics 36 (1989) 359–372.

[12] M. Köksalan, M. Karwan, S. Zionts, An improved method for solving multiple criteria problems involving discrete alternatives, IEEE: Transaction on Systems, Man and Cybernetics, SMC 14 (1984) 24–34.

[13] M. Köksalan, P.N.S. Sagala, Interactive approaches for discrete alternative multiple criteria decision making with monotone utility functions, Management Science 41 (1995).1158-1171

[14] M. Köksalan, P.N.S. Sagala, An approach and computational results on testing the form of a decision maker's utility function, Journal of Multi-criteria Decision Analysis 4 (1995) 189–202.

[15] M. Köksalan, O.V. Taner, An approach for <sup>fi</sup>nding the most preferred alternative in the presence of multiple criteria, European Journal of Operational Research 60 (1992) 52–60.

[16] M. Köksalan, C. Tuncer, A DEA-based approach to ranking multi-criteria alternatives,, International Journal of Information Technology & Decision Making 8 (1) (2009) 29–54.

[17] H.L. Li, L.C. Ma, Ranking decision alternatives by integrated DEA, AHP and GOWER PLOT techniques, International Journal of Information Technology & Decision Making 7 (2) (2008) 241–258.

[18] V. Lot<sup>fi</sup>, An aspiration-level interactive method (AIM) for decision making, Operations Research Letters 8 (1989) 113–115.

[19] V. Lot<sup>fi</sup>, T.J. Stewart, S. Zionts, An aspiration­level interactive model for multiple criteria decision making, Computers and Operations Research 19 (1992) 671–681.

[20] S.Y. Prasad, M. Karwan, S. Zionts, Use of convex cones in interactive multiple objective decision making, Management Science 43 (1997) 723–734.

[21] B. Roy, How outranking relation helps multiple criteria decision making, in: J. Cochrane, M. Zeleny (Eds.), Multiple criteria decision making, University of South Carolina Press, Columbia, SC, 1973, pp. 179–201.

[22] T. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[23] A.A. Salo, R.P. Hämäläinen, Preference assessment by imprecise ratio statements, Operations Research 40 (1992) 1053–1061.

[24] P. Salminen, P. Korhonen, J. Wallenius, Testing the form of a decision maker's multiattribute value function based on pairwise preference information, Journal of Operational Research Society 40 (3) (1989) 299–302.

[25] A. Wierzbicki, The use of reference objectives in multiobjective optimization, in: G. Fandel, T. Gal (Eds.), Multiple Criteria Decision Making, Theory and Application, Springer, New York, 1980.

[26] S. Zionts, A multiple criteria method for choosing among discrete alternatives, European Journal of Operational Research 7 (1981) 143–147.

[27] S. Zionts, J. Wallenius, An interactive programming method for solving the multiple criteria problem, Management Science 22 (1976) 652–663.

[28] S. Zionts, J. Wallenius, Identifying ef<sup>fi</sup>cient vectors: some theory and computational results, Operations Research 28 (1980) 785–793.

Akram Dehnokhalaji is an assistant professor in the Department of Mathematics at Tehran Tarbiat Moallem University of Iran. Her research interests include multiple criteria decision making and data envelopment analysis.

Murat Köksalan is a professor in the Department of Industrial Engineering, Middle East Technical University He has been a visiting professor at, SUNY Buffalo Purdue University, Helsinki University of Technology, Helsinki School of Economics, and Aalto University on various occasions. He is the recipient of the young researcher award of the Scienti<sup>fi</sup>c and Technological Research Council of Turkey and The MCDM Gold Medal of the International Society on Multiple Criteria Decision Making. He is the founding president of INFORMS Section on MCDM. He won the <sup>fi</sup>rst prize at the INFORMS Case Competition with various co-authors three times. His academic interests include multiple criteria decision making, combinatorial optimization, heuristic search in general and evolutionary algorithms in particular, combinatorial auctions, and preparing teaching cases.

Pekka Korhonen is Professor of Statistics at the Aalto University School of Economics (formerly Helsinki School of Economics). He holds a doctorate from Helsinki University. Korhonen is one of the leaders of his field, which encompasses Multiple Criteria Decision Making, decision support, and Data Envelopment Analysis. He is a recipient of multiple awards and distinctions, notably the Cantor award from the Int. Society on Multiple Criteria Decision Making. He is past President of the Int. Society on Multiple Criteria Decision Making.

Nasim Nasrabadi is an assistant professor in the Department of Mathematics at the University of Birjand, Iran. Her research interests include multiple criteria decision making, data envelopment analysis, and network <sup>fl</sup>ows

Jyrki Wallenius is Professor of Management Science at the Aalto University School of Economics (formerly Helsinki School of Economics). He holds a doctorate from the Helsinki School of Economics. Wallenius is one of the leaders of his <sup>fi</sup>eld, which encompasses Multiple Criteria Decision Making and computer-based decision support. He is former editor of the European Journal of Operational Research. Wallenius is a recipient of multiple awards and distinctions, notably the Edgeworth-Pareto award from the Int. Society on Multiple Criteria Decision Making. He is currently the President of the Int. Society on Multiple Criteria Decision Making.
