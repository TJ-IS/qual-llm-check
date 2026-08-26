---
otero_id: 17287
otero_key: "2V6F85ZZ"
title: "DDM: Decision support system for hierarchical dynamic decision making"
authors: "Adedeji B. Badiru; P. Simin Pulat; Myungkoo Kang"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90002-k"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DDM: Decision support system for hierarchical dynamic decision making \*

Adedeji B. Badiru, P. Simin Pulat and Myungkoo Kang

University of Oklahoma, Norman, OK, USA

A simulation-based decision support system for AHP (Analytic Hierarchy Process) is presented in this paper. The software, named DDM (Dynamic Decision Making), is applicable to dynamic decision scenarios where probabilistic interactions exist between the factors in the AHP hierarchy. Decision scenarios are generated using probability information specified by the user. The output of the simulation is the relative frequency of the selection of each alternative rather than a single final selection. The decision maker will evaluate the distribution histogram and make final selection based on his or her own inherent disposition to risk. DDM can be used for forecasting or for evaluating strategic planning options.

Keywords: Decision support system, Forecasting, AHP, Simulation, Probabilistic factors, Decision making, Hierarchical decisions, Dynamic decision making, Probabilistic factors, Factor interactions, Scenario planning, Dependent factors

![](/api/attachments/2V6F85ZZ/fulltext/images/46416483b2e95960ec296accb14aed15dbfdffc54859d0b93dfd0016e13c58c1.jpg)

Adedeji B. Badiru, Ph.D, P.E. is an Associate Professor of Industrial Engineering at the University of Oklahoma. He received BS and MS degrees in Industrial Engineering and MS in Mathematics from Tennessee Technological University and Ph.D. degree in Industrial Engineering from the University of Central Florida. His areas of interest include project management, expert systems, and computer applications. He is the author of several books and papers on project management and expert systems. He is a member of lIE, SME, TIMS, ORSA, TIMS, PMI, and AAAI.
Correspondence to: A.B. Badiru, School of Industrial Engineering, University of Oklahoma, Norman, OK 73019, USA.
Tel: (405) 325-3721. Fax: (405) 325-7555.

## 1. Introduction

A simulated glimpse of the future is better than no glimpse at all!

Simulation is an effective tool for strategic decision making. Systems that are too critical or too obscure to be studied analytically can be successfully modeled by simulation approaches. A decision support system (DSS) that is based on simulation will be more robust than one that is based on static assumptions. The analytic hierarchy process (AHP) is a technique that has been widely used to solve complex decision problems. However, the conventional AHP takes a static view of the interactions between factors in a decision problem. In real world problems, decision factors interact in dynamic and probabilistic fashions. The occurrence level of each factor is uncertain and may depend on the occurrence levels of other factors. The implementation of AHP in a simulation environment considering probabilistic factor interactions can significantly enhance the quality of AHP-based decisions.

![](/api/attachments/2V6F85ZZ/fulltext/images/5910633ba75afa191c94816ddc51e8b959dc95605fd21dc8fd9f648a80401d3d.jpg)

![](/api/attachments/2V6F85ZZ/fulltext/images/360397e27586c1a1218332ca6f9841f07a26aa8b51320ce1121cdd22ecd447dc.jpg)  
Myungkoo Kang received his Ph.D. degree in Industrial Engineering from the University of Oklahoma. His areas of research include operations research and simulation. He received his BS in Mechanical Engineering from Korea Military Academy and his MS in Industrial Engineering from the University of Oklahoma.

P. Simin Pulat, Ph.D. is an Associate Professor of Industrial Engineering at the University of Oklahoma. She received MS and Ph.D. degrees in Operations Research from North Carolina State University. Her research interests include network optimization, mathematical programming, computer applications of optimization techniques, and multiple criteria decision making models. She is a senior member of the Institute of Industrial Engineers and Operations Research

Society of America.

\* Funding for the project was provided by the University of Oklahoma Energy Center.

We present a simulation-based decision support system for AHP. The system, named DDM (Dynamic Decision Making), is applicable to dynamic decision scenarios where probabilistic interactions exist between the factors in the AHP hierarchy. Decision scenarios are generated using probability information specified by the user. The output of the simulation is the relative frequency of the occurrence of each outcome rather than a single final selection. Each outcome is modeled as an alternative in the decision problem. The decision maker will evaluate the distribution histogram and identify the most likely outcome based on his or her own risk taking tendencies. The most likely outcome is referred to as the “selected alternative.” Forecasting is representative of the type of problems for which DDM was designed. Thus, forecasting is used in this paper as the basis for illustrating the application of DDM. Forecasting is very crucial to the evaluation of decision options in strategic planning environments $[23]$ .

## 2. Simulation and scenario planning

Conventional forecasting is based on static and certain relationships among the factors in the forecast problem. Forecasting results in single-value predictions. Scenario planning, by contrast, focuses on uncertainties in the forecast environment. Scenario planning generates probabilistic representations of the future. Our DDM software is based on scenario planning approach. Its development is based on the previous work of Pulat et al. [20], which addresses a probabilistic extension of the analytic hierarchy process (AHP). For the purpose of simulation, factors are referred to as events and subfactors are referred to as subevents. A scenario is defined as the set of events that are assumed to have occurred. Simulation is used to generate the events that occur. A set of weights are derived for each alternative based on a specific scenario. The alternative with the highest weight is selected for each scenario. Using the probability information on the events, a new scenario is generated and an alternative is selected. At the end of the simulation, the frequency of occurrence of each forecast alternative is displayed. Based on the frequency distribution, the decision maker will evaluate the likelihood of each decision alternative. A final decision can then be made based on the decision maker's risk handling tendencies.

## 3. Application of AHP to dynamic decision making

The analytic hierarchy process [32] facilitates the incorporation of qualitative and subjective considerations into quantitative factors for decision making. AHP is a practical approach to solving complex decision problems involving the comparisons of attributes or alternatives. The technique has been used extensively in practice to solve many decision problems $[1,3,4,6,10,14,15,18,21–39]$ . Zahedi [39], Golden et al. [10], and Vargas [34] present comprehensive surveys of the AHP technique and its various applications. Wind [37] presents an example of the application of AHP to marketing. Saaty and Vargas [26] discuss the estimation of technological coefficients by the analytic hierarchy process. Ramanujam and Saaty [22] present a detailed AHP approach to the assessment and selection of imported technology in less developed countries.

