---
otero_id: 17180
otero_key: "H4XN56VP"
title: "Characterization of unknown values with implicit predicate"
authors: "Jae Dong Yang; Yoon Joon Lee"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90052-d"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Characterization of unknown values with implicit predicate

Jae Dong Yang and Yoon Joon Lee
Department of Computer Science, Korea Advanced Institute of Science and Technology, CheongRyang, Seoul, Korea

In general, null values are interpreted as unknown value or inapplicable value. This paper proposes a new approach for solving the unknown value problems with Implicit Predicate (IP). The IP serves as a descriptor corresponding to a set of the unknown values, thereby expressing the semantics of them. In this paper, we demonstrate that the IP is capable of (1) enhancing the semantic expressiveness of the unknown values, (2) entering incomplete information into database and (3) exploiting the information and a variety of inference rules in database to reduce the uncertainties of the unknown values.

Keywords: Unknown value, Evolution, Inference rule.

![](/api/attachments/H4XN56VP/fulltext/images/b351a4f179d7a9a62b1679eaaccbdd18cc8d22b1c3185e5dcd9da49586b675ce.jpg)  
terests include deductive database and fuzzy logic.

Jae Dong Yang was born at Kwangju in Korea. He received the B.E. degree in computer science from Seoul National University, and M.S. degree in computer science from KAIST (Korea Advanced Institute of Science and Technology) in 1985. He is currently a candidate for the Ph.D degree in computer science at KAIST. He is also an assistent professor in Chonbuk National University. He has lectured on database, automated reasoning, and artificial intelligence. His research in

![](/api/attachments/H4XN56VP/fulltext/images/fe49ce9a1390046952575c70754a418a5a806e66f2e2c002b17965c808dea009.jpg)

Yoon Joon Lee was born at Seoul in Korea. He received the B.S. degree in statistics and computer science from Seoul National University, M.S. degree in computer science from KAIST and Ph.D degree in computer science from France, INPG-ENSIMAG in 1983. During 1983–1984, he worked on IMAG laboratory. He is currently an associate professor in KAIST. His research includes deductive database and data model.

## 1. Introduction

The values with abnormal meanings are often encountered in various Database(DB) applications such as police force, medical science and knowledge based systems. Such values, called as null values in database context, are known to have 14 different meanings according to ANSI [1]. Among 14 meanings, the simplest one “nothing is known” is accepted in most current Database Management Systems (DBMS). However, most of 14 meanings should be supported to strengthen the semantic expressiveness of the DBMSs.

Null values can be classified into two categories: unknown values and inapplicable values. Concerning the unknown value problems attempts have been made since pilot papers $[5,6]$ addressed the issues in the relational framework.

Vassiliou [23] proposed an extension of the Functional Dependency (FD) interpretation to handle the unknown values and presented a complete axiomatization of inference rules for extending FDs. Imielinski [11] studied conditions for a semantically meaningful extension of the usual relational operators and their expressions from operators on relations to operators on tables with the unknown values.

Some approaches to treating incomplete information have been developed based on partial information concept $[14,15,19]$ . However, their semantic expressiveness leaves room for improvement because of a limitation that the unknown values occurring in an attribute must be represented as a simple subset of its domain. For example, they can only express the limited meanings such as “blood type of a person is one of A and B”, or “range of his age is from 28 to 30”.

The other researchers $[2,12]$ have paid attentions to capturing the subtle semantics of the unknown values to a large extent by introducing an alternative world concept. This approach, however, requires special data types such as set null, marked null and possible tuples, which change the relational framework considerably. Moreover, these approaches fail to notice that deduction procedure from knowledges can serve in reducing uncertainties.

According to current trends, the deduction procedure has significant meanings. Therefore, several recent literatures have been attacking the unknown value problems in deductive database application environments $[10,20,21,24]$ . Based on the proof theoretic view or the model theoretic view, they have tried to formalize the unknown value problems in three directions. First, indefinite answer to queries and query evaluation algorithms were sketched in DB containing indefinite information according to the CWA or the ECWA $[21,25]$ . Next, update problems were argued, which indirectly spawn incomplete information $[24]$ . Finally, the exploitation of inference rules was discussed to prevent the inconsistencies which the incompleteness may lead to $[10]$ . More specifically, inference rules including view definitions were exploited through query transformation in $[10]$ . By imposing restriction that incomplete knowledge can be introduced in DB only when view definitions are updated, the literature also succeeded in preserving relational DB properties. However, it is due to this restriction that partial information can't be given by user at all and the semantic expressiveness of the unknown values is far from being satisfactory.

As another alternatives tackling the unknown value problems in the logic paradigm, researches employing function symbols have been performed to strengthen the semantic expressiveness $[10,18]$ . Functions were defined as the semantic descriptor of the unknown values. However, they destroy the relational DB properties, which results in making the available relational theories useless.

This paper proposes a new approach for solving the unknown value problems identified so far with Implicit Predicate (IP). By defining the IP as a descriptor corresponding to a set of unknown values, we make the IP serve to express their semantics. For example, let tuple t be R(k, ω) with an unknown value ω known to be a or b but not both in a relation R where k is a key. Then it may be rewritten as (∀X)(R(k, X) ← IP(k, X)) ∧ (IP(k, X) ← X = a ∨ X = b)), the meaning of which is equivalent to R(k, a) ∨ R(k, b).

We demonstrate that the IP is capable of (1) enhancing the semantic expressiveness of the unknown values, (2) entering incomplete information into DB and (3) exploiting the information and a variety of inference rules in DB to reduce the uncertainties of the unknown values.

In chapter 2, we define formally the concepts related to the IP and its evolution procedures are described abstractly in chapter 3 by exploiting two data dependencies as the examples of the inference rules. Finally, the conclusion is presented in chapter 4.

## 2. Formal Concepts

As Keller mentioned [12], inapplicable null values do not fit well into a logical framework. Furthermore, if necessary, they can be removed through appropriate decompositions of relational schemes. Accordingly, we shall only consider the unknown null values from now on.

For the definitions formalizing IP framework, we begin by stating a few conventions and two basic assumptions, DB and DB world assumption adopted throughout this paper.

## 2.1. Conventions

In this section, we describe some conventions adopted for notational convenience.

(1) Constant: denoted as lower-case letter sequences. It represents an element in the domain of an attribute except null values.

(2) Variable: denoted as upper-case letter sequences.

(3) Attribute variable: denoted as $A_{1}, A_{2}, \ldots$ , or attribute name. These are special variables in that they denote the attributes of a relation.

(4) Quantifiers: If X is a variable, then $(\forall X)$ is a universal quantifier and $(\exists X)$ is an existential quantifier.

(5) Determinant: denoted as upper-case letter with subscript. Determinant K is a set of attribute variables $\{A_{1}, A_{2}, \ldots, A_{k}\}$ , or $A_{1}A_{2}\ldots A_{k}$ , on which some other attributes are fully functionally dependent.

(6) Constant determinant: denoted as lower-case letter with subscript. It is a set of constants $\{a_1, a_2, \ldots, a_k\}$ , or $a_1a_2 \ldots a_k$ instantiating determinant $A_1A_2, \ldots A_k$ simultaneously.

(7) Predicate: denoted as upper-case letter sequences. Any predicate can take n arguments, which is called n-place predicate. To differentiate variables from these predicates, we exclude the predicates with no arguments.

(8) Relation predicate: n-place relation predicate R is a special n-place predicate in that it represents the intension of a relation r having n attributes such as EMP(NAME,AGE). Going further, the ground literal, say, the extension of R represents a tuple in r. So, if we would like to emphasize the fact that EMP(yjd, 23) is the extension of EMP(NAME, AGE), we denote it as EMP(yjd/NAME, 23/AGE).

