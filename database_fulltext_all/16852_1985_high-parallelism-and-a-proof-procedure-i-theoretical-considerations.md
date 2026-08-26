---
otero_id: 16852
otero_key: "8EYWZM8F"
title: "High parallelism and a proof procedure I: Theoretical considerations"
authors: "C.-H. Kung"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90172-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# High Parallelism and a Proof Procedure

# I: Theoretical Considerations

C.-H. KUNG

Dept. Computer Science, The Norwegian Institute of Technology, Trondheim-NTH, Norway

This paper presents the theoretical basis of a proof procedure, which allows a high degree of parallel processing. The theoretical method is based upon the works of Prawitz's improved proof procedure and Robinson's unification algorithm. The input to the method is a set of clauses (or alternatively, well-formed formulae). The output of the method is the solution to the problem, if it exists. To overcome the inefficiency of the theoretical approach, we outline the main steps of a practical proof procedure. Besides parallel processing, the proof procedure works with bit manipulation rather than symbol manipulation as found in most of the existing proof mechanisms.

Keywords: First order logic; Proof method; Theorem proving; Inconsistency; Logic programming; Artificial intelligence; Problem-solving; Resolution principle; Unification; PROLOG; Parallelism; Fifth generation computer system; NP-completeness.

![](/api/attachments/8EYWZM8F/fulltext/images/15d46cfc0527782a8e126724ef1b584a0d4cfe0acaf42cb576d8164140db2c76.jpg)

Chen-Ho Kung is currently a visiting researcher at Department of Computer Science, The Norwegian Institute of Technology (NTH), Trondheim. He received a Ph.D. in Computer Science at NTH. Publications have been mainly in information systems and database management. Research interests include conceptual modeling, temporal logic, information systems specification and verification, and automated theorem-proving. He has recently been invited to the memberships of IFIP WG2.6 on data bases and IFIP WG8.1 on information systems design and evaluation.

## 1. Introduction

During the last decade, rapid progress in computer hardware technology has made parallel processing on a number of physical processors attractive and feasible. On the one hand, robotic and other applications of problem-solving require rapid reasoning of the robot for a number of reasons. On the other hand, existing theorem proving mechanisms provide only a limited degree of parallel processing; e.g., the resolution principle and PROLOG. Besides this, the resolution method provides no systematic way of reasoning in the sense that 'trial and error' process cannot be largely avoided. For efficiency considerations, a certain amount of 'heuristic' information must be provided in the search process to conduct the problem-solving in order to reduce unnecessary resolutions.

The resolution method can be characterized as follows:

\- Sequential process in nature because many resolution steps depend on the results of previous steps.

\- Blind search cannot be largely voided even if heuristic information is provided. Note that only very limited simplification strategies can generally be applied. For each particular application, specific heuristics must be given for efficiency account. From a software engineering point of view, the preparation and evaluation of the heuristics involves cost.

\- Extensive symbol manipulation because the whole process of resolution is performed by seeking unifiable literals and producing resolvents. As a consequence, both the parent clauses and their resolvent must be stored unless we know beforehand that they will not be used later.

As a particular implementation of the resolution principle, PROLOG suffers from the following:

\- Sequential in nature although ‘restricted parallelism’ exists.

\- It requires 'clever programming' or the program may never terminate as it should. For instance, the order of the PROLOG statements is important in most releases. The CUT feature in PROLOG encourages the programmers to be ingenious in managing the particular way in which PROLOG develops the basic tree construction [25]. Moreover, the order of the literals of a clause is also important, e.g., for recursive rules.

\- PROLOG statements must be Horn clauses, which might not be attractive in some cases. For instance, we cannot express directly the statement: every student is either a boy or a girl, i.e., $\tilde{\text{STUDENT}}(x) \vee \text{BOY}(x) \vee \text{GIRL}(x)$ .

For a more thorough and thoughtful comment on PROLOG, see [25].

Other interesting proposals on mechanization of theorem-proving are found in [1-3, 5, 6, 9, 18], etc.. Works by Bibel in [5], [6] and [7] have similarity with our current work. The major difference is that Bibel's approach tries one possibility at a time and hence backtracking remains. The second difference is that Bibel's approach allows work on the original formula instead of disjunctive normal form. However, we would like to stress that modification of our approach will be able to prove theorems in their original form.

In [9], the authors claimed that a formula on which Gilmore's routine for the IBM 704 caused the machine to compute for 21 minutes without obtaining a result. The same formula was worked successfully by hand computation using their method in 30 minutes. We have tried the same example by hand computation, it turned out that the solution was found in 10 minutes.

It is beyond the scope of this paper to conduct a feature analysis between our approach and the existing ones. However, we would like to stress the following features for the approach:

\- Due to Prawitz's work [21], our approach reasons in a systematic manner in the sense that each computation contributes to the final solution of the problem. As a consequence, no backtracking is needed.

\- It allows a very high degree of parallelism in the sense that each subtask can be separately assigned to a physical processor. Sequential processing can be limited to a very small amount of 'administrative' or 'coordinating' work among the processors.

\- No programming (up to declaration of non-logic symbols) is required and hence no heuristics is needed. The input to the proof procedure is the set of clauses (or well-formed formulae) and the output of the procedure is the solution to the problem (provided that the solution exists).

