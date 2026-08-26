---
otero_id: 19616
otero_key: "W8JCQZ4G"
title: "Improved simulated annealing based risk interaction network model for project risk response decisions"
authors: "Lei Wang; Mark Goh; Ronggui Ding; Leon Pretorius"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.05.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Improved simulated annealing based risk interaction network model for project risk response decisions

ELSEVIER Decision Support Systems

Lei Wang, Mark Goh, Ronggui Ding, Leon Pretorius

![](/api/attachments/W8JCQZ4G/fulltext/images/2abbaa602b191278b853ea7048831baa83818916511aa2408e1dffb22d0c320d.jpg)

PII: S0167-9236(19)30078-8

DOI: https://doi.org/10.1016/j.dss.2019.05.002

Reference: DECSUP 13062

To appear in: Decision Support Systems

Received date: 24 October 2018

Revised date: 3 May 2019

Accepted date: 5 May 2019

Please cite this article as: L. Wang, M. Goh, R. Ding, et al., Improved simulated annealing based risk interaction network model for project risk response decisions, Decision Support Systems, https://doi.org/10.1016/j.dss.2019.05.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Improved Simulated Annealing Based Risk Interaction Network Model for Project Risk Response Decisions

Lei Wang<sup>\*a,b</sup>, Mark Goh <sup>b,c</sup>, Ronggui Ding <sup>a</sup>, Leon Pretorius <sup>d</sup>

<sup>a</sup> School of Management, Shandong University, Jinan, China

<sup>b</sup> The Logistics Institute – Asia Pacific, National University of Singapore, 21 Heng Mui Keng Terrace, Singapore

<sup>c</sup> NUS Business School, National University of Singapore, 1 Business Link, Singapore

<sup>d</sup> Graduate School of Technology Management, University of Pretoria, Pretoria, South Africa

## Highlights

1. Integrate a simulation-based network model and improved simulated annealing algorithm for optimizing risk response decisions.

2. A simulation model of capturing project risk interaction is formed for evaluating the risk response decisions.

3. An improved simulated annealing algorithm is proposed through enhancing its neighborhood search using social network analysis.

4. Two indices of social network analysis are designed for finding the key nodes and edges in the project risk interaction network.

# ACCEPTED MANUSCRIPT

Abstract: Risk interaction changes the probability and impact of a given risk, which may result in a less effective risk response decision (RD). This study presents an approach for supporting the project manager in making RDs, comprising a simulation model of risk interaction network (RIN) for evaluating the RDs and an improved simulated annealing (SA) algorithm for optimizing the RDs. The simulation model considers different risk levels and the corresponding risk interaction cases, which is closer to the reality. In addition to tailoring the SA algorithm to optimize RDs, it is improved through enhancing its neighborhood search with the aid of social network analysis. Specifically, two new network indices are designed for calculating the quantitative significance of RIN elements, i.e. the nodes that denote risks and edges that reflect the risk interactions. The element with a higher significance is more likely to be dealt with when generating a new RD in the neighborhood search. An application is provided to illustrate the utility of the proposed approach; a contrastive analysis of the improved SA and standard SA is also conducted to validate the effectiveness and efficiency of the former.

Keywords: Project risk response; Network dynamic analysis; Risk interaction; Social network analysis; Simulated annealing.

## 1. Introduction

A project is “a temporary and unique endeavor undertaken to deliver a result”, and the characteristics of risk to be the entity that appears in all aspects of projects [1, 2]. The need for project risk management is therefore well documented. In project risk management, the risk response phase follows from the phase of risk assessment, which decides on the rank order of the risks [1]. As it is not feasibly possible for projects to manage all the risks equally, the risk response decision (RD) is usually proposed to take care of the more critical risks [3, 4].

Risk interaction is gaining traction due to the greater project complexity [4, 5], which means that an identified risk is typically likely to trigger the occurrence of another one. Conventionally, risks are ranked on account of the criticality, which is defined as the product of risk spontaneous probability and impact. However, the interactions among risks may affect their probabilities and impacts [6]. For instance, if a risk is triggered by other risks, then its occurrence probability would be higher than the case without any risk interaction [6]; a risk would have a greater impact if it can cause the occurrence of any other risk. Therefore, risk interactions can alter the risk ranking outcome [2, 6], and may lead to a complex RD making process. For instance, a proactive action eliminating the spontaneous probability of a risk may not be effective in the presence of risk interactions [7].

In the context of risk interactions, researchers typically addressed the RD issue through integrating the RD evaluation model and the RD optimization model [8, 9]. The evaluation model is used to determine the value of the objective function under the given risk probability and impact, which have been changed based on the RD from the optimization model. The optimization model searches for optimal or satisfied RD based on the output of the evaluation model.

Specifically, the RD evaluation model is mostly constructed as a network whose nodes and edges represent risks and risk interactions respectively [7, 9]. A node is related to the spontaneous probability and loss of a risk, and an edge is the likelihood of a risk given that another risk has occurred. Therefore, the analytical methods based models, e.g. the model formed by the probability and impact matrices [8, 9], the model within a Bayesian belief network [10], the model based on the Bow-tie analysis [11] etc., are used to determine the value of the objective function. The objective function usually considers the total risk cost [8], deviation-based measures [1], and the utility of the decision makers [9] etc., to be content. For the RD optimization model, an RD is a combination of risk actions. Each risk action is defined as eliminating the spontaneous probability of or loss due to a risk, or the transition probability between two risks. Accordingly, an RD is presented by a set of binary decision variables; 1 for taking the corresponding risk actions and 0 otherwise [12]. Therefore, the approach that integer linear programming method (ILPM) is commonly used for optimizing the RDs [12-14]. The solution techniques offer exact or heuristic RD [15]. The former is obtained by the special-purpose techniques, such as column generation, branch-and-cut and branch-and-bound [12], solvable through the state-of-the-art solver LINGO [9, 11-13]. The latter is determined by heuristic-based approaches, such as the greedy algorithm [8] and the genetic algorithm [6, 16].

# ACCEPTED MANUSCRIPT

However, the risk interaction poses two intractable problems for the analytical models. In these models, the risk level is treated as a constant [5]. Unfortunately, embracing risk interaction, the level of a given risk should rightly vary with the number of the risks that trigger it simultaneously [2, 6]. In addition, the risk interaction network (RIN) may display the loop phenomenon, namely a causal path that starts from an initial risk leading to the subsequent occurrence of risks until the initial risk resurfaces [7]. Analytical models are inadequate for treating such cases. Therefore, a simulation-based model of RIN is adopted to serve as the RD evaluation model. This is then considered as one the of the contributions offered in this paper.

At the same time, the effect of a risk action differs in level [2, 15, 17], leading to the requirement of a more precise setting of the decision variables. Consider a risk whose spontaneous probability is 0.7, the related decision variable is the reduced value of its spontaneous probability, i.e. 0, 0.1, 0.2 … 0.7. These numerical decision variables lead to a rather large number of combinations of the risk actions. Consequently, searching the optimal combination is a classical non-deterministic polynomial-time hard problem, which generally befits the use of heuristics. Therefore, a heuristic method named the simulated annealing (SA) algorithm is typically adopted in the optimization model considering its good performance in addressing the combinational optimization problem [18, 19].

Also, the heuristic method is confronted with a computing time problem. Specifically, SA generates the new RDs randomly and search for the optimal RD by testing the RDs iteratively. However, testing the RDs relays on the evolution model, i.e. the RIN simulation model in this paper, which consumes much computational effort to yield a representative value as it is stochastic [2, 7]. Therefore, searching for the optimal or near optimal RD is extremely time-consuming. Even though some researchers applied heuristic methods to the RD optimization model [6, 8, 16], they paid scant attention to improving the heuristics. In this work, following the social network analysis (SNA), two new network indices are proposed to calculate the quantitative significance of the nodes and edges in the RIN. This is then applied to enhance the performance of the SA by increasing the likelihood of generating better RDs, which is the main academic contribution of this paper.

The rest of this paper is structured as follows. Section 2 provides the framework of our approach. The simulation model of RIN is presented in Section 3. Section 4 discusses the application of social network analysis, and the improved SA algorithm is described in Section 5. Computational results for an illustrated example are reported in Section 6, and finally, a summary of this study and some possible future research are provided in Section 7.

## 2. Framework of decision support system for project risk response decisions

Traditional risk management assumes that a risk is triggered by the random factors [5]. However, with the consideration of risk interactions, the occurrence of a risk can come from other risks that direct to it in the RIN [4]. Fig. 1 gives the examples of risk occurrence type.

![](/api/attachments/W8JCQZ4G/fulltext/images/7b112712cb3caeb1e823c71d162403302d7f5e9e3aebcdc98900a44b49f0c73a.jpg)  
Fig. 1 Occurrence types of a risk in the RIN

Consider risk 03 and risk 04 for example, which are respectively named as R03 and R04 in Fig. 1. Some random factors contributing to R03 are not identified due to their small effect to project or possibly a lack R03 is activated by an associated risk R04, then we have a secondary risk occurrence for R03.

