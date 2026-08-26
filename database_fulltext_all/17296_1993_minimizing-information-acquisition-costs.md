---
otero_id: 17296
otero_key: "JUXHZJT7"
title: "Minimizing information acquisition costs"
authors: "Brian L. Dos Santos; Vijay S. Mookerjee"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90010-z"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Expert system design Minimizing information acquisition costs

Brian L. Dos Santos \*

Purdue University, West Lafayette, IN, USA

Vijay S. Mookerjee

University of Washington, Seattle, WA, USA

Today, many organizations are investing heavily in expert systems. Unfortunately, many of these systems will fail to deliver the maximum possible value to their investors because little attention has been paid to the cost of providing these systems with the information they require to make a decision. In an expert system, the cost of providing the information that the system requires can be substantial. Minimizing information costs without affecting the decisions made by the system can reduce the cost of operating the system and thereby increase value. We develop an algorithm that determines an optimal information acquisition strategy for an existing system and show how a specific information acquisition strategy can be implemented. Because of the computational complexity of the algorithm, we also develop a simpler, heuristic solution to the problem. Our tests indicate that the heuristic performs very well. Prolog implementations for the same problem, on the other hand, perform poorly.

Keywords: Expert systems design, Optimal systems design, Knowledge representation, Decision support systems, Cost/benefit in system design

## 1. Introduction

Research in artificial intelligence (AI) has resulted in many products that are currently used in organizations. Among these products, expert systems (ES) hold the greatest potential for use in business, because it is believed that they can provide significant value to organizations [18]. However, current development tools and methods may result in expert systems that are excessively costly to use, because the cost of the information a user must provide may be higher than necessary.

![](/api/attachments/JUXHZJT7/fulltext/images/d749653e70b00167d53a8a6f9d0ac65ca38f1fbb500a3fbd61c9214037a46dc4.jpg)

Brian L. Dos Santos is Assistant Professor of Management at the Krannert Graduate School of Management, Purdue University, West Lafayette, Indiana. He received a Ph.D. in Management from Case Western Reserve University. Brian has worked as a systems analyst and project leader for both private and public sector organizations. His major research interests are in the management of information technologies and in the development of decision support and expert systems. His articles have appeared in many journals, including Decision Support Systems, IEEE Transactions on Engineering Management, Information and Management, Information Services & Use, Journal of Management Information Systems, Management Decision, Management Science, and Omega: The International Journal of Management Science, He has also published papers in the Proceedings of many International Conferences.

![](/api/attachments/JUXHZJT7/fulltext/images/8d315e15aac4b5fbbad2f4df44880c0a792b55cbe8727a43b18d1ea06a7d0d41.jpg)

Vijay S. Mookerjee is Assistant Professor at the School of Business Administration, University of Washington, Seattle, Washington. His research interests include Expert Systems, Decision Support Systems and economic considerations in the design and evaluation of information systems. He received a Bachelors Degree in Mechanical Engineering from Nagpur University in 1982 and a Post Graduate Diploma in Business Management from Indian Institute of

Management, Calcutta in 1984. He received his Ph.D in Information Systems from Purdue University in 1991. Prior to joining the Ph.D. program in 1988, he worked as a systems analyst and as a lecturer. He is a member of the Institute of Management Sciences and the Decision Sciences Institute.

Expert system researchers attempt to develop computer systems that emulate the problem solving behavior of human experts. Their efforts are usually judged by comparing the decisions or recommendations made by the system (i.e., expert system outputs) to the decisions made by human experts. Although expert systems now are widely used in many organizations, these systems are evaluated solely on the benefits provided by their outputs $[15,17]$ . The costs of using these systems after they are developed have been neglected. This may result in systems that do not provide the maximum possible value to the organization.

Recently, this problem has received the attention of researchers interested in expert system design $[9,13,21,22]$ . These researchers have tried to develop an economically driven theory for expert system design, based upon classical decision theory. However, their attempts to develop a general theory to guide the design of optimal expert systems have been unsuccessful. Besides, as Hall, Moore and Whinston $[9]$ point out, use of their models is hampered by the difficulty a designer would face in trying to obtain precise measures of the desirability of outcomes (i.e., estimating the value of different decisions that the system can make), a necessary condition for using these models. Their work, however, has drawn attention to the need to consider aspects of expert systems that have heretofore been neglected, most notably, information acquisition costs.

## 1.1. Value of an expert system

The value of an expert system is determined by the quality of the decisions or advice that the system provides and the cost of developing and operating the system. While expert system research has focused on development costs and the quality of the decisions made by the system, little attention has been paid to operational costs [6]. Operational costs include computing costs and the cost of providing information (i.e., input costs) that the expert system needs to make a decision. $^{1}$ A good deal of research in expert systems has focused on programming languages and knowledge representation, design factors that affect computing costs [13]. However, computing costs continue to decrease rapidly, while the costs of providing information that a system needs (referred to as information acquisition costs) are likely to increase. Little attention has been paid to information acquisition costs [6].

Information acquisition costs can constitute a significant portion of the cost of reaching a decision. For example, an expert system that performs medical diagnosis may require inputs that can only be obtained by conducting expensive laboratory tests or exploratory surgery. High input costs make it imperative that such a system request information in a cost effective manner. Failing to do so may result in excessive operational costs and consequently, reduced value to the organization. Information acquisition costs are affected by the information acquisition strategy used by the system. $^{2}$ Many technologies currently used to develop expert systems, such as expert system shells and programming languages such as Prolog, do not allow designers to easily control the information acquisition strategy. $^{3}$ However, even if the information acquisition strategy is easily controlled, the literature does not show how an optimal information acquisition strategy can be determined.

## 1.2. The objective

The primary objective of this paper is to show how an existing system or a system developed using current approaches can be re-designed to reach the same decisions while minimizing information acquisition costs. Much of the expert system research has sought to produce systems that perform at the level of a human expert. To the extent that past research has been successful, the approach described here can be used to develop systems that produce the same decisions that an expert would make, while minimizing information acquisition costs; thereby increasing the value of a system to the organization. The problem addressed here can be considered a special case of the optimal design problem discussed in Jacob, Moore and Whinston [13] and Hall, Moore and Whinston [9]. However, implementing the solution to this problem does not present the same estimation problems because the designer does not have to estimate the value of decisions made by the system because the decisions (i.e., outcomes) made by the system do not change. In this paper, we show how an optimal information acquisition strategy can be determined for an existing system and how such a strategy can be implemented.

## 1.3. Organization of the paper

In the next section, we briefly review literature that leads us to conclude that the use of current development methods and tools will result in systems that fail to minimize information acquisition costs. In Section 3, we present an algorithm that determines an optimal (i.e., least cost) information acquisition strategy for a given expert system. The computational complexity of this algorithm limits its use for problems (i.e., systems) with few inputs. Hence, in Section 4, we present a heuristic algorithm that can be used to solve problems with a large number of inputs. In Section 5, the strategies generated by the heuristic algorithm are compared to the optimal strategy and to strategies used by Prolog implementations for the same problem. We discuss how a specific information acquisition strategy can be implemented in Section 6. The paper ends with a summary and conclusions section.

## 2. Literature review

The literature reviewed here is that which suggests that existing development methods and tools are unlikely to result in expert systems that minimize information acquisition costs. In an expert system, the quality of the outputs and the cost of using the system are determined by two system components: (a) The knowledge base, i.e., the collection of rules and facts which prescribe recommendations (decisions) under different input conditions; and (b) the control mechanism which influences the sequence in which inputs are acquired by the system. The decisions made by an expert system are determined by its knowledge base, whereas both the knowledge base and the control mechanism can determine the information acquisition costs.

In a typical knowledge base, there are two types of knowledge: Domain knowledge and procedural knowledge. Domain knowledge determines the quality of the decisions that are made and therefore, the value of system outputs (i.e., gross payoff from the system). Hence, given specific domain knowledge, the gross payoff from a system is fixed. Procedural knowledge affects the information acquisition costs because it affects the sequence in which inputs are acquired by the system. $^{4}$ The information acquisition costs are determined by the cost of acquiring the individual inputs and the information acquisition strategy. Since procedural knowledge does not affect decision quality, it does not affect the gross payoff. $^{5}$ In addition to procedural knowledge, the input acquisition strategy is affected by the control mechanism and the order in which rules and facts are located in the knowledge base. Since we are concerned with the information acquisition strategy rather than the outputs of the system, our discussion of the literature pertains to: (a) the acquisition of procedural knowledge and its effect on the information acquisition strategy; and (b) the effects of current control mechanisms on the information acquisition strategy.

## 2.1. Knowledge acquisition

