---
otero_id: 17671
otero_key: "U4HVGQ2A"
title: "MCView: An integrated graphical system to support multi-attribute decisions"
authors: "Rodolf Vetschera"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90081-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# MCView: An integrated graphical system to support multi-attribute decisions

Rudolf Vetschera

University of Konstanz, D-W-7750 Konstanz, Germany

The paper presents a DSS for multi-attribute decision problems called MCView. The system combines a process-oriented view of multi-attribute decision making with a comprehensive, graphical user interface. The decision process supported by MCView is based on a two-level representation of evolving preferences, which allows the user to interactively introduce preference information both in the form of holistic choices between alternatives and by directly changing the parameters of a cardinal evaluation method. The graphical user interface of MCView provides comprehensive information about and direct manipulation of all problem components and thus directly supports this learning process.

Keywords: Multi-attribute decision making; Graphical user interface; Preference representation

![](/api/attachments/U4HVGQ2A/fulltext/images/503a71a0b98e5168aa5ee75af147fa005ef8eab69259fac18995c99216f53a42.jpg)

Rudolf Vetschera is a professor of management at the University of Konstanz, Germany. He holds a PhD in Economics and Computer Science from the University of Vienna, Austria. He has published in Decision Support Systems, European Journal of Operational Research, Computers and Operations Research and various other journals. His current research interests are in the development of interaction techniques for decision support systems, group decision support systems, and information systems.

port and the evaluation of information systems.

Correspondence to: Rudolf Vetschera, Faculty of Economic and Statistics, University of Konstanz, P.O. Box 5560, D-W-7750 Konstanz, Germany.

## 1. Introduction

Graphical user interfaces (GUIs) are rapidly becoming an important factor in the design of decision support systems. GUIs allow the user immediate access to and direct manipulation of all relevant elements of the problem at hand. This fact makes them especially attractive in the highly interactive environment usually associated with DSS.

Complex decision problems involve a multitude of different objects such as decision alternatives, criteria and preference information, which the user (the decision maker) needs to obtain and manipulate. A comprehensive graphical user interface can significantly simplify this interaction. In this paper, we present an experimental support system for multi-attribute decision problems called MCView, which is based on a graphical representation of the decision problem integrating all relevant components.

The paper is structured as follows: in section two we provide an overview of the generic decision process to be supported by MCView. Section three presents the underlying theoretical developments and the models incorporated in MCView. The system itself is described in section four, mainly from the user's point of view. Section five concludes the paper with an outlook onto further developments.

## 2. Preference representation and decision process

Following the current development in interactive approaches to multi-criteria decision support [20], the concept of learning is a central element in the decision process supported by MCView. In multi-objective problems, where alternatives are only implicitly given through constraints on decision variables, the learning aspect is often related to exploring the set of feasible outcomes [11]. In the case of given, discrete alternatives, for which MCView was developed, this information is already available. Here, learning mainly concerns the user's preferences. The system aids the user in formulating his/her preferences, in finding out the consequences of preference statements and finally, in applying this preference structure to make a final choice among alternatives.

![](/api/attachments/U4HVGQ2A/fulltext/images/66d04f01b34762454d675fa5300a7ef0a640d0c98342476f8443fdc9b94d3bc2.jpg)  
Fig. 1. Overview of the preference representation.

The decision process supported by MCView is therefore based on the notion of an evolving preference representation, which is gradually built up and modified during the user's interaction with the system. In MCView, the preference representation is simultaneously developed at two levels: at an ordinal level, as a binary relation of preference between alternatives, and at a cardinal level, as cardinal evaluations of alternatives. Figure 1 shows the overall structure of this preference representation, as well as the functions of the systems relating to it.

At the bottom level of preference representation, the user formulates some holistic choices among alternatives, forming a binary relation between alternatives. This relation is interpreted as indicating that the user is definitely sure that he/she prefers a certain alternative to another alternative. Since such a definite preference can probably only be stated between few alternatives, the resulting binary relation will usually not be complete or transitive.

At the second level, a cardinal evaluation method is used, which is controlled by the user via parameters such as criteria weights or aspiration levels. This cardinal representation also induces an ordinal ranking of alternatives, which is complete and transitive. This ranking might contradict some of the binary choices which the user has specified at the bottom level. A consistency checking function of the system constantly monitors the two representations and informs the user whenever such contradictions occur. The second main function of the system, related to the preference representation, is the estimation function. This function allows the user to modify the cardinal preference representation in order to make it consistent with the holistic choices specified at the bottom level.