It should be noted that the change of the risk occurrence is coupled with a change of risk management. The traditional project risk management is commonly regarded as a systematic process of risk identification, risk assessment, risk response and so forth [1]. As the existence of risk interactions, the process is then adjusted. For instance, the identification phase should involve the risk identification as

# ACCEPTED MANUSCRIPT

well as the risk interaction identification. Following Fang and Marle’s work [7], a framework of decision support system (DSS) for project risk RDs is put forward. The framework consists of four phases: (1) RIN identification; (2) RIN assessment; (3) the social network analysis of RIN; (4) RD optimization. Fig. 2 depicts this framework. This paper focuses on the phases (3) and (4), whose input is the matrices of RIN from phases (1) and (2).

![](/api/attachments/W8JCQZ4G/fulltext/images/e9dba758eaef1bfaa4a659445e58093d2bfba4ed8420f177e241afab4416372f.jpg)  
Fig. 2. Framework of DSS for project risk RDs

In phase (1), risks are identified by the project team, project manager and experts, and the result is a project risk list [7]. Consequently, risk interactions are identified and presented as a binary matrix, such that if risk is likely to trigger risk , then the entry in the -th row and -th column has a value of 1.

In phase (2) of the network assessment, the attributes of the node, also noted as risk spontaneous probability and loss are evaluated. Meanwhile, the edges recorded as 1 in the binary matrix of phase (1) are evaluated as transition probabilities between risks, and as a result, the binary matrix is transformed into a numerical one.

Phase (3) conducts the social network analysis to ascertain the quantitative significance of the nodes (risks) and edges (risk interactions) in the RIN. The importance of a node not only relies on the probability of and the loss due to its corresponding risk but also its network position. For example, if a node directs many other nodes in the RIN, its corresponding risk can cause loss through triggering other risks. The edge importance is also related to its network position, which will be discussed in the next section.

The RD optimization of phase (4) consists of three activities: (a) constructing RIN simulation model; (b) improving SA algorithm using the output of SNA; (c) searching for an optimal or near optimal RD relying on (a) and (b).

The project team members, project manager and experts provide the knowledge and information of the project. This is then translated into data and fed into the DSS in phases (1) and (2) of the framework presented in this section. DSS will then output the “best” risk RD comprised of prototypical risk actions in phase (4). Each action is presented by a decision variable. For instance, assuming a variable equal to 0.3, this points to a need to lower a spontaneous probability of a risk or the transition probability between two risks by 0.3. The decision makers can then put forward concrete action by assigning risk control responsibilities and allocating the necessary resources. Consequently, a project risk response plan is obtained.

## Simulation model of risk interaction network

The RIN simulation model serves as the RD evaluation model. The data on risks and risk interactions form the basic input of this model, which is found from the identification and assessment of RIN. An RD will change the input data, leading to a new RIN. Hence, the output of the simulation model is the evaluation of the RIN as well as the corresponding RD. The output is computed by running the model enough times as it is stochastic, to this end, the dynamic process and evaluation approach of RIN are determined in this section.

## 3.1. Identification and assessment of risk interaction network

In terms of describing a network, the design structure matrix is useful [7], which is similar to the adjacent matrix in the SNA and network dynamic analysis [2]. Accordingly, assume a binary and square matrix $\mathcal { B } \mathcal { M } = \left[ b m _ { i j } \right]$ , where $b m _ { i j } = 1$ if risk can cause risk directly. For illustration purpose, Fig. 3 shows an example on using to represent the RIN.

![](/api/attachments/W8JCQZ4G/fulltext/images/79371dc5d8ac5bee2d28e35dc3b0808b945e54297faf8e52b22a97f01c64829f.jpg)

<table><tr><td>$ \underline{\text{↑}} $</td><td>R01</td><td>R02</td><td>R03</td><td>R04</td><td>R05</td><td>R06</td><td>R07</td><td>R08</td><td>R09</td></tr><tr><td>R01</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>R02</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>R03</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>R04</td><td></td><td></td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>R05</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>R06</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>R07</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>R08</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>R09</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/W8JCQZ4G/fulltext/images/217c5c648dc608d044324555ed540d683b6446ad6cde6d3cbe15a93ef329784b.jpg)  
Fig. 3 Illustration of a binary matrix of RIN (adapted from [7])

Matrix is developed from the identification of RIN. This can for example be done using the classical methods of project management, such as the Delphi-based approach [9]. This method can ensure the accuracy of the RIN identification and involves a number of stages: the decision makers are interviewed anonymously and separately, collect and combine their opinions regarding the risks and risk interactions that should be identified, fed back the result to them and then interview each decision maker again. These stages may repeat again and again before these opinions are consentaneous. Besides, other methods and tools, such as risk list [9], work breakdown structure [1, 8, 9, 12], cost breakdown structure [1], are adopted in the literature for increasing the accuracy of the RIN identification result.

The RIN assessment entails evaluating the attributes of the nodes and edges, such as risk spontaneous probability, risk loss and transition probability between the risks [7]. As an illustration of this, Fig. 4 (a) shows the process of evaluating the probabilities.

![](/api/attachments/W8JCQZ4G/fulltext/images/1424bf4b742cf93d296b9b1c8ad8e25a06e77c8b61e0633cf1176910d51df6cf.jpg)  
(a)  
Identification of risks and risk interactions

![](/api/attachments/W8JCQZ4G/fulltext/images/bb680c78e5a79b5f69e651ff876aa4e2c5046d3516c86b77123ea9916966bcf9.jpg)  
(b)  
Evaluation of transition probability  
(c)  
Evaluation of spontaneous probability  
Fig. 4 Illustration of evaluating the probabilities of RIN

# ACCEPTED MANUSCRIPT

In Fig. 4 (a), the parameters have the value of 1 in are estimated directly by the project team, project manager and expert. The binary matrix thus transforms into a transition probability matrix as shown in Fig. 4(b). Meanwhile, the spontaneous probabilities of the risks are estimated. For the sake of simplicity, the parameter $m _ { i i }$ on the matrix diagonal represents the spontaneous probability of risk , as shown in Fig. 4(c).

Compared with the traditional risk perception, the risk interactions generate varied risk occurrence cases. Follow the assumption that “A risk may occur more than once during the project (as witnessed in practical situations). Risk frequency is thus accumulative if arising from different causes or if arising several times from the same cause.” [20], an assumption is consequently put forward. If risk is triggered by different risks or random factors simultaneously, its level is higher than that triggered by one risk or random factors alone.

Furthermore, when risk triggers risk , risk ’s level depends on the level of risk as well. For the purpose of evaluating such levels of risk more accurately, an approach following relative assessment is adopted [7, 21]. Specifically, let the most common level of risk be its general level, denoted by $g _ { i }$ Pairwise comparisons are then conducted between each of risk ’s levels and $g _ { i }$ . The level coefficients are thus obtained. The value of a level of risk is calculated as the product of the related coefficient and $g _ { i }$ . Besides, the probability of risk triggering risk varies with risk ’s level as well. The parameter $m _ { i j }$ in can be regarded as the general transition probability of risk causing the general level of risk . The relative assessment is conducted again to yield the transition probabilities from risk to risk . Apart from the relative assessment that takes the general level or transition probability as the reference, there are other methods and tools capable of ensuring the quality of RIN assessment. For instance, the improved pairwise comparison from Analytic Hierarchy Process [7], the adjusted pairwise comparison from Best Worst Method [2, 21], the approach avoiding the need to moderate divergences and consistency test [9]. Take R04 and R03 as an example, Fig. 5 introduces the different cases in which the level of R04 influences the transition probability and R03’s level.

![](/api/attachments/W8JCQZ4G/fulltext/images/3cf6548b02734dec1872a68faa3046588813348f892f8431cbd547251825b1e7.jpg)

<table><tr><td>R04→R03</td><td>Upper limit</td><td>Lower limit</td><td>Probability coefficient 1</td><td>Level coefficient 2</td><td>Transition probability 3=0.7×1</td><td>Level 4=2×2</td></tr><tr><td>Case 01</td><td>2</td><td>4</td><td>0.8</td><td>0.5</td><td>0.56</td><td>1</td></tr><tr><td>Case 02</td><td>4</td><td>6</td><td>1</td><td>1</td><td>0.70</td><td>2</td></tr><tr><td>Case 03</td><td>6</td><td>8</td><td>1.2</td><td>2</td><td>0.84</td><td>4</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

Note:  
Assume the general level of R03 is 2.  
The general transition probability from R04 to R03 is 0.7.

Fig. 5 The influence of R04 level on the transition probability and level of R03

In Fig. 5, take Case 01 for example. When $\mathrm { R } 0 4 \mathrm { : } \mathrm { s }$ level range from 2 to 4, the decision makers compare the likelihood of triggering R03 with the general transition probability from R04 to R03 (i.e. 0.7). The probability coefficient is 0.8, and then the transition probability of Case 01 is . At the same time, the caused level of R03 in this case is compared with $\mathrm { R } 0 3 ^ { \circ } \mathrm { s }$ general level (i.e. 2), from which the level coefficient is evaluated as 0.5. Accordingly, the level of R03 is .

