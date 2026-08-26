---
otero_id: 4032
otero_key: "G7QH9R8Y"
title: "Solving linear design problems using a linear-fractional value function"
authors: "J. Randall Brown; Aviad A. Israeli"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.037"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Solving linear design problems using a linear-fractional value function

J. Randall Brown <sup>a,</sup>⁎, Aviad A. Israeli <sup>a,b</sup>

<sup>a</sup> Department of Management and Information Systems, College of Business Administration, Kent State University, Kent, OH 44242, USA

<sup>b</sup> The Department of Hotel and Tourism Management, The Guilford Glazer Faculty of Business and Management, Ben-Gurion University of the Negev, Beer-Sheva 84105, Israel

## a r t i c l e i n f o

Article history: Received 26 August 2010 Received in revised form 17 December 2012 Accepted 30 December 2012 Available online 17 January 2013

Keywords: Decision analysis Multiple criteria analysis Linear-fractional preference structure Piecewise linear-fractional model

## a b s t r a c t

Previous papers developed a method to easily elicit a decision maker's (DM) preferences and account for changes in the DM's preference structure. Those preferences are modeled by piecewise linear indifference curves with varying slopes producing a piecewise linear-fractional value function. Compared with traditional optimization problems which traditionally use cost minimization or revenue maximization, this model is DM-speci<sup>fi</sup>c, it generates a knowledge set (KS) and allows the DM to <sup>fi</sup>nd an optimal solution based on his/her expertise and preferences. When combined with real world constraints, maximizing the DM's preferences generates a decision support system (DSS) for solving speci<sup>fi</sup>c organizational problems. This paper develops an ef<sup>fi</sup>cient algorithm to solve a mathematical programming problem with a linear fractional objective function that models changing DM preferences and linear constraints. A DSS is developed and its algorithm is illustrated by constructing a speci<sup>fi</sup>c example of the DSS for scheduling a police force when the objective is to maximize the police chief's expertise and preferences regarding law enforcement.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In organizational decision problems <sup>fi</sup>rms have to assess their core objectives and the business processes needed to ful<sup>fi</sup>ll them [11]. When a decision maker (DM) is trying to solve a traditional problem such as pro<sup>fi</sup>t maximization or cost minimization in products or services mix setting, the resulting model is often a linear decision problem and the solution is based on the weight of each attribute in the objective function which is determined by pro<sup>fi</sup>t or cost parameters. Since most of these parameters are generally deterministic, the objective function is linear with constant rates of substitution. The solution is achieved by maximizing a linear pro<sup>fi</sup>t function or minimizing a linear cost function while taking into account the relevant constraints. In this context, DM individual preferences, or other organizational preferences, are not necessarily included in the objective function although it may be bene<sup>fi</sup>cial to include them in the formulations of the problem. Moreover, there are even problems in which the objective function is not clearly de<sup>fi</sup>ned because the problem is not strictly a problem of pro<sup>fi</sup>t maximization or cost minimization. Those issues are highlighted by Bhatt and Zaveri [2]. They argue that decision support models should assist organizations in coping with speci<sup>fi</sup>c challenges using their own speci<sup>fi</sup>c knowledge and competencies. The purpose of this paper is to offer a model for solving problems when the objective function is based on the DM's knowledge and preferences when these preferences may change in the domain of the problem.

Two previous papers [3,4] introduced an approach for decision making under certainty when the attribute weights are local (rates of substitution vary over the attribute space) and the indifference curves are linear. This approach is named the linear fractional (LF) model and it consists of a preference elicitation technique called the constrained choice table (CCT), the construction of a piecewise linear-fractional value function based on the decision maker's (DM) preferences as shown by his/her data in the CCT, the correction of any inconsistencies if they exist in the DM's preferences, and then assigning a value to each competing alternative by using the piecewise LF value function. This approach provides a decision support system (DSS) in which the DM can provide his/her preferences as the objective. This procedure bypasses the traditional de<sup>fi</sup>nitions of problems as pro<sup>fi</sup>t maximization or cost minimization. It allows the DM to translate his/her knowledge set (KS) and expertise into a set of preferences which become the objective of the DSS and the organizational setting will impose a set of constraints which will be considered when the problem is solved in order to maximize the DM's preferences.

Greasley [8] shows the importance of focusing on DM preferences by presenting a case report of a process improvement within a human resource division at a United Kingdom police force. The case report highlights the importance of constructing a DSS which focuses on the DM preferences to link an organizational reengineering effort to strategic priorities derived from a range of stakeholder interests, rather than being budget driven through a range of <sup>fi</sup>nancial indicators. Greasley demonstrates how a DSS can be developed in a manner which business processes are evaluated based on current performance and overall importance with respect to strategic objectives.

This paper formulates design problems that use the DM's preferences which are modeled as a piecewise LF value function. Section 2 demonstrates how the LF value function is different than the traditional pro<sup>fi</sup>t maximization or cost minimization function (with the solution algorithm in the Section Appendix A). Section 3 provides an example for using such a value function as the objective function in a multiattribute decision problem with an in<sup>fi</sup>nite number of alternatives. This formulation, which is based on the DM's speci<sup>fi</sup>c knowledge and preferences, generates a model which is speci<sup>fi</sup>c to the DM and the organizational problem under consideration. As mentioned before, this formulation is useful in cases where the objective cannot be de<sup>fi</sup>ned as a generic cost minimization or income maximization problem. The example in Section 3 focuses on the objective of a police chief to provide safety and security to the community. In this case, applying a generic model of cost minimization may indeed save money, but it may not provide a good solution for public safety. Even maximization of labor hours may not incorporate all the needed considerations for providing safety and security. Section 3 provides a speci<sup>fi</sup>c DSS which is based on a model that takes into consideration the police chief's expertise, knowledge and preferences in the objective function. This DSS generates a solution that contributes to public safety. Cost control and other issues will be introduced to the model via the constraint set. This model can be the foundation of a scheduling DSS which takes into account the speci<sup>fi</sup>c organizational setting of the problem. Section 4 concludes with summary and discussion.

## 2. The linear-fractional objective function

Two previous papers [3,4] developed an approach to measure a DM's preference structure with linear indifference curves where the DM's preferences and thus the rate of substitution varies over the attribute space. This approach divided the attribute space into J+1 regions where the slope of the indifference curve in each region can vary. Because the rate of substitution can vary within a region, the form of the value function in each region is linear-fractional (a linear function divided by a linear function). If the slope of the indifference curves within a region does not vary, then the form of the preference function reduces to the traditional additive linear function. The general form of a linear-fractional value function with $J + 1$ regions (piecewise segments) is shown in Eq. (1) which emphasizes the fact that regions 1 and $J + 1$ have linear value functions and regions 2 through J have linear-fractional value functions. Examples of piecewise linear-fractional value functions are plotted in [3,4] and the value function for the example in Section 3.1 is plotted in Fig. 1 with one of the hinges labeled.

