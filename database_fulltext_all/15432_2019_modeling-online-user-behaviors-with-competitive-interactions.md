---
otero_id: 15432
otero_key: "RMNMA8HF"
title: "Modeling online user behaviors with competitive interactions"
authors: "Saike He; Xiaolong Zheng; Daniel Dajun Zeng"
year: "2019"
journal: "Information & Management"
doi: "10.1016/j.im.2018.09.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Modeling Online User Behaviors with Competitive Interactions

Authors: Saike He, Xiaolong Zheng, Daniel Dajun Zeng

![](/api/attachments/RMNMA8HF/fulltext/images/554b75ee1b2f639c982cc2c7d1ccc59fbb884d33b1e48c9d9f77b04fdb91e28c.jpg)

PII: S0378-7206(18)30111-3

DOI: https://doi.org/10.1016/j.im.2018.09.007

Reference: INFMAN 3107

To appear in: INFMAN

Received date: 7-8-2017

Revised date: 29-8-2018

Accepted date: 4-9-2018

Please cite this article as: He S, Zheng X, Zeng DD, Modeling Online User Behaviors with Competitive Interactions, Information and amp; Management (2018), https://doi.org/10.1016/j.im.2018.09.007

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Modeling Online User Behaviors with Competitive Interactions

The authors

Saike He<sup>1</sup>, Xiaolong Zheng<sup>1\*</sup>, Daniel Dajun Zeng<sup>1,2,3</sup>

<sup>1</sup>State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China,

<sup>2</sup> University of Chinese Academy of Sciences, Beijing, China.

<sup>3</sup> Department of Management Information Systems, University of Arizona, Tucson, AZ85721, USA

{saike.he, xiaolong.zheng, dajun.zeng }@ia.ac.cn

\* Corresponding author: Xiaolong Zheng

State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China, xiaolong.zheng@ia.ac.cn, phone number: +8613811992712, fax number: +86-10-82544550.

Highlights：

 We present a concise model to study online behaviors in a temporal network.

 We evaluate the proposed model on three large-scale real-world datasets.

 Our model is effective in supervising and predicting long-range online behaviors.

Abstract—Online user behaviors are increasingly modulated by social media. Extant literature mainly focuses on investigating how network structures affect user behaviors. However, recent empirical results demonstrate that user behaviors and ork structures usually coevolve dynamically, and topological patterns turn out to be inadequate for characterizing real-world user behaviors. In this paper, we present a dynamic model to deal with this challenge. This proposed model is mainly governed by two competing principles: homophily and homeostasis. Empirical evaluations of three online real-world datasets suggest that the proposed dynamic model can well predict long-range online user behaviors.

Keywords: Online behaviors; Competitive interactions; Homophily; Homeostasis; Social media.

## 1. Introduction

Social media plays an important role in shaping the dynamics of online user behaviors, and there is a demand of an in-depth understanding on how user behaviors evolve over time and uncovering the nuanced interaction patterns among diverse populations. Recent studies have enlightened the important role played by the connection topology on collective behaviors. One group of researchers used explanatory models to infer the underlying spreading cascade [1-3]. These approaches allow retracing the whole path of spreading a given piece of information and provide significant insights into understanding information dynamics. Another group of researchers aimed to predict how a specific diffusion process unfolds in a given network based on spatial– temporal trajectories. Such predictive approaches can be categorized into two types: graph-based approaches and nongraph-based approaches. Graph-based approaches assume the existence of a static graph structure underlying the diffusion. Two seminal models in this literature are Independent Cascades (IC) [1, 2] and Linear Threshold (LT) [3, 4]. On the other side, nongraph-based approaches are usually adopted to model epidemiological processes, yet they do not define any specific graph structure [5-7].

These aforementioned studies mainly focus on investigating the relations between network topological patterns and user behaviors. Recently, several researchers have shown that topological patterns turn out to be inadequate for characterizing real-world user behaviors [9]. Evidence demonstrates that change in interindividual interactions with time is often associated with individual attributes [10]. In fact, the underlying mechanism through which individual attributes reshape the interaction topology is mainly governed by the competition between two principles: homophily [11] and homeostasis [12, 13].

For the homophily principle, social ties between individuals are found to be strongly favored by the similarity in their attributes. This principle affects the patterns and evolutions of interindividual interactions. At the individual level, homophily can promote the adoption of healthy behaviors [14, 15]. This is because humans are more likely to be influenced by those who are similar to themselves. At the community level, homophily will reduce overall behavior adoptions, thus increasing intergroup inequality across diverse populations [16]. This leads to the emergence of the phenomenon that information exchange is often blocked across populations with different attributes.

Owing to the finite social capital available for each individual (e.g., socialization time, memory span, and attention), the homeostasis principle should be considered to describe the mechanisms governing user interactions. Under the effects of homeostasis, social connections tend to remain relatively stable. In practice, this principle considers that the available resources devoted to sustain social connections are finite. The direct result of this principle is that the enhancement of some connection from an individual is counter-balanced by the weakening of other connections of the same individual to the network. This competition mechanism has been widely observed in real-world social systems. For instance, the time invested for establishing social relationships is always finite; thus, online users tend to impose a careful choice of their acquaintances and spouse [17]. This limits the number of stable social relationships that a person is able to sustain, which is well known as Dunbar’s number [18]. In addition, owing to the limited attention and memory, individuals in social media can only pay attention to a portion of the information they receive [19, 20].

In fact, the reinforcing effect caused by homophily and homeostasis governs the dynamics of user with their social contacts. However, to the best of our knowledge, no existing studies have provided appropriate solutions to uncover the dynamic process by considering the interaction of the two competing principles. In this paper, we propose a dynamic model, which is called the H2 model (i.e., Homophily and Homeostasis model), to depict the evolution of temporal network that is governed by the competition between homophily and homeostasis. In this work, we also consider the mediation effect of external shock events, which enables us to separate exogenous confounding factors from endogenous competing principles. To empirically test the performance of the H2 model, we conduct experiments on three different real-world datasets collected from Twitter.

The remaining parts of the paper are structured as follows. Section 2 reviews existing studies most relevant to our work. In Section 3, the H2 model and the corresponding algorithm for learning the model are represented. Section 4 describes the experimental setup. Section 5 gives the empirical results and analysis. Section 6 discusses the significance and potential implications of the work. Finally, Section 7 concludes this paper with a summary and a projection about future research directions.

## 2. Literature review

In this section, we present the existing studies relevant to our work from three perspectives: homophily, homeostasis, and dynamic models.

## 2.1 Homophily

The homophily principle accounts for the tendency that social ties between individuals are strongly favored by the similarity in their attributes. Under this principle, interactions between similar individuals are enhanced [11]. Such enhancement affects sentimental or behavioral adoption differently at distinct levels. At the peer level, homophilous ties promote the spread of information between individuals [11, 14, 15]. One potential reason for this is that humans are more likely to be influenced by alters, who are similar to themselves. At the community level, homophily will reduce overall information coverage, thereby increasing intergroup inequality across diverse populations [16]. This inequality effect emerges from the fact that information is blocked across populations with distinct attributes. Moreover, the effects of individual attributes can interact with those of homophily [14, 16]. Homophily among high-status individuals can help to promote information diffusion, but low-status individuals may be more likely to be influenced by heterophilous ties to high-status alters [21].

## 2.2 Homeostasis

As a constraint on homophily, homeostasis is the tendency for a system to maintain a relatively stable, constant state of balance [22]. When any deviation from homeostasis occurs, the system enacts a negative feedback to bring itself back to a state of equilibrium. Actually, the concept of homeostasis can be applied widely to any person or system that demonstrates a stable equilibrium. In physiological systems, homeostasis governs the dynamic balance of inner body indicators (e.g., blood pressure and nerve systems) to achieve optimal state. In neural systems, human memory and learning abilities are governed by specific forms of competitive adaptations, which are the essential ingredients of their physiological plasticity [23, 24].

Social systems also work to maintain equilibrium. According to functionalists, the socialization process initiates the formation of conventions and norms among all members, which enhances society stability and balance. For instance, the Family Systems Theory [25] supposes that families function as systems, whose members try to maintain their transactional patterns so that they can maintain their sense of balance. For each member of the society, the social capital available is limited; thus, people tend to enforce a careful choice of interactant and information. Owing to finite time invested in socialization, people tend to make a careful choice of the acquaintances and spouse [17]. This priority selection limits the number of stable social relationships that a person is able to sustain, which is well known as Dunbar’s number [18]. Human attention and memory are also bounded; thus, they could only pay attention to a portion of the information they receive [19].

## 2.3 Dynamic models

Approaches characterizing online social dynamics can be categorized into three groups: linear dynamical systems (LDS), nonlinear dynamical systems (NDS), and coevolving models (CEM). These approaches can help to understand online dynamics from unique perspectives and have been widely used in pattern exploration, series prediction, and event mining.

Linear dynamical systems: Traditional approaches applied to analyze temporal data include auto-regression (AR), Kalman filters (KF), and their variants [26-28]. These approaches assume that time series is linearly dependent on its historical observations. Although this linear assumption does not hold true in real-world applications, linear dynamical systems (LDS) have been used successfully in using key patterns and fingerprinting in temporal data.

Nonlinear dynamical systems: To deal with drawback in LDS, various nonlinear approaches are proposed, such as Wavelets [29] and Fourier transforms (i.e., discrete wavelet transform, discrete Fourier transform, and discrete cosine transform) [30, 31]. These approaches provide nonlinear representation for each time series. A key drawback of these approaches is that they model each time series in isolation; thus, they cannot detect the interactions between multiple coevolving sequences. Advance and diverse interaction models are proposed, including the Lotka–Volterra (LV) [32], logistic function (LF) [33], and epidemic models [5-7]. These models characterize the interactions between different time series, and also incorporate domain knowledge. However, they are not intended to capture coevolving online activities.

