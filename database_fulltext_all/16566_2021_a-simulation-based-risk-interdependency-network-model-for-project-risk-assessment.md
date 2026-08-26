---
otero_id: 16566
otero_key: "XG2P2TKB"
title: "A simulation-based risk interdependency network model for project risk assessment"
authors: "Li Guan; Alireza Abbasi; Michael J. Ryan"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113602"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
A simulation-based risk interdependency network model for project risk assessment

Author: Guan, Li; Abbasi, Alireza; Ryan, Michael

Publication details: Decision Support Systems v. 148 0167-9236 (ISSN); 1873-5797 (ISSN)

Publication Date: 2021-05-21

Publisher DOI: https://doi.org/10.1016/j.dss.2021.113602

License: https://creativecommons.org/licenses/by-nc-nd/4.0/ Link to license to see what you are allowed to do with this resource.

Downloaded from http://hdl.handle.net/1959.4/unsworks\_75946 in https:// unsworks.unsw.edu.au on 2026-07-11

# A simulation-based risk interdependency network model for project risk assessment

Li Guan, Alireza Abbasi<sup>\*</sup>, and Michael J. Ryan

School of Engineering and Information Technology, UNSW, Canberra, Australia.

li.guan1@student.adfa.edu.au, a.abbasi@unsw.edu.au, mike.ryan@ieee.org

## Abstract

Project risks are mostly considered to be independent in risk management, ignoring interdependencies among them, which can lead to inappropriate risk assessment and reduced efficacy in risk treatment. This study introduces a new Monte Carlo simulation-based risk interdependency network model to support decision makers in assessing project risks and planning risk treatment actions more effectively. The Interpretive Structural Modeling method is integrated into this model to develop a hierarchical project risk interdependency network based on identified risks and their cause-effect relationships. The Monte Carlo method is used to model the stochastic behavior of risk occurrence and to generate numerous possible risk scenarios through simulation. To evaluate single risks and overall project risk level while considering risk interdependencies, five major risk indicators are therefore proposed, namely simulated occurrence probability of a risk, simulated local and global influence of a risk, as well as total risk loss and total risk propagation loss of a project. An additional sensitivity analysis is also included to examine the effects of input uncertainties of this model on risk assessment results. Moreover, two case studies are provided to demonstrate the application and effectiveness of the proposed model. The findings accentuate the significance of considering risk interdependencies in project risk assessment and validate the model’s robustness and feasibility in risk management of projects with complex interrelated risks. Keywords: Project risk assessment; Risk interdependency; Interpretive Structural Modeling; Monte Carlo simulation; Sensitivity analysis

## 1. Introduction

Project risk is defined as “the effect of uncertainty on objectives” [1] or “an uncertain event or condition that, if it occurs, has a positive or negative effect on one or more project objectives” [2]. If project risks cannot be managed effectively and efficiently using a systematic approach, it is hard to achieve project objectives. Throughout a project life cycle, a risk management process mainly comprises risk assessment (involving risk identification, risk analysis, and risk evaluation), risk treatment, and risk monitoring and review. Among these phases, risk assessment is the essential activity that allows decision makers to develop an overall risk perception

of a project and therefore to make appropriate risk response decisions proactively [3]. In a real-life project, risks

are often interrelated by complex and varied cause-effect relationships [4] where a risk is likely to trigger the

occurrence of one or more other risks [5,6]. Such risk interdependencies can therefore cause the propagation

from one upstream risk to numerous downstream risks, or a downstream risk may arise from the occurrence of

several upstream risks [7,8]. A chain reaction phenomenon or “domino effect” is the extreme case of this

propagation behavior of risk interdependencies [8]. As a result, in order to improve the effectiveness and

accuracy of project risk assessment (PRA) and predict the emergent behavior of severe risk propagation in time,

risk interdependencies should not be ignored, particularly for the risk management of complex projects.

PRA is inherently related to risk modeling [9]. The prevailing classical Probability–Impact (P–I) risk model,

assessing project risks through their probability of occurrence and corresponding impact on project objectives if

the risks occur, has been gradually extended and incorporated additional parameters to reflect the complexity of

PRA [4,9,10]. Compared with risk checklists and risk P–I matrix, a risk interdependency network (RIN) is more

capable of facilitating modeling and revelation of complex interdependencies among project risks, where nodes

and directed edges represent risks and risk interdependencies, respectively [11,12]. In a project RIN, the

evaluation of a given risk varies with the number of the risks which can trigger it, meaning the obtained influence

of the risk is not always constant due to the stochastic behavior of occurrence of interrelated risks [13].

There may be risk loops in a project RIN where several risks are in a closed causal path [8,13]. For example,

a cost overrun risk – the initial risk in a risk loop – may lead to the subsequent occurrence of a technical risk

which can then influence a project schedule delay, and the original risk of cost overrun may reoccur and is further

amplified on account of the occurrence of the schedule delay risk. Such cases cannot be treated adequately using

analytical PRA methods. Therefore, it is crucial to develop intelligent risk modeling methods that can provide

more objective, repeatable, and visible decision-making support for project management.

In this work, we explore a decision-support system using a simulation-based approach to assess project risks

and further support making risk treatment decisions while taking into account risk interdependencies. Only the

project risks with negative effects are considered in this paper. Specifically, after project risks and their cause-

effect relationships are identified, the Interpretive Structural Modeling (ISM) method is used to present complex project risk interdependencies within a hierarchical RIN. Then, in one of the main contributions of this work, a new Monte Carlo simulation (MCS)-based RIN model is developed to evaluate project risks, which has addressed the two aforementioned intractable problems of analytical risk models, namely the stochastic behavior of risk occurrence and risk loops in a project RIN.

When conducting the PRA, the inputs to the proposed MCS-based RIN model are: risk spontaneous probability (SP) (i.e., the occurrence probability of a risk, ignoring the influence of all other risks and their causeeffect relationships), risk transition probability (TP) (i.e., the probability that one risk can trigger another risk inside the RIN), and the risk impact on project objectives (IO). The main outputs of the proposed simulation model are five newly developed risk indicators: risk’s simulated occurrence probability (SOP), simulated local influence (SLI), and simulated global influence (SGI); as well as a project’s total risk loss (TRL) (i.e., the project’s total risk influence at the local level), and total risk propagation loss (TRPL) (i.e., the project’s total risk influence at the global level).

Additionally, a sensitivity analysis is embedded into the simulation model to examine the effects of input uncertainties on the outputs. These PRA results obtained from the simulation model, together with the risk categorization in terms of source risk, transition risk, and accumulation risk determined based on risks’ input and output links in the RIN, can support decision makers in planning more effective and comprehensive risk treatment actions. The development of these new risk indicators that can be used for PRA and risk treatment is another main contribution of our work.

The remainder of this paper is structured as follows. Section 2 provides an overview of the existing research on modeling project risks. Section 3 introduces the process of developing the proposed MCS-based RIN model for assessing project risks and planning risk treatment actions. Applications of this model and corresponding computational results through two case studies are demonstrated in Section 4. The implications of this study are discussed in Section 5, and conclusions and future research directions are presented in Section 6.

## 2. Related works

This section briefly reviews the literature of existing methods for project risk modeling and assessment mainly from three aspects: (i) conventional analytical PRA methods, (ii) analysis of risk interdependencies in project risk management, and (iii) MCS-based PRA methods. Respective research gaps of each strand, to be addressed in this work, are also summarized in a separate sub-section.

## 2.1. Conventional analytical PRA methods

As a project attribute, risks are generally characterized in terms of their probability (P) of occurrence and corresponding impact (I) on project objectives [1,2,4,14]. The risk criticality (RC) indicator has been widely recognized as an aggregate measure of risk importance, often defined as the multiplication of evaluated values of P and I [14–16]. Decision makers usually develop a two-dimensional risk matrix combining P and I ratings to assess individual risks and categorize risks in a project [2,17,18]. Efforts have increased for improving the P–I risk model and more analytical PRA methods are proposed to handle risks in increasingly complex projects. Fuzzy Set Theory (FST) is introduced to deal with ambiguous, subjective and imprecise judgments of decisionmaking during the PRA [3]. As an application of the FST, Fuzzy Synthetic Evaluation (FSE) method aims to provide a synthetic evaluation of an object relative to an objective in a fuzzy decision environment with multiple criteria, which has been adopted to develop several PRA models [19,20]. Some other Multi Criteria Decision Making (MCDM) methods are commonly used for assessing project risks, such as Analytical Hierarchy Process (AHP) [21] and Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) [22], which are effective in facilitating decision maker’s personal judgement in quantifying relative priorities of decision alternatives. However, the major weakness of these conventional analytical PRA methods is that they fail to consider interdependencies among project risks in PRA. Nonetheless, the concept of the P–I risk model still dominates in the risk management field and has laid a foundation for improvement and generation of more effective PRA methods [9].

## 2.2. Analysis of risk interdependencies in project risk management

From a project complexity-based perspective, more systematic and sophisticated PRA methods have been explored to represent and model risk interdependencies. Several methods are used to identify causes and effects of a single risk. For example, Failure Modes and Effect Analysis (FMEA) is a systematic approach appropriate for identifying different modes of failure and evaluating associated risks based on the values of risk priority number [23]; Fault Tree Analysis (FTA) is employed to construct failure dependencies in a tree form through logical ‘AND’ and ‘OR’ gates, which provides a good sketch of root-causes and cause-effect relationships of the particular risk analyzed [24]. These methods are mainly criticized for their inability to model complex

interdependencies among project risks [25].

Further, network structure, which can represent the causal relationships among project risks, is gradually applied to the analysis of project risk interdependencies, and some specific methods have been proposed. The Analytic Network Process (ANP) considers pairwise comparisons of risks and is able to capture possible causal relationships between clusters (group-risks) as well as among elements (sub-risks) within a cluster [26,27], but a large number of comparison matrices would be required especially for complex projects. The Bayesian Belief Network (BBN) is a probabilistic model that can visualize uncertain knowledge and perform efficient reasoning given a directed acyclic graph which represents the network structure and an associated set of conditional probability tables [3,28]. The BBN has gained much popularity in the PRA due to its robust theoretical framework and the ability to capture uncertainty and to update beliefs when new information becomes available [18,29]. As an example, Hu et al. [28] proposed a BBN-based model with causality constraints for better risk analysis and control of software development projects. Nevertheless, Marle and Vidal [4] pointed out that the BBN demands for oriented links and is acyclic inherently so that it is incapable of modeling some aspects of risk network complexity, such as loops, chain reactions or non-linear couplings. Therefore, they explored the potential applications of Design Structure Matrix (DSM) principles and defined a binary risk structure matrix to represent project risk interactions. AHP-based principles were then used to build a risk numerical matrix considering both causes and effects for catching the strength of these risk interactions. This approach to modeling complex risk interdependencies has inspired many later studies on project management [7,8,11,12,14,25,30]. Moreover, some other network-based methods have also been incorporated into project risk management to improve the modeling of risk interdependencies.

