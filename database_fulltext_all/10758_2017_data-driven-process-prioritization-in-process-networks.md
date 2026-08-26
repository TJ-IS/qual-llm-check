---
otero_id: 10758
otero_key: "GS7SZSGX"
title: "Data-driven Process Prioritization in Process Networks"
authors: "Wolfgang Kratsch; Jonas Manderscheid; Daniel Reißner; Maximilian Röglinger"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.02.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

## Data-driven Process Prioritization in process networks

ELSEVIER Decision Support Systems

Wolfgang Kratsch, Jonas Manderscheid, Daniel Reißner, Maximilian Röglinger

![](/api/attachments/GS7SZSGX/fulltext/images/d3b121748610e50c87606284f299f7b9c786b909ab360b4efa8361ca7db58571.jpg)

PII: S0167-9236(17)30036-2

DOI: doi: 10.1016/j.dss.2017.02.011

Reference: DECSUP 12811

To appear in: Decision Support Systems

Received date: 10 July 2016

Revised date: 13 February 2017

Accepted date: 23 February 2017

Please cite this article as: Wolfgang Kratsch, Jonas Manderscheid, Daniel Reißner, Maximilian Röglinger , Data-driven Process Prioritization in process networks. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi: 10.1016/j.dss.2017.02.011

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Data-driven Process Prioritization in Process Networks

Wolfgang Kratsch<sup>1</sup> Jonas Manderscheid<sup>1</sup> Daniel Reißner<sup>1</sup> Maximilian Röglinger<sup>2,a</sup>

<sup>1</sup> FIM Research Center

<sup>2</sup> FIM Research Center

corresponding author

University of Augsburg

University of Bayreuth

(maximilian.roeglinger@

Universitätsstraße 12

Wittelsbacherring 10

fim-rc.de)

86159 Augsburg, Germany

95444 Bayreuth, Germany

## Abstract

Business process management (BPM) is an essential paradigm of organizational design and a source of corporate performance. The most value-creating activity of BPM is process improvement. With effective process prioritization being a critical success factor for process improvement, we propose the Data-Driven Process Prioritization (D2P2) approach. By addressing the weaknesses of extant process prioritization approaches, the D2P2 accounts for structural and stochastic process dependencies and leverages log data. The D2P2 returns a priority list that indicates in which future periods the processes from a process network should undergo the next in-depth analysis to check whether they actually require improvement. The D2P2 contributes to the prescriptive knowledge on process prioritization and process decision-making. As for evaluation, we discussed the D2P2’s design specification against theory-backed design objectives and competing artefacts. We also instantiated the D2P2 as a software prototype and applied the prototype to a real-world scenario based on the 2012 BPI Challenge log.

Keywords: Business Process Management, Process Prioritization, Process Improvement, Business Process Architecture, Process Logs

## 1 Introduction

Process orientation is an accepted paradigm of organizational design and a source of corporate performance [1,2]. Due to substantial progress in process identification, analysis, implementation, and improvement [3,4], business process management (BPM) receives constant attention from industry [1,5]. In particular, process improvement has received significant attention in recent years [6]. However, more than 60% of process improvement projects are reported to fail [7], as organizations focus on inappropriate processes or improve too many processes simultaneously [8]. Hence, process improvement highly depends on effective process prioritization [9].

The BPM literature offers multiple approaches to process prioritization [10]. Extant approaches can be split into performance- and non-performance-based approaches. Performance-based approaches prioritize processes by quantifying their actual and target performance, deriving their need for improvement, and ranking them [1,10,11]. Non-performance-based approaches prioritize processes using criteria such as urgency, strategic importance, or difficulty of improvement [12–14]. Current prioritization approaches are criticized for sharing individual processes as unit of analysis neglecting dependencies among processes as well as for depending on the potentially biased input of domain experts [9].

Neglecting dependencies in process prioritization is a severe drawback as process dependencies are ubiquitous in practice. In organizational settings, hardly any process is executed in isolation. Improving a process usually impacts other processes [15]. Beyond dependencies among different processes, there are also dependencies among the instances of the same process. Consider an instance delayed due to a machine breakdown. Such a delay affects subsequent instances of the same process and other depending processes. Against this background, process dependencies should be treated as an Daeng essential input of process prioritization to avoid a misallocation of corporate funds. In the literature, process dependencies are so far predominantly used for descriptive purposes, e.g., in business process architectures (BPA) and process repositories [15,16]. The only approach that uses process dependencies for process prioritization is the ProcessPageRank (PPR), a derivative of Google’s PageRank that ranks processes according to their dependency-adjusted need for improvement [9]. The PPR extends BPAs with data on process dependencies and the processes’ need for improvement. However, the PPR neglects dependencies among instances. Such dependencies are considered by Letmathe et al. [17], but for capacity planning rather than for process prioritization purposes. Regarding the dependency on the subjective input of domain experts, almost no prioritization approach uses log data, although the uptake of process mining underpins the relevance of data-driven BPM [3,5,18]. This is detrimental as logs not only bear the potential to objectify process prioritization results, but also contain performance and, increasingly, dependency data [19]. So far, log-based BPM approaches support process discovery, conformance checking, and enhancement [20]. To the best of our knowledge, the only approach leveraging log data for process prioritization purposes is the Critical Process Instance Method (CPIM)

# ACCEPTED MANUSCRIPT

[21]. Based on model and log data, the CPIM determines dynamic “service intervals” for business processes, predicting when a process’ risky future performance violates predefined performance thresholds. The CPIM, however, entirely neglects process dependencies. In sum, existing process prioritization approaches neither consider process dependencies nor tap the potential of log data. Thus, we investigate the following research question: How can business processes be prioritized by leveraging performance and dependency data from process logs?

To address this question, we adopted the design science research (DSR) paradigm and proposed the Data-Driven Process Prioritization (D2P2) approach [22]. Combining extant research on process prioritization and process performance prediction, the D2P2 leverages performance and dependency data from process logs to determine the risky performance of involved processes. Thereby, it accounts for structural dependencies (e.g., processes that use other processes) and stochastic dependencies (e.g., instances that affect instances of the same process). Based on the dependency-adjusted risky process performance, the D2P2 predicts when each process is likely to violate predefined performance thresholds, and schedules it for in-depth analysis in future planning periods. Process analysts can then check whether the process actually requires improvement. If a high-quality log is available, the D2P2’s output is more reliable and detailed than other prioritization approaches. As justificatory knowledge, the D2P2 draws from ideas related to the PPR (i.e., dependency-aware process prioritization) and CPIM (i.e., dynamic scheduling of in-depth analyses based on predicted performance). To extend these ideas, the D2P2 builds on further knowledge such as multi-variate data analysis, simulation, and optimization, which we introduce when outlining the D2P2’s design specification. Using knowledge from these areas is sensible when extracting and predicting the performance of interdependent processes based on process logs and when identifying the optimal sequence in which these processes should be analyzed.

Following the DSR reference process, our study is structured as follows [23]: In section 2, we outline background on process dependencies, process performance, and performance prediction. We also derive design objectives. In section 3, we propose the D2P2’s design specification. Section 4 reports on our evaluation activities. We conclude in section 5 by discussing results, highlighting limitations, and pointing to future research.

## 2 Background and design objectives

## 2.1 Business process management and process dependencies

BPM is the art and science of overseeing how work is performed to ensure consistent outcomes and take advantage of improvement opportunities [1]. BPM combines knowledge from information technology and management sciences [5]. It is typically structured along lifecycle models [24], including activities such as process identification, discovery, analysis, improvement, implementation, monitoring, and controlling [1]. As for process improvement, van der Aalst [5] distinguishes between datadriven and model-based approaches. While model-based approaches support improvement at design time, data-driven approaches help eliminate problems at runtime [5].

Although organizations must manage many processes, almost no process prioritization approach covers process networks, i.e., multiple interdependent processes [9]. The common way of dealing with process dependencies is through process repositories and BPAs [15,16]. Repositories maintain large process model collections [25]. BPAs visualize structural dependencies among processes with specialization, decomposition, use, and trigger being the most frequent dependency types [15,16]. Specialization dependencies indicate that a process is a specialized version of another process, inheriting characteristics of the super-process. Decomposition dependencies split processes into multiple sub-processes. As for use dependencies, the instances of one process may call for instances of other processes, depending on the output of these instances to continue or complete execution. Trigger relations indicate that the instances of one process may initiate the execution of other processes’ instances without depending on their output [15]. This is why the performance of triggering and triggered processes is independent [9], whereas the performance of using processes depends on that of used processes [26]. This property is relevant when considering process dependencies in process prioritization. Lehnert et al. [9] use the idea of structural dependencies to define process networks. Process networks extend BPAs by adding information about processes (e.g., their individual need for improvement) as node weights and about dependencies (e.g., the strength of dependencies) as edge weights.

Besides structural dependencies, processes are subject to stochastic dependencies. Letmathe et al. [17] distinguish intra- and inter-process dependencies. Inter-process dependencies arise, for example, when higher or lower skilled employees are assigned to a production stage. In this case, the execution time of all processes may increase or decrease [17]. Intra-process dependencies occur if the instances of a distinct process, i.e., the performance of these instances, are positively or negatively auto-

# ACCEPTED MANUSCRIPT

correlated. The most common manifestation are positive auto-correlations [17]. For example, a machine breakdown in a distinct instance will probably cause delays in subsequent instances. Stochastic dependencies also reflect positive or negative deviance experienced in past process executions [21,27]. Structural and stochastic process dependencies cannot be considered in isolation, i.e., structural use dependencies imply stochastic inter-process dependencies. That is, a machine breakdown in a production process influences the performance of those processes that use the output of the production profor them when prioritizing processes. This leads to our first design objective for the D2P2 approach: (O.1) Process dependencies: Effective process prioritization requires accounting for (O.1a) stochastic

## 2.2 Process performance measurement and prediction

Process performance management is the active management of processes based on performance indicators, including the comparison of performance indicators with benchmarks and admissible value ranges [11]. Process performance management aims to dev an in-depth understanding of process performance and to improve processes accordingly [28]. When prioritizing processes, it is necessary to resolve trade-offs among multiple process indicators (e.g., time, cost, quality, flexibility) as improving one indicator usually weakens at least one other [29]. To do so, methods from multi-criteria decision another possibility commonly used in process prioritization. Examples are the value contribution of a process [31], the return on process transformation [32], the aggregated cash flow difference from a predefined benchmark [21], and the business value score [10]. In line with value-based BPM, a paradigm for economically well-founded process decision-making, integrated performance indicators should rely on objective monetary quantities, take a long-term perspective, and account for process risks [31,32]. Indicators that meet these criteria are the value contribution of a process (for valuing and comparing alternative process improvement projects) and the aggregated cash flow difference (for process performance monitoring and prediction). Both indicators build on process cash flows. Process cash flows rely on process costs, which are either included in process logs or can be inferred by monetizing execution times and material usage. In contrast to costs, process cash flows also cover the positive monetary effects of process execution (e.g., product sales). In the value-based BPM literature, there are several methods that help valuate processes in line with stochastic process dependencies and complex control flows [33]. The CPIM also complies with the principles of value-based BPM [21].

