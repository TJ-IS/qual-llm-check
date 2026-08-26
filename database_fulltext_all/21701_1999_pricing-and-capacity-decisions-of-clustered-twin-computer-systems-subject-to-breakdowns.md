---
otero_id: 21701
otero_key: "DHYWKATZ"
title: "Pricing and capacity decisions of clustered twin-computer systems subject to breakdowns"
authors: "Hsing Kenneth Cheng"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00089-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Pricing and capacity decisions of clustered twin-computer systems subject to breakdowns

Hsing Kenneth Cheng )

Department of Decision and Information Sciences, Warrington College of Business Administration, The UniÕersity of Florida, GainesÕille, FL 32611-7169, USA

Received 9 June 1998; revised 15 September 1998; accepted 25 November 1998

## Abstract

More and more organizations are running a clustered twin-computer system to tackle the rapidly growing demand of computer capacity. For example, the German airline Deutsche Lufthansa uses two Unisys 2200<sup>r</sup>644 mainframes to handle the torrent of data from passenger reservations and check-ins, baggage handling, and flight scheduling. Basic queuing theory suggests that consolidating twin-computer systems to a bigger system with the same overall capacity will result in a lower total time in the system. The prevailing rationale for a clustered twin-computer system is that it is an effective way of coping with not only the capacity growth challenge but also the computer downtime problem. This paper examines the impact of breakdowns on the decision to consolidate or cluster computer systems. This research finds that both the consolidated single computer system and the clustered twin-computer system, under the same breakdown parameters, have the same effective computer capacity. However, the clustered twin-computer system has a shorter expected time in the system for most cases. The clustered twin-computer system also performs better when there is a heavy traffic intensity. For firms with a consolidated single computer system, this research finds that it pays off to reduce the mean time to repair than to increase the mean time between failures. Finally, this paper derives the optimal pricing and capacity of a firm’s clustered twin-computer system that will maximize the net value of computing by incorporating the analytical model in a microeconomic framework to consider the effect of delay cost of computer processing. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Clustering technology; Computer breakdowns; Multi-server queuing systems; Pricing and capacity decisions

## 1. Introduction

In the late 1980s, the German airline Deutsche Lufthansa faced the challenge of keeping up with the torrent of data from passenger reservations and check-ins, baggage handling and flight scheduling that was growing at 50% a year. Lufthansa airline would run out of its computer capacity in less than a year and a half at this dazzling rate of demand growth, see Guterl 4 , and Laudon and Laudon 7 .<sup>w x</sup> <sup>w x</sup> The typical solution to such a problem is to upgrade the mainframe. In February 1992, however, Lufthansa switched to two Unisys 2200<sup>r</sup>644 series mainframes clustered together. Essentially, clustering technology allows computing requests to be sent to one of the twin computers for processing. Fig. 1 shows a typical configuration of a clustered twin-computer system.

![](/api/attachments/DHYWKATZ/fulltext/images/879b2896ec666efc2651f2155feb4b22438d8c40018cd1958a48574b0346f519.jpg)  
Fig. 1. A typical clustered twin-computer system configuration.

Since a clustered twin-computer system corresponds to a multi-server queuing system, the fundamental research question is why not opt for a bigger computer with twice the capacity of each of the two smaller computers clustered together? Queuing theory favors a consolidated single server system over a multiple server system. A computer system is commonly modeled as an M<sup>r</sup>M<sup>r</sup>1 queuing system. Then the Lufthansa airline’s clustered system consisting of two Unisys 2200<sup>r</sup>644 represents an M<sup>r</sup>M<sup>r</sup>2 queuing system. It is known that M<sup>r</sup>M<sup>r</sup>1 system has a lower oÕerall time in the system than the M<sup>r</sup>M<sup>r</sup>2. The intuition behind this standard result is as follows. Both M<sup>r</sup>M<sup>r</sup>1 and M<sup>r</sup>M<sup>r</sup>2 perform the same when there is no job, or two or more jobs in the system. However, when there is only one job in the system, the M<sup>r</sup>M<sup>r</sup>1 system has the advantage of twice as much processing capacity as the M<sup>r</sup>M<sup>r</sup>2 system.

The prevailing rationale for a clustered computer system is that it is an effective way of coping with not only the capacity growth challenge but also the computer downtime problem. In case one computer in the clustered system breaks down, the other computer takes over the processing until the failed computer becomes available, a feature generally described by the term ‘automatic failover’ in the industry. Apparently, the performance behavior of the M<sup>r</sup>M<sup>r</sup>1 system versus the M<sup>r</sup>M<sup>r</sup>2 system is less clear when breakdowns are allowed. One objective of this paper is to examine the impact of breakdowns on the decision to consolidate or cluster computer systems. This paper provides useful and timely research results for decision makers as clustering for both large computers and servers becomes popular. The popularity of clustering is indicated by the fact that vendors such as Digital, IBM, and NCR reported that 40% of their midrange and high-end servers are shipped with clustering capability 13 .

To characterize conditions under which a clustered twin-computer system will have a better performance, this paper develops a queuing model for the clustered twin-computer system subject to breakdowns. The analytical results of such a twin-computer system are compared with those of a consolidated single computer system with the same total capacity subject to identical breakdown parameters. A major contribution of this paper is the derivation of a useful approximation to the analytical model of clustered twin-computer systems that is found too complicated for further analyses.

This research finds that both the consolidated single computer system and the clustered twin-computer system, under the same breakdown parameters, have the same effective computer capacity. However, the clustered twin-computer system has a shorter expected time in the system for most cases according to numerical experiments using realistic parameter data. The clustered twin-computer system also performs better when there is a heavy traffic intensity. For firms with a consolidated single computer system, this research finds that it pays off to reduce the mean time to repair than to increase the mean time between failures.

The rest of the paper is structured as follows. Section 2 develops analytical models for both a consolidated single computer and a clustered twincomputer system subject to the same breakdown parameters. The analytical results of the expected time in a twin-computer system subject to breakdowns are found too complicated for further analyses. Hence, a useful approximation is proposed in this section as the basis of performance comparison. Numerical explorations provide further insights into the performance comparison of these two different configurations in Section 3. Section 4 describes a firm’s optimization problem where both the pricing of computing service and the capacity decisions have to be jointly considered to maximize the net value of computing. The formulation of the firm’s optimization problem incorporates the delay cost factor, i.e., the congestion cost resulting from queuing delay. Section 5 provides concluding remarks and discusses future research.

## 2. The model

Consider a clustered twin-computer system where there is a Poisson stream with parameter of arriving jobs requiring computer processing, and arriving jobs have a homogeneous service requirement. Service times of arriving jobs are assumed to be independently and identically drawn from an exponential distribution with mean $1 / \mu$ according to the First Come First Serve FCFS service discipline. Each ofŽ . the twin computers has a capacity of processing $\mu$ jobs per unit of time. This corresponds to an $M / M / 2$ queuing system with arrival rate and service rate $\mu$ for each server. To model the computer breakdowns, assume that each computer’s downtime and uptime follow exponential distributions with parameters $\gamma$ and , respectively. Hence, the inverse of the downtime parameter, $1 / \gamma$ , can be interpreted as the mean time to repair MTTR and the inverse of the uptimeŽ . parameter, $1 / \eta ,$ amounts to the mean time between failures MTBF . The MTTR and MTBF are com-Ž . mon measures used in the industry to represent a computer’s breakdown characteristics and availability. Each of the twin computers is assumed to break down and repair independently of each other.

