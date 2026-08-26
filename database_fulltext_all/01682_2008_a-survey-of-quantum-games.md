---
otero_id: 1682
otero_key: "XVJFKWCB"
title: "A survey of quantum games"
authors: "Hong Guo; Juheng Zhang; Gary J. Koehler"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.07.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A survey of quantum games

Hong Guo, Juheng Zhang ⁎, Gary J. Koehler

Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, FL 32611, United States

## a r t i c l e i n f o

Article history: Received 9 April 2008 Received in revised form 27 June 2008 Accepted 3 July 2008 Available online 10 July 2008

Keywords: Quantum computing Game theory Nash equilibria

## a b s t r a c t

This paper presents an overview and survey of a new type of game-theoretic setting based on ideas emanating from quantum computing. (We provide a brief overview of quantum computing at the beginning of the paper.) Initial results suggest this view brings more <sup>fl</sup>exibility and possibilities into decisions involving game-theoretic considerations. Applications cover a broad spectrum of classical games as well as games in economics. finance and other areas

Published by Elsevier B.V.

## 1. Introduction

Game theory (von Neumann and Morgenstern [134] and Nash [131]) plays an important role in decision support systems and decision sciences (e.g., recent papers in this journal include [4,11,67,75,129,162,167]). This paper provides a survey of a new form of game theory — quantum game theory. In recent years a new type of computing, quantum computing, has gained considerable interests. In 1999, Meyer [127] merged game theory with quantum computing and proposed the <sup>fi</sup>rst quantized game. This started an avalanche of related papers. Quantum games offer new ways to cooperate, to remove dilemmas, to alter equilibria and much more. This survey seeks to introduce and provide a summary of quantum games to the decision sciences community. We note the interesting point that not only did John von Neumann provide seminal work in game theory but was also a key researcher in quantum mechanics, so there was an implicit historic relationship between the two areas.

In order to understand these ideas, the basics of quantum computing are required. Towards this end we start with a brief summary of quantum computing concepts, though there are many other good sources (e.g., see Nielsen and Chuang [135] for a good overview). Section 1.1 may be skipped by those already familiar with these ideas.

## 1.1. Quantum computing basics

## 1.1.1. Quantum phenomena

General purpose quantum computers do not exist yet nor are they likely to exist for 20–30 years, although small-scale laboratory models and small specialized commercial models have been developed (http://www.dwavesys.com/). On standard digital computers, the basic unit of information is a bit. A bit represents a 0 or a 1. When very small items are used to represent a zero or one, say, for example, a charged particle like an ion, quantum mechanics dictates the state and the item is called a qubit (for quantum bit — multiple qubits are often called qudits for d qubits). The qubit state can be in either pure state 0 or 1 or in a superposition where both exist simultaneously. This counterintuitive superposition of both 0 and 1 is one of the hallmarks of quantum phenomena and has been experimentally veri<sup>fi</sup>ed in countless ways and times. When performing calculations on a superposition, we end up performing the calculation on all pure states in the superposition. So if there are n qubits involved in a superposition, then the calculation takes place over all of the 2<sup>n</sup> pure states. This parallelism has no counterpart in classical computing.

When one examines or measures a qubit in a superposition state, he will observe only a pure state. This interaction of a quantum system with the environment is called decoherence and can be thought of as nature randomly picking one of the pure states in the superposition. That is, the act of observing the superposition appears to have forced nature to randomly choose one state.

Qubits can be coordinated so that they share their quantum states, even if they are not physically close to each other. This is called entanglement. For example, two qubits can be entangled so that if one is observed in state 0 the other will be in state 1, and vice versa. Until an observation is made, both qubits are in a superposition, but once one state is known, the other state is also known, even if it is extremely far away. This is the non-locality feature Einstein found objectionable [45].

Quantum phenomena of superposition, entanglement and non-locality open the door to all new ways of computing and processing information. Many interesting algorithms have been discovered that take advantage of quantum phenomena. The much celebrated result by Shor [158] provides a quantum factorization algorithm that operates in polynomial-time.

## 1.1.2. Mathematical representation

Mathematically, a qubit is represented by a 2-vector in a complex vector space as $\psi = \alpha { \binom { 1 } { 0 } } + \beta { \binom { 0 } { 1 } }$ . Here, α and $\beta$ are complex numbers called complex amplitudes. The modulus squared of each gives the probability that nature will select pure state 0 given by $\binom { 1 } { 0 }$ and pure state 1 given by $\binom { 0 } { 1 }$ respectively. Physicists often employ Dirac notation to represent quantum states. |0〉 represents pure state 0 and |1〉 pure state 1. So, an equivalent representation of a qubit is $\scriptstyle \psi = \alpha | 0 \rangle \cdot$ + β|1〉 where $1 = \vert \bar { \alpha } \vert ^ { 2 } + \vert \beta \vert ^ { 2 }$ . An n-qubit register is given by

$$
| \psi \rangle = \sum_ {x \in \{0, 1 \} ^ {n}} a _ {x} | x \rangle , \quad \text { where } 1 = \sum_ {x \in \{0, 1 \} ^ {n}} | a _ {x} | ^ {2}.
$$

This takes $2 ^ { n }$ complex numbers to completely describe its state.

The state of a composite system is the tensor product of the state of the components. For example, a composite system of two qubits, ψ and $\psi _ { 2 } ,$ written as $| \psi _ { 1 } \psi _ { 2 } \rangle$ 〉, is

$$
| \psi_ {1} \psi_ {2} \rangle = | \psi_ {1} \rangle \otimes | \psi_ {2} \rangle = \left[ \begin{array}{c} \alpha_ {1} \\ \beta_ {1} \end{array} \right] \otimes \left[ \begin{array}{c} \alpha_ {2} \\ \beta_ {2} \end{array} \right] = \left[ \begin{array}{c} \alpha_ {1} \alpha_ {2} \\ \alpha_ {1} \beta_ {2} \\ \beta_ {1} \alpha_ {2} \\ \beta_ {1} \beta_ {2} \end{array} \right].
$$

## 1.1.3. Quantum computing and information

Closed quantum mechanical systems evolve under unitary transformations. A unitary matrix, U, is a matrix whose adjoint (i.e., the conjugate transpose), U<sup>†</sup>, is its inverse. That is, $\mathbf { U } ^ { \dagger } \mathbf { U } { = } \mathbf { U } \mathbf { U } ^ { \dagger } { = } I .$ Quantum computer computation is carried-out by subjecting qubits to unitary transforms. Developing quantum algorithms requires specifying starting states and unitary transformations to achieve the desired result. Since the <sup>fi</sup>nal measured state is probabilistically chosen based on amplitudes, part of the process of crafting an algorithm either produces a state with an amplitude whose modulus squared is 1.0 or very close to 1.0. Several small sets of unitary transforms are universal, meaning any quantum computation can be reduced to using just the transforms in the set [135]. Also, simple algorithms (see [165]) can be used to do normal arithmetic operations (like addition and multiplication).

Unitary transforms function as gates do in classical computers. For example, the transform $X = { \left\lceil \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right\rceil }$ performs a NOT operation, switching pure state 0 to a 1 and vice versa. The identity transform, I, preserves the current state. The $Z = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { - 1 } \end{array} \right] }$ gate just switches the sign on state 1. The X, Z and $\begin{array} { r } { \mathbf { Y } = \left[ \begin{array} { l l } { 0 } & { - i } \\ { i } & { 0 } \end{array} \right] } \end{array}$ gates are known as Pauli gates. Here i is the usual imaginary number $i = { \sqrt { - 1 } } .$

<sup>¼</sup>Some transforms are of great use. The Hadamard transform, $\begin{array} { r } { H = \frac { 1 } { \sqrt { 2 } } \left\lceil \begin{array} { c c } { 1 } & { 1 } \\ { 1 } & { - 1 } \end{array} \right\rceil } \end{array}$ changes |0〉 to a superposition with equal probabilities for each state. That is

$$
H | 0 \rangle = \frac {1}{\sqrt {2}} \left[ \begin{array}{c c} 1 & 1 \\ 1 & - 1 \end{array} \right] \binom{1}{0} = \frac {1}{\sqrt {2}} \binom{1}{1} = \frac {1}{\sqrt {2}} | 0 \rangle + \frac {1}{\sqrt {2}} | 1 \rangle .
$$

Note that states |0〉 and |1〉 both have probability $\begin{array} { r } { | \frac { 1 } { \sqrt { 2 } } | ^ { 2 } = \frac { 1 } { 2 } } \end{array}$ of being observed. For n qubits, we just use a tensor product to get an equal superposition.

In summary, a quantum computer algorithm takes the general form:

Prepare the initial state (usually taken to be |00···0〉).

Apply a sequence of unitary transforms.

Perform a measurement to read out a state.

## 1.1.4. Ensemble systems and density matrices

Another formalism for representing and working with quantum computing uses positive, semide<sup>fi</sup>nite, Hermitian matrices with trace 1 to represent states. These are called density matrices. Any density matrix, ρ, can be written as $\pmb { \rho } = \sum _ { i = 1 } ^ { n } \lambda _ { i } \nu _ { i } \pmb { \nu } _ { i } ^ { * }$ where $\stackrel { \cdot } { \lambda } _ { i } \geq 0 , ~ 1 = \sum _ { i = 1 } ^ { n } \mathrm { ~ } \lambda _ { i }$ and $1 = \sqrt { \nu _ { i } ^ { * } \nu _ { i } }$ . States ¼ ¼represented by vectors earlier, such as ψ, would be represented by the density matrix ψψ<sup>⁎</sup>. Density matrices represent mixed states that are viewed as a probabilistic mixture (the ${ \bf \lambda } _ { { \bf \lambda } _ { i } ^ { \prime } S } )$ of pure states, ${ \nu _ { i } } { \nu _ { i } } ^ { * }$ . This pays dividends when ensembles of states arise naturally in a problem, as is typical in mixedstrategy, game-theoretic models.

## 1.1.5. Miscellaneous issues

Wootters and Zurek [172] showed that it is impossible to copy a qubit in a superposition state (only pure states can be copied). This is called the “No Clone” theorem. Interestingly, Bennett et al. [8] showed how to “teleport” a qubit. In the process, the original qubit's state is destroyed but the recipient ends with a particle indistinguishable from the original.

Any 2 by 2 unitary matrix U can be represented by ${ \mathrm { U } } = e ^ { i a } { \ ' } e ^ { i b Z } e ^ { i c Y } { \ ' } e ^ { i d Z }$ for appropriate choices of real-valued a, b, c and d. This is known as the Z–Y decomposition or Cartan decomposition. The matrix exponential notation means the following. If x is a real number and A is a matrix such that $\pmb { A } ^ { \dag } \pmb { A } { = } \pmb { A } \pmb { A } ^ { \dag } { = } I$ . Then $e ^ { i x \mathbf { A } } { = } \cos ( x ) I { + } i$ sin (x)A. Y and Z satisfy the requirement $( \mathrm { i } . \mathrm { e } . , \mathbf { Y } ^ { \dagger } \mathbf { Y } = \mathbf { Y } \mathbf { Y } ^ { \dagger } = I$ and $\mathbf { Z } ^ { \dagger } \mathbf { Z } = \mathbf { Z } \mathbf { Z } ^ { \dagger } = I )$ , so for example, $e ^ { i d \bar { \mathbf { Z } } } { = } \cos ( d ) I { + } i$ sin(d)Z.

## 1.2. Quantum games

It is not hard to imagine settings where quantum games may be the natural game-theoretic choice because the phenomena are taking place at microscopic scales where the laws of quantum mechanics reign. For example, evolutionary biologists study the interaction of competition at the gene level. Dawkin's Sel<sup>fi</sup>sh Gene [29] comes to mind. Similar arguments have been made about protein interactions and protein folding [68]. In another setting, information communication with possible eavesdroppers can be viewed as a game and if the communication medium employs quantum components, as many do, quantum games are a natural framework. Even fairness can be guaranteed in remote gambling [69].

Along these lines, if classic games are played on a quantum computer or played by a quantum computer, the games can become quantum games. In [36] the Prisoner's Dilemma is actually played on an NMR quantum computer and Zhuang et al. [177] discuss how a quantum gambling machine, supporting a class of games, could be built using optical elements. Chen et al. actually do experimental studies with human players playing quantum games (see [17,18]). In the prisoner's dilemma game, humans did better in the quantum game than they do in a classic game.

This view quickly leads one to ask what happens when we replace other classical components in games, such as probabilities, with quantum counterparts or if there are parallels between classical systems and quantum systems? For example, Demski et al. [30] <sup>fi</sup>nd interesting parallels between accounting information systems and quantum systems in areas such as measurement (a key task in Accounting) and interactions with the environment. Iqbal [90] argues situations akin to this are worthwhile since there is a basic relationship between quantum algorithms and quantum games and that the study of quantum games may lead to new quantum algorithms.

Perhaps less tangible is Witte's [170] view that imagines quantum games as classical games played by quantum players. He argues that a human player plays virtual games in his mind before choosing a strategy. Since these are never actually played, they are reminiscent of the “many worlds” view of quantum mechanics [79] and thus lead to considering the game as a quantum game. Alternatively, if our brain functions are described by quantum mechanisms as viewed by Penrose [139], then quantum games may be a natural choice for modeling games.

More concretely, Grib et al. [72,73] look at macroscopic games where the rules of the game lead to a non-distributivity property that not only prevents the usual use of probability calculation in mixed strategies but yields a system where Hilbert Space amplitudes capture the appropriate characteristics. That is, macroscopic games can be described by quantum formalisms.

