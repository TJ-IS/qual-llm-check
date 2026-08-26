---
otero_id: 17344
otero_key: "KAYYP2U8"
title: "Relational division in information management"
authors: "Robert W. Blanning"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90044-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Relational division in information management

Robert W. Blanning

Vanderbilt University, Nashville, TN, USA

We present a unified framework for the management of stored data, decision models, and assertions in two-valued logic, based on the algebra of relations and on the operation of relational division. This powerful operation was developed in the context of stored data, and it also has limited applicability to models and assertions. The strength and weakness of division is that it allows universal quantification of certain queries on partitioned relations. We extend this concept by introducing a new operation, relational pseudodivision, which replaces universal with existential quantification and thus enlarges the set of available partitioning operations.

Keywords: Relational division, Data management, Model management, Assertion management, Modal logic.

## 1. Introduction

An important purpose of decision support systems is to integrate a variety of information sources – such as stored data, decision models, and logic-based information of the type found in knowledge bases. (Other types of knowledge structures, such as frames, and other types of information, such as text and visual information, will not be considered here.) For this reason an important purpose of the research being done on decision support systems is to develop a theory of information management that is as independent as possible of the way in which the information is stored and processed.

A unifying framework that has proven useful in several contexts is one based on the mathemat-

![](/api/attachments/KAYYP2U8/fulltext/images/e9fbda36bae0997edf63d0ee9371da7736cf166dab98622921a7e07330527e77.jpg)

The Wharton School at the University of Pennsylvania. His teaching and research interests are in model management systems, information economics, and the management applications of artificial intelligence. He has published in such journals as Management Science, Decision Sciences, Communications of the ACM, Naval Research Logistics Quarterly, Decision Support Systems, Information and Management, Omega, Policy Analysis and Information Systems, international Journal on Policy and Information, Human Systems Management, Journal of Information Science, Range Planning, and Technological Forecasting and Social Change. He has presented papers at such conferences as the National Computer Conference, the International Conference on Decision Support Systems, the International Conference on Information Systems, the International Conference on System Sciences, the International Conference on Information Resources Management, the International Workshop on Expert Database Systems, and the International Workshop on Artificial Intelligence in Economics and Management. He is a member of the Editorial Boards of Decision Support Systems and Information Systems Research, an Associate Editor of Information and Decision Technologies, and a member of the Board of Editors of Journal of Management Information Systems.

ical theory of relations. This framework was originally developed for the management of stored data, in which files are viewed as relations with key and content attributes, and file processing and file integration tasks are defined in terms of such relational operations as selection, projection, and join. A similar framework has been developed for model management, in which models are viewed as virtual relations whose tuples do not exist in stored form but are generated on demand by stored algorithms temporarily resident in core memory [2]. The attributes of these virtual relations are model inputs and outputs, and relational join corresponds to output-to-input model integration. A relational framework has also been developed for the management of assertions in two-valued logic, in which a modified truth table is a virtual relation and the extensional operations of projection and join correspond to the intensional operations of inference and conjunction [1].

The familiar operations of selection, projection, and join have been interpreted in the context of data, model, and assertion management. Another operator, relational division, has also been defined for data relations $[3,5,6]$ . Relational division can be defined in terms of the more traditional relational operators – specifically, set subtraction, projection, and Cartesian product – and it provides a powerful set processing capability for partitioned relations that easily allows certain universally quantified queries. This operation has not been applied to model relations, but it has been applied in a primitive way to assertion relations $[1]$ . In this paper we examine the operation of relational division in the context of these three types of relations and thus, compare the management of stored data, decision models, and logical assertions in the context of a single powerful operation.

One consequence of this comparison is a demonstration that relational division, as it is conventionally defined, is not sufficient to capture the variety of relational partitioning operations that one might wish to perform, especially in model management. Therefore, we will define an additional relational operation, which we will call pseudodivision. Pseudodivision can also be defined in terms of the more traditional relational operations - in this case, projection, set subtraction, and join. Pseudodivision is similar to relational division in that universal quantification is replaced by existential quantification, a pseudoquotient is a superset of a relational quotient, and a pseudoremainder is a subset of a relational remainder. Another advantage of pseudodivision, especially in assertion management, is that it naturally raises the issues of possible world semantics as it applies to tuples in a relation and of unnormalized relations in information management. These topics are briefly addressed.

We begin in Section 2 with a review of relational division in relational database theory, and we define pseudodivision and compare it with division. In Section 3 we summarize the relational view of assertions in two-valued logic and interpret division and pseudodivision in this context. In Section 4 we summarize the relational view of decision models and investigate the applicability of division and pseudodivision to the processing of virtual relations. We conclude by examining the possibility of using relational structures and operations as a unifying framework for information management.

## 2. Relational division and pseudodivision

In addition to the familiar operations of relational data management – selection, projection, and join – there is a growing interest in another operation, relational division [3,4,6,7]. Relational division is defined as follows. $^{1}$ Consider relations X (the dividend) and Y (the divisor), with $\sigma(\mathbf{Y}) \subseteq \sigma(\mathbf{X})$ . The quotient $Q = X \div Y$ is a relation defined over $\sigma(\mathbf{X}) \setminus \sigma(\mathbf{Y})$ consisting of all tuples $\langle q \rangle$ such that for each tuple $\langle y \rangle \in Y$ we have $\langle q, y \rangle \in X$ . Consider the dividend relation in Figure 1, in which customers are renting cassettes. The divisor in Figure 2 consists of the cassettes, and the quotient in Figure 3 consists of all customers who rent both cassettes. In this case $\sigma(\mathbf{X}) = \{\text{CUSTOMER}, \text{CASSETTE}\}$ , $\sigma(\mathbf{Y}) = \{\text{CASSETTE}\}$ , and $\sigma(\mathbf{X}) \setminus \sigma(\mathbf{Y}) = \{\text{CUSTOMER}\}$ . The remainder R, given in Figure 4, consists of all $\langle \text{CUSTOMER}, \text{CASSETTE} \rangle$ combinations in the dividend other than those in which a customer rents all of the cassettes specified in the divisor. Thus, $R = X \setminus (Q \times Y)$ . We note that one can recover the dividend from the divisor, quotient, and remainder in a fashion similar to that of arithmetic: $(Q \times Y) \cup R = X$ . We also note that relational division can be defined in terms of the more conventional operations of projection, Cartesian product, and set subtraction. If we define relations A and B such that

