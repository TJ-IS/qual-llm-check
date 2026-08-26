---
otero_id: 21091
otero_key: "57G3C8WG"
title: "A weight space-based approach to fuzzy multiple-objective linear programming"
authors: "Ana Rosa Borges; Carlos Henggeler Antunes"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00068-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A weight space-based approach to fuzzy multiple-objective linear programming

Ana Rosa Borges <sup>a,b,</sup>\*, Carlos Henggeler Antunes <sup>b,c</sup>

<sup>a</sup>ISEC-Coimbra Polytechnic Institute, Apartado 10057, Quinta da Nora, 3030-601 Coimbra, Portugal <sup>b</sup>Department of Electrical Engineering, University of Coimbra, Polo II, 3030-030 Coimbra, Portugal <sup>c</sup>INESC-Rua Antero de Quental 199, 3000-033 Coimbra, Portugal

Accepted 31 January 2002

## Abstract

In this paper, the effects of uncertainty on multiple-objective linear programming models are studied using the concepts of fuzzy set theory. The proposed interactive decision support system is based on the interactive exploration of the weight space. The comparative analysis of indifference regions on the various weight spaces (which vary according to intervals of values of the satisfaction degree of objective functions and constraints) enables to study the stability and evolution of the basis that correspond to the calculated efficient solutions with changes of some model parameters. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: multiple-objective linear programming; Fuzzy sets; Interactive methods; Weight space; Efficient solutions; Decision support systems

## 1. Introduction

Most of realistic decision-making problems, essentially those stemming from complex and ill-structured situations, are characterized by the existence of multiple, conflicting and incommensurate objectives and are subject to the unavoidable influence of distinct sources of uncertainty. Therefore, models must take into account vague information, imprecise requirements, modifications of the original input data, imprecision stemming from the modeling phase, needed simplifications, unexpected occurrence of important events and the subjective and evolutive nature of human preference structures whenever multiple objectives and trade-offs are at stake.

Interactive techniques based on the weight space decomposition have been developed and computationally implemented as the core of a decision support system (DSS) to deal with uncertainty in multipleobjective linear programming (MOLP) models by using fuzzy set theory concepts.

The decision maker (DM) has the possibility of interactively changing the membership functions associated with the mathematical constraint relations and the objective functions optimization. It is then possible to evaluate the effects of changing the model parameters and to study alternative scenarios without having to reformulate the problem.

The comparative analysis of the weight spaces corresponding to distinct satisfaction degrees is a valuable tool to study the fuzzy efficient solution set. Among these fuzzy solutions, the DM may choose a satisfactory compromise one according to his/her preference structure which may change as more knowledge about the problem is acquired throughout the interactive decision aid process.

This paper is organized in five sections. The introduction of the main concepts of fuzzy multiple-objective linear optimization problems is made in Section 2. The conceptual aspects of the proposed DSS are presented in Section 3. The example presented in Section 4 aims at illustrating the concepts presented. Some conclusions about the potentialities of this approach are drawn in Section 5.

## 2. Decision making in a fuzzy environment

In classical mathematical programming, multipleobjective problems are concerned with the optimization of multiple, conflicting and incommensurate objective functions subject to constraints representing the availability of limited resources and/or requirements.

The following MOLP problem is considered in this study:

$$
\max \underline {{\mathbf {f}}} (\underline {{\mathbf {x}}}) = C \underline {{\mathbf {x}}}\tag{1}
$$

s.t.

$$
\left. \begin{array}{c} A \underline {{\mathbf {x}}} \{\leq = \geq \} \underline {{\mathbf {b}}} \\ \underline {{\mathbf {x}}} \geq \underline {{\mathbf {0}}} \end{array} \right\} X
$$

where $\underline { { \mathbf { x } } } \in \mathbb { R } ^ { n }$ is the decision variable vector, $\mathbf { C } { \in } \mathbb { R } ^ { p ^ { \times } }$ n is the objective function matrix, $\ b { A } \in \mathbb { R } ^ { m } \ ^ { \times _ { n } }$ is the technological matrix and $\underline { { \mathbf { b } } } \in \mathbb { R } ^ { m }$ is the right-hand side vector.

Constraints separate all possible solutions into two distinct sets: those which are feasible (X) and those which are not feasible. Objective functions are to be pursued to the greatest possible extent with regard to the feasible region. However, since the objective functions are generally in conflict, there is not usually a solution that optimize all the objective functions at the same time. The concept of optimal solution to a single objective problem gives, thus, place in a multiple-objective context to the concept of efficient solutions: feasible solutions for which no improvement in any objective function is possible without sacrificing on at least one of the other objective functions. These problems entail analyzing trade-offs among the objectives in order to get a satisfactory compromise from the set of efficient solutions.

Let us consider $p$ objective functions $\underline { { \mathbf { f } } } ( \underline { { \mathbf { x } } } ) { = } ( f _ { 1 } ( \underline { { \mathbf { x } } } )$ 2 $f _ { 2 } ( \underline { { \mathbf { x } } } ) , . . . , f _ { p } ( \underline { { \mathbf { x } } } ) )$ , which are to be maximized in a feasible region X.

$\underline { { \overline { { \mathbf { x } } } } } { \in } X$ is an efficient solution, if and only if no $\underline { { \hat { \mathbf { x } } } } { \in } X$ exists such that

$$
\begin{array}{l} f _ {k} (\underline {{\hat {\mathbf {x}}}}) \geq f _ {k} (\overline {{\mathbf {x}}}), \text {   for   } k = 1, \ldots , p \quad \text { and } \\ f _ {k} (\underline {{\hat {\mathbf {x}}}}) > f _ {k} (\overline {{\mathbf {x}}}), \text {   for   at   least   one   } k = 1, \ldots , p \end{array}\tag{2}
$$

The concept of efficient solution generally refers to the variable space whereas the nondominance concept refers to the corresponding image in the objective function space. That is, if $\underline { { \mathbf { X } } }$ is efficient then $\pmb { f } ( \underline { { \boldsymbol { x } } } )$ is nondominated.

In a fuzzy environment, the main purpose is to find the ‘‘most satisfactory’’ solution under incomplete, subjective, imprecise and/or vague information. In the symmetric model proposed by Bellman and Zadeh [1], there is no difference between objectives and constraints. A fuzzy decision can be viewed as a fuzzy set $\tilde { D }$ resulting from the intersection of fuzzy goals $\tilde { G } _ { k }$ and fuzzy problem constraints ${ \tilde { C } } _ { i }$

$$
\tilde {D} = \tilde {G} _ {1} \cap \tilde {G} _ {2} \cap \dots \cap \tilde {G} _ {p} \cap \tilde {C} _ {1} \cap \tilde {C} _ {2} \cap \dots \cap \tilde {C} _ {m}\tag{3}
$$

An optimal decision is an element with maximum degree of membership to this set. Generally, the most convenient way to model intersection is the minimum operator. If all membership functions $\mu _ { j } ( \underline { { \mathbf { x } } } )$ are known in a space of alternatives $X ( \mu _ { j } ( { \underline { { \mathbf { x } } } } ) { : } X { \longrightarrow } [ 0 , 1 ] )$ , then the fuzzy decision is defined by:

$$
\begin{array}{l} \mu_ {\tilde {D}} (\underline {{\mathbf {x}}}) = \min \{\mu_ {\tilde {G} _ {1}} (\underline {{\mathbf {x}}}),   \mu_ {\tilde {G} _ {2}} (\underline {{\mathbf {x}}}),   \ldots ,   \mu_ {\tilde {G} _ {p}} (\underline {{\mathbf {x}}}), \\ \mu_ {\tilde {C} _ {1}} (\underline {{\mathbf {x}}}),   \mu_ {\tilde {C} _ {2}} (\underline {{\mathbf {x}}}),   \ldots ,   \mu_ {\tilde {C} _ {m}} (\underline {{\mathbf {x}}}) \} \\ \qquad = \min \{\mu_ {j} (\underline {{\mathbf {x}}}) \},   \text { for all }   \underline {{\mathbf {x}}} \end{array}\tag{4}
$$

and the optimal decision by:

$$
\max \mu_ {\tilde {D}} (\underline {{\mathbf {x}}}) = \max [ \min \{\mu_ {j} (\underline {{\mathbf {x}}}) \} ], \text {   for   all   } \underline {{\mathbf {x}}}\tag{5}
$$

