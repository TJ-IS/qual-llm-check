---
otero_id: 21099
otero_key: "JS7QBAFW"
title: "Optimal pricing policies of web-enabled application services"
authors: "Hsing Kenneth Cheng; Gary J. Koehler"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00073-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal pricing policies of web-enabled application services

Hsing Kenneth Cheng \*, Gary J. Koehler

Department of Decision and Information Sciences, Warrington College of Business Administration, University of Florida PO Box 117169, Stuzin 351 Gainesville, FL 32611, USA

Accepted 20 March 2002

## Abstract

Ubiquitous and inexpensive access over the World Wide Web has fueled the growth of application service providers (ASPs). ASPs are ‘‘service firms that provide a contractual service offering to deploy, host, manage, and lease what is typically packaged application software from a centrally managed facility.’’ The application software products offered by ASPs range from standard productivity tools to expensive applications such as Enterprise Resource Planning systems like SAP or PeopleSoft. In this paper, we model the economic dynamics between the ASP and its potential customers. Under a realistic economies-of-scale assumption, we show that there exists a unique rational expectation equilibrium. Optimal pricing policies for the ASP are derived analytically and insights are demonstrated through numerical explorations. <sup>D</sup> 2002 Published by Elsevier Science B.V.

Keywords: Application service providers (ASPs); Web hosting; Pricing policy; Economics of electronic commerce

## 1. Introduction

Several coalescing forces have once again made an old software pricing model attractive [5]. In the 1960s and 1970s, small to medium-sized companies gained access to expensive computing resources and software through time-share services and service bureaus. Today, similar dynamics are driving companies to similar services for expensive applications such as Enterprise Resource Planning systems like SAP or PeopleSoft. These new service providers charge on a pay-per-use basis, a flat-fee basis, or some mixture thereof. It is estimated that application outsourcing will be a \$21 billion industry by 2001 [14] and a o1.8 billion industry by 2003 [20].

Ubiquitous and inexpensive access over the World Wide Web has fueled the growth of software rental on either a pay-per-use basis or a subscription basis. This strategy is reinforced by the emergence of thin-client computers. Thin-client computers, in the form of network computers, Web TV’s or the like, are designed with minimal resources, and operate by downloading applications on an as-needed basis. These applications usually run on the service provider’s system with a front-end running on the thin-client machine. Fig. 1 shows the application service provider (ASP<sup>1</sup>) architecture presented on TRB Solution’s web pages.