With the uptake of process mining and process-aware information systems, ever more data about historical process instances is becoming available via process logs [18,20]. Process logs record events, where each event refers to a distinct task and instance [20]. Process logs may include data not only about tasks, paths, and task performance, but also about structural and stochastic dependencies [34]. Logging the events related to multiple processes or even process networks, information such as the distribution of process cash flows, the frequency with which processes use other processes, or the auto-correlation of process instances can be mined. Logs are a powerful data source, which should be leveraged for process prioritization as far as possible and available [18]. The D2P2 will do so.

Process prioritization should not only use log data, but also forecast the risky future performance of processes. Whereas process mining focuses on historical data, process intelligence includes other data such as from legacy applications or email logs to anticipate future process behavior or performance [35,36]. The focus on future process performance is also referred to as predictive analytics [35,37,38]. Examples are the prediction of abnormal process terminations [39] or of the completion time of future process instances [40]. Leveraging performance data from process logs, one can also predict the future risky process performance to detect when processes will violate performance thresholds [21]. Against this background, we define our second design objective for the D2P2 approach: (O.2) Process Performance Measurement and Prediction: Effective process prioritization requires accounting for the (O.2a) current and (O.2b) future risky performance of processes.

## 3 Design specification

## 3.1 Overview and procedure model

The D2P2 prioritizes processes by leveraging performance data (i.e., process cash flows) and dependency data (e.g., how often processes use other processes) from process logs. As shown in Figure 1, the D2P2 includes three steps: (1) extraction of the involved processes’ dependency-adjusted risky performance, (2) prediction of these processes’ risky future performance, and (3) scheduling of the in volved processes for in-depth analysis. Before going into detail, we provide a high-level overview of these steps along with the methods from outside the traditional BPM toolbox we used.

![](/api/attachments/GS7SZSGX/fulltext/images/322192ca39d6497919266cc6c17ae43c8ba81cb6aa888bc93263bee96f08aee0.jpg)  
Figure 1 – Overview of the D2P2 approach

In step 1, the D2P2 uses process logs to extract the processes to be prioritized as well as relevant structural and stochastic dependencies in terms of a process network. Thereby, the D2P2 requires either an integrated log that captures multiple processes or multiple single-process logs to be joined. On this foundation, the D2P2 determines the dependency-adjusted performance of each process in terms of its risky process cash flow. As a central component of the D2P2, the dependency-adjusted risky performance reflects the stand-alone performance of a process adjusted by the effects of stochastic and structural dependencies. In line with the principle of causation, the dependency-adjusted risky performance captures each process’ fair share of the performance of the entire process network. Resolving all dependencies, the dependency-adjusted risky performance enables treating each process individually in subsequent steps of the D2P2. To determine the dependency-adjusted risky performance, the D2P2 applies multi-variate regression analysis and introduces the concept of process performance variants.

In step 2, the D2P2 uses the dependency-adjusted risky performance from step 1 to predict how the involved processes’ will perform in the future. To identify whether and when involved processes will be subject to substantial under- or over-performance, a circumstance that should lead to an indepth analysis, the D2P2 calculates in which future planning period the aggregated difference between the predicted performance and a predefined benchmark (e.g., the expected process cash flow) is likely to violate predefined thresholds (e.g., upper and lower performance boundaries). As the dependencyadjusted risky performance is a random variable, this D2P2 step draws from methods such as Monte Carlo simulation and financial mathematics (i.e., stochastic processes and confidence intervals).

In step 3, the D2P2 leverages the insights into the processes’ future under- and overperformance gathered in step 2 to schedule each process to a distinct planning period for an in-depth

# ACCEPTED MANUSCRIPT

analysis. If two or more processes should be scheduled to the same period, the D2P2 resolves such conflicts by considering the opportunity costs that would accrue for lost improvement potential. The D2P2 also accounts for capacity restrictions, i.e., how many processes an organization can analyze in a single period (e.g., determined by the number of process analysts) and how complex the involved processes are. Technically, this step of the D2P2 draws from the operations research (OR) literature, particularly from mixed integer linear programming (MILP). The D2P2 returns a priority list indicating in which future periods the involved processes should undergo an in-depth analysis. Due to the risky nature of future process performance, the D2P2 estimates whether processes are likely to violate prewhether they actually violate these thresholds. If so, improvement projects should be initialized.

## 3.2 Process networks and performance variants

Two essential concepts of the D2P2 are process networks and performance variants, particularly for determining the dependency-adjusted risky process performanc step 1. This is why we outline both concepts upfront. Extending BPAs, process networks includ , structural dependencies (e.g., use dependencies), and further inform tion about pro and dependencies [9]. In process networks, directed edges between two different pro denote that instances of one process may cal instances of the other process, requiring the outcome of used instances to proceed or terminate. Such use dependencies are annotated with information about how often they occur per period. To express that processes can be executed without using other processes, process networks include self-directed edges, annotated with information about how often the process is executed stand-alone. Figure 2 shows an exemplary process network, which we use as running example in this section. In this example, process P1 uses P2, but can also be executed stand-alone. Thus, there is a directed edge from P1 to P2, representing a use dependency, and a self-directed edge for P1 capturing stand-alone executions.

![](/api/attachments/GS7SZSGX/fulltext/images/8ec438f04b6574d7ed67cc9a563897974557d3f26f096dbbd3975b9163e602c9.jpg)  
Figure 2 – Exemplary process network

# ACCEPTED MANUSCRIPT

Leveraging the information from process networks, the performance of each process can be decomposed into performance variants based on how use dependencies are embedded in the process’ internal control flow and whether other processes are used or not. A performance variant includes all execution paths of a process that contain the same use dependencies. Performance variants help determine the processes’ dependency-adjusted risky performance, which captures the processes’ fair share of the performance of the entire process network. To determine the fair share, the D2P2 uses performance the poor performance of used processes). This re-allocation enables treating all processes individually in subsequent steps of the D2P2. As some tasks of a process may appear in all execution paths, performance variants typically overlap to a certain extent. Thus, each performance variant can be decomposed into a common core part and a variant-specific part. In case the variant-specific part of a process performance variant includes a use dependency, it must be decomposed into a part that is exclusive to that process and another part that results from using another process. The latter part must be reallocated to the used process s the performance variants of process P1 from our running example. P1 has two performance variants, i.e., 12 to capture the use dependency with P2 and 11 as P1 can be executed stand-alone. Performance variant 12 includes a common (i.e., a1 and a4) and a variant-specific part (i.e., a3, a5, and P2), which splits into an exclusive part (i.e., a3 and a5) and a part caused by using P2.

![](/api/attachments/GS7SZSGX/fulltext/images/5d674ab510b5b2ba1e2fca84890b2d1b9486ac9f2553c62cf47467a166e5ab7c.jpg)  
Figure 3 – Exemplary performance variants of process P1 from the running example

## 3.3 Step 1: Extracting the dependency-adjusted risky process performance

To determine the dependency-adjusted risky process performance, the D2P2 first extracts a process network based on dependency data included in the given process logs. The resulting process network

# ACCEPTED MANUSCRIPT

includes one node per process $( i \in I )$ and directed edges for use dependencies or stand-alone executions. Each edge is either annotated with the number of instances $N _ { i , j } ^ { \mathrm { l o g } }$ of process that use instances of process $( i \neq j )$ or with the number of stand-alone executions $( i = j )$ . After that, the D2P2 leverages the performance data included in the process logs to infer a random variable and a related probabil ity distribution for the dependency-adjusted risky performance of each process. In line with the principles of value-based BPM, the D2P2 measures process performance in terms of a process’ risky cash flows $\widetilde { C F } _ { i }$ at the level of process instances. Process cash flows are directly included in process logs, or must be estimated based on execution times and material usage. Below, we outline how the D2P2 deals with structural and stochastic process dependencies when determining the dependency-adjusted risky process performance.

## 3.3.1 Catering for structural process dependencies

The risky cash flows of a process build on the empirical cash flow data $C F _ { i } ^ { 1 0 8 }$ included in the logs, which must be decomposed hierarchically to be able to allocate performance in line with the principle of causation. On the top-most level, the cash flow data of a process covers the performance of all past instances including the performance of used instances and stand-alone executions. The D2P2 decomposes the empirical cash flow data into the cash flows of each performance variant $C F _ { i , j } ^ { \mathrm { l o g } }$ , which are split into a common core performance part $\widetilde { C F } _ { i } ^ { \mathrm { c c } }$ and a variant-specific performance part $\widetilde { C F } _ { i , j } ^ { \mathrm { v s } }$ . In case the variant-specific part of a performance variant includes use dependencies, it also depends on the empirical cash flow data of the related used processes $C F _ { j } ^ { \mathrm { l o g } }$ . That is, only a distinct part $\widetilde { C F } _ { i , j } ^ { \mathrm { v s } , i }$ of the variant-specific part is caused by process . The remaining part must be reallocated to process .

To extract the hierarchical cash flow structure of the empirical performance data from given process logs, the D2P2 builds on multi-variate regression analysis. Multi-variate regression analysis is commonly used to determine a functional relationship (dependency) between a dependent variable (i.e., a known process cash flow or part of it) and multiple independent variables (i.e., other parts of the process cash flow) [41]. On the one hand, regression analysis returns regression coefficients $\beta$ that indicate how strongly the dependent variable depends on the independent variables. On the other, regression analysis returns constants , which captures the dependent variable’s value in case all independent variables are zero, and residuals as error terms [41].

When applying multi-variate regression analysis, the D2P2 first calculates the variant-specific performance part of each process performance variant by comparing each performance variant with all other performance variants of the same process. The D2P2 determines the variant-specific part of the performance variants $\widetilde { C F } _ { i , j } ^ { \mathrm { v s } }$ as shown in Eq. (1) and Eq. (2). All equations that use $\cdot \approx ^ { \gamma }$ are regression functions. The second term of Eq. (1) captures all performance parts of the process performance variant $i  j$ that also occur in other process performance variants. Thus, in Eq. (2), the variant-specific part of performance variant $i  j$ equals the overall empirical cash flows of performance variant $i  j$ minus the second term of Eq. (1).

$$
C F _ {i, j} ^ {\mathrm{log}} \approx \alpha_ {i, j} ^ {\mathrm{vs}} + \sum_ {k \in I \backslash \{j \}} \beta_ {i, k} ^ {\mathrm{vs}} \cdot C F _ {i, k} ^ {\mathrm{log}} + \varepsilon_ {i, j} ^ {\mathrm{vs}}, \quad \forall i, j \in I\tag{1}
$$

$$
\widetilde {C F} _ {i, j} ^ {\mathrm{vs}} = C F _ {i, j} ^ {\log} - \sum_ {k \in I \setminus \{j \}} \beta_ {i, k} ^ {\mathrm{vs}} \cdot C F _ {i, k} ^ {\log}, \quad \forall i, j \in I\tag{2}
$$

