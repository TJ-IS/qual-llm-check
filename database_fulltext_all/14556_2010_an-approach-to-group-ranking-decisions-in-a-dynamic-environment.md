---
otero_id: 14556
otero_key: "6FDEJU8U"
title: "An approach to group ranking decisions in a dynamic environment"
authors: "Yen-Liang Chen; Li-Chen Cheng"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.12.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An approach to group ranking decisions in a dynamic environment

Yen-Liang Chen <sup>a,</sup>⁎, Li-Chen Cheng

<sup>a</sup> Department of Information Management, National Central University, Chung-Li 320, Taiwan, ROC

<sup>b</sup> Department of Computer Science and Information Management, Soochow University, Taipei 100, Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 25 February 2009 Received in revised form 1 October 2009 Accepted 10 December 2009 Available online 21 December 2009

Keywords: Data mining Group decision making Group ranking Maximum consensus sequence

## a b s t r a c t

The group ranking problem is used to construct coherent aggregate results from preference data provided by decision makers. Although there have been different input formats used to represent user preferences, they share a common weakness, that the input mode is static. In other words, users must provide all the preference data at one time. To overcome this weakness, we propose a framework which allows users to provide partial and/or incomplete preference data at multiple times. Since this is a complicated issue, we speci<sup>fi</sup>cally focus on a particular aspect as a <sup>fi</sup>rst attempt at this framework. Accordingly, we reexamine a variant of the group ranking problem, the maximum consensus mining problem, which will give the longest ranking lists of alternatives that agree with the majority and disagree only with the minority, under the dynamic input mode assumption. An algorithm is developed to determine the maximum consensus sequences from the users' partial ranking data. Finally, extensive experiments are carried out using synthetic data sets. The results indicate that the proposed method is computationally ef<sup>fi</sup>cient, and can effectively identify consensus among all users

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

The group ranking decision process involves aggregating individual rankings to obtain a group ranking that is representative of coherent results. In other words, the group ranking algorithm generates consolidated ranking results which represent the group will, preference or decision from the preference data of all decision makers. In recent years, how to solve group ranking problems has become an important issue and the method has been widely used in many applications, such as decision making [13,17], group recommender systems [6], machine learning [16], web search strategies [2,8] and so on.

Typically, there are three input formats for decision makers to express their preferences regarding the alternatives, i.e., weighting models, pair-wise comparisons and ranking lists. All three formats have been used in previous studies to express the input preferences of individuals. These formats may be not perfect but they express user preferences reasonably well in most practical situations. According to the format adopted, users are asked to rank (in the ranking list model), rate (in the weighting model) or compare (in the pair-wise comparison model) the alternatives. After all preference data have been collected, an algorithm is applied to generate the consolidated results.

However, a limitation of these formats is that before applying the decision model each individual must <sup>fi</sup>rst provide preference data representing his/her preference regarding all alternatives. It is not allowed for a user to provide partial or incomplete preferences at multiple times. Preferences on all alternatives must be made at one certain time, and then expressed using one of the three formats. This kind of input is not possible in many practical situations.

Consider the following scenarios. Suppose there are many items that have to be ranked. In such a situation, decision makers may not be familiar with all items. As a result, it is dif<sup>fi</sup>cult to collect complete preference information from all decision makers at one time. It would be more reasonable to allow decision makes to rank a subset of items at multiple times at their own convenience. The <sup>fi</sup>nal result could then be generated based on partial preference data collected at multiple times.

Another scenario would be the investigation the preferences of a group of target customers. The environment is dynamic and the customers are variable, but we are interested in <sup>fi</sup>nding how the groups' preference changes over time. Nowadays, there are a variety of applications which do allow users to express their preferences more <sup>fl</sup>exibly. For example, in a survey system one investigates the degree of liking of the user for the various alternatives. In this system users are asked to answer questionnaires at multiple times. However, though invited users are not required to take part in all surveys or reply to all questions. As a result, the input preference data may be incomplete or there may be multiple copies. Note that these input records may include not only preference data but also the timestamps when users have submitted their preferences.

Web 2.0 sites, You-tube, Yahoo and Blogger are examples of sites that provide data about the most popular videos, pictures, songs, essays, movies or products on the site based on the rating or ranking provided by users over time. Since users provide this preference data only when they wish to, it is also partial, incomplete and constantly changes over time.

To cope with the emerging demands mentioned above, the input mode of the traditional group ranking system needs to be extended from a static mode to a dynamic mode. The dynamic mode involves the dimension of time. In other words, no longer will users have to provide input preference data at one point in time. A user will be able to input his/her preferences multiples times. Each time he/she only needs to express his/her preference for a subset of alternatives, rather than the complete set of alternatives.

The input format is an important dimension of the group ranking problem. A change from static to dynamic will have many repercussions in future studies. It is impossible to address all these issues at this time. Therefore, in this study we initiate a new approach to the group ranking problem, focusing on a speci<sup>fi</sup>c group ranking problem. This particular problem is used as a <sup>fi</sup>rst example along this new line.

Recently, we proposed a variant of the group ranking problem, called the consensus list mining problem. We assume that an individual's preferences can be represented as a total ranking list. An ordered sequence of alternatives is called a consensus if a majority of users agree to this ordering and only a minority of users disagrees. Accordingly, we developed algorithms to discover the maximum consensus sequences from the users' ranking lists, where the maximum consensus sequences represent the maximum possible consensuses that can be achieved among all users. The advantage to this consensus list approach is that we <sup>fi</sup>nd only the maximum agreeable consensuses from users, rather than forcing a total ranking list for all users. For example, a group of users may have consensus on a part of the items, say {A>D>E}, and have con-<sup>fl</sup>icting opinions on the other two items {B, C}. Previous methods forced us to generate a ranked list, say $\{ \mathsf { A } { > } \mathsf { B } { > } \mathsf { D } { > } \mathsf { C } { > } \mathsf { E } \}$ . However with our algorithm it is just necessary to report what the consensus is and what the con<sup>fl</sup>icts are.

Although the consensus list approach provides more reasonable consensus output results than previous methods, it requires each user to input a complete ranking of all alternatives. This is dif<sup>fi</sup>cult if users are not familiar with each alternative or if there is a large number of alternatives. Therefore, we must <sup>fi</sup>nd a more <sup>fl</sup>exible way to express user preferences. In this current study we allow each individual's preferences to be represented as multiple partial ranking lists, instead of a single total ranking list. A potential problem of this input format, however, is that there may be con<sup>fl</sup>icts within multiple partial ranking lists. This occurs because the same person may have different preferences at different times. Therefore, we allow “ties” and “contradictions” to exist in the users' input ranking lists. The input data differs from that in previous methods in three ways: (1) a user can use a sequence of lists to express his/her interests; (2) a list can be a partial list; and (3) con<sup>fl</sup>icts and ties can exist among the same user's lists.

Based on the input format mentioned above, an algorithm is developed to <sup>fi</sup>nd the maximum consensus lists from all users' partial ranking lists. Two types of results are generated: the maximum consensus sequences; and con<sup>fl</sup>icting alternatives for which we have no user consensus.

In the next section, we brie<sup>fl</sup>y review previous research regarding group ranking. We then de<sup>fi</sup>ne the problem and describe the proposed consensus sequence concept in detail. In the methodology section, an algorithm is developed to <sup>fi</sup>nd the maximum consensus sequences. In addition, the proposed methods are analyzed in a series of experiments. Finally, some conclusions are offered.

## 2. Related work

In this section, we <sup>fi</sup>rst review pertinent literature on group ranking and related work for the proposed methodology. After that, we provide a summary of our recent work, the consensus list approach for solving the group ranking problem.

## 2.1. Group ranking problems

Generally, as shown in the <sup>fi</sup>rst, second and fourth rows of Table 1 the traditional group ranking problem can be classi<sup>fi</sup>ed according to three dimensions: the completeness of the user-provided preference information, the type of compromised outcomes, and the format used to express users' preferences. In the third row, we classify all previous work as static input mode, because users must provide their preferences on the alternatives at one time. On the other hand, since we allow users to specify their preferences partially at multiple times, we classify our new input method as dynamic, because we take the time dimension into consideration. The major value of this work is to add a new dimension to the traditional group ranking problem. With this new dimension, we expect that in the future many variants of the group ranking problem can be proposed. Since it is impossible to address all possible issues in one study the speci<sup>fi</sup>c aim of this current study is to solve one particular variant of the group ranking problem, i.e., the recently proposed consensus mining problem [7]. This particular problem can be classi<sup>fi</sup>ed as a partial ranking approach+ranking lists+dynamic mode+partial order output according to classi<sup>fi</sup>cation scheme proposed in Table 1. The three dimensions of the traditional group ranking problem are now brie<sup>fl</sup>y reviewed.

There are three input formats used for group ranking problems, weighting models, pair-wise comparisons and ranking lists. The weighting model requires each individual to provide weights/scores for all alternatives. The decision maker (DM) often <sup>fi</sup>nds it dif<sup>fi</sup>cult to express his/her preferences as precise numerical values [15]. This model suffers from the problem of bias in the aggregation results due to the effects of personal differences in scoring behavior [21]. Pairwise comparisons are a general method for expressing the users' item preferences. This format requires individuals to provide a set of pairwise comparisons for all alternatives [10,14,21]. Providing these comparisons, however, becomes tedious, especially with a large number of alternatives. In the last type of format users are asked to provide lists of ranked alternatives. Since it is more general and <sup>fl</sup>exible for users to determine partial ordering lists at different times, this work assumes that an individual's preferences can be represented by many partial ranking lists.

According to the output results, previous approaches can be divided into two main types: fully ordered and a partially ordered. Each has its own advantages and has been successfully used in many applications. Most previous approaches pay close attention on how to minimize the total disagreement between the multiple input rankings, to ultimately obtain an overall ranking list which represents the achieved consensus. The fact that user opinions may be discordant is ignored. This may become a disadvantage if there is no consensus or only a slight consensus on alternative rankings. To overcome the above weakness, we recently proposed a novel consensus list approach, where we de<sup>fi</sup>ned the “maximum consensus sequences” as representing the maximum possible consensuses that can be achieved among all users. The advantage of this consensus list approach is that only the maximum agreeable user consensus' are reported, rather than simply producing a total ranking list for all users. This study follows this line to aggregate the result.

