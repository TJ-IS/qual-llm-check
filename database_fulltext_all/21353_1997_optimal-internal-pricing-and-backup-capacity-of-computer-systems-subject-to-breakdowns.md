---
otero_id: 21353
otero_key: "4HE6JCPQ"
title: "Optimal internal pricing and backup capacity of computer systems subject to breakdowns"
authors: "Hsing K. Cheng"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00043-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal internal pricing and backup capacity of computer systems subject to breakdowns

Hsing K. Cheng \*

Graduate School of Business Administration, The College of William and Mary, Williamsburg, VA 23187-8795, USA

Received 6 May 1993; revised 9 December 1993; accepted 21 April 1994

## Abstract

In a recent survey computers were found to break down nine times per year in the average company and computer downtime cost U.S. business \$4 billion in 1991. The existing literature that combines pricing and queuing analysis of a shared service facility does not explicitly consider the failures of computer systems. The objective of this paper is to examine the impact of computer breakdowns on various aspects of the pricing and capacity decisions. It also examines the issue whether to acquire backup capacity when the computer system is in repair. The results of this paper show that computer breakdowns have significant impact on various aspects of concern. In general, computer breakdowns increase the expected time of jobs in the system, thus discouraging the submission of low-value jobs. Less computer capacity is needed to service the jobs with higher values compared to the case where a computer works all the time. The utilization ratio is lower in view of computer breakdowns. The firm, faced with computer breakdowns, has to increase the price of computer service and the increase in price is significant. Secondly, the findings suggest that it is imperative to acquire backup capacity when computing is critical to the firm in terms of high delay cost of jobs. The research results support the “hot backup” strategy, a common industry practice to operate in parallel two computers with the same capacity. Finally, the firm should charge users the total marginal capacity costs of the firm’s computer as well as the backup.

Keywords: Pricing and capacity decisions; Economics of information systems; Computer breakdowns; Computer backup; Reliability

## 1. Introduction

Today's business environment is characterized by a heavy use of computing to promote the survival and prosperity of the organization. Computing is employed to implement the notion of gaining some competitive edge such as to cut down the time to market products and services. Timeliness of computing service implies reduction of user's time cost of waiting for the completion of jobs submitted to the computer. The time of jobs spent in the computer system also translates to possible loss of revenues and business opportunities, a cost normally termed “delay cost”. There are many environments where timeliness of computing service is critical such as security trading systems, airline reservation systems, customer service systems of banks, and orders processing systems at customer service centers.

There are research results available for business managers in managing the congestion-prone computing facility. For example, Mendelson [6] embedded a microeconomic framework in the queuing model for analyzing the effects of delay cost on the management of computing resources. The model is extended by Mendelson and Whang [8] to incorporate the pricing of priorities. Dewan and Mendelson [2] showed that the optimal transfer price is equal to the (constant) marginal capacity cost for the case of a linear capacity cost function and exponentially distributed service requirements.

The existing literature does not explicitly consider the failures of the service facility (the computer). In reality, however, computers do break down. A recent report shows that computer downtime cost U.S. business \$4 billion in 1991, primarily through lost productivity and lost revenues [1]. In the same report, computers are found to break down nine times per year in the average company. Computer downtime becomes more of an issue for companies that depend heavily on computers. As the VP of an investment firm explained [1], “Downtime is one of those things in the financial industry that just cannot be tolerated.”

The objective of this paper is to study the impact of downtime on the internal pricing and capacity decisions of computing resources. This paper also analyzes various important decision problems related to computer downtime. Since many firms rely on a continuous provision of computing service, it is essential for them to acquire some backup capacity when their computers break down. Business managers must address the following questions. When is the firm better off to obtain computer backup capacity? If it is cost effective to have some backup capacity, what is the optimal backup capacity? The decision becomes far more complicated when it has to be jointly decided with the pricing and capacity of the firm's computer. This paper provides useful guidelines for these important issues.

## 2. The model

In this section, a queuing model is embedded in a microeconomic framework for further analysis. Following the notation used in Mendelson [6] and Dewan and Mendelson [2], jobs requiring computer processing time have a Poisson arrival rate $\lambda$ . The expected (gross) value per unit of time of the computing service to the organization corresponding to the arrival rate $\lambda$ is specified by a value function $V(\lambda)$ . Hence, $V'(\lambda)$ can be interpreted as the marginal value function and the demand function for computing service as well. $V(\lambda)$ is usually assumed to be increasing, bounded from above, twice continuously differentiable and strictly concave so that $V'(\lambda)$ is downward-sloping. By contrast, Stidham [10] placed a finite upper bound $\Lambda$ on the arrival rate $\lambda$ and specified a distribution function $F(x)$ on an interval to describe the value of service to a job, where $F(x)$ is assumed to be strictly increasing and continuous. The correspondence $V'(\lambda) = \overline{F}^{-1}(\lambda/\Lambda)$ is used by Stidham [10] to derive the properties of $V(\lambda)$ aforementioned.

In this research, it is assumed that jobs submitted by users have homogeneous service requirements and delay costs. Service times of arriving jobs are assumed to be independently and identically drawn from an exponential distribution with mean $1/\mu$ according to the First Come First Serve (FCFS) service discipline. In other words, the computer service system is formulated as an M/M/1 queue with arrival rate $\lambda$ and processing rate $\mu$ in jobs per unit of time.

A job-by-job transfer pricing scheme is considered where each job is charged a fixed fee p for computer processing. $^{1}$ In the absence of delay cost, the cost for submitting a job involves only the service charge, p. Users will submit jobs for processing as long as the marginal value of doing so is not less than the cost, i.e.,

$$
V ^ {\prime} (\lambda) \geq p.\tag{2.1}
$$

However, there is a high opportunity cost from submitting, waiting, to getting jobs done in today's fast-paced society. Assume that the delay cost per job is a constant v per unit of time. This implies that to shorten the turnaround time of each job by one time unit amounts to v monetary units gain to the organization. Let T be the expected time each job spends in the system, including the actual processing time of each job and the time spent waiting in the queue. Then, the expected delay cost per job equals $v \cdot T$ and the total expected cost per job is the sum of the service charge p and the expected delay cost $v \cdot T$ . Taking the delay cost into account, the equilibrium is achieved when the following relationship is satisfied

$$
V ^ {\prime} (\lambda) = p + v \cdot T.\tag{2.2}
$$

Eq. (2.2) follows the principle of equating the marginal cost of computing service with its marginal value at the equilibrium.

Let D be the expected overall (aggregate) delay cost per unit of time incurred by the service system as a whole. Then one has

