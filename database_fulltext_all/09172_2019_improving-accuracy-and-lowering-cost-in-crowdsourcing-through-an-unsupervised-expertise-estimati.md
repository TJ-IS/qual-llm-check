---
otero_id: 9172
otero_key: "55CERMNW"
title: "Improving accuracy and lowering cost in crowdsourcing through an unsupervised expertise estimation approach"
authors: "Alireza Moayedikia; William Yeoh; Kok-Leong Ong; Yee Ling Boo"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.05.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving accuracy and lowering cost in crowdsourcing through an unsupervised expertise estimation approach

![](/api/attachments/55CERMNW/fulltext/images/f72b7b5d0fe70217cf24bf431192254513b46839356b333ca96d535460492e1f.jpg)

Alireza Moayedikia<sup>a</sup>, William Yeoh<sup>b,⁎</sup>, Kok-Leong Ong<sup>c</sup>, Yee Ling Boo<sup>d</sup>

<sup>a</sup> School of Business Technology and Entrepreneurship, Faculty of Business and Law, Swinburne University of Technology, Australia

<sup>b</sup> Department of Information Systems and Business Analytics, Faculty of Business and Law, Deakin University, Australia

La Trobe Business School, La Trobe University, Australia

<sup>d</sup> School of Business IT and Logistics, College of Business, RMIT University, Australia

## A R T I C L E I N F O

Keywords: Crowdsourcing Unsupervised expertise estimation Harmony search Rough set

## A B S T R A C T

Crowdsourcing refers to distributing microtasks to an unknown group of online workers. Given that workers have varying expertise levels, a major research challenge for crowdsourcing is solving the problems of untargeted task assignment and unestimated aggregation of results. Although existing approaches can estimate the expertise of workers and use expertise information to allocate tasks, the efectiveness of these approaches is limited for the following reasons: 1) reliance on human intervention; 2) dependence on the type of answers; 3) non-sparseness; 4) post-expertise estimation. To overcome these limitations of crowdsourcing, this paper introduces an unsupervised approach to expertise estimation in microtask crowdsourcing that is independent of answer type, which is named ROUgh set based eXpertise estimation (ROUX). We consider the problem of expertise estimation as a metaheuristic optimization search problem, and integrate it with a rough set to better estimate the expertise of each online worker. Further. ROUX uses the expertise rating of workers for task as: signment to maximize the accuracy of the results and lower the cost. Extensive experimental evaluations using real-world datasets show that ROUX performs remarkably in accuracy improvement and cost eficacy.

## 1. Introduction

Crowdsourcing refers to a set of tools, approaches and concepts that are applied in a process of outsourcing work to a large and usually unknown group of online workers [1–3]. Internet developments have made it possible to create crowdsourcing platforms that use prior knowledge of online workers. Crowdsourcing does not restrict outsourcing and the use of crowd wisdom to a particular location, but ofers access to global talent pools, particularly to those in developing countries where salaries and operating costs are lower [4]. Figure Eight and Amazon Mechanical Turk (MTurk) are examples of crowdsourcing platforms that are used by various crowdsourcing organizations (e.g., Threadless, iStockphoto, and InnoCentive) [5].

Conventional microtask-crowdsourcing platforms apply a repeated labelling approach [6] to distribute tasks to online workers. On such platforms, workers choose tasks from the pool of tasks, solve the tasks, and submit the answers to the crowdsourcing platform [7,12]. For each task, there are many answers that must be aggregated to come up with the final aggregated answer using majority voting [8]. If the answers received for a task are not satisfactory, then the task will be repeatedly assigned to more workers [6].

However, the repeated-labelling solution applied to conventional microtask-crowdsourcing platforms has two major limitations: 1) it negatively afects job owners (also known as customers); 2) it demotivates the customer from using the platform thus afecting the success of the platform. The first limitation (i.e., the negative efect on job owners) results from assignments being untargeted, which refers to tasks being assigned repeatedly to workers, without considering the workers' expertise. An untargeted assignment increases the cost of microtask crowdsourcing because workers with insuficient expertise are asked to complete the tasks, but may not produce satisfactory results. The second limitation of repeated labelling (i.e., demotivates the customer from using the platform) is caused by unestimated aggregation. In repeated labelling, answers are collected from all workers and aggregated without estimating the workers' expertise. This means that the least reliable answers (often collected for non-experts) are also used in the aggregation process, which then harms the platform customer and thus the platform. These two principal limitations have motivated this research to consider solutions for estimating worker expertise.

Solutions for expertise estimation personalize task assignment and aggregate answers based on the expertise rating of workers. Examples of such solutions are expectation-maximization (EM) style computation [9–11] and the Troia approach [12]. Applying such solutions allows each worker to be described by an expertise rating [13] that is used to optimize task assignment to workers and answer collection from workers. Knowing the expertise rating of workers has two advantages. First, it allows selection of highly expert workers for tasks. Second, it allows application of the expertise rating in a weighted majority voting manner [8]. However, the existing algorithms for expertise estimation sufer from the following limitations:

• Reliance on human intervention in large crowdsourcing platforms is dificult because the number of tasks is numerous and heterogeneous [8], and the workers are diverse in their level of skills and knowledge [14–16]. For example, on the Figure Eight platform, human intervention prolongs the microtasking process. In addition, human intervention requires someone to examine each answer to a task and calculate its originality and relevance. If we assume a small job $\left( \mathbf { e . g . } \right.$ , labelling breast-cancer images) has 100 tasks distributed to 10 workers, reliance on human intervention requires examining 1000 answers. Considering the complexity and dificulty of the tasks and answers, examining 1000 answers might be labor intensive and might lead to questioning the value of crowdsourcing. If an expert can perform the job once and provide correct answers, then there is no need to leverage the wisdom of crowd.

Post-expertise estimation increases the cost of crowdsourcing and may also reduce the accuracy of the final aggregated answer. In this type of expertise estimation, the expertise is estimated when the answers are received. The GLAD algorithm proposed by Whitehill et al. [17] is an example of post-expertise estimation. Implementation of such an algorithm in a crowdsourcing platform such as Figure Eight (and unlike MTurk where payments are provided upon receiving satisfactory results) requires assignment of tasks to both genuine and non-genuine workers available on the platform. This afects the cost of crowdsourcing because payments are made to non-genuine workers as well as to genuine workers, which means the part of the budget that goes to the non-genuine workers is wasted. In addition, the quality of the final aggregated answer is afected because answers are collected from genuine and non-genuine workers.

