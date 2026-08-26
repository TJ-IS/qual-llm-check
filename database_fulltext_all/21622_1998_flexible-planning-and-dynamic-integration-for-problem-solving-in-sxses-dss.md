---
otero_id: 21622
otero_key: "AU7H6BM9"
title: "Flexible planning and dynamic integration for problem solving in SXSES-DSS"
authors: "Pengzhu Zhang; Yingluo Wang"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00055-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Flexible planning and dynamic integration for problem solving in SXSES-DSS

Pengzhu Zhang <sup>)</sup>, Yingluo Wang

Institute of Strategy and Decision-making, School of Management, Xi’an Jiaotong UniÕersity, Xi’an, 710049, China

Accepted 10 August 1998

## Abstract

In this paper, a user-oriented integrated solving approach to the problems in decision support systems, called as the flexible planning and dynamic integration approach FPDI , is proposed. FPDI consists of the flexible planning of problemŽ . solving chain-path, the flexible connection and dynamic integration of different models, as well as the controllable outputting of problem solutions. FPDI has been implemented in the environment with six components in the prototype of Decision Support System of Macroscopic Coordinate Development of Society, Economy, Science and Technology in Shaanxi Province SXSES-DSS .Ž . q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Problem organizing; Problem solving; Decision support systems

## 1. Introduction

Decision support system DSS is a man-machineŽ . interactive problem solving system. By Vinze and Sen 3 , in DSS, the decision support process con- <sup>w</sup> <sup>x</sup> sists of problem identification, solution planning, tools’ integration and model execution. Of the process, it is essential to plan the solving scheme of different problems and integrate different models in the solving scheme.

Dolle and Kottemann 1 have given an object-ori-<sup>w</sup> <sup>x</sup> ented model integrating approach based on the data base theory. Liang 2 presented a knowledge-based<sup>w</sup> <sup>x</sup> graph searching approach. The integrated solving scheme can be derived by the two steps:

1. Get a set of solving alternatives represented in a directed tree by means of rule-based inference;

2. Select the best solving alternative through searching the directed tree.

Dolle’s approach integrates the models based on the fixed relation information stored in the data base, so that it is available for users to change the integrating relations by the system dynamic behavior. Liang’s integrating approach is based on the knowledge base of input-output relations of models, and also inconvenient for users to organize the solving scheme by themselves.

In the real world, the structure of any system would occur more or fewer changes from one period to the next period, and the system dynamic characteristics would also behave differently. So the planning and integration approach to problem solving should be flexible on the structure of the problem-involved system, called as the structure flexibility, and adaptable to its dynamic behavior, called as the dynamic adaptability.

The structure flexibility means that the users can get an integrated solving scheme from DSS, which is formed on the structure characteristics of probleminvolved system and operation mechanism. The dynamic adaptability to the system behavior indicates that the integrating approach should allow users to select the interactive information included in the integrated solving scheme based on the dynamic characteristics of problem-involved system.

Of the current studies on the integration of problem solving in DSS, there is not a planning and integrating approach that is of the structural flexibility and dynamic adaptability of the problem-involved system. In this paper, we present a flexible planning and dynamic integration approach FPDI , which isŽ . refined from the authors’ research and development experiences on Decision Support System of Macroscopic Coordinate Development of Society, Economy, Science and Technology in Shaanxi Province Ž . SXSES-DSS 5 . The succeeding sections are orga- <sup>w</sup> <sup>x</sup> nized as follows.

The principle frame of FPDI approach is presented in Section 2. Section 3 deals with the flexible planning of problem solving chain-path, which includes three subsections: problem chain editing, solving scheme selecting and model chain editing; while Section 4 deals with the flexible connection and dynamic integration of different models. In Section 5, how to output the problem solutions is discussed. Section 6 gives a summary of this paper.

## 2. FPDI approach frame

For the problem solving alternatives constructed by DSS, it is necessary to satisfy the following conditions to deliver reasonable decision support for users:

1. The constructed problem solving alternatives should correctly reflect the structure composition and relationship of the problem-involved system;

2. The constructed problem solving alternatives can efficiently explain the focus points of the problem.

By the above conditions, we have the following rules.

Rule 1: Let q stand for a decision problem of system S, and let $F _ { t }$ stand for the dynamic behavior characteristics of the problem-involved system S, and $F _ { t }$ varies with the change of time t, and

$$
F _ {t} = f \big (C _ {t}, R _ {t} \big)
$$

Where

