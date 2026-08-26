---
otero_id: 16568
otero_key: "FV2CU5GY"
title: "Visual analytics of set data for knowledge discovery and member selection support"
authors: "Ryuji Watanabe; Hideaki Ishibashi; Tetsuo Furukawa"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113635"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Visual analytics of set data for knowledge discovery and member selection support

Ryuji Watanabe<sup>a</sup>, Hideaki Ishibashi<sup>a</sup>, Tetsuo Furukawa<sup>a,∗</sup>

<sup>a</sup>Kyushu Institute of Technology, 2–4 Hibikino, Wakamatsu-ku, Kitakyushu 808-0196, Japan

## Abstract

Visual analytics (VA) is a visually assisted exploratory analysis approach in which knowledge discovery is executed interactively between the user and system in a human-centered manner. The purpose of this study is to develop a method for the VA of set data aimed at supporting knowledge discovery and member selection. A typical target application is a visual support system for team analysis and member selection, by which users can analyze past teams and examine candidate lineups for new teams. Because there are several dificulties, such as the combinatorial explosion problem, developing a VA system of set data is challenging. In this study, we first define the requirements that the target system should satisfy and clarify the accompanying challenges. Then we propose a method for the VA of set data, which satisfies the requirements. The key idea is to model the generation process of sets and their outputs using a manifold network model. The proposed method visualizes the relevant factors as a set of topographic maps on which various information is visualized. Furthermore, using the topographic maps as a bidirectional interface, users can indicate their targets of interest in the system on these maps. We demonstrate the proposed method by applying it to basketball teams, and compare with a benchmark system for outcome prediction and lineup reconstruction tasks. Because the method can be adapted to individual application cases by extending the network structure, it can be a general method by which practical systems can be built.

Keywords: Visual analytics, Set data, Manifold modeling, Team formation support, Interactive visualization

## 1. Introduction

Decision-making in member selection is dificult when we need to consider the combination efect of members. A typical example is member selection in team formation [1, 2, 3], where we need to consider the synergy between members [4, 5, 6]. Another example is fashion outfit selection, where we need to select items, considering coordination [7]. The purpose of this study is to develop a method for supporting knowledge discovery and member selection using a visual analytics (VA) approach.

VA is a visually assisted exploratory knowledge discovery process from a dataset, whereby users can explore data, examine hypotheses, gain knowledge, make predictions, and make decisions [8, 9]. Such human-centered knowledge discovery is performed as an interaction between the user and VA system, where the system visualizes the analysis results according to the user’s request, and the user feeds back its analysis intention, such as the target of interest (TOI) to the system. Through such an interactive loop, the VA system supports users in gaining a deeper insight into the data. The scope of VA is not limited to the analysis of past data, but also includes the prediction of new cases, whereby users can examine candidate options for decision-making.

The purpose of this study is to develop a general method for the VA of set data, which aims to support knowledge discovery from member set data, and support decision-making in member selection. A typical example is VA for sports teams (i.e., sets of athletes), whereby team managers can analyze the strength and weakness of past teams, as well as examine new lineups for future games. The VA approach is suitable for such management issues because it aims to support users in making decisions by themselves rather than discovering an optimal solution automatically on behalf of users. Thus, VA allows users to integrate their empirical domain knowledge with knowledge obtained from the system, and it leaves the final decision to users. Furthermore, the VA system also supports users not only in understanding what will happen as a result of the decision, but also in discovering why it will happen. This is in contrast to the conventional black-box approach, which only aims to discover an optimal solution automatically.

Because there are several dificulties in handling set data, such as the combinatorial explosion problem, developing VA systems of set data is challenging. Thus, the goal of this study is to establish a general method for the VA of set data by which practical VA systems can be built, in particular, member selection support systems. The central issues of this study are (1) how the VA system should handle set data, (2) how the system should visualize the relation between relevant factors, such as the property of sets, their constituent elements, and output of the sets, (3) how the system should enable users to perform both exploratory analysis and prediction, (4) how the system should escape from the combinatorial explosion problem, and (5) how the system can be plastic so that it can be adapted to individual application cases. These five issues are the loci of interest of this paper.

The key idea of this study is to model the generation process of sets and their outputs from low-dimensional latent variables using a manifold network model (MNM). Thus, to represent the generation process of sets, we connect manifold models of sets and of elements serially, whereas we connect manifold models of relevant factors in parallel, to represent the generation process of outputs. Using the MNM, sets, elements, and relevant factors are visualized on a set of latent spaces, similar to a set of topographic maps. These topographic maps are used as the interactive visual interface in which users can specify their TOI, and on which the corresponding information is visualized. This scheme is depicted in Figure 1. The most important role of the target system is to help users to discover knowledge and hypotheses, and to consider team candidates through this interactive loop.

The structure of this paper is as follows: In Section 2, we introduce the background and related work. In Section 3, we define the requirements of the target system. In Sections 4 and 5, we present the framework and implementation of the proposed method. In Section 6, we demonstrate the proposed method by applying it to basketball team data. Finally, we present the discussion and conclusion in Sections 7 and 8.

## 2. Background and related work

## 2.1. Visual analytics

VA is a visually supported explanatory knowledge discovery process, or methods for the process. Keim et al. provided the definition of VA as follows: “Visual analytics combines automated analysis techniques with interactive visualizations for an efective understanding, reasoning and decision-making on the basis of very large and complex data sets” [8]. The essential property of VA is that analysts themselves are regarded as an important part of the analytics process [9]. VA has been introduced to various fields, for example, telecommunications [10], supply chain management [11], government [12], education [13], and healthcare [14].

![](/api/attachments/FV2CU5GY/fulltext/images/8896eefcd1eb1f9c401c86dc2f2c0a69eb14abd4ca05459c9650c6a8001ec6c7.jpg)  
Figure 1: Key concept of the proposed method. The data are modeled as an MNM which is visualized on a set of topographic maps. In the topographic maps, the analysis targets (e.g., teams, constituent members, and external conditions) are visualized as a mapping, similar to landmarks, whereas other information (e.g., outcome) is visualized using coloring, similar to contour maps. Users can indicate their TOI on the topographic maps, and the system visualizes the corresponding information by changing the color.

VA aims not only at the exploratory analysis of past data, but also exploratory prediction for future cases. VA that particularly aims at prediction is referred to as predictive VA (PVA) [15]. In PVA, it is more important to help users to gain comprehensive knowledge of the prediction model rather than simply improving prediction accuracy. Therefore, in the decisionmaking process, users can obtain knowledge about what will happen and why it will happen as a result of the decision, and can integrate their empirical domain knowledge and management issues to make the final decision. This is in contrast to the conventional black-box approach, which focuses on prediction accuracy. The scope of this study includes PVA of sets. Thus, our target system allows users to examine new sets (e.g., new teams) by predicting their output.

## 2.2. Handling a set of sets

When handling set data, there are several serious problems. First, the treatment of the sets should be invariant to the permutation of the elements. Additionally, the cardinality (number of elements) is not always equal [16].

