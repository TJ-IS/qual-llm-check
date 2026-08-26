---
otero_id: 16894
otero_key: "QNS7HG3H"
title: "Computer based support of reasoning in the presence of fuzziness"
authors: "Amit Basu; Amitava Dutta"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90031-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computer Based Support of Reasoning in the Presence of Fuzziness $^{1}$

Amit BASU \* and Amitava DUTTA \*\*

\* Information Systems Dept., College of Business and Management, University of Maryland, College Park, MD 20742, USA, and \*\* Management Science Dept., College of Business, University of Iowa, Iowa City, IA 52242, USA

Many important problems encountered in managerial decision making are unstructured, making them difficult to solve by preset algorithms. Much of the complexity of such problems is due to the reasoning that is needed to construct solution procedures for each problem instance. Thus, any Decision Support System (DSS) designed for such problems should support this reasoning activity, in addition to data access and computational activities. Yet, existing DSS generally do not provide much reasoning support. One of the difficulties faced in building automated systems to support such reasoning is that much of the knowledge typically available for unstructured problems is imprecise, where imprecision may be caused by either fuzziness, uncertainty, or both. In this paper, we address the problem of supporting problem solving with fuzzy knowledge. We develop a formal method for representing fuzzy knowledge, using a framework of mathematical logic. Using this method, fuzziness in all the major constructs needed to describe knowledge can be represented. Relationships can be constructed using fuzzy operators and terms, and components in relationships can be weighted by their relative significance. Also, computational procedures and data access procedures can be directly integrated into the reasoning process. Knowledge thus represented can be manipulated using suitable reasoning mechanisms. The fuzzy inference methods we present, enable the generation of acceptable solutions to problems even when some of the knowledge used is highly imprecise and/or incomplete. Other desirable features, such as explanation of solution procedures and user participation in problem solving, are also supported by our methodology. In addition, we develop bounding procedures, which convey the imprecision in the reasoning process, and also help to reduce the complexity of the search process by pruning poor solutions. Finally, we describe a prototype system which implements the methods developed in this paper. Using example problems processed by the system, we illustrate the versatility of these methods, and also highlight their major features and potential utility in practical applications.

$^{1}$ This work was done while the authors were at the Graduate School of Management, University of Rochester, Rochester, NY 14627.

## 1. Introduction

The poor structure of many important problems in managerial decision making usually makes it infeasible to solve such problems using preset algorithmic procedures. Much of the complexity of such unstructured problems arises from the reasoning that is needed to construct solution procedures for each problem instance. Therefore, effective support for this type of problem requires a system which can help in this reasoning task as well as in numerical computation. The design of such a system is difficult, however, due to the nature of the knowledge that is generally available for most unstructured problems. One of the pervasive characteristics of this knowledge is that it is usually imprecise, which makes it difficult to represent in a machine interpretable form. Thus, a systematic methodology for the representation and

![](/api/attachments/QNS7HG3H/fulltext/images/4b20cb00db24f8a3df1691daf5468df7542856f96b4953278428a8451088b6a8.jpg)

Amit Basu is assistant professor of information systems in the College of Business and Management, University of Maryland, College Park. His research interests are in the use of artificial intelligence for decision support systems, logic programming and deductive database systems. He received a B. Tech. in Electronics from the Indian Institute of Technology, New Delhi in 1979, an MBA in Finance from Southern Illinois University, Carbondale in 1981, and an MS and PhD in Computers and Information Systems from the University of Rochester (in 1983 and 1986, respectively). Dr. Basu is a member of the IEEE, the IEEE Computer Society and the ACM.

![](/api/attachments/QNS7HG3H/fulltext/images/8ae4d28e85e1f8a4d791e12f17b064d706d8948264164673aa738bc2c9e76d80.jpg)

Amitava Dutta is Associate Professor in the Information Systems Area at The University of Iowa's College of Business. His research interests lie in the use of AI techniques to aid decision making in complex environments, computer integrated manufacturing and database management. He holds a BS in Electronics from IIT Kharagpur, an MS in computer science from UC Santa Barbara and received hi PhD from Purdue University in 1981. Dr. Dutta is a member of the IEEE,

ACM, TIMS, ORSA and is on the editorial board of Expert Systems: Research and Applications.

manipulation of imprecise knowledge is crucial to the design of effective decision support systems for unstructured problems.

The importance of imprecise reasoning has been well established in the literature [3], [32], [12], [24]. We illustrate this further with a small example. Consider a system to support auditing decisions. In particular, consider the usually difficult task of auditing accounts receivable (we use this problem domain in our prototype implementation as well, in section 6). Much of the knowledge available for this purpose is in the form of imprecise ‘rules of thumb’, such as:

RULE: This debt is Collectible IF

(a) The customer has a High credit rating (b) The customer's record on Recent transactions is Good

(c) Recent contact with him about this debt has yielded a Positive response.

