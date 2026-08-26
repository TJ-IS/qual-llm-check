---
otero_id: 16884
otero_key: "4BZSDAHN"
title: "Computer based support of reasoning in the presence of fuzziness and uncertainty"
authors: "Amitava Dutta; Amit Basu"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90004-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computer Based Support of Reasoning in the Presence of Fuzziness and Uncertainty $^{1}$

Amitava DUTTA \* and Amit BASU \*\*

\* Management Science Dept., College of Business, University of Iowa, Iowa City, IA 52242, USA and \*\* Information Systems Dept., College of Business and Management, University of Maryland, College Park, MD 20742, USA

Decision making tasks require that we access (possibly large volumers of) data, transform it in various ways by performing computations on it, as well as reason with such raw or transformed data. Also, imprecision is almost omnipresent in practical decision making environments. In order to provide computer based support for reasoning activities in such environments, it is therefore necessary to develop schemes to represent imprecise knowledge and mechanically manipulate it. A previous paper developed such a scheme for fuzzy knowledge. This paper extends that representation to capture uncertainty as well. Mechanisms for propagating uncertainty during the reasoning process are also developed. The propagation mechanism allows interaction between fuzziness and uncertainty during the course of reasoning. The scheme developed here has been tested on a prototype implementation. The robustness of the representation and its use are demonstrated with an example.

![](/api/attachments/4BZSDAHN/fulltext/images/c1785507523f9a6ea286ffefda2fd99a9fe4f247f741ad932019188c13ec4115.jpg)

Amitava Dutta is Associate Professor in the Information Systems Area at the University of Iowa's College of Business. His research interests lie in the use of AI techniques to aid decision making in complex environments, computer integrated manufacturing and database management. He holds a BS in Electronics from IIT Kharagpur, an MS in computer science from UC Santa Barbara and received his PhD from Purdue University in 1981. Dr. Dutta is a member of the IEEE,

ACM, TIMS, ORSA and is on the editorial board of Expert Systems: Research and Applications.

## 1. Introduction

The use of computers to directly support managers in their decision making function has attracted major research and development effort in recent years, in both academia and industry [14], [9], [4], [23]. Such computer based support is important for several reasons. With the business environment becoming increasingly volatile and competitive, and with the enormous amounts of information that have to be processed as part of the decision making process, decision making is becoming increasingly complex and time-consuming, while constraints on the time available to make each decision are getting tighter. The high speed and versatility of modern computers, and their ability to effectively store large data bases, strongly suggests their use to facilitate such decision making activities.

Development of computer-based decision support tools has proved far more difficult for some types of decision problems than other. Problems that have been easier to support are typically structured in form; that is, they have been amenable to solution by preset algorithmic procedures, since enough is known about them to construct precise quantitative analytic procedures for a variety of problem instances. On the other hand, unstructured problems are difficult to support. Such problems cannot be solved effectively by preset algorithmic procedures, for two reasons.

![](/api/attachments/4BZSDAHN/fulltext/images/8b667e06d71cefc6f84351422218e9d8d7bf158cd4a92f04ee4057dcb1dd85e6.jpg)

First, the knowledge available about an unstructured problem is typically fragmented, imprecise and incomplete, so that formulation of precise, quantitative analytic procedures is difficult. For instance, consider a system to support auditing decisions. In particular, consider the usually difficult task of auditing accounts receivable. Much of the available knowledge is in the form of informal ‘rules of thumb’, such as:

## Rule. This debt is collectible IF

(a) the customer has a High credit rating,

(b) the customer's payment record for Recent transitions is Good,

(c) Recent contact with the customer about this debt has yielded a Positive response.

It is easy to see that knowledge in this form is not structured enough to formulate algorithmically. Also, different instances of the problem may require quite different solution procedures, so that preset procedures cannot be relied upon. Much of the complexity of such a problem arises from the logical ‘intelligent’ reasoning needed to identify suitable solution strategies and procedures for each instance, to apply these procedures appropriately, and to interpret their results. The difficulty of formulating algorithmic procedures to perform this vital reasoning process make computer support for unstructured problems difficult.

In spite of this, the managerial significance of many unstructured problems strongly motivates research effort into methods to overcome the problems in designing computerbased tools for unstructured decision support. One major problem that as yet been unresolved is how to reason effectively with imprecise knowledge, which, as mentioned earlier, is one major characteristic of unstructured problems. Imprecision in decision processes has two major aspects, fuzziness and uncertainty. Fuzziness refers to the use of fuzzy concepts in knowledge representation. That is, some or all of the concepts used are characterized by fuzzy, rather than crisp sets [26], where the distinguishing feature between these two types of sets is that elements of a fuzzy set may have a partial membership in the set (characterized by a membership function $\mu \rightarrow [0,1]$ ). Examples of such fuzzy terms are the italicized terms in the example rule mentioned earlier. On the other hand, uncertainty occurs when only partial knowledge is available about an entity, when future events are involved in the reasoning process, or when the underlying process is inherently stochastic. For instance, in the earlier rule, the conclusion about collectibility given the different premises is still uncertain.

The presence of these two sources of imprecision in decision making and problem-solving has been recognized for several years in the literature [6], [26]. In spite of this, existing approaches to formal knowledge representation and automated reasoning do not adequately distinguish between them, and in most cases, ignore one or the other completely. This shortcoming has been pointed out in some recent expository papers [12], [18], which have also helped identify the major features of the two phenomena in the context of Expert Systems. First, fuzziness and uncertainty are distinct, and can occur independently. We illustrate this by an example. Consider the statement S1: Sales in 1983 were \$1.5 million. This is a precise statement, since all its terms are nonfuzzy and certain (if the sales level in 1983 is known). On the other hand, the statement S2: Sales in 1983 were High is a fuzzy statement, if the term 'High' is considered to be fuzzy, rather than categorical. In moving from S1 to S2, the level of fuzziness was increased. However, if there is no uncertainty in the definition of the membership set of the fuzzy term 'High', the two statements have the same level of certainty. Similarly, a statement like S3: Sales in 1987 will be \$2 million is as nonfuzzy as S1, but has a higher level of uncertainty (assuming that 1987 sales are not predetermined).

Since the phenomena of fuzziness and uncertainty have different sources and characteristics, distinct measures should be used to represent and evaluate them, as suggested in [12]. In other words, every statement in a reasoning system should have two associated measures, a measure of fuzziness, and a measure of uncertainty. We denote these two measures by the symbols $\mu$ and $\pi$ , respectively. In an earlier paper [4], we have addressed the first part of the problem of supporting imprecise reasoning, by developing a methodology for representing and manipulating fuzzy knowledge. In this paper, we develop a formal method for reasoning with imprecise knowledge characterized by both fuzziness and uncertainty. In section 2, we review the literature on existing approaches to imprecise reasoning. In section 3, we extend the logic based representation method for fuzzy knowledge in [4], to include representation of uncertainty in knowledge. Then, methods to propagate the uncertainty measure during inferential reasoning and use it to control the search process are presented in section 4. This is followed by a small example, which illustrates how both fuzzy and uncertain knowledge can be used to solve unstructured problems, and how measures of imprecision can help interpret the reasoning process and the solutions generated.

## 2. Existing Approaches to Incorporating Imprecision in Reasoning

The earliest systems developed for automated reasoning avoided imprecision altogether, by restricting attention to problem domains such as mathematics and symbolic manipulation. However, once intelligent systems were designed for other applications, it became apparent that the models of the problem domains available to the system designers were inherently imprecise, so that some methods for reasoning with imprecise knowledge were essential. As a result, most intelligent systems in use or under development today support some form of imprecise reasoning. The drawback with most of the approaches used, however, is that they do not address both uncertainty and fuzziness. In fact, in many approaches, the two phenomena are not even separated. As a result, during the reasoning process, it is no longer clear which form of imprecision is present, and whether indeed both are present. Most of these approaches fall into one of two categories. The first category consists of approaches to reason with uncertain knowledge, that essentially ignore fuzziness. In the second category are those approaches that focus on fuzzines, of which some consider uncertainty as well. In this section, each of these categories is briefly reviewed.

## 2.1. Methods Dealing With Uncertainty

## 2.1.1. Bayesian Methods

The earliest and most traditional approach to uncertain reasoning is based on Probability and Bayesian theory [13]. In this approach, the reasoning process is usually based on a hypothesis-test paradigm. Entities represented in the knowledge base, and input data, are viewed as evidence which can be used to prove relevant hypotheses. Each item of evidence $E_{i}$ (and each hypothesis $H_{j}$ ) is assigned a prior probability $P(E_{i})(P(H_{j}))$ . In addition, the relationships between the different $E_{i}$ and the hypotheses they support are characterized by conditional or joint probabilities, which may be estimated from statistical samples. During the problem solving process, in which these relationships are instantiated (where relevant), to infer specific hypotheses, the conditional probability of each inferred hypothesis is computed using a mechanism such as Bayes rule. For instance, given a relationship of the form ‘If E then H’, the application of Bayes rule yields

