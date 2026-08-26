---
otero_id: 366
otero_key: "FTUGBPE6"
title: "A Switch in Time Saves the Dime: A Model to Reduce Rental Cost in Cloud Computing"
authors: "Leila Hosseini; Shaojie Tang; Vijay Mookerjee; Chelliah Sriskandarajah"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0912"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/FTUGBPE6/fulltext/images/0817383e0bb57b463635fe92aa14b320f5ff215e4cbd0321b22e491a746d554e.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## A Switch in Time Saves the Dime: A Model to Reduce Rental Cost in Cloud Computing

Leila Hosseini, Shaojie Tang, Vijay Mookerjee, Chelliah Sriskandarajah

To cite this article:

Leila Hosseini, Shaojie Tang, Vijay Mookerjee, Chelliah Sriskandarajah (2020) A Switch in Time Saves the Dime: A Model to Reduce Rental Cost in Cloud Computing. Information Systems Research

Published online in Articles in Advance 04 Aug 2020

https://doi.org/10.1287/isre.2019.0912

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Switch in Time Saves the Dime: A Model to Reduce Rental Cost in Cloud Computing

Leila Hosseini,<sup>a</sup> Shaojie Tang,<sup>b</sup> Vijay Mookerjee,<sup>b</sup> Chelliah Sriskandarajah<sup>c</sup>

<sup>a</sup> Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122; <sup>b</sup> University of Texas at Dallas, Richardson, Texas 75080; <sup>c</sup> Texas A&M University, College Station, Texas 77843

Contact: leila.hsei@gmail.com (LH); shaojie.tang@utdallas.edu, https://orcid.org/0000-0001-9261-5210 (ST); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VM); chelliah@mays.tamu.edu (CS)

Received: Revised: November 8,<sub>Accepted:</sub> Published Online in Articles in Advance: August 4, 2020

https://doi.org/10.1287/isre.2019.0912

Copyright:

Abstract. The goal to continually reduce operating costs while meeting computational needs is common to all modern organizations that use cloud computing. We study the problem of selecting computing resources with the goal of minimizing the total rental cost of completing a computing task in the presence of a time constraint. The problem is formulated as a scheduling problem that assigns computing resources to time periods of the planning horizon (time available to complete a single computing task). This (NP-hard) preemptive-resume type scheduling problem—new to the scheduling literature—has not been carefully addressed in practice to provide an implementable solution. Typically, the approach taken in practice is to use a single resource (a single virtual machine instance, or a cluster of identical virtual machine instances) to complete a computing task. The main insight of this study is that rather than completing a computing task using a single computing resource, rental costs can be significantly lowered by using a few resources (sometimes even just two) to complete the task. Thus, the computing task is switched from one resource to another to exploit the cloud provider’s price-performance schedule. Cloud computing has been recognized as an economically attractive computing environmen whose adoption has been growing over time. However, providers (such as Amazon Web Services) offer a confusing and diverse set of computing resources with different configurations and unit rental costs. Our near-optimal solution is based on switching the computing task from one resource to another in way that leverages the relationship between the price and performance of the available computing resources. The performance of a given resource can vary randomly as well as be correlated with the performance of another (stronger or weaker) resource. We present a worst-case performance guarantee of the proposed solution. In addition, we study the performance using a detailed com putational study and a real-world example of an actual company that can benefit from our proposed solution. In the computational study as well as the real-world example, the cost of our solution is usually about 15%–25% lower than the benchmark solution of using the best single computing resource to process the computing task. Practicing information technology managers can use our approach to migrate in-house solutions to the cloud in a cost-effective manner.

History: D. J. Wu, Senior Editor; Martin Bichler, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0912.

Keywords: cloud computing • total rental cost minimization • near-optimal solution

## 1. Introduction

Cloud computing has been recognized as an important computing environment whose adoption has been growing over time. According to International Data Corporation (IDC), worldwide spending on public cloud computing will grow from \$67 billion in 2015 to \$162 billion in 2020, garnering a compound annual growth rate (CAGR) of 19% (Gantz and Miller 2016). Gartner (2017) predicts that the worldwide public cloud services market will grow 18% in 2017 to \$246.8 billion, up from \$209.2 billion in 2016. According to a global survey of 200 business and technology executives conducted by Oxford Economics and SAP, more than two-thirds (69%) of businesses expect to increase their migration of core business functions to the cloud in the next few years (Oxford Economics and SAP 2015).

Cloud computing providers offer a wide variety of computing resources for users to process varied computing tasks. There are several major providers in the cloud market, with Amazon Web Services (AWS) as the leader, and Microsoft, Google, and IBM as fierce competitors of AWS (Synergy Research Group 2016). Data from Synergy Research Group shows in the third quarter of 2016, AWS, Microsoft, Google, and IBM controlled well over half of the worldwide cloud market, and AWS dominated the worldwide public cloud computing market, enjoying 45% of the market share (Synergy Research Group 2016). AWS’s third quarter revenue in year 2017 was \$3.66 billion, compared with \$2.56 billion during the same period in 2016, attaining a 43% year-over-year growth (Columbus 2017).

Cloud computing users are businesses and enterprises that rent computing resources and storage over the Internet, instead of owning them. Cloud computing tasks are typically of two broad kinds: real time and offline. Computing tasks such as real-time bidding and running an e-commerce website are examples of real-time computing tasks. Offline computing tasks (e.g., log file processing) can be fixed or variable sized. In either case, offline computing tasks usually come with a deadline. This study is concerned with reducing the rental cost of frequently occurring fixedsized offline computing tasks. Offline data analysis is an example of a common fixed-sized-with-deadline computing task that is often processed in the cloud. International Data Group, Inc. (IDG) reports that about 15% of the 200 information technology (IT) and business decision makers surveyed have developed one or more cloud-based data analysis solutions, and 68% of them want to investigate, examine, or seriously plan to develop cloud solutions in the near future. Vince Dell’Anno, managing director of Accenture Analytics, identifies several advantages of cloud-based data analytics, such as increase in return on investment, agility, and pace of innovation (McKendrick 2016). Some practical examples of cloud-based offline data analysis are clickstream analysis, log file processing, posttrade analysis, genomic analysis and clinical studies, and video/image processing.

## 1.1. Motivation of Problem

According to the seventh annual state of the cloud survey conducted by RightScale, optimizing cloud computing costs was the top initiative again in 2018, increasing to 58% from 53% in 2017 (Weins 2018). On the other hand, there was a significant reduction in security concerns among enterprise central technology teams, who are usually responsible for security. Instead, these groups consider cost optimization as the main concern (MSV 2018). However, even though reducing cloud computing costs is a top challenge, users often underestimate the amount of wasted cloud computing spend (Weins 2018).

Industry experts state that cloud providers have confused users by offering a large number of computing resources with different configurations and prices (Harris 2015). For a cloud computing user, it is difficult to choose among the variety of offerings and the complicated price-performance relationships.

Typically, the approach taken in practice is to use a single resource to complete a computing task (Reddy and Sarkar 2015, Quora 2016, Cidewalk 2017). As will become clear soon, the cloud computing user can benefit from using a few resources instead of using a single one. Under the single-resource approach, the cloud com puting user selects the cheapest resource among those that can complete a computing task by a specified deadline. We highlight inefficiency in the single-resource approach and the need for a procedure to generate an efficient solution via a simple but illustrative example.

Assume there is a cloud computing provider that offers two resources: a low-performance one and a high-performance one. The computing performance of a resource can be measured as the fraction of the computing task processed by the resource in one hour. Let us assume that the computing performance and hourly rental cost of these resources are 0.125 and \$2 (for low performance), and 0.25 and \$6 (for high performance). Consider a computing task with a deadline of six hours. The best single-resource solution that is feasible to solve this problem is to use the high-performance resource, which completes the computing task in four hours $( 0 . 2 5 \times 4 \geq 1 )$ at a rental cost of \$24. A better solution is to use the highperformance resource for three hours and the lowperformance resource for two hours (0.25 3 + 0.125 $\bar { 2 } \geq 1 )$ ). The rental cost of this (multiple-resource) solution is \$22, which is lower than the cost of the best single-resource solution. In both solutions, the high performance resource is used for three hours. However, in the new solution, a weaker and cheaper resource (i.e., the low-performance resource) is used to complete the rest of the computing task.

The best solution for this problem is to use the highperformance resource for the first two hours and then use the weaker resource (low-performance resource) for the next four hours $( 0 . 2 5 \times 2 + 0 . 1 2 5 \times 4 \geq 1 )$ ). The rental cost for this solution is \$20. The multipleresource solution lowers the rental cost by exploit ing a concave relationship between the computing performance of a resource and its hourly rental cost. However, the cloud user might face an additional cost when the computing task is switched from one resource to a different one. Therefore, the savings obtained from using multiple resources must be balanced against the switching cost.

In general, it is easy to see that there could be many feasible solutions to the problem (we show later that the problem is NP-hard) so finding the best solution using enumeration is not likely to work for most realworld problems. Thus, cloud users need efficient procedures to find the set of resources to use and the length of time to deploy each resource, so that the computing task can be completed before or by a specified deadline at minimum rental cost.

## 1.2. Problem Description

Consider a situation where the cloud service provider offers a variety of virtual machine (VM) instances to choose from. Cloud users can create clusters from the available VM instances, where a cluster consists of one master VM and one or more slave VMs. Thus, a computing resource in this study refers to a specific VM instance or a cluster of VM instances created by the user.

Given a set of available computing resources, we wish to optimize the rental cost for processing a frequently occurring, fixed-sized computing task with a deadline. Specifically, a fixed-sized computing task is a computing task where the instances of the task are of similar complexity. Each instance needs to be completed within a specified amount of time. Specifically, we ask: How should a subset of computing resources be selected to process a single computing task so as to minimize the total rental cost while respecting a deadline constraint. A key aspect of solving the stated problem is that a subset of resources (rather than a single resource) is used to process the computing task.

## 1.3. Novelty of the Problem

In this study, we present a preemptive-type scheduling problem with features that are new to this class of scheduling problems. The problem definition, the objective criterion (total rental cost), new features such as the preemption-resumption of the computing task at unit time intervals, the deadline constraint, and the complexity of the problem give rise to a scheduling problem with new structural properties, different from those in the classical scheduling literature.

The novelty of our problem compared with scheduling problems in other environments such as grid computing, distributed systems, multiprocessor systems, and cloud computing can be summarized as follows. First, previous study in distributed systems/grid computing/multiprocessor systems has largely ignored the cost of renting computing resources. Most scheduling problems in cloud computing also do not consider rental cost. Second, unlike our problem, where a task’s execution time is random, the execution time of each task is assumed to be fixed and known in scheduling problems in cloud computing. Finally, our problem explicitly incorporates the cost of switching a computing task from one resource to another during the course of processing. Thus, the combination of problem features studied here has not been studied before.

## 1.4. Our Contributions

1.4.1. Theoretical Contributions. We formulate a model to solve the problem of minimizing the cost of renting computing resources that can complete a fixed-sized, offline task with a deadline constraint. The solution proposed is near optimal and efficient—one that can be found in a few seconds—for realistic sized problems. We also provide a theoretical worst-case performance guarantee for our proposed solution and numerically study its computational performance and cost. To demonstrate the cost savings of our proposed solution, we use the cost of the best singleresource solution as a benchmark. Our computational results show that our near-optimal solution can generate substantial savings (around 25%) over the best singleresource solution.

1.4.2. Practical Contributions. Cloud computing is being widely adopted by the business world for its technological, economic, and operational benefits. Thus, lowering cloud computing costs can potentially provide huge efficiency gains. This research contributes by providing a formal representation of a real-world problem encountered by a large number of firms across different industries. Our proposed solution is easy to implement in practice. Near the end of this paper, we illustrate how our approach can be applied to a real-world example of cloud-based offline data analysis, namely, the log file processing problem encountered by Cidewalk, a mobile ad delivery platform.

Our proposed approach can also be used by cloud brokers to navigate the complicated cloud market on the cloud user’s behalf to gain the best value while meeting business objectives. In the cloud computing market, cloud brokers are third-party organizations that act as intermediaries between cloud computing providers and users. They assist cloud users by providing the tools and expertise to choose the most effective cloud service, in terms of performance and price. MarketsandMarkets estimates that the cloud service broker market will grow from \$6.78 billion in 2018 to \$15.03 billion in 2021, at a CAGR of 17.3% during the forecast period (Markets and Markets 2018).

## 1.5. Organization of the Paper

The rest of this paper is organized as follows. In Section 2, we describe related studies. The cloud user’s problem is described in Section 3, and its mathematical formulation and analysis is presented in Section 4. Section 5 presents two model extensions. An extensive computational study is presented in Section 6. The applicability of our approach for a real problem is discussed in Section 7. Section 8 concludes the study.

## 2. Related Literature

This research is related to the literature on scheduling This section describes closely related scheduling problems in the areas of manufacturing and computer systems, grid computing, distributed systems, multiprocessor systems, and cloud computing.

## 2.1. Manufacturing and Computer Scheduling Literature

For an introduction to machine scheduling theory, the reader may refer to Pinedo (2016). An introduction to computational complexity can be found in the study of Garey and Johnson (1979). In a pioneering study, Lenstra et al. (1977) study and classify the complexity status of a wide variety of scheduling problems. Scheduling problems are basically optimization problems that allocate resources (i.e., machines) to activities known as jobs. These problems are encountered in both manufacturing (Pinedo 2016) and computing (Blazewicz et al. 2013) environments.

A typical static scheduling problem over a planning horizon can be stated as follows. There are n jobs denoted by $\{ J _ { k } | k = 1 , 2 , \ldots , n \}$ that require processing on m machines denoted by $\{ M _ { i } | i = \bar { 1 } , 2 , \bar { . } . . , m \}$ in a shop. These jobs are available at time zero. The objective is to optimize a certain criterion such as the makespan, the total job tardiness penalty, and so on, subject to various constraints, for example, on processing technology or job characteristics.

The terminology used in the scheduling literature follows the classification $\alpha _ { s } | \beta _ { s } | \gamma _ { s }$ of scheduling problems suggested by Graham et al. (1979), where $\alpha _ { s }$ indicates the machine environment $( \mathrm { e . g . } , P 2$ for two parallel machines), $\beta _ { s }$ denotes the job characteristics or restrictive requirements (e.g., different release times of jobs are specified), and $\gamma _ { s }$ is the optimality criterion $( \mathrm { e . g . } ,$ , makespan, total tardiness, etc.). Most manufacturing scheduling problems deal with nonpreemptive scheduling in the sense that once the job is assigned to a machine for a task, it must be completed before it is removed from the machine. However, in preemptiveresume scheduling problems (primarily found in the computer science domain), a task of a job on a machine can be preempted and resumed at a later time (Blazewicz et al. 2013).

The scheduling literature is vast and we review only those problems that are closely related to the problem considered in this paper. This problem is new and has not been investigated in the literature. The closest to our problem is the uniform parallel machines problem (denoted Q), which is a generalized version of parallel machine scheduling (denoted P). However, our problem is significantly different, as we describe later. The common uniform parallel machines problem treated in the literature, denoted as $Q m \parallel C _ { \operatorname* { m a x } } ^ { - } ,$ has m machines $\{ M _ { 1 } , M _ { 2 } , . . . , M _ { m } \}$ with speeds $v _ { 1 } < v _ { 2 } < \ldots < v _ { m }$ , respectively. There are n jobs $\{ J _ { k } | k = 1 , 2 , \ldots , n \}$ that have to be scheduled on those machines such that a machine can process only one job at a time, and a job can be processed by only one machine at a time. The processing time of job $J _ { k }$ is $p _ { k }$ on the slowest machine (M ) and the processing time on the other machines is proportional to their speed. The optimality criterion is to find the schedule that minimizes makespan, $C _ { \mathrm { m a x } } .$ . In preemptiveresume version of the presented problem (denoted by $Q m | p m t n | C _ { \mathrm { m a x } } )$ , a job on a machine can be preempted at any time and resume at a later time on any of m machines. Our problem is similar to that of $Q m | p m t n | C _ { \mathrm { m a x } }$ . However, in our problem, there is only one $\mathrm { j o b } \ ( n = 1 )$ ) and the objective function is not the makespan but the total cost of processing the job Moreover, the preemptive-resumption of a job can only be done at discrete time units and the job must be completed on or before time limit T. As will be seen in the subsequent sections, these new features (such as objective criterion [total cost], preemptionresumption of the computing task at unit time intervals, and the time limit constraint T) give rise to a new scheduling problem domain with new structural properties, different from those studied in the literature. Moreover, problem $Q m | p m t n | C _ { \mathrm { m a x } }$ is polynomially solvable (Graham et al. 1979, Pinedo 2016), whereas our problem is shown to be NP-hard.

Other preemptive scheduling models have been studied in the literature. Gonzalez and Sahni (1976) propose a polynomial-time algorithm for $O m | p m t n | C _ { \mathrm { m a x } } .$ Lawler and Labetoulle (1978) show that $R m | p m t n | C _ { \mathrm { m a x } }$ (the unrelated parallel machines problem) can be formulated and solved as linear programming problem. The reader may refer to (Blazewicz et al. 2013, Pinedo 2016) for details about the various other problems considered in the literature.

## 2.2. Scheduling Problems in Grid and Cloud Computing

During the past few decades, task scheduling problems have been extensively studied both experimentally and theoretically for distributed systems (Kartik and Murthy 1995, Braun et al. 2001, Hsieh 2003, Stavrinides and Karatza 2011, Zhang et al. 2016), grid computing (Navimipour and Khanli 2008, Kumar et al. 2009, Kokilavani et al. 2011, Shojafar et al. 2013), and multiprocessor systems (Mahmood 2000, Davis and Burns 2011, Qamhieh et al. 2013). This literature ignores the rental cost of computing. However, reducing rental cost, a key concern for users of commercial cloud services, is the main driver for our study (Liu et al. 2010, Cheng et al. 2016).

Unlike the studies in the previous streams, studies on VM scheduling in cloud computing can be categorized into two broad groups of problems: non-costaware and cost-aware VM scheduling problems. Despite a large body of literature on VM scheduling in cloud computing (Wu et al. 2013, Awad et al. 2015, Chen et al. 2015, Panda et al. 2015, Liu et al. 2016, Sangwan et al. 2016), the majority of studies do not consider the rental cost of computing resources. These studies focus on optimizing objectives such as makespan/memory usage/energy consumption minimization (Buyya et al. 2010, Tsai et al. 2014, Peng et al. 2017), efficiency/utilization maximization (Younge et al. 2010, Wang et al. 2015), and load balancing (Zhang et al. 2011). For example, Aymerich et al. (2009) present a preliminary design of a real-time financial system based on grid and cloud computing. This paper only gives a high-level overview of their system design, and many technical details such as task scheduling are not covered. Tsai et al. (2010) study real-time partitioning of database tasks in a cloud environment, but do not consider rental cost. Wu et al. (2013) study the task scheduling problem based on several quality-of-service (QoS) metrics, including load balancing, average latency, and makespan. They propose a priority-based scheduling algorithm whose performance is verified experimentally. Tsai et al. (2014) propose a hyper-heuristic algorithm to schedule tasks on a cloud computing resource and their objective is to minimize makespan. Our paper differs from these in that we explicitly deal with the real-time task scheduling problem (real-time task scheduling is a problem in which jobs have deadlines) in a cloud environment to minimize the cost of rented computing resources.