Knowledge in this form is not structured enough to construct algorithms for the problem. Furthermore, such rules are inherently imprecise, and transforming them into a precise form is difficult. There are two aspects to this imprecision, fuzziness and uncertainty. Fuzziness refers to the use of fuzzy or vague concepts and operators in knowledge representation. Some of the concepts used to represent object attributes, relationships and procedures in the knowledge base of reasoning system are characterized more appropriately by fuzzy sets (in which some or all the elements have partial membership [30], rather than by 'crisp' sets. In the example rule above, in addition to many of the terms being fuzzy (e.g., Recent, High), the relevant logical operators may also be fuzzy. On the other hand, uncertainty occurs when only partial knowledge is available about an entity or process, when future events are involved in the reasoning process, or when the underlying process is inherently stochastic (that is, some events and operations may be well defined, but their likelihood is less than certain). In the rule above, for instance, the existence of the three premises may not guarantee collectibility, even though it is highly likely (in addition, of course, the existence of the premises themselves may be uncertain).

Since fuzziness and uncertainty are distinct phenomena, and have different interpretations, distinct measures should be used to represent and evaluate them (as suggested in [12]). In this paper, we address the problem of fuzzy reasoning, and develop a methodology for representing and manipulating fuzzy knowledge. The methods that we present can be used to deal with fuzziness in all the major constructs needed in formal knowledge representation frameworks such as First Order Logic (FOL), and reasoning mechanisms such as theorem proving [8]. The problem of including uncertainty in knowledge and reasoning within the same framework will be addressed in a subsequent paper.

The organization of this paper is as follows: we describe the type of decision support that is useful for unstructured problems, in section 2; we then review some of the existing work on fuzzy reasoning, in section 3; the new methodology for representing fuzzy knowledge is presented in section 4; this is followed by methods for manipulating such knowledge inferentially, in section 5; section 6 describes a prototype system which implements the imprecise reasoning methods presented in this paper; and section 7 is the conclusion of the paper.

## 2. Characterization of Effective Support for Unstructured Problems

In addition to being imprecise, the knowledge available for unstructured problems is also usually fragmented and/or incomplete. Much of this knowledge is in the form of individual heuristics, rules and relationships that are concerned with specific aspects of the problem, but are not structured enough to combine into algorithms for the total problem. Given this type of knowledge to work with, effective support for unstructured problems can be provided through the following functional features in a computer based system:

(1) Data Management. Much of the information used in decision making is extracted from data that is explicitly available, usually from a file system or database. However, the specific data that is relevant to a problem cannot usually be determined beforehand. Thus, it is important, that as specific data requirements are identified in the course of solving the unstructured problem, the system provide ready and convenient access to such data.

(2) Model Management. While solving a problem, it may be necessary to use different computational procedures (e.g., statistics procedures, optimization procedures, etc.). As with data, since these computational needs are only identifiable during the problem solving process itself, the system should provide the facility to access these procedures, and use them with appropriate data, in a convenient manner.

(3) Reasoning Support. Although the two earlier features are important [7], they do not directly support the reasoning activities undertaken by a decision maker in solving an unstructured problem. Support for the reasoning task through automated mechanisms includes several features, including the following:

(a) Construction of solutions to problems by appropriately combining imprecise rules and data in a sound and consistent manner.

(b) Selection and use of different computational procedures where relevant, with appropriate data; also the synthesis of complex models from sets of simpler models, where necessary.

(c) Evaluation of solution strategies and solutions.

(d) Explanation of the reasoning process that has been used to generate each solution (how/why each solution is generated).

(e) Facility for the user to participate in the problem solving process, by providing missing rules/data interactively, as needed.

(f) Acquisition of knowledge from experience (new rules, better rules).

(g) A ‘smart’ user interface, so that users who are not sophisticated programmers can interact easily with the system.

All these features are important, and methods for implementing them are active areas of current research. However, the scope of this paper is limited to the development of effective methods for the representation and manipulation of fuzzy knowledge in automated reasoning.

Support for reasoning, as well as for data access and numerical computation is facilitated by the presence of the following three components in a support system:

(1) A knowledge base (KB) containing the system's knowledge of specific problem domains.

(2) Reasoning/control mechanisms embodying the problem-solving capability of the system.

(3) A user interface to interact with the decision maker.

The knowledge base of the system is a critical element in determining its versatility. This component contains a formal representation of all the knowledge available to the system about specific problem domain(s). It can be described by the collection of relevant objects in each domain, the relationships that exist between these objects, and the procedures that describe the dynamics of these objects and relationships. Each object is defined in the knowledge base by a collection of attributes, or descriptors, which provide a mapping between the object and sets of attribute values. Although the values of some attributes are just names or numbers, other attributes may also have more general values, which we call concepts. We define a concept using the notion of a membership set. The membership set of a concept P consists of a collection of values, each of which represents P, partially or completely. For instance, the concept 'Tall' may be defined by a membership set containing the interval 150–300 cm. In some cases, the elements of a concept's membership set may be concepts in themselves (elementary values such as names and numbers can be viewed as concepts with singleton membership sets).

If the valid objects, relationships and procedures needed to solve a problem are adequately represented in the knowledge base of a system, then appropriate reasoning mechanisms can be used to aid the decision maker by generating feasible solutions, identifying problems, and even educating (for instance, by identifying solutions and strategies the user may not be aware of).

## 3. Existing Approaches to Fuzzy Reasoning

The earliest systems developed for automated reasoning, such as MACSYMA [21], avoided imprecision altogether by restricting attention to problem domains such as mathematics and symbolic manipulation. However, once intelligent systems were designed for other domains, it became apparent that the models of the problems and domains available to the system designers were inherently imprecise, so that some means of dealing with imprecision were essential. As a result, most expert systems in use or under development today support some form of imprecise reasoning.

Most of the approaches used fall into one of two categories. The first category consists of those approaches that deal primarily with uncertainty, and essentially ignore fuzziness. In the second category are those approaches that focus on fuzziness. In this section, we will briefly discuss the relevance of fuzzy reasoning, and review some of the existing approaches to dealing with it.

## 3.1. The Case for Fuzziness

Most existing automated reasoning systems only address uncertainty. In other words, they assume that there is no fuzziness in the knowledge and reasoning involved in the problem-solving process. Rather, in situations where there is inherent fuzziness in the knowledge used, these approaches use artificial categorization of concepts and relationships to avoid this fuzziness. However, as shown in [12], this often leads to unrealistic results and interpretations. For instance, consider the following rule (from [25]):

IF Noise or cooling is Noticeable near the relief valve, THEN the relief valve has opened (PW 200, NW 0.5),

where PW and NW are weights used to modify the probability of the implicand based on whether the premise has occurred or not, respectively.

Here, in providing the input which forms the premise of the rule, a numerical imprecision factor p is also included. The interpretation of p in the AL/X framework in which it is set [26] is as an uncertainty measure, with the term ‘Noticeable’ assumed to be categorical. However, consider the application of this rule in practice. The premise might be manually provided by a technician, or automatically by a sensor and transducer. In addition a value for p is also entered or computed. In such cases, p is representative of fuzziness (i.e., the membership level of the perceived noise level in the membership set of the fuzzy term ‘Noticeable’), rather than uncertainty in the event. In fact, there may be no uncertainty involved at all; and if there were any, there should be some way of distinguishing between the two types of imprecision, to enable effective interpretation of the solutions generated.

## 3.2. Methods for Incorporating Fuzziness

The existing literature on fuzzy reasoning is mostly based on the use of many valued logics, and especially fuzzy logic [30]. Fuzzy logic is radically different from traditional binary logic. Its basis is that many concepts in natural language and problem domain knowledge are fuzzy, in that some of the elements comprising the concepts may not have a binary membership level in the concept's membership set, but instead are characterized by a 'possibility distribution' $\Pi_X$ over the unit interval [0,1]. Thus, a fuzzy proposition $p \equiv \{X \text{ is } A\}$ , where $X$ is a variable defined over the universe $U$ and $A$ is a fuzzy subset of $U$ , can be represented by the possibility distribution

$$
\Pi_ {X} = \operatorname{Poss} \left\{X = u \mid X \text {   is   } A \right\} = \mu_ {A} (u), \quad \forall u \in U,\tag{1}
$$

where $\mu_{A}(x)$ is the membership function of A [i.e., $\mu_{A}(x)$ specifies the membership level of x in the fuzzy set A]. Using a suitable language (such as PRUF [32]), fuzzy propositions can be stated, and converted into equivalent possibility assignment equations by operators such as projection and particularization. During the problem-solving process, the compositional rule of inference [32] is used to draw fuzzy conclusions from these equations, and the underlying possibility distributions.

In situations where both fuzziness and uncertainty are present, the uncertainty can be incorporated into the fuzzy framework in the following way. Given a probability space defined by $(R^{n}, \Sigma, P)$ , where $R^{n}$ is an Euclidean n-space, $\Sigma$ is the $\sigma$ -field of Borel sets in $R^{n}$ , and P is a probability measure over $R^{n}$ , the probability of a fuzzy event $A \in \Sigma$ is given by [31]

$$
P (A) = \int_ {R ^ {n}} \mu_ {A} (x) p (x) d x = E (\mu_ {A}),\tag{2}
$$

where $p(x)$ is the probability distribution function of A.

In general, however, fuzzy logic has several drawbacks that limit its direct application for imprecise reasoning. First, its use of linguistic truth variables with structured countable sets of truth values for each such variable, poses several conceptual and implementation problems. One such problem is failure of closure. Given two fuzzy propositions A, B, truth values may be defined for them, as well as for some derivable propositions, such as $A \vee B$ , $\neg B$ , for instance. However, this does not imply that truth values for other derivable propositions such as $A \wedge B$ , $\neg A$ , etc., also exist. Thus there is no way of interpreting the possibility distributions of these latter propositions, if they are indeed derived. In other words, the implicit assumption that the truth values are subjective and linguistic limits the range of results and interpretations that can be derived, even though the mechanical procedures used are quite general.

Another problem is that instead of keeping the two phenomena and their measures distinct, as they should be, many researchers using this approach try to relate the two, and treat fuzziness as a weaker form of uncertainty [24]. In fact, in some cases, the two are functionally related [9]:

$$
P _ {A} (s _ {i}) = \sum_ {j = 1} ^ {n} \frac {1}{j} \left(\mu_ {A} (s _ {j}) - \mu_ {A} (s _ {j + 1})\right),\tag{3}
$$

where A is an event which can have outcomes $s_{1}\ldots s_{n}$ , and the outcomes are ordered so that $\mu_{A}(s_{i})\geq\mu_{A}(s_{i+1}),\forall i.$ Also,

$$
\mu_ {A} (s _ {i}) = \sum_ {j = 1} ^ {n} \min \left(P _ {A} (s _ {j}), P (s _ {i})\right),\tag{4}
$$

which implies that $P_A(s_i) \leq \mu_A(s_i), \forall i$ .

Furthermore, the direct application of fuzzy logic does not enable the representation of some sorts of fuzziness, such as that arising from fuzzy operators in relationships. Nevertheless, the use of fuzzy set theory to deal with fuzziness, along with appropriate measures for uncertainty, does provide an effective basis for imprecise knowledge representation and reasoning. In fact, this approach has been used for several problem areas, such as medical diagnosis [16], structural damage assessment [18] and pattern recognition [19].

## 4. A Methodology for Representing Fuzzy Knowledge

It is apparent that there is a need for a general framework within which imprecise information and reasoning can be incorporated for decision support. We present here a method for the representation of both precise and imprecise knowledge within the same framework. This approach enables imprecision of different types and from different sources to be represented uniformly and effectively. The basis of the approach is the characterization of the knowledge base of a problem solving system in terms of the parameters described earlier, namely concepts, objects, relationships and procedures, which is a general conceptual model, and thus allows the implementation of the approach in any knowledge representation framework. However, we will restrict our attention to logic based systems, and present the approach in this framework. The choice of this framework is motivated by a number of factors, such as the ease of interfacing logic based systems with conventional databases, the versatility of logic as a programming basis, and the ease of generating explanations in logic based systems. Furthermore, as mentioned earlier, we will focus on the fuzziness aspect of imprecision in this paper, and present methods to effectively represent and manipulate fuzzy knowledge. The implications of the presence of uncertainty on these methods will be addressed in a later paper, where the incorporation of uncertainty will be achieved using methods that are an extension of the methods developed here for fuzzy reasoning.

## 4.1. A Logic Framework

Since a logic framework is the basis of the presentation of the new approach here, a brief overview of the logic notions used is in order. In a logic based knowledge base, all knowledge is represented in the form of well-formed formulae (wffs) in mathematical logic [8]. Although a variety of logics exists in the literature, the one most popular and useful for knowledge representation in the context of decision support systems is First Order Logic (FOL) ([15], [11]). In FOL, three types of parameters are used, namely terms, predicates (or atomic formulae) and wffs. Wffs are made up of one or more predicates connected by logical operators according to a well defined syntax. In a knowledge base (KB), most of the (domain) knowledge is in the form of ground literals, which are atomic formulae with all constant terms. In addition, there are a collection of wffs that define the relationships that exist among different literals (predicates). For purposes of compactness and convenience, a many-sorted logic [13] is assumed, in which all terms in literals belong to specific sorts or domains, and substitutions can only occur for terms in the appropriate sorts (see [11]).

In logic based systems, reasoning and problem solving is done via theorem proving. In this method, problems are solved by stating them in the form of one or more wffs, and then viewing these wffs as theorems to be proved inferentially [23]. The proof procedure usually involves Resolution Refutation [27], or tree search.

## 4.2. Representation of Fuzzy Knowledge Using Logic

In order to describe the representation method, we will consider the different constructs used to characterize a knowledge base, and show how fuzziness in each of these constructs can be represented for a logic based system.

## 4.2.1. Representation of Fuzzy Objects

Objects are defined in a knowledge base in terms of a number of relevant attributes and properties, with the latter represented by a collection of relationships. A common approach to the representation of attributes of objects is via a set of Object-Attribute-Value (OAV) 3-tuples [2]. In a logic framework, these 3-tuples are embodied in first-order predicates, with each attribute represented as a term in a suitable predicate. For example, in the predicate instance EMPLOYEE (P. Jones, 28193, Married, Blond), each of the terms is a value for a specific attribute (i.e., name, employee number, marital status, and hair color, respectively), with the specific values being chosen from a set of valid concepts.

A concept may be one of three things. It may be an elementary concept, which is either a name, or a numerical value; or it may be defined in terms of other, simpler concepts. For example, the values Apple, John, 467.35 are elementary concepts, while the value Tall is typically defined in terms of a set of elementary concepts (e.g., the range of heights 150–200 cm). Each concept, in effect, is characterized by a set, which we call its membership set [30], and which contains all the component concepts that make up this concept. It follows that in the case of elementary concepts, the membership sets are singleton sets.

When knowledge about an object is fuzzy, the lowest level at which this fuzziness can occur is at the attribute level. That is, one or more of the concepts used to specify attribute values for the object are fuzzy. The measure of fuzziness for concepts is derived from the theory of fuzzy sets [30]. The elements that define the membership set of an imprecise concept are assigned a graduated level of membership, defined not in terms of binary values (i.e., 0, 1 as in a 'crisp' set), but rather by a measure $\mu$ , called the membership function. Thus, $\mu_S(x)$ is the level of membership of the element $x$ in the concept $S$ , with $0 \leq \mu_S(x) \leq 1$ , $\forall x$ . In other words, $\mu_S$ defines the non-fuzziness, or crispness of the concept $S$ . In the extreme case of a precise concept, $\mu_S(x) \in \{0,1\}$ , $\forall x$ . It is important to note here that a concept may be precise, even if it is not an elementary concept; and furthermore, every elementary concept need not be precise. For example, consider the concept Positive defined on the set of real numbers - it is clearly non-elementary, yet it is not fuzzy; on the other hand, the concept Blond is elementary, yet is typically fuzzy (some blondes are more blond than others).

It is important to note several features of our methodology here. First, fuzzy set theory is only used to define the fuzzy measures for concepts. Unlike fuzzy logic which also uses membership sets for concepts), we do not extend the interpretation of truth values to linguistic truth variables, and truth is not treated as a context dependent linguistic variable. Instead, two different concepts with the same $\mu$ -value are interpreted as having the same level of fuzziness. Also, we assume a many-sorted logic [13], in which each concept is assigned to a specific sort (domain). For example, the attribute ‘Height’ has a sort which contains numbers (say in the range 20–300 cm), as well as concepts such as Short, Tall, etc., each of which has a membership set containing numbers drawn from the range of available atoms in the sort (i.e., 20–300). Use of a many-sorted structure allows the definition of different concepts that have the same name, but are relevant to different domains. For example, the fuzzy concept Tall has a different membership set when used in the context of persons, as opposed to buildings.

In addition, the sort structure can, and typically would be, organized as a hierarchy, so that complex concepts can be defined in terms of other non-elementary concepts. An example of such a hierarchical set of concepts is Growth, High, and

15 to describe a financial security; the first concept, Growth, is defined in terms of concepts such as High, Moderate, etc., where each of the latter set of concepts is itself defined over ranges of annual growth percentages, of which 15 is an example. Such a hierarchical structure of sorts can be viewed as a directed tree rooted at the most general concept. Then, any two concepts in this tree that are linked by a directed path can be matched with each other, although the match may be fuzzy (the interpretation of a fuzzy match will be examined in the next section).

Predicates in logic based knowledge bases serve two purposes. First, they are used to specify some or all attributes of single objects. In addition, however, they are also used to represent predicative relationships among different objects [e.g., FATHER (John, Peter)]. In some cases [e.g., HEIGHT (John, 170)], the $\mu$ -value of the predicate is derived from the $\mu$ -values of the terms, which are in many cases obtained from their sorts. However, in other cases [e.g., HAIR (Mary, Blond), FATHER (John, Peter)], a $\mu$ -value may directly have to be assigned to the predicate instance (tuple) itself. This usually occurs when the best known value for a specific attribute is a fuzzy concept, such as 'Blond' in the first example above.

It is interesting to note that not all predicates have to be explicitly assigned $\mu$ -values. This is because of two reasons. First, it is fairly easy to see that only ground literals (i.e., predicates with all constant terms) can be assigned levels of precision, since variables do not have any intrinsic truth value. Also, in a logic based knowledge base, all domain knowledge [23] is ultimately expressible in terms of ground literals that are explicitly stored in the knowledge base (e.g., explicit relations in relational data bases [11]). Thus, as long as these explicit ground literals (egls) have $\mu$ -values assigned to them, the imprecision in all predicates can be derived from these values during the problem solving process, using the logical relationships that exist in the knowledge base, and the rules for the propagation of fuzziness described later in this chapter. In fact, even some of the egls may not require explicit $\mu$ assignments, since these can be computed during proofs from the $\mu$ -values of constituent terms (which are all constants, in the case of ground literals). The trade-off between explicit storage of $\mu$ -values and generation of these values during proofs essentially corresponds to a computation-time/storage-space trade-off which is a function of specific problem domain, knowledge base size, and available resources.