![](/api/attachments/JS7QBAFW/fulltext/images/2f511c045e0929955ca06afbc952c1c2631eb1342a6391562df5bab67de2a974.jpg)  
Fig. 1. ASP architecture given by TRB Solutions (http://trbsolutions.com)<sup>2</sup>.

Today, such service providers are advertised under titles such as ‘‘Computer Utility Companies’’ or ‘‘Application Service Providers (ASPs).’’ International Data Corporation defines an ASP as ‘‘service firms that provide a contractual service offering to deploy, host, manage, and lease what is typically packaged application software from a centrally managed facility’’ [20]. A good source for current developments can be found at http://www.aspnews.com/.

Some ASPs offer industry-specific software on a pay-as-you-go basis (such as Utiligent’s offering to the utilities industry [10]). One provider offers a onestop shopping alternative for a variety of software products [14], even inviting software providers to partner with them (see Interliant AppsOnline at http://www.appsonline.com/index.html). Mainline software companies, such as Lotus Development, are actively exploring software rental options for their products [11]. And, as in the early days of timesharing, even expensive software is being offered; EDS’s Systemshouse http://www.shl.com/) offers ERP software. Early in 1999, Electronic Data Systems announced that it would provide SAP’s R/3 to small and midsized companies over networks with a service called Keysource. They plan on charging from \$425 to \$660 on a per-user, per-month basis. Other highend ASPs include Usinternetworking, IBM Global Services. USWeb, Oracle Online, Corio, ServiceNet and World Technology Service [20].

The advantages of this business model stem from several sources. First, small to medium-sized companies can gain access to systems not otherwise available. Second, companies can avoid high initial capital expenditures on expensive thick-client hardware, on software licenses and on installation costs. IDC estimates a 10 – 50% savings here [10]. Normal maintenance is easier since upgrades can be automated. Another advantage, which is found in all types of outsourcing, is that management can focus on mission-critical concerns and not be distracted with IT infrastructure problems.

ASPs use a variety of charging algorithms for their services. Some charge a yearly fee for each workstation. Others charge a per-user, per-month fee. Both of these schemes are tantamount to a fixed fee. Some ASPs see an ebb and flow of software needs and charge a subscription fee covering a time period plus a pay-as-you-go fee (charged on a use basis or a timemetered basis). It is this latter case that we study in this paper. In economics, such pricing schemes are known as uniform two-part tariffs (see Oi [18]). We start our analyses with two-part tariff since it is a more general pricing scheme including fixed price and metered charge as its special cases.

ASPs face a more complex environment than that typically found in two-part tariff studies because of congestion created by processing its customers’ computing needs. For example, Oi [18] took as his prototypical setting an amusement park (Disneyland in particular) that charges an entrance fee (the fixed costs) and a per-ride fee (Disney no longer uses a twopart tariff). Anyone who has visited one of Disney’s theme parks knows that long lines precede the more popular rides. Oi [18] did not consider such congestion and possible non-service. ASPs, however, must provide sufficient resources to assure a minimal level of service.

The effect of price on the management and control of congestible resources has been an active research area. Naor [17] studied how to regulate queue sizes by levying tolls on M/M/1 queues with balking (arriving customers need not join the queue). Edelson and Hildebrand [3] extended this model to include a two-part tariff. Dolan [1] was among the first to embed queuing models in a microeconomic framework to study the role of congestion cost. However, it was Mendelson’s [15] presentation and analysis of similar problems in continuous time that became most widely recognized. Mendelson [15] found that the net value maximizing price equals the expected delay cost inflicted on the rest of the system not perceived by the generating user, a cost termed the ‘‘externality’’ cost. Mendelson and Whang [16] extended Mendelson’s [15] work to consider M/M/1 queuing system with multiple user classes. Mendelson and Whang [16] derived a decentralized pricing mechanism that is optimal and incentive compatible. This means that each user makes an individual decision on whether to join the system at what priority level that will maximize the objective of the system as a whole.

Recently, similar methodology was applied to research problems related to the Internet. For example, MacKie-Mason and Varian [13] studied the effect of congestion pricing on the efficient usage of Internet services. Delay is defined as total use divided by capacity. Congestion pricing ‘‘internalizes’’ the externality resulting from the incremental usage of a shared resource degrading the quality to all. They found that competitive pricing would maximize net social benefits. Gupta et al. [7,8] studied many pricing issues for Internet services involving the quality of service (QoS) dimension. In particular, they studied dynamic pricing models based on levels of congestion and contrast their results with fixed charge and time-based pricing mechanisms. They also note that these congestion externalities can be priced by a two-part tariff where the fixed charge meets goals of cost recovery and the congestion charges handle resource allocation. Congestion is handled based on changing prices as perceived or predicted demand varies in different QoS classes.

All the aforementioned models in the literature, with the exception of Gupta et al. [7,8], invariably deal with the setting of a single server, which renders them inadequate in analyzing the problem facing an ASP. The ASP is required by its customers to provide complete protection of various system resources. To meet this requirement, the ASP either partitions the mainframe server into several ‘‘virtual machines’’ (see Silberschatz et al. [19]) or uses several different servers. Each virtual machine is completely isolated from all other virtual machines with no direct sharing of system resources. Alternatively, the ASP can acquire several UNIX servers, each of which is dedicated to an individual customer. Unlike the congestion created by competing for the same single server studied in prior literature, the customers signed up for ASP services compete for the access to a virtual machine (or server) from a pool of virtual machines (or servers). The objective of our research is to examine the interrelationship between price and queuing delay in this distinct setting involving multiple servers with finite calling population.

We consider a two-part pricing scheme to model the ASP problem, but depart from the models discussed above as follows. First, unlike Naor, we do not consider balking. Instead, the ASP reimburses customers for time spent waiting for services. We also require a minimal average performance guarantee. We look at the ASP problem from several perspectives. We define the Short-Run Problem as the period during which the ASP cannot alter the service guarantee or the capacity. Over longer periods, the ASP can increase server capacity and then provide better service and performance guarantees. We call this problem the Service Provider’s Problem (SPP). The most important finding of our research is that the ASP has wide latitude in setting the optimal pricing policy. Specifically, the optimal pricing policy need not be in the form of a fixed fee, metered price, two-part tariff, or two-part tariff plus reimbursement. Any family of pricing schemes is optimal as long as the pricing policy satisfies a relationship we identify in Section 3.

In Section 2, we present the Service Provider’s Problem (SPP). The problem is studied in Section 3 through a sequence of models, starting with the shortrun problem. We determine a family of optimal pricing policies depending on the type of pricing structure desired by the ASP. These range from pure policies having only fixed or variable costs, to policies having fixed, variable and reimbursement cost components. In Section 3, we show that the short-run problem has a unique solution when the probability distribution of customers’ reservation prices satisfies a broad condition. In Section 4, we perform numerical explorations to gain insights into the properties of optimal SPP solutions. We conclude with a discussion in Section 5.

## 2. Model

Assume N potential customers need to run a software product during a specified time period $T ,$ set at 1 year in this paper (notation is summarized in Table 1). This requirement can be met in either one of two ways. In the first, a user may implement the product at an annualized ‘‘ownership’’ cost of OC (which includes software costs, maintenance costs, operating costs, costs of possibly upgrading to bigger computers, etc.) and run it on their own computer. In the second way, a user may subscribe to an ASP service with an annual fixed fee of F and pay p per unit of time usage. We assume that the service provider will offer a reimbursement to customers using its service, $y ,$ for time spent waiting for access to a server. The ASP option may allow the user to have a less expensive computer and to incur lower operating and support costs. On average, a minimal number of required usages of $d \left( \geq 0 \right)$ will be needed during this time period and, thus, a service provider must offer this performance guarantee.

<table><tr><td colspan="2">Table 1Summary of notation</td></tr><tr><td colspan="2">Customers</td></tr><tr><td>N</td><td>number of potential customers</td></tr><tr><td>M</td><td>number of actual customers</td></tr><tr><td colspan="2">Service parameters</td></tr><tr><td>s</td><td>number of servers available</td></tr><tr><td> $\mu$ </td><td>exponential service rate for each servers</td></tr><tr><td> $\lambda$ </td><td>exponential inter-arrival rate for each customer, requires  $\lambda < s\mu$ </td></tr><tr><td>T</td><td>the ASP service contract period</td></tr><tr><td>d</td><td>minimum number of accesses required over time T, the performance guarantee</td></tr><tr><td colspan="2">Revenue and costs</td></tr><tr><td>OC</td><td>annualized software ownership costs, including software cost, maintenance costs, operating costs, and costs of possibly upgrading to bigger computers, etc.</td></tr><tr><td>F</td><td>fixed fee for service</td></tr><tr><td>p</td><td>metered price of service</td></tr><tr><td>y</td><td>reimbursement to customers for waiting to access service</td></tr><tr><td>R</td><td>customer reservation price, a random variable with pdf  $f(r) > 0$ </td></tr><tr><td> $\Re$ </td><td>distribution function for R</td></tr><tr><td> $\omega(F,p,y|s)$ </td><td>revenue with pricing policy ( $F,p,y$ ) given s servers</td></tr><tr><td>c(s)</td><td>cost for supplying s servers</td></tr><tr><td colspan="2">Queue statistics</td></tr><tr><td> $L_q$ </td><td>expected queue length</td></tr><tr><td>L</td><td>expected number of customers in the queue</td></tr><tr><td> $W_q$ </td><td>expected waiting time in queue (excludes service time)</td></tr><tr><td>W</td><td>expected waiting time in queue (includes service time)</td></tr><tr><td colspan="2">Other</td></tr><tr><td> $|x|$ </td><td>the largest integer less than or equal to x</td></tr><tr><td> $|x|$ </td><td>the smallest integer greater than or equal to x</td></tr><tr><td> $Z^+$ </td><td>non-negative integers</td></tr></table>

We assume that the need to use the software can be modeled as an exponential distribution with betweenusage rate, k, and that the required usage time can be modeled as an exponential distribution with rate $\mu .$ In the ASP setting, the customer has complete protection of various system resources (i.e., complete control of a virtual machine or a server), when the customer gains access to the ASP service. The customer may use the ASP service to process volumes of transactions. However, the same customer may not request access to another virtual machine or server, until the prior service request is finished. This implies that a customer cannot have more than one request in the waiting/service queue at a time. For all practical matters, there is no reason why a specific customer would need more than one request pending.<sup>3</sup> Then $( T ) / ( \lambda ^ { - 1 } + \mu ^ { - 1 } )$ is the expected number of times each individual customer uses the software in time T. We require $( ( T ) / ( \lambda ^ { - 1 } + \mu ^ { - 1 } ) ) \geq d$ to assure that customers achieve a minimal average usage.

The application service provider must decide on the price structure of the service $( F , p ,$ and y) and on the number of servers, $s ,$ it will provide (we require $\lambda < s \mu )$ . The cost of the servers (plus a version of the software product that will run in this configuration) is c(s).

We assume customers have a per time-unit reservation price, $R ,$ which is the valuation they place on using the software. This price is modeled as a random variable with continuous probability density function $f ( r ) { > } 0$ and $\Re ( r )$ its distribution. Depending on the price structure, implied waiting times, and customer reservation price of the service, customers must choose between subscribing to the ASP service or purchasing and using the software directly. Let $M ( \leq N )$ be the actual number of customers choosing to use the ASP service.

From basic queuing theory (see Section 2.7 of Gross and Harris [6] for example) we have the following. The ASP service system with M paying customers and s servers is a M/M/s queue with a finite calling population of size M. The arrival and service rates for such a system are

$$
\begin{array}{l} \lambda_ {n} = (M - n) \lambda \text {   for   } 0 \leq n \leq M, \text {   and   } \\ \mu_ {n} = \left\{ \begin{array}{l l} n \mu \text {   for   } 0 \leq n \leq s \\ s \mu \text {   for   } n \geq s \end{array} \right., \end{array}
$$

where n denotes the number of customers in the system (both in service and in the queue).

The expected queue length of customers waiting for service is

$$
L _ {q} = \sum_ {n = s} ^ {M} (n - s) P _ {n}
$$

and the expected number of customers waiting or being serviced is

$$
L = \sum_ {n = 0} ^ {M} n P _ {n}
$$

where

$$
P _ {0} = \frac {1}{\sum_ {n = 0} ^ {s - 1} \binom {M} {n} \left(\frac {\lambda}{\mu}\right) ^ {n} + \sum_ {n = s} ^ {M} \frac {M !}{(M - n) ! s ! s ! ^ {n - s}} \left(\frac {\lambda}{\mu}\right) ^ {n}}
$$

and

$$
P _ {n} = P _ {0} \left\{ \begin{array}{l l} \binom {M} {n} \left(\frac {\lambda}{\mu}\right) ^ {n} & 0 \leq n \leq s \\ \frac {M !}{(M - n) ! s ! s ^ {n - s}} \left(\frac {\lambda}{\mu}\right) ^ {n} & s \leq n \leq M \end{array} \right..
$$

Knowing these values, Little’s formulas [12] give us the expected waiting time in the queue excluding the service time

$$
W _ {q} = \frac {L _ {q}}{\lambda (M - L)}
$$

and with the service time

$$
W = \frac {L}{\lambda (M - L)}.
$$

## 2.1. The customer problem

The undiscounted expected net value to a customer over time period T who buys the software and has reservation price R is

$$
\frac {T}{(\lambda^ {- 1} + \mu^ {- 1})} \frac {R}{\mu} - \mathrm{OC}.
$$

The first term gives the expected number of usages over time period T and, the second term, the expected value per usage of the software. From this the software’s ownership cost is subtracted.

Alternatively, a customer using the ASP service has an expected total value of

$$
\frac {T}{(\lambda^ {- 1} + W)} \left(\frac {R - p}{\mu} + y W _ {q}\right) - F.
$$

The first term is the expected number of software usages which takes into account the expected waiting times until a server becomes free. The second term gives the value of using the software, net of the metered costs of use and any waiting time reimbursement allowances. The last term, $F ,$ is the fixed fee of subscribing to the service.

The expected number of customers who will choose the service is then

$$
\begin{array}{l} M = \left\lfloor N \cdot \operatorname{Prob} \left(\frac {T}{(\lambda^ {- 1} + W)} \left(\frac {R - p}{\mu} + y W _ {q}\right) - F \right. \right. \\ \left. \geq \frac {T}{(\lambda^ {- 1} + \mu^ {- 1})} \frac {R}{\mu} - \mathrm{OC}\right) \Bigg \rfloor \end{array}
$$

where txb is the largest integer less than or equal to x. The above equation means that the number of actual subscribers equals the proportion of potential customers who find the net value of using the ASP service greater than the net value of implementing the software by themselves.

## 2.2. The service provider’s problem

The service provider must determine the price structure $( F , p ,$ and $y )$ and the number of servers. The provider’s revenue is given by

$$
\omega (F, p, y \mid s) = M \left(F + \frac {T}{(\lambda^ {- 1} + W)} \left(\frac {p}{\mu} - y W _ {q}\right)\right)
$$

since M subscribers pay the fixed subscription fee, $F ,$ plus their net payment for all of their uses.

Assumption 1. Economies-of-Scale Assumption. We assume that economies-of-scale will produce a nominal cost for service (the fixed fee plus a total expected usage cost) being less than the annualized software ownership cost facing a potential subscriber. That is,

$$
F + \frac {T}{\lambda^ {- 1} + \mu^ {- 1}} \frac {p}{\mu} <   \mathrm{OC}.
$$

This assumption is supported in the trade press. For example, it is observed that ‘‘ASPs share cost among many customers, allowing for a much lower cost structure than traditional solutions’’ [2]. Savings are estimated at 30–70% by FutureLink (at www.futurelink. com).

A profit-maximizing service provider will solve the Service Provider Problem (SPP) as follows:

$$
\text {(SPP)} \max _ {s} \max _ {F, p, y} \omega (F, p, y \mid s) - c (s)\tag{1}
$$

s.t.

$$
\begin{array}{l} M = \left\lfloor N \cdot \operatorname{Prob} \left(\frac {T}{\lambda^ {- 1} + W} \left(\frac {R - p}{\mu} + y W _ {q}\right) - F \right. \right. \\ \left. \geq \frac {T}{\left(\lambda^ {- 1} + \mu^ {- 1}\right)} \frac {R}{\mu} - \mathrm{OC}\right) \Bigg \rfloor \end{array}\tag{2}
$$

$$
\frac {T}{(\lambda^ {- 1} + W)} \geq d\tag{3}
$$

$$
F, p, y \geq 0
$$

$$
s, M \in Z ^ {+}\tag{4}
$$

$$
s \geq \left\lceil \frac {\lambda}{\mu} \right\rceil
$$

where $Z ^ { + }$ is the set of non-negative integers and qxa is the smallest integer greater than or equal to x. Eq. (1) gives the net profit equal to the revenue less the cost of providing s servers. Eq. (2) reflects the solution to the customer problem. Eq. (3), the performance guarantee, assures that the ASP provides a minimal level of service. When inequalities (3) and (4) imply a negative profit solution, the service provider will choose not to offer the service.

## 3. Analysis

Our first insight is that Eq. (2) can be simplified.

Lemma 1. At an optimal solution

$$
\begin{array}{c} M = N \cdot \operatorname{Prob} \bigg (\frac {T}{(\lambda^ {- 1} + W)} \bigg (\frac {R - p}{\mu} + y W _ {q} \bigg) \\ - F \geq \frac {T}{(\lambda^ {- 1} + \mu^ {- 1})} \frac {R}{\mu} - \mathrm{OC} \bigg). \end{array}
$$

Proof. Please see Appendix A.. The next result tightens the problem statement. 5

Lemma 2. A non-trivial optimal solution to $S P P \ : ( i . e .$ $N \geq s \geq 0 )$ satisfies $M \geq s .$

Proof. Please see Appendix B.. Because of Lemma $^ { 2 , }$ we restrict $M \geq s$ in all formulations. 5

We now examine the Service Provider’s problem in a three-step process—each successively more involved. In the first case, we relax the performance guarantee and fix the number of servers. We call this the short-run problem since server capacity is fixed over short periods of time. The performance guarantee is introduced in the second step. Finally, using the first two steps, we examine the entire Service Provider problem (SPP).

## 3.1. Short-run problem (no performance guarantee)

With the number of servers fixed and the performance guarantee relaxed, SPP reduces to

$$
\left(\text { Short   -   run   SPP }\right) \max _ {F, p, y} \omega (F, p, y \mid s)
$$

$$
= M \left(F + \frac {T}{\left(\lambda^ {- 1} + W\right)} \left(\frac {p}{\mu} - y W _ {q}\right)\right)\tag{5}
$$

$$
\begin{array}{l} \text { s.t. } \\ M = N \cdot \operatorname{Prob} \left(\frac {T}{(\lambda^ {- 1} + W)} \left(\frac {R - p}{\mu} + y W _ {q}\right) - F \right. \end{array}
$$

$$
\geq \frac {T}{(\lambda^ {- 1} + \mu^ {- 1})} \frac {R}{\mu} - \mathrm{OC}\tag{6}
$$

$$
F, p, y \geq 0
$$

$$
M \in Z ^ {+}, M \geq s\tag{7}
$$

After algebraic manipulation, Eq. (6) can be rewritten as

$$
M = N \cdot \operatorname{Prob} \left(R \leq \frac {\mathrm{OC} - F - \frac {T}{\lambda^ {- 1} + W} \left(\frac {p}{\mu} - y W _ {q}\right)}{\frac {T}{(\lambda^ {- 1} + \mu^ {- 1}) \mu} - \frac {T}{(\lambda^ {- 1} + W) \mu}}\right),\tag{8}
$$

where R is the random variable describing potential customers’ valuation (reservation price) of using the software. Eq. (8) implies that no one will subscribe to the ASP service if the expected savings of annualized software cost (the first term in the numerator) is less than the expected cost of subscribing to the ASP service (the remaining terms in the numerator).

M appears on both sides of Eq. (8)—explicitly on the left and implicitly (in W and $W _ { q } )$ on the right. We follow the mechanism described in Katz and Shapiro [9] where a dynamic market process yields equilibrium via rational expectations as potential customers form priors on M. This equilibrium is uniquely determined under the economies-of-scale assumption as shown below.

Theorem 1. Unique Rational Expectation Equilibrium. Under the economies-of-scale assumption, there exists a unique rational expectation equilibrium in Eq. (8) for any distribution function R() on $( \theta , \infty )$

Proof. Please see Appendix C.

To find the optimal solution to the short-run SPP, we define $a ( F , p , y , M )$ and $b ( M )$ as follows:

$$
a (F, p, y, M) = \mathrm{OC} - F - \frac {T}{\lambda^ {- 1} + W} \left(\frac {p}{\mu} - y W _ {q}\right),
$$

and

$$
b (M) = \frac {T}{(\lambda^ {- 1} + \mu^ {- 1}) \mu} - \frac {T}{(\lambda^ {- 1} + W) \mu}.
$$

Under Theorem 1, Eq. (8) can be rewritten as

$$
M = N \Re \left(\frac {a (F , p , y , M)}{b (M)}\right),
$$

where R() is the distribution function of random variable R as defined earlier.Under our assumptions on $\Re ( )$ , its inverse is well-defined and

$$
a (F, p, y, M) = b (M) \Re^ {- 1} \left(\frac {M}{N}\right).
$$

Thus, the short-run SPP can be converted to an unconstrained optimization problem as follows:

$$
\max _ {s \leq M \leq N} V (M)\tag{9}
$$

where

$$
V (M) \equiv M \left(\mathrm{OC} - b (M) \Re^ {- 1} \left(\frac {M}{N}\right)\right).\tag{10}
$$

The optimal short-run ASP profit is found by evaluating $V ( M )$ for all possible M’s ranging from s to N.

Suppose $M ^ { * }$ solves Eq. (9) and that $V ^ { * } ( M ^ { * } )$ is the maximal short-run ASP profit.Then

$$
\begin{array}{l} \mathrm{OC} - F - \frac {T}{\lambda^ {- 1} + W ^ {*}} \left(\frac {p}{\mu} - y W _ {q} ^ {*}\right) \\ = b (M ^ {*}) \Re^ {- 1} \left(\frac {M ^ {*}}{N}\right) = \mathrm{OC} - \frac {V ^ {*} (M ^ {*})}{M ^ {*}} \end{array}
$$

so

$$
F + \frac {T}{\lambda^ {- 1} + W ^ {*}} \left(\frac {p}{\mu} - y W _ {q} ^ {*}\right) = \frac {V ^ {*} (M ^ {*})}{M ^ {*}}\tag{11}
$$

with $F , p , y \geq 0$ . This equation gives a family of pricing schemes that are enumerated in Table 2.

Eqs. (9) – (11) provide several useful managerial insights for the ASP. To find an optimal pricing policy, the ASP first calculates V(M) according to Eqs. (9) and (10) by varying M (from s to N). After $V ^ { * } ( M ^ { * } )$ is found, the values of $W _ { q } { } ^ { * }$ and $W ^ { * }$ become known. Then, the ASP has wide latitude of setting optimal pricing policies by applying Eq. (11). Specifically, the optimal pricing policy need not be in the form of a fixed fee, metered price, two-part tariff, or twopart tariff plus reimbursement. Any family of pricing schemes is optimal as long as the pricing policy $( F , p , y )$ satisfies Eq. (11), see Table 2. When a pricing policy satisfying Eq. (11) is instituted by the ASP, it will in turn induce an optimal number $( M ^ { * } )$ of customers to subscribe to the ASP service because of Eq. (8).

## 3.2. Short-run problem (with performance guarantee)

When the performance guarantee

$$
\frac {T}{(\lambda^ {- 1} + W)} \geq d
$$

is non-binding, the model is the same as the shortrun SPP model. If, however, it is binding, it follows that

$$
W _ {q} (M) \leq \left(\frac {T - d (\lambda^ {- 1} + \mu^ {- 1})}{d}\right),
$$

which in turn implies that M is bounded. Let $\bar { M }$ be the smaller of this bound and N. Hence, the short-run problem with a performance guarantee is transformed into:

Table 2  
Optimal pricing policies

<table><tr><td>Policy</td><td> $p^*$ </td><td> $y^*$ </td><td> $F^*$ </td></tr><tr><td>Fixed price</td><td>0</td><td>0</td><td> $\frac{V^*(M^*)}{M^*}$ </td></tr><tr><td>Fixed price with waiting-time allowance</td><td>0</td><td> $\frac{F - \frac{V^*(M^*)}{M^*}}{\frac{TW_q^*}{\lambda^{-1} + W^*}}$ </td><td> $\frac{V^*(M^*)}{M^*} \leq F < C$ </td></tr><tr><td>Metered usage</td><td> $\frac{\mu V^*(M^*)}{TM^*} (\lambda^{-1} + W^*)$ </td><td>0</td><td>0</td></tr><tr><td>Metered usage with waiting-time allowance</td><td> $\frac{\mu V^*(M^*)}{TM^*} (\lambda^{-1} + W^*) + \mu yW_q^*$ </td><td> $0 < y < \frac{C(\lambda^{-1} + \mu^{-1}) - \frac{V^*(M^*)}{M^*} (\lambda^{-1} + W^*)}{W_q^*T}$ </td><td>0</td></tr><tr><td>Two-part pricing</td><td> $\mu \left( \frac{V^*(M^*)}{TM^*} - \frac{F}{T} \right) (\lambda^{-1} + W^*)$ </td><td>0</td><td> $0 \leq F \begin{cases} < & C \\ \leq & \frac{V^*(M^*)}{M^*} \end{cases}$ </td></tr><tr><td>Two-part pricing with waiting-time allowance</td><td> $\mu \left( \frac{V^*(M^*)}{TM^*} - \frac{F}{T} \right) (\lambda^{-1} + W^*) + \mu yW_q^*$ </td><td> $\frac{\lambda^{-1} + W^*}{W_q^*T} \left( F - \frac{V^*(M^*)}{M^*} \right) < y$ </td><td> $\frac{V^*(M^*)}{M^*} \leq F < C$ </td></tr></table>

$$
\max _ {s \leq M \leq \bar {M}} V (M).
$$

The solution procedure described in the previous section and optimal policies in Table 2 still apply.

## 3.3. Long-run problem

Using the above results, the long-run problem, problem SPP, can now be restated as an enumerative problem

$$
\left(\text { SPP }\right) \max _ {\left\lceil \frac {\lambda}{\mu} \right\rceil \leq s \leq N} V ^ {*} (s) - c (s)
$$

where $c ( s )$ is the cost of the s servers and

$$
V ^ {*} (s) = \max _ {s \leq M \leq \bar {M}} V (M).
$$

Finding the optimal solution to the long-run problem involves a straightforward enumeration on the number of server s from $\left[ \lambda / \mu \right]$ to N. For each s, the corresponding $V ^ { * } ( s )$ is found by using the procedure described in Section 3.1. The ASP will choose the capacity $s ^ { * }$ that achieves the maximized $V ^ { * } ( s )$ . Once $s ^ { * }$ (and hence, $M ^ { * } )$ is determined, Table 2 can be used to set prices. In the next section, we examine some issues which simplify the solution of SPP.

## 3.4. Properties of SPP

Some distributions simplify the computational processes further. For example, the following result shows that the objective function in short-run SPP is unimodal.

Theorem 2. Unimodal Objective Function for General Distributions of Reservation Price. For any general distributions of customers’ reservation price R with the property f(r)>0, the objective function of short-run SPP is unimodal.

## Proof. Please see Appendix D.

In the next section, uniform distributions are used for the numerical explorations of SPP and to illustrate the properties of Theorem 2. It is noted, however, that Theorem 2 applies to all general distributions of reservation price.

## 4. Numerical explorations of SPP

We conducted several numerical experiments to gain further insight into the Service Provider Problem (SPP). We first examine the short-run SPP where the service provider’s capacity is fixed, then turn our attention to cases where the capacity is allowed to change. In both the short-run and long-run problems, we study the effect of number of subscribers on an application service provider’s $( \mathrm { A S P ^ { \circ } s } )$ profit, and the effect of market potential on an $\mathbf { A S P 7 } \mathbf { s }$ optimal profit and the optimal number of subscribers.

In these numerical experiments, we set the contract period T at 365 days (1 year). We arbitrarily picked a Fortune 1000 company with \$1.8 billion revenue with a 3.55% contribution margin due to information technology. This translates to a value of \$175,000 per day attributable to computing. Hence, we assume that the random variable R denoting the customer’s reservation price of computing has a uniform distribution over (\$150,000– \$200,000) per day where the mean is \$175,000/day. We use \$11,000 per day for the annualized software ownership cost, OC, based on typical trade press statistics of \$20 million to implement an ERP system over a 5-year period.

We use a linear function for the server cost, , where c is \$5000 per day to reflect the annual mainframe cost ranging from 1.25 to 3 million reported in Ref. [4]. The average inter-arrival time of individual customer’s requests for ASP services equals 2 h (k = 12/ day), while each request requires on average 0.5 h processing time $( \mu { = } 4 8 / \mathrm { d a y } )$ . The arrival rate k of each customer’s requests for services is subsequently increased sixteen-fold to explore the impact of heavy traffic. Figs. 2 –6 analyze various scenarios of the short-run problem where the number of servers is fixed at 10. The unit of profit in all figures is in \$1000 per contract period.

![](/api/attachments/JS7QBAFW/fulltext/images/aaba0f7a119d66783347c4b106ace54be1025b05e2fcafa415a26540da6d2422.jpg)  
Fig. 2. The effect of number of subscribers on ASP profit (short-run, $N { = } 5 0 0 )$

![](/api/attachments/JS7QBAFW/fulltext/images/0b2a84f8b16eadd3490634182bf0c79e19064d74bfde22bbbcd8c9a3e1a89748.jpg)  
Fig. 3. Optimal ASP profit as a function of market potential.

Fig. 2 shows the effect of number of subscribers on the ASP profit in the short-run where there are 500 potential customers. As predicted in Theorem 2, the ASP profit function is unimodal. The maximum profit is achieved when there are 47 subscribers, giving $M ^ { * } = 4 7$ in Eq. (9) of Section 3.1. This $M ^ { * }$ is in turn plugged into Eq. (11) to prescribe a family of optimal pricing policies. The ASP has a wide range of optimal pricing policies as long as $( F ^ { * } , p ^ { * } , y ^ { * } )$ satisfies the relationship described by Eq. (11).

For the same set of parameters, the effect of market potential on the short-run optimal profit is shown in Fig. 3. Fig. 4 plots the optimal number of subscribers as a function of market potential. Two observations from Figs. 3 and 4 are noteworthy.

![](/api/attachments/JS7QBAFW/fulltext/images/ac1fc726dbe6263762f17981f834e63189b2df795d49f61a4ef4ba9fadfb378f.jpg)  
Fig. 4. Optimal number of subscribers as a function of market potential.

![](/api/attachments/JS7QBAFW/fulltext/images/6307d2c5094cc5a25e9db5c09dec1e1371c6a55c720c2728b34ba7e67448572c.jpg)  
Fig. 5. Optimal ASP profit as a function of market potential (heavy traffic).

Firstly, Fig. 3 shows a ‘‘diminishing’’ increase of optimal ASP profit as the market potential increases. All things equal, this shows that bigger markets are better. However, the cost of growing market awareness, not considered in our model, suggests that when the server capacity is fixed, it might be better for $\mathbf { A S P } \mathbf { \bar { s } }$ to focus on a small set of potential customers with high valuation of its services than to cover the whole market. Secondly, Fig. 4 further suggests that the optimal number of subscribers remains the same when market potential exceeds 150. The optimal ASP profit, however, will be different for different market potentials although the optimal number of subscribers remains the same above 150. For the same number of service subscribers $M ,$ different profits will be realized for different market potentials, N. This becomes evident in Eq. (10) as the profit function V(M) will change with N through the $\mathbf { \hat { \mathfrak { R } } } ^ { - 1 } ( M / N )$ term.

![](/api/attachments/JS7QBAFW/fulltext/images/48c47b93377617dbd142728b51eb0552da7fe57153965585398ded3774268da0.jpg)  
Fig. 6. Optimal number of subscribers as a function of market potential (heavy traffic).

![](/api/attachments/JS7QBAFW/fulltext/images/327542bcf94932e27ec5397079c8d28107436bca3921f2c633550647505b7d3e.jpg)  
Fig. 7. Optimal ASP profit versus capacity (small market).

Figs. 5 and 6 plot the optimal short-run ASP profit and optimal number of subscribers as a function of the market potential, when the arrival rate of individual customer’s requests is increased sixteen-fold from 12/ day to 192/day. (The inter-arrival time is shortened from 2 h to 7.5 min). In the case of heavy arrival of customers’ requests, both the optimal short-run ASP profit and optimal number of subscribers are reduced significantly compared with the light-traffic case reported in Figs. 3 and 4. Facing increased requests arrivals, the ASP will be able to serve fewer customers in the short-run as its capacity is fixed.

The next set of numerical experiments examines the $\mathbf { A S P 7 } \mathbf { s }$ long-run problem where the service capacity has to be jointly determined with its pricing policy to maximize the profit. In Figs. 7 – 10, we plot the optimal ASP profit and optimal number of subscribers as a function of the ASP’s capacity. The same parameters used in Figs. 2 –4 are used in Figs. 7 –10, except by varying the ASP capacity and market potential. In Figs. 7 and 8, we look at results for a small market with 50 potential customers. Results for a large market with 500 potential customers follow in Figs. 9 and 10. Heavy traffic cases in the long-run problem are not reported as they exhibit similar patterns to those in the large-market case in Figs. 9 and 10.

![](/api/attachments/JS7QBAFW/fulltext/images/e60b5a7e6bbde0841edf60413119876cbbdcbef9f6cb0e4a79f681dcdec84c4d.jpg)  
Fig. 8. Optimal number of subscribers versus capacity (small market).

![](/api/attachments/JS7QBAFW/fulltext/images/c77a8740ff82b236389e31b35049e771ed58c49c060ffa0377ed2c1016d54982.jpg)  
Fig. 9. Optimal ASP profit versus capacity (large market).

Fig. 7 is derived by evaluating the optimal ASP profit for the varying capacities. From Fig. 7, the ASP realizes the optimal long-run profit when the number of servers equals 14. The optimal profit starts declining after the capacity exceeds 14, since the increase in revenues cannot compensate for the increase in capacity cost. This observation is corroborated by

![](/api/attachments/JS7QBAFW/fulltext/images/e54c6df7bce468b44aa673ce3a2b6ae402d8779f03e59be162a9e5621135f525.jpg)  
Fig. 10. Optimal number of subscribers versus capacity (large market).

Fig. 8, as the optimal number of subscribers remains the same after the capacity exceeds 11. For a large market with 500 potential customers, both the optimal ASP profit and optimal number of subscribers increase with the increasing capacity in a fashion similar to linear, as shown in Figs. 9 and 10.

## 5. Conclusions

In this paper, we modeled the economic dynamics between a monopolistic ASP and its potential customers. Under a realistic economies-of-scale assumption, we showed that there exists a unique rational expectation equilibrium. Optimal pricing policies for the ASP were derived and insights were garnered from numerical explorations.

In particular, we modeled the ASP’s service provider problem (SPP) and solved it by examining a sequence of progressively more complete problems starting with the short-run SPP problem where service capacity and guaranteed minimal performance is unchangeable and ignored.

From this, we determine a family of optimal policies, the form of which depends on the type of charging structure the ASP chooses. These range from pure policies incorporating only a fixed or variable cost component to policies employing fixed, variable and reimbursement price components. Table 2 summarizes these policies.

We conducted a number of numerical studies to gain insights into properties of optimal SPP solutions. If these generalize, we have the following properties. It appears that with a linear cost function and uniform reservation price distribution, the optimal ASP profit is increasing at a diminishing rate. The optimal number of subscribers reaches a limit as market potential increases, probably due to the performance guarantee. As expected, as the frequency of usage increases, the number of customers that can be handled decreases and, thus, the ASP profit.

Studies performed on the full ASP problem suggests there is an optimal server capacity where profits start to decline as the increased revenues fail to cover increased server costs. The optimal number of subscribers reaches a peak (before the optimal capacity). ASP profit and optimal subscriber level increase as the market potential increases.

Future research could proceed in a number of directions. One could try to generalize the empirical properties observed in Section 4. Special conditions on the pdf of customers’ valuation of using the ASP service f(r) or the cost function of ASP’s servers c(s) may be required to achieve these goals. Another avenue of research might make the market potential, N, a function of advertising and include customers waiting time for service in their valuation of computing. Finally, it is of interest extending this paper’s setting to study the price and capacity competition between multiple ASPs.

## Acknowledgements

The authors gratefully acknowledge comments and suggestions of Professor Ira Horowitz, seminar participants of the1999 Indiana University/University of Florida Joint Workshop on e-Business, the 1999 Workshop on Information Systems and Economics (WISE), The Institute of Economics of Academia Sinica (Taiwan), National Sun Yat-sen University (Taiwan), University of South Florida, and IBM’s T.J. Watson Research Center.

## Appendix A

Proof of Lemma 1:

Eq. (2) implies that

$$
\begin{array}{l} M \leq N \cdot \operatorname{Prob} \left(\frac {T}{\lambda^ {- 1} + W} \left(\frac {R - p}{\mu} + y W _ {q}\right) - F \right. \\ \left. \geq \frac {T}{\left(\lambda^ {- 1} + \mu^ {- 1}\right)} \frac {R}{\mu} - \mathrm{OC}\right). \end{array}
$$

Let M be given by an optimal solution to Eq. (1). Suppose that at an optimal solution has

$$
\begin{array}{l} M <   N \cdot \operatorname{Prob} \biggl (\frac {T}{\lambda^ {- 1} + W} \left(\frac {R - p}{\mu} + y W _ {q}\right) - F \\ \qquad \geq \frac {T}{(\lambda^ {- 1} + \mu^ {- 1})} \frac {R}{\mu} - \mathrm{OC} \biggr). \end{array}
$$

Notice that is Prob() is decreasing in increasing F. Consider increasing F so that the above is an equality.

No other constraint is adversely affected, although the objective function strictly increases. This contradicts starting with an optimal solution. Hence, the equality sign in Eq. (2) holds.

## Appendix B

Once again, we prove this lemma by contradiction. Suppose an optimal solution has $M < s$ . Then $W _ { q } = 0$ and $\mathrm { W } = \mu ^ { - 1 }$ . But then Lemma 1 shows that $M = N .$

## Appendix C

Proof of Theorem 1:

After further algebraic manipulation, Eq. (8) can be re-arranged to

$$
\begin{array}{l} M = N \cdot \operatorname{Prob} \bigg (R \leq \frac {\mu (\lambda^ {- 1} + \mu^ {- 1}) ((\mathrm{OC} - F) + T y)}{T} \\ \quad + \frac {(\lambda^ {- 1} + \mu^ {- 1}) ((\mathrm{OC} - F) (\lambda^ {- 1} \mu + 1) - T p)}{T W _ {q}} \bigg). \end{array}
$$

If $( \mathrm { O C } - F ) ( \lambda ^ { - 1 } ~ \mu + 1 ) - T p { > } 0 $ , then the right-hand side of the above equation is a decreasing function of M since $W _ { q }$ is an increasing function of M and the remaining multipliers are all positive. $( O C - F ) ( \lambda ^ { - }$ 1 $\mu + 1 ) - T p { > } 0$ is always satisfied by our assumption that economies-of-scale make the nominal cost of using the ASP service lower than the cost facing an individual customer.

## Appendix D

Proof of Theorem 2:

Now, $f ( r ) { > } 0$ over its domain assures us that

$$
\Re^ {- 1} \left(\frac {M + 1}{N}\right) = \Re^ {- 1} \left(\frac {M}{N}\right) + \alpha \quad \alpha > 0.
$$

Also, since b(M) is increasing in M, we have

$$
b (M) = \beta b (M + 1) \quad \beta <   1.
$$

Define the difference function $\Delta V = V ( M + 1 ) -$ $V ( M )$ , where $V ( M )$ is given in Eq. (10). After some algebraic manipulation one gets

$$
\begin{array}{l} \Delta V = \mathrm{OC} - b (M + 1) \bigg ((M + 1) \bigg (\Re^ {- 1} \bigg (\frac {M}{N} \bigg) + \alpha \bigg) \\ \qquad - M \beta \Re^ {- 1} \bigg (\frac {M}{N} \bigg) \bigg). \end{array}
$$

Since $( M + 1 ) \ ( \Re ^ { - 1 } ( M / N ) + \alpha ) { > } M \beta \Re ^ { - 1 } ( M / N ) , \Delta V$ is strictly decreasing in M and $\Delta ^ { 2 } V$ is negative. Hence, $V ( M )$ is unimodal.

## References

[1] R.J. Dolan, Incentive mechanisms for priority queueing problems, Bell Journal of Economics 9 (2) (1978) 421 – 436.

[2] M.F. Eastley, Ground rules for selecting an application service provider, CMPnet (March 24, 1999).

[3] N.M. Edelson, D.K. Hildebrand, Congestion tolls for Poisson queuing processes, Econometrica 43 (1) (1975), 81 – 92.

[4] E. Freeman, Mainframes in the 21st century, Datamation (Jan. 1999).

[5] J. Gantz, A brand new practice called. . . time-sharing? Computerworld (July 20, 1998) 27.

[6] D. Gross, C.M. Harris, Queueing Theory, Wiley, New York, 1998.

[7] A. Gupta, D.O. Stahl, A.B. Whinston, An economic approach to network computing with priority classes, Journal of Organizational Computing and Electronic Commerce 6 (1) (1996) 71– 95.

[8] A. Gupta, D.O. Stahl, A.B. Whinston, The economics of network management, Communications of the ACM 42 (9) (1999) 57– 63.

[9] M.L. Katz, C. Shapiro, Technology adoption in the presence of network externalities, Journal of Political Economy 94 (4) (1986) 822 – 841.

[10] J. King, Pay-as-you-go apps on tap, Computerworld 30 (31) (July 29, 1996).

[11] S. Leibs, Software for rent—Internet providers hope renting apps will bring them closer customers, CMPnet (May 25, 1998).

[12] J.D.C. Little, A proof for the queueing formula L = E W, Operations Research 9 (1961) 383 – 387.

[13] J.K. MacKie-Mason, H.R. Varian, Pricing congestible resources, IEEE Journal of Selected Areas in Communications 13 (7) (1995) 1141–1149.

[14] M. Maclachian, Interliant offers web-based app rentals, CMPnet (September 21, 1998).

[15] H. Mendelson, Pricing computer services: queueing effects, Communications of the ACM 28 (3) (1985) 312– 321.

[16] H. Mendelson, S. Whang, Optimal incentive-compatible priority pricing for the M/M/1 queue, Operations Research 38 (5) (1990) 870– 883.

[17] P. Naor, The regulation of queue sizes by levying tolls, Econometrica 37 (1969) 15– 24.

[18] W.Y. Oi, A Disneyland dilemma: two-part tariffs for a Mickey Mouse monopoly, Quarterly Journal of Economics 85 (1) (1971) 77– 96.

[19] A. Silberschatz, J.L. Peterson, P.B. Galvin, Operating System Concepts, 3rd edn. (Addison-Wesley Publishing, Reading, Massachusetts, USA, 1991).

[20] S. Wermer, IDC: Spending in High-end Application Service Provider Market will be Euro 1.8 Billion by 2003, Primeur Weekly (May 24, 1999) http://www.hoise.com/primeur/99 articles/monthly/SW-PR-05-99-24.html.

![](/api/attachments/JS7QBAFW/fulltext/images/4ec36f0ff35bebc182a1d40b82cc476853c1bb7c249531ccdd0c245fbc896ef6.jpg)

Dr. Hsing Kenneth Cheng is the American Economic Institutions Associate Professor at the Department of Decision and Information Sciences of the University of Florida. Prior to joining UF, he served on the faculty at The College of William and Mary from 1992 to 1998. He received his PhD from William E. Simon Graduate School of Business Administration, University of Rochester in 1992. Professor Cheng teaches information technology

strategy, electronic commerce, and supply chain management. His research interests involve electronic commerce, economics of information systems, and supply chain management. His work has appeared in Computers and Operations Research, Decision Support Systems, European Journal of Operational Research, IEICE Transactions, Journal of Business Ethics, Journal of Management Information Systems, and Socio-Economic Planning Sciences. He also contributed book chapters on ‘‘Hacking, Computer Viruses, and Software Piracy: The Implications of Modern Computer Fraud for Corporations’’ and ‘‘The Critical Role of Information Technology for Employee Success in the Coming Decade.’’

![](/api/attachments/JS7QBAFW/fulltext/images/53d79e22007a9d283208979432e4f0fe2a3c757cad3ebc58256e0d266b593f1f.jpg)

Professor Koehler is the John B. Higdon Eminent Scholar of Decision and Information Sciences at the Department of Decision and Information Sciences of the University of Florida. He has been at the university for several years and served as Chair of the department for the period 1990 – 1994. His recent teaching has been in business objects and e-commerce for the graduate programs. Professor Koehler was a faculty member at Purdue University, has

worked as a consultant for a number of firms, and was the cofounder of Micro Data Base Systems, a firm in which he served as CEO for the period 1981 – 1987. He has more than 50 papers published in leading academic journals and he currently serves on the editorial boards of Decision Support Systems; Decision Sciences; International Journal of Business; Journal of Information Technology and Management, INFORMs On-line, and others.
