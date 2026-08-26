---
otero_id: 16843
otero_key: "USECQB2N"
title: "A relational framework for assertion management"
authors: "Robert W. Blanning"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90065-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Relational Framework for Assertion Management

Robert W. BLANNING

Owen Graduate School of Management, Vanderbilt University, Nashville, TN 37203, USA

An important purpose of research on decision support systems is to develop a theory of information management that is as independent as possible of the way in which the information is stored and processed. One framework that has proven useful in this regard is a relational framework, which has been successfully applied to the organization and processing of data files and decision models. In this paper we examine the application of relational theory to the management of assertions – that is, to the organization and processing of statements that may be true or false.

Keywords: First order logic; Virtual relation; Relational projection; Relational join; Lossy join; Clausal form; Query language; Table skeleton; Data management; Model management; Assertion management; Information management; Expert system.

![](/api/attachments/USECQB2N/fulltext/images/ec7a52f199cae41ca39af6313ff901ddf825c4d290605ace7e6afabed7c47a7d.jpg)

Robert W. Blanning is Associate Professor of Management at the Owen Graduate School of Management at Vanderbilt University. He holds a B.S. in Physics from the Pennsylvania State University, an M.S. in Operations Research from the Case Institute of Technology, and a Ph.D. from the University of Pennsylvania, specializing in Operations Research and Management Information Systems. His research and teaching interests are in information economics, model mana-

gement systems, and the management applications of artificial intelligence, and he has published extensively on these topics.

## 1. Introduction

Much of the pioneering work on DSS [23,24,1,22,18] pointed out the need to provide convenient user access to a variety of information sources so that a user can easily assemble the appropriate information to respond to a particular decision problem. These sources include stored data, decision models, logic statements (that can be true or false), and possibly more complex types of information, such as those found in expert systems and other software systems based on artificial intelligence (AI) techniques. The pioneering literature also suggested that user access may be facilitated by the construction of simple but powerful interfaces to the information sources and by the development of theoretical frameworks for viewing the growing spectrum of available information.

An important theoretical framework, which was being developed by computer scientists about the time the interest in DSS technology began, is that of relational database theory [27,29]. By viewing stored data as a system of relations, computer scientists were able to pose and answer interesting questions about database organization and the requirements for completeness of database query languages. The theoretical and practical successes of database management systems has given rise to a growing literature on model management [34,32,31,25]. The purpose of a model management system is to insulate its users from the physical operations of model bank organization and processing, just as a database management system insulates its users from the physical operations of database organization and processing. One component of the model management literature is relational in character: 'a model is viewed as a virtual relation with input and output attributes, just as a data file is viewed as a stored relation with key and content attributes [12,10,8]. The many similarities between the relational views of data and of models [11,13,14] suggests that it may be possible to develop a unified relational theory of information management in DSS, a view which is taken in this paper.

Another area of growing importance in DSS – one that is also relevant to the purpose of this paper – is the incorporation of AI methodology and techniques in DSS [19,20,30]. There are two areas in which AI appears to be most relevant to DSS. The first is natural language processing to facilitate user across to databases [33] and decision models [6,3]. The second is the development of expert (or knowledge-based) systems to assist managers in decision making [2,4,5]. Thus, it is likely that DSS research increasingly will emphasize the integration of stored data, decision models, and AI-based knowledge [15].

This paper attempts to contribute to such an integration by presenting a relational framework for the management of an important type of information found in many AI-based systems - logic (true/false) statements. These will be called assertions. An assertion is represented either by a predicate symbol $(\mathbf{x},\mathbf{y},\mathbf{z}\ldots)$ or by a well-formed expression consisting of predicate symbols and logical operators - for example, $\mathbf{x}\to \mathbf{y}$ , $(\mathbf{x}\wedge \mathbf{y})\vee \mathbf{z}$ , etc. [28]. It may be represented intensively, as above, or extensively in the form of a truth table. We will view an assertion as a virtual relation (i.e., a virtual truth table) that can be processed by means of relational operators (specifically, projection and join). Thus, we extend relational database theory and relational model management theory to encompass assertion management.