Approaches to group ranking problems can be roughly classi<sup>fi</sup>ed into two major types based on the completeness of the decision maker's preference information, the total ranking approach [8,18,22–25] and the partial ranking approach [3,4,9,10–12,19–21]. The former requires individuals to appraise all alternatives, while the latter requires only a subset of alternatives. We now present a review of previous studies according to the completeness of the input information.

Table 1  
A research framework of previous research.

<table><tr><td rowspan="3">Input</td><td>Information Completeness</td><td colspan="2">Total ranking approach</td><td>Partial ranking approach</td></tr><tr><td>Input format</td><td>Weighting</td><td>Ranking lists</td><td>Pair-wise comparison</td></tr><tr><td>Input mode</td><td colspan="2">Static(all previous methods)</td><td>Dynamic(this method)</td></tr><tr><td>Output</td><td>Output result</td><td colspan="2">Fully ordered</td><td>Partially ordered</td></tr></table>

## 2.1.1. Total ranking approach

Borda [5] was the <sup>fi</sup>rst to examine the ordinal ranking problem. He proposed a method of marks to rank candidates according to the sum of ranks assigned by votes for each candidate. Kemeny and Snell studied the ordinal ranking problem using distance measures. Their model is based on an optimization approach that minimizes the distance between two complete rankings presented in a pairwise format [22]. This optimal aggregation is known to be an NP-hard problem [1]. Cohen proposed a greedy-like algorithm for combining multiple rankings in order to minimize the number of disagreements [8]. Saaty developed the AHP (Analytic hierarchy process) in the late 1970s. The core technique of which is to consolidate full ranking lists by assigning weights to different criteria [16,24,25].

## 2.1.2. Partial ranking approach

From a practical point of view, allowing users to submit only a subset of the alternatives is more reasonable. Bogart generalized the Kemeny-Snell's theory of distance to include partial ordering [3,4]. Various solution methods based on distance functions have also been studied [10–12,19]. In some group ranking problems rankings include intensity [21]. The goal of most partial ranking approaches is to obtain a full ranking from user input data. However, Cook proved that in some cases, the aggregated results would not be a full order [13]. Furthermore, the aggregated results of some models do not always achieve a full ranking but only a partial ordering.

## 2.2. Our recent work

Most previous approaches, regardless of input data type, consolidate user input data and generate a full ordered list. As mentioned above, forcing an ordering list may do more harm than good when there is no user consensus on alternative orders. To remedy this shortcoming in our recent work we provided a new approach, the consensus list approach, to discover the maximum agreement among users [7].

The basic idea comes from “consensus decision-making theory”, which stresses that a process is needed to achieve the most agreeable decision among participants [26]. It not only explores the agreements of the majority, but also resolves or mitigates the objections of the minority. To support this decision process, we must <sup>fi</sup>nd the maximum consensus list from the users' ranking data and also identify con<sup>fl</sup>icting alternatives that require further negotiation. Accordingly, the algorithm proposed in our recent study is designed to generate these two types of results.

Although we can obtain maximum consensus lists in support of consensus decision making, the major weakness of the new method is the requirement that an individual's preferences must be represented as a total ranking list. This input requirement is dif<sup>fi</sup>cult when there are many alternatives. Therefore, we seek to relax this input requirement so that a user can provide his/her preferences in a more <sup>fl</sup>exible and dynamic manner.

## 3. Problem de<sup>fi</sup>nition

In this section, we formally de<sup>fi</sup>ne the problem of mining consensus sequences from the users' multiple partial ranking data. Let $U { = } \{ u _ { 1 } , u _ { 2 } , . . . , u _ { m } \}$ and $I = \{ i _ { 1 } , i _ { 2 } , . . . , i _ { n } \}$ denote all users and the sets of all distinct items, respectively. Each user u utilizes a set of ranked lists of items to express his/her preferences. The ranked lists of user $u _ { i }$ can be represented as a set of user sequences ${ { S } _ { i } } = \left\{ { { S } _ { i , 1 } } , { { S } _ { i , 2 } } , . . . { { S } _ { i , j } } . . . \right\}$

Contradictions are allowed in the same user's ranked lists. Let $S _ { i , j }$ be a user sequence, which can be represented as a sequence of distinct items in I

$$
S _ {i, j} = \left\{i _ {a _ {1}} \oplus i _ {a _ {2}} \oplus .. \oplus i _ {a _ {r}} \right\}\tag{1}
$$

where r is the number of items in $S _ { i , j } , 1 { \le } a _ { k } { \le } n$ for $k = 1$ to r and ⊕ $\in$ $\{ > , \geq , = \}$

Each user sequence must satisfy the following conditions: <sup>fi</sup>rst, an item cannot appear more than once in a user sequence; second, the comparator ⊕ belongs to $\{ > , \geq , = \}$ . The comparator $" > "$ means that the preceding item is more preferable than the succeeding item. The comparator $" \geq "$ indicates that the preceding item is at least as preferable as the succeeding item. Finally, the comparator $" = "$ denotes the same preference for both items. For example, we may have $I = \{ { \sf A } , { \sf B } , { \sf C } , { \sf D } , { \sf E } \}$ and $u _ { 1 } \prime _ { S }$ sequences are $S _ { 1 , 1 } = \{ \mathsf { B } > \mathsf { A } > \mathsf { C } > \mathsf { D } \} , \ S _ { 1 , 2 } = \{ \mathsf { A } > \mathsf { B } \geq \mathsf { C } > \mathsf { D } \}$ $S _ { 1 , 3 } = \{ \mathsf { A } > \mathsf { B } \geq \mathsf { C } > \mathsf { D } > \mathsf { F } \} , S _ { 1 , 4 } = \{ \mathsf { A } > \mathsf { B } = \mathsf { E } \geq \mathsf { C } > \mathsf { D } \} , S _ { 1 , 5 } =$ $\{ \mathsf { A } { > } \mathsf { B } { \geq } \mathsf { C } { \geq } \mathsf { D } { > } \mathsf { E } \}$ , and ${ { S } _ { 1 } } = \{ { { S } _ { 1 , 1 } } , { { S } _ { 1 , 2 } } , { { S } _ { 1 , 3 } } , { { S } _ { 1 , 4 } } , { { S } _ { 1 , 5 } } \}$

The sequence database D is formed from a set of records <uid, $S _ { i , j } ,$ timestamp>, where uid is the user identi<sup>fi</sup>er and $S _ { i , j }$ is a user sequence. The timestamp is composed of a sequence of characters denoting the date and/or time at which a certain ranking is submitted. Table 2 helps to explain the de<sup>fi</sup>nitions. The sample database will be used throughout the paper.

The goal of the proposed algorithm is to discover the maximum consensus sequences for the speci<sup>fi</sup>ed time interval. Only those sequences with timestamps that fall into the speci<sup>fi</sup>ed interval are used to discover maximum consensus sequences. A preprocessing step is needed to remove all sequences whose timestamps fall outside the time interval. Without loss of generality, it is assumed below that the preprocessing step has been performed and that all sequences fall inside the time interval. Furthermore, all sequences are viewed as equally important, i.e., we assign the same weights to those sequences. Suppose the speci<sup>fi</sup>ed time interval is $t _ { 1 } - t _ { 9 }$ and that all sequences shown in Table 2 fall in this interval. Then, we discover that $\{ \mathsf { A } { \scriptstyle > } \mathsf { B } { \scriptstyle \geq } \mathsf { C } { \scriptstyle > } \mathsf { D } \}$ is a maximum consensus sequence of these users, because it frequently occurs in their sequence lists. In addition, item F could be a con<sup>fl</sup>icting item because users reach no consensus for it.

Numerous de<sup>fi</sup>nitions are given to formally de<sup>fi</sup>ne the problem. These can be classi<sup>fi</sup>ed as follows:

De<sup>fi</sup>nitions 1, 2: relationships between item-pairs;

De<sup>fi</sup>nitions 3–8: relationships between sequences;

De<sup>fi</sup>nitions 9–12: how to compute the support of sequences in the data set;

De<sup>fi</sup>nitions 13, 14: de<sup>fi</sup>nitions of consensus sequences and con-<sup>fl</sup>icting items.

## 3.1. Definition 1 (Item-pair)

An item-pair can be represented as $p = \{ i _ { a _ { i } } \oplus i _ { a _ { i } } \}$ , where $i _ { a _ { i } } , i _ { a _ { i } } { \in } I ,$ $1 \leq a _ { i } , a _ { j } \leq n$ and ⊕ $\in \{ > , \geq , = \}$ . The relationship between two items in $p$ can be represented as $R e l ( i _ { a , } , i _ { a , } { p } )$

For example, i $\mathsf { f } p = \{ \mathsf { A } { > } \mathsf { B } \} , \mathsf { t h e n } R e l ( \mathsf { A } , \mathsf { B } , p ) { = } { \overset { , } { > } } \mathrm { . }$

## 3.2. Definition 2 (Relationship between two item-pairs)

Let $p _ { 1 }$ and $p _ { 2 }$ be two item-pairs with the same items, $i _ { a _ { i } }$ and $i _ { a _ { i } } .$ . The relationship between item-pairs $p _ { 1 }$ and $p _ { 2 }$ can be classi<sup>fi</sup>ed into three categories: comply, con<sup>fl</sup>ict, and no violation. Comply means that the relationship between $i _ { a _ { i } }$ and $i _ { a _ { j } }$ in $p _ { 1 }$ is the same as the relationship in $p _ { 2 } ;$ con<sup>fl</sup>ict means that the relationship between i and $i _ { a _ { j } }$ in p contradicts the relationship in $p _ { 2 } ;$ no violation means that the relationship between $i _ { a _ { i } }$ and $i _ { a _ { i } }$ in $p _ { 1 }$ does not contradict the relationship in $p _ { 2 } .$ All possible combinations are illustrated in Table 3.

