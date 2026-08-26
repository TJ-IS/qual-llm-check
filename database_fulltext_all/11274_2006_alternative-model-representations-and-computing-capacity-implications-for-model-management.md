---
otero_id: 11274
otero_key: "5682PFGQ"
title: "Alternative model representations and computing capacity: Implications for model management"
authors: "Kingsley Gnanendran; R.P. Sundarraj"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.11.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Alternative model representations and computing capacity: Implications for model management

Kingsley Gnanendran <sup>a,1</sup>, R.P. Sundarraj <sup>b,⁎</sup>

<sup>a</sup> Department of Operations and Information Management, University of Scranton, Scranton, PA 18510-4602, USA <sup>b</sup> Department of Management Sciences, University of Waterloo, 200 University Ave. West, Waterloo, Canada ON N2L 3G1

Received 28 January 2005; received in revised form 16 November 2005; accepted 18 November 2005 Available online 15 March 2006

## Abstract

Recent research on model management systems (MMS) recognizes the importance of considering potential algorithmic performance in the selection of an appropriate model to solve a real-world problem. Model selection, as typically viewed in the literature however, is the process of selecting from among alternative model classes, rather than from alternative mathematical representations of the same model class. In this paper, we take up this subtler aspect of model selection, and provide tangible evidence that shows how just changing the representation of a model can have a dramatic impact on algorithmic performance. Using problem decomposition and distributed processing, we conduct a series of computational experiments to study the interrelationships between model representation, computing capacity, and algorithmic performance. We discuss potential implications of our results for improving MMS design and address a key prerequisite for the enhanced design, by proposing and validating an approach for solution time prediction. © 2005 Elsevier B.V. All rights reserved.

Keywords: Model management systems; Distributed model management; Model selection; Parallel and distributed computing; Grid computing; Metacomputing; Decomposition

## 1. Introduction

A model management system (MMS) is a software system that provides tools for the development, storage, and manipulation of the models, data, and solution methodologies associated with complex decision problems. MMSs make the structural and algorithmic aspects of a model transparent to users, and facilitate the integration of models from diverse modeling traditions (optimization, statistical modeling, simulation, etc.). A key issue addressed by an MMS is model selection; i.e., the choosing of the best model for solving a given problem. When solution time is an important criterion to the user, the model selection decision must take into account not only the semantic nature of the problem class, but also the interactions between alternative computational paradigms (e.g., parallel computing), available computing capacity, and the particular structure and dimensions of the problem instance being presented to the solver. This issue is of particular relevance today due to the emergence of grid computing systems [6] as a commercially viable source of computing capacity. While grid computing could encompass diverse resources such as CPUs, storage units, communication networks, code repositories, databases, etc. [7], our focus in this paper is on grid computing in a narrow sense—as a source of idle CPUs that can be harnessed to solve complex models. Accordingly, throughout this paper, any references to “computing capacity” should be taken to mean “the number of available processors”.

Mathematical programmers have studied the interactions between problem structure and computing capacity for years, but such efforts were generally done from an algorithmic perspective and, largely, not aimed at prediction of solution time. On the other hand, these interactions have hardly ever been addressed in the MMS literature [18] and even the few proposals that do address them have simply called for the use of computational complexity measures, such as worstcase bounds, as a predictor of solver performance [19]. Unfortunately, there often exists a wide divergence between observed performance and the theoretical worst-case bound (a much celebrated example is the simplex method for linear programming). This paper addresses the aforementioned gaps in the literature by: (i) demonstrating, via a series of computational experiments, how the interactions between model representation, computing capacity, and solver performance can impact MMS effectiveness, and (ii) proposing and validating a predictive timing model approach as an alternative to merely using complexity measures as a predictor of solver performance.

Current MMS literature views model selection as the process of selecting from among a heterogeneous collection of models. For example, at a high level of abstraction one may choose a model based on assumptions made for the sake of tractability; e.g., it is common to assume that production cost is linear in the number of units produced, although this may not be true in the real-world situation. At another level are problem transformations, as when a given model is converted to another problem type with better computational characteristics—e.g., a shortest path problem could be converted to an assignment problem. In this paper, we consider a broader definition of model selection that includes, additionally, choices among alternatives at the level of representation. A representation is a depiction of the model so that the problem type and overall problem size are unchanged but the internal structure of the model is presented in a different way (note: we use the term representation to indicate how the model is presented to the solver, rather than how it is stored in the MMS). A common example is when the variables and constraints are re-ordered (permuted) to obtain some type of specialized nonzero pattern within the coefficient matrix.

To understand the interrelationships between model, computing resource, and solver performance, we use the example of a bounded, multi-commodity version of the well-known transportation model. This model can be represented in multiple ways, each having significantly different computational characteristics. In addition, each representation also has a decomposable block structure, making this model a good candidate for decomposition as well as parallelization. The application of decomposition is relevant to our study because the MMS literature recognizes the important role played by decomposition methodologies in solving decision problems [20]. Parallelization is a critical avenue for future development of MMS because of the increasingly prominent role that distributed and grid computing systems are expected to play in the future [22–24].

The rest of this paper is organized as follows. In the next section, we review the literature on model management systems. Alternative representations of the multi-commodity transportation model are described in Section 3. Our experimental framework and computational results are given in Section 4. Section 5 discusses the implications of our results for MMS design, while Section 6 presents an approach for incorporating our results into MMS design. Section 7 contains our concluding remarks.

## 2. Model management systems

MMS research tends to fall into one of two categories [20]: modeling-in-the small and modeling-in-the-large. Modeling-in-the small concerns the support provided by an MMS in the formulation of a particular model. Advances in this category include modeling languages [9], which address the difficulty of specifying the problem instance to the solver (an example is the MPS data format for linear programs). Such modeling languages are important to the development and maintenance of single-user decision support systems.

However, when models are considered to be an organizational resource, the MMS must contend with modeling-in-the-large issues as well. These issues include: model administration, which facilitates the sharing and reusing of models; problem–model linkage, which is a mechanism to facilitate the abstraction of the real-world problem into a model and of translating the results back to real-world terms; model–model linkage, which is the integration of independent models into a larger, composite model; and model–data linkage, which is concerned with data and instance management. Huh et al. [16] provide an MMS framework to facilitate model administration and model synchronization in concurrent, multi-user systems. Muhanna and Pick [20] developed a framework to address the above issues, and built a prototype MMS based on that framework. In addition to a module for interactions with the user (dialog management), this framework consists of three key modules.

• Model consultation subsystem is responsible for assisting the user in selecting a model.

• Model distribution subsystem evaluates the potential of distributing solvers/models across a set of processors of a distributed computer, by considering load distribution and interprocessor communication.

• Model execution subsystem is responsible for handling the administrative functions of the set of distributed solvers. These functions include the management of heterogeneous computing resources as well as providing for fault recovery during the execution process.

Although Muhanna and Pick's framework allows for alternative solution algorithms and for multiple solver instances to be associated with a single model, it did not consider the impact of computational capacity in the choice of a particular algorithm. Mayer [19] suggests conceptual enhancements to the above framework to take into consideration a number of additional aspects. First, Mayer proposes the inclusion of computational complexity measures (CMs) in the model/solver selection decision. Second, resource selection is deemed to be important, especially when machine availability is not uniform. Finally, extensions are proposed to allow for parallelization of the solvers and for the distribution of models/solvers across machines.

In relation to current MMS literature, our contributions in this paper are as follows: First, by showing huge reductions in solution time (sometimes by a factor of almost 500), we provide powerful motivation for the inclusion of alternative representations in the mix of model choices that are to be evaluated by the MMS. Second, we demonstrate that the interaction effects between model (size and representation), computing resource (architecture and capacity), and algorithmic performance (solution time) are significant, thus providing tangible evidence to support the incorporation of the design extensions conceptualized above. Third, we propose and validate a timing model approach that appears superior to the mere inclusion of CMs as a predictor of solver performance in the enhanced MMS design.

## 3. Alternative representations of a model

Our computational study is based on a multicommodity transportation problem with bounds on the node requirements. We begin with a formal statement of the model (Section 3.1) and show how it can yield alternative representations with different block structures (Section 3.2). The effect of these alternative representations on solution time is investigated in Section 4.

## 3.1. Illustrative model

