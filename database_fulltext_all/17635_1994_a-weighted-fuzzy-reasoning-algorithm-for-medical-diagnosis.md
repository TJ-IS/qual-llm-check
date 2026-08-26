---
otero_id: 17635
otero_key: "UNM4WZMJ"
title: "A weighted fuzzy reasoning algorithm for medical diagnosis"
authors: "Shyi-Ming Chen"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90063-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A weighted fuzzy reasoning algorithm for medical diagnosis \*

Shyi-Ming Chen

National Chiao Tung University, Hsinchu, Taiwan, ROC

This paper presents a weighted fuzzy reasoning algorithm for handling medical diagnostic problems, where fuzzy set theory and fuzzy production rules are used for knowledge representation. The algorithm can perform fuzzy matching between the patient's symptom manifestations and the antecedent portions of fuzzy production rules to determine the presence of diseases, where the result is interpreted as a certainty level indicating the degree of certainty of the presence of the disease. Because the algorithm allows each symptom in medical diagnosis to have a different degree of importance, it is more flexible than the ones we presented in [3] and [4]. The algorithm can be executed very efficiently. If the knowledge base contains $n$ fuzzy production rules and there are $p$ symptoms, then the time complexity of the algorithm is $O(np)$ .

Keywords: Fuzzy production rules; Fuzzy set theory; Knowledge base; Knowledge representation; Similarity function; Similarity measures.

![](/api/attachments/UNM4WZMJ/fulltext/images/a86b4015108162c3ef7fcb3562b72bcc1a2ffdade50f653202d29f3f51a0886f.jpg)

Shyi-Ming Chen was born in Taipei, Taiwan, Republic of China, on January 16, 1960. He received the B.S. degree in electronic engineering from National Taiwan Institute of Technology, Taipei, Taiwan, in 1982, and the M.S. and Ph.D. degrees in electrical engineering from National Taiwan University, Taipei, Taiwan, in 1986 and 1991, respectively. From October 1982 to August 1984, he served in the Chinese Navy as an Electronics Officer. Since August 1987, he has been on the faculty of the Department of Electronic Engineering, Fu-Jen University, Taipei, Taiwan. He is currently an Associate Professor in the Department of Computer and Information Science, National Chiao Tung University, Hsinchu, Taiwan. His research interests include knowledge-based systems, database systems, artificial intelligence, and fuzzy systems. Dr. Chen is a member of the IEEE Computer Society and the Phi Tau Phi Scholastic Honor Society.

Correspondence to: Dr. Shyi-Ming Chen, Department of Computer and Information Science, National Chiao Tung University, Hsinchu, Taiwan, R.O.C.

This work was supported by the National Science Council, Republic of China, under Grant NSC 81-0408-E-009-520.

## 1. Introduction

It is obvious that many physicians' knowledge in medical diagnosis and many patients' symptom manifestations involve fuzzy concepts [8]. It is often the case that while medical diagnostic problems can be handled easily by physicians, they are often too difficult to be handled by computers. Therefore, there is an increasing demand to design a medical diagnostic system to handle medical diagnostic problems. In recent years, the application of fuzzy set theory [14] in medical diagnosis has been investigate [1], [3], [4], [9], [11], [12].

The theory of fuzzy sets was proposed by Zadeh [14] in 1965. Let U be the universe of discourse, $U = \{u_{1}, u_{2}, \ldots, u_{p}\}$ . A fuzzy set A of U is a set of ordered pairs $\{(u_{i}, f_{A}(u_{i})) | u_{i} \in U\}$ , where $f_{A}$ is the membership function, $f_{A}: U \to [0, 1]$ , and $f_{A}(u_{i})$ is the grade of membership of $u_{i}$ in A. Let A and B be two fuzzy sets in the universe of discourse U, i.e.,

$$
\begin{array}{l} {U = \left\{u _ {1}, u _ {2}, \ldots , u _ {p} \right\},} \\ {A = \left\{\left(u _ {i}, f _ {A} (u _ {i})\right) | u _ {i} \in U \right\},} \\ {B = \left\{\left(u _ {i}, f _ {B} (u _ {i})\right) | u _ {i} \in U \right\},} \end{array}
$$

where $f_{A}$ and $f_{B}$ are the membership functions of the fuzzy sets A and B, respectively. Then, the intersection operation between the fuzzy sets A and B is defined by:

$$
\begin{array}{r l} A \cap B & = \bigl \{\bigl (u _ {i}, f _ {A \cap B} (u _ {i}) \bigr) | f _ {A \cap B} (u _ {i}) \\ & = \operatorname{Min} \bigl (f _ {A} (u _ {i}), f _ {B} (u _ {i}) \bigr), u _ {i} \in U \bigr \}. \end{array}
$$

