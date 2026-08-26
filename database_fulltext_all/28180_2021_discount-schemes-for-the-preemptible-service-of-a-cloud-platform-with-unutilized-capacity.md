---
otero_id: 28180
otero_key: "JC7XVMAY"
title: "Discount Schemes for the Preemptible Service of a Cloud Platform with Unutilized Capacity"
authors: "Shi Chen; Kamran Moinzadeh; Yong Tan"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Discount Schemes for the Preemptible Service of a Cloud Platform with Unutilized Capacity

Shi Chen,<sup>a</sup> Kamran Moinzadeh,<sup>a</sup> Yong Tan<sup>a</sup>

<sup>a</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195

Contact: shichen@uw.edu, https://orcid.org/0000-0001-8413-0870 (SC); kamran@uw.edu, https://orcid.org/0000-0001-8527-6089 (KM); ytan@uw.edu, https://orcid.org/0000-0001-8087-3423 (YT)

Received: Revised: August 28, 2020; December 6, 2020 Accepted: <sup>January 3, 2021</sup>Published Online in Articles in Advance: May 24,2021

https://doi.org/10.1287/isre.2021.1011

Copyright:

Abstract. Rapid growth in the cloud services market provides tremendous opportunities to cloud providers who have invested heavily in computing capacities but also has led, at time, to low utilization of capacities. To alleviate this problem, some providers have launched a low-priority service with preemptible (spot) instances, which allows them to attract more customers while keeping the right to reclaim capacities when necessary. In this study, we consider a provider who faces a heterogeneous pool of customers with fault-tolerant (interruptible) computing jobs. We develop an analytical framework that consists of a customer-choice model and a diffusion model to capture the underlying supply-demand dynamics and the resulting preemption probability. First, we examine a commonly used discount scheme for preemptible instances, namely, the uniform discount scheme, and derive the optimal discounted price, given customers’ expectation of the preemption probability. Then, we propose another practical discount scheme, namely, the interruption-based discount scheme, which provides customers with compensation for interruptions. As long as the provider interrupts the preemptible instances randomly and customers are risk neutral, the two discount schemes are equivalent from the provider’s perspective. That said, the proposed scheme is fairer than the uniform discount scheme from the customers’ perspective, as the former provides more discounts to customers who experience more interruptions. Finally, in the presence of risk-averse customers, through a numerical study, we <sup>fi</sup>nd that the provider would be better off by adopting the uniform discount scheme in an environment in which the level of surplus capacity stays high and stable. Overall, however, the provider would be better off by adopting the proposed scheme when the level of the surplus capacity is moderate and volatile; the relative advantage of the proposed scheme enlarges as the average surplus capacity decreases and its volatility increases.

History: D. J. Wu, Senior Editor; Zhengrui Jiang, Associate Editor. Funding: This work was supported in part by the National Natural Science Foundation of China [Grants 71729001 and 7207011075]. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2021.1011.

Keywords: discount schemes <sub>•</sub> pricing of capacity <sub>•</sub> preemptible instance <sub>•</sub> cloud computing

## 1. Introduction

The proliferation of information technology (IT) technologies over the last decade has dramatically changed the business world. In particular, cloud computing provides the basis for most of the recent technological advancements including arti<sup>fi</sup>cial intelligence, block chains, and the Internet of Things (Song 2018). A survey by Oxford Economics and SAP (2014) revealed that 69% of companies had planned to migrate their critical business functions to cloud platforms. As a result, cloud services have emerged as a signi<sup>fi</sup>cant marketplace with great potential for growth. According to Gartner Newroom (2018), the revenue of the public cloud services market is expected to reach \$278.3 billion in 2021.

The tremendous opportunities posed by the public cloud services market, however, presents challenges to the cloud service providers regarding pricing and management of computing capacity. Kepes (2015) reported that, on average, approximately 30% of the capacity in the global data centers was underused. The low utilization of the computing resources arises from a con<sup>fl</sup>ict between the rather static capacity of computing resources (because of long lead times when expanding capacity) and the highly volatile day-to-day demand for these resources. Currently, almost all major public cloud providers promise a higher than 99% service level for most customers, which requires the cloud providers to hold excessive surplus capacities to meet occasional demand surges.

To take advantage of their surplus capacities without violating the written service level agreements (SLAs), some leading cloud providers, including Amazon Web Services (AWS), Microsoft Azure (MS Azure), and Google Cloud Platforms (GCP), have launched a relatively new type of service, namely, the low-priority (preemptible) service. Examples of low-priority service include the spot instances at AWS, the low-priority (spot) virtual machines at MS Azure, and the preemptible instances at GCP. Because low-priority services are not covered by providers’ SLAs, the providers can reclaim capacities from low-priority users when necessary, and these users’ computing jobs will be preempted. In practice, preemptions are determined primarily by the providers’ need to balance demand with supply, as exempli-<sup>fi</sup>ed in the following statements:

MS Azure: “Low-priority VMs [virtual machines] enable you to take advantage of our unutilized capacity … . Azure will allocate the VMs if there is capacity available, but there are no SLA guarantees. At any point in time when Azure needs the capacity back, we will evict lowpriority VMs.”<sup>1</sup>

GCP: “A preemptible VM is an instance that you can create and run at a much lower price than normal instances. However, Compute Engine might terminate (preempt) these instances if it requires access to those resources for other tasks. Preemptible instances are excess Compute Engine capacity, so their availability varies with usage.”<sup>2</sup>

Motivated by these practices, we aim to analyze a cloud provider’s discount pricing strategy for low-priority service in the face of varying supply-and-demand dynamics. We begin with an overview of different pricing schemes employed in the public cloud market and then discuss the focus of this study. Cloud providers offer a variety of con<sup>fi</sup>gurations of virtual machines, namely, machine types or instances, for customers to choose. For each instance, the providers offer different types of services, including committed service (e.g., reserved instance), regular service (e.g., ondemand instance), and low-priority service (e.g., preemptible instance). The mainstream service is regular service, also known as a pay-as-you-go type of service, which is charged at a <sup>fi</sup>xed regular price (e.g., an hourly rate) for each machine type. Apart from regular service, customers can take advantage of a reservation discount if they can commit to sustained usage of a virtual machine. A typical reservation contract requires at least one year of sustained usage. Moreover, as noted previously, some customers, whose computing jobs can be interrupted by the providers, can take advantage of a discount in exchange for the risk of preemptions. For example, at GCP, a preemptible instance can be up to 80% less expensive than an on-demand instance.<sup>3</sup> We also note that committed and regular services are covered by the providers’ SLA, whereas the low-priority service is not.

It is beyond the scope of one study to examine various pricing schemes for all three types of services. In this paper, we focus on the speci<sup>fi</sup>c segment of customers with fault-tolerant (interruptible) jobs, which can withstand preemptions. According to MS Azure, faulttolerant jobs are “<sup>fl</sup>exible workloads, like large processing jobs, dev/test environments, demos, and proofs of concept”.<sup>4</sup> We note that, because of the <sup>fl</sup>exible nature of their workloads, customers with fault-tolerant jobs do not need to consider the committed service, which requires customers to enter a long-term contract with the provider. Such customers can, however, choose between regular and low-priority services. Their choices depend on the tradeoff between cost savings and inconvenience (i.e., interruption and delay) of using a preemptible instance compared with an on-demand instance. The low-priority service attracts new customers and thus provides a new revenue stream to the service provider; however, its adoption by a portion of existing customers who use the more lucrative on-demand instances will generate less revenue for the provider. We refer to the former as a marketing campaign effect and the latter as a cannibalization effect. Given these tradeoffs, it is important for the provider to understand the market environment and to determine whether it is economically appealing to launch the low-priority service and, if so, how to optimize the pricing decisions to maximize the expected revenue.

In this paper, we focus on a commonly used discount scheme for low-priority service as a baseline for this study, which sets a <sup>fi</sup>xed hourly discount rate to all customers who use a preemptible instance. We refer to this scheme as a uniform discount scheme. In the cloud industry, apart from a uniform discount scheme, a dynamic spot-pricing scheme also has been used by AWS, whereby bids are submitted for an instance by customers, similar to auctions. Although spot-pricing is an attractive scheme and of great interest to the academic community, as it is perceived as representing the supply-demand dynamics in the market, it has its own de<sup>fi</sup>ciencies. First, from a practical point of view, a uniform discount scheme is much more transparent, predictable, and easier to communicate between the provider and the customers compared with a spot-pricing scheme. Indeed, GCP advocates the simplicity of its uniform discount scheme as a distinct advantage: “pricing is <sup>fi</sup>xed so you will always get low cost and <sup>fi</sup>nancial predictability, without taking the risk of gambling on variable market pricing.”<sup>5</sup> Second, although AWS appears to use a spot-pricing scheme, empirical evidence has shown that the spot prices at AWS are likely to be generated from a predetermined and <sup>fi</sup>xed set of prices rather than representing the underlying supply-demand dynamics of the spot-instance market (Agmon Ben-Yehuda et al. 2013). Thus, we argue that a uniform discount scheme and the one proposed in this paper deserve consideration. Moreover, modeling the supply-demand dynamics in the preemptible (spot) market segment is intriguingly challenging and is one of the distinct features of this study. Here we provide a preview of the main contributions of this study.

Our study makes several contributions. First, we provide an analytical framework to examine discount schemes for low-priority service in the cloud. Our framework consists of two critical elements: (1) a customer choice model that captures the customers’ tradeoff when choosing between an on-demand and a preemptible instance; and (2) a diffusion model developed from a notion of the buffered stochastic <sup>fl</sup>ow (Harrison 2013) that captures the underlying supply-demand dynamics and the resulting preemption probability. Second, we examine the optimal discount rate under a uniform discount scheme whereby all customers have the same expectation of the preemption probability. We analyze the equilibrium outcome when the customers’ rational expectation of the preemption probability is in line with the average preemption probability that results from the underlying supply-demand dynamics. Third, we propose an alternative discount scheme, namely, the interruptionbased scheme, which provides compensation to customers for each interruption (preemption). Similar to the uniform discount scheme, the interruption-based scheme is practical and easy to communicate. Furthermore, this proposed discount scheme is fairer than a uniform discount scheme from the customers’ perspective, because the proposed scheme provides more compensation toward customers who are interrupted more often. We also identify conditions in which the proposed scheme outperforms the uniform discount scheme. We believe that our proposed scheme <sup>fi</sup>lls the gap between the simple uniform discount scheme and the more sophisticated yet opaque spot-pricing scheme.

The remainder of this paper is organized as follows. In the next section, we discuss the related literature. We introduce the model in Section 3, followed by analysis of our base model under certain assumptions in Section 4. In Section 5, we relax those assumptions and provide a comprehensive numerical study. We conclude this paper by presenting the managerial implications and pointing out future research directions in Section 6.

## 2. Literature Review