$$
D = \lambda \cdot v \cdot T.\tag{2.3}
$$

The marginal aggregate delay cost is thus derived by differentiating D with respect to $\lambda$ .

$$
\frac {\partial D}{\partial \lambda} = v T + v \lambda \frac {\partial T}{\partial \lambda}.\tag{2.4}
$$

Eq. (2.4) shows the decomposition of the marginal aggregate delay cost into two terms. The first term of the right-hand side is interpreted as the “self-regulating” term and the second term as the “externality term” by Mendelson [6] and Dewan and Mendelson [2], since the first term represents a cost by generating the added work load, while the second term is inflicted on other jobs and cannot be perceived by the generating job.

The existing literature that combines pricing and queuing analysis of a shared service facility does not explicitly consider the failures of computer systems. As organizations become more and more dependent on the continuous functioning of computers, the impact of computer systems' failures cannot be ignored. This issue is taken into account by letting the computer system have two states, up (operational) and down (breakdown). The breakdown behavior of computer system is modeled as a two-state Markov chain where the up and down states are exponentially distributed with parameters $\eta$ and $\gamma$ respectively. That is, $\gamma$ is the repair rate and $\eta$ is the failure rate of the computer system under consideration. With this set up, $1/\gamma$ has the interpretation of mean time to repair (MTTR) and $1/\eta$ can be interpreted as the mean time between failures (MTBF). Mendelson [6] and Dewan and Mendelson [2] treat the service facility as a “black box” characterized by a general service time distribution, while this paper derives a specific service time distribution, based on a richer description of the queuing behavior inside the black box. The expected time each job spends in such computer system subject to breakdowns, $T(\lambda,\mu)$ , is given by the following theorem.

## Theorem 2.1.

$$
T (\lambda , \mu) = \frac {1 + ((\eta \mu) / (\gamma + \eta) ^ {2})}{(\mu (\gamma / (\gamma + \eta))) - \lambda}.\tag{2.5}
$$

Proof. Please see Appendix A.

The expected time spent in the system in Theorem 2.1 differs from that of an ordinary M/M/1 queue without breakdowns by replacing $\mu$ with the effective capacity $\mu(\gamma/(\gamma+\eta))$ and adding a correction term $(\eta\mu)/(\gamma+\eta)^{2}$ in the numerator. This correction term can be interpreted as the additional time spent in the system caused by the “disruption of service”. We are now in a position to discuss the optimal internal pricing of computer systems subject to breakdowns without backup capacity.

## 3. Internal pricing of computer systems subject to breakdowns and no backup

The objective of the organization is to maximize the expected net value of the computing service. The management is faced with two decision problems, a short-run problem and a long-run problem. The computing capacity $\mu$ is fixed in the short-run problem, while $\mu$ is allowed to change in the long-run problem. The major concern of the short-run problem is to set an optimal internal price of the computing service. The price and the capacity, however, have to be jointly determined in the long-run problem. After the formulation of the short-run and long-run problems for computer systems subject to failures, the results will be compared with previous findings where computer systems are assumed to work all the time. Backup capacity is not considered at this point when the computer system is in repair. The problem of determining optimal backup capacity will be analyzed in the next section.

## 3.1. Short-run problem ( $\mu$ is fixed)

The short-run problem is formulated as

$$
\max _ {\lambda} \left\{V (\lambda) - D \right\},\tag{3.1}
$$

where recall that D, defined in Eq. (2.3), is the expected overall delay cost per unit of time incurred by the whole service system. The first order condition leads to

$$
V ^ {\prime} (\lambda) = \frac {\partial D}{\partial \lambda}.\tag{3.2}
$$

When there is a upper bound $\Lambda$ on the arrival rate $\lambda$ , Stidham [10] showed that an optimal solution may not lie in the interior of the feasible region and that there may be multiple solutions characterized by the first order condition. In order to derive qualitative properties of the underlying problem, it is assumed for the simplicity of analysis that there exists a single interior solution so that it suffices to focus on first order condition.

Eq. (3.2) determines the optimal arrival rate $\lambda^{*}$ that maximizes the expected net value. The optimal price $p^{*}$ that induces this arrival rate is derived by substituting Eq. (2.2) and Eq. (2.4) into Eq. (3.2). It then follows that

$$
p ^ {*} = v \lambda^ {*} \frac {\partial T (\lambda^ {*} , \mu)}{\partial \lambda}.\tag{3.3}
$$

Eq. (3.3) shows that the optimal internal price charged to users equals the externality part of the marginal aggregate delay cost specified in Eq. (2.4).

Theorem 3.1. (Optimal price of the short-run problem.) The optimal internal price, $p^{*}$ , of computing service for the short-run problem is

$$
p ^ {*} = \lambda^ {*} \cdot \frac {v}{\left(\mu - \lambda^ {*}\right) ^ {2}},\tag{3.4}
$$

if computer systems never fail; and

$$
p ^ {*} = \lambda^ {*} \cdot \frac {v \cdot \left[ 1 + \left((\eta \mu) / (\gamma + \eta) ^ {2}\right) \right]}{\left[ \mu \cdot (\gamma / (\gamma + \eta)) - \lambda^ {*} \right] ^ {2}},\tag{3.5}
$$

when computers do break down.

Proof. The theorem follows from Eq. (3.3) and Theorem 2.1.

## 3.2. Long-run problem ( $\mu$ is allowed to change)

The internal price of computing service and the computer capacity are to be jointly determined in the long-run problem. Thus, the capacity cost of the computer system becomes part of the decision problem in maximizing the expected net value. Let the cost rate of the computer system associated with the processing capacity $\mu$ be specified by the function $C(\mu)$ . Mendelson [7] demonstrates that the average cost per unit of computing capacity is constant, suggesting that the use of a linear cost function for computer systems is appropriate. We assume that the capacity cost function has the form

$$
C (\mu) = B + b _ {1} \cdot \mu ,\tag{3.6}
$$

where B represents the fixed overhead and $b_{1}$ is the marginal capacity cost. The marginal capacity cost $b_{1}$ amounts to the cost to expand the computer processing capacity for accommodating one more job per unit of time.

The long-run problem is formulated as

$$
\max _ {\lambda , \mu} \left\{V (\lambda) - D (\lambda , \mu) - C (\mu) \right\}.\tag{3.7}
$$

First order conditions require that

$$
V ^ {\prime} (\lambda) = \frac {\partial D}{\partial \lambda},\tag{3.8}
$$

and

$$
C ^ {\prime} (\mu) = - \frac {\partial D}{\partial \mu}.\tag{3.9}
$$