## 3.2. Dynamic process of risk interaction network

The primary and secondary occurrences of the risks lead to the dynamic process of the RIN, which is presented as the changing of each risk’s level. The Monte Carlo method is used to see whether a risk occurs or not in a specific period of the project lifecycle. For instance, in a situation of primary occurrence, if the generated random number is no more than the spontaneous probability of risk , then risk occurs. Let matrix $\mathcal { C } ^ { t } = [ c _ { j i } ^ { t } ]$ , where $c _ { j i } ^ { t } = 1$ if risk happens in the form of primary occurrence or secondary occurrence $( j \neq i )$ in period , and 0 otherwise.

## (1) The process of primary risk occurrence

In the Monte Carlo method, performs the function of generating the random values over the interval [0, 1]. Through comparing the random number and risk $i ^ { \ ' }$ s spontaneous probability $m _ { i i }$ , the value of $c _ { i i } ^ { t }$ that denotes whether risk is triggered by the its random factors or not is set as:

$$
c _ {i i} ^ {t} = \left\{ \begin{array}{l} 1, r a n d (0, 1) \leq m _ {i i} \\ 0, r a n d (0, 1) > m _ {i i}, \end{array} \right.\tag{1}
$$

Accordingly, the risk level $d p _ { i } ^ { t }$ related to the primary occurrence in period is found from $c _ { i i } ^ { t } \times d p _ { i }$ where $d p _ { i }$ is the level of risk when it is triggered by the random factors.

## (2) The process of secondary risk occurrence

If risk is directed by risk in the RIN, the transition probability from risk to risk in period , denoted by $p _ { j i } ^ { t }$ , is influenced by the level of risk in period $t - 1 ( t \geq 2 )$ and written as:

$$
p _ {j i} ^ {t} = \left\{ \begin{array}{c} s _ {j i _ {1}}, D _ {j i _ {1}} \leq d _ {j} ^ {t - 1} <   D _ {j i _ {2}} \\ s _ {j i _ {2}}, D _ {j i _ {2}} \leq d _ {j} ^ {t - 1} <   D _ {j i _ {3}} \\ \dots \\ s _ {j i _ {h}}, D _ {j i _ {h}} \leq d _ {j} ^ {t - 1} <   D _ {j i _ {h + 1}} \\ \dots \\ s _ {j i _ {h _ {t o t a l}}}, D _ {j i _ {h _ {t o t a l}}} \leq d _ {j} ^ {t - 1} \end{array} , i \neq j, t \neq 1, \right.\tag{2}
$$

where $s _ { j i _ { h } }$ is the transition probability from risk to risk in the case , which is related to ③ in Fig. 5; $D _ { j i _ { h } }$ and $D _ { j i _ { h + 1 } }$ are the lower and upper bounds of case respectively; $d _ { j } ^ { t - 1 }$ is the level of risk in period and $i _ { h _ { t o t a l } }$ is the total number of the cases.

Therefore, the value of $c _ { j i } ^ { t }$ denoting whether risk is triggered by risk in the period is given as:

$$
c _ {j i} ^ {t} = \left\{ \begin{array}{l} 1, r a n d (0, 1) \leq p _ {j i} ^ {t}, \\ 0, r a n d (0, 1) > p _ {j i} ^ {t}, i \neq j, t \geq 2, \end{array} \right.\tag{3}
$$

Following Fig. 5, when risk is triggered by the risk , i.e. $c _ { j i } ^ { t } = 1$ , the level of risk in period will also influence the level of risk in period :

$$
d s _ {j i} ^ {t} = \left\{ \begin{array}{l l} c _ {j i} ^ {t} \times d s _ {j i _ {1}}, D _ {j i _ {1}} \leq d _ {j} ^ {t - 1} <   D _ {j i _ {2}} \\ c _ {j i} ^ {t} \times d s _ {j i _ {2}}, D _ {j i _ {2}} \leq d _ {j} ^ {t - 1} <   D _ {j i _ {3}} \\ \dots \\ c _ {j i} ^ {t} \times d s _ {j i _ {h}}, D _ {j i _ {h}} \leq d _ {j} ^ {t - 1} <   D _ {j i _ {h + 1}} \\ \dots \\ c _ {j i} ^ {t} \times d s _ {j i _ {h _ {t o t a l}}}, D _ {j i _ {h _ {t o t a l}}} \leq d _ {j} ^ {t - 1} \end{array} , i \neq j, t \neq 1. \right.\tag{4}
$$

When , there is no secondary occurrence of risk , so $d s _ { j i } ^ { 1 } { = } 0$

The secondary level of risk caused by all the other risks in period is now stated as:

$$
d s _ {i} ^ {t} = \sum_ {j = 1, j \neq i} ^ {N} d s _ {j i} ^ {t},\tag{5}
$$

where is the volume of identified risks.

Mathematically, the level of risk at the end of period , $d _ { i } ^ { t }$ , is equal to ${ d _ { i } ^ { t - 1 } + d p _ { i } ^ { t } + d s _ { i } ^ { t } }$ Besides, the value of $d _ { i } ^ { t }$ is also influenced by the timeliness of risk elimination during the project lifecycle. When risk occurs, it can be eliminated immediately in the period or in the future periods. We assume that the increased level of risk in the period will be eliminated in the period ( .

## 3.3. Evaluation approach of risk interaction network

An RD changes the input data of the RIN simulation model. Thus the evaluation of this model is also the performance measure of the corresponding RD, which represented by the total risk loss caused by the occurrences of all the risks in the project lifecycle, now written as:

$$
L = \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {N} \left(l u _ {i} \times \left(d p _ {i} ^ {t} + d s _ {i} ^ {t}\right)\right),\tag{6}
$$

where is the duration of the project, $l u _ { i }$ is the loss of risk ’s unit level.

The RIN model is stochastic, this calls for a simulation approach to estimate the total risk loss [6, 7]. Therefore, a stable value of is needed, which can be obtained by simulating RIN model for as many iterations as required. For this, $L ( q )$ is selected to represent the output of the -th simulation run. The arithmetic mean is given by $\widehat { L ( Q ) }$ when the number of simulation interactions is . As increases, the fluctuation of $\widehat { L ( Q ) }$ will decrease. When the fluctuation falls below a given small value, termed as , the stable value is obtained [7].

In the process of computing a stable value, an extreme case may happen when Q is small. That is, the outputs of the simulations are almost the same but different from the stable value. In this case, it is easy to obtain the wrong stable value as the fluctuation of $\widehat { L ( Q ) }$ may be small. Therefore, a warming-up process sufficient number of times, denoted by $Q _ { w a r m }$ , will the program judge whether the stable value has been obtained. Further, the warming-up process helps to determine the value of as well. Specifically, after the warming-up process, the model has ran $Q _ { w a r m }$ times, the corresponding $L ( \widehat { Q _ { w a r m } } )$ denotes the order of the magnitude of the stable value. Combining with the required precision on the evaluation of RD, denoted by , the criterion for evaluating the stable value is formulated as [7]:

$$
\frac {1}{Q _ {e n d}} \times \sum_ {q = 1} ^ {Q _ {e n d}} L (q) - \frac {1}{Q} \times \sum_ {q = 1} ^ {Q _ {e n d}} L (q) <   \frac {P r e c i s i o n}{Q _ {w a r m}} \times \sum_ {q = 1} ^ {Q _ {w a r m}} L (q), Q _ {e n d} \geq Q _ {w a r m}.\tag{7}
$$

where $Q _ { e n d }$ is the simulation times of terminating the RIN simulation model.

Combing this criterion with the warming-up process makes the RIN simulation model be capable of terminating automatically. The stable value of is thus obtained with required and no redundant simulation times.

## 4. Social network analysis of risk interaction network

The RD is designed for minimizing the total risk loss by reducing the spontaneous probabilities of the risks and transition probabilities between the risks, which respectively correspond to the nodes and edges in the RIN. The SNA is used for improving SA through allowing the risk or risk interaction with a higher significance to be dealt with preferentially. Accordingly, this section continues by developing the network indices for quantifying the significance of the node and edge with respect to causing risk loss.

The concept of the path is vital in SNA, based on which some important indices of evaluating the importance of the node and edge, e.g. betweenness, closeness, are put forward [2]. Regard node and node as the start node and end node of a path respectively. The index of distance is used to describe the through this path [2, 22]. For example, in a communication network, if the distance of a path is small, node could send information to node quickly and accurately [2]. However, the index of distance is not suitable for evaluating the path in the RIN. It is the product of the edge values that denotes the impact from the node to node , i.e. the likelihood that risk would trigger risk through this path. Therefore, the impact from one node to another in the RIN is described by “power” instead of “distance” in this study.

A path from node to node can be described by a vector, where the related edges appear in order. Let $k _ { 1 }$ and $k _ { 2 }$ respectively be the start and end nodes of edge , the value of edge is then denoted as $m _ { k _ { 1 } k _ { 2 } }$ The power of this path is expressed as:

$$
P _ {R (i, j)} = \prod_ {k \in R (i, j)} m _ {k _ {1} k _ {2}},\tag{8}
$$

where $R ( i , j )$ is a path that from node to node and $P _ { R ( i , j ) }$ is the power of this path.

As there can exist more than one path from node to node . In the traditional SNA, The distance of the shortest path, i.e. the best path of constructing the impact between the nodes, is selected for reflecting the impact of node on node [22]. Likewise, the most powerful path with the maximum value regarding with Eq. (8) is taken into account in this paper. In the next discussion, without further illustration, the $P _ { i j }$

## 4.1. Network index of the node

The node significance can be gauged by the direct and indirect losses arising from its corresponding risk. The latter is related to the network position of the risk, as shown in Fig. 6.

![](/api/attachments/W8JCQZ4G/fulltext/images/0b862471932bf287a8dacee617bd28aaec1dfec796fc0235296115636c785540.jpg)  
Fig. 6 The network influence of risk

In Fig. 6, some risks in the RIN are influenced by risk , while the others are independent of it. If the paths from risk to the risks denoted by the blank circles are powerful, risk has a high likelihood of causing loss through triggering the occurrences of other risks in the RIN. The powers of these paths aggregate to the network impact of risk , denoted by $a _ { i } ,$ is defined as:

$$
a _ {i} = \sum_ {j = 1, j \neq i} ^ {N} P _ {i j}.\tag{9}
$$

With the consideration of the RIN characteristics, the index of $a _ { i }$ can be weighted from three aspects: the loss of risk risk ’s spontaneous probability, and the loss of the risks triggered by risk . Accordingly, the index of the weighted network power $w a _ { i }$ is updated from Eq. (9):

$$
w a _ {i} = m _ {i i} \times l _ {i} + m _ {i i} \times \sum_ {j = 1, j \neq i} ^ {N} P _ {i j} \times l _ {j}.\tag{10}
$$

where $l _ { i }$ is the loss due to the occurrence of risk and calculated as the product of the its unit loss and general level, i.e. $l u _ { i } \times g _ { i }$

## 4.2. Network index of the edge

Regarding a specific edge , its significance is mainly about the “bridge” function it supplies to the path of each pair nodes (see Fig. 7). In Fig. 7, the paths connecting the nodes on the left and nodes on the right rely on edge seriously. Therefore, edge is very important in such a network structure. This phenomenon is related to the “edge betweenness” in the theory of SNA, which is a measure of the centrality of an edge in the network [22].

![](/api/attachments/W8JCQZ4G/fulltext/images/525f6e04453cd31d9de33275bde4a5c5a99b4e3a553a30d214896793791ea354.jpg)  
Fig. 7 Illustration of the “bridge” function supplied by edge

In the traditional SNA, the shortest paths constructing the biggest impact between two nodes are considered to calculate the index of betweenness [23]. Similarly, in the RIN, the most powerful paths of one node pair are selected. The edge betweenness is defined as a probability, that is, the proportion of all the most powerful paths linking node and node which pass through edge , and is set as:

$$
b _ {k} (i, j) = \frac {W _ {(i , j) _ {k}}}{W _ {(i , j)}},\tag{11}
$$

where $b _ { k } ( i , j )$ is the betweenness of edge on the paths from risk to , $W _ { ( i , j ) _ { k } }$ is the number of most powerful paths from node $i$ to node that pass through edge , and $W _ { ( i , j ) }$ is the number of the most powerful path(s) from node to node .

Mathematically, the betweenness $b _ { k }$ of edge is the sum of its betweenness of each node pair:

$$
b _ {k} = \sum_ {i = 1} ^ {N} \sum_ {j = 1, j \neq i} ^ {N} b _ {k} (i, j).\tag{12}
$$

The index of $b _ { k } ( i , j )$ can be weighted as well by treating the following four aspects: the power of the most powerful path from node to node , edge ’s contribution to the path, the spontaneous probability of risk and the loss of risk . Accordingly, the weighted betweenness of edge on the paths from risk to risk is updated from Eq. (11):

$$
w b _ {k} (i, j) = \frac {1}{W _ {(i , j)}} \times P _ {i j} \times \sum_ {w = 1} ^ {W _ {(i, j)} k} \frac {m _ {k _ {1} k _ {2}}}{\sum_ {l \in R _ {w} (i , j) _ {k}} m _ {l _ {1} l _ {2}}} \times m _ {i i} \times l _ {j}.\tag{13}
$$

where $R _ { w } ( i , j ) _ { k }$ represents the -th most powerful path from node to node passing through edge .

Following Eq. (12), the weighted betweenness $w b _ { k }$ of edge is stated as:

$$
w b _ {k} = \sum_ {i = 1} ^ {N} \sum_ {j = 1, j \neq i} ^ {N} w b _ {k} (i, j) = \sum_ {i = 1} ^ {N} \sum_ {j = 1, j \neq i} ^ {N} \left(\frac {1}{W _ {(i , j)}} \times P _ {i j} \times \sum_ {w = 1} ^ {W } \frac {m _ {k _ {1} k _ {2}}}{\sum_ {l \in R _ {w} (i , j) _ {k}} m _ {l _ {1} l _ {2}}} \times m _ {i i} \times l _ {j}\right).\tag{14}
$$

$$
S = \left[ s _ {i j} \right]
$$

$$
s _ {i j} = \left\{ \begin{array}{c} w a, i = j \\ w b _ {k}, i \neq j, i = k _ {1}, j = k _ {2} \end{array} \right.,\tag{15}
$$

where $k _ { 1 }$ and $k _ { 2 }$ are the start and end nodes of edge respectively.

The proposed approach computing the network indices based on the most powerful paths. However, if there is no loop-phenomenon in RIN and the size of RIN is small, all the paths could be considered for improving the social network analysis. As a result, the indices can present the quantitative significance of the node and edge more accurately. Besides, if the loop-phenomenon appears in the RIN or the size of RIN is too big, the number of paths will be too large to be identified, recorded or analyzed. In this case, will be selected for computing the indices instead of the most powerful paths. The value of the threshold is set based on the expert experience, the complexity of RIN, the RIN size and the conditions for comping the indices.

## 5. Improved simulated annealing algorithm

SA is proposed by an analogy to physical annealing in solids. It is popularized by Kirkpatrick et al. [18], and has been applied to many hard combinatorial optimization problems in networks [19, 24]. In the SA algorithm, the neighborhood search method is a random process that allows all the decision variables to have the same probability to be changed [25], which increases the likelihood of local optima and the computing time [26]. In this paper, the SNA result, i.e. the quantitative significance of the risk and risk interaction, is applied to help the neighborhood search to find good candidate solutions, that is, letting the decision variables related to the important risks and risk interactions be more likely to be selected when generating a new RD. In this section, different parts of the improved SA are introduced, and the relations between them is explained.

## 5.1. RD representation and initial RD

Recall that a risk RD is a combination of prototypical risk actions, which can entail the elimination of the spontaneous probability of one risk or the transition probability between one pair of risks. Suppose the matrix $X = [ x _ { i j } ]$ represents an RD, where $x _ { i j }$ is the decreased value of spontaneous probability of risk if $i = j$ , or the transition probability from risk to risk ${ \mathrm { i f ~ } } i \neq j . \ { \mathrm { T h e } }$ value of $x _ { i j }$ is set as the integer times of the unit probability , which is set as 0.1 in this study. Fig. 8 illustrates the representation of RD. Note that, the RD in this work is conventionally titled the candidate solution in the heuristic method.

![](/api/attachments/W8JCQZ4G/fulltext/images/50c63a5db138c1a03797645a0b8544e31ecdee3450d79c1b741d7a756c5abc12.jpg)  
Fig. 8 Illustration of RD representation

No project can afford to manage all the potential risks, as it is subject to limited time and tight budget constraints [3, 4]. So the RD optimization is under the constraint of the total eliminated value regarding spontaneous probability and transition probability, which is denoted by [27]. Meanwhile, the value of the decision variable $x _ { i j }$ is no more than $m _ { i j }$ as the former is the decreased value of the latter. Accordingly, the optimization of RD has the following structure.

# ACCEPTED MANUSCRIPT

$$
\min \left(\sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {N} \left(l u _ {i} \times \left(d p _ {i} ^ {t} + d s _ {i} ^ {t}\right)\right)\right),\tag{16}
$$

s.t.

$$
0 \leq x _ {i j} \leq m _ {i j},\tag{17}
$$

$$
\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} x _ {i j} \leq T o t a l.\tag{18}
$$

The equal division method is used to determine the initial RD for the SA algorithm [19]. Only the parameters in whose value can be changed based on Eq. (18) are taken as the decision variables and the number of them is denoted by $N _ { x }$ . The application of this method includes two phases. The first phase increases all the decision variables by the value of $a v e _ { x }$ , which is equal to $f l o o r ( T o t a l / ( p u \times N _ { x } ) ) \times$ , where is a function that yields the greatest integer no more than . The second phase is assigning the remainder of to the decision variables arbitrarily. These two phases are shown as: Step 1: Calculate the value of $a v e _ { x }$

Step 2: Increase all the decision variables to ;

Step 3: Calculate the remainder $R e m = T o t a l - a v e _ { x } \times N _ { x }$

Step 4: If is less than , stop the process and take the current $X = [ x _ { i j } ]$ as the initial RD; if not, go to Step 5.

Step 5: Select a decision variable $x _ { i j }$ randomly and increase its value by if $x _ { i j } < m _ { i j }$ ;

Step 6: Calculate the new remainder through lowering its value by and go to step 4.

## 5.2. Definition of neighborhood search

The SA is improved through enhancing its neighborhood search with the quantitative significance ${ \cal { S } } = [ { s _ { i j } } ]$ . For instance, the node of RIN represents risk and the quantitative significance of node is related to risk $i \gamma _ { \mathrm { s } }$ influence on the project risk loss. If node ’s quantitative significance, $s _ { i i } .$ , is high, it is logical to avoid the occurrence of risk . So the decision variable $x _ { i i }$ which is the reduced value of the spontaneous probability of risk should be increased preferentially. The same applied to the edge significance. Thus, the quantitative significance is used to calculate the increasing probabilities of the decision variables, denoted by $I P _ { i j }$ , such that

$$
I P _ {i j} = \left(K _ {1} + \frac {S _ {i j}}{\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} S _ {i j}}\right) / (1 + K _ {1}),\tag{19}
$$

where $K _ { 1 }$ is a constant used to avoid the case $I P _ { i j } = 0$ and the corresponding decision variable $x _ { i j }$ has no chance to be selected in the candidate RD.

Next, $I P _ { i j } ^ { \prime }$ , equals to $I P _ { i j } \times r a n d ( 0 , 1 )$ , is used to yield the RD. The decision variable $x _ { i j }$ corresponding to the maximal (minimal) $I P _ { i j } ^ { \prime }$ will be increased (decreased) by the unit probability ( ). If the change of the $x _ { i j }$ value violates the constraint of Eq. (17), a new $x _ { i j }$ will be selected based on the rank of $I P _ { i j } ^ { \prime }$ . For example, if the $x _ { i j }$ with minimum $P _ { i j } ^ { \prime }$ cannot be reduced further $( x _ { i j } = 0 )$ , the algorithm will search for the next best minimum $I P _ { i j } ^ { \prime }$ until the associated $x _ { i j }$ method of searching for the alternative $x _ { i j }$ also holds for the $x _ { i j }$ corresponding to the maximum $I P _ { i j } ^ { \prime }$ . Specifically, if the $x _ { i j }$ corresponding to the maximum $I P _ { i j } ^ { \prime }$ cannot be increased as its current value is equal to $m _ { i j }$ , the algorithm will search for the $x _ { i j }$ associated with the next best maximal $I P _ { i j } ^ { \prime }$ until the value of $x _ { i j }$ is less than $m _ { i j }$ There is another special condition that the value of the $x _ { i j }$ corresponding to the maximum $I P _ { i j } ^ { \prime }$ being equal to and all the other decision variables being zero. In this case, the $x _ { i j }$ corresponding to the maximum $I P _ { i j } ^ { \prime }$ $x _ { i j }$ related to the second maximum $I P _ { i j } ^ { \prime }$ will increase by . As a consequence, the improved SA algorithm is applied to search for the feasible domain of the decision variables more swiftly and effectively, which is denoted by in the pseudocode in Fig. 9. Our pseudocode is an extension of that related to standard SA found in [19]. In Fig. 9, represents the process of calling the RIN simulation model, whose output is the stable value of total risk loss under the specific $X ; S = \left\{ s _ { i j } \right\}$ is the set of quantitative significance of the nodes and edges in the RIN; $I _ { i t e r }$ represents the total number of iterations that the neighborhood search should repeat at a particular temperature; $T _ { 0 }$ and $T _ { f }$ are the initial and final temperature respectively; is the Boltzmann constant used in computing the probability of accepting a worse solution; and is the coefficient of the cooling schedule [19]. The algorithm terminates when either the current temperature is below or equal to $T _ { f }$ , or the best solution is no better for $N _ { n o n - i m p r o v i n g }$ consecutive temperature reductions.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
SA ( $I_{iter}, N_{non-improving}, T_0, T_f, \alpha, K, S$ )

Begin

    Generate an initial solution X by the equal division method;

    $X_{best} = X; F_X = obj(X); F_{best} = F_X;$ $T = T_0; N_1 = 0;$ 

    while ( $T &gt; T_f \&amp; N_1 &lt; N_{non-improving}$ ) {

    $I = 0; N_1 = N_1 + 1;$ 

    while ( $I &lt; I_{iter}$ ) {
    $r_1 = random(0,1);$ 

    if ( $r_1 &gt; 0.5$ ) { Generate a new solution X' from X through the improved neighborhood search method within S;} else { Generate a new solution X' from X through the standard neighborhood search method randomly;} 
    $F_{X'} = obj(X')$ ;

    $\Delta = F_{X'} - F_X$ ;

    if ( $\Delta \leq 0$ ) { $X = X'; F_X = F_{X'}$ }/

    else { 
    $r_2 = random(0,1);$ 

    if ( $r &lt; exp\left(\frac{-\Delta}{K \times T}\right)$ ) { $X = X'; F_X = F_{X'}$ ; }

    if ( $F_X \leq F_{best}$ ) { $X_{best} = X; F_{best} = F_X; N_1 = 0$ }
    $I = I + 1;$ 

    } 
    $T = T \times \alpha;$ 

end
</div>

Fig. 9. Pseudocode of proposed improved SA

## 6. Illustrative example

We now highlight the application of the proposed approach to an actual research project conducted by a Singapore university and a large logistics service provider. This project concerns the application of machine learning in hospital logistics, and aims to reduce the workload of the nurse through delivering the medical items to the patients by robots. The following analysis shows the implementation of the proposed approach, and the effectiveness and efficiency of the improved SA are indicated by its comparison with the standard SA.

The simulation model of the RIN and the improved SA are implemented in MATLAB R2017b on a Windows 10 PC with Intel Core i7 6700 CPU at 3.40 GHz and 16 GB of RAM.

## 6.1. RIN modeling

As to the method of data gathering involving the identification and assessment of the RIN, we followed the studies related to risk identification, risk interaction identification and assessment [2, 21]. Data gathering is conducted by a project member, who is in charge of the project plan and risk management, and familiar with the related methods. Table 1 shows the identified risks. Fig. 10 presents the interaction relationships among the risks.

Table 1: Risks identified for the project

<table><tr><td>Label</td><td>Risk</td><td>Label</td><td>Risk</td></tr><tr><td>R01</td><td>Insufficient communication at the top level</td><td>R13</td><td>Too much non value added work</td></tr><tr><td>R02</td><td>Poor connection to the pre-project</td><td>R14</td><td>Team atmosphere problem</td></tr><tr><td>R03</td><td>Insufficient project needs analysis</td><td>R15</td><td>Cultural conflict</td></tr><tr><td>R04</td><td>Inaccurate project objectives</td><td>R16</td><td>Insufficient internal communication</td></tr><tr><td>R05</td><td>Unclear project implementation path</td><td>R17</td><td>Too much rework</td></tr><tr><td>R06</td><td>Language, terminology problems</td><td>R18</td><td>Insufficient communication between the team and senior management.</td></tr><tr><td>R07</td><td>Insufficient support from the corporate sector</td><td>R19</td><td>Additional requirements</td></tr><tr><td>R08</td><td>Personnel mobility</td><td>R20</td><td>Project scope spread</td></tr><tr><td>R09</td><td>Poor organizational structure of the project team</td><td>R21</td><td>Project time delay</td></tr><tr><td>R10</td><td>Insufficient staff incentives</td><td>R22</td><td>Failed to achieve the expected results</td></tr><tr><td>R11</td><td>Mismatch between project work and researcher study topics</td><td>R23</td><td>Cost overrun</td></tr><tr><td>R12</td><td>Insufficient time of project members</td><td>R24</td><td>Reputation and trust problems</td></tr></table>

![](/api/attachments/W8JCQZ4G/fulltext/images/c68fc5b8293bf43c882c52fd366f02818f6c613c471003c7a9200f204ec9ff21.jpg)  
Fig. 10. Risk interaction network of the project

## 6.2. Social network analysis

The social network analysis is used for calculating the quantitative significance of the nodes and edges in the RIN. A program is written in MATLAB for identifying the paths of each node pair and calculating their power based on Eq. (8). Accordingly, the most powerful path of each node pair is identified and the value of the index $P _ { i j }$ is obtained.

The matrix $\mathcal { M } = [ m _ { i j } ]$ , where $m _ { i i }$ is the spontaneous probability of risk and $m _ { i j }$ is the transition probability from risk to risk , and the risk loss $l _ { i }$ caused by the occurrence of risk are used for calculating the node network power $a _ { i }$ and the weighted one $w a _ { i }$ based on Eq. (9) and (10) respectively. These results are found in Table 2.

Table 2: Node significance calculation

<table><tr><td>Node</td><td> $m_{ii}$ </td><td> $l_i$ </td><td> $a_i$ </td><td> $wa_i$ </td><td>Node</td><td> $m_{ii}$ </td><td> $l_i$ </td><td> $a_i$ </td><td> $wa_i$ </td></tr><tr><td>R01</td><td>0.6</td><td>2</td><td>4.50</td><td>9.65</td><td>R13</td><td>0.3</td><td>0.8</td><td>4.40</td><td>7.63</td></tr><tr><td>R02</td><td>0.6</td><td>0.6</td><td>6.33</td><td>13.59</td><td>R14</td><td>0.5</td><td>4</td><td>2.64</td><td>7.23</td></tr><tr><td>R03</td><td>0.7</td><td>2.8</td><td>6.21</td><td>17.00</td><td>R15</td><td>0.1</td><td>2</td><td>0.73</td><td>0.49</td></tr><tr><td>R04</td><td>0.5</td><td>3.2</td><td>4.17</td><td>8.87</td><td>R16</td><td>0.7</td><td>2</td><td>4.19</td><td>14.02</td></tr><tr><td>R05</td><td>0.2</td><td>3</td><td>6.03</td><td>4.90</td><td>R17</td><td>0.4</td><td>1</td><td>3.25</td><td>8.39</td></tr><tr><td>R06</td><td>0.4</td><td>0.1</td><td>5.81</td><td>7.60</td><td>R18</td><td>0.6</td><td>0.3</td><td>5.46</td><td>12.59</td></tr><tr><td>R07</td><td>0.5</td><td>3</td><td>2.49</td><td>9.37</td><td>R19</td><td>0.6</td><td>1</td><td>3.04</td><td>7.19</td></tr><tr><td>R08</td><td>0.2</td><td>3</td><td>5.86</td><td>4.22</td><td>R20</td><td>0.3</td><td>1.5</td><td>2.41</td><td>3.67</td></tr><tr><td>R09</td><td>0.8</td><td>4</td><td>8.30</td><td>22.53</td><td>R21</td><td>0.6</td><td>3</td><td>2.79</td><td>8.42</td></tr><tr><td>R10</td><td>0.1</td><td>2.4</td><td>5.55</td><td>2.34</td><td>R22</td><td>0.6</td><td>20</td><td>3.91</td><td>18.76</td></tr><tr><td>R11</td><td>0.2</td><td>0.4</td><td>4.80</td><td>4.21</td><td>R23</td><td>0.1</td><td>3</td><td>1.63</td><td>0.95</td></tr><tr><td>R12</td><td>0.2</td><td>0.6</td><td>5.07</td><td>6.15</td><td>R24</td><td>0.2</td><td>6</td><td>4.93</td><td>4.62</td></tr></table>

As for the edge significance, the indices of betweenness $b _ { k }$ and weighted betweenness $w b _ { k }$ are found from Eq. (12) and (14) respectively, as shown in Table 3.

Table 3: Edge significance calculation

<table><tr><td>Start node</td><td>End node</td><td> $b_k$ </td><td> $wb_k$ </td><td>Start node</td><td>End node</td><td> $b_k$ </td><td> $wb_k$ </td><td>Start node</td><td>End node</td><td> $b_k$ </td><td> $wb_k$ </td></tr><tr><td>R01</td><td>R03</td><td>101</td><td>2.04</td><td>R09</td><td>R10</td><td>6</td><td>5.42</td><td>R16</td><td>R17</td><td>13</td><td>1.00</td></tr><tr><td>R01</td><td>R04</td><td>22</td><td>1.89</td><td>R09</td><td>R16</td><td>5</td><td>1.75</td><td>R17</td><td>R21</td><td>1</td><td>0.72</td></tr><tr><td>R01</td><td>R05</td><td>0</td><td>0.00</td><td>R09</td><td>R18</td><td>8</td><td>2.25</td><td>R17</td><td>R22</td><td>17</td><td>5.70</td></tr><tr><td>R01</td><td>R07</td><td>4</td><td>1.93</td><td>R10</td><td>R12</td><td>16</td><td>2.32</td><td>R17</td><td>R23</td><td>0</td><td>0.00</td></tr><tr><td>R01</td><td>R19</td><td>28</td><td>1.14</td><td>R10</td><td>R14</td><td>13</td><td>2.68</td><td>R18</td><td>R01</td><td>50</td><td>4.80</td></tr><tr><td>R02</td><td>R05</td><td>38</td><td>7.39</td><td>R10</td><td>R16</td><td>6</td><td>0.26</td><td>R18</td><td>R07</td><td>8</td><td>6.36</td></tr><tr><td>R03</td><td>R04</td><td>1</td><td>1.57</td><td>R10</td><td>R17</td><td>0</td><td>0.00</td><td>R19</td><td>R20</td><td>23</td><td>5.39</td></tr><tr><td>R03</td><td>R05</td><td>95</td><td>7.70</td><td>R10</td><td>R18</td><td>45</td><td>0.30</td><td>R19</td><td>R23</td><td>0</td><td>0.00</td></tr><tr><td>R04</td><td>R05</td><td>18</td><td>2.88</td><td>R11</td><td>R12</td><td>1</td><td>0.06</td><td>R20</td><td>R21</td><td>35</td><td>1.82</td></tr><tr><td>R05</td><td>R07</td><td>0</td><td>0.00</td><td>R11</td><td>R13</td><td>17</td><td>1.986</td><td>R20</td><td>R22</td><td>2</td><td>1.59</td></tr><tr><td>R05</td><td>R10</td><td>79</td><td>2.45</td><td>R12</td><td>R21</td><td>3</td><td>0.98</td><td>R20</td><td>R23</td><td>23</td><td>3.45</td></tr><tr><td>R05</td><td>R11</td><td>23</td><td>0.05</td><td>R12</td><td>R22</td><td>21</td><td>7.85</td><td>R21</td><td>R24</td><td>47</td><td>4.32</td></tr><tr><td>R05</td><td>R13</td><td>37</td><td>9.11</td><td>R13</td><td>R20</td><td>26</td><td>2.77</td><td>R22</td><td>R24</td><td>144</td><td>11.88</td></tr><tr><td>R05</td><td>R17</td><td>7</td><td>0.86</td><td>R13</td><td>R21</td><td>11</td><td>2.58</td><td>R23</td><td>R24</td><td>18</td><td>0.31</td></tr><tr><td>R06</td><td>R16</td><td>9</td><td>2.55</td><td>R13</td><td>R22</td><td>83</td><td>20.72</td><td>R24</td><td>R01</td><td>110</td><td>0.89</td></tr><tr><td>R06</td><td>R18</td><td>10</td><td>0.56</td><td>R14</td><td>R12</td><td>12</td><td>0.07</td><td>R24</td><td>R07</td><td>21</td><td>3.97</td></tr><tr><td>R07</td><td>R21</td><td>2</td><td>0.79</td><td>R14</td><td>R13</td><td>35</td><td>1.76</td><td>R24</td><td>R14</td><td>23</td><td>0.43</td></tr><tr><td>R07</td><td>R22</td><td>26</td><td>10.67</td><td>R14</td><td>R17</td><td>3</td><td>0.22</td><td>R24</td><td>R16</td><td>34</td><td>1.12</td></tr><tr><td>R08</td><td>R02</td><td>20</td><td>1.10</td><td>R15</td><td>R14</td><td>19</td><td>0.11</td><td>R24</td><td>R20</td><td>16</td><td>1.80</td></tr><tr><td>R08</td><td>R14</td><td>0</td><td>0.00</td><td>R16</td><td>R13</td><td>36</td><td>7.79</td><td></td><td></td><td></td><td></td></tr></table>

From Eq. (15), the quantitative significance $S = [ s _ { i j } ]$ is obtained and will be fed into the program of improved SA algorithm.

## 6.3. Simulation results of the proposed approach

The proposed approach is programmed in MATLAB, including the program of the optimization model within the improved SA and the program of the RLN simulation model. Table 4 shows the values of the related parameters.

Table 4: Parameter values

<table><tr><td>Parameter</td><td>T</td><td> $Q_{warm}$ </td><td>Precision</td><td>Total</td><td> $K_1$ </td><td> $T_0$ </td><td> $T_f$ </td><td>K</td><td> $I_{iter}$ </td><td>α</td></tr><tr><td>Value</td><td>16</td><td>8000</td><td>0.0001</td><td>50 pu</td><td>0.2</td><td>100</td><td>0.01</td><td>5</td><td>2</td><td>0.01</td></tr></table>

The resulting optimal or near optimal project RD with non-zero decision variables is found to be:

$$
x _ {0 1, 0 1} = 0. 2, x _ {0 1, 0 5} = 0. 3, x _ {0 3, 0 3} = 0. 2, x _ {0 5, 0 5} = 0. 2, x _ {0 5, 0 7} = 0. 1, x _ {0 5, 1 1} = 0. 2, x _ {0 8, 0 8} = 0. 2, x _ {0 8, 1 4} =
$$

$$
0. 1, x _ {0 9, 0 9} = 0. 6, x _ {1 0, 1 7} = 0. 1, x _ {1 1, 1 1} = 0. 2, x _ {1 2, 1 2} = 0. 2, x _ {1 3, 1 3} = 0. 3, x _ {1 4, 1 2} = 0. 2, x _ {1 7, 2 3} =
$$

$$
0. 2, x _ {1 8, 1 8} = 0. 6, x _ {2 0, 2 0} = 0. 1, x _ {2 1, 2 1} = 0. 1, x _ {2 2, 2 2} = 0. 6, x _ {2 4, 1 4} = 0. 2, x _ {2 4, 2 4} = 0. 1.
$$

# ACCEPTED MANUSCRIPT

From these results, the optimal RD can be regarded as the optimal combination of the prototypical actions, which indicate the risks and risk interactions that should be dealt with. Accordingly, decision makers can put forward specific risk actions with the consideration of project actual situation and practical experience. Besides, the existing frameworks, principles and cases of controlling risks can better guide decision making [2, 3, 28]. For instance, $x _ { 2 0 , 2 0 }$ is equal to 0.1 in the previous results mentioned above, means that the spontaneous probability of R20 needs to be reduced by 0.1. R20 is “Project scope spread” which is related to the issue of uncertainty in the contract. Meanwhile, technology change is a significant cause of spreading project scope as it leads to the change of research route as well as the project implementation path. Therefore, a specific action to mitigate R20 is put forward based on the principle of increasing the “contractual flexibility” [28], that is, setting modification clause for changing the technology of machine learning model. This modification clause is capable of changing the technology in time as well as within a reasonable range.

The number of decision variables $N _ { x }$ is 83, within which 24 are related to the risks and 59 are pertain to risk interactions. The optimized RD involves only 21 non-zero variables due to the constraint condition related to Eq. (18). Previous studies usually perceived RD as the set of 1 and 0, where 1 means taking a risk response action and results in eliminating the risk or risk interaction absolutely, 0 otherwise [8, 9]. In this study, eliminating the risk or risk interaction absolutely means that the $x _ { i j }$ reaches its maximum of $m _ { i j }$ on the basis of $\operatorname { E q . }$ (17). But as a matter of a fact, only 13 of the 21 variables reach their corresponding maxima. This demonstrates the necessity of setting the decision variables as the decreased value of probability instead of the binary values.

A research, which is of special significance in the study of risk interaction, reports the importance of making RD based on the risk interaction [7]. This previous research compared the action of eliminating the spontaneous probability and the action of eliminating the transition probability. The result shows that the former makes a very little impact on reducing the frequency of risk occurrence; on the contrary, the latter is effective. Nevertheless, the optimized RD in this study mainly focuses on eliminating the spontaneous probability. The reduced spontaneous probability (36 ) is more than the reduced transition probability (14 ). One explanation for this difference is that the precondition varies in these two studies. The conclusion of the previous research is specific to one risk in the RIN while our conclusion is drawn from the perspective of the entire network. In this case, the risks serve as the interface between the RIN and the environment, which can be regarded as a gathering of random factors (see Fig. 1). Only when a risk occurs, the environment affects the RIN and generates the risk loss. Therefore, the optimized RD focuses more on reducing the spontaneous probability to avoid the occurrence of the risks and eventually cuts down the total risk loss fundamentally.

It is noted that there is still 28% of used to reduce the transition probability. This is because that weakening the related interactions destroys the structure of the RIN effectively and ends in a decrease in the total risk loss.

## 6.4. Contrastive analysis of improved SA and standard SA

The improved SA is compared with the standard SA for the purpose of indicating its effectiveness and efficiency. The SA algorithm searches for the optimal RD by the analogy of annealing. For a fixed value of the temperature, an RD is selected using the Monte Carlo process [19]. The evaluation result of the selected RD, i.e. the current optimized value of the total risk loss, is corresponding to a temperature, and its change represents the searching process of the optimal RD, as shown in Fig. 11.

![](/api/attachments/W8JCQZ4G/fulltext/images/bbec16e37c502c737f537368ec4887db324419f15257fd06c3966b3f004d1934.jpg)  
Fig. 11. Optimized value changing process of each SA

In the initial stage of the temperature decreasing, the full line corresponding to the improved SA decreases more quickly than the dot-dash line related to the standard SA. Besides, the temperature of stopping the improved SA is higher than that of standard SA. These phenomena turn out that the improved SA can search for the optimized result more efficiently. Besides, the lower optimized value of improved SA points to its effectiveness.

To validate this observation, these two SAs run 20 times, and the final optimized value of the total risk loss and the temperature of terminating SA are recorded. As the final temperature is usually too small and not intuitive, the times of running RIN simulation model is adopted, which denoted as NR and is equal to $I _ { i t e r } \times l o g _ { \alpha } ( T _ { s } / T _ { 0 } ) . \mathrm { A }$ summary of the contrastive analysis between the two SAs is shown in Table 5.

Table 5: Contrastive analysis between improved SA and standard SA

<table><tr><td rowspan="2"></td><td colspan="2">Optimized value (100$)</td><td colspan="2">NR</td></tr><tr><td>Mean</td><td>s.d.</td><td>Mean</td><td>s.d.</td></tr><tr><td>Improved SA</td><td>1930.3</td><td>29.4943</td><td>1223.7</td><td>71.5932</td></tr><tr><td>Standard SA</td><td>2079.03</td><td>80.4948</td><td>1384.8</td><td>64.0901</td></tr></table>

Percentage gap 7.15% 11.63%

Notes: s.d. is short for standard deviation; Percentage gap = (Mean of standard SA – Mean of improved SA)/Mean of standard SA.

It is evident from Table 5 that the improved SA performs better on the respects of effectiveness and efficiency. However, it is also necessary to judge whether the difference is significant or not in a statistical sense and the significance level is set as 5% by convention.

With respect to the samples of optimized value, we should judge whether the samples obey the normal distribution and have equal variance, which are the foundations of comparing the two samples by parametric test [29]. A two-sided goodness-of-fit test, named Lilliefors test is adopted to judge whether the sample obeys the normal distribution [30], the p-values of two samples are 0.4620 and 0.5000, which means that both of them obey the normal distribution. Furthermore, the Bartlett’s Test is used to judge whether the two samples have equal variance [31], the p-valu $5 . 7 7 8 8 \times 1 0 ^ { - 5 }$ , which indicates that the test rejects the null hypothesis that the variances are equal across the two samples, in favor of the alternative hypothesis that the variances are different. As the basic assumption are not satisfied, so nonparametric test is adapted instead of the parametric test [32]. The Kruskal-Wallis Test is used to compare the two samples and the p-value is $7 . 2 3 6 0 \times 1 0 ^ { - 8 }$ , which indicates the two samples are different from the lens of statistics theory [32]. Therefore, it is reasonable to make the conclusion that the improved SA is better than the standard SA on the respect of effectiveness. By the same token, the NR samples are compared and the final returned p-value is $4 . 0 9 8 2 \times 1 0 ^ { - 7 }$ , which in favor of the conclusion that these two samples are different with respect to the mean. Therefore, the improved SA is more efficiency than the standard one as well.

## 7. Conclusion and perspective

This study has explored an approach for making the risk response decisions in the context of risk interactions. The approach includes a RIN simulation model for evaluating the RDs and an improved SA for optimizing the RDs. Different from the analytical model, the simulation model considers different levels of risk and the corresponding interaction cases. SA has been improved by enhancing its neighborhood search using SNA. In the SNA, two new network indices are put forward to evaluate the significance of the nodes and edges on the respect of causing risk loss.

The analysis of the optimized RD shows that most of the risk eliminating efforts are allocated to reducing the risk spontaneous possibility, which is opposite to the previous study. This is because that the previous study focuses on one risk in the RIN and aim to reduce the occurrence of the risk, whereas, our study faces all the risk in the RIN with the purpose of reducing the total risk loss. Furthermore, the contrastive analysis shows that the improved SA performs better than the standard SA on the respects of effectiveness and efficiency, which highlights the value of considering SNA in improving the existing heuristic method. The proposed approach provides the project manager with a decision support tool to analyze and control a complex RIN, which helps the project manager to allocate the valuable and finite risk control resources more judiciously. Besides, we use SNA to describes the risk interactions with a quantity and profoundly way. The basic thoughts for designing the network indices, i.e. the whole network influence of the node (risk) and the “bridge” function worked by the edge (risk interaction), shifts project manager perspective to a holistic and dynamic view of understanding the importance of a risk in the context of risk interactions. Moving forward, this research can be expanded. (a) Take into account other risk evaluation measures, e.g. the utility of decision makers and the value-at-risk. (b) Consider the time factor “delay”. The process of triggering a risk through a path may happen in one period or take several periods in the project lifecycle. Add the factor “delay” in the RIN simulation model will further improve the approach’s relevance to actual practice. Besides, in the SNA of the RIN, the significance of a path is evaluated based on its power; however, a paths with smaller delay is more important as it can trigger a risk more quickly. (c) Improve the application of SNA in the research of project risk interaction. The proposed approach uses the most powerful paths and the general level of the risk for computing the network indices in SNA. However, the SNA could be enhanced by developing a systematic approach to determine the threshold value for selecting the “less powerful” paths and taking into account all the levels of a risk. (d) Map the risks and stakeholders for the purposes of changing the RD from dealing with the risks to motivating the related stakeholders. This can bring the approach closer to the need of top managers as they are not familiar with the specific project risks but in charge of governing the stakeholders, such as ensuring the sustainability and efficiency of the stakeholders in the contracts [33, 34]. The proposed approach may also be useful to apply to other network optimization problems, such as enhancing the supply-chain/logistics network by increasing the ability of the nodes and edges.

## Acknowledgments

This work was supported by A\*STAR of Singapore (R-385-000-049-305), National Natural Science Foundation of China (71572094), Science Foundation of Shandong Province (ZR2015GM015), and National Research Foundation of South Africa. Furthermore, we would like to thank the editor and anonymous referees who kindly and significantly have improved the paper’s value, quality and readability.

## References

[1] S.M. Seyedhoseini, S. Noori, M.A. Hatefi, An integrated methodology for assessment and selection of the project risk response actions, Risk Analysis, 29 (2009) 752-763.

[2] L. Wang, Network dynamic analysis for project governance risk, Management Science and

[3] E.W. Larson, C.F. Gray, A Guide to the Project Management Body of Knowledge: PMBOK (®) Guide, Project Management Institute, 2015.

[4] C. Fang, F. Marle, M. Xie, Applying importance measures to risk analysis in engineering project using a risk network model, IEEE Systems Journal, 11 (2017) 1548-1556.

[5] A. Taroun, Towards a better modelling and assessment of construction risk: Insights from a literature review, International Journal of Project Management, 32 (2014) 101-115.

[6] C. Fang, F. Marle, M. Xie, E. Zio, An integrated framework for risk response planning under resource constraints in large engineering projects, IEEE Transactions on Engineering Management, 60 (2013) 627- 639.

[7] C. Fang, F. Marle, A simulation-based risk network model for decision support in project risk management, Decision Support Systems, 52 (2012) 635-644.

[8] I. Ben-David, T. Raz, An integrated approach for risk response development in project planning, Journal of the Operational Research Society, 52 (2001) 14-25.

[9] Y. Zhang, Selecting risk response strategies considering project risk interdependence, International Journal of Project Management, 34 (2016) 819-830.

[10] Y. Hu, X. Zhang, E. Ngai, R. Cai, M. Liu, Software project risk analysis using Bayesian networks

[11] Y. Zhang, X. Guan, Selecting project risk preventive and protective strategies based on bow-tie analysis, Journal of Management in Engineering, 34 (2018) 04018009.

[12] Y. Zhang, Z.-P. Fan, An optimization method for selecting project risk response strategies, International Journal of Project Management, 32 (2014) 412-422.

[13] F. Zuo, K. Zhang, Selection of risk response actions with consideration of secondary risks, International Journal of Project Management, 36 (2018) 241-254.

[14] J. Li, M. Li, D. Wu, H. Song, An integrated risk measurement and optimization model for trustworthy software process management, Information Sciences, 191 (2012) 47-60.

[15] I. Heckmann, T. Comes, S. Nickel, A critical review on supply chain risk–Definition, measure and modeling, Omega, 52 (2015) 119-132.

[16] D. Wu, J. Li, T. Xia, C. Bao, Y. Zhao, Q. Dai, A multiobjective optimization method considering process risk correlation for project risk response planning, Information Sciences, 467 (2018) 282-295.

[17] M. Kılıç, G. Ulusoy, F.S. Şerifoğlu, A bi-objective genetic algorithm approach to risk mitigation in project scheduling, International Journal of Production Economics, 112 (2008) 202-216.

[18] S. Kirkpatrick, C.D. Gelatt, M.P. Vecchi, Optimization by simulated annealing, science, 220 (1983) 671-680.

[19] F.Y. Vincent, S.-Y. Lin, A simulated annealing heuristic for the open location-routing problem, Computers & Operations Research, 62 (2015) 184-196.

[20] C. Fang, F. Marle, Dealing with project complexity by matrix-based propagation modelling for project risk analysis, Journal of Engineering Design, 24 (2013) 239-256.

[21] J. Rezaei, Best-worst multi-criteria decision-making method, Omega, 53 (2015) 49-57.

[22] J. Scott, Popularity, Mediation and Exclusion, in: M. Steele (Ed.) Social network analysis, Sage, London, 2017, pp. 95-112.

[23] U. Brandes, S.P. Borgatti, L.C. Freeman, Maintaining the duality of closeness and betweenness centrality, Social Networks, 44 (2016) 153-159.

[24] K. Govindan, H. Soleimani, D. Kannan, Reverse logistics and closed-loop supply chain: A comprehensive review to explore the future, European Journal of Operational Research, 240 (2015) 603- 626.

[25] P.J. Van Laarhoven, E.H. Aarts, Simulated annealing, Simulated Annealing: Theory and Applications, Springer1987, pp. 7-15.

[26] S. Bahrami, F.D. Ardejani, E. Baafi, Application of artificial neural network coupled with genetic algorithm and simulated annealing to solve groundwater inflow problem to an advancing open pit mine, Journal of Hydrology, 536 (2016) 471-484.

[27] J. Li, X. Sun, F. Wang, D. Wu, Risk integration and optimization of oil-importing maritime system: a

[28] C.O. Cruz, R.C. Marques, Flexible contracts to cope with uncertainty in public–private partnerships, International Journal of Project Management, 31 (2013) 473-483.

[29] W.M. Mendenhall, T.L. Sincich, N.S. Boudreau, Statistics for Engineering and the Sciences, Sixth ed., Chapman and Hall/CRC, Boca Raton, 2016, pp. 157-184.

[30] N. Balakrishnan, Continuous multivariate distributions, Wiley StatsRef: Statistics Reference Online, DOI (2014).

[31] G.V. Glass, Testing homogeneity of variances, American Educational Research Journal, 3 (1966) 187-190.

[32] X.-B. Ma, F.-C. Lin, Y. Zhao, An adjustment to the Bartlett's test for small sample size, Communications in Statistics-Simulation and Computation, 44 (2015) 257-269.

[33] D.C. Ferreira, R.C. Marques, Do quality and access to hospital services impact on their technical efficiency?, Omega, DOI (2018).

[34] D.C. Ferreira, R.C. Marques, A. Nunes, Economies of scope in the health sector: The case of Portuguese hospitals, European Journal of Operational Research, 266 (2018) 716-735.

Lei Wang is currently with The Logistics Institute – Asia Pacific, National University of Singapore, Singapore as a Research Fellow. His current research interests include network analysis, complex system modeling and simulation, project management and governance. He has been involved in eight academic and seven enterprise research projects and provided decision suggestions to government and enterprises. Dr. Wang holds a BS degree in Industry Engineering and a P degree in Management Science and Engineering from Shandong University, People’s Republic of China.

Mark Goh holds the appointments of Director (Industry Research) at the Logistics Institute-Asia Pacific in National University of Singapore. Prof. Mark also used to be Director of Supply Chain Solutions for Asia/Middle East. He is also a Professor of Management at the University of South Australia. He has published over 300 technical papers in internationally refereed journals and conferences, some of his recent articles on risk management and supply chain management in the Industrial Marketing Management, Production and Operations Management, Industrial Organizations, Transportation Research Parts A & E, MIS Quarterly Executive, Information Sciences.

Ronggui Ding is the dean of Department of Management Science and Engineering, and Director of Project Management Institute, Shandong University China. Prof. Ding is the committeeman in the final stage of Global Project Excellence Award from International Project Management Association, the member of the Global Degree Certification Committee in Project Management Institute and chief specialist of Project Management Review. His research interests involve project management and governance, artificial intelligence. He has published more than 100 papers including International Journal of Project Management, Journal of Construction Engineering and Management, Industry Engineering and Management. Besides, his Chinese professional book was translated into English, which is one the bestsellers of Springer books.

Leon Pretorius is currently Professor in the Graduate School of Technology Management at the University of Pretoria. He has concurrently been active as a specialist consultant and researcher in engineering industry since 1980. He has also published more than 260 technical conference papers and peer-reviewed journal articles as author and co-author in his fields of expertise. He serves on the editorial boards of a number of international journals. He is currently the Chairman of the Board of IAMOT. He is an Honorary Fellow of SAIMechE, Member of SAIIE, Member of ASME and Member of IEEE. He is rated as a researcher by the National Research Foundation (NRF) in South Africa.