Conversely, Levine [116] argues that quantum games offer nothing new. He claims quantum entanglement gives features similar to correlated equilibrium and phenomena like cheaptalk equilibrium (where players can get advice). This view is contested. Dahl and Landsburg [28] show that quantum equilibrium with entanglement is not the same as correlated equilibrium in classical games. Eisert et al. [48] also give counterexamples. Lee and Johnson [109] show that whatever a quantum game can do, so can some more complicated classic game but the quantum game is more ef<sup>fi</sup>cient and may be the appropriate model for microscopic games.

In Section 2 we introduce and discuss the details of two simple quantum games. In Section 3 we give a survey of over 100 recent papers in this area, including ones in Accounting,

Finance and Economics. Section 4 provides some future directions for research.

## 2. Quantum game framework

In this section, we present the basic ideas of quantum games using two speci<sup>fi</sup>c examples discussed in the literature. These demonstrate how unique features of quantum mechanics, such as superposition and entanglement, can bring new aspects to classical games.

## 2.1. Quantum game basics

We start by recalling some notation from classic games (e.g., [136]). Assume there are n players with strategy spaces $S _ { i } , \ i { = } 1 , . . . , n$ and payoff functions $u _ { i } ( s _ { 1 } , . . . , s _ { n } ) , \ i = 1 , . . . , n$ where $s _ { i } \in S _ { i } .$ . Then a game can be denoted by G(n, S, u) where $S { = } S _ { 1 } \times \ldots \times S _ { n }$ and $u = u _ { 1 } \times \ldots \times u _ { n } .$ This is the normal-form representation of a game commonly used in static games. For dynamic games, extensive-form representations are used to include the timing of moves by each player, the possible strategies for each player at each move; what each player knows at each of his/her opportunity to move, etc. Classic games implicitly assume an information exchange mechanism to facilitate game implementation. For example, in the classic prisoners' dilemma game, the judge explains the game rules to the two prisoners, collects each prisoner's decision and then calculates the corresponding payoffs.

Quantum games explicitly depict the processes of information exchanges among players and payoff realization. Instead of a triple, a more general form is used to describe a quantum game (based on [47,113]). We denote a quantum game by $G \{ n , \Theta ( \mathbb { H } ) , \rho , S , u \}$ where n is the number of players, is the <sup>f gð Þ</sup>two dimensional Hilbert space, Θ H is the game's state space, $\scriptstyle \rho \in \Theta ( \mathbb { H } )$ is the starting state, $S { = } S _ { 1 } \times \ldots \times S _ { n }$ is the strategy space and $\boldsymbol { u } = u _ { 1 } \times \ldots \times u _ { n }$ is the utility function with $u _ { i } : \Theta ( \mathbb { H } )$ YR for <sup>ð Þ</sup>player i. In quantum games, the state of the game can be represented by a qubit or tensor products of multiple qubits. A referee (also called a judge or arbiter) serves as the coordinator of the game. As shown in the following <sup>fi</sup>gures, at the game's beginning, the referee may alter the starting state using an optional transform U to change the default starting space $\scriptstyle \rho \in \Theta ( \mathbb { H } )$ (which is typically the zero pure state) to a desired <sup>ð Þ</sup>state such as an entanglement of pure states. Then individual players move strategically. In other words, player i chooses $s _ { i } { \in } S _ { i }$ and all the $s _ { i } ^ { \prime } s$ are quantum operations which usually can be represented by unitary transformations U 's. For example, in a simple two-person game, unitary transformations $\mathbf { U } _ { 1 }$ and U are applied either simultaneously $( \mathrm { e . g . }$ , in a static game as in Fig. 1) or sequentially (e.g., in a dynamic game as in Fig. 2) to the game state. After the players move, the referee applies the inverse transform $\mathbf { U } ^ { \dagger }$ to undo the earlier application of U and takes the <sup>fi</sup>nal measurement to reveal the <sup>fi</sup>nal state of the game. Based on the observed <sup>fi</sup>nal state the referee calculates the payoffs to all players according to each player's $\boldsymbol { u } _ { i } ^ { \prime } \boldsymbol { s }$

## 2.2. Example one: PQ penny flip

To illustrate these notions, we start with Meyer's PQ penny <sup>fl</sup>ip game [127] which is recognized as the <sup>fi</sup>rst quantized game. This two-player game pitting player Q against player P offers interesting nuances over its classic counterpart. There are four steps in the classic version: a penny is placed headsup in a box by the referee; Q either <sup>fl</sup>ips the penny over (F) or not (N); then P either <sup>fl</sup>ips the penny over (F) or not (N); and then Q takes the <sup>fi</sup>nal move either <sup>fl</sup>ipping the penny over (F) or not (N). Note that both P and Q don't know each other's move. At the end, if the coin ends heads-down, then P wins with payoff +1 and Q loses with payoff −1. Otherwise, Q gets +1 and P gets −1. The classic penny <sup>fl</sup>ip game can be summarized in the following payoff matrix.

![](/api/attachments/XVJFKWCB/fulltext/images/db3af51bfa11adf69c967adbf9fb5a49209c0a12300b68e0967e264ab28ec6da.jpg)  
Fig. 1. Static quantum games.

![](/api/attachments/XVJFKWCB/fulltext/images/2eb99ac5c65093effc07dac5db875c5116f1d26184752918a8fb51a943c62c4a.jpg)  
Fig. 2. Dynamic quantum games.

<table><tr><td>Q</td><td>NN</td><td>NF</td><td>FN</td><td>FF</td></tr><tr><td>P:N</td><td>(-1,+1)</td><td>(+1,-1)</td><td>(+1,-1)</td><td>(-1,+1)</td></tr><tr><td>P:F</td><td>(+1,-1)</td><td>(-1,+1)</td><td>(-1,+1)</td><td>(+1,-1)</td></tr></table>

This is a dynamic, two-person zero-sum game and has no pure-strategy Nash equilibrium.

Now we turn to a simple quantum version of this game in which we allow player Q to adopt quantum strategies and restrict playerP to classic strategies. We use |0〉 to represent heads and |1〉 to represent tails. Then the state of the game can be represented by a qubit $\scriptstyle { \psi = \alpha | 0 \rangle + \beta | 1 \rangle }$ 〉. The initial state of the game is $\rho { = } | 0 \rangle$ Here the U as shown in Fig.1 is just the identity transform. That is, the referee leaves the initial state as is. Fig. 3 shows the quantum version of this game. The two classic moves — <sup>fl</sup>ip and not <sup>fl</sup>ip can be represented by unitary transforms X and I, respectively. As shown in Fig. 3, P can only play either X or I while Q may choose any unitary transform (we show the Hadamard transform). Thus, the game is speci<sup>fi</sup>ed by $G \{ n = 2 , \Theta ( \mathbb { H } ) = \mathbb { H } , \rho = | 0 \rangle , S _ { 1 } \times S _ { 2 } , u \}$ where $S _ { 1 } = \{ I , X \} ,$ <sup>f g¼ ð Þ ¼ ¼ j i </sup>, S is the set of all unitary matrices, and u gives the payoffs discussed above.

Consider the case where Q plays H (the Hadamard matrix) twice. After Q's <sup>fi</sup>rst move, the state of the game is ${ \bf H } | 0 \rangle =$ $\textstyle { \frac { 1 } { \sqrt { 2 } } } ( | 0 \rangle + | 1 \rangle )$ <sup>j i ¼</sup>. By playing H, Q puts the system in a superposition <sup>ð Þj i þ j i</sup>(i.e., <sup>fi</sup>guratively, the coin stands on its side). As a result, no matter what P chooses, whether X or I, the state of the game remains the same. Then Q chooses H again giving a <sup>fi</sup>nal result of |0〉. In other words, Q always wins! The quantization of Q's strategy allows him to present a superimposed state that can't be altered by P and thus guarantees himself a win.

Now let us examine the classic mixed strategies in this game and the quantum counterpart. Standard game theory results of two-person zero-sum games tell us that the classic PQ penny <sup>fl</sup>ip game has a mixed-strategy Nash equilibrium. It can be easily shown that the mixed-strategy Nash equilibrium has player P choose F or N with equal probability 0.5 and player Q chooses among his four possible strategies (NN, NF, FN, or FF) with equal probability, 0.25. As a result, both players get zero expected payoffs. For the quantum version, we still restrict P to classic strategies but now consider mixed strategies as shown in Fig. 4. Let P's mixed-strategy be <sup>fl</sup>ip with probability p and not <sup>fl</sup>ip with probability $1 - p .$ Once again we allow Q to employ a quantum move. Following Meyers [127], let his transform be given by unitary matrices with the form $\mathbf { U } _ { Q 1 } = \left\lceil \begin{array} { c c } { a } & { b ^ { * } } \\ { b } & { - a ^ { * } } \end{array} \right\rceil$ where $a a ^ { * } { + } b b ^ { * } { = } 1$ . Since now the game involves mixed states, we use a density matrix (as discussed in Section 1.1) to represent the state of the game.

In the form of a density matrix, the initial state is $\rho _ { 0 } =$ $| 0 \rangle \langle 0 | = \left\lceil \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right\rceil$ . The state after Q's move is $\rho _ { 1 } = \mathbf { U } _ { 2 1 } \pmb { \rho } _ { 0 } \mathbf { U } _ { Q 1 } ^ { \tilde { \prime } } =$ $\left[ \begin{array} { l l } { a a ^ { * } } & { a b ^ { * } } \\ { b a ^ { * } } & { b b ^ { * } } \end{array} \right]$ . After P's move we have

$$
\begin{array}{l} \boldsymbol {\rho} _ {2} = p X \boldsymbol {\rho} _ {1} X ^ {\dagger} + (1 - p) I \boldsymbol {\rho} _ {1} I ^ {\dagger} \\ \qquad = \left[ \begin{array}{c c} p b b ^ {*} + (1 - p) a a ^ {*} & p b a ^ {*} + (1 - p) a b ^ {*} \\ p a b ^ {*} + (1 - p) b a ^ {*} & p a a ^ {*} + (1 - p) b b ^ {*} \end{array} \right]. \end{array}
$$

Consider what happens if the game ends here. Recall that the diagonal elements of a density matrix correspond to the probabilities of pure states. The probabilities of |0〉 and |1〉 are $\hat { p } b b ^ { * } + ( 1 - p ) a a ^ { * }$ and $p a a ^ { * } { + } ( 1 { - } \widehat { p } ) b b ^ { * }$ respectively. On the one hand, given Q's strategy, P's best response is to choose p=1 if $a a ^ { * } { > } b \bar { b } ^ { * } ; p { = } 0 \mathrm { i f } a a ^ { * } { < } b b ^ { * } ;$ any $p \in [ 0 , 1 ]$ if $a a ^ { * } { = } b b ^ { * }$ On the other hand, player Q would choose $b b ^ { * } = 1 { \mathrm { ~ i f ~ } } p { > } 0 . 5 ; b b ^ { * } = 0$ if $p { < } 0 . 5 ;$ and any a,b if $p { = } 0 . 5 .$ . Therefore the (classic mixedstrategy, quantum strategy) equilibrium is p=0.5 and $a a ^ { * } =$ $b b ^ { * } { = } 0 . 5$ with both players getting zero payoff. This result is the same as the classic mixed-strategy for both players. This two-step game suggests that a player with an optimal quantum strategy has an expected payoff at least as great as his expected payoff with an optimal mixed-strategy.

![](/api/attachments/XVJFKWCB/fulltext/images/d5d8fee39c2c480ca29932b775918a4c009f01b5e8ca8f8ea0f824c6be75f7f3.jpg)  
Fig. 3. PQ penny <sup>fl</sup>ip (pure-strategy).

![](/api/attachments/XVJFKWCB/fulltext/images/aaff1ef48d0c55ed9468c278929b3f795d37f18bf639a2f0264a34f5bda0e020.jpg)  
Fig. 4. PQ penny <sup>fl</sup>ip (mixed-strategy).

Now we continue the third step in the PQ penny <sup>fl</sup>ip game — Q has a second chance to <sup>fl</sup>ip. Suppose Q chooses a strategy with $\begin{array} { r } { a = b = \frac { 1 } { \sqrt { 2 } } . } \end{array}$ Then $\begin{array} { r } { { \bf U } _ { Q 1 } = { \bf \bar { U } } _ { Q 2 } = \frac { 1 } { \sqrt { 2 } } \left[ \begin{array} { c c } { 1 } & { 1 } \\ { 1 } & { - 1 } \end{array} \right] } \end{array}$ (the Hadamard matrix again) and

$$
\begin{array}{l} \rho_ {1} = \mathbf {U} _ {Q 1} \rho_ {0} \mathbf {U} _ {Q 1} ^ {\dagger} = \frac {1}{2} \left[ \begin{array}{c c} 1 & 1 \\ 1 & 1 \end{array} \right], \quad \rho_ {2} = p X \rho_ {1} X ^ {\dagger} + (1 - p) I \rho_ {1} I ^ {\dagger} \\ = \frac {1}{2} \left[ \begin{array}{c c} 1 & 1 \\ 1 & 1 \end{array} \right], \quad \rho_ {3} = \mathbf {U} _ {Q 2} \rho_ {2} \mathbf {U} _ {Q 2} ^ {\dagger} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \end{array} \right] \end{array}
$$

