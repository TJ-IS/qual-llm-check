---
otero_id: 15940
otero_key: "GPQ4AJMR"
title: "Multi-criteria group consensus under linear cost opinion elasticity"
authors: "D. Ben-Arieh; T. Easton"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.11.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Multi-criteria group consensus under linear cost opinion elasticity

D. Ben-Arieh <sup>⁎</sup>, T. Easton

Department of Industrial and Manufacturing Systems Engineering, Kansas State University, 216 Durland Hall, Manhattan, Kansas, 66506, USA

Received 28 September 2005; received in revised form 9 November 2006; accepted 14 November 2006 Available online 26 December 2006

## Abstract

Consensus is a pivotal concept in group decision making. Many times, such a consensus is achieved by the experts shifting their opinion towards a point of mutual consent. Such a shift in many cases is the result of laborious negotiations, which escalates the cost of reaching the consensus. Moreover, many times the group decision is multi-criteria oriented in which the experts need to agree on each criterion separately.

This paper describes three problems where experts of unequal importance and with a linear cost of changing their opinion (opinion elasticity) consider a single and a multi-criteria decision consensus. These problems achieve a minimum cost consensus without a budget limit. It turns out that the optimal consensus point is at the median opinion for rectilinear cost function and at the weighted average opinion for squared geometric distance calculations.

Linear-time algorithms are presented for all cost consensus problems with no budget limits. Proofs, computational complexity and examples are provided for these algorithms. © 2006 Elsevier B.V. All rights reserved.

Keywords: Distributed decision making; Consensus; Multiple experts

## 1. Introduction

I shall not today attempt further to define the kinds of material, but I know it when I see it”. These famous words of US Supreme Court Justice Potter Stewart did not relate to consensus, although in a similar manner, consensus defies clear definition.

Traditionally, consensus implied a strict and unanimous agreement of all the experts. A classical example of a unanimous agreement involves jury verdicts of severe crimes. If a single jury member does not agree, it is considered a hung jury and no verdict is given in which case a new jury is selected and the trial must be repeated. The cost associated with a new trial is significant and so a jury may receive a substantial amount of pressure to reach a consensus verdict. Some juries have taken weeks to arrive at a consensus verdict.

Ness and Hoffman [17] presented a more moderate definition of consensus, which they defined as “a decision that has been reached when most members of the team agree on a clear option and the few who oppose it think they have had a reasonable opportunity to influence that choice. All team members agree to support the decision.”

Practically, it is very unlikely that a group of experts will share the exact same opinion, especially in the case of a multi-criteria decision problem. Yet, in many cases such a consensus is a necessity in order for a group to reach a mutually agreed decision. Consensus as a process of aggregating experts' judgments has many forms of implementation such as judging figure skating or monetary civil suits (suing for damages). Clearly each such implementation has a different expected level of agreement required from the experts.

With the recognized importance of agreement among experts, consensus has received much attention in the literature (e.g. [1,5,6,12]), mostly as a measurable indication to the quality of the group decision. Generally, the approaches towards reaching consensus in the literature can be divided into two categories. The first one treats consensus as a “mathematical aggregated consensus” [18]. This type of consensus requires some kind of binding arbitration so the contributing experts do not need to converge in their opinions. In some cases, the consensus is achieved by changing the weights of the experts (e.g. [13]) or is calculated as a weighted mean of the participating opinions (e.g. [3]). Also, the consensus can be calculated as an optimal property such as a point that minimizes the weighted sum dissimilarity between the experts [13] or the minimum distance between the experts and the group [19]. In all these cases the experts do not shift their opinion, and the consensus is just a calculated opinion—an opinion that no expert may hold.

In the second type of consensus, the experts are expected to modify their opinion in order to reach a closer agreement in opinions (e.g. [6,7]). This is usually accomplished using a structured group mediation method such as the Delphi approach [14] or Nominal Group Techniques [8]. Many of the consensus reaching methodologies calculate the group decision as an aggregate of the individual opinions and instruct the experts on how to modify their opinion in order to increase the level of consensus. Thus, consensus is measured quantitatively either as an indication to the group decision quality, or as a way to instruct the experts on how to modify their opinion. There are four main approaches to measuring the level of consensus relative to the group opinion: based on a count of the number of experts who share the opinion with the group, based on the distance between the experts and the group decision, based on a similarity or dissimilarity measure between the experts and the group and based on the rank order of the alternatives by the group and by the experts.

A large body of research considers consensus to have fuzzy properties sometimes termed “soft consensus” as in [10,11], allowing the experts' opinions to be represented as fuzzy numbers. Another model for consensus compares the positions of the alternatives founded on the individual solutions and the group solution [6]. Based on the consensus level and the offset of individual solutions, the model gives feedback suggesting the direction in which the individual experts should change their opinion. In effect, the experts compromise their opinion for the sake of consensus. A similar approach presented in [2] calculates consensus based on similarity between preference vectors of the experts. This similarity is used to generate measures of group agreement and group disagreement using threshold parameters. Montero [16] examined the general issue of aggregating expert opinions, showing that the mean and median opinions minimize the “social stress” under Euclidean and rectilinear metrics.

A different school of thought assumes that a consensus is an impossibility since experts, by the nature of their expertise, do not often converge into a common opinion [4]. An excellent review of this expert disagreement phenomenon in different domains can be found in [20,21].

This paper adopts the second approach in which experts can be convinced to shift their position in a manner similar to the Delphi approach. In this approach it takes effort to cause experts to shift their position. This reconciliation effort includes repetitive surveys of the experts, long conversations, visits and interviews, which escalate the costs of arriving at a consensus [9]. Similarly, the cost of bridging the opinion gap among experts includes processing the opinions, maintaining a facilitating party and compensating the experts for travel and communication costs [14]. Therefore, there is a need to find a consensus in a manner that minimizes these costs. This paper focuses on instances where each expert has a linear cost “opinion elasticity” representing the cost of changing the expert's opinion in some cost unit. This minimum cost consensus is then used by the mediator to obtain the optimal convergence point of all experts.

The significance of this paper is in introducing the new concept of the minimum cost consensus. Moreover, the paper defines new variants of the problem termed ε- consensus and provides optimal solutions to all the problems. Also, the paper expands the problems to the multi-criteria cases with its solutions. These problems have not been addressed by the Decision Support Systems community; however, location theory [15] has provided solutions to some of these problems.

From a practical point of view, there are cases in which it may be hard to provide a numeric value to the experts' opinion, especially in an abstract domain such as the paper discusses. However, in many cases experts do provide a quantitative value of their judgments such as the professional livestock judges discussed in [4].