Second, the topological space of sets is not continuous, and there is no trivial definition of distance between two sets. This is a serious problem regarding achieving generalization for unknown sets. Third, the sets are often accompanied by combinatorial explosion problems.

In the case of discriminative tasks, our aim is to estimate a function $f$ from the given dataset, which represents the input-output relation as $y =$ $f ( X )$ , where X is a set. This $f$ should satisfy permutation invariance under arbitrary cardinality. Furthermore, $f$ should be generalized for unknown X, which is not included in the given dataset. Because there is no general method to obtain such an f, it is a challenging issue in the machine learning field [17, 16].

By contrast, in the case of a generative task, our aim is to represent the probability of set X as $p ( X \mid \tau )$ , where τ is the parameter that determines the property of the set. Again, the generative model $p ( X \mid \tau )$ should satisfy permutation invariance. Although there is no established method, the most popular approach is to represent the generative model as $\begin{array} { r } { p ( X \mid \tau ) = \prod _ { i } p ( x _ { i } \mid } \end{array}$ $\tau )$ , where $X ~ = ~ \{ x _ { i } \}$ is regarded as a set of independent and identically distributed random variables [18, 19]. This approach is further categorized into two groups represented as $\begin{array} { r } { p ( x ~ \vert ~ \tau ) ~ = ~ \int p ( x ~ \vert ~ \mu , \tau ) p ( \mu ) d \mu ~ [ 1 9 ] } \end{array}$ and $\begin{array} { r } { p ( x \mid \tau ) = \int p ( x \mid \mu ) p ( \mu \mid \tau ) d \mu } \end{array}$ [18, 20], where $\mu$ is the latent variable that determines the probability density of the element. In this study, we use the latter approach.

For VA of set data, the system needs to visualize output y of set $X \ { \mathrm { ( e . g . } }$ outcome $y$ of team X), in addition to generating or suggesting X when the team property $\tau$ is specified. Thus, VA systems of set data need to equip three functions simultaneously: (i) predict the output for a given set (discriminative task/forward problem), (ii) generate new sets that satisfy the specified property (generative task/inverse problem), and (iii) visualize the property of various sets and their compositions (visualization task). Therefore, VA systems of sets sufer from dificulties in both discriminative and generative tasks, in addition to dificulties in visualization. Because equipping these three functions is a strict requirement, and they sometimes conflict with each other, these dificulties are the reason that few studies have been conducted on the VA of set data.

## 2.3. Member selection support for team management

Decision-making in team formation and member selection is an important and dificult task; therefore, it is important to support it [21, 22]. In most studies, researchers have aimed to identify the optimal team lineup that maximizes the outcome by solving the combinatorial problem [1, 2]. In this group of studies, the outcome was predicted by a function of the member lineup as $y = f ( X )$ , which was often defined a priori. Note that this approach only provides an optimal solution as a black-box system. In another group of studies, researchers aimed to evaluate members to determine or recommend suitable members for the team [4, 23, 24]. Thus, they focused on individual members rather than a combination of members.

Several studies on VA have been conducted in the team management field. Zhao et al. proposed a VA system for evaluating employee performance [25]. Ryoo et al. applied VA to soccer players, which aimed to support player transfer between clubs [26]. These studies were mainly focused on individual members rather than member combinations. Some other studies focused on the operation of teams, such as member collaboration [27]. However, few studies have been conducted on VA for member selection that considers member combinations.

## 3. Requirements of the target system

In this section, we clarify the requirements that the VA system of set data should satisfy. Before considering general cases, we first imagine a case in which a team manager needs to determine members of a team. (For more practical cases, see [28].) To achieve this, the manager first needs to know what types of candidates the organization has. The manager needs to consider not only the abilities of individual candidates, but also their mutual influence, such as synergy. It would be also useful to know what types of teams have been formed and how many outcomes they have achieved. In some cases, the manager also needs to consider some extra factors, such as risks, costs, and external conditions. In the team sports case, the lineup of the opposing team is also an important factor. Considering these entangled factors, the manager needs to examine the candidate lineups, compare them, and then choose one of them. After the decision is made, the manager is also asked to account for the decision.

Using the above scenario as a working assumption, we define the requisites that the target VA system should satisfy. First, the system needs to handle teams, that is, a set of members. More precisely, the system should be able to execute bidirectional mapping between teams and their properties. Thus, by specifying a lineup of a team, the system needs to estimate the property of the team, and estimate how many outcomes are expected (i.e., forward problem). Simultaneously, by specifying a property of a team, or specifying an expected outcome, the system needs to recommend lineups that satisfy the condition (i.e., inverse problem). Second, the system is required to unravel entangled factors, such as member ability, team property, other extra factors, and the outcome (i.e., disentanglement problem). Third, it is desirable that the system provides a table-top field where the manager can examine new lineups. It is also desirable to predict what will happen as a result of the decision and show why it will happen (i.e., analysis and prediction). Fourth, the system should free the manager from the individual consideration of candidate lineups by providing the manager with an overview of multiple lineups simultaneously at a glance (i.e., visualization task).

These requirements are not limited to the team management case, but are generally necessary for the VA system of set data. The above requirements are translated as follows: (1) Clearly, the VA system of set data should be able to handle sets. Thus, the system should be capable of bidirectional (i.e., forward and inverse) mapping between a given set and its property. (2) The VA system of set data should support users in both intra-domain and inter-domain analysis. Particularly, the system is required to unravel the entangled relation of relevant factors using inter-domain visualization. (3) The system should be able to support both the analysis of past data and prediction of future cases. For this purpose, the system needs to obtain the predictive model from past data. (4) The system is required to eliminate the combinatorial explosion problem from which users sufer. Thus, it is desirable for the system to visualize the output of various sets simultaneously to provide users with an overview of them at a glance.

Additionally, we add an extra requirement for the development method: the method should allow us to design VA systems flexibly so that they can adapt to individual cases. Because the input (available dataset) and output (visualized aspects that the user wants to see) are diferent for each case, even if they are in the same application field, such generality is required for the development method. Additionally, the VA process itself is dynamic [9]; after obtaining some insights or hypotheses, it is often necessary for the user to perform further analysis from a diferent viewpoint, by adding a new dataset, or by visualizing additional aspects. Therefore, it is desirable for VA systems to be both adaptable and expandable. In this study, this is referred to as the plasticity requirement.

Our aim in this study is to establish a general method for constructing VA systems of set data that satisfies these five requirements. To the best of our knowledge, no studies have tackled these issues, presumably because of the dificulties of handling sets in VA systems.

## 4. Framework of the proposed method

## 4.1. Manifold assumption