• Non-sparsity assumption is applied by all the existing algorithms for expertise estimation, and refers to the assumption that all workers will complete all the assigned tasks [15–19]. For example, the hammer-spammer algorithm introduced by Karger et al. [20] as sumes that all workers provide answers to all tasks. However, in reality, some workers do not answer some of the assigned tasks, which means that such algorithms limit the utility of expertise estimation in real-world platforms.

Dependence on answer type limits the utility of an algorithm and makes platform maintenance dificult. An expertise-estimation al gorithm can be either applied to binary or multiple-choice problems. However, an algorithm that works well on a binary problem may not work well for multiple-choice problems [21]. On a microtask crowdsourcing platform, customers might distribute various types of tasks with answers in the format of free text, multiple choice, or binary choice. The dependence of algorithms on answer type also makes a platform's maintenance dificult because the company needs to adjust the expertise-estimation algorithm in accordance with the answer type.

To tackle these limitations and make expertise-estimation approaches more applicable to real-world problems, this paper makes the first attempt to introduce an unsupervised approach to expertise estimation in microtask crowdsourcing through the proposed ROUgh set based eXpertise estimation (ROUX). Section 1.1 below outlines the problem formulation, followed by an overview of ROUX solution in Section 1.2.

## 1.1. Problem formulation

A typical microtasking platform has a set of tasks $T = \{ t _ { 1 } , t _ { 2 } , t _ { 3 } , \dots , t _ { i } \}$ in which each task has a specific type $Q = \{ q _ { 1 } , q _ { 2 } , q _ { 3 } , \ldots , q _ { i } \} _ { }$ , along with an unknown ground truth $G = \{ g _ { 1 } , g _ { 2 } , g _ { 3 } , \ldots , g _ { T } { } ^ { Q } \}$ These tasks are assigned to workers $W = \{ w _ { 1 } , w _ { 2 } , w _ { 3 } , \dots , w _ { w } \}$ that are each associated with an unknown expertise level $E = \{ e _ { 1 } , e _ { 2 } , e _ { 3 } , \ldots , e _ { i } \}$ . Every worker provides an answer to each assigned task shown as a worker–task matrix $M _ { W \times I } = \{ { m _ { 1 } } ^ { 1 } , { m _ { 1 } } ^ { 2 } , { m _ { 1 } } ^ { 3 } , \dots , { m _ { W } } ^ { I } \}$ , where entry $m _ { W } ^ { ~ I }$ refers to the answer provided by the wth worker to the ith task. In ROUX's formulation, E and G are latent variables and the purpose is to find suitable values for these.

## 1.2. Solution overview

To estimate the latent variables, ROUX relies on its ofline and on line stages. In the ofline stage, ROUX receives a matrix of worker tasks in which each row is a worker and each column is a task, with each entry being the answer provided by a worker for a task. ROUX generates diferent combinations of workers and uses rough sets to estimate the expertise of each combination, and the expertise of every worker inside each combination. Given that each worker can be a part of different groups, ROUX formulates the search of the proper grouping of workers as an optimization process using harmony search, which was proposed by Geem et al. [22]. The purpose of this optimization is to find the best combination (the one that maximises the expertise rate).

For each worker, the combination in which the worker shows the highest expertise is selected. The worker is then excluded from that combination and a rough set is used to estimate the expertise of that combination. The diference in expertise rates between pre-worker ex clusion and post-worker exclusion is the actual rate of expertise of the worker. ROUX applies the ofline stage to every task with diferent formats (e.g., transcription, image labelling, etc), and preserves a database of worker tasks.

In the online stage, ROUX recognizes the type of task, then retrieves the experts for that task type. To identify the final aggregated answer of a new task, ROUX in online stage, selects the top experts for tasks with type Q and applies majority voting on the answers collected from these experts.

## 2. Related work

Considerable research on expert estimation has been conducted in the field of microtask crowdsourcing [2]. A review of expertise-estimation research is summarized in Table 1.

The approach proposed by Khattak and Salleb-Aouissi [14] named “Expert Label Injected Crowd Estimation” (ELICE), requires human intervention. This approach first injects several expert-generated pairs of task answers, where the answers of the task are unknown to workers but known to the algorithm. ELICE then compares the answers collected from workers against the answers generated by the experts, and then identifies the expertise level of every worker based on how diferent their answers are from the answers of experts.

The Dual Task Assigner (DTA) expertise-estimation approach, proposed by Ho and Vaughan [15], relies on linear programing to determine the skill level of workers and the task weight. DTA asks workers about their skills and competency level in those skills. This information can be used to estimate the quality of the results produced by the workers. Similarly, another approach proposed by Ho et al. [16] relies on linear programing to optimally estimate variables of worker expertise and task dificulty. In these two approaches, human intervention is required to identify the expertise of workers during the assignment of tasks.

Table 1  
Research estimating expertise of crowdsourcing workers.

<table><tr><td>Author</td><td>Main objective</td><td>Approach</td></tr><tr><td>Khattak and Salleb-Aouissi [14]</td><td>Aggregation of answers based on crowd&#x27;s expertise</td><td>Human intervention</td></tr><tr><td>Ho and Vaughan [15]</td><td>Task assignment based on workers&#x27; expertise</td><td>Human intervention and linear programming</td></tr><tr><td>Ertekin et al. [21]</td><td>Weighted voting to estimate crowd&#x27;s opinion</td><td>Probabilistic</td></tr><tr><td>Amirkhani and Rahmati [23]</td><td>Answer aggregation based on crowd&#x27;s opinion</td><td>Probabilistic</td></tr><tr><td>Long et al. [24]</td><td>Selecting proper tasks and workers</td><td>Expectation maximization</td></tr><tr><td>Welinder and Perona [25]</td><td>Expertise estimation</td><td>Expectation maximization</td></tr><tr><td>Whitehill et al. [17]</td><td>Expertise estimation</td><td>Probabilistic</td></tr></table>

Ertekin et al. [21] put forward an approach called “CrowdSense”, which works on binary types of answers (e.g., 1 or −1). In CrowdSense, tasks come one at a time and the algorithm dynamically samples subsets of the crowd based on an exploration/exploitation criterion. Crowd-Sense generates a weighted combination of the subset's votes that approximate the crowd's opinion. However, CrowdSense cannot be applied to multiple choice or text answers.

Amirkhani and Rahmati [23] suggested the Agreement/Disagreement (AD) approach to expertise estimation. Unlike EM style computations that iteratively attempt to estimate two unknown variables of worker expertise and the gold standard, AD first estimates the expertise of workers as the analytical probabilities of conflicts among workers, and then calculates the final aggregated answer based on the estimated expertise.