## 4.2.2. Fuzzy Relationships

The derivation of $\mu$ -values for those literals that are not egls in the KB is achieved through the use of logical relationships defined in the KB (virtual relationships, in [11]). In general, these relationships may not be precise themselves. Fuzziness can occur in two ways in such a relationship. The first, which we have already encountered, is the presence of fuzzy predicates. However, a relationship between different predicates connected by logical operators such as conjunction, disjunction, negation and implication [8], may also have one or more of these operators fuzzy. It is therefore necessary to have systematic measures for these operators. Then, using these measures, an effective method for the interpretation of fuzzy relationships is needed; these issues are discussed below.

The underlying assumption made in our approach to fuzzy reasoning is that the $\mu$ -level of any statement can be interpreted as a measure of its 'distance' from the corresponding precise statement. In a logic based system, a statement is represented as a well-formed formula (wff), such as $W_{1} = W(P_{1}\ldots P_{m}, l_{1}\ldots l_{n}, t_{1}\ldots t_{q})$ , using predicates $P_{1}\ldots P_{m}$ , operators $l_{1}\ldots l_{n}$ , and terms $t_{1}\ldots t_{q}$ . Then, $\mu_{W_2}$ , the $\mu$ -value of an instance $W_{2} = W(\bar{t}_{1}\ldots \bar{t}_{q})$ of this wff, is interpreted as a measure of its proximity to $W_{1}$ . We have already considered the case where $W_{1}$ is a predicate ( $\mu$ is measured on a linear unit scale); we next consider the more complex case where $m, n, q \geq 1$ , for relationships.

In showing how imprecision is defined for relationships, we will first consider binary relationships (X op. Y), and later show how more complex relationships can be accommodated. We start by examining the conjunction and disjunction operators. Consider the binary expressions $w_{X}X\Lambda^{k}w_{Y}Y$ , and $w_{X}XV^{k}w_{Y}Y$ . We define the fuzzy and ( $\Lambda$ ) and or (V) operators used in such expressions as follows:

$$
\begin{array}{l} \mu_ {w _ {x} X \wedge^ {k} w _ {y} Y} (u, v) \\ = 1 - \left[ \frac {w _ {x} ^ {k} (1 - \mu_ {X} (u)) ^ {k} + w _ {y} ^ {k} (1 - \mu_ {Y} (v)) ^ {k}}{w _ {x} ^ {k} + w _ {y} ^ {k}} \right] ^ {\frac {1}{k}}, \end{array}\tag{5}
$$

$$
\mu_ {w _ {x} X \vee^ {k} w _ {y} Y} (u, v) = \left[ \frac {w _ {x} ^ {k} \mu_ {X} (u) ^ {k} + w _ {y} ^ {k} \mu_ {Y} (v) ^ {k}}{w _ {x} ^ {k} + w _ {y} ^ {k}} \right] ^ {\frac {1}{k}},\tag{6}
$$

where $w_{x}$ and $w_{y}$ are the relative weights of the concepts X and Y in the relationship, $\mu_{X}(u)$ and $\mu_{Y}(v)$ are the values of the membership functions of X and Y for the elements u and v respectively, and the proximity of the logical operator to the corresponding precise (boolean) operator is defined by k, with $(1 \leq k \leq \infty)$ .

Examination of the form of (5) and (6) shows that the kth order relationships essentially represent weighted kth order norms (such norm-based functions have been used very effectively in partial-match data retrieval [28]). This can be illustrated graphically for some values of k, and is intuitively appealing. If $\mu_{X}(u)$ and $\mu_{Y}(v)$ are plotted as orthogonal coordinates on a planar graph, then the $\mu$ -value computation via (5) and (6) is denoted by a distance measure in the unit square. For instance, when k=2, the relationships become weighted Euclidean norms, so that the following interpretations can be made:

$$
\begin{array}{r l} & \mu_ {w _ {x} X \wedge k _ {w _ {v} Y}} (u, v) \\ & \quad = 1 - \big (\text { weighted   dist.   of } (\mu_ {X} (u), \\ & \qquad \mu_ {Y} (v) \big) \text { from } (1, 1) \big), \\ & \mu_ {w _ {x} X \vee^ {2} w _ {v} Y} (u, v) = \big (\text { weighted   dist.   of } (\mu_ {X} (u), \\ & \qquad \mu_ {Y} (v) \big) \text { from } (0, 0) \big). \end{array}\tag{7}
$$

(8)

In other words, since the most desirable state in a conjunction is $(1, 1)$ , we penalise any movement away from it; and since the most undesirable state in a disjunction is $(0, 0)$ , we reward any movement away from it.

There are two other characteristics of the operators as defined here, that make the approach very versatile. First, by allowing X and Y in the definitions above to be weighted differently, and with arbitrary positive weights (since the weights are normalized by the operators), we enable different degrees of importance to be accorded to different components in a relationship. With boolean logical operators, these weights are inconsequential. However, when the component literals and/or operators themselves are fuzzy, the weights $w_{i}$ can indeed be used meaningfully. The usefulness of the weights arises from the fact that they enable the formulation of fuzzy relationships in which several factors (represented by suitable literals) are relevant, but are not all equally important. For example, the quality of a financial investment such as a stock might be determined by both the level of sales growth of the firm, as well as its return on assets (ROA), but the two factors may have different levels of significance (e.g., the ROA may be predominant). Such a relationship would be extremely difficult to represent in a boolean system, but can be represented effectively using (5).

The parameter k is used to characterize the fuzziness in the logical $\Lambda$ and $\vee$ operators. The effect of changing the k-value in a relationship is to alter the impact of the different component literals upon the relationship. For instance, in a fuzzy conjunction such as (5), as the k-value is increased, the weights $w_{i}$ of the different components become increasingly significant. For very large values of k, the $\mu$ -value of the fuzzy conjunction is predominantly determined by the component(s) with the highest weights (more specifically, the component(s) $A_{i}$ such that $w_{i}(1-\mu_{i})=\max_{j}w_{j}(1-\mu_{j})$ , as shown below).

This property provides the basic criterion for selecting the k-value in a specific relationship. If the manager/expert formulating the relationship is fairly confident about the relative weights $w_{1} \ldots w_{n}$ applicable to it, a high k-value can be used, denoting relatively precise operators. On the other hand, if knowledge about the relationship is limited, and the weights are only approximately known, a low k-value ( $\simeq 1$ ) is appropriate. In such a case, small variations in the weights $w_{i}$ have a lesser impact on the resulting $\mu$ -values for the relationship, and successful results may be possible even when the instances of some of the more heavily weighted components have low $\mu$ -values. This feature enables the use of relationships even when they cannot be formulated very precisely, and makes the k-value a useful parameter for knowledge representation, especially in the development stage of an IDSS. It is useful to note here that the use of low k-values in ill-defined relationships is not the same as equating the weights $w_{i}$ , since the latter does not provide information about the perceived weights, which is useful for deriving a more precise model of the relationship (in the knowledge refinement process).

In the norm function [e.g., (5)], the valid range of k-values is $(1, \infty)$ , which could make the task of selecting a particular k-value quite difficult. However, the $\mu$ -values obtained from this function vary significantly with k only for low values of k, in the range $(1, 10)$ . Therefore, it is adequate to choose k-values from this reduced range, and even from a discrete set of values in this range (e.g., 1359∞, with ∞ as the special extreme case of a precise conjunction); this approach has several advantages, which will be discussed in the next section. Also, the extreme values of k yield rather interesting and important special cases. Thus, k = 1 implies an extremely weak logical relationship, while $k = \infty$ implies that the operator is precise. To see this, consider first the case when k = 1 (from now on, we will omit the arguments of $\mu$ -functions except where there is some ambiguity. Thus, $\mu_{X}$ is used to denote $\mu_{X}(u)$ for some appropriate u).

Proposition 1. The and and or operators have the same interpretation when k = 1.

Proof.

$$
\begin{array}{r l} \mu_ {w _ {x} X \wedge^ {1} w _ {y} Y} & = 1 - \left[ \frac {w _ {x} (1 - \mu_ {X}) + w _ {y} (1 - \mu_ {Y})}{w _ {x} + w _ {y}} \right], \\ & = \frac {w _ {x} \mu_ {X} + w _ {y} \mu_ {Y}}{w _ {x} + w _ {y}}, \\ & = \mu_ {w _ {x} X \vee 1 w _ {y} Y}. \quad Q. E. D. \end{array}
$$

Proposition 2. The and and or operators have the same interpretation as in two-valued logic and fuzzy logic when $k = \infty$ .

$$
\begin{array}{l} \text {Proof.} \\ \mu_ {w _ {x} X \wedge^ {\infty} w _ {y} Y} \\ = 1 - \left[ \frac {\max \left[ w _ {x} (1 - \mu_ {X}) , w _ {y} (1 - \mu_ {Y}) \right]}{\max \left[ w _ {x} , w _ {y} \right]} \right], \\ = \min [ \mu_ {X}, \mu_ {Y} ], \end{array}
$$

when $w_{x} = w_{y}$ . And similarly,

$$
\begin{array}{r l} \mu_ {w _ {x} X \vee^ {\infty} w _ {y} Y} & = \frac {\max [ w _ {x} \mu_ {X} , w _ {y} \mu_ {Y} ]}{\max [ w _ {x} , w _ {y} ]}, \\ & = \max [ \mu_ {X}, \mu_ {Y} ], \end{array}
$$

when $w_{x} = w_{y}$ . Q.E.D.

We can see, from Proposition 2, that boolean logic and fuzzy logic interpretations of these logical operators are just special cases of the general operators that we have defined. Thus, in a knowledge base containing both precise and fuzzy knowledge, we can distinguish between the different types by appropriate use of the parameter k.

In order to represent logical relationships, it is also necessary to characterize the implication operator. If a relationship involves a strict implication, such as $A \to B$ , then $A \subseteq B$ and furthermore, $\mu_A(x) \leq \mu_B(x)$ , $\forall x$ [30]. If the relationship between $A$ and $B$ is not well known, then the approximation $\mu_B(x) = \mu_A(x)$ is reasonable for most applications (since it is a lower bound, and hence a basis for conservative reasoning). On the other hand, in some cases, the implication in a 'rule' may not be strict. This happens when the relationship between the premise and conclusion varies in 'strength' over the range of possible instances. In many cases, this variation can be represented by a suitable conjunction in the premise. However, in other cases, such as when the premise is a single proposition, it may be necessary to modify the implication operator itself. Consider for example the axiom 'The customer is Active IF he/she has made at least one Recent transaction'. Here, the term Active in the conclusion, and the term Recent in the premise, are both fuzzy. If a strict implication were to be used, then we would have $\mu_{Active} \geq \mu_{Recent}$ , and in practice, would have to assume equality of the $\mu$ -values. However, this may be quite inappropriate. Thus, the use of a fuzzy implication operator enables the representation of knowledge such as the above axiom without placing such strong restrictions on the resulting $\mu$ -values.

A fuzzy implication $A \to B$ is one in which $A \subsetneq B$ necessarily. To compute $\mu_B$ , a suitable characterization of the relationship between $A$ and $B$ is required. However, this is likely to be difficult to obtain, in practice (for instance, $A$ and $B$ may have different metrics, dimensions, etc.). A reasonable simplification is to characterize the implication in terms of the relevant $\mu$ -values, rather than $A$ and $B$ themselves. This is achieved by using a function $\Phi(x): \mu_A \to \mu_B$ (i.e., $\Phi(x): [0,1] \to [0,1]$ ). Then, given $\mu_A$ , the value of $\mu_B$ is computed as $\Phi(\mu_A)$ .