Werners $[ 8 , 9 ]$ proposed the generalization of the classical efficient solution definition for the fuzzy multiple-objective linear programming (FMOLP)

model with flexible constraints and crisp objective functions.

Let m be the number of membership functions of the constraints $\mu _ { \tilde { C } , } ( { \bf x } ) \colon X \longrightarrow [ 0 , 1 ] , i = 1 , 2 , . . . , m .$

x<sup>a</sup>X is a fuzzy efficient solution, if and only if no $\underline { { \hat { \mathbf { x } } } } { \in } X$ exists such that

$$
\begin{array}{l} f _ {k} (\underline {{\hat {\mathbf {x}}}}) \geq f _ {k} (\overline {{\underline {{\mathbf {x}}}}}), \text { for } k = 1, \ldots , p \quad \text { and } \\ \mu_ {\tilde {C} _ {i}} (\underline {{\hat {\mathbf {x}}}}) \geq \mu_ {\tilde {C} _ {i}} (\overline {{\underline {{\mathbf {x}}}}}), \text { for } i = 1, \ldots , m \quad \text { and } \\ [ f _ {k} (\underline {{\hat {\mathbf {x}}}}) > f _ {k} (\overline {{\underline {{\mathbf {x}}}}}), \text { for   at   least   one } k = 1, \ldots , p \quad \text { or } \\ \mu_ {\tilde {C} _ {i}} (\underline {{\hat {\mathbf {x}}}}) > \mu_ {\tilde {C} _ {i}} (\overline {{\underline {{\mathbf {x}}}}}), \text { for   at   least   one } i = 1, \ldots , m ] \end{array}\tag{6}
$$

The set of all fuzzy efficient solutions is called the fuzzy complete solution [8,9].

By comparing the definitions of crisp $\left( \operatorname { E q . } \left( 2 \right) \right)$ and fuzzy (Eq. (6)) efficient solutions, this latter takes into account that an improvement in an objective function can only be obtained either at the expense of another objective function or at the expense of the degree of membership to the constraints.

The following example illustrates how this generalization has been done. Let us consider the problem, already studied by Zimmermann [12], with two objective functions, $f _ { 1 } ( \underline { { \mathbf { x } } } ) = - x _ { 1 } + 2 x _ { 2 } , f _ { 2 } ( \underline { { \mathbf { x } } } ) = 2 x _ { 1 } + x _ { 2 } ,$ and four constraints $\mathbf { X } = \{ \underline { { \mathbf { x } } } \in \mathbb { R } ^ { 2 } | \mathbf { c } _ { 1 } : - x _ { 1 } + 3 x _ { 2 } \leq 2 1 ;$ $\mathbf { c } _ { 2 } : x _ { 1 } + 3 x _ { 2 } \leq 2 7 ; \mathbf { c } _ { 3 } : 4 x _ { 1 } + 3 x _ { 2 } { \leq } 4 5 ; \mathbf { c } _ { 4 } : 3 x _ { 1 } + x _ { 2 } { \leq }$ $3 0 ; x _ { 1 } { \ge } 0 ; x _ { 2 } { \ge } 0 \}$ (let us consider that the first and second constraints are fuzzy ones). Fig. 1 shows the fuzzy region of feasible solutions in the objective function space, where the subregion with membership values $( \mu _ { \tilde { c } _ { 1 } }$ and $\mu _ { \tilde { c } _ { \gamma } } )$ between $\cdot _ { 0 } ,$ and $^ { \mathfrak { \ell } _ { 1 } , }$ is the union of the vertical and horizontal hatched regions.

In case that all constraints and objectives are crisp (as in classical optimization), $P _ { \mathbf { A } }$ and $P _ { \mathrm { { D } } }$ are the individual optima of $f _ { 1 } ( \underline { { \mathbf { x } } } )$ and $f _ { 2 } ( \underline { { \mathbf { x } } } )$ , respectively. The set of efficient solutions contains all points on the lines $[ P _ { \mathrm { A } } , P _ { \mathrm { B } } ] , [ P _ { \mathrm { B } } , P _ { \mathrm { C } } ]$ and $[ P _ { \mathrm { C } } , P _ { \mathrm { D } } ]$

In a fuzzy environment, feasible solutions can be distinct by their degrees of feasibility (membership function values). Therefore, the set of fuzzy efficient solutions includes all points on the lines $[ P _ { \mathrm { A } } , P _ { \mathrm { B } } ] _ { \mathrm { : } }$ $[ P _ { \mathrm { B } } , P _ { \mathrm { C } } ]$ and $[ P _ { \mathrm { C } } , P _ { \mathrm { D } } ] ,$ , as well as the hatched section of the feasible region including the boundaries, that is all points which can be obtained by a convex combination of $\{ P _ { \mathrm { A } } , P _ { \mathrm { N } } , P _ { \mathrm { M } } , P _ { \mathrm { L } } , P _ { \mathrm { I } } \}$ and of $\{ P _ { \mathrm C } , P _ { \mathrm M } , P _ { \mathrm L } , P _ { \mathrm J } \}$

![](/api/attachments/57G3C8WG/fulltext/images/b33b8b6743015e7624f9dfc7c7489a8ab7b25a0245c4fcbadc7d665c9308433c.jpg)  
Fig. 1. Example—fuzzy region of feasible solutions in the objective function space for a problem with fuzzy constraints.

Definition (6) leads to fuzzy efficient solutions which are not feasible in a crisp environment (in Fig. 1, all solutions for which $0 \leq \mu _ { \tilde { c } _ { 1 } } < 1$ and $0 \leq \mu _ { \tilde { c } _ { 7 } } < 1 )$ . It may also happen that a solution for which all objective function values are worse than those of another solution is still fuzzy efficient, provided that at least one membership function value of the constraints is higher. For example, the point $P _ { \mathrm { I } }$ is not feasible in a crisp environment, but it is feasible and fuzzy efficient in a fuzzy environment. With respect to $P _ { \mathrm { A } } , P _ { \mathrm { I } }$ has better values for both objectives but a worse membership value with respect to the first fuzzy constraint. Both are efficient in a fuzzy environment.

## 3. An interactive decision support system

Unlike classical linear programming, in a fuzzy environment there is more than just a single model formulation.

Several authors [6,7] consider a broad distinction in fuzzy programming: flexible and robust programming problems. In flexible programming problems, the structure of models is fixed (all coefficients involved are known) and the mathematical relations involved are fuzzy (fuzzy objectives and constraints). In robust programming problems, the structure of the models is not known exactly, that is the model coefficients cannot be precisely given.

The solution of a fuzzy linear programming problem may be crisp [8–14] or fuzzy [2,3]. In the latter case, a solution set is presented to the DM and he/she must choose the ‘‘best’’ compromise one, according to his/her preferences.

In Zimmermann’s [11–14] approach, a fuzzy linear programming problem with fuzzy objectives and fuzzy constraints is to be solved. All these are fuzzy inequality constraints represented by linear membership functions. If $\mu _ { \mathrm { D } } ( \underline { { \mathbf { x } } } )$ has a unique value, $\mu _ { \mathrm { D } } ( \underline { { \mathbf { x } } } _ { 0 } ) { = } \operatorname* { m a x } \ \mu _ { \mathrm { D } } ( \underline { { \mathbf { x } } } )$ , then $\underline { { \boldsymbol { x } } } _ { 0 } .$ which is an element of the complete solution set $\underline { { \boldsymbol { x } } } ,$ can be derived by solving a classical linear programming problem with one more variable $\lambda . \ \lambda$ is interpreted as the degree of satisfaction of the fuzzy objectives and constraints. It is suggested [11] that the use of the individual optima as upper bounds and ‘‘least justifiable’’ solutions as lower bounds be made to define the membership functions associated with the objectives.

Considering the example presented in Section $^ { 2 , }$ the maximum degree of overall satisfaction $\lambda { = } 0 . 7 4 2$ is achieved for the solution $\underline { { \mathbf { x } } } \mathrm { = } ( 5 . 0 3 ; 7 . 3 2 ) ^ { T } ,$ that is point $P _ { \mathrm { F } }$ in Fig. 2.

The optimal solution of Zimmermann’s model belongs to the fuzzy efficient solution set in the proposed approach. For specific membership functions, the optimal Zimmermann’s solution can be reached as the efficient extreme solution obtained with maximum satisfaction degree (of the fuzzy objectives and constraints presented in the model).