Wabalickis [36] presents the use of AHP for the justification of flexible manufacturing system. Banai-Kashani [3] presents an application of AHP to urban housing and transportation planning. Rahman and Frair [21] present an application of AHP to electric utility planning. The problem of long-range planning and AHP was addressed by Emshoff and Saaty [6]. Mustafa [18] applies AHP to the problem of industrial planning. Azani and Khorramshahgol [1] present the Analytic Delphi Method (ADM), which integrates the Delphi method of forecasting [15] and AHP for location planning. Khorramshahgol et al. [14] use AHP for project evaluation and selection. Cook et al. [4] present an extension of the AHP technique for urban economic forecasting. Liberatore [16] presents AHP application to project selection. The mathematical basis, procedures, and extensions of AHP are widely available in the literature [5,9,10,11,25,27,28,29,30,31,32,33,38]. The general approach to using AHP covers the following steps:

1. Develop the hierarchical structure for the decision problem.

2. Determine the relative weights of each alternative with respect to the characteristics and sub-characteristics in the hierarchy.

3. Determine the overall priority score of each alternative.

4. Determine the indicators of consistency in making pair-wise comparisons of the characteristics and alternatives.

5. Make a final decision based on the results.

The decision hierarchy in AHP is constructed so that factors at the same level are of the same class and can be related to factors at the next higher level. The top level of the hierarchy reflects the overall objective or focus of the decision problem. Criteria, factors, or attributes on which the final objective is dependent are listed at intermediate levels in the hierarchy. The lowest level in the hierarchy contains the competing alternatives through which the final objective might be achieved. After the hierarchy has been constructed, the decision maker must undertake a subjective comparison procedure to determine the weight of each factor at each level of the hierarchy. Pairwise comparisons are performed at each level to determine the relative importance of each factor at that level with respect to each factor at the next higher level in the hierarchy.

![](/api/attachments/2V6F85ZZ/fulltext/images/e271702f5b313213133eff072445bd4331b37d3b83dff4de097d6a2973c287fa.jpg)  
Fig. 1. Flowchart of AHP methodology (adapted from Badiru [2]).

Table 1
AHP weight scale

<table><tr><td>Weight scale</td><td>Interpretation</td></tr><tr><td>1</td><td>Equal importance</td></tr><tr><td>3</td><td>Weak importance of one over another</td></tr><tr><td>5</td><td>Strong importance of one over another</td></tr><tr><td>7</td><td>Very strong importance of one over another</td></tr><tr><td>9</td><td>Absolute importance</td></tr><tr><td>2, 4, 6, 8</td><td>Intermediate weights</td></tr><tr><td>Reciprocals</td><td>Represented by negative numbers</td></tr></table>

Table 1 presents the pair-wise comparison weight scale suggested by Saaty [32]. The translations of the importance weights, as suggested by Saaty [32], are presented below:

If factor A is equally important as factor B, then the importance rating of A over B is 1.

If factor A is weakly more important than factor B, then the importance rating of A over B is 3.

If factor A is strongly more important than factor B, then the importance rating of A over B is 5.

If factor A is very strongly more important than factor B, then the importance rating of A over B is 7.

If factor A is absolutely more important than factor B, then the importance rating of A over B is 9.

Intermediate numbers are used whenever appropriate to indicate intermediate levels of importance. If the comparison order is reversed (e.g. B versus A rather than A versus B), then the reciprocal of the importance weight is entered for the pair-wise comparison. Typically, the decision maker will need to go through several iterations of obtaining the subjective relative weights of the factors. Typical questions that are posed to elicit the subjective weights are:

"Do you consider Factor A to be more important than Factor B in the selection of a machine to achieve our goal?"

"If so, how much more important is it on a scale of 1 to 9?"

Similar questions are posed iteratively until each factor has been compared with each of the other factors. Fig. 1 shows a flowchart presented by Badiru [2] for the conventional AHP methodology. Interested readers should refer to [2,32,34,39] for further details on the AHP procedures shown in the flowchart.

In the conventional AHP, the alternatives are treated as choice variables. By contrast, our approach treats alternatives as possible outcomes subject to probabilistic interactions of factors in the decision problem. Our AHP simulation approach differs from conventional AHP software (e.g. EXPERT CHOICE [8] and NEWTECH from Expert Choice, Inc.) in that it accepts conditional probabilities of the occurrence of events. Also, we do not compare all subevents of each event with all subevents of the other events. Rather, we pairwise compare only a subset of the subevents. Sensitivity analysis of the relative priorities [17] can be conducted by running the simulation several times. Full details of the methodology are presented below.

## 4. DDM operational and systems requirements

DDM is a very interactive program. It is PC-based. This facilitates accessibility and ease of execution for users. It is written in C language. Thus, it is very portable on various computer systems. DDM runs on any PC compatible computer with EGA display unit and 640K RAM. The design of the system makes use of drop down menu structures. The program contains an on-line help from which a user can get clarification on the procedures and parameters involved in using the program. A demo program is also available to introduce users to the general operation of the program. The demo program uses a built-in AHP decision problem for its execution. The program operates in the following sequence:

User Input $\Rightarrow$ AHP Simulation

⇒ Distribution of Forecast Outcomes

The input requirements are the main events, sub-events, dependent set, independent events, conditional probabilities, forecast alternatives, and pair-wise comparison matrices. A dependent set is defined as the collection of two main events that are mutually dependent. The output of the simulation is a frequency histogram of the distribution of the forecast outcomes. Our simulation methodology is designed to minimize the amount of inputs required from the user.

An issue of concern is the nature and amount of data entry required from the user. It is noted that the premise of AHP and other similar approaches is to permit the subjectivity of the decision maker to be included in the methodology. In any risk-prone decision process (e.g. [7,12,13]), the decision maker must provide subjective rating of one factor relative to other factors. The larger the problem size, the bigger the burden of data entry. The subjective data entry requirements in multiattribute decision making has been a topic of research for many years [5,9,25,27,29,31,33,38]. There are a number of serious criticisms which have been debated concerning the practicality and efficacy of the AHP approach [5,38]. The major criticisms of AHP involve the validity of the subjective information provided by the decision maker.

Our approach is designed to address some of the prevailing criticisms dealing with the amount of pair-wise comparisons required to implement AHP for large problems. Our spanning tree approach helps in reducing what might, otherwise, be a large set of pair-wise comparisons. Our intention is to preserve the user subjectivity as conventionally granted by AHP. The user is not expected to provide perfect hierarchical or probability information. What DDM requires are subjective estimates based on historical data and/or the user's intuition, experience, risk averseness, and rational preferences. The simulation approach uses these estimates to generate composite measures that can aid the user in making and justifying specific decisions. Simulation is effective for problems that lack perfect information. Such problems are the focus of our DDM software.