\- Instead of symbol manipulation, most part of our approach can be implemented as bit manipulation, which will be much faster than the former. Further, storage requirement can be kept to minimal.

The layout of the paper is as follows. Section 2 presents the theoretical basis of the proof procedure to be outlined in section 3. The theoretical approach is a combination of Prawitz's work [21] and the unification concept [23]. Section 3 sketches the practical proof procedure. We leave the details of the procedure to another report [16]. Performance issues will not be detailed in this paper. For assumptions on logic with or without equality, we refer the reader to [24]. We assume that the reader is familiar with mathematical logic notions and denotations. For references to mathematical logic and other relevant topics, see [4,8,19,26].

## 2. The Theoretical Approach

Based upon the work of Prawitz [21], we formulate an improved method for testing the inconsistency of a set of wffs in clause form [19]. We assume that different clauses use different sets of variables. This can be easily achieved by renaming.

It should be pointed out that in 1969, Prawitz reformulated his approach in terms of ideas in model theory, see [22]. However, this later work does not give essential improvement over the original approach except that some 'matrix reduction' mechanism is used. (The reader should not confuse Prawitz's matrix reduction with the Boolean matrices in section 3 of this paper.) Our general comment on [22] is as follows:

(a) It did not provide an efficient way of finding out the possible assignments of elements from the Herbrand universe to the variables. The incorporation of the unification mechanism in our approach makes it more efficient and general than that in [22].

(b) The implementation remained inefficient in the sense that enumeration of all the possible combinations of literals was adopted. The use of matrix reduction attempted to reduce the effort. However, we believe that the gain would be limited. Note that our theoretical approach suffers from the inefficiency of the enumeration. However, the practical approach outlined in section 3 has avoided this.

For an analysis of the correspondence between our theoretical approach and that in [21], see [12].

To facilitate understanding, we will use the following example (which can be shown to be inconsistent):

C1: \~WF(u, Chief-manager) ∨ WF(Tom, u)
Tom works for anybody who works for the Chief-manager.

C2: $\tilde{\mathrm{WF}}(x, x) \vee \tilde{\mathrm{WF}}(y, x)$ Nobody works for any body who works for himself.

C3: WF(Tom, Chief-manager)
Tom works for the Chief-manager.

Our approach is presented as follows:

Step 1: Let $S = \{C_1, C_2, \ldots, C_n\}$ be a set of clauses, where each $C_i$ , $i = 1, \ldots, n$ , is of the form $\alpha_{i1} \vee \alpha_{i2} \vee \ldots \vee \alpha_{im(i)}$ where $\alpha_{ij}$ , $j = 1, \ldots, m(i)$ , is a literal. That is, $\alpha_{ij}$ is either an atomic formula or the negation of an atomic formula. (In section 3, we use $C_i = \{\alpha_{i1}, \ldots, \alpha_{im(i)}\}$ )

to denote the disjunction form as defined here. There should be no significant difference except explanation convenience). If $m(i)=0$ for some i, then S contains an empty clause and hence S is inconsistent. Otherwise, define the disjunction normal form of $C_{1}\&\ldots\&C_{n}$ as the origin formula OF. If OF contains a disjunction clause which contains an atomic formula as well as the negation of the same atomic formula, then the entire disjunction clause can be removed from OF without affecting the consistency of S. Because of this, we will assume in the sequel that OF contains no such disjunction clause.

The OF for our example is:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\tilde{\mathrm{WF}}(\mathrm{u},\text{Chief-manager}) \&amp; \tilde{\mathrm{WF}}(x,x)$ $\&amp; \mathrm{WF}(\mathrm{Tom},\text{Chief-manager})$ $\vee \tilde{\mathrm{WF}}(\mathrm{u},\text{Chief-manager}) \&amp; \tilde{\mathrm{WF}}(y,x)$ $\&amp; \mathrm{WF}(\mathrm{Tom},\text{Chief-manager})$ $\vee \mathrm{WF}(\mathrm{Tom},\mathrm{u}) \&amp; \tilde{\mathrm{WF}}(x,x)$ $\&amp; \mathrm{WF}(\mathrm{Tom},\text{Chief-manager})$ $\vee \mathrm{WF}(\mathrm{Tom},\mathrm{u}) \&amp; \tilde{\mathrm{WF}}(y,x)$ $\&amp; \mathrm{WF}(\mathrm{Tom},\text{Chief-manager})$
</div>

Step 2: The following steps are performed cyclically. In cycle t we mark every variable of the origin formula OF by superscribed t. The resulting formula is denoted as $OF_{t}$ . That is, the $OF_{1}$ of our example is

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\tilde{\text{WF}}(\text{u}^1, \text{Chief-manager}) \&amp; \tilde{\text{WF}}(\text{x}^1, \text{x}^1) \&amp; \text{WF(Tom, Chief-manager)}$ $\vee \tilde{\text{WF}}(\text{u}^1, \text{Chief-manager}) \&amp; \tilde{\text{WF}}(\text{y}^1, \text{x}^1) \&amp; \text{WF(Tom, Chief-manager)}$ $\vee \text{WF(Tom, u}^1) \&amp; \tilde{\text{WF}}(\text{x}^1, \text{x}^1) \&amp; \text{WF(Tom, Chief-manager)}$ $\vee \text{WF(Tom, u}^1) \&amp; \tilde{\text{WF}}(\text{y}^1, \text{x}^1) \&amp; \text{WF(Tom, Chief-manager)}$
</div>

