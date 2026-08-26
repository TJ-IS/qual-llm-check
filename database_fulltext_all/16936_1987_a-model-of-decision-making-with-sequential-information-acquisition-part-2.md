---
otero_id: 16936
otero_key: "2UBC4DHS"
title: "A model of decision-making with sequential information-acquisition (part 2)"
authors: "James C. Moore; Andrew B. Whinston"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90035-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Model of Decision-Making with Sequential Information-Acquisition (Part 2)

James C. MOORE and Andrew B. WHINSTON
Department of Computer Science and Krannert Graduate School of Management, Purdue University, West Lafayette, IN 47907, USA

While most real-life decision are of necessity made with less than perfect information, there is usually some opportunity to acquire additional information regarding the problem at hand before a final decision is made. It is, of course, the recognition of this fact which has led to the importance now attached to the field of Decision Support Systems. On the other hand, the formal analysis of the sort of decision problem for which Decision Support Systems can be useful appears to have lagged behind the developments in applications. In this paper we develop a model of decision-making in which there is available a variety of informational sources (experiments) which can reduce (though generally not eliminate) the uncertainty associated with the final decision. Since the informational sources are available only at some cost (either monetarily or in terms of time, or both), the decision-maker must solve two conceptually distinct problems: (1) developing an optimal information-gathering strategy, and (2) developing an optimal final decision strategy, conditional upon the information obtained during the information-gathering process. A theoretical framework is developed here for the analysis of this general problem, and fairly complete solutions are obtained for some interesting special cases; most notably the computer file search problem.

1. keywords: Decision support systems, Decision theory, Dynamic programming, File management.

## 4. The Categorization Problem

has co-authored two bool 'with C. Holsapple and R. Bonczek', Foundations of Decision Support Systems (Academic Press, 1981), and Micro Database Management – Practical Techniques for Application Development (Academic Press, 1985). He has been a consultant to various companies, governmental agencies, and international organizations on data processing questions.

## 4.1. Basic Model

In Part 1 of this paper that appeared in the previous issue of the DSS Journal the basic model was presented and the structure of an efficient solution was analyzed. In Part 2 we apply the basic model to describe the categorization problem so that more specific results may be obtained.

The special case of Model I which we shall refer to as the ‘categorization problem’ is characterized by the following assumptions (in addition to those set forth in section 2).

(1) The final decision set, $D$ , can be written in the form $D = \{0, 1, \ldots, p\}$ , where $p \geqslant 1$ is a positive integer.

(2) There exists a partition of $X$ , $\{X_0, X_1, \ldots, X_p\}$ , such that $\omega$ takes the form $^{16}$

$$
\begin{array}{r l} \omega (x, d) & = \left\{ \begin{array}{c c} \overline {{\omega}} > 0 & \text { if } x \in X _ {d} \\ 0 & \text { otherwise } \end{array} \right\} \\ \text { for } (x, d) & \in X \times D. \end{array}
$$

Andrew B. Whinston is on the faculty of the Krannert Graduate School of Management and the Department of Computer Science at Purdue University. His primary teaching interest is management information systems. His current research interests include data base management and applications of artificial intelligence to economics and management. He has also studied applied economics, regulatory economics, and accounting theory.

We may think of $\{X_0, X_1, \ldots, X_p\}$ as repre-

![](/api/attachments/2UBC4DHS/fulltext/images/9bc51c546008613066332e2b162d6b0a0f6f74106a2baf5ee759673fb102c66b.jpg)

![](/api/attachments/2UBC4DHS/fulltext/images/e2a7193fe2f76db6e97de0586e4aa3f6e9ea1eeb953e682cef06f57392590de4.jpg)

James C. Moore is Professor of Economics in the Krannert School of Management, Purdue University, West Lafayette, Indiana. His research interests lie in the areas of Micro/mathematical Economics, Welfare Economics, and the Economics of Information and Organization. He received a B.A. in Economics from the University of Nebraska at Omaha in 1960, and his Ph.D. in Economics from the University of Minnesota in 1968. Prior to joining the faculty at Purdue University, he taught at the University of Missouri, Columbia. Dr. Moore is a member of the American Economics Association and the Econometrics Society.

senting an (exhaustive) set of categories (or classifications) to which the true state, $\hat{x}$ , may belong. There is a constant (constant over categories) positive payoff, $\overline{\omega}$ , if $\hat{x}$ is categorized correctly, and a payoff of zero is obtained if $\hat{x}$ is not correctly categorized (or classified). Some examples which seem to fit this formulation reasonably well are (a) chemical analysis of an unknown substance, (b) the game of ‘twenty question’, and (c) the computer file search problem. $^{17}$ We shall develop the computer file search problem in detail in the next subsection.

In dealing with the categorization problem, the function $\psi: P(X) \to [0, 1]$ defined by

$$
\psi (B) = \max \left\{\pi (B \cap X _ {d}) | d \in D \right\} \quad \text { for } \quad B \subseteq X,\tag{1}
$$

will be of particular interest.

4.1.1. Proposition. If $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is an efficient strategy for $D$ , then

$$
\Omega (\sigma) = \overline {{{\omega}}} \sum_ {B \in B _ {r + 1}} \psi (B).\tag{1}
$$

Proof. If $\sigma$ is an efficient strategy for D, then we must have

$$
(\forall B \in B _ {r + 1}): \delta (B) \in D ^ {*} (B).
$$

From the form of $\omega(\cdot)$ it is clear, however, that for $B \subseteq X$ , we will have $d^{*} \in D^{*}(B)$ if, and only if

$$
(\forall d \in D): \pi (B \cap X _ {d}) \leq \pi (B \cap X _ {d ^ {*}}) \equiv \psi (B).
$$

Thus, for each $B \in B_{r+1}$ ,

$$
\begin{array}{r l} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] & = \sum_ {x \in B \cap X _ {\delta (B)}} \phi (x) \overline {{\omega}} \\ & = \overline {{\omega}} \sum_ {x \in B \cap X _ {\delta (B)}} \phi (x) \\ & = \overline {{\omega}} \pi (B \cap X _ {\delta (B)}) \\ & = \overline {{\omega}} \psi (B). \end{array}
$$

Therefore

$$
\begin{array}{r l} \Omega (\sigma) & = \sum_ {B \in B _ {r + 1}} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ & = \overline {{\omega}} \sum_ {B \in B _ {r + 1}} \psi (B). \end{array}
$$

Q.E.D.

There are several special cases of the categorization problem in which we shall have a particular interest. In order to define the first two (to which we shall not attach special names) we begin by defining

$$
\boldsymbol {X} = \left\{X _ {0}, X _ {1}, \dots , X _ {p} \right\}.\tag{2}
$$

The following two alternative conditions then define the two basic sub-cases with which we shall be interested

$$
\begin{array}{l l} \boldsymbol {X} \geq \boldsymbol {B} ^ {A}, & \text { and } \\ \boldsymbol {B} ^ {A} \geq \boldsymbol {X}. \end{array}\tag{3}
$$

(4)

In the first special case, that in which (3) holds, X is at least as fine as $B^{A}$ ; that is

$$
(\forall d \in D) (\exists B \in B ^ {A}): X _ {d} \subseteq B.\tag{5}
$$

The second special case is nearly the opposite of the first; that is, (4) holds if and only if

$$
(\forall B \in B ^ {A}) (\exists d \in D): B \subseteq X _ {d}\tag{6}
$$

(it is, of course, possible for a decision problem to satisfy both (3) and (4); that is, we may have $B^{A} = X$ ). Notice that in the situation in which (4) holds, we will have

$$
(\forall B \in B ^ {A}): \psi (B) = \pi (B).\tag{7}
$$

There are also sub-cases of both (3) and (4) which we shall find particularly interesting: (a) the 'only correct guesses count' problem, which we define below, is a sub-case of (3), and (b) the computer file search problem, which we shall introduce in the next subsection, is a special case of (4).

4.1.2. Definition. If D is a categorization problem, we shall say that D has the only correct guesses count form iff

(i) D satisfies (3), above,

(ii) There exists a positive integer $m \geq p + 1$ , satisfying

$$
(\forall B \in B ^ {A}): \psi (B) = 1 / m,\tag{8}
$$

(iii) D has constant information cost, $c \geq 0$ , i.e., $(\forall a \in A_{1})$ : $c(a) = c$ . (9)

The simplest case in which condition (8) holds is that in which

$$
\boldsymbol {X} = \boldsymbol {B} ^ {X}\tag{10}
$$

In this case the categories $X_{0}, X_{1}, \ldots, X_{p}$ are simply singleton sets, and the problem has the following interpretation: we know that the true state, $\hat{x}$ , is one of $p + 1$ possible states, $x_{0}, x_{1}, \ldots, x_{p}$ ; and we receive a reward of $\overline{\omega} > 0$ if we guess correctly which $x_{i} = \hat{x}$ , and receive nothing if our guess is incorrect. $^{18}$ If, in addition to (10), we have

$$
\boldsymbol {B} ^ {A} = \boldsymbol {B} ^ {X},
$$

then condition (8), above, amounts to the assumption that $\phi$ , the probability density function on X, is the uniform distribution, with

$$
\phi (x) = 1 / m = 1 / (p + 1) \quad \text { for   each } \quad x \in X.
$$

In the case where condition (3) holds, the expected gross payoff function takes on a particularly simple form, as follows.

4.1.3. Proposition. If D is a categorization problem satisfying condition (3), above (i.e., $X \geq B^{A}$ ) then for any efficient strategy, $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ , we have

$$
\Omega (\sigma) = \left[ \sum_ {B \in B _ {r + 1}} \max \left\{\psi (B ^ {\prime}) \mid B ^ {\prime} \in B ^ {A} (B) \right\} \right] \overline {{\omega}}.
$$

Proof. We have from Proposition 1 that

$$
\Omega (\sigma) = \left[ \sum_ {B \in B _ {r + 1}} \psi (B) \right] \overline {{\omega}}.\tag{11}
$$

However, let $B \in B_{r+1}$ be arbitrary, and let $d \in D$ . Then we have, since $B^A(B)$ is a partition of $B$ ,

$$
\pi (B \cap X _ {d}) = \sum_ {B ^ {\prime} \in B ^ {A} (B)} \pi (B ^ {\prime} \cap X _ {d}).\tag{12}
$$

However, since $X \geq B^A$ , it follows that for all but at most one $B' \in B^A(B)$ , we have

$$
\pi \left(B ^ {\prime} \cap X _ {d}\right) = 0,
$$

and if $B' \in B^A(B)$ is such that $\pi(B' \cap X_d) > 0$ , we have

$$
\pi \left(B ^ {\prime} \cap X _ {d}\right) \leq \psi \left(B ^ {\prime}\right).
$$

It follows, therefore, that

$$
\begin{array}{r l} \psi (B) & = \max \left\{\pi (B \cap X _ {d}) \mid d \in D \right\} \\ & = \max \left\{\psi (B ^ {\prime}) \mid B ^ {\prime} \in B ^ {A} (B) \right\} \\ \text { and   our   result   follows. } & \quad \text { Q.E.D. } \end{array}
$$

The following is an immediate consequence of Proposition 3.

4.1.4. Corollary. If D is of the only correct guesses count form and if $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ is an efficient strategy for D, then

