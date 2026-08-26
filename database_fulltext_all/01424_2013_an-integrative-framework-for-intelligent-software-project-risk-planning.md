---
otero_id: 1424
otero_key: "6ME2D4R2"
title: "An integrative framework for intelligent software project risk planning"
authors: "Yong Hu; Jianfeng Du; Xiangzhou Zhang; Xiaoling Hao; E.W.T. Ngai; Ming Fan; Mei Liu"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.029"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An integrative framework for intelligent software project risk planning

Yong Hu <sup>a,</sup>⁎, Jianfeng Du <sup>a</sup>, Xiangzhou Zhang <sup>b</sup>, Xiaoling Hao <sup>c</sup>, E.W.T. Ngai <sup>d</sup>, Ming Fan <sup>e</sup>, Mei Liu <sup>f</sup>

<sup>a</sup> Institute of Business Intelligence and Knowledge Discovery, Guangdong University of Foreign Studies, Sun Yat-sen University, Guangzhou 510006, PR China

<sup>b</sup> School of Business, Sun Yat-sen University, Guangzhou 510006, PR China

<sup>c</sup> Shanghai University of Finance and Economics, Shanghai 200433, PR China

<sup>d</sup> Department of Management and Marketing, The Hong Kong Polytechnic University, Kowloon, Hong Kong, China

<sup>e</sup> Foster School of Business, University of Washington, Seattle, WA 353226, USA

<sup>f</sup> Department of Computer Science, New Jersey Institute of Technology, Newark, NJ 07102, USA

## a r t i c l e i n f o

Available online xxxx

Keywords: Decision support systems Software project risk analysis and planning Actionable knowledge discovery Social media platform project

## a b s t r a c t

Software projects have inherent uncertainties and risks. Social software projects suffer even more requirement changes and require more attention to risk management. Risk analysis and planning are complex, making it dif<sup>fi</sup>- cult to manage risks effectively through subjective judgment. At present, ample empirical research on intelligent decision-support models for risk analysis in software projects exists. However, to the best of our knowledge, empirical models for software project risk planning, or those related to integrative software risk analysis and planning are not available. Thus, the current study proposes an integrative framework for intelligent software project risk planning (IF-ISPRP) to help in minimizing the impacts of project risks and achieving a better foreseeable project outcome. IF-ISPRP includes two core components, namely, risk analysis module and risk planning module. The risk analysis module is to predict whether a project will be successful or not. The risk planning module is to produce a cost-minimal action set for risk control based on the risk analysis module. For integrative risk analysis and planning, we propose a novel many-to-many actionable knowledge discovery (MMAKD) method for complex risk planning. We also apply the framework on a social media platform project, Guangzhou Wireless City, and demonstrate how the model can generate a cost-minimal action set to mitigate the project risk. The risk-control actions found may help develop strategies on mitigating the risks of other social software projects. We hope that the proposed framework will provide an intelligent decision-support tool for project stakeholders to effectively control project risks by integrating risk analysis and planning.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Software projects have inherent uncertainties and risks [32]. Moreover, software development has a high failure rate. The Standish Group [46], in their report “CHAOS Summary 2009,” showed that the success rate of global software projects is only approximately 32%. Software development is subject to a variety of risks, which are generally de<sup>fi</sup>ned as a set of factors or conditions that seriously threatens the successful completion of a software project [48]. The necessity of identifying and tackling these risks has spurred signi<sup>fi</sup>cant interest among academic researchers and practitioners [6]. A research by the Microsoft corporation indicated that putting 5% work into effective risk management could produce a 50%–75% opportunity to complete project before the deadline [36]. It helps to prevent catastrophes such as redo and overkill of a software project.

“Social software” has been used to denote Internet software that enables people to communicate and collaborate, such as e-mail, IM, group forums, blogs, and SNS [11]. The designers and developers of social software are faced by a major challenge — how to facilitate social interaction and engagement among the users [22]. Although social software projects share common risks with general software projects, they also have their own distinct and unique risk source because people use social software for a variety of purposes [22]. Moreover, as a common characteristic of social software, the continuous and fast requirement changes, in terms of user interface design and interaction functions, make it more imperative to conduct risk management.

Risk analysis and planning are two of the most important processes in software project risk management (SPRM). Risk analysis involves exploring the relationships between risk factors and project outcome [1,43], which is critical for effective risk control. Substantial research on risk analysis models based on intelligent technologies is available such as [27,30,31,37,49]. Note that this paper does not aim to discuss the topics of software reliability, safety, cost/effort, etc., such as those mentioned in [7]. Risk planning involves developing an effective plan to address the most critical risks and optimizing the allocation of project resources [1,43]. While risk planning is generally acknowledged as critical to risk management, few studies have been put forward and there is no widely accepted tool or model to support it [6].

At the U.S. National Aeronautics and Space Administration (NASA), risk planning requires not only “developing effective plans” but also planning “only as much as needed” [43]. Boehm [9] believes that risk planning should not only “plan for each risk item” but also be able to “integrate the risk-management plans for each risk item with each other and with the overall project plan.” Therefore, in order to optimize resource allocation while maximizing the project outcome, it is imperative to consider the combined impact of the risk factors on the project outcome as well as the total execution cost of the selected risk-control actions. Due to the tremendous computational effort, intelligent decisionsupport models/tools are preferred over subjective expert judgment in achieving effective and economical decision making during risk analysis and planning. Studies that adopt integer-programming technology for risk planning, such as those of Ben-David and Raz [6] and Pan and Chen [40], aim to eliminate all kinds of risks. However, in a resourcerestricted situation, such objective is not practical because of the high cost of controlling all the risks. Moreover, controlling all risks is often not necessary as only a few risks can directly affect the project outcome. Furthermore, the risk of continuous requirement changes cannot be avoided in a social software project. These studies cannot identify the key risks because they have not taken advantage of the relationships between risk factors and project outcome, which are characterized by an intelligent risk analysis model.

To overcome the above limitations, the present study proposes an empirical and intelligent framework that can provide an integrative risk analysis and planning in SPRM. We <sup>fi</sup>rst introduce the components and application steps of the framework. Given a speci<sup>fi</sup>c project, the project outcome is predicted and then, based on the prediction mechanism and planning context, a cost-minimal risk-control plan is determined. Random forest [12] is adopted to establish a risk analysis model while a many-to-many actionable knowledge discovery (MMAKD) method is proposed to accomplish risk planning. Finally we implement the proposed framework and present a real case study of social media platform project to demonstrate the application of the proposed framework.

The study has two speci<sup>fi</sup>c contributions. First, the proposed framework for integrative risk analysis and planning is the <sup>fi</sup>rst in the <sup>fi</sup>eld of SPRM. Second, the proposed risk-planning method considers many-to-many relationships between risk factors and risk-control actions, which adequately meet the requirements of risk analysis and planning in practice. A many-to-many relationship implies that a risk factor can be in<sup>fl</sup>uenced by several risk-control actions, and vice versa a risk-control action can in<sup>fl</sup>uence several risk factors. In the case study, the social media platform project (Guangzhou Wireless City) demonstrates how the model generates a cost-minimal action set to mitigate the whole project risk.

## 2. Literature review

## 2.1. Software project risk management

Risk management was introduced into software project management by Boehm [8] and Charette [16]. SPRM is a series of rules or practices, which can identify, analyze, and monitor the risk factors as well as increase the success rate of the project [3]. SPRM could positively in<sup>fl</sup>uence budget, schedule, scope of the project, etc. [28]. In general, SPRM comprises two stages [8,16,25]:

1) First stage is risk assessment which involves risk identi<sup>fi</sup>cation, risk analysis, and risk prioritization. Risk identi<sup>fi</sup>cation requires systematic identification and classification of the risk factors. Risk analysis assesses the state of each identi<sup>fi</sup>ed risk factor, and analyzes the relationships among risk factors, and between risk factors and project outcome. Risk prioritization decides the priority sequence in controlling each risk factor.

2) Second stage is risk control which involves risk planning and risk monitoring. Risk planning involves not only planning for each risk factor, but also coordinating the individual plans with each other. Continuous monitoring of the states of risk factors, examination of the effectiveness of the risk-control plan, and the prompt discovery of impending risks are required during and after the implementation of the plan.

## 2.2. Software project risk analysis and planning

Recently, a signi<sup>fi</sup>cant number of related studies on risk analysis and planning in the <sup>fi</sup>eld of SPRM have become available. This paper focuses on historical-data-based risk analysis, speci<sup>fi</sup>cally on predicting the probability of success for software development projects; thus we exclude studies that are based on subjective analysis or expert judgment, which are methods often used in project risk management [19]. We also exclude studies that analyze software reliability, cost, safety, etc. The representative literature is summarized in Table 1. To the best of our knowledge, there is no speci<sup>fi</sup>c study on the topic of intelligent risk management for social software project.