In [1], Adlassnig defined inexact medical entities as fuzzy sets and used fuzzy logic [13] to perform approximate reasoning [10, p.30] for medical diagnosis. In [9], Leung et al. developed a novel expert system shell SYSTEM Z-II based on fuzzy sets, fuzzy logic, and fuzzy numbers [8]. In [11] and [12], Sanchez presented a treatment of linguistic entities in medicine based on fuzzy

Table 1

sets, allowing the assignment of graded diagnosis to patients. In [3] and [4], we have presented the techniques for handling medical diagnostic problems based on fuzzy set theory. However, the techniques presented in [3] and [4] assume that all symptoms in medical diagnosis are of equal importance (i.e., each symptom in medical diagnosis has the same weight). If we can allow each symptom in medical diagnosis to have a different degree of importance, then there is room for more flexibility.

In this paper, we propose a weighted fuzzy reasoning algorithm to handle medical diagnostic problems, where fuzzy set theory and fuzzy production rules $[3]$ , $[4]$ , $[5]$ , $[10]$ are used for knowledge representation. The algorithm allows each symptom in medical diagnosis to have a different degree of importance. It can perform fuzzy matching between the patient's symptom manifestations and the antecedent portions of fuzzy production rules, where the result is interpreted as a certainty level indicating the degree of certainty of the presence of the disease. The algorithm is more flexible than the ones we presented in $[3]$ and $[4]$ due to the fact that it allows each symptom in medical diagnosis to have a different degree of importance.

This paper is organized as follows. In section 2, the concepts of fuzzy production rules are introduced. In section 3, the definition of the similarity function F is presented to measure the degree of similarity between fuzzy sets. In section 4, a weighted fuzzy reasoning technique is presented. In section 5, we present a weighted fuzzy reasoning algorithm for handling medical diagnostic problems. The conclusions are given in section 6.

## 2. Knowledge representation

It is obvious that much knowledge in the real-world is fuzzy rather than precise. The fuzziness [8] occurs when the boundary of a piece of information is not clear cut. For example, the following is a piece of fuzzy knowledge: “If you have a strong headache, then you might have caught a cold” where “strong” is a fuzzy concept because the meaning of the term “strong” is not clear cut and is also context dependent.

Fuzzy quantifiers and their corresponding numerical intervals.

<table><tr><td>Fuzzy quantifiers</td><td>Numerical intervals</td></tr><tr><td>always</td><td>[1.00, 1.00]</td></tr><tr><td>very strong</td><td>[0.95, 0.99]</td></tr><tr><td>strong</td><td>[0.80, 0.94]</td></tr><tr><td>more or less strong</td><td>[0.65, 0.79]</td></tr><tr><td>medium</td><td>[0.45, 0.64]</td></tr><tr><td>more or less weak</td><td>[0.30, 0.44]</td></tr><tr><td>weak</td><td>[0.10, 0.29]</td></tr><tr><td>very weak</td><td>[0.01, 0.09]</td></tr><tr><td>no</td><td>[0.00, 0.00]</td></tr></table>

In order to make the real-world knowledge suitable for being processed by computers, fuzzy production rules have been used for knowledge representation. The fuzzy production rule allows the rule to contain some fuzzy quantifiers [3] (i.e., strong, weak, very strong, more or less weak, etc.).

Let $R$ be a set of fuzzy production rules,

$$
R = \left\{R _ {1}, R _ {2}, \dots , R _ {n} \right\}.
$$

The general formulation of the rule $R_{i}, 1 \leqslant i \leqslant n$ , is as follows:

$$
R _ {i} \colon \text { IF } D _ {i} \text { THEN } d _ {i} (C F = \mu_ {i}), \quad \text { where }
$$

(1) $D_{i}$ represents the antecedent portion of $R_{i}$ which may contain some fuzzy quantifiers. The definitions of the fuzzy quantifiers and their corresponding numerical intervals are given in Table 1 [3].

(2) $d_{i}$ represents the consequence portion of $R_{i}$

(3) $\mu_{i}$ is the certainty factor which indicates the certainty that $R_{i}$ is believed in. The certainty levels which we used and their corresponding numerical intervals are given in Table 2.

Table 2  
Certainty levels and their corresponding numerical intervals.

<table><tr><td>Certainty levels</td><td>Numerical intervals</td></tr><tr><td>absolutely certain</td><td>[1.00, 1.00]</td></tr><tr><td>extremely certain</td><td>[0.96, 0.99]</td></tr><tr><td>very certain</td><td>[0.86, 0.95]</td></tr><tr><td>pretty certain</td><td>[0.76, 0.85]</td></tr><tr><td>quite certain</td><td>[0.66, 0.75]</td></tr><tr><td>fairly certain</td><td>[0.56, 0.65]</td></tr><tr><td>more or less certain</td><td>[0.46, 0.55]</td></tr><tr><td>little certain</td><td>[0.30, 0.45]</td></tr><tr><td>very little certain</td><td>[0.16, 0.29]</td></tr><tr><td>hardly certain</td><td>[0.01, 0.15]</td></tr><tr><td>absolutely uncertain</td><td>[0.00, 0.00]</td></tr></table>

