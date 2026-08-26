---
otero_id: 7766
otero_key: "2HCU22V3"
title: "Information sharing using entangled states and its applications to quantum card tricks"
authors: "Takashi Mihara"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information sharing using entangled states and its applications to quantum card tricks

Takashi Mihara ⁎

Department of Information Sciences and Arts, Toyo University, 2100 Kujirai Kawagoe, Saitama, 350-8585, Japan

## a r t i c l e i n f o

Article history: Received 6 January 2010 Received in revised form 3 September 2010 Accepted 6 November 2010 Available online 11 November 2010

Keywords: Information sharing Entangled state Cooperative game Quantum card trick

## a b s t r a c t

Quantum superposition states, especially, quantum entangled states, are useful for several <sup>fi</sup>elds such as quantum computation, quantum cryptography, quantum game theory, and so on. In this paper, <sup>fi</sup>rst, we propose methods to share entangled states without communication among players that may not know each other. Next, we introduce quantum cards and propose some quantum card tricks using this sharing method. For example, we propose tricks such that by sharing an entangled state between two spectators secretly, magicians make a spectator's card number and another spectator's card number the same.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Quantum superposition states have many strange properties. For example, let

$$
\left| 0 _ {x} \right\rangle = 1 / \sqrt {2} \left(\left| 0 _ {z} \right\rangle + \left| 1 _ {z} \right\rangle\right), \text {and} \left| 1 _ {x} \right\rangle = 1 / \sqrt {2} \left(\left| 0 _ {z} \right\rangle - \left| 1 _ {z} \right\rangle\right).
$$

Here, let the states $| 0 _ { z } \rangle$ and $| 1 _ { z } \rangle$ be the states corresponding to the values 0 and 1 on z-axis. At that time, it is known that the states $| 0 _ { x } \rangle$ and $| 1 _ { x } \rangle$ mean the states corresponding to the values 0 and 1 on x-axis. We de<sup>fi</sup>ne the notation |⋅〉 in Section $^ { 2 , }$ and these are called quantum bits or qubits as values corresponding to classical bits.

Now, Alice makes a state

$$
\frac {1}{\sqrt {2}} (| 0 _ {z} \rangle | 0 _ {x} \rangle - | 1 _ {z} \rangle | 1 _ {x} \rangle).
$$

This state can also express as follows:

$$
\frac {1}{\sqrt {2}} (| 0 _ {x} \rangle | 1 _ {z} \rangle + | 1 _ {x} \rangle | 0 _ {z} \rangle).
$$

Here, let us consider a game that Alice guesses by using the state whether Carol chooses 0 or 1. Namely, Alice predicts Carol's choice by the state. If Carol chooses 0, Alice measures on z-axis for the <sup>fi</sup>rst qubit $b _ { 1 }$ and measures on x-axis for the second qubit $b _ { 2 } .$ Then, $b _ { 1 } \oplus b _ { 2 } = 0 .$ Otherwise, if Carol chooses 1, Alice measures on x-axis for the <sup>fi</sup>rst qubit and measures on z-axis for the second qubit. Then, $b _ { 1 } \oplus b _ { 2 } = 1$ Thus, Alice can make one state that possesses two values corresponding to Carol's will although Alice must know Carol's will before measurement.

This is a simple game, but represents a characteristic property of quantum states. The security of many quantum key distribution systems is also based on this property [1,2,8]. Distributors hide information against eavesdroppers by switching from one axis to another axis at random.

Moreover, Meyer proposed a quantum strategy for a coin <sup>fl</sup>ipping game, and showed that the quantum strategy has an advantage over the classical ones [12]. In addition, he also showed the importance of a relationship between quantum game theory and quantum algorithms. After that, other types of quantum strategies have been also proposed. For example, Eisert et al. proposed a quantum strategy with entangled states for a famous two-player game called the Prisoner's Dilemma [7] (also see Refs. [4–6,10]). Marinatto et al. also proposed a quantum strategy with entangled states for another famous two-player game called the Battle of the Sexes [11]. For these games, they showed quantum Nash equilibriums different from the classical ones by using quantum states. As a summary of this <sup>fi</sup>eld, see, e.g., Ref. [9].

In this paper, <sup>fi</sup>rst, we propose methods to share entangled states without communication among players that do not share them. This means that players sharing entangled states may not know each other. Next, we propose some quantum card tricks based on this method. By de<sup>fi</sup>ning quantum cards, magicians show some card tricks to spectators. For example, we propose tricks such that by sharing an entangled state between two spectators secretly, magicians make a spectator's card number and another spectator's card number the same. Namely, by showing some quantum tricks, we propose methods manipulating as if a player's choice were led by another player's will and methods sharing/guessing a player's choice among some other players without knowing the choice. In Ref. [14], we have proposed the similar quantum tricks, i.e., quantum coin and card tricks. The card tricks in that paper use cards whose numbers are written in both sides. On the other hand, in this paper, we use cards whose numbers are written in one side. In addition, we also focus on tricks using remote communications among players (magicians and spectators).

Our results seem to be related to game theory, especially, quantum pseudo-telepathy (see, e.g., Ref. [3] and references therein). Now, let us consider two players, Alice and Bob. Assume that they cannot communicate with each other, but that they share entangled states beforehand. Pseudo-telepathy game is as follows. Let x be Alice's input and y be Bob's input. Moreover, let w be a winning condition. Then, the players make a strategy $f ( x , y , g ( x , y ) )$ , where g is a strategy computing the players' outputs. The game is whether they can <sup>fi</sup>nd outputs corresponding to $w { = } f ( x , y , g ( x , y ) )$ . In order to compute ${ \boldsymbol { g } } ,$ the players use the entangled states in the quantum strategy. In addition, in quantum pseudo-telepathy game, every player has the same ability generally. On the other hand, although our strategies also use entangled states, there exist two types of players, magicians and spectators. Magicians know all the information of strategies, but spectators know only a part of them. Moreover, magicians can also manipulate spectators' information (i.e., quantum states) in our games. Consequently, our tricks are to make strategies that lead to outputs corresponding magicians' will although quantum pseudo-telepathy game is to <sup>fi</sup>nd outputs corresponding to a winning condition.

