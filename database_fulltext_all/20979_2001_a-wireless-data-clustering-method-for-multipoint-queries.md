---
otero_id: 20979
otero_key: "QGEW9EJ4"
title: "A wireless data clustering method for multipoint queries"
authors: "Yon Dohn Chung; Myoung Ho Kim"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00145-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A wireless data clustering method for multipoint queries

Yon Dohn Chung <sup>)</sup>, Myoung Ho Kim

DiÕision of Computer Science, Department of Electrical Engineering and Computer Science, Korea AdÕanced Institute of Science and Technology KAIST , 373-1 Kusung-dong, Yusung-gu, Taejon 305-701, South Korea( )

## Abstract

By effective data clustering, the mobile clients can access the data objects of their interest in short latency. In this paper, we propose a clustering method of wireless data for multipoint queries, where wireless data objects are uniformly broadcasted.

We first analyze the data clustering problem and propose a new measure, named the Query Distance, i.e., convenient to manipulate for the analyses of the average query performance. Then, we propose a clustering method that efficiently minimizes the Query Distance, based on the Gray coding scheme. We show that the Gray coding scheme has useful properties that can be utilized for clustering the data on the air. We also show the performance advantage of our method through experiments. Since, as far as we are aware of, there is no previous work that deals with multipoint queries in wireless data broadcasting, the experiments are in comparison with the random clustering method. q 2001 Published by Elsevier Science B.V.

Keywords: Data clustering; Gray codes; Wireless data broadcasting; Wireless information systems; Mobile computing

## 1. Introduction

Data broadcasting in wireless information systems has many applications because it provides the energy efficiency on the mobile clients and the bandwidth efficiency on the wireless channel 6 .<sup>w</sup> <sup>x</sup> AStock Price BroadcastingB and ATraffic Information BroadcastingB can be typical examples of wireless data broadcasting.

There are two important parameters related with wireless data broadcasting. These are the access time <sup>w</sup> <sup>x</sup> <sup>w x</sup> 1,2,10 and the tuning time 3,7 . The access time is the amount of time elapsed from the moment a client submits a query to the receipt of relevant data on the broadcast channel. The tuning time is the amount of time spent by a client’s listening to the channel. In this paper, we focus on reducing clients’ access time by efficient organization of wireless broadcast data.

There have been some studies on the efficient organization of the broadcast data stream 1,2,10 .<sup>w</sup> <sup>x</sup> The Broadcast Disks’ 1,2 approach analyzes the<sup>w</sup> <sup>x</sup> access preference of each data object and differentiates the delivery frequencies of data objects. That is, the more popular data objects are more frequently broadcasted. While this way of broadcasting gives an advantage for the queries that ask for frequently accessed data, it gives a disadvantage for other queries due to the increase of the broadcast cycle. In other words, the lengthy cycle causes the average access time for queries accessing less popular data objects to increase. The scheduling method in Ref.

![](/api/attachments/QGEW9EJ4/fulltext/images/b785aed181e4faaf4733427d97ded068ce80eab4ebbdabf9939caa51f85c248a.jpg)  
Fig. 1. A multipoint query on the wireless broadcast.

<sup>w</sup> <sup>x</sup> 10 constructs the broadcast schedule by using the stochastic model. It considers the access frequencies of data objects and controls their delivery intervals. However, all these approaches considered the case that a query accesses only one data object, and did not consider the case for a multipoint query, i.e., a query accessing more than one data object.

In this paper, we mainly focus on effective data clustering of wireless broadcast data for multipoint queries so that the mobile clients can access the data on the air in a short access time. Fig. 1 illustrates how a multipoint query retrieves the broadcast data, where the set of data objects in one broadcast cycle commonly called bcast is $\{ d _ { 1 } , d _ { 2 } , d _ { 3 } , d _ { 4 } , d _ { 5 } \}$ . This bcast is repeatedly broadcasted to unspecified number of clients. It is assumed in this paper that data broadcasting is uniform, which means that a data object is not replicated within one bcast.

Suppose a client issues a multipoint query retrieving $d _ { 1 }$ and $d _ { 4 }$ . In Fig. 1, the client has to wait for the next bcast because $d _ { 1 }$ has passed over at the time when the client’s query is issued. However, if the order of the data in the current bcast is $\langle d _ { 2 } , d _ { 3 } , d _ { 1 }$ $d _ { 4 } , d _ { 5 } \rangle$ , then the client can retrieve $d _ { 1 }$ and $d _ { 4 }$ in the current bcast. This implies that how to cluster the broadcast data is important to the access time of the mobile query.

The rest of the paper is organized as follows. In Section 2, we present the problem definition and propose a new measure called the Query Distance for wireless data clustering. Based on the measure, we propose a data clustering method using Gray codes in Section 3. We explain the concept of Gray codes and describe our method with some examples.

The useful properties of Gray codes for our clustering problem are also discussed in this section. In Section 4, we present the results of performance evaluation. We conclude the paper with some directions for further work in the last section.

## 2. Problem and measure definition

## 2.1. Wireless data clustering problem

We first explain some relevant notation that will be used throughout the paper. The data object is denoted by $d _ { i } ,$ and $\mid d _ { i } \mid$ is the size of $d _ { i }$ . The set of data in a bcast is denoted by $\mathcal { D } .$ , and the size of one bcast is denoted by B. Thus, in this paper, B is equal to $\Sigma \mid d _ { i } \mid , \forall d _ { i } \in \mathcal { D }$ because uniform broadcasting is assumed. We use the symbol $q _ { i }$ for the query and $\mathcal { Q }$ for the set of queries. $D ( q _ { i } )$ denotes the set of data accessed by $q _ { i } ,$ , and freqŽ . q denotes the frequency of $q _ { i } .$ The broadcast schedule denoted by $\sigma$ is the broadcasting sequence of data with angle brackets at both ends. For example, for the bcast in Fig. 1 is $\langle d _ { 1 } , d _ { 2 } , d _ { 3 } , d _ { 4 } , d _ { 5 } \rangle$

Fig. 2 shows a placement of the data set of query $q _ { i } , \ \mathrm { i . e . , } D ( q _ { i } )$ . Here, $D ( q _ { i } ) = \{ d _ { i 1 } , ~ d _ { i 2 } , ~ \cdot ~ \cdot ~ \cdot ~ , ~ d _ { i k } \}$ where k is the number of data objects that $q _ { i }$ accesses. The distance between two data objects $d _ { i j }$ and $d _ { i ( j + 1 ) }$ is denoted by $\delta _ { i j }$ . Note that since the data objects are on the air, the distance has the same semantics as the length of time.

Suppose $\operatorname { A T } ^ { \mathrm { a v g } } ( q _ { i } , \sigma )$ is the average access time of $q _ { i }$ in $\sigma .$ . Then, the data clustering problem for wireless broadcasting is to find a broadcast schedule $\sigma$ that minimizes the total access time TAT , de-Ž . noted by:

$$
\mathrm{TAT} (\sigma) = \sum_ {q i \in \mathscr {Q}} \mathrm{AT} ^ {\text { avg }} (q _ {i}, \sigma) \times \operatorname{freq} (q _ {i}),
$$

