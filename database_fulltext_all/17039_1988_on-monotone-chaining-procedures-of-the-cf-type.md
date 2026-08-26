---
otero_id: 17039
otero_key: "JCE95BD3"
title: "On monotone chaining procedures of the CF type"
authors: "Robert G. Jeroslow"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90127-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On Monotone Chaining Procedures of the CF Type

Robert G. JEROSLOW $^{1}$

College of Management, Georgia Institute of Technology, Atlanta, GA 30332-0520, USA

We study procedures in which revised estimates of variables are iteratively computed, from initially given estimates, via use of monotone functions. Under broad hypotheses, we show how to obtain the limit values, when these exist, by solving a single mixed integer program.

This result aids the computation of ‘measures of belief’ in procedures based on inexact reasoning, such as occur in some ‘expert systems’.

Keywords: Mixed Integer Programming, Representability, Expert Systems, Forward Chaining.

![](/api/attachments/JCE95BD3/fulltext/images/694731dd016f50a50aacb01baab6a8a898bc4c4fbad9ee45cfc1a181c8cf1456.jpg)

Robert G. Jeroslow is Professor in the College of Management at the Georgia Institute of Technology, and also Adjunct Professor in the School of Industrial and Systems Engineering. He received the B.S. in Industrial Engineering from Columbia University in 1964 and the Ph.D. in Mathematical Logic from Cornell University in 1969. His research interests are applied artificial intelligence, decision support systems, information systems, applied logic, knowledge representa-

tion for discrete optimization, operations management, strategic planning, and strategy.

$^{1}$ The author's research has been partially supported by National Science foundation grant MCS-8304075.

## 1. Introduction

We study procedures in which revised estimates of variables are iteratively computed, from initially given estimates, via use of monotone functions. The limiting values, if any, of the iterates is desired.

In section 2 we provide a treatment for the CF and MB concepts as used here, and review an earlier definition and result. In section 3, we set up notation, proceed to the main result, and conclude with comments and observations.

Under mild assumptions, primarily that the epigraph of the functions be representable by linear constraints in binary and continuous variables, we show that the limiting values can be obtained by solving a single mixed-integer program (MIP).

Our result was motivated by an MIP treatment for ‘certainty factors’ (CFs) and ‘measures of belief’ (MBs) in the inexact reasoning similar to that done in some of the ‘expert systems’ (ESs); see, e.g., [2], [7], [8] [13]. The result presented here (Theorem 3.1) generalizes that work, and further generalizations are sketched in subsequent remarks. Our result was first reported in [14].

## 2. CFs, MBs and MIPs

A measure of belief in a proposition B is a real number $y \in [0,1]$ which summarizes the evidence in favor of B from the facts known, ignoring contrary evidence. As such, an increase in data available cannot decrease y, although if evidence quite unfavorable to B becomes available, it would tend to increase the MB $y'$ of the proposition $\neg B$ ( $\neg B$ means: B is false). Finally, the certainty factor for B is computed as a function $j(y, y')$ of the MB y of B and the MB $y'$ of $\neg B$ .

A typical ‘production rule’ in some expert systems can read

$A_{1}$ with MB $y_{1}$ and...and $A_{r}$ with MB

$y_{r}\rightarrow B$ with MB $w$

(2.1)

in which w is given as a function of $y_{1},\ldots,y_{r}$

$$
w = g (y _ {1}, \dots , y _ {r}).\tag{2.2}
$$

Underpinning (2.1) conceptually is an ‘inexact inference’: $A_{1}$ and … and $A_{r}$ tend to imply B. Thus, more evidence for the $A_{i}$ intuitively means more evidence for B. Hence, it is natural for g to be monotone

$$
\begin{array}{r l}y _ {1}&\geqslant y _ {1} ^ {\prime} \text {   and   } \dots \text {   and   } y _ {r} \geqslant y _ {r} ^ {\prime} \rightarrow g (y _ {1}, \dots , y _ {r})\\&\geqslant g (y _ {1} ^ {\prime}, \dots , y _ {r} ^ {\prime}).\end{array}\tag{2.3}
$$

The most commonly-suggested functions $g$ have the form $g(y_1, \ldots, y_r) = \alpha \min_i y_i$ , where $0 \leqslant \alpha \leqslant 1$ is a constant. Indeed, such $g$ are monotone. These also reflect the conservative idea, that an inference is as strong as its 'weakest link'. In contrast, the function $h(y_i, \ldots, y_r) = \alpha \max_i y_i$ accepts the strongest premiss $A_i$ as determining the validity of the conclusion $B$ , and can be appropriate in some situations.