The consistency ratio approach suggested by Saaty [11,32] is designed to overcome some of the concerns discussed above. Consistency refers to the consistency of the transitivity of the weight scales when multiple factors are compared. A discussion of the consistency ratio methodology is beyond the scope of this present paper. Interested readers should refer to [11,25,27,28,29,30, 32,38] for further details. In DDM, the check of the consistency ratio for a pair-wise comparison matrix is done internally. If a pair-wise comparison matrix is not consistent, the user is informed and he/she is requested to modify the comparison scales. To further reduce the burden of data entry, DDM provides an initial set of consistent weights for each pair-wise comparison matrix. The user then has the option of modifying the weights as desired. The example simulation run presented later in this paper illustrates the procedures for using DDM.

## 5. Development of the methodology

The objective is to predict the change in the base forecast as a function of qualitative factors which were not included in the forecast. The model consists of sets of independent events, dependent events, levels at which the events may occur, and alternatives defined as the possible variations in base forecast due to the occurrence of such events. The occurrence probabilities for the independent events and the conditional probabilities for the dependent events are provided by the user. The user also provides pairwise comparisons for the set of events generated by the procedure. Subevents in a scenario occur according to event probability distributions and the scenario is evaluated using the AHP approach. The AHP approach consists of defining a hierarchy and analyzing the factors at each level in terms of their impact on the factors at the higher level by means of pairwise comparisons. The pairwise comparisons are synthesized into an overall relative weight for each factor. The weights are then aggregated to derive a set of ratings for the alternatives. The alternative with the highest rating is selected. For the development of our simulation methodology, we define the following notations:

$A_{i}$ Alternative i $M_{i}$ Main Event i $E_{iu}$ Subevent u of Event i $P_{iu}$ Probability that $E_{iu}$ will occur $w_{ab}^{iu}$ Likelihood of Alternative a over Alternative b with respect to $E_{iu}$ $d_{ij}$ Overall significance of $M_{i}$ over $M_{j}$ $c_{uv}^{ij}$ Relative significance of $E_{iu}$ over $E_{jv}$ $E'_{iu}$ Subevent u of the event in the i'th position of the rearranged sequence of events $c'_{uv}^{ij}$ Relative Significance of $E'_{iu}$ over $E'_{jv}$

$x_{a}^{iu}$ Relative weight of alternative $a$ with respect to $E_{iu}$

$S_{k}$ $k^{\prime}$ th scenario

$e_{iu}(S_k)$ Relative weight of $E_{iu}$ calculated with respect to $S_{k}$

$z_{iu}$ Ratio of relative weight of $E_{iu}$ to relative weight of root node, $E_{12}(z_{12} = 1)$

$C(A_{i})$ Composite weight for alternative $a_{i}$

Fig. 2 presents a general model of the AHP problem. The highest hierarchy specifies the objective of the problem, which is to estimate changes in a base forecast. The second level contains a set of events which affect the objective. These events are further broken down to subevents contained in the third level. The fourth level contains the decision alternatives, such as the forecasted percent change from the base forecast. The main events (level 2) may be probabilistic in nature. In Fig. 2, Event 3 depends on Event 2 and Event 4 depends on Event 3. Each main event has a certain number of sub-events. The number of sub-events don't have to be equal for all main events. The definition of the alternatives is based on the alternatives used by Saaty and Gholamnezhad [24] for forecasting oil prices.

Factors are referred to as main events, factor levels are referred to as sub-events, and alternatives are referred to as forecast outcome. We have to assign probabilities to each subevent. Based on the notations above, we have:

$$
P (E _ {i u}) = P _ {i u}, \forall E _ {i u},\tag{1}
$$

where $E_{iu}$ denotes Subevent u of Event i. The occurrence of an event may be dependent on another event. In Fig. 2, events 1 and 2 are independent events and events 3 and 4 are dependent events. Event 3 depends on event 2 and event 4 depends on event 3. Information on $E_{iu}$ will affect the likelihood of $E_{jv}$ if $M_{j}$ is dependent on $M_{i}$ . Therefore, we incorporate conditional probabilities, $P(E_{jv} | E_{iu})$ , for all dependent events i, j and their respective subevents u, v. The next step is pairwise comparison of alternatives (level 4) for each $E_{iu}$ . We let $w_{ab}^{iu}$ denote the importance of Alternative a over Alternative b with respect to $E_{iu}$ . The conventional weight scale [32] presented earlier in Table 1 is adopted for $w_{ab}^{iu}$ .

The relative importance of subevents of Event i over subevents of Event j are also needed for the computation of final composite weights for each alternative. We define $c_{uv}^{ij}$ as the relative importance of $E_{iu}$ over $E_{jv}$ in accordance with the weight scale described in Table 1. It is practically impossible for the user to input $c_{uv}^{ij}$ for all pairs of i,j and u,v such that a consistent comparison matrix will be generated for each scenario. It is also practically infeasible to input the comparison matrix for each scenario separately. Our procedure requires the user to provide $c_{uv}^{ij}$ for only a subset of i,j and u,v. The remaining comparisons are internally generated during the simulation. The procedure is as follows:

![](/api/attachments/2V6F85ZZ/fulltext/images/497fda84f02885af5ee2ff656f91ad82bedf4f64346ce1b39ad402292e14b033.jpg)  
Fig. 2. General model of AHP hierarchy for forecasting.

First, rearrange all the main events in increasing order of the number of subevents. This rearrangement is needed to generate the minimal scenario set. Let $E_{iu}^{\prime}$ denote subevent u of the event in the i'th position of the rearranged sequence of events. Let $c_{uv}^{rij}$ denote the comparison weight of $E_{iu}^{\prime}$ over $E_{jv}^{\prime}$ . The first subevent of each event is defined as the event not occurring (i.e. "no change" in the parent event). Hence, $c_{uv}^{ij}$ , and $c_{uv}^{rij}$ are defined only for $u \neq 1$ and $v \neq 1$ . Let each $E_{iu}^{\prime}$ be represented by a node. The objective is to define the minimal number of scenarios such that pairwise comparisons of events within each scenario, if consistent, will collectively lead to consistent weight matrices for all scenarios. Although there is more than one way of generating such scenarios, our procedure adopts the heuristic described below.

## 6. Generation of minimal scenario set

The procedure assumes a definite layout of nodes whereby the nodes (i.e. subevents) belonging to the same event are arranged row-wise and the nodes corresponding to the same subevent number are arranged column-wise. A generic example of the layout is illustrated in Fig. 3.

Step 1: The first subevent of each event is excluded from pairwise comparisons. Thus, the first column of nodes in Fig. 3 will not be included in the generation of scenarios. In this example, we will start marking the scenarios from column 2 of nodes. Define a scenario, $S_{k}$ , as the set of subevents such that main events occur at the same level of subevent number. That is, all the subevents making up $S_{k}$ all have the same second subscripts. Mark all columns of $S_{k}$ having two or more elements. For the network in Fig. 3, columns 2, 3, and 4 satisfy Step 1 requirements. Thus, there are three scenarios:

