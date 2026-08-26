---
otero_id: 18907
otero_key: "CAQGABQX"
title: "An evaluation method for the availability of a distributed database management system"
authors: "Heeseok Lee"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90016-m"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# An evaluation method for the availability of a distributed database management system

Heeseok Lee

University of Nebraska, Omaha, NE 68182, USA

The availability of a distributed database management system is defined as the fraction of transactions that are successfully executed out of all transactions that are submitted to the system over a given time interval. Several variables that determine availability are addressed. These determinants are categorized as transaction traffic, reliability measures, data distribution, concurrency control, and fault tolerance. An evaluation expression for availability is presented in terms of these determinants. The method proposed in this paper is shown to provide several advantages compared to previous methods.

Keywords: Availability; Availability evaluation; Reliability; Distributed database management system

![](/api/attachments/CAQGABQX/fulltext/images/a07f893f571d40167a05b5d9cfe2a46f035474a867201e06e2b19b90672a45fb.jpg)

Heeseok Lee is an Assistant Professor of Management Information Systems at the University of Nebraska at Omaha. He held his Ph.D. in Business Administration from the University of Arizona. He received his B.S. in Industrial Engineering from Seoul National University and an M.S. in Industrial Engineering from Korea Advanced Institute of Science & Technology. Dr. Lee taught Management Information Systems at the University of Arizona and State University of

Minnesota-Moorhead. His current research interests include distributed information systems, performance evaluation of computer and telecommunication systems, and systems analysis and design. His research papers appear in such journals as Information and Management, Journal of Systems and Software, European Journal of Operational Research, Annals of Operations Research, Computers and Industrial Engineering, Computers and Operations Research, and Systems Science.

Correspondence to: Heeseok Lee, Department of Information Systems and Quantitative Analysis, College of Business Administration, University of Nebraska, Omaha, NE 68182, USA. hlee@odin.unomaha.edu.

## 1. Introduction

Advances in telecommunication technologies coupled with increase in organizational need for operations involving dispersed data have made distributed information processing an important alternative for information service. A distributed information system consists of several data files that are controlled and coordinated by a distributed database management system. Transactions read or write data files that are located at geographically dispersed sites. For a detailed description of distributed database management system, see [3].

Availability is an important performance measure in distributed database management systems. Availability is defined as the fraction of transactions that complete on time out of all transactions that are submitted to the database system during a specified period (say one month). In distributed databases, availability can be improved by sharing data among heterogeneous sites. Such sharing of data also adds design complexity compared with a centralized database management system.

Several failures and design issues affect availability. For instance, failures of processors and/or transmission links in computer-communication networks may cause some transactions to be incomplete at a particular time. Transactions themselves may fail, due to their own errors. If the file containing the data item requested resides at a remote site, the transaction request must be routed to that site through communication channels. Clearly, therefore, availability depends upon hardware and data file configurations, such as file allocations, transaction routing, network reliability, system reliability, transaction reliability, etc.

Irani and Khabbaz [5] originally investigated an expression for availability in the context of distribution of data and the design of communication links. Their model has been used for availability evaluation in the design of distributed computing system (see [6] and [7]). Irani and Khabbaz's method approximates availability based on the assumption that a communication networks is highly reliable; i.e., the network reliability is close to one. The emphasis of this method is on query transactions; i.e., it ignores update transactions.

In this paper we discuss several variables that determine availability. Based on these determinants, we proceed to provide its evaluation expression within the framework of query and update operations. We consider an important aspect of transaction operation, namely query transaction routing, because it is a common strategy to transfer query transactions that attempt to access data items residing at remote sites. Furthermore, we incorporate several key aspects of distributed information processing, such as transaction reliabilities, s-t terminal reliabilities, etc. Finally, it is shown that the availability evaluation method proposed in this paper has several advantages over the other method.

## 2. Availability determinants

Let us consider a distributed database management system that operates on a communication network. A file in this system is a collection of data items. A transaction can be defined as an atomic unit of file access, i.e., a read or write operation on data items in the system. The transaction must be a unit of consistent and reliable computation. Transactions may be identified as belonging to various classes. However, for the evaluation of availability, transactions are categorized as queries and updates.