Chanas [3] showed that the complete fuzzy decision set x rather than only $\underline { { \boldsymbol { x } } } _ { 0 }$ can be derived by using parametric programming. Instead of $\mu _ { \mathrm { D } } ( \underline { { \mathbf { x } } } ) , \mu _ { \mathrm { D } } ( \theta )$ is calculated. h is interpreted as the degree of violation of the constraints.

The parametric approach by Carlsson and Korhonen [2] is applied to problems where A, b and C might be totally or partially fuzzy. The range of the possible parameters must be given by the DM. Although the authors related that parametric programming is used, in practice they set specific values within the overall degree of satisfaction $( \mu { = } 0 . 0 , 0 . 1 , 0 . 2 , . . . , 0 . 9 , 1 )$ and several linear programming problems are then solved using these values.

The interactive DSS presented by Werners [8,9] helps solving FMOLP problems with fuzzy objectives and fuzzy constraints, but the goals are not given a priori by the DM. The system’s main purpose is to find the ‘‘best’’ compromise solution or to conclude that no compromise solution satisfying those requirements exists.

The interactive FMOLP approach herein developed can incorporate uncertainty elements into the optimization operation, and into the mathematical relations of the constraints or into the constraints right-hand sides. The aim of the proposed interactive DSS is to help the DM to gather knowledge about the fuzzy problem and to exploit his/her convictions and (evolutionary) preference system, in order to make a better informed decision, rather than converging to a ‘‘best’’ compromise solution, as in the Werners [8,9] approach. There are no irrevocable decisions throughout the interactive process and the DM is always allowed to revise prior preference information and exploit new search directions.

It is particularly suited to problems with two or three objective functions (or those that can be converted into problems with two or three objective functions), in order to profit from the display of the weight space and objective function space. Based on the comparative analysis of the various weight spaces and objective function spaces as well as on the numerical information obtained in each interaction, the DM can interactively change the membership functions considered in the model and the relative importance of the objectives in order to direct the search to new regions. In this way it is possible to compare different scenarios and study the stability and evolution of the basis which correspond to the calculated efficient solutions.

![](/api/attachments/57G3C8WG/fulltext/images/53eaf4721d8066dc8f6b995c83e8c9f005157d0467441463fbee95f1dcb90c33.jpg)  
Fig. 2. Example—fuzzy region of feasible solutions in the objective function space for a problem with fuzzy objectives

## 3.1. Introductory concepts

The definition of fuzzy efficient solution for a MOLP model with flexible constraints and crisp objectives has been presented in Section 2. The generalization of this definition for problems where some objective functions are flexible is possible. The study of all fuzzy efficient solutions can be made, in the proposed approach, based on that generalization.

Let us consider the example presented in Section 2. In Zimmermann’s [11 –14] approach, the membership functions associated with the objectives are defined by considering the individual optima as upper bounds and the ‘‘least justifiable’’ solutions as lower bounds. However, other values might be considered to define them. If, for example, the decision maker assumes that he/she is not interested in solutions with a negative value for the first objective function the lower bound of $f _ { 1 } ( \underline { { \mathbf { x } } } )$ is set to zero. In this situation, the maximum degree of overall satisfaction $\lambda { = } 0 . 7 1$ 4 is achieved for the solution $\underline { { \mathbf { x } } } = ( 4 . 8 ; 7 . 4 ) ^ { T } ,$ , that is point $P _ { \mathrm { H } }$ in Fig. 3.

In Fig. 4, we consider that the membership functions associated with the objectives are defined as those in Fig. 3 and the membership functions associated with the constraints are defined as in Fig. 1.

The set of fuzzy efficient solutions in the flexible environment includes all points which are convex combination of $P _ { \mathrm { A } } , P _ { \mathrm { I } } , P _ { \mathrm { L } } , P _ { \mathrm { M } } , P _ { \mathrm { G } }$ and $P _ { 1 } ^ { \prime }$ in Fig. 4.

These solutions are such that for each one it is not possible to improve the membership degree in relation to one fuzzy set (corresponding to all the fuzzy objectives and constraints) without worsening w.r.t. another one.

![](/api/attachments/57G3C8WG/fulltext/images/9b2d02b8ce471b0ab220ad0391aae8b45fe3fc546af2946ce59efd1eff62bdb2.jpg)  
Fig. 3. Example—fuzzy region of feasible solutions in the objective function space for a problem with fuzzy objectives.

If we are only interested in the fuzzy efficient solution which has the maximum degree of overall satisfaction k (for all the fuzzy objectives and constraints), it is achieved on point $P _ { \mathrm { { P } } }$ in Fig. 4, with $\lambda { = } 0 . 7 9$

![](/api/attachments/57G3C8WG/fulltext/images/625752012349f402ff2b888cd5d0b2be7bb7ae2ad076dd135f2bd98503f06e9a.jpg)  
Fig. 4. Example—fuzzy region of feasible solutions in the objective function space for a problem with fuzzy objectives and constraints

We can now define a fuzzy efficient solution for MOLP models with flexible constraints and objective functions as follows.

Let $\mu _ { \tilde { G } _ { k } } ( \underline { { { \mathbf { x } } } } ) \colon \boldsymbol { X } \longrightarrow [ 0 , 1 ] , \ k = 1 , \ 2 , \ . . . , \ p ,$ , be the objective membership functions (which are to be maximized, without loss of generality) and $\mu _ { \tilde { C } _ { \mathrm { i } } } ( \underline { { \mathbf { x } } } ) ;$ $X \longrightarrow [ 0 , 1 ] , i = 1 , 2 , . . . , m$ , the constraints’ membership functions.

![](/api/attachments/57G3C8WG/fulltext/images/07cc33327e055731f00dbd9e2bca023b8a7a93a39c7858499244797b23045b7c.jpg)  
Fig. 5. Block diagram of the proposed approach.

(a)  
![](/api/attachments/57G3C8WG/fulltext/images/d3617f7d07714279880ee599e21ba28025d600933e65f70cafe6a3c6cc18875f.jpg)

(b)  
![](/api/attachments/57G3C8WG/fulltext/images/4d2951ddc59ce8e4ef3960d169897e49340be4296f71f893f9b25ca1d700e9e4.jpg)  
(c)

![](/api/attachments/57G3C8WG/fulltext/images/af543d716b52efa4ca289fd15cba022e3bc3f3b46e789573ab613e7111c2b588.jpg)  
Fig. 6. Membership functions used in the model (a – c).

$\underline { { \overline { { \mathbf { x } } } } } { \in } X$ is a fuzzy efficient solution, if and only if no $\underline { { \hat { \mathbf { x } } } } { \in } \overline { { X } }$ exists such that

$\mu _ { \tilde { G } k } ( \underline { { \hat { \mathbf { x } } } } ) { \geq } \mu _ { \tilde { G } k } ( \overline { { \underline { { \mathbf { x } } } } } )$ , for k ¼ 1, . . . , p and

$\mu _ { \tilde { C } _ { i } } ( \underline { { \hat { \mathbf { x } } } } ) { \geq } \mu _ { \tilde { C } _ { i } } ( \overline { { \mathbf { x } } } )$ , for i ¼ 1, . . . , m and $\begin{array} { r } { [ \mu _ { \tilde { G } k } ( \underline { { \hat { \mathbf { x } } } } ) > \mu _ { \tilde { G } k } ( \underline { { \overline { { \mathbf { x } } } } } ) , } \\ { = 1 , \ . . . , } \end{array}$ for at least one $k$ p or

$$
\begin{array}{l} \mu_ {\tilde {C} _ {i}} (\underline {{\hat {\mathbf {x}}}}) > \mu_ {\tilde {C} _ {i}} (\overline {{\underline {{\mathbf {x}}}}}), \text {   for   at   least   one   } i \\ = 1, \ldots , m ] \end{array}\tag{7}
$$

## 3.2. The interactive FMOLP approach

In what follows, we will present an interactive FMOLP approach which has been computationally implemented as a DSS as an extension of the TRI-MAP method [4,5]. Fig. 4 and the block diagram shown in Fig. 5 sketch how it works.

All membership functions used in the model possess a piecewise linear structure as those shown in Fig. 6a, b and c.

For each $\cdot _ { i } \cdot$ fuzzy constraint, the DM specifies the membership functions in the following manner:

For $\textbf { a } \lessapprox$ constraint (submatrix $A ^ { 1 }$ of $A ) _ { i }$ , the DM specifies values ${ \underline { { b _ { i } } } } ^ { 1 }$ and $\bar { b _ { i } } ^ { 1 }$ . An excess of $\bar { b _ { i } } ^ { 1 }$ is not allowed in any case, and the constraint is completely satisfied for values not above $\underline { { b } } _ { i } ^ { 1 } ( \mathrm { F i g }$ $\mathrm { 6 a ) }$

For $\mathrm { ~ a ~ } \gtrapprox$ constraint (submatrix $A ^ { 2 }$ of $A )$ , the DM specifies values ${ \underline { { b _ { \mathrm { i } } } } } ^ { 2 }$ and ${ \bar { b } } _ { i } ^ { 2 }$ . The constraint is completely satisfied for values not below ${ { \bar { b } } _ { i } } ^ { 2 }$ and a value lower than ${ \underline { { b _ { i } } } } ^ { 2 }$ is not allowed in any case (Fig. 6b).

For $\mathrm { ~ a ~ } \equiv$ constraint (submatrix $A ^ { 3 }$ of $A ) ,$ , the membership function is determined by three values, ${ \underline { { b _ { i } } } } ^ { 3 } , \ { b _ { i } } ^ { 3 }$ and $\bar { b _ { i } } ^ { 3 } . \ b _ { i } ^ { 3 }$ should be met, while a maximal deviation up to ${ \underline { { b } } } _ { i } ^ { 3 }$ or $\bar { b _ { i } } ^ { 3 }$ is still acceptable (Fig. 6c).

Because of the model formulation ${ \underline { { b _ { i } } } } ^ { r } \leq { b _ { i } } ^ { r } \leq \bar { b _ { i } } ^ { r }$ always holds.

The main difference between crisp and fuzzy constraints is that in case of crisp constraints the DM can strictly differentiate between feasibility and infeasibility and in case of fuzzy constraints he/she wants to consider a certain degree of feasibility in the interval $[ { \underline { { b } } } _ { i } ^ { r } { \bar { \mathcal { b } } } _ { i } ^ { r } ]$

The fuzzy objectives for which the DM is able to indicate the goals and the maximally acceptable tolerance (or $\underline { { b } } _ { i }$ and $\bar { b _ { i } } )$ can be considered fuzzy constraints in the model.

Table 1 Efficient extreme solutions

<table><tr><td></td><td colspan="2"> $\underline{\mathbf{c}_{1}\underline{\mathbf{x}}}$ </td><td colspan="2"> $\underline{\mathbf{c}_{2}\underline{\mathbf{x}}}$ </td><td>...</td><td colspan="2"> $\underline{\mathbf{c}_{p}\underline{\mathbf{x}}}$ </td></tr><tr><td>Solution 1-1 ( $x^{11}$ )</td><td colspan="2"> $\sum_{j} c_{1j}x_{j}^{11}$ </td><td colspan="2"> $\sum_{j} c_{2j}x_{j}^{11}$ </td><td>...</td><td colspan="2"> $\sum_{j} c_{pj}x_{j}^{11}$ </td></tr><tr><td> $\vdots$ </td><td colspan="2"></td><td colspan="2"></td><td></td><td colspan="2"></td></tr><tr><td>Solution 1-p ( $x^{1p}$ )</td><td colspan="2"> $\sum_{j} c_{1j}x_{j}^{1p}$ </td><td colspan="2"> $\sum_{j} c_{2j}x_{j}^{1p}$ </td><td>...</td><td colspan="2"> $\sum_{j} c_{pj}x_{j}^{1p}$ </td></tr><tr><td>Solution 0-1 ( $x^{01}$ )</td><td colspan="2"> $\sum_{j} c_{1j}x_{j}^{01}$ </td><td colspan="2"> $\sum_{j} c_{2j}x_{j}^{01}$ </td><td>...</td><td colspan="2"> $\sum_{j} c_{pj}x_{j}^{01}$ </td></tr><tr><td> $\vdots$ </td><td colspan="2"></td><td colspan="2"></td><td></td><td colspan="2"></td></tr><tr><td>Solution 0-p ( $x^{0p}$ )</td><td colspan="2"> $\sum_{j} c_{1j}x_{j}^{0p}$ </td><td colspan="2"> $\sum_{j} c_{2j}x_{j}^{0p}$ </td><td>...</td><td colspan="2"> $\sum_{j} c_{pj}x_{j}^{0p}$ </td></tr></table>

The model consists of $p$ linear objective functions and m constraints, where some of the objective functions and constraints may be defined in a fuzzy manner:

$$
\widetilde {\max} \underline {{\mathbf {f}}} (\underline {{\mathbf {x}}}) = C \underline {{\mathbf {x}}} (p \text {   objective   functions })\tag{8}
$$

s.t.

$$
A ^ {1} \underline {{{\mathbf {x}}}} \leq \underline {{{\underline {{{\mathbf {b}}}}}}} ^ {1}, \bar {\underline {{{\mathbf {b}}}}} ^ {1} \quad (m _ {1} \text {   constraints })
$$

$$
A ^ {2} \underline {{{\mathbf {x}}}} \geq \underline {{{\mathbf {b}}}} ^ {2}, \bar {\underline {{{\mathbf {b}}}}} ^ {2} \quad (m _ {2} \text {   constraints })
$$

$$
A ^ {3} \underline {{{\mathbf {x}}}} \equiv \underline {{{\underline {{{\mathbf {b}}}}}}} ^ {3}, \underline {{{\mathbf {b}}}} ^ {3}, \bar {\underline {{{\mathbf {b}}}}} ^ {3} \quad (m _ {3} \text {   constraints })
$$

$$
\left. \begin{array}{l} D ^ {1} \underline {{\mathbf {x}}} \leq \underline {{\mathbf {d}}} ^ {1} \\ D ^ {2} \underline {{\mathbf {x}}} \geq \underline {{\mathbf {d}}} ^ {2} \\ D ^ {3} \underline {{\mathbf {x}}} = \underline {{\mathbf {d}}} ^ {3} \\ \underline {{\mathbf {x}}} \geq \underline {{0}} \end{array} \right\} X
$$

where $\underline { { \mathbf { b } } } ^ { r } , ~ \underline { { \bar { \mathbf { b } } } } ^ { r }$ and $\underline { { \mathbf { b } } } ^ { r }$ are the column vectors associated with the membership values $\underline { { b _ { i } ^ { r } } } , ~ \bar { b _ { i } } ^ { r }$ and $b _ { i } ^ { r } , r = 1 , 2 , 3$

Illustrative example — extreme solutions

<table><tr><td></td><td>Maximize  $f_1$ </td><td>Maximize  $f_2$ </td><td>Maximize  $f_3$ </td></tr><tr><td>Solution 1 – 1</td><td>66</td><td>30</td><td>-12</td></tr><tr><td>Solution 1 – 2</td><td>12.5</td><td>50</td><td>25</td></tr><tr><td>Solution 1 – 3</td><td>15</td><td>-15</td><td>75</td></tr></table>

In the proposed approach, there is initially a noninteractive step aimed at offering the DM an overview of the range of values that the objective functions can attain within the efficient region.

Each objective function is separately optimized with $\mathsf { \Omega } \mathsf { z } = 1$ and $\scriptstyle { \alpha = 0 }$ in the region

$$
\begin{array}{l l}A ^ {1} \underline {{\mathbf {x}}} \leq \underline {{\mathbf {b}}} ^ {1} + \alpha (\underline {{\mathbf {b}}} ^ {1} - \underline {{\mathbf {b}}} ^ {1})&(m _ {1} \leq \text { constraint })\\A ^ {2} \underline {{\mathbf {x}}} \geq \underline {{\mathbf {b}}} ^ {2} + \alpha (\underline {{\mathbf {b}}} ^ {2} - \underline {{\mathbf {b}}} ^ {2})&(m _ {2} \geq \text { constraints })\\A ^ {3} \underline {{\mathbf {x}}} \leq \underline {{\mathbf {b}}} ^ {3} + \alpha (\underline {{\mathbf {b}}} ^ {3} - \underline {{\mathbf {b}}} ^ {3})&(m _ {3} \rightleftharpoons \text { constraints })\\A ^ {3} \underline {{\mathbf {x}}} \geq \underline {{\mathbf {b}}} ^ {3} + \alpha (\underline {{\mathbf {b}}} ^ {3} - \underline {{\mathbf {b}}} ^ {3})&(m _ {3} \rightleftharpoons \text { constraints })\\\underline {{\mathbf {x}}} \in X\end{array}\tag{9}
$$

