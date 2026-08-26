---
otero_id: 5620
otero_key: "83E6MREN"
title: "A novel hybrid share reporting strategy for blockchain miners in PPLNS pools"
authors: "Rui Qin; Yong Yuan; Fei-Yue Wang"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.01.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel hybrid share reporting strategy for blockchain miners in PPLNS pools

![](/api/attachments/83E6MREN/fulltext/images/e4f60c6d1486fef015f06a975c007690cf9965cb430f591d07211104756ec847.jpg)

Rui Qin<sup>a,b,f</sup>, Yong Yuan<sup>a,b,\*</sup>, Fei-Yue Wang<sup>a,b,c,d,e</sup>

<sup>a</sup> The State Key Laboratory for Management and Control of Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing, China <sup>b</sup> Qingdao Academy of Intelligent Industries, Qingdao, China

<sup>c</sup> Research Center of Military Computational Experiments and Parallel System, National University of Defense Technology, Changsha, China

<sup>d</sup> Institute of Systems Engineering, Macau University of Science and Technology, Macau, China

<sup>e</sup> University of Chinese Academy of Sciences, Beijing, China

<sup>f</sup> Beijing Engineering Research Center of Intelligent Systems and Technology, Institute of Automation, Chinese Academy of Sciences, Beijing, China

## A R T I C L E I N F O

Keywords: Share reporting strategy Blockchain mining PPLNS reward Pool mining Computational experiments approach

## A B S T R A C T

In blockchain pool mining, Pay-Per-Last-N-Shares (PPLNS) is one of the most commonly used reward mechanisms in practice, in which the mining pools will distribute the reward among the miners whose reported shares fall in the last N shares, according to the proportion of the number of shares of the miner in the last N shares. In the PPLNS mechanism, miners' reporting strategies may impose significant impacts to their rewards via determining the number of shares appeared in the last N shares. As such, how to strategically report their shares to the pool has become an important decision faced by miners. In this paper, we study the share reporting problem in PPLNS pools, and establish a share reporting model for a miner to optimize his/her rewards. We also propose a novel hybrid share reporting strategy for the miner based on our model, and design computational experiments to evaluate our hybrid share reporting strategy. The experimental results show that the hybrid strategy outperforms two baseline share reporting strategies commonly used in practice. This work is the first attempt to study the share reporting issue faced by miners in PPLNS pools. and it can provide important managerial insights for blockchain pool miners when making their share reporting decisions.

## 1. Introduction

Since the blockchain technology was invented in Bitcoin by Satoshi Nakamoto [10], blockchain mining has attracted a lot of participants to compete for the lucrative cryptocurrency rewards through contributing their computational power to the blockchain network [8,9,25]. Due to the desirable characteristics of the blockchain technology, it has raised many researchers' interests [1,6,21], and has been applied in many fields with success so far [3,17,20,22,27].

In blockchain mining, miners compete to solve the proof-of-work (PoW) based cryptographic puzzles with their computational power, and only the winning miner can create the next block and get the cryptocurrency reward, if the new block can be appended onto the blockchain ledger [18]. Since the cryptocurrency reward is extremely lucrative, blockchain mining has attracted more and more miners swarming into this new market, resulting in a sharp increase in the dificulty of finding new blocks. As such, miners may find it even harder to find a new block using the so-called solo mining scheme, which made pool mining more and more popular [4,5,7]. In pool mining, all the miners in the pool will aggregate their computational power together to mine the new block, leading to an increased winning probability for the mining pool. When a miner in the pool reports a new valid block, the pool operator broadcasts it to all the miners on the network, and receives a reward of one block from the network. After that, the pool will distribute the rewards to its miners according to the predefined reward mechanism.

Up till now, many reward mechanisms have been proposed based on the PoW consensus protocol, such as the proportional mechanism, payper-share (PPS), Slushes method, Geometric method and pay-per-last-Nshares (PPLNS) [15]. Among the above mechanisms, PPLNS mechanism is regarded as one of the most widely used mechanisms adopted by pool operators, which distributes the reward according to the last N shares reported by the miners [15,26].

For all mechanisms including PPLNS, incentive compatibility is a very important characteristic for the miners to behave truthfully in the mining pools. However, the PPLNS mechanism has been proved to be incentive incompatible since it does not satisfy the condition for judg ment of the incentive compatibility of a reward proposed by Schrijvers et al. [16]. As such, miners can increase their rewards through strategic behaviors such as delaying the reporting time of their found shares [26].

As can be seen in the PPLNS mechanism, only the last N shares are considered by the pool when it distributes the rewards among its miners. As such, the reporting order of the shares are of great importance, and if the shares reported by the miner are not in the last N shares, the miner can not get any reward from the pool. We call such issue as share reporting decision, and it has become an important problem faced by miners when they participate in mining with the PPLNS mechanism [12]. However, in the literature, the share reporting problem has not yet received suficient attention from researchers.

This paper aims to study the share reporting issue faced by the miners in PPLNS pools, and as far as we know, this work is the first attempt to study this issue. Based on the expected value of random variable [2,23], we establish a share reporting optimization model for the miners to maximize the expected reward of the miners, and propose a hybrid share reporting strategy for the miners based on the established model. We also design several experiments utilizing the computational experiment approach [11,13,19,28], to validate the efectiveness of the proposed new share reporting strategy, and the results show that our proposed share reporting strategy outperforms two baseline strategies.

The organization of the rest of this paper is as follows. Section 2 describes the process of blockchain mining and the PPLNS reward mechanism. In Section 3, we study the expected reward in two commonly used share reporting strategies. In Section 4, we introduce the research issue, and propose a share reporting optimization model. In Section 5, we evaluate our proposed share reporting strategy with computational experiment approach. In Section 6, we draw conclusions of our paper.

## 2. Blockchain mining pool and PPLNS mechanism

## 2.1. Pool mining

The notations used in this paper are listed in Table 1.

In a mining pool, miners cooperate with each other to solve a challenging cryptographic puzzle by contributing their hashing power to the pool. In each round of blockchain mining, a new block can be found. When the new block is confirmed, the pool can win the block reward from the blockchain system, as well as the associated transaction fees from the users [14].

![](/api/attachments/83E6MREN/fulltext/images/e2a92dee837165db3829d82239acaaf444d6daf5ac5a3fbf671ceafc1829daf8.jpg)  
Fig. 1. The mining process in the blockchain network.

The detailed blockchain mining process is shown in Fig. 1, and can be described as follows:

(1) The pool receives the cryptographic puzzle with dificulty $D _ { 1 }$ from the blockchain network.

(2) The pool determines a smaller dificulty $D _ { 2 } < D _ { 1 }$ for its miners considering the mining power of the miners, and distributes the same cryptographic puzzle but with dificulty $D _ { 2 }$ to its miners.

(3) Once receiving the puzzle from the pool, miners begin to seek for potential solutions satisfying the specified dificulty $D _ { 2 }$ with their computational power. Such solution is called a share, and it has a probability to be a valid solution. The miners submit the shares they found to the pool.

(4) When the pool receives a share satisfying dificulty $D _ { 1 } ,$ , it will broadcast it to the blockchain network.

(5) If the new block is confirmed by the network, the pool can win the reward of the block, as well as the transaction fees from the transactions packaged into the block.

(6) The pool distributes the block reward as well as the transaction fees among its miners according to the preset reward mechanism.

## 2.2. PPLNS mechanism

In blockchain mining, the mining pool needs to adopt a certain reward distribution mechanism to distribute the reward among its miners. Traditionally, the reward mechanism is important to both miners and the mining pools since it can greatly afect the rewards of the miners as well as the stability of the blockchain ecosystems. Up till now, many reward mechanisms have been proposed, such as the proportional mechanism, the PPS mechanism and the PPLNS mechanism, among others [15].

Among these reward mechanisms, PPLNS mechanism is widely adopted by mainstream pools. In PPLNS mechanism, the reward will be distributed to the miners whose submitted shares fall in the last N shares received by the pool.

Table 1

