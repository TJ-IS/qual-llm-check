---
otero_id: 1734
otero_key: "ZS6BSZ76"
title: "A bi-level decision support system for uncertain network design with equilibrium flow"
authors: "Suh-Wen Chiou"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.12.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A bi-level decision support system for uncertain network design with equilibrium <sup>fl</sup>ow

Suh-Wen Chiou ⁎

Department of Information Management, National Dong Hwa University, Da Hsueh Rd., Shou-Feng, Hualien 97401, Taiwan

a r t i c l e i n f o

Article history: Received 16 September 2013 Received in revised form 12 October 2014 Accepted 1 December 2014 Available online 9 December 2014

Keywords: Bi-level decision support system Stackelberg game Equilibrium network <sup>fl</sup>ow Robust optimization

## a b s t r a c t

A bi-level decision support system (BDSS) is proposed for a normative road network design with uncertain travel demand. A bi-level decision support model with link capacity expansion is developed to simultaneously reduce travel delay to road users and mitigate vulnerability of road network. A tractable solution scheme for BDSS is developed. Due to some hierarchy in decision-making order of BDSS, a bi-level programming is employed. A riskaverse Stackelberg solution is established for a normative BDSS under travel demand uncertainty. Numerical computations are performed using a real-data road network. Computational results indicate that the proposed solution scheme can effectively improve a worst-case performance of BDSS with greater success while incurring a relatively slighter loss of optimality when compared to deterministic solutions at nominal condition. Particularly, our computation results showed that proposed solution becomes more attractive as the realization taken by unknown demand growth factor increases.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

For most urban traf<sup>fi</sup>c road networks, severe travel delays could be incurred by road travelers as a result of insuf<sup>fi</sup>cient provision of link capacity in the presence of travel demand surges and disruptive events. In this paper, a bi-level decision support system (BDSS) is proposed to cope with continuously growing travel demand and alleviate increasing traf<sup>fi</sup>c congestion via link capacity expansion. For a road network with uncertain travel demand, decision maker at upper level determines link capacity expansion with an objective of minimizing total travel time constrained by investment budget. The road users at lower level are supposed to minimize their journey travel time [1] from pairs of origin to destination through route choice for realization taken by unknown travel demand which is most unfavorable. The solution for the decision maker with precedence in decision can be regarded as a Stackelberg solution. The Stackelberg solution is an optimal strategy for the leader when road users react by playing optimally. A worstcase analysis is considered for a normative BDSS in the presence of unknown travel demand to mitigate vulnerability of road network. In this regard, a bi-level model is proposed for BDSS in order to effectively characterize a risk-averse Stackelberg equilibrium at worst case scenario.

In the presence of uncertainty there has been a growing number of research papers [2–8] investigating the performance reliability of networked system over past years. For instance, a spatial decision support system (SDSS) is developed in [5] to widely explore and examine the effects of different networked disruption scenarios. The proposed SDSS is helpful for decision makers in conveniently identifying critical network components and facilitate decisions about maintaining and enhancing network survivability. [7] also developed a network equilibrium model accounting for multi-criteria decision making behavior of various market participants for optimal pricing and resource allocation in a computational grid network. More recently, Burgholzer et al. [4] proposed a simulation tool for transportation network planners to support time-ef<sup>fi</sup>cient alternative route choice of carriers in intermodal transportation networks in case of disruption. Considering a network design with uncertain input data, there are two mostly commonly used approaches in literature: stochastic programming and robust optimization [9]. From the prospective of stochastic programming, given a known priori distribution of probabilities of uncertain data, there are a variety of approaches applied to road network design with uncertain demand [10–13]. A growing interest in robust optimization approach [14–23] has attracted various applications. For example, a scenariobased robust solution in [14] is presented for large-scaled network design in which a stochastic linear programming approach is employed ([18–20]). Assuming uncertain data bounded within some certain set, there are plenty research works ([21–23]) extending a robust optimization ([15–17]) to road network design with uncertain demand. However, regarding a road network with equilibrium <sup>fl</sup>ow in the presence of uncertain travel demand, to the best of author's knowledge there is very limited research work using a bi-level programming approach to tackle a hierarchical decision making problem. For a general bi-level problem, decision variables at the upper level are optimized subject to the solution of lower level problem. As is noted by [24–27], in most cases a solution of lower level problem is not mathematically explicit.

A bi-level program generally turns out to be a non-convex problem and computationally intractable. Because of the non-convexity, solution algorithms in [28–31] can simply solve a bi-level problem of modestsize only locally. As noted from literature in [32–34], the equilibrium <sup>fl</sup>ow at lower level is generally not differentiable at some point. The <sup>fi</sup>rst-order approximation for equilibrium <sup>fl</sup>ow may fail at these points. Therefore it would be preventive from direct use of the results in [35] for equilibrium <sup>fl</sup>ow. In this paper, we propose a novel and computationally tractable solution scheme based on recent work in sensitivity for generalized gradients [36–38] to solve BDSS in the presence of uncertain travel demand for equilibrium <sup>fl</sup>ow.

The contributions made from this paper are summarized as follows. Firstly, a bi-level decision support system (BDSS) is presented to determine optimal link capacity expansion for uncertain road network with equilibrium <sup>fl</sup>ow. A risk-averse Stackelberg equilibrium for a worst case scenario of system performance is established. The performance measure, maximized with respect to travel demand growth factor on the one hand, is minimized with respect to link capacity expansion in the presence of uncertain travel demand, on the other hand. In this regard, the worst-case performance measure serves as an upper bound estimate for link capacity expansion in the presence of a worst case travel demand. Secondly, a computationally tractable solution scheme is proposed for BDSS. To this end, a modi<sup>fi</sup>ed gradient-based approach using generalized gradients is presented. Thirdly, numerical computations are performed using a benchmark real-data road network with various initial data. The rest of the paper is organized as follows. Section 2 introduces a bi-level decision support system with a min– max model for equilibrium network <sup>fl</sup>ow. A bi-level programming approach is proposed. A risk-averse Stackelberg solution is characterized by a tractable computation scheme proposed in Section 3. Numerical computations are performed in Section 4 using a medium-size realdata road network with link capacity expansions. Conclusions for this paper and extensions of the proposed approach to topics of interest are brie<sup>fl</sup>y summarized in Section 5.

## 2. A BDSS problem formulation

A BDSS program is introduced for uncertain road network design with equilibrium <sup>fl</sup>ow. In the presence of uncertain travel demand, a BDSS with link capacity expansion can be regarded as a Stackelberg game. Both the decision maker with the leader at the upper level and road users with the followers at the lower level are trying to realize a best solution on their own with respect to some certain but generally different objectives. At the upper level the decision maker has the leadership in playing the game and can determine a set of robust link capacity expansions. The route choice chosen by users at the lower level for a worst-case realization taken by unknown demand strongly relies on link capacity expansion determined by decision maker at the upper level. That is, road users have to react optimally on decision maker's choice for a worst-case realization taken by unknown travel demand.

In the presence of uncertain demand, the solution for BDSS with equilibrium <sup>fl</sup>ow is considered as a risk-averse Stackelberg equilibrium. The constraints at the lower level can be de<sup>fi</sup>ned in part by a parametric variational inequality. Notation used for a BDSS with respect to link capacity expansion under uncertain travel demand is summarized <sup>fi</sup>rst.

## 2.1. Notation

$G ( N , L )$ a road network with node set N and link set L.

W a set of origin-destination (OD) pairs.

$R _ { w }$ a set of routes between OD pair $w , \forall w \in W .$

q a matrix of travel demand for OD pairs.

$\mu$ a set of OD demand growth factor, $\mu = [ \mu _ { w } ] , \forall w \in W .$

$k$ a vector of link current capacity, $k = [ k _ { a } ] , \forall a \in L .$

a vector of link capacity expansion upper bound, $\begin{array} { r } { u = [ u _ { a } ] , } \end{array}$ $\forall a \in L$

a vector of link capacity expansion, $y = [ y _ { a } ] , \forall a \in L$

f a vector of average link <sup>fl</sup>ow, $f = [ f _ { a } ] , \forall a \in L .$

$h$ vector of route <sup>fl</sup>ow between points of entry to points of exit from network, $h = [ h _ { p } ] , \forall p \in R _ { w } , \forall w \in W .$

$\lambda$ a link-route incidence matrix.

$\Lambda$ a OD-route incidence matrix.

$c ( y , f )$ a vector of link <sup>fl</sup>ow travel cost, $c = [ c _ { a } ( y _ { a } , f ) ] , \forall a \in L .$

π a vector of minimum travel cost between OD pair $w , \forall w \in W ,$ $\pi = [ \pi _ { w } ] .$

a vector of route <sup>fl</sup>ow travel cost, $C = [ C _ { p } ] , \forall p \in R _ { w } , \forall w \in W .$

$V ( y )$ a vector of link capacity expansion investment cost, $V ( y ) =$ $[ V _ { a } ( y _ { a } ) ] , \forall a \in L$

a conversion factor from investment cost to travel cost.

## 2.2. A lower level problem