Suppose we are given a set of commodities that need to be transported from various suppliers to various customers. Customer demands and supplier capacities (per commodity as well as aggregate) are given, as also is the unit cost of transporting each commodity from each supplier to each customer. The objective is to determine the shipment quantities for each commodity–customer– supplier combination that minimize the total transportation cost. This type of multi-commodity transportation model appears in a number of production–distribution situations (e.g., [28]) and is stated as follows.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Notation
I Set of customers (indexed by i)
J Set of commodities (indexed by j)
K Set of suppliers (indexed by k)
 $x_{ijk}$  Units of commodity j shipped to customer i from supplier k
 $c_{ijk}$  Unit cost of shipping commodity j from supplier k to customer i
 $p_{ijk}$  Capacity consumed at supplier k by one unit of commodity j shipped to customer i
 $q_{ijk}$  Capacity consumed at customer i by one unit of commodity j received from supplier k
 $a_{k}(b_{k})$  Lower (upper) limit on the aggregate capacity of supplier k
 $d_{i}(e_{i})$  Lower (upper) limit on the aggregate capacity of customer i
 $f_{ij}(g_{ij})$  Lower (upper) limit on the demand for commodity j by customer i
 $u_{jk}(v_{jk})$  Lower (upper) limit on the supply of commodity j by supplier k
</div>

Model (M)

$$
\operatorname{Min} \sum_ {i, j, k} c _ {i j k} x _ {i j k}\tag{1}
$$

s.t.

$$
a _ {k} \leq \sum_ {i, j} p _ {i j k} x _ {i j k} \leq b _ {k} \quad \text {   for   all   } k\tag{2}
$$

$$
d _ {i} \leq \sum_ {j, k} q _ {i j k} x _ {i j k} \leq e _ {i} \quad \text {   for   all   } i\tag{3}
$$

$$
f _ {i j} \leq \sum_ {k} x _ {i j k} \leq g _ {i j} \quad \text {   for   all   } i, j\tag{4}
$$

$$
u _ {j k} \leq \sum_ {i} x _ {i j k} \leq v _ {j k} \quad \text {   for   all   } j, k\tag{5}
$$

$$
x _ {i j k} \geq 0 \quad \text {   for   all   } i, j, k.\tag{6}
$$

In model (M), expression (1) minimizes the total shipping cost; constraints (2) and (3) specify bounds on capacity utilization at the supply and demand points, respectively; and (4) and (5) represent bounds, respectively, on the supplies and demands of individual commodities.

## 3.2. Alternative representations

Permuting the rows and columns of the coefficient matrix is a frequently used technique to create an equivalent, but computationally advantageous, representation of a given problem. A number of authors have considered the issue of “optimal” permutation (e.g., [21]) although it is known that, for unstructured problems, the determination of an optimal permutation reduces to the NP-hard graph partitioning problem [8].

In contrast to these studies, the permutation approach that we propose here is based on an intuitive understanding of the problem, and is very easy to perform. Rather than relying on the mechanical application of some procedures (e.g., pivoting, partitioning, etc.) on unstructured problems, the emphasis here is on exploiting the semantics of the problem. This is similar to the approach taken by Burton and Obel [1] in their study of organizational design problems.

In the case of model (M) given earlier, the problem context suggests that one should be able to decompose this model in three different ways: by customer, by commodity, or by supplier. We denote these alternative representations as Perm(I), Perm(J), and Perm(K), since $I , J ,$ and K are the index sets of customers, commodities, and suppliers, respectively. To obtain Perm(I), the constraints involving summations over the index i are written first. That is, constraint sets (2) and (5) are written first, followed by constraint sets (3) and (4). The second representation, Perm(J), is obtained by reordering constraint sets (2) and (3) first, followed by (4) and (5). Likewise, in Perm(K), the rows are reordered so that constraints involving summations over the index k are written first. Obviously, since these representations are simply permutations of the rows and columns, there is no change in the overall dimensions of the model. Further, all the three representations of (M) have the block-angular structure (i.e., have diagonal blocks connected by a set of coupling constraints).

However, the representations can have markedly different internal dimensions. These differences can significantly impact solution time of (M), forcing the user to evaluate and choose a suitable computational strategy. Indeed, this issue becomes considerably more complicated when parallel processing is also an available option. We investigate the impact of alternative model representation and available computing capacity on solution time in the ensuing section. These interrelationships have been researched algorithmically but, so far, have not been incorporated into the MMS framework.

## 4. Model representation and computing capacity

The model selection decision in an MMS pertains to picking the “best” model to solve a given problem instance (in our case, model (M) with |I|, |J|, |K| and other data instantiated) within the available computing capacity (computing capacity is defined as the number of processors employed in the solution process). This decision essentially reduces to the following questions: (i) Given a fixed computing capacity, what is the best representation? (ii) When a variable amount of computing capacity is available, what combination of representation and computing capacity is best?

To investigate these questions, we conducted a series of computational experiments on the model (M) given in Section 3.1. This linear programming model exhibits the block-angular structure, making it an excellent candidate for solution by parallel decomposition. Specifically, we used a parallel implementation [10] of the Dantzig–Wolfe (DW) decomposition algorithm [3] to conduct these experiments. We begin with a brief overview of Dantzig–Wolfe decomposition followed by computational experiments addressing the questions raised.

## 4.1. Dantzig–Wolfe decomposition

Decomposition approaches, in general, are relevant to MMS research for several reasons. First, structured models abound in real-world applications, with decomposition being commonly suggested as a solution approach [12]. Second, the MMS literature itself recognizes the importance of the decomposition approach in providing resource-allocation decisions in decentralized situations [20]. Finally, decomposition algorithms are often well-suited for parallel- and distributed-computing platforms that have been projected to become more widely prevalent in the future.

Consider a block-angular linear program with P sets of diagonal block-constraints that are tied together by a series of coupling constraints. In the DW decomposition for block-angular linear programs, the original problem is decomposed into a series of subproblems, one for each diagonal block. The original problem is then replaced by an equivalent linear program, known as the master problem (MP). The columns of the master problem (called proposals) are projections of the solutions generated by the subproblems $( \mathrm { S P } _ { 1 } , \mathrm { S P } _ { 2 } , . . . )$ The rows of the master essentially consist of a modified version of the coupling constraints plus an additional P convexity constraints, one each for a subproblem. The dual price vector of the coupling constraints are often simply known as prices.

An iteration of the DW algorithm consists of first solving the master problem and passing on the prices to the subproblems. Next, the subproblems are solved independent of one another, and any proposals generated by them are sent to the master. As mentioned before, these proposals become columns in the master, with the potential to enter the basis. Thus, proposals are generated by a subproblem only if they can potentially generate an improvement (i.e., yield a negative reduced cost) in the master. The algorithm terminates when none of the subproblems is able to generate a proposal.

To study our research questions with this algorithm, recall from Section 3.2 that each representation of (M) has the block-angular structure, and can therefore be parallelized. However, the representations are different from one another in terms of the relative dimensions of the resulting master and subproblems. For example, with |I| = 2, |J| = 3, and |K| = 5, Perm(I) has 2 subproblems of dimensions 8×15 and a master problem of 40×30, Perm(J) has 3 subproblems of dimensions 14 ×10 and a master problem of $1 4 \times 3 0$ , while Perm(K) has 5 subproblem of dimensions 8 ×6 and a master problem of 16 × 30. Thus, their computational performances are likely to vary as well considerably. Another important difference among the representations is the number of subproblems. In Perm(I), there will be |I| subproblems, whereas in Perm(J) and Perm(K), there will be |J| and |K subproblems, respectively.

Finally, the consideration of all these variations is further compounded by the need to take into account computing capacity as well as architecture (serial vs. parallel computation). If one wants to exploit all the parallelism with a large pool of available processors, then the MMS could allocate one subproblem to each processor (e.g., Perm(I) uses |I| processors, etc.). However, this mechanism could have the undesirable effect of increasing communication overheads. Thus, it might perhaps be advantageous to allocate multiple subproblems (instead of a single subproblem) to each processor, thereby providing a better balance of the subproblem processors' loads relative to that of the master.

The next section describes the experiments conducted to study the relationship between model and performance, and how this link is impacted by available computing capacity (in our case, number of processors) in both the serial and distributed computing environments.

## 4.2. Experimental results

The solver used in our experiments conducts interprocessor communication through the Message Passing Interface (MPI) [11], which has been implemented on many platforms. Currently, the solver runs on a 40-processor Silicon Graphics Origin under a 64-bit UNIX operating system (IRIX 6.5). Our implementation features a number of techniques that have been shown to work well in previous research (e.g., [10]). It handles block-angular linear programming problems with up to 30 subproblems, and maximum overall dimensions of 37,200 rows and 120,000 columns.

## 4.2.1. Experiment 1

The purpose of the first experiment is to test whether different model representations have an impact on solution time. For this purpose, we consider 10 random problems with |I| = 10, |J| = 2, and $| K | = 1 5 .$ . The serial solution times for the three representations, and the ratios of the maximum to minimum times are given in Table 1. The shaded cell in each row of the table indicates the representation with the lowest solution time for that problem. It can be observed that there is a significant difference in the solution times between the three representations. On average we find that, for these problems, a suitable representation can reduce the solution time by a factor of 2.38.

## 4.2.2. Experiment 2

