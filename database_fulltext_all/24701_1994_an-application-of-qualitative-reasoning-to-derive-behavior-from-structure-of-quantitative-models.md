---
otero_id: 24701
otero_key: "5BTXCVU8"
title: "An Application of Qualitative Reasoning to Derive Behavior from Structure of Quantitative Models"
authors: "Srinivasan Raghunathan"
year: "1994"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1994.11518031"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Application of Qualitative Reasoning to Derive Behavior from Structure of Quantitative Models

## Srinivasan Raghunathan

To cite this article: Srinivasan Raghunathan (1994) An Application of Qualitative Reasoning to Derive Behavior from Structure of Quantitative Models, Journal of Management Information Systems, 11:1, 73-100, DOI: 10.1080/07421222.1994.11518031

To link to this article: http://dx.doi.org/10.1080/07421222.1994.11518031

![](/api/attachments/5BTXCVU8/fulltext/images/f0154e3e79401e9b1d53cb0df1283ededb9c4c440b113ba7049042173d9a7282.jpg)

Published online: 14 Dec 2015.

![](/api/attachments/5BTXCVU8/fulltext/images/ad9f3972e56041bcb5be67d497782cb2b43a09532b0c2de293eb24a13964d23b.jpg)

Submit your article to this journal ↗

![](/api/attachments/5BTXCVU8/fulltext/images/7d7aee13cf05c208256fc56e3ce346d4d3bb48835a8bb2f6e1e5d53650286a24.jpg)

View related articles ↗

# An Application of Qualitative Reasoning to Derive Behavior from Structure of Quantitative Models

SRINIVASAN RAGHUNATHAN

SRINIVASAN RAGHUNATHAN is an assistant professor of MIS at the Bowling Green State University, Bowling Green, Ohio. He obtained his Ph.D. degree from the Katz School of Business, The University of Pittsburgh, in 1990. His current research interest is in the integration of artificial intelligence and operations research techniques to support managerial problem solving.

ABSTRACT: Mathematical modeling and analysis are a valuable tool in decision support contexts. Consequently, model management system(s) have become a key component of decision support system generators. Model management systems support modelers in various phases of the modeling life cycle including model representation, formulation, selection, integration, and execution. An important phase of the modeling life cycle involves analyzing and explaining the behavior of the formulated model. Such an analysis is necessary to understand the structure and behavior of the model, and to verify the appropriateness of the model to the problem. Traditional computer-based methods of analysis use the model solution as a basis to explain the model structure that caused the solution. This article presents an alternate approach that explains model behavior using the model structure and commonsense mathematical rules. The approach builds upon the qualitative reasoning methodology, developed in the artificial intelligence area to explain the behaviors of physical devices. A benefit of the qualitative reasoning approach is that it may describe the causes of modeling errors in terms of model structure. I also describe an implemented prototype model preprocessor that uses qualitative reasoning to provide qualitative explanations of the model behavior prior to solving the model. While I do not claim the sufficiency of the qualitative reasoning approach to detect and describe all types of modeling behavior, the article presents several examples demonstrating the utility of the approach.

KEY WORDS AND PHRASES: artificial intelligence, computer-assisted analysis, decision support systems, model management systems, modeling, qualitative analysis.

## 1. Introduction

THE VALUE OF MATHEMATICAL MODELING AND ANALYSIS in decision support contexts is well recognized. As a consequence, the model management system has become a key component of decision support system (DSS) generators. Model management systems support modelers in different phases of the modeling life cycle, including model representation, formulation, execution, and maintenance. $^{1}$ An important phase of this life cycle involves analyzing and explaining the structure and the behavior $^{2}$ of the formulated model. Such an analysis is necessary to gain “deep” $^{3}$ knowledge about the model, and to verify the appropriateness of the model to the problem. The traditional computer-based model analysis methods have relied on the model solution to explain the model structure that caused the solution. For instance, Greenberg’s ANALYZE system [12] explains the structure of a linear programming (LP) model by analyzing its solution. Numerous other analytical techniques use the phase-I solution of an LP model to explain its behavior [13]. However, experienced human modelers frequently explain model behavior by qualitatively analyzing the model structure without actually solving the model. Such explanations usually focus on the “interesting” descriptive characteristics of the solution, such as the range, the order of magnitude, and the trend, rather than the exact numerical values. Modelers appear to use qualitative knowledge about the underlying causal connections among the model components to generate such explanations. This research attempts to identify and use such knowledge in explaining models.

The motivations for developing qualitative reasoning methods for model management stem from unresolved problems in modeling. We want to identify the core knowledge that underlies the modeling expertise. Human modelers appear to use qualitative causal reasoning to understand and explain the behavior of models. Judging from the kinds of explanations that human modelers give, this reasoning is quite different from the model solution algorithms used in model analysis methods and from those taught in the classrooms. This raises questions as to what this knowledge is like, and how it helps a modeler reason about a model. Some of the modeling-related issues have been addressed by previous research in automatic model formulation $[3, 16, 20, 22, 25]$ model maintenance $[21]$ , and in empirical investigations of the modeling process of experienced modelers $[22, 25]$ . Qualitative reasoning provides additional tools that seek to improve our understanding of the modeling process and enhance the capabilities of model management systems in DSS generators.

The artificial intelligence (AI) community first investigated the use of qualitative reasoning methods to derive and explain the behaviors of physical devices, such as electronic circuits and heat exchangers, from the device structures $[5]$ . The primary research objective here is to explore the potential role of qualitative reasoning methodology in explaining mathematical models. The focus is restricted to a class of models consisting of algebraic spreadsheet models that include systems of equations/inequalities, and mathematical programming (MP) models. The secondary objective is to construct, on the basis of principles of qualitative reasoning, a model preprocessor that identifies and explains the causes of at least some of the incorrectly formulated models prior to solving them.

This research indicates that the significant advantage of the qualitative reasoning approach lies in its explanation of model behavior in terms of “commonsense” mathematical rules that can be understood by even those without extensive knowledge of model solution algorithms. Experience with the model preprocessor suggests that it can complement the model solvers as an additional model analysis tool in model management systems. However, the qualitative reasoning approach appears to be most appropriate for models with loosely connected variables.

This article is organized as follows: section 2 discusses the qualitative reasoning methodology used in AI and explores its usefulness in model management. Section 3 illustrates the qualitative reasoning techniques that explain model behavior. Section 4 discusses the implementation details of this model preprocessor. The fifth section then offers analysis of the scope and limitations of the qualitative reasoning approach, while the sixth section concludes with a summary.

## 2. Qualitative Reasoning: Background

QUALITATIVE REASONING, AS USED BY THE AI COMMUNITY, deals with explaining how physical systems work in qualitative terms. A collection of the most influential articles in qualitative reasoning can be found in [5] and in [26]. De Kleer illustrates the use of qualitative reasoning approach in electronic circuits in [6]. We illustrate the basic idea behind qualitative reasoning using a mathematical model.

Consider the following algebraic model (assume that all the variables in the model are nonnegative):

$$
\begin{array}{l} 0. 5 * U \leq V; \\ U = W + X; \\ V \leq Y; \\ X \geq Z; \\ Z \geq 2 0 0; \\ Y \leq 7 5. \end{array}
$$

Traditional computer-based model analysis methods solve this model by using mathematical algorithms. However, when an experienced human modeler is asked to analyze the model, the modeler is likely to describe the behavior in terms of a sequence of events, each of which is “caused” by previous events. Each event is an assertion about some behavioral parameter of some constituent of the model (i.e., values and ranges for variables in the model etc.) A typical explanation is given below.

Since Y is less than or equal to 75, and V is less than or equal to Y, V should be less than or equal to 75 which in turn causes 0.5 \* U to be less than or equal to 75. That means U should be less than or equal to 150 which causes W + X to be less than or equal to 150. However, since X is greater than or equal to Z which is lower bounded by 200, X is at least 200. So W + X should be at least 200 because the variables are nonnegative. This contradicts the previous conclusion that W + X is less than or equal to 150.

The above description of the behavior of the model is similar to the electronic circuit behavioral description discussed in [6]. Qualitative reasoning methodology provides the inference mechanisms needed to derive explanations of behavior, such as the one described above.

An important shared characteristic of qualitative reasoning research in AI is that the behavioral description of physical systems is compositional—that is, the description of the system's behavior must be derivable from the structure of the system. "Structure" refers to the components of the analysis, component behaviors, and the connections among components. For example, the resistors and transistors form some of the components of an electronic circuit. In a mathematical model, the variables and the constraints form the structure. "Behavior" refers to the time course of observable changes of the state of the components and the system as a whole. In electronic circuits, behavior is described in terms of the current through the resistor, state of the transistor, and so on, whereas in mathematical models, the behavior is described in terms of the specific values and ranges assumed by variables.