A user equilibrium <sup>fl</sup>ow at the lower level in BDSS can be identi<sup>fi</sup>ed by a variational inequality as follows. Let K denote a feasible set for network <sup>fl</sup>ow, i.e.

$$
K = \{f: f = \lambda h, \Lambda h = q, h \geq 0 \}.\tag{1}
$$

According to [39], a user equilibrium <sup>fl</sup>ow can be characterized if and only if for every ${ \overline { { f } } } \in K$ there exists $\mathsf { a } f \in K$ such that

$$
c (f) (\overline {{f}} - f) \geq 0.\tag{2}
$$

For a BDSS with a set of link capacity expansion y in the presence of a realization taken by unknown demand growth factor μ, a responding user equilibrium <sup>fl</sup>ow $f ( \mu , y )$ can be characterized in the following way. Let $K ( \mu )$ denote a feasible set for a parametric user equilibrium <sup>fl</sup>ow with respect to some realization taken by unknown future demand growth factor $\mu$ we have

$$
K (\mu) = \{f: f = \lambda h, \Lambda h = \mu q, h \geq 0 \}.\tag{3}
$$

Therefore a parametric user equilibrium <sup>fl</sup>ow with demand growth factor μ can be characterized if and only if for every $\scriptstyle { \overline { { f } } } \in K ( \mu )$ there exists $\mathsf { a } f ( \mu , y ) \in K ( \mu )$ such that

$$
c (y, f) (\overline {{f}} - f) \geq 0.\tag{4}
$$

Let $\Omega _ { f } ( \mu , y )$ denote a solution set determined by $\operatorname { E q . } \left( 4 \right)$ consisting of responding <sup>fl</sup>ow $f ( \mu , y )$ to a set of link capacity expansion y, i.e.

$$
f (\mu , y) \in \Omega_ {f} (\mu , y).\tag{5}
$$

Both link capacity expansion $y ^ { * }$ and travel demand growth factor μ<sup>∗</sup> can be determined by a bi-level program such that a pair of saddle points $( \mu ^ { * } , \boldsymbol { y } ^ { * } )$ exists. Let $Z _ { 0 } ( \mu , y , f )$ denote an objective function for a BDSS with equilibrium <sup>fl</sup>ow f. A Stackelberg solution $( \mu ^ { * } , y ^ { * } )$ is a saddle point if the following condition holds:

$$
Z _ {0} \left(\mu , y ^ {*}, f \left(\mu , y ^ {*}\right)\right) \leq Z _ {0} \left(\mu^ {*}, y ^ {*}, f ^ {*}\right) \leq Z _ {0} \left(\mu^ {*}, y, f \left(\mu^ {*}, y\right)\right).\tag{6}
$$

In Eq. (5), a responding user equilibrium <sup>fl</sup>ow f<sup>∗</sup> to a pair of saddle points $( \mu ^ { * } , y ^ { * } )$ is a solution of a parametric variational inequality $\operatorname { E q . } \left( 4 \right)$ . Therefore, we have

$$
f ^ {*} = f \left(\mu^ {*}, y ^ {*}\right).\tag{7}
$$

## 2.3. A BDSS model

A bi-level decision support model with equilibrium <sup>fl</sup>ow for uncertain road network design through optimal link capacity expansion can be introduced below. In the bi-level model, a link capacity expansion $y ^ { * }$ can be optimally determined with a worst-case realization of travel demand growth μ<sup>∗</sup> for equilibrium <sup>fl</sup>ow f<sup>∗</sup>. That is,

$$
\underset {y, f} {\text { MinMax }} \quad P (\mu , y, f) = \sum_ {a} c _ {a} (y _ {a}, f (\mu , y)) f _ {a} (\mu , y) + \omega V _ {a} (y _ {a}).\tag{8}
$$

Subject to 0 ≤ y ≤ u , ∀ a ∈ L

$$
f _ {a} (\mu , y) \leq k _ {a} + y _ {a}, \quad \forall a \in L.
$$

In Eq. (8) a responding <sup>fl</sup>ow f<sup>∗</sup> is solved by a parametric variational inequality (4). The link <sup>fl</sup>ow f<sup>∗</sup> associated with uncertain travel demand growth factor μ is constrained by current link capacity plus potential expansion. Let $( \mu ^ { * } , y ^ { * } , f ^ { * } )$ de<sup>fi</sup>ne a risk-averse Stackelberg solution if the following condition holds.

$$
P \left(\mu , y ^ {*}, f \left(\mu , y ^ {*}\right)\right) \leq P \left(\mu^ {*}, y ^ {*}, f ^ {*}\right) \leq P \left(\mu^ {*}, y, f \left(\mu^ {*}, y\right)\right).\tag{9}
$$

## 2.4. Generalized gradients

According to [36,37], the direction of change that occurs in responding <sup>fl</sup>ow f<sup>∗</sup> can be evaluated by directional derivatives. Because a responding <sup>fl</sup>ow f<sup>∗</sup> is not always differentiable, it would be preventive from direct use of sensitivity analysis results in [35] for equilibrium <sup>fl</sup>ow. However, the <sup>fi</sup>rst-order directional derivatives exist almost everywhere for a general equilibrium network <sup>fl</sup>ow problem. To the best knowledge of the author, there exists very limited research work for calculation of generalized gradients of equilibrium <sup>fl</sup>ow for a bi-level support decision support model (8). In this section, the perturbation ∇f of responding <sup>fl</sup>ow f<sup>∗</sup> with respect to change in Δy and Δμ can be conveniently determined by solving the following variational inequality. Let $\Delta K ( \mu ^ { * } ) = \{ \nabla f \colon \nabla f = \lambda ( \Delta h ) , \Lambda ( \Delta h ) = \mu ^ { * } q , \exists \Delta h \in K _ { 0 } ( \mu ^ { * } ) \}$ denote a feasible set of perturbation <sup>fl</sup>ow ∇f where $K _ { 0 } ( \mu ^ { * } ) =$

$$
\left\{ \begin{array}{c} (i) \Delta h _ {p} \quad f r e e, \quad i f \quad h _ {k} ^ {*} > 0, \\ \Delta h: (i i) \Delta h _ {p} \geq 0,   i f \quad h _ {p} ^ {*} = 0, C _ {p} = \pi_ {w}, \quad \forall p \in R _ {w}, \forall w \in W \\ (i i i) \Delta h _ {p} = 0,   i f \quad h _ {p} ^ {*} = 0, C _ {p} > \pi_ {w} \end{array} \right\}. F o r e v e r y
$$

$\scriptstyle { \hat { \boldsymbol { f } } } \in \Delta K ( \mu ^ { * } )$ a directional derivative $\nabla _ { y } f \in \Delta K ( \mu ^ { * } )$ along a direction $\varDelta y$ <sup>ð Þ</sup>can be determined in the following way.

$$
\left(\nabla_ {y} c \left(\mu^ {*}, y ^ {*}, f ^ {*}\right) \Delta y + \nabla_ {f} c \left(\mu^ {*}, y ^ {*}, f ^ {*}\right) \nabla_ {y} f\right) (\hat {f} - \nabla_ {y} f) \geq 0\tag{10}
$$

Along a direction Δμ, for every $\hat { \boldsymbol { f } } \in \Delta K ( \mu ^ { * } )$ a directional derivative $\nabla _ { \mu } f \in \Delta K ( \mu ^ { * } )$ <sup>ð Þ</sup>of a responding <sup>fl</sup>ow f<sup>∗</sup> can be also determined below.

$$
\left(\nabla_ {\mu} c \left(\mu^ {*}, y ^ {*}, f ^ {*}\right) \Delta \mu + \nabla_ {f} c \left(\mu^ {*}, y ^ {*}, f ^ {*}\right) \nabla_ {\mu} f\right) (\hat {f} - \nabla_ {\mu} f) \geq 0\tag{11}
$$

In Eqs. (10)–(11) the gradients $\nabla _ { y } c ( \mu ^ { * } , y ^ { * } , f ^ { * } ) , \nabla _ { \mu } c ( \mu ^ { * } , y ^ { * } , f ^ { * } )$ and $\nabla _ { f } c ( \mu ^ { * } , y ^ { * } , f ^ { * } )$ are evaluated at $( \mu ^ { * } , y ^ { * } , \bar { f } ^ { * } )$ when perturbations in Δy and Δμ are speci<sup>fi</sup>ed. The directional derivatives $\nabla _ { y } f$ and $\nabla _ { \mu } f$ are piecewise linear and differentiable almost everywhere along every direction Δy and Δμ. Therefore the generalized gradients in [40] for responding flow $f ^ { * }$ with respect to perturbations Δy and Δμ can be characterized as follows. Let co denote a convex hull; it implies

$$
\partial_ {y} \Omega_ {f} \left(\mu^ {*}, y ^ {*}\right) = c o \left\{\lim _ {n \rightarrow \infty} \nabla_ {y} f \left(\mu^ {(n)}, y ^ {(n)}\right): \left(\mu^ {(n)}, y ^ {(n)}\right)\rightarrow \left(\mu^ {*}, y ^ {*}\right), \nabla_ {y} f \left(\mu^ {(n)}, y ^ {(n)}\right) e x i s t \right\}\tag{12}
$$