<table><tr><td>CUSTOMER</td><td>CASSETTE</td></tr><tr><td>HIPPOLYTE</td><td>ROBIN HOOD</td></tr><tr><td>HIPPOLYTE</td><td>THE GREEN BERETS</td></tr><tr><td>OPHELIA</td><td>ROBIN HOOD</td></tr><tr><td>OPHELIA</td><td>THE BRIDE OF FRANKENSTEIN</td></tr><tr><td>TRILBY</td><td>ROBIN HOOD</td></tr><tr><td>TRILBY</td><td>THE BRIDE OF FRANKENSTEIN</td></tr><tr><td>TRILBY</td><td>THE JAZZ SINGER</td></tr><tr><td>XANTHIPPE</td><td>THE WAR OF THE ROSES</td></tr></table>

Fig. 1. Dividend (stored data relation).

$$
\begin{array}{l} \mathrm{A} = \pi (\mathrm{X}, \sigma (\mathrm{X}) \setminus \sigma (\mathrm{Y})), \\ \mathrm{B} = \pi ((\mathrm{A} \times \mathrm{Y}) \setminus \mathrm{X}, \sigma (\mathrm{X}) \setminus \sigma (\mathrm{Y})), \\ \text { then } \mathrm{X} \div \mathrm{Y} = \mathrm{A} \setminus \mathrm{B}. \end{array}
$$

The original purpose of relational division was to define an algebra that operates on partitioned relations with a set processing capability [6]. To date there have been two principal extensions of this concept, each of which allows even more powerful set operations to be expressed conveniently in a relationally complete language. One is Grouped Generalized Division (GGD), in which division is based not only on set containment, but on a $\theta$ operator that includes containment, equality, inequality, disjointness, etc. [4]. In addition, the schemes of the dividend and the divisor are each partitioned into three attribute lists, and two of the lists in the dividend are compatible with (i.e., contain the same attributes as) two of the lists in the divisor. One of the pairs of attribute lists is used to group the tuples in the two relations and the other is used to perform the division. GGD is accomplished by comparing the groups of tuples in the two relations, and then performing the division.

## CASSETTE

ROBIN HOOD
THE BRIDE OF FRANKENSTEIN
Fig. 2. Divisor (stored data relation).

## CUSTOMER

OPHELIA
TRILBY
Fig. 3. Quotient (stored data relation).

The second extension of relational division is provided by a HAS operator, which selects dividend tuples by combinations of values of the divisor attributes [3]. For example, we may wish to identify those customers who have not rented any of the cassettes specified in the divisor (in this case, XANTHIPPE) or who have rented all of the cassettes in the divisor but no others (in this case, OPHELIA). There are 63 such operators, called HAS operators, some of which allow for the recovery of the dividend – that is, $(Q \times Y) \cup R = X$ . The existence of the various HAS operators demonstrates that this property of traditional relational division is not exclusive, but rather is shared with other similar operators.

We now examine in detail a variation on this theme, which we will call relational pseudodivision, which is of special interest because it can be extended to relational model bases in order to specify a type of sensitivity analysis. Since relational division identifies the tuples in the dividend which are completed by all of the tuples in the divisor, it is defined by universal quantification across the tuples in the divisor. As we will see, it is often useful, especially in model management, to consider existential quantification as well. For example, we may ask which customers rented any of the cassettes in the divisor – that is, which customers rented either ROBIN HOOD or THE BRIDE OF FRANKENSTEIN (or both). This operation, which we will call pseudodivision, results in a pseudoquotient, given in Figure 5. Since HIPPOLYTE rented ROBIN HOOD (but not THE BRIDE OF FRANKENSTEIN), she appears in the pseudoquotient, even though she is not in the quotient. The pseudoremainder, given in Figure 6, consists of all <CUSTOMER, CASSETTE> combinations in the dividend other than those for which a customer rents any

<table><tr><td>CUSTOMER</td><td>CASSETTE</td></tr><tr><td>HIPPOLYTE</td><td>ROBIN HOOD</td></tr><tr><td>HIPPOLYTE</td><td>THE GREEN BERETS</td></tr><tr><td>TRILBY</td><td>THE JAZZ SINGER</td></tr><tr><td>XANTHIPPE</td><td>THE WAR OF THE ROSES</td></tr><tr><td>HIPPOLYTE</td><td>THE GREEN BERETS</td></tr><tr><td>TRILBY</td><td>THE JAZZ SINGER</td></tr><tr><td>XANTHIPPE</td><td>THE WAR OF THE ROSES</td></tr><tr><td colspan="2">Fig. 6. Pseudoremainder (stored data relation).</td></tr></table>

## CUSTOMER

HIPPOLYTE
OPHELIA
TRILBY
Fig. 5. Pseudoquotient (stored data relation).

of the cassettes specified in the divisor. Thus, the pseudoremainder consists of the remainder less the tuple $\langle$ HIPPOLYTE, ROBIN HOOD $\rangle$ .

Before formally defining pseudodivision, it may be helpful to write the symbolic definition of division for dividend X and divisor Y with $\sigma(\mathrm{Y}) \subseteq \sigma(\mathrm{X})$ . The definition presented above in terms of the relations A and B is based on the relational algebra. A more intuitive definition based on the relational calculus is as follows [10]:

$$
\begin{array}{l}\mathrm{Q} = \mathrm{X} \div \mathrm{Y}\\\qquad = \left\{\langle \mathrm{q} \rangle | \forall \mathrm{y} ((\langle \mathrm{y} \rangle \in \mathrm{Y}) \rightarrow (\langle \mathrm{q}, \mathrm{y} \rangle \in \mathrm{X})) \right\}.\end{array}
$$

We now define pseudodivision by replacing universal with existential quantification.