$$
\begin{array}{l} S _ {1} = \left\{E _ {1 2} ^ {\prime}, E _ {2 2} ^ {\prime}, E _ {3 2} ^ {\prime}, E _ {4 2} ^ {\prime}, E _ {5 2} ^ {\prime} \right\}, \\ S _ {2} = \left\{E _ {3 3} ^ {\prime}, E _ {4 3} ^ {\prime}, E _ {5 3} ^ {\prime} \right\}, \\ S _ {3} = \left\{E _ {4 4} ^ {\prime}, E _ {5 4} ^ {\prime} \right\}. \end{array}
$$

The elements of the scenarios are joined by solid arrows in Fig. 3. Note in Fig. 3 that the main events do not necessarily appear in numerical order in the first column since they are arranged in increasing order of the number of associated subevents.

![](/api/attachments/2V6F85ZZ/fulltext/images/2704c0c81ffbf30c1581b29e80c35b7c3d55a189a20df127b263b346b004aa93.jpg)  
Fig. 3. Illustration of the generation of relative weights.

Step 2: Generate a new scenario. Let the first node in the next unmarked column be the first element of the new scenario. Include the first node in each column which has a lower subevent number subject to the following restrictions:

(a) No subevent, except $E_{12}'$ , can appear in more than one scenario generated in Step 2.

(b) Not more than one subevent of the same main event can appear in a scenario.

Add $E_{12}^{\prime}$ to the scenario if it is not already included. Stop if all columns have been marked. Otherwise, repeat Step 2. The elements of the resulting scenarios are connected by broken arrows in Fig. 3. The scenarios are:

$$
\begin{array}{l} S _ {4} = \left\{E _ {1 2} ^ {\prime}, E _ {3 3} ^ {\prime}, E _ {4 4} ^ {\prime}, E _ {5 5} ^ {\prime} \right\}, \\ S _ {5} = \left\{E _ {1 1} ^ {\prime} 2, E _ {5 6} ^ {\prime} \right\}, \\ S _ {6} = \left\{E _ {1 2} ^ {\prime}, E _ {5 7} ^ {\prime} \right\}. \end{array}
$$

Note that the arcs of the network of Fig. 3 define a spanning tree rooted at $E_{12}'$ . By generating a small number of scenarios (defined by the paths of the spanning tree), one can determine the relative weights of $E_{iu}'$ and normalize the weights for each scenario. In summary, once the hierarchy structure is determined, the user needs to input the following:

1. $P_{iu}$ for each Subevent $u$ of independent Event $i$ .

2. $P(E_{jv} \mid E_{iu})$ for each Subevent $v$ of dependent Event $j$ .

3. Comparison matrix $W_{iu} = [w_{ab}^{iu}]$ of alternatives with respect to $E_{iu}$ .

4. Comparison matrix $C_{S_{k}} = [c_{uv}^{ij}]$ for each pair of $E_{iu}$ and $E_{jv}$ in $S_{k}$ with respect to the overall objective.

The consistency of each comparison matrix is checked by comparing its maximum eigenvalue to the number of elements in the matrix [32]. More specifically, a comparison matrix is consistent if the ratio of $(\lambda_{\max}-n)/(n-1)$ to the average random index for the same order matrix is less than 10 percent, where $\lambda_{max}$ denotes the maximum eigenvalue of the comparison matrix and n denotes the size of the matrix. The matrices are modified until the consistency condition is satisfied. The normalized eigenvector of a consistent matrix defines the relative weights of the activities in that matrix. Let $x_{a}^{iu}$ denote the relative weight of alternative a with respect to the $E_{iu}$ . Let $e_{iu}(S_{k})$ be the relative weight of $E_{iu}$ calculated with respect to scenario $S_{k}$ . The procedure determines $e_{iu}(S_{k})$ and $x_{a}^{iu}$ using $C_{S_{k}}$ and $W_{iu}$ matrices, respectively. Suppose there exist K independent scenarios (i.e. $S_{k}, k = 1, 2, \ldots, K$ generated by using the scenario generation procedure). Note that $\bigcup_{k=1}^{K} S_{k}$ contains all $E_{iu}$ except $E_{i1}$ . Also observe that for the illustrative example, we have:

$$
\begin{array}{r l} \bigcap_ {k = 1} ^ {K} S _ {k} & = \left\{E _ {1 2} ^ {\prime}, E _ {3 3} ^ {\prime}, E _ {4 4} ^ {\prime} \right\} \\ & = \text { Set   of   lead   subevents   in   columns   having } \\ & \text { more   than   one   subevent. } \end{array}
$$

The relative weight of $E_{iu}$ with respect to a new $S_{j} \neq S_{k}, k = 1, 2, \ldots, K$ , can be calculated as shown below. Let

$$
z _ {i u} = \frac {e _ {i u} (S _ {k})}{e _ {1 2} (S _ {k})}, \forall E _ {i u} \in S _ {k}, k = 1, 2, \dots , K\tag{2}
$$

where $z_{iu}$ is the ratio of the relative weight of $E_{iu}$ to the relative weight of the root node, $E_{12}$ . Note that $z_{12}=1$ . For a new $S_{j}$ , we have

$$
e _ {i j} (S _ {j}) = \frac {z _ {i u}}{\sum_ {E _ {i u} \in S _ {j}} z _ {i u}}.\tag{3}
$$

Once the comparison matrices are filled, new scenarios are generated by using $E_{iu}$ 's, not $E'_{iu}$ 's. This is done internally by the program. First, independent events are randomly generated using the $P_{iu}$ values. Next, conditional probabilities are used to generate dependent events. A scenario is defined by the set of events and subevents which are assumed to have occurred. Then, relative weight, $e_{iu}(S_j)$ of each $E_{iu}$ and the relative weight, $x_{a}^{iu}$ , of each alternative “a” are calculated as discussed above. It should be noted that

$$
\sum_ {a = 1} ^ {N} x _ {a} ^ {i u} = 1\tag{4}
$$

with respect to each $E_{iu}$ , where $a = 1, 2, \ldots, N$ alternatives. Finally, the composite weight, $C(a)$ , for each alternative a with respect to each scenario j is calculated as:

$$
C (a) = \sum_ {i} x _ {a} ^ {i u} e _ {i u} (S _ {j}), \forall E _ {i u} \in S _ {j}.\tag{5}
$$

![](/api/attachments/2V6F85ZZ/fulltext/images/a297eeac35262960b278a2750bb25e47706acd1a36ffa1d496e557592a32a4b1.jpg)  
Fig. 4. Illustrative example of probabilistic AHP hierarchy.