In medical diagnostic problems, a physician's knowledge can be represented as

IF symptoms THEN concluded disease (CF = $\mu_{i}$ ). For example, let U be a set of symptoms, $U = \{vomiting, fever, knee pain, right lower abdominal pain, leukocyte increased\}$ , and appendicitis be a concluded disease, then a physician's knowledge may be represented by the rule $R_{1}$ as follows:

$R_{1}$ : IF {always vomiting $\wedge$ always fever $\wedge$ no knee pain $\wedge$ always right lower abdominal pain $\wedge$ always leukocyte increased}

THEN appendicitis (CF = very certain)
According to Table 1 and Table 2, the rule $R_{1}$ may subjectively be expressed as follows:

$R_{1}$ : IF $\{(\text{vomiting, 1.00}), (\text{fever, 1.00}), (\text{knee pain, 0.00}), (\text{right lower abdominal pain, 1.00}), (\text{leukocyte increased, 1.00})\}$

THEN appendicitis (CF = 0.90)

where $D_{1}=\{(vomiting,1.00),(fever,1.00),(knee pain,0.00),(right lower abdominal pain,1.00),(leukocyte increased,1.00)\}$ . It is obvious that $D_{1}$ is a fuzzy set of the universe of discourse U, where U={vomiting, fever, knee pain, right lower abdominal pain, leukocyte increased}.

## 3. Similarity measures

In this section, the similarity function F is introduced to measure the degree of similarity between fuzzy sets.

Let x and y be two real values between zero and one. The degree of similarity between x and y can be measured by the function T [6],

$$
T (x, y) = 1 - | x - y |,\tag{1}
$$

where $T(x, y) \in [0, 1]$ . The larger the values of $T(x, y)$ , the higher the similarity between x and y. For example, if x = 0.9 and y = 0.7, then $T(x, y) = 0.8$ . It indicates that the degrees of similarity between the real numbers 0.9 and 0.7 is 0.8. It is obvious that if x = y, then $T(x, y) = 1$ .

Let $U$ be the universe of discourse and let $A$ and $B$ be two fuzzy sets of $U$ , i.e.,

$$
\begin{array}{l} U = \left\{u _ {1}, u _ {2}, \ldots , u _ {p} \right\}, \\ A = \left\{\left(u _ {1}, a _ {1}\right), \left(u _ {2}, a _ {2}\right), \ldots , \left(u _ {p}, a _ {p}\right) \right\}, \\ B = \left\{\left(u _ {1}, b _ {1}\right), \left(u _ {2}, b _ {2}\right), \ldots , \left(u _ {p}, b _ {p}\right) \right\}. \end{array}
$$

where $a_{i} \in [0, 1]$ , $b_{i} \in [0, 1]$ , and $1 \leqslant i \leqslant p$ . By using the vector representation method [3], A and B can be represented by the vectors $\overline{A}$ and $\overline{B}$ , respectively, where

$$
\overline {{{A}}} = \langle a _ {1}, a _ {2}, \dots , a _ {p} \rangle ,
$$

$$
\overline {{{B}}} = \langle b _ {1}, b _ {2}, \dots , b _ {p} \rangle .
$$

Assume that each $u_{i}$ in U has a different degree of importance and the importance of $u_{i}$ is $w_{i}$ , where $w_{i} \in [0, 1]$ and $1 \leqslant i \leqslant p$ , then the degree of importance of each $u_{i}$ in U can be described by a weighted vector $\overline{W}$ , where

$$
\overline {{{W}}} = \left\langle w _ {1}, w _ {2}, \dots , w _ {p} \right\rangle .
$$

In this case, the degree of similarity between the fuzzy sets A and B can be measured by the similarity function $F, F(\overline{A}, \overline{B}, \overline{W}) \in [0, 1]$ , where

$$
F (\overline {{A}}, \overline {{B}}, \overline {{W}}) = \sum_ {j = 1} ^ {p} \left[ T (a _ {j}, b _ {j}) * \frac {W _ {j}}{\sum_ {k = 1} ^ {p} W _ {k}} \right].\tag{2}
$$

The larger the value of $F(\overline{A}, \overline{B}, \overline{W})$ , the higher the similarity between the fuzzy sets A and B.

Example 3-1: Let A and B be two fuzzy sets of the universe of discourse U, where