Theoretically, there are no further constraints on the form of $\Phi(x)$ , so that its use raises the spectre of having to store a multitude of different functions in the knowledge base. However, work on the use of fuzzy membership functions [32] has shown that most 'rules' in deductive problem solving can be adequately represented using a few specific functional forms. These include the S-form and the K-form (see figs. 1 and 2). The major difference between these two forms is that in the S-form, the transition in $\mu$ -values is smoother, and it is possible to define the lower end of the range where $\mu$ is significant. For instance, an implication which is nearly categorical can be represented by an S-form function with $(c - a) \ll 1$ . On the other hand, the K-form is simpler. In constructing a knowledge base, an expert (or a user) can characterize most fuzzy implications using suitable functions $\Phi(x)$ from these forms, thus significantly reducing the complexity of both storage and computation.

The use of $\Phi(x)$ to characterize implications is a versatile tool for imprecise reasoning. For one thing, it enables variation in the degree of implication (i.e., it allows for the interpretation of an implication as a sufficient, but not strictly necessary condition). And furthermore, it allows for the inference of $B$ with $\mu_B(x) \geq \mu_A(x)$ for some instances of $x$ , in appropriate situations. For example, in the axiom 'IF the stock has a High $\beta$ THEN it is Volatile', let $\mu_{High}$ for $\beta$ be defined so that $\beta > 2$ for $\mu_{High}(\beta)$ to be 1. In this case, it is likely that $\mu_{Volatile} > \mu_{High}$ for some values of $\beta$ . The use of a suitable $\Phi(x)$ (an S-form function with $c < 1$ or a K-form function with $k > 1$ ) en-

![](/api/attachments/QNS7HG3H/fulltext/images/0ccbb8be36f59ab7c26d88e608b6546738065463d90791443fe3e98db07a78cd.jpg)  
Fig. 1. The S-Form fuzzy membership function:

$$
\begin{array}{r l} S (x; a, b, c) & = 0 \text {   for   } x \leq a, \\ & = 2. \left(\frac {x - a}{c - a}\right) ^ {2} \text {   for   } a \leq x \leq b, \\ & = 1 - 2. \left(\frac {x - c}{c - a}\right) ^ {2} \text {   for   } b \leq x \leq c, \\ & = 1 \text {   for   } x \geq c. \end{array}
$$

![](/api/attachments/QNS7HG3H/fulltext/images/db3c33f33f61257c8da0f535d7ba3420c71a27e70903b6e4c2cc301c094ceb86.jpg)  
Fig. 2. The K-form fuzzy membership function: $K(x; l) = \min[1, l.x]$ .

ables this relationship to be effectively represented.

## 4.2.3. Fuzziness in Computational Procedures

A method for representing imprecision in procedures is also necessary. The major source of imprecision in procedures is uncertainty. However, fuzziness can also occur, either in the procedure itself (e.g., a fuzzy mathematical program [3]), or if the inputs/outputs of the procedure involve fuzzy terms. As with the other constructs, fuzziness in a procedure can be represented by a $\mu$ -value, which is computed either as part of the procedure itself, or generated when the results of the procedure are interfaced with the rest of the problem under examination. In a logic-based system, procedures can be incorporated as special predicates called model predicates, as shown in [11]. Unlike state descriptors, however, $\mu$ -values for procedures do not actually have to be stored in the knowledge base; instead, they are generated as needed upon execution. The resolution of model predicates is achieved differently than for ordinary predicates, since unification of the former requires model execution in general. However, it has been shown that resolution proofs including model predicates can be obtained using a two-phase procedure. This allows for compactness of representation, as well as compatibility with imprecision measures for the other components in the knowledge base.

Based on the logical interpretations of fuzzy objects, relationships and procedures described above, it is feasible to design logic based decision support systems that use inference to derive proofs and answers to a broad class of user queries. Specific rules for the evaluation and propagation of fuzziness during inferential procedures are presented in the next section.

## 5. Reference with Imprecise Knowledge

Given a knowledge base containing fuzzy knowledge, it is necessary to also have appropriate reasoning and control mechanisms to manipulate this knowledge for solving problems. As mentioned earlier, the presence of imprecise information necessitates the use of reasoning and control mechanisms that can manipulate this imprecise knowledge effectively. In a logic based system, resolution based theorem proving [27] is probably the most popular reasoning mechanism (although non-resolution theorem proving has been used as well [5]). However, ordinary theorem proving is inadequate to reason with imprecise knowledge. In this section, we show how the representation approach for imprecise knowledge described earlier can be used with modified theorem proving techniques to solve problems inferentially. As before, we restrict our attention here to fuzzy knowledge. Although the techniques are applicable to any inferential method, we use modified resolution as the specific inference mechanism in this paper, due to its generally and intuitive simplicity. The modifications suggested to resolution here can facilitate the proof process by restricting and guilding the process of searching for feasible solutions.

## 5.1. Properties of the $\mu$ -functions

We assume that the wffs in the KB are such that they can be transformed into horn clauses (disjunctive normal form, with at most one positive literal [23]). In other words, all the wffs (axioms) in the KB are either conjunctions of positive literals or implications with single-literal consequents. The process of transformation of wffs into horn clauses is justified, in the case of fuzzy wffs, by properties 1 and 2.

Property 1. $\mu_{\neg A} = 1 - \mu_A$ . This property enables the use of theorem proving techniques based on refutation (such as resolution), that use negations of literals, rather than the literals themselves.

Property 2. $\mu_{\neg (A\wedge^k B)} = \mu_{(\neg AV^k \neg B)}$ . This essentially shows that the functions in (5) and (6) obey De

Morgan's laws [8]. The transformation of conjunctions of positive literals into disjunctions of negative literals (as in a horn clause) is central to resolution refutation. This property allows us to deal with expressions stated as conjunctions of literals in the remainder of this thesis, without loss of generality. Proof:

$$
\begin{array}{r l} \mu_ {\neg (A \wedge {} ^ {k} B)} & = 1 - \mu_ {A \wedge {} ^ {k} B}, \\ & = \left[ \frac {w _ {a} ^ {k} (1 - \mu_ {A}) ^ {k} + w _ {b} ^ {k} (1 - \mu_ {B}) ^ {k}}{w _ {a} ^ {k} + w _ {b} ^ {k}} \right] ^ {\frac {1}{k}}, \\ & = \left[ \frac {w _ {a} ^ {k} \mu_ {\neg A} ^ {k} + w _ {b} ^ {k} \mu_ {\neg B} ^ {k}}{w _ {a} ^ {k} + w _ {b} ^ {k}} \right] ^ {\frac {1}{k}}, \\ & = \mu_ {\neg A} \vee^ {k} \neg B. \end{array}
$$

The following properties also help solidify the foundation of fuzzy reasoning using our methodology:

Property 3. Tautologies

$$
\begin{array}{l} \mu_ {w _ {1} X \wedge^ {k} w _ {2} X} = \mu_ {X}, \quad \mu_ {w _ {1} X \vee^ {k} 2 _ {2} X} = \mu_ {X}, \\ \mu_ {\neg \neg X} = \mu_ {X}. \\ \text { Similarly, } \mu_ {\neg (\mathbf {A} \vee^ {k} \mathbf {B})} = \mu_ {(\neg \mathbf {A} \wedge^ {k} \neg \mathbf {B})}. \quad \text { Q.E.D. } \end{array}
$$

In the previous section, it was noted that predicates, or atomic formulae, form the basis of most of the knowledge in the KB. In resolution refutation, two literals (predicates) are resolved at a time (in the simplest case), until a null clause is derived. In order to resolve two literals (of which one or both are non-ground), the process of unification is necessary [8]. In the presence of fuzziness, however, the usual exact pattern-matching nature of unification cannot be used, since it may be necessary to resolve two literals even if the unifier used does not yield a perfect match. To achieve this and allow the computation of the fuzziness in any ground literals that may result, the following rule is used, and illustrated by an example.

Rule 1. The imprecision level of an atomic formula (predicate) is defined by the $\mu$ -values of its terms, using the following rule (which can be interpreted as the conjunction of the individual terms with $p = \infty$ and all weights $w_{i}$ equal):

$$
\mu_ {P R E D I C A T E (t e r m _ {1} \dots t e r m _ {n})} = \min _ {i} \left\{\mu_ {t e r m _ {i}} \right\}.\tag{9}
$$

Example. Consider an explicit tuple $C_1 = STUDENT(John, 170, Blond)$ , in the knowledge

base, with

John $\in$ Name with $\mu_{Name}(John) = 1$

$170 \in \text{Height with } \mu_{\text{Height}}(170) = 1$

Blond $\in$ Color with $\mu_{\text{Color}}(Blond) = 0.7$

so that $\mu_{STUDENT(Name,Height,Hair)}(John,170,$ Blond) $= \min \{1,1,0.7\} = 0.7$

Now consider a predicate $C_2$ in a proof, $C_2 = \neg STUDENT(x, Tall, Blond)$ , and let $\mu_{\text{Tall}}(170) = 0.6$ . Then, resolving $C_1$ and $C_2$ yields the $\mu$ -value $\mu_{C_1 \wedge C_2} = \min\{\mu_{Name}(John)\mu_{Tall}(170), \mu_{Color}(Blond)\} = \min\{1, 0.6, 0.7\} = 0.6$ .

Using this convention, unification and resolution of fuzzy predicates can be effected. In addition, however, the following rules are needed.

Rule 2. Conjunctions of literals when all conjunctions are of the same order p (Axioms in the knowledge base that are multiple conjunctions have all the operators of the same order, with the value of k indicating the level of precision in the conjunction).

$$
\begin{array}{l} \mu_ {w _ {1} X _ {1} \wedge^ {k} \dots \wedge^ {k} w _ {n} X _ {n}} \\ = 1 - \left[ \frac {w _ {1} ^ {k} (1 - \mu_ {X _ {1}}) ^ {k} + \dots w _ {n} ^ {k} (1 - \mu_ {X _ {n}}) ^ {k}}{w _ {1} ^ {k} + \dots w _ {n} ^ {k}} \right] ^ {\frac {1}{k}}. \end{array}\tag{10}
$$

Rule 2a. Conjunctions of different orders in the same wff.

Such wffs are not axioms, but may be formed during an inference procedure or proof. These wffs are evaluated in a hierarchical manner. To achieve this, literals that enter a wff together (from the same axiom) are nested within the wff, so that the goal wff in any stage consists of a hierarchy of wffs, each of which has operators of a single order. Evaluation of the whole wff is then done in a stepwise manner, evaluating all components of each wff before evaluating it. The following example illustrates the method.

Let $(w_{3}X_{3}\wedge{}^{k_{2}}w_{4}X_{4}\to X_{2})$ be an axiom, and consider the case when $X_{2}$ in the conjunction $w_{1}X_{1}\wedge{}^{k_{1}}w_{2}X_{2}$ is resolved using this axiom. Then, $\mu_{w_1X_1\wedge{}^{k_1}w_2(w_3X_3\wedge{}^{k_2}w_4X_4)}$

$$
= 1 - \left[ \frac {w _ {1} ^ {k _ {1}} \left(1 - \mu_ {X _ {1}}\right) ^ {k _ {1}} + w _ {2} ^ {k _ {1}} \left(1 - \mu_ {Y}\right) ^ {k _ {1}}}{w _ {1} ^ {k _ {1}} + w _ {2} ^ {k _ {1}}} \right] ^ {\frac {1}{k _ {1}}},\tag{11}
$$

where $\mu_{Y} = \mu_{w_3X_3\Lambda^{k_2}w_4X_4}$ .

Rule 3. Axioms with implications having a single consequent, i.e., of the form

$$
\left\{\text { conjunctive   exp. } \right\}\rightarrow^ {I m p} B.\tag{12}
$$

In a resolution based system, $\mu_{B}$ is usually unknown, and is derived from $\mu_{\{exp\}}$ . Thus,

$$
\mu_ {B} = \Phi (\mu_ {e x p}).\tag{13}
$$

Rule 4. Associativity of conjunctions and disjunctions (although these operators are not strictly associative, due primarily to the use of the weights $w_{i}$ with each premise, a weaker form of associativity can be maintained in conjunctions and disjunctions having a single k for all the operators).