Structural Equation Modeling (SEM), as a statistical method, can recognize complex interrelations among observed or latent variables [30,31]. One of the noteworthy efforts of risk modeling in this regard is the risk-path model developed by Eybpoosh et al. [31] in which both measurement and construct models were used, where measurement model provides the relationships between each risk (the observed variable) and its respective risk category (the latent variable), while the construct model estimates the structural relationships among the validated risk categories. They demonstrated that a network of diverse interactive risks consisting of several risk paths and vulnerability factors can better reflect the complex nature of multiple risk sources than hierarchical lists in real construction projects, but the SEM cannot be used to assess the probability of the occurrence of risk paths

unless being improved by combining with probabilistic techniques. Additionally, only the interdependencies

among risk categories are presented in the SEM, which ignores cause-effect relationships among individual risks

with a risk category.

Social Network Analysis (SNA) is typically concerned with analyzing the structure and pattern of

relationships among system components. Analyzing the patterns and/or structure of an interrelated risk network

assists to investigate the influence of overall risk cause-effect relationships on individual risks. However, using

SNA alone cannot reveal the uncertainty issues and dynamics of the risk network [12,32]. In addition, although

the critical project risks and their interactions can be determined by the SNA indicators, their probability and

influence level cannot be reflected from a whole network view [32].

Interpretive Structural Modeling (ISM), an interactive learning process aiming to identify complex

interrelationships among elements of a system, has the advantage of structuring all the interrelated elements into

a comprehensive systematic model, either directly extracted from the responses of participants or by the

application of transitive inference [33,34]. The ISM has been used in many recent studies on modeling of project

risk interdependencies [6,35–37]. For instance, Guan et al. [6] constructed a hierarchical network structure based

on the ISM method to illustrate cause-effect relationships among project constraints, risk factors, and project

objectives of green building projects. Critical risk factors and constraints were then determined by calculating

their importance to project objectives based on influence transmission through network paths. The main

limitation of ISM is its inability to evaluate the strength of interdependency between interrelated elements [35].

Compared with analyzing risks independently in PRA, different kinds of risk treatment actions would be

formulated when further taking risk interdependencies into account [38]. In a project RIN, risks are usually

categorized into several categories according to their interactions with other dependent risks (e.g., being

autonomous risk, dependent risk, linkage risk, and independent risk in [6], or being source risk, transition risk,

and accumulation risk in [8]) and therefore, risk treatment actions, which focus on the mitigation of risk

propagation across a project RIN, are devised in accordance to these risks’ categories. However, more

quantitative risk characteristics from PRA results should be considered in risk response in addition to qualitative

risk categories so as to sufficiently evaluate the effectiveness of alternative risk treatment actions and related

decision-making.

## 2.3. MCS-based PRA methods

In the context of project management, comprehensive field experimental studies on projects are costly and infeasible and thus, simulation is commonly used as an alternative decision-making tool for empirical research in decision-support systems [39]. Some simulation-based methods have been proposed and applied to PRA, among which Monte Carlo simulation (MCS) is the most widely used. The MCS is a powerful quantitative technique in making better decisions to solve problems in which uncertainty and variability in information have distorted forecasts [40]. It can predict the general outcome of project risks given random values of input variables which falls inside a predetermined probability distribution after a sufficient number of simulation runs [41]. By using a specified range of values as inputs, MCS gives a far-reaching perspective of scenario analysis for decisionmaking. The ability of measuring the stochastic behavior of risk and generating statistics of outputs under uncertainty makes MCS a promising technique among PRA methods. As for some applications of this simulation method in PRA, Sadeghi et al. [42] proposed a fuzzy MCS framework for risk assessment and cost-range estimation in construction projects; Qazi and Simsekler [43] developed a process for prioritizing construction project risks based on the MCS that has integrated decision maker’s risk attitude, uncertainty about risks both in terms of the associated P and I ratings, and correlations across risk assessments; and similarly theoretically grounded in the framework of MCS, Qazi et al. [44] assessed and prioritized sustainability-related risks in sustainable construction projects relative to different confidence levels across the risk matrix-based exposure zones. However, a major limitation of MCS used for PRA is that the individual risks are assumed as independent factors, leading to its inability to modeling complex risk interdependencies. To improve the application of MCS to risk interdependency modeling, Wang et al. [5,13] developed a simulation model of risk interaction network based on Monte Carlo method to support the evaluation of project risk response decisions and proposed new network indices using SNA to quantify the significance of risks and risk interactions. Although their research has modeled risks in different periods of the project life cycle, there is a shortcoming that risk interdependencies in a single project period were ignored.

## 2.4. Research gaps related to the existing PRA methods and solutions to address them

Overall, the aforementioned studies indicate that sophisticated decision-support systems are being devised progressively to facilitate the analytical and statistical tools and to handle the growing complexity of the PRA, especially the interdependencies among project risks. The conventional analytical PRA methods (e.g., FSE [19], AHP [21], and TOPSIS [22]) are unable to analyze risk interdependencies, which limits their ability to tackle the complexity of risk assessment. The existing network-based analytical PRA methods can well structure and visualize cause-effect relationships among project risks via a RIN, but they are insufficient in modeling the stochastic behavior of project risk occurrence (e.g., SNA [12], ANP [26], SEM [30], and ISM [36]) and analyzing the risk propagation phenomenon in the RIN with risk loops (e.g., BBN [29], and SEM [30]). In contrast, the MCS alone fails to explicitly model complex risk interdependencies but it can well capture the stochastic behavior of risks through simulation [13,44]. Additionally, existing PRA methods usually stop at the risk evaluation phase (e.g., FSE [19], FMEA [23], and ISM [36]) with little attention given to planning and evaluating risk treatment actions, leading to less effective project risk treatment in practice.

This work tries to fill these research gaps by developing an integrated decision-support system for PRA in the context of risk interdependencies. A new MCS-based RIN model is thus proposed through combining the MCS with the ISM approach, where the ISM is responsible for analyzing cause-effect relationships among project risks and constructing a hierarchical RIN, and the stochastic behavior of project risk occurrence, the variation of RIN, and possible risk loops in the RIN are mainly tackled by improving the MCS considering complex risk interdependencies. To the best of our knowledge, the integration of ISM and MCS has never been explored in the PRA. In addition, interdependency-based risk indicators are devised on the basis of the concept of the classical P–I risk model and the risk propagation behavior in a RIN, so as to prioritize single risks and evaluate overall project risk in PRA and risk treatment phases.

## 3. Proposed decision-support system for PRA

The framework of proposed decision-support system for PRA in this work consists of three main phases: (i) development of a RIN for risk identification; (ii) development of an MCS-based RIN model for risk assessment; and (iii) planning and evaluation of risk treatment actions. Fig. 1 illustrates the three phases and their related inputs and outputs in detail. One innovation of the framework is that both direct and indirect project risk interdependencies are considered and analyzed using the ISM method for risk identification (the first step of PRA), which further provides an ISM-based RIN to be integrated with the MCS for risk assessment. Moreover, in the second phase, five risk indicators that consider risk interdependencies are devised for the comprehensive evaluation of each single risk and overall project risk. Further, this framework includes preliminary risk treatment in the third phase, which equips decision makers with more detailed information in planning and evaluation of appropriate risk treatment actions through the risk assessment results from the proposed MCS-based RIN model.

![](/api/attachments/XG2P2TKB/fulltext/images/5f33baa7ee423ba5ff9feb9e6b9ba823a218e82be95b351c901e11102c14d43f.jpg)  
Fig. 1. The framework of the proposed decision-support system for PRA.

## 3.1. Development of a project RIN

## 3.1.1. Identifying project risks and risk interdependencies

Identifying project risks should be based on relevant, appropriate, and up-to-date information which may come from previous academic research on relevant project risks, historical risk data of similar completed projects, and professional opinions on project risks from the project team and experts. In addition to the

identification of individual project risks, the interdependencies (i.e., cause-effect relationships) among project risks also need to be further identified so as to construct a RIN. Delphi-based approaches can be used to determine the contextual relationship with the type of “leads to” or “influences” between each pair of identified project risks. The interrelations among project components (e.g., work-packages, or tasks) or product components can facilitate increasing the accuracy of identifying project risk interdependencies [8]. Besides, different contexts or domains (e.g., quality, cost or schedule) of the project should be considered because their associated risks may have cause-effect relationships.

## 3.1.2. Representing a project RIN using ISM method

To develop a project RIN in a systematic way, the ISM method is adopted to present both direct and indirect cause-effect relationships among identified project risks. The major advantage of the ISM process is that it can transform unclear, poorly articulated mental models of systems into visible and well-defined models by considering all possible pairwise relations of system elements [37]. In terms of developing the contextual relationships among interrelated risks, expert opinions are usually used as the evidence along with various management techniques such as brainstorming, interviews, and questionnaire surveys [35].

First, a binary and square matrix, known as the Structural Self-Interaction Matrix (SSIM), is built to represent the identified direct project risk interdependencies. Representing the SSIM as $A = ( a _ { i j } ) _ { n \times n } , a _ { i j } = 1$ if risk i can influence risk j directly, otherwise $a _ { i j } = 0 [ 6 , 3 6 ]$ . Next, a Reachability Matrix (RM) that incorporates indirect interdependencies between risk i and risk j (through intermediate risks) is constructed from the SSIM based on the rationale in Eq. (1). The identity matrix (I<sub>n</sub>) in Eq. (1) is the n×n square matrix with 1 on the main diagonal and 0 elsewhere, represented as $I _ { n } = d i a g \left( 1 , 1 , . . . , 1 \right)$ .

$$
(A + I _ {n}) ^ {K - 1} \neq (A + I _ {n}) ^ {K} = (A + I _ {n}) ^ {K + 1} = M, \quad K = 2, 3, 4, \dots\tag{1}
$$

where $( A + I _ { n } ) ^ { K }$ denotes an intermediate RM with K intermediates, and M represents the final RM. Then, project risks can be partitioned into levels according to each risk’s reachability set (RS (R<sub>i</sub>), Eq. (2)), antecedent set (AS (R<sub>i</sub>), Eq. (3)), and intersection set (i.e., the overlap of RS (R<sub>i</sub>) and $A S \left( R _ { i } \right) )$ which are obtained from the final RM. Based on Eq. (4), if the risks for which the reachability and the intersection sets are the same, these risks are considered to occupy the top level of the ISM-based hierarchy. Once the top-level risks are determined, they are removed from the consideration, and the next top-level risks are then identified according to Eq. (4). This step