Table 2 Sample database.

<table><tr><td>Uid</td><td colspan="2">1</td><td colspan="2">2</td><td colspan="2">3</td></tr><tr><td>Sid</td><td> $S_{ij}$ </td><td>Timestamp</td><td> $S_{ij}$ </td><td>Timestamp</td><td> $S_{ij}$ </td><td>Timestamp</td></tr><tr><td>1</td><td>B&gt;A&gt;C&gt;D</td><td> $t_1$ </td><td>A&gt;B≥C</td><td> $t_1$ </td><td>B≥D&gt;E</td><td> $t_2$ </td></tr><tr><td>2</td><td>A&gt;B≥C&gt;D</td><td> $t_2$ </td><td>B≥C&gt;D&gt;F</td><td> $t_3$ </td><td>B≥C&gt;D&gt;E</td><td> $t_3$ </td></tr><tr><td>3</td><td>A&gt;B≥C&gt;D&gt;F</td><td> $t_3$ </td><td>A&gt;B≥C&gt;D</td><td> $t_4$ </td><td>A=F&gt;B≥C</td><td> $t_5$ </td></tr><tr><td>4</td><td>A&gt;B=E≥C&gt;D</td><td> $t_4$ </td><td>A&gt;B&gt;C&gt;E&gt;F</td><td> $t_5$ </td><td>A=D&gt;B&gt;C=E</td><td> $t_6$ </td></tr><tr><td>5</td><td>A&gt;B≥C≥D&gt;E</td><td> $t_9$ </td><td>B≥C&gt;D&gt;E=F</td><td> $t_7$ </td><td>B&gt;A&gt;C=E&gt;D</td><td> $t_7$ </td></tr><tr><td>6</td><td></td><td></td><td>A&gt;B&gt;C&gt;D&gt;E</td><td> $t_8$ </td><td>A&gt;B&gt;C=E&gt;D</td><td> $t_9$ </td></tr><tr><td>....</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

For example, $\mathrm { i f } p _ { 1 } = \{ \mathsf { A } > \mathsf { B } \}$ and $p _ { 2 } = \{ { \sf A } = { \sf B } \}$ , then $R e l ( \mathrm { A } , \mathrm { B } , p _ { 1 } ) = \omega _ { > } "$ and $R e l ( \mathrm { A } , \mathrm { B } , p _ { 2 } ) = " = "$ . As a result, the relationship between $p _ { 1 }$ and $p _ { 2 }$ is con<sup>fl</sup>ict.

## 3.3. Definition 3 (Sequence)

A sequence α is an ordered list of distinct items. The number of items in a sequence is the length of the sequence. A sequence that has a length of k is referred to as a k-sequence. A k-sequence can be represented as $\alpha = \{ i _ { a _ { 1 } } \oplus i _ { a _ { 2 } } \oplus . . . \oplus i _ { a _ { k } } \}$ , where $i _ { a _ { k } } { \in } I \ 1 { \le } a _ { k } { \le } n$ and $\oplus \in \{ > , \geq , = \}$ . Note that if the comparators in successive items are al $" = "$ , these items are ordered alphabetically.

For example, $\alpha { = } \{ \mathsf { A } { > } \mathsf { B } { \geq } \mathsf { D } { = } \mathsf { E } \}$ is a 4-sequence.

## 3.4. Definition 4 (Sequence's relationship function)

Given a sequence $x { = } i _ { a _ { 1 } } { \oplus } _ { 1 } { \ldots } { \oplus } _ { p { - } 1 } i _ { a _ { v } } { \oplus } _ { p { \cdot } } { \oplus } _ { j } { \cdot } { \oplus } _ { q { - } 1 } i _ { a _ { o } } { \oplus } { \ldots } i _ { a _ { k } } ,$ let Rel $( i _ { a _ { p } } , i _ { a _ { q } } , x )$ denote the relationship between items $i _ { a _ { p } }$ and $i _ { a _ { q } }$ in x, whose value is de<sup>fi</sup>ned below.

(i) If ∃ ⊕ $\ u _ { j } \in \{ > \} p \le j \le q - 1$ , then $R e l ( i _ { a _ { n } } , i _ { a _ { a } } , x ) = " > " ;$

(ii) If $\forall \oplus _ { j } \in \{ = \} p \le j \le q - 1$ , then $R e l ( i _ { a _ { n } } , i _ { a _ { \alpha } } , x ) = " = " ;$

(iii) Otherwise, $R e l ( i _ { a _ { p } } , i _ { a _ { q } } , x ) = " \geq " .$

For example, given a sequence $\alpha { = } \{ \mathsf { A } { > } \mathsf { B } { \geq } \mathsf { D } { = } \mathsf { E } \}$ , we obtain Rel $( \mathsf { A } , \mathsf { B } , \alpha ) = \mathsf { \Omega } ^ { * } > ^ { \flat } , R e l ( \mathsf { B } , \mathsf { D } , \alpha ) = \mathsf { \Omega } ^ { * } \geq ^ { \flat }$ , and $R e l ( \mathrm { D } , \mathrm { E } , \alpha ) = " = "$

## 3.5. Definition 5 (Complying sequence)

A sequence α complies with another sequence $\beta$ if the following conditions are satis<sup>fi</sup>ed:

(i.) All item-pairs in α also appear in $\beta ,$ and all their relationships comply;

(ii.) |β| > |α|.

If the conditions in De<sup>fi</sup>nition 5 are satis<sup>fi</sup>ed, we call α a subsequence $\mathrm { o f } \ \beta .$

For example, assume that we have two sequences $\beta = \{ { \tt E } > { \tt A } =$ $\mathsf { B } \geq \mathsf { D } > \mathsf { C } > \mathsf { H } \}$ and $\alpha _ { 1 } = \{ \mathrm { B } \ge \mathrm { D } > \mathrm { C } \}$ . According to De<sup>fi</sup>nition 5, α complies with β.

Relationships between two item-pairs, $p _ { 1 }$ and $p _ { 2 } .$

<table><tr><td rowspan="2" colspan="2">Comparator</td><td colspan="3"> $Rel(i_{a},i_{a},p_{2})$ </td><td colspan="2"> $Rel(i_{a},i_{a},p_{2})$ </td></tr><tr><td>&gt;</td><td>=</td><td>≥</td><td>&gt;</td><td>≥</td></tr><tr><td rowspan="3"> $Rel(i_{a},i_{a},p_{1})$ </td><td>&gt;</td><td>Comply</td><td>Conflict</td><td>No violation</td><td>Conflict</td><td>Conflict</td></tr><tr><td>=</td><td>Conflict</td><td>Comply</td><td>No violation</td><td>Conflict</td><td>No violation</td></tr><tr><td>≥</td><td>No violation</td><td>No violation</td><td>Comply</td><td>Conflict</td><td>No violation</td></tr></table>

## 3.6. Definition 6 (Conflict sequence)

A sequence α con<sup>fl</sup>icts with another sequence β if there is an itempair $p _ { 1 }$ in α and another item-pair $p _ { 2 }$ in $\beta$ with the same items but with a con<sup>fl</sup>icting relationship between $p _ { 1 }$ and $p _ { 2 } .$

For example, assume that we have two sequences $\beta = \{ { \mathsf { E } } > { \mathsf { A } } =$ $\mathsf { B } \geq \mathsf { D } > \mathsf { C } > \mathsf { H } \}$ and $\alpha _ { 2 } = \{ \mathrm { B } > \mathrm { A } > \mathrm { C } \}$ . Then, $\alpha _ { 2 }$ con<sup>fl</sup>icts with $\beta ,$ since Rel $( \mathsf { B } , \mathsf { A } , \alpha _ { 2 } ) = \ " > "$ and $R e l ( \mathbb { A } , \mathbb { B } , \mathbb { B } ) = " = "$

## 3.7. Definition 7 (No violation sequence)

There is a no violation relationship between sequences α and $\beta$ if the following conditions are satis<sup>fi</sup>ed:

(i.) There is at least one item-pair $p _ { 1 }$ in α and another item-pair p<sub>2</sub> in $\beta$ with the same items but with a no violation relationship between $p _ { 1 }$ and $p _ { 2 } ;$ and

(ii.) all the other item-pairs containing common items in α and $\beta$ comply.

## 3.8. Definition 8 (Unknown sequence)

The relationship between sequences α and $\beta$ is unknown if the following conditions are satis<sup>fi</sup>ed:

(i.) α does not con<sup>fl</sup>ict with $\beta ;$ and

(ii.) not all items in α appear in $\beta .$

For example, assume that we have three sequences $\beta =$ $\{ \mathrm { E } > \mathsf { A } = \mathsf { B } \ge \mathsf { D } > \mathsf { C } > \mathsf { H } \} , \ \alpha _ { 3 } = \{ \mathsf { A } \ge \mathsf { B } > \mathsf { C } \}$ , and $\alpha _ { 4 } = \{ \mathtt { A } \ge \mathtt { G } > \mathtt { D } \}$ . Then the relationship between α and $\beta$ is no violation, because (1) the relationship between Rel(A, B, β) and $R e l ( \mathsf { A } , \mathsf { B } , \alpha _ { 3 } )$ is no violation; and (2) the relationship between $R e l ( \mathsf { A } , \mathsf { C } , \beta )$ and $R e l ( \mathsf { A } , \mathsf { C } , \alpha _ { 3 } )$ and that between Rel(B, C, β) and Rel(B, C, α ) are comply. Further, the relationship between α and $\beta$ is unknown because item G appears in $\alpha _ { 4 } ,$ but not in $\beta .$

From De<sup>fi</sup>nitions 5, 6, 7, and 8, we develop a procedure to determine the relationship between two sequences. The procedure is illustrated in Fig. 1 using an activity diagram, where the rounded rectangles represent activities and the gray rounded rectangles represent the <sup>fi</sup>nal relationship between two sequences. By repeatedly processing all item-pairs in α, we can determine the relationship between these two sequences.

## 3.9. Definition 9 (User's complying support)