(9) Constant relation: Let R be a relation predicate. If R is used as constant, it is called constant relation or simply, relation. Such a relation is denoted as lower-case letter of R, say r.

(10) Projection: denotes as [ ], which has the same meaning as in relation algebra.

(11) Relation scheme: Set of attribute variables forming a relation predicate R, denoted as SCH(R).

## 2.2. Database

Logic paradigm for relational Database (DB) model has two different viewpoints: model theoretic and proof theoretic [7]. In a model theoretic view, DB is a particular kind of first order interpretation and query evaluation is a process of truth functional evaluation of first order formulas. On the contrary, in a proof theoretic view, DB is regarded as a set of first order formulas not as an interpretation. Queries are formulas to be proven, given DB as premises.

In this paper, we adopt a proof theoretic view for employing mechanical theorem proving techniques to answer queries and to deal with computational aspects involving DB in general.

DB consists of Intentional Database (IDB), Extensional Database (EDB) and Conjunction of I-clause Database (CI-DB). Besides normal general laws, IDB contains complete set of types, where all information about types reside. It also contains (1) domain closure axioms such as $(\forall X)(X = c_{1}) \vee \ldots \vee (X = c_{n})$ implying that there is a finite number of elements in the universe and they are all known and named by constants, (2) unique name axioms such as $c_{1} \neq c_{2}$ for each pair of distinct constants $c_{1}$ and $c_{2}$ and (3) equality axioms [4]. EDB is considered as a set of relational tuples or it is a set of function free ground literals in the logical point of view. Finally, CI-DB is a set of conjunction of implicit clauses, which will be defined later in section 2.4.

Remark. DB could exclude domain closure axioms and equality axioms except $(\forall X)(X = X)$ if queries to be evaluated have only existential quantifiers. But, details about that are out of our concerns (see [18]).

## 2.3. Database World Assumption

Generally, DB may respond to a query based on the Open World Assumption (OWA), the Closed World Assumption (CWA), or the Expanded Closed World Assumption (ECWA). The OWA corresponds to the usual first order approach to query evaluation: Given a DB and a query Q, the only answers to Q are those which obtain from proofs of Q given DB as the theory. Under the CWA, answers are admitted as a result of failure to find a proof. More specially, if no proof of a positive ground literal exists, then the negation of the literal is assumed true. The CWA is codified in the following completion axiom:

$$
\begin{array}{l}\left(\forall X _ {1}\right) \dots \left(\forall X _ {n}\right)\\\left(\left(\left(\left(X _ {1} = c _ {1 1}\right) \wedge \dots \wedge \left(X _ {n} = c _ {1 n}\right)\right) \right. \right.\\\quad \vee \left(\left(X _ {1} = c _ {2 1}\right) \wedge \dots \wedge \left(X _ {n} = c _ {2 n}\right)\right) \vee \dots\\\quad \vee \left(\left(X _ {1} = c _ {m 1}\right) \wedge \dots \wedge \left(X _ {n} = c _ {m n}\right)\right))\\\leftarrow R (X _ {1}, X _ {2}, \dots , X _ {n})\left. \right)\end{array}
$$

where $R(c_{11},\ldots,c_{1n})$ through $R(c_{m1},\ldots,c_{mn})$ are tuples in a relation r.

We say that $\mathrm{R}(\mathrm{c}_{1},\ldots,\mathrm{c}_{n})$ is represented in the axiom if $(\mathrm{X}=\mathrm{c}_{1})\wedge(\mathrm{X}=\mathrm{c}_{2})\wedge\ldots\wedge(\mathrm{X}=\mathrm{c}_{n})$ is a disjunct of the completion axiom. For the case of $X=a\vee X=b\leftarrow R(X)$ , $R(a)$ and $R(b)$ are the only tuples represented in the given completion axiom. However, the CWA leads to inconsistencies when used with indefinite DB. For example, consider a DB that consists of a single fact, $\mathrm{EMP}(\mathrm{yid})\vee\mathrm{EMP}(\mathrm{kjh})$ , and of a single deductive law, $X=yjd\vee X=kjh\leftarrow EMP(X)$ . $\mathrm{EMP}(\mathrm{yjd})$ can not be proved, because the application of the CWA leads to $DB\vdash\sim EMP(yjd)$ . Similarly, one can also conclude $DB\vdash\sim EMP(kjh)$ . But, the set of clauses $\{X=yjd\vee X=kjh\leftarrow EMP(X), EMP(yjd)\}$ $\vee$ EMP(kjh), $\sim$ EMP(yjd), $\sim$ EMP(kjh)} is obviously inconsistent.

A third alternative constraints, called ECWA, was presented in [12,13]. The incomplete knowledge can be explicitly stated using the ECWA theory. All true facts in any particular model of the theory must either appear as part of a disjunction explicitly mentioned in the theory, or else be derivable from such disjunctions. All facts not derivable from combinations of the disjunctions can't be answers to a given query.

Notice the semantic difference between X = a $\leftarrow$ R(X) and R(X) $\leftarrow$ X = a relative to the IP construct which will be described in the following section. The former states that R(X) is true when X = a, otherwise false, whereas the latter states that R(X) can be true not only for a constant a but for another constant b. In other words, R(b) may be true if R(b/X) $\leftarrow$ IP(k, b/X) is valid. The IP concept is based on this ECWA, which is known to be more computationally tractable than the OWA and more powerful in representation than the CWA.

## 2.4. Implicit Predicate (IP) Concept

At first, we describe the terminologies and conventions for the formal definition of IP construct.

(1) Range predicate is an inequality predicate such as $\mathbf{X} \geq a$ .

(2) Simple type is a 1-place predicate, an equality predicate such as $\mathbf{X} = \mathbf{a}$ or a range predicate.

(3) A set of types can be constructed by the followings.

(a) A simple type is a type.

(b) If $\tau_{1}$ and $\tau_{2}$ are types, then $\tau_{1} \vee \tau_{2}$ , $\tau_{1} \wedge \tau_{2}$ and $\sim \tau_{1}$ are types.

(c) Nothing else can be a type.

(4) If $S$ is a variable or constant and $\tau_{1}$ and $\tau_{2}$ are types, then

(a) If $\tau$ is $\tau_{1} \vee \tau_{2}$ , $\tau(S)$ is $\tau_{1}(S) \vee \tau_{2}(S)$ .

(b) If $\tau$ is $\tau_{1} \wedge \tau_{2}$ , $\tau(S)$ is $\tau_{1}(S) \wedge \tau_{2}(S)$ .

(c) If $\tau$ is $\sim \tau_{1}$ , $\tau_{1}(\mathbf{S})$ is $\sim \tau_{1}(\mathbf{S})$ .

Let T be a set of types. Then T is $\tau$ -complete in the sense that for each constant c and each simple type $\tau$ , $T \vdash \tau(c)$ or $T \vdash \sim \tau(c)$ . The set of types can be regarded as a domain descriptor. Furthermore, it serves as the initial descriptor in the evolving step of implicit predicate, which is defined as follows.

Definition 1. Let 1 be an integer constant representing evolution level, r be a relation and A ∈ SCH(R). Implicit Predicate (IP) is a predicate shared by a set of unknown values occurring in A. 1) If the unknown values are determined by an determinant constant k, it is denoted as IP(r, k, A, l) and 2) if the unknown values are determined by a determinant, it is denoted as IP(r, K, A,l).

For notational simplicity, we will not explicitly specify r or l in the case when ambiguities do not occur. In addition, when the reference of tuple t containing the unknown value is necessary rather than determinant or determinant constant, $\mathrm{IP}_{t}(\mathrm{A})$ will be used.

Definition 2. Implicit well formed formula, Iwff, is defined recursively as follows:

(1) Implicit Predicate IP and Type $\tau$ are Iwffs.