$$
\begin{array}{l} \mu_ {w _ {1} X \wedge^ {k} w _ {2} (w _ {3} Y \wedge^ {k} w _ {4} Z)} \\ = \mu_ {w _ {1} X \wedge^ {k} \frac {w _ {2} w _ {3}}{(w _ {3} ^ {k} + w _ {4} ^ {k}) ^ {1 / k}}} Y \wedge^ {k} \frac {w _ {2} w _ {4}}{(w _ {3} ^ {k} + w _ {4} ^ {k}) ^ {1 / k}} Z. \end{array}\tag{14}
$$

This property is useful in those situations where nested conjunctions with the same k-level are encountered, which is a relatively specialized situation. Since the valid range for k is $1 \leq k \leq \infty$ , such situations will rarely arise, and the utility of Rule 4 under these general circumstances is likely to be quite low. However, the form of the norm function (5) used to evaluate fuzzy conjunctions is such that most of the significant changes in the $\mu$ -levels of a fuzzy conjunction occur for changes in k-levels when k is very low (i.e., $k \simeq 1$ ); on the other hand, for high k-levels ( $k \geq 10$ ), changing the k-level of a conjunction does not significantly affect its $\mu$ -value. This suggests the viability of an imprecise reasoning system with only a small set of permissible k-levels (e.g., $1359\infty$ ). Not only does this facilitate the search process by increasing the likelihood of encountering situations where Rule 4 can be applied, but it also makes the task of formulating the axioms in the knowledge base easier, since research on human cognitive processes shows that reducing the choice set to around 5–9 choices significantly improves a person's ability to make choices [22].

## 5.2. Theorem Proving With Fuzzy Knowledge

So far, we have developed a method for representing fuzzy knowledge, and examined the major properties of the representation method that facilitate problem solving using search based techniques, in an IDSS. We next show how a logic based problem solving system can use fuzzy knowledge to solve unstructured problems. In such a system, problems posed by the user are formulated as well-formed formulae (wffs). These are then viewed by the system as theorems in logic, that have to be proved. Another way to view such formulae is as goal statements, whose existence has to be established. We will consider only goal-directed problem solving here (also known as backward chaining [29]). This does not imply that the representation method we have developed does not support other strategies for problem solving, since the method is general, and could be used with a variety of other strategies. There are several reasons why we choose to present only goal-directed reasoning here. First, it is conceptually simple, since it essentially corresponds to top-down analysis, and hierarchical problem decomposition. Secondly, it is a strategy that is easy to implement. And furthermore, it facilitates the development of effective methods for evaluating problem solutions. This last point will become more evident in the following discussion.

Using the rules defined in the previous section, both precise and imprecise information can be used together to generate proofs for problems stated as wffs. As pointed out earlier, the propagation of imprecision can be achieved as the proof is being generated, and can actually be used to assist the heuristic search for a proof by fathoming unreasonable searches. Since this bounding process is effected in the same way as in conventional resolution-based theorem proving, with the exception that partial matches are also accepted, the method does not violate the soundness of resolution refutation [20].

In order to see how this is achieved, it is helpful to view the proof as an inverted tree, in which each node represents a literal in some wff instantiated in the proof. The children of each node are the literals forming the premises of the axiom used to derive the parent literal in the proof. Thus, the root node of the tree is the query wff itself, or a part of it. The following weights are assigned to each axiom in the knowledge base, to enable proof generation and propagation of imprecision (the weights are described as they relate to the proof tree):

(1) Node weights. Each node in the proof tree has an associated weight $w_{i}$ . This is the relative weight of the literal at the node, in the axiom which instantiated it as a subproblem. This weight is used to compute the $\mu$ -value of the literal which is at the parent node for this node. The only node for which this weight is obviously irrelevant is the root node of the tree; this special case, as well as cases where the premise of an axiom has only one literal, can be assigned any default weight, to make the methodology uniform. The weights $w_{i}$ can be stored in an actual system either in their original form (unnormalized), or in the normalized form $w_{i}^{*}$ , which is computed as

$$
w _ {i} ^ {*} = \frac {w _ {i}}{\sum_ {i} w _ {i} ^ {k ^ {1 / k}}}.\tag{15}
$$

Since all the elements of (15) are known once the relevant axiom is formulated and added to the knowledge base, this latter policy is useful, since it reduces the computation necessary during a proof itself. Of course, the computation of $w_{i}^{*}$ requires that entering axioms be suitably transformed by some appropriate procedure before they are actually stored in the knowledge base.

(2) Arc weights. Each arc connecting a literal to its parent node is assigned the weight $w_{ij}$ which is the weight of the child literal i in the wff used to derive the parent j.

These node and arc weights are used with the representation method developed earlier to propagate imprecision through the proof tree in resolution-based theorem proving for different types of queries (problems). Essentially, the imprecision measures ( $\mu$ -values) for the data and relationships stored in the knowledge base are used with these weights to compute $\mu$ -values for derived data and formulae in the reasoning process. A side benefit of the procedures presented here is that they not only enable reasoning with fuzzy knowledge, but also use the $\mu$ -values to guide the heuristic search process for solutions.

The two processes used to develop a proof are the search process, and the evaluation process. The search process consists of some systematic method for scanning the knowledge base, to find data and/or axioms that can be used to match with components of the current goal statement (as each goal item is matched with an axiom, it is replaced in the goal statement by a set of items that comprise the premises of the instantial axiom). This process remains essentially the same as in any precise reasoning system (i.e., it is not affected by the presence of imprecision). As we mentioned earlier, we base our discussion on goal-directed search (in particular, we will use depth-first search [23]), although alternative strategies are also available.

The other process used in a proof is the evaluation process. This is a crucial element in imprecise reasoning. One of the major advantages of an imprecise reasoning system is its ability to generate fuzzy (as well as uncertain) solutions, or solutions with $\mu < 1$ . However, from the point of view of the complexity of the search process, this very feature poses additional problems. To see this, consider the proof process in a precise theorem prover. At each stage of the proof, a solution is generated only if it is precise. If solutions are found for all the subproblems, then the overall problem (from now on, we will refer to the original problem stated by the user as the global problem, and the subproblems at different nodes in the proof tree as local problems) is, in effect, solved as well. That is, the search process is for precise matches, and the evaluation process is trivial. On the other hand, when partial matches are considered in an imprecise reasoning system, it becomes necessary to examine every solution that has $\mu > 0$ , unless some means of screening solutions is adopted. This can result in a vast array of highly imprecise, and hence useless solutions being generated before a useful one with high enough precision levels is identified. Note that the terms useful and useless themselves have different interpretations in precise and imprecise systems. In the former, every solution is equally precise, and hence equally useful. However, when imprecise solutions are involved, in an imprecise reasoner, different solutions generated are not all equivalent, and some criterion is needed to decide whether a particular solution should be accepted or not; thus, the evaluation process is no longer trivial.

As far as fuzziness is concerned, an obvious way to evaluate solutions is by using a lower bound $z_{i}$ ( $0 \leq z_{i} \leq 1$ ) for each subproblem (i.e., each node in the proof tree), so that candidate solutions can be evaluated based on this bound, and only those solutions with $\mu_{i} \geq z_{i}$ are accepted. The bound $z_{i}$ can be interpreted as a level of imprecision tolerance. Since the global problem wff is also part of the proof tree, it also needs a z-bound. It is usually best to allow the user to specify this value as part of the problem specification, since it gives him/her greater flexibility and control. Note here that we have been considering the global problem as being in the form of a single literal. This may seem restrictive, since some problems may not be directly expressible in this form. However, any problem that can be stated as a horn clause can be converted into a form with a single literal at the root. This can be accomplished by creating a dummy root node. For example, let the global problem be

$$
w _ {1} P _ {1} \wedge {} ^ {k} w _ {2} P _ {2} \dots \wedge {} ^ {k} w _ {n} P _ {n}.\tag{16}
$$

This can be converted into the following problem:

$$
Q (t _ {1}, t _ {2}, \dots t _ {m})
$$

by adding the following temporary axiom, using the dummy consequent literal $Q(t_{1}, t_{2}, \ldots, t_{m})$ , in which the terms $t_{1}, \ldots, t_{m}$ include all terms used in (17):

$$
w _ {1} P _ {1} \wedge {} ^ {k} w _ {2} P _ {2} \dots \wedge {} ^ {k} w _ {n} P _ {n} \rightarrow {} ^ {1} Q.\tag{17}
$$

So far, we have not considered how the value of $z_{i}$ at node i can be obtained. Several methods for this are possible, and these are examined next.

(a) Use a fixed value such as 0.5 for all $z_{i}$ . This method has been used commonly in earlier work on fuzzy reasoning [20]. Its advantage is that it is very simple, and imposes no computational overhead or storage overhead on the reasoning process. However, it restricts the statement and interpretation of imprecise knowledge. Different axioms that have different degrees of imprecision cannot be treated differently; and the user cannot impose his/her preferences for precision in solutions generated upon the system. Also, some of the advantages of using axioms with unequally weighted premisses are lost; this will become clearer when we examine some of the alternative methods.

(b) Explicit specification of $z_{i}$ for each premise in an axiom. In this approach whenever an axiom is formulated, a z-value is specified for each premise by the expert providing the axiom. For example, in an axiom such as

$$
w _ {1} A _ {1} \wedge {} ^ {k} w _ {2} A _ {2} \dots \wedge {} ^ {k} w _ {n} A _ {n} \rightarrow {} ^ {\Phi} B,
$$

the expert has to provide n different z-values, one for each $A_{i}$ . This method overcomes some of the rigidity of (a), and still avoids any computational overhead. However, it imposes a significant burden upon the person(s) formulating the axioms, especially since there is no clear cognitive basis for deriving the different z-values, such as in the specification of the weights $w_{i}$ . Also, this method still does not give the user control over the precision of local problem solutions, and may cause certain solutions to be rejected, even they would lead to acceptable global solutions. Furthermore, if the same literal, say $A_{i}$ , is used in a number of axioms (but with different terms), each instance has to be assigned an explicit z-value (a simplifying assumption is that all instances of $A_{i}$ should have the same z-level, but this is hard to justify).

(c) Assign a z-level to each axiom. In this method, the z-value of each axiom is associated with its consequent, rather than each premise. A solution instance for each consequent is then accepted only if its $\mu$ -value, computed using (5), is high enough. The basis for evaluating each premise depends upon the method used to obtain its local solution. If an axiom is used, then the z-level of the axiom applies; if a direct match with a ground literal is made, either a default value such as 0.5, or no bound, is used. The latter may be somewhat inefficient, but since this inefficiency is only at the lowest level of search (i.e., database search), it may be tolerable, except where very large relations are involved (i.e., relations with many tuples), for which a default z-value is recommended. The distinction between this method and (b) is that in this method, the number of z-values that have to be specified is essentially equal to the number of axioms in the knowledge base, which would typically be far smaller than the number of literals used in all the axioms. Further, the basis for selecting specific values for the z-levels of axioms is easier to establish. That is, the z-level can be interpreted as a measure of the quality of the rule; if $z_{i}$ is high, the axiom can be considered as a weak axiom, which can be used only if the inputs are very precise; on the other hand, if $z_{i}$ were low, the axiom would be applicable even with relatively imprecise inputs, which would indicate greater versatility.

The only problem with this approach is that, like all the previous ones, it fails to take characteristics of specific problem instances into account. Thus, it is possible that even though the user stating the global problem is willing to accept certain imprecise solutions, these solutions are pruned by the theorem prover; and conversely, even if the user states a problem with a very high z-bound, the theorem prover will not be able to take this information into account when addressing subproblems. It is clear that the control of search should be effected by an evaluation process that is problem-driven. The next method provides this feature.

(d) Problem-driven evaluation. The central idea in this method, as stated above, is the evaluation of fuzzy problems based on criteria specified by the system user, rather than by the system. In other words, the basis for accepting a local solution should be primarily its adequacy for generating feasible global solutions. Unfortunately, since the global solution is determined by all the local solutions, and not just any specific one, it is usually impossible to ensure that the above objective will be satisfied by any particular local solution, until the complete problem has been solved. Inspite of this, it is possible to evaluate local solutions in a goal-driven manner, utilising what information is currently available at any stage of the proof process, even if the information is not complete.