The remainder of the paper is organized as follows. Some notation and assumptions are provided in Section 2. Section 3 presents two algorithms that solve the minimum cost consensus problem when there is no budget constraint, for experts with varying degrees of importance (weight) using a single criterion decision. Section 4 describes the problem and solution for the minimum cost multi-criteria consensus using rectilinear and geometric cost calculations. Conclusions and some directions for future research are discussed in Section 5.

## 2. Consensus notation

Before these minimum cost consensus problems are analyzed, some notation must first be developed. Let $E =$ $\{ e _ { 1 } , . . . , e _ { n } \}$ be a set of n experts that provide an opinion on $J { \in } Z$ topics (criteria). Define $o _ { i , j } { \in } \Re$ as expert $i ^ { \circ } \mathbf { s }$ initial opinion regarding the jth criterion for $i { = } 1 , . . . ,$ n and $j = 1$ $\mathrm { . . . , } J .$ For each expert, define $c _ { i } \in \Re ^ { + }$ to be the cost of moving expert $i \mathrm { \ ' } _ { \mathrm { S } }$ opinion 1 unit. Thus, it costs $c _ { i } | | o _ { i } - o _ { i } ^ { \prime } | |$ to change expert $i \ ' \mathrm { s }$ opinion from $o _ { i }$ to $o _ { i } ^ { \prime }$ where $\bigstar \bigstar | | \bigstar | |$ is the distance in some metric. For the remainder of the paper, $o _ { i } ^ { \prime } { = } ( o _ { i , 1 } ^ { \prime } , o _ { i , 2 } ^ { \prime } { , . . . , o _ { i , J } ^ { \prime } } )$ will denote expert $i \mathrm { \ ' } _ { \mathrm { S } }$ current opinion.

A standard set of metrics is the p-norms $( \parallel \parallel _ { p } )$ for $p { \geq } 1$ . Given $\boldsymbol { x } { = } ( x _ { 1 } , . . . , x _ { m } )$ and $y = ( y _ { 1 } , \cdots y _ { m } ) { \in } \Re ^ { m }$ , then $\begin{array} { r } { | | x - y | | _ { p } = ( \sum _ { i = 1 } ^ { m } x _ { i } – y _ { i } | | ^ { p } ) ^ { \frac { 1 } { p } } } \end{array}$ . If $p { = } 1$ , then the p-norm is equivalent to the rectilinear or Manhattan distance. If $p { = } 2$ , then the p-norm is equivalent to the Euclidean or straight-line distance. If $p { = } \infty$ , then the p-norm is the maximum distance in any single dimension, $\scriptstyle \operatorname* { m a x } _ { i = 1 \ldots , m } | x _ { i } - y _ { i } | .$

As mentioned in Section 1, there can be a number of distinct ways to define a common consensus. Here, an exact common consensus, called a common consensus, occurs if and only if every expert has the same opinion for each criterion, i.e. $o _ { 1 , j } ^ { \prime } { = } o _ { 2 , j } ^ { \prime } { = } . . . { = } o _ { n , j } ^ { \prime }$ for all $\scriptstyle j = 1 , \ldots J .$ A close consensus, called an ε common consensus, occurs at $o ^ { \prime } { = } ( o _ { 1 } ^ { \prime } , ~ o _ { 2 } ^ { \prime } , . . . , ~ o _ { J } ^ { \prime } )$ if and only if every expert's opinion is sufficiently close to $o _ { j } ^ { \prime } .$ Mathematically, $o ^ { \prime }$ is an ε common consensus, for some $\varepsilon > 0 .$ , if and only if $\left\| { \boldsymbol { o } } _ { i } ^ { \prime } - { \boldsymbol { o } } ^ { \prime } \right\| \leq \varepsilon$ for all $i { = } 1 , . . . , n$ Regardless of the problem, an optimal opinion will be denoted by $o ^ { * } { = } ( o ^ { * } { } _ { 1 } , o ^ { * } { } _ { 2 } { , } . . . , o ^ { * } { } _ { J } )$

Throughout the remainder of the paper, we will assume that for each $j { = } 1 , { \ldots } , J$ there exist experts $i ,$ $k { \in } \{ 1 , . . . , n \}$ such that $o _ { i , j } \neq o _ { k , j } .$ . If not, every expert has the same opinion in the jth criterion and it can be removed from the problem. Fig. 1 represents a graphical view of 4 experts' initial opinions of 3 distinct criteria. For example, using criterion 2, the figure shows that expert $e _ { 3 }$ has the lowest score, followed by expert $_ { e _ { 2 } , }$ with expert $e _ { 1 }$ with a much higher score followed by $e _ { 4 }$ with the highest score.

![](/api/attachments/GPQ4AJMR/fulltext/images/909adb547dc5275c7c6f2ff27ec2d35c73186f3b281cda074093569f59773737.jpg)  
Fig. 1. Representing four expert's initial scores of three distinct criteria.

In addition to the expert's opinion and cost, each expert has a degree of importance $w _ { i } { \in } { \mathfrak { R } } ^ { + }$ , representing the weight that should be attributed to expert $i \mathbf { \ ' } _ { \mathbf { S } }$ opinion. As an example, assume that a family with small children is buying a van. While the children may be strongly enticed by entertainment features (such as DVD and video game capabilities), their opinions should not be assigned the same weight as the adults opinions.

The methodology can be applied to numerous areas, one example being the Product Development domain. In this application, various design groups decide on the product properties based on various functional objectives. Usually, the various design groups come up with various opinions regarding a feature such as product's diameter, weight, etc. Ultimately, all groups have to converge to a single value, each one modifying their preferred value, under an estimated penalty for deviating from the perceived “optimal” value.

The problems considered here seek to find an opinion that yields a minimum cost weighted consensus, on both single and multiple criteria. As one would expect, different choices of the metrics yield different optimal consensus points. We begin with the case where there is only one criterion and develop a solution methodology leading to the algorithms that can solve multiple criteria problems.

## 3. Single criterion unconstrained cost weighted consensus problems

This section describes two algorithms that obtain the minimum cost consensus with unlimited budget and a single criterion. The first problem discusses the weighted consensus at minimum cost problem (WCMC). The second problem describes how to find an ε consensus at minimum cost (εWCMC).

The assumption that the experts only have a single criterion is substantially limiting. Since the experts can only move in a single direction, all p-norms are equivalent for any $p { \in } [ 1 , \infty ]$ . That is, $\| x - y \| _ { p } = | x - y |$ where $x , y { \in } \Re$ . So for the remainder of this section, assume that the distance between $o ^ { \prime }$ and $o ^ { \prime \prime }$ is $| o ^ { \prime } - o ^ { \prime \prime } |$ In addition, also assume that the opinions can be ordered such that $o _ { 1 , 1 } \leq o _ { 2 , 1 } \leq . . . \leq o _ { n , 1 }$ . We may further assume that $o _ { 1 , 1 } { < } o _ { 2 , 1 } { < } . . . . < o _ { n , 1 }$ . If not, then $o _ { i , 1 } { = } o _ { i + 1 , 1 }$ for some $i { \in } \{ 1 , . . . , n { - } 1 \}$ . When two experts i and $i + 1$ (without loss of generality) share the same opinion with regard to criterion $j ,$ one can merge these two experts into a single expert with a cost of $c _ { i } + c _ { i + 1 }$ per unit opinion moved and a weight of $w _ { i } + w _ { i + 1 }$

## 3.1. The weighted consensus at minimum cost problem

The single consensus opinion cost function, $f _ { c } ,$ takes as input a desired consensus ${ \boldsymbol { o } } ^ { \prime } \in { \mathfrak { R } }$ and returns the weighted cost required to change every expert's opinion to $o ^ { \prime }$ . Since each expert has a weight and linear cost, it is not difficult to see that $f _ { c }$ is piecewise linear and given by the following equation $\begin{array} { r } { f _ { c } ( o ^ { \prime } ) { = } \sum _ { i \in \{ 1 , . . . , n \} } w _ { i } c _ { i } | o _ { i , 1 } { - } o ^ { \prime } | . } \end{array}$ WCMC seeks an $o ^ { * } \in \Re$ such that $f _ { c } ( o ^ { * } ) \mathop { \leq } f _ { c } ( o ^ { \prime } )$ for every $o ^ { \prime } \in \Re$

Finding an optimal solution to WCMC is a wellsolved problem from location theory [15]. Here we present a linear-time algorithm to calculate an optimal solution to WCMC. This algorithm is not new but does provide the reader with some key concepts for the forthcoming ε common consensus problems. These ε common consensus problems along with their algorithms have not been previously studied.

The following algorithm provides a solution to WCMC. The sets L and R represent the experts that are to the left and right of the optimal value and thus these experts' opinions will need to be moved.

## 3.1.1. WCMC algorithm (WCMCA)

Initialization: Sort the experts by their opinion such as $o _ { 1 , 1 } { < } o _ { 2 , 1 } { < } . . . { < } o _ { n , 1 }$

Set L ←{1}, R←{n}, l=1 and r=n.

Main Step: While $l \neq r .$

define $\scriptstyle c _ { L } ^ { \prime } = \sum _ { i \in L } w _ { i } c _ { i } .$

define $\scriptstyle c _ { R } ^ { \prime } = \sum _ { i \in R } w _ { i } c _ { i } .$

$\operatorname { I f } c _ { L } ^ { \prime } \leq c _ { R } ^ { \prime }$ , then $l \gets l + 1$ and $L \gets L \cup \{ l \}$

Else, $r  r - 1$ and $R \gets R \boxdot { \ = } \{ r \}$

Termination: Return $o _ { r , 1 }$ as the optimal opinion, $o _ { r , 1 } =$ $o ^ { * } { = } o _ { 1 , 1 } ^ { \prime } { = } . . . { = } o _ { n , 1 } ^ { \prime }$ , and the total weighted cost $f _ { c } ( o ^ { * } )$

## 3.1.2. Proof of correctness

Without loss of generality, we may assume that WCMCA returns an $o ^ { * } { = } o _ { k , 1 }$ for some $k { \in } \{ 1 , . . . , n \}$ . Let $\delta > 0$ and δbmin $\{ | o _ { k , 1 } - o _ { k - 1 , 1 } | , | o _ { k , 1 } - o _ { k + 1 , 1 } | \}$ . Examining $\begin{array} { r } { f _ { c } ( o ^ { * } + \delta ) = f _ { c } ( o ^ { * } ) + \textstyle \sum _ { i \in \{ 1 . . k \} } w _ { i } c _ { i } \delta - \textstyle \sum _ { i \in \{ k + 1 . . n \} } w _ { i } c _ { i } \delta . } \end{array}$ Due to the algorithm, $\begin{array} { r } { \sum _ { i \in \{ 1 . . k \} } w _ { i } c _ { i } \ge \sum _ { i \in \{ k + 1 . . n \} } w _ { i } c _ { i } ; } \end{array}$ thus, $f _ { c } ( o ^ { * } + \delta ) { \ge } f _ { c } ( o ^ { * } )$ . Similarly, $f _ { c } ( o ^ { * } - \delta ) { = } f _ { c } ( o ^ { * } ) -$ $\begin{array} { r } { \sum _ { i \in \{ 1 . . k - 1 \} } w _ { i } c _ { i } \delta + \sum _ { i \in \{ k . . n \} } w _ { i } c _ { i } \delta . } \end{array}$ . Again, due to the algorithm, $\begin{array} { r } { \sum _ { i \in \{ 1 . { k } - 1 \} } w _ { i } c _ { i } \le \sum _ { i \in \{ k . { n } \} } w _ { i } c _ { i } } \end{array}$ and so $f _ { c } ( o ^ { * } - \delta ) { \ge } f _ { c } ( o ^ { * } )$ Consequently, $o ^ { * }$ is a local optimal. Observe that $f _ { c }$ is the summation of convex functions and so $f _ { c }$ is also convex. Consequently, any local optimal solution is also a global optimum and the result follows.

The running time of this algorithm is $O ( n )$ . Each cost and opinion only needs to be examined a single time (assuming that a cumulative sum of $c _ { L } ^ { \prime }$ and $c _ { R } ^ { \prime }$ are efficiently implemented). Thus, the algorithm has a linear run time.

Example 1. Given are the following initial opinion pool of five experts: $( 0 . 5 , \ 1 . 0 , \ 2 . 5 , \ 3 . 0 , \ 6 . 0 )$ , with the corresponding cost vector $c { = } ( 1 . 0 , 4 . 0 , 3 . 0 , 5 . 0 , 2 . 0 )$ and weight vector w = (6.0, 3.0, 4.0, 1.0, 2.0).

Step 1: $L = \{ 1 \} , R = \{ 5 \}$ . So $c _ { L } ^ { \prime } { = } 6 . 0$ and $c _ { R } ^ { \prime } { = } 4 . 0$ . Thus, $R \gets \{ 4 , 5 \}$ and $r { = } 4 .$ . So expert 5's opinion is moved to expert $4 \mathrm { { : } s }$ initial opinion.

Step $2 \colon L = \{ 1 \} , R = \{ 4 , 5 \} , c _ { \mathrm { L } } ^ { \prime } = 6 . 0$ (unchanged) and $c _ { R } ^ { \prime } = $ 9.0. Thus $L \gets \{ 1 , 2 \}$ and r remains 4. So expert $1 { \mathrm { : } } { \mathrm { } } $ opinion is moved to expert $2 \mathrm { { } ^ { \circ } s }$ initial opinion.

Step $3 \colon L = \{ 1 , 2 \} , R = \{ 4 , 5 \} , c _ { L } ^ { \prime } = 6 + 1 2 = 1 8 . 0$ and $c _ { R } ^ { \prime } = $ 9.0 (unchanged). Thus, $R \gets \{ 3 , 4 , 5 \} , r = 3$ , and l remains as 2. Experts 4 and $5 \mathrm { { ^ { \circ } s } }$ opinions are moved to expert $3 ^ { \circ } \mathrm { s }$ initial opinion.

Step 4: $L = \{ 1 , 2 \} , R = \{ 3 , 4 , 5 \} , c _ { R } ^ { \prime } = 4 + 5 + 1 2 + = 2 1 . 0$ and ${ c _ { L } ^ { \prime } } { = } 1 8 . 0 .$ . Thus, $L \gets \{ 1 , 2 , 3 \}$ and $l { = } 3$ . So experts 1 and $2 \mathrm { { } ^ { * } s }$ opinions are moved to expert $3 \mathrm { { } ^ { \circ } s }$ initial opinion.

Termination step: Since $l { = } r { = } 3 ,$ , the optimal consensus opinion is at $2 . 5 \left( o _ { 3 } \right)$ with $2 . 5 { = } \sigma ^ { * } { = } { o ^ { * } } _ { 1 } { = } _ { \ldots } { = } { o ^ { * } } _ { 5 }$ . The overall weighted cost is $6 ^ { * } ( 2 . 5 - 0 . 5 ) + 1 2 ^ { * } ( 2 . 5 - 1 ) +$ $1 2 ^ { * } ( 2 . 5 - 2 . 5 ) + 5 ^ { * } ( 3 . 0 - 2 . 5 ) + 4 ^ { * } ( 6 . 0 - 2 . 5 ) = 4 6 . 5 , \mathrm { o r }$ equivalently one can view this costs by incrementally moving sets of experts which leads to $6 ^ { * } ( 1 - 0 . 5 ) ^ { + }$ $4 ^ { * } ( 6 - 3 ) + 1 8 ^ { * } ( 2 . 5 - 1 ) + 9 ^ { * } ( 3 - 2 . 5 ) = 4 6 . 5 .$

A common technique to gain a single criterion consensus among n equally weighted experts is to take their average opinion as the best consensus. WCMCA shows that this technique may be nonoptimal and requires the total amount of opinion changed to be larger than necessary. WCMCA shows that the correct answer to this problem is the median opinion. For instance, if the opinions were {0,1,3,5,11}, then the average opinion is 4. To arrive at a consensus, the experts must change their opinions by $4 + 3 + 1 + 1 + 7 = 1 6$ . However, WCMCA has an optimal opinion of 3 (the median) with a total change of $3 + 2 + 0 + 2 + 8 = 1 5$

If the experts do not have identical costs and weights, then WCMCA will return the weighted cost median of these n experts. A weighted cost median can be easily seen by replacing the one expert at $o _ { i , 1 }$ with $w _ { i } c _ { i }$ experts at $o _ { i , 1 }$ for each $i { = } 1 , . . . , n$ . The optimal solution now occurs at the median opinion point (half of these “new” experts have a lower opinion and half a higher one).

One insightful remark should additionally be made regarding the 2 expert consensus problem (when n is restricted to two). The expert that is the most stubborn (highest weighted cost to move) has the opinion that is the optimal solution to WCMC. From an expert's point of view, the optimal policy for any expert results in an infinite cost solution. That is to say, if expert one is asked to change his/her opinion, he or she should sufficiently increase his/her cost function until the other expert is required to change his/her opinion. This process continues to escalate with each expert becoming more obstinate until a consensus will never be reached. This analysis supports the importance of a moderator in negotiations.

## 3.2. The ε consensus at minimum cost problem

A natural variation of WCMC is to allow each expert's opinion to be sufficiently close to a consensus opinion. Recall that an opinion $o ^ { \prime } \in \Re$ is called an ε common consensus if $\left| { \left| o ^ { \prime } - o _ { i } ^ { \prime } \right| } \right| \leq \varepsilon$ for all $i { = } 1 , . . . , n .$ . Then the ε consensus at minimum cost problem (εWCMC) seeks an $o ^ { * }$ such that the cost to reach this ε-consensus is minimal. As before, assume that the opinions are sorted and that $\| o ^ { \prime } - o _ { i } ^ { \prime } \| = | o ^ { \prime } - o _ { i } ^ { \prime } |$

For any $o ^ { \prime }$ , it is clearly a waste of money to change the opinion of an expert that is within ε of $\smash { o ^ { \prime } } .$ . Furthermore, any expert with initial opinion further than ε from $o ^ { \prime }$ should only be moved until that individual is exactly ε away from $o ^ { \prime }$ . These facts lead to the single criterion ε-consensus cost of any opinion $f _ { c _ { \varepsilon } } \ \left( o ^ { \prime } \right)$ Given an opinion $o ^ { \prime }$ , define $f _ { c _ { \varepsilon } } ( o ^ { \prime } ) { = } \textstyle \sum _ { \{ i : o _ { i { \ldots } 1 } < o ^ { \prime } { - } \varepsilon \} } w _ { i } c _ { i }$ $( o ^ { \prime } - \varepsilon - o _ { i , 1 } ) + \Sigma _ { \{ i : o _ { i , 1 } > o ^ { \prime } + \varepsilon \} } w _ { i } c _ { i } ( o _ { i , 1 } - ( o ^ { \prime } + \varepsilon ) )$ . Consequently, εWCMC seeks to obtain an opinion $o ^ { * } { \in } \Re$ such that $f _ { c _ { \mathrm { ~ e ~ } } } \left( o ^ { * } \right) { \leq } f _ { c \varepsilon } \left( o ^ { \prime } \right)$ for all ${ \boldsymbol { o } } ^ { \prime } \in { \mathfrak { R } }$

The following εWCMC algorithm is an extension to the WCMC algorithm presented above. Furthermore, this εWCMC algorithm assumes that the costs and weights are again linear and that the initial opinions are again ordered. Trivially, if $o _ { n , 1 } - o _ { 1 , 1 } \leq 2 \varepsilon$ , then $o ^ { * } { = } ( o _ { n , 1 } { + } o _ { 1 , 1 } ) / 2$ with a weighted cost of 0. So assume $o _ { n , 1 } - o _ { 1 , 1 } > 2 \varepsilon$

## 3.2.1. εWCMC Algorithm (εWCMCA)

Initialization: Set $L \gets \{ 1 \} , \ R \gets \{ n \} , \ l = 1 , \ r = n$ and $d i r { = } l e f t .$

Main step: While $| o _ { r , 1 } - o _ { l , 1 } | > 2 \varepsilon$

define $\scriptstyle c _ { L } ^ { \prime } = \sum _ { i \in L } w _ { i } c _ { i }$

define $\scriptstyle c _ { R } ^ { \prime } = \sum _ { i \in R } w _ { i } c _ { i } .$

If $c _ { L } ^ { \prime } \leq c _ { R } ^ { \prime } ,$ then $l {  } l { + } 1 , L {  } L { \cup } \{ l \}$ and $d i r \gets l e f t .$

Else, $r {  } r { - } 1 , R {  } R \cup \{ r \}$ and $d i r \gets r i g h t .$

Termination: $\operatorname { I f } d i r = l e f t ,$ , then $o ^ { * } = o _ { r , 1 } - \varepsilon$ is the optimal ε consensus opinion.

If not, $\jmath ^ { * } = o _ { l , 1 } + \varepsilon$ and is the optimal ε consensus opinion.

Calculate $f _ { c _ { s } } ( o ^ { * } )$ and report the corresponding optimal opinions of each expert, $o _ { i , 1 } ^ { \prime }$

Since $f _ { c _ { s } }$ is convex, the proof of correctness of this algorithm follows almost identically to the proof of correctness of WCMCA and is left to the reader. One should also observe that this algorithm can be implemented in linear time. The following example demonstrates the use of εWCMCA.

Example 2. Let the data be taken from Example 1 and let $\varepsilon = 0 . 8$ . Observe that the first 2 steps remain identical, and at the end of Step $2 \colon L = \{ 1 , 2 \} , R = \{ 4 , 5 \} , l = 2 , r = 4 ,$ $d i r { = } r i g h t$ and ${ | o _ { r , 1 } - o _ { l , 1 } | = 2 > 1 . 6 = 2 \varepsilon }$ . In Step 3 $c _ { L } ^ { \prime } =$ 18.0, ${ c _ { R } ^ { \prime } } { = } 9 . 0 $ , so R← {3,4,5}, r= 3, l = 2, dir= right and $\lvert o _ { r , 1 } - o _ { l , 1 } \rvert = 1 . 5 < 1 . 6$ . In the Termination step dir = right and so ${ o ^ { * } } = _ { O _ { l } } + \varepsilon = 1 . 0 + 0 . 8 = 1 . 8$ . Now the optimal opinions are 1.0, 1.0, 2.5, 2.6 and 2.6 for experts 1, 2, 3, 4 and 5, respectively. The total cost of $f _ { \mathrm { c . 8 } } ~ ( 1 . 8 ) ^ { = }$ $6 ^ { * } 0 . 5 + 4 ^ { * } 3 + 9 ^ { * } 0 . 4 = 1 8 . 6 ,$ a significant reduction in the weighted cost due to the wider tolerance of the consensus.

A natural variation on the εWCMC problem is to require every expert to be within ε of each other. That is, a consensus exists if and only if $\left| o _ { i } ^ { \prime } - o _ { j ^ { \prime } } \right| \leq \varepsilon$ for all $i , j { \in } \{ 1 , . . . , n \}$ . The solution to this problem can be easily obtained by running the εCMC algorithm with the ε in the algorithm set to ε/2.

## 4. Multiple criteria unconstrained cost weighted consensus problems

This section explores the minimum cost consensus of n experts using a multi-criteria decision problem, when experts have a linear opinion elasticity $c _ { i } ,$ and individual weight $w _ { i } .$ As before, this weight can be viewed as the degree of recognition of the expert and thus represents a resistance to changing this expert's opinion. With multiple dimensions two norms are no longer equivalent. Section 4.1 focuses on the 1-norm (rectilinear distance) and Section 4.2 examines the metric given as the square of the 2-norm (Euclidean distance squared). The ε multicriteria consensus problem is discussed in Section 4.3.

## 4.1. Rectilinear cost calculations

Measuring the distance between two opinions rectilinearly is a natural measurement. This measurement assumes that an agreement on each criterion can be negotiated independently. In other words, an expert can only be influenced one criterion at a time and this negotiation will not impact any of that expert's other opinions.

Since each criterion can be negotiated independently, each expert can have a distinct linear cost and weight for each criterion. That is, let $c _ { i , j } { \in } \mathfrak { R } ^ { + }$ denote the cost to move expert i one unit distance in the $j ^ { \mathrm { t h } }$ criterion and $w _ { i , j } { \in } { \mathfrak { R } } ^ { + }$ denote the weight of the ith expert given to criterion j for all $i { = } 1 , . . . , n$ and $\scriptstyle j = 1 , \ldots J .$

Returning to the family that is purchasing a van, the adults should have a high weight given to their opinions on the performance, handling and reliability of the vehicle and a lower weight to the features (such as DVD and video game capabilities) of the van. In contrast, the children should have a low weight given to their opinions of the performance, handling and reliability of the van, but a large weight on the features of the van.

In this case the minimum cost consensus problem seeks to find the $\boldsymbol { o } ^ { * } = ( o ^ { * } { } _ { 1 } , o _ { 2 } ^ { * } , \cdots , o _ { i } ^ { * } ) { \in } \Re ^ { J }$ that minimizes $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { J } c _ { i , j } w _ { i , j } \big | o _ { i , j } { - } \bar { o _ { j } ^ { * } } \big | } \end{array}$ . Due to the independence of the criteria, each criterion can be treated independently allowing the problem to be treated as a collection of J single criterion problems. That is, WCMCA can be run once for each criterion and the optimal opinion in the jth criterion is WMCA's solution on the $j ^ { \mathrm { t h } }$ criterion. In this case, the algorithm runs in O(nJ). As expected, the solution to this problem is the weighted cost median on each criterion as before.