It is important to note that a single query or update is posed as a transaction. A query transaction requests data retrieval only. However, an update transaction requires the modification of current data content. While a query reads a single data item that has been requested, an update must reference and write all of data items which contain the information to be updated.

A steady-state availability is affected by a variety of system variables. These are categorized as transaction traffic, reliability measures, data distribution, and concurrency control and fault tolerance, as follows:

1. Transaction traffic. In distributed databases, load balancing policies determine how transactions are assigned to each site. The database manager can estimate the volume of transactions that must be processed at each site. Traffic intensities of query and update transactions needs to be measured so that availability can be evaluated.

2. Reliability measures. Due to the potential for failure of hardware and software components of distributed databases, certain transaction requests may be lost at a particular point of time. Evaluating availability requires identifying the types of failures with which the system has to deal. The corresponding reliabilities must be measured to evaluate availability. In distributed cases, the database manager has to deal with four types of failures: transaction, site, media, and communication [9].

\- Transaction failures. Transactions may fail for a number of reasons: incorrect input data, deadlock, abort by concurrency control algorithm, etc. The common approach in cases of transaction failure is to reset the database to its state prior to the start of this transaction.

\- System failures. A distributed database management system consists of hardware (CPU, main memory, power supply, etc.) and software at each site. Failures can result in the loss of main memory contents. This leads to a failed site that is unreachable from other sites.

\- Media failures. Media failures refer to failures of the secondary storage devices (i.e., disks). Transactions may or may not need to access disks at each site.

\- Communication failures. Communication between sites can fail due to link and/or system/media failures. Such communication failures are unique to distributed systems.

3. Data distribution. Query and update transactions involve a need for data access. Therefore, it is not surprising to find that availability also depends upon distribution of the data in distributed databases. Distributing the data determines where and how data files are located and how queries are routed over geographically dispersed sites. If the database manager allocates most files to highly reliable sites and routes queries through highly reliable links, availability can be kept very high. Constraints may, however, occur due to low storage capacities of sites and slow links.

4. Concurrency control and fault tolerance. The level of concurrency in transaction processing and a need for fault tolerance impact on availability. Increases in the level and needs add design complexity. A variety of concurrency control techniques (for example, two-phase locking or time stamping) and fault tolerance mechanisms (for example, two-phase commit protocol) have been introduced. Clearly, the improvement level of availability depends upon the particular software mechanisms adopted. Improvements through concurrency control lead to improved availability of transaction. In contrast, software mechanisms for fault tolerance affect the type of failure dealt with. For instance, recovery protocols that deal with network partitioning due to communication line failures may prevent the loss of messages and thus improve the availability of the communication link. Typically, fault tolerance mechanisms are developed to enhance the availability of transaction, site, and communication.

In summary, four key variables that impact on availability are important. This implies that the database manager can deal with several design issues to further achieve cost effectiveness of a distributed database management system. For instance, transactions can be balanced among sites, so that availability can be enhanced. However, one design problem cannot be solved in isolation, because of interdependence of design issues: the relationship between availability determinants and the related design issues is depicted in Figure 1. An evaluation expression for availability based on these determinants is presented in the following section.

## 3. Notation and evaluation

In this section, the following notation is used to evaluate steady-state availability.

![](/api/attachments/CAQGABQX/fulltext/images/506774ca6e932f3173d303d4c1f9c61b1a6b129c8c9dafde8a12499455207544.jpg)  
Fig. 1. Availability determinants and related design issues in distributed database management systems.

1. Transaction traffic:

$\lambda$ total transaction request rate to the system

$\lambda^q$ total query transaction request rate to the system

$\lambda^{u}$ total update transaction request rate to the system

$\lambda_{i}$ mean transaction request rate of file $i$ $\lambda_{is}$ mean transaction request rate of file $i$ at site $s$

$\lambda_{is}^{q}$ mean query transaction rate of file $i$ at site $s$

$\lambda_{is}^{u}$ mean update transaction rate of file $i$ at site $s$

## 2. Reliability measures:

$R_{n}$ network reliability

$r_{st}$ s-t terminal reliability