will continue until all the project risks are allocated to appropriate levels in the hierarchy. If there are risk loops, the risks within the connected loops would be in the same level. Moreover, the risks located in higher levels of the hierarchy tend to influence project objectives more directly.

$$
R S \left(R _ {i}\right) = \left\{R _ {j} \mid m _ {i j} = 1 \right\}, \quad i = 1, 2, \dots , n; j = 1, 2, \dots , n\tag{2}
$$

$$
A S \left(R _ {i}\right) = \left\{R _ {j} \mid m _ {j i} = 1 \right\}\tag{3}
$$

$$
L = \left\{R _ {i} \mid R S \left(R _ {i}\right) \cap A S \left(R _ {i}\right) = R S \left(R _ {i}\right) \right\}\tag{4}
$$

where $R _ { i }$ and $R _ { j }$ represent project risks, $m _ { i j }$ and $m _ { j i }$ denote the value of $( i , j )$ entry in the RM, and L is a set of risks determined in each level of the ISM-based hierarchy. Finally, after removing the indirect links further added in the RM and checking if there is conceptual inconsistency of risk interdependencies, the structure of an ISMbased project RIN is established, where nodes and directed edges represent the project risks and their interdependencies, respectively.

## 3.1.3. Evaluating parameters of the project RIN

From the perspective of a project RIN, the attributes of nodes (i.e., the spontaneous probability (SP) and the impact on project objectives (IO) of a risk) and edges (i.e., the transition probability (TP) between interdependent risks) constitute the parameters of the project RIN. In the development of an MCS-based RIN model, the two concepts from the classical P–I risk model, namely occurrence probability and impact of a risk, are also used. Compared with the classical P–I risk model, the occurrence probability of each risk in this work involves two aspects (i.e., SP and TP) because of the consideration of risk interdependencies. The RIN parameters – SP, TP, and IO – are essential inputs of the MCS-based RIN model to obtain the risk indicators for PRA (in Section 3.2.3). The values of SP (between 0 and 1) and IO of each risk in RIN are often provided based on similar exprojects and/or project team and expert opinions. Similarly, the edges of RIN which are recorded as 1 in the SSIM (i.e., $a _ { i j } = 1 )$ ) can also be assigned with specific values (between 0 and 1) to represent TPs. Fig. 2 shows a sample RIN and its equivalent numerical matrix, based on the evaluated values of SP and TP.

<table><tr><td></td><td>R01</td><td>R02</td><td>R03</td><td>R04</td><td>R05</td><td>R06</td><td>R07</td></tr><tr><td>R01</td><td>0.3</td><td>0.2</td><td>0.3</td><td></td><td></td><td></td><td></td></tr><tr><td>R02</td><td></td><td>0.6</td><td></td><td></td><td>0.6</td><td>0.4</td><td></td></tr><tr><td>R03</td><td></td><td></td><td>0.7</td><td></td><td>0.5</td><td></td><td></td></tr><tr><td>R04</td><td></td><td></td><td>0.2</td><td>0.2</td><td></td><td>0.4</td><td></td></tr><tr><td>R05</td><td></td><td></td><td></td><td>0.7</td><td>0.5</td><td></td><td></td></tr><tr><td>R06</td><td></td><td></td><td></td><td></td><td>0.3</td><td>0.3</td><td>0.8</td></tr><tr><td>R07</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.4</td></tr></table>

![](/api/attachments/XG2P2TKB/fulltext/images/01b4c1ebce860a045b97b35fbf195bb4b5d0fdf97ae4dbcda4d35e1b9839b3f5.jpg)

Fig. 2. An example of a RIN with evaluated values of SP and TP in a numerical matrix.

## 3.2. Development of an MCS-based RIN model

This research proposes a new MCS-based RIN model by combining the MCS method with the established ISM-based project RIN. The advantages of this model for PRA are as follows: (i) the stochastic behavior of project risk occurrence and possible risk loops in a RIN are considered and modeled; (ii) appropriate risk indicators are devised to evaluate single risk and overall project risk level in the context of risk interdependencies; and (iii) the effects of RIN parameter uncertainties on risk assessment results are examined using sensitivity analysis, which can support the double-checking and proper adjustment of the evaluated values of RIN parameters as the model inputs and further improve robustness of the model.

## 3.2.1. Modeling the stochastic behavior of project risk occurrence

Monte Carlo method is used in the simulation-based RIN model to capture the stochastic behavior of project risk occurrence and then to generate numerous risk scenarios during a project life cycle within the ISM-based project RIN. In a few existing studies [5,8,13], project risks were assumed to occur more than once during one run of a project simulation, and simulated risk frequency (may be greater than 1) was used to represent the average occurrence of a risk during the project. This research, however, from a probability perspective, focuses on investigating the occurrence of project risks as well as the resulting risk influence on project objectives. Therefore, we make the following assumption in the proposed simulation model: the status of risk occurrence (occurred or not) for each project risk in the RIN is determined once in a single simulation run.

In the Monte Carlo method, random numbers (RNs) representing occurrence probabilities of a risk are generated in the interval (0, 1) following a certain probability distribution. According to Law [39], the common probability distributions for input variables in MCS are usually divided into two types: continuous distributions (e.g., uniform, normal, exponential, triangular, and beta) and discrete distributions (e.g., Bernoulli, geometric, binomial, and Poisson). If a theoretical distribution cannot be found to fit the data adequately, a knowledge based on empirical approximation ought to be used instead [45]. To improve the traditional MCS on modeling risk stochastic behavior based on a deterministic range of probability distribution, this work proposes calculated occurrence probability (COP) regarding a risk as a dynamic threshold to evaluate a risk’s occurrence status by comparing generated RNs (following a specific probability distribution) with its COP. A risk’s COP is calculated based on the SP of the risk and TPs from other related upstream risks (varied with the dynamic change of RIN in each simulation run) using probability theory, as shown in Eq. (5).

$$
C O P _ {i, t} = 1 - \left[ \left(1 - S P _ {i}\right) \times \prod_ {k = 1} ^ {m} \left(1 - T P _ {k} ^ {i}\right) \right], m = 0, 1, 2, \dots\tag{5}
$$

where $C O P _ { i , t }$ is the calculated occurrence probability of $R _ { i }$ in the $t ^ { \mathrm { { t h } } }$ simulation run, $S P _ { i }$ represents the spontaneous probability of $R _ { i } ,$ m is the number of risks that have occurred and can influence risk $R _ { i }$ directly in the $t ^ { \mathrm { { t h } } }$ simulation run, and $T { \cal P } _ { k , t } ^ { i }$ represents the transition probability of the kth link to $R _ { i }$ in the $t ^ { \mathrm { { t h } } }$ simulation run. For example, in Fig. 2, if the risks R02, R03, and R06 have occurred in a simulation run, the COP (i.e., the threshold) of R05 would be: $C O P \left( \mathrm { R } 0 5 \right) = 1 - \{ ( 1 - 0 . 5 ) \times [ ( 1 - 0 . 6 ) \times ( 1 - 0 . 5 ) \times ( 1 - 0 . 3 ) ] \} = 0 . 9 3$ . If the risks R03 and R06 have occurred in a simulation run while R02 does not occur, the COP of R05 would be: $C O P \left( { \mathrm { R 0 5 } } \right) = 1 - \{ ( 1 -$ $0 . 5 ) \times [ ( 1 - 0 . 5 ) \times ( 1 - 0 . 3 ) ] \} = 0 . 8 2 5$

Therefore, according to Eq. (6), if a generated RN of risk $R _ { i }$ in the $t ^ { \mathrm { { t h } } }$ simulation run $( \mathrm { i . e . , } R N _ { i , t } )$ is no more than its calculated $\mathrm { C O P } \left( \mathrm { i . e . , } C O P _ { i , t } \right)$ , then $R _ { i }$ occurs in this simulation run and its occurrence status $m c _ { i , t } = 1$ otherwise $R _ { i }$ does not occur and $m c _ { i , t } = 0$