Example 3. Below is a three-criteria decision problem with five experts that have the following initial opinions, costs and weights (Table 1).

As stated above, the problem is solved one criterion at a time. The optimal consensus occurs at $o ^ { * } { = } ( 2 . 5 , 2 . 0$ 2 2.0) representing the opinions $( e _ { 3 , 1 } , e _ { 3 , 2 } , e _ { 5 , 3 } )$ with a total weighted cost of $4 6 . 5 + 6 2 + 8 4 = 1 9 2 . 5$

## 4.2. Square distance cost calculations

In this section we analyze the situation when compromising along several criteria yields a straight line distance in terms of the cost. In other words, there is confounding cost effect when an expert compromises along several criteria—in this case, the cost is not purely additive. A justification for this case is that during a negotiation effort several criteria can be negotiated towards compromise at the same time. Thus, the metric used in this section is the 2-norm squared. In this case, the minimum cost consensus problem seeks to find an $o * = \left( o _ { 1 } * , o _ { 2 } * , \cdots , o _ { J } * \right) { \in } \Re ^ { J }$ that minimizes

$$
\sum_ {i = 1} ^ {n} c _ {i} w _ {i} \Big ((o _ {i, 1} - o _ {1} ^ {*}) ^ {2} + (o _ {i, 2} - o _ {2} ^ {*}) ^ {2} + \dots + (o _ {i, J} - o _ {J} ^ {*}) ^ {2} \Big).\tag{1}
$$