Long et al. [24] recommended an approach that applies EM to visual recognition tasks. The proposed algorithm explicitly models both the overall noise in answers and the expertise level of each worker. The probabilistic nature of the model allows the adoption of the prediction entropy for active selection of tasks to be answered, and active selection of high-quality workers based on their estimated expertise.

Welinder and Perona's [25] proposed approach is able to measure the expertise of workers dealing with image labelling. The expertise of workers is estimated by a scalar vector. The computation of expertise is achieved through an EM style computation. In the E step, the worker parameters are estimated and a posterior probability on the target value is computed. In the M step, the parameters of workers are estimated. A probabilistic framework for measuring worker expertise for imagery tasks was proposed by Whitehill et al. [17]. The proposed probabilistic model uses inference methods to infer simultaneously the expertise of each labeller, the dificulty of each image, and the most probable label for each image. According to Karger et al. [26] and Tarasov et al. [27], an EM approach is heuristic and without any rigorous guarantees of correctness or overall performance.

Overall, the current state-of-the-art approaches mainly adopt supervised or semi-supervised approaches to estimating the expertise of workers, and these approaches function only with one type of answer (e.g., binary, multiple choice or text). To address these limitations, this paper proposes an unsupervised expertise-estimation approach named “ROUX”. ROUX uses harmony search as a metaheuristic formulation, which not only improves the performance of answer aggregation and eliminates reliance on human intervention, but also is independent of answer type.

## 3. ROUgh set based eXpertise estimation (ROUX) approach

The objective of ROUX is to estimate the expertise of workers in microtask crowdsourcing to improve task allocation in such crowdsourcing. ROUX begins by executing the following three steps as part of the ofline stage: Step 1: worker sampling; Step 2: best-expertise selection; and Step 3: single-worker expertise estimation. These steps are explained in detail in Section 3.1.

## 3.1. Step 1: worker sampling: stepwise process

In a pool of workers, some have higher levels of expertise than others. Thus, expertise level can be defined as the level of knowledge a worker has compared with other workers in a pool, and can be estimated by calculating the level of expertise of a worker in diferent groups. To do this, the group for which a worker shows the highest expertise must be found. The possible combinations of workers can be computed as follows:

$$
S = 2 ^ {| W |} - W - 1\tag{1}
$$

where |W| is the number of workers. If we assume that on a crowdsourcing platform $\vert \mathbf { W } \vert = 1 0 0 0$ , then we need to investigate approximately $1 . 0 7 2 \times 1 0 ^ { 3 0 1 }$ possible samples in a greedy manner for each worker, and identify the sample in which a worker has the highest level of expertise in relation to the other workers in that sample. This consumes a great deal of time and resources. Thus, in Step 1, we use an optimization formulation to estimate the expertise of each sample of workers. As noted by Diao and Shen [28] and Moayedikia et al. [29], the simplicity of harmony search allows the overall complexity of the search process to be reduced. Therefore, in Step 1 we utilize harmony search as an optimization solution.

Step 1 begins by initializing the dynamic parameters of harmony memory size (HMS), harmony memory consideration rate (HMCR), minimum pitch-adjustment rates (PARmin), maximum pitch-adjustment rates (PARmax) along with a dynamic entity named “harmony memory” (HM). ROUX initializes the parameters empirically, and initializes the HM by randomly inserting workers into diferent groups in a binary format as: 1, 1, 0, 1, 0, 1, 1, where each digit corresponds to a worker and where 1 means inclusion and 0 means exclusion. After initialization, harmony search generates new harmony vectors (NHVs), where each NHV is a new combination of workers. An NHV is a binary vector with length equal to the number of workers. For each component, a random number is first generated $R _ { H M C R } { \sim } ( 0 , 1 )$ , and is then compared against the HMCR value.

If R is larger, then a row will be selected randomly from HM and its corresponding component will be copied to the current component of NHV. Otherwise, the current component is filled randomly by choosing either 1 or 0. To verify whether the generated NHV is acceptable, its fitness is measured via rough-set theory (explained in Section 3.2).

Frequent selections from HM (i.e., when $H M C R \mathrm { ~ < ~ } R _ { H M C R } )$ may result in having an NHV with a very high level of similarity to the vectors already in HM. This prevents the algorithm from exploring further possible solutions. To avoid this, harmony search applies the pitch-adjustment operation to only the components filled from HM. ROUX first generates a random number as $R _ { P A R } { \sim } ( 0 , 1 )$ , and if the number is larger than the number produced by $\operatorname { E q . } \ ( 2 ) ;$ , the pitch-adjustment operation flips the value in a component, provided that this flipping improves the fitness of NHV. Pitch adjustment is formulated as:

$$
P A R (t) = \frac {t}{N I} \times (P A R _ {m a x} - P A R _ {m i n})\tag{2}
$$

where $P A R _ { m a x }$ and $P A R _ { m i n }$ are the maximum and minimum values of PAR, t is the current iteration number, and NI is the total number of iterations. Fitness of an NHV is referred to as $F _ { N H V } .$ The newly generated NHV will replace the worst vector in HM, $F _ { w o r s t } \mathrm { { i f } } \ F _ { N H V } > \ F _ { w o r s t } .$ ROUX performs initialization once, and improvisation NI times.

The output of Step 1 is the tuned HM with HMS vectors. Step 1 generates the set of workers with the highest possible expertise compared with the other workers. However, the purpose is to find the level of expertise of every single worker for each task type. To estimate the expertise of every worker, Step 2 takes HM as the input, and identifies for each worker the vector in which a worker has the highest level of expertise. For example, if w1 is a member of several samples of S2, S6 and S7 with fitness (i.e., overall expertise) of 0.96, 0.991, and 0.9, respectively, then the sample w belongs to is S6. The output of Step 2 is a mapping vector A with length $| \mathbf { W } | , A = \mathbf { \Psi } < ( w _ { 1 } , s _ { 1 } ) , ( w _ { 2 } , s _ { 2 } ) , ( w _ { 3 } , s _ { 3 } ) , \dots$ $( w _ { W } , s _ { H M S } ) >$ , where each component of this vector indicates the assignment of a worker $w _ { W }$ to a sample s .

Step 3 is where the expertise of each worker is assessed. This step receives the mapping vector and estimates the expertise of every in dividual worker w. As stated. a worker can be a member of more than one combination. To estimate the expertise of a worker who belongs to more than one combination, the worker is first removed from the best sample set $\textstyle S _ { e } .$ The removed worker is referred to as as $w _ { r } .$ Then using Eq. (11) (see Section 3.2), the value of k is calculated. Thus, for the set $\scriptstyle { S _ { e } , }$ there are two expertise values: one for pre-removal and one for postremoval. The change in expertise value of the set $\boldsymbol { S _ { e } } ,$ shown as $D _ { r } ,$ is the estimated expertise of worker w . A formulation of this is shown in Eq. (12) (see Section 3.2). The higher the change, the higher the level of expertise of the worker. To better understand how rough sets are used in ROUX, Section 3.2 explains the application of rough-set theory in ROUX.