(2) Let $Iwf_{1}$ and $Iwf_{2}$ be Iwffs. Then $Iwf_{1} \vee Iwf_{2}$ , $Iwf_{1} \wedge Iwf_{2} \sim Iwf_{1}$ , $(\forall X)Iwf_{1}$ and $(\exists X)Iwf_{1}$ are Iwffs.

(3) Nothing else can be Iwff.

Let IWF be a set of Iwffs. If $Iwf \in IWF$ contains an attribute variable A which does not participate in determinant K, we will sometimes denote it as $Iwf(A)$ . So, as shown above,

(1) when $Iwf$ is $Iwf_1 \vee Iwf_2$ , $Iwf(A)$ is $Iwf_1(A) \vee Iwf_2(A)$ ,

(2) when $Iwf$ is $Iwf_1 \wedge Iwf_2$ , $Iwf(A)$ is $Iwf_1(A) \wedge Iwf_2(A)$ ,

$$
(3) \text {   when   } I w f \text {   is   } \sim I w f _ {1}, I w f (A) \text {   is   } \sim I w f _ {1} (A).
$$

In this convention, if variable A are instantiated by constant c, then notation $Iwf(c/A)$ will be used. For example, if Iwf is $Iwf_{1} \wedge Iwf_{2}$ , then $Iwf(c/A)$ will be $Iwf_{1}(c/A) \wedge Iwf_{2}(c/A)$ .

According to [9], as Iwff is monadic predicate calculus, there exists an algorithm which determines whether or not DB $\vdash$ Iwf for any $Iwf\in$ IWF. This must remain true regardless of how DB is represented. Moreover, the implementation efficiencies are thoroughly studied in [3,17]. So we can assume this efficient decision procedure is available, which appears in the following definition.

Definition 3. Let Iwf be Iwff. The value of Iwf, |Iwf(A)|, is defined as |Iwf(A)| = {constant c|DB|Iwf(c/A)}.

Now, consider the implication form composed of Iwffs such as $(\forall\mathbf{A})(\mathrm{IP}(\mathbf{k},\mathbf{A}) \leftarrow Iwf_{1}(\mathbf{A}) \vee Iwf_{2}(\mathbf{A}))$ . It can be transformed to $(\forall\mathbf{A})((\mathrm{IP}(\mathbf{k},\mathbf{A}) \leftarrow Iwf_{1}(\mathbf{A})) \wedge (\mathrm{IP}(\mathbf{k},\mathbf{A}) \leftarrow Iwf_{2}(\mathbf{A})))$ , the form of which is the conjunction of clauses. Therefore, we get the following definition.

Definition 4. Let Iwf be Iwff. The Conjunction of Implicit clause (CI-clause) corresponding to an unknown value $\omega$ occurring in an attribute $A \in \text{SCH}(R)$ is a valid well formed formula having the following form.

$$
\begin{array}{l} (\forall \mathrm{A}) \big (\mathrm{IP} (\mathrm{r}, \mathrm{K}, \mathrm{A}, \mathrm{l} _ {\mathrm{i}}) \leftarrow I w f (\mathrm{A}) \big) ^ {*} \text {   satisfying } \\ | \mathrm{IP} (\mathrm{r}, \mathrm{K}, \mathrm{A}, \mathrm{l} _ {\mathrm{i}}) | = | I w f (\mathrm{A}) |, \end{array}
$$

where R is a relation predicate and K is a determinant. The CI-clause expresses $\omega$ by restricting that $\omega$ is one of the elements in $|\mathrm{IP}(\mathbf{r},\mathbf{K},\mathbf{A},\mathbf{l}_{i})|$ . Particularly, if K is replaced by determinant constant k, we will call the above formula extensional CI-clause; otherwise, intensional one.

The reason for setting the condition, $|\mathrm{IP}(\mathbf{r},\mathbf{k},\mathbf{A},\mathbf{l}_{i})| = |Iwf(A)|$ , is to avoid the situation that different CI-clauses, but having same $\mathrm{IP}(\mathbf{r},\mathbf{k},\mathbf{A},\mathbf{l}_{i})$ coexist. For example, let $\mathrm{IP}(\mathbf{r},\mathbf{k},\mathbf{A},\mathbf{l}_{i})\leftarrow \mathbf{A} = a\lor \mathbf{A} = b$ be a CI-clause. If another CI-clause, $\mathrm{IP}(\mathbf{r},\mathbf{k},\mathbf{A},\mathbf{l}_{i})\leftarrow \mathbf{A} = c$ exist, then $|\mathrm{IP}(\mathbf{r},\mathbf{k},\mathbf{A},\mathbf{l})| = \{\mathbf{a},\mathbf{b},\mathbf{c}\} \neq |\mathbf{A} = \mathbf{a}\lor \mathbf{A} = \mathbf{b}| = \{\mathbf{a},\mathbf{b}\}$ . This condition also is related to our world assumption ECWA, since the information that an unknown value $\omega$ is one of a and b implies that $\omega$ can't be c.

Remark. The condition stated above enables us to treat CI-clause and IP as same constructs. So, if necessary, we will reference them interchangeably. For brevity, we assume a CI-clause is governed by universal quantifier if the quantifier is not explicitly specified.

Now, let's turn our arguing point to the characteristics of intensional CI-clause and extensional

![](/api/attachments/H4XN56VP/fulltext/images/173a2b9b04bf9f75d23fc9281e713c3f85a83fa17f23e8a75ae12ff1cb15d78d.jpg)  
Fig. 1. Representation of the relationships between enterprises and labs.

CI-clause. At the initial evolution stage, in other words, when knowledge about an unknown value comes only from type $\tau$ , an intensional CI-clause, $\mathrm{IP}(\mathrm{r},\mathrm{K},\mathrm{A})\leftarrow\tau(\mathrm{A})$ distinguishes unknown values only by the attribute A. In this case, unknown values appearing in one common attribute A share $\mathrm{IP}(\mathrm{r},\mathrm{K},\mathrm{A})\leftarrow\tau(\mathrm{A})$ in the sense that $\mathrm{IP}_{\mathrm{t}}(\mathrm{r},\mathrm{k}/\mathrm{K},\mathrm{A})\leftarrow\tau(\mathrm{A})$ is valid for any determinant constant k of any tuple t in r. This intensional CI-clause will evolve gradually as the incomplete data from user or the various inference rules in DB are exploited. Then it will be capable of distinguishing unknown values by the tuple in the sense that $\mathrm{IP}_{\mathrm{t}}(\mathrm{r},\mathrm{k},\mathrm{A})\leftarrow I wf(\mathrm{A})$ is valid for only one determinant constant k of some tuple t in r. Such an evolved CI-clause is the extensional CI-clause.

Example 1. A database to be referenced throughout the paper, called research database, is described as following. We model the environments that researchers in several labs are engaged in projects with several enterprises by m to n relationships as shown in fig. 1. Unknown values appearing in this database are not marked nulls [16], but marked only for referential convenience.

Fig. 1. expresses the semantics of the sets of types. For example, in fig. 2(b), type $\tau_{\mathrm{SLAB}}(\mathbf{X})$ , $(\forall \mathbf{X})(\mathbf{X} = \mathrm{os}\lor \mathbf{X} = \mathrm{db})$ on which an attribute SLAB of sams is defined, expresses the semantic that sams has projects only with os and db labs. Other relations in fig. 3, link\_seminar and tax contain the information about researchers taking part in more than one projects and tax imposed on the researchers respectively.