Step 3: Form the t-th cycle formula $CF_{t}$ as follows. $CF_{1}$ is $OF_{1}$ which has been defined above. If the s-th cycle formula is $CF_{s}$ then the $(s+1)$ -th cycle formula is $(CF_{s} \& OF_{s+1})$ transformed into disjunctive normal form.

Step 4: If there is a disjunction clause of $\mathbf{CF}_t$ in which no literal is unifiable with the negation of any other literal, then $S$ is consistent. This proposition can be proved as follows:

Proof

Suppose that there is such a disjunctive clause of $\mathbf{CF}_t$ , let it be:

$$
\alpha_ {1 k 1} ^ {t} \& \dots \& \alpha_ {n k n} ^ {t}
$$

Then there must be the disjunction clause:

$$
\alpha_ {1 k 1} ^ {1}, \& \dots \& \alpha_ {n k n} ^ {1},
$$

in $\mathbf{CF}_1$ . A model of $S$ will be:

$$
\left\{\alpha_ {i k i} ^ {1} \Theta : \alpha_ {i k i} ^ {1} \Theta \in \bigcup H (S) \right\}, \quad i = 1, \dots , n
$$

where $H(S)$ is the Herbrand expansion of S and $UH(S)$ is the set of all literals appearing in clauses of $H(S)$ . $\Theta$ is any substitution. E.Q.

If there is no such a disjunction clause as described above, we continue. We associate an identity condition $IC_{i}$ with every disjunctive clause $M_{i}$ of $CF_{i}$ as follows:

(1) If $M_{i}$ contains two formulae one of which is the negation of the other, then $IC_{i}$ is $c_{1}=c_{1}$ ;

(2) If $\mathbf{M}_i$ is not as in (1), then for every couple of literals in $\mathbf{M}_i$ , we examine if one of them is unifiable with the negation of the other. We then form the identity list IL as follows:

If $\alpha_{i}$ and $\tilde{\beta}_{i}$ of $\mathbf{M}_{i}$ is unifiable, and $\Theta$ is the most general unifier for $\alpha_{i}$ and $\tilde{\beta}_{i}$ , then the identity list is simply $\Theta$ . For most general unifier (mgu), see [19].

$IC_{i}$ is to be the disjunction of all the $n_{i}$ identity lists. $n_{i}$ is supposed to be the number of couples of literals in $M_{i}$ such that one of which can be unifiable with the negation of the other.

As an illustration, our example in cycle 1 has the following four disjunction clauses $\mathbf{M}_1$ , $\mathbf{M}_2$ , $\mathbf{M}_3$ , and $\mathbf{M}_4$ :

$M_{1}$ : $\tilde{\mathrm{WF}}(\mathbf{u}^{1}, \text{Chief-manager})$ & $\tilde{\mathrm{WF}}(x^{1}, x^{1})$ & WF(Tom, Chief-manager)

$M_{2}$ : $\tilde{\mathrm{WF}}(\mathbf{u}^{1}, \text{Chief-manager})$ & $\tilde{\mathrm{WF}}(y^{1}, x^{1})$ & WF(Tom, Chief-manager)

$M_{3}$ : $\mathrm{WF(Tom,u^{1})\&~\tilde{WF}(x^{1},x^{1})\&~WF(Tom,Chief-manager)}$

$M_{4}$ : WF(Tom, $u^{1}$ ) & $\tilde{WF}(y^{1}, x^{1})$ & WF(Tom, Chief-manager)

In what follows, we will denote the mgu in the form of identity. For example, the mgu for $\tilde{\mathrm{WF}}(\mathbf{u}^1$ , Chief-manager) & WF(Tom, Chiefmanager) of $\mathbf{M}_1$ is denoted as $\mathbf{u}^1 = \mathbf{Tom}$ .

It will be clear in the sequel that such a treatment will cause no problem in our approach. The identity conditions for the $M_{i}$ , $i = 1, \ldots, 4$ , are as follows:

$$
\mathbf {I C} _ {1}: \mathbf {u} ^ {1} = \mathbf {T o m}
$$

$$
\begin{array}{r l} \mathrm{IC} _ {2}: & (\mathrm{u} ^ {1} = \text { Tom }) \vee (x ^ {1} = \text { Chief - manager } \& y ^ {1} \\ & = \text { Tom }) \end{array}
$$

$$
\begin{array}{l} \mathbf {i C} _ {3}: x ^ {1} = \text { Tom } \& u ^ {1} = x ^ {1} \\ \mathbf {I C} _ {4}: (y ^ {1} = \text { Tom } \& u ^ {1} = x ^ {1}) \vee (x ^ {1} = \text { Chief - } \\ \text { manager } \& y ^ {1} = \text { Tom }) \end{array}
$$