The remainder of this paper has the following organization. In Section 2, we de<sup>fi</sup>ne notations and basic operations used in this paper. In Section $^ { 3 , }$ we propose methods sharing entangled states among players without communication. In Section 4, <sup>fi</sup>rst, we de<sup>fi</sup>ne quantum cards. Then, we show some magician's techniques, and propose several quantum card tricks. Finally, in Section $5 ,$ we provide some concluding remarks.

## 2. Preliminaries

In this subsection, we de<sup>fi</sup>ne some basic notations used in this paper. Let $\mathbf { B } { = } \{ 0 , 1 \} , \ \mathbf { Z } _ { n } { = } \{ 0 , 1 , . . . , n - 1 \}$ , and $\pmb { Z } _ { n } ^ { + } = \{ 1 , 2 , . . . , n - 1 \}$ for a positive integer n. Let a and b be integers. We say that a is congruent to b to modulus n if n is a divisor of a–b and denote by a≡b (modn). Moreover, let ⊕ be an exclusive-OR operator, e.g., (1,1,0,0)⊕ $( 1 , 0 , 1 , 0 ) = ( 0 , 1 , 1 , 0 )$

Next, we denote quantum states in the following way. Let $| 0 \rangle = \left( 1 \quad 0 \right) ^ { T }$ and $\vert 1 \rangle \overset { \cdot } { = } \left( 0 \begin{array} { c c } { 1 } \end{array} \right) ^ { T }$ , where $A ^ { T }$ is the transposed matrix of a matrix A. These states correspond to values 0 and 1 of classical bits, and are called qubits. We denote an n-qubit state by $\left| b _ { 1 } \right. \otimes \left| b _ { 2 } \right.$ $\otimes \cdots \otimes | b _ { n } \rangle = | b _ { 1 } \rangle | b _ { 2 } \rangle \cdots | b _ { n } \rangle = | b _ { 1 } b _ { 2 } \cdots b _ { n } \rangle$ , where ⊗ is a tensor product and $b _ { i } { \in } \mathbf { B } ( i { = } 1 , 2 , . . . , n )$ . In addition, we denote a set of states of an N-dimensional system by ${ \bf Z } _ { N _ { a } } = \{ \left| x \right. \left| x \in { \bf Z } _ { N } \right\}$ , where $N ( \geq 2 )$ is an integer. We call |x〉 a quantum register. We also abbreviate $\underbrace { | x \rangle | { \overline { { x } } } \rangle \cdots | x \rangle } _ { \mathrm { ~ } } \tan \vert x \rangle ^ { \otimes n }$ . Moreover, the outcome of a state can be obtained {z

by only measurement. Here, let $\begin{array} { r l } { \sum _ { x _ { 1 } } \sum _ { x _ { 2 } } \alpha _ { x _ { 1 } x 2 } | x _ { 1 } \rangle | x _ { 2 } \rangle } & { { } } \end{array}$ be a state, where $| \alpha _ { x _ { 1 } x 2 } | ^ { 2 } = 1$ . Then, by measurement on the <sup>fi</sup>rst register (without loss of generality), the state becomes $\sum { _ { x _ { 2 } } ( \alpha _ { c x _ { 2 } } / \sum _ { x _ { 2 } } \lvert \alpha _ { c x _ { 2 } } \rvert ^ { 2 } ) \lvert c \rangle }$ |x 〉 with probability $\textstyle \sum _ { x _ { 2 } } | \alpha _ { c x _ { 2 } } | ^ { 2 }$ , where c is the outcome.

Finally, we denote some unitary matrices used for quantum tricks. We use $2 \times 2$ unitary matrices

$$
H = \frac {1}{\sqrt {2}} \left( \begin{array}{c c} 1 & 1 \\ 1 & - 1 \end{array} \right) \text { and } S (\theta) = \left( \begin{array}{c c} 1 & 0 \\ 0 & e ^ {\imath \pi \theta} \end{array} \right)
$$

for one-qubit state transition, where $\ l ^ { 2 } = - 1$ . The matrix H is called a Walsh–Hadamard operator. Note that $\boldsymbol { H } ^ { - 1 } = \boldsymbol { H }$ and $S ^ { - 1 } ( \theta ) { = } S ( - \theta )$

Moreover, we de<sup>fi</sup>ne two operations for N-state transition. Let ${ \boldsymbol { x } } \in \mathbf { Z } _ { N } .$ A quantum Fourier transform QFT [15] is

$$
Q F T | x \rangle = \frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} e ^ {i 2 \pi x y / N} | y \rangle ,
$$

and

$$
Q F T ^ {- 1} | x \rangle = \frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} e ^ {- \imath 2 \pi x y / N} | y \rangle .
$$

We also de<sup>fi</sup>ne a shift operator, $S _ { E } ( \theta )$ , by

$$
S _ {E} (\theta) | x \rangle = e ^ {\imath \pi \theta x} | x \rangle .
$$

Note that ${ S _ { E } } ^ { - 1 } ( \theta ) = { S _ { E } } ( - \theta )$ . For example, this operator can be constructed as follows. Let $\scriptstyle x = \sum _ { i = 0 } ^ { n - 1 } b _ { i } 2 ^ { i }$ , where $b _ { i } \in { \bf B } ( i = 0 , 1 , . . . ,$ $n - 1 )$ . Then, |x〉 can be represented as the tensor product of qubits, $\mathfrak { i . e . , } | x \rangle = | b _ { n - 1 } , b _ { n - 2 } , . . . , b _ { 0 } \rangle$ 〉. We apply $S ( \theta 2 ^ { n - 1 } )$ for the <sup>fi</sup>rst qubit state, $S ( \theta 2 ^ { n - 2 } )$ for the second qubit state, and so on. Finally, we apply $S ( \theta 2 ^ { 0 } )$ for the last qubit state. Then, the state becomes

$$
e ^ {1 \pi \theta \sum_ {i = 0} ^ {n - 1} b _ {i} 2 ^ {i}} | x \rangle = e ^ {1 \pi \theta x} | x \rangle .
$$

This means that $S _ { E } ( \theta ) = \varPi _ { i = 0 } ^ { n - 1 } ( I ^ { \otimes n - i - 1 } \otimes S ( \theta 2 ^ { i } ) \otimes I ^ { \otimes i } )$ , let I be the $2 \times 2$ identity matrix and $I ^ { \otimes 0 }$ be also no operation.

