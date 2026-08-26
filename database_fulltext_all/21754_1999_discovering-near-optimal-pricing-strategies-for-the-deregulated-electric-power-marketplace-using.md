---
otero_id: 21754
otero_key: "5Z8XYEJ5"
title: "Discovering near-optimal pricing strategies for the deregulated electric power marketplace using genetic algorithms"
authors: "D.J. Wu"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00035-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Discovering near-optimal pricing strategies for the deregulated electric power marketplace using genetic algorithms

D.J. Wu )

The Wharton School, UniÕersity of PennsylÕania, Philadelphia, PA 19104, USA Bennett LeBow College of Business, Drexel UniÕersity, Philadelphia, PA 19104, USA

## Abstract

A new approach based on genetic algorithms has been used to a general class of problems arising in network industries, in particular, to the first-best pricing problems for the electric power sector. The fundamental challenge in these applications is the treatment of various network constraints. Building on the work of Michalewicz, this study extends the state of the art of constraint-handling techniques to a realistic network problem. The computational approach studied here can be extended to other constraint-rich problems. q 1999 Elsevier Science B.V. All rights reserved

Keywords: Genetic algorithms; Electric power networks; Pricing strategies; Network industries; Constrained optimization

## 1. Introduction

Network industries have technologies characterized by a spatial hierarchy, the ‘‘network’’, with capital intensive interconnections and time dependent, capacity-limited flows of products and services through the network to customers. Typical network industries include: airlines, electricity, financial services, gas, information networks e.g., the Internet , Ž . telecommunications, transportation, postal services and water. In addition, nearly every non-local industry has some of the characteristics of a network industry.

The significance of providing decision support with respect to pricing, investment and operating strategies to network industries is well known in the literature and in industry for the following reasons <sup>w</sup> <sup>x</sup> 44 :

Ž . 1 Network industries are capital intensive and problems of capacity planning and scheduling of facilities are therefore central to successful operations.

Ž . 2 Capital intensity gives rise to fundamental interest in demand management, including pricing strategies, to align capacity cost and utilization with customer value; in particular, network industries provide a good opportunity for deepening our understanding of the marketing<sup>r</sup>manufacturing interface and of the value of information sharing in the supply chain.

Ž . 3 Capital intensity and price-quantity volatility give rise to problems of risk hedging and associated financial instruments futures, options, forwards Ž . which, coupled with 1 and 2 above, present inter- Ž . Ž . esting new problems in coordinating finance and operations.

Ž . 4 Added to the above problems, network industries are frequently regulated, and, consequently, changes in pricing and investment policies need to be carefully legitimated.

Ž . 5 Finally, service performance and quality have become central issues in the new customer-focused approach that is driving change in network industries as they become more competitive.

Because of their importance, network industries have generated significant interest in the literature. However, even ‘‘easy’’ network problems are usually NP-hard, without incorporating the complexities noted above on financial and marketing interface issues. Perhaps for this reason only selected features of network operations problems, such as capacity planning and utilization and optimal network flows, have been studied to date. The goal of this study is to advance this state of the art by considering the application of genetic algorithms 23 to problems of<sup>w</sup> <sup>x</sup> investment planning, network flows and pricing simultaneously. We will do so with a primary focus on electric power, but with methods that have promise for other network problems as well.

The rest of this paper is organized as follows. Section 2 provides a literature review. Section 3 models the first-best pricing problem for the electric power network. Section 4 sets up the design of a genetic algorithms experiment. Section 5 describes the experimental performance of genetic algorithms and provides some perspective on related literature. The paper concludes with a summary in Section 6.

Note: Throughout this paper, the reader is assumed basic familiarity with genetic algorithms 23 .<sup>w</sup> <sup>x</sup>

## 2. Literature review

This section first briefly reviews some recent studies of network pricing and investment that serve as background for this research. It then reviews a new evolutionary approach, based on genetic algorithms, for solving network problems.

## 2.1. Network pricing and inÕestment

The following are representative studies in the indicated industries: airlines 2,4 , electric power 5–<sup>w x</sup> <sup>w</sup> 7,22,27,28,44 , gas 41 , financial services 1 , postal <sup>x</sup> <sup>w</sup> <sup>x</sup> <sup>w x</sup> and delivery services 9–11 , telecommunications and<sup>w</sup> <sup>x</sup> pricing the Internet 16,30,31,38 , and transportation <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 19,20,29 .

The above-noted studies provide key insights on the structure of optimal pricing and investment rules. These include such well-recognized principles as marginal-cost pricing for public enterprises andŽ . value-based possibly regulated pricing for profit- Ž . Ž maximizing firms . On the investment side, the struc-. ture of optimal rules typically involves tradeoffs between multi-year capital recovery payments and the short-term increases in productivity that are leveraged by capital investments. In addition to these structural insights, a key decision operations managers have to make is how the system should be operated to achieve minimum cost, customer value and other measurable objectives. There is also significant literature on network industries devoted to these operational issues, including the electric power industry.

This paper takes a multi-disciplinary approach, which builds on general theoretical literature, as well as on models of implementable operations strategies for the topics treated. In particular, this research seeks to provide both general insights on pricing and investment, as well as approaches that can be used to support actual decision making on pricing and investment. The key approach pursued here is the use of emerging information technologies, such as genetic algorithms, to provide a means for evaluating pricing and investment policies for complex networks, which would not be accessible to traditional analytic methods. However, this paper focuses on using GA to explore pricing strategies. The computation of network investment strategies as well as how to design genetic algorithms that can handle highly non-linear constraints have been addressed elsewhere <sup>w</sup> <sup>x</sup> 44 .

2.2. Genetic algorithms for solÕing network problems

Let me begin with a story on evaluating the effectiveness of a popular commercial GA package. In a Wharton operations class, a group of MBAs, as well as the TA a doctoral student , were invited toŽ . test the effectiveness of this GA software. The vendor claimed that the package could efficiently solve a class of network problems in the manufacturing and service area, such as scheduling and the traveling salesman problem. To get a feel for the software, the group started with a baby problem, which was to maximize $x ^ { 2 }$ , with a simple constraint, $x \in [ - 1 , 1 ] .$ Surprisingly, the software could not even return a feasible solution after many trials. The group reported the findings to the professor, who then called the vendor. The manager of the vendor then requested that a group of software engineers fix the problem; the group failed. Finally, the manager blamed the problem on the ‘‘educational version’ that the students were using. What the manager did not know was that his GA package suffered from a very difficult ‘‘constraint-handling’’ problem. Not surprisingly, further tests showed that the package could not consistently find a feasible solution for several of the problems the vendor claimed the package was able to solve to ‘‘optimality’’, regardless of its versions, educational or professional Paul Klein-Ž dorfer, private communication ..

How to handle constraints has been an active area of research in both the AI literature 8,17,36,37 as<sup>w</sup> <sup>x</sup> well as in the OR literature 33 . The key difference<sup>w</sup> <sup>x</sup> between the two is that the later focuses on constrained optimization not just satisfying all the constraints, while the former AI track traditionallyŽ . focuses on constraint conflict resolution but pays little attention to efficiency or optimality. This paper follows the OR track, and studies network constrained optimization using genetic algorithms. Generally speaking, there is no single preferred solution for constrained optimization in the literature, especially when constraints are non-linear. Adding to the difficulty of constraint-handling in genetic algorithms is the fact that the success of GA depends on some tolerance of inferior or infeasible candidates during the process of searching. How to use this infeasible information to guide efficient search is not found in the literature. In spite of their theoretical and practical significance, constraint-handling techniques in genetic algorithms have largely been ignored in the GA research community until some recent experimental work pioneered by Michalewicz <sup>w</sup> <sup>x</sup> 33 .

There are two major constraint-handling mechanisms in the literature: penalty function methods and specialized genetic operators. The penalty function methods are widely used in the mathematical programming literature. Such methods essentially add to the objective function some terms which punish a solution that is not feasible. The terms are generally penalized in increasing, convex form with departures from feasibility. Three types of penalty function methods were recently introduced into the design of GA: static penalty functions 24,32 , dynamic penalty <sup>w</sup> <sup>x</sup> functions 26 and death penalty functions 33 . Spe-<sup>w x</sup> <sup>w x</sup> cialized genetic operators are domain-specific, i.e., it is usually difficult to generalize their performance. Among various specialized genetic operators, the most popular ones are: arithmetic crossover 12, 13,40 , non-uniform mutation 33,35 , and the repair<sup>x</sup> <sup>w x</sup> method 34 . In this paper, we study arithmetic<sup>w</sup> <sup>x</sup> crossover and non-uniform mutation, which are defined in Section 5.3. The special property of arithmetic crossover is that it always guarantees the feasibility of its offspring in convex problems. Nonuniform mutation, unlike the traditional uniform mutation that GA uses, does not search uniformly at later stages; it searches very locally instead. A repair method repairs any infeasible solution in the current population of GA with a feasible solution in the search space which returns the same evaluation function value as the repaired infeasible solution. For an excellent full review of constraint-handling techniques in genetic algorithms, the reader is referred to Ref. 33 .<sup>w</sup> <sup>x</sup>

This research intends to extend the experiments by Michalewicz and others on simple but tractable mathematical functions to a complicated system that has rich economical and practical implications. Along the same line, genetic algorithms has been used to play strategic games in an evolving electric power market 27 ; to find trading rules in financial markets<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 1 ; and to discover network investment strategies and to incorporate non-linear constraints 44 . Further, a framework has been proposed for testing the applicability of such methods as a basis for electronic bidding and contracting 28,45 . The scope of<sup>w</sup> <sup>x</sup> this paper is limited to the exploration of using genetic algorithms for discovering pricing strategies for large-scale deregulated electric power networks, which serves as a foundation for the above-mentioned ‘‘lines of research’’.

Section 3 applies the theoretical framework on first-best pricing, investment and operating problems for general network industries developed in Ref. 44<sup>w</sup> <sup>x</sup> to electric power networks, with a focus on the first-best pricing problem.

## 3. First-best solutions for electric power networks

Among various ‘‘blue prints’’ of electric power industry deregulation, perhaps the most important one is the ‘‘PoolCo’’ proposal. Under this proposal, all generators inject power into a central power ‘‘Pool’’ from which all customers extract power. All customers pay the PoolCo for the energy consumed, and the PoolCo in turn pays the generators for the power they provide. The research interest here is, under the scenario of various proposals such as the PoolCo, how to discover pricing strategies for each supplier. What is the optimal consumption amount for each consumer?

The operation of this PoolCo can be modeled as a first-best welfare maximization problem. We begin with some necessary notations.

Let: <sub>N</sub> be the network structure under consideration; N be the number of nodes or buses a bus is aŽ node in the electric power network where electric power is injected or extracted in the electric power. network $\mathcal { N }$ with a fixed frequency e.g., 60 Hz ;Ž . $\mathcal { G } = \left\{ 1 , 2 , \dots , N \right\}$ be the set of power generators $( \zeta \in$ $\mathcal { G } )$ , assume $\mathcal { G } _ { i }$ the subset of all generators at node $i ;$ $\mathcal { D } = \{ 1 , 2 , \ldots , N \}$ be the set of consumers or distribution companies $( \eta \in \mathcal { D } )$ , assume $\mathcal { D } _ { i }$ the subset of all consumers at node $i ; F$ be the total fixed cost for the power transmission network;

$$
X \stackrel {\text { def }} {=} \left\{x (\eta) | x (\eta) \geq 0, \quad \eta \in \mathscr {D} \right\}
$$

be the demand vector;

$$
Q \stackrel {\mathrm{def}} {=} \left\{q (\zeta) | q (\zeta) \geq 0, \quad \zeta \in \mathcal {G} \right\}
$$

be the supply vector; $C _ { \mathrm { g } } ( q ( \zeta ) ; \zeta )$ be supplier $\zeta ^ { \bullet } \mathbf { s }$ cost for producing $q ( \zeta )$ amount of electric power; $V ( x ( \eta ) ; \eta )$ be consumer $\eta ^ { \star } \mathbf { s }$ willingness-to-pay by consuming $x ( \eta )$ amount of electric power.