$$
\Omega (\sigma) = \left(\# B _ {r + 1}\right) \overline {{{\omega}}} / m.
$$

Proposition 3 shows one reason why the case where condition (3) holds is of particular interest. In section 5.2 we shall be able to develop other results which exploit condition (3) to obtain a sharper characterization of the solution to this special case of the categorization problem; and in section 6.5 we shall also be able to obtain similar (though somewhat weaker) results for the case where condition (4) holds.

## 4.2. The Computer File Search Problem

The computer file search problem, as we shall develop it here, is also a special case of our categorization problem. We develop it as follows.

We suppose that there is some universal set, U, which is finite and linearly ordered, and that we are dealing with a non-empty subset,

$$
S = \left\{b _ {1}, b _ {2}, \dots , b _ {n} \right\} \subseteq U,\tag{1}
$$

with

$$
b _ {i} <   b _ {i + 1} \quad \text { for } \quad i = 1, \dots , n - 1.\tag{2}
$$

We suppose that there is a probability measure on U, so that the probabilities $\Pr(b < b_{1})$ , $\Pr(b > b_{n})$ , $\Pr(b_{i} < b < b_{i+1})$ for $i = 1, \ldots, n - 1$ , and $\Pr(b = b_{i})$ for $i = 1, \ldots, n$ , are well-defined, for b a random element of U.

The basic idea is that the elements of S correspond to a stored data set drawn from U. We consider the problem of searching the set in order to determine whether a randomly drawn element from U, b is in the set S or not; and if it is in S, to determine its location (i.e., for which i we have $b = b_{i}$ ). The available experiments can be denoted by

$$
A = \{0, 1, \dots , n \},
$$

where for $a = 1, \ldots, n$ , the experiment $a$ is interpreted as

'compare b with $\mathbf{b}_{\mathbf{a}}$ '

(and $a=0$ represents the null information experiment). Thus, for $a\in A_{1}$ , the possible outcomes of the experiment are

$$
b <   b _ {a}, \quad b = b _ {a} \quad \text { or } \quad b > b _ {a}.\tag{3}
$$

For notational convenience, we shall represent the state space as

$$
X = Y \cup Z,
$$

where $Y = \{y_{1},\ldots ,y_{n}\}$ , with the interpretation $x = y_{i}\Leftrightarrow b = b_{i}\quad \text{for}\quad i = 1,\dots ,n,$

and $Z = \{z_0, z_1, \ldots, z_n\}$ , with the interpretation

$$
x = z _ {j} \Leftrightarrow \left\{ \begin{array}{l l} b <   b _ {1} & \text {if} \quad j = 0 \\ b _ {j} <   b <   b _ {j + 1} & \text {for} \quad j = 1, \dots , n - 1 \\ b > b _ {n} & \text {for} \quad j = n. \end{array} \right.
$$

We then define

$$
\begin{array}{l} p _ {i} = P r (x = y _ {i}) = P r (b = b _ {i}) \quad \text { for } \quad i = 1, \ldots , n, \\ q _ {0} = P r (x = z _ {0}) = P r (b <   b _ {1}), \\ q _ {j} = P r (x = z _ {j}) = P r (b _ {j} <   b <   b _ {j + 1}) \\ \quad \text { for } \quad j = 1, \ldots , n - 1, \quad \text { and } \\ q _ {n} = P r (x = z _ {n}) = P r (b > b _ {n}). \end{array}
$$

From (3) and our specification of X, we see that for each $a \in A_{1}$ , the information structure for a, $M_{a}$ , can be written as

$$
\begin{array}{l} M _ {a} = \left\{M _ {a 1}, M _ {a 2}, M _ {a 3} \right\}, \quad \text {where} \\ M _ {a 1} = \left\{y _ {1}, \ldots , y _ {a - 1} \right\} \cup \left\{z _ {0}, \ldots , z _ {a - 1} \right\}, \\ M _ {a 2} = \left\{y _ {a} \right\}, \quad \text {and} \\ M _ {a 3} = \left\{y _ {a + 1}, \ldots , y _ {n} \right\} \cup \left\{z _ {a}, \ldots , z _ {n} \right\}. \end{array}
$$

To complete our specification of the problem, we note that we can specify D as

$$
\boldsymbol {D} = \{0, 1, \dots , n \},
$$

with the following interpretation: $d = 0$ corresponds to the decision $b \notin S$ (i.e., $x \in Z$ ), $d = j$ corresponds to the decision $b = b_j$ (i.e., $x = y$ ) for $j = 1, \ldots, n$ . It also seems appropriate here to specify our gross payoff function $\omega: X \times D \to \mathbb{R}$ as

$$
\omega (x, d) = \left\{ \begin{array}{l l} \overline {{\omega}} > 0 & \text {if} d = 0 \text {and} x \in Z, \\ & \text {or if} d \in \{1, \dots , n \} \\ & \text {and} x = y _ {d}, \text {and} \\ 0 & \text {otherwise.} \end{array} \right.
$$

We also suppose that there exists some constant $c > 0$ such that

$$
c (a) = c \quad \text { for } \quad a = 1, \dots , n.
$$

Thus we see that, in the formulation developed here, the problem of finding an optimal for the solution of the computer file search problem is a special case of our categorization problem. Notice also that the file search problem satisfies condition (4) of the previous subsection, i.e., we have $B^{A} \geq X$ .

We shall examine the solution of the computer file search problem in some detail in section 6.5.

## 5. Expected Costs and the Number of Sets in the Final Information Structure

## 5.1. Prelimina, Results

In this section we shall often be dealing with situations in which D satisfies one or both of the following conditions.

5.1.1. Definition. We shall say that $\pmb{D}$ has constant information cost $c$ , if $c \in \mathbb{R}_+$ is such that

$$
(\forall a \in A _ {1}): c (a) = c.
$$

5.1.2. Definition. We shall say that D is a k-element information structure problem, where $k \in \{2, 3, \ldots\}$ , iff

$$
(\forall a \in A _ {1}) \colon n _ {a} = \# M _ {a} = k,
$$

i.e., for each $a \in A_1$ , $M_a$ is of the form

$$
M _ {a} = \left\{M _ {a 1}, \dots , M _ {a k} \right\}
$$

(note: If k=2, we shall use the term 'binary' in place of 'two-element'; and if k=3, we shall similarly use the term 'trinary').

In this section we shall assume that D is a k-element information structure problem only where explicitly stated. However, throughout this section we shall use k to denote the value of

$$
k = \max _ {a \in A} \# M _ {a} = \max _ {a \in A _ {1}} n _ {a}.\tag{1}
$$

We shall also find the following to be convenient in characterizing the value of expected cost.

5.1.3. Definition. Given an efficient information-gathering strategy for $D$ , $\alpha = \langle B_1, \alpha_1 \rangle$ , ..., $(B_r, \alpha_r) \rangle$ , and letting $B_{r+1} = R(B_r, \alpha_r)$ , we define $\tau_\alpha: B_{r+1} \to \{1, \ldots, r\}$ by

$$
\tau_ {\alpha} (B) = \max \left\{t \in \{1, \dots , r \} \mid a (t, B) \neq 0 \right\}.
$$

5.1.4. Proposition. If the decision problem D has constant information cost, c, and $\alpha$ is an efficient information-gathering for D, then

$$
\begin{array}{r l} \gamma (\alpha) & = \left[ \sum_ {B \in B _ {r + 1}} \pi (B) \tau_ {\alpha} (B) \right] c \\ & = r c - \sum_ {B \in B _ {r + 1}} \pi (B) [ r - \tau_ {\alpha} (B) ] c. \end{array}\tag{1}
$$

Proof. We have

$$
\gamma (\alpha) = \sum_ {B \in B _ {r + 1}} \pi (B) C (B), \quad \text { where }\tag{2}
$$

$$
C (B) = \sum_ {t = 1} ^ {r} c [ a (t, B) ].\tag{3}
$$

However, since

$$
c [ a (t, B) ] = \left\{ \begin{array}{l l} 0 & \text { if } \quad a (t, B) = 0, \\ c & \text { if } \quad a (t, B) \neq 0. \end{array} \right.
$$

it follows (since $\alpha$ is efficient) that

$$
\sum_ {t = 1} ^ {r} c [ a (t, B) ] = \tau_ {\alpha} (B) c.\tag{4}
$$

Therefore, by (2)-(4),

$$
\begin{array}{r l} \gamma (\alpha) & = \sum_ {B \in B _ {r + 1}} \pi (B) \tau_ {\alpha} (B) c \\ & = \left[ \sum_ {B \in B _ {r + 1}} \pi (B) \tau_ {\alpha} (B) \right] c, \end{array}
$$

which establishes the first equality in (1). The second equality follows readily, using the fact that, since $B_{r+1}$ is a partition of X,

$$
\sum_ {B \in B _ {r + 1}} \pi (B) = 1.
$$

Q.E.D.

Turning now to the question of characterizing the number of elements in $B_{r+1}$ , we note first that it is fairly obvious that if $\alpha$ is a feasible information-gathering strategy for D, and $B_{r+1} = R(B_r, \alpha_r)$ , then

$\#B_{r+1}\leq k^{r}.$

However, with the use of the $\tau_{\alpha}(\cdot)$ function, we will be able to prove a somewhat sharper result; although we must first develop some supporting material, as follows.

Let $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ be an efficient information-gathering strategy for $D$ such that $\alpha_1(X) \neq 0$ , $^{19}$ and let

$$
\boldsymbol {B} _ {r + 1} = R \left(\boldsymbol {B} _ {r}, \alpha_ {r}\right).
$$

For $t = 1, \ldots, r$ , we partition $B_t$ into three subsets, as follows:

$$
\begin{array}{l} \boldsymbol {B} _ {1} ^ {1} = \boldsymbol {B} _ {1} ^ {0} = \boldsymbol {B} _ {2} ^ {0} = \phi , \boldsymbol {B} _ {1} ^ {2} = \boldsymbol {B} _ {1} = \{X \}, \\ \boldsymbol {B} _ {2} ^ {1} = \left\{B \in \boldsymbol {B} _ {2} | \alpha_ {2} (B) = 0 \right\}, \\ \boldsymbol {B} _ {2} ^ {2} = \left\{B \in \boldsymbol {B} _ {2} | \alpha_ {2} (B) \neq 0 \right\}, \\ \text { and,   in   general } \\ \boldsymbol {B} _ {t} ^ {0} = \bigcup_ {s = 1} ^ {t - 1} \boldsymbol {B} _ {s} ^ {1}, \\ \boldsymbol {B} _ {t} ^ {2} = \left\{B \in \boldsymbol {B} _ {t} | \alpha_ {t} (B) \neq 0 \right\}, \quad \text { and } \\ \boldsymbol {B} _ {t} ^ {1} = \boldsymbol {B} _ {t} \setminus \left[ \boldsymbol {B} _ {t} ^ {0} \cup \boldsymbol {B} _ {t} ^ {2} \right] \quad \text { for } \quad t = 1, \ldots , r. \end{array}
$$

Note that for $t \in \{1, \ldots, r\}$ , $B_t^2$ might be called the action set; it is only if the previous actions (experiments) have shown that $\hat{x}$ , the true state, is an element of some $B \in B_t^2$ that an information-gathering activity is conducted at the $t$ th step. The information sets in $B_t \setminus B_t^2$ all have the property that no new experimentation is to be performed at the $t$ th step. However, the sets in $B_t \setminus B_t^2$ are of two types: (a) those on which no new experimentation was to have been performed at the $(t-1)$ st step, and which were, therefore, also elements of $B_{t-1}$ , and (b) those sets $B \in B_t$ for which $\alpha_t(B) = 0$ , but which were not elements of $B_{t-1}$ [thus for $B \in B_t^1$ , $\alpha_{t-1}[\beta_{t-1}(B)] \neq 0$ ].

Thus we have, for each $t \in \{1, \ldots, r\}$ ,

$$
\boldsymbol {B} _ {t} ^ {0} \cup \boldsymbol {B} _ {t} ^ {1} = \left\{\boldsymbol {B} \in \boldsymbol {B} _ {t} \mid \alpha_ {t} (\boldsymbol {B}) = 0 \right\},
$$

and, since $\alpha$ is efficient, it follows that

$$
\boldsymbol {B} _ {t} ^ {0} \cup \boldsymbol {B} _ {t} ^ {1} \subseteq \boldsymbol {B} _ {r + 1} \quad \text { for } \quad t = 1, \dots , r.\tag{5}
$$

In fact, for each $t \in \{1, \ldots, r + 1\}$ ,

$$
\boldsymbol {B} _ {t} ^ {1} = \left\{\boldsymbol {B} \in \boldsymbol {B} _ {r + 1} \mid \tau_ {\alpha} (\boldsymbol {B}) = t - 1 \right\}, \quad \text { and }\tag{6}
$$

$$
\boldsymbol {B} _ {t} = \boldsymbol {B} _ {t} ^ {2} \cup \left[ \bigcup_ {s = 1} ^ {t} \boldsymbol {B} _ {s} ^ {1} \right] \quad \text { for } \quad t = 1, \dots , r + 1.\tag{7}
$$

5.1.5. Lemma. If $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ is an efficient and non-trivial information-gathering strategy, and we define

$$
\boldsymbol {B} _ {r + 1} = R \left(\boldsymbol {B} _ {r}, \alpha_ {r}\right),
$$

then we have

$$
\begin{array}{l} \# B _ {t} \leq k ^ {t - 1} - \sum_ {s = 1} ^ {t - 1} \big (\# B _ {s} ^ {1} \big) (k ^ {t - s} - 1) \\ \text { for } \quad t = 2, \dots , r + 1. \end{array}\tag{8}
$$

Proof. For $t = 2$ , we have $B_2 = M_{\alpha_1(X)}$ , and obviously, $\# B_2 = \# M_{\alpha_1(X)} \leq k$ , while $\sum_{s=1}^{1} (\# B_s^1)(k^{2-s} - 1) = 0 \cdot (k - 1) = 0$ .

Suppose now that our formula (8) holds for $t = q(q \geq 2)$ . then for $t = q + 1$ , we have

$$
\begin{array}{r l} & {\# \mathbf {B} _ {t} = \# \mathbf {B} _ {q + 1} = \# \bigg (\bigcup_ {B \in B _ {q}} \iota [ B, \alpha_ {q} (B) ] \bigg)} \\ & {\quad = \sum_ {B \in B _ {q}} \# \big (\iota [ B, \alpha_ {q} (B) ] \big)} \\ & {\quad = \sum_ {B \in B _ {q} ^ {0}} \# \big (\iota [ B, \alpha_ {q} (B) ] \big)} \\ & {\quad + \sum_ {B \in B _ {q} ^ {1}} \# \big (\iota [ B, \alpha_ {q} (B) ] \big)} \\ & {\quad + \sum_ {B \in B _ {q} ^ {2}} \# \big (\iota [ B, \alpha_ {q} (B) ] \big)} \\ & {\leq \sum_ {s = 1} ^ {q} \# B _ {s} ^ {1} + \big (\# B _ {q} ^ {2} \big) k} \\ & {\quad = \sum_ {s = 1} ^ {q} \# B _ {s} ^ {1} + \Bigg (\# B _ {q} - \sum_ {s = 1} ^ {q} \# B _ {s} ^ {1} \Bigg) k} \\ & {\leq \sum_ {s = 1} ^ {q} \# B _ {s} ^ {1} + k \Bigg [ k ^ {q - 1} - \sum_ {s = 1} ^ {q - 1} \big (\# B _ {s} ^ {1} \big) (k ^ {q - s} - 1)} \\ & {\quad - \sum_ {s = 1} ^ {q} \# B _ {s} ^ {1} \Bigg ]} \\ & {\quad = \sum_ {s = 1} ^ {q} \# B _ {s} ^ {1} + k ^ {q} - \sum_ {s = 1} ^ {q} \big (\# B _ {s} ^ {1} \big) k ^ {q + 1 - s}} \\ & {\quad = k ^ {q} - \sum_ {s = 1} ^ {q} \big (\# B _ {s} ^ {1} \big) (k ^ {q + 1 - s} - 1)} \\ & {\quad = k ^ {t - 1} - \sum_ {s = 1} ^ {t - 1} \big (\# B _ {s} ^ {1} \big) (k ^ {t - s} - 1).} \end{array}
$$

Q.E.D.

We can now prove the following.

5.1.6. Proposition. If $\alpha = \langle (\pmb{B}_1, \alpha_1), \ldots, (\pmb{B}_r, \alpha_r) \rangle$ is an efficient information-gathering strategy for $\pmb{D}$ , and $\pmb{B}_{r+1} = R(\pmb{B}_r, \alpha_r)$ , we have

$$
\begin{array}{r l} \# B _ {r + 1} & \leq k ^ {r} - \sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) (k ^ {r + 1 - t} - 1) \\ & = k ^ {r} - \sum_ {B \in B _ {r + 1}} [ k ^ {r - \tau_ {\alpha} (B)} - 1 ], \end{array}\tag{9}
$$

and thus

$$
\sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) k ^ {r + 1 - t} \leq k ^ {r}.\tag{10}
$$

Proof. (i) We first prove the inequality in (9), as follows. If $\min\{\tau_{\alpha}(B)|B\in B_{r+1}\}=0$ , then, since $\alpha$ is efficient, $B_{r+1}=\{X\}$ , $\#B_{r+1}=1$ , and

$$
\sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) (k ^ {r + 1 - t} - 1) = 1 \cdot (k ^ {r} - 1),
$$

so that

$$
1 = \# B _ {r + 1} = k ^ {r} - \sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) \left(k ^ {r + 1 - t} - 1\right),
$$

as required.

Now suppose $\min\{\tau_{\alpha}(B) | B \in B_{r+1}\} \geq 1$ . Then $\alpha$ is non-trivial, and by Lemma 5 we have

$$
\# B _ {r + 1} \leq k ^ {r} - \sum_ {t = 1} ^ {r} \left(\# B _ {t} ^ {1}\right) \left(k ^ {r + 1 - t} - 1\right).\tag{11}
$$

Since

$$
\left(\# B _ {r + 1} ^ {1}\right) \left(k ^ {r + 1 - (r + 1)} - 1\right) = 0,
$$

we can extend (11) to

$$
\# B _ {r + 1} \leq k ^ {r} - \sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) \left(k ^ {r + 1 - t} - 1\right),\tag{12}
$$

$$
\begin{array}{l} \text { which   establishes   the   inequality   in(9). } \\ \text { Now,we have } \\ B _ {r + 1} = \bigcup_ {t = 1} ^ {r + 1} B _ {t} ^ {1}, \\ \text { and,for all } B \in B _ {t} ^ {1} (t = 1, \ldots , r + 1), \tau_ {\alpha} (B) = t - 1. \\ \text { Thus } \end{array}
$$

$$
\begin{array}{l} k ^ {r} - \sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) (k ^ {r + 1 - t} - 1) \\ = k ^ {r} - \sum_ {B \in B _ {r + 1}} \left[ k ^ {r - \tau_ {\alpha} (B)} - 1 \right], \end{array}
$$

which establishes the equality in (9).

(ii) We have

$$
\begin{array}{r l} & \sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) (k ^ {r + 1 - t} - 1) \\ & = \sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) k ^ {r + 1 - t} - \sum_ {t = 1} ^ {r + 1} \# B _ {t} ^ {1} \\ & = \sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) k ^ {r + 1 - 1} - \# B _ {r + 1}, \end{array}\tag{13}
$$

where the last equality follows from the fact $\{B_{1}^{1}, B_{2}^{1}, \ldots, B_{r+1}^{1}\}$ is a partition of $B_{r+1}$ . Substitution of (13) into (12) yields inequality (10). Q.E.D.

5.1.7. Corollary. If, under the hypotheses of Proposition 6, we have

$$
\# B _ {r + 1} > k (k ^ {r - 1} - 1) + 1, \quad \text { then }\tag{14}
$$

$$
(\forall B \in B _ {r + 1}) \colon \tau_ {\alpha} (B) = r,\tag{15}
$$

or, equivalently, for each $t \in \{1, \dots, r\}$ , we have

$$
(\forall B \in \mathcal {B} _ {t}): \alpha_ {t} (B) \neq 0, \quad \text { or }\tag{16}
$$

$$
\# B _ {t} ^ {1} = 0.\tag{17}
$$

Proof. Since it is obvious that (15)-(17) are all equivalent, we shall prove that (14) implies (17). Accordingly, from (14) and (9) of Proposition 6, we have

$$
k \left(k ^ {r - 1} - 1\right) + 1 <   k ^ {r} - \sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) \left(k ^ {r + 1 - t} - 1\right),
$$

from which we obtain