## 3.2. Estimating rough-set-based expertise

The key component of ROUX is the use of rough sets. According to Jensen and Shen [30], a rough set provides a filter-based tool by which knowledge can be extracted concisely from a domain, retaining the information content while reducing the amount of knowledge involved [32]. Rough-set theory is parameter free, in that it requires no parameters to operate other than the supplied data, only the granularity structure of the data is used.

ROUX uses rough sets to identify the most expert worker(s) for the newly arrived task(s). Let $I { \in } ( T , W )$ , where T is a non-empty and finite set of tasks and W is a non-empty finite set of workers. For each worker, $w \in W ,$ there is an assigned task, $t \in T ,$ and the worker provides an answer, $V _ { w } ,$ for that task. If we consider W the set of all workers, then ∀P ⊂ W there is an associated equivalence relation IND(P), as shown in Eq. (3).

$$
I N D (P) = \{(x, y) \in T ^ {2} | \forall w \in P, w (x) = w (y) \}\tag{3}
$$

The partition of T generated by IND(P) is denoted as T = IND(P) (or in simpler terms $\mathrm { T } = \mathrm { P } )$ , which is determined as in Eqs. (4) and (5)

$$
T / I N D (P) = \bigotimes \{T / I N D (w) \mid w \in P \}\tag{4}
$$

where the operator ⨂ is defined as in Eq. (5) for sets A and B.

$$
A \textcircled {\times} B = \{X \cap B \mid X \in A, Y \in B, X \cap Y \neq 0 \}\tag{5}
$$

If (x,y) ∈ IND(P), then x and y are the most suitable tasks for the workers from P. Let $X \subseteq T .$ X can be approximated using only the information contained within P by constructing the P-lower and P-upper approximations of X formulated in Eqs. (7) and (6).

$$
\left. \begin{array}{l} P X = \{x \in T | [ x ] _ {p} \subseteq X \\ - \end{array} \right\}\tag{6}
$$

$$
\overline {{P}} X = \{x \in T | [ x ] _ {p} \neq X \}\tag{7}
$$

where $[ x ] _ { p }$ is the equivalence class of the set P. The tuple < ${ \overline { { P } } } X$ , PX > is called a rough set. Let P and Q be sets of workers inducing equivalence relations over T, then the positive, negative, and boundary regions can be defined as in Eqs. (8) to (10):

$$
P O S _ {P} (Q) = \bigcup_ {X \in T / Q} P X\tag{8}
$$

$$
N E G _ {P} (Q) = T - \bigcup_ {X \in T / Q} \overline {{P}} X\tag{9}
$$

$$
B N D _ {P} (Q) = \bigcup_ {X \in T / Q} \overline {{P}} X - \bigcup_ {X \in T / Q} P X\tag{10}
$$

where Q is the task type (e.g., classification, annotation, tagging) of the previously solved tasks in the repository. The positive region, POS (Q), contains all the tasks that can be truly solved by the workers in the subset P. The boundary region, $B N D _ { P } ( Q )$ is the set of tasks that can possibly but not certainly be solved by the workers in set P. The negative region, $N E G _ { P } ( Q )$ , is the set of tasks that cannot be solved by the set P. Thus, the positive region can be used in Eq. (11) to measure the expertise of workers:

$$
k = \gamma_ {p} (Q) = \frac {| P O S _ {P} (Q) |}{| T |}\tag{11}
$$

If k = 1, then the workers in P are the best combination of workers and are highly expert; i $\mathbf { \Phi } _ { 0 } < \mathbf { k } < \mathbf { \Phi } _ { 1 }$ , the workers in P are partially (in a degree k) expert; and if k = 0 the workers in P are not expert. To measure the level of expertise of an individual worker, the following equation can be used:

$$
\varepsilon_ {p} (Q, w) = \gamma_ {p} (Q) - \gamma_ {p - \{w _ {r} \}} (Q)\tag{12}
$$

where $\varepsilon _ { p } ( Q , w )$ is the expertise of worker w on tasks with type Q. The output of the ofline stage is the expertise value of every worker for a given task type. During the online stage, the workers with the highest level of expertise are queried once a new task arrives, and majority voting is used to aggregate the answers collected from experts. Algorithm 1 below provides an overview of ROUX algorithm.

Algorithm 1. Expertise estimation in ROUX.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:
w: set of workers
$l_{w}^{t}$: worker-task matrix
NI: number of generations
HMCR: harmony memory consideration rate
PAR: maximum and minimum values of pitch-adjustment rate
HMS: harmony memory size
Output: e: expertise of workers

Algorithm:

Initialize()
for $t \leftarrow 1$ to $NI$ $R_{f} \leftarrow$ A randomly generated number;
    if $R_{f} &gt; HMCR$ then
    Randomly select vector $V_{r}$ from HM
    $NHV[f] \leftarrow V_{r}[f]$ $R_{p} \leftarrow$ A randomly generated number;
    $P_{f} \leftarrow PAR(t)$
    if $P_{f} &lt; R_{p}$ $NHV[f] \leftarrow \overline{NHV[f]}$
    end if
    else
    $\phi \leftarrow$ Random number;
    if $\phi &gt; 0.5$ then
    $NHV[f] \leftarrow 1$
    else
    $NHV[f] \leftarrow 0$
    end if
    $k_{NHV} =$ rough set (NHV)
    $k_{worst} \leftarrow HM_{worst}$
    if $k_{NHV} &gt; k_{worst}$ then
    $HM = HM - \{worst\} \cup \{NHV\}$
    end if
end for

for h $\leftarrow 1$ to HMS
    for w $\leftarrow 1$ to W
    $HM_{best(w)} \leftarrow$ fetch the best combination for w from HM
    $HM_{best(w)}^{-w} \leftarrow$ remove w from $HM_{best(w)}$ $k_{best(w)}^{-w} \leftarrow$ using Equation (11), estimate the expertise of $HM_{best(w)}^{-w}$ $e_{w} = HM_{best(w)} - k_{best(w)}^{-w}$
    end for
end for
</div>

## 4. Experimental evaluation