Previous studies on cost-aware VM scheduling can be classified into two categories: (1) optimizing virtual resource selection from the user’s perspective, and (2) optimizing virtual resource configuration from the service provider’s perspective. For example, one example is to design a low-cost mechanism for mapping VMs to physical resources (Li et al. 2014), and another example is to determine optimal resource allocation so as to minimize service-level agreement violations (Sen et al. 2010, Wu et al. 2012, Yuan et al. 2018).

We study our problem from the user’s perspective. To better position our paper in the literature, we next present a more detailed review of recent studies on cost-aware real-time task scheduling. The common focus of these studies is to minimize the rental cost subject to a deadline constraint. Kumar et al. (2011) study the deadline constraint real-time task scheduling problem. They formulate the problem as a constrained optimization problem and propose a polynomial-time solution. Yi et al. (2013) consider the cost-minimization problem in cloud computing, and develop a mixed integer linear programming formulation along with several heuristic algorithms. Recently, Mahmood and Khan (2017) and Anwar and Deng (2018) consider the scientific workflow scheduling problem under deadline constraints in cloud computing environments where a scientific workflow is represented as a directed acyclic graph. However, all these studies and many others (Madni et al. 2017) suffer from the following limitations: (1) they assume that the execution time of each task is fixed and preknown, and (2) most only provide heuristic algorithms without any theoretical guarantee, thus they may perform poorly when worst-case scenarios happen. In contrast, we model the execution time of a task as a random variable.

To the best of our knowledge, Dziok et al. (2016) is the only study that considers the workflow scheduling problem with uncertain task execution time. The authors propose an adaptive solution whose idea can be roughly described as follows. It runs round by round. After each round, it takes into account the real execution time of already completed tasks, and, based on that, updates the scheduling. For example, when the execution time is shorter than estimated, it selects slower (and cheaper) VMs. However, there is no theoretical guarantee that their solution will be (near) optimal or feasible: (1) it is not clear how likely their solution can meet the deadline, and (2) even when the deadline has been met, its cost could be arbitrarily higher than the optimal solution. Unlike their model, we consider a nonadaptive real-time task scheduling problem where only one task is to be scheduled and the scheduling must be decided all at once in advance. Moreover, our model explicitly incorporates the cost of switching a computing task from one resource to another during processing. We develop a near-optimal solution that is guaranteed to meet the deadline with an arbitrarily high probability. Moreover, we show that the cost of our solution is close to the optimal solution. This research contributes fundamentally to the field of cost-aware task scheduling subject to a probabilistic deadline constraint.

## 3. Model Preliminaries

The cloud computing user’s problem we study here is the following. We consider a cloud computing provider that offers different VM instances for a fixed perunit-time rental cost. We assume a unit of time to be an hour, because VM instances are typically charged hourly. The VM instances have different virtual central processing unit (vCPU) and memory configurations and possess different computing capabilities. Since each partial hour used is charged as a full hour, terminating or stopping a VM instance before a full hour of operation does not reduce the total rental cost.

Cloud computing users can create computing clusters from VM instances using one master instance and one or more slave instances. The master VM instance manages the computing cluster and distributes the computing task among slave VM instances. We assume the cloud user is able to create m possible computing resources (possibly some of them are clusters), $\Omega = \{ K _ { 1 } , K _ { 2 } , \ldots , \bar { K } _ { m } \}$ Let us assume $K _ { 1 }$ (respectively, $K _ { m } )$ is the slowest (respectively, fastest) resource. The cost of renting one hour of computing resource $K _ { i }$ is a constant and denoted by $c _ { i } ,$ which is calculated as sum of the hourly rental costs of all the VM instances in that resource (if the resource is a cluster). We assume that $c _ { 1 } < c _ { 2 } < \ldots < c _ { m } ,$ that is, computing resources with higher hourly rental costs are more powerful. This is a reasonable assumption and consistent with the pricing policy of cloud computing providers such as AWS, Google, and Microsoft Azure.

Different resources can be assigned during each hour of processing a computing task. We represent the computing power of resource $K _ { i }$ during hour $t ,$ by the random variable $\tilde { q } _ { i t } .$ . This is the fraction of the computing task that can be completed by resource $K _ { i }$ during hour t. Note that we allow the performance of a computing resource to be uncertain. The cause of randomness in the performance of a computing resource is because the inner structure of the computing task could differ from one instance to another. Therefore, it is necessary to consider randomness in a resource’s computing performance. That is, for any given instance of the computing task, it is not possible to deterministically predict the fraction that computing resource $K _ { i }$ will complete in a particular hour. The source of randomness across hour units (t) for the same computing resource is not a change in the resource’s computing capability. Rather, we allow the portion of the computing task processed across time units to be slightly different in terms of complexity. Thus, we draw the values of random variables $\tilde { q } _ { i t }$ from the same probability distribution function g . (we also define $G _ { i } ( . )$ as the cumulative probability distribution function) on the support $[ q _ { { } _ { i } } , \overline { { q } } _ { { } _ { i } } ] , \mathrm { { \dot { 0 } } } < q _ { { } _ { i } } < \overline { { q } } _ { { } _ { i } } \leq 1$ , with an expected value $\mathbb { E } ( \tilde { q } _ { i t } ) = q _ { i }$ and variance $\dot { \mathbb { V } } ( \tilde { q } _ { i t } ) = \sigma _ { i } ^ { 2 } .$ for different values of t. We assume that $\underline { { q } } _ { i } \leq \underline { { q } } _ { i + 1 }$ and $\overline { { q } } _ { i } \leq \overline { { q } } _ { i + 1 }$

The variation across instances of the computing task and within portions of the same instance could generate some overlap in the support of the distributions associated with the performance of different resources. When these distributions overlap, it creates some dependence in the distributions of these resources. We consider two cases depending on whether the distributions associated with the resources are independent or dependent. In our base model (Section 4), we consider the distributions of the computing resources to be independent, and in Section 5, we extend the model to accommodate the fact that the distributions are dependent.

Previous studies have observed an increasing and concave relationship between the characteristics of a computing resource (CPU, memory, storage, etc.) and its computing performance (Dongarra 1993, Mao and Humphrey 2011, Juve et al. 2012). In addition, there is an increasing and linear relationship between these characteristics and the hourly rental cost of computing resources offered by commercial cloud computing providers. Therefore, we can assume that there is a concave increasing relationship between the expected computing performance of a resource and its hourly rental cost.

The cloud computing user’s problem is to find the total cost (rental cost plus switching cost) minimizing schedule of the computing task to be processed on one or more computing resources such that the task is finished on or before a specified integer deadline T. When a computing task is switched from one resource to another during the course of processing, the solution incurs a switching cost (denoted by S). This switching cost arises from the need to rent remote storage to preserve data persistence. The technical details behind switching are explained in the online appendix. The unit rental cost of remote storage is not large. To provide some perspective, Amazon’s EBS Cold HDD remote storage costs \$0.025 per gigabyte (GB)-month to rent. If a cloud user were to provision 1,000s GB of this storage for 40 hours, a switching cost of \$1.39 would be incurred. In practice, the switching cost is usually less than 2% of the total rental cost.

Table 1 summarizes the main notation in this study

## 4. Model Formulation and Solution

The problem is formulated as one in which the decision is to choose a specific computing resource during each hour to complete a computing task within T hours (an integer deadline). In this section, we assume that deadline T is large, but we relax this assumption in Section 5.

Let <sup>x</sup> and <sup>y</sup> be two decision matrices with components $x _ { i t }$ and $y _ { i t } ,$ , respectively. The component $x _ { i t }$ is equal to 1 if computing resource K is assigned during hour t, and is equal to 0 otherwise. The component $y _ { i t }$ is equal to 1 if computing resource $K _ { i }$ is assigned during hour $t + 1$ but not assigned during hour $t ,$ and is equal to 0 otherwise.<sup>1</sup> We define $\beta$ as the desired confidence (probability) of satisfying the deadline constraint.

Table 1. Main Notation

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $i$ </td><td>Computing resource index</td></tr><tr><td> $t$ </td><td>Hour index</td></tr><tr><td> $m$ </td><td>Number of available computing resources</td></tr><tr><td> $T$ </td><td>Deadline for completing the process of the computing task</td></tr><tr><td> $\beta$ </td><td>The cloud user&#x27;s probabilistic guarantee</td></tr><tr><td> $S$ </td><td>Switching cost</td></tr><tr><td> $c_{i}$ </td><td>Unit rental cost of computing resource  $K_{i}$ </td></tr><tr><td> $\tilde{q}_{it}$ </td><td>A fraction of the computing task processed by computing resource  $K_{i}$  during hour  $t$ </td></tr><tr><td> $q_{i}$ </td><td>Expected value of  $\tilde{q}_{it}$ </td></tr><tr><td> $\sigma_{i}^{2}$ </td><td>Variance of  $\tilde{q}_{it}$ </td></tr></table>

Problem ${ \mathcal { P } } ^ { w } ( \beta )$

$$
Z ^ {w} (\beta) = \min _ {\mathbf {x}, \mathbf {y}} \quad \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} c _ {i} x _ {i t} + S \sum_ {t = 1} ^ {T - 1} \sum_ {i = 1} ^ {m} y _ {i t}
$$

subject to

$$
\sum_ {i = 1} ^ {m} x _ {i t} \leq 1, \quad \forall t,\tag{1}
$$

$$
\mathbb {P} \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \tilde {q} _ {i t} x _ {i t} \geq 1 \right] \geq \beta ,\tag{2}
$$

$$
y _ {i t} \geq x _ {i t + 1} - x _ {i t}, \quad \forall i, \forall t \in \{1, \dots , T - 1 \},\tag{3}
$$

$$
x _ {i t}, y _ {i t} \in \{0, 1 \}, \quad \forall i, t,\tag{4}
$$

where the superscript w denotes the problem with a positive switching cost.

Theorem 1. The recognition version of problem ${ \mathcal { P } } ^ { w } ( \beta )$ is NP-complete.

The proof is provided in the online appendix.

Since problem ${ \mathcal { P } } ^ { w } ( \beta )$ does not have an efficient solution, our goal is to find a solution for this problem that can be quickly computed and implemented in practice, and is provably near optimal. Our strategy to achieve this goal is as follows:

• First, we define a new problem ${ \mathcal { P } } ^ { w o } ( \beta )$ , similar to problem ${ \mathcal { P } } ^ { w } ( { \boldsymbol { \beta } } )$ , but where the switching cost is zero.

• Next, we obtain a relaxation of problem ${ \mathcal { P } } ^ { w o } ( \beta )$ denoted by ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$ , and obtain a lower-bound solution for ${ \mathcal { P } } _ { R } ^ { w o } ( \beta ) .$ , which is, of course, also a lower bound for problem ${ \mathcal { P } } ^ { w o } ( \beta )$

• We use this lower-bound solution to get a nearoptimal solution for problem ${ \mathcal { P } } ^ { w o } ( \beta )$

• Finally, we use the same strategy to find a nearoptimal solution for problem ${ \mathcal { P } } ^ { w } ( \beta )$ .

## 4.1. The Problem with Zero Switching Cost

Problem ${ \mathcal { P } } ^ { w o } ( \beta )$

$$
Z ^ {w o} (\beta) = \min _ {\mathbf {x}} \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} c _ {i} x _ {i t}
$$

subject to

$$
\sum_ {i = 0} ^ {m} x _ {i t} = 1, \quad \forall t,\tag{5}
$$

$$
\mathbb {P} \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \tilde {q} _ {i t} x _ {i t} \geq 1 \right] \geq \beta ,\tag{6}
$$

$$
x _ {i t} \in \{0, 1 \} \quad \forall i, t.\tag{7}
$$

Note that in this given formulation, we have set $S = 0$ We have also introduced a dummy computing resource $K _ { 0 } ,$ , with $c _ { 0 } = 0$ and $\tilde { q } _ { 0 t } = 0 .$ , t. The dummy resource $K _ { 0 }$ adds no extra cost and has no processing power. This allows us to use the equality constraint in Equation (5) instead of the inequality constraint in Equation (1) in ${ \mathcal { P } } ^ { w } ( { \boldsymbol { \beta } } )$ . Problem ${ \hat { \mathcal { P } } } ^ { w o } ( \beta )$ is mathematically equivalent to ${ \mathcal { P } } ^ { w } ( \beta )$ with $S = 0$

We next formulate a relaxation of problem ${ \mathcal { P } } ^ { w o } ( \beta )$ and obtain a lower bound for this relaxation. Then we use this lower-bound solution to obtain a nearoptimal solution for problem ${ \mathcal { P } } ^ { w o } ( \beta )$ , and derive a performance guarantee for the near-optimal solution.

4.1.1. A Relaxation of Problem ${ \mathcal { P } } ^ { w o } ( \beta )$ . In the relaxed problem, we replace the probabilistic constraint in Equation (6) with an expectation constraint (Equation (9)). We can write the relaxed problem, denoted by problem ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$ , as follows.

Problem $\mathcal { P } _ { R } ^ { w o } ( \beta )$

$$
Z _ {R} ^ {w o} (\beta) = \min _ {\mathbf {x}} \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} c _ {i} x _ {i t}
$$

subject to

$$
\sum_ {i = 0} ^ {m} x _ {i t} = 1, \quad \forall t,\tag{8}
$$

$$
\mathbb {E} \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \tilde {q} _ {i t} x _ {i t} \right] \geq \beta ,\tag{9}
$$

$$
x _ {i t} \in \{0, 1 \} \quad \forall i, t.\tag{10}
$$

The probabilistic guarantee (Equation (6)) in problem $\bar { \mathcal { P } } ^ { w o } ( \beta )$ implies the expectation guarantee (Equation (9)) in $\mathcal { P } _ { R } ^ { w \bar { o } } ( \beta )$ . This can be easily shown using the relationship between the expectation of a random variable and its cumulative distribution function: $\begin{array} { r } { \mathbb { E } ( \tilde { X } ) = \int _ { \boldsymbol { r } } ( 1 - { F } ( { { x } } ) ) d { x } } \end{array}$ . We first write,

$$
\mathbb {E} \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \tilde {q} _ {i t} x _ {i t} \right] = \int_ {y} \mathbb {P} \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \tilde {q} _ {i t} x _ {i t} \geq y \right] d y.
$$

However,

$$
\int_ {0} ^ {1} \mathbb {P} \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \tilde {q} _ {i t} x _ {i t} \geq y \right] d y \geq \int_ {0} ^ {1} \beta d y = \beta .
$$

Hence, Equation (6) implies Equation (9). However, the reverse statement is not true. Hence, ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$ is a relaxation of ${ \mathcal { P } } ^ { w o } ( \beta )$ , or any feasible solution of problem ${ \mathcal { P } } ^ { w o } ( \beta )$ is also a feasible solution for problem ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$

Although it is a relaxation, problem ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$ is also NP-complete in the strong sense, as stated in Theorem 2.

Theorem 2. The recognition version of problem ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$ is NP-complete.

The proof is similar to the proof of Theorem 1.

4.1.2. A Further Relaxation. To solve problem ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$ we propose a linear programming (LP) relaxation of this problem that can be solved optimally. This also provides a lower-bound solution for ${ \mathcal { P } } _ { R } ^ { w o } ( { \bar { \beta } } )$ . Later, we use this lower-bound solution to get a near-optimal solution for problem ${ \mathcal { P } } ^ { w o } ( \beta )$

The LP-relaxation of problem ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$ (denoted by ${ \mathcal { P } } _ { R } ^ { w o - L P } ( \beta ) )$ can be obtained by removing the integrality constraint on $x _ { i t }$ as in the following.

Problem $\mathcal { P } _ { R } ^ { w o - L P } ( \beta )$

$$
Z _ {R} ^ {w o - L P} (\beta) = \min _ {\mathbf {x}} \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} c _ {i} x _ {i t}
$$

subject to Equations 8<sub>(</sub> <sub>)</sub> and 9<sub>(</sub> <sub>)</sub>,

$$
0 \leq x _ {i t} \leq 1 \quad \forall i, t.\tag{11}
$$

To solve ${ \mathcal { P } } _ { R } ^ { w o - L P } ( \beta )$ , we write its Lagrangian, denoted by $\mathcal { P } _ { R } ^ { w o - L R } ( \overset {  } { \beta } , \mu )$ , obtained by dualizing the constraint in Equation (9) and introducing the Lagrange variable, $\mu \geq 0$ as in the following.

Problem $\mathcal { P } _ { R } ^ { w o - L R } ( \beta , \mu )$

$$
\begin{array}{l} Z _ {R} ^ {w o - L R} (\beta , \mu) = \min _ {\mathbf {x}} \quad \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} c _ {i} x _ {i t} \\ \qquad + \mu \left(\beta - \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \mathbb {E} (\tilde {q} _ {i t}) x _ {i t}\right) \\ \text { subject   to   Equation(8)and(11). } \end{array}
$$

We know $\mathbb { E } ( \tilde { q } _ { i t } ) = q _ { i }$ . Hence, we can rewrite the previous model as follows:

$$
Z _ {R} ^ {w o - L R} (\beta , \mu) = \min _ {\mathbf {x}} \quad \sum_ {t = 1} ^ {T} \left(\sum_ {i = 0} ^ {m} (c _ {i} - \mu q _ {i}) x _ {i t}\right) + \beta \mu
$$

subject to Equations 8 and 11 .

This relaxation is defined for $\mu \geq 0 ,$ , which is a necessary condition for $Z _ { R } ^ { w o - L R } ( \beta , \dot { \mu } ) \leq Z _ { R } ^ { w o - L P } ( \beta )$ to hold. The previous model can easily be solved for any fixed $\mu \geq 0$ by determining m $\mathrm { i n } _ { i } ( c _ { i } - \mu q _ { i } )$ and setting, for each $t ,$ the associated $x _ { i t } = 1$ and the remaining $x _ { i t }$ values to zero. We can therefore rewrite the problem as

$$
Z _ {R} ^ {w o - L R} (\beta , \mu) = \min _ {i} (T c _ {i} + (\beta - T q _ {i}) \mu),\tag{12}
$$