Let |S | be the total number of sequences in $S _ { i }$ (for user i). The complying support of sequence α in user i's sequences is de<sup>fi</sup>ned as

$$
u s u p _ {i} (\alpha) = \frac {\left| \left\{S _ {i , j} \mid S _ {i , j} \in S _ {i} \wedge \alpha \text {   is   complied   with   } S _ {i , j} \right\} \right|}{\left| S _ {i} \right|}.\tag{2}
$$

For example, user 1's comply support of sequence $\{ \mathsf { A } { > } \mathsf { B } { \geq } \mathsf { C } \} \mathrm { i } \mathsf { s } 4 / 5$ in the sequence database shown in Table 2.

![](/api/attachments/6FDEJU8U/fulltext/images/4388771723531061e52cc33976e3690221b76d4363073265fd99c2eafb9ec7fe.jpg)  
Fig. 1. Activity diagram for determining the relationship between two sequences.

## 3.10. Definition 10 (Complying support)

Let m be the total number of users. The complying support of sequence α in database D is de<sup>fi</sup>ned as

$$
c m p \_ s u p (\alpha) = \sum_ {i = 1, m} u s u p _ {i} (\alpha) / m.\tag{3}
$$

A sequence α is called a complying sequence if it satis<sup>fi</sup>es the relationship cmp $. s u p ( \alpha ) { \geq } c m p$ \_minsup, where cmp\_minsup is a userspeci<sup>fi</sup>ed threshold.

Continuing from the previous example after De<sup>fi</sup>nition 9, the user's complying supports of sequence $\{ \mathsf { A } > \mathsf { B } \ge \mathsf { C } \}$ for user 1, user 2, and user 3 are 0.8, 0.33, and 0.17, respectively. Using Eq. (3), the complying support of sequence $\{ A > B \ge { \mathsf { C } } \} { \mathrm { ~ i s ~ } } 1 . 3 / 3 = 0 . 4 3$

## 3.11. Definition 11 (User's conflict support)

The con<sup>fl</sup>ict support of sequence α in user i's sequences is de<sup>fi</sup>ned as

$$
c f _ {-} u s u p _ {i} (\alpha) = \frac {| \{S _ {i , j} | S _ {i , j} \in S _ {i} \wedge \alpha \text {   is   conflict   with   } S _ {i , j} \} |}{| S _ {i} |}.\tag{4}
$$

For example, user 1's con<sup>fl</sup>ict support of sequence $\{ \mathsf { B } > \mathsf { A } \}$ is 4/5 in the sequence database of Table 2.

## 3.12. Definition 12 (Conflict support)

The con<sup>fl</sup>ict support of sequence α in database D is de<sup>fi</sup>ned as

$$
c f _ {-} \sup (\alpha) = \sum_ {i = 1, m} c f _ {-} u s u p _ {i} (\alpha) / m\tag{5}
$$

For example, assume that the user's con<sup>fl</sup>ict supports of sequence $\{ { \tt B } > { \tt A } \}$ for user 1, user 2, and user 3 are 0.8, 0.66 and 0.5, respectively. Using Eq. (5), the con<sup>fl</sup>ict support of sequence {B>A} is 0.65.

## 3.13. Definition 13 (Consensus sequence)

Let cmp\_minsup and cf\_maxsup be the user speci<sup>fi</sup>ed thresholds. A sequence cs is called a consensus sequence if it satis<sup>fi</sup>es the following constraints:

$$
\operatorname{cmp} _ {-} \sup (\mathrm{cs}) \geq \operatorname{cmp} _ {-} \text {   minsup   and   } \operatorname{cf} _ {-} \sup (\mathrm{cs}) * \operatorname{cf} _ {-} \max \sup.\tag{6}
$$

A consensus sequence cs is maximum if cs is not contained in any other consensus sequence.

## 3.14. Definition 14 (Conflicting items)

Let L denote the set of all consensus sequences with a minimum length of two. An item α is a con<sup>fl</sup>icting item if it does not appear in any sequence in L.

No consensus can be achieved regarding a con<sup>fl</sup>icting item. These items should be identi<sup>fi</sup>ed and further negotiated.

## 4. Methodology

In this section, we propose a new algorithm, called MCSP, to discover maximum consensus sequences. In Section 4.1, we give an overview of the MCSP algorithm. Then, in Section 4.2 we detail the process of candidate generation and counting supports, which is the most important and complicated part of our algorithm.

## 4.1. The MCSP algorithm

We propose an MCSP algorithm for mining maximum consensus sequences from all users' partial ranking lists. Parameters cmp\_minsup and $c f _ { - }$ maxsup, de<sup>fi</sup>ned in De<sup>fi</sup>nition 13, are used to <sup>fi</sup>lter out consensus sequences. A sequence with length k is referred to as a k-sequence. Let $L _ { k }$ denote the set of all k-consensus sequences, and $C _ { k }$ the set of candidate k-consensus sequences. To begin, we introduce the downward closure property, which is the foundation of the proposed algorithm.

## Lemma 1. (Downward closure)

All subsequences of a consensus sequence must be consensus sequences.

Proof. From De<sup>fi</sup>nition 5, we see that a subsequence's complying support cannot be smaller than its super-sequence's complying support. From De<sup>fi</sup>nition $6 ,$ we see that a subsequence's con<sup>fl</sup>ict support cannot be larger than its super-sequence's con<sup>fl</sup>ict support. Therefore, all subsequences of a consensus sequence must be consensus sequences.

The mining algorithm proceeds in phases, where the k-th phase determines $L _ { k } .$ The steps are given below. Maximum consensus sequence algorithm Input:

User database : D

Set of items: I

A user speci<sup>fi</sup>ed minimum complying support threshold: cmp\_minsup, A user speci<sup>fi</sup>ed maximum con<sup>fl</sup>icting support threshold : cf\_maxsup Output: maximum consensus sequences with complying support> cmp\_minsup and con<sup>fl</sup>icting support<cf\_maxsup

Method:

1. Generate large 1 consensus sequences $L _ { 1 }$ using function (I);

2. Generate large 2 consensus sequences $L _ { 2 }$ <sup>genL1</sup>using function (L1)

3. Repeatedly generate large k consensus sequences $L _ { k }$

$$
(k = 3; L _ {k - 1} \neq \phi ; k + +)
$$

C<sub>k</sub>= $\left( L _ { k - 1 } \right)$

$L _ { k } \{ c \in C _ { k } | c m p \_ s u p ( c ) \ge c m p _ { - }$ min sup, and $c f _ { - } s u p \left( c \right) \leq c f _ { - }$ \_ max sup} 4. Find maximum consensus sequences from al $L _ { k }$ by removing those consensus sequences contained in other consensus sequences.

5. Find con<sup>fl</sup>ict items by removing those items which are not contained in any sequence in $L _ { 2 } .$

Detailed explanation of the algorithm's steps:

(Step 1) $L _ { 1 }$ is generated using function ( ). Since users only <sup>genL1 I</sup>provide partial rankings, not all items will appear in the database. Therefore, items that do not appear in any user sequence can be removed.

(Step 2) The second phase uses function (L ). First, $C _ { 2 }$ is generated with $L _ { 1 } \oplus L _ { 1 } ,$ where $\oplus \in \{ > , \geq , = \}$ and their supports are computed by scanning the database. A sequence will be in $L _ { 2 }$ if its complying support and con<sup>fl</sup>ict support satisfy the support constraints. Along with each consensus sequence, there is a record of related information. The stored information indicates which users' sequences contain this pattern and the lengths of these sequences.

(Step 3) Through Lemma 1, we know that $C _ { k }$ can be generated from $L _ { k - 1 } .$ Therefore, we apply the function $g e n L k ( L _ { k - 1 } )$ to generate $C _ { k } .$ After obtaining $C _ { k } , L _ { k }$ is the set of candidates whose cmp\_sup and cf\_sup satisfy the support constraints. Step 3 terminates when there are no sequences after joining, or when there are no candidate (k+1)-sequences generated. Since the function genL $k ( L _ { k - 1 } )$ is very complicated, it will be described further in the next section.

(Step 4) After obtaining all consensus sequences, sequences contained in other, longer ones must be removed. This step is completed by cycling longer sequences to shorter sequences. When examining a sequence, we simply remove all its subsequences from the set of consensus sequences.

(Step 5) To <sup>fi</sup>nd con<sup>fl</sup>icting items, we look for items in I that do not appear in any consensus sequence in $L _ { 2 } .$ This can be easily done with a single examination of all sequences in L . The remaining ones are the con<sup>fl</sup>icting items.

Example 1. We apply the algorithm to the sequence database D in Table 2 with cmp\_minsup=0.3 and $c f \_ m a x s u p = 0 . 2 5$ . The entire process of the MCSP algorithm is shown in Fig. 2. The set of all items are $\{ \mathsf { A } , \mathsf { B } , \mathsf { C } , \mathsf { D } , \mathsf { E } , \mathsf { F } , \mathsf { G } \}$ . First, ${ \cal L } _ { 1 } = \{ \mathrm { A } , \mathrm { B } , \mathrm { C } , \mathrm { D } , \mathrm { E } , \mathrm { F } \}$ } is generated using genL $\pmb { 1 } ( I )$ . Item G is removed because it does not appear in any user <sup>genL1</sup>sequence. In step 2, we use $L _ { 1 }$ to generate $C _ { 2 }$ by applying the function $g e n L 2 ( L _ { 1 } )$ and scan the database to determine $L _ { 2 } . \Lambda$ set of consensus sequences are determined with thresholds cmp\_minsup and $c f _ { - }$ \_maxsup. As a result, $L _ { 2 }$ contains the following sequences: $\{ \mathsf { A } > \mathsf { B } \}$ $\{ \mathsf { A } > \mathsf { C } \} , \{ \mathsf { A } > \mathsf { D } \} , \{ \mathsf { A } > \mathsf { E } \} , \{ \mathsf { B } > \mathsf { C } \} , \{ \mathsf { B } \geq \mathsf { C } \} , \{ \mathsf { B } > \mathsf { D } \} , \{ \mathsf { B } > \mathsf { E } \} , \{ \mathsf { C } > \mathsf { D } \} , \{ \mathsf { D } > \mathsf { E } \}$ Repeating step 3 recursively would <sup>fi</sup>nd all consensus sequences. We generate $C _ { 3 }$ and use cmp\_minsup and $c f _ { - }$ \_maxsup to determine $L _ { 3 } .$ In this example, $L _ { 3 }$ contains $\{ A > B \geq C \} , \ \{ A > B > D \} , \ \{ A > C > D \}$ , and $\{ { \tt B } \ge { \tt C } > { \tt D } \}$ . Similarly, we generate $C _ { 4 }$ and determine $L _ { 4 } =$ $\{ \mathsf { A } { \scriptstyle > } \mathsf { B } { \scriptstyle \geq } \mathsf { C } { \scriptstyle > } \mathsf { D } \}$ . Step 3 <sup>fi</sup>nally terminates when $C _ { 5 }$ is generated since there is only one 4-sequence and $C _ { 5 }$ could not be generated. By identifying consensus sequences that are not contained in any longer consensus sequences, we obtain maximum consensus sequences $\{ A > E \} , \{ \mathrm { B } > C \} , \{ \mathrm { B } > \mathrm { E } \} , \{ \mathrm { D } > \mathrm { E } \} , \{ \mathrm { A } > \mathrm { B } \geq C > \mathrm { D } \}$ . Also, we <sup>fi</sup>nd con<sup>fl</sup>icting item F because it did not appear in any sequence in $L _ { 2 } .$