Risk analysis is more widely studied and the modeling methods mainly include the use of statistical analysis and data mining.

1) Research based on statistical methods. For example, Wallace et al. [48] used structural equation modeling (SEM) to develop an exploratory model for testing and estimating the relations between software project risks and project performance. Drew Procaccino et al. [17] assessed several early risk factors and their effects on software project success using regression analysis. Their research found that the presence of a committed sponsor and the level of con<sup>fi</sup>dence that the customers and users have in the project manager and the development team are the most important factors for project success. Jiang and Klein [27] presented a model using principal component analysis (PCA) based on a survey of 86 project managers, exploring the relationships between IS success measures and risk factors. In conclusion, these studies aim to discover the universal knowledge about risks (i.e. the correlation or causality between risk factors and project outcome) rather than predict the overall risk level of an ongoing project.

2) Research based on data mining methods. For example, Aguilar-Ruiz et al. [2] proposed an approach using a software project simulator and evolutionary computation. Their model predicts whether a project can be kept within the cost, quality and duration targets. Zhang et al. [55] built an early warning system to predict project escalation. They found that neural network is preferable to logistic regression model in prediction, as it can capture the non-linear relationships between risk factors and project outcome. However, the network is a “black box”, and thus cannot provide explicit decision-making knowledge to managers. Fan and Yu [21] presented a risk analysis model using Bayesian networks. Lauría and Duchessi [31] demonstrated a methodology for building a Bayesian network for information technology (IT) implementation from survey data and used it to predict the attainment of IT bene<sup>fi</sup>ts. Moreno García et al. [37] used association rules technology to evaluate the impact of certain project management policies on software project quality, duration, and development effort. In conclusion, the models based on data mining methods can analyze and predict dynamic risk level of ongoing projects.

On the other hand, there are relative few studies on risk planning. They can be divided into two types.

1) Studies that adopt statistical methods to verify the effectiveness of risk-control actions. For example, Benaroch et al. [5] used logistical regression analysis to verify the validity of the risk-option mappings of an IT investment option-based risk management (OBRiM) framework. Li et al. [32] adopted Pearson's correlation to analyze the relationship between risk-reduction activities and risk factors. Jiang et al. [29] found that user partnering is signi<sup>fi</sup>cantly relevant to higher user support, less residual risk, and better project performance. Na et al. [38] proved the presence of a strong negative relationship between standardization and residual performance risk. Li et al. [32] validated and compared the effects of <sup>fi</sup>ve risk-reduction activities on risk factors based on 133 software projects. Wang et al. [50] collected data from 212 project managers from the Project Management Institute (PMI) and veri<sup>fi</sup>ed that the level of control activities during the system development process has a signi<sup>fi</sup>cant effect on software <sup>fl</sup>exibility. In conclusion, statistical methods are often applied to study the validity of risk-control actions on risk factors.

Table 1  
Empirical studies on software project risk analysis and planning models (1996 to 2011).

<table><tr><td>Phase</td><td>Classification</td><td>Technologies</td><td>Representative studies</td><td>Comment</td></tr><tr><td rowspan="4">Analysis</td><td>Statistical analysis</td><td>SEM; CFA; EFA; PCA; ANOVA; regression</td><td>[23,47,48,50,54]</td><td rowspan="4">Statistical analysis is used to explore the common knowledge about the relationship between risk factors and project outcome Data mining is used to perform intelligent and dynamic analysis of risk. Prediction and classification are used for early assessment of project outcome. Cluster analysis is used for identifying the risk across levels of project outcome. Association analysis is used for finding out the association between risk and project outcome.</td></tr><tr><td>Prediction and classification</td><td>BBN; DT; ANN; EA; GA; logistic regression; fuzzy aggregation</td><td>[2,14,18,21,31,34,39,42,55]</td></tr><tr><td>Cluster analysis</td><td>Clustering; visualization</td><td>[24,41,49]</td></tr><tr><td>Association analysis</td><td>Association rules</td><td>[37]</td></tr><tr><td rowspan="2">Planning</td><td>Statistical analysis</td><td>SEM; CFA; PCA; ANOVA; regression; Pearson&#x27;s correlation</td><td>[5,29,32,38,50]</td><td>Verify the effectiveness of risk control actions on risk factors</td></tr><tr><td>Operation optimization</td><td>Integer programming</td><td>[6,40,51]</td><td>Generate optimized risk control action set</td></tr></table>

2) Studies that aim to produce the optimal risk-control action set using integer programming technology. For example, Ben-David and Raz [6] built a risk-response model, which can represent the overlapping effects of multiple risk reduction actions and the impacts of secondary risk events. This risk-response model can also evaluate the total risk exposure under various combinations of risk reduction actions. The model applies integer-programming technology to generate the most cost-effective combination of risk reduction actions. Pan and Chen [40] presented an economic optimization model for selecting risk reduction actions in the risk response planning phase of CMMI-based SPRM. Their model considers the logical constraints (exclusion and implication) that limit the combination of reduction actions, and can be solved using integer-programming technology. Based on a real option analysis framework, Wu et al. [51] applied multistage stochastic integer programming to address complex decisionmaking problems in ERP project investment.

## 3. Integrative framework for intelligent software project risk planning

To achieve an integrative risk management that can provide decision support from risk analysis to planning, we propose an integrative framework for intelligent software project risk planning (IF-ISPRP). As shown in Fig. 1, our framework is composed of three key components: (1) Project Risk Database, (2) Risk Analysis Module, and (3) Risk Planning Module.

## 3.1. Key components of the proposed framework

Project Risk Database is a collection of risk factors and <sup>fi</sup>nal outcomes of real software projects. It provides project samples for the risk analysis module. The sample size and quality signi<sup>fi</sup>cantly in<sup>fl</sup>uence the validity and reliability of the risk analysis module and subsequently, of the risk planning module.

Risk Analysis Module takes a risk analysis model as its core to analyze and predict the project risks. The model takes the states of risk factors as input and returns the predicted project outcomes (i.e. success or failure) as output.

Risk Planning Module takes the risk-control actions list, the manyto-many relationship between actions and risk factors, and the execution cost of actions as input. It outputs a cost-minimal risk-control action set that can help in achieving that the prediction of the project outcome is success. The module proceeds through a generate-andtest-based process as follows.

1) A new candidate action set is generated according to the list of risk-control actions, the execution costs of the actions, and the many-to-many relationship between risk-control actions and risk factors.

2) The effect of the candidate action set on the states of risk factors is calculated. Given the new states, the risk analysis module predicts the project outcome. If success is predicted, the total execution cost of the candidate action set is compared with that of the current optimal set. The less costly one is selected as the new optimal set.

3) If having traveled the entire search space, the module outputs the current optimal set, which is a cost-minimal action set. Otherwise, it proceeds to the <sup>fi</sup>rst step.

## 3.2. Steps of applying the proposed framework

As shown in Fig. 2, IF-ISPRP application comprises <sup>fi</sup>ve steps. The <sup>fi</sup>rst three steps focus on building a reusable tool/model for integrative risk analysis and planning whereas the last two steps are to apply the tool to an ongoing software project.

## Step 1 Data collection

First, the risk factors that will be used in the risk analysis module are identi<sup>fi</sup>ed. Second, project samples are collected according to the list of risk factors to construct the project risk database. Collecting high-quality software project samples is a long-term and expensive process.

## Step 2 Risk analysis module construction

First, a proper modeling method for risk analysis is chosen by considering the characteristics of the collected project samples and the interpretability of the objective model. Second, a risk analysis model is constructed based on the training data provided by the project risk database.

## Step 3 Risk planning module construction

First, the many-to-many relationship model between riskcontrol actions and risk factors is established. The model is to restrict the scope of the risk planning problem covered in the present study. Second, the proposed MMAKD

Y. Hu et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/6ME2D4R2/fulltext/images/5a70992cc7394ce8a3d3766206b0befce6f1b35441106e4801efec01353da266.jpg)  
Fig. 1. Integrative framework for software project risk intelligent planning.

method is implemented to solve the risk planning problem (details of both the model and the method are presented in Section 4).

## Step 4 Risk analysis

First, the current states of the risk factors of the project are assessed. Second, the risk analysis module is used to predict the project outcome. If the predicted outcome is a failure, the subsequent risk planning is pursued. The procedures of risk analysis should be periodically performed.

## Step 5 Risk planning