$$
\begin{array}{l} U = \left\{u _ {1}, u _ {2}, u _ {3}, u _ {4} \right\}, \\ A = \left\{\left(u _ {1}, 0. 9\right), \left(u _ {2}, 0. 5\right), \left(u _ {3}, 0. 1\right), \left(u _ {4}, 0. 2\right) \right\}, \\ B = \left\{\left(u _ {1}, 0. 3\right), \left(u _ {2}, 0. 8\right), \left(u _ {3}, 0. 6\right), \left(u _ {4}, 0. 2\right) \right\}. \end{array}
$$

Then, by using the vector representation method, the fuzzy sets A and B can be represented by the vectors $\overline{A}$ and $\overline{B}$ , respectively, where

$$
\overline {{{A}}} = \langle 0. 9, 0. 5, 0. 1, 0, 2 \rangle ,
$$

$$
\overline {{{B}}} = \langle 0. 3, 0. 8, 0. 6, 0. 2 \rangle .
$$

Assume that the weighted vector $\overline{W}$ is as follows: $\overline{W} = \langle 0.5, 1.0, 0.8, 1.0 \rangle$ , then

$$
\begin{array}{r l} F (\overline {{A}}, \overline {{B}}, \overline {{W}}) & = (1 - | 0. 9 - 0. 3 |) * \frac {0 . 5}{3 . 3} \\ & + (1 - | 0. 5 - 0. 8 |) * \frac {1 . 0}{3 . 3} \\ & + (1 - | 0. 1 - 0. 6 |) * \frac {0 . 8}{3 . 3} \\ & + (1 - | 0. 2 - 0. 2 |) * \frac {1 . 0}{3 . 3} \simeq 0. 6 9 6 9. \end{array}
$$

It indicates that the degree of similarity between the fuzzy sets A and B is about 0.6969.

## 4. A weighted fuzzy reasoning technique

In this section, we present a weighted fuzzy reasoning technique based on the similarity function F.

Let $U$ be a set of symptoms and $V$ be a set of diseases, where

$$
\begin{array}{l} U = \left\{m _ {1}, m _ {2}, \ldots , m _ {p} \right\}, \\ V = \left\{d _ {1}, d _ {2}, \ldots , d _ {n} \right\}. \end{array}
$$

Assume that the knowledge base contains the following fuzzy production rule:

$$
R _ {i} \colon \text { IF } D _ {i} \text { THEN } d _ {i} (C F = \mu_ {i}),
$$

where $D_{i} = \{(m_{j}, t_{ij}) | t_{ij} \in [0, 1], 1 \leqslant j \leqslant p\}$ , $\mu_{i} \in [0, 1]$ , and $1 \leqslant i \leqslant n$ , and assume that the patient has a set $M$ of symptom manifestations, where $M = \{(m_{j}, x_{j}) | x_{j} \in [0, 1], 1 \leqslant j \leqslant p\}$ . It is obvious that $D_{i}$ and $M$ are fuzzy sets of $U$ , where $U = \{m_{1}, m_{2}, \ldots, m_{p}\}$ . By using the vector representation method, $D_{i}$ and $M$ can be represented by the vectors $\overline{D}_{i}$ and $\overline{M}$ , respectively, where

$$
\begin{array}{r l} & {\overline {{D}} _ {i} = \langle t _ {i 1}, t _ {i 2}, \ldots , t _ {i p} \rangle ,} \\ & {\overline {{M}} = \langle x _ {1}, x _ {2}, \ldots , x _ {p} \rangle .} \end{array}
$$

Let $\overline{W}_i$ be the weighted vector of the symptoms appearing in $D_i$ , where $\overline{W}_i = \langle w_{i1}, w_{i2}, \ldots, w_{ip} \rangle$ . By applying (2), we can get

$$
F \left(\overline {{M}}, \overline {{D}} _ {i}, \overline {{W}} _ {i}\right) = \sum_ {j = 1} ^ {p} \left[ T \left(x _ {j}, t _ {i j}\right) * \frac {W _ {i j}}{\sum_ {k = 1} ^ {p} W _ {i k}} \right],\tag{3}
$$

where $F(\overline{M}, \overline{D}_{i}, \overline{W}_{i}) \in [0, 1]$ . The larger the value of $F(\overline{M}, \overline{D}_{i}, \overline{W}_{i})$ , the higher the similarity between M and $D_{i}$ .

Let $\lambda$ be a threshold value. If $F(\overline{M},\overline{D}_i,\overline{W}_i)\geqslant$ $\lambda$ , then the rule $R_{i}$ can be fired; it indicates that the patient might have the disease $d_{i}$ with the degree of certainty of about $c_{i}$ , where $c_{i} = F(\overline{M},\overline{D}_{i},\overline{W}_{i})*\mu_{i}$ and $c_{i}\in [0,1]$ . The larger the value $c_{i}$ , the higher the possibility that the patient might have the disease $d_{i}$ . If $F(\overline{M},\overline{D}_{i},\overline{W}_{i}) < \lambda$ , then the rule $R_{i}$ can not be fired.