## 4.2. Candidate generation and counting support

In this section, we discuss how to generate $C _ { k }$ from $L _ { k - 1 } ,$ where $k > 2 ,$ and how to compute the support of sequences in $C _ { k } .$ Based on some important properties that will be introduced later in this section, the support of these candidate sequences can be computed using the information already stored in the main memory; therefore, it is not necessary to scan the database. In this way, the ef<sup>fi</sup>ciency of the support counting procedure is greatly improved.

Before presenting the details of this procedure, we <sup>fi</sup>rst introduce several important properties in the following lemmas. Lemmas 2 and 3 are properties regarding the con<sup>fl</sup>icting sequence and con<sup>fl</sup>ict support counting, while Lemmas 4 and 5 are about the complying sequence and complying support counting. These lemmas indicate that we can compute the con<sup>fl</sup>ict supports and the complying supports of sequences in $C _ { k }$ directly from information stored in $L _ { k - 1 } .$ As a result, no database scan is needed when computing support.

Lemma 2. (Property of the con<sup>fl</sup>ict sequence) Let $\alpha = \alpha _ { 1 } \otimes \alpha _ { 2 }$ , where $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are in $L _ { k - 1 }$ and ⊗ is the joining operation that generates $C _ { k }$ from $L _ { k - 1 }$ . Then, user sequences $\beta$ that con<sup>fl</sup>ict with α must con<sup>fl</sup>ict with either $\alpha _ { 1 } , \alpha _ { 2 }$ or both.

Proof. Assume that $\alpha = \alpha _ { 1 } \otimes \alpha _ { 2 } \stackrel { } { = } a _ { 1 } \oplus _ { 1 } . . . \oplus _ { k } a _ { k }$ where $\alpha _ { 1 } = a _ { 1 } \oplus _ { 1 } . . .$ $\oplus _ { k - 2 } a _ { k - 1 }$ and $\alpha _ { 2 } = a _ { 2 } \oplus _ { 2 } . . . \oplus _ { k - 1 } a _ { k } .$ Since $\beta$ con<sup>fl</sup>icts with α, the con<sup>fl</sup>ict must occur somewhere in α. If the con<sup>fl</sup>ict occurs entirely in α or entirely in $\alpha _ { 2 } ,$ then this corresponds with the lemma. Let us assume that the con<sup>fl</sup>ict does not occur in $\alpha _ { 1 } \ o r \alpha _ { 2 } ,$ but only occurs in $\alpha _ { 1 } \otimes \alpha _ { 2 } .$ . Then, the only possibility in this situation is that the con<sup>fl</sup>ict occurs in $R e l ( a _ { 1 } , a _ { k } , \alpha )$ . In other words, $R e l ( a _ { 1 } , a _ { k } , \alpha )$ con<sup>fl</sup>icts with Rel $( a _ { 1 } , a _ { k } , \beta )$ . The following observations, however, indicate that this is impossible: $\mathrm { ( i ) } \ R e l ( a _ { 1 } , a _ { k - 1 } , \alpha )$ does not con<sup>fl</sup>ict with $R e l ( a _ { 1 } , a _ { k - 1 } , \beta )$ because the con<sup>fl</sup>ict does not occur in $\alpha _ { 1 } ; ( \mathrm { i i } ) R e l ( a _ { k - 1 } , a _ { k } , \alpha )$ does not con<sup>fl</sup>ict with $R e l ( a _ { k - 1 } , a _ { k } , \beta )$ because the con<sup>fl</sup>ict does not occur in $\alpha _ { 2 } ;$

![](/api/attachments/6FDEJU8U/fulltext/images/cd5d44620339e8161d4693d6d81a5a256be4ac9233df815c2c4ab8b43e7104af.jpg)  
Fig. 2. Entire MCSP algorithm process (grey boxes indicate the maximum consensus sequences).

(iii) From (i) and (ii), we conclude that $R e l ( a _ { 1 } , a _ { k } , \alpha )$ does not con<sup>fl</sup>ict with $R e l ( a _ { 1 } , a _ { k } , \beta )$

Through Lemma 2, we can derive the following lemma.

Lemma 3. (Con<sup>fl</sup>ict support) Let $\alpha = \alpha _ { 1 } \otimes \alpha _ { 2 } .$ For user i, let A be the sequences of user i that con<sup>fl</sup>ict with $\alpha _ { 1 } , \mathrm { i } . e . , \left\{ S _ { i , j } \right\} S _ { i , j } { \in } S _ { i } \wedge \alpha _ { 1 }$ con<sup>fl</sup>icts with $S _ { i , j } \}$ , and B be the sequences of user i that con<sup>fl</sup>ict with $\alpha _ { 2 } , \mathrm { i } . \mathrm { e } . , \{ S _ { i , j } \}$ $S _ { i , j } { \in } S _ { i } \wedge \alpha _ { 2 }$ con<sup>fl</sup>icts with $S _ { i , j } \}$ . Then, the con<sup>fl</sup>ict support of sequence α in user i's sequences is

$$
c f _ {-} u s u p _ {i} (\alpha) = \frac {| A \cup B |}{| S _ {i} |}\tag{7}
$$

Lemma 2 indicates that if a sequence con<sup>fl</sup>icts with $\alpha$ , it will also con<sup>fl</sup>ict with either $\alpha _ { 1 , \ } \alpha _  2 , $ or both. Furthermore, we see from Lemma $^ { 3 , }$ that if we store user i's sequence identi<sup>fi</sup>ers that con<sup>fl</sup>ict with $\alpha _ { 1 }$ and $\alpha _ { 2 , }$ along with $L _ { k - 1 } ,$ we can compute the con<sup>fl</sup>ict support of user i using the union of these two sets.

Lemmas 4 and 5 are properties concerning the complying sequence, which can simplify the process of complying support counting.

## Lemma 4. (Property of complying sequence)

Let $\alpha = \alpha _ { 1 } \otimes \alpha _ { 2 }$ where $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are in $L _ { k - 1 }$ and ⊗ is the joint operation to generate $C _ { k }$ from $L _ { k - 1 }$ . If both $\alpha _ { 1 }$ and $\alpha _ { 2 }$ comply with user sequences $\beta ,$ then α must comply with $\beta .$

## Proof. Similar to that of Lemma 2.

Through Lemma 4, we can derive the following lemma.

Lemma 5. (Complying support)

Let $\alpha = \alpha _ { 1 } \otimes \alpha _ { 2 }$ . For user i, le $A = \{ S _ { i , j } | S _ { i , j } \in S _ { i } \wedge { }$ α complies with $S _ { i , j } \}$ and $B = \{ S _ { i , j } | \ S _ { i , j } \in S _ { i } \ \wedge \ \alpha _ { 2 }$ complies with $S _ { i , j } \}$ . The comply support of sequence α in user i's sequences is

$$
c m p _ {-} u s u p _ {i} (\alpha) = \frac {| A \cap B |}{| S _ {i} |}.\tag{8}
$$

Lemma 4 indicates that if a sequence complies with $\alpha _ { 1 }$ and $\alpha _ { 2 } ,$ then it must comply with α. Furthermore, we see from Lemma 5 that if we store user i's sequence identi<sup>fi</sup>ers that comply with α and α along with $L _ { k - 1 }$ , we can compute the complying support of user i using the intersection of these two sets.

In general, $C _ { k }$ can be generated with $L _ { k - 1 } \otimes L _ { k - 1 } ,$ , where denotes joining. From Lemmas 2 and 4, we will join two sequences $s _ { 1 }$ and $s _ { 2 }$ in $L _ { k - 1 }$ if the subsequence obtained by dropping the <sup>fi</sup>rst element of $s _ { 1 }$ is the same as the subsequence obtained by dropping the last element of $s _ { 2 } .$ . During the joining phase, we use a buffer to record related information for each sequence s in $L _ { k - 1 } .$ Let $C o m _ { s } ^ { i }$ denote the set of sequences for user i that comply with s, Conflict<sup>i</sup> denote the set of sequences for user i that con<sup>fl</sup>ict with $s ,$ and $| S _ { i } |$ be the number of sequences for user i. Then, the buffer contains the sequence numbers for Com<sub>s</sub><sup>i</sup>, Conflict<sub>s</sub><sup>i</sup>, and |S<sub>i</sub>| for each user i. According to Lemmas 3 and $5 ,$ there is no need to scan the database repeatedly to count the complying supports and con<sup>fl</sup>ict supports, cmp\_usup (α) and cf\_usup (α). Example 2 demonstrates the steps in detail.