a can be interpreted as the satisfaction degree of the fuzzy objectives and constraints in the model. The region considered in problem (9) is the feasible region to the initial problem considering crisp constraints $( \alpha = 1 )$ and considering fuzzy constraints with maximum fuzziness (a = 0).

Table 1 is then obtained where solutions $1 - k , k = 1$ $2 , \ldots , p ,$ are the efficient extreme solutions for $\mathsf { \Omega } \mathsf { z } = 1$ and solutions $0 - k , k = 1 , 2 , \ldots , p ,$ the efficient extreme solutions for $\scriptstyle { \alpha = 0 }$ . Table 1 is a double ‘‘pay-off’’ table, the upper part considering crisp constraints $( \alpha = 1 )$ and the lower part obtained with maximum fuzziness $( \alpha = 0 )$ . If the model contains crisp constraints only, the lower part of the table will not exist.

In case that some optimal solutions cannot be computed (because the linear models does not possess a feasible solution or it is not bounded) the appropriate information is shown on the corresponding row in Table 1.

Based on this information, the system suggests the membership functions of the existing objective functions. The diagonal in the lower half part of the table contains the maximally achievable objective functions values $\bar { \mathsf { c } } _ { k } .$ . The pessimistic values $\underline { { \mathbf { c } } } _ { k }$ are determined by choosing the minimum in column k (not necessarily the worst values in the efficient region, but the worst in the individual optima table range; however, these values are convenient because they are very simple to determine).

Illustrative example — bounds used to define the membership functions associated with the fuzzy objectives and constraints

<table><tr><td colspan="3">Objective functions</td><td colspan="3">Constraints</td></tr><tr><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td></tr><tr><td>[36, 66]</td><td>[20, 50]</td><td>[45, 75]</td><td>[60, 66]</td><td>[60, 84]</td><td>[50, 60]</td></tr></table>

Table 4 Illustrative example

<table><tr><td rowspan="2"></td><td colspan="3">Objective functions</td><td colspan="3">Constraints</td></tr><tr><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td></tr><tr><td colspan="7">(a) Compromise solution 1</td></tr><tr><td> $x_1=12.17-13.76\alpha$ </td><td>61.88-37.32 $\alpha$ </td><td>20+30 $\alpha$ </td><td>45+30 $\alpha$ </td><td>66-6 $\alpha$ </td><td>84-24 $\alpha$ </td><td>56.59+23.12 $\alpha$ </td></tr><tr><td> $x_2=9.68-1.02\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_3=7.54-3.80\alpha$ </td><td>[61.88, 58.03]</td><td>[20, 23.09]</td><td>[45, 48.09]</td><td>[66, 65.38]</td><td>[84, 81.53]</td><td>[56.59, 58.97]</td></tr><tr><td> $x_4=0.61+12.59\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_f_1=25.88-67.32\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_c_3=3.41-33.12\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0≤ $\alpha$ ≤0.103093</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_1=10.75-8.40\alpha$ </td><td>58.03-53.15 $\alpha$ </td><td>23.09+18.33 $\alpha$ </td><td>48.09+18.33 $\alpha$ </td><td>65.38-54.25 $\alpha$ </td><td>81.53-14.66 $\alpha$ </td><td>58.97-6.11 $\alpha$ </td></tr><tr><td> $x_2=9.58-0.63\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_3=7.14-22.56\alpha$ </td><td>[52.56, 43.95]</td><td>[24.98, 27.95]</td><td>[49.98, 52.95]</td><td>[59.79, 51.01]</td><td>[80.01, 77.64]</td><td>[58.34, 57.35]</td></tr><tr><td> $x_4=1.91+17.81\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_f_1=18.94-71.48\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_c_1=0+50.59\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.103093≤ $\alpha$ ≤0.264957</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">(b) Compromise solution 2</td></tr><tr><td> $x_1=6.51+9.57\alpha$ </td><td>36+30 $\alpha$ </td><td>41.43-47.02 $\alpha$ </td><td>45+30 $\alpha$ </td><td>50.04-1.70 $\alpha$ </td><td>64.85+53.96 $\alpha$ </td><td>60-10 $\alpha$ </td></tr><tr><td> $x_2=6.19+12.34\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_4=10.28-11.06\alpha$ </td><td>[36, 43.18]</td><td>[41.43, 30.16]</td><td>[45, 52.18]</td><td>[50.04, 49.63]</td><td>[64.85, 78.25]</td><td>[60, 57.61]</td></tr><tr><td> $s\_f_2=21.43-77.02\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_c_1=15.96-4.30\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_c_2=19.15-79.96\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0≤ $\alpha$ ≤0.239489</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_1=8.80-1.05\alpha$ </td><td>43.18+2.88 $\alpha$ </td><td>30.16-8.36 $\alpha$ </td><td>52.18+2.88 $\alpha$ </td><td>49.63+5.18 $\alpha$ </td><td>78.25-2.31 $\alpha$ </td><td>57.61-0.96 $\alpha$ </td></tr><tr><td> $x_2=9.15+1.00\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_3=0+4.41\alpha$ </td><td>[43.88, 43.95]</td><td>[28.16, 27.95]</td><td>[52.88, 52.95]</td><td>[50.88, 51.01]</td><td>[77.70, 77.64]</td><td>[57.37, 57.35]</td></tr><tr><td> $x_4=7.63-3.78\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_f_2=2.98-11.25\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_c_1=14.93-5.76\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.239489≤ $\alpha$ ≤0.264957</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">(c) Compromise solution 3</td></tr><tr><td> $x_1=5.21+14.24\alpha$ </td><td>36+30 $\alpha$ </td><td>20+30 $\alpha$ </td><td>75.52-79.70 $\alpha$ </td><td>44.85+16.97 $\alpha$ </td><td>83.03-9.39 $\alpha$ </td><td>60-10 $\alpha$ </td></tr><tr><td> $x_2=13.33-13.33\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_4=7.03+0.61\alpha$ </td><td>[36, 37.99]</td><td>[20, 21.99]</td><td>[75.52, 70.22]</td><td>[44.85, 45.98]</td><td>[83.03, 82.41]</td><td>[60, 59.34]</td></tr><tr><td> $s\_f_3=30.52-109.70\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_c_1=21.15-22.97\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_c_2=0.97-14.61\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0≤ $\alpha$ ≤0.06639</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_1=6.16+8.94\alpha$ </td><td>37.99+22.48 $\alpha$ </td><td>21.99+22.48 $\alpha$ </td><td>70.22-65.20 $\alpha$ </td><td>45.98+18.99 $\alpha$ </td><td>82.41-17.99 $\alpha$ </td><td>59.34-7.49 $\alpha$ </td></tr><tr><td> $x_2=12.45-11.46\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_3=0+4.41\alpha$ </td><td>[39.48, 43.95]</td><td>[23.48, 27.95]</td><td>[65.90, 52.95]</td><td>[47.24, 51.01]</td><td>[81.21, 77.64]</td><td>[58.84, 57.35]</td></tr><tr><td> $x_4=7.07-1.68\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_f_3=23.23-87.68\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $s\_c_1=19.63-23.49\alpha$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.06639≤ $\alpha$ ≤0.264957</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The interactive process begins at this point. The DM can now reformulate the membership functions associated with objectives and constraints or accept the suggestions given by the method.

The application of parametric programming to the p linear problems corresponding to the optimization of each objective function in the region