Finally, throughout this paper, note that an operation $| x \rangle \to | x \circ y \rangle$ for any arithmetic operation ∘ is always executed by $\vert x \rangle  \vert x \circ y ( { \mathrm { m o d } } N ) \rangle$ .

## 3. Quantum information sharing

In this section, we show methods sharing entangled states among players. For example, we can make a simple entangled state by adding the <sup>fi</sup>rst register to the second register as follows:

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | 0 \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle .
$$

First, we show methods concatenating some quantum states. These results can be used in order to share entangled states among known/ unknown players that do not share them. In addition, by sharing the entangled states, the players can also share some information as mentioned in the next section.

Lemma 3.1. Let

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} | x \rangle^ {\otimes n _ {1}} a n d \frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} \beta_ {y} | y \rangle^ {\otimes n _ {2}},
$$

where $n _ { 1 } \geq 1$ and $n _ { 2 } \geq 2 ,$ , and let $\alpha _ { x }$ and $\beta _ { y }$ be complex numbers such that $\begin{array} { r } { \sum _ { x = 0 } ^ { N - 1 } | \alpha _ { x } | ^ { 2 } = 1 } \end{array}$ and $\begin{array} { r } { \sum _ { y = 0 } ^ { N - 1 } \lvert \beta _ { y } \rvert ^ { 2 } = 1 } \end{array}$

Then, we can make an entangled state

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} \beta_ {x + c} | x \rangle^ {\otimes n _ {1}} | x + c \rangle^ {\otimes n _ {2} - 1}
$$

for a constant $\mathbf { c } \in \mathbf { Z } _ { N } .$

Proof. First, we subtract the last register of the <sup>fi</sup>rst state from the <sup>fi</sup>rst register of the second state (without loss of generality, we can obtain the same result also by executing other registers).

$$
\begin{array}{l}\left(\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} | x \rangle^ {\otimes n _ {1}}\right) \left(\frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} \beta_ {y} | y \rangle^ {\otimes n _ {2}}\right)\\\rightarrow \frac {1}{\sqrt {N ^ {2}}} \sum_ {x = 0} ^ {N - 1} \sum_ {y = 0} ^ {N - 1} \alpha_ {x} \beta_ {y} | x \rangle^ {\otimes n _ {1}} | y - x \rangle | y \rangle^ {\otimes n _ {2} - 1}.\end{array}
$$

Next, we measure the <sup>fi</sup>rst register of the second state. Let c be the outcome, $\mathrm { i } . \mathrm { e } . , y - x = c .$ Therefore, the state becomes

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} \beta_ {x + c} | x \rangle^ {\otimes n _ {1}} | x + c \rangle^ {\otimes n _ {2} - 1}.
$$

Here, we omit the measured register.

Then, the statement of this lemma is satis<sup>fi</sup>ed.

The following corollary is a result using limited states. For instance, these states can be made by using a quantum Fourier transform QFT.

Corollary 1. Let

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r _ {1} x / N} | x \rangle^ {\otimes n _ {1}} a n d \frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r _ {2} y / N} | y \rangle^ {\otimes n _ {2}},
$$

where let $n _ { 1 } \geq 1 ,$ n<sub>2</sub>≥2, and $r _ { 1 } , r _ { 2 } { \in } Z .$

Then, we can make an entangled state

$$
\frac {1}{\sqrt {N}} e ^ {\mathrm{i} 2 \pi r _ {2} c / N} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi (r _ {1} + r _ {2}) x / N} | x \rangle^ {\otimes n _ {1}} | x + c \rangle^ {\otimes n _ {2} - 1}
$$

for a constant $c \in Z _ { N } .$

Moreover, we can also remove a constant c from the sharing entangled states because this value is known to a player.

Corollary 2. Let

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} | x \rangle^ {\otimes n _ {1}} a n d \frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} \beta_ {y} | y \rangle^ {\otimes n _ {2}},
$$

where $n _ { 1 } \geq 1$ and $n _ { 2 } \geq 2 ,$ , and let $\alpha _ { x }$ and $\beta _ { y }$ be complex numbers such that $\begin{array} { r } { \sum _ { x = 0 } ^ { N - 1 } \lvert \alpha _ { x } \rvert ^ { 2 } = 1 } \end{array}$ and $\begin{array} { r } { \sum _ { y = 0 } ^ { N - 1 } \lvert \beta _ { y } \rvert ^ { 2 } = 1 . } \end{array}$

Then, we can make an entangled state

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} \beta_ {x + c} | x \rangle^ {\otimes n _ {1} + n _ {2} - 1}.
$$

Especially, when $\alpha _ { x } { = } e ^ { \imath 2 \pi r _ { 1 } x / N }$ and $\beta _ { y } = e ^ { { { 1 2 \pi } { r _ { 2 } } y } / { N } } \operatorname { f o r } { r _ { 1 } } , { r _ { 2 } } \in Z$ and we know the values of $r _ { 1 }$ and $r _ { 2 } ,$ we can make an entangled state

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle^ {\otimes n _ {1} + n _ {2} - 1}.
$$

Proof. These results can be immediately obtained by Lemma 3.1 and Corollary 1, i.e., by removing the phases with $r _ { 1 } , r _ { 2 } ,$ and c, we can make the statements of this corollary.

These results can be easily extended to share an entangled state from m states.

Corollary 3. Let

$$
\frac {1}{\sqrt {N}} \sum_ {x _ {i} = 0} ^ {N - 1} \alpha_ {x _ {i}} ^ {(i)} | x _ {i} \rangle^ {\otimes n _ {i}}
$$

be m states, where $i { \in } \{ 1 , 2 , . . . , m \}$ . Here, let $n _ { \scriptscriptstyle { 1 } } \geq$ 1 and $n _ { i } { \geq } 2 f o r j { \in } \{ 2 , 3 , . . . , m \}$ and let $\alpha _ { x _ { i } } ^ { ( i ) }$ be a complex number such that $\begin{array} { r } { \sum _ { x _ { i } = 0 } ^ { N - 1 } \lvert \stackrel { \prime } { \alpha } _ { x _ { i } } ^ { ( i ) } \rvert ^ { 2 } = 1 . } \end{array}$

Then, we can make an entangled state

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x _ {1}} ^ {(1)} \prod_ {i = 2} ^ {m} \alpha_ {x _ {1} + c _ {i}} ^ {(i)} | x \rangle^ {\otimes n _ {1}} | x + c _ {2} \rangle^ {\otimes n _ {2} - 1} \dots | x + c _ {m} \rangle^ {\otimes n _ {m} - 1},
$$