$C _ { t }$ stands for the set of structure elements of the system S at time t;

$R _ { t }$ stands for the set of relations among the elements of system S at time t;

$f ( C _ { t } , R _ { t } )$ represents the functional characteristics of system S.

Furthermore, let $F _ { t } ^ { \prime }$ represent a problem-domain expert’s recognition to $F _ { t }$ of system S, and

$$
F _ {t} ^ {\prime} = f ^ {\prime} \big (C _ {t} ^ {\prime}, R _ {t} ^ {\prime} \big) \sim F _ {t}
$$

If DSS could make it possible for each problem-domain expert to get an integrated problem solving scheme by his recognition to $F _ { t } ,$ , then, DSS is said to be structure flexible to system S.

Hence, the structure flexibility makes DSS provide different problem-domain experts with different integration alternatives by different recognition to the problem-involved system.

Rule 2: If a decision is to make for $F _ { t } \to F _ { t } $ , and in DSS, to solve problem q is to perform $F _ { t } ^ { \prime } \ \to \ F _ { t } ^ { \prime }$ by integrating the real state information of the problem-involved system $E _ { t }$ in the past time and the expert’s interactive information $E _ { t } ^ { \prime } ,$ , if

$$
F _ {t} ^ {\prime} \sim F _ {t}
$$

then, the DSS may be said to be of dynamic adaptability to the system behavior.

The dynamic adaptability to the system behavior makes DSS possible to deliver decision support for different users’ problems.

Based on the two rules, we put forward the flexible planning and dynamic integration approach Ž . FPDI . FPDI approach performs the problem solving in three steps shown in Fig. 1:

1. Formulate and structure the problem solving chain-path so as to make all its sub-problems and their solving scheme respond to the structure characteristics of the problem-involved system $F _ { t } \mathrm { ; }$ ;

![](/api/attachments/AU7H6BM9/fulltext/images/6767f702aef2146d39e52bd14d39a16b15d63d95ebc32998f8b35d365ac7bc61.jpg)  
Fig. 1. FPDI flow diagram.

2. Solve the sub-problems by integrating the dynamic behavior characteristics of the problem-involved system $E _ { t }$ and the expert’s interactive information $E _ { t } ^ { \prime }$

3. Output the solutions of all sub-problems to form the solution of the user’s problem.

## 3. Problem solving chain-path planning

Due to the continuous variation of DSS’s problem-involved system in time and space, the problems presenting in the problem-involved system are varied with the time. Hence, it is necessary for DSS to deliver flexible decision support for users to deal with the various problems occurred during the operation of the problem-involved system. To get a flexible decision support, DSS should provide some tools for users to interactively organize the problem solving scheme.

Here, the problem solving scheme is composed of three parts:

1. A sequence of sub-problems, called as problem chain;

2. A set of models, called as model chain of problem; and

3. A set of executive documents, called as executive chain of models.

In the following, the problem solving scheme with the three parts is also called as problem solving chain-path.

Let $P _ { \mathrm { c } } = ( w _ { 1 } , w _ { 2 } , \dots , w _ { \mathrm { n } } )$ stand for the problem chain organized in DSS for the user’s problem, $M _ { \mathrm { c i } } = ( m _ { \mathrm { i 1 } } , ~ m _ { \mathrm { i 2 } } , \dots , ~ m _ { \mathrm { i k } } )$ stand for the model chain of sub-problem $w _ { \mathrm { i } } ,$ , and $S _ { \mathrm { c i j } }$ stand for the solving executive chain of model $m _ { \mathrm { i j } } .$ Then, the structure $R _ { w }$ of the solving chain-path of the user’s problem q may be represented as follows:

$$
\left| \begin{array}{l} R _ {w} = \left(P _ {\mathrm{c}}, \{M _ {\mathrm{ci}} \}, \{S _ {\mathrm{cij}} \}\right) \\ P _ {\mathrm{c}} = (w _ {1}, w _ {2}, \ldots , w _ {n}) \\ M _ {\mathrm{ci}} = (m _ {\mathrm{i1}}, m _ {\mathrm{i2}}, \ldots , m _ {\mathrm{ik}}) \\ i \in [ 1, n ], j \in [ 1, k ] \end{array} \right.
$$

So the problem solving chain-path $R _ { w }$ has a threelayer hierarchical structure shown in Fig. 2.

In Fig. 2, the three layers separately refer to problem chain, model chain and solving executive chain. The solving executive chain consists of the required data, model body, knowledge, graph, text and some connecting interfaces.

