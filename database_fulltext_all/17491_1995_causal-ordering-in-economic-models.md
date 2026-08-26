---
otero_id: 17491
otero_key: "XHX4NEFN"
title: "Causal ordering in economic models"
authors: "Ron Berndsen"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00034-p"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Causal ordering in economic models

Ron Berndsen

Monetary and Economic Policy Department, The Netherlands Bank, P.O. Box 98, 1000 AB Amsterdam The Netherlands

## Abstract

In this paper, a framework is introduced in which economic models can be represented in a graphical way using causal ordering. This framework unifies the existing approaches of causal ordering in the literature. On the basis of locally imposed directions of causality (derived from the underlying economic theory) global causal dependencies can be derived for the whole model. The result is a graphical representation of the causal dependencies of the model, called a signed causal-ordering graph. On the basis of a small example taken from the area of public finance, it is pointed out what kind of conclusions can be drawn from the signed causal-ordering graph. The conclusions of this kind of qualitative analysis can be viewed as a hypothesis which requires subsequent empirical analysis in order to see if the hypothesis can be rejected.

Keywords: Causal ordering; Qualitative modelling; Qualitative reasoning; Economics; Explanation; Causality

## 1. Introduction

Explanations about particular economic phenomena or predictions of future economic developments are often formulated in causal terms (e.g. “A caused B”). Even if the results are obtained from a quantitative model, the accompanying verbal description employs causal dependencies to “exhibit the story”. Although it is by no means necessary to communicate the results of a simulation by using causal statements, such results are more easily understood and accepted if the corresponding text is presented in a causal form. Furthermore, in order to preserve the information in the translation from the economic content of a model (quantitative or qualitative) to a causal explanation, it is important to obtain a formal representation of the causal dependencies in the model.

In the 1950's, Simon (1953) developed a theory called causal ordering which can be used to identify causal dependencies in the model. The causal ordering of a model can graphically be represented by a graph in which the nodes correspond to the variables in the model and the links denote causal relationships. A path from variable $A$ to $B$ implies that $B$ is causally dependent on $A$ .

In more recent years, several researchers proposed extensions of Simon's theory and alternative approaches to causal ordering. In Iwasaki (1988) Simon's theory is extended to include dynamic models. Gilli (1984) developed a program called CAUSOR which can determine the causal ordering of both static and dynamic models. De Kleer and Brown (1986) developed a way of solving qualitative models such that the order in which the variables are solved, reflects the causal dependencies in the model. However, it is shown that for a certain class of models all causal ordering approaches are equivalent in a sense defined below (Berndsen, 1992).

The goal of causal ordering is twofold. Firstly, it can be used to clarify causal dependencies in the model. This may improve the understanding of the “working” of the model and may increase the confidence in the results obtained from it. Especially if the model is large (e.g. 500 relations), it is difficult to keep track of the interdependent relationships in the model. Secondly, it may serve as a tool for building qualitative models as a first approximation of the problem at hand. Prior to econometric analysis (and quantitative data collection), causal ordering can be used to verify if the working of the qualitative model is not inconsistent with the underlying economic theory, i.e. is the model qualitatively plausible. As such, the result of applying causal ordering to a model can be viewed as the creation of a hypothesis. Subsequent econometric analysis may then be employed to see if the hypothesis can be rejected.

The plan of the paper is as follows. In section 2, a brief overview of the three theories of causal ordering will be presented. In addition, it will be shown in which sense the theories can be considered as equivalent. In section 3, a simple framework will be introduced in which the core of the theories of causal ordering can be represented in a canonical form. In section 4, a small qualitative model will be employed in order to illustrate the use of causal ordering in the model building process. The model is used to assess how budgetary policy can be used to raise economic activity. In section 5, conclusions and directions for future research are presented.

## 2. Theories of causal ordering

## 2.1. Simon's causal ordering

Originally, the theory of causal ordering (Simon, 1953) was developed to deal with static economic models with the following properties:

(1) The model is self-contained, i.e., it consists of $n$ relations and $n$ unknown variables;

(2) in every subset of $k$ relations ( $0 \leq k \leq n$ ) of the model at least $k$ different variables appear with non-zero coefficient;