where a constant $c _ { i } \in Z _ { N } \mathrm { f o r } i \in \{ 2 , 3 , . . . , m \} .$

Next, we show methods removing a register from an entangled state. These results can be used in order to take a player's quantum state off from an entangled state.

Lemma 3.2. Let

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} | x \rangle^ {\otimes n},
$$

where $n { \geq } 2 ,$ and let $\alpha _ { x }$ be a complex number such that $\begin{array} { r } { \sum _ { x = 0 } ^ { N - 1 } | \alpha _ { x } | ^ { 2 } = 1 } \end{array}$ Then, we can make a state

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} e ^ {\mathrm{i} 2 \pi c x / N} | x \rangle^ {\otimes n - 1}
$$

for a constant ${ \boldsymbol { c } } \in \mathbf { Z } _ { N } .$ Especially, when a state is

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r x / N} | x \rangle^ {\otimes n}
$$

for $r { \in } \mathbf { Z } ,$ we can make a state

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {i 2 \pi (r + c) x / N} | x \rangle^ {\otimes n - 1}.
$$

Proof. First, we execute an operation $Q F T$ to the <sup>fi</sup>rst register (without loss of generality, we can obtain the same result also by executing another register).

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} | x \rangle^ {\otimes n}\\\rightarrow \frac {1}{\sqrt {N ^ {2}}} \sum_ {x = 0} ^ {N - 1} \sum_ {y = 0} ^ {N - 1} \alpha_ {x} e ^ {i 2 \pi x y / N} | y \rangle | x \rangle^ {\otimes n - 1}.\end{array}
$$

Next, we measure the <sup>fi</sup>rst register. Let c be the outcome. Therefore, the state becomes

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} \alpha_ {x} e ^ {i 2 \pi c x / N} | x \rangle^ {\otimes n - 1}.
$$

Here, we omit the measured register. Then, the <sup>fi</sup>rst statement of this lemma is satis<sup>fi</sup>ed.

The second statement of this lemma is immediately obtained by $\alpha _ { x } { = } e ^ { \imath 2 \pi r x / N }$ □

Moreover, by the same reason as Corollary $^ { , 2 , }$ we can also remove a constant c from the sharing entangled states.

Corollary 4. Let

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {1 2 \pi r x / N} | x \rangle^ {\otimes n},
$$

where $n { \geq } 2$ and $r \in Z .$ Then, we can make a state

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle^ {\otimes n - 1}.
$$

Proof. This result can be immediately obtained by Lemma 3.1, i.e., by removing the phase with r and c, we can make the statement of this corollary.

## 4. Quantum card tricks

## 4.1. Quantum cards

In this subsection, <sup>fi</sup>rst, we de<sup>fi</sup>ne cards used in this paper.

A classical card is denoted by |m〉, where $m { \in } { \mathbf { Z } } _ { N }$ . That is, a classical card is a quantum state decided to a number with certainty. On the other hand, a quantum superposition card is denoted by $\textstyle \sum _ { x } ^ { N - 1 } { _ { 0 } ^ { } \mathbf { \alpha } \alpha _ { x } ^ { } } | x \rangle$ , where $\alpha _ { x }$ is a complex number satisfying $\begin{array} { r } { \sum _ { x = 0 } ^ { N - 1 } | \alpha _ { x } ^ { * } | ^ { 2 } = 1 } \end{array}$ . A quantum card is a quantum state decided to a classical card corresponding to a number x with probability $| \alpha _ { x } | ^ { 2 }$ . For example, we can make a quantum superposition card from a classical card |m〉 by QFT. Namely,

$$
| m \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x \rangle .
$$

Moreover, let $\left| { c _ { i } } \right.$ for i∈ $\mathbf { z } _ { N }$ be a classical/quantum card. Then, a deck $o f$ cards is denoted by $\otimes _ { i } ^ { N - 1 } { = } _ { 0 } ^ { 1 } | c _ { i } \rangle$

Next, we show some fundamental operations using cards.

A quantum cut is denoted by

$$
| m \rangle \rightarrow | m + r \rangle a n d \sum_ {x = 0} ^ {N - 1} \alpha_ {x} | x \rangle \rightarrow \sum_ {x = 0} ^ {N - 1} \alpha_ {x} | x + r \rangle ,
$$

where $r { \in } { \mathbf { Z } } _ { N }$ $\boldsymbol { \mathbf { \rho } } _ { = \mathbf { Z } _ { N } , \Lambda }$ quantum shuffle is denoted by

$$
| m \rangle \rightarrow | r ^ {\prime} m \rangle \text {   and   } \sum_ {x = 0} ^ {N - 1} \alpha_ {x} | x \rangle \rightarrow \sum_ {x = 0} ^ {N - 1} \alpha_ {x} | r ^ {\prime} x \rangle .
$$

where $\boldsymbol { r } ^ { \prime } { \in } { \mathbf { Z } _ { N } } ^ { + }$ and N are relatively prime. This condition means that r x ≢r′x′(modN) if x≢x′(modN).

Finally, we de<sup>fi</sup>ne a quantum box. A quantum box is a box such that a player can execute any operation mentioned in Section 2 but cannot obtain any information without measurement. We use a quantum box in order to hide the information of cards. The methods taking some information out from the box are to measure states or to open the box. A player can obtain a partial information from measurement, e.g., the outcome of some register(card). On the other hand, all the information of cards is obtained by opening the box.

## 4.2. Basic tricks

In this subsection, we show some magicians' basic techniques. Throughout this paper, let Alice and Bob be magicians, and Carol and Davis be spectators. In addition, let Alice and Carol be one pair, and Bob and Davis be another pair in each game, and let Alice and Bob can manipulate Carol's states and Davis's states, respectively. Any player cannot know the content of quantum states without measurement, and only magicians can measure states partially. Moreover, although magicians know all the procedures of tricks and communicate with each other when necessary, spectators execute faithfully the procedures ordered by magicians.

The following two tricks are magicians' fundamental techniques.

False cut: The number of a card that a spectator Carol selects is maintained also after a cut.

Method for false cut