For problem planning, that is to edit problem chain, select solving scheme and edit model chain.

## 3.1. Problem chain editing

In the real decision making process, a decision maker usually gets the solution of the original problem q through solving a series of sub-problems $( w _ { 1 } , w _ { 2 } , \ldots , w _ { \mathrm { n } } )$ , in which there exist a logic order and a certain of information transference relations. So it is necessary for DSS to organize the sub-problems by the following two steps:

1. Structure the sub-problems by reduction recognition to the user’s problem q <sup>w</sup> <sup>x</sup> 4 ;

![](/api/attachments/AU7H6BM9/fulltext/images/5db070b11e437d2133ee65211c576f0938788318e556e5b6773d4b075521a8d3.jpg)  
Fig. 2. Structure of problem solving chain-path.

2. Provide a problem chain editor for the user to add, delete and rearrange the sub-problems by their understanding and recognition to the user’s problem.

In the prototype of SXSES-DSS, the implemented problem chain editors support the user by following steps:

1. Display auto-organizing problem chain for the user;

2. Rearrange the sequence of the sub-problems in the problem chain by changing the order of the sub-problems according to the user’s requirements;

3. Input the index number of the problems to be appended, if the user wants to add some sub-problems to the problem chain;

4. Input the index number of the problems to be deleted, if the user wants to delete some sup-problems in the problem chain;

5. Update the order number of the sub-problems by moving the cursor, if the operation of adding and deleting has been done by the user.

Here is an example that the user applied SXSES-DSS to support ‘making development objective decision of national economy in Shaanxi Province’. By use of auto-organizing problem chain, the user can get the problem chain: T071000101, T07100010101, T07100010102, T7071000103 or T032500101,4  T032500102 .4

If the user hoped to combine the two problem chains into one, then the user can edit and obtain the following problem chain by using the problem chain editor: T032500101, T0710010101, T07100010102, T07100010103, T071000101, T032500102 .4

## 3.2. SolÕing scheme selecting

In DSS, the solving schemes are groups of models, knowledge bases and cases. And the relations between the problems $( w _ { 1 } , w _ { 2 } , \ldots , w _ { \mathrm { n } } )$ and the solving schemes $( m _ { 1 1 } , \ldots , \ m _ { 1 \mathrm { k } } ) , \ldots , ( m _ { \mathrm { n 1 } } , \ldots , m _ { \mathrm { n k } } )$ should have been stored. Due to the different focus points and the variation of time for the user’s problem, the user may want to change the solving scheme for one or more sub-problems. The man-machine interactive problem solution planning component has been developed in the prototype of SXSES-DSS, which can be used to choose the best solving alternatives for the sub-problems in the problem chain by the following process:

1. Set a sub-problem $w _ { \mathrm { i } }$ by moving the cursor on the treelike problem graph;

2. Provide a candidate scheme group $( m _ { \mathrm { i } 1 } , \hdots , m _ { \mathrm { i } \mathrm { k } } )$ for the user by means of knowledge-based inference based on the user’s problem name;

3. Display all the scheme groups for the user to select a suited scheme group by moving cursor in up and down directions if the user does not accepts the candidate scheme;

4. Display the solving alternatives of the selected scheme group for the user to choose the best of the solving alternatives as the solving scheme of the current sub-problem;

5. Repeat 1Ž . Ž . <sup>;</sup> 4 until all the sub-problems have been endowed with the solving schemes.

For problem T07100010103 ‘designing countermeasures of economic adjustment and control’ in the prototype of SXSES-DSS, the solving scheme may be obtained by the following man-machine interaction:

1. Select the scheme group: national economic adjustment and control group;

2. Display all its solving alternatives, which are listed in the following:

M092001: combined-inference model for recognizing the wave stage of national economy M092002: combined-inference model for recognizing the state characteristics of national economy

M090501: combined-inference model for generating the countermeasure of economic adjustment and control

M090502: combined-inference model for generating the policy of economic adjustment and control

K42J0010101: knowledge base for adjusting and controlling the decrease of production

K42J0010102: knowledge base for adjusting and controlling the fast increase of economy

K42J0010103: knowledge base for adjusting and controlling the inflation

K42J0010104: knowledge base for adjusting and controlling the soft market

K42J0010105: knowledge base for adjusting and controlling the imbalance of economic structure

3. It is better for the user to choose the scheme M090501: ‘combined-inference model for generating the countermeasures of economic adjustment and control’ as the solving scheme of problem T07100010103.