$r_i$ reliability of site (node) $i$

$s_i$ reliability of system $i$

$m_{i}$ reliability of media (disk) $i$

$p_i$ probability of transactions that need to access disk among those arriving at site $i$

$t_{is}^{q}$ reliability of query transaction of file $i$ at site $s$ $t_{is}^{u}$ reliability of update transaction of file $i$ at site $s$ $l_{ij}$ reliability of link between site $i$ and site $j$

3. Data distribution decisions: $f_{is}$ file allocation decision variable $q_{isk}$ query transaction routing decision variable

4. System parameters:
C communication network
F total number of files on C
S total number of sites on C $\Phi$ availability of distributed database management system $\Phi^{q}$ query availability $\Phi^{u}$ update availability $\Phi_{approx}$ approximate measure of availability

Among variables that affect availability, the database manager first has to estimate reliability measures and transaction traffic intensities. Data distribution decisions are typically made after these are known.

File allocation and query routing assignment are decided by available file allocation models. A variety of such models can be found in several sources (e.g., see [4] or [10]). The file allocation decision variable $f_{is}$ is one if file i is located in site s; otherwise, it is zero. The query transaction routing decision variable $q_{isk}$ is the percentage that queries of file i are routed to site k among queries of file i arriving at site s.

Before using reliability measures directly to evaluate a steady-state availability of a system, it should be pointed out that the database manager is responsible for adjusting the reliability measures by taking into account software mechanisms for concurrency control and/or fault tolerance. For instance, if the level of improvement by concurrency control in query processing is estimated as $c^{q}(c^{q} \geq 1)$ , the corresponding query reliabilities are improved so that $t_{is}^{q}$ becomes $c^{q}t_{is}^{q}, \forall i, s$ .

We can now evaluate steady-state availability. We first note that site reliability $r_{i}$ can be computed by considering the reliabilities of several CPUs, main memory, and disks at site i. If transactions need to access disks, both the system and disks must be available so that the transactions can complete successfully; otherwise, they can complete only if the system (i.e., CPUs and main memory) is available. Hence, the site reliabilities can be computed as

$$
r _ {i} = s _ {i} m _ {i} p _ {i} + s _ {i} (1 - p _ {i}), \forall i = 1, \dots , S.
$$

Query transactions in distributed databases operate as follows. If data items requested by queries are located locally, the queries receive file service at that site; otherwise, they are transferred to the site where the file containing the requested data items is located. In other words, it is required that

$$
\sum_ {t \neq s} ^ {S} q _ {i s t} + f _ {i s} = 1, \forall i = 1, \dots , F, s = 1, \dots , S.
$$

According to this query expression, for the queries that arrive at site s and request data items of file i, the probability that these queries complete is $r_{s}f_{is}$ if $f_{is}=1$ ; otherwise the probability is $\sum_{t\neq s}r_{st}q_{ist}$ in terms of s-t terminal reliability. Here, the s-t terminal reliability is the probability that site s can communicate with site t. In contrast, the network reliability is defined as the probability that all operative site pairs in a communication network are able to communicate. For an excellent survey of several reliability measures in communication networks, readers are referred to Ball's paper [2].

s-t terminal reliability depends upon site reliabilities and/or link reliabilities. A method to compute s-t terminal reliabilities has been proposed by Ball, but we should point out that reliability analysis on networks in which only links fail (for example $[8]$ ) cannot be directly adopted. An exact expression for availability of query transactions can be represented as

$$
\Phi^ {q} = \frac {1}{\lambda^ {q}} \sum_ {i = 1} ^ {F} \sum_ {s = 1} ^ {S} \lambda_ {i s} ^ {q} t _ {i s} ^ {q} \left[ \sum_ {t \neq s} r _ {s t} q _ {i s t} + r _ {s} f _ {i s} \right].
$$

Updates are required to be transferred to all sites that contain data items to be modified. An update transaction is successfully executed if all update messages transferred are complete. Hence, update availability can be represented as

$$
\Phi^ {u} = \frac {1}{\lambda^ {u}} \sum_ {i = 1} ^ {F} \sum_ {s = 1} ^ {S} \lambda_ {i s} ^ {u} t _ {i s} ^ {u} \prod_ {\substack {k \\ f _ {i s} = 1}} r _ {s k}.
$$