The access time of each query varies depending on the start time of the query as illustrated in Fig. 1. It is shown in Appendix A that the average access time of a query has a form of the quadratic equation as follows:

![](/api/attachments/QGEW9EJ4/fulltext/images/9a8af0bb442db1d205e9777be3995e7648e068d9cccf6dcb61a50135c6e74de6.jpg)  
Fig. 2. Placement of a query data set $D ( q _ { i } )$ .

$$
\mathrm{AT} ^ {\text { avg }} \left(q _ {i}, \sigma\right) = \sum_ {q _ {i} \in \mathscr {Q}} \left(B - \frac {1}{2 B} \sum_ {j = 1} ^ {k} \left(\delta_ {i j}\right) ^ {2}\right).
$$

## 2.2. Measure definition

While the average access time $\operatorname { A T } ^ { \mathrm { a v g } } ( q _ { i } , \sigma )$ is an intuitive measure for the performance of a query, it is too complex to manipulate by which the performance of a broadcast schedule is analyzed. Thus, we define a new measure, called the Query Distance QD , that is the minimum distance withinŽ . which all the relevant data objects for a given query can be accessed when the bcast is repeatedly broadcasted.

Definition 1. Let $D ( q _ { i } )$ be $\{ d _ { i 1 } , ~ d _ { i 2 } , ~ d _ { i k } \}$ in schedule. Then, the Query Distance QD of Ž . $q _ { i }$ in $\sigma$ is defined as follows:

$$
\mathrm{QD} \left(q _ {i}, \sigma\right) = B - \operatorname{MAX} \left(\delta_ {i j}\right), \quad j = 1, 2, \dots , k.
$$

The meaning of QD is illustrated in Fig. 3, where $D ( q )$ for a query $q$ is $\{ d _ { 1 } , d _ { 2 } , d _ { 3 } , d _ { 4 } \}$ in a broadcast schedule $\sigma .$ . Note that in the figure there may existŽ other data objects between two data objects of $D ( q ) . )$ Then, the QD of $q$ in the given schedule $\sigma$ is the minimum among $p _ { 1 } , p _ { 2 } , p _ { 3 }$ and $p _ { 4 }$ , where $p _ { i }$ is the access time when query q starts at the beginning of $d _ { i } , { \mathrm { i . e . , ~ } } p _ { 1 } = B - \delta _ { 4 } , \ p _ { 2 } = B - \delta _ { 1 } , \ p _ { 3 } = B - \delta _ { 2 }$ and $p _ { 4 } = B - \delta _ { 3 }$

Lemma 1. GiÕen a query $q _ { i }$ and two schedules $\sigma _ { I }$ and $\sigma _ { 2 }$

$$
\text { if } \mathrm{QD} (q _ {i}, \sigma_ {1}) \geq \mathrm{QD} (q _ {i}, \sigma_ {2}),
$$

$$
\text { then } \mathrm{AT} ^ {\text { avg }} (q _ {i}, \sigma_ {1}) \geq \mathrm{AT} ^ {\text { avg }} (q _ {i}, \sigma_ {2})
$$

Proof. See Appendix B.

Let the total query distance in schedule $\sigma .$ , denoted by TQDŽ ., be $\Sigma _ { q i \in \mathcal { Q } } \mathrm { Q D } ( q _ { i } , \ \sigma ) \times \mathrm { f r e q } ( q _ { i } )$ Now we redefine the problem of wireless data clustering by using Lemma 1.

Definition 2. Given a set of data objects $\mathcal { D }$ and a set of queries ${ \mathcal { Q } } ,$ the wireless data clustering problem is to find a broadcast schedule $\sigma _ { i }$ such that $\mathrm { T Q D } ( \sigma _ { i } )$ is the minimum among all possible $\sigma _ { i } , i = 1 , \ \cdot \cdot \cdot$

Theorem 1. The wireless data clustering problem in Definition 2 is NP complete.

Proof. The proof easily follows transformation from the Optimal Linear Arrangement Problem 5 . See <sup>w</sup> <sup>x</sup> Appendix C. I

## 2.3. Comparison with data clustering on the disk

A commonly used measure of data clustering for the shared data on the disk is the number of disk accesses for the queries. Thus, it is beneficial to minimize the number of clusters by placing the relevant data objects together in the same or neighbor disk pages. However, in wireless broadcasting, since there is no concept of Aseek timeB as in the disk, the number of clusters for the query data set has little or no importance.

![](/api/attachments/QGEW9EJ4/fulltext/images/7d392ee38870004f5aa4e676c6ee06be7c3aceb9473b0277b6ca6b3d0520b155.jpg)  
Fig. 3. Graphical illustration of the QD of a query.

Fig. 4 shows two examples of data clustering. Suppose that query q accesses data objects $d _ { 1 } , \ d _ { 2 }$ $d _ { 6 } , d _ { 7 } , d _ { 8 } , d _ { 1 3 }$ and $d _ { 1 4 }$ . In the disk-based environment, the placement A is better than B with respect to $q .$ This is because only three clusters need to be accessed for processing the query in placement A, while five clusters have to be accessed in placement B. However, in wireless data broadcasting, placement B is better because $\mathrm { Q D } ( q , B )$ is smaller than $\mathrm { Q D } ( q , \ A )$

## 2.4. Basic properties of the wireless data schedule

We describe two basic properties in the wireless broadcast schedule.

Proposition 1 Ž . Interchangeability . Let there be two schedules $\sigma _ { I }$ and $\sigma _ { 2 }$ such that:

$$
\begin{array}{c} \sigma_ {1} = \left\langle d _ {1}, d _ {2}, \dots , d _ {i - 1}, d _ {i}, d _ {i + 1}, \dots , \right. \\ \left. d _ {j - 1}, d _ {j}, d _ {j + 1}, \dots , d _ {N - 1}, d _ {N} \right\rangle , \\ \sigma_ {2} = \left\langle d _ {1}, d _ {2}, \dots , d _ {i - 1}, d _ {j}, d _ {i + 1}, \dots , d _ {j - 1}, d _ {i}, \right. \\ \left. d _ {j + 1}, \dots , d _ {N - 1}, d _ {N} \right\rangle . \end{array}
$$

Then, for any query $q _ { i }$ such that both $d _ { i }$ and $d _ { j }$ are in $D ( q _ { i } ) , Q D ( q _ { i } , \sigma _ { l } ) = Q D ( q _ { i } , \sigma _ { 2 } )$

Definition 3. Given two schedules $\sigma _ { 1 }$ and $\sigma _ { 2 }$ , if $\mathrm { Q D } ( q _ { i } , \ \sigma _ { 1 } )$ is equal to $\mathrm { Q D } ( q _ { i } , \sigma _ { 2 } )$ for every query $q _ { i } ,$ then we say that $\sigma _ { 1 }$ is distance-equivalent to $\sigma _ { 2 }$ and is denoted by the equality, i.e., $\sigma _ { 1 } = \sigma _ { 2 }$

Proposition 2 Ž . Symmetry . If a schedule $\sigma _ { 2 }$ is the mirror image of $\sigma _ { I }$ , i.e.:

$$
\begin{array}{l} \sigma_ {1} = \big \langle d _ {1}, d _ {2}, \dots d _ {i - 1}, d _ {i}, d _ {i + 1}, \dots d _ {N - 1}, d _ {N} \big \rangle , \\ \sigma_ {2} = \big \langle d _ {N}, d _ {N - 1}, \dots d _ {i + 1}, d _ {i}, d _ {i - 1}, \dots d _ {2}, d _ {1} \big \rangle , \end{array}
$$

then $\sigma _ { I }$ is distance-equiÕalent to $\sigma _ { 2 } , i . e . , \sigma _ { I } = \sigma _ { 2 }$

The Interchangeability property is a direct consequence from the definition of the Query Distance. The property says that any two data objects in $D ( q _ { i } )$ are mutually interchangeable with respect to the Query Distance of $q _ { i }$ . In the Symmetry property, $\mathrm { Q D } ( q _ { i } , \sigma _ { 1 } )$ is equal to $\mathrm { Q D } ( q _ { i } , \sigma _ { 2 } )$ for all $q _ { i }$ because any in $\sigma _ { 1 }$ is equal to that in $\sigma _ { 2 }$

## 3. The proposed clustering method

In our method, we utilize the Gray coding scheme for clustering wireless data. After briefly describing the Gray coding scheme, we explain our method. Then, we analyze the clustering properties of the Gray coding scheme.

## 3.1. Gray codes

The Gray coding scheme is one of the schemes for linear mapping of multidimensional space. In the binary reflected Gray code, numbers are coded into binary bit strings such that successive numbers differ in exactly 1-bit position. It is observed that difference in only 1-bit position has a relationship with locality 4,8 . The terms and notation below are from<sup>w</sup> <sup>x</sup> Ref. 4 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/QGEW9EJ4/fulltext/images/0a73296dfdf2a0754b03d36770fe174aaf30327145a2a4321fda812f0f274071.jpg)  
Fig. 4. Comparison of two data placements.

Table 1 shows an illustration of 3-bit binary reflected Gray codes with corresponding binary codes. From now on, we use the term AGray codeB for Abinary reflected Gray codeB throughout the paper. The Gray Value of a binary string, denoted by $( . ) _ { \mathrm { G } }$ Ž . , is the order or position of the binary string in the Gray code. For instance, the Gray value of 110 , Ž . denoted by $( 1 1 0 ) _ { \mathrm { G } }$ , is 4. It is the same as $\left( 4 \right) _ { 1 0 }$ and $\left( 1 0 0 \right) _ { 2 }$

The conversion formulas of a Gray codeword to its order i.e. Gray value described below are fromŽ . Ref. 9 . Suppose the<sup>w</sup> <sup>x</sup> n-bit Gray codeword is $\textstyle { \big ( } g _ { n } ,$ $g _ { n - 1 } , \ \cdot \cdot \cdot , \ g _ { 1 } )$ and its order in binary is $( b _ { n } , b _ { n - 1 } ,$ $\cdots , b _ { 1 } , b _ { 0 } )$ . Then:

$$
b _ {n} = 0,
$$

$$
b _ {n} = \sum_ {m = j + 1} ^ {n} g _ {m} \bmod 2 \quad 0 \leq j <   n.
$$

## 3.2. Bit-Õector representation

In our proposed method for wireless data clustering, we first associate each data object with a bit vector of dimension M, where M is the number of queries in ${ \mathcal { Q } } .$ In the bit vector, the ith bit is set to $^ { 6 6 } 1 ^ { , 5 }$ if the data object is accessed by the query $q _ { i } .$ Otherwise, the bit is set to $\mathbf { \vec { \Delta } } ^ { 6 } 0 ^ { 9 }$

Definition 4. Let there be M number of queries in $\mathcal { Q }$ such that for all $q _ { i } , \ i = 1 , \ \cdot \ \cdot \ , \ ( M - 1 )$ in ${ \mathcal { Q } } .$

Illustration of the 3-bit binary reflected Gray code

<table><tr><td>Gray value</td><td>Gray code</td><td>Binary code</td></tr><tr><td>0</td><td>000</td><td>000</td></tr><tr><td>1</td><td>001</td><td>001</td></tr><tr><td>2</td><td>011</td><td>010</td></tr><tr><td>3</td><td>010</td><td>011</td></tr><tr><td>4</td><td>110</td><td>100</td></tr><tr><td>5</td><td>111</td><td>101</td></tr><tr><td>6</td><td>101</td><td>110</td></tr><tr><td>7</td><td>100</td><td>111</td></tr></table>

freq $\mathbf { \chi } _ { q _ { i } } ) \geq \mathrm { f r e q } ( q _ { i + 1 } )$ . Let $d _ { \vec { i } } ^ {  }$ denote the bit vector for data object $d _ { i } .$ Then, $d _ { \vec { i } } ^ {  }$ consists of $( u _ { 1 } , u _ { 2 } , \cdot \cdot \cdot$ $u _ { M } )$ such that:

$$
u _ {k} = \left\{ \begin{array}{l l} 1 & \text { if } d _ {i} \in D (q _ {k}), \\ 0 & \text { otherwise } \end{array} \right.
$$

Note that $u _ { 1 }$ corresponds to the most frequently referenced query, $u _ { 2 }$ corresponds to the same or next frequently referenced query, <sup>PPP</sup> , and $u _ { M }$ corresponds to the least one.

Example 1. Suppose that the set of queries is $\{ \boldsymbol { q } _ { 1 }$ $q _ { 2 } , q _ { 3 } \}$ and the set of data objects in the bcast is $\{ d _ { 1 } ,$ $d _ { 2 } , \ d _ { 3 } , \ d _ { 4 } , \ d _ { 5 } , \ d _ { 6 } , \ d _ { 7 } , \ d _ { 8 } \}$ . Suppose also that the reference frequency and the query data set $D ( q _ { i } )$ of each query are:

$$
\begin{array}{l} \operatorname{freq} (q _ {1}) = 3, D (q _ {1}) = \left\{d _ {1}, d _ {2}, d _ {4}, d _ {5} \right\}, \\ \operatorname{freq} (q _ {2}) = 2, D (q _ {2}) = \left\{d _ {4}, d _ {5}, d _ {6}, d _ {7}, d _ {8} \right\}, \\ \operatorname{freq} (q _ {3}) = 1, D (q _ {3}) = \left\{d _ {2}, d _ {3}, d _ {5}, d _ {6} \right\}. \end{array}
$$

Then, the bit-vector representations of the data objects are as follows:

$$
\begin{array}{l} \vec {d _ {1}} = (1, 0, 0), \vec {d _ {2}} = (1, 0, 1), \\ \vec {d _ {3}} = (0, 0, 1), \vec {d _ {4}} = (1, 1, 0), \\ \vec {d _ {5}} = (1, 1, 1), \vec {d _ {6}} = (0, 1, 1), \\ \vec {d _ {7}} = (0, 1, 0), \vec {d _ {8}} = (0, 1, 0). \end{array}
$$

Here, the leftmost vector element is for $q _ { 1 } ,$ , the second element is for $q _ { 2 }$ and the third element is for $q _ { 3 } .$

## 3.3. Gray code clustering method

Our clustering method consists of two steps: 1Ž . generating a bit vector for each data object, and 2Ž . sorting the bit vectors based on their Gray values. Thus, the complexity of the method is MAXŽ Ž . O NM , O NŽ .. log N , where N is the number of data objects and M is the number of queries. The sequence of data objects corresponding to the sorted sequence of bit vectors is our broadcast schedule. For convenience, the bit vector is denoted by the binary codeword, e.g., 101 for 1,0,1 .Ž .

Table 2 shows the sorted result of the data objects in Example 1. Thus, a broadcast schedule $( \mathrm { i . e . }$ , the broadcasting sequence of wireless data based on our. proposed Gray code clustering method is as follows:

$$
\sigma_ {\text { Gray }} = \left\langle d _ {3}, d _ {6}, d _ {7}, d _ {8}, d _ {4}, d _ {5}, d _ {2}, d _ {1} \right\rangle .
$$

The data objects having the same bit-vector representation, such as $d _ { 7 }$ and $d _ { 8 }$ in Table 2, can be mutually interchangeable in the schedule by Property 1 . Ž . The reverse ordering of the above schedule is also distance-equivalent to the original ordering by Prop- Ž erty 2 , which means that the sorted sequence of the. bit vectors in a nonincreasing order has the same effect with respect to our proposed method.

## 3.4. Clustering properties of the Gray coding scheme in wireless enÕironment

The Gray coding scheme has been studied for data clustering in the disk-based environment for the purpose of minimizing the number of clusters that a query accesses 4,8 . However, in this paper, we <sup>w</sup> <sup>x</sup> consider the clustering of data on the air, where the Query Distance is important rather than the number of clusters.

We define the Code Distance to describe the clustering property of Gray codes in wireless environment.

Definition 5. For an n-bit coding scheme $\mathcal { C } _ { \mathrm { : } }$ , where a codeword is denoted by $^ { \cdots } e _ { 1 } , e _ { 2 } , \ ^ { \cdots } , e _ { n } , ^ { \cdots }$ there is a list of $2 ^ { n }$ different codewords that are sorted based on its own coding scheme. Then the Code Distance of the ith bit $e _ { i }$ in $\mathcal { C } ,$ denoted by ${ \mathrm { C D } } _ { \mathcal { C } } ( i , n )$ , is defined as:

Table 2  
Data ordering based on the Gray values

<table><tr><td>Gray value</td><td>Bit vector</td><td>Data object</td></tr><tr><td>1</td><td>001</td><td> $d_{3}$ </td></tr><tr><td>2</td><td>011</td><td> $d_{6}$ </td></tr><tr><td>3</td><td>010</td><td> $d_{7}, d_{8}$ </td></tr><tr><td>4</td><td>110</td><td> $d_{4}$ </td></tr><tr><td>5</td><td>111</td><td> $d_{5}$ </td></tr><tr><td>6</td><td>101</td><td> $d_{2}$ </td></tr><tr><td>7</td><td>100</td><td> $d_{1}$ </td></tr></table>

Table 3  
Binary coding scheme: 3-bit example

<table><tr><td> $b_{1}$ </td><td> $b_{2}$ </td><td> $b_{3}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

$$
\mathrm{CD} _ {\mathscr {C}} (i, n) = 2 ^ {n} - \phi_ {\mathscr {C}} (i, n).
$$

Here, $\phi _ { \mathcal { C } } ( \boldsymbol { i } , n )$ is the maximum number of consecutive codewords whose ith bits are $\cdot _ { 0 } ,$ when the codewords are cyclically repeated.

Example 2. Consider the binary coding scheme BC in Table 3, where 3-bit codewords are sorted based on the binary coding scheme. The values of $\mathrm { C D } _ { \mathrm { B C } }$ and $\phi _ { \mathrm { B C } }$ for the above 3-bit binary codewords are in Table 4.

In the Gray coding, the values of $\phi _ { \mathrm { G } } ( { \boldsymbol { i } } , { \boldsymbol { n } } )$ can be computed by the following formula, which is easily obtained by the definition of the Gray code.

$$
\phi_ {\mathrm{G}} (i, n) = \left\{ \begin{array}{l l} 2 ^ {n - 1} & \text { if } i = 1, \\ 2 ^ {n - i + 1} & \text { otherwise }. \end{array} \right.
$$

Consider the data objects in Example 1. Fig. 5 shows the 3-bit Gray codes and those data objects that are clustered by the Gray code clustering method.

Table 4  
Code Distance values of 3-bit binary codewords

<table><tr><td>i</td><td> $\phi_{\text{BC}}(i,3)$ </td><td> $\text{CD}_{\text{BC}}(i,3)$ </td></tr><tr><td>1</td><td>4</td><td>4</td></tr><tr><td>2</td><td>2</td><td>6</td></tr><tr><td>3</td><td>1</td><td>7</td></tr></table>

Table 5  
![](/api/attachments/QGEW9EJ4/fulltext/images/cb8396e0525c6add3719aa784b5bb44cd2b7a472c5b928b95fb9f759165541d3.jpg)  
Fig. 5. Clustering of data objects in Example 1 using 3-bit Gray codewords.

The result schedule $\sigma _ { \mathrm { G r a y } }$ is $\langle d _ { 3 } , d _ { 6 } , d _ { 7 } , d _ { 8 } , d _ { 4 } , d _ { 5 }$ $d _ { 2 } , d _ { 1 } \rangle$ . And, Table 5 shows that the values of $\phi _ { \mathrm { G } }$ and $\mathrm { C D } _ { \mathrm { G } }$ for 3-bit Gray codes, and the values of MAXŽ . and QD in the result schedule $\sigma _ { \mathrm { G r a y } }$ . We can observe that the concepts of the Code Distance and $\phi$ are closely related with those of the Query Distance and MAXŽ .  , respectively. Though our proposed method is based on the similarity between those concepts, $\mathrm { C D } _ { \mathrm { G } } ( i , { \cal M } )$ and $\phi _ { \mathrm { G } }$ are not exactly the same as $\mathrm { Q D } ( q _ { i } , \ \sigma _ { \mathrm { G r a y } } )$ Ž . and MAX . This is because the size of each data object is not the same, and each codeword is not matched to exactly one data object. For example, in Fig. 5, there is no matched data for 0,0,0 , while two data objectsŽ . $d _ { 7 }$ and $d _ { 8 }$ are matched to the same codeword 0,1,0 .Ž .

In the figure, the data objects accessed by query $q _ { 1 }$ can be represented by a bit vector $( 1 , \ ^ { * } , \ ^ { * } )$ , which are the bottom four rows in the figure, i.e., $d _ { 1 } , \ d _ { 2 }$ $d _ { 5 }$ and $d _ { 4 }$ . Here, ‘<sup>)</sup> ’ denotes a don’t care condition. ŽSimilarly, the data objects accessed by $q _ { 2 }$ and $q _ { 3 }$ can be represented by $^ { ( ^ { * } , ~ 1 , ~ ^ { * } ) }$ and $( \bar { \ast } , \bar { \ast } , 1 ) .$ respectively..

In the binary coding scheme, $\mathrm { C D } _ { \mathrm { B C } } ( 1 , 3 )$ $\mathrm { C D } _ { \mathrm { B C } } ( 2 , 3 )$ and $\mathrm { C D } _ { \mathrm { B C } } ( 3 , 3 )$ are 4, 6 and 7, respectively, as shown in Example 2, while the corresponding code distances in the Gray coding scheme are 4, 4 and 6. This means that our proposed clustering method utilizes the fact that the average code distance in the Gray coding scheme is relatively small compared with those of other coding schemes. Here, the average n-bit code distance in the coding scheme $\mathcal { C }$ is defined by $[ \sum _ { i = 1 } ^ { n } \mathrm { C D } _ { \mathcal { C } } ( { i , n } ) ] / n$

Thus, the following heuristics can be a viable alternative for the wireless clustering problem: AUtilize a coding scheme $\mathcal { C }$ that minimizes the average code distance.B

Suppose the mapping from the set of data objects to the set of codewords is one-to-one correspondent. Suppose also that all the queries have the same reference frequency and all the data objects are of the same size. Then, the above heuristics would give the optimal solution.

Definition 6. Consider a coding scheme $\mathcal { C } .$ . The sequence of code distances in coding scheme $\mathcal { C }$ is said to be nondecreasing or nonincreasing if, for allŽ . $i \leq j , \ C \mathrm { D } _ { \mathcal { C } } ( i ,$ . Ž . , n is always smaller or larger than or equal to $\mathrm { C D } _ { \mathcal { C } } ( j , n )$

It is also useful that the values of ${ \mathrm { C D } } _ { \mathcal { C } } ( i , n )$ $i = 1 , 2 , \ \cdots , \ n$ , are either nondecreasing or nonincreasing. This means that we can easily associate the set of queries with the set of bit positions according to the degree of reference frequencies of the queries.

Proposition 3. The sequence of code distances in Gray coding scheme is nondecreasing.

Note that, in Definition 4, we construct the bit vector for a data object such that the leftmost bit corresponds to the highest-frequency query.

Theorem 2. The aÕerage code distance in the Gray coding scheme is minimum among all the coding schemes whose sequence of code distances is nondecreasing or nonincreasing .( )

Proof. The proof is straightforward due to the way the Gray code is defined. I

Concepts of the Query Distance and the Code Distance

<table><tr><td>i</td><td> $\phi_G(i, 3)$ </td><td> $CD_G(i, 3)$ </td><td>MAX(δ) for  $q_i$ </td><td> $QD(q_i, \sigma_{Gray})$ </td></tr><tr><td>1</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>2</td><td>4</td><td>4</td><td>3</td><td>5</td></tr><tr><td>3</td><td>2</td><td>6</td><td>3</td><td>5</td></tr></table>

## 4. Performance evaluation

## 4.1. Experiments

Most previous studies are based on the assumption that a query can access only a single data object. Some of them 1,2,10 use replication of frequently<sup>w</sup> <sup>x</sup> accessed data in a single bcast. This has an advantage for a query accessing frequently the accessed data, but also has a disadvantage for a query accessing less frequently accessed one because data replication causes the length of a bcast to increase. Our proposed method considers the case that a query can access any number of data objects. This type of query is not only general but also has many useful applications in practice. However, our method does not consider replication of data objects in a single bcast. Since the main applications as well as the operational environments between the previous work <sup>w</sup> <sup>x</sup> 1,2,10 and this work are quite different, direct comparison of our method with the previous ones is not very meaningful. Thus, in this section, we evaluate the performance of our proposed method compared with the random scheduling method.

![](/api/attachments/QGEW9EJ4/fulltext/images/e48de8b456b8dac536f762582601b2f448f762f64e50164afbe2dd7cbe4288a4.jpg)  
Fig. 6. TAT reduction with various selectivity values.

The experimental parameters are as follows. N is the number of data objects in the bcast where every data object is accessed by at least one query. The number of query patterns is M. Every query accesses one or more data on the broadcasting channel and the query data sets Ž . Ds are mutually independent between queries. The selectivity S is the percentage of data objects that a single query accesses among all the data objects in the bcast. For example, 2% selectivity means that every query accesses 2% of the data objects in the bcast. We assume that the query data set $D ( q _ { i } )$ of each query $q _ { i }$ is uniformly distributed in the bcast. We consider three different kinds of distribution for queries’ reference frequency $\mathrm { f r e q } ( q _ { i } )$ : uniform distribution, normal distribution and exponential distribution $( \lambda = 1 )$ . In all the three distributions, we set the minimum frequency into 1 and the maximum frequency into M. We assume that all the data objects are of the same size.

![](/api/attachments/QGEW9EJ4/fulltext/images/aa1595be2dfdf88166a43cf80645f81e1a65801b53a614a53a3d8ba8d76b5a09.jpg)  
Fig. 7. TAT reduction with various numbers of query patterns.

Fig. 6 shows the ratios of TAT i.e., the totalŽ access time reduction of the schedules generated by. the proposed method to random schedules i.e., 100 <sup>w</sup> $- ( 1 0 0 \times \mathrm { T A T _ { G r a y } / T A T _ { r a n d o m } ) ] }$ with various values of query selectivity. The number of data objects is 500 and the number of query patterns is 100. The performance improvement is about 20–30% when the selectivity is low and is about 10–15% when the selectivity is high. The Query Distance of each query increases when its query data set D is overlapped much with those of other queries. Thus, the proposed clustering method shows the best performance when the selectivity is low, and gradually decreases with the increase of selectivity.

Fig. 7 shows TAT reductions for various numbers of query patterns, where all the queries have 1% selectivity. The number of data objects is 500. The figure shows that the performance improvement of the proposed method is best with a small number of query patterns, and gradually decreases with the increase of the number of query patterns. This can be explained by the fact that for any i, $\mathrm { C D } _ { \mathrm { G } } ( i , \ M ^ { \prime } ) >$ $\mathrm { C D } _ { \mathrm { G } } ( i , M )$ when $M ^ { \prime } > M$

We have also experimented with various numbers of data objects and variable size data objects, and have found that the performance improvement of the proposed method has little dependency with them.

In all the experiments, the best performance is achieved when the distribution is exponential. That is, the more highly skewed distribution of queries reference frequency is, the better performance our method can achieve. This is because our method gives priority to the higher frequency queries in reducing the Query Distance.

## 4.2. Optimality test

It is shown in Theorem 1 that the data clustering problem considered in this paper is NP complete and, hence, there could be no optimal algorithm except the exhaustive search method. The solutions produced by our method are optimal in some cases, but are not in general. Thus, we first present the cases where our method provides optimal results, and then describe some experiments that show the comparison with the optimal results.

Theorem 3. The proposed method based on the Gray coding scheme generates an optimal broadcast schedule when each query data set $D ( q _ { i } )$ is o Õerlapped at most by two other query data sets.

Proof. When each query data set $D ( q _ { i } )$ is overlapped at most by two other query data sets, our method generates a schedule where the data objects are placed as in Fig. 8. Fig. 8 a shows the case that Ž . every query data set D is mutually exclusive, and Fig. 8 b shows the case that every query data set Ž . D is overlapped by one or two other query data sets.

Suppose that we move a certain data object in $D ( q _ { i } )$ into a position where the data object in $D ( q _ { j } )$ is placed. Then, in both cases of the figure, the $\mathrm { Q D } ( q _ { j } )$ and $\mathrm { Q D } ( q _ { j } )$ increase, while the QDs of the other queries remain unchanged. Thus, the TQD of the modified schedule is bigger than the TQD of the original schedule.

In consequence, we can prove by contradiction that the proposed method produces optimal schedules if each query data set is overlapped at most by two other query data sets. I

a)  
![](/api/attachments/QGEW9EJ4/fulltext/images/cff82586722de6feaf756d5d045116137b64d373ecc75d6163f1481cec57d494.jpg)

b)  
![](/api/attachments/QGEW9EJ4/fulltext/images/cdac6bf65d6f34eb0937942972130340118ed9ededa6daedf4c3100ec3ded6dd.jpg)  
Fig. 8. Cases of optimal schedules.