For the system to escape from the combinatorial explosion problem, the exploration space must be restricted. Additionally, the system needs to estimate the predictive model from the limited number of past data, which do not cover the possible combinations exhaustively. Therefore, we use the manifold assumption in this study, which is common in the VA field [9]. Thus, we postulate that meaningful team compositions are distributed in low-dimensional space. More properly, we suppose a continuous topological space of team compositions $\mathcal { P }$ in which the distance between two teams is defined. Then we assume that the team compositions that are worth considering are in a low-dimensional manifold in ${ \mathcal { S } } ^ { ( \mathrm { t } ) } \subseteq { \mathcal { P } }$ , whereas all other compositions are not of interest. This assumption allows us to restrict the exploration space within the manifold, and allows us to visualize team compositions more easily. Additionally, the assumption also means that team compositions that were observed in the past are distributed in the manifold, whereby the system becomes able to estimate the predictive model from a non-exhaustive dataset. Because two-dimensional space is convenient for visualization, we further assume that we are interested in the two-dimensional principal dimensions of the manifold. Under this assumption, we can define a bidirectional mapping between $\mathcal { S } ^ { ( \mathrm { t } ) }$ and the latent space $\mathcal { L } ^ { \mathrm { ( t ) } }$ , which is used for visualization. Thus, we can define a bijection $\pi \colon \mathcal { L } ^ { ( \mathrm { t } ) }  \mathcal { S } ^ { ( \mathrm { t } ) }$ , whereby a team at $\tau \in \mathcal { L } ^ { ( \mathrm { t } ) }$ is mapped to ${ \mathcal S } ^ { ( \mathrm { t } ) } \ni q _ { \tau } = \pi ( \tau )$ , and vice versa. This bijection π plays an essential role in bidirectional exploration in the VA system.

Similarly, we also assume that member properties are distributed in low (typically two)-dimensional manifolds in their feature space. Thus, we assume that the member feature vectors are distributed in manifold ${ \mathcal { S } } ^ { ( \mathrm { m } ) } \subseteq { \mathcal { C } }$ ${ \mathcal { O } } ^ { ( \mathrm { m } ) }$ where ${ \mathcal { O } } ^ { ( \mathrm { m } ) }$ is the vector space of member features. Then we can define the homeomorphic latent space $\mathcal { L } ^ { ( \mathrm { m } ) }$ , and a bidirectional mapping $g \colon { \mathcal { L } } ^ { ( \mathrm { m } ) }  { \mathcal { S } } ^ { ( \mathrm { m } ) }$ , whereby a member at $\mu \in \mathcal { L } ^ { ( \mathrm { m } ) }$ is mapped to the feature space as $\mathbf { x } = g ( \mu )$ , and vice versa. Similarly, we assume the manifolds of extra factors. For example, when we need to consider an external condition, manifold ${ \mathcal S } ^ { \mathrm { ( c ) } } \subseteq { \mathcal O } ^ { \mathrm { ( c ) } }$ and the latent space $\mathcal { L } ^ { \mathrm { ( c ) } }$ can be defined, in addition to the bijection $h \colon { \mathcal { L } } ^ { \mathrm { ( c ) } }  \mathcal { S } ^ { \mathrm { ( c ) } }$

The manifold assumption results in another benefit: it allows us to represent the member composition of a team as a probability density in the member latent space $\mathcal { L } ^ { ( \mathrm { m } ) }$ as $p ( \mu )$ . Thus, the team composition space $\mathcal { P }$ is defined as the function space that consists of the probability densities on $\mathcal { L } ^ { ( \mathrm { m } ) }$ . Therefore, in our method, teams are treated as probability densities instead of discrete sets. This approach allows us to measure the distance between two teams and generate new lineups. This is the key idea for handling sets in the proposed method.

![](/api/attachments/FV2CU5GY/fulltext/images/55ff0da4aaea0e4864bb7568acc5fd78e24114ddab7b4134f2fbd257353d847d.jpg)

Figure 2: Conceptual diagrams of the traditional (a) and proposed $( \mathrm { b } , \mathrm { c } , \mathrm { d } )$ approaches. Circles represent the latent variables. (a) Traditional optimization approach. (b) Generative model approach using the team latent variable τ . (c) Generative model approach with external conditions. (d) Generative model of sport teams in a match.  
![](/api/attachments/FV2CU5GY/fulltext/images/3f4a79e14e6b729107bffe52d307d53f9d2c8f7d31796584b4517f1ad9ac97bf.jpg)  
Figure 3: Generative model of team lineup X from the team latent variable τ . The variables indicated by circles are latent, and the box indicates that the generative process repeats n times.

## 4.2. Framework of the proposed method

Now we formulate the framework of the proposed approach. Let Ω be the total set of members. A team that consists of n members is represented as a set $T = \{ \omega _ { 1 } , \ldots , \omega _ { n } \}$ , where $\omega _ { i } \in \Omega$ . In this paper, T is referred to as the lineup of the team. Let $\mathfrak { T }$ be the set of all lineups<sup>1</sup>. Thus $\mathfrak { T }$ is a set of sets. Note that the order of the members is not fixed generally. Let $\mathbf { x } ( \omega ) \in \mathcal { O } ^ { ( \mathrm { m } ) }$ be the feature vector of member $\omega ,$ which represents the property of the member, such as ability. Then we have a set of feature vectors with respect to lineup T : $X _ { T } = \{ \mathbf { x } ( \omega _ { 1 } ) , \dots , \mathbf { x } ( \omega _ { n } ) \}$ . Because $T$ and $X _ { T }$ are often identified, we also refer to $X _ { T }$ as the lineup.

In a conventional framework, we typically assume that the outcome $y$ is determined as a function of $X _ { T }$ , say $y = f ( X _ { T } )$ . Simply speaking, a typical traditional task is to identify the optimal lineup $T _ { \mathrm { o p t } } \in \mathfrak { T }$ that maximizes the outcome $y \ ( \mathrm { F i g u r e \ 2 \ ( a ) } )$ . Note that outcome y should be scalar in this approach. Additionally, f is typically given or designed by authors.

By contrast, the proposed framework assumes that both lineup X and outcome y (which can be vectors in our case) are generated from the latent variable $\tau \in \mathcal { L } ^ { ( \mathrm { t } ) }$ , which represents the intrinsic property of the team (Figure $2 \ ( \mathrm { b } ) )$ . Thus, the outcome is generated as $\mathbf { y } = f ( \tau )$ from $\tau$ instead of from lineup X directly. Unlike the conventional framework, $f$ is not given a priori, but is estimated in a data-driven manner. Note that outcome $\mathbf { y } \in \mathcal { O } ^ { ( \mathrm { o } ) }$ is distributed in a manifold ${ \mathcal { S } } ^ { ( \mathrm { o } ) } \subseteq { \mathcal { O } } ^ { ( \mathrm { o } ) }$ . Parallel to the outcome, τ also generates a probability density $q ( \mu \mid \tau ) \equiv q _ { \tau } ( \mu )$ , which represents the member composition of the team. Thus, the generative model of team lineups is represented as

$$
q (X \mid \tau) = \prod_ {i} \int \mathcal {N} (\mathbf {x} _ {i} \mid g (\mu), \beta^ {- 1} \mathbf {I}) q _ {\tau} (\mu) d \mu ,\tag{1}
$$

where $q _ { \tau } = \pi ( \tau )$ , and $\beta ^ { - 1 }$ is the variance (I is the unit matrix) (Figure 3). Conversely, when a lineup $X ~ = ~ \{ \mathbf { x } _ { 1 } , \ldots , \mathbf { x } _ { n } \}$ is given, the corresponding latent variable $\tau ( X )$ is determined as