The adaptive evaluation process achieved by this method does have a cost, in terms of computational overhead. This is because it requires that the z-values be computed at each node, in addition to the $\mu$ -values that also have to be computed, and then compared with the z-value. In effect, therefore, this method substitutes search efficiency for fast computation at each node. Since the type of problems that such systems are used with are characterized by large state spaces, however, this trade-off is more than justified. That is, it is usually better to perform greater computation at each node (which consumes mainly cpu resources, and is thus fast), than resort to significantly greater search and backtracking (which is usually both cpu and IO-bound, and is thus more time-consuming). Furthermore, the computation of the z-values is quite straightforward, and in most cases, would not be a significant factor in efficiency considerations. From now on, we will use this method as the basis for evaluation of solutions.

The method for imprecision propagation is based primarily on Rule 2, which, in the proof tree implies that evaluation of $\mu$ -values is only done at leaf nodes of the tree. A node becomes a leaf node once all its children have been evaluated. In the case of universally quantified queries, the evaluation of a leaf node representing an explicit relation consists of finding all tuples of the relation that have $\mu_i \geq z_i$ . Once a leaf node $s$ is evaluated, these tuples, along with their $\mu$ -values, are passed up to the parent node of $s$ (i.e., the consequent of the wff of which $s$ is one of the premises). When all the siblings of $s$ are resolved and evaluated, the parent of $s$ becomes a leaf node in turn, and $s$ and its siblings are dropped from the set of lead nodes. The new leaf node is evaluated by computing all valid instances of the wff at this node (using the unifiers from its children nodes), and their $\mu$ -values. Thus, while the resolution process causes the proof tree to grow downwards, the imprecision evaluation and propagation process tries to move up the tree, till a successful evaluation of the root node is achieved. The proof procedure for existentially quantified queries is similar, except that at each leaf node, a single satisfactory instance, rather than all valid instances, is sought. A consequence of this is that a solution obtained for an existentially quantified query may not be the best one, although it will be a valid one, and will have an associated $\mu$ -value for evaluation (see the example in the next section). It is interesting to note that in a precise system, this method would yield the same results as ordinary resolution.

Since the development of a proof is backward, from the goal wff, which has a specified z-bound, this value can be used to set the z-values of all the premises of the axiom used to match with the goal. To illustrate how this can be done, we consider a literal $x_{i}$ in the current goal (i.e., the current collection of subproblems). Let $x_{i}$ be resolved using the following wff:

$$
w _ {1} x _ {1} \wedge {} ^ {k} w _ {2} x _ {2} \dots \wedge {} ^ {k} w _ {n} x _ {n} \rightarrow x _ {i}.\tag{18}
$$

Then, in the proof tree, $x_{1}, \ldots, x_{n}$ form the children nodes of $x_{i}$ with arc weights $w_{1}, \ldots, w_{n}$ respectively. Now consider $x_{1}$ . Even if $x_{2}, \ldots, x_{n}$ resolve with all precise terms, so that $\mu_{2} = \mu_{3}, \ldots, \mu_{n} = 1$ , the lowest value of $\mu_{1}$ which will still yield $\mu_{i} \geq x_{i}$ is given by $\mu_{I}^{*}$ , where

$$
\mu_ {1} ^ {*} = 1 - \frac {\left[ 1 - z _ {i} \right]}{w _ {1} ^ {*}}, \quad \text { with }\tag{19}
$$

$$
w _ {1} ^ {*} = \frac {w _ {1}}{\left[ w _ {1} ^ {k} + \dots + w _ {n} ^ {k} \right] ^ {1 / k}}.\tag{20}
$$

Proof. At the very least, we need

$$
\begin{array}{l} \mu_ {i} = z _ {i}, \\ \qquad = 1 - \left[ \frac {w _ {1} ^ {k} (1 - \mu_ {1}) ^ {k} + \dots w _ {n} ^ {k} (1 - \mu_ {n}) ^ {k}}{w _ {1} ^ {k} + \dots w _ {n} ^ {k}} \right] ^ {\frac {1}{k}}, \\ \qquad = 1 - \frac {w _ {1} (1 - \mu_ {1})}{\left[ w _ {1} ^ {k} + \dots w _ {n} ^ {k} \right] ^ {1 / k}}, \\ \qquad = 1 - w _ {1} ^ {*} (1 - \mu_ {1}). \end{array}
$$

and the result follows. Q.E.D.