Some discussions on modeling the clustered computer systems are in order. First, a typical clustered twin-computer system linked together by cabling and software is a group of two independent computers. This leads to the independent breakdowns and repairs assumption described above. Each computer in the cluster can be running applications while acting as a standby for the other. In the event of one computer’s failure, the other will take over the operations, a feature enabled by logic in the clustering software running on both computers. Second, a clustered twin-computer system is not to be confused with Symmetrical Multi-Processing SMP or Scal-Ž . able Parallel Processing SP2 where theŽ . main memory is shared by all processors computers . While aŽ . clustered twin-computer system consists of two independent computers, they may share a common pool of secondary storage in the shared-disk architecture, as depicted in Fig. 1. In the shared-nothing architecture, each processor has its own disk storage. The model rules out breakdowns of the pool of common disks because of extremely high reliability of today’s RAID Redundant Array of Independent Disks andŽ . HA High Availability disk storage products. Third,Ž . the model ignores a small overhead incurred in the clustered twin-computer system due primarily to synchronous waits created by the coupling facility that links computers to the shared data. Finally, the computer system’s breakdowns may result from hardware failures or software malfunctions. This model is general in nature and does not attempt to distinguish specific types of computer failures.

For comparison purposes, also consider a consolidated single computer system having twice the processing capacity of each of the twin computers. That is, this single computer system has a capacity $2 \mu .$ This single computer service system has an identical stream of arriving jobs and breakdown characteristics.

Some may conjecture that the clustered twin-computer system will have a larger effective long-runŽ expected capacity since at least one computer is. likely to run. Proposition 2.1 proves that neither the single computer system nor the clustered twin computers provide more effective capacity. Both configurations have the same effective capacity as long as they have the same breakdown characteristics.

Proposition 2.1. Both the consolidated single computer system and the clustered twin-computer system aforementioned have the same effective expectedŽ . capacity, $2 \mu [ \gamma / ( \gamma + \eta ) ]$

## Proof. Please see Appendix A.

After one knows Proposition 2.1, a natural question arises. Will both configurations have the same expected time in the system? One objective of this section is to compare the expected time in the system, including both queuing and service times, of these two competing configurations. The expected time in the consolidated single computer system subject to breakdowns is readily available from Cheng 2 as follows.<sup>w</sup> <sup>x</sup>

$$
T _ {\mathrm{ss}} (\lambda , \mu , \gamma , \eta) = \frac {1 + \frac {2 \eta \mu}{(\gamma + \eta) ^ {2}}}{2 \mu \frac {\gamma}{\gamma + \eta} - \lambda}\tag{2.1}
$$

where the subscript ss in Eq. 2.1 stands for SingleŽ . Server.

The earliest theoretical work on a multiple-server system subject to breakdowns is due to Mitrany and Avi-Itzhak 10 . A similar but simpler method, prob- <sup>w</sup> <sup>x</sup> ability generating function method, is used in Appendix B to derive the expected time in the clustered twin-computer system subject to breakdowns. The expected time in a clustered twin-computer system equals the sum of Eqs. B.17 , B.18 and B.19 in Ž . Ž . Ž . Appendix B divided by the arrival rate . Eqs. Ž . Ž . Ž . Ž . Ž . Ž .B.17 , B.18 , B.19 , B.20 , B.21 , B.22 and Ž . B.23 are equivalent to the results in Ref. 10 ,<sup>w</sup> <sup>x</sup> although some equations have different expressions.

The analytical results for the clustered twin-computer system are too complicated for subsequent analyses, especially when they are included in a firm’s overall optimization problem to find the optimal pricing and capacity of such a twin-computer system. A useful approximation to the clustered twin-computer system’s performance is proposed by taking advantage of certain characteristics in the computing environment as follows.

Proposition 2.2. In the computing environment, and  are numerically negligible compared with and $\mu$ in mathematical expressions.

Observations. This is a rather intuitive result. In the computing environment, and $\mu$ are in the order of hundreds or thousands of jobs submitted and processed per minute, while the computer breaks down once every several months and it takes hours to repair. In other words, the inverse of $\eta ,$ MTBF, is measured in months and the inverse of $\gamma ,$ , MTTR, is measured in terms of hours. That is, and $\mu$ are seÕeral orders of magnitude bigger than $\gamma$ and $\eta .$

Therefore, $\gamma$ and $\eta$ are numerically negligible compared with  and $\mu$ in mathematical expressions. Q.E.D.

Proposition 2.2 holds true in the computing environment, but cannot be applied in a manufacturing setting since the several orders of magnitude differences phenomenon does not occur in manufacturing. Furthermore, a computer has an infinite waiting room for jobs to be processed, while the buffer space in a manufacturing environment is usually limited.

Using Proposition 2.2, a useful approximation for the expected time in a clustered twin-computer system is derived in the following theorem. Extra care has been taken in deriving the approximation. One must note that $\gamma$ and $\eta$ are numerically negligible only compared with  and $\mu ,$ , while  and $\eta$ should be retained in other places of expressions to maintain the accuracy of the approximation. For example, a term $\gamma \mu$ cannot be dropped out when compared with $\mu .$

Theorem 2.3. An approximation for the expected time in a clustered twin-computer system is given by

$$
T _ {\mathrm{tc}} (\lambda , \mu , \gamma , \eta) = \frac {1 + \frac {\eta \mu}{(\gamma + \eta) ^ {2}}}{\frac {\gamma}{\gamma + \eta} 2 \mu - \lambda} + \frac {\frac {\gamma}{\gamma + \eta}}{2 \mu + \lambda}.\tag{2.2}
$$

Proof. Please see Appendix C.

When there is no breakdown, i.e., $\gamma / ( \gamma + \eta ) \to 1$ and $\eta / ( \gamma + \eta ) \to 0$ , the expected time $T _ { \mathrm { t c } } ( \lambda , \mu , \gamma , \eta )$ reduces to that of a regular $M / M / 2$ queue. This is a corroboration of Theorem $2 . 3 \mathrm { ^ , s }$ validity. The following corollary is a direct result of Theorem 2.3 and Eq. 2.1 .Ž .

Corollary 2.4. The clustered twin-computer system has a shorter expected time in the system than the consolidated single computer system if and only if

$$
\frac {\frac {\gamma}{\gamma + \eta}}{2 \mu + \lambda} <   \frac {\frac {\eta \mu}{(\gamma + \eta) ^ {2}}}{2 \mu \frac {\gamma}{\gamma + \eta} - \lambda}.\tag{2.3}
$$

Although the expected effective capacity of the single system and the twin-computer system are the same as shown in Proposition 2.1, the Õariance of the capacity will be different. For simplicity of understanding, suppose that the computer system works half the time. Then, the consolidated single system has $2 \mu$ capacity half the time and zero capacity half the time. The clustered twin-computer will have $2 \mu$ capacity a quarter time, $\mu$ capacity half the time, and zero capacity a quarter time. Thus the effective capacity is the same, but the variance of capacity is higher in the single computer system case than in the clustered twin computers. Since this variance is induced by breakdowns, one should expect that the twin cluster will have better performance when breakdowns are more often in terms of increased MTTR or reduced MTBF, as predicted by Corollary 2.4.

On the other hand, the single computer system has a higher performance under low loads when there are few breakdowns. Hence, there exists a trade-off between higher performance under low loads in the consolidated single computer system Ž . when breakdowns are rare and less capacity variance under the twin cluster system. To gain further insights, numerical experiments were conducted and reported in Section 3.

## 3. To consolidate or to cluster?

This section compares the expected time in two configurations, a clustered twin-computer system with capacity $\mu$ for each computer versus a consolidated single computer system with capacity $2 \mu .$ Both systems have identical breakdown characteristics, i.e., the same mean time between failures Ž . Ž . MTBF and the same mean time to repair MTTR . Four parameters under consideration include: 1 theŽ . arrival rate of jobs for computing processing, , 2Ž . the computer capacity, , 3 MTBF, and 4 MTTR.Ž . Ž . Only one parameter will be changed each time while the other three remain the same. The following numerical experiments aimed at uncovering the conditions under which the clustered twin-computer system generates a lower, or higher for this matter, expected time in the system than the consolidated single computer system. <sup>1</sup>