$$
\tau (X) = \underset {\tau} {\arg \min} D _ {\mathrm{KL}} \left[ p (\mu \mid X) \| q _ {\tau} (\mu) \right],\tag{2}
$$

where $p ( \mu \mid X )$ is given by the kernel density estimator, and $D _ { \mathrm { K L } }$ is the Kullback–Leibler (KL) divergence. Such bidirectional mapping allows bidirectional exploration between the team latent variable and lineups, and it is an advantage of this method.

![](/api/attachments/FV2CU5GY/fulltext/images/3f260f49faac2c6bc60d971bf0466f9920d8f93bc5d6c3518cfe3f2eb50a6928.jpg)  
Figure 4: Generative model and the structure of the proposed method for the scenario of Figure 2 (c). The MNM consisting of four manifold models corresponding to the four outputs, and consisting of three topographic maps corresponding to the three latent spaces.

This generative model can easily adapt to any scenario in which some additional factors are to be considered. If we need to consider an external condition, then the model is extended by adding another latent variable $\xi \in \mathcal { L } ^ { \mathrm { ( c ) } }$ , which represents the intrinsic property of the condition. In this case, the expected outcome is predicted as $\mathbf { y } = f ( \tau , \xi )$ (Figure 2 (c)). Another typical case is sport teams in a match, where victory or defeat depends on the latent variables of both teams, such as $\mathbf { y } = f ( \tau _ { A } , \tau _ { B } )$ (Figure 2 (d)).

In our approach, the entire generative model becomes a network of manifold models, that is, the MNM. Figure 4 shows the network structure of the MNM, when an external condition is considered (Figure 2 (c)). In the MNM, the generation process of lineups is represented by a serial connection of two manifold models $\mathcal { S } ^ { ( \mathrm { t } ) }$ and $\mathcal { S } ^ { ( \mathrm { m } ) }$ via latent space $\dot { \mathcal { L } } ^ { ( \mathrm { m } ) }$ , whereas the outcomes and relevant factors are modeled by the parallel connection of manifolds $\mathcal { S } ^ { ( \mathrm { t } ) }$ $\mathcal { S } ^ { \mathrm { ( c ) } }$ , and $\mathcal { S } ^ { ( \mathrm { o } ) }$ via latent spaces $\mathcal { L } ^ { \mathrm { ( t ) } }$ and $\mathcal { L } ^ { \mathrm { ( c ) } }$ . Because the network structure can be adapted to individual application cases, the proposed framework satisfies the plasticity requirement.

## 4.3. Definition of the learning task

In our framework, the manifold models are estimated in a data-driven manner. In the following, we clarify what the method needs to estimate from the given dataset when external conditions are considered (Figure 4). Suppose that the given dataset consists of $N ^ { \mathrm { ( t ) } }$ lineups $\mathfrak { L } = \{ T _ { i } \} _ { i = 1 } ^ { N ^ { ( \mathrm { t } ) } }$ , with $N ^ { ( \mathrm { m ) } }$ members $\mathbf { X } = \left( \mathbf { x } _ { j } \right) _ { j = 1 } ^ { N ^ { \left( \mathrm { m } \right) } }$ , under $N ^ { \mathrm { ( c ) } }$ external conditions ${ \bf Z } = ( { \bf z } _ { k } ) _ { k = 1 } ^ { N ^ { \mathrm { ( c ) } } }$ , where

$T _ { i } \in \mathfrak { T } , \mathbf { x } _ { j } \in \mathcal { O } ^ { ( \mathrm { m } ) }$ , and $\mathbf { z } _ { k } \in \mathcal { O } ^ { \mathrm { ( c ) } }$ . Furthermore, let $\mathbf { Y } = ( \mathbf { y } _ { n } ) _ { n = 1 } ^ { N ^ { ( \mathrm { o } ) } } , \mathbf { y } _ { n } \in \mathcal { O } ^ { ( \mathrm { o } ) }$ be the outcome data observed from the combinations of $\left\{ ( T _ { i ( n ) } , { \bf z } _ { k ( n ) } ) \right\} _ { n = 1 } ^ { N ^ { ( \mathrm { o } ) } }$ Note that it is not necessary to cover all combinations, and missing combinations are allowed. Under such a dataset, the task of the proposed method is to estimate the mappings $f , g , h$ , and $\pi ,$ in addition to estimating the latent variables ${ \bf T } = \left( \tau _ { i } \right) _ { i = 1 } ^ { N ^ { ( \mathrm { t } ) } } , { \bf M } = \left( \mu _ { j } \right) _ { j = 1 } ^ { N ^ { ( \mathrm { m } ) } }$ , and $\Xi = \left( \xi _ { k } \right) _ { k = 1 } ^ { N ^ { \mathrm { ( c ) } } }$

## 5. Implementation

## 5.1. Generative manifold modeling

As described above, the core idea of our proposed approach is to represent the generative model using the MNM. To achieve this, we adopt generative manifold modeling (GMM) as a building block in the implementation. Thus, the MNM is estimated by the network of GMM. This is the key idea of the implementation.

The term GMM in this paper refers to the paradigm of unsupervised learning, which aims to model the given dataset using a manifold. For this purpose, GMM estimates a map from low-dimensional latent space to highdimensional data space, in addition to estimating the low-dimensional latent variable for each sample. After learning is complete, GMM allows users to conduct both retro- and anterograde surveys, that is, analysis and prediction. This is why we use GMM in our method. The representatives of GMM are the Gaussian process latent variable model (GPLVM) [29], and unsupervised kernel regression (UKR) [30].

Let $\mathbf { \boldsymbol { \mathcal { O } } } = \mathbb { R } ^ { D }$ and $\mathcal { L } = \mathbb { R } ^ { d }$ be high-dimensional observable space and lowdimensional latent space, respectively. For a high-dimensional dataset $\mathbf { X } =$ $( { \bf x } _ { 1 } , \dots , { \bf x } _ { N } ) ^ { \top } \in \mathbb { R } ^ { N \times D }$ , the task of GMM is to estimate the corresponding latent variables $\\Xi = ( \xi _ { 1 } , \ldots , \xi _ { N } ) \in \mathbb { R } ^ { N \times d }$ , and represent the mapping $f \colon { \mathcal { L } } $ O as $\mathbf { x } = f ( \xi \mid \Xi )$ . For this purpose, GPLVM uses the Gram matrices of observed data $\mathbf { \dot { S } } = \mathbf { X } \mathbf { X } ^ { \top }$ and of latent variables $\mathbf { K } ~ = ~ \left( k _ { i j } \right)$ , where $k _ { i j } \equiv$ $k ( \zeta _ { i } , \zeta _ { j } )$ is the kernel function. The objective function of GPLVM is defined as