We follow the standard formulation and notation for electric power flows $\left( \mathrm { e . g . } \right.$ , Refs. 7,15 . The<sup>w</sup> <sup>x</sup>. alternating voltage at node i is represented by a sinusoidal wave form with amplitude $V _ { i }$ and voltage angle $\theta _ { i }$ . We denote by $r _ { i k } + \mathbf { j } x _ { i k }$ the impedance for the circuit connecting node i and node $k ,$ where $\mathbf { j } = { \sqrt { - 1 } }$ . Without loss of generality, we assume $\theta _ { N } = 0$ , where vector $\pmb { \Theta } = ( \theta _ { 1 } , \ldots , \theta _ { N } )$ represents the vector of voltage angles.

Denote $\varPsi _ { i j } ( \theta _ { i } - \theta _ { j } )$ as the real power flow from bus i to bus $j$ on line $i j ,$ which is given by the non-linear function below 15 :<sup>w</sup> <sup>x</sup>

$$
\begin{array}{c} \Psi_ {i j} \big (\theta_ {i} - \theta_ {j} \big) = G _ {i j} V _ {i} ^ {2} - G _ {i j} V _ {i} V _ {j} \cos \big (\theta_ {i} - \theta_ {j} \big) \\ + Y _ {i j} V _ {i} V _ {j} \sin \big (\theta_ {i} - \theta_ {j} \big), \end{array}
$$

where

$$
Y _ {i j} \stackrel {\mathrm{def}} {=} \frac {x _ {i j}}{r _ {i j} ^ {2} + x _ {i j} ^ {2}},\tag{1}
$$

and

$$
G _ {i j} \stackrel {\text { def }} {=} \frac {r _ {i j}}{r _ {i j} ^ {2} + x _ {i j} ^ {2}}.
$$

There is a transmission capacity limit, the maximum power flow on line $( i , j )$ , denoted by ${ \overline { { P } } } _ { i j } ,$ which is determined by the thermal and line stability limits on the power flow through the line 25 . <sup>w</sup> <sup>x</sup>

While the focus of the following analysis is a static model of real power flows, the model has been generalized to include reactive power flows elsewhere 44 . It can also be generalized to include<sup>w</sup> <sup>x</sup> demand and supply uncertainty 7 . For a discussion <sup>w</sup> <sup>x</sup> of related work in the DSS area, see Ref. 14 .<sup>w</sup> <sup>x</sup>

## 3.1. The model

The fixed capacity first-best problem for electric power networks can now be stated as: First-best problem FBPŽ .

$$
\max _ {\mathbf {X}, \mathbf {Q}, \boldsymbol {\Theta}} \left[ \sum_ {\eta \in \mathscr {D}} V (x (\eta); \eta) - \sum_ {\zeta \in \mathscr {G}} C _ {\mathrm{g}} (q (\zeta); \zeta) - F \right],\tag{2}
$$

s.t.

$$
\sum_ {\zeta \in \mathcal {G} _ {i}} q (\zeta) - \sum_ {\eta \in \mathcal {D} _ {i}} x (\eta) = \sum_ {j = 1} ^ {N} \Psi_ {i j} \left(\theta_ {i} - \theta_ {j}\right)
$$

$$
i = 1, \ldots , N,\tag{3}
$$

$$
\Psi_ {i j} \big (\theta_ {i} - \theta_ {j} \big) \leq \overline {{P}} _ {i j} \text { for } 1 \leq i, j \leq N.\tag{4}
$$

The objective function 2 is the social welfare forŽ . the given network. The first term is consumers’ willingness-to-pay, the second term is power generators’ costs, and the last term is the fixed investment cost for the transmission network.

Note: Our model is original in the sense that 1 itŽ . is a direct application of the first-best modeling framework for general network industries in Ref. <sup>w</sup> <sup>x</sup> 44 and 2 it differs slightly from that of Chao andŽ . Peck 7 in that we explicitly characterize con- <sup>w</sup> <sup>x</sup> sumers’ willingness to pay.

Due to the network flow constraints as specified in Eq. 3 , and the non-linearity of the Ž . $\varPsi ( \cdot )$ function as in Eq. 1 , this problem is NP-Hard and in- Ž . tractable using the traditional analytic methods. Before we construct genetic algorithms to compute the optimal solution, we provide some theoretical analysis of the problem to guide the GA approach, such as the existence of an optimal solution in this problem, the structure of optimal pricing rules, and model simplification.

Theorem 1 Existence of optimal solution( ): ${ \mathrm { A s } } -$ sume that all willingness-to-pay and cost functions are continuous and that $\overline { { P } } _ { i j } \in ( 0 , \infty )$ , ; i, j. Then, there exists an optimal solution to the first-best model.

Sketch of proof of Theorem 1 is found in Appendix A.

Let $P ( q ( i ) ; i )$ , and $\mu _ { i j } \geq 0$ be the associated shadow prices associated with constraints 3 – 4 . Ž . Ž . Using the standard Kuhn–Tucker conditions, we can derive the following necessary conditions for maximizing social welfare:

$$
V ^ {\prime} (x (\eta); \eta) = C _ {\mathrm{g}} ^ {\prime} (q (\zeta); \zeta) = P (q (i); i),\tag{5}
$$

$$
\begin{array}{l} V (x (\eta), \eta) = C _ {g} (q (\zeta), \zeta) = P (q (i), i), \\ \sum_ {j = 1} ^ {N} \left[ \left(P (q (i); i) + \mu_ {i j}\right) \Psi_ {i j} ^ {\prime} (\theta_ {i} - \theta_ {j}) \right. \\ \left. - \left(\left(P (q (j); j) + \mu_ {j i}\right) \Psi_ {j i} ^ {\prime} (\theta_ {j} - \theta_ {i})\right) \right] = 0 \\ i = 1, 2, \dots , N, \\ \mu_ {i j} \left[ \Psi_ {i j} (\theta_ {i} - \theta_ {j}) - \overline {{P}} _ {i j} \right] = 0, \quad \text { for } \quad 1 \leq i, \quad j \leq N. \end{array}
$$

Since Eqs. 2 – 4 is the starting point for much Ž . Ž . of what follows, let us consider the first-order conditions above in more detail. First, Eq. 5 is theŽ . standard first-order condition for pricing at node $i ;$ it specifies that price should be set to equate marginal cost and marginal benefits note that there is no Ž capacity expansion problem involved here, so only short-run marginal costs are of interest . The com- . plexity in solving Eqs. 2 – 4 arises from the formŽ . Ž . of transmission constraints and power flow equations. As shown in Eq. 1 , these are quite non-lin- Ž . ear, and the optimal solution to the FBP is therefore likely to be complicated. The literature has approached this problem by approximating the flow Eq. 1 via a so-calledŽ . DC approximation model

which amounts to assuming that the phase angle difference at each node i Žviz. $\theta _ { i } - \theta _ { j } )$ is small and that voltages $V _ { i }$ are all close to their normalized values assumeŽ $V _ { i } = V _ { j } = 1$ .  for simplicity . These assumptions, which are reasonable for many practical networks, give rise to the following approximation for $\psi _ { i j } ( \cdot )$ Ž . in Eq. 1 :

$$
\begin{array}{c} \Psi_ {i j} \big (\theta_ {i} - \theta_ {j} \big) = G _ {i j} - G _ {i j} \cos \big (\theta_ {i} - \theta_ {j} \big) \\ + Y _ {i j} \sin \big (\theta_ {i} - \theta_ {j} \big) \cong Y _ {i j} \big (\theta_ {i} - \theta_ {j} \big). \end{array}\tag{6}
$$

If it is further assumed that $x _ { i j } \gg r _ { i j } ,$ then $Y _ { i j } =$ $( x _ { i j } ) / ( r _ { i j } ^ { 2 } + x _ { i j } ^ { 2 } ) \cong 1 / x _ { i j } ,$ , so that we finally obtain the usual approximate expression for real power flow from bus i to bus $j \colon$

$$
\Psi_ {i j} \big (\theta_ {i} - \theta_ {j} \big) = \frac {1}{x _ {i j}} \big (\theta_ {i} - \theta_ {j} \big).
$$

Assume customer $\eta ^ { \star } \mathbf { s }$ inverse demand function is $P ( \boldsymbol { q } ( \eta ) ; \eta )$ , then the $V ( \cdot )$ Ž . in Eq. 2 can be specified as $\begin{array} { r l } { \int _ { 0 } ^ { x ( \eta ) } P _ { \eta } ( q ( \eta ) ) \mathrm { d } q ( \eta ) } \end{array}$ . Using this representation of $V ( \cdot )$ and the above results, the DC approximation of the FBP can be stated as follows: Approximate first-best problem AFBP Ž .

$$
\begin{array}{l} \max _ {\mathbf {X}, \mathbf {Q}, \boldsymbol {\Theta}} \Bigg [ \sum_ {\eta \in \mathcal {D}} \int_ {0} ^ {x (\eta)} P (  q (\eta); \eta) \mathrm{d} q (\eta) \\ - \sum_ {\zeta \in \mathcal {G}} C _ {\mathrm{g}} (  q (\zeta); \zeta) - F \Bigg ], \end{array}\tag{7}
$$

s.t.

$$
\sum_ {\zeta \in \mathscr {G} _ {i}} q (\zeta) - \sum_ {\eta \in \mathscr {D} _ {i}} x (\eta) = \sum_ {j = 1} ^ {N} \frac {1}{x _ {i j}} \left(\theta_ {i} - \theta_ {j}\right)
$$

$$
i = 1, \ldots , N,\tag{8}
$$

$$
\frac {1}{x _ {i j}} \left(\theta_ {i} - \theta_ {j}\right) \leq \overline {{P}} _ {i j}, \quad \text { for } 1 \leq i, \quad j \leq N.\tag{9}
$$

To illustrate the first-best framework developed above, we present a numerical three-node example adapted from Chao and Peck 7 .<sup>w</sup> <sup>x</sup>

## 3.2. A simple numerical example

We make the following assumptions:

1. There are two power generators nodes 1 and 2 , Ž . $\mathrm { i . e . , ~ } \mathcal { G } = \{ 1 , 2 \}$ and one customer node 3 , i.e.,Ž . $\mathcal { D } = \{ 3 \}$

2. Customer’s inverse demand function is $P ( q ( 3 ) ; 3 )$ $= a _ { 3 } - b _ { 3 } q ( 3 )$ , with $a _ { 3 } = 1 1 0$ and $b _ { 3 } = 0 . 2$ , so that $P ( q ( 3 ) ; 3 ) = 1 1 0 - 0 . 2 q ( 3 )$

3. No line losses, in this case, the only transmission cost is the fixed investment, which is assumed to be $F = 1 5 .$

4. Generation capacity limits, both firms have a generation capacity of 500 MW, ${ \overline { { q ( 1 ) } } } = { \overline { { q ( 2 ) } } } =$ 500.

5. Generation costs for firm 1: $C _ { \mathrm { g } } ( q ( 1 ) ; 1 ) = 1 0 0 +$ $1 0 q ( 1 )$ , and for firm 2: $C _ { \mathrm { g } } ^ { \mathrm { ^ { \circ } } } ( q ( 2 ) ; 2 ) = 1 0 0 +$ $3 0 q ( 2 )$

6. We assume a symmetric physical network, i.e., each line has the same impedance.

The problem we are interested in is: How much power should each firm inject into the network $( q ( 1 ) , q ( 2 ) ) \ ?$ Additionally, what price $( P ( q ( 3 ) ; 3 ) )$ should the consumer pay?

Case 1: There is no transmission capacity limit on any line. The objective function in Eq. 7 can be Ž . expressed for this example as:

$$
\begin{array}{l} \max _ {q (1), q (2)} W = \int_ {0} ^ {q (1) + q (2)} P _ {3} (  q (3); 3) \mathrm{d} q (3) \\ \qquad - C _ {\mathrm{g}} (  q (1); 1) - C _ {\mathrm{g}} (  q (2); 2) - F, \end{array}\tag{10}
$$