Example 2. Fig. 3 illustrates the support counting process in the mining algorithm. In this example, there are two large sequences $s _ { 1 } , s _ { 2 } \in L _ { 3 } ,$ where $s _ { 1 } = \{ { \mathsf { A } } > { \mathsf { B } } \geq { \mathsf { C } } \}$ and $s _ { 2 } = \{ \mathsf { B } \geq \mathsf { C } > \mathsf { D } \}$ . Fig. 3 shows how to generate candidate sequence $C = s _ { 1 } \otimes s _ { 2 } = \{ \mathsf { A } > \mathsf { B } \geq \mathsf { C } > \mathsf { D } \}$ in $C _ { 4 }$ and determine its supports with the union and intersection operations. Using De<sup>fi</sup>nition 10, we have cmp $s u p = ( 4 / 5 + 1 / 6 + 0 ) / 3 = 0 . 3 2 .$ . Also, using De<sup>fi</sup>nition 12, we have $\scriptstyle \mathtt { \mathtt { = } f _ { - } } u s u p = ( 1 / 5 + 0 + 2 / 6 ) / 3 = 0 . 1 7 7 .$

<table><tr><td>Sequence,  $S_I$ </td><td colspan="4">buffer</td></tr><tr><td rowspan="4">A&gt;B≥C</td><td>User number</td><td> $Com_{s_1}^i$ </td><td> $Conflict_{s_1}^i$ </td><td>|Si|</td></tr><tr><td>1</td><td>{2,3,4,5}</td><td>{1}</td><td>5</td></tr><tr><td>2</td><td>{1,3}</td><td>{}</td><td>6</td></tr><tr><td>3</td><td>{3}</td><td>{5}</td><td>6</td></tr><tr><td colspan="5">Join</td></tr><tr><td>Sequence,  $S_2$ </td><td colspan="4">buffer</td></tr><tr><td rowspan="4">B≥C&gt;D</td><td>User number</td><td> $Com_{s_2}^i$ </td><td> $Conflict_{s_2}^i$ </td><td>|Si|</td></tr><tr><td>1</td><td>{2,3,4,5}</td><td>{}</td><td>5</td></tr><tr><td>2</td><td>{2,3,5}</td><td>{}</td><td>6</td></tr><tr><td>3</td><td>{2}</td><td>{4}</td><td>6</td></tr><tr><td colspan="5">Lemma 5 Lemma 3</td></tr><tr><td>Candidate, C</td><td>User number</td><td> $Com_C^i$ </td><td> $Conflict_C^i$ </td><td>|Si|</td></tr><tr><td rowspan="3">A&gt;B≥C&gt;D</td><td>1</td><td>{2,3,4,5}</td><td>{1}</td><td>5</td></tr><tr><td>2</td><td>{3}</td><td>{}</td><td>6</td></tr><tr><td>3</td><td>{}</td><td>{4,5}</td><td>6</td></tr></table>

Fig. 3. Support counting process in the mining algorithm.

## 5. Experimental results

To evaluate the ef<sup>fi</sup>ciency and effectiveness of the proposed MCSP algorithm we performed several experiments using synthetic data sets. In this section, we describe the generation of the synthetic data set and the experimental settings. The proposed algorithm was implemented in Java language and tested on an Intel Celeron 2.6 GHz PC with 2 gigabytes of main memory running the Windows 2000 operating system.

## 5.1. Synthetic data generation

In the following experiments, we generated several synthetic data sets composed of incomplete sequences. The parameters used in our data generation algorithm are listed in Table 4. The data generation process is described below.

Each synthetic data set contains |U| users and each user has an average of eight user sequences, where a user sequence is an ordered list of items. In the following, we discuss how each user sequence is generated. Initially, a seed sequence containing twenty-<sup>fi</sup>ve items is randomly generated. We used parameters mr and sr, missing rate and swap rate respectively, to generate partial ranking lists from the seed sequences. Missing rate determines what percentage of items in the seed sequences will be removed, while swap rate determines how many items in the sequences will be swapped. In other words, a user sequence is generated in two steps. (1) We randomly select mr% of items from the seed sequence and eliminate them, and (2) we choose sr% of items for a swap. Therefore, a higher missing rate indicates more incomplete ranked lists, and a higher swap rate indicates more con<sup>fl</sup>icts. Table 5 shows the parameter settings of different synthetic data generations.

Parameters of data generation.

<table><tr><td>Parameters</td><td>Description</td></tr><tr><td>|U|</td><td>Number of users</td></tr><tr><td>|I|</td><td>Number of items per seed sequence</td></tr><tr><td>mr</td><td>Missing rate</td></tr><tr><td>sr</td><td>Swap rate</td></tr></table>

## 5.2. Run time comparisons and pattern comparisons

We compared the run times of the data sets with different parameter settings and show the number of discovered patterns. These comparisons were based on the <sup>fi</sup>rst four data sets in Table 5: SYN-01–SYN-04.

Con<sup>fi</sup>gurations of synthetic data sets.

<table><tr><td>ID</td><td>Name</td><td>|U|</td><td>|I|</td><td>mr</td><td>sr</td></tr><tr><td>SYN-01</td><td>U1000-I25-mr0.2</td><td>1000</td><td>25</td><td>20%</td><td>-</td></tr><tr><td>SYN-02</td><td>U1000-I25-mr0.4</td><td>1000</td><td>25</td><td>40%</td><td>-</td></tr><tr><td>SYN-03</td><td>U1000-I25-sr0.2</td><td>1000</td><td>25</td><td>-</td><td>20%</td></tr><tr><td>SYN-04</td><td>U1000-I25-sr0.4</td><td>1000</td><td>25</td><td>-</td><td>40%</td></tr><tr><td>SYN-05</td><td>U1000-I50-mr0.3</td><td>1000</td><td>50</td><td>30%</td><td>-</td></tr><tr><td>SYN-06</td><td>U500-I75-mr0.3sr0.4</td><td>500</td><td>75</td><td>30%</td><td>40%</td></tr><tr><td>SYN-07</td><td>U500-I50-mr0.3sr0.4</td><td>500</td><td>50</td><td>30%</td><td>40%</td></tr><tr><td>SYN-08</td><td>U500-I25-mr0.3sr0.4</td><td>500</td><td>25</td><td>30%</td><td>40%</td></tr><tr><td>SYN-09</td><td>U500-I75-mr0.4sr0.4</td><td>500</td><td>75</td><td>40%</td><td>40%</td></tr><tr><td>SYN-10</td><td>U500-I50-mr0.4sr0.4</td><td>500</td><td>50</td><td>40%</td><td>40%</td></tr><tr><td>SYN-11</td><td>U500-I25-mr0.4sr0.4</td><td>500</td><td>25</td><td>40%</td><td>40%</td></tr><tr><td>SYN-12</td><td>U1000-I25-mr0.4sr0.3</td><td>1000</td><td>25</td><td>40%</td><td>30%</td></tr><tr><td>SYN-13</td><td>U5000-I25-mr0.4sr0.3</td><td>5000</td><td>25</td><td>40%</td><td>30%</td></tr><tr><td>SYN-14</td><td>U7000-I25-mr0.4sr0.3</td><td>7000</td><td>25</td><td>40%</td><td>30%</td></tr><tr><td>SYN-15</td><td>U1000-I25-mr0.3sr0.3</td><td>1000</td><td>25</td><td>30%</td><td>30%</td></tr><tr><td>SYN-16</td><td>U5000-I25-mr0.3sr0.3</td><td>5000</td><td>25</td><td>30%</td><td>30%</td></tr><tr><td>SYN-17</td><td>U7000-I25-mr0.3sr0.3</td><td>7000</td><td>25</td><td>30%</td><td>30%</td></tr></table>

![](/api/attachments/6FDEJU8U/fulltext/images/b4e0136798e2bcf92d1456da2365e31a303c7e0c918a7c019234ed022a801fec.jpg)  
(c) SYN-03 (sr = 0.2, com\_minsup = 0.35)

(b) SYN-02 (mr = 0.4, com\_minsup = 0.35)  
![](/api/attachments/6FDEJU8U/fulltext/images/f9be4f88fef4c2a396498ce438ae7529d89c2dc817715926ee782701af7b54b6.jpg)

![](/api/attachments/6FDEJU8U/fulltext/images/bb77768a654eedb8af8cd363d830959fb1b7584929e23ab2cad9045351369c5a.jpg)

(d) SYN-04 (sr = 0.4, com\_minsup = 0.35)  
![](/api/attachments/6FDEJU8U/fulltext/images/6c490c518808e9d7c022508dadc8d6c187558c7680732c24396e972360e19804.jpg)  
Fig. 4. Effects of cf\_maxsup on the run time performance when com\_minsup =0.35.

The effects of maximum con<sup>fl</sup>ict support, minimum complying support, and the numbers of discovered patterns were considered.

## 5.2.1. Effects of maximum conflict support

We set the minimum complying support at 0.35 and varied the maximum con<sup>fl</sup>ict support from 0.05 to 0.2. The in<sup>fl</sup>uence of maximum con<sup>fl</sup>ict support on MCSP's run time performance is shown in Fig. 4. In this <sup>fi</sup>gure, the x-axis and y-axis represent the maximum con<sup>fl</sup>ict support and the run time, respectively. We observed some interesting results.

As shown in these <sup>fi</sup>gures, all results indicate that the run time increases as the maximum con<sup>fl</sup>ict support threshold increases. This is because when cf\_maxsup is larger, it is easier for a sequence to satisfy the constraint and more candidate sequences are generated.

As stated previously, when mr and sr are larger, user sequences become more incomplete and con<sup>fl</sup>icting, making it more dif<sup>fi</sup>cult to reach consensus. The results in Fig. 4 indicate that the run time increases as mr or sr decreases. This is because when mr or sr decreases, it is easier to reach consensus; thus, more candidates are generated, which increases run time.

## 5.2.2. Effects of minimum comply support