$$
P (H \mid E) = \frac {P (E \cdot H)}{P (E)} = \frac {P (E \mid H) \cdot P (H)}{P (E)}.\tag{1}
$$

Although intuitively appealing, (1) is difficult to apply in practice. For one thing, all the terms on the right-hand side of (1) have to be known precisely. In practical situations, most of the probability values used are estimates, based either on statistical sampling or subjective intuition, and thus the above requirement cannot be enforced, leading to problems (such as $P(H|E) \geq 1$ ). In addition, when the evidence E is not a single atomic event or datum, but a combination $E_{1}, E_{2}, \ldots, E_{n}$ , the computation of $P(E)$ itself requires knowledge of all dependencies between its constituents, since

$$
\begin{array}{c} P (E) = P (E _ {1}) \cdot P (E _ {2} | E _ {1}) \dots \\ \times P (E _ {n} | E _ {1} \dots E _ {n - 1}), \end{array}\tag{2}
$$

where the order of evaluation is insignificant. Besides the difficulty of knowing all these dependencies, this model (2) requires the availability or computation of a very large number of conditional probabilities, which would easily become infeasible in practice. To avoid this problem, if the $E_{i}$ s considered are such that indeed independence holds, then the simplified form

$$
P (E) = \prod_ {i = 1} ^ {n} P (E _ {i}),\tag{3}
$$

can be used instead. It is clear that this formulation is much simpler, since far fewer probabilities are needed. On the other hand, this imposes limitations on the relationships that can be constructed, especially since mutual dependencies may not always be obvious. In practice, however, this is a viable approach, as illustrated by an example. Consider a rule in a medical knowledge base:

R2: IF the Agent is Viral AND A Vaccine is still Effective THEN Vaccinate.

If the determination of whether a vaccine is still effective involves consideration of the agent's characteristics (e.g., that it is viral), then the two premises are clearly dependent. Thus, (3) cannot be used, and (2) is the appropriate formulation of $\pi$ for the premise of R2. However, in such situations, it might be preferable to reformulate R2 into a set of rules in which (3) holds (by representing dependencies through implications as far as possible, and avoiding having dependent propositions as premises in the same rule). If the set of rules comprising a knowledge base largely conform to this approach, then indeed (3) can be used as the appropriate function for evaluating uncertain conjunctions. However, even this does not remove the first problem with (1), that of normalization.

In some existing systems, the Bayesian approach has been modified, by assuming conditional independence between the different $E_{i}$ , so that

$$
P (E _ {1}, \dots , E _ {n} | H) = \prod_ {i} P (E _ {i} | H)
$$

$$
\text { and } P (E _ {1}, \dots , E _ {n} | \overline {{H}}) = \prod_ {i} P (E _ {i} | \overline {{H}}),
$$

and by expressing uncertainty in terms of odds, rather than probabilities, where

$$
O (H) = \frac {P (H)}{P (\overline {{{H}}})} \text { and } O (H | E) = \frac {P (H | E)}{P (\overline {{{H}}} | E)}.
$$

Then the conditional odds of the implicand in a relationship can be computed as

$$
O (H \mid E) = \left[ \prod_ {i = 1} ^ {n} \frac {P (E _ {i} \mid H)}{P (E _ {i} \mid \overline {{{H}}})} \right] \cdot O (H).\tag{4}
$$

With this formulation, the problems of normalization are avoided, so that subjective estimates of probabilities can be used, as in PROSPECTOR [11], and AL/X [20]. The number of specific conditional probabilities that have to be computed (or stored) can still be large, although not as large as in (1) and (2).

## 2.1.2. Certainty Factors

This approach has been applied in a number of Expert Systems for diagnosis, such as MYCIN [22], EMYCIN [24], PUFF [16], and SACON [7]. Each hypothesis is assigned a certainty factor (CF) ( $-1 \leq CF \leq 1$ ) derived from associated measures of belief (MB) and disbelief (MD). These measures, and consequently, the CF, are revised during the diagnosis process by the incidence of each premise implying the hypothesis, so that the uncertainty in the hypothesis is always reflected in its CF. The combination of evidence in this approach is based on a set of rules, such as

(1) The CF of the implicand in a rule is the product of the rule's CF and the CF of the collective premise.

(2) The $CF$ of a conjunction of several propositions is the minimum of the $CF$ 's of each proposition.

(3) If several rules implying the same hypothesis are instantiated, the CF of the hypothesis is taken as the maximum such CF obtained.

The major drawback of this approach is that it provides no mechanism for dealing with fuzzy knowledge, and at the same time, loses some of the firm foundation that probability theory provides, due to its ad hoc structure. Nevertheless, its successful use in existing systems does support its validity for some specific problem types.

## 2.1.3. The Dempster-Shafer Theory of Evidence

This approach has attracted significant interest in recent years. Its major attraction is that instead of assuming that uncertainty can be measured precisely, each proposition X is represented by an interval estimate of uncertainty $(s, p)$ , where s is a lower band for $P(X)$ , and p is a lower bound for $P(\neg X)$ (and thus an upper bound for $P(X)$ ). As evidence is accumulated during the problem-solving process, these bounds are updated, using an ‘orthogonal sum’ operation to combine evidence. By using a conservative approach of preserving valid bounds on the true probability value, this approach is able to conform to probability theory without making some of the restrictive assumptions of other approaches. Although conditional independence between different premises in a rule is still assumed, a modified approach has been developed which avoids this assumption, and also includes some consistency checking capabilities for the derived uncertainty estimates [19].

## 2.1.4. Other Approaches

A variety of other, less general methods for incorporating uncertain knowledge and reasoning have been suggested. These include the use of Information Theory and Entropy, and the use of meta-level probability evaluation in logic-based systems. Although some of these have interesting theoretical bases, their applicability to a broad range of systems is as yet untested.

## 2.1.5. The Case for Fuzziness

All the approaches reviewed so far only address uncertainty. That is, they assume that there is no fuzziness in the knowledge and reasoning involved in the problem-solving process. Instead, in situations where there is inherent fuzziness in the knowledge used, these approaches use artificial categorization of concepts and relationships to avoid this fuzziness. However, as shown in [12], this often leads to unrealistic results and interpretations. For instance, consider the following rule [19].

IF Noise or cooling is Noticeable near the relief valve, THEN The relief valve has opened (PW 200, NW 0.5),

where PW and NW are weights used to modify the probability p of the implicand based on whether the premise has occurred or not, respectively. Here, in providing the input which forms the premise of the rule, a numerical imprecision factor p is also included. The interpretation of p in the AL/X framework [20] is as an uncertainty measure, with the term ‘Noticeable’ assumed to be categorical. However, consider the application of this rule in practice. The premise, along with an associated p-value, might be manually provided by a technician, or automatically by a sensor and transducer. In such situations, p is more representative of fuzziness (i.e., the membership level of the perceived noise level in the membership set of the fuzzy term ‘Noticeable’), than of uncertainty (in the observation of noise or cooling). In fact, there may be no uncertainty involved at all; and if there were any, some way of distinguishing between the two types of imprecision is needed. None of the approaches discussed so far provide any means to do this.

## 2.2. Methods for Incorporating Fuzziness

The second category of research on imprecise reasoning, which focuses on fuzziness as a source of imprecision, is generally based on the use of many-valued logics, and especially fuzzy logic [26]. Fuzzy logic is radically different from traditional binary logic. Its basis is that many concepts in natural language and problem domain knowledge are fuzzy, in that some of their elements may not have a binary membership level in the membership set of the concepts, but instead are characterized by a ‘possibility distribution’ $\Pi_{X}$ over the unit interval [0,1]. Thus, a fuzzy proposition $p\equiv\{X\text{ is }A\}$ , where X is a variable defined over the universe U and A is a fuzzy subset of U, can be represented by the possibility distribution

$$
\Pi_ {X} = \operatorname{poss} \left\{X = u \mid X \text {is} A \right\} = \mu_ {A} (u), \quad \forall u \in U,\tag{5}
$$

where $\mu_{A}(x)$ is the membership function of A (i.e., $\mu_{A}(x)$ specifies the membership level of x in the fuzzy set A). Using a suitable language (such as PRUF [28]), fuzzy propositions can be stated, and converted into equivalent possibility assignment equations by operators such as projection and particularization. During the problem-solving process, the compositional rule of inference [28] is used to draw fuzzy conclusions from these equations, and the underlying possibility distributions.