which is a lower envelop of a family of linear functions $f _ { i } ( \mu ) = T c _ { i } + ( \beta - T q _ { i } ) \mu$

The following lemma provides an explicit form of function $Z _ { R } ^ { w o - L R } ( \beta , \mu )$ under the concavity assumption.

Lemma 1. For any constant $\mu ,$ we have

$$
Z _ {R} ^ {w o - L R} (\beta , \mu) = \left\{ \begin{array}{l l} f _ {0} (\mu) & \quad \text {   if   } \quad 0 \leq \mu \leq \mu_ {0}, \\ f _ {1} (\mu) & \quad \text {   if   } \quad \mu_ {0} \leq \mu \leq \mu_ {1}, \\ . & \quad . \\ . & \quad . \\ f _ {m - 1} (\mu) & \quad \text {   if   } \quad \mu_ {m - 2} \leq \mu \leq \mu_ {m - 1}, \\ f _ {m} (\mu) & \quad \text {   if   } \quad \mu_ {m - 1} \leq \mu \leq \bar {\mu}, \end{array} \right.\tag{13}
$$

where $\mu _ { i }$ is the intersection of the functions $f _ { i } ( \mu )$ and $f _ { i + 1 } ( \mu )$ for all $i = 0 , \ldots , m - 1$ and equals to $\frac { c _ { i + 1 } - c _ { i } } { q _ { i + 1 } - q _ { i } }$ and $\bar { \mu }$ is the maximum value of $\mu .$ .

The proof is provided in online appendix.

For any fixed $\mu ,$ function $Z _ { R } ^ { w o - L R } ( \beta , \dot { \mu } )$ will be a lower bound for $Z _ { R } ^ { w o - \dot { L } P } ( \beta )$ . Now, we need to select an appropriate value for $\mu$ . It is clear that the best choice for μ would be an optimal solution to the dual problem of $\dot { \mathcal { P } } _ { R } ^ { w o - L P } ( \beta )$ , denoted by ${ \mathcal { P } } _ { R } ^ { w o - D } ( \beta )$ , and written as follows.

Problem $\mathcal { P } _ { R } ^ { w o - D } ( \beta )$

$$
\begin{array}{l} Z _ {R} ^ {w o - D} (\beta) = \max _ {\mu} Z _ {R} ^ {w o - L R} (\beta , \mu) \\ \text { subject   to } \quad \mu \geq 0. \end{array}\tag{14}
$$

To find the optimal solution to problem ${ \mathcal { P } } _ { R } ^ { w o - D } ( \beta ) .$ , we need to show there exists a feasible solution for problem ${ \mathcal { P } } _ { R } ^ { w o - L P } ( \beta )$ that has the same objective function value. We can see function $Z _ { R } ^ { w o - L R } ( \beta , \mu )$ has all the nice properties, such as continuity and concavity, except one-differentiability. Although this function is differentiable almost everywhere, it is nondifferentiable at the optimal point. Theorem 3 describes how we can obtain an optimal solution to problem ${ \mathcal { P } } _ { R } ^ { w o - L P } ( \beta )$ . Let us define $\begin{array} { r } { \tau _ { j } ^ { ~ \bullet } = ( \frac { \beta - T q _ { j - 1 } } { q _ { j } - q _ { j - 1 } } ) } \end{array}$

Theorem 3. The optimal solution of problem ${ \mathcal { P } } _ { R } ^ { w o - L P } ( \beta )$ is to assign computing task to:

(i) Resource $K _ { j } f o r \tau _ { j }$ hours, $i f \beta - T q _ { j } < 0 ,$ , where $j = 1 ;$ (ii) Resource ${ \bf \dot { \cal K } } _ { j }$ for $\tau _ { j }$ hours, if $\dot { \beta } - T q _ { j } = 0 .$ , where $j = i \in \{ 1 , \ldots , m \}$

(iii) Otherwise, resource $K _ { j - 1 } f o r \left( T - \tau _ { j } \right)$ hours and $K _ { j }$ $f o r \tau _ { j }$ hours, where $j = \gamma$ and $\gamma - 1$ and γ are the indices of the fastest infeasible and the slowest feasible computing resource for problem ${ \mathcal { P } } _ { R } ^ { w o - L P } ( \beta )$ , respectively.

The proof is provided in the online appendix.

Under two cases, the solution to the LP-relaxation problem is trivial:

Case (i). When T is a large enough number such that the slowest computing resource can satisfy Equation (9), implying that using only the slowest resource to complete the task is optimal.

Case (ii). When there is a computing resource that can finish processing the computing task exactly at the end of hour T. In this case, using only this computing resource is an optimal solution.

Because of concave relationship between the expected computing performance $( q _ { i } )$ and the hourly rental cost $( c _ { i } )$ , selecting a slower computing resource is always more efficient. Therefore, if the least powerful computing resource is feasible, then using only this resource will be optimal. However, if the slowest resource is not feasible, but there exists a computing resource $K _ { i }$ for $i > 1$ that is able to finish the task exactly at the end of hour T, then using only this computing resource is optimal.

If neither case (i) nor case (ii) hold, then the slowest feasible resource (with some slack) and the fastest infeasible resource must be selected.

4.1.3. A Near-Optimal Solution for Problem ${ \mathcal { P } } ^ { w o } ( \beta )$ . So far, we have derived a lower bound for problem ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$ , which is also a lower bound for problem ${ \mathcal { P } } ^ { w o } ( { \boldsymbol { \beta } } )$ . As we discussed in Section 4.1.1, the probabilistic constraint in problem ${ \mathcal { P } } ^ { w o } ( \beta )$ implies the expected constraint in problem ${ \mathcal { P } } _ { R } ^ { w o } ( \beta )$ . Therefore, we need to formulate a new problem $\mathcal { P } _ { R } ^ { w o } ( \beta ^ { \prime } )$ using a suitable parameter $\beta ^ { \prime } \geq \beta$ such that the near-optimal solution of problem $\dot { \mathcal { P } } _ { R } ^ { w o } ( \beta ^ { \prime } )$ is feasible for problem ${ \mathcal { P } } ^ { w o } ( \beta )$

We derive the value of α such that $\mathbb { E } [ \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } \times$ $\widetilde { q } _ { i t } x _ { i t } ] = \alpha$ implies $\begin{array} { r } { \mathbb { P } [ \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } \tilde { q } _ { i t } x _ { i t } \ge 1 ] = \beta . } \end{array}$ . We apply the Lindeberg version of the central limit theorem to use the normal approximation for the distribution of the random variable $\textstyle \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } { \tilde { q } } _ { i t } x _ { i t } ,$ , which is appropriate when the random variables $\tilde { q } _ { i t }$ <sub>t</sub> are independent, the individual variance of random variables is not too large relative to the rest, and sample size is large enough (Billingsley 2008). The sample size here is number of time units used for processing the task (usually in the order of T), rather than the number of different computing resources used in the schedule. According to Hogg and Tanis (2009), $T \geq 3 0$ can be considered as a large enough sample size for using the central limit theorem. Since $x _ { i t }$ is a binary variable, $( x _ { i t } ) ^ { 2 } = x _ { i t }$ , we obtain $\begin{array} { r } { \bar { \Phi } _ { N } ( \frac { 1 - \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } q _ { i } x _ { i t } } { \sqrt { \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } \sigma _ { i } ^ { 2 } x _ { i t } } } ) = \beta , } \end{array}$ , where $\bar { \Phi } _ { N } ( . ) = 1 - \Phi _ { N } ( . )$ and $\Phi _ { N } ( . )$ is the cumulative distribution function of the standard normal distribution. Therefore, we have $\begin{array} { r } { \alpha = 1 + z _ { \beta } \sqrt { \textstyle \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } \sigma _ { i } ^ { 2 } x _ { i t } } } \end{array}$ , where $z _ { \beta } = \Phi _ { N } ^ { - 1 } ( \beta )$ . Using the given value of α for the expectation constraint in problem ${ \mathcal P } _ { R } ^ { w o } ( \alpha )$ creates nonlinearity in this problem. To avoid this, we replace α with

$$
\beta^ {\prime} = 1 + z _ {\beta} \sigma \sqrt {T},\tag{15}
$$

where $\sigma ^ { 2 } \geq \operatorname* { m a x } \{ \sigma _ { i } ^ { 2 } \}$ and $\textstyle \sum _ { i = 0 } ^ { m } x _ { i t } = 1 . ^ { 2 }$

For finding a feasible solution for problem ${ \mathcal P } _ { R } ^ { w o } ( \beta ^ { \prime } ) .$ we first find the optimal solution of problem $\mathcal { P } _ { R } ^ { w o - \sum P ^ { \prime } } ( \beta ^ { \prime } )$ based on the procedure explained in Section 4.1.2. Then, this solution is adapted using the BaseM method described in Lemma 2. Let us define $\begin{array} { r } { \tau _ { g } ^ { \prime } = \frac { \beta ^ { \prime } - T q _ { g - 1 } } { q _ { g } - q _ { g - 1 } } } \end{array}$

Lemma 2. The BaseM method produces a feasible solution for problem $\mathcal { P } _ { R } ^ { w o } ( \beta ^ { \prime } )$ , in which the computing task is assigned to:

(i) Resource $K _ { g }$ for $\left\lceil \tau _ { g } ^ { \prime } \right\rceil$ hours, $i f \beta ^ { \prime } - T q _ { g } < 0 .$ , where $g = 1 ,$ ;

(ii) Resource $K _ { g } f o r \lceil \tau _ { g } ^ { \prime } \rceil$ hours, $i f \beta ^ { \prime } - T q _ { g } = 0$ , where $g = \hat { i } \in \{ 1 , \ldots , m \} ;$

(iii) Otherwise, resource $K _ { g - 1 } f o r \left\lfloor T - \tau _ { g } ^ { \prime } \right\rfloor$ <sup>⌋</sup> hours and $K _ { g }$ $f o r \left\lceil \tau _ { g } ^ { \prime } \right\rceil$ hours, where $g = \hat { \gamma }$ and $\hat { \gamma } - \hat { 1 }$ and γˆ are the indices of the fastest infeasible and the slowest feasible computing resource for $\mathcal { P } _ { R } ^ { w o - L P } ( \beta ^ { \prime } )$ , respectively.

The proof is provided in the online appendix.

4.1.3.1. Enhanced Rounding. When $c _ { g }$ is large, the BaseM solution can be substantially improved using the EnhancedRounding approach. The Enhanced Rounding approach produces a solution arbitrarily close to the optimal. This approach builds on a pruning technique and the basic idea is to exclude expensive computing resources (whose schedule can be decided later through enumeration) from the input of problem $\mathcal { P } _ { R } ^ { w o } ( \beta ^ { \prime } )$ . Let $O = \{ o _ { 1 } , \ldots , o _ { T } \}$ denote the optimal solution of problem $\mathcal { P } _ { R } ^ { w o } ( \beta ^ { \prime } )$ , where $\forall t : o _ { t } \in$ $\{ \hat { K } _ { i } | i \in \{ 1 , \cdots , m \} \}$ denotes the computing resource scheduled at time unit t. Let $Z _ { R } ^ { w o } ( \beta ^ { \prime } )$ denote the total cost of O. For some given error bound $\delta > 0$ , we say a computing resource is expensive if its hourly rental cost is larger than or equal to $\delta Z _ { R } ^ { w o } ( \beta ^ { \prime } )$