(1) Carol selects a card |m〉 for m∈ $\mathbf { \Delta } [ { \bf Z } _ { N } ,$ , and does not tell it to anybody. She puts it in a quantum box.

(2) Alice executes QFT.

$$
| m \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {1 2 \pi m x / N} | x \rangle .
$$

(3) Carol executes a cut in the following way.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x + r \rangle ,
$$

where $r { \in } { \mathbf { Z } } _ { N } .$

(4) Alice executes $\boldsymbol { Q } \boldsymbol { F } \boldsymbol { T } ^ { - 1 } .$

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\imath 2 \pi m x / N} | x + r \rangle\\\rightarrow \frac {1}{\sqrt {N ^ {2}}} \sum_ {x = 0} ^ {N - 1} e ^ {\imath 2 \pi m x / N} \sum_ {y = 0} ^ {N - 1} e ^ {- \imath 2 \pi (x + r) y / N} | y \rangle\\= \frac {1}{\sqrt {N ^ {2}}} \sum_ {y = 0} ^ {N - 1} e ^ {- \imath 2 \pi r y / N} \sum_ {x = 0} ^ {N - 1} e ^ {\imath 2 \pi (m - y) x / N} | y \rangle\\= e ^ {- \imath 2 \pi r m / N} | m \rangle .\end{array}
$$

(5) Then, Carol opens the box and obtains |m〉.

Obviously, Alice can succeed the false cut even if Carol executes cuts several times in step 3.

False shuf<sup>fl</sup>e: The number of a card that a spectator Carol selects is maintained also after shuf<sup>fl</sup>es.

Method for false shuf<sup>fl</sup>e

(1) Carol selects a card |m〉 for $m { \in } { \mathbf { Z } } _ { N } ,$ , and executes a shuf<sup>fl</sup>e. Then, the state becomes

$$
| m \rangle \rightarrow | r m \rangle ,
$$

where let $r ^ { 2 } \not \equiv 1 ( \mathrm { m o d } N )$ for $r { \in } { \bf { Z } } _ { N } ^ { + }$ . She does not tell it to anybody, and puts it in a quantum box.

(2) Alice executes QFT.

$$
| r m \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {i 2 \pi r m x / N} | x \rangle .
$$

(3) Carol executes a shuf<sup>fl</sup>e.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r m x / N} | x \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | r x \rangle .
$$

(4) Alice executes $Q F T ^ { - 1 }$

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r m x / N} | r x \rangle\\\rightarrow \frac {1}{\sqrt {N ^ {2}}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r m x / N} \sum_ {y = 0} ^ {N - 1} e ^ {- \mathrm{i} 2 \pi r x y / N} | y \rangle\\= \frac {1}{\sqrt {N ^ {2}}} \sum_ {y = 0} ^ {N - 1} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r (m - y) x / N} | y \rangle = | m \rangle .\end{array}
$$

(5) Then, Carol opens the box and obtains |m〉.

Next, we consider tricks using two or more cards. In the following, we show a trick that cannot guess the number by one card but can guess the numbers by two or more cards.

Double guess: A magician Alice guesses the numbers of two successive cards that a spectator Carol selects.

Method for double guess

(1) Carol selects two successive cards |m〉 and $| m + 1 \rangle$ for $m { \in } { \mathbf { Z } } _ { N }$ and executes a shuf<sup>fl</sup>e.

$$
| m \rangle \rightarrow | r _ {1} m \rangle \text { and } | m + 1 \rangle \rightarrow | r _ {1} (m + 1) \rangle ,
$$

where $\boldsymbol { r } _ { 1 } { \in } \boldsymbol { { \mathbf { Z } } } _ { N } ^ { + }$ . She puts them in a quantum box.

(2) Alice executes QFT.

$$
\begin{array}{l} | r _ {1} m \rangle \to \frac {1}{\sqrt {N}} \sum_ {x _ {1} = 0} ^ {N - 1} e ^ {i 2 \pi r _ {1} m x _ {1} / N} | x _ {1} \rangle , \text { and } \\ | r _ {1} (m + 1) \rangle \to \frac {1}{\sqrt {N}} \sum_ {x _ {2} = 0} ^ {N - 1} e ^ {i 2 \pi r _ {1} (m + 1) x _ {2} / N} | x _ {2} \rangle . \end{array}
$$

(3) Carol executes a cut.

$$
\begin{array}{l} \frac {1}{\sqrt {N}} \sum_ {x _ {1} = 0} ^ {N - 1} e ^ {\imath 2 \pi r _ {1} m x _ {1} / N} | x _ {1} \rangle \to \frac {1}{\sqrt {N}} \sum_ {x _ {1} = 0} ^ {N - 1} e ^ {\imath 2 \pi r _ {1} m x _ {1} / N} | x _ {1} + r _ {2} \rangle , \text { and } \\ \frac {1}{\sqrt {N}} \sum_ {x _ {2} = 0} ^ {N - 1} e ^ {\imath 2 \pi r _ {1} (m + 1) x _ {2} / N} | x _ {2} \rangle \to \frac {1}{\sqrt {N}} \sum_ {x _ {2} = 0} ^ {N - 1} e ^ {\imath 2 \pi r _ {1} (m + 1) x _ {2} / N} | x _ {2} + r _ {2} \rangle , \end{array}
$$

where $r _ { 2 } { \in } { \bf Z } _ { N } .$

(4) Alice executes $Q F T ^ { - 1 }$

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x _ {1} = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r _ {1} m x _ {1} / N} | x _ {1} + r _ {2} \rangle\\\rightarrow \frac {1}{\sqrt {N ^ {2}}} \sum_ {x _ {1} = 0} ^ {N - 1} \sum_ {y _ {1} = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r _ {1} m x _ {1} / N} e ^ {- \mathrm{i} 2 \pi (x _ {1} + r _ {2}) y _ {1} / N} | y _ {1} \rangle\\= \frac {1}{\sqrt {N ^ {2}}} \sum_ {y _ {1} = 0} ^ {N - 1} e ^ {- \mathrm{i} 2 \pi r _ {2} y _ {1} / N} \sum_ {x _ {1} = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi (r _ {1} m - y _ {1}) x _ {1} / N} | y _ {1} \rangle\\= \frac {1}{\sqrt {N}} \sum_ {r _ {1} m - y _ {1} = 0 (\text { mod } N)} e ^ {- \mathrm{i} 2 \pi r _ {2} y _ {1} / N} | y _ {1} \rangle ,\end{array}
$$