$$
m c _ {i, t} = \left\{ \begin{array}{l l} 1, & R N _ {i, t} \leq C O P _ {i, t} \\ 0, & R N _ {i, t} > C O P _ {i, t} \end{array} \right.\tag{6}
$$

## 3.2.2. Incorporating risk loops in the simulation model

If there are risk loops in a RIN, it is difficult to model such complexity and analyze risk propagation influence in the RIN using analytical PRA models. To solve this problem, a “hypothesis-test” method is designed and incorporated in the proposed simulation model, whose major steps in a single simulation run are as follows: (i) making a hypothesis on the occurrence status (occur or not) of one or more risks which can influence $R _ { i }$ within a loop; (ii) calculating the COP of $R _ { i } \left( C O P _ { i } \right)$ based on Eq. (5) and then determining the occurrence status of $R _ { i }$ using Eq. (6); (iii) proceeding with the calculation of COP of other risks in the RIN and determination of risk occurrence status until a simulation run is completed; (iv) testing whether the obtained occurrence status (i.e., occur or not) of the risks that are assumed in step (i) is the same with the null hypothesis; and (v) keeping the simulation runs with consistent results (i.e., the obtained occurrence status of hypothetical risks from a simulation run accords with the null hypothesis) and removing invalid runs (i.e., the obtained occurrence status of hypothetical risks from a simulation run is inconsistent with the null hypothesis). For instance, the RIN in Fig. 2 has a risk loop involving R03, R04, and R05. During a simulation run, the COP of the source risk R01 (COP<sub>1</sub>)

can be first determined (equal to $S P _ { 1 } )$ , and if we want to calculate $C O P _ { 3 }$ subsequently, the occurrence status of R04 should be hypothesized. After completing the simulation run across the RIN, whether the hypothetical risk R04 occurs or not can be obtained, which is then compared with the null hypothesis before keeping or removing this simulation run. The fewer risks to be hypothesized in a RIN with risk loops, the more accurate the simulation results. Fig. A.1 shows the pseudocode of the proposed MCS algorithm for modeling RIN in the proposed decision-support system. This algorithm has the flexibility to deal with a RIN with/without risk loops while modeling the stochastic behavior of risk occurrence within the RIN.

## 3.2.3. Developing risk indicators for PRA

The simulated occurrence probability (SOP) of each project risk can be obtained after the simulation of project RIN with parameters of SP and TP, representing how likely a risk is to occur based on all scenarios of risk occurrence and considering all direct and indirect risk interdependencies in the RIN. The SOP of $R _ { i } \left( S O P _ { i } \right)$ is calculated following Eq. (7).

$$
S O P _ {i} = n \left(R _ {i}\right) / N\tag{7}
$$

where N is the number of valid simulation runs, and $n ( R _ { i } )$ denotes the number of occurrence times of $R _ { i }$ in all valid simulation runs.

The simulation of project RIN will be terminated when the sum of squared difference of SOP for all risks between adjacent iteration groups is less than a threshold $h ,$ as shown in Eq. (8) [8]. The value of h is determined based on a convergence diagram (e.g., Fig. 4) during the simulation process. For example, as shown in Fig. 4, our results tend to converge around the value of $1 0 ^ { - 4 }$ for a large number of simulation runs, so the threshold h is assigned with $1 0 ^ { - 4 }$ in our simulation. Then, the appropriate number of simulation runs can be determined. $\begin{array} { r } { \sum _ { i = 1 } ^ { n } { ( \Delta S O P _ { i } ) ^ { 2 } } < h } \end{array}$ (8)

where $\Delta S O P _ { i }$ indicates the difference of simulated risk occurrence probabilities of $R _ { i }$ between adjacent iteration groups of a simulation.

In addition to each risk’s SOP, by involving the evaluated value of each risk’s IO together with its SOP, another four indicators for quantifying risk influence are proposed, namely, each risk’s simulated local influence (SLI) and simulated global influence (SGI), and a project’s total risk loss (TRL) and total risk propagation loss (TRPL).

The $S L I _ { i }$ of $R _ { i }$ can be calculated by multiplying its $S O P _ { i }$ and $I O _ { i } ,$ as shown in Eq. (9). The TRL – that is, the project risk influence at the local level – is thus calculated in Eq. (10).

$$
S L I _ {i} = S O P _ {i} \times I O _ {i}\tag{9}
$$

$$
T R L = \sum S L I _ {i}\tag{10}
$$

Considering both the direct and indirect cause-effect relationships among risks across a RIN, the $S G I _ { i }$ of $R _ { i }$ can be approximately evaluated based on the inducible influence of other risks on project objectives owing to the occurrence of $R _ { i } ,$ as presented Eq. (11). The TRPL – that is, the project total risk influence at the global level – is subsequently calculated based on Eq. (12).

$$
S G I _ {i} = \sum S L I _ {j} ^ {i} - \sum S L I _ {j} ^ {i ^ {\prime}}\tag{11}
$$

where $\sum S L I _ { j } ^ { i }$ denotes the sum of the SLI of all the risks that could be affected by $R _ { i }$ in a RIN (involving the influence from $R _ { i } ,$ other risks, and factors outside the RIN), and $\sum S L I _ { j } ^ { i ^ { \prime } }$ represents the sum of the SLI of all the risks that could be affected by $R _ { i }$ in a RIN when $R _ { i }$ does not occur (considering only the influence from other risks and factors outside the RIN).

$$
T R P L = \sum S G I _ {i}\tag{12}
$$

The proposed risk indicators concerning SOP, SLI, and SGI can be used to prioritize project risks, respectively, helping decision makers to formulate appropriate risk treatment actions targeting critical risks. TRL indicates the total risk loss of a project due to the occurrence of project risks, which can give decision makers a perception of risk local influence on an overall level of a project; while TRPL represents the risk propagation loss of all the project risks those have occurred, providing decision makers with a better understanding of risk global influence on an overall project risk level.

## 3.2.4. Examining the effects of RIN parameter uncertainties on PRA results using sensitivity analysis

There are uncertainties in the PRA when collecting the RIN parameters (i.e., SP, TP, and IO) from expert opinions, which may arise from different risk attitudes and different levels of expertise. The effects of these uncertainties on subsequent PRA results $( { \mathrm { i . e . } }$ , the SLI, and SGI of each risk, as well as the TRL and TRPL related to the overall project) from the proposed simulation model can be examined via sensitivity analysis. The results of this sensitivity analysis mainly present two aspects: (i) the sensitivity of each risk’s SLI/SGI to the variation of the values of three RIN parameters, respectively; and (ii) the model’s sensitivity in terms of a project’s TRL and

TRPL to the variation of the values of three RIN parameters, respectively. These obtained results can be used to double-check the evaluated values of the RIN parameters, especially for those unstable risks with high sensitivity values and to improve the precision of the PRA results from the simulation model.

## 3.3. Planning and evaluation of risk treatment actions

## 3.3.1. Planning risk treatment actions

Project risk treatment actions are usually formulated targeting the risks with the highest ranking or priority in terms of risk influence, which may include avoiding the risk, removing the risk source, reducing the risk probability, reducing the risk impact on project objectives, sharing the risk through contracts or insurance, retaining the risk by informed decision, and etc. [1]. However, the risk prioritization results from the classical P–I risk model without considering risk interdependencies may not well support the planning of risk treatment actions. In this study, a more structured risk treatment plan can be developed given three types of risk rankings based on the proposed risk indicators of SOP, SLI, and SGI, respectively, along with three risk categories (i.e., source risk, transition risk, and accumulation risk) in a project RIN.

Some risk treatment actions, such as reducing a risk’s SP, reducing TP between interdependent risks, and alleviating a risk’s IO can be designed for critical risks with high value of SLI. The risks with higher value of SGI can cause a wide range of risk propagation across a RIN, so the output links of such risks (belonging to source risk or transition risk) to other downstream risks should be well controlled. In addition, the risks with higher value of SOP but lower value of SP are primarily affected by their dependent risks. Thus, the influence of input links to these risks (belonging to transition risk or accumulation risk) should be mitigated in risk treatment. As a result, a series of appropriate risk treatment actions that consider the influences of risk interdependencies should be designed.

## 3.3.2. Evaluating the proposed risk treatment actions

By means of the risk assessment process conducted by the MCS-based RIN model, the risk treatment actions designed in the planning step can be evaluated by changing the values of RIN parameters (i.e., SP, TP, and IO). After using each risk treatment action, every risk’s SOP, SLI, and SGI, together with the reduced project’s TRL and TRPL can be calculated that enables the evaluation of the proposed risk treatment actions’ effectiveness.

## 3.3.3. Decision on risk treatment actions

This step can support decision makers to select the most effective risk treatment action among the proposed alternatives after evaluation. In respect to a single risk, the lower the obtained value of its SOP, SLI, and SGI, the better the performance of a risk treatment action; while from a whole project RIN perspective, the higher of the reduced value of project’s TRL and TRPL, the better the efficacy of a risk treatment action. Therefore, the most effective risk treatment action is the one with the highest value of both reduced project’s TRL and TRPL while the lowest value of SOP, SLI, and SGI for a majority of risks.

## 4. Applications and results

In this section, our proposed decision-support system based on the MCS-based RIN model is applied to two case studies. The first sample project (from [5]) is related to employing artificial intelligence technology for predicting medical items, which belongs to a logistics and healthcare program. This project has identified a RIN (with risk loops) involving 16 risks and 26 direct risk interdependencies. The second sample project (from [3]) is a high-speed railway project in Turkey through an Engineering, Procurement and Construction agreement. Its RIN (without risk loops) has 91 risks (including a top risk: the project failure) and 111 direct risk interdependencies. Due to the length of this paper, the results of all three phases of the proposed decision-support system are displayed in detail using the first sample project (in Sections 4.1–4.3), while the second sample project is used only for the evaluation of risk treatment actions (in Section 4.3). The results of these two different sample projects demonstrate the flexibility and effectiveness of the proposed MCS-based RIN model for PRA. The simulation model was implemented in MATLAB R2017b on a Windows 10 PC with Intel® Core™ i7-6700 CPU at 3.40GHz and 16.0 GB of RAM.

## 4.1. RIN modeling

The risk-related data for the first sample project, including identification of project risks and possible direct interdependencies between each pair of risks, as well as the evaluated values of project RIN parameters (i.e., SP, TP, and IO (denoted by cost in this case study) for each risk), were obtained directly from [5]. These data were originally collected by a primary project member who oversaw the project plan, implementation, and risk management. Then, a two-level hierarchical structure of an ISM-based project RIN was established based on Eq. (1)–(4). Table 1 shows the identified project risks and evaluated values of SP and IO for each risk. Fig. 3 presents the developed ISM-based project RIN with evaluated TP for each directed link (i.e., the direct risk

interdependency), where all risk loops (e.g., the closed loop “R09, R08, R12, R13, R02, R09”) are in the top level (i.e., L1). R01, located in the bottom level of the hierarchy, is a source risk of the project without any influence from other project risks.

Table 1. Project risks with their evaluated values of SP and IO, respectively (from Wang et al. [5]).

<table><tr><td>Risk No.</td><td>Risk description</td><td> $SP_i$ </td><td> $IO_i$  ($100)</td></tr><tr><td>R01</td><td>Language problems and cultural conflicts</td><td>0.8</td><td>1</td></tr><tr><td>R02</td><td>Communication problems between the teams</td><td>0.4</td><td>2</td></tr><tr><td>R03</td><td>Unclear milestone and technical route</td><td>0.7</td><td>2.5</td></tr><tr><td>R04</td><td>Lack of professional medical knowledge</td><td>0.6</td><td>1</td></tr><tr><td>R05</td><td>Poor analysis of the factors regarding medical items</td><td>0.3</td><td>0.5</td></tr><tr><td>R06</td><td>Poor selection of the medical items</td><td>0.4</td><td>1.8</td></tr><tr><td>R07</td><td>Poor selection of the existing database</td><td>0.4</td><td>1</td></tr><tr><td>R08</td><td>Building and training the model repeatedly</td><td>0.3</td><td>3</td></tr><tr><td>R09</td><td>Interfaces problem among the software platforms of different terms</td><td>0.6</td><td>2</td></tr><tr><td>R10</td><td>Poor quality of the data from hospital and logistics company</td><td>0.2</td><td>1.4</td></tr><tr><td>R11</td><td>Poor effectiveness and efficiency of the model</td><td>0.2</td><td>4</td></tr><tr><td>R12</td><td>Too much investigation</td><td>0.1</td><td>2</td></tr><tr><td>R13</td><td>Tense partnerships among the teams</td><td>0.4</td><td>1.5</td></tr><tr><td>R14</td><td>Too many tests on the model</td><td>0.2</td><td>2</td></tr><tr><td>R15</td><td>Project scope spread</td><td>0.4</td><td>1.6</td></tr><tr><td>R16</td><td>Too much rework for the team in charge of the modeling</td><td>0.4</td><td>3</td></tr></table>

![](/api/attachments/XG2P2TKB/fulltext/images/0e04870b27c89fd5abe1738d24880a26d54c0456f77e58d3f27466bfb05ccd33.jpg)  
Fig. 3. The ISM-based RIN with 16 risks and 26 direct risk interdependencies of the first sample project.

4.2. Risk assessment results based on the proposed simulation-based model

## 4.2.1. Assessment results of SOP, SLI, and SGI for each risk

In the MCS method, to model the stochastic behavior of project risk occurrence based on expert judgements, rand (0, 1) – a function of generating RNs of risk occurrence probabilities following a uniform probability distribution in the interval (0, 1) – was set, and through comparing the RNs regarding each risk with its COP using Eq. (6), whether a risk occurs or not in a single simulation run was determined subsequently. Other types of probability distributions (e.g., normal, triangular, and beta) could also be used, but appropriate parameters need to be first defined accordingly to make sure that the stochastic behavior of the occurrence of each risk is modeled given a dynamic threshold (i.e., the COP) of the risk. Since the type of probability distribution will not affect the results of this research, the uniform probability distribution was used owing to its simplicity of operation. In the simulation, we started the number of simulation runs from 1000 in the first iteration group and increased by 1000 in later iteration groups until 300000 simulation runs in the $3 0 0 ^ { \mathrm { t h } }$ iteration group. Eq. (8) was used to terminate the simulation. According to the convergence diagram shown in Fig. 4, the sum of squared differences of SOP for all project risks between adjacent iteration groups in this simulation tends to converge around 10<sup>-4</sup>, so the $1 0 ^ { - 4 }$ threshold h in Eq. (8) was set to be $1 0 ^ { - 4 }$ . For obtaining more stable simulation results and considering the statistical convenience, 300000 simulation runs were conducted to model all scenarios of the RIN.

![](/api/attachments/XG2P2TKB/fulltext/images/ad4cf94ab54ce5d12a44362f0de032d749a9b5161457d2e93ab7d8cac1d24a0e.jpg)  
Fig. 4. Convergence diagram of the proposed simulation model used in the first sample project.

Based on Eq. (7), (9) and (11), the values of SOP, SLI, and SGI of each risk, while considering risk interdependencies, were calculated. Meanwhile, the project risks were prioritized by the following six different indicators as presented in Table 2: three from the proposed simulation model $( \mathrm { i . e . , } S O P _ { i } , S L I _ { i } ,$ and $S G I _ { i } ) ;$ ; two from the classical P–I risk model $( \mathrm { i } . \mathrm { e } . , S P _ { i } ,$ and risk criticality $( R C _ { i } )$ – the product of $S P _ { i }$ and $I O _ { i } )$ ), and one from [5] $( \mathrm { i } . \mathsf { e } . , S _ { i j } )$