Example 2. From fig. 3 (a) and Definition 3, the value of $\tau_{\mathrm{TIME}}(\mathrm{TIME})$ and $\tau_{\mathrm{LLAB}}(\mathrm{LLAB})$ are $|\tau_{\mathrm{TIME}}(\mathrm{TIME})| = \{\text{constant c} | \text{DB} |\tau_{\mathrm{TIME}}(\text{c}/$

researcher

$\tau_{\mathrm{KLAB}}(X) = (\forall X)(X = db \vee X = os \vee X = nw)$ .

<table><tr><td>NAME</td><td>PROJ</td><td>TOPIC</td><td>LAB</td></tr><tr><td>yjd</td><td>sams</td><td> $\omega_1$ </td><td> $\omega_2$ </td></tr><tr><td>hrl</td><td>keum</td><td> $\omega_3$ </td><td> $\omega_4$ </td></tr><tr><td>hrl</td><td>sams</td><td> $\omega_5$ </td><td> $\omega_6$ </td></tr><tr><td>hrl</td><td>sams</td><td> $\omega_7$ </td><td> $\omega_8$ </td></tr><tr><td>kck</td><td>keum</td><td> $\omega_9$ </td><td>os</td></tr><tr><td>jim</td><td>sams</td><td> $\omega_{10}$ </td><td>os</td></tr><tr><td>hkl</td><td>keum</td><td> $\omega_{11}$ </td><td>os</td></tr></table>

sams

<table><tr><td>NAME</td><td>DEPT</td><td>STOPIC</td><td>SLAB</td></tr><tr><td>yjd</td><td>sys</td><td> $\omega_{21}$ </td><td> $\omega_{22}$ </td></tr><tr><td>hrl</td><td>sys</td><td> $\omega_{23}$ </td><td> $\omega_{24}$ </td></tr><tr><td>hrl</td><td>db</td><td> $\omega_{25}$ </td><td> $\omega_{26}$ </td></tr><tr><td>jim</td><td>sys</td><td> $\omega_{27}$ </td><td>os</td></tr></table>

(a)  
(b)

$\tau_{PROJ}(X) = (\forall X)(X = keum \lor X = sams \lor X = daew)$ . $\tau_{TOPIC}(X) = (\forall X)(X = kern \lor X = dbms \lor X = modem \lor X = s/w)$ . $\tau_{LAB}(X) = (\forall X)(X = os \lor X = db \lor X = sa \lor X = nw)$ .

$$
\begin{array}{r l} \tau_ {\text { SLAB }} (X) & = (\forall X) (X = o s \lor X = d b). \\ \tau_ {\text { STOPIC }} (X) & = (\forall X) (X = k e m \lor \\ & X = d b m s \lor X = s / w). \end{array}
$$

keum

<table><tr><td>NAME</td><td>....</td><td>KLAB</td></tr><tr><td>hrl</td><td></td><td> $\omega_{31}$ </td></tr><tr><td>kck</td><td></td><td> $\omega_{32}$ </td></tr><tr><td>hkl</td><td></td><td> $\omega_{33}$ </td></tr></table>

(c)

os

<table><tr><td>NAME</td><td>....</td><td>OPROJ</td></tr><tr><td>kck</td><td></td><td> $\omega_{41}$ </td></tr><tr><td>jim</td><td></td><td>sams</td></tr><tr><td>hkl</td><td></td><td> $\omega_{42}$ </td></tr></table>

(d)  
Fig. 2.  
TIME) = c/ TIME ≥ 10 ∧ c/TIME ≤ 17} and | τLLAB(LLAB) | = {constant c | DB |τSLAB(c/ SLAB) ∧ τKSLAB(c/KLAB)} = {os, db}.

Example 3. In fig. 2 (a), the intensional CI-clause of the unknown values occurring in TOPIC is IP(K, TOPIC, $l_{1}$ ) ← $\tau_{\text{TOPIC}}(\text{TOPIC})$ and one in

link\_seminar  
tax

<table><tr><td>NAME</td><td>TIME</td><td>TOPIC</td><td>LLAB</td></tr><tr><td>hrl</td><td> $\omega_{51}$ </td><td> $\omega_{52}$ </td><td> $\omega_{53}$ </td></tr></table>

(a)  
$\tau_{\mathrm{TIME}}(\mathbf{X}) = (\forall \mathbf{X})(\mathbf{X}\geq 10\wedge \mathbf{X}\leq 17)$  
$\tau_{\mathrm{LLAB}}(X) = \tau_{\mathrm{SLAB}}(X) \wedge \tau_{\mathrm{KLAB}}(X)$ .

Fig. 3.

(b)

<table><tr><td>NAME</td><td>..AMOUNT</td><td>TOPIC</td></tr><tr><td>yjd</td><td>... 20</td><td> $\omega_{61}$ </td></tr><tr><td>hrl</td><td>... 10</td><td> $\omega_{62}$ </td></tr><tr><td>hrl</td><td>... 10</td><td> $\omega_{63}$ </td></tr><tr><td>jim</td><td>... 15</td><td>os</td></tr></table>

LAB is IP(K, LAB, $l_{1}$ ) ← $\tau_{\text{LAB}}(\text{LAB})$ , where K = NAMEPROJ. Example about extensional CI-clauses will be shown in Example 5.

Thus far we have defined a CI-clause as the descriptor of a set of unknown values associated with it. Going one step further, can this CI-clause mirror the continual augmentation of available user knowledge on a corresponding unknown value? Now, we will concentrate on the evolution of the CI-clause by these user information.

Definition 5. Let $f_1, f_2 \in \mathrm{IWF}$ . $f_1$ is more informative than $f_2$ if and only if $f_1(c / A_1) \to f_2(c / A_2)$ is valid for all constant $c$ . We denote it as $f_1 \geq f_2$ .

We can easily see that if $f_{1}$ is more informative than $f_{2}$ , then $f_{2}$ is the logical consequence of $f_{1}$ relative to the definition in [4]. The following lemma will give the intuitive insight into the relation $\geq$ .

Lemma 1. Let $Iwf_{1}$ and $Iwf_{2} \in \mathrm{IWF}$ . Then $|Iwf_{2}(A_{2})| \supseteq |Iwf_{1}(A_{1})|$ if and only if $Iwf_{1} \geq Iwf_{2}$ .

Proof. (⇒) Suppose $|Iwf_{2}(A_{2})| \supseteq |Iwf_{1}(A_{1})|$ . Then by Definition 3, for all constant a satisfying DB $|Iwf_{1}(a/A_{1}), DB|-Iwf_{2}(a/A_{2})$ also holds. So $Iwf_{1}(a/A_{1}) \to Iwf_{2}(a/A_{2})$ is valid. If DB $\vdash \sim Iwf_{1}(b/A_{1})$ , in other words, if $Iwf_{1}(b/A_{1})$ is false for some constant b, where $b \neq a$ , then $Iwf_{1}(b/A_{1}) \to Iwf_{2}(b/A_{2})$ will be vacuously true. In consequence, $Iwf_{1} \geq Iwf_{2}$ by Definition 5.

$(\Leftarrow)$ Suppose $Iwf_{1} \geq Iwf_{2}$ . Then by Definition 5, $Iwf_{1}(a / A_{1}) \to Iwf_{2}(a / A_{2})$ is valid for all constant a. So if DB $\vdash Iwf_{1}(a / A_{1})$ , then DB $\vdash Iwf_{2}(a / A_{2})$ which means $|Iwf_{2}(A_{2})| \supseteq |Iwf_{1}(A_{1})|$ . Q.E.D.

Example 4. In fig. 2 (a) and fig. 2 (c), $\tau_{\mathrm{KLAB}}(\mathrm{KLAB}) \geq \tau_{\mathrm{LAB}}(\mathrm{LAB})$ since $|\tau_{\mathrm{LAB}}(\mathrm{LAB})| = \{\mathrm{os}, \mathrm{db}, \mathrm{sa}, \mathrm{nw}\} \supseteq |\tau_{\mathrm{KLAB}}(\mathrm{KLAB})| = \{\mathrm{db}, \mathrm{os}, \mathrm{nw}\}$ .