The common core performance $\widetilde { C F } _ { i } ^ { \mathrm { c c } }$ of process equals that part of the overall empirical cash flow data $C F _ { i } ^ { \mathrm { l o g } }$ that is not exclusive to any performance variant. The D2P2 determines the common core performance part as shown in Eq. (3) and (4). To do so, the second term in Eq. (4), which reflects the variant-specific part of each performance variant, must be subtracted from the overall cash flow of process .

$$
C F _ {i} ^ {\mathrm{log}} \approx \alpha_ {i} ^ {\mathrm{cc}} + \sum_ {k \in I} \beta_ {k} ^ {\mathrm{cc}} \cdot \widetilde {C F} _ {i, k} ^ {\mathrm{vs}} + \varepsilon_ {i} ^ {\mathrm{cc}}, \quad \forall i \in I\tag{3}
$$

$$
\widetilde {C F} _ {i} ^ {\mathrm{cc}} = C F _ {i} ^ {\log} - \sum_ {k \in I} \beta_ {k} ^ {\mathrm{cc}} \cdot \widetilde {C F} _ {i, k} ^ {\mathrm{vs}}, \quad \forall i \in I\tag{4}
$$

As discussed, the variant-specific performance part $\widetilde { C F } _ { i , j } ^ { \mathrm { v s } }$ may split into a part caused by process and another part that results from structural dependencies with another process . The D2P2 determines the intensity of such dependencies $\beta _ { i , j } ^ { \mathrm { v s , } j }$ as shown in Eq. (5). On this foundation, the D2P2 determines the exclusive part of the variant-specific part of performance variant $i  j ,$ , i.e., $\widetilde { C F } _ { i , j } ^ { \mathrm { v s } , i }$ , by subtracting the second term of Eq. (5) from the variant-specific part of performance variant $i  j ,$ , see Eq. (6).

$$
\widetilde {C F} _ {i, j} ^ {\mathrm{vs}} \approx \alpha_ {i, j} ^ {\mathrm{vs}, j} + \beta_ {i, j} ^ {\mathrm{vs}, j} \cdot C F _ {j} ^ {\mathrm{log}} + \varepsilon_ {i, j} ^ {\mathrm{vs}, j}, \quad \forall i \in I, \forall j \in I \backslash \{i \}\tag{5}
$$

