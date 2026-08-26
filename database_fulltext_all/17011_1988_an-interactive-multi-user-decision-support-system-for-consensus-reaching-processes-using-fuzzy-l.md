---
otero_id: 17011
otero_key: "BGC5BGNV"
title: "An interactive multi-user decision support system for consensus reaching processes using fuzzy logic with linguistic quantifiers"
authors: "Mario Fedrizzi; Janusz Kacprzyk; Sł;awomir Zadrożny"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90019-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Interactive Multi-User Decision Support System for Consensus Reaching Processes Using Fuzzy Logic with Linguistic Quantifiers

Mario FEDRIZZI \*, Janusz KACPRZYK \*\* and Sławomir ZADROŻNY \*\*

\* Institute of Informatics, University of Trento, Via Verdi 26, 38100 Trento, Italy

\*\* Systems Research Institute, Polish Academy of Sciences, ul. Newelska 6, 01-447 Warsaw, Poland

We present an interactive user-friendly microcomputer-based decision support system for consensus reaching processes. The point of departure is a group of individuals (experts, decision makers,...) who present their testimonies (opinions) in the form of individual fuzzy preference relations. Initially, these opinions are usually quite different, i.e. the group is far from consensus. Then, in a multistage session a moderator, who is supervising the session, tries to make the individuals change their testimonies by, e.g., rational argument, bargaining, etc. to eventually get closer to consensus. For gauging and monitoring the process a new 'soft' degree (measure) of consensus is used whose essence is the determination to what degree, e.g., 'most of the individuals agree as to almost all of the relevant options'. A fuzzy-logic-based calculus of linguistically quantified propositions is employed.

Keywords: Group Decision Making, Consensus, Consensus Degree (Measure), Decision Support System, Fuzzy Logic, Linguistic Quantifier.

## 1. Introduction

Much of decision making activities in reality is to proceed in a group framework. This is necessary in the present world in which virtually all problems to be solved concern diverse aspects and involve different actors with their diverse, often conflicting, value systems. A group may consist both of some individuals and of some subgroups (e.g., institutions, agencies, departments,...) if only they can be viewed uniform as to some aspect in question (e.g., preferences or value systems).

Tasks of decision making groups may be quite diverse. On the one hand, they may concern various steps of the problem-solving process as, e.g., sensing, exploration and definition of the problem, identification of criteria and constraints, proposal generation and evaluation, choice and implementation of a course of action, performance evaluation, etc. On the other hand, a group may serve as an information generator, recommendation generator, autonomous decision unit, etc.

It is quite natural that some computerized decision support system can be useful to help run group decision making processes. And, indeed, group decision support systems are widely advocated, developed, and employed both by academic research groups, public administration, and private sector companies. For a review, see, e.g., DeSanctis and Gallupe (1985), Gray (1987) or Huber (1983, 1984).

This paper concerns some issues related to a group decision support system which is under development. Basically, we discuss some means for supporting consensus reaching processes. These processes are an important part of group decision making, hence should find a proper place in a group decision support system. However, they are by no means the only aspect of group decision making. The algorithms and software to be described here form therefore just a subsystem in the intended group decision support system though, for brevity, we use the word 'system' instead of 'subsystem'. Parenthetically, let us note that the intended system is meant to support a wide spectrum of group-decision-making-related tasks, of which consensus reaching is just a small subset, since we share the view of many researchers and practitioners (see, e.g., Huber, 1983) that the greater the range of tasks supported by the system, the more chance that it will be used, hence will survive. This opinion is also confirmed by our experience.

![](/api/attachments/BGC5BGNV/fulltext/images/d9764fb485c3df0c461f4b0355f615a1b6b0b000fd20768d16cb63f150257404.jpg)  
Fig. 1. Group decision support system and its consensus-reaching-related part.

The basic framework within which we will operate may be portrayed as in fig. 1. We have a set of individuals (experts, decisionmakers,...) who present their opinions concerning an issue in question, and a distinguished person, called moderator, who is supposed to be responsible for the session with the individuals. The individuals present their testimonies which may initially differ to a large extent, i.e. the group may be far from consensus (unanimous agreement, as traditionally meant). Then, the moderator – via some exchange of information, rational argument, bargaining, etc. – tries to persuade the individuals to change their opinions. If the individuals are rationally committed to consensus, such a change usually occurs, and the group gets closer to consensus. This is repeated until the group gets sufficiently close to consensus, i.e. until the individual opinions become sufficiently similar, or until we reach some time limit meant for the process.

It is clear from the above that if the number of individuals is high enough and the form of their opinions is complex enough (as will be in our case), then it may be difficult for the moderator to assess how close to consensus the group is, hence to efficiently run the session. Thus, he or she needs a degree of consensus, as well as some effective communication means with the system and individuals. Both should be user-friendly and human-consistent. We attain this, firstly, by using in the definition of our degree of consensus some elements of commonsense knowledge and of a natural language, and, secondly, by allowing elements of a natural language, computer graphics, interactive mode, etc. for communication.

Our basic framework within which to operate is as follows. We have a set of options and a set of individuals. The individual testimonies are assumed to be expressed as individual fuzzy preference relations. This is a convenient representation of real-life preferences which are often not clear-cut. Basically, if $S = \{s_{1}, \ldots, s_{n}\}$ is a set of options, then the individual fuzzy preference relation of individual k, $R_{k}$ , is given by its membership function $\mu_{R_{k}}: S \times S \to [0, 1]$ such that $\mu_{R_{k}}(s_{i}, s_{j}) \in [0, 1]$ is the strength of preference of option $s_{i}$ over option $s_{j}$ as felt by individual k. More information on fuzzy preferences will be given in section 3. Notice that a fuzzy preference relation is a convenient means for representing human preferences; moreover, it encompasses other conventional representations as, e.g., nonfuzzy preference relations or preference orderings.

As a means for assessing the similarity of individual fuzzy preference relations, i.e. the closeness to consensus, we use some new degrees of consensus (Fedrizzi and Kacprzyk, 1988; Kacprzyk, 1987a; Kacprzyk and Fedrizzi, 1986, 1988). Basically, the degree of consensus is meant to be the degree to which, e.g., ‘most of the individuals agree as to their preferences concerning almost all of the relevant options’; ‘most’ and ‘almost all’ may be replaced by any suitable linguistic quantifier. This degree of consensus takes on its values in the unit interval, from 0 for a complete lack of consensus (dissensus) to 1 for full consensus, through all intermediate values. Notice that this new degree of consensus is certainly more realistic and human-consistent than conventional degrees. Section 3 is concerned with the description of the new degree of consensus.

As a formal tool for deriving the new degree of consensus we use Zadeh's (1983) fuzzy-logic-based calculus of linguistically quantified propositions presented in section 2. This calculus is a prerequisite for Zadeh's (1984) representation of commonsense knowledge as a collection of dispositions, i.e. propositions with implicit linguistic quantifiers. The use of this calculus in the development of our degree of consensus may be therefore viewed as an attempt at introducing commonsense into the essence of consensus.

In section 4 we describe an interactive microcomputer-based decision support system for consensus reaching processes based on the new degree of consensus. We briefly present the structure of the system. Emphasis is on its use. We present the main menus, helps, data elicitation modes, etc. All are user-friendly making much use of a quasi natural language, graphics, etc.

Our notation concerning fuzzy sets is standard; for details, see, e.g., Kacprzyk (1983) or Zimmermann (1985, 1987).

## 2. A Fuzzy-Logic-Based Calculus of Linguistically Quantified Propositions

A linguistically quantified proposition is exemplified by ‘most experts are convinced’ and is generally written as

$$
\mathbf {Q Y ^ {\prime} s a r e F},\tag{1}
$$