For the sake of convenience, we denote the notation $r_{kk}$ by $r_k$ .

Finally, availability can be evaluated as the weighted sum of query availability and update availability as follows.

$$
\begin{array}{l} \Phi = w ^ {q} \Phi^ {q} + w ^ {u} \Phi^ {u} \\ = \frac {w ^ {q}}{\lambda^ {q}} \sum_ {i = 1} ^ {F} \sum_ {s = 1} ^ {S} \lambda_ {i s} ^ {q} t _ {i s} ^ {q} \left[ \sum_ {t \neq s} r _ {s t} q _ {i s t} + r _ {s} f _ {i s} \right] \\ + \frac {w ^ {u}}{\lambda^ {u}} \sum_ {i = 1} ^ {F} \sum_ {s = 1} ^ {S} \lambda_ {i s} ^ {u} t _ {i s} ^ {u} \prod_ {\substack {k \\ f _ {i s} = 1}} ^ {k} r _ {s k}. \end{array}
$$

The database designer has the responsibility to assign relative weights $w^{q}$ and $w^{u}$ . Good candidates are the ratios of query and update arrival rate to total arrival rate, i.e., $w^{q} = \lambda^{q}/\lambda$ , and $w^{u} = \lambda^{u}/\lambda$ .

## 4. Method comparison

The Irani and Khabbaz's availability expression (for convenience denoted by $\Phi_{approx}$ ) has been adopted for availability evaluation of distributed database management system. After minor arrangements, this expression can be represented as

$$
\Phi_ {a p p r o x} = \frac {R _ {n}}{\lambda} \sum_ {i = 1} ^ {F} \lambda_ {i} \left[ 1 - \prod_ {s = 1} ^ {S} \left(1 - r _ {s} f _ {i s}\right) \right].
$$

It should be pointed out that $\lambda_{i}=\sum_{s=1}^{S}\lambda_{is}=\sum_{s=1}^{S}(\lambda_{is}^{q}+\lambda_{is}^{u})$ , $\forall i=1,\cdots,F$ and $\lambda=\sum_{i=1}^{F}\lambda_{i}$ . A number of methods have been proposed to measure network reliability, $R_{n}$ , in $\Phi_{approx}$ . For example, readers are referred to [1].

It is noted that network reliability is assumed to be very high (i.e., close to one) to derive $\Phi_{approx}$ . It is also assumed that transactions are completely reliable. This evaluation does not distinguish the difference between query and update transactions. These points show that $\Phi_{approx}$ is indeed approximate. Furthermore, the fact that query routing decision is ignored in $\Phi_{approx}$ is significant, because routing is an important issue in the design of distributed databases.

We therefore explore several advantages of $\Phi$ over $\Phi_{approx}$ .

1. $\Phi$ requires no assumptions on reliabilities, so it is more accurate.

2. Both queries and updates can be considered in availability evaluation by using $\Phi$ . However, $\Phi_{approx}$ considers queries only.

3. Query transaction routing assignment is incorporated so that further cost-effectiveness of database management system can be achieved.

4. $\Phi_{approx}$ usually underestimates availability due to lack of consideration of query transaction routing and transaction reliabilities. This underestimate may be offset by the assumption of very high network reliability.

5. If we confine ourselves to queries (equivalently, assuming $w^{u}=0$ ), $\Phi$ is a linear function of file allocation and query routing ( $\Phi_{approx}$ is a nonlinear function). Let us consider the case of maximizing availability by determining file allocation and query routing operation for given values of system and link reliabilities. If we adopt the objective as $\Phi$ instead of $\Phi_{approx}$ , then the optimization model will fall into the class of linear integer programming problem, which is relatively easier to solve than a nonlinear integer programming problem using $\Phi_{approx}$ .