## 5. A weighted fuzzy reasoning algorithm

In this section, we present a weighted fuzzy reasoning algorithm for handling medical diagnostic problems. Let $\lambda$ be a threshold value, U be a set of symptoms, and V be a set of diseases, where $U = \{m_{1}, m_{2}, \ldots, m_{p}\}$ and $V = \{d_{1}, d_{2}, \ldots, d_{n}\}$ . Assume that the knowledge base contains the following fuzzy production rules:

$$
R _ {i} \colon \text { IF } D _ {i} \text { THEN } d _ {i} (C F = \mu_ {i}),
$$

where $D_{i} = \{(m_{1}, t_{i1}), (m_{2}, t_{i2}), \ldots, (m_{p}, t_{ip})\}$ , $\mu_{i} \in [0, 1]$ , and $1 \leqslant i \leqslant n$ , then, based on the vector representation method, $D_{i}$ can be represented by the vector $\overline{D}_{i}$ , where

$$
\overline {{{D}}} _ {i} = \left\langle t _ {i 1}, t _ {i 2}, \dots , t _ {i p} \right\rangle \text {   and   } 1 \leqslant i \leqslant n.
$$

Assume that the degree of importance of each symptom $m_{j}$ in $D_{i}$ is $w_{ij}$ , where $1 \leqslant j \leqslant p$ , and assume that the degrees of importance of all symptoms in $D_{i}$ can be described by a weighted vector $\overline{W}_{i}$ , where

$$
\overline {{{W}}} _ {i} = \left\langle w _ {i 1}, w _ {i 2}, \dots , w _ {i p} \right\rangle .
$$

Assume that the patient has a set M of symptom manifestations,

$$
M = \left\{\left(m _ {j}, x _ {j}\right) \mid x _ {j} \in [ 0, 1 ], 1 \leqslant j \leqslant p \right\},
$$

then M can also be represented by the vector $\overline{M}$ , where $\overline{M} = \langle x_{1}, x_{2}, \ldots, x_{p} \rangle$ . The algorithm is now presented as follows:

## Weighted fuzzy reasoning algorithm for $i \gets 1$ to $n$ do

begin let the fuzzy set $Q$ be the result of the intersection between the fuzzy sets $M$ and $D_{i}$ , i.e.,

$$
\begin{array}{r l} Q & = M \cap D _ {i} \\ & = \left\{(m _ {j}, s _ {j}) \mid (m _ {j}, x _ {j}) \in M, (m _ {j}, t _ {i j}) \in D _ {i}, \right. \\ & \quad \left. s _ {j} = \operatorname{Min} (x _ {j}, t _ {i j}) \text {and} 1 \leqslant j \leqslant p \right\}. \end{array}
$$

let T be a set of symptoms which have nonzero membership value in the fuzzy set T, i.e.,

$$
\begin{array}{r l} T = \left\{m _ {j} \mid (m _ {j}, s _ {j}) \in Q, 0 <   s _ {j} \leqslant 1 \right. \\ & \text { and } 1 \leqslant j \leqslant p \Big \}. \end{array}
$$

$$
\begin{array}{c} \text {if T\neq\not\in then} \\ 2 y _ {i} \leftarrow F (\overline {{M}},   \overline {{D}} _ {i},   \overline {{W}} _ {i}); \\ \text {begin y_{i} \geqslant\lambda then} \\ \text {begin} \\ c _ {i} \leftarrow y _ {i} * \mu_ {i}; \end{array}
$$

(\* the patient might have the disease $d_{i}$ with the degree of certainty of about $c_{i} \ast$ )
if there exists a tuple $(P, [a, b])$ in Table 2 which is shown as follows:

<table><tr><td>Certainty levels</td><td>Numerical intervals</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td> $P$ </td><td> $[a, b]$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td></tr></table>

where $c_{i} \in [a, b]$ and $0 < a \leqslant b \leqslant 1$ , then the corresponding certainty level of $c_{i}$ is P
end
end.
end.

In the following, we use an example to illustrate the medical diagnostic process, where the result of any arithmetic operation is represented by 2 digits of significant numbers.

Example 5-1: Let U be a set of symptoms, V be a set of concluded diseases, and M be a set of the patient's symptom manifestations, where

$$
\begin{array}{l} U = \left\{m _ {1}, m _ {2}, m _ {3}, m _ {4}, m _ {5}, m _ {6} ^ {-} \right\}, \\ V = \left\{d _ {1}, d _ {2}, d _ {3}, d _ {4}, d _ {5} \right\}, \\ M = \left\{(m _ {1}, 0. 8 0), (m _ {2}, 0. 0 0), (m _ {3}, 0. 5 0), \right. \\ \left. (m _ {4}, 0. 0 0), (m _ {5}, 0. 2 0), (m _ {6}, 0. 0 0) \right\}. \end{array}
$$