In situations where both fuzziness and uncertainty are present, the following approach has been proposed to evaluate the uncertainty. Given a probability space defined by $(R^{n}, \Sigma, P)$ , where $R^{n}$ is an Euclidean n-space, $\Sigma$ is the $\sigma$ -field of Borel sets in $R^{n}$ , and P is a probability measure over $R^{n}$ , the probability of a fuzzy event $A \in \Sigma$ is given by [27]

$$
P (A) = \int_ {R ^ {n}} \mu_ {A} (x) p (x) d x = E (\mu_ {A}),\tag{6}
$$

where $p(x)$ is the probability distribution function of A.

In general, however, Fuzzy logic has several drawbacks that limit its direct application for imprecise reasoning. First, its use of linguistic truth variables with structured countable sets of truth values for each such variable, poses several conceptual and implementation problems. One such problem is failure of closure. Given two fuzzy propositions A, B, truth values may be defined for them, as well as for some derivable propositions, such as $A \vee B$ , $\neg B$ , for instance. However, this does not imply that truth values for other derivable propositions such as $A \wedge B$ , $\neg A$ , etc. also exist. Thus there is no way of interpreting the possibility distributions of these latter propositions, if they are indeed derived. In other words, the implicit assumption that the truth values are subjective and linguistic limits the range of results and interpretations that can be derived, even though the mechanical procedures used are quite general.

Another problem is that instead of keeping the two phenomena and their measures distinct, as they should be, many researchers using this approach try to relate the two, and treat fuzziness as a weaker form of uncertainty [18]. In fact, in some cases, the two are functionally related:

$$
P _ {A} (S _ {i}) = \sum_ {j = 1} ^ {n} \frac {1}{j} \left(\mu_ {A} (s _ {j}) - \mu_ {A} (s _ {j + 1})\right),\tag{7}
$$

where A is an event which can have outcomes $s_{1}\ldots s_{n}$ , and the outcomes are ordered so that $\mu_{A}(s_{i})\geq\mu_{A}(s_{i}+1),\forall i.$ Also,

$$
\mu_ {A} (s _ {i}) = \sum_ {j = 1} ^ {n} \min \left(P _ {A} (s _ {j}), P (s _ {i})\right),\tag{8}
$$

which implies that $P_{A}(s_{i}) \leq \mu_{A}(s_{i}), \forall i$ . Furthermore, as pointed in [4], the direct application of fuzzy logic does not enable the representation of some types of fuzziness, such as that arising from fuzzy operators in relationships. Nevertheless, the use of fuzzy set theory to deal with fuzziness, along with appropriate measures for uncertainty, does provide an effective basis for imprecise knowledge representation and reasoning, and has been applied to several problem areas, such as medical diagnosis, structural damage assessment and pattern recognition.

## 3. Representation of Uncertain Knowledge

Several formal frameworks for the representation of unstructured knowledge in machine interpretable form have been developed, such as Production Systems, Inference Nets, Frames and Mathematical Logic [10]. Of these, logic, and in particular, First-Order Logic (FOL) [10], has some features that make it appealing for use in IDSS. These include the effectiveness of FOL as a basis for modeling and manipulating databases, the power of logic programming as a widely applicable programming tool, and the ease of generating explanations in logic based systems.

Knowledge in a logic based system is represented in three forms, namely atomic formulae (predicates), relationships (well-formed formulae), and procedures. In this section, we will describe how uncertainty in each of these three constructs can be represented.

## 3.1. Uncertainty in Atomic Formulae

Atomic formulae are used primarily to represent attributes of specific objects, or predicative relationships between objects. Uncertainty in an atomic formula (also referred to as a predicate or literal) is represented by a measure $\pi$ . which we call the certainty level $(0 \leq \pi \leq 1)$ . The $\pi$ -value of a literal indicates the certainty of the factual statement embodied in the literal, and is the lowest level at which uncertainty has to be represented in the knowledge base, consequently, the $\pi$ -value of a ground literal (in which all terms are constants) is provided explicitly in the knowledge base.

In the case of non-ground literals, the $\pi$ -value has to be computed once the literal is fully instantiated (i.e., once all its terms are bound to constants). This can happen in two ways. First, the literal may be directly matched with a ground literal stored in the knowledge base; alternatively, it may be instantiated by inferring it using one or more relationships available in the knowledge base. We will consider the first case here, and defer the latter case till the next subsection.

If the match between a non-ground literal and a ground literal is precise, then the $\pi$ -value of the latter is directly passed to the former. The situation is somewhat more complicated when the match is fuzzy. To illustrate this, consider the proposition S4: Sales in 1987 will be High as a goal statement we want to prove. Assume that during the solution process the statement S5: Sales in 1987 will be 1.75 million is generated, with an associated certainty level $\pi = 0.8$ (a likely interpretation of this measure is as 80 percent). Also, let the attribute value 'High' b characterized by a fuzzy set in which $\mu_{High}$ (1.75 million) = 0.9. Then a fuzzy match can be made between S4 and S5.

However, in doing so, it is not immediately clear how to deal with the certainty level for the goal statement that is inferred. Since S4 is a fuzzier statement than S5, and since it is also satisfied by values of sales other than \$1.75 million, it should be more certain than S5. However, if the inferred statement is interpreted as S6: Sales in 1987 will be High to a degree $\mu = 0.9$ , which is more precise than S4, then $\pi = 0.8$ could indeed be a valid estimate of the certainty of this statement.

A question that may arise here is, whether statements S5 and S6 are equivalent, and if so, what do we gain by using the fuzzy terms at all. There are two reasons why the use of fuzzy terms is still justified. First, the two statements are not equivalent in general, even though they might be in specific instances. This is because, there may be several elements in the membership set of 'High' with $\mu = 0.9$ , and thus the statement S6 would be less precise than S5. Furthermore, the use of fuzzy terms enables the representation of knowledge using more realistic concepts that are inherently fuzzy, and not categorical in a boolean sense.

Given that the derivation of solution statements such as S6 is desirable, an appropriate value of $\pi$ for such statements has to be derived as well. In general, the uncertainty measure $\pi_{0}$ for a proposition with a fuzzy value X having a value of $\mu = \mu_{0}$ is given by

$$
\pi_ {0} = \sum \pi_ {i},\tag{9}
$$

where $I = [x \mid \mu_{X}(x) = \mu_{0}]$ . In the case where the attribute value X is fuzzy, but $\mu$ is not known. The relevant certainty level is

$$
\pi_ {0} = \sum_ {i \in X} \pi_ {i}.\tag{10}
$$

In practice, it is often the case that $\mu_{0}$ is known for specific instances, but the distribution of $\pi_{i}$ is not known over the fuzzy set X. In such situations, an approximation which is appropriate is

$$
\pi_ {0} = \sum_ {i \in I _ {1}} \pi_ {i},\tag{11}
$$

where $I_{1}=\{i\in I\mid\mu_{i}=\mu,\pi_{i}\text{ known}\}$ . This always yields a lower bound on the $\pi$ -value, which should be the case when information is incomplete.

## 3.2. Uncertainty in Relationships

A common characterization of relationships in automated reasoning systems, such as rule-based systems, is as 'IF premise THEN implicand', where the premise may be a conjunction of specific conditions (predicates), and the implicand is a hypothesis or conclusion. Since this characterization is fairly general, it will be used here. In logic based systems, such relationships are expressed in the form

$$
P _ {1} \wedge P _ {2} \wedge \dots \wedge P _ {n} \rightarrow B.\tag{12}
$$

In an imprecise knowledge base, some relationships may be imprecise too, and a more general form than (12) for a logic based relationship is

$$
w _ {1} P _ {1} \wedge^ {k} w _ {2} P _ {2} \dots \wedge^ {k} w _ {n} P _ {n} \rightarrow {} ^ {\gamma} B,\tag{13}
$$

where the terms $w_{i}$ are used to specify the relative weights of different premises in the relationship, and k is a parameter defining the level of conjunction in the premise. We have already shown, in [4], how fuzziness can be represented in such relationships, and how it can be propagated during inferential problem solving. However, methods to propagate uncertainty in fuzzy knowledge are also needed, in order to effectively construct and evaluate problem solutions, and we will address this problem here.

One alternative is to use the same propagation technique for both fuzziness and uncertainty. However, the different characteristics of the two phenomena make this infeasible. Uncertainty is usually related to the concept of probability, and thus it is desirable to propagate it using methods that are conformal with the calculus of probability theory where relevant. On the other hand, we view the fuzziness measure $\mu$ as a level of set membership, with its value representing how close a particular element is to full membership in a specified set. This motivates the view of a fuzziness measure as a distance, and the use of a norm-based method for evaluating fuzziness. When relationships involving logical operators are encountered, such as conjunctions of propositions, the certainty level of the intersections characterizing the conjunctions are computed typically by probability-like calculi that generally yield