Table 6 Closeness to optimality

<table><tr><td>N</td><td>M</td><td>S</td><td>Frequency dist. type</td><td>Closeness to optimality</td></tr><tr><td>7</td><td>20</td><td>40</td><td>Uniform</td><td>0.99</td></tr><tr><td>7</td><td>20</td><td>40</td><td>Normal</td><td>0.98</td></tr><tr><td>7</td><td>20</td><td>40</td><td>Exponential</td><td>0.99</td></tr><tr><td>7</td><td>20</td><td>60</td><td>Uniform</td><td>0.99</td></tr><tr><td>7</td><td>20</td><td>60</td><td>Normal</td><td>0.99</td></tr><tr><td>7</td><td>20</td><td>60</td><td>Exponential</td><td>0.99</td></tr><tr><td>8</td><td>20</td><td>40</td><td>Uniform</td><td>0.98</td></tr><tr><td>8</td><td>20</td><td>40</td><td>Normal</td><td>0.98</td></tr><tr><td>8</td><td>20</td><td>40</td><td>Exponential</td><td>0.98</td></tr><tr><td>8</td><td>20</td><td>60</td><td>Uniform</td><td>0.99</td></tr><tr><td>8</td><td>20</td><td>60</td><td>Normal</td><td>0.98</td></tr><tr><td>8</td><td>20</td><td>60</td><td>Exponential</td><td>0.98</td></tr><tr><td>9</td><td>20</td><td>40</td><td>Uniform</td><td>0.98</td></tr><tr><td>9</td><td>20</td><td>40</td><td>Normal</td><td>0.97</td></tr><tr><td>9</td><td>20</td><td>40</td><td>Exponential</td><td>0.97</td></tr><tr><td>9</td><td>20</td><td>60</td><td>Uniform</td><td>0.98</td></tr><tr><td>9</td><td>20</td><td>60</td><td>Normal</td><td>0.98</td></tr><tr><td>9</td><td>20</td><td>60</td><td>Exponential</td><td>0.99</td></tr><tr><td>10</td><td>20</td><td>40</td><td>Uniform</td><td>0.98</td></tr><tr><td>10</td><td>20</td><td>40</td><td>Normal</td><td>0.98</td></tr><tr><td>10</td><td>20</td><td>40</td><td>Exponential</td><td>0.98</td></tr><tr><td>10</td><td>20</td><td>60</td><td>Uniform</td><td>0.98</td></tr><tr><td>10</td><td>20</td><td>60</td><td>Normal</td><td>0.98</td></tr><tr><td>10</td><td>20</td><td>60</td><td>Exponential</td><td>0.98</td></tr></table>