We begin in Section 2 by defining certain relational operations in the context of assertion management. We shall see that extensional projection corresponds to intensional implication and that extensional join corresponds to intensional conjunction. In Section 3 we address the organization of relational assertion banks; we examine the circumstances under which a relation and its projections possesses the lossy join property and thus, will determine how to organize an assertion bank so as to avoid lossy joins. Finally, we present the design of a simple tabular query language, similar to Query by Example, for constructing and processing relational assertion banks.

## 2. The Processing of Relational Assertion Banks

We begin by defining an a-relation (assertion-relation) scheme, S, as a set of attributes $\{x, y, z\ldots\}$ each of whose domains is $\{0, 1\}$ (representing false and true). An a-relation, R, defined on a scheme S is a subset of the Cartesian product of the domains of S; thus, if S contains N elements, then an a-relation on S is a .subset of $\{0, 1\}^{N}$ . We define the following four relational operations:

1. Intension. Let R be an a-relation on S. Then I(R), the intension of R, is a predicate formula whose truth table is R. More exactly, R is a modified truth table containing only the rows for which the predicate formula is true and less the column giving the value, 1 or 0, of the predicate formula. For example, if S = {x, y} and R = {⟨1, 1⟩, ⟨1, 0⟩, ⟨0, 1⟩}, then I(R) = (x v y). We note that an intension is not unique in form; we could have written I(R) = ( $\overline{x} \wedge \overline{y}$ ) or I(R) = ( $\overline{x} \rightarrow y$ ). However, we are interested only in equivalence classes of intensions. Thus, R = R' if and only if I(R) ≡ I(R').

2. Extension. If J is a predicate formula defined on S, then E(J) is an a-relation on S consisting of all tuples for which $J \equiv 1$ . In other words, E(J) is the truth table for J (less the rows for which J = 0 and less the column containing the value of J). For example, if $J = (x \wedge y)$ , then $E(J) = \{\langle 1, 1 \rangle\}$ . The intension and extension operators bear the following relationships to each other: $E(I(R)) = R$ and $I(E(J)) \equiv J$ .

3. Projection. Let R be an a-relation on S, and let $S' \subseteq S$ . Then $P(R, S')$ is the projection of R along $S'$ . That is, $P(R, S')$ is an a-relation on $S'$ formed by deleting from R all columns corresponding to $S \cap \overline{S}'$ and eliminating duplicate tuples. We note that $P(R, S) = R$ .

3. Join. Let R and R' be relations on the schemes S and S'. Then J(R, R') is the natural join of R and R'. That is, J(R, R') is an a-relation on S ∪ S' consisting of those tuples in R and R' for which the S ∩ S' components are identical. If S ∩ S' = 0, then J(R, R') is the Cartesian product of the tuples in R and R'. Since the join operation is associative, we can write J(R, R', R'', ...).

We now demonstrate that the operations of projection and join correspond to the logical operations of inference and conjunction. We begin with the join operation. At the top of Figure 1 are shown the extensions of $x \rightarrow y$ and $y \rightarrow z$ . The join of these two a-relations, shown in the middle of Figure 1, is the truth table for the predicate formula $(\mathbf{x}\to \mathbf{y})\wedge (\mathbf{y}\rightarrow \mathbf{z})$ . That extensional join always corresponds to intensional conjunction is proven in