The reader should note that the cost of an expert $c _ { i }$ becomes uniform for all criteria since a diagonal distance calculated is not conducive to a different cost on each criterion.

One may question why not just use the Euclidean distance (2-norm). In n-dimensional space, even finding a point of minimum distance, known as a Fermat– Torricelli point, is not an easy problem. In addition, given a set of n points in a plane, Tóth [22] showed that there could exist more than 2n distinct points that all have the property that the sum of the distance to each of these points is the minimum distance. Thus, there may not exist a unique solution. Since consensus is a sufficiently vague concept, having several distinct optimal opinions should result in no consensus. Each expert can have his/her favorite optimal opinion (the optimal opinion that is the closest to his/her original opinion) and no expert could be convinced into moving away from this solution since the overall cost of the group will not diminish and this expert will be further away from his/her original opinion.

Table 1  
Data for Example 3

<table><tr><td rowspan="2">Expert</td><td colspan="3">Criterion 1</td><td colspan="3">Criterion 2</td><td colspan="3">Criterion 3</td></tr><tr><td>Opinion</td><td>Cost</td><td>Weight</td><td>Opinion</td><td>Cost</td><td>Weight</td><td>Opinion</td><td>Cost</td><td>Weight</td></tr><tr><td> $E_1$ </td><td>0.5</td><td>1.0</td><td>6.0</td><td>8.0</td><td>2.0</td><td>3.0</td><td>4.0</td><td>4.0</td><td>2.0</td></tr><tr><td> $E_2$ </td><td>1.0</td><td>4.0</td><td>3.0</td><td>1.0</td><td>4.0</td><td>1.0</td><td>6.0</td><td>1.0</td><td>2.0</td></tr><tr><td> $E_3$ </td><td>2.5</td><td>3.0</td><td>4.0</td><td>2.0</td><td>3.0</td><td>5.0</td><td>5.0</td><td>4.0</td><td>4.0</td></tr><tr><td> $E_4$ </td><td>3.0</td><td>5.0</td><td>1.0</td><td>6.0</td><td>1.0</td><td>3.0</td><td>1.0</td><td>2.0</td><td>6.0</td></tr><tr><td> $E_5$ </td><td>6.0</td><td>2.0</td><td>2.0</td><td>4.0</td><td>2.5</td><td>2.0</td><td>2.0</td><td>5.0</td><td>4.0</td></tr></table>