and

$$
\partial_ {\mu} \Omega_ {f} (\mu^ {*}, y ^ {*}) = c o \left\{\lim _ {n \rightarrow \infty} \nabla_ {\mu} f (\mu^ {(n)}, y ^ {(n)}): (\mu^ {(n)}, y ^ {(n)}) \rightarrow (\mu^ {*}, y ^ {*}), \nabla_ {\mu} f (\mu^ {(n)}, y ^ {(n)}) e x i s t \right\}.\tag{13}
$$

## 2.5. A single-level model for BDSS

According to the results given in Eqs. (12)–(13), the generalized gradients for Eq. (8) can be addressed as follows.

$$
\begin{array}{l} \nabla_ {y} P = \Big (\nabla_ {y} c (y, f (\mu , y)) + \nabla_ {f} c (y, f (\mu , y)) \nabla_ {y} f (\mu , y) \Big) f (\mu , y) \\ \quad + c (y, f (\mu , y)) \nabla_ {y} f (\mu , y) + \omega \nabla V (y) \end{array}\tag{14}
$$

and

$$
\nabla_ {\mu} P = \nabla_ {f} c (y, f (\mu , y)) \nabla_ {\mu} f (\mu , y) f (\mu , y) + c (y, f (\mu , y)) \nabla_ {\mu} f (\mu , y)\tag{15}
$$

The performance measure in Eq. (8) can be re-expressed as follows:

$$
P _ {1} (\mu , y) = \sum_ {a} c _ {a} (\mu , y _ {a}, f) f _ {a} + \omega V _ {a} (y _ {a}).\tag{16}
$$

Also the generalized gradients in Eqs. (14) and (15) can be reexpressed as follows.

$$
\nabla_ {y} P _ {1} = \nabla_ {y} P\tag{17}
$$

and

$$
\nabla_ {\mu} P _ {1} = \nabla_ {\mu} P\tag{18}
$$

A bi-level model for Eq. (8) can be reduced to the following single level problem.

$$
\underset {y} {\text { MinMax }} \quad P _ {1} (\mu , y) = \sum_ {a} c _ {a} (\mu , y _ {a}, f) f _ {a} + \omega V _ {a} (y _ {a})\tag{19}
$$

Subject to 0 ≤ y ≤ u , ∀ a ∈ L

$$
f _ {a} (\mu , y) \leq k _ {a} + y _ {a}, \quad \forall a \in L.
$$

Let $( \mu ^ { * } , y ^ { * } )$ ) de<sup>fi</sup>ne a pair of BDSS solutions in Eq. (19). A link capacity expansion y<sup>∗</sup> can be optimally determined with a worst-case realization taken by demand growth factor $\boldsymbol { \mu } ^ { * }$ . Following Eq. (6), a pair of BDSS saddle points $( \mu ^ { * } , y ^ { * } )$ exists if the following condition holds

$$
P _ {1} \left(\mu , y ^ {*}\right) \leq P _ {1} \left(\mu^ {*}, y ^ {*}\right) \leq P _ {1} \left(\mu^ {*}, y\right).\tag{20}
$$

In Eq. (20), at the <sup>fi</sup>rst inequality a worst-case travel demand growth factor μ<sup>∗</sup> can be optimally determined such that the performance measure in Eq. (19) is maximized. At the second inequality the link capacity expansion y<sup>∗</sup> can also be optimally determined such that performance measure is minimized. Let

$$
\underline {{P _ {1}}} (\mu) = P _ {1} \left(\mu , y ^ {*}\right) = \underset {y} {\text { Min }} P _ {1} (\mu , y)\tag{21}
$$

where y- Arg minP μ; y , and

$$
\overline {{P _ {1}}} (y) = P _ {1} \left(\mu^ {*}, y\right) = \underset {\mu} {M a x} P _ {1} (\mu , y)\tag{22}
$$

where $\mu ^ { * } = A r g \operatorname* { m a x } _ { \mu } P _ { 1 } ( \mu , y )$ . The inequalities in Eq. (20) can be reexpressed as follows.

$$
\underline {{P _ {1}}} (\mu) \leq P _ {1} \left(\mu^ {*}, y ^ {*}\right) \leq \overline {{P _ {1}}} (y)\tag{23}
$$

A pair of BDSS solutions $( \mu ^ { * } , y ^ { * } )$ in Eq. (19) can be alternately solved by two following sub-problems. First, for a link capacity expansion $y ^ { * } ,$ it is to

$$
\underset {\mu} {M a x} \quad \underline {{P _ {1}}} (\mu) = \sum_ {a} c _ {a} \left(\mu , y _ {a} ^ {*}, f\right) f _ {a} + \omega V _ {a} \left(y _ {a} ^ {*}\right).\tag{24}
$$

Subject to $f _ { a } ( \mu , y ^ { * } ) \leq k _ { a } + y _ { a } ^ { * } , \forall a \in L ,$

Next, for a worst-case realization taken by demand growth factor μ<sup>∗</sup>, it is to

$$
\underset {y} {\text { Min }} \quad \overline {{P _ {1}}} (y) = \sum_ {a} c _ {a} (\mu^ {*}, y _ {a}, f) f _ {a} + \omega V _ {a} (y _ {a}).\tag{25}
$$

Subject to $) \leq y _ { a } \leq u _ { a } , \forall a \in L$

$$
f _ {a} \left(\mu^ {*}, y\right) \leq k _ {a} + y _ {a}, \quad \forall a \in L.
$$

De<sup>fi</sup>nition 1. (A normative BDSS design) We say that $( \mu ^ { * } , y ^ { * } )$ is a pair of BDSS Stackelberg solutions if and only if there exists a link capacity expansion $y ^ { * }$ for Eq. (25) in the presence of a worst-case realization taken by demand growth factor μ<sup>∗</sup> for Eq. (24), i.e.

$$
\underline {{{P _ {1}}}} \left(\mu^ {*}\right) = P _ {1} \left(\mu^ {*}, y ^ {*}\right) = \overline {{{P _ {1}}}} \left(y ^ {*}\right).\tag{26}
$$

In Eq. (26) we have

$$
\mu^ {*} = \operatorname{Arg} \max P _ {1} (\mu)\tag{27}
$$

and

$$
y ^ {*} = \operatorname{Arg} \min \overline {{P _ {1}}} (y).\tag{28}
$$

According to Eq. (21)–(22), it concludes that at Stackelberg equilibrium we have a link capacity expansion y<sup>∗</sup> in the presence of a worstcase realization of demand growth factor μ<sup>∗</sup> such that

$$
P _ {1} \big (\mu^ {*}, y ^ {*} \big) = \underset {\mu} {M a x} \underset {y} {M i n} P _ {1} (\mu , y) = \underset {y} {M i n} \underset {\mu} {M a x} P _ {1} (\mu , y).\tag{29}
$$

Furthermore, by means of Eq. (9), we have

$$
P (\mu^ {*}, y ^ {*}, f ^ {*}) = \underset {\mu} {M a x} \underset {y} {M i n} P (\mu , y, f) = \underset {y} {M i n} \underset {\mu} {M a x} P (\mu , y, f).\tag{30}
$$

## 3. A computationally tractable solution scheme

In this section, a computationally tractable solution scheme is proposed to effectively solve two sub-problems (24) and (25). In the presence of uncertain travel demand, perturbations of parametric <sup>fl</sup>ow with respect to link capacity expansion can be evaluated using generalized gradients given in Eq. (14) and (15). A modi<sup>fi</sup>ed gradient-based method for BDSS using generalized gradients is introduced immediately.

## 3.1. A gradient-based method for BDSS

A bundle-type gradient-based method is presented to solve a minimization problem (25). The generalized gradient of an upper bound estimate $\overline { { P _ { 1 } } } ( \cdot )$ can be characterized by Eq. (17) and represented as a convex hull of all points of the form $\operatorname* { l i m } _ { n \to \infty } \nabla \overline { { P _ { 1 } } } \Big ( y ^ { ( n ) } \Big )$ where the subsequence $\{ y ^ { ( n ) } \}$ converges to a limit value y<sup>∗</sup>

$$
\partial \overline {{P _ {1}}} (y ^ {*}) = c o \left\{\lim _ {n \rightarrow \infty} \nabla_ {y} \overline {{P _ {1}}} (y ^ {(n)}): y ^ {(n)} \rightarrow y ^ {*}, \nabla_ {y} \overline {{P _ {1}}} (y ^ {(n)}) e x i s t s \right\}.\tag{31}
$$

For a linear approximation of an upper bound $\overline { { P _ { 1 } } } ( \cdot ) \mathrm { a t } y ^ { ( n ) }$ <sup>)</sup>, a cutting plane along a perturbed direction $\Delta y ^ { ( i ) }$ is constructed using a bundle of gradients $\{ \overline { { P _ { 1 } } } ( y ^ { ( i ) } ) , \nabla \overline { { P _ { 1 } } } ( y ^ { ( i ) } ) , 1 \leq i \leq n \}$ . Let $\overline { { P _ { 1 } } } ^ { ( n ) }$ denote a linear approximation of $\overline { { P _ { 1 } } } ( y )$ close to $y ^ { ( n ) }$ <sup>)</sup> at iteration $i , \forall 1 \leq i \leq n ,$ , we have