Assume that the threshold value $\lambda$ is 0.20 (i.e., $\lambda = 0.20$ ), and the knowledge base of a medical diagnostic system contains the following fuzzy production rules:

$$
\begin{array}{r l} & R _ {1} \colon \mathrm{IF} \bigl \{(m _ {1}, 0. 9 0), (m _ {2}, 0. 0 0), (m _ {3}, 0. 0 0), \\ & \qquad (m _ {4}, 0. 0 0), (m _ {5}, 0. 3 0), (m _ {6}, 0. 0 0) \bigr \} \\ & \text {THEN} d _ {1} (C F = 0. 9 8) \\ & R _ {2} \colon \mathrm{IF} \bigl \{(m _ {1}, 0. 0 0), (m _ {2}, 0. 9 5), (m _ {3}, 0. 0 0), \\ & \qquad (m _ {4}, 0. 5 0), (m _ {5}, 0. 0 0), (m _ {6}, 0. 1 0) \bigr \} \\ & \text {THEN} d _ {2} (C F = 0. 9 0) \end{array}
$$

$$
R _ {3}: \operatorname{IF} \left\{\left(m _ {1}, 0. 0 0\right), \left(m _ {2}, 0. 0 0\right), \left(m _ {3}, 0. 9 0\right), \right.
$$

$$
\left. \left(m _ {4}, 0. 0 0\right), \left(m _ {5}, 0. 3 0\right), \left(m _ {6}, 0. 0 0\right) \right\}
$$

$$
\text { THEN } d _ {3} (C F = 0. 9 2)
$$

$$
R _ {4}: \mathrm{IF} \left\{\left(m _ {1}, 0. 0 0\right), \left(m _ {2}, 0. 0 0\right), \left(m _ {3}, 0. 0 0\right) \right.
$$

$$
\left. \left(m _ {4}, 0. 9 0\right), \left(m _ {5}, 0. 0 0\right), \left(m _ {6}, 0. 6 0\right) \right\}
$$

$$
\text { THEN } d _ {4} (C F = 0. 9 5)
$$

$$
R _ {5}: \operatorname{IF} \left\{\left(m _ {1}, 0. 0 0\right), \left(m _ {2}, 0. 0 0\right), \left(m _ {3}, 0. 0 0\right) \right.
$$

$$
\left. \left(m _ {4}, 0. 0 0\right), \left(m _ {5}, 0. 9 0\right), \left(m _ {6}, 0. 4 0\right) \right\}
$$

$$
\text { THEN } d _ {5} (C F = 0. 9 6). \text { Then }
$$

$$
\mu_ {1} = 0. 9 8, \mu_ {2} = 0. 9 0, \mu_ {3} = 0. 9 2, \mu_ {4} = 0. 9 5,
$$

$$
\mu_ {5} = 0. 9 6,
$$

$$
D _ {1} = \left\{\left(m _ {1}, 0. 9 0\right), \left(m _ {2}, 0. 0 0\right), \left(m _ {3}, 0. 0 0\right) \right.
$$

$$
(m _ {4}, 0. 0 0), (m _ {5}, 0. 3 0), (m _ {6}, 0. 0 0) \}.
$$

$$
D _ {2} = \left\{\left(m _ {1}, 0. 0 0\right), \left(m _ {2}, 0. 9 5\right), \left(m _ {3}, 0. 0 0\right), \right.
$$

$$
(m _ {4}, 0. 5 0), (m _ {5}, 0. 0 0), (m _ {6}, 0. 1 0) \},
$$

$$
D _ {3} = \left\{\left(m _ {1}, 0. 0 0\right), \left(m _ {2}, 0. 0 0\right), \left(m _ {3}, 0. 9 0\right), \right.
$$

$$
(m _ {4}, 0. 0 0), (m _ {5}, 0. 3 0), (m _ {6}, 0. 0 0) \},
$$

$$
D _ {4} = \left\{\left(m _ {1}, 0. 0 0\right), \left(m _ {2}, 0. 0 0\right), \left(m _ {3}, 0. 0 0\right), \right.
$$

$$
(m _ {4}, 0. 9 0), (m _ {5}, 0. 0 0), (m _ {6}, 0. 6 0) \}
$$