Definition 1: Given relations X and Y, the pseudoquotient of X and Y, denoted X∅Y or Q', is

$$
= \left\{\langle q ^ {\prime} \rangle | \exists y ((\langle y \rangle \in Y) \rightarrow (\langle q ^ {\prime}, y \rangle \in X)) \right\},
$$

and the pseudoremainder is $\mathbf{R}' = \mathbf{X} \setminus (\mathbf{Q}' \times \mathbf{Y})$ .

We note that for a pseudoquotient to exist we must have $\sigma(\mathbf{Y}) \subseteq \sigma(\mathbf{X})$ , and as with division, we have $\sigma(\mathbf{Q}') = \sigma(\mathbf{X}) \setminus \sigma(\mathbf{Y})$ and $\sigma(\mathbf{R}') = \sigma(\mathbf{X})$ . We also note that one cannot recover the dividend from the divisor, pseudoquotient, and pseudoremainder in a fashion analogous to the simple method appropriate for the quotient and remainder – that is, the identity $(\mathbf{Q}' \times \mathbf{Y}) \cup \mathbf{R}' = \mathbf{X}$ does not obtain. For example, since HIPPOLYTE did not rent THE BRIDE OF FRANKENSTEIN, the tuple $\langle$ HIPPOLYTE, THE BRIDE OF FRANKENSTEIN $\rangle$ does not appear in X. But this tuple does appear in $(\mathbf{Q}' \times \mathbf{Y}) \cup \mathbf{R}'$ , since $\langle$ THE BRIDE OF FRANKENSTEIN $\rangle$ is in the divisor, HIPPOLYTE rented ROBIN HOOD, and $\langle$ ROBIN HOOD $\rangle$ is also in the divisor. However, we note that $X \subseteq (Q' \times Y) \cup R'$ .

Four additional properties of relational pseudodivision are specified in Proposition 1. The first can be inferred from Figures 1–6: the quotient is a subset of the pseudoquotient and the pseudoremainder is a subset of the remainder. The second concerns the case in which division is equivalent to pseudodivision. The third describes the relationship between dividend, divisor, pseudoquotient and pseudoremainder, and the fourth allows us to define pseudodivision in terms of projection, join, intersection, set subtraction, and Cartesian product.

Proposition 1: Let X and Y be dividend and divisor relations with quotient and pseudoquotient Q and Q' and remainder R and R'. Then
1. Q ⊆ Q' and R' ⊆ R
2. Q = Q' iff R = R'
3. X ⊆ ((Q' × Y) ∪ R')
4. Q' = π(Θ(X, Y), σ(X) \ σ(Y))
[Proven in Appendix I.]

The last result is of special interest, because it allows us to define a pseudoquotient in terms only of projection, set subtraction, and join. But one should keep in mind that for Q' to be defined, and thus for Proposition 1 to be valid, we must have $\sigma(Y) \subseteq \sigma(X)$ . If we relax this requirement by allowing $\sigma(Y) \setminus \sigma(X) \neq NULL$ , the result would be a generalized pseudodivision operation that would be similar to a semijoin, except that the generalized pseudoquotient is $\pi(\Theta(X, Y), \sigma(X) \setminus \sigma(Y))$ , whereas the semijoin is $\pi(\Theta(X, Y), \sigma(X))$ . Generalized pseudodivision does not appear to be relevant here, but it may later prove to be useful in other contexts.

Another possible generalization, which turns out to produce the same result, would be obtained by replacing the semijoin with the semi-outerjoin. This would make a difference if there were a tuple in the divisor that does not correspond to any tuple in the dividend. For example, if the divisor in Figure 2 were to contain the tuple $\langle STAR\ WARS\rangle$ , with no change in the dividend (i.e., no customer rented it), then the quotient would not exist and the pseudoquotient would be unchanged from the one in Figure 5. However, one could construct the outerjoin over $\{CUSTOMER, CASSETTE\}$ , which would consist of the five purchases of ROBIN HOOD and THE BRIDE OF FRANKENSTEIN, along with the tuple $\langle NULL, STAR WARS\rangle$ . This would also be the semi-outerjoin of X and Y, and the projection of this along $\sigma(X)\setminus\sigma(Y)$ would be the pseudoquotient (Figure 3). Although a value NULL would appear in the CUSTOMER column of the outerjoin, it would disappear when the outerjoin is projected along the CUSTOMER attribute, since it is not a part of a larger tuple. Thus, the proposition of the semi-outerjoin along $\sigma(X)\setminus\sigma(Y)$ , like that of the semijoin, is the pseudoquotient.

Thus, a pseudoquotient can be viewed as a transformed semijoin of two relations in which (1) the scheme of one of the relations is wholly contained within the scheme of the other and (2) the semijoin is then projected along those attributes of the larger scheme that are not contained in the smaller scheme. However, there is another difference, which concerns the motivation for defining these two operations. A semijoin is intended to increase the efficiency of performing joins in distributed relational databases by reducing the volume of data that must be exchanged among the relations [14]. The motivation for defining pseudodivision is quite different. A pseudoquotient is a superset of a quotient that is useful when the criteria for completing a tuple is less restrictive than that arising in relational division – that is, when any match (rather than all matches) is appropriate – and a pseudoremainder is a restriction of the remainder in that it is a subset of the remainder consisting of those tuples in the dividend not matched by any tuple in the divisor.

The principal purpose of pseudodivision is to help to define a type of sensitivity analysis. Consider a relation whose schema includes two sets of attributes with a many-to-one mapping from the first set to the second. (Thus, each attribute in the second set is functionally dependent on the attributes in the first set.) For example, the first set may be an employee identifier and the second the employee's salary. Then division can be used to determine all employees earning a particular salary (which would be the sole tuple in the divisor), but not to determine the employees earning salaries in a particular range. For this purpose it would be useful to identify a range variable (i.e., a symbol designating all salaries within a particular range) and to divide by a relation consisting of the range variable in the salary domain. The pseudoquotient will consist of all people whose salaries are in the designated range.

Another example is a decision model, which would be represented by a virtual relation whose tuples are generated on demand. Consider a financial model that determines the net present value of an investment as a function of the project under consideration (identified by means of a project identification symbol) and an assumed inflation rate. Pseudodivision could be used to identify those projects that will produce a return of 10% to 12% with an assumed inflation rate of 4%–8%. As before, relational division would produce no answer (i.e., the quotient would be a null relation) unless only a single number were used for each percentage figure – for example, a return of 11% and an inflation rate of 5%. But in the more general case, where the query contains a range of returns and inflation rates, it is necessary to replace universal with existential quantification – that is, to replace relational division with pseudodivision.

## 3. Division and pseudodivision in relational assertion management

We now turn to the case in which the variables of interest are not multivalued attributes of entities but rather are statements, or assertions, that can be true or false. Assertions can be combined to produce other assertions by using logical operators such as AND, OR, and NOT.

Assertions are represented in extensional form as a set of tuples in a virtual relation specifying the circumstances under which the assertion will be true or in intensional form as an expression in sentential logic [1]. For example, the extensions of $x = (a \lor b)$ and $y = (b \rightarrow c)$ appear in Figure 7. These are isomorphic with the truth tables for

<table><tr><td colspan="2">a b</td><td colspan="2">b c</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td></tr></table>

Fig. 7. Relations to be joined (virtual assertion relation).

<table><tr><td>a</td><td>b</td><td>c</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr></table>

Intension: $\theta = (a \vee b) \wedge (b \to c)$

Fig. 8. Joined relation (virtual assertion relation).

<table><tr><td>a</td><td>c</td></tr><tr><td>1</td><td>1</td></tr><tr><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td></tr></table>

Intension: $\pi = (\mathbf{a} \vee \mathbf{c})$

Fig. 9. Projection of the join (virtual assertion relation).

<table><tr><td>a</td><td>b</td><td>c</td><td>d</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr></table>

Intension: $\mathbf{x} = ((\mathbf{a} \equiv \mathbf{b}) \land (\mathbf{c} \oplus \mathbf{d})) \lor (\mathbf{a} \land \neg \mathbf{b} \land \mathbf{c})$

Fig. 10. Dividend (virtual assertion relation).

<table><tr><td>c</td><td>d</td></tr><tr><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td></tr></table>

Intension: $\mathbf{y} = (\mathbf{c}\oplus \mathbf{d})$  
Fig. 11. Divisor (virtual assertion relation).

<table><tr><td>a</td><td>b</td></tr><tr><td>1</td><td>1</td></tr><tr><td>0</td><td>0</td></tr></table>

Intension q = (a = b)

Fig. 12. Quotient (virtual assertion relation).

<table><tr><td>a</td><td>b</td></tr><tr><td>1</td><td>1</td></tr><tr><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td></tr></table>

Intension: $q^{*} = (b \to a)$

Fig. 13. Pseudoquotient (virtual assertion relation).

<table><tr><td>a</td><td>b</td><td>c</td><td>d</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr></table>

Intension: $r = (a \wedge \neg b \wedge c)$  
Fig. 14. Remainder (virtual assertion relation).

these expressions: each tuple specifies the values of the labelled assertions (a and b in the first case and b and c in the second case) for which the assertions x or y will be true, and values for which they will be false are omitted. We will call these relations (in which 1 represents TRUE and O represents FALSE) a-relations, or assertion relations.

Three interesting relationships between relational operations performed on extensions and corresponding logical operations performed on intensions are given in Proposition 2. Two of these are illustrated in Figures 7–9. The first result is that extensional join corresponds to intensional conjunction. For example, the join of the two relations in Figure 7 appear in Figure 8, and its intension is $(a \lor b) \land (b \rightarrow c)$ , which is the conjunction of the intensions of the two relations in Figure 7. The second result is that the projection of an a-relation along a subset of its scheme has an intension that is implied by the intension of the original relation. For example, the relation of Figure 8 is projected along the scheme $\{a \lor c\}$ in Figure 9. The intension of this projection, $(a \lor c)$ , is implied by the intension of the relation in Figure 8 – that is:

$$
\left(\left(a \vee b\right) \wedge (b \rightarrow c)\right)\rightarrow (a \vee c).
$$

In other words, if we know that either a is true or b is true or both are true and that wherever b is true c is true, then the most complete information we have about the relationship between a and c is that either a is true or c is true or both are true. Thus, extensional projection corresponds to intensional implication. The third result is that extensional set inclusion for union-compatible relations also corresponds to intensional implication.

Proposition 2: Let X, Y, and Z be a-relations with intensions x, y, and z. Then

1. $Z = \Theta (X,Y)$ iff $z = x\wedge y$

2. If $\sigma(\mathbf{Y}) \subseteq \sigma(\mathbf{X})$ and $\mathbf{Y} = \pi(\mathbf{X}, \sigma(\mathbf{Y}))$ , then $\mathbf{x} \to \mathbf{y}$

3. If $\sigma(X) = \sigma(Y)$ , then $x \to y$ iff $X \subseteq Y$

[Proven in Appendix II.]

We now apply these results to the results of Section II in order to examine the intensional meaning of a-relational division and pseudodivision. These operations are illustrated in Figures

<table><tr><td>a</td><td>b</td><td>c</td><td>d</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr></table>

Intension: $r' = (a \land \neg b \land c \land d)$  
Fig. 15. Pseudoremainder (virtual assertion relation).

10–15, and the results of interest are given in Proposition 3. The first three results are analogous to those of the previous section, and the fourth result corresponds to the fourth result of Proposition 1.

Proposition 3: Let X and Y be dividend and divisor a-relations with quotient Q, psuedoquotient Q', remainder R, and pseudoremainder R', and let the corresponding intensions be x, y, q, q', r, and r'. Then

1. $\mathbf{q}\rightarrow \mathbf{q}^{\prime}$ and $\mathbf{r}'\to \mathbf{r}$

$$
2. \mathrm{x} \equiv ((\mathrm{q} \wedge \mathrm{y}) \vee \mathrm{r})
$$

$$
3. \mathrm{x} \rightarrow ((\mathrm{q} ^ {\prime} \wedge \mathrm{y}) \vee \mathrm{r} ^ {\prime})
$$

$$
4. (\mathbf {x} \land \mathbf {y}) \rightarrow \mathbf {q} ^ {\prime}
$$

$$
[ \text { Proven   in   Appendix   III. } ]
$$

For example, in the example of Figures 10–15, the quotient is $q = (a \equiv b)$ , since it is the largest relation on $\{a, b\}$ that, when joined (by conjunction) with the divisor $c \oplus d$ , produces a product contained in the dividend. The only larger relations are $a \to b$ (which contains the additional tuple $\langle 0, 1 \rangle$ ), $b \to a$ (which contains $\langle 1, 0 \rangle$ ), and 1, the true relation over $\{a, b\}$ which contains all of the tuples in $\{0, 1\}^2$ . All three of these would produce tuples not found in the dividend. However, the pseudoquotient is $b \to a$ , since the additional tuple $\langle 1, 0 \rangle$ over $\{a, b\}$ completes the tuple $\langle 1, 0 \rangle$ in the divisor to produce the fifth tuple in Figure 10. Thus augmentation of tuples requires that $q \to q'$ ; that is $(a \equiv b) \to (b \to a)$ . A similar but more cumbersome argument can be used to demonstrate that $r' \to r$ and results 2 and 3 of Proposition 3.

The fourth result of Proposition 3 corresponds to the fourth result of Proposition 1. In the example, the first four tuples in Figure 10 correspond both to the quotients and the divisor, the fifth tuple corresponds to the pseudoquotient (but not the quotient) and the divisor, and the last corresponds to the pseudoquotient but neither the quotient nor the divisor. Thus, we can state that the divisor entails the pseudoquotient. This can be stated another way: whenever the dividend is true, the divisor entails the pseudoquotient (i.e., $x \rightarrow (y \rightarrow q')$ ). In this example, if we restrict ourselves to the tuples in the dividend, we have $(c \oplus d) \rightarrow (b \rightarrow a)$ . In fact we have $b \rightarrow a$ for all of the tuples in Figure 10. Similarly, we can demonstrate $y \rightarrow (x \rightarrow q')$ – that is, whenever the divisor is true, the dividend implies the pseudoquotient.

Finally, we examine an analogy with the results of Section 2 that does not hold. For any dividend and divisor the quotient and pseudoquotient are equal if and only if the remainder and pseudoremainder are equal. From this one would expect that the expression $(q \equiv q') \equiv (r \equiv r')$ would be valid. That it is not valid can be seen by evaluating the last tuple in Figure 10, for which a = 1, b = 0, c = d = 1 and thus q = 0 and $q' = r = r' = 1$ . In this case, the expression $(q \equiv q') \equiv (r \equiv r')$ is false.

Although the above expression is not valid, there is a sense in which equality of quotient and pseudoquotient is equivalent to equality of remainder and pseudoremainder, as was pointed out in Section 2. In order to describe this and contrast it with the invalid result above it is necessary to index the tuples in the dividend. Let $\omega \in \Omega$ be the index, so that the first tuple in Figure 10 corresponds to $\omega = 1$ , the second to $\omega = 2$ , etc., and $\Omega$ is the set $\{1 \ldots 6\}$ . Thus, the sixth tuple $(a \wedge \neg b \wedge c \wedge d)$ corresponds to $\omega = 6$ , and $a(6) = 1$ , $b(6) = 0$ , and $c(6) = d(6) = 1$ . We now index $q(\omega)$ , $q'(\omega)$ , $r(\omega)$ , and $r'(\omega)$ , each of which will be true or false, depending on the value of $\omega$ - for example, $q(6) = 0$ and $q'(6) = r(6) = r1(6) = 1$ . We have seen that the following expression is not valid.

$$
\forall \omega ((q (\omega) \equiv q ^ {\prime} (\omega)) \equiv (r (\omega) \equiv r ^ {\prime} (\omega))),
$$

since it is violated when $\omega = 6$ . But it is true that for any X and Y

$$
\forall \omega (\mathrm{q} (\omega) \equiv \mathrm{q} ^ {\prime} (\omega)) \equiv \forall \omega (\mathrm{r} (\omega) \equiv \mathrm{r} ^ {\prime} (\omega)),
$$

which corresponds to Result (2) of Proposition 1 (i.e., that $\mathbf{Q} = \mathbf{Q}'$ iff $\mathbf{R} = \mathbf{R}'$ ).

This results suggests an interpretation in terms of a simple modal logic of necessity and possibility, in which the dividend represents a universe of possible worlds, each tuple corresponding to a possible world $[9,13]$ . If □ is the necessity operator, then for any X and Y, we have

$$
\Box (q \equiv q ^ {\prime}) \equiv \Box (r \equiv r ^ {\prime})
$$

but not

$$
\Box \left(\left(q \equiv q ^ {\prime}\right) \equiv \left(r \equiv r ^ {\prime}\right)\right).
$$

In other words, we envision a possible world for each tuple in the relation and thus, for each set of truth values of the propositional variables for which the intension of the relation is true. Any statement involving these variables that is true in all possible worlds is said to be necessarily true, any statement that is false in all possible worlds is necessarily false, and all remaining statements are contingently true (and also contingently false). We have shown above that for any dividend and divisor, it is necessarily true that the quotient and pseudoquotient are equivalent (i.e., they are both true and both false) if and only if it is necessarily true that the remainder and pseudoremainder are equivalent. However, it is not necessarily true that the quotient is equivalent to the pseudoquotient if and only if the remainder is equivalent to the pseudoremainder.

The suggestion that a relation, real or virtual, be viewed as a universe of possible worlds with an appropriate invocation of possible world semantics may be useful more generally. For stored relations the universe is the entity set being described, and each entity is a possible world. When the relation is virtual, the universe is the set of conditions being modeled. In this case a condition is a set of assignments of truth values to the ground assertions that make up the assertion describing the universe - and each such set describes a possible world. We have assumed that the accessibility relation is the Cartesian product of the worlds, so that the worlds are completely connected, any world being accessible from any other. However, more sophisticated patterns of accessibility, such as those of temporal logic, have proven useful elsewhere. Whether other types of accessibility are useful in relational information management is at present an open question.

## 4. Division and pseudodivision in relational model management

Models, like assertions, may be viewed as virtual relations, but they are similar to stored data relations in that they contain input and output attributes, the latter being functionally dependent on the former, just as data relations typically contain both key and contact attributes, with the content being functionally dependent on the key [2]. In this respect, model bases are similar to functional data bases [11], but the nature of the functional dependencies, and especially of the relational operations, differs. For example, in relational model management, a join corresponds to an output-to-input integration of two or more models.

![](/api/attachments/KAYYP2U8/fulltext/images/fffb1b6bcfd2a379eea07450bff1a9b8b9f6c33281bd2dbcfb889838c15d742e.jpg)  
Fig. 16. Joined model relations.

Consider Figure 16, in which $\alpha$ and $\beta$ are the input and output of model A and $\beta$ and $\gamma$ are the input and output of Model B. For example, $\alpha$ may be the prices to be charged for several products, $\beta$ the resulting sales volumes, and $\gamma$ the total cost of producing to these volumes. We note that not all outputs of A are permissible inputs of B and vice versa - that is, the range of the mapping from $\alpha$ to $\beta$ is not equal to the domain of the mapping from $\beta$ to $\gamma$ . The diagrams of Figure 16 are drawn so as to avoid repetition of symbols as much as possible - for example, Model A is a virtual relation with five tuples, two of which contain the attribute value $\beta_{1}$ .

Relational division is of limited use in model management, since the quotient will generally not exist. (We will say that a relation does not exist if it contains no tuples.) For example, if X = A and $Y = \{\langle \beta_{1} \rangle, \langle \beta_{2} \rangle\}$ , then q = NULL, since there is no $\alpha'$ such that both $\langle \alpha', \beta_{1} \rangle$ and $\langle \alpha', \beta_{2} \rangle$ are in X.

Proposition 4: Consider a model $\mathbf{X} = \{\langle \alpha(\omega), \beta(\omega) \rangle | \omega \in \Omega\}$ such that for any $\omega \neq \omega'$ , we have $\alpha(\omega) \neq \alpha(\omega')$ . Then

(1) If Y is defined over $\alpha$ , then $X \div Y$ exists if for any $\langle \alpha(\omega) \rangle$ and $\langle \alpha(\omega') \rangle$ , both in Y, we have $\beta(\omega) = \beta(\omega')$

(2) If Y is defined over $\beta$ , then $X \div Y$ exists iff Y consists of a single tuple.

[Proven in Appendix IV.]

For example, let X be a model of a production faculty in which the input $\alpha$ is a set of production requirements for several products and the output $\beta$ describes the consequences of meeting these requirements - for example, the resulting production cost and the inventory level. If we were to divide the model by a single value of $\beta$ (i.e., a single value of production cost and a single value for the inventory level), then the quotient is the production requirements (i.e., a requirement for each product) that would lead to the specified cost and inventory level. We note that there may be several combinations of production requirements leading to this cost and inventory level, so that the quotient would consist of several tuples.

We may also wish to perform a simple sensitivity analysis by entering a range of values (i.e., upper and lower bound) for $\beta$ and asking for the values of $\alpha$ that would result in values of $\beta$ somewhere in the range. If the divisor were the set of allowable values of $\beta$ , then the quotient would not exist (by Part 2 of Proposition 4). However, a pseudoquotient would consist of the desired values of $\alpha$ . This is the reason for introducing the concept of pseudodivision in relational model management.

Thus, pseudodivision corresponds to a type of sensitivity (or insensitivity) analysis whose purpose is to determine values of attributes that combine the remaining attributes to the set of values specified by the divisor. In the example of Figure 16, if X = A and $Y = \{\langle \beta_{1} \rangle, \langle \beta_{2} \rangle\}$ , then $Q' = \{\langle \alpha_{1} \rangle, \langle \alpha_{2} \rangle, \langle \alpha_{3} \rangle\}$ , and $R' = \{\langle \alpha_{4}, \beta_{3} \rangle, \langle \alpha_{5}, \beta_{4} \rangle\}$ . A similar insensitivity analysis could be performed over a subset of $\beta$ -for example, if $Y = \{\langle \alpha_{1} \rangle, \langle \alpha_{2} \rangle, \langle \alpha_{3} \rangle\}$ , then $q' = \{\langle \beta_{1} \rangle, \langle \beta_{2} \rangle\}$ . A similar analysis obtains if two or more models are joined, with the output of one equal to the input to the other, such that the models are executed in sequence with output-to-input piping. We will call this a model sequence.

Definition 2: A model sequence of length N is a sequence of N models $A_{1}\ldots A_{N}$ such that model $A_{i}$ has input $\alpha^{(i)}$ and output $\alpha^{(i+1)}$ for $i=1\ldots N$ .

Proportion 4': Consider a model sequence of length N, $A_{1}\ldots A_{N}$ , with input/output attributes $\alpha^{(1)}$ , $\alpha^{(2)}\ldots\alpha^{(N+1)}$ , and let $X=\Theta(A_{1},\ldots,A_{N})$ . Then

(1) If Y is defined over $\alpha^{(1)}$ , then $X \div Y$ exists iff for any $\langle \alpha^{(1)}(\omega) \rangle$ and $\langle \alpha^{(1)}(\omega') \rangle$ , both in Y, we have $\alpha^{(2)}(\omega) = \alpha^{(2)}(\omega')$

(2) If Y is defined over $\alpha^{(i)}$ for i > 1, then $X \div Y$ exists iff Y consists of a single tuple.

[The proof is analogous to that of Proposition 4 proven in Appendix IV.]

For example, in Figure 16, N = 2, $A_{1} = A$ , $A_{2} = B$ , $\alpha^{(1)} = \alpha$ , $\alpha^{(2)} = \beta$ , $\alpha^{(3)} = \gamma$ and X = C = $\Theta(A, B)$ . If $Y = \{\langle \gamma_{1} \rangle\}$ , then $q = \{\langle \alpha_{1}, \beta_{1} \rangle, \langle \alpha_{2}, \beta_{1} \rangle, \langle \alpha_{3}, \beta_{2} \rangle$ , and if $Y = \{\langle \beta_{1}, \gamma_{1} \rangle\}$ , then $q = \{\langle \alpha_{1} \rangle, \langle \alpha_{2} \rangle\}$ . But if $Y = \{\langle \beta_{2} \rangle, \langle \beta_{4} \rangle\}$ , then q does not exist. However, in both cases $q'$ exists and represents an interval of insensitivity for the appropriate attributes.

A model sequence is a very simple model base structure. The set of models needed to respond to a user query may bear a more complex relationship to each other – for example, the output of one model may be the input to several other models or vice versa. The set of models may also be cyclic – that is, it may be possible to trace a path through the chain of models that arrives at the starting set of attributes, so that it is necessary to obtain an equilibrium solution for the attributes. We will not examine these more complex structures here.

The relations in Figure 16 are drawn to emphasize the many-to-one relationship between $\alpha$ and $\beta$ , $\beta$ and $\gamma$ and $\alpha$ and $\gamma$ . They can be represented as a set of unnested relations (in first normal form) or as a set of partially-nested or fully-nested relations, as in Figure 17. (Models A and B cannot be partially-nested.) Relational division is less straightforward when the relations are nested. For example, if $X = C$ and $Y = \{\langle \alpha_1 \rangle\}$ , then neither $q$ nor $q'$ exist when $C$ is nested. The algebraic structure of nested relations and the design of languages for processing them are topics of growing interest, because they allow for information types more complex than flat data tables [5,8,12]. Although causal decision models

## UNNESTED MODELS

A = {<α₁, β₁>, <α₂, β₁>, <α₃, β₂>, <α₄, β₃>, <α₅, β₄>}

B = {<β1, γ1>, <β2, γ1>, <β4, γ2>, <β5, γ3>}

$\mathbf{C} = \{\langle \alpha_1, \beta_1, \gamma_1 \rangle, \langle \alpha_2, \beta_1, \gamma_1 \rangle, \alpha_3, \beta_2, \gamma_1 \rangle, \langle \alpha_5, \beta_4, \gamma_2 \rangle\}$

FULLY-NESTED MODELS

A = {<α1, α2}, β1>, <α3, β2>, <α4, β3>, <α5, β4>}

B = {< $\beta_{1}, \beta_{2}$ }, $\gamma_{1}>$ , < $\beta_{4}, \gamma_{2}>$ , < $\beta_{5}, \gamma_{3}>$ }

C = {<<{α₁, α₂}, β₁>, <α₃, β₂>>, γ₁>, <<α₅, β₄>, γ₂>}

PARTIALLY-NESTED MODEL

C = {<<{α₁, α₂}, β₁>, γ₁>, <<α₃, β₂>, γ₁>, <<α₅, β₄>, γ₂>}

Fig. 17. Nesting of model relations.

present a relatively simple information structure, an understanding of their representation and manipulation may be enhanced by viewing them as unnormalized relations, especially when the model banks are less straightforward than model sequences of the type considered here.

## 5. Conclusion

At the beginning of this paper we said that an important purpose of decision support systems is to integrate a variety of information sources. Because of this, an important purpose of the research being done on DSS is to provide a theoretical framework for the integration of a variety of information types, and the framework should be as independent as possible of the way in which the information is stored and processed.

In this and other papers, we have been developing an analytical framework for the organization and processing of decision models and of logic statements based on a relational framework that has been successful in the organization and processing of stored data. We have focused here on one operation, relational division, that has been explored in a limited way by workers in data management, and we have enlarged it to encompass existentially, as well as universally, quantified completion of tuples in partitioned relations. In so doing we have identified two additional areas for research in relational information management, modal logic and nested relations, both of which contribute added complexity to the simple algebraic and logical structures that form the foundation of this paper. It is not yet clear whether this complexity, or that of other possible enhancements for a simple relational framework, will be justified by any added expressive power. Further testing of these ideas may disclose the proper balance between power – especially, the power to describe diverse information structures – and elegance of representation.

## Acknowledgement

This research was supported by the Dean's Fund for Faculty Research of the Owen Graduate School of Management of Vanderbilt University.

## References

[1] R.W. Blanning, A Relational Framework for Assertion Management, Decision Support Systems 1, No. 2 (April 1985) 167–172.

[2] R.W. Blanning, A Relational Theory of Model Management, in: C.W. Holsapple and A.B. Whinston, Eds., Decision Support Systems: Theory and Application, Ch. 2 (Springer-Verlag, Berlin, 1987) 19–53.

[3] J.V. Carlis, HAS: A Relational Algebra Operator, or Divide is Not Enough to Conquer, Proceedings of the IEEE International Conference on Data Engineering (February 1986) 254–261.

[4] M. Dadashzadeh, An Improved Division Operator for Relational Algebra, Information Systems 14, No. 5 (1989) 431–437.

[5] B.C. Desai, P. Goyal and F. Sadri, Non-First Normal Form Universal Relations: An Application to Information Retrieval Systems, Information Systems 12, No. 1 (1987) 49–55.

[6] A.L. Furtado, and L. Kerschberg, An Algebra of Quotient Relations, Proceedings of the ACM-SIGMOD International Conference on Management of Data (August 1977) 1–8.

[7] G. Gardarin, and P. Valduriez, Relational Data Bases and Knowledge Bases Ch. 4 (Addison-Wesley, Reading, MA, 1989) 91–132.

[8] H.F. Korth, Extending the Scope of Relational Languages, IEEE Software 3, No. 1 (January 1986) 19–28.

[9] S.A. Kripke, Semantical Considerations on Modal Logic, in: L. Linsky, Reference and Modality (Oxford University Press, London, 1971) 63–72.

[10] D. Maier, The Theory of Relational Databases, (Computer Science Press, Rockville, 1983).

[11] L. Orman, Design Criteria for Functional Data Bases, Information Systems 10, No. 2 (1985) 207–217.

[12] W.J. Schek, and M.H. Scholl, The Relational Model with Relation-Valued Attributes, Information Systems 11, No. 2 (1986) 137–147.

[13] A. Thayse, (Ed.), From Standard Logic to Logic Programming, Ch. 4 (Wiley, Chichester, 1988) 159–203.

[14] J.D. Ullman, Principles of Database Systems, 2 ed., Section 12.2 (Computer Science Press, Rockville, 1982) 416-424.

## Appendix 1

We prove Proposition I: Let X and Y be dividend and divisor relations with quotient and pseudoquotient Q and Q' and remainder R and R'. Then

1. $\mathbf{Q} \subseteq \mathbf{Q}'$ and $\mathbf{R}' \subseteq \mathbf{R}$

2. $\mathbf{Q} = \mathbf{Q}'$ iff $\mathbf{R} = \mathbf{R}'$

3. $\mathbf{X} \subseteq ((\mathbf{Q}' \times \mathbf{Y}) \cup \mathbf{R}')$

$$
4. \mathrm{Q} ^ {\prime} = \pi (\Theta (\mathrm{X}, \mathrm{Y}), \sigma (\mathrm{X}) \setminus \sigma (\mathrm{Y}))
$$

Proof: #1 follows from the fact that the set of tuples $\langle q, y \rangle$ that complete all of the tuples in Y must be a subset of the tuples $\langle q', y \rangle$ that complete any of the tuples in Y; hence, $Q \subseteq Q'$ . Also, $R'$ is the set of tuples in X which are not completed by any tuple in Y, whereas R includes these tuples along with those that complete some, but not all, of the tuples in Y, hence $R' \subseteq R$ .

#2 follows from the fact that the set of all $\{q\}$ will equal the set of all $\{q'\}$ if and only if there is no $q'$ and $\langle y_{1}\rangle$ , $\langle y_{2}\rangle \in Y$ such that $\langle q', y_{1} \rangle \in X$ but $\langle q', y_{2} \rangle \notin X$ . But these are also the conditions under which the set of all $\langle r \rangle$ will equal the set of all $\langle r' \rangle$ .

\# 3: $\Theta(X, Y)$ consists of all tuples in $X$ for which there is at least one $\sigma(Y)$ -segment in $Y$ ; therefore, its projection along $\sigma(X) \setminus \sigma(Y)$ consists of those tuples in $Q'$ .

## Appendix II

We prove Proposition 2: Let X, Y, and Z be a-relations with intensions x, y, and z. Then 1. $Z = \Theta(X, Y)$ iff $z = x \wedge y$

2. If $\sigma(\mathbf{Y}) \subseteq \sigma(\mathbf{X})$ and $\mathbf{Y} = \pi(\mathbf{X}, \sigma(\mathbf{Y}))$ , then $\mathbf{x} \to \mathbf{y}$

3. If $\sigma(X) = \sigma(Y)$ , then $x \to y$ iff $X \subseteq Y$ . Proof: #1: This is proven in [1].

#2. If $\sigma(Y) \subseteq \sigma(X)$ , then $\pi(X, \sigma(Y))$ consists of those tuples with their $\sigma(Y)$ -segment in $X$ . Therefore, the intension of any of these tuples is valid only if there is a valid corresponding X-tuple; hence, $x \to y$ .

#3. The collection of tuples of X and Y represent x and y in a primitive disjunctive form (similar to disjunctive normal form). If $\sigma(\mathrm{X}) = \sigma(\mathrm{Y})$ , then $X \subseteq Y$ if and only if any conjunctive expression in the disjunctive form of X is also contained in the disjunctive form of Y, which in turn is true if and only if $x \to y$ .

## Appendix III

We prove Proposition 3: Let X and Y be dividend and divisor a-relations with quotient Q, psuedoquotient Q', remainder R and pseudore-mainder R', and let the corresponding intensions be x, y, q, q', r, and r'. Then

1. $\mathbf{q}\rightarrow \mathbf{q}'$ and $\mathbf{r}^{\prime}\rightarrow \mathbf{r}$

2. $\mathbf{x} \equiv ((\mathbf{q} \wedge \mathbf{y}) \vee \mathbf{r})$

3. $\mathbf{x}\rightarrow ((\mathbf{q}'\wedge \mathbf{y})\vee \mathbf{r}')$

4. $(\mathbf{x}\wedge \mathbf{y})\to \mathbf{q}'$

Proof: #1 follows from #1 of Proposition 1 and #3 of Proposition 2.

#2 follows from the relationship $((Q \times Y) \cup R) = X$ , along with #1 of Proposition 2 and the fact that the union of two union-compatible relations is the disjunction of their intensions.

#3 follows from #2 of Proposition 2 and #3 of Proposition 1.

#4: The intension of $\Theta(X, Y)$ is $x \wedge y$ (from #3 Proposition 2), and $Q'$ is the projection of this along a subset of $\sigma(X)$ (#4 of Proposition 1). Therefore, from #2 of Proposition 2 the intension of $\Theta(X, Y)$ implies the intension of $Q'$ - that is, $x \wedge y \to q'$ .

## Appendix IV

We prove Proposition 4: Consider a model $X = \{\langle \alpha(\omega), \beta(\omega) \rangle | \omega \in \Omega\}$ such that for any $\omega \neq \omega'$ , we have $\alpha(\omega) \neq \alpha(\omega')$ . Then

(1) If Y is defined over $\alpha$ , then $X \div Y$ exists if for any $\langle \alpha(\omega) \rangle$ and $\langle \alpha(\omega') \rangle$ , both in Y, we have $\beta(\omega) = \beta(\omega')$

(2) If Y is defined over $\beta$ , then $X \div Y$ exists iff Y consists of a single tuple.

Proof: #1 follows from the fact that if there is a single $\beta$ corresponding to each $\alpha$ in Y, then $Q = \{(\langle \beta \rangle\}$ and hence, Q exists.

#2. If Y contains two distinct tuples $\langle y_{1}\rangle$ and $\langle y_{2}\rangle$ , then there can be no $\alpha$ such that $\langle\alpha, y_{1}\rangle$ , $\langle\alpha, y_{2}\rangle \in X$ and hence, Q = NULL.