$$
F _ {\mathrm{GPLVM}} (\boldsymbol {\Xi} \mid \mathbf {X}) = - \frac {N D}{2} \ln 2 \pi - \frac {D}{2} \ln | \hat {\mathbf {K}} | - \frac {1}{2} \mathrm{Tr} \left[ \hat {\mathbf {K}} ^ {- 1} \mathbf {S} \right],\tag{3}
$$

and (the mean of) the mapping is determined by $\begin{array} { r } { f ( \xi \mid \Xi ) = \mathbf { k } ( \xi ) ^ { \top } \hat { \mathbf { K } } ^ { - 1 } \mathbf { X } } \end{array}$ where $\hat { \mathbf { K } } = \mathbf { K } + \beta ^ { - 1 } \mathbf { I }$ and $\mathbf { k } ( \xi ) = ( k ( \xi , \xi _ { i } ) ) _ { i = 1 } ^ { N }$ , and $\beta ^ { - 1 }$ is the variance. An advantage of using GPLVM is that we obtain not only the average mapping $f ( \xi \mid \Xi )$ , but also its variance $\sigma ( \xi , \xi ^ { \prime } )$ , which represents uncertainty. By contrast, the objective function of UKR is defined as

$$
F _ {\mathrm{UKR}} (\boldsymbol {\Xi} | \mathbf {X}) = - \frac {\beta}{2} \sum_ {i} \left\| f (\xi_ {i}) - \mathbf {x} _ {i} \right\| ^ {2},\tag{4}
$$

and the mapping is determined as $\begin{array} { r } { f ( \xi \mid \Xi ) = \frac { 1 } { K ( \xi ) } \sum _ { j = 1 } ^ { N } k ( \xi , \xi _ { j } ) \mathbf { x } _ { j } } \end{array}$ , where $\begin{array} { r } { K ( \xi ) = \sum _ { j = 1 } ^ { N } k ( \xi , \xi _ { j } ) } \end{array}$ . An advantage of UKR is that it can deal with a set of probability distributions as a dataset. In this case, the Euclidean distance in (4) is replaced by the KL divergence. We use GPLVM for modeling the outcome predictor $f ,$ whereas we use UKR for modeling the team composition generator π.

## 5.2. Estimation of the manifold network model using GMM

The structure of the MNM consists of four types of connections: (a) mapping from a latent space to the counterpart manifold (e.g., mapping g from $\mathcal { L } ^ { ( \mathrm { m } ) }$ to $\mathcal { S } ^ { ( \mathrm { m } ) }$ in Figure 4); (b) serial connection between the manifold of sets and the latent space of elements $( \mathrm { i . e . }$ , the link between $\mathcal { L } ^ { ( \mathrm { m } ) }$ and ${ \mathcal S } ^ { ( \mathrm { t } ) } )$ (c) mappings from a latent space to two (or more) manifolds $( \mathrm { e . g . }$ , mappings π and $f ,$ from $\mathcal { L } ^ { \mathrm { ( t ) } }$ to $\mathcal { S } ^ { ( \mathrm { t } ) }$ and ${ \mathcal S } ^ { ( \mathrm { o } ) } )$ ; and (d) mappings from two (or more) latent spaces to a manifold (e.g., mapping $f ,$ from $\bar { \mathcal { L } } ^ { ( \mathrm { t } ) }$ and $\mathcal { L } ^ { \mathrm { ( c ) } }$ to ${ \mathcal S } ^ { ( \mathrm { o } ) } )$ . These links are estimated by GMM as follows:

(a) To estimate a mapping from a latent space to the counterpart manifold, ordinary GMM (either GPLVM or UKR) can be used.

(b) To transform a team composition from team manifold ${ \mathcal S } ^ { ( \mathrm { t } ) }$ to the lineup in member latent space $\mathbf { \mathcal { L } ^ { ( m ) } }$ , member latent variables are generated by the team composition $q ( \mu \mid \tau )$ . By contrast, from $\mathcal { L } ^ { ( \mathrm { m ) } } \mathrm { ~ \bar {  t o } ~ } \mathcal { S } ^ { ( \mathrm { t } ) }$ , a team lineup $X = \{ \mathbf { x } _ { 1 } , \ldots , \mathbf { x } _ { n } \}$ is transformed to the team composition as $\begin{array} { r } { p _ { X } ( \mu ) ~ = ~ { \frac { 1 } { n } } \sum _ { i } k ( \mu ~ \vert ~ g ^ { - 1 } ( \mathbf { x } _ { i } ) ) ~ } \end{array}$ using the kernel density estimator. If the lineup is defined by a weighted set, then it becomes $p _ { X } ( \mu ) =$ $\begin{array} { r } { \frac { 1 } { W } \sum _ { i } w _ { i } k ( \mu \mid g ^ { - 1 } ( { \bf x } _ { i } ) ) } \end{array}$ , where $w _ { i }$ is the weight of the i-th member, and $\begin{array} { r } { \dot { W } = \sum _ { i } w _ { i } } \end{array}$ . For example, in the sports game case, weight $w _ { i }$ can be defined by the playing time of the i-th athlete.

(c) To estimate mappings from a latent space to two manifolds, two objective functions of GMM are summed with the weight coeficient as $\alpha _ { 1 } F _ { 1 } +$ $\alpha _ { 2 } F _ { 2 }$ . In this study, the coeficients $\alpha _ { i }$ are determined so that the average norms of the gradient vectors are approximately equal.

![](/api/attachments/FV2CU5GY/fulltext/images/559e3c92f96dbc3e7d1ac9dc8fce37601d8bd7095a97ce56f85a8cfa7131c906.jpg)  
Figure 5: Visual analytics system for the NBA dataset.

(d) To estimate a mapping from two latent spaces to a product manifold, the joint kernel function is defined as the product of two kernels. Thus, the kernel function for f is defined as $k ( \tau , \xi , \tau ^ { \prime } , \xi ^ { \prime } ) \equiv k ( \tau , \tau ^ { \prime } ) \times k ( \xi , \xi ^ { \prime } )$

In the case of Figure 4, the objective functions of four GMM blocks are integrated into the following two objective functions:

$$
F (\mathbf {M}) = F ^ {(\mathrm{m})} (\mathbf {M} \mid \mathbf {X}),\tag{5}
$$

$$
F (\mathbf {T}, \boldsymbol {\Xi}) = \alpha_ {1} F ^ {(t)} (\mathbf {T} \mid P) + \alpha_ {2} F ^ {(c)} (\boldsymbol {\Xi} \mid \mathbf {Z}) + \alpha_ {3} F ^ {(o)} (\mathbf {T}, \boldsymbol {\Xi} \mid \mathbf {Y}),\tag{6}
$$

where $P = \{ p _ { i } ( \mu ) \}$ is the set of team compositions.

Regardless of the network structure, any MNM can be estimated by the combination of these four styles of GMM connections. Therefore, the plasticity requirement is also satisfied at the implementation level.

## 6. Demonstration of the proposed VA system

