---
otero_id: 17599
otero_key: "955R4C2U"
title: "A relational algebra for propositional logic"
authors: "Robert W Blanning"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90032-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A relational algebra for propositional logic

Robert W. Blanning

Vanderbilt University, Nashville, TN, USA

We apply the established relational theory of stored data to the management of propositions in two-valued logic. Since the truth table for a propositional formula is a virtual relation, we can establish a correspondence between the relational algebra, as applied to the management of stored data, and the same algebra, as applied to the management of logical formulas. In doing so, we present a single comprehensive framework for the management of these two types of information.

Keywords: Propositional logic; l-relations; Relational projection; Relational join; Relational division; Intension and extension.

Correspondence to: R.W. Blanning, Oven Graduate School of Management, Vanderbilt University, Nashville,TN 37203, USA.

## 1. Introduction

An important purpose of the research being done on decision support systems is to develop a theory of information management that is as independent as possible of the way in which the

![](/api/attachments/955R4C2U/fulltext/images/0f684c22998dafa43c1e5fdbf2447083a79a6f2fafd74309849c1475300b6ca9.jpg)

Robert W. Blanning is Professor of Management at the Owen Graduate School of Management at Vanderbilt University. He has a B.S. in Physics from the Pennsylvania State University, an M.S. in Operations Research from the Case Institute of Technology, and a Ph.D. from the University of Pennsylvania, specializing in operations research and management information systems. He has been a member of the faculties of the Schools of Business of New York University and

the Wharton School at the University of Pennsylvania. His teaching and research interests are in model management systems, information economics, and the management applications of artificial intelligence. He has published articles in Management Science, Decision Sciences, Communications of the ACM, Naval Research Logistics Quarterly, Decision Support Systems, Information and Management, Omega, Policy Analysis and Information Systems, International Journal on Policy and Information, Human Systems Management, Journal of Information Science, Long Range Planning, Technological Forecasting and Social Change, and the Concise Encyclopedia of Information Processing in Systems and Organizations, published by Pergamon Press. He has presented papers at such conferences as the National Computer Conference, the International Conference on Decision Support Systems, the International Conference on Information Systems, the International Conference on System Sciences, the International Conference on Information Resources Management, the International Workshop on Expert Database Systems, and the International Workshop on Artificial Intelligence in Economics and Management. He is a member of the Editorial Board of Decision Support Systems and is an Associate Editor of Information and Decision Technologies, and a member of the Board of Editors of Journal of Management Information Systems. He is editor of the text Foundations of Expert Systems for Management, published by Verlag Rheinland in 1990.

\* An earlier version of this paper was presented at the Twenty-Second Annual Hawaii International Conference on System Sciences, which was held at Kailua-Kona, Hawaii, January 3–6, 1989. The paper was selected by the conference organizers for submission to Decision Support Systems. This research was supported by the Dean's Fund for Faculty Research of the Owen Graduate School of Management of Vanderbilt University.

information is stored and processed. Two types of information that have been examined in some detail are stored data and decision models. We are concerned here with a third type of information – logic statements that may be true or false. We will show that a simple and elegant theory that has been developed for the management of stored data, one based on the mathematics of relations, can also fruitfully be applied to this type of logic management.

A substantial amount of effort has been devoted to the development of a relational theory of stored data $[8,10]$ and to a lesser extent of decision models $[2]$ . In the latter work, a model is viewed as a virtual relation whose tuples do not exist in stored form but are generated on demand by a stored algorithm, and the input and output attributes of the model correspond to the key and content attributes of a file. Some attention has also been paid to the development of a relational view of well-formed formulas in two-valued propositional calculus $[3]$ . In the latter work these formulas are represented both intensionally (i.e., by expressions in propositional calculus) and extensionally, in the form of simplified truth tables, which are virtual relations. It was shown that two important relational operations, projection and join, performed on the extensions correspond to two simple intensional operations. In this paper we consider a complete set of relational operations, called the relational algebra of relational database theory, and derive the corresponding intensional operations. The purpose of this effort is to interpret the relational view of data in the context of a simple form of logic. Thus, we hope to integrate, from a theoretical perspective, two important types of information, (stored) data and (logical) propositions, used in decision support $[1,2]$ .