where Q is a linguistic quantifier (e.g., most), $Y = \{y\}$ is a set of objects (e.g., experts), and F is a property (e.g., convinced).

Importance B may also be introduced into (1) yielding

$$
\mathbf {Q B Y ^ {\prime} s a r e F},\tag{2}
$$

e.g., ‘most (Q) of the important (B) experts (Y's) are convinced (F)’.

The problem is basically to find truth(QY's are F) or truth (QBY's are F), respectively, knowing truth ( $y_i$ is F), for all $y_i \in Y$ . This may be done by a fuzzy-logic-based calculus of linguistically quantified propositions due to Zadeh (1983).

First, a linguistic quantifier $\mathbf{Q}$ is assumed to be a fuzzy set in [0, 1], written $\mathbf{Q} \subsetneq [0, 1]$ . For instance, Q = 'most' may be given by its membership function as

$$
\begin{array}{r l} \mu_ {\text {most}} (x) = 1 & \text {for} x \geq 0. 8, \\ = 2 x - 0. 6 & \text {for} 0. 3 <   x <   0. 8, \\ = 0 & \text {for} x \leq 0. 3. \end{array}\tag{3}
$$

Throughout the paper we will use the so-called proportional linguistic quantifiers ('most', 'almost all', 'much more than 75%',...) since they are more appropriate in our context. For the so-called absolute linguistic quantifiers ('about 5', 'much more than 7',...) the reasoning is similar.

Particularly important in our context are the so-called non-decreasing fuzzy quantifiers defined as

$$
\begin{array}{l} x ^ {\prime} > x ^ {\prime \prime} \Rightarrow \mu_ {Q} (x ^ {\prime}) \geq \mu_ {Q} (x ^ {\prime \prime}) \\ \text { for   each } \quad x ^ {\prime}, x ^ {\prime \prime} \in [ 0, 1 ]. \end{array}\tag{4}
$$

'Most' given by (3) is evidently non-decreasing.

Property F is defined as a fuzzy set in Y, $F \subseteq Y$ .

If $Y = \{y_{1}, \ldots, y_{p}\}$ , then the determination of truth( $y_{i}$ is F) is based on the (non-fuzzy) cardinalities, the so-called $\Sigma$ Counts, of the respective fuzzy sets (see, e.g., Zadeh, 1983, 1984) and proceeds in the two steps:

$$
r = \Sigma \operatorname{Count} (F) / \Sigma \operatorname{Count} (Y) = \frac {1}{p} \sum_ {i = 1} ^ {p} \mu_ {F} \left(y _ {i}\right),\tag{5}
$$

$$
\operatorname{truth} (\mathrm {QY^ {\prime} s~are~F}) = \mu_ {\mathrm{Q}} (r).\tag{6}
$$

Importance of the particular $y_{i} \in \mathbf{Y}$ is introduced as follows. $\mathbf{B} =$ 'important' is defined as a fuzzy set in $\mathbf{Y}, \mathbf{B} \subsetneq \mathbf{Y}$ , such that $\mu_{\mathbf{B}}(y_i) \in [0,1]$ is a degree of importance of $y_{i}$ , the higher $\mu_{\mathbf{B}}(y_i)$ the more important $y_{i}$ .

We rewrite “QBY’s are F” as “Q(B and F)Y’s are B” which leads to the following counterparts of (5) and (6), respectively:

$$
\begin{array}{l} r ^ {\prime} = \Sigma \text {Count(B and F)} / \Sigma \text {Count(B)} \\ = \sum_ {i = 1} ^ {p} \left(\mu_ {\mathrm{B}} (y _ {i}) * \mu_ {\mathrm{F}} (y _ {i})\right) / \sum_ {i = 1} ^ {p} \mu_ {\mathrm{B}} (y _ {i}), \end{array}\tag{7}
$$

where ‘\*’ is a t-norm; the following popular t-norms may be used in the system:

$$
a \wedge b = \min (a, b),\tag{8}
$$

ab,

(9)

$$
1 - \left(1 \wedge ((1 - a) ^ {p} + (1 - b) ^ {p}) ^ {1 / p}\right), \quad p \geq 1,\tag{10}
$$

referred to later on as type 1, type 2 and type 3 t-norms, respectively.

Then

$$
\operatorname{truth} (\mathrm {QBY^ {\prime} s~are~F}) = \mu_ {\mathrm{Q}} (r ^ {\prime}).\tag{11}
$$

Example 1. Let Y = 'experts' = {A, B, C}; F = 'convinced' = 0.1/A + 0.6/B + 0.8/C; Q = 'most' be given by (3); B = 'important' = 0.2/A + 0.5/B + 0.6/C.

Then, on the one hand, by (5) and (6), $r = 0.5$ and truth ('most experts are convinced') $= 2 \times 0.5 - 0.6 = 0.4$ , while, on the other hand, by (7) and (11), $r' = 1.2 / 1.3$ and truth ("most of the important experts are convinced") $= 1$ .

For more information on this calculus of linguistically quantified propositions, some other calculi, and an extensive exposition of its applications in a wide spectrum of decision making, control, etc. problems, see Kacprzyk (1987b).

## 3. A 'Soft' Degree of Consensus Based on Fuzzy Logic with Linguistic Quantifiers

In this section we will present the idea of a new 'soft' degree of consensus as proposed in Kacprzyk (1987), and then advanced in Kacprzyk and Fedrizzi (1986, 1988) and Fedrizzi and Kacprzyk (1988). This degree is meant to overcome some 'rigidness' of conventional degrees of consensus in which full consensus (= 1) occurs only when 'all the individuals agree as to all the issues'. This may often be counter-intuitive, hence that new degree can be equal to 1, which stands for full consensus, when, say, 'most of the individuals agree as to almost all (of the relevant) issues'.

Our point of departure is a set of individual fuzzy preference relations. If $S = \{s_{1}, \ldots, s_{n}\}$ is a set of options and $I = \{1, \ldots, m\}$ is a set of individuals, then a fuzzy preference relation of individual k, $R_{k}$ , is given by its membership function $\mu_{R_{k}}: S \times S \to [0, 1]$ such that

$$
\begin{array}{r l} \mu_ {\mathbf {R} _ {k}} (s _ {i}, s _ {j}) & = 1, \text { if } s _ {i} \text { is   definitely } \\ & \text { preferred   over } s _ {j}, \\ & = c \in (0. 5, 1), \quad \text { if } s _ {i} \text { is   slightly } \\ & \text { preferred   over } s _ {j}, \\ & = 0. 5, \text { if   there   is   no   preference } \\ & \text {(i.e.   indifference)}, \end{array}
$$

$$
\begin{array}{l} = d \in (0, 0. 5), \text { if } s _ {j} \text { is   slightly } \\ \quad \text { preferred   over } s _ {i}, \\ = 0, \text { if } s _ {j} \text { is   definitely } \\ \quad \text { preferred   over } s _ {i}. \end{array}\tag{12}
$$

If card S is small enough, as we assume here, $R_{k}$ may be represented by a matrix $[r_{ij}^{k}]$ , $r_{ij}^{k} = \mu_{\mathbf{R}_{k}}(s_{i}, s_{j})$ ; i, j = 1, ..., n; k = 1, ..., m. $R_{k}$ is commonly assumed (also here) reciprocal, i.e. $r_{ij}^{k} + r_{ji}^{k} = 1$ ; moreover, $r_{ii}^{k} = 0$ , for all i, j, k.

The degree of consensus is now derived in three steps. First, for each pair of individuals we derive a degree of agreement as to their preferences between all the pair of options, next we pool (aggregate) these degrees to obtain a degree of agreement of each pair of individuals as to their preferences between Q1 (a linguistic quantifier as, e.g., 'most', 'almost all', 'much more than 50%',...) pairs of relevant options, and, finally, we pool these degrees to obtain a degree of agreement of Q2 (a linguistic quantifier similar to Q1) pairs of individuals as to their preferences between Q1 pairs of relevant options. This is meant to be the degree of consensus sought.

We start with the degree of strict agreement between individuals k1 and k2 as to their preferences between options $s_{i}$ and $s_{j}$

$$
\begin{array}{r l} v _ {i j} (k 1, k 2) = 1, & \text { if } r _ {i j} ^ {k 1} = r _ {i j} ^ {k 2}, \\ = 0, & \text { otherwise }, \end{array}\tag{13}
$$

where $k1 = 1, \ldots, m - 1$ ; $k2 = k1 + 1, \ldots, m$ ; $i = 1, \ldots, n - 1$ ; $j = i + 1, \ldots, n$ .

Relevance of the options is assumed to be a fuzzy set defined in the set of options, $B \subseteq S$ , such that $\mu_{\mathbf{B}}(s_{i}) \in [0,1]$ is a degree of relevance of option $s_{i}$ : from 0 standing for ‘definitely irrelevant’ to 1 for ‘definitely relevant’, through all intermediate values.

Relevance of a pair of options, $(s_{i}, s_{j}) \in \mathbf{S} \times \mathbf{S}$ , may be defined in various ways among which

$$
b _ {i j} ^ {\mathrm{B}} = \left(\mu_ {\mathrm{B}} (s _ {i}) + \mu_ {\mathrm{B}} (s _ {j})\right) / 2,\tag{14}
$$

is certainly the most straightforward; obviously, $b_{ij}^{\mathbf{B}} = b_{ji}^{\mathbf{B}}$ , and $b_{ii}^{\mathbf{B}}$ 's are irrelevant since they concern the same option, for all $i, j, k$ .

The degree of agreement between individuals k1 and k2 as to their preferences between all the relevant pairs of options is

$$
\begin{array}{r l} v _ {\mathrm{B}} (k 1, k 2) & = \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} \left(v _ {i j} (k 1, k 2) * b _ {i j} ^ {\mathrm{B}}\right) / \\ & / \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} b _ {i j} ^ {\mathrm{B}}, \end{array}\tag{15}
$$