In the next experiment, we set cf\_maxsup=0.15 and varied the minimum complying support, com\_minsup, from 0.2 to 0.6. The effects of minimum complying support on MCSP's run time performance is shown in Fig. 5. In this <sup>fi</sup>gure, the x-axis and y-axis represent the minimum complying support and the run time, respectively. The results show that as com\_minsup increases, the run time decreases. This is because as com\_minsup increases, fewer candidate sequences are generated, decreasing the run time.

## 5.2.3. Number of discovered patterns

Fig. 6 shows the number of patterns discovered by the proposed algorithms for the same four data sets from Fig. 4. In Fig. 6, the x-axis and y-axis represent the lengths of sequences and the number of sequences, respectively.

From Fig. 6, we see that as mr and sr decrease, the number of longer consensus patterns increases. This is because when mr and sr are lower, user sequences are more similar. Therefore, when mr and sr are lower, more consensuses are achieved, which increases the number of longer consensus patterns.

In addition, we observe that as mr and sr increase, the consensus list becomes shorter. This result is reasonable because when mr and sr are large, it is more dif<sup>fi</sup>cult to achieve consensus. Between mr and sr, however, we <sup>fi</sup>nd that mr has a greater impact on the length of maximum consensus lists.

The numbers of maximum consensus sequences and con<sup>fl</sup>icting items discovered by the proposed algorithms for data sets SYN-02 and SYN-05 are illustrated in Fig. 7. In this <sup>fi</sup>gure, the bar chart and line graph represent the numbers of maximum consensus sequences and con<sup>fl</sup>icting items, respectively. Fig. 7(a) and (b) shows the effects of maximum con<sup>fl</sup>ict support on patterns discovered. As one can see, the number of maximum consensus sequences increases as the maximum con<sup>fl</sup>ict support increases. The number of con<sup>fl</sup>icting items, however, remains steady.

As seen in Fig. 7(c) and (d), the number of maximum consensus sequences decreases rapidly as the minimum complying support increases. On the other hand, the number of con<sup>fl</sup>icting items increases as the minimum complying support increases from 0.2 to 0.6. This matches our predictions because the larger the minimum complying support, the fewer generated candidates.

## 5.3. Scalability

This section investigates the scalability of the MCSP algorithm. The <sup>fi</sup>rst part of the experiment concerns the number of users, |U|, and the second part concerns the number of items per seed sequence, |I|.

In scaling up |U|, the comparison was based on datasets SYN-12– SYN-17 from Table 5. We varied the number of users from 1000 to 7000 and set com\_minsup=0.4 and cf\_maxsup=0.05. The x-axis and y-axis represent the number of users and the run time, respectively. As seen in Fig. 8(a), MCSP's run time increases linearly with the number of users.

(a) SYN-01 (mr = 0.2, cf\_maxsup = 0.15)  
![](/api/attachments/6FDEJU8U/fulltext/images/303ae16bd4613168666d8074446453f2a83ca0b0ca30a8922833fa380c462c4d.jpg)  
(c) SYN-03 (sr = 0.2 , cf\_maxsup = 0.15)

(b) SYN-02 (mr = 0.4, cf\_maxsup = 0.15)  
![](/api/attachments/6FDEJU8U/fulltext/images/6907f888dedb028a8f2f7d90c94f949ed826fe1eef4d4187f294eae440865b44.jpg)

![](/api/attachments/6FDEJU8U/fulltext/images/0a79718699c40d0c2c60011210a507bd1dec9ff7b8d70f2f96de626000c0dd6b.jpg)

(d) SYN-04 (sr = 0.4, cf\_maxsup = 0.15)  
![](/api/attachments/6FDEJU8U/fulltext/images/c6d4bc75f4ce7601d76a847f172b20bd3026c17abec7f99e5f6cb94d736728b3.jpg)  
Fig. 5. Effects of com\_minsup on the run time performance when cf\_maxsup = 0.15.

In Fig. 8(b), the comparison was based on data sets SYN-6–SYN-11 from Table 5. We varied the value of |I| from 25 to 75 and <sup>fi</sup>xed cf\_maxsup =0.05 and cmp\_minsup =0.5. The x-axis and y-axis represent the number of items and the run time, respectively. This <sup>fi</sup>gure shows that the algorithm's run time grows exponentially with |I|.

(a) SYN-01 (com\_minsup = 0.35 cf\_maxsup = 0.05)  
![](/api/attachments/6FDEJU8U/fulltext/images/973ece1828e21f5014ee9cfb50fccabe9914ee32e4ed73f557224f10c69b866b.jpg)

(b) SYN-02 (com\_minsup = 0.35 cf\_maxsup = 0.05)  
![](/api/attachments/6FDEJU8U/fulltext/images/af932b4a0c2a58bd2d956baa12c732337f3ceff39d8e37c6accb67eb7529439b.jpg)

(c) SYN-03 (com\_minsup = 0.35 cf\_maxsup = 0.05)  
![](/api/attachments/6FDEJU8U/fulltext/images/3a1a87c8eedc166eb15bf7e479f58265f5a3848fa35c693cfe1816b80b738c37.jpg)

(d) SYN-04 (com\_minsup = 0.35 cf\_maxsup = 0.05)  
![](/api/attachments/6FDEJU8U/fulltext/images/80557d6b3c83d3c409ae99514c48f75295c8614bc9ce21b415afdf9e6931e23f.jpg)  
Fig. 6. Number of patterns discovered by the proposed algorithms

![](/api/attachments/6FDEJU8U/fulltext/images/4e01cd39219ac891430f9d659e3ca970ec8faeb02a05b8b7f3dadef178fbb465.jpg)

![](/api/attachments/6FDEJU8U/fulltext/images/96d5533e33937fdcd8db77d2281f17e83b34aaea7f3f059b21f67d567491e0e2.jpg)

(c)  
![](/api/attachments/6FDEJU8U/fulltext/images/39e210c396a144ee17ab8db93aa750bf1c27f94f1e32f525c5b9f0b73d8322ef.jpg)

![](/api/attachments/6FDEJU8U/fulltext/images/2714c472b2ad64cecdb7936142accccb769112a209ee46fa984ec88d47048cc3.jpg)  
Fig. 7. Number of patterns discovered by the proposed algorithms.

## 6. Illustrative example

In this section, we discuss how the proposed algorithm is used in the decision process and evaluate the effectiveness of the methods. We collected movie preference data for 10 users and 10 movies. Each user provided many ranked list of items in which ties are allowed. The movies are listed in Table 6. Table 7 shows the users' sequences database.

The parameter settings were cmp\_minsup=0.5 and cf\_maxsup=0.2. In addition, the maximum consensus sequences discovered by the algorithms are summarized in Fig. 9. A directed graph is used to express relationships among items. Each node represents an item, and a solid directional arc between items a and b means that users prefer a over b. Our investigation indicates that items can be clustered into two groups: a consensus group and a con<sup>fl</sup>ict group. A consensus group means that a majority of users agree upon the relationships between items. On the other hand, those having no consensus on the items are grouped into a con<sup>fl</sup>ict group. For example, items E and F are con<sup>fl</sup>ict items. Those from the consensus groups like action/adventure movies more than romantics. For example, (G>D>J) and (H>D>I) are two such sequences.

The consensus graph is obtained from the maximum consensus patterns. This graph provides useful clues for marketing and decision making. The patterns are indicative of the interest of the people during this period of time. The graph can be used for product recommendations. When a user buys or inquires about a product, we can recommend to the user other products that precede it in the graph. This is because when an item precedes another item in the consensus graph, it means that most users like the preceding item more than the succeeding one. Furthermore, by comparing two consensus graphs generated at two different times, we can observe how preferences change over time, where a preference is a connected subgraph consisting of at least two items. A preference can be classi<sup>fi</sup>ed as invariant if it exists in both consensus graphs, as emerging if it only exists in the new graph, as obsolete if it only exists in the old graph, as increasing if it exists in both graphs but its support has increased signi<sup>fi</sup>cantly in the new graph, and as declining if its support has decreased signi<sup>fi</sup>cantly in the new graph.

![](/api/attachments/6FDEJU8U/fulltext/images/0969ca1c00e0c8e6f614a9705174fbdb02d7bd38632619d419470ec2b62c56c0.jpg)

(b)  
![](/api/attachments/6FDEJU8U/fulltext/images/4484a3c3a568d74a28ded1f691958640e9de9e4d1cd0f7a09d71b4a29a71fefc.jpg)  
Fig. 8. Scalability of the proposed algorithms for |U| and |I|.

Table 6 The movies.

<table><tr><td>Item number</td><td>List of movies</td></tr><tr><td>A</td><td>The Lord of the Rings: The Fellowship of the Ring</td></tr><tr><td>B</td><td>Transformers</td></tr><tr><td>C</td><td>Sex and the City</td></tr><tr><td>D</td><td>The Curious Case of Benjamin Button</td></tr><tr><td>E</td><td>The Terminal</td></tr><tr><td>F</td><td>Harry Potter and the Order of the Phoenix</td></tr><tr><td>G</td><td>Star Wars</td></tr><tr><td>H</td><td>Spider-Man</td></tr><tr><td>I</td><td>High School Musical 2</td></tr><tr><td>J</td><td>Brokeback Mountain</td></tr></table>

In addition, the contradictory opinions of the con<sup>fl</sup>ict items show that these items are not suitable for mass marketing: rather, we should search for users who like these con<sup>fl</sup>ict items and do one-toone marketing for this group of potential customers. Finally, if necessary to obtain a consensus for all items, users should negotiate with each other to mitigate the differences of opinions on these con<sup>fl</sup>ict items.

## 7. Conclusions

Generally, traditional group ranking problems can be classi<sup>fi</sup>ed according to the completeness of the user-provided preference information, the types of compromise outcomes, and the format used to express user preferences. In this work, we add a new dimension to the traditional group ranking problem by classifying the input mode as either static or dynamic, depending on whether users provide their preferences all at once or at multiple times. We expect that this will open the door to many new variants of the group ranking problem in future. However, since it is impossible to address all possible issues at once, in this study we aim at solving a particular variant of the group ranking problem, i.e., the maximum consensus mining problem, where the maximum consensus is de<sup>fi</sup>ned as the longest ranking lists of alternatives that agree with the majority and disagree only with the minority.