Figure 2 provides an overview of the entire decision process. It is probably easier for the user to formulate initial preference statements in the form of holistic choices, rather than by directly specifying parameters for a cardinal evaluation method such as criteria weights or aspiration levels. The first step of the decision process therefore consists in providing initial preference statements at the ordinal level. The estimation function of the system is then used to obtain a first representation at the cardinal level. It should be clearly noted that at this point, we do not want to measure the user's "true" preferences, since we expect preferences to evolve over time as the user finds out more about the consequences of his statements. On the other hand, anchoring effects [17,6,21,9] might cause the user to stay close to this initial representation. It is therefore important that the user should not specify parameter values in an arbitrary way, but that the initial cardinal representation is derived from clear choices about which the user is certain and by a methodologically sound technique. To achieve this goal, the system must convey the necessary information for making holistic choices to the user in a way which can easily be understood and processed. In MCView, a projection-based graphical approach is used for this purpose [19]. This approach is based on an extension of principal component analysis, which has been proposed by several authors to visualize multi-attribute problems [12,10].

![](/api/attachments/U4HVGQ2A/fulltext/images/7ce52fc2b28e0bbfddad43feb1df1ba97aa31c9bb996e02a3b715dd1aac2ed46.jpg)  
Fig. 2. Overview of the decision process.

Once an initial preference representation is established, the user is free to modify it as he/she finds out more about his/her preferences. The system supports this learning and discovering process in several ways. Firstly, the system provides immediate information about the ranking of alternatives induced by the current cardinal preference representation. This is also achieved by the extended projection method of MCView, which makes it possible to align alternatives on screen according to their ranks. Thus any changes which the user makes to the cardinal preference representation immediately lead to visibly detectable consequences. This feature is closely connected to the consistency checking function of the system, which points out those holistic choices contradicting the cardinal preference information.

The estimation function of the system also plays an important role during this stage of the decision process. Here it serves as a kind of sensitivity analysis tool. If the consistency checking function detects any inconsistencies between the two layers of preference representation, the estimation function can be used to find out how much the cardinal representation would need to be changed in order to reflect the holistic choices. The user can also introduce new holistic choices and apply the estimation function in order to adapt his cardinal preference representation accordingly.

Once the user is convinced that a reasonable preference representation has been established, a final choice based on that preference representation can be made.

## 3. Models

In this section, we describe the mathematical models underlying the various functions of the

MCView system. We begin with a short review of possible preference representations, then present the estimation models for them and conclude with a short review of the graphical representation methods. Throughout the remainder of the paper, we will use the following notation: There are N decision alternatives, indexed by $n = 1, \ldots, N$ , which are characterized by K criteria $k = 1, \ldots, K$ . We denote the performance of alternative n in criterion k by $x_{n,k}$ . Unless otherwise stated, we assume that the $x_{n,k}$ are scaled so that the best alternative for criterion k has a value of 1 and the worst alternative a value of 0. The entire data vector of alternative n is denoted by $X_{n} = (x_{n,1}, \ldots, x_{n,K})$ .

## 3.1. Preference representations

In the literature, several methods for representing preferences towards multiple attributes have been proposed. These methods can be classified into two main classes $[13,1,2,3,23,14]$ :

\- Methods in which preferences are represented by some weighting of criteria.

\- Methods in which preferences are represented by aspiration levels of criteria.

In McView, simple examples are used for both classes of methods. For the first class, a direct additive weighting of criteria values is provided. Here, an alternative is evaluated according to:

$$
u (X _ {n}) = \sum_ {k} w _ {k} x _ {n, k},\tag{1}
$$

where $w_{k}$ is the weight of criterion k and $\Sigma_{k}w_{k}=1$ . These weights are the parameters in the cardinal preference representation of the system. Since all $x_{n,k}$ are scaled between 0 and 1, $u(X_{n})$ will also lie in that interval.

For the second class, following [23], we use an evaluation based on the Tchebycheff distance from an aspiration vector $\overline{X} = (\overline{x_{1}}, \ldots, \overline{x_{K}})$ defined as:

$$
s (X _ {n}) = \min _ {k} \left(x _ {n, k} - \overline {{x _ {k}}}\right).\tag{2}
$$

Here, the preference representation parameters at the cardinal level correspond to the aspiration vector $\overline{X} = (\overline{x_{1}}, \ldots, \overline{x_{K}})$ .

## 3.2. Estimation

