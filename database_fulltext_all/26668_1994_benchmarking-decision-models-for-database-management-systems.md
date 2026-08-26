---
otero_id: 26668
otero_key: "WEMK76YR"
title: "Benchmarking Decision Models for Database Management Systems"
authors: "Debabrata Dey; Abraham Seidmann"
year: "1994"
journal: "Information Systems Research"
doi: "10.1287/isre.5.3.275"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/WEMK76YR/fulltext/images/64f940fbd2b4e2493ba0aae387a1a4249ff99de82fbc2b6dcd705d1a8d798078.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Benchmarking Decision Models for Database Management Systems

Debabrata Dey, Abraham Seidmann,

To cite this article:

Debabrata Dey, Abraham Seidmann, (1994) Benchmarking Decision Models for Database Management Systems. Information Systems Research 5(3):275-293. http://dx.doi.org/10.1287/isre.5.3.275

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1994 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/WEMK76YR/fulltext/images/174f5a61c166e139f88cefd8c710fdb625a39eff6043f748e0fc9ede5e22f87c.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Benchmarking Decision Models for Database Management Systems

Debabrata Dey

Department of Quantitative Business Analysis

Louisiana State University

Abraham Seidmann

Baton Rouge, Louisiana 70803

William E. Simon Graduate School of Business Administration

University of Rochester

Rochester, New York 14627

Benchmarking is the quantitative method most commonly used when managers contemplate procuring a large business information system. It consists of running a group of representative applications on the systems offered by vendors to validate their claims. The implementation of benchmarking can be very costly, as users need to convert, run, and test applications on several partially compatible computer systems. Benchmarking works well in modern database management systems (DBMS)-oriented applications because the system performance is more a function of the database structure and activities than of the complexity of the application code. Earlier research focused primarily on designing various benchmarks for database systems; the decision problem associated with finding an optimal mix of benchmarks has largely been overlooked. In this paper, we examine the problem of defining the most economical process for generating and evaluating the appropriate mix of benchmarks to be used across the contending information systems. Our analytical approach considers information-gathering priorities, acquisition and execution costs, resource consumption, and overall time requirements. We present a multiobjective decision-making approach for deriving the optimal mix of benchmarks; this approach reflects the major organizational objectives in more than simple one-dimensional numerical terms. A practical example illustrates the utility of this approach for evaluating a client-server relational database system.

Multicriteria decision making (MCDM)—Goal programming—Database benchmarking

## 1. Introduction

valuating the performance of computer hardware and software systems is one of the most important practices in today's information industry. It is propelled by rapid technological developments, the proliferation of competing standards, and the increased complexity of modern applications. Managers commonly employ either benchmarking or mathematical modeling and analysis to evaluate performance. A typical benchmark generates an artificial workload by using a set of programs or interactive scripts representing the anticipated operations of a system.

Mathematical performance models (similar to the BGS or the RESQ commercial products) are excellent tools for long-run capacity planning (Jain 1991). Benchmarking requires more time and money than mathematical analyses, but it has some relative advantages critical to the success of modern business systems. First, mathematical tools make some restrictive assumptions (to keep the problem mathematically tractable) in order to model a system for performance evaluation; these analyses are thus only approximate. Second, it is very difficult to model subjective performance concerns about security, integration, control, reliability, and user-friendliness using mathematical tools. Distributed and partitioned systems are also prohibitively difficult to model using mathematical tools. Technical system issues such as recovery and concurrency control can hardly be mathematically analyzed. Finally, mathematical tools for performance analysis may not be sophisticated enough to evaluate domain-specific performance, e.g., the performance of a relational database management system or the interaction effects of several software products on a client-server network.

This paper explores the benchmarking of database systems, which are widely used in current computerized systems. Many business systems handle large volumes of data, and a database system is a popular and natural choice for supporting these data. One must evaluate and monitor such database systems to ensure their smooth operation: database benchmarking provides a tool for this. In addition, benchmarking also provides a tool when selecting among competing vendors and deciding on the architecture of systems (Sheppard and Weston 1993). Although vendors regularly publish their performance data, and certain journals present comparative studies (Robinson 1993), these results cannot address the specific performance of certain individual applications.

Implementation of benchmarking requires careful planning and significant investments in the planning, development (or requisition), and execution of the benchmarks and in the analysis of the results (Perry 1985). In the course of a typical benchmarking, the users must convert, run, and test several sample applications on a few partially compatible computer systems. As a result, the cost and time associated with benchmarking are significant. Users planning benchmarking must deal with multiple goals such as timeliness, data validity, cost, and ease of use. We focus on the development of an integrated decision-theoretic methodology for planning a benchmarking effort. We consider information-gathering priorities, acquisition and execution costs, resource consumption, and overall time requirements. More specifically, we focus on performance concerns for database systems and propose a multicriteria decision framework that offers the most economical set of benchmarks to meet the needs of a particular case. This methodology specifies the optimal mix of benchmarks to be used under different combinations of time and budget constraints. It also reveals when it is better for the users to develop a particular benchmark in-house, and when it is better to use a commercially available one.

Section 2 of this paper presents a brief historical sketch of database benchmarking and discusses performance concerns for databases. Section 3 outlines our proposed goal-programming methodology for benchmarking decisions. In §4, an application of this model is illustrated with an example. Section 5 presents some concluding remarks and offers future research directions.

## 2. Performance of Database Systems

Many current information systems are centered on a database that integrates the data relevant to multiple applications. The system's capabilities determine the effectiveness of the business process it supports. Unfortunately, no single performance metric can measure the performance of database systems in all applications. Although MIPS (million instructions per second) or MFLOPS (million floating point operations per second) may indicate the raw horsepower of a CPU, they do not provide much information on the response time for update and retrieval queries from a database. As applications become increasingly complex, the time and effort required for database testing also increases. What needs to be measured depends on what is important, which in turn depends on the purpose a particular system serves. Domain-specific benchmarks are the answer to the diversity of computer applications.

## 2.1. Performance of On-line Transaction Processing

The early 1980s saw an increased interest in characterizing the performance of on-line transaction processing (OLTP) systems (Serlin 1991). Many vendors started using ad hoc tests to claim superiority for their products. The first attempt to organize and standardize such testing process was the celebrated paper by “Anon et al. (1985)." The paper recommended the adoption of three standard performance tests for OLTP systems: one on-line transaction processing test, called DebitCredit, and two batch tests, a sort and a scan. The two batch tests proposed in this paper were largely ignored by the industry, but the proposed on-line test gained popularity, and a variation called TP1 was developed around 1987. TP1 used a major simplification by ignoring the user terminals and the X.25 connecting network in its entirety, and it exhibited abnormally high performance ratings (Serlin 1991). Although this simplification made some sense from the viewpoint of database vendors, it introduced a significant new uncertainty regarding the comparability of results from these tests. Around this time, the industry formed the Transaction Processing Performance Council (TPC) to create and enforce OLTP performance measurement standards. So far TPC has defined two benchmarks: TPC BM™MA is the council's version of the DebitCredit test and TPC BM™B is the council's version of the TP1 test.

## 2.2. Performance of Relational Queries