and

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x _ {2} = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi r _ {1} (m + 1) x _ {2} / N} | x _ {2} + r _ {2} \rangle\\\rightarrow \frac {1}{\sqrt {N}} \sum_ {r _ {1} (m + 1) - y _ {2} \equiv 0 (\mathrm{mod} N)} e ^ {- \mathrm{i} 2 \pi r _ {2} y _ {2} / N} | y _ {2} \rangle .\end{array}
$$

(5) Alice measures the states and obtains $y _ { 1 }$ and $y _ { 2 }$ satisfying $r _ { 1 } m - y _ { 1 } \equiv 0 ( \mathrm { m o d } N )$ and $r _ { 1 } ( m + 1 ) - y _ { 2 } { \equiv } 0$ (modN). Therefore, she can guess m (and $r _ { 1 } )$ .

This trick can be easily extended to two cards $| m _ { 1 } \rangle$ and $| m _ { 2 } \rangle$ such that $m _ { 2 } = m _ { 1 } + c$ for a known number c, or to multiple successive cards, and so on.

## 4.3. Quantum tricks using entangled states

In this subsection, we show quantum card tricks using entangled states. The <sup>fi</sup>rst trick is a trick such that a spectator's card number coincides with a magician's card number.

Magician's coincidence: A magician Alice guesses the number of a card that a spectator Carol selects.

Method for magician's coincidence

(1) Carol makes a quantum superposition card from |0〉, i.e., she executes $Q F T .$

$$
| 0 \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle .
$$

She puts it in a quantum box.

(2) Alice makes an entangled state between Carol's state and another state [0>.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | 0 \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle .
$$

(3) Carol executes a cut.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x + r \rangle | x \rangle ,
$$

where $r \in \mathbf { Z } _ { N }$

(4) Carol executes $Q F T ^ { - 1 }$ and Alice executes QFT.

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x + r \rangle | x \rangle\\\rightarrow \frac {1}{\sqrt {N ^ {3}}} \sum_ {y _ {1} = 0} ^ {N - 1} \sum_ {y _ {2} = 0} ^ {N - 1} \sum_ {x = 0} ^ {N - 1} e ^ {- \mathrm{i} 2 \pi (x + r) y _ {1} / N} e ^ {\mathrm{i} 2 \pi x y _ {2} / N} | y _ {1} \rangle | y _ {2} \rangle\\= \frac {1}{\sqrt {N ^ {3}}} \sum_ {y _ {1} = 0} ^ {N - 1} e ^ {- \mathrm{i} 2 \pi r y _ {1} / N} \sum_ {y _ {2} = 0} ^ {N - 1} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi (y _ {2} - y _ {1}) x / N} | y _ {1} \rangle | y _ {2} \rangle\\= \frac {1}{\sqrt {N}} \sum_ {y _ {2} - y _ {1} \equiv 0 (\bmod N)} e ^ {- \mathrm{i} 2 \pi r y _ {1} / N} | y _ {1} \rangle | y _ {2} \rangle .\end{array}
$$

(5) When Alice and Carol measure their registers, the two numbers are same.

This trick is a trick that a magician guesses a number. The following two tricks are tricks such that a spectator's card number coincides with another spectator's card number.

Spectators' coincidence: The numbers of cards that two spectators Carol and Davis select are same.

Method for spectators' coincidence

(1) Carol makes a quantum superposition card from $| 0 > , \mathrm { i } . \mathsf { e } . ,$ she executes QFT.

$$
| 0 \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle .
$$

She puts it in a quantum box.

(2) Alice makes an entangled state between Carol's state and another state |0〉.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | 0 \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle .
$$

(3) Davis also makes a quantum superposition card from $| 0 \rangle , \mathrm { i . e . }$ , he executes $Q F T ^ { - 1 }$

$$
| 0 \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} | y \rangle .
$$

He puts it in another quantum box.

(4) Bob also makes an entangled state between Davis's state and another state |0〉.

$$
\frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} | y \rangle | 0 \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} | y \rangle | y \rangle .
$$

(5) Alice and Bob take their states off from the boxes secretly, and make the following state by Corollary 2 (applied to the second and the fourth registers).

$$
\left(\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle\right)\left(\frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} | y \rangle | y \rangle\right)\rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle | x \rangle ,
$$

where the last register is Bob's register (Alice's register is omitted). Bob returns his state in Davis's box secretly.

(6) Bob makes the following state by Corollary 4 (applied to the last register). Here, Bob also uses Davis's register.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle | x \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle ,
$$

where the <sup>fi</sup>rst register is Carol's register and the second register is Davis's register.

(7) Carol and Davis execute cuts.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x + r _ {1} \rangle | x + r _ {2} \rangle ,
$$

where $r _ { 1 } , r _ { 2 } { \in } { \bf { Z } } _ { N } .$

(8) Carol executes $Q F T ^ { - 1 }$ and Davis executes QFT.

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x + r _ {1} \rangle | x + r _ {2} \rangle\\\rightarrow \frac {1}{\sqrt {N ^ {3}}} \sum_ {y _ {1} = 0} ^ {N - 1} \sum_ {y _ {2} = 0} ^ {N - 1} \sum_ {x = 0} ^ {N - 1} e ^ {- i 2 \pi (x + r _ {1}) y _ {1} / N} e ^ {i 2 \pi (x + r _ {2}) y _ {2} / N} | y _ {1} \rangle | y _ {2} \rangle\\= \frac {1}{\sqrt {N ^ {3}}} \sum_ {y _ {1} = 0} ^ {N - 1} \sum_ {y _ {2} = 0} ^ {N - 1} e ^ {i 2 \pi (r _ {2} y _ {2} - r _ {1} y _ {1}) / N} \sum_ {x = 0} ^ {N - 1} e ^ {i 2 \pi (y _ {2} - y _ {1}) x / N} | y _ {1} \rangle | y _ {2} \rangle\\= \frac {1}{\sqrt {N}} \sum_ {y _ {2} - y _ {1} \equiv 0 (\mathrm{mod} N)} e ^ {i 2 \pi (r _ {2} y _ {2} - r _ {1} y _ {1}) / N} | y _ {1} \rangle | y _ {2} \rangle .\end{array}
$$