Let $U \subseteq O$ denote the set of all expensive computing resources in O and assume $K _ { r }$ is the most expensive computing resource in O U. To illustrate, let us take $O = \dot { \{ K _ { 1 } , K _ { 1 } , K _ { 3 } , K _ { 5 } \} }$ as an example of an optimal solution. Assume $c _ { 1 } = 1 , c _ { 3 } = 2 , c _ { 5 } = 1 0 \AA$ , thus $Z _ { R } ^ { w o } ( \beta ^ { \prime } ) = 1 4 .$ For a given error bound $\delta = 0 . 5$ , we have $\ddot { U } = \{ K _ { 5 } , K _ { 5 } \}$ and $r = 3 .$ , because $c _ { 5 } > 1 4 / 2 = 7$ and $K _ { 3 }$ has the highest hourly rental cost in $O \backslash U$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 (EnhancedRounding)
Input: error bound δ;
Output: a near-optimal schedule
    1: D = ∅, opt = ∞;
    2: for all possible pairs of U (with size no larger than  $\lfloor 1/\delta \rfloor$ ) and  $K_{r}$  do
    3: Apply BaseM to solve problem  $\mathcal{P}_{R}^{wo}(\beta', U, r)$  and get H;
    4: if  $Z_{R}^{wo}(\beta', U, r) &lt; opt$  then
    5: opt =  $Z_{R}^{wo}(\beta', U, r)$ ,  $D \leftarrow H \cup U$
</div>

Although we do not know U and $K _ { r } ,$ , the size of U is at most $\lfloor \bar { 1 / \delta } \rfloor$ and there are at most m possibilities for $K _ { r }$ such that for every $K _ { i } \in U : c _ { r } < c _ { i } .$ Therefore, we can enumerate all possible pairs of U and $K _ { r }$ in time $O ( m ^ { 1 / \delta + 1 } )$ . Notice that our method differs from existing pruning techniques (Sahni 1975, Lenstra et al. 1977, Chakaravarthy et al. 2013) in that we need to enumerate both expensive computing resources (U) and the inexpensive computing resource with the highest hourly rental cost $( \bar { K _ { r } } )$ . We solve the following optimization problem for all possible pairs of U and $K _ { r } ,$ and return the one with the minimum cost. For a given U and $K _ { r } ,$ , let $q ( U )$ (respectively, $c ( U ) )$ denote the fraction of computing task that is processed by U (respectively, the total cost of U). We next consider a modified version of $\mathcal { P } _ { R } ^ { w o } ( \beta ^ { \prime } )$ on a restricted set of computing resources $\{ K _ { 1 } , \cdots , K _ { r } \}$

Problem $\mathcal { P } _ { R } ^ { w o } ( \beta ^ { \prime } , U , r ) ;$

$$
Z _ {R} ^ {w o} \big (\beta^ {\prime}, U, r \big) = \min _ {\mathbf {x}} \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {r} c _ {i} x _ {i t} + c (U)
$$

subject to

$$
\sum_ {i = 0} ^ {r} x _ {i t} = 1, \qquad t = 1, 2, \ldots , T - | U |,\tag{16}
$$

$$
\mathbb {E} \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {r} \tilde {q} _ {i t} x _ {i t} \right] \geq \beta^ {\prime} - q (U),\tag{17}
$$

$$
x _ {i t} \in \{0, 1 \} \forall i \in \{1, 2, \dots , r \}, t \in \{1, 2, \dots , T - | U | \}.\tag{18}
$$

We apply BaseM to get the set H as a solution to the previous problem. The final solution of problem $\bar { \mathcal { P } } _ { R } ^ { w o } ( \beta ^ { \prime } )$ for a given U and $K _ { r }$ is composed of U and H. For ease of presentation, we define $Z _ { R } ^ { w o } ( \beta ^ { \prime } , U , r ) = \infty$ when problem $\mathcal { P } _ { R } ^ { w o } ( \beta ^ { \prime } , U , r )$ admits no feasible solution. A detailed description of our algorithm is given in Algorithm 1. Now we are ready to analyze the approximation ratio of this solution.

Lemma 3. Assume U∗ and $K _ { r ^ { * } }$ give the minimum cost. Given an error bound $\delta > 0$ , we can enumerate all possible U and $K _ { r }$ in time $O ( m ^ { 1 / \delta + 1 } )$ and the total rental cost of proposed EnhancedRounding approach for problem $\mathcal { P } _ { R } ^ { w o } ( { \bar { \beta ^ { \prime } } } )$ is upper bounded by $Z _ { R } ^ { w o } ( \beta ^ { \prime } , \breve { U } ^ { * } , \dot { r } ^ { * } ) \leq ( \dot { 1 } + \dot { \delta } ) Z _ { R } ^ { w o } ( \beta ^ { \prime } )$

The proof is provided in the online appendix.The proof is provided in the online appendix.

Theorem 4. Assume U∗ and $K _ { r ^ { * } }$ give the minimum cost. The proposed EnhancedRounding approach achieves the following performance guarantee for problem ${ \mathcal { P } } ^ { w o } ( \beta )$

$$
\begin{array}{l} \frac {Z _ {R} ^ {w o} (\beta^ {\prime} , U ^ {*} , r ^ {*})}{Z ^ {w o} (\beta)} \\ <   (1 + \delta) \bigg (\frac {q _ {j} - q _ {j - 1}}{q _ {g} - q _ {g - 1}} \bigg) \\ \times \left( \begin{array}{c} \Big (T q _ {g} - z _ {\beta} \sigma \sqrt {T} - 1 \Big) c _ {g - 1} \\ + \Big (z _ {\beta} \sigma \sqrt {T} + 1 - T q _ {g - 1} \Big) c _ {g} + \eta (q _ {g} - q _ {g - 1}) \\ \hline (T q _ {j} - \beta) c _ {j - 1} + (\beta - T q _ {j - 1}) c _ {j} \end{array} \right). \end{array}
$$

## 4.2. The Problem with Positive Switching Cost

In this section, we consider the cloud computing user problem with a positive cost for switching the computing task from one computing resource to a different one. This problem has already been formulated in the model in Equations (1)–(4). For solving this problem, we use the same procedure that we applied to get a near-optimal solution for problem ${ \mathcal { P } } ^ { w { \bar { o } } } ( { \bar { \beta } } )$

Let us define expected version of problem ${ \mathcal { P } } ^ { w } ( \beta )$ <sub>)</sub> as problem ${ \mathcal { P } } _ { R } ^ { w } ( \beta )$ . We first obtain the optimal solution of LP-relaxation of problem ${ \mathcal { P } } _ { R } ^ { w } ( \beta )$ , which is called problem ${ \mathcal { P } } _ { R } ^ { w - L P } ( \beta )$ . Then, we use the objective function value of this solution as a lower bound for problem ${ \mathcal { P } } ^ { w } ( \beta )$ Finally, we will try to find a near-optimal solution for problem ${ \mathcal { P } } ^ { w } ( { \boldsymbol { \beta } } )$ and show its performance guarantee. The following theorem explains the optimal solution of problem $\mathcal { P } _ { R } ^ { w - L P } ( \beta )$

Theorem 5. The optimal solution of problem ${ \mathcal { P } } _ { R } ^ { w - L P } ( \beta )$ is to assign computing task to:

(i) Resource $K _ { j } f o r \tau _ { j }$ hours, $i f \beta - T q _ { j } < 0 ,$ , where $j = 1 ;$ (ii) Resource ${ \bf \dot { \theta } } _ { k _ { j } }$ for $\tau _ { j }$ hours, if $\dot { \beta } - T q _ { j } = 0 .$ , where $j = i \in \{ 1 , \ldots , m \} ;$

(iii) Resource K<sub>j</sub> for τ<sub>j</sub> hours, $i f ( \mathrm { i } )$ and (ii) do not hold and $\begin{array} { r } { S > ( \frac { \overbrace { T q _ { j } - \beta } } { q _ { j } - q _ { j - 1 } } ) ( \frac { q _ { j - 1 } c _ { j } - q _ { j } ^ { \prime } \tilde { c } _ { j - 1 } } { q _ { j } } ) } \end{array}$ , where $j = \gamma$ and γ is the index of the slowest feasible computing resource for problem ${ \mathcal { P } } _ { R } ^ { w o - L P } ( \beta ) ;$

(iv) Resource $K _ { j - 1 } f o r T - \tau _ { j }$ hours and $K _ { i } f o r \tau _ { i }$ hours, if (i) and (ii) do not hold and $\begin{array} { r } { S \le ( \frac { T q _ { j } - \beta } { q _ { i } - q _ { j - 1 } } ) ( \frac { q _ { j - 1 } \check { c } _ { j } - q _ { j } { c } _ { j - 1 } } { q _ { i } } ) } \end{array}$ , where $j = \gamma \ a n d \ \gamma - 1$ is the index of the fastest infeasible computing resource for problem $\dot { \mathcal { P } } _ { R } ^ { w o - L P } ( \beta )$

The proof is provided in the online appendix.

After getting the lower bound for problem ${ \mathcal { P } } ^ { w } ( \beta ) _ { . }$ now we need to find a near-optimal solution for this problem. Similar to problem $\hat { \mathcal { P } } _ { R } ^ { w o } ( \beta ^ { \prime } )$ , a possible feasible solution for problem $\mathcal { P } _ { R } ^ { w } ( \beta ^ { \prime } )$ generated by BaseM can be explained in Lemma 4.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 (EnhancedRounding with Positive Switching Cost)
Input: error bound δ;
Output: a near-optimal schedule
1: D = ∅, opt = ∞;
2: for all possible pairs of U (with size no larger than  $\lfloor1/\delta\rfloor$ ) and  $K_{r}$  do
3: Apply BaseM to solve problem  $\mathcal{P}_{R}^{wo}(\beta', U, r)$  and get H;
4: if  $Z_{R}^{wo}(\beta', U, r) \neq \infty$ , then
5: if  $\min\{c_{r}\lceil\frac{\beta'-q(U)}{q_{r}}\rceil + c(U), Z_{R}^{wo}(\beta', U, r)\} &lt; opt$ , then
6: opt =  $\min\{c_{r}\lceil\frac{\beta'-q(U)}{q_{r}}\rceil + c(U), Z_{R}^{wo}(\beta', U, r)\}$ ,
7: if  $c_{r}\lceil\frac{\beta'-q(U)}{q_{r}}\rceil + c(U) &lt; Z_{R}^{wo}(\beta', U, r)$ , then
8:  $D \leftarrow \{\lceil\frac{\beta'-q(U)}{q_{r}}\rceil \text{ copies of } K_{r}\} \cup U$ 
9: else
10:  $D \leftarrow H \cup U;$
</div>

Lemma 4. The BaseM method produces a feasible solution for problem $\mathcal { P } _ { R } ^ { w } ( { \boldsymbol { \beta } } ^ { \prime } )$ in which the computing task is assigned to:

(i) Resource $K _ { g } f o r \ \lceil \tau _ { g } ^ { \prime } \rceil$ hours, $i f \beta ^ { \prime } - T q _ { g } < 0 .$ , where $g = 1 ;$ (ii) Resource $K _ { g } f o r \ \lceil \tau _ { g } ^ { \prime } \rceil$ hours, $i f \beta ^ { \prime } - T q _ { g } = 0 .$ , where $g = \hat { i } \in \{ 1 , \ldots , m \} ;$

(iii) Resource $K _ { g } f o r \lceil \tau _ { g } ^ { \prime } \rceil$ hours, $i f \left( \mathrm { i } \right)$ and (ii) do not hold and $\begin{array} { r } { S > ( T - \tau _ { g } ^ { \prime } ) ( \frac { q _ { g - 1 } c _ { g } - q _ { g } c _ { g - 1 } } { q _ { g } } ) } \end{array}$ , where $g = \hat { \gamma } a n d \hat { \gamma }$ is the index of the slowest feasible computing resource for problem $\mathcal { P } _ { R } ^ { w o - L P } ( \beta ^ { \prime } ) ,$ ;

(iv) Resource $K _ { g - 1 } f o r \lfloor T - \tau _ { g } ^ { \prime } \rfloor$ hours and $K _ { g }$ for $\lceil \tau _ { g } ^ { \prime } \rceil$ hours, $i f ( \mathrm { i } )$ and (ii) do not hold and $\begin{array} { r } { S \le ( T - \tau _ { g } ^ { \prime } ) ( \frac { q _ { g - 1 } c _ { g } - q _ { g } c _ { g - 1 } } { q _ { g } } ) } \end{array}$ where $g = \hat { \gamma }$ and $\hat { \gamma } - 1$ is the index of the fastest infeasible computing resource for problem $\mathcal { P } _ { R } ^ { w o - L P } ( \bar { \beta } ^ { \prime } )$ .

The proof is similar to proof of Lemma 2.

We use Lemma 4 and a slight modification of Algorithm 1 to get the near-optimal solution for problem $\mathcal { P } _ { R } ^ { w } ( \beta ^ { \prime } )$ , which is also a feasible solution for problem ${ \mathcal { P } } ^ { w } ( \beta )$ . A detailed description of our algorithm is given in Algorithm 2. We next highlight the modified part: For a given U and $K _ { r } ,$ in addition to solving $\mathcal { P } _ { R } ^ { \bar { w } o } ( \beta ^ { \prime } , U , r )$ to get H, we also compute the cost when using $K _ { r }$ only to perform the remaining computing task $\beta ^ { \prime } - q ( U )$ , for example, $\begin{array} { r } { c _ { r } \lceil \frac { \beta ^ { \prime } - q ( U ) } { q _ { r } } \rceil } \end{array}$ . I $: Z _ { R } ^ { w o } ( \beta ^ { \prime } .$ $U , r ) \neq \infty$ and $c _ { r } \lceil \frac { \beta ^ { \prime } - q ( U ) } { q _ { r } } \rceil + c ( U ) < Z _ { R } ^ { w o } ( \beta ^ { \prime } , U , r )$ , we use $\{ \lceil \frac { \beta ^ { \prime } - q ( U ) } { q _ { r } } \rceil$ copies of $K _ { r } \} \cup U$ as the final solution, but if $Z _ { R } ^ { w o } ( \beta ^ { \prime } , U , r ) \neq$ and $\begin{array} { r } { c _ { r } \lceil \frac { \beta ^ { \prime } - q ( U ) } { q _ { r } } \rceil + c ( U ) \geq Z _ { R } ^ { w o } ( \beta ^ { \prime } , U , r ) . } \end{array}$ we use H U as the final solution. Line 4 in Algorithm 2 ensures that the returned solution is feasible. Similar to Lemma 3 and Theorem 4, we provide the following performance bound.

Lemma 5. Assume U∗ and $K _ { r ^ { * } }$ give the minimum cost. We use $\begin{array} { r } { \overline { { Z } } _ { R } ^ { w } ( \beta ^ { \prime } , U ^ { * } , r ^ { * } ) = \operatorname* { m i n } \{ c _ { r } \lceil \frac { \beta ^ { \prime } - q ( U ^ { * } ) } { q _ { r ^ { * } } } \rceil + c ( U ^ { * } ) , Z _ { R } ^ { w o } ( \beta ^ { \prime } , U ^ { * } , r ^ { * } ) \} } \end{array}$ to denote the total rental cost of our solution. Given an error bound $\delta > 0$ , we can enumerate all possible U and $K _ { r }$ in time $O ( m ^ { 1 / \delta + 1 } )$ and the total rental cost of the proposed EnhancedRounding approach for problem $\mathcal { P } _ { R } ^ { w } ( { \boldsymbol { \beta } } ^ { \prime } )$ is upper bounded by $\begin{array} { r } { \sum _ { R } ^ { w } ( \tilde { \beta } ^ { \prime } , \dot { U } ^ { * } , r ^ { * } ) \le ( 1 + \delta ) Z _ { R } ^ { w } ( \beta ^ { \prime } ) } \end{array}$

The proof is provided in the online appendix.

Theorem 6. Assume U∗ and $K _ { r ^ { * } }$ give the minimum cost. The proposed EnhancedRounding approach achieves the following performance guarantee for problem ${ \mathcal { P } } ^ { w } ( \beta )$

$$
\begin{array}{l} \frac {\overline {{Z}} _ {R} ^ {w} (\beta^ {\prime} , U ^ {*} , r ^ {*})}{Z ^ {w} (\beta)} \\ <   (1 + \delta) \bigg (\frac {q _ {j} - q _ {j - 1}}{q _ {g} - q _ {g - 1}} \bigg) \\ \times \left( \begin{array}{c} \Big (T q _ {g} - z _ {\beta} \sigma \sqrt {T} - 1 \Big) c _ {g - 1} \\ + \Big (z _ {\beta} \sigma \sqrt {T} + 1 - T q _ {g - 1} \Big) c _ {g} + \big (q _ {g} - q _ {g - 1} \big) \big (c _ {g} + I _ {1} S \big) \\ \hline (T q _ {j} - \beta) c _ {j - 1} \\ + (\beta - T q _ {j - 1}) c _ {j} + I _ {2} S (q _ {j} - q _ {j - 1}) \end{array} \right), \end{array}
$$

where $I _ { 1 }$ is an indicator function that is set to 0 under cases (i)–(iii) in Lemma 4 and set to 1 otherwise. Similarly, the indicator function $I _ { 2 }$ is set to 0 under cases (i)–(iii) in Theorem 5, and set to 1 otherwise.

The proof is provided in the online appendix.

## 5. Extensions: Relaxing Our Assumptions

In this section, we extend our base model in two directions. First, we consider a dependency relationship across the distributions of the computing performance of the available resources. Second, we consider a small time limit for completing the processing of the computing task. The second extension is important because we use the central limit theorem to model the distribution of the sum of individual distributions as a normal distribution.

## 5.1. Ordering Constraint Dependency Structure

Our analysis thus far has made the assumption that the distributions associated with the resources are independent. Here, we consider an alternative dependency structure referred to as the ordering constraint (OC), which is represented in the following statement: For any specific instance of the computing task, the realized fractions processed (in one hour) by the resources can be ordered so that the fraction processed by a weaker resource will be smaller than the fraction processed by a more powerful one.

The previous condition is natural. Despite the presence of randomness in the performance (across instances and across time units), we would not expect a stronger resource to process (in one hour) less of the computing task than a weaker one. To illustrate the concept of OC dependency more clearly, consider two computing resources $K _ { i }$ and $K _ { i + 1 }$ with probability distribution functions $g _ { i } ( . )$ and $g _ { i + 1 } ( . )$ on supports $[ \underline { { q } } _ { i } , \overline { { q } } _ { i } ]$ and $[ \underline { { q } } _ { i + 1 } , \overline { { q } } _ { i + 1 } ] ,$ , respectively. Let us focus on a case where the computing task is first processed on a stronger resource, that is, $K _ { i + 1 }$ , for one hour and the fraction processed is $\theta _ { i + 1 }$ . According to OC condition, if $\theta _ { i + 1 } \leq \overline { { \overline { { q } } } } _ { i } ,$ , the fraction processed by weaker resource $K _ { i }$ will lie in interval $[ q _ { i } , \theta _ { i + 1 } ]$ with probability distribution function $\frac { g _ { i } ( q ) } { G _ { i } ( \theta _ { i + 1 } ) }$ for all $q \in [ \underline { { q } } _ { i } , \theta _ { i + 1 } ]$ ; otherwise, it will be in interval $[ \underline { { q } } _ { i } , \overline { { q } } _ { i } ]$ with probability distribution function $g _ { i } ( q )$ for all $q \in [ q _ { , } , \overline { { q } } _ { i } ]$ . Similarly, if the computing task is first processed by resource $K _ { i }$ for one hour and the fraction processed is $\theta _ { i } ,$ , the fraction processed by stronger resource $K _ { i + 1 }$ will be in interva $[ \theta _ { i } , \overline { { q } } _ { i + 1 } ]$ with probability distribution function $\frac { g _ { i + 1 } ( q ) } { 1 - G _ { i + 1 } ( \theta _ { i } ) }$ for all $q \in [ \theta _ { i } , \overline { { q } } _ { i + 1 } ] ,$ , if ${ \underline { { q } } } _ { i + 1 } \leq \theta _ { i } ;$ it will be in $[ \underline { { q } } _ { i + 1 } , \overline { { q } } _ { i + 1 } ]$ with probability distribution function $g _ { i + 1 } ( q )$ for all $q \in$ $[ q _ { i + 1 } , \widehat { \overline { { q } } } _ { i + 1 } ]$ otherwise. When there is no overlap in the support of the computing performance of the resources, the resources are substantially different from one another. Therefore, knowing the performance of one of the resources will not give much information about the computing performance of the other one.

In this section, we first propose a new heuristic procedure named EnhancedRounding<sup>OC</sup> for problem ${ \bar { \ p } } ^ { w } ( \beta )$ under the OC dependency structure, and then we provide a lower bound for the problem and a worst-case performance guarantee bound for the proposed heuristic.

5.1.1. EnhancedRounding<sup>OC</sup>. The proposed heuristic EnhancedRounding<sup>OC</sup> creates a feasible solution for problem ${ \mathcal { P } } ^ { w } ( \beta )$ under OC dependency as follows. First, it makes the distribution of the resources independent in a particular way. Second, it uses the updated distributions, and similar to Section 4.2, it implements EnhancedRounding to find a feasible solution for problem $\mathcal { P } _ { R } ^ { w } ( { \boldsymbol { \beta } } ^ { \prime } )$ . It is shown that the generated solution is feasible for problem ${ \mathcal { P } } ^ { w } ( \beta )$ under OC dependency. Finally, it improves the solution using a pruning approach. A precise description of our proposed EnhancedRounding<sup>OC</sup> heuristic is presented in Algorithm 3.

As described in Section 4.1.3, the value of $\beta ^ { \prime }$ (Equation (15)) is calculated based on the assumption that the distributions of the resources are independent. Therefore, to be able to use this value of $\beta ^ { \prime } ,$ , we must make the distribution of the resources independent. This is done using the following procedure:

For any two resources $K _ { i }$ and $K _ { i + 1 }$ for all $i \in \{ 1 , \ldots ,$ $m - 1 \}$ , we assume that the fraction processed by stronger resource, that is, $K _ { i + 1 } , i s \thinspace g _ { \underline { { { i + 1 } } } }$ and thus update <sup>+</sup> the distribution of the computing performance of resource $K _ { i }$ as $[ \underline { { q } } _ { i } , \mathrm { m i n } \{ \overline { { q } } _ { i } , \underline { { q } } _ { i + 1 } \} ]$

Let $q _ { i } ^ { \mathrm { u b } }$ be the updated expected value of the computing performance of resource $K _ { i } ,$ defined as

$$
\begin{array}{r l} & q _ {i} ^ {\mathrm{ub}} = \mathbb {E} \Big [ \tilde {q} _ {i t} \big | \tilde {q} _ {i t} \leq \min \Big \{\overline {{q}} _ {i}, \underline {{q}} _ {i + 1} \Big \} \Big ] \\ & \qquad = \int_ {\underline {{q}} _ {i}} ^ {\min \big \{\overline {{q}} _ {i}, \underline {{q}} _ {i + 1} \big \}} q _ {i t} g _ {i} \Big (q _ {i t} \big | \tilde {q} _ {i t} \leq \min \big \{\overline {{q}} _ {i}, \underline {{q}} _ {i + 1} \big \} \Big) d q _ {i t}, \end{array}\tag{19}
$$

where $\begin{array} { r } { g _ { i } ( q _ { i t } \vert \tilde { q } _ { i t } \le \operatorname* { m i n } \{ \overline { { q } } _ { i } , \underline { { q } } _ { i + 1 } \} ) = \frac { g _ { i } ( q _ { i t } ) } { G _ { i } ( \operatorname* { m i n } \{ \overline { { q } } _ { i } , \underline { { q } } _ { i + 1 } \} ) } } \end{array}$ for all $q _ { i t } \leq$ min $\{ \overline { { q } } _ { i } , \underline { { q } } _ { i + 1 } \}$ <sup>+</sup>. We use the updated expected computing performance of resources and implement the EnhancedRounding approach described in Section 4.2 to find the solution $\bar { \mathbf { x } } ^ { \mathrm { u \bar { b } } }$ for problem $\mathcal { P } _ { R } ^ { w } ( { \boldsymbol { \beta } } ^ { \prime } )$ . Then, we improve the solution $\mathbf { x } ^ { \mathrm { { u b } } }$ using the pruning procedure explained later. We calculate the total expected fraction processed by solution $\mathbf { x } ^ { \mathrm { { u b } } }$ as sum of the original expected value of computing performance of resources selected in the solution. We prune those resources from the solution $\mathbf { x } ^ { \mathrm { { u b } } }$ such that the total expected fraction processed by remaining resources is not less than $\beta ^ { \prime }$ . The following theorem asserts that the obtained solution is a feasible one for problem ${ \mathcal { P } } ^ { w } ( \beta )$ under the OC dependency structure.

Theorem 7. The EnhancedRounding<sup>OC</sup> approximation algorithm generates a feasible solution for problem ${ \mathcal { P } } ^ { w } ( \beta )$ under the OC dependency structure.

The proof is provided in the online appendix.

Algorithm 3 (EnhancedRoundin ${ \mathsf { P } } ^ { \mathsf { C } } )$ <sup>Output</sup>: a near-optimal schedule

1: $D = \varnothing , o p t = 0 ;$

2: Calculate the expected computing performance of resources using Equation (19);

3: Apply EnhancedRounding to solve problem $\bar { \mathcal { P } } _ { R } ^ { w } ( \beta ^ { \prime } )$ with expected values calculated in line $2 ;$

4: Prune resources from solution obtained in line 3 such that the total expected fraction processed by remaining resources is not less than $\beta ^ { \prime }$ and get $D ;$

5: opt total rental cost of D;

5.1.2. Lower Bound. To evaluate the performance of the proposed EnhancedRounding<sup>OC</sup> heuristic, we now propose a lower bound for the problem ${ \mathcal { P } } ^ { w } ( \beta )$ under the OC dependency structure. Let us update the distribution of the computing performance of the resources in the following manner:

For any two resources $K _ { i - 1 }$ and K for al $i \in \{ 2 , \ldots , m \}$ we assume that the fraction processed by the weaker resource, that is, $K _ { i - 1 } ,$ , is $\overline { { q } } _ { i - 1 }$ and thus update the distribution of the computing performance of resource $K _ { i }$ based on OC dependency such that its support becomes <sub>[</sub>max $\{ q _ { _ { i } } , \overline { { q } } _ { i - 1 } \} , \overline { { q } } _ { i } ]$

Let us define $q _ { i } ^ { \mathrm { l b } }$ as the updated expected value for the computing performance of each resource as follows:

$$
\begin{array}{r l} & q _ {i} ^ {\mathrm{lb}} = \mathbb {E} \Big [ \tilde {q} _ {i t} \big | \tilde {q} _ {i t} \geq \max \Big \{\underline {{q}} _ {i}, \overline {{q}} _ {i - 1} \Big \} \Big ] \\ & \quad = \int_ {\max \big \{\underline {{q}} _ {i}, \overline {{q}} _ {i - 1} \big \}} ^ {\overline {{q}} _ {i}} q _ {i t} g _ {i} \Big (q _ {i t} \big | \tilde {q} _ {i t} \geq \max \Big \{\underline {{q}} _ {i}, \overline {{q}} _ {i - 1} \Big \} \Big) d q _ {i t}, \end{array}\tag{20}
$$

where $\begin{array} { r } { g _ { i } ( q _ { i t } | \tilde { q } _ { i t } \geq \operatorname* { m a x } \{ \underline { { q } } _ { i } , \overline { { q } } _ { i - 1 } \} ) = \underline { { g } } _ { i } ( q _ { i t } ) } \\ { g _ { i } ( q _ { i t } | \tilde { q } _ { i t } \geq \operatorname* { m a x } \{ \underline { { q } } _ { i } , \overline { { q } } _ { i - 1 } \} ) = \underline { { g } } _ { i } ( \operatorname* { m a x } \{ \underline { { q } } _ { \cdot } , \overline { { q } } _ { i - 1 } \} ) } \end{array}$ for all $q _ { i t } \geq$ max $\{ \underline { { q } } _ { i } , \overline { { q } } _ { i - 1 } \}$ and $\overline { { G } } _ { i } ( . ) = 1 - G _ { i } ( . )$ <sup>i</sup>. We use the new expected computing performance of the resources and find the optimal solution of problem ${ \mathcal { P } } _ { R } ^ { w - L P } ( \beta )$ denoted by $\mathbf { x } ^ { \mathrm { { l b } } }$ . Theorem 8 states that solution $\mathbf { x } ^ { \mathrm { { l b } } }$ is not a feasible solution for problem ${ \mathcal { P } } _ { R } ^ { w - L P } ( \beta )$ under OC dependency and its objective function value is a lower bound for $\mathcal { P } _ { R } ^ { w - L P } ( \beta )$ under OC dependency, and also a lower bound for problem ${ \mathcal { P } } ^ { \hat { w } } ( \beta )$ under OC dependency.

Theorem 8. The optimal solution of problem ${ \mathcal { P } } _ { R } ^ { w - L P } ( \beta ) ,$ where the expected computing performance of resources are calculated using Equation (20) is a lower bound for problem ${ \mathcal { P } } ^ { w } ( \beta )$ under OC dependency.

The proof is provided in the online appendix.

5.1.3. Performance Guarantee. The following lemma expresses the performance guarantee of the proposed EnhancedRounding<sup>OC</sup> heuristic for problem ${ \mathsf { \hat { \mathcal P } } } ^ { w } ( \beta )$ under OC dependency structure.

Lemma 6. The proposed EnhancedRounding<sup>OC</sup> approach achieves the following performance guarantee for problem ${ \mathcal { P } } ^ { w } ( \beta )$ under OC dependency:

$$
\begin{array}{l} \frac {\overline {{Z}} _ {R} ^ {w} (\beta^ {\prime} , U ^ {*} , r ^ {*})}{Z ^ {w} (\beta)} \\ <   (1 + \delta) \left(\frac {q _ {j} ^ {\mathrm{lb}} - q _ {j - 1} ^ {\mathrm{lb}}}{q _ {g} ^ {\mathrm{ub}} - q _ {g - 1} ^ {\mathrm{ub}}}\right) \\ \times \left(\frac {\left(T q _ {g} ^ {\mathrm{ub}} - z _ {\beta} \sigma \sqrt {T} - 1\right) c _ {g - 1}}{\left(T q _ {j} ^ {\mathrm{lb}} - \beta\right) c _ {j - 1} + \left(\beta - T q _ {j - 1} ^ {\mathrm{lb}}\right) c _ {j} + I _ {2} S \left(q _ {j} ^ {\mathrm{lb}} - q _ {j - 1} ^ {\mathrm{lb}}\right)}\right). \end{array}
$$

## 5.2. Computing Tasks with Short Deadlines

In this section, we consider a case where the computing task needs to be processed in a short period, that is, the deadline $T < 3 0$ . We first show how the proposed solution in Section 4.2 might get affected when the deadline of the computing task is short.

In Section 4.1.3, we assumed that deadline T is sufficiently large and used the central limit theorem to approximate the distribution of the random variable $\textstyle \bar { \sum _ { t = 1 } ^ { T } } \sum _ { i = 0 } ^ { m } \tilde { q } _ { i t } x _ { i t }$ . In probability theory, the central limit theorem states that the probability distribution of the scaled mean of a random sample converges to a normal distribution as the sample size $( \mathrm { i } . \mathrm { e } . , T )$ is large enough. However, when the sample size is not large, the Berry-Esseen theorem can be used to obtain a bound on the maximal error of approximation between the true distribution of the random variable $\begin{array} { r } { ( \mathrm { i . e . , } \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } \tilde { q } _ { i t } x _ { i t } ) } \end{array}$ and the normal distribution (Berry 1941, Esseen 1942). Using this bound on the maximal error, we get a new value for $\alpha ,$ different from the one used in Section 4.1.3. Our proposed heuristics can solve the problem using the new value of α. We next explain how to obtain the value for α when T is not large enough $\left( \mathrm { i } . \mathrm { e } . , T < 3 0 \right)$ ).

Let $\tilde { q } _ { i t } - q _ { i }$ be independent random variables with $\mathbb { E } ( \tilde { q } _ { i t } - q _ { i } ) \stackrel { \cdot } { = } 0 , \mathbb { V } ( \tilde { q } _ { i t } - q _ { i } ) = v _ { i } ^ { 2 }$ , and $\mathbb { E } ( | \tilde { q } _ { i t } - q _ { i } | ^ { 3 } ) < \infty$ Then, according to the Berry-Esseen theorem, we have

$$
\left| \mathbb {P} \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \tilde {q} _ {i t} x _ {i t} \leq 1 \right] - \Phi_ {N} \left(\frac {1 - \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} q _ {i} x _ {i t}}{\sqrt {\sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \sigma_ {i} ^ {2} x _ {i t}}}\right) \right| \leq \varepsilon_ {0} \varpi_ {0},\tag{21}
$$

where $\begin{array} { r } { \varpi _ { 0 } = ( T \sum _ { i = 0 } ^ { m } v _ { i } ^ { 2 } ) ^ { - \frac { 3 } { 2 } } \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } \mathbb { E } ( | \widetilde { q } _ { i t } - q _ { i } | ^ { 3 } ) } \end{array}$ , and the lower bound established by Esseen (1956) on $\varepsilon _ { 0 }$ is $\varepsilon _ { 0 } \geq 0 . 4 0 9 7 .$ . Let <sup>x</sup> with components $x _ { i t }$ be a solution that satisfies