Coevolving models: To model coevolving sequences, Matsubara et al. developed a fully automatic mining algorithm [34]. Rakthanmanon et al. proposed a similarity search algorithm for “trillions of time series” under the dynamic time warping distance [35]. Yang et al. developed a new model for mining time-evolving event sequences [36]. The works in [37, 38] focused on summarization and clustering according to the minimum description length (MDL) principle. All of these models examine temporal data on static complex networks.

However, they are inadequate for describing many real-world networks, which are intrinsically time varying [39-42].

Indeed, online users interact in complex nonlinear patterns that change with time, e.g., exponential ebb and flow in interactions. To the best of our knowledge, none of the existing studies examines such nonlinear dynamics in a time-varying manner, and the underlying mechanism governing the dynamic process demands further investigation.

## 3. Model

In this section, we first describe the basic scheme of the proposed H2 model (Homophily and Homeostasis model), which accommodates the competition mechanisms between homophily and homeostasis. We then characterize how user attributes reshape user interactions in time-varying social networks. To avoid potential confounding effects caused by exogenous activities, we further design a shock tensor to detect external shock events. Finally, we develop optimization algorithms to estimate an optimal parameter set for the H2 model.

## 3.1 The basic scheme

Driven by the economy of attention theorized by Simon [43], social media users endeavor to compete for collective attention by intended posting online. Herein, we elaborate a competitive model (H2) to characterize and predict the posting behavior of social media users while they are interacting with others.

Modeling individual behaviors directly is often intractable because individual difference exists due to selection bias and the computational cost for large-scale individuals for a long period is expensive [44]. For reliable and effective analysis, we aggregate users into different groups according to their overall sentiments toward a given event, i.e., positive (POS), negative (NEG), or neutral (NEU). To depict the posting behavior of each user group, we need to depict two mechanisms: (a) unrestricted growth, i.e., with infinite social capital, the number of messages posted (posting number hereafter) by a user group grows at a constant rate r, and (b) competition, i.e., when social capital (e.g., socialization time) is finite, a user group can only post at most K messages at each time tick. It is notable that there are both intragroup and intergroup competitions. This competition keeps the posting number of a user group from growing exponentially, i.e., excessive posting from one group will depress the intension of its members for consequent posting. One of the canonical models that captures the above mechanisms is the LV population model of competition [45]. In the following sections, we use this framework to guide the design for the H2 model. In this model, the feedback ruled by homophily and homeostasis reshapes the interaction topology, thus influencing the consequent posting behaviors of members in each group.

Suppose that we have a collection of temporal data X of d user groups $X = \left\{ x _ { 1 } , x _ { i } , \ldots , x _ { d } \right\}$ . Here, $x _ { i }$ is the posting sequence of the user group i (i.e., $x _ { i } = \left\{ x _ { i } ^ { t } \right\} _ { t = 1 } ^ { n } )$ , and n is the time span of all d user groups. The aims of this paper are to (a) capture the evolution of X, (b) uncover how the attributes of each sequence reshape their interactions with others, and (c) predict its future dynamics. For these purposes, we need to encode the properties of user posting behaviors from three aspects:

 (P1) Nonlinear evolution of posting number of user groups: The posting number of online users fluctuates continuously, with a sharp surge and drop in extreme situations (e.g., the H1N1 pandemic [46] and tobacco control [47]). To characterize this property, we propose to use nonlinear differential equations.

 (P2) Time-varying competitive interactions between user groups: We assume that the interactions between two user groups change with time. In sum, there are three types of interaction patterns, i.e., attractive, repulsive, and none. When two user groups interact attractively, behaviors from two groups act in harmony. When two user groups interact repulsively, their behaviors compete with each other. If no interactions exist between two groups, members from each group behave independently. To encode these interaction patterns, it is necessary to introduce an interaction matrix.

(P3) Effects of external shocks: Apart from intragroup and intergroup interactions, online user behaviors are also influenced by external shock events. For example, there are few postings against vaccination during the World Immunization Week. Thus, it is imperative to quantify the effects of external shock events.

Let $g _ { _ i } ^ { t }$ be the estimated posting number of the user group i at time tick t; then, its evolution can be

described with the following equation:

$$
g _ {i} ^ {t + 1} = g _ {i} ^ {t} \left[ 1 + r _ {i} \left(1 - \frac {\sum_ {j = l} ^ {d} a _ {i j} ^ {t} \cdot g _ {j} ^ {t}}{K _ {i}}\right) \right], (i = 1, \dots , d)\tag{1}
$$

with the initial condition $g _ { i } ^ { 0 } = g _ { i }$ where

— ${ { g } _ { i } ^ { t } }$ : The posting number of the user group i at time tick t.

— $g _ { i }$ : Initial condition, i.e., the posting number of the user group i at time tick $\scriptstyle { t = 0 }$

— $r _ { i } \colon$ Intrinsic growth rate of the posting number of the user group i, $\left( r _ { i } \ge 0 \right)$

— $K _ { i }$ : Carrying capacity of the posting number of the user group i when other user groups are absent $\left( K _ { i } > 0 \right)$ This variable bounds the maximum number of posting from group i.

$- a _ { i j } ^ { t } .$ : Interaction coefficient pointing from group j to i at time tick t; $a _ { i i } ^ { t }$ corresponds to intragroup interactions. In the proposed model, the change in posting number of the user group i can be described with the following equation:

$$
\left(1 - \frac {\sum_ {j = 1} ^ {d} a _ {i j} ^ {t} \cdot g _ {j} ^ {t}}{K _ {i}}\right)\tag{2}
$$

where $a _ { i j } ^ { t }$ is the interaction coefficient, which describes the effect rate of the user group j on the user group i. If there are no intergroup interactions $( \mathrm { i } . \mathrm { e } . , a _ { i j } ^ { t } = 0 ( i \neq j ) )$ ), the model deteriorates to traditional time series model that treats each temporal sequence in isolation, such as AR, Autoregressive integrated moving average (ARIMA) and KF [48]. If $a _ { i j } ^ { t }$ is independent of the time tick t for the user groups i and j (i.e., $a _ { i j } ^ { t } \equiv a _ { i j } )$ , then the model deteriorates to the classical LV population model, where the interaction coefficients remain constant. In our modeling scheme, the interaction coefficients are set as time varying and asymmetric. This means the interaction strength is directed and varies during the whole observation period. In what follows, we describe the setting of the interaction coefficient matrix A, which accommodates both homophily and homeostasis.

## 3.2 Time-varying competitive interactions

User interactions can be quantified from two dimensions, i.e., the interaction frequency and the effect of each single interaction. For a compact model representation, we encode the compound effect of interaction frequency and its effect into a unique time-varying variable $a _ { i j } ^ { t }$ . In this model, $a _ { i j } ^ { t }$ depicts three types of interaction, i.e., attractive (negative values), repulsive (positive values), and none (zero value). In addition, user attributes are highly related to user interaction patterns. How user attributes reshape the interaction coefficients are ruled by the following equations:

$$
a _ {i j} ^ {t + 1} = a _ {i j} ^ {t} \left[ 1 + \left(s _ {i} ^ {t} \cdot p _ {i j} ^ {t} - \sum_ {l = 1} ^ {N} a _ {i l} ^ {t} \cdot p _ {i l} ^ {t}\right) \right]\tag{3}
$$

where ${ \boldsymbol { s } } _ { i } ^ { t }$ is the total incoming strength of the user group i at time tick t, $s _ { i } ^ { t } = \textstyle \sum _ { j = 1 } ^ { N } a _ { i j } ^ { t }$ . This variable quantifies the homeostasis degree of the target user group. $p _ { i j } ^ { t }$ is the degree of local homophily between groups i and $j ,$ averaged with time in the interval [t-T, t] [49]:

$$
p _ {i j} ^ {t} = \frac {1}{T} \left| \sum_ {l = 1} ^ {T} e ^ {i \phi_ {i, j} ^ {t}} \right|\tag{4}
$$

where T is a control parameter that quantifies the amount of memory used by each user group in the updating process. $\phi _ { i , j } ^ { t }$ is a phase-difference function measuring the attribute distance between the user groups i and j at time tick t:

$$
\phi_ {i j} ^ {t} = \arccos \left(\cos \left(m _ {i} ^ {t}, m _ {j} ^ {t}\right)\right)\tag{5}
$$

where $m _ { i } ^ { t }$ and $m _ { j } ^ { t }$ correspond to the attribute vectors of the user groups i and $j ,$ respectively, at time tick $t ;$ arcos(\*) calculate the angle of the cosine value enclosed. Given the above setting, the quantity $p _ { _ { i j } } ^ { t }$ takes values of [0, 1], with $p _ { _ { i j } } ^ { t } = 1$ meaning that groups i and j have been perfectly entrained with regard to their attributes along the last T time ticks [50].

![](/api/attachments/RMNMA8HF/fulltext/images/a8187936fe625f2cb337cf0f153e6e6dc5e9bfc26fb9580d89b9e74cecc31c5f.jpg)  
Fig. 1. Competition between homophily and homeostasis. Nodes represent users in the social network (node A represents the target user group), arrows indicate the interaction pointing from the neighbors (nodes B, C, D, and E) to the target user group A, and numbers along arrows measure the interaction strengths at given time ticks. The attribute distances between two groups are measured with ϕ (as shown in the homophily table in Fig. 1), whereas the total incoming strengths of group A are quantified with sA (as shown in the homeostasis table in Fig. 1).

