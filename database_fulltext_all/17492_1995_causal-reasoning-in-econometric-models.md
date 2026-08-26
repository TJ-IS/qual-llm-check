---
otero_id: 17492
otero_key: "D6RQY5ZW"
title: "Causal reasoning in econometric models"
authors: "Kuan-Pin Lin; Arthur M Farley"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00035-q"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Causal reasoning in econometric models $^{*}$

Kuan-Pin Lin $^{a,*}$ , Arthur M. Farley $^{b}$

$^{a}$ Department of Economics, Portland State University, Portland, OR 97207, USA $^{b}$ Department of Computer and Information Science, University of Oregon, Eugene, OR 97403, USA

## Abstract

Propagation of change based on causal ordering is a central element of causal reasoning in economic models. While causal reasoning has most often been applied in qualitative models, we demonstrate a technique for causal reasoning that offers explanations of structure and behaviour in quantitative, econometric contexts. Given a matching of equations with endogenous variables, causal reasoning can be applied to both static and dynamic system models. By propagating the disturbance of one or more exogenous variables, impact or static multipliers of the model can be derived along with a causal explanation. Dynamic analysis is achieved by propagation of lagged endogenous variables carried from the previous time periods. Two versions of Keynesian macro-econometric models, Klein's Model I, and the Klein-Goldberger Model are used as examples.

Keywords: Causal reasoning; Causal ordering; Qualitative reasoning; Quantitative models

## 1. Introduction

The purpose of causal reasoning is to explain and predict phenomena based on causal notions embedded in a model. In economics, the causality among variables is represented by theoretical doctrine or statistical law. Propagating changes through cause/effect relations associated with domain knowledge is an intuitive and natural way to realize explanations and predictions of model structure and behaviour. Causal reasoning has most often been formalized and applied in the context of qualitative models of economic systems. In this paper, we demonstrate a technique for applying a form of causal reasoning to quantitative, econometric models, thereby forming a bridge between qualitative and quantitative methodologies. This technique not only computes impact multipliers, as do standard numerical solution methods, but also provide structure-based explanations of these multipliers.

Given a set of equations representing the structure of an economic system, reasoning about causal relations among variables is not a new concern. Considering a linear model represented in matrix form, an element of the matrix can be given causal interpretation, as follows: Let $a_{ij}$ be a nonzero element of matrix A associated with a pair of variables $X_{i}$ and $X_{j}$ , where i and j are the row and column index respectively. The value of $a_{ij}$ measures the impact on $X_{i}$ due to change in $X_{j}$ . Therefore, the column index indicates the cause, while the row index is the effect. If there is no direct causal relation from j to i, then $a_{ij} = 0$ . In a similar directed graph (digraph) representation, we use pointed arrow to indicate the causality: $j \rightarrow i$ or more intuitively $X_{j} \rightarrow X_{i}$ .

Recent developments in qualitative physics, a field of artificial intelligence, offer at least three approaches to reasoning about the physical world (for surveys of the subject, see $[1,16,26]$ ). They are component-based confluence analysis $[6]$ , process-based qualitative process theory $[10]$ , and constraint-based qualitative simulation $[20]$ . Causal descriptions of the basic laws of physics are given to be used as bases for explaining the behaviour of particular physical devices.

Economists have applied techniques of qualitative analysis, such as comparative statics, for a number of years [23]. The pioneering work of Simon [24] on causal ordering in economic models was a forerunner to AI theories of qualitative physics. Iwasaki and Simon [15] focused on the structural analysis of causality and formalized the concept of causal ordering of an equilibrium state. An essentially equivalent, but more intuitive, component-based approach of de Kleer and Brown [7] does not order variables in accordance with causality. Instead, the model structure is interpreted by propagating a given change through causes and effects. The technique of causal ordering is embedded in various, other approaches to qualitative physics. Modern approaches to qualitative reasoning in economics emphasizes causal explanation through propagation and simulation (see, for example, [2,4,9,11]).

This paper does not intend to redefine causality or causal ordering, but to demonstrate a technique of causal reasoning as applied to the more quantitative domain of econometric modelling. In econometric contexts, the definition of causality is not without controversy. Simon's definition of causal ordering provides a formal treatment of the syntax of causality, applicable to systems of simultaneous equations, linear or nonlinear. It describes the asymmetric relationship among variables as causes and effects. For a given equation, the static causal description is expressed in terms of dependent and independent variables of the same time period while dynamic relationships involve lagged dependent variables. Simon and Iwasaki [25] give a recent account of the subject, while the equivalent digraph representation of causal ordering provides another view of causal structure in economic models (see [13,22], and [21], for examples).

Given the causal structure of an econometric model, propagating change through causal relations in terms of brute force, depth-first or breadth-first algorithms can be inefficient. To deal with large systems having hundreds of equations and variables, the theory of causal ordering can provide an avenue for determining an acyclic, hierarchical ordering among blocks of variables. This establishes modularity for the larger model, lowering average breadth of branching. Cyclic, dense interactions only occur within modular components, reducing the overall complexity of the propagation algorithm. Propagation based on causal ordering, together with a technique for determining cyclic impacts, will be the central feature of the approach to causal reasoning in econometric models to be discussed here.