<table><tr><td>Notation</td><td>Descriptions</td></tr><tr><td>W</td><td>The total number of shares in each round</td></tr><tr><td>n</td><td>The number of shares submitted by the miner in each round, n = 2,3,⋯,W</td></tr><tr><td>L</td><td>The total number of rounds considered in the PPLNS mechanism</td></tr><tr><td>K</td><td>The number of blocks found by the pool in the L rounds, 0 ≤ K ≤ L</td></tr><tr><td>N</td><td>The value of N in the PPLNS mechanism, N = (l-1)W+j, j = 1,2,⋯,W, l = 1,2,⋯,L</td></tr><tr><td>i</td><td>Case i of the positions for the n shares in each round</td></tr><tr><td>pi</td><td>The probability of the n shares for case i under the Packaging Strategy</td></tr><tr><td>δ</td><td>The proportion of the reward reserved by the pool</td></tr><tr><td>R</td><td>The reward of the pool obtained from each block</td></tr><tr><td>s1</td><td>The Packaging Strategy</td></tr><tr><td>s2</td><td>The Random Strategy</td></tr><tr><td>vs1,N,n,i</td><td>The reward of the miner in case i under the Packaging Strategy</td></tr><tr><td>rs1,N,n,i</td><td>The reward proportion of the miner in the pool in case i under the Packaging Strategy</td></tr><tr><td>Vs1,N,n</td><td>The random reward of the miner under the Packaging Strategy</td></tr><tr><td>rs1,N,n</td><td>The random reward proportion of the miner in the pool under the Packaging Strategy</td></tr><tr><td>I(m1≤ j ≤ m2)</td><td>The indicator function</td></tr><tr><td>rs2,N,n</td><td>The random reward proportion of the miner in the pool under the Random Strategy</td></tr><tr><td>Vs2,N,n</td><td>The random reward of the miner under the Random Strategy</td></tr></table>

In the PPLNS pool, suppose the reward will be distributed after L rounds, and the reward for each block is fixed as R. If n shares of a miner fall in the last N shares, then the reward of the miner can be computed as

$$
V = \frac {n}{N} (1 - \delta) K R,\tag{1}
$$

where δ is the proportion of the reward reserved by the pool, and K is the number of blocks found by the pool, $0 \le K \le L$ . If all the blocks in the L rounds can be found by the pool, then we have $K = L$

## 2.3. Commonly used reporting strategies

As can be seen in the PPLNS mechanism, if a miner submitted a lot of shares to the pool, but none of them falls in the last N shares, then the miner can not get any reward from the pool. As such, the reporting strategy can significantly influence the rewards of a miner. Thus, how to formulate an appropriate share reporting strategy has become an important issue faced by the miners in pool mining. Due to the com plexity of the mining process of blockchain mining, we simplified our problem by focusing only on the share reporting process of the miners, but neglecting their mining process. In such case, we only need to consider the rewards of the miners under all possible positions of their shares.

As shown in Fig. 2, in the PPLNS pool, suppose the reward will be distributed after L rounds, according to the last N shares reported by the miners. For simplicity, we assume that in each round, there are exactly W shares, with the Wth share as a full solution. For the convenience of calculation, we can denote N as $\boldsymbol { N } = ( l - 1 ) \boldsymbol { W } + j , l = 1 , 2 , \cdots$ $, L , j = 1 , 2 , \cdots , W .$ For example, i $\mathbf { \nabla } \cdot N = W - 1$ , then $l = 1 , j = W - 1$ , and if $N = 2 W + 3 ,$ then $l = 3 , j = 3 .$

The reward for each block in these rounds keeps the same, denoted as $R ,$ and δ proportion of the reward will be reserved by the pool. In this paper, we consider the cases that there are multiple shares reported by the miner, $\mathrm { i . e . , }$ in the W shares of each round, there are exactly n shares reported by the miner, where $n \in \{ 2 , 3 , \cdots , W \}$ }. For simplicity, we always assume that the positions of the n shares keep the same in the L rounds.

As such, there are two feasible strategies to report his/her found shares to the pool for the miner, namely Packaging Strategy and Random Strategy, which can be described as follows:

• Packaging Strategy: In this strategy, the miner will report n shares simultaneously. For simplicity, we denote such strategy as $s _ { 1 } .$

• Random Strategy: In this strategy, the miner will report n shares randomly. For simplicity, we denote such strategy as $s _ { 2 } .$

## 3. Expected rewards in commonly used strategies

In pool mining, when formulating the share reporting strategies, the miner can not observe the reporting strategies of other miners. Thus, for each reporting strategy, there are multiple cases for the positions of the miner's shares, and the rewards of the miner under diferent cases may also difer. As such, we aim to optimize the miner's share reporting strategy, and propose a novel reporting strategy to maximize the expected rewards of the miner. In the following, we compute the expected rewards of the miner in the two strategies.

## 3.1. Expected rewards in Packaging Strategy

In the W shares of every round, n shares are submitted by the miner, where $2 \leq n < W .$ Moreover, the n shares are submitted to the pool simultaneously, and their positions in the W shares are random, with a probability $p _ { i }$ to be in the ith, $( i + 1 ) \mathrm { t h } , \cdots , ( i + n - 1 ) \mathrm { t h }$ positions. For simplicity, we assume that $\begin{array} { r } { p _ { i } = \frac { 1 } { W - n + 1 } } \end{array}$ for any case i, and the n shares are in the same positions in the L rounds. As such, there are $W - n + 1$ cases for the shares, and in case $i ,$ the shares appear in the $i \mathrm { t h } , ( i + 1 )$ ${ \mathrm { t h } , } \cdots { } , ( i + n - 1 ) \mathrm { t h }$ positions in each of the L rounds.

During the L rounds, the total rewards distributed to the miners by the pool are $( 1 - \delta ) K R ,$ , and the reward of the miner is

$$
v _ {s _ {1}, N, n, i} = r _ {s _ {1}, N, n, i} (1 - \delta) K R\tag{2}
$$

for case $i ,$ where $r _ { s _ { 1 } , N , n , i }$ for case i under any $N = ( l - 1 ) W + j , j = 1 , 2 , \cdots$ $, W , l = 1 , 2 , \cdots , L ,$ are given in Table $^ { 2 , }$ where n $\textstyle \bigwedge 3 = \operatorname* { m i n } \{ n , 3 \}$

According to Table $2 , r _ { s _ { 1 } , N , n , i }$ can be represented as