## 2. The relational view of propositional formulas

In this section we present briefly some of the definitions and theorems of [3] in order to introduce the interpretation of the complete relational algebra in Section 3. We begin by considering a set of propositional variables that may take on the values of 1 (true) or 0 (false). These may be combined by certain operations to produce more complex propositional formulas, which will also take on the values of 1 or 0. The operations are (1) conjunction $(x \wedge y) = 1$ iff $x = 1$ and $y = 1$ , (2) disjunction $(x \vee y) = 0$ iff $x = 0$ and $y = 0$ , (3) implication $(x \to y) = 0$ iff $x = 1$ and $y = 0$ , (4) equivalence $(x \equiv y) = (x \to y) \wedge (y \to x)$ , and (5) negation $\bar{x} = 1$ iff $x = 0$ .

<table><tr><td>x</td><td>y</td></tr><tr><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td></tr></table>

Fig. 1. The extension of $x \vee y$ .

We now define an l-relation scheme (logic relation scheme) as follows:

Definition I: An l-relation scheme, S, is a set of variable names — for example, $S = \{x, y, z\}$ . An l-relation, L, defined over S, is a subset of the Cartesian product of domains of the elements of S. Thus, if S contains N variable names, then $L \subseteq \{0, 1\}^{N}$ .

For example, the l-relation for the expressions $x \vee y$ and $y \equiv z$ appear in Figures 1 and 2. All tuples in the Cartesian products for these two schemes are represented, except for those for which the expressions are false. We note that an l-relation is similar to a truth table [4] except that (1) all rows corresponding to the value “false” of the expression are missing and (2) the column containing the value of the expression (which would then take on the value “true” for each tuple) is missing. Thus, truth tables and l-relations are isomorphic up to an ordering of their rows and columns.

We note that the value “true” (or 1) defined over a scheme S consisting of N variables is represented by the full Cartesian product of the domains of S – that is, it is $\{0, 1\}^{N}$ – because it is satisfied for all combinations of the values of the variables in S. Similarly, the value “false” (or 0) defined over S is represented by the null relation over S – that is, there are no values of the variables that result in a true value for the expression.

![](/api/attachments/955R4C2U/fulltext/images/02395a873941de810337004a61a04d6a90840ad167c4400159f8b9230c316807.jpg)  
Fig. 2. The extension of $y \equiv z$ .

Since l-relations are relations, the operations of relational database theory, such as projection and join, can be performed on them. Our purpose here is to uncover the intensional meaning of these extensional operations. We begin by defining transformations between extensional and intensional representations, as follows:

Definition II: Given an expression K defined over an l-relation scheme S, its extension $\mathrm{E}(K)$ is an l-relation over S for which K is true. Given an l-relation L over S, its intension $\mathrm{I}(L)$ is a propositional formula which is true for all tuples in L and false for all tuples defined over S that are not in L.

An extension of a propositional formula is obtained by generating the Cartesian product of the domains of the variables in the formula and deleting any tuples for which the formula is false. For example, the l-relation in Figure 1 was generated by enumerating all tuples defined over the domains of x and y and eliminating those for which $x \vee y$ is false. Thus, the tuple $\langle0, 0\rangle$ was eliminated.

The intension of an l-relation is generated as a disjunction of its tuples, each of which is a conjunction of true/false assignments for the variables. For example, to obtain the intension of the l-relation in Figure 1, we write each tuple as a conjunction of variable values. Thus, the first tuple becomes $(x \wedge y)$ , the second tuple becomes $(x \wedge \bar{y})$ , and the third tuple becomes $(\bar{x} \wedge y)$ . The intension of the l-relation is the disjunction of these three expressions: $(x \wedge y) \vee (x \wedge \bar{y}) \vee (\bar{x} \wedge y)$ . This is simplified to $x \vee y$ . Quine [9], calls the expanded form a developed alternational normal schema, and the simplified expression is generally called a disjunctive normal form.

