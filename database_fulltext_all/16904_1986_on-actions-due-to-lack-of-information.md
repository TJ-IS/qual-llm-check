---
otero_id: 16904
otero_key: "Z3XA52WJ"
title: "On actions due to lack of information"
authors: "Bengt G. Lundberg"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90094-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On Actions Due to Lack of Information

Bengt G. LUNDBERG

Delft University of Technology, Delft, The Netherlands

The problem of making conclusions from representations of knowledge is presented and analyzed. In particular, conclusion making due to lack of information has been studied. The concepts of immediately available information, assumptionally inferable information and constructively inferable information are introduced and exemplified. It follows that it is important to specify the assumptions that are made about a representation, in particular with respect to the conclusions that can be made from the representation. Concerning constructively inferable information it is shown that the lack of information can only be used to select which among a set of possible conclusions to make.

![](/api/attachments/Z3XA52WJ/fulltext/images/8dcffc32cb1fd89aaeb87cd092c3890107a72300e61a09ca4116f8bc304875a6.jpg)

Bengt G. Lundberg is acting professor in Computer Sciences, Information Systems, at the Chalmers University of Technology and the University of Göteborg, Sweden. He received his Ph.D. from the Royal Institute of Technology, Stockholm, in 1982. His current research interests are concerned with epistemological and methodological aspects of design of knowledge-based systems.

## 1. Introduction

It often occurs that human beings are performing an action, instead of another possible action, due to lack of information. The same phenomenon occurs when a conclusion is made instead of another conclusion due to that a better goal satisfaction is achieved. Those phenomena are well known, for example, in computer programs ('if...then...else...'-statements), in knowledge based systems ('if absent...then...'-statements [2]) and also in heuristic search systems (e.g., the best-first strategy [1]). The problems concerned with conclusion making due to lack of information has in particular been pointed out in the area of production rule systems for modelling of condition-action behavior of human beings, e.g., [2].

In this paper we analyze and discuss the basic principles involved in conclusion making (or decision making) due to lack of information. The analysis starts from the assumption that one has knowledge about a domain and that an explicit representation of part of that knowledge is created. The created representation can be used to inform about the domain in three ways, namely by (direct) interpretation of the representation, by application of assumptions about the representation and by application of (assumed) inference rules in the representation. Thus, three types of information can be recognized, namely immediately available information, assumptionally inferable information, respectively constructively inferable information.

The main result of our discussions is that a clear distinction has to be made concerning lacking information depending on whether it is due to assumptions about the represented knowledge or it is due to not (yet) constructed valid conclusions. Further, a general requirement is stated concerning production rules which reflect conclusion making due to lack (or absence) of information. The underlying principle is that a production rule must subsume a valid deductive rule which is not affected by an absence operator.

## 2. Preliminary discussion

Assume that a human being has knowledge about an object system, i.e., a set of objects to which a set of predicates is applicable. When representing that knowledge in a language usually only part of the knowledge is explicitly represented and the rest of the knowledge is considered to be subsumed by a set of assumptions made about the explicitly represented knowledge. A typical case is that we usually only represent positive facts (and not the negated facts).

The information that can be communicated from the explicitly represented knowledge is here referred to as immediately available information. The information that can be inferred from an explicit representation is of two types, namely assumptionally inferable information which is inferred due to the assumptions made about the representation (such as the negated facts) and constructively inferable information which is inferred due to the inference rules that are considered to hold in the representation. It can be argued that the inference rules for a representation are also assumptions about it. However, the inference rules are constructive in the sense that conclusions are made from the existing representation and the conclusions that are made due to the assumptions about the representation have the absence of represented information as a premissse.

When constructing a representation of knowledge it is important to state explicitly the assumptions made about the represented knowledge, in particular as the assumptionally inferable information can be used as premises of constructively inferable information. This means that the conclusions that can be made may depend on the assumptions that are made about the representation.

As a preliminary example let us consider a marine map. The knowledge that is represented in the map is the immediately available information. It may represent those areas of the sea bottom which are deep enough for an ordinary ship. When using the map in navigation of a ship we do not assume that passages exist that can be used in going from one place to another if they are not marked on the map. Further, we do not expect to hit a rock if we keep to the areas which are denoted deep enough. However, we cannot exclude the possibility of deep passages when searching for a submarine hiding in the archipelago. It should be noted that the assumptions we apply to a representation when using it, must not be stronger than the assumptions made when the representation is constructed.

## 3. Assumptionally inferable information

## 3.1. A preliminary example

Consider the following knowledge base:

$$
\begin{array}{l l} \text {secretary (Jim)} & \text {trucker (Joan)} \\ \text {secretary (James)} & \text {truck (EUJ 399)} \end{array}
$$

Further, assume that the following query is stated:

secretary(John)?

The logical answer to that query is 'don't know' as

\- nothing supports the proposition that John is a secretary,

\- nothing supports the proposition that John is not a secretary.

In most database applications the above query would be negatively replied due to that the following assumptions are made:

\- as it is not stated that John is a secretary it is concluded that he is not a secretary,

\- as it is not explicitly stated that 'John' and, say, 'Jim' are synonyms it is assumed that the symbols are not synonyms.

It should be noted that the above knowledge base could be completed with expressions such that the logical answer to the query is 'no', i.e., the knowledge base should be completed with expressions corresponding to the assumptionally inferable information.

## 3.2. Name uniqueness

A usual assumption made in database systems is that the used symbols (names) refer to distinct objects, i.e., no symbols are considered to be synonyms. That assumption is made, e.g., when a functional dependency is controlled in a relational database, cf [3]. Assume a relation with two attributes, say, $R(EMP, SAL)$ for which the functional dependency $EMP \rightarrow SAL$ holds. The functional dependency has the following representation in standard first-order predicate logic [5]:

$$
\forall x \forall y \forall z (r (x, y) \&r (x, z) \rightarrow y = z).
$$

Further, assume the following two instances of the relation:

$$
r (\text { Jim }, 1 0 0) \quad r (\text { Jim }, 1 5 0),
$$

from which we can derive 100 = 150 (assuming the axioms of equality). If we complete the database with expressions denoting the inequality of the symbols,

$$
1 0 0 \neq 1 5 0 \quad \text {   Jim   } \neq 1 0 0 \quad \text {   Jim   } \neq 1 5 0,
$$

we immediately obtain an inconsistency.

In order to state the assumption of name uniqueness we arrive at a meta statement as follows:

if $a_i$ and $a_j$ are names and $i \neq j$ then conclude $-(a_i = a_j)$ .

The above statement, however, precludes the use of synonyms in the database. That preclusion can be removed by the following formulation:

if $a_{i}$ and $a_{j}$ are names and $i \neq j$ and unless $a_{i} = a_{j}$ is stated then conclude $-(a_{i} = a_{j})$ .

This means that unless it is explicitly stated that two symbols are synonyms then we immediately conclude that they are not.

The above statements can be expressed as deductive rules by the use of auxiliary symbols, cf [6]:

$$
\begin{array}{l} \text { name } (x), \text { name } (y), \text { notid } (x, y) \to - (x = y), \\ \text { respectively } \\ \text { name } (x), \text { name } (y), \text { notid } (x, y), \omega (x = y) \to \\ - (x = y), \end{array}
$$

where notid and $\omega$ are auxiliary symbols denoting the inequality of symbols, respectively the absence of an expression.

## 3.3. Completeness assumption

The completeness assumption implies that for those expressions which cannot be proved in a representation their negation is assumed to hold. This means in particular that a fact that is not explicitly represented is assumed to be false. The assumption implies a problem concerning the possibility of stating something about objects we do not know about. So, let us restrict ourselves to the case that the assumption holds for those predicates and names which are known to us. Then the assumption can be formulated as follows:

for a predicate $p$ of degree $n$ and an $n$ -ary sequence $\bar{a}$ of names and $p(\bar{a})$ is not stated then conclude $-p(\bar{a})$ .

The corresponding formal representation of the assumption becomes

$$
\text { name } (x), \omega (p (x)) \rightarrow - p (x),
$$

where p is a parameter, as well as x is, and thus such an expression is required for all (known) predicates.

However, the assumption is too strong in the case that we perform deductions in the representations according to some deductive rules. For example assume the following deductive rule

$$
p (x) \rightarrow q (x),
$$

and an instance $p(a)$ . Before the above deductive rule is applied the assumption would imply $-q(a)$ . But, the deductive rule would construct the conclusion $q(a)$ which thus results in an inconsistency. This implies that the order of the application of the completeness assumption respectively the deductive rule is crucial. However, the problem can easily be removed by requiring that the completeness assumption is applied only to the basic predicates, i.e., those predicates which are not only consequences of deductive rules.

## 3.4. Domain closure assumption

When we discussed the completeness assumption, cf section 3.3, we assumed that the assumption only applies to known predicates and symbols, i.e., those that are represented. That assumption also implies that we do not consider objects which are not known, i.e., we consider only those which are referred to by a symbol (name). A stronger formulation of the latter assumption is the domain closure assumption which states that no other objects are considered to exist than those referred to by the symbols of the system. That assumption can directly be represented in predicate logic as the domain closure axiom [4]