$$
\sum_ {t = 1} ^ {r + 1} \left(\# B _ {t} ^ {1}\right) \left(k ^ {r + 1 - t} - 1\right) <   k - 1.\tag{18}
$$

If it were the case that for some $q \in \{1, \ldots, r\}$ , we had $\# B_q^1 \geq 1$ , then we would obtain from (18) that

$$
k - 1 > \left(\# B _ {q} ^ {1}\right) (k ^ {r + 1 - q} - 1) \geq k - 1,
$$

yielding a contradiction. Thus we conclude that

$$
\# B _ {t} ^ {1} = 0 \quad \text { for } \quad t = 1, \dots , r.
$$

Q.E.D.

## 5.2. Application to the Categorization Problem

Throughout this section, we shall suppose that D is a categorization problem and that D has constant

information cost, c, i.e.,

$$
(\forall a \in A _ {1}): c (a) = c \geq 0.\tag{1}
$$

We write

$$
\boldsymbol {B} ^ {A} = \left\{B _ {1}, \dots , B _ {q} \right\},\tag{2}
$$

and suppose, without loss of generality, that, defining

$$
\theta_ {i} = \psi (B _ {i}) \quad \text { for } \quad i = 1, \dots , q,\tag{3}
$$

that we have

$$
\theta_ {1} \geq \theta_ {2} \geq \dots \geq \theta_ {q}.\tag{4}
$$

Finally, we shall once again let

$$
k \equiv \max _ {a \in A} \# M _ {a}.\tag{5}
$$

Before turning to our first result of this section, it may be worthwhile to set the stage by considering some aspects of the principal new hypothesis we shall use in said result. In Theorem 1, below, we assume that there exists an efficient strategy, $\sigma^{*} = \langle \alpha^{*}, B_{r+1}^{*}, \delta^{*} \rangle$ such that $\# B_{r+1}^{*} = k^{r}$ . If this is the case, then $q \geq k^{r}$ [where $q$ is from (2), above]; and, since $B^{A} \geq B_{r+1}^{*}$ , there is no loss in generality in supposing that we can label the sets in $B^{A}$ in such a way that there exists a one-to-one and onto mapping,

$$
\zeta \colon \{1, \dots , k ^ {r} \} \rightarrow B _ {r + 1} ^ {*},
$$

satisfying

$$
B _ {i} \subseteq \zeta (i) \quad \text { for } \quad i = 1, \dots , k ^ {r},\tag{6}
$$

[each $B \in B_{r+1}^{*}$ contains at least one $B' \in B^{A}$ ; and, for each $B$ , $B' \in B_{r+1}^{*}$ , $B^{A}(B) \cap B^{A'}(B') = \emptyset$ ]. We shall suppose, however, that the labeling and the mapping $\zeta$ can be constructed in such a way as to satisfy (4) as well. This combination of conditions is, therefore, more restrictive $^{20}$ than the mere assumption that $\#B_{r+1}^{*} = k^{r}$ .

## 5.2.1. Theorem. If $\pmb{D}$ satisfies

$$
\boldsymbol {X} \geq \boldsymbol {B} ^ {A},\tag{7}
$$

$$
(k - 1) \overline {{{\omega}}} \theta \geq c,\tag{8}
$$

where $\theta = \theta_{k}r$ , and if there exists an efficient strategy for $D$ , $\sigma^{*} = \langle \alpha^{*}, B_{r+1}^{*}, \delta^{*} \rangle$ , satisfying

$\# B_{r+1}^{*} = k^{r}$ , and there exists a one-to-one

and onto mapping

(9)

$^{20}$ Notice, however, that the labeling of $B^{A}$ which produces (4) will generally not be unique; that is, it is unique if, and only if, all the inequalities in (4) are strict.

$\zeta: \{1, \ldots, k^r\} \to B_{r+1}^*$ , satisfying

$B_{i}\subseteq \zeta (i)$ for $i = 1,\dots ,k^r$ , then

(i) the expected net return from $\sigma^{*}$ is

$$
\Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) = \left(\sum_ {i = 1} ^ {k ^ {\prime}} \theta_ {i}\right) \bar {\omega} - r c, \quad \text { and }
$$

(ii) $\sigma^{*}$ is optimal for $D$ .

Proof. (i) By Proposition 4.1.3, we have

$$
\Omega (\sigma^ {*}) = \left[ \sum_ {B \in B _ {r + 1} ^ {*}} \max \left\{\psi (B ^ {\prime}) \mid B ^ {\prime} \in B ^ {A} (B) \right\} \right] \bar {\omega}.\tag{10}
$$

However, if $B \in B_{r+1}^*$ is such that

$$
\zeta^ {- 1} (B) = i \in \{1, \dots , k ^ {r} \},
$$

we have

$$
\boldsymbol {B} _ {i} \subseteq \boldsymbol {B},
$$

and, for $j < i$ , $B \cap B_j = \emptyset$ . Therefore, by (4),

$$
\max \left\{\psi (B ^ {\prime}) \mid B ^ {\prime} \in B ^ {A} (B) \right\} = \theta_ {i} = \psi (B _ {i}),
$$

and, by (10) we then have

$$
\Omega (\sigma^ {*}) = \left(\sum_ {i = 1} ^ {k ^ {\prime}} \theta_ {i}\right) \overline {{{{\omega}}}}.\tag{11}
$$

Now, by Proposition 5.1.4,

$$
\Gamma (\sigma^ {*}) = \left[ \sum_ {B \in B _ {r + 1} ^ {*}} \pi (B) \tau_ {\alpha^ {*}} (B) \right] c.\tag{12}
$$

However, since $\# B_{r+1}^{*} = k^{r}$ , it follows from Corollary 5.1.7 that

$$
(\forall B \in B _ {r + 1} ^ {*}) \colon \tau_ {\alpha^ {*}} (B) = r,
$$

and thus we have from (12) that

$$
\Gamma (\sigma^ {*}) = \left[ \sum_ {B \in B _ {r + 1} ^ {*}} \pi (B) \right] r c = r c,\tag{13}
$$

where the second equality is by the fact that $B_{r+1}^{*}$ is a partition of X.

(ii) Suppose $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ is an efficient strategy for $D$ . Then we have by Proposition 4.1.3 and 5.1.4 that

$$
\begin{array}{l} \Omega (\sigma) - \Gamma (\sigma) \\ = \left[ \sum_ {B \in B _ {r + 1}} \max \{\psi (B ^ {\prime}) | B ^ {\prime} \in B ^ {A} (B) \} \right] \overline {{\omega}} \\ - r c + \sum_ {B \in B _ {r + 1}} \pi (B) [ r - \tau_ {\alpha} (B) ] c \end{array}\tag{14}
$$

Now, by Proposition 5.1.6, we have

$$
\# B _ {r + 1} \leq k ^ {r} - \sum_ {B \in B _ {r + 1}} \left[ k ^ {r - \tau_ {\alpha} (B)} - 1 \right].\tag{15}
$$

Defining

$$
\bar {p} = \sum_ {B \in B _ {r + 1}} \left[ k ^ {r - \tau_ {a} (B)} - 1 \right],
$$

we see from (15), (4) and the form of $\Omega(\sigma)$ that we can write

$$
\begin{array}{l} \Omega (\sigma) = \left[ \sum_ {B \in B _ {r + 1}} \max \left\{\psi (B ^ {\prime}) \mid B ^ {\prime} \in B ^ {A} (B) \right\} \right] \overline {{{\omega}}} \\ \leq \left(\sum_ {i = 1} ^ {k ^ {r} - \bar {p}} \theta_ {i}\right) \overline {{{\omega}}}. \end{array} \tag {1}\tag{16}
$$

Thus from (11), (13), (14), and (16), we have

$$
\begin{array}{l} \Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) - [ \Omega (\sigma) - \Gamma (\sigma) ] \\ \geq \left(\sum_ {i = k ^ {r} - \overline {{p}} + 1} ^ {k ^ {r}} \theta_ {i}\right) \overline {{\omega}} - \sum_ {B \in B _ {r + 1}} \pi (B) [ r - \tau_ {\alpha} (B) ] c \\ \geq [ k ^ {r} - (k ^ {r} - \overline {{p}}) ] \theta \overline {{\omega}} \\ \quad - \sum_ {B \in B _ {r + 1}} \pi (B) [ r - \tau_ {\alpha} (B) ] c \\ = \left[ \sum_ {B \in B _ {r + 1}} (k ^ {r - \tau_ {\alpha} (B)} - 1) \right] \theta \overline {{\omega}} \\ \quad - \sum_ {B \in B _ {r + 1}} \pi (B) [ r - \tau_ {\alpha} (B) ] c, \end{array}
$$

and thus,

$$
\begin{array}{l} \Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) - [ \Omega (\sigma) - \Gamma (\sigma) ] \\ \geq \sum_ {B \in B _ {r + 1}} \left\{k ^ {r - \tau_ {\alpha} (B)} - 1\right) \theta \overline {{\omega}} \\ \qquad - \pi (B) [ r - \tau_ {\alpha} (B) ] c \}. \end{array}\tag{17}
$$

Now, let $B \in B_{r+1}$ be arbitrary, and define

$$
\chi (B) = \left(k ^ {r - \tau_ {\alpha} (B)} - 1\right) \theta \overline {{{{\omega}}}} - \pi (B) [ r - \tau_ {\alpha} (B) ] c.\tag{18}
$$

We consider two cases.

(a) $\tau_{\alpha}(B) = r$ . In this case, (18) becomes

$$
\chi (B) = (k ^ {0} - 1) \theta \overline {{{{\omega}}}} - \pi (B) \cdot 0 \cdot c = 0.\tag{19}
$$

(b) $\tau_{\alpha}(B) \in \{1, \ldots, r - 1\}$ . Since $r - \tau_{\alpha}(B) > 0$ in this case, we see that

$$
\begin{array}{r l} \chi (B) & \geq 0 \Leftrightarrow \theta \overline {{\omega}} [ k ^ {r - \tau_ {\alpha} (B)} - 1 ] / [ r - \tau_ {\alpha} (B) ] \\ & \geq \pi (B) c. \end{array}\tag{20}
$$

However, it is easy to prove that, since $k \geq 2$ ,

$$
(k ^ {q} - 1) / q \geq k - 1 \quad \text { for } \quad q = 1, 2, \dots ,
$$

and thus

$$
\theta \overline {{{{\omega}}}} \big [ k ^ {r - \tau_ {\alpha} (B)} - 1 \big ] / \big [ r - \tau_ {\alpha} (B) \big ] \geq (k - 1) \theta \overline {{{{\omega}}}}.\tag{21}
$$

However, by assumption (8) and the fact that $B \subseteq X$ , we have

$$
(k - 1) \theta \overline {{{{\omega}}}} \geq c \geq \pi (B) c,\tag{22}
$$

and thus it follows from (20)-(22) that $\chi(B) \geq 0$ in this case as well.

From our analysis of the two possible cases, we see that the right-hand-side of (17) is a sum of non-negative terms, and it follows that

$$
\begin{array}{l} \Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) \geq \Omega (\sigma) - \Gamma (\sigma). \\ \text { Q.E.D. } \end{array}
$$

5.2.2. Corollary. If $\pmb{D}$ is of the only correct guesses count form, and satisfies

$$
(k - 1) \overline {{{\omega}}} / m \geq c,\tag{23}
$$

and $\sigma^{*} = \langle \alpha^{*},\mathbf{B}_{r + 1}^{*},\delta^{*}\rangle$ is an efficient strategy for $D$ satisfying

$$
\# B _ {r + 1} ^ {*} = k ^ {r}, \quad \text { then }
$$

(i) the expected net return from $\sigma^{*}$ is given by

$$
\Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) = k ^ {r} \overline {{{{\omega}}}} / m - r c,
$$

(ii) $\sigma^{*}$ is optimal for $D$ .

Proof. We first note that, in the notation of Theorem 1 we have

$$
\theta_ {i} = 1 / m \quad \text { for } \quad i = 1, \dots , q.
$$

Thus, since $\# B_{r+1}^{*}=k^{r}$ , it is clear that hypotheses (8) and (9) of Theorem 1 are satisfied. Since $D$ is of the only correct guesses count form [and thus satisfies (7) as well], it then follows from Theorem 1 that

$$
\Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) = \left(\sum_ {j = 1} ^ {k ^ {\prime}} \theta_ {i}\right) \overline {{{{\omega}}}} - r c = k ^ {r} \overline {{{{\omega}}}} / m - r c,
$$

and $\sigma^{*}$ is optimal for $D$ . Q.E.D.

In the case where D has the structure assumed in Theorem 1, the following provides a simple condition for constructing admissible strategies for D.

5.2.3. Proposition. Suppose $\pmb{D}$ satisfies

$$
\boldsymbol {X} \geq \boldsymbol {B} ^ {A}, \quad \text { and }\tag{24}
$$

$$
\overline {{{\omega}}} \theta_ {q} > c,\tag{25}
$$

and that $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is an efficient strategy for $D$ such that for some $t \in \{1, \ldots, r\}$ and some $B \in B_t$ we have

$$
\boldsymbol {B} \notin \boldsymbol {B} ^ {A} \quad \text { and } \quad \alpha_ {i} (\boldsymbol {B}) = 0.\tag{26}
$$

Then $\sigma$ is strictly dominated.

Proof. If $B \in B_t$ satisfies (26), it follows from Proposition 2.4.7 that there exists $\hat{a} \in A$ such that $\#_{\iota}(B, \hat{a}) \geq 2$ .

Thus, using (the proof of) Proposition 4.1.3, we see that