In respect to risk occurrence probability, R14, R05 and R16 have lower value of SP, while in terms of SOP, they are top ranked with the highest values, indicating that although this kind of risks are unlikely to occur spontaneously, they are highly affected by others due to direct and indirect cause-effect relationships. Some risks occurrence probabilities may be evaluated as similar (e.g., R03 and R15) using the classical P–I risk model (SP<sub>i</sub>) and the proposed simulation model (SOP<sub>i</sub>), however, they are still underestimated to some extent. Except for the source risk R01, all the other risks have increased occurrence probabilities calculated by the proposed method, demonstrating that risk interdependencies can increase risk occurrence probability.

<table><tr><td rowspan="3">Ranking</td><td colspan="6">From the proposed MCS-based RIN model</td><td colspan="4">From the classical P-I risk model</td><td rowspan="2" colspan="2">From the indicator in [5]  $S_{ij}$  ($100)</td></tr><tr><td colspan="2"> $SOP_i$ </td><td colspan="2"> $SLI_i$  ($100)</td><td colspan="2"> $SGI_i$  ($100)</td><td colspan="2"> $SP_i$ </td><td colspan="2"> $RC_i$  ($100)</td></tr><tr><td>Risk No.</td><td>Value</td><td>Risk No.</td><td>Value</td><td>Risk No.</td><td>Value</td><td>Risk No.</td><td>Value</td><td>Risk No.</td><td>Value</td><td>Risk No.</td><td>Value</td></tr><tr><td>1</td><td>R14</td><td>0.895</td><td>R11</td><td>2.950</td><td>R05</td><td>18.574</td><td>R01</td><td>0.8</td><td>R03</td><td>1.75</td><td>R03</td><td>5.18</td></tr><tr><td>2</td><td>R05</td><td>0.853</td><td>R16</td><td>2.516</td><td>R14</td><td>18.041</td><td>R03</td><td>0.7</td><td>R16</td><td>1.2</td><td>R06</td><td>3.23</td></tr><tr><td>3</td><td>R16</td><td>0.839</td><td>R08</td><td>2.345</td><td>R07</td><td>17.256</td><td>R04</td><td>0.6</td><td>R09</td><td>1.2</td><td>R02</td><td>2.24</td></tr><tr><td>4</td><td>R03</td><td>0.830</td><td>R03</td><td>2.074</td><td>R13</td><td>17.185</td><td>R09</td><td>0.6</td><td>R08</td><td>0.9</td><td>R04</td><td>2.22</td></tr><tr><td>5</td><td>R13</td><td>0.825</td><td>R14</td><td>1.791</td><td>R01</td><td>17.095</td><td>R02</td><td>0.4</td><td>R01</td><td>0.8</td><td>R01</td><td>2.15</td></tr><tr><td>6</td><td>R07</td><td>0.811</td><td>R02</td><td>1.321</td><td>R03</td><td>16.322</td><td>R06</td><td>0.4</td><td>R02</td><td>0.8</td><td>R09</td><td>1.74</td></tr><tr><td>7</td><td>R01</td><td>0.799</td><td>R06</td><td>1.250</td><td>R16</td><td>16.243</td><td>R07</td><td>0.4</td><td>R11</td><td>0.8</td><td>R07</td><td>1.55</td></tr><tr><td>8</td><td>R08</td><td>0.782</td><td>R09</td><td>1.246</td><td>R10</td><td>15.711</td><td>R13</td><td>0.4</td><td>R06</td><td>0.72</td><td>R08</td><td>1.43</td></tr><tr><td>9</td><td>R11</td><td>0.737</td><td>R13</td><td>1.238</td><td>R08</td><td>15.546</td><td>R15</td><td>0.4</td><td>R15</td><td>0.64</td><td>R05</td><td>1.41</td></tr><tr><td>10</td><td>R10</td><td>0.736</td><td>R10</td><td>1.031</td><td>R06</td><td>14.597</td><td>R16</td><td>0.4</td><td>R13</td><td>0.6</td><td>R15</td><td>1.16</td></tr><tr><td>11</td><td>R06</td><td>0.694</td><td>R15</td><td>0.879</td><td>R11</td><td>14.049</td><td>R05</td><td>0.3</td><td>R04</td><td>0.6</td><td>R13</td><td>1.05</td></tr><tr><td>12</td><td>R02</td><td>0.661</td><td>R07</td><td>0.811</td><td>R04</td><td>13.676</td><td>R08</td><td>0.3</td><td>R07</td><td>0.4</td><td>R16</td><td>0.86</td></tr><tr><td>13</td><td>R04</td><td>0.651</td><td>R01</td><td>0.799</td><td>R02</td><td>13.442</td><td>R10</td><td>0.2</td><td>R14</td><td>0.4</td><td>R11</td><td>0.70</td></tr><tr><td>14</td><td>R09</td><td>0.623</td><td>R12</td><td>0.746</td><td>R09</td><td>12.730</td><td>R11</td><td>0.2</td><td>R10</td><td>0.28</td><td>R10</td><td>0.59</td></tr><tr><td>15</td><td>R15</td><td>0.549</td><td>R04</td><td>0.651</td><td>R15</td><td>11.423</td><td>R14</td><td>0.2</td><td>R12</td><td>0.2</td><td>R14</td><td>0.31</td></tr><tr><td>16</td><td>R12</td><td>0.373</td><td>R05</td><td>0.427</td><td>R12</td><td>8.131</td><td>R12</td><td>0.1</td><td>R05</td><td>0.15</td><td>R12</td><td>0.22</td></tr></table>

From the aspect of risk influence, the SLI of each risk (excluding R01) is higher than its evaluated RC from the classical P–I risk model due to the different values of risk occurrence probability, indicating that the risk propagation across the RIN has amplified the risk influence on project objectives. The SGI of a risk reflects to what extent the occurrence of this risk can increase other risks’ influence on project objectives. Some risks have lower SLI, but their SGI may be higher, such as R05 and R07. In Wang et al. [5], the significance indicator $S _ { i j }$ (developed based on weighted edge betweenness in a directed network) for evaluating risks was calculated based on the SP of each risk ignoring risk interdependencies, resulting in very different risk rankings compared with using the indicator $S L I _ { i }$

Overall, the project risk prioritization results have changed after using the proposed MCS-based RIN model. For example, R03 was considered to be the most critical risk according to both the indicators $R C _ { i }$ and $S _ { i j } ,$ however, the one with the highest SLI is R11, and R05 has the highest SGI. R08 and R09 were evaluated with similar values both from the indicators $R C _ { i }$ and $S _ { i j } .$ . While following the indicators $S L I _ { i }$ and $S G I _ { i } ,$ R08 is ranked above R09, and the relative gap between them has widened.

Further, Spearman rank correlation test was conducted to statistically examine the correlations between these six PRA indicators. As shown in Table 3, $S O P _ { i }$ and $S G I _ { i }$ have a significant positive correlation, and so are the correlation between $S L I _ { i }$ and $R C _ { i } , S P _ { i }$ and $R C _ { i } ,$ as well as $S P _ { i }$ and $S _ { i j } ,$ which means that project risks evaluated by these pairs of risk indicators have similar risk rankings, respectively. Owing to the risk indicators $S O P _ { i } , S L I _ { i } ,$ and SGI<sub>i</sub> proposed in our MCS-based RIN model are all developed considering risk interdependencies, their correlations to the indicators $S P _ { i } , R C _ { i } ,$ and $S _ { i j }$ are proved to be very weak. One exception to this is the significant positive correlation between $S L I _ { i }$ and $R C _ { i } ,$ which is because these two indicators both use the same value of risk’s IO in their calculation. The results of Spearman rank correlation test reinforce the necessity of incorporating risk interdependencies in PRA.

Table 3. Spearman rank correlation coefficients for six risk indicators in the first sample project.

<table><tr><td>Risk indicator</td><td> $SOP_i$ </td><td> $SLI_i$ </td><td> $SGI_i$ </td><td> $SP_i$ </td><td> $RC_i$ </td></tr><tr><td> $SOP_i$ </td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td> $SLI_i$ </td><td>0.262</td><td>-</td><td></td><td></td><td></td></tr><tr><td> $SGI_i$ </td><td>0.929**</td><td>-0.024</td><td>-</td><td></td><td></td></tr><tr><td> $SP_i$ </td><td>-0.017</td><td>-0.108</td><td>0.021</td><td>-</td><td></td></tr><tr><td> $RC_i$ </td><td>0.006</td><td>0.681**</td><td>-0.219</td><td>0.568*</td><td>-</td></tr><tr><td> $S_{ij}$ </td><td>-0.088</td><td>-0.029</td><td>-0.038</td><td>0.798**</td><td>0.492</td></tr><tr><td colspan="6">Notes: ** Correlation is significant at the 0.01 level (2-tailed);* Correlation is significant at the 0.05 level (2-tailed).</td></tr></table>