Fortunately, if this Euclidean distance is squared, then there exists a unique optimal solution. This optimal point can be obtained by taking the partial derivatives of (1) and setting them equal to 0. Solving this system of equations leads to the optimal opinion $o ^ { * } { = } ( o _ { 1 } ^ { * } , o _ { 1 } ^ { * } { , . . . , o _ { } ^ { * } } )$ where

$$
o _ {j} ^ {*} = \frac {\sum_ {i = 1} ^ {n} c _ {i} w _ {i} o _ {i , j}}{\sum_ {i = 1} ^ {n} c _ {i} w _ {i}}\tag{2}
$$

for al $\scriptstyle j = 1 , \ldots , J .$ Since Eq. (1) is convex and continuously differentiable, $o ^ { * }$ is the optimal solution.

This solution shows that the optimal consensus point is the weighted cost average of the experts' opinions in each criterion—a surprising deviation from the median. The following example demonstrates this method.

Example 4. Consider the following data that are similar to the data in Example 3, but now each expert only has a single cost and weight (Table 2).

Applying Eq. (2) results in an optimal consensus at $o ^ { * } { = } ( 2 . 1 5 , \ 3 . 3 3 , \ 4 . 3 3 )$ . The total cost is 467.9. As expected, this opinion differs from both the optimal opinion in Example 3 and the opinion for the å common consensus problem with the 1-norm.