![](/api/attachments/DHYWKATZ/fulltext/images/2d0dab700914695e58bc842eddcc3f8daeb5b2957ffe3db644d07d792ea6cd51.jpg)  
Fig. 2. Expected time in the system as a function of MTBF Ž .MTTR<sup>s</sup>60 min .

Figs. 2 and 3 plot the expected overall time in the system of two different configurations where the broken line and the solid line represent the consolidated single computer and the clustered twin-computer respectively. The expected time in the system is plotted as a function of the mean time between failures MTBF , ranging from 30 to 360 days. The Ž . mean time to repair MTTR in Fig. 2 is 60 min, Ž . while MTTR in Fig. 3 is reduced to 10 min. The arrival rate is held constant at 480 jobs per minute and each configuration has a total capacity of processing 900 jobs per minute. The parameter values conform to empirical data of business computer systems reported in Ballou 1 and Simpson 11 .<sup>w x</sup> <sup>w</sup> <sup>x</sup>

When the mean time to repair MTTR equals 60 Ž . min, Fig. 2 shows that the clustered twin-computer has a lower expected time in the system even if the mean time between failures equals one year. The difference of the expected time in the system becomes smaller as the mean time between failures gets longer as depicted in Fig. 2. In general, the more reliable the computer system is, the better a consolidated single computer will be. However, a computer is considered rather reliable if it only breaks down about once a year. Fig. 2 clearly demonstrates the value of having a clustered twincomputer system.

![](/api/attachments/DHYWKATZ/fulltext/images/292b533ae1648ca909e09d1c7ba89eb6c4f8b5c658b02b007a62d484627bfe49.jpg)  
Fig. 3. Expected time in the system as a function of MTBF Ž . MTTR<sup>s</sup>10 min .

Fig. 3 portrays a comparison of the expected time in the systems with the same job arrival rate and computer capacity as in Fig. 2. The mean time to repair, however, is reduced to 10 min. Fig. 3 shows that the consolidated single computer system will have a shorter time in the system when the mean time between failures exceeds about 100 days. In contrast to Fig. 2, Fig. 3 has some important managerial implications. Given the parameters experimented within Figs. 2 and 3, it pays off for firms having a consolidated single computer system to reduce the mean time to repair rather than to increase the mean time between failures. When the mean time to repair is 60 min, it does not help the firm with a single computer system to extend the mean time between failures, even to a year. However, reducing MTTR to 10 min has apparent benefits in terms of a shorter expected time in the system than the clustered twin-computer system. Some practices following this suggestion should be beneficial to firms having a consolidated single computer system. For example, adequate backup of mission critical databases may not extend the mean time between failures of computer operations but will contribute to a speedy recovery, thus reducing the mean time to repair.

Both Figs. 4 and 5 plot the expected time in the system of the two configurations under consideration as a function of utilization ratio, , defined as the ratio of arrival rate to the total capacity. The utilization ratio, also termed the traffic intensity, is a typical measure of computer system’s work load. The computer capacity is held at 900 jobs per minute and the mean time between failures is set at six months. The mean times to repair are 60 min and 10 min, respectively in Figs. 4 and 5. When the mean time to repair equals 60 min in Fig. 4, the clustered twin-computer system has a lower expected time in the system for utilization ratios ranging from 0.06 to 0.93. As the mean time to repair is reduced to 10 min, the consolidated single computer system yields a smaller expected time in the system if the utilization ratio falls below 0.66. Figs. 4 and 5 further confirm the benefit of reducing the mean time to repair for firms with a consolidated single computer system.

Figs. 4 and 5 also show that reducing the mean time to repair pays off for both configurations. In this setup, reducing the downtime helps the single system more than the twin cluster. At lower load in terms of lower utilization ratio, the higher performance of the single system takes effect and the single system performs better. As the utilization ratio increases, the effect of system breakdowns increases, resulting in an increased capacity variance and a better performance for the twin cluster. The trade-off between higher performance under low loads in the consolidated single computer system and less capacity variance under the twin cluster system can be summarized as follows. The differences of performance between the consolidated and twin the systems is an increasing function of both utilization ratio and MTTR, and a decreasing function of computer capacity and MTBF.

![](/api/attachments/DHYWKATZ/fulltext/images/9cd1757c9be0c74268b58a5b04847d5eecd0edeec64e264ffc94016b89d475cb.jpg)  
Fig. 4. Expected time in the system as a function of utilization ratio MTTRŽ . <sup>s</sup>60 min .

![](/api/attachments/DHYWKATZ/fulltext/images/8f54632ef7f15bdd8dd3a38b85b4ccc5576cb92fc9ff45d450015fb69b4d0590.jpg)  
Fig. 5. Expected time in the system as a function of utilization ratio MTTRŽ . <sup>s</sup>10 min .

## 4. Optimal pricing and capacity decisions

In this section, the queuing model in Section 2 is embedded in a microeconomic framework to determine the optimal pricing and capacity of the clustered twin-computer system subject to breakdowns. Embedding queuing models in a microeconomic framework to study the role of congestion cost was first developed in Mendelson 8 and later extended<sup>w</sup> <sup>x</sup> by Mendelson and Whang 9 , and Dewan and <sup>w</sup> <sup>x</sup> Mendelson 3 . This section adopts their underlying <sup>w</sup> <sup>x</sup> models to examine the impact of breakdowns on pricing and capacity decisions of the clustered twincomputer system, and compares the results with those of a consolidated single computer system reported in Cheng 2 . In particular, this section fol- <sup>w</sup> <sup>x</sup> lows the notation used in Dewan and Mendelson 3<sup>w</sup> <sup>x</sup> and Cheng 2 .<sup>w</sup> <sup>x</sup>

As before, jobs requiring computer processing have a Poisson arrival rate and arriving jobs have a homogeneous service requirement. However, various jobs are heterogeneous in value. The expected grossŽ . value per unit of time of the computing service to the organization corresponding to the arrival rate  is specified by a value function $V ( \lambda )$ . Hence, $V ^ { \prime } ( \lambda )$ can be interpreted as the marginal value function and the demand function for computing service as well. $V ( \lambda )$ is usually assumed to be increasing, bounded from above, twice continuously differentiable and strictly concave so that $V ^ { \prime } ( \lambda )$ is downward-sloping.

Service times of arriving jobs are assumed to be independently and identically drawn from an exponential distribution with mean $1 / \mu$ according to the First Come First Serve FCFS service discipline. Ž . Each of the twin computers has a processing capacity of $\mu$ jobs per unit of time. Each computer breaks down and repairs independent of each other, and the downtime and uptime follow exponential distributions with parameters  and , respectively.

A job-by-job transfer pricing scheme is considered where each job is charged a fixed fee $p$ for computer processing. When jobs have homogeneous service requirements, job-by-job pricing corresponds to charging users by the actual CPU time each job consumes, a common pricing practice in the industry. While the actual charge may vary in the CPU time-based pricing, both pricing schemes will have the same expected total charge to the users. The job-by-job pricing has a simpler structure that allows users to be aware of the prices before they decide whether to submit jobs. Such a job-by-job pricing scheme has the desired effect of changing customer behavior as suggested in Hall 5 .<sup>w</sup> <sup>x</sup>