While the above benchmarks measure system throughput in transactions per second (tps) and \$/tps, there have been other benchmarks that measure database system performance with respect to relational queries. The first such query benchmark, the Wisconsin benchmark (Bitton et al. 1983, Bitton and Turbyfill 1988), was widely used, but it was originally developed as a single-user benchmark and failed to test critical features required for real-world applications. Two competing multi-user benchmarks were developed (Bitton et al. 1983, Boral and Dewitt 1984) from this benchmark, but neither has attracted wide-spread interest or use.

The traditional Wisconsin benchmark suffered a number of limitations—it did not test utility functions, did not mix batch and interactive queries, and did not emphasize multi-user tests. Subsequently, Turbyfill et al. (1989) provided a more complete metric by including such features in a benchmark called ANSI SQL Standard Scaleable and Portable (or AS³AP, in short). AS³AP also allows one to set a time limit on the benchmark and then measure the largest database that the system can process within the time limit. This gives each database system an equivalent database size rating. AS³AP gives a more balanced and realistic evaluation of the overall performance of a relational system used for database queries (Gray 1991).

Several other benchmarks are available today. The most prominent ones are: the Set Ouery benchmark by Pat O'Neil (O'Neil 1991), which evaluates the ability of a system to process complex queries typically found in decision-support applications; an Engineering Database benchmark by Rick Cattell (Cattell 1991) for evaluating database systems to store engineering or object-oriented databases; and commercial benchmarks sold for profit, such as benchmarks by Neal Nelson Associates and AIM Technology (Nelson 1991), or the Rhobot testing tools sold by the Promark Corporation. All these benchmarks vary widely in terms of their capabilities, operating systems support, price, and resource requirements. The methodology presented in §3 will enable a user to select the best set of these benchmarks.

## 2.3. Performance Metrics for Database Systems

A database system integrates four major components: the hardware, the operating system, the database management system (DBMS), and the data files. As a result, the performance of the system depends upon all four of these components. Separate metrics for separate components make comparison of different systems very difficult. On the other hand, deriving a composite metric from the various components is always difficult and may not provide correct criteria for judging system performance. Establishing meaningful metrics can thus be as difficult as designing the actual benchmarks to evaluate the performance of database systems.

Earlier research has attempted to derive one or two composite metrics,' magic numbers that can serve as the criteria for comparing different database systems. We wish to differ from this approach, since different applications have different priorities and performance requirements. In certain business environments, a database is used only to retrieve information and updates are few, but in others frequent updates are made in the database. A system that shows good performance characteristics in the first case may do badly in the second, and vice versa. A benchmark should provide the user with different performance metrics for different components of the user's application workload.

Performance evaluation of a database system involves evaluation of many operational parameters or metrics (Bitton et al. 1983, Rubenstein et al. 1987, Shaw 1991, Turbyfill et al. 1989). Since the definition of each of these parameters is relative to a given transaction or activity, one thus needs to know the types of transactions or the dynamic workload of a database system before the performance criteria can be established. There are three basic transactions in a database system: (i) inquiring transactions, where information is retrieved from the database; (ii) insertion transactions, where new tuples are added to the database; and (iii) updating transactions, where existing tuples are changed. Either a representative or an average transaction (statistically) can be defined from the relative frequency and arrival rate of these transactions, or each transaction can be treated separately for any given performance index.

In either case, the result will be a set of parameters or indices of interest on which the benchmarks should provide the user with useful information.

## 2.4. Benchmarking Decision Models and Related Studies

Database benchmarking has not been modeled from a decision-theoretic perspective, though several studies exist that model the performance evaluation of computerized systems. Ahituv et al. (1978) modeled a generic selection process of a job mix for running benchmarks using an integer programming model. Their model maximizes the number of runs of each benchmark within given resource constraints, but they fail to account for the fact that a particular benchmark may be useful in testing more than one system parameter. Their model is useful in developing benchmarks, but not in selecting the desired subset of benchmarks to be used.

In a related work, Ahituv and Igbaria (1988) proposed a model based on a statistical method for predicting and evaluating the consumption of computer resources. They have used this model for evaluating alternative hardware configurations. Subsequently, Ahituv et al. (1988) have proposed a compumetrical approach for analysis and clustering of computer system performance variables. These works provide useful methods for deciding on system configuration, but they are not directly useful for deciding the optimal mix of benchmarks. Capacity planning, benchmarking, and evaluation of small computer systems have also been studied by Arbel and Seidmann (1985). Their hierarchical framework integrates relevant decision elements for systematic analysis. While their model has been successfully used in real-world acquisition cases, it is not directly applicable to database benchmarking decisions.

## 3. The Decision Framework for Database Benchmarking

Running benchmarks on a database system provides information on the system, but this information comes at the expense of time, money, and system resources. We seek to maximize the information derivable from a mix of benchmarks and minimize the cost and time spent to obtain that information. The methodology developed here parameterizes the cost, time, and resource consumption of each benchmark, the relative weights of the decision criteria, and the reliability of the benchmarks.

Benchmarking evaluates the performance of a system (or several systems) with respect to a well-defined set of parameters or metrics (e.g., mean response time for different types of queries, mean time before failure, paging rate, disk utilization). We classify these parameters into two categories: (i) mandatory and (ii) optional. Mandatory parameters are those which are of extreme importance to the decision maker with respect to the performance of the system; they must be tested at any cost. On the other hand, optional parameters are not critical for the decision at hand, but many benchmarks provide these results at little added cost. Once a set of parameters has been identified, its division into mandatory and optional parameters depends largely on the system's functions and the evaluator's preferences.

Our approach also considers the relative reliability of benchmarks. There are several reasons why a benchmark might not be perfectly reliable. First, most of them are designed for a qualitative representation of certain technologies for the user, such as hardware, software, or system architecture, but they may be applied elsewhere. As an example, suppose that a benchmark was designed to evaluate performance of a distributed system with a maximum of six remote sites. If it is used when there are more than six remote sites, the accuracy of the results can be questioned. Second, if the benchmark is not developed in-house, the user's inexperience with it can reduce its reliability.²

The optimal benchmarking decision problem contains multiple goals or objectives such as parameter coverage, cost, and overall testing times. Because these goals frequently conflict with each other, our decision model is formulated as a linear goal program with preemptive priority (Bitran 1979, Ignizio 1976). In goal programming, the users need to set some estimated targets for each of their major goals and rank them in order of importance; the advantage of goal programming is that users only have to state which goals they consider more important, and they need not state how much more important they consider them. This approach has a sound theoretical basis and is widely used. Linear goal programs are easily solved iteratively using any software that can handle a linear programming model. They provide considerable ease of computation, and can handle fairly large problems. Finally, a goal programming formulation provides flexibility in performing post-optimality analysis. Goal programming has also been used by Jain et al. (1991) for generating and evaluating alternatives in requirement analysis. Their model is very useful in the early stages of system development. It does not help in the system acquisition decisions typically made at the later stages, which are the focus of this paper.

Our overall optimization model was formulated following three decision steps: (i) identification of parameters and decision variables, (ii) formulation of the objectives, and (iii) specification of the constraints.

## 3.1. Parameters and Decision Variables