## 4.3. Multi-dimensional ε common consensus

Experts being sufficiently close to a consensus in multiple criteria can have various reasonable definitions. The most obvious definition is that each expert must be within ε units of the optimal consensus where units are measured in some norm. Two other practical definitions of a multi-criteria ε common consensus exist. One restricts each expert to be within some $\varepsilon _ { j }$ in the j criterion. The other seeks to optimally allocate an ε tolerance among the J criteria.

Table 2  
Data for Example 4

<table><tr><td rowspan="2">Expert</td><td rowspan="2">Cost</td><td rowspan="2">Weight</td><td colspan="3">Opinions</td></tr><tr><td>Criterion 1</td><td>Criterion 2</td><td>Criterion 3</td></tr><tr><td> $E_1$ </td><td>1.0</td><td>6.0</td><td>0.5</td><td>8.0</td><td>4.0</td></tr><tr><td> $E_2$ </td><td>4.0</td><td>3.0</td><td>1.0</td><td>1.0</td><td>6.0</td></tr><tr><td> $E_3$ </td><td>3.0</td><td>4.0</td><td>2.5</td><td>2.0</td><td>5.0</td></tr><tr><td> $E_4$ </td><td>5.0</td><td>1.0</td><td>3.0</td><td>6.0</td><td>1.0</td></tr><tr><td> $E_5$ </td><td>2.0</td><td>2.0</td><td>6.0</td><td>4.0</td><td>2.0</td></tr></table>

## 4.3.1. Uniform ε for each criterion (∞-norm)

The simplest case of the ε common consensus problem occurs when the metric is the ∞-norm and every expert must be within ε of the optimal opinion. Since the ∞-norm is the maximum difference in any single criterion between the $o ^ { * }$ and $o _ { i } ^ { \prime } ,$ it suffices to have each expert within ε of each individual optimal opinion. In practice, this occurs if each expert can differ by no more than ε from each optimal opinion (on each criterion). Applying εWCMCA to each individual criterion will provide the optimal consensus. The total running time of the algorithm would be $O ( n J )$ . If ε = 0.8 and the data are taken from Example 3, then the optimal opinion is $O ^ { * } = ( 1 . 8 , 2 . 8 , 2 . 8 )$ with a total cost of 18.6 + $4 4 . 5 + 4 2 . 4 = 1 0 5 . 5$