Proposition 1. $\langle \mathrm{IWF},\geq \rangle$ is a Partially Ordered Set(POSET).

Proof. Obviously, $\geq$ is reflexive, transitive and antisymmetric (see [22]).

Definition 6. Let $\langle \mathrm{IWF},\geq \rangle$ be a POSET and let $\{Iwf_1,Iwf_2\in \mathrm{IWF}\}$ be I. The Least Upper

Bound(LUB) for I, denoted as LUB( $Iwf_{1}$ , $Iwf_{2}$ ), is an element $Iwf \in IWF$ such that Iwf is an upper bound for I and $Iwf_{3} \geq Iwf$ , where $Iwf_{3}$ is any upper bound for I. Any $Iwf_{3} \in IWF$ is upper bound for I if $Iwf_{3} \geq Iwf_{1}$ and $Iwf_{3} \geq Iwf_{2}$ . Similarly, the Greatest Lower Bound(GLB) for I, denoted as GLB( $Iwf_{1}$ , $Iwf_{2}$ ), is an element $Iwf \in IWF$ such that Iwf is a lower bound for I and $Iwf \geq Iwf_{3}$ where $Iwf_{3}$ is any lower bound for I. Any $Iwf_{3} \in IWF$ is lower bound for I if $Iwf_{1} \geq Iwf_{3}$ and $Iwf_{2} \geq Iwf_{3}$ .

Lemma 2. Let $\langle IWF, \geq \rangle$ be a POSET and let $Iwf_{1}, Iwf_{2}$ and $Iwf_{3} \in IWF$ .

(1) If $Iwf_{3} \geq Iwf_{1}$ and $Iwf_{3} \geq Iwf_{2}$ , then (i) $Iwf_{3} \geq (Iwf_{1} \wedge Iwf_{2})$ and (ii) $Iwf_{3} \geq (Iwf_{1} \wedge Iwf_{2})$ .

(2) If $Iwf_{3} \leq Iwf_{1}$ and $Iwf_{3} \leq Iwf_{2}$ , then (i) $Iwf_{3} \leq (Iwf_{1} \wedge Iwf_{2})$ and (ii) $Iwf_{3} \leq (Iwf_{1} \vee Iwf_{2})$ .

The proof methodology of the lemma can be found in [9].

Theorem 1. Let $\langle \mathrm{IWF},\geq \rangle$ be a POSET. Then any pair of elements in IWF, say $Iwf_{1}$ and $Iwf_{2}$ , has LUBs and GLBs which should satisfy

$$
\left| \mathrm{LUB} \left(I w f _ {1}, I w f _ {2}\right) \right| = \left| I w f _ {1} \wedge I w f _ {2} \right|
$$

$$
\left| \operatorname{GLB} \left(I w f _ {1}, I w f _ {2}\right) \right| = \left| I w f _ {1} \vee I w f _ {2} \right|
$$

In particular, When $Iwf_{1} \geq Iwf_{2}$ , $|\mathrm{LUB}| = |Iwf_{1} \wedge Iwf_{2}| = |Iwf_{1}|$ and $|\mathrm{GLB}| = |Iwf_{1} \vee Iwf_{2}| = |Iwf_{2}|$ .

Proof. Assume there exists a LUB, $Iwf_{3}$ not satisfying $|Iwf_{3}| = |Iwf_{1} \wedge Iwf_{2}|$ . But, we can get $|Iwf_{1} \wedge Iwf_{2}| \supseteq |Iwf_{3}|$ by Lemma 1, 2 and Definition 6, and successively get $|Iwf_{3}| \supseteq |Iwf_{1} \wedge Iwf_{2}|$ since $Iwf_{1} \wedge Iwf_{2}$ is upper bound and $(Iwf_{1} \wedge Iwf_{2}) \geq Iwf_{3}$ . So, we conclude $|Iwf_{3}| = |Iwf_{1} \wedge Iwf_{2}|$ , which contradict the assumption. In particular, we postulate $|Iwf_{1}| \supseteq |Iwf_{1} \wedge Iwf_{2}|$ . Since $Iwf_{1} \geq Iwf_{1}$ by reflexivity, if $Iwf_{1} \geq Iwf_{2}$ , then we get $|Iwf_{1} \wedge Iwf_{2}| \supseteq |Iwf_{1}|$ from Lemma 1 and 2. Hence, $|Iwf_{1}| = |Iwf_{1} \wedge Iwf_{2}|$ . Proof in the case of GLB is similar to that of LUB.

Lemma 3. Let $\mathrm{IP}_{\mathrm{t1}}(\mathbf{A}) \leftarrow Iwf_1(\mathbf{A})$ and $\mathrm{IP}_{\mathrm{t2}}(\mathbf{A}) \leftarrow Iwf_2(\mathbf{A})$ be CI-clauses where tuple $t_1$ and $t_1$ are not necessarily distinct. If $Iwf_1 \geq Iwf_2$ , then $\mathrm{IP}_{\mathrm{t1}}(\mathbf{A}) \geq \mathrm{IP}_{\mathrm{t2}}(\mathbf{A})$ .

Proof. If $Iwf_{1} \geq Iwf_{2}$ , then $|Iwf_{2}| \supseteq |Iwf_{1}|$ . Since $|\mathrm{IP}_{\mathrm{t1}}(\mathbf{A})| = |Iwf_{1}|$ and $|\mathrm{IP}_{\mathrm{t2}}(\mathbf{A})| = |Iwf_{2}|$ by the definition of CI-clause, we get $\mathrm{IP}_{\mathrm{t1}}(\mathbf{A}) \geq \mathrm{IP}_{\mathrm{t2}}(\mathbf{A})$ . Q.E.D.

Theorem 2. Let a set of CI-clauses $\{\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},\mathbf{l}_{\mathrm{i}})\leftarrow Iwf_{i}(\mathbf{A})|1\leq \mathrm{i}\leq \mathrm{n}\}$ be given where tuples, $\mathfrak{t}_1,\ldots ,\mathfrak{t}_n$ are not necessarily distinct. Then for all i and j, $1\leq \mathrm{i},\mathrm{j}\leq \mathrm{n},$

$$
\begin{array}{l} \text { case   1 } \quad | \mathrm{LUB} \big (\mathrm{IP} _ {\mathrm{ti}} (\mathrm{A}, 1 _ {\mathrm{i}}), \mathrm{IP} _ {\mathrm{tj}} (\mathrm{A}, 1 _ {\mathrm{j}}) \big) | \\ \qquad = | \mathrm{IP} _ {\mathrm{ti}} (\mathrm{A}, 1 _ {\mathrm{i}}) | \\ \text { if   } I w f _ {i} \geq I w f _ {j}. \\ \text { case   2 } \quad | \mathrm{LUB} \big (\mathrm{IP} _ {\mathrm{ti}} (\mathrm{A}, 1 _ {\mathrm{i}}), \mathrm{IP} _ {\mathrm{tj}} (\mathrm{A}, 1 _ {\mathrm{j}}) \big) | \\ \qquad = | \mathrm{IP} _ {\mathrm{ti}} (\mathrm{A}, 1 _ {\mathrm{i}}) \wedge \mathrm{IP} _ {\mathrm{tj}} (\mathrm{A}, 1 _ {\mathrm{j}}) | \end{array}
$$