<table><tr><td>x → y</td><td>x</td><td>y</td><td>y → z</td><td>y</td><td>z</td></tr><tr><td></td><td>1</td><td>1</td><td></td><td>1</td><td>1</td></tr><tr><td></td><td>0</td><td>1</td><td></td><td>0</td><td>1</td></tr><tr><td></td><td>0</td><td>0</td><td></td><td>0</td><td>0</td></tr><tr><td>JOIN</td><td>x</td><td>y</td><td>z</td><td></td><td></td></tr><tr><td></td><td>1</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td></td><td>0</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>1</td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td></tr><tr><td colspan="3">PROJECTION</td><td>x</td><td>z</td><td></td></tr><tr><td></td><td></td><td></td><td>1</td><td>1</td><td></td></tr><tr><td></td><td></td><td></td><td>0</td><td>1</td><td></td></tr><tr><td></td><td></td><td></td><td>0</td><td>0</td><td></td></tr></table>

Figure 1. Projection and Join

THEOREM I: Let R and R' be two a-relations. Then J(R, R') = E(I(R) ∧ I(R')). (See Appendix 1.)

The projection of an a-relation along a subset of its attributes produces another a-relation whose intension is implied by the intension of the former relation and which implies any other intension implied by the former relation. For example, in Figure 1 the projection of the extension of $(\mathbf{x} \to \mathbf{y}) \wedge (\mathbf{y} \to \mathbf{z})$ along $\mathbf{x}$ and $\mathbf{z}$ is the extension of $\mathbf{x} \to \mathbf{z}$ , which clearly is implied by $(\mathbf{x} \to \mathbf{y}) \wedge (\mathbf{y} \to \mathbf{z})$ . Furthermore, any other predicate formula implied by $(\mathbf{x} \to \mathbf{y}) \wedge (\mathbf{y} \to \mathbf{z})$ (e.g., 1, whose extension on $\{\mathbf{x}, \mathbf{z}\}$ is $\{0, 1\}^2$ ) is also implied by the projection. That this is true in general is proven in

THEOREM II: Let R and R' be a-relations on S and S' such that S' ⊆ S and R' = P(R, S'). Then I(R) → I(R'). Furthermore, if J is a predicate formula on S' such that I(R) → J, then I(P(R, S')) → J. (See Appendix 2.)

## 3. Lossy and Lossless Joins

Although the relational view of assertions is analogous in some respects to the relational views of data and models, the concepts of key, functional dependency, update anomaly, and normal form are not of importance in relational assertion management. The reason is that a-relations are not time varying -- that is, individual tuples in an a-relation are not updated over time. Thus, anomalies resulting from attempts to update relations with inappropriate groupings of functional dependencies cannot arise, because updating is never performed. We also note that implication is not a functional dependency (i.e., $x \to y$ does not mean that $y$ is functionally dependent on $x$ ).

However, there is one organizational concept in relational database theory that also arises in relational assertion management, the possible existence of lossy joins. A relation and a set of its projections are said to possess the lossy join property if joining the projections does not recover the original relation. Otherwise, the relation and its projections are said to possess the lossless join property. For example, if the extension of $(x \rightarrow y) \land (y \rightarrow z)$ , illustrated in the middle of Figure 1, is projected into the conjunctive expressions $x \rightarrow y$ and $y \rightarrow z$ , illustrated at the top of Figure 1, then the lossless join property obtains, for the join of these two projections is the original relation. On the other hand, if the projections are not conjunctive components of the original relation, then the lossy join property will obtain. For example, in Figure 2 the extension of $(x \rightarrow y) \land (y \rightarrow z)$ is projected along the domains $\{x, y\}$ and $\{x, z\}$ . The join of these two projections, which appears at the bottom of Figure 2, differs from the original relation. (It is the extension of $x \rightarrow (y \land z)$ .) That the lossless join property obtains if and only if the projections are a complete set of conjunctive components of the original relation is proven in