While a rule (2.1) is written, from the perspective of MB's only the functions (2.2) are essential. Generally, there are many rules of the form (2.1) with different $A_i$ , $B$ and $g$ . If more than one concludes $B$ , one takes the maximum over all possible MB's for $B$ (i.e., the strongest 'argument' for $B$ is accepted). In this manner, the MB's for all propositions can be revised from any given values, provided that for every proposition $B$ occurring in any rule, there is at least one rule which concludes $B$ . This latter condition can be assured by including rules of this form, where necessary

$$
B \text {   with   } \mathbf {M B} w \to B \text {   with   } \mathbf {M B} w.\tag{2.4}
$$

We shall assume that this is done.

Notation for the process of revising the MB's $x = (x_{1},\ldots ,x_{n})$ of a set of $n$ propositions occurring in all rules, from given values $x^{(t)} = (x_1^{(t)},\ldots ,x_n^{(t)})$ to $x^{(t + 1)} = (x_1^{(t + 1)},\ldots ,x_n^{(t + 1)})$ , is as follows: $x_{i}^{(t + 1)} = \max \left\{f_k(x^{(t)})|k\in K_i\right\} i = 1,\dots ,n.$

(2.5)

Here $K_{i} \neq 0$ is a finite index set for those rules with function $f_{k}(x)$ , which conclude the ith proposition. Of course, generally $f_{k}(x)$ depends only on a small subset of the variables in x, and $f_{k}$ is monotone

$$
x _ {1} \geq x _ {1} ^ {\prime} \text {   and   } \dots \text {   and   } x _ {n} \geq x _ {n} ^ {\prime} \rightarrow f _ {k} (x) \geq f _ {k} (x ^ {\prime})
$$

for all $k \in K_i$ and $i = 1, \ldots, n$ .

(2.6)

In the terminology of production rules, $x^{(t)}$ is obtained after t-times ‘firing’ all of these rules. The process of iteration is called (forward) chaining of the given rules.

We next give some mixed-integer-programming background.

A set $S \subseteq R'$ is called $b - MIP.r$ ('bounded-MIP-representable') if it is the projection of a set defined by linear inequality constraints in binary and continuous variables. I.e., $S$ is b-MIP.r if there are matrices $A, B$ , a vector $b$ and a subset $P$ of the indices of a vector of 'auxiliary variables', such that

$x \in S \leftrightarrow$ for some $y$ with $y_p \in \{0, 1\}$ for $p \in P$ ,

$$
\text { we   have } A x + B y \geqslant b.\tag{2.7}
$$

(The 'boundedness' in this definition is that of the $y_{p}$ , $p \in P$ , and not of $S$ , which can be unbounded.)

The notion of the recession cone $\operatorname{rec}(Q) = \{y \mid x + \lambda y \in Q$ whenever $x \in Q$ and $\lambda \geqslant 0\}$ is as in [21], [24].

The following is a characterization of b-MIP.r sets.

Theorem 2.1. [15], [16]. A set $S$ is $b$ -MIP. $r$ iff $S = Q_1 \cup \ldots \cup Q_s$ is a finite union of polyhedra $Q_i$ with $rec(Q_i)$ independent of $i, 1 \leqslant i \leqslant s$ .

In section 3, we shall require that the epigraph $\operatorname{epi}(f_k) = \{(z, x) | z \geqslant f_k(x)\}$ , of all the functions $f_k$ of 2.5, are b-MIP.r.

This is certainly true for the minimum functions $g(y_1, \ldots, y_r) = \min_i y_i$ on [0,1], since $\text{epi}(g) = Q_1 \cup \ldots \cup Q_r$ where $Q_i = \{(z, y) | z \geqslant y_i \geqslant 0, 1 \geqslant y_j \geqslant y_i \text{ for } j \neq i\}$ is a polyhedron with $\text{rec}(Q_i) = \{(z, y) | z \geqslant 0, \text{ all } y_j = 0\}$ independent of $i$ .

The epigraph of the function $h(y_{1},\ldots,y_{r})=\max_{i}y_{i}$ is not only b-MIP. r, but a polyhedron $\operatorname{epi}(h)=\{(z,y)\mid z\geqslant y_{i}\geqslant0,1\geqslant y_{i},\text{ for all }i\}$ . The epigraph of g is not convex, hence not a polyhedron (for r=2, $g(1,0)=g(0,1)=0$ , but $g(1/2,1/2)=1/2$ ).