Let $\pmb { \mathcal { I } } = \{ 1 , 2 , \dots , I \}$ denote the set of systems to be evaluated. $\mathcal { J } = \{ 1 , 2 , \ldots , J \}$ denotes the set of all parameters that one is interested in measuring. In other words, one will choose a system based on performance of the system with respect to the parameters in . We assume that the decision maker can specify the relative weight of $\pmb { \mathcal { S } } .$ parameter $j ,$ denoted by $w _ { i } , \forall j \in \mathcal { J } ,$ , and (without loss of generality) that $\begin{array} { r } { \sum _ { i \in \pmb { \mathscr { s } } } \pmb { w } _ { j } = 1 } \end{array}$ (Canada and Sullivan 1989). The set ∂ is partitioned into subsets ∂1 and ∂2. The $\pmb { \mathcal { J } }$ $\pmb { \mathcal { J } _ { 1 } }$ $\pmb { \mathcal { J } } _ { 2 } .$ parameters in the set ♂, are the mandatory parameters, and they must be tested; the $\pmb { \mathcal { J } } _ { 1 }$ testing of the parameters in $\pmb { \mathcal { J } } _ { 2 }$ (optional parameters) is not mandatory.

Let $\mathcal { H } = \{ 1 , 2 , \dots , K \}$ be a set of different available benchmarks, and let each benchmark $k \in \mathcal { H }$ evaluate a set of parameters $\mathcal { L } _ { k }$ where $\mathcal { L } _ { k } \subseteq \mathcal { S }$ . We will assume that benchmark $k \in \mathcal { K }$ has an ordinal reliability (or fidelity) index $v _ { k } , 0 \leq v _ { k } \leq 1 .$ A reliability index of 1 implies that it is perfectly reliable; in that case, the benchmark results very closely resemble how the system is expected to perform. The reliability index of a benchmark is assumed to be uniform over all the parameters that it can measure, since the reliability index is a measure of how closely the benchmark emulates the real-world application, and it is thus a macroscopic index.

The cost and time needed for running a database benchmark must be considered separately; one cannot be expressed in terms of the other, since, in most cases, benchmarking is undertaken with specific incommensurable cost and time constraints. Let $\pmb { c _ { k } }$ be the cost of buying or developing benchmark $k \in \mathcal { R } ,$ and let $d _ { k }$ be its development or acquisition time. If a particular benchmark k is developed, then estimation of ck must take into account the fact that it may be possible to reuse or sell it at a $\pmb { c _ { k } }$ later date.

Let $\pmb { q } _ { i k }$ and $\pmb { S } _ { i k }$ be the cost and time needed to run benchmark $k \in \mathcal { K }$ on system $i \in { \mathcal { I } }$ . Typically a benchmark provides information on a number of parameters during a single run; $\pmb { q } _ { i k }$ and $\pmb { S } _ { i k }$ parameterize the cost and time (common to all parameters) needed to run benchmark $k \in \mathcal { K }$ on system $i \in \mathcal I$ . These also include the cost and time required for any conversion of the program or data necessary to address system-specific characteristics. Also let $r _ { i j k }$ and $t _ { i j k }$ be the cost and time needed to run benchmark $k \in \mathcal { K }$ on system $i \in \mathcal { I }$ for parameter $j \in \mathcal { L } _ { k } ;$ they include the additional cost and time needed to take care of parameter-specific details. As an example, assume that running the kth benchmark on the ith system takes 60 hours, and two parameters can be measured during this run. However, it is necessary to spend 10 additional hours in post-processing some data to estimate the first parameter, and 5 extra hours to install the software monitor collecting data for the second parameter. In that case, $s _ { i k } = 6 0$ hours, whereas $t _ { i 1 k } = 1 0$ hours and $t _ { i 2 k } = 5$ hours. If some benchmark $k \in \mathcal { K }$ cannot be run on some system $i \in \mathcal { I }$ for some parameter $j \in \mathcal { L } _ { k }$ that particular case can be accommodated by setting $r _ { i j k } = t _ { i j k } = + \infty$

Let us also assume that $\mathcal { N } = \{ 1 , 2 , \dots , N \}$ denotes the set of required computer resources, and $\pmb { b _ { n } }$ is the available amount of resource $\pmb { n } \in \mathcal { N }$ (Ahituv et al. 1978). Let $b _ { i j k n }$ be the consumption of resource $\pmb { n } \in \mathcal N$ if benchmark $k \in \mathcal { K }$ is run for parameter j $\in \mathcal { L } _ { k }$ of system $i \in \mathcal { I }$