Our next experiment is designed to test whether the best representation changes with respect to the computing architecture used (i.e., serial vs. parallel). Ten random problems with $\scriptstyle | I | = 2 0 , \ | J | = 2$ , and $| K | = 3 0$ were solved using both serial and parallel versions of the DW algorithm (here we assign one processor per “natural” subproblem, while Experiments 4 and 5 consider multiple subproblem assignment per processor). Table 2 gives the results. The two shaded cells in each row denote the best serial and best parallel times for the given problem. We see that the best representation for the serial case (typically Perm(K)) is indeed different from that for the parallel case (Perm(J)). Moreover, for the parallel case, the best representation is, on average, superior to the worst representation by a factor of almost 5. These results highlight the tremendous importance of having to consider computing architecture and capacity in the resolution of the model choice issue.

Table 1  
Impact of model representation on solution time (Experiment 1)

<table><tr><td rowspan="2">Problem</td><td colspan="4">Solution times (serial)</td></tr><tr><td>Perm(I)</td><td>Perm(J)</td><td>Perm(K)</td><td>Max/Min</td></tr><tr><td>1</td><td>47</td><td>20</td><td>26</td><td>2.35</td></tr><tr><td>2</td><td>49</td><td>35</td><td>45</td><td>1.40</td></tr><tr><td>3</td><td>53</td><td>20</td><td>27</td><td>2.65</td></tr><tr><td>4</td><td>56</td><td>38</td><td>36</td><td>1.56</td></tr><tr><td>5</td><td>51</td><td>23</td><td>27</td><td>2.22</td></tr><tr><td>6</td><td>59</td><td>22</td><td>26</td><td>2.68</td></tr><tr><td>7</td><td>33</td><td>25</td><td>20</td><td>1.65</td></tr><tr><td>8</td><td>36</td><td>135</td><td>33</td><td>4.09</td></tr><tr><td>9</td><td>58</td><td>35</td><td>18</td><td>3.22</td></tr><tr><td>10</td><td>62</td><td>31</td><td>37</td><td>2.00</td></tr><tr><td>Mean</td><td>50.4</td><td>38.4</td><td>29.5</td><td>2.38</td></tr></table>

|I| = 10, |J| = 2, |K| = 15.  
All times here and in the following tables have been scaled-down by a factor of 10,000.

We also observe two other results that are counterintuitive at least at first sight. First, for certain representations, we see that the parallel times can actually be worse (larger) than the corresponding serial times for the same representation. Second, for a majority of the problem instances, the best parallel time across the three representations is actually larger than the best serial time overall (e.g., best parallel time for Problem 1 is 709, whereas the best serial time is 465). Both these results can be explained by the fact that the communication overhead needed for the many subproblems (in Perm(I) and Perm(K)) outweighs the benefits attained through decomposition.

## 4.2.3. Experiment 3

While Experiment 2 offered a rather pessimistic view of parallelization, our next experiment is aimed at establishing the existence of effectively parallelizable problem instances. Table 3 shows timing results on 10 random problems with |I|=8, |J|=10, and |K|=8. The times given by the best representation (Perm(J)) are better, on average, than the worst representation (almost always Perm(I)) by factors of over 150 for the serialsolver case, and almost 500 for the parallel-solver case.

While all three representations employed about the same number of processors (either 8 or 10), they differ in terms of the complexity of the master vis-à-vis the subproblems. Perm(I) and Perm(K) both have 176 rows in the master and 22 rows in each subproblem, while Perm(J) has 32 rows in both master and each subproblem. The lack of significant speedups with Perm(I) and Perm(K) can be attributed to the fact that the master problem is more of a bottleneck under these representations.

## 4.2.4. Experiment 4

Next, we examine computational efficacy of blocking; i.e., the assignment of more than one natural subproblem to a processor. To investigate this question, we study a single representation, namely, Perm $( J ) ,$ for a problem with $[ I ] = 1 5 , | J | = 2 4 , | K | = 1 5 .$ . The number of processors used ranged from 2 to 24. In cases when the number of processors is less than $| J | ,$ each processor was assigned multiple subproblems. For example, when two processors are used, $\mathrm { S P } _ { 1 } , \mathrm { S P } _ { 2 } ,$ $. . . , \mathrm { S P } _ { 1 2 }$ are combined into one block and assigned to processor 1, while $\mathrm { S P } _ { 1 3 }$ through $\mathrm { S P } _ { 2 4 }$ are assigned to processor 2. For the first set of runs, we used 2, 4, 6, 8, 12, and 24 processors (equivalently, blocks). Since these numbers divide evenly into the number of natural subproblems (24), each block is assigned an equal number of subproblems, yielding perfectly loadbalanced instances.

Table 2  
Impact of computing architecture on best model representation (Experiment 2)

<table><tr><td rowspan="2">Problem</td><td colspan="4">Solution times (serial)</td><td colspan="4">Parallel times</td></tr><tr><td>Perm(I)</td><td>Perm(J)</td><td>Perm(K)</td><td>Max/Min</td><td>Perm(I)</td><td>Perm(J)</td><td>Perm(K)</td><td>Max/Min</td></tr><tr><td>1</td><td>727</td><td>811</td><td>465</td><td>1.74</td><td>1019</td><td>709</td><td>1270</td><td>1.79</td></tr><tr><td>2</td><td>832</td><td>300</td><td>208</td><td>4.00</td><td>1182</td><td>240</td><td>1035</td><td>4.93</td></tr><tr><td>3</td><td>613</td><td>462</td><td>326</td><td>1.88</td><td>863</td><td>385</td><td>1763</td><td>4.58</td></tr><tr><td>4</td><td>545</td><td>350</td><td>183</td><td>2.98</td><td>712</td><td>283</td><td>522</td><td>2.52</td></tr><tr><td>5</td><td>474</td><td>166</td><td>468</td><td>2.86</td><td>732</td><td>118</td><td>911</td><td>7.72</td></tr><tr><td>6</td><td>595</td><td>604</td><td>296</td><td>2.04</td><td>895</td><td>510</td><td>645</td><td>1.75</td></tr><tr><td>7</td><td>457</td><td>132</td><td>179</td><td>3.46</td><td>722</td><td>89</td><td>803</td><td>9.02</td></tr><tr><td>8</td><td>537</td><td>111</td><td>335</td><td>4.84</td><td>840</td><td>72</td><td>681</td><td>11.67</td></tr><tr><td>9</td><td>514</td><td>274</td><td>206</td><td>2.50</td><td>742</td><td>213</td><td>508</td><td>3.48</td></tr><tr><td>10</td><td>642</td><td>510</td><td>275</td><td>2.33</td><td>1021</td><td>461</td><td>632</td><td>2.21</td></tr><tr><td>Mean</td><td>594</td><td>372</td><td>294</td><td>2.86</td><td>873</td><td>308</td><td>877</td><td>4.97</td></tr></table>

|I| = 20, |J| = 2, |K| = 30.

Table 3  
Impact of model representation on parallelization effectiveness (Experiment 3)

<table><tr><td rowspan="2">Problem</td><td colspan="4">Serial times</td><td colspan="4">Parallel times</td><td rowspan="2">Worst to best ratioa</td></tr><tr><td>Perm(I)</td><td>Perm(J)</td><td>Perm(K)</td><td>Max/Min</td><td>Perm(I)</td><td>Perm(J)</td><td>Perm(K)</td><td>Max/Min</td></tr><tr><td>1</td><td>5735</td><td>40</td><td>4474</td><td>143.38</td><td>5621</td><td>18</td><td>4370</td><td>312.28</td><td>318.6</td></tr><tr><td>2</td><td>6548</td><td>28</td><td>5973</td><td>233.86</td><td>6436</td><td>9</td><td>5855</td><td>715.11</td><td>727.6</td></tr><tr><td>3</td><td>6233</td><td>46</td><td>6042</td><td>135.50</td><td>6154</td><td>42</td><td>5928</td><td>146.52</td><td>148.4</td></tr><tr><td>4</td><td>5227</td><td>39</td><td>3904</td><td>134.03</td><td>5105</td><td>19</td><td>3803</td><td>268.68</td><td>275.1</td></tr><tr><td>5</td><td>6390</td><td>27</td><td>5905</td><td>236.67</td><td>6274</td><td>9</td><td>5791</td><td>697.11</td><td>710.0</td></tr><tr><td>6</td><td>7842</td><td>31</td><td>6053</td><td>252.97</td><td>7720</td><td>11</td><td>5944</td><td>701.82</td><td>712.9</td></tr><tr><td>7</td><td>6072</td><td>44</td><td>4930</td><td>138.00</td><td>5952</td><td>22</td><td>4819</td><td>270.55</td><td>276.0</td></tr><tr><td>8</td><td>4934</td><td>29</td><td>5248</td><td>180.97</td><td>4832</td><td>11</td><td>5139</td><td>467.18</td><td>477.1</td></tr><tr><td>9</td><td>5168</td><td>30</td><td>5828</td><td>194.27</td><td>5059</td><td>12</td><td>5713</td><td>476.08</td><td>485.7</td></tr><tr><td>10</td><td>6131</td><td>26</td><td>4591</td><td>235.81</td><td>6008</td><td>9</td><td>4485</td><td>667.56</td><td>681.2</td></tr><tr><td>Mean</td><td>6028</td><td>34</td><td>5295</td><td>188.5</td><td>5916</td><td>16</td><td>5185</td><td>472.3</td><td>481.3</td></tr></table>