$$
v (x) \left\{ \begin{array}{l l} v _ {1} (x) = c _ {1, 1} x _ {1} + c _ {2, 1} x _ {2} + \dots + c _ {n, 1} x _ {n} + \sigma_ {1} & i f V _ {0} \leq v (x) \leq V _ {1} \\ v _ {2} (x) = \frac {c _ {1 , 2} x _ {1} + c _ {2 , 2} x _ {2} + \cdots + c _ {n , 2} x _ {n} + \alpha_ {2}}{d _ {1 , 2} x _ {1} + d _ {2 , 2} x _ {2} + \cdots + d _ {n , 2} x _ {n} + \beta_ {2}} & i f V _ {1} \leq v (x) \leq V _ {2} \\ \vdots \quad \vdots \quad \vdots \quad \vdots \quad \vdots \quad \vdots \quad \vdots & \vdots \\ v _ {J} (x) = \frac {c _ {1 , J} x _ {1} + c _ {2 , J} x _ {2} + \cdots + c _ {n , J} x _ {n} + \alpha_ {J}}{d _ {1 , J} x _ {1} + d _ {2 , J} x _ {2} \cdots + d _ {n , J} x _ {n} + \beta_ {J}} & i f V _ {J - 1} \leq v (x) \leq V _ {J} \\ v _ {J + 1} (x) = c _ {1, J + 1} x _ {1} + c _ {2, J + 1} x _ {2} + \dots c _ {n, J + 1} x _ {n} + \sigma_ {1} & i f v (x) \geq V _ {J} \end{array} \right.\tag{1}
$$

For an application, the speci<sup>fi</sup>c form of the linear-fractional value function is determined by the DM completing a CCT. Based on the CCT information, the corresponding value function can be constructed. Using the formulae in Brown and Israeli [3] for the two attribute case ([4] contains the formulae for the n attribute case), the axis intercepts for each region j are $I _ { 1 , j } { = } [ ( x _ { 1 , j } ^ { b } ) ^ { 2 } + ( x _ { 2 , j } ^ { b } ) ^ { 2 } ] / x _ { 1 , j } ^ { b }$ and $I _ { 2 , j } + [ ( x _ { 1 , j } ^ { b } ) ^ { \hat { 2 } } +$ $( x _ { 2 , j } ^ { b } ) ^ { 2 } ] / x _ { 2 , j } ^ { b }$ where superscript b means that $x _ { 1 , j } ^ { b }$ and $x _ { 2 , j } ^ { b }$ are the values in the CCT given by the DM (see Table 1). The hinge coordinates for each region j are $h _ { 1 , j } { = } I _ { 1 , j - 1 } I _ { 1 , j } ( I _ { 2 , j } - I _ { 2 , j - 1 } ) / ( I _ { 1 , j - 1 } I _ { 2 , j } - I _ { 2 , j - 1 } I _ { 1 , j } )$ and $h _ { 2 , j } = I _ { 2 , j - 1 } I _ { 2 , j } ( I _ { 1 , j } - I _ { 1 , j - 1 } ) / ( I _ { 2 , j - 1 } \bar { I } _ { 1 , j } - \bar { I } _ { 1 , j - 1 } I _ { 2 , j } )$ . For each region j, the standardized metric is $N _ { j } { = } x _ { j } ^ { M } V _ { j - 1 } { - } x _ { j - 1 } ^ { M } V _ { j }$ and the intermediate value is $N _ { j } { = } x _ { j } ^ { M } V _ { j - 1 } { - } x _ { j - 1 } ^ { M } V _ { j } .$ Then for region $j ,$ the linear-fractional value functions in Eq. (1) can be constructed by calculating $c _ { 1 , j } = - N _ { j } +$ $h _ { 2 , j } \vee _ { j - 1 } - h _ { 2 , j } \vee _ { j } , c _ { 2 , j } = N _ { j } + h _ { 1 , j } \vee _ { j } - h _ { 1 , j } \vee _ { j - 1 } , \ \propto _ { j } = N _ { j } ( \ln _ { 1 , j } - h _ { 2 , j } ) , \ d _ { 1 , j } = - x _ { j } ^ { \tilde { M } } +$ ${ x _ { j - 1 } ^ { \tilde { M } } } , { d _ { 2 , j } } = \bar { x } _ { j } ^ { \tilde { M } } - \bar { x } _ { j - 1 } ^ { M } ,$ , and $\beta _ { j } = ( x _ { j } ^ { M } - x _ { j - 1 } ^ { M } ) ( h _ { 1 , j } - h _ { 2 , j } ) .$ . The value v (x) for any alternative x in region j goes from $V _ { J - 1 }$ to $V _ { J }$ so that $V _ { J - 1 } { \leq } { \nu } _ { j } ( x ) \mathop { \leq } V _ { J } .$

Using the linear-fractional preference function as an objective function to maximize the DM's preferences combined with linear constraints produces the linear-fractional programming problem shown in Eq. (2).

![](/api/attachments/G7QH9R8Y/fulltext/images/512a20d6e1ce9e2be37cadf0bcd49e86c53d919b04af167a29f4bb184a8ff5f2.jpg)  
Fig. 1. Attribute space for the police patrol example.

Constrained choice table (CCT) and attributes amount table for the police patrol example.

<table><tr><td rowspan="2">Attribute</td><td rowspan="2">Standardized quantity</td><td colspan="6">Percentages for constrained choice j</td></tr><tr><td>j=0</td><td>j=1</td><td>j=2</td><td>j=3</td><td>j=4</td><td>j=5</td></tr><tr><td>I</td><td>di</td><td>pi,0b</td><td>pi,1b</td><td>pi,2b</td><td>pi,3b</td><td>pi,4b</td><td>pi,5b</td></tr><tr><td>1. Foot patrol hours</td><td>1600</td><td>0</td><td>25</td><td>60</td><td>70</td><td>100</td><td>130</td></tr><tr><td>2. Car patrol hours</td><td>1200</td><td>0</td><td>25</td><td>40</td><td>80</td><td>100</td><td>120</td></tr><tr><td></td><td>Percent totals Tb:</td><td>0</td><td>50</td><td>100</td><td>150</td><td>200</td><td>250</td></tr><tr><td colspan="2">Attribute amounts table</td><td colspan="6">Attribute amounts for constrained choice j</td></tr><tr><td>Attribute</td><td rowspan="2">Formula</td><td>j=0</td><td>j=1</td><td>j=2</td><td>j=3</td><td>j=4</td><td>j=5</td></tr><tr><td>I</td><td>xi,0b</td><td>xi,1b</td><td>xi,2b</td><td>xi,3b</td><td>xi,4b</td><td>xi,5b</td></tr><tr><td>1. Foot patrol hours</td><td>xb1,j=p1,d1/100</td><td>0</td><td>400</td><td>960</td><td>1120</td><td>1600</td><td>2080</td></tr><tr><td>2. Car patrol hours</td><td>xb2,j=p2,d2/100</td><td>0</td><td>300</td><td>480</td><td>960</td><td>1200</td><td>1440</td></tr><tr><td></td><td>Value Vj:</td><td>0</td><td>25</td><td>50</td><td>75</td><td>100</td><td>125</td></tr></table>

$$
\begin{array}{c} \max v (x) \\ s. t. \\ A x = b \\ x \geq 0 \end{array}\tag{2}
$$

For any of the $j = 1 , 2 , \cdots J + 1$ regions in the piecewise linear fractional objective function (1), a corresponding linear-fractional programming problem can be created from problem (2) by simply replacing the objective function v(x) with $. \nu _ { j } ( x ) ,$ , the objective function for region j. Let $\dot { \boldsymbol { \nu } } _ { j } ^ { * }$ be the optimal value of the objective function for region $j ^ { \prime } s$ corresponding problem. The basic strategy to solve linear-fractional programming problem (2) with the piecewise objective function in Eq. (1) is to construct the corresponding problem for every region $j = 1 , \bar { 2 } , \cdots J + 1 . \operatorname { L e t } j ^ { * }$ be the region that contains the optimal feasible solution to problem (2). For every region $^ { \cdot j , }$ the objective function to the corresponding problem is increasing so that if $\begin{array} { r } { \check { v } _ { j } ^ { * } > V _ { j } , } \end{array}$ then the optimal solution to problem (2) lies in a region greater than $j , j ^ { * } > j$ . Similarly, $\mathrm { i f } \ V _ { j } ^ { * } > V _ { j } ,$ then the optimal solution to problem (2) lies in a region less than $j , j ^ { \ast } < j$ Finally, if $V _ { j - 1 } { \leq } { \stackrel { * } { \upsilon _ { j } } } { \leq } V _ { j } ,$ then the optimal solution to problem (2) lies in region $j , j ^ { * } { = } j$

## 2.1. Linear value function region

The function in (1) demonstrates that regions 1 and $J + 1$ do not have a linear-fractional value function but a strictly linear value function so the corresponding problems for regions 1 and J+1 are linear programming problems. For region $J + 1 ^ { \prime } s$ corresponding problem, if no feasible solution exists or an unbounded solution exists (a feasible solution with an in<sup>fi</sup>nite value of the objective function), then respectively no feasible solution or an unbounded solution exists to the original problem (2). For any region j with a linear value function $( d _ { i , j } = 0$ for all $i = 1 , 2 , \cdots , n )$ , then $\beta _ { j } \neq 0$ and the corresponding linear programming problem (3) can be solved to <sup>fi</sup>nd the optimal solution for region j.

$$
\begin{array}{l} v _ {j} ^ {*} = \max v j (x) = \max \left\{\frac {c _ {1 , j}}{\beta_ {j}} x _ {1} + \frac {c _ {2 , j}}{\beta_ {j}} x _ {2} + \dots + \frac {c _ {n , j}}{\beta_ {j}} x _ {n} + \frac {\alpha_ {j}}{\beta_ {j}} \right\} \\ s. t. \\ A x = b \\ x \geq 0 \end{array}\tag{3}
$$

## 2.2. Linear-fractional value function region

As explained in a previous paper [3] for a linear-fractional value function computed from a CCT, the hinge point for column j in the

CCT is the intersection of the linear indifference curves de<sup>fi</sup>ned by CCT columns j and j-1 which form the boundaries of region j. All the linear value functions in region j will pivot (go through) the hinge point. The linear-fractional value function for region j is represented by $\nu _ { j } ( \boldsymbol { x } )$ . The denominator of $\nu _ { j } ( \boldsymbol { x } )$ can only equal zero when the hinge is in the non-negative orthant. The points in the hinge are all the points that satisfy the two equations $\nu _ { j } ( x ) = V _ { j - 1 }$ and $\nu _ { j } ( x ) = V _ { j } .$ These two equations can be converted to the linear equations shown in (4) below.

$$
\begin{array}{r l} & \left(c _ {1, j} - d _ {1, j} V _ {j - 1}\right) x _ {1} + \left(c _ {2, j} - d _ {2, j} V _ {j - 1}\right) x _ {2} + \dots + \left(c _ {n, j} - d _ {n, j} V _ {j - 1}\right) x _ {n} \\ & = \beta_ {j} V _ {j - 1} - \alpha_ {j} \left(c _ {1, j} - d _ {1, j} V _ {j}\right) x _ {1} + \left(c _ {2, j} - d _ {2, j} V _ {j}\right) x _ {2} + \dots + \left(c _ {n, j} - d _ {n, j} V _ {j}\right) x _ {n} \\ & = \beta_ {j} V _ {j} - \alpha_ {j} \end{array} \tag {4}
$$

Linear program (5) can be solved to see if a point on the hinge for region j is feasible.

$$
\begin{array}{l} \max x _ {i} \\ \text { s.t. } \\ A x = b \\ \left(c _ {i, j} - d _ {1, j} V _ {j - 1}\right) x _ {1} + \left(c _ {2, j} - d _ {2, j} V _ {j - 1}\right) x _ {2} + \dots + \left(c _ {n, j} - d _ {n, j} V _ {j - 1}\right) x _ {n} \\ = \beta_ {j} V _ {j - 1} - \alpha_ {j} \quad \left(c _ {i, j} - d _ {1, j} V _ {j}\right) x _ {1} + \left(c _ {2, j} - d _ {2, j} V _ {j}\right) x _ {2} + \dots \\ + \left(c _ {n, j} - d _ {n, j} V _ {j}\right) x _ {n} = \beta_ {j} V _ {j} - \alpha_ {j} \end{array}\tag{5}
$$

If linear program (5) has a feasible solution, then it is the optimal solution for region j with a value of $V _ { j } .$

If linear program (5) does not have a feasible solution, then the denominator of $\nu _ { j } ( \boldsymbol { x } )$ is not zero for all feasible points in region j. Thus, the linear-fractional programming problem (6) can be solved for the optimal feasible solution in region j.

$$
\begin{array}{l} v _ {j} ^ {*} = \max v _ {j} (x) = \max \left\{\frac {c _ {1 , j} x _ {1} + c _ {2 , j} x _ {2} + \cdots + c _ {n , j} x _ {n} + \alpha_ {j}}{d _ {1 , j} x _ {1} + d _ {2 , j} x _ {2} + \cdots + d _ {n , j} x _ {n} + \beta_ {j}} \right\} \\ s. t. \\ A x = b \\ x \geq 0 \end{array}\tag{6}
$$

The method of Charnes and Cooper [5] can be used to solve linear-fractional program (6) by creating two linear programs. First, de<sup>fi</sup>ne new a variable t and n new variables y. Then create the two linear programs, linear program (7)

$$
\begin{array}{l} \max \left\{c _ {1, j} y _ {1} + c _ {2, j} y _ {2} + \dots + c _ {n, j} y _ {n} + \infty_ {j} t \right\} \\ s. t. \\ A y - b t = 0 \\ d _ {1, j} y _ {1} + d _ {2, j} y _ {2} + \dots + d _ {n, j} y _ {n} + \beta_ {j} t = 1 \\ y, t \geq 0 \end{array}\tag{7}
$$

and linear program (8).

$$
\begin{array}{c} \max \left\{- c _ {1, j} y _ {1} - c _ {2, j} y _ {2} - \dots - c _ {n, j} y _ {n} - \infty_ {j} t \right\} \\ s. t. \\ A y - b t = 0 \\ - d _ {1, j} y _ {1} - d _ {2, j} y _ {2} - \dots - d _ {n, j} y _ {n} - \beta_ {j} t = 1 \\ y, t \geq 0 \end{array}\tag{8}
$$

At least one of the two linear programs (7) and (8) will not have a feasible solution. If both have no feasible solution, then linearfractional problem (6) has no feasible solution. If one of the two linear programs (7) and (8) has an optimal feasible solution $y ^ { * }$ and $t ^ { * } ,$ , then $\bar { \mathrm { t } } ^ { * } { > } 0$ and an optimal feasible solution to linear-fractional problem (6) is $x ^ { * } { = } \mathbf { y } ^ { * } / t .$ . The detailed algorithm for solving a problem is provided in the Section Appendix A. The next section applies the algorithm to solve a human resource allocation problem in the context of law enforcement.

## 3. The two attribute police patrol example

This section presents an example of using the LF model as a DSS for solving an organizational problem. Bhatt and Zaveri [2] provide an overview of DSS in organizational learning. They propose that the main motivation for using a DSS is to allow organizations to cope with environmental complexities by employing their knowledge and skills. Their review explains the context of the proposed LF model and its DSS. Bhatt and Zaveri [2] note that two key subsystems of a DSS are its Knowledge System (KS) and it Problem Processing System (PPS). The LF model presented in the paper uses the DM knowledge and preferences as the KS for the system. The model itself (presented in the Section 2) is the systems' PPS.

Workforce planning is dealing with strategic questions relating to the optimal size or mix of a workforce [7]. Optimal staff scheduling can provide signi<sup>fi</sup>cant bene<sup>fi</sup>ts, but requires a carefully implemented DSS to meet customer demands in a cost effective manner while satisfying different constraints and requirements such as shift equity and support of customers' needs and demands. The following example focuses on constructing a DSS for a scheduling problem in the area of law enforcement.

In this law enforcement example, the DM is a police chief who evaluates two attributes of the police force which he/she considers to be perfect substitutes and can be represented by linear indifference curves. The two attributes are based on the fact that the police patrol force can be split into two main subforces [12], one primarily proactive to prevent crimes from being committed [6] and the other primarily reactive to react to already committed crimes [9]. A foot patrol is considered to be a primarily proactive allocation of the police force because it takes longer to cover a given area than a car patrol but it provides more intensive coverage and projects a law enforcement presence to the community. Car patrol, on the other hand, can be viewed more as a reactive allocation of the police force because it can be dispatched quickly to the scene when a crime is committed and therefore, it can be viewed as more reactive compared with foot patrol.

While foot patrol and car patrol can be viewed as substitutes, the rate of substitution between foot patrol and car patrol is not constant or global. The decision to allocate the available force between foot patrol and car patrol is determined by three main issues: citizens' safety, cost of operations and of<sup>fi</sup>cer morale [14]. A sizable proportion of resources will provide a certain tradeoff between foot and car patrols. However, with limited resources the DM may change his preferences and focus on proactive or reactive enforcement according to his management style philosophy, his knowledge and his preferences. Therefore, in different states of nature, different availability of resources will result in different allocations of resources and will cause the linear indifference curves to change slope.

This dynamic setting must be formulated into a KS that can determine the necessary allocation of foot patrol and car patrol according to different environmental and organizational settings. As mentioned before, without a speci<sup>fi</sup>c KS, some traditional models may be used to solve the problem (such as cost minimization or coverage maximization). However, if the DSS is aimed at allowing the law enforcement organization to cope with environmental complexities by employing speci<sup>fi</sup>c knowledge and skills, a KS must be established. We assume that the police chief is the DM which has the ultimate knowledge about the problem and this knowledge is manifested through his preferences with respect to the different proportions of allocating law enforcement resources (foot patrol and car patrol). Therefore, this knowledge serves as the KS for the DSS. The LF model is then used as the PPS in which the DM can insert his preferences and constraints and receive an optimal police force allocation [14]. The proposed application in this paper includes preferences (and changing preferences) as the focus of police force allocation KS. Although scheduling in general, and speci<sup>fi</sup>cally in police force problems, usually involve more than two attributes, this example will be limited to two attributes for illustrative purposes.

## 3.1. Police force scheduling problem

The problem analyzed in this section involves an expanded version of the police patrol example used in Brown and Israeli [3]. A city's police chief (DM) is formulating his KS by deciding how to schedule his policemen to proactive patrols during the week where the policemen can be assigned either to foot patrols or car patrols. Let x represent the number of foot patrol hours (one policeman hour for every foot patrol hour) and let $x _ { 2 }$ represent the number of car patrol hours (two policeman hours and one car hour for every car patrol hour). The DM wants to determine how many of the available police of<sup>fi</sup>cer hours to assign to foot patrols and how many to car patrols. A standardized point is determined by asking the DM, “How many foot patrol hours and how many car patrol hours would it take to give you a feasibly good level of satisfaction?” The standardized point should be at the upper end of the DM's region of interest. The reasoning behind the standardized point closely resembles the reasoning behind the “ideal point” de<sup>fi</sup>ned by Zeleny [17]. The term standardized point is also closely related to the term industry standard (or, in this case, law enforcement standards) which is often used in a speci<sup>fi</sup>c environment to describe the “best” feasible alternative. Experience has shown that DMs have no dif<sup>fi</sup>culty in identifying a standardized point in just a few minutes even with a large number of attributes [1,13].

First, the DM wants to maximize his/her value as measured by a linear-fractional value function developed in [3,4]. For a particular week, suppose the DM speci<sup>fi</sup>es the desirable point (1600,1200) and completes the constrained choice table (CCT) which gives the DM's preferences for points in the attribute space. The <sup>fi</sup>rst part of Table 1 contains the DM's responses for the police patrol example. The second part of Table 1 contains the attribute amounts corresponding to the percentages that the DM provided in the <sup>fi</sup>rst part. Then the procedures in [3] are used to correct any possible inconsistencies in the DM's preferences which produce the results in Tables 2, 3, and 4 with the linear-fractional indifference curves plotted in Fig. 1. This is essentially the system's KS. Table 2 includes the coordinates of the access intercepts and hinges which are used to draw the linear lines de<sup>fi</sup>ning each region's boundary in Fig. 1. For example, the upper boundary line for region 3 drawn in Fig. 1 is the linear indifference curve for constrained choice 3 which intersects axis one at $I _ { 1 , 3 } = 1 9 4 2 . 8 6$ and intersects axis two at $I _ { 2 , 3 } = 2 2 6 6 . 6 7$ . The hinge H for region 3 shown in Fig. 1 is the point (0,226.67) which is given in Table 2 as $h _ { 1 , 3 } = 0$ and $h _ { 2 , 3 } = 2 2 6 6 . 6 7$ . Table 3 provides the value function for each of the six regions and the value function coef<sup>fi</sup>cients and constants are summarized in Table 4. Using region $j = 3$ as an example, Eq. (9) gives the linear-fractional value function $\nu _ { 3 } ( x _ { 1 } , x _ { 2 } )$ using the coef<sup>fi</sup>cients and constants $c _ { 1 , 3 } , c _ { 2 , 3 } , d _ { 1 , 3 , } d _ { 2 , 3 } , \alpha _ { 3 } ,$ and $\beta _ { 3 }$ contained in Table 4 to produce the value function in Table 3.

$$
\begin{array}{r l} v _ {3} (x _ {1}, x _ {2}) & = \frac {c _ {1 , 3} x _ {1} + c _ {2 , 3} x _ {2} + \alpha_ {3}}{d _ {1 , 3} x _ {1} + d _ {2 , 3} x _ {2} \beta_ {3}} \\ & = \frac {- 5 0 1 2 8 . 2 0 x _ {1} - 6 5 3 8 . 4 6 x _ {2} + 1 4 8 2 0 5 0 0}{- 2 6 1 . 5 4 x _ {1} + 2 6 1 . 5 4 x _ {2} - 5 9 2 8 2 0} \end{array}\tag{9}
$$

Cost, manpower, and citizen protection concerns provide a number of constraints. Since the patrols require support and supervision in the <sup>fi</sup>eld, the <sup>fi</sup>eld support cost is \$5 for each foot patrol hour and \$4 for each car patrol hour. Since the budget for <sup>fi</sup>eld support cost is \$9600, the <sup>fi</sup>eld support cost constraint is $5 x _ { 1 } + 4 x _ { 2 } \leq 9 , 6 0 0$ . The patrols also require support in the police station where the station support cost is \$5 for each foot patrol hour and \$8 for each car patrol hour. Since the budget for station support cost is \$10,080, the station support cost constraint is $5 x _ { 1 } + 8 x _ { 2 } \leq 1 0 , 0 8 0$ . Each week, a total of 2200 h of of<sup>fi</sup>cer time can be assigned to either foot or car patrols which yields an of<sup>fi</sup>cer hours constraint of $x _ { 1 } + 2 x _ { 2 } \leq 2 2 0 0$ (as stated, each car patrol hour requires two of<sup>fi</sup>cer hours). Finally, the political leaders have determined for citizen safety that the number of foot patrol hours should always equal or exceed the number of car patrol hours which yields a citizen safety constraint of $x _ { 1 } \geq x _ { 2 }$ or writing it as a less than or equal constraint $- x _ { 1 } + x _ { 2 } \leq 0$ . The police patrol example with a piecewise linear-fractional objective function is shown in problem (10). This is essentially the model's PPS.

Table 2  
Axis intercepts and hinges for each region in the police patrol example.

<table><tr><td rowspan="2">Constrained choice</td><td colspan="2">Linear indifference curve</td><td colspan="3">Indifference curve intercepts</td></tr><tr><td colspan="2">Final axis intercepts</td><td>Region</td><td colspan="2">Final hinge coordinates</td></tr><tr><td>j</td><td> $_{11,j}$ </td><td> $_{12,j}$ </td><td>j</td><td> $_{h1,j}$ </td><td> $_{h2,j}$ </td></tr><tr><td>1</td><td>625</td><td>833.33</td><td></td><td></td><td></td></tr><tr><td>2</td><td>1200</td><td>2266.67</td><td>2</td><td>2580</td><td>-2606.67</td></tr><tr><td>3</td><td>1942.86</td><td>2266.67</td><td>3</td><td>0</td><td>2266.67</td></tr><tr><td>4</td><td>2500</td><td>3333.33</td><td>4</td><td>6400</td><td>-5200</td></tr><tr><td>5</td><td>3076.92</td><td>4444.44</td><td>5</td><td>10,000</td><td>-10000</td></tr></table>

$$
\begin{array}{l l} \max v (x _ {1}, x _ {2}) \\ s. t. \\ 5 x _ {1} + 4 x _ {2} \leq 9 6 0 0 & (\text { Field support cost }) \\ 5 x _ {1} + 8 x _ {2} \leq 1 0 0 8 0 & (\text { Station support sost }) \\ x _ {1} + 2 x _ {2} \leq 2 2 0 0 & (\text { Officer hours }) \\ - x _ {1} + x _ {2} \leq 0 & (\text { Citizen safety }) \\ x _ {1}, x _ {2} \geq 0 & (\text { Non - negativity }) \end{array}\tag{10}
$$

The constraints for The Police Patrol problem produce a feasible polygon bounded by the points (0,0), (733.33, 733.33), (1280, 460), (1824, 1200), and (1920, 0). Fig. 2 combines the linear-fractional indifference curves in Fig. 1 with the set of feasible solutions (the shaded polygon).

## 3.2. The two attribute police patrol example solved

Once the DM has established his/her KS and the PPS as depicted in problem (10), the problem can be solved using the solution algorithm provided in Section (Appendix A). The <sup>fi</sup>rst step of the algorithm in the Section Appendix A is to construct the corresponding linear programming problem for region $j = J + 1 = 6 .$ Problem (11) is the resultant linear programming problem using the data in Tables 3 and 4.

Mathematica [16] <sup>fi</sup>nds problem (11)'s optimal feasible solution is $x _ { 1 } ^ { * } { = } 1 9 2 0 \operatorname { a n d } x _ { 2 } ^ { * } { = } 0$ . The optimal value of the objective function value is $\nu _ { 6 } ^ { * } = 0 . 0 4 0 6 2 5 * 1 9 2 0 + 0 . 0 2 8 1 2 5 * 0 = 7 8 .$ . Since $\nu _ { 6 } ^ { * } = 7 8 < V _ { 5 } = 1 2 5 ,$ region 6 does not contain the optimal feasible solution to the linearfractional problem and the algorithm proceeds to Step 2.

Table 3  
Value function for each region in the police patrol example.

<table><tr><td>Region</td><td colspan="2">Value limits</td><td>Value function</td></tr><tr><td>j</td><td> $V_{j-1}$ </td><td> $V_j$ </td><td> $v_j(x1,x2)$ </td></tr><tr><td>1</td><td>0</td><td>25</td><td> $0.04x_1 + 0.03x_2$ </td></tr><tr><td>2</td><td>25</td><td>50</td><td> $\frac{63408.40x_1 + 66258.20x_2 + 9119410}{-427.47x_1 + 427.47x_2 + 2217160}$ </td></tr><tr><td>3</td><td>50</td><td>75</td><td> $-50128.20x_1 - 6538.46x_2 + 14820500$  $-261.54x_1 + 261.54x_2 - 592820$ </td></tr><tr><td>4</td><td>75</td><td>100</td><td> $\frac{127473x_1 + 162527x_2 + 29318700}{-382.42x_1 + 382.42x_2 + 4436040}$ </td></tr><tr><td>5</td><td>100</td><td>125</td><td> $\frac{246753x_1 + 253247x_2 + 64935100}{-389.61x_1 + 389.61x_2 + 7792210}$ </td></tr><tr><td>6</td><td>125</td><td>∞</td><td> $0.040625x_1 + 0.028125x_2$ </td></tr></table>

$$
\begin{array}{l l} \max v (x _ {1}, x _ {2}) \\ s. t. \\ 5 x _ {1} + 4 x _ {2} + x _ {3} = 9 6 0 0 & (\text { Field   support   cost }) \\ 5 x _ {1} + 8 x _ {2} + x _ {4} = 1 0 0 8 0 & (\text { Station   support   cost }) \\ x _ {1} + 2 x _ {2} + x _ {5} = 2 2 0 0 & (\text { Officer   hours }) \\ - x _ {1} + x _ {2} + x _ {6} = 0 & (\text { Citizen   safety }) \\ x _ {1}, x _ {2}, x _ {3}, x _ {4}, x _ {5}, x _ {6} \geq 0 & (\text { Non - negativity }) \end{array}\tag{11}
$$

The <sup>fi</sup>rst run of Step 2 sets $j = 5 ,$ determines that the region 5 value function is linear-fractional and proceeds to Step 4. Step 4 constructs problem (12).

$$
\begin{array}{l l} \max \left\{2 4 6 7 5 3 y _ {1} + 2 5 3 2 4 7 y _ {2} + 6 4 9 3 5 1 0 0 t \right\} \\ s. t. \\ \begin{array}{l l} 5 y _ {1} + 4 y _ {2} + y _ {3} = 9 6 0 0 t = 0 & (\text { Field   support   cost }) \\ 5 y _ {1} + 8 y _ {2} + y _ {4} = 1 0 0 8 0 t = 0 & (\text { Station   support   cost }) \\ y _ {1} + 2 y _ {2} + y _ {5} = 2 2 0 0 t = 0 & (\text { Officer   hours }) \\ - y _ {1} + y _ {2} + y _ {6} = 0 & (\text { Citizen   safety }) \\ - 3 8 9. 6 1 y _ {1} + 3 8 9. 6 1 y _ {2} + 7 7 9 2 2 1 0 t = 1 & (\text { Denominator }) \\ y _ {1}, y _ {2}, y _ {3}, y _ {4}, y _ {5}, y _ {6}, t \geq 0 & (\text { Non - negativity }) \end{array} \end{array}\tag{12}
$$

Mathematica determines that problem (12) has the optimal feasible solution $y _ { 1 } ^ { * } = 0 . 0 0 2 5 5 8 8 1 , y _ { 2 } ^ { * } = 0 . 0 0 0 0 1 6 8 3 4 3 ,$ , and $t ^ { * } { = } \bar { 1 } . 4 0 2 8 6 { * } 1 0 ^ { - 7 } .$ The optimal solution for the original variables is ${ x ^ { * } } \mathrm { { = } } { y ^ { * } } / t ^ { * }$ which yields $x _ { 1 } ^ { * } { = } 1 8 2 4$ and $x _ { 2 } ^ { * } = 1 2 0$ with an optimal function value $V ^ { * } { = } 7 6 . 5 1 2 1$ computed in Eq. (13).

$$
\begin{array}{r l} V ^ {*} & = \frac {c _ {1 , 5} x _ {1} ^ {*} + c _ {2 , 5} x _ {2} ^ {*} + \alpha_ {5}}{d _ {1 , 5} x _ {1} ^ {*} + d _ {2 , 5} x _ {2} ^ {*} + \beta_ {5}} \\ & = \frac {2 4 6 7 5 3 * 1 8 2 4 + 2 5 3 2 4 7 * 1 2 0 + 6 4 9 3 5 1 0 0}{- 3 8 9 . 6 1 * 1 8 2 4 + 3 8 9 . 6 1 * 1 2 0 + 7 7 9 2 2 1 0} = 7 6. 5 1 2 1 \end{array}\tag{13}
$$

Since $V ^ { * } = 7 6 . 5 1 2 1 < V _ { j - 1 } = V _ { 4 } = 1 0 0 ,$ , the optimal feasible solution is in a region below region $j = 5$ so the algorithm proceeds to Step 2.

The second run of Step 2 sets j=4, determines that the region 4 value function is linear-fractional and proceeds to Step 4. Step 4 constructs a linear programming problem like problem (12) except the objective function is max $\{ 1 2 7 4 7 3 \mathrm { y } _ { 1 } + 1 6 2 5 2 7 \mathrm { y } _ { 2 } + 2 9 3 1 8 7 0 0 \mathrm { t } \}$ and the Denominator constraint $\begin{array} { r l } { \mathrm { i } s } & { { } - 3 8 2 . 4 2 y _ { 1 } + 3 8 2 . 4 2 y _ { 2 } + 4 4 3 6 0 4 0 \ \mathrm { t } = 1 . } \end{array}$ Mathematica determines that this linear programming problem has the optimal feasible solution $y _ { 1 } ^ { * } { = } 0 . 0 0 0 4 \bar { 8 } 1 9 \bar { 7 } 9 , y _ { 2 } ^ { * } { = } \bar { 0 } . \bar { 0 } 0 0 0 3 1 7 0 9 2 ,$ and $t ^ { \check { * } } { = } 2 . 6 4 2 4 3 * 1 0 ^ { - 7 }$ . The optimal solution for the original variables $\mathrm { i } s x ^ { * } { = } y ^ { * } / t ^ { * }$ which yields $x _ { 1 } ^ { * } { = } 1 8 2 4$ and $x _ { 2 } ^ { * } = 1 2 0$ with an optimal function value $V ^ { * } { = } 7 4 . 3 4 0 2$ computed in Eq. (14).

$$
\begin{array}{r l} V ^ {*} & = \frac {c _ {1 , 4} x _ {1} ^ {*} + c _ {2 , 4} x _ {2} ^ {*} + \alpha_ {4}}{d _ {1 , 4} x _ {1} ^ {*} + d _ {2 , 4} x _ {2} ^ {*} + \beta_ {4}} \\ & = \frac {1 2 7 4 7 3 * 1 8 2 4 + 1 6 2 5 2 7 * 1 2 0 + 2 9 3 1 8 7 0 0}{- 3 8 2 . 4 2 * 1 8 2 4 + 3 8 2 . 4 2 * 1 2 0 + 4 4 3 6 0 4 0} = 7 4. 3 4 0 2 \end{array}\tag{14}
$$

Since $V ^ { * } { = } 7 4 . 3 4 0 2 { < } V _ { j - 1 } { = } V _ { 3 } { = } 7 5$ , the optimal feasible solution is in a region below region j=4 so the algorithm proceeds to Step 2.

The third run of Step 2 sets $j = 3$ , determines that the region 3 value function is linear-fractional and proceeds to Step 4. Step 4 constructs a linear programming problem like problem (12) except the objective function is max $\left\{ - 5 0 1 2 8 . 2 0 { \ y } _ { 1 } - 6 5 3 8 . 4 6 { \ y } _ { 2 } \right.$ +14820500 t} and the Denominator constraint $\mathrm { i s } - 2 6 1 . 5 4 y _ { 1 } + 2 6 1 . 5 4 y _ { 2 } - 5 9 2 8 2 0 \ t =$ 1. Mathematica determines that this linear programming problem has no feasible solution and the algorithm proceeds to Step 5.

A new linear programming problem like problem (12) is constructed by Step 5 except the objective function is max $\{ 5 0 1 2 8 . 2 0 y _ { 1 } + 6 5 3 8 . 4 6 y _ { 2 } - 1 4 8 2 0 5 0 0 \mathrm { ~ t } \}$ and the Denominator constraint is $2 6 1 . 5 4 \mathrm { y } _ { 1 } - 2 6 1 . 5 4 \mathrm { y } _ { 2 } + 5 9 2 8 2 0 \ : \mathrm { t } = 1$ . Mathematica determines that this linear programming problem has the optimal feasible solution $y _ { 1 } ^ { * } { = } 0 . 0 0 1 7 5 6 4 1$ $y _ { 2 } ^ { * } { = } 0 . 0 0 0 1 1 5 5 5 3$ , and $t ^ { * } =$

Table 4  
Value function coef<sup>fi</sup>cients for each region in the police patrol example.

<table><tr><td>Region</td><td colspan="3">Numerator value function coefficients</td><td colspan="3">Denominator value function coefficients</td></tr><tr><td>j</td><td> $c_{1,j}$ </td><td> $c_{2,j}$ </td><td> $\infty_j$ </td><td> $d_{1,j}$ </td><td> $d_{2,j}$ </td><td> $\beta_j$ </td></tr><tr><td>1</td><td>0.04</td><td>0.03</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>2</td><td>63,408.40</td><td>66,258.20</td><td>9,119,410</td><td>-427.47</td><td>427.47</td><td>2,217,160</td></tr><tr><td>3</td><td>-50128.20</td><td>-6538.46</td><td>14,820,500</td><td>-261.54</td><td>261.54</td><td>-592820</td></tr><tr><td>4</td><td>127,473</td><td>162,527</td><td>29,318,700</td><td>-382.42</td><td>382.42</td><td>4,436,040</td></tr><tr><td>5</td><td>246,753</td><td>253,247</td><td>64,935,100</td><td>-389.61</td><td>389.61</td><td>7,792,210</td></tr><tr><td>6</td><td>0.040625</td><td>0.028125</td><td>0</td><td>0</td><td>0</td><td>1</td></tr></table>

$9 . 6 2 9 4 2 * 1 0 ^ { - 7 }$ . The optimal solution for the original variables is $x ^ { * } =$ $y ^ { * } / t ^ { * }$ which yields $\kappa _ { 1 } ^ { * } \substack { = } 1 8 2 4$ and $x _ { 2 } ^ { * } = 1 2 0$ with an optimal function value $V ^ { * } { = } 7 4 . 5 2 9 7$ computed in Eq. (15).

$$
\begin{array}{r l} V ^ {*} & = \frac {c _ {1 , 3} x _ {1} ^ {*} + c _ {2 , 3} x _ {2} ^ {*} + \alpha_ {3}}{d _ {1 , 3} x _ {1} ^ {*} + d _ {2 , 3} x _ {2} ^ {*} + \beta_ {3}} \\ & = \frac {- 5 0 1 2 8 . 2 0 * 1 8 2 4 - 6 5 3 8 . 4 6 * 1 2 0 + 1 4 8 2 0 5 5 0 0}{- 2 6 1 . 5 4 * 1 8 2 4 + 2 6 1 . 5 4 * 1 2 0 - 5 9 2 8 2 0} \\ & = 7 4. 5 2 9 7 \end{array}
$$

Since $V ^ { * } { = } 7 4 . 5 2 9 7 { \geq } V _ { j - 1 } { = } V _ { 2 } { = } 5 0$ , the optimal feasible solution has been found so the algorithm sets $j ^ { * } { = } 3$ and goes to Step 8 which terminates the algorithm with the optimal feasible solution $x _ { 1 } ^ { * } { = } 1 8 2 4$ and $x _ { 2 } ^ { * } = 1 2 0$ , and $V ^ { * } { = } 7 4 . 5 2 9 7$ . Thus, the optimal solution that maximizes the DM's preferences is to have 1824 foot patrol hours and 120 car patrol hours a week yielding a value of $\boldsymbol { \dot { V } } ^ { * } =$ 74.5297. For the optimal solution, the <sup>fi</sup>eld support cost and station support cost constraints are binding which means the DM cannot increase the patrol hours until the support budgets are increased.

## 4. Discussion

The main contribution of this paper is the development of a DSS which allows a DM to introduce his knowledge, expertise and preferences to build a KS for the system. The implication of this method and the solution algorithm suggest that speci<sup>fi</sup>c PPS models to maximize a DM's preferences can be constructed even when the DM's preference structure is not constant.

15

A common approach for solving scheduling problems uses a traditional maximization problem (of police force coverage) or a minimization problem (of police force costs). In the case of the police patrol example, solving a cost minimization problem would probably not have served the public need for safety. Similarly, solving the problem as a coverage maximization problem may generate a coverage scheme which will be based on the different forces coverage parameters, but may not support the public needs for security. In order to address problems such as the one presented here, when traditional maximization or minimization models do not apply well to the problem domain, this paper offers a different perspective with a DSS which is speci<sup>fi</sup>cally tailored to take into account a KS which is constructed around the preferences, expertise and knowledge of an expert DM. Moreover, the PPS of this DSS can handle the DM's preferences even when they are not constant. The approach provided in this paper can be employed in different organizational settings by generating a problem-speci<sup>fi</sup>c KS. Some of these problems may include scheduling (which is presented here) or in the evaluation of occupancy and room prices in a hotel with changing preferences regarding the price and occupancy scenarios of hotel operations [10].

![](/api/attachments/G7QH9R8Y/fulltext/images/6be853c2d7db54dc7776cdd577a26473f5190f79044e4ccc75c6191d2142c28d.jpg)  
Fig. 2. Attribute space and feasible solution set for the police patrol example.

This system uses an ef<sup>fi</sup>cient algorithm to solve a mathematical programming problem with linear constraints and a piecewise linearfractional objective function. Charnes and Cooper [5] and Wolf [15] have developed algorithms to solve mathematical programming problems with fractional objective functions. However, their algorithms are only applicable to one region objective functions where the linearfractional function is the same over the entire attribute space. This paper divides the attribute space into regions where the linearfractional objective function can be different between regions and then extends Charnes and Cooper's [5] algorithm to this case thus incorporating it into a decision problem PPS. This paper demonstrated how to use a preference elicitation process (KS) and the solution algorithm (PPS) in constructing a DSS for speci<sup>fi</sup>c organizational problems. Future research will employ this approach to model and solve a real life application in n attributes. Future practical applications will develop a computerized DSS in which a DM will be able to provide his preferences, map the constraints and use the system to <sup>fi</sup>nd an optimal solution.

## Appendix A

An algorithm for programs with linear-fractional objective functions and linear constraints

Step 1: (Region J+1) Initialize $j = J + 1$ . Construct and solve region J+1's corresponding linear programming problem (3). If an unbounded solution is found, go to Step 6. If no feasible solution is found, go to Step 7. If the optimal value of the objective function ${ \nu _ { J + 1 } } ^ { * }$ to linear programming problem (3) equals or exceeds ${ V _ { J + 1 } } , { V _ { J + 1 } } ^ { * } \ge V _ { J + 1 } ,$ , then the optimal feasible solution $x ^ { * }$ to linear programming problem (3) is the optimal feasible solution to linear-fractional problem (2), set the optimal value $V ^ { * } = \nu _ { J + 1 } \stackrel { * } { , }$ , and go to Step 8. Otherwise, go to Step 2 as region J+1 does not contain the optimal feasible solution to linear-fractional problem (2).

Step 2: (New region) Set j=j-1. If $d _ { i , j } = 0$ for all $i = 1 , 2 , \cdots , n$ , then v<sub>j</sub>(x) is linear and go to Step 3. Otherwise, $\nu _ { j } ( \boldsymbol { x } )$ is linear-fractional and go to Step 4.

Step 3: (Linear value function region) Construct and solve linear programming problem (3). If the optimal value of the objective function $\bar { \nu _ { j } ^ { * } }$ to linear programming problem (3) equals or exceeds $V _ { j - 1 } , \stackrel { * } { v _ { j } ^ { * } } \geq V _ { j - 1 }$ , then the optimal feasible solution $x ^ { * }$ to linear programming problem (3) is the optimal feasible solution to linear-fractional problem (2), set the optimal value $V ^ { * } = \mathbb  \} _ { j } ^ { * } ,$ , set $j ^ { * } { = } j ,$ and go to Step 8. Otherwise, go to Step 2 as region j does not contain the optimal feasible solution to linear-fractional problem (2).