Intuitively, $IC_{1}$ indicates that under the substitution of Tom to $u^{1}$ (or under the condition that $u^{1} = Tom$ ) $M_{1}$ will be false. $IC_{2}$ indicates that either substituting Tom for $u^{1}$ or substituting Chief-manager for $x^{1}$ and Tom for $y^{1}$ will make $M_{2}$ become false. We can similarly interpret $IC_{3}$ and $IC_{4}$ . Clearly, if there is a combination of one identity list from each $IC_{i}$ such that there exists no contradictory assignment (to be defined below in step 5) of terms to variables then each of the $M_{i}$ will be false. That is, the disjunction of the $M_{i}$ will also be false which in turn indicates that the set S of clauses is inconsistent.

Step 5: S can be confused (i.e., proved to be inconsistent) in cycle s iff the conjunction of the identity conditions:

$$
\begin{array}{r l} \mathrm{IC} _ {1} & \& \mathrm{IC} _ {2} \& \dots \& \mathrm{IC} _ {r} \\ & = (\mathrm{IL} _ {1 1} \vee \dots \vee \mathrm{IL} _ {1 n 1}) \& \dots \\ & \& (\mathrm{IL} _ {r 1} \vee \dots \vee \mathrm{IL} _ {r n r}) \end{array}
$$

where, $r = m_1^* \ldots^* m_n$ , contains a disjunction clause:

$$
\mathrm{IL} _ {1 q 1} \& \mathrm{IL} _ {2 q 2} \& \dots \& \mathrm{IL} _ {r q r}\tag{9}
$$

$$
\left(\text { where } 1 \leqslant q 1 \leqslant n _ {1}, 1 \leqslant q 2 \leqslant n _ {2}, \dots , 1 \leqslant q r \leqslant n _ {r}\right)
$$

which does no violate the following restriction:

Restriction: If $x^{i}=t_{1}$ and $x^{i}=t_{2}$ can be derived from step (9), where $i\leqslant s$ and $t_{1}$ and $t_{2}$ are terms, then $t_{1}$ and $t_{2}$ must agree. $t_{1}$ and $t_{2}$ do not agree if either of the following holds; otherwise, $t_{1}$ and $t_{2}$ are said to agree:

(1) $t_1$ and $t_2$ are two different constant symbols.

(2) $t_1 = y$ and $t_2 = f(\ldots, y, \ldots)$ , where $y$ is a variable introduced in some cycle and $f$ is a function symbol.

(3) $t_1$ is a constant symbol and $t_2 = f(\ldots)$ , where $f$ is a function symbol.

(4) $t_1 = f(\ldots)$ and $t_2 = g(\ldots)$ and $f \neq g$ .

(5) $t_1 = f(t_{11}, \ldots, t_{1k})$ and $t_2 = f(t_{21}, \ldots, t_{2k})$ and some pair $\langle t_{1j}, t_{2j} \rangle$ , $j = 1, \ldots, k$ , do not agree.

It can be proved that the above restriction is essentially the same restrictions defined by Prawitz in [21].

If $S$ cannot be confused in cycle $s$ , then we start another cycle.

This finishes the presentation of our theoretical approach.

As an illustration, we see that:

$$
\begin{array}{l} \mathbf {u} _ {1} = \text { Tom   from } \mathbf {I C} _ {1} \text { and } \\ \mathbf {u} _ {1} = \text { Tom   from } \mathbf {I C} _ {2} \text { and } \\ \mathbf {u} _ {1} = x _ {1} \& x _ {1} = \text { Tom   from } \mathbf {I C} _ {3} \text { and } \\ \mathbf {u} _ {1} = x _ {1} \& y _ {1} = \text { Tom   from } \mathbf {I C} _ {4} \\ \text { implies: } \\ \mathbf {u} _ {1} = x _ {1} = y _ {1} = \text { Tom } \end{array}
$$

which does not violate the restriction defined above. This means that $\{C_{1}, C_{2}, C_{3}, C_{4}\}$ is inconsistent.

## 3. Implementation Considerations

The procedure that is presented in section 3 could be carried out in parallel by a number of processors. We might assign each disjunction clause $M_{i}$ of the t-th cycle formula $CF_{t}$ to a processor $CPU_{i}$ , which would investigate whether some $\alpha, \tilde{\beta} \in M_{i}$ are unifiable. As in Step 4, section 2, $CPU_{i}$ would return the identity condition $IC_{i}$ to the ‘administrative’ CPU, which may be one o the $CPU_{i}$ . The administrative CPU would then convert $IC_{1}$ & $IC_{2}$ & . . . & $IC_{r}$ into disjunctive normal form whose typical disjunctive clause is as in (9). It then would assign each such disjunctive clause to a $CPU_{j}$ to investigate whether the restriction is violated.

Obviously, this approach must be discarded since it is inefficient. Suppose that we are going to prove the inconsistency of $S = \{C_{1}, \ldots, C_{n}\}$ , where $C_{i}$ contains $m_{i}$ literals. There will be $m_{1}^{*}m_{2}^{*}\ldots^{*}m_{n}$ disjunctive clauses in $CF_{1}$ . Our study shows that many identity lists in the $IC_{i}$ are repeated. This means that tremendous work has been duplicated by the $CPU_{i}$ which in turn complicates the task of detecting possible violations in Step 5.