This study is related to two bodies of literature: (1) pricing and revenue management and (2) applications of operations management to the cloud industry. The literature on pricing and revenue management is abundant, and Talluri and Van Ryzin (2006) and Ozer<sup>¨</sup> and Phillips (2012) provided excellent reviews of the theoretical models. In particular, a stream of research on service systems faced by delay-sensitive customers is relevant to our study. As one of the initial works in this stream of research, Mendelson and Whang (1990) examined the optimal pricing policy that maximizes the social welfare of a queueing system. Other studies also considered maximizing the revenue of the provider, including those of Lederer and Li (1997), Maglaras and Zeevi (2005), and Afeche (\` 2013). See also Hassin and Haviv (2003) and Deng et al. (2015) for a survey of this stream of research.

Our paper has three features that, taken together, make this study distinct from the previously noted studies. (1) Demands for regular and low-priority services are substitutable. (2) Market heterogeneity consists of two dimensions: the customers’ willingness-to-pay and sensitivity-to-delay, each of which takes a value along a continuum and re<sup>fl</sup>ects the diversi<sup>fi</sup>ed customer computational needs in the cloud. (3) The underlying supply-demand dynamics are captured by a diffusion model developed from a notion of the buffered stochastic flow (Harrison 2013) (see Heyman and Sobel 1982 and Harrison 2013 for the treatment of the diffusion process).

Furthermore, there has been a growing research interest in the pricing strategies of the cloud industry in the last decade. Samimi and Patel (2011) provided a review of various pricing models in the cloud. More recently, Li and Kumar (2018) investigated competitive strategies of an incumbent provider and an entrant provider, whereby a subscription-based pricing scheme is used. Yuan et al. (2018) focused on a cloud provider’s SLA-based price-penalty scheme and derived an effective search algorithm to determine the optimal provision of backup resources to minimize the total provision and penalty costs. Chen et al. (2019) analyzed two pricing schemes for a provider’s committed service; one is similar to GCP’s sustained usage discount scheme, and the other is similar to the reservation discount scheme of AWS and MS Azure. The authors found that customers with relatively high (low) use volatility would prefer the former (latter). Please see Joe-Wong and Sen (2018) and the references therein for additional studies of customer fairness and cloud neutrality under providers’ various pricing and capacity management strategies.

A number of studies have focused on auction-based spot-pricing schemes motivated by AWS spot instances, including those of Xu and Li (2013), Kilcioglu and Maglaras (2015), Zheng et al. (2015), Cheng et al. (2016), Toosi et al. (2016), Dierks and Seuken (2021), and Gao et al. (2019). Gao et al. (2019) examined competition between a <sup>fi</sup>rm that uses an auction-based pricing model and another <sup>fi</sup>rm that uses a <sup>fi</sup>xedprice model, which resembles competition between AWS and GCP in the preemptible (spot) instance segment. We also note that there is a debate over the practicability of the mechanisms proposed in the previous studies and call for studies of simpler but more practical pricing schemes (Li et al. 2016). By proposing a practical interruption-based scheme, our study addresses the large gap between the uniform discount scheme offered by GCP and the spot-pricing scheme adopted by AWS, which represent the two extremes of the spectrum.

Our research is also related to the literature on quality differentiation and its impact on a <sup>fi</sup>rm’s product line design. Jones and Mendelson (2011) provided a summary of the main features of earlier work on this topic. Quality differentiation also has been studied in other contexts, including customer codesign (Basu and Bhaskaran 2018), probabilistic selling (Zhang et al. 2015), and pricing and bundling strategies for information goods (Ma and Seidmann 2015, Chen and Huang 2016, Mehta et al. 2019). A well-known result of such research is the concept of damaged goods (Deneckere and McAfee 1996), whereby <sup>fi</sup>rms may degrade the quality of their low-end product to mitigate a cannibalization effect. In contrast, our study considers low-priority service in the cloud, whereby preemptions occur because of the supply-demand dynamics rather than the provider’s purposeful manipulation, as shown in the statements from MS Azure and GCP in Section 1.

## 3. Model Setup

In this study, we consider a cloud provider (he) and focus on a market segment in which customers’ computing jobs can be interrupted by the provider, namely, the fault-tolerant jobs. When submitting a job, such a customer (she) can choose between the regular service (e.g., on-demand instance) and the low-priority service (e.g., preemptible instance) offered by the provider. In the former, the customer receives continuous service and pays a regular price, whereas, in the latter, she pays less in exchange for the risk of interruptions. As noted in the Introduction, there is another market segment in which the customers’ computing jobs cannot be interrupted, namely, the fault-intolerant (noninterruptible) jobs. Such computing jobs, however, cannot be completed by using a preemptible instance. Thus, our study does not include in the model the behavior of a customer who has fault-intolerant jobs. Instead, we assume that the aggregate demand of fault-intolerant jobs follows a stochastic process. The volatility of such a stochastic process is a primary source of the volatility in the provider’s surplus capacity that can be used to meet demand from the focal segment of fault-tolerant jobs.

Next, we discuss two distinct features of our analytical model: the supply-demand dynamics of the system and the asymmetric information about the preemption probability. First, as fault-tolerant jobs continually arrive, they create new demand for the preemptible instances, whereas completed jobs leave the system. When the total demand exceeds the available capacity, some (but not necessarily all) preemptible instances will be interrupted. Because there is little information about the preemption rules used by the cloud providers in practice, customers would expect that all preemptible instances face the same probability of interruptions. Second, because of the lack of information, most customers do not have the sophisticated knowledge they need in regard to the real-time preemption probability of a cloud platform. That said, customers may have a reasonable common belief about the average preemption probability of the cloud platform. For instance, the average probability can be estimated based on detailed observations of the frequency of preemptions, which can be done by a third party, such as a cloud services consulting company. Moreover, the cloud provider also can reveal useful information about the historical average preemption frequency to help customers to form a reasonable common belief. In this regard, GCP states, “For reference, we’ve observed from historical data that the average preemption rate varies between 5% and 15% per day per project, on a seven-day average, occasionally spiking higher depending on time and zone.”<sup>6</sup> Accordingly, potential users of the preemptible instances at GCP can make a sound decision based on the information about the average preemption probability. Therefore, in this study, we assume that customers can form a sensible common belief about the average preemption probability, although they do not possess the more sophisticated knowledge about the dynamic preemption probability in real time.

Notably, there is an important interplay between the provider’s pricing strategy and the system’s preemption probability. For example, if the provider decides to offer a deeper discount for employment of a preemptible instance, it attracts not only new customers who could not previously afford to pay the higher price but also some existing customers who previously used an on-demand instance. To characterize the supply-demand dynamics of the system, it is imperative to analyze a customer’s tradeoff between the cost savings and the risk of interruptions by using a preemptible instance. In Section 3.1, we develop a customer-choice model, which provides the aggregate demand for preemptible instances. Then, in Section 3.2, we develop a model of the supply-demand dynamics and the resulting average preemption probability. Table 1 provides a summary of notations.

We start with the basics of our model. On the demand side, we focus on the market segment of customers with fault-tolerant jobs. We assume that arrivals of such customers follow a Poisson process with rate λ. Each customer brings a fault-tolerant job, and the random workloads of these jobs, in terms of time units to complete, are independent and identically distributed (i.i.d.) with mean $\mu$ and standard deviation σ. A customer with a fault-tolerant job has three options: an on-demand instance, a preemptible instance, or to walk away $( \mathrm { e . g . }$ , turn to another provider or on-premises computing resources). Let $m _ { o } \in [ 0 , 1 ]$ or $m _ { p } \in [ 0 , 1 ]$ be the portion of the fault-tolerant jobs for which an on-demand or a preemptible instance is requested, respectively, and note that $0 \leq m _ { o } + m _ { p } \leq 1$ Thus, the total (cumulative) workload of the fault-tolerant jobs in 0, t , D(t), follows a compound Poisson process with arrival rate $( m _ { o } + m _ { p } ) \lambda$ and i.i.d job workloads with mean $\mu$ and standard deviation σ.

Table 1. Summary of Notations

<table><tr><td>Notation</td><td>Explanation</td></tr><tr><td> $\lambda$ </td><td>Mean arrival rate of the fault-tolerant (interruptible) jobs</td></tr><tr><td> $\mu$ </td><td>Mean of the fault-tolerant job workloads measured in terms of time units</td></tr><tr><td> $\sigma$ </td><td>Standard deviation of the fault-tolerant job workloads measured in terms of time units</td></tr><tr><td> $m_o$ </td><td>Portion of the fault-tolerant jobs for which an on-demand instance is requested</td></tr><tr><td> $m_p$ </td><td>Portion of the fault-tolerant jobs for which a preemptible instance is requested</td></tr><tr><td> $M_0\lambda$ </td><td>Mean arrival rate of the fault-intolerant (noninterruptible) jobs</td></tr><tr><td> $\mu_0$ </td><td>Mean of the fault-intolerant job workloads measured in terms of time units</td></tr><tr><td> $\sigma_0$ </td><td>Standard deviation of the fault-intolerant job workloads measured in terms of time units</td></tr><tr><td>K</td><td>Total capacity of instances; K = k $\lambda$ </td></tr><tr><td>D(t)</td><td>Total workload of the fault-tolerant jobs in [0,t]</td></tr><tr><td>D0(t)</td><td>Total workload of the fault-intolerant jobs in [0,t]</td></tr><tr><td>S(t)</td><td>Total surplus capacity in [0,t]; S(t) = Kt - D0(t)</td></tr><tr><td> $\delta$ </td><td>Length of one time unit; let  $\delta$  = 1 without loss of generality</td></tr><tr><td>I</td><td>Random number of interruptions that a preemptible instance encounters</td></tr><tr><td>w</td><td>Regular price for an on-demand instance</td></tr><tr><td> $\beta w$ </td><td>Discounted price under the uniform discount scheme;  $\beta \in [0,1]$ </td></tr><tr><td> $\alpha$ </td><td>Compensation rate under the interruption-based discount scheme;  $\alpha \geq 0$ </td></tr><tr><td>v</td><td>Customer&#x27;s willingness-to-pay with a marginal CDF H(·)</td></tr><tr><td>a</td><td>Customer&#x27;s sensitivity-to-delay with a marginal CDF G(·)</td></tr><tr><td>p</td><td>Customer&#x27;s belief about the average preemption probability</td></tr><tr><td>Uo(v,a)</td><td>Customer&#x27;s expected utility of completing a unit job using an on-demand instance</td></tr><tr><td>Up(v,a)</td><td>Customer&#x27;s expected utility of completing a unit job using a preemptible instance</td></tr><tr><td> $\Pi^{UD}(p,\beta)$ </td><td>Provider&#x27;s expected revenue under the uniform discount scheme for any p and  $\beta$ </td></tr><tr><td> $\Pi^{IB}(p,\alpha)$ </td><td>Provider&#x27;s expected revenue under the interruption-based discount scheme for any p and  $\alpha$ </td></tr></table>

On the supply side, we note that only the surplus capacity after satisfying the demand from the fault-intolerant (noninterruptible) jobs can be utilized to serve the fault-tolerant (interruptible) jobs. Let $K = k \lambda$ be the provider’s total capacity of instances and $D _ { 0 } ( t )$ be the total (cumulative) workload for fault-intolerant jobs in 0, t . We assume that $D _ { 0 } ( t )$ follows a compound Poisson with mean arrival rate $\lambda _ { 0 } = M _ { 0 } \lambda$ and i.i.d job workloads with mean $\mu _ { 0 }$ and standard deviation $\sigma _ { 0 } .$ Then, the total surplus capacity that can be used for the fault-tolerant jobs in 0, t , S(t), is random. As can be seen, the volatility of demand for fault-intolerant jobs is a primary source for the volatility of the surplus capacity that can be utilized for fault-tolerant jobs. Because, in reality, the provider has plenty of surplus capacity, on average, we assume that the total capacity, $K = k \lambda$ , is much larger than the average workload per time unit brought by fault-intolerant jobs, $M _ { 0 } \mu _ { 0 } \lambda$

## 3.1. Model of Customer Choice

We now focus on the market segment of customers with fault-tolerant (interruptible) jobs. Let v be a customer’s willingness-to-pay per time unit and p be the customer’s belief about the average preemption probability on the cloud platform. If the customer chooses an on-demand instance, she can <sup>fi</sup>nish the job without any delay; however, if the customer chooses a preemptible instance, her job may be interrupted and the delay caused by the interruptions reduces the customer’s utility. We assume that the reduction in the customer’s expected utility is equal to the average delay multiplied by the customer’s sensitivity-to-delay, denoted by parameter a. We consider a market in which customers differ in their willingness-to-pay and sensitivity-to-delay. In general, let $( v , a )$ follow a joint cumulative distribution function (CDF) $F ( v , a )$ . Furthermore, let H(v) and G(a) denote the CDF of the customer’s willingness-to-pay, v, and her sensitivityto-delay, a, respectively.

In our base model, we consider that the customers are risk neutral and aim to maximize their expected utility. In Section $5 ,$ we extend the base model to riskaverse customers. To de<sup>fi</sup>ne the customers’ expected utility, we consider a unit $j o b$ as one that takes one time unit to complete $( \mathrm { i . e . }$ , the workload of the unit job is one), as, in general, a fault-tolerant job with an arbitrary workload can be viewed as consisting of multiple unit jobs. Moreover, let w be the price of an on-demand instance and βw $( \beta \in [ 0 , 1 ] )$ be the discounted price of a preemptible instance per time unit. For a customer endowed with v and $a ,$ the expected utility of completing a unit job with an on-demand instance, $U _ { o } ( v , a ) _ { \cdot }$ , or a preemptible instance, $U _ { p } ( v , a )$ , is given as follows:

$$
U _ {o} (v, a) = v - w, U _ {p} (v, a) = \left(v - \frac {a p}{1 - p}\right) - \beta w.\tag{1}
$$

If the customer chooses an on-demand instance, she pays the provider w and <sup>fi</sup>nishes the unit job in one time unit. In contrast, if the customer chooses a preemptible instance, her completion of the job can be interrupted and delayed. As noted earlier, the customer knows neither the real-time preemption probability nor the provider’s rule of preemption. Indeed, the customer’s estimate of the expected delay, at best, can be approximated by using her limited knowledge about the platform’s average preemption probability p. Thus, we assume that, from the customer’s perspective, the expected delay of a unit job is approximately $p / ( 1 - p )$ which is the mean of a geometric distribution with success (noninterruption) probability $1 - p$ . The customer pays the provider βw for the one-time unit needed to complete the unit job regardless of whether the job is delayed, as the customer will be charged only when the instance is running.

Next, we present the underlying assumptions of Equation (1). First, for the customer’s problem, we discretize the timeline and assume that the customer submits a request for starting a new instance or restarting a previously interrupted instance only at the beginning of each time unit. If the request is granted or rejected, the job will run or wait for the entire time unit until the beginning of the next time unit. In general, we let $\delta > 0$ be the duration of one-time unit (e.g., per minute, per hour) and note that the provider sets a proper δ in practice such that the customer will have enough time to complete a substantial amount of computational workload within δ. Therefore, for a unit job, the delay can be expressed as $\delta I ,$ where I is the random number of rejections before the unit job can be started and then completed in one time unit. As noted previously, I can be approximated by a geometric distribution with success probability $1 - p ,$ , where p is the average preemption probability. Thus, $E [ I ] = p / ( 1 - p )$ . Second, we assume that the reduced utility is proportional to the expected delay, which is a common assumption in the literature (Mendelson and Whang 1990, Afeche\` 2013, and Kilcioglu and Maglaras 2015). As a result, Equation (1) can be extended to any workload of the job that takes $T \geq$ 1 time units to complete. In that case, $U _ { o } ( v , a ) = ( v - w ) T \delta$ and $U _ { p } ( v , a ) = ( v \bar { - } \beta w ) T \delta - ( a p / ( 1 - p ) ) T \delta$ . As can be seen, neither the workload of the job $( \mathrm { i } . \mathrm { e } . , T )$ nor the scale of the time unit $( \mathrm { i } . \mathrm { e } . , \delta )$ affects the customer’s choice between the two types of instances. Hence, without loss of generality, we can focus on the customer’s expected utility based on the unit job and normalize δ to one.

A customer with a fault-tolerant job will choose an on-demand instance if and only if (iff) $U _ { o } ( v , a ) \geq$ $U _ { p } ( v , a )$ and $U _ { o } ( v , a ) \geq 0$ , whereas she will choose a preemptible instance iff $U _ { o } ( v , a ) < U _ { p } ( v , a )$ and $U _ { p } ( v , a ) { \bar { \geq 0 } }$ Here, we assume that the customer’s expected utility of the outside option, “walk away,” is zero, although our analysis can be easily extended to any constant nonzero value of this option. In particular, if $p = 0 .$ then $U _ { p } ( v , a ) \geq U _ { o } ( v , a )$ for all customers, and the equality holds iff $\beta = 1$ . If $p = 1$ , however, then $U _ { p } ( v , a ) <$ $\dot { U _ { o } } ( v , a )$ for all customers. Throughout the remainder of the paper, we focus on the nontrivial situation where $0 < p < 1$ , when the reduced utility because of the possible delay is convexly increasing in $p ,$ and, thus, $U _ { p } ( v , a )$ is concavely decreasing in $p .$

Lemma 1. Define $\tilde { a } = ( 1 - \beta ) w ( 1 - p ) / p ,$ . Under the uniform-discount scheme, the split in the fault-tolerant jobs between the on-demand and preemptible instances is $m _ { o } ( p , \beta )$ and $m _ { p } ( p , \beta )$

$$
m _ {o} (p, \beta) = \int_ {\tilde {a}} ^ {\infty} \int_ {w} ^ {\infty} d F (v, a), m _ {p} (p, \beta) = \int_ {0} ^ {\tilde {a}} \int_ {\beta w + \frac {a p}{1 - p}} ^ {\infty} d F (v, a).\tag{2}
$$

In particular, if the distributions of v and a are independent, then

$$
m _ {o} (p, \beta) = \overline {{H}} (w) \overline {{G}} (\tilde {a}), m _ {p} (p, \beta) = \int_ {0} ^ {\tilde {a}} \overline {{H}} \bigg (\beta w + \frac {a p}{1 - p} \bigg) d G (a),
$$

where $\overline { { H } } ( \cdot )$ is the complementary CDF of the customer’s willingness-to-pay, v. Furthermore, as $\beta$ or $p$ decreases, $m _ { o }$ will decrease, m will increase, and $m _ { p }$ $m _ { o } + m _ { p }$ will increase.

All mathematical proofs of this paper are provided in Online Appendix A.

Lemma 1 shows that our model can capture two salient effects of offering low-priority service with the preemptible instances: the cannibalization and marketing campaign effects. As the provider makes the lowpriority service more attractive (i.e., as $\beta$ or $p$ decreases), existing customers who have fault-tolerant jobs will be more likely than before to adopt the preemptible instances. Furthermore, new customers will be more interested in migrating their computing jobs from an on-premise environment or another provider to this provider. As a result, although customers with fault-tolerant jobs will use fewer on-demand instances, provider will note that the demand from such customers for the preemptible instances will increase, and the total demand will increase as well.

## 3.2. Estimation of the Average Delay Using a Diffusion Approximation Model

In this section, we derive the average delay in completing a unit job on a preemptible instance. It is natural to model the system as a priority-queueing system with preemption, whereby different priority classes are charged at different price rates. This approach, however, fails to provide a closed-form solution for our problem. Therefore, we adopt an alternative approach of diffusion approximation, which has been widely used to approximate the operating characteristics of the $G / G / C$ queues in heavy traf<sup>fi</sup>c (Kingman 1962, Gross et al. 2008, Harrison 2013). In particular, we apply the modeling framework by Harrison (2013) to derive the average workload preempted.

The total workload of the fault-tolerant jobs in $[ 0 , t ] .$ D(t), is a compound Poisson with mean arrival rate $( m _ { o } + m _ { p } ) \lambda$ and random job workloads with mean $\mu$ and variance $\sigma ^ { 2 }$ . The mean of D(t) is equal to the product of average job arrivals in $[ 0 , t ] , ( m _ { o } + m _ { p } ) \lambda t$ , and the average workload of each job, $\mu ;$ that ${ \mathrm { i } } \mathbf { s } ,$

$$
\mathbf {E} [ D (t) ] = (m _ {o} + m _ {p}) \lambda t \mu .
$$

The variance of D(t) is equal to the product of average job arrivals in $[ 0 , t ] , ( m _ { o } + m _ { p } ) \lambda t ,$ and the second moment of the job workload (Kao 1997, equation 2.4.3). Because the second moment of the workload is equal to $\mu ^ { 2 } + \sigma ^ { 2 }$ , we obtain

$$
\mathbf {V a r} [ D (t) ] = (m _ {o} + m _ {p}) \lambda t (\mu^ {2} + \sigma^ {2}).
$$

Also, the total workload of the fault-intolerant jobs in $[ 0 , t ] , D _ { 0 } ( t )$ is a compound Poisson with mean arrival rate $M _ { 0 } \lambda$ and random job workloads with mean µ<sub>0</sub> and variance $\sigma _ { 0 } ^ { 2 } .$ . Similar to the previous derivations, we have

$$
\mathbf {E} [ D _ {0} (t) ] = M _ {0} \lambda t \mu_ {0}, \mathrm{and} \mathbf {V a r} [ D _ {0} (t) ] = M _ {0} \lambda t (\mu_ {0} ^ {2} + \sigma_ {0} ^ {2}).
$$

Moreover, $S ( t ) = k \lambda t - D _ { 0 } ( t )$ is the provider’s total surplus capacity that can be used for the fault-tolerant jobs in 0, t . The mean and variance of $S ( t ) = k \lambda t - D _ { 0 } ( t )$ are given by, respectively,

$$
\begin{array}{r} \mathbf {E} [ S (t) ] = k \lambda t - \mathbf {E} [ D _ {0} (t) ] = (k - M _ {0} \mu_ {0}) \lambda t \\ \mathbf {V a r} [ S (t) ] = \mathbf {V a r} [ D _ {0} (t) ] = M _ {0} \lambda t (\mu_ {0} ^ {2} + \sigma_ {0} ^ {2}). \end{array}
$$

Here, we assume that k is signi<sup>fi</sup>cantly larger than $M _ { 0 } \mu _ { 0 }$ (i.e., $( k - M _ { 0 } \mu _ { 0 } ) \gg 0 )$ so that the probability of having a need to preempt a fault-intolerant job is negligible.

Let $\bar { X ( t ) } = \bar { D ( t ) } - \bar { S ( t ) }$ . Then,

$$
\begin{array}{r l} & {\mathbf {E} [ X (t) ] = \mathbf {E} [ D (t) ] - \mathbf {E} [ S (t) ]} \\ & {\qquad = \lambda t [ (m _ {o} + m _ {p}) \mu + M _ {0} \mu_ {0} - k ],} \end{array}
$$

$$
\begin{array}{r l} & {\mathbf {V a r} [ X (t) ] = \mathbf {V a r} [ D (t) ] + \mathbf {V a r} [ S (t) ]} \\ & {\qquad = \lambda t [ (m _ {o} + m _ {p}) (\mu^ {2} + \sigma^ {2}) + M _ {0} (\mu_ {0} ^ {2} + \sigma_ {0} ^ {2}) ].} \end{array}
$$

We now approximate X(t) to a Brownian motion (BM), $d X ( t ) = \mu _ { x } d t + \sigma _ { x } d W ( t ) .$ , where W(t) is a standard Weiner process, and the drift and standard deviation, $\mu _ { x }$ and $\sigma _ { x } ,$ respectively, are

$$
\begin{array}{r l} & {\mu_ {x} = \lambda [ (m _ {o} + m _ {p}) \mu + M _ {0} \mu_ {0} - k ], \mathrm{and}} \\ & {\sigma_ {x} = \sqrt {\lambda [ (m _ {o} + m _ {p}) (\mu^ {2} + \sigma^ {2}) + M _ {0} (\mu_ {0} ^ {2} + \sigma_ {0} ^ {2}) ]}.} \end{array}
$$

By this de<sup>fi</sup>nition, it can be seen that $\mathbf { E } [ X ( t ) ] = \mu _ { x } t$ and ${ \dot { \mathbf { V } } } \mathbf { a r } [ X ( t ) ] = \sigma _ { r } ^ { 2 } t$

Hence, following Harrison (2013, chapter 2.1), the amount of workload preempted (and to be resumed later) at the point of time $t , Z _ { t } ,$ has been proven to be a reflected BM given X(t), also known as a BM modified by a lower reflecting barrier at zero given X(t). We refer the reader to Online Appendix B for more details about the derivation.

Then, the CDF of $Z _ { t }$ is as follows (Harrison 2013, equation 1.51):

$$
\operatorname * {P r} \{Z _ {t} \leq z \} = \Phi \bigg (\frac {z - \mu_ {x} t}{\sigma_ {x} \sqrt {t}} \bigg) - e ^ {\frac {2 \mu_ {x} z}{\sigma_ {x} ^ {2}}} \Phi \bigg (\frac {- z - \mu_ {x} t}{\sigma_ {x} \sqrt {t}} \bigg),
$$

where $\Phi ( \cdot )$ is the CDF of a standard normal distribution. ${ \mathrm { I f } } ,$ on average, the total workload of the fault-tolerant jobs exceeds the surplus capacity $( \mathrm { i . e . , ~ } \mu _ { x } \geq 0 )$ then the amount of workload preempted goes to in<sup>fi</sup>nity in the long run. Clearly, this is not a relevant case. We thus focus on the case in which $\mu _ { x } < 0 ,$ , that is, $( m _ { o } + m _ { p } ) \mu < k - M _ { 0 } \mu _ { 0 }$

$\mathbf { A } \mathbf { s } \ t  \infty ,$ the steady-state distribution of $Z _ { t }$ will be

$$
\operatorname * {P r} \{Z _ {\infty} \leq z \} = 1 - e ^ {\frac {2 \mu_ {x} z}{\sigma_ {x} ^ {2}}}.
$$

Therefore, the long-term average amount of workload preempted, namely, $N _ { p } ,$ is given by

$$
\begin{array}{r l} & N _ {p} = E [ Z _ {\infty} ] = \frac {\sigma_ {x} ^ {2}}{2 | \mu_ {x} |} \\ & \qquad = \frac {(m _ {o} + m _ {p}) (\mu^ {2} + \sigma^ {2}) + M _ {0} (\mu_ {0} ^ {2} + \sigma_ {0} ^ {2})}{2 [ k - (m _ {o} + m _ {p}) \mu - M _ {0} \mu_ {0} ]}, \mathrm{with} \\ & \qquad k > (m _ {o} + m _ {p}) \mu + M _ {0} \mu_ {0}. \end{array}\tag{3}
$$

According to Harrison (2013), this approximation using the BM is reasonable, provided that the input $( \mathrm { i . e . , }$ the total workload of the fault-tolerant jobs) and output (i.e., supply of the surplus capacity) are suf<sup>fi</sup>ciently large and the difference between the two stochastic processes is not too small. These conditions are well suited in the context of our model in which a public cloud provider has suf<sup>fi</sup>cient surplus capacity to serve a large pool of customers.

Finally, applying Little’s Law, the average delay of a unit job on a preemptible instance, $W _ { p } ,$ is

$$
W _ {p} = \frac {N _ {p}}{\lambda m _ {p} \mu} = \frac {(m _ {o} + m _ {p}) (\mu^ {2} + \sigma^ {2}) + M _ {0} (\mu_ {0} ^ {2} + \sigma_ {0} ^ {2})}{2 \lambda m _ {p} \mu [ k - (m _ {o} + m _ {p}) \mu - M _ {0} \mu_ {0} ]},\tag{4}
$$

where an implicit assumption is that the provider will interrupt only the preemptible instances, as, in practice, the on-demand instances are covered by the provider’s SLA and are never interrupted.

It is important to note that $W _ { p }$ given by (4) is the system’s actual average delay for a unit job (i.e., from the provider’s perspective). The customers, however, do not possess such information; rather, they may have a rational expectation of the average delay based on their belief about the average preemption probability. As noted earlier, the customers can form a common belief about the average preemption probability based on either an observation of the historical preemption frequency by a third party (e.g., a cloud services consulting company) or, sometimes, information provided by the cloud provider (see Endnote 6). Thus, of particular interest is an equilibrium that would arise from the customers’ rational expectation, which requires the customers’ estimate of the average delay based on a common belief about the average preemption probability to be consistent with the true average delay of the system. Such a condition for the existence of an equilibrium arising from the customers’ rational expectation translates into the following equation:

$$
\frac {p}{1 - p} = \frac {(m _ {o} + m _ {p}) (\mu^ {2} + \sigma^ {2}) + M _ {0} (\mu_ {0} ^ {2} + \sigma_ {0} ^ {2})}{2 \lambda m _ {p} \mu [ k - (m _ {o} + m _ {p}) \mu - M _ {0} \mu_ {0} ]}.\tag{5}
$$

A <sup>fi</sup>nal remark is that our model can be solved with or without the equilibrium Condition (5). In fact, in the next section, we <sup>fi</sup>rst formulate the provider’s revenue-maximization problem based on any common belief of the customers about the average preemption probability, whereas the common belief may or may not be biased. Furthermore, with Condition (5) imposed, we also derive the equilibrium that would arise from the customers’ rational expectation.

## 4. Analysis of the Discount Pricing Schemes

In this section, we examine the provider’s revenuemaximization problem. In Section 4.1, we focus on the uniform discount scheme, which has been used by many cloud providers, such as GCP and IBM Cloud (Schonberg 2019). In Section 4.2, we propose and analyze a class of alternative discount schemes, namely, the interruption-based discount scheme, for which the form of discount is based on actual interruptions experienced in each individual instance.

To obtain a closed-form solution to the provider’s problem, from which useful insights can be derived, we assume that the customers’ willingness-to-pay and sensitivity-to-delay follow two independent uniform distributions. To demonstrate the robustness of our results under different distributions and with interdependency between the two parameters, in Section 5, we extend our model to a bivariate normal distribution and obtain numerically the provider’s optimal decision.

We note that, in practice, the cloud provider offers a variety of VMs with different con<sup>fi</sup>gurations, but the discount rates are determined individually for each type of VM. Without loss of generality, we consider a generic type of VM and let w be the regular price per time unit for an on-demand instance based on the generic VM. Evidence shows that the intense competition among major public cloud providers has led to the same or similar on-demand prices for comparable VMs (CloudHealth by VMWare 2018). Thus, we consider w as an exogenous parameter determined by the market, which allows us to focus on a provider’s pricing strategy for his low-priority, preemptible instances. Unlike the mainstream market of on-demand instances, the low-priority service with preemptible instances is relatively new in the marketplace. Furthermore, different cloud providers have different technical strengths and weaknesses in providing the preemptible instances (Schonberg 2019). In particular, they face different market sizes and have different surplus capacities, and thus, each provider faces unique supply-demand dynamics for the market segment of preemptible instances. Thus, in the subsequent analysis, we focus on deriving the provider’s optimal discount rate for the preemptible instances.

## 4.1. Uniform Discount Scheme

Given customers’ common belief about the average preemption probability, $p ,$ the provider’s objective is to determine the discounted price, βw $( \beta \in \left[ 0 , 1 \right] )$ , to maximize his expected revenue per time unit. The optimization problem is formulated as follows:

$$
\max _ {0 \leq \beta \leq 1} \Pi^ {U D} (p, \beta) = \max _ {0 \leq \beta \leq 1} w \Bigl (m _ {o} (p, \beta) + \beta m _ {p} (p, \beta) \Bigr) \lambda \mu ,\tag{6}
$$

where $m _ { o } ( p , \beta )$ and $m _ { o } ( p , \beta )$ can be obtained using Lemma 1. We use the superscript UD hereafter to denote results under the uniform discount scheme.

In general, Optimization Problem (6) can at least be solved numerically using the line-search method. To obtain more analytical results and deeper insights, we now assume that customers’ willingness-to-pay, v, is uniformly distributed on $[ 0 , V ]$ , and their sensitivity-todelay, a, is uniformly distributed on 0, A . Moreover, we assume that the two parameters are independent. To avoid trivial cases that are not of interest, we focus on cases in which (i) $V > w$ and (ii) $\overline { { { H } } } ( w ) \mu < k - M _ { 0 } \mu _ { 0 } .$ The reason is as follow. If $V \leq w ,$ , then none of the customers will choose the on-demand instance. If $\overline { { { H } } } ( w ) \mu \geq$ $\begin{array} { r } { k - M _ { 0 } \mu _ { 0 } \ ( \mathrm { i . e . , ~ } V \geq \frac { \mu w } { \mu + M _ { 0 } \mu _ { 0 } - k } ) . } \end{array}$ , then the provider will not be interested in offering the preemptible instance to attract more demand as, on average, the surplus capacity is not enough to satisfy customers’ requests for the ondemand instances.

It should be noted that Optimization Problem (6) is formulated based on any common belief of the customers about the average preemption probability, and that, in general, such a belief may or may not be consistent with the system’s true average preemption probability. Of particular interest, however, is an equilibrium that would arise from the customers’ rational expectation of the average preemption probability and the provider’s optimal response to that expectation. Let $\stackrel { \star } { p } { } ^ { U D }$ denote the average preemption probability in such an equilibrium under the uniform discount

Split of demand between the on-demand and preemptible instances 35.00%

scheme. Speci<sup>fi</sup>cally, given the customers’ common belief about the average preemption probability, $p ^ { U D }$ the provider solves Problem (6) (with p replaced by $p ^ { U D } )$ to obtain the optimal pricing decision, $\beta ( p ^ { U D } )$ This decision, in turn, should cause an average delay that is consistent with the customers’ estimate of the average delay given their common belief $p ^ { U D }$ (i.e., Equation (5) should hold). The proposition below provides analytical results of the provider’s optimal pricing decision, the resulting split of demand, and the provider’s maximal revenue.

Proposition 1. When the customers’ willingness-to-pay and their sensitivity-to-delay are independent and uniformly distributed, solving Problem (6) yields $\beta ( p ^ { U D } ) = 1$ when $2 V \geq 3 w ,$ while $\beta ( p ^ { U D } ) = \frac { 4 V } { 3 w } - 1$ when $2 V < 3 w$ . Moreover, for cases where $2 V < 3 w ,$ , we have

$$
m _ {o} \left(p ^ {U D}, \beta \left(p ^ {U D}\right)\right) = \frac {V - w}{V} - \frac {2 \left(1 - p ^ {U D}\right) (3 w - 2 V) (V - w)}{3 A p ^ {U D} V};\tag{7}
$$

$$
m _ {p} (p ^ {U D}, \beta (p ^ {U D})) = \frac {2 (1 - p ^ {U D}) (3 w - 2 V)}{9 A p ^ {U D}};\tag{8}
$$

$$
\Pi^ {U D} (p ^ {U D}, \beta (p ^ {U D})) = \left\{\frac {(V - w) w}{V} + \frac {2 (1 - p ^ {U D}) (3 w - 2 V) ^ {3}}{2 7 A p ^ {U D} V} \right\} \lambda \mu .\tag{9}
$$

Proposition 1 reveals an important market condition that is favorable (unfavorable) to the provider’s motivation for offering the preemptible instances. In particular, under the assumptions of this proposition, the provider should optimally offer (not offer) the preemptible instances if $\hat { V } < 3 w \hat { / } 2$ (or $V \geq 3 w / 2 )$ . The reason is that, if the market consists of a signi<sup>fi</sup>cant portion of customers whose willingness-to-pay is higher than the on-demand price rate, it may not be bene<sup>fi</sup>- cial to offer the preemptible instances because the increased revenue caused by the marketing campaign effect of such an offer cannot offset the reduced revenue caused by the cannibalization effect, as lots of customers would switch from on-demand instances to preemptible instances.

To simplify the notation, de<sup>fi</sup>ne $m _ { o } ^ { U D } = m _ { o } ( p ^ { U D } ,$ $\beta ( p ^ { U D } ) ) , \bar { m _ { p } ^ { U D } } \stackrel { \cdot } { = } m _ { p } ( p ^ { U D } , \beta ( p ^ { U D } ) )$ and $\Pi ^ { U { \bar { D } } } = \Pi ^ { U D } ( p ^ { U D } ,$ $\beta ( p ^ { U D } ) _ { , }$ . Similar to Lemma 1, Proposition 1 yields the following results.

Corollary 1. As $p ^ { U D }$ increases, then $m _ { o } ^ { U D }$ increases and $m _ { p } ^ { U D }$ decreases. The total demand (i.e., $m _ { o } ^ { U D } + m _ { p } ^ { U D } )$ , however, decreases, and thus the provider’s optimal revenue decreases.

Figure 1 illustrates the results of Corollary 1. As can be seen, as the customers’ common belief about the average preemption probability increases, demand for the preemptible instances decreases rapidly and then converges to zero. Meanwhile, demand for the on-demand instances <sup>fi</sup>rst increases and then <sup>fl</sup>attens out to a plateau. The increase in demand for the on-demand instances, however, cannot offset the decrease in demand for

## Figure 1. Split of Demand and Total Demand Under Various Average Preemption Probabilities

![](/api/attachments/JC7XVMAY/fulltext/images/738373d027a0aa740bc78a7b79ea34d815e9e65410740c60908791b3b5a7113f.jpg)  
Note. w 100, V 135, A 500, and p<sup>UD</sup> 5%, 100% .

Figure 2. Managerial Implications of Propositions 1 and 2  
![](/api/attachments/JC7XVMAY/fulltext/images/5ea6cba91b657df3930999fc75956fb47c2eecc722003a372bc4d6bee8e2449c.jpg)

the preemptible instances as the provider loses sales to customers who are interested in using only the preemptible instances. Consequently, the total demand and the provider’s optimal revenue are both (convex) decreasing functions of the customers’ common belief about the average preemption probability.

Furthermore, under an equilibrium that would arise from the customers’ rational expectation of the average preemption probability and average delay, $p ^ { U D }$ can be obtained by Equation (5); that is,

$$
\frac {p ^ {U D}}{1 - p ^ {U D}} = \frac {(m _ {o} ^ {U D} + m _ {p} ^ {U D}) (\mu^ {2} + \sigma^ {2}) + M _ {0} (\mu_ {0} ^ {2} + \sigma_ {0} ^ {2})}{2 \lambda m _ {p} ^ {U D} \mu [ k - (m _ {o} ^ {U D} + m _ {p} ^ {U D}) \mu - M _ {0} \mu_ {0} ]}.\tag{10}
$$

Lemma 2. When the customers’ willingness-to-pay and sensitivity-to-delay are independent and uniformly distributed, there exists a unique nonzero solution, $p ^ { U D }$ , which satisfies Equation (10).<sup>7</sup>

The closed-form solution for $p ^ { U D }$ is provided in the proof of this lemma in Online $\mathrm { A }$ ppendix A.

Based on the result of Lemma 2, we obtain deeper results regarding the impacts of the mean and variance of the surplus capacity on key performance measures of the system, as stated in the next proposition.

## Proposition 2.

As the average surplus capacity increases (k increases, $M _ { 0 } ,$ or $\mu _ { 0 }$ decreases), then $p ^ { \dot { \boldsymbol { u } } D }$ reduces. As a result, $m _ { o } ^ { U D }$ decreases, $m _ { p } ^ { \dot { U } D }$ increases, $m _ { o } ^ { U D } + m _ { p } ^ { U D }$ increases, and $\Pi ^ { U D }$ increases.

As the volatility of the surplus capacity decreases $( M _ { 0 } ,$ µ<sub>0</sub>, or $\sigma _ { 0 }$ decreases), then $p ^ { \boldsymbol { \omega } }$ reduces. As a result, $m _ { o } ^ { U D }$ decreases, $m _ { p } ^ { U D }$ increases, $m _ { o } ^ { U D } + m _ { p } ^ { U D }$ increases, and $\Pi ^ { U D }$ increases.

Propositions 1 and 2 together establish the following important managerial insights:

First, on the supply side, there are two key operating characteristics: the average and the variation (volatility) of the surplus capacity. As the total capacity of instances $( \mathrm { i } . \mathrm { e } . , k )$ increases, the average surplus capacity increases. Moreover, the arrival rate and workloads of fault-intolerant jobs also heavily in<sup>fl</sup>uence the surplus capacity, as the provider needs to prioritize the computing needs of such jobs and then allocates the remaining capacity to serve the fault-tolerant jobs. Speci<sup>fi</sup>cally, as the arrival rate or the average workload of the fault-intolerant jobs $( \mathrm { i . e . , } \ M _ { 0 } \ \mathrm { o r } \ \mu _ { 0 } )$ increases, not only will the average surplus capacity decrease, but the volatility of the surplus capacity will increase. As the variation of the workload of fault-intolerant jobs $( \mathrm { i . e . } , \sigma _ { 0 } )$ increases, however, the average surplus capacity will not be affected, but the volatility of the surplus capacity will increase.

Hence, as Figure 2 shows, as k increases, $M _ { 0 }$ decreases, $\mu _ { 0 }$ decreases, or $\sigma _ { 0 }$ decreases, the average surplus capacity increases and the volatility of the surplus capacity decreases. As a result, the average preemption probability $( \mathrm { i . e . } , p ^ { U D } )$ is expected to decrease, as Proposition 2 con<sup>fi</sup>rms.

Second, on the demand side, as a result of the smaller preemption probability $( \mathrm { i . e . , }$ $p ^ { U D }$ decreases), there will be more demand for the preemptible instances $( \mathrm { i } . \mathrm { e } . , m _ { p } ^ { U D }$ will increase). Meanwhile, because of the cannibalization effect of the preemptible instances, use of the on-demand instances $( \mathrm { i . e . } , m _ { o } ^ { U D } )$ will decrease. The total demand from the fault-tolerant jobs (i.e., $m _ { o } ^ { U D } + m _ { p } ^ { U D } )$ , however, will increase. Such results also are consistent with Proposition 1.

Last, but not least, as the average surplus capacity increases or the variation of the surplus capacity decreases, the average preemption probability decreases. As a result, the total demand increases, which, however, tends to cause the average preemption probability to rise. Proposition 2 implies that between the two opposite effects, the former dominates the latter, and, overall, the average preemption probability will decrease for sure.

## 4.2. Interruption-Based Discount Scheme

Although the uniform discount scheme has been commonly used, one may argue that it is not fair from the customers’ perspective to receive the same discount, as some of them may experience no preemption at all in the completion of their jobs, whereas some others may experience many interruptions. To address such challenge, we propose and analyze an alternative discount scheme based on the occurrence of preemptions, namely, the interruption-based discount scheme.

Speci<sup>fi</sup>cally, when a customer submits a job for a preemptible instance, she does not receive a discount automatically. Instead, the customer will receive a monetary compensation at a rate of $\alpha \ge 0$ per interruption in the completion of her job. As noted in Section ${ 3 , } ^ { \top }$ we assume that the customer can submit a request for starting a new instance or restarting a preempted instance only at the beginning of each time unit. If the request is granted (rejected), then the job will run (wait) for the entire time until the beginning of the next time unit. Thus, the delay for a unit job can be expressed as Iδ, where I is the random number of interruptions before the job can be completed and δ is the duration of one-time unit. Recall that, without loss of generality, we set $\delta = 1$ . Thus, the compensation rate is α per interruption or, equivalently, per time unit of delay. The customer’s expected utility of completing a unit job with an on-demand or a preemptible instance will be

$$
U _ {o} (v, a) = v - w, U _ {p} (v, a) = \left(v - \frac {a p}{1 - p}\right) - w + \frac {\alpha p}{1 - p}.\tag{11}
$$

To explain the customer’s expected utility with a preemptible instance, we note that the customer pays w for the unit job while she may experience interruptions and delays before completing the job. As explained in Section $^ { 3 , }$ because of the lack of accurate information about the realtime preemption probability, the customer’s estimation of the expected delay can be well approximated by $p / ( 1 - p )$ given her belief about the average preemption probability, $p .$ Thus, from the customer’s perspective, the expected amount of compensation is equal to $\alpha p / ( 1 - p )$

Lemma 3. Under the interruption-based scheme, the split of demand from the fault-tolerant jobs between the on-demand and preemptible instances are, respectively,

$$
\begin{array}{c} m _ {o} (p, \beta) = \int_ {\alpha} ^ {\infty} \int_ {w} ^ {\infty} d F (v, a), m _ {p} (p, \beta) \\ = \int_ {0} ^ {\alpha} \int_ {w \frac {(a - a) p}{1 - p}} ^ {\infty} d F (v, a). \end{array}\tag{12}
$$

If α increases, then $m _ { o }$ decreases, $m _ { p }$ increases, and $m _ { o } + m _ { p }$ increases. If p increases (while α stays the same), then $m _ { o }$ stays the same, $m _ { p }$ increases, and $m _ { o } + m _ { p }$ increases.

The following analysis of the interruption-based discount scheme is parallel to that of the uniform discount scheme in Section 4.1. Suppose that the customers’ common belief about the average preemption probability is $p .$ The provider determines the optimal compensation rate, $\alpha ( p )$ , to maximize the expected revenue per time unit, which is formulated as follows:

$$
\max _ {\alpha \geq 0} \Pi^ {I B} (p, \alpha) = \max _ {\alpha \geq 0} w \Bigl (m _ {o} (p, \alpha) + m _ {p} (p, \alpha) \Bigr) \lambda \mu - \alpha N _ {p},\tag{13}
$$

where $N _ { p }$ is the average amount of workload preempted given by (3). For the last term of (13), the provider pays α per interruption as a compensation for every instance preempted. Equivalently, the compensation scheme can be viewed as α per time unit of delay; thus, the average amount of compensation for a unit job is α $: W _ { p } ,$ where $W _ { p }$ is the average delay of the unit job. Because there are $\lambda m _ { p } ( p , \alpha ) \mu$ unit jobs per time unit on average, the total amount of compensation per time unit will be α $\langle W _ { p } \cdot \lambda m _ { p } ( p , \alpha ) \mu = \alpha { \bar { N } } _ { p }$ according to Equation (4).

Similar to the analysis in Section 4.1, we examine the equilibrium that arises from the customers’ unbiased common belief about the average preemption probability, $p ^ { I B }$ . Given the customers’ common belief $\stackrel { \bullet } { p } ^ { I B } .$ , the provider should solve Problem (13) to determine the optimal compensation rate, $\alpha ( p ^ { I B } )$ . Such a decision, in turn, will cause an average delay $W _ { p } ,$ which should be in line with the customers’ rational expectation of the average delay based on their unbiased belief about $p ^ { I B }$ (i.e., Equation (5) should hold at $p ^ { I B } )$ . Assuming that customers’ willingness-to-pay and sensitivity-to-delay are independent and uniformly distributed, we obtain a closed-form solution for $\alpha ( p ^ { I \bar { B } } )$

Proposition 3. If customers’ willingness-to-pay and sensitivity-to-delay are independent and uniformly distributed, the optimal compensation rate is as follows: If $2 V \geq 3 w$ then $\overset { \cdot } { \alpha } ( p ^ { I B } ) = 0$ . But $i f 2 V < 3 w ,$ then $\alpha ( p ^ { I B } )$ is equal to $2 ( 1 - p ^ { \dot { I } \dot { B } } ) ( 3 w - 2 V ) / ( \bar { 3 } p ^ { I B } )$ and decreases in $p ^ { I B }$

It is important to note that the optimal compensation rate is a decreasing function of the average preemption probability in equilibrium. An intuitive explanation is as follows. When there is a large portion of customers with relatively low willingness-to-pay (i.e., when $2 V < 3 w )$ who are potential users of the preemptible instances, the provider should reduce the compensation rate in response to an increase in the average preemption probability to cap the total amount of compensation. There is a side effect of reducing the compensation rate as demand for the preemptible instances will decrease; however, it is less of a concern for the provider, given that there is a relatively large pool of the potential preemptible instance users. In contrast, when there is only a small portion of customers with relatively low willingness-to-pay $( \mathrm { i . e . } $ , when $2 V \geq 3 w )$ , the conclusion is the same as that of Proposition 1. That is, the provider should not offer the preemptible instances as the loss of revenue from the existing users of the on-demand instances because the cannibalization effect will dominate the bene<sup>fi</sup>ts of attracting new customers by offering the preemptible instances.

Furthermore, for the nontrivial case where $2 V < 3 w$ we <sup>fi</sup>nd

$$
m _ {o} (p ^ {I B}, \alpha (p ^ {I B})) = \frac {V - w}{V} - \frac {2 (1 - p ^ {I B}) (3 w - 2 V) (V - w)}{3 A p ^ {I B} V};\tag{14}
$$

$$
m _ {p} (p ^ {I B}, \alpha (p ^ {I B})) = \frac {2 (1 - p ^ {I B}) (3 w - 2 V)}{9 A p ^ {I B}};\tag{15}
$$

$$
\Pi^ {I D} (p ^ {I B}, \alpha (p ^ {I B})) = \left\{\frac {(V - w) w}{V} + \frac {2 (1 - p ^ {I B}) (3 w - 2 V) ^ {3}}{2 7 A p ^ {I B} V} \right\} \lambda \mu .\tag{16}
$$

Interestingly, (14)–(16) have the same expressions as those of $( 7 ) - ( 9 )$ . In other words, from the provider’s perspective, the interruption-based discount scheme becomes equivalent to the uniform discount scheme. That is, as long as the customers’ common beliefs about the average preemption probability are the same, the provider’s optimal pricing decision will lead to the same demand under the two discount schemes, which will result in the same average preemption probability faced by the customers. The equivalence between the two discount schemes stems from two assumptions. That is, (1) as customers are risk neutral, their utility ex ante is in<sup>fl</sup>uenced by their expectation of the preemption probability; and (2) as the provider interrupts the preemptible jobs randomly from the customers’ perspective, they will have the same expectation of the preemption probability.

Provided that these two conditions hold, we can generalize the equivalency result to a family of interruption-based discount schemes, each of which is denoted by Θ. For instance, Θ can be viewed as a set of parameters that de<sup>fi</sup>nes the speci<sup>fi</sup>c discount scheme. Let EC p Θ denote the expected amount of compensation that a customer would receive in the completion of a unit job using a preemptible instance, given her expectation of the preemption probability $p .$ Then, the customer’s utility function can be written as

$$
U _ {p} (v, a) = \left(v - \frac {a p}{1 - p}\right) - w + E C (p | \Theta).\tag{17}
$$

For instance, if the provider offers α per interruption as compensation, then $E C ( p | \Theta ) = \alpha p / ( \bar { 1 } - p ) ,$ and thus, (17) reduces to (11). However, if the compensation is a <sup>fi</sup>xed lump sum of γ for each interrupted preemptible instance, regardless of the number of interruptions, then $\bar { E } \bar { C } ( p | \Theta ) = \gamma p$

Proposition 4. If the provider interrupts the preemptible instances randomly and the customers are risk neutral, then from the provider’s perspective, the uniform discount scheme and the family of the interruption-based schemes are equivalent in terms of the split in demand between the ondemand and preemptible instances as well as the maximal expected revenue.

Our explanation is as follows. Under an interruption-based discount scheme, the expected amount of compensation, $E C ( p | \Theta )$ , depends only on the parameters of the compensation scheme and the customers expectation of the preemption probability. Because the provider interrupts the preemptible instances randomly, the customers’ expectation of the preemption probability will be the same. As a result, the expected amount of compensation is indeed “uniform” for all customers, although the compensations ex post can be (and usually are) different. Hence, the provider can adjust the parameters of the interruption-based discount scheme to ensure that the expected amount of compensation is equal to the cost savings (discounts) under the uniform discount scheme, and vice versa, so that the customers will be indifferent in regard to the two discount schemes.

Proposition 4 also can explain the popularity of the uniform discount scheme in practice. Not only is it easy to communicate, but the resulting expected revenue for the provider is the same as that of the general family of interruption-based discount schemes. Having said that, the customers of the preemptible instances may perceive that the interruption-based schemes have a distinct advantage in terms of fairness, as the cost savings in the form of compensation are distributed only among interrupted jobs and, thus, the affected customers.

Fairness, or social justice, has been widely studied by psychologists, economists, and social behavior scientists. In particular, there is a body of literature on fairness in queues. For instance, Maister (1984) highlighted the difference between a customer’s perception and expectation in his discussion of the psychology of waiting lines. Larson (1987) identi<sup>fi</sup>ed social injustice as one of the most important factors that could affect a customer’s satisfaction in a queueing system.

Of particular relevance to our problem is the socalled “individual customer (job) unfairness (discrimination)” by Avi-Itzhak et al. (2008, p. 503), which is “the deviation of the treatment given to the customer, in a particular scenario, from the absolutely fair treatment as de<sup>fi</sup>ned by the underlying fairness principle of the measure.” In our problem, absolutely fair treatment means that all users of the preemptible instances should experience the same waiting time. In this regard, the uniform-discount scheme creates a deviation from the absolutely fair treatment, thus resulting in individual customer (job) unfairness ex post. The reason is that, although all customers need to pay the same discounted price for using the same service (i.e., the preemptible instances), only a small portion of the customers will actually experience interruptions and thus be affected. For instance, in a given time window (e.g., within 24 hours), some customers may have experienced interruptions, knowing that some others must have experienced no interruption at all. It is likely that the former will perceive unfairness compared with others’ experience. By contrast, the proposed interruption-based scheme can mitigate such negative feelings of the frustrated customers, as such a scheme aims to provide a compensation for each interruption, and thus, an impacted customer who experiences more interruptions will also receive a deeper discount than others.

## 4.3. Comparison of the Two Discount Schemes with Risk-Averse Customers

It is important to note that the equivalency between the uniform and interruption-based discount schemes does not require the assumption of independence and uniformity of the customers’ willingness-to-pay and sensitivity-to-delay. Instead, a necessary condition for the equivalency is that the customers are all risk neutral. When such an assumption is relaxed, however, not only the average but also the variance of the delay that a customer may experience due to the interruptions can in<sup>fl</sup>uence the customer’s preference of one discount scheme over the other. We now examine an extension to our base model with an assumption that the customers are risk averse.

Consider a customer who needs to complete a unit job. Recall that I denotes the random number of interruptions or, equivalently, the delay in terms of time units that the customer may experience in the completion of the unit job. If this customer uses an on-demand instance, the net value of completing the unit job will be $u _ { o } ( v , a , I ) = v - w$ . If, instead, this customer uses a preemptible instance, the net value will be $u _ { p } ( v , a , \bar  I ) = ( v - a I ) - \beta w$ under the uniform discount scheme or $u _ { p } ( v , a , I ) = ( v - a I ) - w + \alpha I$ under the interruption-based scheme,<sup>8</sup> respectively.

If the customer is risk neutral, his objective is to maximize the expectation of the net value, $U _ { i } ( v , a ) = \mathbf { E } [ u _ { i } ( v , a , I ) ] , i \in \{ o , p \}$ , where the expectation is with respect to I. Speci<sup>fi</sup>cally, $U _ { o } ( v , a ) = v - w$ and because $\mathbf { E } [ I ] { \bar { = } } p / ( 1 - p { \bar { ) } } , U _ { p } ( v , a )$ reduces to Equation (1) or (11) under the uniform or the interruption-based scheme, respectively. In contrast, if the customer is risk averse, we assume that his objective is to maximize the expectation of a commonly used exponential utility function, $U _ { i } ( v , a ) = \mathbf { E } [ 1 - e ^ { - \bar { r u } _ { i } ( v , a , I ) } ] , i \in \bar { \{ o , p \} }$ , where $r >$ 0 is the parameter of the exponential utility function and the expectation is with respect to I. Speci<sup>fi</sup>cally,

$U _ { o } ( v , a ) = 1 - e ^ { - r ( v - w ) }$ . Moreover, $U _ { p } ( v , a )$ is given as follows. Under the uniform discount scheme,

$$
\begin{array}{c} U _ {p} (v, a) = \mathbf {E} [ 1 - e ^ {- r (v - a I - \beta w)} ] = 1 - e ^ {- r (v - \beta w)} \frac {1 - p}{1 - p e ^ {r a}}, \\ \text {for} a <   \frac {1}{r} \ln \left(\frac {1}{p}\right). \end{array}\tag{18}
$$

However, under the interruption-based discount scheme,

$$
\begin{array}{r l} & U _ {p} (v, a) = \mathbf {E} [ 1 - e ^ {- r (v - a I - w + \alpha I)} ] \\ & \qquad = 1 - e ^ {- r (v - w)} \frac {1 - p}{1 - p e ^ {r (a - \alpha)}}, \text {for} a <   \alpha + \frac {1}{r} \ln \left(\frac {1}{p}\right). \end{array}\tag{19}
$$

The conditions in Equations (18) and (19) ensure that $\mathbf { E } [ e ^ { r a I } ]$ and $\mathbf { E } [ e ^ { r ( a - \alpha ) I } ]$ are well de<sup>fi</sup>ned.

As in the base model, we assume that the net value of completing a unit job with the walk away option is zero, and thus the exponential utility of this option also is zero $( \mathrm { i . e . , ~ } 1 - \stackrel { \cdot } { e ^ { - r \cdot 0 } } = 0 )$ . Hence, similar to the base model, the customer prefers to use an on-demand instance iff $U _ { o } ( v , a ) \overset { \vartriangle } { \geq } U _ { p } ( v , a )$ and $U _ { o } ( v , a ) \geq 0 .$ whereas the customer prefers to use a preemptible instance iff $U _ { p } ( v , a ) \geq U _ { o } ( v , a )$ and $U _ { p } ( v , a ) \geq 0$

Lemma 4. Under the uniform discount scheme, let $\tilde { a } = \frac { 1 } { r } \mathrm { l n } \left( \frac { 1 - \left( 1 - p \right) e ^ { - r \left( 1 - \beta \right) w } } { p } \right) .$ . Then,

$$
\begin{array}{r} m _ {o} (p, \beta) = \int_ {\tilde {a}} ^ {\frac {1}{r} \ln \left(\frac {1}{p}\right)} \int_ {w} ^ {\infty} d F (v, a), m _ {p} (p, \beta) \\ = \int_ {0} ^ {\tilde {a}} \int_ {\beta w + \frac {1}{r} \ln \left(\frac {1 - p}{1 - p e ^ {x \beta}}\right)} ^ {\infty} d F (v, a). \end{array}\tag{20}
$$

Under the interruption-based scheme, where the compensation is α per interruption, we obtain

$$
\begin{array}{r} m _ {o} (p, \alpha) = \int_ {\alpha} ^ {\alpha + \frac {1}{r} \ln \left(\frac {1}{p}\right)} \int_ {w} ^ {\infty} d F (v, a), m _ {p} (p, \alpha) \\ = \int_ {0} ^ {\alpha} \int_ {w + \frac {1}{r} \ln \left(\frac {1 - p}{1 - p e ^ {r (a - \alpha)}}\right)} ^ {\infty} d F (v, a). \end{array}\tag{21}
$$

Then, the provider’s problem under the uniform discount and interruption-based schemes can be expressed in the same way as (6) and (13), respectively. Unlike the base model, it is dif<sup>fi</sup>cult to obtain a closed-form solution for the provider’s optimal pricing decisions because of the lack of a compact form of the provider’s objective function in the presence of risk-averse customers. That said, the provider’s optimal pricing decision can be obtained numerically, using the standard line-search approach, as illustrated by our numerical experimentation in Section 5.

Although a closed-form solution for the provider’s revenue-maximization problem is not available, we can show that the uniform and interruption-based discount schemes now have different impacts on different customer segments, given that they are risk averse and their decisions are based on the exponential utility functions in Equations (18) or (19), respectively.

Speci<sup>fi</sup>cally, we compare a customer’s utility under the interruption-based scheme to that under the uniform-discount scheme. Suppose that the customers’ belief about the average preemption probability, $p ,$ is the same under the two scheme. Then, we <sup>fi</sup>nd

$$
\begin{array}{c} U _ {p} ^ {I B} (v, a) \geq U _ {p} ^ {U D} (v, a) \Longleftrightarrow a \geq \overline {{a}} (\alpha , \beta) \\ = \frac {1}{r} \ln \left(\frac {1 - e ^ {- r (1 - \beta) w}}{p [ 1 - e ^ {- r (1 - \beta) w} e ^ {- r \alpha} ]}\right) \end{array}\tag{22}
$$

The implication of (22) is as follows: the utility of a customer is no longer the same under different schemes. As a result, the customer will have a preference for a particular scheme, and the preference is dependent on various factors including the compensation (discount) rate of the interruption-based (uniformdiscount) scheme as well as the customer’s sensitivity to delay.

1. For customers who are patient (i.e., their sensitivity-to-delay, $a ,$ is smaller than $\overline { { a } } ( \alpha , \beta ) )$ , their utility of using a preemptible instance is lower under the interruption-based scheme than that under the uniformdiscount scheme, resulting in a lower demand from such customers as compared with the demand under the uniform discount scheme.

2. For customers who are moderately patient (i.e., their sensitivity-to-delay, $a ,$ is in the interval $\overline { { a } } ( \alpha , \beta ) <$ $a \leq \alpha )$ , their utility of using a preemptible instance is higher under the interruption-based scheme than that under the uniform-discount scheme, leading to a higher demand from such customers compared with the demand under the uniform discount scheme. Moreover, it is worth noting that, for customers who are impatient (i.e., their sensitivity-to-delay, a, is greater than the compensation rate, α), they will indeed switch to an ondemand instance rather than adopting a preemptible instance under the interruption-based scheme.

These <sup>fi</sup>ndings can shed some light on conditions in which the interruption-based scheme can outperform the uniform discount scheme from the provider’s perspective as, intuitively, in an environment whereby the majority of customers’ sensitivity-to-delay falls into the second interval, the interruption-based scheme can induce more demand compared with the uniformdiscount scheme. Because of the lack of a closed-form solution, we will reveal characteristics of such an environment in the next section through a comprehensive numerical study.

## 5. Numerical Study

In the previous section, we analyzed the provider’s optimal pricing decision under the uniform discount and interruption-based schemes, respectively. The customers’ willingness-to-pay and sensitivity-to-delay are assumed to be independent and uniformly distributed. Furthermore, we also established the equivalency of the two discount schemes from the provider’s perspective, given that the customers are risk neutral and have the same expectation of the preemption probability. In this section, we report our comprehensive numerical study to examine two important extensions to our base model. First, to show the robustness of the main insights obtained by our analytical results in Section 4, we use normal distributions to model the customers’ willingness-to-pay and sensitivity-to-delay. Second, we compare the uniform and interruption-based discount schemes in the presence of risk-averse customers. To this end, we extend our base model using the commonly used exponential utility function as discussed in Section 4.3.

The setting of the core test bed is as follows. Let the duration of one time unit be one day and let $w = 3 0 0$ (cents) per instance per day.<sup>9</sup> Initially, we let the customers’ willingness-to-pay $( \mathbf { i . e . , \textit { v } } )$ and sensitivity-todelay $( \mathrm { i } . \mathrm { e } . , a )$ follow two independent normal distributions. Speci<sup>fi</sup>cally, v follows a normal distribution with mean $\bar { E _ { v } } = 2 8 0$ and standard deviation $\sigma _ { v } \in \{ 2 0 , 4 0 , 6 0 \}$ and a follows another normal distribution with mean $E _ { a } = 1 6 0$ and standard deviation $\sigma _ { a } \in \{ 2 0 , 4 0 , 6 0 \}$ . We allow the two normal distributions to be correlated later in this section. Because the customers’ risk aversion is captured by an exponential utility function (see Equations (18) and (19) for details), let the parameter of the exponential utility function be $r = 0 . 0 0 5$

Moreover, in Online Appendix C, we present an expanded test bed in which the customers’ willingnessto-pay and sensitivity-to-delay follow two gamma distributions instead of normal distributions, and we also considered a larger range and combination of these parameter values to demonstrate that our <sup>fi</sup>ndings from the core test bed are robust.

We normalize the arrival rate of the fault-tolerant jobs to $\lambda { = } 1 0 0$ and that of the fault-intolerant jobs to $\lambda _ { 0 } = M _ { 0 } \lambda$ , where $M _ { 0 } \in \{ 0 . 5 0 , 0 . 7 5 , 1 . 0 0 , 1 . 5 0 , 2 . { \dot { 0 } } 0 \}$ . In addition, we assume that the workloads of the fault-tolerant and fault-intolerant jobs follow two independent exponential distributions with mean $\mu = 1 0$ and $\mu _ { 0 } = 3 0 ,$ respectively. Thus, $\sigma = \mu = 1 0$ and $\sigma _ { 0 } = \mu _ { 0 } = 3 0$

Recall that the total capacity of the instances, K, is equal to kλ. Let $k - M _ { 0 } \mu _ { 0 } = \kappa \mu$ and $\kappa \in \{ 1 . 0 , 1 . 1 , \cdot \cdot \cdot , 2 . 0 \}$ . The ratio of the average surplus capacity to the total capacity is $( k - M _ { 0 } \mu _ { 0 } ) / k = ( \kappa \mu ) / ( \kappa \mu + M _ { 0 } \mu _ { 0 } )$ . Thus, as κ increases from 1.0 to $2 . 0 ,$ the average percentage surplus capacity increases from 25% to 40%.

In total, we examine 495 cases in the core test bed, which cover a wide range of reasonable parameters and lead to meaningful results. In particular, under the uniform discount scheme, the optimal discount rate for a preemptible instance is up to 70% off the ondemand price, which is similar to the typical range of discount rates for the preemptible (or spot) instances in practice. The resulting average preemption probability ranges from 5.00% to 36.00% among all cases tested, thus covering the typical range of average preemption probabilities observed by GCP, fo which the “average preemption rate varies between 5% and 15% per day per project” and “occasionally spiking higher depending on time and zone” (see Endnotee 6).

First, we study the feasibility and attractiveness of offering the preemptible instances from the provider’s perspective. To this end, we identify cases that satisfy the following two conditions: (1) there exists an unbiased common belief about the average preemption probability, which converges to the system’s actual average preemption probability, given that the provider makes the optimal pricing decision in response to the customer’s common belief; and (2) the provider’s expected revenue with offering the preemptible instances is higher than that without such an offer.

The <sup>fi</sup>rst condition ensures that the provider will not exploit the customers’ lack of information about the preemption probability, or at least this is not the primary motive for the provider to offer the preemptible instances. The statement from GCP, for example, illustrates that the provider is also willing to truthfully reveal information in order to help customers form a correct common belief about the average preemption probability. The second condition ensures that the provider will be better off with the preemptible instances offered, compared with the baseline revenue without such an offer. In our model, the provider can choose not to offer the preemptible instances by setting $\beta = 1$ and $\alpha = 0$ under the uniform and interruption-based discount schemes, respectively. Thus, not offering the preemptible instances is always feasible but not necessarily the optimal solution for the provider.

Among the 495 cases examined, there are 402 and 465 cases under the uniform and interruption-based discount schemes, respectively, which satisfy the aforementioned two conditions. This result implies that the proposed interruption-based discount scheme can make the option of launching the preemptible instances more appealing to the provider. Furthermore, because the evidence clearly shows that the primary motive for cloud providers to offer the preemptible instances is to better use their random surplus capacities (as noted in the Introduction), we examine the in<sup>fl</sup>uence of the provider’s surplus capacity on the appeal of offering the preemptible instances. Recall that

$$
\begin{array}{c} \mathbf {E} [ S (t) ] = (k - M _ {0} \mu_ {0}) \lambda t = \kappa \mu \lambda t \text {and} \mathbf {V a r} [ S (t) ] \\ = M _ {0} (\mu_ {0} ^ {2} + \sigma_ {0} ^ {2}) \lambda t \end{array}
$$

In particular, as κ increases, the average surplus capacity will increase, whereas as the arrival rate of the fault-intolerant jobs $( \mathrm { i . e . , } M _ { 0 } )$ increases, the variance (volatility) of the surplus capacity will increase. In our numerical experiment, we allow κ and $M _ { 0 }$ to vary such that the mean and the variance (volatility) of the surplus capacity change accordingly. In general, we <sup>fi</sup>nd that when κ is very small and $M _ { 0 }$ is very large, the previous two conditions that de<sup>fi</sup>ne the provider’s decision to offer preemptible instances is dif<sup>fi</sup>cult to satisfy and vice versa. The observation is as follows.

Observation 1. When the surplus capacity is limited and highly volatile, it is not attractive for the provider to launch the preemptible instances.

Second, we examine the in<sup>fl</sup>uence of the surplus capacity on the provider’s optimal pricing decisions and the resulting average preemption probabilities under the two discount schemes. Again, we let k and $M _ { 0 }$ to vary such that the mean and the variance of the surplus capacity change accordingly. A close observation of all cases examined provides the following result.

Observation 2. As the average surplus capacity increases and/or the volatility of the surplus capacity decreases, the optimal discount rate under the uniform discount scheme should decrease, while the optimal compensation rate under the interruption-based discount scheme should increase. Moreover, under both schemes, the average preemption probability will decrease.

The provider responds differently to changes in the surplus capacity between the two discount schemes. Under the uniform discount scheme, as the mean (or volatility) of the surplus capacity increases (decreases), it is optimal for the provider to lower the discount rate; that is, the discount rate $1 - \beta$ should decrease, or equivalently, the discounted price βw should increase. Although such a pricing strategy seems to make the preemptible instances less attractive to customers, the negative effect of increasing the discounted price can be offset by the lower average preemption probability that results from the increase (decrease) in the mean (volatility) of the surplus capacity. In fact, we observe that the resulting demand for the preemptible instances always increases, and, thus, the total demand and the provider’s expected revenue also increase, which echoes the <sup>fi</sup>ndings in Proposition 2 based on our analytical results. In contrast, under the interruption-based discount scheme, as the mean (volatility) of the surplus capacity increases (decreases), it is optimal for the provider to raise the compensation rate. That is, α should increase, as the provider can afford to increase the compensation per interruption, given that the average preemption probability decreases. In Proposition 3, our analytical results also predict that, as the average preemption probability decreases, the provider should optimally increase the compensation rate accordingly under the interruption-based discount scheme.

Figure 3. Average Preemption Probabilities Under the UD and IB Schemes as the Average Surplus Capacity Increases  
![](/api/attachments/JC7XVMAY/fulltext/images/28c9cd54c28cf89ea3f2785773fb9d1634ecc11570a366a0124f654fd2e58456.jpg)  
Note. w <sub></sub> 300, E<sub>[</sub>v<sub>]</sub> <sub></sub> 280, σ<sub>[</sub>v<sub>]</sub> <sub></sub> 20, E<sub>[</sub>a<sub>]</sub> <sub></sub> 160, σ<sub>[</sub>a<sub>]</sub> <sub></sub> 20, µ <sub></sub> 10, µ <sub></sub> 30, M<sub>0 </sub> 1, and λ <sub></sub> 100.

To illustrate this observation, Figure 3 depicts the trend of the average preemption probabilities under the two discount schemes as the average surplus capacity increases. Similarly, Figure 4 depicts the discount rate and the compensation rate under the uniform discount (UD) scheme and the interruption-based (IB) scheme. In both <sup>fi</sup>gures, the x axis represents $\kappa \in \{ 1 . 0 , 1 . 1 , \cdots , 2 . 0 \}$ where $\kappa \mu = k - M _ { 0 } \mu _ { 0 } .$ . As noted earlier, as κ increases from 1.0 to 2.0, the average percentage surplus capacity increases from 25% to 40%.

Third, we compare the performance of the two discount schemes in terms of the expected revenue from the provider’s perspective. Speci<sup>fi</sup>cally, we examine in<sup>fl</sup>uences of the mean and variance of the surplus capacity on the relative advantage/disadvantage of the interruption-based scheme compared with the uniform discount scheme, de<sup>fi</sup>ned as $( \Pi ^ { I B } - \Pi ^ { U D } ) / \Pi ^ { U D }$

Figure 4. Optimal Discount Rate Under the UD Scheme and Optimal Compensation Rate Under the IB Scheme as the Average Surplus Capacity Increases  
![](/api/attachments/JC7XVMAY/fulltext/images/c549a0c3927488bb7c077eb9dd9a82f4e050375c9d19c8613624e5b0619c9b59.jpg)  
Note. w 300, E v 280, σ v 20, E a 160, σ a 20, µ 10, µ 30, M 1, and λ 100.

Figure 5. Impact of Increasing the Average Surplus Capacity on the Relative Advantage/Disadvantage of the Proposed IB Scheme Compared with the UD Scheme  
![](/api/attachments/JC7XVMAY/fulltext/images/8b14bc6ef384539403741b206183b75f0f22f8051dd5aea9292e04d13a29b37a.jpg)  
Note. w 300, E v 280, σ v 20, E a 160, σ a 20, µ 10, µ 30, M 1, and λ 100.

Observation 3. As the mean (volatility) of the surplus capacity decreases (increases), the interruption-based scheme is more likely to outperform the prevalent uniform discount scheme.

Figures 5 and 6 illustrate the relative advantage or disadvantage of the interruption-based scheme as compared with the uniform discount scheme as the mean or the volatility of the surplus capacity increases, respectively. Speci<sup>fi</sup>cally, the x axis in Figure 5 represents κ, where $\kappa \mu = \left( k - M _ { 0 } \mu _ { 0 } \right)$ , and as κ increases, the average surplus capacity increases. When $\kappa \leq 1 . 3 ,$ which implies that the average surplus capacity is less than 30%, our proposed scheme outperforms the commonly used uniform discount scheme. Similarly, the x axis in Figure 6 represents $M _ { 0 } ,$ and as $M _ { 0 }$ increases, the variance of the surplus capacity increases. The coef<sup>fi</sup>- cient of variation of the surplus capacity, $c v ,$ is equal to $( \sqrt { M _ { 0 } ( \mu _ { 0 } ^ { 2 } + \sigma _ { 0 } ^ { 2 } ) \lambda } ) / ( \kappa \mu \lambda )$ . Thus, when $M _ { 0 } \geq 1 . 0$ , which implies $c v \geq 1 1 \%$ , our proposed scheme outperforms the commonly used uniform discount scheme.

To explain the underlying rationale for Observation $^ { 3 , }$ we recall our <sup>fi</sup>ndings based on (22). That is, customer who are very patient will <sup>fi</sup>nd the uniform discount scheme more attractive, whereas customers who are moderately patient will <sup>fi</sup>nd the interruption-based discount scheme more attractive. The changing environment (i.e., the surplus capacity and the preemption probability) will have little impact on the former but may have a considerable in<sup>fl</sup>uence on the latter, especially when the mean (volatility) of the surplus capacity is relatively low (high) and the resulting average preemption probability is relatively high. In such cases, customers with moderate patience would be better off under the interruption-based discount scheme, which gives the provider a strong incentive to switch to the proposed scheme.

Figure 6. Impact of Increasing the Volatility of the Surplus Capacity on the Relative Advantage/Disadvantage of the Proposed IB Scheme Compared with the UD Scheme  
![](/api/attachments/JC7XVMAY/fulltext/images/cd1256974a10e3024492ad2d523d6d7a96697dab0fa3ce2d8c26f650a6f018d7.jpg)  
Note. w 300, E v 280, σ v 20, E a 160, σ a 20, µ 10, µ 30, κ 1:3, and λ 100.

Figure 7. Impact of Correlation Between the Customers’ Willingness-to-Pay and Sensitivity-to-Delay on the Relative Advantage/Disadvantage of the IB Scheme Compared with the UD Scheme  
![](/api/attachments/JC7XVMAY/fulltext/images/60ad4f4a46a8ca2002aafe774c5c0809837a14534fe33b8e9bcbb13757621bfd.jpg)  
Note. w <sub></sub> 300, E<sub>[</sub>v<sub>]</sub> <sub></sub> 280, σ<sub>[</sub>v<sub>]</sub> <sub></sub> 40, E<sub>[</sub>a<sub>]</sub> <sub></sub> 160, σ<sub>[</sub>a<sub>]</sub> <sub></sub> 40, µ <sub></sub> 10, µ <sub></sub> 30, κ <sub></sub> 1:2, M<sub>0 </sub> 1, and λ <sub></sub> 100.

Finally, we examine the impact of the correlation between the customers’ willingness-to-pay (i.e., v) and sensitivity-to-delay $( \mathrm { i } . \mathrm { e } . , a )$ . We assume that the pair of (v, a) follows a bivariate normal distribution with correlation $\rho \in \{ - 0 . 7 5 , - 0 . 5 0 , - 0 . 2 5 , 0 , 0 . 2 5 , 0 . 5 0 , 0 . 7 5 \}$ , while keeping the marginal distributions of v and a the same as before. Note that a larger value of the sensitivity-to-delay means that the customer is less tolerant of interruptions. Thus, a positive (negative) correlation implies that a customer with a higher willingness-to-pay is likely to be less (more) patient with the interruptions.

Observation 4. As the correlation between the customers’ willingness-to-pay and sensitivity-to-delay increases, the relative advantage of the interruptionbased scheme shrinks.

Figure 7 illustrates the trend as described by the previous observation. Notably, the positive correlation between the customers’ willingness-to-pay and sensitivity-to-delay diminishes the relative advantage of the interruption-based scheme. An intuitive explanation is as follows. Because of the positive correlation, customers with very high willingness-to-pay also are very impatient, and thus, they will use an on-demand instance anyway. Conversely, customers with very low willingness-to-pay are also very patient; such customers, however, will <sup>fi</sup>nd the uniform discount scheme more attractive than the interruption-based scheme, as noted in the explanation for Observation 3. In other words, the interruption-based scheme has an advantage of attracting customers with low willingness-to-pay and moderate patience, whereas such a customer base shrinks in the presence of a positive correlation between the willingness-to-pay and sensitivity-to-delay.

## 6. Conclusion and Recommendations for Future Research

As the public cloud services are emerging as a major marketplace, cloud providers are facing tremendous opportunities and challenges in pricing and managing capacity of computing resources. Some cloud providers have launched low-priority service with preemptible or spot instances to increase the use levels of their surplus capacities. In this paper, we focused on three main research questions. (1) When is launching the low-priority service appealing to a provider? (2) Under the commonly used uniform discount scheme, how should the provider determine the optimal discounted price? Under the proposed interruption-based scheme, how should the provider determine the optimal compensation rate? (3) In which business environment does the proposed scheme outperform the prevalent uniform discount scheme?

We developed an analytical framework, whereby a cloud provider is faced with a population of customers with fault-tolerant jobs. Because of the lack of real-time information, the customers do not have an accurate estimate of the cloud platform’s dynamic preemption probability. That said, they can form a common belief about the average preemption probability, which can be estimated based on historical preemption frequency observed by a third party or the provider himself. We <sup>fi</sup>rst formulated the provider’s revenue-maximization problem based on any customers’ common belief about the average preemption probability. We then derived the average preemption probability in an equilibrium that arises from customers’ rational expectation of the preemption probability.

To answer the <sup>fi</sup>rst question, our results revealed that, when the provider has ample and stable surplus capacity (i.e., the average surplus capacity is large and the volatility of the surplus capacity is low), then launching a lowpriority service is appealing to the provider. Nevertheless, the provider needs to be mindful of the cannibalization effect of launching a low-priority service, especially when a large portion of the customers with fault-tolerant jobs have relatively high willingness-to-pay and would have used an on-demand instance otherwise.

To address the second question, we derived the optimal discount rate under the uniform discount scheme and the optimal compensation rate under the proposed interruption-based scheme, under an assumption that customers’ willingness-to-pay and sensitivity-to-delay follow two independent uniform distributions. We also found that the optimal compensation rate of the proposed scheme should be a decreasing function of the average preemption probability. When the assumption of independence and uniformity of the distributions is relaxed, we examined the robustness of these results through a comprehensive numerical study employing a bivariate normal distribution.

To answer the third question, we <sup>fi</sup>rst showed that, as long as the provider interrupts the preemptible instances randomly and the customers are risk neutral, they will have the same expectation of the preemption probability. As a result, the uniform and the interruption-based schemes are, indeed, equivalent from the perspective of the provider. The proposed scheme, however, is fairer than the uniform discount scheme for the customers, as the former gives discounts (in the form of compensation) to customers based on the actual occurrence of interruptions. Furthermore, in the presence of risk-averse customers, we derived the following managerial insights:

When the average surplus capacity is very high and its volatility is very low, the provider would be better off adopting the uniform discount scheme. Conversely, when the average surplus capacity is very low and its volatility is very high, the provider would indeed be better off not offering the preemptible instance, and thus there is no need to adopt a discount scheme.

When the average surplus capacity is moderately high and its volatility is moderately low, the provider would be better off adopting the proposed interruption-based scheme, but the provider should be mindful of a positive correlation between the customers’ willingness-to-pay and sensitivity-to-delay as it diminishes the relative advantage of the proposed scheme.

Finally, we acknowledge that this research has some limitations, and addressing them can lead to valuable research opportunities. For instance, although our model can partly capture the effect of competition with another provider by assuming that the customers have an outside option, explicitly modeling the competition among multiple providers in the preemptible (spot) instance market segment will give rise to more valuable results. Moreover, by proposing the practical interruption-based scheme, this study attempts to <sup>fi</sup>ll in the gap in the research that exists between the two extremes of the spectrum: the simple yet transparent uniform discount scheme at one end and the sophisticated yet opaque spot-pricing scheme at the other end. We acknowledge that there is still considerable room for designing practical discount schemes. For instance, instead of <sup>fi</sup>xing the discount rate or compensation rate, as in this paper, one could extend our model to a simple dynamic discount scheme, whereby the discounted price varies between two modes: a higher price when there are preemptions and a lower price when there are no preemptions. Comparing such a scheme to the two extremes of the spectrum is a worthwhile future research endeavor.

## Acknowledgment

The authors thank the senior editor, associate editor, and two anonymous reviewers for thoughtful and constructive suggestions throughout the review process.

## Endnotes

<sup>1</sup> See https://azure.microsoft.com/en-us/blog/low-priority-scale -sets, accessed on Nov 13. 2019

<sup>2</sup> See https://cloud.google.com/compute/docs/instances/preemptible, accessed on Nov 13, 2019.

<sup>3</sup> See https://cloud.google.com/preemptible-vms/, accessed on Nov 13, 2019.

<sup>4</sup> See https://azure.microsoft.com/en-us/blog/low-priority-scale-sets, accessed on Nov 13, 2019.

<sup>5</sup> See https://cloud.google.com/preemptible-vms/, accessed on Nov 14, 2019.

<sup>6</sup> See https://cloud.google.com/compute/docs/instances/preemptible, accessed on Nov 13, 2019.

<sup>7</sup> If $p ^ { U D } \leq 0$ or $p ^ { U D } \geq 1$ , then the equilibrium does not exist in the reasonable range, but if $0 < p ^ { U D } < \bar { 1 , }$ then it is the unique equilibrium that would arise from the customers’ rational expectation of the average preemption probability.

<sup>8</sup> Here, we consider the specific interruption-based scheme as in Section 4.2, where the compensation is α per interruption (or per unit time of delay), because the analysis for other forms of compensation schemes is similar.

<sup>9</sup> For instance, the daily price of a standard E2 virtual machine at GCP with two or four virtual CPUs and 8- or 16-GB memory ranges from \$1:93 to \$3:86 per day.

## References

Afeche P (2013) Incentive-compatible revenue management in\` queueing systems: Optimal strategic delay. Manufacturing Service Oper. Management 15(3):423–443.

Agmon Ben-Yehuda O, Ben-Yehuda M, Schuster A, Tsafrir D (2013) Deconstructing Amazon EC2 spot instance pricing. ACM Trans. Econom. Comput. 1(3):16.

Avi-Itzhak B, Levy H, Raz D (2008) Quantifying fairness in queuing systems: Principles, approaches, and applicability. Probabilities Engrg. Inform. Sci. 22(4):495–517.

Basu A, Bhaskaran S (2018) An economic analysis of customer co-design. Inform. Systems Res. 29(4):787–786.

Chen YJ, Huang KW (2016) Pricing data services: Pricing by minutes, by Gigs, or by Megabytes per second? Inform. Systems Res. 27(3):596–617.

Chen S, Lee H, Moinzadeh K (2019) Pricing schemes in cloud computing: Utilization-based vs. reservation-based. Production Oper. Management 28(1):82–102.

Cheng HK, Li Z, Naranjo A (2016) Research note: Cloud computing spot pricing dynamics: Latency and limits to arbitrage. Inform. Systems Res. 27(1):145–165.

CloudHealth by VMWare (2018) A look at Azure vs AWS pricing in 2018-2019. Accessed October 28, 2019, https://www .cloudhealthtech.com/blog/azure-vs-aws-pricing.

Deneckere RJ, McAfee RP (1996) Damaged goods. J. Econom. Man agement Strategy 5(2):149–174.

Deng T, Chen YJ, Shen ZJM (2015) Optimal pricing and scheduling control of product shipping. Naval Res. Logist. 62(3):215–227.

Dierks L, Seuken S (2021) Cloud pricing: The spot market strikes back. Management Sci., ePub ahead of print February 25, https://pubsonline.informs.org/doi/10.1287/mnsc.2020.3907.

Gao J, Iyer K, Topaloglu H (2019) When <sup>fi</sup>xed price meets priority auctions: Competing <sup>fi</sup>rms with different pricing and service rules. Stochastic Systems 9(1):47–80.

Gartner Newsroom (2018) Gartner forecasts worldwide public cloud revenue to grow 17.3% in 2019. Accessed October 9, 2018, https://www.gartner.com/en/newsroom/press-releases/.

Gross D, Shortle JF, Thompson JM, Harris CM (2008) Fundamentals of Queueing Theory, 4th ed. (John Wiley & Sons, Inc., Hoboken, NJ).

Harrison JM (2013) Brownian Models of Performance and Control (Cambridge University Press, Cambridge, UK).

Hassin R, Haviv M (2003) To Queue or Not to Queue: Equilibrium Behavior in Queueing Systems, vol. 59 (Springer Science & Business Media, New York).

Heyman DP, Sobel MJ (1982) Stochastic Models in Operations Research (Dover Publications, Mineola, NY).

Joe-Wong C, Sen S (2018) Harnessing the power of the cloud: Revenue, fairness, and cloud neutrality. J. Management Inform. Systems 35(3):813–836.

Jones R, Mendelson H (2011) Information goods vs. industrial goods: Cost structure and competition. Management Sci. 57(1): 164–176.

Kao EP (1997) An Introduction to Stochastic Processes (Duxbury Press).

Kepes B (2015) 30% of servers are sitting “comatose” according to re search. Accessed November 12, 2017, https://www.forbes.com/ sites/benkepes/2015/06/03/30-of-servers-are-sitting-comatose -according-to-research/#5cd4c69859c7.

Kilcioglu C, Maglaras C (2015) Revenue maximization for cloud computing services. Performance Evaluation Rev. 43(3):76.

Kingman JF (1962) On queues in heavy traf<sup>fi</sup>c. J. Royal Statist. Soc. B 24(2):383–392.

Larson RC (1987) OR Forum—Perspectives on queues: Social justice and the psychology of queueing. Oper. Res. 35(6):895–905.

Lederer PJ, Li L (1997) Pricing, production, scheduling, and deliverytime competition. Oper. Res. 45(3):407–420.

Li B, Kumar S (2018) Should you kill or embrace your competitor: Cloud service and competition strategy. Production Oper. Management 27(5):822–838.

Li Z, Zhang H, O’Brien L, Jiang S, Zhou Y, Kihl M, Ranjan R (2016) Spot pricing in the cloud ecosystem: a comparative investigation. J. Systems Software 114:1–19.

Ma D, Seidmann A (2015) Analyzing software as a service with pertransaction charges. Inform. Systems Res. 26(2):360–378.

Maglaras C, Zeevi A (2005) Pricing and design of differentiated services: Approximate analysis and structural insights. Oper. Res. 53(2):242–262.

Maister DH (1984) The Psychology of Waiting Lines (Harvard Business School, Boston, MA).

Mehta S, Dawande M, Janakiraman G, Mookerjee V (2019). How to sell a dataset? Pricing policies for data monetization. Inform. Systems Res. Forthcoming.

Mendelson H, Whang S (1990) Optimal incentive-compatible priority pricing for the M/M/1 queue. Oper. Res. 38(5):870–883.

Oxford Economics and SAP (2014) The cloud grows up. Accessed April 28, 2018, https://www.oxfordeconomics.com/recentreleases/the-cloud-grows-up.

Ozer O, Phillips R (2012)<sup>¨</sup> The Oxford Handbook of Pricing Management (Oxford University Press, Oxford, UK).

Samimi P, Patel A (2011) Review of pricing models for grid & cloud computing. 2011 IEEE Sympos. Comput. Informatics, Kuala Lumpur, Malaysia, 634–639.

Schonberg Z (2019) Understanding excess capacity: Amazon EC2 spot vs. Azure low-priority VM vs. Google preemptible VM vs IBM transient servers. Accessed October 15, 2019, https://spotinst.com/blog/.

Song D (2018) Three best practices for digital transformation. Accessed October 23, 2018, https://www.ibm.com/blogs/cloud -computing/2018/05/03/3-best-practices-digital-transformation.

Talluri KT, Van Ryzin GJ (2006) The Theory and Practice of Revenue Management (Springer Science & Business, New York).

Toosi AN, Vanmechelen K, Khodadadi F, Buyya R (2016) An auction mechanism for cloud spot markets. ACM Trans. Autonomous Adaptive Systems 11(1):1–33.

Xu H, Li B (2013) Dynamic cloud pricing for revenue maximization. IEEE Trans. Cloud Comput. 1(2):158–171.

Yuan S, Das S, Ramesh R, Qiao C (2018) Service agreement trifecta: Backup resources, price and penalty in the availability-aware cloud. Inform. Systems Res. 29(4):947–964.

Zhang Z, Joseph K, Subramaniam R (2015) Probabilistic selling in quality-differentiated markets. Management Sci. 61(8):1959–1977.

Zheng L, Joe-Wong C, Tan CW, Chiang M, Wang X (2015) How to bid the cloud. Comput. Comm. Rev. 45(4):71–84.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