where ‘\*’ is a t-norm as, e.g., (8)-(10).

The degree of agreement between individuals k1 and k2 as to their preferences between Q1 relevant pairs of options is

$$
v _ {\mathrm{Q1.B}} (k 1, k 2) = \mu_ {\mathrm{Q1}} \big (v _ {\mathrm{B}} (k 1, k 2) \big).\tag{16}
$$

In turn, the degree of agreement of all the pairs of individuals as to their preferences between Q1 relevant pairs of options is

$$
v _ {\mathrm{Q1.B}} = \frac {2}{m (m - 1)} \sum_ {k 1 = 1} ^ {m - 1} \sum_ {k 2 = k 1 + 1} ^ {m} v _ {\mathrm{Q1.B}} (k 1, k 2),\tag{17}
$$

and, finally, the degree of agreement of Q2 pairs of individuals as to their preferences between Q1 relevant pairs of options, called the degree of Q1/Q2/B-consensus, is

$$
\operatorname{con} _ {\mathrm{B}} (\mathrm{Q1}, \mathrm{Q2}) = \mu_ {\mathrm{B}} (v _ {\mathrm{Q1,B}}).\tag{18}
$$

Since the strict agreement (13) may be viewed too rigid, we can use the degree of sufficient agreement (at least to degree $\alpha \in [0, 1]$ ) of individuals k1 and k2 as to their preferences between options $s_{i}$ and $s_{j}$ , defined by

$$
\begin{array}{r l} v _ {i j} ^ {\alpha} (k 1, k 2) = 1, & \text { if } \quad | r _ {i j} ^ {k 1} - r _ {i j} ^ {k 2} | \leq 1 - \alpha \leq 1, \\ = 0, & \text { otherwise. } \end{array} \tag {1}\tag{19}
$$

Then, following the reasoning (14)-(18), we obtain the degree of sufficient agreement (at least to degree $\alpha$ ) of Q2 pairs of individuals as to their preferences between Q1 pairs of relevant options, called the degree of $\alpha/\mathrm{Q1}/\mathrm{Q2}/\mathrm{B}$ -consensus, given by

$$
\operatorname{con} _ {\mathrm{B}} ^ {\alpha} (\mathrm{Q1}, \mathrm{Q2}) = \mu_ {\mathrm{Q2}} (v _ {\mathrm{Q1,B}} ^ {\alpha}).\tag{20}
$$

We can also explicitly introduce the strength of agreement into (13) and define the degree of strong agreement of individuals k1 and k2 as to their preferences between options $s_{i}$ and $s_{j}$ , e.g., as

$$
v _ {i j} ^ {s} (k 1, k 2) = s \left(\left| r _ {i j} ^ {k 1} - r _ {i j} ^ {k 2} \right|\right),\tag{21}
$$

where $s\colon[0,1]\to[0,1]$ is some function representing the degree of strong agreements as, e.g.,

$$
\begin{array}{l l} s (x) = 1 & \text { for } \quad x \leq 0. 0 5, \\ = - 1 0 x + 1. 5 & \text { for } \quad 0. 0 5 <   x <   0. 1 5, \\ = 0 & \text { for } \quad x \geq 0. 1 5, \end{array}\tag{22}
$$

such that $x' < x'' \Rightarrow s(x') \geq s(x'')$ , for all $x', x'' \in [0, 1]$ , and $s(x) = 1$ for some $x \in [0, 1]$ .

Then, following the reasoning (14)-(18), we obtain the degree of strong agreement of Q2 pairs of individuals as to their preferences between Q2 pairs of relevant options, called the degree of $s / \mathrm{Q}1 / \mathrm{Q}2 / \mathrm{B}$ -consensus, as

$$
\operatorname{con} _ {\mathrm{B}} ^ {s} (\mathrm{Q1}, \mathrm{Q2}) = \mu_ {\mathrm{Q2}} (v _ {\mathrm{Q1,B}} ^ {s}).\tag{23}
$$

Example 2. Let the numbers of options, n, and individuals, m, be both four, and the individual fuzzy preference relations be (the left lower triangular parts are obviously irrelevant in the fuzzy preference matrices considered in this paper which are assumed to be reciprocal):

$$
\mathbf {R} ^ {1} = \left[ r _ {i j} ^ {1} \right] = i \begin{array}{c} 2 \\ 3 \\ 4 \end{array} \left[ \begin{array}{c c c c} 1 & 2 & j & 4 \\ - & 0. 4 & 0. 7 & 0. 1 \\ & - & 0. 8 & 0. 2 \\ & & - & 0. 7 \\ & & & - \end{array} \right],
$$

$$
\mathbf {R} ^ {2} = \left[ r _ {i j} ^ {2} \right] = i \begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \end{array} \left[ \begin{array}{c c c c} 1 & 2 & j & 3 \\ - & 0. 4 & 0. 5 & 0. 0 \\ & - & 0. 8 & 0. 2 \\ & & - & 0. 7 \\ & & & - \end{array} \right],
$$

$$
\mathbf {R} ^ {3} = \left[ r _ {i j} ^ {3} \right] = i \begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \end{array} \left[ \begin{array}{c c c c} 1 & 2 & j & 3 \\ - & 0. 4 & 0. 4 & 0. 3 \\ & - & 0. 8 & 0. 2 \\ & & - & 0. 7 \\ & & & - \end{array} \right],
$$