## 3.3. Model chain editing

The solving scheme, derived by the above process for a problem, may be composed of one or more models, which are arranged by their logic order under the user’s interaction. The model chain editor has been developed for the user to add models, delete models and change the model order to form the model chain by the logic order. In the following, the man-machine interacting process to edit the model chain is given.

1. Display the auto-organizing model chain for the user;

2. Change the sequence of the models in the model chain according to the user’s requirements;

3. Input the index number of the models to be appended, if the user wants to add some models to the model chain;

4. Input the index number of the models to be deleted, if users want to delete some models in the problem chain;

5. Update the model order number of the model chain by moving the cursor, if the operation of adding or deleting models has been done by the user.

In the prototype of SXSES-DSS, the problem T010000103 is named as ‘Analyzing the long-run trend of main objectives of coordinate development of society, economy, science and technology in Shaanxi Province’. Once it is selected, the user would edit and get the model chain under the model chain editor: M190101, M060204, M120204, M110202, M180201, M010304, M210105, M020201, M010202, M010101, M010301, M090501 .4

## 4. Flexible connection and dynamic integration of different models

In the above section, we have described that the required information resources for DSS to solve the user’s problem have been given in the problem solving chain-path. Moreover, to reach the dynamic integration of problem solving it is necessary to have the related information among the models in the model chain $M _ { \mathrm { c } }$ . Here, the related information among the models can be set for the user to interact with DSS based on the user-owned dynamic information and knowledge.

So for $M _ { \mathrm { c } } = \{ M _ { \mathrm { c i } } | \mathrm { i } = 1 , \dots , \mathrm { k } \}$ , we have the connection information set $R _ { \mathrm { i j } }$ between model $m _ { \mathrm { i } }$ and $m _ { \mathrm { j } } { \mathrm { : } }$

$$
R _ {\mathrm{ij}} = \left\{r _ {\mathrm{ij}} ^ {(1)}, r _ {\mathrm{ij}} ^ {(2)}, \dots , r _ {\mathrm{ij}} ^ {(\mathrm{h})} \right\} (i <   j)
$$

Where