To illustrate the suitability of the evaluation expression, let us consider a 2-node 1-link system with a single file (Figure 2). For simplicity, a query-intensive system is used, i.e., the sample system deals with the case of no update. This example is simple enough to highlight the significance of the difference between $\Phi_{approx}$ and $\Phi$ . Transaction traffic is denoted by $\lambda = \lambda_1 = 1$ and $\lambda_{11} = \lambda_{12} = 0.5$ . File allocation and query routing decisions are $f_{11} = 1$ , $f_{12} = 0$ , $q_{112} = 0$ and $q_{121} = 1$ . We assume that transactions are completely reliable, i.e., $t_{is}^{q} = 1$ , $\forall i, s$ . Let us denote the reliabilities as $r_1 = r_2 = l_{12}(= l_{21}) = p$ . It can be easily seen that $R_n = r_{12}(= r_{21}) = p^3$ .

Finally, we can compute $\Phi_{approx} = p^4$ and $\Phi = (p + p^3) / 2$ . It is noted that $\Phi_{approx} \leq \Phi$ for $0 \leq p \leq 1$ . Hence, $\Phi_{approx}$ underestimates $\Phi$ . The difference tends to be smaller as $p$ increases, i.e., as

$$
\bigcirc \quad l _ {1 2} = p \quad r _ {2} = p
$$

Fig. 2. 2-node 1-link example.

Table 1  
$\Phi$ and $\Phi_{approx}$ for the example

<table><tr><td>p</td><td>0.5</td><td>0.9</td><td>0.99</td><td>0.999</td><td>0.9999</td><td>1.0</td></tr><tr><td> $\Phi_{approx}$ </td><td>0.0625</td><td>0.6561</td><td>0.9606</td><td>0.9960</td><td>0.9996</td><td>1.0000</td></tr><tr><td> $\Phi$ </td><td>0.3125</td><td>0.8145</td><td>0.9802</td><td>0.9980</td><td>0.9998</td><td>1.0000</td></tr></table>

network reliability increases. This property is illustrated in Table 1.

## 5. Concluding remarks

By sharing data among several computing sites, the level of availability can be enhanced compared to centralized systems. However, this improvement in availability can only be achieved through its appropriate evaluation.

This research has attempted to provide an effective methodology to evaluate availability of a distributed database management system. Several variables that determine availability have been addressed. Design issues dependent on availability improvement are thus identified. Our method is more accurate, by using s-t terminal reliability, than one previous expression that is an approximation based on network reliability. Furthermore, our method has additional advantages, because it incorporates query routing assignment, an important aspect of distributed databases in a communication network, as well as other system considerations.

## Acknowledgement

The author thanks the editor whose suggestions improved the presentation of this paper. This research was supported in part by the International Center for Telecommunications Management at the University of Nebraska.

## References

[1] K.K. Aggarwal and S. Rai, “Reliability evaluation in computer-communication networks”, IEEE Transactions on Reliability, vol. R-30, 1981, pp. 32–35.

[2] M.O. Ball, “Computing network reliability”, Operations Research, vol. 27, 1979, pp. 823–838.

[3] S. Ceri and G. Pelagatti, Distributed Databases: Principles and Systems, McGraw Hill, 1984.

[4] L.W. Dowdy and D.V. Foster, “Comparative models of the file assignment problem”, ACM Computing Surveys, vol. 14, 1982. pp. 287–313.

[5] K.B. Irani and N.G. Khabbaz, “A methodology for the design of communication networks and the distribution of data in distributed supercomputer systems”, IEEE Transactions on Computers, vol. C-31, 1982, pp. 419–434.

[6] H.K. Jain and A. Dutta, “Distributed computer system design: a multicriteria decision-making methodology”, Decision Sciences, vol. 17, 1986, pp. 437–453.

[7] H.K. Jain, “A comprehensive model for the design of distributed computer systems”, IEEE Transactions on Software Engineering, vol. SE-13, 1987, pp. 1092–1104.

[8] K.B. Misra and T.S.M. Rao, “Reliability analysis of redundant networks using flow graphs”, IEEE Transactions on Reliability, vol. R-19, 1970, pp. 19–24.

[9] M.T. Ozsu and P. Valdureiz, Principles of Distributed Database Systems, Prentice Hall, 1991.

[10] B.W. Wah, “File placement on distributed computer systems”, IEEE Computer, vol. 17, 1984, pp. 23–32.