## 4.3.2. Allocated consensus tolerance $\varepsilon _ { j }$ for each criterion

Another natural case to consider occurs when the level of consensus does not have to be the same on each criterion. In other words, there may exist an $\varepsilon _ { j } \in \Re ^ { + }$ for each $\scriptstyle j = 1 , \ldots J .$ Returning to the van example, the consensus on cost would probably have a smaller ε than the features consensus. As in the ∞-norm, this problem can be solved by applying $\varepsilon _ { j } \mathrm { W C M C A }$ to each criterion individually.

## 4.3.3. Allocating a tolerance among J criteria

In this case the group facilitator allows a total tolerance $\varepsilon _ { T }$ to be allocated to the J criteria. In other words, the facilitator is seeking a tolerance $\varepsilon _ { j }$ for each criterion that minimizes the total consensus cost and has $\scriptstyle \sum _ { j = 1 } { } _ { \mathrm { t o } } J \varepsilon _ { j } = \varepsilon _ { T } .$ Thus, the facilitator is seeking a range of acceptable opinions in each criterion.

The algorithm to solve this problem follows the same spirit of the εWCMCA. The idea is to successively add on the smallest costs until the tolerance is sufficiently close. An equivalent methodology takes the solution from WCMCA and retraces the steps according to the highest cost. In this case, the algorithm must evaluate the cost of moves in all J axes. For brevity, a formal description of the algorithm is not presented here, but the following example provides enough information so that the reader can reproduce the algorithm.

Example 5. This example uses the data from Example 4 with criteria $c _ { 1 }$ and $c _ { 2 }$ only (2-dimensional problem) and $\varepsilon _ { T } { = } 4 . 0$ . The following figure presents the opinions of the five experts with the optimal solution (region) inside of the box (Fig. 2).

The experts' movements proceed as shown in Table 3:

The highest cost move (i.e. move 8) consists of a move of 1.5 units of distance, from (2.5,2.0) to (1.0,2.0). Backing up this distance allows a range of [1.0,2.5] in criterion 1. There is still 4.0 − 1.5 = 2.5 units of distance left and so backing up the 7th move, results in a range of [2,4] in criterion 2. There still remains 0.5 left. So the final step is to back up move 6 by 0.5, which has a range of [1.5,4.0] in criterion 2. Thus, the optimal region is given as ([1.0,2.5], [1.5,4.0]). Consequently, the final opinions of the five experts will be $o ^ { * } { } _ { 1 } = ( 1 . 0 , 4 . 0 ) , o ^ { * } { } _ { 2 } =$ (1.0,1.5), $o ^ { * } { } _ { 3 } = ( 2 . 5 , 2 . 0 )$ $o ^ { * } { } _ { 4 } = ( 2 . 5 , 4 . 0 )$ and $o ^ { * } { } _ { 5 } =$ (2.5,4.0) with a total cost of 59.5.

Interestingly, this algorithm allocates the “consensus tolerance” to the various criteria based on the cost of reaching a consensus at that point. Thus, in general, the optimal region is not symmetrical.

## 4.3.4. All experts within ε of the optimal consensus (1-norm)

Solving for ε common consensus with the 1-norm is different from the problem discussed in Section 4.3.3, since the tolerance is not freely allocated between the criteria. In the above case, the mediator decides the tolerance allowed in each criterion and each expert must move until he or she has met this tolerance in each criterion. In the 1-norm case all experts have to be within a distance of ε from the optimal consensus point (sum of distances on all criteria), allowing each expert to determine their optimal opinion.

An individual may naively take the center of optimal region produced in Section 4.3.3 to be the optimal opinion for ε common consensus in the 1-norm case. In

![](/api/attachments/GPQ4AJMR/fulltext/images/cd75cd08a6720951ffdda44e8ef9f75e504ec84b317301aaea2057db270fde54.jpg)  
Fig. 2. Opinions and optimal region for Example 5.

Table 3  
Experts' opinion movements for Example 5

<table><tr><td>Step</td><td>Move</td><td>Weighted Cost</td><td>Next Cost</td></tr><tr><td>1</td><td> $o_{5,1} \rightarrow o_{4,1} = 1.0$ </td><td>4</td><td>9</td></tr><tr><td>2</td><td> $o_{1,2} \rightarrow o_{4,2} = 1.0$ </td><td>6</td><td>11</td></tr><tr><td>3</td><td> $O_{1,1} \rightarrow o_{2,1}$ </td><td>6</td><td>18</td></tr><tr><td>4</td><td> $\{o_{5,1}, o_{4,1}\} \rightarrow o_{3,1}$ </td><td>9</td><td>21</td></tr><tr><td>5</td><td> $\{o_{1,2}, o_{4,2}\} \rightarrow o_{5,2}$ </td><td>11</td><td>15</td></tr><tr><td>6</td><td> $O_{2,2} \rightarrow o_{3,2}$ </td><td>12</td><td>24</td></tr><tr><td>7</td><td> $\{o_{1,2}, o_{4,2}, o_{5,2}\} \rightarrow o_{3,2}$ </td><td>15</td><td>*</td></tr><tr><td>8</td><td> $\{o_{1,1}, o_{2,1}\} \rightarrow o_{3,1}$ </td><td>18</td><td>*</td></tr></table>

Note: the asterisk (<sup>⁎</sup>) symbol represents the final move with the optimal WCMCA solution in a single criterion. To extend the algorithm to the ε<sub>j</sub>WCMCA the most recent moves are undone.

Example 5 with ε = 2.0 (1/2 of the total ε allocated) the center of the optimal region is (1.75,2.75). The experts' opinions for the 1-norm would be $o _ { 1 } ^ { \prime } = ( 1 . 0 , 4 . 0 ) , o _ { 2 } ^ { \prime } =$ (1.0,1.5), o′ = (2.5,2.0), o′ = (2.5,4.0) and $o _ { 5 } ^ { \prime } { = } ( 2 . 5 , 4 . 0 )$ with a total cost of 59.5 (the same solution).

However, if the mediator decides the opinion should be (1.5,3.0), then the experts' opinions would be ${ o _ { 1 } } ^ { \prime \prime } =$ (0.5,4), ${ o _ { 2 } } ^ { \prime \prime } { = } ( 1 . 0 , 1 . 5 )$ , ${ o _ { 3 } } ^ { \prime \prime } \mathrm { = } ( 2 . 5 , 2 . 0 )$ , ${ o _ { 4 } } ^ { \prime \prime } \mathrm { = } ( 2 . 5 , 4 . 0 )$ and $o _ { 5 } { } ^ { \prime \prime } { = } ( 2 . 5 , 4 . 0 )$ with a total cost of 56.5. Thus, the center of the region produced by the above algorithm will not yield an optimal solution for the 1-norm case. The multi-criteria ε common consensus problem with the 1-norm remains an important future research topic.