The computational complexity of the exhaustive search method is $O ( N ! \times N \times M )$ . Due to the high complexity, our experiment for comparing with the optimal method i.e., exhaustive search method hasŽ . been done only on 7, 8, 9 and 10 data objects. The result is described in Table 6, where ‘Closeness to Optimality’ is defined as $\mathrm { T A T _ { O p t i m a l } / T A T _ { G r a y } }$ . As shown in the table, the proposed method finds solutions that are very close to optimal irrespective of different distributions. This indicates that the optimal schedule inherently gives priority to high frequency queries. Though the number of data objects used in the exhaustive method is small, the result shows that the proposed method is an efficient heuristic method.

## 5. Conclusion

In this paper, we have proposed a wireless data clustering method for multipoint queries, where the data objects are not replicated in a single bcast. By effective data clustering, the mobile clients can access the wireless data in short latency. The multipoint query is one of the most popular query patterns in various applications. To the best of our knowledge, there is no previous work considering multipoint queries in wireless data broadcasting.

We have defined the problem of wireless data clustering, and have proposed a measure, named the Query Distance, for wireless data clustering. The Query Distance is the minimum distance within which all the relevant data objects can be accessed when the bcast is repeatedly broadcasted. Then, we have proposed a wireless data clustering method for multipoint queries, which utilizes the properties of the Gray coding scheme for minimizing the Query Distance of each query. We have observed that the concept of the Code Distance is closely related with that of the Query Distance. Based on this observation, we have indicated important characteristics of the Gray coding scheme that are useful for clustering wireless broadcast data. Finally, by experiments, we have evaluated the performance i.e., the access timeŽ reduction of the proposed method in comparison. with the random clustering method.

We are currently investigating an extension of the proposed method for the case that data objects are replicated in a single bcast. Another extension can be considered for the case that there exist multiple channels for wireless data broadcasting.

## Acknowledgements

This work was supported by BK21 Educational-Industrial collaboration fund.

## Appendix A. Derivation of Average Access Time

Let $p ( x )$ and $F ( x )$ be the probability and the access time of query $q _ { i }$ issued at location x, respectively. Then the estimated average access time of $q _ { i }$ is computed as follows, where B denotes the size of a single bcast. Note that, in wireless data broadcasting the distance between two data objects has the same semantics as the length of time. Thus, we regard the access time of a query in the dimension of data size for simplicity. In the final step, we convert the data size into time dimension:

$$
\mathrm{AT} ^ {\text { avg }} (q _ {i}, \sigma) = \int_ {0} ^ {B} p (x) F (x) \mathrm{d} x,\tag{1}
$$

$$
\mathrm{AT} ^ {\text { avg }} (q _ {i}, \sigma) = \frac {1}{B} \int_ {0} ^ {B} F (x) \mathrm{d} x,\tag{2}
$$

$$
\mathrm{AT} ^ {\text { avg }} (q _ {i}, \sigma) = \frac {1}{B} \sum_ {j = 1} ^ {k} \int_ {0} ^ {t _ {i j}} F (y) \mathrm{d} y,\tag{3}
$$

$$
= \frac {1}{B} \sum_ {j = 1} ^ {k} \left[ \int_ {0} ^ {\left| d _ {i j} \right|} F (y) \mathrm{d} y + \int_ {\left| d _ {i j} \right|} ^ {t _ {i j}} F (y) \mathrm{d} y \right],\tag{4}
$$

$$
\begin{array}{l} \mathrm{AT} ^ {\text {avg}} (q _ {i}, \sigma) \\ = \frac {1}{B} \sum_ {j = 1} ^ {k} \left[ \int_ {0} ^ {| d _ {i j} |} B \mathrm{d} y + \int_ {| d _ {i j} |} ^ {t _ {i j}} (B - y + | d _ {i j} |) \mathrm{d} y \right], \end{array}\tag{5}
$$