Step 4: (Linear-fractional linear program, part 1) For region j, de<sup>fi</sup>ne new variable t and n new variables y. Then, construct and solve linear programming problem (7). If no feasible solution exists to linear programming problem (7), go to Step 5. Otherwise, an optimal feasible solution $\mathrm { t } ^ { \ast }$ and $\boldsymbol { \mathrm { y } } ^ { * }$ is found, set the optimal feasible solution in terms of the x variables to ${ \bf x } ^ { * } =$ $\boldsymbol { \mathrm { y } } ^ { * } / \boldsymbol { \mathrm { t } } ^ { * }$ , and set the optimal value of the linear-fractional objective function to $\begin{array} { r } { \mathsf { V } ^ { * } = \mathsf { v _ { j } } ( \mathbf { x } ^ { * } ) . \mathsf { I f } \mathsf { V } ^ { * } \geq \mathsf { V _ { j - 1 } } } \end{array}$ , then the optimal feasible solution has been found, set $\mathrm { { \bar { j } } ^ { * } = j }$ and go to Step 8. Otherwise, go to Step 2.

Step 5: (Linear-fractional linear program, part 2) Construct and solve linear programming problem (8). If no feasible solution exists to linear programming problem $( 8 ) _ { ! }$ , go to Step 2. Otherwise, an optimal feasible solution $t ^ { * }$ and $y ^ { * }$ is found, set the optimal feasible solution in terms of the x variables to ${ x ^ { * } } \mathrm { { = } } { y ^ { * } } / t ^ { * }$ , and set the optimal value of the linear-fractional objective function to $\boldsymbol { V } ^ { \hat { \mathbf { \pi } } } = \nu _ { j } ( \boldsymbol { x } ^ { * } )$ . If $\cdot \boldsymbol { V } ^ { * } \geq V _ { j - 1 }$ , then the optimal feasible solution has been found, set $j ^ { * } { \dot { = } } j$ and go to Step 8. Otherwise, go to Step 2.