First, the parameters of risk planning, including a list of candidate risk-control actions, the many-to-many relationship between

![](/api/attachments/6ME2D4R2/fulltext/images/7b2173e950341305ddad0e73d2e6f286930b45c545eb728c24bdce605c3a1c32.jpg)  
Fig. 2. Application steps of IF-ISPRP.

Please cite this article as: Y. Hu, et al., An integrative framework for intelligent software project risk planning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.12.029

actions and risk factors, and the execution costs of actions are assessed. Second, taking the above parameters as input, the risk planning module outputs the cost-minimal action set. Third, the project stakeholders evaluate the generated action set and modify it according to real-life situations. Consequently, the risk resolution process is initiated to implement the produced plan.

## 4. Many-to-many actionable knowledge discovery

## 4.1. Problem setting: formulation of the risk planning problem

Some notations are <sup>fi</sup>rst de<sup>fi</sup>ned as follows.

$\{ F _ { 1 } , . . . , F _ { n } \} - \mathfrak { a }$ set of features (feature refers to risk factors in the present study);

$\{ A _ { 1 } , . . . , A _ { m } \} - \mathsf { a }$ set of actions;

$< \nu _ { 1 } , . . . , \nu _ { n } > - \textrm { a }$ state of the given instance, where $\nu _ { i }$ is the value of feature $F _ { i } ;$

$\left\{ \nu _ { i , 1 } , . . . , \nu _ { i , n _ { i } } \right\} - \mathsf { a }$ set of all possible values of feature $F _ { i } \left( \nu _ { i , 1 } { < \dots < } \nu _ { i , n _ { i } } \right)$ $< c _ { 1 } , . . . , c _ { m } > - \ : a$ vector of nonnegative execution costs, where $c _ { i }$ denotes the execution cost of action $A _ { i } ,$ particularly $c _ { i } = 0$ denoting no execution.

$f _ { i , j } ( c _ { j } , \nu _ { i } ) \ : - \ : a$ functions that returns the new value of feature $F _ { i }$ obtained from the value $\nu _ { i }$ by solely applying action $A _ { j }$ with an execution cost c ;

$f _ { i } \left( \vec { C } , \dot { \nu _ { i , n _ { i } } } \right) \mathrm { ~ - ~ } \mathsf { a }$ function that returns a new value of feature $F _ { i }$ obtained by applying actions at costs that represented by ${ \vec { C } } = { \dot { } }$ $< c _ { 1 } , . . . , c _ { m } > \left( 1 \leq i \leq n \right)$

Therefore, the risk planning problem can be stated as: given a classi<sup>fi</sup>er and an instance whose original state is represented by $\left. \nu _ { 1 , s _ { 1 } } , . . . , \nu _ { n , s _ { n } } \right.$ , where $1 \leq s _ { i } \leq n _ { i } ,$ , and which is classi<sup>fi</sup>ed to an inferior class, we intend to compute the cost-minimal action set, ${ \vec { C } } = < c _ { 1 } , . . . , c _ { m } >$ , such that $\sum _ { i = 1 } ^ { m } c _ { i }$ is minimized among all vectors,

$\vec { C } = < c _ { 1 } ^ { ' } , . . . , c _ { m } ^ { ' } >$ , and such that the given instance with a new state represented by $\left. f _ { 1 } \left( \overrightarrow { C } ^ { \prime } , \nu _ { 1 , s _ { 1 } } \right) , . . . , f _ { n } \left( \overrightarrow { C } ^ { \prime } , \nu _ { n , s _ { n } } \right) \right.$ is classified to the preferred output class $o _ { p } .$

## 4.2. Problem setting: the many-to-many relationship model

Most existing studies on actionable knowledge discovery [33,52,53] only deal with the one-to-one relationship between actions and factors. In the present study, we consider a more general and reasonable case, i.e., the many-to-many relationship — an action can simultaneously affect several features, and vice versa, a feature can be simultaneously affected by several actions. Besides, three reasonable assumptions are introduced to lower the complexity of the risk planning problem:

Assumption 1. Actions are applied synchronously; the dependencies and execution orders among actions are not considered.

Assumption 2. The compound effect of a set of actions is equal to the maximum effect of an individual action. Thus, we have

$$
f _ {i} \left(<   c _ {1}, \dots , c _ {m} >, v _ {i}\right) = \max _ {1 \leq j \leq m} f _ {i, j} \left(c _ {j}, v _ {i}\right) \quad \text { for   all } 1 \leq i \leq n.\tag{1}
$$

For example, let $A _ { 1 }$ and $A _ { 2 }$ be two actions that will change the value of factor F from high (risk level) to mid and to low respectively. When both $A _ { 1 }$ and $A _ { 2 }$ are applied, the value of F would be changed from high to low (noting that, we use larger numeric value for lower risk level).

Assumption 3. The effect of an action is de<sup>fi</sup>ned using a monotonically increasing step function on the execution cost of the action.

Hence, for any action $A _ { j }$ and any value $\nu _ { i , k }$ of $F _ { i }$ where $1 \leq \mathbf { k } \leq n _ { i } ,$ there exists an increasing sequence of positive thresholds $\delta _ { i , j , \nu _ { i , k } , \nu _ { i , k + 1 } } , . . . , \delta _ { i , j , \nu _ { i , k } , \nu _ { i , n _ { i } } }$ such that