Thus, the value of $\mu_1^*$ provides a valid lower bound for $\mu_1$ to be acceptable, and can be used as $z_1$ . Values of $z_i$ thus computed for each child node of a literal that has been matched with an axiom, als have the desirable property that they take the weights $w_i$ of the different premises of the axiom into account. Thus, if $w_i > w_j$ , then $z_i > z_j$ (the relative magnitudes of $z_i$ , $z_j$ depend upon the $k$ -value of the axiom, in addition to the $w_i$ 's. This is an important and useful property. Different chunks of knowledge used in imprecise reasoning may be imprecise to different degrees. However, in using imprecise information, it is desirable to be able to specify how imprecise any specific chunk may be without jeopardizing the quality of solutions obtained. In practice, the tolerance for imprecision is typically a function of the role played by the specific item. That is, if the item is very important, the decision maker would like to obtain it with a high degree of precision; on the other hand, he/she would be fairly tolerant of low levels of precision in relatively unimportant items. The $z$ -bound computation scheme described above directly supports this idea, and in the process, also helps reduce the complexity of the heuristic search process.

Although the z-bounds generated thus are useful, however, they are still quite conservative. This is due to the assumption made when computing the z-bound for a specific node i, that all its siblings are non-fuzzy (i.e., have $\mu=1$ ). This assumption is quite adequate for the z-bound of the first sibling $x_{1}$ of a set $x_{1}, x_{2}, \ldots, x_{n}$ (where $x_{1}, \ldots, x_{n}$ together form the premises of an axiom), since at that point, all the available information is taken into account. However, once one or more of the $x_{i}$ have been evaluated successfully, the z-bounds for the remaining siblings could take the additional information available about the computed $\mu$ -values into account. Yet, this is not done in the above method. As a result, the effect of the z-bounds becomes progressively weaker with each $x_{i}$ that is evaluated, especially if some of the $x_{i}$ have $\mu_{i}<1$ .

A more efficient bound generation method is thus possible, and is described next. In this procedure, the z-bound at each node is determined not just by the form of the axiom and the z-bound of the parent node, but also by the $\mu$ -values of all sibling nodes that have already been evaluated. Thus, once $x_{1}$ is evaluated, the value of $z_{2}$ is computed.

Furthermore, as each leaf node $l$ is evaluated, its tuples' $\mu$ -values can be used to update the $z$ -bounds of its siblings. For this purpose, the above bounding procedure is somewhat modified, in that now $\mu_k^*$ in (19) is computed as

$$
z _ {2} = 1 - \frac {1}{w _ {2} ^ {*}} \left[ (1 - z _ {0}) ^ {k} - \left(w _ {1} ^ {*}\right) ^ {k} (1 - \mu_ {1} ^ {*}) ^ {k} \right] ^ {\frac {1}{k}}\tag{21}
$$

with $w_{1}^{*}$ , $w_{2}^{*}$ defined as before [using (20)], and $z_{0}$ as the z-bound of the parent node of $x_{1}$ and $x_{2}$ . Proof. As in the earlier proof, the smallest $\mu_{2}$ allowed if $u_{j}=1$ , $\forall j>2$ , is such that

$$
\begin{array}{r l} & z _ {0} = 1 - \left[ \left(w _ {1} ^ {*}\right) ^ {k} (1 - \mu_ {1}) ^ {k} + \dots \right. \\ & \qquad \left. + \left(w _ {2} ^ {*}\right) ^ {k} (1 - \mu_ {2} ^ {*}) ^ {k} \right] ^ {\frac {1}{k}}, \\ & \qquad = 1 - \left[ \left(w _ {1} ^ {*}\right) ^ {k} (1 - \mu_ {1}) ^ {k} + \left(w _ {2} ^ {*}\right) ^ {k} (1 - \mu_ {2} ^ {*}) ^ {k} \right] ^ {\frac {1}{k}}, \end{array}
$$

so that

$$
\left(w _ {2} ^ {*}\right) ^ {k} \left(1 - \mu_ {2}\right) ^ {k} = \left(1 - z _ {0}\right) ^ {k} + \left(w _ {1} ^ {*}\right) ^ {k} \left(1 - \mu_ {1} ^ {*}\right) ^ {k}.
$$

and the result follows. Q.E.D.

In general, if there are n siblings $x_{1},\ldots,x_{n}$ , and if these are evaluated in order, the z-bound $z_{1}$ of the l-th sibling $x_{l}$ is given by

$$
z _ {l} = 1 - \frac {1}{w _ {l} ^ {*}} \left[ (1 - z _ {0}) ^ {k} - \sum_ {i = 1} ^ {l - 1} \left(w _ {i} ^ {*}\right) ^ {k} (1 - \mu_ {i}) ^ {k} \right] ^ {\frac {1}{k}}.\tag{22}
$$

This method of dynamically updating the zbounds obviously requires more computation than (19). However, it significantly improves the effectiveness of the bounding process. For instance, if $i < j$ , and $w_i \gg w_j$ , (19) would yield $z_i \gg z_j$ . Now, assume that $x_i$ is evaluated with a $\mu$ -value that is only marginally acceptable (i.e., $\mu_i = z_i$ ). Use of the bound $z_j$ from (19) in this situation would likely result in a local solution for $x_j$ that would be rejected once the parent node of $i$ and $j$ is evaluated. On the other hand, use of (22) would result in $z_j = 1$ , that is, a much tighter constraint on $\mu_j$ , even though it has a low weight $w_j$ . As a result, much more efficient pruning of the search process for a solution for $x_j$ would be achieved. The dynamic bound computation method imposes an even greater computational overhead at each node than the method of (19). However, in heuristic search based problem solving, this is usually more than justified, as was discussed earlier.

The proof is completed when the root node is evaluated. During the proof, if at any point a leaf node is evaluated with no valid tuples being found, then this node l and all its siblings are dropped from the search tree, and an alternative resolvent for the parent node of l is sought, using some other axiom in the knowledge base.

## 6. A Prototype System for Imprecise Reasoning

A prototype system has been developed to demonstrate the feasibility and major features of the approach to imprecise reasoning. In this section, we describe this prototype briefly, and illustrate its use through a set of example problems.

The system has been developed on a DEC VAX11/750 using Fransz LISP [14]. The imprecise theorem prover is largely built on top of a conventional theorem prover called HORNE [1]. For purposes of demonstration, we have used a knowledge base extracted from an experimental expert system for auditing accounts receivable [10].

The knowledge base contains three types of knowledge. First, there is a set of explicit relations, which are stored using standard LISP data structures. In addition, the knowledge base contains a collection of rules or 'axioms', which are stored in the form

$$
\begin{array}{c} \left(B t _ {1} \dots t _ {n}\right) <   \left(A _ {1} r _ {1, 1} \dots r _ {1, m}\right) \dots \left(A _ {q} r _ {q, 1} \dots r _ {q, \delta}\right) \\ \left(\texttt {\textsf {S E T V A L U E}} \dots\right) \end{array}
$$

to represent logical relationships of the form

$$
\begin{array}{l}w _ {1} A _ {1} (r _ {1, 1} \dots r _ {1, m}) \wedge^ {k} \dots \wedge^ {k} w w _ {q} A _ {q} (r _ {q, 1} \dots r _ {q, \delta})\\\rightarrow^ {\Phi} B\end{array}
$$

with the parameters $w_{i}$ , k and $\Phi(x)$ being represented through the special predicate SETVALUE. Also, the first term in each predicate, following the predicate name, is used to store (represent) the $\mu$ -value for the predictable.

The third component of the knowledge base is a collection of fuzzy sets stored either explicitly, or represented by fuzzy membership functions that are stored as suitable LISP functions.

The system functions primarily as an interpreter, so that the user can add or remove axioms and/or data, can examine the knowledge base, can pose and solve a variety of problems, and can examine the solutions produced and solution procedures generated, in interactive sessions. Since the system is currently experimental, its user interface is fairly crude; in an application environment the user should be able to perform the above functions far more easily than via the LISP syntax that is currently used.

## 6.1. Example Problems

We next illustrate some of the features of the prototype system (and the methods developed) that enable and facilitate imprecise reasoning and decision making, using sample outputs for a variety of problems stated as user queries. To enhance readability, comments lines in the sample interactive sessions shown in the exhibits are prefaced by ‘\*\*\*’, and user inputs are highlighted (in bold face).

The simplest type of problem is where only database access is required to obtain the required information (solution). An example of such a problem is Query 1. We have mentioned earlier in the paper that a major aspect of decision support is relieving the user of procedural details of a problem. In a logic based system such as the prototype, problems are stated as theorems to be proved, regardless of how their solutions are obtained; thus in Query 1, the user does not have to know that the predicate SALE represents an explicit relation in the knowledge base.

Another simple type of problem is the explicit use of a specific computational procedure, as in Query 2. Here a procedure SUM is invoked to accumulate the payments made by a customer. The predicate SETVALUE is used to specify the output parameter for the procedure.

```txt
**********************************************************************
*** Database accesses are handled as in relational calculus,
*** and the user is insulated from having to know whether the
*** predicate is explicitly stored, or inferred. In this
*** query, SALE is an explicit relation.

*** QUERY 1: Find details of transaction #3
(proveq (SALE ?m 3 ?d ?x ?a ?dd))
-> (q- 1)(SALE ?m 3 ?d ?x ?a . &)
(r- 1)(SALE 1 3 840220 Baker 3050.5 . &)
((SALE 1 3 840220 Baker 3050.5 840220))

**********************************************************************
*** Use of computational procedures is enabled by the special
*** predicate SETVALUE

*** Query 2: Find the sum of all payments by Acme
(proveq (SETVALUE ?m 'a (SUM 5 'PAID 5 '((4 Acme)) nil)))
-> (q- 1)(SETVALUE ?ml 'a (SUM 5 'PAID 5 '((4 Acme)) nil))
(q- 2)(PAID ?x7001 ?x7002 ?x7003 Acme ?x7004)
(r- 2)(PAID 1 2 840112 Acme 400.0)
(r- 2)(PAID 1 4 840317 Acme 500.0)
(r- 2)(PAID 1 4 840415 Acme 600.0)
(r- 1)(SETVALUE 1500.0 'a (SUM 5 'PAID 5 '((4 Acme)) nil))
((SETVALUE 1500.0 'a (SUM 5 'PAID 5 '((4 Acme)) nil)))

**********************************************************************
*** In all predicates, the first term after the predicate name
*** is the mu-value
**********************************************************************
Query 1.    Query 2.
```

At the next level of complexity are problems for which some inference is required. Examples of such problems are Query 3 and Query 4. In these queries, which involve a single rule (axiom), the following features are demonstrated:

(1) Fuzziness in a term. The term ‘Recent’ in the domain of transaction date is a fuzzy term, and thus unification with it may be fuzzy, resulting in $\mu$ -values less than 1.

(2) Trace mode. The system has a trace mode, which provides a form of explanation capability, of how each solution (for the overall problem as well as each subproblem) is generated (see Query 3a). This trace mode can be activated either selectively, for specific predicates or rules, or globally (as shown). In the trace, the first item on each line identifies the current step in the proof. Each subproblem is represented by a q-node (query node), while each solution is represented by an r-node (response node). The adjoining number indicates the level of the relevant node in the search tree, which is also indicated by suitable indentation.

\*\*\* QUERY 3: Is Toyco an Active Customer? \*\*\*
\*\*\* (i.e. made any recent purchases)

(proveq (ACTIVE ?m Toyco))

-> ((ACTIVE 0.5464852607709751 Toyco))

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*\*\* The trace mode prints out each search and evaluation step
\*\*\* q-nodes correspond to searches (queries)
\*\*\* r-nodes correspond to evaluations (responses)
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* QUERY 3a: QUERY 1 with trace

-> (q- 1)(ACTIVE ?m Toyco)
(q- 2)(SALE ?ml1 ?tll ?d21:Recent Toyco ?all . &)
(r- 2)(SALE 0 1 ?d21:Recent Toyco 6400.0 . &)
(r- 2)(SALE 0 5 ?d21:Recent Toyco 850.0 . &)
(r- 2)(SALE 0.1 6 ?d21:Recent Toyco 12000.0 . &)
(r- 2)(SALE 0.4428571428571429 10 ?d21:Recent Toyco 4325.5 . &)
(r- 2)(SALE 0.5142857142857143 11 ?d21:Recent Toyco 635.5 . &)
(r- 1)(ACTIVE 0.5464852607709751 Toyco)
((ACTIVE 0.5464852607709751 Toyco))

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*\*\* The system has a "Universally Quantified" query mode, as
\*\*\* shown in the following query

\*\*\* QUERY 4: Find all active customers \*\*\*
(proveq all (ACTIVE ?m ?x))

-> ((ACTIVE 0.5464852607709751 Toyco)
(ACTIVE 0.5464852607709751 Acme)
(ACTIVE 0.9954648526077097 Bull)
(ACTIVE 1 Acme))

Query 3. Query 4.

Thus “(r-2)” indicates a response at level 2 in the proof tree (the initial problem wff is at level 0). Traces can be generated as the proof proceeds, or after the proof is complete (without having to regenerate the proof itself). Using this trace facility enables better understanding of the system’s performance by the user, and is a very desirable feature in providing support for unstructured problems.

(3) Fuzziness in implication. The rule used in these queries has a fuzzy implication, characterized by an $\Phi(r)$ function of the S-form. Its effect is evident in Query 3a, where it modifies the $\mu$ -value of the SALE predicate to obtain the $\mu$ -value for ACTIVE.

(4) Generating alternative solutions. Query 3 is an example of an existentially quantified problem (find a single feasible solution), which is the default mode of the system. However, a decision maker is often interested in identifying all the feasible alternative solutions to a problem. The latter situation is addressed by stating problems as universally quantified queries, as in Query 4 (i.e., 'Find all acceptable solutions').

The next example, Query 5, involves the use of both inference and numerical computation. In this instance, a procedure MAX-MIN is used to compute the oldest outstanding debt for a specific customer, and a procedure SUM is used to obtain the total outstanding debt for a customer. This example also shows how several procedures can be automatically synthesized and executed in the problem solving process, even when the output of one procedure is an input to another. Furthermore, this example also illustrates the unification of procedure outputs with fuzzy terms; in this case, the data of the oldest debt is unified with the fuzzy term 'Notdelinquent'. This shows how the evaluation and propagation of imprecision can be achieved in the same way for both ordinary predicates and model predicates.

In some cases, there may be no feasible solutions to the problem posed. Such situations lead to unsuccessful proofs, which return the value “nil”.

```txt
******************************************************************************************
*** Computational procedures are used as predicates.
*** QUERY 5: How good is the record of customer Bull?
(proveq (RECORD ?m Bull Good))

-> (q- 1)(RECORD ?m Bull Good)
(q- 2)(MAXAGE ?mll Bull ?ul:NotDelinquent)
(q- 1)(DUE ?x7101 ?x7102 Bull ?x7104 ?x7105)
(q- 2)(SALE ?mll ?x7102 ?dsalel Bull ?all . &)
(r- 2)(SALE 1 8 840430 Bull 245.0 . &)
(r- 2)(SALE 1 9 840430 Bull 420.0 . &)
(r- 1)(DUE 1 9 Bull 420.0 840630)
(r- 2)(SALE 1 13 840525 Bull 836.75 . &)
(r- 1)(DUE 1 13 Bull 836.75 840725)
(r- 2)(MAXAGE 1 Bull ?ul:NotDelinquent)
(q- 1)(DUE ?x7201 ?x7202 Bull ?x7204 ?x7205)
(q- 2)(SALE ?mll ?x7202 ?dsalel Bull ?all . &)
(r- 2)(SALE 1 8 840430 Bull 245.0 . &)
(r- 2)(SALE 1 9 840430 Bull 420.0 . &)
(r- 1)(DUE 1 9 Bull 420.0 840630)
(r- 2)(SALE 1 13 840525 Bull 836.75 . &)
(r- 1)(DUE 1 13 Bull 836.75 840725)
(r- 1)(RECORD 0.985736111111111 Bull Good)
((RECORD 0.98573611111111 Bull Good))

******************************************************************************************
*** Unsuccessful proofs result in a nil solution, as in the
*** following query. Here, the failure is caused by the
*** delinquent debts of Acme.

*** QUERY 6: How good is the record for Acme?
(proveq (RECORD ?m Acme Good))

-> (q- 1)(RECORD ?m Acme Good)
(q- 2)(MAXAGE ?mll Acme ?ul:NotDelinquent)
(q- 1)(DUE ?x7301 ?x7302 Acme ?x7304 ?x7305)
(q- 2)(SALE ?mll ?x7302 ?dsalel Acme ?all . &)
(r- 2)(SALE 1 2 840118 Acme 2000.0 . &)
(r- 1)(DUE 1 2 Acme I600.0 840318)
(r- 2)(SALE 1 4 840223 Acme I290.75 . &)
(r- 1)(DUE 1 4 Acme I90.75 B40423)
(r- 2)(SALE 1 12 840507 Acme B00.5 . &)
(r- 1)(DUE 1 12 Acme B00.5 B40707)
(r- 2)(SALE 1 14 840531 Acme 90.25 . &)
(r- 1)(DUE 1 14 Acme 90.25 B40731)
((nil))

Query 5. Query 6.
```

An example of an unsuccessful proof is shown for Query 6. Here the proof fails because the only axiom to infer a customer's good record requires that the customer have no delinquent debts, and this is not true for the customer Acme to any acceptable extent. Of course, if additional rules were available to make the desired inference, they would also be tried before the proof failed.

Query 7 is an example of a more complex problem than those considered so far; part of the proof tree is shown in fig. 3, with k-values for each axiom specified next to the parent (axiom parameters are not printed out as part of the trace, to make the trace easier to follow; however, the axioms used and their parameters can be easily examined at any time, via suitable commands). In this case, several rules have to be instantiated, including several different instances of a computational procedure (SUM). In addition, this example illustrates a very important aspect of imprecise logical reasoning – the derivation of acceptable solutions with high $\mu$ -values, even when some of the information used is highly imprecise. The low $\mu$ -value for ACTIVE (=0.55) which is obtained in the proof does not cause the proof to fail, since

```txt
**********************************************************************
*** QUERY 7: Should the outstanding balance on transaction#1
*** be written off?

(proveq (WRITE-OFF ?m Toyco 1))

-> (q- 1)(WRITE-OFF ?m Toyco 1)
(q- 2)(DUE ?m11 1 Toyco ?a1 ?d1:Overdue)
(q- 3)(SALE ?m12 1 ?dsale2 Toyco ?a12 . & )
(r- 3)(SALE 1 1 840117 Toyco 6400.0 . & )
(r- 2)(DUE 1 1 Toyco 3900.0 ?d1:Overdue)
(q- 2)(CONTACT ?m21 Toyco 1 ?dt1 Negative)
(r- 2)(CONTACT 1 Toyco 1 840501 Negative)
(q- 2)(NEWPAID ?m31 Toyco 1)
(q- 3)(DUE ?m18 1 Toyco ?a8:Significant ?d18)
(q- 4)(SALE ?m19 1 ?dsale9 Toyco ?a19 . & )
(r- 4)(SALE 1 1 840117 Toyco 6400.0 . & )
(r- 3)(DUE 1 1 Toyco ?a8:Significant 840317)
(q- 3)(SALE ?mx8 ?t18 ?dx8 Toyco ?a28 . & )
(r- 3)(SALE 1 1 840117 Toyco 6400.0 . & )
(q- 3)(GT 840317 840317)
(r- 3)(GT 840317 840317)
(q- 3)(PAID-UP ?m28 Toyco 1 6400.0)
(q- 4)(GT 2500.0 6400.0)
(r- 3)(SALE 1 5 840305 Toyco 850.0 . & )
(q- 3)(GT 840505 840317)
(r- 3)(GT 840505 840317)
(q- 3)(PAID-UP ?m28 Toyco 5 850.0)
(q- 4)(GT 850.0 850.0)
(r- 4)(GT 850.0 850.0)
(r- 3)(PAID-UP 1 Toyco 5 850.0)
(r- 2)(NEWPAID 1 Toyco 1)
(q- 2)(ACTIVE ?m41 Toyco)
(q- 3)(SALE ?m125 ?t125 ?d225:Recent Toyco ?a125 . & )
(r- 3)(SALE 0 1 ?d225:Recent Toyco 6400.0 . & )
(r- 3)(SALE 0 5 ?d225:Recent Toyco 850.0 . & )
(r- 3)(SALE 0.1 6 ?d225:Recent Toyco 12000.0 . & )
(r- 3)(SALE 0.4428571428571429 10 ?d225:Recent Toyco 4325.5 . & )
(r- 3)(SALE 0.5142857142857143 11 ?d225:Recent Toyco 635.5 . & )
(r- 2)(ACTIVE 0.5464852607709751 Toyco)
(r- 1)(WRITE-OFF 0.9157538867755811 Toyco 1)
((WRITE-OFF 0.9157538867755811 Toyco 1))
```

ACTIVE has a low weight in the rule it arises in, and its low $\mu$ -value is compensated by the high $\mu$ -value of the more important premises in the rule. As a result, we are still able to obtain a result with $\mu$ -0.92.

In addition to the existentially quantified default mode and the universally quantified 'prove all' mode, the system has a mode called the Query mode. In this mode, the system checks with the user whether additional solutions are desired, after each successful solution is obtained. This enables the generation of alternative solutions under user control, without having to generate a possibly large number of alternatives in the universally quantified mode. This query mode is illustrated in Query 8. The system stops generating new solutions either when the user tells it to, or when no further solutions are possible. At this point, the system provides a list of all solutions that have been generated, along with their $\mu$ -values, which can be used to evaluate (compare) them.

One of the characteristics of the knowledge available for unstructured problems that was mentioned early in this paper was that it is often incomplete. For instance, in the course of a proof, the system might encounter a predicate for which no axioms or data is available. In the prototype, such situations result in the user being informed of the missing knowledge, and given the option of providing it interactively if possible (in the form of rules or data). The additional knowledge is then assimilated into the proof, which proceeds from that point. This feature is illustrated in Query 9. In this example, the user is notified of the lack of any information about the predicate NOTPAY-EVER. At this point, the user is able to check the proof so far, identify the axiom that contains the

```txt
**********************************************************************
*** QUERY MODE - In this mode, after generating each solution,
*** the system checks whether further solutions are required.
*** QUERY 8: What payments has Acme made?
(proveq query (PAID ?m ?t ?d Acme ?a))
-> ((PAID 1 2 840112 Acme 400.0))
another ? y n y ((PAID 1 4 840317 Acme 500.0))
another ? y n y ((PAID 1 4 840415 Acme 600.0))
another ? y n y
((PAID 1 2 840112 Acme 400.0)
(PAID 1 4 840317 Acme 500.0)
(PAID 1 4 840415 Acme 600.0))
Query 8.
```

![](/api/attachments/QNS7HG3H/fulltext/images/a2a2c028d196946b3a21ba50a67902b6addcf72f312ec5444b36897d00d61ec1.jpg)  
Fig. 3.

unknown predicate to establish the context in which the predicate is being used, and if the required information is known to him/her (as in the example), provide it. This form of interactive knowledge acquisition can be a valuable tool in the development stages of a practical system, when the knowledge base is being constructed, since it enables the system to be used productively even when all the necessary knowledge is not yet stored in the knowledge base.

```lisp
**********************************************************************
*** The following query illustrates the ability of the
*** system to interact with the user, so that he/she can provide
*** an axiom for a predicate that is required, but for which
*** the knowledge base has no axioms or tuples
*** This query is the same as #7, but an alternate axiom is
*** used (there could be several axioms for each predicate

***QUERY 9: Should we write off Toyco's debt on transaction#1?

(proveq (WRITE-OFF ?m Toyco 1))

-> (q- 1)(WRITE-OFF ?m Toyco 1)
(q- 2)(DUE ?m11 1 Toyco ?a1 ?d1:Delinquent)
(q- 3)(SALE ?m12 1 ?dsale2 Toyco ?a12 . &)
(r- 3)(SALE 1 1 840117 Toyco 6400.0 . &)
(r- 2)(DUE 1 1 Toyco 3900.0 ?d1:Delinquent)

(warning: no axioms for NOTPAYEVER)
|trapped - type "go" to continue|
| type "reset" to get to toplevel |

(printpq WRITE-OFF)

.(WRITE-OFF ?m ?x ?t)
(
(DUE ?m1 ?t ?x ?a ?d:Delinquent)
(NOTPAYEVER ?m2 ?x ?t)
(LEGAL-OP ?m3 ?x ?t Negative)
(SETVALUE ?m 0.7
(CR ( list ?m1 ?m2 ?m3) ( list 1 5 ( list 3 2 1)))))

WRITE-OFF

go

|Can you provide an axiom (y n)?y
||type in new axiom in Lisp format|
((NOTPAYEVER 1 Toyco 1))

(q- 2)(NOTPAYEVER ?m21 Toyco 1)
(r- 2)(NOTPAYEVER 1 Toyco 1)
(q- 2)(LEGAL-OP ?m31 Toyco 1 Negative)
(r- 2)(LEGAL-OP 1 Toyco 1 Negative)
(r- 1)(WRITE-OFF 1 Toyco 1)
((WRITE-OFF 1 Toyco 1))

Query 9.
```

## 7. Conclusion

In this paper, we have presented a new method for representing and manipulating fuzzy knowledge. Several features make this method versatile. First, it enables fuzziness in all components of a knowledge base to be included. Thus, the use of fuzzy operators as well as terms in relationships, the use of components with differing weights in relationships, and fuzziness in computational procedures, can be effectively handled.

The methods for manipulating this fuzzy knowledge enable fuzzy reasoning features, such as the derivation of acceptable solutions even when some of the knowledge used is highly imprecise. Imprecision in the reasoning process is conveyed be suitable bounding procedures. These bounds also help reduce the complexity of the search process during problem solving. In addition, the inference methods we present also support features such as explanation of solution procedures, user interaction during problem solving, and interactive acquisition of knowledge (as demonstrated in the example problems in section 6), which, as discussed in section 2, are useful for effective decisions support.

The primary emphasis of this paper has been on effective methods to represent and manipulate fuzzy knowledge in unstructured problem solving.

However, as mentioned earlier, it is often necessary to deal with knowledge that is uncertain as well as fuzzy. We are currently developing methods to represent and manipulate both fuzziness and uncertainty in the same framework, and also studying the implications of the joint presence of both phenomena on the problem solving process, using the prototype system.

## References

[1] Allen, J.F., M. Guiliano and A.M. Frisch, The HORNE Reasoning System, TR 126 (Dept. of Computer Science, University of Rochester, Rochester, NY, 1984).

[2] Barr, A. and E.A. Feigenbaum, The Handbook of Artificial Intelligence, vols. 1–3 (William Kaufmann, Los Altos, CA, 1982).

[3] Bellman, R.E. and L.A. Zadch, Decision Making in a Fuzzy Environment, Management Science, 17:4 (1970) B141-B163.

[4] Bennett, J.S. et al., SACON: A Knowledge Based Consultant for Structural Analysis, Tech. Report CS-89-699 (Computer Science Dept., Stanford University, CA, 1978).

[5] Bledsoe, W.W., Non-Resolution Theorem Proving, Artificial Intelligence 9 (1) (1978) 1–35.

[6] Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, NY, 1981).