Step 6: (Unbounded solution) Terminate the algorithm with an unbounded solution.

Step 7: (No feasible solution) Terminate the algorithm with no feasible solution.

Step 8: (Optimal feasible solution) Terminate the algorithm with optimal value $V ^ { * }$ and the optimal feasible solution $x ^ { * }$ in region j<sup>⁎</sup>.

## References

[1] R.D. Anderson, J.R. Brown, Better park management, Park Maintenance 31 (1978) 10–12.

[2] G.D. Bhatt, J. Zaveri, The enabling role of decision support systems in organizational learning, Decision Support Systems 32 (2002) 297–309.

[3] J.R. Brown, A.A. Israeli, Solving multiattribute decision problems using a linear-fractional model: the two attribute case, International Journal of Operations and Ouantitative Management 15 (2009) 45–63.

[4] J.R. Brown, A.A. Israeli, Solving multiattribute decision problems using a linear-fractional model: the n attribute case, International Journal of Operations and Ouantitative Management 16 (2010) 331-347.

[5] A. Charnes, W.W. Cooper, Programming with linear fractional functionals, Naval Research Logistics Quarterly 9 (1962) 181–186

[6] K. Chelst, An algorithm for deploying a crime directed (tactical) police force, Management Science 24 (1978) 1314–1327.