$$
f _ {i, j} \Big (c _ {j}, v _ {i, k} \Big) = \left\{ \begin{array}{l l} v _ {i, k} & \text { if } 0 \leq c _ {j} <   \delta_ {i, j, v _ {i, k}, v _ {i, k + 1}} \\ v _ {i, k + 1} & \text { if } \delta_ {i, j, v _ {i, k}, v _ {i, k + 1}} \leq c _ {j} <   \delta_ {i, j, v _ {i, k}, v _ {i, k + 2}} \\ ... \\ v _ {i, n _ {i}} & \text { if } c _ {j} \geq \delta_ {i, j, v _ {i, k}, v _ {i, n _ {i}}} \end{array} \right..\tag{2}
$$

For example, suppose the cost threshold for changing a risk factor $F$ from high to mid by action $A _ { 1 }$ is \$2, then $A _ { 1 }$ cannot change the value of F from high to low with a cost less than \$2 and, with a cost more than \$2, $A _ { 1 }$ will do no worse than change the value of F from high to mid.

## 4.3. Problem solving: a MMAKD method based on random forest

The above risk planning problem is a search problem and can be solved through a traditional method which is based on the exhaustive generate-and-test framework. In this method, all possible vectors of execution costs are generated and only the cost-minimal one that can make the given instance to be classi<sup>fi</sup>ed to the preferred output class is chosen. However, the method is relatively inef<sup>fi</sup>cient when the search space is large and the classi<sup>fi</sup>er is complex, because the given classi<sup>fi</sup>er is applied as a black box and the classi<sup>fi</sup>cation process cannot be anatomized to heuristically prune the huge search space. To improve the ef<sup>fi</sup>ciency, we consider encoding the above problem as a propositional satisfiability (SAT) problem so that modern powerful SAT techniques can be used to direct the search and prune the search space. Therefore, we develop a novel method, called the MMAKD method, to extract a cost-minimal action set from random forest [12]. The key idea is to reduce the original problem into an extended SAT problem, called linear PBO problem [35], de<sup>fi</sup>ned as follows:

minimize $\sum _ { j = 1 } ^ { n } c _ { j } x _ { j }$

$$
\begin{array}{l} \text { subject   to } \sum_ {j = 1} ^ {n} a _ {i j} x _ {j} \geq b _ {i} \\ x _ {j} \in \{0, 1 \}, a _ {i j}, b _ {i} \in Z, i \in \{1,..., m \}, \end{array}
$$

where $c _ { j }$ is a nonnegative integer associated with the variable $x _ { j } ,$ and $a _ { 1 j } , . . . , a _ { m j }$ are integer coefficients of $x _ { j }$ in the set of m pseudo-Boolean constraints. A 0-1 truth assignment Φ on $\{ x _ { 1 } , . . . , x _ { n } \}$ is referred to as a solution to the above linear PBO problem $\mathrm { i f } \sum _ { j = 1 } ^ { n } c _ { j } \phi \Bigl ( x _ { j } \Bigr )$ is minimized

$$
\phi^ {'}
$$

$$
\sum_ {j = 1} ^ {n} a _ {i j} \Phi^ {\prime} (x _ {j}) \geq b _ {i}
$$

for all $1 \leq i \leq m .$ . A linear PBO problem can be solved by ef<sup>fi</sup>cient pseudo-Boolean solvers, such as MiniSAT<sup>+</sup> [20], GALENA [15], and PUEBLO [45].

The proposed MMAKD method uses a random forest as the classi<sup>fi</sup>er, i.e., the project outcome predictor. Random forest [12] is an ensemble classi<sup>fi</sup>er, which takes decision trees as base classi<sup>fi</sup>ers. A decision tree is an analytical decision support tool that uses a tree-like graph to solve classi<sup>fi</sup>cation problems. Random forest uses a majority voting mechanism for aggregating individual outcomes of decision trees. A random forest can be easily encoded as a set of (classi<sup>fi</sup>cation) rules. The reasons why rule representation is adopted would spontaneously show up later. The method is outlined as follows.

Initially, a set of variables is introduced in the target linear PBO problem. Variables of the form $x _ { j , c }$ are introduced to denote whether action $A _ { j }$ is applied with an execution cost c. The variable $x _ { j , c }$ is introduced only when applying action $\mathsf { A } _ { j }$ with an execution cost c that is suf<sup>fi</sup>cient to change the original value $\nu _ { i , s _ { i } }$ of $F _ { i }$ to a larger value. For every action $A _ { j } ,$ a variable $x _ { j , 0 }$ is also introduced to denote whether action $A _ { j }$ is not applied. Variables of the form $y _ { i , \nu _ { i , k } }$ are introduced to denote whether the value of $F _ { i }$ is changed to $\nu _ { i , k }$ by applying all actions. Variables of the form $z _ { i , j , \nu _ { i , k } }$ are introduced to denote whether the value of F is changed to $\nu _ { i , k }$ by applying action $A _ { j } .$ The variable $y _ { i , \nu _ { i , k } } ~ ( \mathrm { r e s p . } z _ { i , j , \nu _ { i , k } } )$ is introduced only when $\nu _ { i , k } { \ge } \nu _ { i , s _ { i } }$ because we assume that the value of any feature cannot be decreased by applying actions. Moreover, variables of the form $w _ { i , o _ { j } }$ are introduced to denote whether the ith decision tree assembled in the random forest can classify the given instance with the new state to the class $o _ { j } .$ The variable $w _ { i , o _ { j } }$ is introduced for every decision tree and every possible output class of the given random forest.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
2. Add a rule $x_{j,c_1} \vee x_{j,c_2} \vee \cdots \vee x_{j,c_k}$ to $\Pi$, where $x_{j,c_1}, \cdots, x_{j,c_k}$ are all variables in $X$ of the form $x_{j,c}$;
3. For any two different variables $x_{j,c_1}$ and $x_{j,c_2}$ in $X$, add a rule $x_{j,c_1} \wedge x_{j,c_2} \to \bot$ to $\Pi$;
Sub-procedure EncodeFeatureConstraints
1. For all $1 \leq i \leq n$ do
2. Add a rule $y_{i,v_{i,s_i}} \vee y_{i,v_{i,s_{i+1}}} \vee \cdots \vee y_{i,v_{i,n_i}}$ to $\Pi$;
3. For any two integers $j$ and $k$ such that $s_i \leq j &lt; k \leq n_i$, add a rule $y_{i,v_{i,j}} \wedge y_{i,v_{i,k}} \to \bot$ to $\Pi$;
4. For all $s_i \leq k \leq n_i$, add two rules $z_{i,1,v_{i,k}} \vee z_{i,2,v_{i,k}} \vee \cdots \vee z_{i,m,v_{i,k}} \to y_{i,v_{i,k}} \vee y_{i,v_{i,k+1}} \vee \cdots \vee y_{i,v_{i,n_i}}$ and $y_{i,v_{i,k}} \to z_{i,1,v_{i,k}} \vee z_{i,2,v_{i,k}} \vee \cdots \vee z_{i,m,v_{i,k}}$ to $\Pi$;
5. For all $1 \leq j \leq m$ and $s_i \leq k \leq n_i$, if $\delta_{i,j,v_{i,s_i},v_{i,k}} = +\infty$ then add a rule $z_{i,j,v_{i,k}} \to \bot$ to $\Pi$, else add a rule $x_{j,c_1} \vee x_{j,c_2} \vee \cdots \vee x_{j,c_l} \leftrightarrow z_{i,j,v_{i,k}}$ to $\Pi$, where $x_{j,c_1},\cdots,x_{j,c_l}$ are all variables in $X$ of the form $x_{j,c}$ such that $\delta_{i,j,v_{i,s_i},v_{i,k}} \leq c &lt; \delta_{i,j,v_{i,s_i},v_{i,k+1}}$ (for briefness, we define $\delta_{i,j,v_{i,s_i},v_{i,s_i}} = 0$ and $\delta_{i,j,v_{i,s_i},v_{i,n_i+1}} = +\infty$);
Sub-procedure EncodeDecisionTrees
</div>

Subsequently, all pseudo-Boolean constraints in the target linear PBO problem are generated using the sub-procedures shown in Fig. 3. For convenience, standard rule form is adopted to represent the constraints, using symbols including contradiction ⊥, conjunction $\wedge ,$ implication → and equivalence ↔. Let Π denote the set of these pseudo-Boolean constraints that can be represented as rules.

2) The second subset consists of rules that encode action–feature interaction constraints and is appended to Π in the sub-procedure “EncodeFeatureConstraints.” The rules added in line 2 specify that for every feature, the original value should be changed to some larger value or remain unchanged after all actions are applied. The rules added in line 3 stipulate that the original value cannot be changed to two different values. The rules added in line 4 specify that the new value obtained by applying all actions is equal to the maximum value obtained by applying individual actions. These rules encode the assumption given in Formula (1). The rules added in line 5 state that for every feature, a new value can be obtained by applying a single action only when the corresponding threshold is <sup>fi</sup>nite, and the new value can only be obtained when the execution cost is not less than the corresponding threshold but is less than the next threshold. These rules encode the assumption given in Formula (2).

The encoding of the computation of $\dot { \bar { f } } _ { 1 } \left( \vec { C } , \nu _ { 1 , s _ { 1 } } \right) , . . . , f _ { n } \left( \vec { C } , \nu _ { n , s _ { n } } \right)$ for a vector of execution costs ${ \vec { C } } = < c _ { 1 } , . . . , c _ { m } >$ yields two subsets of Π:

Suppose the given random forest is assembled with t decision trees $T _ { 1 } , . . . , T _ { t } ,$ then the encoding of the condition that ${ f _ { 1 } } \left( { \vec { C } } , { \nu _ { 1 , s _ { 1 } } } \right) , . . . , { f _ { n } } \left( { \vec { C } } , { \nu _ { n , s _ { n } } } \right)$ is classi<sup>fi</sup>ed to the preferred output class $o _ { p }$ yields another two subsets of Π:

1) The <sup>fi</sup>rst subset consists of rules that encode action constraints and is appended to Π in the sub-procedure “EncodeActionConstraints.” The rules added in line 2 specify that every action is applied with some execution cost or is not applied. The rules added in line 3 specify that an action cannot be applied with two different execution costs.

1) The <sup>fi</sup>rst subset consists of rules that encode the classi<sup>fi</sup>cation process of every decision tree and is appended to Π in the sub-procedure “EncodeDecisionTrees.” It is well-known that a decision tree can be translated into a set of rules, where each rule corresponds to a path

Sub-procedure EncodeActionConstraints

1. For all $1 \leq j \leq m$ do

1. For all $1 \leq i \leq t$ do

2. For each path $F _ { r _ { 1 } } = v _ { r _ { 1 } , u _ { 1 } } , F _ { r _ { 2 } } = v _ { r _ { 2 } , u _ { 2 } } , \cdots , F _ { r _ { k } } = v _ { r _ { k } , u _ { k } } , ~ o _ { l }$ from the root of $T _ { i }$ to a leaf of $T _ { i }$ such that $u _ { j } \geq s _ { r _ { j } }$ for all $1 \leq j \leq k$ , add a rule $y _ { r _ { 1 } , v _ { r _ { 1 } , u _ { 1 } } } \wedge y _ { r _ { 2 } , v _ { r _ { 2 } , u _ { 2 } } } \wedge$ $\cdot \cdot \wedge y _ { r _ { k } , v _ { r _ { k } , u _ { k } } } \to w _ { i , o _ { l } }$ to ∏;

3. For any two integers i and k such that $1 \leq j < k \leq q .$ , add a rule $w _ { i , o _ { j } } \wedge w _ { i , o _ { k } } \to$ ⊥ to $I I ;$

Sub-procedure EncodeVotingResult

1. For all $1 \leq i \leq q$ such that $i \neq p ,$ , add a pseudo-Boolean constraint

