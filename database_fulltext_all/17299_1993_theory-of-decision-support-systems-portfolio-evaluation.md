---
otero_id: 17299
otero_key: "4CFBA5RU"
title: "Theory of decision support systems portfolio evaluation"
authors: "James R. Marsden; David E. Pingry"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90011-q"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Theory of Decision Support Systems portfolio evaluation \*

James R. Marsden

University of Kentucky, Lexington, KY, USA

David E. Pingry

University of Arizona, Tucson, AZ, USA

A theory is developed for the evaluation of Decision Support System portfolios in a for-profit firm. The critical relationship captured in this theory is between what Decision Support Systems do (increase the efficiency and effectiveness of search for structures for unstructured problems) and what they accomplish for the firm (solve unstructured problems). The resulting theory is used to develop testable hypotheses, some of which are counterintuitive. For example, we suggest that increasing the effectiveness of a DSS should lower its use, but increasing the efficiency of DSS should increase its use. A solution technique for finding a profit maximizing portfolio of Decision Support Systems is proposed. The solution technique is used to solve an example problem, which illustrates the important relationship between scope and scale in the evaluation of Decision Support Systems.

Keywords: Decision Support Systems, DSS evaluation, DSS theory, Information systems

Although there is still debate over the role of Decision Support Systems (DSS) for organizational and individual decision-making (see [9,21,24], there is wide support for the definition of DSS proposed by Sprague [38]: “interactive computer based systems, which help decision makers utilize data and models to solve unstructured problems.” Experience with DSS over the past 20 years has led researchers to propose a number of frameworks in order to isolate the important factors in successful DSS design, e.g., [3,6,11,14,15,18,19,26,38]. Other researchers have concentrated on observing the impacts of DSS usage in empirical and experimental environments, e.g., [4,8,13,17,20,25,37].

## 1. Introduction

![](/api/attachments/4CFBA5RU/fulltext/images/a1eed2030308e46c6d6d8a8a0ac7e42c35a035af4c4647418f6c13a7487614aa.jpg)

While heuristic design frameworks and empirical observation are very useful, they should be viewed as necessary precursors to the development of a formal DSS design theory. Formal theory can tightly link the design factors isolated in the frameworks and observations to allow for precise formulation and testing of hypotheses. The purpose of this paper is to begin the task of developing formal theory and testable hypotheses which can be used for ex-ante evaluation of DSS [10].

James R. Marsden is the Phillip Morris Professor and Chair, Department of Decision Science and Information Systems, and Professor of Economics at the University of Kentucky. Professor Marsden has held visiting positions at the University of North Carolina, Purdue University, University of York (England), and the University of Arizona. Dr. Marsden's research interests include DSS, expert system modeling of microeconomic markets, and management of information.

The problem we deal with is goal driven selection of an optimal DSS portfolio. While the appropriate goal differs across settings, we selected a for-profit firm to illustrate our approach. We assume that the set of DSS to be evaluated either exists in the market place or could be built internally by the firm. That is, the technical problems of building the DSS (model management, data base management, user interface, etc.) are assumed to have been solved and the cost of the best system, given a particular objective, is known. The design or portfolio selection problem, from our point of view, is that the firm must decide what unstructured problems to assign to an automated DSS, what unstructured problems to do manually, and what unstructured problems to ignore (i.e., problems whose solution costs exceed solution benefits). The problem is how to exploit the DSS technology for the benefit of the firm. This is not to undervalue the importance of research in the design of these components, but rather represents a conscious decision to concentrate on building a model which can be used to evaluate that technology. An appropriate analogy might be operations management experts who are interested in the problem of utilizing robots on the factory floor, but not in designing better robots.

![](/api/attachments/4CFBA5RU/fulltext/images/e26ca0519aa35ca073520eb820d62720106381c5235b16d247b09574119cabbf.jpg)  
David E. Pingry is Professor of Management Information Systems and Professor of Economics at the University of Arizona. He previously was on the faculty at Virginia Polytechnic Institute and held visiting positions at Purdue University and at Texas A&M University. Dr. Pingry's research interests include DSS, management of information, and economics of information systems.

We present a framework which isolates the variables for making the portfolio decision, a theory which is based on that framework, and a solution technique to solve specific design evaluation problem occurrences. An example design evaluation problem is also presented. The framework is a modification and distillation of those frameworks which have struggled with the notion of unstructured problems. The theory borrows freely from traditional decision theory and uses standard optimization techniques.

Our approach to DSS design in a for-profit firm is based on the following observations:

(i) The profit-maximizing firm faces three types of problems: (1) Currently structured problems (for which a decision to structure was already made and implemented); (2) currently unstructured problems (which may or may not be worth structuring); and (3) fundamentally unstructured problems (where optimal or satisficing decision-making can have no predictively useful role).

(ii) The role of a computerized DSS in a profit-maximizing environment is to improve the efficiency and/or effectiveness of the search for appropriate structures for currently unstructured problems.

(iii) The for-profit firm seeks to select the profit-maximizing portfolio of DSS.

(iv) The DSS portfolio selection problem has been an unstructured problem.

In this paper we structure the DSS portfolio selection problem. In Section 2 we present our design framework which defines and discusses types of problem unstructure and relates them to the choice set available to the DSS designer. In Section 3 we integrate the design framework principles into the context of the profit-maximizing firm. In Section 4 we present a theory of DSS portfolio selection in a basic case where the choice is whether to do a decision task with a manual or computerized DSS. This model is used to explore in detail the roles of 'efficiency' and 'effectiveness'. A variety of testable hypotheses are generated. In Section 5 this basic model serves as a building block for our general model. An example problem is solved and examined using sensitivity analysis. Summary and conclusions are presented in Section 6.

## 2. DSS evaluation framework

We begin by operationally defining two key concepts: (1) What it means for a problem to be unstructured; and (2) what it means to solve an unstructured problem [27]. Sorting problems into structured and unstructured classes is an issue that firms must address in order to evaluate their DSS options correctly. Frequently, discussions of unstructured problems suggest that problems are intrinsically unstructured or structured. Our position is that there are problems which have been structured and problems that have not been, or cannot be, structured by the decision maker. An unstructured problem is solved by finding an appropriate structure, if one exists, for modelling the problem (i.e., moving the problem from the unstructured to the structured category). Gorry and Scott Morton [11] noted: “...the evolutionary nature of the line separating structured from unstructured decisions. This line is moving down over time as we improve our understanding of a particular decision”.

They implicitly assume, however, that all decision-makers would agree on where the line separating the problems should be drawn. We argue that whether a problem is structured or unstructured is itself a decision problem facing individual decision-makers. Moore and Chang [33] also made the point that it only makes sense to speak of structured and unstructured problems with regard to a particular decision maker. Landry et al. [24] discussed the fact that different decision makers can have a different view of the same problem. The resolution of these differences in an organization is appropriately in the domain of the study of group decision processes and Group Decision Support Systems (GDSS). We will assume that the decision-maker is an individual or a group in which agreement has been reached.

We are ‘solving’ the currently unstructured DSS design evaluation problem by structuring it using the classical decision theory paradigm. The components of the standard decision theory paradigm include states, actions, and goal(s). In the implemented decision model, these components translate into constraints (parameters and relationships), variables, and an objective function (utility, profit, etc.). In order for a decision model to be useful, it must be solvable. A necessary, but not sufficient, condition for a decision model to be solvable is that there exist mappings from action–state combinations to goals (a specific linear programming model provides a common example of a structured decision model). Further, if the solution is to be utilized, the individual and organization must be satisfied with the decision model, that is, it must be acceptable as adequately representing the problem.

The above discussion leads us to the definition we will use for the term structured problem:

Definition 1. If a problem can be adequately represented by a decision model which is solvable, then we will say that the problem is structured.

The natural corresponding definition for an unstructured problem is:

Definition 2. Any problem which does not satisfy the definition of a structured problem is an unstructured problem.

To understand the potential usefulness of DSS, it is necessary to get a very clear understanding of ‘unstructured problem’ and the conditions of ‘adequately represent’ and ‘solvable.’ It follows from our discussion of decision models and the definition of unstructure that there are three sources of unstructure: (1) The states, actions, goals and/or the mappings between the states, actions, and/or goals are uncertain; (2) the adequately represent condition is violated; and/or (3) the solvability condition is violated. We consider each of these sources of unstructure in turn.

## Uncertainty in states, actions, goals or mappings

The uncertainty in states, actions, goals or mappings can come from two sources. First, the decision maker may lack rudimentary knowledge about the problem space. We call this fundamental unstructure (Knight [22] used the term “uncertainty”). Second, the appropriate decision model could be stochastic, that is, the states or mappings may be realizations of random processes. We call this stochastic unstructure (Knight [22] used the term “risk”).

## Inadequacy of representation

Inadequacy of representation refers to a judgement by the individual or organizational user. Such judgments might be based simply on the user's beliefs or perceptions [24] or on the results of fitting and validating models with, in the most rigorous cases, model validation based on scientific methods. We call this representation unstructure.

## Insolvability of model

We use the term solvability unstructure to refer to situations when the model can be formulated but not solved. Solvability unstructure can exist because of algorithmic limitations in dealing with the mathematical structure (e.g. nonlinearities and large numbers of variables) of the selected model. Following Simon [36], we call this category of solvability unstructure complexity unstructure (see Appendix A for a detailed discussion of the relationship of our approach to the view of problem solving introduced by Simon). It may also be the case that the decision-maker lacks needed knowledge about the numerical values of one or more of the model's parameters. For example, a corporate planner may have a detailed, accurate and technically solvable model of inventory control, but lack either direct information on parameter values or the data necessary to accurately estimate these values. We call this category of solvability unstructure information unstructure.

Although we have divided the sources of unstructure into five categories (including the two types of uncertainty unstructure and the two types of solvability unstructure) for purpose of analysis, the boundaries between these categories are somewhat fuzzy. For example, formulating a model which does not adequately represent a problem could be an indication that the mappings are uncertain. Also, consider that it is possible to write a solvable linear programming model of almost any problem, but these models will most likely not adequately represent the large majority of real world problems. On the other hand, it is possible to write non-linear programming models which adequately represent a large number of real world problems, but which cannot be solved given current software or hardware capabilities.

The strategy choices available to a decision-maker when faced with an unstructured problem, while not easy to implement, are straightforward to consider. The decision-maker must search for a solvable decision model which adequately represents the problem as currently formulated. Table 1 summarizes the decision-makers choice set when faced with each possible type of unstructure. For example, in the case of information unstructure, the YES in the first column indicates that a change in model is a possible choice. However, the NO in the second column indicates that solving the current model is not possible (given the current information). Thus, in this case the decision-maker can only deal with the unstructure by acquiring adequate information to support the current model or by modifying the model to one for which he has the appropriate information. This is a common dilemma for the modeler and researcher.

Available choices of different sources of unstructure.

<table><tr><td rowspan="2">Source of unstructure</td><td colspan="2">Choices</td></tr><tr><td>Change in structure</td><td>Solve</td></tr><tr><td>1. Fundamental</td><td>No</td><td>No</td></tr><tr><td>2. Stochastic</td><td>Yes</td><td>Yes</td></tr><tr><td>3. Representation</td><td>Yes</td><td> $No^a$ </td></tr><tr><td>4. Complexity</td><td>Yes</td><td>No</td></tr><tr><td>5. Information</td><td>Yes</td><td>No</td></tr></table>

$^{a}$ The decision-maker could decide to solve a model which did not adequately represent a problem. However, this would mean incurring costs for no identifiable benefits.

A perusal of table 1 reveals three problem categories of particular interest. First, in the case of fundamental uncertainty, there is no way to deal with the underlying unstructure given the state of knowledge. These problems await some breakthrough in basic research or are simply not capable of being structured.

Second, in the cases of information unstructure, complexity unstructure, and representation unstructure, the choice open to the decision-maker involves either: (1) Changing the model of the problem (given the information, solution techniques, and standards of representation); or (2) acquiring information, developing solution techniques, and/or altering standards of representation (each with their special costs).

The third case, that of stochastic unstructure, is the only case which presents the decision-maker with the possibility of solving the current model. Stochastic models can be solved (e.g., select the action that maximizes expected value) even though they do have uncertain mappings between states, actions and goal(s). In the other four cases of unstructure it is not possible (given the information, solution algorithms, and degree of acceptability of the structure) to pick a 'best' action without modifying the model. In fact, decision consultants often structure a decision problem by working with decision-makers to estimate probabilities of events, thus enabling 'best' action to be determined.

With these observations in mind, we argue that for a DSS to deal with unstructured problems it must assist in the search for solvable decision models. Any other proposed role of DSS ignores the basic observation that unstructured problems cannot be solved in a way that is useful (i.e., cannot be tied to an objective), unless the problem is structured using a decision model. This is also true for the DSS portfolio evaluation problem. For ease of exposition we consider only one of many possible firm goals, profit maximization. In many firm situations other goals will be dominant and the decision problem would be modified accordingly.

## 3. DSS portfolio choice framework

In the profit-maximizing firm, the issue with respect to DSS is the same as with any potential input into the firm's production process—how can the firm utilize the input in a way consistent with the firm's goal of profit-maximization? For each occurrence of an unstructured problem, the firm would like to develop an optimal strategy to select a model (or structure), $s_{i}$ , for that problem such that the necessary mappings exist, the structure is solvable, and the structure adequately represents the problem. Formally, this problem can be written as follows:

$$
\text { Maximize } \pi (s _ {i}) = \operatorname{Revenue} (s _ {i}) - \operatorname{Cost} (s _ {i}),\tag{1}
$$

$$
s _ {i} \in S ^ {M}, \quad s _ {i} \in S ^ {S}, \quad s _ {i} \in S ^ {R},
$$

where $\pi$ is the profit from utilizing structure $s_{i}$ , $S^{M}$ is the set of all structures for which the necessary mappings exist, $S^{S}$ is the set of all structures that are solvable, and $S^{R}$ is the set of all structures that adequately represent the problem according to the decision-maker's criteria. The Revenue function is the benefit from solving the unstructured problem with structure $s_{i}$ . The Cost function is the cost of searching for, obtaining the data for, and solving structure $s_{i}$ . We would anticipate tradeoffs common to such optimization problems. For example, the cost function incorporates information and solution costs which typically increase with complexity and information requirements. In addition, we would expect that both the revenue generated from solving the problem structure and the adequacy of representation of the model to be increasing functions of model complexity.

If finding the best model were costless (i.e., if the search were free), the firm could simply scan the structure space and select the structure which yielded the most revenue (net of data and solution costs). No decision support would be necessary. However, the fact is that searching for structure costs resources. Thus, the following observations can immediately be made using the formulation of the decision support evaluation problem in (1):

(i) The profit-maximizing structure will not necessarily be the revenue maximizing structure;

(ii) increased profitability can be obtained by lowering the cost or increasing the revenue per search iteration.

These observations lead us to the following definition of decision support systems in a profit-maximizing firm:

## Definition 3. Decision Support Systems

Manual procedures or computerized systems which have as their objective to decrease the cost of searching for and solving a structure or to increase the effectiveness of searching for and solving a structure for an unstructured problem.

In practice, computerized decision support is accomplished using three primary components: (1) A model base; (2) a data base; and (3) a language for user interface. The model base contains the potential structures, the data base contains the problem related data, and the user language allows the user to select specific structures and associated data for evaluation. The development of the computerized model-data-user interface has been the primary contribution of DSS. These languages have lowered the costs of considering alternative structures.

The major DSS portfolio selection issues at our level of concern are driven by what we call the ‘scope’ and the ‘scale’ of the DSS. The concepts of economies of scale and scope are commonly used terms in economics (a detailed discussion of the relationship of scale and scope can be found in [7]). A DSS is wider in scope if it can deal with a larger number of problem areas with a larger number of possible structure types. For example, a DSS with the widest scope would be one which includes all of the possible models (or solution algorithms), all of the possible supporting data, and a user interface which can deal with any problem-structure/solution algorithm combination (the terms ‘flexibility’ and ‘adaptability’ instead of scope are ‘often used in the DSS literature). Since DSS with such wide scope are not observed, DSS designers have apparently thought it more efficient to design DSS with relatively narrow problem and structure scope. The savings from a narrower scope occur due to one or more of the following:

(i) The search for structure can be over a smaller, homogeneous structure space;

(ii) the model and data storage can be reduced; and

(iii) the user languages can be simplified.

As the structure scope is reduced, the risk is that 'good' structures may be eliminated from the model base. As the problem scope is reduced, the risk that a problem occurrence cannot be handled is incurred. The DSS with the narrowest scope would be one which could only consider a single problem with a single model. In this case search costs would be zero. One such example would be the most basic operations research/management science type of model. In our framework, operations research techniques are used to model the DSS evaluation problem. The DSS, in turn, can search for operations research/management science techniques to 'solve' other unstructured problems.

The scale of the DSS refers to the expected number of problem occurrences that a DSS will deal with. As we will show later, the scale is critical in determining whether or not to computerize a DSS. To justify the computerization of a DSS, the expected number of problem occurrences in the problem space must be large enough to capture sufficient benefit increases and/or cost decreases to cover the development costs.

Using the above discussion, we define the DSS portfolio choice problem as follows:

Definition 4. DSS Portfolio Selection Problem
The DSS portfolio selection problem for a profit-maximizing firm is to select the set of DSS which maximizes profits given an expected number of unstructured problem occurrences of different types.

One might argue that the problem types and number of occurrences faced by firms are unknown and, therefore, that the DSS design evaluation problem itself has fundamental unstructure. Casual observation of implemented DSS suggest, however, that firms often must have a good idea about what problem types are likely to occur and the approximate frequency with which they are likely to occur. Further, firms spend considerable money on gathering information about problems and expected problem occurrences. It is no accident that financial planning packages are widely used. Firms know that they frequently face problems where present value calculations are critical, but where the time patterns of cost and revenue of each individual project may be very different and not known in advance.

Firms also spend a great deal of resources evaluating problem-solving employees, people who can be viewed as manual DSS. The curriculums of MBA programs describe the scope of a manual DSS [30].

Before proceeding, we note that the literature distinguishes between a DSS generator and a DSS. For example, Sprague [38] defines a DSS generator as “a ‘package’ of related hardware and software which provides a set of capabilities to quickly and easily build a specific DSS”. Both DSS portfolio selection and DSS generator portfolio selection can be evaluated using the approach proposed here.

## 4. A basic DSS selection model

Our approach to the DSS selection problem presumes that both structure and problem spaces can be partitioned into a finite number of ‘equivalence classes.’ That is, there are problems which are enough alike that they can be approached with a similar solution strategy. Examples include inventory control, production planning, cash management, project management, and financial analysis. Structures, on the other hand, can be partitioned into model categories such as regression, linear programming, integer programming, and simulation.

Our basic model considers whether to computerize a DSS when the problem type $(P_{k})$ is given and the structure space $(S_{l})$ , which contains structures which may adequately represent these problems, is well known. That is, the scope of the DSS is assumed to be given and fixed. This allows us to isolate the critical relationship between what DSS do (reduce model search costs or improve model search effectiveness) and what DSS accomplish for the firm (handle unstructured problems more profitably).

Using the notation described in table 2 (with subscripts deleted for clarity since there is only one DSS), we formalize the basic problem as follows [29].

$$
\begin{array}{l} \underset {x ^ {c}, x ^ {m}, \delta} {\text { maximize }} \quad x ^ {c} \big \{o _ {i} \big [ R - (1 / (\Phi^ {c} \cdot \delta)) - \delta \cdot C ^ {c} \big ] - D ^ {c} \big \} \\ \qquad + x ^ {m} \big \{o _ {i} \big [ R - (1 / (\Phi^ {m} \cdot \delta)) - \delta \cdot C ^ {m} \big ] \big \}, \\ \text { subject   to } \quad x ^ {c} + x ^ {m} \leqslant 1, \end{array}\tag{2}
$$

where $x^{c} = 0, 1$ and $x^{m} = 0, 1$ . The options the firm must evaluate, as represented in this mathematical programming formulation are:

Table 2
Model notation.

<table><tr><td> $p_{i}$ </td><td>A specific problem.</td></tr><tr><td> $s_{j}$ </td><td>A specific structure.</td></tr><tr><td> $I$ </td><td>The set of the problem indices.</td></tr><tr><td> $J$ </td><td>The set of the structure indices.</td></tr><tr><td> $P$ </td><td>The set of all problems,  $P = \{p_{i} \mid i \in I\}$ .</td></tr><tr><td> $S$ </td><td>The set of all structures,  $S = \{s_{j} \mid j \in J\}$ .</td></tr><tr><td> $\alpha(P)$ </td><td>A partition of  $P$  into  $M$  ‘equivalence classes’ or problem types.</td></tr><tr><td> $\beta(S)$ </td><td>A partition of  $S$  into  $N$  ‘equivalence classes’ or structure types.</td></tr><tr><td> $P_{k}$ </td><td>A set of problem types,  $P_{k} = \{P_{m}^{*} \mid P_{m}^{*} \in \alpha(P)\}$ .</td></tr><tr><td> $S_{l}$ </td><td>A set of structure types,  $S_{l} = \{S_{n}^{*} \mid S_{n}^{*} \in \beta(S)\}$ .</td></tr><tr><td> $\text{DSS}_{kl}$ </td><td>A DSS which is designed for problem types  $P_{k}$  and structure types  $S_{l}$ .</td></tr><tr><td> $D_{kl}^{c}$ </td><td>The development cost for computerized  $\text{DSS}_{kl}$ .</td></tr><tr><td> $C_{kl}^{c}$ </td><td>Cost per search iteration (efficiency) for computerized  $\text{DSS}_{kl}$ .</td></tr><tr><td> $C_{kl}^{m}$ </td><td>Cost per search iteration for manual  $\text{DSS}_{kl}$ .</td></tr><tr><td> $R_{kl}$ </td><td>The revenue from ‘solving’ a problem occurrence in  $P_{l}$  with the ‘best’ structure in  $S_{k}$ .</td></tr><tr><td> $\Phi_{kl}^{c}$ </td><td>The effectiveness of search parameter for computerized  $\text{DSS}_{kl}$ .</td></tr><tr><td> $\Phi_{kl}^{m}$ </td><td>The effectiveness of search parameter for manual  $\text{DSS}_{kl}$ .</td></tr><tr><td> $o_{i}$ </td><td>The number of problem occurrences of problem type  $i$ .</td></tr><tr><td> $O_{kl}$ </td><td>The total number of problem occurrences for  $\text{DSS}_{kl}$ .</td></tr><tr><td> $\delta_{kl}$ </td><td>The number of search iterations.</td></tr></table>

(1) Ignore the problem $(x^{c} = 0$ and $x^{m} = 0)$ ;

(2) implement a manual DSS ( $x^c = 0$ and $x^m = 1$ );

(3) implement a computerized DSS ( $x^c = 1$ and $x^m = 0$ ).

In addition, in order for the firm to evaluate these options it must determine the optimal number of search iterations ( $\delta$ ) for the computerized or manual system (given the various cost, revenue, and problem occurrence parameters).

The objective function is designed to capture the elements of the efficiency and effectiveness of the search for structure. This specific form assumes positive but decreasing marginal revenue from searching. Revenue asymptotically approaches R as $\delta$ goes to $\infty$ . The parameter (R) can be interpreted as the best (in terms of revenue) that the user can do for the given problem with the given structure type (assuming the search is free). Similarly, this form assumes that the marginal cost of searching is constant. This formulation is one of many reasonable formulations of the profit function (e.g., the rate of convergence to R could be a function of the level of R or the cost of searching could be variable).

For the specific model form given in (2), the values of the parameters $\Phi^{c}$ and $\Phi^{m}$ can be interpreted as the ‘effectiveness’ of the search. The higher the value of $\Phi$ , the ‘quicker’ structures which generate higher revenue are ‘found.’ This is analogous to the improvement of a programming algorithm so that it converges to an optimal solution in fewer iterations. This interpretation of the term ‘effectiveness of DSS design’ focuses on the net contribution of the DSS to firm profit. We note that this usage of ‘effectiveness’ may not be directly related to other authors’ use of the term.

The search for structure, whether or not it yields better structures, is not free. Our model assumes costs of $C^{c}$ or $C^{m}$ per iteration, depending on whether a computerized or manual system is selected. These cost parameters include the search, solution, and data costs of model evaluation.

In Figure 1 we illustrate the relations assumed in our model. These relationships include those between the number of iterations and the per problem occurrence revenue and cost for a given number, $o_{i}$ , of problem occurrences. The profit maximizing number of iterations for a computerized and manual DSS are, respectively

$$
\delta^ {c} = 1 / \left(\left(\Phi^ {c}\right) ^ {1 / 2} \left(C ^ {c}\right) ^ {1 / 2}\right), \text { and }\tag{3}
$$

$$
\delta^ {m} = 1 / \left(\left(\Phi^ {m}\right) ^ {1 / 2} \left(C ^ {m}\right) ^ {1 / 2}\right).\tag{4}
$$

Note, that in the case presented in fig. 1 the computerized DSS maximizes the per problem occurrence profit.

Figure 2 provides an illustration of the relationship between the revenue and costs for computerized and manual DSS as a function of the expected number of problem occurrences. This example assumes that the number of search iterations is fixed at the profit maximizing number implying that revenues and costs are linear in the number of occurrences.

For the example illustrated in fig. 2, the manual system would be optimal for problem occurrences less than $o^{*}$ , the transition point where the manual and computerized systems would yield identical returns. This point occurs where

![](/api/attachments/4CFBA5RU/fulltext/images/89b7c2ab0c7e574231fdd4f500db4059b73390caefd7549bc48ef9ed62a6c612.jpg)  
Fig. 1. Revenue and costs of search.

![](/api/attachments/4CFBA5RU/fulltext/images/883840d54bea8a75b18897aba45add2f6de262c32204a27ff8f4310500608b51.jpg)  
Fig. 2. Revenue and cost of problem occurrence.

$$
\begin{array}{r l} & o _ {i} \big \{R - \big (1 / (\Phi^ {c} \cdot \delta^ {c}) \big) - \delta^ {c} \cdot C ^ {c} \big \} - D \\ & \qquad = o _ {i} \big \{R - \big (1 / (\Phi^ {m} \cdot \delta^ {m}) \big) - \delta^ {m} \cdot C ^ {m} \big \}. \end{array}\tag{5}
$$

If the expected number of problem occurrences exceeds this transition value, the computerized DSS becomes optimal.

There are two critical components which drive the choice between a manual and a computerized DSS. The first is the possible enhancement of revenue by the computerized DSS. This enters the model in the form of the effectiveness parameter $\Phi^{c}$ . The second is the lowering of the search costs per iteration $C^{c}$ (or increasing efficiency). Reduction in per iteration search costs has two potential impacts. It can lower the cost of increasing the number of iterations searched, thereby increasing the potential quality of the answer for a given expenditure. It can also reduce the total search cost, thereby increasing the profit from any given number of search iterations. In the example illustrated in fig. 1 (where $o_{i}$ is assumed fixed), the per occurrence revenue and cost increase at the profit maximizing number of iterations if the system is computerized. The example in fig. 2 (where expected $o_{i}$ is a variable) is consistent with the example in fig. 1 in this regard. At levels of problem occurrence above $o^{*}$ , the computerized system is optimal even though the per occurrence costs for the computerized system are larger than for the manual system (that is $(C^{c} \cdot \delta^{c} + D/o_{i}) > C^{m} \cdot \delta^{m}$ ). Even though the per iteration cost of the computerized system is much lower than the manual system, it is optimal to greatly increase the number of search iterations compared to the manual system. This, along with the development cost of the computerized system, leads to a higher per occurrence cost of the computerized system. These examples illustrate two observations that are very important for the DSS portfolio selection process:

(1) Lower search costs of a computerized system do not imply lower per occurrence costs; and

(2) higher per occurrence costs of a computerized system do not imply that the system is not profit maximizing.

In other words, comparing the per iteration costs or per problem occurrence cost is not sufficient to determine whether or not it is optimal to choose a computerized DSS. Cost of search is related to profit, but that relationship is complicated by the interactions that exist between costs, revenue, and the determination of the optimal number of search iterations. This emphasizes our earlier comment that the value of DSS lies not in what they do (i.e., search), but in what they accomplish (i.e., solve).

Our theoretical formulation of the DSS selection problem provides the means to develop testable hypotheses. Consider the impact that changes in the effectiveness and efficiency parameters can have on the optimal number of search iterations and on the transition point. For simplicity we only look at the computerized system. A parallel analysis could be conducted for a manual system. Taking the partial derivative of (3) with respect to $C^{c}$ and $\Phi^{c}$ , we obtain

$$
\partial \delta^ {c} / \partial C ^ {c} = - 1 / \left(2 (C ^ {c}) ^ {3 / 2} \cdot (\Phi^ {c}) ^ {1 / 2}\right) <   0,\tag{6}
$$

$$
\partial \delta^ {c} / \partial \Phi^ {c} = - 1 / \left(2 (C ^ {c}) ^ {1 / 2} \cdot (\Phi^ {c}) ^ {3 / 2}\right) <   0.\tag{7}
$$

Both of these partial derivatives are less than zero. As expected, this implies that a decrease in cost per iteration will cause the optimal number of search iterations to increase. However, an increase in $\Phi^{c}$ will cause the optimal number of search iterations to decrease. This is interesting, since improvements in effectiveness and efficiency both reflect more profit per search, yet they imply opposite responses in the use of the system.

Since $C^{c}$ is inversely related to the number of optimal iterations, it is not immediately clear what will happen to the size of the variable cost per problem occurrence, $\delta^{c} \cdot C^{c}$ . The direction of this change can be determined by calculating the elasticity of the response of $\delta^{c}$ to a change in $C^{c}$ . For the functional forms assumed above, the elasticity of the response is -1/2. This implies, for example, that a 2% decrease in $C^{c}$ will increase $\delta^{c}$ by 1% which in turn implies that the per occurrence cost will decrease. In fact, in this particular model the per occurrence cost will always move in the same direction as the per iteration cost since the elasticity is constant and, therefore, not a function of the level of $C^{c}$ . Of course, generally this may not be the case for differing assumed functional forms.

A third set of testable hypotheses can be derived by analyzing the effect that changes in the efficiency and effectiveness parameters have on the transition point, the first level of $o_{i}$ for which a computerized system becomes economical. The transition point can be determined by solving equation (5) for $o_{i}$ , yielding

$$
o ^ {*} = D / \left\{R - \left(1 / \left(\Phi^ {c} \cdot \delta^ {c}\right)\right) - \delta^ {c} \cdot C ^ {c} - M \right\},
$$

where

$$
M = R - \left(1 / \left(\Phi^ {m} \cdot \delta^ {m}\right)\right) - \delta^ {m} \cdot C ^ {m}.\tag{8}
$$

Substituting the expression for the optimal level of $\delta^{c}$ (4) into (8) and then taking the partial derivatives of the result with respect to $C^{c}$ and $\Phi^{c}$ yields

$$
\partial o ^ {*} / \partial C ^ {c} = - D \left\{- (C ^ {c}) ^ {- 1 / 2} / (\Phi^ {c}) ^ {1 / 2} \right\} / V ^ {2} > 0,\tag{9}
$$

$$
\partial o ^ {*} / \partial \Phi^ {c} = - D \left\{\left(C ^ {c}\right) ^ {3 / 2} / \left(\Phi^ {c}\right) ^ {1 / 2} \right\} / V ^ {2} <   0,
$$

where

$$
V = \left\{R - 2 \left(\left(C ^ {c}\right) ^ {1 / 2} / \left(\Phi^ {c}\right) ^ {1 / 2}\right) - M \right\}.\tag{10}
$$

Equation (9) is always positive and (10) is always negative. Thus, for example, a reduction in search costs or an increase in effectiveness of the computerized system always lowers the transition point.

Changes in the development cost also affect the transition point. Using the procedure outlined above and then taking the partial derivative with respect to D, yields

$$
\partial o ^ {*} / \partial D = 1 / V > 0 \quad \text { for } V > 0.\tag{11}
$$

The condition V>0 simply states that the per problem occurrence profit of the computerized system (independent of development costs) must be larger than the per occurrence profit of the manual system. This condition must be satisfied for the computerized system to be feasible at any positive level of problem occurrence. There is certainly no reason to pay the development costs for a system which generates fewer dollars per problem occurrence than the manual system.

Efficiency and effectiveness are often treated as if they are independent goals. However, even in this basic model, these goals are highly interactive in their impacts on the optimal DSS design. Consider, for example, the notion that computerized DSS will be more efficient because of the 'economies of scale' of a computer. In the context of the basic model the computerized DSS has economies of scale because the average cost per occurrence, $(\delta^c \cdot C^c) + (D / o_i)$ , decreases as $o_i$ increases because of the 'sunk' costs of development which are averaged over the number of problem occurrences. However, the existence of economies of scale does not imply that the computerized system is the profit maximizing choice. Nor does it imply, if the computerized system is profit maximizing, that the per occurrence or total cost will be lower. As pointed out above, with lower search cost (increased efficiency) it can become beneficial to buy more effectiveness.

Table 3  
Impact of search parameter changes.

<table><tr><td colspan="2">Change in parameter</td><td> $\delta^{c}$ </td><td> $\delta^{c} \cdot C^{c}$ </td><td> $o^{*}$ </td></tr><tr><td> $C^{c}$ </td><td>↑</td><td>↓</td><td>↑</td><td>↑</td></tr><tr><td> $C^{c}$ </td><td>↓</td><td>↑</td><td>↓</td><td>↓</td></tr><tr><td>D</td><td>↑</td><td>-</td><td>-</td><td>-</td></tr><tr><td>D</td><td>↓</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $\Phi^{c}$ </td><td>↑</td><td>↓</td><td>↓</td><td>↓</td></tr><tr><td> $\Phi^{c}$ </td><td>↓</td><td>↑</td><td>↑</td><td>↑</td></tr></table>

Table 3 summarizes the testable comparative static results, hypotheses which can be tested in an experimental environment. These hypotheses are derived using specific assumptions about the revenue and cost functions. Under alternative specifications, we could derive competing testable hypotheses. This is the advantage of moving from a framework to a formal theory. We are not arguing that the theory proposed here will survive experimental tests. What we are arguing is that the process of constructing this theory from the framework has forced the formal consideration of the relationship between what DSS do and what DSS accomplish for the firm. Formal theory construction provides us with the means to derive testable implications, hypotheses which may be empirically tested using laboratory experiments and field studies. Following standard scientific method, such testing would result in theory validation or theory modification. Subsequent testing and analysis might then be directed at investigating the generality of the theory or validity of theory modification [10].

Although the basic DSS design model helps to identify the important parameters for measurement of DSS performance and for determining whether or not the scale of a DSS justifies the computerization of a DSS, it fails to capture important joint cost and synergistic benefit effects that can be critical in determining the optimal set of DSS and their scope for a profit maximizing firm. We now focus consideration on a more general model incorporating these components.

## 5. A general DSS portfolio selection model

As earlier, we continue to assume the ability to estimate the necessary revenue and cost parameters. Using the notation of table 2, we posit the general constrained optimization DSS design model as follows:

maximize

$$
\begin{array}{r l} & x _ {k l} ^ {c}, x _ {k l} ^ {m}, \delta_ {k l} ^ {c}, \delta_ {k l} ^ {m} \\ & \sum_ {k} \sum_ {l} x _ {k l} ^ {c} \big \{O _ {k} \big [ R _ {k l} - \big (1 / (\Phi_ {k l} ^ {c} \cdot \delta_ {k l} ^ {c}) \big) \\ & \qquad - \delta_ {k l} ^ {c} \cdot C _ {k l} ^ {c} \big ] - D _ {k l} ^ {c} \big \} \\ & + \sum_ {k} \sum_ {l} x _ {k l} ^ {m} \big \{O _ {k} \big [ R _ {k l} - \big (1 / (\Phi_ {k l} ^ {m} \cdot \delta_ {k l} ^ {m}) \big) \\ & \qquad - \delta_ {k l} ^ {m} \cdot C _ {k l} ^ {m} \big ] \big \}, \end{array}\tag{13}
$$

subject to

$x_{kl}^{c} + x_{kl}^{m}\leqslant 1$ for all $k$ and $l$

$$
\sum_ {k} \left(x _ {k l} ^ {c} + x _ {k l} ^ {m}\right) \leqslant 1 \text {   for   all   } l,
$$

where $x_{kl}^{c} = 0,1,x_{kl}^{m} = 0,1.$

The value of the objective function is the summation of the profit contribution from each of the selected computerized and manual DSS. The first set of constraints guarantees that each potential DSS is only assigned one outcome; that is, each DSS is computerized $(x_{kl}^{c}=1)$ , manual $(x_{kl}^{m}=1)$ , or not used. The second set of constraints guarantees that no problem type in the set of potential problem types is addressed by more than one DSS. Note that it may be optimal to ignore one or more problem types because of their small impact on revenue relative to the cost of the most efficient manual or computerized DSS available. This formulation of the problem assures that all possible DSS are considered.

As formulated, the general DSS portfolio selection problem can be solved in two stages. First the profit maximizing level of search iterations is determined for each possible manual and computerized DSS. This is the scale problem as discussed in the previous section. The solution for each individual DSS can be determined using equations (3) and (4). Typically we would expect that many of the solutions would generate negative profits and should not be considered further. The second step is to search over the profitable DSS for the profit maximizing combination or portfolio of DSS. In the second step, the general DSS design problem reduces to a linear integer programming problem for which solution algorithms are available. In related work, Ahituv and Halpern [2] utilized an integer programming approach for report design and allocation and Marsden and Pingry [28] provided a framework for determining the optimal generation of reports in an environment with economies of scope. The following numerical example should serve to clarify the key elements of the constrained optimization model and the solution technique suggested above. Assume that a firm faces three problem types and has two structure types from which to select models or structures to deal with problem occurrences. There are 21 possible combinations of problem-structure types that can form the domain of a DSS, each of which can be computerized, manual, or not utilized. The domain of these 21 DSS are enumerated in the first two columns of table 4. For example, the DSS in row 13 of table 4 applies structure type $S_{2}$ to problem types $P_{2}$ and $P_{3}$ . Table 4 provides the hypothetical values used for the parameters in our example for the 42 manual and computerized DSS.

Table 4  
Parameter values for sample problem.

<table><tr><td>Structure</td><td>Problem</td><td>R</td><td> $\Phi^m = \Phi^c$ </td><td> $C^m$ </td><td> $C^c$ </td><td>D</td></tr><tr><td> $S_1$ </td><td> $P_1$ </td><td>500</td><td>0.001</td><td>6</td><td>0.5</td><td>2500</td></tr><tr><td> $S_1$ </td><td> $P_2$ </td><td>20</td><td>0.001</td><td>7</td><td>2</td><td>400</td></tr><tr><td> $S_1$ </td><td> $P_3$ </td><td>5</td><td>0.001</td><td>6</td><td>2</td><td>300</td></tr><tr><td> $S_1$ </td><td> $P_1P_2$ </td><td>500</td><td>0.001</td><td>18</td><td>9</td><td>2600</td></tr><tr><td> $S_1$ </td><td> $P_1P_3$ </td><td>500</td><td>0.001</td><td>18</td><td>9</td><td>1900</td></tr><tr><td> $S_1$ </td><td> $P_2P_3$ </td><td>20</td><td>0.001</td><td>18</td><td>9</td><td>2600</td></tr><tr><td> $S_1$ </td><td> $P_1P_2P_3$ </td><td>500</td><td>0.0001</td><td>25</td><td>14</td><td>2800</td></tr><tr><td> $S_2$ </td><td> $P_1$ </td><td>10</td><td>0.001</td><td>7</td><td>3</td><td>600</td></tr><tr><td> $S_2$ </td><td> $P_2$ </td><td>200</td><td>0.001</td><td>5</td><td>1</td><td>600</td></tr><tr><td> $S_2$ </td><td> $P_3$ </td><td>150</td><td>0.001</td><td>5</td><td>2</td><td>400</td></tr><tr><td> $S_2$ </td><td> $P_1P_2$ </td><td>200</td><td>0.001</td><td>8</td><td>4</td><td>1200</td></tr><tr><td> $S_2$ </td><td> $P_1P_3$ </td><td>150</td><td>0.001</td><td>8</td><td>4</td><td>1000</td></tr><tr><td> $S_2$ </td><td> $P_2P_3$ </td><td>200</td><td>0.001</td><td>8</td><td>4</td><td>1000</td></tr><tr><td> $S_2$ </td><td> $P_1P_2P_3$ </td><td>200</td><td>0.0001</td><td>12</td><td>8</td><td>1800</td></tr><tr><td> $S_1S_2$ </td><td> $P_1$ </td><td>500</td><td>0.001</td><td>8</td><td>4</td><td>1300</td></tr><tr><td> $S_1S_2$ </td><td> $P_2$ </td><td>200</td><td>0.001</td><td>8</td><td>4</td><td>800</td></tr><tr><td> $S_1S_2$ </td><td> $P_3$ </td><td>150</td><td>0.001</td><td>8</td><td>4</td><td>500</td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_2$ </td><td>500</td><td>0.0001</td><td>12</td><td>6</td><td>2500</td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_3$ </td><td>500</td><td>0.0001</td><td>12</td><td>6</td><td>2300</td></tr><tr><td> $S_1S_2$ </td><td> $P_2P_3$ </td><td>200</td><td>0.0001</td><td>12</td><td>6</td><td>2600</td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_2P_3$ </td><td>500</td><td>0.0001</td><td>15</td><td>9</td><td>3500</td></tr></table>

Assuming the parameter values are known, the portfolio selection problem can be solved using the two steps discussed above. The first step is to solve for the optimal values of $\delta^{m}$ and $\delta^{c}$ for the computerized and manual options for each DSS using equations (3) and (4). The results of these calculations, along with the marginal profit and transition level of problem occurrence (using (5)), are presented in table 5. The marginal profit is the profit added by optimally solving another problem occurrence (for example, $[R_{kl} - (1/(\Phi_{kl}^{c} \cdot \delta_{kl}^{c})) - \delta_{kl}^{c} \cdot C_{kl}^{c}]$ evaluated at the optimal number of searches). Note that the transition level is not listed for the DSS where the manual option has negative marginal profit. In these cases the transition from manual to computerized has no interpretation. Utilizing the optimal number of searches and the number of problem occurrences, the profit can be calculated for the 21 computerized and 21 manual DSS. This information for three different sets of problems occurrences is presented in table 6a–c.

The second step is to solve the resulting linear integer programing problem. Although, this problem is simple enough to be solved by inspection, we utilized ZOOM/XMP developed by Marsten [32]. In the context of the discussion above, solving the first problem determined the scale information and solving the second problem determined the optimal scope given the scale information. The solution to the integer problem (see panel (a) of fig. 3 and table 6a) or optimal portfolio problem for the first set of problem occurrences is to computerize the DSS in row 10 and use a manual version of the DSS in row 4. This portfolio yields a profit of $6950 + 448 = 7398$ . Note that no problem type is solved by more than one DSS. This illustration helps to emphasize several important points. First, note that the DSS with the widest scope is not in the profit maximizing portfolio. In fact, use of the DSS in row 21 would result in a loss. A similar result holds for portfolios of DSS having narrow scope, containing one structure type and one problem type. The most profitable portfolio of narrow scope DSS has a profit of $1725 + 2819 + 448 = 4992$ . Although this portfolio is profitable, there are several more profitable alternatives.

Table 6a
Profits for sample problem. $O_{1}=5$ , $O_{2}=25$ , $O_{3}=14$ .  
Table 5  
Calculated values for sample problem.

<table><tr><td rowspan="2">Structure</td><td rowspan="2">Problem</td><td rowspan="2"> $\delta_m^*$ </td><td rowspan="2"> $\delta_c^*$ </td><td colspan="2">Marginal profit</td><td rowspan="2"> $o_i^*$ </td></tr><tr><td>Computer</td><td>Manual</td></tr><tr><td> $S_1$ </td><td> $P_1$ </td><td>12.91</td><td>44.72</td><td>345</td><td>455</td><td>22.7</td></tr><tr><td> $S_1$ </td><td> $P_2$ </td><td>11.95</td><td>22.36</td><td>-147</td><td>-69</td><td></td></tr><tr><td> $S_1$ </td><td> $P_3$ </td><td>12.91</td><td>22.36</td><td>-150</td><td>-84</td><td></td></tr><tr><td> $S_1$ </td><td> $P_1P_2$ </td><td>7.45</td><td>10.54</td><td>232</td><td>310</td><td>33.1</td></tr><tr><td> $S_1$ </td><td> $P_1P_3$ </td><td>7.45</td><td>10.54</td><td>232</td><td>310</td><td>24.1</td></tr><tr><td> $S_1$ </td><td> $P_2P_3$ </td><td>7.45</td><td>10.54</td><td>-248</td><td>-170</td><td></td></tr><tr><td> $S_1$ </td><td> $P_1P_2P_3$ </td><td>20.00</td><td>26.73</td><td>-500</td><td>-248</td><td></td></tr><tr><td> $S_2$ </td><td> $P_1$ </td><td>11.95</td><td>18.26</td><td>-157</td><td>-100</td><td></td></tr><tr><td> $S_2$ </td><td> $P_2$ </td><td>14.14</td><td>31.62</td><td>59</td><td>137</td><td>7.7</td></tr><tr><td> $S_2$ </td><td> $P_3$ </td><td>14.14</td><td>22.36</td><td>9</td><td>61</td><td>7.7</td></tr><tr><td> $S_2$ </td><td> $P_1P_2$ </td><td>11.18</td><td>15.81</td><td>21</td><td>74</td><td>22.9</td></tr><tr><td> $S_2$ </td><td> $P_1P_3$ </td><td>11.18</td><td>15.81</td><td>-29</td><td>24</td><td></td></tr><tr><td> $S_2$ </td><td> $P_2P_3$ </td><td>11.18</td><td>15.81</td><td>21</td><td>74</td><td>19.1</td></tr><tr><td> $S_2$ </td><td> $P_1P_2P_3$ </td><td>28.87</td><td>35.36</td><td>-493</td><td>-366</td><td></td></tr><tr><td> $S_1S_2$ </td><td> $P_1$ </td><td>11.18</td><td>15.81</td><td>321</td><td>374</td><td>24.8</td></tr><tr><td> $S_1S_2$ </td><td> $P_2$ </td><td>11.18</td><td>15.81</td><td>21</td><td>74</td><td>15.3</td></tr><tr><td> $S_1S_2$ </td><td> $P_3$ </td><td>11.18</td><td>15.81</td><td>-29</td><td>24</td><td></td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_2$ </td><td>28.87</td><td>40.82</td><td>-193</td><td>10</td><td></td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_3$ </td><td>28.87</td><td>40.82</td><td>-193</td><td>10</td><td></td></tr><tr><td> $S_1S_2$ </td><td> $P_2P_3$ </td><td>28.87</td><td>40.82</td><td>-493</td><td>-290</td><td></td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_2P_3$ </td><td>25.82</td><td>33.33</td><td>-275</td><td>-100</td><td></td></tr></table>

Table 6b  
Profits for sample problem. $O_{1} = 9$ , $O_{2} = 25$ , $O_{3} = 14$ .

<table><tr><td>Structure</td><td>Problem</td><td> $O_{t}$ </td><td>Manual profit</td><td>Computer profit</td></tr><tr><td> $S_{1}$ </td><td> $P_{1}$ </td><td>5</td><td>1725</td><td>-224</td></tr><tr><td> $S_{1}$ </td><td> $P_{2}$ </td><td>25</td><td>-3683</td><td>-2136</td></tr><tr><td> $S_{1}$ </td><td> $P_{3}$ </td><td>14</td><td>-2099</td><td>-1482</td></tr><tr><td> $S_{1}$ </td><td> $P_{1}P_{2}$ </td><td>30</td><td>6950</td><td>6708</td></tr><tr><td> $S_{1}$ </td><td> $P_{1}P_{3}$ </td><td>19</td><td>4402</td><td>3995</td></tr><tr><td> $S_{1}$ </td><td> $P_{2}P_{3}$ </td><td>39</td><td>-9685</td><td>-9220</td></tr><tr><td> $S_{1}$ </td><td> $P_{1}P_{2}P_{3}$ </td><td>44</td><td>-22000</td><td>-13727</td></tr><tr><td> $S_{2}$ </td><td> $P_{1}$ </td><td>5</td><td>-787</td><td>-1098</td></tr><tr><td> $S_{2}$ </td><td> $P_{2}$ </td><td>25</td><td>1464</td><td>2819</td></tr><tr><td> $S_{2}$ </td><td> $P_{3}$ </td><td>14</td><td>120</td><td>448</td></tr><tr><td> $S_{2}$ </td><td> $P_{1}P_{2}$ </td><td>30</td><td>633</td><td>1005</td></tr><tr><td> $S_{2}$ </td><td> $P_{1}P_{3}$ </td><td>19</td><td>-549</td><td>-553</td></tr><tr><td> $S_{2}$ </td><td> $P_{2}P_{3}$ </td><td>39</td><td>823</td><td>1867</td></tr><tr><td> $S_{2}$ </td><td> $P_{1}P_{2}P_{3}$ </td><td>44</td><td>-21684</td><td>-17890</td></tr><tr><td> $S_{1}S_{2}$ </td><td> $P_{1}$ </td><td>5</td><td>1606</td><td>568</td></tr><tr><td> $S_{1}S_{2}$ </td><td> $P_{2}$ </td><td>25</td><td>528</td><td>1038</td></tr><tr><td> $S_{1}S_{2}$ </td><td> $P_{3}$ </td><td>14</td><td>-404</td><td>-171</td></tr><tr><td> $S_{1}S_{2}$ </td><td> $P_{1}P_{2}$ </td><td>30</td><td>-5785</td><td>-2197</td></tr><tr><td> $S_{1}S_{2}$ </td><td> $P_{1}P_{3}$ </td><td>19</td><td>-3664</td><td>-2108</td></tr><tr><td> $S_{1}S_{2}$ </td><td> $P_{2}P_{3}$ </td><td>39</td><td>-19220</td><td>-13906</td></tr><tr><td> $S_{1}S_{2}$ </td><td> $P_{1}P_{2}P_{3}$ </td><td>44</td><td>-12082</td><td>-7900</td></tr></table>

<table><tr><td>Structural</td><td>Problem</td><td> $O_l$ </td><td>Manual profit</td><td>Computer profit</td></tr><tr><td> $S_1$ </td><td> $P_1$ </td><td>9</td><td>3106</td><td>1598</td></tr><tr><td> $S_1$ </td><td> $P_2$ </td><td>25</td><td>-3683</td><td>-2136</td></tr><tr><td> $S_1$ </td><td> $P_3$ </td><td>14</td><td>-2099</td><td>-1482</td></tr><tr><td> $S_1$ </td><td> $P_1P_2$ </td><td>34</td><td>7877</td><td>7949</td></tr><tr><td> $S_1$ </td><td> $P_1P_3$ </td><td>23</td><td>5328</td><td>5236</td></tr><tr><td> $S_1$ </td><td> $P_2P_3$ </td><td>39</td><td>-9685</td><td>-9220</td></tr><tr><td> $S_1$ </td><td> $P_1P_2P_3$ </td><td>48</td><td>-24000</td><td>-14720</td></tr><tr><td> $S_2$ </td><td> $P_1$ </td><td>9</td><td>-1416</td><td>-1496</td></tr><tr><td> $S_2$ </td><td> $P_2$ </td><td>25</td><td>1464</td><td>2819</td></tr><tr><td> $S_2$ </td><td> $P_3$ </td><td>14</td><td>120</td><td>448</td></tr><tr><td> $S_2$ </td><td> $P_1P_2$ </td><td>34</td><td>718</td><td>1299</td></tr><tr><td> $S_2$ </td><td> $P_1P_3$ </td><td>23</td><td>-664</td><td>-459</td></tr><tr><td> $S_2$ </td><td> $P_2P_3$ </td><td>39</td><td>823</td><td>1867</td></tr><tr><td> $S_2$ </td><td> $P_1P_2P_3$ </td><td>48</td><td>-23655</td><td>-19353</td></tr><tr><td> $S_1S_2$ </td><td> $P_1$ </td><td>9</td><td>2890</td><td>2062</td></tr><tr><td> $S_1S_2$ </td><td> $P_2$ </td><td>25</td><td>528</td><td>1038</td></tr><tr><td> $S_1S_2$ </td><td> $P_3$ </td><td>14</td><td>-404</td><td>-171</td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_2$ </td><td>34</td><td>-6556</td><td>-2157</td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_3$ </td><td>23</td><td>-4435</td><td>-2068</td></tr><tr><td> $S_1S_2$ </td><td> $P_2P_3$ </td><td>39</td><td>-19220</td><td>-13906</td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_2P_3$ </td><td>48</td><td>-13181</td><td>-8300</td></tr></table>

This example can be used to explore the impacts of these synergistic effects on optimal DSS portfolio selection. In particular, we illustrate how changes in the expected level of problem occurrence can lead not only to shifts from manual to computerized DSS, but also to shifts in the scopes of the DSS and changes in the optimal composition of the portfolio.

We explore the impact of changes in scale on optimal DSS portfolio selection by increasing the expected level of problem occurrence for problem type one $(P_{1})$ and the resulting changes in the profit-maximizing DSS portfolio. At the original level of $o_{1}$ , 5, the optimal solution is the one discussed above (and illustrated in panel (a) of fig. 3 and table 6a). When $o_{1}$ is increased to 9, it becomes optimal to computerize the manual DSS (see panel (b) of fig. 3 and the calculations in table 6b). Profit increases to $7949 + 448 = 8397$ .

Table 6c  
Profits for sample problem. $O_{1} = 34$ , $O_{2} = 25$ , $O_{3} = 14$ .

<table><tr><td>Structure</td><td>Problem</td><td> $O_I$ </td><td>Manual profit</td><td>Computer profit</td></tr><tr><td> $S_1$ </td><td> $P_1$ </td><td>34</td><td>11733</td><td>12979</td></tr><tr><td> $S_1$ </td><td> $P_2$ </td><td>25</td><td>-3683</td><td>-2136</td></tr><tr><td> $S_1$ </td><td> $P_3$ </td><td>14</td><td>-2099</td><td>-1482</td></tr><tr><td> $S_1$ </td><td> $P_1P_2$ </td><td>59</td><td>13669</td><td>15706</td></tr><tr><td> $S_1$ </td><td> $P_1P_3$ </td><td>48</td><td>11120</td><td>12993</td></tr><tr><td> $S_1$ </td><td> $P_2P_3$ </td><td>39</td><td>-9685</td><td>-9220</td></tr><tr><td> $S_1$ </td><td> $P_1P_2P_3$ </td><td>73</td><td>-36500</td><td>-20928</td></tr><tr><td> $S_2$ </td><td> $P_1$ </td><td>34</td><td>-5349</td><td>-3985</td></tr><tr><td> $S_2$ </td><td> $P_2$ </td><td>25</td><td>1464</td><td>2819</td></tr><tr><td> $S_2$ </td><td> $P_3$ </td><td>14</td><td>120</td><td>448</td></tr><tr><td> $S_2$ </td><td> $P_1P_2$ </td><td>59</td><td>1246</td><td>3137</td></tr><tr><td> $S_2$ </td><td> $P_1P_3$ </td><td>48</td><td>-1387</td><td>128</td></tr><tr><td> $S_2$ </td><td> $P_2P_3$ </td><td>39</td><td>823</td><td>1867</td></tr><tr><td> $S_2$ </td><td> $P_1P_2P_3$ </td><td>73</td><td>-35976</td><td>-28495</td></tr><tr><td> $S_1S_2$ </td><td> $P_1$ </td><td>34</td><td>10918</td><td>11399</td></tr><tr><td> $S_1S_2$ </td><td> $P_2$ </td><td>25</td><td>528</td><td>1038</td></tr><tr><td> $S_1S_2$ </td><td> $P_3$ </td><td>14</td><td>-404</td><td>-171</td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_2$ </td><td>59</td><td>-11376</td><td>-1904</td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_3$ </td><td>48</td><td>-9255</td><td>-1815</td></tr><tr><td> $S_1S_2$ </td><td> $P_2P_3$ </td><td>39</td><td>-19220</td><td>-13906</td></tr><tr><td> $S_1S_2$ </td><td> $P_1P_2P_3$ </td><td>73</td><td>-20046</td><td>-10800</td></tr></table>

![](/api/attachments/4CFBA5RU/fulltext/images/e84f12a9151640d3405bb88b60509e6958755311ccc07eeab4a0ba2c5ba3f2ab.jpg)

![](/api/attachments/4CFBA5RU/fulltext/images/9fa0b6f21a74edbefe7e09694fe9df50e25ce6f406fea18b860c41114e6cf618.jpg)

![](/api/attachments/4CFBA5RU/fulltext/images/2d48d726ef8e672829d75027838b54e4ee65637597575d0e3919f4d44531043f.jpg)  
Fig. 3. Optimal DSS portfolios.

Note that the scale of every DSS which includes problem type 1 increases as $o_{1}$ increases. When $o_{1}$ is increased to 34 the composition of the optimal portfolio changes again. At this level of occurrence of problem type 1, the optimal DSS consists of three computerized DSS with the narrowest scope (see panel (c) of fig. 3 and the calculations in table 6c). Profit increases to 12979 + 2819 + 448 = 16246. Note that this compares to a profit of 15706 + 448 = 16154 for the previously optimal DSS portfolio.

The profit of the firm is increasing as the number of problems of type 1 increase. This seems to imply that the firm could make more money by solving more problems. However, in our formulation, the number of problems is assumed to be exogenous and determined by the level of production of the firms revenue-generating product. Clearly as the marginal profit from the product decreased, it would imply decreasing marginal profit from solving problem occurrences (our assumptions may hold for a consulting firm).

The key point illustrated by the example is that, depending on the level of type 1 problem occurrence, different portfolios of DSS are optimal. The implication for the DSS portfolio selection strategy of a firm is that each DSS should not be evaluated independently.

We have not generated mathematical comparative static results (hypotheses for laboratory or empirical testing) for the general model similar to those generated for the basic model of the previous section. This could be done. Our previous testable implications were derived either by assuming that one option (computerized or manual) was already selected and looking at the impact of changes on the optimal number of search iterations, or by looking at the impact of changes on the transition point. The first procedure could be duplicated in the general case by assuming a particular DSS had been selected and examining the impact on the number of searches for that specific DSS (much as was done numerically above). However, accomplishing comparative statics (sensitivity analysis) across DSS in the more general case requires determining which DSS will enter and leave the optimal solution. This analysis is logically equivalent to that presented earlier, but computationally more difficult.

There are obviously many generalizations of this model. Examples include more general functional forms and dynamic or stochastic model formulations. Gremillion and Pyburn [12] considered the possibility of a stochastic portfolio model of DSS evaluation (without considering search or scope). Exploration of these generalizations, as well as the model form presented here, should build on fundamental relationships confirmed by careful experimental inquiry.

## 6. Summary

We have proposed a structure for the DSS portfolio selection problem and have argued that our initial modeling is a first step on the road to creating a solvable structure which adequately represents the DSS design problem. The value of this structure will ultimately lie in its ability to produce new insights and testable hypotheses, new design procedures, and, eventually improved management practice. We briefly summarize how the proffered structure provides a basis for interpreting various current issues in DSS research.

## 6.1. DSS experiments

There have been several papers addressing questions of DSS from an experimental perspective (see [5] for a recent thorough survey). These experiments have typically examined the performance of individuals (or groups) in a controlled task context, with and without a DSS. The null hypotheses tested in these experiments typically involved DSS related improvement in decision-maker performance measured by decision quality, time, and confidence.

The results of these experiments have been mixed in terms of the benefit of DSS usage. While this has caused some concern in the DSS community, we argue that generalizing from these results can be inappropriate and misleading. These experiments have been ex-post facto benefit/cost studies of specific systems in specific environments and not tests of hypotheses generated from theory about issues of DSS design and use [5].

To illustrate our point, consider an analogy from economics. There are several general principles in economics, based in theory and tested statistically and in the laboratory across a wide range of environments, which can be used in the evaluation of alternative investments or business strategies. These principles include ‘the law of demand’ and demand revealing properties of different types of auctions. The empirical and experimental work has been driven by the need to develop and test general principles as opposed to the ex post evaluation of specific individual or market behavior in a unique context.

Carrying the economics analogy further, suppose that a new machine is invented for producing the enduring example good, widgets. Being uncertain of the machine's value, suppose we decide to test the machine in two plants in different locations. Further, suppose that at the completion of the study we determine that the machine was valuable in one location but not in the other. What can we conclude from these results? Without a structure which guides our exploration of the relationships (production function?) and variables (price of labor?) which might affect the performance of the machine in different circumstances, any generalization is risky. On the other hand, the ex-ante availability of information on the production function and price of labor might allow for ex-ante evaluation of the machines in different circumstances.

In our view, the development of general principles of DSS design and evaluation must follow the same road (see [10] for a discussion of ex-ante versus ex-post information systems evaluation). However, the development of DSS principles can benefit immensely from the availability of the body of existing decision and economic theory. For example, our use of decision theory in this paper allows us to posit general principles and questions about DSS which might be tested using a systematic experimental research program.

## 6.2. DSS, learning, and expert systems

One general question raised by the analysis above is: When individuals search a model base, are there any general statements that can be made about the quality of the search strategies that they follow? Knowledge about individual's ability to search model bases could dramatically impact the benefit cost calculations for DSS. The shape of the benefit function posited earlier in this paper assumes that DSS users are very good at picking the first structure for evaluation and then they make improvements on that structure of declining marginal value. Another possible scenario is that individuals initially make bad guesses but then learn, resulting in increasing marginal revenue per search iteration (up to some limiting point). The implications for the optimal DSS portfolio choice and its associated net value will be quite different under these alternative learning assumptions. In the first case, the benefits are mainly captured in the early use. In the learning case 'use investment' must be incurred to capture the benefits.

The capture of expertise in the search for structure is a domain amenable for expert systems. For example, recently there has been discussion of expert modelling systems to assist the user in the structuring of statistical models and forecasting $[23,31,34]$ . The systems provide ‘value’ by reducing learning costs. If individuals are generally good ‘first guessers,’ then these systems provide less value than if individuals are ‘bad first guessers’ who benefit through learning.

## 6.3. DSS management

It is important for a DSS manager to distinguish between selecting the DSS portfolio and managing the use of the portfolio. If firm incentives are different than individual incentives, the use (number of searches) of the DSS will not necessarily coincide with the optimizing strategy upon which the DSS portfolio selection was based. Thus, estimating the value of a DSS portfolio must include the costs of creating and enforcing an appropriate incentive structure for the users of the DSS and the lost performance because of the difference between user incentive and firm goals [16].

## 6.4. Research agenda

Much remains to be done. The hypotheses must be interpreted and tested in experimental or empirical environments. At the heart of this problem is the measurement of ‘search iterations’, ‘effectiveness’, ‘revenue’ and ‘search cost.’ We must determine whether sufficient information can be gathered so that the states, actions, and mappings of the DSS portfolio selection problem can be specified and the requirements of adequate representation and solvability met. It is to these tasks that our present, ongoing research is directed [10].

The DSS design strategy expressed in this paper is in the spirit of the principles of MIS and DSS design found in the seminal works of Ackoff [1] and Sprague [38]. We strongly agree with the words of Ackoff: “The moral is simple: one cannot specify what information is required for decision making until an explanatory model of the decision process and the system involved has been constructed.”

This moral holds for all currently unstructured problems, including the DSS portfolio selection problem.

## Appendix A: Simon and DSS

To a large extent, the discussions of the ‘theory of DSS’ have been dominated by the views of decision-making set forth by Simon [35,36]. To help clarify our points, consider the relationship between the views offered by Simon and the views we have expressed here. Simon offered the following concepts related to decision-making: Stages (intelligence, design, and choice), types of problems (programmed and non-programmed), bounded rationality (caused by uncertainty, lack of information, and complexity), and types of goals (satisficing and optimality). In our formulation, the intelligence and design stages can be interpreted as a search for the structure which will be used to make the choice. Making a choice in a problem area must be proceeded by a choice of structure for making the choice (that is, selecting a structure for an unstructured problem). The reason the choice of structures is difficult (i.e., costly) is because of bounded rationality considerations. The intelligence and design phases of problem solving have traditionally been handled by labor (MBA's) rather than capital (hardware). The unique aspect of a computerized DSS is that it assigns computer hardware to assist in the intelligence and design phase of problem solving. This is in contrast to OR/MS models which are directed at the choice problem.

In this paper we have used decision theory to propose a structure for use in evaluating and choosing DSS for a profit maximizing firm, assuming that the purpose of DSS is to assist in finding the structures to deal with a forecasted stream of unstructured problems. Our interpretation of Simon's view of problem solving is to apply classic decision theory at a logically prior level of analysis, intelligence and design. As our goal we assume profit maximization. Profit is the criterion which is used to mediate the trade-offs between complexity, information requirements, and costly search when selecting a structure for choice. Clearly, all structures selected are satisficing in the sense that there will be less than a complete search and they will take into account the complexity, information, and search cost trade-offs. But profit maximizing firms cannot decide unilaterally to pursue a satisficing strategy in a competitive market. Competition will assure that the firms will satisfy at the 'highest level' (optimize?). Assuming otherwise is assuming that the firms can form and enforce a cartel to reduce profit performance. In a satisficing model a final choice is still made between competing goals using some criterion. The difference is that the criterion is in the head of the decision maker rather than in the form of a specified objective function. This is simply another consideration in the capital–labor trade-off problem in decision support.

## References

[1] R. Ackoff, Management Misinformation Systems, Management Science 14(4), B147–B156 (1967).

[2] N. Ahituv and J. Halpern, Data and Reports: Contents Design and Users Allocation, The Journal of Systems and Software 2, 193–199 (1981).

[3] M. Alavi and J.C. Henderson, An Evolutionary Strategy for Implementing a Decision Support System, Management Science (27)11, 1309–1323 (1981).

[4] M. Alavi and H.A. Napier, An Experiment in Applying the Adaptive Design Approach to DSS Development, Information and Management (7), 21–28 (1984).

[5] I. Benbasat and B.R. Nault, An Evaluation of Empirical Research in Management Support Systems, Decision Support Systems 6(3), 203–226 (1990).

[6] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, 1981).

[7] W.J. Baumol, J.C. Panzar, and R.D. Willig, Contestable Markets and the Theory of Industry Structure (Harcourt Brace Jovanovich, Inc., New York, 1982).

[8] J.F. Courtney, G. Desanctis, and G.M. Kasper, Continuity in MIS/DSS Laboratory Research: The Case for a Common Gaming Simulator, Decision Sciences (14), 419–439 (1983).

[9] J. Elam, J.C. Henderson, P.G.W. Keen, B.R. Konsynski, and C.L. Meador, A Vision for Decision Support, Working Paper (1984).

[10] C. Gardner, J.R. Marsden, and D.E. Pingry, The Design and Use of Laboratory Experiments in DSS Evaluation and DSS Portfolio Selection: Some Initial Results, Proceedings of the First Meetings of the International Society for Decision Support Systems (1990).

[11] G.A. Gorry and M.S. Scott Morton, A Framework for Management Information Systems, Sloan Management Review 13(1) (1971).

[12] L.L. Gremillion, and P.J. Pyburn, Justifying Decision Support and Office Automation Systems, Journal of Management Information Systems, 5–17 (Summer 1985).

[13] J.T. Hogue, and H. Watson, Management's Role in the Approval and Administration of Decision Support Systems, MIS Quarterly, 15–26 (June 1983).

[14] C. Holsapple, and A.B. Whinston, Artificially Intelligent Decision Support Systems—Criteria for Tool Selection, Decision Support Systems: Theory and Application (Holsapple and Whinston, ed., Springer-Verlag, 185–213, 1987).

[15] G.P. Huber, The Nature of Organizational Decision Making and the Design of Decision Support Systems, MIS Quarterly, 1–11 (June 1981).

[16] R. Mark Isaac, and David E. Pingry, Managing J. Pierrepont Finch: Should He be Given a PC?, Information and Management 21, 269–277 (1991).

[17] G.W. Kasper, The Effect of User-Developed DSS Applications on Forecasting Decision-Making Performance in an Experimental Setting, Journal of Management Information Systems, II(2), 26–39 (1985).

[18] P.G. Keen, and M. Scott-Morton, Decision Support Sys-

tems: An Organizational Perspective (Addison–Wesley, Reading, MA, 1978).

[19] P.G. Keen, Adaptive Design for Decision Support Systems, Data Base, (12)1 & 2, 15–25 (1980).

[20] P.G. Keen, Value Analysis: Justifying Decision Support Systems, MIS Quarterly, 1–15 (March, 1981).

[21] H.K. Klein, and R. Hirschheim, Fundamental Issues of Decision Support Systems: A Consequentialist Perspective, Decision Support Systems, (1)1, 5–24 (1985).

[22] F. Knight, Risk, Uncertainty and Profit, (Houghton Mifflin, New York, 1921).

[23] S. Kumar, and C. Hsu, An Expert System Framework for Forecasting Method Selection, Proceedings of the 21st Hawaii International Conference on System Sciences, 86–95 (1988).

[24] M. Landry, D. Pascot and D. Briolat, Can DSS Evolve Without Changing Our View of the Concept of 'Problem'? Decision Support Systems, (1)1, 25–36 (1985).

[25] M.A. Mahmood and J.N. Medewitz, Impact of Design Methods on Decision Support Systems Success: An Empirical Assessment, Information and Management, (9), 137–151 (1985).

[26] R.I. Mann, and H.J. Watson, A Contingency Model For User Development in DSS Development, MIS Quarterly, 27–38 (March, 1984).

[27] J.R. Marsden and D.E. Pingry, Problem Structure and DSS Design, Proceedings of the Nineteenth Annual Hawaii International Conference on System Sciences, 603–608 (1986a).

[28] J.R. Marsden and D.E. Pingry, Generating an Optimal Information System: PMAX-SDLC and the Redirection of MIS Research, Journal of Management Information Systems (Summer, 1986b).

[29] J.R. Marsden and D.E. Pingry, Decision Tables for Decision Support Systems Design, Proceedings of the Twentieth Annual Hawaii International Conference on System Sciences, 647–654 (1987).

[30] J.R. Marsden and D.E. Pingry, Decision Support System Approach to MBA Curriculum Design: Forecasting MBA 2000, Proceedings of the 23rd Hawaii International Conference on System Sciences.

[31] J.R. Marsden, D.E. Pingry and R.D. St. Louis, A Strategy for Determining the Optimal Domain for Knowledge Based Decision Support Systems, European Journal of Operational Research, 48(3), 342–350 (1990).

[32] R.E. Marsten, The Design of the XMP Linear Programming Library, ACM Transactions on Mathematical Software, (7)4, 481–497 (1981).

[33] J.H. Moore and M.G. Chang, Design of Decision Support Systems, Proceedings of the 17th Hawaii International Conference on System Sciences, 1–8 (1984).

[34] D. Nute, R. Mann, and B. Brewer, Using Defeasible Logic to Control Selection of a Forecasting Technique, Proceedings of the 21st Hawaii International Conference on System Sciences, 437–444 (1988).

[35] H.A. Simon, The New Science of Management (Harper and Row, New York, 1960).

[36] H.A. Simon, Theories of Bounded Rationality, in Decision and Organization, C.B. McGuire and Roy Radner (eds.) (North-Holland, 1972).

[37] S.R. Snitkin and W.R. King, Determinants of the Effectiveness of Personal Decision Support Systems, Information and Management, (10), 83–89 (1986).

[38] R.M. Sprague, A Framework for the Development of Decision Support Systems, MIS Quarterly, (4)4, 1–26 (1980).