In this section, we outline a procedure which can be of practical use. The procedure runs cyclically until an inconsistency is detected. This outline is meant to convey the 'favour' without dealing with most of the details. We plan to explain the ideals behind the procedure in another report [16], which will give other useful techniques and more complicated examples.

(1) Let $S = \{C_1, \ldots, C_n\}$ be the set of clauses which is to be proved to be inconsistent. We assume that each $C_i$ is a set of $m_i$ literals (see step 1 in section 2). Let $P_1, \ldots, P_m$ be the predicate symbols that appear in $S$ . That is, if $P(x), \tilde{Q}(a)$ are literals of $S$ , then $P, Q$ are predicate symbols of $S$ .

As an example, we assume the following set S of clauses:

$$
\begin{array}{l} \mathsf {C} _ {1} \colon \mathsf {\tilde {C}} (x) \vee \mathsf {G} (x) \\ \mathsf {C} _ {2} \colon \mathsf {\tilde {G}} (u) \vee \mathsf {C} (u) \\ \mathsf {C} _ {3} \colon \mathsf {C} (a) \\ \mathsf {C} _ {4} \colon \mathsf {\tilde {C}} (b) \\ \mathsf {C} _ {5} \colon \mathsf {G} (b) \end{array}
$$

where $C(x)$ might mean that x is a cat which catches mouse, and $G(x)$ might mean that x is a good cat. Thus, $C_{1}$ says that any cat is a good cat if it catches mouse. $C_{3}$ , $C_{4}$ and $C_{5}$ respectively records the facts that a is a cat which catches mouse, b does not catch mouse and b is a good cat. Finally, $C_{2}$ might be interpreted as the negation of a query to the 'database'. The query asks list all good cats which do not catch mouse', i.e., $G(u)$ & $\tilde{C}(u)$ . All the assignments of values to u which make S inconsistent will be the response to the query.

(2) Form a Boolean matrix $M^{+}$ (resp. $M^{-}$ ) such that $M_{i,j}^{+}=1(M_{i,j}^{-}=1)$ iff $P_{j}\left(\tilde{P}_{j}\right)$ appears in $C_{i}, j=1,\ldots,m$ and $i=1,\ldots,n$ . Clearly, this step has linear computation time.

The $M^{+}$ and $M^{-}$ for our simple example is shown in Fig. 1 below.

![](/api/attachments/8EYWZM8F/fulltext/images/86a9f3e9a9e881c0e10e9e528be3b02e49f9f0927e2a0d634f6d54bf5f9b4e4f.jpg)  
Fig. 1. The Boolean matrices of the example

(3) Compute $M = M^{+*}(M^{-})^{\mathrm{T}}$ , where $M_{ij} = 1$ iff for some $k = 1, \ldots, m$ such that $M_{ik}^{+} = 1$ and $M_{kj}^{-} = 1$ , $i, j = 1, \ldots, n$ . The computation is of polynomial time. The matrix $M$ for our example is shown in Fig. 2.

(4) For each entry $M_{ij} = 1$ or $M_{ji} = 1$ , assign $C_i$ , $C_j$ to a CPU, say $CPU_{ij}$ . (Alternatively, we may also assign several such pairs to one CPU, there is no significant difference). The program on $CPU_{ij}$ returns a list of pairs $\langle \{ik_i, jk_j\}, \Theta_{kikj}\rangle$ , where $\{ik_i, jk_j\}$ , called a pair of indices, indicates that the $k_i$ -th literal of $C_i$ is unifiable with the negation of the $k_j$ -th literal of $C_j$ with $\Theta_{kikj}$ as the most general unifier. We assume that the literals of a clause is ordered from the left to the right. Further, without losing generality, we may assume that $\Theta_{kikj}$ is of the form $v_1 = t_1 \& \ldots \& v_r = t_r$ , where $v_q$ is a variable introduced in some cycle and $t_q$ is a term, for $q = 1, \ldots, r$ . $CPU_{ij}$ returns an empty list otherwise. If all the 'operators' (i.e., functions) in $S$ are noncommutative, then this step runs in polynomial time [11].

The resultant lists for the example is as follows (Fig. 3), where columns 2, 3 and 4 are to be explained in steps (6) and (7).

(5) Suppose that in total $r$ pairs $\langle p_1, \Theta_1 \rangle, \ldots, \langle p_r, \Theta_r \rangle$ are returned from all $\mathbf{CPU}_{ij}$ , where recalling the last paragraph, $p_q$ is of the form $\{i_q k_{iq}, j_q k_{jq}\}$ . For our example, $r = 5$ and $p_1 = \{11, 22\}$ , $p_2 = \{12, 21\}$ , $p_3 = \{22, 41\}$ ,

$$
M = M ^ {+} * (M ^ {-}) ^ {T} = \left[ \begin{array}{c c c c c} C 1 & C 2 & C 3 & C 4 & C 5 \\ & 1 & & & \\ 1 & & & 1 & \\ 1 & & & 1 & \\ & & & & \\ & 1 & & & \end{array} \right] \begin{array}{l} C 1 \\ C 2 \\ C 3 \\ C 4 \\ C 5 \end{array}
$$

Fig. 2. The matrix M of the example