$$
\sum_ {j = 1} ^ {t} w _ {j, o _ {p}} - \sum_ {j = 1} ^ {t} w _ {j, o _ {i}} \geq 1 \text {   to   } \Pi ;
$$

Fig. 3. The sub-procedures for the MMAKD method.

from the root to a leaf of the decision tree. Thus, line 2 adds to Π all the rules translated from the paths that match a possible new state of the given instance, while line 3 adds to Π the rules that ensure the given instance with the new state to be classi<sup>fi</sup>ed to a unique class by an individual decision tree.

2) The second subset consists of pseudo-Boolean constraints that encode the output class of the given random forest and is appended to Π in the sub-procedure “EncodeVotingResult.” The constraints added in line 1 state that the mode of the class outputs of all decision trees assembled in the random forest is unique and is exactly the preferred class $o _ { p } .$

Finally, rules in Π are translated to a set of pseudo-Boolean constraint. Each rule can be translated to a set of logically equivalent SAT clauses [20] using the mapping function π. For example, $\pi ( C _ { 1 } \land C _ { 2 } ) = \{ C _ { 1 } , C _ { 2 } \}$ $\pi ( x _ { 1 }  x _ { 2 } ) = \{ \neg { x _ { 1 } } \lor x _ { 2 } \}$ $\pi ( x _ { 1 }  x _ { 2 } ) = \{ \lnot x _ { 1 } \lor x _ { 2 } \lor x _ { 3 } \lor x _ { 2 } \lor x _ { 3 } \lor x _ { 2 } \}$ ¬x<sub>2</sub> ∨ x<sub>1</sub>}, and $\pi ( x _ { 1 } \wedge x _ { 2 } \to \bot ) = \{ \neg { x } _ { 1 } \vee \neg { x } _ { 2 } \}$ , where $C _ { 1 }$ and $C _ { 2 }$ are standard SAT clauses, and $x _ { 1 }$ and x are variables. Moreover, SAT clauses of the form, $\neg x _ { 1 } \lor \dots \lor \neg x _ { p } \lor x _ { p + 1 } \lor \dots \lor x _ { q }$ (where $0 { \leq } p { \leq } q )$ is logically equal to a pseudo-Boolean constraint $- 1 \cdot x _ { 1 } + . . . + - 1 \cdot x _ { p } + ; 1 \cdot x _ { p + 1 } +$ $\dots { + 1 \cdot x _ { q } } { \geq 1 - p }$ (where $0 { \leq } p { \leq } q )$

Therefore, the target linear PBO problem is formed by combining the set of pseudo-Boolean constraints with the object function $\sum \mathbf { X } _ { \mathrm { j , c } \in \mathbf { X } } \mathbf { c } \cdot \mathbf { X } _ { \mathrm { j , c } }$ to be minimized. Each solution of the target linear PBO problem is a 0-1 truth assignment Φ on all variables appearing in Π. It corresponds to a cost-minimal action set. That is, for all 1 ≤ j ≤ m, let $c _ { j }$ be the unique execution cost of action $A _ { j }$ such that $\boldsymbol { \Phi } \big ( x _ { j , c _ { j } } \big ) = 1$ , then ${ \vec { C } } = < c _ { 1 } , . . . , c _ { m } >$ is a vector of execution costs <sup>¼ ¼</sup>that the original problem aims to compute.

## 5. Implementation of IF-ISPRP

## 5.1. Data collection

Researchers have proposed a variety of classi<sup>fi</sup>cation frameworks on software project risk factors. For example, Barki et al. [4] divided 35 software risks into <sup>fi</sup>ve dimensions, including technological newness, application size, expertise, application complexity, and organizational environment. Schmidt et al. [44] launched a cross-cultural research in Hong Kong, Finland, and the U.S. They established a framework that covers 14 dimensions and 33 risks. Wallace et al. [48] classi<sup>fi</sup>ed 27 software risk factors into six dimensions, as shown in Table 2. The current paper adopted the framework proposed by Wallace et al. because: 1) it not only systematically summarizes the previous studies but it also offers extensions; 2) it is relatively new, and it has been frequently cited for further investigation, e.g. in Han and Huang [24] and Huang and Han [26].

With the support of the Guangdong Software Industry Association, a total of 460 questionnaires were sent out and the respondents were requested to <sup>fi</sup>ll the questionnaires based on their recent software project. A total of 317 respondents (response rate of 69%) returned the questionnaires, out of which 269 were valid responses. Questionnaires missing any of the risk factor values were considered incomplete or invalid and thus excluded. Results showed that 27.1% of the projects were successful, while others were unsatisfactory or canceled. The surveys covered a wide variety of sectors such as government (15.2%), information industry (26%), manufacturing (11.9%), and commerce (15.2%). More than 80% of the respondents had related work experience of more than three years. The respondents were project managers (27.5%), project technical leaders (19.0%), development team members (34.9%), etc.

## 5.2. Module construction and evaluation

A risk analysis model requires method with good interpretability and high predictive accuracy. Numerous algorithms are suitable, such as the decision tree, the Bayesian network, etc. The present study adopts random forest algorithm which was usually shown to be more accurate than decision tree and is consistent with the proposed MMAKD method.

In this study, successful projects are regarded as positive samples, whereas failed ones are regarded as negative samples. We denote as TP the number of true positive samples (i.e., positive samples that are classi<sup>fi</sup>ed as positive), TN as the number of true negative samples, $F P$ as the number of false positive and FN as the number of false negative samples. To evaluate the model's performance, the following four measures are calculated.

$$
A c c u r a c y = \frac {T P + T N}{T P + T N + F P + F N}
$$

$$
P r e c i s i o n = \frac {\mathrm{TP}}{T P + F P}
$$

$$
\text { Recall } = \frac {T P}{T P + F N}
$$

$$
F \text {-measure} = \frac {2 \times \text { Precision } \times \text { Recall }}{\text { Precision } + \text { Recall }}
$$

The results of ten-fold cross-validation indicate that random forest performs best in terms of accuracy, recall, and F-measure with comparable precision, compared with other algorithms with good interpretability, including C4.5, naïve Bayes, and Bayesian networks. More details are shown in Table 3.

The risk planning module is implemented to reduce the risk planning problem into a linear PBO problem, which can be solved by a pseudo-Boolean solver (see Section 4 for more detail).

Risk dimensions and risk factors adopted from [48].

<table><tr><td>Risk dimension</td><td>Abbr.</td><td>Risk factors</td></tr><tr><td rowspan="4">Organizational environment risk</td><td>Org1</td><td>Change in organizational management during the project</td></tr><tr><td>Org2</td><td>Corporate politics with negative effect on project</td></tr><tr><td>Org3</td><td>Unstable organizational environment</td></tr><tr><td>Org4</td><td>Organization undergoing restructuring during the project</td></tr><tr><td rowspan="5">User risk</td><td>User1</td><td>Users resistant to change</td></tr><tr><td>User2</td><td>Conflict between users</td></tr><tr><td>User3</td><td>Users with negative attitudes toward the project</td></tr><tr><td>User4</td><td>Users not committed to the project</td></tr><tr><td>User5</td><td>Lack of cooperation from users</td></tr><tr><td rowspan="4">Requirement risk</td><td>Req1</td><td>Continually changing system</td></tr><tr><td>Req2</td><td>System requirements not adequately identified</td></tr><tr><td>Req3</td><td>Unclear system requirements</td></tr><tr><td>Req4</td><td>Incorrect system requirements</td></tr><tr><td rowspan="4">Project complexity risk</td><td>Comp1</td><td>Project involves the use of new technology</td></tr><tr><td>Comp2</td><td>High level of technical complexity</td></tr><tr><td>Comp3</td><td>Immature technology</td></tr><tr><td>Comp4</td><td>Project involves the use of technology that has not been used in prior projects</td></tr><tr><td rowspan="7">Planning and control risk</td><td>PaC1</td><td>Lack of an effective project management methodology</td></tr><tr><td>PaC2</td><td>Project progress not monitored closely enough</td></tr><tr><td>PaC3</td><td>Inadequate estimation of required resources</td></tr><tr><td>PaC4</td><td>Poor planning</td></tr><tr><td>PaC5</td><td>Project milestones not clearly defined</td></tr><tr><td>PaC6</td><td>Inexperienced project manager</td></tr><tr><td>PaC7</td><td>Ineffective communication</td></tr><tr><td rowspan="3">Team risk</td><td>Team1</td><td>Inadequately trained development team members</td></tr><tr><td>Team2</td><td>Inexperienced team members</td></tr><tr><td>Team3</td><td>Team members lack specialized skills required by the project</td></tr></table>