$$
P \left(A _ {1} \wedge A _ {2} \dots A _ {N}\right) \ll P \left(A _ {i}\right), \quad i = 1, \dots , n,\tag{14}
$$

and $P(A_1 \wedge \ldots A_N)$ could be much smaller than $\min_i P(A_i)$ , even if all the $P(A_i)$ are very similar. On the other hand, viewing fuzziness as a distance, the $\mu$ -value of such a conjunction would be much higher (for instance, if $\mu_{A_{1}} = \mu_{A_{2}} \ldots = \mu_{A_{n}} = \mu_{0}$ , then the $\mu$ -value of the combined expression would be $\mu_{0}$ ). It follows that the two phenomena require different propagation methods. The problem thus is to develop a calculus for the propagation of uncertainty for (possibly fuzzy) relationships.

## 3.2.1. Imprecise Conjunction

The relationships that are encountered for unstructured problems can be modeled using the two logical operators of conjunction and implication. In the case of the former, if the uncertainty measure is interpreted as a probability measure, then the uncertainty of the collective premises in a relationship of the form (12) can be calculated using a Bayesian argument, as in (2) (and (3) if we assume that the propositions are independent).

$$
\pi (E) = \pi (E _ {1}) \cdot \pi (E _ {2} | E _ {1}) \dots \pi (E _ {n} | E _ {1} \dots e _ {n - 1}),\tag{2}
$$

$$
\pi (E) = \prod_ {i = 1} ^ {n} \pi (E _ {i}).\tag{3}
$$

However, imprecise relationships may have weaker forms of conjunctions, characterized by the parameter k, and also by unequally weighted premises, as in (13). The impact of these factors on the evaluation of uncertainty must be considered. First, if one premise is more significant than another in implying a conclusion, it would seem intuitively sound that the uncertainty in the conclusion should be more closely related to that in the more important premise. To see this, consider the following abstract rule:

$$
0. 9 A _ {1} \wedge^ {\infty} 0. 1 A _ {2} \rightarrow {} ^ {1} B,\tag{15}
$$

with $\pi_{A_{1}}=1$ and $\pi_{A_{2}}=0.4$ . Then, assuming that $A_{1}$ and $A_{2}$ are independent, we would get $\pi_{B}=0.4$ . However, given that $A_{1}$ is certain, and the predominant determinant of B, this seems an unreasonable estimate for $\pi_{B}$ . Thus, some method that allows unequally weighted terms in a conjunction should be used. In addition, the factor k in (13) also has to be considered, since this parameter defines the form of the conjunction in the premise of a rule. In other words, the level of certainty in the premise should be related to the form of the relationship between the different component premises, and k is integral to this form. The direct application of probability theory provides no means to achieve this.

Based on these considerations, we present a model of uncertainty propagation through conjunction operators in relationships, which not only conforms with probability theory where valid, but also incorporates the effects of $w_{i}$ and k. If a relationship is of the form (13), and if $\pi_{1}, \pi_{2}, \ldots, \pi_{n}$ are the levels of certainty in the individual premises, then the $\pi$ -value of the composite premise is given by

$$
\pi_ {\left(w _ {1} A _ {1} \wedge {} ^ {k} w _ {2} A _ {2} \dots \wedge {} ^ {k} w _ {n} A _ {n}\right)} = \left[ \prod_ {r = 1} ^ {n} \pi_ {r} ^ {w _ {r}} \right] ^ {[ 1 / \Sigma_ {i} w _ {i} ^ {k} ] ^ {1 / k}},\tag{16}
$$

which can also be expressed as

$$
\pi_ {\left(w _ {1} A _ {1} \wedge {} ^ {k} w _ {2} A _ {2} \dots \wedge {} ^ {k} w _ {n} A _ {n}\right)} = \prod_ {r = 1} ^ {n} \pi_ {r} ^ {w _ {r} ^ {*}},\tag{17}
$$

where $w_{r}^{*}=w_{r}/[\sum_{i}[w_{i}^{k}]]^{1/k}$ , $\forall r$ is the k-normalized weight of $A_{r}$ in the relationship.

## 3.2.2. Properties of the Uncertainty Function

(1) Interpretation of $w_{i}$ . Given a proposition of the form $w_{1}A_{1} \wedge^{k}w_{2}A_{2}\ldots w_{n}A_{n}$ , its certainty level should be affected by the certainty levels of the different components $A_{j}, i = 1\ldots n$ , in accordance with their weights. That is, the $\pi$ -value of the collective proposition should be determined more by those $A_{i}$ that have a high relative weight (we stress the word relative because a proportionate increase in all the weights $w_{i}$ leaves the resulting $\pi$ -value unchanged). Thus, the effects of the weights $w_{i}$ can be examined better when the uncertainty function is stated in the functional form (17). In that form, since $0 \leq \pi$ , $w_{i} \leq 1$ , $\pi_{i}^{w_{i}^{*}} \geq \pi_{i}$ , and as $w_{i}^{*}$ decreases, $\pi_{i}^{w_{i}^{*}}$ approaches 1 for any $\pi_{i}$ , thus progressively decreasing the impact of $\pi_{i}$ on the certainty level for the conjunction. In the limit, when $w_{i}^{*} = 0$ , then $\pi_{i}^{w_{i}^{*}} = 1$ , and hence the $i$ th term becomes totally inconsequential. On the other hand, if a particular term $A_{j}$ has $w_{j}^{*} = 1$ and all other $w_{i}^{*} = 0$ , then $\pi$ in (17) becomes $\pi_{j}$ , which again conforms to intuition.

(2) The effect of k. In the uncertainty function (17), the weights $w_{i}^{*}$ are normalized using a kth order norm, where the factor k characterizes the conjunction operator in the relationship. Thus, as k varies, so should the uncertainty level in the relationship. To see this, consider the following conjunction:

$$
R = (1 0) A \wedge^ {k} (1) B.\tag{18}
$$

If $k = \infty$ , then the conjunction is strict, and thus the uncertainty function should resemble the product form of a probabilistic conjunction as far as possible. However, as k decreases, the conjunction becomes progressively weaker, and hence its certainty value should be correspondingly higher (in an extreme case, if the operator were a disjunction, then the certainty value would be the highest). As shown in the following proposition, the uncertainty function does indeed display this behavior, which is consistent with intuition (based on Mean of order k, and Sum of order k, in [5, pp. 16–18]).

Proposition. The uncertainty function in (16) is a monotonically non-increasing function of $k$ , $\forall k \geq 1$ .

Proof.

$$
\pi (k) = \left[ \prod_ {i} \pi_ {i} ^ {w _ {i}} \right] ^ {(1 / \Sigma_ {i} w _ {i} ^ {k}) ^ {1 / k}} = A ^ {L},
$$

where $A = \prod_{i}\pi_{i}^{w_{i}}$

$$
\text { and } L = \frac {1}{\left[ \sum_ {i} w _ {i} ^ {k} \right] ^ {1 / k}} \Rightarrow \ln (\pi (k)) L \cdot \ln (A),
$$

$$
\frac {1}{\pi (k)} \cdot \frac {\mathrm{d} \pi}{\mathrm{d} k} = \ln (A) \cdot \frac {\mathrm{d} L}{\mathrm{d} k},
$$

$$
\begin{array}{l} \frac {\mathrm{d} L}{\mathrm{d} k} = \frac {\ln \left[ \sum_ {i} w _ {i} ^ {k} \right]}{k ^ {2} \left[ \sum_ {i} w _ {i} ^ {k} \right] ^ {\frac {1}{k}}} - \frac {\sum_ {k} \left(w _ {i} ^ {k} \cdot \ln (w _ {i})\right)}{k \left[ \sum_ {i} w _ {i} ^ {k} \right] ^ {\left(1 + \frac {1}{k}\right)}} \\ = \left[ \frac {\ln \sum_ {i} w _ {i} ^ {k}}{k} - \frac {\sum_ {i} \left(w _ {i} ^ {k} \cdot \ln (w _ {i})\right)}{\sum_ {i} w _ {i} ^ {k}} \right] \cdot \frac {1}{\left[ \sum_ {j} w _ {j} ^ {k} \right] ^ {\frac {1}{k}}}, \\ \geq 0, \forall w _ {i} \geq 0, k \geq 1, \end{array}
$$

$$
\begin{array}{r l} & \left(\text { since } \sum_ {i} w _ {i} ^ {k} \ln \left[ \sum_ {j} \left(w _ {j} ^ {k}\right) \right] \geq \sum_ {i} \left(w _ {i} ^ {k} \cdot \ln \left(w _ {i} ^ {k}\right)\right), \right. \\ & \quad \left. \forall w _ {i} \geq 0, k \geq 1\right) \end{array}
$$