In this section, we demonstrate the proposed method by applying it to real team data, and show how the interactive analytics process can be executed using our system. We used basket team data from the National Basketball Association (NBA)<sup>2</sup>. The developed VA system is shown in Figure 5, which is based on the generative model shown in Figure 2 (d). In the proposed method, the latent spaces are visualized as square spaces, such as a set of topographic maps. In the case of the NBA dataset, the system has four topographic maps: own and opposing athlete maps, and own and opposing team maps. The own and opposing maps are essentially identical, and they can be colored diferently according to the TOI of users. In addition to these topographic maps, there are two bar charts that display the statistics of the athlete and team (i.e., the outcome), and pull-down menus that enable the user to select a stat to be visualized.

![](/api/attachments/FV2CU5GY/fulltext/images/70b5daa310d3cdc92ebfa526eca770c64a05d9292725c73b4fa7cb70546420bc.jpg)  
Figure 6: Visualization results of athletes and teams for the NBA dataset. (a) Athlete map: markers indicate the athletes and their positions, and the color scale indicates the number of ofensive rebounds per minute. (b) Team map: markers indicate the teams and the clubs to which they belong. The color scale shows the mean of the PTD.

Figure 6 shows the obtained athlete map and team map. In the athlete map, athletes are indicated as fixed points, like landmarks, so that athletes who have similar stats are arranged close to each other. This can be seen from the fact that the athletes are roughly divided according to their positions on the map. Similarly, teams are visualized as landmarks on the team map, in which teams that have similar stats are arranged close to each other.

In the case of real topographic maps, we can visualize additional information, such as altitudes and population density, using a contour map or heat map. In the same way, the topographic maps in our system can be colored according to one of the stats. In Figure 6 (a), the athlete map is colored according to the ofensive rebound per minute. When a user wants to see another stat (e.g., number of two-point goals attempted), the user selects the stat from the pull-down menu. In the same way, the team map (Figure 6 (b)) is colored according to the average point diference (PTD), which indicates the chance of winning (higher for the red region). If the user selects a stat from the pull-down menu, the system shows other stats on the map, which enables the user to analyze the strength and weakness of the teams.

![](/api/attachments/FV2CU5GY/fulltext/images/10da30a8931cd3e559de3ab32e64dc85fd1f357cb8096963d14cc064b8057efa.jpg)  
(a) Athlete stats

![](/api/attachments/FV2CU5GY/fulltext/images/fecf74e917f70d8c92ee6dcc38a89320f740676cffc8da1ec79d8181c5a79107.jpg)  
(b) Own athlete map

![](/api/attachments/FV2CU5GY/fulltext/images/c2eea416183ca5b795c3c1e0def11bff5c26ca534d425b3201d52078efbb4704.jpg)  
(c) Own team map

![](/api/attachments/FV2CU5GY/fulltext/images/d4e8a87aad5ad945c25d328b5ad822fd9ddd7c4dad98319a781495c789de3104.jpg)  
(d) Opposing team map  
Figure 7: Example of interactive visualization. The TOI is team ˆτ indicated on the own team map (c) by the user. The predicted PTD is shown on the opposing team map (d), which indicates that team ˆτ would defeat the opposing teams in the red region. Simultaneously, the member composition of the team p(µ | τˆ) is visualized on the athlete map (b). If the user selects one of the members (ˆµ), the stats of the member are indicated as a bar chart (a).

These topographic maps are used as the bidirectional visual interface by which the user can indicate its TOI in the system. Figure 7 shows an example of interactive analysis. Suppose that the TOI of the user is the team located at $\hat { \tau }$ on the own team map (c). If the user points to $\hat { \tau }$ on the map, the system visualizes the corresponding member composition $q ( \mu \mid \hat { \tau } )$ in grayscale on the athlete map (b), which shows the population density of team $\hat { \tau }$ on the athlete map. The user can further see the stats of each constituent member as a bar chart by pointing to it on the athlete map. Simultaneously, the system also visualizes the predicted game result such as the PTD on the opposing team map (d). Thus, the winning chance for team ˆτ is higher when it plays a game against the opposing teams indicated in the red region. This is achieved by visualizing $f ( \hat { \tau } , \tau _ { \mathrm { o p p } } )$ as the function of $\tau _ { \mathrm { o p p } }$ . Additionally, the confidence of the prediction can be indicated by the brightness of the color by visualizing $\sigma ( \hat { \tau } , \tau _ { \mathrm { o p p } } )$

As shown in the above example, the proposed system solves the forward and inverse problems seamlessly. We evaluated the accuracy of the forward problem using game result (i.e., winning/losing) prediction, and the system yielded 63% accuracy<sup>3</sup>, where the baseline was 50% (i.e., the chance level). For comparison, we constructed a “benchmark system” based on the average stats of members<sup>4</sup>, which yielded 56% accuracy. We also evaluated the accuracy of the inverse problem using the reconstruction error of member compositions. Thus, we evaluated the Jensen–Shannon (JS) divergence [32] between the test member composition $p _ { i } ^ { \mathrm { t e s t } } ( \mu )$ and the composition reconstructed from the model $q ( \mu | \tau _ { i } ^ { \mathrm { { \bar { t e s t } } } } )$ for each test lineup. The reconstruction error of the proposed method was 0.012, whereas the baseline was 0.24 (measured using the uniform distribution). For comparison, we also measured the JS divergence between the test lineups and the average member composition $\overline { { p } } ( \mu )$ , where $\begin{array} { r } { \overline { { p } } ( \mu ) = { \frac { 1 } { N ^ { ( \mathrm { t } ) } } } \sum _ { i } p _ { i } ^ { \mathrm { t r a i n i n g } } \bar { ( \mu ) } } \end{array}$ . It was 0.14, which means that the degree of lineup variety was much larger than the reconstruction error of the proposed system. Note that the reconstruction error of member compositions cannot be measured for methods that do not consider lineup sets, including the benchmark system.

Figure 8 shows an example of the member selection process assisted by the VA system. In this scenario, suppose that the opposing team is located at S on the opposing team map. If the user points to S, the system visualizes the predicted PTD on the own team map, thereby showing which own team may defeat the opposing team. Note that the user can view the predicted results of all teams on the team map simultaneously at a glance. By selecting a desired team (say, T that shows the highest PTD) as the TOI, the system visualizes the member composition on the own athlete map as grayscale. Thus, by selecting athletes from the high-density region in the athlete map, the member composition becomes roughly equal to the desired composition. The system can also visualize the past lineup that is closest to T . After the user determines a lineup, the system indicates the location of the lineup on the own team map (T <sup>0</sup>). If necessary, the user can modify the lineup by trial and error while monitoring the lineup on the own team map. In this process,

![](/api/attachments/FV2CU5GY/fulltext/images/bea67fa22b2e832bac120bb6333764dae7277b73b4f2fb5e91f1abe3f06bde82.jpg)