$$
D _ {5} = \left\{\left(m _ {1}, 0. 0 0\right), \left(m _ {2}, 0. 0 0\right), \left(m _ {3}, 0. 0 0\right), \right.
$$

Based on the vector representation method, M, $D_{1}$ , $D_{2}$ , $D_{3}$ , $D_{4}$ , and $D_{5}$ can be represented by the vectors $\overline{M}$ , $\overline{D}_{1}$ , $\overline{D}_{2}$ , $\overline{D}_{3}$ , $\overline{D}_{4}$ , and $\overline{D}_{5}$ , respectively, where

$$
\overline {{M}} = \langle 0. 8 0, 0. 0 0, 0. 5 0, 0. 0 0, 0. 2 0, 0. 0 0 \rangle
$$

$$
\overline {{{D}}} _ {1} = \langle 0. 9 0, 0. 0 0, 0. 0 0, 0. 0 0, 0. 3 0, 0. 0 0 \rangle
$$

$$
\overline {{{D}}} _ {2} = \langle 0. 0 0, 0. 9 5, 0. 0 0, 0. 5 0, 0. 0 0, 0. 1 0 \rangle
$$

$$
\overline {{{D}}} _ {3} = \langle 0. 0 0, 0. 0 0, 0. 9 0, 0. 0 0, 0. 3 0, 0. 0 0 \rangle
$$

$$
\overline {{{D}}} _ {4} = \langle 0. 0 0, 0. 0 0, 0. 0 0, 0. 9 0, 0. 0 0, 0. 6 0 \rangle
$$

$$
\overline {{{D}}} _ {5} = \langle 0. 0 0, 0. 0 0, 0. 0 0, 0. 0 0, 0. 9 0, 0. 4 0 \rangle .
$$

Assume that the weighted vectors of $D_1, D_2, D_3, D_4$ , and $D_5$ are $\overline{W}_1, \overline{W}_2, \overline{W}_3, \overline{W}_4$ , and $\overline{W}_5$ , respectively, where $\overline{W}_1 = \langle 1.00, 0.00, 0.00, 0.00, 0.20, 0.00 \rangle$ $\overline{W}_2 = \langle 0.00, 1.00, 0.00, 0.50, 0.00, 0.10 \rangle$

$$
\overline {{{W}}} _ {3} = \langle 0. 0 0, 0. 0 0, 1. 0 0, 0. 0 0, 0. 2 0, 0. 0 0 \rangle
$$

$$
\overline {{W}} _ {4} = \langle 0. 0 0, 0. 0 0, 0. 0 0, 1. 0 0, 0. 0 0, 0. 5 0 \rangle
$$

$$
\overline {{{W}}} _ {5} = \langle 0. 0 0, 0. 0 0, 0. 0 0, 0. 0 0, 1. 0 0, 0. 2 0 \rangle , \text { then }
$$

$$
\begin{array}{r l} Q & = M \cap D _ {1} \\ & = \left\{(m _ {1}, 0. 8 0), (m _ {2}, 0. 0 0), (m _ {3}, 0. 0 0), \right. \\ & \quad (m _ {4}, 0. 0 0), (m _ {5}, 0. 2 0), (m _ {6}, 0. 0 0) \}; \end{array}
$$

$$
T = \left\{m _ {1}, m _ {5} \right\}.
$$

Because $T \neq \emptyset$ , we get $y_1 = F(\overline{M}, \overline{D}_1, \overline{W}_1) = 0.90$ . Since $0.90 > \lambda$ , we obtain $c_1 = 0.90 * 0.98 \simeq 0.88$ . From Table 2, we can see that the corresponding certainty level of $c_1$ is “very certain”.

when $i = 2$ ,

$$
\begin{array}{r l} Q & = M \cap D _ {2} \\ & = \left\{(m _ {1}, 0. 0 0), (m _ {2}, 0. 0 0), (m _ {3}, 0. 0 0), \right. \\ & \left. (m _ {4}, 0. 0 0), (m _ {5}, 0. 0 0), (m _ {6}, 0. 0 0) \right\}; \end{array}
$$

when $i = 3$ ,

$$
\begin{array}{r l} Q & = M \cap D _ {3} \\ & = \{(m _ {1}, 0. 0 0), (m _ {2}, 0. 0 0), (m _ {3}, 0. 5 0), \\ & \quad (m _ {4}, 0. 0 0), (m _ {5}, 0. 2 0), (m _ {6}, 0. 0 0) \}; \end{array}
$$

$$
T = \left\{m _ {3}, m _ {5} \right\}.
$$

Because $T \neq \emptyset$ , we get $y_3 = F(\overline{M}, \overline{D}_3, \overline{W}_3) = 0.65$ .

Since $0.65 > \lambda$ , we obtain $c_{3} = 0.65 * 0.92 \simeq 0.60$ . From Table 2, we can see that the corresponding certainty level of $c_{3}$ is “fairly certain”.

$$
\begin{array}{l} Q = M \cap D _ {4} \\ \quad = \left\{(m _ {1}, 0. 0 0), (m _ {2}, 0. 0 0), (m _ {3}, 0. 0 0), \right. \\ \quad \left. (m _ {4}, 0. 0 0), (m _ {5}, 0. 0 0), (m _ {6}, 0. 0 0) \right\}; \\ T = \varnothing . \\ w h e n i = 5, \\ Q = M \cap D _ {5} \\ \quad = \left\{(m _ {1}, 0. 0 0), (m _ {2}, 0. 0 0), (m _ {3}, 0. 0 0), \right. \\ \quad \left. (m _ {4}, 0. 0 0), (m _ {5}, 0. 2 0), (m _ {6}, 0. 0 0) \right\}; \\ T = \left\{m _ {5} \right\}. \end{array}
$$

Because $T \neq \emptyset$ , we get $y_5 = F(\overline{M}, \overline{D}_5, \overline{W}_5) = 0.35$ . Since $0.35 > \lambda$ , we obtain $c_5 = 0.35 * 0.96 \simeq 0.34$ . From Table 2, we can see that the corresponding certainty level of $c_{5}$ is “little certain”. Thus, we can obtain the following results:

The patient might have the disease $d_{1}$ with the degree of certainty of about 0.88 (very certain)

The patient might have the disease $d_{3}$ with the degree of certainty of about 0.60 (fairly certain)

The patient might have the disease $d_{5}$ with the degree of certainty of about 0.34 (little certain).

## 6. Conclusions

In this paper, we present a weighted fuzzy reasoning algorithm for handling medical diagnostic problems. The algorithm is more flexible than the ones we presented in [3] and [4] due to the fact that it allows each symptom in medical diagnosis to have a different degree of importance. The algorithm can be executed very efficiently. If the knowledge base contains n fuzzy production rules and there are p symptoms, then the time complexity of the algorithm is $O(np)$ . In the above we assumed that the same set of symptoms is used to describe all disease features. However, if we can divide the diseases into subcategories, such that different categories of diseases are described by different vectors, then the number of symptoms included in each vector description will be reduced and the execution time of the systems will be improved.

Based on the proposed algorithm, we have implemented a medical diagnostic expert system on a PC/AT by using Turbo Pascal version 5.5 for diagnosing the diseases of the gastro-intestinal system including esophagus cancer, esophagism, gastric ulcer, stomach cancer, gastritis acute, appendicitis, duodenum ulcer, peritonitis acute, gallbladder acute, pancreatitis acute, diarrhea, hemorrhoid, large intestine cancer, and splenohepatomegalia.

## References

[1] K.P. Adlassnig, Fuzzy Set Theory in Medical Diagnosis, IEEE Trans. Syst. Man Cybern., 16, 2 (1986) 260–265.

[2] C.L. Chang, Introduction to Artificial Intelligence Techniques, JMA Press, Texas, 1985.

[3] S.M. Chen, A New Approach to Handling Fuzzy Decisionmaking Problems, IEEE Trans. Syst. Man Cybern., 18, 6 (1988) 1012–1016.

[4] S.M. Chen, J.S. Ke, and J.F. Chang, An Efficient Algorithm to Handle Medical Diagnostic Problems, Cybernetics and Systems: An International Journal, 21, 4 (1990) 377–387.

[5] S.M. Chen, J.S. Ke, and J.F. Chang, Knowledge Representation Using Fuzzy Petri Nets, IEEE Trans. on Knowledge and Data Engineering, 2, 3 (1990) 311–319.

[6] S.M. Chen, J.S. Ke, and J.F. Chang, Techniques for Handling Multicriteria Fuzzy Decision-Making Problems, Proc. of the 4th International Symposium on Computer and Information Sciences (1989) 919–925.

[7] J.S. Ke and G.T. Her, A Fuzzy Information Retrieval System Model", Proc. of National Computer Symposium (1983) 147–155.

[8] K.S. Leung and W. Lam, Fuzzy Concepts in Expert Systems, IEEE Computer, 21, 9 (1988) 43–56.

[9] K.S. Leung, W.S. Felix Wong, and W. Lam, Applications of a Novel Fuzzy Expert System Shell, Expert Systems, 6, 1 (1989) 2–10.

[10] C.V. Negoita, Expert Systems and Fuzzy Systems, Benjamin/Cummings, California, 1985.

[11] E. Sanchez, Medical Application with Fuzzy Sets, in A. Jones, A. Kaufmann, and H.-J. Zimmermann (eds.) Fuzzy Sets Theory and Applications, D. Reidel, Holland, 1986, 331–347.

[12] E. Sanchez, Medical Diagnosis and Composite Fuzzy Relations, in M.M. Gupta, R.K. Ragade, and R.R. Yager (eds.) Advances in Fuzzy Set Theory and Applications, North-Holland, 1979, 437–444.

[13] L.A. Zadeh, The Role of Fuzzy Logic in the Management of Uncertainty in Expert Systems, Fuzzy Sets and Systems, 11 (1983) 199–227.

[14] L.A. Zadeh, Fuzzy Sets, Information and Control, 8 (1965) 338–353.