$$
\Rightarrow \frac {\mathrm{d} L}{\mathrm{d} k} \geq 0, \forall k \geq 1.
$$

also, $\ln (A) = \sum_{i}w_{i}\cdot \ln (\pi_{i})\leq 0$ since $\pi_i\leq 1,\forall i$

$$
\text { Thus, } \frac {\mathrm{d} \pi}{\mathrm{d} k} = \pi (k) \cdot \ln (A) \cdot \frac {\mathrm{d} L}{\mathrm{d} k} \leq 0.
$$

since $\pi(k)$ is always non-negative. Q.E.D.

(3) Disjunctions. Although we assume that relationships are expressed in terms of conjunctions and implications only, the representation method can be used to interpret an imprecise disjunction as well, as:

$$
\pi_ {(w _ {1} A _ {1} \vee^ {k} w _ {2} A _ {2})} = \pi_ {1} ^ {w _ {i} ^ {*}} + \pi_ {2} ^ {w _ {2} ^ {*}} - \pi_ {(w _ {1} A _ {1} \wedge^ {k} w _ {2} A _ {2})}\tag{19}
$$

(4) Strict conjunctions. In the extreme case when the conjunction of premises in a relationship is precise, then $k = \infty$ , and the outer term becomes

$$
L (\infty) = 1 / \max _ {i} w _ {i}\tag{20}
$$

$$
= 1 / w \quad \text { if } \quad w _ {1} = w _ {2} = \dots = w _ {n} = w.\tag{21}
$$

In the case of (21), the conjunction reduces to a conventional FOL conjunction, and the application of (16) gives

$$
\pi_ {w A _ {1} \wedge^ {\infty} w A _ {2} \dots \wedge^ {\infty} w A _ {n}} = \left[ \left[ \prod_ {i} \pi_ {i} \right] ^ {w} \right] ^ {\frac {1}{w}},
$$

which in turn gives

$$
\pi_ {w A _ {1} \wedge^ {\infty} w A _ {2} \dots \wedge^ {\infty} w A _ {n}} = \prod_ {i} \pi_ {i} = \pi (A _ {1} \wedge A _ {2} \dots \wedge A _ {n}),\tag{22}
$$

which is a probabilistic interpretation, as in (3) (assuming independent premises). Thus the use of (16) includes the conventional interpretation of nonfuzzy relationships as a special case. Furthermore, in the situation of (20), where the weights are possibly unequal, the effect of $L$ is determined by the relative values of the $w_{i}$ , ranging from the case of (22) to that of $\pi = \eta_{i_r}$ , when $w_{i_r} = 1$ , and all other $w_{i}$ 's are 0.

(5) $\pi = 1$ when $\pi_{i} = 1$ , $\forall i$ , regardless of the values of $k$ and $w_{1}, \ldots, w_{n}$ .

(6) Conjunctions of dependent propositions. In section 2, we had seen that most existing methods for evaluating uncertainty assume that when there is a conjunction of several propositions in the premise of a rule, the different propositions are mutually (or conditionally) independent. The result of this assumption is, in the Bayesian approach for instance, that (3) can be used instead of (2), to evaluate the conjunction. When only strict conjunctions of equally weighted propositions are allowed in the knowledge representation framework, as is the case with most existing methods, the justification of this assumption is limited by every possible dependency to the same extent. Consequently, the use of this assumption implies very careful and restrictive rule formulation. This can be an unreasonable burden, since even a domain expert providing rules could find it very difficult to analyse all possible dependencies before composing a rule (even when the number of propositions in a conjunction is fairly small). On the other hand, when fuzzy rules are allowed, as in our framework, even though the uncertainty function (16) does assume independence between the terms $A_1, \ldots, A_n$ , the impact of this assumption is somewhat reduced. To see this, consider two propositions $A_i$ and $A_j$ in a conjunction (of order $k$ and possibly involving other propositions too), with weights $w_i$ and $w_j$ respectively. The effect of $\pi_i$ and $\pi_j$ on the $\pi$ -value of the conjunction is determined by the values of $w_i^*$ and $w_j^*$ respectively. Thus if $A_i$ and $A_j$ are indeed dependent on each other, the impact of this dependency is only significant in the $k$ -conjunction if both $w_i^*$ and $w_j^*$ are large. The consequence of this is that whenever a rule involves a fuzzy conjunction ( $k$ small) with unequally weighted components in the conjunction, the independence assumption is justified as long as no major dependencies hold between the most significant terms. Of course, this mitigating effect is not achieved in conjunctions in which all the components are equally or similarly weighted. However, since many 'real' rules are likely to be fuzzy with a 'skewed' distribution of weights, the use of (16) can reduce the impact of missed dependencies on the effectiveness of rules formulated in the knowledge base.

(7) Associativity of conjunctions with same k. Although the uncertainty function is not strictly associative, in the case when a single k is involved, a weaker form of associativity holds, with modified weights, as with the $\mu$ -function for fuzziness. Thus,

$$
\pi_ {(w _ {1} A _ {1} \wedge^ {k} w _ {2} (w _ {3} A _ {3} \wedge^ {k} w _ {4} A _ {4}))} = \pi_ {(w _ {1} A _ {1} \wedge^ {k} \overline {{w}} _ {3} A _ {3} \wedge^ {k} \overline {{w}} _ {4} A _ {4})},\tag{23}
$$

where $\overline{w}_3 = w_3w_2 / (w_3^k +w_4^k)^{1 / k}$ , and $\overline{w}_4 = w_4w_2 / (w_3^k +w_4^k)^{1 / k}$ are the modified weights of $A_{3}$ and $A_{4}$ respectively.

$$
\begin{array}{l} \text {Proof.} \\ \pi_ {(w _ {1} A _ {1} \wedge {} ^ {k} w _ {2} (w _ {3} A _ {3} \wedge {} ^ {k} w _ {4} A _ {4}))} \\ = \left[ \pi_ {1} ^ {w _ {1}} \cdot \left[ \pi_ {3} ^ {w _ {2} w _ {3}} \cdot \pi_ {4} ^ {w _ {2} w _ {4}} \right] ^ {1 / [ w _ {3} ^ {k} + w _ {4} ^ {k} ] ^ {1 / k}} \right] ^ {1 / [ w _ {1} ^ {k} + w _ {2} ^ {k} ] ^ {1 / k}} \\ = \left[ \pi_ {1} ^ {w _ {1}} \cdot \pi_ {3} ^ {\overline {{w}} _ {3}} \cdot \pi_ {4} ^ {\overline {{w}} _ {4}} \right] ^ {1 / [ w _ {1} ^ {k} + w _ {2} ^ {k} ] ^ {1 / k}}, \end{array}
$$

$$
\begin{array}{l} \text { since } \overline {{w}} _ {3} ^ {k} + \overline {{w}} _ {4} ^ {k} = w _ {2} ^ {k}, \\ = \left[ \pi_ {1} ^ {w _ {1}} \cdot \pi_ {3} ^ {\overline {{w}} _ {3}} \cdot \pi_ {4} ^ {\overline {{w}} _ {4}} \right] ^ {1 / [ w _ {1} ^ {k} + \overline {{w}} _ {3} ^ {k} + \overline {{w}} _ {4} ^ {k} ] ^ {1 / k}} \\ = \pi_ {(w _ {1} A _ {1} \wedge^ {k} \overline {{w}} _ {3} A _ {3} \wedge^ {k} \overline {{w}} _ {4} A _ {4})}. \end{array} \quad \mathbf {Q . E . D .}
$$

This property is very useful where applicable, since it allows greater flexibility in the problem solving process. By transforming nested conjunctions into single level conjunctions, each term in the resulting relationship can be explored independently, so that some degree of parallel processing can be achieved. This is further facilitated by the fact that the form of ‘pseudo-associativity’ that holds in the uncertainty function is exactly the same as that in the norm-based function used to propagate fuzziness. Therefore, an identical decomposition of the problem can be achieved for the consistent propagation of both major forms of imprecision. Of course, this is possible only when nested relationships involve the same value of k, whereas theoretically k could assume any value in the range $1 \leq k \leq \infty$ . Nevertheless, most real relationships can be modeled adequately by choosing k from a small set of discrete choices, and thus at least partial decomposition of problems can be effected as above (whenever subproblems involving a single k are identified).

## 3.2.3. Implication