<table><tr><td>List of pairs</td><td>toc</td><td>poc</td><td>toc - poc</td></tr><tr><td> $\langle \{11,22\},x=u\rangle$ </td><td>1</td><td>1</td><td>0</td></tr><tr><td> $\langle \{12,21\},x=u\rangle$ </td><td>1</td><td>1</td><td>0</td></tr><tr><td> $\langle \{22,41\},u=b\rangle$ </td><td>2</td><td>1</td><td>1</td></tr><tr><td> $\langle \{11,31\},x=a\rangle$ </td><td>2</td><td>1+1</td><td>0</td></tr><tr><td> $\langle \{21,51\},u=b\rangle$ </td><td>2</td><td>1+1</td><td>0</td></tr></table>

Fig. 3. Pairs returned from the CPU's and the relevant numbers

$p_{4} = \{11, 31\}$ and $p_{5} = \{21, 51\}$ . Form an $r \times r$ Boolean matrix $A$ such that $A_{pq} = 1$ iff:

$\left[\mathrm{COM}(k_{ip}) \cup \mathrm{COM}(k_{jp})\right]$ and $\{\mathbf{i}_{\mathbf{q}} \mathbf{k}_{\mathbf{i}\mathbf{q}}, \mathbf{j}_{\mathbf{q}} \mathbf{k}_{\mathbf{j}\mathbf{q}}\}$ contains no common element

where $\mathrm{COM}(k_{ip})$ denotes the set of indices of clause $i_{p}$ except $i_{p}k_{ip}$ . Clearly, A is reflexive and symmetric so we only have to compute the left lower triangle. Moreover, A divides the set $\Gamma=\{p_{1},\ldots,p_{r}\}$ of pairs of indices into a number of maximal compatibility blocks $B_{h}$ such that:

$$
\begin{array}{l}(\forall x) (\forall y) (x, y \in B _ {h} \rightarrow x R y) \text { and }\\\tilde {} (\exists x) (x \in \Gamma - B _ {h} \&\tilde {} (\exists y) (y \in B _ {h} \&\tilde {} (x R y)))\end{array}
$$

where R denotes the reflexive and symmetric relation defined by A. For more about maximal compatibility blocks and the algorithm for computing them, see [26]. This step runs in polynomial time.

![](/api/attachments/8EYWZM8F/fulltext/images/26e34c579076088547230244b268281bc115b181b2593e186f5cc6c998c08aae.jpg)  
Fig. 4a. The compatibility relation R

![](/api/attachments/8EYWZM8F/fulltext/images/6cb7ff46407aede96859413a2e9fe7c3b77d098315ea991896a9723a57bcfe37.jpg)  
Fig. 4b. The maximal compatibility blocks

Alternatively, the maximal compatibility blocks can also be computed by using a graph theoretical method.

Figure 4a represents compatibility relation R, where nodes $n_{i}$ and $n_{j}$ is connected by an arc iff $n_{i} \cup n_{j}$ contains no two different indices from the same clause. Figure 4b gives the maximal compatibility blocks of our simple example. That is, all the nodes of a maximal complete subgraph forms a maximal compatibility block. A complete subgraph is defined as a subset of nodes, where any two nodes of the subset are connected.

(6) Compute the number of theoretical occurrences (toc) and the number of practical occurrences (poc) for each pair of indices. Let $p_{q}=\{ik_{i},jk_{j}\}$ be a pair of indices returned by some CPU in step 4. The toc of $p_{q}$ is computed as follows:

$$
\operatorname{toc} (p _ {q}) = \left(m _ {1} ^ {*} \dots^ {*} m _ {n}\right) / \left(m _ {i} ^ {*} m _ {j}\right)
$$

Note that the toc-values can be computed by the subordinary CPUs in step (4).

Let $C_{i1}, \ldots, C_{iq}$ be the clauses whose literals have indices appear in $B_h$ . The poc of $B_h$ is then: $\text{poc}(B_h) = (m_1^* \ldots^* m_n)/(m_{i1}^* \ldots^* m_{iq})$ .

The poc of $p_{q}$ is the sum of the poc-values of all the $B_{h}$ -values in which $p_{q}$ appears.

(7) Let $\operatorname{toc}_k$ and $\operatorname{poc}_k$ be associated with $p_k$ . If $(\operatorname{toc}_k - \operatorname{poc}_k) > 0$ , then add $\{p_k\}$ to the set of $B_h$ 's the poc of $\{p_k\}$ is $(\operatorname{toc}_k - \operatorname{poc}_k)$ . This step is performed with respect to all $p_k$ -values. The resulting set of blocks is denoted by $Z$ . This step runs in polynomial time. From Fig. 3, we see that $\operatorname{toc}_3 - \operatorname{poc}_3 = 1 > 0$ , which introduces $B_4 = \{22, 41\}$ as an additional block.