|I| = 8, |J| = 10, |K| = 8.  
<sup>a</sup> Ratio of worst serial time to best parallel time.

Our results are shown in Table 4 for 10 problem instances. When using 24 processors, the problem's decomposability and parallelism are fully exploited, whereas at the other extreme–when two processors are employed–interprocessor communication is at its lowest. For this set of problem instances, the number of processors that balances these two factors and yields the lowest solution time is 12. However, from Table 4, we also note that while a large reduction in solution time is possible when going from 2 to 4 processors, the time differences between the 6-, 8-, and 12-processors solutions are not very large and, hence, may not be significant to the end-user. This observation points to the need to devise a solution strategy that considers the amount of resources expended in solving a model. In other words, when the organization has to pay for computational time, it is quite possible to have a negative marginal worth when more than 6 processors are employed (i.e., for these problems, the optimal number of processors could be 6 or 8, instead of 12, when considering computational cost).

Parallel times when computing capacity is varied WITH load balance (Experiment 4)

<table><tr><td colspan="6">Number of processors</td></tr><tr><td>2</td><td>4</td><td>6</td><td>8</td><td>12</td><td>24</td></tr><tr><td>1645</td><td>522</td><td>333</td><td>295</td><td>234</td><td>395</td></tr><tr><td>1819</td><td>593</td><td>314</td><td>296</td><td>253</td><td>576</td></tr><tr><td>2817</td><td>1051</td><td>575</td><td>458</td><td>345</td><td>1015</td></tr><tr><td>2357</td><td>903</td><td>554</td><td>460</td><td>395</td><td>1008</td></tr><tr><td>1960</td><td>526</td><td>378</td><td>310</td><td>296</td><td>880</td></tr><tr><td>1545</td><td>538</td><td>293</td><td>219</td><td>156</td><td>824</td></tr><tr><td>1670</td><td>508</td><td>342</td><td>221</td><td>156</td><td>534</td></tr><tr><td>1679</td><td>477</td><td>312</td><td>254</td><td>114</td><td>616</td></tr><tr><td>1742</td><td>516</td><td>266</td><td>188</td><td>152</td><td>405</td></tr><tr><td>1962</td><td>677</td><td>359</td><td>351</td><td>262</td><td>759</td></tr></table>

|I| = 15, |J| = 24, |K| = 15.

For the second set of runs, we varied the number of processors from 13 to 23 for one problem instance. Thus, the number of subproblems is a non-integral multiple of the number of processors. The results in Table 5 show that the resulting load imbalance makes the parallelization less effective.

## 4.2.5. Experiment 5

Finally, we repeated Experiment 4 for scaled-up and scaled-down versions of the problems therein. The scaled-down problem had dimensions of $\textstyle I = 1 0 , \left| J = 2 4 \right.$

Parallel times when computing capacity is varied WITHOUT load balance (Experiment 4)

<table><tr><td colspan="11">Number of processors</td></tr><tr><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td></tr><tr><td>211</td><td>314</td><td>376</td><td>512</td><td>428</td><td>779</td><td>569</td><td>596</td><td>676</td><td>480</td><td>603</td></tr></table>

and $| K | = 1 0$ , while the scaled-up problem had $\scriptstyle { | I | = 2 0 , | J | = }$ 24, $| K | = 2 0$ . Fig. 1A plots the parallel solution times under conditions of perfect load balance (i.e., number of natural subproblems is an integral multiple of the number of processors employed). Although there are differences in the magnitudes of the solution times between problem classes, the same distinct shape is discernible for all classes. The optimal number of processors appears to be 12, emphasizing that blocking is computationally advantageous. However, the curves are relatively flat near the optimum, and the 6- and 8- processor solution times are not much worse than the optimum values. Fig. 1B indicates the parallel times when the number of processors was varied from 13 to 23. This plot further reinforces the conclusion from Experiment 4 that load imbalance adversely and significantly affects speedup.

## 5. Potential implications for model management

The results from the previous section highlight the significant interaction effects between the alternative, albeit equivalent, representations of a model and computing resources (both architecture and capacity). Given below are four implications of our results for MMS design, and they directly impact two of the modules of the MMS framework discussed in Section 2 [19]. A prerequisite for these enhancements, however, is the ability to predict how solution time is affected when model representation and computational resources are varied. Later, in Section 6, we propose and validate a predictive timing model approach for this purpose.

## 5.1. Implications

The first implication relates to the model consultation subsystem (MCS) in the MMS framework. MCS provides modeling-in-the-large support by presenting an array of model choices to the end user. Typically, the offered models are heterogeneous in the sense that the mathematical structure of one model might be completely different from that of another (e.g., moving average versus exponential smoothing). Our experiments have demonstrated, however, that alternative representations of even the same model have drastically different computational characteristics and must be considered in the model choice decision. Although the fact that model representation could significantly affect solution time is well-accepted by the mathematical programming community, this aspect of model selection has not been explicitly considered in prior MMS literature.

![](/api/attachments/5682PFGQ/fulltext/images/73bbdd7a57d611472b95c9b4f3b4fd619a9c8aa683dace537a04a296b6c4bbda.jpg)

![](/api/attachments/5682PFGQ/fulltext/images/fbfc0163eb4e02284d9a84f38367c43414696c209af3364b8e83d366cbadd907.jpg)  
Fig. 1. Patterns among scaled problems (Experiment 5). (A) With load-balance. (B) Without load-balance.

Second, our results suggest that the MCS component needs to consider the interaction effect between model representation, problem instance, and computing architecture in order to obtain optimum solver performance. In Experiment 3, observe that although an improvement was obtained on all three representations by using a parallel computer (Table 3), the improvement in Perm(J) is substantially higher that those for the other two representations (Fig. 2A). Also note that while Perm(J) was the best choice on both serial and parallel computers in Experiment 3, it is unlikely that, in general, a single representation would be the best choice for a given instance regardless of the environment. Indeed, this is borne out by the results of Experiment 2—Perm(J) is the best representation when using parallel computation but, at least in the majority of cases, Perm(K) is the better option under serial computation. The interaction between problem instance and model representation is depicted in Fig. 2B where Set 1 (Set 2) represents the instances used in Experiment 1 (Experiment 2). It shows that, even for the same model class (in our case multicommodity transportation), the best model representation depends on the problem instance.

Third, an important function of the model distribution subsystem (MDS) is to determine the optimal computing capacity, i.e., the number of processors (or solvers) that should be used on a given problem instance. Our results showed that parallelization could sometimes be ineffective for certain instances regardless of the representation used. For example, even if a parallel computing environment is available, a serial solution would be the better choice for the majority of problem instances of Experiment 2. We also saw that even when parallelization is effective, full exploitation of the inherent parallelism may be counterproductive if interprocessor communication effects outweigh any time-savings due to the concurrent execution. Therefore, aggregating the natural model components into “blocks” may be a more effective strategy for certain problems. Experiment 5 provides initial evidence of a possible pattern (a rough “bowl” shape) that suggests an optimal blocking strategy or, equivalently, the optimal computing capacity that should be brought to bear on a given model instance. Another factor to consider in the model distribution subsystem is the balance of the workload among processors. The effect of this factor is illustrated in both Fig. 1B and Table 5, where using more processors is actually shown to increase solution time, conceivably due to load imbalance among the processors.

A  
![](/api/attachments/5682PFGQ/fulltext/images/8a9954010bdfd71f9501d9f5259c4304864dabf751e7092de9521536c1a3a92b.jpg)  
B

![](/api/attachments/5682PFGQ/fulltext/images/3c34bd59c7859723ca8b272ec3ebf4502b5958d433d16f0a8d296d3e9fa90b46.jpg)  
Fig. 2. (A) Interaction between computing architecture and model representation. (B) Interaction between problem instance and model representation

Finally, we question the appropriateness of the commonly used “least solution time” criterion for algorithmic performance, in light of the emerging computational paradigm known as metacomputing (or grid computing). Metacomputing utilizes the idle time of heterogeneous, geographically dispersed computers, and can result in a powerful, but relatively inexpensive, computational resource. Recent reports [2,26] place a metacomputer among the 10 fastest computers in the world. Further, their time can also be “sold” to potential buyers of CPU time (see, for example, Ref. [17]). In this context, therefore, a solution strategy should take into account the twin objectives of solution time and solution cost. In particular, it should be assessed whether the decrease in solution time through the use of additional resources is worth the extra dollars expended. Experiment 4 highlights this trade-off between the two objectives. If solution time was the only consideration, the 12-processor solution will be chosen. On the other hand, since the 6- and 8-processor solution times are not that much larger, cost considerations might suggest using fewer than 12 processors.