(3) in every subset of k relations $(0 \leq k \leq n)$ in which m different variables appear $(k \leq m \leq n)$ , the relations can be solved for unique values of k variables if the values of the remaining $(m-k)$ variables are chosen arbitrarily.

Following Porté et al. (1988), models which satisfy these conditions are called non-degenerated. In the context of purely qualitative models, the only information available is the incidence matrix, and therefore, we must assume rather than verify that the model is non-degenerated.

Given a non-degenerated model $F$ with expressions $f_{\mathrm{i}}(x_1,\dots,x_n)$ , the causal ordering procedure of Simon can be described as follows. Let $M_0$ denote the incidence matrix associated with $F$ where the rows of $M_0$ correspond to relations and columns correspond to variables. Element $m_{\mathrm{ij}} = 1$ if variable $x_{\mathrm{j}}$ appears in relation $f_{\mathrm{i}}$ ; otherwise $m_{\mathrm{ij}} = 0$ . The causal ordering is derived by identifying so-called minimal complete subsets (MCS). A subset of $k$ relations is complete if it contains exactly $k$ different variables. A complete subset is minimal if it contains no proper complete subset. The set of MCS's derived from the initial incidence matrix $M_0$ , is called the set of minimal complete subsets of zero order ( $\mathrm{MCS}_0$ ). Suppose that the union of the elements of $\mathrm{MCS}_0$ consists of $k$ variables ( $0 < k \leq n$ ) then the incidence matrix $M_1$ is obtained from $M_0$ by deleting the corresponding $k$ rows and columns of $M_0$ . In the terminology of Iwasaki and Simon (1986), $M_1$ is called the derived structure of first order. The MCS's of order $m$ ( $m \geq 1$ ) are determined by inspecting the incidence matrix $M_m$ . The search for MCS's terminates if the incidence matrix has no rows and columns left.

A minimal complete subset A is said to be of order k if $A \in MCS_{k}$ . Every variable of relation $f_{i}$ belongs to some minimal complete subset of order k denoted by $MCS_{k}$ . Let $MCS^{*}$ denote the MCS of the highest order in $f_{i}$ . Suppose, A and B are two MCS's and at least one variable of each MCS appears in relation $f_{i}$ . Then we define the relation B is directly causally dependent on A, denoted by $A \rightarrow B$ , iff $B = MCS^{*}$ and $A \neq MCS^{*}$ . The interpretation of the relation $A \rightarrow B$ is that changes in the variable(s) belonging to A are the direct cause of changes in the variable(s) belonging to B. From the definition of $A \rightarrow B$ it follows that variables belonging to the same MCS are not ordered.

Iwasaki (1988) extended the original method of causal ordering to deal with models consisting of static and dynamic relations. Such models, called mixed models, can be obtained from a static model by replacing one or more static relations with their dynamic counterparts, or from a dynamic model by replacing dynamic relations with corresponding static relations. In this paper we focus on economic effects in the long term which implies that the lag structure need not be specified. Therefore, in the rest of this paper only static models will be considered.

## 2.2. Mythical causality

Mythical causality is a method of causal ordering developed by De Kleer and Brown (1986). Mythical Causality derives a causal ordering which is used to provide causal explanations of qualitative behaviour. In this section, the emphasis is on how to solve a set of qualitative relations, called confluences, in accordance with some notion of causality. The determination of a solution of the set of confluences is a constraint satisfaction problem (CSP). Here, we describe the local propagation algorithm used in De Kleer and Brown (1984). The purpose of the algorithm is to assign a value from $\{+,0,-\}$ to each variable such that all confluences are satisfied. A variable v is free if it is not assigned a value; otherwise, v is said to be determined. Basically, the local propagation algorithm consists of three steps:

(1) Select a confluence c of arity n with exactly one free variable x, i.e. n-1 variables in c are determined.

(2) Assign a value to $x$ which satisfies $c$ .

(3) Propagate the value of $x$ to other confluences in which $x$ appears.