(9) When Carol and Davis measure their registers, the two numbers are same.

Spectators' coincidence 2: Let $y _ { 1 } , y _ { 2 } , m { \in } \mathbf { Z } _ { N } .$ . Then, the relationship between the numbers of cards that two spectators Carol and Davis select is $y _ { 1 } \equiv y _ { 2 } + m ( { \bmod { N } } )$ , where $y _ { 1 }$ is Carol's numbe $; y _ { 2 }$ is Davis's number, and m is a value that Carol(or Davis) selects and opens beforehand.

Method for spectators' coincidence 2

(1) Step 1 to step 5 are same as spectators' coincidence.

(2) Bob makes the following state by Corollary 4 (applied to the last register) and executes a shift operation. Here, Bob also uses Davis's register.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} | x \rangle | x \rangle | x \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x \rangle | x \rangle ,
$$

where the <sup>fi</sup>rst register is Carol's register and the second register is Davis's register.

(3) Carol and Davis execute cuts.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\imath 2 \pi m x / N} | x \rangle | x \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\imath 2 \pi m x / N} | x + r _ {1} \rangle | x + r _ {2} \rangle ,
$$

where $r _ { 1 } , r _ { 2 } { \in } { \bf { Z } } _ { N }$

(4) Carol executes $Q F T ^ { - 1 }$ and Davis executes QFT.

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x + r _ {1} \rangle | x + r _ {2} \rangle\\\rightarrow \frac {1}{\sqrt {N ^ {3}}} \sum_ {y _ {1} = 0} ^ {N - 1} \sum_ {y _ {2} = 0} ^ {N - 1} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} e ^ {- \mathrm{i} 2 \pi (x + r _ {1}) y _ {1} / N} e ^ {\mathrm{i} 2 \pi (x + r _ {2}) y _ {2} / N} | y _ {1} \rangle | y _ {2} \rangle\\= \frac {1}{\sqrt {N}} \sum_ {y _ {1} \equiv y _ {2} + m (\textit {m o d} N)} e ^ {\mathrm{i} 2 \pi (r _ {2} y _ {2} - r _ {1} y _ {1}) / N} | y _ {1} \rangle | y _ {2} \rangle .\end{array}
$$

(5) Carol and Davis measure. The relationship between Carol's number $y _ { 1 }$ and Davis's number is $y _ { 1 } \equiv y _ { 2 } + m ( { \bmod { N } } )$

Next, we show a trick such that two magicians share a number that a spectator selects.

Magicians' share: Beforehand, a spectator Carol selects a number m∈ $\displaystyle : \mathbf { Z } _ { N } ,$ and keeps it secret to anybody. The sum of the numbers that two magicians Alice and Bob select is $y _ { 1 } + y _ { 2 } \equiv m ( { \bmod { N } } )$ , where $y _ { 1 }$ is Alice's number, and $y _ { 2 }$ is Bob's number.

Method for magicians' share

(1) Carol makes a quantum superposition card from |m〉 for $m { \in } { \mathbf { Z } } _ { N }$ i.e., she executes QFT. Moreover, she executes a cut.

$$
| m \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x + s \rangle ,
$$

where s∈ $\mathbf { \Delta } = \mathbf { Z } _ { N } .$ She puts it in a quantum box.

(2) Beforehand, Alice and Bob share an entangled state $\begin{array} { r } { ( 1 / \sqrt { N } ) { \sum _ { v } } _ { = 0 } ^ { N - 1 } | y \rangle | y \rangle } \end{array}$ . Alice and Bob make the following state by Corollary 2 (applied to the <sup>fi</sup>rst and the second registers).

$$
\begin{array}{l}\left(\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x + s \rangle\right) \left(\frac {1}{\sqrt {N}} \sum_ {y = 0} ^ {N - 1} | y \rangle | y \rangle\right)\\\rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x + s \rangle | x + s \rangle\\= \frac {1}{\sqrt {N}} e ^ {- \mathrm{i} 2 \pi m s / N} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x \rangle | x \rangle .\end{array}
$$

In the following steps, we omit $e ^ { - \imath 2 \pi m s / N }$

(3) Carol executes a cut.

$$
\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x \rangle | x \rangle \rightarrow \frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x + r \rangle | x \rangle ,
$$

where $r { \in } { \mathbf { Z } } _ { N }$

(4) Alice and Bob execute $Q F T ^ { - 1 }$

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} | x + r \rangle | x \rangle\\\rightarrow \frac {1}{\sqrt {N ^ {3}}} \sum_ {y _ {1} = 0} ^ {N - 1} \sum_ {y _ {2} = 0} ^ {N - 1} \sum_ {x = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi m x / N} e ^ {- \mathrm{i} 2 \pi (x + r) y _ {1} / N} e ^ {- \mathrm{i} 2 \pi x y _ {2} / N} | y _ {1} \rangle | y _ {2} \rangle\\= \frac {1}{\sqrt {N}} \sum_ {y _ {1} + y _ {2} \equiv (\mathrm{mod} N)} e ^ {- \mathrm{i} 2 \pi r y _ {1} / N} | y _ {1} \rangle | y _ {2} \rangle .\end{array}
$$

(5) Alice and Bob measure. The sum of Alice's number $y _ { 1 }$ and Bob's number is $y _ { 1 } + y _ { 2 } \equiv m ( { \bmod { N } } )$

Finally, we show a trick such that a magician guesses the sum of the numbers of cards that two spectators select.

Spectators' sum: Beforehand, two spectators Carol and Davis select numbers $m _ { 1 } , m _ { 2 } { \in } { \bf Z } _ { N }$ , and keeps them secret to anybody. A magician Alice guesses the sum $m _ { 1 } + m _ { 2 } ($ (mod N) of the numbers.

Method for spectators' sum

(1) Carol selects a card $| m _ { 1 } \rangle$ , and Davis selects a card $| m _ { 2 } \rangle .$ . They put them in a quantum box.

(2) Alice executes QFT.

$$
| m _ {1} \rangle | m _ {2} \rangle \rightarrow \frac {1}{\sqrt {N ^ {2}}} \sum_ {x _ {1} = 0} ^ {N - 1} \sum_ {x _ {2} = 0} ^ {N - 1} e ^ {\imath 2 \pi (m _ {1} x _ {1} + m _ {2} x _ {2}) / N} | x _ {1} \rangle | x _ {2} \rangle .
$$