We will demonstrate that the technique of causal reasoning can offer an explanation of structure and behaviour in econometric contexts. By propagating a disturbance of one or more exogenous variables, impact or static multipliers of the model can be derived through a process driven by causal propagation. The propagation works well for static model explanation and draws similarity with the analysis of comparative statics in qualitative economics. By introducing causal relations between time periods, the dynamic behaviour of a model can be investigated. Two versions of Keynesian macro-econometric models, Klein's Model I [18] and the Klein-Goldberger Model [19], are used as examples. The next section describes the econometric model representation. Section 3 discusses the paradigm of causal reasoning in econometric contexts. Reasoning based on causal ordering is implemented and demonstrated with examples in section 4.

## 2. Econometric models

In this section, we review definitions and standard techniques of quantitative methods for dealing with linear, econometric models. In a typical econometric model, there are two kinds of equations: behaviour equations and identities. The former describes the functional relations among the variables in each equation, while the latter represents either equilibrium conditions or accounting definitions. Since a mathematical description of human or social behaviour can never be exact, behaviour equations are assumed to be stochastic or approximate. On the other hand, identities are considered to be exact. For causal reasoning purposes, the particular functional form of the behaviour equations is not essential. It is the direction of the propagation, or cause-effect relation, that is of concern. This has been the primary insight of qualitative approaches that focus on causal explanation. A nonlinear model can be approximated by its first-order form, or more specifically, the changes of variables can be expressed in derivative form from a first-order approximation.

In addition to equation specifications, we will use several classifications of variables. A variable is called endogenous if its value is determined within the system at the current time. Endogenous variables are the focus of econometric analysis and simulation; their values at any point in time are functions of the past and present values of other variables of the system. All other variables are classified as exogenous An exogenous variable may have its value determined outside the system, being an external parameter to the system, or it could have been determined in a previous time period, being a so-called lagged variable.

A linear (or linearized) econometric system can be written as

$$
\mathbf {Y B} + \mathbf {X A} + \mathbf {E} = \mathbf {0},\tag{1}
$$

where Y and X are the data matrices of endogenous and exogenous variables, respectively. B and A are the corresponding coefficient matrices. E is the matrix of error terms. For propagation of changes in (1), Y and X are interpreted as the changes of corresponding variables. Suppose there are n endogenous variables. For a self-contained system, there must be n equations. Following a proper normalization, all of the diagonal elements of B will be exactly -1. We note that a model is normalized if all the endogenous variables match with the left-hand-side of equations. That is, each endogenous variable must appear once as the effect or dependent variable of an equation, stochastic or identity. Normalization is typically achieved by algebraic operations such as dividing and shifting variables around the equations in the system. We now define several submatrices of interest. Let $y_{1}, y_{2}, \ldots, y_{n}$ be the column vectors of Y (i.e., $Y = [y_{1}, y_{2}, \ldots, y_{n}]$ ), and let $Y_{i}$ be the matrix Y with column $y_{i}$ deleted, i = 1, 2, ..., n. Similarly, $B = [b_{1}, b_{2}, \ldots, b_{n}]$ , and $B_{i}$ is B with $b_{i}$ deleted. Moreover, $E = [e_{1}, e_{2}, \ldots, e_{n}]$ . Therefore, for the i-th equation, we have

$$
\mathbf {y} _ {\mathrm{i}} = \mathbf {Y} _ {\mathrm{i}} \mathbf {B} _ {\mathrm{i}} + \mathbf {X A} + \mathbf {e} _ {\mathrm{i}} \mathrm{i} = 1, 2, \dots , \mathrm{n}\tag{2}
$$

Of course, $e_{i}=0$ if the i-th equation is an identity, as we assume no error in that case.

In the following, the famous Klein's Model I [18] is used for illustration. It was designed for the study of U.S. prewar (1921–41) economy. This first generation econometric model is a small Keynesian system, which serves a pedagogical purpose of illustrating causal reasoning about the basics of Keynes' General Theory. There are 6 linear equations in Klein's Model I:

$$
\mathrm{C} = \alpha_ {0} + \alpha_ {1} \mathrm{P} + \alpha_ {2} \mathrm{P} _ {- 1} + \alpha_ {3} (\mathrm{W} 1 + \mathrm{W} 2) + \epsilon_ {\mathrm{c}}\tag{3.1}
$$

$$
\mathrm{I} = \beta_ {0} + \beta_ {1} \mathrm{P} + \beta_ {2} \mathrm{P} _ {- 1} + \beta_ {3} \mathrm{K} _ {- 1} + \epsilon_ {\mathrm{I}}\tag{3.2}
$$