$$
\begin{array}{l l} C \underline {{\mathbf {x}}} \geq \underline {{\underline {{\mathbf {c}}}}} + \alpha (\underline {{\mathbf {c}}} - \underline {{\underline {{\mathbf {c}}}}}) & (p \text {   objective functions }) \\ A ^ {1} \underline {{\mathbf {x}}} \leq \underline {{\mathbf {b}}} ^ {1} + \alpha (\underline {{\underline {{\mathbf {b}}}}} ^ {1} - \underline {{\mathbf {b}}} ^ {1}) & (m _ {1} \leq \text {   constraints }) \\ A ^ {2} \underline {{\mathbf {x}}} \geq \underline {{\underline {{\mathbf {b}}}}} ^ {2} + \alpha (\underline {{\mathbf {b}}} ^ {2} - \underline {{\underline {{\mathbf {b}}}}} ^ {2}) & (m _ {2} \geq \text {   constraints }) \\ A ^ {3} \underline {{\mathbf {x}}} \leq \underline {{\mathbf {b}}} ^ {3} + \alpha (\underline {{\mathbf {b}}} ^ {3} - \underline {{\mathbf {b}}} ^ {3}) & (m _ {3} \equiv \text {   constraints }) \\ A ^ {3} \underline {{\mathbf {x}}} \geq \underline {{\underline {{\mathbf {b}}}}} ^ {3} + \alpha (\underline {{\mathbf {b}}} ^ {3} - \underline {{\underline {{\mathbf {b}}}}} ^ {3}) & (m _ {3} \equiv \text {   constraints }) \\ \underline {{\mathbf {x}}} \in X, \alpha \in [ 0, 1 ]. \end{array}\tag{10}
$$

yields a set of $p$ fuzzy compromise solutions, which are analytically dependent on the parameter a. The a bounds corresponding to the same optimal basis for each fuzzy compromise solution are ordered. That is, the method computes, for each objective function separately, the ranges for the satisfaction degree of the fuzzy objectives and constraints in the model (a) that lead to the same efficient basis.

The region defined by Eq. (10) contains all solutions for which at least one of the membership function values is not zero. In the limit situation, all the degrees may be zero.

If the DM considers that the obtained information is sufficient to make a decision, the process can successfully be concluded, otherwise this interactive step can be repeated with other membership functions or a second interactive phase may begin.

$$
\begin{array}{l l} \max \left[ \sum_ {k = 1} ^ {p} (w _ {k} f _ {k} (\underline {{\mathbf {x}}})) \right] \\ \text {s.t.} \\ C \underline {{\mathbf {x}}} \geq \underline {{\mathbf {c}}} + \alpha (\underline {{\mathbf {c}}} - \underline {{\mathbf {c}}}) & (p \text {objective functions}) \\ A ^ {1} \underline {{\mathbf {x}}} \leq \underline {{\mathbf {b}}} ^ {1} + \alpha (\underline {{\mathbf {b}}} ^ {1} - \underline {{\mathbf {b}}} ^ {1}) & (m _ {1} \leq \text {constraints}) \\ A ^ {2} \underline {{\mathbf {x}}} \geq \underline {{\mathbf {b}}} ^ {2} + \alpha (\underline {{\mathbf {b}}} ^ {2} - \underline {{\mathbf {b}}} ^ {2}) & (m _ {2} \geq \text {constraints}) \\ A ^ {3} \underline {{\mathbf {x}}} \leq \underline {{\mathbf {b}}} ^ {3} + \alpha (\underline {{\mathbf {b}}} ^ {3} - \underline {{\mathbf {b}}} ^ {3}) & (m _ {3} \equiv \text {constraints}) \\ A ^ {3} \underline {{\mathbf {x}}} \geq \underline {{\mathbf {b}}} ^ {3} + \alpha (\underline {{\mathbf {b}}} ^ {3} - \underline {{\mathbf {b}}} ^ {3}) & (m _ {3} \equiv \text {constraints}) \\ \underline {{\mathbf {x}}} \in X \\ \sum w _ {k} = 1 \text {and} w _ {k} \geq 0 \text {for} k = 1, 2, \dots , p. \end{array}\tag{11}
$$

In the second interactive phase, for each different a a weighted sum of the objectives in region (10) is optimized

Illustrative example—nondominated extreme solutions with a = 0

By using the TRIMAP method, it is possible to perform a progressive and selective search of the fuzzy efficient solutions on the weight space, for the considered a. For each a, the TRIMAP method automatically generates $p$ efficient extreme points corresponding to the optimum of each objective function in the domain (10). Thereafter, the DM can interactively select the weights and calculate different fuzzy efficient solutions, thus, avoiding an exhaustive search which would require a cumbersome computational burden.

<table><tr><td>α=0 solutions</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $x_B$ </td><td> $L_\infty$ </td></tr><tr><td>A1</td><td>61.88</td><td>20</td><td>45</td><td> $x_1=12.17, x_2=9.68, x_3=7.54, x_4=0.61, s\_f_1=25.88, s\_c_3=3.14$ </td><td>30.52</td></tr><tr><td>A2</td><td>36</td><td>41.43</td><td>45</td><td> $x_1=6.51, x_2=6.19, x_4=10.28, s\_f_2=21.43, s\_c_1=15.96, s\_c_2=19.15$ </td><td>30.52</td></tr><tr><td>A3</td><td>36</td><td>20</td><td>75.52</td><td> $x_1=5.21, x_2=13.33, x_4=7.03, s\_f_3=30.52, s\_c_1=21.15, s\_c_2=0.97$ </td><td>25.88</td></tr><tr><td>A4</td><td>51.52</td><td>35.48</td><td>45</td><td> $x_1=11.79, x_2=8.17, x_4=7.97, s\_f_1=15.52, s\_f_2=15.48, s\_c_1=10.34$ </td><td>30.52</td></tr><tr><td>A5</td><td>60</td><td>27</td><td>45</td><td> $x_1=12, x_2=9, x_3=6, x_4=3, s\_f_1=24, s\_f_2=7$ </td><td>30.52</td></tr><tr><td>A6</td><td>58.25</td><td>20</td><td>53.75</td><td> $x_1=10.25, x_2=10.75, x_3=7.75, x_4=1.25, s\_f_1=22.25, s\_f_3=8.75$ </td><td>21.77</td></tr><tr><td>A7</td><td>37.07</td><td>20</td><td>74.93</td><td> $x_1=5.6, x_2=13.33, x_4=6.93, s\_f_1=1.07, s\_f_3=29.93, s\_c_1=20.67$ </td><td>24.81</td></tr></table>

Table 6  
Illustrative example—nondominated extreme solutions with a = 0.06639

<table><tr><td> $\alpha=0.06639$  solutions</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $x_B$ </td><td> $L_\infty$ </td></tr><tr><td>B1</td><td>59.40</td><td>21.99</td><td>46.99</td><td> $x_1=11.26, x_2=9.61, x_3=7.28, x_4=1.45, s\_f_1=21.41, s\_c_3=1.22$ </td><td>23.23</td></tr><tr><td>B2</td><td>37.99</td><td>38.30</td><td>46.99</td><td> $x_1=7.15, x_2=7.01, x_4=9.54, s\_f_2=16.31, s\_c_1=15.67, s\_c_2=13.84$ </td><td>23.23</td></tr><tr><td>B3</td><td>37.99</td><td>21.99</td><td>70.22</td><td> $x_1=6.15, x_2=12.45, x_3=0, x_4=7.07, s\_f_3=23.23, s\_c_1=19.63$ </td><td>21.41</td></tr><tr><td>B4</td><td>49.21</td><td>34.01</td><td>46.99</td><td> $x_1=10.96, x_2=8.44, x_4=7.87, s\_f_1=11.22, s\_f_2=12.02, s\_c_1=11.62$ </td><td>23.23</td></tr><tr><td>B5</td><td>58.73</td><td>24.48</td><td>46.99</td><td> $x_1=11.20, x_2=9.37, x_3=6.74, x_4=2.30, s\_f_1=20.74, s\_f_2=2.49$ </td><td>23.23</td></tr><tr><td>B6</td><td>58.11</td><td>21.99</td><td>50.11</td><td> $x_1=10.57, x_2=9.99, x_3=7.36, x_4=1.67, s\_f_1=20.12, s\_f_3=3.12$ </td><td>20.11</td></tr></table>

In each interaction of this second interactive phase, in addition to numerical information, two graphs are presented to the DM for two or three objective function problems. The first one is the decomposition of weight space filled with the indifference regions corresponding to each of the already known fuzzy efficient solutions. The second one displays the fuzzy efficient solutions already computed on the objective function space graph (or any of its projections).

An indifference region comprises the set of weights that leads to the same efficient extreme solution, and it is computed by optimizing a scalarizing function consisting of a weighted sum of the objective functions (such as in Eq. (11)). The DM can then be indifferent to all the combinations of weights within it because they lead to the same efficient solution. The area occupied by each indifference region is somehow a measure of the robustness of the corresponding efficient solution regarding the variation of the weights.