$$
\mathrm{AT} ^ {\text { avg }} \left(q _ {i}, \sigma\right) = B - \frac {1}{2 B} \sum_ {j = 1} ^ {k} \left(t _ {i j} - \left| d _ {i j} \right|\right) ^ {2},\tag{6}
$$

$$
\mathrm{AT} ^ {\text { avg }} \left(q _ {i}, \sigma\right) = \left(B - \frac {1}{2 B} \sum_ {j = 1} ^ {k} \left(\delta_ {i j}\right) ^ {2}\right).\tag{7}
$$

In Eqs. 1 and 2 , the estimated average accessŽ . Ž . time is computed by summing up $p ( x ) \times F ( x )$ for all location x in one bcast, and $p ( x )$ is $1 / B$ regardless of x. Then, $\operatorname { A T } ^ { \mathrm { a v g } } ( q _ { i } , \sigma )$ can be computed by dividing the bcast into $t _ { i j } ,$ the distance between each data object that $q _ { i }$ accesses i.e.,Ž $t _ { i j } = | d _ { i j } | + \delta _ { i j }$ in Eq. 3 . Here,Ž . k denotes the number of data objects that query $q _ { i }$ accesses. The interval $t _ { i j }$ is divided into two smaller intervals, $0 - | d _ { i j } |$ and $| d _ { i j } ^ { \top } | { - } t _ { i j }$ in Eq. Ž . Ž . 4 see Fig. 2 .

In the interval $0 - | d _ { i j } | ,$ the access time $F ( y )$ is the period of one bcast because parts of $d _ { i j }$ have passed over. The client has to read the remaining parts of data in the next bcast, which takes B. In the interval $\lvert d _ { i j } \rvert { - } t _ { i j } .$ , the access time is the period of one bcast minus the interval $y - | d _ { i j } | ,$ where y is the probe position in the unit interval. This is shown in Eqs. Ž . Ž . 5 and 6 . In consequence, the average access time is computed as in Eq. 7 . Ž .

Now, we convert the dimension of $\mathbf { A T } ^ { \mathrm { a v g } }$ into time by using a conversion factor Ži.e., the amount of time for transmitting a unit size of data such as a packet . Then, the average access time of query . $q _ { i }$ is described as follows:

$$
\mathrm{AT} ^ {\text { avg }} (q _ {i}, \sigma) = \kappa \left(B - \frac {1}{2 B} \sum_ {j = 1} ^ {k} \left(\delta_ {i j}\right) ^ {2}\right).
$$

## Appendix B. Proof of Lemma 1

Let us assume there are two schedules $\sigma _ { 1 }$ and $\sigma _ { 2 }$ , and a query $q _ { i } .$ . By definition, $\mathrm { Q D } ( q _ { i } , \ \sigma _ { 1 } )$ and $\mathrm { Q D } ( q _ { i } , \mathrm { ~ \it ~ \sigma ~ } _ { 2 } )$ are $B \mathrm { ~ - ~ } \mathrm { M A X } ( \delta _ { i j , 1 } )$ and $B -$ $\mathbf { M A X } ( \delta _ { i j , 2 } ) ,$ , where $\delta _ { i j , 1 }$ is the of $q _ { i }$ in schedule $\sigma _ { 1 }$ , and $\bar { \boldsymbol { \delta } } _ { i j , 2 }$ is the of $q _ { i }$ in schedule $\sigma _ { 2 }$ , respectively. Then, $\operatorname { A T } ^ { \mathrm { a v g } } ( q _ { i } , \ \sigma _ { 1 } )$ and $\operatorname { A T } ^ { \mathrm { a v g } } ( q _ { i } , \ \sigma _ { \gamma } )$ are represented as $[ B - ( 1 / \dot { 2 } B ) \Sigma _ { j = 1 } ^ { k } ( \delta _ { i j , 1 } ) ^ { 2 } ]$ and $\kappa [ B$ $- ( 1 / 2 B ) \Sigma _ { j = 1 } ^ { k } ( \delta _ { i j , 2 } ) ^ { 2 } ]$ Thus, the lemma to be proved becomes as follows, if:

$$
B - \operatorname{MAX} \left(\delta_ {i j}, 1\right) \geq B - \operatorname{MAX} \left(\delta_ {i j}, 2\right),\tag{8}
$$

then:

$$
\kappa \left[ B - \frac {1}{2 B} \sum_ {j = 1} ^ {k} \left(\delta_ {i j, 1}\right) ^ {2} \right] \geq \kappa \left[ B - \frac {1}{2 B} \sum_ {j = 1} ^ {k} \left(\delta_ {i j}, 2\right) ^ {2} \right],\tag{9}
$$

Since  and B are positive constants, we can simplify the inequalities as follows:

$$
\text { if } \operatorname{MAX} \left(\delta_ {i j, 1}\right) \leq \operatorname{MAX} \left(\delta_ {i j, 2}\right),
$$

$$
\text { then } \sum_ {j = 1} ^ {k} \left(\delta_ {i j, 1}\right) ^ {2} \leq \sum_ {j = 1} ^ {k} \left(\delta_ {i j, 2}\right) ^ {2}.\tag{10}
$$

We prove the lemma in Eq. 10 by induction.Ž . Note that $\delta _ { i j , 1 } \geq 0 , \quad \delta _ { i j , 2 } \geq 0$ and $\begin{array} { r } { \sum _ { j = 1 } ^ { k } \delta _ { i j , 1 } = } \end{array}$ $\begin{array} { r } { \sum _ { j = 1 } ^ { k } \delta _ { i j , 2 } = C } \end{array}$ , where C is $\begin{array} { r } { B - \sum _ { j = 1 } ^ { k } \lvert d _ { i j } \rvert . } \end{array}$

## B.1. Base step k( ) <sup>s</sup> 2

Let us assume there are two $\delta \mathbf { s } ,$ , i.e., $\delta _ { i 1 , 1 } , \ \delta _ { i 2 , 1 }$ and $\delta _ { i 1 , 2 } , \delta _ { i 2 , 2 }$ . As the total sum of the s is fixed, they can be represented as follows using a positive constant :

$$
\delta_ {i 1, 1} = \alpha (\geq 0), \quad \delta_ {i 2, 1} = \beta + \lambda ,\tag{11}
$$

$$
\delta_ {i 1, 2} = \beta (\geq 0), \quad \delta_ {i 2, 2} = \alpha + \lambda .\tag{12}
$$

If Aif–clauseB of the lemma holds, i.e., $\mathbf { M A X } ( \delta _ { i j , 1 } )$ is less than or equal to $\mathbf { M A X } ( \delta _ { i j , 2 } )$ where $i = 1 - 2$ , then Athen–clauseB of the lemma also holds because $\alpha ^ { 2 } + ( \beta + \lambda ) ^ { 2 }$ is less than or equal to $\beta ^ { 2 } + ( \alpha + \lambda ) ^ { 2 }$ . Thus, the lemma holds when k is 2.

## B.2. Induction Hypothesis k( ) <sup>s</sup>n