$$
\mathbf {R} ^ {4} = \left[ r _ {i j} ^ {4} \right] = i \begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \end{array} \left[ \begin{array}{c c c c} 1 & 2 & 3 & 4 \\ - & 0. 4 & 0. 7 & 0. 1 \\ & - & 0. 7 & 0. 1 \\ & & - & 0. 7 \\ & & & - \end{array} \right].
$$

Q1, the quantifiers concerning the options, and Q2, the quantifier concerning the individual, are both assumed to be 'most' defined by (3), and the t-norm is (8), i.e. $a \wedge b = \min(a, b)$ . First, relevance of the options is not accounted for, i.e. it is assumed that $\mu_{\mathbf{B}}(s_i) = 1$ , for $s_i \in \mathbf{S}$ .

First, via (15) we obtain the degree of agreement between individuals k1 and k2 as to their preferences between all the relevant pairs of options as

$$
v _ {\mathrm{B}} (k 1, k 2) = k 1 \begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \end{array} \left[ \begin{array}{c c c c} 1 & 2 & k 2 & 3 \\ - & 0. 6 7 & 0. 6 7 & 0. 6 7 \\ & - & 0. 6 7 & 0. 3 3 \\ & & - & 0. 3 3 \\ & & & - \end{array} \right],
$$

and the degree of agreement between individuals k1 and k2 as to their preferences between Q1 ('most') relevant pairs of options as

$$
v _ {\mathrm{Q1.B}} (k 1, k 2) = k 1 \left[ \begin{array}{c c c c} 1 & 2 ^ {k 2} & 3 & 4 \\ - & 0. 7 3 & 0. 7 3 & 0. 7 3 \\ & - & 0. 7 3 & 0. 0 7 \\ & & - & 0. 0 7 \\ 4 & & & - \end{array} \right],
$$

and, via (18), we obtain

$$
\operatorname{con} _ {B} \left(^ {\prime} \text {most}, ^ {\prime} \text {most}\right) = 0. 4 2 2 2.
$$

Next, we assume that $\alpha = 0.9$ . First, via (15) we obtain the degree of (sufficient, at least to degree $\alpha = 0.90$ ) agreement between individuals k1 and k2 as to their preferences between all the relevant pairs of options as

$$
v _ {\mathrm{B}} ^ {0. 9 0} (k 1, k 2) = k 1 \begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \end{array} \left[ \begin{array}{c c c c} 1 & 2 & k 2 & 3 \\ - & 0. 8 3 & 0. 6 7 & 1. 0 0 \\ & - & 0. 8 3 & 0. 8 3 \\ & & - & 0. 6 7 \\ & & & - \end{array} \right],
$$

and the degree of (sufficient, at least to degree $\alpha=0.90$ ) agreement between individuals k1 and k2 as to their preferences between Q1 ('most') relevant pairs of options as

$$
v _ {\mathrm{Q1,B}} ^ {0. 9 0} (k 1, k 2)
$$

$$
= k 1 \begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \end{array} \left[ \begin{array}{c c c c} 1 & 2 & k 2 & 3 \\ - & 1. 0 0 & 0. 7 3 & 1. 0 0 \\ & - & 1. 0 0 & 1. 0 0 \\ & & - & 0. 7 3 \\ & & & - \end{array} \right],
$$

and, via (20), we obtain

$$
\operatorname{con} _ {\mathbf {B}} ^ {0. 9 0} \left(^ {\prime} \text {most}, ^ {\prime} \text {most}\right) = 1. 0.
$$

Next, we assume $s(x)$ given by (22). First, via (15) we obtain the degree of (strong) agreement between individuals k1 and k2 as to their preferences between all the relevant pairs of options as

$$
v _ {\mathrm{B}} ^ {s} (k 1, k 2) = k 1 \begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \end{array} \left[ \begin{array}{c c c c} 1 & 2 & k 2 & 3 \\ - & 0. 7 5 & 0. 6 7 & 0. 8 3 \\ & - & 0. 7 5 & 0. 5 8 \\ & & - & 0. 6 7 \\ & & & - \end{array} \right],
$$

and the degree of (strong) agreement between individuals k1 and k2 as to their preferences between Q1 ('most') relevant pairs of options as

$$
v _ {\mathrm{Q1}, \mathrm{B}} ^ {s} (k 1, k 2) = k 1 \begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \end{array} \left[ \begin{array}{c c c c} 1 & 2 & k 2 \\ - & 0. 9 0 & 0. 7 3 & 1. 0 0 \\ & - & 0. 9 0 & 0. 5 7 \\ & & - & 0. 4 0 \\ & & & - \end{array} \right],
$$

and, via (23), we obtain

$$
\operatorname{con} _ {\mathbf {B}} ^ {s} \left(^ {\prime} \text {most}, ^ {\prime} \text {most}\right) = 0. 9 0.
$$

If the relevance of the particular options is, e.g., $\mu_{\mathbf{B}}(s_1) = 0.1$ , $\mu_{\mathbf{B}}(s_2) = 1.0$ , $\mu_{\mathbf{B}}(s_3) = 0.1$ and $\mu_{\mathbf{B}}(s_4) = 1.0$ , then we obtain

$$
\operatorname{con} _ {\mathrm{B}} \left(^ {\prime} \text {most} ^ {\prime}, ^ {\prime} \text {most} ^ {\prime}\right) = 0. 5 9 9 8,
$$

$$
\operatorname{con} _ {\mathbf {B}} ^ {0. 9 0} \left(^ {\prime} \text {most}, ^ {\prime} \text {most}\right) = 1. 0,
$$

$$
\operatorname{con} _ {\mathbf {B}} ^ {s} \left(^ {\prime} \text {most}, ^ {\prime} \text {most}\right) = 1. 0.
$$

For more information on these degrees of consensus, see Fedrizzi and Kacprzyk (1988), Kacprzyk (1987a), and Kacprzyk and Fedrizzi (1986, 1988).

## 4. Description of an Interactive System for Supporting Consensus Reaching

In this section we will briefly describe the structure of the system, and then present some examples of the system's menus, helps, commands, data elicitation procedures, etc. Finally, we will sketch an example of a session concerning the choice of an investment option.

## 4.1. The Structure of the System

The nature of the problem considered and its solution procedures imply the structure of the system, both in its hardware and software aspects. From the software viewpoint, the system may be portrayed as in fig. 2 to be meant as follows. The Data Elicitation Module makes it possible to elicit from the users, i.e. the moderator and the particular individuals, data needed by the system as, e.g., individual fuzzy preference relations, relevance of options, forms of the fuzzy linguistic quantifiers, etc. This all is possible in a user-friendly way.

![](/api/attachments/BGC5BGNV/fulltext/images/52bf61f5c517b44809b950157d72edbad28a29b143320b265d429331704e2c06.jpg)  
Fig. 2. Software structure of the decision support system for consensus reaching.

The Managing Module is an ‘operating system’ meant to decode the moderator’s commands, the individuals’ responses, etc. Basically, it: (1) controls the data elicitation mode as, e.g., an initial introduction of data or their review or updating, (2) sets appropriate parameters as, e.g., coefficients or types of algorithms for, say, computational procedures, and (3) activates an appropriate reporting facility as, e.g., display of the value of a consensus measure, or of some ‘troublesome’ options or individuals (those causing a low value of a degree of consensus).

The Parameter Setup Module determines the necessary parameters and their values due to the moderator's commands decoded by the Managing Module.

The purpose of the Consensus Degree Computation Module is first of all to calculate the value of a consensus degree. The type of the algorithm to be used and the necessary parameters are determined by the Parameter Setup Module. Moreover, the Consensus Degree Computation Module provides some additional information on, e.g., 'troublesome' options and individuals.