$$
\overline {{P _ {1}}} ^ {(n)} \approx \underset {1 \leq i \leq n} {\text { Max }} \left\{\nabla \overline {{P _ {1}}} \left(y ^ {(i)}\right) \left(y - y ^ {(i)}\right) + \overline {{P _ {1}}} \left(y ^ {(i)}\right) \right\}.\tag{32}
$$

Supposing that $\overline { { P _ { 1 } } } ^ { ( n ) }$ is convex, let

$$
\varepsilon_ {i, n} = \overline {{P _ {1}}} (y ^ {(n)}) - (\overline {{P _ {1}}} (y ^ {(i)}) + \nabla \overline {{P _ {1}}} (y ^ {(i)}) (y ^ {(n)} - y ^ {(i)}))\tag{33}
$$

denote an error bound for a linear approximation of $\overline { { P _ { 1 } } } \left( y ^ { ( n ) } \right)$ and $\varepsilon _ { i , n } \geq 0$ due to local convexity of $\overline { { P _ { 1 } } } ( y )$ . Let Δy be a search direction from the current iterate $y ^ { ( n ) }$ to the next one and denoted by

$$
\Delta y = y - y ^ {(n)}.\tag{34}
$$

A linear approximation of $\overline { { P _ { 1 } } } ^ { ( n ) }$ in $\operatorname { E q . }$ (32) can be expressed in the following way:

$$
\overline {{P _ {1}}} ^ {(n)} \approx \underset {1 \leq i \leq n} {\text { Max }} \left\{\nabla \overline {{P _ {1}}} \Big (y ^ {(i)} \Big) \Delta y - \varepsilon_ {i, n} \right\} + \overline {{P _ {1}}} \Big (y ^ {(n)} \Big).\tag{35}
$$

Since $\overline { { P _ { 1 } } } ( y ^ { ( n ) } )$ is constant in Eq. (35), for convenience let us skip this, a cutting plane model along a perturbed direction Δy can be constructed as follows.

$$
\overline {{P _ {1 c p}}} ^ {(n)} \left(y ^ {(n)}; \Delta y\right) = \underset {1 \leq i \leq n} {\text { Max }} \left\{\nabla_ {\Psi} \overline {{P _ {1}}} \left(y ^ {(i)}\right) \Delta y - \varepsilon_ {i, n} \right\}\tag{36}
$$

The solution Δy can be solved by the following quadratic model:

$$
\underset {\Delta y} {M i n} \quad v + \frac {1}{2} \| \Delta y \| ^ {2}.\tag{37}
$$

$$
\text { Subject   to } \nabla \overline {{P _ {1}}} (y ^ {(i)}) \Delta y - \varepsilon_ {i, n} \leq \nu , \quad 1 \leq i \leq n.
$$

## 3.2. A modified gradient-based method

In order to effectively solve a minimization problem (25), a modi<sup>fi</sup>ed gradient-based method is proposed. Let $t = \tau \frac { \overline { { P _ { 1 } } } ^ { ( n ) } - \overline { { P _ { 1 } } } ^ { * } } { \left. \Delta y \right. ^ { 2 } }$ ; 0≤a≤τ≤2−b; $b { > } 0$ with a local minimum point $y ^ { * }$ for problem (25). The corresponding $\overline { { P _ { 1 } } } ^ { * }$ is supposed to be known and $\textstyle { \boldsymbol { \tau } } = { \frac { 1 } { n } }$ such that

$$
y ^ {(n + 1)} = y ^ {(n)} + t \Delta y.\tag{38}
$$

In Eq. (38), a search for link capacity expansion y<sup>∗</sup> can be optimally determined using successive evaluations of subgradients of a piecewise linear approximation of Eq. (25) as introduced in Eq. (35). The corresponding performance measure (PM) of Eq. (25) can be successively improved until a search direction Δy de<sup>fi</sup>ned in Eq. (34) vanishes.

## 3.3. A tractable computation scheme

According to De<sup>fi</sup>nition 1, a Stackelberg solution for BDSS can be determined by successively solving two sub-problems (24) and (25). In this section, a tractable computation scheme solving BDSS is presented in steps.

Step 1 Start with initial link capacity expansion $y ^ { ( k ) }$ and demand growth factor $\mu ^ { ( k ) }$ . Set index $k = 0$ , and stopping threshold ε.

Step 2 Solve a maximization problem (24) with respect to a demand growth factor $\mu ^ { ( k + 1 ) }$ . Update an upper bound estimate $\overline { { P } } _ { 1 } =$

Table 2

$P _ { 1 } ( \mu ^ { ( k + 1 ) } , y ^ { ( k ) } )$ with a worst-case demand growth factor $\mu ^ { ( k ^ { * } + 1 ) }$ . Details about how to set an upper bound estimate $\overline { { P } } _ { 1 }$ are described in the following sub-steps.

Step 2-1 Characterize a responding <sup>fl</sup>ow $f ( \mu ^ { ( k ) } , \bar { y } ^ { ( k ) } )$ via Eq. (4).

Step 2-2 Conduct sensitivity analysis and determine $\nabla _ { \mu } \bar { f } ( \mu ^ { ( k ) } , y ^ { ( k ) } )$ via (11).

Step 2-3 Conduct sensitivity analysis for a lower bound estimate $P _ { 1 } ( \mu )$ and determine generalized gradient $\nabla _ { \boldsymbol { \mu } } P _ { 1 }$ from Eq. (18).

Step 2-4 Construct a cutting plane model for $\underline { { P _ { 1 } } } \left( \mu ^ { ( k ) } \right)$ <sup></sup> and determine a feasible search direction of Δμ.

Step 2-5 Follow a modi<sup>fi</sup>ed gradient-based method given in Section 3.2. Determine a new demand growth factor $\mu ^ { ( k + 1 ) }$ along a determined direction Δμ such that $\dot { \mu } ^ { ( k + 1 ) } = \mu ^ { ( k ) } + t \Delta \mu$

Step. 2-6 Update an upper bound estimate $\overline { { P } } _ { 1 } = P _ { 1 } ( \mu ^ { ( k + 1 ) } , y ^ { ( k ) } )$ for a new demand growth factor $\mu ^ { ( k + 1 ) }$

Step 3 Solve a minimization problem (25) with respect to link capacity expansion $y ^ { ( k \mathrm { ~ \overset { ~ } { + ~ } { ~ } } 1 ) }$ . Update a lower bound estimate $\bar { \underline { { P _ { 1 } } } } = \bar { P _ { 1 } } \bar { \big ( } \mu ^ { ( k + 1 ) } , y ^ { ( k + 1 ) } \bar { \big ) }$ with link capacity expansion $y ^ { ( k + 1 ) }$ Details about setting a lower bound estimate about $\underline { { P _ { 1 } } }$ are described in the following sub-steps.

Step 3-1 Determine a responding <sup>fl</sup>ow $f ( \tilde { \mu } ^ { ( k + 1 ) } , y ^ { ( k ) } )$ via Eq. (4).

Step 3-2 Conduct sensitivity analysis and determine $\nabla _ { y } f ( \mu ^ { ( k \mathrm { ~ + ~ } 1 ) } , y ^ { ( k ) } )$ via Eq. (10).

Step 3-3 Conduct sensitivity analysis for an upper bound estimate $\overline { { P _ { 1 } } }$ y and determine generalized gradient $\nabla _ { y } P _ { 1 }$ from Eq. (17). Step 3-4 Construct a cutting plane model for $\overline { { P _ { 1 } } } ( y ^ { ( \dot { k } ) } )$ and determine an optimal direction of change Δy.

Step 3-5 Follow a modi<sup>fi</sup>ed gradient-based method given in Section 3.2. Determine link capacity expansion $y ^ { ( k + 1 ) }$ along a determined direction Δy such that $y ^ { ( k ^ { ^ { - } } + 1 ) } =$ $y ^ { ( k ) } + t \Delta y$

![](/api/attachments/ZS6BSZ76/fulltext/images/ffb1ce536f8c06b472dcd9b384d0cfe6474c191db9e651571cfd489154224e84.jpg)  
Fig. 1. Sioux Falls real-data test network [42].

Initial data sets for Sioux Falls city network.