The following fact, which follows from Theorem 2.1, will be important to note.

Proposition 2.1. If $S$ is $b$ -MIP. $r$ , then $S$ is closed

## 3. Main Result

Suppose that the epigraph of every function $f_{k}$ in (2.5) is b-MIP.r. Let the $a_{i}>0$ be positive scalars and let initial values $x^{0}=(x_{1}^{0},\ldots,x_{n}^{0})$ for x be given. The following can then be construed as a mixed-integer program

min $\sum_{i = 1}^{n}a_{i}x_{i}$

$$
\begin{array}{l l} \text { subject   to } & x _ {i} \geq f _ {k} (x), k \in K _ {i}, \\ & x _ {i} \geq x _ {i} ^ {(0)}, \end{array}\tag{3.1}
$$

$$
i = 1, \dots , n.
$$

In fact, by replacing the ‘constraint’ $x_{i} \geq f_{k}(x)$ by its representation via binary and continuous variables in linear constraints, (3.1) becomes exactly a MIP. We shall refer to (3.1) itself as a (MIP), for convenience.

With notation as in (2.5), write $\bar{x}_i = \lim_t x_i^{(t)}$ and $\bar{x} = (\bar{x}_1, \ldots, \bar{x}_n)$ , when these limits exist.

Our main result (Theorem 3.1 just below) asserts that a potentially infinite, and typically long, iteration process is captured by a single mixed-integer program.

Theorem 3.1. Assume that all functions $f_{k}$ in (2.5) are $b$ -MIP. $r$ , monotone (2.6), and that $\overline{x}$ exists and $\overline{x} \geq x^{(0)}$ . Let $x^{*}$ be the $x$ -coordinates of any optimal solution to the MIP (3.1). Then $x^{*}$ exists and $\overline{x} = x^{*}$ .

Proof. We prove by induction on $t$ that, if $x$ is feasible for (3.1), then

$$
x \geq x ^ {(t)}, \quad t = 0, 1, 2 \dots\tag{3.2}
$$

Of course, for $t = 0$ (3.2) holds due to the constraints of (3.1).

To go from $t$ to $(t + 1)$ , we note by monotonicity and by the induction hypothesis $x \geq x^{(t)}$ , that $x_{i} \geq f_{k}(x) \geq f_{k}(x^{(t)})$ for all $k \in K_{i}$ and $i = 1, \ldots, n$ . By (2.5), $x_{i} \geq x_{i}^{(t + 1)}$ , i.e. $x \geq x^{(t + 1)}$ .

From (3.2), it follows that $x \geq \overline{x}$ for all feasible solutions $x$ to (3.1).

We next show that $\bar{x}$ is feasible in (3.1). By (2.5) $(x_{i}^{(t + 1)}, x^{(t)}) \in \operatorname{epi}(f_k)$ for all $k \in K_i$ and $i = 1, \ldots, n$ for any $t$ . Upon taking the limit on $t$ , and using the closedness of $\operatorname{epi}(f_i)$ (Proposition 2.1), we find $(\bar{x}_i, \bar{x}) \in \operatorname{epi}(f_k)$ , i.e., $\bar{x}_i \geq f_k(\bar{x})$ . As $\bar{x} \geq x^{(0)}$ is an hypothesis, we see that $\bar{x}$ does satisfy all constraints of (3.1).

Thus, $\bar{x}$ is pointwise the minimum solution to (3.1). As the $a_{i} > 0$ , $\bar{x}$ is the unique optimum $x^{*}$ to (3.1). Q.E.D.

An example where the iteration process is infinite occurs for $n = 1$ , $K_{1} = \{1\}$ , $f_{1}(x_{1}) = \min \{\max \{0, 2x_{1} - 1/2\}, 1/2 + 1/2x_{1}\}$ , with $x_{1}^{0} = 2/3$ . (Note that $f_{1}(x_{1}) = 1/2 + 1/2x_{1}$ for $x_{1} \in [2/3, 1]$ ; and then $x^{(t)} = 1 - 1/3 \cdot 2^{t-1}$ ).

Mixed integer programs constitute one approach to completing the limit process for the approximates $x^{(t)}$ . In those instances where a small number of iterations are guaranteed to obtain prespecified tolerance of the limit $\bar{x}$ , direct iteration can be superior to MIP. However, work to date on this latter issue appears to be largely heuristic. In those cases where the epigraph of each $f_{k}$ is a polyhedron, then (3.1) becomes a linear program, which is particularly tractable.