The decision variables $X _ { i j k } { ' s } , i \in \mathcal { I } , j \in \mathcal { L } _ { k } , k \in \mathcal { R } _ { i }$ , are defined as:

$X _ { i j k } = \left\{ { 1 , } \atop { 0 , } \right.$ if benchmark $k \in \mathcal { K }$ is run on system $i \in \mathcal { I }$ for parameter $j \in \mathcal { L } _ { k }$ otherwise.

We will set $X _ { i j k } = 0 \ i f j \notin \mathcal { L } _ { k } .$ . We also make use of the following two auxiliary variables in our formulation;

$$
Y _ {i k} = \left\{ \begin{array}{l l} 1, & \text { if   benchmark } k \in \mathcal {H} \text { is   run   on   system } i \in \mathcal {I}, \\ 0, & \text { otherwise }, \end{array} \right.
$$

and

$$
Z _ {k} = \left\{ \begin{array}{l l} 1, & \text { if   benchmark } k \in \mathcal {R} \text { is   bought   or   developed }, \\ 0, & \text { otherwise }. \end{array} \right.
$$

## 3.2. Objective Function

The decision model we present here is multiobjective. More specifically, we attempt to maximize the information derivable from the benchmarking and to minimize, at the same time, the cost and time needed for the benchmarking effort. These three components of the objective function are combined in a linear goal programming formulation (Bitran 1979, Ignizio 1976). The optimization scheme tries to minimize the deviations from the targets set for each goal. It begins with the most important one and continues until achieving a less important goal causes failure to achieve a more important one

3.2.1. Parameter Coverage Objective. One of the objectives of a system evaluation using benchmarks is to gather as much information about each parameter as possible, assuming that more information will improve the decision based on this information. It is further assumed that the information available from running a benchmark for a particular parameter is proportional to the reliability of the benchmark and the relative weight of the parameter. The total information available from benchmarking can be expressed as the fractional parameter coverage of all the benchmarks:

$$
f _ {1} (X) = \frac {1}{I} \sum_ {i \in \mathcal {I}} \sum_ {k \in \mathcal {H}} \sum_ {j \in \mathcal {L} _ {k}} w _ {j} v _ {k} X _ {i j k}.\tag{1}
$$

If all parameters are tested using perfectly reliable tests, then a value of 1.0 of this obiective will be attained. A value of less than 1.0 indicates that either some optional parameters were not tested or some tests were not perfectly reliable. It is possible to achieve a value that is greater than unity by testing some parameters more than once.

3.2.2. Cost Objective. Another important objective in an evaluation study is to minimize the cost to perform such a study. The cost of benchmarking considers either buving or developing the benchmarks and the costs for running them on different systems. The relevant parameters to determine these costs are $c _ { k } , q _ { i k }$ and $r _ { i j k }$ and haye been described above. The overall cost of benchmarking can be written as:

$$
f _ {2} (X, Y, Z) = \sum_ {k \in \mathcal {H}} c _ {k} Z _ {k} + \sum_ {i \in \mathcal {I}} \sum_ {k \in \mathcal {H}} q _ {i k} Y _ {i k} + \sum_ {i \in \mathcal {I}} \sum_ {k \in \mathcal {H}} \sum_ {j \in \mathcal {L} _ {k}} r _ {i j k} X _ {i j k}.\tag{2}
$$

3.2.3. Time Objective. Time is also an important concern in an evaluation study, since most evaluation projects are undertaken under time constraints with limited time available. The time required for benchmarking should thus be minimized. The total time required for a study consists of the time required to develop (acquire) the benchmarks and the time required to run them on different systems. Since the development (acquisition) of benchmarks can be done in parallel, we must include only the maximum development (acquisition) time in the objective function. The relevant parameters to determine the time requirement are $d _ { k } , s _ { i k } ,$ and $t _ { i j k } ,$ as described above. The total time required for benchmarking can be written as:

$$
f _ {3} (X, Y, Z) = \max _ {k \in \mathcal {K}} \left(d _ {k} Z _ {k}\right) + \sum_ {i \in \mathcal {I}} \sum_ {k \in \mathcal {K}} s _ {i k} Y _ {i k} + \sum_ {i \in \mathcal {I}} \sum_ {k \in \mathcal {K}} \sum_ {j \in L _ {k}} t _ {i j k} X _ {i j k}.\tag{3}
$$

Since the maximum is not a linear function, we linearize it, using another auxiliary variable W and a set of constraints, as follows:

$$
f _ {3} (X, Y, Z) = W + \sum_ {i \in \mathcal {I}} \sum_ {k \in \mathcal {H}} s _ {i k} Y _ {i k} + \sum_ {i \in \mathcal {I}} \sum_ {k \in \mathcal {H}} \sum_ {j \in \mathcal {L} _ {k}} t _ {i j k} X _ {i j k}, \quad \text { where }\tag{4}
$$

$$
W \geq d _ {k} Z _ {k}, \quad \forall k \in \mathcal {K}.\tag{5}
$$

These objectives can be written in terms of the decision-maker's goals as:

$$
G _ {m} = f _ {m} + n _ {m} - p _ {m}, \quad \forall m = 1, 2, 3,\tag{6}
$$

where Gm is the mth goal, and n and pm are the negative and positive deviations from $G _ { m }$ $n _ { m }$ $p _ { m }$ that goal. We also set the fractional parameter coverage goal $G _ { 1 } = 1$

## 3.3. Specification of Constraints

The constraints in the model include constraints on available system resources, as well as a set of constraints that ensures certain simple requirements for the solution. The following constraints were identified in this optimization model:

1. The total consumption of every system resource (such as CPU time, printing volume, storage requirement) must be within the available limit (Ahituv et al. 1978), i.e.,

$$
\sum_ {i \in \mathcal {I}} \sum_ {k \in \mathcal {K}} \sum_ {j \in \mathcal {L} _ {k}} b _ {i j k n} X _ {i j k} \leq b _ {n}, \quad \forall n \in \mathcal {N}.\tag{7}
$$

2. If a benchmark is not run on a system, it must not be run on any parameter of that system, i.e.,

$$
X _ {i j k} \leq Y _ {i k}, \quad \forall i \in \mathcal {I}, \forall j \in \mathcal {L} _ {k}, \forall k \in \mathcal {K}.\tag{8}
$$

3. If a benchmark is run on a system, then it must be run on at least one parameter for that system, i.e.,

$$
\sum_ {j \in \mathcal {A}} X _ {i j k} \geq Y _ {i k}, \quad \forall i \in \mathcal {I}, \forall k \in \mathcal {K}.\tag{9}
$$

4. A benchmark must be purchased or developed if it is to be used, i.e,

$$
Y _ {i k} \leq Z _ {k}, \quad \forall i \in \mathcal {I}, \forall k \in \mathcal {K}.\tag{10}
$$

5. If a benchmark is not used, it is not purchased, i.e.,

$$
\sum_ {i \in \mathcal {I}} Y _ {i k} \geq Z _ {k}, \quad \forall k \in \mathcal {K}.\tag{11}
$$

6. At least one benchmark must be performed for each parameter in the set of mandatory parameters () for every alternative system under consideration, i.e., $( \pmb { \mathcal { F } } _ { 1 } )$

$$
\sum_ {k \in \mathcal {H}} X _ {i j k} \geq 1, \quad \forall i \in \mathcal {I}, \forall j \in \mathcal {J} _ {1}.\tag{12}
$$

## 3.4. Goal Programming Formulation

Having described the parameters, decision variables, objectives, and constraints. we set the integrated decision model as a generalized goal program:

$$
\min _ {X, Y, Z} \quad \bar {a} = \left\{g _ {1} (\bar {n}, \bar {p}), g _ {2} (\bar {n}, \bar {p}), \dots , g _ {L} (\bar {n}, \bar {p}) \right\}\tag{13}
$$

$$
\text { s.t. } \quad f _ {m} + n _ {m} - p _ {m} = G _ {m}, \quad \forall m = 1, 2, 3,\tag{14}
$$

$$
W \geq d _ {k} Z _ {k}, \quad \forall k \in \mathcal {K},
$$

$$
\sum_ {i \in \mathcal {I}} \sum_ {k \in \mathcal {K}} \sum_ {j \in \mathcal {L} _ {k}} b _ {i j k n} X _ {i j k} \leq b _ {n}, \quad \forall n \in \mathcal {N},\tag{15}
$$

$$
X _ {i j k} \leq Y _ {i k}, \quad \forall i \in \mathcal {I}, \forall j \in \mathcal {L} _ {k}, \forall k \in \mathcal {K},\tag{16}
$$

$$
\sum_ {j \in \mathcal {S}} X _ {i j k} \geq Y _ {i k}, \quad \forall i \in \mathcal {I}, \forall k \in \mathcal {K},\tag{17}
$$

$$
Y _ {i k} \leq Z _ {k}, \quad \forall i \in \mathcal {I}, \forall k \in \mathcal {K},\tag{19}
$$

$$
\sum_ {i \in \mathcal {I}} Y _ {i k} \geq Z _ {k}, \quad \forall k \in \mathcal {K},\tag{20}
$$

$$
\sum_ {k \in \mathcal {H}} X _ {i j k} \geq 1, \quad \forall i \in \mathcal {I}, \forall j \in \mathcal {J} _ {1},\tag{21}
$$

$$
X _ {i j k}, Y _ {i k}, Z _ {k} \in \{0, 1 \}, \quad \forall i \in \mathcal {I}, \forall j \in \mathcal {J}, \forall k \in \mathcal {K}.\tag{22}
$$

In this formulation, ā denotes the generalized achievement function and is an ordered vector. The order of the goals denotes the descending preemptive priority ranks associated with the functions $g _ { i } ( \bar { n } , \bar { p } ) , l = 1 , 2 , . . . , L ,$ , the first component having the highest priority level. The form of the functions and the priority levels associated with them will, of course, depend on the decision maker. A more detailed discussion is found in Ignizio (1976) and Lee (1972).

Our formulation (13)–(22) is very general and can be used for benchmarking any system. It assumes, however, that the benchmarks are applicable to all platforms; that is, if we are benchmarking the CPU, then the rest of the hardware and software do not change. Different components of a system interact nonlinearly, and thus the performance of one component is highly dependent on the rest of the components. In order to make a reasonable choice from the benchmark results, it is, then, imperative that the alternatives be compared on similar, if not the same, platforms. We therefore suggest that this model is particularly suited for database benchmarking. First, when benchmarking a database system, other system components (such as hardware and operating system) are likely to remain the same. Second, the performance of a database system is more a function of the database structure and activities than of the complexity of the application code. Finally, if benchmarking is used to evaluate relational databases, which are currently gaining rapid popularity, then alternative physical level implementations (for a given logical structure) can be evaluated to arrive at an optimal storage strategy. In such cases, every system component except the physical file structure remains the same during benchmarking.

## 3.5. Data Collection

In this section. we briefly discuss how the different parameter values of our decision framework can be determined. Consider the relative weight w, assigned to a parameter $j \in \mathcal { J } ;$ it denotes the decision maker's subjective judgment of the relative importance assigned to parameter j in the overall evaluation process. Many realworld problems associated with the management of information systems involve the assignment of priorities to a set of objectives, projects, or response measures. Users' preferences are often expressed in the form of pairwise comparisons, rather than in weights directly. In many environments, this is the most convenient format for extracting such preference data. Specifically, if J parameters are being compared, the users' preferences are supplied by means of a J × J matrix $\underline { { \underline { { P } } } } = \left( p _ { i k } \right)$ —whose elements are the degree to which parameter i is preferred to parameter k. Arbel and Seidmann (1985), Canada and Sullivan (1989), Charnes and Cooper (1961), and Gass (1985) present several such methods for determining the relative weights $w _ { j } , j \in \mathcal { I }$ These methods are typically based on pairwise comparison of parameters and on testing the transitivity of the relative values assigned to each pair of parameters. Shin and Ravindran (1991) discuss other methods involving vector comparisons, aspiration level trade-offs, and comparative ratios.

The reliability index ${ \boldsymbol { v } } _ { k } \ { \boldsymbol { k } } \in { \mathcal { K } } ,$ of each benchmark measures how closely it matches the operational characteristics of the application. In most cases, the benchmark is designed independently of the application on which it would be run; the reliability index parameterizes the resemblance of the benchmark to the application. Using the design characteristics of the available benchmarks, it is possible to obtain some kind of ranking based on a weighted deviation from the operational characteristics of the application, which can be used, after normalization, as the reliability index. In absence of such an estimate, it is, of course, possible to start with an assumption that all the benchmarks are equally reliable and set $v _ { k } = 1$ for all $k \in \mathcal { K }$

The cost and basic resource consumption figures, such as memory requirements, hard disk space, etc. are readily available for standardized off-the-shelf benchmarks. This information is also available when testing existing programs on another platform. It is admittedly more difficult to generate these estimates when developing a new benchmark from scratch, but several methods of estimating such parameters for software projects have been proposed in the literature (Boehm 1981, Kemerer 1993).

The proposed model aims at estimating and minimizing the total administrative time (not CPU time) spent during the study. CPU time, if important in this context, is treated as a resource constraint. As an example, if benchmark k is developed in-house then $\pmb { d } _ { \pmb { k } }$ is the development time (in days) as estimated prior to the development effort. On the other hand, if benchmark k is purchased then $d _ { k }$ is the time that must be spent in its acquisition. Other time parameters may be estimated in a similar fashion at an early stage.

The achievement function used in the model, with its component functions and their priorities, is specified by the user. Korhonen et al. (1992) present several methods for eliciting user preferences and Ignizio (1976) discusses several ways of translating user's preferences into the achievement function. Similarly, the specific goals associated with the time and money spent are specified by the user. The computational efficiency of (13)–(22) facilitates rapid sensitivity analyses and helps the user in assessing the robustness of the optimal benchmark. In some cases, the user may specify a goal and an upper limit for each of these objectives; two additional constraints with the upper bounds could easily be added to our formulation in those cases.

## 4. A Case Study

Our multiple criteria approach was applied to a simulated benchmarking decision for determining the capacity of a client-server relational database supporting the main office of a large corporation. The actual objective was to select an optimal mix of benchmarks to evaluate whether or not the existing system could meet future demands. The example is motivated by a real-world application; details were somewhat modified at the request of the company involved.

## 4.1. Data

Three types of average transactions were defined for this application, based on the anticipated dynamic workload of the application to be served by the existing database system. The transaction types were: (i) simple retrievals (single relation), (ii) complex retrievals (multiple relations with subselection and remote procedural calls), and (ii updates. Concurrency control, segment locking and other features primarily designed to support high volume on-line transaction processing capabilities were not critical in this context. Benchmarking was used to evaluate the performance of the existing system in place, and to decide whether or not extra capacity will be needed within the near future to accommodate new users' needs. Six parameters relevant to the decision were identified: (i) mean time before failure (MTBF), (ii) mean response time for simple retrieval (MRTSR) (ii mean response time for complex retrieval (MRTCR), (iv) mean response time for update (MRTU), (v) paging rate, and (vi) disk utilization. The first four were identified as mandatory parameters and tested for each system. In other words, we have:

Dey • Seidmann

<table><tr><td colspan="7">TABLE 1The Four Available Benchmarks</td></tr><tr><td>k</td><td> $\mathcal{L}_{k}$ </td><td> $c_{k}$ ($)</td><td> $d_{k}$ (days)</td><td> $v_{k}$ </td><td> $q_{1k}$ ($)</td><td> $s_{1k}$ (days)</td></tr><tr><td>1</td><td> $\{1,3,5\}$ </td><td>60,000</td><td>4</td><td>1.0</td><td>3400</td><td>20</td></tr><tr><td>2</td><td> $\{2,3,4,5\}$ </td><td>56,000</td><td>7</td><td>0.8</td><td>2600</td><td>30</td></tr><tr><td>3</td><td> $\{1,2,4,6\}$ </td><td>42,000</td><td>12</td><td>0.7</td><td>3600</td><td>20</td></tr><tr><td>4</td><td> $\{1,2,3,4,5,6\}$ </td><td>38,000</td><td>80</td><td>1.0</td><td>0</td><td>35</td></tr></table>

$$
\mathcal {I} = \{1 \}, \quad \mathcal {I} = \{1, 2, 3, 4, 5, 6 \}, \quad \mathcal {I} _ {1} = \{1, 2, 3, 4 \}, \quad \mathcal {I} _ {2} = \{5, 6 \}.
$$

The following relative weights were specified by guiding the evaluators through the steps of the interactive pairwise comparison process as discussed above:

$$
\begin{array}{l l l} w _ {1} = 0. 2 4, & w _ {2} = 0. 1 6, & w _ {3} = 0. 2 6, \\ w _ {4} = 0. 2 4, & w _ {5} = 0. 0 5, & w _ {6} = 0. 0 5. \end{array}
$$

We found that three benchmarks (denoted by $k = 1 , 2 , 3 )$ were commercially available for evaluating the performance of the existing database system. It was also possible to develop a benchmark internally to measure the performance of all six parameters. Details of these benchmarks, such as the estimated cost and time needed for their acquisition and execution and the parameters they can test, are presented in Tables 1 and 2. The resource consumption constraints (7) were excluded from this example because the availability of all relevant resources (such as printer, disk storage, etc.) in the example case was very high, and thus the evaluators felt that they did not form binding constraints. The reliability index of each benchmark was based on the evaluators' subjective evaluation of its affinity with the operational characteristics of the application under investigation.

These data were analyzed for the four different priority structures shown in Table 3. Under structure I, the time objective was given the maximum priority, and under structure II the maximum priority was attached to the cost objective.³ Under structures III and $\mathbf { I V } ,$ both cost and time were given the same priority, though their weights were different. The weights given to ${ \pmb p } _ { 3 }$ were based on the usual opportunity cost argument, i.e., they may represent the opportunity cost of delaying the system installation by one day. The last goal in all priority structures attempts to maximize the parameter coverage objective within the limits of the other goals.

TABLE 2  
The Additional Cost and Time Required for Testing Specific Parameters Using the Four Benchmarks

<table><tr><td rowspan="2">Cost/Time</td><td rowspan="2">Benchmark k</td><td colspan="6">Parameters (j)</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Cost</td><td>1</td><td>1000</td><td>—</td><td>2000</td><td>—</td><td>1200</td><td>—</td></tr><tr><td rowspan="3"> $r_{1jk}$ ($)</td><td>2</td><td>—</td><td>400</td><td>2200</td><td>1000</td><td>0</td><td>—</td></tr><tr><td>3</td><td>800</td><td>200</td><td>—</td><td>400</td><td>—</td><td>400</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Time</td><td>1</td><td>2</td><td>—</td><td>1</td><td>—</td><td>1</td><td>—</td></tr><tr><td rowspan="3"> $t_{1jk}$ (days)</td><td>2</td><td>—</td><td>1</td><td>1</td><td>1</td><td>2</td><td>—</td></tr><tr><td>3</td><td>2</td><td>3</td><td>—</td><td>2</td><td>—</td><td>1</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Benchmarking Decision Models for Database Management Systems

<table><tr><td colspan="4">TABLE 3Four Different Priority Structures</td></tr><tr><td>Priority I</td><td>Priority II</td><td>Priority III</td><td>Priority IV</td></tr><tr><td> $g_1 = p_3$ </td><td> $g_1 = p_2$ </td><td> $g_1 = p_2 + 10000p_3$ </td><td> $g_1 = p_2 + 200p_3$ </td></tr><tr><td> $g_2 = p_2$ </td><td> $g_2 = p_3$ </td><td> $g_2 = n_1 - p_1$ </td><td> $g_2 = n_1 - p_1$ </td></tr><tr><td> $g_3 = n_1 - p_1$ </td><td> $g_3 = n_1 - p_1$ </td><td></td><td></td></tr></table>

## 4.2. Results and Discussion

For each priority structure, the decision model was solved 25 times (with $\mathbf { \hat { f } } \mathbf { v } \mathbf { e } ^ { 4 }$ different goals for budget and time); the decision space was discretized to a set of 25 points to allow for detailed trade-off analysis. The results are summarized in Figure 1, and the decision associated with each region is outlined in Table 4. In Figure 1, the horizontal and vertical axes of each of the graphs represent the goals for the cost and time objectives respectively. Each graph represents one of the four priority structures.

Given specific values of budget and time goals, the optimal decision pertaining to a specific priority structure can be read directly from Figure 1. For example, if the budget and time goals are \$80,000 and 80 days respectively, then, under priority structure I, the optimal decision is read from Figure 1(a) as region B; this implies that the evaluators should buy benchmark 2 for parameters 3 and 5, and benchmark 3 for ${ \mathfrak { s } } ,$ parameters 1, 2 and 4 (from Table 4). Similarly, under priority structure II, the above set of goals would yield a different optimal decision (region C) which suggests inhouse development of benchmark 4 for all the parameters (from Figure 1(b) and Table 4).

An overall examination reveals that the cost and time goals were not satisfied whenever the goals were too ambitious. For example, in Figures 1(a) and 1(c), a significant portion of region B did not meet the cost goal, since the minimum requirement was \$107,800. Similarly, portions of regions A and E did not meet the time

![](/api/attachments/WEMK76YR/fulltext/images/bc2d874d719e7484caaec45a9bda03b0681d58b2228585d37ddeb81bfa6ef761.jpg)  
(a) Priority structure I

![](/api/attachments/WEMK76YR/fulltext/images/0b228a77845a8094ecda8af55ee23f2897fb8dd1f680cb1e6b3438e242ad7da0.jpg)  
(b) Priority structure II

![](/api/attachments/WEMK76YR/fulltext/images/741b07ab9205bab01be24dc84fcc1742423a7a3da410d8d848d2680ecfe6e7e4.jpg)  
(c) Priority structure III

![](/api/attachments/WEMK76YR/fulltext/images/13940e9bbafff01626d31d7ef991f4f30f5bc6142b5f19c00cc588c439a53c9d.jpg)  
(d) Priority structure IV  
FiGuRE 1. Partitioned Decision Space for Different Time and Budget Goals (see Table 4 for Description of Each Region).

goal, since the minimum time requirement was 60 days. The budget and time goals were, however, met for a large portion of the decision space. The parameter coverage goal of unity was satisfied only in regions C and F.

In Figure 1, the decision space is partitioned into several closely connected regions, each region having a unique optimal decision. These regions allow the evaluators to estimate the sensitivity of the optimal solution to changes in the subjective cost and time constraints put by management on the project. It is interesting to note that priority structures I and III result in the same decision spaces. Priority structure I gives the highest priority to the time objective. Although structure III treats both the cost and time objectives at the same priority level, the opportunity cost associated with the time objective is very high; as a consequence of this, the results resemble those under priority structure I. Similar observation holds for structures II and IV with respect to the cost objective.

Benchmarking Decision Models for Database Management Systems

<table><tr><td colspan="5">TABLE 4Description of Each Region of the Decision Space</td></tr><tr><td>Region</td><td>Decision</td><td> $f_1$ </td><td> $f_2$ (\$ × 103)</td><td> $f_3$ (days)</td></tr><tr><td>A</td><td>Buy benchmark 1 for parameter 3Buy benchmark 3 for parameters 1, 2, 4</td><td>0.644</td><td>112.4</td><td>60</td></tr><tr><td>B</td><td>Buy benchmark 2 for parameters 3, 5Buy benchmark 3 for parameters 1, 2, 4</td><td>0.632</td><td>107.8</td><td>71</td></tr><tr><td>C</td><td>Develop benchmark 4 for all parameters</td><td>1.000</td><td>38.0</td><td>115</td></tr><tr><td>D</td><td>Buy benchmark 2 for parameters 2, 3, 4, 5Buy benchmark 3 for parameters 1, 2, 4, 6</td><td>0.982</td><td>109.6</td><td>75</td></tr><tr><td>E</td><td>Buy benchmark 1 for parameters 1, 3Buy benchmark 3 for parameters 2, 4</td><td>0.740</td><td>112.6</td><td>60</td></tr><tr><td>F</td><td>Buy benchmark 1 for parameters 1, 3, 5Buy benchmark 2 for parameters 2, 3, 4, 5</td><td>1.118</td><td>129.8</td><td>66</td></tr><tr><td>G</td><td>Buy benchmark 2 for parameters 2, 3, 5Buy benchmark 3 for parameters 1, 4</td><td>0.664</td><td>108.0</td><td>69</td></tr></table>

In Figures 1(b) and 1(d), a large portion of the decision space is occupied by region C. Regions A and B are nonexistent in both cases. These results are intuitive because, within region $\mathbf { c } ,$ the optimal decision is in-house development of the fourth benchmark, whereas within regions A and B, the recommendation is to buy two benchmarks. Given that cost minimization had been given the highest priority in structures II, one would expect that the fourth benchmark, which costs the least, would be preferred.

Another useful observation is the stability of the decisions within régions D, E, and F, which implies that with larger budgets the decision is insensitive to the priority structure, so the user should purchase off-the-shelf benchmarks if available. Moreover, the three highest parameter coverage regions C, D, and F appear at the upper right area of the quadrant. Region F, which provides the best parameter coverage, was always more sensitive to budgetary rather than time constraints.

The results are very sensitive at the low end, i.e., low budget and low available time, because the cost and time resources are very tight and there is no slack. For example, the cost and time requirements within regions A and E are similar, though region E provides a higher parameter coverage than region A; a 15% improvement in parameter coverage is obtained at the additional expense of \$200 by moving from region A to region E. The results appeared to be fairly stable for small changes in the reliability indices; this tends to suggest that, as long as the reliability indices of all the alternative benchmarks are close, they could be dropped from the model without changing the optimal solution.

## 5. Conclusions

Past research in the area of database benchmarking focused primarily on developing particular benchmarks. Some of these benchmarks require extensive modification of the code as well as preparation of data files and design of various queries and user interfaces. In addition, each benchmark has its strengths and weaknesses. The need for decision models determining the optimal level of database benchmarking has largely been overlooked. Modern information systems rely more and more on the performance of large-scale databases, so there is a greater need to develop an integrated decision framework to help users select the optimal set of benchmarks to be run for the purpose of purchasing, capacity planning, regression testing, or tuning.

This research establishes a decision model for database benchmarking that permits systematic analysis and provides insights into the decision problem. Instead of providing the user with a composite metric, we suggest using separate performance metrics for different components of the application workload. The decision model proposed in §3 of this paper determines the optimal mix of benchmarks; it combines three different objectives, namely parameter coverage, cost, and time, in a detailed goal programming formulation. The model parameterizes information-gathering priorities, the reliability of benchmarks, acquisition and execution costs, resource consumption, and overall time requirements. The proposed modeling approach establishes the quantitative framework needed for managing database benchmarking decisions for many purposes, such as procurement, monitoring, design, etc.

The application reported here indicates that this methodology is easy to use, and that it generates a consistent and logical benchmarking plan. By combining the concepts of weighted and absolute priority in our achievement function, we simultaneously tested the impact of conflicting and noncommensurable goals. This methodology is computationally efficient and can handle a large number of decision variables. It also provides a wealth of additional insights by perturbing the initial formulation. For instance. one can redefine the constraint set in order to depict various other policies. Consider an example where users may wish to augment the validity of the testing process by testing each parameter at least twice. This requirement is easily accommodated by setting the right-hand side of constraint (12) to two; then each mandatory parameter will be tested at least twice by two distinct benchmarks. One may also consider that alternative systems can be compared in more than one step. If one has a large set of alternative systems, then it might be economical to run these benchmarks by an elimination process. The elimination process would run only a few important benchmarks on all systems; a subset of the alternative systems could then be eliminated. This process may be repeated several times until a single dominating system remains.

Several insights can be gained from the application illustrated here. Our method not only determines which benchmarks should be purchased (or developed), but also indicates which parameters should be tested with them. For example, regions B, D, and G—all require that benchmarks 2 and 3 be purchased, but they differ in which parameter is tested by each benchmark. It was observed that the decision space could be partitioned into closely connected regions; this indicates that if the decision is well inside a specific region, then it is robust. It is also possible to use a finer grid size if a more accurate trade-off analysis is desired. In this case, we also observed that the priority structure does not affect decisions when budgetary and time constraints are not very tight; it seems that the optimal decisions become most sensitive to changes in time, budget, and priority structure when the above constraints get tighter. In those cases, small changes in the cost goal could lead to dramatic changes in parameter coverage; for example spending additional \$200 in moving from region A to E provides a 15% increase in parameter coverage.

Our decision framework is robust and easy to use because it translates the important characteristics of database benchmarking into an efficient optimization framework. However, the model suffers from a few limitations. Some limitations arise from our attempt to provide the user with an easy-to-use tool, and can be accounted for at the expense of simplicity. Other limitations arise from the inherent complexities associated with benchmarking and the corresponding assumptions made in the model. We have assumed a linear form of the parameter coverage objective function, which means that the marginal information available from running a benchmark for any parameter has constant return to scale. This functional form could be changed to incorporate diminishing return to scale for information. A quasi-linear approximation can easily be made if the new objective function is either convex or concave. The goal levels and the priority structure would typically be determined by a variety of groups including functional users, information systems experts, and the budget officers. Once an initial set of goals is established by the various groups, they would subsequently be reviewed and modified as necessary. The goal formulation process dynamically converges at the desired set of goals and priorities (Shin and Ravindran 1991, Wilson and Jain 1988). This interactive process may consist of several changes in the structure of the feasible decision region as discussed in our case study.

There are certainly several other important issues and questions to be studied in benchmarking database systems; for example, the potential role of knowledge-based expert systems in helping problem formulation and output analysis, or the development of a quantitative framework that integrates empirical testing with performance evaluation models. This paper is an attempt to establish some underlying decision structure which hopefully will help others address some of these issues.\*

Acknowledgements. The authors wish to express their deep gratitude to Mr. Bob Wasilewski and Mr. Daryl Coons of Xerox Corp., Rochester, NY for providing us with sample benchmarking data and many useful discussions. This paper has benefited substantially from the insightful comments and suggestions of Professor Niv Ahituv of Tel Aviv University, Professor Marshall Freimer of the University of Rochester, three unknown reviewers, and an associate editor. The authors wish to thank them all.

\* Prabuddha De, Associate Editor. This paper was received on May 19, 1992, and has been with the authors 9 months for 2 revisions.

## Notation Summary

ā = achievement function as specified by the user.

$\pmb { b _ { \pmb { \mathscr { n } } } }$ = available amount of resource n.

$b _ { y k m }$ = amount of resource n consumed by benchmark k running on system i for parameter i.

$\pmb { c _ { k } }$ = cost of buying or developing benchmark k.

$\pmb { d _ { k } }$ = time needed to develop benchmark k.

$f _ { m }$ = the mth objective.

$G _ { m }$ = goal for the mth objective.

$\pmb { \delta } \pmb { I }$ = the th component of the achievement function.

I = total number of alternative systems, $\pmb { I } = | \pmb { \mathcal { I } } |$

J = set of alternative systems.

J = total number of system parameters to be tested, $J = | \tilde { \phi } |$

$\pmb { \mathcal { A } }$ = set of system parameters to be tested.

$\pmb { \mathscr { s } } _ { \pmb { \imath } }$ = set of mandatory parameters.

$\pmb { \mathscr { s } _ { 2 } }$ = set of optional parameters.

Bitton, D.. D. J. Dewitt, and C. Turbyfill, “Benchmarking Database Systems: A Systematic Approach," Proceedings of the Ninth International Conference on Very Large Databases, November 1983, 8–19. - and C. Turbyfill. “A Retrospective on the Wisconsin Benchmark," Readings in Database Systems M. Stonebraker (Ed.), Morgan Kaufmann, San Mateo, CA, 1988.

## Dey • Seidmann

K = total number of available benchmarks, ${ \pmb { K } } = | { \mathcal { H } } |$ « = set of available benchmarks. L = set of parameters benchmark k can evaluate. N = total number of computer resources, $N = | { \mathcal { N } } | .$ N = set of computer resources. nm , = negative deviation from the goal for the mth objective. Pm , = positive deviation from the goal for the mth objective. qik cost of running benchmark k on system i. the additional cost of running benchmark k on system i for parameter j. rijk Stk time needed to run benchmark k on system i. tuk the additional time needed to run benchmark k on system i for parameter j. vk reliability index of benchmark k (equals 1 for a perfectly reliable benchmark). Wi relative weight of parameter j as specified by the user. W = the maximum of development (acquisition) times for all benchmarks that are used. $\begin{array} { r l r } & { } & { X _ { i i k } = \left\{ 1 , \right. } \\ & { } & \\ & { } & { Y _ { i k } = \left\{ 1 , \right. } \\ & { } & \\ & { } & { Z _ { k } = \left\{ 1 , \right. } \end{array}$ if benchmark k is run on system i for parameter j, otherwise. if benchmark k is run on system $i ,$ otherwise. if benchmark k is bought or developed otherwise.

## References

Ahituv, N., Y. Benjamini, and M. Igbaria, “A Compumetrical Approach for Analysis and Clustering of Computer System Performance Variables," Computers and Operations Research, 15, 6 (1988), 489- 496.

-, I. Borovits, and S. Neumann, "Selecting a Job Mix for Running a Benchmark by Using an Integer Programming Model." Computers and Operations Research, 5, 1 (1978), 73–79.

and M. Igbaria, “A Model for Predicting and Evaluating Computer Resource Consumption," Communication of the ACM, 31, 12 (December 1988), 1467–1473.

Anon et al., “A Measure of Transaction Processing Power," Datamation, 31, 7 (April 1985), 112.

Arbel. A. and A. Seidmann, “Capacity Planning, Benchmarking and Evaluation of Small Computer Systems." European Journal of Operational Research, 22 (1985), 347–358.

Bitran, G. R., “Theory and Algorithms for Linear Multiple Objective Programs with Zero-One Variables," Mathematical Programming, 17, 3 (1979), 362–390.

Boehm B W Software Engineering Economics. Prentice-Hall, Englewood Cliffs, NJ, 1981.

Boral, H. and D. J. Dewitt, "A Methodology for Database System Performance Evaluation," Proceedings of the Annual Meeting of SIGMOD '84. Boston, MA. ACM, June 1984, 176–185.

Canada, J. R. and W. G. Sullivan, Economic and Multiattribute Evaluation of Advanced Manufacturing Systems. Prentice-Hall, Englewood Cliffs, NJ, 1989.

Cattell, R. G. G., "Chapter 6: An Engineering Database Benchmark," The Benchmark Handbook for Database and Transaction Processing Systems, J. Gray (Ed.), Morgan Kaufmann, San Mateo, CA, 1991, 247–281.

Charnes, A, and W. W. Cooper, Management Models and Industrial Applications of Linear Programming, Vol. I. Wiley, New York, 1961.

Gass. S., “A Process to Determine Priorities and Weights for Large-Scale Linear Goal Programming," Proceedings of the 12th International Symposium on Mathematical Programming, Boston, MA, August 1985.

Gray, J., "Chapter 1: Introduction," The Benchmark Handbook for Database and Transaction Processing Systems. Morgan Kaufmann, San Mateo, CA, 1991, 1–17.

Ignizio. J. P., Goal Programming and Extensions, Lexington Books, Lexington, MA, 1976.

Jain, H. K., M. R. Tanniru, and B. Fazlollahi, "MCDM Approach for Generating and Evaluating Alternatives in Requirement Analysis," Information Systems Research, 2, 3 (September 1991), 223–239.

Jain, R., The Art of Computer Systems Performance Analysis, Wiley, NY, 1991.

Kemerer, C. F., “Reliability of Function Points Measurement: A Field Experiment," Communications of the ACM, 36, 2 (February 1993), 85–97.

Korhonen, P., H. Moskowitz, and J. Wallenius, "Multiple Criteria Decision Support—A Review," European Journal of Operational Research, 63 (1992), 361–375.

Lee, S. M., Goal Programming for Decision Analysis, Auerbach Publishers, Philadelphia, PA, 1972.

Nelson, N., "Chapter 7: The Neal Nelson Database Benchmark™M: A Benchmark Based on the Realities of Business," The Benchmark Handbook for Database and Transaction Processing Systems, J. Gray (Ed.), Morgan Kaufmann, San Mateo, CA, 1991, 283–300.

O'Neil, P. E., "Chapter 5: The Set Query Benchmark," The Benchmark Handbook for Database and Transaction Processing Systems, J. Gray (Ed.), Morgan Kaufmann, San Mateo, CA, 1991, 209–245.

Perry, E., Data Processing Budget—How to Develop and Use Efficiently, Prentice-Hall, Englewood Cliffs, NJ, 1985.

Robinson, C., “Databases Come to Windows," PC World, June (1993), 188–206.

Rubenstein, W. B., M. S. Kubicar, and R. G. G. Cattell, "Benchmarking Simple Database Operations," Proceedings of the ACM SIGMOD 1987 Annual Conference, San Francisco, CA, ACM, May 1987, 387-393.

Serlin, O., “Chapter 2: The History of DebitCredit and the TPC," The Benchmark Handbook for Database and Transaction Processing Systems, J. Gray (Ed.), Morgan Kaufmann, San Mateo, CA, 1991, 19–117.

Shaw, R. H., "dBase IV, Version 1.1, A New Beginning," PC Magazine, 10, 2 (January 1991), 155.

Sheppard, G. and R. Weston, “The Power Edge," Corporate Computing, 2, 5 (1993), 88–94

Shin, W. S. and A. Ravindran, "Interactive Multiple Objective Optimization: Survey I—Continuous Case," Computers and Operations Research, 18, 1 (January 1991), 97–114.

Turbyfill, C., C. Orji, and D. Bitton, “AS³AP—A Comparative Relational Database Benchmark," Proceedings of the Thirty-Fourth IEEE Computer Society International Conference, San Francisco, CA, 1989, 560-564.

Wilson, G. R. and H. K. Jain, “An Approach to Postoptimality and Sensitivity Analysis of Zero-One Goal Programs," Naval Research Logistics, 35, 1 (February 1988), 72–84.