The propagation process stops at step 1, if there is no confluence of arity n with exactly one free variable. If all variables are determined, the algorithm terminates successfully. Otherwise, one of the free variables must be selected and assigned a value. To guide this choice, three heuristics are proposed in De Kleer and Brown (1984). The application of the heuristics is necessary if there is a “feedback loop” in the model which implies that some of the variables are interdependent. The choices suggested by the heuristics do not always lead to a solution. In that case, the algorithm stops at step 2 and backtracking occurs to the last variable for which a choice was made on the basis of the heuristics and another value is tried. To obtain a notion of causal ordering in the constraint satisfaction process, De Kleer and Brown introduce the concept of “mythical time”. Starting in an equilibrium state, i.e., a situation in which the quasi-static model is valid, one of the external parameters is perturbed marking the starting point of mythical time. At the end point of mythical time, the static model is valid again. In between, the model goes through a sequence of non-equilibrium states caused by the perturbation. Hence, the mythical time span is the time necessary to reach the situation in which the quasi-static model is valid again. This time span is called mythical because in intra-state behaviour or, equivalently, in comparative statics, there is no real notion of time; the transition from one equilibrium state to the next occurs instantaneously. The order in mythical time in which the variables are assigned a value represents the mythical causality in the model. The ultimate cause is the disturbed external parameter.

Often, the set of confluences allows multiple solutions leading to multiple causal accounts of intra-state behaviour. However, even a unique solution is no guarantee for a unique mythical causal explanation.

## 2.3. CAUSOR

In this section, we discuss some of the techniques for analysing causal structures as implemented in the program CAUSOR (Gilli, 1984). The techniques apply to both static and dynamic models. The discussion is limited to the techniques used for static models. In the case of dynamic models, the causal structure may be obtained by repeating the procedure for static models n times where n is the order of the model (temporal aggregation of the results yields the causal structure of the model for the long term).

In this approach, a static model is comprised of n relations consisting of n endogenous variables y and m exogenous variables z:

$$
h (y, z) = 0.\tag{1}
$$

It is assumed that there is a matching W of variables to relations such that every endogenous variable appears exactly once on the left-hand side of a relation. In Berndsen (1992), it is proved that such a matching exists in the case of non-de-generated static models. So, (1) can be written explicitly as

$$
y _ {i} = g _ {i} (y, z) \quad (i = 1, \dots , n)\tag{2}
$$

The causal structure of (2) is derived automatically by the program in two steps. First, a directed graph $G = (X, E)$ is constructed from (2) as follows: X is the set of nodes representing the set of endogenous and exogenous variables. E is the set of directed links; there is a link from $x_{i}$ to $x_{j}$ iff $x_{i}$ appears on the right-hand side of the relation in which $x_{j}$ is the left-hand variable. Secondly, G is partitioned into its strong components. A strong component (also called block) S of a digraph G is a maximal subgraph in which each pair of nodes is mutually reachable.

In Garbeli and Gilli (1984), it is argued that the block structure of economic models usually consists of only a few blocks containing a large number of variables. This is confirmed in the case of three Dutch econometric models, each consisting of more than 200 equations. The causal structure of these models consists of only 1 or 2 blocks (see Houtman and Sterken, 1989). Therefore, the importance of analysing the interior structure of a block seems evident. To this end, CAUSOR offers a technique to obtain a hierarchical ordering of the variables within a block.

The basic idea is to identify all variables which are essential for the interdependency of the block. The feedback vertex set or essential set is defined as the set of variables which appear in every cycle of the block. A minimal feedback vertex set or minimal essential set is defined as the feedback vertex set with minimal cardinality. The minimal essential set can be employed to transform the block into a directed acyclic graph (DAG). The procedure to derive this DAG can be found in Gilli (1984). The DAG represents the causal structure among variables of the same block. A node in the DAG is said to be causally dependent upon its predecessors.

2.4. The equivalence of the theories of causal ordering

In Berndsen (1992) it is proved that the aforementioned three theories of causal ordering are equivalent for the class of non-degenerated static models with respect to the minimal complete subsets (or strong components) in the model. The three theories of causal ordering all produce the same, and unique, causal dependencies between strong components. The three theories are different with respect to the direction of the links within strong components. In Simon's approach no direction is specified within a strong component which limits its use because usually an economic model consists of only 1 or 2 strong components (see e.g. Garbeli and Gilli, 1984).