The other operator of concern is the implication operator ( $\rightarrow$ ). If an implication is a precise and certain one, then the certainty level of the implicand should be the same as that of the premise. The reason for this is that in an inferential system, knowledge of the truth value of an implicand in a rule is limited by what is known about the premise of rule. In cases where the implication is itself uncertain, it is usually characterized by a factor (we call this $\gamma$ , with $0 \leq \gamma \leq 1$ ). The certainty level of the implicand inferred via such a rule (say $A \rightarrow B$ ) is then given by

$$
\pi_ {B} = \gamma \times \pi_ {A}.\tag{24}
$$

This formulation ignores the presence of any fuzziness. However, since imprecise knowledge may be both uncertain and fuzzy, it is necessary to consider the impact of fuzziness upon uncertainty representation and propagation. We have already seen how uncertainty in conjunctions takes fuzziness in the conjunctive expression (represented by the parameter k and the weights $w_{i}$ ) into account.

Similarly, uncertainty propagation through implication is also affected by fuzziness in the knowledge used, and this interaction can be quite significant. For example, consider the rule 'If sales growth is high, then stockprice is volatile', which can be represented as

$$
S A L E S G R O W T H (x, H i g h)
$$

$$
\rightarrow {} ^ {\gamma} S T O C K (x, \text { Volatile }).
$$

This rule may hold with different certainty levels for different ranges of $\mu$ -values of the premise. For instance, when the sales growth is clearly high, the certainty in the stock price being volatile is greater than when the sales growth is only marginally high. Thus, $\mu_{SALESGROWTH(x,High)}$ affects $\mu_{STOCK(x,Volatile)}$ as well as $\pi_{STOCK(x,Volatile)}$ . It is clear that if such interaction is ignored in the process of imprecise reasoning, the axioms (rules) contained in a knowledge base would be restricted to only specialized subsets of unstructured problems (i.e., those for which fuzziness is not a significant factor, and $\mu\simeq1$ for all propositions concerned). Effective uncertainty propagation through the implication operator thus requires a function which takes the interaction of fuzziness and uncertainty into account. A generalized form of such a function, which modifies the uncertainty in the consequent if the antecedent of an axiom is fuzzy, can be expressed as follows, for a relationship of the form $A\to B$ :

$$
\pi_ {B} = f \left(\pi_ {A}, \mu_ {A}, \gamma\right),\tag{25}
$$

where $\gamma$ is a normalized factor characterizing the uncertainty in the implication when no fuzziness is present. That is, when $\mu_{A}=1$ , then $\pi_{B}$ is computed as in (24). The definition of a suitable function f for (25) requires the consideration of several features that are desirable in such a function

(a) When $\pi$ and $\mu$ are related, $\pi$ should be a monotonically non-decreasing function of $\mu$ . This results from the usual interpretation of an implication as a positive statement; that is, the greater the extent to which a premise holds, the greater should be the certainty of the implicand being true. Violation of this property would suggest an inverse form of relationship between the premise and implicand, which is contradictory to the interpretation of implication.

(b) The function $f$ should allow situations where $\pi \geq \mu$ . Such situations can occur, since fuzziness and uncertainty have different sources, and although they interact, each can occur independent of the other. For instance, a statement may be very fuzzy (i.e., $\mu \ll 1$ ), even though it is certain ( $\pi \simeq 1$ ).

(c) The function $f$ should allow situations where $\pi$ and $\mu$ are not related. That is, it should permit representation of relationships in which the certainty level of the implicand is not affected by any fuzziness in the premise. Such a situation would occur when the implication itself is certain, so that the only source of uncertainty is the premise.

Based on these desirable characteristics, we use the following formulation for propagating uncertainty through an imprecise implication:

$$
\pi_ {B} = [ \gamma ] ^ {1 / \mu_ {A}} \cdot \pi_ {A},\tag{26}
$$

In other words, $\pi_B = \gamma_{eff} \cdot \pi_A$ , where $\gamma_{eff} = \gamma^{1/\mu_A}$ represents the imprecision in the implication itself. The choice of this function is based on several factors. First, it possesses all the above characteristics. The first one, (a) follows from the non-negativity of $\gamma$ and $\mu$ . For (b), when $\mu_A = 1$ , then (25) yields $\pi_B = \gamma \cdot \pi_A$ , which is a commonly accepted model of an uncertain implication. On the other hand, when $\mu < 1$ , then $\pi_B \leq \gamma \cdot \pi_A$ ; however, $\pi_B$ may be greater than $\mu_B$ . Also, in situations where (c) is relevant, the independence of $\pi$ and $\mu$ is achieved by setting $\gamma = 1$ , which logically corresponds to a certain implication.

In the previous section, we considered the special case of nested conjunctions with the same k-levels, and showed how such nested expressions could be factorized into simpler expressions. When imprecise implications are present in relationships, the situation is somewhat complicated. However, the associative property is still achieved for the same special case (i.e., when all the conjunctions in the nested expression have the same k-level), due to the separable nature of the functions used. To see this, consider the following two rules:

$$
w _ {1} A \wedge^ {k} w _ {2} B \rightarrow {} ^ {\gamma_ {1}} C,\tag{27}
$$

$$
w _ {3} F \wedge^ {k} w _ {4} G \rightarrow {} ^ {\gamma_ {2}} B.\tag{28}
$$

If (28) is used to interfere and substitute B and its $\pi$ -value for (27), it is clear that (23) cannot be directly applied. However, in this case, the following applies:

$$
\begin{array}{r l} \pi_ {C} & = \gamma_ {1} ^ {\frac {1}{\mu_ {(w _ {1} A \wedge^ {k} w _ {2} B)}}} \cdot \pi_ {(w _ {1} A \wedge^ {k} w _ {2} B)} \\ & = \gamma_ {1} ^ {\frac {1}{(w _ {1} A \wedge^ {k} w _ {2} B)}} \cdot \left[ \pi_ {A} ^ {w _ {1} ^ {*}} \cdot \pi_ {B} ^ {w _ {2} ^ {*}} \right] \\ & = \gamma_ {1} ^ {\frac {1}{\mu_ {(w _ {1} A \wedge^ {k} w _ {2} B)}}} \\ & \cdot \left[ \pi_ {A} ^ {w _ {1} ^ {*}} \cdot \left[ \gamma_ {2} ^ {\frac {1}{\mu_ {(w _ {3} F \wedge^ {k} w _ {4} G)}}} \cdot \pi_ {(w _ {3} F \wedge^ {k} w _ {4} G)} \right] ^ {w _ {2} ^ {*}} \right] \\ & = \gamma_ {1} ^ {\frac {1}{\mu_ {(w _ {1} A \wedge^ {k} w _ {2} B)}}} \cdot \gamma_ {2} ^ {\frac {w _ {2} ^ {*}}{\mu_ {(w _ {1} F \wedge^ {k} w _ {4} G)}}} \cdot \left[ \pi_ {A} ^ {w _ {1} ^ {*}} \cdot (\pi_ {F} ^ {\overline {{w}} _ {3}} \cdot \pi_ {G} ^ {\overline {{w}} _ {4}}) ^ {w _ {2} ^ {*}} \right] \\ & = \gamma_ {1} ^ {\frac {1}{\mu_ {(w _ {1} A \wedge^ {k} w _ {2} B)}}} \cdot \gamma_ {2} ^ {\frac {w _ {2} ^ {*}}{\mu_ {(w _ {3} F \wedge^ {k} w _ {4} G)}}} \\ & \cdot \left[ \pi_ {(w _ {1} A \wedge^ {k} (w _ {2} ^ {*} \overline {{w}} _ {3}) F \wedge^ {k} (w _ {2} ^ {*} \overline {{w}} _ {4}) G)} \right], \end{array} \tag {29}
$$

where $\overline{w}_{3}=w_{3}/(w_{3}^{k}+w_{5}^{k})^{1/k}$ , and $\overline{w}_{4}=w_{4}/(w_{3}^{k}+w_{4}^{k})^{1/k}$ are the normalized weights of the premises in (28). Thus, when the different conjunctions in a nested expression are of the same level k, uncertainty in implication operators can be separated from that in the conjunctions, so that problem decomposition can still be achieved. In general, this situation is unlikely to occur very often, since the value of k may be anywhere in the range $1\leq k\leq\infty$ . However, the effect of changing k upon the values of the normalised weights $w_{i}^{*}$ in (17) is significant only for low values of k (less than 10); thus, it is usually adequate to choose k from the range ( $1\leq k\leq10$ ), and even restrict it to a few discrete values (e.g., $1\;3\;5\;9\;\infty$ ). Not only does this improve the likelihood of identifying situations where the associativity property can be applied, to facilitate distributed proof generation (i.e., preventing the need for depth-first search), but research on human choice behavior shows that choosing from a small discrete set of choices is a much easier cognitive task than choosing from a large range, or a continuum [15].