The Reporting Module provides various reporting facilities both for the moderator and the individuals, mainly concerning display of the value of a degree of consensus and its temporal evolution, ‘troublesome’ options and individuals, ‘history’ of changes and updates, etc.

The meaning of the Data Files, Output Files, and Reports is self-evident.

Finally, let us note that although in fig. 2 we show separate terminals for the moderator and all the particular individuals, this is not a prerequisite. In the case of some hardware or software limitations, when the number of the terminals is to be limited, the system can also work fine, even in the extreme case of just one terminal for the moderator who inputs from his or her terminal the individuals' testimonies, their changes and updates, etc.

The system is written in Borland's Turbo-Pascal™ and implemented on the IBM PC XT/AT.

## 4.2. Brief Description of Running the System

Now we will briefly present how to run the system, mainly in the sense of man-machine interaction.

In its present version the system is menu-driven. From the top level viewpoint the system's operation is governed by the Main Menu shown in Exhibit 1. This menu is meant for the moderator and includes basic options for initializing, running and quitting the session. Instructions are given in a 'help' submodule shown in Exhibit 2.

Let us sketch the essence of the particular options from the Main Menu. The 'Prepare Data (Preference Matrices)' option activates the Data Preparation Menu shown in Exhibit 3 and briefly explained in a 'help' submodule shown in Exhibit 4. The main step is to initialize the system, i.e. to introduce the fuzzy preference matrices (relations) of the particular individuals. This is done as explained in a 'help' submodule shown in Exhibit 5. By following the instructions, one (individual 1 in our case) finally arrives at a fuzzy preference matrix shown in Exhibit 6. Evidently, the lower part of this matrix is irrelevant (cf. (12)).

The other options in the Main Menu (Exhibit 1) are self-explanatory. For instance, choosing options 1 or 2, i.e. 'Save Data to Disk File' or

Moderator

Main Menu

Do you want to

1 PREPARE DATA (PREFERENCE MATRICES)

2 SET PARAMETERS

3 DISPLAY CURRENT VALUES OF PARAMETERS

4 COMPUTE CONSENSUS DEGREE

5 GET HELP

6 QUIT THE SYSTEM

Press a key with a number of suitable item from the list

Exhibit 1

'Restore Data from Disk File', respectively, the moderator should proceed according to the 'Saving/Restoring Data' help submodule shown in Exhibit 7.

The ‘Set Parameters’ option in the Main Menu (Exhibit 1) is quite complex. It is to be chosen in the beginning of each session, and less frequently during it. By choosing this option we consecu-

## MODERATOR

## CONSENSUS MEASURE SYSTEM

This program computes a consensus degree between opinions of a group of experts (decision-makers) as to their preferences over a set of options.

Its algorithm is based on the concept of fuzzy agreement. The number of options is limited to 10 and so is the number of experts.

Opinions of the experts must be expressed in the form of fuzzy preference matrices. To enter them directly from the keyboard or from the disk --> choose option 1.

There are a few parameters of the algorithm. They have default values, but you can change them. If you want to --> choose option 2.

To find out how they are set --> choose option 3.

After entering data and, optionally, setting parameters you start the algorithm --> choose option 4.

Option 5 provides some help information.

Option 6 quits the program.

During the dialog you face two forms of communication with the program: a menu and the setting of parameters. A menu is a list of actions the program can undertake for you. To execute a given action you have only to press a key with the number of this action in the list. During the setting of parameters you are asked to define values of certain parameters. You put these values in "white" fields on the screen - a set of editing facilities are provided.

Moderator

Data preparation menu

Do you want to

1 SAVE DATA TO DISK FILE

2 RESTORE DATA FROM DISK FILE

3 ENTER/EXAMINE/CORRECT DATA FROM KEYBOARD

4 CORRECT PREFERENCE MATRIX OF PARTICULAR USER

5 GET HELP

6 GO BACK TO MAIN MENU

Press a key with a number of suitable item from the list

Exhibit 3

tively define the problem's parameters. First, we input the name of the problem which is relevant for documentation purposes only, and we define the number of individuals and options (Exhibit 8). Then, we define the names (labels) and importance coefficients of the particular options (Exhibit 9).

The next group of the problem's parameters is input in a different, more human-friendly way as sketched in Exhibit 10a–d. First, by pressing key

## MODERATOR

## DATA PREPARATION MENU

Now you are asked to prepare data:

\- Experts can choose to enter data directly from the keyboard → choose option 3;

\- If you prepared data during an earlier session and saved them on disk, you can restore them now → choose option 2;

\- You can save data → choose option 1. Obviously, before that you should enter data either from the keyboard or disk. Otherwise meaningless data will be saved;

\- If a particular expert wants to change his preference matrix $\rightarrow$ choose option 4. It may be useful in the second phase of the consensus reaching process;

\- Options 5 and 6 are self-explanatory.

EXPERT No. 1

## HOW TO ENTER PREFERENCES

You are requested to enter your preferences as to each pair of options.

The upper triangular part of your preference matrix, PRMAT, is shown on the display screen. The value of its $(i,j)$ -th entry, PRMAT $(i,j)$ , i<j, expresses the degree of your preference of option i over option j. The value PRMAT $(j,i)=1-$ PRMAT $(i,j)$ hence need not be entered.

Your preference must be expressed by one of the following numbers:

0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 according to the rule

PRMAT (i,j) = 0.0 if you definitely prefer option j to over option i
= d ∈ (0.0, 0.5) if you slightly prefer j over i
= 0.5 if you are indifferent as to j and i
= c ∈ (0.5, 1.0) if you slightly prefer i to j
= 1.0 if you definitely prefer i to j

with intermediate values for intermediate cases.

You enter data by just pressing keys with selected digits; you need not enter the decimal point or move the cursor. By using the cursor movement keys you can move around the matrix to modify the values entered earlier. "Beep" means that you tried to enter an illegal character.

## press any key when ready

## Exhibit 5

F3 we define the quantifier Q1 for the options. For simplicity, only the nondecreasing fuzzy quantifiers (cf. (4)) are allowed whose membership functions are piecewise-linear. Thus we need to specify two points: the first below which the quantifier's membership function is 0, and the second above which it is 1. This is done by moving the cursor from 0 to 1 along the x-axis, stopping the cursor at an appropriate point (value), and entering this value by pressing a key. In Exhibit 10a it is shown that we have input 0.10 and 0.80, respectively. The same procedure is used for defining the quantifier Q2 for the individuals (Exhibit 10b). Next, we press key F5 and by moving the cursor

EXPERT No. 1

<table><tr><td></td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1</td><td>0.9</td><td>0.8</td><td>0.3</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.3</td><td>0.6</td><td>0.2</td></tr><tr><td></td><td>2</td><td>0.6</td><td>0.7</td><td>0.4</td><td>0.1</td><td>0.7</td><td>0.8</td><td>0.8</td><td>0.4</td></tr><tr><td></td><td></td><td>3</td><td>0.5</td><td>0.3</td><td>0.6</td><td>0.7</td><td>0.7</td><td>0.3</td><td>0.8</td></tr><tr><td></td><td></td><td></td><td>4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.3</td><td>0.6</td><td>0.2</td></tr><tr><td colspan="4">F1 - HELP</td><td>5</td><td>0.2</td><td>0.5</td><td>0.7</td><td>0.5</td><td>0.7</td></tr><tr><td rowspan="4" colspan="5">F2 - INPUT COMPLETED←→↓↑- SEE HELP</td><td>6</td><td>0.5</td><td>0.7</td><td>0.6</td><td>0.7</td></tr><tr><td></td><td>7</td><td>0.8</td><td>0.8</td><td>0.4</td></tr><tr><td></td><td></td><td>8</td><td>0.6</td><td>0.7</td></tr><tr><td></td><td></td><td></td><td>9</td><td>0.4</td></tr></table>