This section evaluates the practical aspects of ROUX and examines its performance in realistic settings. We compare the performance of ROUX against state-of-the-art approaches of expertise estimation (i.e., Raykar [11], Gaussian expertise estimation [10], ELICE [14] and GLAD [17]). Real-world datasets enable us to provide a realistic environment for testing the eficacy of the proposed ROUX approach. The ROUX source code is available at: shorturl.at/alNQ4.

## 4.1. Experimental design

To test the performance of ROUX in a realistic setting, this research uses accuracy, area under curve (AUC), and cost through the following procedure. In ROUX and in other approaches to expertise estimation, the expertise of workers is estimated, and then candidate experts are selected based on a pre-specified threshold, and finally, tasks are as signed to the set of candidate experts. By applying majority voting to the answers collected from experts, the final answer to every task is determined. Accuracy is the ratio of ground truth specified correctly.

The five real-world benchmark datasets are presented in Table 2. The selected datasets are highly sparse to evaluate the eficacy of ROUX in dealing with highly sparse datasets. Using a hold-out strategy, we divide each dataset into two disjointed sets: testing (30%) and training (70%). The parameters of the state-of-the-art approaches discussed above are set based on their reference paper, while the parameters of ROUX are set experimentally as $H M C R = 0 . 5 2 , \quad \mathrm { N I } = 2 0 0 ,$ HMS = number of tasks in a dataset, $P A R _ { m i n } = 0 . 2 5 , P A R _ { m a x } = 0 . 6 5 .$ Experiments are conducted in five separate runs, where each run has 100 iterations. The final results are averaged over 500 iterations. Further, to prove that the obtained results are statistically significant, and the null hypotheses is rejected, the Wilcoxon Ranksum, and Signrank statistical tests are performed.

## 4.2. Results

## 4.2.1. Performance measurement

This section presents the results achieved by ROUX and the rival approaches. Fig. 1 presents the accuracy results, where the X-axis represents the minimum expertise threshold and the Y-axis represents the accuracy value. ROUX outperforms the state-of-the-art approaches in accuracy across all the five datasets (RTE, TEMP, SQUARE-Duchenne, Google, and TREC). Similarly, as presented in Fig. 2, for AUC, ROUX outperforms the existing approaches in four of the datasets, while showing comparable performance to the TREC dataset. The perfor mance of ROUX with TREC dataset using the AUC measure may not be as remarkable as it is with the other datasets, but this performance can be enhanced by increasing the number of iterations of the harmony search component.

Table 2  
List of datasets used for experiments.

<table><tr><td>Datasets</td><td>Workers (No.)</td><td>Tasks (No.)</td><td>Tasks nature</td><td>Ground truth samples</td></tr><tr><td>SQUARE-RTE [31]</td><td>164</td><td>800</td><td>Binary choice</td><td>[0; 1]</td></tr><tr><td>SQUARE-TEMP [31]</td><td>76</td><td>462</td><td></td><td></td></tr><tr><td>SQUARE-Duchenne [17]</td><td>17</td><td>159</td><td></td><td></td></tr><tr><td>Google</td><td>57</td><td>576</td><td>Multiple choice</td><td>[-1; 0; 1]</td></tr><tr><td>TREC</td><td>137</td><td>46</td><td></td><td>[-2; -1; 0; 1; 2]</td></tr></table>

![](/api/attachments/55CERMNW/fulltext/images/c19732d9308b68d31f5e9ce23a400152aa05a0370daaf1af072a9ea3206029c4.jpg)

![](/api/attachments/55CERMNW/fulltext/images/1421bd30f064f3e65a265b4601e46901fb584426760a2e10e6d7302af38362ce.jpg)

![](/api/attachments/55CERMNW/fulltext/images/0f8bb2e18e4a72e3d7e7c21bc377982f7a1080f8904dbcd9ed26dfddc0072bc1.jpg)

![](/api/attachments/55CERMNW/fulltext/images/a32129836f5051df62ef1624962e1bafc659288f3ff9942445ca909be1b8258b.jpg)

![](/api/attachments/55CERMNW/fulltext/images/c75e77fd7fb53c73a2fa323431b01a8d9a8533e72942f6bc4731b9f645246d28.jpg)  
Fig. 1. Performance of ROUX for accuracy compared with prior state-of-the-art approaches.

On the other hand, the existing approach ELICE uses a task-injection technique to estimate the expertise rating of workers in a task; however, the injected tasks may not always be accurate in predicting the expertise of workers because different tasks have different levels of dificulties. Thus, ELICE is inferior to ROUX due to its reliance on injected tasks. Other approaches GLAD and Raykar rely on the EM style computations. As noted by Tarasov [27] and Raykar [11], EM style computations are heuristic approaches with no guarantee of correctness, and also it is impossible to predict whether an EM algorithm can achieve an optimal solution. Although slightly behind Gaussian in some rare cases, ROUX still outperforms or is competitive to the Gaussian approach. As mentioned by Groot et al. [10], Gaussian provides a rich and well-established alternative to parametric models. In this research, ROUX applies harmony search and rough set to estimate the expertise.

![](/api/attachments/55CERMNW/fulltext/images/5f84ddbc46f5d01226dc91d096d08ba5e704ae7bab69a9e65e242066f7f1bb8b.jpg)

![](/api/attachments/55CERMNW/fulltext/images/64f2d96a63925f343692930413078065ea98d0faa49f341eff2a061adf54b992.jpg)

![](/api/attachments/55CERMNW/fulltext/images/df2cdf75005e57cab6d508f0d12267e0e4efbb1f6a3d0bee862bff35107d6ea8.jpg)

![](/api/attachments/55CERMNW/fulltext/images/05428a0aaa63b1f3c1e2d08fa7f6ccd300c6b964d26198312d0d3b01ca30c6a3.jpg)

![](/api/attachments/55CERMNW/fulltext/images/21c6e600ed950353aa557c9a15b37a14a1b881c059de9338275885ef1314d581.jpg)  
Fig. 2. Performance of ROUX for AUC compared with prior state-of-the-art approaches.

Rough set is parameter free, but the harmony search requires tuning of some parameters, hence this explains why the performance difers.

The significant performance of ROUX lies in its integration of me taheuristic search optimization and rough sets. Specifically, ROUX benefits from harmony search as a metaheuristic search technique for reducing the complexity of the search process [28,29]. Harmony search also formulates the process as an optimization solution that helps find the optimal combination of workers. A rough set provides a filter-based tool that allows extraction of concise knowledge from a domain [30]. This concise knowledge allows recognition of the appropriate worker(s) for a given task. In addition, the obtained results presented in Figs. 1 and 2 are in line with the findings of Ravkar [11] and Tarasoy et al. [27] that in a binary task problem, EM style computations should be avoided because non-EM algorithms work better in this context.