$$
\widetilde {C F} _ {i, j} ^ {\mathrm{vs}, i} = \left\{ \begin{array}{c c} \widetilde {C F} _ {i, j} ^ {\mathrm{vs}} - \beta_ {i, j} ^ {\mathrm{vs}, j} \cdot C F _ {j} ^ {\log}, & \forall i \in I, \forall j \in I / \{i \} \\ \widetilde {C F} _ {i, j} ^ {\mathrm{vs}}, & \forall i \in I, j = i \end{array} \right.\tag{6}
$$

Having separated the empirical cash flow data of all processes, the D2P2 disposes of all information that characterizes the processes’ performance. On this foundation, we can formulate the dependencyadjusted risky performance of each process $\widetilde { C F } _ { i }$ for structural dependencies. $\mathbf { A } s$ the common core performance part $\widetilde { C F } _ { i } ^ { \mathrm { c c } }$ occurs in each instance, it occurs in the risky performance of all instances independent of structural dependencies. The variant-specific performance parts, however, depend on structural dependencies. In line with our objective of allocating performance according to the principle of causation, variant-specific performance parts that are caused by used processes must be reallocated. To do so, the D2P2 reduces the variant-specific performance part of using processes (except for cases where $i = j )$ as shown in Eq. (6). At the same time, the D2P2 increases the performance of used processes by adding the respective remaining part of the variant-specific performance as shown in Eq. (8). Adding and subtracting the same amount of performanc D2P2 leaves the overall performance of the process network unchanged. However, the D2P2 must only reallocate performance if a process uses other processes. This must be done based on the probability $p _ { i , j }$ with which performance variants $i  j$ occur. The D2P2 estimates the variant probabilities based on log data as shown in Eq. (7).

$$
p _ {i, j} = \frac {N _ {i , j} ^ {\log}}{\sum_ {j \in I} N _ {i , j} ^ {\log}}, \quad \forall i, j \in I\tag{7}
$$

Based on all intermediate results so far, the risky process cash flow $\widetilde { C F } _ { i }$ can be specified as shown in Eq. (8) and, after a mathematical rearrangement, as shown in Eq. (9). Eq. (8) indicates that the dependency-adjusted risky performance of a process equals the sum of the common core performance part, the weighted variant-specific performance parts that are caused by that process, and the weighted reallocated performance parts due to structural dependencies incoming from other processes. This outcome, however, only accounts for structural process dependencies from the process network.

$$
\widetilde {C F} _ {i} = \widetilde {C F} _ {i} ^ {\mathrm{cc}} + \sum_ {j \in I} p _ {i, j} \cdot \widetilde {C F} _ {i, j} ^ {\mathrm{vs}, i} + \sum_ {j \in I \setminus \{i \}} p _ {j, i} \cdot \beta_ {i, j} ^ {\mathrm{vs}, j} \cdot \widetilde {C F} _ {i}, \quad \forall i \in I\tag{8}
$$

$$
\widetilde {C F} _ {i} = \frac {\widetilde {C F} _ {i} ^ {\mathrm{cc}} + \sum_ {j \in I} p _ {i , j} \cdot \widetilde {C F} _ {i , j} ^ {\mathrm{vs} , i}}{1 - \sum_ {j \in I \setminus \{i \}} p _ {j , i} \cdot \beta_ {i , j} ^ {\mathrm{vs} , \mathrm{j}}}, \quad \forall i \in I\tag{9}
$$

## 3.3.2 Catering for stochastic process dependencies

Next, the D2P2 integrates stochastic process dependencies (i.e., dependencies among the instances of one process) in the dependency-adjusted risky process performance. For each process, the D2P2 investigates the chronological sequence of the related instances based on data from the given process logs. This enables capturing how strongly the performance of process instances influences the performance of subsequent instances. As for our running example: if an IT service that supports process P1 breaks down in a distinct instance, a circumstance that causes severe delay due to manual work, immediately subsequent instances will most likely be delayed, too.

To examine the stochastic dependency between subsequent instances of a distinct process, the D2P2 builds on correlation effects and time series analysis, which is a particular variant of regression analysis. More precisely, as the D2P2 considers the relationship between performance values of the same process at different points in time (i.e., for distinct instances), i ines the auto-correlation of the process performance as a function of the time lag betw equent instances [42]. We refer to this as a “lag of one instance” [17,42]. Analogous to the decomposition of empirical cash flow data for the treatment of structural process dependencies, the D2P2 distinguishes an auto-correlated common core performance part and an auto-correlated exclusive variant-specific performance part, which is caused by the process itself. Figure 4 illustrates the basic idea based on our running example. The topmost timeline indicates that the auto-correlated common core performance part is determined based on all pairs of immediately subsequent instances of a distinct process (here: P1). The second and the third timelines show that the auto-correlated exclusive variant-specific performance part builds on immediately subsequent instances of the same performance variants (e.g., 12 or 11).

Technically, the performance of the $n _ { i } .$ -th instance of process , which is the $n _ { i , j }$ -th instance of process using process , depends on the common core performance part $\widetilde { C F } _ { i , n _ { i } - 1 } ^ { \mathrm { c c } }$ of the previous instance and the exclusive variant-specific performance part $\widetilde { C F } _ { i , j , n _ { i , j } - 1 } ^ { \boldsymbol { v s , i } }$ of the latest instance that used process . To determine the regression coefficients $\beta _ { i } ^ { \mathrm { c c , a u t o } }$ and $\beta _ { i , j } ^ { \mathrm { v s , a u t o , \it j } }$ , the D2P2 uses Eq. (10) and Eq. (12). On this foundation, the auto-correlated common core performance part $\widetilde { C F } _ { i , n _ { i } } ^ { \mathrm { c c , a u t o } }$ and the exclusive variant-specific performance part $\widetilde { C F } _ { i , j , n _ { i , j } } ^ { \mathrm { v s , a u t o } , i }$ can be calculated following Eq. (11) and Eq. (13). This approach is analogous to the treatment of structural process dependencies above, except from the fact that the regression analyses conducted here correlate data from the same processes.

![](/api/attachments/GS7SZSGX/fulltext/images/c8c2a2fdd6d648df97d731cc95d846a6a788e4cdaf17721d038c1a786d732f02.jpg)  
Figure 4 - Decomposed auto-correlation effects between subsequent instances

$$
\widetilde {C F} _ {i, n _ {i}} ^ {\mathrm{cc}} \approx \alpha_ {i} ^ {\mathrm{cc,auto}} + \beta_ {i} ^ {\mathrm{cc,auto}} \cdot \widetilde {C F} _ {i, n _ {i} - 1} ^ {\mathrm{cc}} + \varepsilon_ {i} ^ {\mathrm{cc,auto}}, \quad \forall i \in I, \forall n _ {i} \in N _ {i}\tag{10}
$$

$$
\widetilde {C F} _ {i, n _ {i}} ^ {\mathrm{cc}, \mathrm{auto}} = \widetilde {C F} _ {i, n _ {i}} ^ {\mathrm{cc}} - \beta_ {i} ^ {\mathrm{cc}, \mathrm{auto}} \cdot \widetilde {C F} _ {i, n _ {i} - 1} ^ {\mathrm{cc}}, \quad \forall i \in I, \forall n _ {i} \in N _ {i}\tag{11}
$$

$$
\widetilde {C F} _ {i, j, n _ {i, j}} ^ {\mathrm{vs}, i} \approx \alpha_ {i, j} ^ {\mathrm{vs,auto}, j} + \beta_ {i, j} ^ {\mathrm{vs,auto}, j} \cdot \widetilde {C F} _ {i, j, n _ {i, j - 1}} ^ {\mathrm{vs}, i} + \varepsilon_ {i, j} ^ {\mathrm{vs,auto}, j}, \quad \forall i, j \in I, \forall n _ {i} \in N _ {i}\tag{12}
$$

$$
\widetilde {C F} _ {i, j, n _ {i, j}} ^ {\mathrm{vs}, \mathrm{auto}, i} = \widetilde {C F} _ {i, j, n _ {i, j}} ^ {\mathrm{vs}, i} - \beta_ {i, j} ^ {\mathrm{vs}, \mathrm{auto}, j} \cdot \widetilde {C F} _ {i, j, n _ {i, j - 1}} ^ {\mathrm{vs}, i}, \quad \forall i, j \in \mathrm{I}, \forall n _ {i} \in N _ {i}\tag{13}
$$

Based on these results, the dependency-adjusted risky process performance of process ’s $n _ { i } .$ -th instance can be calculated as shown in Eq. (14). This equation incorporates the auto-correlation effects as well as the intermediate results from Eq. (9), which already catered for structural process dependencies. The main idea of Eq. (14) is to substitute performance parts that cater for stochastic process dependencies for those that do not cater for stochastic process dependencies.

$$
\widetilde {C F} _ {i, n _ {i}} ^ {\mathrm{auto}} = \frac {\widetilde {C F} _ {i , n _ {i}} ^ {\mathrm{cc,auto}} + \beta_ {i} ^ {\mathrm{cc,auto}} \cdot \widetilde {C F} _ {i , n _ {i} - 1} ^ {\mathrm{cc}} + \sum_ {j \in I} p _ {i , j} \cdot (\widetilde {C F} _ {i , j , n _ {i , j}} ^ {\mathrm{vs,auto} , i} + \beta_ {i , j} ^ {\mathrm{vs,auto} , j} \cdot \widetilde {C F} _ {i , j , n _ {i , j} - 1} ^ {\mathrm{vs} , i})}{1 - \sum_ {j \in \mathrm{I} \backslash \{i \}} p _ {j , i} \cdot \beta_ {i , j} ^ {\mathrm{vs} , j}}, \forall i \in I, \forall n _ {i} \in N _ {i}\tag{14}
$$

Besides the dependency-adjusted risky process performance, the D2P2 accounts for the processes’ execution frequency to forecast in step 2 whether, and in which planning period, the involved processes violate performance thresholds [9]. Depending on the process at hand, the number of instances (e.g., the process demand) typically differs per period. The D2P2 thus considers demand volatility as a second type of stochastic dependency for process prioritization purposes. The risky number of execu-

# ACCEPTED MANUSCRIPT

tions may be continuous and predictable, fluctuating (e.g., seasonable demand or based on advertising), or something in between. The combination of a rather predictable and a strongly volatile number of instances per period is comparable to a common phenomenon from the field of automotive accident claims. That is, besides an average number of claims per year, there may be volatile accumulations owing to weather conditions. Thus, we can draw an analogy between automotive accident claims and the process demand. Based on this analogy, the D2P2 adopts the concept of stochastic Delaporte processes from financial mathematics that capture two types of risky demand by independent, but differently weighted Poisson and Polya distributed arrivals [43]. The Delaporte distribution is determined by the constant average inter-arrival time for Poisson-distributed arrivals, which reflect continuous demand, as well as by a gamma-distributed average inter-arrival time parameterized by and for Polya-distributed arrivals that reflect the natural fluctuations. Thus, the D2P2 derives the number of process ’s instances that occur in any distinct period $\widetilde { N } _ { i }$ following Eq. (15). The required input parameters can be gathered from process logs according to Rigby et al. [44]. In sum: by integrating structural and stochastic process dependencies, the D2P2 can predict the future dependency-adjusted risk process performance of each involved process at any point ime based on the data from process logs.

$$
\widetilde {N} _ {i} \sim D e l \left(\lambda_ {i} ^ {\log}, a _ {i} ^ {\log}, b _ {i} ^ {\log}\right), \quad \forall i \in I, \forall t \in T\tag{15}
$$

## 3.4 Step 2: Predicting risky future process performance

As the D2P2 aims to determine whether and in which future period the involved processes should undergo an in-depth analysis, it must predict the processes’ future dependency-adjusted risky performance. With process managers prioritizing processes by comparing their actual and target performance, the D2P2 assesses over- and under-performance in terms of the difference between an instance’s predicted perform nce $\widetilde { C F } _ { i , n _ { i } } ^ { \mathrm { a u t } 0 }$ and a predefined process-specific benchmark $B _ { i }$ [21] (e.g., the expected process cash flow). As performance differences of individual instances are too fine-grained for process prioritization, the D2P2 is able to aggregate the performance difference of all instances executed until the end of any period . The D2P2 thereby accounts for the number of instances per period as shown in Eq. (15). The result is an aggregated performance difference $\delta _ { i , t }$ as shown in Eq. (16). Thereby, the aggregated number of executions $\widetilde { N } _ { i , t } ^ { \mathrm { a g g } }$ is a random variable as it adds up the risky number of instances per period.

$$
\delta_ {i, t} = \sum_ {n _ {i} = 1} ^ {\widetilde {N} _ {i, t} ^ {\mathrm{agg}}} \left(\widetilde {C F} _ {i, n _ {i}} ^ {\mathrm{auto}} - B _ {i}\right), \forall i \in I, \forall t \in T \mathrm{with} \widetilde {N} _ {i, t} ^ {\mathrm{agg}} = \sum_ {1} ^ {t} \widetilde {N} _ {i}\tag{16}
$$

The aggregated difference is the D2P2’s central indicator for determining when to schedule a process for in-depth analysis. The aggregated difference is risky and may take any value. As a sum of random variables, its value range is cone-shaped (Figure 5), i.e., its value range is small in the near future and continuously broadens in the farer future. It is possible to determine the aggregated difference’s value range as a confidence interval in which the true value lies with a distinct probability $w \in \left] 0 ; 1 \right[ \mathrm { ( i . e . }$ •, confidence level) based on its inverse cumulative distribution function $F ^ { - 1 } \big ( \delta _ { i , t } , w \big )$

![](/api/attachments/GS7SZSGX/fulltext/images/553667aefc356104550b28f08ced3033f0d18608413962aa2412a28915f97873.jpg)  
Figure 5 – Cone-shaped structure of the predicted aggregated performance difference

To estimate the cumulative distribution function of the aggregated performance difference, the D2P2 must generate a large sample of random values using Monte Carlo simulation [45]. On this foundation, the D2P2 creates a histogram that helps approximate the aggregated difference’s distribution using kernel density estimation [45]. The confidence level, which is required to determine the confidence interval, must be set by the management (e.g., 95%). Higher confidence levels (e.g., 99%) increase the probability that the confidence interval contains the true future value of the dependency-adjusted risky process performance, but it may lead to overly early in-depth analyses.

To identify substantial under- and over-performance of a process, a circumstance that should lead to an in-depth analysis, the D2P2 builds on further control parameters, i.e., an upper performance threshold $\delta _ { i } ^ { \mathrm { m a x } }$ and a lower performance threshold $\delta _ { i } ^ { \mathrm { m i n } }$ per process. Exceeding the upper performance threshold implies substantial positive deviance, which provides a chance for first mover ad-

# ACCEPTED MANUSCRIPT

vantages or a reallocation of assigned resources. Violating the lower performance threshold mirrors substantial negative deviance, which threatens the profitability or competitiveness of the process in focus [1,21,27,46]. A process should undergo an in-depth analysis if the predicted aggregated performance difference violates at least one performance threshold at the given confidence level. Thus, the D2P2 determines the highest absolute aggregated under- or over-performance $\Delta _ { i , t }$ per process and period based on the predefined performance thresholds and the predicted aggregated performance difference as shown in Eq. (17). For processes whose predicted aggregated performance difference exceeds no threshold, the highest absolute aggregated under- or over-performance is zero. Exceeding a performance threshold, however, does not necessarily mean that an in-depth analysis is scheduled for the respective period. The reason is potential conflicts (e.g., insufficient capacities to analyze all processes scheduled to a distinct planning period), which are resolved in step 3 of the D2P2.

$$
\Delta_ {i, t} = \max \Bigl (\max \bigl (F ^ {- 1} \bigl (\delta_ {i, t}, w \bigr) - \delta_ {i} ^ {\max}, 0 \bigr), \max \bigl (\delta_ {i} ^ {\min} - F ^ {- 1} \bigl (\delta_ {i, t}, w \bigr), 0 \bigr) \Bigr), \forall i \in I, \forall t \in T\tag{17}
$$

## 3.5 Step 3: Scheduling processes for in-depth analysis

Finally, the D2P2 schedules the involved processes for an in-depth analysis in line with their absolute aggregated under- or over-performance determined in step 2. Thereby, the D2P2 must handle conflicts. The most typical conflicts relate to the number of in-depth analyses that an organization can perform per period [8]. If several processes are scheduled to the same period, the organization may not have enough capacity to analyze all processes simultaneously such that some processes must be rescheduled. To resolve such conflicts, the D2P2 seeks for an assignment of in-depth analyses to planning periods that minimizes the opportunity costs for lost improvement potential in case of lower threshold violations and untapped opportunities in case of upper threshold violations. The corresponding optimization problem is shown in Eq. (18). The D2P2 measures opportunity costs $o _ { i , t }$ in terms of the maximum absolute under- or over-performance $\Delta _ { i , t }$ from Eq. (17).

$$
\min \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {I} o _ {i, t}\tag{18}
$$

This optimization problem is a typical assignment problem known in the OR literature [47]. That is, the D2P2 matches processes and planning periods at minimum cost while considering constraints in terms of linear equations or inequalities. Below, we specify the constraints of the optimization problem. To model that process should be analyzed in-depth in a distinct period , the D2P2 uses binary auxiliary variables $x _ { i , t }$ as shown in Eq. (19). As the D2P2 schedules processes for in-depth analysis but cannot foresee the outcome of in-depth analyses, each involved process can undergo at the most one in-depth analysis in the planning horizon. If the D2P2 already knew the outcomes of the in-depth analyses, it could directly schedule improvement projects instead of in-depth analyses. In Eq. (20), the D2P2 thus limits the number of in-depth analyses per process in the planning horizon to one. For the same reason, the D2P2 neglects opportunity costs for all periods after an in-depth analysis has been scheduled for a distinct process. This is captured via Eq. (21) and Eq. (22). To consider more than one potential in-depth analysis per process during the planning horizon, the D2P2 must be applied iteratively after each completed in-depth analysis. Eq. (21) ensures that the opportunity costs of an already scheduled process are zero for all periods after the in-depth analysis. Eq. (22) ensures that the opportunity costs of a distinct process equal the maximum absolute under- or over-performance $\Delta _ { i , t }$ in all periods up to the scheduled in-depth analysis period. Thereby, the parameter must be a sufficiently large number. Besides, the D2P2 ensures positive opport nity costs via Eq. (23).

$$
x _ {i, t} \in \{0; 1 \}, \quad \forall t \in T, \forall i \in I\tag{19}
$$

$$
\sum_ {t = 1} ^ {T} x _ {i, t} \leq 1, \quad \forall i \in I\tag{20}
$$

$$
o _ {i, t} \leq \left(1 - \sum_ {l = 1} ^ {t} x _ {i, l}\right) \cdot M, \quad \forall t \in T, \forall i \in I\tag{21}
$$

$$
\Delta_ {i, t} - o _ {i, t} \leq \left(\sum_ {l = 1} ^ {t} x _ {i, l}\right) \cdot M, \quad \forall t \in T, \forall i \in I\tag{22}
$$

$$
o _ {i, t} \geq 0, \quad \forall t \in T, \forall i \in I\tag{23}
$$

In Eq. (24), the D2P2 considers the maximum amount of in-depth analyses $c _ { t }$ that an organization can perform per period. Parameter $d _ { i }$ enables accounting for process-specific capacity consumption. We use $d _ { i } = 1$ as default. The value of $d _ { i }$ can be increased for complex and reduced for simple processes. It can be set by the management or based on log data, e.g., using the amount of execution paths as proxy. For our purposes, we assume that $d _ { i }$ is always smaller than the highest $c _ { t } .$ . Otherwise, it might be the case that some processes cannot be scheduled at all.

$$
\sum_ {i = 1} ^ {I} x _ {i, t} \cdot d _ {i} \leq c _ {t}, \quad \forall t \in T\tag{24}
$$

As it contains only linear constraints, our optimization problem is a MILP problem, which can be efficiently solved via the simplex algorithm [47,48]. On this foundation, the D2P2 returns a priority list that indicates in which planning periods the involved processes should undergo the next in-depth analysis, considering these processes’ predicted future performance and the opportunity costs of analyzing them too early or too late. Each in-depth analysis reveals whether the process’ aggregated performance difference actually violates a predefined threshold. If so, the process must be improved. Otherwise, the D2P2 should be re-applied based on updated performance data gathered during the in-depth analysis.

## 4 Evaluation

## 4.1 Evaluation strategy

To evaluate the D2P2, we followed Sonnenberg and vom Brocke’s [49] framework of evaluation activities in DSR, including four evaluation activities: EVAL1 to EVAL4. EVAL1 aims to justify the research problem and derive design objectives. We already completed this activity in the introduction and the theoretical background. EVAL2 strives for validated design specifications. To validate the (Section 4.2). EVAL3 strives for validated artefact instantiations. We thus implemented the D2P2 as a software prototype based on the numerical and statistical computing environment MATLAB (Section 4.3). EVAL4 requires validating an artefact’s usefulness and applicability in real-world case studies. To show the D2P2 in action, we applied our prototype to the 2012 BPI Challenge log, which captures an application process for a personal loan or overdraft, and compared the results to competing artefacts (Section 4.4). As there is currently no process log with data of multiple processes available, we chose a log containing events with a hierarchical structure. With the 2012 BPI Challenge log including three intertwined sub-processes, it could be preprocessed via hierarchical mining to derive a process network. Further, the 2012 BPI challenge log includes data suitable for inferring instance-level cash outflows and cash inflows in terms of loan repayments. Thus, this log was very appropriate to illustrate the D2P2’s key features. Our application corroborated that the D2P2 leads to interpretable results, helps solve problem instances of non-trivial complexity, and outperforms competing artefacts.

## 4.2 Feature comparison and competing artefacts analysis (EVAL2)

To validate whether the D2P2 answers the research question, we discuss its specification against the design objectives and competing artefacts. As competing artefacts, we selected approaches offering guidance on process prioritization. Although this sample may not include all extant approaches, we are confident that is does cover the most recent developments. Table 1 shows the results of our analysis. Below, we discuss the D2P2 against the PPR and the CPIM, as both approaches served as reference for designing the D2P2 and meet the design objectives best, except for the D2P2.

The D2P2 addresses both design objectives. It considers stochastic and structural dependencies (O.1) and prioritizes processes based on their actual and future performance (O.2). Compared to competing artefacts, the D2P2 is one of the few approaches that leverage log data to prioritize processes. Except for the D2P2, only the CPIM uses log data to prioritize processes based on future performance mance-related parameters or errorprone expert assessments. While the CPIM offers an analytical solution to determine when processes should undergo the next in-depth analysis, the D2P2 cannot deliver an analytical solution due to a common problem of integrating auto-correlation effects and dependencies [50]. The D2P2 uses numerical simulation instead, which enables covering structural and stochastic dependencies as well as predicting the periods in which processes should undergo the next in-depth analysis. Numerical simulation also enables capturing risky future process performance based on more realistic probability distributions than the normal distribution, which is a limitation of the CPIM. Longer computation times, which are unavoidable in simulation-based approaches, are uncritical from our perspective as process prioritization decisions need not be made in real time. As mentioned, the D2P2 accounts for structural and stochastic process dependencies. All other process prioritization approaches, except for the PPR but including the CPIM, share the individual process as unit of analysis, while neglecting process dependencies. In sum, the D2P2’s results are not only more reliable due to the usage of log data, but also structurally more complete and more detailed than those of competing artefacts. The D2P2 thus answers the research question and contributes to prescriptive knowledge on process prioritization.

## ACCEPTED MANUSCRIPT

Table 1 - Results of feature comparison and competing artefacts analysis

<table><tr><td></td><td>Characteristics of the D2P2</td><td>Darmani and Hanafizadeh [51]</td><td>Lehnert et al. [9] (PPR)</td><td>Levina and Hillmann [52]</td><td>Manderscheid et al. [21] (CPIM)</td><td>Ohlsson et al. [8]</td><td>Shrestha et al. [53]</td></tr><tr><td>Summary</td><td>Supports the prioritization of business processes for in-depth analysis based on log data. Predicts when the dependency-adjusted risky future process performance will violate predefined thresholds. Accounts for structural and stochastic process dependencies. Establishes a priority list.</td><td>Supports the selection of processes for redesign and offers best practice candidates for business process re-engineering. Aims to achieve lower risk and higher probability of success for portfolios containing several process improvement projects.</td><td>Considers process networks and structural dependencies to prioritize business processes. Ranks processes according to their network-adjusted need for improvement.</td><td>Supports the categorization of business processes by exploring business process models with metrics from social network analysis. Shows that process characteristics can be explored and analyzed using network theory and statistical methods.</td><td>Supports the determination of dynamic service intervals for business processes. Predicts after which number of instances a process should undergo an in-depth analysis.</td><td>Supports the categorization of business processes and the prioritization of improvement initiatives. Includes a process assessment heat map and a process categorization map as tools.</td><td>Supports the selection of IT service management processes. Balances business and IT service management objectives based on a selection matrix.</td></tr><tr><td>(O.1a)</td><td>Considers stochastic inter-process dependencies and intra-process dependencies.</td><td>Does not consider inter-process dependencies as independent processes are assumed. Intra-process dependencies are excluded also.</td><td>Partly considers stochastic inter-process dependencies via structural process dependencies. Does not consider stochastic intra-process dependencies.</td><td>Does not consider inter-process dependencies as independent processes are assumed. Intra-process dependencies are excluded also.</td><td>Does not consider inter-process dependencies as independent processes are assumed. Intra-process dependencies are excluded also.</td><td>Does not consider inter-process dependencies as independent processes are assumed. Intra-process dependencies are excluded also.</td><td>Does not consider inter-process dependencies as independent processes are assumed. Intra-process dependencies are excluded also.</td></tr><tr><td>(O.1b)</td><td>Considers structural dependencies in terms of use dependencies.</td><td>Does not consider structural dependencies.</td><td>Structural dependencies are considered in terms of use dependencies.</td><td>Does not consider structural dependencies.</td><td>Does not consider structural dependencies.</td><td>Does not consider structural dependencies.</td><td>Does not consider structural dependencies.</td></tr><tr><td>(O.2a)</td><td>Derives the interdependency-adjusted risky performance of each involved process in order to be able to treat each process as a stand-alone. Resolves process dependencies via multi-variate regression analysis of log data. Uses the process cash flow as an integrated performance measure.</td><td>Does not quantify process performance via performance indicators. Instead, 19 factors and 44 indicators determine the perceived degree of change in relation to organizational goals.</td><td>Measures process performance abstractly in terms of an integrated need for improvement index.</td><td>Does not consider process performance as a build time perspective is taken.</td><td>Derives the current risky process performance based on log data and process models. Uses the process cash flow as an integrated performance measure.</td><td>Assesses process performance qualitatively via color regimes. Covers five perspectives (positioning, relating, preparing, implementing, proving), which refer to de Bruin and Rosemann&#x27;s BPM capability framework [54].</td><td>Derives a perceived service gap based on the SERVQUAL model. Qualitatively rates business drivers in the context of IT service management.</td></tr><tr><td>(O.2b)</td><td>Estimates the future risky performance of each process via stochastic processes and Monte Carlo simulation. Measures future risky process performance via the aggregated difference from a predefined performance benchmark. Compares the future risky process performance with predefined performance thresholds. Schedules processes for in-depth analysis by optimizing opportunity costs.</td><td>Does not consider the risky future performance of processes.</td><td>Does not consider the risky future performance of processes.</td><td>Does not consider the risky future performance of processes.</td><td>Estimates the future risky process performance via stochastic processes. Measures future risky process performance via the aggregated difference from a predefined performance benchmark. Compares the future risky process performance with predefined performance thresholds.</td><td>Does not consider the risky future performance of processes.</td><td>Does not consider the risky future performance of processes.</td></tr></table>

## 4.3 Prototype construction (EVAL3)

To provide a proof of concept and enable real-world applications, we instantiated the D2P2’s specification as a software prototype. To decide which platform is most suited, we defined the availability of a simulation engine, an optimization engine with MILP-solving algorithms, and advanced statistical methods as mandatory requirements. The possibility of adding a lightweight graphic user interface (GUI) was an optional requirement. Eligible platforms were numerical and statistical computing environments, e.g., MATLAB and R, as well as general-purpose programming languages such as Java.

MATLAB offers a well-documented simulation module (Simulink), an optimization toolbox with MILP-solving algorithms, and advanced statistical methods such as distribution fitting. In MATLAB, integrating additional modules is fail-safe as modules are implemented on the same platform. Further, a handler enables creating GUIs. R also supports advanced statistical methods and offers optimization and simulation add-ons. Drawbacks are the missing graphical representation of simulations and the missing support for native GUI development. MATLAB and R suffer from limited programming capabilities due to a restrictive scripting language, a drawback tha the scalability and accessibility of software prototypes. The advantages of general-purpose languages are their scalability and accessibility due to the possibility of deploying software in a platform-independent manner. Further, simulation and optimization engines are available via application programming interfaces, which, however, can be error-prone [55]. Comparing advantages and drawbacks, we decided in favor of MATLAB.

To provide an overview of the prototype’s architecture, we modeled relevant layers, modules, and interactions as a sequence diagram (Figure 6). From a static perspective, the prototype has a threelayer architecture, containing an application, coordination, and presentation layer [56]. All modules that implement application logic belong to the application layer. To enable interactions among the application modules, the prototype implements a coordination layer containing a controller module, which also serves as interface between the presentation and the application layer. The presentation layer covers the GUI that receives user input and presents results. With this architecture, we decrease the number of point-to-point interactions. From a dynamic perspective, the prototype follows the steps of the D2P2. As determining the dependency-adjusted risky process performance in step 1 of the D2P2 requires case-specific preprocessing of log data (e.g., hierarchical mining, infrequent label elimination, multiple regression analyses), it is not part of the prototype.

![](/api/attachments/GS7SZSGX/fulltext/images/624c7d03ed73196d91d1bd26adafee6e9ae1d491b0fdfe6a57db1e377681bfb7.jpg)  
Figure 6 - Sequence diagram illustrating the architecture of our software prototype

The prediction of the future dependency-adjusted risky performance of each process according to step 2 of the D2P2 is implemented in the simulator module. We use Simulink to simulate the processes’ risky future performance over the planning horizon based on the probability distributions and autocorrelation effects determined in step 1 outside the software prototype. To account for structural and stochastic dependencies, we developed and used Simulink patterns. During the simulation, the controller calls the Simulink module via its run(seed) function, using a loop. The number of required iterations must be determined in line with the convergence behavior [57]. As a rule of thumb, 10,000 iterations are reasonable. In each iteration, the loop variable changes the seed, a parameter characterizing the distributions of pseudorandom numbers. This procedure ensures randomized, but reproducible results [58]. The simulation output is a matrix per process that contains the process cash flows of all iterations and planning periods. To analyze the simulation output, the controller calls the processor module via the fitDist function that calculates an empirical distribution function of the periodic process cash flows over all iterations. Using its calcUOP function, the processor then calculates the absolute under- and over-performance per process based on inverse distribution functions and according to the predefined performance thresholds and confidence intervals [59].

To prioritize the involved processes in step 3 of the D2P2 based on the predicted absolute under- and over-performance, we use MATLAB’s built-in optimization toolbox. In version R2014a, MATLAB introduced the MILP-solving function intlinprog [60]. Due to the standardized input parameters of this function, we created the optHelper module that transforms our MILP into the required structure. As shown in Figure 6, the controller calls the optimize(UOP) function, parameterized with the output of step 2, and returns a priority list and the opportunity costs of lost improvement potential to the processor module. Finally, the processor module uses its calcThresholdViolation function to calculate the period when the process with the highest priority violates one of its performance thresholds at a predefined confidence level. To visualize the prioritization results, the controller returns the priority list, the period of threshold violation, and the opportunity costs to the GUI.

## 4.4 Real-world example based on the 2012 BPI Challenge log (EVAL4)

## 4.4.1 Introducing the basic scenario

To show the D2P2 in action, we applied our software prototype to the 2012 BPI Challenge log [61]. Stemming from a Dutch Financial Institute, this log data captures an application process for a personal loan or overdraft. The basic logic of the process is as follows: First, the customer submits their application via a webpage. The application system and the bank zisor then perform data checks and complete the required information, calling the customer a required information is available. Eligible customers eventually receive an offer by mail ter further data processing activities, a final assessment is performed and the application is approved.

The 2012 BPI Challenge log contains 262,200 events and 13,087 cases, covering a timeframe from 1/10/2011 until 1/03/2012. Beyond data about tasks and their sequence, the log contains data about the requested amount of money, the processing time, and the responsible bank advisor. However, it lacks data about structural process dependencies and the performance of the executed process instances. We thus had to preprocess the log as follows: To improve the quality of the data included, we removed infrequent behavior and labels using ProM [62]. In order to be able to deal with structural process dependencies, we transformed the flat process model from the process log into a hierarchical process model via the automated discovery of abstractions with domain significance using ProM [63]. This step was necessary as the 2012 BPI Challenge log contains data referring to a single process only. Hierarchical mining helped derive a process network including structural process dependencies, which is necessary to apply the D2P2. Finally, we enriched the data with cash flow information by monetizing the execution times based on the average hourly rates of Dutch loan officers [64]. Regarding the cash inflows of successfully completed process instances, we assumed an average interest rate and credit period related to the amount of money requested by the customer. The preprocessing ensured that the D2P2 could be applied to real-world data However, the preprocessing of the 2012 BPI Challenge single-process log also caused some drawbacks, which we discuss in section 4.4.4.

![](/api/attachments/GS7SZSGX/fulltext/images/de6c165b085f00d31fb339a5bebc5891fd5797e973032237c4dc36cc770c680e.jpg)  
Figure 7 - Process network of the example (left) and its representation in Simulink (right)

The process network extracted from the 2012 BPI Challenge log consists of four processes (P1 to P4), whereas P1 has a use dependency with each other process and a self-directed edge, as shown in Figure 7 on the left. Figure 7 also indicates how often each use dependency is executed and how often P1 is executed stand-alone. In the example, only P1 has a self-directed edge as the processes P2 to P4 have been determined based on hierarchical mining. That is, they actually are “sub-processes” of the personal loan or overdraft application process and thus cannot be executed in a stand-alone manner.

According to step 1 of the D2P2, we also extracted the dependency-adjusted risky performance of each process, the stochastic arrival process that captures the random occurrence of process instances, the auto-correlation coefficients that represent stochastic intra-process dependencies, and the adjustment factors that capture structural process dependencies. All these input parameters could be determined based on the preprocessed log. The results are shown in Table 2. Regarding the other input parameters, we used the expected dependency-adjusted risky performance as performance benchmark for each process. In addition, we set the performance thresholds for the aggregated performance difference in line with the six sigma approach. That is, the lower performance boundary represents the expected aggregated performance difference minus six times the standard deviation of the respective process performance. The same logic holds true for the upper performance boundary. Based on the log data, the distribution of the cash flows that exclusively belong to the variant-specific parts of the process performance variants could be best approximated via individually parameterized normal distributions (e.g., for performance variant 11) or mixed Gaussian distributions (i.e., the sum of two individual parameterized normal distributions) (e.g., for performance variant 12). In our example, P1 has a stochastic arrival process that captures the risky number of process instances per period as processes P2 to P4 have been extracted via hierarchical mining. Thus, their risky amount of instances is determined by P1 and the related use dependencies. Beyond, we assumed that the bank’s process analysts can only analyze one process per period, which is feasible as only four processes are involved.

Table 2 – Process characteristics extracted from the preprocessed log

<table><tr><td>ID</td><td>Arrival process</td><td>Performance Thresholds</td><td>Performance Variant i → j</td><td>pi,j</td><td> $\widehat{CF}_{i,j,n_{ij}}^{vs,i}$ </td><td> $\beta_{i,j}^{vs,auto,j}$ </td><td> $\beta_{i,j}^{vs,j}$ </td></tr><tr><td rowspan="4">P1</td><td rowspan="4">Delaporte(34.25; 17.17; 2.99)</td><td rowspan="4">-633,083;633,083</td><td>1→1</td><td>0.23</td><td>Gaussian (-2.4;33.2)</td><td>0.27</td><td>-</td></tr><tr><td>1→2</td><td>0.20</td><td>0.5815 * Gaussian (2429.07, 2979.69) + 0.4185 * Gaussian (-1102.67, 1416.5)</td><td>0.07</td><td>1.18</td></tr><tr><td>1→3</td><td>0.01</td><td>0.6889 * Gaussian (604.349, 1304.75) + 0.3111 * Gaussian (-646.003, 1140.87)</td><td>0.11</td><td>1.64</td></tr><tr><td>1→4</td><td>0.56</td><td>0.5191* Gaussian (1297.35, 2440.71) + 0.4809 * Gaussian (-481.204, 1323.9)</td><td>0.04</td><td>1.45</td></tr><tr><td>P2</td><td>-</td><td>-100,020;100,020</td><td>2→2</td><td>1</td><td>0.6826* Gaussian (1128.76,1833.72) + 0.3174 * Gaussian (-10.219, 61.6708)</td><td>0.21</td><td>-</td></tr><tr><td>P3</td><td>-</td><td>-1,649;1,649</td><td>3→3</td><td>1</td><td>0.3111* Gaussian (2633.08,3112.43) + 0.6889 * Gaussian (-137.716, 419.119)</td><td>-0.05</td><td>-</td></tr><tr><td>P4</td><td>-</td><td>-308,250;308,250</td><td>4→4</td><td>1</td><td>0.5035* Gaussian (1753.7,2808.14) + 0.4965 * Gaussian (-25.5918, 219.433)</td><td>0.13</td><td>-</td></tr></table>

## 4.4.2 Creating the simulation models

As input for our prototype, which covers steps 2 and 3 of the D2P2, we used the developed Simulink patterns and built process-specific simulation models on their foundation. We connected the processspecific simulation models via an integrated super-model that reflects the entire process network (Fig-Simulink elements based on the process characteristics shown in Table 2.

![](/api/attachments/GS7SZSGX/fulltext/images/895bbaa8998e40b21a26c85ead9f470d08070c92d689b12b87c88d29b18858d7.jpg)  
Figure 8 - Extract of P1’s implementation in Simulink

The starting point of each process-specific simulation model is the stochastic arrival process that captures the uncertain occurrence of process instances (Figure 8 on the left). In order to cover various arrival processes, we rely on Delaporte distributions that can be parameterized individually. During the simulation, the arrival process generates entities. Each entity represents a process instance. After a new entity occurred, the simulation model draws a random instance-level process cash flow following the probability distribution of the respective dependency-adjusted risky process performance (Figure 8 on the left). In the next step, our simulation model caters for auto-correlation effects in the common core performance part as defined by the auto-correlation coefficients in Table 2. To do so, we implemented a separate block that builds a subsystem as shown in Figure 8 on the right. In this block, we first subtract a process-specific performance benchmark (here: the expected instance-level cash flow) from the common core performance. After that, we adjust the unexpected common core performance, adding the cash flow of the previous instance multiplied with the respective auto-correlation coefficient. After that, the simulation model deals with different performance variants. The simulation model uses variant probabilities to route entities into performance variants. Similar to the common core part, the simulation model adds variant-specific cash flows. To consider stochastic intra-process dependencies in the variant-specific performance, the simulation model contains a second autocorrelation block, which adds the variant-specific cash flow proportionally to the variant-specific autocorrelation coefficient.

After that, the simulation model resolves structural dependencies according to the discovered performance variants by shifting performance from using processes to used processes. This is done via new entities, representing instances of used processes and annotated with a flag indicating a use dependency. If a process instance uses an instance of another process, the simulation model increases subtract the increased part of the instance cash flow of instance from the cash flow of the using instance according to Eq. (6). All process-specific simulation models follow the same logic.

## 4.4.3 Conducting the simulation and interpreting the results

To prioritize the processes based on the D2P2, we conducted a Monte Carlo simulation with 10,000 iterations according to step 2 of the D2P2 and solved the optimization problem specified in step 3 of the D2P2. Even though running the simulation takes several hours depending on the available computing infrastructure, the fact that the software prototype could identify a feasible prioritization result corroborates that the D2P2 is applicable in real-world settings. As a result, the prototype returned a priority list that specifies in which period the involved processes should undergo an in-depth analysis. In addition, the prototype provided information about the accruing opportunity costs as well as more detailed timing information regarding the expected threshold violation of the process scheduled first.

Table 3 shows our results. In our example, the D2P2 schedules process P2 for period 1, process P1 for period 2, and process P3 for period 4. No processes are scheduled to the periods 3, 5, and 6. Moreover, process P4 is not scheduled at all. This priority list causes no opportunity costs, a circumstance that indicates that the D2P2 was able to schedule each process for that future period where it is anticipated to violate its predefined performance threshold without any resource conflicts. Looking at the process characteristics (Table 2) and the structure of the process network (Figure 7), it is reasonable to schedule P2 prior to P1, as P2 is the second most used process and therefore receives performance reallocations from P1. P3 is scheduled after P1 due to its low use frequency. The D2P2 does not schedule P4 as it never violates its thresholds, i.e. it never leads to opportunity costs, as shown in Table 4. The opportunity costs also explain the gap in period 3. As the D2P2 expects P3 to violate its performance threshold in period 4 for the first time, an earli in-depth analysis of P3 would unneces-

Table 3 – Results

<table><tr><td rowspan="2"></td><td colspan="6">Period</td><td rowspan="2">Total Opportunity Costs</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>D2P2</td><td>2</td><td>1</td><td></td><td>3</td><td></td><td></td><td>0</td></tr><tr><td>PPR</td><td>4</td><td>1</td><td>3</td><td>2</td><td></td><td></td><td>12,441</td></tr><tr><td>CPIM</td><td>2</td><td>1</td><td>3</td><td>4</td><td></td><td></td><td>0</td></tr></table>

Table 4 – Opportunity Costs

<table><tr><td> $\Delta_{i,t}$ </td><td> $t_1$ </td><td> $t_2$ </td><td> $t_3$ </td><td> $t_4$ </td><td> $t_5$ </td><td> $t_6$ </td></tr><tr><td>P1</td><td>0</td><td>4,186</td><td>3,1262</td><td>5,0331</td><td>68,283</td><td>69,265</td></tr><tr><td>P2</td><td>9,483</td><td>13,499</td><td>16,090</td><td>19,150</td><td>21,473</td><td>21,718</td></tr><tr><td>P3</td><td>0</td><td>0</td><td>0</td><td>4,819</td><td>42,324</td><td>46,827</td></tr><tr><td>P4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

## 4.4.4 Comparison against competing artefacts and discussion

In line with the feature comparison conducted in EVAL2, we also compared the D2P2 against competing artefacts, i.e., PPR [9] and CPIM [21], using the real-world case as a benchmark. First, we had to ensure that all approaches return comparable outputs. Whereas the CPIM could be directly executed on the preprocessed log, we had to derive a process-specific “need for improvement index” for the PPR, which captures how strongly a distinct process needs to be improved. To do so, we first defined

# ACCEPTED MANUSCRIPT

two-sided performance thresholds, which amounted to 1.5 times the standard deviation per instance inspired by the long-term six sigma shift [65]. To calculate the process-specific need for improvement indices, we counted the number of instances with threshold violations and related them to the total amount of instances per process. Moreover, we had to consider that the PPR and CPIM do not schedule processes to future planning periods, but return a process ranking or a critical process instance, respectively. As a further preparatory activity, we thus assumed for the PPR that the highest ranked process is analyzed in the first period followed by other processes in subsequent periods. As for the CPIM, we determined the in-depth analysis period for each process based on the critical instance in relation to the average use frequency. Further, we calculated the opportunity costs for all approaches.

As shown in Table 3, the PPR ranks process P4 with the highest priority (i.e., P4 should be analyzed in period 1), followed by P1, P3, and P2. As the PPR focuses on structural dependencies, it ranks the most-used process P4 first. Considering neither process performance nor historical process data, the PPR does not recognize that P4 is very unlikely to violate its predefined performance thresholds within the planning horizon. Consequently, the PPR yields inferior results compared to the D2P2. In terms of opportunity costs, the PPR causes 12,441 EUR.

The CPIM schedules the involved processes in the same order as the D2P2. This is reasonable as both the CPIM and the D2P2 build on past and predicted performance data, even though the CPIM does not cater for structural or stochastic dependencies. As shown in Figure 7 and Table 2, the process network used in this example is rather simple and the stochastic dependencies very weak. Thus, the D2P2 does not make use of its strength to cater for structural and stochastic process dependencies here. This, however, would be the case in a more complex example. Nevertheless, there is a difference in the priority list returned by both approaches. The D2P2 schedules no process for period 3 and never schedules P4 within in the planning horizon. While both approaches do not cause opportunity costs due to the violation of performance thresholds, the D2P2 is more economical regarding the capacity of the bank’s process analysts. In fact, analyzing a process in-depth involves costs as well.

In sum, the real-world evaluation confirmed that neglecting structural and/or stochastic dependencies results in the over- or underestimation of the processes’ future performance, a circumstance that biases process prioritization decisions and may waste the capacity of process analysts. However, we must keep in mind that the chosen example builds on a preprocessed process log that originally includes a single process. Thus, the process network used in this example, which was extracted via hierarchical process mining, may differ from more complex real-world cases in terms of the dependencies’ strengths. In our example, structural and stochastic dependencies were comparatively weak such that they do not severely influence the processes’ future performance. Nevertheless, the D2P2 outperformed the PPR and the CPIM as the most competing artefacts.

## 5 Conclusion

## 5.1 Summary and contribution

With effective process prioritization being a critical success factor for process improvement, we analyzed how processes can be prioritized by leveraging performance and dependency data from process logs. To answer this question, we developed and evaluated the D2P2, a process prioritization approach that uses dependency and performance data from logs to determine in which periods the processes from a process network should undergo the next in-depth analysis to check whether they actually require improvement. Drawing from and extending knowledge on dependency-aware process prioritization as well as dynamic scheduling of in-depth process analyses, the D2P2 predicts when the dependency-adjusted risky future performance of each involved process is likely to violate predefined performance thresholds. To do so, the D2P2 also leverages methods from outside the traditional BPM toolbox such as multi-variate data analysis, simulation, and optimization. We evaluated the D2P2 by discussing it against design objectives and competing artefacts. We also instantiated the D2P2 as a software prototype based on the numerical and statistical computing environment MATLAB. We finally applied the prototype to a real-world scenario based on the 2012 BPI Challenge log. This application corroborated that the D2P2 can be effectively applied and yields interpretable results. The comparison of the D2P2 with the competing artefacts showed that it yields superior results and that process prioritization decisions are in fact biased if process dependencies and risky future process performance are neglected. The D2P2 contributes to the prescriptive knowledge on process decision-making and process prioritization. As the D2P2 leverages performance and dependency data from process logs, it addresses two criticisms of extant prioritization approaches, i.e., the neglect of process dependencies and the dependence on potentially biased domain experts. In the case where a high-quality log is available, the D2P2 is easy to apply, and its output is both more reliable and detailed than that of competing artefacts.

## 5.2 Limitations and future research

While validating its design specification and applicability, we identified directions in which the D2P2 should be advanced. Below, we present these directions together with ideas for future research. Regarding its design specification, the D2P2 includes simplifying assumptions. As we account for structural process dependencies using linear regression, there may be a loss in quality in the case of nonlinear dependencies. The D2P2 also relies on Monte Carlo simulation to predict the risky future process performance. The results may slightly differ from exact approaches. Future research should focus on relaxing these assumptions. When extending the D2P2, however, one must keep in mind that models are purposeful abstractions that need not capture all the complexity of the real world. As the D2P2 is already quite complex, a circumstance that is justified from our perspective as the problem of process prioritization is complex as well, it is imperative to carefully deliberate whether a further increase in closeness to reality out-values the related increases in complexity and data collection. Finally, the D2P2 only determines in which periods processes should undergo the next in-depth analysis. Although this output is more detailed than that of other approaches, future research may extend the D2P2 such that it already anticipates effects of improvement projects, e.g., by applying methods related to dynamic optimization.

Regarding the D2P2’s applicability, we implemented a software prototype and applied it to a real-world scenario. As currently available process logs tend to contain performance data of single processes and lack dependency data, we had to preprocess the used 2012 BPI Challenge log via hierarchical mining and infrequent label elimination. This limitation, however, is not specific to the D2P2, but applies to all data-driven BPM approaches. We are aware that the D2P2 makes high demands on process logs. However, we are confident that, in line with the uptake of process mining, appropriate logs will be available in the near future. In the meanwhile, the BPM community should make an effort to compile publicly available process logs that encompass multiple processes. The price for more detailed prioritization results is that the D2P2 requires more input data (e.g., performance benchmarks and thresholds, capacity of process analysts, and planning horizon) and longer computation times than competing artefacts. Nevertheless, many input parameters can be derived from process logs or assessed without subjective bias. Longer computation times are uncritical from our perspective, as process prioritization decisions need not be made in real time. Future research should focus on further real-world evaluation in different contexts. More case studies will not only help gain experience in data collection and log preprocessing, but also help identify how the D2P2 must be tailored to fit multiple contexts. To facilitate real-world cases, we also recommend advancing the software prototype such that it can be used more conveniently and offers more sophisticated analysis functionality.

## References

[1] M. Dumas, M. La Rosa, J. Mendling, H.A. Reijers, Fundamentals of Business Process Management, Springer, Berlin, Heidelberg, 2013.

[2] M. Kohlbacher, H.A. Reijers, The effects of process‐oriented organizational design on firm performance, Business Process Management Journal 19 (2) (2013) 245–262.

[3] J. Recker, J. Mendling, The State of the Art of Business Process Management Research as Published in the BPM Conference, Business & Information Systems Engineering 58 (1) (2016) 55–72.

[4] R.J.B. Vanwersch, et al., A Critical Evaluation and Framework of Business Process Improvement Methods, Business & Information Systems Engineering 58 (1) (2016) 43–53.

[5] W.M.P. van der Aalst, Business Process Management: A Comprehensive Survey, ISRN Software Engineering 2013 (1) (2013) 1–37.

[6] P. Harmon, The State of Business Process Management, BP Trends (2016).

[7] S.S. Chakravorty, Where Process-Improvement Projects Go Wrong, Wall Street Journal - Eastern Edition 19 (255) (2010).

[8] J. Ohlsson, S. Han, P. Johannesson, F. Carpenhall, L. Rusu, Prioritizing business processes improvement initiatives: The Seco Tools case, in: CAiSE 2014 Proceedings.

[9] M. Lehnert, M. Röglinger, J. Seyfried, M. Siegert, ProcessPageRank - A Network-based Approach to Process Prioritization Decisions, in: ECIS 2015 Proceedings, Paper 118.

[10] W. Bandara, A. Guillemain, P. Coogans, Prioritizing Process Improvement: An Example from the Australian Financial Services Sector, in: J. Vom Brocke, M. Rosemann (Eds.), Handbook on Business Process Management 2, Springer, Berlin, Heidelberg, 2015, pp. 289–307.

[11] M. Leyer, D. Heckl, J. Moormann, Process Performance Measurement, in: J. Vom Brocke, M. Rosemann (Eds.), Handbook on Business Process Management 2, Springer, Berlin, Heidelberg, 2015, pp. 227–241.

[12] T.H. Davenport, Process innovation: Reengineering work through information technology, Harvard Business School Press, Boston, Massachusetts, 1993.

[13] M. Hammer, J. Champy, Reengineering the corporation: A manifesto for business revolution, Business Horizons 36 (5) (1993) 90–91.

[14] P. Hanafizadeh, E. Osouli, Process selection in re‐engineering by measuring degree of change, Business Process Management Journal 17 (2) (2011) 284–310.

[15] R. Dijkman, I. Vanderfeesten, H.A. Reijers, Business process architectures: Overview, comparison and framework, Enterprise Information Systems 10 (2) (2016) 129–158.

[16] M. Malinova, H. Leopold, J. Mendling, A Meta-Model for Process Map Design, in: CAiSE 2014 Proceedings, pp. 25–32.

[17] P. Letmathe, L. Petersen, M. Schweitzer, Capacity management under uncertainty with inter-process, intra-process and demand interdependencies in high-flexibility environments, OR Spectrum 35 (1) (2013) 191–219.

[18] W.M.P. van der Aalst, M. La Rosa, F.M. Santoro, Business Process Management, Business & Information Systems Engineering 58 (1) (2016) 1–6.

[19] W.M.P. van der Aalst, What’s the return on modeling, in: P. Harmon, R. Tregear (Eds.), Questioning BPM?: 109 answers by 33 authors to 15 questions about business process management, Meghan-Kiffer Press, Tampa, Florida, 2016, pp. 264–266.

[20] W.M.P. van der Aalst, et al., Process Mining Manifesto, in: Business Process Management Workshops, Springer, Berlin, 2012, pp. 169–194.

[21] J. Manderscheid, D. Reißner, M. Röglinger, Inspection Coming Due! How to Determine the Service Interval of Your Processes!, in: BPM 2015 Proceedings, pp. 19–34.

[22] S. Gregor, A.R. Hevner, Positioning and presenting design science research for maximum impact, MIS Quaterly 37 (2) (2013) 337–355.

[23] K. Peffers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A Design Science Research Methodology for Information Systems Research, Journal of Management Information Systems 24 (3) (2007) 45–77.

[24] R. Macedo de Morais, S. Kazan, S. Inês Dallavalle de Pádua, A. Lucirton Costa, An analysis of BPM lifecycles: From a literature review to a framework proposal, Business Process Management Journal 20 (3) (2014) 412–432.

[25] M. La Rosa, et al., APROMORE: An advanced process model repository, Expert Systems with Applications 38 (6) (2011) 7029–7040.

[26] T.W. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 (1) (1994) 87–119.

[27] D. Beverungen, Exploring the Interplay of the Design and Emergence of Business Processes as Organi zational Routines, Business & Information Systems Engineering 6 (4) (2014) 191–202.

[28] F. Martin, A performance technologist’s approach to process performance improvement, Performance Improvement 47 (2) (2008) 30–40.

[29] H.A. Reijers, S. Limam Mansar, Best practices in business process redesign: An overview and qualitative evaluation of successful redesign heuristics, Omega 33 (4) (2005) 283–306.

[30] S. Limam Mansar, H.A. Reijers, F. Ounnar, Development of a decision-making strategy to improve the efficiency of BPR, Expert Systems with Applications 36 (2, Part 2) (2009) 3248–3262.

[31] H.U. Buhl, M. Röglinger, S. Stöckl, K.S. Braunwarth, Value Orientation in Process Management, Business & Information Systems Engineering 3 (3) (2011) 163–172.

[32] J. Vom Brocke, C. Sonnenberg, Value-Orientation in Business Process Management, in: J. Vom Brocke, M. Rosemann (Eds.), Handbook on Business Process Management 2, Springer, Berlin, Heidel berg, 2015.

[33] M. Bolsinger, Bringing value-based business process management to the operational process level, Information Systems and e-Business Management 13 (2) (2015) 355–398.

[34] L. Wen, J. Wang, J. Sun, Detecting Implicit Dependencies Between Tasks from Event Logs, in: Asia-Pacific Web Conference 2006 Proceedings, pp. 591–603.

[35] W.M.P. van der Aalst, J.L. Zhao, H.J. Wang, Editorial: Business Process Intelligence: Connecting Data and Processes, ACM Transactions on Management Information Systems 5 (4) (2015) 1–7.

[36] S.-M.-R. Beheshti, B. Benatallah, S. Sakr, D. Grigori, H.R. Motahari-Nezhad, M.C. Barukh, A. Gater, S.H. Ryu, Process Analytics, Springer, Cham, 2016.

[37] A. Metzger, et al., Comparing and Combining Predictive Business Process Monitoring Techniques, IEEE Transactions on Systems, Man, and Cybernetics: Systems 45 (2) (2015) 276–290.

[38] M. Dumas, F.M. Maggi, Enabling Process Innovation via Deviance Mining and Predictive Monitoring, in: J. Vom Brocke, T. Schmiedel (Eds.), BPM - driving Innovation in a digital world, Springer, 2015, pp. 145–154.

[39] B. Kang, D. Kim, S.-H. Kang, Real-time business process monitoring method for prediction of abnormal termination using KNNI-based LOF prediction, Expert Systems with Applications 39 (5) (2012) 6061–6068.

[40] W.M.P. van der Aalst, M.H. Schonenberg, M. Song, Time prediction based on process mining, Information Systems 36 (2) (2011) 450–475.

[41] D. Freedman, Statistical models: Theory and practice, 1<sup>st</sup> ed., Cambridge Univ. Press, Cambridge, 2009.

[42] G. Kirchgässner, J. Wolters, U. Hassler, Introduction to modern time series analysis, 2<sup>nd</sup> ed., Springer, Berlin, New York, 2013.

[43] T. Rolski, H. Schmidli, V. Schmidt, J. Teugels, Stochastic processes for insurance and finance, J. Wiley, Chicester, New York, 2009.

[44] R.A. Rigby, D.M. Stasinopoulos, C. Akantziliotou, A framework for modelling overdispersed count data, including the Poisson-shifted generalized inverse Gaussian distribution, Computational Statistics & Data Analysis 53 (2) (2008) 381–393.

[45] G.H. Givens, J.A. Hoeting, Computational Statistics, John Wiley & Sons, Hoboken, 2012.

[46] V. Grover, S.R. Jeong, W.J. Kettinger, J.T. Teng, The Implementation of Business Process Reengineering, Journal of Management Information Systems 12 (1) (2015) 109–144.

[47] R. Burkard, M. Dell’Amico, S. Martello, Assignment Problems, Society for Industrial and Applied Mathematics, 2012.

[48] P. Le Bodic, G.L. Nemhauser, An Abstract Model for Branching and its Application to Mixed Integer Programming, 2015, available at http://arxiv.org/pdf/1511.01818.

[49] C. Sonnenberg, J. Vom Brocke, Evaluation Patterns for Design Science Research Artefacts, in: European Design Science 2012 Proceedings, pp. 71–83.

[50] D. Guégan, B.K. Hassani, Using a time series approach to correct serial correlation in operational risk capital calculation, The journal of operational risk 8 (3) (2013) 31–56.

[51] A. Darmani, P. Hanafizadeh, Business process portfolio selection in re-engineering projects, Business Process Management Journal 19 (6) (2013) 892–916.

[52] O. Levina, R. Hillmann, Network-Based Business Process Analysis, in: HICSS 2012 Proceedings, pp. 4356–4365.

[53] A. Shrestha, A. Cater-Steel, M. Toleman, W.-G. Tan, A Method to Select IT Service Management Processes for Improvement, Journal of Information Technology Theory and Application 15 (3) (2015).

[54] T. de Bruin, M. Rosemann, Using the Delphi Technique to Identify BPM Capability Areas, ACIS 2007 Proceedings.

[55] V.R. Basili, B.T. Perricone, Software errors and complexity: an empirical investigation0, Communications of the ACM 27 (1) (1984) 42–52.

[56] M. Fowler, Patterns of Enterprise Application Architecture, Addison-Wesley Professional, Boston, 2002.

[57] S.P. Brooks, A. Gelman, General Methods for Monitoring Convergence of Iterative Simulations, Journal of Computational and Graphical Statistics 7 (4) (1998) 434–455.

[58] J.E. Gentle, Random number generation and Monte Carlo methods, 2<sup>nd</sup> ed., Springer, New York, 2005.

[59] The MathWorks Inc., Statistics and Machine Learning Toolbox User’s Guide, available at http://de.mathworks.com/help/pdf\_doc/stats/stats.pdf (accessed on June 8, 2016).

[60] The MathWorks Inc., Optimization Toolbox User’s Guide, available at http://de.mathworks.com/help/pdf\_doc/optim/optim\_tb.pdf (accessed on June 8, 2016).

[61] B.F. van Dongen, BPI Challenge 2012, Eindhoven University of Technology, 2012.

[62] R. Conforti, M. La Rosa, A.H.M. ter Hofstede, Filtering out Infrequent Behavior from Business Process Event Logs, IEEE Transactions on Knowledge and Data Engineering (2016) 1.

[63] R.P.J.C. Bose, E.H.M.W. Verbeek, W.M.P. van der Aalst, Discovering Hierarchical Process Models Using ProM, in: W. van der Aalst, J. Mylopoulos, M. Rosemann, M.J. Shaw, C. Szyperski, S. Nurcan (Eds.), IS Olympics: Information Systems in a Diverse World, Springer, Berlin, Heidelberg, 2012, pp. 33–48.

[64] https://www.salaryexpert.com/salarysurveydata/state=oost-netherlands/job=consumer-loanofficer/salary (accessed on December 20, 2016).

[65] M.J. Harry, Six Sigma: a breakthrough strategy for profitability, Quality progress 31 (5) (1998) 60–64.

## Author Biographies

Wolfgang Kratsch studied Information Systems (B.A.) as well as Computer Science and Information Management (M.Sc.) at the University of Augsburg. Since Summer 2015, Wolfgang is a research fellow with the Research Center Finance & Information Management (FIM) in the area of business process management (BPM).

Jonas Manderscheid studied Business Informatics (B.A.) and Information Management (M.Sc.), while also serving as (in-house) IT Consultant at Hamm Reno Group GmbH. From 2012 to 2016, Jonas has been a research associate at the Research Center Finance & Information Management (FIM). Most of his work centers around business process management (BPM), focusing on the monitoring and improvement phases of the BPM lifecycle. During his studies, Jonas dealt with BPM in the fields of wholesale, retail, and e-commerce, in addition to electronic data exchange and data analysis. Jonas earned his PhD at the University of Augsburg. Currently, Jonas serves as Project Manager Internet of Things at Hilti Befestigungstechnik AG.

Daniel Reissner studied Information Systems (B.A.) and Information-oriented Business Administration (M.Sc.) at the University of Augsburg and Queensland University of Technology. From 2014 to 2016, Daniel has been a research fellow with the Research Center Finance & Information Management (FIM) in the area of business process management (BPM). Currently, Daniel is working as research fellow at the Queensland University of Technology.

Maximilian Roeglinger is a Professor of Information Systems at the University of Bayreuth. Maximilian serves as Deputy Academic Director of the Research Center Finance & Information Management (FIM), where he heads the business process management (BPM) group. Maximilian also works with the Project Group Business & Information Systems Engineering of the Fraunhofer FIT. Most of Maximilian’s work centers around BPM, customer relationship management, and digital transformation. He publishes in journals like Business & Information Systems Engineering, Business Process Management Journal, Decision Support Systems, Journal of the Association for Information Systems, and Journal of Strategic Information Systems. Maximilian is highly engaged in projects with companies such as Deutsche Bahn, Deutsche Bank, Hilti, Infineon Technologies, Radeberger, and Siemens. Maximilian earned his PhD at the University of Augsburg, and holds a Diploma in Business and Information Systems Engineering from the University of Bamberg.

## Highlights

\- Process prioritization based on process log data

\- Process prioritization based on structural and stochastic dependencies

\- Process prioritization based on predicted process perforance