# M. Fedrizzi, J. Kacprzyk, S. Zadrozny / DSS for Consensus Reaching Using Fuzzy Logic MODERATOR

## SAVING/RESTORING DATA

You have chosen the saving/restoring option. Now you should submit a name of the file to or from which data will be transferred. Saved or restored are the following data:

\- option names

\- option importance coefficients

\- problem name

\- number of options

\- number of decision-makers (experts)

\- preference matrices of all decision-makers

press any key when ready

Exhibit 7

define a t-norm (Exhibit 10c). Finally, we choose the kind of agreement. We press key F6 and by moving the cursor choose the strict, sufficient or strong agreement (cf. section 3). For the strict one no parameters are needed. For the strong one, a function such as (22) should be defined. Once again, for simplicity, we allow it to be piecewise-linear, therefore we should define two values by moving the cursor; in Exhibit 10d it is shown that we have input 0.20 and 0.80.

We are now ready for running a consensus reaching session. If we wish to check once again the current values of the parameters, we choose option 3 in the Main Menu, while if we wish to compute the value of a degree of consensus, we choose option 4 (cf. Exhibit 1). Then, in the next step, we can update the preference matrices of the particular individuals (cf. Exhibits 3 and 4). Finally, if we reach either a sufficiently high value of a degree of consensus or have no more time for the session, we can quit.

When the session is terminated, this is the end of the problem considered in our paper. Evidently, having sufficiently similar (in terms of a degree of

## MODERATOR

## ENTERING CHARACTERISTIC OF THE PROBLEM

You are asked to enter a name of the problem - this name is only for documentation purposes. More important are two other items whose meaning is clear.

Number of decision makers should be in the range of 2 to 10.

Number of options should be in the range of 2 to 10.

press any key when ready

# M. Fedrizzi, J. Kacprzyk, S. Zadrozny / DSS for Consensus Reaching Using Fuzzy Logic MODERATOR ENTERING NAMES AND IMPORTANCE COEFFICIENTS OF THE OPTIONS

Now you are asked to name each option and define its importance coefficient. The longer field is for the name and shorter for the coefficient.

The naming of options makes it easier for the expert to enter the preference matrix. You can avoid naming them by leaving the field empty.

The importance coefficient is used in computing a consensus measure.

For a given option the higher it is the closer the agreement between the decision-makers.

press any key when ready

Exhibit 9

consensus) individual fuzzy preference relations, we can use some other known method as, e.g., given in Kacprzyk (1984, 1985a–c, 1986a, b, 1987a) or Nurmi (1981) to pick up some option(s) which are to be viewed as a choice of the group of individuals as a whole. This is, however, beyond the scope of this paper.

Let us now present an example of a consensus reaching session concerning the choice of an investment option in a small community.

Example 3. There are four options: school, movie theater, shopping center, and swimming pool. There are ten individuals who represent both the local and upper level authorities, social and political organizations, some informal groups, a ‘man-in-the-street’, etc. Their (initial) individual fuzzy preference relations are as follows:

a)  
![](/api/attachments/BGC5BGNV/fulltext/images/3d318c1c77a0ab031b558271350e2621381a5ba62b55328392019ea1c74072e7.jpg)

b)  
![](/api/attachments/BGC5BGNV/fulltext/images/51a9e1f54909970ea35bb9cc5294026aa6a3b66d3ff50d5565ec5a8a482819b5.jpg)

c)  
![](/api/attachments/BGC5BGNV/fulltext/images/6192e40f29b26f25901cf8b5d0f8430448b954b10102fac56ce80a7dac7f3be7.jpg)

d)  
![](/api/attachments/BGC5BGNV/fulltext/images/d0b93357dac78f381896f903f2b88f5daf3867dc3b7f2697b67840f97de434da.jpg)  
F1 - Help F2 - input completed F3F4F5F6 - set parameters

$$
\begin{array}{r l} & {\mathbf {R} _ {1} = \left[ \begin{array}{l l l l} - & 0. 9 & 0. 9 & 1. 0 \\ & - & 0. 8 & 0. 7 \\ & & - & 0. 7 \\ & & & - \end{array} \right],} \\ & {\mathbf {R} _ {2} = \left[ \begin{array}{l l l l} - & 0. 7 & 1. 0 & 1. 0 \\ & - & 0. 8 & 0. 9 \\ & & - & 0. 5 \\ & & & - \end{array} \right],} \\ & {\mathbf {R} _ {3} = \left[ \begin{array}{l l l l} - & 1. 0 & 0. 6 & 1. 0 \\ & - & 0. 0 & 0. 4 \\ & & - & 1. 0 \\ & & & - \end{array} \right],} \\ & {\mathbf {R} _ {4} = \left[ \begin{array}{l l l l} - & 0. 9 & 0. 8 & 0. 6 \\ & - & 0. 6 & 0. 3 \\ & & - & 0. 3 \\ & & & - \end{array} \right],} \\ & {\mathbf {R} _ {5} = \left[ \begin{array}{l l l l} - & 0. 9 & 0. 5 & 1. 0 \\ & - & 0. 0 & 0. 4 \\ & & - & 1. 0 \\ & & & - \end{array} \right],} \\ & {\mathbf {R} _ {6} = \left[ \begin{array}{l l l l} - & 0. 6 & 1. 0 & 0. 7 \\ & - & 0. 0 & 0. 5 \\ & & - & 1. 0 \\ & & & - \end{array} \right],} \\ & {\mathbf {R} _ {7} = \left[ \begin{array}{l l l l} - & 1. 0 & 0. 7 & 1. 0 \\ & - & 0. 1 & 0. 5 \\ & & - & 0. 9 \\ & & & - \end{array} \right],} \\ & {\mathbf {R} _ {8} = \left[ \begin{array}{l l l l} - & 0. 6 & 0. 6 & 0. 4 \\ & - & 0. 9 & 0. 5 \\ & & - & 0. 4 \\ & & & - \end{array} \right],} \\ & {\mathbf {R} _ {9} = \left[ \begin{array}{l l l l} - & 0. 9 & 0. 8 & 0. 9 \\ & - & 0. 2 & 0. 5 \\ & & - & 0. 9 \\ & & & - \end{array} \right],} \\ & {\mathbf {R} _ {1 0} = \left[ \begin{array}{l l l l} - & 1. 0 & 0. 6 & 1. 0 \\ & - & 0. 0 & 0. 7 \\ & & - & 1. 0 \\ & & & - \end{array} \right]} \end{array}
$$

For both the individuals and options the quantifiers (Q1 and Q2, respectively) are ‘most’ given by (3), i.e.

$$
\begin{array}{r l} \mu_ {\text {most}} (x) = 1 & \text {for} x \geq 0. 8, \\ = 2 x - 0. 6 & \text {for} 0. 3 <   x <   0. 8, \\ = 0 & \text {for} x \leq 0. 3. \end{array}
$$

We chose the type 1 t-norm, i.e. ‘ $\wedge$ ’=‘min’, and the strong agreement with

$$
\begin{array}{r l} s (x) = 1 & \text { for } \quad x \leq 0. 5, \\ = - 1. 8 x + 1. 2 6 & \text { for } \quad 0. 1 5 <   x <   0. 7, \\ = 0 & \text { for } \quad x \geq 0. 7. \end{array}
$$