## 5.2. Summary

The above discussion suggests the following enhancements to model management systems: alternative model representations should be included in the model mix; interactions between model representation and computing architecture should be considered during model choice; solver distribution should include partial parallelization options in addition to the extremes of serial solution and full parallelism; and, finally, in a metacomputing environment, computational cost should be made an additional criterion for evaluating solver performance.

Note that, in current MMS frameworks, the model distribution subsystem (MDS) determines the deployment of solvers across a distributed architecture following the selection of the model type in the model consultation subsystem (MCS) (p. 331, of [19]). However, as seen in our computational results, model choice and solver distribution should be interrelated, not independent, decisions. In other words, the MMS must address this question: What combination of model and computing capacity results in best solver performance? Current MMS frameworks handle this issue by providing computational complexity measures (CMs) up front to the analyst [19]. While we acknowledge the difficulty of addressing model choice and solver distribution simultaneously, we contend (see next section) that there may be a better alternative to the mere provision of CMs.

The implications of our results for MMS design can be stated by making two changes to the MMS framework given in Mayer [19]. With MDS, an additional feature must be to decide on the number of solvers instances that must be used for a given problem. For MCS, an MMS must identify the representation that would be appropriate for a given capacity. Finally, in Mayer, the link between MCS and MDS was represented by a dotted arrow. We prefer to represent this link by two solid arrows, signifying the crucial nature of the interrelationship between model selection and solver distribution. The next section outlines an approach that can be used to facilitate the enhanced design.

## 6. Exploratory approach for predicting performance

Our computational experiments have highlighted the importance of designing MMS modules that take into account the interactions between model representation, computing capacity and solver performance. In order to actually implement such a design, however, the computational profile (i.e., the solution times across the different representations for various levels of computing capacity) must be predictable in advance. Our approach to accomplishing this is through the use of a timing model [13,14]. A timing model can be described as a mathematical characterization that accounts for the total time spent by the algorithm by relating it to various parameters such as model size, model representation, computing capacity, and computing architecture. Under this approach, scaled-down versions of a model are first solved and, by using statistical analysis on the observed patterns, a functional form relating performance to model and environment is derived. Then, when faced with a larger model instance, the optimal representation and capacity level can be derived by extrapolating this functional relationship.

Our goal in this section is to investigate whether the timing model approach has the potential to facilitate the proposed enhancements to MMS. First, we formulate an optimization model for finding the best representation and capacity to be used in solving a given instance of model (M). (Similar models can be developed for other problem classes.) The purpose of this formal model statement is to frame the subsequent discussion, and to emphasize the broad scope of the issues involved in attempting to predict algorithmic performance. In view of the difficulty of this model, no attempt has been made to date to solve this type of optimization problem exactly for any problem class. The closest solution proposals have called for the use of CMs to infer solver performance. We adopt instead a twostage, heuristic approach (best representation first, then best capacity) that is intended to demonstrate the superiority of timing models over the CM-approach. In the ensuing analysis, we narrow down the scope of the timing model to only a subset of the issues specified in the optimization model. Fortunately, our computational experiments show that even this restricted timing model is quite an adequate predictor of performance—its errors are all within reasonable bounds. Next, the two stages of the timing model approach are discussed, respectively, in Section 6.2 (for finding the best representation) and Section 6.3 (for finding the best capacity level, in terms of number of processors). Limitations of this approach and some avenues for future work are discussed in Section 6.4.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$P$ $(= |\mathrm{Psite} |)$ is the number of processors,  
$m_0$ is the number of master rows,  
$n$ is the number of natural subproblems,  
$m_{\mathrm{n}}$ is the number of rows in a natural subproblem, and  
$d_{\mathrm{n}}$ is the number of rows in a natural subproblem.
</div>

6.1. An optimization model for best representation and capacity

In a distributed-computing application, data is allocated across a network of computers, so as to minimize communication and storage costs. Using this data distribution for model (M), problem-specific data such as demands, capacities and bounds (for each representation) is then extracted from the raw data. In the model below, we assume that the above steps are completed, and that we are given an available set of processors. Our decision then is to determine an appropriate representation of the problem instance and an allocation of the available computing resources for its solution, so as to minimize some function of the system resources (e.g., CPU time, cost to solve to solve the problem, etc.—we will use CPU time). The processors themselves can belong to a traditional tightly coupled system or, alternatively, to a loosely coupled gridcomputing (or metacomputing) infrastructure such as Condor [4].

Our model is especially significant to grid systems because such systems are characterized by ever-changing resources. Grid-based solutions of optimization problems have been reported in the literature. One example is NEOS–Condor system [5] in which the front-end (NEOS) reads the problem from the user and spawns the appropriate programs to the distributed resource management system (Condor) which, in turn, hunts for idle processors on the grid to run the specified programs. In NEOS–Condor, all of this takes place without exploiting problem characteristics, and without considering whether the extra usage of computing resources would improve solution time. An enhanced MMS design can serve as an intermediary between NEOS and Condor: once the problem specifications are provided to NEOS, MMS takes over, and uses the model to determine the optimal allocation of subproblems to processors (and in turn the corresponding submatrices that must be distributed on each processor).

Given this background, we develop a model that provides, for each representation, the capacity utilization that will minimize solution time (see Appendix A). By running this model for each representation, we can obtain both the optimal representation and capacity for a problem instance.

From the list of variables given in Appendix A, we drop the representation index t, and use the following notations in Sections 6.2 and 6.3. So,

Further, in our experiments, since load balancing is a crucial to reducing the solution time (see Experiment 4 in Section 4.2), we have allocated the same number of subproblems to each processor $( \mathrm { i } . \mathrm { e } _ { \cdot } , b _ { j }$ is the same for all processors j). Hence, let

b be the blocking factor, $m _ { \mathrm { s } } ( = \mathrm { b m } _ { \mathrm { n } } )$ be the number of rows in a blocked subproblem and

$d _ { \mathrm { s } } \left( = d _ { \mathrm { n } } / b \right)$ be the density of rows in a blocked subproblem.

## 6.2. Stage I: optimal representation

A series of random instances of (M) was generated by varying $| I | , | J | ,$ and |K| from 5 through 8 (yielding $4 \times 4 \times 4 = 6 4$ instances). Each instance was then represented by each of the three permutations (Perm(I), Perm (J), Perm(K)), and solved using both serial and parallel processing, to obtain $1 9 2 \ ( = 6 4 \times 3 )$ parallel solution times (with $P { = } n )$ and 192 serial solution times. Fig. 3 shows the serial solution times plotted against model dimensions (number of master problem rows, number of subproblem rows, and number of natural subproblems). From this figure, one can observe the very striking relationship between the solution times and model dimensions. (The graph for the parallel solution times is similar and is omitted.)

![](/api/attachments/5682PFGQ/fulltext/images/ee315bd14dea7d8811d7116e029cb4a6a348a83c87506bf8d3fdbf66ba36e1ff.jpg)  
Fig. 3. Serial solution times versus model dimensions.

## 6.2.1. Model development

In order to derive a functional relationship of solution time versus model dimensions, we first note the wellknown result that the observed computational effort required for the simplex method is bounded polynomially in the number of rows, i.e., $O ( m ^ { k } )$ where k is small (see, for example, Todd [25]). Since the DW algorithm is just an iterative application of the simplex method between a master problem and multiple subproblems, we postulate that an appropriate estimate of effort for DW is of the form:

$$
\text { Solution   Time } = \beta_ {0} ^ {\prime} m _ {0} ^ {\beta_ {1}} P ^ {\beta_ {2}} m _ {\mathrm{s}} ^ {\beta_ {3}},\tag{7}
$$

which after applying the logarithmic linearizing transformation becomes $( \beta _ { 0 } \equiv \mathrm { L n } ( \beta _ { 0 } ^ { \prime } ) )$ :

$$
\begin{array}{c} \text { Ln(Solution   Time) } = \beta_ {0} + \beta_ {1} \text { Ln } (m _ {0}) + \beta_ {2} \text { Ln } (P) \\ + \beta_ {3} \text { Ln } (m _ {\text { s }}). \end{array}\tag{8}
$$

Before testing whether this hypothesized model fits our observations, we segregated the data into two subsets, one containing the 128 runs pertaining to Perm(I) and Perm(K) (henceforth called IK-data), and the other consisting of the remaining 64 points corresponding to Perm(J) (J-data). This segregation was based on the observation that the solution times for the IK-data were several orders of magnitude higher than the J-data times. Then, to determine whether any of the parameters in the hypothesized model (7) can be excluded from further consideration, we plotted scatter diagrams of the two data subsets. Based on this, the following conclusions were reached:

1. For the IK-data, both serial and parallel solution times increased superlinearly with $m _ { 0 }$ and $m _ { \mathrm { s } }$ (see an example plot in Fig. 4A), and increased sublinearly with P. Thus, all parameters were included for further analysis with this data set.

2. For the J-data points, serial solutions times increased superlinearly with $m _ { 0 }$ and $m _ { \mathrm { s } } ,$ , and increased

A  
![](/api/attachments/5682PFGQ/fulltext/images/e9739d0c379547bf173f8b46f7d46716d56727a25c7704e14ca281ad18984c5f.jpg)

B  
![](/api/attachments/5682PFGQ/fulltext/images/84d40981dac9ef2660c3b214203a17595b52aaabeae741c6830aeb4241491597.jpg)  
Fig. 4. Scatter plots for the partitioned data. (A) Superlinear increase for IK-data with number of master rows. (B) Lack of pattern for parallel J-data with number of processors.

sublinearly with P. However, model (M) has the characteristic in which the number of natural subproblem rows under Perm(J) is always the same as the number of master rows. Hence, we drop $m _ { \mathrm { s } } ,$ and use $m _ { 0 }$ and $P$ for further analysis of the $J \mathrm { - d a t a ^ { \prime } s }$ serial times. (Each natural subproblem under Perm(J) contains the rows corresponding to each commodity. Later, in our experiments in Section 6.3, wherein rows corresponding to multiple commodities are grouped into a subproblem, this equality between $m _ { \mathrm { s } }$ and $m _ { 0 }$ would not hold.)

3. Observation (2) holds for the parallel times of the $J _ { - }$ data as well, except that there was no discernible trend with $P$ (see Fig. 4B). Hence, we performed further analysis of J-data's parallel times with $m _ { 0 }$ only.

We then ran linear regression with the data points and parameters mentioned above. For the IK-data, we observed a few outliers (i.e., with standardized residuals greater than 2.5). Following suggestions in the literature

IK-data:

[27], these outliers were removed and the regression was re-run to obtain the following results (note: numbers in the tables are scaled-down by a factor of 10,000, but numbers in Eqs. (9)–(12) have not been scaled).

$$
\begin{array}{c} \mathrm{Ln(Serial Time)} = -4.442 + 3.328\mathrm{Ln}(m_{0}) + 0.566\mathrm{Ln}(P) + 1.179\mathrm{Ln}(m_{\mathrm{s}})\\ (R^{2} = 96.1\%) \qquad \qquad (p <   0.001)\qquad (p <   0.001)\qquad (p <   0.001) \end{array}\tag{9}
$$

$$
\begin{array}{c} \text {Ln(Parallel Time)} = - 5. 0 2 4 + 3. 4 3 0 \mathrm{Ln} (m _ {0}) + 0. 5 4 0 \mathrm{Ln} (P) + 1. 2 1 4 \mathrm{Ln} (m _ {\mathrm{s}}) \\ (R ^ {2} = 9 5. 9 \%) \quad (p <   0. 0 0 1) \quad (p <   0. 0 0 1) \quad (p <   0. 0 0 1) \end{array}\tag{10}
$$

J-data:

$$
\begin{array}{c} \text {Ln(Serial Time)} = 2.534 + 2.350\text{Ln}(m_0) + 0.837\text{Ln}(P) \\ (R^2 = 68.6\%) \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ (p <   0.001) \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \end{array}\tag{11}
$$

$$
\begin{array}{c} \operatorname{Ln} (\text {Parallel Time}) = 4.072 + 2.113 \operatorname{Ln} (m _ {0}) \\ (R ^ {2} = 40.0 \%) \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad (p <   0.001) \end{array} .
$$

## 6.2.2. Model validation

First, we wanted to test how well (9)–(12) predicts the best representation. For this purpose, we consider the five average times (of each representation) given in Experiments 1 through 3 (see Tables 1–3)). Table 6 gives the dimensions of the problems, the observed and predicted best representation, and the corresponding times in cases where there are agreements in the best representation. We observe that the model predicts the best representation in four out of five cases, and when the dimensions of the experimental problems are comparable to the 192 benchmark problems, the absolute error in prediction is quite small (see the shaded portion of the table).

Because of this last observation, we needed to test whether our model can predict the solution times of larger problem instances that are scaled-up from our 192 benchmark set. For this purpose, fifteen random problems (5 per representation) were generated. For each representation, the size of the corresponding index set was varied from 9 through 17, in steps of 2, while keeping the

<sub>ð</sub><sup>12</sup><sub>Þ</sub>

## Table 6

Inference of optimal representation

<table><tr><td rowspan="2">Experiment</td><td rowspan="2">|I|, |J|, |K|</td><td colspan="2">Best representation</td><td colspan="2">Solution times</td></tr><tr><td>Observed</td><td>Predicted</td><td>Observed</td><td>Predicted</td></tr><tr><td>1.</td><td>Serial</td><td>10, 2, 15</td><td>Perm(K)</td><td>Perm(J)</td><td></td></tr><tr><td rowspan="2">2.</td><td>Serial</td><td>20, 2, 30</td><td>Perm(J)</td><td>Perm(J)</td><td>372</td></tr><tr><td>Parallel</td><td>20, 2, 30</td><td>Perm(J)</td><td>Perm(J)</td><td>308</td></tr><tr><td rowspan="2">3.</td><td>Serial</td><td>8,10, 8</td><td>Perm(J)</td><td>Perm(J)</td><td>34</td></tr><tr><td>Parallel</td><td>8, 10, 8</td><td>Perm(J)</td><td>Perm(J)</td><td>16</td></tr></table>

|I|, |J| and |K| for the 192 benchmark set range from 5 through 8.

other two index sets constant at 8 (e.g., for Perm(I), |I| was varied, while |J| and |K| were kept constant). This variation implies that the largest problem generated had at least 1.5 times as many rows as the benchmark set. This way, we have a good test of the timing model.

The results, displayed in Table 7, show that the average inferential errors for these problems are all less than 25%. Since the coefficients of determination in (9)–(12) are also generally high, this validates our approach for predicting solution times across representations. Using the predicted times, the optimal representation can be picked by an analyst, or even automatically obtained by an enhanced MMS.

## 6.3. Stage II: optimal capacity

As seen in Experiment 4, rather than employing one processor to solve each natural subproblem (full parallelism), it may often be computationally advantageous to combine multiple subproblems into “blocks” (partial parallelism). This leads naturally to the question: What is the optimal number of processors (equivalently, computing capacity) to be used in order to minimize solution time? Here, we develop a timing model approach to answer this question for the Perm(J) representation as an example.

## 6.3.1. Model development

According to our discussion in Section 6.1, $m _ { \mathrm { s } } { = } b$ $m _ { \mathrm { n } } { = } ( n / P ) m _ { \mathrm { n } }$ . Thus, $P { m _ { \mathrm { { s } } } } \mathrm { { = } } n { m _ { \mathrm { { n } } } } ,$ , which is a constant for a given model instance. Therefore, as P increases, $m _ { \mathrm { s } }$

decreases. However, interprocessor communication (IPC) increases when P increases. This tradeoff between the decrease in $m _ { \mathrm { s } }$ and the increase in IPC explains the rough bowl shape obtained in Experiment 4, and it also suggests a polynomial relationship between solution time and P. It should be noted that such a relationship was absent in the experiments in Section $6 . 2 ,$ where P and $m _ { \mathrm { s } }$ were not correlated. Our investigation in this section is, therefore, based on a different data set-one drawn from Experiment 4. In particular, we consider 17 runs, six corresponding to $\vert I \vert = 1 0 , \ \vert J \vert = 2 4 , \ \vert K \vert = 1 0$ and P = 2, 4, 6, 8, 12, 24, another six corresponding to $\left| I \right| =$ $1 5 , | J | = 2 4 , | K | = 1 5$ and $P { = } 2 , 4 , 6 , 8 , 1 2 , 2 4$ , and a third five for $\lvert I \rvert = 2 0 , \lvert J \rvert = 2 4 , \lvert K \rvert = 2 0 , P = 4 , 6 , 8 , 1 2 , 2 4$ (see Table 8 for problem dimensions). The following polynomial fit was then obtained for this data:

$$
\begin{array}{r l} \text {Parallel Time} & = 519.241 + 25.736m_{0} - 420.366P + 31.74P^{2} - 0.71P^{3} \\ (R^{2} = 80.6\%) & \quad (p <   0.001) \quad (p = 0.02) \quad (p = 0.07) \quad (p = 0.12) \end{array}
$$

## 6.3.2. Model validation

To validate the efficacy of this model in prediction, we conducted 8 runs. First, we generated two random scaledup problems with |I|=25, |J|=24 and |K|=25. Then, each problem was solved with P= 6, 8, 12, and 24, and then, the average solution time over the two problems was obtained for each value of P. The last column in Table 8 shows the master and blocked subproblem rows for these problems, and Table 9 shows the observed and predicted average times for the eight runs. We see that our model predicts the optimal number of processors correctly, and is subject to an average error of 15% in predicting the solution times for these problems.