The adaptive scheme defined in (3) retains the main characteristics of both homophily and homeostasis (Fig. 1). The user group j, that has attributes similar to those of the group i (e.g., average emotion valence and activity level), will enhance their interaction strength according to homophily. For example, the interaction strengths within group pairs (A, B) and (A, E) are enhanced at time tick $t _ { 1 }$ owing to the lower attribute distances ϕ(A, B) and ϕ(A, E) at the previous time tick $t _ { 0 }$ (Fig. 1). As a consequence of homeostasis, the interaction strength from the remaining groups will be depressed to keep constant the total incoming interaction strength ${ S } _ { i } ^ { t }$ of the group i. Under this principle, the interaction strengths from user pairs (A, C) and (A, D) are weakened at time tick $t _ { 1 }$ , keeping the incoming strength $S _ { A } ^ { t _ { 1 } } = S _ { A } ^ { t _ { 0 } } = 6$ constant (Fig. 1). For the follow time tick $t _ { 2 }$ , homophily and homeostasis compete continuously and drive the evolution of user interaction topology.

## 3.3 External shock events

Apart from endogenous competition mechanisms, it is also notable that online users change their behaviors according to various external shock events [34]. These exogenous activities should be considered to avoid any potential confounding effects (e.g., attributing pure exogenous effect to endogenous stimuli). Let ${ \dot { g } } _ { i } ^ { t }$ be the posting number of the user group i at time tick t when considering external shock events; the full model captures exogenous effects with the following equation:

$$
\dot {g} _ {i} ^ {t} = g _ {i} ^ {t} \left[ 1 + e _ {i} ^ {t} \right], \quad (i = 1, \dots , d)\tag{6}
$$

where $e _ { _ i }$ corresponds to the additional change rate of posting number of the user group i owing to the exogenous shock events. Here, $e _ { _ i }$ takes values of $[ - 1 , + \infty )$