<table><tr><td colspan="2">(x → y) ∧ (y → z)</td><td>x</td><td>y</td><td>z</td></tr><tr><td rowspan="4" colspan="2"></td><td>1</td><td>1</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td colspan="2">PROJECTION</td><td>x</td><td>y</td><td>PROJECTION</td></tr><tr><td rowspan="3" colspan="2"></td><td>1</td><td>1</td><td>1</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>JOIN</td><td>x</td><td>y</td><td>z</td><td></td></tr><tr><td rowspan="5"></td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>0</td><td>1</td><td>1</td><td></td></tr><tr><td>0</td><td>1</td><td>0</td><td></td></tr><tr><td>0</td><td>0</td><td>1</td><td></td></tr><tr><td>0</td><td>0</td><td>0</td><td></td></tr></table>

Figure 2. Lossy Join

THEOREM III: Let $R_{0}$ , $R_{1}$ , $R_{2}\ldots R_{N}$ be $N+1$ a-relations on $S_{0}$ , $S_{1}$ , $S_{2}\ldots S_{N}$ such that $S_{i}\subseteq S_{0}$ and $\mathbf{R}_{i}=\mathbf{P}(\mathbf{R}_{0},\mathbf{S}_{i})$ for $i=1\ldots N$ . Then $\mathbf{J}(\mathbf{R}_{1},\mathbf{R}_{2}\ldots\mathbf{R}_{N})=\mathbf{R}_{0}$ iff $\mathbf{I}(\mathbf{R}_{0})\equiv\mathbf{I}(\mathbf{R}_{1})\wedge\ldots\wedge\mathbf{I}(\mathbf{R}_{N})$ . (See Appendix III.)

## 4. AQL: A Language for Relational Assertion Management

We have seen that an assertion bank may be viewed as a conjunction of separate assertions and that inferences may be obtained by projection along appropriate attributes. We now present the design (but not yet the implementation) of a tabular query language -- similar to Query-by-Example [35] and to a similar tabular language proposed for model management [7] -- for organizing and processing assertion banks whose conjunctive components are in clausal form. An assertion is in clausal form if it is of the form $(\mathbf{x}_1 \wedge \mathbf{x}_2 \wedge \ldots \wedge \mathbf{x}_N) \to (\mathbf{y}_1 \vee \mathbf{y}_2 \vee \ldots \vee \mathbf{y}_M)$ . It can be shown that any assertion can be rendered into clausal form [26] -- that is, it can be expressed as one or more clauses. Several examples of expressions rendered into clausal form appear in Table 1. The advantage of the clausal form is not only its simplicity, but also that many of the knowledge bases found in expert systems are in clausal form [21], and logic programming languages, such as PROLOG, easily handle clausal (or more exactly, Horn clause) expressions [16,17].

Table 1. Clausal Forms

<table><tr><td>Assertion</td><td>Clausal Form</td></tr><tr><td>x</td><td>1 → x</td></tr><tr><td> $\bar{x}$ </td><td>x → 0</td></tr><tr><td>x ∧ y</td><td>1 → x</td></tr><tr><td></td><td>1 → y</td></tr><tr><td>x ∨ y</td><td>1 → x ∨ y</td></tr><tr><td>(x ∧ y) ∨ z</td><td>1 → x ∨ z</td></tr><tr><td></td><td>1 → y ∨ z</td></tr><tr><td>(x ∨ y) ∧ z</td><td>1 → x ∨ y</td></tr><tr><td></td><td>1 → z</td></tr><tr><td> $\bar{x} \rightarrow y$ </td><td>1 → x ∨ y</td></tr><tr><td>x →  $\bar{y}$ </td><td>x ∧ y → 0</td></tr><tr><td>x ≡ y</td><td>x → y</td></tr><tr><td></td><td>y → x</td></tr><tr><td>(x ∨ y) → (z ∧ w)</td><td>x → z</td></tr><tr><td></td><td>x → w</td></tr><tr><td></td><td>y → z</td></tr><tr><td></td><td>y → w</td></tr></table>