By doing so, Q wins with probability 1. Thus Q can always win by playing a Hadamard matrix in both of his turns no matter whether P uses a pure or mixed-strategy. Meyer also proved that a two-person zero-sum game may not have a (pure-strategy quantum, pure-strategy quantum) equilibrium but always has a (mixed-strategy quantum, mixed-strategy quantum) equilibrium.

## 2.3. Example two: prisoners' dilemma

The penny <sup>fl</sup>ip game demonstrated one unique outcome of quantum phenomena — superposition. Eisert et al. [48] <sup>fi</sup>rst looked at a quantized prisoner's dilemma game showing how another unique quantum feature – entanglement – can affect the outcome of the game. In the classic game of prisoners dilemma, each player has two choices, either cooperate (C) or defect (D). The corresponding payoff is:

<table><tr><td></td><td>Player 2: C</td><td>Player 2: D</td></tr><tr><td>Player 1: C</td><td>(3,3)</td><td>(0,5)</td></tr><tr><td>Player 1: D</td><td>(5,0)</td><td>(1,1)</td></tr></table>

The resulting Nash equilibrium is (D, D) which is Pareto suboptimal because both players would be better off choosing (C, C).

Now we consider a quantization of this game given by Eisert [48] as shown below in Fig. 5.

In this game, let |0〉 denote cooperate and |1〉 denote defect The state of the game is determined by the players' choices and so the state of the game can be represented as the combination of the two players' choices. The initial state is |00〉 representing the case where both players cooperate. The initial U transform produces an entangled state, $U | 0 0 \rangle = ( | 0 0 \rangle + i | 1 1 \rangle ) /$ ${ \sqrt { 2 } } .$ . Then the players may choose one of the classic moves — I (maintains “cooperate”) or X (switch to defect) or a quantum move restricted to unitary matrix Z. Thus, the game is $G \{ n = 2 , \Theta ( \mathbb { H } ) = \mathbb { H } ^ { 2 } , \pmb { \rho } = | 0 0 \rangle , S _ { 1 } \times S _ { 2 } , u \}$ where $S _ { 1 } = S _ { 2 } = \{ I , \ X ,$ Z} and u gives the normal payoffs. The nine possible results are:

<table><tr><td></td><td>Player 2: I</td><td>Player 2: X</td><td>Player 2: Z</td></tr><tr><td>Player 1: I</td><td> $(I \otimes I)U|00\rangle$  $=\frac{1}{\sqrt{2}}(|00\rangle + i|11\rangle)$ </td><td> $(I \otimes X)U|00\rangle$  $=\frac{1}{\sqrt{2}}(|01\rangle + i|10\rangle)$ </td><td> $(I \otimes Z)U|00\rangle$  $=\frac{1}{\sqrt{2}}(|00\rangle - i|11\rangle)$ </td></tr><tr><td>Player 1: X</td><td> $(X \otimes I)U|00\rangle$  $=\frac{1}{\sqrt{2}}(|10\rangle + i|01\rangle)$ </td><td> $(X \otimes X)U|00\rangle$  $=\frac{1}{\sqrt{2}}(|11\rangle + i|00\rangle)$ </td><td> $(X \otimes Z)U|00\rangle$  $=\frac{1}{\sqrt{2}}(|10\rangle - i|01\rangle)$ </td></tr><tr><td>Player 1: Z</td><td> $(Z \otimes I)U|00\rangle$  $=\frac{1}{\sqrt{2}}(|00\rangle - i|11\rangle)$ </td><td> $(Z \otimes X)U|00\rangle$  $=\frac{1}{\sqrt{2}}(|01\rangle - i|10\rangle)$ </td><td> $(Z \otimes Z)U|00\rangle$  $=\frac{1}{\sqrt{2}}(|00\rangle + i|11\rangle)$ </td></tr></table>

After applying $\mathbf { U } ^ { \dagger }$ we get:

<table><tr><td></td><td>Player 2: I</td><td>Player 2: X</td><td>Player 2: Z</td></tr><tr><td>Player 1: I</td><td> $\mathbf{U}^{\dagger}(I \otimes I)\mathbf{U}|00\rangle$ = |00⟩</td><td> $\mathbf{U}^{\dagger}(I \otimes X)\mathbf{U}|00\rangle$ = |01⟩</td><td> $\mathbf{U}^{\dagger}(I \otimes \mathbf{Z})\mathbf{U}|00\rangle$ =-i|11⟩</td></tr><tr><td>Player 1: X</td><td> $\mathbf{U}^{\dagger}(X \otimes I)\mathbf{U}|00\rangle$ = |10⟩</td><td> $\mathbf{U}^{\dagger}(X \otimes X)\mathbf{U}|00\rangle$ = |11⟩</td><td> $\mathbf{U}^{\dagger}(X \otimes \mathbf{Z})\mathbf{U}|00\rangle$ =-i|01⟩</td></tr><tr><td>Player 1: Z</td><td> $\mathbf{U}^{\dagger}(\mathbf{Z} \otimes I)\mathbf{U}|00\rangle$ =-i|11⟩</td><td> $\mathbf{U}^{\dagger}(\mathbf{Z} \otimes X)\mathbf{U}|00\rangle$ =-i|10⟩</td><td> $(\mathbf{Z} \otimes \mathbf{Z})\mathbf{U}|00\rangle$ = |00⟩</td></tr></table>

![](/api/attachments/XVJFKWCB/fulltext/images/c83175fb46c3bba0edcd3ba5050db1f03b96f60ae90c1374c9bff38c4bc0bf86.jpg)  
Fig. 5. Prisoners' dilemma.

The <sup>fi</sup>nal measurement gives us the following payoffs:

<table><tr><td></td><td>Player 2: I</td><td>Player 2: X</td><td>Player 2: Z</td></tr><tr><td>Player 1: I</td><td>(3,3)</td><td>(0,5)</td><td>(1,1)</td></tr><tr><td>Player 1: X</td><td>(5,0)</td><td>(1,1)</td><td>(0,5)</td></tr><tr><td>Player 1: Z</td><td>(1,1)</td><td>(5,0)</td><td>(3,3)</td></tr></table>

In this quantized game, (Z, Z) is not only the unique Nash equilibrium but is also Pareto optimal. The quantum generalization allows players to escape the usual prisoner's dilemma.

A more general class of strategies is considered in [48] where

$$
\begin{array}{l} \mathbf {U} _ {j} = \left[ \begin{array}{c c} e ^ {i \phi} \cos (\theta / 2) & \sin (\theta / 2) \\ - \sin (\theta / 2) & e ^ {- i \phi} \cos (\theta / 2) \end{array} \right] \\ \text { and } \\ \mathbf {U} = \left[ \begin{array}{c c c c c} \cos (\gamma / 2) & 0 & 0 & i s i n (\gamma / 2) \\ 0 & \cos (\gamma / 2) & - i s i n (\gamma / 2) & 0 \\ 0 & - i s i n (\gamma / 2) & \cos (\gamma / 2) & 0 \\ i s i n (\gamma / 2) & 0 & 0 & \cos (\gamma / 2) \end{array} \right] \end{array}
$$

with $\gamma { \in } [ 0 , \pi / 2 ]$ . Parameter γ measures the degree of entanglement with γ=0 representing zero entanglement making the game separable (i.e., U is I) and $\gamma = \pi / 2$ represents maximum entanglement. Eisert [48] showed that separable games do not display any feature that goes beyond the classic game. The game with maximum entanglement has a unique equilibrium.

## 2.4. Generalizations

We introduce one of many extensions proposed by researchers — generalizing the strategy spaces.

## 2.4.1. A general form of PQ penny flip

We <sup>fi</sup>rst reexamine the PQ penny <sup>fl</sup>ip game where we allow Q to take general quantum moves using the Z–Y decomposition discussed in Section 1.1. Let

$$
\begin{array}{l} \mathbf {U} _ {Q 1} = e ^ {i a} e ^ {i b \mathsf {Z}} e ^ {i c \mathsf {Y}} e ^ {i d \mathsf {Z}} = e ^ {i a} \left[ \begin{array}{c c} e ^ {i (b + d)} \cos (c) & e ^ {i (b - d)} \sin (c) \\ - e ^ {i (- b + d)} \sin (c) & e ^ {- i (b + d)} \cos (c) \end{array} \right] \\ \mathbf {U} _ {Q 2} = e ^ {i \alpha} e ^ {i \beta \mathsf {Z}} e ^ {i \gamma \mathsf {Y}} e ^ {i \delta \mathsf {Z}} = e ^ {i \alpha} \left[ \begin{array}{c c} e ^ {i (\beta + \delta)} \cos (\gamma) & e ^ {i (\beta - \delta)} \sin (\gamma) \\ - e ^ {i (- \beta + \delta)} \sin (\gamma) & e ^ {- i (\beta + \delta)} \cos (\gamma) \end{array} \right] \end{array}
$$

where a, b, c, d, α, β, γ and δ are all real-valued. The state of the game in the three steps can be represented by the corresponding density matrix as follows:

$$
\begin{array}{l} \boldsymbol {\rho} _ {0} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \end{array} \right], \quad \boldsymbol {\rho} _ {1} = \mathbf {U} _ {Q 1} \boldsymbol {\rho} _ {0} \mathbf {U} _ {Q 1} ^ {\dagger}, \quad \boldsymbol {\rho} _ {2} = p X \boldsymbol {\rho} _ {1} X ^ {\dagger} + (1 - p) I \boldsymbol {\rho} _ {1} I ^ {\dagger} \\ \boldsymbol {\rho} _ {3} = p \mathbf {U} _ {Q 2} X \mathbf {U} _ {Q 1} \boldsymbol {\rho} _ {0} \mathbf {U} _ {Q 1} ^ {\dagger} X ^ {\dagger} \mathbf {U} _ {Q 2} ^ {\dagger} + (1 - p) \mathbf {U} _ {Q 2} \mathbf {U} _ {Q 1} \boldsymbol {\rho} _ {0} \mathbf {U} _ {Q 1} ^ {\dagger} \mathbf {U} _ {Q 2} ^ {\dagger} \\ = \mathbf {U} _ {Q 2} \mathbf {U} _ {Q 1} \boldsymbol {\rho} _ {0} \mathbf {U} _ {Q 1} ^ {\dagger} \mathbf {U} _ {Q 2} ^ {\dagger} + p \Big (\mathbf {U} _ {Q 2} X \mathbf {U} _ {Q 1} \boldsymbol {\rho} _ {0} \mathbf {U} _ {Q 1} ^ {\dagger} X ^ {\dagger} \mathbf {U} _ {Q 2} ^ {\dagger} - \mathbf {U} _ {Q 2} \mathbf {U} _ {Q 1} \boldsymbol {\rho} _ {0} \mathbf {U} _ {Q 1} ^ {\dagger} \mathbf {U} _ {Q 2} ^ {\dagger} \Big) \end{array}
$$

Since the probability of heads is $( \pmb { \rho } _ { 3 } ) _ { 1 , 1 }$ and the probability of tails is $( \pmb { \rho } _ { 3 } ) _ { 2 , 2 } ,$ , the expected payoff for $P { \mathrm { ~ i s ~ E V } } ( P ) = ( \mathbf { \rho } _ { \mathbf { 3 } } ) _ { 2 , 2 } -$ $( \pmb { \rho } _ { 3 } ) _ { 1 , 1 }$ and the expected payoff for $\begin{array} { r } { Q \mathrm { i } s \operatorname { E V } ( Q ) = ( \pmb { \rho } _ { 3 } ) _ { 1 , 1 } - ( \pmb { \rho } _ { 3 } ) _ { 2 , 2 } . } \end{array}$ Now we derive the conditions for Q to win and look for conditions giving $\mathrm { E V } ( P ) = - 1$ and $\mathrm { E V } ( Q ) = 1$ . For this result to hold requires both $\begin{array} { r } { ( \mathbf { U } _ { Q 2 } X \mathbf { U } _ { Q 1 } \mathbf { \rho } _ { 0 } \mathbf { U } _ { Q 1 } \mathbf { \dot { X } } ^ { \dagger } \mathbf { U } _ { Q 2 } \mathbf { \dot { - } } \mathbf { U } _ { Q 2 } \mathbf { U } _ { Q 1 } \mathbf { \rho } _ { 0 } \mathbf { U } _ { Q 1 } \mathbf { \dot { U } } _ { Q 2 } ) _ { 1 , 1 } = 0 } \end{array}$ and $( \mathbf { U } _ { Q 2 } X \mathbf { U } _ { Q 1 } \mathbf { \rho } _ { 0 } \mathbf { U } _ { Q 1 } \mathbf { \overset { . } { X } ^ { \dagger } } \mathbf { \overbrace { U } } _ { Q 2 } ^ { \dagger } \mathbf { - U } _ { Q 2 } \mathbf { U } _ { Q 1 } \mathbf { \rho } _ { 0 } \mathbf { U } _ { Q 1 } \mathbf { \overset { . } { U } } _ { Q 2 } ) _ { 2 , 2 } = 0$ for all p. Substituting U and U gives cos(2b)sin(2c)sin(2γ)cos(2δ)= −1. Notice the winning strategy for Q discussed above of $\mathbf { U } _ { Q 1 } = \mathbf { U } _ { Q 2 } = \mathbf { H }$ is a special case of this condition (e.g., a = $b = \alpha = \beta = \pi / 2 , \ c = \gamma = \pi / 4$ , and $d = \delta = \pi )$ . However, other unitary matrices will also work. For example,