$$
\bar {\Phi} _ {N} \left(\frac {1 - \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} q _ {i} x _ {i t}}{\sqrt {\sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \sigma_ {i} ^ {2} x _ {i t}}}\right) \geq \varepsilon_ {0} \varpi_ {0} + \beta ,
$$

From the previous equation and Equation (21), the solution <sup>x</sup> also satisfies

$$
\mathbb {P} \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \tilde {q} _ {i t} x _ {i t} \geq 1 \right] \geq \varepsilon_ {0} \varpi_ {0} + \beta .\tag{22}
$$

Hence, we have

$$
\alpha = 1 + z _ {(\varepsilon_ {0} \varpi_ {0} + \beta)} \sqrt {\sum_ {t = 1} ^ {T} \sum_ {i = 0} ^ {m} \sigma_ {i} ^ {2} x _ {i t}},
$$

where $z _ { ( \varepsilon _ { 0 } \varpi _ { 0 } + \beta ) } = \Phi _ { N } ^ { - 1 } ( \varepsilon _ { 0 } \varpi _ { 0 } + \beta )$

Similar to Section 4.1.3, to avoid nonlinearity in the expectation constraint, we replace α with

$$
\beta^ {\prime} = 1 + z _ {(\varepsilon_ {0} \varpi_ {0} + \beta)} \sigma \sqrt {T},\tag{23}
$$

where $\sigma ^ { 2 } \geq \operatorname* { m a x } \{ \sigma _ { i } ^ { 2 } \}$ and $\scriptstyle \sum _ { i = 0 } ^ { m } x _ { i t } = 1$ . Therefore, when the deadline T is not large, our proposed Enhanced Rounding approach produces a feasible solution for problem $\mathcal { P } _ { R } ^ { w } ( { \boldsymbol { \beta } } ^ { \prime } )$ , where $\hat { \beta ^ { \prime } }$ is calculated using Equation (23), which is also a feasible solution for problem ${ \bar { \wp } } ^ { w } ( \beta )$ . Note that $\beta ^ { \prime }$ calculated in Equation (23) converges to $\beta ^ { \prime }$ calculated in Equation (15) when T is large enough.

Remark 1. When the deadline is short or the distribution of resources is broad, we may consider using an adaptive scheduling policy to further reduce the expected cost. One possible way to implement this idea, inspired by (Dziok et al. 2016), is described as follows. Basically, the idea is to use an explore-and-exploit scheme and learn on the way to finding a nearoptimal solution. Assuming some priors for the resources, we first compute a nonadaptive solution and run the job (e.g., for one hour) using the first resource. Next, the priors of all the remaining resources are updated using the observed fraction of the job completed in the first hour. This process is repeated until the job is completed. More generally, we could partition the time horizon into two phases: (1) a learning phase and (2) an optimization phase. The key challenge, of course, is to decide the optimal length of the learning phase. We can start with a short length and then gradually increase this length as more information is gathered about the distribution of resources. More sophisticated machine learning algorithms in the spirit of the multi-armed bandit theory (Bubeck et al. 2012) can be applied to overcome this challenge.

Table 2. Resource Computing Performance and Hourly Rental Cost

<table><tr><td>Computing resource</td><td> $\underline{q}_{i}$ </td><td> $\overline{q}_{i}$ </td><td> $q_{i}$ </td><td> $c_{i}( \$ )$ </td></tr><tr><td> $K_{1}$ </td><td>0.0400</td><td>0.0600</td><td>0.0506</td><td>0.096</td></tr><tr><td> $K_{2}$ </td><td>0.0693</td><td>0.1039</td><td>0.0876</td><td>0.288</td></tr><tr><td> $K_{3}$ </td><td>0.1058</td><td>0.1587</td><td>0.1338</td><td>0.672</td></tr></table>

## 6. Computational Results

In Section 6.1, we provide a simple illustrative example to highlight the efficiency of our proposed EnhancedRounding heuristic’s solution and demonstrate the shortcoming in the benchmark procedure. In Sections 6.2 and 6.3, we conduct numerical experiments to assess the performance of the proposed EnhancedRounding and EnhancedRounding<sup>OC</sup> heuristics, respectively.

## 6.1. An Illustrative Example

In this section, our goal is to provide a simple example to understand the benefit of using our proposed Enhanced Rounding heuristic approach over the benchmark approach. Consider a problem with deadline $T = 2 0$ and three computing resources, $K _ { 1 } , K _ { 2 } ,$ and $K _ { 3 }$ . Resource $K _ { 1 }$ (respectively, $K _ { 3 } )$ is the slowest (respectively, fastest). The computing resource $K _ { 1 }$ includes one VM instance, m5.large, offered by an Amazon EC2 cloud computing provider. The second and third computing resources (i.e., K and $K _ { 3 } )$ includes three and seven copies of the VM instance m5.large, respectively. We assume that the computing capability of the resource $K _ { i }$ at time unit $t \ ( \mathrm { i . e . , } \ \tilde { q } _ { i t } )$ follows a truncated beta distribution on the interval $[ \underline { { q } } _ { i } , \overline { { q } } _ { i } ] , 0 < \underline { { q } } _ { i } < \overline { { q } } _ { i } \leq 1$ . The truncated beta distributions are created from beta distribution Beta 2, 2 with support [0, 1]. We also assume that random variables $\tilde { q } _ { i t }$ are independent and their distributions’ supports do not overlap. Next, we randomly generate values $\underline { { q } } _ { 1 }$ and $\overline { { q } } _ { 1 } .$ . According to previous studies, there exists an increasing and concave relationship between the performance of a computing resource and the number of its nodes $( \mathrm { i . e . , }$ number of VM instances) (Barak and La’adan 1998, Ekanayake and Fox 2009, Ostermann et al. 2009). Therefore, for each computing resource $K _ { i }$ consisting of λ numbers of VM instance , $\underline { { q } } _ { i } = \chi ( \lambda ) \underline { { q } } _ { o }$ and $\overline { { { q } } } _ { i } = \chi ( \lambda ) \overline { { { q } } } _ { \varrho } ,$ , where χ λ is an increasing and concave function in λ. Specifically, we use $\chi ( \lambda ) = \sqrt { \lambda }$ . Hence, for computing resources $K _ { 2 }$ and $K _ { 3 }$ consisting of three and seven copies of the VM instance m5.large, we assume that $\underline { { { q } } } _ { 2 } = \sqrt { 3 } \ : \underline { { { q } } } _ { 1 } , \ : \ : \underline { { { q } } } _ { 3 } = \sqrt { 7 } \ : \underline { { { q } } } _ { 1 } , \ : \ : \overline { { { q } } } _ { 2 } = \sqrt { 3 } \ : \overline { { { q } } } _ { 1 } ,$ , and $\overline { { q } } _ { 3 } = \sqrt { 7 } \overline { { q } } _ { 1 }$ . The support, the expected value of the resource distributions, and the hourly rental cost of the resources are presented in Table 2. The other parameters for the example are reported in Table 3.

Table 3. Parameters in the Illustrative Example

<table><tr><td>m</td><td>T</td><td> $\beta$ </td><td> $\sigma$ </td><td>S ($)</td></tr><tr><td>3</td><td>20</td><td>0.90</td><td>0.01</td><td>0.10</td></tr></table>

Table 4. EnhancedRounding Solution in the Illustrative Example

<table><tr><td rowspan="2"></td><td colspan="3">Time unit</td></tr><tr><td>1 – 13</td><td>14 – 16</td><td>17 – 20</td></tr><tr><td>Enhanced Rounding solution</td><td> $K_1$ </td><td> $K_1$ </td><td> $K_2$ </td></tr><tr><td>Rental cost ($)</td><td> $13c_1 = 1.248$ </td><td> $3c_1 = 0.288$ </td><td> $4c_2 + S = 1.252$ </td></tr><tr><td>Expected processed fraction</td><td> $13q_1 = 0.6578$ </td><td> $3q_1 = 0.1518$ </td><td> $4q_2 = 0.3504$ </td></tr></table>

We used MATLAB to implement the proposed Enhanced Rounding approach to obtain an approximate solution for the illustrative example. The error bound (δ) for Enhanced Rounding was set to $0 . 6 .$ We also calculated a benchmark solution for the numerical example to highlight the efficiency of the solution obtained from the Enhanced Rounding approach compared with the benchmark solution. The benchmark solution is defined as a single computing resource solution corresponding to the cheapest feasible computing resource for the problem.

For this illustrative example, the value of $\beta ^ { \prime } = 1 +$ ${ z _ { \beta + \varepsilon _ { 0 } \varpi } } \sigma \sqrt { T }$ is equal to 1.1374. Therefore, $K _ { 2 }$ and $K _ { 3 }$ are able to finish 1.1374 of the computing task (in expectation) before T. Since $\begin{array} { r } { \left\lceil \frac { \beta ^ { \prime } } { q _ { 2 } } \right\rceil = 1 3 } \end{array}$ and $\begin{array} { r } { \left\lceil \frac { \beta ^ { \prime } } { q _ { 3 } } \right\rceil = 9 } \end{array}$ are smaller than $T = 2 0$ , the cheapest feasible resource for the illustrative example is resource $K _ { 2 } .$ . The benchmark solution uses resource $K _ { 2 }$ for 13 hours and its total rental cost is \$3.744.

The solution obtained from the Enhanced Rounding heuristic and benchmark solution are presented in Tables 4 and 5, respectively. As can be seen, in the EnhancedRounding heuristic solution, the computing task is processed using computing resource $K _ { 1 }$ during the first hours, and 0.6578 of the computing task is processed in expectation and $\beta ^ { \prime } - 0 . 6 5 \bar { 7 } 8 =$ 0.4796 is left for the rest of the horizon. However, in the benchmark solution, the computing resource $K _ { 2 }$ is used for the first 13 hours and the task is completed. At the end of hour 13, the total rental cost for the Enhanced Rounding solution is calculated as

Table 5. Benchmark Solution in the Illustrative Example

<table><tr><td rowspan="2"></td><td colspan="3">Time unit</td></tr><tr><td>1 – 13</td><td>14 – 16</td><td>17 – 20</td></tr><tr><td>Benchmark solution</td><td> $K_2$ </td><td>—</td><td>—</td></tr><tr><td>Rental cost ($)</td><td> $13c_2 = 3.744$ </td><td>—</td><td>—</td></tr><tr><td>Expected processed fraction</td><td> $13q_2 = 1.1388$ </td><td>—</td><td>—</td></tr></table>