In the theory of De Kleer and Brown (1986), the direction of links in strong components is derived on the basis of a set of heuristics. However, the general nature of these heuristics allows multiple solutions and hence multiple causal orderings for one and the same model. In CAU-SOR, the direction of causality within strong components is derived on the basis of minimal essential sets. In this case too, multiple solutions are possible because in general the number of minimal essential sets is greater than 1. Furthermore, the causal ordering within a strong component is derived on the basis of a graph-theoretic criterion instead of an economic criterion.

In the framework presented in the next section, the causal ordering within strong components is determined on the basis of a matching from variables to relations. The underlying idea is that each relation in the model determines exactly one variable. This corresponds to the practice in economic model building of writing one variable on the left-hand side of the equation. In a causal interpretation of that equation, the variables on the right-hand side are said to cause changes in the variable on the left-hand side. In formalising this practice, we impose a direction of causality on the model at the level of the individual relation. The added value of applying causal ordering to the model lies in identifying causal dependencies between variables which appear in different relations. In so doing, it is possible to clarify the causal dependencies in a model with interdependent variables.

## 3. A general framework for causal ordering

In this section, we present a framework in which economic models can be represented graphically by so-called model graphs. The causal ordering of a model is represented by a causal-ordering graph. The process of deriving the causal-ordering graph from the model graph is described below. In section 4, a detailed example is presented to illustrate the notions introduced below.

## 3.1. Graph representation of economic models

Before presenting the definition of the model graph M, we introduce some notation. Let V denote a set of m economic variables $\{v_{1},\ldots,v_{m}\}$ . Let R denote a set of economic relations $\{r_{1},\ldots,r_{n}\}$ . Each relation $r_{i}$ is represented by a k-tuple containing k elements of V: $(v_{j},\ldots,v_{j+k-1})$ . Relation $r_{i}$ is said to contain k economic variables. If $r_{i}$ contains a variable $v_{j}$ then $v_{j}$ is said to appear in $r_{i}$ . Then, the model graph M can be defined as follows:

Definition 1. (Model graph). The model graph is a bipartite graph $M = (V \cup R, A)$ where the node set consists of the union of the economic variables and the economic relations. The arc set $A$ is defined by $\{(v_i, r_j) \in A | v_i \text{ appears in } r_j\}$ .

The model graph M is a graphical representation of the information indicating which variable appears in which equation. It is assumed that the model is self-contained (the number of variables equals the number of relations). However, in case the model is under-determined, i.e. the number of relations n is less than the number of variables m, it is generally straightforward to transform the model into a self-contained model by adding m-n relations, each containing a single variable. The interpretation is that the variable appearing in such a relation is an exogenous variable. Graph M contains the minimal information needed to derive the causal ordering between strong components.

In order to derive the causal ordering within strong components, it is assumed that there is a matching W from variables to relations such that every variable matches exactly one relation (perfect matching). The matching indicates the direction of causality at the level of the individual relation, as argued in section 2.4.

In addition, the sign of economic effects may be incorporated (at the level of the individual relation). From the standpoint of causal ordering, this information is not necessary. However, using that information it is possible to determine the consequences of a change in one of the exogenous variables. This will be illustrated in section 4.

## 3.2. Derivation of the causal ordering graph $C$

In this section, we describe the procedure to derive the causal-ordering graph C. Given the model graph $M = (V \cup R, A)$ and the perfect matching W, the causal ordering procedure can be described in the following three steps:

(1) Direct every arc $(v_{\mathrm{j}}, r_{\mathrm{i}}) \in W$ from $r_{\mathrm{i}}$ to $v_{\mathrm{j}}$ ;

(2) Direct every arc $(v_{\mathrm{j}}, r_{\mathrm{i}}) \in (A - W)$ from $v_{\mathrm{j}}$ to $r_{\mathrm{i}}$

(3) Contract all nodes $r_i \in R$ ;

The graph which remains after step 3 is defined by