The purpose of the estimation function of the system is to find a cardinal preference representation which is as compatible as possible with the holistic preference statements made by the user at the ordinal level. If several representations (i.e. weight vectors or aspiration levels) are compatible with the holistic choice statements, the system should use a representation which is as close as possible to the representation used before.

At the ordinal level, the user makes preference statements indicating that he/she considers one alternative $X_{n}$ to be at least as good, as another alternative $X_{m}$ . The entire set of such preference statements forms a binary relation nRm. Since the user will probably only make a few such statements, relation R will usually not be complete. The system also does not enforce the transitivity of relation R. However, since both cardinal preference representations used in MCView imply transitivity, the estimation function will not be able to determine a representation at the cardinal level which is fully compatible with an intransitive relation at the ordinal level, and the user will be informed about this fact.

## 3.2.1. Estimation of weights

Several methods are available in the literature for estimating additive utility functions of the form (1) (e.g. [5,7,8,16,22]). Most of these methods also measure single criteria utility functions, which is not necessary in our context, since these functions are assumed to be strictly linear.

A common model for estimating criteria weights from discrete choices has the form:

$$
\begin{array}{l} \sum_ {m, n: m R n} d _ {m, n} = \min!, \\ \sum_ {k} w _ {k} x _ {m, k} + d _ {m, n} \geq \sum_ {k} w _ {k} x _ {n, k} \quad \forall m R n, \\ \sum_ {k} w _ {k} = 1, \end{array}\tag{3}
$$

where $d_{m,n}$ represents the amount of contradiction to an ordinal statement that alternative m is preferred to alternative n. This model, however, does not take into account the set of weights previously used at the cardinal level, if such weights already existed. If it is possible to reproduce relation R by several different sets of weights, model (3) will select some arbitrary weight vector. Due to the properties of the simplex algorithm, it is highly likely that the resulting weight vector will have an extreme structure in which several weights are zero and others are very high. This problem does not occur in the usual estimation problems, in which relation R contains many (perhaps inconsistent) choices and consequently, a unique solution exists with an objective value greater than zero.

To avoid this problem, we use a modified model in which a previous set of weights $w_{k}^{0}$ is taken into account:

$$
\begin{array}{l} M \cdot \sum_ {m, n: m R n} d _ {m, n} + \sum e _ {k} = \min!, \\ \sum_ {k} w _ {k} x _ {m, k} + d _ {m, n} \geq \sum_ {k} W _ {k} x _ {m, k} \quad \forall m R n, \\ \sum_ {k} w _ {k} = 1, \\ w _ {k} + e _ {k} \geq w _ {k} ^ {0} \quad \forall k. \end{array}\tag{4}
$$

In model (4), $e_{k}$ represents the reduction in weight $w_{k}$ as compared to the previous value. Since the scaling of all weights is maintained, it is sufficient to consider the total reduction in weights, which is equal to the total increase in other weights. By selecting a suitably large value for the constant M, priority of the quality of fit over proximity to the previous weights is enforced.

## 3.2.2. Estimation of aspiration levels

A similar approach can also be used to estimate aspiration levels for preference representation (2). Since the minimum operator used in (2) would require a mixed integer formulation leading to unacceptable solution times, a heuristic method [18] is used to estimate reference levels. This heuristic method uses an unconstrained optimization technique based on the direct search algorithm from [4] and improved by [15] to solve the following problem:

$$
\begin{array}{l} \sum_ {m, n: m R n} d _ {m, n} = \min!, \\ d _ {m, n} = \left\{ \begin{array}{l l} 0 & \text {if} s (X _ {m}) \geq s (X _ {n}) \\ s (X _ {n}) - s (X _ {m}) & \text {if} s (X _ {m}) <   s (X _ {n}) \end{array} \right. \\ \forall m R n, \\ \sum_ {k} \overline {{x _ {k}}} = \frac {K}{2}. \end{array}\tag{5}
$$

The scaling condition in model (5) is not necessary for method (2), but serves to provide a “reasonable” reference point, which also fits nicely into the graphical representation of the problem. It is taken into account by substituting

$$
\overline {{{{x _ {K}}}}} = \frac {K}{2} - \sum_ {k = 1} ^ {K - 1} \overline {{{{x _ {k}}}}}
$$

in (5), resulting in an unconstrained optimization problem, which can be solved very efficiently. Here, a previous reference point can be taken into account by using it as a starting value for the iterative optimization algorithm.

## 3.3. Graphical representation

The graphical representation of problem data used in MCView is based on the preference-preserving projection approach developed in [19]. This method projects the $[N \times K]$ data matrix

$$
X = \left[ \begin{array}{c} X _ {1} \\ \vdots \\ X _ {N} \end{array} \right]
$$

onto the two-dimensional screen by postmultiplication with a $[K \times 2]$ projection matrix T. Matrix T itself is a linear combination of two components:

$$
\boldsymbol {T} = \lambda \boldsymbol {P} + (1 - \lambda) \boldsymbol {Q}.\tag{6}
$$

Matrix P is a projection matrix derived from principal component analysis and provides as much information as possible on the criteria values of alternatives. Similar projections are also used in other graphical systems like GAIA [12] and BIPLOT [10]. This kind of display is particularly helpful to the user when making holistic choices between alternatives. A disadvantage of this projection is that information about the ranking of alternatives cannot be inferred from the graphical representation.

Matrix Q, on the other hand, is chosen so that the alternatives are aligned on screen in increasing order of preference. For the additive preference representation (1), this can be achieved by using the weight vector as one column of Q. For preference representation (2), a linear approximation is constructed. Since this leaves only one axis for the representation of criteria values, less information about the criteria values of alternatives can be inferred from this projection. By varying the projection parameter $\lambda$ , the user can select a projection which best suits his/her needs.

It is also possible to calculate indifference regions in the projection plane, in which alternatives equivalent to a given alternative $X_{n}$ are projected. For the additive preference specification (1), these regions are determined by solving the following parametric linear program:

$$
\begin{array}{l} \sum y _ {k} t _ {k, 1} + \theta \sum y _ {k} t _ {k, 2} = \max / \min!, \\ \sum y _ {k} w _ {k} = \sum x _ {n, k} w _ {k}, \\ 0 \leq y _ {k} \leq 1, \end{array}\tag{7}
$$

where $t_{k,i}$ are elements of the projection matrix $T$ and $y_k$ are variables of the linear program.

For the aspiration-based representation (2), the linear approximation used for projection is also used for the parametric program.

## 4. Implementation

The MCView system is designed to run on personal computers under the MS-DOS operating system. It is written in TopSpeed Modula-2 using the TopSpeed DOS extender to overcome the 640 KB memory limit which DOS imposes. The main focus of the system design is the development of a userfriendly graphical interface, which allows the user to control most functions of the system by direct interaction using a mouse. In this section, we will therefore present the system mainly from a user's point of view. As an example, we use data from the car selection problem presented in [12].

Screen 1 shows the main interaction screen of MCView. The screen layout follows the standard established by modern graphical user interfaces. The main part of the screen shows a graphical representation of the problem data obtained by two-dimensional projection. The attributes are presented as a system of coordinates, where the angle between coordinates corresponds to the correlation of attributes within the given data set. Each decision alternative is represented by a data point. The location of each data point, relative to the criteria axes, indicates how well the alternative performs with respect to the criteria. To enhance the legibility of the screen, different colors are used for criteria and alternatives.

![](/api/attachments/U4HVGQ2A/fulltext/images/9ae4254c5d5235b697d5d450d820f1ee87929e78349a91fe506a6c5012d84103.jpg)  
Screen 1. Data-oriented projection.

Screen 1 shows a projection which is close to the standard principal component projection ( $\lambda = 0.94$ in equation (6)), in which the criteria axes are widely dispersed and the performance in each criterion can easily be detected. The value of parameter $\lambda$ is controlled by a scroll bar at the right of the screen. By clicking on the bar with the mouse and changing the size of the bar, the user can change the value of $\lambda$ and thus the type of projection. During this change, the main screen is continuously updated, thus it is possible for the user to select a value of $\lambda$ which provides the most suitable graphical representation.

At the top of the screen is the main menu of the system, which provides access to several command menus for various functions of the system. Below the main menu, the system displays a status line. The main function of this line is to identify the object currently being pointed at by the mouse. This method of object identification was chosen to avoid overloading the graphical display with the identification of every object. However, for easy identification, it is possible for the user to attach small labels to selected objects, as shown in Screen 2.

![](/api/attachments/U4HVGQ2A/fulltext/images/74f943b59ff093245c8d7925fb2ec57723289c4300f2fc483711d68e63e38a36.jpg)  
Screen 2. Preference-oriented projection and data editing.

![](/api/attachments/U4HVGQ2A/fulltext/images/4ac1c308b015cd5380cfd5f3342f5f6d2091189e6f9f161989b022938135a1a9.jpg)  
Screen 3. Indifference region.

In Screen 2, the user has selected a projection with a low value of $\lambda = 0.06$ . This screen also shows the data editing function. This function is invoked by clicking with the mouse on the data point representing an alternative. It allows the user to change the description and data values of an alternative and to select several options for the representation of the alternative. The first option “Show Indifference Region” activates a graphical display showing the region around an alternative in which indifferent alternatives can be located. This kind of display is shown in Screen 3. Here a small value of $\lambda$ is used again, thus the indifference region is just a narrow band. The second option “Display Short Label” activates the short three-letter identification label next to the data point. Similar labels can also be attached to criteria.

![](/api/attachments/U4HVGQ2A/fulltext/images/a80c05d008a215a66d4ede0b8d1e75382a2b8e059852f3f01f13c26b8a57bc03.jpg)  
Screen 4. Reference point display.

![](/api/attachments/U4HVGQ2A/fulltext/images/f2bf4226f99546a3630941a86993f2a009d3565a2cc2ae1e08e7cb7e3b63f31f.jpg)  
Screen 5. Pairwise preference.

The criteria values of alternatives entered in the editing window shown in Screen 2 need not be normalized to the zero/one interval. This normalization is automatically performed by the system, which also takes into account whether a criterion is to be minimized or maximized.

The first two commands in the main menu, "File" and "Edit", lead to submenus containing commands for storing problems on and retrieving them from disk, and for adding or deleting alternatives and criteria. Screen 4 shows the submenu, which is activated by clicking the third item "Preference" on the main menu. Its first item allows the user to select one of the two preference representations provided at the cardinal level. If the aspiration-method is selected, the reference point $\overline{X}$ is displayed on screen as a small rectangle, also shown in Screen 4. The remaining items in this menu deal with holistic choices at the ordinal level and the interconnection between the two levels.

![](/api/attachments/U4HVGQ2A/fulltext/images/afd666357940c6095d3e61096cc35a677191feceea9858ea68afc549d0ef5836.jpg)  
Screen 6. Estimation of weights.

![](/api/attachments/U4HVGQ2A/fulltext/images/5be62acba3b28ec9e1f7dca554e43b219cacaa7c4a72508d77f1a364cc563cac.jpg)  
Screen 7. Changed weights.

Adding and removing choices can also be directly performed in the graphical representation. To indicate that alternative A is preferred to alternative B, the user first clicks on A then B. In the graphical representation, these preference statements are shown as arrows between the two alternatives concerned. For example, in Screen 5, the user has indicated to prefer alternative “Lad” to alternative “323”. Since alternative “Lad” is to the left of “323” in the projection showing preferences, this discrete choice statement contradicts the ranking implied by the current cardinal preference representation. The arrows corresponding to such contradictory choices are a different color (yellow) to those choices in accordance with the cardinal representation (and alternatives), which are green. The user can now select “Estimate” to obtain a new cardinal preference representation which is consistent with all of the ordinal choices. Since alternative “Lad” (the Lada 2105) is cheaper but less economical than alternative “323” (Mazda 323), the system now generates a weight vector in which the weight for criterion “Price” is increased and that for “Consumption 2” is decreased. The user is then given the option of accepting the new weights or keeping the old ones (Screen 6). Of course, it is also always possible to change the weights directly by means of an editing mechanism similar to that for alternatives. If the user decides to accept the new weights, the two alternatives are aligned at the same level of preference (Screen 7).

![](/api/attachments/U4HVGQ2A/fulltext/images/58557a030c0efe8134e5afa7e8d2121bbee0aece1d33828180b3127f4bc52e8e.jpg)  
Screen 8. "View" submenu.

The last item of the main menu, “View”, leads to another submenu shown in Screen 8. This submenu allows the user to control various aspects of the graphical representation, like zooming the display to full screen size or displaying pairwise choices. It is also possible to select the type of approximation used for the aspiration-based preference representation.

This intuitive and flexible interaction makes it possible for the user to understand the effects of his specifications for holistic choices and/or direct changes of the cardinal preference representation. Holistic choices are immediately classified as being in accordance with or contrary to the cardinal representation. The estimation function provides information about how much the cardinal representation would need to be changed in order to reflect the holistic choices. Furthermore, this kind of analysis is not restricted to single holistic choices between two alternatives. By specifying several holistic choices and then invoking the estimation function, these choices will be processed simultaneously.

Similarly, the system also provides immediate reactions to changes to the cardinal representation. Whenever criteria weights (or aspiration levels) are directly changed, the graphical screen display is updated to reflect the new ranking of alternatives implied by the new parameter values.

As a result of the consistency checking function, holistic choices which contradict this ranking will also be pointed out to the user.

## 5. Conclusions

In this paper we have introduced the MCView system for the graphical support of multi-attribute decision problems. This system provides an intuitive, easy to use interface allowing for direct manipulation of all aspects of such problems. In turn, this direct manipulation gives the user a better understanding of the consequences of any information about preferences which he provides the system with.

In this respect, MCView is a distinct step ahead of current multi-attribute decision support systems. At present, the learning effects which can be obtained by using such a responsive and open system can only be estimated. Experimentation with MCView will allow for additional insight into the behavioural changes induced by the system.

## References

[1] V. Chankong and Y. Haimes, Multiobjective Decision Making: Theory and Methodology, (North-Holland, New York, Amsterdam, Oxford, 1983).

[2] G.W. Evans, An Overview of Techniques for Solving Multiobjective Mathematical Programs, Management Science 30, (1984), 1268–1282.

[3] M. Gershon, The role of weights and scales in the application of multiobjective decision making, European Journal of Operational Research 15, (1984), 44–250.

[4] R. Hooke and T.A. Jeeves, "Direct Search" Solution of Numerical and Statistical Problems, Journal of the ACM 8, (1961), 212-229.

[5] G.P. Huber, Methods for Quantifying Subjective Probabilities and Multi-Attribute Utilities, Decision Sciences 5, (1974), 430–458.

[6] V.L. Huber and M.A. Neale, Effects of Cognitive Heuristics and Goals on Negotiator Performance and Subsequent Goal Setting, Organizational Behavior and Human Decision Processes 38, (1986), 342–365.

[7] E. Jacquet-Lagreze and J. Siskos, Assessing a set of additive utility functions for multicriteria decision-making, the UTA method, European Journal of Operational Research 10, (1982), 151–164.

[8] G.W. Klein, H. Moskowitz, S. Mahesh, A. Ravindran, Assessment of Multiattribute Measurable Value and Utility Functions via Mathematical Programming, Decision Sciences 16, (1985), 309–324.

[9] C.T. Kydd, Cognitive Biases in the Use of Computer-Based Decision Support Systems, Omega 17, (1989), 335–344.

[10] A. Lewandowski and J. Granat, Dynamic BIPLOT as an Interaction Interface for Aspiration-Based Decision Support Systems, in: P. Korhonen, A. Lewandowski, J. Wallenius, Eds., Multiple Criteria Decision Support, (Springer, Berlin, 1991), 229–241.

[11] A. Lewandowski and A. Wierzbicki, Decision Support Systems Using Reference Point Optimization, in: A. Lewandowski and A. Wierzbicki, Eds., Aspiration-Based Decision Support Systems, (Springer, Berlin, 1989), 3–20.

[12] B. Mareschal and J.-P. Brans, Geometrical representations for MCDA, European Journal of Operational Research 34, (1988), 69–77.

[13] B. Roy, Problems and methods with multiple objectives, Mathematical Programming 1, (1971), 239–266.

[14] W.S. Shin, and A. Ravindran, Interactive Multiple Objective Optimization: Survey I: Continuous Case, Computers and Operations Research 18, (1991), 97–114.

[15] H. Späth, Algorithm für multivariable Ausgleichsmodelle, (Oldenbourg, München, 1974).

[16] V. Srinivasan and A.D. Shocker, Estimating the Weights

for Multiple Attributes in a Composite Criterion Using Pairwise Judgements, Psychometrika 38, (1973), 473–493.

[17] A. Tversky and D. Kahneman, Judgement under Uncertainty: Heuristics and Biases, Science 185, (1974), 1124–1131.

[18] R. Vetschera, Estimating Preference Cones from Discrete Choices-Computational Techniques and Experiences, Discussion Paper I-259, Faculty of Economics and Statistics, University of Konstanz, (1992).

[19] R. Vetschera, A Preference-Preserving Projection Technique for MCDM, European Journal of Operational Research 61 (1992) 195–203.

[20] P. Vincke, Multicriteria Decision-aid. (J. Wiley & Sons, Chichester, 1992).

[21] D. von Winterfeldt, Expert Systems and Behavioral Decision Research, Decision Support Systems 4, (1988), 461–471.

[22] M. Weber, A Method of Multiattribute Decision Making with Incomplete Information, Management Science 31, (1985), 1365–1371.

[23] A.P. Wierzbicki, On the Completeness and Constructiveness of Parametric Characterizations to Vector Optimization Problems, OR Spektrum 8, (1986), 73–87.