(8) Find out whether there is a non-contradictory assignment of terms to variables. Let $Z = \{z_1, \ldots, z_q\}$ , where each $z_k$ is of the form $z_k = \{\{p_{k1}\}, \ldots, \{p_{kj}\}\}$ for some $j, \{p_{kg}\}, 1 \leqslant g \leqslant j$ , denotes a set of pairs of indices. If $(m_1^*, \ldots^* m_n - \text{SUM}(\text{poc}_i)) > 0$ , where $z_i \in Z$ for $i = 1, \ldots, q$ , then $S$ is consistent and the procedure stops. Otherwise we continue. Recall from step 4, associated with each $p_{kg}$ there is a conjunction of identities $\Theta_{kg}$ of the form $v_1 = t_1 \& v_2 = t_2 \& \ldots \& v_r = t_r$ . Thus each $z_k$ is associated with a set $\Psi_k$ of $\Theta_{kg}$ . To find out whether there is a non-contradictive tory assignment, we can use the following methods (more efficient methods will appear in another report [16]):

(a) Compute the Cartesian product of $\Psi_1 \times \ldots \times \Psi_q$ . Assign each element $\langle \mathrm{IL}_{1k1}, \ldots, \mathrm{IL}_{qkq} \rangle$ of the Cartesian product to a processor for evaluation. The processor simply forms the conjunction $\mathrm{IL}_{1k1} \& \ldots \& \mathrm{IL}_{qkq}$ and examines if it implies a contradictory assignment. This method can be used for small problems.

(b) For bigger problems, we may partition the $\Psi_{k}$ into several groups. Compute each group by using a processor, which will return a set of non-contradictory combinations (having not many elements) and we repeat the process in a similar manner.

(c) For even large problems, we may partition the $\Psi_{k}$ and process each group step by step, where each step is performed on a number of processors, and then synthese the results in a similar way.

If some assignments can be evaluated to be non-contradictory according to the Restriction as defined in section 2, then each of these assignments gives a solution to the problem. In this case, the procedure successfully stops. Otherwise, we continue.

(9) Let $C_{i1}, \ldots, C_{ir}$ be those clauses of S whose variables have been contradictorily assigned terms. For example, $x^{j} = c_{1} \& x^{j} = c_{2}$ and $c_{1} \neq c_{2}$ , where $c_{1}$ and $c_{2}$ are constant symbols, and j denotes some cycle index (see Step 2 of section 2). Another example could be that $x^{j} = f(\ldots, x^{j}, \ldots)$ where f is a function symbol. If the process is in cycle t - 1, then we augment S by:

$$
S = S \cup \left\{\mathbf {C} _ {i k} \left(x _ {1} ^ {\prime}, \dots , x _ {n k} ^ {\prime}\right): k = 1, \dots , r \right\}
$$

where $n_{k}$ is the number of variable symbols of $C_{ik}$ ; Goto step (1).

There is an efficient mechanism for evaluating each $IL_{1k1}$ &... $IL_{qkq}$ and for determining those $C_{ik}$ whose variables are contradictorily assigned. We plan to publish these in [16]. As an illustration, we may group our four blocks:

B1: $\{\{21,51\},\{11,31\}\}$

B2: $\{\{11, 22\}, \{11, 31\}, \{22, 41\}\}$

B3: $\{\{12, 21\}, \{21, 51\}\}$ and

B4: { {22, 41}}

into two groups {B1, B3} and {B2, B4} since both B1 and B3 contain {21, 51}, and both B2 and B4 contain {22, 41}. Obviously, the most general unifier associating with {22, 41} has to be included for consideration in step (8) because B4 contains only that element. Thus, picking up the same element from B2 will be more likely to give a solution than picking up either {11, 22} or {11, 31} from B2. Therefore, we grouped B2 and B4 together. Grouping B1 and B3 together can be explained as follows. Since {21, 51} appears in both B1 and B3, it will be more likely to result in a solution if we pick up this common element for evaluation. If the most general unifier associating with {21, 51} is in conflict with that of {22, 41}, then there remains only one more possibility, i.e., picking up {11, 31} from B1 and {12, 21} rom B3. We see that grouping enables us to reduce the number of possible evaluations in step 8). That is, instead of evaluating

$$
\left| \mathrm{B} 1 \right| ^ {*} \left| \mathrm{B} 2 \right| ^ {*} \left| \mathrm{B} 3 \right| ^ {*} \left| \mathrm{B} 4 \right| = 1 2
$$

possible assignments of values to variables, we only have to evaluate 2 possibilities as shown in fig. 5 below, where u = b is the solution to the problem (or the answer to the data base query).

## 4. Future Work

In this paper, we have presented the theoretical basis of an efficient proof procedure, which has very high degree of parallelism as shown in section 3. The procedure operates on bit manipulation instead of symbol manipulation. Furthermore, it concentrates on finding the final solution to the problem by exhausting all the possibilities in an intelligent manner. Backtracking is not needed.

![](/api/attachments/8EYWZM8F/fulltext/images/7f0877bf23b8f7890751229b3acb1d3ea12ecc9f97de5579d79cb92c6a870ddf.jpg)  
Fig. 5. Evaluation of possible assignments

Therefore, we may speculate that the procedure will have much better performance than existing proof mechanisms. We plan to do the following:

(1) Performance evaluation by simulation. The purpose is to provide performance statistics for using the practical approach as outlined in section 3. Another purpose is to identify the bottlenecks to be implemented in VLSI.

(2) Derive a set of formulae for estimating the computing time and storage needed by the resolution method, by a PROLOG inference engine and by our practical approach, respectively. We expect that our practical approach will give better performance under the same environmental hypothesis.