[7] Carlson, E. and R.H. Sprague, Building Effective Decision Support Systems (Addison Wesley, 1982).

[8] Chang, C.L. and R.C. Lee, Symbolic Logic and Mechanical Theorem Proving (Academic Press, NY, 1973).

[9] Dubois, D. and H. Prade, On Several Representations of an Uncertain Body of Evidence, in: M.M. Gupta and S. Sanchez, eds. Fuzzy Information and Decision Processes, (North Holland, Amsterdam, 1982) 167–181.

[10] Dungan, C.W., A Model of An Audit Judgement in the form of an Expert System, PhD Thesis (Univ. of Illinois, Urbana-Champaign, IL, 1983).

[11] Dutta, A. and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer, 17:9 (1984) 89–97.

[12] Dutta, A., Reasoning with Imprecise Knowledge in Expert Systems, Information Sciences 37:1 (1985) 3–24.

[13] Feferman, S., Applications of Many-sorted Interpolation

Theorems, Proceedings of the Tarski Symposium (AMS, Providence, RI, 1975) 205–224.

[14] Foderaro, J.K., The Franz LISP Manual (Univ. of California, Berkeley, 1980).

[15] Gallaire, H. and J. Minker, Logic and Databases (Plenum Press, NY, 1978).

[16] Gupta, M.M. and E. Sanchez, eds., Approximate Reasoning in Decision Analysis (North Holland, Amsterdam, 1982).

[17] Haack, S., Do We Need Fuzzy Logic, Tech. Rep. (Dept. of Philosophy, Univ. of Warwick, 1977).

[18] Ishizuka, M., K.S. Fu and J.T.P. Yao, Inexact Inference for Rule-Based Damage Assessment of Existing Structures, Proc. IJCAI 7 (1981) 837–842.

[19] Kandel, A., Fuzzy Techniques in Pattern Recognition (Wiley, NY, 1982).

[20] Lee, R.C., Fuzzy Logic and the Resolution Principle, Journal of the ACM 19 (1972) 109–19.

[21] MACSYMA Reference Manual, Unnumbered Report (Lab. of Computer Science, MIT, Cambridge, MA, 1974).

[22] Newell, A. and H.A. Simon, Human Problem Solving (Prentice-Hall, Englewood Cliffs, NJ, 1972).

[23] Nilsson, N.J., Principles of Artificial Intelligence (Tioga Press, Palo Alto, CA, 1980).

[24] Prade, H., A Computational Approach to Approximate and Plausible Reasoning with Applications to Expert Systems, IEEE Transactions on Pattern Analysis and Machine Intelligence, vol PAMI-7:3 (1985) 260–283.

[25] Quinlan, J.R., INFERNO: A Cautious Approach to Uncertain Inference, Technical Note N-1898-RC (Rand Corp., Santa Monica, CA., 1982).

[26] Reiter, J.E., AL/X: An Inference System for Probabilistic Reasoning, M.S. Thesis (Computer Science Dept., University of Illinois, Urbana-Champaign, 1981).

[27] Robinson, J.A., A Machine-Oriented Logic Based on the Resolution Principle, Journal of the ACM 12:1 (1965) 25–41.

[28] Salton, G., et al., Extended Boolean Information Retrieval, Communications of the ACM 26 (11) (1983) 1022–1036.

[29] Winston, P.H., Artificial Intelligence (2nd ed.) (Addison-Wesley, Reading, MA, 1984).

[30] Zadeh, L.A., Fuzzy Sets, Info. Control 8 (1965) 338–353.

[31] Zadeh, L.A., Probability Measures of Fuzzy Events, Journal of Mathematical Analysis and Applications 23 (1968) 421–427.

[32] Zadeh, L.A., A theory of Approximate Reasoning, in: J.E. Hayes, D. Michie and L.I. Mikulich, eds., Machine Intelligence, vol 9 (Wiley, New York, 1979, 149–194).