$$
\forall x (x = a \vee x = b \vee x = c \dots),
$$

where $a, b$ and $c$ , etc., are names used in the system.

The domain closure axiom has consequences concerning the objects being referred to by existentially quantified formulae, e.g.

$$
\forall x \exists y (e m p l o y e e (x) \rightarrow h a s - s a l a r y (x, y)).
$$

In this case the domain closure axiom implies that for the second argument of the predicate, hassalary, only a known object can be substituted. The above formula of the domain closure assumption has a global validity in a system and a more realistic version of it would be to constrain it to specific types of objects, e.g., no other persons exist than those being represented

$\forall x$ (person $(x) \to x = \operatorname{Jim} \lor x = \operatorname{James}$ ),

which for a name different from 'Jim' and 'James' gives -person(a), where $a$ is the considered symbol.

## 3.5. Comments

In the formulation of the name uniqueness assumption and the completeness assumption we used the absence operator, which has been introduced as an auxiliary symbol. The formal formulations of the assumptions introduced earlier conform to the pattern

$$
\omega (p) \rightarrow q,
$$

which means that we conclude q because of the absence of p. However, we have restricted the application of the absence operator to the basic predicates which becomes obvious when constructively inferable information is considered.

## 4. Constructively inferable information

## 4.1. Introduction

With constructively inferable information we refer to the information that is derived in an explicit representation of knowledge according to a set of deductive rules. This means in particular that the representation is assumed to be completed with expressions inferable according to the assumptions made about the representation. A deductive rule is a rule according to which a conclusion can be constructed from a set of pre-misses satisfying the antecedent of the rule. For example, assume the following deductive rule and instances of the antecedent

$$
\begin{array}{l} \text { has - salary } (x, y), - m a n a g e r (x) \to e m p l o y e e (x), \\ \text { has - salary } (\text { Jim }, 1 0 0), \\ - m a n a g e r (\text { Jim }), \end{array}
$$

from which we can conclude employee(Jim).

In the area of production rule systems, constructs including an absence operator are found, e.g., [2]

$$
\begin{array}{l}\text {has - salary} (x, y), \omega (\text {manager} (x))\\\quad \rightarrow \text {business - class} (x),\\\text {has - salary} (x, y), \text {manager} (x) \rightarrow \text {royal - class} (x),\end{array}
$$

where the conclusions that can be made can be considered as prescriptive sentences. The symbol $\omega$ denotes the absence operator (cf section 3). The idea behind production rule systems is that condition-action relations are acquired and represented in a rule base. The condition-action relations are considered to reflect chunks of knowledge of a human being about a domain and are considered to reflect heuristic knowledge about the domain. Thus, the acquired rules are not considered to be the deductive rules of a formal system (though they may be so), rather they are rules which are composed of an inferential part and a control part to be applied in a system generating conclusions according to the breadth-first strategy.

## 4.2. Control of deductions

Assume a formal system for which a set of deductive rules are specified. The deductive rules may be recursive and when applied according to a breadth-first strategy gives an infinite set of conclusions, as here being exemplified by the deductive rule for conjunction of propositional logic

$$
A, B \rightarrow A \&B,
$$

where A and B refer to propositional sentences.

Even if the deductive rules are not recursive, as above, one might wish to restrict the set of actually performed deduction, e.g., for efficiency reasons. This corresponds to the selection of an action among a set of possible actions in decision making.

Assume the following two deductive rules

$$
A \rightarrow B,
$$

$$
A \rightarrow C.
$$

Assuming that A is satisfied, one can conclude both B and C when the rules are applied. In order to restrict the number of constructed conclusions the antecedents of the rules have to be completed with a criterion for application – such a criterion is here referred to as a heuristic criterion. The above rules thus can be completed as follows:

$$
H _ {1}, A \rightarrow B,
$$

$$
H _ {2}, A \rightarrow C,
$$

where $H_{1}$ and $H_{2}$ are the heuristic criteria. A rule which is completed in this way is thus restricted to be applied only when the heuristic criterion is also satisfied. It should be noted that the conclusions B and C are both valid conclusions as soon as A is satisfied and thus the heuristic criterion does not affect the validity of the conclusions.

## 4.3: Acquired rules

When production rules are acquired from human beings the rules are normally not primitive deductive rules but rules which state under which condition a conclusion is made. This means that the rules may include a heuristic criterion and an inferential part, though the components are not recognized. With respect to our earlier examples the rules can be of the following types:

$$
A, B \rightarrow C,\tag{T1}
$$