AQL (Assertion Query Language) allows a user (1) to construct an assertion bank by joining clausal expressions and (2) to request inferences by projecting along appropriate attributes. Clauses are entered or displayed in a table skeleton by entering arrows under the appropriate attribute names: “→” for a conjunctive component of an antecedent and “←” for a disjunctive component of a consequent. Projection is accomplished by entering “P” under the appropriate attribute names.

Consider the example in Figure 3. Let

PCH = product cost is high

$$
\mathrm{PQL} = \text { product   quality   is   low }
$$

RMH = raw material cost is high

PMM = production facilities are being mismanaged

ESS = production equipment is substandard

PL = profits will be low

We assume four relationships between these variables. First, if raw material cost is high or if facilities are being mismanaged and equipment is substandard, then product cost will be high. This is represented by the clauses

I. RMH → PCH

II. PMM ∧ ESS → PCH

Second, product quality is low if and only if facilities are mismanaged:

III. PMM → PQL

IV. PQL → PMM

Third, if both product quality is low and product cost is high, then profit will be low:

V. PCH ∧ PQL → PL

Fourth, equipment is substandard:

VI. 1 → ESS

These six clauses make up the assertion bank in Figure 3. The user wishes to know the relationship between mismanagement and low profit. This is accomplished by requesting a projection along PMM and PL. The result, that mismanagement will lead to low profit (PMM → PL) appears at the bottom of Figure 3. We note that if Assertion VI were missing, then the system would give a null response, for there would be no relationship between PMM and PL. That is, for any combination of truth values for PMM and PL, there would be at least one set of values for the other variables such that the remaining five assertions are satisfied.

<table><tr><td colspan="2"></td><td>1</td><td>0</td><td>PCH</td><td>PQL</td><td>RMH</td><td>PMM</td><td>ESS</td><td>PL</td></tr><tr><td rowspan="6">ASSETS EARNTKION</td><td>I</td><td></td><td></td><td>←</td><td></td><td>→</td><td></td><td></td><td></td></tr><tr><td>II</td><td></td><td></td><td>←</td><td></td><td></td><td>→</td><td>→</td><td></td></tr><tr><td>III</td><td></td><td></td><td></td><td>←</td><td></td><td>→</td><td></td><td></td></tr><tr><td>IV</td><td></td><td></td><td></td><td>→</td><td></td><td>←</td><td></td><td></td></tr><tr><td>V</td><td></td><td></td><td>→</td><td>→</td><td></td><td></td><td></td><td>←</td></tr><tr><td>IV</td><td>→</td><td></td><td></td><td></td><td></td><td></td><td>←</td><td></td></tr><tr><td colspan="2">USERQUERY</td><td></td><td></td><td></td><td></td><td></td><td>P</td><td></td><td>P</td></tr><tr><td colspan="2">SYSTEMRESPONSE</td><td></td><td></td><td></td><td></td><td></td><td>→</td><td></td><td>←</td></tr></table>

Figure 3. Example of AQL

## Conclusion

The purpose of this effort is not merely to develop a theory of assertion management, but also to present a framework for assertion management similar to the existing analytical frameworks for data and model management. One advantage of developing a common framework for the management of data, models, and assertions is that it may be possible to combine (and possibly to enlarge) them to produce a framework for the organization and processing of knowledge bases in expert systems for management (ESMs). A growing number of ESMs have been developed for resource allocation (e.g., portfolio management), problem diagnosis (e.g., in auditing), and scheduling and assignment (e.g., of personnel), and it appears that there will be many more fruitful applications of ESMs $[2,4,5]$ . Most ESMs are rule-based systems, although some also make use of decision models and stored data. In addition, it has been shown that the operation of sensitivity analysis, which is prominent in model management, can also be applied to certain rule-based ESMs $[9]$ . Thus, it may be possible to develop a unified framework for the management of data, models, assertions, and knowledge in DSS.

## Appendix 1