The decomposition of the weight space into indifference regions to perform a progressive and selective learning of the efficient solution set in MOLP has also been used in Clı´maco and Antunes [4,5].

Special attention should be paid to the comparative analysis of the two graphs obtained in each interaction: knowing the objective functions values for efficient extreme points corresponding to regions in the neighborhood of not yet filled weight space regions can be important to decide about the need to further proceed the search in those regions.

By changing the weights associated with the objectives and the a value, it can be visualized how the different solutions and the corresponding optimal basis change for the considered membership functions.

Since the feasible region considered for each a is different (with the increase of a the feasible region shrinks), distinct extreme solutions can be obtained. In practice, all points of the fuzzy efficient solutions set can be obtained if modifications are made on the membership functions.

Once a is successively greater (from 0 to $\alpha _ { \mathrm { m a x } } )$ and the corresponding region (10) smaller, for ${ \alpha } = { \alpha } _ { \mathrm { m a x } }$ the computed solution is unique.

This FMOLP approach is easy to handle computationally and is not too demanding with respect to information required from the DM in each interaction. The aim is to provide the DM a flexible decision aid tool by means of which changes can be easily incorporated in the model and their consequences in terms of efficient solutions are automatically visualized.

Table 7  
Illustrative example—nondominated extreme solutions with a = 0.103093

<table><tr><td>α=0.103093 solutions</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $x_B$ </td><td> $L_\infty$ </td></tr><tr><td>C1</td><td>58.03</td><td>23.09</td><td>48.09</td><td> $x_1=10.75, x_2=9.58, x_3=7.15, x_4=1.91, s_-f_1=18.94, s_-c_1=0$ </td><td>18.94</td></tr><tr><td>C2</td><td>39.09</td><td>36.58</td><td>48.09</td><td> $x_1=7.50, x_2=7.46, x_4=9.14, s_-f_2=13.49, s_-c_1=15.51, s_-c_2=10.91$ </td><td>18.94</td></tr><tr><td>C3</td><td>39.09</td><td>23.09</td><td>67.03</td><td> $x_1=6.60, x_2=11.89, x_3=0.22, x_4=6.99, s_-f_3=18.94, s_-c_1=18.48$ </td><td>18.94</td></tr><tr><td>C4</td><td>47.93</td><td>33.19</td><td>48.09</td><td> $x_1=10.51, x_2=8.59, x_4=7.82, s_-f_1=8.84, s_-f_2=10.10, s_-c_1=12.32$ </td><td>18.94</td></tr><tr><td>C5</td><td>39.09</td><td>23.72</td><td>66.40</td><td> $x_1=6.72, x_2=11.75, x_4=7.19, s_-f_2=.63, s_-f_3=18.31, s_-c_1=18.63$ </td><td>18.94</td></tr></table>

Table 8  
Illustrative example—nondominated extreme solutions with $\alpha { = } 0 . 2 3 9 4 8 9$

<table><tr><td>α=0.239489 solutions</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $x_B$ </td><td> $L_\infty$ </td></tr><tr><td>D1</td><td>46.16</td><td>27.18</td><td>52.18</td><td> $x_1=8.88, x_2=9.44, x_3=2.11, x_4=5.88, s\_f_1=2.98, s\_c_1=11.29$ </td><td>2.98</td></tr><tr><td>D2</td><td>43.18</td><td>30.16</td><td>52.18</td><td> $x_1=8.80, x_2=9.15, x_3=0, x_4=7.63, s\_f_2=2.98, s\_c_1=14.93$ </td><td>2.98</td></tr><tr><td>D3</td><td>43.18</td><td>27.18</td><td>55.16</td><td> $x_1=8.22, x_2=9.80, x_3=1.02, x_4=6.68, s\_f_3=2.98, s\_c_1=14.20$ </td><td>2.98</td></tr></table>

## 4. An illustrative example

To illustrate the interactive approach, let us consider the following FMOLP problem with three objective functions:

$$
\begin{array}{r l} \widetilde {\max} \underline {{\mathbf {f}}} (x) & = \widetilde {\max} \left( \begin{array}{c} f _ {1} \\ f _ {2} \\ f _ {3} \end{array} \right) \\ & = \widetilde {\max} \left( \begin{array}{c} 3 x _ {1} + x _ {2} + 2 x _ {3} + x _ {4} \\ x _ {1} - x _ {2} + 2 x _ {3} + 4 x _ {4} \\ - x _ {1} + 5 x _ {2} + x _ {3} + 2 x _ {4} \end{array} \right) \end{array}
$$

s.t.