Notice that, first, even for such a small example it is difficult to assess how far from consensus the individuals are. Second, in the above preference relations we can see that some restrictions of many conventional approaches such as, e.g., transitivity, are clearly violated. This is, however, irrelevant in the case of our method.

For lack of space we cannot present here all the intermediate results obtained by following (13)-(18) [in fact, with (21) replacing (13) and (23) replacing (18)], let us therefore show (15), i.e. the degree of (strong) agreement between individuals $k1$ and $k2$ as to their preferences between all the relevant pairs of options

$v_{\mathbf{B}}^{s}(k1,k2)$

$$
= k 1 \left[ \begin{array}{c c c c c c c c c c} & 1 & 2 & 3 & 4 & 5 & k ^ {2} & 6 & 7 & 8 & 9 & 1 0 \\ 1 & - & 0. 8 9 & 0. 6 7 & 0. 6 2 & 0. 6 4 & 0. 5 2 & 0. 7 6 & 0. 6 2 & 0. 7 7 & 0. 7 4 \\ 2 & & - & 0. 4 4 & 0. 6 1 & 0. 4 1 & 0. 4 1 & 0. 5 3 & 0. 6 8 & 0. 5 5 & 0. 5 3 \\ 3 & & & - & 0. 6 7 & 1. 0 0 & 0. 7 7 & 0. 9 8 & 0. 5 2 & 0. 9 4 & 0. 9 5 \\ 4 & & & & - & 0. 6 1 & 0. 5 0 & 0. 6 4 & 0. 8 3 & 0. 7 0 & 0. 5 6 \\ 5 & & & & & - & 0. 7 7 & 0. 9 5 & 0. 4 8 & 0. 9 1 & 0. 9 5 \\ 6 & & & & & & - & 0. 7 1 & 0. 5 2 & 0. 7 0 & 0. 7 3 \\ 7 & & & & & & & - & 0. 4 7 & 0. 9 8 & 0. 9 7 \\ 8 & & & & & & & & - & \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \end{array} \right],
$$

and (16), i.e. the degree of (strong) agreement between individuals k1 and k2 as to their preferences between Q1 relevant pairs of options

$v_{\mathbf{Q1},\mathbf{B}}^{s}(k1,k2)$

$$
= k 1 \left[ \begin{array}{c c c c c c c c c c} 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 1 0 \\ 1 & - & 1. 0 0 & 0. 7 3 & 0. 6 4 & 0. 6 7 & 0. 4 3 & 0. 9 2 & 0. 6 4 & 0. 9 5 & 0. 8 8 \\ 2 & & - & 0. 2 8 & 0. 6 1 & 0. 2 2 & 0. 2 2 & 0. 4 6 & 0. 7 6 & 0. 4 9 & 0. 4 6 \\ 3 & & & - & 0. 7 3 & 1. 0 0 & 0. 9 5 & 1. 0 0 & 0. 4 3 & 1. 0 0 & 1. 0 0 \\ 4 & & & & - & 0. 6 1 & 0. 4 0 & 0. 6 7 & 1. 0 0 & 0. 7 9 & 0. 5 2 \\ 5 & & & & & - & 0. 9 5 & 1. 0 0 & 0. 3 7 & 1. 0 0 & 1. 0 0 \\ 6 & & & & & & - & 0. 8 2 & 0. 4 3 & 0. 7 9 & 0. 8 5 \\ 7 & & & & & & & - & 0. 3 4 & 1. 0 0 & 1. 0 0 \\ 8 & & & & & & & & - & 0. 2 8 & 0. 3 4 \\ 9 & & & & & & & & & - & 1. 0 0 \\ 1 0 & & & & & & & & & - \end{array} \right].
$$

Then, assuming the same importance of all the options, i.e. $\mu_{\mathrm{B}}(s_i) = 1$ for all $s_i \in S$ , we obtain via (23)

$$
\operatorname{con} _ {B} ^ {s} \left(^ {\prime} \text {most}, ^ {\prime} \text {most}\right) = 0. 8 0 6 9.
$$

Parenthetically, let us remark that if we diminished the importance of option 3 (shopping center), we would obtain $\mathrm{con}_{B}^{S}(..) = 0.934$ ; on the other hand, if we chose the sufficient agreement (19) with $\alpha = 0.85$ , we would obtain $\mathrm{con}_{\mathbf{B}}^{0.85}(.,.) = 0.0$ .

Coming back to the situation mentioned above in which $\mathrm{con}_{\mathrm{B}}^{s}(.,.)=0.8069$ , let us assume that this is viewed unsatisfactory. A higher value of $\mathrm{con}_{\mathrm{B}}^{s}(.,.)$ can be obtained via an interaction between the moderator and individuals. For space limitations we cannot present here all the subsequent steps of the actual session, and we will only show some interactions whose essence might be more intuitively appealing.

In the first attempt at obtaining a higher value of a degree of consensus, as a result of the moderator's involvement there has occurred some change in the preferences of individuals 1, 2 and 8 as to the pair of options '2 (movie theater)-3 (shopping center)'. The following new values have been given: $r_{23}^{1} = r_{23}^{2} = r_{23}^{8} = 0.5$ (previously: 0.8, 0.8 and 0.9, respectively). In this case we obtain

$\mathrm{con}_{\mathbf{B}}^{s}('\mathrm{most}', ' \mathrm{most}') \cong 0.9232.$

In the second attempt, the above changes are neglected and via an interaction between the moderator and the individuals the following changes in the preferences of individuals 1, 2, 4, and 8 as to the pair '3 (shopping center)-4 (swimming pool)' occur: $r_{34}^{1} = 1.0$ , $r_{34}^{2} = 1.0$ . $r_{34}^{4} = 0.6$ , and $r_{34}^{8} = 1.0$ (previously: 0.7, 0.5, 0.3, and 0.4, respectively). We obtain

$\mathrm{con}_{\mathbf{B}}^{s}('\mathrm{most}', ' \mathrm{most}') \equiv 0.9934.$

In the third attempt the moderator has persuaded the individuals to accept jointly the changes in preferences which have occurred in the first and second attempt, and we obtain

$\mathrm{con}_{\mathbf{B}}^{s}('\mathrm{most}', ' \mathrm{most}') = 1.$

This value of the degree of consensus is evidently fully satisfactory, and the session is terminated.

## 5. Concluding Remarks

We have presented a microcomputer-based implementation of a decision support system for consensus reaching which is a part of an intended decision support system for supporting a large spectrum of group-decision-making-related tasks. We have used a new 'soft' human-consistent degree of consensus which better reflects the real human perception of the very essence and nature of consensus. We have used fuzzy logic with linguistic quantifiers which has proven to be an effective and efficient formal tool.

Experience does clearly indicate that the system may be useful in many cases which is primarily a result of its high flexibility and user-friendliness.

## References

Bezdek, J., B. Spillman and R. Spillman (1977), Fuzzy Measures of Preferences and Consensus in Group Decision Making. In K.S. Fu (Ed.), Proc. of 1977 IEEE Conf. on Decision and Control, pp. 1303–1309.

Bezdek, J., B. Spillman and R. Spillman (1978), A Fuzzy Relation Space for Group Decision Theory. Fuzzy Sets and Syst. 1, 255–268.

Bezdek, J., B. Spillman and R. Spillman (1979), Fuzzy Relation Spaces for Group Decision Theory: An Application. Fuzzy Sets and Syst. 2, 5–14.

Blin, J.M. (1974), Fuzzy Relations in Group Decision Theory. J. Cybern. 4, 17–22.

Blin, J.M. and A.B. Whinston (1973), Fuzzy Sets and Social Choice. J. Cybern. 3, 28–33.

De Groot, M.M. (1974), Reaching a Consensus. J. Amer. Stat. Ass. 69, 118–121.