$$
\mathrm{W} 1 = \gamma_ {0} + \gamma_ {1} \mathbf {X} + \gamma_ {2} \mathbf {X} _ {- 1} + \gamma_ {3} \mathrm{A} + \epsilon_ {\mathrm{w}}\tag{3.3}
$$

$$
\mathrm{X} = \mathrm{C} + \mathrm{I} + \mathrm{G}\tag{3.4}
$$

$$
\mathbf {X} = \mathbf {P} + \mathbf {W 1} + \mathbf {T}\tag{3.5}
$$

$$
\mathrm{K} = \mathrm{I} + \mathrm{K} _ {- 1}\tag{3.6}
$$

The first three are stochastic behaviour equations with error terms $\epsilon_{c}$ , $\epsilon_{I}$ , and $\epsilon_{w}$ respectively. The remaining three equations are identities. The six endogenous variables are: C (consumption), P (private profits), W1 (private wage bill), I (investments), X (income of private sectors before taxes), and K (capital stock). The exogenous variables are: W2 (government wage bill), G (government non-wage spending), T (taxes), A (time trend), and the lagged variables, $P_{-1}$ , $K_{-1}$ , and $X_{-1}$ . The $\alpha s$ , $\beta s$ , and $\gamma s$ are the non-zero coefficients of the three behaviour equations, respectively.

We will interpret a behaviour equation as expressing the causes on the right-hand-side with the effect on the left-hand-side, based upon economic theory or empirical evidence. That is, as in (3.1), the wage bill $(W1 + W2)$ causes the consumption (C) to change according to the direction and magnitude of coefficient $\alpha_{3}$ . Of course, the structure expressed in this manner is not unique mathematically. For example (3.1) can be restated in terms of profits (P) instead:

$$
\mathbf {P} = \delta_ {0} + \delta_ {1} \mathbf {C} + \delta_ {2} \mathbf {P} _ {- 1} + \delta_ {3} (\mathbf {W} 1 + \mathbf {W} 2) + \epsilon_ {\mathrm{p}}\tag{3.1'}
$$

Where $\delta_0 = -\alpha_0 / \alpha_1$ , $\delta_1 = 1 / \alpha_1$ , $\delta_2 = -\alpha_2 / \alpha_1$ , $\delta_3 = -\alpha_3 / \alpha_1$ , and $\epsilon_{\mathrm{p}} = -\epsilon_{\mathrm{c}} / \alpha_{1}$ . Since the causal interpretation of consumption (C) or wage bill (W1 + W2) on profits (P) is questionable in a Keynesian system, this representation is not used in the original Klein's Model I. Even if (3.1') were theoretical plausible, the equation must be statistically verified as the reciprocal functional relationship between (3.1) and (3.1') may not hold empirically.

The specification of a behaviour equation is made to reflect the causal structure of the underlying economic theory. However, the same argument does not necessary apply to the specification of identities. Some identities may be given obvious causal implications of aggregation (total is the sum of components) or dynamic process (adjustment over time). On the other hand, balance sheet or accounting identities do not have causal meanings. In general, we can not assign the left-to-right directional relationship to variables in the identities without proper normalization of the econometric model. The typical approach is to keep the endogenous variables already appearing on the left-hand-side of behaviour equations where they are and associate the rest of the endogenous variables with left-hand-sides of identity equations. Although this result of normalization is not unique, the frequent existence of such a complete normalization has been noted [3].

Returning to the example of Klein's Model I, the endogenous variables X, P, and K were not specified as the dependent variables of behaviour equations. They must be shown on the left-hand-side of corresponding identities. Eqs. (3.4) and (3.6) are kept without modification, while (3.5) is re-written as follows:

$$
\mathbf {P} = \mathbf {X} - \mathbf {W 1} - \mathbf {T}\tag{3.5'}
$$

Now, there is a one-to-one matching of variables to equations such that every endogenous variable appears exactly once on the left-hand-side of an equation.

From this structural representation of the model, a reduced form can be derived to link exogenous and endogenous variables. In a reduced form, all the endogenous variables are on the left-hand-side of the equations and, through substitution, are made to appear on this side only. Although the reduced form has a unique representation of direct causality from exogenous (right-hand-side) variables to endogenous (left-hand-side) variables, the causal structure among endogenous variables is lost in this representation. Our model interpretation process will rely on the causal structure of the model, not the reduced form. Economists seldom reason with the reduced form directly, but accept theoretical justification and statistical experience as basis for specifying causal structure instead.

## 3. Causal reasoning

Econometric models presented as sets of linear equations can be solved by standard numerical methods. We would argue, however, that causal reasoning applied to these econometric models can provide a more direct and intuitive explanation of model structure and behaviour while providing equivalent numerical solutions. We must also be able to compute the impact multipliers as done by the numerical methods. In qualitative reasoning about econometric models, often we must assume stability and convergence, as qualitative values are insufficient to determine these properties. For a quantitative model, we propagate changes from causes to effects in an iterative manner until a prespecified threshold of convergence is reached. The only disadvantage is that the time for such causal-based propagation can be high when compared with time required by traditional methods of matrix algebra that compute the reduced form solutions directly. However, through causal reasoning, we gain an explanatory capability reflecting a model's structure.

Given an acausal, equational representation of an econometric model, we need to extract all the causal relations from the model. Based on the normalization discussed in the previous section, for each equation we simply assign a direct causal relation from each independent (right-hand-side) variable to the dependent (left-hand-side) variable. With each causal relation between a right-hand-side variable and the left-hand-side of a normalized equation, a propositional representation of the model, equivalent to a weighted digraph representation, is constructed. An element of the representation is expressed as $\mathrm{cr}(\mathrm{Y},\mathrm{X},\mathrm{C})$ , where the predicate cr stands for “causal relation”, Y is the effect or dependent variable, and X is the cause or independent variable. The argument C is the magnitude of the causal relationship from X to Y. We do not treat behaviour and identity equations differently in the cr representation. Endogenous variables must appear as the first argument of the cr predicates. Reasoning by propagation through causes and effects is thus equivalent to unifying aspects of corresponding $\mathrm{cr}(\mathrm{Y},\mathrm{X},\mathrm{C})$ propositions.

Based on the Two-Stage Least Squares parameter estimates of Klein's Model I (i.e., $\alpha s$ , $\beta s$ , and $\gamma s$ ), the causal relations representing the consumption Eq. (3.1) are given below:

$cr(c,w1,0.216).$

$$
c r (c, l a g (p, 1), 0. 8 1 0).
$$

Note that a lagged variable is expressed in terms of another predicate $\text{lag}(V,N)$ , where V is the variable name and N, N > 1, is the number of time steps involved. This is useful for modelling dynamic simulations in which lagged variables play an important role.

Similarly, the causal structure of the investment and wage Eqs. (3.2), (3.3) of Klein's Model I are translated as follows:

$$
\begin{array}{l} c r (i, p, 0. 1 5 0). \qquad c r (w 1, x, 0. 4 3 9). \\ c r (i, l a g (p, 1), 0. 6 1 6). \quad c r (w 1, l a g (x, 1), 0. 1 4 7). \\ c r (i, l a g (k, 1), - 0. 1 5 8). \quad c r (w 1, a, 0. 1 3 0). \end{array}
$$

Finally, three normalized identities describing income (3.4), profit (3.5'), and capital stock formation (3.6) are expressed as follows:

$$
\begin{array}{l l} c r (x, c, 1). & c r (p, x, 1). \quad c r (k, i, 1). \\ c r (x, i, 1). & c r (p, w 1, - 1). \quad c r (k, l a g (k, 1), 1). \\ c r (x, g, 1). & c r (p, t, - 1). \end{array}
$$

In the following, we focus on a depth-first process for causal reasoning. The idea of depth-first reasoning can be illustrated by a partial tree diagram of Klein's Model I starting from the branch X in Fig. 1.

If X changes due to some external disturbance, both P and W1 will be effected. The depth-first algorithm will start with one such effect first, say

![](/api/attachments/D6RQY5ZW/fulltext/images/7373da9867ba72df3155eead68d6298d02a1c1874f0410e6ba79115136360811.jpg)  
Fig. 1. Partial tree diagram evaluating Klein's model I.

W1, and propagate downward to C and X in sequence. The loop X->W1->C->X generates changes of the corresponding variables X, W1, and C, respectively. Now we start the loop analysis again with the change indicated for X. We continue to propagate along this loop, accumulating the changes for the variables involved each time around the cycle. This process repeats until a convergence threshold is attained. For a stable system, the accumulated changes must eventually reach an asymptotic level (i.e., the incremental changes approach 0). In qualitative reasoning based on similar structures, one must assume stability, and then need traverse the loop only once or at most twice to determine the qualitative impacts [17]. In the quantitative case considered here, a loop must be traversed until convergence is realized, indicating stability and representing total impact of loop-related influences.

After completing a particular subtree, the process returns to propagate the neighbouring branch P as done for W1 just described. Changes will be noted for all endogenous variables visited. By the same token, we continue to propagate branches below I and K. After K, the process backs up to where we first branch off at W1 to C and proceeds to propagate P at that level. This propagation process continues until all branches below it are evaluated. All propagated changes along paths or in loops are accumulated for all endogenous variables. The paradigm of depth-first reasoning allows propagation of multiple causes and can be applied to static and dynamic cases. Since all changes simply are accumulated during the reasoning process, it does not matter which variable changes first in the case of propagating changes of multiple causes.

It is important to stress that propagational stability is a prerequisite for the success of causal reasoning. This should not be confused with the concept of dynamic stability. By propagational stability we mean that the process of causal propagation must converge eventually, i.e., there must be no explosive cycles in the reasoning paths. Every cycle in the model must be self-damping if the model is to demonstrate propagational stability. In the above example as applied to Klein's Model I, the requirement of a damping loop such as X->W1->C->X implies that $|\alpha_{3}\gamma_{1}|<1$ . Similarly, we must have $|\alpha_{1}\gamma_{1}|<1$ , $|\beta_{1}\gamma_{1}|<1$ , $|\alpha_{1}|<1$ , and $|\beta_{1}|<1$ for other loops.

After the completion of causal propagation for a current time period, a dynamic simulation can be continued by incrementing the time step. All lagged variables are now instantiated with the changes carried over from the propagation of previous period(s). Changes due to each of the lagged variables are propagated exactly the same way as done in the static case above, for each time period.

## 4. Causal ordering

For a large model, the technique of causal ordering offers a method to recognize and utilize model modularity in the causal propagation process. A hierarchical order among groups of variables and equations, termed blocks or components, can be used to establish a priority in propagation and simulation. This technique takes an equational model and identifies substructures of causes and effects. A hierarchical ordering of blocks of variables can be uniquely identified, but the ordering of variables within a block can not. Propagation among variables in each block depends on the specific causal theory or statistical relationship in question, as discussed above. The advantage of applying causal ordering before propagation is two fold: limiting loop analysis to the smaller blocks reduces the complexity of the process and not all the blocks will have to be processed for every change analyzed, again reducing complexity.

Simon [24] and Iwasaki and Simon [15] consider a n-variable, n-equation system to be self-contained if it had the following properties: (1) for any subset of k equations $(k \leq n)$ there must be at least k different variables with non-zero coefficients; (2) for any subset of k equations with m different variables $(k \leq m \leq n)$ of non-zero coefficients, if the values of the remaining m-k variables are chosen arbitrarily, the equations can be solved for unique values of k variables. The first is the identification property which ensures that no part of the structure is over-determined.

The second is the independence requirement that guarantees equations are not mutually dependent. An econometric model for which our technique applies must be a self-contained system.

## 4.1. Minimal complete subsets

It is not difficult to find a subset of equations which is self-contained but does not itself include a self-contained proper subset. This subset of equations is called a minimal complete subset. The idea of determining a causal ordering in a self-contained system is to find minimal complete subsets of different orders in sequence. The strategy is to solve variables in the first minimal subset and to substitute or propagate the solutions to that in the next higher order. One repeats this process until no further search for minimal subsets is possible. Among different orders of minimal complete subsets, the value of variables in a minimal subset depends on those variables appearing in lower order subsets. Variables in the former are said to be causally dependent on the elements in the latter. Causal ordering depends upon the ordering of minimal complete subsets of a system. However, variables belonging to the same minimal subset are not ordered structurally.

This concept of causal ordering has been implemented and employed in various qualitative formulations, including as basis for constructing signed digraphs of a system $[12]$ and for diagnosing problems or determining causes of unexpected changes of an economic system $[17]$ .

In the following, we base causal ordering analysis on the $\mathrm{cr}(\mathrm{Y},\mathrm{X},\mathrm{C})$ representation. First, we collect all propositions specifying the model and determine a classification of the exogenous and endogenous variables. We denote such collections as EX and EN, respectively. Let $O = EX - EN$ and $A = EN - EX$ . The set O contains those exogenous variables which must be determined outside the system in the current time period. The set A is the endogenous variables that must be determined after all other variables have been solved.

We now eliminate O from EX, and call the result M; that is, $M = EX - O$ . We recursively apply the classification process above for variables now in M: Collect the new EN and EX from M, and construct a new O = EX - EN. If O is not empty, then variables in O must be independently determined at this level of the system. Repeat the same decomposition process until O is empty. Finally, re-define M = EX - A. No further decomposition is possible. Clearly, at this point, M consists of a nucleus of interacting variables in the system. Variables in M must be reasoned about simultaneously with joint determination of the whole system or several subsystems.

## 4.2. Maximal elementary circuits

Since we are searching for interdependent or feedback relationships among endogenous variables, the concept of cycles must be introduced. We are interested in finding the maximal elementary circuits for each variable in M. Here, an elementary circuit is defined to be a non-repeating cycle in causal relations. The maximal elementary circuit corresponds closely to the concept of strong component in the theory of directed graphs. Every element in a strong component is linked, either directly or indirectly, with all other elements forming the block. After finding the maximal elementary circuits for each variable in M, we take the union of all non-disjoint, maximal, elementary circuits to form blocks in M.

More formally, for each variable V in M, the maximal elementary circuit is

$$
\mathbf {C} (\mathbf {V}) = \bigcup_ {k} \mathbf {C} ^ {k} (\mathbf {V})
$$

where $\mathbf{C}^{\mathrm{k}}(\mathrm{V})$ is the k-th elementary circuit of V. Now, a block is constructed by taking the union of non-disjoint maximal elementary circuits over all variables. That is, for the i-th block,

$$
\mathbf {B} ^ {i} = \bigcup_ {\mathrm{V}} \mathbf {C} (\mathrm{V}), \text { whenever } \bigcap_ {\mathrm{V}} \mathbf {C} (\mathrm{V}) \neq 0.
$$

The block decomposition of M is thus defined as $M = \{B^{1}, B^{2}, ..., B^{m}\}$ with m < k, where k is the number of variables in M. According to Simon, there exists a unique, acyclic ordering of these blocks in M. Therefore, the remaining step of causal ordering is to establish this hierarchy. Given a causal relation $\text{cr}(Y, X, C)$ and X in $B^{i}$ , if

![](/api/attachments/D6RQY5ZW/fulltext/images/6cebeec9c75890f7e55143e18e4244e70cb28b6b71c3e76f142a2895490805af.jpg)  
Fig. 2. Causal ordering of Klein's model I.

Y in $B^{j}$ ( $i \neq j$ ) then $B^{i}$ precedes $B^{j}$ . In other words, variables in $B^{i}$ are ordered lower than those in $B^{j}$ . This process establishes the hierarchical ranking of blocks, but variables in a particular block are not ordered.

## 4.3. Examples

By applying causal ordering to Klein's Model I, Fig. 2 shows the ordering of three hierarchical levels: all exogenous variables that act individually are at the top; five endogenous variables (C, I, W1, X, P) belong to a non-decomposable block (shadow) in the middle; and one trailing endogenous variable (K) occurs in the final block.

Now we show the technique whereby we employ the causal ordering determined above to compute econometric multipliers while determining causal explanations in terms of propagations within and between blocks of variables. By combining the information from causal ordering with the pairwise causal relations, we extend our rep-

![](/api/attachments/D6RQY5ZW/fulltext/images/47c6d893d49173b68e0908b6fa1b28afe704c10b91619e6b62381a3c6418199c.jpg)  
Fig. 3. Partial trace of analysis for Klein's model I.

Table 1

presentation of the predicate cr(Y,X,C,From,To). The arguments From and To are the identifiers of source and target blocks, respectively. In other words, From indicates the hierarchical level of variable X, and To is the level of Y. These new arguments of the cr predicate are determined automatically by the causal ordering process described in the previous section. If related variables appear in the same block, they will have the same From and To identifiers. In general, To ≥ From, where To > From indicates the variables are from different blocks in the causal ordering.

The following is the modified cr database for Klein's Model I:

```prolog
cr(i,p,0.150,1,1).
cr(c,w2,0.216,0,1). cr(i,lag(p,1),0.616,0,1).
cr(c,lag(p,1),0.810,0,1).
cr(i,lag(k,1),-0.158,0,1).
cr(w1,x,0.439,1,1). cr(x,c,1,1,1).
cr(w1,lag(x,1),0.147,0,1). cr(x,i,1,1,1).
cr(w1,a,0.130,0,1). cr(x,g,1,0,1).
cr(p,x,1,1,1). cr(k,i,1,1,2).
cr(p,w1,-1,1,1). cr(k,lag(k,1),1,0,2).
cr(p,t,-1,0,1).
```

With the aid of causal ordering, we now can propagate changes within blocks and according to an acyclic path of blocks. Evaluation of interdependent variables within a block is performed by our depth-first, loop process described earlier. Propagating from a lower level variable to those of higher levels in the causal ordering is a simple one-step process, while propagating through causes and effects within a block involves the loop accumulation process described earlier. Starting from perturbation of an exogenous variable, the flow of reasoning is controlled by the causal ordering. In some situations, an exhaustive propagation is not necessary. In others, focus is maintained on subproblems before consideration of subsequent impacts. For example, the propagation within the 5-variable block (C, I, W1, X, P) of Klein's Model I must converge before updating the variable K at the next level. Variable K is not given partial updates which must be accumulated, but is only considered once, after the block processing has been completed.

Impact and interim multipliers of Klein's model I: Unit increase of government non-wage expenditure

<table><tr><td rowspan="2">Endogenous variable</td><td colspan="6">Time period</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>X</td><td>1.815</td><td>1.801</td><td>1.182</td><td>0.445</td><td>-0.188</td><td>-0.610</td></tr><tr><td>W1</td><td>0.797</td><td>1.061</td><td>0.782</td><td>0.369</td><td>-0.017</td><td>-0.296</td></tr><tr><td>C</td><td>0.663</td><td>1.084</td><td>0.796</td><td>0.385</td><td>-0.001</td><td>-0.281</td></tr><tr><td>P</td><td>1.018</td><td>0.743</td><td>0.400</td><td>0.075</td><td>-0.171</td><td>-0.314</td></tr><tr><td>I</td><td>0.153</td><td>0.709</td><td>0.383</td><td>0.062</td><td>-0.185</td><td>-0.328</td></tr><tr><td>K</td><td>0.153</td><td>0.862</td><td>1.244</td><td>1.307</td><td>1.122</td><td>0.794</td></tr></table>

Fig. 3 shows the initial part of the trace of incremental changes (i.e., predicate change1) generated by our causal propagation algorithm for Klein's Model I, while Table 1 presents summary results of this quantitative causal reasoning about one unit increase in government non-wage expenditure G.

In Table 2 and Table 3 we present similar analyses for a change in business taxes T and for combined changes in both G and T (i.e., balanced budget policy) for up to five time periods. Similar explanations are generated in these cases. The propagation convergence criteria is set to a tolerance level of 0.001. The computed multipliers are close to those obtained from the matrix solution method, except for some rounding and approximation errors.

Impact and interim multipliers of Klein's model I: Unit increase of business taxes

<table><tr><td rowspan="2">Endogenous variable</td><td colspan="6">Time period</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>X</td><td>-0.302</td><td>-1.753</td><td>-1.429</td><td>-0.626</td><td>0.143</td><td>0.693</td></tr><tr><td>W1</td><td>-0.133</td><td>-0.814</td><td>-0.888</td><td>-0.482</td><td>-0.029</td><td>0.325</td></tr><tr><td>C</td><td>-0.127</td><td>-0.919</td><td>-0.926</td><td>-0.511</td><td>-0.052</td><td>0.305</td></tr><tr><td>P</td><td>-1.162</td><td>-0.945</td><td>-0.540</td><td>-0.144</td><td>0.173</td><td>0.369</td></tr><tr><td>I</td><td>-0.174</td><td>-0.824</td><td>-0.507</td><td>-0.118</td><td>0.192</td><td>0.385</td></tr><tr><td>K</td><td>-0.174</td><td>-0.998</td><td>-1.505</td><td>-1.623</td><td>-1.431</td><td>-1.046</td></tr></table>

Table 3  
Impact and interim multipliers of Klein's model I: Unit increase of government non-wage expenditure and business tax

<table><tr><td rowspan="2">Endogenous variable</td><td colspan="6">Time period</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>X</td><td>1.520</td><td>0.045</td><td>-0.252</td><td>-0.191</td><td>-0.046</td><td>0.085</td></tr><tr><td>W1</td><td>0.667</td><td>0.242</td><td>-0.104</td><td>-0.121</td><td>-0.049</td><td>0.031</td></tr><tr><td>C</td><td>0.538</td><td>0.162</td><td>-0.127</td><td>-0.131</td><td>-0.054</td><td>0.026</td></tr><tr><td>P</td><td>-0.147</td><td>-0.198</td><td>-0.148</td><td>-0.070</td><td>0.002</td><td>0.054</td></tr><tr><td>I</td><td>-0.022</td><td>-0.116</td><td>-0.123</td><td>-0.061</td><td>0.008</td><td>-0.059</td></tr><tr><td>K</td><td>-0.022</td><td>-0.138</td><td>-0.261</td><td>-0.322</td><td>-0.314</td><td>-0.255</td></tr></table>

This demonstrates that reasoning from the causal structure of Klein's Model I as specified in terms of a simultaneous equation model (3) produces results consistent with traditional numerical techniques for quantitative models.

To demonstrate our technique of causal reasoning on a moderate size model, we considered the 20-equation Klein-Goldberger Model [19]. For notational description of the Klein-Goldberger Model, see [[14], p. 5,6]. As shown in Fig. 4, the main block of the Klein-Goldberger Model consists of 14 variables, located at level 2 in the causal ordering. Beside this main block and predetermined variables at the initial level 0, there are 3 variables (short-term interest rate IS, long-term interest rate IL, investment I) ordered as a group at level 1. At the final level, household liquid assets L1, business liquid assets L2, and corporate surplus SB are determined. In fact, money market variables IS, IL, L1, L2 can be broken off from the system, while investment I links into the main block. Based on the causal ordering of the Klein-Goldberger Model, static and dynamic propagations of one unit increase of government non-wage expenditure G were computed by our causal propagation method and found to be close to those reported in Goldberger [[14], p.87].

![](/api/attachments/D6RQY5ZW/fulltext/images/d4ac72027318db3bb4c7479d12c4a803bd84802ba851ab554fac96355fa38067.jpg)  
Fig. 4. Causal ordering of Klein-Goldberger model.

## 5. Conclusions

By combining the technique of causal propagation with causal ordering, this paper presents a working implementation of causal reasoning for econometric models. With the examples of small and medium size Keynesian models, we demonstrate the technique of quantitative causal reasoning in both static and dynamic multiplier simulations.

The utility of causal reasoning in econometric models is not simply to compute quantitative multipliers accurately. Rather it is to amplify numeric results with causal analysis of system structure. Furthermore, causal reasoning as discussed here can be modified to reason correctly even with incomplete or imperfect information. The paradigm of propagation with causal ordering as described in this paper can be either quantitative or qualitative. Indeed the concept of causal ordering is qualitative and reasoning can be based on symbolic description of the state changes. If the precise quantitative information is not available, reasoning based on the causal structure of the model can be performed at lesser granularity using interval or order of magnitude mathematics.

This paper sets out a framework for mixing aspects of quantitative and qualitative reasoning in causal economic models. Causal reasoning in qualitative models is useful for understanding the structure and behaviour of large models without precise quantitative description. Extending this reasoning to quantitative models adds precision to the more qualitative results of standard causal analysis. Future research can focus on model explanation, including aggregation of impacts due to component loops of a model, and economic diagnosis leading to the development of AI approach to econometric-based analysis.

## References

[1] D.G. Bobrow (ed), Qualitative Reasoning about Physical Systems, MIT Press, Cambridge, MA (1985).

[2] R. Berndsen and H. Daniels, Qualitative Dynamics and Causality in a Keynesian Model, Journal of Economic Dynamic and Control 14 (1985) 435–450.

[3] R. Berndsen, Qualitative Reasoning and Knowledge representation in Economic Models, Ph.D. Dissertation, University of Tilburg, The Netherlands (1992).

[4] P. Bourgine and O. Raiman, Economics as Reasoning on a Qualitative Model, Proceedings of the First International Conference on Economics and Artificial Intelligence, Aix-en-Provence, France, (September 1986) 185–189.

[5] W.F. Clocksin and C.S. Mellish, Programming in Prolog, 2nd ed., Springer-Verlag, New York (1984).

[6] J. de Kleer and J.S. Brown, A Qualitative Physics Based on Confluences, Artificial Intelligence 24 (1984) 7–83.

[7] J. de Kleer and J.S. Brown, Theories of Causal Ordering, Artificial Intelligence 29 (1986) 33–61.

[8] A.M. Farley, Qualitative Modelling of Economic Systems, Proceedings of the First International Conference on Economics and Artificial Intelligence, Aix-en-Provence, France, (September 1986) 61–64.

[9] A.M. Farley and K.-P. Lin, Qualitative Reasoning in Economics, Journal of Economic Dynamic and Control 14 (1990) 465–490.

[10] K.D. Forbus, Qualitative Process Theory, Artificial Intelligence 24 (1984) 85–168.

[11] G. Gianotti, G., Causality and Consistency in Economic Models, Computer Science in Economics and Management 4, 135–149.

[12] M. Gilli, CAUSOR: A Program for the Analysis of Recursive and Interdependent Causal Structures, Cahiers du Department d'Econometrie 84.03, Universite de Geneve (1984).

[13] M. Gilli, Causal Ordering and Beyond, International Economic Review 33 (1992) 957–971.

[14] A.S. Goldberger, Impact Multipliers and Dynamic Properties of the Klein-Goldberger Model, North-Holland, Amsterdam (1959).

[15] Y. Iwasaki and H.A. Simon, Causality in Device Behaviour, Artificial Intelligence 29 (1986) 3–32.

[16] Y. Iwasaki, Qualitative Physics, The Handbook of Artificial Intelligence, Ch. XXI, Vol. IV, ed. by Avron Barr, Paul R. Cohen, and Edward A. Feigenbaum, Addison-Wesley Publishing Co. (1989) 324–413.

[17] G. Karakoulas, Model-Based Diagnosis of an Economy, Proceedings of the Second International Conference on Economics and Artificial Intelligence, Paris, France (1990) 139–144.

[18] R.L. Klein, Economic Fluctuations in the United States, 1921–1941, John Wiley, New York (1950).

[19] R.L. Klein and A.S. Goldberger, An Econometric Model of the United States, 1929–1952, North-Holland, Amsterdam (1955).

[20] B. Kuipers, Qualitative Simulation, Artificial Intelligence 29 (1986) 289–338.

[21] J. Quirk, Qualitative Stability of Matrices and Economic Theory: A Survey Article, Computer-Assisted Analysis and Model Simplification, ed. by H. Greenberg and J. Maybee (1981) 113–164, Academic Press, New York.

[22] G. Ritschard, Computable Qualitative Comparative Static Techniques, Econometrica 51 (1983) 1145–1168.

[23] P.A. Samuelson, Foundations of Economic Analysis, Harvard University Press, Cambridge, MA (1947).

[24] H.A. Simon, Causal Ordering and Identifiability, in Hood and Koopmans, eds., Studies in Econometric Methods, Cowles Commission research 14, John Wiley and Sons, New York (1953) 49–74.

[25] H.A. Simon and Y. Iwasaki, Causal Ordering, Comparative Statistic, and Near Decomposability Journal of Econometrics 39 (1988) 149–173.

[26] D.S. Weld and J. de Kleer (ed), Readings in Qualitative Reasoning about Physical Systems, Morgan Kaumann, San Mateo, CA (1990).

Kuan-Pin Lin is the Professor of Economics at Portland State University, and Arthur M. Farley is the Professor of Computer and Information Science at the University of Oregon. Since 1986 both authors have worked on several projects on AI applications in economics and management, qualitative reasoning in particular.