Let us assume there are n $\delta \mathrm { s } ,$ i.e., $\delta _ { i 1 , 1 } { - } \delta _ { i n , 1 }$ and $\delta _ { i 1 , 2 } \ – \delta _ { i n , 2 }$ , and the lemma holds.

That is:

$$
\text { if } \operatorname{MAX} \left(\delta_ {i j, 1}\right) \leq \operatorname{MAX} \left(\delta_ {i j, 2}\right),
$$

$$
\text { then } \sum_ {j = 1} ^ {n} \left(\delta_ {i j, 1}\right) ^ {2} \leq \sum_ {j = 1} ^ {n} \left(\delta_ {i j, 2}\right) ^ {2},\tag{13}
$$

and:

$$
\sum_ {j = 1} ^ {n} \delta_ {i j, 1} = \sum_ {j = 1} ^ {n} \delta_ {i j, 2}.\tag{14}
$$

## B.3. Induction step $( k = n + 2 )$

Consider the case that two s are added to the above step, which are $\delta _ { i ( n + 1 ) , 1 } , \delta _ { i ( n + 2 ) , 1 }$ and $\delta _ { i ( n + 1 ) , 2 } ,$ $\delta _ { i ( n + 2 ) , 2 }$ . As the total sum of the s is fixed, they can be represented as follows:

$$
\delta_ {i (n + 1), 1} = \alpha^ {\prime} (\geq 0), \quad \delta_ {i (n + 2), 1} = \beta^ {\prime} + \lambda^ {\prime}.\tag{15}
$$

$$
\delta_ {i (n + 1), 2} = \beta^ {\prime} (\geq 0), \quad \delta_ {i (n + 2), 2} = \alpha^ {\prime} + \lambda^ {\prime}.\tag{16}
$$

If Aif–clauseB of the lemma holds, i.e., $\mathbf { M A X } ( \delta _ { i j , 1 } )$ is less than or equal to $\mathbf { M A X } ( \delta _ { i j , 2 } )$ where $j = 1 - ( n + 2 )$ , then Athen–clauseB of the lemma also holds because $\alpha ^ { \prime } { } ^ { 2 } + ( \beta ^ { \prime } + \lambda ^ { \prime } ) ^ { 2 }$ is less than or equal to ${ \beta ^ { \prime } } ^ { 2 } + ( \alpha ^ { \prime } + \lambda ^ { \prime } ) ^ { \dot { 2 } } .$ . For $j = 1 - n$ $\Sigma _ { j = 1 } ^ { n } ( \delta _ { i j , 1 } ) ^ { 2 }$ is less than or equal to $\Sigma _ { i = j } ^ { n } ( \delta _ { i j , 2 } ) ^ { 2 }$ by Induction Hypothesis. I

## Appendix C. Proof of Theorem 1

We prove the theorem by transformation from a well-known NP-complete problem, Optimal Linear

Arrangement Problem OLAP 5 . The OLAP is toŽ . <sup>w</sup> <sup>x</sup> find a one-to-one mapping function f such that:

$$
f: V \to \{1, 2, \dots , | v | \},
$$

$$
\text { minimizing } \sum_ {\{u, v \} \in E} | f (u) - f (v) | \leq k
$$

in a graph $G = \left( V , \ E \right)$ , where k is a positive constant.

Step 1: Based on the given schedule , there exists a nondeterministic polynomial function that determines if:

$$
\sum_ {q _ {i} \in \mathcal {Q}} \mathrm{QD} (q _ {i}, \sigma) \times \operatorname{freq} (q _ {i}) <   w,
$$

where w is a positive constant. Thus, the wireless data clustering problem is an NP problem.

Step 2: We assume the following in the wireless data clustering problem:

v Each query accesses only two data objects.

v The size of each data object is the same.

v The frequency of each query is the same.

Then, the wireless data clustering problem is easily transformed into the OLAP in polynomial timeŽ . by considering the data object as the node in the graph and the query as the edge in the graph. Thus, the wireless data clustering problem is an NP-hard problem.

Therefore, by Step 1 and Step 2, the problem of wireless data clustering is NP-complete.I

## References

<sup>w</sup> <sup>x</sup>1 S. Acharya, R. Alonso, M. Franklin, S. Zdonik, Broadcast disks: data management for asymmetric communication environments, Proceedings of ACM SIGMOD Conference, 1995, pp. 199–210.

<sup>w</sup> <sup>x</sup> 2 S. Acharya, M. Franklin, S. Zdonik, Disseminating updates on broadcast disks, Proceedings of Very Large Data Bases Conference, 1996, pp. 354–365.

<sup>w</sup> <sup>x</sup> 3 Y.D. Chung, M.H. Kim, An index replication scheme for wireless data broadcasting, Journal of Systems and Software 51 3 2000 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 C. Faloutsos, Multiattribute hashing using Gray codes, Proceedings of ACM SIGMOD Conference, 1986, pp. 227–238.

5 M.R. Garey, D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, Freeman Publishing, New York, 1976.

<sup>w</sup> <sup>x</sup> 6 T. Imielinski, S. Viswanathan, Adaptive wireless information systems, Proceedings of SIGDBS Conference, 1994, pp. 121–128.

7 T. Imielinski, S. Viswanathan, B.R. Badrinath, Data on air: organization and access, IEEE Transactions on Knowledge and Data Engineering 9 3 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 H.V. Jagadish, Linear clustering of objects with multiple attributes, Proceedings of ACM SIGMOD Conference, 1990, pp. 332–342.

<sup>w</sup> <sup>x</sup> 9 E.M. Reingold, J. Nievergelt, N. Deo, Combinatorial Algorithms: Theory and Practice, Prentice Hall, Englewood Cliffs, NJ, 1977.

<sup>w</sup> <sup>x</sup> 10 C. Su, L. Tassiulas, V.J. Tsotras, Broadcast Scheduling for Information Distribution, Wireless Networks, New York, 1998.

![](/api/attachments/QGEW9EJ4/fulltext/images/9671f1f409b00c6813c3455baeed2cd768693f9dc5d483380a85824c204c97bb.jpg)  
semistructured data management.  
Yon Dohn Chung received his BS degree in Computer Science from the Korea University, Seoul, Korea, in 1994, and his MS and PhD degrees in Computer Science from Korea Advanced Institute of Science and Technology Ž . KAIST , Taejon, Korea, in 1996 and 2000, respectively. He is currently a postdoctoral fellow in the Department of Computer Science at KAIST. His research interests include mobile computing, OLAP, data warehouse, and

![](/api/attachments/QGEW9EJ4/fulltext/images/e52c733805871a9614b31debefd123efe2cb8bde671f2d58e67919d069cb71b4.jpg)

Myoung Ho Kim received his BS and MS degrees in Computer Engineering from the Seoul National University, Seoul, Korea, in 1982 and 1984, respectively, and his PhD degree in Computer Science from Michigan State University, East Lansing, MI, in 1989. In 1989, he joined the faculty of the Department of Computer Science at KAIST, Taejon, Korea, where currently he is a professor. His research interests include database systems, OLAP, mobile information sys-

tems, data mining, information retrieval and distributed processing. He is a member of the ACM and the IEEE Computer Society.