Given the above definition, the posting number of the user group i at time tick $t ~ \dot { g } _ { i } ^ { t }$ depends on both the endogenous competitive interactions and the exogenous activities $\mathbf { E } { = } \left\{ e _ { i } \left( t \right) \right\} _ { i , t { = } 1 } ^ { d , n }$ . Each element in E describes the additional change in the posting number caused by external shock events (e.g., holidays, memorial day, etc.). For a more compressed representation of $\mathbf { E } ,$ we decompose E into two matrices, i.e., the effection matrix B of size $( k \times ~ n _ { p } )$ and the participation (weight) matrix W of size (d × $( d \times k )$ . B describes a set of k external shock components with duration $n _ { p } ,$ whereas W describes the participation weight of each sequence for each shock component. Consequently, the external shock tensor $\mathbf { E } = \left\{ e _ { _ i } ^ { t } \right\} _ { i , t = 1 } ^ { d , n }$ can be described with the following function:

$$
e _ {i} ^ {t} = f (i, t | \mathbf {W}, \mathbf {B}) = \sum_ {j = 1} ^ {k} w _ {i j} b _ {j} ^ {\tau}, \quad (\tau = [ t \mod n _ {p} ])\tag{7}
$$

where

$- \boldsymbol { n } _ { p }$ : Period (e.g., 52 weeks in one year).

— k: Number of latent shock components.

$\begin{array} { r } { - \mathbf { W } = \left\{ { w } _ { i j } \right\} _ { i , j = 1 } ^ { d , k } \ ; } \end{array}$ Participation (weight) matrix, i.e., the participation weight of group i for the j-th shock component.

$- \mathbf { B } = \left\{ b _ { j } ^ { \tau } \right\} _ { j , \tau = 1 } ^ { k , n _ { p } } .$ : Effection matrix (consisting of k effection dimensions), i.e., temporal effection at time tick τ for the j-th shock component.

![](/api/attachments/RMNMA8HF/fulltext/images/5cfa16f38ca86d53325d5003bfe9fa33109471389fd1da872cb7dd1ca4015e40.jpg)  
Fig. 2. Model illustration. Given a set of d posting sequences X of length n, the model depicts (P1) user group properties, i.e., initial volume: $g ^ { \boldsymbol { \theta } } ,$ growth rate: r, carrying capacity: K, (P2) time-varying competitive matrix: A, and (P3) a set of k shock components, i.e., participation matrix: W and effection matrix: B.

## Table 1

Notations.

<table><tr><td>Symbol</td><td>Definition</td></tr><tr><td> $d$ </td><td>Number of user groups</td></tr><tr><td> $n$ </td><td>Time span of sequences</td></tr><tr><td> $X$ </td><td> $d$  coevolving time sequences (i.e.,  $X = \{x_1, \dots, x_d\}$ )</td></tr><tr><td> $x_i$ </td><td>Temporal sequence  $i$  (i.e.,  $x_i = \{x_i^l, \dots, x_i^n\}$ )</td></tr><tr><td> $x_i^t$ </td><td>Value of sequence  $i$  at time tick  $t$ .</td></tr><tr><td> $g_i^t$ </td><td>Estimated posting number of the user group  $i$  at time tick  $t$ </td></tr><tr><td> $\dot{g}_i^t$ </td><td>Estimated posting number of the user group  $i$  at time tick  $t$  when considering external shock events</td></tr><tr><td> $g_1^0$ </td><td>Initial posting number, i.e.,  $\{g_i^0\}_{i=1}^d$ </td></tr><tr><td> $r$ </td><td>Growth rate, i.e.,  $\{r_i\}_{i=1}^d$ </td></tr><tr><td> $K$ </td><td>Carrying capacity, i.e.,  $\{K_i\}_{i=1}^d$ </td></tr><tr><td> $A$ </td><td>Interaction matrix  $(d \times d)$ , i.e.,  $A = \{a_{ij}\}_{i,j=1}^{d,d}$ </td></tr><tr><td> $n_p$ </td><td>Period (e.g., 52 weeks)</td></tr><tr><td> $k$ </td><td>Number of hidden shock events</td></tr><tr><td> $E$ </td><td>External shock tensor  $(d \times n)$ , i.e.,  $E = \{e_i(t)\}_{i,t=1}^{d,n}$ </td></tr><tr><td> $W$ </td><td>Participation (weight) matrix  $(d \times k)$ , i.e.,  $W = \{w_{ij}\}_{i,j=1}^{d,k}$ </td></tr><tr><td> $B$ </td><td>Effecton matrix  $(k \times n_p)$ , i.e.,  $B = \{b_j(\tau)\}_{j,\tau=1}^{k,np}$ </td></tr></table>

The full model is illustrated in Fig. 2, and its full parameter set to be learned is $S = \left\{ g ^ { 0 } , r , { \bf K } , { \bf A } , { \bf W } , { \bf B } \right\}$ . Table 1 summarizes the notations used throughout this paper.

## 3.4 Optimization algorithms

Next, we optimize model parameters. Specifically, we need to solve the following two problems: (1) to find an optimal set of shock components (i.e., W and B) and (2) to efficiently estimate the full parameter set S that best captures the important patterns in the posting behaviors of different user groups.

To determine the number of the component k, we elaborate an efficient coding scheme, which permits automatic configuration of appropriate sizes for W and B. This coding scheme is according to the MDL principle [51]. The basic idea behind this scheme is that the more we can compress the data, the more we can learn about its underlying patterns. The description complexity of the model parameter set S is summarized in Table 2.

## Table 2

Description complexity of the proposed model.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Item Description complexity (bits)  
$d + n$ $\log^{*}(d) + \log^{*}(n)$ $\{g^0,r,\mathbf{K}\}$ $c_{F}\cdot (\mathrm{d}\times 3)$   
A $c_{F}\cdot (d\times d - d)$ $\{k,\mathbf{W},\mathbf{B}\}$ $\log^{*}(k) + \log^{*}(n_{p}) + c_{F}\cdot (dk + kn_{p})$
</div>

Note. lo $\mathbf { g } ^ { * }$ is the universal code length for integers. Floating point cost $c _ { F } = 8$ bits.

Once the full parameter set S is determined, the original data X can be encoded with Huffman coding [52]. Huffman coding assigns a number of bits (i.e., the negative log-likelihood) to each value in X. The encoding cost of X given parameter S is calculated using the following equation:

$$
\operatorname{Cost} _ {C} (X | S) = \sum_ {i, t = 1} ^ {d, n} \log_ {2} p _ {\text { Gauss } (\mu , \sigma^ {2})} ^ {- 1} \left(x _ {i} ^ {t} - \dot {g} _ {i} ^ {t}\right)\tag{8}
$$

where $ { \boldsymbol { x } } _ { _ { i } } ^ { t }$ and $\dot { g } _ { i } ^ { t }$ are the original and estimated posting numbers of the user group i at time tick $t ; \ \mu$ and $\sigma ^ { 2 }$ are the mean and variance of the distance between $ { \boldsymbol { x } } _ { _ { i } } ^ { t }$ and ${ \dot { g } } _ { i } ^ { t }$

```txt
ALGORITHM 1. CI-FIT(X)

Input: Coevolving sequences X (d × n).

Output: Full parameter set, i.e., S = {g⁰, r, K, A, W, B}.

A = I_d;    /* Initialize A, i.e., identity matrix of size (d × d) */
For i = 1: d do    /* (I) Single fitting */
    Si = STEPFIT(xi);    /* Estimate individual parameters of sequence i */
End For

While improving the parameters do    /* (II) Pair fitting */
    i = arg max Cos t_T(x_i';S);    /* Find the most unfitted sequence xi */
    For j = 1: d do    /* Estimate parameters of pair (i, j) */
    S'_ij = STEPFIT(xi, x_j);
End For
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$j = \arg\min_{j'} \text{Cos } t_T(x_i, x_{j'}, S'_{ij'})$ ; /* Find the most affecting sequence $x_j$ on $x_i$ */  
Update $S_{ij} = S'_{ij'}$  /* Update best pair parameters */  
End While  
$S = \arg\min_{S'} \text{Cos } t_T(X; S')$ ; /* (III) Full fitting */  
Return S.
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
ALGORITHM 2. STEPFIT(X)

Input: Coevolving sequences X (d × n).

Output: Full parameter set, i.e., $S = \{g^0, r, \mathbf{K}, \mathbf{A}, \mathbf{W}, \mathbf{B}\}$.

$\mathbf{W} = \mathbf{B} = 0$;

While improving the parameters do

$\left\{ g^0, r, \mathbf{K}, \mathbf{A} \right\} = \arg \min_{g^{0'}, r', \mathbf{K}', \mathbf{A}'} \text{Cos } t_T \left( X; g^{0'}, r', \mathbf{K}', \mathbf{A}', \mathbf{W}, \mathbf{B} \right)$;

$\left\{ \mathbf{W}, \mathbf{B} \right\} = \arg \min_{\mathbf{W}', \mathbf{B}'} \text{Cos } t_T \left( X; g^0, r, \mathbf{K}, \mathbf{A}, \mathbf{W}', \mathbf{B}' \right)$;

End While

Return $S = \{ g^0, r, \mathbf{K}, \mathbf{A}, \mathbf{W}, \mathbf{B} \}$.
</div>

The total code length for X with regard to a given parameter set S is described by the following equation:

$$
\begin{array}{r l} \operatorname{Cos} t _ {T} (X; S) & = \log^ {*} (d) + \log^ {*} (n) + \operatorname{Cos} t _ {M} (g ^ {0}, r, \mathbf {K}) \\ & + \operatorname{Cos} t _ {M} (\mathbf {A}) + \operatorname{Cos} t _ {M} (k, \mathbf {W}, \mathbf {B}) + \operatorname{Cos} t _ {C} (X | S) \end{array}\tag{9}
$$

The optimal number of shock components $\left( k _ { o p t } \right)$ could be automatically determined by minimizing (9) with regard to k:

$$
k _ {o p t} = \arg \min \operatorname{Cos} t _ {T} (X; S)\tag{10}
$$

Given the optimal number of shock components, we then turn to estimate the whole parameter set $S = \left\{ g ^ { 0 } , r , { \bf K } , { \bf A } , { \bf W } , { \bf B } \right\}$ in an efficient and effective way. The most straightforward optimization would be estimating all the parameters in S simultaneously. However, this approach is highly expensive and ineffective. It requires the estimation of $( 3 d + d { \cdot } ( d { - } 1 ) + k { \cdot } ( d + n _ { p } ) )$ parameters for each iteration. Additionally, it requires the comparison of all possible solutions for different k values (1≤k≤d). As such, we introduce a partition approach CI-FIT (competitive interaction-fit) to analyze temporal data at a large scale, yet with a significant reduction in computational cost. Algorithm 1 describes the overall procedure of CI-FIT. Instead of fitting all the parameters of set S simultaneously, the optimization algorithm first assumes that no intergroup interactions exist, and set A $\mathbf { \sigma } = \mathbf { I } _ { d } , \mathrm { i . e . , } \mathrm { a } _ { i j } ^ { t } = 0 ( \mathrm { i } \neq \mathrm { j } )$ . Through the STEPFIT algorithm (Algorithm 2), the model parameter ${ { S } _ { i } } = \left\{ p _ { i } , r _ { i } , K _ { i } , w _ { i i } , b _ { i } \right\}$ for each individual sequence xi $( i = 1 , . . . , d )$ can be estimated. Next, it assumes that there exists an interaction between the two user groups i and j. In each single iteration, CI-FIT attempts to find the best sequence pair (xi, xj) that minimizes the cost function CostT $( x _ { i } , \ x _ { j } \ | \ S _ { i j } )$ . This pair-fitting process continues until convergence. Finally, the algorithm optimizes the full parameter set S using the entire sequence set X.

## 4. Experimental setup

To test the proposed H2 model, we used three different Twitter datasets: (1) the measles outbreak in the USA in 2015 [53], (2) the Ebola outbreak in West Africa in 2015 [54], and (3) the imposed e-cigarettes regulations in the USA in 2016 [55]. The first two datasets represent the widespread epidemics with different scales and impacts, and the third dataset deals with enhanced e-cigarette regulations. These three datasets are appropriate for this research for two reasons. First, large-scale datasets allow supervising the entire competitive interactions of online user behaviors. Second, data analyzing from three different types of online user behaviors can offer generalizable insights into the interaction patterns.

## 4.1 Data collection

For each of the three datasets, we used Twitter4J API [56] to collect all tweets in English containing predefined keyword sets (Table 3). In each dataset, we constructed two synthetic keyword sets, where the root set contains mention variations for measles, Ebola, and e-cigarettes, and the Prefix $( S u f f i x )$ set contains properties related to the mentions (e.g., regulation or isolation policies). We combined words from these two sets to synthesize keywords for collecting target tweets. Keywords that hit no meaningful tweets were ignored in Table 3, such as missing spellings (e.g., “ecigarett regulation”) and seldom used patterns (e.g., “morbilli vaccination”). Along with the tweet text, we also downloaded the tweet id, the user id, the publish time, and the retweet id. The descriptive statistics of the three experimental datasets are summarized in Table 4.

## Table 3

Keywords used for data collection.

<table><tr><td>Datasets</td><td>Root</td><td></td><td>Prefix (Suffix)</td><td>Keywords</td></tr><tr><td>Measles*</td><td>measles,</td><td>measle,</td><td>vaccination,</td><td>measles vaccination, measles vaccination,</td></tr></table>

<table><tr><td></td><td>morbilli, rubeolla</td><td>rubeola, vaccinate against, vacinate against</td><td>rubeola vaccination, vaccinate against measles, vaccinate against measles, vaccinate against morbilli, vaccinate against rubeola, vaccinate against rubeolla, vaccinate against measles, vaccinate against rubeola, vaccinate against rubeolla</td></tr><tr><td>Ebola</td><td>ebola</td><td>patient, outbreak, virus, epidemic, quarantine, isolation</td><td>ebola patient, ebola outbreak, ebola virus, ebola epidemic, ebola quarantine, ebola isolation</td></tr><tr><td>E-Cigarettes</td><td>ecig, ecigs, e-cig, e-cigarette, e-cigarettes, ecigarette, ecigarettes, electronic cigarette, electronic cigarettes, electronic nicotine delivery systems, vape, vapor, vapor, vapers, vaping, vapin, evape, vaporizer, vaporizers</td><td>regulation, regulate, restrict, restriction</td><td>ecig regulation, ecigs regulation, e-cig regulation, e-cigarette regulation, e-cigarettes regulation, ecigarettes regulation, electronic cigarette regulation, regulation of electronic cigarettes, regulation of electronic nicotine delivery systems, vape regulation, vaper regulation, vapers regulation, vaping regulation, vapin regulation, vaporizer regulation, vaporizers regulation, regulate vapor, regulate vaping, regulate evape, regulate vaporizer, regulate vaporizers, restrict vaporizer, restrict vaporizers, ecig restriction, ecigs restriction, e-cig restriction, e-cigarette restriction, e-cigarettes restriction, ecigarette restriction, electronic cigarette restriction, electronic cigarettes restriction, vape restriction, vaping restriction, vaporizers restriction</td></tr><tr><td>Note.</td><td colspan="3">*: Root words are selected according to CHV Wiki</td></tr></table>

http://consumerhealthvocab.chpc.utah.edu/CHVwiki/

## Table 4

Data statistics.

<table><tr><td>Item</td><td>Measles</td><td>Ebola</td><td>E-Cigarettes</td></tr><tr><td>Number of tweets</td><td>206,687</td><td>255,118</td><td>772,969</td></tr><tr><td>Number of users</td><td>101,514</td><td>150,382</td><td>336,492</td></tr><tr><td>Number of weeks</td><td>28</td><td>4</td><td>24</td></tr></table>

## 4.2 Sentiment analysis and user group division

After data collection, we classified each tweet into one of four sentiment polarities: positive, negative, neutral, and irrelevant, with regard to the topic discussed in each dataset. For the Measles, Ebola, and E-Cigarettes datasets, the topics are respectively “getting vaccination against measles,” “isolation policy during the Ebola outbreak,” and “E-Cigarettes Regulation”. Because the original dataset was very large for manual classification within a reasonable timeframe, we used a machine learning approach to identify the sentiment manifested in each tweet. Inspired by [57], we designed a two-step approach, i.e., we first decided the relevance of the tweet with the topic and then decided its polarity (e.g., positive, negative, or neutral) if it is relevant.

In each of the two steps, we built a SVM classifier to perform classification. To train the classifiers, we used LIBSVM [58] with a linear-kernel and adopted all other parameters by default. To create a training dataset for each classifier, we held back a random subset of 5% tweets from each dataset. For the held-out subset, we manually rated each tweet with regard to the assigned topic. Because tweets are free texts with nonstandard abbreviations, slangs, and otherwise poorly written phrases, this characteristic demands us to conduct dedicated preprocessing, including tweet normalization (e.g., restoring word lengthening such as “coooool” to its original form “cool”), part-of-speech (POS) tagging, and word stemming. In this study, we built a rule-based model for assign each group a numerical code. For example, the word “coooool” would be first converted by Soundex to C400, and then, this code would be used to find a match in SenticNet, i.e., “cool” (whose Soundex code is also C400). For POS tagging and word stemming, we use the NLTK Toolkit [60].

## Table 5

Sentiment analysis results.

<table><tr><td>Category</td><td>Measles</td><td>Ebola</td><td>E-Cigarettes</td></tr><tr><td>POS</td><td>26,699</td><td>41,285</td><td>156,041</td></tr><tr><td>NEG</td><td>78,558</td><td>46,718</td><td>90,378</td></tr><tr><td>NEU</td><td>52,476</td><td>85,477</td><td>310,118</td></tr><tr><td>Irrelevant</td><td>48,954</td><td>81,638</td><td>216,432</td></tr><tr><td>Total</td><td>206,687</td><td>255,118</td><td>772,969</td></tr></table>

Note. The statistics takes into account both the training datasets (that manually labeled) and the classification results (obtained by the two-step classifier).

In feature design, we were inspired by the effective features discovered by [61, 62]. The chosen ones were content features (e.g., words, punctuation, emoticons, and hashtags) and sentiment lexicon features (e.g., number of sentiment words in a tweet). In both the relevance classifier and the polarity classifier, the same feature set was used. Overall, this approach combing two classifiers achieved an empirical precision of 80.14% with fourfold cross-validation on the training dataset. We then used the trained classifiers to classify tweets in each corresponding dataset. The statistics of the classification results are presented in Table 5.

On the basis of the sentiment analysis results, we divided users into three groups according to their average sentiment valence of tweets, as given by an indicator function:

$$
C _ {i} (u) = \left\{ \begin{array}{l l} P O S, & \text { if } 1 / | M | \sum_ {m \in M} V a l (m) > v _ {i l o w}, \\ N E G, & \text { if } 1 / | M | \sum_ {m \in M} V a l (m) <   v _ {i u p}, \\ N E U, & \text { otherwise }. \end{array} \right.\tag{11}
$$

where $C _ { i } ( u )$ indicates the group type in the i-th dataset, with POS, NEG, and NEU, respectively, representing the positive, negative, and neutral user groups; M is the set of $| M | { = } N$ relevant tweets written by user u $( \mathrm { i f } | M | = 0 ;$ the user together with his tweets will be pruned out from the dataset); $V a l ( m )$ represents the sentiment valence of tweet m; vilow and $\mathbf { V } _ { i u p }$ are, respectively, the lower and upper valence boundaries that separate the three user groups for the i-th dataset. In general, we considered that users within each group possess a certain kind of sentiment “tone,” i.e., users within the POS group possess an overall positive sentiment in the whole observation period, although with fluctuations in their emotion dynamics.

## 4.3 Group attributes

To inquire the competitive interactions between user groups, we mainly employed three types of group attributes, namely, emotion attributes, behavior attributes, and meme attributes [63], to calculate the distance $\phi _ { i , j } ^ { t }$ of the attributes defined in (5). These attributes are summarized in Table 6. Emotion (behavior) attributes were designed to capture the relationship between emotion states (activity level) of online users and their posting number, whereas meme attributes might uncover the effect of meme diffusion on the posting number. In this study, we used the algorithm proposed by He et al. [64] to extract memes (i.e., popular phrases in social media). On the basis of these attributes, we were able to generate an attribute vector $m _ { i } ^ { t }$ for each user group i at time tick t. Then, $\phi _ { i , j } ^ { t }$ can be readily calculated according to (5). The above attributes were chosen, as they are representative for describing user groups, whereas other attributes can also be involved flexibly if applicable in other situations.

## Table 6

Group attributes.

<table><tr><td>Type</td><td>Attribute</td><td>Description</td></tr><tr><td rowspan="2">Emotion</td><td> $avgEmoVal_{i}^{t}$ </td><td>Average emotion valence of individuals in group  $i$  at time tick  $t$ .</td></tr><tr><td> $avgEmoStren_{i}^{t}$ </td><td>Average emotion strength of individuals in group  $i$  at time tick  $t$ ; emotion strength is measured by the ratio of posts with the domain sentiment.</td></tr><tr><td rowspan="2">Behavior</td><td> $avgActLevel_{i}^{t}$ </td><td>Average activity level (posting number) of individuals in group  $i$  at time tick  $t$ .</td></tr><tr><td> $diffuCoef_{i}^{t}$ </td><td>Ratio of diffusion (reply or reposting) in group  $i$  at time tick  $t$ .</td></tr><tr><td rowspan="2">Meme</td><td> $memeEntr_{i}^{t}$ </td><td>Entropy of meme distribution in group  $i$  at time tick  $t$ .</td></tr><tr><td> $memeEmbed_{i}^{t}$ </td><td>Ratio of common memes between individuals in group  $i$  at time tick  $t$ .</td></tr></table>

## Table 7

User number in each group.

<table><tr><td>User Group</td><td>Measles</td><td>Ebola</td><td>E-Cigarettes</td></tr><tr><td>POS</td><td>17,323</td><td>29,736</td><td>80,830</td></tr><tr><td>NEG</td><td>31,537</td><td>35,679</td><td>63,242</td></tr><tr><td>NEU</td><td>42,501</td><td>59,098</td><td>152,039</td></tr><tr><td>Total</td><td>91,361</td><td>124,513</td><td>296,111</td></tr></table>

## 4.4 Parameter settings

In the following studies, we set time tick as 1 day, T=7 days in (4), and $n _ { p }$ is the observation period of each dataset. For user group division, we set [vlow , vup], respectively, as [-0.157, 0], [-0.001, 0], and [0, 0.118] for the Measles, Ebola, and E-Cigarettes dataset. This setting considers the emotion bias [65] in each dataset. For instance, the emotion bias in the measles dataset is negative (e.g., average emotion is -0.157), thus indicating that a large portion of users hold negative sentiments toward vaccination during the measles outbreak in 2015. With irrelevant users pruned, the results for user group division are shown in Table 7.

## 5. Results

We analyze the dynamic behavior of online users in different groups from three aspects. First, we check how our model fits the posting number of user groups holding different sentiments, i.e., positive, negative, or neutral. Second, we evaluate the prediction performance of the model. Third, we examine how the competition between homophily and homeostasis drives the evolution of user group interactions.

(i) Fitting result - RMSE=0.037327  
![](/api/attachments/RMNMA8HF/fulltext/images/e588bd8843dc6bcc5e0801bbce8bb43e396c8eab6db5b5aee20f460e8ed28fe2.jpg)

(ii) Time-varying interactions  
![](/api/attachments/RMNMA8HF/fulltext/images/38456f7123d980e069a841d4f89aa470fa715b17d282958c70a70a6c0b3344e6.jpg)

(iii) External shocks (k=1)  
![](/api/attachments/RMNMA8HF/fulltext/images/81c459880adeac130b31218f34ad52c093b086098a158f56330e9c739bde46fe.jpg)  
(a) Measles

(i) Fitting result - RMSE=0.037531  
![](/api/attachments/RMNMA8HF/fulltext/images/2d7ff79ea06ba4dfbe36e0bcb59512c865b86eed44d9cfaf271096d40372d238.jpg)

(ii) Time-varying interactions  
![](/api/attachments/RMNMA8HF/fulltext/images/4a13bc960d6ab290f975aa71908a456ddfd5ea83848635db9eab7137855ccc0e.jpg)

(iii) External shocks (k=1)  
![](/api/attachments/RMNMA8HF/fulltext/images/26782d6b98896710d2808d16d26c647e35c2fad3f2bd57c9e056502cb20ac12e.jpg)  
(b) Ebola

(i) Fitting result - RMSE=0.050765  
![](/api/attachments/RMNMA8HF/fulltext/images/c8b925e7e8e6937dd0813583fe0fd309c768f39eaab80cb9c71286264f470fa9.jpg)

(ii) Time-varying interactions  
![](/api/attachments/RMNMA8HF/fulltext/images/77eedf3b42f1a978897f9f2c08c8ac1d2f1e3c177d0b18a612a278cf4cdff080.jpg)

(iii) External shocks (k=1)  
![](/api/attachments/RMNMA8HF/fulltext/images/a82de3eb3bd57af29c2c5e612d5a20bcd807cce499b64a443648b7b884a78f5e.jpg)  
(c) E-Cigarettes  
Fig. 3. Fitting results. Our model (deep color lines) fits the original data (light color lines) very well. In \*-i figures, blue, yellow, and green lines, respectively, correspond to the POS, NEG, and NEU groups; In \*-ii figures, $a _ { i j } ^ { t }$ demotes the interaction strength pointing from the user group j to i; the subscripts 1, 2, and 3 correspond to the POS, NEG, and NEU groups, respectively.

## 5.1 Model fitting

We demonstrate the power of our model in terms of capturing important and informative patterns of posting behaviors of online users. Fig. 3 shows the fit of the H2 model to the posting number of user groups with different sentiments. The x-axis corresponds to the time period, and the posting numbers in the y-axis are scaled so that each temporal series has a peak volume of 1.0.

Fig. 3-\*-i shows the fitting results (deep colored lines) and the original sequences (light colored lines) for different datasets. The good agreement proves the capability of the model in capturing long-range online user behaviors. In the measles (Fig. 3-a-i) and Ebola datasets (Fig. 3-b-i), the posting volume of the NEG group outpaces that of the POS group. This result indicates that resentments against the measles vaccination and the Ebola quarantine still prevail among online users. With regard to E-Cigarette regulation (Fig. 3-c-i), the posting volumes of the POS group and the NEG group surpass each other interchangeably, thereby reflecting that there are fierce debates on whether E-Cigarettes should be regulated on Twitter. After April 10, 2016, postings from the POS group outpaced those from the NEG group. This change suggests that tweets supporting for E-Cigarette regulation ultimately prevailed on Twitter.

Fig. 3-\*-ii shows the evolution of time-varying interactions between different users groups $( a _ { i j } ^ { t }$ in the y-axis). Compared with intergroup interactions, user behaviors are more influenced by members from the same group because $a _ { i i } ^ { t } > a _ { i j , i \neq j } ^ { t }$ for most of the time (p<0.001 according to an independent two-tailed t-test). This interaction pattern can be explained by the homophily principle, i.e., online users are more likely to be influenced by alters who are similar to themselves.

The effects of external shocks are captured by the participation matrix W and the Effection matrix B. The participation matrix W depicts how the sentimental behaviors of each user group are affected by external shock events. The values of the learned W for the three datasets are shown in Table 8. Table 8 suggests that external shock events affect the POS group and the NEG group differently, i.e., posting behaviors of the NEG group are more sensitive to external shocks (values in the third column of Table 8 are large), and their volumes are generally augmented when big events occur.

## Table 8

The learned W for the three datasets.

<table><tr><td rowspan="2">Datasets</td><td colspan="3">W</td></tr><tr><td>POS</td><td>NEG</td><td>NEU</td></tr><tr><td>Measles</td><td>-1.157</td><td>5.394</td><td>3.826</td></tr><tr><td>Ebola</td><td>0.222</td><td>1.264</td><td>-0.829</td></tr><tr><td>E-Cigarettes</td><td>-1.683</td><td>5.260</td><td>0.719</td></tr></table>

On the other hand, the effection matrix B encodes the effects of external events (y-axis in Fig. 3-\*-iii), and the k value in B determines the event number. Fig. 3-\*-iii summarizes external shock events detected during the observation period in each dataset. As the values of matrix B deviate from zero apparently, the proposed model does detect external shock events. Take the measles outbreak, for example (Fig. 3-a-iii); the World Immunization Week (from April 23 to April 30 2015) depresses the posting behaviors of the NEG group because $\mathrm { W \cdot B } < 0$ within the corresponding timeframe; when one death due to measles was reported, behaviors of the NEG group are catalyzed because $\mathbf { W \cdot B } > 0$ . In the two other datasets, we also detect several external events that depress or catalyze online user behaviors, as shown in Fig. 3-b-iii and Fig. 3-c-iii.

It is also noteworthy that all the parameters in the H2 model are fitted automatically without any empirical refinement. The only factors that might impact the fitting results are the initial conditions (e.g., the initial values in $\left\{ g ^ { 0 } , r , { \bf K } , { \bf A } , { \bf W } , { \bf B } \right\} )$ ). To test the robustness of the H2 model, we have run the model 100 times with randomly selected initialization conditions and observed similar fitting results. This fact proves that the H2 model is robust and insensitive to the parameters.

To further test the rationale of the proposed H2 model, we also compared its fitting ability with three alternative models, namely, the revised H2 model, which only considers homophily (H model); the LV population model; and the AR model. Fig. 4 shows the root mean square error (RMSE) between the original and the estimated posting number given by different models. A lower value indicates a higher fitting accuracy. As shown in Fig. 4, the H2 model achieved the highest fitting accuracy. Because the AR model tries to fit the posting behaviors of each user group linearly and in isolation, it is incapable of capturing nonlinear interactions between different user groups and achieves the worst performance. As an advance, the LV model characterizes nonlinear dynamics and intergroup interactions. However, it assumes that both intragroup and intergroup interactions are constant during the observation period; thus, they are inadequate for describing time-varying networks in the real world. With regard to the H Model, it is able to describe time-varying interactions by involving the homophily principle. This principle enables it to capture the interaction enhancement between similar user groups. However, the H model fails to consider the homeostasis principle due to limited social capital; thus, it could not depict the essential competition between homophily and homeostasis.

![](/api/attachments/RMNMA8HF/fulltext/images/e96a3167c5c55a765f0da8b211b9393e6d6538310e316bdfaa18adcda53e13f5.jpg)  
(a) Measles  
Fig. 4. Fitting error of different models.

![](/api/attachments/RMNMA8HF/fulltext/images/10aba11adafbc3b5ce577fe57ecadd99c36060f21d34524803bbc061e25cfc37.jpg)  
(b) Ebola

![](/api/attachments/RMNMA8HF/fulltext/images/0365010008602eef61c196eaecd5f027d04031846e39e751223700469f07b6ed.jpg)  
(c) E-Cigarettes

## 5.2 Prediction performance

This subsection presents the prediction ability of the proposed H2 model compared with two alternatives, i.e., the LV model and the AR model. Fig. 5 shows the prediction performance of different models. In this evaluation, we trained the model parameters by using the 3/4 values for each user group (black dashed lines in Fig. 5) and then predicted the following time ticks (colored lines). In Fig. 5, the top to the bottom rows show the original data and the prediction results of H2, LV, and AR, respectively. As shown in Fig. 5, the proposed H2 model successfully predicted the long-range evolution of posting behaviors of different user groups (with the longest period of 28 weeks in Fig. 5-a). In addition, the H2 model can capture the change details of user posting behaviors, i.e., the surge and the drop of posting numbers. In contrast, the LV model can model the nonlinear change in posting numbers, yet ignores the details, whereas the AR model only captures the general trend in a linear manner.

Among the three datasets, Ebola is the easiest to predict (lowest RMSE). This may be attributed to the fact that the posting behaviors of users during the Ebola outbreak are comparatively stable (with standard deviations of 0.056, 0.073, and 0.081 for the POS, NEG, and NEU groups, respectively); thus, the AR model can also predict with high accuracy through linear combination (bottom of Fig. 5-b). In contrast, the posting behaviors of Measles (Fig. 5-a) and E-Cigarettes (Fig. 5-c) fluctuate frequently, with the respective standard deviation vectors [0.136, 0.192, 0.187] and [0.093, 0.089, 0.107].

![](/api/attachments/RMNMA8HF/fulltext/images/f3277f213fc097cbb840a0094c1ccf810f53c842c848a5264698559f46af485a.jpg)

(a) Measles  
![](/api/attachments/RMNMA8HF/fulltext/images/d9beeb33f2c5e5f62916f65de19b2f598a7dffe41045a54ade58e8151fd0ade5.jpg)  
(b) Ebola

![](/api/attachments/RMNMA8HF/fulltext/images/c235b288eebd8995171a0f859278d808cc26a48eb84256cbed52da2b39749aff.jpg)  
Fig. 5. Prediction performance of different models.  
(c) E-Cigarettes

## 5.3 Time-varying competitive interactions

We examine how online users interact with each other and how the two competing principles homophily and homeostasis drive the evolution of online interaction patterns.

Homophily: We first check how the homophily principle drives user interactions. We previously found that the behaviors of online users are most influenced by those with similar sentiments because intragroup interactions are the strongest. With regard to intergroup interactions, we find that there exist significant positive correlations between interaction strengths from different user groups. The corresponding Pearson's Correlation Coefficients (PCCs) are shown in Table 9, with p<0.001. These results suggest a strong mutual interaction between user groups, i.e., the surge of posting numbers from one group is likely to incur more postings from other groups, and vice-versa.

Further, we quantify the relationship between intergroup interactions and the group attributes. As shown in Table 10, the interaction strength is negatively correlated with attribute distance, with merely several insignificant exceptions. Because $\phi ^ { t } { } _ { i j }$ measures the distance of the attributes between the user groups i and j at time tick t, this negative correlation suggests that interactions between user groups are stronger when their attributes are similar, and vice-versa. These negative correlations well support the homophily principle, i.e., interactions between similar individuals are enhanced.

## Table 9

Strength correlations between user groups.

<table><tr><td>Interactions</td><td>Measles</td><td>Ebola</td><td>E-Cigarettes</td></tr><tr><td> $a_{12}$  VS.  $a_{21}$ </td><td>0.987</td><td>0.997</td><td>0.998</td></tr><tr><td> $a_{13}$  VS.  $a_{31}$ </td><td>0.999</td><td>0.889</td><td>0.953</td></tr><tr><td> $a_{23}$  VS.  $a_{32}$ </td><td>0.987</td><td>0.993</td><td>0.992</td></tr></table>

Note. $\mathrm { a _ { i j } }$ denotes the interaction strength pointing from the user group j to $i ;$ the subscripts 1, 2, and 3 correspond to the POS, NEG, and NEU groups, respectively.

## Table 10

Correlations between interaction strength and attribute distance.

<table><tr><td>Item</td><td>Measles</td><td>Ebola</td><td>E-Cigarettes</td></tr><tr><td> $a_{12}$  VS.  $\phi_{12}$ </td><td>-0.401***</td><td>-0.309*</td><td>-0.238***</td></tr><tr><td> $a_{21}$  VS.  $\phi_{12}$ </td><td>-0.340**</td><td>-0.270</td><td>-0.249***</td></tr><tr><td> $a_{13}$  VS.  $\phi_{13}$ </td><td>-0.305*</td><td>-0.641***</td><td>-0.251***</td></tr><tr><td> $a_{31}$  VS.  $\phi_{13}$ </td><td>-0.300</td><td>-0.534***</td><td>-0.242***</td></tr><tr><td> $a_{23}$  VS.  $\phi_{23}$ </td><td>-0.387**</td><td>-0.382**</td><td>-0.253***</td></tr><tr><td> $a_{32}$  VS.  $\phi_{23}$ </td><td>-0.378**</td><td>-0.388**</td><td>-0.170</td></tr></table>

Note. $\mathrm { a _ { i j } }$ denotes the interaction strength pointing from the user group j to i; ϕij represents the distance of attributes between the user groups i and $j ;$ the subscripts 1, 2, and 3 correspond to the POS, NEG, and NEU groups, respectively; significance of correlation according to a paired two-tailed t-test is indicated using \*-notation $( ^ { * } \mathrm { = ^ { * } p \mathrm { < 0 . 1 ^ { 1 9 } , } } * * \mathrm { = ^ { * } p \mathrm { < 0 . 0 5 ^ { 9 } , } * * * = ^ { \mathrm { * } } p \mathrm { < 0 . 0 1 ^ { \mathrm { > } } } ) }$ .

Homeostasis: To test whether the social capital is limited during online social interactions, we examine how the total incoming strength of the user group i (denoted as $s _ { i } ^ { t } )$ evolves. Fig. 6 depicts the relative difference of ${ S } _ { i } ^ { t }$ at each time tick t, which is defined as $r d _ { i } ^ { t } = \frac { s _ { i } ^ { t } - s _ { i } ^ { t - 1 } } { s _ { i } ^ { t - 1 } } \times 1 0 0 \%$ . The results suggest that the temporal dynamics of ${ S } _ { i } ^ { t }$ is stationary because the mean and variance span in narrow intervals (no larger than 1e-12). This stationary is consistent with previous modeling assumption that online social capital devolved in online interactions is finite. Further, we notice that $r d _ { i } ^ { t }$ still fluctuates at the end in the Ebola dataset, whereas $r d _ { i } ^ { t }$ diminishes to zero in the Measles and

E-Cigarettes datasets. This difference may be attributed to the relative short observation period of Ebola (only 1 month), which is not long enough for social capital to enter the stable state.

![](/api/attachments/RMNMA8HF/fulltext/images/ca0ad576e37e2eec59870c122003b04e964a6e1a3483819df1446e7b58ad0531.jpg)  
(a) Measles

![](/api/attachments/RMNMA8HF/fulltext/images/3e054522b3ecbbc4600c9a1b41b08a18279606d5f53a7a7487221ea84ec89663.jpg)  
(b) Ebola

![](/api/attachments/RMNMA8HF/fulltext/images/f67157932d17a9e2b7b25ddc8077f82194884eb919fb1e59baac56dd0573b38e.jpg)  
(c) E-Cigarettes  
Fig. 6. Relative difference of $\mathrm { S i } .$ The subscripts 1, 2, and 3 correspond to POS, NEG, and NEU groups, respectively.

## 6. Discussion

In this paper, we investigated how individual attributes reshape their social connections by considering two competing principles, i.e., homophily and homeostasis. The evaluation was conducted on three Twitter datasets: the measles outbreak in the USA in 2015, the Ebola outbreak in West Africa in 2015, and the imposed e-cigarettes regulations in the USA in 2016. These datasets are large enough and offer generalizable implications.

Originally, we elaborated a dynamic model that accommodates homophily and homeostasis at the same time. In this model, we also considered the mediation effect of external shock events by involving a shock tensor. Experimental results proved that the proposed H2 model is able to capture important and informative patterns of user behaviors. Furthermore, examination of the time-varying interactions suggested that online users are more likely to be influenced by alters who are similar to themselves. Analysis of the learned shock tensors indicated that users holding negative opinions are more sensitive to external shocks in all three datasets.

In the behavior prediction task, the H2 model successfully predicted the long-range evolution of online users’ posting behaviors. Compared to existing methods, the H2 model consistently provided the lowest error rate. This result can be attributed to its nonlinear depiction of changes in user behaviors and consideration of both homophily and homeostasis.

We turned next to study how homophily and homeostasis drive the evolution of online users’ interaction patterns. We found that there exists reciprocal interaction between user groups, i.e., posting behaviors of one group tend to incur consequent posting from its interactant. We also noticed that interactions between similar user groups are strong. This result, again, supports the homophily principle. By quantifying the total incoming strength of a user group, we found that homeostasis is well preserved in all three datasets.

## 7. Conclusions and future work

We have proposed a new dynamic model (H2 model) to depict the evolution mechanisms of the temporal networks, which is governed by the competition of homophily and homeostasis. Evaluation of the three Twitter datasets suggested that the H2 model can capture long-range behavior dynamics and present lower error rate in behavior prediction. Through the shock tensor of the model, we successfully detected several typical events and revealed that users with negative emotions are more sensitive to external shock events than those with positive emotions. By examining online time-varying connections, we found that interaction strength is negatively correlated with user attribute distance, whereas homeostasis is well preserved in the datasets.

In our future work, we intend to clarify how different kinds of user attributes influence the online interaction topology. As the interaction topology may affect the sentiments spreading on it, we will further pay more attention to uncover the relationship between network diversity and sentiment diffusion in online communities.

## Acknowledgment

We thank each member of the iBasic team in the Institute of Automation, Chinese Academy of Sciences. This work was supported in part by the following grants: the National Key R&D Program of China under Grant Nos. 2017YFC1200302, 2016QY02D0305, and 2017YFC0820105; the National Natural Science Foundation of China under Grant Nos. 71602184, 71472175, 71603253, and 71621002; and the Ministry of Health of China under Grant No. 2017ZX10303401-002.

## References

[1] J. Goldenberg, B. Libai, E. Muller, Talk of the network: A complex systems look at the underlying process of word-of-mouth, Marketing letters, 12 (2001) 211-223.

[2] S. Goel, A. Anderson, J. Hofman, D.J. Watts, The structural virality of online diffusion, Management Science, 62 (2015) 180-196.

[3] M. Granovetter, Threshold models of collective behavior, American journal of sociology, (1978) 1420-1443.

[4] Y.-M. Li, C.-Y. Lai, L.-F. Lin, A diffusion planning mechanism for social marketing, Information & Management, 54 (2017) 638-650.

[5] H.W. Hethcote, The mathematics of infectious diseases, SIAM review, 42 (2000) 599-653.

[6] M.E. Newman, The structure and function of complex networks, SIAM review, 45 (2003) 167-256.

[7] J. Yang, J. Leskovec, Modeling information diffusion in implicit networks, in: Data Mining (ICDM), 2010 IEEE 10th International Conference on, IEEE, 2010, pp. 599-608.

[8] S. Gomez, A. Diaz-Guilera, J. Gomez-Gardeñes, C.J. Perez-Vicente, Y. Moreno, A. Arenas, Diffusion dynamics on multiplex networks, Physical review letters, 110 (2013) 028701.

[9] T. Gross, B. Blasius, Adaptive coevolutionary networks: a review, Journal of the Royal Society Interface, 5 (2008) 259-271.

[10] G. Kossinets, D.J. Watts, Empirical analysis of an evolving social network, science, 311 (2006) 88-90.

[11] M. McPherson, L. Smith-Lovin, J.M. Cook, Birds of a feather: Homophily in social networks, Annual review of sociology, (2001) 415-444.

[12] R. Gutiérrez, A. Amann, S. Assenza, J. Gómez-Gardenes, V. Latora, S. Boccaletti, Emerging meso-and macroscales from synchronization of adaptive networks, Physical review letters, 107 (2011) 234103.

[13] G.G. Turrigiano, S.B. Nelson, Homeostatic plasticity in the developing nervous system, Nature Reviews Neuroscience, 5 (2004) 97-107.

[14] E.M. Rogers, Diffusion of innovations, Simon and Schuster, 2010.

[15] G. Appa Rao, E.M. Rogers, S. Singh, Interpersonal relations in diffusion of an innovation in two Indian Villages, Indian journal of extension education, (1980).

[16] P. DiMaggio, F. Garip, How network externalities can exacerbate intergroup inequality, American Journal of Sociology, 116 (2011) 1887-1933.

[17] V. Palchykov, K. Kaski, J. Kertész, A.-L. Barabási, R.I. Dunbar, Sex differences in intimate relationships, Scientific reports, 2 (2012).

[18] R.I. Dunbar, Neocortex size as a constraint on group size in primates, Journal of Human Evolution, 22 (1992) 469-493.

[19] L. Weng, A. Flammini, A. Vespignani, F. Menczer, Competition among memes in a world with limited attention, Scientific reports, 2 (2012).

[20] X. Liu, Q. Ye, The different impacts of news-driven and self-initiated search volume on stock prices, Information & Management, 53 (2016) 997-1005.

[21] S.J. Correll, C.L. Ridgeway, Expectation states theory, in: Handbook of social psychology, Springer, 2006, pp. 29-51.

[22] K. Kirst-Ashman, Human Behavior in the Macro Social Environment, Cengage Learning, 2010.

[23] A. Ooyen, Competition in the development of nerve connections: a review of models, Network: Computation in Neural Systems, 12 (2001) 1-47.

[24] A. Van Ooyen, Using theoretical models to analyse neural development, Nature Reviews Neuroscience, 12 (2011) 311-326.

[25] D.V. Papero, Bowen family systems theory, Prentice Hall, 1990.

[26] A. Jain, E.Y. Chang, Y.-F. Wang, Adaptive stream resource management using kalman filters, in: Proceedings of the 2004 ACM SIGMOD international conference on Management of data, ACM, 2004, pp. 11-22.

[27] L. Li, B.A. Prakash, C. Faloutsos, Parsimonious linear fingerprinting for time series, Proceedings of the VLDB Endowment, 3 (2010) 385-396.

[28] Y. Tao, C. Faloutsos, D. Papadias, B. Liu, Prediction and indexing of moving objects with unknown motion patterns, in: Proceedings of the 2004 ACM SIGMOD international conference on Management of data, ACM, 2004, pp. 611-622.

[29] Y. Meyer, D.H. Salinger, Wavelets and operators, Cambridge university press, 1995.

[30] R. Bracewell, The fourier transform and iis applications, New York, 5 (1965).

[31] W. Dai, D. Han, Y. Dai, D. Xu, Emotion recognition and affective computing on vocal social media, Information & Management, 52 (2015) 777-788

[32] R.M. May, Qualitative stability in model ecosystems, Ecology, (1973) 638-641.

[33] F. Brauer, C. Castillo-Chavez, C. Castillo-Chavez, Mathematical models in population biology and epidemiology, Springer, 2001.

[34] Y. Matsubara, Y. Sakurai, W.G. Van Panhuis, C. Faloutsos, FUNNEL: automatic mining of spatially coevolving epidemics, in: Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2014, pp. 105-114.

[35] T. Rakthanmanon, B. Campana, A. Mueen, G. Batista, B. Westover, Q. Zhu, J. Zakaria, E. Keogh, Searching and mining trillions of time series subsequences under dynamic time warping, in: Proceedings of the 18th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2012, pp. 262-270.

[36] J. Yang, J. McAuley, J. Leskovec, P. LePendu, N. Shah, Finding progression stages in time-evolving event sequences, in: Proceedings of the 23rd international conference on World wide web, ACM, 2014, pp. 783-794.

[37] C. Böhm, C. Faloutsos, C. Plant, Outlier-robust clustering using independent components, in: Proceedings of the 2008 ACM SIGMOD international conference on Management of data, ACM, 2008, pp. 185-198

[38] D. Chakrabarti, S. Papadimitriou, D.S. Modha, C. Faloutsos, Fully automatic cross-associations, in: Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2004, pp. 79-88.

[39] P. Holme, Network reachability of real-world contact sequences, Physical Review E, 71 (2005) 046119.

[40] M. Valencia, J. Martinerie, S. Dupont, M. Chavez, Dynamic small-world behavior in functional brain networks unveiled by an event-related networks approach, Physical Review E, 77 (2008) 050905.

[41] J. Tang, S. Scellato, M. Musolesi, C. Mascolo, V. Latora, Small-world behavior in time-varying graphs, Physical Review E, 81 (2010) 055101.

[42] J. Stehlé, A. Barrat, G. Bianconi, Dynamical and bursty interactions in social networks, Physical review E, 81 (2010) 035101.

[43] H.A. Simon, Designing organizations for an information-rich world, Computers, Communication, and the Public Interest, (1971).

[44] L. Coviello, Y. Sohn, A.D. Kramer, C. Marlow, M. Franceschetti, N.A. Christakis, J.H. Fowler, Detecting emotional contagion in massive social networks, PloS one, 9 (2014) e90315.

[45] J.D. Murray, Mathematical Biology II: Spatial Models and Biomedical Applications, Intercisciplinary Applied Mathematics: Mathematical Biology. Springer, 2001.

[46] M. Salathé, S. Khandelwal, Assessing vaccination sentiments with online social media: implications for infectious disease dynamics and control, PLoS Comput Biol, 7 (2011) e1002199.

[47] Y. Liang, X. Zhou, D.D. Zeng, B. Guo, X. Zheng, Z. Yu, An integrated approach of sensing tobacco-oriented activities in online participatory media, (2014).

[48] M. Vlachos, G. Kollios, D. Gunopulos, Discovering similar multidimensional trajectories, in: Data Engineering, 2002. Proceedings. 18th International Conference on, IEEE, 2002, pp. 673-684.

[49] J. Gómez-Gardenes, Y. Moreno, A. Arenas, Paths to synchronization on complex networks, Physical review letters, 98 (2007) 034101.

[50] S. He, X. Zheng, D. Zeng, C. Luo, Z. Zhang, Exploring Entrainment Patterns of Human Emotion in Social Media, PloS one, 11 (2016) e0150630.

[51] J. Ferlez, C. Faloutsos, J. Leskovec, D. Mladenic, M. Grobelnik, Monitoring network evolution using MDL, in: Data Engineering, 2008. ICDE 2008. IEEE 24th International Conference on, IEEE, 2008, pp. 1328-1330.

[52] C. Böhm, C. Faloutsos, J.-Y. Pan, C. Plant, RIC: Parameter-free noise-robust clustering, ACM Transactions on Knowledge Discovery from Data (TKDD), 1 (2007) 10.

[53] CDC, Measles Cases and Outbreaks, in, Centers for Disease Control and Prevention, 2015.

[54] WHO, Ebola virus disease, in, World Health Organization, 2015.

[55] P. Galewitz, Here’s what you need to know about new e-cig regulations, in, The Washington Post, 2016.

[56] Y. Yamamoto, Twitter4J-A java library for the twitter API, in, sep, 2014.

[57] B. Pang, L. Lee, A sentimental education: Sentiment analysis using subjectivity summarization based on minimum cuts, in: Proceedings of the 42nd annual meeting on Association for Computational Linguistics, Association for Computational Linguistics, 2004, pp. 271.

[58] C.-C. Chang, C.-J. Lin, LIBSVM: a library for support vector machines, ACM Transactions on Intelligent Systems and Technology (TIST), 2 (2011) 27.

[59] A. Beider, Beider-Morse phonetic matching: An alternative to Soundex with fewer false hits, Avotaynu: the International Review of Jewish Genealogy, (2008).

[60] S. Bird, E. Klein, E. Loper, Natural language processing with Python, " O'Reilly Media, Inc.", 2009.

[61] L. Barbosa, J. Feng, Robust sentiment detection on twitter from biased and noisy data, in: Proceedings of the 23rd International Conference on Computational Linguistics: Posters, Association for Computational Linguistics, 2010, pp. 36-44.

[62] D. Davidov, O. Tsur, A. Rappoport, Enhanced sentiment learning using twitter hashtags and smileys, in: Proceedings of the 23rd international conference on computational linguistics: posters, Association for Computational Linguistics, 2010, pp. 241-249.

[63] S. He, X. Zheng, D. Zeng, A model-free scheme for meme ranking in social media, Decision support systems, 81 (2016) 1-11.

[64] S. He, X. Zheng, J. Wang, Z. Chang, Y. Luo, D. Zeng, Meme Extraction and Tracing in Crisis Events, in: IEEE Intelligence and Security Informatics 2016 Conference (ISI 2016), Tucson, Arizona USA, 2016.

[65] L. Carretié, F. Mercado, M. Tapia, J.A. Hinojosa, Emotion, attention, and the ‘negativity bias’, studied through event-related potentials, International journal of psychophysiology, 41 (2001) 75-85.

![](/api/attachments/RMNMA8HF/fulltext/images/7aa75db3c87b042a6d9f8f52381da866767a75e6f014480c8ad5489f292f79e1.jpg)  
Biography

and M.S. degree in computer science and B.S. degree in automation in 2010 and 2007, respectively, from the Beijing University of Posts and Telecommunications, Beijing, China.

His research interest includes natural language processing, behavior modeling, information diffusion, and synchronization in complex networks. To date, Saike He has published 3 journal papers and 21 conference papers, including one Best Paper Runner-up Award at ISI 2016. Saike He has also won the championships of the Big Data Analytics Contest in China (2016), Massive Short Text Analytics Contest in China (2014), NTCIR-8 MOAT Evaluation (2010), and CIPS-CLPE: Bakeoff-4 (2007)

![](/api/attachments/RMNMA8HF/fulltext/images/3ac475152beee6f5922b8bf10560e7569fdbf822766cd6e661c15bafba703ff2.jpg)

Xiaolong Zheng is currently an Associate Professor at the Institute of Automation, Chinese Academy of Sciences. He received Ph.D. degree from the Institute of Automation, Chinese Academy of Sciences, in 2009, M.S. degree from Beijing Jiaotong University in 2006, and B.S. degree from China Jiliang University in 2003. Xiaolong Zheng has published more than 100 peer-to-peer academic papers in journals/magazines and conferences. Xiaolong Zheng has served as the Program Co-chair of The 2017 IEEE International Conference on Intelligence and Security Informatics (IEEE ISI 2017), International conference for Smart Health (ICSH 2014), Pacific Asia Workshop on Intelligence and Security Informatics 2013 (PAISI 2013), and Pacific Asia Workshop on Intelligence and Security Informatics 2011 (PAISI 2011). He also served as Academic Secretary of ACM Social and Economic Computing Chapter from 2012 to 2013, Associate Editor

of Security Informatics, and Technical Program Committee Member for more than 30 international conferences.

![](/api/attachments/RMNMA8HF/fulltext/images/f4bd0927e70026ce56a90046430cc43966909316d92e82d4462ed0b0afc92351.jpg)

Daniel Zeng (M’04–SM’07) received Ph.D. degree in industrial administration from Carnegie Mellon University in 1998.

He is a research professor at the Institute of Automation, Chinese Academy of Sciences, Beijing, China, and is also affiliated with the University of Arizona, Tucson, AZ, USA. His current research interests include software agents and multiagent systems, intelligence and security informatics, social computing, and recommendation systems.