$r _ { \mathrm { i j } } ^ { ( \alpha ) } ( \alpha = 1$ . , h stands for number output-to-input relation between model $m _ { \mathrm { i } }$ and $m _ { \mathrm { j } } ,$

h stands for h output-to-input relations included in $R _ { \mathrm { i j } } ^ { } .$

Let $U _ { \mathrm { i } } = \{ u _ { \mathrm { i } } ^ { ( 1 ) } , \dots , u _ { \mathrm { i } } ^ { ( \mathrm { g } ) } \}$ stand for g interactivegiven variables between user and DSS during the executive process of model $m _ { \mathrm { i } }$

Moreover, let $x _ { \mathrm { i j } } = m _ { \mathrm { i } } R _ { \mathrm { i j } } { \stackrel { \cdot } { m _ { \mathrm { i } } } } ( \mathrm { i } < \mathrm { j } )$ , then, there is a relation matrix $\dot { X } = \{ x _ { \mathrm { i j } } \}$ for the model chain $M _ { \mathrm { c } }$ $\mathbf { \Omega } = ( m _ { 1 } , \dots , m _ { \mathrm { k } } )$ in the problem solving chain-path $R _ { w }$ , that is

$$
m _ {1} \quad m _ {2} \quad m _ {3} \quad \dots m _ {\mathrm{i}} \dots \quad m _ {\mathrm{k-1}} \quad U s e r
$$

$$
m _ {1} \quad | \quad U _ {1}
$$

$$
m _ {\mathrm{j}} \qquad \left| \begin{array}{c c c c} R _ {1 \mathrm{j}} & R _ {2 \mathrm{j}} & R _ {3 \mathrm{j}} & \dots R _ {3 \mathrm{j}} \dots \end{array} \right.
$$

$$
m _ {\mathrm{k}} \qquad \left| \begin{array}{c c c c c c} R _ {1 \mathrm{k}} & R _ {2 \mathrm{k}} & R _ {3 \mathrm{k}} & \dots R _ {\mathrm{ik}} \dots & R _ {\mathrm{k-1k}} & U _ {\mathrm{k}} \end{array} \right.
$$

The connection information $R _ { \mathrm { i j } }$ is given with the following information structure in SXSES-DSS:

$$
R _ {\mathrm{ij}} = \left\{p, d _ {\mathrm{i}}, m _ {\mathrm{i}}, m _ {\mathrm{j}}, t _ {\mathrm{b}}, v, t _ {\mathrm{j}} \right\}
$$

Where

$p$ is the problem index number,

$m _ { \mathrm { i } }$ is the source model index number, $d _ { \mathrm { i } }$ is the output data index of source model stored in decision support database,

$m _ { \mathrm { j } }$ is the target model index,

$t _ { \mathrm { b } }$ is the input table name of target model $m _ { \mathrm { j } } ,$

$v$ is the input variable name in input table $t _ { \mathrm { b } } ,$

$t _ { \mathrm { j } }$ is the data type of variable Õ.

According to the matrix X, model $m _ { \mathrm { i } }$ has the following connection information in DSS. $\dot { C } _ { 1 } = U _ { 1 } C _ { \mathrm { j } }$ $= \{ R _ { 1 \mathrm { i } } , \ R _ { 2 \mathrm { i } } , \ldots , \ R _ { \mathrm { i - 1 } \mathrm { i } } , \ U _ { \mathrm { i } } \} , ( \mathrm { j } = 2 , \ldots , \mathrm { k } )$

Here, $C _ { 1 } , C _ { 2 } , \ldots ,$ and $C _ { \mathrm { k } }$ should be flexible in composition, arrangement and task assignment between DSS and users for different users. The value of them should be dynamically obtained during the integration of the models in $M _ { \mathrm { c } }$

To deliver the flexible and dynamic connection information, the model connection organizing component has been developed, which is used for the user to choose the connection variables among the models in the model chain based on the requirement of problem solving and the user’s recognition.

On the other hand, during the execution of the integrated solving scheme, a connected variable may have different values to give because of the repeating operation of the source model under the different user’s interactive alternatives. So a dynamic integration information acquiring component in DSS is required.

The dynamic integration information structure is presented in the following formula.

$$
r _ {v} ^ {(t)} = \left(a, d _ {\mathrm{i}}, m _ {\mathrm{i}}, m _ {\mathrm{j}}, t _ {\mathrm{b}}, v, t _ {\mathrm{j}}, t\right)
$$

Where

$r _ { v } ^ { ( t ) }$ stands for the dynamic integration information structure for input variable Õ at time t,

a stands for the alternative number of the output from source model,

$d _ { \mathrm { i } } , \ m _ { \mathrm { i } } , \ m _ { \mathrm { j } } , \ t _ { \mathrm { b } } , \ v , \ t _ { \mathrm { j } }$ mean the same as above formula,

t is the time variable.

Furthermore, the source model $m _ { \mathrm { i } }$ will be executed before the target model $m _ { \mathrm { j } } .$ . The output of model $m _ { \mathrm { i } }$ will be transferred from its working output tables to the decision support data base for model $m _ { \mathrm { j } }$

In the prototype of SXSES-DSS, the implemented model connection organizing component supports the user to perform the flexible connection of different models in the model chain by the following steps:

1. Run the model integration organizing component;

2. Display the stored connection information;

3. Display the names of the input variables of the target model;

4. Display the names of the output variables of the resource model;

5. Select the input variables and output variables by moving the cursor, if the user wants to append the connection information;

6. Reset the output variable by moving the cursor if the user wants to change a connection relation;

7. Move the cursor to the input variable and deleting it, if the user wants to delete a connection relation;

8. Repeat $2 \sim 7$ steps until the user has built all the required connection relations.

During the execution of the flexible and dynamic integrated solving scheme, the user can control the decision support process by the following three approaches:

1. Repeat the operation of the current model;

2. Perform the operation of the former part of models in the model chain and returning, after a break or more time redoing the solving scheme by jumping to a remaining model;

3. Go back to the former model by inputting its model index, if a former model does not provide correct input data for the latter models.

For each model, the operation process is doing as follows:

1. Acquire the required input data from the decision support data base and users;

2. Schedule the related resources to execute the model;

3. Generate the special model based on the scheduled resources;

4. Execute the model and putting the results into work output tables;

5. Formulate the output in forms of graph, table and explaining text based on the data in the working output tables;

6. Display the output for users, if the users appreciate the output, go to step 7, else repeat the steps $1 \sim 6$ for the same model;

7. Transfer the results from working output tables to decision support data base giving the same alternative number.

## 5. Controllable outputting of problem solutions

In the prototype of SXSES-DSS, the users can control the process of outputting the problem solu tions by the following approaches 5 :<sup>w</sup> <sup>x</sup>

1. Display the solutions in forms of graphs, tables, distributed maps and reports by the users’ requirements;

2. Reorganize the solutions by the users’ requirements to form a combined decision support report file for printing out.

Here, the combined decision support report may be provided by the following three forms in the prototype of SXSES-DSS.

Ž . 1 One-problem and one-model solving scheme. The combined decision support report consists of the graphs, texts for explaining the graphs and the explaining report for all the solution of the model. Here the model includes knowledge model and case model;

Ž . 2 One-problem and model-chain solving scheme. The combined decision support report is composed of the graphs, texts for explaining the graphs and tables generated under the operation of all the models in the model chain, as well as the explaining report for all the solutions of the models;

Ž . 3 Problem-chain and model-chain solving scheme. The combined decision support report is composed of many sub-problem decision support reports of all the one-problem and model-chain solving schemes by the problem chain.

## 6. Conclusion

In this paper, a flexible and dynamic integrated problem solving approach FPDI has been pre-Ž . sented. By the FPDI approach, the integrated solving scheme of the user’s problem consists of the problem solving chain-path and its connection information of different models. The problem solving is implemented with three steps:

1. Do the flexible generation of problem solving chain-path,

2. Do the connection and dynamic integration of different models in the model chains, and

3. Output the problem solutions by the user’s requirement.

In the prototype of SXSES-DSS, FPDI approach has been implemented in the environment with six parts, which are given as follows:

1. Problem Chain Editor

2. Interactive Problem Solving Component

3. Model Chain Editor

4. Model Connection Organizing Component

5. Dynamic Integration Information Acquiring Component

6. Solution Synthesizing Editor

It is worth noticing that the synthesizing task based on the combined decision support report is allocated to the users in SXSES-DSS. Therefore, on one hand, the users can depend on the decision support delivered by DSS, and on the other hand, the users would also interact or even control the decision support process to obtain their required decision support.

## References

<sup>w</sup> <sup>x</sup> 1 D.R. Dolle, J.E. Kottemann, Model integration and a theory of models, Decision Support Systems 9 1993 51–63.Ž .

<sup>w</sup> <sup>x</sup> 2 Ting Ping Liang, Development of a knowledge based model management system, Operations Research 36 6 1988 849–Ž . Ž . 863.

<sup>w</sup> <sup>x</sup> 3 Ajay Vinze, Arun Sen, Expert assistance for the decision support process using hierarchical planning, IEEE Transactions on Systems, Man and Cybernetics 21 2 1991 390–400.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 P.Z. Zhang, C.Z. Han, B.W. Wan, Problem recognizing environment and implementation for intelligent decision support systems, Journal of Systems Engineering 2 1 1993 1–8, inŽ . Ž . Ž Chinese ..

<sup>w</sup> <sup>x</sup> 5 P.Z. Zhang, C.Z. Han, B.W. Wan, Problem processing approaches and implementation for problem-driven intelligent decision support, 1, Information and Systems Engineering 1 Ž . Ž . 2 1995 149–158.

![](/api/attachments/AU7H6BM9/fulltext/images/cdb3f90ba5650e5d7946bc20473a414dd3da45b4c466aa61243332a3025a2e91.jpg)

Yingluo Wang is Senior Professor of Systems Engineering and Industrial Engineering in the School of Managemen at Xi’an Jiaotong University, China. He is the Vice Director of China Systems Engineering Society from 1992. He has obtained a first-grade prize from China’s National Science and Technology Progress and several national, provincial and ministerial awards. His papers have appeared in several journals, including Computer and Industrial Engineering,

Pengzhu Zhang is currently Professor of Management Science and Systems Engineering in the School of Management at Xi’an Jiaotong University, China. He received his Ph. D. in Systems Engineering from Xi’an Jiaotong University in 1993. He also holds a B. Sc. in Mining Engineering and a M. Sc. in Mining System Engineering from Shandong Institute of Mining Technology. Aspects of his research have appeared in Information and Systems Engineering

Systems Science and Systems Engineering. His present research interests are manufacturing systems management and finance engineering.

![](/api/attachments/AU7H6BM9/fulltext/images/4a328a8b3c07fb37f5051e5198f685df97f6e7d3fd6a5e3666b58508ae42eb8b.jpg)

and other Chinese journals. His current research interests include intelligent decision support systems, expert systems, risk management and Internet-based firm management.