## 4.2.2. Wilcoxon statistical test

The practical utility of ROUX lies in its performance with unseen data. To evaluate the performance with unseen data, we conduct the Wilcoxon signed-rank test and the Ranksum test, which according to Demšar [32], is a more sensible measure than a t-test because the Wilcoxon signed-rank test assumes commensurability of diferences. The Wilcoxon signed-rank test is also considered safer because it does not assume normal distributions, and the outliers have less efect on the final result. The purpose of the Wilcoxon signed-rank is to show if the results from the two approaches are independent, thereby rejecting the null hypothesis. The test results are presented in Table 3 in the form of h (p), where h refers to the test value and p indicates whether the null hypothesis is rejected (i.e., p = 1). The results reported in Table 3 reject the null hypothesis between ROUX and all other approaches in the measures of accuracy and AUC. Thus, ROUX's performance is considered significant.

## 4.2.3. Cost eficacy analysis

The principal goal of ROUX is to increase the accuracy of the final aggregated answer estimation while reducing the cost of microtasking by assigning tasks to expert workers. Thus, assessing expertise estimation without analyzing the involved cost is not sensible. This section analyzes the cost eficacy of ROUX, and compares it against the prior state-of-the-art approaches based on the following assumptions:

• payments to all workers are the same regardless of their expertise level

payment for each task (regardless of its dificulty) is the same

• job owners pay extra for task quality to ensure the results are reli able.

Wilcoxon test comparisons.

<table><tr><td rowspan="2">Algorithms</td><td colspan="4">State-of-the-art approaches</td></tr><tr><td>ELICE: h (p)</td><td>Gaussian: h (p)</td><td>Raykar: h (p)</td><td>GLAD: h (p)</td></tr><tr><td>ROUX Ranksum: Accuracy</td><td>1.09e-06 (1)</td><td>2.67e-06 (1)</td><td>7.67e-05 (1)</td><td>1.38e-11 (1)</td></tr><tr><td>ROUX Ranksum: AUC</td><td>1.2e-06 (1)</td><td>0.0495 (1)</td><td>0.0606 (1)</td><td>0.0051 (1)</td></tr><tr><td>ROUX Signrank: Accuracy</td><td>1.4e-10 (1)</td><td>5.16e-10 (1)</td><td>1.23e-10 (1)</td><td>5.05e-12 (1)</td></tr><tr><td>ROUX Signrank: AUC</td><td>1.35e-06 (1)</td><td>6.3e-04 (1)</td><td>8.23e-05 (1)</td><td>5.63e-06 (1)</td></tr></table>

Note. The results are presented in the form of h (p), where h refers to the test value and p indicates whether the null hypothesis is rejected $( \mathrm { i . e . , ~ p = 1 } )$

The quality tasks are the tasks that a platform such as Figure Eight uses to assess the suitability of workers. In this section, the budget that we allocate to quality tasks is named the “exploration budget”, and is shown as $\mathbf { B _ { e x p l o r e } } .$ The remaining microtasking budget, which is named the “exploitation budget”, is allocated to the actual job, and is shown as $\mathbf { B _ { e x p l o i t } }$ . We estimate the amount of wasted budget on the basis that quality is a function of cost. That is, if the quality increases, then the budget spent on microtasking also increases. In fact, the budget spent on microtasking will not be wasted if paying more to workers leads to higher quality. However, waste is considered to occur when the job owner pays more while receiving unsatisfactory results. This is budget waste. A mathematical formulation of this definition is provided in Eq. (14).

$$
W a s t a g e = B _ {e x p l o r e} + (B _ {e x p l o i t} \times (1 - a c c u r a c y))\tag{14}
$$

The objective of this equation is to reduce budget waste by increasing accuracy (i.e., increasing the quality). Table 4 below shows the results for budget waste, where a lower level of budget waste represents better results. ROUX is first of the approaches in lowering the cost in two large datasets (RTE and TREC), and second (after the Gaussian approach) in three smaller datasets (TEMP, Duchenne, and Google). This significant cost eficacy of ROUX can be explained from a dataset perspective.

ROUX performs better in larger datasets (i.e., RTE and TREC). A shown in Table 2 above, in RTE and TREC, there are 164 and 137 workers, respectively. As the number of workers increases, the amount of cost involved in microtasking decreases, and the performance of ROUX improves (see Figs. 1 and 2). A larger dataset provides more information, which allows ROUX to learn more about the workers. A the dataset becomes smaller (i.e., TEMP: 76 workers, Duchenne: 17 workers, and Google: 57 workers), the learning power of ROUX could not leverage, and thus its cost eficacy is slightly lower than that of the Gaussian approach, but still outperforms the other state-of-the-art approaches. Moreover, ROUX applies rough sets that do not require any parameter tuning other than the provided data. Rough sets could hold the information content while minimizing the amount of knowledge involved [32], and therefore, it helps ROUX to lower the cost.

## 5. Concluding remarks

Crowdsourcing allows organizations to outsource tasks and access a wide range of online workers with varying levels of knowledge and expertise. This necessitates a cost-efective approach to expertise esti mation to identify the most appropriate workers. The principal purpose of this paper is to introduce an unsupervised expertise-estimation approach named “ROUX” to overcome the limitations of the existing stateof-the-art expertise-estimation approaches. ROUX was compared with these approaches in five benchmark datasets. The results demonstrated that ROUX outperforms competitors in both accuracy and AUC. The achieved superior performance results from the novel integration of rough sets with a metaheuristic optimization search algorithm $( \mathrm { i . e . , }$ harmony search). Integration of rough sets and harmony search allows the extraction of workers who are suitable for a specific task. It also allows ROUX to formulate the expertise estimation as an optimization problem, and search within the possible solution space. This paper has made the important contributions described below:

Cost eficacy analysis of ROUX and its comparisons with state-of-the-art ap proaches (lower level of budget waste represents better results).

<table><tr><td rowspan="2">Dataset</td><td colspan="5">Approaches</td></tr><tr><td>ELICE</td><td>Gaussian</td><td>Raykar</td><td>GLAD</td><td>ROUX</td></tr><tr><td>RTE</td><td>2832</td><td>188</td><td>273.5</td><td>506</td><td>84.25</td></tr><tr><td>TEMP</td><td>1824.4</td><td>31.4</td><td>172.4</td><td>443.7</td><td>45.6</td></tr><tr><td>Duchenne</td><td>99.5</td><td>16</td><td>140.6</td><td>365</td><td>26</td></tr><tr><td>Google</td><td>443.4</td><td>77.3</td><td>289</td><td>911.5</td><td>102.5</td></tr><tr><td>TREC</td><td>159.2</td><td>51.6</td><td>114</td><td>934.8</td><td>8.25</td></tr></table>