Knowledge acquisition (KA) refers to the transfer and transformation of expertise from a knowledge source (e.g., humans, documents, etc.) to a program [10]. Many different methodologies, both manual and automated, have been proposed to aid in acquiring expert knowledge [3,8,20,28]. It is widely believed that different methods of acquiring expert knowledge are best suited to capture different kinds of knowledge [8,14]. Interviews are best suited to capture domain knowledge while verbal protocols are best suited to capturing procedural knowledge [2,8]. $^{6}$

A good deal of the KA literature has focused on the transfer of knowledge from human experts. Hence, it is important to determine whether KA techniques capture the procedural knowledge used by experts. Acquiring procedural knowledge is difficult because human experts are often very poor at articulating such knowledge [24]. For example, when the expert system MYCIN was being built, it was found that the domain experts, in this case physicians, were unable to explicitly state the sequence of steps they used to arrive at a diagnosis [4]. The knowledge acquired consisted of discrete 'knowledge packets.' The task of sequencing these packets to arrive at a diagnosis was left to the control mechanism. Among current techniques for acquiring knowledge from human experts, protocol analysis is best suited to capturing procedural knowledge. In protocol analysis, procedural knowledge is typically acquired by studying transcripts of verbal reports produced during performance of the task [8]. In concurrent verbalizations of tasks, humans only report what is accessible in short term memory [7]. Since procedural knowledge often exists in a highly compiled form, it is often inaccessible in short term memory [23]. Hence, although an expert may use an optimal information acquisition strategy, an expert's procedural knowledge is not easily captured using current KA methods. Besides, experts may not use optimal information acquisition strategies [12,16]. We conclude, therefore, that current knowledge acquisition techniques are unlikely to help in designing systems that minimize information acquisition costs.

## 2.2. Control mechanism

An expert system's control mechanism is that component of the system that controls the pro-

An example of a knowledge base for a simple credit-granting system

<table><tr><td>Rule 1</td><td>If Sound-Financial-Status then Grant-Loan.</td></tr><tr><td>Rule 2</td><td>If Future-Repayment-Potential then Investigate-Further.</td></tr><tr><td>Rule 3</td><td>If Doubtful-Repayment-Potential then Investigate-Further.</td></tr><tr><td>Rule 4</td><td>If Poor-Financial-Status then Refuse-Loan</td></tr><tr><td>Rule 5</td><td>If (Income = High), then Sound-Financial-Status.</td></tr><tr><td>Rule 6</td><td>If (Income = Medium) and (Employed) and (Education &gt; = Bachelors) then Sound-Financial-Status.</td></tr><tr><td>Rule 7</td><td>If (Income = Medium) and (not Employed) and (Education &gt; = Bachelors) then Future-Repayment-Potential.</td></tr><tr><td>Rule 8</td><td>If (Income = Medium) and (Employed) and (Education &lt; Bachelors) then Doubtful-Repayment-Potential.</td></tr><tr><td>Rule 9</td><td>If (Income = Low) and (Good References) then Future-Repayment-Potential.</td></tr><tr><td>Rule 10</td><td>If (Income = Low) and (not Good References) then Poor-Financial-Status.</td></tr><tr><td>Rule 11</td><td>If (Income = Medium) and (not Employed) and (Education &lt; Bachelors) then Poor-Financial-Status.</td></tr></table>

![](/api/attachments/JUXHZJT7/fulltext/images/3ff2ee0b39da3e844c463217741a6c6f275f2a56a3d1f5f8b929cb0c9d514c4c.jpg)  
Fig. 1. Information acquisition strategy used in the prolog implementation in appendix A.

cessing of knowledge in the knowledge base. The control mechanism affects the information acquisition strategy used by the system [5]. The control mechanism in many expert systems use uninformed search techniques [1,26]. Using these techniques, typically, a solution, rather than the best solution is sought (i.e., the least cost solution). Uninformed search techniques are unlikely to result in an optimal acquisition strategy unless, for each problem, all possible sequences are found and the best one chosen. The high cost of such a search makes it impractical.

Today, most expert systems are developed using special development tools, e.g., programming languages such as Prolog, or expert system shells such as GURU, ART, EXSYS, KEE, etc. [11,19]. Control mechanisms provided by these tools allow a variety of search techniques to be used (e.g., backward chaining with depth first, forward chaining, mixed chaining, etc.). However, even with these techniques, an optimal information acquisition strategy cannot always be implemented. Besides, current development tools do not support the system designer in determining an optimal strategy. Hence, with current development tools, an optimal information acquisition strategy will occur only by chance. A simple example will support this assertion.

A decision table representation of the credit granting application in table 1

<table><tr><td rowspan="2"></td><td rowspan="2">Inputs &amp; decisions</td><td colspan="7">Rulesa</td></tr><tr><td>R1</td><td>R2</td><td>R3</td><td>R4</td><td>R5</td><td>R6</td><td>R7</td></tr><tr><td> $I_1$ </td><td>Income</td><td>High</td><td>Med.</td><td>Med.</td><td>Med.</td><td>Low</td><td>Low</td><td>Med.</td></tr><tr><td> $I_2$ </td><td>Applicant employed?</td><td>-</td><td>N</td><td>Y</td><td>Y</td><td>-</td><td>-</td><td>N</td></tr><tr><td> $I_3$ </td><td>Education &gt; = Bachelors</td><td>-</td><td>Y</td><td>N</td><td>Y</td><td>-</td><td>-</td><td>N</td></tr><tr><td> $I_4$ </td><td>Good references</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Y</td><td>N</td><td>-</td></tr><tr><td>D1</td><td>Grant loan</td><td>*</td><td></td><td></td><td>*</td><td></td><td></td><td></td></tr><tr><td>D2</td><td>Investigate further</td><td></td><td>*</td><td>*</td><td></td><td>*</td><td></td><td></td></tr><tr><td>D3</td><td>Refuse loan</td><td></td><td></td><td></td><td></td><td></td><td>*</td><td>*</td></tr></table>

$^{a}$ A “−” indicates that the state of the input need not be known for the decision to be made. A “\*” in the decision rows indicates the decisions to be made.

In table 1, the rules used in a simple credit granting application are shown. In this example, there are four inputs that the user may have to provide (i.e., income, education, employment and references) and three recommendations that the system can make (i.e., grant loan, refuse loan and investigate further). A Prolog implementation of this system is shown in Appendix A. With the domain knowledge organized as shown in Appendix A, the Prolog control mechanism will use the information acquisition strategy depicted as a decision tree in fig. 1. This strategy will not minimize information acquisition costs.

For this problem, an optimal strategy is easily determined, as demonstrated here. The domain knowledge in Appendix A is represented as a mixed-entry decision table in table 2 [27]. In the first column, the first four row entries describe the input variables. The first variable, income, can take on one of three values, while the other three variables are binary valued. The next three row entries describe the decisions that the system can make. The columns represent rules. An “\*” indicates that the decision described in that row is to be made, if the input variables take on the values indicated for that rule. A “-” in an input variable row indicates that for that rule, the input is not needed. Hence, the first rule is interpreted as follows: If an applicant’s income is high, a loan should be granted, regardless of the applicant’s education, employment status, or the quality of the applicant’s references.

If costs are incurred in acquiring these inputs, then, from table 2 it is easily seen that ‘income’ information should be acquired first, because ‘income’ information is required in every rule (while the other inputs are not required in some of the rules), and when ‘income is high,’ a decision can be made without acquiring additional information. If the applicant’s ‘income is medium,’ then information on ‘employment’ and ‘education’ should be gathered. In this case, the order in which information on employment and education is gathered does not matter, since information on both these variables is always required to reach a decision. If the applicant’s ‘income is low,’ then references should be sought in order to reach a decision. The optimal information acquisition strategy for this problem is depicted by the decision tree in fig. 2. In this example, the optimal strategy was derived without actually considering specific values for input costs and input state probabilities. Very often, however, input costs and input state probabilities are necessary to find an optimal strategy. In the next section, we show how an optimal information acquisition strategy can be determined when input costs and input state probabilities are required.

![](/api/attachments/JUXHZJT7/fulltext/images/e77688131545163c59a95de4df5f7dd9026e5ccee976128774e01502a03de09b.jpg)  
Fig. 2. An optimal information acquisition strategy for the credit granting application in table 1.

## 3. Determining an optimal strategy

To determine an optimal information acquisition strategy, it is necessary to determine from the existing system, the set of inputs that the system requests from the user and the set of decisions that the system can make. It is also necessary to find a mapping between the states that the different inputs can take and the resulting decisions reached by the system. Table 2 was generated from the rules in table 1 by determining the inputs, decisions and a mapping between input states and decisions.

## 3.1. Preliminaries