Figure 8: Example of the member selection process supported by the proposed VA system.  
![](/api/attachments/FV2CU5GY/fulltext/images/e095e38b6ac09aac26d687e797d4873892339495e5d36320bc0b91f7fab20427.jpg)  
Figure 9: Table-top simulation of new lineups. Nine members were already selected (indicated by $\bullet )$ , and the 10th member was selected. (a) Predicted PTD with respect to the 10th member when the team plays a game with team S in (c). $a , a ^ { \prime } .$ , and $a ^ { \prime \prime }$ are the tentative candidates (indicated by ◦). (b) $T , T ^ { \prime }$ , and $T ^ { \prime \prime }$ indicate the position of the team when one of $a , a ^ { \prime } .$ , and $a ^ { \prime \prime }$ is used, respectively. The color scale indicates the predicted PTD against team S. (c) The predicted PTD against team T .

it is easy for the user to consider other factors, such as empirical knowledge, which are not built into the system. As shown in this example, the system allows a point on the team map to be transformed into the corresponding member composition in the athlete map, and vice versa. Such bidirectional mapping between teams and member compositions plays an essential role in member selection support. This is the remarkable achievement of the proposed method.

Figure 9 shows another scenario in which the user already has a team consisting of nine members (indicated by black markers on the athlete map (a)), and tries to determine a new (i.e., 10th) member for the team. Additionally, suppose that the opposing team is located at $S$ on the opposing team map (c). In this scenario, the predicted PTD is visualized on the athlete map (a) as a function of the 10th member. Thus, the winning chance would be high/low if a member in the red/blue region is selected. Then, let $a , \ a ^ { \prime } .$ and $a ^ { \prime \prime }$ (white circles in the athlete map) be the candidates to be the 10th member. The corresponding teams T , $T ^ { \prime }$ , and $T ^ { \prime \prime }$ , respectively, are indicated on the own team map (b). On the own team map, the predicted PTD is also visualized as a heat map. Thus, the winning chance is higher than 50% for team $T ^ { \prime }$ , whereas it is less than 50% for team $T ^ { \prime \prime }$ . Figure 9 (c) shows the predicted PTD when team $T$ plays a game against various opposing teams. It shows that team $T$ may defeat the opposing teams in the red region. In the above scenario, the task of the user is to select one of the candidates for the given team. The VA system can also be used in the opposite case, in which the manager needs to determine a suitable team for a newly added member. Thus, the VA system can support managers in assigning a new member to an existing team.

Although only a few examples are provided above, they demonstrate the advantages of the proposed method. First, the system allows users to perform bidirectional exploration between a team property and member composition. For example, if a desired team is identified on the team map, the system visualizes the member composition on the athlete map. Conversely, if a lineup is provided, the system visualizes the position on the team map, as well as the predicted outcome. Second, the system allows users to indicate their TOI for each topographic map independently, which enables users to discover knowledge by unraveling the entangled factors. Third, the system allows users to perform analysis and prediction seamlessly. If a user selects an existing team or member as the TOI, the system shows the analysis result of past data, whereas the system predicts the result if the TOI did not exist in the past. Fourth, the system provides users with a bird’s-eye view by providing topographic maps. Users can compare all team compositions in the team manifold simultaneously at a glance, and one-by-one comparison is not necessary. These four advantages correspond to the four requirements that we defined for the target system. In addition to these, the system has the advantages of the VA approach. Thus, it allows users to explore huge complex data interactively; it leaves the final decision to users; it allows users to make decisions together with considering their empirical knowledge or other factors that are not built in the system; and users can be accountable for their decisions.

Note that the aim of this study is not to develop the demonstrated VA system; rather, our aim is to develop a general method for constructing such VA systems of set data. As already described, the proposed method allows developers to extend and adapt the system flexibly. Such plasticity is the advantage of the proposed approach as a system development method.

## 7. Discussion

## 7.1. Evaluation and the five requirements

Generally, the evaluation of a VA system is dificult, and there is no established protocol for evaluation [9]. For an application-specific VA system, the system is usually evaluated using case studies, user studies, and expert reviews. If the study aims at developing a visual interface, then the operability is evaluated in subject experiments, whereas if the study aims at improving performance, then the system should be compared with other systems. By contrast, if the study aims at solving theoretical problems, the method should be evaluated logically to determine whether the problems are solved rather than using experiments. Because this study corresponds to the last case, we defined the five requirements as the criteria for evaluation.

There may be a concern about the validity of these requirements. We can show that they are necessary conditions by considering what occurs if one or more requirements are not satisfied. In such a case, it is obvious that the system does not work as a VA system of set data anymore, or its ability is crucially limited. If either the first or fourth requirement is not achieved, the system cannot be used as a VA system of set data anymore. If the second requirement is not achieved, then the system can visualize only a limited aspect of the given data, and it cannot unravel the entangled factors anymore. If the third requirement is not achieved, the system cannot be used for decision-making for future cases. Clearly, each application requires additional requirements that are specific to the domain. To satisfy applicationspecific requirements, we highlight the importance of the fifth requirement. In this study, we focused on solving theoretical problems regarding handling set data. Evaluation using other criteria is our future task. Particularly, evaluation of operability and usefulness from the human-centered viewpoint is an important issue in the VA field.

## 7.2. Extensions of the proposed method

To apply the proposed system to practical cases, the VA system needs to be adapted according to cases; thus, plasticity is necessary. The key idea of this method is to model the generation process using the MNM, the structure of which is easy to adapt according to the data structure. In an implementation, the MNM can be estimated using combinations of GMM, where four connection styles are used consistently. Therefore, the proposed method can be adapted flexibly according to application cases. Because the MNM can be regarded as a Bayesian network model of manifolds, the method can be said to be universal rather than general. Although we have not programmed yet, it is possible to develop a software library so that the network structure can be extended incrementally on demand. Such ondemand plasticity would make the analytics process more dynamic.

This method also allows us to develop an integrated VA system by combining other analysis methods because topographic maps can be used as platforms on which various analysis results are visualized. For example, the results of PCA or factor analysis can be visualized on the maps. In this case, users only need to select those components as their TOI from the component list (i.e., the pull-down menu). Similarly, the outputs of other black-box systems can be visualized on the topographic maps.

For team formation support, it is easy to extend the method to cases in which the roles of members are given (e.g., positions in basketball, such as point guard and center). In this case, the team composition is represented by the joint probability of the member latent variable and role as $q ( \mu , \rho \mid \tau )$ where $\rho$ represents the role. This extension would also be useful when the method is applied to a fashion outfit, in which the member and role are translated to a fashion item and category (e.g., shirts, pants, and coats) [7].

When new data are incrementally added over time, the proposed system can be updated by applying online learning. In this case, the members and teams are not fixed landmarks anymore; rather, they become ‘moving objects’ in the topographic maps. For example, if the athlete stats are obtained for every month, then the stats vector and corresponding latent variable become time series ${ \bf x } _ { i } ( t )$ and $\mu _ { i } ( t )$ , respectively. When we want to consider the latest performance of members, such an extension would be useful.

## 8. Conclusion

In this paper, we proposed a method for VA systems of set data that satisfies five requirements. Because there are dificulties in handling set data, our proposed method is the first attempt to tackle these issues. The proposed method represents complex data using a network of manifold models, the structure of which can be flexibly extended according to the data structure. Therefore, we have proposed a general method for constructing VA systems of set data rather than a specific system for team management.