Please cite this article as: Y. Hu, et al., An integrative framework for intelligent software project risk planning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.12.029

## 6. Application of IF-ISPRP

To demonstrate the integrative risk analysis and planning, we applied the model to a real social media platform project called “Guangzhou Wireless City.” The project aims to establish an integrated social media platform, which provides a variety of social media applications for people in a city covered with ad-hoc wireless network. Due to privacy concern, basic information of the company is not presented in the paper.

A variety of information is required as input parameters, including the state assessment of risk factors, the many-to-many relationships between risk-control actions and risk factors, and the execution cost of each risk-control action.

The assessment of each input parameter was conducted by an expert panel, which is composed of three project key stakeholders, including the project manager, chief technical of<sup>fi</sup>cer, and customer manager. There are three rounds for the panelists to reach a consensus. In the <sup>fi</sup>rst round, each participant anonymously and independently gives his or her own opinion and a corresponding reason for each parameter. In the second round, based on the other experts' opinions and reasons collected in the <sup>fi</sup>rst round, each participant is asked to revise his or her opinion. In the third round, the differences in opinions are discussed until consensus is reached over all parameters.

In the present application, the reached consensus is shown in Table 4. The state of each risk factor is either high or low, indicating the degree of risk. Not surprisingly, the social software project mainly suffers from requirement and user risks. For example, con<sup>fl</sup>icts exist among users in terms of software functions, due to distinct purposes of using social software (User2 “Conflict between users”). In addition, user requirements are vague and unstable (Req1 “Continually changing system” and Req3 “Unclear system requirements”). Taking the states of risk factors as input, the risk analysis module predicted the “Guangzhou Wireless City” project as a failure.

The prediction implied that it is necessary to carry out the subsequent planning process.

First, the expert panel was asked to choose a subset among the 74 risk-control actions listed by Benaroch et al. [5] according to the real situation of the company. The <sup>fi</sup>nal consensus covers 12 risk-control actions as shown in Table 5.

Second. the expert panel was also asked to arrive at a consensus on how each risk factor can be improved by speci<sup>fi</sup>c risk-control actions given a speci<sup>fi</sup>c execution cost. Considerable amount of effort was spent to con<sup>fi</sup>rm this information (shown in Table 6). Each action can change the state of the corresponding risk factor from high to low with a given execution cost.

Given the above parameters as input, a cost-minimal action set for risk control was computed by the risk planning module as shown in Table 7.

The solution shows that if two actions, Act3 and Act12, are applied with a total execution cost of 90,000 RMB, the “Guangzhou Wireless City” project will be predicted as a success. In total, the risk analysis model generates ten decision trees. Fig. 4 only shows how the Act3 changes the states of risk factors for achieving a success prediction. The effect of Act12 is manifested in another decision tree(s). As the state of PaC4 is originally high, the project is consequently predicted as a failure in Fig. 4 (node 4). The state of PaC4 can be changed into

Table 3  
Comparison of performances.

<table><tr><td></td><td>Random forest</td><td>C4.5</td><td>Naïve Bayes</td><td>General Bayesian networks</td></tr><tr><td>Accuracy</td><td>82.2%</td><td>76.2%</td><td>76.9%</td><td>77.7%</td></tr><tr><td>Precision</td><td>85.9%</td><td>84.0%</td><td>93.5%</td><td>86.2%</td></tr><tr><td>Recall</td><td>90.3%</td><td>83.2%</td><td>73.5%</td><td>82.7%</td></tr><tr><td>F-Measure</td><td>0.881</td><td>0.836</td><td>0.823</td><td>0.844</td></tr></table>

PS.: High risk project is treated as positive class

## Table 4

Risk assessment of the “Guangzhou Wireless City” project

<table><tr><td>Risk</td><td>State</td><td>Risk</td><td>State</td><td>Risk</td><td>State</td></tr><tr><td>Org1</td><td>High</td><td>Req1</td><td>High</td><td>PaC2</td><td>Low</td></tr><tr><td>Org2</td><td>Low</td><td>Req2</td><td>High</td><td>PaC3</td><td>Low</td></tr><tr><td>Org3</td><td>Low</td><td>Req3</td><td>High</td><td>PaC4</td><td>High</td></tr><tr><td>Org4</td><td>Low</td><td>Req4</td><td>Low</td><td>PaC5</td><td>High</td></tr><tr><td>User1</td><td>Low</td><td>Comp1</td><td>Low</td><td>PaC6</td><td>Low</td></tr><tr><td>User2</td><td>High</td><td>Comp2</td><td>High</td><td>PaC7</td><td>Low</td></tr><tr><td>User3</td><td>Low</td><td>Comp3</td><td>Low</td><td>Team1</td><td>High</td></tr><tr><td>User4</td><td>High</td><td>Comp4</td><td>Low</td><td>Team2</td><td>Low</td></tr><tr><td>User5</td><td>High</td><td>PaC1</td><td>Low</td><td>Team3</td><td>Low</td></tr></table>

low by Act3 “Research/better project planning,” with an execution cost of 40,000 RMB; the project then changes from a failure prediction to as a success prediction (Org2=low, Team2=low, PaC7=low, so falls into node 11 in Fig. 4).

It is interesting that the model chooses Act3 to make the project outcome prediction a success rather than take actions Act6, Act7 or Act8, which aim to mitigate requirement risks (as shown in Table 6). A rational explanation may be that such social software project has inherent risk of frequent requirement changes, thus improving project planning ability is more effective than directly mitigating the requirement risks.

## 7. Discussion

The proposed framework, IF-ISPRP, can adopt various risk factor models, thus it can be adapted to other risk management <sup>fi</sup>elds. Moreover, we discuss the established model in the following aspects:

1) Objective function. The model minimizes the total execution cost for risk control, i.e., generate a cost-minimal action set. However, it can be adapted to optimize alternative objective functions, such as the total utility or execution time. The model outputs only one solution with the minimal total cost. However, it can be adapted to produce multiple solutions that are equally good; therefore, project stakeholders are given the freedom to choose the one best suited to their situations.

2) Method. The MMAKD method uses random forest as the risk analysis model. Random forest can be transformed to a set of (classi<sup>fi</sup>- cation) rules with a good interpretability, and is well-<sup>fi</sup>tted for solving and explaining risk planning problems. Bayesian network may be another good choice for the risk analysis model because it has also a good interpretability and can cope with uncertainty. However, we need to extract rules from a Bayesian network for applying the MMAKD method. Although there exist methods for extracting rules from a Bayesian network [13], the extraction of rules is clearly out of the scope of this study; thus Bayesian network is not used as the risk analysis model in this study.

## Table 5

Candidate risk-control actions.

<table><tr><td>ID</td><td>Risk control action</td></tr><tr><td>Act1</td><td>Get corporate sponsor</td></tr><tr><td>Act2</td><td>Plan for change management</td></tr><tr><td>Act3</td><td>Research/better project planning</td></tr><tr><td>Act4</td><td>Put QA process in place</td></tr><tr><td>Act5</td><td>Deployed in a small market segment</td></tr><tr><td>Act6</td><td>More testing of IT elements of the project</td></tr><tr><td>Act7</td><td>5–10% of investment gone into research prior to full commitment</td></tr><tr><td>Act8</td><td>Staged implementation-rolling releases</td></tr><tr><td>Act9</td><td>MOSCOW (get project&#x27;s Must haves, then Should haves, Could haves, and finally Would haves)</td></tr><tr><td>Act10</td><td>Contingency plan/possibility to abandon existed</td></tr><tr><td>Act11</td><td>Get corporate sponsor</td></tr><tr><td>Act12</td><td>Extra training of employees</td></tr></table>

Please cite this article as: Y. Hu, et al., An integrative framework for intelligent software project risk planning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.12.029

Table 6  
Many-to-many relationship and execution cost of risk-control actions

<table><tr><td></td><td>Org1</td><td>Org2</td><td>Org3</td><td>User1</td><td>User3</td><td>User4</td><td>Req1</td><td>Req2</td><td>Req3</td><td>Req4</td><td>Comp2</td><td>PaC1</td><td>PaC4</td><td>PaC5</td><td>Team1</td></tr><tr><td>Act1</td><td></td><td></td><td></td><td></td><td></td><td>15W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Act2</td><td>10W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3W</td><td></td></tr><tr><td>Act3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>10W</td><td>4W</td><td></td><td></td></tr><tr><td>Act4</td><td></td><td></td><td>20W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Act5</td><td></td><td></td><td></td><td>5W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Act6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>7W</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Act7</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5W</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Act8</td><td></td><td></td><td></td><td></td><td>35W</td><td></td><td>10W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Act9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Act10</td><td></td><td>50W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Act11</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5W</td><td></td><td></td><td></td><td></td></tr><tr><td>Act12</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5W</td></tr></table>

W stands for ten thousand CNY.

3) Continuous risk management. It is usually impossible to eliminate all risks by a single round of risk analysis and planning. A long-term, continuous, and iterative process of risk assessment, analysis, planning, resolution, and tracking, needs to be performed on a regular interval (weekly, monthly, at every milestone, etc.) throughout the lifecycle of a software project. During and after the implementation of the risk-control plan, the states of the risk factors should be dynamically monitored and tracked. The feedback information should be provided for subsequent reassessment of risk factors and for making a new risk-control plan (using the proposed framework).