DeSanctis, G. and B. Gallupe (1985), Group Decision Support Systems: A New Frontier. Data Base, 3–10.

Fedrizzi, M. (1986), Group Decisions and Consensus: A Model Using Fuzzy Sets Theory (in Italian). Rivista per le scienze econ. e soc. A. 9, F. 1, 12–20.

Fedrizzi, M. and J. Kacprzyk (1988), On Measuring Consensus in the Setting of Fuzzy Preference Relations. In J. Kacprzyk and M. Roubens (Eds.), Non-Conventional Preference Relations in Decision Making. Springer-Verlag, Berlin–New York–Tokyo, pp. 129–141.

French, S. (1981), Consensus of Opinion. Europ. J. Op. Res. 27, 332–340.

Gray, P. (1987), Group Decision Support Systems. Decision Support Syst. 3, 233–242.

Huber, G.P. (1983), The Design of Group Decision Support Systems. Proc. 16th Hawaii Int. Conf. on Systems Sci. (Honolulu, USA), pp. 437–444.

Huber, G.P. (1984), Issues in the Design of Group Decision Support Systems. MIS Quarterly 8, 195–204.

Kacprzyk, J. (1983), Multistage Decision Making under Fuzziness. Verlag TÜV Rheinland, Cologne.

Kacprzyk, J. (1984), Collective Decision Making with a Fuzzy Majority Rule. Proc. WOGSC Congress, AFCET, Paris, pp. 153–159.

Kacprzyk, J. (1985a), Zadeh's Commonsense Knowledge and Its Use in Multicriteria, Multistage and Multiperson Decision Making. In M.M. Gupta et al. (Eds.), Approximate Reasoning in Expert Systems, North-Holland, Amsterdam, pp. 105–121.

Kacprzyk, J. (1985b), Some 'Commonsense' Solution Concepts

in Group Decision Making via Fuzzy Linguistic Quantifiers. In J. Kacprzyk and R.R. Yager (Eds.), Management Decision Support Systems Using Fuzzy Sets and Possibility Theory. Verlag TÜV Rheinland, Cologne, pp. 125–135.

Kacprzyk, J. (1985c), Group Decision-making with a Fuzzy Majority via Linguistic Quantifiers. Part I: A Consensory-like Pooling; Part II: A Competitive-like Pooling. Cybernetics and Systems: an Int. Journal 16, 119–129 (Part I), 131–144 (Part II).

Kacprzyk, J. (1986a), Group Decision Making with a Fuzzy Linguistic Majority. Fuzzy Sets and Syst. 18, 105–118.

Kacprzyk, J. (1986b), Towards an Algorithmic/Procedural 'Human Consistency' of Decision Support Systems: A Fuzzy Logic Approach. In W. Karwowski and A. Mital (Eds.), Applications of Fuzzy Sets in Human Factors. Elsevier, Amsterdam, pp. 101–116.

Kacprzyk, J. (1987a), On Some Fuzzy Cores and 'Soft' Consensus Measures in Group Decision Making. In J.C. Bezdek (Ed.), The Analysis of Fuzzy Information, Vol. 2. CRC Press, Boca Raton, pp. 119–130.

Kacprzyk, J. (1987b), Towards ‘Human Consistent’ Decision Support Systems Through Commonsense-Knowledge-Based Decision Making and Control Models: A Fuzzy Logic Approach. Computers and Artificial Intelligence 6, 97–122.

Kacprzyk, J. and M. Fedrizzi (1985), 'Soft' Consensus Measures For Monitoring Real Consensus Reaching Processes under Fuzzy Preferences. Control and Cybern. 15, 309–323.

Kacprzyk, J. and M. Fedrizzi (1988), A 'Soft' Measure of Consensus in the Setting of Partial (Fuzzy) Preferences. Europ. J. Op. Res. 34, 316–325.

Kacprzyk, J. and M. Roubens, Eds. (1988), Non-Conventional Preference Relations in Decision Making. Springer-Verlag, Berlin-New York-Tokyo.

Kacprzyk, J. and R.R. Yager, Eds. (1985), Management Decision Support Systems Using Fuzzy Sets and Possibility Theory. Verlag TÜV Rheinland, Cologne.

Kelly, F.P. (1981), How a Group Reaches Agreement: A Stochastic Model. Math. Soc. Sci. 2, 1–8.

Kuzmin, V.B. (1982), Construction of Group Decisions in the Spaces of Non-Fuzzy and Fuzzy Binary Relations (in Russian). Nauka, Moscow.

Kuzmin, V.B. and S.V. Ovchinnikov (1980a), Group Decisions I: In Arbitrary Spaces of Fuzzy Binary Relations. Fuzzy Sets and Syst. 4, 53–62.

Kuzmin, V.B. and S.V. Ovchinnikov (1980b), Design of Group Decisions II: In Arbitrary Spaces of Fuzzy Binary Relations. Fuzzy Sets and Syst. 4, 153–165.

Lehrer, K. and C. Wagner (1981), Rational Consensus in Science and Society. Reidel, Dordrecht–Boston.

Loewer, B., Guest Ed. (1985), Special Issue on Consensus. Synthese 62, No. 1.

Nurmi, H. (1981). Approaches to Collective Decision Making with Fuzzy Preference Relations. Fuzzy Sets and Syst. 6, 187–198.

Ragade, R.K. (1976), Fuzzy Sets in Communication Systems and in Consensus Formation Systems. J. Cybern. 6, 21–38.

Ragade, R.K. (1977). Profile Transformation Algebra and Group Consensus Formation Through Fuzzy Sets. In M.M. Gupta, G.N. Saridis and B.R. Gaines (Eds.), Fuzzy Automata and Decision Processes. North-Holland, Amsterdam, pp. 331–356.

Spillman, B., J. Bezdek and R. Spillman (1979), Coalition Analysis with Fuzzy Sets. Kybernetes 8, 302–211.

Spillman, B., R. Spillman and J. Bezdek (1979), Development of an Instrument for the Dynamic Measurement of Consensus. Comm. Memo. 1–12.

Spillman, B., R. Spillman and J. Bezdek (1980), A Fuzzy Analysis of Consensus in Small Groups. In P.P. Wang and S.K. Chang (Eds.), Fuzzy Sets Theory and Applications to Policy Analysis and Information Systems. Plenum, New York, pp. 291–308.

Tanino, T. (1984), Fuzzy Preference Orderings in Group Decision Making. Fuzzy Sets and Syst. 12, 117–131.

Tanino, T. (1988), Fuzzy Preference Relations in Group Decision Making. In J. Kacprzyk and M. Roubens (Eds.), Non-Conventional Preference Relations in Decision Making. Springer-Verlag, Berlin–New York–Tokyo, pp. 54–71.

Zadeh, L.A. (1983), A Computational Approach to Fuzzy Quantifiers in Natural Languages. Comp. and Maths. with Appls. 9, 149–184.

Zadeh, L.A. (1984), A Theory of Commonsense Knowledge. In H.J. Skala, S. Termini and E. Trillas (Eds.), Aspects of Vagueness, Reidel, Dordrecht–Boston, pp. 257–295.

Zadeh, L.A. (1985), Syllogistic Reasoning in Fuzzy Logic and its Application to Usuality and Reasoning with Dispositions. IEEE Trans. on Syst., Man and Cybern. SMC-15, 754–763.

Zimmermann, H.J. (1985), Fuzzy Sets Theory and Its Applications. Kluwer-Nijhoff, Boston-Dordrecht-Lancaster.

Zimmermann, H.J. (1987), Fuzzy Sets, Decision Making, and Expert Systems. Kluwer, Boston–Dordrecht–Lancaster.