Figure 1. (Color online) Enhanced Rounding Solution Versus Benchmark Solution  
![](/api/attachments/FTUGBPE6/fulltext/images/602152fc9412567a70911afdaac2c1002011f6293ce7d3c07e997f82a0231604.jpg)  
$1 3 c _ { 1 } = \$ 1 .24 8$ and for the benchmark solution, it is calculated as $1 3 c _ { 2 } = \$ 3.744$ . For hours 14 to $^ { 1 6 , }$ , the Enhanced Rounding solution continues to pick $K _ { 1 }$ and incurs a rental cost of $3 c _ { 1 } = \$ 0 .28 8$ during these three hours. It then chooses a stronger resource $( K _ { 2 } )$ for hours 17 to 20 to finish the process. The Enhanced Rounding solution incurs a switching cost of $S = 0 . 1$ and a rental cost of $4 c _ { 2 } = \$ 1.152$ during hours 17–20. Hence, the total rental cost for heuristic solution is calculated as $1 6 c _ { 1 } + 4 c _ { 2 } + S = \$ 2 .78 8$ . For benchmark solution, the total cost is $1 3 c _ { 2 } = \$ 3.744$ . In this illustrative example, compared with the benchmark solution, the proposed heuristic first selects a weaker and cheaper computing resource to process the computing task during the first 16 hours, and a stronger resource $( K _ { 2 } )$ to process the remaining task to finish by the deadline $\dot { T } = 2 0$ with lower total rental cost. The savings of the Enhanced Rounding solution over the benchmark solution for this example is about 0.2553. The difference between the rental cost of the heuristic solution and the benchmark solution across time units is illustrated in Figure 1. Although, the computing task in the heuristic and benchmark solutions is completed at 19.742 and 12.984 hours, respectively, the cloud user is charged for 20 and 13 hours because of the hourly based pricing scheme used by cloud computing providers.

## 6.2. Performance of the

## EnhancedRounding Heuristic

In this section, we first conduct numerical experiments to study the quality of the proposed Enhanced Rounding heuristic for small size problem instances. We compare the heuristic solution with the solution obtained from a scenario-based formulation of problem ${ \mathcal { P } } ^ { w } ( \beta )$ (described later) and the benchmark solution—a single-resource solution corresponding to the cheapest feasible computing resource to solve the problem. We also compare the heuristic solution with a lower bound and report the worst-case performance guarantee for each problem instance. We next evaluate the performance of the proposed EnhancedRounding heuristic for large size problem instances and compare the solution with the benchmark and the lower bound.

6.2.1. Scenario-Based Formulation of Problem ${ \mathcal { P } } ^ { w } ( \beta )$ Since problem ${ \mathcal { P } } ^ { w } ( { \boldsymbol { \beta } } )$ is a stochastic program, one possible approach for solving this problem is to approximate the uncertainty in the parameters $\tilde { q } _ { i t } \left( \forall i , t \right)$ by generating a set of scenarios and replace the probabilistic constraint with the set of constraints written for all these scenarios. A scenario is defined as one possible outcome of the uncertain parameters, $\tilde { q } _ { i t } .$ Since a large number of scenarios is possible, con sidering all of them in the decision-making process is not practical. However, if the number of scenarios used is large enough, the solution can be of good quality. In these experiments, each scenario ε is a randomly drawn <sup>q</sup> vector (i.e., $\mathbf { q } ^ { \varepsilon } = \{ q _ { 1 1 } ^ { \varepsilon } , \ldots , q _ { 1 T } ^ { \varepsilon } , \ldots ,$ $q _ { m 1 } ^ { \varepsilon } , \ldots , q _ { m T } ^ { \varepsilon } \} )$ . Hence, the scenario-based formulation of problem ${ \mathcal { P } } ^ { w } ( \beta )$ can be stated as follows:

$$
\min _ {\mathbf {x}, \mathbf {y}} \quad \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} c _ {i} x _ {i t} + S \sum_ {t = 1} ^ {T - 1} \sum_ {i = 1} ^ {m} y _ {i t}
$$

subject to Equations 1 ,  3 , and 4 ,

$$
\sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} q _ {i t} ^ {\varepsilon} x _ {i t} \geq 1 \qquad \varepsilon = 1, 2, \ldots , \zeta ,
$$

where $\zeta$ denotes the number of scenarios.

Table 6. Parameters in Small Size Problem Instances

<table><tr><td>No.</td><td>m</td><td>T</td><td> $\beta$ </td><td> $\sigma$ </td><td>S</td><td> $\varpi_0$ </td><td> $\beta'$ </td><td> $\min\{S/c_i\}$ </td><td> $\max\{S/c_i\}$ </td><td> $\min\{q_i\}$ </td><td> $\max\{q_i\}$ </td></tr><tr><td>1</td><td>10</td><td>10</td><td>0.91</td><td>0.01</td><td>1.5</td><td>0.1615</td><td>1.07</td><td>0.06</td><td>0.29</td><td>0.06</td><td>0.25</td></tr><tr><td>2</td><td>14</td><td>11</td><td>0.93</td><td>0.04</td><td>1.5</td><td>0.1247</td><td>1.32</td><td>0.03</td><td>0.16</td><td>0.06</td><td>0.26</td></tr><tr><td>3</td><td>19</td><td>12</td><td>0.94</td><td>0.03</td><td>1.2</td><td>0.1097</td><td>1.27</td><td>0.05</td><td>0.35</td><td>0.05</td><td>0.26</td></tr><tr><td>4</td><td>23</td><td>15</td><td>0.90</td><td>0.10</td><td>1.5</td><td>0.0952</td><td>1.63</td><td>0.02</td><td>0.17</td><td>0.04</td><td>0.24</td></tr><tr><td>5</td><td>30</td><td>21</td><td>0.92</td><td>0.02</td><td>1.4</td><td>0.0607</td><td>1.15</td><td>0.05</td><td>0.56</td><td>0.01</td><td>0.08</td></tr><tr><td>6</td><td>32</td><td>23</td><td>0.93</td><td>0.20</td><td>1.0</td><td>0.0942</td><td>2.92</td><td>0.01</td><td>0.16</td><td>0.02</td><td>0.20</td></tr><tr><td>7</td><td>37</td><td>25</td><td>0.91</td><td>0.01</td><td>1.3</td><td>0.0780</td><td>1.08</td><td>0.01</td><td>0.16</td><td>0.01</td><td>0.11</td></tr><tr><td>8</td><td>41</td><td>21</td><td>0.95</td><td>0.06</td><td>1.1</td><td>0.0882</td><td>1.69</td><td>0.07</td><td>0.20</td><td>0.01</td><td>0.14</td></tr><tr><td>9</td><td>44</td><td>16</td><td>0.90</td><td>0.05</td><td>1.2</td><td>0.0994</td><td>1.33</td><td>0.07</td><td>1.14</td><td>0.02</td><td>0.20</td></tr><tr><td>10</td><td>50</td><td>24</td><td>0.92</td><td>0.08</td><td>1.4</td><td>0.0691</td><td>1.66</td><td>0.05</td><td>0.93</td><td>0.02</td><td>0.14</td></tr></table>

Table 7. Performance of EnhancedRounding Heuristic on Small Size Problem Instances

<table><tr><td rowspan="2">No.</td><td rowspan="2">LB</td><td rowspan="2">CPLEX</td><td rowspan="2">Benchmark</td><td colspan="3">BaseM</td><td colspan="5">Enhanced Rounding</td></tr><tr><td>Time (seconds)</td><td>TC</td><td>%  $Sv_{bm}^{bench}$ </td><td>Time (seconds)</td><td>TC</td><td>%  $Sv_{er}^{cplex}$ </td><td>%  $Sv_{er}^{bench}$ </td><td>P-G</td></tr><tr><td>1</td><td>53.69</td><td>72.45</td><td>98.06</td><td> $1.16e^{-05}$ </td><td>78.14</td><td>20.31</td><td>0.005</td><td>72.45</td><td>0</td><td>26.12</td><td>1.35</td></tr><tr><td>2</td><td>106.21</td><td>130.64</td><td>170.92</td><td> $1.12e^{-05}$ </td><td>144.58</td><td>15.41</td><td>0.006</td><td>130.64</td><td>0</td><td>23.57</td><td>1.23</td></tr><tr><td>3</td><td>62.17</td><td>81.71</td><td>112.81</td><td> $1.48e^{-05}$ </td><td>98.58</td><td>12.61</td><td>0.007</td><td>81.71</td><td>0</td><td>27.57</td><td>1.31</td></tr><tr><td>4</td><td>157.25</td><td>168.26</td><td>225.20</td><td> $1.96e^{-05}$ </td><td>186.70</td><td>17.10</td><td>0.009</td><td>170.70</td><td>-1.45</td><td>24.20</td><td>1.09</td></tr><tr><td>5</td><td>93.15</td><td>124.84</td><td>170.76</td><td> $1.49e^{-05}$ </td><td>161.03</td><td>5.70</td><td>0.008</td><td>127.57</td><td>-2.19</td><td>25.30</td><td>1.37</td></tr><tr><td>6</td><td>158.35</td><td>165.29</td><td>224.73</td><td> $2.82e^{-05}$ </td><td>201.68</td><td>10.26</td><td>0.010</td><td>170.40</td><td>-3.09</td><td>24.17</td><td>1.08</td></tr><tr><td>7</td><td>210.84</td><td>213.42</td><td>281.08</td><td> $2.56e^{-05}$ </td><td>241.80</td><td>13.98</td><td>0.016</td><td>220.58</td><td>-3.35</td><td>21.53</td><td>1.05</td></tr><tr><td>8</td><td>171.72</td><td>191.23</td><td>262.35</td><td> $2.53e^{-05}$ </td><td>248.26</td><td>5.37</td><td>0.019</td><td>196.48</td><td>-2.75</td><td>25.11</td><td>1.14</td></tr><tr><td>9</td><td>64.07</td><td>77.56</td><td>109.68</td><td> $2.62e^{-05}$ </td><td>99.38</td><td>9.39</td><td>0.032</td><td>79.75</td><td>-2.82</td><td>27.29</td><td>1.24</td></tr><tr><td>10</td><td>140.78</td><td>142.64</td><td>189.84</td><td> $2.69e^{-05}$ </td><td>170.13</td><td>10.38</td><td>0.037</td><td>147.60</td><td>-3.48</td><td>22.25</td><td>1.05</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td>12.05</td><td></td><td></td><td>-1.91</td><td>24.71</td><td></td></tr></table>

Note. LB, lower bound; Bench, benchmark; TC, total cost; P-G, worst-case performance guarantee

6.2.2. Performance of EnhancedRounding Heuristic on Small Size Problem Instances. We evaluate the performance of the proposed EnhancedRounding approach for solving small size problem instances. The experimental design to generate small size numerical examples is as follows: We consider a set of VM instances offered by Amazon EC2. From each VM instance, we create many computing clusters with different size (i.e., number of nodes) to have a large pool of resources. We assume that the computing performance of resource $K _ { i }$ in the pool, that is, $\tilde { q } _ { i t } ,$ , follows a truncated beta distribution on the interval $[ \underline { { q } } _ { i } , \overline { { q } } _ { i } ] ,$ $0 < \underline { { q } } _ { i } < \overline { { q } } _ { i } \leq 1$ . The truncated beta distributions are created from beta distribution Beta 2, 2 . The random variables are independent and their supports do not overlap. The limits for these supports are randomly generated.

For all computing resources that represent a cluster of a specific VM instance, we calculate the limits as described in Section 6.1. Thus, for each computing resource $K _ { i }$ consisting of λ VM instances $\varrho , \underline { { q } } _ { i } = \chi ( \lambda ) \underline { { q } } _ { \iota }$ and $\overline { { \boldsymbol { q } } } _ { i } = \chi ( \lambda ) \overline { { \boldsymbol { q } } } _ { \varrho } ,$ where $\chi ( \lambda )$ is an increasing and concave function in λ. Specifically, we use $\chi ( \lambda ) = \sqrt { \lambda }$ . We set the hourly rental cost of a computing resource in the pool as the sum of hourly rental costs of the VM instances in that resource using price data from Amazon EC2.

We randomly generate the value of the two parameters $\beta$ and S from U [0.90, 0.99] and U [\$1, \$1.5] respectively. The value of parameter T is drawn randomly from U [5, 30]. The value of parameter m is drawn randomly from U [5, 50]. For each problem instance, the value of σ is set such that $\sigma ^ { 2 } \geq \mathrm { \hat { m a x } } \{ \sigma _ { i } ^ { 2 } \}$ For each problem instance, we consider six values (25, 50, 75, 100, 125, and 150) for ζ and pick the value that gives the smallest total rental cost. We generate 10 random problem instances with parameters presented in Table 6.

In Table 6, for each problem instance, the value o $\overline { { \beta ^ { \prime } } }$ is calculated using Equation (23). As explained in Section 5.2, when T is small, to get an approximation solution for the problem, the proposed Enhanced Rounding heuristic is implemented to solve problem $\mathcal { P } _ { R } ^ { w } ( { \boldsymbol { \beta } } ^ { \prime } )$ , where $\beta ^ { \prime } = 1 + \dot { z } _ { ( \varepsilon _ { 0 } \varpi _ { 0 } + \beta ) } \sigma \sqrt { T }$ and $\varepsilon _ { 0 } \geq 0 . 4 0 9 7$ (Esseen 1956). Here, we set the value of $\varepsilon _ { 0 }$ equal to 0.5. We calculate the value $\varpi _ { 0 }$ and $\beta ^ { \prime }$ for each problem instance as presented in Table 6.

We used CPLEX to solve the given scenario-based problem. CPLEX (2011) is recognized as the leading software for solving integer programs. The hardware used is an Intel Core i7 CPU running at 3.4 GHz. CPLEX can solve all problem instances presented in Table 6 in less than five hours. We used MATLAB to implement the proposed EnhancedRounding approach and calculate the benchmark solution and the lowerbound solution. The error bound (δ) for Enhanced Rounding was set to 0.6.

Table 8. Parameters in Large Size Problem Instances

<table><tr><td>No.</td><td>m</td><td>T</td><td> $\beta$ </td><td> $\sigma$ </td><td>S</td><td> $\beta'$ </td><td> $\min\{S/c_i\}$ </td><td> $\max\{S/c_i\}$ </td><td> $\min\{q_i\}$ </td><td> $\max\{q_i\}$ </td></tr><tr><td>1</td><td>570</td><td>50</td><td>0.90</td><td>0.10</td><td>1.5</td><td>1.91</td><td>0.03</td><td>1.22</td><td>0.008</td><td>0.24</td></tr><tr><td>2</td><td>594</td><td>53</td><td>0.97</td><td>0.07</td><td>1.3</td><td>1.96</td><td>0.01</td><td>0.33</td><td>0.006</td><td>0.17</td></tr><tr><td>3</td><td>630</td><td>60</td><td>0.95</td><td>0.10</td><td>1.3</td><td>2.27</td><td>0.01</td><td>0.58</td><td>0.006</td><td>0.18</td></tr><tr><td>4</td><td>705</td><td>47</td><td>0.93</td><td>0.02</td><td>1.0</td><td>1.20</td><td>0.01</td><td>0.49</td><td>0.004</td><td>0.13</td></tr><tr><td>5</td><td>753</td><td>45</td><td>0.91</td><td>0.01</td><td>1.2</td><td>1.09</td><td>0.02</td><td>0.89</td><td>0.007</td><td>0.22</td></tr><tr><td>6</td><td>842</td><td>62</td><td>0.97</td><td>0.03</td><td>1.1</td><td>1.74</td><td>0.02</td><td>0.84</td><td>0.006</td><td>0.20</td></tr><tr><td>7</td><td>871</td><td>67</td><td>0.92</td><td>0.05</td><td>1.4</td><td>1.58</td><td>0.01</td><td>0.76</td><td>0.007</td><td>0.27</td></tr></table>

Table 9. Performance of Proposed EnhancedRounding Heuristic on Large Size Problem Instances

<table><tr><td rowspan="2">No.</td><td rowspan="2">LB</td><td rowspan="2">Bench</td><td colspan="3">BaseM</td><td colspan="4">EnhancedRounding</td></tr><tr><td>Time (seconds)</td><td>TC</td><td> $\%Sv_{bm}^{bench}$ </td><td>Time (seconds)</td><td>TC</td><td> $\%Sv_{er}^{bench}$ </td><td>P-G</td></tr><tr><td>1</td><td>170.69</td><td>240.86</td><td> $7.59e^{-04}$ </td><td>210.12</td><td>12.76</td><td>1.26</td><td>184.21</td><td>23.52</td><td>1.08</td></tr><tr><td>2</td><td>210.92</td><td>316.30</td><td> $9.40e^{-05}$ </td><td>271.05</td><td>14.31</td><td>1.64</td><td>230.92</td><td>26.99</td><td>1.09</td></tr><tr><td>3</td><td>265.25</td><td>372.94</td><td> $1.12e^{-04}$ </td><td>357.45</td><td>4.15</td><td>1.98</td><td>292.42</td><td>21.59</td><td>1.10</td></tr><tr><td>4</td><td>138.59</td><td>212.69</td><td> $1.11e^{-04}$ </td><td>190.59</td><td>10.39</td><td>2.15</td><td>161.57</td><td>24.03</td><td>1.17</td></tr><tr><td>5</td><td>83.74</td><td>140.04</td><td> $1.20e^{-04}$ </td><td>131.25</td><td>6.28</td><td>2.53</td><td>111.16</td><td>20.63</td><td>1.33</td></tr><tr><td>6</td><td>145.59</td><td>309.94</td><td> $1.08e^{-04}$ </td><td>174.51</td><td>11.16</td><td>2.49</td><td>229.15</td><td>26.06</td><td>1.57</td></tr><tr><td>7</td><td>126.18</td><td>206.81</td><td> $1.25e^{-04}$ </td><td>174.51</td><td>15.62</td><td>2.75</td><td>148.38</td><td>28.25</td><td>1.18</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td>10.67</td><td></td><td></td><td>24.44</td><td></td></tr></table>

Note. LB, lower bound; Bench, benchmark; TC, total cost; P-G, worst-case performance guarantee.

In Table $^ { 7 , }$ for each problem instance presented in Table 6, we compare the EnhancedRounding solution with the lower-bound, CPLEX, BaseM, and benchmark solutions. The lower bound is calculated based on results explained in Theorem 5. Table 7 summarizes the computational results, including the total rental cost for the lower-bound, CPLEX, benchmark, BaseM, and Enhanced Rounding solutions, and it reports the computational time (in seconds) for BaseM and EnhancedRounding. For each problem instance, we measure the quality of the EnhancedRounding solution by proving the worstcase performance guarantee values and the savings of EnhancedRounding over the benchmark solution as $\mathrm { S v } _ { e r } ^ { b e n c h } =$ (Benchmark <sup>−</sup> EnhancedRounding)/Benchmark 100. We also calculate the saving of BaseM over benchmark solution as $\mathrm { S v } _ { b m } ^ { b e n c h } =$ (Benchmark <sup>−</sup> BaseM)/Benchmark × 100. We report the savings of CPLEX over EnhancedRounding solution as ${ \bf S v } _ { e r } ^ { c p l e x } =$ (CPLEX <sup>−</sup> EnhancedRounding)/CPLEX 100.