## 4.2.2. Assessment results of project level PRA indicators: TRL and TRPL

To provide decision makers with a clearer perception of how the project’s TRL will be distributed and its expected value, we analyzed all scenarios of the project RIN from the simulation and obtained the probability distribution of TRL. The results of probability density function (PDF) and cumulative distribution function (CDF) with respect to the TRL are presented in Fig. 5. Based on the histogram of PDF, the potential TRL in the six intervals of \$2222–\$2323, \$2525–\$2626, \$2626–\$2727, \$2323–\$2424, \$2222–\$2323, and \$2727–\$2828 are more likely to occur (in descending order) than other intervals displayed, each of which has a probability greater than 8%. In addition, the expected value of the TRL was evaluated as \$2207 based on Eq. (10). From the CDF curve, the TRL in the interval of \$1500–\$2820 accounts for around 79% of all the possible project RIN scenarios, indicating that the project loss due to occurrence of project risks is very likely to distribute in this interval.

![](/api/attachments/XG2P2TKB/fulltext/images/2fb03a9f44fd33ab0dedbbdc464617c96bfa443194e702aeca009af66592e925.jpg)  
Fig. 5. Probability distribution of the TRL for the first sample project.

As shown in Fig. 6, among the RIN scenarios causing the TRL in the interval of \$1500–\$2820, R14 has the highest value of SOP (i.e., 0.74) while R12 has the lowest value (i.e., 0.28), and most of the risks have the SOP greater than 0.5 except for R09 (i.e., 0.48), R12, and R15 (i.e., 0.42). The TRL in the intervals of \$0–\$1500 and \$2820–\$3030 account for about only 10% and 11% of all the possible RIN scenarios, respectively (in Fig. 5), and all the risks in terms of these two TRL intervals have similar and very low SOP (less than 0.11) (in Fig. 6).

![](/api/attachments/XG2P2TKB/fulltext/images/4c81d3895d1c89c99c10b47d59cc17e5c9296783c19a9abc8a5fd1a27b800f46.jpg)  
Fig. 6. The risk’s SOP in three TRL intervals (less than 15.0 (\$100), between 15.0 and 28.2 (\$100), and greater than 28.2 (\$100)).

Moreover, the expected value of the TRPL was calculated based on Eq. (12) with the numerical value of \$24002. The expected values of TRL and TRPL can be used to represent the overall project risk level considering risk interdependencies from a local and a global perspective, respectively, which provide decision makers with the risk perception of an overall project before risk treatment.

## 4.2.3. Examination of the effects of RIN parameter uncertainties on PRA results

Sensitivity analyses were conducted to examine how the uncertainties in the evaluated values of RIN parameters (i.e., each risk’s SP and IO, and TPs between each pair of direct interdependent risks) can affect the obtained values of each risk’s SLI and SGI, as well as the TRL and TRPL regarding the overall project. Threelevel (pessimistic, most likely, and optimistic) values for SP, IO, and TP were separately used as the new input data sets of the proposed simulation model, and the corresponding PRA results were obtained. The values of SP and IO in Table 1, and the values of TP in Fig. 3 were regarded as the most likely values of these RIN parameters. Due to a lack of the project information needed to generate appropriate pessimistic and optimistic values in terms of SP, IO, and TP, respectively, rational assumptions on these values were made in order to demonstrate the function of sensitivity analyses integrated in the PRA model.

Using radar diagrams, Fig. 7 depicts the sensitivity of each risk’s SLI/SGI to the variation of the values (i.e., the three-level values) of RIN parameters (i.e., SP, TP, and IO), respectively. According to Fig. 7(a), all the risks SLI is the most sensitive to the variation of IO except for R12, and R11 is the most sensitive and unstable risk in terms of the variations of all RIN parameter values. From Fig. 7(b), a number of risks have similar and high sensitivity of SGL, which shows their SGL could be highly affected by the variation of evaluated values of SP, TP, and IO, respectively. For example, the SGI of R01, R04, R09 and R15 are more sensitive to uncertainties of evaluated values of SP, while for R10, R11, and R12, their SGI become more sensitive to variations of evaluated values of TP. In addition, the uncertainties in the evaluated values of IO are more likely to influence the SGI of R05, R07, R14 and R16.

![](/api/attachments/XG2P2TKB/fulltext/images/9dac0dd0101a1babd5f867c899636f928ccbf5b56acb420a54c9cac1c741e684.jpg)  
(a)

![](/api/attachments/XG2P2TKB/fulltext/images/9805c93979a12c9febc77b62296f962182119ccb8c415491d1325b1f48d00198.jpg)  
(b)  
Fig. 7. Sensitivity radar diagrams of the first sample project related to: (a) SLI values (\$100), and (b) SGI values (\$100).

The sensitivities of the proposed simulation model in respect to project’s TRL and TRPL to the variation of model inputs (e.g. SP, TP, and IO) were also evaluated, respectively. The performance of the first sample project for the most likely scenario was: \$2207 for the TRL, and \$24002 for the TRPL. Here, the model sensitivity in terms of a RIN parameter is defined as the percent loss of project performance compared to the performance of the most likely scenario due to changing the values of one RIN parameter from the optimistic to the pessimistic scenario values. For example, when the values of SP increase from the optimistic scenario to the pessimistic scenario values, the project’s TRL increases from \$1255 (optimistic scenario) to \$2604 (pessimistic scenario). The \$1349 change in the project’s TRL (2604 - 1255 = \$1349) represents a 61% model sensitivity (1349/2207 = 0.61) for the SP parameter. The effect of variation in IO on the project’s TRL (model sensitivity: 100%) and TRPL (100%) is the highest, followed by that of variation in SP (61% related to TRL; and 95% related to TRPL) and TP (49% related to TRL; and 88% related to TRPL). The results also present that the project’s TRPL are more affected by the variation of SP and TP than the project’s TRL.

The above sensitivity analyses results can supplement the proposed simulation model for PRA and help decision makers to double-check the evaluated values of RIN parameters (the model inputs) especially for those unstable risks with high sensitivity values. For this case study, the evaluated model input values particularly related to R11, evaluated SP values of R01, R04, R09 and R15, evaluated TP values for R10 and R12, and evaluated IO values for all risks should be paid more attention to during the PRA process for the sake of getting more accurate model output values.

## 4.3. Planning and evaluation of the project risk treatment actions

Based on the obtained PRA results from the proposed MCS-based RIN model, a series of appropriate risk treatment actions can be formulated. To support demonstrating the superiority of our proposed model from the aspect of risk treatment effectiveness in Section 4.4, the performance of four risk treatment actions (in which one was devised based on the PRA results from the proposed model, and the other three were devised based on the results from previous PRA methods, respectively) were evaluated and compared. In this paper, reducing the probability of critical risks is the major concern for risk treatment. It was assumed that a risk’s SP can be reduced to 0 and the cause-effect relationship between two risks can be completely cut off (i.e., TP can be reduced to 0) when devising risk treatment actions.

For the first sample project, Actions 1–4 were formulated as follows. Action 1 was made based on the PRA results from the classical P–I risk model. As shown in Table 2, R03 and R16 are the top-two critical risks with high RC value, so Action 1 aims to mitigate the SP of R03 and R16 (i.e., SP(R03)=0, and SP(R16)=0), which only acts on critical individual project risks. Action 2 was proposed based on the PRA results from the method of quantifying risk significance in [13]. R03 and R06 were considered as the most critical risks, and the cause-effect relationship between R06 and R05 as well as that between R05 and R10 are highly ranked based on their significance values. Accordingly, Action 2 was developed to mitigate the SP of R03 and R06, together with cutting off the links from R06 to R05 and from R05 to R10 (i.e., SP(R03)=0, SP(R06)=0, TP(R06→R05)=0, and TP(R05→R10)=0). Action 2 focuses on reducing the influence of risk interdependencies, which could be done by setting up an inspection team to make sure appropriate selection and analysis of medical items in practice. Action 3 was formulated based on the PRA results from the method of quantifying risk significance in [5] where the top two critical risks are R03 and R06 (similar to Action 2), and the causal relationship between R03 and R06 was found to be the most important, followed by the interaction between R06 and R05. Therefore, the Action 3

was devised as minimizing the SP of R03 and R06 and breaking off the link from R03 to R06 as well as that from R06 to R05 (i.e., SP(R03)=0, SP(R06)=0, TP(R03→R06)=0, and TP(R06→R05)=0). Action 4 was formulated according to the PRA results from the proposed MCS-based RIN model. As presented in Table 2, R11 and R16 (as transition risks) were evaluated as the top-two risks with high SLI, so their SP and significant TP from other interrelated risks should be mitigated. R03 has relatively high SLI due to highest rank of its SP, and the SP of R03 should also be reduced by risk treatment. In addition, R05 and R14 (as transition risks) are highly ranked both based on SOP and SGI, indicating that they tend to largely affect, and be affected by, other related risks through risk interdependencies, although they have relatively lower SP. In this regard, several key risk interdependencies related to R05 and R14 should be mitigated in risk treatment. Therefore, Action 4 was devised as reducing the SP of R11, R16 and R03 (i.e., SP(R11)=0, SP(R16)=0, and SP(R03)=0), together with cutting off some of key risk interdependencies (i.e., TP(R08→R16)=0, TP(R10→R11)=0, TP(R05→R10)=0, TP(R14→ R16)=0, TP(R08→R14)=0, and TP(R06→R05)=0)). Apart from mitigating critical project risks, Action 4 focuses more on the control of risk propagation across the project RIN, and some measures in practice for this sample project can be, for example, setting a threshold earlier to evaluate a product’s performance, or raising quality standards of the data collection.

Fig. 8 illustrates the residual values of SOP, SLI, and SGI of each risk in the first sample project after conducting different risk treatment actions (i.e., Actions 1–4), including the project risk conditions before the risk treatment (no action). The values of SOP, SLI, and SGI for most risks after conducting Action 4 are lower than those obtained from the implementation of other three risk treatment actions. In Fig. 8 (a) and (b), the SOP and SLI regarding R06, R07 and R08, after using Action 2 and Action 3, respectively, are lower than those obtained from the implementation of Action 4, and the same situation with the SGI of R06 in Fig. 8 (c). The main reason is that the SP of R06 was reduced to 0 in Action 2 and Action 3. From the perspective of the reduced overall project risk, Table 4 denotes the performance of Actions 1–4 through “reduced project’s TRL” and “reduced project’s TRPL”. The results show that Action 4 can help minimize the project’s TRL and TRPL, followed by Action 2, Action 3, and Action 1. Overall, Action 4 performs best among these four risk treatment actions and can be selected to mitigate risks of the first sample project.