We prove Theorem I: Let R and R' be two a-relations. Then $\mathbf{J}(\mathbf{R},\mathbf{R}')=\mathbf{E}(\mathbf{I}(\mathbf{R})\wedge\mathbf{I}(\mathbf{R}'))$ .

Proof: Let S and S' be the schemes for R and R'. We define three attribute sets: $S_{1}=S\cap\bar{S}'$ , $S_{2}=S\cap S'$ , and $S_{3}=\bar{S}\cap S'$ . Thus, $S=S_{1}\cup S_{2}$ and $S'=S_{2}\cup S_{3}$ . If $S_{2}\neq\emptyset$ , then the extension of $I(R)\wedge I(R')$ will consist of all combinations of tuples on $S\cup S'$ whose $\{S_{1},S_{2}\}$ component is in R and whose $\{S_{2},S_{3}\}$ component is in R'. However, these tuples are those found in the natural join of R and R'. If $S_{2}=\emptyset$ , then the extension of $I(R)\wedge I(R')$ is the Cartesian product of the tuples in R and R', which is also the natural join of R and R'. Therefore, $J(R,R')=E(I(R)\wedge I(R'))$ .

## Appendix 2

We prove Theorem II: Let R and $R'$ be a-relations on S and $S'$ such that $S' \subseteq S$ and $R' = P(R, S')$ . Then $I(R) \to I(R')$ . Furthermore, if J is a predicate formula on $S'$ such that $I(R) \to J$ , then $I(P(R, S')) \to J$ .

Proof: Since $\mathbf{R}' = \mathbf{P}(\mathbf{R}, \mathbf{S})$ , the $S'$ component of any tuple in R is in $R'$ . Thus, $\mathbf{I}(\mathbf{R}) \to \mathbf{I}(\mathbf{R}')$ . In addition, if J is an intension of a relation defined on $S'$ such that $\mathbf{I}(\mathbf{R}) \to \mathbf{J}$ , then $\mathbf{P}(\mathbf{R}, \mathbf{S}')$ is a subset of $\mathbf{E}(\mathbf{J})$ . Thus, $\mathbf{I}(\mathbf{P}(\mathbf{R}, \mathbf{S}')) \to \mathbf{J}$ .

## Appendix 3

We prove Theorem III: Let $R_{0}$ , $R_{1}$ , $R_{2}\ldots R_{N}$ be $N+1$ a-relations on $S_{0}$ , $S_{1}$ , $S_{2}\ldots S_{N}$ such that

$S_{i} \subseteq S_{0}$ and $R_{i} = P(R_{0}, S_{i})$ for $i = 1 \ldots N$ . Then $J(R_{1}, R_{2} \ldots R_{N}) = R_{0}$ iff $I(R_{0}) \equiv I(R_{1}) \wedge I(R_{2}) \wedge \ldots \wedge I(R_{N})$ .

Proof: This follows directly from Theorem I, where the projections $R_{0}$ and $R_{i}$ correspond to R and $R'$ and the associative property of join and conjunction are invoked.

## Acknowledgement

This work was supported by the Dean's Fund for Faculty Research of the Owen Graduate School of Management of Vanderbilt University.

## References

[1] S.L. Alter, Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, Reading (1980):

[2] R.W. Blanning, “Knowledge Acquisition and System Validation in Expert Systems for Management,” Human Systems Management (Autumn 1984) 280–285.

[3] R.W. Blanning, "MERLIN: System and User Manual," Working Paper 84-132, Owen Graduate School of Management, Vanderbilt University (1984).

[4] R.W. Blanning, "Issues in the Design of Expert Systems for Management," Proceedings of the National Computer Conference (July 1984) 489-495.

[5] R.W. Blanning, "Expert Systems for Management: Possible Application Areas," DSS-84 Transactions (April 1984) 69-77.

[6] R.W. Blanning, "Conversing with Management Information Systems in Natural Language," Communications of the ACM, 27 (March 1984) 201-207.

[7] R.W. Blanning, "TQL: A Model Query Language Based on the Domain Relational Calculus," Proceedings of the IEEE Workshop on Languages for Automation (November 1983) 141-146.

[8] R.W. Blanning, "Issues in the Design of Relational Model Management Systems," Proceedings of the National Computer Conference (June 1983) 395-401.

[9] R.W. Blanning, "Sensitivity Analysis in Expert Systems for Management," Owen Graduate School of Management, Vanderbilt University, Nashville (1983).

[10] R.W. Blanning, "A Relational Framework for Model Management in Decision Support Systems," DSS-82 Transactions (June 1982) 16-22.

[11] R.W. Blanning, "Data Management and Model Management: A Relational Synthesis," Proceedings of the 20th Annual Southeast ACM Regional Conference (April 1982) 139-147.

[12] R.W. Blanning, "Model Structure and User Interface in Decision Support Systems," DSS-81 Transactions (June 1981) 1-7.

[13] R.W. Blanning, "Model-based and Data-based Planning Systems," Omega, 9 (February 1981) 163-168.

[14] R.W. Blanning, "The Functions of a Decision Support System," Information & Management, 2 (September 1979) 87-93.

[15] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York (1981).

[16] K.L. Clark and S.-A. Tarnlund, Logic Programming, Academic Press, London (1982).

[17] W.F. Clocksin and C.S. Mellish, Programming in Prolog, Springer-Verlag, Berlin (1981).

[18] G. Fiek and R.H. Sprague, (eds.), Decision Support Systems: Issues and Challenges, Pergamon, Oxford, 1980.

[19] M.S. Fox, “The Intelligent Management System: An Overview,” in: Processes and Tools for Decision Support, ed. by H.G. Sol, North-Holland, Amsterdam (1983) 105-103.

[20] G.A. Gorry and R. Krumland, "Artificial Intelligence Research and Decision Support Systems," in: Building Decision Support Systems, ed. by J.L. Bennett, Addison-Wesley (1983) 205-219.

[21] F. Hayes-Roth, D.A. Waterman and D.B. Lenat, Building Expert Systems, Addison-Wesley, Reading (1983).

[22] W.C. House (ed.), Decision Support Systems: A Data-Based, Model-Oriented, User-Developed Discipline, Petrocelli, New York (1983).

[23] P.G.W. Keen and M.S.S. Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading (1978).

[24] P.G. Keen and G.R. Wagner, "DSS: An Executive Mind-Support System," Datamation, 25 (November 1979) 117-122.

[25] B. Konsynski, "Model Management in Decision Support Systems," in: Data Base Management: Theory and Applications, ed. by C.W. Holsapple and A.B. Whinston, D. Reidel, Dordrecht (1983).

[26] R. Kowalski, Logic for Problem Solving, North Holland, New York (1979).

[27] D. Maier, The Theory of Relational Databases, Computer Science Press, Rockville (1983).

[28] A. Margaris, First Order Mathematical Logic, Blaisdell, Waltham (1967).

[29] T.H. Merrett, Relational Information Systems, Reston Publishing Company, Reston, 1984.

[30] W. Reitman, "Applying Artificial Intelligence to Decision Support: Where do Good Alternatives Come From?" in: Decision Support Systems, ed. by M.J. Ginsberg, W. Reitman, and E.A. Stohr, North-Holland, Amsterdam (1982) 155-174.

[31] R.H. Sprague, Jr. and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs (1982).

[32] R.H. Sprague and H.J. Watson, "Model Management in MIS," Proceedings of the 7th National AIDS (November 1975) 213-215.

[33] H. Tennant, Natural Lanaguage Processing, Petrocelli, New York, 1981.

[34] H.J. Will, "Model Management Systems," in: Information Systems and Organization Structure, ed. by E. Grochla and N. Szyperski, Walter de Gruyter, Berlin (1975).

[35] M.M. Zloof, "Query by Example," Proceedings of the National Computer Conference (June 1975), 431-438.