where $P ( q ( 3 ) ; 3 )$ is the inverse demand function. Plugging in our previous assumptions 2 and 5, the solution to this unconstrained optimization problem is: $( W ^ { * } , q ^ { * } ( 1 ) , q ^ { * } ( 2 ) , P ^ { * } ( q ^ { * } ( 3 ) ; 3 ) ) = ( 2 4 , 7 8 5 , 5 0 0 ,$ 0, 10 ..

Case 2: Now, we consider transmission constraints. Assume line 12 has a capacity limit of 50

![](/api/attachments/5Z8XYEJ5/fulltext/images/b34b927ba38c237a8c6cfeeb00e571b1c78105f2a700075aca19e0d49957b209.jpg)  
Fig. 1. Three-bus example with line congestion. This example is borrowed from Chao and Peck 7 using the objective function <sup>w</sup> <sup>x</sup> Ž . 10 .

MW. There are no limits on other lines. The problem of interest is:

$$
\begin{array}{c} \max _ {q (1), q (2)} W = \int_ {0} ^ {q (1) + q (2)} P (  q (3); 3) \mathrm{d} q (3) \\ - C _ {\mathrm{g}} (  q (1); 1) - C _ {\mathrm{g}} (  q (2); 2) - F, \end{array}
$$

s.t.

$$
\left| \frac {1}{3} q (1) - \frac {1}{3} q (2) \right| \leq 5 0,\tag{11}
$$

$$
0 \leq q (i) \leq 5 0 0, \quad i = 1, 2.
$$

Constraint 11 holds because of the followingŽ . reason. Since the network is symmetric, for every $q ( 1 )$ generated at node 1, according to Kirchoff’s law, $( 1 / 3 ) q ( 1 )$ flows on line 12. Similarly, one third of generator $2 \mathrm { { } ^ { * } s }$ power output, $( 1 / 3 ) q ( 2 )$ , flows on line 21. Therefore, the net flow on line 12 would be $| ( 1 / 3 ) q ( 1 ) - ( 1 / 3 ) q ( 2 ) |$ , which must satisfy the line<sup><</sup> capacity limit 50 MW , hence, the constraint.Ž .

The optimal solution is $\left( W ^ { * } , \ q ^ { * } ( 1 ) , \ q ^ { * } ( 2 ) \right.$ $P ^ { * } ( q ^ { * } ( 3 ) ; 3 ) ) = ( 2 1 , 5 3 5 , 3 0 0 , 1 5 0 , 2 0 )$ as shown in Fig. 1. Note that as a result of the line congestion, the optimal social welfare decreases from 24,785 toŽ 21,535 ..

## 4. Experimental design

We now describe an experiment to test the efficacy of GA in solving problem AFBP, i.e., Eqs. $( 7 ) { - } ( 9 )$ . We begin by describing the test cases to be examined. The computational experiment reported below is based on a system that can randomly gener-

Table 1

ate problems for genetic algorithms to solve. It can generate any number of N-bus electric power network problems. This paper reports the six nodes or buses case i.e.,Ž . Ž N <sup>s</sup> 6 , as shown in Fig. 2. The sample six-bus network, including structure and electric characteristics of the network, is borrowed from Ref. 42 . Buses 1, 2, and 3 are power suppliers,<sup>w</sup> <sup>x</sup> . while buses 4, 5, and 6 are consumers of power. Each supplier has its own technology i.e., costŽ function and a maximum capacity limit; each con- . sumer has its own demand function. There is also a capacity limit for each line in the network. For simplicity, we assume no line losses; however, line losses can be incorporated in the model with no difficulty, as shown elsewhere 44 . We focus on<sup>w</sup> <sup>x</sup> problem AFBP, but we will discuss results for the more general problem FBP below.

## 4.1. Generating costs

Assume each supplier has a fixed power generating capacity. In the test problems which follow, assume capacity is fixed at 500 MW for each generation node i, i <sup>s</sup> 1,2,3. As in standard public economics 9 , assume the following relationship be- <sup>w</sup> <sup>x</sup> tween variable cost $b _ { 1 } < b _ { 2 } < b _ { 3 }$ and capacity cost $\beta _ { 1 } > \beta _ { 2 } > \beta _ { 3 }$ so that none of the generation plants is a priori dominated. The generation cost function for node i then has the formula of $C _ { \mathrm { g } } ( q ( \zeta ) ; \zeta ) = \beta _ { \zeta } +$ $b _ { \zeta } q ( \zeta ) , \zeta = 1 , 2 , 3$ , where $( b _ { \zeta } , \beta _ { \zeta } )$ are given in Table 1.

![](/api/attachments/5Z8XYEJ5/fulltext/images/beb5851819bbe6f6056ca7156606be40f036b2bd91d1854b3bbab42dbb66e107.jpg)  
Fig. 2. Network structure for a six-bus sample power system.

<table><tr><td> $\zeta$ </td><td> $b_{\zeta}$ </td><td> $\beta_{\zeta}$ </td></tr><tr><td>1</td><td>x</td><td>1000+50x</td></tr><tr><td>2</td><td>1.2x</td><td>1000+40x</td></tr><tr><td>3</td><td>1.4x</td><td>1000+30x</td></tr></table>

The above $x$ is randomly chosen; it can be either ‘‘high’’ H or ‘‘low’’ L . In the test problems Ž . Ž . which follow, high cost means x is drawn from a probability distribution that is uniformly distributed over 25, 30 , and low cost meansŽ . x is drawn from a probability distribution that is uniformly distributed over 10, 15 .Ž .

## 4.2. Line capacities

There are 11 possible interconnecting links among the six nodes in the network Fig. 2 . The capacity of Ž . each link is randomly generated. The following scheme has been used:

$$
L _ {i} = L ^ {*} \frac {u _ {i}}{\sum_ {j = 1} ^ {1 1} u _ {j}}, \quad i = 1, \dots , 1 1,
$$

where $u _ { i }$ are uniformly distributed over 0, 1 .Ž .

$L ^ { * }$ Ž . total transmission capacity can either be ‘‘high’’ H or ‘‘low’’ L . In the test problems Ž . Ž . below, high capacity means that $L ^ { * } = 2 0 0 0$ MW, and low capacity means $L ^ { * } = 5 0 0 ~ \mathrm { M W }$

## 4.3. InÕerse demand functions

For each of the demand nodes , assume there is a linear inverse demand function,

$$
P (x (\eta); \eta) = a _ {\eta} - b _ {\eta} x (\eta),
$$

where $a _ { \eta }$ defines the intercept and $b _ { \eta }$ defines the slope. Four possible combinations have been considered: high intercept, low intercept, elastic demand Ž . low slope in the inverse demand function , and inelastic demand high slope in the inverse demandŽ function , as shown in Table 2..

The actual values of $a _ { \eta }$ for each test problem are generated as follows:

$$
a _ {\eta} = I ^ {*} \frac {u _ {\eta}}{\sum_ {j = 4} ^ {6} u _ {j}}, \quad \eta = 4, 5, 6,
$$

Table 2 Demand functions

<table><tr><td rowspan="2"></td><td colspan="2">Demand elasticity</td></tr><tr><td>L</td><td>H</td></tr><tr><td>Intercept (L)</td><td>(L,L)</td><td>(L,H)</td></tr><tr><td>Intercept (H)</td><td>(H,L)</td><td>(H,H)</td></tr></table>

where $u _ { \eta }$ Ž . are uniformly distributed over 0, 1 . $I ^ { * }$ can either be high intercept or low intercept. In the six-bus test problems below, high intercept means $I ^ { * } = 1 5 0 0 ~ \mathrm { M W }$ , and low intercept means $I ^ { * } = 1 0 0 0$ MW.

In a similar fashion, the values of $b _ { \eta }$ are generated as follows:

$$
b _ {\eta} = S ^ {*} \frac {u _ {\eta}}{\sum_ {j = 4} ^ {6} u _ {j}}, \quad \eta = 4, 5, 6,
$$

where $u _ { \eta }$ Ž . are uniformly distributed over 0, 1 . $S ^ { * }$ can be either high or low. In problems tested, high slope means $S ^ { * } = 0 . 8$ , and low slope means $S ^ { * } =$ 0.6.

To summarize, three factors line capacity, de-Ž mand and cost are being considered in the testing. scenarios. Factor 1 line capacity has two levels.Ž . Factor 2 demand has four levels. Factor 3 costŽ . Ž . has two levels. A full combination of factors and levels yields 16 cases for a particular test set. The experiment runs three complete sets that examine a total of 48 different network scenarios. Tables 6–11 in Appendix B show data generated.

## 4.4. Optimal solutions

Using the information regarding the inverse demand functions at each bus, and network structure input data, the AFBP, i.e., Eqs. 7 – 9 , can beŽ . Ž . reduced to a quadratic programming problem with linear constraints. Thus, the search space is convex. There may, however, be a very large number of constraints due to the complexity of the system. Nevertheless, constraint set convexity will be exploited in the designing of genetic algorithms in Section 5.

Since AFBP can be reduced to quadratic programming with linear constraints, the optimal solution for each case of interest can be computed using GAMS <sup>w</sup> <sup>x</sup> 18 software. The resulting computational results are used to benchmark the performance of genetic algorithms. The general problem studied here will soon be out of reach of any existing software package when incorporating the general non-linear objective function of FBP, or system constraints of the form Ž . Ž . 3 – 4 . However, such problems will still be within the scope of the genetic algorithms approach 44 . <sup>w</sup> <sup>x</sup> The study here intends to provide the foundation for future development of such methods.

## 5. GA approach, experimental results and discussion

This section describes the representation, constraint-handling mechanisms and findings of the experiment. The goal of this experiment is to find what types of genetic algorithms perform well for the network problem of interest. Several GAs have been designed and implemented. These GAs share common representation, fitness function and initialization procedure, as summarized below, but differ in constraint-handling mechanisms.

## 5.1. GA representation

Ž . 1 Representation: Since the variables of interest in the AFBP are real numbers, these will be represented in standard floating point representation in the computer implementation of the GA. Each chromosome vector is coded as a vector of floating point numbers of the same length as the solution vector.

Ž .2 Fitness function: This is the social welfare function modified as discussed below to penalize constraint violation s .Ž .

Ž . 3 Initialization: GA will try a user pre-specified number e.g., 5000 of times randomly to find aŽ . feasible initial population; if not successful, GA will request a feasible solution from the user, and then produce identical copies for the initial population.

## 5.2. Penalty function methods

Various penalty function methods have been experimentally studied as constraint-handling techniques. Before providing a brief summary of the results, we use standard notations in the literature Že.g., Ref. 33 .<sup>w</sup> <sup>x</sup>.

Define a general mathematical program as:

$$
\max _ {x} f (x),
$$

s.t.

$$
x = \left(x _ {1}, \dots , x _ {n}\right) \in X \subseteq \mathcal {R} ^ {n},
$$

$$
g _ {i} (x) \leq 0, j = 1, 2, \ldots , k,
$$

$$
h _ {j} (x) = 0, \quad j = k + 1, \dots , m.
$$

Let ${ \mathcal { F } } \subseteq { \mathcal { R } } ^ { n }$ be the feasible set for the above program.

Define the evaluation function as:

$$
\operatorname{eval} (x) = \left\{ \begin{array}{l l} f (x), & \text { if } x \in \mathscr {F}, \\ f (x) + \text { penalty } (x), & \text { otherwise }. \end{array} \right.
$$

Define the set of penalty functions $f _ { j } ( x )$ as:

$$
f _ {j} (x) = \left\{ \begin{array}{l l} \max \bigl \{0, g _ {j} (x) \bigr \}, & \text { if } 1 \leq j \leq k, \\ | h _ {j} (x) |, & \text { if } k + 1 \leq j \leq m. \end{array} \right.
$$

## 5.2.1. Static penalty functions

The static penalty function implemented has the formula:

$$
\operatorname{eval} (x) = f (x) + \sum_ {j = 1} ^ {m} R _ {j} f _ {j} ^ {2} (x),
$$

where $R _ { i } < 0$ is the penalty coefficient and m is the number of constraints in the problem.

The following parameters have been tested: $R _ { j } =$ 1, 5, 100; $j = 1 , \ldots , m$ . In all cases, what was found could be called a ‘‘Drug-dealer’’ type of GA behavior, i.e., GA is making the tradeoff between the additional benefit by violating the constraints vs. the additional punishment incurred because of the constraint violation. The results show that the static penalty function method implemented cannot guarantee the feasibility of the solution.

## 5.2.2. Dynamic penalty functions

Two simplified versions of the dynamic penalty function method are implemented. The following are the corresponding formulas used:

$$
\operatorname{eval} _ {1} (x) = f (x) + t \sum_ {j = 1} ^ {m} f _ {j} ^ {2} (x),
$$

and

$$
\operatorname{eval} _ {2} (x) = f (x) + t ^ {2} \sum_ {j = 1} ^ {m} f _ {j} ^ {2} (x),
$$

where t is the generation number.

The experiment shows that dynamic penalty function methods do not do well either. What was observed is that in the initial stage of GA trials, GA can detect some of the feasible solutions to the problem of interest. As the generation number increases, GA cannot find any feasible solution at all. This observation is further confirmed when the extreme form of penalty, the death penalty, is used.

## 5.2.3. Death penalty functions

The method used rejects all infeasible solutions in the population. Under this method, if in some current population infeasible solutions result after the GA operators are applied, these are simply eliminated and replaced by randomly drawn new solutions. If a new solution is still not feasible, we randomly draw a fixed number say, 1000 of trials until a feasibleŽ . solution results. However, after all these trials, if the system still cannot find a new feasible solution, then we randomly make identical copies of existing Ž . feasible solutions.

The experiments show that the death penalty is the worst method among all three penalty function methods tested. However, this method has been used in other evolution-based approaches with some success, such as in simulated annealing and evolutionary programming 33 . Using standard GA parameters, <sup>w</sup> <sup>x</sup> unless given by the user, GA could not even find an initial feasible solution to some test problems after 1 million trials.

## 5.3. Domain specific genetic algorithms

Finally, domain specific genetic algorithms are introduced as constraint-handling techniques. GA-1 is designed and implemented using special operators that are defined as follows. We use standard definitions of these operators in the literature e.g., Ref. Ž <sup>w</sup> <sup>x</sup> 33 ..

Arithmetic cross-over is defined as a linear combination of two vectors: if x and y are to be crossed, the resulting offspring are $x ^ { \prime } = a x + ( 1 - a ) y$ and $y ^ { \prime } = a y + ( 1 - a ) x .$ , where a is a random value $\in$ <sup>w</sup> <sup>x</sup> 0,1 .

Table 3  
GA-1 performance for test set-1

<table><tr><td>No.</td><td>Optimal solution</td><td>100 generations</td><td>Errors</td><td>500 generations</td><td>Errors</td><td>5000 generations</td><td>Errors</td><td>Best solution</td><td>Errors</td></tr><tr><td>1</td><td>314,660</td><td>312,980</td><td>0.5</td><td>314,166</td><td>0.2</td><td>313,130</td><td>0.5</td><td>314,624</td><td>0.0</td></tr><tr><td>2</td><td>236,413</td><td>225,680</td><td>4.5</td><td>236,413</td><td>0.0</td><td>236,413</td><td>0.0</td><td>236,413</td><td>0.0</td></tr><tr><td>3</td><td>306,536</td><td>291,282</td><td>5.0</td><td>292,248</td><td>4.7</td><td>305,602</td><td>0.3</td><td>305,602</td><td>0.3</td></tr><tr><td>4</td><td>343,405</td><td>281,413</td><td>18.1</td><td>303,232</td><td>11.7</td><td>295,090</td><td>14.1</td><td>334,722</td><td>2.5</td></tr><tr><td>5</td><td>254,836</td><td>252,162</td><td>1.0</td><td>253,743</td><td>0.4</td><td>252,222</td><td>1.0</td><td>253,743</td><td>0.4</td></tr><tr><td>6</td><td>366,276</td><td>354,520</td><td>3.2</td><td>365,572</td><td>0.2</td><td>359,814</td><td>1.8</td><td>365,572</td><td>0.2</td></tr><tr><td>7</td><td>458,807</td><td>195,274</td><td>57.4</td><td>433,847</td><td>5.4</td><td>458,633</td><td>0.0</td><td>458,633</td><td>0.0</td></tr><tr><td>8</td><td>422,846</td><td>409,258</td><td>3.2</td><td>410,167</td><td>3.0</td><td>410,189</td><td>3.0</td><td>410,189</td><td>3.0</td></tr><tr><td>9</td><td>23,971</td><td>17,643</td><td>26.4</td><td>18,143</td><td>24.3</td><td>18,102</td><td>24.5</td><td>21,784</td><td>9.1</td></tr><tr><td>10</td><td>22,627</td><td>16,542</td><td>26.9</td><td>22,108</td><td>2.3</td><td>18,415</td><td>18.6</td><td>22,108</td><td>2.3</td></tr><tr><td>11</td><td>79,283</td><td>67,871</td><td>14.4</td><td>69,445</td><td>12.4</td><td>79,281</td><td>0.0</td><td>79,281</td><td>0.0</td></tr><tr><td>12</td><td>94,838</td><td>45,607</td><td>51.9</td><td>94,837</td><td>0.0</td><td>88,236</td><td>7.0</td><td>94,837</td><td>0.0</td></tr><tr><td>13</td><td>83,908</td><td>79,751</td><td>5.0</td><td>74,500</td><td>11.2</td><td>83,468</td><td>0.5</td><td>83,679</td><td>0.3</td></tr><tr><td>14</td><td>68,869</td><td>36,166</td><td>47.5</td><td>55,839</td><td>18.9</td><td>65,174</td><td>5.4</td><td>65,174</td><td>5.4</td></tr><tr><td>15</td><td>65,025</td><td>64,784</td><td>0.4</td><td>64,761</td><td>0.4</td><td>64,972</td><td>0.1</td><td>64,972</td><td>0.1</td></tr><tr><td>16</td><td>145,970</td><td>145,868</td><td>0.1</td><td>145,962</td><td>0.0</td><td>145,889</td><td>0.1</td><td>145,962</td><td>0.0</td></tr></table>

Uniform mutation is defined as follows: suppose $\boldsymbol { x } ( t ) = ( x _ { 1 } , \ldots , x _ { k } , \ldots , x _ { N } ) ,$ then $x ( t + 1 ) =$ $( x _ { 1 } , \ldots , x _ { k } ^ { \prime } , \ldots , x _ { N } )$ , where $x _ { k } ^ { \prime } \ldots$ . is a random value uniformly distributed over the feasible domain of variable $x _ { k }$ where $l ( k ) \leq x _ { k } \leq r ( k )$ . A special case of uniform distribution is boundary mutation, where $\ v x _ { k } ^ { \prime }$ is either the left boundary Ž Ž .. l k or the right boundary Ž Ž .. r k of the domain of $x _ { k }$ , with equal probability 50% each .Ž .

Non-uniform mutation is defined as follows:

$x _ { k } ^ { \prime } = \left\{ { { x _ { k } } + \Delta ( t , r ( k ) - x _ { k } ) } \right.$ if a random binary digit is 0, if a random binary digit is 1,

for $k = 1 , \ldots , n .$ The function $\boldsymbol { \varDelta } ( t , y )$ returns a value in the range 0, <sup>w</sup> <sup>x</sup> y such that the probability of $\varDelta ( t , y )$

Table 4  
GA-1 performance for test set-2

<table><tr><td>No.</td><td>Optimal solution</td><td>100 generations</td><td>Errors</td><td>500 generations</td><td>Errors</td><td>5000 generations</td><td>Errors</td><td>Best solution</td><td>Errors</td></tr><tr><td>1</td><td>249,348</td><td>228,637</td><td>8.3</td><td>242,206</td><td>2.9</td><td>242,921</td><td>2.6</td><td>241,865</td><td>3.0</td></tr><tr><td>2</td><td>148,539</td><td>143,430</td><td>3.4</td><td>148,229</td><td>0.2</td><td>140,078</td><td>5.7</td><td>148,229</td><td>0.2</td></tr><tr><td>3</td><td>555,289</td><td>552,953</td><td>0.4</td><td>552,561</td><td>0.5</td><td>552,691</td><td>0.5</td><td>552,953</td><td>0.4</td></tr><tr><td>4</td><td>327,740</td><td>326,504</td><td>0.4</td><td>286,970</td><td>12.4</td><td>297,953</td><td>9.1</td><td>326,943</td><td>0.2</td></tr><tr><td>5</td><td>185,301</td><td>181,880</td><td>1.8</td><td>181,456</td><td>2.1</td><td>176,742</td><td>4.6</td><td>181,880</td><td>1.8</td></tr><tr><td>6</td><td>268,446</td><td>246,827</td><td>8.1</td><td>267,111</td><td>0.5</td><td>266,986</td><td>0.5</td><td>267,111</td><td>0.5</td></tr><tr><td>7</td><td>278,889</td><td>274,007</td><td>1.8</td><td>227,827</td><td>18.3</td><td>242,956</td><td>12.9</td><td>277,155</td><td>0.6</td></tr><tr><td>8</td><td>431,454</td><td>431,314</td><td>0.0</td><td>431,269</td><td>0.0</td><td>431,351</td><td>0.0</td><td>431,351</td><td>0.0</td></tr><tr><td>9</td><td>59,154</td><td>52,487</td><td>11.3</td><td>57,871</td><td>2.2</td><td>58,622</td><td>0.9</td><td>58,622</td><td>0.9</td></tr><tr><td>10</td><td>25,496</td><td>22,985</td><td>9.8</td><td>25,488</td><td>0.0</td><td>25,496</td><td>0.0</td><td>25,496</td><td>0.0</td></tr><tr><td>11</td><td>87,864</td><td>81,520</td><td>7.2</td><td>84,611</td><td>3.7</td><td>84,672</td><td>3.6</td><td>84,672</td><td>3.6</td></tr><tr><td>12</td><td>96,072</td><td>94,838</td><td>1.3</td><td>94,969</td><td>1.1</td><td>95,097</td><td>1.0</td><td>95,097</td><td>1.0</td></tr><tr><td>13</td><td>73,281</td><td>65,901</td><td>10.1</td><td>65,901</td><td>10.1</td><td>65,868</td><td>10.1</td><td>72,606</td><td>0.9</td></tr><tr><td>14</td><td>53,743</td><td>52,585</td><td>2.2</td><td>53,532</td><td>0.4</td><td>53,731</td><td>0.0</td><td>53,731</td><td>0.0</td></tr><tr><td>15</td><td>106,000</td><td>105,942</td><td>0.1</td><td>83,534</td><td>21.2</td><td>105,944</td><td>0.1</td><td>105,944</td><td>0.1</td></tr><tr><td>16</td><td>77,825</td><td>67,559</td><td>13.2</td><td>75,887</td><td>2.5</td><td>74,956</td><td>3.7</td><td>76,607</td><td>1.6</td></tr></table>

Table 5  
GA-1 performance for test set-3

<table><tr><td>No.</td><td>Optimal solution</td><td>100 generations</td><td>Errors</td><td>500 generations</td><td>Errors</td><td>5000 generations</td><td>Errors</td><td>Best solution</td><td>Errors</td></tr><tr><td>1</td><td>244,381</td><td>242,702</td><td>0.7</td><td>244,214</td><td>0.1</td><td>244,232</td><td>0.1</td><td>244,255</td><td>0.1</td></tr><tr><td>2</td><td>40,113</td><td>37,445</td><td>6.7</td><td>37,961</td><td>5.4</td><td>39,955</td><td>0.4</td><td>39,955</td><td>0.4</td></tr><tr><td>3</td><td>386,594</td><td>386,130</td><td>0.1</td><td>354,628</td><td>8.3</td><td>386,754</td><td>0.0</td><td>386,754</td><td>0.0</td></tr><tr><td>4</td><td>489,516</td><td>481,006</td><td>1.7</td><td>466,423</td><td>4.7</td><td>483,008</td><td>1.3</td><td>483,008</td><td>1.3</td></tr><tr><td>5</td><td>277,125</td><td>276,870</td><td>0.1</td><td>255,831</td><td>7.7</td><td>251,631</td><td>9.2</td><td>277,091</td><td>0.0</td></tr><tr><td>6</td><td>155,465</td><td>150,204</td><td>3.4</td><td>143,951</td><td>7.4</td><td>141,187</td><td>9.2</td><td>151,572</td><td>2.5</td></tr><tr><td>7</td><td>298,810</td><td>67,600</td><td>77.4</td><td>65,821</td><td>78.0</td><td>115,033</td><td>61.5</td><td>297,831</td><td>0.3</td></tr><tr><td>8</td><td>295,806</td><td>271,652</td><td>8.2</td><td>272,686</td><td>7.8</td><td>268,544</td><td>9.2</td><td>293,923</td><td>0.6</td></tr><tr><td>9</td><td>52,200</td><td>51,738</td><td>0.9</td><td>52,080</td><td>0.2</td><td>52,080</td><td>0.2</td><td>52,080</td><td>0.2</td></tr><tr><td>10</td><td>93,459</td><td>91,052</td><td>2.6</td><td>93,307</td><td>0.2</td><td>93,307</td><td>0.2</td><td>93,307</td><td>0.2</td></tr><tr><td>11</td><td>46,951</td><td>46,610</td><td>0.7</td><td>46,128</td><td>1.8</td><td>46,913</td><td>0.1</td><td>46,913</td><td>0.1</td></tr><tr><td>12</td><td>111,045</td><td>109,341</td><td>1.5</td><td>108,269</td><td>2.5</td><td>110,428</td><td>0.6</td><td>110,428</td><td>0.6</td></tr><tr><td>13</td><td>28,106</td><td>27,414</td><td>2.5</td><td>27,837</td><td>1.0</td><td>27,856</td><td>0.9</td><td>27,909</td><td>0.7</td></tr><tr><td>14</td><td>50,537</td><td>25,977</td><td>48.6</td><td>44,168</td><td>12.6</td><td>48,298</td><td>4.4</td><td>50,432</td><td>0.2</td></tr><tr><td>15</td><td>160,027</td><td>159,727</td><td>0.2</td><td>159,601</td><td>0.3</td><td>156,165</td><td>2.4</td><td>159,993</td><td>0.0</td></tr><tr><td>16</td><td>110,199</td><td>51,351</td><td>53.4</td><td>55,604</td><td>49.5</td><td>54,845</td><td>50.2</td><td>102,928</td><td>6.6</td></tr></table>

being close to 0 increases as t increases Žt is the generation number . This way of choosing . $\boldsymbol { \varDelta } ( t , y )$ assures that the mutation operator will search the entire feasible space uniformly initially when theŽ generation number is small , and very locally at later . stages when the generation number is large . In theŽ . experiment, we use the following function of Michalewicz 33 :<sup>w</sup> <sup>x</sup>

$$
\Delta (t, y) = y r \left(1 - \frac {t}{T}\right) ^ {b},
$$

where r is a random number between 0,1 ,  T is the user-specified maximum generation number, and b <sup>)</sup>0 is a system parameter determining the degree of non-uniformity.

Table 3 4, 5 shows GA-1 performance on the 16Ž . problems in test set 1 2, 3 . GA-1 was run a numberŽ . of times for a particular problem to observe the effects of running time maximum number of genera- Ž tions on performance..

The results in Tables 3–5 suggest that GA-1 is very efficient and robust in solving the problems of interest here. Fig. 3 shows the search procedure for an ‘‘easy’’ problem for GA-1, where GA-1 detects a close-to-optimal solution within 100 generations. In contrast, Fig. 4 shows the search procedure for a ‘‘tough’’ problem for GA-1, where GA-1 quickly detects close-to-optimal regions, but the asymptotic convergence rate for this problem is slow. In summary, for all 48 test problems, the gap between

GA-1 solutions and optimal solutions ranges from 0% to 9.1%. The average error rate for test sets 1, 2 and 3 are correspondingly 1.48%, 0.94%, and 0.86%. These results are very promising.

## 5.4. Discussion of GA experiment

The experiment raises the issue of how to explain, understand and justify the behavior of genetic algorithms. It also connects with relevant research in the literature, such as the usefulness of infeasible information.

![](/api/attachments/5Z8XYEJ5/fulltext/images/ed5b25ff5459096721ed465bde9b8990a36d38b201943ff0785a85d9ed3e615b.jpg)  
Fig. 3. GA-1 behavior for problem 2 in test set-1. Dotted line represents the optimal solution. Solid line represents the search procedure of GA-1. This figure shows that GA-1 detects close-tooptimal solution within 100 generations.

![](/api/attachments/5Z8XYEJ5/fulltext/images/9cc152310dac8dafa8795384bc72e8d43f8284e58cc5d050a9ccefeef12cd3bb.jpg)  
Fig. 4. GA-1 behavior for problem 9 in test set-1. Solid line represents the search procedure of GA-1. Dotted line represents the optimal solution. This figure shows that GA-1 quickly detects close-to-optimal regions but this case also illustrates that further work on end-game solutions remains an interesting research area given the slow asymptotic convergence rate for this problem.

When using static penalty functions, GA trades off additional gains of welfare vs. additional punishment due to violations of the constraints. This is reminiscent of the behavior of a drug dealer, hence, the name ‘‘Drug-Dealer’’. When the dynamic penalty function method was used, in the initial stage, GA performed adequately in finding some feasible solutions. However, due to the heavy punishment in later stages, GA rarely found feasible solutions there. This was consistent with findings by other researchers where these methods were applied solely to simple mathematical problems see Ref. 33 for an excel-Ž <sup>w</sup> <sup>x</sup> lent review . The significance of this study is that it. extends these findings to a realistic network problem.

The experiments showed that the death penalty function methods, which have always been used in traditional mathematical programming, were the poorest for solving the problems being tested. GA was unable to find an initial feasible population due to the extreme punishment of the ‘‘death penalty’’. This illustrates the wisdom of the ancient Chinese philosopher, Chuang-Tzu: ‘‘When the water is too pure, there are no fish.’’

More interesting questions arising from this study are on the usefulness of infeasible solutions, an issue first addressed in Ref. 33 . Was the poor perfor-<sup>w</sup> <sup>x</sup> mance of the death penalty method due to not using the information embodied in infeasible solutions? Could the information in the infeasible solutions be used to direct the search of genetic algorithms?

The experiments showed that the arithmetic crossover method embodied in GA-1 works best for AFBP. GA-1 can find near-optimal solutions for all randomly generated 48 different network scenarios as shown in Tables 3–5.

Notwithstanding these promising results for AFBP, the reader should note that the more important message arising from these computational explorations is the significance of domain-specific GAs. AFBP is a convex problem and, therefore, it may not be entirely surprising that the arithmetic crossover method does well, in that it allows a rich exploration of interior solutions while maintaining feasibility. In non-convex problems or in problems with other domain-specific characteristics, other methods could well be required to utilize the domain-specific structure of the problem. In particular, repair methods, non-uniform mutation methods and other methods idiosyncratic to the specific problem will likely be required to assure superior performance for other problems. On the one hand, the problem specificity of GAs may be considered a disadvantage of GA as a general solution approach. But, considering the scope of possible GA methods, in fact, GAs are quite robust and can be used across a broad set of problem types. The key issue is to determine the appropriate methods from the set of available tools for each problem type. For problems of the type AFBP, GA-1 represents a very robust approach.

It remains unknown whether any domain-specific GA will consistently converge to a global optimum <sup>w</sup> <sup>x</sup> 3,43,44 . The primary difficulty is again due to network constraints. So far, formal analysis on global convergence of genetic algorithms is valid only for classical GA, i.e., bit-string representation with standard crossover, with no constraints except for simple bounds on decision variables 3,21,39 . None of the<sup>w</sup> <sup>x</sup> known analysis applies for domain-specific genetic algorithms such as those studied here.

## 6. Summary

This paper is a first step in an effort to provide efficient decision support for network problems. It applies a theoretical framework for modeling network problems, developed earlier by the author, to a class of important network pricing problems in the electric power sector. Given the NP-hardness of such models, genetic algorithms could be a useful primary computational approach. The attention of the research has been on what type of genetic algorithms could effectively solve the problems of interest.

In terms of the GA experiment, the results obtained are potentially significant for the advancement of research in the field. In contrast to the existing style in the literature or in toy industry products, the genetic algorithms studied here have solid foundations. The arithmetic crossover operator, as well as the mutation operator of GA-1, has been carefully designed to maintain the feasibility of all intermediate and final solutions. This works well because the search space of AFBP is convex.

GA-1 was designed to solve general network problems with convex constraints. This approach, in conjunction with a repair method, has been generalized to the non-convex problem respecting the actual FBP, i.e., Eqs. 2 – 4 , for electric power 44 . TheŽ . Ž . <sup>w</sup> <sup>x</sup> result was the design of two other types of genetic algorithms, GA-2 and GA-3. GA-2 aimed to discover new business operating strategies for network expansion and investment problems. GA-3 aimed to incorporate real world technology constraints of electric power systems that are highly non-linear. GA-1, GA-2 and GA-3 are three DSS prototypes built as a result of this research that might be useful for researchers as well as industry practitioners. For example, they could be useful in providing constructive methods to help develop commercial GA software packages that currently have limited constraint-handling capability.

Due to space limitation, this paper only reports the results of a six-node fully connected power grid; however, the approach is general. It works for a general network with any number of buses as specified in the first-best model. In terms of real application, the six-node example is already very useful to derive insightful business operating strategies. For example, the node here can be viewed as a ‘‘zone’’ that might constitute a region of a larger power grid. Therefore, the six-node example can be viewed as a six-zone network, which is already general enough to study policies such as the ‘‘zonal pricing’’ proposal <sup>w</sup> <sup>x</sup> <sub>6</sub> <sub>.</sub>

## Acknowledgements

The author is grateful for the insightful guidance of Paul Kleindorfer for this research. Penalty function methods GAs were implemented using Steven Kimbrough’s GAVBSTUB. GA-1 was developed using Zbigniew Michalewize’s GENOCOP. I thank the owners for sharing the source code. Helpful comments from James Laing, Steve Kimbrough, Ronald Lee, participants in the formal aspects of the electronic commerce session of HICSS-32, and three anonymous referees are greatly appreciated. Thanks to Marge Weiler for proofreading this paper. However, all errors remain with the author. This paper was based on Chapter 4 of the author’s dissertation 44 .<sup>w</sup> <sup>x</sup> The dissertation was nominated for the best PhD dissertation for the 1998 Elwood Buffa National Dissertation Award Competition in the 1998 National Decision Science Institute DSI meeting in Ž . November, 1998, in Las Vegas. An earlier and much abbreviated version of this paper 46 appeared in the<sup>w</sup> <sup>x</sup> Proceedings of the 32nd Annual Hawaii International Conference on System Sciences HICSS-32 in Jan-Ž . uary, 1999, Hawaii. This work was made possible by research grants from SAP America, Andersen Consulting, and an equipment grant from Hewlett-Packard.

## Appendix A. Sketch of proof of Theorem 1

By the Weierstrass theorem and the continuity of the objective function, it suffices to show that the constraint set defines a non-empty compact set. To this end, first note that the constraint set is non-empty since setting all the decision vectors X, Q, to 0, yields a feasible solution. To see that the constraint set is compact, note that from the continuity of all the functions involved and the compactness of $\theta _ { i }$ $( \mathrm { w . o . l . g . } , 0 \leq \theta _ { i } \leq 2 \pi )$ that the range of $\varPsi _ { i j }$ is closed and bounded, hence, compact in Euclidean N-space. The claim is thus clear.

Appendix B. Data for line capacities, cost and demand functions

See Tables 6–11.

T<sub>a</sub>bl<sub>e</sub> 6 Li<sub>ne</sub> <sub>capac</sub>iti<sub>es</sub> f<sub>or</sub> t<sub>es</sub>t <sub>se</sub>t- 1

<table><tr><td>No.</td><td> $\overline{P}_{12}$ </td><td> $\overline{P}_{14}$ </td><td> $\overline{P}_{15}$ </td><td> $\overline{P}_{23}$ </td><td> $\overline{P}_{24}$ </td><td> $\overline{P}_{25}$ </td><td> $\overline{P}_{26}$ </td><td> $\overline{P}_{35}$ </td><td> $\overline{P}_{36}$ </td><td> $\overline{P}_{45}$ </td><td> $\overline{P}_{56}$ </td></tr><tr><td>1</td><td>244.5</td><td>264.7</td><td>207.1</td><td>23.9</td><td>72.2</td><td>269.8</td><td>177.9</td><td>234.9</td><td>129.1</td><td>67.6</td><td>308.2</td></tr><tr><td>2</td><td>285.3</td><td>206.7</td><td>124.7</td><td>6.0</td><td>230.6</td><td>298.3</td><td>160.1</td><td>171.9</td><td>118.8</td><td>308.2</td><td>89.3</td></tr><tr><td>3</td><td>117.9</td><td>22.6</td><td>59.5</td><td>104.4</td><td>164.2</td><td>202.3</td><td>375.7</td><td>71.4</td><td>440.5</td><td>94.3</td><td>347.2</td></tr><tr><td>4</td><td>152.2</td><td>53.2</td><td>289.6</td><td>84.0</td><td>285.8</td><td>45.0</td><td>254.0</td><td>114.2</td><td>167.7</td><td>223.6</td><td>330.7</td></tr><tr><td>5</td><td>318.2</td><td>287.8</td><td>65.8</td><td>292.9</td><td>269.1</td><td>26.3</td><td>238.9</td><td>89.6</td><td>11.0</td><td>288.0</td><td>112.2</td></tr><tr><td>6</td><td>152.9</td><td>79.4</td><td>236.1</td><td>160.9</td><td>70.2</td><td>164.4</td><td>249.3</td><td>277.0</td><td>214.5</td><td>100.4</td><td>295.1</td></tr><tr><td>7</td><td>6.1</td><td>234.2</td><td>328.4</td><td>310.9</td><td>88.1</td><td>22.0</td><td>229.6</td><td>8.9</td><td>347.2</td><td>190.5</td><td>234.1</td></tr><tr><td>8</td><td>191.8</td><td>143.7</td><td>180.1</td><td>296.6</td><td>191.6</td><td>146.4</td><td>244.8</td><td>277.0</td><td>120.3</td><td>201.4</td><td>6.4</td></tr><tr><td>9</td><td>90.9</td><td>67.7</td><td>97.0</td><td>19.7</td><td>6.8</td><td>55.5</td><td>7.3</td><td>20.1</td><td>27.4</td><td>97.9</td><td>9.7</td></tr><tr><td>10</td><td>25.9</td><td>13.9</td><td>5.7</td><td>44.0</td><td>63.3</td><td>71.2</td><td>70.3</td><td>66.2</td><td>2.6</td><td>77.5</td><td>59.5</td></tr><tr><td>11</td><td>26.8</td><td>3.0</td><td>64.5</td><td>68.8</td><td>30.9</td><td>51.4</td><td>46.2</td><td>52.9</td><td>18.2</td><td>70.0</td><td>67.4</td></tr><tr><td>12</td><td>22.6</td><td>66.2</td><td>56.1</td><td>31.6</td><td>7.5</td><td>56.3</td><td>48.9</td><td>35.1</td><td>70.0</td><td>35.5</td><td>70.2</td></tr><tr><td>13</td><td>79.8</td><td>62.9</td><td>38.1</td><td>45.6</td><td>41.5</td><td>15.2</td><td>71.8</td><td>29.7</td><td>33.3</td><td>53.0</td><td>29.1</td></tr><tr><td>14</td><td>49.7</td><td>44.5</td><td>72.5</td><td>16.4</td><td>0.3</td><td>52.2</td><td>21.9</td><td>85.6</td><td>64.6</td><td>13.2</td><td>79.1</td></tr><tr><td>15</td><td>25.2</td><td>38.7</td><td>34.3</td><td>51.7</td><td>28.4</td><td>76.8</td><td>84.7</td><td>93.9</td><td>9.8</td><td>22.1</td><td>34.5</td></tr><tr><td>16</td><td>58.2</td><td>65.3</td><td>41.8</td><td>26.4</td><td>44.3</td><td>17.8</td><td>45.9</td><td>23.0</td><td>44.7</td><td>63.3</td><td>69.3</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 7  
C<sub>os</sub>t f<sub>unc</sub>ti<sub>ons an</sub>d d<sub>eman</sub>d f<sub>unc</sub>ti<sub>ons</sub> f<sub>or</sub> t<sub>es</sub>t <sub>se</sub>t- 1

<table><tr><td>No.</td><td> $b_1$ </td><td> $β_1$ </td><td> $b_2$ </td><td> $β_2$ </td><td> $b_3$ </td><td> $β_3$ </td><td> $a_4$ </td><td> $b_4$ </td><td> $a_5$ </td><td> $b_5$ </td><td> $a_6$ </td><td> $b_6$ </td></tr><tr><td>1</td><td>2265.8</td><td>25.3</td><td>2012.6</td><td>30.4</td><td>1759.5</td><td>35.4</td><td>183.3</td><td>0.2</td><td>537.0</td><td>0.2</td><td>279.7</td><td>0.3</td></tr><tr><td>2</td><td>2396.2</td><td>27.9</td><td>2117.0</td><td>33.5</td><td>1837.7</td><td>39.1</td><td>423.5</td><td>0.2</td><td>237.9</td><td>0.5</td><td>338.6</td><td>0.1</td></tr><tr><td>3</td><td>2375.4</td><td>27.5</td><td>2100.3</td><td>33.0</td><td>1825.2</td><td>38.5</td><td>455.6</td><td>0.1</td><td>734.1</td><td>0.1</td><td>310.3</td><td>0.4</td></tr><tr><td>4</td><td>2430.2</td><td>28.6</td><td>2144.2</td><td>34.3</td><td>1858.1</td><td>40.0</td><td>500.0</td><td>0.3</td><td>276.3</td><td>0.2</td><td>723.6</td><td>0.2</td></tr><tr><td>5</td><td>1640.7</td><td>12.8</td><td>1512.5</td><td>15.4</td><td>1384.4</td><td>17.9</td><td>494.1</td><td>0.1</td><td>268.3</td><td>0.5</td><td>237.6</td><td>0.1</td></tr><tr><td>6</td><td>1511.7</td><td>10.2</td><td>1409.3</td><td>12.3</td><td>1307.0</td><td>14.3</td><td>108.5</td><td>0.3</td><td>503.1</td><td>0.3</td><td>388.5</td><td>0.2</td></tr><tr><td>7</td><td>1521.1</td><td>10.4</td><td>1416.9</td><td>12.5</td><td>1312.7</td><td>14.6</td><td>17.5</td><td>0.3</td><td>399.2</td><td>0.1</td><td>1083.3</td><td>0.2</td></tr><tr><td>8</td><td>1543.1</td><td>10.9</td><td>1434.5</td><td>13.0</td><td>1325.8</td><td>15.2</td><td>222.0</td><td>0.3</td><td>211.3</td><td>0.4</td><td>1066.7</td><td>0.1</td></tr><tr><td>9</td><td>2424.6</td><td>28.5</td><td>2139.7</td><td>34.2</td><td>1854.8</td><td>39.9</td><td>366.0</td><td>0.2</td><td>194.0</td><td>0.2</td><td>440.0</td><td>0.2</td></tr><tr><td>10</td><td>2456.9</td><td>29.1</td><td>2165.5</td><td>35.0</td><td>1874.1</td><td>40.8</td><td>111.1</td><td>0.4</td><td>546.3</td><td>0.1</td><td>342.6</td><td>0.3</td></tr><tr><td>11</td><td>2348.7</td><td>27.0</td><td>2079.0</td><td>32.4</td><td>1809.2</td><td>37.8</td><td>558.1</td><td>0.3</td><td>400.2</td><td>0.2</td><td>541.6</td><td>0.2</td></tr><tr><td>12</td><td>2337.3</td><td>26.7</td><td>2069.8</td><td>32.1</td><td>1802.4</td><td>37.4</td><td>643.0</td><td>0.2</td><td>287.0</td><td>0.2</td><td>570.0</td><td>0.3</td></tr><tr><td>13</td><td>1609.3</td><td>12.2</td><td>1487.4</td><td>14.6</td><td>1365.6</td><td>17.1</td><td>503.5</td><td>0.1</td><td>119.3</td><td>0.3</td><td>377.2</td><td>0.2</td></tr><tr><td>14</td><td>1521.4</td><td>10.4</td><td>1417.1</td><td>12.5</td><td>1312.8</td><td>14.6</td><td>194.1</td><td>0.3</td><td>417.0</td><td>0.2</td><td>388.9</td><td>0.4</td></tr><tr><td>15</td><td>1576.5</td><td>11.5</td><td>1461.2</td><td>13.8</td><td>1345.9</td><td>16.1</td><td>452.3</td><td>0.1</td><td>332.1</td><td>0.4</td><td>715.6</td><td>0.1</td></tr><tr><td>16</td><td>1597.3</td><td>11.9</td><td>1477.8</td><td>14.3</td><td>1358.4</td><td>16.7</td><td>1137.1</td><td>0.2</td><td>140.5</td><td>0.2</td><td>222.5</td><td>0.4</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 8 Li<sub>ne</sub> <sub>capac</sub>iti<sub>es</sub> f<sub>or</sub> t<sub>es</sub>t <sub>se</sub>t-2

<table><tr><td>No.</td><td> $\overline{P}_{12}$ </td><td> $\overline{P}_{14}$ </td><td> $\overline{P}_{15}$ </td><td> $\overline{P}_{23}$ </td><td> $\overline{P}_{24}$ </td><td> $\overline{P}_{25}$ </td><td> $\overline{P}_{26}$ </td><td> $\overline{P}_{35}$ </td><td> $\overline{P}_{36}$ </td><td> $\overline{P}_{45}$ </td><td> $\overline{P}_{56}$ </td></tr><tr><td>1</td><td>185.3</td><td>179.5</td><td>61.9</td><td>132.6</td><td>188.9</td><td>66.9</td><td>374.7</td><td>258.6</td><td>247.6</td><td>10.9</td><td>292.9</td></tr><tr><td>2</td><td>290.9</td><td>90.0</td><td>102.6</td><td>361.3</td><td>221.5</td><td>361.1</td><td>32.2</td><td>102.6</td><td>27.9</td><td>230.3</td><td>179.7</td></tr><tr><td>3</td><td>55.9</td><td>180.9</td><td>232.6</td><td>99.8</td><td>162.4</td><td>134.2</td><td>297.7</td><td>211.5</td><td>311.1</td><td>303.7</td><td>10.2</td></tr><tr><td>4</td><td>228.3</td><td>104.2</td><td>271.8</td><td>141.7</td><td>137.8</td><td>18.5</td><td>420.9</td><td>125.8</td><td>286.1</td><td>236.9</td><td>28.0</td></tr><tr><td>5</td><td>318.6</td><td>102.8</td><td>274.9</td><td>240.5</td><td>52.2</td><td>42.8</td><td>93.8</td><td>271.3</td><td>237.0</td><td>84.0</td><td>282.1</td></tr><tr><td>6</td><td>159.8</td><td>113.2</td><td>239.9</td><td>263.2</td><td>36.8</td><td>169.7</td><td>164.7</td><td>282.3</td><td>62.6</td><td>226.6</td><td>281.1</td></tr><tr><td>7</td><td>256.8</td><td>76.5</td><td>73.1</td><td>285.0</td><td>19.4</td><td>99.7</td><td>162.3</td><td>288.6</td><td>274.4</td><td>280.8</td><td>183.3</td></tr><tr><td>8</td><td>66.1</td><td>271.8</td><td>284.8</td><td>195.9</td><td>147.4</td><td>253.5</td><td>35.1</td><td>148.8</td><td>75.3</td><td>292.0</td><td>229.3</td></tr><tr><td>9</td><td>47.6</td><td>59.2</td><td>7.7</td><td>87.2</td><td>68.4</td><td>54.7</td><td>61.9</td><td>16.8</td><td>26.6</td><td>10.8</td><td>59.1</td></tr><tr><td>10</td><td>97.7</td><td>15.4</td><td>50.6</td><td>97.6</td><td>44.1</td><td>10.4</td><td>86.3</td><td>53.8</td><td>11.0</td><td>27.6</td><td>5.5</td></tr><tr><td>11</td><td>60.0</td><td>23.8</td><td>51.4</td><td>12.8</td><td>44.4</td><td>58.2</td><td>13.0</td><td>71.2</td><td>66.7</td><td>83.9</td><td>14.5</td></tr><tr><td>12</td><td>79.0</td><td>7.7</td><td>89.6</td><td>11.5</td><td>33.9</td><td>27.4</td><td>6.9</td><td>59.1</td><td>22.8</td><td>86.2</td><td>75.9</td></tr><tr><td>13</td><td>18.3</td><td>56.4</td><td>47.6</td><td>67.8</td><td>57.7</td><td>61.3</td><td>51.7</td><td>16.9</td><td>48.6</td><td>0.6</td><td>73.0</td></tr><tr><td>14</td><td>45.8</td><td>2.8</td><td>70.0</td><td>72.3</td><td>3.2</td><td>62.6</td><td>18.4</td><td>71.1</td><td>95.9</td><td>46.7</td><td>11.1</td></tr><tr><td>15</td><td>30.1</td><td>79.2</td><td>77.3</td><td>11.5</td><td>21.7</td><td>76.1</td><td>96.2</td><td>48.9</td><td>47.0</td><td>8.3</td><td>3.7</td></tr><tr><td>16</td><td>46.5</td><td>60.6</td><td>32.9</td><td>94.1</td><td>25.9</td><td>75.1</td><td>46.3</td><td>24.5</td><td>11.4</td><td>24.0</td><td>58.7</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 9  
C<sub>os</sub>t f<sub>unc</sub>ti<sub>ons an</sub>d d<sub>eman</sub>d f<sub>unc</sub>ti<sub>ons</sub> f<sub>or</sub> t<sub>es</sub>t <sub>se</sub>t-2

<table><tr><td>No.</td><td> $b_1$ </td><td> $β_1$ </td><td> $b_2$ </td><td> $β_2$ </td><td> $b_3$ </td><td> $β_3$ </td><td> $a_4$ </td><td> $b_4$ </td><td> $a_5$ </td><td> $b_5$ </td><td> $a_6$ </td><td> $b_6$ </td></tr><tr><td>1</td><td>2299.8</td><td>26.0</td><td>2039.8</td><td>31.2</td><td>1779.9</td><td>36.4</td><td>92.8</td><td>0.1</td><td>386.3</td><td>0.3</td><td>520.9</td><td>0.3</td></tr><tr><td>2</td><td>2375.1</td><td>27.5</td><td>2100.1</td><td>33.0</td><td>1825.1</td><td>38.5</td><td>219.1</td><td>0.4</td><td>409.6</td><td>0.1</td><td>371.3</td><td>0.4</td></tr><tr><td>3</td><td>2364.6</td><td>27.3</td><td>2091.6</td><td>32.7</td><td>1818.7</td><td>38.2</td><td>343.5</td><td>0.3</td><td>622.6</td><td>0.3</td><td>534.0</td><td>0.1</td></tr><tr><td>4</td><td>2331.7</td><td>26.6</td><td>2065.4</td><td>32.0</td><td>1799.0</td><td>37.3</td><td>778.1</td><td>0.2</td><td>313.8</td><td>0.3</td><td>408.1</td><td>0.3</td></tr><tr><td>5</td><td>1750.0</td><td>15.0</td><td>1600.0</td><td>18.0</td><td>1450.0</td><td>21.0</td><td>499.2</td><td>0.3</td><td>188.3</td><td>0.2</td><td>312.6</td><td>0.1</td></tr><tr><td>6</td><td>1641.5</td><td>12.8</td><td>1513.2</td><td>15.4</td><td>1384.9</td><td>18.0</td><td>393.4</td><td>0.3</td><td>415.8</td><td>0.2</td><td>190.8</td><td>0.3</td></tr><tr><td>7</td><td>1576.7</td><td>11.5</td><td>1461.4</td><td>13.8</td><td>1346.0</td><td>16.1</td><td>500.3</td><td>0.1</td><td>456.1</td><td>0.1</td><td>543.6</td><td>0.5</td></tr><tr><td>8</td><td>1565.6</td><td>11.3</td><td>1452.5</td><td>13.6</td><td>1339.4</td><td>15.8</td><td>575.5</td><td>0.3</td><td>556.7</td><td>0.1</td><td>367.8</td><td>0.3</td></tr><tr><td>9</td><td>2261.1</td><td>25.2</td><td>2008.9</td><td>30.3</td><td>1756.7</td><td>35.3</td><td>389.8</td><td>0.4</td><td>173.2</td><td>0.1</td><td>437.0</td><td>0.2</td></tr><tr><td>10</td><td>2260.2</td><td>25.2</td><td>2008.2</td><td>30.2</td><td>1756.1</td><td>35.3</td><td>49.0</td><td>0.2</td><td>269.3</td><td>0.3</td><td>681.6</td><td>0.4</td></tr><tr><td>11</td><td>2401.8</td><td>28.0</td><td>2121.4</td><td>33.6</td><td>1841.1</td><td>39.3</td><td>572.4</td><td>0.2</td><td>329.8</td><td>0.3</td><td>597.7</td><td>0.1</td></tr><tr><td>12</td><td>2337.0</td><td>26.7</td><td>2069.6</td><td>32.1</td><td>1802.2</td><td>37.4</td><td>264.0</td><td>0.4</td><td>787.6</td><td>0.2</td><td>448.4</td><td>0.2</td></tr><tr><td>13</td><td>1575.9</td><td>11.5</td><td>1460.7</td><td>13.8</td><td>1345.5</td><td>16.1</td><td>144.8</td><td>0.2</td><td>803.8</td><td>0.2</td><td>51.4</td><td>0.1</td></tr><tr><td>14</td><td>1620.4</td><td>12.4</td><td>1496.3</td><td>14.9</td><td>1372.2</td><td>17.4</td><td>397.3</td><td>0.2</td><td>130.5</td><td>0.3</td><td>472.2</td><td>0.3</td></tr><tr><td>15</td><td>1707.5</td><td>14.1</td><td>1566.0</td><td>17.0</td><td>1424.5</td><td>19.8</td><td>489.8</td><td>0.2</td><td>905.4</td><td>0.2</td><td>104.8</td><td>0.2</td></tr><tr><td>16</td><td>1609.6</td><td>12.2</td><td>1487.7</td><td>14.6</td><td>1365.7</td><td>17.1</td><td>738.6</td><td>0.4</td><td>396.7</td><td>0.2</td><td>364.7</td><td>0.2</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 1 0  
Li<sub>ne</sub> <sub>capac</sub>iti<sub>es</sub> f<sub>or</sub> t<sub>es</sub>t <sub>se</sub>t- 3

<table><tr><td>No.</td><td> $\overline{P}_{12}$ </td><td> $\overline{P}_{14}$ </td><td> $\overline{P}_{15}$ </td><td> $\overline{P}_{23}$ </td><td> $\overline{P}_{24}$ </td><td> $\overline{P}_{25}$ </td><td> $\overline{P}_{26}$ </td><td> $\overline{P}_{35}$ </td><td> $\overline{P}_{36}$ </td><td> $\overline{P}_{45}$ </td><td> $\overline{P}_{56}$ </td></tr><tr><td>1</td><td>252.9</td><td>113.8</td><td>82.9</td><td>67.1</td><td>149.5</td><td>311.2</td><td>276.0</td><td>82.9</td><td>195.3</td><td>342.1</td><td>126.3</td></tr><tr><td>2</td><td>256.8</td><td>286.0</td><td>23.9</td><td>405.5</td><td>108.8</td><td>1.3</td><td>27.6</td><td>359.0</td><td>17.3</td><td>181.5</td><td>332.3</td></tr><tr><td>3</td><td>165.9</td><td>161.5</td><td>199.8</td><td>130.9</td><td>113.1</td><td>270.0</td><td>92.9</td><td>141.0</td><td>254.5</td><td>229.1</td><td>241.2</td></tr><tr><td>4</td><td>230.8</td><td>137.8</td><td>106.3</td><td>211.1</td><td>222.8</td><td>243.3</td><td>222.4</td><td>144.7</td><td>253.5</td><td>130.3</td><td>97.1</td></tr><tr><td>5</td><td>33.6</td><td>182.3</td><td>249.7</td><td>108.0</td><td>330.6</td><td>334.1</td><td>167.1</td><td>6.2</td><td>61.9</td><td>214.8</td><td>311.9</td></tr><tr><td>6</td><td>528.1</td><td>373.7</td><td>127.3</td><td>153.7</td><td>40.7</td><td>46.5</td><td>192.5</td><td>167.3</td><td>41.4</td><td>54.2</td><td>274.7</td></tr><tr><td>7</td><td>37.0</td><td>169.9</td><td>293.1</td><td>0.6</td><td>33.3</td><td>384.7</td><td>312.1</td><td>13.5</td><td>275.8</td><td>89.8</td><td>390.2</td></tr><tr><td>8</td><td>14.1</td><td>89.9</td><td>299.6</td><td>80.8</td><td>410.8</td><td>20.7</td><td>62.6</td><td>374.3</td><td>433.2</td><td>164.5</td><td>49.5</td></tr><tr><td>9</td><td>14.3</td><td>68.3</td><td>73.7</td><td>12.8</td><td>15.3</td><td>80.6</td><td>13.3</td><td>22.1</td><td>84.4</td><td>44.6</td><td>70.7</td></tr><tr><td>10</td><td>31.7</td><td>64.2</td><td>47.9</td><td>72.3</td><td>67.3</td><td>55.7</td><td>42.4</td><td>38.4</td><td>14.3</td><td>47.8</td><td>18.1</td></tr><tr><td>11</td><td>1.3</td><td>57.3</td><td>96.8</td><td>57.1</td><td>37.8</td><td>6.6</td><td>98.6</td><td>4.3</td><td>50.4</td><td>13.3</td><td>76.4</td></tr><tr><td>12</td><td>14.5</td><td>34.0</td><td>52.4</td><td>31.4</td><td>44.8</td><td>115.9</td><td>45.6</td><td>92.4</td><td>12.9</td><td>30.8</td><td>25.3</td></tr><tr><td>13</td><td>8.4</td><td>6.1</td><td>49.4</td><td>65.0</td><td>24.8</td><td>3.1</td><td>107.9</td><td>79.9</td><td>50.0</td><td>57.0</td><td>48.4</td></tr><tr><td>14</td><td>23.7</td><td>0.2</td><td>57.0</td><td>56.7</td><td>75.0</td><td>58.2</td><td>27.4</td><td>35.1</td><td>32.9</td><td>67.3</td><td>66.5</td></tr><tr><td>15</td><td>34.4</td><td>77.3</td><td>46.5</td><td>71.0</td><td>40.0</td><td>76.8</td><td>25.5</td><td>21.3</td><td>36.9</td><td>52.6</td><td>17.6</td></tr><tr><td>16</td><td>81.6</td><td>49.2</td><td>10.3</td><td>68.0</td><td>66.3</td><td>13.1</td><td>34.5</td><td>5.6</td><td>68.7</td><td>54.9</td><td>47.8</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 1 1  
C<sub>os</sub>t f<sub>unc</sub>ti<sub>ons an</sub>d d<sub>eman</sub>d f<sub>unc</sub>ti<sub>ons</sub> f<sub>or</sub> t<sub>es</sub>t <sub>se</sub>t-3

<table><tr><td>No.</td><td> $b_1$ </td><td> $β_1$ </td><td> $b_2$ </td><td> $β_2$ </td><td> $b_3$ </td><td> $β_3$ </td><td> $a_4$ </td><td> $b_4$ </td><td> $a_5$ </td><td> $b_5$ </td><td> $a_6$ </td><td> $b_6$ </td></tr><tr><td>1</td><td>2255.0</td><td>25.1</td><td>2004.0</td><td>30.1</td><td>1753.0</td><td>35.1</td><td>137.6</td><td>0.1</td><td>413.1</td><td>0.4</td><td>449.3</td><td>0.2</td></tr><tr><td>2</td><td>2462.7</td><td>29.3</td><td>2170.2</td><td>35.1</td><td>1877.6</td><td>41.0</td><td>254.1</td><td>0.5</td><td>477.0</td><td>0.2</td><td>268.9</td><td>0.1</td></tr><tr><td>3</td><td>2352.9</td><td>27.1</td><td>2082.3</td><td>32.5</td><td>1811.7</td><td>37.9</td><td>923.0</td><td>0.2</td><td>162.6</td><td>0.1</td><td>414.4</td><td>0.3</td></tr><tr><td>4</td><td>2266.4</td><td>25.3</td><td>2013.1</td><td>30.4</td><td>1759.8</td><td>35.5</td><td>1114.8</td><td>0.1</td><td>141.7</td><td>0.3</td><td>243.5</td><td>0.4</td></tr><tr><td>5</td><td>1662.9</td><td>13.3</td><td>1530.3</td><td>15.9</td><td>1397.8</td><td>18.6</td><td>543.6</td><td>0.3</td><td>324.5</td><td>0.2</td><td>131.9</td><td>0.1</td></tr><tr><td>6</td><td>1631.0</td><td>12.6</td><td>1504.8</td><td>15.1</td><td>1378.6</td><td>17.7</td><td>285.8</td><td>0.1</td><td>418.1</td><td>0.1</td><td>296.2</td><td>0.6</td></tr><tr><td>7</td><td>1533.1</td><td>10.7</td><td>1426.5</td><td>12.8</td><td>1319.8</td><td>14.9</td><td>658.3</td><td>0.3</td><td>189.6</td><td>0.3</td><td>652.2</td><td>0.1</td></tr><tr><td>8</td><td>1641.8</td><td>12.8</td><td>1513.4</td><td>15.4</td><td>1385.1</td><td>18.0</td><td>639.1</td><td>0.3</td><td>780.2</td><td>0.4</td><td>80.7</td><td>0.2</td></tr><tr><td>9</td><td>2304.2</td><td>26.1</td><td>2043.4</td><td>31.3</td><td>1782.5</td><td>36.5</td><td>183.4</td><td>0.3</td><td>145.3</td><td>0.2</td><td>671.4</td><td>0.1</td></tr><tr><td>10</td><td>2479.1</td><td>29.6</td><td>2183.3</td><td>35.5</td><td>1887.5</td><td>41.4</td><td>352.4</td><td>0.2</td><td>501.8</td><td>0.3</td><td>145.8</td><td>0.3</td></tr><tr><td>11</td><td>2391.2</td><td>27.8</td><td>2113.0</td><td>33.4</td><td>1834.7</td><td>39.0</td><td>719.5</td><td>0.4</td><td>666.0</td><td>0.1</td><td>114.5</td><td>0.1</td></tr><tr><td>12</td><td>2293.3</td><td>25.9</td><td>2034.7</td><td>31.0</td><td>1776.0</td><td>36.2</td><td>411.0</td><td>0.2</td><td>510.2</td><td>0.4</td><td>578.8</td><td>0.3</td></tr><tr><td>13</td><td>1652.1</td><td>13.0</td><td>1521.7</td><td>15.6</td><td>1391.2</td><td>18.3</td><td>398.8</td><td>0.1</td><td>308.1</td><td>0.3</td><td>293.1</td><td>0.2</td></tr><tr><td>14</td><td>1717.2</td><td>14.3</td><td>1573.7</td><td>17.2</td><td>1430.3</td><td>20.1</td><td>289.6</td><td>0.4</td><td>268.8</td><td>0.3</td><td>441.6</td><td>0.1</td></tr><tr><td>15</td><td>1597.6</td><td>12.0</td><td>1478.1</td><td>14.3</td><td>1358.5</td><td>16.7</td><td>56.3</td><td>0.1</td><td>1151.6</td><td>0.3</td><td>292.0</td><td>0.2</td></tr><tr><td>16</td><td>1619.5</td><td>12.4</td><td>1495.6</td><td>14.9</td><td>1371.7</td><td>17.3</td><td>329.8</td><td>0.1</td><td>881.2</td><td>0.4</td><td>289.1</td><td>0.3</td></tr></table>

## References

<sup>w</sup> <sup>x</sup>1 F. Allen, R. Karjalainen, Using genetic algorithms to find technical trading rules, Journal of Financial Economics 51 Ž . Ž . 2 1999 245–271.

<sup>w</sup> <sup>x</sup> 2 J. Alstrup, S. Boas, O. Madsen, R. Vidal, Booking policy for flight with two types of passengers, European Journal of Operations Research 27 1986 274–288. Ž .

<sup>w</sup> <sup>x</sup> 3 T. Back, Evolutionary Algorithms in Theory and Practice, ¨ Oxford Univ. Press, 1996.

<sup>w</sup> <sup>x</sup> 4 P. Belobaba, Applications of a probabilistic decision model to airline seat inventory control, Operations Research 37 Ž . 1989 183–197.

<sup>w</sup> <sup>x</sup> 5 J. Bushnell, S. Stoft, Electric grid investment under a contract network regime, Journal of Regulated Economics 10 1Ž . Ž .1996 61–79.

<sup>w</sup> <sup>x</sup> 6 H. Chao, H. Huntington Eds. , Designing Competitive Elec- Ž . tricity Markets, Kluwer Academic Publishers, Boston, 1998.

<sup>w</sup> <sup>x</sup> 7 H. Chao, S. Peck, A market mechanism for electric power transmission, Journal of Regulated Economics 10 1 1996Ž . Ž . 25–59.

<sup>w</sup> <sup>x</sup> 8 C. Bessiere, Arc-consistency in dynamic constraint satisfac-\` tion problems, in: Proceedings of the 9th National Conference on Artificial Intelligence AAAI-91 , Vol. 1, AAAIŽ . Press<sup>r</sup>MIT Press, Menlo Park, CA, pp. 221–226.

<sup>w</sup> <sup>x</sup> 9 M. Crew, P. Kleindorfer, The Economics of Public Utility Regulation, The MIT Press, Cambridge, 1986.

<sup>w</sup> <sup>x</sup> 10 M. Crew, P. Kleindorfer, The Economics of Postal Service, Kluwer Academic Publishers, Boston, 1992.

<sup>w</sup> <sup>x</sup> 11 M. Crew, P. Kleindorfer Eds. , Emerging Competition inŽ . Postal and Delivery Services, Kluwer Academic Publishers, Boston, 1999.

<sup>w</sup> <sup>x</sup> 12 L. Davis Ed. , Genetic Algorithms and Simulated Anneal-Ž . ing, Pitman, London, 1987.

<sup>w</sup> <sup>x</sup> 13 L. Davis, Adapting operator probabilities in genetic algorithms, in: J. Schaffer Ed. , Proceedings of the 3rd Interna- Ž . tional Conference on Genetic Algorithms, Morgan Kaufmann, 1989, pp. 61–69.

<sup>w</sup> <sup>x</sup> 14 Decision Support Systems, Robert Thomas Guest Editor ,Ž . Special Issue: Restructuring the Electric Power Business — A New Paradigm for Reducing Regulation, Vol. 24, 1999.

<sup>w</sup> <sup>x</sup> 15 O. Elgerd, Electric Energy Systems and Theory, 2nd edn., McGraw-Hill, New York, 1982.

<sup>w</sup> <sup>x</sup> 16 G. Faulhaber, Pricing internet: the efficient subsidy, in: B. Kalin Ed. , Building Information Infrastructure, McGraw-Ž . Hill, New York, 1992.

<sup>w</sup> <sup>x</sup> 17 E. Freuder, Eliminating interchangeable values in constraint satisfaction problems, in: Proceedings of the 9th National Conference on Artificial Intelligence AAAI-91 , Vol. 1,Ž . AAAI Press<sup>r</sup>MIT Press, Menlo Park, CA, pp. 227–233.

<sup>w</sup> <sup>x</sup> 18 GAMS, The Solver Manuals, GAMS Development Corporation, 1993.

<sup>w</sup> <sup>x</sup> 19 P. Harker, Lectures on computation of equilibria with equation-based methods, Louvain-La-Neuve Belgium : COREŽ . Foundation, Universite catholique de Louvain, 1993.

<sup>w</sup> <sup>x</sup> 20 P. Harker, T. Friesz, The use of equilibrium network models

in logistics management: with applications to U.S. Coal Industry, Transportation Research 5 1985 457–470.Ž .

<sup>w</sup> <sup>x</sup> 21 R. Hartl, A Global Convergence Proof for a Class of Genetic Algorithms, Technische Universitat Wien, 1990.

<sup>w</sup> <sup>x</sup> 22 W. Hogan, Contract network for electric power transmission, Journal of Regulatory Economics 4 1992 211–242.Ž .

<sup>w</sup> <sup>x</sup> 23 J. Holland, Adaptation in Natural and Artificial Systems, The MIT Press, 1992.

<sup>w</sup> <sup>x</sup> 24 A. Homaifar, S.H. Lai, X. Qi, Constrained optimization via genetic algorithms, Simulation 62 4 1994 242–254.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 M. Illic, S. Liu, Hierarchical Power Systems Control: Its´ Value in a Changing Industry, Springer, London, 1996.

<sup>w</sup> <sup>x</sup> 26 J. Joines, C. Houck, On the use of non-stationary penalty functions to solve non-linear constrained optimization problems with GAS, in: Z. Michalewicz et al. Eds. , ProceedingsŽ . of the First IEEE International Conference on Evolutionary Computation, IEEE Press, 1994, pp. 579–584.

<sup>w</sup> <sup>x</sup> 27 P. Kleindorfer, D.-J. Wu, C. Fernando, Strategic gaming and the evolving electric power market, working paper, The Wharton School, University of Pennsylvania, 1997.

<sup>w</sup> <sup>x</sup> 28 P. Kleindorfer, D.-J. Wu, J.E. Zhang, Optimal long-term contracting in the deregulated electric power market, Decision Sciences Institute 1998 Proceedings, November, Las Vegas, Vol. 3, 1998, pp. 1645–1648.

<sup>w</sup> <sup>x</sup> 29 P. Lederer, Competitive delivered pricing and production, Regional Sciences and Urban Economics 24 1994 229–252.Ž .

<sup>w</sup> <sup>x</sup> 30 J. MacKie-Mason, H. Varian, Pricing the internet, prepared for the conference, Public Access to the Internet, JFK School of Government, Harvard University, May 1993.

<sup>w</sup> <sup>x</sup> 31 J. MacKie-Mason, H. Varian, Pricing congested network resources, Working Paper, University of Michigan, October 1994.

<sup>w</sup> <sup>x</sup> 32 Z. Michalewicz, Genetic Algorithms, Numerical Optimization and Constraints, in: Proceedings of the 6th International Conference on Genetic Algorithms, Morgan Kaufmann, 1995, pp. 151–158.

<sup>w</sup> <sup>x</sup> 33 Z. Michalewicz, Genetic Algorithms<sup>q</sup>Data Structures<sup>s</sup> Evolution Programs, 3rd edn., Springer, New-York, 1996.

<sup>w</sup> <sup>x</sup> 34 Z. Michalewicz, G. Nazhiyath, in: D. Fogel Ed. , GenocopŽ . III: A Co-evolutionary Algorithms for Numerical Optimization with Non-linear Constraints, IEEE Press, 1995, pp. 647–651.

<sup>w</sup> <sup>x</sup> 35 Z. Michalewicz, M. Schoenauer, Evolutionary algorithms for constrained parameter optimization problems, Evolutionary Computation 4 1 1996 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 36 S. Minton, M. Johnston, A. Philips, P. Laird, Solving largescale constraint satisfaction and scheduling problems using a heuristic repair method, in: Proceedings of the 9th National Conference on Artificial Intelligence AAAI-90 , Vol. 1,Ž . AAAI Press<sup>r</sup>MIT Press, Cambridge, MA, pp. 17–24.

<sup>w</sup> <sup>x</sup>37 S. Mittal, B. Falkenhainer, Dynamic constraint satisfaction problems, in: Proceedings of the 9th National Conference on Artificial Intelligence AAAI-90 , Vol. 1, AAAI PressŽ . <sup>r</sup>MIT Press, Cambridge, MA, pp. 25–32.

<sup>w</sup> <sup>x</sup> 38 H. Mendelson, S. Whang, Pricing for communication network service, Graduate School of Business, Stanford University, October 1994.

<sup>w</sup> <sup>x</sup> 39 G. Rudolph, Convergence analysis of canonical genetic algorithms, IEEE Transactions on Neural Networks 5 1 1994 .Ž . Ž .

40 H. Schwefel, Numerical Optimization of Computer Models, Wiley, New York, 1995.

<sup>w</sup> <sup>x</sup> 41 P. Surry, N. Radcliffe, I. Boyd, A multi-objective approach to constrained optimization of gas supply networks: the COMOGA method, in: T. Fogarty Ed. , Evolutionary Com-Ž . puting, 1995.

<sup>w</sup> <sup>x</sup> 42 A. Wood, B. Wollenberg, Power Generation, Operation, and Control, Wiley, New York, 1984.

<sup>w</sup> <sup>x</sup> 43 D.-J. Wu, On convergence of genetic algorithms, Working Paper, The Wharton School, University of Pennsylvania, 1993.

<sup>w</sup> <sup>x</sup> 44 D.-J. Wu, Using genetic algorithms to determine near-optimal pricing, investment and operating strategies in the electric power industry, PhD Dissertation, The Wharton School, University of Pennsylvania, 1997.

<sup>w</sup> <sup>x</sup> 45 D.-J. Wu, P. Kleindorfer, J.E. Zhang, Optimal bidding and contracting strategies for non-storable commodities, Working Paper, The Wharton School, University of Pennsylvania, January 1999.

<sup>w</sup> <sup>x</sup> 46 D.-J. Wu, Constraint programming applications in designing electronic agents: an experimental study, in: Proceedings of the 32nd Hawaii International Conference on System Science, HICSS-32, Hawaii, January 1999.

![](/api/attachments/5Z8XYEJ5/fulltext/images/2fac5230913a28eade820980cacafd0e78c15a97ed2637a1f594737ffa8601b1.jpg)

Dr. D.J. Wu is SAP Alliance Liaison and Assistant Professor of MIS at Bennett LeBow College of Business, Drexe University. Dr. Wu was a two-time winner of the SAP University Alliance Award 1998, 1999 . Working with hisŽ . colleagues, Dr. Wu initiated and successfully led the restructuring of Drexel’s MIS curriculum to integrate with ERP systems such as SAP R<sup>r</sup>3. This initiative got worldwide recognition and generated tremendous research grants.

Dr. Wu’s research interest lies in ERP and Electronic Commerce, Bidding and Contracting in Multi-agent Systems, and Genetic Algorithms. Dr. Wu obtained his MA and PhD from the Wharton School, BE in Computer Science and BE in Industrial Engineering from Tsinghua University in Beijing. Dr. Wu’s thesis was nominated for the best PhD dissertation for the 1998 Elwood Buffa National Dissertation Award Competition in the US.
