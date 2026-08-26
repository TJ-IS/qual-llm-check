---
otero_id: 17008
otero_key: "Y4DNDC94"
title: "Some problems on uncertain knowledge acquisition for rule based systems"
authors: "S. Gaglio; P.P. Puliafito; M. Paolucci; P.P. Perotto"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90018-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Some Problems on Uncertain Knowledge Acquisition for Rule Based Systems

S. GAGLIO, P.P. PULIAFITO, M. PAOLUCCI, P.P. PEROTTO

Dipartimento di Informatica Sistemistica e Telematica (DIST), Facoltà di Ingegneria, 16145 Genova, Italy

The problem of uncertainty management in systems based on rules can be dealt with using several methodologies. A particularly significant and well-founded one is based on Dempster-Shafer's Theory of Evidence. This methodology is based on the hypothesis that the values of an attribute for a certain object are mutually exclusive. This hypothesis is often too restrictive and the present work proposes a procedure of knowledge acquisition which allows for the application of the D-S theory even in cases where the objects are described, for example, in a linguistically 'conventional' manner, where such a constraint would not be satisfied.

This paper introduces the concept of knoxel and relates also to other problems which are of particular interest for the use of complex networks based on knoxels.

Keywords: Knowledge Acquisition, Uncertainty Representation, Theory of Evidence, Rule Based Systems.

![](/api/attachments/Y4DNDC94/fulltext/images/6e2f2ef790966ee471b08139cc3bd20a67075b9d812835bd581b63ad53a1fe0b.jpg)

Salvatore Gaglio was born in Agrigento, Italy, on April 11, 1954. He graduated in electrical engineering at the University of Genoa, Genoa, Italy in 1977. In 1978 he received the M.S.E.E. degree from the Georgia Institute of Technology, Atlanta, U.S.A.. From 1981 he is professor of artificial intelligence at the University of Genoa, Italy, and from 1986 professor of computer science at the University of Palermo, Italy. His present research activities are in the area of artificial

intelligence and robotics. He is a member of IEEE, ACM, and AAAI.

## 1. Introduction

At the basis of many applications of Artificial Intelligence, for which the ability to heuristically explain some of the features of human reasoning is required, we find the so-called production system [1].

We assume that such production systems are made of facts and rules. In our paper facts are of the type

$$
A (x) = v,
$$

![](/api/attachments/Y4DNDC94/fulltext/images/f9d4359a0ff524cb01107712d6955832c0c183d4d991e07cb2637c1c21a30029.jpg)

Pier Paolo Puliafito was born in Genoa on 1939 and graduated in electrical engineering at the University of Genoa, Italy, on 1965. From the early seventies he is professor of System Theory at the Engineering Faculty of Genoa and from 1983 he also teaches Operations Research and Information Systems at the same Faculty. He is working in the area of decision support systems and socio-medical decision making and helth information systems. He is presently head of De partment of Communication, Computer and System Sciences (DIST) at the University of Genoa.

![](/api/attachments/Y4DNDC94/fulltext/images/98f2ccea16938704b910c401086bf5830c7243aa4e07c1401c40050c7841d294.jpg)  
management.

Massimo Paolucci graduated in 1986 as an electronics engineer from the University of Genoa, Italy. He is presently completing his Ph.D in Computer Science at the Department of Communication, Computers and Systems Sciences (DIST) of the University of Genoa. His research interests are in the field of Artificial Intelligence, particularly knowledge acquisition and representation, uncertainty management, expert systems. He is also working on D.S.S. and database

![](/api/attachments/Y4DNDC94/fulltext/images/b68cee72888e2c3255a0fbceeed2cc995b164659bf09e32937389188cb96a420.jpg)

Pier Paolo Perotto graduated in 1986 as an electronics engineering from the University of Genoa (Italy). He started his professional career as an assistant researcher for the Department of Communication, Computers and Systems Sciences (DIST) before moving to California to work for Olivetti. Upon joining Olivetti, he belonged to the Advanced Projects Division. However, he now works both in California and Italy at the Olivetti A.I. Center (OAIC), one of the most prominent artificial intelligence groups.