(3) Investigate the possibility of providing more natural language like interface for input/output functions.

(4) Incorporate existing simplification strategies such as Robinson's purity principle, elimination by tautology, elimination by subsumptions, etc [20]. Moreover, other existing results in undecidability theory may also be incorporated into the practical approach to improved the performance, e.g., [12], [17]. We believe that such strategies can be easily incorporated into our approach.

(5) Explore the applicability of the practical approach to specific areas such as deductive databases, where thousands of relation tuples are involved [10]. However, the tuples of a relation scheme can be 'compressed' as a relation whose arguments are parameters. A 'compilation' approach can then be used instead of inferencing upon all the tuples. This will largely reduce the computation time and storage needed by our approach. We also plan to address the consistency (as opposed to inconsistency) problem in some future report as this problem has important applications in information systems and databases [13], [14], [15].

## Acknowledgement

In 1983, Dr. J.A. Ribonson made a casual visit to our department. He recommended the paper by

Prawitz [21] to me which leads to the theoretical approach. I wish to thank Dr. Robinson for this. I also want to thank Prof. Arne Solvberg for his guidance and encouragement. Thanks also to Jachim Kaisen and Heidi Pran for their stimulating and constructive discussions.

## References

[1] Andrews, P.B., Refutations by matings, IEEE Trans. Comput. c-25 (1976) pp. 801–807.

[2] Andrews, P.B., Theorem proving via general matings, J. ACM, 28 (1981) pp. 193–214.

[3] Andrews, P.B., On simplifying the matrix of a WFF, in: Automation of Reasoning, Siekman and Wrightson EDs., Vol. 2, pp. 102–115, Springer, New York (1983).

[4] Bell, J. and M. Machover, A Course in Mathematical Logic, North-Holland, Amsterdam, New York (1977).

[5] Bibel, W., On matrices with connections, J. ACM 28 (1981) pp. 663–645.

[6] Bibel, W., A comparative study of several proof procedures, Artif. Intell. 18 (1982) pp. 269–293.

[7] Bibel, W., Automated Theorem Proving, Vieweg, Wiesbaden (1982).

[8] Chang, C.C. and H.J. Keisler, Model Theory, North-Holland, Amsterdam, New York (1973).

[9] Davis, M. and H. Putnam, A computing procedure for quantification theory, J. ACM 7 (1960) pp. 201-215.

[10] Gallaire, H., J. Minker and J.-M. Nicolas, Logic and databases: a deductive approach, Comput. Surv. 16 (1984) pp. 153–185.

[11] Garey, M.R and D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, Bell Telephone Lab., Inc., Murray Hill NJ (1979).

[12] Kung, C.H., A Temporal Framework for Information Systems Specification and Verification, Ph.D Thesis, Dept. of Computer Science, The Norwegian Inst. of Tech., Trondheim, (1984).

[13] Kung, C.H., A temporal framework for database specification and verification Proc. 10th Int. Conf. VLDB, pp. 91–9, Singapore (Aug. 27–31, 1984).

[14] Kung, C.H., A tableaux approach for consistency checking, Proc. IFIP WG8.1 Working Conference on Theoretical and Formal Aspects of Information Systems (Sernadas, A. et al. eds) North-Holland, Amsterdam, New York (1985).

[15] Kung, C.H., On verification of database temporal constraints, Proc. ACM SIGMOD Ann. Conf. Management of Data, Austin TX (May 28–31, 1985).

[16] Kung, C.H., High Parallelism and a Proof Procedure II: Practical Considerations, Dept. Computer Science, The Norwegian Inst. of Technology, NTH-Trondheim (1985) in preparation.

[17] Lewis, H.R., Cycles of Unifiability and Decidability by Resolution, Aiken Computation Laboratory, Tech. Rept., Harvard Univ., Cambridge MA (1975).

[18] Maslov, S.Yu., An inverse method for establishing deducibility of Nonprenex formulas of the predicate calculus, in: Automation of Reasoning, (Siekman and Wrightson Eds, pp. 48–54, Springer, New York (1983).

[19] Nilsson, N.J., Problem-Solving Methods in Artificial Intelligence, McGraw-Hill, New York (1971).

[20] Nilsson, J., Principles of Artificial Intelligence, Springer, New York (1982).

[21] Prawitz, D., An improved proof procedure, Theoria 26 (1960) pp. 102–139.

[22] Prawitz, D., Advances and problems in mechanical proof procedures, Machine Intell. 4 (1969) pp. 59–71.

[23] Robinson, J.A., A machine-oriented logic based on the resolution principle, J. ACM 12 (1965) pp. 23–41.

[24] Robinson, J.A., An overview of mechanical theorem proving, in: Theoretical Approaches to Non-numerical Problem Solving Banerji, R. and M. Mesarovic Eds, pp. 2–20, Springer, New York, (1970).

[25] Robinson, J.A., Leading article: Logic programming - past, present and future, New General. Comput. (1983) pp. 107-124.

[26] Tremblay, J.P. and R. Manohar, Discrete Mathematical Structures with Applications in Computer Science, McGraw-Hill, New York (1975).