$$
r _ {s _ {1}, N, n, i} = \left\{ \begin{array}{c c} \frac {(l - 1) n}{N}, & 1 \leq i \leq W - j - n + 1, \\ & 1 \leq j \leq W - n \\ \frac {(l - 1) n + 1}{N}, & i = W - j - n + 2, \\ & 1 \leq j \leq W - n + 1 \\ \frac {(l - 1) n + 2}{N}, & i = W - j - n + 3, \\ & 2 \leq j \leq W - n + 2 \\ \vdots & \vdots \\ \frac {l n - 1}{N}, & i = W - j, \\ & n - 1 \leq j \leq W - 1 \\ \frac {l n}{N}, & W - j + 1 \leq i \leq W - n + 1, \\ & n \leq j \leq W, \end{array} \right.\tag{3}
$$

which is a discrete random variable, and its probability distribution is

![](/api/attachments/83E6MREN/fulltext/images/26e65899b779bac4df01891cee05db66e959837aa566c9581826f82398ccb413.jpg)  
Fig. 2. An illustration of the PPLNS mechanism.

The values of $r _ { s _ { 1 } , N , n , i }$ under diferent N in each case i.

$$
\begin{array}{c c c c c c c c c c} N & 1 & 2 & 3 & \dots & W & W + 1 & W + 2 & \dots & L W - 1 & L W \\ \hline \text {Case 1} & 0 & 0 & 0 & \dots & \frac {n}{W} & \frac {n}{W + 1} & \frac {n}{W + 2} & \dots & \frac {L n - 1}{L W - 1} & \frac {L n}{L W} \\ \text {Case 2} & 0 & 0 & 0 & \dots & \frac {n}{W} & \frac {n}{W + 1} & \frac {n}{W + 2} & \dots & \frac {L n}{L W - 1} & \frac {L n}{L W} \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ \text {Case (W - n - 1)} & 0 & 0 & \frac {1}{3} & \dots & \frac {n}{W} & \frac {n}{W + 1} & \frac {n}{W + 2} & \dots & \frac {L n}{L W - 1} & \frac {L n}{L W} \\ \text {Case (W - n)} & 0 & \frac {1}{2} & \frac {2}{3} & \dots & \frac {n}{W} & \frac {n}{W + 1} & \frac {n + 1}{W + 2} & \dots & \frac {L n}{L W - 1} & \frac {L n}{L W} \\ \text {Case (W - n + 1)} & 1 & \frac {2}{2} & \frac {n \wedge 3}{3} & \dots & \frac {n}{W} & \frac {n + 1}{W + 1} & \frac {n + 2}{W + 2} & \dots & \frac {L n}{L W - 1} & \frac {L n}{L W} \end{array}
$$

$$
r _ {s _ {1}, N, n} = \left\{ \begin{array}{c c} \frac {(l - 1) n}{N}, & \text {with probability} \frac {W - j - n + 1}{W - n + 1}, \\ & 1 \leq j \leq W - n \\ \frac {(l - 1) n + m}{N}, & \text {with probability} \frac {1}{W - n + 1}, \\ & m \leq j \leq W - n + m,   m = 1, 2, \dots , n - 1 \\ \frac {l n}{N}, & \text {with probability} \frac {j - n + 1}{W - n + 1}, \\ & n \leq j \leq W. \end{array} \right.\tag{4}
$$

Thus, the reward of the miner is

$$
V _ {s _ {1}, N, n} = r _ {s _ {1}, N, n} (1 - \delta) K R,\tag{5}
$$

which is also a discrete random variable, and the expected reward can be represented as

$$
\begin{array}{r l} E [ V _ {s _ {1}, N, n} ] = & \left(\frac {(l - 1) n}{N} \frac {W - j - n + 1}{W - n + 1} I (1 \leq j \leq W - n) \right. \\ & \left. + \frac {1}{W - n + 1} \sum_ {q = 1} ^ {n - 1} \frac {(l - 1) n + q}{N} I (q \leq j \leq W - n + q) \right. \\ & \left. + \frac {l n}{N} \frac {j - n + 1}{W - n + 1} I (n \leq j \leq W)\right) (1 - \delta) K R \\ = & E [ r _ {s _ {1}, N, n} ] (1 - \delta) K R, \end{array}\tag{6}
$$

where $I ( m _ { 1 } \leq j \leq m _ { 2 } )$ is an indicator function defined as follows:

$$
I (m _ {1} \leq j \leq m _ {2}) = \left\{ \begin{array}{l l} 1, & \text { if } \quad m _ {1} \leq j \leq m _ {2} \\ 0, & \text { other }. \end{array} \right.\tag{7}
$$

In the following theorem, we give the values of $E \left[ r _ { s _ { 1 } , N , n } \right]$ under diferent values of n. Theorem 1. For any $N = ( l - 1 ) W + j , l = 1 , 2 , \cdots , L , j = 1 , 2 , \cdots$ ,W, $\begin{array} { r } { i f n \le \frac { W } { 2 } , E \left[ r _ { s _ { 1 } , N , n } \right] } \end{array}$ can be represented as

$$
E \left[ r _ {s _ {1}, N, n} \right] = \left\{ \begin{array}{l l} \frac {(l - 1) n}{N} + \frac {j (j + 1)}{2 N (W - n + 1)}, & \text {if} 1 \leq j \leq n - 1 \\ \frac {(l - 1) n}{N} + \frac {n (2 j - n + 1)}{2 N (W - n + 1)}, & \text {if} n \leq j \leq W - n \\ \frac {l n}{N} - \frac {(W - j + 1) (W - j)}{2 N (W - n + 1)}, & \text {if} W - n + 1 \leq j \leq W - 1 \\ \frac {n}{W}, & \text {if} j = W, \end{array} \right.\tag{8}
$$

and $\displaystyle i f n > \frac { W } { 2 } , E [ r _ { s _ { 1 } , N , n } ]$ can be represented as

$$
E \left[ r _ {s _ {1}, N, n} \right] = \left\{ \begin{array}{l l} \frac {(l - 1) n}{N} + \frac {j (j + 1)}{2 N (W - n + 1)}, & \text {if} 1 \leq j \leq W - n \\ \frac {(l - 1) n}{N} + \frac {2 j - W + n}{2 N}, & \text {if} W - n + 1 \leq j \leq n - 1 \\ \frac {l n}{N} - \frac {(W - j + 1) (W - j)}{2 N (W - n + 1)}, & \text {if} n \leq j \leq W - 1 \\ \frac {n}{W}, & \text {if} j = W. \end{array} \right.\tag{9}
$$

Proof. We first compute the value of $E \left[ r _ { s _ { 1 } , N , n } \right]$ for $\begin{array} { r } { n \leq \frac { W } { 2 } , } \end{array}$ , and the expected reward for each j can be computed as follows.

When $j = 1 , 2 , \cdots , n - 1 ,$ , we have

$$
\begin{array}{r l} E [ r _ {s _ {1}, N, n} ] & = \frac {(l - 1) n}{N} \frac {W - j - n + 1}{W - n + 1} + \frac {1}{W - n + 1} \sum_ {q = 1} ^ {j} \frac {(l - 1) n + q}{N} \\ & = \frac {(l - 1) n}{N} + \frac {j (j + 1)}{2 N (W - n + 1)}. \end{array}\tag{10}
$$

Whe $\mid j = n , n + 1 , \cdots , W - n ,$ , we have

$$
\begin{array}{l} E [ r _ {s _ {1}, N, n} ] = \frac {(l - 1) n}{N} \frac {W - n - j + 1}{W - n + 1} + \frac {1}{W - n + 1} \sum_ {q = 1} ^ {n - 1} \frac {(l - 1) n + q}{N} \\ \qquad + \frac {l n}{N} \frac {j - n + 1}{W - n + 1} \\ \qquad = \frac {(l - 1) n}{N} + \frac {n (2 j - n + 1)}{2 N (W - n + 1)}. \end{array}\tag{11}
$$

Whe $\mid j = W - n + 1 , W - n + 2 , \cdots , W - 1$ , we have

$$
\begin{array}{l} E \left[ r _ {s _ {1}, N, n} \right] = \frac {1}{W - n + 1} \sum_ {q = j - W + n} ^ {n - 1} \frac {(l - 1) n + q}{N} + \frac {\ln}{N} \frac {j - n + 1}{W - n + 1} \\ = \frac {2 (l - 1) n (W - j) + (j - W + 2 n - 1) (W - j) + 2 \ln (j - n + 1)}{2 N (W - n + 1)} \\ = \frac {2 \ln (W - n + 1) - (W - j + 1) (W - j)}{2 N (W - n + 1)} \\ = \frac {\ln}{N} - \frac {(W - j + 1) (W - j)}{2 N (W - n + 1)}. \end{array}\tag{12}
$$

When j = W, we have

$$
E [ r _ {s _ {1}, N, n} ] = \frac {l n}{N} \frac {W - n + 1}{W - n + 1} = \frac {n}{W}.\tag{13}
$$

Thus, when n $\begin{array} { r } { \mathrm { ~  ~ \xi ~ } : \leq \frac { W } { 2 } , E \left[ r _ { s _ { 1 } , N , n } \right] } \end{array}$ can be represented as Eq. (8). Next, we compute the value of $E \left[ r _ { s _ { 1 } , N , n } \right]$ for $\begin{array} { r } { n > \frac { W } { 2 } } \end{array}$ , and the expected reward for each j can be computed as follows.

When $j = 1 , 2 , \cdots , W - n ,$ we have

$$
\begin{array}{r l} E [ r _ {s _ {1}, N, n} ] & = \frac {(l - 1) n}{N} \frac {W - j - n + 1}{W - n + 1} + \frac {1}{W - n + 1} \sum_ {q = 1} ^ {j} \frac {(l - 1) n + q}{N} \\ & = \frac {(l - 1) n}{N} + \frac {j (j + 1)}{2 N (W - n + 1)}. \end{array}\tag{14}
$$

$N \mathrm { h e n } j = W - n + 1 , W - n + 2 , \cdots , n - 1 ,$ we have

$$
\begin{array}{r l} E [ r _ {s _ {1}, N, n} ] & = \frac {1}{W - n + 1} \sum_ {q = j - W + n} ^ {j} \frac {(l - 1) n + q}{N} \\ & = \frac {2 (l - 1) n (W - n + 1) + (W - n + 1) (2 j - W + n)}{2 N (W - n + 1)} \\ & = \frac {(l - 1) n}{N} + \frac {(2 j - W + n)}{2 N}. \end{array}\tag{15}
$$

When $j = n , n + 1 , \cdots , W - 1$ , we have

$$
\begin{array}{l} E [ r _ {s _ {1}, N, n} ] = \frac {1}{W - n + 1} \sum_ {q = j - W + n} ^ {n - 1} \frac {(l - 1) n + q}{N} + \frac {l n}{N} \frac {j - n + 1}{W - n + 1} \\ = \frac {2 l n (W - n + 1) - (W - j + 1) (W - j)}{2 N (W - n + 1)} \\ = \frac {l n}{N} - \frac {(W - j + 1) (W - j)}{2 N (W - n + 1)}. \end{array}\tag{16}
$$

When $j = W ,$ we have

$$
E [ r _ {s _ {1}, N, n} ] = \frac {l n}{N} \frac {W - n + 1}{W - n + 1} = \frac {n}{W}.\tag{17}
$$

Thus, when $\begin{array} { r } { n > \frac { W } { 2 } , E \left[ r _ { s _ { 1 } , N , n } \right] } \end{array}$ can be represented as Eq. (9).

## 3.2. Expected rewards in Random Strategy

In this section, we compute the expected reward of the miner in Random Strategy.

For $N = ( l - 1 ) W + j , \ l = 1 , 2 , \cdots , L , \ j = 1 , 2 , \cdots , W , \ r _ { s _ { 2 } , N , n }$ can take $n + 1$ values, i.e., ${ \mathrm { , ~ } } { \frac { ( l - 1 ) n } { N } } , { \frac { ( l - 1 ) n + 1 } { N } } , \cdots { \mathrm { , ~ } } { \frac { l n } { N } }$ . In the following, we first discuss the probability for each case.

For the case of $\begin{array} { r } { r _ { s _ { 2 } , N , n } = \frac { ( l - 1 ) n } { N } } \end{array}$ , it means that none of the shares of the miner is in the last j shares of the $( L - l +$ 1)th round, i.e., the positions of the shares in the $( L - l +$ 1)th round could be chosen from $^ { 1 , 2 , \cdots }$ $, W - j .$ Thus, the probability of $\begin{array} { r } { r _ { s _ { 2 } , N , n } = \frac { ( l - 1 ) n } { N } } \end{array}$ can be computed by

$$
\operatorname * {P r} \left\{r _ {s _ {2}, N, n} = \frac {(l - 1) n}{N} \right\} = \frac {C _ {W - j} ^ {n}}{C _ {W} ^ {n}},\tag{18}
$$

where $n \leq W - j , \mathrm { i . e . , } 1 \leq j \leq W - n .$

For the case of $\begin{array} { r } { r _ { s _ { 2 } , N , n } = \frac { ( l - 1 ) n + m } { N } , ~ m = 1 , 2 , ~ \cdots , n - 1 , } \end{array}$ , it means that in the $( L - l + 1 ) \mathsf { t }$ h round, there are m shares for the miner in the last shares, and all the other $n - m$ shares are in the first $W - j$ shares. Thus, the probability of $\begin{array} { r } { r _ { s _ { 2 } , N , n } = \frac { ( l - 1 ) n + m } { N } } \end{array}$ can be computed by

$$
\operatorname * {P r} \left\{r _ {s _ {2}, N, n} = \frac {(l - 1) n + m}{N} \right\} = \frac {C _ {W - j} ^ {n - m} C _ {j} ^ {m}}{C _ {W} ^ {n}},\tag{19}
$$

where $n - m \le W - j$ and $m \leq j , \mathrm { i . e . , } m \leq j \leq W - n + m $

For the case of $\begin{array} { r } { r _ { s _ { 2 } , N , n } = \frac { l n } { N } . } \end{array}$ , it means that in the $( L - l + 1 ) \mathrm { t h }$ round, all the n shares for the miner are in the last j shares. Thus, the probability of $\begin{array} { r } { r _ { s _ { 2 } , N , n } = \frac { l n } { N } } \end{array}$ can be computed by

$$
\operatorname * {P r} \biggl \{r _ {s _ {2}, N, n} = \frac {l n}{N} \biggr \} = \frac {C _ {j} ^ {n}}{C _ {W} ^ {n}},\tag{20}
$$

where $n \leq j \leq W .$

Thus, $r _ { s _ { 2 } , N , n }$ can be represented as a random variable with the following distributions:

$$
r _ {s _ {2}, N, n} = \left\{ \begin{array}{c c} \frac {(l - 1) n}{N}, & \text {with probability} \frac {C _ {W - j} ^ {n}}{C _ {W} ^ {n}}, \\ & 1 \leq j \leq W - n \\ \frac {(l - 1) n + m}{N}, & \text {with probability} \frac {C _ {W - j} ^ {n - m} C _ {j} ^ {m}}{C _ {W} ^ {n}}, \\ & m \leq j \leq W - n + m, \\ & m = 1, \dots , n - 1 \\ \frac {l n}{N}, & \text {with probability} \frac {C _ {j} ^ {n}}{C _ {W} ^ {n}}, \\ & n \leq j \leq W. \end{array} \right.\tag{21}
$$

The expected value of $r _ { s _ { 2 } , N , n }$ can be computed by

$$
\begin{array}{l} E [ r _ {s _ {2}, N, n} ] = \frac {(l - 1) n}{N} \frac {C _ {W - j} ^ {n}}{C _ {W} ^ {n}} I (1 \leq j \leq W - n) \\ \quad + \sum_ {m = 1} ^ {n - 1} \frac {(l - 1) n + m}{N} \frac {C _ {W - j} ^ {n - m} C _ {j} ^ {m}}{C _ {W} ^ {n}} I (m \leq j \leq W - n + m) \\ \quad + \frac {\ln}{N} \frac {C _ {j} ^ {n}}{C _ {W} ^ {n}} I (n \leq j \leq W), \end{array}\tag{22}
$$

and thus the expected reward of the miner under Random Strategy is $E \left[ V _ { s _ { 2 , N , n } } \right] = E \left[ r _ { s _ { 2 , N , n } } \right] ( 1 - \delta ) K R$

In the following theorem, we give the value of $E \left[ r _ { s _ { 2 } , N , n } \right]$ in the Random Strategy.

Theorem 2. The expected value $o f r _ { s _ { 2 } , N , n }$ in the Random Strategy is

$$
E [ r _ {s _ {2}, N, n} ] = \frac {n}{W}.\tag{23}
$$

Proof. We only prove the case of n $\begin{array} { r } { \leq W - n , \mathrm { i . e . , } n \leq \frac { W } { 2 } } \end{array}$ , and the case of $\begin{array} { r } { n > \frac { W } { \lambda } } \end{array}$ can be proved in a similar way.

$\bar { \mathrm { W h e n } } j = 1 , 2 , \cdots , n - 1 ;$ , we have

$$
\begin{array}{r l} E [ r _ {s _ {2}, N, n} ] & = \frac {(l - 1) n}{N} \frac {C _ {W - j} ^ {n}}{C _ {W} ^ {n}} + \sum_ {m = 1} ^ {j} \frac {(l - 1) n + m}{N} \frac {C _ {W - j} ^ {n - m} C _ {j} ^ {m}}{C _ {W} ^ {n}} \\ & = \frac {(l - 1) n}{N} \frac {(C _ {W - j} ^ {n} + \sum_ {m = 1} ^ {j} C _ {W - j} ^ {n - m} C _ {j} ^ {m})}{C _ {W} ^ {n}} + \frac {1}{N} \sum_ {m = 1} ^ {j} \frac {m C _ {W - j} ^ {n - m} C _ {j} ^ {m}}{C _ {W} ^ {n}} \\ & = \frac {(l - 1) n}{N} \frac {C _ {W} ^ {n}}{C _ {W} ^ {n}} + \frac {j}{N} \frac {C _ {W - 1} ^ {n - 1}}{C _ {W} ^ {n}} \\ & = \frac {(l - 1) n}{N} + \frac {j n}{N W} \\ & = \frac {n}{W} \end{array}\tag{24}
$$

When $j = n , \cdots , W - n ,$ we have

$$
\begin{array}{r l} E [ r _ {s _ {2}, N, n} ] & = \frac {(l - 1) n}{N} \frac {C _ {W - j} ^ {n}}{C _ {W} ^ {n}} + \sum_ {m = 1} ^ {n - 1} \frac {(l - 1) n + m}{N} \frac {C _ {W - j} ^ {n - m} C _ {j} ^ {m}}{C _ {W} ^ {n}} + \frac {\ln}{N} \frac {C _ {j} ^ {n}}{C _ {W} ^ {n}} \\ & = \frac {(l - 1) n}{N} \frac {(C _ {W - j} ^ {n} + \sum_ {m = 1} ^ {n - 1} C _ {W - j} ^ {n - m} C _ {j} ^ {m} + C _ {W - j} ^ {0} C _ {j} ^ {n})}{C _ {W} ^ {n}} \\ & + \frac {1}{N} \sum_ {m = 1} ^ {n - 1} \frac {m C _ {W - j} ^ {n - m} C _ {j} ^ {m} + n C _ {W - j} ^ {0} C _ {j} ^ {n}}{C _ {W} ^ {n}} \\ & = \frac {(l - 1) n}{N} \frac {C _ {W} ^ {n}}{C _ {W} ^ {n}} + \frac {j}{N} \frac {C _ {W - 1} ^ {n - 1}}{C _ {W} ^ {n}} \\ & = \frac {(l - 1) n}{N} + \frac {j n}{N W} \\ & = \frac {n}{W} \end{array}\tag{25}
$$

Whe $\mathrm { ~  ~ \xi ~ } _ { \downarrow } j = W - n + 1 , \cdots , W - 1 ,$ , we have

$$
\begin{array}{r l} E [ r _ {s _ {2}, N, n} ] & = \sum_ {m = j - (W - n)} ^ {n - 1} \frac {(l - 1) n + m}{N} \frac {C _ {W - j} ^ {n - m} C _ {j} ^ {m}}{C _ {W} ^ {n}} + \frac {l n}{N} \frac {C _ {j} ^ {n}}{C _ {W} ^ {n}} \\ & = \frac {(l - 1) n}{N} \frac {\left(\sum_ {m = j - (W - n)} ^ {n - 1} C _ {W - j} ^ {n - m} C _ {j} ^ {m} + C _ {W - j} ^ {0} C _ {j} ^ {n}\right)}{C _ {W} ^ {n}} \\ & + \frac {1}{N} \sum_ {m = j - (W - n)} ^ {n - 1} \frac {m C _ {W - j} ^ {n - m} C _ {j} ^ {m} + n C _ {W - j} ^ {0} C _ {j} ^ {n}}{C _ {W} ^ {n}} \\ & = \frac {(l - 1) n}{N} \frac {C _ {W} ^ {n}}{C _ {W} ^ {n}} + \frac {j}{N} \frac {C _ {W - 1} ^ {n - 1}}{C _ {W} ^ {n}} \\ & = \frac {(l - 1) n}{N} + \frac {j n}{N W} \\ & = \frac {n}{W} \end{array}\tag{26}
$$

When $j = W ,$ we have

$$
E [ r _ {s _ {2}, N, n} ] = \frac {l n}{N} \frac {C _ {W} ^ {n}}{C _ {W} ^ {n}} = \frac {l n}{N} = \frac {n}{W}.\tag{27}
$$

Thus, we have

$$
E [ r _ {s _ {2}, N, n} ] = \frac {n}{W}\tag{28}
$$

## 4. Expected reward based optimal reporting strategy

## 4.1. Expected reward based model

In this section, we establish the following expectation model to optimize the miner's reporting decisions under diferent values of N

$$
\max _ {s \in \{s _ {1}, s _ {2} \}} E \left[ V _ {s, N, n} \right].\tag{29}
$$

In the following, we find the optimal strategies of model (29) under diferent N. We first compare the expected revenues in the two strategies, which can be given in the following theorem.

Theorem 3. For any W and $\begin{array} { r l r } { 2 } & { { } \le } & { n < W , } \end{array}$ whenj $< \frac { W } { 2 }$ , we haveE $[ r _ { s _ { 1 } , N , n } ] < E [ r _ { s _ { 2 } , N , n } ] \qquad ,$ when $\begin{array} { r } { \boldsymbol { j } = \frac { \boldsymbol { W } } { 2 } \qquad o r \qquad j = W , } \end{array}$ we haveE $[ r _ { s _ { 1 } , N , n } ] = E \left[ r _ { s _ { 2 } , N , n } \right]$ and whe $\begin{array} { r } { \imath \frac { W } { 2 } < j \leq W - 1 } \end{array}$ we haveE $[ r _ { s _ { 1 } , N , n } ] > E \left[ r _ { s _ { 2 } , N , n } \right]$

Proof. We first consider the case of $\begin{array} { r } { n \leq \frac { W } { 2 } , } \end{array}$

When $j = 1 , 2 , \cdots , n - 1$ , we have

$$
\begin{array}{l} E \left[ r _ {s _ {1}, N, n} \right] - E \left[ r _ {s _ {2}, N, n} \right] = \frac {(l - 1) n}{N} + \frac {j (j + 1)}{2 N (W - n + 1)} - \frac {n}{W} \\ = \frac {2 (l - 1) n W (W - n + 1) + j (j + 1) W - 2 N n (W - n + 1)}{2 W N (W - n + 1)} \\ = \frac {j (W j + W - 2 W n + 2 n ^ {2} - 2 n)}{2 W N (W - n + 1)} \\ \leq \frac {(n - 1) (W (n - 1) + W - 2 W n + 2 n ^ {2} - 2 n)}{2 W N (W - n + 1)} \\ = - \frac {n (n - 1) (W + 2 - 2 n)}{2 W N (W - n + 1)} \\ \leq - \frac {n (n - 1) (W + 2 - W)}{2 W N (W - n + 1)} \\ = - \frac {2 n (n - 1)}{2 W N (W - n + 1)} \\ <   0. \end{array}\tag{30}
$$

Thus, we have $E [ r _ { s _ { 1 } , N , n } ] < E [ r _ { s _ { 2 } , N , n } ] .$

When $j = n , n + 1 , \cdots , W - n ,$ , we have

$$
\begin{array}{r l} E [ r _ {s _ {1}, N, n} ] - E [ r _ {s _ {2}, N, n} ] & = \frac {(l - 1) n}{N} + \frac {n (2 j - n + 1)}{2 N (W - n + 1)} - \frac {n}{W} \\ & = \\ & \frac {2 (l - 1) W n (W - n + 1) + W n (2 j - n + 1) - 2 n N (W - n + 1)}{2 W N (W - n + 1)} \\ & = \\ & \frac {2 (N - j) n (W - n + 1) + W n (2 j - n + 1) - 2 n N (W - n + 1)}{2 W N (W - n + 1)} \\ & = \frac {n (n - 1) (2 j - W)}{2 W N (W - n + 1)}. \end{array}\tag{31}
$$

Thus, when $\begin{array} { r } { j < \frac { W } { 2 } , } \end{array}$ we have $E [ r _ { s _ { 1 } , N , n } ] < E [ r _ { s _ { 2 } , N , n } ] ,$ when $\begin{array} { r } { j = \frac { W } { 2 } , } \end{array}$ we have $E [ r _ { s _ { 1 } , N , n } ] = E [ r _ { s _ { 2 } , N , n } ] ,$ , and when $\begin{array} { r } { \frac { W } { 2 } < j \le W - 1 . } \end{array}$ , we have $E [ r _ { s _ { 1 } , N , n } ] > E [ r _ { s _ { 2 } , N , n } ] .$

Whe $\imath \textit { j } = W - n + 1 , W - n + 2 , \cdots , W - 1$ , we have

$$
\begin{array}{l} E \left[ r _ {s _ {1}, N, n} \right] - E \left[ r _ {s _ {2}, N, n} \right] = \frac {2 l n (W - n + 1) - (W - j + 1) (W - j)}{2 N (W - n + 1)} - \frac {n}{W} \\ = \\ \frac {2 l W n (W - n + 1) - W (W - j + 1) (W - j) - 2 n N (W - n + 1)}{2 N W (W - n + 1)} \\ \frac {2 n N (W - n + 1) + 2 n (W - j) (W - n + 1)}{2 N W (W - n + 1)} \\ = \frac {- W (W - j + 1) (W - j) - 2 n N (W - n + 1)}{2 N W (W - n + 1)} \\ = \frac {(W - j) (2 n (W - n + 1) - W (W - j + 1))}{2 N W (W - n + 1)} \\ \geq \frac {(W - j) (2 n \left(W - \frac {W}{2} + 1\right) - W (W - (W - n + 1) + 1))}{2 N W (W - n + 1)} \\ = \frac {2 n (W - j)}{2 N W (W - n + 1)} \\ > 0, \end{array}\tag{32}
$$

thus, we have $E [ r _ { s _ { 1 } , N , n } ] > E [ r _ { s _ { 2 } , N , n } ] .$

When $j = W ,$ we have $E [ r _ { s _ { 1 } , N , n } ] = E [ r _ { s _ { 2 } , N , n } ] .$

Therefore, the theorem has been demonstrated for $n \le W / 2$

In the following, we consider the case of $\begin{array} { r } { n > \frac { W } { 2 } } \end{array}$

When $j = 1 , 2 , \cdots , W - n ,$ we have

$$
\begin{array}{r l} E [ r _ {s _ {1}, N, n} ] - E [ r _ {s _ {2}, N, n} ] & = \frac {(l - 1) n}{N} + \frac {j (j + 1)}{2 N (W - n + 1)} - \frac {n}{W} \\ & = \frac {j (W j + W - 2 W n + 2 n ^ {2} - 2 n)}{2 W N (W - n + 1)} \\ & <   \frac {j (2 n j + 2 n - 2 W n + 2 n ^ {2} - 2 n)}{2 W N (W - n + 1)} \\ & = \frac {n j (j - W + n)}{W N (W - n + 1)} \\ & \leq \frac {n j ((W - n) - W + n)}{W N (W - n + 1)} \\ & = 0, \end{array}\tag{33}
$$

thus, we have $E [ r _ { s _ { 1 } , N , n } ] < E [ r _ { s _ { 2 } , N , n } ] .$

When $j = W - n + 1 , W - n + 2 , \cdots , n - 1 ,$ , we have

$$
\begin{array}{r l} E \left[ r _ {s _ {1}, N, n} \right] - E \left[ r _ {s _ {2}, N, n} \right] & = \frac {(l - 1) n}{N} + \frac {(2 j - W + n)}{2 N} - \frac {n}{W} \\ & = \frac {2 (l - 1) W n + (2 j - W + n) W - 2 N n}{2 W N} \\ & = \frac {2 (N - j) n + (2 j - W + n) W - 2 N n}{2 W N} \\ & = \frac {(2 j - W) (W - n)}{2 W N}. \end{array}\tag{34}
$$

Thus, when $\begin{array} { r } { j < \frac { W } { 2 } , } \end{array}$ , we have $E [ r _ { s _ { 1 } , N , n } ] < E [ r _ { s _ { 2 } , N , n } ] ,$ when $\begin{array} { r } { j = \frac { W } { 2 } , } \end{array}$ , we have $E [ r _ { s _ { 1 } , N , n } ] = E [ r _ { s _ { 2 } , N , n } ] ,$ and when $\begin{array} { r } { \frac { W } { 2 } < j \le W - 1 } \end{array}$ , we have $E [ r _ { s _ { 1 } , N , n } ] > E [ r _ { s _ { 2 } , N , n } ] .$

When $j = n , n + 1 , \cdots , W - 1$ , we have

![](/api/attachments/83E6MREN/fulltext/images/9c9d809337b13d5f25f3527e7957cc67283f75818d417124cdb2d49e8d4d89cc.jpg)  
n = 2

![](/api/attachments/83E6MREN/fulltext/images/522b3fe9302cbce306f23930b9d09dc2e007dc406c02be15128ae48c5a425f7f.jpg)  
n = 3

![](/api/attachments/83E6MREN/fulltext/images/ef8f50741f0680ccc95876b6e179ea5ace01239fa2bdbfa53486423fd9bc874b.jpg)  
n = 4

![](/api/attachments/83E6MREN/fulltext/images/4094cf1928797bb986da87c4e00b66c28e9927ebad594879d91b256857a6dd04.jpg)  
n = 5

![](/api/attachments/83E6MREN/fulltext/images/1252d8a15b352b824ef98cf003d819ed8dde89c119c497dc1742fd7d45c5397d.jpg)  
n = 6

![](/api/attachments/83E6MREN/fulltext/images/0d7da7a8f427136721297a1edac259970ee9967604d29d3f0a2006cdb9240948.jpg)  
n = 7

![](/api/attachments/83E6MREN/fulltext/images/c459cd806a20cb2c6d4ca235fe0e7d2e34555e5ac918c68c47d1757d4e6a63f2.jpg)  
n = 8

![](/api/attachments/83E6MREN/fulltext/images/b3aac6feaeabfc70e9d44dd893b3c735359754aa1bd8866554125a492caddb41.jpg)  
n = 9  
Fig. 3. Comparisons of $E [ r _ { s , N , n } ]$ for the three strategies under different values of n

$$
\begin{array}{r l} E [ r _ {s _ {1}, N, n} ] - E [ r _ {s _ {2}, N, n} ] & = \frac {2 l n (W - n + 1) - (W - j + 1) (W - j)}{2 N (W - n + 1)} - \frac {n}{W} \\ & = \frac {(W - j) (2 n (W - n + 1) - W (W - j + 1))}{2 N W (W - n + 1)} \\ & \geq \frac {(W - j) (2 n (W - n + 1) - W (W - n + 1))}{2 N W (W - n + 1)} \\ & = \frac {(W - j) (2 n - W) (W - n + 1)}{2 N W (W - n + 1)} \\ & > 0, \end{array}\tag{35}
$$

thus, we have $E [ r _ { s _ { 1 } , N , n } ] > E [ r _ { s _ { 2 } , N , n } ] .$

When $j = W ,$ we have $E [ r _ { s _ { 1 } , N , n } ^ { - } ] = E [ r _ { s _ { 2 } , N , n } ] .$

Therefore, the theorem has been demonstrated for $n > W / 2$

Based on Theorem 3, the optimal strategy can be given in the following theorem. Theorem 4. For any $\begin{array} { r } { N = ( l - 1 ) W + j } \end{array}$ and W, when1 $\leq j < { \frac { W } { 2 } }$ , the optimal strategy is Random Strategy, and when $\begin{array} { r } { \frac { W } { 2 } < j \leq W - 1 } \end{array}$ , the optimal strategy is Packing Strategy. $\begin{array} { r } { { v h e n } \boldsymbol { j } = \frac { W } { 2 } o r \boldsymbol { j } = \boldsymbol { W } , } \end{array}$ , both the two strategies are optimal.

## 4.2. The hybrid strategy

Based on Theorem $^ { 4 , }$ we propose a new share reporting strategy, which can be described as follows.

Definition 1 ([Hybrid Strategy]). For any $N = ( l - 1 ) W + j$ and $W ,$ when $\begin{array} { r } { 1 \leq j < \frac { W } { 2 } , } \end{array}$ , the Hybrid Strategy adopts Random Strategy, and when $\begin{array} { r } { \frac { W } { 2 } < j \le \mathbf { \bar { W } } - 1 } \end{array}$ , the Hybrid Strategy adopts Packing Strategy. When $\begin{array} { r } { j = \frac { W } { 2 } \thinspace \thinspace \mathrm { { o r } } \thinspace j = W , } \end{array}$ the Hybrid Strategy randomly adopts one of the two strategies.

According to Theorem 4, we can obtain the superiority of our proposed Hybrid Strategy, which can be given in the following corollary. Corollary 1. The expected reward of the miner in the Hybrid Strategy is higher than or equal to the expected rewards in both the Packing Strategy and Random Strategy.

## 4.3. An illustrative example

In this section, we present an example to illustrate our proposed hybrid strategy. Suppose a miner participates in a mining pool adopting PPLNS mechanism. The pool will distribute the rewards after $L = 3$ rounds, where $K = 3$ blocks can be found by the pool, and in each round, there are $W = 1 0$ shares, in which n shares are found by the miner. As such, N can take the values of $^ { 1 , 2 , \cdots , 3 0 }$ . Suppose the pro portion of the service fees reserved by the pool is fixed as δ. Then the expected reward of the three strategies can be represented as

$$
E \left[ V _ {s, N, n} \right] = E \left[ r _ {s, N, n} \right] 3 (1 - \delta) R,
$$

and comparisons of $E [ r _ { s , N , n } ]$ for the three strategies under diferent values of $n \in \{ 2 , 3 , \cdots , 1 0 \}$ are given in Fig. 3.

Fig. 3 confirms the superiority of our proposed hybrid strategy.

## 5. Computational experiments

In this section, we will validate the efectiveness of our proposed hybrid strategy for the miner in PPLNS pools with the computational experiments approach [24]. For comparison purpose, we adopt Packaging Strategy and Random Strategy as two baseline strategies.

## 5.1. Experimental scenario

In our experiment, we consider that a miner is mining in a pool adopted PPLNS mechanism. We run large numbers of experiments with randomly generated values of the parameters $W , L ,$ n and K. According to these experiments, we can see that all these experiments can validate our proposed strategy. Therefore, without loss of generality, we randomly select one experiment as an illustrative example to analyze our experiment results.

In the pool, each round contains $W = 1 0$ shares, in which $n = 4$ shares are found by the miner, and the pool will distribute the rewards among its miners after $L = 3$ rounds, according to the last N shares submitted to the pool, where N can take the values of $^ { 1 , 2 , 3 , \cdots , 3 0 }$ , and $K = 3$ blocks can be found by the pool. For each feasible N, there are 7 cases and 210 cases for the positions of the 4 shares of the miner in the Packaging strategy and Random Strategy, respectively, and these cases are shown in Figs. 4–5. Moreover, we assume that the reward is the same for each block, and the pool keeps a fixed proportion of the service fees.

## 5.2. Results and analysis

Without loss of generality, we run 10,000 independent experiments for each $N ,$ and the distribution of each case in the Packaging Strategy and the Random Strategy are given in Fig. 6.

According to Eqs. (4) and (21), in all possible cases of positions for the 4 shares shown in Fig. 6, there are 5 cases of rewards for each $N = 1 0 ( l - 1 ) + j$ in the Packaging Strategy and the Random Strategy, denoted as

• Case $\begin{array} { r } { \mathrm { r } ; r = \frac { 4 ( l - 1 ) } { N } , j = 1 , 2 , \cdots , 6 . } \end{array}$

• Case $\begin{array} { r } { \mathrm { I I } \colon r = \frac { 4 ( l - 1 ) + 1 } { N } , j = 1 , 2 , \cdots , 7 . } \end{array}$

Case III: $\begin{array} { r } { r = \frac { 4 ( l - 1 ) + 2 } { N } , j = 2 , 3 , \cdots , 8 . } \end{array}$

• Case $\begin{array} { r } { \mathrm { I V } ; r = \frac { 4 ( l - 1 ) + 3 } { N } , j = 3 , 4 , \cdots , 9 . } \end{array}$

• Case $\begin{array} { r } { \mathrm { V } \mathrm { : } r = \frac { 4 l } { N } , j = 4 , 5 , \cdots , 1 0 . } \end{array}$

The number of times for the five cases of the rewards in the 10,000 experiments for Packaging Strategy and Random Strategy are shown in Fig. 7.

With our proposed model, we can obtain our proposed new share reporting strategies for the miner under diferent N, as shown in Fig. 8, and comparisons of the proportion of the average reward for our new Hybrid Strategy with Packaging Strategy and Random Strategy under diferent N are given in $\mathrm { F i g . ~ } 9 .$

From Figs. 6 to 9, we can draw the following conclusions:

(1) In Packaging Strategy, the number of times for each of the five cases

![](/api/attachments/83E6MREN/fulltext/images/e2fc638f611dd2f2081c0a0aa962cf0544c9f7a0689967dd8de879bb6eb396c4.jpg)  
Fig. 4. 7 possible cases for Packaging Strategy.

![](/api/attachments/83E6MREN/fulltext/images/5a2f2ed7f6cc1f506b64a6a7e34e9b971856145e4fdcd4a06c8a4c7162cfbf6e.jpg)  
Cases 1-70 for Random Strategy

![](/api/attachments/83E6MREN/fulltext/images/64e619d073d149e892ce89fd5baa529d2037198f3e41bdb20ee14aa46e69f070.jpg)  
Cases 71-140 for Random Strategy

![](/api/attachments/83E6MREN/fulltext/images/e3f14b5015a8de36d0f1c6416af6ecf39491575132bd1ae0a75dd4531778d081.jpg)  
Cases 141-210 for Random Strategy  
Fig. 5. The 210 possible cases for Random Strategy.

![](/api/attachments/83E6MREN/fulltext/images/b5bc53fdd2d91596b35fc7e3777e207f383ac5e017e5e6783e68e9950c2db975.jpg)

Packaging Strategy  
![](/api/attachments/83E6MREN/fulltext/images/fbb6fd5442c80c82bbbdee6ac8e008ec13b3dc6ea6ee94fbf4dbb1a2ed778ecb.jpg)  
Random Strategy  
Fig. 6. The number of times for the possible cases in the 10,000 experiments in Packaging Strategy and Random Strategy.

are the same for the same j. Specifically, the largest number of times for the five cases are 8586, 1474, 1476, 1476 and 10,000, occurring at j = 1, j = 7, j = 7, j = 8 and j = 10, respectively.

(2) In Random Strategy, the number of times for each of the five cases are the same for the same j. Specifically, the largest number of times for the five cases are 5952, 5393, 4746, 5283 and 10,000, occurring at j = 1, j = 2, j = 4, j = 8 and j = 10, respectively.

(3) Our proposed hybrid strategy is to adopt the random reporting strategy for N = 1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24, and the packaging reporting strategy for N = 6, 7, 8, 9, 16, 17, 18, 19, 26, 27, 28, 29. For N = 5, 10, 15, 20, 25, 30, our new strategy adopts either the Packaging Strategy or the Random Strategy.

(4) For each $N ,$ our new strategy can get a reward which is higher than or equal to that in the Packaging Strategy, which illustrates that our proposed new strategy is better than the Packaging Strategy.

(5) For each $N ,$ our new strategy can get a reward which is higher than or equal to that in the Random Strategy, which illustrates that our proposed new strategy is better than the Random Strategy.

(6) Comparing the rewards of diferent $N = 1 0 ( l - 1 ) + j , l = 1 , 2 , 3 ,$ with the same $j ,$ we can obtain that the reward of the miner is non increasing with the increasing of l. The possible reason is that with the increasing of l, N is approaching LW, and the efect of the strategic behavior of the miner becomes smaller.

![](/api/attachments/83E6MREN/fulltext/images/c94fde4048fa5ef395412433c95e856629f130f105c0398df454cda0ad35bd9d.jpg)  
Packaging strategy

![](/api/attachments/83E6MREN/fulltext/images/a5a68a8dffa1041670c674cc68bb57e5fd5d45a99c61394fcab46a1d443ad219.jpg)  
Random strategy

Fig. 7. The number of times for the five cases of reward in the 10,000 ex periments for the Packaging Strategy and Random Strategy.  
![](/api/attachments/83E6MREN/fulltext/images/bbfb8b33aa593e2b6382e8971be328a2ca4cca0e9c4b59b32513171351558a24.jpg)  
Fig. 8. Our proposed new reporting strategies for the miner under diferent N.

![](/api/attachments/83E6MREN/fulltext/images/4211dc68e9d97216f352e2da04350cacfe3ecb69443acde37093e76458777dce.jpg)  
Fig. 9. Comparisons of the proportion of the average rewards for the three strategies under diferent N.

## 6. Conclusions and future work

In this work, we mainly studied the share reporting issues faced by the miners in mining pools adopted the PPLNS reward mechanism. Considering that the share reporting strategy can greatly afect the rewards of the miners, we established a share reporting optimization model for the miners in PPLNS mining pools, which can help the miners find their optimal share reporting strategies under diferent values of N. Based on the established model, we propose a hybrid share reporting strategy. We also designed computational experiments to validate our proposed share reporting strategy, and the results showed that our proposed hybrid share reporting strategy outperforms two strategies commonly used in practice. Our work can provide important managerial insights for miners participating in PPLNS pools when making their share reporting decisions. Specifically, the optimal strategies of the miners can not be influenced by the values of n, but can be greatly influenced by the values of N. As such, the miners should formulate their share reporting strategies on the values of N.

In the future, we intend to extend this work according to the following aspects: 1) Studying the share reporting strategies in the case that both the number of shares of the miner and the total shares in a round can vary; b) Exploring the joint optimization strategy of pool selection and share reporting for the miners when there are multiple pools with diferent reward mechanisms.

## Acknowledgments

This work is partially supported by the National Natural Science Foundation of China (71702182, 71472174, 61533019, 71232006).

## References

[1] K. Alabi, Digital blockchain networks appear to be following Metcalfe's Law, Electronic Commerce Research and Applications 24 (2017) 23–29.

[2] M. Boncompte, The expected value of perfect information in unrepeatable decision: making, Decision Support Systems 110 (2018) 11–19.

[3] G. Chen, P. Goes, H.J. Wang, O. Wei, J.L. Zhao, Guest editorial: business applications of web of things, Decision Support Systems 63 (2014) 1–2.

[4] I. Eval, The miner's dilemma, Proceedings of the 2015 IEEE Symposium on Security and Privacy. 2015. pp. 89–103

[5] B. Fisch, R. Pass, A. Shelat, Socially optimal mining pools, Proceedings of 13Th International Conference Web and Internet Economics, 2017, pp. 205–218.

Rui Qin received her B.S., M.S. degrees in mathematics and applied mathematics, operational research and cybernetics from Hebei University, in 2007 and 2010, respectively, and received her Ph.D. degree in computer application technology from the University of Chinese Academy of Sciences, in 2016. She is currently an Assistant Professor with the

[6] F. Hawlitschek, B. Notheisen, T. Teubner, The limits of trust-free systems: a literature review on blockchain technology and trust in the sharing economy, Electronic Commerce Research and Applications 29 (2018) 50–63

[7] A. Laszka, B. Johnson, J. Grossklags, When bitcoin mining pools run dry, Lecture Notes in Computer Science 8976 (2015) 63–77.

[8] X. Li, C.A. Wang, The technology and economic determinants of cryptocurrency exchange rates: the case of Bitcoin, Decision Support Systems 95 (2017) 49–60.

[9] X. Liu, W. Wang, D. Niyato, N. Zhao, P. Wang, Evolutionary game for mining pool selection in blockchain networks, IEEE Wireless Communications Letters 7 (5) (2018) 760–763.

[10] S. Nakamoto, Bitcoin: a peer-to-peer electronic cash system, Tech. Rep. 2008

[11] R. Qin, Y. Yuan, F.Y. Wang, Exploring the optimal granularity for market segmentation in RTB advertising via computational experiment approach, Electronic Commerce Research and Applications 24 (2017) 68–83.

[12] R. Qin, Y. Yuan, F.Y. Wang, Optimal share reporting strategies for blockchain miners in PPLNS pools, Proceedings of the IEEE International Conference on Systems, Man, and Cybernetics, 2018, pp. 3357–3362

[13] R. Qin, Y. Yuan, F.Y. Wang, A Pareto optimal mechanism for demand-side platforms in real time bidding advertising markets, Information Sciences 469 (2018) 119–140.

[14] R. Qin, Y. Yuan, F.Y. Wang, Research on the selection strategies of blockchain mining pools, IEEE Transactions on Computational Social Systems 5 (3) (2018) 748–757.

[15] M. Rosenfeld, Analysis of bitcoin pooled mining reward systems, arXiv preprint, 2011. arXiv:1112.4980.

[16] O. Schriivers, J. Bonneau, D. Boneh, T. Roughgarden, Incentive compatibility of bitcoin mining pool reward functions, Proceedings of the International Conference on Financial Cryptography and Data Security, 2016, pp. 477–498.

[17] J.J. Sikorski, J. Haughton, M. Kraft, Blockchain technology in the chemical industry: machine-to-machine electricity market, Applied Energy 195 (2017) 234-246.

[18] D.K. Tosh, S. Shetty, X. Liang, C.A. Kamhoua, K.A. Kwiat, L. Njilla, Security implications of blockchain cloud with analysis of block withholding attack, Proceedings of the 17Th IEEE/ACM International Symposium on Cluster Cloud and Grid Computing, 2017, pp. 458–467.

[19] D. Wen, Y. Yuan, X. Li, Artificial societies, computational experiments, and parallel systems: an investigation on a computational theory for complex socioeconomic systems, IEEE Transactions on Services Computing 6 (2) (2013) 177–185.

[20] S. Wang, J. Wang, X. Wang, T. Qiu, Y. Yuan, L. Ouyang, Y. Guo, F.Y. Wang, Blockchain-powered parallel healthcare systems based on the ACP approach, IEEE Transactions on Computational Social Systems 5 (4) (2018) 942–950

[21] F.Y. Wang, Y. Yuan, C. Rong, J.J. Zhang, Parallel blockchain: an architecture for CPSS-based smart societies, IEEE Transactions on Computational Social Systems 5 (2) (2018) 303–310

[22] F.Y. Wang, Y. Yuan, J. Zhang, R. Qin, M.H. Smith, Blockchainized internet of minds: a new opportunity for cyber-physical-social systems, IEEE Transactions on Computational Social Systems 5 (4) (2018) 897–906

[23] D. Yang, X.H. Li, R.J. Jiao, B. Wang, Decision support to product configuration considering component replenishment uncertainty: a stochastic programming ap proach, Decision Support Systems 105 (2018) 108–118.

[24] Y. Yuan. D. Zeng, Co-evolution-based mechanism design for sponsored search advertising, Electronic Commerce Research and Applications 11 (6) (2012) 537–547

[25] Y. Yuan, F.Y. Wang, Blockchain and cryptocurrencies: model, techniques and ap plications. JEEE Transactions on Systems Man, and Cybernetics: Systems 48 (9) (2018)1421-1428

[26] Y. Zolotavkin, J. García, C. Rudolph, Incentive compatibility of pay per last N shares in bitcoin mining pools, International Conference on Decision and Game Theory for Security, 2017, pp. 21–39.

[27] Y. Zhang, J. Wen, The IoT electric business model: using blockchain technology for the internet of things, Peer-to-Peer Networking and Applications 10 (4) (2017) 983-994.

[28] J. Zhang, Y. Yang, X. Li, R. Qin, D. Zeng, Dynamic dual adjustment of daily budgets and bids in sponsored search auctions, Decision Support Systems 57 (2014) 105-114.

State Key Laboratory for Management and Control of Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing, China. She is also with the Qingdao Academy of Intelligent Industries, Qingdao, China.

Dr. Qin's research interests include blockchain, social computing, computational advertising and parallel management. Currently, Dr. Qin is the Associate Director of the CAA (Chinese Association of Automation) Technical Committee of Blockchain.

Yong Yuan received his B.S., M.S., and Ph.D. degrees in computer software and theory from the Shandong University of Science and Technology, Shandong, China, in 2001, 2004, and 2008, respectively. He is an Associate Professor at the State Key Laboratory for Management and Control of Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing, China, and he is the Vice President of the Qingdao Academy of Intelligent Industries. Oingdao. China

Dr. Yuan's research interests include blockchain, cryptocurrency and smart contract. He has authored over 90 papers published in academic journals and conferences. Currently. Dr. Yuan is the Associate Editor of IEEE Transactions on Computational Social Systems, and also Associate Editor of ACTA Automatica Sinica, He is a Senior Member of IEEE, and the Chair of IEEE Council on RFID Technical Committee on Blockchain. Co-chair of JEEE SMC Technical Committee on Blockchain, and also Director of the CAA (Chinese Association of Automation) Technical Committee of Blockchain. Dr. Yuan is the Secretary-general of IEEE SMC Technical Committee on Social Computing and Social Intelligence, Vice Chair of IFAC Technical Committee on Economic, Business and Financial Systems (TC 9.1), Chair of ACM Beijing Chapter on Social and Economic Computing. Dr. Yuan is also the Secretary-general of CAAI (Chinese Association of Artificial Intelligence) Technical Committee on Social Computing and Social Intelligence, Vice Director and Secretary-general of CAM (Chinese Academy of Management) Technical Committee on Parallel Management.

Fei-Yue Wang received the Ph.D. degree in computer and systems engineering from Rensselaer Polytechnic Institute, Troy, NY, USA, in 1990. He joined the University of Arizona, Tucson. AZ, USA, in 1990. and became a Professor and the Director of the Robotics and Automation Laboratory and the Program in Advanced Research for Complex Systems. In 1999, he founded the Intelligent Control and Systems Engineering Center, Institute of Automation, Chinese Academy of Sciences (CAS), Beijing, China, under the support of the Outstanding Overseas Chinese Talents Program from the State Planning Council and “100 Talent Program" from CAS. In 2002, he joined the Lab of Complex Systems and Intelligence Science, CAS, as the Director, where he was the Vice President for Research. Education, and Academic Exchanges with the Institute of Automation from 2006 to 2010. In 2011, he was named as the State Specially Appointed Expert and Director of the State Key Laboratory for Management and Control of Complex Systems, Beijing, China. His current research interests include methods and applications for par allel systems, social computing, parallel intelligence, and knowledge automation.

Dr. Wang has been the general or program chair of more than 30 IEEE, INFORMS, ACM, and ASME conferences. He was the President of the JEEE ITS Society during 2005–2007. the Chinese Association for Science and Technology, USA, in 2005, and the American Zhu Kezhen Education Foundation during 2007–2008. He was the Vice President of the ACM China Council during 2010–2011, and chair of IFAC TC on Economic and Social Systems from 2008–2011. Currently, he is the President-Elect of IEEE Council on RFID. Since 20o8. he has been the Vice President and the Secretary General of the Chinese Association of Automation. He was the Founding Editor-in-Chief of the International Journal of Intelligent Control and Systems during 1995–2000 and the IEEE ITS Magazine during 2006–2007. He was the EiC of the IEEE Intelligent Systems during 2009–2012 and the JEEE Transactions on ITS during 2009–2016. He is currently the EiC of the JEEE Transactions on Computational Social Systems, and the Founding EiC of the IEEE/CAA Journal of Automatica Sinica and the Chinese Journal of Command and Control. He was elected as a fellow of INCOSE, IFAC, ASME, and AAAS. In 2007, he was a recipient of the National Prize in Natural Sciences of China and was awarded the Outstanding Scientist by ACM for his research contributions in intelligent control and social computing. He was a recipient of the IEEE Intelligent Transporation Systems (ITS) Outstanding Application and Research Awards in 2009. 2011, and 2015. and the JEEE SMC Norbert Wiener Award ir 2014.