Another shared characteristic of qualitative reasoning methods is that the behavior is derived by propagating the component behaviors locally, through specified connections among device components. This contrasts sharply with traditional computer-based analysis methods. In traditional methods, systems are described using mathematical models, such as differential equations, which provide constraints on the state variables. Analytical techniques or solution algorithms determine the allowable time-varying behavior of these variables, but there is no sense from these solutions of how that time course comes to be. Descriptive terms of behavior are derived by interpreting the resulting solution, rather than from an understanding of the “causal” processes underlying the system. In contrast, qualitative reasoning attempts to explicate these causal processes by providing explicit links between the structure and the behavior of the system.

It appears that qualitative reasoning can play a useful role in explaining mathematical models. As discussed in the previous paragraphs, mathematical models are similar to physical devices. Although exact solution to a model is desirable, and is often obtained using model solvers, there are situations when the modeler may not be interested in the exact numerical solution. Some broad qualitative characteristics, such as the range, of the solution may be adequate. We believe that qualitative analysis may prove to be useful in these situations. In addition, qualitative reasoning may provide the modeler with the “deep” knowledge about the behavior of models necessary to gain expertise in modeling.

It should be emphasized that qualitative reasoning does not attempt to derive or explain the exact behavior—that is, precise numerical solution. The qualitative reasoning methods cannot, in general, derive the exact behavior [6]. Sometimes, the explanations themselves may be ambiguous. For instance, qualitative reasoning may derive multiple behavioral patterns because of the lack of, or its inability to derive, precise numerical values of certain parameters [6].

Qualitative reasoning research in AI has developed many techniques, such as qualitative calculus [6], interval arithmetic [24], and qualitative simulation [17]. These techniques have been applied to perform a variety of different tasks such as diagnosis [9], simulation [17], and design verification [2]. Many of the above techniques that explain physical devices are also useful in explaining mathematical models. We have augmented these techniques with additional rules specific to mathematical models. We illustrate the qualitative reasoning techniques and how they explain model behavior next.

## 3. Qualitative Reasoning in Mathematical Models

THE QUALITATIVE REASONING TECHNIQUES DESCRIBED in this section are applicable to a variety of related classes of models such as algebraic spreadsheet models and mathematical programming. These models are characterized by a set of constraints consisting of equations and/or inequalities. The functions represented in the models can be linear or nonlinear. The mathematical programming (MP) models also have an objective function. We use the following production planning problem as an example to illustrate the representation of model structure and the derivation of behavior from the structure.

A manufacturer produces different products using a set of resources. The products are transported to sales sites where sales take place. The manufacturer has various constraints related to demand, resource capacity, transportation capacity, and others. The problem is to plan the production level.

We begin with a discussion of model structure representation.

## 3.1. Structure Representation

Mathematical models can be represented using a variety of modeling languages including GAMS [15], LINDO [23], and the more recent Structured Modeling Language (SML) [10]. We use SML in our implementation of the preprocessor because it is the most formal, structured, and also expressive representation scheme to date. Also, SML is being increasingly used in the model management research as a tool to represent models. However, we illustrate qualitative reasoning using the traditional textbook notation used to represent models. We use the example model shown in figure 1. The SML representation of the same model, and a brief description of SML is provided in the appendix; an exhaustive description can be found in [10].

## 3.2. Behavior Description

The exact behavior of a model is described by the assignment of values to variables (in SML terminology, the attribute elements) that satisfies the constraints (test elements in SML). $^{4}$ In the case of MP models, the assignment should also maximize/minimize the objective function. However, as mentioned in section 2, qualitative reasoning attempts not explicitly to solve the model, but to explain the “interesting” characteristics of the model behavior in terms of the model structure. In many domains, these interesting behaviors are denoted by meaningful domain-specific terms. For example, in the domain of financial markets, if the number of stocks traded in a day exceeds a certain number, the market is termed “active,” otherwise the market is called “moderate” or “passive.” Identification of such categories of behavior generally requires domain knowledge. We are focusing on mathematical models which are used in a variety of domains. Hence, we illustrate our ideas with the following domain-independent behavior types that are frequently used to characterize mathematical models.

$$
\text { Profit } = \text { Totrevenue } - \text { Totcost }\tag{c1}
$$

$$
\text { Totrevenue } = P _ {a} ^ {*} (S _ {a, s 1} + S _ {a, s 2})\tag{c2}
$$

$$
\text { Totcost } = U _ {r} ^ {*} C _ {r} + Z _ {a, s 1} ^ {*} T _ {a, s 1} + Z _ {a, s 2} ^ {*} T _ {a, s 2}\tag{c3}
$$

$$
\text { Totprodn } = P _ {\mathbf {a}} ^ {*} X _ {\mathbf {a}}\tag{04}
$$

$$
S _ {\mathbf {a}, \mathbf {s} 1} \geq E _ {\mathbf {a}, \mathbf {s} 1}\tag{∞5}
$$

$$
S _ {\mathbf {a}, \mathbf {s} 2} \geq E _ {\mathbf {a}, \mathbf {s} 2}\tag{∞}
$$

$$
S _ {\mathbf {a}, \mathbf {s} 1} \leq D _ {\mathbf {a}, \mathbf {s} 1}\tag{c7}
$$

$$
S _ {\mathbf {a}, \mathbf {s} 2} \leq D _ {\mathbf {a}, \mathbf {s} 2}\tag{8}
$$

$$
Z _ {\mathbf {a}, \mathbf {s} 1} + Z _ {\mathbf {a}, \mathbf {s} 2} \leq X _ {\mathbf {a}}\tag{∞}
$$

$$
Z _ {\mathbf {a}, \mathbf {s} 1} \leq W _ {\mathbf {a}, \mathbf {s} 1}\tag{c10}
$$

$$
Z _ {\mathbf {a}, \mathbf {s} 2} \leq W _ {\mathbf {a}, \mathbf {s} 2}\tag{c11}
$$

$$
S _ {\mathbf {a}, \mathbf {s} 1} \leq Z _ {\mathbf {a}, \mathbf {s} 1}\tag{c12}
$$

$$
S _ {\mathbf {a}, \mathbf {s} 2} \leq Z _ {\mathbf {a}, \mathbf {s} 2}\tag{c13}
$$

$$
U _ {r} = U _ {r, a} ^ {*} X _ {a}
$$

$$
V _ {r} \leq A _ {r}\tag{c14}
$$

$$
P _ {a} = \text { Price } (A) = 5 0\tag{c15}
$$

$$
X _ {a} = \text { Production } (A)
$$

$$
A _ {r} = \text { Availability } (R) = 7 5
$$

$$
C _ {r} = \operatorname{Cost} (R) = 5
$$

$$
U _ {r, a} = \text { Utilrate } (R, A) = 0. 5
$$

$$
V _ {r} = \text { Utilization } (R)
$$

$$
D _ {\mathbf {a}, \mathbf {s} 1} = \text { Maxdemand } (A, S 1) = 5 0 0
$$

$$
D _ {\mathbf {a}, \mathbf {s} 2} = \text { Maxdemand } (A, S 2) = 5 0 0
$$

$$
E _ {\mathbf {a}, \mathbf {s} 1} = \text { Mindemand } (A, S 1) = 2 5
$$

$$
E _ {\mathbf {a}, \mathbf {s} 2} = \text { Mindemand } (A, S 2) = 2 0 0
$$

$$
S _ {a, s 1} = \text { Sales } (A, S 1)
$$