The alternative with the highest $C(a)$ value in the current scenario is selected in this specific run of the simulation. The procedure then generates a new set of random numbers and, hence, a new scenario. For each scenario, the most likely alternative is determined. After a desired number of simulation runs, one can determine the frequency of selection for each alternative. This frequency distribution is presented to the decision maker rather than an estimated single forecast. For most practical applications, a simulation sample size of 100 will be sufficient. However, interested readers may refer to standard texts on statistics to determine appropriate sample sizes for desired error levels. The bigger the sample size, the higher the confidence in the simulation results. Since our compiled C program runs very fast, we have used very large sample sizes (e.g. 15,000 runs in about 30 seconds) in most of our illustrative examples. The hypothetical example below demonstrates the implementation of our approach.

![](/api/attachments/2V6F85ZZ/fulltext/images/e1f37f10d2f8c828e28a84797347a1c2df4f27fece2900790a934c6f58923ab9.jpg)  
Fig. 5. A spanning tree of the example problem.

Table 2  
$P_{iu}$ for independent events

<table><tr><td rowspan="2">Main Event (i)</td><td colspan="2"> $P_{iu}$ </td></tr><tr><td>Subevent (u=1)</td><td>Subevent (u=2)</td></tr><tr><td>1</td><td>0.8</td><td>0.2</td></tr><tr><td>3</td><td>0.6</td><td>0.4</td></tr></table>

## 7. Illustrative example

Fig. 4 illustrates a simple hierarchy structure where events 1 and 3 are independent. The occurrence of Event 2 depends on the level that Event 3 occurs. The first subevent under each event describes nonoccurrence of that event. If all three events do not occur during a particular simulation run, then no alternative is selected for that run. Main Event 1, $M_{1}$ , contains two subevents, $E_{11}$ and $E_{12}$ . Main Event 2, $M_{2}$ , contains three subevents, $E_{21}$ , $E_{22}$ , and $E_{23}$ . Main Event 3, $M_{3}$ , contains two subevents, $E_{31}$ and $E_{32}$ .

## 7.1. Manual computational analysis

Reordering the events in increasing order of number of subevents, we get the following:

$$
\begin{array}{l} E _ {1 u} ^ {\prime} = E _ {i u}, u = 1, 2, \\ E _ {2 u} ^ {\prime} = E _ {3 u}, u = 1, 2, \\ E _ {3 u} ^ {\prime} = E _ {2 u}, u = 1, 2, 3. \end{array}
$$

Fig. 5 shows the spanning tree structure. Table 2 displays $P_{ij}$ values for the independent events. Table 3 shows the $P(E_{2v} | E_{3v})$ values and Table 4 shows the $w_{ab}^{iu}$ values. Negative values in Table 4 are used to indicate reverse importance weights in the pair-wise comparison matrices. The entries in Table 4 are used later to compute the $x_{a}^{iu}$ values for the alternatives. Table 5 shows the comparison matrices for the sub-events in the two scenarios, $S_{1}$ and $S_{2}$ , indicated by Fig. 5.

Table 3  
Conditional probabilities for dependent events

<table><tr><td rowspan="2">Subevent (u)</td><td colspan="3"> $P(E_{2v} | E_{3u})$ </td></tr><tr><td>Subevent (v = 1)</td><td>Subevent (v = 2)</td><td>Subevent (v = 3)</td></tr><tr><td>1</td><td>0.6</td><td>0.3</td><td>0.1</td></tr><tr><td>2</td><td>0.2</td><td>0.4</td><td>0.4</td></tr></table>

$$
\begin{array}{l} S _ {1} = \left\{E _ {1 2} ^ {\prime}, E _ {2 2} ^ {\prime}, E _ {3 2} ^ {\prime} \right\}, \\ S _ {2} = \left\{E _ {1 2} ^ {\prime}, E _ {3 3} ^ {\prime} \right\}, \end{array}
$$

which, after rearranging the elements, yield

$$
\begin{array}{l} S _ {1} = \left\{E _ {1 2}, E _ {3 2}, E _ {2 2} \right\}, \\ S _ {2} = \left\{E _ {1 2}, E _ {3 3} \right\}. \end{array}
$$

The relative weights of the subevents in scenarios 1 and 2 are calculated from the comparison matrices in Table 5:

$$
\begin{array}{l l} e _ {1 2} (S _ {1}) = 0. 5 3 & e _ {1 2} (S _ {2}) = 0. 3 3, \\ e _ {3 2} (S _ {1}) = 0. 3 3, & e _ {2 3} (S _ {2}) = 0. 6 7, \\ e _ {2 2} (S _ {1}) = 0. 1 4. \end{array}
$$

Using equation (2), the ratios, $z_{iu}$ , are computed for the elements in each scenario:

$$
z _ {1 2} = 1, z _ {3 2} = 0. 6, z _ {2 2} = 0. 2 6, z _ {2 3} = 2. 0 3.
$$

To generate a new scenario, a random number, $r_{1}$ , is generated from a uniform distribution [0, 1] for Event 1. If $r_{1} \leq 0.8$ , then, based on $P_{11}$ in Table 2, we conclude that $E_{11}$ occurs. Otherwise, $E_{12}$ occurs. Similarly, random number $r_{2}$ determines level at which Event 3 occurs ( $E_{3u}$ ). Suppose $E_{12}$ and $E_{32}$ have occurred. Random number $r_{3}$ is generated and occurrence of $E_{2u}$ (u = 1, 2, 3) is determined using $P(E_{2u} | E_{32})$ .

Examples of pairwise comparisons of alternatives

<table><tr><td> $w_{ab}^{12}$ </td><td colspan="2"> $b$ </td><td> $w_{ab}^{22}$ </td><td colspan="2"> $b$ </td><td> $w_{ab}^{23}$ </td><td colspan="2"> $b$ </td><td> $w_{ab}^{32}$ </td><td colspan="2"> $b$ </td></tr><tr><td> $a$ </td><td>1</td><td>2</td><td> $a$ </td><td>1</td><td>2</td><td> $a$ </td><td>1</td><td>2</td><td> $a$ </td><td>1</td><td>2</td></tr><tr><td>1</td><td>1</td><td>3</td><td>1</td><td>1</td><td>-2</td><td>1</td><td>1</td><td>5</td><td>1</td><td>1</td><td>-7</td></tr><tr><td>2</td><td>-3</td><td>1</td><td>2</td><td>2</td><td>1</td><td>2</td><td>-5</td><td>1</td><td>2</td><td>7</td><td>1</td></tr></table>

SCREEN 4

Event/Alternative, Probability, Comparison, Help, Run, Verify/data, Quit