Proof. We only consider the case 1, since case 2 coincides with Theorem 1. Assume there exists LUB such that $|\mathrm{LUB}| \neq |\mathrm{IP}_{\mathrm{ti}}(\mathbf{A}, l_{i})|$ despite that $Iwf_{i} \geq Iwf_{j}$ . We will prove the theorem by contradicting the assumption. Since $Iwf_{i} \geq Iwf_{j}$ , $\mathrm{IP}_{\mathrm{ti}}(\mathbf{A}, l_{i}) \geq \mathrm{IP}_{\mathrm{tj}}(\mathbf{A}, l_{j})$ as specified in Lemma 3. Accordingly, $|\mathrm{LUB}| = |\mathrm{IP}_{\mathrm{ti}}(\mathbf{A}, l_{i})|$ by Theorem 1. Q.E.D.

Lemma 4. Let $\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},1_{\mathrm{i}})\leftarrow Iwf_{i}(\mathbf{A})$ and $\mathrm{IP}_{\mathrm{tj}}(\mathbf{A},1_{\mathrm{j}})$ $\leftarrow Iwf_{j}(\mathbf{A})$ be CI-clauses. Then $\mathrm{LUB}(\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},1_{\mathrm{i}}),\mathrm{IP}_{\mathrm{tj}}(\mathbf{A},1_{\mathrm{j}}))$ is the logical consequence of $\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},1_{\mathrm{i}})$ and $\mathrm{IP}_{\mathrm{tj}}(\mathbf{A},1_{\mathrm{j}})$ .

Proof. According to Definition 6, $|\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},1_{\mathrm{i}})| \supseteq |\mathrm{LUB}|$ and $|\mathrm{IP}_{\mathrm{tj}}(\mathbf{A},1_{\mathrm{j}})| \supseteq |\mathrm{LUB}|$ . So, for any constant c, if $c \in |\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},1_{\mathrm{i}})|$ and $c \in |\mathrm{IP}_{\mathrm{tj}}(\mathbf{A},1_{\mathrm{j}})|$ , then $c \in |\mathrm{LUB}|$ , which means LUB is the logical consequence of two IPs. Q.E.D.

Up to this point, we have argued the relation $\geq$ between two IPs. But, under what conditions can this relation derive a meaningful logical consequence of several IPs? As an answer, we will introduce a new type of constraint.

Definition 7. IP Equality Constraint (IEC) is defined as the equality of two unknown values in spite of their incompleteness, denoted $\mathrm{IPt}_{1}(\mathbf{A}_{1})=\mathrm{IP}_{\mathrm{t}_{2}}(\mathbf{A}_{2})$ for tuples $t_{1}$ and $t_{2}$ such that $t_{1}[\mathbf{A}_{1}]=\omega_{1}$ , $t_{2}[\mathbf{A}_{2}]=\omega_{2}$ and $\omega_{1}=\omega_{2}$ , where $A_{1}$ and $A_{2}$ are attribute variables.

In the above Definition 7, if $\mathrm{IP}_{\mathrm{t1}}(\mathbf{A}_{1}) \neq \mathrm{IP}_{\mathrm{t2}}(\mathbf{A}_{2})$ in a current DB state, then we may regard IEC as a procedure to make two IPs equal to their logical consequence through LUB. The following theorem specify the way to generate this logical consequence, which will be commonly associated with two unknown values under IEC.

Theorem 3. Let $\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},1_{\mathrm{i}})\leftarrow Iwf_{i}(\mathbf{A})$ and $\mathrm{IP}_{\mathrm{tj}}(\mathbf{A},1_{\mathrm{j}})\leftarrow Iwf_{j}(\mathbf{A})$ be CI-clauses of two unknown values under IEC respectively. If $\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},1_{\mathrm{k}})\leftarrow$ LUB $(\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},1_{\mathrm{i}}),\mathrm{IP}_{\mathrm{tj}}(\mathbf{A},1_{\mathrm{j}}))$ be new common CI-clause of two unknown values under IEC, then $\mathrm{IP}_{\mathrm{ti}}(\mathbf{A},1_{\mathrm{k}})$ is not only the logical consequence of the previous two IPs but also more informative than each of them, where level $1_{\mathrm{k}}$ is one plus maximum value of $1_{\mathrm{i}}$ and $1_{\mathrm{j}}$ .

Proof. It can be proved by Lemma 4 and the definition of LUB.

Example 5. We accept the incomplete information from user for unknown value $\omega_{51}$ in fig. 3 (a) that "hrl's seminar is held before 11 A.M. or after 3 P.M. but not 5 P.M." Then corresponding $Iwf \in IWF$ is $Iwf(\text{TIME}) = (\text{TIME} \leq 11 \lor \text{TIME} \geq 15) \land \text{TIME} \neq 17$ . If we assume that the information provided by users are always correct, IP(hrl, TIME, $l_2$ ) $\leftarrow Iwf(\text{TIME})$ is a valid formula. Next, consider the original CI-clause of $\omega_{51}$ , IP(hrl, TIME, $l_1$ ) $\leftarrow \tau_{\text{TIME}}(\text{TIME})$ . Here, since $Iwf \gtrsim \tau_{\text{TIME}}$ and $\tau_{\text{TIME}} \gtrsim Iwf$ , IP(hrl, TIME, $l_3$ ) $\leftarrow$ IP(hrl, TIME, $l_1$ ) $\land$ IP(hrl, TIME, $l_2$ ) will be the most evolved CI-clause of $\omega_{51}$ to be asserted by Theorem 2 and 3. In the same fashion, user may supply the information for the unknown value $\omega_9$ that "kck's topic is one of kern and dbms" into the relation researcher. Then corresponding $Iwf$ and new CI-clause are $Iwf$ (TOPIC) = (TOPIC = kern $\lor$ TOPIC = dbms) and IP(kck, TOPIC, $l_2$ ) $\leftarrow Iwf(\text{TOPIC})$ respectively. Again, consider IP(kck, TOPIC, $l_1$ ) $\leftarrow \tau_{\text{TOPIC}}(\text{TOPIC})$ . Since $Iwf \geq \tau_{\text{TOPIC}}$ , we know LUB(IP(kck, TOPIC, $l_1$ ), IP(kck, TOPIC, $l_2$ )) is IP(kck, TOPIC, $l_2$ ) by Theorem 2. Accordingly, IP(kck, TOPIC, $l_3$ ) $\leftarrow$ IP(kck, TOPIC, $l_2$ ) will be the most evolved CI-clause of $\omega_9$ to be asserted.

Notice that GLB concept is useful only when we permit such type of information as “kck’s topic may be kern or dbms”. Apparently this information imply that kck's topic can take any other value. Suppose we accept the subsequent information that kck's topic may be dbms or s/w. Then the augmented knowledge will be "kck's topic may be kern, dbms or s/w", which is the GLB of Iwffs corresponding to the two informations. However, we have assumed that other cases not specified explicitly in user information can't be possible. This can prevent meaningless deductions. For example, suppose a user asserts that kck's topic may be dbms and the other that his topic may not be dbms to the contrary. Then the conclusion obtained by GLB concept tells us nothing, because the topic may or may not be dbms.

Recall that we defined two kinds of IP, intensional IP and extensional IP. You may easily see that all CI-clauses appearing in Example 5 are the examples of extensional IP.

## 3. IP Evolutions through Inference Rules

It is well known that most inference rules can be uniformly represented by generalized dependency statement $[8]$ . Among them, Functional Dependency (FD) and Inclusion Dependency (ID) are the most frequently referenced inference rules in DB applications because of their powerful expressiveness for the semantics of relational DB model. Accordingly we present how IP can evolve in a uniform and consistent way through exploiting these two inference rules.

## 3.1. Functional Dependencies (FD) and IP

Since FD is one of the representative constraints expressing the logic of relational model, many algorithms exploiting the constraint to unknown value evolution have been developed $[19,23]$ . The scenario we propose in this section is that these algorithms can be revised in the context of IP constructs. Due to IP's enhanced expressiveness, the revision can evolve IP through FDs in more general and uniform way compared with $[19,23]$ . Now, we describe it abstractly.