In the context of the second sample project, different risk treatment actions were devised based on the PRA results from the classical P–I risk model (Action 1), FSE method (Action 2), Fuzzy Bayesian belief network (FBBN) method (Action 3), and the proposed MCS-based RIN model (Action 4). Comparison results of the performance of Actions 1–4 are shown in Table 5. By using Action 4, the SOP of the top risk (the project failure) in the project RIN can be reduced to 0, and the ratings of project’s TRL and TRPL can be minimized. Thus, Action 4 outperforms the other three risk treatment actions.

![](/api/attachments/XG2P2TKB/fulltext/images/e57548880323c79bb4d6d909c6478c4ac5c54e4eff2af45021ecd8aa101a9aac.jpg)

![](/api/attachments/XG2P2TKB/fulltext/images/01aa3f42086bba9a220e13a215ef327309051c150ff54ec7f0772ba85c8c1e59.jpg)

![](/api/attachments/XG2P2TKB/fulltext/images/e098eb7a1315d9bfd1babe1b72f6d0396e69d3ce8e5bbeab4f22aa7d03c44cde.jpg)  
Fig. 8. Comparison of (a) the SOP, (b) the SLI, and (c) the SGI of risks in the first sample project after different risk treatment actions.

Table 4. The performance of different risk treatment actions in the first sample project.

<table><tr><td>Risk treatment action</td><td>Reduced value of project&#x27;s TRL after risk treatment</td><td>Reduced value of project&#x27;s TRPL after risk treatment</td></tr><tr><td>Action 1 (Classical P–I risk model)</td><td>$217</td><td>$3711</td></tr><tr><td>Action 2 ([13])</td><td>$489</td><td>$9274</td></tr><tr><td>Action 3 ([5])</td><td>$412</td><td>$7978</td></tr><tr><td>Action 4 (Proposed model)</td><td>$826</td><td>$14717</td></tr></table>

Table 5. The performance of different risk treatment actions in the second sample project.

<table><tr><td>Risk treatment action</td><td>SOP of the project failure</td><td>Reduced rating of project&#x27;s TRL after risk treatment</td><td>Reduced rating of project&#x27;s TRPL after risk treatment</td></tr><tr><td>Action 1 (Classical P–I risk model)</td><td>0.926</td><td>6.941</td><td>35.413</td></tr><tr><td>Action 2 (FSE method [3])</td><td>0.893</td><td>5.523</td><td>30.614</td></tr><tr><td>Action 3 (FBBN method [3])</td><td>0.892</td><td>6.360</td><td>38.228</td></tr><tr><td>Action 4 (Proposed model)</td><td>0</td><td>8.228</td><td>131.780</td></tr></table>

## 5. Discussion

Risks in a project usually have cause-effect relationships among each other, and independent risks seldom exist [36]. As projects become more complicated in ever-changing environments, the complexity of project risk interdependencies increases as well, making the PRA an information-intensive process in project management. The proposed MCS-based RIN model embedded in an integrated decision-support system for PRA can facilitate a structured and systematic risk assessment of projects with complex risk interdependencies and also allow decision makers to evaluate the effectiveness of alternative risk treatment actions. The results obtained in the previous applications show the model’s flexibility and validity in risk management for large and complex projects. The proposed risk indicators can provide decision makers with useful information for understanding project risks (each single risk and the overall project risk) at both local and global scales in a project RIN.

Compared with the classical P–I risk model, the proposed process demonstrates that some risk ratings would inevitably be underestimated if the effects of risk interdependencies are exclusively ignored. This is also in line with the results from previous studies on project risk management when considering risk interdependencies [3,7,8,18]. As shown in Table 2, the positive deviation value between $S O P _ { i }$ (from the proposed model) and $S P _ { i }$ (from classical P–I risk model) as well as that between SLI<sub>i</sub> (from the proposed model) and RC<sub>i</sub> (from classical P–I risk model) reflect the effects of risk propagation across the project RIN on PRA results, except for the source risk R01.

In addition, focusing on the effects of risk’s SP variation on project risk loss for the first sample project, the sensitivity of our proposed model was compared with that of classical P–I risk model from the following two aspects. Firstly, for the variation of SP (from optimistic scenario to pessimistic scenario values) of all project risks, there is a 61% sensitivity of our proposed model (calculated in Section 4.2.3), which is much lower than the classical P–I risk model’s sensitivity (96%, calculated by $( 1 6 6 9 - 5 7 2 ) / 1 1 4 4 = 0 . 9 6 )$ . Secondly, while for the variation of SP of each individual risk, the comparison of sensitivity results for these two models are shown in Fig. 9, indicating that the proposed model is less sensitive to the variation of SP of all the risks only except for that of R13. Therefore, these results reflects that the proposed MCS-based RIN model is more stable than the classical P–I risk model in conducting PRA.

![](/api/attachments/XG2P2TKB/fulltext/images/cded70262a28e23af5091de0badd7d9c1dbfd3fde25e8be3612e19eb474857eb.jpg)  
Fig. 9. Comparison of sensitivity results for these two models due to the variation of each risk’s SP in the first sample project.

This study makes a methodological contribution to the academic research on project risk management and in particular, on risk assessment. A hybrid method of ISM and MCS is first explored and extended to support an effective PRA in the context of complex risk interdependencies, and the MCS-based RIN model is therefore developed. Major superiorities of the proposed method compared with existing PRA methods such as FSE [19],

BBN-based methods [3,28], SEM [30], and SNA [12] are as follows. Firstly, apart from involving the identification of cause-effect relationships among risks in the proposed decision-support system for PRA, more aspects of the RIN complexity are taken into account, including risk loops, and dynamic change of RIN due to the stochastic behavior of project risks. Secondly, by means of the theoretical framework of MCS (i.e., a robust technique for generating and evaluating future scenarios), the proposed method is capable of modeling all possible risk scenarios within a RIN. The proposed interdependency-based risk indicators (i.e., each risk’s SOP, SLI, and SGI, as well as a project’s TRL and TRPL) are calculated considering all the possible RIN scenarios through simulation, which helps in advancing the accuracy of PRA results. Thirdly, the proposed MCS-based RIN model can be further used to quantitatively evaluate the performance of alternative risk treatment actions, which provides an integrated platform for sufficient utilization of the obtained PRA results by risk treatment. The performance results of different risk treatment actions in the two case studies (as shown in Table 4 and Table 5, respectively) also reflect that our proposed model is more effective than other benchmark methods (e.g., classica P–I risk model, FSE, and FBBN) for PRA and planning of risk treatment actions. Moreover, although this paper focuses on the project risks that can cause negative effects, the proposed process is also applicable to modeling and assessing positive risks.

There are a number of major managerial implications of our work. First, practitioners can have more comprehensive perception of project risk from the PRA results obtained using the MCS-based RIN model. Considering risk interdependencies, the proposed indicators to assess each risk, i.e., SOP, SLI, and SGI, can be used to determine risk priorities. In addition, the indicators to assess the overall project risk, i.e., TRL and TRPL, can provide practitioners with the project risk loss from local and global scales within a project RIN. A series of appropriate risk treatment actions can be formulated and evaluated through the proposed decision-support system. Then, the proposed model considers the two concepts of risk’s probability and impact existing in the classical P–I risk model, which are widely used by practitioners in managing project risks, so that all practitioners can engage their knowledge and experience in the PRA process. As a result, our proposed method facilitates mitigating the gap between theory and practice of the PRA. Further, the proposed decision-support system for PRA can be readily operationalized in practice by simulation, which outperforms many existing analytical PRA methods which mainly need complicated calculations (e.g., ANP [26], and BBN [28]).

Additionally, the proposed process has high universality and flexibility and can be applied to projects in different fields (e.g., software, civil, or business), and even to large and complex projects. Furthermore, it can be used at the commencement stage of a project when there is high uncertainty about project risks and can update periodically to reflect risk conditions of the project over time when new risk information is captured. Project risk scenarios based on different risk attitudes of decision makers can also be obtained to support formulating appropriate risk treatment actions.

## 6. Conclusion

To perform better PRA and risk treatment, taking the interdependencies among project risks into account is important. This study has explored an intelligent simulation-based decision-support system for assessing project risks and facilitating risk treatment in the context of risk interdependencies, making both academic and practical contributions to the field of project risk management. The novelty of this work is that a new MCS-based RIN model, as part of the proposed decision-support system, was developed by integrating the ISM method and MCS for modeling the stochastic behavior of project risk occurrence in a RIN with loops and analyzing the effects of risk propagation across the RIN. Interdependency-based risk indicators were introduced to support decision makers in prioritizing single risks and evaluating the overall project risk. The effects of uncertainties in the model’s inputs (i.e., the RIN parameters) on PRA results were examined using sensitivity analysis to further improve the robustness of decision-support system in practical use. In addition, the performance of alternative risk treatment actions can be evaluated in the integrated decision-support system. Two application cases of the proposed decision-support system were provided in this work, and the results demonstrated the necessity of considering risk interdependencies in PRA and also verified the effectiveness of the proposed MCS-based RIN model for the PRA. In practice, the framework of the proposed decision-support system for PRA allows decision makers to use their professional experience and implement their strategies in an easy and transparent manner.

Despite its utility, there are two limitations to this study: (i) the proposed MCS-based RIN model is not applicable to simultaneously modeling and assessing both positive and negative connotations of risks within a project RIN; and (ii) in the planning of risk treatment actions in case studies, it was assumed that a risk’s SP and the TP between two interrelated risks can be reduced to 0, so that the control of risk impact was not considered in order to simplify the analysis process. Potential extensions of this research in future work can be: (i) including

the dynamic behavior of project RIN throughout a project life cycle in the current simulation model, as projects are time-related dynamic systems, and project risks and their interdependencies may vary with project phases; and (ii) optimizing project risk treatment decisions by considering additional parameters such as project budget, cost of risk treatment, and risk positions in a network.

## Appendix

Fig. A.1 presents the proposed MCS algorithm for modeling a project RIN in the proposed decision-support system for PRA.

![](/api/attachments/XG2P2TKB/fulltext/images/a0a93501b36a43669068698183d91d7431db3ead9a828e13fa37e50d3ef5d854.jpg)  
Fig. A.1. The proposed MCS algorithm for modeling a project RIN.

## Declarations of interest: none

## Acknowledgements

The work in this paper is supported by a research stipend from the UNSW. We really appreciate Shuo Yang for his contribution in conceiving the simulation algorithm of this work. We are also very grateful to the editor and anonymous referees for their valuable comments and suggestions.