$$
\begin{array}{l} \mathbf {U} _ {Q 1} = \frac {1}{\sqrt {2}} \left[ \begin{array}{c c} e ^ {- 2 i \pi / 3} & e ^ {2 i \pi / 3} \\ - e ^ {- 2 i \pi / 3} & e ^ {2 i \pi / 3} \end{array} \right] = \frac {1}{\sqrt {2}} \left[ \begin{array}{c c} - (- 1) ^ {1 / 3} & (- 1) ^ {2 / 3} \\ (- 1) ^ {1 / 3} & (- 1) ^ {2 / 3} \end{array} \right], \\ \mathbf {U} _ {Q 2} = \frac {i}{\sqrt {2}} \left[ \begin{array}{c c} - 1 & 1 \\ - 1 & - 1 \end{array} \right] \end{array}
$$

with $a = \pi , b = 0 , c = \gamma = \pi / 4 , d = \pi / 3 , \alpha = \beta = \delta = \pi / 2 .$

Now we constrain the available quantum strategies for Q to derive conditions for the classic results of this game, $\mathrm { i . e . , ~ E V } ( P ) { = } \mathrm { E V } ( Q ) { = } 0 .$ . Substituting the previous results gives EV P 1−2p cos 2c cos 2γ sin 2b sin 2c sin 2γ sin 2δ cos 2b sin 2c sin 2γ cos 2δ :

<sup>ð Þ ð Þ ð Þ ð Þ</sup>The maximal payoff P can achieve by selecting p as cos 2c <sup>j ð</sup>cos 2γ sin 2b sin 2c sin 2γ sin 2δ cos 2b sin 2c sin 2γ <sup>ð Þ</sup>cos 2δ :

<sup>ð Þ</sup>Therefore the game will have classic results when cos 2c cos 2γ sin 2b sin 2c sin 2γ sin 2δ cos 2b sin 2c sin 2γ cos $( 2 \delta ) = 0 .$

<sup>ð Þ ¼</sup>Can P actually win? The following conditions provide an af<sup>fi</sup>rmative result for this case: cos 2c cos 2γ sin 2b sin 2c sin $( 2 \gamma ) s i n ( 2 \delta ) | + c o s ( 2 b ) s i n ( 2 c ) s i n ( 2 \gamma ) c o s ( 2 \delta ) = 1$

<sup>ð Þ ð Þj þ ð Þ ð Þ ð Þ ð Þ ¼</sup>Thus, the strategy space can be partitioned into four areas corresponding to the three special cases — P wins, Q wins, a tie which is the classic result - and all other cases. We can see that restrictions on Q's strategy space determine the outcome of the generalized PQ penny <sup>fl</sup>ip game: Depending on Q's strategy space, he can win, tie or lose.

## 2.4.2. A general form of prisoner's dilemma

For a general form of prisoner's dilemma strategies let strategies be given by

$$
\mathbf {U} _ {1} = e ^ {i a} e ^ {i b \mathbf {Z}} e ^ {i c \mathbf {Y}} e ^ {i d \mathbf {Z}} = e ^ {i a} \left[ \begin{array}{c c} e ^ {i (b + d)} \cos (c) & e ^ {i (b - d)} \sin (c) \\ - e ^ {i (- b + d)} \sin (c) & e ^ {- i (b + d)} \cos (c) \end{array} \right]
$$

$$
\mathbf {U} _ {2} = e ^ {i \alpha} e ^ {i \beta \mathbf {Z}} e ^ {i \gamma \mathbf {Y}} e ^ {i \delta \mathbf {Z}} = e ^ {i \alpha} \left[ \begin{array}{c c} e ^ {i (\beta + \delta)} c o s (\gamma) & e ^ {i (\beta - \delta)} s i n (\gamma) \\ - e ^ {i (- \beta + \delta)} s i n (\gamma) & e ^ {- i (\beta + \delta)} c o s (\gamma) \end{array} \right].
$$

If there is no preprocessing transform U, then the <sup>fi</sup>nal state of the game is

$$
\mathbf {U} _ {1} \otimes \mathbf {U} _ {2} | 0 0 \rangle = \left[ \begin{array}{c} e ^ {i (a + b + d + \alpha + \beta + \delta)} c o s (c) c o s (\gamma) \\ - e ^ {i (a + b + d + \alpha - \beta + \delta)} c o s (c) s i n (\gamma) \\ - e ^ {i (a - b + d + \alpha + \beta + \delta)} s i n (c) c o s (\gamma) \\ e ^ {i (a - b + d + \alpha - \beta + \delta)} s i n (c) s i n (\gamma) \end{array} \right].
$$

The resulting expected payoff for players 1 and 2 are

$$
\begin{array}{l} \text { EV } _ {1} = 3 c o s ^ {2} (c) c o s ^ {2} (\gamma) + 0 c o s ^ {2} (c) s i n ^ {2} (\gamma) + 5 s i n ^ {2} (c) c o s ^ {2} (\gamma) \\ \quad + 1 s i n ^ {2} (c) s i n ^ {2} (\gamma) \\ \text { EV } _ {2} = 3 c o s ^ {2} (c) c o s ^ {2} (\gamma) + 5 c o s ^ {2} (c) s i n ^ {2} (\gamma) + 0 s i n ^ {2} (c) c o s ^ {2} (\gamma) \\ \quad + 1 s i n ^ {2} (c) s i n ^ {2} (\gamma). \end{array}
$$

Given γ, player 1's best response is to set $\sin ^ { 2 } ( c ) = 1 .$ . Given c, player 2's best response is to set sin $\begin{array} { r } { \mathbf { \nabla } ^ { 2 } ( \gamma ) = 1 . } \end{array}$ So the equilibrium would be $c = k \pi / 2$ and $\gamma = l \pi / 2$ where k and l are integers. This result corresponds to the Pareto suboptimal equilibrium of $( D , D )$ in the classic game. The prisoners cannot escape the dilemma without entanglement.

Now we consider the maximally entangled $\begin{array} { r } { \mathbf { U } = \frac { 1 } { \sqrt { 2 } } \left( I ^ { \otimes 2 } + i X ^ { \otimes 2 } \right) } \end{array}$ After the players' moves:

$$
\begin{array}{l} \left(\mathbf {U} _ {1} \otimes \mathbf {U} _ {2}\right) \mathbf {U} | 0 0 \rangle \\ = \frac {e ^ {i (a + \alpha)}}{\sqrt {2}} \left[ \begin{array}{l} e ^ {i (b + \beta)} \left[ e ^ {i (d + \delta)} \cos (c) \cos (\gamma) + i e ^ {- i (d + \delta)} \sin (c) \sin (\gamma) \right] \\ e ^ {i (b - \beta)} \left[ i e ^ {- i (d + \delta)} \sin (c) \cos (\gamma) - e ^ {i (d + \delta)} \cos (c) \sin (\gamma) \right] \\ e ^ {i (- b + \beta)} \left[ - e ^ {i (d + \delta)} \sin (c) \cos (\gamma) + i e ^ {- i (d + \delta)} \cos (c) \sin (\gamma) \right] \\ e ^ {i (- b - \beta)} \left[ i e ^ {- i (d + \delta)} \cos (c) \cos (\gamma) + e ^ {i (d + \delta)} \sin (c) \sin (\gamma) \right] \end{array} \right]. \end{array}
$$

After applying U<sup>†</sup> we get

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\mathbf{U}^{\dagger}(\mathbf{U}_{1}\otimes \mathbf{U}_{2})\mathbf{U}|00\rangle$ $= \left[ \begin{array}{l}(cos(a + \alpha) + isin(a + \alpha))(cos(c)cos(\gamma)cos(b + d + \beta +\delta) - sin(c)sin(\gamma)sin(b - d + \beta -\delta))\\ -(cos(a + \alpha) + isin(a + \alpha))(cos(c)sin(\gamma)cos(b + d - \beta +\delta) + sin(c)cos(\gamma)sin(b - d - \beta -\delta))\\ -(cos(a + \alpha) + isin(a + \alpha))(sin(c)cos(\gamma)cos(b - d - \beta -\delta) - cos(c)sin(\gamma)sin(b + d - \beta +\delta))\\ (cos(a + \alpha) + isin(a + \alpha))(sin(c)sin(\gamma)cos(b - d + \beta -\delta) + cos(c)cos(\gamma)sin(b + d + \beta +\delta)) \end{array} \right].$
</div>

There are four possible outcomes − |00〉, |01〉, |10〉, and |11 with probabilities u , $u _ { 0 1 } , \ u _ { 1 0 } ,$ and $u _ { 1 1 }$ respectively. The probabilities u , u , u , and $u _ { 1 1 }$ can be speci<sup>fi</sup>ed as

$$
\begin{array}{l} u _ {0 0} = (c o s (c) c o s (\gamma) c o s (b + d + \beta + \delta) - s i n (c) s i n (\gamma) s i n (b - d + \beta - \delta)) ^ {2} \\ u _ {0 1} = (c o s (c) s i n (\gamma) c o s (b + d - \beta + \delta) + s i n (c) c o s (\gamma) s i n (b - d - \beta - \delta)) ^ {2} \\ u _ {1 0} = (s i n (c) c o s (\gamma) c o s (b - d - \beta - \delta) - c o s (c) s i n (\gamma) s i n (b + d - \beta + \delta)) ^ {2} \\ u _ {1 1} = (s i n (c) s i n (\gamma) c o s (b - d + \beta - \delta) + c o s (c) c o s (\gamma) s i n (b + d + \beta + \delta)) ^ {2} \end{array}
$$

Given player 1's choices a, b, c, and d, player 2 can choose $\gamma = c , \beta = 3 \pi / 4 - b ,$ and $\delta \mathrm { = } \mathrm { - } d \mathrm { - } 3 \pi / 4$ to undo player 1's move which restores the initial state of the game |00〉. The corresponding undo matrix for player 2 is ${ \bf U } _ { \mathrm { u n d o } } =$ $e ^ { i \alpha } { \binom { e ^ { - i ( b + d ) } C O S ( c ) } { - e ^ { i ( - 3 \pi / 2 + b - d ) } S i n ( c ) } } ^ { - { i } ( { 3 \pi / 2 - b + d ) } S i n ( c ) }$ . So the best response for player 2 is to play $X \mathbf { U } _ { \mathrm { u n d o } }$ <sup>ð Þ</sup>, i.e., $\gamma { = } { - } c { - } \pi / 2 , \beta { = } b { - } 5 \pi / 4$ , and $\delta =$ $- d - \pi / 4 ,$ which results in the <sup>fi</sup>nal state of |01〉 with probability 1 and the highest possible payoff 5 for player 2. Similarly, player 1 will adopt the same strategy and results in the <sup>fi</sup>nal state of |10〉 with probability 1 and the highest possible payoff 5 for player 1. Therefore there is no pure-strategy equilibrium.

In the next sectionwe present a literature review of quantum games. Other summaries, expositions and reviews are available targeting different areas of interest and covering different publication time-frames (e.g., see [53,54,56,57,71,90,109,130, $^ { 1 4 5 , 1 4 7 ] ) }$ .

## 3. Literature review of quantum game theory

Although Meyer [127] is usually cited as originating quantum game theory, Piotrowski and Sladowski [147] claim Vaidman [164] was the <sup>fi</sup>rst to use the term “game” in the context of quantum phenomena and that Wiesner [169] deserves credit for considering quantum money in 1983 giving the <sup>fi</sup>rst glimmer of market-based quantum game notions.

We start our literature review by collecting in Table 1 the various quantum game counterparts to classic games studied by researchers. With each game type, we give citations, a description of the game and discuss what aspect is uncovered in the quantum game versions. (We use NE for Nash Equilibrium in the singular or plural.)

As one can see, many types of games have been studied, including most of the classic cases typically encountered in game theory courses. Most of the initial results showed that quantum games offered ways around classic dilemmas. However, as researcher's focused more carefully, some of these results vanished. For example, in the prisoner's dilemma, as shown in Section 2, only restricted strategy spaces resulted in the usual dilemma being removed. Once strategy spaces were allowed to be more general, this aspect disappeared.

Several avenues of research emerged. Many researchers focused on the representation of quantum games and various types of generalization therein. Others looked at additional aspects of quantum mechanics, like decoherence, and the role they play in quantum games. Still others looked at theoretical properties of quantum games, like Nash Equilibria, or at extensions such as into evolutionary games. Finally, a number of researchers opened new areas of quantum game applications especially in communication and econophysics applica tions. We briefly look at each of these areas

## 3.1. Generalizations

Many avenues of generalization have been explored. Table 1 shows generalizations from simple two-player static, noncooperative games to dynamic games, multiplayer games, cooperative games, etc.

As discussed in Section 2, some generalizations focused on expanding the strategy space from restricted sets of unitary matrices to more general collections of unitary transforms. Papers that fall in this category are [5,6,123,124]. Some researchers use vectors to represent player strategies instead of unitary transformations (e.g., [24,25,85,86]). Among these researchers, Ichikawa [86] uses Schmidt decomposition approaches and <sup>fi</sup>nds that eight phase structures exist for general symmetric games when varying correlation between players. A similar phase transition phenomenon is found in the minority game by Challet [13] and in the prisoner's dilemma game by Du [43]. Iqbal [100] looks at whether quantum games are the same as classic games. He compares them under two constraints, one where the classic and quantum game have the same set of strategies and the other with the same explicit payoffs, and claims that the quantum games are not reproducible with classic games.

Table 1 Quantum games