<table><tr><td>Decision variables</td><td>1st initial data</td><td>2nd initial data</td><td>3rd initial data</td><td>4th initial data</td></tr><tr><td> $y_{(4,11)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(10,11)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(12,11)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(14,11)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(9,10)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(11,10)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(15,10)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(16,10)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(17,10)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(11,14)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(15,14)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(23,14)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(10,15)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(14,15)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(19,15)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(22,15)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(15,22)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(20,22)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(21,22)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(23,22)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(14,23)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(22,23)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $y_{(24,23)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>4.0</td></tr><tr><td> $\mu$ </td><td>0.93</td><td>0.96</td><td>0.95</td><td>0.94</td></tr><tr><td>PM (in $)</td><td>102.5</td><td>103.7</td><td>109.2</td><td>104.8</td></tr></table>

Where $y _ { ( a , b ) }$ denotes link (a, b) capacity expansion and upper bound for link (a, b) is 25.0

Step. 3-6 Update a lower bound estimate $P _ { 1 } = P _ { 1 } ( \mu ^ { ( k + 1 ) } , y ^ { ( k + 1 ) } )$ for $y ^ { ( k { \stackrel { . . } { + } } 1 ) } .$ new link capacity expansion

Step 4 If the distance of PM between upper bound estimate $\overline { { P _ { 1 } } }$ and lower bound estimate $P _ { 1 }$ is within a threshold ε, i.e. $\left| { \overline { { P _ { 1 } } } } - P _ { 1 } \right| \leq$ ε then stop. According to Eq. (26), a Stackelberg equilibrium is achieved for BDSS with link capacity expansion $\bar { y ^ { * } } = y ^ { ( k + 1 ) }$ Otherwise, increase index k by 1 and go to Step 2.

Link capacity expansions for Sioux Falls city network under uncertain travel demand.

<table><tr><td>Decision variables</td><td>1st initial data</td><td>2nd initial data</td><td>3rd initial data</td><td>4th initial data</td></tr><tr><td> $y_{(4,11)}$ </td><td>1.5</td><td>1.7</td><td>3.2</td><td>3.3</td></tr><tr><td> $y_{(10,11)}$ </td><td>3.2</td><td>2.5</td><td>2.2</td><td>1.9</td></tr><tr><td> $y_{(12,11)}$ </td><td>2.5</td><td>2.2</td><td>3.5</td><td>2.0</td></tr><tr><td> $y_{(14,11)}$ </td><td>2.5</td><td>1.8</td><td>3.1</td><td>2.8</td></tr><tr><td> $y_{(9,10)}$ </td><td>1.6</td><td>1.4</td><td>2.2</td><td>3.5</td></tr><tr><td> $y_{(11,10)}$ </td><td>1.5</td><td>2.4</td><td>1.5</td><td>3.4</td></tr><tr><td> $y_{(15,10)}$ </td><td>4.3</td><td>3.5</td><td>1.8</td><td>2.4</td></tr><tr><td> $y_{(16,10)}$ </td><td>2.6</td><td>4.2</td><td>2.2</td><td>3.5</td></tr><tr><td> $y_{(17,10)}$ </td><td>2.2</td><td>3.5</td><td>2.9</td><td>4.1</td></tr><tr><td> $y_{(11,14)}$ </td><td>2.5</td><td>4.0</td><td>2.9</td><td>3.8</td></tr><tr><td> $y_{(15,14)}$ </td><td>1.4</td><td>3.0</td><td>3.2</td><td>3.5</td></tr><tr><td> $y_{(23,14)}$ </td><td>1.6</td><td>2.5</td><td>2.8</td><td>2.4</td></tr><tr><td> $y_{(10,15)}$ </td><td>2.2</td><td>2.5</td><td>4.2</td><td>3.8</td></tr><tr><td> $y_{(14,15)}$ </td><td>2.5</td><td>3.2</td><td>2.3</td><td>4.2</td></tr><tr><td> $y_{(19,15)}$ </td><td>2.5</td><td>3.5</td><td>2.3</td><td>2.9</td></tr><tr><td> $y_{(22,15)}$ </td><td>3.2</td><td>3.5</td><td>3.5</td><td>3.4</td></tr><tr><td> $y_{(15,22)}$ </td><td>3.2</td><td>2.5</td><td>3.5</td><td>4.1</td></tr><tr><td> $y_{(20,22)}$ </td><td>4.5</td><td>2.5</td><td>2.8</td><td>3.0</td></tr><tr><td> $y_{(21,22)}$ </td><td>4.0</td><td>3.5</td><td>1.5</td><td>2.4</td></tr><tr><td> $y_{(23,22)}$ </td><td>3.5</td><td>4.2</td><td>1.5</td><td>4.2</td></tr><tr><td> $y_{(14,23)}$ </td><td>2.0</td><td>4.2</td><td>4.2</td><td>3.8</td></tr><tr><td> $y_{(22,23)}$ </td><td>2.0</td><td>1.5</td><td>2.5</td><td>2.4</td></tr><tr><td> $y_{(24,23)}$ </td><td>4.2</td><td>1.4</td><td>2.7</td><td>3.4</td></tr><tr><td> $\mu$ </td><td>1.02</td><td>1.03</td><td>1.04</td><td>1.03</td></tr><tr><td>PM (in $)</td><td>92.5</td><td>89.5</td><td>88.1</td><td>91.4</td></tr><tr><td>Improvement rate (%)</td><td>9.76</td><td>13.69</td><td>19.32</td><td>12.79</td></tr></table>

Table 5  
Stackelberg solution for the 1st initial data set.

<table><tr><td> $(\mu,y)$ </td><td> $\mu$ </td><td> $P_1(\mu,y)$ </td><td> $\overline{P}_1$ </td><td> $\underline{P}_1$ </td><td>gap</td></tr><tr><td> $(\mu^{(0)},y^{(0)})$ </td><td>0.93</td><td>102.5</td><td></td><td></td><td></td></tr><tr><td> $(\mu^{(1)},y^{(0)})$ </td><td>0.95</td><td>124.5</td><td>124.5</td><td></td><td>44.7</td></tr><tr><td> $(\mu^{(1)},y^{(1)})$ </td><td>0.95</td><td>79.8</td><td></td><td>79.8</td><td></td></tr><tr><td> $(\mu^{(2)},y^{(1)})$ </td><td>0.97</td><td>112.4</td><td>112.4</td><td></td><td>28.9</td></tr><tr><td> $(\mu^{(2)},y^{(2)})$ </td><td>0.97</td><td>83.5</td><td></td><td>83.5</td><td></td></tr><tr><td> $(\mu^{(3)},y^{(2)})$ </td><td>0.98</td><td>107.6</td><td>107.6</td><td></td><td>21.5</td></tr><tr><td> $(\mu^{(3)},y^{(3)})$ </td><td>0.98</td><td>86.1</td><td></td><td>86.1</td><td></td></tr><tr><td> $(\mu^{(4)},y^{(3)})$ </td><td>0.99</td><td>101.6</td><td>101.6</td><td></td><td>12.4</td></tr><tr><td> $(\mu^{(4)},y^{(4)})$ </td><td>0.99</td><td>89.2</td><td></td><td>89.2</td><td></td></tr><tr><td> $(\mu^{(5)},y^{(4)})$ </td><td>1.0</td><td>95.8</td><td>95.8</td><td></td><td>4.1</td></tr><tr><td> $(\mu^{(5)},y^{(5)})$ </td><td>1.0</td><td>91.7</td><td></td><td>91.7</td><td></td></tr><tr><td> $(\mu^{(6)},y^{(5)})$ </td><td>1.02</td><td>92.5</td><td>92.5</td><td></td><td>0</td></tr><tr><td> $(\mu^{(6)},y^{(6)})$ </td><td>1.02</td><td>92.5</td><td></td><td>92.5</td><td></td></tr></table>

Where $P ^ { \ast } = P _ { 1 } ( \mu ^ { ( 6 ) } , y ^ { ( 6 ) } ) = 9 2 . 5 , \widetilde { P } = P _ { 1 } \left( \mu ^ { ( 6 ) } , y ^ { ( 1 ) } \right) = 1 1 9 . 9 , P _ { L } = P _ { 1 } ( \mu ^ { ( 1 ) } , y ^ { ( 1 ) } ) = 7 9 . 8 \mathrm { ~ a n d ~ }$ ${ \hat { P } } = P _ { 1 } \left( \mu ^ { ( 1 ) } , y ^ { ( 6 ) } \right) = 8 2 .$ 1; therefore by $\operatorname { E q . }$ $\left( 3 9 \right) r ^ { + } = 2 9 . 6 2 \%$ and by Eq. $\left( 4 0 \right) r ^ { - } = 2 . 8 8 \%$

## 4. Numerical computations

In this section, numerical computations were performed using a real-data benchmark problem of Sioux Falls city network as shown in Fig. 1. The travel time and link investment cost functions in Eq. (19) were adopted from [41] where convex investment function form was adopted from [42], together with data input details. This numerical test included 23 candidate links for capacity expansions. Four sets of initial link capacity expansions $y ^ { ( 0 ) }$ with travel demand growth factor $\cdot \mu ^ { ( 0 ) }$ were given in Table 1. The performance measure (PM) was also given for various sets of initial settings. Implementations for carrying out the following computations were made on SUN SPARC SUNW, 900 MHz processor with 4GB RAM under Unix SunOS 5.8 using C++ compiler. The stopping criterion was set when the relative difference in the objective function value is less than 0.15%. Computational results were summarized in Table 2. As is shown in Table 2, improvement rates for the PM value over various initial data sets were between about 9.8% and 19%. As is mentioned, a bi-level BDSS program is typically non-convex. The results from Table 2 also indicated this consequence of nonconvex problem where various local solutions were obtained for various sets of initial settings. Computational results at four initial data sets were shown in detail in Tables 3–6 and plotted in Figs. 2–5 respectively. The effectiveness of the proposed approach was demonstrated when the gap of bounds for PM value was continuously reduced. The resulting PM value can be achieved only when a risk-averse Stackelberg solution for min–max problem (19) is found. Take the 1st data set as is shown in Table 3 for example, a PM value of \$102.5 at initial link capacity expansion $y ^ { ( 0 ) }$ with travel demand growth $\mu ^ { ( 0 ) }$ of 0.93 was degraded to that of \$124.5 for a worst-case travel demand growth factor $\mu ^ { ( 1 ) }$ of 0.95 when conducting Step 2. The new PM value can be considered as an upper bound estimate for a BDSS with initial link capacity expansion $y ^ { ( 0 ) }$ . A new link capacity expansion $y ^ { ( 1 ) }$ can be accordingly determined after conducting Step 3. A new lower bound estimate of PM value of \$79.8 was therefore obtained. As is indicated in Table 3, at iteration 1 the gap of bounds of PM value was as high as \$44.7. As it proceeds, the gap starts to fall from a value of \$44.7 to that of \$28.9 and continues to decrease until the gap vanishes at iterate 6. At this point, as is observed from Table 3 and indicated in Fig. 2, the value of upper bound estimate equals that of a lower bound estimate. The resulting PM value is of \$92.5 after 6 iterations. As is demonstrated in steps, a resulting link capacity expansion $y ^ { ( 6 ) }$ was obtained for a worst-case demand growth factor of 1.02. As is indicated in Table 2, the improvement rate of a proposed link capacity expansion was about 9.8%. For the 2nd data set as is shown in Table $4 , \mathsf { a }$ PM value of \$103.7 at signal setting $y ^ { ( 0 ) }$ <sup>)</sup> was degraded to that of \$125.1 for a travel demand growth factor $\dot { \mu } ^ { ( 1 ) }$ of 0.97. The PM value can be continuously reduced until the gap vanishes. At this point, as is observed from Table 4 and indicated in Fig. 3, the upper bound estimate equals lower bound estimate. The resulting PM value is of \$125.1 after 5 iterations. As it proceeds, a resulting link capacity expansion $y ^ { ( 5 ) }$ was obtained for a demand growth factor of 1.03. As is indicated in Table 2, the improvement rate was about 14%. For the 3rd data set as is shown in Table 5, a PM value of \$109.2 with demand growth of 0.95 was continuously degraded to that of \$88.1 for a demand growth factor of 1.04 after 7 iterations. As is indicated in Table 2, the improvement rate was about 19%. Finally, for the 4th data set as shown in Table 6, a PM value of \$104.8 with initial travel demand growth of 0.94 was degraded to a resulting one of \$91.4 for a worst-case travel demand growth factor of 1.03 after 6 iterations. As is indicated in Table 2, the improvement rate was about 13%.

Stackelberg solution for the 2nd initial data set.

<table><tr><td> $(\mu,y)$ </td><td> $\mu$ </td><td> $P_1(\mu,y)$ </td><td> $\overline{P}_1$ </td><td> $\underline{P}_1$ </td><td>gap</td></tr><tr><td> $(\mu^{(0)},y^{(0)})$ </td><td>0.96</td><td>103.7</td><td></td><td></td><td></td></tr><tr><td> $(\mu^{(1)},y^{(0)})$ </td><td>0.97</td><td>125.1</td><td>125.1</td><td></td><td>45</td></tr><tr><td> $(\mu^{(1)},y^{(1)})$ </td><td>0.97</td><td>80.1</td><td></td><td>80.1</td><td></td></tr><tr><td> $(\mu^{(2)},y^{(1)})$ </td><td>0.98</td><td>113.5</td><td>113.5</td><td></td><td>28.7</td></tr><tr><td> $(\mu^{(2)},y^{(2)})$ </td><td>0.98</td><td>84.8</td><td></td><td>84.8</td><td></td></tr><tr><td> $(\mu^{(3)},y^{(2)})$ </td><td>0.99</td><td>107.6</td><td>107.6</td><td></td><td>20.1</td></tr><tr><td> $(\mu^{(3)},y^{(3)})$ </td><td>0.99</td><td>87.5</td><td></td><td>87.5</td><td></td></tr><tr><td> $(\mu^{(4)},y^{(3)})$ </td><td>1.02</td><td>95.1</td><td>95.1</td><td></td><td>6.2</td></tr><tr><td> $(\mu^{(4)},y^{(4)})$ </td><td>1.02</td><td>88.9</td><td></td><td>88.9</td><td></td></tr><tr><td> $(\mu^{(5)},y^{(4)})$ </td><td>1.03</td><td>89.5</td><td>89.5</td><td></td><td>0</td></tr><tr><td> $(\mu^{(5)},y^{(5)})$ </td><td>1.03</td><td>89.5</td><td></td><td>89.5</td><td></td></tr></table>

$\mathsf { W h e r e } P ^ { * } = P _ { 1 } ( \mu ^ { ( 5 ) } , y ^ { ( 5 ) } ) = 8 9 . 5 , \widetilde { P } = P _ { 1 } \left( \mu ^ { ( 5 ) } , y ^ { ( 1 ) } \right) = 1 1 7 . 6 , P _ { L } = P _ { 1 } ( \mu ^ { ( 1 ) } , y ^ { ( 1 ) } ) = 8 0 . 1 \mathrm { ~ a n d }$ $\hat { \cal P } = { \cal P } _ { 1 } \left( \mu ^ { ( 1 ) } , y ^ { ( 5 ) } \right) = 8 2 . 3 ;$ therefore by Eq. (39) r<sup>+</sup> = 31.4 % and by Eq. (40) r<sup>−</sup> = 2.75 %.

Stackelberg solution for the 3rd initial data set.

<table><tr><td> $(\mu,y)$ </td><td> $\mu$ </td><td> $P_1(\mu,y)$ </td><td> $\overline{P}_1$ </td><td> $\underline{P}_1$ </td><td>gap</td></tr><tr><td> $(\mu^{(0)},y^{(0)})$ </td><td>0.95</td><td>109.2</td><td></td><td></td><td></td></tr><tr><td> $(\mu^{(1)},y^{(0)})$ </td><td>0.96</td><td>130.1</td><td>130.1</td><td></td><td>50.9</td></tr><tr><td> $(\mu^{(1)},y^{(1)})$ </td><td>0.96</td><td>79.2</td><td></td><td>79.2</td><td></td></tr><tr><td> $(\mu^{(2)},y^{(1)})$ </td><td>0.97</td><td>121.9</td><td>121.9</td><td></td><td>40.5</td></tr><tr><td> $(\mu^{(2)},y^{(2)})$ </td><td>0.97</td><td>81.4</td><td></td><td>81.4</td><td></td></tr><tr><td> $(\mu^{(3)},y^{(2)})$ </td><td>0.99</td><td>113.6</td><td>113.6</td><td></td><td>30.9</td></tr><tr><td> $(\mu^{(3)},y^{(3)})$ </td><td>0.99</td><td>82.7</td><td></td><td>82.7</td><td></td></tr><tr><td> $(\mu^{(4)},y^{(3)})$ </td><td>1.01</td><td>105.1</td><td>105.1</td><td></td><td>20.6</td></tr><tr><td> $(\mu^{(4)},y^{(4)})$ </td><td>1.01</td><td>84.5</td><td></td><td>84.5</td><td></td></tr><tr><td> $(\mu^{(5)},y^{(4)})$ </td><td>1.02</td><td>97.4</td><td>97.4</td><td></td><td>11.3</td></tr><tr><td> $(\mu^{(5)},y^{(5)})$ </td><td>1.02</td><td>86.1</td><td></td><td>86.1</td><td></td></tr><tr><td> $(\mu^{(6)},y^{(5)})$ </td><td>1.03</td><td>89.2</td><td>89.2</td><td></td><td>1.1</td></tr><tr><td> $(\mu^{(6)},y^{(6)})$ </td><td>1.03</td><td>88.1</td><td></td><td>88.1</td><td></td></tr><tr><td> $(\mu^{(7)},y^{(6)})$ </td><td>1.04</td><td>88.1</td><td>88.1</td><td></td><td>0</td></tr><tr><td> $(\mu^{(7)},y^{(7)})$ </td><td>1.04</td><td>88.1</td><td></td><td>88.1</td><td></td></tr></table>

Where $P ^ { \ast } = P _ { 1 } ( \mu ^ { ( 7 ) } , y ^ { ( 7 ) } ) = 8 8 . 1 , \widetilde { P } = P _ { 1 } \left( \mu ^ { ( 7 ) } , y ^ { ( 1 ) } \right) = 1 1 7 . 9 , P _ { L } = P _ { 1 } ( \mu ^ { ( 1 ) } , y ^ { ( 1 ) } ) = 7 9 . 2 \mathrm { ~ a n d ~ }$ $\hat { P } = P _ { 1 } \left( \mu ^ { ( 1 ) } , y ^ { ( 7 ) } \right) = 8 1 . 2 ;$ therefore by Eq. $( 3 9 ) r ^ { + } = 3 7 . 5 7 \%$ and by $( 4 0 ) r ^ { - } = 2 . 5 3 \% .$

Stackelberg solution for the 4th initial data set

<table><tr><td> $(\mu,y)$ </td><td> $\mu$ </td><td> $P_1(\mu,y)$ </td><td> $\overline{P}_1$ </td><td> $\underline{P}_1$ </td><td>gap</td></tr><tr><td> $(\mu^{(0)},y^{(0)})$ </td><td>0.94</td><td>104.8</td><td></td><td></td><td></td></tr><tr><td> $(\mu^{(1)},y^{(0)})$ </td><td>0.96</td><td>127.8</td><td>127.8</td><td></td><td>47.4</td></tr><tr><td> $(\mu^{(1)},y^{(1)})$ </td><td>0.96</td><td>80.4</td><td></td><td>80.4</td><td></td></tr><tr><td> $(\mu^{(2)},y^{(1)})$ </td><td>0.97</td><td>118.7</td><td>118.7</td><td></td><td>33.5</td></tr><tr><td> $(\mu^{(2)},y^{(2)})$ </td><td>0.97</td><td>85.2</td><td></td><td>85.2</td><td></td></tr><tr><td> $(\mu^{(3)},y^{(2)})$ </td><td>0.99</td><td>109.7</td><td>109.7</td><td></td><td>21.6</td></tr><tr><td> $(\mu^{(3)},y^{(3)})$ </td><td>0.99</td><td>88.1</td><td></td><td>88.1</td><td></td></tr><tr><td> $(\mu^{(4)},y^{(3)})$ </td><td>1.01</td><td>97.8</td><td>97.8</td><td></td><td>7.3</td></tr><tr><td> $(\mu^{(4)},y^{(4)})$ </td><td>1.01</td><td>90.5</td><td></td><td>90.5</td><td></td></tr><tr><td> $(\mu^{(5)},y^{(4)})$ </td><td>1.02</td><td>93.7</td><td>93.7</td><td></td><td>2.3</td></tr><tr><td> $(\mu^{(5)},y^{(5)})$ </td><td>1.02</td><td>91.4</td><td></td><td>91.4</td><td></td></tr><tr><td> $(\mu^{(6)},y^{(5)})$ </td><td>1.03</td><td>91.4</td><td>91.4</td><td></td><td>0</td></tr><tr><td> $(\mu^{(6)},y^{(6)})$ </td><td>1.03</td><td>91.4</td><td></td><td>91.4</td><td></td></tr></table>

$\mathrm { W h e r e } ~ P ^ { * } = P _ { 1 } ( \mu ^ { ( 6 ) } , y ^ { ( 6 ) } ) = 9 1 . 4 , \widetilde { P } = P _ { 1 } \left( \mu ^ { ( 6 ) } , y ^ { ( 1 ) } \right) = 1 1 9 . 9 , P _ { L } = P _ { 1 } ( \mu ^ { ( 1 ) } , y ^ { ( 1 ) } ) = 8 0 . 4 \mathrm { a n d }$ $\hat { P } = P _ { 1 } \left( \mu ^ { ( 1 ) } , y ^ { ( 6 ) } \right) = 8 2 . 1$ ; therefore by Eq. (39) r<sup>+</sup> = 31.18 % and by Eq. $( 4 0 ) r ^ { - } = 2 . 1 1 \% .$

![](/api/attachments/ZS6BSZ76/fulltext/images/0d6b762533caf20c712ca9249c9adbf19a37040ae03783475a2e5935e60adc56.jpg)  
Fig. 2. Bound changes for the 1st initial data set.

A robust solution is often regarded as a solution for a worst-case scenario. The feasibility of solutions against parameter ambiguity and stochastic uncertainty is pursued at the expense of solution optimality. A robust link capacity expansion can be determined under a worst-case of demand. For a BDSS problem with equilibrium <sup>fl</sup>ow, it becomes a trade-off between system performance and protection against travel demand uncertainty. To investigate the ef<sup>fi</sup>ciency and robustness of proposed solutions, two computational indices are introduced: the infeasibility gain and optimality loss. First, the infeasibility gain of a robust link capacity expansion is de<sup>fi</sup>ned as a percent gain for the difference between the PM value of the upper bound estimate and that at robust link capacity expansions in the following manner. Let $\widetilde { P }$ represent an upper bound estimate for a deterministic link capacity expansion under a worst-case realization of demand growth factor. Let $P ^ { * }$ denote a BDSS solution. We de<sup>fi</sup>ne the infeasibility gain of proposed robust link capacity expansion for a worst-case realization taken by demand growth factor in the following way:

$$
r ^ {+} = \left(\frac {\widetilde {P} - P ^ {*}}{P ^ {*}}\right) * 100 \%.\tag{39}
$$

Second, let $P _ { L }$ represent a lower bound estimate for a deterministic link capacity expansion at nominal condition. Let $\hat { P }$ denote a suboptimum for a robust link capacity expansion at nominal condition. The optimality loss of a proposed link capacity expansion for BDSS can be de<sup>fi</sup>ned as a percent loss for the difference between the PM value of a lower bound estimate and that at a nominal condition as follows.

PM (in \$)  
![](/api/attachments/ZS6BSZ76/fulltext/images/9fa280a083c3f378092be723a164be0e0efd68a1a58c2c9655f051c43b4f0a77.jpg)  
Fig. 3. Bound changes for the 2nd initial data set.

![](/api/attachments/ZS6BSZ76/fulltext/images/4c78fb45ecc42151a2f64bebfc76736ad0ff21a3ea49ad9bd9999d0de4afbc7a.jpg)  
Fig. 4. Bound changes for the 3rd initial data set.

$$
r ^ {-} = \left(\frac {\hat {P} - P _ {L}}{P _ {L}}\right) * 100 \%\tag{40}
$$

Take the <sup>fi</sup>rst initial data set for example, as is observed from Table 3, a proposed link capacity expansion $y ^ { ( 6 ) }$ obtained more than 29% gain in infeasibility while incurring a less than 3% loss in optimality. For the 2nd initial data set, as is observed in Table $^ { 4 , }$ a proposed link capacity expansion $y ^ { ( 5 ) }$ achieved more than 31% gain in infeasibility while incurring a less than 3% loss in optimality at nominal condition. For the 3rd and 4th initial data sets, again, as is indicated respectively in Tables 5–6, the proposed robust link capacity expansions achieved greater advantage of gain in infeasibility over than did the deterministic solutions. As is observed in Tables 5–6, the proposed link capacity expansion $y ^ { ( 7 ) }$ and $y ^ { ( 6 ) }$ achieved more than 37% and 31% gains in infeasibility while incurring a near 2.5% loss in optimality at nominal condition. Numerical computations for BDSS in terms of Eqs. (39) and (40) over four sets were also plotted in Figs. 6–7 respectively. As is observed in Fig. 6, at the very beginning the infeasibility gain starts to rise from a value of 29.6% to that of 31.4%. As it proceeds, the gain of proposed solutions steadily rises as demand growth factor grows on the one hand. On the other hand, as is seen in Fig. 7, the trend of optimality loss steadily falls from a value of 2.88% to that of 2.11% against growing demand growth factor. The gain of proposed solutions becomes much more signi<sup>fi</sup>cant as travel demand growth factor increases while incurring relatively modest loss in optimality. Regarding computational efforts of CPU overheads, they were within 2 min for complete run of BDSS following the procedure given in Section 3.3.

![](/api/attachments/ZS6BSZ76/fulltext/images/6a0c82a091043ddfa1f7703217151b46039cb210aa84b088ad2b8f81544502b9.jpg)  
Fig. 5. Bound changes for the 4th initial data set.

![](/api/attachments/ZS6BSZ76/fulltext/images/1636e6d7dfc829dd199c7e5f635715d2208a02590cc2e58eeee23dc98d8e64be.jpg)  
Fig. 6. Infeasibility gain in percentage for initial data sets.

## 5. Conclusions and further issues

In this paper, we presented a bi-level decision support system (BDSS) for uncertain road network design with equilibrium <sup>fl</sup>ow. A bi-level decision support model with link capacity expansion was developed to effectively reduce total travel delay for all road users in the presence of uncertain travel demand. Using generalized gradients, a computationally tractable solution scheme was proposed. A risk-averse Stackelberg solution for normative BDSS design was obtained. Numerical computations were performed using a mediumsize real-data road network. In comparison with deterministic solutions obtained for road network at nominal condition, the proposed solutions performed far better under the worst-case travel demand despite the expense of relatively smaller loss of optimality at nominal condition. In particular, our computation results showed that the proposed solution becomes even attractive as demand growth factor increases.

While the present work on link capacity expansion for BDSS with equilibrium <sup>fl</sup>ow indicated that a bi-level decision support model is attractive, a min–max approach can be regarded as a normative design for decision makers at a worst-case scenario of general road network when information of travel demand is barely known. Considering a general road network design with limited access of demand, the value of system performance at risk can be taken into account. Applications of using probability-based functions like chance-constrained model to tackle a general network design at risk are being investigated. We will discuss this issue in a subsequent paper.

![](/api/attachments/ZS6BSZ76/fulltext/images/f6cd74f9ea50c3547e5342471cac7cbf19a83ad2a026a75b501dea1be71e2972.jpg)  
Fig. 7. Optimality loss in percentage for initial data sets.

## Acknowledgments

The author would like to thank anonymous reviewers and editor for their constructive comments in the earlier versions of this manuscript. Many thanks also go to the Editor-in-chief for his kind arrangement. The work reported in this paper has been supported by grants NSC 98-2410-H-259-009-MY3 and NSC-101-2628-H-259-001-MY2 from Taiwan National Science Council.

## References

[1] J.G. Wardrop, Some theoretical aspects of road traf<sup>fi</sup>c approach, Proceeding of the Institution of Civil Engineers II (1952) 325–378.

[2] A.R. Hatami, H. Sei<sup>fi</sup>, M.K. Sheikh-El-Eslami, Hedging risks with interruptible load programs for a load serving entity, Decision Support Systems 48 (2009) 150–157.

[3] T. Comes, M. Hiete, N. Wijngaards, F. Schultmann, Decision maps: a framework for multi-criteria decision support under severe uncertainty, Decision Support Systems 52 (2011) 108–118.

[4] W. Burgholzer, G. Bauer, M. Posset, W. Jammernegg, Analysing the impact of disruptions in intermodal transport networks: a micro simulation-based model, Decision Support Systems 54 (2013) 1580–1586.

[5] D.E. Snediker, A.T. Murray, T.C. Matisziw, Decision support for network disruption mitigation, Decision Support Systems 44 (2008) 954–969.

[6] K. Dahal, K. Almejalli, M.A. Hossain, Decision support for coordinated road traf<sup>fi</sup>c control actions, Decision Support Systems 54 (2013) 962–975.

[7] J.M. Cruz, Z. Liu, Modeling and analysis of the effects of QoS and reliability on pricing, pro<sup>fi</sup>tability, and risk management in multiperiod grid-computing networks, Decision Support Systems 52 (2012) 562–576.

[8] C.W. Zobel, Representing perceived tradeoffs in de<sup>fi</sup>ning disaster resilience, Decision Support Systems 50 (2011) 394–403.

[9] B.D. Chung, T. Yao, C. Xie, A. Thorsen, Robust optimization model for a dynamic network design problem under demand uncertainty, Networks and Spatial Economics 11 (2011) 371–389.

[10] A. Chen, Z. Zhou, P. Chootinan, S. Ryu, C. Yang, S.C. Wong, Transport network design problem under uncertainty: a review and new developments, Transport Reviews 31 (6) (2011) 743–768.

[11] R. Farahani, E. Miandoabchi, W. Szeto, H. Rashidi, A review of urban transportation network design problems, European Journal of Operational Research 229 (2013) 281–302.

[12] P. Luathep, A. Sumalee, W.H.K. Lam, Z. Li, H. Lo, Global optimization method for mixed transportation network design problem: a mixed-integer linear programming approach, Transportation Research Part B 45 (6) (2011) 808–827.

[13] E. Miandoabchi, R.Z. Farahani, W. Szeto, Bi-objective bimodal urban road network design using hybrid metaheuristics, Central European Journal of Operations Research 20 (4) (2012) 583–621

[14] J.M. Mulvey, R.J. Vanderbei, S.A. Zenios, Robust optimization of large-scale systems, Operations Research 43 (2) (1995) 264–281

[15] A. Ben-Tal, A. Nemirovski, Robust optimization—methodology and applications, Mathematical Programming 92 (2002) 380–453.

[16] A. Ben-Tal, L. El Ghaoui, A. Nemirovski, Robustness Optimization, Princeton University Press, Princeton, NJ, 2009.

[17] D. Bertsimas, D.B. Brown, C. Caramanis, Theory and applications of robust optimiza tion, SIAM Review 53 (3) (2011) 464–501.

[18] A. Karoonsoontawong, S.T. Waller, Integrated network capacity expansion and traf-<sup>fi</sup>c signal optimization: robust bi-level dynamic formulation, Networks and Spatial Economics 10 (2010) 525–550.

[19] S.V. Ukkusuri, T. Mathew, T. Waller, Robust transportation network design under demand uncertainty, Computer Aided Civil and Infrastructure Engineering 22 (2007) 6–18.

[20] S.V. Ukkusuri, G. Patil, Multi-period transportation network design under demand uncertainty, Transportation Research Part B 43 (6) (2009) 625–642.

[21] Y. Yin, S.M. Madanat, X. Lu, Robust improvement schemes for road networks under demand uncertainty, European Journal of Operation Research 198 (2) (2009) 470–479.

[22] F. Ordonez, J. Zhao, Robust capacity expansion of network <sup>fl</sup>ows, Networks 50 (2) (2007) 136–145.

[23] S. Mudchanatongsuk, F. Ordonez, J. Liu, Robust solutions for network design under transportation cost and demand uncertainty, Journal of the Operational Research Society 59 (2008) 652–662.

[24] Z.-Q. Luo, J.-S. Pang, D. Ralph, Mathematical Programs with Equilibrium Constraints, Cambridge University Press, Cambridge, 1996.

[25] A. Migdalas, P.M. Pardalos, P. Varbrand, Multilevel Optimization: Algorithms and Applications, Kluwer Academic Publishers, Dordrecht, 1998.

[26] J.F. Bard, Practical Bilevel Optimization: Algorithms and Applications, Kluwer Academic Publishers, Dordrecht, 1998.

[27] S. Dempe, Foundations of Bilevel programming, Kluwer Academic Publishers, Dordrecht 2002

[28] T.L. Friesz, R.L. Tobin, H.-J. Cho, N.J. Mehta, Sensitivity analysis based heuristic algorithms for mathematical programs with variational inequality constraints, Mathematical Programming 48 (1990) 265–284.

[29] S. Suh, T.J. Kim, Solving nonlinear bilevel programming models of the equilibrium network design problem: a comparative review, Annals of Operations Research 34 (1992)203-218

[30] Q. Meng, H. Yang, M.G.H. Bell, An equivalent continuously differentiable model and a locally convergent algorithm for the continuous network design problem, Transportation Research Part B 35 (1) (2001) 83–105.

[31] S.-W. Chiou, Bilevel programming for the continuous transport network design problem, Transportation Research Part B 39 (4) (2005) 361–383.

[32] M.G.H. Bell, Y. Iida, Transportation Network Analysis, Wiley, Chichester, 1997.

[33] H. Yang, M.G.H. Bell, Sensitivity analysis of network traf<sup>fi</sup>c equilibria revisited: the corrected approach, in: B.G. Heydecker (Ed.), Mathematics in Transport, Selected Proceedings of the 4th IMA International Conference on Mathematics in Transport in Honor of Richard Allsop, Elsevier, Oxford, 2007, pp. 373–395.

[34] M. Josefsson, M. Patriksson, Sensitivity analysis of separable traf<sup>fi</sup>c equilibrium equilibria with application to bilevel optimization in network design, Transportation Research Part B 41 (2007) 4–31.

[35] R.L. Tobin, T.L. Friesz, Sensitivity analysis for equilibrium network <sup>fl</sup>ow, Transportation Science 22 (1988) 242-250

[36] A.L. Dontchev, R.T. Rockafellar, Ample parameterization of variational inclusions, SIAM Iournal on Optimization 12 (2001) 170–187.

[37] M. Patriksson, R.T. Rockafellar, Sensitivity analysis of aggregated variational inequality problems, with application to traf<sup>fi</sup>c equilibrium, Transportation Science 37 (2003) 56–68.

[38] S. Lu, Sensitivity of static traf<sup>fi</sup>c user equilibria with perturbations in arc cost func tion and travel demand, Transportation Science 42 (1) (2008) 105–123.

[39] M. Smith, The existence, uniqueness and stability of traf<sup>fi</sup>c equilibria, Transportation Research 13B (4) (1979) 295–304.

[40] F.F. Clarke, Optimization and Nonsmooth Analysis, John Wiley & Sons, New York, 1983

[41] C. Suwansirikul, T.L. Friesz, R.L. Tobin, Equilibrium decomposed optimization: a heuristic for continuous equilibrium network design problem, Transportation Science 21 (1987) 254–263.

[42] M. Abdulaal, L. LeBlanc, Continuous equilibrium network design models, Transportation Research B 13 (1979) 19–32.

Suh-Wen Chiou received a Bachelor's and Master's degrees in 1990 and 1992 in Transport and Communication Management in NCKU, Taiwan. She received the Ph.D. degree in Transport Studies in 1998 from UCL, University of London, UK. She served as a Research Associate at the Department of Computer Science, KCL, University of London from 1997 to 1999. She took the post as an Assistant Professor at Department of Information Management, Tatung University, Taiwan in 1999. After 2002, she took post as an Assistant and Associate Professor at Information Management Department at National Dong Hwa University, Taiwan. In 2008, she took a chair as a full Professor. Her research interests include decision support systems, transportation and logistics, nonlinear system control and mathematical analysis of network <sup>fl</sup>ow. She is also a member of the editorial advisory board of The Open Transportation Journal, The Open Operational Research Journal and The Open Management Journal.