[7] A.T. Ernst, H. Jiang, M. Krishnamoorthy, D. Sier, Staff scheduling and rostering: a review of applications, methods, and models, European Journal of Operational Research 153 (2004) 3–27

[8] A. Greasley, Process improvement within a HR division at a UK police force, International Journal of Operations & Production Management 24 (2004) 230–240.

[9] L. Green, P. Kolesar, Testing the validity of a queueing model of police patrol Management Science 35 (1989) 127–148

[10] A.A. Israeli, J.R. Brown, Modelling a decision maker's preferences Part 2: a tool for pricing decisions in the hospitality industry, Tourism Economics 10 (2004) 5–22.

[11] R.S. Kaplan, D.P. Norton, How to implement a new strategy without disrupting your organization, Harvard Business Review (March 2006) 100–109.

[12] R.C. Larson, Police deployment introduction, Management Science 24 (1978) 1278–1279.

[13] D.N. Manocha, Empirical testing of the decision utility model, Doctoral dissertation, Kent State University, Kent, OH, 1986.

[14] P.E. Taylor, S.J. Huxley, A break from tradition for the San Francisco police: patrol of<sup>fi</sup>cer scheduling using an optimization-based decision support system, Interfaces 19 (1989) 4–24.

[15] H. Wolf, A parametric method for solving the linear fractional programming problem, Operations Research 33 (1985) 835–841.

[16] S. Wolfram, The Mathematica Book, Fifth ed. Wolfram Media and Cambridge University Press, 2003.

[17] M. Zeleny, Multiple Criteria Decision Making, McGraw-Hill, 1982.

J. Randall Brown is an emeritus professor in the Management and Information Systems Department, College of Business Administration at Kent State University. H earned a BS in Electrical Engineering, a SM in Management, and a Ph.D. in Management all from the Massachusetts Institute of Technology. Dr. Brown has published over 40 articles in many journals including Management Science, Operations Research, Mathematical Programming, Naval Research Logistics Ouarterly, and Journal of Statistical Soft ware. He has also chaired 29 dissertations.

Aviad A. Israeli is an associate professor at Ben Gurion's University's Guilford Glaser Faculty of Business and Management in Israel and a visiting professor at the College of Business Administration. Kent State University. He earned a BA from Haifa University and an MBA and Ph.D. from Kent State University. Dr. Israeli's main area of interest is management in service industries with speci<sup>fi</sup>c focus on hospitality. He published in many journals including Service Industries Journal, Tourism Economics and the Interna tional Journal of Hospitality Management