In this work, we assumed that member selection support for team formation is a representative application, and demonstrated it by applying the proposed method to basketball team data. Although we still need to evaluate whether the method reaches a satisfactory level for team management, the concept of VA is more suited to such management issues than the conventional black-box approach. Therefore, we hope that this study will contribute not only to the VA field, but also the team management field as a methodology for a decision support system.

## Acknowledgements

This work was supported by JSPS KAKENHI [grant numbers 18K11472, 21K12061 and 20K19865] and ZOZO Research. We would like to thank Prof. D. Jahng from Kyushu Institute of Technology, Prof. H. Isogai from Kyushu Sangyo University, and Dr. T. Ohkubo from ZOZO Technologies for their valuable advice. We thank Mr. K. Senoura, who contributed to the preliminary stage of this study.

## References

[1] J. Moreno, D. A. Ovalle, R. M. Vicari, A genetic algorithm approach for group formation in collaborative learning considering multiple student characteristics, Computers & Education 58 (1) (2012) 560–569.

[2] M. A. P´erez-Toledano, F. J. Rodriguez, J. Garc´ıa-Rubio, S. J. Iba˜nez,<sup>´</sup> Players’ selection for basketball teams, through performance index rating, using multiobjective evolutionary algorithms, PLOS ONE 14 (9) (2019) e0221258.

[3] F. Rahmanniyay, A. J. Yu, A multi-objective stochastic programming model for project-oriented human-resource management optimization, International Journal of Management Science and Engineering Management 14 (4) (2019) 231–239.

[4] J. Calder, I. Durbach, Decision support for evaluating player performance in rugby union, International Journal of Sports Science and Coaching 10 (2015) 21–38.

[5] B. Travassos, Davids, D. Araujo, P. Esteves, Performance analysis in team sports: Advances from an ecological dynamics approach, International Journal of Performance Analysis in Sport 13 (2013) 89–95.

[6] D. Ara´ujo, K. Davids, Team synergies in sport: Theory and measures, Frontiers in Psychology 7 (2016) 1449.

[7] Y. Li, L. Cao, J. Zhu, J. Luo, Mining fashion outfit composition using an end-to-end deep learning approach on set data, IEEE Transactions on Multimedia 19 (8) (2017) 1946–1955.

[8] D. Keim, G. Andrienko, J.-D. Fekete, C. G¨org, J. Kohlhammer, G. Melan¸con, Visual Analytics: Definition, Process, and Challenges, Springer, Berlin, Heidelberg, 2008, pp. 154–175.

[9] W. Cui, Visual analytics: A comprehensive overview, IEEE Access 7 (2019) 81555–81573.

[10] B. Wu, Q. Ye, Y. Wang, R. Bi, L. Suo, D. Hu, S. Yang, Visual analysis of complex networks and community structure, in: Complex Sciences, Springer, Berlin, Heidelberg, 2009, pp. 2171–2183.

[11] H. Park, M. Bellamy, R. Basole, Visual analytics for supply network management: System design and evaluation, Decision Support Systems 91 (2016) 89–102.

[12] W. Didimo, L. Giamminonni, G. Liotta, F. Montecchiani, D. Pagliuca, A visual analytics system to support tax evasion discovery, Decision Support Systems 110 (2018) 71–83.

[13] H. Qu, Q. Chen, Visual analytics for mooc data, IEEE Computer Graphics and Applications 35 (6) (2015) 69–75.

[14] J. Caban, D. Gotz, Visual analytics in healthcare - opportunities and research challenges, Journal of the American Medical Informatics Association 22 (2) (2015) 260–262.

[15] Y. Lu, R. Garcia, B. Hansen, M. Gleicher, R. Maciejewski, The state-ofthe-art in predictive visual analytics, Computer Graphics Forum 36 (3) (2017) 539–562.

[16] J. Lee, Y. Lee, J. Kim, A. Kosiorek, S. Choi, Y. W. Teh, Set transformer: A framework for attention-based permutation-invariant neural networks, in: International Conference on Machine Learning, Vol. 97, 2019, pp. 3744–3753.

[17] M. Zaheer, S. Kottur, S. Ravanbakhsh, B. Poczos, R. R. Salakhutdinov, A. J. Smola, Deep sets, in: Advances in Neural Information Processing Systems, 2017, pp. 3391–3401.

[18] H. Edwards, A. Storkey, Towards a neural statistician, in: International Conference on Learning Representations, 2017.

[19] D. Bouchacourt, R. Tomioka, S. Nowozin, Multi-level variational autoencoder: Learning disentangled representations from grouped observations, in: AAAI Conference on Artificial Intelligence, 2017, pp. 2095– 2102.

[20] H. Ishibashi, T. Furukawa, Hierarchical tensor SOM network for multilevel–multigroup analysis, Neural Processing Letters 47 (3) (2018) 1011–1025.

[21] J. Mathieu, T. Maynard, T. Rapp, L. Gilson, Team efectiveness 1997- 2007: A review of recent advancements and a glimpse into the future, Journal of Management 34 (3) (2008) 410–476.

[22] S. T. Bell, S. G. Brown, J. A. Weiss, A conceptual framework for leveraging team composition decisions to build human capital, Human Resource Management Review 28 (4) (2018) 450–463.

[23] O. Uzochukwu, P. Enyindah, A machine learning application for football players’ selection, International Journal of Engineering Research & Technology 4 (10) (2015) 459–465.

[24] S. B. Jayanth, A. Anthony, G. Abhilasha, N. Shaik, G. Srinivasa, A team recommendation system and outcome prediction for the game of cricket, Journal of Sports Analytics 4 (4) (2018) 263–273.

[25] J. Zhao, M. Karimzadeh, L. Snyder, C. Surakitbanharn, Z. Qian, D. Ebert, Metricsvis: A visual analytics system for evaluating employee performance in public safety agencies, IEEE Transactions on Visualization and Computer Graphics 26 (1) (2020) 1193–1203.

[26] M. Ryoo, N. Kim, K. Park, Visual analysis of soccer players and a team, Multimedia Tools and Applications 77 (12) (2018) 15603–15623.

[27] Y. Wu, X. Xie, J. Wang, D. Deng, H. Liang, H. Zhang, S. Cheng, W. Chen, Forvizor: Visualizing spatio-temporal team formations in soccer, IEEE Transactions on Visualization and Computer Graphics 25 (1) (2019) 65–75.

[28] A Guide to the Project Management Body of Knowledge (PMBOK), 6th Edition, Project Management Institute, 2017.

[29] N. Lawrence, Probabilistic non-linear principal component analysis with gaussian process latent variable models, Journal of Machine Learning Research 6 (2005) 1783–1816.

[30] P. Meinicke, S. Klanke, R. Memisevic, H. Ritter, Principal surfaces from unsupervised kernel regression, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (9) (2005) 1379–1391.

[31] T. Horvat, J. Job, The use of machine learning in sport outcome prediction: A review, Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery 10 (5) (2020) e1380.

[32] J. Lin, Divergence measures based on the shannon entropy, IEEE Transactions on Information Theory 37 (1) (1991) 145–151.