## 8. Conclusion and limitations

Risk analysis and planning are complex, resulting in dif<sup>fi</sup>culties to manage risks effectively through subjective judgment. So far, the SPRM domain lacks an empirical integrative intelligent model for risk analysis and planning. The current study has two major contributions:

1) The proposed IF-ISPRP is the <sup>fi</sup>rst integrative framework for intelligent SPRM, which aims at generating a cost-minimal risk-control action set. In addition, an empirical model is established based on real software project data.

2) The proposed MMAKD method considers the many-to-many relationship between risk factors and risk-control actions, which is prevalent in practical risk planning. Compared with existing studies that use integer-programming technology [6], this method directly uses a risk analysis model and is more reasonable.

To demonstrate the effectiveness of the model, application of the model on a social software project showed how the model generates a risk-control plan to mitigate the whole project risk. To control the high-level requirement and user risks, the model suggests the need to improve project planning ability and train the development team. This suggestion may also be applied to other social software projects.

However, our research has the following limitations:

1) Although the MMAKD method can <sup>fi</sup>nd a cost-minimal risk-control action set, it does not consider the execution order of risk-control actions. However, it is very hard or even unrealistic for practitioners to de<sup>fi</sup>ne complete information for order constraints among different candidate risk-control actions. Therefore, our model assumes that all actions can be executed simultaneously.

Table 7  
Cost-minimal risk-control action set.

<table><tr><td>No.</td><td>Action</td><td>Cost</td><td>Effects</td></tr><tr><td>1</td><td>Act3</td><td>4</td><td>Change PaC4 from high to low</td></tr><tr><td>2</td><td>Act12</td><td>5</td><td>Change Team1 from high to low</td></tr></table>

2) In order to facilitate the modeling and application process, three reasonable assumptions are taken to simplify the risk planning problems. For example, the assumption that the effect of an action is de<sup>fi</sup>ned using a monotonically increasing step function on the execution cost of the action (i.e., the more costs we input, the better effectiveness of risk control we will have) only works in certain situations. Hence, if extreme result occurs, the experts must make additional judgments and adjustments before the implementation of the risk-control plan. As George Box said, “All models are wrong, but some models are useful” [10, p. 202], the established model is only a simpli<sup>fi</sup>cation of the real world it represents and as such, it is merely suitable for a limited range of situations.

## Acknowledgments

This research was partly supported by the National Natural Science Foundation of China (71271061, 70801020), Science and Technology Planning Project of Guangdong Province, China (2010B010600034, 2012B091100192), and Business Intelligence Key Team of Guangdong University of Foreign Studies (TD1202).

![](/api/attachments/6ME2D4R2/fulltext/images/d2c767bb7c662ecda5ab57c8b6dbaf4bf04d830d1393bb0919afb4e74452c961.jpg)  
Fig. 4. Effect of risk-control action.  
Please cite this article as: Y. Hu, et al., An integrative framework for intelligent software project risk planning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.12.029

## References

[1] CMMI Product Team, Capability Maturity Model Integration (CMMI<sup>SM</sup>) Version 1.1, CMMI for Systems Engineering, Software Engineering, Integrated Product and Process Development, and Supplier Sourcing (CMMI-SE/SW/IPPD/SS, V1.1), 2002.

[2] J. Aguilar-Ruiz, I. Ramos, J. Riquelme, M. Toro, An evolutionary approach to estimating software development projects, Information and Software Technology 43 (14) (2001) 875–882

[3] P.L. Bannerman, Risk and risk management in software projects: a reassessment, Journal of Systems and Software 81 (12) (2008) 2118–2133.

[4] H. Barki, S. Rivard, J. Talbot, Toward an assessment of software development risk, Journal of Management Information Systems 10 (2) (1993) 203–225.

[5] M. Benaroch, Y. Lichtenstein, K. Robinson, Real options in IT risk management: an empirical validation of risk-option relationships, MIS Quarterly 30 (2) (2006) 827–864.

[6] I. Ben-David, T. Raz, An integrated approach for risk response development in project planning, Journal of the Operational Research Society 52 (1) (2001) 14–25.

[7] J.C. Bennett, G.A. Bohoris, E.M. Aspinwall, R.C. Hall, Risk analysis techniques and their application to software development, European Journal of Operational Research 95 (3) (1996) 467–475.

[8] B.W. Boehm, Software Risk Management, IEEE Computer Society Press, Los Alamitos, CA, 1989.

[9] B.W. Boehm, Software risk management: principles and practices, IEEE Software (1991) 32–41.

[10] G.E.P. Box, Robustness in the strategy of scienti<sup>fi</sup>c model building, in: R.L. Launer, G.N. Wilkinson (Eds.), Robustness in Statistics, Academic Press, New York, 1979, pp. 201–235.

[11] D. Boyd, The signi<sup>fi</sup>cance of social software, in: J.S. Thomas, N. Burg (Eds.), BlogTalks Reloaded: Social Software Research & Cases Books on Demand Vienna 2o07 pp. 15–30.

[12] L. Breiman, Random forests, Machine Learning 45 (1) (2001) 5–32.

[13] G. Bressan, V. Oliveira, E. Hruschka Jr., M. Nicoletti, Using Bayesian networks with rule extraction to infer the risk of weed infestation in a corn-crop, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 22 (4–5) (2009) 579–592.

[14] G. Büyüközkan, D. Ruan, Choquet integral based aggregation approach to software development risk assessment, Information Sciences 180 (3) (2010) 441–451.

[15] D. Chai, A. Kuehlmann, A fast pseudo-Boolean constraint solver, Computer-Aided Design of Integrated Circuits and Systems, IEEE Transactions on 24 (3) (2005) 305–317.

[16] R. Charette, Software Engineering: Risk Analysis and Management, McGraw-Hill, Inc., New York, NY, 1989.

[17] J. Drew Procaccino, J. Verner, S. Overmyer, M. Darter, Case study: factors for early prediction of software development success, Information and Software Technolog 44 (1) (2002) 53–62.

[18] J. Drew Procaccino, J. Verner, M. Darter, W. Amadio, Toward predicting software development success from the perspective of practitioners: an exploratory Bayesian model, Journal of Information Technology 20 (3) (2005) 187–200.

[19] S. Du, M. Keil, L. Mathiassen, Y. Shen, A. Tiwana, Attention-shaping tools, expertise, and perceived control in IT project risk assessment, Decision Support Systems 43 (1) (2007) 269–283.

[20] N. Eén, N. Sörensson, Translating pseudo-Boolean constraints into SAT, Journal on Satis<sup>fi</sup>ability, Boolean Modeling and Computation 2 (3–4) (2006) 1–26.

[21] C. Fan, Y. Yu, BBN-based software project risk management, Journal of Systems and Software 73 (2) (2004) 193–203.

[22] Q. Gao, Y. Dai, Z. Fan, R. Kang, Understanding factors affecting perceived sociability of social software, Computers in Human Behavior 26 (6) (2010) 1846–1861.

[23] E.D. Hahn, J. Doh, K. Bunyaratavej, The evolution of risk in information systems offshoring: the impact of home country risk, <sup>fi</sup>rm learning, and competitive dynamics, Management Information Systems Quarterly 33 (3) (2009) 597–616.

[24] W. Han, S. Huang, An empirical analysis of risk components and performance on software projects, Journal of Systems and Software 80 (1) (2007) 42–50.

[25] R.P. Higuera, Y.Y. Haimes, Software risk management, Software Engineering Institute, Carnegie Mellon University, 1996.

[26] S. Huang, W. Han, Exploring the relationship between software project duration and risk exposure: a cluster analysis, Information Management 45 (3) (2008) 175-182.

[27] J. Jiang, G. Klein, Risks to different aspects of system success, Information Management 36 (5) (1999) 263–271.

[28] J. Jiang, G. Klein, T. Ellis, A measure of software development risk, Project Management Journal 33 (3) (2002) 30–41.