Setting K as determinant in Definition 1 assumes the exploitation of FDs imposed on a relation. For example, in fig. 2 (b), $\omega_{23}$ and $\omega_{25}$ share common IP, IP(hrl, STOPIC). That results from FD: NAME → STOPIC. The generalization dependency statement for this constraint is shown as follows.

sams

<table><tr><td>NAME</td><td>DEPT</td><td>STOPIC</td><td>SLAB</td></tr><tr><td>yjd</td><td>sys</td><td> $\omega_{21}$ </td><td> $\omega_{22}$ </td></tr><tr><td>hrl</td><td>sys</td><td> $\omega_{23}$ </td><td> $\omega_{24}$ </td></tr><tr><td>hrl</td><td>db</td><td> $\omega_{25}$ </td><td> $\omega_{26}$ </td></tr><tr><td>jim</td><td>sys</td><td> $\omega_{27}$ </td><td>os</td></tr></table>

$\tau_{\mathrm{STOPIC}}(X) = (\forall X)(X = \ker \vee X = \mathrm{dbms} \vee X = \mathrm{s/w})$ .

$$
\begin{array}{r l} & \mathrm{IEC} (\mathrm{IP} _ {\mathrm{t1}} (\text { STOPIC }), \mathrm{IP} _ {\mathrm{t2}} (\text { STOPIC })) \\ & \leftarrow \text { SAMS } [ \text { hrl / NAME }, \omega_ {2 3} / \text { STOPIC } ] \\ & \wedge \text { SAMS } [ \text { hrl / NAME }, \omega_ {2 5} / \text { STOPIC } ] \end{array}
$$

where $\mathfrak{t}_1[\mathrm{STOPIC}] = \omega_{23}$ and $\mathfrak{t}_2[\mathrm{STOPIC}] = \omega_{25}$ .

Actually, the evolution procedure for the above IEC coincides with that for IEC imposed by user supplied information. But, contrary to the latter case, the former differs in that even two IPs having different determinants can take part in this evolution procedure. The following example will clarify this point.

Example 6. For convenience, fig. 2 (b) will be depicted again as fig. 4 along with the CI-clauses associated with corresponding unknown values. The CI-clauses also include one more extensional CI-clause assumed to be asserted previously by accepting a user information for $\omega_{23}$ , as the fashion shown in Example 5.

$$
\begin{array}{l} C I \text {-clauses for sams (fig. 4 (b))} \\ \omega_ {2 1} \colon \mathrm{IP(yjd,STOPIC,1} _ {1}) \leftarrow \tau_ {\text {STOPIC}} (\text {STOPIC}). \\ \omega_ {2 3}, \omega_ {2 5} \colon \mathrm{IP(hrl,STOPIC,1} _ {3}) \leftarrow \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \wedge \mathrm{IP(hrl,STOPIC,1} _ {1}). \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \mathrm{IP(hrl,STOPIC,1} _ {2}) \leftarrow (\text {STOPIC} \neq \\ \qquad \qquad \qquad \qquad \qquad \text {dbms}). \\ \omega_ {2 7} \colon \qquad \qquad \qquad \qquad \qquad \qquad \qquad \tau_ {\text {STOPIC}} (\text {STOPIC}). \\ \omega_ {2 2}, \omega_ {2 4}, \omega_ {2 6} \colon \mathrm{IP(K,SLAB,11)} \leftarrow \tau_ {\text {SLAB}} (\text {SLAB}). \end{array}
$$

Suppose another FD, FD: DEPT → STOPIC is imposed on sams as well as FD: NAME → STOPIC. You will see that both IP(hrl, STOPIC, $l_{3}$ ) ← IP(hrl, STOPIC, $l_{2}$ ) ∧ IP(hrl, STOPIC, $l_{1}$ ) and IP(sys, STOPIC, $l_{1}$ ) ← τ $_{STOPIC}$ (STOPIC) can be candidate CI-clauses of ω $_{23}$ . Since more than one IPs for ω $_{23}$ , i.e., IPs under IEC having different determinant constant each other coexist, a procedure needs to be invoked taking the more informative of the two. In detail, since LUB(IP(hrl, STOPIC, $l_{3}$ ), IP(sys, STOPIC, $l_{1}$ )) = IP(hrl, STOPIC, $l_{3}$ ), we get the most evolved CI-clause of ω $_{23}$ , IP(hrl, STOPIC, $l_{4}$ ) ← IP(hrl, STOPIC, $l_{3}$ ) or IP(sys, STOPIC, $l_{4}$ ) ← IP(hrl, STOPIC, $l_{3}$ ). The coexistence situation may help along the procedure invoked by user information shown in chapter 2. For example, imagine how feasible two different user's insertion pattern into ω $_{23}$ afterwards will be; one insertion that hrl's topic may be one of os and db, and the other that department sys has project with os lab concerning a topic either os or sa. But, since it is time consuming to recognize this coexistence situation, it may be desirable to avoid it by keeping all relations 3NF in which every nonkey attribute is nontransitively dependent on the primary key [6].

## 3.2. Inclusion Dependencies (ID) and IP

IDs [10] are another important subclass of data dependencies denoted by S[Y] ⊃ R[X] where R and S are relation predicates and X and Y are attribute sets. For example, in fig. 4, fig. 5 and fig 3 (b), when the dependencies such as RESEARCHER[NAME, TOPIC] ⊃ SAMS[NAME, STOPIC], TAX[NAME, TOPIC] ⊃ RESEARCHER[NAME, TOPIC] and RESEARCHER[NAME, TOPIC] ⊃ LINK\_SEMINAR[NAME, LAB] are imposed, these are called IDs. Without loss of generality, we can permit these IDs to have a restriction that one determinant per relation should exist among the attributes taking part in the dependencies. Under this restrictions, the IDs can be regarded as the generalization of FDs imposed on between relations. For example, the semantic that subtuple SAMS[hrl/NAME, ω₂₃/STOPIC] should exist in RESEARCHER[NAME, TOPIC] is represented as IEC(IPₜ₁(STOPIC), IPₜ₂(TOPIC)) ← SAMS[hrl/ SNAME, ω₂₃/ STOPIC] ∧

researcher

<table><tr><td>NAME</td><td>PROJ</td><td>TOPIC</td><td>LAB</td></tr><tr><td>yjd</td><td>sams</td><td> $\omega_1$ </td><td> $\omega_2$ </td></tr><tr><td>hrl</td><td>keum</td><td> $\omega_3$ </td><td> $\omega_4$ </td></tr><tr><td>hrl</td><td>sams</td><td> $\omega_5$ </td><td> $\omega_6$ </td></tr><tr><td>hrl</td><td>sams</td><td> $\omega_7$ </td><td> $\omega_8$ </td></tr><tr><td>kck</td><td>keum</td><td> $\omega_9$ </td><td>os</td></tr><tr><td>jim</td><td>sams</td><td> $\omega_{10}$ </td><td>os</td></tr><tr><td>hkl</td><td>keum</td><td> $\omega_{11}$ </td><td>os</td></tr></table>

(a)  
Fig. 5.

RESEARCHER[hrl/NAME, $\omega_{5}$ /TOPIC], where $t_1$ [STOPIC] = $\omega_{23}$ and $t_2$ [TOPIC] = $\omega_{5}$ .

Incorporated with FDs, these IDs can also evolve IP construct. The following example will demonstrate this evolution procedure.