SCREEN 2  
SCREEN 1  
SCREEN 3

<table><tr><td colspan="6">Main Event 1 2 3
Number of Sub-Event 2 3 2</td></tr></table>

Screen 1-4

SCREEN 6  
![](/api/attachments/2V6F85ZZ/fulltext/images/2adf178e0851f9b6466687caedaee9d3274aa5ce1802faa28c8aa4eaa1336f46.jpg)  
SCREEN 8  
SCREEN 5  
SCREEN 7  
Screen 5-8

SCREEN 10

Do you want to change current data? (Y/N)

SCREEN 12

Data Entry Menu Selection Sequence

Alternatives

PROBABILITIES OF SUBEVENTS

SCREEN 11

SUB EVENT -> 1 2
Event 1 0.80 0.20
Event 2 ■■■■■■■
Event 3 0.60 0.40

<table><tr><td colspan="3">Memory Available: 351582</td></tr><tr><td colspan="3">RELATIVE WEIGHT MATRIX OF ALTERNATIVES FOR MAIN EVENT 1 SUBEVENT 2</td></tr><tr><td>ALTERNATIVE</td><td>1</td><td>2</td></tr><tr><td>ALT 1</td><td>■■■■■</td><td>3</td></tr><tr><td>ALT 2</td><td>■■■■■■■■</td><td></td></tr><tr><td colspan="3">RELATIVE WEIGHT MATRIX OF ALTERNATIVES FOR MAIN EVENT 2 SUBEVENT 3</td></tr><tr><td>ALTERNATIVE</td><td>1</td><td>2</td></tr><tr><td>ALT 1</td><td>■■■■</td><td>5</td></tr><tr><td>ALT 2</td><td>■■■■■■■■</td><td></td></tr></table>

SCREEN 9  
Screen 9-12

subEvent 1-2 3-2 2-2
1-2 3 2
3-2 -2
2-2

Memory Available: 351572 RELATIVE WEIGHT MATRIX OF SUBVENTS Header 1-J: The Jth subevent of the 1th event.

SCREEN 16  
![](/api/attachments/2V6F85ZZ/fulltext/images/4853a5fde2912d0fd3afbd93306b885acf1fe4a24a29b1146921ef62b6619b5a.jpg)  
SCREEN 14  
Screen 13-16

SubEvent 1-2 2-3
1-2 ■■■■+2
2-3 ■■■■■■■

Memory Available: 351582 RELATIVE WEIGHT MATRIX OF SUBEVENTS
header I-J: The Jth subsequent of the 1th event.

## SCREEN 15

SCREEN 13

<table><tr><td>Event/alternative, Probability, Comparison, Help, Run, Verify/data, Quit</td></tr><tr><td>Simulation
Histogram
Main menu</td></tr><tr><td>Dynamic Decision Making</td></tr><tr><td>Data Entry Menu Selection Sequence</td></tr><tr><td>1. Event/Alternative 2. Probability 3. Comparison 4. Run</td></tr></table>

![](/api/attachments/2V6F85ZZ/fulltext/images/80dceb1ea07c8c7c710fdfef6e73548583714f8352950d1d8fa4a8adc4cbe8d9.jpg)

SCREEN 18

<table><tr><td colspan="2">ENTER THE FOLLOWING INFORMATION</td></tr><tr><td>NUMBER OF SIMULATION RUNS</td><td>15000_</td></tr></table>

SCREEN 17  
SCREEN 19

SCREEN 20  
![](/api/attachments/2V6F85ZZ/fulltext/images/ddcfd789be7c5f3b68047c28ca6ad766288764ef72ed6c21195a66b41f086a82.jpg)

![](/api/attachments/2V6F85ZZ/fulltext/images/cd4ad94a2c84ff44d85cb60ebc13eafcfd97f3f74f4560a901f30c2ba5f3313d.jpg)  
Screen 17-20

Table 5  
Comparison matrices for $S_{1}$ and $S_{2}$

<table><tr><td> $C_{S1}$ </td><td> $E_{12}$ </td><td> $E_{32}$ </td><td> $E_{22}$ </td><td> $C_{S2}$ </td><td> $E_{12}$ </td><td> $E_{23}$ </td></tr><tr><td> $E_{12}$ </td><td>1</td><td>3</td><td>2</td><td> $E_{12}$ </td><td>1</td><td>-2</td></tr><tr><td> $E_{32}$ </td><td>-3</td><td>1</td><td>-2</td><td> $E_{23}$ </td><td>2</td><td>1</td></tr><tr><td> $E_{22}$ </td><td>-2</td><td>2</td><td>1</td><td></td><td></td><td></td></tr></table>

Suppose that $R_{3}=0.8$ . Then, using the second row of Table 3, we conclude that $E_{23}$ has occurred. The new scenario is now defined by:

$$
S _ {3} = \left\{E _ {1 2}, E _ {2 3}, E _ {3 2} \right\}.
$$

Using equation (3), $e_{iu}$ for each $E_{iu} \in S_{3}$ is calculated as:

$$
v _ {1 2} \left(S _ {3}\right) = \frac {z _ {1 2}}{\sum_ {E _ {i u} \in S _ {3}} z _ {i u}} = \frac {1}{(1 + 2 . 0 3 + 0 . 6 2)} = 0. 2 7 4,
$$

$$
v _ {2 3} \left(S _ {3}\right) = \frac {z _ {2 3}}{\sum_ {E _ {i u} \in S _ {w}} z _ {i u}} = \frac {2 . 0 3}{(1 + 2 . 0 3 + 0 . 6 2)} = 0. 5 5 6,
$$

$$
v _ {3 2} \left(S _ {3}\right) = \frac {z _ {3 2}}{\sum_ {E _ {i u} \in S _ {3}} z _ {i u}} = \frac {0 . 6 2}{(1 + 2 . 0 3 + 0 . 6 2)} = 0. 1 7 0.
$$

The relative weights $x_{a}^{iu}$ for alternatives 1 and 2 are obtained from the comparison matrices based on $E_{12}$ , $E_{23}$ , and $E_{32}$ in Table 4.

$$
x _ {1} ^ {1 2} = 0. 7 5 0, \quad x _ {1} ^ {2 3} = 0. 8 3 3, \quad x _ {1} ^ {3 2} = 0. 1 2 5,
$$

$$
x _ {2} ^ {1 2} = 0. 2 5 0, \quad x _ {2} ^ {2 3} = 0. 1 6 7, \quad x _ {2} ^ {3 2} = 0. 8 7 5.
$$

The composite weights for the two alternatives are now calculated based on equation (5):