## 6.4. Discussion

Although our timing-model approach for prediction of potential algorithmic performance yields high $R ^ { 2 }$ in

Table 7 Inference of solution times

<table><tr><td>Representation</td><td>|I|, |J|, |K|</td><td>Absolute % error (serial)a</td><td>Absolute % error (parallel)a</td></tr><tr><td rowspan="5">Perm(I)</td><td>9, 8, 8</td><td>28.53</td><td>29.99</td></tr><tr><td>11, 8, 8</td><td>16.21</td><td>16.05</td></tr><tr><td>13, 8, 8</td><td>38.20</td><td>38.95</td></tr><tr><td>15, 8, 8</td><td>6.03</td><td>5.35</td></tr><tr><td>17, 8, 8</td><td>27.82</td><td>27.31</td></tr><tr><td>Average</td><td></td><td>23</td><td>24</td></tr><tr><td rowspan="5">Perm(J)</td><td>8, 9, 8</td><td>22.68</td><td>48.00</td></tr><tr><td>8, 11, 8</td><td>29.78</td><td>8.37</td></tr><tr><td>8, 13, 8</td><td>0.71</td><td>28.24</td></tr><tr><td>8, 15, 8</td><td>44.17</td><td>22.99</td></tr><tr><td>8, 17, 8</td><td>29.44</td><td>1.58</td></tr><tr><td>Average</td><td></td><td>25</td><td>22</td></tr><tr><td rowspan="5">Perm(K)</td><td>8, 8, 9</td><td>8.12</td><td>8.65</td></tr><tr><td>8, 8, 11</td><td>26.59</td><td>27.21</td></tr><tr><td>8, 8, 13</td><td>0.03</td><td>0.11</td></tr><tr><td>8, 8, 15</td><td>7.15</td><td>6.52</td></tr><tr><td>8, 8, 17</td><td>20.24</td><td>19.90</td></tr><tr><td>Average</td><td></td><td>12</td><td>13</td></tr></table>

<sup>a</sup> Based on Eqs. (9)–(12).

<sub>ð</sub><sup>13</sup><sub>Þ</sub>

general, and average prediction errors that are no more than 25%, more work needs to be done to make the timing model approach robust and widely applicable. Below, we discuss some important limitations.

First, the results described above are for a single problem class, although there are some positive indications for external validity of the timing model approach. For example, Ho and Sundarraj [13] developed a timing model for the revised simplex method and validated it on 35 different linear programs drawn from 19 different application areas that range from food industry to electricpower industry. As with the application of timing models described here, they also found that the use of timing models yields significant savings in solution time.

Second, although we derived our timing model by using over 200 test problems, the index sets used in those problems were limited in range, mainly due to the limitations of the parallel Dantzig–Wolfe solver used in this study. A better sampling design, and a more thorough examination of all relevant parameters, including ones omitted in this study (e.g., nonzero density, solver characteristics) could result in a more robust methodology. While more work needs to be done, the timing model approach is promising enough for us to envisage at least one immediate application. In a number of situations, the same model needs to be run over and over, albeit with different data values. For such cases, a timing model, once derived, can be used to predict the solution times for various computational strategies, and to choose the best alternative for solving the model instance at hand.

Finally, in Section 4, we emphasized the importance of choosing model representation and computing capacity simultaneously, while acknowledging the difficulty of this decision. Although our timing model approach falls short of this goal, as do all of the current MMS frameworks (since they propose CMs), we believe that our approach is superior. CMs are widely acknowledged [15] to suffer from significant gaps in the inference of actual algorithmic behavior. A pertinent case is the simplex algorithm, which has an exponential worst-case bound, but whose empirical performance is typically polynomial. Further, even in cases in which the complexity bound is polynomial (e.g., interior-point methods for linear programming), researchers acknowledge the wide errors between the theoretical bounds and actual performance. By contrast, timing models are based on empirically observed performance and, hence, their use should represent an advance over current MMS designs.

Table 8  
Problem dimensions for optimal capacity experiment

<table><tr><td rowspan="2">P</td><td colspan="4"> $(m_0, m_s)$  for  $|I|, |J|, |K|$ </td></tr><tr><td>10, 24, 10</td><td>15, 24, 15</td><td>20, 24, 20</td><td>25, 24, 25</td></tr><tr><td>2</td><td>(40, 480)</td><td>(60, 720)</td><td> $(80, 480)^a$ </td><td> $(100, 480)^a$ </td></tr><tr><td>4</td><td>(40, 240)</td><td>(60, 360)</td><td>(80, 480)</td><td> $(100, 240)^a$ </td></tr><tr><td>6</td><td>(40, 160)</td><td>(60, 240)</td><td>(80, 320)</td><td>(100, 160)</td></tr><tr><td>8</td><td>(40, 120)</td><td>(60, 180)</td><td>(80, 240)</td><td>(100, 120)</td></tr><tr><td>12</td><td>(40, 80)</td><td>(60, 120)</td><td>(80, 160)</td><td>(100, 80)</td></tr><tr><td>24</td><td>(40, 40)</td><td>(60, 60)</td><td>(80, 80)</td><td>(100, 40)</td></tr></table>

<sup>a</sup> Indicates that subproblem dimensions exceeded that allowed by the code.

## 7. Concluding remarks

In this paper, we studied the interactions between model representation, computing capacity, and algorithmic performance, by conducting a series of experiments on an illustrative linear programming model, namely, the multi-commodity version of the familiar transportation problem. Our computational results obtained on a parallel, decomposition-based solver indicate the interactions are quite significant and have important implications for MMS design.

The contributions of our work are as follows. First, our research has elicited that a subtler element of model selection, namely alternative model representations, is important and yet not considered (explicitly) in the distributed MMS literature. Second, the finding that computing capacity affects model selection and vice versa contributes to the viewpoint that, in order to minimize solution time, the MCS and MDS decisions must be interlinked and undertaken simultaneously. Third, to address these decisions, we have proposed an approximate timing-model approach which, despite certain limitations, appears superior to the current practice of using worst-case bounds as a predictor of potential algorithmic performance. Fourth, our experiments suggest that, in addition to solution time, the design of a MMS must consider computational cost in dollar-terms, especially in the context of a commercial metacomputing environment in which computing capacity can be purchased over the Internet.

Table 9  
Prediction of optimal capacity

<table><tr><td>Observed times</td><td>Predicted times</td><td>% Error</td></tr><tr><td>1928.5</td><td>1559.925</td><td>19.1</td></tr><tr><td>1438.5</td><td>1397.753</td><td>2.8</td></tr><tr><td>1024.5</td><td>1392.129</td><td>35.9</td></tr><tr><td>1423.5</td><td>1471.257</td><td>3.4</td></tr><tr><td>Average</td><td></td><td>15</td></tr></table>

We conclude this paper with some suggestions for future work. First, although our results are promising, the scope of the experiments should be expanded to include more test problems, a wider range of variation in the data, and additional causal variables. The experiments must also consider other problem classes that are amenable to alternative representations. Finally the scope of our paper is limited to treating computing capacity as the number of processors. An expanded view of computing capacity that includes additional factors (e.g., storage or other specialized needs) would be a useful extension.

## Appendix A

In Section 6.1, we discussed how an enhanced MMS could be designed by incorporating an allocation model that assigns, for each representation, multiple natural subproblems to a processor; the combined set of natural subproblems on a processor shall be referred to as a “blocked” subproblem. The purpose of this appendix is to develop an optimization allocation model for a given representation t. We minimize the overall solution time, which is the sum of two components, namely, the communication time and the computational time.

Our model adapts ideas from Purao et al. [23,24], although there are certain differences. First, unlike the base model in the aforementioned literature which provides for communication among all object–fragment pairs, the interprocessor communication in our case is only between the master and each of the subproblems. Second, we do not consider storage costs, but instead consider computational time, since time-minimization is an important criterion of this research. As seen in Section 4.2, computational time is dependent on the number of subproblems allocated to each processor.

For a given representation t, let:

$m _ { 0 } ^ { t }$ Number of rows in the master problem $d _ { 0 } ^ { t }$ Nonzero density of the master problem $m _ { \mathrm { n } } ^ { t }$ Number of rows in any natural subproblem $d _ { \mathrm { n } } ^ { t }$ Nonzero density of any natural subproblem DSites Set of natural subproblems (i.e., data sites) (indexed by $i ^ { \prime } s ; i { = } 0$ indicates master)