## 5. Conclusion and future research

Group decision making, an important area in numerous applications, implements the pivotal concept of consensus. Consensus, which signifies the point at which the individual opinions turn into the group opinion, does not carry a universally accepted definition and is applied differently in varying contexts.

This paper provides two different definitions of consensus in the uni-criterion decision domain and shows how to reach such a consensus at a minimum cost. More specifically, these models assume linear opinion elasticity (cost of opinion shift or degree of stubbornness). The paper presents linear-time algorithms to find the consensus when all experts have to adopt the same opinion, and also when the experts are allowed to be within a given interval from the consensus point.

In addition, the paper presents several models for consensus on a multi-criteria problem. The first model assumes rectilinear cost function allowing separate negotiations on each criterion. The second model allows the experts to negotiate several criteria at the same time using the squared distance cost function. The rectilinear case provides a minimum cost consensus at the point of weighted median, while the squared distance cost provides an optimal consensus at the weighted mean opinion. Some additional results are presented for the multi-criteria å common consensus problem.

Future research in this area involves finding the minimum cost consensus of a single criterion decision problem while considering non-linear opinion elasticity with and without a budget constraint. In addition, creating an algorithm to find the optimal å common consensus for the 1-norm and 2-norm squared case remains an important research topic.

## References

[1] G. Bordogna, M. Fedrizzi, G. Pasi, A linguistic modeling of consensus in group decision making based on OWA operators, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 27 (1997) 31–49.

[2] N. Bryson, Group decision-making and the analytic hierarchy process: exploring the consensus-relevant information content, Computers & Operations Research 23 (1996) 27–35.

[3] M.A.P. Davies, A multicriteria decision model application for managing group decisions, The Journal of the Operational Research Society 45 (1) (1994) 47–58.

[4] J. Einhorn, Expert judgment: some necessary conditions and an example, Journal of Applied Psychology 59 (1974) 562–571.

[5] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, Rational consensus model in group decision making using linguistic assessments, Fuzzy Sets and Systems 88 (1) (1997) 31–49.

[6] E. Herrera-Viedma, F. Herrera, F. Chiclana, A consensus model for multiperson decision making with different preference structures, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 32 (3) (2002) 394–402.

[7] H.M. Hsu, C.T. Chen, Aggregation of fuzzy opinions under group decision making, Fuzzy Sets and Systems 79 (1996) 279–285.

[8] C.L. Hwang, M.-J. Lin, Group Decision Making Under Multiple Criteria, Lecture Notes in Economics and Mathematical Systems, vol. 281, Springer-Verlag, Berlin/Heidelberg, 1987.

[9] A. Ishikawa, The new fuzzy Delphi methods: economization of GDS (group decision support), Proceeding of the Twenty-Sixth Hawaii International Conference on System Sciences, vol. 4, 1993, pp. 255–264.

[10] J. Kacprzyk, M. Fedrizzi, A soft measure of consensus in the setting of partial (fuzzy) preferences, European Journal of Operational Research 343 (3) (1988) 316–325.

[11] J. Kacprzyk, M. Fedrizzi, H. Nurmi, Group decision making and consensus under fuzzy preferences and fuzzy majority, Fuzzy Sets and Systems 49 (1992) 21–31.

[12] J. Kacprzyk, H. Nurmi, M. Fedrizzi (Eds.), Consensus Under Fuzziness, Kluwer Academic Publishers, Boston, 1997.

[13] H.-S. Lee, Optimal consensus of fuzzy opinions under group decision making environment, Fuzzy Sets and Systems 132 (3) (2002) 303–315.

[14] H.A. Linstone, M. Turoff (Eds.), The Delphi Method; Techniques and Applications, Addison Wesley, 1975.

[15] R.F. Love, J.G. Morris, G. Wesolowsky, Facilities Location Models and Methods, North-Holland, 1988.

[16] J. Montero, Rational aggregation rules, Fuzzy Sets and Systems 62 (1994) 267–276.

[17] J. Ness, C. Hoffman, Putting Sense Into Consensus: Solving the Puzzle of Making Team Decisions, VISTA Associates, Tacoma, Wash., 1998.

[18] K.-C. Ng, B. Abramson, Consensus diagnosis: a simulation study, IEEE Transactions on Systems, Man and Cybernetics 22 (5) (1992) 916–928.

[19] W.L. Perry, J. Moffat, Measuring consensus in decision making: an application to maritime command and control, Journal of the Operational Research Society 48 (4) (1997) 383–390.

[20] J. Shanteau, What does it mean when experts disagree? in: G. Klein, E. Salas (Eds.), Naturalistic Decision Making, Lawrence Erlbaum Associates, Hillsdale, NJ, 2001.

[21] J. Shanteau, D. Weiss, R.R. Thomas, J.C. Pounds, Performance based assessment of expertise: how to decide if someone is an expert or not, European Journal of Operational Research 136 (2002) 253–263.

[22] G. Tóth, The shortest distance among points in general position, Computational Geometry, Theory and Applications 8 (1997) 33–38.

Dr. DAVID BEN-ARIEH is a Professor of Industrial Engineering at Kansas State University. Prior to joining Kansas State University, Dr. Ben-Arieh taught at the Department of Industrial Engineering and Management, Ben-Gurion University in Beer Sheva, Israel. He also served as the head of the Paul Ivanier Center for Robotics and Production Management in that institute.

His industrial experience includes working for AT&T Bell Laboratories, and being a consultant for aerospace industry and health care organizations. Dr. Ben-Arieh has also received fellowship appointments with the Boeing Company and NASA.

Dr. Ben-Arieh concentrates mainly on applications of Decision Theory, and Artificial Intelligence applications in manufacturing, and holds one patent in this area.

Dr. Ben-Arieh received a B.S. and M.S. in Industrial Engineering from Ben-Gurion University, and a Ph.D. from Purdue University in the same area.

Dr. TODD EASTON is an Assistant Professor of Industrial and Manufacturing Systems Engineering at Kansas State University. Prior to this position, Dr. Easton has a post-doctoral and instructor position in the Industrial and Systems Engineering Department at Georgia Institute of Technology.

Dr. Easton received his B.S. in Mathematics from Brigham Young University, his M.S. in Operations Research from Stanford University and his Ph.D. in Industrial and Systems Engineering from Georgia Institute of Technology.

Dr. Easton researches combinatorial optimization with an emphasis in integer programming, graph theory and algorithmic development.