We note that the symbolic representations of intensions and extensions are not unique. For example, since an l-relation is a relation, it is unique (with respect to an intension) up to an ordering of its rows and (labelled) columns. Similarly, an intension is unique up to logical equivalence. For example, if L is the l-relation in Figure 1, then $\mathbf{I}(L) = x \vee y$ , but we could also write $\mathbf{I}(L) = \overline{\bar{x} \wedge \bar{y}}$ . We note that $\operatorname{E}(\mathbf{I}(L)) = L$ and $\mathbf{I}(\operatorname{E}(\mathbf{K})) = K$ .

Since l-relations are relations, it is possible to define the relational operations of (natural) join and projection, as follows:

Definition III: Let L and $L'$ be l-relations with schemes S and $S'$ . The join of L and $L'$ , $\mathrm{J}(L, L')$ is the subset of the Cartesian product of L and $L'$ for which the attribute values of $S \cap S'$ in L equal the attribute values of $S \cap S'$ in $L'$ .

Definition IV: Let $L$ be an l-relation on $S$ and let $S' \subseteq S$ . The projection of $L$ along $S'$ , $\mathrm{P}(L, S')$ , is formed by deleting from $L$ all columns belonging to $S \setminus S'$ and then eliminating duplicate tuples.

We note that (1) the join of any two l-relations is an l-relation, (2) the projection of an l-relation along any subset of its scheme is an l-relation, and (3) the projection of an l-relation along its scheme is the relation itself (i.e., $P(L, S) = L$ ). We now state and illustrate two results that reveal the intensional meaning of these two relational operations. Although the proofs were given in [3], they are restated here so that the paper will be self-contained.

Theorem I: Let $L$ and $L'$ be l-relations such that $\mathrm{I}(L) = K$ and $\mathrm{I}(L') = K'$ . Then $\mathrm{I}(\mathrm{J}(L, L')) = K \wedge K'$ . Similarly, $\mathrm{E}(K \wedge K') = \mathrm{J}(L, L')$ .

Proof: Let $S$ and $S'$ be the schemes for $L$ and $L'$ . We define three attribute sets: $S_1 = S \cap \overline{S}'$ , $S_2 = S \cap S'$ , and $S_3 = \overline{S} \cap S'$ . Thus, $S = S_1 \cup S_2$ and $S' = S_2 \cup S_3$ . If $S_2 \neq \emptyset$ , then the extension of $I(L) \wedge I(L')$ will consist of all combinations of tuples on $S \cup S'$ whose $S_1, S_2$ component is in $L$ and whose $S_2, S_3$ component is in $L'$ . However, these tuples are those found in the natural join of $L$ and $L'$ . If $S_2 = \emptyset$ , then the extension of $I(L) \wedge I(L')$ is the Cartesian product of the tuples in $L$ and $L'$ , which is also the natural join of $L$ and $L'$ . Therefore, $J(L, L') = E(I(L) \wedge I(L'))$ .

In other words, extensional join corresponds to intensional conjunction. For example, the l-relation in Figure 3, whose intension is $(x \vee y) \wedge (y$ $\equiv z)$ , is the join of the two l-relations in Figures 1 and 2, whose intensions are $x \vee y$ and $y \equiv z$ .

<table><tr><td>x</td><td>y</td><td>z</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td></tr></table>

Fig. 3. The join of figures 1 and 2.

Since a null relation represents a false expression (i.e., there are no values of the variables in the expression for which it is true), the join of the extensions of two or more collectively contradictory expressions will be a null relation. Consider the simplest case: a scheme S consisting of a single proposition P. The extension of p consists of the tuple $\{\langle1\rangle\}$ defined over S, and the extension of $\bar{p}$ is $\{\langle0\rangle\}$ , also defined over S. The join of these is a null set $\{\}$ defined over S, since $p \wedge \bar{p}$ is false.

Theorem II: Let $L$ and $L'$ be l-relations on $S$ and $S'$ such that $S' \subseteq S$ and $L' = \mathrm{P}(L, S')$ , then: a. $\mathrm{I}(L) \to \mathrm{I}(L')$

b. If $K$ is an expression defined on $S'$ such that $\mathrm{I}(L) \to K$ , then $\mathrm{I}(L') \to K$ .

Proof: Since $L' = \mathrm{P}(L', S')$ , the $S'$ component of any tuple in $L$ is also in $L'$ . Thus, $\mathrm{I}(L) \to \mathrm{I}(L')$ . In addition, if $K$ is the intension of an l-relation defined on $S'$ such that $\mathrm{I}(L) \to K$ , then $\mathrm{P}(L, S')$ is a subset of $\mathrm{E}(K)$ . Therefore, $\mathrm{I}(\mathrm{P}(L, S')) \to K$ , and so $\mathrm{I}(L') \to K$ .

Thus, extensional projection corresponds to intensional inference. For example, the protection of the l-relation in Figure 3 – whose intention is $(x \vee y) \wedge (y \equiv z)$ – along the scheme $\{x, z\}$ is the l-relation in Figure 4, the intension of which is $x \vee z$ . This is the most that we can infer about the relationship between x and z, given that $(x \vee y) \wedge (y \equiv z)$ is true, without any information about the value of y. Of course, if we knew the value of y, then we could state an additional assertion. For example, if y were known to be false, then the first and third rows of Figure 3 would be eliminated, and we could assert that x is true and z is false.

<table><tr><td>x</td><td>z</td></tr><tr><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td></tr></table>

Fig. 4. The projection of figure 3 along $\{x, z\}$ .

Additional information of this type may also result in redundancies or inconsistencies. For examples, if y were known to be true, then the l-relation of Figure 3 would consist of the tuples $\{\langle1,1,1\rangle,\langle0,1,1\rangle\}$ . The intension of this is $y\wedge z$ , and x can be either true or false – that is, x is independent of y and z. Thus, the l-relation can be simplified by reducing the scheme to $\{y,z\}$ , and it would consist of the single tuple $\langle1,1\rangle$ . On the other hand, if both x and y were known to be false, then the l-relation would be null, indicating an inconsistency. The inconsistency is preserved even if a null l-relation is projected along a subset of its scheme. If the null relation with scheme $\{x,y,z\}$ is projected along x and y, the result is a null relation with scheme $\{x,y\}$ . Thus, an inconsistency in the large is projected into an inconsistency in the small.

Although we have not yet presented the entire relational algebra as applied to assertions, it should be apparent that there are three differences between the relational view of data and of assertions. First, the notion of functional dependency does not arise in assertion management – for example, if $x \rightarrow y$ , it is not true that y is functionally dependent on x. Second, the tuples in an l-relation are not time varying – that is, they are not individually updated. Thus, notions of storage anomalies and normal forms do not arise in assertion management. (However, another important issue in information organization, that of lossy and lossless joins, does arise and has been addressed in [3].) Third, l-relations have an elegant intensional representation (i.e., the propositional calculus), which makes is possible to interpret the relational algebra in logical terms – thus, making it possible to establish a correspondence between the algebras of these two important types of information. We have begun to do this in this section, and will complete it in the following section.

## 3. The relational algebra of propositional formulas

We are now ready to present and interpret the full complement of the operations that make up the relational algebra of relational database theory $[8,9]$ in the context of l-relations. The operations are as follows:

1. Projection and Join

2. Selection

3. The set operations of union, intersection, difference and complementation

4. Renaming

5. Division

The first of these was presented in the previous section of this paper, and the fourth is trivial. The second and third are straightforward, once their meaning is clear. The fifth, relational division, is more complicated, and we will examine at the end of this section.

Selection is accomplished by limiting the tuples in a relation to those that meet the restrictions of a logical expression containing assignments or comparisons (i.e., equalities or inequalities) – such as $(x = 1)$ , $(x \geqslant y)$ , $(x = 1 \text{ AND } y = 0)$ , etc. Strictly speaking, inequalities do not apply to assertions, since the domain $\{1, 0\}$ is not an integer domain; it could be denoted {true, false}. However, 0 and 1 are sometimes in the domains of both integer and logic operators (such as in APL), and we will allow that interpretation here. We now present the intensional analogue of extensional selection:

Theorem III: Let L be an l-relation, and let k be a logical expression containing assignments or comparisons. Let K be an assertion derived from k as follows: x = 1 is replaced by x, x = 0 is replaced by $\bar{x}$ , x < y is replaced by $\bar{x} \wedge y$ , $x \leqslant y$ is replaced by $x \rightarrow y$ , x = y is replaced by $x \equiv y$ , AND is replaced by $\wedge$ , OR is replaced by $\vee$ , and NOT is replaced by negation. Then the intension of the selection of L, restricted by k, is $I(L) \wedge K$ .

Proof: The tuples that remain after a selection operation has been performed on a relation are those that satisfy exactly two criteria. First, they must have been in the original relation. Therefore, their intension can be true only if $I(L)$ is true. Second, they must satisfy the selection criteria. Therefore, their intension can be true only if a logic statement equivalent to the selection criteria is true. The rules for deriving K from k ensure that this logic statement is K. Therefore, the intension of L selected by k is $I(L) \wedge K$ .

The set operations of union (denoted $\cup$ ) intersection (denoted $\cap$ ), and difference (denoted $\setminus$ ), are performed on the tuples of relations that are union compatible - that is, on the tuples of relations that have the same schemes. The complement of a relation, which is denoted by the same symbol ( $\overline{L}$ ) as the negation operator, is the set of tuples in the Cartesian product of domains of the relation that are not in the relation itself. The correspondence between intensional logic operations on propositions and extensional set operations on relational tuples is demonstrated in:

Theorem IV: If $L$ and $L'$ are union-compatible l-relations with intensions $K = \mathrm{I}(L)$ and $K' = \mathrm{I}(L')$ , then:

$$
\begin{array}{l l} 1. & \mathrm{I} (L \cup L ^ {\prime}) = K \lor K ^ {\prime} \\ 2. & \mathrm{I} (L \cap L ^ {\prime}) = K \land K ^ {\prime} \\ 3. & \mathrm{I} (L \setminus L ^ {\prime}) = K \land \overline {{K}} ^ {\prime} \\ 4. & \mathrm{I} (\overline {{L}}) = \overline {{K}} \end{array}
$$

Proof: Since the tuples in an l-relation correspond to the sets of values of the scheme assertions for which the intension of the relation is true, the union (resp., intersection) of two sets of tuples corresponds to the sets of values for which either (resp., both) of the intensions are true, and hence, to $K \vee K'$ (resp., $K \wedge K'$ ). Similarly, since the tuples in the complement of an l-relation correspond to the sets of values of the scheme assertions for which the intension of the relation is false, complementation corresponds to negation and set subtraction to intersection and negation.

The fourth operation, renaming, consists of changing the name of a variable to another name (e.g., changing x to w) in the labelled column of an l-relation. This corresponds to making the same change in the intension of the l-relation.

Relational division is a more complex operation and is defined as follows:

<table><tr><td>NAME</td><td>SKILL</td></tr><tr><td>SMITH</td><td>SMALLTALK</td></tr><tr><td>JONES</td><td>LISP</td></tr><tr><td>JONES</td><td>PROLOG</td></tr><tr><td>BROWN</td><td>LISP</td></tr></table>

Fig. 5. Data example - The dividend.

Definition V: Let L and $L'$ be l-relations defined over S and $S'$ , where $S' \subseteq S$ . L will be called dividend and $L'$ will be called the divisor. Q is the quotient of L and $L'$ , written $Q = L \div L'$ , if Q is defined over $S \setminus S'$ and the tuples in Q are the largest subset of $\mathrm{P}(L, S \setminus S')$ such that $\mathrm{J}(Q, L') \subseteq L$ . The remainder, R, is defined by $R = L \setminus \mathrm{J}(Q, L')$ . We note that Q and R are l-relations and that $R \div L'$ is a null relation over S.

Before describing relational division in the context of logic management and presenting its intensional interpretation, we illustrate its use in relational database management. Consider the data relation in Figure 5, which contains the names of three programmers and the names of the programming languages in which they are skilled. We will divide this by the relation in Figure 6, which is defined over the skill attribute and contains two tuples, corresponding to two elements in the language domain – LISP and PROLOG. The quotient, displayed in Figure 7, is defined over all of the attributes (i.e., NAME) not in the divisor. The quotient is the largest subset of the NAME elements for which there is both a LISP and a PROLOG tuple in the dividend. In other words, it consists of the names of

Fig. 7. Data example - The quotient $(Q)$ .

Fig. 6. Data example - The divisor.  
Fig. 8. Data example - The remainder $(R)$ .

<table><tr><td>x</td><td>y</td><td>z</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td></tr></table>

Fig. 9. Logic example - The dividend $(L)$ .

all people who program both in LISP and in PROLOG. The remainder is a subset of the dividend; it consists of all tuples except for the LISP and PROLOG records of JONES. We note that if JONES were also skilled in another language (e.g., APL), then a $\langle$ JONES, APL $\rangle$ tuple would appear in the dividend and also in the remainder. Finally, we note that there is no person in the remainder who programs in both LISP and PROLOG (although BROWN programs in LISP).

When the dividend and the divisor are l-relations, the interpretation is the same, except that it can be represented intensionally. Let the dividend be the l-relation in Figure 9, which is the extension of $(x \vee y) \wedge (y \equiv z)$ . (This is the same as Figure 3.) Let the divisor be the l-relation in Figure 10, which is the extension of z (i.e., the statement that z is true). The quotient, given in Figure 11, is the extension of y. (In other words, y is true and nothing is known about x.) The intensional interpretation of the quotient opera-

Fig. 10. Logic example - The divisor $(L')$ .

Fig. 11. Logic example - The quotient $(Q)$ .

tion is that y is the most general statement that one can make about the relationship between x and y such that if the assertion is true and z is true, then $((x \vee y) \wedge (y \equiv z))$ is true (i.e., $I(L)$ is true). We now demonstrate formally these properties of l-relational division:

Theorem V: Let $L, L', Q$ and $R$ be l-relations over $S, S', \subseteq S, S \setminus S'$ , and $S$ , respectively, such that $Q = L \div L'$ and $R = L \setminus \mathrm{J}(Q, L')$ . Then:

1. $((\mathbf{I}(Q) \wedge \mathbf{I}(L')) \vee \mathbf{I}(R)) \equiv \mathbf{I}(L)$

2. $\mathrm{I}(R\div L') = 0$

Proof: #1 holds because (1) the tuples in L consists of both the tuples in $\mathrm{J}(Q, L')$ and the tuples in R, and (2) the union of the tuples in two union-compatible relations corresponds to an intensional OR ( $\vee$ ) operation (Theorem IV-1). #2 holds because $R \div L'$ is the null relation over S—that is, all of the rows of the truth table for $\mathrm{I}(R)$ result in the value “false.”

## From Theorem V one can derive

Corollary I: If the conditions of Theorem V obtain, then:

1. $(\mathrm{I}(Q)\wedge \mathrm{I}(L'))\to \mathrm{I}(L)$

2. $\mathrm{I}(R)\to \mathrm{I}(L)$

For example, in the example of Figures 9–12, we have

1. $\operatorname{I}(Q) = y$

2. $\mathrm{I}(L') = z$

$$
3. \mathrm{I} (L) = (x \vee y) \wedge (y \equiv z)
$$

4. $\mathrm{I}(R) = x\wedge \bar{y}\wedge \bar{z}$

and therefore,

$$
5. (y \wedge z) \rightarrow ((x \vee y) \wedge (y \equiv z))
$$

$$
6. (x \wedge \bar {y} \wedge \bar {z}) \rightarrow ((x \vee y) \wedge (y \equiv z))
$$

![](/api/attachments/955R4C2U/fulltext/images/f712ca587a9924f7b56587a0322705a8b14e58b15833cfe0f44212f8e30a585a.jpg)  
Fig. 12. Logic example - The remainder $(R)$ .

## 4. Possible extensions

It was stated at the beginning of this paper that an important purpose of the research being done on decision support systems is to develop a theory of information management that is as independent as possible of the way in which the information is stored and processed. A promising framework for information organization and processing that spans a variety of information types is a relational framework, in which each information source (e.g., a data file, a decision model, or knowledge element) is viewed as a stored or virtual relation – that is, as a subset of the Cartesian product of domains representing variables of interest. These variables may be key or content fields in a file, input or output parameters in a decision model, or propositions (i.e., logic variables) that may be true or false. We are concerned here with the latter, and our purpose has been to demonstrate the applicability of the relational algebra of relational database theory to the management of propositional logic.

The purpose of this work is not to present a computationally efficient method for processing expressions in propositional logic. There are more efficient ways of doing this than to represent the expressions in extensive form and to store and process them using a relational database management system. Rather, we wish to demonstrate a correspondence between the relational framework that has proven useful in the management of stored data and some of the important operations of propositional logic.

One problem with an extensional implementation of logical inference is the memory requirements for storing l-relations and the computational effort needed to process them. If the number of propositions is small, as in the simple examples given here, extensional representation and processing is both computationally feasible and instructive, as it helps to illustrate the correspondence between data management and a very elementary (i.e., propositional) form of logic management. But as the number of propositions increases, the computational complexity of logic operations reduces both the illustrative value of extensional processing and its computational feasibility [7]. However, this does not negate the principal purpose of this work: to demonstrate a correspondence, at a fundamental level, an important relationship between the management of propositional variables and other types of information (stored data and decision models) used in decision support.

The relationship between model management and propositional logic has not been examined here, except by noting that a relational framework has been developed for model management [1]. However, a relationship between propositional logic and an important class of operations research models, those based on mathematical programming, has been examined [5]. Although propositional variables are symbolic variables (taking on the values TRUE and FALSE), they can be interpreted as numerical variables (taking on the values 1 and 0), and techniques of integer programming have been applied to their solution.

These observations suggest that it may be possible to extend this work to first order logic – or at least to an appropriate subset of quantified logic. It is possible to reduce formulas in predicate logic to propositional approximations to the formulas [6]. Restrictions of the problem domain (e.g., the number of quantified arguments and the nature of any functions in the predicate formulas) may result in an analytically tractable and insightful extension of this work. Similar extensions may be possible in other areas of knowledge management, such as those involving networks, frames, objects, and case-based knowledge.

## 5. Conclusion

Decision makers are being given access to an increasing variety of information sources – such as stored data, decision models, and expert knowledge – and it is important that a common framework be developed for as many of these sources as possible. We have suggested elsewhere that the established relational framework for stored data be enlarged to encompass decision models [1], and we suggest in [2,3] and here that it be specialized to encompass logic statements.

## References

[1] Blanning, Robert W., A Relational Theory of Model Management, in: Decision Support Systems: Theory and Applications, ed. by Clyde W. Holsapple and Andrew B. Whinston, Springer-Verlag, Berlin, 1987, pp. 19–53.

[2] Blanning, Robert W., A Relational Framework for Information Management, in Decision Support Systems: A Decade of Perspective, ed. by Ephraim R. McLean and Henk G. Sol, North-Holland, Amsterdam, 1986, pp. 25–40.

[3] Blanning, Robert W., A Relational Framework for Assertion Management, Decision Support Systems, Vol. 1, No. 2, April 1985, pp. 167–172.

[4] Hilbert, D. and Ackerman, W., Principles of Mathematical Logic, Chelsea, New York, 1950.

[5] Hooker, J.N., A Quantitative Approach to Logical Inference, Decision Support Systems, Vol. 4, No. 1, March 1988, pp. 45–69.

[6] Jeroslow, Robert G., Computation-Oriented Reductions of Predicate to Propositional Logic, Decision Support Systems, Vol. 4, No. 2, June 1988, pp. 183–197.

[7] Lewis, Harry R., Complexity Results for Classes of Quantification Formulas, Journal of Computer and Systems Sciences, Vol. 21, No. 3, December 1980, pp. 317–353.

[8] Maier, David, The Theory of Relational Databases, Computer Science Press, Rockville, 1983.

[9] Quine, W.V., Methods of Logic, (Fourth Edition), Harvard University Press, Cambridge, 1982 (Chapter 11: Simplification, pp. 74–77).

[10] Yang, Chao-Chi, Relational Databases, Prentice-Hall, Englewood Cliffs, 1986.