Example 7. First, we will show the evolution procedure occurred between intensional CI-clause. Consider $\omega_{4}$ in fig. 5 and $\omega_{53}$ in fig. 6. Since IP(link\_seminar, hrl, LLAB, $l_{1}$ ) $\geq$ IP(researcher, hrl, LAB, $l_{1}$ ), IP(researcher, hrl, LAB, $l_{2}$ ) $\leftarrow$ IP (link\_seminar, hrl, LAB, $l_{1}$ ) is an evolved CI-clause of $\omega_{4}$ by Theorem 3, where LLAB is renamed by LAB. We now turn to the example that an extensional CI-clause evolved by FDs or user informations in a relation is also used to evolve another CI-clause in another relation. Consider $\omega_{23}$ in fig. 4 and $\omega_{5}$ in fig. 5. Since IP(sams, hrl, STOPIC, $l_{3}$ ) $\geq$ IP(researcher, hrl, TOPIC, $l_{1}$ ), we

link\_seminar

<table><tr><td>NAME</td><td>TIME</td><td>T∅PIC</td><td>LLAB</td></tr><tr><td>hrl</td><td> $\omega_{51}$ </td><td> $\omega_{52}$ </td><td> $\omega_{53}$ </td></tr></table>

(a)  
$\tau_{\mathrm{TIME}}(X) = (X \geq 10 \land X \leq 17)$ .  
$\tau_{\mathrm{LLAB}}(X) = (\tau_{\mathrm{SLAB}}(X) \wedge \tau_{\mathrm{KLAB}}(X)).$

Fig. 6.

get IP(researcher, hrl, TOPIC, $l_{4}$ ) ← IP(sams, hrl, TOPIC, $l_{3}$ ) as an evolved CI-caluse of $\omega_{5}$ . Lastly, consider $\omega_{62}$ in fig. 3 (b) with $\omega_{5}$ and $\omega_{23}$ for preparing an example in which transitive IDs exist. We can easily see that new CI-clause of $w_{62}$ , IP(tax, hrl, TOPIC, $l_{5}$ ) ← IP(researcher, hrl, TOPIC, $l_{4}$ ) should be asserted because IP(researcher, hrl, TOPIC, $l_{4}$ ) ≥ IP(tax, hrl, TOPIC, $l_{1}$ ).

CI-clauses for researcher (fig. 5(b)) $\omega_{1}, \omega_{3}, \omega_{5}, \omega_{7}, \omega_{9}, \omega_{10}, \omega_{11}: IP(K, TOPIC, 1_{1}) \leftarrow \tau_{TOPIC}(TOPIC).$ $\omega_{2}, \omega_{4}, \omega_{6}, \omega_{8}: IP(K, LAB, 1_{1}) \leftarrow \tau_{LAB}(LAB).$

CI-clauses for link \_seminar (fig. 6 (b))
ω51: IP(hrl, TIME, l₃) ← IP(hrl, TIME, l₁) ∧
    IP(hrl, TIME, l₂).
    IP(hrl, TIME, l₂) ← TIME ≤ 11 ∨ TIME ≥
    15 ∧ TIME ≠ 17.
    IP(K, TIME, l₁) ← τ\_TIME(TIME).
ω52: IP(K, TOPIC, l₁) ← τ\_TOPIC(TOPIC).
ω53: IP(K, LLAB, l₁) ← τ\_LLAB(LLAB).

## 4. Conclusion

In this paper we introduced IP as a descriptor for expressing the unknown value semantics. By employing it, we accepted user-supplied incomplete information into DB and reflected it on the unknown values. Besides enhancing the semantic expressiveness of the unknown values, we proposed the procedure exploiting functional dependencies and inclusion dependencies as the examples of inference rules to reduce the indefiniteness.

We believe that various inference mechanisms developed already in deductive database areas can be incorporated in this IP framework easily due to its inherent properties based on the first order logic. As an another application, this can serve in building interface for relational DB framework to support incomplete data.

Though we did not mention the extended relational operators for the IP construct, it is indispensable to design these operators. We will leave them having some necessary properties to further research. The properties are, if suggested a few, faithfulness, adequacy and precious generalization according to [16].

## References

[1] ANSI/X3/SPARK, Study Group on DBMS Interim Report, ACM SIGMOD FDT BULL., Vol. 7, No. 2, 1975.

[2] S. Abiteboul and G. Grahne, Updata Semantics for Incomplete Databases, Proc. of VLDB, Stockholm, 1985, pp. 1–12.

[3] Bishop, C., On taxonomies. Tech. Rep. Dept. of Computer Science. U. of British, Comumbia, 1980.

[4] C.L. Chang and R.C.T. Lee, Symbolic Logic and Mechanical Theorem Proving, Academic Press, New York, 1973.

[5] E.F. Codd, Extending the Database Relational Model to Capture More Meaning, ACM TPDS. Vol. 4, No. 4, December 1979, pp. 397–434.

[6] C.J. Date, An Introduction to Database Systems, Vol. II, Addison-Wesley, 1983.

[7] H. Gallaire, Logic and Databases, Plenum Press, New York, 1984.

[8] J. Grant and B.E. Jacobs, On the Family of Generalized Dependency Constraints, J. ACM, Vol. 29, No. 4, October 1982, pp. 986–997.

[9] D. Hilbert and Ackermann, W., Principle of Mathematical Logic, Chelsea, New York, 1950.

[10] T. Imielinski, Query Processing in Deductive Database with Incomplete Information, ACM Proc. of SIGMOD'86, 1986, pp. 268–280.

[11] T. Imielinski and W. Lipski, On Representing Incomplete Information in a Relational Databases, Proc. 7th Int. Conf. on VLDB, IEEE, New York, 1981, pp. 389–397.

[12] A.M. Keller and M.W. Wilkins, On the Use of an Extended Relational Model to Handle Changing Incomplete Information, IEEE, Transactions on SE, July 1985.

[13] H.J. Levesque, The Logic of Incomplete Knowledge Bases, in On Conceptual Modelling, M.L. Brodie, J. Mylopoulos and, J.W. Schmidt, Eds., Springer-Verlag, 1984, pp. 191–238.

[14] W. Lipski, On Semantic Issues Connected with Incomplete Information Databases, ACM TODS Vo. 4, No. 3, September 1979, pp. 262–296.

[15] W. Lipski, On Database with Incomplete Information, J. ACM, Vol. 28, No. 1, January 1981, pp. 41–70.

[16] D. Maier, The Theory of Relational Databases, Computer Science Press, 1983.

[17] J.R. Mcskimin, The Use of Semantic Information in Deductive Question Answering Systems, Tech. Rep. TR-506. Dept. of CS, U. of Maryland, 1977.

[18] J. Minker, L. Henschen and J. Grant, Deductive Databases - Theory and Applications.

[19] S. Park, Incomplete Relational Model for Formal Treatment of partial Information, Ph.D. Dissertation, KAIST, Dept. of Computer Science, Seoul, Korea, 1983.

[20] R. Reiter, Towards a Logical Reconstruction of Relational Databases Theory, in On Conceptual Modelling, M.L. Brodie, J. Mylopoulos and J.W. Schmidt, Eds., Springer-Verlag, 1984, pp. 191–238.

[21] R. Reiter, A Sound and Sometimes Complete Query

Evaluation Algorithm for Relational Databases with Null Values, J. ACM, Vol. 33, No. 2, April 1986, pp. 349–370.

[22] J.P. Tremblay and R. Manohar, Discrete Mathematical Structures with Applications to Computer Science, McGraw-Hill, 1975.

[23] Y. Vassiliou, Functional Dependencies and Incomplete Information, Proc. 6th Int. Conf. on VLDB, IEEE, New York, 1980, pp. 260–269.

[24] M. Winslett, A Model Based Approach to Updating Databases With Incomplete Information, ACM TODS, Vol. 13, 1988, pp. 167–196.

[25] L. Yan Yuan and Ding An Chiang, A Sound and Complete Query Evaluation Algorithm for Relational Databases with Null Values, ACM, 1988, pp. 74–81.