We note that the average savings of the proposed Enhanced Rounding approach over benchmark is 24.71% across 10 random problem instances. The computational time for BaseM is much less than that of EnhancedRounding. However, the time taken for EnhancedRounding is only a few seconds. Thus, EnhancedRounding can be used in practice, and offers considerable savings over BaseM. CPLEX saves 1.91% on average over the EnhancedRounding across 10 problem instances, implying that there is no substantial difference between these two procedures.

6.2.3. Performance of the EnhancedRounding Heuristic on Large Size Problem Instances. In this section, we evaluate the performance of the proposed Enhanced Rounding approach for solving large size problem instances under base model assumptions. The experimental design to generate large size problem instances is as follows. We use the procedure explained in Section 6.2 to create a random sample of m resources. We ran domly generate the value of the two parameters $\beta$ and S from U [0.90, 0.99] and U [\$1, \$1.5] respectively. The value of parameter T is drawn randomly from U [40, 70]. The value of parameter m is drawn randomly from U [500,900], which is a reasonable range for practical problems. According to a RightScale survey in 2017, 8% of respondents were running more than 1,000 VM instances and 42% were running between 50 and 1,000 VM instances (Weins 2018). For each problem instance, the value of σ is set such that $\sigma ^ { 2 } \geq \operatorname* { i m a x } \{ \sigma _ { i } ^ { 2 } \}$ . Based on the given design, we generate seven random problem instances with the parameters presented in Table 8. For all problem instances, the value of $\beta ^ { \prime }$ calculated in Equation (23) converges to value of $\dot { \beta } ^ { \prime }$ calculated in Equation (15).

Table 10. Parameters in Small Size Problem Instances Under OC

<table><tr><td>No.</td><td>m</td><td>T</td><td> $\beta$ </td><td> $\sigma$ </td><td>S</td><td> $\varpi_0$ </td><td> $\beta'$ </td><td> $\min\{S/c_i\}$ </td><td> $\max\{S/c_i\}$ </td><td> $\min\{q_i\}$ </td><td> $\max\{q_i\}$ </td></tr><tr><td>1</td><td>8</td><td>9</td><td>0.90</td><td>0.02</td><td>1.4</td><td>0.1933</td><td>1.16</td><td>0.14</td><td>1.11</td><td>0.05</td><td>0.19</td></tr><tr><td>2</td><td>12</td><td>10</td><td>0.91</td><td>0.01</td><td>1.5</td><td>0.1399</td><td>1.06</td><td>0.10</td><td>0.74</td><td>0.05</td><td>0.20</td></tr><tr><td>3</td><td>17</td><td>15</td><td>0.94</td><td>0.05</td><td>1.3</td><td>0.1191</td><td>1.65</td><td>0.06</td><td>0.55</td><td>0.05</td><td>0.28</td></tr><tr><td>4</td><td>21</td><td>16</td><td>0.93</td><td>0.08</td><td>1.1</td><td>0.0914</td><td>1.63</td><td>0.04</td><td>0.39</td><td>0.06</td><td>0.29</td></tr><tr><td>5</td><td>29</td><td>22</td><td>0.95</td><td>0.03</td><td>1.4</td><td>0.0757</td><td>1.32</td><td>0.04</td><td>0.37</td><td>0.04</td><td>0.24</td></tr><tr><td>6</td><td>30</td><td>25</td><td>0.91</td><td>0.09</td><td>1.0</td><td>0.0703</td><td>1.72</td><td>0.03</td><td>0.25</td><td>0.04</td><td>0.24</td></tr><tr><td>7</td><td>35</td><td>23</td><td>0.91</td><td>0.04</td><td>1.2</td><td>0.0825</td><td>1.32</td><td>0.01</td><td>0.23</td><td>0.01</td><td>0.11</td></tr><tr><td>8</td><td>40</td><td>27</td><td>0.95</td><td>0.06</td><td>1.5</td><td>0.0705</td><td>1.68</td><td>0.03</td><td>0.24</td><td>0.03</td><td>0.22</td></tr><tr><td>9</td><td>43</td><td>20</td><td>0.90</td><td>0.01</td><td>1.2</td><td>0.0805</td><td>1.07</td><td>0.03</td><td>1.08</td><td>0.03</td><td>0.23</td></tr><tr><td>10</td><td>50</td><td>26</td><td>0.92</td><td>0.12</td><td>1.1</td><td>0.0848</td><td>2.09</td><td>0.01</td><td>0.19</td><td>0.02</td><td>0.25</td></tr></table>

Table 11. Performance of Proposed EnhancedRounding<sup>OC</sup> Heuristic on Small Size Problem Instances

<table><tr><td rowspan="2">No.</td><td rowspan="2">LB</td><td rowspan="2">Bench</td><td colspan="4">EnhancedRounding $^{OC}$ </td></tr><tr><td>Time (seconds)</td><td>TC</td><td>% $S_{v_{oc}^{bench}}$ </td><td>P-G</td></tr><tr><td>1</td><td>29.50</td><td>64.28</td><td>0.01</td><td>57.14</td><td>11.10</td><td>1.94</td></tr><tr><td>2</td><td>41.44</td><td>71.92</td><td>0.02</td><td>60.10</td><td>16.43</td><td>1.45</td></tr><tr><td>3</td><td>36.68</td><td>86.70</td><td>0.03</td><td>76.67</td><td>11.57</td><td>2.09</td></tr><tr><td>4</td><td>46.66</td><td>94.61</td><td>0.05</td><td>82.70</td><td>12.59</td><td>1.77</td></tr><tr><td>5</td><td>102.68</td><td>174.36</td><td>0.08</td><td>145.82</td><td>16.37</td><td>1.42</td></tr><tr><td>6</td><td>102.34</td><td>201.62</td><td>0.09</td><td>173.17</td><td>14.11</td><td>1.69</td></tr><tr><td>7</td><td>121.48</td><td>216.08</td><td>0.12</td><td>185.10</td><td>14.34</td><td>1.52</td></tr><tr><td>8</td><td>167.26</td><td>276.49</td><td>0.18</td><td>234.65</td><td>15.13</td><td>1.40</td></tr><tr><td>9</td><td>68.88</td><td>125.67</td><td>0.23</td><td>104.85</td><td>16.57</td><td>1.52</td></tr><tr><td>10</td><td>151.83</td><td>310.55</td><td>0.33</td><td>264.14</td><td>14.95</td><td>1.74</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td>14.32</td><td></td></tr></table>

Note. LB, lower bound; Bench, benchmark; TC, total cost; P-G, worst-case performance guarantee.

The computational study revealed that CPLEX was not able to solve any of the problem instances in five hours. As shown in Section $^ { 4 , }$ problem ${ \mathcal { P } } ^ { w } ( \beta )$ is NPcomplete and hence, CPLEX is not capable to handle large size problem instances. Table 9 summarizes the computational results, including the lower-bound, benchmark, BaseM, and EnhancedRounding solutions, and the computational time (in seconds) for BaseM and EnhancedRounding . We report the savings of BaseM and EnhancedRounding over the benchmark solution. We also provide the worst-case performance guarantee for EnhancedRounding for each problem instance. It is notable that for large size problem instances, the EnhancedRounding approach again takes a longer time than BaseM, but it provides significant saving over BaseM. The average saving of EnhancedRounding over the benchmark is 24.44%.

## 6.3. Performance of the

In this section, we relax the independence assumption and study the performance of the proposed EnhancedRounding<sup>OC</sup> approach for problem ${ \mathsf { \bar { \boldsymbol { \mathcal { P } } } } } ^ { w } ( \beta )$

on small and large size problem instances when the corresponding distributions of the resources are de pendent based on the OC dependency structure.

## EnhancedRounding<sup>OC</sup> Heuristic

6.3.1. Performance of the EnhancedRounding<sup>OC</sup> Heuristic on Small Size Problem Instances. We assess the performance of the proposed EnhancedRounding<sup>OC</sup> heuristic for solving small size problem instances. To proceed, similar to procedure we used in Section 6.2.2, we generate 10 problem instances and we assume that random variables $\tilde { q } _ { i t }$ are dependent and that the supports of the distribution of resources have overlap. The randomly generated problem instances are presented in Table 10. For each problem instance presented in Table 10, we implement the EnhancedRounding<sup>OC</sup> heuristic and compare the result with the benchmark and lower bound proposed in Section 5.1. Table 11 illustrates the lower-bound, benchmark, and EnhancedRounding<sup>OC</sup> solutions and computational time (in seconds) for the EnhancedRounding<sup>OC</sup> heuristic. Table 11 also reports the value of the worst-case performance guarantee. We report the savings of EnhancedRounding<sup>OC</sup> over the benchmark as $\mathbf { S } \mathbf { v } _ { o c } ^ { b e n c h } =$ (Benchmark <sup>−</sup> EnhancedRounding<sup>OC</sup>)/Benchmark 100. The computational results show that the average saving of the EnhancedRounding<sup>OC</sup> over the benchmark is 14.32% for small size problem instances.

6.3.2. Performance of the EnhancedRounding<sup>OC</sup> Heuris tic on Large Size Problem Instances. Next, we study the performance of the EnhancedRounding<sup>OC</sup> heuristic solution on large size problem instances when the corresponding distributions of the resources are dependent based on the OC dependency structure and the support of the distribution of resources are allowed to share some interval. We randomly generate seven problem instances based on procedure explained in Section 6.2.3. The problem instances are presented in Table 12. For each problem instance, we present the total rental cost of the lower-bound, benchmark, and EnhancedRounding<sup>OC</sup> solutions in Table 13. We also report the computational time of EnhancedRounding<sup>OC</sup>, worst-case performance guarantee, and the savings of EnhancedRounding<sup>OC</sup> over the benchmark solution. The results show that the average saving of EnhancedRounding<sup>OC</sup> over the benchmark is 14.82% for large size problem instances.

Table 12. Parameters in Large Size Problem Instances Under OC

<table><tr><td>No.</td><td>m</td><td>T</td><td> $\beta$ </td><td> $\sigma$ </td><td>S</td><td> $\beta'$ </td><td> $\min\{S/c_i\}$ </td><td> $\max\{S/c_i\}$ </td><td> $\min\{q_i\}$ </td><td> $\max\{q_i\}$ </td></tr><tr><td>1</td><td>555</td><td>56</td><td>0.90</td><td>0.01</td><td>1.5</td><td>1.10</td><td>0.05</td><td>2.23</td><td>0.010</td><td>0.35</td></tr><tr><td>2</td><td>583</td><td>51</td><td>0.97</td><td>0.05</td><td>1.2</td><td>1.67</td><td>0.01</td><td>0.40</td><td>0.006</td><td>0.18</td></tr><tr><td>3</td><td>625</td><td>60</td><td>0.94</td><td>0.07</td><td>1.0</td><td>1.65</td><td>0.06</td><td>0.55</td><td>0.050</td><td>0.28</td></tr><tr><td>4</td><td>702</td><td>45</td><td>0.96</td><td>0.02</td><td>1.4</td><td>1.63</td><td>0.04</td><td>0.39</td><td>0.060</td><td>0.29</td></tr><tr><td>5</td><td>747</td><td>42</td><td>0.91</td><td>0.04</td><td>1.3</td><td>1.32</td><td>0.04</td><td>0.37</td><td>0.04</td><td>0.24</td></tr><tr><td>6</td><td>839</td><td>62</td><td>0.93</td><td>0.03</td><td>1.5</td><td>1.72</td><td>0.03</td><td>0.25</td><td>0.04</td><td>0.24</td></tr><tr><td>7</td><td>862</td><td>65</td><td>0.92</td><td>0.01</td><td>1.1</td><td>1.11</td><td>0.02</td><td>0.76</td><td>0.006</td><td>0.19</td></tr></table>

Table 13. Performance of Proposed EnhancedRounding<sup>OC</sup> Heuristic on Large Size Problem Instances

<table><tr><td rowspan="2">No.</td><td rowspan="2">LB</td><td rowspan="2">Bench</td><td colspan="4">EnhancedRoundingOC</td></tr><tr><td>Time (seconds)</td><td>TC</td><td>%Svbenchoc</td><td>P-G</td></tr><tr><td>1</td><td>68.14</td><td>114.88</td><td>5.22</td><td>96.44</td><td>16.05</td><td>1.42</td></tr><tr><td>2</td><td>177.51</td><td>256.53</td><td>5.96</td><td>248.74</td><td>13.19</td><td>1.40</td></tr><tr><td>3</td><td>152.48</td><td>274.90</td><td>6.97</td><td>239.08</td><td>13.03</td><td>1.57</td></tr><tr><td>4</td><td>120.42</td><td>229.30</td><td>7.25</td><td>197.22</td><td>13.99</td><td>1.64</td></tr><tr><td>5</td><td>57.38</td><td>157.27</td><td>7.42</td><td>134.33</td><td>14.59</td><td>2.34</td></tr><tr><td>6</td><td>112.30</td><td>212.40</td><td>8.13</td><td>177.46</td><td>16.45</td><td>1.58</td></tr><tr><td>7</td><td>147.48</td><td>205.53</td><td>8.62</td><td>171.75</td><td>16.43</td><td>1.16</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td>14.82</td><td></td></tr></table>

Note. LB, lower bound; Bench, benchmark; TC, total cost; P-G, worst-case performance guarantee.

## 6.4. Sensitivity Analysis

We examine changes in the value of the total rental cost of solution obtained from EnhancedRounding with respect to changes in $\sigma , \beta ,$ and T. When either σ, $\beta ,$ or T increase, total rental cost increases because the time constraint tightens $\begin{array} { r } { \mathrm { ( i . e . , ~ } \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } q _ { i } x _ { i t } \textgreater 1 + } \end{array}$ ${ z _ { \beta } } \sigma { \sqrt { T } }$ is a tighter constraint). We also evaluate the quality of the performance guarantee with respect to changes in these three parameters $( \sigma , \beta ,$ , and T). It can be analytically seen that the performance guarantee calculated in Theorem 6 is increasing in σ. When σ increases, the performance guarantee gets worse because the constraint $\begin{array} { r } { \sum _ { t = 1 } ^ { T } \breve { \sum _ { i = 0 } ^ { m } } q _ { i } x _ { i t } \geq \bar { 1 } + z _ { \beta } \sigma \sqrt { T } } \end{array}$ gets tighter while $\begin{array} { r } { \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } q _ { i } x _ { i t } \geq \bar { \beta } } \end{array}$ does not change. On the other hand, it is difficult to make an analytical statement about the how the performance guarantee reacts to changes in $\beta$ and T. Thus, we numerically study these behaviors. Figure 2 demonstrates how the performance guarantee changes with respect to changes in $\beta$ and T. As Figure 2 shows, when $\beta$ increases, the performance guarantee improves. This is because both constraints $\begin{array} { r } { \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } q _ { i } x _ { i t } \sum 1 + z _ { \beta } \sigma \sqrt { T } } \end{array}$ and $\begin{array} { r } { \sum _ { t = 1 } ^ { T } \sum _ { i = 0 } ^ { m } q _ { i } x _ { i t } \geq \beta } \end{array}$ get tighter.

## 7. Cidewalk Log File Processing

To lend further credibility to our approach, we contacted a real company (Cidewalk) that uses cloud computing (Amazon EC2) to identify an offline fixedsize-with-deadline computing problem of the kind we study here. Cidewalk is a mobile ad delivery platform that is in the business of running mobile inapp ad campaigns for small to medium sized firms. Cidewalk faces a routine log file processing problem that needs to solved daily. In this section, we discuss how the proposed Enhanced Rounding approach can be applied to Cidewalk’s problem to save rental cost.

To better understand the computing problem faced by Cidewalk, it is necessary to provide a brief de scription of mobile ad delivery. When a mobile app user opens an app, an opportunity to display an inapp ad is created. This opportunity is sold on a realtime basis in a mobile ad exchange (e.g., MobPub). If Cidewalk’s bid on the opportunity is won, a request goes to one of Cidewalk’s ad servers to supply an ad. After displaying the ad, a log of this impression is created. This log records detailed data on the specifics of the ad shown, time shown, and other information concerning the event. If the visitor clicks on the ad, an ad server logs this event. It is important to note that the ad server that records the impression may be different from the one that records the click (although both are likely to be in the same data center). Once every day, all the ad servers purge their logs to a local log processor at the data center. These local log processors (one for each data center), in turn, broadcast their contents to a master log processor that collects the entire log (consisting of millions of log files) for the day. Thus at the end of each day, the raw log data are consolidated into two files (impressions log file and clicks log file) that are processed to match impressions with clicks and create a single data record for the joint impression and possible click event. This consolidated log is analyzed to update the status of the different campaigns being run (impressions served, clicks acquired) as well as to generate trends regarding the cost of the impressions and the clicks generated. The cost of impressions provides feedback to Cidewalk’s real-time bidding platform that bids on different mobile ad exchanges to acquire impressions for ad delivery. This log file processing task is performed daily. Usually, processing needs to start at around 9 p.m. on each day (when impression volume starts to reduce) and must be completed before 9 a.m. the next day, since the results of log file processing are needed as input to plan the ad campaigns that are run each day.

Figure 2. (Color online) Changes in Performance Guarantee with Respect to Changes in $\beta$ and T  
![](/api/attachments/FTUGBPE6/fulltext/images/a52df380b4a52f754b8a61c58fdf1f9bfe0081016a93554cc1e8b4abb475bb52.jpg)

![](/api/attachments/FTUGBPE6/fulltext/images/ced974ece4b743e9605a44b6e8b0d3ff95d1f879a799c3bae80cf9444dd6b8af.jpg)

Table 14. Parameters in Cidewalk Problem

<table><tr><td>m</td><td>T</td><td> $\beta$ </td><td> $\sigma$ </td><td>S</td><td> $\varpi_0$ </td><td> $\beta'$ </td><td> $\min\{S/c_i\}$ </td><td> $\max\{S/c_i\}$ </td><td> $\min\{q_i\}$ </td><td> $\max\{q_i\}$ </td></tr><tr><td>1,000</td><td>12</td><td>0.97</td><td>0.05</td><td>1.5</td><td>0.0372</td><td>1.39</td><td>0.02</td><td>1.27</td><td>0.01</td><td>0.38</td></tr></table>

Based on our conservations with Cidewalk engineers, we considered the parameters presented in Table 14 to illustrate the advantage of our approach. The computing resource $K _ { i }$ was assigned a truncated beta distribution on support $[ \underline { { q } } _ { i } , \overline { { q } } _ { i } ]$ that represented the fraction of the task this resource could complete within one hour, during a particular time unit t $( t = 1 , \ldots , 1 2 )$ . Similar to the procedure explained in Section 6.2.2, we generate the support of the distributions. We assume that the computing performance of resources are independent and their distributions supports have no overlap. The value of β is calculated using Equation (23).