$$
\begin{array}{l} \left[ 1 / \pi (B) \right] \left[ \sum_ {B ^ {\prime} \in \iota (B, \hat {a})} \pi \left(B ^ {\prime}\right) v \left(B ^ {\prime}\right) \right. \\ \quad - \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ = [ \bar {\omega} / \pi (B) ] \\ \times \left[ \sum_ {B ^ {\prime} \in \iota (B, \hat {a})} \max \left\{\psi \left(B ^ {\prime \prime}\right) \mid B ^ {\prime \prime} \in B ^ {A} \left(B ^ {\prime}\right) \right\} - \max \left\{\psi \left(B ^ {\prime \prime}\right) \mid B ^ {\prime \prime} \in B ^ {A} (B) \right\} \right]. \end{array} \tag {27}\tag{27}
$$

However, since $\iota(B, \hat{a})$ is a partition of $B$ , and each $B' \in \iota(B, \hat{a})$ is $n$ -feasible,

$$
\bigcup_ {B ^ {\prime} \in \iota (B, \hat {a})} B ^ {A} (B ^ {\prime}) = B ^ {A} (B).
$$

Therefore, if

$$
\max \left\{\psi (B ^ {\prime \prime}) \mid B ^ {\prime \prime} \in B ^ {A} (B) \right\} = \theta_ {h},
$$

it follows from the fact that $\# \iota(B, \hat{a}) \geq 2$ that there exists $i \in \{1, \ldots, q\}$ such that

$$
\begin{array}{l} \left[ \overline {{\omega}} / \pi (B) \right] \\ \times \left[ \sum_ {B ^ {\prime} \in \iota (B, \hat {a})} \max \left\{\psi (B ^ {\prime \prime}) \mid B ^ {\prime \prime} \in B ^ {A} (B ^ {\prime}) \right\} - \max \left\{\psi (B ^ {\prime \prime}) \mid B ^ {\prime \prime} \in B ^ {A} (B) \right\} \right] \\ \geq \left[ \overline {{\omega}} / \pi (B) \right] \left[ \theta_ {h} + \theta_ {i} - \theta_ {h} \right] \\ \geq \overline {{\omega}} \theta_ {q} / \pi (B). \end{array}\tag{28}
$$

However, it follows from (25), (27), (28), and the

fact that $0 < \pi(B) \leq 1$ , that

$$
\begin{array}{r l} & {\left[ 1 / \pi (B) \right] \Bigg [ \sum_ {B ^ {\prime} \in \iota (B, \hat {a})} \pi (B ^ {\prime}) \nu (B ^ {\prime})} \\ & {\qquad - \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \Bigg ] > c,} \end{array}
$$

and it then follows from Proposition 3.2.3 that $\sigma$ is strictly dominated. Q.E.D.

## 5.3. Balanced Strategies

In section 5.1 we presented a result (Proposition 5.1.6) which gave an upper bound on the number of sets in the final information structure. In some situations, however, we can provide a more exact characterization of the number of sets in the final information structure. One of these situations is defined by the following (note: in the following we shall use the $B_{t}^{0}$ , $B_{t}^{1}$ , $B_{t}^{2}$ partition of $B_{t}$ that was introduced in section 5.1.

5.3.1. Definition. Let D be a k-element information structure problem, and let $I \in \{0, 1, \ldots, k - 1\}$ . We shall say that a feasible information-gathering strategy for D,

$$
\alpha = \langle (B _ {1}, \alpha_ {1}), \dots , (B _ {r}, \alpha_ {r}) \rangle
$$

is a $(k, I)$ -balanced (informational) strategy for $D$ iff $\alpha$ satisfies

(1) $\# B_{2} = k$ (and thus $\# B_{1}^{2} = 1$ and $\# B_{1}^{1} = 0$ ).

(2) $\# B_{t+1} = k (\# B_t^2) + \sum_{s=1}^{t} \# B_s^1$ for $t = 1, \ldots, r$ .

(3) $\# B_t^1 = I(\# B_{t-1}^2)$ for $t = 2, \ldots, r$ .

(We shall say that a feasible strategy, $\sigma = \langle \alpha, B_{r+1}, \delta \rangle$ is a $(k, I)$ -balanced strategy if $\alpha$ is a $(k, I)$ -balanced strategy.)

Thus with a $(k, I)$ -balanced strategy, $\alpha_{t}(B) \neq 0$ implies

$$
\# \iota [ B, \alpha_ {t} (B) ] = k,
$$

for $B \in B_t$ , $t = 1, \ldots, r$ (experimentation is performed only when there are $k$ -possible outcomes, given the information available beforehand). Furthermore, (on average) each time a non-null experiment is undertaken at $t \in \{1, \ldots, r-1\}$ on $B \in B_t$ , no new experimentation is undertaken on $I$ of the sets in $t[B, \alpha_t(B)]$ at $t+1$ . The most likely situation in which this latter condition will happen is when it is true that for each $B \in B_t$ and each $a \in A$ , $\iota(B, a)$ contains $I$ sets from $B^{A}$ . We will find this sort of situation to obtain, for example, in the computer file search problem.

5.3.2. Proposition. If $D$ is a $k$ -element information structure problem, $I \in \{0, 1, \ldots, k-1\}$ , and $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$

is a $(k, I)$ -balanced strategy for $D$ , then

(i) $\# B_{t}^{2} = (k - I)^{t - 1}$ for $t = 1,\dots ,r$

(ii) $\# B_t^1 = I(k - I)^{t - 2}$ for $t = 2,\dots ,r$

$$
(i i i) \sum_ {s = 1} ^ {t} \left(\# B _ {s} ^ {1}\right)
$$

$$
= \left\{ \begin{array}{l} I \left[ \frac {(k - I) ^ {t - 1} - 1}{k - I - 1} \right] \\ \text { for } \quad I \in \{0, \dots , k - 2 \} \\ I (t - 1) \\ \text { for } \quad I = k - 1 \end{array} \right\}
$$

for $t = 1,\dots ,r$

(iv) $\# B_{t}$

$$
= \left\{ \begin{array}{c} \frac {(k - 1) (k - I) ^ {t - 1} - I}{k - I - 1} \\ \text { for } \quad I \in \{0, \dots , k - 2 \} \\ I (t - 1) + 1 \\ \text { for } \quad I = k - 1 \end{array} \right\}
$$

for $t = 1,\dots ,r + 1,$

where $B_{r+1}=R(B_{r},\alpha_{\tau})$ .

Proof. (i) We have [see (7) of section 5.1],

$$
\# B _ {t + 1} = \# B _ {t + 1} ^ {2} + \sum_ {s = 1} ^ {t + 1} \# B _ {s} ^ {1} \quad \text { for } \quad t = 1, \dots , r - 1,\tag{1}
$$

while, since $\alpha$ is a $(k, I)$ -balanced strategy,

$$
\# \boldsymbol {B} _ {t + 1} = k \left(\# \boldsymbol {B} _ {t} ^ {2}\right) + \sum_ {s = 1} ^ {t} \# \boldsymbol {B} _ {s} ^ {1} \quad \text { for } \quad t = 1, \dots , r,\tag{2}
$$

$\# B_{t}^{1} = I\left(\# B_{t - 1}^{2}\right)$ for $t = 2,\dots ,r,$ and (3)

$\# B_{2} = k, \# B_{1}^{2} = 1, \# B_{1}^{1} = 0.$

(4)

Substituting (3) into (1) and (2), and equating

the result, we obtain

$$
\begin{array}{l} \# B _ {t + 1} ^ {2} + \sum_ {s = 2} ^ {t + 1} I (\# B _ {s - 1} ^ {2}) \\ = k (\# B _ {t} ^ {2}) + \sum_ {s = 2} ^ {t} I (\# B _ {s - 1} ^ {2}), \end{array}
$$

from which we have

$$
\# B _ {t + 1} ^ {2} = (k - I) \left(\# B _ {t} ^ {2}\right) \quad \text { for } \quad t = 1, 2, \dots , r - 1.\tag{5}
$$

From the initial condition (4), eq. (5), and a trivial induction argument, we obtain

$$
\# B _ {t} ^ {2} = (k - I) ^ {t - 1} \quad \text { for } \quad t = 1, \dots , r.\tag{6}
$$

(ii) From (3) and (6) we obtain

$$
\# B _ {t} ^ {1} = I (k - I) ^ {t - 2} \quad \text { for } \quad t = 2, \dots , r.\tag{7}
$$

(iii) It follows at once from (7) that

$$
\sum_ {s = 1} ^ {t} \# B _ {s} ^ {1} = I \sum_ {s = 2} ^ {t} (k - I) ^ {s - 2} = I \sum_ {s = 0} ^ {t - 2} (k - I) ^ {s}\tag{8}
$$

From (8) we obtain two cases

$$
\begin{array}{l l} \sum_ {s = 1} ^ {t} \# B _ {s} ^ {1} = I (t - 1) & \text { for } \quad t = 1, \dots , r, \\ \text { if } \quad I = k - 1, \end{array}\tag{9}
$$

and, using the formula for the partial sum of a geometric series

$$
\begin{array}{l} \sum_ {s = 1} ^ {t} \# B _ {s} ^ {1} = I \left[ \frac {(k - I) ^ {t - 1} - 1}{k - I - 1} \right] \quad \text { for } \quad t = 1, \dots , r, \\ \text { if } \quad I \in \{0, \dots , k - 2 \}. \end{array} \tag {10}
$$

(iv) From (2), (6), (9), and (10), we obtain

$$
\begin{array}{r l} & {\# B _ {t} = k (k - I) ^ {t - 2} + I (t - 2) = I (t - 1) + 1} \\ & {\quad \text {for} \quad t = 2, \dots , r, \quad \text {if} \quad I = k - 1, \quad \text {and}} \\ & {\# B _ {t} = k (k - I) ^ {t - 2} + I \left[ \frac {(k - I) ^ {t - 2} - 1}{k - I - 1} \right]} \\ & {\qquad = \left[ k (k - I) ^ {t - 1} - k (k - I) ^ {t - 2} \right.} \\ & {\qquad \qquad \qquad \qquad \qquad \qquad + I (k - I) ^ {t - 2} - I ]} \\ & {\qquad \times [ k - I - 1 ] ^ {- 1}} \\ & {\qquad = \frac {(k - 1) (k - I) ^ {t - 1} - I}{k - I - 1}} \\ & {\text {for} \quad t = 2, \dots , r + 1, \quad \text {if} \quad I \in \{0, \dots , k - 2 \}.} \end{array}
$$

Since the formulas

$$
\begin{array}{l} f (t) = I (t - 1) + 1, \quad \text { and } \\ g (t) = \left[ (k - 1) (k - I) ^ {t - 1} - I \right] / [ k - I - 1 ], \\ \text { yield } \\ f (1) = g (1) = 1 = \# B _ {1}, \\ \text { our   conclusion   follows. } \quad \text { Q.E.D. } \end{array}
$$

It is entirely possible that the only interesting application of our next result is to the computer file search problem. However, since the hypotheses are satisfied in a much wider class of problems, we present the result here rather than postponing it to section 6.5.

5.3.3. Proposition. Suppose D is a k-element information structure problem with constant information cost, $c \geq 0$ ; and suppose $\alpha = \langle (B_{1}, \alpha_{1}), \ldots, (B_{r}, \alpha_{r}) \rangle$ is a $(k, I)$ -balanced strategy for D such that for each $t \in \{1, \ldots, r\}$ , and each $B \in B_{t}^{1}$ , we have $\pi(B) = p > 0$ . Then

$$
\gamma (\alpha) = \left\{ \begin{array}{c} (c / 2) [ 2 r - p I r (r - 1) ] \\ \text {if} \quad I = k - 1, \\ \left\{c / (k - I - 1) \right\} \\ \cdot \left\{r (k - I - 1 + p I) \right. \\ \left. - p I [ (k - I) ^ {r} - 1 ] \right. \\ / [ k - I - 1 ] \} \\ \text {if} \quad I \in \{0, \dots , k - 2 \}. \end{array} \right.
$$

Proof. From Proposition 2.3.2 and the definition of $B_t^2$ , we have

$$
\begin{array}{l} \gamma (\alpha) = \sum_ {t = 1} ^ {r} \sum_ {B \in B _ {t}} \pi (B) c [ \alpha_ {t} (B) ] \\ = c \left[ \sum_ {t = 1} ^ {r} \sum_ {B \in B _ {t} ^ {2}} \pi (B) \right] \\ = c \left(\sum_ {t = 1} ^ {r} \left[ 1 - \sum_ {s = 1} ^ {t} \sum_ {B \in B _ {s} ^ {1}} \pi (B) \right]\right) \\ = c \left(\sum_ {t = 1} ^ {r} \left[ 1 - p \sum_ {s = 1} ^ {t} (\# B _ {s} ^ {1}) \right]\right) \\ = c \left(r - p \sum_ {t = 1} ^ {r} \sum_ {s = 1} ^ {t} \# B _ {s} ^ {1}\right). \end{array}\tag{11}
$$

Using Proposition 2, we now distinguish two cases. (a) $I = k - 1$ . Here we have

$$
\sum_ {s = 1} ^ {t} \# B _ {s} ^ {1} = I (t - 1).\tag{12}
$$

Substituting (12) into (11), we then have

$$
\begin{array}{r l} \gamma (\alpha) & = c \left[ r - p I \sum_ {t = 1} ^ {r} (t - 1) \right] \\ & = c \left(r - p I \left[ \frac {r (r - 1)}{2} \right]\right) \\ & = (c / 2) [ 2 r - p I r (r - 1) ]. \end{array}
$$

(b) $I \in \{0, \ldots, k - 2\}$ . Here we have

$$
\sum_ {s = 1} ^ {t} \# B _ {s} ^ {1} = I [ (k - I) ^ {t - 1} - 1 ] / (k - I - 1).\tag{13}
$$

Substituting (13) into (11), we then obtain

$$
\begin{array}{r l} \gamma (\alpha) & = c \left(r - p I / (k - I - 1) \times \sum_ {t = 1} ^ {r} \left[ (k - I) ^ {t - 1} - 1 \right]\right) \\ & = c \left[ r + r p I / (k - I - 1) - p I / (k - I - 1) \sum_ {t = 1} ^ {r} (k - I) ^ {t - 1} \right] \\ & = c \left\{r + r p I / (k - I - 1) - p I \left[ (k - I) ^ {r} - 1 \right] / (k - I - 1) ^ {2} \right\} \\ & = \left\{c / (k - I - 1) \right\} \\ & \cdot \left\{r (k - I - 1 + p I) - p I \left[ (k - I) ^ {r} - 1 \right] / (k - I - 1) \right\}. \end{array}
$$

Q.E.D.

The special case of the above result which will be pertinent to our analysis of the computer file search problem is the following; the proof of which is immediate.

5.3.4. Corollary. Under the hypotheses of 5.3.3, and with $k = 3$ and $I = 1$ , we have

$$
\gamma (\alpha) = c [ r (1 + p) - p (2 ^ {r} - 1) ].
$$

While the results of this subsection have direct applications to both the 'only correct guesses count' problem and the computer file search problem, we shall postpone our discussion of these applications until after we have developed the theoretical results of the next section.

6. Binary and Trinary Information Structures with a Linear Ordering on the Set of Experiments

## 6.1. Introduction

Throughout this section we shall suppose that D is a k-element information structure problem, and that k is either two or three; that is, that information is either binary or trinary. Many of the concepts, and some of the results we shall develop here are valid for $k \geq 4$ as well; but the key results, those which make the material to follow of real use, do not hold (or hold only in trivial special cases) for $k \geq 4$ .

By way of introducing the material to follow, suppose k = 2, and consider the binary relation $\geq$ defined on $A_{1}$ by

$$
a \geq a ^ {\prime} \Leftrightarrow M _ {a 1} \supseteq M _ {a ^ {\prime} 1} \quad \text { for } \quad a, a ^ {\prime} \in A _ {1}.\tag{i}
$$

It is easy to show that $\geq$ is a partial order on $A_{1}$ (that is, it is reflexive, transitive, and antisymmetric), $^{21}$ and has the asymmetric part, $>$ given by $^{22}$

$$
a ^ {\prime} > a ^ {\prime} \Leftrightarrow M _ {a ^ {\prime} 1} \subset M _ {a 1}\tag{2}
$$

In section 6.4, below, we shall explore some implications of the assumption that $\geq$ is total on $A_{1}$ . Since $\geq$ is a partial order on $A_{1}$ (and thus antisymmetric), it follows, however, that if $\geq$ is total, then $>$ is total $^{23}$ as well; and, conversely, if $>$ is total, then $\geq$ is total. Consequently, rather than assuming that $\geq$ is total, we can equivalently (and shall) proceed by assuming that $>$ is total on $A_{1}$ .

In the trinary case $(k = 3)$ , we proceed by first

$^{22}$ Where we use the notation ‘ $A \subset B$ ’ to indicate that A is a proper subset of B; i.e., $A \subseteq B$ and $A \neq B$ .

$^{23}$ That is, for all $a, a' \in A_{1}$ , we have $a > a', a' > a$ , or $a = a'$ .

defining $^{'}$ > on $A_{1}$ as a slight strengthening of (2)

$$
a ^ {2} > a ^ {\prime} \Leftrightarrow M _ {a ^ {\prime} 1} \cup M _ {a ^ {\prime} 2} \subset M _ {a 1}.\tag{3}
$$

It is easily shown that the relation $'>$ defined in (3) is asymmetric and transitive. In section 6.2 we will explore the implications of the assumption that it is total as well.

In the next three subsections we shall treat the trinary and binary case separately. It would be possible to treat the two cases simultaneously [although we would have to introduce a new condition in place of (2) for the binary case], but this would require our introducing some new notation which would serve no purpose other than to allow us to treat the two cases simultaneously.

While we shall assume in both subsections that the pertinent ordering is total on $A_1$ , it should be noted that in each case the results are applicable on any chain in $A_1$ . That is, in section 6.2-6.4 we could replace $A_1$ with some (possibly proper) subset of $A_1$ , call it $A^*$ , on which $>$ is total. We shall discuss this extension very briefly in section 6.5.

## 6.2. The Linear Ordering in the Trinary Case

Throughout this section we shall assume that D is a trinary information structure problem. Moreover, defining ' > on $A_{1}$ by

$$
a ^ {\prime} > a ^ {\prime} \Leftrightarrow M _ {a ^ {\prime} 1} \cup M _ {a ^ {\prime} 2} \subset M _ {a 1},\tag{1}
$$

we assume that $'>$ is total on $A_{1}$ . Since $'>$ is total on $A_{1}$ , we can also suppose, without loss of generality that our experiments are numbered in such a way that $'>$ coincides with the usual strict inequality for the real numbers. Thus

$$
(\forall i, j \in A _ {1}): i > j \Leftrightarrow M _ {j 1} \cup M _ {j 2} \subset M _ {i 1}.\tag{2}
$$

It will be convenient in the following to adjoin to $A_{1}$ the two elements 0 and $n + 1$ , where we define

$$
\boldsymbol {M} _ {0} = \left\{M _ {0 1}, M _ {0 2}, M _ {0 3} \right\} \quad \text { with }
$$

$$
M _ {0 1} = M _ {0 2} = \emptyset , M _ {0 3} = X, \quad \text { and }
$$

$$
M _ {n + 1} = \left\{M _ {n + 1, 1}, M _ {n + 1, 2}, M _ {n + 1, 3} \right\} \quad \text { with }\tag{3}
$$

$$
M _ {n + 1, 1} = X, M _ {n + 1, 2} = M _ {n + 1, 3} = \emptyset .\tag{4}
$$

Defining

$$
\hat {A} = A _ {1} \cup \{0, n + 1 \} = \{0, 1, \dots , n + 1 \},\tag{5}
$$

we can then prove the following.

6.2.1. Lemma. With the definitions (3)-(5), above, $^{'} >$ is total on $\hat{A}$ and coincides with the usual strict inequality for the real numbers on $\hat{A}$ ; that is

$$
(\forall i, j \in \hat {A}): j > i \Leftrightarrow M _ {i 1} \cup M _ {i 2} \subset M _ {j 1}.\tag{6}
$$

Moreover, we have

$$
(\forall i, j \in \hat {A}): j > i \Leftrightarrow M _ {j 2} \cup M _ {j 3} \subset M _ {i 3}.\tag{7}
$$

Proof. In order to establish (6) it obviously (given our previous reasoning) suffices to establish (6) for the special case where $\{i, j\} \cap \{0, n + 1\} \neq \emptyset$ . However, if $i = 0$ and $j \in \{1, \ldots, n + 1\}$ then $M_{j1} \neq \emptyset$ , while

$$
M _ {i 1} \cup M _ {i 2} = \emptyset .
$$

Thus, for $i = 0$ and $j \in \{1, \dots, n + 1\}$

$$
\emptyset = M _ {i 1} \cup M _ {i 2} \subset M _ {j 1}.
$$

Similarly, if $j = n + 1$ and $i \in \{0, 1, \ldots, n\}$ , then $M_{j1} = X$ , while

$$
\begin{array}{l} M _ {i 3} \neq \emptyset , \quad \text { so   that } \\ X \neq X \backslash M _ {i 3} = M _ {i 1} \cup M _ {i 3}, \quad \text { Therefore } \\ M _ {i 1} \cup M _ {i 2} \subset M _ {j 1} \end{array}
$$

in this case as well.

Now let $i, j \in \hat{A}$ be such that $j > i$ . Then by (6) we have

$$
M _ {i 1} \cup M _ {i 2} \subset M _ {j 1}, \quad \text { so   that }
$$

$$
M _ {j 2} \cup M _ {j 3} = X \backslash M _ {j 1} \subset X \backslash (M _ {i 1} \cup M _ {i 2}) = M _ {i 3}.
$$

Conversely, if $i, j \in \hat{A}$ such that

$M_{j2} \cup M_{j3} \subset M_{i3},$ then

$$
M _ {i 1} \cup M _ {i 2} = X \backslash M _ {i 3} \subset X \backslash \left(M _ {j 2} \cup M _ {j 3}\right) = M _ {j 1},
$$

and thus by (6), $j > i$ . Q.E.D.

The following sets forth the basic facts regarding intersections of $M_{ay}, M_{a'y'}$ .

6.2.2. Proposition. For all $i, j, k \in \hat{A}$ , we have

$$
(i) M _ {j 1} \cap M _ {i 3} \neq \emptyset \Leftrightarrow j > i,
$$

$$
(i i) k \geq j \rightarrow M _ {k 2} \cap M _ {j 1} = \emptyset ,
$$

$$
(i i i) k \leq i \rightarrow M _ {k 2} \cap M _ {i 3} = \emptyset ,
$$

$$
(i v) j \neq k \rightarrow M _ {k 2} \cap M _ {j 2} = \emptyset ,
$$

$$
(v) i <   k <   j \rightarrow M _ {j 1} \cap M _ {k 2} \cap M _ {i 3} = M _ {k 2}.
$$

Proof. (i) If $j \leq i$ , $M_{j1} \subseteq M_{i1}$ . Since $M_{i1} \cap M_{i3} =$

Using (15), define

$$
i = \max A _ {\eta} ^ {3} \quad \text { and } \quad j = \min A _ {\eta} ^ {1}.\tag{16}
$$

It then follows at once from (14) that

$$
\boldsymbol {B} \subseteq M _ {j 1} \cap M _ {i 3},\tag{17}
$$

and since $B \neq \emptyset$ (by the assumption that $B$ is $n$ -feasible), it follows from (i) of Proposition 2 that

$$
j \geq i + 1.\tag{18}
$$

Furthermore, by Lemma 1, we also have

$$
\bigcap_ {a \in A _ {\eta} ^ {1}} M _ {a 1} = M _ {j 1}, \quad \text { and }\tag{19}
$$

$$
\bigcap_ {a \in A _ {\eta} ^ {3}} M _ {a 3} = M _ {i 3}.\tag{20}
$$

From (14) and (18)-(20), we have, therefore

$$
j \in \{i + 1, \dots , n + 1 \} \quad \text { and }
$$

$$
B = M _ {j 1} \cap \left(\bigcap_ {a \in A _ {\eta} ^ {2}} M _ {a 2}\right) \cap M _ {i 3}.\tag{21}
$$

Next, we note that, again using the fact that $B \neq \emptyset$ , it follows at once from (21) and (iv) of Proposition 2 that there exists $k \in \{1, \ldots, n\}$ such that

$$
A _ {\eta} ^ {2} \subseteq \{k \}.\tag{22}
$$

Thus we can distinguish two cases, which are mutually exclusive and exhaustive.

(a) $A_{\eta}^{2} = \emptyset$ . In this case,

$$
\bigcap_ {a \in A _ {\eta} ^ {2}} M _ {a 2} = X,
$$

and it follows from (21) that

$B = M_{j1}\cap M_{i3}$ with $i\in \{0,1,\dots ,n\}$ and

$$
j \in \{i + 1, \dots , n + 1 \}.\tag{23}
$$

(b) $A_{\eta}^{2} = \{k\}$ for some $k \in \{1, \ldots, n\}$ . In this case we have from (21) that

$$
B = M _ {j 1} \cap M _ {k 2} \cap M _ {i 3}.\tag{24}
$$

However, from (ii) and (iii) of Proposition 2 we see that, since $B \neq \emptyset$ , we must then have

$$
i <   k <   j,
$$

and it then follows from (24) and (v) of Proposition 2 that $B = M_{k2}$ . Q.E.D.

We will make heavy use of the following definition in the remainder of this subsection.

6.2.4. Definition. For each $i \in \{0, 1, \ldots, n\}$ and each $j \in \{i + 1, \ldots, n + 1\}$ , we define $B_{ij} \subseteq X$ by $B_{ij} = M_{j1} \cap M_{i3}$ .

Notice that with the use of the above definition, we can give an equivalent statement of Theorem 3 as

6.2.3'. Theorem. If $B \subseteq X$ is $n$ -feasible, then exactly one of the following holds:

(a) $B = B_{ij}$ for some $i\in \{0,\dots ,n\}$ ， $j\in \{i+$ $1,\ldots ,n + 1\}$ or

(b) $B = M_{k2}$ for some $k \in \{1, \ldots, n\}$ .

From Theorem 3 or $3'$ , we see that if $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $D$ , $B_{r+1} = R(B_r, \alpha_r)$ , $t \in \{1, \ldots, r\}$ , and $B \in B_t$ , then $B$ is of either the form given by (a), or by (b) in Theorem $3'$ , above. Since this is the case, a question of obvious interest is, what is the form of $\iota(B, a)$ for $a \in A_1$ ? This is the subject matter of the following result.

6.2.5. Theorem. Suppose $i \in \{0, \ldots, n\}$ , $j \in \{i + 1, \ldots, n + 1\}$ , and $k \in \{0, 1, \ldots, n + 1\}$ . Then we have:

(i) (a) $\# \iota(B_{ij}, k) > 1$ if, and only if, $k \in \{i + 1, \ldots, j - 1\}$ ,  
(b) $k \in \{i + 1, \ldots, j - 1\}$ implies $\iota(B_{ij}, k) = \{B_{ik}, M_{k2}, B_{kj}\}$ , and

(ii) $\iota(M_{i2}, k) = \{M_{i2}\}$ .

Proof. (i) Suppose $i \in \{0, \ldots, n\}$ , $j \in \{i + 1, \ldots, n + 1\}$ , and $k \in \hat{A}$ . Then

$$
\begin{array}{r l} \iota (B _ {i j}, k) & = \left\{B _ {i j} \cap M _ {k 1}, B _ {i j} \cap M _ {k 2}, B _ {i j} \cap M _ {k 3} \right\} \\ & \backslash \{\emptyset \}. \end{array} \tag {2}\tag{25}
$$

However, if $k < i$ , then by Proposition 2,

$$
\begin{array}{r l} B _ {i j} \cap M _ {k 1} & = (M _ {j 1} \cap M _ {i 3}) \cap M _ {k 1} \\ & = M _ {j 1} \cap (M _ {k 1} \cap M _ {i 3}) = M _ {j 1} \cap \emptyset = \emptyset , \end{array}
$$

and

$$
\iota \left(B _ {i j}, k\right) = \left\{B _ {i j} \cap M _ {k 3} \right\}, \quad \text { and }
$$

$$
B _ {i j} \cap M _ {k 3} = M _ {j 1} \cap (M _ {i 3} \cap M _ {k 3}) = M _ {i 1} \cap M _ {i 3} = B _ {i j}.
$$

$$
M _ {k 2} \cap M _ {k 3} = \emptyset = M _ {k 1} \cap M _ {k 3},
$$

$$
k = i,
$$

$$
\iota (B _ {i j}, k) = \left\{B _ {i j} \right\}.
$$

Similarly, it is easy to show that if $j \leq k$ , then $\iota(B_{ij}, k) = \{B_{ij}\}$ .

On the other hand, if $k \in \{i + 1, \ldots, j - 1\}$ , then $M_{k1} \subseteq M_{j1}$ , and

$$
B _ {i j} \cap M _ {k 1} = (M _ {j 1} \cap M _ {i 3}) \cap M _ {k 1} = (M _ {j 1} \cap M _ {k 1})
$$

$$
\cap M _ {i 3} = M _ {k 1} \cap M _ {i 3} = B _ {i k}
$$

and, since $M_{k3} \subseteq M_{i3}$ ,

$$
\begin{array}{r l} B _ {i j} \cap M _ {k 3} & = M _ {j 1} \cap (M _ {i 3} \cap M _ {k 3}) = M _ {j 1} \cap M _ {k 3} \\ & = B _ {k j}; \end{array}
$$

while by (v) of Proposition 2,

$$
\boldsymbol {B} _ {i j} \cap M _ {k 2} = M _ {k 2}.
$$

Thus we see that if $\# \iota(B_{ij,k}) > 1$ , $k \in \{i + 1, \ldots, j - 1\}$ ; while if $k \in \{i + 1, \ldots, j - 1\}$ ,

$$
\iota \left(B _ {i j}, k\right) = \left\{B _ {i k}, M _ {k 2}, B _ {k j} \right\},
$$

and thus

$$
\# \iota (B _ {i j}, k) = 3 > 1.
$$

(ii) It is immediate that if $k = i$ , then

$$
\iota (M _ {i 2}, k) = \left\{M _ {i 2} \right\}.
$$

Suppose now that $k \neq i$ . Then

$i < k \to M_{i2} \subseteq M_{k1}$ , so that $M_{i2} \cap M_{k2} = M_{i2} \cap M_{k3} = \emptyset$ , while, by (7) of Lemma 1 $i > k \to M_{i2} \subseteq M_{k3}$ , and thus $M_{i2} \cap M_{k1} = M_{i2} \cap M_{k2} = \emptyset$ .

Therefore, in all possible cases, we have $\iota(M_{i2}, k) = \{M_{i2}\}$ . Q.E.D.

The following two results are more or less immediate implications of the previous two theorems, and their proof will be left to the interested reader.

6.2.6. Corollary. If $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $D$ , and we define

$$
\boldsymbol {B} _ {r + 1} = R \left(\boldsymbol {B} _ {r}, \alpha_ {r}\right),
$$

then for every $t \in \{1, \ldots, r + 1\}$ and every $B \in B_t$ , either

(i) there exists $i \in \{0, \ldots, n\}$ and $j \in \{i + 1, \ldots, n + 1\}$ such that $B = B_{ij}$ , or

(ii) there exists $k \in \{1, \ldots, n\}$ such that $B = M_{k2}$ . Furthermore, if $\alpha$ is efficient, and $t$ and $B$ are such that $t \in \{1, \ldots, r\}$ , $B \in B_t$ , and

$$
\alpha_ {i} (B) \neq 0,
$$

then there exists $i \in \{0, \ldots, n-1\}$ and $j \in \{i+2, \ldots, n+1\}$ such that

$$
B = B _ {i j} \quad \text { and } \quad \alpha_ {i} (B) \in \{i + 1, \dots , j - 1 \}.
$$

6.2.7. Corollary. The family $B^{A}$ contains $2n+1$ elements, and is given by

$$
\boldsymbol {B} ^ {A} = \left\{M _ {1 2}, M _ {2 2}, \dots , M _ {n 2}, B _ {0 1}, B _ {1 2}, \dots , B _ {n, n + 1} \right\}.
$$

We will be able to use the results obtained here to develop a dynamic programming solution for D for the case where $r \geq n$ ; which solution will be developed in the next subsection. However, in some cases, most notably that where D has the 'only correct guesses count' form, finding an optimal solution essentially amounts to a matter of finding the feasible final information structure having the largest possible number of elements. In such a context, the following result will be of particular interest (see also 6.2.9, below).

6.2.8. Theorem. If $r$ and $n$ satisfy $2^r \leq n + 1$ , then there exists a (3, 1)-balanced strategy for $D$ . Furthermore, if $\alpha = \langle (\pmb{B}_1, \alpha_1), \ldots, (\pmb{B}_r, \alpha_r) \rangle$ is a (3, 1)-balanced strategy for $D$ and $B_{r+1} = R(B_r, \alpha_r)$ , then $\# B_{r+1} = 2^{r+1} - 1$ .

Proof. We begin be defining p as that unique integer satisfying

$$
p \leq \log_ {2} (n + 1) <   p + 1, \quad \text { and }
$$

$$
n ^ {*} = 2 ^ {p} - 1,\tag{25}
$$

(26)

and we note that

$$
n ^ {*} \leq n \quad \text { and } \quad r \leq p.\tag{27}
$$

Next, define $N_{i}$ by

$$
N _ {t} = 2 ^ {t - 1} - 1 \quad \text { for } \quad t = 2, \dots , r,\tag{28}
$$

and the $r - 1$ sequences, $\langle j_q^\prime \rangle$ by

$$
j _ {q} ^ {t} = \left\{ \begin{array}{l l} q 2 ^ {[ p - (t - 1) ]} & \text { for } \quad q = 0, 1, \dots , N _ {t} \\ n + 1 & \text { for } \quad q = N _ {t} + 1 = 2 ^ {t - 1} \end{array} \right\}
$$

$$
\text { for } \quad t = 2, \dots , r.\tag{29}
$$

(Since $j_{N_t + 1}^t = n + 1$ for each $t$ , we shall generally simply write $n + 1$ in place of $j_{N_t + 1}^t$ in the following.)

We now define the (3, 1)-balanced strategy, $\alpha = \langle (\pmb{B}_1, \alpha_1), \ldots, (\pmb{B}_r, \alpha_r) \rangle$

inductively, as follows. First let

$$
\alpha_ {1} (X) = \frac {n ^ {*} + 1}{2} = 2 ^ {p} / 2 = 2 ^ {p - 1} = j _ {1} ^ {2},\tag{30}
$$

and obtain, by Theorem 5

$$
\begin{array}{r l} \boldsymbol {B} _ {2} & = \left\{\boldsymbol {B} _ {0, j _ {1} ^ {2}}, \boldsymbol {B} _ {j _ {1} ^ {2}, n + 1}, \boldsymbol {M} _ {j _ {1} ^ {2}, 2} \right\} \\ & = \left\{\boldsymbol {B} _ {j _ {0} ^ {2}, j _ {1} ^ {2}}, \boldsymbol {B} _ {j _ {1} ^ {2}, n + 1}, \boldsymbol {M} _ {j _ {1} ^ {2}, 2} \right\}, \quad \text { so   that } \end{array}\tag{31}
$$

$$
\# B _ {2} = 3.\tag{32}
$$

Now suppose that after the $(t-1)$ st step (i.e., after defining $B_{t-1}$ and $\alpha_{t-1}$ for $t\geq2$ , we have obtained

$$
\boldsymbol {B} _ {t} = \left\{B _ {j _ {0} ^ {t}, j _ {1} ^ {t}}, B _ {j _ {1} ^ {t}, j _ {2} ^ {t}}, \dots , B _ {j _ {N t} ^ {t}, n + 1}, M _ {j _ {1} ^ {t}, 2}, \dots , M _ {j _ {N t} ^ {t}, 2} \right\}.\tag{33}
$$

Taking

$$
\boldsymbol {B} _ {t} ^ {2} = \left\{B _ {j _ {0} ^ {t}, j _ {1} ^ {t}}, \dots , B _ {j _ {N t} ^ {t}, n + 1} \right\}, \quad \text { and }\tag{34}
$$

$$
\bigcup_ {s = 2} ^ {t} \boldsymbol {B} _ {s} ^ {1} = \left\{M _ {j _ {1} ^ {t}, 2}, \dots , M _ {j _ {N _ {t}} ^ {t}, 2} \right\},\tag{35}
$$

we define $\alpha_{t}: B_{t} \to A$ by

$$
\alpha_ {t} (B) = 0 \text {   for   } B \in \bigcup_ {s = 2} ^ {t} B _ {s} ^ {1},\tag{36}
$$

and on $B_{t}^{2}$ we define $\alpha_{t}$ by

$$
\begin{array}{l} \alpha_ {t} \left(B _ {j _ {q - 1} ^ {t}, j _ {q} ^ {t}}\right) \\ = \left\{ \begin{array}{l l} \left(j _ {q - 1} ^ {t} + j _ {q} ^ {t}\right) / 2 & \text { for } \quad q = 1, \dots , N _ {t}, \\ j _ {N _ {t}} ^ {t} + 2 ^ {p - t} & \text { for } \quad q = N _ {t} + 1 = 2 ^ {t - 1}. \end{array} \right. \end{array}\tag{37}
$$

Now, for $q = 1, \ldots, N_t$ , we have

$$
\begin{array}{l} \alpha_ {t} \left(B _ {j _ {q - 1} ^ {t}, j _ {q} ^ {t}}\right) \\ = \frac {j _ {q - 1} ^ {t} + j _ {q} ^ {t}}{2} = \frac {2 q 2 ^ {p - (t - 1)} - 2 ^ {p - (t - 1)}}{2} \\ = (2 q - 1) 2 ^ {p - t} = j _ {q - 1} ^ {t} + \left(j _ {q} ^ {t} - j _ {q - 1} ^ {t}\right) / 2, \end{array}\tag{38}
$$

and

$$
j _ {q} ^ {t} - j _ {q - 1} ^ {t} = 2 ^ {p + 1 - t},
$$

we see that, for $t \leq r \leq p$ ,

$$
j _ {q - 1} ^ {t} + 1 \leq \alpha_ {t} \left(B _ {j _ {q - 1} ^ {t}, j _ {q} ^ {t}}\right) \leq j _ {q} ^ {t} - 1.\tag{39}
$$

Furthermore, by (38)

$$
\alpha_ {t} \left(B _ {j _ {q - 1} ^ {t}, j _ {q} ^ {t}}\right) = (2 q - 1) 2 ^ {p - t} = j _ {2 q - 1} ^ {t + 1}.\tag{40}
$$

Consequently, by (39), (40), and Theorem 5, we have

$$
\begin{array}{r l} \iota & \left[ B _ {j _ {q - 1} ^ {t}, j _ {q} ^ {t}}, \alpha_ {t} \left(B _ {j _ {q - 1} ^ {t} j _ {q} ^ {t}}\right) \right] \\ & = \left\{B _ {j _ {q - 1} ^ {t}, j _ {2 q - 1} ^ {t + 1}}, B _ {j _ {2 q - 1} ^ {t + 1}, j _ {q} ^ {t}}, M _ {j _ {2 q - 1, 2} ^ {t + 1}} \right\} \\ & \text {for} q = 1, \dots , N _ {t}. \end{array}\tag{41}
$$

Similarly

$$
\begin{array}{r l} \alpha_ {t} \left(B _ {j _ {N _ {t}}, n + 1}\right) & = j _ {N _ {t}} ^ {t} + 2 ^ {p - t} \\ & = (2 ^ {t - 1} - 1) 2 ^ {p - (t - 1)} + 2 ^ {p - t} \\ & = 2 ^ {p} - 2 ^ {p - (t - 1)} + 2 ^ {p - t} = 2 ^ {p} - 2 ^ {p - t} \\ & = (2 ^ {t} - 1) 2 ^ {p - t} \\ & = N _ {t + 1} 2 ^ {p - t} = j _ {N _ {t + 1}} ^ {t + 1}, \end{array} \tag {42}
$$

so that

$$
\alpha_ {t} \left(B _ {j _ {N _ {t}} ^ {t}, n + 1}\right) \geq j _ {N _ {t}} ^ {t} + 1,
$$

$$
\text { and,   since } t \leq r \leq p,
$$

$$
\alpha_ {t} \left(B _ {j _ {N _ {t}} ^ {\prime}, n + 1}\right) \leq 2 ^ {p} - 1 \leq n
$$

as well. Thus by Theorem 5,

$$
\begin{array}{l} \iota \left[ B _ {j _ {N _ {t}} ^ {t}, n + 1}, \alpha_ {t} \left(B _ {j _ {N _ {t}} ^ {t}, n + 1}\right) \right] \\ = \left\{B _ {j _ {N _ {t}} ^ {t}, j _ {N _ {t + 1}} ^ {t + 1}, B j _ {N _ {t + 1}} ^ {t + 1}, n + 2}, M _ {j _ {N _ {t + 1}} ^ {t + 1}, 2} \right\}. \\ \text { From   (33) - (35),   (41),   and   (43),   we   see   that } \end{array} \tag {1}\tag{43}
$$

$$
\# B _ {t + 1} = 3 \left(\# B _ {t} ^ {2}\right) + \sum_ {s = 2} ^ {t} \# B _ {s} ^ {1}.\tag{44}
$$

$$
\begin{array}{c} \boldsymbol {B} _ {t + 1} ^ {1} = \left\{M _ {j _ {1} ^ {t + 1}, 2}, M _ {j _ {3} ^ {t + 1}, 2}, \dots , \right. \\ \left. M _ {j _ {2 q - 1} ^ {t + 1}, 2}, \dots , M _ {j _ {N _ {t + 1}} ^ {t + 1}, 2} \right\}, \end{array}
$$

we see from (34), (38), and (41) that

$$
\# B _ {t + 1} ^ {1} = \# B _ {t} ^ {2}.\tag{45}
$$

$$
\text {   Finally,   we   note   that   } j _ {q - 1} ^ {t} = (q - 1) 2 ^ {p - (t - 1)} = [ 2 (q - 1) ] 2 ^ {p - t} = j _ {2 (q - 1)} ^ {t + 1}, \tag {46}\tag{46}
$$

$$
\begin{array}{l} \text {and} \\ j _ {q} ^ {t} = q 2 ^ {p - (t - 1)} = 2 q 2 ^ {p - t} = j _ {2 q} ^ {t + 1} \\ \text {for} q = 1, \dots , N _ {t - 1} = 2 ^ {t - 1} - 1; \text {while} \\ j _ {N _ {t}} ^ {t} = (2 ^ {t - 1} - 1) 2 ^ {p - (t - 1)} = [ (2 ^ {t} - 1) - 1 ] 2 ^ {p - t} \\ \quad = j _ {N _ {t + 1}} ^ {t + 1}. \end{array}\tag{47}
$$

(48)

Then, since also

$$
N _ {t + 1} = 2 ^ {t} - 1 = 2 \cdot (2 ^ {t - 1} - 1) + 1 = 2 N _ {t} + 1,
$$

we see from (41), (43), and (46)-(48) that $B_{t+1}$ has the form

$$
\begin{array}{r} \pmb {B} _ {t + 1} = \Big \{B _ {j _ {0} ^ {t + 1}, j _ {1} ^ {t + 1}}, B _ {j _ {1} ^ {t + 1}, j _ {2} ^ {t + 1}}, \ldots , B _ {j _ {N _ {t + 1}} ^ {t + 1}, n + 1}, \\ M _ {j _ {1} ^ {t + 1}, 2}, \ldots , M _ {j _ {N _ {t + 2}} ^ {t + 1}} \Big \}. \end{array}
$$

Thus, if $t + 1 < r$ , we may define $\alpha_{t+1}$ on $B_{t+1}$ by the formulas (34)-(37) (substituting $t + 1$ for $t$ ). It then follows from (32), (44), and (45) that $\alpha$ is a (3, 1)-balanced strategy. Q.E.D.

According to the above result, if $2^{r} \leq n + 1$ , then there exists a (3, 1)-balanced strategy for D,

$$
\alpha^ {*} = \left\langle \left(B _ {1} ^ {*}, \alpha_ {1} ^ {*}\right), \dots , \left(B _ {r} ^ {*}, \alpha_ {r} ^ {*}\right) \right\rangle .
$$

and, defining

$$
\boldsymbol {B} _ {r + 1} ^ {*} = R \left(\boldsymbol {B} _ {r} ^ {*}, \alpha_ {r} ^ {*}\right),
$$

it then follows from Proposition 5.3.2 that

$$
\# B _ {r + 1} ^ {*} = 2 ^ {r + 1} - 1.\tag{49}
$$

It will probably come as no surprise to the reader that no feasible strategy for D can result in a final information structure having a larger number of elements than $2^{r+1}-1$ ; however, this statement would nonetheless appear to require a formal proof. In order to provide said proof, we begin by establishing the following, which is a result we shall find useful in other contexts. For purposes of this and the next result, we shall say that a feasible information-gathering process is efficient\* if it satisfies (i) and (ii.a) of Definition 3.1.8.

6.2.9. Proposition. If $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ is non-trivial and efficient, $^*$ and we define $B_{r+1} = R(B_r, \alpha_r)$ , then

$$
\# \boldsymbol {B} _ {t + 1} = 2 \sum_ {s = 1} ^ {t} \# \boldsymbol {B} _ {s} ^ {2} + 1 \quad \text { for } \quad t = 1, \dots , r.
$$

Proof. We have for $t \in \{1, \ldots, r\}$

$$
\begin{array}{r l} \boldsymbol {B} _ {t + 1} & = \bigcup_ {\boldsymbol {B} \in \boldsymbol {B} _ {t}} \iota [ \boldsymbol {B}, \alpha_ {t} (\boldsymbol {B}) ] \\ & = \bigcup_ {\boldsymbol {B} \in \boldsymbol {B} _ {t} ^ {2}} \iota [ \boldsymbol {B}, \alpha_ {t} (\boldsymbol {B}) ] \\ & \cup \left[ \bigcup_ {s = 2} ^ {t} \bigcup_ {\boldsymbol {B} \in \boldsymbol {B} _ {s} ^ {1}} \iota [ \boldsymbol {B}, \alpha_ {t} (\boldsymbol {B}) ] \right]. \end{array}\tag{50}
$$

Therefore

$$
\begin{array}{r l} \# B _ {t + 1} = & \sum_ {B \in B _ {t} ^ {2}} \# t [ B, \alpha_ {t} (B) ] \\ & + \sum_ {s = 2} ^ {t} \sum_ {B \in B _ {s} ^ {1}} \# t [ B, \alpha_ {t} (B) ]. \end{array}\tag{51}
$$

However, since $\alpha$ is efficient, $^{*}$ we have

$$
\left(\forall B \in B _ {t} ^ {2}\right): \# \iota [ B, \alpha_ {t} (B) ] \geq 2,
$$

and it then follows from Theorem 5 that

$$
\left(\forall B \in \boldsymbol {B} _ {t} ^ {2}\right): \# t [ B, \alpha_ {t} (B) ] = 3.\tag{52}
$$

Furthermore, by definition of $B_{s}^{1}$ (and again using the fact that $\alpha$ is efficient), we have

$$
\left(\forall B \in \boldsymbol {B} _ {s} ^ {1}\right): \# t [ B, \alpha_ {t} (B) ] = 1 \quad \text { for } \quad s = 2, \dots , t.\tag{53}
$$

Substituting (52) and (53) into (51), we then obtain

$$
\# \boldsymbol {B} _ {t + 1} = 3 \left(\# \boldsymbol {B} _ {t} ^ {2}\right) + \sum_ {s = 2} ^ {t} \# \boldsymbol {B} _ {s} ^ {1}.\tag{54}
$$

Now, we also have

$$
\# \boldsymbol {B} _ {t + 1} = \# \boldsymbol {B} _ {t + 1} ^ {2} + \sum_ {s = 2} ^ {t + 1} \# \boldsymbol {B} _ {s} ^ {1},\tag{55}
$$

and equating (54) and (55), we have

$$
\# \boldsymbol {B} _ {t + 1} ^ {1} = 3 \left(\# \boldsymbol {B} _ {t} ^ {2}\right) - \# \boldsymbol {B} _ {t + 1} ^ {2} \quad \text { for } \quad t = 1, \dots , r\tag{56}
$$

(for $t = r$ , $\# B_{t+1}^2$ is, of course, equal to zero). Since (56) holds for $t = 1, \ldots, r$ , it follows that

$$
\# \boldsymbol {B} _ {s} ^ {1} = 3 \left(\# \boldsymbol {B} _ {s - 1} ^ {2}\right) - \# \boldsymbol {B} _ {s} ^ {2} \quad \text { for } \quad s = 2, \dots , r,
$$

and substituting into (54), we have

$$
\begin{array}{r l} \# B _ {t + 1} & = 3 \big (\# B _ {t} ^ {2} \big) + \sum_ {s = 2} ^ {t} \left[ 3 \big (\# B _ {s - 1} ^ {2} \big) - \# B _ {s} ^ {2} \right] \\ & = 3 \big (\# B _ {t} ^ {2} \big) = 3 \sum_ {s = 2} ^ {t} \# B _ {s - 1} ^ {2} - \sum_ {s = 2} ^ {t} \# B _ {s} ^ {2} \\ & = 2 \sum_ {s = 2} ^ {t} \# B _ {s} ^ {2} + 3 \big (\# B _ {1} ^ {2} \big) \\ & = 2 \sum_ {s = 1} ^ {t} \# B _ {s} ^ {2} + \big (\# B _ {1} ^ {2} \big). \end{array}
$$

However, since $\alpha$ is non-trivial, we have $\# B_1^2 = 1$ ,

and the above becomes

$$
\# \boldsymbol {B} _ {t + 1} = \left(2 \sum_ {s = 1} ^ {t} \# \boldsymbol {B} _ {s} ^ {2}\right) + 1 \quad \text { for } \quad t = 1, \dots , r.
$$

Q.E.D.

6.2.10. Corollary. If $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $D$ , and we define $B_{r+1} = R(B_r, \alpha_r)$ , we have

$$
\# B _ {r + 1} \leq 2 ^ {r + 1} - 1.\tag{57}
$$

Proof. If $\alpha$ is a feasible strategy, then it is easy to see that there exists an efficient\* strategy

$$
\alpha^ {*} = \left\langle \left(B _ {1} ^ {*}, \alpha_ {1} ^ {*}\right), \dots , \left(B _ {r} ^ {*}, \alpha_ {r} ^ {*}\right) \right\rangle
$$

which is such that, defining $B_{r+1}^{*}=R(B_{r}^{*},\alpha_{r}^{*})$ , we have

$\# B_{r+1}^{*}\geq \# B_{r+1}$

Thus it suffices to prove that (57) holds for the case where $\alpha$ is a non-trivial efficient\* information-gathering strategy.

From Theorem 6.2.5 it follows that for each non-null information-gathering action taken at the $t$ th step, we obtain at least one element of $\pmb{B}^A$ . Consequently

$$
\# B _ {t + 1} ^ {1} \geq \# B _ {t} ^ {2} \quad \text { for } \quad t = 1, \dots , r.\tag{58}
$$

However, by (56) of the preceding proof, we then obtain

$$
\begin{array}{r l} & {\# B _ {t} ^ {2} \leq 3 \big (\# B _ {t} ^ {2} \big) - \# B _ {t + 1} ^ {2}, \qquad \mathrm{or}} \\ & {\# B _ {t + 1} ^ {2} \leq 2 \big (\# B _ {t} ^ {2} \big) \quad \mathrm{for} \quad t = 1, \dots , r.} \end{array}
$$

Since

$$
\# B _ {1} ^ {2} = 1,\tag{59}
$$

it follows from (59) and a trivial induction argument that

$$
\# B _ {t} ^ {2} \leq 2 ^ {t - 1} \quad \text { for } \quad t = 1, \dots , r.\tag{60}
$$

Now, by Proposition 9, we have

$$
\# B _ {r + 1} = 2 \sum_ {s = 1} ^ {r} \# B _ {s} ^ {2} + 1,\tag{61}
$$

and substituting (60) into (61), we obtain

$$
\begin{array}{r l} \# B _ {r + 1} & \leq 2 \left(\sum_ {s = 1} ^ {r} 2 ^ {s - 1}\right) + 1 \\ & = 2 (2 ^ {r} - 1) + 1 = 2 ^ {r + 1} - 1. \end{array}
$$

Q.E.D.

## 6.3. A Dynamic Programming Solution for the Tri-nary Case

In this subsection we shall retain all the assumptions of the previous subsection [(1) and (2) of section 6.2], and assume, in addition, that

$$
r \geq n.\tag{1}
$$

Our object here is to develop a dynamic programming solution for this case and to establish that the strategy obtained is, indeed, optimal. We proceed as follows.

(1) For each $i \in \{0, 1, \ldots, n\}$ , we define $\Delta(B_{i,i+1})$ by

$$
\Delta \left(B _ {i, i + 1}\right) = \pi \left(B _ {i, i + 1}\right) \nu \left(B _ {i, i + 1}\right),\tag{2}
$$

and, for each $k \in \{1, \ldots, n\}$ , we define

$$
\Delta (M _ {k 2}) = \pi (M _ {k 2}) \nu (M _ {k 2}).\tag{3}
$$

(2) For each $i \in \{0, 1, \ldots, n - 1\}$ , we calculate the following:

$$
\begin{array}{r l} w (i + 1) & = \Delta \left(B _ {i, i + 1}\right) + \Delta \left(B _ {i + 1, i + 2}\right) + \Delta \left(M _ {i + 1, 2}\right) \\ & - \pi \left(B _ {i, i + 2}\right) c (i + 1), \quad \text { and } \end{array} \tag {4}
$$

$$
w (0) = \pi (B _ {i, i + 2}) v (B _ {i, i + 2}).\tag{5}
$$

We then define

$$
\Delta \left(B _ {i, i + 2}\right) = \max \left\{w (0), w (i + 1) \right\}, \quad \text { and }\tag{6}
$$

(7)

(3) For each $i \in \{0, 1, \ldots, n-2\}$ , we calculate

$$
\begin{array}{r l} w (j) & = \Delta (B _ {i j}) + \Delta (B _ {j, i + 3}) + \Delta (M _ {j 2}) \\ & - \pi (B _ {i, i + 3}) c (j) \quad \text { for } \quad j = i + 1, i + 2, \end{array}\tag{8}
$$

$$
w (0) = \pi (B _ {i, i + 3}) v (B _ {i, i + 3}),\tag{9}
$$

$$
\Delta \left(B _ {i, i + 3}\right) = \max \left\{w (0), w (i + 1), w (i + 2) \right\},\tag{10}
$$

and

$$
\begin{array}{r l} \hat {a} (i, i + 3) & = \min \left\{j \in \{0, i + 1, i + 2 \} \mid w (j) \right. \\ & = \Delta \left(B _ {i, i + 3}\right) \}. \end{array}\tag{11}
$$

(4) Having found $\Delta(B_{i,i+I-1}), i=0,1,\ldots,n+1-(I-1), I\geq 2$ , we compute for $i\in\{0,\ldots,n+1$

$$
\begin{array}{r l} & {- I \}} \\ & {w (j) = \Delta (B _ {i j}) + \Delta (B _ {j, i + I}) + \Delta (M _ {j 2})} \\ & {\qquad - \pi (B _ {i, i + I}) c (j)} \\ & {\text {for} \quad j = i + 1, \dots , i + I - 1} \end{array}\tag{12}
$$

(note that for $j \in \{i + 1, \ldots, i + I - 1\}$ , both $j - i \leq I - 1$ and $i + I - j \leq I - 1$ ),

$$
w (0) = \pi (B _ {i, i + 1}) \nu (B _ {i, i + 1}),\tag{13}
$$

$$
\begin{array}{l} \Delta (B _ {i, i + I}) \\ = \max \left\{w (j) \mid j \in \{0, i + 1, \dots , i + I - 1 \}, \right. \end{array}\tag{14}
$$

and

$$
\begin{array}{r l} \hat {a} (i, i + I) & = \min \left\{j \in \{0, i + 1, \dots , i + I - 1 \} \right. \\ & \quad | w (j) = \Delta (B _ {i, i + I}) \}. \end{array}\tag{15}
$$

(5) Proceeding as above, we eventually obtain $\Delta(B_{0,n+1}) = \Delta(X)$ and $\hat{a}(0, n+1)$ .

We then define the strategy $\sigma^{*} = \langle (B_{1}^{*},\alpha_{1}^{*}),\ldots ,$ $(B_r^*,\alpha_r^*),(B_{r + 1}^*,\delta^*)\rangle$ by

$$
\alpha_ {1} ^ {*} (X) = \hat {a} (0, n + 1) \equiv a ^ {*}.\tag{16}
$$

By Theorem 6.2.5 we then obtain one of two cases. (a) $\alpha_{1}^{*}(X) = 0$ and $B_{2}^{*} = M_{a*} = \{X\}$ ; in which case, we complete the definition of $\sigma^{*}$ by defining

$$
\alpha_ {t} ^ {*} (X) = 0 \quad \text { for } \quad t = 2, \dots , r, \quad \text { and   let }\tag{17}
$$

$$
d ^ {t} \in D ^ {*} (X).\tag{18}
$$

(b) $\alpha_{1}^{*}\in \{1,\dots ,n\}$ and

$$
\boldsymbol {B} _ {2} ^ {*} = \boldsymbol {M} _ {a ^ {*}} = \left\{B _ {0 a ^ {*}}, M _ {a ^ {*} 2}, B _ {a ^ {*}, n + 1} \right\}.
$$

Here we define $\alpha_2^*$ by

$$
\begin{array}{r l} \alpha_ {2} ^ {*} (B _ {0, a ^ {*}}) & = \hat {a} (0, a ^ {*}), \alpha_ {2} ^ {*} (M _ {a ^ {*} 2}) \\ & = 0, \alpha_ {2} ^ {*} (B _ {a ^ {*}, n + 1}) = \hat {a} (a ^ {*}, n + 1). \end{array}\tag{19}
$$

Having obtained $\alpha_{t-1}^{*}$ and $B_{t}^{*}$ , for $t \in \{3, \ldots, r\}$ , we have by Corollary 6.2.6 that each $B \in B_{t}^{*}$ is either of the form

$B = B_{ij}$ for some $i\in \{0,1,\dots ,n\}$

$$
j \in \{i + 1, \dots , n + 1 \},\tag{20}
$$

or is of the form

$$
B = M _ {k 2} \quad \text { for   some } \quad k \in \{1, \dots , n \}.\tag{21}
$$

We then define $\alpha_{t}^{*}$ on $B_{t}^{*}$ by

$$
\alpha_ {i} ^ {*} (B) = \left\{ \begin{array}{l l} \hat {a} (i, j) & \text { if   } B \text {   is   of   the   form   (20) } \\ & \text { with   } j > i + 1. \\ 0 & \text { otherwise. } \end{array} \right.\tag{22}
$$

Proceeding in this fashion we eventually obtain $B_{r+1}^{*}$ , and let $\delta^{*}(B)$ be an element of $D^{*}(B)$ , for each $B \in B_{r+1}^{*}$ . Q.E.D.

It will be an easy consequence of the following result that $\alpha^{*}$ , as defined in (17)-(22), above, is optimal for $D$ .

6.3.1. Theorem. If $\sigma = \langle (\pmb{B}_1, \alpha_1), \ldots, (\pmb{B}_r, \alpha_r), (\pmb{B}_{r+1}, \delta) \rangle$ is a feasible strategy for $\pmb{D}$ , $q \in \{1, \ldots, r + 1\}$ , and $i \in \{0, 1, \ldots, n\}$ and $j \in \{i + 1, \ldots, n + 1\}$ are such that $B_{ij} \in B_q$ , then

$$
\begin{array}{l} \sum_ {B \in B _ {r + 1} (B _ {i j})} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ - \sum_ {t = q} ^ {r} \sum_ {B ^ {\prime} \in B _ {t} (B _ {i j})} \pi (B ^ {\prime}) c [ \alpha_ {t} (B ^ {\prime}) ] \leq \Delta (B _ {i j}), \end{array}\tag{23}
$$

where for $q = r + 1$ , we define

$$
\sum_ {t = q} ^ {r} \sum_ {B ^ {\prime} \in B _ {t} (B _ {t, j})} \pi (B ^ {\prime}) c [ \alpha_ {t} (B ^ {\prime}) ] = 0.
$$

Proof. We distinguish two cases, based on the value of $q$ .

(a) $q = r + 1$ . Here the left-hand-side of inequality (23) becomes

$$
\sum_ {x \in B _ {i j}} \phi (x) \omega [ x, \delta (B) ],\tag{24}
$$

and, since (24) is less than or equal to

$$
\pi \left(B _ {i j}\right) \nu \left(B _ {i j}\right) \leq \Delta \left(B _ {i j}\right),
$$

The desired inequality follows at once.

(b) $q \in \{1, \ldots, r\}$ . Here we establish our result for arbitrary $i \in \{0, 1, \ldots, n\}$ by induction on $I = j - i$ , as follows.

(i) $I = 1$ (and $j = i + 1$ ). Here we have by Theorem 6.2.5 that

$$
\boldsymbol {B} _ {r + 1} \left(\boldsymbol {B} _ {i j}\right) = \left\{\boldsymbol {B} _ {i j} \right\},
$$

and hence the left-hand-side of (23) becomes

$$
\sum_ {x \in B _ {i j}} \phi (x) \omega [ x, \delta (B) ]
$$

$$
\begin{array}{l} - \sum_ {t = q} ^ {r} \sum_ {B ^ {\prime} \in B _ {t} (B _ {i j})} \pi (B ^ {\prime}) c [ \alpha_ {t} (B ^ {\prime}) ] \\ \leq \sum_ {x \in B _ {i j}} \phi (x) \omega [ x, \delta (B) ] \leq \pi (B _ {i j}) \nu (B _ {i j}) \\ = \Delta (B _ {i j}). \end{array}
$$

(ii) Suppose the desired inequality holds for $j = i + I$ , where $I \in \{1, \ldots, n - i\}$ . Then for $j = i + I + 1$ , we have three possible cases.

Case 1. $\alpha_{q}(B_{ij})\equiv k\in \{i + 1,\dots ,j - 1\}$ . Here it follows from Theorem 6.2.5 that we can write the left-hand-side of (23) as

$$
\begin{array}{l} \sum_ {B \in B _ {r + 1} (B _ {i k})} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ - \sum_ {t = q + 1} ^ {r} \sum_ {B ^ {\prime} \in B _ {t} (B _ {i k})} \pi (B ^ {\prime}) c [ \alpha_ {t} (B ^ {\prime}) ] \\ + \sum_ {B \in B _ {r + 1} (B _ {k j})} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ - \sum_ {t = q + 1} ^ {r} \sum_ {B ^ {\prime} \in B _ {t} (B _ {k j})} \pi (B ^ {\prime}) c [ \alpha_ {t} (B ^ {\prime}) ] \\ + \sum_ {B \in B _ {r + 1} (M _ {k 2})} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ - \sum_ {t = q + 1} ^ {r} \sum_ {B ^ {\prime} \in B _ {t} (M _ {k 2})} \pi (B ^ {\prime}) c [ \alpha_ {t} (B ^ {\prime}) ] \\ - \pi (B _ {i j}) c (k). \end{array}\tag{25}
$$

However, since $k \in \{i + 1, \ldots, j - 1\}$ , and $j = i + I$ , it follows that $k - i \leq I$ and $j - k \leq I$ . Consequently, it follows from our inductive hypothesis that (25) is less than or equal to

$$
\begin{array}{l} \Delta (B _ {i k}) + \Delta (B _ {k j}) + \Delta (M _ {k 2}) - \pi (B _ {i j}) c (k) \\ \leq \Delta (B _ {i j}). \end{array}\tag{26}
$$

Case 2. $\alpha_{q}(B_{ij})\equiv k\notin\{i+1,\ldots,j-1\}$ and $B_{r+1}(B_{ij})=\{B_{ij}\}$ .

Here it is immediate that the left-hand side of (23) is less than or equal to

$$
\begin{array}{l} \pi (B _ {i j}) \nu (B _ {i j}) \leq \Delta (B _ {i j}) \\ \text { Case   3. } \quad \alpha_ {q} (B _ {i j}) \equiv k \notin \{i + 1, \dots , j - 1 \} \text { and } \\ B _ {r + 1} (B _ {i j}) \notin \{B _ {i j} \}. \end{array}
$$

In this case, it follows at once from Theorem 6.2.5

$$
\begin{array}{l} \text { that   for   some } t \in \{q + 1, \dots , r \} \text { we   have } \\ \alpha_ {t} (B _ {i j}) = k ^ {\prime} \in \{i + 1, \dots , j - 1 \}, \quad \text { and } \\ \alpha_ {s} (B _ {i j}) \notin \{i + 1, \dots , j - 1 \} \\ \text { for } s = q, \dots , t - 1, \end{array}\tag{27}
$$

and thus

$$
\begin{array}{l} \sum_ {B \in B _ {r + 1} (B _ {i j})} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ - \sum_ {t = q} ^ {r} \sum_ {B ^ {\prime} \in B _ {t} (B _ {i j})} \pi (B ^ {\prime}) c [ \alpha_ {t} (B ^ {\prime}) ] \\ = \sum_ {B \in B _ {r + 1} (B _ {i j})} \sum_ {x \in B} \phi (x) \omega [ x, \delta (B) ] \\ - \sum_ {s = q} ^ {t - 1} \pi (B _ {i j}) c [ \alpha_ {s} (B _ {i j}) ] \\ - \sum_ {s = t} ^ {r} \sum_ {B ^ {\prime} \in B _ {s} (B _ {i j})} \pi (B ^ {\prime}) c [ \alpha_ {s} (B ^ {\prime}) ] \\ \leq \sum_ {B \in B _ {r + 1} (B _ {i j})} \sum_ {x \in B} \phi (x) \omega [ x, \delta (\tilde {B}) ] \\ - \sum_ {s = t} ^ {r} \sum_ {B ^ {\prime} \in B _ {s} (B _ {i j})} \pi (B ^ {\prime}) c [ \alpha_ {s} (B) ], \end{array}\tag{28}
$$

and it follows from our analysis of the preceding cases that the right-hand side of (28) is less than or equal to $\Delta(B_{ij})$ . Q.E.D.

6.3.2. Corollary. The strategy $\sigma^{*} = \langle (B_{1}^{*}, \alpha_{1}^{*}), \ldots, (B_{r}^{*}, \alpha_{r}^{*}), (B_{r+1}^{*}, \delta^{*}) \rangle$ , defined in (17)-(22), above, is optimal for $D$ .

Proof. It is an immediate consequence of our definition of $\sigma^{*}$ (in particular of our definition of $\alpha_{1}^{*}(X)$ and $\delta^{*}$ ) that

$$
\Omega (\sigma^ {*}) - \Gamma (\sigma^ {*}) = \Delta (B _ {0, n + 1}) = \Delta (X).
$$

Consequently, it follows from Theorem 1 that $\sigma^{*}$ is optimal for $D$ . Q.E.D.

## 6.4. The Linear Ordering in the Binary Case

This section parallels section 6.2; although here we suppose that D is a binary information problem. We also suppose, defining > on $A_{1}$ by

$$
a ^ {\prime} > a ^ {\prime} \Leftrightarrow M _ {a ^ {\prime} 1} \subset M _ {a 1},\tag{1}
$$

that $^{'} >$ is total on $A_{1}$ . Thus we can suppose,

without loss of generality that

$$
(\forall i, j \in A _ {1}): j > i \Leftrightarrow M _ {i 1} \subset M _ {j 1}.\tag{2}
$$

As in section 6.2, it will be convenient to adjoin to $A_{1}$ the two elements 0 and $n + 1$ , where

$$
M _ {0} = \left\{M _ {0 1}, M _ {0 2} \right\} \quad \text { with } \quad M _ {0 1} = \emptyset , M _ {0 3} = X,\tag{3}
$$

and

$$
\begin{array}{l l} M _ {n + 1} = \left\{M _ {n + 1, 1}, M _ {n + 1, 2} \right\} & \text { with } \\ M _ {n + 1, 1} = X, M _ {n + 1, 2} = \emptyset . \end{array}\tag{4}
$$

As in section 6.2 (Lemma 6.2.1), we can then show that; defining $\hat{A} = A_{1} \cup \{0, n + 1\}$ , we have

$$
\begin{array}{l} \left(\forall i, j \in \hat {A}\right): j > i \\ \Leftrightarrow \left[ M _ {i 1} \subset M _ {j 1} \quad \text { and } \quad M _ {j 2} \subset M _ {i 2} \right]. \end{array}\tag{5}
$$

With the assumptions and definition set forth in the previous two paragraphs, we can obtain results for the binary case which parallel all the key results for the trinary case. We list the main results here without proof. The proof in all cases is similar to that for the corresponding result in the trinary case, except that it can generally be simplified slightly by virtue of having only two possible outcomes instead of three. In our list to follow, we have skipped some digits in our numbering in order to maintain the convention that 6.4.m always corresponds to 6.2.m.

6.4.3. Theorem. If $B \subseteq X$ is $n$ -feasible, then there exists $i \in \{0, \ldots, n\}$ , $j \in \{i + 1, \ldots, n + 1\}$ such that

$$
B = M _ {j 1} \cap M _ {i 2}.
$$

6.4.4. Definition. For each $i \in \{0, \ldots, n\}$ and each $j \in \{i + 1, \ldots, n + 1\}$ , we define $B_{ij} \subseteq X$ by $B_{ij} = M_{j1} \cap M_{i2}$ .

6.4.5. Theorem. Suppose $i \in \{0, \ldots, n\}$ , $j \in \{i + 1, \ldots, n + 1\}$ , and $k \in \{0, 1, \ldots, n + 1\}$ . Then $\# \iota(B_{ij}, k) > 1$ if, and only if, $k \in \{i + 1, \ldots, j - 1\}$ , in which case we have

$$
\iota \left(B _ {i j}, k\right) = \left\{B _ {i k}, B _ {k j} \right\}.
$$

6.4.7. Corollary. The family $\pmb{B}^{\pmb{A}}$ contains $n + 1$ elements, and is given by

$$
\boldsymbol {B} ^ {A} = \left\{B _ {0 1}, B _ {1 2}, \dots , B _ {n, n + 1} \right\}.
$$

6.4.8. Theorem. If $r$ and $n$ satisfy $2^r \leq n + 1$ , then there exists a (2, 0)-balanced strategy for $D$ . Furthermore, if $\alpha = \langle (\pmb{B}_1, \alpha_1), \ldots, (\pmb{B}_r, \alpha_r) \rangle$ is a (2, 0)-balanced strategy for $D$ , and $B_{r+1} = R(\pmb{B}_r, \alpha_r)$ , then $\# B_{r+1} = 2^r$ .

6.4.9. Proposition. If $\alpha = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r) \rangle$ is a feasible information-gathering strategy for $D$ , and we define $B_{r+1} = R(B_r, \alpha_r)$ , then $\# B_{r+1} \leq 2^r$ .

We can also define a dynamic programming solution for the binary case in essentially the same fashion in which we proceeded in the trinary case (except that now we need only define $\Delta(B_{ij})$ for $i \in \{0, \ldots, n\}$ , $j \in \{i + 1, \ldots, n + 1\}$ ; and it can be shown, as before that the resulting strategy is optimal for D.

## 6.5. Applications to the Computer File Search Problem

As we noted earlier, all the maintained assumptions of section 6.2 and 6.3 are satisfied by our model of the computer file search problem (section 4.2); which we can demonstrate as follows. As developed in section 4.2, the information structures for the file search problem take the form

$$
\begin{array}{l} M _ {a} = \left\{M _ {a 1}, M _ {a 2}, M _ {a 3} \right\}, \quad \text { where } \\ M _ {a 1} = \left\{y _ {1}, \ldots , y _ {a - 1} \right\} \cup \left\{z _ {0}, \ldots , z _ {a - 1} \right\}, \\ M _ {a 2} = \left\{y _ {a} \right\}, \quad \text { and } \\ M _ {a 3} = \left\{y _ {a + 1}, \ldots , y _ {n} \right\} \cup \left\{z _ {a}, \ldots , z _ {n} \right\}, \\ \text { for   } a \in \{1, \ldots , n \}. \text { Therefore } \\ a > a ^ {\prime} \Leftrightarrow M _ {a ^ {\prime} 1} \cup M _ {a ^ {\prime} 2} \subset M _ {a 1}, \end{array}\tag{1}
$$

and we see that (1) [and (2)] of section 6.2 is satisfied in this case. The results of sections 6.2 and 6.3 then yield a number of implications for the file search problem; the principal application being the following.

(1) If $r$ and $n$ satisfy

$$
2 ^ {r} \leq n + 1,\tag{2}
$$

then there exists a (3, 1)-balanced strategy for $D$ , $\sigma^{*} = \langle \alpha^{*}, B_{r+1}^{*}, \delta^{*} \rangle$ . Furthermore,

$$
\# B _ {r + 1} ^ {*} = 2 ^ {r + 1} - 1,
$$

(Theorem 6.2.8).

(2) If, using the notation of section 6.2, we have $p_i = p > 0$ for $i = 1, \ldots, n$ ,

then the cost of the above strategy, $\sigma^{*}$ , is given by

$$
\Gamma (\sigma^ {*}) = [ r (1 + p) - p (2 ^ {r} - 1) ] c,\tag{3}
$$

(Corollary 5.3.4).

(3) The dynamic programming solution developed in section 6.3 can be utilized to solve any particular realization of the computer file search problem.

However, we can supplement these results a bit, and at the same time obtain some results applicable to a more general special case of the categorization problem. Consider the following.

6.5.1. Proposition. Suppose $\pmb{D}$ is a categorization problem satisfying

$$
\theta \overline {{{{\omega}}}} > \bar {c},\tag{4}
$$

where $\theta > 0$ and $\bar{c}$ are defined by

$$
\theta = \min \left\{\psi (B) \mid B \in \boldsymbol {B} ^ {A} \right\} \quad \text { and } \quad \bar {c} = \max _ {a \in A} c (a),
$$

respectively, Then if $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is a feasible strategy for $D$ such that for some $B^* \in B_{r+1}$ , some $q \in \{1, \ldots, r\}$ and some $\bar{a} \in A$ we have

$a(q, B^{*}) = 0$ and for some $B^{\tau} \in \iota(B^{*}, \bar{a})$ we have

$$
\boldsymbol {B} ^ {\tau} \cap X _ {\delta (\boldsymbol {B} ^ {*})} = \emptyset ,\tag{5}
$$

then $\sigma$ is strictly dominated.

Proof. We have

$$
\begin{array}{l} \sum_ {B \in \iota (B ^ {*}, \bar {a})} \pi (B) \nu (B) \\ = \overline {{\omega}} \left[ \sum_ {B \in \iota (B ^ {*}, \bar {a}) \setminus \{B ^ {\tau} \}} \psi (B) + \psi (B ^ {\tau}) \right] \\ \geq \overline {{\omega}} \left(\sum_ {B \in \iota (B ^ {*}, \bar {a}) \setminus \{B ^ {\tau} \}} \pi [ B \cap X _ {\delta (B ^ {*})} ]\right) \\ + \overline {{\omega}} \psi (B ^ {\tau}) \\ = \sum_ {x \in B ^ {*}} \phi (x) \omega [ x, \delta (B ^ {*}) ] + \overline {{\omega}} \psi (B ^ {\tau}), \end{array}\tag{6}
$$

where the last equality is by the fact that

$$
B ^ {\tau} \cap X _ {\delta (B ^ {*})} = \emptyset .
$$

Moreover, by (4), the definition of $\theta$ , and the fact that $\pi(B^{*}) \leq 1$ we have

$$
\overline {{{\omega}}} \psi (B ^ {\tau}) \geq \theta \overline {{{\omega}}} > \bar {c} \geq \pi (B ^ {*}) c (\bar {a}).\tag{7}
$$

From (6) and (7) we see that

$$
\begin{array}{l} \sum_ {B \in \iota (B ^ {*}, \bar {a})} \pi (B) \nu (B) - \sum_ {x \in B ^ {*}} \phi (x) \omega [ x, \delta (B ^ {*}) ] \\ > \pi (B ^ {*}) c (\bar {a}), \end{array}
$$

and it then follows from Proposition 3.2.3 that $\sigma$ is strictly dominated, Q.E.D.

6.5.2. Corollary. Suppose D is a categorization problem satisfying (4) of Proposition 1, and that, in addition D satisfies

for all n-feasible $B \subseteq X$ , if $B \notin B^A$ , then for each $d \in D^*(B)$ , there $\exists a^* \in A$ (possibly depending on $d$ ) and $B^* \in \iota(B, a^*)$ such that $B^* \cap X_d = \emptyset$ .

(8)

Their if $r \geq n$ , and $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is optimal for $D$ , we have $B_{r+1} = B^A$ .

Proof. Suppose $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta) \rangle$ is optimal for $D$ , let $B \in B_{r+1}$ be arbitrary and suppose, by way of obtaining a contradiction, that $B \notin B^A$ . Since $\sigma$ is optimal for $D$ , $\sigma$ must be efficient, and thus

$$
\delta (B) \in D ^ {*} (B),\tag{9}
$$

and, since $r \geq n$ , there must exist $q \in \{1, \ldots, r\}$ such that

$$
a (q, B) = 0.\tag{10}
$$

However, by (9) and hypothesis (8), there exists $\bar{a} \in A$ and $B^{*} \in \iota(B, \bar{a})$ such that

$$
B ^ {*} \cap X _ {\delta (B)} = \emptyset ,
$$

and it then follows from Proposition 1 that $\sigma$ is strictly dominated; contradicting the assumption that $\sigma$ is optimal for $D$ . Q.E.D.

While condition (8) of the preceding Corollary may look a bit odd, and possibly somewhat artificial, it is satisfied in the computer file search problem; as we shall demonstrate in the proof of the following.

6.5.3. Proposition. If D is a computer file search problem satisfying (in the notation of section 4.2),

$$
\overline {{{\omega}}} \min \left\{p _ {1}, \dots , p _ {n}, q _ {0}, \dots , q _ {n} \right\} > c,\tag{11}
$$

and $r \geq n$ , then if $\sigma = \langle (B_1, \alpha_1), \ldots, (B_r, \alpha_r), (B_{r+1}, \delta \rangle)$ is optimal for $D$ , we must have

$$
\boldsymbol {B} _ {r + 1} = \boldsymbol {B} ^ {A} = \boldsymbol {X},
$$

and thus $\Omega (\sigma) = \overline{\omega}$ .

Proof. The reader will readily see that in order to prove this result it suffices to establish the fact that the computer file search problem satisfies (8) of Corollary 2. To do this, we note that if $B \subseteq X$ is $n$ -feasible, and $B \notin B^A$ , then it follows from Theorem 6.2.3' and Corollary 6.2.7 that there exists $i \in \{0, \ldots, n-1\}$ and $j \in \{i+2, \ldots, n+1\}$ such that

$$
\boldsymbol {B} = \boldsymbol {B} _ {i j}.\tag{12}
$$

Furthermore, if $d^{*} \in D^{*}(B)$ , then either $d^{*} = 0$ , or $d^{*} \in \{i + 1, \ldots, j - 1\}$ . Letting $k = i + 1$ , we have from Theorem 6.2.5, we have that $\iota(B, k) = \{B_{ik}, M_{k2}, B_{kj}\}$ . We can thus distinguish two cases.

(a) $\mathbf{d}^{*} = i + 1$ . In this case

$$
B _ {i k} \cap X _ {d ^ {*}} = \emptyset \quad \left[ \text { and } B _ {k j} \cap X _ {d ^ {*}} = \emptyset \text { as   well } \right].
$$

(b) $d^{*}\in \{0,i + 2,\dots ,j - 1\}$ .Here we have $\dot{M}_{k2}\cap X_{d^{*}} = \emptyset$

Thus we see that D satisfies condition (8) of Corollary 2, and our conclusion is then an immediate implication of that result. Q.E.D.

It is an immediate implication of the above result that if in the computer file search problem one can reasonably assume that

$$
\overline {{{\omega}}} \min \left\{p _ {1}, \dots , p _ {n}, q _ {0}, \dots , q _ {n} \right\} > c,\tag{11'}
$$

and that $r \geq n$ , then one can proceed as follows to solve the problem. First find the collection of efficient strategies, call it $\Sigma^*$ , given by

$$
\Sigma^ {*} = \left\{\sigma = \langle (\alpha , B _ {r + 1}, \mathfrak {J}) \rangle \in \Sigma^ {e} | B _ {r + 1} = B ^ {A} \right\}.
$$

Secondly, find $\sigma^{*} \in \Sigma^{*}$ satisfying

$$
(\forall \sigma \in \Sigma^ {*}): \Gamma (\sigma) \geq \Gamma (\sigma^ {*}).\tag{13}
$$

if $\sigma^{*} \in \Sigma^{*}$ satisfies (13), then $\sigma^{*}$ will be optimal for $D$ . Of course the algorithm developed in section 6.3 will find a $\sigma^{*}$ satisfying (13); however, it is interesting to note that, while we have approached the problem from a very different point of view that which has been followed in the computer science literature, the simple (and fairly plausible) condition (11') and the assumption that $r \geq n$ together imply that the solution obtained here is perfectly consistent with the approach followed in computer science (cf. Aho, Hopcroft, and Ullman [1974, pp. 113–123]).

In connection with this latter point, however, we would have to note that it appears to us at this juncture that there may have been a bit too much emphasis in the computer science literature on the 'balanced tree' solution to the search problem. This may come about because of a certain ambiguity in that literature as to whether what is most important as a criterion for solution is to (a) minimize 'worst-case' time, or (b) minimize expected cost. The 'balanced tree' solution, which is equivalent to the (3, 1)-balanced strategy solution developed in the proof of Theorem 6.2.8, does minimize the worst-case time of obtaining a solution with certainty (in our terms $B_{r+1} = X$ ), as is shown by Theorem 6.2.8 and 6.2.9. However, that solution may not minimize the expected cost of obtaining such a solution. $^{24}$ At this point, we believe that the following is true: $^{25}$ if, in the notation used here and in section 4.2 we have

![](/api/attachments/2UBC4DHS/fulltext/images/0f7807d60dfed79a214081f5675a53b136be20be2d3f246d2d2a5f2d0dc9c334.jpg)  
Fig. 5.

![](/api/attachments/2UBC4DHS/fulltext/images/9e2c1c3ad42d7c78eba7311a31ca59043d3bc9f1a2d2193193ec30346c1556d0.jpg)  
Fig. 6.

$$
p _ {i} = p > 0 \quad \text { for } \quad i = 1, \dots , n, \quad \text { and }
$$

$$
q _ {i} = q > 0 \quad \text { for } \quad i = 0, 1, \dots , n,
$$

(and, of course, $nq + (n + 1)q = 1$ ) then the (3, 1)-balanced strategy of Theorem 6.2.8 satisfies (13), above; and thus is optimal for any value of $r \geq \log_2(n + 1)$ . On the other hand, with $n = 7$ , and

$$
p _ {i} = p \quad \text { for } \quad i = 1, \dots , 7, \quad \text { and }
$$

$$
q _ {i} = q > 0 \quad \text { for } \quad i = 1, \dots , 6,\tag{14}
$$

it can be shown on the basis of the algorithm of Section 6.3 [or on the basis of the algorithm on pp. 119–123 of Aho, Hopcroft, and Ullman, for that matter] that the following is true.

(1) If we also have $q_{0} \leq 2q + p$ and $q_{7} \leq 2q + p$ then the best (i.e., least) expected costs of strategies which begin with the various possible first steps are as in the table

<table><tr><td>If the first experiment is</td><td>least expected cost is</td></tr><tr><td>1</td><td> $(q_0 + 3q_7 + 24q + 21p)c$ </td></tr><tr><td>2</td><td> $(2q_0 + 3q_7 + 21q + 19p)c$ </td></tr><tr><td>3</td><td> $(2q_0 + 3q_7 + 20q + 18p)c$ </td></tr><tr><td>4</td><td> $(3q_0 + 3q_7 + 18q + 17p)c = (3 - 4p)c$ </td></tr><tr><td>5</td><td> $(3q_0 + 2q_7 + 20q + 18p)c$ </td></tr><tr><td>6</td><td> $(3q_0 + 2q_7 + 21q + 19p)c$ </td></tr><tr><td>7</td><td> $(3q_0 + q_7 + 24q + 21p)c$ </td></tr></table>

In this case it is easy to see that the best (least-) expected cost obtainable when one begins with experiment 4 (i.e., first compares b with $b_{4}$ ) is no higher than that obtainable with any other possible first step; and it can be shown that the (3, 1)- balanced strategy is optimal in this case. $^{26}$ However, it is interesting to note that if $q_{0}=2q+p$ , then the strategy which begins with experiment 3 has exactly the same expected cost as that which begins with experiment 4. Moreover, we can get somewhat strange-looking solutions in this general situation, as is shown by the following two cases.

(2) Suppose (14) holds and that

$$
2 q + p <   q _ {0} \leq 3 q + p \quad \text { and } \quad q <   q _ {7} \leq 2 q + p.
$$

Then it can be shown that the search strategy in fig. 5 is optimal (if $r \geq 4$ ).

(3) Suppose (14) holds and that

$$
4 q + 3 p <   q _ {7} \leq q _ {0}.
$$

Then it can be shown that the search strategy in fig. 6 is optimal, if $r \geq 5$ .

The reason that we consider cases 2 and 3 to be of some significance is that in general one would suppose that in many, if not most, realizations of a file search problem we would likely have

$$
\begin{array}{l l} q _ {0} > q _ {i} & \text { for } \quad i = 1, \ldots , 6 \quad \text { and } \\ q _ {7} > q _ {i} & \text { for } \quad i = 1, \ldots , 6, \end{array}
$$

(i.e., it is more likely that a randomly-drawn element from $U$ is outside the range of $\{b_{1},\ldots,b_{7}\}$ than that is a 'gap' between some $b_{i}$ and $b_{i+1}$ ). Where this is the case the unbalanced strategy of case 3 may well have a lower expected cost than the balanced strategy of case 1. To take a more specific example, suppose our data set consists of seven integers

$$
\begin{array}{l} b _ {1} = 1 1 4, b _ {2} = 1 2 6, b _ {3} = 1 3 8, b _ {4} = 1 5 0, b _ {5} = 1 6 2, \\ b _ {6} = 1 7 4, b _ {7} = 1 8 6. \end{array}
$$

In this case if we take the universal set, $U$ , to be given by

$$
U = \{1 0 1, \dots , 1 9 9 \},
$$

and take the probability distribution on U to be uniform; then, multiplying all probabilities by 99, for the sake of convenience, we will have

$$
\begin{array}{l} q _ {0} = q _ {7} = 1 3, q _ {2} = q _ {3} = \dots = q _ {6} = 1 1, \quad \text { and } \\ p _ {i} = p = 1 \quad \text { for } \quad i = 1, \ldots , 7. \end{array}
$$

Thus, if we denote the balanced strategy of case 1, above, by $\sigma^b$ and the strategy of case 3 by $\sigma^e$ , we have, respectively

$$
\begin{array}{l} \Gamma (\sigma^ {b}) = (2 9 7 - 4) c = 2 9 3 c, \quad \text { and } \\ \Gamma (\sigma^ {e}) = 3 7 1 c. \end{array}
$$

Thus in this case, the expected cost of the balanced strategy, $\sigma^{b}$ , is significantly lower than that of the extremes/balance strategy, $\sigma^{e}$ . However, suppose we change the example by taking

$$
U = \{1, \dots , 2 5 0 \},
$$

retaining our assumption of a uniform distribution on U. If we again normalize (this time multiply by 250) the values of p and $q_{1},\ldots,q_{6}$ remain as before. Thus the expected cost of $\sigma^{b}$ is given by

$$
\Gamma (\sigma^ {b}) = 7 4 6 c.
$$

$$
\begin{array}{l} \text { On   the   other   hand,   we   have } \\ q _ {0} = 1 1 3, q _ {7} = 6 4, \quad \text { and } \\ \Gamma (\sigma^ {e}) = 5 7 3 c. \end{array}
$$

The extreme-balance strategy $\sigma^{e}$ thus has a significantly lower expected cost than that for $\sigma^{b}$ with the second universal set. $^{27}$ The optimal expected cost solution for the computer file search problem appears, therefore, to be fairly sensitive to the specification of the universal set U. Whether this is a fact which should be of great concern to computer scientists is, however, a question upon which we shall not speculate further.

In closing this section, we believe that it is of interest to note that all of the general results obtained here hold if D is a general search problem, defined as follows.

6.5.4. Definition. We shall say that a decision problem, $\pmb{D}$ is a general search problem iff $\pmb{D}$ :

(1) is a categorization problem,

(2) satisfies the assumptions of section 6.2, so that we can write

$$
\boldsymbol {B} ^ {A} = \left\{M _ {1 2}, \dots , M _ {n 2}, B _ {0 1}, B _ {1 2}, \dots , B _ {n, n + 1} \right\},
$$

(3) satisfies the condition: for each $d \in \{0, 1, \ldots, p\}$ , and each $i \in \{1, \ldots, n\}$ ,

$$
M _ {i - 1, i} \cap X _ {d} \neq \emptyset \rightarrow M _ {i 2} \cap X _ {d} = \emptyset ,
$$

(4) has constant information cost, $c > 0$ .

## Reference

Aho, A.V., J.E. Hopcroft, and J.D. Ullman, The Design and Analysis of Computer Algorithms, Addison-Wesley, Reading, MA (1974).

$^{27}$ The condition of Case 3 is satisfied in this case, and thus $\sigma^{e}$ is the optimal solution for this example.