PSites Set of available processor sites (indexed by j's) PickP<sub>j</sub> 1 if some data site is allocated to processor site j; 0 otherwise

$\mathrm { A l l o c D P } _ { i , j }$ 1 if data site i is allocated to processor $j ; 0$ otherwise

AssignD Index of the processor site allocated to data site $i , \mathrm { i } . \mathrm { e } . , j$ such that $\mathrm { A l l o c D P } _ { i , j } { = } 1$

$b _ { j } ^ { t }$ Number of natural subproblems allocated (i.e., blocked) to processor site j

$m _ { \mathrm { s } , j } ^ { t }$ Number of rows in the blocked subproblem at processor site $j ; m _ { \mathrm { s } } ^ { t } \equiv ( m _ { \mathrm { s , l } } ^ { t } , . . . , m _ { \mathrm { s , l P S i t e } } ^ { t } )$

$d _ { \mathrm { s } , j } ^ { t }$ Nonzero density of the blocked subproblem at processor j; $d _ { \mathrm { s } } ^ { t } \equiv ( d _ { \mathrm { s , 1 } } ^ { t } , . . . , d _ { \mathrm { s , | P S i t e | } } ^ { t } )$

$\mathrm { C o m m P P } _ { j 1 , j 2 }$ Time to communicate a single data element from processor site $j _ { 1 }$ to processor site $j _ { 2 }$

BigM A sufficiently large number

Model

$$
\begin{array}{l} \text { Min } \sum_ {j} m _ {\mathrm{s}, j} ^ {t} \text { CommPP } _ {j, \text { AssignD } _ {0}} \\ + \sum_ {j} m _ {0} ^ {t} \text { PickP } _ {j} \text { CommPP } _ {j, \text { AssignD } _ {0}} + f (m _ {0} ^ {t}, d _ {0} ^ {t}, m _ {\mathrm{s}} ^ {t}, d _ {\mathrm{s}} ^ {t}) \end{array}\tag{A.1}
$$

s.t.

$$
\sum_ {j} \operatorname{AllocDP} _ {i, j} = 1 \quad \text {   for   all   } i\tag{A.2}
$$

$$
b _ {j} ^ {t} = \sum_ {i} \operatorname{AllocDP} _ {i, j} \quad \text {   for   all   } j\tag{A.3}
$$

$$
\sum_ {i} \operatorname{AllocDP} _ {i, j} \leq \text { BigM } ^ {*} \text { PickP } _ {j} \quad \text {   for   all   } j\tag{A.4}
$$

$$
\operatorname{AssignD} _ {i} = \underset {j \in \text { PSite }} {\arg} \left\{\operatorname{AllocDP} _ {i, j} \right\} \quad \text { for   all } i\tag{A.5}
$$

$$
d _ {\mathrm{s}, j} ^ {t} = \left(d _ {\mathrm{n}} ^ {t} * (m _ {\mathrm{n}} ^ {t}) ^ {2}\right) / (m _ {\mathrm{s}, j} ^ {t}) ^ {2} \quad \text {   for   all   } j\tag{A.6}
$$

$$
m _ {\mathrm{s}, j} ^ {t} = m _ {\mathrm{n}} ^ {t} * b _ {j} ^ {t} \quad \text {   for   all   } j\tag{A.7}
$$

$$
\operatorname{AllocDP} _ {i, j} = \text { binary } \quad \text {   for   all   } i, j\tag{A.8}
$$

$$
\operatorname{Pick} \mathrm{P} _ {j} = \text { binary } \quad \text {   for   all   } j.\tag{A.9}
$$

The objective comprises both the communication cost as well as the computational time. The first component of the objective deals with communications from each block-processor site to the master-processor site: we multiply the unit communication cost by the number of rows in the blocked subproblem, on the assumption that a greater number of rows implies a larger requirement for information transfers between these sites. The second term accounts for the communication from the master to the subproblem sites. The third term is a function that provides the computational time, given the distribution of natural subproblems into blocks. It should be pointed out that when a certain processor site j has no subproblem allocation, $b _ { j } ^ { t }$ and in turn $m _ { \mathrm { s } , j } ^ { t }$ would both be 0.

Constraint (A.2) ensures that every data site is allocated to a processor. Constraint (A.3) computes the number of blocks allocated to each processor, (A.4) determines if there is any allocation to processor $j ,$ and (A.5) determines the site allocated to given subproblem or master problem. Constraints (A.6) and (A.7) compute the blocked subproblem density and subproblem rows at each processor site, and (A.8) and (A.9) require the variables to be binary.

The solution to the above model for all problem representations of model (M) gives the optimal representation–capacity combination for a given problem instance.

## References

[1] R.M. Burton, B. Obel, Designing Efficient Organizations: Modelling and Experimentation, North-Holland, Amsterdam, 1984.

[2] CNN, World's fastest computer simulates earth, 2002, http:// www.cnn.com/2002/TECH/biztech/11/15/fastest.computer.ap/ index.html.

[3] G.B. Dantzig, P. Wolfe, The decomposition algorithm for linear programs, Econometrica 29 (4) (1961) 767–778.

[4] D.H.J. Epema, M. Livny, R. van Dantzig, X. Evers, J. Pruyne, A worldwide flock of Condors: load sharing among workstation clusters, Future Generations Computer Systems 12 (1) (1996) 53–65.

[5] M.C. Ferris, M.P. Mesnier, J.J. Moré, NEOS and Condor: solving optimization problems over the Internet, ACM Transactions on Mathematical Software 26 (1) (2000) 1–18.

[6] I. Foster, C. Kesselman (Eds.), The Grid: Blueprint for a New Computing Infrastructure, Second edition, Morgan Kaufman, 2004.

[7] I.C. Foster Kesselman, S. Tuecke, The anatomy of the grid: enabling scalable virtual organizations, International Journal of Supercomputer Applications 15 (3) (2001) 200–222.

[8] M.R. Garey, D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, Freeman, San Francisco, 1979.

[9] A.M. Geoffrion, The SML language for structured modeling, Operations Research 40 (1) (1992) 38–75.

[10] S.K. Gnanendran, J.K. Ho, Load balancing in the parallel optimization of block-angular linear programs, Mathematical Programming 62 (1993) 41–67.

[11] W. Gropp, E. Lusk, A. Skjellum, Using MPI: Portable Parallel Programming with the Message-Passing Interface, The MIT Press, Cambridge, MA, 1994.

[12] J.K. Ho, E. Loute, Computational experience with advanced implementation of decomposition algorithms for linear programming, Mathematical Programming 27 (1983) 383–290.

[13] J.K. Ho, R.P. Sundarraj, A timing model for the revised simplex method, Operations Research Letters 13 (1993) 67–73.

[14] J.K. Ho, R.P. Sundarraj, Distributed nested decomposition of staircase linear programs, ACM Transactions on Mathematical Software 23 (2) (1997) 148–171.

[15] J. Hooker, Needed: an empirical science of algorithms, Operations Research 42 (2) (1994) 201–212.

[16] S. Huh, H. Kim, Q. Chung, Framework for change notification and view synchronization in distributed model management system, Omega 27 (1999) 431–443.

[17] Juno, Juno to harvest wasted CPU power, 2001, http://news.com. com/2100-1023-251978.html?legacy=cnet.

[18] R. Krishnan, K. Chari, Model management: survey, future research directions and a bibliography, ITORMS: Interactive Transactions of ORMS, 3(1), 2000, http://catt.okstate.edu sharda/docs/itorms/kchari/kchari/outline.html.

[19] M.K. Mayer, Future trends in model management systems: parallel and distributed extensions, Decision Support Systems 22 (4) (1998) 325–335.

[20] W.A. Muhanna, R.A. Pick, Meta-modeling concepts and tools for model management: a systems approach, Management Science 40 (9) (1994) 1093–1123.

[21] A. Pinar, Ü.V. Çatalyürek, C. Aykanat, M. Pinar, Decomposing linear programs for parallel solution, Lecture Notes in Computer Science, vol. 1041, Springer-Verlag, Heidelberg, Germany, 1996, pp. 473–482.

[22] S. Purao, H. Jain, D. Nazareth, Effective distribution of objectoriented applications, Communications of the ACM 41 (8) (1998) 100–108.

[23] S. Purao, H. Jain, D. Nazareth, An approach to distribution of object-oriented applications in loosely coupled networks, Journal of Management Information Systems 18 (3) (2002) 195–234.

[24] S. Purao, H. Jain, D. Nazareth, ODE: a tool for distributing object-oriented applications, Information and Management 39 (2002) 689–703.

[25] M. Todd, The many facets of linear programming, Mathematical Programming 91 (3) (2002) 417–436.

[26] Top500, Top 500 List for November 2002, 2002, http://www. top500.org/list/2002/11/.

[27] P. Vellman, D. Hoaglin, Applications, Basics and Computing for Exploratory Data Analysis, PWS Publishers, Belmont, CA, 1981.

[28] M. Zuo, W. Kuo, K.L. McRoberts, Application of mathematical programming to a large-scale agricultural production and distribution system, Journal of the Operational Research Society 42 (8) (1991) 639–648.