$$
\omega (A), B \rightarrow C,\tag{T2}
$$

$$
\omega (A) \rightarrow C.\tag{T3}
$$

The problem is now whether it is interesting to find out which part of the antecedent of a rule is the heuristic criterion and which part is the antecedent of a deductive rule. If the absence operator is not present in a rule the problem is not very interesting. But, if the absence operator is present in the antecedent the rest of the rule must be a valid deductive rule (not necessarily primitive), i.e., the following must be valid rules (cf above)

$$
B \rightarrow C,
$$

$$
\rightarrow C.\tag{T2'}
$$

(T3')

This gives us a criterion of correctness of acquired rules; that topic will be further explicated in the next section.

## 4.4. Correctness criteria on rules

In order to explain the preliminary criterion on correctness of rules let us consider the following set of rules

$$
A, B \rightarrow E,\tag{R1}
$$

$$
F \rightarrow D,\tag{R2}
$$

$$
\omega (D) \rightarrow - C,\tag{R3}
$$

$$
D, E \rightarrow C.\tag{R4}
$$

Further, assume that A, B and F are satisfied. An execution of the above rules according to a breadth-first strategy gives the derivation graph in fig. 1, where we arrive at an inconsistency from C and -C, and conclude that the rule system is incorrect. The above problem is due to that the system interprets the rules as deductive rules (and the detected inconsistency is delayed). If we had a set of deductive rules to which heuristic criteria are applied we would not face the problem as all the conclusions are valid conclusions and a lagging inconsistency would result only if the deductive rules are inconsistent. One solution to the problem is to make sure that the residual rules, when the parts that are affected by the absence operator are disregarded, are valid rules. This can be performed by informal reasoning only. It follows

(1) Given a rule

$$
\omega (A), B \rightarrow C,
$$

$B \to C$ must be a valid rule.

$$
(2) \text {   Given   a   rule   }
$$

$$
\omega (A) \rightarrow C,
$$

C must be an axiom, i.e., it always holds in the considered domain.

In the more general case when the rules include variables we have to consider that

(3) The variables of the consequent must also occur in the antecedent of a valid rule.

In particular the latter point gives us a criterion for the correctness of an acquired rule, namely

level 0

level 1

![](/api/attachments/Z3XA52WJ/fulltext/images/97d3ab79ff4866997e68b6b66bf802f479bc67b0824effae4efea2fd7c55b666.jpg)

level 2

Fig. 1.

the consequent of a rule must not include a variable which only occurs in the antecedent in an expression being affected by the absence operator.

Thus, the following rule is incorrect in the above sense:

$$
\omega (p (y)), q (x) \rightarrow r (x, y),
$$

but the following rule is correct:

$$
\omega (p (x)), q (x, y) \rightarrow r (x, y),
$$

because the absence operator only restricts the values that can be substituted for the variable x.

In the above presentation we have not considered the assumptions about the immediately available information, for which the pattern concerning the absence operator is

$$
\omega (p) \rightarrow - p.
$$

Together with the rules above we can conclude that the absence operator may be applicable to an expression if the expression represent immediately available information. However, in that case we propose that it is better to separate the two types of rules as follows:

Assume the rule

$$
\omega (p), q \rightarrow r,
$$

where p is a basic predicate, for which the completeness assumption holds. Reformulate the rule as follows:

$$
\begin{array}{c}\omega (p) \rightarrow - p,\\- p, q \rightarrow r.\end{array}
$$

The latter formulation makes the criteria above applicable to the acquired rules.

## 4.5. Use of the absence operator

Concerning constructively inferable information we have to assume a set of inference rules to which heuristic criteria are applied. The rule of the heuristic criteria, independent of whether they include the absence operator or not, is to select a subset of the inference rules for application, i.e., the heuristic criteria determine which action to perform. When the absence operator is used it is important not to interprete it as a negation operator, i.e., $\omega(p)$ and -p do not have the same meaning. The former expression denotes that it is not known that p holds and the latter expression denotes that it is known that p is false (and thus $\omega(-p)$ denotes that it is not known that p is false).

Example. Assume that it holds for an application

‘a status is on if an on event has occurred and an off event has not occurred’.

Let us assume that we have knowledge about the successor relation for time points. Then, we arrive at the rules

$$
o n (x) \rightarrow s (x),
$$

which means that if an event has occurred on a time point then the status is on at the time point; $s(x)$ , $suc(x, y)$ , $\omega(off(y)) \to s(y)$ ,

which means that the status is on also at the following time point if an off event has not occurred.

However, the rule

$$
s (x), s u c (x, y) \rightarrow s (y),
$$

can not be considered as a valid rule, thus we have to rewrite the second rule as follows:

$$
s (x), \operatorname{suc} (x, y), - o f f (y) \rightarrow s (y),
$$

which means that we have applied the completeness assumption, i.e.,

$$
\omega (o f f (x)) \rightarrow - o f f (x).
$$

Example. The use of the absence operator to select one of two rules is quite straightforward and corresponds to the 'if...then...else...' -constructs of ordinary programming languages.

$$
\omega (C), A \rightarrow B,
$$

$$
C, A \rightarrow D,
$$

in which case either B or D will be concluded depending on the presence of C (assuming that A is satisfied).

Example. Let us assume a system for which the following inference rules are specified:

$$
A, B \rightarrow K,\tag{R1}
$$

$$
B, C \rightarrow L,\tag{R2}
$$

$$
D, L \rightarrow M,\tag{R3}
$$

$$
E, D \rightarrow P,\tag{R4}
$$

$$
P, K \rightarrow M,\tag{R5}
$$

which can be illustrated as in fig. 2. From the figure we find two ways of deriving M and the crucial premises are A, C and E. Let us assume that B and D are satisfied. It follows that P and K should be deduced only when C is absent even if both A and E are satisfied, i.e., the interesting rules should become

$$
\omega (C), A, B \rightarrow K,\tag{R1'}
$$

$$
\omega (C), E, D \rightarrow P,\tag{R4'}
$$

$$
B, C \rightarrow L.\tag{R2}
$$

![](/api/attachments/Z3XA52WJ/fulltext/images/f70028d537de19098a50b8e461fa849c421378b94732c1fd16eb493933920f3d.jpg)  
Fig. 2.

This means that if C is satisfied (present) two inferences are performed, otherwise three inferences will be performed. Further, if all the expressions A-E are satisfied and the absence operator is not used five inferences will be performed.

## 5. An interpretation of the results

The role of the heuristic criterion, and in particular the absence operator, is to select suitable deductive rules (or actions) to be performed in order to arrive at a desired result. The decision making that is involved in that selection process makes the results (which are presented earlier in this paper) applicable to, e.g., decision support systems and the modelling of heuristic decision rules.

The main result of section 4.4 states that a decision rule should conform to the presented criteria and that the rule must include a valid decision rule, i.e., be a correct decision rule. Further, the set of alternative, but disregarded, decisions are those which are disregarded only because the heuristic criterion is not satisfied. However, the main and the most difficult problem is to conclude the primitive valid rules (or decisions) of a system. Our results thus give some hints for finding the valid rules.

Example. Assume that a person is going to make air line reservations for a number of persons. Assume also that it is known that all the persons are qualified for tickets. In the case that a person is manager he/she should have a royal class ticket and in case not a manager a business class ticket. In such a case it might be legitimate to give a business class ticket in the situation it is not known whether a person is a manager or not. The reason may be that it is to difficult (or to expensive) to find out which is the case. Thus, we arrive at the following rules

$$
\text { manager } (x) \rightarrow \text { royal - class } (x),
$$

$$
\omega (\text { manager } (x)) \rightarrow \text { business - class } (x),
$$

where the conclusions are the decisions that are taken and to be reacted upon. The latter rule can be interpreted as a default rule stating the default decision to make.

## 6. Conclusions

In this paper we have discussed the information that can be obtained from representations of knowledge. The concepts of immediately available information, assumptionally inferable and constructively inferable information are introduced and exemplified. The performed analyses show that it is important to specify the assumptions that are made about a representation, and in particular what conclusions can be made from the absence of information. Further, the role of lacking information when making conclusions, or decisions, is discussed. It follows that the lack of information can be used only in order to select which among a set of possible and valid conclusions to make.

## Acknowledgements

The author wishes to thank Prof. H.G. Sol, M.A.F. van Schaik and Dr. J. van den Herik for constructive criticism and suggestions for improvements on earlier versions of this paper.

## References

[1] N. Nilsson. Principles of artificial intelligence, Tioga, Palo Alto, CA (1980).

[2] E. Charniak, D. McDermott. Introduction to artificial intelligence, Addison-Wesley (1985).

[3] B. Lundberg. On correctness of information models, Information Systems 8, No. 2 (1983).

[4] R. Reiter. Data bases: A logical perspective, SIGMOD 11: 2 (1981).

[5] J-M. Nicolas. First order logic formulations for functional, multivalued and mutual dependencies, Proc. ACM-SIGMOD Conf., Austin, USA (1978).

[6] H.B. Curry. Foundations of mathematical logic, Dover (1977).