We assume that the domain knowledge in the current system is consistent (i.e., identical values for inputs do not result in different decisions) and complete (i.e., when all inputs have been observed, a decision can be reached). By including 'no decision' as one of the decisions that the system can arrive at, completeness is assured.

An optimal information acquisition strategy is determined using a dynamic programming approach. It is described here using the following definitions.

x is the set of inputs that the system can request from the user. If a system can request n inputs, then define $x = \{x_{i} \mid x_{i}$ is an input variable; $i = 1, \ldots, n\}$ .

$X_{i}$ is the set of (finite) disjoint states that input $x_{i}$ can take. Requesting $x_{i}$ from the user of a system determines the state of input $x_{i}$ . If $x_{i}$ has p possible states, then define $X_{i} = \{X_{iz} \mid X_{iz}\}$ is a possible state of input $x_{i}; z = 1, \ldots, p\}$ .

D is the set of decisions or outputs that the system can arrive at. These correspond to the decisions or recommendations made by the system. If the system can make m unique decisions, then define $D = \{d_{i} \mid d_{i}$ is a decision; $i = 1, \ldots, m\}$ ,

A decision function, $\delta$ , maps a set of input states to decisions that the system can make. $\delta: B \to \{D, \theta\}$ , where B is the set of input states obtained by observing inputs $x_{i}$ , and $\theta$ corresponds to situations where more information has to be gathered.

$C(x_{i})$ is the cost of gathering information on $x_{i}$ . We assume that input costs are independent of the order in which inputs are acquired. Here, we also assume that the input probability distributions are independent. $^{7}$

$\pi(X_{ij})$ is the probability of state $X_{ij}$ .

We define stage j as a stage at which j inputs have been acquired. Then, at stage j, the problem is one of determining whether a decision can be made with the information currently available, or another input has to be selected from the inputs that have not already been acquired.

$y_{jk}$ is the kth subset of x with j distinct elements, i.e., inputs. $|y_{jk}| = j$ , i.e., the cardinality of $y_{jk}$ is j. There are $^{n}C_{j}$ subsets of x with j elements. $y_{j}$ is the set of all subsets of x with j elements. $y_{j} = \{y_{jk} \mid y_{jk}, k = 1, \ldots, ^{n}C_{j}\}$ . At stage 0 (i.e., no inputs have been selected), $y_{0} = \emptyset$ .

$w_{jkq}$ is the qth list. A permutation of the elements of $y_{jk}$ generates $w_{jkq}$ . Factorial j (i.e., j!) permutations of the elements of set $y_{jk}$ are possible. Hence, $q = 1, 2, \ldots, j!$ . Each list is a sequence of elements from $y_{jk}$ . At stage 0, the list is null.

$u_{jkqr}$ is a list representing the rth state of the system, which may be reached if the members of $w_{jkq}$ are observed in sequence. When the members of $w_{jkq}$ are observed, each input takes on one of the possible states for that input. For each $w_{jkq}$ there are s possible states, where

$$
s = \prod_ {x _ {i} \in y _ {j k}} | X _ {i} |.
$$

If each input has p possible states, then $s = p^{j}$ . And, s = 0, if $y_{j} = \emptyset$ . At stage 0 (i.e., the null state), no information is available.

$Y_{j}$ is the set of all possible states that can exist by observing the members of all lists $w_{jkq}$ ; for each $k$ and $q$ . Then, $Y_{j} = \{u_{jkqr} \mid u_{jkqr}$ is a possible state $r$ for each $k$ and $q\}$ .

If state $u_{jkqr}$ is observed (j < n), let the optimal action to be taken by $a^{*}(u_{jkqr})$ . Having observed a subset of the inputs, either a decision can be reached with the information already available, or the $(j + 1)$ th input to be acquired must be selected (j inputs already have been selected). In other words, the optimal action in state $u_{jkqr}$ may be to observe a new input from the set of inputs not contained in $y_{jk}$ , or to make a decision if $\delta(u_{jkqr}) = d, d \in D$ .

Let $c^{*}(u_{jkqr})$ be the expected cost of taking optimal actions having reached state $u_{jkqr}$ , i.e., taking action $a^{*}(u_{jkqr})$ next and, if necessary, taking future optimal actions until a decision is reached. Then,

$$
c ^ {*} (u _ {j k q r})
$$