$$
\begin{array}{r l} C (A 1) & = x _ {1} ^ {1 2} e _ {1 2} (S _ {3}) + x _ {1} ^ {2 3} v _ {2 3} (S _ {3}) + x _ {1} ^ {3 2} v _ {3 2} (S _ {3}) \\ & = 0. 7 5 0 (0. 2 7 4) + 0. 8 3 3 (0. 5 5 6) \\ & \quad + 0. 1 2 5 (0. 1 7 0) \\ & = 0. 6 9 0, \\ C (A 2) & = x _ {2} ^ {1 2} v _ {1 2} (S _ {3}) + x _ {2} ^ {2 3} v _ {2 3} (S _ {3}) + x _ {2} ^ {3 2} v _ {3 2} (S _ {3}) \\ & = 0. 2 5 0 (0. 2 7 4) + 0. 1 6 7 (0. 5 5 6) \\ & \quad + 0. 8 7 5 (0. 1 7 0) \\ & = 0. 3 1 0. \end{array}
$$

Hence, Alternative 1 is forecasted for this specific scenario. The above scenario generation and selection of alternatives are repeated a number of times and the frequency distribution for each alternative is determined. The simulation run in the next section confirms the manual computation shown above.

## 7.2. Sample simulation run

This section presents a DDM simulation run of the illustrative example in the preceding section. The AHP decision hierarchy shown earlier in Fig. 4 is used for this example. For the example, events 1 and 3 are independent. The occurrence of Event 2 depends on the level at which Event 3 occurs. The first sub-event under each event describes nonoccurrence of that event. If all three events do not occur, then no alternative is picked. Main Event 1, $M_{1}$ , contains two sub-events, $E_{11}$ and $E_{12}$ . Main Event 2, $M_{2}$ , contains three sub-events, $E_{21}$ , $E_{22}$ , and $E_{23}$ . Main Event 3, $M_{3}$ , contains two sub-events, $E_{31}$ and $E_{32}$ . Since this is a forecasting problem, there is a possible outcome (alternative) defined as “no change.” The first alternative in Fig. 4 (i.e. Alternative A1) is used to represent the “no change” alternative. Similarly, the first sub-event of each main event is selected as the sub-event indicating “no change.” Thus, the alternatives are compared only with respect to the sub-events associated with changes in event levels. Referring to Fig. 4, the sub-events eligible for the pair-wise comparisons are $E_{12}$ , $E_{22}$ , $E_{23}$ , and $E_{32}$ .

The Screen 1 shows the main menu of DDM. The options on the menu involve the specification of events and alternatives, entry of probability information, entry of pair-wise comparison matrices, on-line help, running the simulation, data verification, and terminating the program. An option is selected from DDM menus by pressing the first letter of the name of the desired option. Screen 2 shows the drop down menu for the first option in the main menu. The specification of events and alternatives must be done before any of the other options are selected from the main menu. Entries required are events and sub-events, dependent sets, and alternatives. Screen 3 shows the specification of 3 main events and their respective number of sub-events.

The number of dependent sets is shown on Screen 4. Based on Fig. 4, there is only one dependent set. Dependent set 1 consists of two main events. Screen 5 shows the sequential entry of the mutually dependent events in each dependent set. Two columns (Col 1, Col 2) are provided for the specification of the member events in each dependent set. The elements of dependent set 1 are entered as 3 and 2 (i.e. 3 before 2). This indicates that Event 2 is dependent on Event 3. Screen 6 indicates that the number of alternatives is 2. As mentioned earlier, Alternative 1 is indicated as the alternative representing “no change.” The next set of entries involve the probability information for the problem. Screen 7 shows options for conditional probability and probability of independent events.

Screen 8 is for dependent set 1. The conditional event is Event 3 and the dependent event is Event 2. The conditional probability information from Table 3 are entered as shown on the screen. The three dependent sub-events of Event 2 are indicated in the columns. The two conditional sub-events of Event 3 are indicated in the rows. Note that the probabilities entered for each row must sum to one. The probabilities of the sub-events of the independent events 1 and 3 are entered on the Screen 9. This probability information is obtained from Table 2. Note that dependent event 2 is blocked out of the data entry for this screen. Note also that the sum of the probability entries for each row is one.

The next set of data entries involve pair-wise comparisons. Screen 10 shows that entries are required for comparison matrices for alternatives and sub-events. The Screens 11, 12, 13, and 14 show the comparison of the two alternatives with respect to each of the four sub-events $E_{12}$ , $E_{22}$ , $E_{23}$ , and $E_{32}$ . These matrices are presented in Table 4. Since each matrix is symmetric, only one half of the matrix is required to be entered by the user. DDM internally completes the matrix. Note that reciprocal pair-wise ratings are entered as negatives on the screen. This is to facilitate ease of data entry. DDM internally converts the negative numbers to the appropriate reciprocals. For example, -5 on the screen is converted to 1/5 when normalizing the matrices.

The pair-wise comparison matrices for the sub-events contained in the initial two scenarios, as shown in Table 5, are entered in Screens 15 and 16. Screen 17 shows the next option from the main menu. This option involves running the simulation and printing the histogram. When the simulation option is selected, Screen 18 appears. The desired number of simulation runs is entered on the screen. For this example, we have specified 15,000 simulation runs. The Screen 19 shows the result of the simulation run. Out of the 15,000 forecast outcomes, 9,933 are for alternative 1 while 5,067 are for alternative 2. Screen 20 shows the histogram of the simulation result. Sixty-six percent of the outcomes are for Alternative 1 and 34% are for Alternative 2.

Table 6  
Comparison of the results of manual computation and simulation

<table><tr><td></td><td>Manual</td><td>Simulation</td></tr><tr><td>Alternative 1</td><td>0.69</td><td>0.66</td></tr><tr><td>Alternative 2</td><td>0.31</td><td>0.34</td></tr></table>

The result of the simulation closely matches the manual computation presented for one specific scenario. It should be recalled that the simulation result in this example is based on 15,000 simulated scenarios. A smaller simulation sample size (e.g., 100) yields similar results (i.e., 0.67, 0.33). Table 6 shows a comparison of the result of the manual computation and the simulation result.

## 8. Conclusion

We have presented a decision support system which incorporates qualitative factors with uncertainty in decision problems. The system, named DDM, can be applied to forecasting problems. It takes into consideration the dependencies between factors affecting the outcome in a given planning scenario. The simulation technique generates scenarios, evaluates each scenario, and provides the frequency distribution for each alternative. The decision maker is presented with the distribution of the selection of forecast alternatives rather than a single forecasted value. The present implementation of DDM is limited to four levels of hierarchy. An ongoing research is directed at developing a more general case with more levels of hierarchy. This will accommodate more complex dependency structures. Future versions of DDM will also provide more information (e.g. sensitivity analysis) and confidence intervals for the occurrence of the respective alternatives.