<table><tr><td>Game types</td><td>Game description</td><td>Contribution</td></tr><tr><td>Bar game [101]</td><td>A bar has 2-seats but all n players want to sit and they also want more people present.</td><td>In this multiplayer quantum game, a noisy demon that controls the input qubit's corruption reduces the value of the game.</td></tr><tr><td>Bargaining game [142]</td><td>The game is a model of interactive bargaining with a fixed resource amount. Two players get what they want if the sum of their demands is less than or equal to the fixed amount. Otherwise, they get nothing.</td><td>In a complex quantum bargaining game, the profit is in a superposition and market transaction is polarized.</td></tr><tr><td>Battle of the sexes [2,5,37,38,123,124,132]</td><td>Two players (husband and wife) choose to go to the theater or to a football game and have different preference, but they would benefit more if they pick the same option.</td><td>Infinite NE exist with the same payoff as does the classical game. In the game with a general strategy space, there is no equilibrium. The classical game can be reproduced from the quantum game without entanglement.</td></tr><tr><td>Byzantine agreement [55]</td><td>There are three players and one of them is the enemy. They use pair-wise channels to communicate and player A sends a bit to player B and C separately. Player C should find that his bit is the same as the bit player B tells him. However, this is false information since one of player A or B is cheating.</td><td>A quantum solution is found by using pair-wise quantum channels and entangled qudits. The game can be applied to cryptography.</td></tr><tr><td>Card game [34,71]</td><td>Player A puts three different cards in a blackbox. The first card has dots on both sides, the second card has circles, and the third card has a dot on one side and a circle on the other side. Player B picks one card from the box. If the card has the same pattern on both sides, player A wins. Otherwise, player B wins.</td><td>Without the help of entanglement, this unfair game becomes fair when the classical card game is quantized.</td></tr><tr><td>Chicken game [47,64,85,86]</td><td>Also known as the Hawk-Dove game, this is similar to the Battle of the Sexes except the players' payoffs are higher when they pick different strategies.</td><td>The usual dilemma can be removed if players use quantum strategies within a restricted strategy space.</td></tr><tr><td>Chinos game [77]</td><td>In each turn, every player guesses the total number of coins hidden in hands of a group of n players and the player whose guess is right wins. After m plays, the player whose total winning time is worst looses the game.</td><td>The partial quantum strategy is not stable while the classical strategy is. A full quantum analogy gives a winning strategy.</td></tr><tr><td>Cooperative game [26,28,88,96,100,102,105]</td><td>Groups of players make an agreement to coordinate their strategies.</td><td>In the three player case, conditions on the pure initial states are found that prevent coalition formation.</td></tr><tr><td>Guess the number game [71]</td><td>Player A picks any integer and lets player B guess the number. Player B wins if he can guess right within k tries.</td><td>Player B wins more often in the quantum game than in the classical game since she can put player A's oracle in superposition states. She uses Grover's database search algorithm [74] to search for the number.</td></tr><tr><td>Gun duel [60]</td><td>Two or more gunfighters shoot each other and the winner is the player who is still standing after the fight. With respect to the quantum analogy, players lay out their strategies which are not contingent on prior outcomes since a measurement isn't taken till the final round is over.</td><td>One round quantum duels are equivalent to the classical version, but not so with longer turns. Interference effects play a big role.</td></tr><tr><td>Minority game [3,7,13-15,18,23,49,50,62,63,146]</td><td>An odd number of players have two strategies. Players win if their strategy is in the minority group.</td><td>New NE arises when the number, n, of players is even. When n is odd, the quantum game is like the classical one with non-maximal entanglement.</td></tr><tr><td>Monty Hall problem [27,58,118]</td><td>Based on a TV game show, a contestant chooses one of three doors behind which there is a car or a goat. The host, Monty Hall, opens one of two doors that have not been chosen and asks whether the player wants to switch her choice. The problem in this game is whether the player should switch or not. She should switch since the probability of winning the game is 2/3 then.</td><td>The quantum game becomes a fair game between the contestant and host. If both play quantum strategies there is no NE in pure strategies but there is in mixed strategies which is the same as the classic game. With entanglement, one quantum player has an advantage over the other classic player. The classical game is the same as the quantum one with no entanglement of initial states.</td></tr><tr><td>Newcombs game [144]</td><td>In this game, there is an open box with $1000 and a closed box that has one million dollars or nothing. A human player can only pick the closed box or pick both boxes. The player always wins $1,000 more if he chooses to open two boxes. However, there is a predictor (Omega) who decides how much money was put in the closed box before the game starts and can predict the player's behavior. If he predicts the player will pick both boxes, he will put in the closed box. Otherwise one million dollars is put in.</td><td>This problem is quantized with alien Omega against the human player and the paradox is removed. In this game humans retain their free will but cannot profit from their decisions.</td></tr><tr><td>Parrondo's ([117]) game [59,78,112,115,128,138]</td><td>When played in an alternating order, two losing games become a winning game.</td><td>The quantum game can have a spatial state-dependent or historical-dependent version. The quantum game can remove the dependence on a modulo rule based on the current capital in classical game.</td></tr><tr><td>Penny flip [71,89,127]</td><td>Two players each have a coin. Simultaneously, they flip the coins to heads or tails secretly and then reveal it to each other. If the coins match, player A wins, otherwise player B wins. A special case of this game is Spin-flip game, in which two players take turns in flipping an electron up or down twice and then the electron's final state is measured. Player B wins if the measured state is up.</td><td>If player B uses quantum strategies while player A uses mixed classical ones, player B can win the game with certainty.</td></tr><tr><td>Prisoner's dilemma [17,19,24,33,39,42,43,85-87,94,98,137,160]</td><td>Two players (prisoners) choose either to confess a crime or to corporate with each other and deny a crime. When they cooperate their payoff is higher than the payoff when they defect.</td><td>The usual dilemma disappears if the players use restricted quantum strategies, but it cannot be removed within a general strategy space. The payoffs for the players are dependent on the degree of entanglement. The classical analogy is embedded.</td></tr><tr><td>Rock-scissors-paper [53,90,97,99]</td><td>Two players use their hands to represent their three strategies, Rock, Scissors or Paper. Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. If their gestures are same the game is tied.</td><td>Although the mixed-strategy classic solution is not stable, the modified game (where draws get a slight premium) yields stable mixed-strategy NE for some initial state for the quantum game.</td></tr><tr><td>RSA game [71]</td><td>One player sends an encrypted message  $M^e$ and public key N and e to the other player. If the message can be decrypted, then the player who encrypts the message losses.</td><td>The message is decrypted and the player who guesses the number M wins. Shor's quantum algorithm [158] and Fourier transformation techniques are used in the decryption process.</td></tr><tr><td>Stag hunt game (Samaritan game) [85,86,147,163]</td><td>Two players choose to cooperate or not. Their payoffs are higher if they cooperate with each other than if they do not. Two Nash equilibrium exists, which is the difference between the stag hunt game and prisoner's dilemma game.</td><td>The usual dilemma is ameliorated if we use Schmidt decomposition in describing two-player joint strategies. The classical game can be reproduced from entangled states when Greenberger-Horne-Zeilinger (GHZ) states are used. A GHZ state is  $\frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$ </td></tr><tr><td>Trucker's game [41]</td><td>A number of truckers choose one of n roads to drive to a city. The worst case is that all truckers chose the same road, and the best is that every road is chosen by a single trucker.</td><td>The worst case is removed in the quantum game.</td></tr><tr><td>Ultimatum game [166]</td><td>Two players divide a fixed amount of money. Player A proposes a plan. If player B agrees with the proposal then the players get what was agreed upon. However, if player B rejects the plan, then both get nothing.</td><td>The ultimatum game can be quantized, and entanglement effects cause interdependency between players.</td></tr><tr><td>Vaidman's game [12,90,164]</td><td>Three players reach agreement before they are brought to separate places. They are asked questions “what is Z” or “what is X” and their answers can be “0” or “1” only. If they are all asked the question about Z and the number of “0” answers is odd, the team wins. The team also can win in the case where two of them are asked Z question and one is asked X question and the number of “0” answers is even.</td><td>It is possible to win the Vaidman's game. Vaidman's game implicitly assumed that 3-players shared a common eference frame.</td></tr><tr><td>Wise and foolish Alice [147]</td><td>Player B puts a ball on one of four corners and player A guesses the location of the ball. Player A can ask questions about where B put the ball, and B gives “yes” or “no” answers assuming that he is honest. If the answer is “yes” then A is satisfied, otherwise player B losses money to player A.</td><td>The Wise Alice game has the same payoff matrix as the Foolish Alice game showing that the payoff matrix doesn't tell us about the rules of the game. However, the average payoff to both types of Alice is the same for a single game. Repeated games lead to differences. A non-distributive property arises which is easily and naturally handled in a quantum version of the game.</td></tr></table>

Others worried about the preparation of the initial state. Some early papers viewed the initial state prepared by the referee [94,114]. Witte [170] formulates quantum games where initial states are prepared by players. Others look at the entanglement between the initial state and the measurement basis [133], at special types of entangled initial states [44,63,157,163] or at a general initial states [132]. An interesting issue arises when the referee might lie to the players about the initial state [155].

In classic games, players can be viewed as random variables. Boukas [9] generalizes this to viewing players as quantum entities. De Sousa et al. [160] treats the payoffs as quantum information, allowing entanglement between payoffs and strategies. This can make a game where some possibilities of the payoff table are forbidden or for the game to remain only in equilibrium states.

Some generalizations occur because of quantum mechanical considerations. One avenue looks at the changes to the basic game theory model under decoherence. In closed systems, unitary matrices dictate state changes. In open systems where decoherence is likely to occur, other classes of transforms are needed [1,47,82,174,175].

## 3.2. Additional quantum mechanical aspects

The most common quantum mechanical feature explored in quantum games is entanglement. Even within this topic, there are additional issues. For example, there are different types of entanglement. Dur et al. [44] look at two different representations of entanglement (Greenberger–Horne–Zeilinger state and W state). The W state is more stable than the GHZ state since if one qubit is removed, the W state remains entangled. This is used in the Minority quantum game by Flitney and Hollenberg [63] where they show the GHZ states become very fragile as the number of players increases. Interestingly, Shimamura et al. [157] show that classical games can be reproduced from quantum games if initial states are N-product states, or entangled GHZ states.

A number of papers have looked at effects other than entanglement that quantum mechanics brings to game theory. As shown in Section 2 with the Penny Flip game, superposition can play a role. This is seen in Table 1 — for example in the Bargaining Game and the Number Game. Another quantum mechanical feature that plays a prominent topic in quantum games is decoherence which can be viewed as introducing noise into a game. Some papers look at the impact of decoherence on speci<sup>fi</sup>c games (e.g., [19,21,56,61,

63,133]) with many <sup>fi</sup>nding that noise reduces the quantum effects of entanglement. Most such papers view decoherence as a statistically independent stochastic process but evidence suggest it is likely a correlated noise that can be suppressed using Parrondo type games [115].

Özdemir et al. [137] look at how corruption of the source input qubits strongly and negatively in<sup>fl</sup>uences payoffs and the number of NE if players are unaware of corruption – removing advantages seen in quantum games. If they know about the corruption they can handle it.

Some more esoteric aspects have been explored too. Hruby [82] uses ideas from supersymmetric quantum mechanics in exploring quantum games. This leads to another type of generalization to unitary matrices discussed earlier in Section 3.1. Grover's quantum database search [74] is used to search for the number in the Guess the Number game [71].

## 3.3. Theoretical properties of quantum games and extensions

Boukas [9] provides a general Minimax result assuming players are quantum entities. Lee [110,113] shows all classical games are subset of quantum games and that the Minimax theorem for zero-sum games and NE for general static games holds by assuming that the quantum feature in games is not the players but the strategies that players have. This assumption is widely used.

Landsburg [108] considers computing NE when the players can communicate with the referee, thus effectively expanding their strategy sets. In [107], he argues that a referee would never be able to distinguish a player's mixed-strategy from a pure strategy in a single game. Others also <sup>fi</sup>nd that the arbiter is critical in computing NE. Cheon et al. [25] see that an arbiter can provide entanglement between the two strategies chosen by the players, and Ichikawa et al. [85] show that the arbiter furnishes a correlation. However, Iqbal et al. [94] note that the referee can remove any motivation for coalitions in cooperative games.

Mixed strategies are studied in quantum games. Landsburg [107] formalizes mixed strategies in general games. Stohler and Fischbach [161] show two ways to study mixed quantum strategies, either by using classical probabilities or a single matrix that combines classical probabilities and operators. Even though in some cases no pure-strategy equilibrium exists in games with general strategy spaces, mixed-strategy equilibria may exist, as shown by Eisert et al. [47].

Some studies study how to quantize multiplayer games and to generalize two-player quantum games into n player quantum games. For example, Du et al. [40,42] extend the Prisoner's Dilemma game to an n player prisoner's dilemma game. Wu [173,175] presents a different view on how to represent multiplayer games. More speci<sup>fi</sup>cally, a base vector set of the Hilbert space that is a direct product of each player's strategy vector base set is used to represent multiplayer games. The problem that the number of parameters and equations increases as the number of players expands is resolved. This is very helpful in solving n players game. In entangled multiplayer games, Flitney [63] gives an interesting result that as the number of players increases, the entanglement of the game decreases. This diminishes the added contribution quantization brings over their classic counterpart.

When quantum games are allowed to repeat, results different from the single game may appear. In the Wise and