[29] J. Jiang, G. Klein, H. Chen, The effects of user partnering and user non-support on project performance, Journal of the Association for Information Systems 7 (2) (2006) 68–90.

[30] E.J.M. Lauría, P.J. Duchessi, A Bayesian belief network for IT implementation decision support, Decision Support Systems 42 (3) (2006) 1573–1588.

[31] E. Lauría, P. Duchessi, A methodology for developing Bayesian networks: an application to information technology (IT) implementation, European Journal of Operational Research 179 (1) (2007) 234–252.

[32] J. Li, R. Conradi, O. Slyngstad, M. Torchiano, M. Morisio, C. Bunse, A state-of-the-practice survey of risk management in development with off-the-shelf software components, IEEE Transactions on Software Engineering 34 (2) (2008) 271–286.

[33] C. Ling, T. Chen, Q. Yang, J. Cheng, G. Analytics, Mining optimal actions for pro<sup>fi</sup>table CRM, Proceedings of 2002 IEEE International Conference on Data Mining (Citeseer), 2002, pp. 767–770.

[34] X. Liu, G. Kane, M. Bambroo, An intelligent early warning system for software quality improvement and project management, Journal of Systems and Software 79 (11) (2006) 1552–1564.

[35] V. Manquinho, O. Roussel, The <sup>fi</sup>rst evaluation of pseudo-Boolean solvers, Journa on Satis<sup>fi</sup>ability, Boolean Modeling and Computation 2 (2006) 103–143.

[36] S. McConnell, Software Project Survival Guide: How to Be Sure Your First Important Project Isn't Your Last, Microsoft Press, Redmond, WA, 1997.

[37] M. Moreno García, I. Román, F. García Peñalvo, M. Bonilla, An association rule mining method for estimating the impact of project management policies on software quality, Development Time and Effort, Expert Systems with Applications 34 (1) (2008) 522–529.

[38] K. Na, J. Simpson, X. Li, T. Singh, K. Kim, Software development risk and project performance measurement: evidence in Korea, Journal of Systems and Software 80 (4) (2007) 596–605.

[39] E. Ngai, F. Wat, Fuzzy decision support system for risk analysis in e-commerce development Decision Support Systems 40 (2) (2005) 235–255

[40] C. Pan, Y. Chen, An optimization model of CMMI-based software project risk response planning, International Journal of Applied Mathematics and Computer Sciences 1 (2005) 155–159.

[41] B. Reyck, Y. Grushka-Cockayne, M. Lockett, S. Calderini, M. Moura, A. Sloper, The impact of project portfolio management on information technology projects, In ternational Journal of Project Management 23 (7) (2005) 524–537.

[42] F. Reyes, N. Cerpa, A. Candia-Véjar, M. Bardeen, The optimization of success probability for software projects using genetic algorithms, Journal of Systems and Software 84 (5) (2011) 775–785.

[43] L. Rosenberg, T. Hammer, A. Gallo, Continuous risk management at NASA, The Applied Software Measurement/Software Management Conference, (San Jose, CA, USA), 1999.

[44] R. Schmidt, K. Lyytinen, M. Keil, P. Cule, Identifying software project risks: an International Delphi Study, Journal of Management Information Systems 17 (4) (2001) 5–36.

[45] H. Sheini, K. Sakallah, Pueblo: a hybrid pseudo-Boolean SAT solver, Journal on Satis<sup>fi</sup>ability, Boolean Modeling and Computation 2 (2006) 61–96.

[46] The Standish Group, New Standish Group Report Shows More Project Failing and Less Successful Projects, in, The Standish Group, Boston, Massachusetts, 2010.

[47] A. Tiwana, M. Keil, Functionality risk in information systems development: an empirical investigation, IEEE Transactions on Engineering Management 53 (3) (2006) 412–425

[48] L. Wallace, M. Keil, A. Rai, How software project risk affects project performance: an investigation of the dimensions of risk and an exploratory model, Decision Sciences 35 (2) (2004) 289–321.

[49] L. Wallace, M. Keil, A. Rai, Understanding software project risk: a cluster analysis, Information Management 42 (1) (2004) 115–125.

[50] E. Wang, P. Ju, J. Jiang, G. Klein, The effects of change control and management review on software <sup>fl</sup>exibility and project performance, Information Management 45 (7) (2008) 438–443.

[51] F. Wu, H. Li, L. Chu, D. Sculli, K. Gao, An approach to the valuation and decision of ERP investment projects based on real options, Annals of Operations Research 168 (1) (2009) 181–203

[52] Q. Yang, J. Yin, C. Ling, T. Chen, Postprocessing decision trees to extract actionable knowledge, Proceeding of 2003 Third JEEE International Conference on Data Mining (IEEE). 2003, pp. 685–688

[53] Q. Yang, J. Yin, C. Ling, R. Pan, Extracting actionable knowledge from decision trees, IEEE Transactions on Knowledge and data Engineering 19 (1) (2007) 43–56.

[54] H. Yen, E. Li, B. Niehoff, Do organizational citizenship behaviors lead to information system success?: Testing the mediation effects of integration climate and project management, Information Management 45 (6) (2008) 394–402.

[55] G. Zhang, M. Keil, A. Rai, J. Mann, Predicting information technology project escalation: a neural network approach, European Journal of Operational Research 146 (1) (2003) 115–129.

Yong Hu is currently an Associate Professor and Chair in the Department of e-commerce, and Director of Institute of Business Intelligence and Knowledge Discovery at the Guangdong University of Foreign Studies and Sun Yat-Sen University. He received his B.Sc in Computer Science, M.Phil and Ph.D. in Management Information Systems from Sun Yat-Sen University. His research interests are in the areas of business intelligence, software project risk management, e-commerce and decision support systems. He has published in a number of journals and conferences such as DSS, ESWA and IEEE ICDM. Dr. Hu's research is supported by the National Natural Science Foundation, the Science and Technology Planning Project of Guangdong Province, and “211 Project” of the Guangdong University of Foreign Studies.

Jianfeng Du is currently a lecturer in Institute of Business Intelligence and Knowledge Discovery in Guangdong University of Foreign Studies. He received the Ph.D. degree from the State Key Laboratory of computer science, Institute of Software, Chinese Academy of Sciences, and both the Master degree and the Bachelor degree from Sun Yat-Sen University in PR China. His current research interests include knowledge representation and reasoning, and semantic web. He has published papers in major conferences in these areas, such as IJCAI, AAAI, UAI, WWW and ISWC

Xiangzhou Zhang is a Ph.D. student in Sun Yat-sen University and working as an assistant researcher in Institute of Business Intelligence and Knowledge Discovery at the Guangdong University of Foreign Studies and Sun Yat-sen University, He has received his B S degree in Computer Science from Sun Yat-sen University, and M.S. degree in Management from Guangdong University of Foreign Studies. His research interests include data mining, software project risk management, and business intelligence

Xiaoling Hao is an associate professor at the School of Information Management and Engineering, Shanghai University of Finance and Economics. She was a visiting scholar at the Foster School of Business, University of Washington. Her research interests include project management and IT governance.

Prof. Eric Ngai is a Professor in the Department of Management and Marketing at The Hong Kong Polytechnic University. His current research interests are in the areas of e-commerce, Supply Chain Management, Decision Support Systems and RFID Technology and Applications. He has published papers in a number of international journals including MIS Quarterly, Journal of Operations Management, Decision Support Systems, IEEE Transactions on Systems, Man and Cybernetics, Information & Management, Production & Operations Management, and others. He is an Associate Editor of European Journal of Information Systems and serves on editorial board of six international journals. Prof. Ngai has attained an h-index of 13, and received 510 citations, ISI Web of Science.

Ming Fan is an associate professor in information systems at Foster School of Business, University of Washington. He received his B.S. from Nanjing University, China and Ph.D. degree in information systems management from the business school in University of Texas at Austin. He is an associate editor of Information Systems Research, Decision Sciences Journal, and Decision Support Systems.

Mei Liu is currently an Assistant Professor in the Department of Computer Science at New Jersey Institute of Technology. She received her Ph.D. degree in Computer Science from the University of Kansas, Lawrence, USA and completed her postdoctoral training as an NIH-NLM research fellow in the Department of Biomedical Informatics at Vanderbilt University, Nashville, USA. Her research interest includes data mining, machine learning, text mining, decision support systems, quantitative investment, and medical informatics. She has published a number of papers in conferences and journals such as Bioinformatics, JAMIA, ESWA, EURASIP Journal on Applied Signal Processing, BMC Bioinformatics, PLoS ONE, and IEEE ICDM.