(3) Carol and Davis execute cuts.

$$
\begin{array}{l} \frac {1}{\sqrt {N ^ {2}}} \sum_ {x _ {1} = 0} ^ {N - 1} \sum_ {x _ {2} = 0} ^ {N - 1} e ^ {\imath 2 \pi (m _ {1} x _ {1} + m _ {2} x _ {2}) / N} | x _ {1} \rangle | x _ {2} \rangle \\ \to \frac {1}{\sqrt {N ^ {2}}} \sum_ {x _ {1} = 0} ^ {N - 1} \sum_ {x _ {2} = 0} ^ {N - 1} e ^ {\imath 2 \pi (m _ {1} x _ {1} + m _ {2} x _ {2}) / N} | x _ {1} + r _ {1} \rangle | x _ {2} + r _ {2} \rangle , \end{array}
$$

where $r _ { 1 } , r _ { 2 } { \in } { \bf { Z } } _ { N } .$

(4) Alice makes the following state by the procedure in Lemma 3.1.

$$
\begin{array}{l}\frac {1}{\sqrt {N ^ {2}}} \sum_ {x _ {1} = 0} ^ {N - 1} \sum_ {x _ {2} = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi (m _ {1} x _ {1} + m _ {2} x _ {2}) / N} | x _ {1} + r _ {1} \rangle | x _ {2} + r _ {2} \rangle\\\rightarrow \frac {1}{\sqrt {N}} \sum_ {x _ {1} = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi (m _ {1} x _ {1} + m _ {2} (x _ {1} + r _ {1} - r _ {2} + c)) / N} | x _ {1} + r _ {1} \rangle | c \rangle\\= \frac {1}{\sqrt {N}} e ^ {\mathrm{i} 2 \pi m _ {2} (r _ {1} - r _ {2} + c) / N} \sum_ {x _ {1} = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi (m _ {1} + m _ {2}) x _ {1} / N} | x _ {1} + r _ {1} \rangle | c \rangle ,\end{array}
$$

where $c { \in } { \mathbf { Z } } _ { N } .$

In the following step, we omit the second register and $e ^ { \imath 2 \pi m _ { 2 } ( r _ { 1 } - r _ { 2 } + c ) / N }$

(5) Alice executes QFT.

$$
\begin{array}{l}\frac {1}{\sqrt {N}} \sum_ {x _ {1} = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi (m _ {1} + m _ {2}) x _ {1} / N} | x _ {1} + r _ {1} \rangle\\\rightarrow \frac {1}{\sqrt {N ^ {2}}} \sum_ {y = 0} ^ {N - 1} e ^ {- \mathrm{i} 2 \pi r _ {1} y / N} \sum_ {x _ {1} = 0} ^ {N - 1} e ^ {\mathrm{i} 2 \pi (m _ {1} + m _ {2} - y) x _ {1} / N} | y \rangle\\= e ^ {- \mathrm{i} 2 \pi r _ {1} (m _ {1} + m _ {2}) / N} | m _ {1} + m _ {2} \rangle .\end{array}
$$

(6) Alice measures the state and obtainsm $_ 1 + m _ { 2 } ( { \bmod { N } } )$ .

## 5. Conclusions

In this paper, <sup>fi</sup>rst, we proposed methods to share entangled states without communication among players that do not share them. Since entangled states can be also used tools sharing information [13], a player can let sharing information secretly among other players that are not acquainted with each other.

Next, by using this property, we proposed some quantum card tricks. We de<sup>fi</sup>ne quantum cards and showed some fundamental techniques. Then, we proposed some tricks such that by sharing an entangled state between two spectators secretly, magicians make a spectator's card number and another spectator's card number the same.

The tricks in this paper are fundamental ones using entangled states. However, we think that we will be able to construct attractive tricks by combining our proposed tricks. In addition, since magicians use one card for one spectator in our tricks, it is an interesting problem that we construct quantum tricks combining several quantum cards.

## References

[1] C.H. Bennett, Quantum cryptography using any two nonorthogonal states, Physical Review Letters 68 (1992) 3121–3124.

[2] C.H. Bennett, G. Brassard, Quantum cryptography: public key distribution and coin tossing, Proceedings of IEEE International Conference on Computers, Systems and Signal Processing, 1984, pp. 175–179.

[3] G. Brassard, A. Broadbent, A. Tapp, Quantum pseudo-telepathy, Foundations of Physics 35 (2005) 1877–1907.

[4] J. Du, H. Li, X. Xu, M. Shi, J. Wu, X. Zhou, R. Han, Experimental realization of quantum games, on a quantum computer, Physical Review Letters 88 (2002) 137902.

[5] J. Du, H. Li, X. Xu, X. Zhou, R. Han, Entanglement enhanced multiplayer quantum games, Physics Letters A 302 (2002) 229–233.

[6] J. Eisert, M. Wilkens, Quantum games, Journal of Modern Optics 47 (2000) 2543–2556.

[7] J. Eisert, M. Wilkens, M. Lewenstein, Quantum games and quantum strategies, Physical Review Letters 83 (1999) 3077–3080.

[8] A.K. Ekert, Quantum cryptography based on Bell's theorem, Physical Review Letters 67 (1991) 661–663.

[9] H. Guo, J. Zhang, G.J. Koehler, A survey of quantum games, Decis Support Systems 46 (2008) 318–332.

[10] A. Iqbal, A.H. Toor, Evolutionarily stable strategies in quantum games, Physics Letters A.280 (2001).249-256

[11] L. Marinatto, T. Weber, A quantum approach to static games of complete information Physics Letters A 272 (2000) 291-303

[12] D.A. Meyer, Quantum strategies, Physical Review Letters 82 (1999) 1052–1055.

[13] T. Mihara, Splitting information securely with entanglement, Information and Computation 187 (2003) 110–122

[14] T. Mihara, Quantum number tricks, Journal on Software Engineering and Application 3 (2010) 240–244

[15] P.W. Shor, Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM Journal on Computing 26 (1997 1484-1509

Takashi Mihara received the B.Sc. degree in Hiroshima University in 1982, and the M. Sc. and Ph.D. degrees in Japan Advanced Institute of Science and Technology in 1994 and 1997. He is now an Associate Professor at Toyo University. His research interests include quantum algorithms, computational complexity, and decision support systems.