$$
S _ {a, s 2} = \text { Sales } (A,
$$

$$
W _ {a, s 1} = \text { Capacity } (A, S 1) = \infty
$$

$$
W _ {\mathbf {a}, \mathbf {s} 2} = \text { Capacity } (A, S 2) = 3 0 0
$$

$$
Z _ {\mathbf {a}, \mathbf {s} 1} = \operatorname{Transq} (A, S 1)
$$

$$
Z _ {\mathrm{a}, \mathrm{s} 2} = \text { Transq } (A, S 2)
$$

## Figure 1. The Algebraic Model

1. Infeasibility: Infeasibility represents the situation when no assignment of values to variables can satisfy the constraints of the model. Infeasibilities occur due to incorrect formulations, overspecification of the model, physical impossibilities, and for other reasons.

2. Unboundedness: Unboundedness represents the situation when a variable or a function (especially the objective function) assumes extremal values such as $+/-\infty$ . Unboundedness typically occurs because of missing constraints and underspecification of the model.

3. Boundedness: Boundedness represents the situation when all the variables and functions (especially the objective function) assume values in a finite range, usually tighter than what is explicitly specified in the model. Boundedness is a very broad classification of what may actually be several behavior types. For example, depending on the domain in which the model is used, a range, such as (10, 20), of the objective function may be denoted by type I behavior, and a range, such as (20, 30), may be denoted by type II. Both these ranges will fall under the boundedness type in our case because we do not assume a priori domain-specific knowledge. Note that unboundedness can be considered as a special case of boundedness.

Along with the above three types of behavior, we include redundancy as the fourth type. Though redundancies in a model do not characterize the behavior per se, we include them because they affect the time needed to obtain the exact behavior through a solver. Redundancies also provide additional insights into the model structure by identifying model elements that do not affect model behavior. The time saved by removing the redundancies in the model can be very significant, especially for integer and mixed-integer programming models $[14]$ .

4. Redundancy: Redundancy represents the situation when the model contains variables, functions, or constraints that do not affect the model behavior.

Behavior types 1, 2, and 4 indicate that the formulated model contains modeling errors, or that the model design can be improved. Type 3 provides insights into the model behavior not readily observed in the model structure itself. We should emphasize that modeling errors can be detected by other analytical techniques [13]. However, as Greenberg and Murphy [13] point out, the diagnosis of modeling errors “seem totally dependent on the problem and the astuteness of the analyst. There is no dominant method that provides a good diagnosis for all modeling errors. Instead, we should think of these techniques as a toolkit for some intelligent aid” to the modeler. We view qualitative reasoning as an additional tool for the diagnosis of models. The primary benefit of qualitative reasoning remains in the explanation of the behavior in terms of model structure and common-sense arithmetic knowledge.

## 3.3. Qualitative Reasoning Rules

Given a model represented in SML or other schemes, how does qualitative reasoning derive its behavior without actually solving it? Qualitative reasoning methodology derives behavior by applying common-sense mathematical rules to the values of variables and functions in the model, and the interconnections among these elements, that is, constraints.

In mathematical models, a variable can have a constant value, the value determined through a function, and/or the value limited by lower and upper bounds. We use intervals, instead of constants, to represent the values of variables and functions for qualitative reasoning purposes. For example, an interval such as $(3, 8)$ indicates that the variable can assume a value between 3 and 8. A variable that has a constant value such as 5 would be assigned the interval (5, 5). An interval such as $(-∞, ∞)$ indicates that the variable can assume any value. It is assumed here that all the intervals are closed intervals. However, the methodology can be applied to open and semiopen intervals by making minor modifications to the rules discussed in the next section.

Qualitative reasoning applies a variety of model-structure-related rules to the intervals and the constraints that connect these intervals. The structure rules derive tighter intervals and new constraints not specified in the model, and modify existing constraints. Qualitative reasoning then applies the behavior rules to derive a characterization of the model behavior. The individual rules themselves are simple commonsense rules; but the collection and the systematic application of these rules provide a powerful inference mechanism.

## 3.3.1. Structure Rules

Structure rules make inferences about the model elements such as the variables and constraints. The rules are based on arithmetic laws. Similar structure rules have been previously employed in domains such as VLSI design and geology [24].

a. Interval Arithmetic: Interval arithmetic allows the derivation of the interval of a function using the intervals of its arguments. The four basic interval arithmetic operations are shown in figure 2. The arithmetic for more complex functions, such as polynomial functions, can be derived using these basic operations. Interval arithmetic has been studied extensively in mathematics [19]. It has also been previously applied to analyze LP models [18]. However, unlike [18], interval arithmetic is just one among the many techniques in the qualitative reasoning approach.

EXAMPLE (taken from [24]):

$$
\begin{array}{l} \text { Consider   the   following: } \\ A \geq 3, A \leq 4 (\text { i.e.,   the   interval   of } A \text { is } (3, 4)); \\ B \geq 1, B \leq 4 (\text { i.e., } (1, 4)); \\ C = 2 (\text { i.e., } (2, 2)); \\ D = (B ^ {*} C) / (A + B). \end{array}
$$

In the above model, we can show that the interval of $(B^{*}C)$ is (2, 8), and the interval of $(A+B)$ is (4, 8) using the interval arithmetic rules IA3, and IA1 respectively. Then, using IA4, we get (0.25, 2) as the interval of D.

When interval arithmetic derives more than one interval for a variable or a function, the most constraining interval is used for further analysis. Consider the following example:

$$
\begin{array}{l} A = B + C, A = D + E; \\ 6 \leq B \leq 3 0, 4 \leq C \leq 1 0, 3 \leq D \leq 1 0, 2 \leq E \leq 2 0. \end{array}
$$

Using the interval arithmetic, we can show that A is assigned the intervals $(10, 40)$ and $(5, 30)$ . Qualitative reasoning will use the interval $(10, 30)$ for A in further analysis.

$$
\begin{array}{l} \text {IA1. (xl, xu) + (yl, yu) = ((xl + yl), (xu + yu))} \\ \text {IA2. (xl, xu) - (yl, yu) = ((xl - yu), (xu - yl))} \\ \text {IA3. (xl, xu) * (yl, yu) = (min(xl*yl, xl*yu, xu*yl, xu*yu), max(xl*yl, xl*yu, xu*yl, xu*yu))} \\ \text {IA4. (xl, xu) / (yl, yu) = (-∞,∞) if yl <   0 and yu > 0} \\ (\min (x l / y l, x l / y u, x u / y l, x u / y u), \max (x l / y l, x l / y u, x u / y l, x u / y u)) \\ \text {otherwise} \end{array}
$$

Figure 2. Interval Arithmetic

Nonoverlapping intervals, such as (10, 20) and (40, 50), for an expression indicates infeasibility in the model. We discuss infeasibility in more detail in section 3.3.2.

b. Transitivity Arithmetic: Transitivity arithmetic allows derivation of new constraints using constraints already known. The transitivity arithmetic for relational constraints is shown in figure 3. For example, if the model specifies that A = B and $B \geq C$ , then we can derive that $A \geq C$ using transitivity arithmetic. However, transitivity arithmetic alone is insufficient in many situations to derive new constraints. For example, if A > B, and B < C, then transitivity arithmetic cannot derive a constraint between A and C.

c. Relational Arithmetic: Relational arithmetic allows inferences, such as if X > Y then $X + 5 > Y + 5$ and vice versa, and which cannot always be derived using interval and transitivity arithmetic. The axioms of relational arithmetic are shown in figure 4. In this figure, RA1 states that if expressions x and y are related by a relational operator in a constraint, then the same relational operator will hold if another expression is added to or subtracted from both x and y. If an expression z subtracts both x and y, then the left and right hand sides of the relationship are exchanged in the new relationship.

EXAMPLE:

$$
\begin{array}{l l} \text { Assume } X ^ {2} + Y ^ {2} \geq Z ^ {2}. \text { Then } & X ^ {2} + Y ^ {2} + W ^ {2} \geq Z ^ {2} + W ^ {2}, \text { and } \\ 1 0, 0 0 0 - Z ^ {2} \geq 1 0, 0 0 0 - (X ^ {2} + Y ^ {2}). \end{array}
$$

d. Relational Inference: Relational inference allows derivation of constraints between two expressions based on their intervals, and vice versa. The axioms of relational inference are shown in figure 5. For example, relational inference rule RI1 states that if the upper bound of an expression X is lower than or equal to the lower bound of expression Y, then $X \leq Y$ . On the other hand, if it is known that $X \leq Y$ , then we can infer that the upper bound of X does not exceed the upper bound of Y. Similarly, RI3 states that if the lower bound of X is greater than or equal to the upper bound of Y, then $X \geq Y$ , and if it is known that X > Y, then the lower bound of X is not lower than the lower bound of Y.

$$
\begin{array}{c c c c c c c c c} & & & & \text { B   op   C } \\ & & <   & <   = & > & > = & = & <   > \\ \hline & <   & <   & <   & ? & ? & <   & ? \\ \text { A } & <   = & <   & <   = & ? & ? & <   = & ? \\ \text { op } & > & ? & ? & > & > & > & ? \\ \text { B } & > = & ? & ? & > & > = & > = & ? \\ \hline & = & <   & <   = & > & > = & = & <   > \\ \hline & <   > & ? & ? & ? & ? & <   > & ? \end{array} \quad \text { A   op   C } \quad \text { ?   means   that   relationship   is   unknown   op   --   operator }
$$

Figure 3. Transitivity Table

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
For op in  $\{&lt;, \leq, &gt;, \geq, = &lt;&gt;\}$ ,
RA1. x op  $y \leftrightarrow (x+z)$  op  $(y+z)$ ,  $(x-z)$  op  $(y-z)$ ,  $(z-y)$  op  $(z-x)$ 
RA2. For  $x, z \geq 0$ 
    x op  $y \leftrightarrow (x^{*}z)$  op  $(y^{*}z)$ ,  $(x/z)$  op  $(y/z)$ 
RA3. For  $x, z &lt; 0$ 
    x op  $y \leftrightarrow (z^{*}y)$  op  $(z^{*}x)$ ,  $(y/z)$  op  $(x/z)$
</div>

Figure 4. Axioms for Relational Arithmetic

EXAMPLE:

$$
X \geq 2, X \leq 5 (\text {i.e.,} (2, 5));
$$

The reader can verify that all of the above structure rules are sound rules, that is, they deduce only correct inferences. It should also be observed that structure rules make deductions only about the model structure.

## 3.3.2. Behavior Rules

Behavior rules transform the model structure into behavioral descriptions. Since we are focusing only on the four types of behavior discussed in section 3.2, we discuss the applicable behavior rules in the following paragraphs.

## a. Infeasibility:

INF1. The model is infeasible if two or more intervals without a common

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Let $(h, u1)$ and $(l2, u2)$ be the intervals of X and Y respectively.

RI1. $u1 \leq l2 \rightarrow X \leq Y \rightarrow u1 \leq u2$

RI2. $u1 &lt; l2 \rightarrow X &lt; Y \rightarrow u1 &lt; u2$

RI3. $h1 \geq u2 \rightarrow X \geq Y \rightarrow h1 \geq l2$

RI4. $h1 &gt; u2 \rightarrow X &gt; Y \rightarrow h1 &gt; l2$

RI5. $h1 = u1 = l2 = u2 \rightarrow X = Y \rightarrow h1 = l2, u1 = u2$
</div>

```txt
Figure 5. Axioms for Relational Inference
region is assigned, or derived as the value of a variable or a function.
EXAMPLE:
0 ≤ X ≤ 5 (i.e., (0, 5));
X + 5 ≥ 12.
Using relational arithmetic rule RA1, X ≥ 7 (i.e., (7,∞)).
The intervals (0, 5), and (7,∞) do not have a common region, hence the model is infeasible.
INF2. The model is infeasible if any of the following occurs with respect to a constraint t:
a. t is a ≤ constraint, and lhs of t can be shown to be > the rhs.
b. t is a < constraint, and lhs of t can be shown to be ≥ the rhs.
c. t is a = constraint, and lhs of t can be shown to be < or > the rhs
d. t is a > constraint, and lhs of t can be shown to be ≤ rhs.
e. t is a ≥ constraint, and lhs of t can be shown to be < rhs.
f. t is a <> constraint, and lhs can be shown to be = rhs.
EXAMPLE:
0 ≤ X ≤ 1 (i.e., (0, 1));
0 ≤ Y ≤ 2 (i.e., (0, 2));
0 ≤ Z ≤ 3 (i.e., (0, 3));
X + (Y*Z) ≥ 10.
Using interval arithmetic, the interval of X + (Y*Z) is (0, 7), Using relational inference rule RI2, X + (Y*Z) < 10. Hence, rule INF2 states that the model is infeasible.
b. Unboundedness:
UNB1. The model is unbounded if a variable or a function assumes a value of (∞, ∞) or (−∞, −∞).
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Maximize $X + Y - 2Z$, Subject to $2 \leq X \leq 10$; $0 \leq Z \leq 5$; $Y \geq 0$.
</div>

## EXAMPLE:

In the above model, X has the interval $(2, 10)$ , Z has the interval $(0, 5)$ , and Y has the interval $(0, \infty)$ . Hence, the interval of the objective function, using interval arithmetic, is $(2, \infty)$ . Since the objective of the modeler is to maximize the objective function, the objective function will assume its upper bound, that is, as the value in the solution. Hence, the objective function is unbounded.

## c. Boundedness:

BOU1. The value of a variable or a function is bounded by $(l, u)$ where l = maximum of the lower bounds of all intervals assigned to, or derived for it u = minimum of the upper bounds of all intervals assigned to, or derived for it. Note that if l > u, it is infeasible.

## EXAMPLE:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Maximize $X + Y + Z$ Subject to 1. $1 \leq X \leq 5$; 2. $X + Z \geq 10$; 3. $Y + Z \leq 60$; 4. $0 \leq Y \leq 20$.
</div>

In the above model, the interval of X is $(1, 5)$ , and the interval of Y is $(0, 20)$ . Now using constraint 2, the interval of X, and the relational inference rule RI3, we can determine that the lower bound of Z is 5. Using constraint 3, the interval for Y, and the rule RI 3, the upper bound of Z can be determined as 60. So, the interval of Z is $(5, 60)$ . Now, the interval of the objective function becomes $(6, 85)$ , using interval arithmetic.

Typically, we say that a model is bounded if all the variables and functions, including the objective function, in the model assume finite intervals.

## d. Redundancy:

RED1. A variable is redundant if it is not used in the derivation of any new interval or constraint.

RED2. A constraint t is redundant if the following can be derived without using t: In the case of $\leq$ constraints, the upper bound of the lhs is $\leq$ the lower bound of the rhs. For $\geq$ constraints, the lower bound of the lhs is $\geq$ the upper bound of the rhs. For = constraints, the lower and upper bound of the lhs is = to the lower and upper bound of the rhs.

The following rules are applicable specifically to MP models that have an objective function.

RED3. A variable a is redundant if the value of the objective function does not depend on the value of a. In other words, the interval of a is not used in the derivation of the interval of the objective function.

RED4. A constraint is redundant if it is not used in the derivation of the interval of the objective function.

## EXAMPLE:

Maximize $X^2 + Y^2$

Subject to

1. $X + Y \leq Z$ ;

2. $0 \leq X \leq 10$ ;

3. $XY + Z\geq 5$

4. $0 \leq Y \leq 15$ .

In the above model, the interval of X is $(0, 10)$ , and the interval of Y is $(0, 15)$ . Z can assume any value. The interval of the objective function then becomes $(0, 325)$ . Since, this interval does not depend on the interval of Z, Z is redundant. Also, constraints 1 and 3 are not used in the derivation of intervals for X and Y, and hence the objective function. So constraints 1 and 3 are also redundant.

In summary, structure rules infer new intervals and constraints by analyzing the model specified by the modeler. The behavior rules then transform this model structure into behavioral descriptions. In the previous paragraphs, we illustrated the individual qualitative rules with simple examples. Next, we illustrate the qualitative reasoning methodology in detail with the example model given in figure 1.

## 3.4. Qualitative Reasoning in the Example Problem

Consider the model given in figure 1. The qualitative reasoning procedure first transforms the data into intervals for the corresponding variables in the model. For example, the cost data 5 for resource R is transformed into $(5, 5)$ for the variable $C_{r}$ (i.e., $\text{cost}(R)$ ). Then, the procedure systematically applies all the applicable structure rules to derive new intervals and constraints. For example, consider the variable MINDEM(A, S2). The modeler has specified the interval of MINDEM(A, S2) as $(200, 200)$ . The constraint c6 states that SALES(A, S2) ≥ MINDEM(A, S2). Hence, the interval of SALES(A, S2) can be inferred as $(200, \infty)$ using the relational inference rule RI1. In a similar manner, the structure rules can infer the following intervals.

<table><tr><td>Variable/function</td><td>Interval</td></tr><tr><td>MINDEM(A, S2)</td><td>(200, 200)</td></tr><tr><td>SALES(A, S2)</td><td>(200,∞)</td></tr><tr><td>TRANSQ(TRANS(A, S2))</td><td>(200,∞)</td></tr><tr><td>TRANSQ(TRANS(A, S1))</td><td>(0,∞)</td></tr><tr><td>PRODUCTION(A)</td><td>(200,∞)</td></tr></table>

Qualitative reasoning will now determine that the interval of UTILRATE(R,A)\*PRO-

DUCTION(A), the rhs of the constraint c14, as $(100, \infty)$ using the intervals of UTILRATE(R, A) and PRODUCTION(A), and IA3. So, the interval of UTILIZATION(R), the lhs of c14, becomes $(100, \infty)$ since c14 is an equality constraint. However, using c15 and the interval of AVAILABILITY(R), the interval of UTILIZATION(R) is also inferred as $(0, 75)$ . Now, qualitative reasoning will conclude, using behavior rule INF1, that the model is infeasible because UTILIZATION(R) is assigned two nonoverlapping intervals, namely $(0, 75)$ , and $(100, \infty)$ .

The behavior of the model is thus characterized by infeasibility. It was claimed in section 2 that a primary goal of the qualitative reasoning methodology is to explain the behavior of the model in qualitative terms like a human modeler does. We also mentioned that experienced modelers describe behavior in terms of a sequence of events, each of which is caused by previous events, and that each event is an assertion about some parameter of some constituent of the model. For our example model, the derivation procedure for its infeasibility can be explained in a number of ways at various levels of detail. One such explanation, which can be easily generated by a computer analyzing the model, is shown in Table 1.

Though the above explanation is not as clear as the natural language explanation that may be provided by human modelers, we can observe that the above explanation is similar, at least at the surface level, to that provided by human modelers. Both explanations are organized in terms of events, the preceding events causing the succeeding ones.

Let us consider a variation of the example problem. Assume that the modeler wishes to plan his production level so that TOTPRODN is maximized. The qualitative reasoning procedure will still conclude that the model is infeasible. However, the procedure will also conclude, by applying the rules for redundancy, COST and TRANSQ variables, the function PROFIT, and constraints c12 and c13, are redundant. We illustrate the reasoning process briefly below. Qualitative reasoning will determine the interval of the objective function TOTPRODN as $(10000,\infty)$ . This is derived from the interval $(200,\infty)$ for PRODUCTION(A) and the interval $(50,50)$ of PRICE(A), and the rule IA3. No other interval can be derived for the objective function. Also, the intervals used to derive $(10000,\infty)$ do not depend on the intervals of COST, and TRANSQ. Hence, using the rule RED3, qualitative reasoning determines that these attributes are redundant. The explanations for redundancies can be provided in a manner similar to the explanation shown for infeasibility.

## 4. The Model Preprocessor

THE QUALITATIVE REASONING METHODOLOGY HAS BEEN IMPLEMENTED as a model preprocessor using Common Lisp on a 386 microcomputer. The architecture of the preprocessor is shown in figure 6. The pre-processor takes an SML model as input. First, it transforms the SML model into a model network that makes explicit the interconnections among the model elements. The model network representation facilitates the preprocessor in its application of qualitative rules. The preprocessor extends the model network (i.e., adds new intervals and constraints) using the structure rules. Finally, the preprocessor applies the behavior rules to the extended model network to derive the model behavior description. During this reasoning process, the preprocessor also creates a dependency network that links the model elements with the behavior. The dependency network is used to generate explanations of the behavior. We discuss the specific implementation details of the preprocessor in the following paragraphs.

Table 1

<table><tr><td>Event</td><td>Model Feature</td><td>Inference</td><td>Reason</td></tr><tr><td>1</td><td>MINDEM (A, S2)</td><td>(200, 200)</td><td>200) USER</td></tr><tr><td>2</td><td>SALES (A, S2)</td><td>(200,∞)</td><td>c6, RI1</td></tr><tr><td>3</td><td>TRANSQ (A, S2)</td><td>(200,∞)</td><td>c13, RI1</td></tr><tr><td>4</td><td>PRODUCTION (A)</td><td>(200,∞)</td><td>c11, RA1</td></tr><tr><td>5</td><td>UTILIZATION (R)</td><td>(100,∞)</td><td>c14, IA3, RI1</td></tr><tr><td>6</td><td>AVAILABILITY (R)</td><td>(75, 75)</td><td>USER</td></tr><tr><td>7</td><td>UTILIZATION (R)</td><td>(0, 75)</td><td>c15, RI1</td></tr><tr><td>8</td><td>UTILIZATION (R)</td><td>Infeasible</td><td>INF1</td></tr></table>

![](/api/attachments/5BTXCVU8/fulltext/images/ad69c10b14cd2cf69362a4eba73cc6422347c6f2167e6badd9d1d57f8feb9160.jpg)  
Figure 6. The Architecture of the Model Preprocessor

## 4.1. Model Network

The preprocessor represents the model elements as a directional network in which the variable, function, and the lhs and the rhs of the constraints form the nodes. The nodes representing the lhs and the rhs of a constraint are connected by an arc. The arc is marked by the operator that indicates the constraint between the nodes. For example, a constraint such as $X + 5 \geq Y$ is represented as $X + 5 \stackrel{\geq}{\rightarrow} Y$ . The node representing a function has incoming arcs from the nodes representing its arguments. Also, each node has an associated interval(s) that represents the lower and upper bounds on the value of the node. For example, if variable X has its lower bound as 0 and upper bound as 10, the corresponding node will have the interval (0, 10).

A segment of the initial model network for our example production planning model is shown in figure 7. In this figure, the nodes UTILIZATION(R) and AVAILABILITY(R) represent the corresponding variables in the model (figure 1), and the arc that connects these two nodes represents the constraint c15. Note that the network contains nodes for variables (e.g., AVAILABILITY(R)), functions (e.g., TOTPRODN), and the left- and right-hand sides of constraints (e.g., UTILRATE(A, R)\*PRODUCTION(A)) in the model. The nodes representing the variables (e.g., AVAILABILITY(R)) and functions with known data values have their intervals specified. Also, the arcs that connect the lhs and the rhs of the constraints (e.g., c15) in the model have their operators specified.

## 4.2. Qualitative Analysis Algorithm

The model preprocessor applies all the applicable structure rules to the initial model network using an exhaustive search of the nodes and links. The search procedure derives all possible new intervals and constraints that could be derived in the model network using the structure rules. The new intervals and constraints are added to the model network. When the preprocessor cannot derive any new interval or constraint using the structure rules, it applies the behavior rules to the extended network to determine the model behavior type. The qualitative analysis algorithm is given below.

ALGORITHM QualAnal(ModelNetwork, StructureRules, BehaviorRules)
Initialize the intervals of all the nodes to $(-∞, ∞)$ Repeat

{Compute intervals for nodes using Interval Arithmetic rules} For each function node with a single interval in the network, applicable Interval Arithmetic rules to determine the interval of the node.

{Compute intervals for nodes using Relational Inference rules}
For each link with a single constraint and that connects nodes with single intervals,

Apply the applicable Relational Inference rules to determine the intervals of the nodes connected by the link.

{Compute new constraints among nodes using Relational Arithmetic rules} For each link with a single constraint,

Apply the applicable Relational Arithmetic rules to determine new constraints among nodes in the network.

{Compute new constraints among nodes using Transitivity table}

For each pair of links of the form A op1 B, and B op2 C,

Apply the transitivity table to determine the constraint between A and C.

![](/api/attachments/5BTXCVU8/fulltext/images/673457e93a4917f9d8c4c96c13e63c680b502e409dade191648281ecc17aa707.jpg)  
Figure 7. A Segment of the Initial Model Network

Until there is no modification to the model network or the computational resources have exceeded.

Apply the behavior rules to all the nodes and links in the extended model network.

END QualAnal.

Note that the procedure attempts to identify all the rules that are applicable in the specific model by systematically searching through the rules and the elements of the model network. The procedure determines that a rule is applicable to a model element (such as a node or link) if the element matches with the antecedent of the rule. The procedure is repeated until either it does not result in any new intervals or constraints because any modification to the network has the potential to modify some other part of the network, or computational resources such as the CPU are exceeded before the solution converges. The order in which the structure rules are applied is irrelevant as all the rules are searched in one cycle of the loop. We can also note that only nodes and links that have single interval and constraint respectively are used to make further inferences. There are two reasons for this restriction. First, nodes with multiple intervals indicate infeasibility because, as mentioned in section 3.3.1, if the intervals are overlapping, then the most constraining interval (i.e., a single interval) is assigned to the node, and nonoverlapping intervals indicate infeasibility (Rule INF1 discussed in section 3.3.2). A similar reason applies to links. Second, when a node (or a link)

has more than one interval (constraint), making further inferences using the node (link) is complex because the inferences need to be made for all the intervals. As a result, the reasoning process becomes combinatorially explosive, but the model will still be characterized by infeasibility.

The above algorithm does raise two issues. The first issue is whether the algorithm will converge to a solution. Although the algorithm will terminate ultimately because of the preset resource limit, the algorithm is likely to converge to a solution before the limit is reached. We show informally that the algorithm indeed converges to a solution using the following reasoning. The algorithm terminates when there are no modifications to the model network. The network can be modified in three ways: the interval for a node can be changed, the constraint in a link can be changed, or a new link with the appropriate constraint can be added. When the interval for a node is changed, it can only constrain the original interval, as described in the previous paragraph. Such changes will ultimately make the interval a constant (the lower and upper values of the interval become equal) preventing further modifications (unless, of course, a non-overlapping interval is assigned, in which case the node will not be considered again anyway). In the case of a link, once the constraint in a link is made =, >, or <, further changes are not possible. Also, with respect to the third way of modification to the network, only a finite number of new links can be created as the initial model network has a finite number of nodes. So, the modifications will ultimately converge to a solution. However, there may exist special model structures for which the algorithm may take infinite number of iterations before the convergence. This topic needs further research.

The second issue is the computational complexity. Each cycle in the loop of the above algorithm has a worst case complexity of $O(N^{2})$ , where N is the number of nodes in the network. $^{5}$ However, the average case complexity, although difficult to determine, is much better. As we discuss later about our experience with the preprocessor, the algorithm appears to work well, especially for models that have loosely connected variables with finite intervals. The above algorithm is a straightforward implementation in which we were concerned only with making all qualitative inferences about the model. Improvements, such as identifying portions of the model network that get affected by a change and analyzing only those portions further, and the like, can be made to improve the average case performance.

The extended model network generated by the preprocessor for our example model is shown in figure 8, where the shaded regions represent the derivations made by the preprocessor. The extended model network represents, in addition to the derivations made by the preprocessor, a dependency network [8] (shown as dotted lines in figure 8) that allows the preprocessor to generate explanations of the model behavior.

## 4.3. Dependency Network

Whenever the model network is modified and the behavior type is determined, the preprocessor also creates dependencies between the model elements and the inferences. The dependencies indicate the reasons or causes for the inferences made by the preprocessor during the qualitative reasoning process. Our implementation of the dependencies maintains a list of justifications for each node, interval, and arc in the model network. An element in the network may be justified by the modeler (by making it as part of the initial model), or by other elements in the network along with a qualitative rule. We represent a justification for z as the following logical implication:

![](/api/attachments/5BTXCVU8/fulltext/images/17bc919a73099b35d8ab59d15b27f0b3b0a674ec6fa9850acfaed903b3f41f08.jpg)  
Figure 8. A Segment of the Extended Model Network

$$
x _ {1}, x _ {2}, \dots , x _ {\mathrm{n}}, y \rightarrow z,
$$

where $x_{i}$ 's are elements in the model network and y is a qualitative rule. The comma represents the conjunction. For example, in figure 8, MINDEM(A, S2): (200, 200), c13, RI3 → SALES(A, S2): (200, ∞) indicates that the interval (200, ∞) for SALES(A, S2) is justified by the model elements MINDEM(A, S2): (200, 200) and c13, and the relational inference rule RI3. In the figure, the conjunction is denoted by an arc that connects the elements that form the justification.

Dependency networks have been used in AI systems for a variety of purposes including verification of the consistency of the knowledge base $[8]$ , intelligent backtracking during the problem solving process $[7]$ , and sensitivity analysis $[21]$ . In our implementation, the dependency network is used only to record the reasoning steps used by the preprocessor. The dependency network is later used by the preprocessor to trace through the steps and explain its analysis of the model.

## 4.4. Generating Explanations

The process of generating explanations of the model behavior is straightforward once the final model network and the dependency network are set up. The process starts with the node representing the model behavior, and determines the justifications for the behavior node. It repeats the process with these justifications until the nodes are modeler defined. The collection of justifications thus obtained forms the sequence of events that caused the behavior—that is, the collection provides an explanation for the behavior. The above procedure is implemented using the following algorithm:

ALGORITHM Explain(Extended\_Model\_Network)
Initialize OPEN and CLOSED to empty lists
For each behavior node in the network,
Do
Add the node to the end of OPEN
Repeat
Determine the justification of the first element of OPEN
Add all the nodes in the justification to the end of OPEN
Add the pair consisting of the first element of OPEN and its justification to the end of CLOSED
Remove the first element from OPEN
until OPEN is empty
Display CLOSED from first to the last element.
end.
END Explain.

For example, in figure 8, the node infeasibility is justified by the conjunction of intervals (0, 75) and $(100, \infty)$ of the node UTILIZATION(R), and the behavior rule INF1. The preprocessor collects the justifications for both the intervals. The interval (0, 75) for UTILIZATION(R) is justified by the interval (75, 75) of AVAILABILITY(R), the operator $\leq$ of the arc that connects UTILIZATION(R) and AVAILABILITY(R), and RI1. Now, the preprocessor will obtain the justifications for the intervals associated with AVAILABILITY(R) and the operator $\leq$ , and both of these justifications are modeler defined. The preprocessor will then obtain the justifications for the second interval, that is, $(100, \infty)$ , for UTILIZATION(R) in a similar manner. These justifications will then be provided as an explanation for the infeasibility. Note that the collection of these justifications, arranged in the reverse order, is the same as the explanation of the infeasibility shown in section 3.

## 4.5. Evaluation of the Preprocessor

The model preprocessor has been evaluated using an experiment. The goal of the experiment was twofold: one, to get some insights into the qualitative analyses used by a human modeler and the preprocessor for the same models; and two, to demonstrate the feasibility of qualitative reasoning approach and its analyze the scope. We used 25 simple textbook models in our experiment. They consisted of 15 algebraic spreadsheet, financial, and IFPS models with sets of equations/inequalities and 10 optimization models. The optimization models were taken from an introductory management science textbook [1]. All the models contained fewer than 100 variables and constraints.

The models were given to the model preprocessor and an experienced modeler. The human modeler was a faculty member who has extensive experience in mathematical modeling. The human modeler was asked to analyze the models mentally and to come up with the complete solution, or a description of the partial solution for each of the models. The human modeler was also asked to provide reasons for his analysis. Before the experiment, the human modeler was told that he could describe the behavior in terms of the four types discussed in section 3.3.2, that is, infeasibility, boundedness, unboundedness, and redundancy. However, the human modeler was not restricted to only those types. The human modeler was not allowed to use any tool such as a computer package or even a calculator, although he was allowed to use paper and pencil.

The descriptions of model behavior, and the reasoning processes obtained from the human modeler and the preprocessor were then compared for similarities. Table 2 summarizes the results obtained. Note that the preprocessor and the human modeler derived the same behavior for 15 models, 60 percent of those used in the experiment. In these 15 models, the explanations were different in four cases even though the behavioral descriptions were the same. In two cases, the modeler was not able to derive the behavior and both of them were optimization models. The preprocessor could not derive the behavior for one spreadsheet model and an optimization model. The time taken by the human modeler to derive the behavior of a model ranged from two to thirty minutes. On the contrary, the preprocessor did not take more than two minutes for any model.

The differences in the solutions and the explanations obtained from the modeler and the preprocessor can be attributed to several factors. As indicated earlier, the preprocessor and the human modeler gave different explanations for the same behavior in four models. The primary reason for such differences lies in the implementation of the preprocessor itself. We mentioned in section 4.2 that the preprocessor does not use the node or link that contributes to infeasibility in making further inferences. In effect, the preprocessor does not investigate all the ways of deriving infeasibility. In many mathematical models, there are multiple ways of establishing infeasibilities. For instance, consider the following segment of a model:

$X \geq Y, X \leq Z, Z$ has the interval (100, 100), and $Y$ has the interval $(200, \infty)$ .

Using the interval for Z, and rule RI1, we can establish that the interval for X is $(0, 100)$ . Using the interval for Y and rule RI1, we can establish the interval for X as $(200, \infty)$ . Now that X has two overlapping intervals, the model is determined as infeasible. We can also establish infeasibility by showing that X < Y by using the interval $(0, 100)$ of X, $(200, \infty)$ of Y, and rule RI1. Hence, the same behavior can be explained in two ways. In the models we used in our experiment, the differences were due to different orders in which inferences were made by the preprocessor and the human modeler.

Table 2 Preprocessor Evaluation Results

<table><tr><td></td><td>Equations/inequalities</td><td>Optimization</td><td>Total</td></tr><tr><td>Same behavior, same explanation</td><td>8</td><td>3</td><td>11</td></tr><tr><td>Same behavior, different explanation</td><td>3</td><td>1</td><td>4</td></tr><tr><td>Different behaviors</td><td>3</td><td>3</td><td>6</td></tr><tr><td>No behavior from modeler</td><td>0</td><td>2</td><td>2</td></tr><tr><td>No behavior from preprocessor</td><td>1</td><td>1</td><td>2</td></tr></table>

For some models, the preprocessor and the human modeler gave different behavioral descriptions. A reason for these differences was the human modeler's knowledge of simple solution techniques such as solving simultaneous equations. The preprocessor does not have this knowledge. For example, consider the following model segment:

$$
X + Y = 3, \text {   and   } 2 X + 3 Y = 8; \text {   both   variables   } \geq 0.
$$

The preprocessor will conclude that the model is bounded, in the sense that X will have the interval $(0, 3)$ and Y will have an interval $(0, 2.67)$ . However, the human modeler will give the exact solution to the model, that is, X has the interval $(1, 1)$ and Y has the interval $(2, 2)$ .

In two models, the human modeler was not able to derive any behavioral description, whereas the preprocessor identified that these models contained redundant variables or constraints. However, the reason for this difference was simple human error. When the preprocessor results were shown to the modeler, he admitted that he overlooked certain details of the model. The preprocessor could outperform the human modeler in these cases because it systematically applies all the rules available to it whereas the human modeler may not conduct a thorough search of his or her knowledge base.

In two models, the preprocessor could not derive any behavioral description whereas the human modeler could derive a description. In these two cases, the human modeler used a variety of qualitative rules not known to the preprocessor. For instance, in one model, the human modeler inferred that $X + Y \geq X$ from the constraint $X^{2} + Y^{2} = Z^{2}$ . He explained the reasoning by stating that the second constraint holds true for a right-angled triangle and that in any triangle the sum of any two sides is greater than or equal to the third, represented by the first constraint. This illustrates that human modelers use a wide variety of qualitative knowledge, and it may be impossible to represent all this knowledge in a computer system.

Although our experience with the preprocessor is limited and the results are preliminary, it suggests that the preprocessor appears to provide “good” logical explanations of the model behavior. Our experience has also provided us a number of insights about the methodology in general.

## 5. Scope and Limitations of Qualitative Reasoning

THE QUALITATIVE REASONING APPROACH IS BENEFICIAL in the modeling process in a number of ways. First, it is an alternate and a new approach to analyze models. The traditional computer-based model analysis methods use model solutions. Postsolution analysis is cumbersome and time-consuming because it attempts to get insights into the model structures in a backward fashion by interpreting their solutions. The qualitative reasoning approach attempts to uncover the structure during the derivation of the behavior itself. Second, model simplifications through preprocessing can reduce the time needed to solve the model exactly. Earlier work on model reformulation has shown that speedups of 50 to 75 percent are possible [14]. The time savings can be especially significant for integer and mixed integer programming models which usually require a large computational time. Third, qualitative reasoning approach has the inherent ability to generate explanations of the behavior of models. These explanations are in terms of common-sense qualitative laws that can be understood even by modelers without extensive knowledge of solution algorithms. In traditional computer-based analysis, interpretation of model results can be extremely difficult even for very experienced modelers [12].

However, qualitative reasoning has many limitations. For example, the qualitative rules described here can derive only certain types of behaviors and the rules are not sufficient to derive even these limited types in some cases. For instance, qualitative reasoning cannot make any inference when a model contains only constraints such as A > B, and B < C. Sometimes, the derived intervals may not provide additional insights. For instance, if X has an interval $(0, \infty)$ , and Y has an interval $(0, \infty)$ , then qualitative analysis will derive the interval $(0, \infty)$ for $X + Y$ , which is not useful. A reason for the inability of the qualitative reasoning procedure to derive behavior in these cases is that it uses simple common-sense rules that are applicable to a wide variety of mathematical models.

We also found that qualitative reasoning provides maximum benefit when the constraints in the model relate a small number of variables with finite upper and lower bounds. This may inhibit the application of qualitative reasoning to large models with densely connected variables. However, we believe that even in such situations the modeler may be able to get additional insights into the model structure by using qualitative analysis. For instance, many optimization models have dense constraint sets. In these cases, even though the modeler is interested in the best solution that maximizes (or minimizes) the objective function, a range on the magnitude of the objective function provided by the qualitative analysis is extremely useful before a detailed analysis of the model is performed. For example, if the qualitative analysis derives an interval such as $(10, 100)$ for the objective function—say, profit—and the modeler was expecting to achieve a profit of at least 150, then the model clearly needs to be changed, or the modeler should change his or her goal.

Qualitative reasoning, in general, has other limitations whether it is applied to mathematical models or physical devices. Research in AI has shown that qualitative reasoning may result in the derivation of multiple behavior types and that they may not be resolved unless additional information becomes available or assumptions are made about the device structures [6]. In such cases, only an exact numerical solution may be able to remove the ambiguity among the behavior types. This observation reinforces our view that qualitative reasoning is just another tool to understand the structure of models and it should work in conjunction with traditional computer-based analysis.

## 6. Conclusions

WE HAVE PRESENTED A NEW APPROACH, BASED ON QUALITATIVE common-sense rules, to analyze and explain model behaviors. The approach is part of a general move towards developing integrated modeling environments [11] that support all phases of modeling. The significant benefit of using the qualitative reasoning in model management is the generation of qualitative explanations of model behaviors. These explanations, we believe, would provide deep insights into abstract models. The insights gained through the analysis would enhance our understanding and knowledge of mathematical models. Another advantage of qualitative reasoning is that it can be used to preprocess models before they are solved. The preprocessing may result in model simplifications that reduce the time needed to solve the model. Our experience with an implemented preprocessor suggests that qualitative reasoning is especially useful when the model has loosely connected variables. Our experience also suggests that qualitative reasoning can be applied to a wider class of models if additional qualitative rules can be developed. Currently, we are in the process of investigating analytical results developed in the modeling area to derive additional common-sense qualitative rules.

## NOTES

1. An exhaustive bibliography of model management systems can be found in [4].

2. The terms model "behavior" and "solution" are used synonymously throughout.

3. "Deep" knowledge refers to the understanding of the causal processes that produce specific behaviors.

4. Variable and attribute, and constraint and test element are used synonymously in the rest of this article.

5. The maximum number of links in the network is assumed (i.e., $^{N}C_{2}$ ), which is $O(N^{2})$ .

## REFERENCES

1. Anderson, D.J.; Sweeney, D.J.; and Williams, T.A. An Introduction to Management Science: Quantitative Approaches to Decision Making. St. Paul, MN: West Publishing, 1988.

2. Barrow, H.G. VERIFY: a program for proving correctness of digital hardware design. Artificial Intelligence, 24 (December 1984), 437–491.

3. Binbasioglu, M., and Jarke. M. Domain-specific DSS tools for knowledge-based model building. Decision Support Systems, 2 (June–July 1986), 213–223.

4. Blanning, R.; Whinston, A.; Holsapple, J.M.; Kimbrough, S.O.; and Prietula, M. Model management systems. In E.A. Stohr and B.R. Konsynski (eds.), Information Systems and Decision Processes. New York: Academic Press, 1992.

5. Bobrow, D.G. Qualitative Reasoning about Physical Systems. Cambridge, MA: MIT Press, 1985.

6. De Kleer, J. How circuits work. Artificial Intelligence, 24 (December 1984), 205–280.

7. Dhar, V. Using knowledge generated in heuristic search for non-chronological backtracking. Computational Intelligence, 2 (1986), 151–158.

8. Doyle, J. A truth maintenance system. Artificial Intelligence, 12 (1979), 231–272.

9. Genesereth, M.R. The use of design principles in automated diagnosis. Artificial Intelligence, 24 (December 1984), 411–437.

10. Geoffrion, A.M. An introduction to structured modeling. Management Science, 33 (1987), 547–588.

11. Geoffrion, A.M. Integrated modeling systems. Computer Science in Economics and Management, 2 (1989), 3–15.

12. Greenberg, H.J. A functional description of ANALYZE: a computer-assisted analysis system for linear programming models. ACM Transactions on Mathematical Software, 9 (1983), 18–56.

13. Greenberg, H.J., and Murphy, F.H. Approaches to diagnosing infeasible linear programs. ORSA Journal on Computing, 3 (Summer 1991), 180–201.

14. Karwan, M.H.; Lofti, V.; Telgen, J.; and Zionts, S. Redundancy in Mathematical Programming: A State of the Art Survey. Berlin: Springer Verlag, 1983.

15. Kendrick D., and Meeraus, A. GAMS: An Introduction. Palo Alto, CA: The Scientific Press, 1987.

16. Krishnan, R. Automated model construction: a logic based approach. Annals of Operations Research, 21 (1989), 195–226.

17. Kuipers, B. Commonsense reasoning about causality: deriving behavior from structure. Artificial Intelligence, 24 (December 1984), 169–205.

18. Lodwick, W.A. The use of interval arithmetic in uncovering the structure of linear systems. In R.E. Moore (ed.), Reliability in Computing. London: Academic Press, 1988.

19. Neumaier, I. Interval Methods for Systems of Equations. Cambridge: Cambridge University Press, 1990.

20. Murphy, F., and Stohr, E. An intelligent system for formulating linear programs. Decision Support Systems, 2 (June–July 1986), 39–47.

21. Raghunathan, S.; Krishnan, R.; and May, J. On using belief maintenance systems to assist mathematical modeling. Working Paper, AI in Management Laboratory, Joseph M Katz Graduate School of Business, University of Pittsburgh, 1991.

22. Raghunathan, S.; Krishnan, R.; and May, J. MODFORM: a knowledge based tool to support the modeling process. Information Systems Research, 4 (December 1993), 331–358.

23. Schrage, L. Linear, Integer, and Quadratic Programming with LINDO. Palo Alto, CA: Scientific Press, 1984.

24. Simmons, R. Commonsense arithmetic reasoning. Proceedings of the National Conference on Artificial Intelligence, Philadelphia, PA (1986), pp. 118–124.

25. Vinze, A.; Sen, A.; and Liou, S.F.T. AEROBA: a blackboard approach to model formulation, Proceedings of Hawaii International Conference on System Sciences, vol. 3, January 1992, pp. 551–564.

26. Weld, D.S., and de Kleer, J. Readings in Qualitative Reasoning about Physical Systems. Palo Alto, CA: Morgan Kaufmann, 1988.

## Appendix

STRUCTURED MODELING REPRESENTS A MODEL using definitional elements. There are five element types.

1. Primitive entity (pe) elements have no associated value and generally represent distinctly identifiable entities (e.g., PRODUCT in figure 1).

2. Compound entity (ce) elements have no associated value and generally represent things or concepts that are defined in terms of other things or concepts (e.g., TRANS which is defined in terms of PRODUCT and SSITE in figure 1).

3. Attribute (a) elements have a constant value and generally represent properties of things or concepts (e.g., PRODUCTION is an attribute of PRODUCT in figure 1).

4. Function (f) elements have a value that is dependent according to a definite rule on the values of the called elements and generally represent calculable properties and more complex aspects of models (e.g., TOTREVENUE associated with the sales of products in figure 1). In MP models a function element is designated as the objective function which the modeler may wish to maximize or minimize.

5. Test (t) elements are like function elements except that their value must be either true or false (e.g., MINSALES in figure 1 represents that the constraint that sales should exceed the minimum demand should be TRUE). In MP models, the test elements are relational constraints.

The model described using the above five elements is called the elemental structure that aims to capture all of the definitional detail of a specific model instance. In addition to the elemental structure, the structured model representation also has a generic structure that captures natural familial groupings of elements, and a modular structure that organizes the generic structure hierarchically.

## An Example SML. Model

&SAMPLE\_MODEL,

&PDATA PRODUCT DATA

PRODUCTi/pe/ There is a list of PRODUCTS.

PRODUCTION(PRODUCTi)/va/{PRODUCT}: R+ There is a certain amount of PRODUCTION associated with each PRODUCT measured in units.

PRICE(PRODUCTi)/a/{PRODUCT}: R+ Every PRODUCT has a unit. PRICE measured in \$/unit.

&RDATA RESOURCE DATA

RESOURCEj/pe/ There is a list of RESOURCES

AVAILABILITY(RESOURCEj)/va/{RESOURCE}: R+ There is a certain amount of AVAILABILITY associated with each RESOURCE measured in units.

UTILRATE(RESOURCEj,PRODUCTi)/a/{RESOURCE} \* {PRODUCT}: R+ Every RESOURCE and PRODUCT combination has a resource utilization rate measured in units of resources/unit of product.

UTILIZATION(RESOURCEj)/va/{RESOURCE}: R+ Every RESOURCE has a certain UTILIZATION measured in units.

COST(RESOURCEj)/a/{RESOURCE}: R+ Every RESOURCE has unit

COST measured in \$/unit.
&SDATA SALES DATA
SSITEk/pe/ There is a list of sales sites where the products are sold.
MAXDEM(PRODUCTi, SSITEk)/a/{PRODUCT} \* {SSITE}: R+
Every SSITE and PRODUCT combination has a MAXDEMAND measured in units.
MINDEM(PRODUCTi, SSITEk)/a/{PRODUCT} \* {SSITE}: R+ Every SSITE and PRODUCT combination has a MINDEMAND measured in units.
SALES(PRODUCTi, SSITEk)/va/{PRODUCT} \* {SSITE}: R+ Every SSITE and PRODUCT combination has a certain SALES measured in units.

## &TDATA TRANSPORTATION DATA

TRCOST(TRANSik)/a/{TRANS}: R+ Every TRANS has a unit TRCOST measured in \$/unit.

CAPACITY(TRANSik)/a/{TRANS}: R+ Every TRANS has CAPACITY measured in units.

TRANSQ(TRANSik)/va/{TRANS}: R+ Every TRANS has TRANS-QUANTITY measured in units

TOTREVENUE(PRICE, SALES)/f/; SUMi(PRICEi\*SUMk(SALESik)) The TOTAL REVENUE is the summation of revenues from all products.

TOTCOST(COST, UTILIZATION, TRCOST, TRANSQ)/f/; SUMj(UTILIZATION-j\*COSTj) +

SUMi SUMk (TRCOSTik \* TRANSQik) The TOTAL COST is the summation of resource costs and transportation costs.

PROFIT(TOTREVENUE, TOTCOST)/f/; TOTREVENUE-TOTCOST The PROFIT is revenue minus cost.

TOTPRODN(PRODUCTION, PRICE)/f/; SUMi(PRICEi \* PRODUCTIONi) The TOTAL PRODUCTION VALUE is the production values of all products.

T:MINSALES(SALESik, MINDEMik)/t/{PRODUCT} {\*SSITE}; SALESik ≥ MINDEMik Sales of a PRODUCT at a SALES SITE should meet the MINIMUM DEMAND TEST.

T: MAXSALES(SALESik, MAXDEMik)/t/{PRODUCT} \* {SSITE}; SALESik ≤ MAXDEMik Sales of a PRODUCT at a SALES SITE cannot exceed the MAXIMUM DEMAND TEST.

T:TRANSP(TRANSQi., PRODUCTIONi)/t/{PRODUCT}; SUMk(TRANSQik) ≤ PRODUCTIONi The amount of a PRODUCT transported to all the SSITES cannot exceed the PRODUCTION. TRANSPORTATION TEST.

T:TRANSCAP(TRANSQik,CAPACTYik)/t/{TRANS};TRANSQik≤CAPACITY-ik The amount of a PRODUCT transported to a SSITE cannot exceed the TRANSPORT CAPACITY TEST.

T: SALES(SALESik, TRANSik)/t/{PRODUCT} \* {SSITE}; SALESik ≤ TRANSQik The amount of a PRODUCT sold at a SSITE cannot exceed the amount transported to that SSITE. SALES TEST.

T:RES(UTILIZATIONj, AVAILABILITYj)/t/{RESOURCE}; UTILIZATIONj ≤ AVAILABILITYj This is RESOURCE CAPACITY TEST.

T:RESUTIL(UTILIZATIONj, UTILRATEj., PRODUCTIONi)/t/{RESOURCE}; UTILIZATIONj = SUMi(UTILRATEji\*PRODUCTIONi) The UTILIZATION of a resource is UTILRATE times the PRODUCTION of all PRODUCT. RESOURCE UTILIZATIONTEST.

Elemental Data Table for the SML Model

<table><tr><td>PRODUCT</td><td></td><td colspan="4">RESOURCE</td></tr><tr><td>PRODUCT</td><td>PRICE</td><td>RESOURCE</td><td colspan="2">AVAILABILITY</td><td>COST</td></tr><tr><td>A</td><td>50</td><td>R</td><td colspan="2">75</td><td>5</td></tr><tr><td>UTILRATE</td><td></td><td></td><td colspan="2">SSITE</td><td></td></tr><tr><td>RESOURCE</td><td>PRODUCT</td><td>UTILRATE</td><td colspan="2">SSITE</td><td></td></tr><tr><td>R</td><td>A</td><td>0.5</td><td colspan="2">S1</td><td></td></tr><tr><td></td><td></td><td></td><td colspan="2">S2</td><td></td></tr><tr><td>MAXDEM</td><td></td><td></td><td colspan="2">MINDEM</td><td></td></tr><tr><td>PRODUCT</td><td>SSITE</td><td>MAXDEM</td><td>PRODUCT</td><td>SSITE</td><td>MINDEM</td></tr><tr><td>A</td><td>S1</td><td>500</td><td>A</td><td>S1</td><td>25</td></tr><tr><td>A</td><td>S2</td><td>500</td><td>A</td><td>S2</td><td>200</td></tr><tr><td>TRANS</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PRODUCT</td><td>SSITE</td><td>TRCOST</td><td colspan="2">CAPACITY</td><td></td></tr><tr><td>A</td><td>S1</td><td>0</td><td colspan="2">—</td><td></td></tr><tr><td>A</td><td>S2</td><td>5</td><td colspan="2">300</td><td></td></tr></table>