## 4. Inference with Uncertain Knowledge

In this section, the use of the representation methods presented in the previous section in knowledge manipulation and problem solving will be studied. In inferential reasoning, a problem is usually stated as a theorem to be proved (a wff whose truth is to be established). A common way to develop a proof is by using a backward search method [17]. During the search process, for each literal (predicate) in the current goal statement, if a stored ground literal (data relation tuple) that matches with it can be found, then the stored literal provides a candidate solution to the subproblem represented by the goal literal. Otherwise, the predicate is substituted by the premise of a rule whose implicand it matches. Thus the search can be represented graphically by a tree. The nodes of the tree are the different literals (predicates) in the proof, and the edges correspond to implicative relationships. The proof consists of two processes. The first is the search process, which causes the tree to grow. The other is the evaluation process, in which different instances of literals that are generated by the search are evaluated. If the instances are acceptable, the appropriate information is passed up the tree; the evaluated portion of the tree is then pruned. The proof is completed when the original goal is evaluated successfully.

When knowledge is precise, the evaluation process is based on boolean logic. However, when imprecise knowledge is involved, the evaluation process includes the computation and propagation of the relevant imprecision measures. Rules for achieving this for the fuzziness measure have been developed [4]. Corresponding methods for the certainty level $\pi$ need to be developed, and this problem is addressed next.

The portion of the proof process that is affected by uncertainty is the evaluation process. Part of the evaluation of any node (literal) is the level of uncertainty in the generated instance of the literal. When the instance is generated by matching with an explicit ground literal in the knowledge base, the $\pi$ -value of the node is essentially the $\pi$ -value of the ground literal (usually 1), unless the match is fuzzy one, rather than an exact match, in which case, the $\pi$ -value of the node literal may require additional computation, as discussed in section 3.1. Of course, if the ground literal is certain, then so is the node literal, regardless of the fuzziness of the match.

On the other hand, when the node literal is inferred using a rule, it is evaluated only when it becomes a leaf node (i.e., when all the propositions in the rule implying this node literal have been evaluated). If successful matches are achieved for all these children nodes, the $\pi$ -value for the literal is computed using (16) and (26). Here again, if the match between the node literal and the implicand literal in the underlying rule was fuzzy, the situation described in the previous paragraph re-occurs.

The inclusion of uncertainty (and fuzziness) does impose an additional computational burden at each node in the proof tree. However, the methods used to compute the $\pi$ -values are such that this effect can be mitigated in several ways. For instance in (17), the normalized weights $w_{i}^{*}$ can be computed when the rule is added to the knowledge base, rather than during each proof generation instance. Furthermore, the modified weights $\overline{w}_{i}^{*}$ needed when property 7 in section 3.2.2 is used to factorize the goal expression, are computed by a single product, since [using the example in (29)], the normalized weights of F and G in the factorized conjunction are

$$
\overline {{{w}}} _ {3} ^ {*} = w _ {2} ^ {*} \cdot \overline {{{w}}} _ {3} \quad \text { and } \quad \overline {{{w}}} _ {4} ^ {*} = w _ {2} ^ {*} \cdot \overline {{{w}}} _ {4}.\tag{30}
$$

The significance of the uncertainty measure is more than merely an additional item of information. In fact, it can be used to modify the proof process. In other words, the $\pi$ -value of a literal can be actually used to make control decisions, such as whether an instance is acceptable or not. This is an important feature, since it avoids the generation of solutions that are highly unlikely (i.e., $\pi \ll 1$ ). It is achieved by setting a boundary values $\pi_{i}^{0}$ for each node i, which denotes the lowest acceptable value of $\pi_{i}$ (the value of $\pi_{i}^{0}$ may be anywhere in the range [0,1], and a default such as 0.5 can also be used). Then, if the evaluated $\pi_{i}$ for a candidate instance of i is less than $\pi_{i}^{0}$ , the candidate is rejected, and an alternative instance is sought. The boundary value $\pi_{i}^{0}$ can be used in two ways. First, during the search process, it helps screen out rules that are potentially useless for a problem instance; second, during evaluation, it can be used to propagate $\pi$ -values, in a form accessible and useful to the system user.

## 4.1. Interaction Between Fuzziness and Uncertainty

Interaction between the measures for fuzziness and uncertainty occurs for all the constructs used to represent knowledge, that is atomic formulae as well as relationships and procedures. In this section, we review the type of interaction that can occur, and examine the impact of this upon the reasoning process and solutions generated.

In the case of atomic formulae (predicates), fuzziness in one or more of the terms of an inferred predicate affects its $\pi$ -value as discussed in section 3.1. We have also seen how the increased complexity of this situation can be alleviated by making suitable assumptions. In the case of relationships, fuzziness affects the propagation of uncertainty through both the conjunction and the implication operators. For instance, the function used to compute the $\pi$ -value of a conjunction takes into account the weights $w_{i}$ and the parameter k that together characterize the fuzziness in the expression. As for implication, in the previous section we have seen how the evaluation function (26) enables dependency of the $\pi$ -value of the implicand in a relationship on the $\mu$ -value of its premise to be accommodated. This dependency is important, since it allows the representation of rules where the ‘strength’ of the rule (characterized in (26) by the factor $\gamma^{1/\mu}_{Premise}$ ) is affected by the fuzziness in its premise, which is fairly common in practice (yet, existing methods for representing imprecise knowledge do not allow this dependency).

A consequence of all this interaction between $\pi$ and $\mu$ is that both measures are needed in order to effectively reason with imprecise knowledge. For example, just knowing the $\pi$ -value of a solution does not reveal how much of the uncertainty in this solution is attributable to fuzziness in the knowledge and relationships used. The situation may vary between two extremes

(a) where no fuzziness is present in the data, so that all the uncertainty is due to uncertainty in the data used, and

(b) where all the data used is certain, yet fuzziness in the data caused uncertainty in the conclusions drawn.

Another consequence is that a solution generated may have an acceptable $\mu$ -value, and yet, this $\mu$ -value may be low enough to cause the associated $\pi$ -value to be unacceptably low. This is more likely to occur for weaker rules (i.e., those with low $\gamma$ ), and is a useful feature, since it enables the use of weak rules, with the security that such rules are more critically evaluated (i.e., they are acceptable only with relatively precise inputs). From the standpoint of control of the proof process, this interaction between $\pi$ and $\mu$ implies that for each proposition, it is necessary to compute $\mu$ before $\pi$ . However, since a solution instance is defined only after its $\mu$ -value is known, this is not a problem. Also, even though the evaluation of solutions requires both $\pi$ and $\mu$ , it is not necessary that these be computed in-step (i.e., computing both measures for each node in the proof tree before proceeding to the next node). An interesting alternative is to first generate a set of feasible solutions on the basis of $\mu$ -values only, and then to compute the $\pi$ -values for this set of solutions to obtain one or more acceptable solutions, if they exist. The relative efficiency of this strategy as compared to the in-step strategy is determined by the nature of the knowledge base used (if a large proportion of the data and rules used are uncertain, the in-step strategy is likely to be better), and choice of strategy could be used by a system designer to fine-tune an actual system.

## 5. An Example

We next present a small example problem solved by a prototype system which we have developed. The example shows how imprecise axioms and data in logic based knowledge base can be combined to construct solutions to unstructured problems, and also how both fuzziness and uncertainty can interact in the problem solving process.

The example problem posed to the system can be paraphrased as 'Should the collection of the balance on transaction 9 be pursued?'. It is stated as a theorem, which the system solves by constructing a proof. Such a proof can be represented graphically by a proof tree, shown for part of the proof in fig. 1. In this tree, each non-leaf node represents the implicand of an axiom, whose pre-misses are the children nodes. For simplicity, we have denoted each node by only the name of the relevant predicate, along with the parameters $(z_{\mu}, z_{\pi}, \mu, \pi)$ , and $(k, \gamma)$ for the axiom used to resolve the predicate. The arcs have weights representing the weight of each child node as a premise for the parent node in the particular axiom used. Of the node parameters, only $z_{\mu}, z_{\pi}$ for the root node are provided by the user. All the other $(z_{\mu}, z_{\pi}, \mu, \pi)$ values are generated as the proof is constructed, by the system.

Several features of the imprecise reasoning methodology can be observed in this example. First, the values generated for the z-bounds of different premises are influenced by their relative weights. For instance, the bounds for CORRESPOND, with w = 5, are (0.49, 0.59), while those for ACTIVE, with w = 1, are (0.1, 0.18) (we assume a default lower bound of 0.1 for the measures). Thus, the system is able to tolerate lesser precision in ACTIVE than in CORRESPOND, due to their difference in weights.