• Unsupervised expertise estimation. This paper introduced a new unsupervised expertise-estimation approach for multitask crowdsourcing. Some existing algorithms assume that there is an expert to supervise the performance of workers. However, in real-world crowdsourcing platforms, the tasks and workers are heterogeneous and numerous. It is impractical to expect human intervention to be available to supervise the performance of workers on such platforms. As an unsupervised approach, ROUX does not rely on human intervention, rather, it formulates the process of expertise estimation as an optimization process using harmony search and uses rough-set theory to estimate the expertise of workers.

• Independence from answer type. Some existing approaches require that answers to the assigned tasks follow specific formats (e.g., numerical, binary, multiple choice, or text). This implies that expertise estimation requires diferent approaches for diferent answer formats. This limits the utility of an expertise-estimation approach because an approach that works well on multiple-choice answers might not work on binary answers. ROUX uses rough sets to estimate the expertise of workers. This means that ROUX will work with any format of answer type (e.g., numerical, binary, multiple choice, or text). For each type of task, ROUX builds a task repository. Once a new task arrives, based on its type, ROUX retrieves workers with the highest level of expertise in that task type.

• Robustness to sparseness. ROUX does not sufer from data sparsity because the rough-set component estimates the expertise of each worker based on the tasks the worker has answered. This means that if a worker has not accepted some specific tasks, then the corresponding entry in the worker–task matrix is empty, and ROUX assigns a lower expertise rating to the worker for that type of task(s). Thus, if a worker participates in a greater number of tasks and provides a greater number of accurate answers, then ROUX is more likely to assign a higher expertise rating to that worker.

In practical terms, ROUX ofers three important benefits for crowdsourcing stakeholders. First, the advantage of ROUX as an unsupervised approach relaxes the requirement for human intervention. As a result, it grounds improvement of the accuracy of expertise esti mation. Once this accuracy is improved, the crowdsourcing platform will be more reliable and thus attract more customers. This advantage results from the optimization formulation of ROUX, which relies on harmony search metaheuristic. Second, ROUX makes it easier for or ganizations to use crowdsourcing. Given that ROUX can work on various types of worker inputs (i.e., various types of answers: numerical, binary, multiple choice, or text), crowdsourcing platforms do not need to implement new approaches for aggregating results. Third, im plementing ROUX means crowdsourcing platforms will not require large volumes of data because ROUX performs successfully even with a low volume data. This is because ROUX's adoption of rough sets as the main component of expertise estimation.

There are a number of limitations to the study. First, ROUX depend on harmony search as a metaheuristic search algorithm. This optimization formulation is a global search algorithm, in that it is capable in locating a globally optimal solution while becoming trapped in a local optima [33,34]. To help the harmony search component of ROUX es cape from local optima, integrating harmony search with proper local search operators (e.g., Forsati et al.'s proposal [34]) can be considered. This integration helps to refine the subset of workers and thus worker with more similar expertise will be placed in the same group.

The second limitation relates to real-world dataset. The datasets used in this study are sparse, meaning that some workers skip an swering some tasks, thus leading to data sparseness. Overcoming sparsity can help ROUX learn more about workers and thus generate better results. That is, although the sparsity does not stop ROUX from estimating the expertise of workers, it might reduce the accuracy of the expertise estimation. Therefore, future research can consider an optimization-based matrix factorization [35] to overcome the sparsity of the datasets.

The third limitation of ROUX is that the cost performance is limited by the size of datasets (i.e., the number of workers). Although its performance in accuracy and AUC is remarkable, in smaller datasets that have insuficient information about workers, ROUX becomes slightly less cost efective. Thus, future research can consider enhancing ROUX using an oversampling technique [36] to enable it to work better for smaller datasets. By employing the oversampling technique, an algorithm can generate artificial data that is similar to the existing data, which will increase the learning power of ROUX.

Future researchers may also explore the performance of ROUX using other datasets. This research was conducted on five real-world crowd sourcing datasets using binary and multiple-choice answer types. Future research could consider other answer types such as text and images. Nevertheless, this paper represents the first study to propose and test an unsupervised approach to expertise estimation for microtask crowdsourcing, and finds that the created algorithm leads to improved accuracy and lower cost.

## References

[1] K.R. Jespersen, Crowdsourcing design decisions for optimal integration into the company innovation system, Decision Support Systems 115 (2018) 52–63.

[2] A. Moayedikia, W. Yeoh, K.-L. Ong, Y.L. Boo, Framework and literature analysis for crowdsourcing's answer aggregation, Journal of Computer Information Systems 58 (1) (2017) 1–12.

[3] C. Chiu, T. Liang, E. Turban, What can crowdsourcing do for decision support, Decision Support Systems 65 (2014) 40–49.

[4] D. Nevo, J. Kotlarsky, Primary vendor capabilities in a mediated outsourcing model: can IT service providers leverage crowdsourcing, Decision Support Systems 65 (2014) 17–27.

[5] D.C. Brabham. Moving the Crowd at iStockphoto: The Composition of the Crowd and Motivations for Participation in a Crowdsourcing Application, vol. 13, (2008) p. 6.

[6] V. S. Sheng, F. Provost and P. G. Ipeirotis, Get another label? improving data quality and data mining using multiple, noisy labelers, in Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining, (2008) 614–622

[7] P. Wu, E.W. Ngai, Y. Wu, Toward a real-time and budget-aware task package allocation in spatial crowdsourcing, Decision Support Systems 110 (2018) 107–117

[8] D. Geiger, M. Schader, Personalized task recommendation in crowdsourcing information systems — current state of the art, Decision Support Systems 65 (2014) 3-16.

[9] A. Dawid, A. Skene, Maximum likelihood estimation of observer error-rates using the EM algorithm, Applied Statistics 28 (1979) 20.

[10] P. Groot, A. Birlutiu, T. Heskes, Learning from multiple annotators with Gaussian processes, Artificial Neural Networks and Machine Learning–ICANN, Springer, 2011, pp. 159–164.

[11] V. Raykar, S. Yu, L. Zhao, G. Valadez, C. Florin, L. Bogoni, L. Moy, Learning from crowds, Journal of Machine Learning Research 11 (2010) 1297–1322.

[12] P.G. Ipeirotis, Project Troia: quality Assurance in Crowdsourcing, 18 June 2013, [Online]. Available: https://www.behind-the-enemy-lines.com/2013/06/project troia-quality-assurance-in.html , Accessed date: 10 March 2019.

[13] Y. Yan, R. Rosales, G. Fung, R. Subramanian, J. Dy, Learning from multiple anno tators with varving expertise, Machine Learning 95 (3) (2014) 291–327

[14] F. Khattak, A. Salleb-Aouissi, Quality control of crowd labeling through expert evaluation. Proceedings of the NIPS 2nd Workshop on Computational Social Science and the Wisdom of Crowds. 2011

[15] C. Ho, J. Vaughan, Online Task Assignment in Crowdsourcing Markets, AAAI, 2012.

[16] C. Ho, S. Jabbari, J. Vaughan, Adaptive task assignment for crowdsourced classi fication, Proceedings of the 30th International Conference on Machine Learning (ICML-13), 2013.

[17] J. Whitehill, P. Ruvolo, T. Wu, J. Bergsma, J. Movellan, Whose vote should count more: Optimal integration of labels from labelers of unknown expertise, Advances in Neural Information Processing Systems, 2009.

[18] I. Boutsis, V. Kalogeraki, On task assignment for real-time reliable crowdsourcing, Distributed Computing Systems (ICDCS). 2014 JEEE 34th International Conference on, 2014.

[19] L. Tran-Thanh, S. Stein, A. Rogers, N.R. Jennings, Eficient crowdsourcing of unknown experts using multi-armed bandits, Artificial Intelligence 214 (2014) 89-111.

[20] D. Karger, S. Oh, D. Shah, Iterative learning for reliable crowdsourcing systems, Advances in Neural Information Processing Systems (2011) 1953–1961.

[21] Ş. Ertekin, C. Rudin and H. & Hirsh, Approximating the crowd, Data Mining and Knowledge Discovery, 28(5–6) (2014) 1189–1221.

[22] Z.W. Geem, J.H. Kim, G.V. Loganathan, A new heuristic optimization algorithm: harmony search, Simulation 76 (2) (2001) 60–68 Simulation.

[23] H. Amirkhani, M. Rahmati, Agreement/disagreement based crowd labeling Applied Intelligence 41 (1) (2014) 212–222

[24] C. Long, G. Hua, A. Kapoor, A joint Gaussian process model for active visual recognition with expertise estimation in crowdsourcing, International Journal of Computer Vision (2015) 1–25

[25] P. Welinder, P. Perona, Online crowdsourcing: Rating annotators and obtaining cost-efective labels, Computer Vision and Pattern Recognition Workshops (CVPRW), 2010 IEEE Computer Society Conference on, 2010.

[26] D.R. Karger, S. Oh, D. Shah, Eficient crowdsourcing for multi-class labeling, Proceedings of SIGMETRICS, 2013.

[27] A. Tarasov, S. Delany, B. Namee, Dynamic estimation of worker reliability in crowdsourcing for regression tasks: making it work, Expert Systems with Applications 41 (2014) 6190–6210.

[28] R. Diao. O. Shen. Feature selection with harmony search. JEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics) 42 (6) (2012) 1509–1523.