To model the opportunity cost from submitting and waiting to getting jobs processed in the clustered twin-computer system, assume that jobs have homogeneous delay costs and that the delay cost per job is a constant Õ per unit of time. This implies that to shorten the turnaround time of each job by one time unit amounts to Õ monetary units gain to the organization. Let $T _ { \mathrm { t c } }$ be the expected time each job spends in the clustered twin-computer system, including the actual processing time of each job and the time spent waiting in the queue. Then, the expected delay cost per job equals $v T _ { \mathrm { t c } }$ and the total expected cost per job is the sum of the service charge $p$ and the expected delay cost $v T _ { \mathrm { t c } }$ . Taking the delay cost into account, equilibrium is achieved when the following relationship is satisfied

$$
V ^ {\prime} (\lambda) = p + v T _ {\mathrm{tc}}.\tag{4.1}
$$

Eq. 4.1 follows the principle of equating the Ž . marginal cost of computing service with its marginal value at the equilibrium.

Let D be the expected overall aggregate delayŽ . cost per unit of time incurred by the computing system as a whole. Then one has

$$
D = \lambda v T _ {\mathrm{tc}}.\tag{4.2}
$$

The objective of the firm is to maximize the expected net value of the computing service. Management is faced with two decision problems, a short-run problem and a long-run problem. The computing capacity $\mu$ is fixed in the short-run problem, while $\mu$ is allowed to change in the long-run problem. This research focuses on the firm’s long-run problem where the price and the capacity have to be jointly determined. After the formulation of the longrun problem for the clustered twin-computer system subject to breakdowns, the results will be compared with findings of a consolidated single computer system subject to the same breakdown characteristics.

## 4.1. Long-run problem $( \mu$ ) is allowed to change

The capacity cost of the computer system becomes part of the decision problem in the firm’s long-run problem. Let the cost rate of the computer system associated with the processing capacity $\mu$ be specified by the function $C ( \mu )$ . The capacity cost function is assumed to be linear as in Dewan and Mendelson 3 , having the form<sup>w</sup> <sup>x</sup>

$$
C (\mu) = B + b _ {1} 2 \mu ,\tag{4.3}
$$

where B represents the fixed overhead and $b _ { 1 }$ is the marginal capacity cost. The marginal capacity cost $b _ { 1 }$ amounts to the cost to expand the computer processing capacity for accommodating one more job per unit of time.

The long-run problem is thus formulated as

$$
\max _ {\lambda , \mu} \left\{V (\lambda) - D (\lambda , \mu) - C (\mu) \right\},\tag{4.4}
$$

where $D ( \lambda , \mu )$ Ž .is defined in 4.2 and $C ( \mu )$ is given in 4.3 .First-order conditions require thatŽ .

$$
V ^ {\prime} (\lambda) = \frac {\partial D}{\partial \lambda},\tag{4.5}
$$

and

$$
C ^ {\prime} (\mu) = - \frac {\partial D}{\partial \mu}.\tag{4.6}
$$

Theorem 4.1 Optimal price of the long-run prob( - ) lem . The optimal internal price, $p ^ { * }$ , for the consolidated single computer system is from Ref. 2<sup>w</sup> <sup>x</sup>

$$
p _ {\mathrm{ss}} ^ {*} = \frac {\gamma + \eta}{\gamma} b _ {1} + \frac {\frac {\lambda_ {\mathrm{ss}} ^ {*} v \eta}{\gamma (\gamma + \eta)}}{\frac {\gamma}{\gamma + \eta} (2 \mu_ {\mathrm{ss}} ^ {*}) - \lambda_ {\mathrm{ss}} ^ {*}}\tag{4.7}
$$

while for the clustered twin-computer system

$$
\begin{array}{l} p _ {\mathrm{tc}} ^ {*} = \frac {\gamma + \eta}{\gamma} b _ {1} + \frac {\frac {\lambda_ {\mathrm{tc}} ^ {*} v \eta}{2 \gamma (\gamma + \eta)}}{\frac {\gamma}{\gamma + \eta} (2 \mu_ {\mathrm{tc}} ^ {*}) - \lambda_ {\mathrm{tc}} ^ {*}} \\ - \frac {\lambda_ {\mathrm{tc}} ^ {*} v \frac {2 \gamma + \eta}{\gamma + \eta}}{(2 \mu_ {\mathrm{tc}} ^ {*} + \lambda_ {\mathrm{tc}} ^ {*}) ^ {2}} \end{array}\tag{4.8}
$$

where the subscripts ss and tc stand for single system and twin cluster, respectively.

## Proof. Please see Appendix D.

The optimal price of the clustered twin-computer system appears to be lower than that of the consolidated single computer system, if the optimal arrival rate and capacity are the same. However, the optimal arrival rates and capacities of these two configurations will be different since the expected time components in the long-run problem 4.4 are different.Ž . The following numerical experiments were conducted to explore and compare the behavior of optimal arrival rates, capacities, and prices of the clustered twin-computer system with those of the consolidated single computer system.

Let the demand function belong to the class of isoelastic demand functions used in Ref. 3 and have<sup>w</sup> <sup>x</sup> the form $V ^ { \prime } ( \lambda ) = A / \lambda ^ { \alpha }$ , where $0 < \alpha \leq 1$ . The corresponding expected gross value function has the form $V ( \lambda ) = A \lambda ^ { 1 - \alpha } / ( 1 - \alpha )$ . The expected gross value function is $V ( \lambda ) = A \ln \lambda$ for the case of unit elasticity $( \alpha = 1 )$ . In the following numerical examples, A equals 100 and $\alpha = 0 . 5$ . Both the clustered and consolidated systems share the same breakdown characteristics as follows. The mean time between failures $( 1 / \eta )$ Ž , MTBF, equals 259 200 min about six months and mean time to repair. $( 1 / \gamma )$ , MTTR, is set at either 10 min or 60 min.

Both the clustered and the consolidated systems have the same marginal capacity cost ${ \left( { b _ { 1 } } \right) }$ which equals 1. The fixed overhead, B, in 4.3 is set toŽ . zero since it will not affect the maximization problem. The long-run problem described in 4.4 isŽ . solved for both the consolidated single computer system and the clustered twin-computer system subject to the same breakdown parameters  and aforementioned. Both the arrival rate and service capacity are in number of jobs per unit of time.

In the figures that follow, clustered twin-computer system results are represented by solid lines, while the consolidated single computer systems are shown in broken lines. Fig. 6 plots the optimal arrival rates as a function of the delay cost, Õ, in dollars per job per unit of time. Two different MTTRs, 10 min and 60 min, were experimented with and shown in the same graph. Fig. 7 shows the optimal capacities of both the clustered twin-computer system and the consolidated single computer system as a function of delay cost.