which is equivalent to saying that the attribute A of object x has value v.

The rules, on the other hand, are formed by a premise, which is a condition placed on the values which might be taken by some objects and by a conclusion, which is the assignment of value to another object.

In an expert system or in a system of decision making support, knowledge is in general affected by two possible forms of uncertainty [2]. The first is connected with the mode itself of representing knowledge and the uncertainty is therefore explained by bearing in mind, in a manner congruent with the mode of representation chosen, the imperfect knowledge of logical connections and of the relations existing among assertions. This obviously also applies in the case where knowledge is represented through production rules, as described above. The second type of uncertainty, on the other hand, is encountered the moment we represent the observed world, that is the object of analysis studied by the system under discussion. In the latter case, whether because of instrumental measurements or because of linguistic measures, judgements or evaluations, the observation of phenomena is always the result of approximation and hence of uncertainty. We'll call these two types of uncertainty uncertain knowledge and uncertain observation respectively.

The methodology most commonly used in the past to represent uncertainty draws from the theory of probability and of Bayes' formula [3]. Subsequent developments proposed the use of 'certainty factors' [3], [4].

Recently, the mathematical theory of evidence, developed by A. Dempster in 1960 and extended by G. Shafer [5] has been used. According to this theory the values of the attribute of an object can be expressed by appropriate joining of ‘primary’ elements, that is of those elements which have been chosen to characterize that attribute. The word ‘element’ is used here to mean the values assigned to one of the nodes of a network, whether this represents one of the possible values on a scale used to measure an attribute or it represents a possible hypothesis to be chosen among the causes of a phenomenon (cholestasis in the example used in [3] and [6]). Elements which are not primary will be built up starting from these primary ones, considered as basic, through Boolean OR combinations. The constraints which must be satisfied by the selected elements as a whole are two:

![](/api/attachments/Y4DNDC94/fulltext/images/7124a4682c28645af713f58eba2659818c7e4e400d212b28b542083379f39e9c.jpg)  
Fig. 1.

\- the ‘primary’ elements must be mutually exclusive;

\- the combination of all the primary elements must be exhaustive, that is to say it must exhaustively represent the attribute.

The joining of all elements constitutes a whole called frame of discernment and is indicated by 1 (1 represents the Frame of Discernment). The number of possible values, with the number of primary elements assumed as equal to n, is equal to $2^{n}-1$ , since one disregards the term nought.

The values obtainable for a particular choice of elements can be represented by means of a Value Lattice (VL) (fig. 1), which puts the values in a hierarchical relationship. Each value is represented by a node: in fig. 1 four elements A, B, C and D are quoted, which bring about a frame of discernment equal to (A, B, C, D).

It is not difficult to imagine situations in which such elements do not satisfy the first of the above mentioned constraints. If, for example, one were dealing with a scale of measurement of age composed of the terms (very young, middle-aged, old, very old) or if one had to express the intensity of a phenomenon, for example pain, with the terms (unbearable, very acute, acute, not slight, slight), one could imagine several possible intersections between the values of each attribute.

## 2. Structuring the Domain

In the process of knowledge acquisition and formalization, we need to define and to structure a domain which has to be a reference for all the assertions and the rules in the system under consideration. Since in a decision support system most of the assertions are depicted in linguistic terms, such a domain must express a structure corresponding to the intuitive (for the human expert) relationship among all the terms, as referred to by the human experts.

A very general form of assertion, to which we will restrict our analysis, is one in which values of attributes of entities are compared. As a consequence, each domain is characterized by a set of entities, which are described by a set of attributes that must be entirely provided by the human expert, who must identify the objects of his reasoning and their particular aspects that are relevant in the decision process.