## References

[1] H. Azani and R. Khorramshahgol, Analytic Delphi Method (ADM): A Strategic Decision Making Model

Applied to Location Planning, Engineering Costs and Production Economics 20, (1990) 23–28.

[2] A.B. Badiru, Expert Systems Applications in Engineering and Manufacturing (Prentice-Hall, Englewood Cliffs, NJ, 1992).

[3] R. Banai-Kashani, Discrete Model-Choice Analysis of Urban Travel Demand by the Analytic Hierarchy Process, Transportation 16 (1989) 81–96.

[4] T. Cook, P. Falchi and R.. Mariano, An Urban Allocation Model Combining Time Series and Analytic Hierarchical Methods, Management Science 30, No. 2 (Feb. 1984) 198–208.

[5] J.S. Dyer, Remarks on the Analytic Hierarchy Process, Management Science, 36, No. 3 (1990) 249–258.

[6] J.R. Emshoff and T.L. Saaty, Applications of the Analytic Hierarchy Process to Long Range Planning, European Journal of Operational Research 10 (1982) 131–143.

[7] C.H. Falkner and S. Benhajla, Multi-Attribute Decision Models in the Justification of CIM Systems, Engineering Economist 35, No. 2 (Winter 1990) 91–114.

[8] E.H. Forman, T.L. Saaty, M.A. Selly and R. Waldom, Expert Choice, Decision Support Software, (McLean, VA, 1983).

[9] A.A. Girgis, M.A. Wortman and R.S. Henry, Development of Rank Ordering Techniques Based on the Analytical Hierarchy Process for Evaluation of Energy Conversion Devices, International Journal of Energy Research 13, (1989) 279–287.

[10] B.L. Golden, E.A. Wasil and P.T. Harker, Eds, The Analytic Hierarchy Process: Applications and Studies, (Springer-Verlag, New York, 1989).

[11] P.T. Harker and and L.G. Vargas, The Theory of Ratio Scale Estimation: Saaty's Analytic Hierarchy Process, Management Science 33, No. 11 (1987) 1383–1403.

[12] R. Kangari and L.T. Boyer, Risk Management by Expert Systems, Project Management Journal 20, No. 1 (1989) 40–48.

[13] R.L. Keeney and H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs (Wiley, New York, 1976).

[14] R. Khorramshahgol and V.S. Moustakis, Delphic Hierarchy Process (DHP): A Methodology for Priority Setting Derived from the Delphi Method and Analytic Hierarchy Process, European Journal of Operational Research 37, (1988) 347–354.

[15] R. Khorramshahgol, H. Azani and Y. Gousty An Integrated Approach to Project Evaluation and Selection, IEEE Transactions on Engineering Management 35, No. 4, (Nov. 1988) 265–270.

[16] M.J. Liberatore, An Extension of the Analytic Hierarchy Process for Industrial R&D Project Selection and Resource Allocation, IEEE Transactions on Engineering Management 34, No. 1 (1987) 12–18.

[17] T. Masuda, Hierarchical Sensitivity Analysis of Priority Used in Analytic Hierarchy Process, International Journal of Systems Science 21, No. 2 (1990) 415–427.

[18] M.A. Mustafa, An Integrated Hierarchical Programming Approach for Industrial Planning, Computers and Industrial Engineering 16, No. 4 (1989) 525–534.

[19] E.V. Newland, New Scenarios for Economic Growth,

Proceedings: 1986 Fuel Supply Seminar, (Electric Power Research Institute, place?, Sept. 1987).

[20] P.S. Pulat, H. Lee and B. Groten, A Dynamic Decision Making Approach, Working Paper 89-01 (School of Industrial Engineering, University of Oklahoma, Norman, OK, Nov. 1989).

[21] S. Rahman and L.C. Frair, A Hierarchical Approach to Electric Utility Planning, Energy Research 8 (1984) 185–196.

[22] V. Ramanujam and P.L. Saaty, Technological Choice in the Less Developed Countries: An Analytic Hierarchy Approach, Technological Forecasting and Social Change 19 (1981) 81–98.

[23] T.L. Saaty and L.G. Vargas, Prediction, Projection and Forecasting (Kluwer Academic Publishers, Boston, MA, 1991).

[24] T.L. Saaty and H. Gholamnezhad, Oil Prices: 1985 and 1990, Energy Systems and Policy 5, No. 4 (1981) 303–318.

[25] T.L. Saaty, L.G. Vargas and R. Wendell, Assessing Attribute Weights by Ratios, Omega 11, No. 1 (1983) 9–13.

[26] T.L. Saaty and L.G. Vargas, Estimating Technological Coefficients by the Analytic Hierarchy Process, Socio-Economic Planning Science 13 (1979) 333–336.

[27] T.L. Saaty and L.G. Vargas, Inconsistency and Rank Preservation, Journal of Mathematical Psychology 18 (1984) 205–214.

[28] T.L. Saaty and L.G. Vargas, The Analytic Hierarchy Process: Theoretic Developments and Some Applications, Math Modelling 9 (1987) 3–5.

[29] T.L. Saaty, A Scaling Method for Priorities in Hierarchical Structures, Journal of Mathematical Psychology 15 (June 1977) 235–281.

[30] T.L. Saaty, An Exposition of the AHP in Reply to the paper ‘Remarks on the Analytic Hierarchy Process’, Management Science 36, No. 3 (1990) 259–268.

[31] T.L. Saaty, Axiomatic Foundations of the Analytic Hierarchy Process, Management Science 32, No. 7 (1986) 841–855.

[32] T.L. Saaty, The Analytic Hierarchy Process (McGraw-Hill, New York, 1980).

[33] T.L. Saaty and J.M. Alexander, Conflict Resolution: The Analytic Hierarchy Approach (Praeger, New York, 1989).

[34] L.G. Vargas, An Overview of the Analytic Hierarchy Process and its Applications, European Journal of Operational Research 48 (1990) 2–8.

[35] L.G. Vargas, Prediction and the Analytic Hierarchy Process, Mathematics and Computers in Simulation 25 (1983) 156–167.

[36] R.D. Wabalickis, Justification of FMS with the Analytic Hierarchy Process, Journal of Manufacturing Systems 7, No. 3 (1988) 175–182.

[37] Y. Wind and T.L. Saaty, Marketing Applications of the Analytic Hierarchy Process, Management Science 26, No. 7 (1980) 641–658.

[38] R.L. Winkler, Decision Modeling and Rational Choice: AHP and Utility Theory, Management Science 36, No. 3 (1990) 247–248.

[39] F. Zahedi, The Analytic Hierarchy Process: A Survey of the Method and its Applications, Interfaces 16 (1986) 96–108.