## References

[1] BSI, International Standard ISO 31000: Risk Management-Guildelines, (2018).

[2] PMI, A Guide to the Project Management Body of Knowledge (PMBOK), (2017).

[3] L. Guan, Q. Liu, A. Abbasi, M.J. Ryan, Developing a comprehensive risk assessment model based on

fuzzy Bayesian belief network (FBBN), J. Civ. Eng. Manag. 26 (2020) 614–634. https://doi.org/10.3846/jcem.2020.12322.

[4] F. Marle, L.A. Vidal, Potential applications of DSM principles in project risk management, in: Proc. 10th Int. DSM Conf., 2008.

[5] L. Wang, T. Sun, C. Qian, M. Goh, V.K. Mishra, Applying social network analysis to genetic algorithm in optimizing project risk response decisions, Inf. Sci. (Ny). 512 (2020) 1024–1042. https://doi.org/10.1016/j.ins.2019.10.012.

[6] L. Guan, A. Abbasi, M.J. Ryan, Analyzing green building project risk interdependencies using Interpretive Structural Modeling, J. Clean. Prod. 256 (2020) 120372. https://doi.org/10.1016/j.jclepro.2020.120372.

[7] C. Fang, F. Marle, L.A. Vidal, Modelling risk interactions to re-evaluate risks in project management, in: Manag. Complex. by Model. Depend. - Proc. 12th Int. DSM Conf., 2010.

[8] C. Fang, F. Marle, A simulation-based risk network model for decision support in project risk management, Decis. Support Syst. 52 (2012) 635–644. https://doi.org/10.1016/j.dss.2011.10.021.

[9] A. Taroun, Towards a better modelling and assessment of construction risk: Insights from a literature review, Int. J. Proj. Manag. (2014). https://doi.org/10.1016/j.ijproman.2013.03.004.

[10] T. Aven, Risk assessment and risk management: Review of recent advances on their foundation, Eur. J. Oper. Res. 253 (2016) 1–13. https://doi.org/10.1016/j.ejor.2015.12.023.

[11] F. Marle, L.A. Vidal, J.C. Bocquet, Interactions-based risk clustering methodologies and algorithms for complex project management, in: Int. J. Prod. Econ., 2013. https://doi.org/10.1016/j.ijpe.2010.11.022.

[12] R.J. Yang, P.X.W. Zou, Stakeholder-associated risks and their interactions in complex green building projects: A social network model, Build. Environ. 73 (2014) 208–222. https://doi.org/10.1016/j.buildenv.2013.12.014.

[13] L. Wang, M. Goh, R. Ding, L. Pretorius, Improved simulated annealing based risk interaction network model for project risk response decisions, Decis. Support Syst. 122 (2019) 113062. https://doi.org/10.1016/j.dss.2019.05.002.

[14] C. Fang, F. Marle, M. Xie, Applying importance measures to risk analysis in engineering project using a risk network model, IEEE Syst. J. (2017). https://doi.org/10.1109/JSYST.2016.2536701.

[15] B.G. Hwang, X. Zhao, Y.L. See, Y. Zhong, Addressing Risks in Green Retrofit Projects: The Case of Singapore, Proj. Manag. J. (2015). https://doi.org/10.1002/pmj.21512.

[16] X. Qin, Y. Mo, L. Jing, Risk perceptions of the life-cycle of green buildings in China, J. Clean. Prod. (2016). https://doi.org/10.1016/j.jclepro.2016.03.103.

[17] T. Aven, Improving risk characterisations in practical situations by highlighting knowledge aspects, with applications to risk matrices, Reliab. Eng. Syst. Saf. (2017). https://doi.org/10.1016/j.ress.2017.05.006.

[18] A. Qazi, I. Dikmen, From Risk Matrices to Risk Networks in Construction Projects, IEEE Trans. Eng. Manag. (2019). https://doi.org/10.1109/TEM.2019.2907787.

[19] X. Zhao, B.G. Hwang, Y. Gao, A fuzzy synthetic evaluation approach for risk assessment: A case of Singapore’s green projects, J. Clean. Prod. (2016). https://doi.org/10.1016/j.jclepro.2015.11.042.

[20] Y. Wu, L. Li, R. Xu, K. Chen, Y. Hu, X. Lin, Risk assessment in straw-based power generation publicprivate partnership projects in China: A fuzzy synthetic evaluation analysis, J. Clean. Prod. (2017). https://doi.org/10.1016/j.jclepro.2017.06.008.

[21] T. Wang, S. Wang, L. Zhang, Z. Huang, Y. Li, A major infrastructure risk-assessment framework: Application to a cross-sea route project in China, Int. J. Proj. Manag. (2016). https://doi.org/10.1016/j.ijproman.2015.12.006.

[22] E.K. Zavadskas, Z. Turskis, J. Tamošaitiene, Risk assessment of construction projects, J. Civ. Eng. Manag. (2010). https://doi.org/10.3846/jcem.2010.03.

[23] H.W. Lo, J.J.H. Liou, A novel multiple-criteria decision-making-based FMEA model for risk assessment, Appl. Soft Comput. J. (2018). https://doi.org/10.1016/j.asoc.2018.09.020.

[24] A. V. Thomas, S.N. Kalidindi, L.S. Ganesh, Modelling and assessment of critical risks in BOT road projects, Constr. Manag. Econ. (2006). https://doi.org/10.1080/01446190500435275.

[25] C. Fang, F. Marle, E. Zio, J.C. Bocquet, Network theory-based analysis of risk interactions in large engineering projects, Reliab. Eng. Syst. Saf. (2012). https://doi.org/10.1016/j.ress.2012.04.005

[26] D. Ergu, G. Kou, Y. Shi, Y. Shi, Analytic network process in risk assessment and decision analysis, Comput. Oper. Res. 42 (2014) 58–74. https://doi.org/10.1016/j.cor.2011.03.005.

[27] B. Chang, C. Kuo, C.H. Wu, G.H. Tzeng, Using fuzzy analytic network process to assess the risks in

enterprise resource planning system implementation, Appl. Soft Comput. J. 28 (2015) 196–207. https://doi.org/10.1016/j.asoc.2014.11.025.

[28] Y. Hu, X. Zhang, E.W.T. Ngai, R. Cai, M. Liu, Software project risk analysis using Bayesian networks with causality constraints, Decis. Support Syst. 56 (2013) 439–449. https://doi.org/10.1016/j.dss.2012.11.001.

[29] R. Ojha, A. Ghadge, M.K. Tiwari, U.S. Bititci, Bayesian network modelling for supply chain risk propagation, Int. J. Prod. Res. 56 (2018) 5795–5819. https://doi.org/10.1080/00207543.2018.1467059.

[30] A.A. Ahmadabadi, G. Heravi, Risk assessment framework of PPP-megaprojects focusing on risk interaction and project success, Transp. Res. Part A Policy Pract. 124 (2019) 169–188. https://doi.org/10.1016/j.tra.2019.03.011.

[31] M. Eybpoosh, I. Dikmen, M. Talat Birgonul, Identification of Risk Paths in International Construction Projects Using Structural Equation Modeling, J. Constr. Eng. Manag. (2011). https://doi.org/10.1061/(asce)co.1943-7862.0000382.

[32] J. Yuan, K. Chen, W. Li, C. Ji, Z. Wang, M.J. Skibniewski, Social network analysis for social risks of construction projects in high-density urban areas in China, J. Clean. Prod. (2018). https://doi.org/10.1016/j.jclepro.2018.07.109.

[33] A.P. Sage, Interpretive Structural Modeling: Methodology for Large Scale Systems, McGraw-Hill, New York, USA, 1977.

[34] J.N. Warfield, Developing Interconnection Matrices in Structural Modeling, IEEE Trans. Syst. Man Cybern. (1974). https://doi.org/10.1109/TSMC.1974.5408524.

[35] M. Tavakolan, H. Etemadinia, Fuzzy Weighted Interpretive Structural Modeling: Improved Method for Identification of Risk Interactions in Construction Projects, J. Constr. Eng. Manag. 143 (2017). https://doi.org/10.1061/(ASCE)CO.1943-7862.0001395.

[36] D.W. Kwak, V.S. Rodrigues, R. Mason, S. Pettit, A. Beresford, Risk interaction identification in international supply chain logistics: Developing a holistic model, Int. J. Oper. Prod. Manag. 38 (2018) 372–389. https://doi.org/10.1108/IJOPM-03-2016-0121.

[37] H. Etemadinia, M. Tavakolan, Using a hybrid system dynamics and interpretive structural modeling for

risk analysis of design phase of the construction projects, Int. J. Constr. Manag. (2018) 1–20. https://doi.org/10.1080/15623599.2018.1511235.

[38] Y. Zhang, Selecting risk response strategies considering project risk interdependence, Int. J. Proj. Manag. 34 (2016) 819–830. https://doi.org/10.1016/j.ijproman.2016.03.001.

[39] A.M. Law, Simulation Modeling and Analysis, Fourth, McGraw-Hill, New York, USA, 2007.

[40] H. Zaroni, L.B. Maciel, D.B. Carvalho, E. de O. Pamplona, Monte Carlo Simulation approach for economic risk analysis of an emergency energy generation system, Energy. 172 (2019) 498–508. https://doi.org/10.1016/j.energy.2019.01.145.

[41] L. Zhang, Y. Huang, X. Wu, M.J. Skibniewski, Risk-based estimate for operational safety in complex projects under uncertainty, Appl. Soft Comput. J. 54 (2017) 108–120. https://doi.org/10.1016/j.asoc.2017.01.020.

[42] N. Sadeghi, A.R. Fayek, W. Pedrycz, Fuzzy Monte Carlo simulation and risk assessment in construction, Comput. Civ. Infrastruct. Eng. 25 (2010) 238–252. https://doi.org/10.1111/j.1467-8667.2009.00632.x.

[43] A. Qazi, Mecit Can Emre Simsekler, Risk assessment of construction projects using Monte Carlo simulation, Int. J. Manag. Proj. Bus. (2021) 1753–8378. https://doi.org/10.1108/IJMPB-03-2020-0097.

[44] A. Qazi, A. Shamayleh, S. El-Sayegh, S. Formaneck, Prioritizing risks in sustainable construction projects using a risk matrix-based Monte Carlo Simulation approach, Sustain. Cities Soc. 65 (2021) 102576. https://doi.org/https://doi.org/10.1016/j.scs.2020.102576.

[45] U. Arnold, Ö. Yildiz, Economic risk analysis of decentralized renewable energy infrastructures - A Monte Carlo Simulation approach, Renew. Energy. (2015). https://doi.org/10.1016/j.renene.2014.11.059.