Theorem 3.2. (Optimal price of the long-run problem.) The optimal internal price, $p^*$ , for the long-run problem is

$$
p ^ {*} = b _ {1},\tag{3.10}
$$

if computers never fail [2]; and

$$
p ^ {*} = \frac {\gamma + \eta}{\gamma} b _ {1} + \frac {v \cdot ((\eta \lambda^ {*}) / (\gamma (\gamma + \eta)))}{(\mu^ {*} (\gamma / (\gamma + \eta)) - \lambda^ {*}},\tag{3.11}
$$

when computers do break down.

Proof. Refer to Dewan and Mendelson [2] for the proof of Eq. (3.10). For the case where computer systems are subject to breakdowns, the proof is derived in a similar procedure by replacing the standard M/M/1 queue result with $T(\lambda,\mu)$ in Theorem 2.1. □

The pricing rule of the long-run problem is simple and intuitive for the case where computer systems never fail: simply charge users the computer's long-run marginal capacity cost regardless of utilization. Dewan and Mendelson [2] interpret it as “allocated fixed cost”, a result consistent with Miller and Buckman [9] where the allocated fixed cost is a good approximation for the optimal transfer price.

However, the optimal price no longer has a simple form when computer systems do break down. Notice that the prices must be scaled up both for the short-run and long-run problems to compensate the lost processing capacity of computers due to breakdowns. Ignoring the fact that computers will fail leads to suboptimal internal pricing, as shown in the following numerical examples.

For comparison purpose, let the demand function belong to the class of isoelastic demand functions used in Dewan and Mendelson [2] and have the form $V'(\lambda) = A/\lambda^{\alpha}$ , where $0 < \alpha \leq 1$ . The corresponding expected gross value function has the form $V(\lambda) = A\lambda^{1-\alpha}/(1-\alpha)$ . The expected gross value function is $V(\lambda) = A \ln \lambda$ for the case of unit elasticity ( $\alpha = 1$ ). In the following numerical examples, A equals 100. To see the effect of computer breakdowns, consider a computer system characterized by the following parameters. The mean time between failures, $1/\eta$ , equals 259200 minutes (about six months).

![](/api/attachments/4HE6JCPQ/fulltext/images/0f5f82131e5275c6ce1af5c34bf2321ba9de65a0042e99405540e6ab406ea598.jpg)  
Fig. 1. Optimal arrival rates versus delay cost, $\alpha = 0.5$ .

and the mean time to repair, $1/\gamma$ , varies from 60, 120, 180, to 240 minutes. According to the empirical data in Ballou [1], these configurations represent a realistic profile of business computer systems.

The marginal capacity cost $(b_{1})$ equals 1. The fixed overhead, B, in Eq. (3.6) is set to zero since it will not affect the maximization problem. The long-run problem described in Eq. (3.7) is solved for both cases where the computer does not fail and where the computer breaks down according to the physical parameters $\gamma$ and $\eta$ aforementioned. Both the arrival rate and service capacity are in number of jobs per unit of time.

The optimal arrival rates are plotted against the delay cost, v, for $\alpha = 0.5$ and $\alpha = 1.0$ in Fig. 1 and Fig. 2 respectively. One sees that the optimal arrival rates decline as v increases whether computer systems break down or not. However, Fig. 1 and Fig. 2 clearly show that the optimal arrival rates to the computer systems subject to breakdowns are significantly less than their respective rates of computers that do not fail. Breakdowns will increase the expected time each job spends in the system. According to Eq. (2.2), users will only submit the jobs with higher value at the equilibrium, thus decreasing the optimal arrival rates. Furthermore, arrival rates are smaller for computer systems with longer mean time to repair (MTTR), since the longer the MTTR is, the longer the expected time each jobs spends in the system.

![](/api/attachments/4HE6JCPQ/fulltext/images/9f99b00ca118af63f2b8cd93768db4f6acdc9da2d4ddd46dbe1b65540520db5b.jpg)  
Fig. 2. Optimal arrival rates versus delay cost, $\alpha = 1.0$ .

Since a lower arrival rate induces smaller required computer capacity, the same pattern is observed for optimal capacities as a function of delay cost graphed in Fig. 3 and Fig. 4 for $\alpha = 0.5$ and $\alpha = 1.0$ respectively. When a computer does not fail, Fig. 4 shows that optimal capacity is fixed and independent of delay cost for the unit elasticity case.

![](/api/attachments/4HE6JCPQ/fulltext/images/9107bfc9a333f184e80b2b3e7bedb1b1800a917e2b8cf9ef07dc7b21509b7cbf.jpg)  
Fig. 3. Optimal capacities versus delay cost, $\alpha = 0.5$ .

![](/api/attachments/4HE6JCPQ/fulltext/images/b366d739ec80e6870c78245df72fd2fbcc6e801b874181351de6dcca6dc53c95.jpg)  
Fig. 4. Optimal capacities versus delay cost, $\alpha = 1.0$ .

Fig. 5 and Fig. 6 show the optimal prices plotted against the delay cost for $\alpha=0.5$ and $\alpha=1.0$ . According to Theorem 3.2, the optimal internal price of computing must be scaled up in view of computer breakdowns. From Fig. 5 and Fig. 6, one sees that the optimal price increases when it takes more time to repair the system and it also increases as delay cost increases. Fig. 5 and Fig. 6 clearly show that there is a significant impact of computer breakdowns on the internal price of computing. Ignoring the fact that a computer system will fail can lead to an error of as much as 300%. In summary, computer breakdowns are shown to have significant impact on each aspect of pricing and capacity decisions.

![](/api/attachments/4HE6JCPQ/fulltext/images/81b710e572f17f2f8c3db0daeec726dab3c3cf148db5fb59e4bb36a0ecf35d1a.jpg)  
Fig. 5. Optimal prices versus delay cost, $\alpha = 0.5$ .

![](/api/attachments/4HE6JCPQ/fulltext/images/0a372a556cabe046b8435d551becaaac54bd4d62cacf9bca689a05e294f653f3.jpg)  
Fig. 6. Optimal prices versus delay cost, $\alpha = 1.0$ .

## 4. Optimal internal pricing and backup capacity decisions

Many industries rely on the continuous operation of computer systems to such a great extent that they cannot afford the loss caused by computer breakdowns. For example, banks would have to close after two days without computers, distribution companies in four days, and factories would be shut down in a week $[5]$ . Thus, it is essential for those firms that cannot tolerate the breakdowns of their computer systems to acquire some computer backup capacity. When backup capacity is available, many important decision problems must be addressed by business managers. The bottomline question is whether or not the firm is better off with backup capacity when acquiring backup capacity involves high costs? If it is cost effective to have some backup capacity, what is the optimal backup capacity? The decision problem gets more complicated when the backup capacity has to be jointly determined with the pricing and original computer capacity of the firm. This section is devoted to examining these important decision problems.

Following the notation used in previous sections, let $V(\lambda)$ be the expected aggregate value of the computing service to the organization per unit of time corresponding to arrival rate $\lambda$ . The usual assumption that $V(\lambda)$ is increasing, twice continuously differentiable, and strictly concave still applies. Each job submitted for computer processing is charged a fixed fee p. The firm's computer has a capacity for processing $\mu$ jobs per unit of time, where the cost of computing is specified by Eq. (3.6). The firm can purchase a backup capacity $\mu_{B}$ from outside sources when its own computer breaks down. The backup capacity is assumed to be readily available upon request. $^{2}$ The cost of acquiring $\mu_{B}$ backup capacity is specified by the function $C_{B}(\mu_{B})$ .

$$
C _ {B} \left(\mu_ {B}\right) = F + b _ {2} \cdot \mu_ {B},\tag{4.1}
$$

where F represents a fixed fee for using the backup capacity. The cost of backup capacity, $b_{2}$ , can be a function of the physical parameters $\gamma$ and $\eta$ of the firm's original computer. In the extreme case, $b_{2}$ equals zero when the firm's computer never fails, i.e., $\gamma \to \infty$ or $\eta \to 0$ . Moreover, $b_{2}$ is presumably greater than the marginal capacity cost of the firm's own computer, $b_{1}$ . If there is $\mu_{B}$ backup capacity available when the computer system is down, then the expected time each job spends in the system, T, is a function of the arrival rate $\lambda$ , the original capacity $\mu$ , and the backup capacity $\mu_{B}$ and is given by the following theorem.

Theorem 4.1. (Expected time in the system with backup capacity $\mu_B$ .)

$$
\begin{array}{r l} T (\lambda , \mu , \mu_ {B}) & = \left[ 1 + \left(\left((\mu - \mu_ {B}) [ \eta (\lambda - \mu_ {B}) + \mu_ {B} p _ {0, d} (\gamma + \eta) ]\right) / (\lambda (\gamma + \eta) ^ {2})\right) \right] \\ & \times \left[ \left((\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta)\right) - \lambda \right] ^ {- 1}, \end{array} \tag {4.2}
$$

where $p_{0,d}$ is the probability that the computer system is down and there are no jobs in the system.

Proof. Please see Appendix B.

The expression for the expected time in the system, $T(\lambda,\mu,\mu_{B})$ , in Theorem 4.1 has a unknown term $p_{0,d}$ . After some analysis (please see Appendix C), one finds that

$$
p _ {0, d} = \frac {\eta \bar {z} \left[ \left(\left(\gamma \mu + \eta \mu_ {B}\right) / (\gamma + \eta)\right) - \lambda \right]}{\mu_ {B} (1 - \bar {z}) (\mu - \lambda \bar {z})},\tag{4.3}
$$

where $\bar{z}$ is the zero of the polynomial

$$
\begin{array}{r l} G (z) & = \lambda^ {2} z ^ {3} - \lambda (\lambda + \gamma + \eta + \mu + \mu_ {B}) z ^ {2} \\ & \quad + [ \mu (\lambda + \gamma + \mu_ {B}) + \mu_ {B} (\lambda + \eta) ] z - \mu \mu_ {B}. \end{array}\tag{4.4}
$$

Although the unknown $p_{0,d}$ is expressed in terms of another unknown $\bar{z}$ , $\bar{z}$ is readily available from many numerical routines that find the roots of a polynomial. In the setting of computing, job arrival and processing time is measured in seconds. However, the mean time between failures (1/ $\eta$ ) is measured in months and the mean time to repair (1/ $\gamma$ ) is in the order of hours or days. This means that the inverse of the mean time between failures, $\eta$ , and the inverse of the mean time to repair, $\gamma$ , are numerically negligible compared with $\lambda$ , $\mu$ , and $\mu_{B}$ . Taking advantage of this special property, $T(\lambda,\mu,\mu_{B})$ in Theorem 4.1 can be very accurately approximated by (please see Appendix D)

$$
T (\lambda , \mu , \mu_ {B}) \cong \frac {1}{\left((\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta)\right) - \lambda}.\tag{4.5}
$$

Eq. (4.5) is equivalent to the expected time spent in a regular M/M/1 queue by replacing the service rate with the effective capacity $(\gamma\mu + \eta\mu_{B})/(\gamma + \eta)$ when backup capacity $\mu_{B}$ is available. Unlike the case of no backup, the correction term in Theorem 4.1 disappears since there is no service disruption when backup capacity is available.

If the firm can acquire some computer backup capacity $\mu_{B}$ at a cost specified by Eq. (4.1), the long-run problem becomes

$$
\max _ {\lambda , \mu , \mu_ {B}} \left\{V (\lambda) - D (\lambda , \mu , \mu_ {B}) - C (\mu) - C _ {B} (\mu_ {B}) \right\},\tag{4.6}
$$

where $D(\lambda,\mu,\mu_{B})$ , the aggregate expected delay cost, equals $v\cdot\lambda\cdot T(\lambda,\mu,\mu_{B})$ , and $T(\lambda,\mu,\mu_{B})$ is specified by Eq. (4.5). The capacity cost function $C(\mu)$ is the same as in Eq. (3.6) before. First order conditions require that

$$
V ^ {\prime} (\lambda) = \frac {\partial D}{\partial \lambda},\tag{4.7}
$$

$$
C ^ {\prime} (\mu) = b _ {1} = \frac {v \cdot \lambda \cdot (\gamma / (\gamma + \eta))}{\left[ \left((\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta)\right) - \lambda \right] ^ {2}},\tag{4.8}
$$

and

$$
C _ {B} ^ {\prime} (\mu_ {B}) = b _ {2} = \frac {v \cdot \lambda \cdot (\eta / (\gamma + \eta))}{\left[ ((\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta)) - \lambda \right] ^ {2}}.\tag{4.9}
$$

Theorem 4.2. (Optimal internal pricing of computer with backup capacity $\mu_B$ .) If the firm's computer capacity is $\mu$ and has the backup capacity $\mu_B$ when the computer breaks down, then the optimal internal price, $p^*$ , for such computer service system is given by

$$
p ^ {*} = b _ {1} + b _ {2}.\tag{4.10}
$$

Proof. Combining Eq. (2.2), Eq. (2.4), and Eq. (4.7), the optimal price equals the externality part of the marginal aggregate delay cost in the long-run problem, i.e.,

$$
p ^ {*} = \frac {v \lambda^ {*}}{\left[ \left(\left(\gamma \mu^ {*} + \eta \mu_ {B} ^ {*}\right) / (\gamma + \eta)\right) - \lambda^ {*} \right] ^ {2}}.\tag{4.11}
$$

The right-hand side of Eq. (4.11) equals $b_{1} + b_{2}$ , the sum of Eq. (4.8) and Eq. (4.9). ☐

The pricing rule becomes simple and intuitively appealing again for the computer service system with backup. The firm should charge users the total marginal costs of all available computing capacities, including the backup. The following theorem specifies the relationship between optimal arrival rate $\lambda^{*}$ and optimal capacities $\mu^{*}$ and $\mu_{B}^{*}$ so that the net value to the firm is maximized.

Theorem 4.3. The optimal arrival rate $\lambda^{*}$ and optimal capacities $\mu^{*}$ and $\mu_{B}^{*}$ that maximize the firm's net value must satisfy the following relationship:

$$
\mu^ {*} = \mu_ {B} ^ {*} = \frac {V ^ {\prime} (\lambda^ {*}) \lambda^ {*}}{b _ {1} + b _ {2}}.\tag{4.12}
$$

Proof. The first order condition (Eq. (4.7)) leads to

$$
V _ {1} ^ {\prime} (\lambda) \lambda = \frac {v \lambda [ (\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta) ]}{[ ((\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta)) - \gamma ] ^ {2}}.\tag{4.13}
$$

By combining Eq. (4.8), Eq. (4.9), and Eq. (4.13), it follows that

$$
b _ {1} \mu + b _ {2} \mu_ {B} = V ^ {\prime} (\lambda) \lambda .\tag{4.14}
$$

From observing the fact that

$$
\frac {v \cdot \lambda}{\left[ \left(\left(\gamma \mu + \eta \mu_ {B}\right) / (\gamma + \eta)\right) - \lambda \right] ^ {2}} = b _ {1} + b _ {2},\tag{4.15}
$$

one can rewrite Eq. (4.13) as

$$
\frac {\gamma}{\gamma + \eta} \mu + \frac {\eta}{\gamma + \eta} \mu_ {B} = \frac {V ^ {\prime} (\lambda) \lambda}{b _ {1} + b _ {2}}.\tag{4.16}
$$

The theorem follows from solving Eq. (4.14) and Eq. (4.16) for $\mu$ and $\mu_B$ .

Theorem 4.3 dictates that the firm should equate the backup capacity with the capacity of the firm's computer, and their optimal long-run capacities are determined by the sum of their respective marginal capacity costs, the demand function $V'(\lambda)$ , and underlying queuing characteristic. When the demand function belongs to the class of isoelastic demand functions and has the form, $V'(\lambda) = A / \lambda^{\alpha}$ , where $0 < \alpha \leq 1$ , close-form solutions for capacities $\mu^{*}$ and $\mu_{B}^{*}$ are available for $\alpha=0.5$ and $\alpha=1$ . The following corollary is a direct application of Theorem 4.3.

Corollary 4.1. If $V'(\lambda) = A / \lambda^{\alpha}$ , where $0 < \alpha \leq 1$ , then

$$
\mu^ {*} = \mu_ {B} ^ {*} = \frac {A}{b _ {1} + b _ {2}} \left| \frac {A}{b _ {1} + b _ {2}} - \sqrt {\frac {v}{b _ {1} + b _ {2}}} \right|,
$$

$$
\text { for } \alpha = 0. 5;\tag{4.17}
$$

and

$$
\mu^ {*} = \mu_ {B} ^ {*} = \frac {A}{b _ {1} + b _ {2}}, \text { for } \alpha = 1.\tag{4.18}
$$

Two interesting observations are in order. First of all, according to Theorem 4.3, optimal long-run backup capacity should equal the firm's optimal long-run original capacity for all forms of demand functions of computing. This result supports a common industry practice called "hot backup" strategy, i.e., to operate in parallel another identical computer site [5]. Secondly, if the demand function is isoelastic and has unit elasticity, the optimal capacities depend only on parameter $A$ of the demand function and the sum of marginal capacity costs $b_{1}$ and $b_{2}$ , regardless of the underlying queuing characteristics.

A numerical exploration is conducted to address the questions raised at the beginning of this section and to compare a computer system having backup capacity with the case without backup. In the numerical example that follows, the expected gross value function of computing takes the form $V'(\lambda)=100/\lambda^{\alpha}$ . Since the numerical results for $\alpha=0.5$ exhibit the same pattern as for $\alpha=1$ , only the case where $\alpha=1$ is reported here. The mean time between failures (1/ $\eta$ ), MTBF, is fixed at 259200 minutes (6 months). The mean time to repair (1/ $\gamma$ ), MTTR, will be varied from 60 to 180 minutes to observe the impact of a computer system's reliability on various aspects of concern. The marginal capacity cost of the firm's computer, $b_{1}$ , equals 1. The marginal capacity cost of backup capacity, $b_{2}$ , equals 3. Since the fixed overhead of operating the firm's computer, the B in Eq. (3.6), and the fixed fee, F, in Eq. (4.1) will not affect the maximization problem, they are set to zero.

![](/api/attachments/4HE6JCPQ/fulltext/images/ddaa3eb3e66fbcb22d01b2b696c7c9b8ffcd12a0b2a2af6091441c398a96f5b2.jpg)  
Fig. 7. Optimal arrival rates of various configurations.

Fig. 7 shows the behavior of optimal arrival rates as delay cost changes. The optimal arrival rate remains relatively stable for the service system with backup capacity, while the arrival rate declines sharply as delay cost increases for the computer system without backup. The arrival rates are smaller for those systems with longer mean time to repair, given the same delay cost.

In Fig. 8, optimal capacities are plotted against delay cost for different computer configurations. The optimal capacity for computer systems with backup is the same regardless of the delay cost as described in Corollary 4.1. Optimal capacities are smaller for computer systems with longer mean time to repair. These findings are consistent with those in Section 3, the reason being, longer mean time to repair translates into longer expected time spent in the system for submitted jobs. Longer expected time spent in the system will discourage the arrival of low-value jobs, thus requiring less capacity to service jobs with higher values.

Fig. 9 displays the maximum net values of computer systems with backup capacity and those systems with different reliability measures but without backup. Fig. 9 directly addresses the question whether or not to consider backup capacities. The decision depends on several factors: the ratio of the marginal backup capacity cost to the marginal capacity cost of the firm's computer, the reliability of the firm's computer, and the delay cost of jobs. Fig. 9 shows one intuitive and yet important result: having backup capacity is imperative for an environment where the delay cost is high and the computer system is unreliable in terms of longer repair time given the same mean time between failures. For instance, it is cost effective to acquire backup capacity if the delay cost exceeds \$13/min and it takes more than four hours to repair the firm's computer, even though the cost of backup is three times as high as that of the firm's computer.

![](/api/attachments/4HE6JCPQ/fulltext/images/99a7662107d43c19c83ef2d3f41eb5e19d36350b956856fd94439e31f0da2a0e.jpg)  
Fig. 8. Optimal capacities of various configurations.

![](/api/attachments/4HE6JCPQ/fulltext/images/33b552da231315abac33319cc6d04225a1fd3fc36043feca46be7f4733de7099.jpg)  
Fig. 9. Maximum net values of various configurations.

Hence, managers should collect empirical data regarding the reliability of the firm's computer system, the cost of running the firm's computer, and delay cost. Fig. 9 also implies that managers should keep track of the cost trend of the computer backup service from the outside market because acquiring backup capacity becomes more and more attractive as the cost of obtaining backup capacity gets lower.

## 5. Summary and conclusions

This paper studies the impact of breakdowns on pricing and capacity decisions of a computer service system. Previous research that studies delay cost in the pricing and capacity decisions does not explicitly consider computer breakdowns. According to a recent survey, computer downtime is a serious reality that companies must reckon with. The results in this paper show that computer breakdowns have significant impact on various aspects of concern. In general, computer breakdowns increase the expected time of jobs in the system, thus discouraging the submission of low-value jobs. A smaller computer capacity is needed to service the jobs with higher values compared to the case where computer works all the time. The utilization ratio is lower in view of computer breakdowns. The firm, faced with computer breakdowns, has to increase the price of computer service. The numerical examples presented in this paper suggest that the increase in price may be significant for some firms.

This paper also examines the issue of whether to obtain backup computer capacity when the computer system is in repair. The decision depends on the delay cost, the reliability of the computer system and capacity costs of the firm's computer and the backup computer. Therefore, managers must collect empirical data on these variables to make correct decisions. The findings suggest that it is imperative to acquire backup capacity when computing is critical to the firm in terms of high delay cost of jobs. The research results support the “hot backup” strategy, a common industry practice to operate in parallel two computers with the same capacity. A theorem in this paper provides a simple and helpful guideline for the pricing of computer service when backup capacity is available. That is, the firm should charge users the total marginal capacity costs of the firm's computer as well as the backup. Finally, if the demand function of computing has unit elasticity, optimal capacity decision depends only on the demand characteristic and the marginal capacity costs of the firm's computer and the backup, regardless of the delay cost.

## Acknowledgements

This paper receives helpful comments from Professors Marshall Freimer, John McCray, Lawrence Pulley, William Richmond, Ushio Sumita, and Ahmed Zaki. I would like to thank the research seminar participants of the University of Rochester, and the Institute of Information Management at the National Sun Yat-Sen University in Taiwan, R.O.C. for their useful feedback. Very constructive comments and suggestions from the guest editor and two anonymous referees are greatly appreciated.

## Appendix A. Proof of Theorem 2.1

Let $p_{n,u} = \text{Prob}\{\text{The computer is up and there are } n \text{ jobs in the system}\}$ and $p_{n,d} = \text{Prob}\{\text{The computer is down and there are } n \text{ jobs in the system}\}$ . Then, one has the following sets of balance equations.

$$
p _ {0, u} (\lambda + \eta) = p _ {1, u} \mu + p _ {0, d} \gamma ,\tag{A.1}
$$

$$
p _ {n, u} (\lambda + \mu + \eta) = p _ {n - 1, u} \lambda + p _ {n + 1, u} \mu + p _ {n, d} \gamma \text {   for   } n \geq 2,\tag{A.2}
$$

$$
p _ {0, d} (\lambda + \gamma) = p _ {0, u} \eta ,\tag{A.3}
$$

$$
p _ {n, d} (\lambda + \gamma) = p _ {n - 1, d} \lambda + p _ {n, u} \eta \text {   for   } n \geq 2.\tag{A.4}
$$

Define the generating functions $\pi_u(z)$ and $\pi_d(z)$ as follows.

$$
\pi_ {u} (z) = \sum_ {n = 0} ^ {\infty} p _ {n, u} z ^ {n},\tag{A.5}
$$

and

$$
\pi_ {d} (z) = \sum_ {n = 0} ^ {\infty} p _ {n, d} z ^ {n}.\tag{A.6}
$$

From Eq. (A.1) through Eq. (A.4), it follows that

$$
\pi_ {d} (z) = \frac {\eta}{(\lambda + \gamma - \lambda z)} \pi_ {u} (z),\tag{A.7}
$$

and

$$
\mu \pi_ {u} (z) - \mu p _ {0, u} = \lambda z \pi_ {u} (z) + \lambda z \pi_ {d} (z).\tag{A.8}
$$

After some algebra, one has

$$
\pi_ {u} (z) + \pi_ {d} (z) = \frac {\mu (\lambda + \gamma + \eta - \lambda z) p _ {0 , u}}{\left[ \lambda^ {2} z ^ {2} - (\lambda \mu + \lambda \gamma + \lambda \eta + \lambda^ {2}) z + \mu (\lambda + \gamma) \right]}.\tag{A.9}
$$

By letting $z = 1$ in Eq. (A.9),

$$
p _ {0, u} = \frac {\gamma}{\gamma + \eta} - \frac {\lambda}{\mu}.
$$

Since $d / dz[\pi_u(z) + \pi_d(z)]_{z=1}$ is the expected number of jobs in the system, the theorem follows from Little's law.

Appendix B. Proof of Theorem 4.1

Define $p_{n,u} = \text{Prob}\{\text{The computer is up and there are } n \text{ jobs in the system}\}$ and $p_{n,d} = \text{Prob}\{\text{The computer is down and there are } n \text{ jobs in the system}\}$ . Then, one has the following sets of balance equations:

$$
p _ {0, d} (\lambda + \gamma) = p _ {1, d} \mu_ {B} + p _ {0, u} \eta ,\tag{B.1}
$$

$$
p _ {n, d} (\lambda + \gamma + \mu_ {B}) = \lambda p _ {n - 1, d} + \mu_ {B} p _ {n + 1, d} + \eta p _ {n, u} \text {   for   } n \geq 1,\tag{B.2}
$$

$$
p _ {0, u} (\lambda + \eta) = p _ {1, u} \mu + p _ {0, d} \gamma ,\tag{B.3}
$$

and

$$
p _ {n, u} (\lambda + \eta + \mu) = \lambda p _ {n - 1, u} + \mu p _ {n + 1, u} + \gamma p _ {n, d} \text {   for   } n \geq 2.\tag{B.4}
$$

Let the generating functions $\pi_u(z)$ and $\pi_d(z)$ be as follows.

$$
\pi_ {u} (z) = \sum_ {n = 0} ^ {\infty} p _ {n, u} z ^ {n},\tag{B.5}
$$

and

$$
\pi_ {d} (z) = \sum_ {n = 0} ^ {\infty} p _ {n, d} z ^ {n}.\tag{B.6}
$$

Combining Eqs. (B.1), (B.2), (B.3) and (B.4), one has

$$
\lambda \left(p _ {n, u} + p _ {n, d}\right) = \mu p _ {n + 1, u} + \mu_ {B} p _ {n + 1, d} \text {   for   } n \geq 0.\tag{B.7}
$$

It then follows from Eq. (B.7) that

$$
\pi_ {u} (z) = \frac {\mu_ {B} - \lambda z}{\lambda z - \mu} \pi_ {d} (z) - \frac {\mu p _ {0 , u} + \mu_ {B} p _ {0 , d}}{\lambda z - \mu}.\tag{B.8}
$$

Combining Eq. (B.1) and Eq. (B.2) leads to

$$
\left[ (\lambda + \gamma + \mu_ {B}) - \lambda z - \frac {\mu_ {B}}{z} \right] \pi_ {d} (z) = \eta \pi_ {u} (z) + \left(\mu_ {B} - \frac {\mu_ {B}}{z}\right) p _ {0. d}.\tag{B.9}
$$

By substituting Eq. (B.8) into Eq. (B.9), one has

$$
\pi_ {d} (z) = \frac {(\lambda z - \mu) (1 - z) \mu_ {B} p _ {0 , d} + \eta z (\mu p _ {0 , u} + \mu_ {B} p _ {0 , d})}{\lambda^ {2} z ^ {3} - \lambda (\lambda + \gamma + \eta + \mu + \mu_ {B}) z ^ {2} + [ \mu (\lambda + \gamma + \mu_ {B}) + \mu_ {B} (\lambda + \eta) ] z - \mu \mu_ {B}}.\tag{B.10}
$$

Since $\pi_d(1)$ is the ergodic probability that the computer system is down, which equals $\eta / (\gamma + \eta)$ , letting $z = 1$ in Eq. (B.10) and solving for $(\mu p_{0,u} + \mu_B p_{0,d})$ gives

$$
\pi_ {d} (z) = \frac {(\lambda z - \mu) (1 - z) \mu_ {B} p _ {0 , d} + \eta z \left[ \left((\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta)\right) - \lambda \right]}{\lambda^ {2} z ^ {3} - \lambda (\lambda + \gamma + \eta + \mu + \mu_ {B}) z ^ {2} + \left[ \mu (\lambda + \gamma + \mu_ {B}) + \mu_ {B} (\lambda + \eta) \right] z - \mu \mu_ {B}}.\tag{B.11}
$$

After substituting Eq. (B.10) into Eq. (B.8) and some algebra, one has

$$
\begin{array}{r c l} \pi_ {u} (z) & = & \frac {\left(\mu_ {B} - \lambda z\right) (1 - z) \mu_ {B} p _ {0 , d}}{\lambda^ {2} z ^ {3} - \lambda (\lambda + \gamma + \eta + \mu + \mu_ {B}) z ^ {2} + \left[ \mu (\lambda + \gamma + \mu_ {B}) + \mu_ {B} (\lambda + \eta) \right] z - \mu \mu_ {B}} \\ & + & \frac {\left[ \left((\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta)\right) - \lambda \right] (- \lambda z ^ {2} + (\lambda + \gamma + \mu_ {B}) z - \mu B)}{\lambda^ {2} z ^ {3} - \lambda (\lambda + \gamma + \eta + \mu + \mu_ {B}) z ^ {2} + \left[ \mu (\lambda + \gamma + \mu_ {B}) + \mu_ {B} (\lambda + \eta) \right] z - \mu \mu_ {B}}. \end{array}\tag{B.12}
$$

The expected time spent in such system, $T(\lambda, \mu, \mu_B)$ , follows from Little's law. That is,

$$
T (\lambda , \mu , \mu_ {B}) = \frac {\pi_ {d} ^ {\prime} (1) + \pi_ {u} ^ {\prime} (1)}{\lambda},\tag{B.13}
$$

due to the fact that $\pi_d'(1) + \pi_u'(1)$ equals the expected number of jobs in the system. After some algebra, the theorem follows from Eqs. (B.11), (B.12) and (B.13).

## Appendix C. The derivation of Eq. (4.3)

Recall from Eq. (B.11) that

$$
\pi_ {d} (z) = \frac {(\lambda z - \mu) (1 - z) \mu_ {B} p _ {0 , d} + \eta z [ ((\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta)) - \lambda ]}{\lambda^ {2} z ^ {3} - \lambda (\lambda + \gamma + \eta + \mu + \mu_ {B}) z ^ {2} + [ \mu (\lambda + \gamma + \mu_ {B}) + \mu_ {B} (\lambda + \eta) ] z - \mu \mu_ {B}}.\tag{C.1}
$$

Letting $G(z)$ be the denominator of $\pi_d(z)$ , one has

$$
G (1) = (\gamma + \eta) \left[ \frac {\gamma \mu + \eta \mu_ {B}}{\gamma + \eta} - \lambda \right] = (\gamma + \eta) (\mu p _ {0, u} + \mu_ {B} p _ {0, d}) > 0,\tag{C.2}
$$

$$
G (0) = - \mu \mu_ {B} <   0,\tag{C.3}
$$

$$
G (- 1) = - \lambda^ {2} - \lambda (\lambda + \gamma + \eta + \mu + \mu_ {B}) - [ \mu (\lambda + \gamma + \mu_ {B}) + \mu_ {B} (\lambda + \eta) ] - \mu \mu_ {B} <   0,\tag{C.4}
$$

and

$$
G (- 1) <   G (0).\tag{C.5}
$$

Since $G(z)$ is a cubic polynomial of $z$ , $G(z) = 0$ has three zeros. From $G(1) > 0$ and $G(0) < 0$ , $G(z)$ has either one or three zeros in the interval (0,1). Since $\pi_d(z)$ must converge inside or on the unit circle and the numerator of $\pi_d(z)$ is quadratic in $z$ , this implies that $G(z)$ has at most two zeros inside or on the unit circle. Hence, there exists only one zero in the interval (0,1). One can easily deduce that no zeros exist in $(-1,0)$ from the fact that $G(-1) < G(0)$ and the same line of reasoning. Denote the zero of $G(z)$ that lies in the interval (0,1) by $\bar{z}$ . Then the numerator of $\pi_d(z)$ must also have the same zero $\bar{z}$ . This leads to

$$
p _ {0, d} = \frac {\eta \bar {z} \left[ \left(\left(\gamma \mu + \eta \mu_ {B}\right) / (\gamma + \eta)\right) - \lambda \right]}{\mu_ {B} (1 - \bar {z}) (\mu - \lambda \bar {z})}. \quad \square\tag{C.6}
$$

## Appendix D. The approximation of $T(\lambda, \mu, \mu_B)$ in Theorem 4.1

In the computing environment, job arrival and processing time is measured in seconds. However, the mean time between failures $(1/\eta)$ is measured in months and the mean time to repair $(1/\gamma)$ is in the order of hours or days. This means that the inverse of the mean time between failures, $\eta$ , and the inverse of the mean time to repair, $\gamma$ , are numerically negligible compared with $\lambda$ , $\mu$ , and $\mu_{B}$ . Hence, $G(z)$ can be properly approximated by

$$
G (z) \cong \lambda^ {2} z ^ {3} - \lambda (\lambda + \mu + \mu_ {B}) z ^ {2} + (\mu \mu_ {B} + \lambda \mu_ {B} + \lambda \mu) z - \mu \mu_ {B}.\tag{D.1}
$$

Hence,

$$
G (z) \cong (\lambda z - \mu_ {B}) (\lambda z - \mu) (z - 1).\tag{D.2}
$$

This implies that the zero of $G(z)$ is extremely close to one and can be approximated by a single iteration of the Newton's method using one as the starting point. That is,

$$
\bar {z} \cong 1 - \frac {G (1)}{G ^ {\prime} (1)}.\tag{D.3}
$$

After some algebra, one has

$$
1 - \bar {z} \cong \frac {(\mu - \lambda) \gamma + (\mu_ {B} - \lambda) \eta}{(\mu - \lambda) (\mu_ {B} - \lambda) + (\mu - 2 \lambda) \gamma + (\mu_ {B} - 2 \lambda) \eta}.\tag{D.4}
$$

Substituting Eq. (D.4) into Eq. (4.3) and after some algebra, it follows that

$$
p _ {0, d} \cong \frac {\eta \bar {z}}{(\gamma + \eta) \mu_ {B}} \frac {(\mu - \lambda) (\mu_ {B} - \lambda) + (\mu - 2 \lambda) \gamma + (\mu_ {B} - 2 \lambda) \eta}{\mu - \lambda \bar {z}}.\tag{D.5}
$$

Since $\gamma$ and $\eta$ are numerically negligible compared with $\lambda$ , $\mu$ , and $\mu_B$ , and $\bar{z}$ is extremely close to one, the probability $p_{0,d}$ can be approximated by

$$
p _ {0, d} \cong \frac {\eta (\mu_ {B} - \lambda)}{(\gamma + \eta) \mu_ {B}}.\tag{D.6}
$$

In fact, the approximation (Eq. (D.6)) holds for any reasonable range of parameters in the computing setting. Substituting Eq. (D.6) back to Eq. (4.2) results in a much simplified expression for $T(\lambda,\mu,\mu_{B})$ ,

$$
T (\lambda , \mu , \mu_ {B}) \cong \frac {1}{\left((\gamma \mu + \eta \mu_ {B}) / (\gamma + \eta)\right) - \lambda}. \quad \square\tag{D.7}
$$

## References

[1] M-C. Ballou, Survey Pegs Computer Downtime Costs at \$4 Billion, Computerworld (August 10, 1992) 53–56.

[2] S. Dewan and H. Mendelson, User Delay Costs and Internal Pricing for a Service Facility, Management Science 36, No. 12 (1990) 1502–1517.

[3] M. Freimer, U. Sumita and H.K. Cheng, Analysis of Economics of Computer Backup Service, IEICE Transactions on Communications E75-B, No. 5 (1992) 385–400.

[4] R.W. Hall, Queuing Methods for Services and Manufacturing (Prentice-Hall, 1991) 289–290.

[5] J. Mason, Hot Sites Turn Up the Heat on America, Computerworld (April 23, 1990) 88–89.

[6] H. Mendelson, Pricing Computer Services: Queuing Effect, Communications of the ACM 28, No. 3 (1985) 312–322.

[7] H. Mendelson, Economics of Scale in Computing: Grosch's Law Revisited, Communications of the ACM 30, No. 12 (1987) 1066–1073.

[8] H. Mendelson and S. Whang, Optimal Incentive-Compatible Priority Pricing for the M/M/1 Queue, Operations Research 38, No. 5 (1990) 870–884.

[9] B.L. Miller and A.G. Buckman, Cost Allocation and Opportunity Costs, Management Science 33, No. 5 (1987) 626–639.

[10] S. Stidham, Jr., Pricing and Capacity Decisions for a Service Facility: Stability and Multiple Local Optima, Management Science 38, No. 8 (1992) 1121–1139.

![](/api/attachments/4HE6JCPQ/fulltext/images/5ebeee2dd3417c6eb8b9dbd24df4cb226dcf15759b06a7f5b42dba506c1655c5.jpg)

Hsing Kenneth Cheng is Assistant Professor of Information Technology at the Graduate School of Business Administration, The College of William and Mary. He received his B.S. in Electronic Engineering and his M.B.A. from the National Chiao-Tung University (Taiwan, R.O.C.) and his Ph.D. from William E. Simon Graduate School of Business Administration of the University of Rochester. His research interests include information systems economics,

managing the risks of computer system breakdowns, and analyzing the impacts and policy implications of information technology on society. His research has appeared or will appear in Computers and Operations Research, IEICE Transactions on Communications, Decision Support Systems, European Journal of Operational Research, Journal of Business Ethics, and leading conference proceedings. He contributed a chapter on computer fraud in Corporate Misconduct: The Legal, Societal, and Management Issues.