To do this, we relax the input requirement by using multiple incomplete rankings to represent users' preferences. This method is more intuitive and <sup>fl</sup>exible. A novel algorithm is also proposed for <sup>fi</sup>nding all maximum consensus patterns. To verify the ef<sup>fi</sup>ciency and effectiveness of this algorithm, experiments are performed using several synthetic data sets. The results indicate that the proposed method is ef<sup>fi</sup>cient and demonstrates that our approach can effectively identify the consensus among all users.

There are two limitations in this study. One is that, although sequences are submitted at different times, they are given the same weights. This is not reasonable because sequences that come more recently should be weighted more heavily than older ones. The discovery of the maximum consensus sequences with consideration that sequences are weighted differently according to their timestamps could be a direction of future research. Another limitation is that with the dynamic input mode not all users are active throughout the whole time interval. In other words, some users may only be active during a part of the interval. It is thus not fair to weight all users equally. Therefore, a possible research direction would be to reconsider the problem of mining maximum consensus sequences under the condition that users may be assigned different weights according to their active periods.

Table 7  
Users' sequences database.

<table><tr><td rowspan="3">User 1</td><td>B = H &gt; F &gt; C = D &gt; I &gt; J</td><td rowspan="2">User 6</td><td>A = F &gt; G &gt; H &gt; C = D</td></tr><tr><td>B &gt; F &gt; G &gt; D &gt; E &gt; I</td><td>G &gt; F = H &gt; D &gt; E &gt; I</td></tr><tr><td>B &gt; D &gt; E = I</td><td>User 7</td><td>B = H &gt; A = G &gt; C = D</td></tr><tr><td rowspan="2">User 2</td><td>H &gt; A = F &gt; C &gt; G &gt; D &gt; I &gt; J</td><td rowspan="2"></td><td>B &gt; A = F &gt; G &gt; D &gt; E &gt; I</td></tr><tr><td>H &gt; F &gt; G &gt; D = E &gt; I</td><td>B = H &gt; C &gt; E = J</td></tr><tr><td rowspan="3">User 3</td><td>B = H &gt; F &gt; A &gt; C = D &gt; I &gt; J</td><td rowspan="2">User 8</td><td>A = F &gt; G &gt; B &gt; C = D</td></tr><tr><td>B &gt; A = F &gt; G &gt; D = E &gt; I</td><td>F &gt; G &gt; B = H &gt; D &gt; E &gt; I</td></tr><tr><td>B &gt; C &gt; E = J</td><td>User 9</td><td>H &gt; C &gt; D &gt; F &gt; A &gt; I &gt; J</td></tr><tr><td rowspan="2">User 4</td><td>B &gt; A = F &gt; G &gt; C = D &gt; I &gt; J</td><td rowspan="2"></td><td>D &gt; E &gt; B = F &gt; A &gt; G &gt; I</td></tr><tr><td>B = F = H = F &gt; G &gt; C &gt; E &gt; I</td><td>A &gt; C &gt; B = E &gt; F &gt; J</td></tr><tr><td rowspan="3">User 5</td><td>B = H &gt; A &gt; C = D</td><td rowspan="3">User 10</td><td>H &gt; F = A &gt; G &gt; C = D &gt; I &gt; J</td></tr><tr><td>B &gt; A = F &gt; G &gt; D = E &gt; I</td><td>B = F = H &gt; G &gt; D &gt; E &gt; I</td></tr><tr><td>B &gt; A = H &gt; D &gt; I &gt; J</td><td></td></tr></table>

![](/api/attachments/6FDEJU8U/fulltext/images/e7c66cdb690c6a4dbab560ed3627e79f498de30656d59aa0edb23a4273b50dad.jpg)  
Fig. 9. Results for case study.

It is easy to see many future extensions along this line. It is common knowledge there are already many variants of the group ranking problem. However, all previous variants have used the static input mode. It is becoming increasingly necessary to allow user preference data to be input at multiple times, for example in e-survey systems or for Web 2.0 sites. The static input mode is no longer suitable for these modern applications. If we change the input mode of these traditional approaches from static to dynamic, we believe that this will open the door to a large array of future research issues.

## Acknowledgement

It is our pleasure to acknowledge the anonymous reviewers for their valuable suggestions and the careful reading of our manuscript. The authors would like to express their gratitude to these reviewers for their suggestions that helped substantially improve our paper. This study was supported by the National Science Council of Taiwan under grant No. NSC 97-2410-H-031-056.

## References

[1] J. Bartholdi, C.A. Tovey, M.A. Trick, Voting schemes for which it can be dif<sup>fi</sup>cult to tell who won the election, Social Choice and Welfare 6 (2) (1989) 157–165.

[2] M.M.S. Beg, N. Ahmad, Soft computing techniques for rank aggregation on the World Wide Web, World Wide Web-Internet and Web Information Systems 6 (1) (2003) 5-22

[3] K. Bogart, Preference structures I: distances between transitive preference relations, Journal of Math Sociology 3 (1973) 49–67.

[4] K. Bogart, Preference structures II: distances between asymmetric relations, SIAM Journal of Applied Math 29 (2) (1975) 254–265.

[5] J.C. Borda, Memoire sur les elections au scrutin, Histoire de l'Academie Royale de Science, Paris, 1981.

[6] Y.L. Chen, L.C. Cheng, A novel collaborative <sup>fi</sup>ltering approach for recommending ranked items, Expert Systems with Applications 34 (4) (2008) 2396–2405.

[7] Y.L. Chen, L.C. Cheng, Mining maximum consensus sequences from group ranking data, European Journal of Operational Research 198 (1) (2009) 241–251.

[8] W. Cohen, Learning to order things, Journal of Arti<sup>fi</sup>cial Intelligence Research 10 (1999) 243.

[9] W.D. Cook, Distance-based and ad hoc consensus models in ordinal preference ranking, European Journal of Operational Research 172 (2) (2006) 369–385.

[10] W.D. Cook, M. Kress, L. Seiford, An axiomatic approach to distance on partial orders, Revue Automatique, Informatique et Recherche Operationnelle 20 (2) (1986) 115–122.

[11] W.D. Cook, M. Kress, L. Seiford, Information and preference in partial orders: a bimatrix representation, Psychometrika 51 (2) (1986) 197–207.

[12] W.D. Cook, M. Kress, L. Seiford, A general framework for distance-based consensus in ordinal ranking models, European Journal of Operational Research 96 (1996) 392-397

[13] W.D. Cook, B. Golany, M. Kress, M. Penn, T. Raviv, Optimal allocation of proposals to reviewers to facilitate effective ranking, Management Science 51 (4) (2005) 655-661

[14] W.D. Cook, B. Golany, M. Kress, M. Penn, T. Raviv, Creating a consensus ranking of proposals from reviewer's partial ordinal rankings, Computers & OR 34 (4) (2007) 954–965.

[15] S. Damart, L.C. Dias, V. Mousseau, Supporting groups in sorting decisions: methodology and use of a multi-criteria aggregation/disaggregation DSS, Decision Support Systems 43 (4) (2007) 1464–1475.

[16] R. Fagin, R. Kumar, D. Sivakumar, Ef<sup>fi</sup>cient similarity search and classi<sup>fi</sup>cation via rank aggregation, Proceedings of the ACM SIGMOD international conference on management of data, ACM, San Diego, California, 2003, pp. 301–312.

[17] E. Fernandez, R. Olemdo, An agent model based on ideas of concordance and discordance for group ranking problems, Decision Support Systems 39 (3) (2005) 429.

[18] B. Golden, The analytic hierarchy process: applications and studies, Springer, New York NY, 1989.

[19] J. Gonzalez-Pachon, C. Romero, Aggregation of partial ordinal rankings: an interval goal programming approach, Computers and Operations Research 28 (8) (2001) 827–834.

[20] S. Greco, V. Mousseau, R. Slowinski, Ordinal regression revisited: multiple criteria ranking using a set of additive value functions, European Journal of Operational Research 191 (2) (2008) 416–436.

[21] D.S. Hochbaum, A. Levin, Methodologies and algorithms for group-ranking decision, Management Science 52 (9) (2006) 1394–1408.

![](/api/attachments/6FDEJU8U/fulltext/images/50c27b6b8e3fb5b28536a91c5d78623fabb51b72df99ee93aa91e9326cafecf8.jpg)

[22] J.G. Kemeny, L.J. Snell, Preference ranking: an axiomatic approach, Proceedings of mathematical models in the social science, 1962, pp. 9–23.

[23] M. Kendall, Rank correlation methods, ThirdHafner, New York, 1955.

[24] F.D. Robert, H.F. Ernest, Group decision support with the analytic hierarchy process, Decision Support System 8 (2) (1992) 99–124.

[25] T.L. Saaty, Rank generation, preservation, and reversal in the analytic hierarchy decision process, Decision Sciences 18 (2) (1987) 157.

[26] S. Saint, J.R. Lawson, Rules for Reaching Consensus: A Modern Approach to Decision Making, Pfeiffer & Company, 1994.

![](/api/attachments/6FDEJU8U/fulltext/images/eb099a0904a42ec769ef0262cd3a01bed22cf996d81e7cbe3876decd9a2bc6f0.jpg)

Yen-Liang Chen is Professor of Information Management at National Central University of Taiwan. He received his Ph.D. degree in computer science from National Tsing Hua University, Hsinchu, Taiwan. His current research interests include data mining, information retrieval, knowledg management and decision making models. He has published papers in Decision Support Systems, Information & Management, IEEE Transactions on Software Engineering, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on SMC — part A and part B, Information Systems, Operations Research, Journal of Information Science, Information Sciences, Naval Research Logistics, Transportation Research — part B, European Journal of

Operational Research, Knowledge-based Systems and many others. He is currently the editor-in-chief of Journal of Information Management.

Li-Chen Cheng is an Assistant Professor of Department of Computer Science and Information Management, Soochow University, Taipei, Taiwan. She received her Ph.D. degree in information management from National Central University, Chung-Li, Taiwan. Her current research interests include data mining, information retrieval and EC technologies