$$
= \left\{ \begin{array}{l} 0 \quad i f \delta (u _ {j k q r}) = d, \quad d \in D, e l s e \\ \underset {x _ {i} \in B} {\text {Min}} \left\{C (x _ {i}) + \sum_ {n = 1} ^ {p} \pi (X _ {i z}) c ^ {*} \right. \\ \left(\text {APPEND} [ u _ {j k q r}, X _ {i z} ]\right) \Bigg \}, \end{array} \right.\tag{1}
$$

where B is a subset of x, such that $B \cap y_{jk} = \emptyset$ and $B \cup y_{jk} = x$ . APPEND[ $u_{jkqr}, X_{iz}$ ] creates a new state by adding $X_{iz}$ to the end of list $u_{jkqr}$ . $c^{*}(\text{APPEND}[u_{jkqr}, X_{iz}])$ is the cost of optimal actions to reach a decision d ( $d \in D$ ), if the system reaches the state APPEND[ $u_{jkqr}, X_{iz}$ ].

## 3.2. The algorithm

This algorithm uses backward iteration to generate an optimal information acquisition strategy. Begin by determining what are the best actions to take for each possible state that may be reached if all but one of the inputs have been selected, i.e., $(n-1)$ inputs have been selected. Then, proceed to determine the best actions to take for each possible state than may be reached if $(n-2)$ inputs have been selected. Work backwards in this way, for $(n-3)$ inputs, then $(n-4)$ inputs and so on, until the first action to be taken is determined. For problems with at least two inputs, the algorithm is as follows:

Step 0. Begin by setting $j = n - 1$ .

Step 1. Determine $y_{jk}$ , $w_{jkq}$ and $u_{jkqr}$ . For each possible information state $u_{jkqr}$ use (1) to determine $c^{*}(u_{jkqr})$ . For a specific state $u_{jkqr}$ , either a decision can be made with the information available (resulting in $c^{*}(u_{jkqr}) = 0$ ), or the nth input will have to be observed. For j = n - 1, the second term in the expression to be minimized in (1) will always be 0. If the nth input is necessary to make a decision in state $u_{jkqr}$ , then $c^{*}(u_{jkqr})$ is the cost of acquiring the nth input. Note $c^{*}(u_{jkqr})$ for each $u_{jkqr}$ .

Step 2. Set $j = j - 1$ .

Step 3. Determine $y_{k}, w_{jkq}$ and $u_{jkqr}$ .

Step 4. For each state $u_{jkqr}$ , using (1), determine $c^{*}(u_{jkqr})$ . At stage j, for each state $u_{jkqr}$ note $a^{*}(u_{jkqr})$ as the optimal action given state $u_{jkqr}$ , i.e., determine the action corresponding to $c^{*}(u_{jkqr})$ . Here, $a^{*}(u_{jkqr})$ is the action that yields $c^{*}(u_{jkqr})$ . The optimal action could be a decision (if one can be reached with information state $u_{jkqr}$ ), or it could be a specification of the next input to be acquired.

Step 5. If $j = 0$ , proceed to Step 6, else return to Step 2.

Step 6. Construct an optimal information acquisition strategy, $T^{*}$ , by finding all paths $P_{i}^{*}$ , where each $P_{i}^{*}$ is determined by tracing the optimal actions $a^{*}(u_{jkqr})$ , beginning at the root node $(u_{jkqr} = u_{0110})$ and ending at a leaf node $(a^{*}(u_{jkqr}) = d$ , for $d \in D$ ).

The optimal strategy has an expected cost $c^{*}(u_{0110})$ , where $u_{0110}$ is the state where no information has been acquired, i.e., the null state.

To use this algorithm, we need to know the costs of each input and the probability of an input taking on a given state. We show how this algorithm works on the credit granting application in table 2, using the information in table 3. The problem is to determine what information should be gathered first. To begin, there are four choices and having selected one of them, there are three possible choices for the next variable, and so on. However, the information obtained from the first input may determine what the next choice should be. Fig. 3 depicts the possible choices for variable selection, while fig. 4 includes outcomes for the scenario in fig. 3 where $I_{1}$ is the first variable selected.

Initially, the algorithm begins with j = 3. All possible permutations of the four input variables, taken three at a time are first determined. For each such permutation, all possible states that the inputs can take are determined. In table 4, we show only those states when $I_{1}$ is the first input selected and $I_{1}$ has a value M (denoted by $I_{1M}$ ). The second and third inputs can be any of the three remaining inputs and they can take on any of their possible states. In addition, in table 4, we show the optimal action to be taken if a given state is reached and the cost of taking all future optimal actions. The first row in table 4 indicates that when $I_{1}$ , $I_{2}$ and $I_{3}$ are selected in order and take on values M, Y and Y, respectively, the next action is to reach decision $D_{1}$ and the additional cost is zero.

In addition to the states shown in table 4, the algorithm also considers all possible states when

![](/api/attachments/JUXHZJT7/fulltext/images/f324abde5e8e19df166cd3b45c3f7a4c58b7600d7118ae6620ee01ec67c1f2f1.jpg)  
Fig. 3. Possible choice for selection of inputs for the credit granting application.

$I_{1}$ is selected first and takes on values M or L. Also, all possible states when each of the other three variables are selected first are considered. Having determined the cost of future actions, given all possible states when three variables are selected, the algorithm determines the best possible action given all possible states when two variables are selected. This is shown in table 5, once again for the situation where $I_{1}$ is the first variable chosen and takes on a value M.

The second column shows the current state while the third column lists the possible inputs, given the current state. For each possible action in the current state, the possible outcomes are listed in the next column, followed by the action that would be taken if that outcome is reached.

![](/api/attachments/JUXHZJT7/fulltext/images/1cb41052ed5235b8d6a51bc64c80cdbf432d914bbdac0b09f7faa03a8e6d29c4.jpg)  
Fig. 4. Input choices with outcomes for the credit granting application.

Input costs and probabilities for credit granting application

<table><tr><td>Inputs</td><td>Costs ($)</td><td>Input states</td><td>Probabilities</td></tr><tr><td rowspan="3"> $I_1$ </td><td rowspan="3">2.00</td><td>H</td><td>0.5</td></tr><tr><td>M</td><td>0.3</td></tr><tr><td>L</td><td>0.2</td></tr><tr><td rowspan="2"> $I_2$ </td><td rowspan="2">1.00</td><td>Y</td><td>0.4</td></tr><tr><td>N</td><td>0.6</td></tr><tr><td rowspan="2"> $I_3$ </td><td rowspan="2">4.00</td><td>Y</td><td>0.6</td></tr><tr><td>N</td><td>0.4</td></tr><tr><td rowspan="2"> $I_4$ </td><td rowspan="2">3.00</td><td>Y</td><td>0.5</td></tr><tr><td>N</td><td>0.5</td></tr></table>

with one variable being selected and an optimal strategy would then be constructed.

The cost column shows what the cost would be if the current state is reached and the action in column 3 is taken, followed by optimal actions after that, if necessary. Finally, the optimal action, given the current state is reached (i.e., the state in column 2) is shown in the last column. That is the action to be taken, given the current state, i.e., $a^{*}(u_{jkqr})$ . Next, the process is repeated

## 3.3. Computational complexity

If each input can take on m values, at stage j there will be a total of $\left(^{n}P_{j}m^{j}\right)$ possible states. For each state $u_{jkqr}$ , $a^{*}(u_{jkqr})$ and $c^{*}(u_{jkqr})$ must be determined. If a decision is not possible in state $u_{jkqr}$ , determining an optimal action requires a choice of an additional input to be selected from the set of inputs that have not already been chosen (i.e., choosing from $x_{i} \in b_{jk}$ , where $|b_{jk}| = n - j$ , $b_{jk} \cap y_{jk} = \emptyset$ , and $b_{jk} \cup y_{jk} = x$ ). For each $x_{i} \in b_{jk}$ , m possibilities need to be considered, corresponding to the m possible states for $x_{i}$ . Then, for each $X_{ij}$ , the optimal action is determined from a list with $\left(^{n}P_{j+1}m^{j+1}\right)$ members, where $\left(^{n}P_{j+1}m^{j+1}\right)$ is the number of states at stage $j + 1$ . Hence, in order to determine the least cost set of actions at stage j, it is necessary to perform J evaluations, where $J = \left(^{n}P_{j}m^{j}\right)(n - j)m\left(\left(^{n}P_{j+1}m^{j+1}\right)/2\right)$ ,

Operation of the optimal algorithm with two inputs, the first input being $I_{1}$ which takes on a value M

<table><tr><td>Number</td><td>State  $u_{jkqr}$ </td><td>Action</td><td>Outcome</td><td>Next action</td><td>Cost ($)</td><td>Optimal action in state  $u_{jkqr}$ </td></tr><tr><td rowspan="4">1</td><td rowspan="4"> $I_{1M} I_{2Y}$ </td><td rowspan="2">Get  $I_3$ </td><td>Y</td><td>D1</td><td>4.00</td><td>Get  $I_3$ </td></tr><tr><td>N</td><td>D2</td><td></td><td></td></tr><tr><td rowspan="2">Get  $I_4$ </td><td>Y</td><td>Get  $I_3$ </td><td>7.00</td><td></td></tr><tr><td>N</td><td>Get  $I_3$ </td><td></td><td></td></tr><tr><td rowspan="4">2</td><td rowspan="4"> $I_{1M} I_{2N}$ </td><td rowspan="2">Get  $I_3$ </td><td>Y</td><td>D2</td><td>4.00</td><td>Get  $I_3$ </td></tr><tr><td>N</td><td>D3</td><td></td><td></td></tr><tr><td rowspan="2">Get  $I_4$ </td><td>Y</td><td>Get  $I_3$ </td><td>7.00</td><td></td></tr><tr><td>N</td><td>Get  $I_3$ </td><td></td><td></td></tr><tr><td rowspan="4">3</td><td rowspan="4"> $I_{1M} I_{3Y}$ </td><td rowspan="2">Get  $I_2$ </td><td>Y</td><td> $D_1$ </td><td>1.00</td><td>Get  $I_2$ </td></tr><tr><td>N</td><td>D2</td><td></td><td></td></tr><tr><td rowspan="2">Get  $I_4$ </td><td>Y</td><td>Get  $I_2$ </td><td>4.00</td><td></td></tr><tr><td>N</td><td>Get  $I_2$ </td><td></td><td></td></tr><tr><td rowspan="4">4</td><td rowspan="4"> $I_{1M} I_{3N}$ </td><td rowspan="2">Get  $I_2$ </td><td>Y</td><td>D2</td><td>1.00</td><td>Get  $I_2$ </td></tr><tr><td>N</td><td>D3</td><td></td><td></td></tr><tr><td rowspan="2">Get  $I_4$ </td><td>Y</td><td>Get  $I_2$ </td><td>4.00</td><td></td></tr><tr><td>N</td><td>Get  $I_2$ </td><td></td><td></td></tr><tr><td rowspan="4">5</td><td rowspan="4"> $I_{1M} I_{4Y}$ </td><td rowspan="2">Get  $I_2$ </td><td>Y</td><td>Get  $I_3$ </td><td>5.00</td><td>Get  $I_2$  or  $I_3$ </td></tr><tr><td>N</td><td>Get  $I_3$ </td><td></td><td></td></tr><tr><td rowspan="2">Get  $I_3$ </td><td>Y</td><td>Get  $I_2$ </td><td>5.00</td><td></td></tr><tr><td>N</td><td>Get  $I_2$ </td><td></td><td></td></tr><tr><td rowspan="4">6</td><td rowspan="4"> $I_{1M} I_{4N}$ </td><td rowspan="2">Get  $I_2$ </td><td>Y</td><td>Get  $I_3$ </td><td>5.00</td><td>Get  $I_2$  or  $I_3$ </td></tr><tr><td>N</td><td>Get  $I_3$ </td><td></td><td></td></tr><tr><td rowspan="2">Get  $I_3$ </td><td>Y</td><td>Get  $I_2$ </td><td>5.00</td><td></td></tr><tr><td>N</td><td>Get  $I_2$ </td><td></td><td></td></tr></table>

and, the number of different evaluations to be conducted to determine an optimal information acquisition strategy is

$$
\sum_ {j = 0} ^ {n - 1} 1 / 2 (n - j) m ^ {2 (j + 1) n} P _ {j} ^ {n} P _ {j + 1}
$$

Hence, the complexity of the algorithm is $O(m^{2n}(n!)^{2})$ . When the number of inputs and the states that each input can take are large (e.g., n > 7, m > 2), determining an optimal strategy with this algorithm is not practical. Hence, in the next section, we present a simpler, heuristic approach to the problem.

## 4. A heuristic solution

and expensive procedure to guarantee an optimal information acquisition strategy may not be of much value. Instead, a heuristic algorithm which can produce a strategy that is close to optimal, but takes much less time to do so, would be useful. Here, we present a heuristic algorithm that performed very well on our test problems.

The information costs and probabilities will often only be approximate values. Besides, the structure of the decision table may change as the expert system evolves. Hence, a time consuming

## 4.1. Preliminaries

We assume that the states of each input variable represented in the decision table are disjoint and the sum of the probabilities of all possible states represented in the decision table for each variable, equals 1. In addition, we also assume that the rules in the table are such that in every case presented to the system, one of the decisions in the table will be reached.

Before describing the algorithm, we define some terms using table 2. In table 2, $I_{1}$ through $I_{4}$ represent the inputs that may be acquired, D1 through D3 represent the decisions that the system can make and R1 through R7 are the rules. If, at any stage an input row has an entry for each rule in the table (i.e., there are no “−” entries in the row), we refer to the input as an always necessary input. In the example in table 2, $I_{1}$ is an always necessary input.

Operation of the optimal algorithm with three inputs, the first input being $I_{1}$ which takes on a value M

<table><tr><td>Number</td><td>State  $u_{jkqr}$ </td><td>Action taken</td><td> $c^{*}(u_{jkqr})(\$)$ </td></tr><tr><td>1</td><td> $I_{1M} I_{2Y} I_{3Y}$ </td><td>Grant Loan (D1)</td><td>0</td></tr><tr><td>2</td><td> $I_{1M} I_{2Y} I_{3N}$ </td><td>Investigate Further (D2)</td><td>0</td></tr><tr><td>3</td><td> $I_{1M} I_{2N} I_{3Y}$ </td><td>Investigate Further (D2)</td><td>0</td></tr><tr><td>4</td><td> $I_{1M} I_{2N} I_{3N}$ </td><td>Refuse Loan (D3)</td><td>0</td></tr><tr><td>5</td><td> $I_{1M} I_{3Y} I_{2Y}$ </td><td>Grant Loan (D1)</td><td>0</td></tr><tr><td>6</td><td> $I_{1M} I_{3Y} I_{2N}$ </td><td>Investigate Further (D2)</td><td>0</td></tr><tr><td>7</td><td> $I_{1M} I_{3N} I_{2Y}$ </td><td>Investigate Further (D2)</td><td>0</td></tr><tr><td>8</td><td> $I_{1M} I_{3N} I_{2N}$ </td><td>Refuse Loan (D3)</td><td>0</td></tr><tr><td>9</td><td> $I_{1M} I_{2Y} I_{4Y}$ </td><td>Get  $I_3$ </td><td>4.00</td></tr><tr><td>10</td><td> $I_{1M} I_{2Y} I_{4N}$ </td><td>Get  $I_3$ </td><td>4.00</td></tr><tr><td>11</td><td> $I_{1M} I_{2N} I_{4Y}$ </td><td>Get  $I_3$ </td><td>4.00</td></tr><tr><td>12</td><td> $I_{1M} I_{2N} I_{4N}$ </td><td>Get  $I_3$ </td><td>4.00</td></tr><tr><td>13</td><td> $I_{1M} I_{4Y} I_{2Y}$ </td><td>Get  $I_3$ </td><td>4.00</td></tr><tr><td>14</td><td> $I_{1M} I_{4Y} I_{2N}$ </td><td>Get  $I_3$ </td><td>4.00</td></tr><tr><td>15</td><td> $I_{1M} I_{4N} I_{2Y}$ </td><td>Get  $I_3$ </td><td>4.00</td></tr><tr><td>16</td><td> $I_{1M} I_{4N} I_{2N}$ </td><td>Get  $I_3$ </td><td>4.00</td></tr><tr><td>17</td><td> $I_{1M} I_{3Y} I_{4Y}$ </td><td>Get  $I_2$ </td><td>1.00</td></tr><tr><td>18</td><td> $I_{1M} I_{3Y} I_{4N}$ </td><td>Get  $I_2$ </td><td>1.00</td></tr><tr><td>19</td><td> $I_{1M} I_{3N} I_{4Y}$ </td><td>Get  $I_2$ </td><td>1.00</td></tr><tr><td>20</td><td> $I_{1M} I_{3N} I_{4N}$ </td><td>Get  $I_2$ </td><td>1.00</td></tr><tr><td>21</td><td> $I_{1M} I_{4Y} I_{3Y}$ </td><td>Get  $I_2$ </td><td>1.00</td></tr><tr><td>22</td><td> $I_{1M} I_{4Y} I_{3N}$ </td><td>Get  $I_2$ </td><td>1.00</td></tr><tr><td>23</td><td> $I_{1M} I_{4N} I_{3Y}$ </td><td>Get  $I_2$ </td><td>1.00</td></tr><tr><td>24</td><td> $I_{1M} I_{4N} I_{3N}$ </td><td>Get  $I_2$ </td><td>1.00</td></tr></table>

The criterion used to choose the next input variable, referred to as the loss criterion, is determined by computing the expected loss for each input in a decision table, as follows:

$$
L (x _ {i}) = C (x _ {i}) p (x _ {i}),
$$

where

$L(x_{i}) =$ Expected loss from observing input $x_{i}$ $C(x_{i}) =$ Cost of observing input $x_{i}$

![](/api/attachments/JUXHZJT7/fulltext/images/395d8f837162c52f9d051ecae7aa8f0ff17739bd4b5226e8e847b9aaf8b08b24.jpg)  
Fig. 5. Application of the heuristic to the credit granting application.

$p(R_{j}) = \text{The probability of using rule } R_{j} \text{ in the decision table. Here, we assume the inputs are independent,}$

$p(x_{i}) = \sum_{j \in B} p(R_{j})$ , where $B$ is the set of rules that has a “-” entry for variable $x_{i}$ .

Here, $\mathbf{p}(x_{i})$ is the probability of reaching a decision without observing $x_{i}$ . It is easy to see that the expected loss of an always necessary input is zero. The loss criterion is used in the algorithm described here.

## 4.2. The algorithm

This algorithm builds a decision tree representation of an information acquisition strategy by beginning at the root node and working towards the leaf nodes, adding nodes to the tree, one at a time. The algorithm is as follows:

Step 0. Create a set O of tables. Initially, O is empty. Designate the decision table representation of the knowledge base the current table.

Step 1. Check the current table to determine whether there are any always necessary inputs. If only one always necessary input is found, select it. If more than one always necessary input is found, arbitrarily select one input.

Step 2. If an input is selected in step 1, go to Step 4.

Step 3. Calculate the expected loss of observing an input (i.e., determine $L(x_{i})$ ), for each input in the current table. Select the input with the minimum expected loss. In the case of ties, arbitrarily choose one input.

Step 4. The current decision table is split into two or more decision tables. Determine the number of different possible states that the input selected in either Step 1 or Step 3 can take. Split the current table into as many new tables as the most recently selected input has states, with each table containing those rules that have the same value for the most recently selected input. If, for the most recently selected input, some rules have a “—” entry, include these rules in each of the newly created tables. Delete the row for the recently selected variable from all the new tables. If any of the newly created tables has a rule with all dashes (i.e., “−”), delete this rule from the table and note the decision reached as a result of the recently selected input taking on that value. If this results in all rules in a table being deleted, delete this table. Any remaining newly created tables are added to O.

Step 5. If O is empty, STOP. Otherwise, select any element of O and designate it the current table. Remove the selected member from O.

Step 6. If the current table has only one input row, select that input, note the decisions reached for the different states for that input and return to Step 5.

Step 7. Return to Step 1.

For the credit granting application, this process is shown in fig. 5. Initially, we start out with the decision table from table 2 as the current table. In the current table, $I_{1}$ is an always necessary input. Hence, $I_{1}$ is selected and three new tables are constructed for the three different states $I_{1}$ can take. Each of the newly created tables includes rules in which $I_{1}$ has the same state (i.e., $I_{1}=L$ or M or H). For $I_{1}=H$ , however, there is only one rule in the new table and it contains all dashes. Hence, the decision corresponding to that rule is noted (i.e., D1) and the table is deleted. The two remaining tables are added to O. We then repeat the process with one of the two tables in O as the current table. Again we select an input. With either table, we select an input because it is an always necessary input. It turns out that in this example, a strategy is generated by selecting ‘always necessary inputs’ in every iteration. In such cases, the strategy generated by the heuristic is an optimal strategy. It is only when it is necessary to use the loss criterion that the two algorithms may produce different strategies.

An always necessary input should be chosen first because it must be acquired in all paths in the tree. Hence, acquiring such an input at any point has no impact on the cost of the strategy and therefore, its optimality. Choosing always necessary inputs first, eliminates the need to compute the expected loss for all inputs and quickly reduces the size of the sub-tables. It follows that if there is more than one always necessary input, the order in which they are chosen will not affect the cost of the strategy.

In order to demonstrate the use of the loss function, we have modified the decision table in table 2 to that shown in table 6. With the new decision table, initially, there are no always necessary inputs. Hence, Step 3 in the algorithm is reached and the loss function is calculated for each possible input, as follows.

$$
L (I _ {1}) = C (I _ {1}) p (I _ {1}),
$$

where, from table 3, $C(I_1) = 2.00$ , and

$$
\begin{array}{r l} \mathrm{p} (I _ {1}) & = \mathrm{p} (R _ {2}) = \mathrm{p} (I _ {2} = Y) \mathrm{p} (I _ {3} = Y) \mathrm{p} (I _ {4} = Y) \\ & = 0. 4 \cdot 0. 6 \cdot 0. 5 = 0. 1 2. \end{array}
$$

Therefore,

$$
L (I _ {1}) = 2 \cdot 0. 1 2 = 0. 2 4.
$$

$$
\text { Also,   from   table   3, } C (I _ {2}) = 1. 0 0, \text { and }
$$

$$
\mathrm{p} (I _ {2}) = \mathrm{p} (R _ {1}) + \mathrm{p} (R _ {7}) = 0. 5 + 0. 1 = 0. 6.
$$

Therefore,

$$
L (I _ {2}) = 1 \cdot 0. 6 0 = 0. 6 0.
$$

Similarly, $L(I_{3})$ and $L(I_{4})$ are determined to be 2.64 and 2.4, respectively. Hence, Income $(I_{1})$ will be the first input selected and the tables will be split up as before. In this case too, there will be no further need to compute loss functions. Further input selection will be determined by always necessary inputs.

## 4.3. Computational complexity

Initially, a choice needs to be made between n inputs. After an input is chosen, m sub-tables are created, where m is the number of states that an input variable may take. In each sub-table, an input is selected from n-1 inputs, creating m new sub-tables. When two inputs are left in a table, selecting one of them completes the process since the last input is automatically selected. The computational complexity of the algorithm in terms of the number of inputs, n, and the number of states that each input can take, m, is

$$
\begin{array}{r l} & = (n) (m) (n - 1) (m) (n - 2) (m) (n - 3) \\ & \times (m) \dots (3) (m) (2). \end{array}
$$

The complexity of this algorithm is $O(m^{n-1}n!)$ . This heuristic is much more efficient in generating a strategy than the algorithm that generates an optimal strategy. In the next section, the quality of the strategy generated by the heuristic is compared to the optimal strategy for two different problems.

## 5. Performance comparisons

The first problem was adapted from O'Neill [25]. The problem represents a portion of a system used to assist in the identification of radars from intercepted emissions. This system requires a maximum of five inputs and arrives at one of five conclusions (i.e., radar classifications). A C-Prolog implementation of this system is shown in Appendix B.

In this case, the quality of the strategies generated by the optimal and heuristic algorithms are compared to one another and to the strategy that would be followed by two C-Prolog implementations for this problem. $^{8}$ One hundred test cases were generated by randomly selecting input costs and input state probabilities from a list of possible costs and input state probabilities. $^{9}$ For each of these 100 cases, an information acquisition strategy was generated using each of the algorithms and the expected cost of using the strategy was determined. The expected cost of a strategy was computed from the input costs and input state probabilities used to generate the strategy.

A modified version of the decision table in table 2

<table><tr><td rowspan="2"></td><td rowspan="2">Inputs &amp; decisions</td><td colspan="8">Rulesa</td></tr><tr><td>R1</td><td>R2</td><td>R3</td><td>R4</td><td>R5</td><td>R6</td><td>R7</td><td>R8</td></tr><tr><td> $I_1$ </td><td>Income</td><td>High</td><td>-</td><td>Med.</td><td>Med.</td><td>Med.</td><td>Low</td><td>Low</td><td>Med.</td></tr><tr><td> $I_2$ </td><td>Applicant employed?</td><td>-</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>-</td><td>-</td><td>N</td></tr><tr><td> $I_3$ </td><td>Education &gt; = Bachelors</td><td>-</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>-</td><td>-</td><td>N</td></tr><tr><td> $I_4$ </td><td>Good references</td><td>-</td><td>Y</td><td>-</td><td>-</td><td>-</td><td>Y</td><td>N</td><td>-</td></tr><tr><td>D1</td><td>Grant loan</td><td>*</td><td>*</td><td></td><td></td><td>*</td><td></td><td></td><td></td></tr><tr><td>D2</td><td>Investigate further</td><td></td><td></td><td>*</td><td>*</td><td></td><td>*</td><td></td><td></td></tr><tr><td>D3</td><td>Refuse loan</td><td></td><td></td><td></td><td></td><td></td><td>*</td><td>*</td><td></td></tr></table>

$^{a}$ A “-” indicates that the state of the input need not be known for the decision to be made. A “-” in the decision rows indicates the decisions to be made.

Table 7  
Comparison of heuristic and optimal algorithms and two C-Prolog implementations for the problem in Appendix B (100 cases)

<table><tr><td></td><td>Optimal</td><td>Heuristic</td><td>Prolog-1</td><td>Prolog-2</td></tr><tr><td>Average cost</td><td>310.24</td><td>310.85</td><td>371.93</td><td>371.74</td></tr><tr><td>Standard dev.</td><td>89.94</td><td>90.61</td><td>95.81</td><td>96.17</td></tr><tr><td>% of cases with optimal strategy</td><td>Not applicable</td><td>96</td><td>0</td><td>0</td></tr></table>

In a Prolog implementation, the strategy does not change if input costs and input state probabilities change. The expected cost of the strategy, however, will change with a change in input costs or input state probabilities. Two strategies, corresponding to two different sequences of the rules in Appendix B were determined. The expected cost of using each of these strategies was determined for each of the 100 cases used. A summary of the results of these tests for the two algorithms and the two Prolog implementations are presented in table 7. The average cost in table 7 is an average for 100 cases. The last row indicates how often the strategy used was the optimal strategy. The heuristic and optimal algorithms generated the same strategy in 96% of the cases (i.e., for the different input costs and input state probabilities) and both were considerably better than the strategies used by the two Prolog implementations.

The strategy generated by the heuristic was also compared to the optimal strategy for another problem. This problem was constructed so that many rules required only a small subset of the inputs (i.e., the decision table had many dash (“−”) entries in the input section). There were 4 inputs, 9 different decisions and 10 rules. For this problem, there is a very low probability that the inputs selected early on will be selected because they are always necessary inputs. Hence, the loss criterion is used more often. Two hundred test cases of costs and probabilities were created by randomly varying input costs and input state probabilities. The input costs were generated to fall within a range. For each case, a strategy was generated using the heuristic and the optimal algorithms and the expected cost of using each strategy was determined. Next, the input costs were generated for a different range and 200 test cases of costs and probabilities were generated as before. The average input cost and the range were varied to determine whether the heuristic would be affected. The results are summarized in table 8. The heuristic generated an optimal strategy in 65 to 70% of the cases. Besides, the average expected cost using the heuristic was only slightly higher than the average expected cost for the optimal strategy. The performance of the heuristic did not appear to be greatly affected by the range of input cost values.

Comparison of heuristic and optimal algorithms for a hypothetical problem (200 cases for each range of input costs)

<table><tr><td rowspan="2">Input range</td><td rowspan="2">% Optimal</td><td colspan="2">Optimal strategy</td><td colspan="2">Heuristic strategy</td></tr><tr><td>Avg.cost</td><td>Std.dev.</td><td>Avg.cost</td><td>Std.dev.</td></tr><tr><td>0-200</td><td>68</td><td>351</td><td>171</td><td>362</td><td>176</td></tr><tr><td>0-400</td><td>67</td><td>634</td><td>317</td><td>649</td><td>325</td></tr><tr><td>0-600</td><td>67</td><td>976</td><td>484</td><td>1004</td><td>498</td></tr><tr><td>0-800</td><td>70</td><td>1316</td><td>647</td><td>1354</td><td>668</td></tr><tr><td>0-1000</td><td>65</td><td>1549</td><td>792</td><td>1591</td><td>816</td></tr></table>

These results indicate that the heuristic performs quite well and frequently generates an optimal strategy. On the other hand, the two Prolog implementations performed poorly. For the first problem, the optimal strategy was never used by either of the Prolog implementations and the average expected cost for the Prolog implementations was much higher. Hence, identifying and implementing an optimal or near optimal (using the heuristic) information acquisition strategy should reduce information acquisition costs. In the next section, implementation of a strategy using existing tools is discussed.

## 6. Implementation

A specific information acquisition strategy may be implemented by adding appropriate metarules to the current system. Having determined an optimal or near optimal strategy using one of the algorithms presented earlier, appropriate metarules may be included within the domain knowledge in such a way as to force the control mechanism to use the strategy. The specific metarules necessary depend upon domain knowledge, the information acquisition strategy to be implemented and the control mechanism used by the system.

In this approach, logically, the knowledge base is separated into two parts, one containing domain rules and the other metarules. These two sub-components of the knowledge base interact via the inputs. The metarules implement the information acquisition strategy, while domain knowledge is used to determine whether a decision can be made. Whenever new information is acquired by the system, the domain rules are checked to determine whether a decision can be made with the information currently available. If a decision can be made, no additional information need be acquired. If a decision cannot be made, the metarules are consulted to determine which input should be acquired next, given the current state of knowledge. For the radar classification example, Appendix C shows how this approach can be implemented in C-Prolog.

## 7. Summary and conclusions

Most of the expert systems research has attempted to improve system outputs. The cost of the inputs required by the system have not been paid much attention. As a result, the use of existing tools and methods to develop expert systems are likely to result in systems that incur unnecessary input costs and therefore, reduced system value. Since expert systems are now widely used, it is important to direct efforts towards the provision of methods and tools that maximize the value of these systems to the organization.

Existing development methods and tools result in sub-optimal information acquisition strategies being used by expert systems, thereby reducing their value. For systems developed using existing methods, an optimal information acquisition strategy can be determined and implemented. An algorithm is described that generates such an optimal strategy, without affecting the decisions made by the system. Use of the algorithm, however, is impractical for systems with many inputs. As an alternative, an intuitively appealing heuristic algorithm that generates an information acquisition strategy is presented. In our tests, the heuristic generated optimal or near optimal strategies. Prolog implementations for the same problem resulted in much higher information acquisition costs than either the optimal strategy or the strategy generated by the heuristic. Finally, an approach that may be used to implement the optimal information acquisition strategy, using current development tools, is presented.

The current practice of separating the knowledge base from the control mechanism is useful during expert system development. Separation of these two components, allows a developer to focus attention on the acquisition of domain knowledge without any concern for how this knowledge is to be processed. However, as demonstrated in the paper, when the system is used, the resulting system could incur excessive input costs. Hence, it would be useful to provide expert system developers with tools that can aid in the determination of an optimal information acquisition strategy and the implementation of this strategy. These tools could then be used to redesign the system before it actually is used in an organization.

In developing other types of business applications (e.g., transaction processing systems), it is not unusual to use one set of tools during development and testing, while other tools are used to produce a more efficient system for production use. For example, it is now common to use an interpreter during system development and testing, while a compiler is used to produce an efficient system for use in production (i.e., when the system is actually used in the organization). A similar approach may be used in developing expert systems. Current development tools can be used to develop and test expert systems. Then, prior to actually using these systems, another software system could be used to produce the production version of the system. This software system would determine an optimal or near optimal information acquisition strategy and produce a program that implements the strategy.

## Appendix A. A C-Prolog implementation of the credit-granting application in table 1

value(X,Y):- fact(X,Y).

value(X,Y):- fact(X,Z), Y = Z.

value(X,Y):- not(fact(X, \_), write('Please Supply the Value of'), write(X), write(''), read(Z), asserta(fact(X,Z)), Z = Y.

retract-all:− retract(fact(X,Y)), retract-all.

retract-all.

run:- start.

run:- retract-all.

start: - not(process), start.

process: - grant-loan.

process: - investigate-further.

process: - refuse-loan.

grant-loan: - sound-financial-status.

sound-financial-status: - value(employed, y),
    value(education-above-bachelors, y),
    value(income, med), write('Grant-loan'), nl.

future-repayment-potential: - value(education-above-bachelors, y), value(income, med), value(employed, n), write('investigate further'), nl.

sound-financial-status: - value(income,high), write('Grant loan'), nl.

investigate-further:– future-repayment-potential.

investigate-further:— doubtful-repayment-potential.

doubtful-repayment-potential:-
value(income,med), value(employed,y),
value(education-above-bachelors,n),
write('investigate further'), nl.

future-repayment-potential: - value(income,low), value(good-references,y), write('investigate further'), nl.

refuse-loan: - poor-financial-status.

poor-financial-status: - value(income,low), value(good-references,n), write('Refuse loan'), nl.

poor-financial-status: - value(income,med), value(employed,n), value(education-above-bachelors,n), write('Refuse loan'), nl.

## Appendix B. A C-Prolog knowledge base for radar classification $^{10}$

run:– classify,!, retract-all.

classify: - surf-search, write('search-search').

classify: - air-intercept, write('air-intercept').

classify: - air-bomber, write('air-bomber').

classify: - early-warning, write('early-warning').

classify: - fire-control, write('fire-control').

classify: - write('No Classification').

value(X,Y):- fact(X,Y).

value(X,Y):- fact(X,Z), Y = Z.

value(X,Y):- not(fact(X,\_)), write('Please Supply the Value of'), write(X), write(''), read(Z), asserta(fact(X,Z)), Z = Y.

retract-all:- retract(fact(X,Y)), retract-all.

retract-all.

surf-search:- value(scan-type, x), value(radio-freq, x), value(pulse-width, x).

fire-control: - value(scan-type, x), value(radio-freq, y), value(pulse-width, x).

fire-control: - value(scan-type, x), value(radio-freq, z), value(pulse-width, x).

air-intercept: - value(scan-type, x), value(pulse-width, y).

air-intercept: - value(scan-type, y), value(pulse-freq, x), value(radio-freq, x).

air-intercept: - value(scan-type,y), value(pulse-freq,x), value(radio-freq,y).

fire-control:- value(scan-type, y), value(scan-time, x), value(radio-freq, z), value(pulse-width, x).

air-bomber: - value(scan-type, y), value(pulse-freq, y), value(pulse-width, y).

early-warning: - value(scan-type, y), value(pulse-freq, x), value(radio-freq, z), value(pulse-width, y).

surf-search: - value(scan-type, y), value(pulse-freq, y), value(radio-freq, x), value(pulse-width, x).

surf-search: - value(scan-type, y), value(pulse-freq, y), value(radio-freq, y), value(pulse-width, x).

air-intercept: - value(scan-type, y), value(scan-time, y), value(pulse-width, x), value(radio-freq, z).

run:- classify,!,retract-all.

classify:- air-bomber,write('air-bomber').

classify: - early-warning, write('early-warning').

classify:- fire-control,write('fire-control').

classify:- surf-search,write('search-search').

classify: - air-intercept, write('air-intercept').

classify: - write('No Classification').

value(X,Y):- fact(X,Y).

value(X,Y):- fact(X,Z), Y = Z.

value(X,Y):- not(fact(X,\_)), write('Please Supply the Value of'), write(X), write(''), read(Z), asserta(fact(X, Z)), Z = Y.

retract-all:− retract(fact(X,Y)), retract-all.

retract-all.

surf-search: - value(scan-type, x), value(radio-freq, x), value(pulse-width, x).

fire-control: - value(scan-type, x), value(radio-freq, y), value(pulse-width, x).

fire-control: - value(scan-type, x), value(radio-freq, z), value(pulse-width, x).

air-intercept: - value(scan-type, x), value(pulse-width, y).

air-intercept: - value(scan-type, y), value(pulse-freq, x), value(radio-freq, x).

air-intercept:-- value(scan-type, y), value(pulse-freq, x), value(radio-freq, y).

fire-control: - value(scan-type, y), value(scan-time, x), value(radio-freq, z), value(pulse-width, x).

air-bomber: - value(scan-type, y), value(pulse-freq, y), value(pulse-width, y).

early-warning: - value(scan-type, y), value(pulse-freq, x), value(radio-freq, z), value(pulse-width, y).

surf-search: - value(scan-type, y), value(pulse-freq, y), value(radio-freq, x), value(pulse-width, x).

surf-search:- value(scan-type, y), value(pulse-freq, y), value(radio-freq, y), value(pulse-width, x).

air-intercept: - value(scan-type, y), value(scan-time, y), value(pulse-width, x), value(radio-freq, z).

## Appendix C. C-Prolog implementation of an optimal information acquisition strategy for the radar classification problem in Appendix B

The information acquisition strategy implemented in this program is optimal for the input costs and input state probabilities shown below.

<table><tr><td rowspan="2">Inputs</td><td rowspan="2">Input costs</td><td colspan="3">Input state probabilities</td></tr><tr><td>x</td><td>y</td><td>z</td></tr><tr><td>scan-type</td><td>7.0</td><td>0.6</td><td>0.4</td><td></td></tr><tr><td>scan-time</td><td>85.0</td><td>0.1</td><td>0.9</td><td></td></tr><tr><td>pulse-frequency</td><td>123.0</td><td>0.1</td><td>0.9</td><td></td></tr><tr><td>radio-frequency</td><td>41.0</td><td>0.4</td><td>0.5</td><td>0.1</td></tr><tr><td>pulse width</td><td>60.0</td><td>0.9</td><td>0.1</td><td></td></tr></table>

The C-Prolog program

getinput(X):- write('please supply the value of'), write(X), write(''), read(Y), addinfo(X,Y).

addinfo(X,Y):- asserta(value(X,Y)).

measure-next: - not(value(scan-type, \_)),
    getinput(scan-type).

measure-next: - value(scan-type, x), not-
(value(pulse-width, \_)), getinput(pulse-
width).

measure-next: - value(scan-type, x), value(pulse-width, x), not(value(radio-freq, \_), getinput(radio-freq).

measure-next:- value(scan-type, y), not(value(radio-freq, \_)), getinput(radio-freq).

measure-next: - value(scan-type, y), (value(radio-freq, x); value(radio-freq, y)), not-(value(pulse-freq, \_)), getinput(pulse-freq).

measure-next: - value(scan-type, y), (value(radio-freq, x); value(radio-freq, y)), value(pulse-freq, y), not(value(pulse-width, \_)), getinput(pulse-width).

measure-next: - value(scan-type, y), value(radio-freq, z), not(value(pulse-width, \_)), getinput(pulse-width).

measure-next: - value(scan-type, y), value(radio-freq, z), value(pulse-width, x), not-(value(scan-time, \_)), getinput(scan-time).

measure-next: - value(scan-type, y), value(radio-freq, z), value(pulse-width, y), not-(value(pulse-freq, \_)), getinput(pulse-freq).

aaai: - value(scan-type, x), value(pulse-width, y), write('Radar type is air-intercept'), nl.

aaai: - value(scan-type, y), value(pulse-freq, x), (value(radio-freq, x); value(radio-freq, y)), write('Radar type is air-intercept'), nl.

aaai:- value(scan-type,y), value(scan-time,y), value(radio-freq,z), value(pulse-width,x), write('Radar type is air-intercept'), nl.

safc: - value(scan-type, x), value(radio-freq, y), value(pulse-width, x), write('Radar type is fire-control'), nl.

safc: - value(scan-type, x), value(radio-freq, z), value(pulse-width, x), write('Radar type is fire-control'), nl.

safc: - value(scan-type, y), value(scan-time, x), value(radio-freq, z), value(pulse-width, x), write('Radar type is fire-control'), nl.

ssss:- value(scan-type, x), value(radio-freq, x), value(pulse-width, x), write('Radar type is surf-search'), nl.

ssss:- value(scan-type, y), value(pulse-freq, y), (value(radio-freq, x); value(radio-freq, y)), value(pulse-width, x), write('Radar type is surf-search'), nl.

asab: - value(scan-type, y), value(pulse-freq, y), value(pulse-width, y), write('Radar type is air-bomber'), nl.

saew: - value(scan-type, y), value(pulse-freq, x), value(radio-freq, z), value(pulse-width, y), write('Radar type is early-warning'), nl.

run:- start.

run:- remove-all.

remove-all:- retract(value(X,Y)), remove-all.

remove-all.

start: - measure-next,!, not(process), start.

process:- aaai.

process:- safc.

process:- asab.

process:- saew.

process:-ssss.

## References

[1] A. Bagchi and A. Mahanti, Search Algorithms Under Different Kinds of Heuristics: A Comparative Study, JACM 30, No. 1, p 1–21 (1983).

[2] L. Bainbridge, Verbal Reports as Evidence of the Process Operator's Knowledge, International Journal of Man-Machine Studies 11, No. 4, p 411-436 (1979).

[3] J. Boose, A Program for Expert Systems Based on Personal Construct Psychology, International Journal of Man-Machine Studies 23, p 495–525 (1985).

[4] B. Buchanan and E. Shortliffe (Eds.), Rule-Based Expert Systems—The MYCIN experiments of the Stanford Heuristic programming Project (Addison-Wesley, 1984).

[5] R. Davis, Meta-Rules: Reasoning about Control, Artificial Intelligence 15, p 179–222 (1980).

[6] B.L. Dos Santos and V.S. Mookerjee, Towards Optimal

Expert System Design, Proceedings of the Twenty-fourth Annual Hawaii International Conference on System Sciences, IEEE Computer Society Press III, p 266–273 (January 1991).

[7] K. Ericsson and H. Simon, Verbal Reports as Data, Psychological Review 87, No. 3, p 215–251 (1980).

[8] J. Gammack and R. Young, Psychological Techniques for Eliciting Expert Knowledge, in Research and Development in Expert Systems, Proceedings of the Fourth Technical Conference of the BCS specialist group on Expert Systems, University of Warwick (1984).

[9] H.K. Hall, J.C. Moore and A.B. Whinston, A Theoretical Basis for Expert Systems, in Artificial Intelligence in Economics and Management, L. Pau, (Ed.) (Elsevier Science Publishers, 11–20, 1986).

[10] F. Hayes-Roth, D. Waterman, D. Lenat (Eds.), Building Expert Systems, (Addison-Wesley, New York, 1983).

[11] C.W. Holsapple and A.B. Whinston, Business Expert Systems (Irwin, Homewood, Illinois, 1987).

[12] V. Jacob, L. Gaultney and G. Salvendy, Strategies and Biases in Human Decision Making and their Implications for Expert Systems, Behavior and Information Technology 5, No. 2, 119–140 (1986).

[13] V.S. Jacob, J.C. Moore and A.B. Whinston, Artificial Intelligence and the Management Science Practitioner: Rational Choice and Artificial Intelligence, Interfaces 18, No. 4, 24–35 (July–August 1988).

[14] J. Kim and J. Courtney, A Survey of Knowledge Acquisition Techniques and Their Relevance to Managerial Problem Domains, Decision Support Systems 4, p 269-284 (1988).

[15] G. Klein and C. Brezovic, Evaluation of Expert Systems, in Defense Applications of Artificial Intelligence, S. Andriole and G. Hopple (Eds.), D.C. (Heath Coy., MA., 1987).

[16] K. Kroeck, P. Kirs and A. Fiedler, Cognitive Biasing Effects in Information Systems: Implications for Linking Real World Information with Human Judgement, Proceedings of the Twenty-second Annual Hawaii Interna-

tional Conference on System Sciences, IEEE Computer Society Press (January 1989).

[17] J. Liebowitz, Useful Approach for Evaluating Expert Systems, Expert Systems 3, p 86–95 (1986).

[18] F. Luconi, T. Malone and M. Scott Morton, Expert Systems: The Next Challenge for Managers, Sloan Management Review (Summer 1986).

[19] J. Martin and S. Oxman, Building Expert Systems: A Tutorial (Prentice Hall, Englewood Cliffs, New Jersey, 1988).

[20] R. Michalski, Understanding the Nature of Learning, in Machine Learning: An Artificial Intelligence Approach, R. Michalski, J.G. Carbonell and T.M. Mitchell, (Eds.), Vol. 2, 3–25 (Morgan Kaufmann, California, 1986).

[21] J.C. Moore and A.B. Whinston, A Model of Decision Making with Sequential Information Acquisition—Part I, Decision Support Systems 2, No. 4, p 285–307 (1986).

[22] J.C. Moore and A.B. Whinston, A Model of Decision Making with Sequential Information Acquisition—Part II, Decision Support Systems, 3, No. 1, p 47–72 (1987).

[23] D. Neves and J.R. Anderson, Compilation: A mechanism for the Automatization of Cognitive Skills, in J.R. Anderson (Ed.), Cognitive Skills and Their Acquisition (Erlbaum, Hillsdale, New Jersey, 1981).

[24] R.E. Nisbett and T.D. Wilson, Telling More Than We Can Know about Mental Processes, Psychological Review 34, 23 1259 (May 1977).

[25] J. O'Neill, Knowledge Acquisition for Radar Classification, Applications of Expert Systems 1, J. Ross Quinlan (Ed.) (Turing Institute Press, in Association with Addison-Wesley Publishing Company, Reading MA., 1986).

[26] J. Pearl, Heuristics: Intelligent Search Strategies for Computer Problem Solving, (Addison-Wesley, Reading, MA. 1984).

[27] S.L. Pollack, H.T. Hicks and W.J. Harrison, Decision Tables: Theory and Practice (Wiley, New York, 1971).

[28] J. Quinlan, Induction, Knowledge and Expert Systems, in Artificial Intelligence Developments and Applications, J.S. Gero and R. Stanton (Eds.) (North-Holland, 1988).