The second feature that can be observed is the effect of imprecise instances of evaluated nodes upon the z-bounds of the remaining siblings of these nodes. This is illustrated in the bounds of RECORD, which are (0.27, 0.48). If the preceding siblings DUE and CORRESPOND had precise solutions, the z-bounds for RECORD would be (0.13, 0.42). This, in turn, illustrates another useful feature. If an important node is evaluated with an acceptable, but low set of imprecision measures, this can lead to the bounds for its lesser important siblings to be very high. In fact, these bounds may become $\geq 1$ , in which case the current search is fathomed. For instance, if CORRESPOND were evaluated with measures (0.5, 0.6), the nodes RECORD and ACTIVE would be immediately fathomed. On the other hand, if the important nodes are evaluated fairly precisely, the lesser important nodes become even less significant, as described earlier.

![](/api/attachments/4BZSDAHN/fulltext/images/2254baf58fedea040e2777129b02ff440cb8726d32e2ec63eaf54ff9edd2501e.jpg)  
Fig. 1. Partial Proof Tree for Query (The second row of parameters at each non-leaf node represent $z_{\mu}, z_{\pi}, \mu, \pi$ respectively).

The example also demonstrates the interaction of $\mu$ and $\pi$ during proof generation, which is an important feature of our methodology. This interaction occurs at several points in the proof. For instance, RECORD is inferred from two premises, namely MAXAGE and AVERAGE which are both certain, but fuzzy. As a result of the fuzziness in these premises, the implicand RECORD is also fuzzy. Now, this fuzziness also causes the $\pi$ -value for the implicand to be lowered, to 0.85, rather than 0.9, which would be the case if $\mu_{RECORD}$ were 1, rather than 0.63. A similar effect is found in inferring CORRESPOND from its premises CONTACT and CREDIT-RATE. The certainty of the final conclusion, PURSUE, is also modified by the fuzziness in all the knowledge and data used. This illustrates a strength of the imprecise reasoning methodology used here; that is, we are able to use axioms, even when their premises are satisfied only approximately; at the same time, this fuzziness in the premises is taken into account in the subsequent reasoning for the rest of the proof.

Another observation that can be made from the example, is that the fuzziness of the axiom used to derive PURSUE, reflected in the parameter k (= 3 in the axiom), leads to the certainty level $\pi_{PURSUE} = 0.75$ , rather than 0.7, which would result if a probabilistic function such as (3) were used. Here again, the methodology allows the fuzziness in the knowledge used to be reflected in the results obtained. In achieving this, the weights of the different premises are also significant. For instance, assume that the generated solution for ACTIVE had $\pi = 0.5$ . The resulting final solution for PURSUE by our imprecise reasoning method, would yield $\pi_{PURSUE} = 0.68$ , instead of 0.38, which would be the value if (3) were used. This is due to the low weight of ACTIVE in the relationship, which allows relatively uncertain instances of this premise to be useful as well.

Finally, the example also illustrates the utility of measuring and propagating fuzziness and uncertainty separately. For instance, examination of the solution shows that it is both fuzzy and uncertain, with a $\mu$ -value slightly lower than the $\pi$ -value. The initial conclusion that can be suggested by a low $\mu$ -value and a high $\pi$ -value is that the solution instance found (i.e., the tuple itself, as well as its proof), does not match the problem specification very well; and this can be concluded with a relatively high level of certainty. In the example, the two measures are relatively close. However, examination of the proof provides some interesting information. For instance, the fuzziness of the final solution is caused by premises that are all quite fuzzy (indicating that regardless of the form of the axiom, if the conclusion depends upon these premises, the generated solution is not a very good instance), while the premises are not uncertain, so the uncertainty of the solution arises mainly from the implications used. The two separate measures of imprecision thus enable the decision maker to separate and identify the causes of imprecision in the solution, and responded appropriately to them. In a system which only supports precise reasoning, such evaluation of solutions and proofs is difficult. Even in a system supporting only uncertain reasoning, evaluation of the quality of a particular solution, or the relative qualities of alternative solutions, is limited to comparison of certainty measures; also, since such a system cannot generate fuzzy solutions, evaluation of solutions based on their proximity to desired goals is not possible.

## 6. Conclusion

In this paper, we have developed new methods for the representation and manipulation of uncertainty in the knowledge used to solve unstructured problems. The major advantage of the approach used is that it allows for the effective use of both uncertain as well as fuzzy knowledge in inferential reasoning. At the same time, the treatment of uncertainty is consistent with probabilistic models where relevant. These methods, along with the methods developed for fuzzy reasoning developed in a related paper, provide a firm basis for the design of effective computer based systems to support imprecise reasoning for unstructured problem solving. Currently, the implementation of these methods is being investigated through the development of a prototype system.

## References

[1] Barnett, J.A., Computational Methods for a Mathematical Theory of Evidence, 7th International Joint Conference on Artificial Intelligence, B.C. (1981) 868–875.

[2] Barr, A. and E.A. Feigenbaum, The Handbook of Artificial Intelligence, vols 1–3, William Kaufmann, Los Altos, CA (1982).

[3] Barwise, J., Handbook of Mathematical Logic, North-Holland, Amsterdam (1977).

[4] Basu, A. and A. Dutta, Computer Based Support of Reasoning Activities for Decision Support in the Presence of Fuzzy Knowledge, Decision Support Systems 2, No. 3 (1986).

[5] Beckenbach, E.F. and R. Bellman, Inequalities, Springer-Verlag, New York (1965).

[6] Bellman, R.E. and L.A. Zadeh, Decision Making in a Fuzzy Environment, Management Science 17, No. 4 (1970) B141-B163.

[7] Bennett, J.S. et al., SACON: A Knowledge Based Consultant for Structural Analysis, Tech. Report CS-78-699, Computer Science Dept., Stanford University, CA (1978).

[8] Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, NY (1981).

[9] Carlson, E. and R.H. Sprague, Building Effective Decision Support Systems, Addison Wesley (1982).

[10] Chang, C.L. and R.C. Lee, Symbolic Logic and Mechanical Theorem Proving, Academic Press, NY (1973).

[11] Duda, R., P. Hart and N. Nilsson, Subjective Bayesian

Methods for Rule-Based Inference Systems, Proc. 1976 National Computer Conference 45, AFIPS (1976) 1075-1082.

[12] Dutta, A., Reasoning with Imprecise Knowledge in Expert Systems, Information Sciences 37, No. 1 (1985) 3–24.

[13] Feller, W., An Introduction to Probability Theory and its Applications, vol 1 and 2, John Wiley, NY (1971).

[14] Keen, P.G.W. and M. Scott-Morton, Decision Support Systems: An Organizational Perspective, Addison Wesley, NY (1979).

[15] Newell, A. and H.A. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ (1972).

[16] Nii, H.P., Heuristic Programming Project Brochure, Dept. of Computer Science, Stanford Univ., CA (1980).

[17] Nilsson, N.J., Principles of Artificial Intelligence, Tioga Press, Palo Alto, CA (1980).

[18] Prade, H., A Computational Approach to Approximate and Plausible Reasoning with Applications to Expert Systems, IEEE Transactions on Pattern Analysis and Machine Intelligence, vol PAMI-7:3 (1985) 260–283.

[19] Quinlan, J.R., INFERNO: A Cautious Approach to Uncertain Inference, Technical Note N-1898-RC, Rand Corp., Santa Monica, CA (1982).

[20] Reiter, J.E., AL/X: An Inference System for Probabilistic Reasoning, M.S. Thesis, Computer Science Dept., University of Illinois, Urbana-Champaign (1981).

[21] Salton, G. et al., Extended Boolean Information Retrieval, Communications of the ACM 26, No. 11 (1983).

[22] Shortliffe, E.H., Computer-Based Medical Consultation: MYCIN, American Elsevier, New York, NY (1976).

[23] Technology Resources, Inc., Comprehensive Current Library: Expert Systems (1982).

[24] van Emden, M.H., Programming with Resolution Logic, in: D. Michie, ed, Machine Intelligence 8, John Wiley, NY (1977) 266–299.

[25] Weiss, S.M., C.A. Kuikowski and A. Safir, A Model Based Method for Computer Aided Medical Decision Making, Artificial Intelligence 11 (1978) 145–172.

[26] Zadeh, L.A., Fuzzy Sets, Info. Control 8 (1965) 338–353.

[27] Zadeh, L.A., Probability Measures of Fuzzy Events, Journal of Mathematical Analysis and Applications 23 (1968) 421–427.

[28] Zadeh, L.A., A Theory of Approximate Reasoning, in: J.E. Hayes, D. Michie and L.I. Mikulich, eds., Machine Intelligence 9, John Wiley, New York (1979) 149–194.