Optimal Arrival Rates (# of jobs/minute)  
![](/api/attachments/DHYWKATZ/fulltext/images/807bfecedd8226f3f539bac7b7d79c0bafa2d360eaefb990360bab2cfc6fdc53.jpg)  
Fig. 6. Optimal arrival rates versus delay cost MTBF Ž . <sup>s</sup>6 months .

![](/api/attachments/DHYWKATZ/fulltext/images/6a5daf5abf9e76789d7719754eb2023cfd0ef92c3727976f9d792b80dd00ded3.jpg)  
Fig. 7. Optimal capacities versus delay cost MTBF Ž . <sup>s</sup>6 months .

Fig. 6 shows that the clustered twin-computer system will induce a higher optimal arrival rate than the consolidated single computer system for the parameters and demand function specified above. Optimal arrival rate decreases as the delay cost increases in Fig. 6 since a higher delay cost results in a higher total cost to users at the equilibrium described in Ž . Ž . 4.1 . According to 4.1 , a higher total cost will discourage the submission of low value jobs, thus resulting in a lower arrival rate. Given the same delay cost, optimal arrival rates are lower when the mean time to repair, MTTR, is increased from 10 min to 60 min. Again, a higher MTTR will increase the expected time in the system, the T component in Ž . 4.1 , discouraging the submission of low value jobs. Fig. 7 shows the behavior of optimal capacities as the delay cost changes. Fig. 7 exhibits the same pattern as Fig. 6.

Optimal Prices (\$/job)  
![](/api/attachments/DHYWKATZ/fulltext/images/1dca86bbbc113d68e44fbedb10eda6beff66913555bc108adb09777220dd52e5.jpg)  
Fig. 8. Optimal prices versus delay cost MTBF Ž . <sup>s</sup>6 months .

Fig. 8 plots the optimal prices as a function of the delay cost. Recall that clustered twin-computer systems are represented by solid lines, while the consolidated single computer systems are shown in broken lines. We found that optimal prices of the consolidated single computer system are always higher than those of the clustered twin-computer system in our numerical experiments. Optimal prices are higher for a higher delay cost or a higher mean time to repair. This phenomenon holds true for both the consolidated single computer system and the clustered twin-computer system.

Perhaps the most important implication from these series of numerical experiments is due to Fig. 9. In

Maximized Net Value (\$/minute)  
![](/api/attachments/DHYWKATZ/fulltext/images/d866c15da9f1a9315c737f364710e5d93daeeafcfd7a5433be533fc8676087d6.jpg)  
Fig. 9. Maximized net value versus delay cost MTBF Ž . <sup>s</sup>6 months .

Section 3 where the computer capacity is fixed, the consolidated single computer system had a chance to beat the clustered twin-computer system in terms of smaller expected time in the system when the mean time to repair, MTTR, is reduced to 10 min. However in the long-run problem where the optimal arrival rate and computer capacity are to be jointly determined, we found in Fig. 9 that the clustered twin-computer system generated a higher maximized net value of computing to the firm than the consolidated single computer system even when MTTR equals 10 min. Furthermore, it is more desirable to have a clustered twin-computer system if the firm is faced with a high delay cost. This is evidenced by the fact that the net value gap between the clustered twin-computer system and the consolidated single computer system becomes larger as the delay cost increases in Fig. 9.

## 5. Concluding remarks and future research

More and more organizations are running a clustered twin-computer system to tackle the rapidly growing demand of computer capacity. Without considering breakdowns, basic queuing theory suggests that consolidating twin-computer systems to a bigger system with the same overall capacity will result in a lower total time in the system. However, the performance behavior of a consolidated single computer versus a clustered twin computers is less clear when breakdowns are taken into account. One objective of this paper is to analyze the impact of breakdowns on the decision to consolidate or cluster computer systems.

This research finds that both the consolidated single computer system and the clustered twin-computer system, under the same breakdown parameters, have the same effective computer capacity. Although the effective capacity is the same, the variance of capacity induced by breakdowns is higher in the single computer system case than in the clustered twin computers. Since this variance is induced by breakdowns, one should expect that the twin cluster will have better performance when breakdowns are more often in terms of increased MTTR or reduced MTBF. On the other hand, when there are few breakdowns the single computer system has a higher performance under low loads. Hence, there exists a trade-off between higher performance under low loads in the consolidated single computer system Ž . when breakdowns are rare and less capacity variance under the twin cluster system. To gain further insights, numerical experiments were conducted and showed that the clustered twin-computer system has a shorter expected time in the system for most cases. The clustered twin-computer system also performs better when there is a heavy traffic intensity. For firms with a consolidated single computer system, this research finds that it pays off to reduce the mean time to repair than to increase the mean time between failures. For instance, backing up mission critical databases will speed up the recovery process that has the desired effect of reducing mean time to repair.

This paper further incorporates the queuing model in a microeconomic framework to consider effects of the delay cost of computer processing. This paper derives the optimal pricing and capacity of a firm’s clustered twin-computer system that will maximize the net value of computing. Major findings include the following. In general, the clustered twin-computer system will induce a larger optimal arrival rate, computer capacity, and maximized net value of computing, resulting in the need for a lower pricing than that of the consolidated single computer system. For both systems, optimal arrival rate decreases as the delay cost increases since a higher delay cost will discourage the submission of low value jobs. Given the same delay cost, optimal arrival rate is lower when the mean time to repair is increased since an increased mean time to repair adds a higher delay cost to users. The optimal prices follow an opposite direction of the optimal arrival rates. That is, a lower optimal arrival rate induces a higher optimal price and vice versa. Finally, it is found more desirable for the firm to have a clustered twin-computer system when the firm places a high opportunity cost of computing characterized by a high delay cost.

This paper provides useful and timely research results for decision makers as clustering for both large computers and servers becomes popular. Vendors offering clustering technologies include, among others, IBM’s Sysplex, with which users can cluster ES<sup>r</sup>9000s, and Digital Equipment VMSclusters, formally called VAXclusters. Furthermore, computer vendors have begun to deliver clustering capabilities for mid-range computers and local area network servers. For example, complete clustering capabilities for IBM’s AS<sup>r</sup>400 were officially introduced in 1996 12 . On the network servers front, the cluster-<sup>w</sup> <sup>x</sup> ing concept has be implemented in Windows NT servers conforming to the Wolfpack standard developed by Microsoft, DEC, and others. The current NT Server 4.0 Enterprise Edition can cluster only two Windows NT servers together to provide simple failover protection 6 . Apparently, the analytical <sup>w</sup> <sup>x</sup> model and research results of this paper can be directly applied in such an environment. Later releases of Wolfpack are expected to offer the ability to cluster more than two Windows NT servers. Future research will concentrate on analyzing the performance of clustered network servers involving many computers.

## Acknowledgements

The author gratefully acknowledges comments and suggestions of Professors Rajiv Banker and Marshall Freimer, and seminar participants of INSEAD, Purdue University, University of Connecticut, University of Florida, University of Texas at Dallas and University of Washington. The usual disclaimer applies.

## Appendix A

In the single computer case, the effective capacity equals the computer capacity, 2 , multiplied by the ergodic probability that the computer system is up, $\gamma / ( \gamma + \eta )$

For the case of twin computers subject to the same breakdown characteristics, the state transition diagram of such a system is shown in the following.

![](/api/attachments/DHYWKATZ/fulltext/images/94081c2ded66b11f02c7cb6a2e3b4fcabed9790cafcbb23605a9a257e9f875cd.jpg)

Let $p _ { \mathrm { u } } = \mathrm { P r o b } \{ \mathrm { b o t h } $ servers are up ,  4 $p _ { 1 } = \mathrm { P r o b } \{ \mathrm { s e r v e r ~ n o . } $ 4. 1 is up and no. 2 is down , $p _ { 2 } = \mathrm { P r o b } \{ \mathrm { s e r v e r ~ n o } $ . 1 is down and no. 2 is up ,4 $p _ { \mathrm { d } } =$  4 Prob both servers are down . By looking at only the rows of the detailed chain and corresponding balance equations, one has

$$
p _ {\mathrm{u}} = \frac {\gamma^ {2}}{(\gamma + \eta) ^ {2}}, (p _ {1} + p _ {2}) = \frac {2 \gamma \eta}{(\gamma + \eta) ^ {2}}, p _ {\mathrm{d}} = \frac {\eta^ {2}}{(\gamma + \eta) ^ {2}}.\tag{A.1}
$$

Hence the effective capacity of a clustered twin computers subject to breakdowns equals

$$
2 \mu \frac {\gamma^ {2}}{(\gamma + \eta) ^ {2}} + \mu \frac {2 \gamma \eta}{(\gamma + \eta) ^ {2}} = 2 \mu \frac {\gamma}{\gamma + \eta}.\tag{A.2}
$$

Q.E.D.

Appendix B

Recall Eq. A.1 in Appendix A, one can thus combine the two columns in the middle of the state transitionŽ . diagram in Appendix A as the following.

![](/api/attachments/DHYWKATZ/fulltext/images/104ab871a8a52a6f77efd110d2efab7cb9e20c80ff1f388fa2803eb41460c412.jpg)

Define: $p _ { n \mathrm { u } } = \mathrm { P r o b } \{ \mathrm { b o t h } $ servers are up and there are  4n customers in the system ; $p _ { n \mathrm { k } } = \mathrm { P r o b \{ o n l y } $ one server is up and there are n customers in the system ;4 $p _ { n \mathrm { d } } = \mathrm { P r o b } \{ \mathrm { b o t h } $ servers are down and there are n customers in the system . Then, one has the following set of balance equations.4

$$
p _ {0 \mathrm{u}} (\lambda + 2 \eta) = p _ {0 \mathrm{k}} \gamma + p _ {1 \mathrm{u}} \mu\tag{B.1}
$$

$$
p _ {1 \mathrm{u}} (\lambda + \mu + 2 \eta) = p _ {0 \mathrm{u}} \lambda + p _ {1 \mathrm{k}} \gamma + p _ {2 \mathrm{u}} (2 \mu)\tag{B.2}
$$

$$
p _ {n \mathrm{u}} (\lambda + 2 \mu + 2 \eta) = p _ {n - 1, \mathrm{u}} \lambda + p _ {n \mathrm{k}} \gamma + p _ {n + 1, \mathrm{u}} (2 \mu) \quad \text { for } n \geq 2\tag{B.3}
$$

$$
p _ {0 \mathrm{k}} (\lambda + \gamma + \eta) = p _ {0 \mathrm{u}} (2 \eta) + p _ {1 \mathrm{k}} \mu + p _ {0 \mathrm{d}} (2 \gamma)\tag{B.4}
$$

$$
p _ {n \mathrm{k}} (\lambda + \mu + \gamma + \eta) = p _ {n - 1, \mathrm{k}} \lambda + p _ {n \mathrm{u}} (2 \eta) + p _ {n \mathrm{d}} (2 \gamma) + p _ {n + 1, \mathrm{k}} \mu \quad n \geq 1\tag{B.5}
$$

$$
p _ {0 \mathrm{d}} (\lambda + 2 \gamma) = p _ {0 \mathrm{k}} \eta\tag{B.6}
$$

$$
p _ {n \mathrm{d}} (\lambda + 2 \gamma) = p _ {n - 1, \mathrm{d}} \lambda + p _ {n \mathrm{k}} \eta \quad n \geq 1.\tag{B.7}
$$

Define generating functions

$$
\pi_ {\mathrm{u}} (z) = \sum_ {n = 0} ^ {\infty} p _ {n \mathrm{u}} z ^ {n}, \quad \pi_ {\mathrm{k}} (z) = \sum_ {n = 0} ^ {\infty} p _ {n \mathrm{k}} z ^ {n}, \text {   and   } \pi_ {\mathrm{d}} (z) = \sum_ {n = 0} ^ {\infty} p _ {n \mathrm{d}} z ^ {n}.\tag{B.8}
$$

The balance equations B.1 to B.7 lead toŽ . Ž .

$$
\left\{\lambda z ^ {2} - (\lambda + 2 \mu + 2 \eta) z + 2 \mu \right\} \pi_ {\mathrm{u}} (z) + (\gamma z) \pi_ {\mathrm{k}} (z) = \mu z (1 - z) p _ {1 \mathrm{u}} + 2 \mu (1 - z) p _ {0 \mathrm{u}}\tag{B.9}
$$

$$
2 \eta z \pi_ {\mathrm{u}} (z) + \left\{\lambda z ^ {2} - (\lambda + \mu + \gamma + \eta) z + \mu \right\} \pi_ {\mathrm{k}} (z) + 2 \gamma z \pi_ {\mathrm{d}} (z) = \mu (1 - z) p _ {0 \mathrm{k}}\tag{B.10}
$$

$$
\eta \pi_ {\mathrm{k}} (z) + \left\{\lambda z - (\lambda + 2 \gamma) \right\} \pi_ {\mathrm{d}} (z) = 0.\tag{B.11}
$$

After rather lengthy algebra, the above three equations lead to

$$
\pi_ {\mathrm{k}} (z) = \frac {\left\{\left(\lambda + 2 \gamma\right) - \lambda z \right\} \pi_ {\mathrm{d}} (z)}{\eta},\tag{B.12}
$$

$$
\pi_ {\mathrm{u}} (z) = \frac {\mu z (1 - z) p _ {1 \mathrm{u}} + 2 \mu (1 - z) p _ {0 \mathrm{u}}}{\left\{\lambda z ^ {2} - (\lambda + 2 \mu + 2 \eta) z + 2 \mu \right\}} + \frac {\gamma z \left\{\lambda z - (\lambda + 2 \gamma) \right\} \pi_ {\mathrm{d}} (z)}{\eta \left\{\lambda z ^ {2} - (\lambda + 2 \mu + 2 \eta) z + 2 \mu \right\}},\tag{B.13}
$$

and

$$
\pi_ {\mathrm{d}} (z) = \frac {N (z)}{D (z)},\tag{B.14}
$$

where

$$
N (z) = \eta \mu \left\{p _ {0 \mathrm{k}} \left[ \lambda z ^ {2} - (\lambda + 2 \mu + 2 \eta) z + 2 \mu \right] - 2 \eta z \left(z p _ {1 \mathrm{u}} + 2 p _ {0 \mathrm{u}}\right) \right\}\tag{B.15}
$$

$$
D (z) = \left\{\lambda z ^ {2} - (\lambda + \gamma + \mu + \eta) z + \mu \right\} \left\{\lambda^ {2} z ^ {2} - (\lambda^ {2} + 2 \lambda \gamma + 2 \lambda \mu + 2 \lambda \eta) z + (2 \lambda \mu + 4 \gamma \mu) \right\}.\tag{B.16}
$$

The expected number of jobs in a clustered twin-computer system subject to breakdowns equals $\pi _ { \mathrm { u } } ^ { \prime } ( 1 ) +$ $\pi _ { \mathrm { k } } ^ { \prime } ( 1 ) + \pi _ { \mathrm { d } } ^ { \prime } ( 1 )$ as is obvious from the definition of the probability generating functions. According to Little’s law, the expected time in such a clustered twin-computer system is derived by dividing the expected number in the system by the arrival rate of jobs, .

From Eqs. B.12 , B.13 , B.14 , B.15 and B.16 and some algebra, one has the following equations. Ž . Ž . Ž . Ž . Ž .

$$
\begin{array}{l} \pi_ {\mathrm{d}} ^ {\prime} (1) = \frac {\eta^ {2}}{(\gamma + \eta) ^ {2}} \frac {- 2 \lambda \gamma^ {2} - 2 \lambda \eta^ {2} - 4 \lambda \gamma \eta - 8 \lambda \gamma \mu - 4 \lambda \eta \mu + 3 \lambda^ {2} \gamma + 3 \lambda^ {2} \eta + 4 \gamma \mu^ {2}}{\lambda (\gamma + \eta) ^ {2} - 2 \mu (\gamma^ {2} + \gamma \eta)} \\ - \frac {\eta \mu [ (2 \mu - \lambda) p _ {0 k} + 2 \eta p _ {1 u} ]}{2 [ \lambda (\gamma + \eta) ^ {2} - 2 \mu (\gamma^ {2} + \gamma \eta) ]}, \end{array}\tag{B.17}
$$

$$
\pi_ {\mathrm{k}} ^ {\prime} (1) = - \frac {\lambda}{\eta} \frac {\eta^ {2}}{(\gamma + \eta) ^ {2}} + \frac {2 \gamma}{\eta} \pi_ {\mathrm{d}} ^ {\prime} (1),\tag{B.18}
$$

and

$$
\pi_ {\mathrm{u}} ^ {\prime} (1) = \frac {\mu p _ {1 \mathrm{u}} + 2 \mu p _ {0 \mathrm{u}}}{2 \eta} + \frac {\gamma}{2 \eta} \pi_ {\mathrm{k}} ^ {\prime} (1) + \frac {\gamma^ {2} (\lambda - 2 \mu)}{2 \eta (\gamma + \eta) ^ {2}}.\tag{B.19}
$$

Notice that the expected number in the system, $\pi _ { \mathrm { u } } ^ { \prime } ( 1 ) + \pi _ { \mathrm { k } } ^ { \prime } ( 1 ) + \pi _ { \mathrm { d } } ^ { \prime } ( 1 )$ , involves three unknowns: $p _ { \mathrm { 0 u } } , ~ p _ { \mathrm { 0 k } }$ and $p _ { \mathrm { 1 u } }$ . Hence we need three independent equations. The first equation comes from the fact that $\pi _ { \mathrm { d } } ( 1 ) =$ $\eta ^ { 2 } / ( \gamma + \eta ) ^ { 2 }$ and substituting one into Eq. B.14 . The second equation comes from the balance equation B.1 .Ž . Ž . $D ( z )$ Ž . Ž . in Eq. B.16 has a root in the interval 0,1 , denoted by $z _ { 1 }$ . One can easily see that

$$
z _ {1} = \frac {\left(\lambda + \gamma + \mu + \eta\right) - \sqrt {\left(\lambda + \gamma + \mu + \eta\right) ^ {2} - 4 \lambda \mu}}{2 \lambda}.\tag{B.20}
$$

Then $N ( z )$ Ž . in Eq. B.15 must also have this root $z _ { 1 }$ in that the probability generating function $\pi _ { \mathrm { d } } ( z ) =$ $N ( z ) / D ( z )$ Ž .must converge in 0,1 . Then, $N ( z _ { 1 } ) = 0$ constitutes the third needed equation to solve for $p _ { \mathrm { 0 u } } , p _ { \mathrm { 0 k } }$ and $p _ { \mathrm { 1 u } }$ . After some algebra, it follows that

$$
p _ {0 \mathrm{k}} = \frac {\frac {2 \mu \gamma - \lambda (\gamma + \eta)}{\mu (\gamma + \eta)} \left[ 4 \eta \mu z _ {1} + 2 \eta (\lambda + 2 \eta) z _ {1} ^ {2} \right]}{\left\{\left(\lambda^ {2} + 2 \lambda \mu + 4 \lambda \eta + 4 \gamma \eta + 4 \eta^ {2}\right) z _ {1} ^ {2} + \left[ 4 \eta (\mu - \gamma) - (\lambda + 2 \mu + 2 \eta) ^ {2} \right] z _ {1} + 2 \mu (\lambda + 2 \mu + 2 \eta) \right\}},\tag{B.21}
$$

$$
p _ {1 \mathrm{u}} = \frac {\frac {2 \mu \gamma - \lambda (\gamma + \eta)}{\mu (\gamma + \eta)} \left\{\lambda (\lambda + 2 \eta) z _ {1} ^ {2} - [ (\lambda + 2 \eta) (\lambda + 2 \mu + 2 \eta) + 4 \gamma \eta ] z _ {1} + 2 \mu (\lambda + 2 \eta) \right\}}{\left\{\left(\lambda^ {2} + 2 \lambda \mu + 4 \lambda \eta + 4 \gamma \eta + 4 \eta^ {2}\right) z _ {1} ^ {2} + \left[ 4 \eta (\mu - \gamma) - (\lambda + 2 \mu + 2 \eta) ^ {2} \right] z _ {1} + 2 \mu (\lambda + 2 \mu + 2 \eta) \right\}}\tag{B.22}
$$

and

$$
p _ {\mathrm{0u}} = \frac {\gamma p _ {\mathrm{0k}} + \mu p _ {\mathrm{1u}}}{\lambda + 2 \eta}.\tag{B.23}
$$

## Appendix C

Taking advantage of Proposition 2.2, one can see from Eq. B.20 thatŽ .

$$
z _ {1} \cong \frac {(\lambda + \mu) - \sqrt {(\lambda + \mu) ^ {2} - 4 \lambda \mu}}{2 \lambda} = 1
$$

Letting $z _ { 1 } \to 1 , p _ { \mathrm { 0 k } } , p _ { \mathrm { 0 u } }$ , and $p _ { \mathtt { l u } }$ can be very accurately approximated by the following:

$$
p _ {0 \mathrm{k}} = \frac {\eta (2 \mu \gamma - \lambda (\gamma + \eta))}{\mu (\gamma + \eta) ^ {2}},\tag{C.1}
$$

$$
p _ {0 \mathrm{u}} = \frac {(2 \mu \gamma - \lambda (\gamma + \eta)) \gamma}{(\gamma + \eta) ^ {2} (2 \mu + \lambda)},\tag{C.2}
$$

and

$$
p _ {1 \mathrm{u}} = \frac {\lambda \gamma (2 \mu \gamma - \lambda (\gamma + \eta))}{\mu (\gamma + \eta) ^ {2} (2 \mu + \lambda)}.\tag{C.3}
$$

Let E Y<sup>w</sup> <sup>x</sup> be the expected number of jobs in the clustered twin-computer system under consideration. Recall that $E [ Y ] = \pi _ { \mathrm { u } } ^ { \prime } ( 1 ) + \pi _ { \mathrm { k } } ^ { \prime } ( 1 ) + \pi _ { \mathrm { d } } ^ { \prime } ( 1 )$ Ž . Ž . . From Eqs. B.18 and B.19 ,

$$
\pi_ {\mathrm{u}} ^ {\prime} (1) + \pi_ {k} ^ {\prime} (1) = \frac {\mu p _ {1 \mathrm{u}} + 2 \mu p _ {0 \mathrm{u}}}{2 \eta} + \frac {\gamma^ {2} (\lambda - 2 \mu)}{2 \eta (\gamma + \eta) ^ {2}} + \frac {\gamma + 2 \eta}{2 \eta} \pi_ {\mathrm{k}} ^ {\prime} (1).\tag{C.4}
$$

Substituting B.18 into C.4 leads toŽ . Ž .

$$
\pi_ {\mathrm{u}} ^ {\prime} (1) + \pi_ {\mathrm{k}} ^ {\prime} (1) = \frac {\mu p _ {1 \mathrm{u}} + 2 \mu p _ {0 \mathrm{u}}}{2 \eta} + \frac {\gamma^ {2} (\lambda - 2 \mu)}{2 \eta (\gamma + \eta) ^ {2}} - \frac {\lambda (\gamma + 2 \eta)}{2 (\gamma + \eta) ^ {2}} + \frac {\gamma (\gamma + 2 \eta)}{\eta^ {2}} \pi_ {\mathrm{d}} ^ {\prime} (1).\tag{C.5}
$$

Hence,

$$
E [ Y ] = \pi_ {\mathrm{u}} ^ {\prime} (1) + \pi_ {\mathrm{k}} ^ {\prime} (1) + \pi_ {\mathrm{d}} ^ {\prime} (1) = \frac {\mu p _ {1 \mathrm{u}} + 2 \mu p _ {0 \mathrm{u}}}{2 \eta} + \frac {\gamma^ {2} (\lambda - 2 \mu)}{2 \eta (\gamma + \eta) ^ {2}} - \frac {\lambda (\gamma + 2 \eta)}{2 (\gamma + \eta) ^ {2}} + \frac {(\gamma + \eta) ^ {2}}{\eta^ {2}} \pi_ {\mathrm{d}} ^ {\prime} (1).\tag{C.6}
$$

Ž .By Eq. C.1 and noting the fact that $\pi _ { \mathrm { d } } ( 1 ) = \eta ^ { 2 } / ( \gamma + \eta ) ^ { 2 }$ , the first term in C.6 can be simplified as follows. Ž .

$$
\frac {\mu p _ {1 \mathrm{u}} + 2 \mu p _ {0 \mathrm{u}}}{2 \eta} = \frac {\mu}{2 \eta} \left(\frac {2 \mu \gamma - \lambda (\gamma + \eta)}{\mu (\gamma + \eta)} - \frac {\eta (2 \mu \gamma - \lambda (\gamma + \eta))}{\mu (\gamma + \eta) ^ {2}}\right) = \frac {\gamma (2 \mu \gamma - \lambda (\gamma + \eta))}{2 \eta (\gamma + \eta) ^ {2}}.\tag{C.7}
$$

Substituting C.7 into C.6 leads toŽ . Ž .

$$
E [ Y ] = \frac {(\gamma + \eta) ^ {2}}{\eta^ {2}} \pi_ {\mathrm{d}} ^ {\prime} (1) - \frac {\lambda}{\gamma + \eta}.\tag{C.8}
$$

From Eqs. B.17 , C.1 and C.3 , one has after some algebra Ž . Ž . Ž .

$$
\frac {(\gamma + \eta) ^ {2}}{\eta^ {2}} \pi_ {\mathrm{d}} ^ {\prime} (1) = \frac {2 \lambda + \frac {\lambda \mu (4 \gamma + 2 \eta)}{(\gamma + \eta) ^ {2}} - \frac {2 \lambda^ {2}}{\gamma + \eta}}{2 \left(\frac {\gamma}{\gamma + \eta} 2 \mu - \lambda\right)} + \frac {\lambda \gamma}{(2 \mu + \lambda) (\gamma + \eta)}.\tag{C.9}
$$

Substituting C.9 into C.8 , it follows that Ž . Ž .

$$
E [ Y ] = \frac {\lambda + \frac {\lambda \eta \mu}{(\gamma + \eta) ^ {2}}}{\left(\frac {\gamma}{\gamma + \eta} 2 \mu - \lambda\right)} + \frac {\lambda \gamma}{(2 \mu + \lambda) (\gamma + \eta)}.\tag{C.10}
$$

According to Little’s law, the expected time in such a clustered twin-computer system equals $E [ Y ]$ divided by the arrival rate, . Hence,

$$
T _ {\mathrm{tc}} (\lambda , \mu , \gamma , \eta) = \frac {1 + \frac {\eta \mu}{(\gamma + \eta) ^ {2}}}{\frac {\gamma}{\gamma + \eta} 2 \mu - \lambda} + \frac {\frac {\gamma}{\gamma + \eta}}{2 \mu + \lambda}.\tag{C.11}
$$

Q.E.D.

Appendix D

From Eqs. 4.1 , 4.2 and 4.5 , it follows thatŽ . Ž . Ž .

$$
p * = \lambda * v \frac {\partial T _ {\mathrm{tc}}}{\partial \lambda}.\tag{D.1}
$$

From Theorem 2.3 and after some algebra, one has

$$
\frac {\partial T _ {\mathrm{tc}}}{\partial \mu} = \frac {\frac {\eta}{(\gamma + \eta) ^ {2}}}{\frac {\gamma}{\gamma + \eta} 2 \mu - \lambda} - \frac {2 \gamma}{\gamma + \eta} \left\{\frac {\partial T (\lambda , \mu)}{\partial \lambda} + \frac {\frac {2 \gamma + \eta}{\gamma + \eta}}{(2 \mu + \lambda) ^ {2}} \right\}.\tag{D.2}
$$

Multiplying both sides of D.2 byŽ . Ž . Ž . Ž . Õ, and applying Eqs. D.1 , 4.3 and 4.6 leads to

$$
- 2 b _ {1} = \frac {\frac {\lambda v \eta}{(\gamma + \eta) ^ {2}}}{\frac {\gamma}{\gamma + \eta} 2 \mu - \lambda} - \frac {2 \gamma}{\gamma + \eta} \left(p + \frac {\lambda v \frac {2 \gamma + \eta}{\gamma + \eta}}{(2 \mu + \lambda) ^ {2}}\right).\tag{D.3}
$$

Hence,

$$
p ^ {*} = \frac {\gamma + \eta}{\gamma} b _ {1} + \frac {\frac {\lambda^ {*} v \eta}{2 \gamma (\gamma + \eta)}}{\frac {\gamma}{\gamma + \eta} 2 \mu^ {*} - \lambda^ {*}} - \frac {\lambda^ {*} v \frac {2 \gamma + \eta}{\gamma + \eta}}{(2 \mu^ {*} + \lambda^ {*}) ^ {2}}.\tag{D.4}
$$

Q.E.D.

## References

<sup>w</sup> <sup>x</sup> 1 M. Ballou, Survey pegs computer downtime costs at \$4 billion, Computerworld August 10, 1992 53–56.Ž .

<sup>w</sup> <sup>x</sup> 2 H.K. Cheng, Optimal internal pricing and backup capacity of computer systems subject to breakdowns, Decision Support Systems 19 2 1997 93–108.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 S. Dewan, H. Mendelson, User delay costs and internal pricing for a service facility, Management Science 36 12Ž . Ž .1990 1502–1517.

<sup>w</sup> <sup>x</sup> 4 F.V. Guterl, Twin mainframes power Lufthansa’s reservations, Datamation October 1, 1992 95–96.Ž .

<sup>w</sup> <sup>x</sup> 5 R.W. Hall, Queuing Methods for Services and Manufacturing, Prentice-Hall, 1991, pp. 289–290.

<sup>w</sup> <sup>x</sup> 6 G.M. Hayes, Next time is now? Computerworld January 26,Ž 1998 ..

<sup>w</sup> <sup>x</sup> 7 K.C. Laudon, J.P. Laudon, Management Information Systems: Organization and Technology, Macmillan, 1994, pp. 30–31.

<sup>w</sup> <sup>x</sup> 8 H. Mendelson, Pricing computer services: queuing effects, Communications of the ACM 28 3 1985 312–321.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 H. Mendelson, S. Whang, Optimal incentive-compatible priority pricing for the M<sup>r</sup>M<sup>r</sup>1 queue, Operations Research 38 Ž . Ž . 2 1990 870–883.

<sup>w</sup> <sup>x</sup> 10 I.L. Mitrany, B. Avi-Itzhak, A many-server queue with service interruptions, Operations Research 16 1968 628–638.Ž .

<sup>w</sup> <sup>x</sup> 11 D. Simpson, Can’t tolerate SERVER downtime? Cluster ’em! Datamation August 15, 1995 45–47.Ž .

<sup>w</sup> <sup>x</sup> 12 D. Simpson, Cluster AS<sup>r</sup>400? Datamation http:Ž <sup>rr</sup>www. datamation.com<sup>r</sup>PlugIn<sup>r</sup>1996<sup>r</sup>feb15<sup>r</sup>02binfc1.html ..

<sup>w</sup> <sup>x</sup> 13 D. Simpson, Shoot this server, Datamation http:Ž <sup>rr</sup>www. datamation.com<sup>r</sup>PlugIn<sup>r</sup>1997<sup>r</sup>june<sup>r</sup>observ.html ..

Dr. Hsing Kenneth Cheng is currently with Department of Decision and Information Sciences of The University of Florida. He received his PhD from William E. Simon Graduate School of Business Administration, The University of Rochester. His research interests focus on electronic commerce, computer clustering technology, and how to optimally price computer software. His work has appeared in Computers and Operations Research, Decision Support Systems, European Journal of Operational Research, IEICE Transactions, Journal of Business Ethics, Journal of Management Information Systems, and Socio-Economic Planning Sciences.