For many cases where the $f_{k}$ are not piecewise linear, but are piecewise convex, a broader concept of representability was developed in [15]. In this setting, (3.1) would consist of convex constraints in binary and continuous variables, and the same conclusions hold.

The requirement $\bar{x} \geqslant x^{(0)}$ is weak, as it holds when rules (2.4) are used, and is implied by the conception that further facts (including deductions) cannot decrease an MB.

Of course, if the limits $\lim_{t}x^{(t)}$ do not exist, the result still holds with all $\bar{x}_{i}=\operatorname*{limsup}x_{i}^{(t)}$ .

## References

[1] E. Balas, Disjunctive Programming: Cutting-planes fro Logical conditions, in: O.L Mangasarian, R.R Meyer, And S.M. Robinson, Nonlinear Programming 2 (Academic Press, New York, 1975) 279–312.

[2] Avron Barr and Edward A. Feigenbaum, The Handbook of Artificial Intelligence (Heuris Tech Press and William Kaufman, Stanford and Los Altos, CA, 1981).

[3] W.W. Bledsoe and D.W. Loveland, eds., Automated Theorem Proving: After 25 Years, Contemporary Mathematics, vol. 29 (American Mathematical Society, Rhode Island, 1983).

[4] S.A. Cook The Complexity of Theorem-Proving Procedures, in: Proc. Third ACM Symposium on the Theory of Computing (1971) 151–158.

[5] G.B. Dantzig, Linear Programming and Extensions (Princeton, NJ, Princeton University Press, 1963).

[6] G.B. Dantzig, Discrete Variable Extremum Problems, Operations Research 5 (1957) 266–277.

[7] Randall Davis and Douglas B. Lenat, Knowledge-Based Systems in Artificial Intelligence and McGraw-Hill International, New York, 1982).

[8] R. Davis, B. Buchanan and E. Shortliffe, Production Rules as a Representation for a Knowledge-Based Consultation Program, Artificial Intelligence 8 (1977) 15–45.

[9] R. Garfinkel and G.L. Nemhauser, Integer Programming, (Wiley, New York, 1972).

[10] F. Glover, Polyhedral Annexation in Mixed Integer and Combinatorial Programming, Mathematical Programming 9 (1975) 161–188.

[11] R.E. Gomory, An Algorithm for Integer Solutions to Linear Programs, in: R.L. Graves and P. Wolfe, eds., Recent Advances in Mathematical Programming (McGraw-Hill, New York, 1983).

[12] R.E. Gomory, Some Polyhedra Related to Combinatorial Problems, Linear Algebra and its Applications 2 (1969) 451–558.

[13] Frederick Hayes-Roth, Donald A. Waterman and Douglas B. Lenat, Building Expert Systems (Addison-Wesley, Reading, MA, 1983).

[14] R. Jeroslow, An Extension of Mixed-Integer Programming Models and Techniques to some Database and Artificial Intelligence Settings (March, 1985).

[15] R. Jeroslow, Representability in Mixed-Integer Program-

ming, I: Characterization Results, Discrete Applied Mathematics 17 (1987) 223–243.

[16] R. Jeroslow and J.K. Lowe, Modelling with Integer Variables, Mathematical Programming Studies 22 (1984) 167–184.

[17] Donald W. Loveland, Automated Theorem-Proving: A Logical Basis (North-Holland, Amsterdam, 1978).

[18] James K. Lowe, Modelling With Integer Variables, Ph.D. thesis, Georgia Institute of Technology (March, 1984).

[19] R.R. Meyer, Integer and Mixed-Integer Programming Models: General Properties, Journal of Optimization Theory and Applications 16 (1975) 191–206.

[20] Elaine Rich, Artificial Intelligence (McGraw-Hill, New York, 1983).

[21] R.T. Rockafellar, Convex Analysis (Princeton University Press, Princeton, NJ, 1970).

[22] Edward H. Shortliffe, A Model of Inexact Reasoning in Medicine, Mathematical Biosciences 23 (1975) 351–379.

[23] Herbert A. Simon, The Structure of Ill-Structured Problems, Artificial Intelligence 4 (1973) 181–201.

[24] J. Stoer and C. Witzgall, Convexity and Optimization in Finite Dimensions I (Springer-Verlag, 1970).

[25] Patrick Henry Winston, Artificial Intelligence, 2nd ed. (Addison-Wesley, London, 1984).