Definition 2. (Causal-ordering graph). The causal-ordering graph is the directed graph $C = (V, A')$ where the node set consists of the economic variables $V$ . The arc set $A'$ is obtained from $A$ by the three-step procedure described above.

The interpretation of a link $(v_{1}, v_{2}) \in A'$ is that $v_{2}$ is directly causally dependent on $v_{1}$ . A path in C from $v_{1}$ to $v_{2}$ , $(v_{1}, v_{2}) \notin A'$ , indicates that $v_{2}$ is indirectly causally dependent on $v_{1}$ . In addition, graph C can be transformed into a signed causal ordering graph by labelling each directed link $(v_{i}, v_{j})$ with a plus-sign if an increase in $v_{i}$ results in an increase in $v_{j}$ or a minus-sign if an increase in $v_{i}$ results in a decrease of $v_{j}$ .

## 4. Example: a simple model for budgetary policy analysis

## 4.1. The model

In this section, it is shown what information can be obtained from the (signed) causal-ordering graph C. To this end, we present a qualitative analysis of budgetary policy using a small closed-economy model. This model will be employed to determine the best alternative for reducing the deficit given the two instruments available: the tax rate and autonomous government expenditure. The set of variables V and equations R of the model is given in Table 1.

The model graph M is depicted in Fig. 1. The second part needed in order to derive graph C is the perfect matching W which is shown in Table 2.

The underlying reasons for choosing the particular matching shown in Table 2 can be split in three categories. The first category is comprised of definitions. In definitional relations, the direction of causality imposed is from the other variables to the variable which is defined in that relation. For example, relation $r_{1}$ is the definition of the government deficit. Therefore, causality runs from expenditures (broken down in two components IP and G) and receipts (T) to the deficit (D). The second category consists of so-called institutional relations. One example of an institutional arrangement is the way of financing the unemployment benefits (relation $r_{8}$ ). In this model, the amount of social security payments is determined on the basis of the unemployment rate. The third group contains the behavioural relations. In these relations, the direction of causality is derived from underlying economic theory. Usually, the naming convention of such relations, i.e. “Consumption function”, indicates the proper direction of causality. Given the types of the relations, it is possible to compute a perfect matching of relations to variables.

The model  
Table 1

<table><tr><td>Set of variables V</td><td>Set of relations R</td></tr><tr><td>BR Borrowing Requirement</td><td> $r_1$  (D, IP, G, T)</td></tr><tr><td>CB Collective Burden</td><td> $r_2$  (BR, D)</td></tr><tr><td>D Deficit (government)</td><td> $r_3$  (r1, BR)</td></tr><tr><td>EA Economic Activity</td><td> $r_4$  (IP, BR, r1)</td></tr><tr><td>G Government expenditure</td><td> $r_5$  (EA, T, t)</td></tr><tr><td>IP Interest Payments</td><td> $r_6$  (EA, G, CB, r1)</td></tr><tr><td>r1 Long-term interest rate</td><td> $r_7$  (U, EA)</td></tr><tr><td>SSP Social Security Payments</td><td> $r_8$  (U, SSP)</td></tr><tr><td>T Taxes</td><td> $r_9$  (CB, T, SSP)</td></tr><tr><td>t Tax rate</td><td> $r_{10}$  (G)</td></tr><tr><td>U Unemployment</td><td> $r_{11}$  (t)</td></tr></table>

![](/api/attachments/XHX4NEFN/fulltext/images/e169761003335922360f1f9633c330a18ec920fec14e4f0fe63b8a82c368b6bb.jpg)  
Fig. 1. Model graph.

Table 2  
Perfect matching

<table><tr><td>Relation—variable</td><td>Type</td></tr><tr><td> $r_1-D$ </td><td>definition</td></tr><tr><td> $r_2-BR$ </td><td>institutional relation</td></tr><tr><td> $r_3-r1$ </td><td>behavioural relation</td></tr><tr><td> $r_4-IP$ </td><td>definition</td></tr><tr><td> $r_5-T$ </td><td>definition</td></tr><tr><td> $r_6-EA$ </td><td>behavioural relation</td></tr><tr><td> $r_7-U$ </td><td>behavioural relation</td></tr><tr><td> $r_8-SSP$ </td><td>technical relation</td></tr><tr><td> $r_9-CB$ </td><td>definition</td></tr><tr><td> $r_{10}-G$ </td><td>definition</td></tr><tr><td> $r_{11}-t$ </td><td>definition</td></tr></table>

![](/api/attachments/XHX4NEFN/fulltext/images/4483d32a3a1393ed37db2bb819c2748f4d46f1c95438559543541229714a39c1.jpg)  
Fig. 2. Modified model graph (step 1).

Given graph M (Fig. 1) and perfect matching W (Table 2), the causal-ordering graph C can be derived by the procedure presented in subsection 3.2. In Figs. 2, 3 and 4, the result of applying the three steps of the causal ordering procedure is shown (in Figs. 2 and 3, each link of the perfect matching is shown as a bold arrow). The signed causal ordering graph depicted in Fig. 5, is obtained from the causal ordering graph (Fig. 4) by labelling the links with the appropriate signs derived from the underlying economic theory.

![](/api/attachments/XHX4NEFN/fulltext/images/20c26a39d2d79b5b5f52f29ab41ddc7849770105a4f2631a978c4a69f6e19444.jpg)  
Fig. 3. Modified model graph (step 2).

![](/api/attachments/XHX4NEFN/fulltext/images/820ea1769d450ec72d1b4e43d21ad1832c52e7f84cce96f7fde45222f9d35167.jpg)  
Fig. 4. Causal ordering graph.

## 4.2. Reading the signed causal ordering graph

In general, the information which can be obtained from a signed causal ordering graph falls into two categories:

(1) identification of amplifying cycles (positive feedback) and counteracting cycles (negative feedback).

(2) the sign of the long-run effect(s) on an endogenous variable as a result of a change in one or more exogenous variables.

In the following, an increase respectively decrease of variable x is denoted by $x \uparrow$ respectively $x \downarrow$ and “y is causally dependent on x” is denoted by $x \rightarrow y$ . As stated above, the problem at hand is to assess what kind of budgetary policy is needed to raise economic activity ( $EA \uparrow$ ). Some conclusions which can be obtained from the signed causal-ordering graph by applying basic graph-algorithms for path-identification and cycle-detection, (for computational details see e.g. Harary et al. (1965) and Berge (1973)) are as follows:

![](/api/attachments/XHX4NEFN/fulltext/images/7b39ae9de88a434950a1ecc93cc32b1c0b3813ee3658c7a73f7c73ed0998c409.jpg)  
Fig. 5. Signed causal ordering graph.

(1) A rise in the budget-deficit is potentially harmful because of the amplifying cycle (positive feedback-loop) in the model $D \uparrow \rightarrow BR \uparrow \rightarrow rl \uparrow \rightarrow IP \uparrow \rightarrow D \uparrow$ . On the other hand, a cut in the deficit may lead to further reductions in the deficit because of lower interest payments;

(2) The deficit can be cut either by raising the tax rate $(t\uparrow \rightarrow T\uparrow \rightarrow D\downarrow)$ or by decreasing autonomous government expenditure $(G\downarrow \rightarrow D\downarrow)$ ;

(3) A raise of the tax rate will only cause a rise in economic activity if the effect of a lower interest rate $(t \uparrow \rightarrow T \uparrow \rightarrow D \downarrow \rightarrow BR \downarrow \rightarrow rl \downarrow \rightarrow EA \uparrow)$ outweighs the effect of a higher collective burden $(t \uparrow \rightarrow T \uparrow \rightarrow CB \uparrow \rightarrow EA \downarrow)$ ;

(4) A cut in autonomous government expenditure will lead to higher economic activity if the indirect effect via lower interest rates $(G \downarrow \rightarrow D \downarrow \rightarrow BR \downarrow \rightarrow rl \downarrow \rightarrow EA \uparrow)$ is greater than the direct effect $(G \downarrow \rightarrow EA \downarrow)$ ;

These conclusions are intrinsically useful to illustrate the underlying economic theory. By reading the signed causal ordering graph as shown above, the underlying economic mechanisms are disclosed. However, the long-term effects are ambiguous, so they depend on the quantitative value of the implicitly assumed coefficients. The results of this qualitative analysis could serve as input for subsequent econometric analysis.

## 5. Conclusions

In this paper, a framework is introduced in which economic models can be represented in a graphical way. On the basis of locally imposed directions of causality (derived from the underlying economic theory) global causal dependencies can be derived for the whole model. The result is a graphical representation of the causal dependencies of the model, called a signed causal-ordering graph. On the basis of a small example, it is pointed out what kind of conclusions can be drawn from the signed causal-ordering graph. The goals of causal ordering are to clarify the “working of the model” by laying out the causal dependencies of the model and to provide a formal tool for qualitative model-building as a first approximation to subsequent quantitative modelling. As such, the conclusions of the qualitative analysis can be viewed as a hypothesis requiring empirical analysis in order to see if the hypothesis can be rejected.

However, the analysis presented in this paper is only a first step towards the creation of a practical tool for qualitative modelling. Future research should be aimed at providing a firm theoretical underpinning of the procedures pointed out in section 4. In addition, further work should include a full implementation of the algorithms and procedures described in this paper such that a larger part of the modelling process can be carried out in a formal and automated way.

## 6. For further reading

Boutillier (1984), Gilli (1979) and Karakoulas (1991).

## References

Berge, C., Graphs and Hypergraphs, North-Holland, Amsterdam (1973).

Berndsen, R., Qualitative Reasoning and Knowledge Representation in Economic Models, Ph.D. Thesis, University of Tilburg, Tilburg (1992).

Boutillier, M., Reading Macroeconomic Models and Building Causal Structures in: J. Ancot (ed.) Analysing the Structure of Econometric Models, Martinus Nijhoff Publishers, The Hague (1984).

De Kleer, J. and J. Brown, A Qualitative Physics Based on Confluences, Artificial Intelligence, vol. 24 (1984) pp. 7–83.

De Kleer, J. and J. Brown, Theories of Causal Ordering, Artificial Intelligence, vol. 29 (1986) pp. 33–62.

Garbeli, M. and M. Gilli, Two Approaches in Reading Model Interdependencies in: J. Ancot (ed.) Analysing the Structure of Econometric Models, Martinus Nijhoff Publishers, The Hague (1984).

Gilli, M., Etude et Analyse des Structures Causales dans les Modeles Economiques, Peter Lang, Bern (1979).

Gilli, M., CAUSOR: A Program for the Analysis of Recursive and Interdependent Causal Structures, Universite de Geneve, Cahiers du Département d'Econometrie no. 84.03 (1984).

Harary, F., R. Norman and D. Cartwright, Structural Models: An Introduction to the Theory of Directed Graphs, John Wiley and Sons, New York (1965).

Houtman, M. and E. Sterken, The Structure of Macroeconomic Models, Proceedings of the IFAC Symposium Dynamic Modelling and Control of National Economies, Edinburgh (1989) pp. 629–634.

Iwasaki, Y. and H. Simon, Causality in Device Behaviour, Artificial Intelligence, vol 29 (1986) pp. 3–32.

Iwasaki, Y., Causal Ordering in a Mixed Structure, Proceedings of the Seventh National Conference on Artificial Intelligence (AAAI-88), St Paul, Minnesota (1988) pp. 313–318.

Karakoulas, G., Model-Based Diagnosis of an Economy in: P. Bourgine and B. Walliser (eds.) Economics and Cognitive Science, Pergamon Press, Oxford (1991).

Porté, N., S. Boucheron, J. Sallantin and F. Arlabosse, An

Algorithmic View at Causal Ordering, Centre de Recherche en Informatique de Montpellier, Technical Report No. 45 (1988).

Simon, H., Causal Ordering and Identifiability, W. Hood and T. Koopmans (eds.), Studies in Econometric Method, Cowles Commission for Research in Economics, no. 14, Wiley and Sons, New York (1953) pp. 49–74.

![](/api/attachments/XHX4NEFN/fulltext/images/0e8aa959db7d66883362ef4a02b8cfcd1531e2908c0ee3c9b65d78616fc90cb5.jpg)  
Ron Berndsen is a staff member of the Monetary and Economic Policy Department of the Netherlands Bank. He has a doctorate in Economics from Tilburg University.