[29] A. Moayedikia, K.L. Ong, Y.L. Boo, W.G. Yeoh, R. Jensen, Feature selection for high dimensional imbalanced class data using harmony search, Engineering Applications of Artificial Intelligence 57 (2017) 38–49.

[30] R. Jensen, Q. Shen, New approaches to fuzzy-rough feature selection, IEEE Transactions on Fuzzy Systems 17 (4) (2009) 824–838.

[31] R. Snow, B. O'Connor, D. Jurafsky, A. Ng, Cheap and fast–but is it good? Evaluating non-expert annotations for natural language tasks, Proceedings of the Conference on Empirical Methods in Natural Language Processing, 2008.

[32] J. Demšar, Statistical comparisons of classifiers over multiple data sets, The Journal of Machine Learning Research 7 (2006) 1–30.

[33] M. Mirkhani, R. Forsati, A. Mohammad Shahri, A. Moavedikia, A novel efficient algorithm for mobile robot localization. Robotics and Autonomous Systems 61 (9 (2013) 920–931.

[34] R. Forsati, A. Moavedikia, M. Shamsfard, M. Mohammad Reza, Enriched ant colony optimization and its application in feature selection, Neurocomputing 142 (2014) 354–371.

[35] R. Forsati, M. Mahdavi, M. Shamsfard, M. Sarwat, Matrix factorization with explici trust and distrust side information for improved social recommendation, ACM Transactions on Information Systems 17 (2014) 32

[36] T. Zhu, Y. Lin, Y. Liu, W. Zhang, J. Zhang, Minority oversampling for imbalanced ordinal regression, Knowledge-Based Systems 166 (2019) 140–155.

Alireza Moavedikia received his PhD from Deakin University Australia in 2018. Prior to that, he received Bachelor of Software Engineering from Karai Azad University Iran in 2011, and Master of Science in Software Engineering from Staffordshire University ir 2013. He is currently a lecturer at Swinburne University of Technology, His research interests include machine learning, data mining and their application in crowdsourcing and recommender system. His research works have appeared in reputable journals such as Engineering Applications of AI, and Neurocomputing.

William Yeoh is the Director for IBM Centre of Excellence in Business Analytics at Deakin

University Australia. His main research interests include Business Analytics, Data Mining, Cloud Computing and Crowdsourcing. His research are supported by various funding bodies and have appeared in high-tier journals (ABDC A\* & A journals) and top IS conferences (eg. ICIS). He has won numerous awards including the 2017 ICT Educator of the Year Gold Award (awarded by the Australian Computer Society ACS), internationally competitive IBM Faculty Award, Deakin's Vice-Chancellor Award, and Deakin's Faculty Excellence in Research Award.

Kok-Leong Ong is an Associate Professor in Business Analytics at La Trobe Business School, La Trobe University. Before joining La Trobe in 2015, he was a Senior Lecturer in the School of Information & Business Analytics, Deakin University. He received his PhD and B.A.Sc. (Hons) from the Nanyang Technological University, Singapore in 1999 and

2004 respectively. His research interests include data mining and analytics, machine learning and decision support systems. He has published over 50 peer-reviewed conference and journal papers, and book chapters. He has served on a number of program committees, including grant assessor for the Australia Research Council since 2007, and a steering committee of Australia's Data Mining and Analytics Conference.

Yee Ling Boo received her PhD in Information Technology from Monash University Australia. She is currently a lecturer at School of Business IT and Logistics, RMIT University Australia. Her research interests include Data Mining, Brain Inspired Computing, Cognitive Analytics and their applications in business, education and health. Before the pursuit of her PhD. degree, she was a software engineer in Malaysia. Her research works have appeared in reputable journals and conferences