Foolish Alice game, Grib and Par<sup>fi</sup>onov [73] <sup>fi</sup>nd that the expected payoff of Alice is higher than that of her opponent in repeated games even though they have the same expected payoffs in one round. Iqbal [98] show that different results emerge between the repeated quantum Prisoner's Dilemma game and the single round version. For example, if the game is repeated twice, players in the game cooperate instead of defect.

Cooperation in games has also been explored. Some papers [33,39,40] show that entanglement improves the coordination between players and thus payoffs (if the payoff function depends on players' types.) The quantum coordination problem is studied in a number of papers [83,88,96,100,102,105]. Iqbal et al. [96] focus on the correlations of outcomes and <sup>fi</sup>nd that NE change based on correlation and quantum games are not reproducible with classic games. Witte [171] shows correlations between payoffs yields neutral or winning/losing strategies. Flitney and Greentree [62] compare coalitions using entanglement versus classic communication, and <sup>fi</sup>nd that as the coalition size increases, classic communication is better when measurement is done in an arbitrary basis.

Evolutionary game theory originated from the combination of evolutionary biology and game theory with a focus on players' strategy dynamics. The associated equilibrium concept is evolutionary stable strategy (ESS) de<sup>fi</sup>ned as a strategy that cannot be invaded by mutant strategies once <sup>fi</sup>xed in the population. Evolutionary quantum games were introduced through papers like [65,66,125]. Iqbal et al. [91–93,95,97,99] show that, under a symmetric information condition, classical games can evolve to quantum games while NE remain unchanged, and that a non-ESS attractor of replicator dynamics can be changed into an ESS or, conversely, when a classic game is changed to a quantum game. However, entanglement in asymmetric or symmetric games can disturb ESS equilibria. Kay et al. [103] concludes that a quantum evolutionary game dominates a classic game if time steps are large, but the quantum evolutionary game is not better with small time intervals. Application of ESS in <sup>fi</sup>nancial markets is studied by Gonçalves and Gonçalves [70].

## 3.4. Information and communication theory

Quantum information theory [135,104] deals with information theory that relies on quantum effects. These problems often arise in communication applications including such topics as error correction, coding, teleportation and others. Iqbal [90] states that the theory of quantum communication can be viewed as quantum games. Although most researchers in quantum information don't use game-theoretic paradigms, it is clear that this view offers many unique perspectives. We only touch on quantum games in this area.

Fitzi and Gisin [55] show that a quantum solution to the Byzantine Agreement problem exists with the help of entangled qudits. Eisert et al. [46] discuss an entanglementassisted local operator in classical communication (ELOCC) and shows that ELOCC is greater than LOCC (local operator in classical communication.)

Lee et al. [111] tighten the link between quantum game theory and quantum information. They address two technical issues that arise in quantum information areas by studying quantum games that capture the phenomena. Werner [168] also argues that quantum games are a good way to view quantum information.

Table 2  
Econophysics games

<table><tr><td>Research stream</td><td>Type</td><td>Description</td><td>Contribution</td></tr><tr><td rowspan="4">Competitive models</td><td>Cournot [22,35,117]</td><td>There is a quantity competition between duopoly firms who produce a homogeneous product. Firms compete in quantities and choose quantities simultaneously.</td><td>Entanglement can increase payoffs by inducing cooperation. Information asymmetry under entanglement impacts payoffs for both players. The effect of entanglement becomes complicated when information is uncertain. here quantum games do not perform better than classical ones.</td></tr><tr><td>Bertrand [121,156]</td><td>There is a price competition between duopoly firms who produce a homogeneous product. Firms compete in prices and choose prices simultaneously.</td><td>Profit is a monotonic function of entanglement degree.</td></tr><tr><td>Stackelberg [94,120,122]</td><td>In a Stackelberg game, a leader moves first and followers second. The leader becomes better off at the expense of the followers.</td><td>In a Stackelberg duopoly game with complete information, the first move advantage is a monotonic function of entanglement degree. Positive entanglement measurement enhances the advantage, while negative degree decreases the benefit. In a Stackelberg duopoly game with incomplete information, entanglement helps the first mover advantage. Negative entanglement hurts. The uncertainty of information for the first player hurts his first move advantage.</td></tr><tr><td>Oligopolies [33,119]</td><td>Oligopoly refers to a market form within which a small number of sellers dominate the market.</td><td>Entanglement can be used to study oligopolies in a quantum setting. A measure of information incorrectness can be varied to regulate bad aspects.</td></tr><tr><td rowspan="4">Financial models</td><td>Financial markets [140,141,143,148,150-153,159]</td><td>There are changing and unlimited number of players whose payoffs are non-constant. Each trader possesses asset B and money $. Arbiter A considers traders&#x27; strategies, assets and money to decide the output.</td><td>Quantum market models can explain sudden large price changes (quantum zeno effect), &quot;undividity of attention of traders&quot;, etc.</td></tr><tr><td>Financial markets as a minority game [14,15,50]</td><td>Financial markets can be modeled as minority games with minor modification.</td><td>If players in a market act as price takers, the minority game reproduces stylized facts of financial markets such as fat tailed distribution of returns and volatility clustering.</td></tr><tr><td>Financial markets as an evolutionary quantum game [70]</td><td>Financial markets can be modeled as evolutionary quantum games.</td><td>Financial markets can be modeled as evolutionary quantum games to explain multifractal behavior.</td></tr><tr><td>Treasury bonds [3]</td><td>A treasury bond is a financial instrument for which there is no risk of default in receiving the payments. The forward rate of a treasury bond represents the spot interest rate at a future time for a contract entered at a previous time which is a stochastic variable.</td><td>Path integral approaches are used to model forward rates of treasury bonds. For forward rates, the entire yield curve impacts a bond&#x27;s price.</td></tr><tr><td>Principal-agent</td><td>Production [31,51,52]</td><td>The principal is risk neutral and the risk averse agent can be either a worker or a shirker. If the agent is a worker, then the outcome would be a success with probability p and a failure with probability 1-p; If the agent is a shirker, then the outcome would be a failure for sure.</td><td>The agency model is analyzed under no synergy, pure synergy and partial synergy. &quot;Nature&#x27;s production&quot; models synergy as an entangled state. With max synergy, an aggregate (group) measure is more effective. With partial synergy, an aggregate measure may be more or less effective depending on other factors.</td></tr><tr><td>Public goods</td><td>N-player free riding problem [20]</td><td>An n-player public goods game involves an organization that decides whether to provide a common good which can be consumed by n players. Some players may free ride on the efforts of other players.</td><td>By using entangled two particles, players achieve better (near optimal) expected payoff than in the classical problem when they play mixed strategies.</td></tr><tr><td rowspan="2">Auctions</td><td>General [76,81]</td><td>An auction is a mechanism of bidding and deciding the winning bidder(s) and payment rule.</td><td>Quantum auctions work better than classical ones with respect to payoffs, privacy, and other aspects. Privacy is not necessarily improved in a quantum auction. A dishonest auctioneer can violate the privacy guarantees but bidders can counter this. (See also [146]).</td></tr><tr><td>English auction [18,149]</td><td>An English auction is an open-bid auction. The auctioneer announces a reserve price (the lowest acceptable price) and then the competing buyers increase their bids. The highest bidder wins and pays the highest bid.</td><td>Experiments with humans [18] show that people tend to overbid compared to NE even in classic settings. Lower revenue and allocative efficiencies resulted - probably because of the many no win cases.</td></tr><tr><td>Asset valuation models</td><td>Binomial (CRR) market [16]</td><td>There is a stock with a current price  $S_0$  and an option on the stock with a current price C. The stock price can either go up or down. Assumes no arbitrage.</td><td>The classic binomial market model results in a paradox - the option price does not depend on the probabilities of the stock price moving up and down. Quantization of the binomial market model resolves the paradox.</td></tr></table>

Goldenberg et al. [69] offer a secure communication scheme using a quantum game. This was extended by Hwang et al. [84]. Bennett et al [8] show that while encoding two bits and then transmitting them as a single particle of two states, players can non-locally communicate with each other and a player can know the other player's operation. La Mura [105] concludes that quantum signals are better than classical ones in classic games.

## 3.5. Quantum econophysics

The application of ideas in physics to economics [50] is often called econophysics. Some have argued that mathematical economics and quantum mechanics are isomorphic [80,106]. With the advent of quantum game theory, a particularly interesting stream of research explores quantum game theory applications in economic areas. Table 2 gives a summary of articles organized along several economic themes. We brie<sup>fl</sup>y discuss each theme and some quantum results.

Three of the most common competitive models (Cournot, Bertrand, and Stackelberg) are quantized in the context of both duopoly and oligopoly. Quantum <sup>fi</sup>nancial models (minority game and evolutionary game) are proposed to depict <sup>fi</sup>nancial markets and <sup>fi</sup>nancial instruments. These quantum <sup>fi</sup>nancial models can explain special features such as quantum zeno effect, undividity of attention of traders, fat tailed distribution of returns, volatility clustering, multifractal behavior, etc. Quantum public goods games are more ef<sup>fi</sup>cient in terms of players' expected payoff compared to classic results. Quantum auctions sometimes outperform classic auctions with respect to payoffs, privacy, and other aspects. Concepts and techniques from quantum game theory are also applied to principal–agent theory. The effectiveness of different measures depends on the synergy of agents. Quantization of a simple asset valuation model – the binomial model – resolves the classic paradox.

## 4. Concluding remarks and future research

Although much has been accomplished in this nascent <sup>fi</sup>eld, much remains to be explored. None of the themes discussed in Section 3 are mature leaving plenty of room for future work. Some streams are likely to be extended by specialists in quantum phenomena, like the generalizations involving decoherence. However, formulating and studying applications of quantum games within the decision sciences is an important area for future research.

Many papers in quantum games involve quantization of classic games as presented in Table 1. However, there is a noticeable concentration on static games and dynamic games with complete information. Numerous categories of classic games still remain unexplored. The only quantized games studied with incomplete information are continuous games such as Cournot duopoly, Stackelberg duopoly and Bertrand duopoly. There is no discussion of quantum games with perfect information versus imperfect information. Quantization of classic games and comparisons between quantum and classic counterparts are of special importance because they represent a natural start to explore the power of quantum games.

Many decision science problems can be viewed as principal– agent problems, including learning involving strategic agents [10]. Only one principle–agent model has been discussed in a quantum form [31,51,52] leaving much to be explored in future research. Trust in eCommerce (e.g., [126]) has received considerable attention in recent years. Ar<sup>fi</sup> [2] used the Stag Hunt and Prisoner's Dilemma games to illustrate how trust can be constructed by a quantum approach. This avenue may prove useful in eCommerce especially since communication systems are inherently quantum mechanical. Related ideas of cheating [154] and reputation [176] might also bene<sup>fi</sup>t from such research.

Although several papers address the gap between quantum mechanical level phenomena and the macro level most activities take place in, more work is needed here. An interesting contribution by Deutsch [32] shows how quantum formulas relating amplitudes to probabilities can be derived from other axioms of quantum mechanics. He does this assuming a rational economic agent, who believes everything about quantum mechanics but does not assume the probabilistic postulates, makes decisions. The result is the usual zerosum game-theoretic setting.

## References

[1] D. Aerts, M. Czachor, L. Gabora, M. Kuna, A. Posiewnik, J. Pykacz, M. Syty, Quantum morphogenesis: a variation on Thom's catastrophe theory, Physical Review E 67 (5) (2003) 51926.

[2] B. Ar<sup>fi</sup>, Resolving the trust predicament: a quantum game-theoretic approach, Theory and Decision 59 (2005) 127–174.

[3] B.E. Baaquie, Quantum <sup>fi</sup>eld theory of treasury bonds, Physical Review E 64 (1) (2001) 16121.

[4] S. Bandyopadhyay, P. Pathak, Knowledge sharing and cooperation in outsourcing projects — a game-theoretic analysis, Decision Support Systems 43 (2) (2007) 349–358.

[5] S.C. Benjamin, Comment on “a quantum approach to static games of complete information”, Physics Letters A 277 (3) (2000) 180–182.

[6] S.C. Benjamin, P.M. Hayden, Comment on “quantum games and quantum strategies”, Physical Review Letters 87 (6) (2001) 69801.

[7] S.C. Benjamin, P.M. Hayden, Multiplayer quantum games, Physical Review A 64 (3) (2001) 30301.

[8] C.H. Bennett, S.J. Wiesner, Communication via one- and two-particle operators on Einstein–Podolsky–Rosen states, Physical Review Letters 69 (20) (1992) 2881–2884.

[9] A. Boukas, Quantum formulation of classical two person zero-sum games, Open Systems & Information Dynamics 7 (2004) 19–32.

[10] F. Boylu, H. Aytug, G.J. Koehler, Induction over strategic agents, Information Systems Research (in press).

[11] J. Brynielsson, Using AI and games for decision support in command and control, Decision Support Systems 43 (4) (2007) 1454–1463.

[12] A. Cabello, Greenberger–Horne–Zeilinger-like proof of Bell's theorem involving observers who do not share a reference frame, Physical Review A 68 (4) (2003) 42104.

[13] D. Challet, M. Marsili, Phase transition and symmetry breaking in the minority game, Physical Review E 60 (6) (1999) 6271–6274.

[14] D. Challet, M. Marsili, Y.C. Zhang, Minority games and stylized facts, Physica A: Statistical Mechanics and its Applications 299 (1–2) (2001) 228-233.

[15] D. Challet, M. Marsili, Y.C. Zhang, Stylized facts of <sup>fi</sup>nancial markets and market crashes in minority games, Physica A: Statistical Mechanics and its Applications 294 (3–4) (2001) 514–524.

[16] Z. Chen, Quantum theory for the binomial model in <sup>fi</sup>nance theory, Working paper, arxiv:quant-ph/0112156v5, (2002).

[17] K.Y. Chen, T. Hogg, How well do people play a quantum prisoner's dilemma? Quantum Information Processing 5 (1) (2006) 43–67.

[18] K.Y. Chen, T. Hogg, Experiments with probabilistic quantum auctions, Working paper, arXiv: 0707.4195, (2007).

[19] L.K. Chen, H. Ang, D. Kiang, L.C. Kwek, C.F. Lo, Quantum prisoner dilemma under decoherence, Physics Letters A 316 (5) (2003) 317–323.

[20] K.Y. Chen, T. Hogg, R. Beausoleil, A quantum treatment of public goods economics, Quantum Information Processing 1 (6) (2002) 449–469.

[21] J.L. Chen, L.C. Kwek, C.H. Oh, Noisy quantum game, Physical Review A 65 (5) (2002) 52320.

[22] X. Chen, G. Qin, X. Zhou, J. Du, Quantum games of continuous distributed incomplete information, Chinese Physics Letters 22 (005) (2005) 1033–1036.

[23] Q. Chen, Y. Wang, J.T. Liu, K.L. Wang, N-player quantum minority game, Physics Letters A 327 (2–3) (2004) 98–102.

[24] T. Cheon, Altruistic contents of quantum prisoner's dilemma, Europhysics Letters 69 (2) (2005) 149–155.

[25] T. Cheon, I. Tsutsui, Classical and quantum contents of solvable game theory on Hilbert space, Physics Letters A 348 (3–6) (2006) 147–152.

[26] R. Cleve, P. Høyer, B. Toner, J. Watrous, Consequences and limits of nonlocal strategies, Proceedings: 19th IEEE Annual Conference on Computational Complexity, 2004, pp. 236–249.

[27] G.M. D'ariano, R.D. Gill, M. Keyl, R.F. Werner, B. Kummerer, H. Maassen, The quantum Monty Hall problem, Working paper, arXiv:quant-ph/ 0202120 v1, (2002).

[28] G.B. Dahl, S.E. Landsburg, Quantum strategies in noncooperative games, University of Rochester, Working paper, (2005).

[29] R. Dawkins, The sel<sup>fi</sup>sh gene, Oxford University Press, New York, 1989.

[30] J.S. Demski, S.A. Fitzgerald, Y. Ijiri, Y. Ijiri, H. Lin, Quantum information and accounting information: their salient features and conceptual applications, Journal of Accounting and Public Policy 25 (2006) 435–464.

[31] J.S. Demski, J.C. Fellingham, H.H. Lin, D.A. Schroeder, Interaction between measurement and production, Accounting Department University of Florida, Working paper, (2007).

[32] D. Deutsch, Quantum theory of probability and decisions, Proceedings: Mathematical, Physical and Engineering Sciences 455 (1988) (1999) 3129–3137.

[33] J. Du, C. Ju, H. Li, Quantum entanglement helps in improving economic ef<sup>fi</sup>ciency, Journal of Physics A Mathematical and General 38 (7) (2005) 1559–1565.

[34] J. Du, C. Ju, H. Li, Quantum strategy without entanglement, Journal of Physics A Mathematical and General 38 (7) (2005) 1559–1565

[35] J. Du, H. Li, C. Ju, Quantum games of asymmetric information, Physical Review E 68 (1) (2003) 16124.

[36] J. Du, H. Li, X. Xu, M. Shi, J. Wu, X. Zhou, R. Han, Experimental realization of quantum games on a quantum computer, Physical Review Letters 88 (13) (2002) 137902.

[37] J. Du, H. Li, X. Xu, M. Shi, X. Zhou, R. Han, Remark on quantum battle of the sexes game, Working paper, arXiv:quant-ph/0103004v (2001).

[38] J. Du, X. Xu, H. Li, X. Zhou, R. Han, Nash equilibrium in the quantum battle of sexes game, Working paper, arxiv quant-ph/0010050, (2000)

[39] J. Du, X. Xu, H. Li, X. Zhou, R. Han, Entanglement playing a dominating role in quantum games, Physics Letters A 289 (1) (2001) 9–15.

[40] J. Du, H. Li, X. Xu, X. Zhou, R. Han, Entanglement enhanced multiplayer quantum games, Physics Letters A 302 (2002) 229–233.

[42] J. Du, X. Xu, H. Li, X. Zhou, R. Han, Playing prisoner's dilemma with quantum rules, Fluctuation and Noise Letters 2 (4) (2002) R189–R203.

[43] J. Du, H. Li, X. Xu, X. Zhou, R. Han, Phase-transition-like behaviour of quantum games, Journal of Physics A Mathematical and General 36 (23) (2003) 6551–6562.

[44] W. Dür, G. Vidal, J.I. Cirac, Three qubits can be entangled in two inequivalent ways, Physical Review A 62 (2000).

[45] A. Einstein, B. Podolsky, N. Rosen, Can quantum-mechanical description of physical reality be considered complete? Physical Review 47 (10) (1935) 777–780.

[46] J. Eisert, M. Wilkens, Catalysis of entanglement manipulation for mixed states, Physical Review Letters 85 (2) (2000) 437–440.

[47] J. Eisert, M. Wilkens, Quantum games, Journal of Modern Optics 4 (14/ 15) (2000) 2543–2556.

[48] J. Eisert, M. Wilkens, M. Lewenstein, Quantum games and quantum strategies Physical Review Letters 83 (15) (1999) 3077–3080

[49] D. Farmer, Physicists attempt to scale the ivory towers of <sup>fi</sup>nance, Computing in Science and Engineering 1 (6) (1999) 26–39.

[50] J.D. Farmer, M. Shubik, E. Smith, Is economics the next physical science? Physics Today 58 (9) (2005) 37–42.

[51] J. Fellingham, D. Schroeder, Quantum information and accounting, Journal of Engineering and Technology Management 23 (1–2) (2006) 33–53.

[52] J. Fellingham, D. Schroeder, Synergy, quantum probabilities, and cost of control, Essays in Accounting Theory in Honour of Joel S. Demski Springer, New York, 2007.

[53] P.V. Fellman, The Nash equilibrium revisited: chaos and complexity hidden in simplicity, International Conference on Complex Systems, Boston, 2004.

[54] P.V. Fellman, J.V. Post, Quantum Nash equilibria and quantum computing, Southern New Hampshire University, New Hampshire, 2007.

[55] M. Fitzi, N. Gisin, U. Maurer, Quantum solution to the Byzantine agreement problem, Physical Review Letters 87 (21) (2001) 217901.

[56] A.P. Flitney, Aspects of quantum game theory, Department of Electrical and Electronic Engineering, Faculty of Engineering, Computer and Mathematical Sciences, The University of Adelaide, Australia. 2005

[57] A.P. Flitney, D. Abbott, An introduction to quantum game theory, Working paper, arxiv: quant-ph/0208069, (2002).

[58] A.P. Flitney, D. Abbott, Quantum version of the Monty Hall problem Physical Review A 65 (6) (2002) 62318.

[59] A.P. Flitney, D. Abbott, Quantum models of Parrondo's games, Physica A: Statistical Mechanics and its Applications 324 (1–2) (2003) 152–156.

[61] A.P. Flitney, D. Abbott, Quantum games with decoherence, Journal of Physics A Mathematical and General 38 (2) (2005) 449–459.

[62] A.P. Flitney, A.D. Greentree, Coalitions in the quantum minority game: classical cheats and quantum bullies, Physics Letters A 362 (2–3) (2007) 132–137.

[63] A.P. Flitney, L.C.L. Hollenberg, Multiplayer quantum minority game with decoherence, Working paper, arXiv:quant-ph/0510108v2, (2005).

[64] A.P. Flitney, L.C.L. Hollenberg, Nash equilibria in quantum games with generalized two-parameter strategies, Physics Letters A 363 (5–6) (2007) 381–388.

[65] J.S.Gale,L.J.Eaves,Logicof animalcon<sup>fl</sup>ict,Nature254(5499)(1975)463.

[66] P.W. Glimcher, Decisions, decisions, decisions choosing a biologica science of choice, Neuron 36 (2) (2002) 323–332.

[67] P. Gmytrasiewicz, S. Parsons, Editorial: decision theory and game theory in agent design, Decision Support Systems 39 (2) (2005) 151–152.

[68] V. Gogonea, K.M. Merz, Fully quantum mechanical description of proteins in solution — combining linear scaling quantum mechanical methodologies with the Poisson–Boltzmann equation, Journal of Physical Chemistry A 103 (26) (1999) 5171–5188.

[69] L. Goldenberg, L. Vaidman, S. Wiesner, Quantum gambling, Physica Review Letters 82 (16) (1999) 3356–3359.

[70] C.P. Gonçalves, C.G. Gonçalves, An evolutionary quantum game mode of <sup>fi</sup>nancial market dynamics — theory and evidence, Working paper, (2007).

[71] J.O. Grabbe, An introduction to quantum game theory, Working paper, : quant-ph/0506219, (2005).

[72] A.A. Grib, A.Y. Khrennikov, G.N. Par<sup>fi</sup>onov, K.A. Starkov, Distributivity breaking and macroscopic quantum games, Working paper, arXiv: quant-ph/0504129v1, (2005).

[73] A.A. Grib, G.N. Par<sup>fi</sup>onov, Can a game be quantum? Journal of Mathematical Sciences 125 (2) (2005) 173–184.

[74] L.K. Grover, A fast quantum mechanical algorithm for database search, Proceedings of the Twenty-Eighth Annual ACM Symposium on Theory of Computing, Philadelphia, PA, USA, 1996, pp. 212–219.

[75] L.A. Guardiola, A. Meca, J. Timmer, Cooperation and pro<sup>fi</sup>t allocation in distribution chains, Decision Support Systems 44 (1) (2007) 17–27.

[76] S. Guha, T. Hogg, D. Fattal, T. Spiller, R.G. Beausoleil, Quantum auction using adiabatic evolution: the corrupt auctioneer and circuit imple mentations, Working paper, arxiv.org/abs/0707.2051, (2007).

[77] F. Guinea, M.A. Martin-Delgado, Quantum Chinos game: winning strategies through quantum <sup>fl</sup>uctuations, Journal of Physics A: Mathematical and General 36 (13) (2003) 197–204.

[78] G.P. Harmer, D. Abbott, Losing strategies can win by Parrondo's paradox, Nature 402 (1999) 864.

[79] M. Hemmo, I. Pitowsky, Quantum probability and many worlds, Studies in History and Philosophy of Modern Physics 38 (2) (2007) 333–350.

[80] E.G. Hidalgo, Quantum econophysics, Working paper, arxiv:quant-ph/ 0609245v2, (2007).

[81] T. Hogg, P. Harsha, K.Y. Chen, Quantum auctions, Working paper, arXiv: quant-ph/0704.0800v1 (2007).

[82] J. Hruby, Supersymmetry and quantum games, Working paper, arxiv: quant-ph/0703275, (2007).

[83] B.A. Huberman, T. Hogg, Quantum solution of coordination problems, Quantum Information Processing 2 (6) (2003) 421–432.

[84] W.Y. Hwang, D. Ahn, S.W. Hwang, Quantum gambling using two nonorthogonal states, Physical Review A 64 (6) (2001) 64302.

[85] T. Ichikawa, I. Tsutsui, Duality, phase structures, and dilemmas in symmetric quantum games, Annals of Physics 322 (3) (2007) 531–551.

[86] T. Ichikawa, I. Tsutsui, T. Cheon, Quantum game theory based on the Schmidt decomposition: can entanglement resolve dilemmas? Working paper, arxiv: quant-ph/0702167, (2007).

[87] A. Iqbal, Quantum games with a multi-slit electron diffraction setup, Working paper, arxiv: quant-ph/0207078, (2002).

[88] A. Igbal. Ouantum correlations and Nash equilibria of a bi-matrix game, Journal of Physics A: Mathematical and General 37 (29) (2004) L353–L359.

[89] A. Iqbal, Playing games with EPR-type experiments, Journal of Physics A: Mathematical and General 38 (43) (2005) 9551–9564.

[90] A. Iqbal, Studies in the theory of quantum games, Department of Electronics, Quaid-i-Azam University, Islamabad, Pakistan, 2005.

[91] A. Iqbal, A.H. Toor, Entanglement and dynamic stability of Nash equilibria in a symmetric quantum game, Physics Letters A 286 (2001) 245–250.

[92] A. Iqbal, A.H. Toor, Equilibria of replicator dynamics in quantum games, Working paper, arxiv: quant-ph/0106135, (2001).

[93] A. Iqbal, A.H. Toor, Evolutionarily stable strategies in quantum games, Physics Letters A 280 (5–6) (2001) 249–256.

[94] A. Iqbal, A.H. Toor, Backwards-induction outcome in a quantum game, Physical Review A 65 (5) (2002) 52328.

[95] A. Iqbal, A.H. Toor, Darwinism in quantum systems? Physics Letters A 294 (2002) 261–270.

[96] A. Iqbal, A.H. Toor, Quantum cooperative games, Physics Letters A 293 (2002) 103–108.

[97] A. Iqbal, A.H. Toor, Quantum mechanics gives stability to a Nash equilibrium, Physical Review A 65 (2) (2002) 22306.

[98] A. Iqbal, A.H. Toor, Quantum repeated games, Physics Letters A 300 (2002) 541–546.

[99] A. Iqbal, A.H. Toor, Stability of mixed Nash equilibria in symmetric quantum games, Working paper, arXiv:quant-ph/0106056v4 6 Jul 2004, (2007).

[100] A. Iqbal, S. Weigert, Quantum correlation games, Journal of Physics A Mathematical and General 37 (22) (2004) 5873–5885.

[101] N.F. Johnson, Playing a quantum game with a corrupted source, Physical Review A 63 (2) (2001) 20302.

[102] V. Kargin, On coordination games with quantum correlations, International Journal of Game Theory 37 (2) (2008) 211–218.

[103] R. Kay, N.F. Johnson, S.C. Benjamin, Evolutionary quantum game, Journal of Physics A: Mathematical and General 34 (41) (2001) 547–552.

[104] M. Keyl, Fundamentals of quantum information theory, Working paper, arXiv:quant-ph/0202122v1, (2002).

[105] P. La Mura, Correlated equilibria of classical strategic games with quantum signals, Working paper, arXiv:quant-ph/0309033v1, (2003).

[106] L. Lambertini, Quantum mechanics and mathematical economics are isomorphic, 2000.

[107] S.E. Landsburg, Quantum game theory, Notices of the American Mathematical Society 51 (2004) 394–399.

[108] S. Landsburg, Nash equilibria in quantum games, Working paper, http://ideas.repec.org/p/roc/rocher/524.html, (2006).

[109] C.F. Lee, N. Johnson, Let the quantum games begin, Physics World 15 (10) (2002) 25–29.

[110] C.F. Lee, N.F. Johnson, Ef<sup>fi</sup>ciency and formalism of quantum games, Physical Review A 67 (2) (2003) 022311.

[111] C.F. Lee, N.F. Johnson, Game-theoretic discussion of quantum state estimation and cloning, Physics Letters A 319 (2003) 429–433.

[112] C.F. Lee, and N. Johnson, Parrondo games and quantum algorithms, Oxford University, Working paper, arxiv: quant-ph/0203043, (2006).

[113] C.F. Lee, and N. Johnson, Quantum game theory, Working paper, arXiv: quant-ph/0207012, (2006).

[114] C.F. Lee, N.F. Johnson, Non-cooperative quantum game theory, Oxford University, Working paper, arXiv:quant-ph/0210192v2, (2007).

[115] C.F. Lee, N.F. Johnson, F. Rodriguez, L. Quiroga, Quantum coherence, correlated noise and Parrondo games, Working paper, arXiv:quant-ph/ 0210185, (2007).

[116] D.K. Levine, Quantum games have no news for economists, Department of Economics UCLA and Federal Reserve Bank of Minneapolis Working paper, http://dklevine.com/papers/quantumnonews.pdf, (2005).

[117] H. Li, J. Du, S. Massar, Continuous-variable quantum games, Physics Letters A 306 (2–3) (2002) 73–78.

[118] C.F. Li, Y.S. Zhang, Y.F. Huang, G.C. Guo, Quantum strategies of quantum measurement, Physics Letters A 280 (2001) 257–260.

[119] C.F. Lo, D. Kiang, Quantum oligopoly, Europhysics Letters 64 (5) (2003) 592–598.

[120] C.F. Lo, D. Kiang, Quantum Stackelberg duopoly, Physics Letters A 318 (4–5) (2003) 333–336.

[121] C.F. Lo, D. Kiang, Quantum Bertrand duopoly with differentiated products, Physics Letters A 321 (2) (2004) 94–98.

[122] C.F. Lo, D. Kiang, Quantum Stackelberg duopoly with incomplete information, Physics Letters A 346 (1–3) (2005) 65–70.

[123] L. Marinatto, T. Weber, A quantum approach to static games of complete information, Working paper, arxiv: quant-ph/0004081, (2000).

[124] L. Marinatto, T. Weber, Reply to “Comment On: A Quantum Approach to Static Games of Complete Information”, Physics Letters A 277 (3) (2000) 183–184.

[125] J. Maynard-Smith, G.R. Price, The logic of animal con<sup>fl</sup>ict, Nature 246 (5427) (1973) 15–18.

[126] D.H. Mcknight, V. Choudhury, C. Kacmar, Developing and validating trust measures for e-commerce: an integrative typology, Information Systems Research 13 (2002) 334–359.

[127] D.A. Meyer, Quantum strategies, Physical Review Letters 82 (5) (1999) 1052–1055.

[128] D.A. Meyer, H. Blumer, Parrondo games as lattice gas automata, Journa of Statistical Physics 107 (1) (2002) 225–239.

[129] S. Minner, Bargaining for cooperative economic ordering, Decision Support Systems 43 (2) (2007) 569–583.

[130] A. Nahlik, Survey of quantum game theory, Economics Department, University of Florida, Gainesville, FL, 2007.

[131] J.F. Nash, Essays on game theory, Edward Elgar Publishing, Cheltenham, England, 1996.

[132] A. Nawaz, A.H. Toor, Dilemma and quantum battle of sexes, Journal of Physics A Mathematical and General 37 (15) (2004) 4437–4443

[133] A. Nawaz, A.H. Toor, Quantum games with correlated noise, Journal of Physics A: Mathematical and General 39 (29) (2006) 9321–9328.

[134] J.V. Neumann, O. Morgenstern, Theory of games and economic behavior, Princeton University Press, Princeton, 1953.

[136] M.J. Osborne, A. Rubinstein, A course in game theory, MIT Press, Cambridge, Mass, 1994.

[137] S.K. Özdemir, J. Shimamura, N. Imoto, Quantum advantage does not survive in the presence of a corrupt source optimal strategies in simultaneous move games, Physics letters. A (2004) 104–111.

[138] J.M.R. Parrondo, G.P. Harmer, D. Abbott, New paradoxical games based on Brownian ratchets, Physical Review Letters 85 (24) (2000) 5226–5229.

[139] R. Penrose, Shadows of the mind, Oxford University Press, New York, New York, USA, 1994.

[140] E.W. Piotrowski, Fixed point theorem for simple quantum strategies in quantum market games, Physica A: Statistical Mechanics and its Applications 324 (1–2) (2003) 196–200.

[141] E.W. Piotrowski, J. Sladkowski, Quantum-like approach to <sup>fi</sup>nancial risk: quantum anthropic principle, Working paper, arxiv: quant-ph/ 0110046, (2001).

[142] E.W. Piotrowski, J. Sladkowski, Quantum bargaining games, Physica A: Statistical Mechanics and its Applications 308 (1–4) (2002) 391–401.

[143] E.W. Piotrowski, J. Sladkowski, Quantum market games, Physica A: Statistical Mechanics and its Applications 312 (1–2) (2002) 208–216.

[145] E.W. Piotrowski, J. Sladkowski, An invitation to quantum game theory, International Journal of Theoretical Physics 42 (5) (2003) 1089–1099.

[146] E.W. Piotrowski, J. Sladkowski, The merchandising mathematician model: pro<sup>fi</sup>t intensities, Physica A 318 (3–4) (2003) 496–504

[147] E.W. Piotrowski, J. Sladkowski, The next stage: quantum game theory, Working paper, arxiv: quant-ph/0308027, (2003).

[148] E.W. Piotrowski, J. Sladkowski, Quantum computer: an appliance for playing market games, Working paper, arxiv: quant-ph/0305017, (2003).

[149] E.W. Piotrowski, J. Sladkowski, Quantum English auctions, Physica A: Statistical Mechanics and its Applications 318 (3–4) (2003) 505–515

[150] E.W. Piotrowski, J. Sladkowski, Trading by quantum rules: quantum anthropic principle, International Journal of Theoretical Physics 42 (5) (2003) 1101–1106.

[151] E.W. Piotrowski, J. Sladkowski, Quantum game theory in <sup>fi</sup>nance, Working paper, arXiv:quant-ph/0406129v1, (2004).

[152] E.W. Piotrowski, J. Sladkowski, Quantum diffusion of prices and pro<sup>fi</sup>ts, Physica A: Statistical Mechanics and its Applications 345 (1–2) (2005) 185–195.

[153] E.W. Piotrowski, J. Sladkowski, J. Syska, Interference of quantum market strategies, Physica A: Statistical Mechanics and its Applications 318 (3-4) (2003) 516-528

[154] R. Porter, Y. Shoham, On cheating in sealed-bid auctions, Decision Support Systems 39 (1) (2005) 41–54

[155] J. Pykacz, P. Frackiewicz, Arbiter as the third man in classical and quantum games, Working paper, arXiv: quant-ph/0707.0591v1, (2007).

[156] G. Qin, X. Chen, M. Sun, J. Du, Quantum Bertrand duopoly of incomplete information, Journal of Physics A Mathematical and General 38 (19) (2005) 4247–4253.

[157] J. Shimamura, S.K. Özdemir, F. Morikoshi, N. Imoto, Entangled states that cannot reproduce original classical games in their quantum version Physics Letters A 328 (2004) 20–25

[158] P.W. Shor, Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer, SIAM Journal on Computing 26 (5) (1997) 1484–1509.

[159] J. Sladkowski, Giffen paradoxes in quantum market games, Physica A: Statistical Mechanics and its Applications 324 (1–2) (2003) 234–240.

[160] P.B. Sousa, R. Viana Ramos, J. Tarcísio Costa Filho, New models of quantum games, Working paper, arXiv quant-ph/0608131, (2006).

[161] M. Stohler, E. Fischbach, Non-transitive quantum games, Working paper, arXiv:quant-ph/0307072v1, (2003).

[162] A.P. Tchangani, A satis<sup>fi</sup>cing game theory approach for group evaluation of production units, Decision Support Systems 42 (2) (2006) 778–788.

[163] N. Toyota, Quantization of the stag hunt game and the Nash equilibrium, Working paper, arXiv:quant-ph/0307029v1, (2003).

[164] L. Vaidman, Variations on the theme of the Greenberger–Horne– Zeilinger proof, Foundations of Physics 29 (4) (1999) 615–630

[165] V. Vedral, A. Barenco, A. Ekert, Quantum networks for elementary arithmetic operations, Physical Review A 54 (1) (1996) 147–153.

[166] R. Vilela Mendes, The quantum ultimatum game, Quantum Information Processing 4 (2005) 1–12.

[167] M. Wei, G. Chen, J.B. Cruz, L. Hayes, M. Kruger, E. Blasch, Gametheoretic modeling and control of military operations with partially emotional civilian players, Decision Support Systems 44 (3) (2008) 565–579.

[168] R.F. Werner, Optimal cloning of pure states, Physical Review A 58 (3) (1998) 1827–1832.

[169] S. Wiesner, Conjugate coding, ACM SIGACT News 15 (1) (1983) 78–88.

[170] F.M.C. Witte, On pay-off induced quantum games, Working paper, arXiv:quant-ph/0208171v1, (2002).

[171] F.M.C. Witte, Quantum 2-player gambling and correlated pay-off, Physica Scripta 71 (2) (2005) 229–232

[172] W.K. Wootters, W.H. Zurek, A single quantum cannot be cloned, Nature 299 (1982) 802–803.

[173] J. Wu, A New Mathematical representation of game theory I, Workin paper, arXiv:quant-ph/0404159v5, (2004).

[174] J. Wu, Hamiltonian formalism of game theory, Working paper, arXiv: quant-ph/0501088, (2005).

[175] J. Wu, Theory of games on quantum objects, Working paper, arXiv: quant-ph/0503094, (2005).

[176] J. Yang, X. Hu, H. Zhang, Effects of a reputation feedback system on an online consumer-to-consumer auction market, Decision Support Systems 44 (1) (2007) 93-105.

[177] Y.S. Zhang, C.F. Li, W.L. Li, Y.F. Huang, G.C. Guo, Optical realization of quantum gambling machine, Working paper, arXiv:quant-ph/ 0001008v1, (2000).

Hong Guo is a Ph.D. student in the Department of Information Systems and Operations Management in the Warrington School of Business at the University of Florida. Her interests are in economics of information systems, computer-mediated social networks, quantum computing and quantum games.

Juheng Zhang is a Ph.D. student in the Department of Information Systems and Operations Management in the Warrington School of Business at the University of Florida. Her interests are in quantum computing and quantum games, real options, and economics of information systems.

Gary I. Koehler is the John B. Higdon Eminent Scholar of Management Information Systems at the University of Florida. He received his Ph. D. from Purdue University in 1974. He has held academic positions at Northwestern University and Purdue University and between 1979–1987 was a cofounder and CEO of a high-tech company which grew to over 260 employees during that period. His research interests are in areas formed by the intersection of the Operations Research, Arti<sup>fi</sup>cial Intelligence and Information Systems areas and include such areas as genetic algorithm theory, machine learning, e-commerce, quantum computing and decision support systems. He has published in journals including Management Science, Operations Research, Informs Journal on Computing, Evolutionary Computation, Decision Sciences, Decision Support Systems, the European Journal on Operational Research, the Journal of Management Information Systems, Information Systems and e-Business Management, SIAM Journal on Control and Optimization, Discrete Applied Mathematics, Journal of Finance, and others. He is an area editor for Decision Support System and is on several other editorial boards. He has served as an expert witness for many large firms (including AT&T). has been an External Examiner for several Universities and has worked under grants from IBM and the National Science Foundation.