The expert must also explicitly provide a set of possible values for each attribute. Such a set must be exhaustive, in the sense that it must cover all the instances of the particular aspect described by the attribute. What is difficult to explicitly obtain from the expert is the relationship among the elements of a set of values, in particular when such values refer to situations which are not mutually exclusive. Our investigation concerns precisely this topic: we will present a model to represent and effectively use in the context of D-S Theory of Evidence such relationship, and an interactive procedure to elicit them from the human experts.

During the reasoning process, in the presence of uncertainty, a certain amount of evidence may be assigned to a combination of the values provided by the experts and defined as Conventional Linguistic Terms (CLT). It is, therefore, convenient to enlarge the set of all the values obtained by applying the logical operators AND, OR and NOT. We call the new values, which form a Boolean algebra, Extended Conventional Linguistic Terms (ECLT). We represent the structure of such a set by means of a Boolean lattice, that we call Values Lattice (VL).

We can assign evidence to elements (ECLT's) of VL according to the D-S theory. This is quite simple if the CLT's are mutually exclusive, as hypothesized in [6]. In such a case, each node of VL is either a CLT or a disjunction of CLT's and is guaranteed to have a different meaning from the others. Unfortunately, when linguistic terms are provided as values for attributes, it is difficult to guarantee mutual exclusion.

Generally we can refer to a VL in which conjunctions of CLT's are also present, and some of them are included in the frame of discernment. This means that the CLT's describe a more composite reality, whose single component pieces must be individuated. We say that two CLT's A and B have a Semantic Intersection (SI) if there exists a situation which can be described by both A and B, in other words both A and B are true. In such a case, the VL contains a node which is the conjunction of A and B.

Let us consider, as an example, the following terms describing the attribute ‘kind’ of the object ‘wind’:

(A) Strong,

(B) Very strong,

(C) Blowing in gusts,

(D) Dead calm.

Among these terms some SI's exist, according to the meaning that we assign to them. We assume, for instance, that very strong implies strong and sometime a strong wind can also be blowing in gusts, while dead calm is a separate case from the others. These interactions correspond to some SI's that we can represent by means of Ven diagrams, by associating each terms with a set (see fig. 2). The set of intersections determine a collection of subsets which partition the space of values and which are, therefore, mutually exclusive and represent the most elementary SI's that can be obtained from the CLT's. In our example such subsets are the set intersection that correspond to the conjunctions:

(1) A(\~B)(\~C)(\~D)

(2) AB(\~C)(\~D),

(3) $(\sim A)(\sim B)C(\sim D)$

(4) A(\~B)C(\~D),

(5) ABC(\~D),

(6) $(\sim \mathbf{A})(\sim \mathbf{B})(\sim \mathbf{C})\mathbf{D},$

![](/api/attachments/Y4DNDC94/fulltext/images/553a3ed724ac6def2b6748d3612319ae706d44f1aaa4c4d9470a4d2075795f9c.jpg)  
Fig. 2.

where the sign \~ stands for the logical NOT and the logical operator & (AND) has been omitted for convenience.

We call Possible Complete Conjunction (PCC) the logical conjunction that can be constructed from the n CLT's and has the form:

$L_{1}$ and $\cdots$ and $L_{n}$ ,

where each $L_{i}$ is either a different CLT or its negation, having excluded the case in which $L_{i}$ is a negated term for every i, because of the hypothesis of exhaustiveness.

We call knoxel or atomic knowledge element all the semantically correct conjunctions of all CLT's, in direct or negated form, that partition the value space. Clearly, the six conjunctions in the example above are knoxels. Moreover we call Potential Knoxels' Set (PKS) the set of all PCC's generated by n CLT's.

The VL constructed with all the possible disjunctions of knoxels represents the correct structure for the original set of values, in which each node is associated with a semantically correct ECLT. The set of knoxel for such a VL can play the role of the frame of discernment, as required in the D-S Theory of Evidence. The CLT's which are now expressed as disjunctions of knoxels, correspond to nodes that can have any position in the VL.

At this point, we need to consider a few practical problems in order to derive the above structure for a set of linguistic values that an attribute can take. First of all, we need a suitable method for interviewing the expert to individuate the knoxels and, then, the structure of VL.

## 3. The Individuation of the Knoxels

The problem that we address in this section is the derivation of a set of elementary SI's, that express the semantic relationship among the CLT's provided by the expert, and generate the space of values for a given attribute. Our strategy is based on a set of yes/no questions to be asked of the expert which satisfy the following two criteria:

(1) asking a limited number of questions;

(2) avoiding complex questions that cannot be understood by the expert.

![](/api/attachments/Y4DNDC94/fulltext/images/d95e6644cfa610d1812fe0cf1cfaf651fba2bece3cb0c625f972125c4d520f14.jpg)  
Fig. 3.

A way to satisfy the above criteria is to formulate the questions in a top-down fashion: more general questions come first, and at each step we collect all the information that can be used to reduce the number of successive questions. We can distinguish between two kinds of questions: the first kind (more general) asks about the existing SI's among two or more terms, while the second kind (more specific) asks which of the expressions that have not been eliminated make sense as knoxels.

Given n CLT's, an SI may involve from 2 to n of such terms. The hierarchical relationship (in the sense of the set inclusion) among the SI's for n terms can be represented with a lattice, that we call Semantic Intersection Lattice (SIL). For instance, the SIL corresponding to the terms A, B, C and D, of the previous example is shown in fig. 3.

In a SIL each node represents a possible SI, therefore, in the case of n CLT's the number of nodes is equal to $2^{n}-n-1$ . We indicate as level of a node the number of terms that occur in the associated SI. We denote as predecessors of a node those nodes of lesser level representing SI's among terms occurring in the node. We call, instead, successors of a node those nodes of greater level representing SI's comprising all the terms occurring in the node. Each successors is clearly included in its predecessors.

These hierarchical relationship represented by the arcs of the lattice allow drastic reductions in the number of questions to be asked. In particular, as soon as we have established that a node represents a not-existing SI, we can perform the two following actions:

(1) we can eliminate from the SIL the node together with all its successors, since the presence of a node in the SIL is conditioned by the presence of all its predecessors;

(2) we can eliminate from the PKS all the PCC's in which all terms that are associated with the node occur in direct (i.e. not negated) form.

The following interactive procedure of acquisition returns the set of knoxels for n CLT's

## Procedure acquisition

## 1 Consider:

\- a set PKS with $2^n$ -1 PCC's generated by $n$ CLT's;

\- a set $Z$ initially empty, that at the end will contain the PCC's that are knoxels;

\- a SIL with $2^{n} - n - 1$ nodes.

2. for $i = 2$ to $n$ do

## 3 begin

4 Select from SIL each node of level i and ask for each of them if the corresponding SI does exist (more general kind of questions).

5 if (answer = no) then eliminate from SIL the node with all its successors, and from PKS all the PCC's whose not-negated CLT's represent the SI's associated with the nodes that have been eliminated from the SIL.

## 6 end

7 Select from PKS all the PCC's whose not-negated terms do not also occur together within other PCC's; put them in Z and eliminate them from PKS.

8 while (PKS is not empty) do

9 begin

10 Select one of the remaining PCC's; eliminate it from PKS and ask if it is semantically correct (more specific kind of questions).

11 if (answer = yes) then put such a PCC in Z.

12 end.

This procedure can be simplified if we know certain properties of the semantic structure of CLT's in advance, for instance, in the case of ordered values [7].

## 4. Correlated Representation Problems

Some problems remain to be solved in order to completely achieve the goal of a friendly interface with the user. These problems concern, on one hand, the individuation of a node of the lattice corresponding to a generic Boolean expression of CLT's provided by the user, and, on the other hand, for instance, the application of some rules and the simplification of the expressions associated with the nodes, which are complex disjunctions of knoxels.

The first problem can be easily solved by means of the following procedure that individuates the node corresponding to an external expression.

## Condensed procedure translate

1. translate each term occurring in external expression into the knoxels that individuate it;

2. perform set operations of union and intersection of knoxels, in correspondence respectively with the logical operators OR and AND;

3 if the resulting expression is not empty return success, otherwise failure.

Notice that the above procedure refuses meaningless expressions.

The second problem is more difficult, since the simplification of an expression cannot be performed using the usual rules of the Boolean algebra only, because we must take into account the semantic intersections (SI's) of the CLT's. Furthermore, we have to choose which is the best expression to be used to represent a node such as to convey its intuitive meaning. This problem is still under investigation and is discussed in more detail in [8].

## 5. Concluding remarks

The Dempster–Shafer theory of evidence provides a powerful method for dealing with uncertainty in rule-based systems. However, as it happens with all methods based on probabilistic concepts, it requires a space of mutually exclusive alternatives, which in rule-based systems are the possible values that an attribute of an object can take.

Shortliffe and Gordon [6] have extended the application of the theory to hierarchical tree-structured spaces of values, but their approach still relies upon a well-individuated basic set of mutually-exclusive values. Assertions in rule-based systems are mostly expressed in linguistic terms, which are provided by human experts during the process of knowledge acquisition and which are communicated to the user in a working session. It is often difficult for such terms, which express subjective and imprecise judgments and common sense knowledge, to guarantee mutual exclusiveness.

We have presented a method which allows the application of D-S theory in those cases in which the terms provided by the expert, that we denote as conventional linguistic terms (CLT), are not mutually exclusive. The method is based on the interactive individuation, through a sequence of yes/no questions, of a lattice which represents a sort of 'deep-structure' of the domain to which the terms refer. In this lattice, denoted as value lattice (VL), the nodes correspond to a new set of values of a given attribute, which are expressed by Boolean combinations of the CLT's, and the frame of discernment, as required by the D-S theory, is made by a subset of such nodes, that we call knoxels (atomic knowledge elements), which, in general, are not those corresponding to the CLT's. In this way we separate an internal structure of the domain, which retains the formal properties required by the D-S theory, from an external structure, which retains all the expressive power of the same linguistic terms provided by the expert and used by a non-expert user.

## Acknowledgements

This research was funded partly by Italian Ministry of Education (MPI 40%, 1987 on AI) and partly by National Research Council (CNR, n. 87.02492.74 on Expert Systems and D.S.S.).

## References

[1] N.J. Nilsson: Principles of Artificial Intelligence, Palo Alto, CA, Tioga, 1980.

[2] S. Gaglio, R. Minciardi, P.P. Puliafito: On Acquisition and Processing of Uncertain Information in Rule-Based Decision Support System, Proc. of the IEEE Int. Conf. on System, Man and Cybernetics, Atlanta, Georgia, October 1986, pp. 943–948.

[3] B.G. Buchanan, E.H. Shortliffe (Eds): Rule-Based Expert System, Addison Wesley, 1984.

[4] R.O. Duda, P.E. Hart, N.J. Nilsson: Subjective Bayesian method for rule-based inference system. In AFIPS Conf. Proc. of the 1976 National Computer Conference, vol. 45 (New York) pp. 1075–1082.

[5] G. Shafer: A mathematical Theory of Evidence, Princeton University Press, Princeton, N.J., 1976.

[6] J. Gordon, E.H. Shortliffe: A Method for Managing Evidential Reasoning in a Hierarchical Hypothesis Space, Artificial Intelligence, 26 (1985) pp. 323–357.

[7] M. Paolucci, P.P. Perotto: Metodologie per il trattamento dell'incertezza nella rappresentazione della conoscenza nei sistemi esperti (Methodologies for the uncertainty management in the knowledge representation in expert system), Tesi di Laurea, Genoa, March 1986.

[8] S. Gaglio, P.P. Puliafito, M. Paolucci, P.P. Perotto: Assessment of a knowledge domain in rule based system in a theory of evidence framework (in preparation).