We next picked the cheapest computing resource that could solve the problem without exceeding the time constraint (T 12). The total rental cost of this single resource (comprised of a cluster of VM instances) was \$179.98. However, our proposed EnhancedRounding solution assigns the computing task to three different computing resources with total rental cost of \$129.74. This would save about 27.91% of Cidewalk’s rental cost. Incidentally, the problem could not be solved in CPLEX within a time limit of five hours. Given this, finding a solution using a stateof-art solver such as CPLEX is ruled out, since just finding the solution takes more than five hours, let alone solving the problem once a possible CPLEX solution is implemented. The company is considering the possibility of implementing our approach.

## 8. Conclusion

We set ourselves the task of reducing rental costs for recurring, offline computing tasks that need to be solved within a specified deadline. Offline computingintensive tasks are good candidates to be solved using a divide-and-conquer strategy. The main idea is to use a carefully chosen set of computing resources in a sequence to solve the problem. However, current practice typically solves the problem using a single resource (which could be a cluster of servers). As companies migrate their computing tasks to the cloud, they must be aware that unlike in-house computing installations, each hour of usage incurs cost. Thus, new computing strategies need to be developed to exploit the price-performance relationships of the diverse computing configurations offered by cloud providers. Our contributions are two-fold. First, we identify an opportunity to save rental costs that can potentially generate huge efficiency gains for companies. Next, we provide a practical, easy-to-implement solution to this problem.

To our knowledge, this research is the first attempt to study the problem of lowering the rental cost of computing services from the perspective of a cloud user. We analyze the relationship between the unit rental cost and performance of various computing resources offered by cloud computing providers and develop a near-optimal solution that uses a switching solution, rather than a single-resource solution. A theoretical (worst-case) performance guarantee for the solution is proposed. An additional aspect of interest is that our solution can handle cases where the computing resources have random, but correlated processing capabilities. Dependencies across processing resources are addressed using an OC that ensures that a stronger resource will always process a higher fraction of the task than a weaker one. Beyond the worst-case performance guarantee, we extensively study performance using computational experimentation to find that the proposed near-optimal solution outperforms the benchmark solution. We also illustrate the value of our approach using an example from Cidewalk Inc., a company that needs to solve an offline, log file processing problem on a recurring basis.

An insight of our study is that a task’s deadline pressure is an important determinant of the extent of savings that arise from a multiple-resource solution (one that uses switching) over a single-resource solution (the benchmark used in this study). Deadline pressure can be understood as the following. For a given set of computing resources, let us consider the fraction of the task that will be finished by the weakest (respectively, strongest) resource if the resource is used for T hours. If either of these values is close to 1, then the task is either very simple (since the weakest resource can finish it close to the deadline) or the task is very complex (only the strongest resource can finish it on time). The switching solution will be more useful when neither of the previous fractions are close to 1. Otherwise, a simple heuristic is to use the weakest machine or the strongest machine to solve the problem. A more general take-away is that the switching solution is more useful when the fraction completed in T hours is not close to 1 for any of the available computing resources. Otherwise, picking the weakest feasible computing resource to solve the problem will provide a good heuristic solution. Another insight is that the multiple-resource solution is more beneficial when the switching cost is small relative to the total rental cost. This is natural: If the switching cost is high, a singleresource solution is likely to be better.

This study is not without limitations. We only target a certain kind of computing task, namely, a fixed-size, offline computing task that occurs frequently and needs to be solved with a deadline constraint. Many examples of cloud-based solutions, on the other hand, are real-time computing tasks. Although the idea of switching from one resource to another might still be advantageous, care must be taken that the real-time task being supported does not get disrupted during the switch (at the very least, the drop in performance should not be noticeable to end users). The other feature of this study that could be extended is to use a combination of fixed-price and “spot rental” computing resources to further reduce rental cost. Here, we only considered fixed-price computing resources.

## Endnotes

<sup>1</sup> The <sup>x</sup> variables are used to code the usage of a particular resource (on/off variables) and the <sup>y</sup> variables are used to model a resource switch (start/stop variables). These definitions follow the convention used in resource-constrained project scheduling (Artigues et al. 2015).

<sup>2</sup> Since we use the normal distribution to approximate the binomial distribution, it is possible that our proposed solution slightly violates the probabilistic guarantee. This infeasibility can be avoided by precisely computing the buffer (using the binomial distribution) such that our proposed policy satisfies the probabilistic guarantee that the process of the computing task is completed with probability β.

<sup>3</sup> A letter from Venkat Kolluri, chief executive officer of Cidewalk Inc., describing our interaction with the company, is provided in the online appendix.

## References

Anwar N, Deng H (2018) Elastic scheduling of scientific workflows under deadline constraints in cloud computing environments. Future Internet 10(1):5–28.

Artigues C, Koné O, Lopez P, Mongeau M (2015) Mixed-integer linear programming formulations. Schwindt C, Zimmermann J, eds. Handbook on Project Management and Scheduling, vol. 1 (Springer, New York), 17–41.

Awad A, El-Hefnawy N, Abdel\_kader H (2015) Enhanced particle swarm optimization for task scheduling in cloud computing environments. Procedia Comput. Sci. 65:920–929.

Aymerich FM, Fenu G, Surcis S (2009) A real time financial system based on grid and cloud computing. Proc. 2009 ACM Symp. Appl. Comput. (Association for Computing Machinery, New York), 1219–1220.

Barak A, La’adan O (1998) The MOSIX multicomputer operating system for high performance cluster computing. Future Generation Comput. Systems 13(4–5):361–372.

Berry AC (1941) The accuracy of the Gaussian approximation to the sum of independent variates. Trans. Amer. Math. Soc. 49(1): 122–136.

Billingsley P (2008) Probability and Measure (John Wiley & Sons, Hoboken, NJ).

Blazewicz J, Ecker KH, Pesch E, Schmidt G, Weglarz J (2013) Scheduling Computer and Manufacturing Processes (Springer Sci ence & Business Media, New York).

Braun TD, Siegel HJ, Beck N, Bol¨ oni LL, Maheswaran M, Reuther AI,¨ Robertson JP, et al. (2001) A comparison of eleven static heuristics for mapping a class of independent tasks onto heterogeneous distributed computing systems. J. Parallel Distributed Comput. 61(6):810–837.

Bubeck S, Cesa-Bianchi N (2012) Regret analysis of stochastic and nonstochastic multi-armed bandit problems. Foundation Trends Machine Learn. 5(1):1–122.

Buyya R, Beloglazov A, Abawajy J (2010) Energy-efficient management of data center resources for cloud computing: A vision, architectural elements, and open challenges. Working paper, University of Melbourne, Melbourne, Australia.

Chakaravarthy VT, Choudhury AR, Natarajan SR, Roy S (2013) Knapsack cover subject to a matroid constraint. Seth A, Vishnoi NK, eds. 2013 Leibniz Internat. Proc. Informatics (Schloss Dagstuhl Leibniz-Zentrum fuer Informatik, Dagstuhl, Germany), 275–286.

Chen H, Zhu X, Guo H, Zhu J, Qin X, Wu J (2015) Toward energyefficient scheduling for real-time tasks under uncertain cloud computing environment. J. Systems Software 99:20–35.

Cheng HK, Li Z, Naranjo A (2016) Research note—Cloud computing spot pricing dynamics: Latency and limits to arbitrage. Inform. Systems Res. 27(1):145–165.

Cidewalk (2017) Private e-mail and in-person communication.

Columbus L (2017) Roundup of cloud computing forecasts. Forbe (April 29), https://www.forbes.com/sites/louiscolumbus/2017 04/29/roundup-of-cloud-computing-forecasts-2017/#640e448e31e8

CPLEX (2011) IBM ILOG CPLEX Optimization Studio: CPLEX User’s Manual, version 12, release 4 (IBM, Armonk, New York).

Davis RI, Burns A (2011) A survey of hard real-time scheduling fo multiprocessor systems. ACM Comput. Surveys 43(4):1–44.

Dongarra JJ (1993) Performance of various computers using standard linear equations software. Report, Computer Science Depart ment, University of Tennessee, Knoxville.

Dziok T, Figiela K, Malawski M (2016) Adaptive multi-level workflow scheduling with uncertain task estimates. Parallel Processing and Applied Mathematics (Springer, New York), 90–100.

Ekanayake J, Fox G (2009) High performance parallel computing with clouds and cloud technologies. Internat. Conf. Cloud Comput. (Springer, New York), 20–38.

Esseen CG (1942) On the Liapounoff Limit of Error in the Theory of Probability (Almqvist & Wiksell, Stockholm).

Esseen CG (1956) A moment inequality with an application to the central limit theorem. Scandanavian Actuarial J. 1956(2): 160–170.

Gantz JF, Miller P (2016) The Salesforce economy: Enabling 1.9 million new jobs and \$389 billion in new revenue over the next five years. White paper, International Data Corporation, New York

Garey MR, Johnson DS (1979) Computers and Intractability. A Guide to the Theory of NP-Completeness (W. H. Freeman and Company, New York).

Gartner (2017) Gartner says worldwide public cloud services market to grow 18 percent in 2017. Gartner, Inc. (February 22), http:/ www.gartner.com/newsroom/id/3616417.

Gonzalez T, Sahni S (1976) Open shop scheduling to minimize finish time. J. ACM 23(4):665–679.

Graham RL, Lawler EL, Lenstra JK, Kan AR (1979) Optimization and approximation in deterministic sequencing and scheduling: A survey. Ann. Discrete Math. 5:287–326.

Harris D (2015) The economics of cloud computing are, in a word, confusing. Forbes (June 10), http://www.forbes.com/sites/ciocentral/ 2015/06/10/the-economics-of-cloud-computing-are-in-a-word -confusing/#85c8222106ca.

Hogg RV, Tanis EA (2009) Probability and Statistical Inference (Pearson Educational International, London).

Hsieh CC (2003) Optimal task allocation and hardware redundancy policies in distributed computing systems. Eur. J. Oper. Res. 147(2):430–447.

Juve G, Deelman E, Berriman GB, Berman BP, Maechling P (2012) An evaluation of the cost and performance of scientific workflows on Amazon EC2. J. Grid Comput. 10(1):5–21.

Kartik S, Murthy CSR (1995) Improved task-allocation algorithms to maximize reliability of redundant distributed computing systems. IEEE Trans. Reliability 44(4):575–586.

Kokilavani T, Amalarethinam DG (2011) Load balanced min-min algorithm for static meta-task scheduling in grid computing. Internat. J. Comput. Appl. 20(2):43–49.

Kumar K, Feng J, Nimmagadda Y, Lu YH (2011) Resource allocation for real-time tasks using cloud computing. Proc. 20th Internat. Conf. Comput Comm. Networks (ICCCN) (Institute of Electrical and Electronics Engineers, Piscataway, NJ), 1–7.

Kumar S, Dutta K, Mookerjee V (2009) Maximizing business value by optimal assignment of jobs to resources in grid computing. Eur. J. Oper. Res. 194(3):856–872.

Lawler EL, Labetoulle J (1978) On preemptive scheduling of unrelated parallel processors by linear programming. J. ACM 25(4): 612–619.

Lenstra JK, Kan AR, Brucker P (1977) Complexity of machine scheduling problems. Ann. Discrete Math. 1:343–362.

Li X, Wu J, Tang S, Lu S (2014) Let’s stay together: Toward traffic aware virtual machine placement in data centers. Proc. IEEE INFOCOM (Institute of Electrical and Electronics Engineers, Piscataway, NJ), 1842–1850.

Liu D, Sarkar S, Sriskandarajah C (2010) Resource allocation policies for personalization in content delivery sites. Inform. Systems Res. 21(2):227–248.

Liu L, Mei H, Xie B (2016) Toward a multi-QoS human-centric cloud computing load balance resource allocation method. J. Supercomput. 72(7):2488–2501.

Madni SHH, Latiff MSA, Coulibaly Y, Abdulhamid SM (2017) Recent advancements in resource allocation techniques for cloud computing environment: A systematic review. Cluster Comput. 20(3):2489–2533.

Mahmood A (2000) A hybrid genetic algorithm for task scheduling in multiprocessor real-time systems. Stud. Inform. Control 9(3): 207-218.

Mahmood A, Khan SA (2017) Hard real-time task scheduling in cloud computing using an adaptive genetic algorithm. Computers 6(2): 15–36.

Mao M, Humphrey M (2011) Auto-scaling to minimize cost and meet application deadlines in cloud workflows. Proc. Internat. Conf. High Performance Comput. Networking Storage Anal. (Institute of Electrical and Electronics Engineers, Piscataway, NJ), Article 49.

Markets and Markets (2018) Cloud services brokerage market worth 15.03 billion USD by 2023. Markets and Markets (May), https://www.marketsandmarkets.com/PressReleases/cloud -brokerage.asp.

McKendrick J (2016) Cloud computing becomes a home for data analytics. Forbes (February 6), https://www.forbes.com/sites/ joemckendrick/2016/02/06/cloud-computing-becomes-a-home -for-data-analytics/#6bdcd7824eaa.

MSV J (2018) 10 key takeaways from RightScale state of the cloud report. Forbes (February 18), https://www.forbes.com/sites janakirammsv/2018/02/18/10-key-takeaways-from-rightscale -state-of-the-cloud-report/#7d19ce041283

Navimipour NJ, Khanli LM (2008) The LGR method for task scheduling in computational grid. Proc. Internat. Conf. Advanced Comput. Theory Engrg. (ICACTE) (Institute of Electrical and Elec tronics Engineers, Piscataway, NJ), 1062–1066

Ostermann S, Iosup A, Yigitbasi N, Prodan R, Fahringer T, Epema D (2009) A performance analysis of EC2 cloud computing services for scientific computing. Proc. Internat. Conf. Cloud Comput (Springer), 115–131.

Oxford Economics and SAP (2015) The cloud grows up. Oxford Eco nomics (March 2), http://www.oxfordeconomics.com/my-oxford projects/291744.

Panda SK, Gupta I, Jana PK (2015) Allocation-aware task scheduling for heterogeneous multi-cloud systems. Procedia Comput. Sci. 50: 176–184.

Peng Y, Kang DK, Al-Hazemi F, Youn CH (2017) Energy and QoS aware resource allocation for heterogeneous sustainable cloud datacenters. Optical Switching Networking 23:225–240.

Pinedo ML (2016) Scheduling: Theory, Algorithms, and Systems (Springer, New York).

Qamhieh M, Fauberteau F, George L, Midonnet S (2013) Global EDF scheduling of directed acyclic graphs on multiprocessor systems. Proc. 21st Internat. Conf. Real-Time Networks Systems (Association for Computing Machinery, New York), 287–296.

Quora (2016) How can I choose the right EC2 instance type? Accessed March 2, 2020, https://www.quora.com/How-can -I-choose-the-right-EC2-instance-type.

Reddy S, Sarkar A (2015) Amazon EC2 Cookbook (Packt Publishing Ltd, Birmingham, UK).

Sahni S (1975) Approximate algorithms for the 0/1 knapsack prob lem. J. ACM 22(1):115–124.

Sangwan A, Kumar G, Gupta S (2016) To convalesce task scheduling in a decentralized cloud computing environment. Rev. Comput. Engrg. Res. 3(1):25–34.

Sen S, Raghu T, Vinze A (2010) Demand information sharing in heterogeneous IT services environments. J. Management Inform. Systems 26(4):287–316

Shojafar M, Pooranian Z, Abawajy JH, Meybodi MR (2013) An efficient scheduling method for grid systems based on a hierarchical stochastic Petri net. J. Comput. Sci. Engrg. 7(1):44–52.

Stavrinides GL, Karatza HD (2011) Scheduling multiple task graphs in heterogeneous distributed real-time systems by exploiting schedule holes with bin packing techniques. Simulation Model. Practice Theory. 19(1):540–552.

Synergy Research Group (2016) Amazon dominates public IAAS and ahead in PAAS; IBM leads in private cloud. Synergy Re search Group (October 30), https://www.srgresearch.com/articles/ amazon-dominates-public-iaas-paas-ibm-leads-managed-private -cloud.

Tsai CW, Huang WC, Chiang MH, Chiang MC, Yang CS (2014) A hyper-heuristic scheduling algorithm for cloud. IEEE Trans. Cloud Comput. 2(2):236–250.

Tsai WT, Shao Q, Sun X, Elston J (2010) Real-time service-oriented cloud computing. Proc. 6th World Congress Services (Institute of Electrical and Electronics Engineers, Piscataway, NJ), 473–478.

Wang H, Wang F, Liu J, Wang D, Groen J (2015) Enabling customer provided resources for cloud computing: potentials, challenges, and implementation. IEEE Trans. Parallel Distributed System 26(7):1874–1886.

Weins K (2018) Cloud computing trends: 2018 state of the cloud survey. Flexera (blog) (February 13), https://www.rightscale .com/blog/cloud-industry-insights/cloud-computing-trends -2018-state-cloud-survey#significant-wasted-cloud-spend.

Wu D, Ding M, Hitt LM (2012) II implementation contract design: Analytical and experimental investigation of IT value, learning, and contract structure. Inform. Systems Res. 24(3):787–801.

Wu X, Deng M, Zhang R, Zeng B, Zhou S (2013) A task scheduling algorithm based on QoS-driven in cloud computing. Procedia Comput. Sci. 17:1162–1169.

Yi P, Ding H, Ramamurthy B (2013) Budget-minimized resource allocation and task scheduling in distributed grid/clouds. Proc. 22nd Internat. Conf. Comput. Comm. Networks (ICCCN) (Institute of Electrical and Electronics Engineers, Piscataway, NJ), 1–8.

Younge AJ, Von Laszewski G, Wang L, Lopez-Alarcon S, Carithers W (2010) Efficient resource management for cloud computing

environments. Proc. Internat. Green Comput. Conf. (Institute of Electrical and Electronics Engineers, Piscataway, NJ), 357–364.

Yuan S, Das S, Ramesh R, Qiao C (2018) Service agreement trifecta: Backup resources, price and penalty in the availability-aware cloud. Inform. Systems Res. 29(4):779–1068.

Zhang YF, Tian YC, Fidge C, Kelly W (2016) Data-aware task scheduling for all-to-all comparison problems in heterogeneous distributed systems. J. Parallel Distributed Comput. 93–94:87–101.

Zhang Z, Wang H, Xiao L, Ruan L (2011) A statistical based resource allocation scheme in cloud. Proc. Internat. Conf. Cloud Service Comput. (CSC) (Institute of Electrical and Electronics Engineers, Piscataway, NJ), 266–273.