$$
2 x _ {1} + x _ {2} + 4 x _ {3} + 3 x _ {4} \stackrel {\leq} {\sim} 6 0\tag{\( (c_{1}) \}
$$

$$
3 x _ {1} + 4 x _ {2} + x _ {3} + 2 x _ {4} \stackrel {\leq} {\sim} 6 0\tag{\( (c_{2}) \}
$$

$$
x _ {1} + 2 x _ {2} + 3 x _ {3} + 4 x _ {4} \stackrel {\leq} {\sim} 5 0\tag{\( (c_{3}) \}
$$

$$
x _ {1}, x _ {2}, x _ {3}, x _ {4} \geq 0
$$

By computing the efficient solutions which individually optimize each objective function, Table 2 is determined.

Let us suppose the DM establishes a numerical tolerance of 30 with respect to each of the optimal objective function values (diagonal values in Table 2), and admits a tolerance of 10%, 40% and 20% on the right-hand side of (c<sub>1</sub>), (c<sub>2</sub>) and (c<sub>3</sub>), respectively. The bounds used to define the membership functions associated with the fuzzy objectives and constraints are presented in Table 3.

By applying parametric programming to each objective in the region defined by nonnegativity constraints and

$$
\begin{array}{l} 3 x _ {1} + x _ {2} + 2 x _ {3} + x _ {4} \geq 3 6 + 3 0 \alpha \\ x _ {1} - x _ {2} + 2 x _ {3} + 4 x _ {4} \geq 2 0 + 3 0 \alpha \\ - x _ {1} + 5 x _ {2} + 1 x _ {3} + 2 x _ {4} \geq 4 5 + 3 0 \alpha \\ 2 x _ {1} + x _ {2} + 4 x _ {3} + 3 x _ {4} \leq 6 6 - 6 \alpha \\ 3 x _ {1} + 4 x _ {2} + x _ {3} + 2 x _ {4} \leq 8 4 - 2 4 \alpha \\ x _ {1} + 2 x _ {2} + 3 x _ {3} + 4 x _ {4} \leq 6 0 - 1 0 \alpha \\ \alpha \in [ 0, 1 ] \end{array}
$$

three fuzzy compromise solutions, which are analytically dependent on the parameter $\alpha ,$ are computed (Table 4a, b and c). $s \_ f _ { k } \left( k = 1 , 2 , 3 \right)$ is the slack of the kth goal, and $s \_ c _ { i } \ ( i { = } 1 , 2 , 3 )$ is the slack of the ith constraint.

These tables contain the a intervals that correspond to the same optimal basis, the fuzzy compromise solution values (analytically dependent on a), the objective functions and constraints values obtained at this solution (analytically dependent on a), the objective functions and constraints values obtained at the bounds of the a intervals.

Illustrative example—nondominated extreme solutions with a = 0.264957

<table><tr><td> $\alpha=0.264957$  solutions</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $x_B$ </td><td> $L_\infty$ </td></tr><tr><td>E1</td><td>43.95</td><td>27.95</td><td>52.95</td><td> $x_1=8.53, x_2=9.41, x_3=1.17, x_4=6.62, s\_f_1=0, s\_c_1=13.40$ </td><td>0</td></tr></table>

![](/api/attachments/57G3C8WG/fulltext/images/814888d7c47152f8e949a717c922e22497bc61bdb5949e843f47c8ba845bbb98.jpg)  
Fig. 7. Illustrative example—nondominated extreme solutions with a = 0 (Ai solutions).

If the DM is not yet satisfied with the calculated fuzzy compromise solutions, he/she can change the membership functions and compute other fuzzy compromise solutions or proceed the search in regions of the weight space not yet investigated by using the information given by the display of indifference regions in the weight space as visual feedback, for every a bounds previously computed.

Let us suppose the DM wants to compute additional solutions, in order to have a broader view of the efficient region, for the calculated a bounds. Tables 5 – 9 and Figs. 7 – 11 show the characteristics of the various efficient extreme solutions calculated for different values of a (each indifference region in the weight space is associated with an efficient extreme solution obtained by optimizing a weighted-sum scalarizing function). $L _ { \infty }$ is the Tchebycheff (minmax) distance to the ideal solution for each efficient extreme solution. The so-called ideal solution is the one which would optimize all the objective functions simultaneously (which is not feasible whenever the objective functions are in conflict). The figures are copies of the computer screens presented to the user and the $f _ { 1 } - f _ { 2 }$ objective function projection labels corresponds to solution identification/f value.

![](/api/attachments/57G3C8WG/fulltext/images/0ee3727ca7d2fdf9e7f334efaa5044cd4dfdb08bb1482df28966d35a9fda5f74.jpg)  
Fig. 8. Illustrative example—nondominated extreme solutions with $\alpha { = } 0 . 0 6 6 3 9$ (Bi solutions).

![](/api/attachments/57G3C8WG/fulltext/images/f7841fe0a1f63d7911e1509454ce3a359e68da3ac42b35fad69c52a9ff55f281.jpg)  
Fig. 9. Illustrative example—nondominated extreme solutions with a = 0.103093 (Ci solutions).

By comparing the weight spaces on Figs. 7 and 8, it can be concluded that the indifference regions corresponding to solutions A3 and A7 are going to join and originate solution B3 indifference region. That is, the set of weights with which solutions A3 and A7 are obtained for a = 0 are the same that lead to solution B3 with $\alpha { = } 0 . 0 6 6 3 9$ , a more stable solution as far as weight changes is concerned.

By analyzing Figs. 8 and 9, it can be observed that the (degenerate) B3 solution indifference region is split into the indifference regions corresponding to solutions C3 and C5. Solutions B1, B5 and B6 indifference regions are going to join and originate the indifference region corresponding to the (degenerate) solution C1, a more stable solution regarding to weight changes.

From visual inspection of the other weight spaces (Figs. 9–11), it can be concluded that solutions C2, C4 and C5 indifference regions are going to join and originate (degenerate) solution D2 indifference region. This region and the solutions D1 and D3 indifference regions will also join and originate solution E1 indifference region, which is the only efficient solution for a = 0.264957.

For these membership functions, all the calculated solutions are outside the original crisp feasible region.

![](/api/attachments/57G3C8WG/fulltext/images/7c19cb14e9bdce0ed86147243928881af5350dece361e01eaed9d39cb964f5ca.jpg)  
Fig. 10. Illustrative example—nondominated extreme solutions with a = 0.239489 (Di solutions).

![](/api/attachments/57G3C8WG/fulltext/images/749b9419326708dbdccbe8cb93bbce9a981bcb440321cf43630ed90fa57bff43.jpg)  
Fig. 11. Illustrative example—nondominated extreme solutions with a = 0.264957 (Ei solution).

Besides, as a grows, the solutions become nearer to the initial crisp constraints.

Let us suppose that at this moment, the DM has gathered sufficient information about the fuzzy efficient solution set, in a way that a better informed final decision can be made or eventually he/she concludes that it is necessary to review the model.

In this simple illustrative example, all the weight spaces have been filled completely with indifference regions. However, it must be emphasized that this is not generally the goal in actual decision situations. The main concern being to provide the DM a flexible decision aid tool by means of which it is possible to gather, in a progressive and selective manner, knowledge about the efficient solution set in order to make a final decision.

## 5. Conclusions

Decisions to be made in complex contexts, characterized by the presence of multiple evaluation aspects, are normally affected by uncertainty, which is essentially due to the insufficient and/or imprecise nature of input data as well as the subjective and evolutive preferences of the decision maker. An interactive approach, based on the search of the weight space, to deal with FMOLP problems has been proposed and implemented as a DSS. Linear fuzzy objective functions and fuzzy constraints have been considered.

The analysis is based on the weight space which enables to show graphical information interactively to the DM in a way that promotes to gain new insights into the problem and the trade-offs to be made in order to select a satisfactory compromise solution. Special attention has been paid to the computational simplicity and graphical interactivity, in order to visualize dynamically the behavior of the efficient solutions according to changes in the initial model coefficients, by displaying the indifference regions on the weight space.

The comparative study of distinct weight space decomposition, which changes according to the range of the parameter a, shows the evolution of the indifference regions corresponding to the calculated efficient solutions, in a way that enables to understand the shape of the fuzzy efficient feasible region and the nature of the trade-offs to be made in selecting a final satisfactory compromise solution.

The interactive computer environment contributes to stimulate the DM to take a more active role in the decision process by exploring the problem and his/her convictions, criticizing the obtained results and carefully considering distinct situations that can arise (regarding objective functions values, used resources, intervals of values of the objective functions’ and constraints’ satisfaction degree, etc.). The membership functions can also be interactively changed, thus, allowing to further study the fuzzy efficient solution set.

Despite the fact that uncertainty elements in the coefficients of the objective functions have not been incorporated, this seems very easy to integrate in the proposed approach both methodologically and computationally. In this situation the shape and the size of the indifference regions on the weight spaces would change dynamically as the value of the objective functions and constraints satisfaction degree varies. Research is currently underway to extend this DSS based on the weight space to incorporate uncertainty elements in the coefficients of the objective functions.

[1] R. Bellman, L.A. Zadeh, Decision making in a fuzzy environment, Management Science 17 (4) (1970) 141 – 164.

[2] C. Carlsson, P. Korhonen, A parametric approach to fuzzy linear programming, Fuzzy Sets and Systems 20 (1986) 17 – 30.

## References

[3] S. Chanas, The use of parametric programming in fuzzy linear programming, Fuzzy Sets and Systems 11 (1983) 243– 251.

[4] J. Clı´maco, C.H. Antunes, TRIMAP—an interactive tricriteria linear programming package, Foundations of Control Engineering 12 (1987) 101– 119.

[5] J. Clı´maco, C.H. Antunes, Implementation of an user friendly software package—a guided tour of TRIMAP, Mathematical and Computer Modelling 12 (1989) 1299 – 1309.

[6] E.S. Lee, R.J. Li, Fuzzy multiple objective programming and compromise programming with Pareto optimum, Fuzzy Sets and Systems 53 (1993) 275– 288.

[7] C.V. Negoita, The current interest in fuzzy optimization, Fuzzy Sets and Systems 6 (1981) 261– 269.

[8] B. Werners, An interactive fuzzy programming system, Fuzzy Sets and Systems 23 (1987) 131 – 147.

[9] B. Werners, Interactive multiple objective programming subject to flexible constraints, European Journal of Operational Research 31 (1987) 342– 349.

[10] G. Wiedey, H.J. Zimmermann, Media selection and fuzzy lin-

ear programming, Journal of the Operational Research Society 29 (1978) 1071– 1084.

[11] H.J. Zimmermann, Fuzzy programming and linear programming with several objective functions, Fuzzy Sets and Systems 1 (1978) 45–55.

[14] H.J. Zimmermann, Fuzzy set theory—and its applications, International Series in Management Science/Operations Research, Kluwer Academic Publishing, Boston, 1992.

[12] H.J. Zimmermann, Fuzzy mathematical programming, Computers and Operations Research 10 (1983) 291– 298.

[13] H.J. Zimmermann, Fuzzy set, decision making, and expert systems, International Series in Management Science/Operations Research, Kluwer Academic Publishing, Boston, 1987.

![](/api/attachments/57G3C8WG/fulltext/images/357f2a7d24e08d184fa9b2d0c800f3f7820a48a05faf3a0592e7d8bba8f2db94.jpg)

Ana Rosa Borges received her Computer Engineering degree in 1989 and her Master in Systems and Information Technology in 1995 from the Coimbra University. Currently, she is preparing her PhD degree. She is a lecturer at the Department of Computer and Systems Engineering, ISEC-Coimbra Polytechnic Institute. Her current research areas include multiple objective programming, decision support systems and fuzzy sets.

![](/api/attachments/57G3C8WG/fulltext/images/c648c8cb6c99c58c65349ec60377976dd90f87c349d3fa95be86061c190005e3.jpg)

Carlos Henggeler Antunes received his PhD degree in Electrical Engineering (Optimisation and Systems Theory) from the University of Coimbra in 1992. He is an associate professor at the Department of Electrical Engineering and Computers, University of Coimbra. His research areas include multiple objective programming, decision support systems, energy planning and telecommunication network planning.
