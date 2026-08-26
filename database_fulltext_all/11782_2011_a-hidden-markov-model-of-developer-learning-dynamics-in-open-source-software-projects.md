---
otero_id: 11782
otero_key: "6XSTPGUN"
title: "A Hidden Markov Model of Developer Learning Dynamics in Open Source Software Projects"
authors: "Param Vir Singh; Yong Tan; Nara Youn"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0308"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/6XSTPGUN/fulltext/images/cd668faf168f21471c3aadbe0f489f64ceaad70446536182913b7579c14f8068.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Hidden Markov Model of Developer Learning Dynamics in Open Source Software Projects

Param Vir Singh, Yong Tan, Nara Youn,

## To cite this article:

Param Vir Singh, Yong Tan, Nara Youn, (2011) A Hidden Markov Model of Developer Learning Dynamics in Open Source Software Projects. Information Systems Research 22(4):790-807. http://dx.doi.org/10.1287/isre.1100.0308

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/6XSTPGUN/fulltext/images/52ded04b737ae87d08fa644458123ca4f7f5a97cb5021658484d94e25b7bef6e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

http://dx.doi.org/10.1287/isre.1100.0308 © 2011 INFORMS

# A Hidden Markov Model of Developer Learning Dynamics in Open Source Software Projects

Param Vir Singh

Tepper School of Business, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, psidhu@cmu.edu

Yong Tan

Foster School of Business, University of Washington, Seattle, Washington 98195, ytan@u.washington.edu

Nara Youn

School of Business, Hongik University, Seoul 121-791, Korea, nara@hongik.ac.kr

his study develops a stochastic model to capture developer learning dynamics in open source software Tprojects (OSS). A hidden Markov model (HMM) is proposed that allows us to investigate (1) the extent to which individuals learn from their own experience and from interactions with peers, (2) whether an individual’s ability to learn from these activities varies as she evolves/learns over time, and (3) to what extent individual learning persists over time. We calibrate the model based on six years of detailed data collected from 251 developers working on 25 OSS projects hosted at Sourceforge. Using the HMM, three latent learning states (high, medium, and low) are identified, and the marginal impact of learning activities on moving the developer between these states is estimated. Our findings reveal different patterns of learning in different learning states. Learning from peers appears to be the most important source of learning for developers across the three states. Developers in the medium learning state benefit the most through discussions that they initiate. On the other hand, developers in the low and the high states benefit the most by participating in discussions started by others. While in the low state, developers depend entirely upon their peers to learn, whereas in the medium or high state, they can also draw upon their own experiences. Explanations for these varying impacts of learning activities on the transitions of developers between the three learning states are provided. The HMM is shown to outperform the classical learning curve model. The HMM modeling of this study contributes to the development of a theoretically grounded understanding of learning behavior of individuals. Such a theory and associated findings have important managerial and operational implications for devising interventions to promote learning in a variety of settings.

Key words: hidden Markov model; learning curve; productivity; learning by doing, learning from peers; open source software; dynamic models; structural models; regime switching models; behavior dynamics

History: Ram Gopal, Senior Editor; Indranil Bardhan, Associate Editor. This paper was received on January 9, 2009, and was with the authors 6 months for 2 revisions. Published online in Articles in Advance November 18, 2010.

## 1. Introduction

Understanding how an individual’s skills and efficiency evolve over time through learning is key to the strategic management of a firm. Learning has become an important construct to understand in business because of its effects on firm competitive advantage. The objective of this study is to present a model that captures the heterogeneous development of an individual’s skill and expertise over time through learning activities and allows for the dynamic classification of individuals based on their unobserved learning patterns. We propose a hidden Markov model (HMM)<sup>1</sup> to offer an approach for capturing learning dynamics, and we apply the model to the case of open source software (OSS) projects to show model performance. This empirical application stresses the value of the suggested model as an addition to the existing learning curve literature and also as an introduction of a new approach to analyzing developer behavior in the field of information systems. Our modeling framework allows us to investigate the influence of developer participation history in the project on her code contribution behavior. Two types of participation, coding experience and peer interactions, are considered. We calibrate the model on six years of detailed data collected from 251 developers working on 25 OSS projects hosted at Sourceforge.

Most empirical efforts to date measure the impact of learning in the context of manufacturing (Argote et al. 2003). This work makes the important contribution of studying learning dynamics in the context of

OSS development. Many commercial firms today are inclined to utilize and contribute to OSS resources. Hence, there is huge potential to address managerial issues pertaining to increasing developer competence in OSS projects that are of value to firms. An underlying motivation behind OSS developers’ participation is their desire to learn, i.e., to enhance their knowledge and skills through participation in OSS projects (Mehra et al. 2010). Learning creates a growing stock of knowledge and skills that can be applied in the future to improve productivity (Argote and Epple 1990, Mukhopadhyay et al. 2011). Developers build long-term capabilities through participation in OSS that can be transferred to new environments, resulting in increased job wages (Mehra et al. 2010, Lerner and Tirole 2002). Hence, a potential way to influence developer behavior and motivate contributions is to provide a richer environment for developer learning in an OSS project.

Although learning from one’s own experience and from peers has been studied in a commercial software development environment, prior research has not investigated learning in OSS environments. The effects of experience on developer productivity may differ between commercial and OSS development environments for several reasons. First, in a commercial software development environment, goals are clear, the division of labor is preassigned, actions to follow are specified in advance, and support processes are clearly defined. In contrast, OSS represents an ambiguous organizational setting where goals are often vague and shift over time and where code architecture evolves in an unstructured way, resulting in variation in the meaning and utility of knowledge across time and space, with no preset paths to solving a problem and ill-defined support processes (Raymond 1998). Second, there is significant diversity in the knowledge and skills of developers attracted to OSS and their joining times. Hence, OSS developers might differ in their abilities and preferences regarding learning from different activities (Cohen and Levinthal 1990). Third, whereas prior research does not account for the depreciation of learning in software development (Boh et al. 2007), it is important to consider this in an OSS environment, as OSS development is a part-time activity for most developers. An OSS developer might remain absent for extended periods during her involvement in the project. This might lead not only to the depreciation of developer knowledge but also to changes in the relevance of the possessed knowledge and skills, because the code could evolve through the contributions of her peers during her absence.

The proposed HMM has several advantages over the conventional learning curve framework. First, the

HMM allows the segmentation of developers according to their code contributions and learning abilities. This segmentation allows one to investigate the varying impacts of learning activities across groups of developers on subsequent learning and code contributions. It provides insight into the strategic targeting of developers at different skill or expertise levels to effectively induce higher coding competency. This cannot be done in the standard learning curve framework. Second, existing learning research assumes a static model of worker contribution behavior that might lead to erroneous estimates of the impact of participation in learning activities if the code contribution behavior of developers evolves dynamically. The way the existing learning curve literature incorporates the learning effect is by allowing productivity to change with cumulative experience, which entails a static model of behavior. The parameters of the learning curve model are constant and are not allowed to vary over time. The HMM provides a simple and flexible way to account for the possibility of change in task-relevant behavior based on learning by explicitly specifying the structural dynamics. We compare our model with the standard learning curve framework. The results indicate that the HMM more appropriately explains the data.

Third, Dutton and Thomas (1984) did a metaanalysis of more than 200 learning curve studies and emphasized the importance of contingency variables that affect the learning rate. In our setting, the contingency is the amount of skills and knowledge that the developers possess at any point in time (Cohen and Levinthal 1990). In a learning curve model, accounting for this contingency would require several interactions of a priori unknown structural form between the existing knowledge and skills of a developer and present participation levels in learning activities. HMM provides an easy and flexible way to account for this contingency by making the learning from an activity dependent on the learning state of the developer. Finally, our HMM allows for depreciation of knowledge and skills, which is a critical aspect to incorporate into any learning model but hasn’t been fully addressed in the context of software development.

The rest of the paper is organized as follows. In §2, we present the theoretical background. The HMM for analyzing developer learning is laid out in §3. Section 4 explains the data collection methodology. The description of the variables and the estimation procedure are presented in §§5 and 6, respectively. The results from the HMM are discussed in §7. Section 8 offers concluding remarks.

2. Literature and Theory Development In this section, we draw upon the vast prior literature to develop a theory of learning dynamics for

OSS environments. We first determine the factors that affect developer productivity. Then, we build a theory to explain why participation in learning activities (one’s own experience and peer interactions) have the potential to affect developer productivity.

## 2.1. Factors That Affect Developer Productivity

Rodney et al. (1994) state that relevant variance in worker productivity in a specific task environment can be explained by two factors: (1) declarative knowledge (DK) and (2) procedural knowledge and skills (PKS). DK represents knowing what to do: knowledge of facts, rules, principles, and procedures. PKS represent knowledge about how to perform a task and the ability to do so (Kanfer 1990). According to this framework, a situation (activity) can influence differences in worker productivity only by influencing DK and PKS. The learning curve literature investigates how experience or training affects productivity by influencing DK and PKS (Argote et al. 1990). Although learning curves have been found in many organizations (Epple et al. 1996, Argote et al. 1990, Dutton and Thomas 1984, Reagans et al. 2005), the individuals in these organizations were involved in repetitive tasks.

Software development activities, although not entirely repetitive, require a considerable amount of abstract, technical, theoretical and experiential knowledge (Sacks 1994). Prior research suggests that the processes that lead to creation of new knowledge, embodied in complex artifacts such as software, most often involve a recombination of known conceptual and physical materials (Fleming 2001). Critical inputs into these processes are understanding and knowledge of current design problems, existing related solutions, novel approaches to solve these problems, and failed approaches. Also essential are related technical skills in areas such as relationships among data items, algorithms, the invocation of functions, and code architecture, among others (Fleming 2001, Grewal et al. 2006, Sacks 1994, Singh 2010, Singh et al. 2007). Through involvement in software development activities, a developer could build her own knowledge repositories, which can be applied in related situations in the future (Basili and Caldiera 1995, Sacks 1994). However, some knowledge might also become irrelevant because of new advancements or significant contributions to the code by peers. It might also depreciate because of forgetting as a result of inactivity on the part of a developer.

## 2.2. Effect of Learning Activities on Developer Productivity

Developers are endowed with a certain amount of DK and PKS when they join an OSS project. The initial endowment of an individual could be attenuated or accentuated by subsequent experiences with the same or related processes (Heckman 1991). The DK and PKS of an individual might also affect her ability to identify and assimilate knowledge from the environment, which would further affect her productivity (Cohen and Levinthal 1990). Furthermore, the knowledge and skills of an individual could influence the generation of task-specific behavior (Campbell and Prichard 1976).

2.2.1. Own Experience. One’s own experience primarily affects both DK and PKS. Expertise in programming is known to produce an orderof-magnitude improvement in program efficiency (Brooks 1987). In any innovative process like software development, technical problems are solved through an adaptive process (Sacks 1994). Such an adaptive process involves a person’s undertaking a course of action, the environment’s producing a result, and the person’s updating her course of action to increase her probability of achieving her goals (Van de Ven and Polley 1992). By solving technical problems or developing code, a developer acquires knowledge of not only what works in a given situation but also what does not work in such a situation. The more a developer participates in such activities, the richer her repositories of such knowledge become, and this knowledge can be applied in future. Personal experience may also affect the knowledge of a developer by introducing her to data sets, relationships among data items, algorithms, the invocation of functions, and code architecture, among others (Brooks 1987).

2.2.2. Peer Interactions. Extant research on learning from others focuses on the facilitating role of transfer mechanisms, conduits, or agents through which the transfer of knowledge takes place (Darr et al. 1995). In general, the literature suggests that higher levels of use of transfer mechanisms are associated with increased levels of knowledge transfers. The transfer mechanism particularly relevant in the present study is interaction with peers. At the group level, information can be distributed across individuals, and individual members can draw upon social cognition to solve problems (Larson and Christensen 1993). Several studies have identified that knowledge is shared through peer interactions among OSS developers (Grewal et al. 2006, Singh and Tan 2009, Singh 2010, Singh et al. 2011, Singh and Phelps 2009).

Interactions with peers are an important source of learning for developers in an OSS project for several reasons. First, these interactions allow opportunities for resource pooling, knowledge spillovers, and sharing alternative interpretations of design problems. A developer can draw upon the knowledge repositories of her peers in solving a problem. Second, these interactions help in coordinating the development effort, which could minimize effort duplication, besides updating the community about recent advancements to the code (Kraut and Streeter 1995, Singh et al. 2011). Third, interaction with peers provides opportunities for a developer to apply her efforts or knowledge to different but related problem domains (in which her peers might be having problems) and, in the process, to develop a deeper cognitive understanding of both (Schilling et al. 2003).

## 2.3. Hidden Markov Model for Developer Learning in OSS

Based on the above discussions, it is clear that a comprehensive model of developer learning in OSS should (1) be able to capture the change in developer code contribution behavior as a result of participation in learning activities, (2) account for the relevant knowledge and the skill set of a developer insofar as it influences her ability to identify, assimilate and exploit knowledge from the environment, and (3) allow for depreciation in DK and PKS. To operationalize these aspects of learning, we propose an HMM that uses individual participation history in order to analyze the learning dynamics of OSS developers. An HMM consists of two things: finite set of hidden states and observed outcome. A hidden state corresponds to a unique outcome. Transitions from one state to another follow a Markov process.

In our HMM, for lack of a more appropriate term, we call the hidden states learning states. The space of a state is spanned by latent skill and knowledge factors (DK and PKS). All other things being equal, each learning state corresponds to a unique code contribution behavior. This can be easily explained because each learning state represents a particular skill level that is a very important input in programmer productivity. The conceptualization of a learning state with unique contribution behavior allows us the ability to capture dynamics in developer code contribution behavior. At any given point in time, a developer resides in only one state. She can transition from one state to another through participation in learning activities, some of which are observed, over a given period. The Markovian transitions account for the dependence of subsequent learning on the present learning state of a developer. This dependence allows for the relevant knowledge and skills of a developer to affect her ability to identify and assimilate knowledge from the environment. Furthermore, the transition of a developer from one state to another captures the change in code contribution behavior of developer as each state corresponds to a unique code contribution behavior. We adapt and extend the HMM in several important ways. First, the probabilities to transition from one state to another are structurally determined as a function of a developer’s observed level of participation in learning activities as well as unobserved random factors. This allows for the transition probability from a given state to another to be different across developers as well as across time periods for the same developer. Second, the observed outcome in our HMM is the amount of code contributed which is structurally determined as a function of observed developer and product characteristics, project life-cycle effects, and unobserved random factors. Given a state, this allows the code contributions to vary across developers as well as across time periods for the same developer.

Our HMM works as follows. In period t, a developer probabilistically belongs to a learning state based on her skills and knowledge stock, 1 being the lowest learning state and n being the highest. The extent of her participation in learning activities in t determines whether she will either move up to a higher state, stay where she is, or move down to a lower state in the next period t + 1. Then, her realized learning state in period t + 1 probabilistically determine her levels of code contribution. She again engages in learning activities at t + 1 that will lead her to move to the next learning state at t. Figure 1 graphically illustrates how the HMM developers’ transitions between learning states through participation in various learning activities and how their coding probabilities depend on the learning states.

In this way, the learning process is structurally modeled through an integrated framework that links the unobserved but evolving latent state of learning with the realized outcomes of learning—developer code contributions. Through this model, we investigate the impact of learning activities that affect the transitions of a developer between the hidden states. The model allows us to probabilistically identify the learning state of a developer and investigate the impact of learning activities in moving the developer to a different state without observing the direct measure of skill and knowledge levels (which would require primary data collection). This improved methodology utilizes massively available secondary data and effectively discovers learning dynamics.

Figure 1 Hidden Markov Model of Developer Learning in OSS  
![](/api/attachments/6XSTPGUN/fulltext/images/8a924e698707aba3c47eeeb8e97fe1ad53d68149cf43972cedc72d33c541e219.jpg)

Figure 2 Conceptual Research Framework  
![](/api/attachments/6XSTPGUN/fulltext/images/d7ed0da08bedb93724b645e31f62e68e680ea0323b83c47608be05c6a3eb000c.jpg)

Figure 2 summarizes our conceptual research framework. Our framework consists of two parts. In part one, the learning activities determine the present learning state moderated by the past learning state. In part two, the developer characteristics, project characteristics and project life-cycle controls determine productivity moderated by the present learning state. The specific relationships and associations we test are depicted by arrows in Figure 2. First, we investigate the extent to which developers’ own coding experience in the project and interactions with peers impact learning across different states. Second, we estimate how the developer and project characteristics, as well as the project life-cycle controls, determine developer productivity in the different learning states of the developers. Third, we segment developers based on their learning states. Neither the number of learning states nor to which state a developer belongs at any time are a priori defined; instead, they are empirically recognized post hoc.

## 3. Modeling Developer Learning Dynamics

Consider an OSS project. The entire time horizon starting from the inception of the project is divided into periods. For each period, we observe the factors that might affect the code contributions of the developer as well as her actual code contributions, if any. For any given period, a developer resides in an unknown learning state.

Given a set of learning states $s \in \{ 1 , 2 , \ldots , n \} .$ , where 1 is the lowest learning state and n the highest, and a sequence of observed contribution outcomes $O =$ $O _ { 1 } O _ { 2 } ^ { - } \cdot \cdot \cdot O _ { T } \ ( O _ { t } \in$ 8amount of code contributed9 in our model), the HMM comprises three elements: (i) the initial state distribution, ; (ii) the state-transition probability distribution, $Q ;$ and (iii) the observed outcome probability vector, A. An HMM requires the specification of n (number of states) and the three components $( \pi , Q , A )$ . For convenience, we use the following compact notation, $\lambda = ( \pi , Q , A )$ , to represent the complete parameter set of the model.

Consider, for developer i, a fixed state sequence $S ( i ) = S _ { i 1 } S _ { i 2 } \cdot \cdot \cdot S _ { i T } ,$ where $S _ { i 1 }$ is the initial state for developer i and $S _ { i t } \in \{ 1 , 2 , \dots , n \} _ { }$ , and an observed outcome sequence $O ( i ) = O _ { i 1 } O _ { i 2 } \cdot \cdot \cdot O _ { i T }$ . The probability that we observe the outcome sequence O4i5 given the state sequence S4i5 and the parameter set  is

$$
P (O (i) \mid \lambda , S (i)) = \prod_ {t = 1} ^ {T} P (O _ {i t} \mid \lambda , S _ {i t}).
$$

Then we obtain

$$
P (O (i) \mid \lambda , S (i)) = a (O _ {i 1} \mid S _ {i 1}) \cdot a (O _ {i 2} \mid S _ {i 2}) \dots a (O _ {i T} \mid S _ {i T}),
$$

where $a ( O _ { i t } \mid S _ { i t } )$ is the probability of observing contribution outcome $O _ { i t }$ given that developer i is in state $S _ { i t }$ at time t. Note that $a ( O _ { i t } \mid S _ { i t } )$ is an element of the contribution probability vector, $A ( i , t )$

The probability of a state sequence S4i5 is given by

$$
P (S (i) \mid \lambda) = \pi (i) q (S _ {i 1}, S _ {i 2}) \dots q (S _ {i t}, S _ {i t + 1}) \dots q (S _ {i T - 1}, S _ {i T}),
$$

where $\pi ( i )$ is the initial probability that developer i is in state $S _ { i 1 }$ in period $t \doteq 1 . \ q ( S _ { i t } , \mathbf { \bar { { S } } } _ { i t + 1 } )$ is the probability that developer i is in state $S _ { i t + 1 }$ in period $t + 1$ given that she was in state $S _ { i t }$ in period t. Note that $q ( S _ { i t } , S _ { i t + 1 } )$ is an element of the state transition matrix $Q ( i , t , t + 1 )$ for developer i.

The probability that $\bar { O } ( i )$ and S4i5 occur simultaneously is

$$
P (O (i), S (i) \mid \lambda) = P (O (i) \mid \lambda , S (i)) P (S (i) \mid \lambda).\tag{1}
$$

Hence, the probability of the observed outcome sequence $O ( i )$ given the model parameter set  is the likelihood of observing this sequence and is obtained by summing Equation (1) over all possible values of state sequence $\hat { S } ( i )$ (Rabiner 1989):

$$
L (O (i)) = P (O (i) \mid \lambda) = \sum_ {\forall S (i)} P (O (i) \mid \lambda , S (i)) P (S (i) \mid \lambda).
$$

The individual likelihood can be written in more compact matrix notation (MacDonald and Zucchini 1997):

$$
\begin{array}{c} L (O (i)) = \pi (i) \Lambda (i, 1) Q (i, 1, 2) \Lambda (i, 2) \\ \cdot Q (i, 2, 3) \dots Q (i, T - 1, T) \Lambda (i, T) \mathbf {1} ^ {\prime}. \end{array}\tag{2}
$$

Here, the matrix $\Lambda ( i , t ) = \mathrm { d i a g } ( a ( O _ { i 1 } \mid S _ { i t } = 1 ) , a ( O _ { i 1 } \mid S _ { i t }$ $= 2 ) , \dots , a ( O _ { i 1 } \mid S _ { i t } = n ) )$ , and 1 is a n × 1 vector of ones. The model parameters $Q , A ,$ and  to obtain the likelihood of the observed outcome sequence $L ( O ( i ) )$ are defined in the following subsections.

## 3.1. State Transition Matrix

In our HMM, the transition between states is modeled as a random walk where only transitions to the adjacent states are allowed. The random walk assumption keeps the model parsimonious. However, this assumption can be easily relaxed by assigning nonzero probabilities to transitions to nonadjacent states. We allow transitions to lower states to account for forgetting and the temporal nature of the relevance of possessed knowledge and skills. Then the random walk state transition matrix is defined as follows:

Q4i1t1t +15

$$
= \left( \begin{array}{c c c c c c} q (1, 1) & q (1, 2) & 0 & \dots & 0 & 0 \\ q (2, 1) & q (2, 2) & q (2, 3) & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & \dots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & q (n, n - 1) & q (n, n) \end{array} \right).
$$

Here, $q ( j , k ) = q ( S _ { i t } = j , S _ { i t + 1 } = k ) = P ( S _ { i t + 1 } = k \mid S _ { i t } = j ) .$ and for each state $j , \sum _ { k = 1 } ^ { n } q ( j , k ) = 1$ and $0 \leq q ( j , k ) \leq$ $1 \forall j , k \in \{ 1 , 2 , \ldots , \dot { n } \}$

This probabilistic transition is modeled by assuming that a propensity for transition $( L S T _ { i j t } )$ is affected by developer’s participation in learning activities. It is represented as $L \hat { S } T _ { i t j } = \beta _ { j } R _ { i t } + \xi _ { i } + e _ { i t j }$ . Here, $R _ { i t }$ is a vector of variables that capture the extent of participation in learning activities by developer i in period t. The parameter vector $\beta _ { j }$ measures the impact of developer learning activities $R _ { i t }$ on the propensity toward a transition from state j. The variables included in the vector $R _ { i t }$ are explained in §5.1. The developer-specific unobserved heterogeneity for state transitions is captured by the developer-specific random effects,  . A transition to a higher state occurs if the learning through these activities is higher than a certain threshold value, $\mu ( h , j )$ . Similarly, a transition to a lower state occurs if the amount of learning is lower than a certain threshold value, $\mu ( l , j )$ . The state transition matrix Q4i1 t1 t + 15 contains the probabilities of transitions from one state to another for a developer i from time t to t +1. Specifically, $q ( S _ { i t } , S _ { i t + 1 } )$ is modeled as an ordered logit:

$$
\begin{array}{c} q (j, j + 1) = 1 - \frac {\exp (\mu (h , j) - \beta_ {j} R _ {i t} - \xi_ {i})}{1 + \exp (\mu (h , j) - \beta_ {j} R _ {i t} - \xi_ {i})}, \\ q (j, j - 1) = \frac {\exp (\mu (l , j) - \beta_ {j} R _ {i t} - \xi_ {i})}{1 + \exp (\mu (l , j) - \beta_ {j} R _ {i t} - \xi_ {i})}, \quad \text { and } \\ q (j, j) = \frac {\exp (\mu (h , j) - \beta_ {j} R _ {i t} - \xi_ {i})}{1 + \exp (\mu (h , j) - \beta_ {j} R _ {i t} - \xi_ {i})} \\ - \frac {\exp (\mu (l , j) - \beta_ {j} R _ {i t} - \xi_ {i})}{1 + \exp (\mu (l , j) - \beta_ {j} R _ {i t} - \xi_ {i})}, \\ \forall   j \in \{1, 2, \ldots , n \}. \end{array}\tag{3}
$$

Here, $\mu ( h , n ) = \infty , \mu ( l , 1 ) = - \infty$ . The threshold value necessary to move to an upper state is represented by $\mu ( h , \bar { j } )$ , whereas the threshold value necessary to move to a lower state is represented by $\mu ( l , j )$ . The constraint $\mu ( h , j ) > \mu ( l , j )$ is applied to ensure that the high threshold is larger than the low threshold. Notice that in an intermediary state $j \in \{ 2 , 3 , \ldots , n - 1 \} ,$ , a developer has three options: (i) to move up one state, (ii) to stay in the same state, and (iii) to move down one state. However, in the lowest state, 1, a developer can either move up one state or stay in the same state. Similarly, in the highest state, $n ,$ a developer can either move down one state or stay in the same state.

## 3.2. State-Dependent Code Contribution Probability

The extant software development research suggests the use of completions of modification requests (MRs) as a measure of productivity for projects that follow incremental software development approaches (Boh et al. 2007). MRs are similar in their concept to work orders and are used to add new functions and modify or repair old functions (Boh et al. 2007). In OSS, the concurrent versioning system (CVS) commit transaction<sup>2</sup> represents a basic change similar to the MR in commercial development environments (Mockus et al. 2002). Hence, we use number of CVS commits by a developer as a measure of her productivity. Because the number of CVS commits is a count measure, we employ the negative binomial distribution to model the state-dependent contribution probabilities. The probability of observing a particular number of CVS commits is

$$
\begin{array}{l} \operatorname * {P r} (\text { number   of   CVS   commits } = O _ {i t}) \\ = e ^ {- \lambda_ {j}} \lambda_ {j} ^ {O _ {i t}} / \Gamma (O _ {i t} + 1), \end{array}
$$

where $O _ { i t }$ is the number of CVS commits made by developer i in period $t , \lambda _ { j } = \exp ( \rho _ { j } W _ { i t } + \eta _ { i } + \varepsilon _ { i j t } )$ is the conditional mean, $W _ { i t }$ is the vector of input variables that influence a developer’s coding process, $\rho _ { j }$ is a vector of state-dependent parameters, and $\varepsilon _ { i j t }$ is the error term that follows a log-gamma distribution (Greene 2007). The developer-specific random effects $\eta _ { i }$ capture the developer-specific unobserved heterogeneity. The probability that the developer i will contribute a given number of CVS commits $O _ { i t }$ at time t conditional on her learning state $S _ { i t }$ at time t is then

$$
a (O _ {i t} \mid S _ {i t} = j) = \frac {\Gamma (\theta_ {j} + O _ {i t})}{\Gamma (O _ {i t} + 1) \Gamma (\theta_ {j})} h _ {i t | j} ^ {O _ {i t}} (1 - h _ {i t | j}) ^ {\theta_ {j}},
$$

where

$$
h _ {i t \mid j} = \frac {\exp (\rho_ {j} W _ {i t} + \eta_ {i})}{\exp (\rho_ {j} W _ {i t} + \eta_ {i}) + \theta_ {j}}.
$$

Here, $\theta _ { j }$ and $\rho _ { j }$ are the parameters to be estimated. $\theta _ { j }$ is a dispersion parameter. The variables that constitute $W _ { i t }$ are explained in §5.2. We can rewrite the likelihood for developer i as

$$
L (O (i)) = \int_ {\xi} \int_ {\eta} L (O (i) \mid \eta , \xi) d G (\eta \mid \xi) d H (\xi).\tag{4}
$$

We allow the individual-specific random effects for learning () and coding () to be correlated.

## 4. Data

Data were collected from the projects hosted at Sourceforge.net (SF) (Madey 2006). SF is the world’s largest OSS project repository and accounts for approximately 90% of all OSS projects. It provides a good sample of the OSS community that is useful in studying the underlying dynamics. We considered only those projects that were begun at Sourceforge during the sixmonth period from January 1, 2000 to June 30, 2000. We further considered only those projects that satisfied three criteria: (1) the project must use CVS at Sourceforge, (2) all associated developers of the project should be authorized to commit to CVS, and (3) the project’s e-mail list at Sourceforge should be its only mentioned source of developer discussions. The first condition is required to ensure that the developer code contribution data are available. The second condition ensures that the developer code contributions are correctly tracked. In some projects, only a selected few are given the power to commit to the CVS. This hampers the tracking of development activity. The third condition ensures that complete peer interaction data are available. Some of the projects use other platforms for discussion than the mailing lists at Sourceforge. Due to difficulty in matching the identity of developers at the two places (e.g., Sourceforge and homepage), we do not consider projects that have outside mailing lists or use Internet relay chat channels for discussion.

We collected the data for these projects for the period spanning from the registration date of each project until December 30, 2005. This process provided us with approximately 6 years of data for 25 projects. The data about the code contributions of developers in a project are extracted through the CVS log entries.<sup>3</sup> The peer interactions data were collected from the archives of the developer mailing lists<sup>4</sup> using Web agents. In mailing lists hosted at Sourceforge, the e-mails that belong to a same original post are assigned the same thread ID. This helped us in retrieving the information about the starter of a thread and subsequent participants in the thread. The date, time, thread starter, and participants were recorded. Sometimes developers used different ID tags or names when communicating or committing in CVS. Names/IDs of all the CVS committers and communicators were scanned and matched for each project by human effort. The e-mail information we use is based on threaded correspondence, which ensures that the original post was not just an announcement and demanded a reply. Projectand developer characteristic-related data were collected from the project homepages at Sourceforge.net. The CVS commit and developer mailing list data for developers who appear at least 10 times in the data set are used to calibrate the HMM. There were 251 developers who fit this criterion, and they provide us with a rich enough data set for HMM analysis. During the time span of our data set, these 251 developers were working only on the considered OSS projects. Each developer was working on only one project at a time.

## 5. Variable Descriptions

In this section, we describe the variables that constitute Wit and Rit. A succinct definition of these variables is also provided in Table 1.

Table 1 Model Variables

<table><tr><td colspan="2">Learning activities ( $R_{it}$ )</td></tr><tr><td> $TDC\_coding\_experience_{it}$ </td><td>Time-discounted cumulative number of CVS commits by developer  $i$  until period  $t - 1$ </td></tr><tr><td> $TDC\_threads\_start_{it}$ </td><td>Time-discounted number of threads started by developer  $i$  until period  $t$ </td></tr><tr><td> $TDC\_threads\_part_{it}$ </td><td>Time-discounted number of threads in which developer  $i$  participated but which it did not start until period  $t$ </td></tr><tr><td> $TDC\_read\_threads_{it}$ </td><td>Time-discounted number of threads posted in developer  $i's$  project until period  $t$ </td></tr><tr><td colspan="2">Code contribution ( $W_{it}$ )</td></tr><tr><td>Manager</td><td>Dummy variable equals 1 if the developer is a manager of the project and 0 otherwise</td></tr><tr><td> $Project\ rank_{t-1}$ </td><td>Sourceforge project rank in period  $t - 1$ . 1 is the highest rank</td></tr><tr><td> $Involvement\ quotient_t$ </td><td>Number of months the developer showed activity after joining the project</td></tr><tr><td> $Availability_t$ </td><td>Dummy variable equals 1 if the developer participated in communication in period  $t$  and 0 otherwise</td></tr><tr><td>Software development</td><td>Dummy variable equals 1 if the project type is software development and 0 otherwise</td></tr><tr><td>Technical audience</td><td>Dummy variable equals 1 if the intended audience for project is technical (i.e., system administrators/developers) and 0 otherwise</td></tr><tr><td> $Project\ age_t$ </td><td>Number of months since project inception at Sourceforge by period  $t$ </td></tr><tr><td> $Project\ age\ squared_t$ </td><td>Square of project  $age_t$ </td></tr></table>

## 5.1. Variables Impacting Learning

The variables in the vector $R _ { i t }$ are used to calculate the state-transition probabilities. They represent either of the two modes of learning for an OSS developer. These variables are recorded after the first observation of a developer in the project. The first observation of a developer is the first time she appears on the mailing list or in the CVS commit logs.

Learning curve studies have modeled learning as a function of cumulative experience performing a task (Argote et al. 1990). In our model, learning by one’s own experience is represented by the amount of developed code accumulated up to the previous time period. It is possible that more recent participation in learning activities has a stronger impact on learning than earlier participation. Hence, we modeled a time-discounted coding experience (TDC\_coding\_experience) as

TDC\_coding\_experience<sub>it</sub>

$$
= \sum_ {k = 1} ^ {k = t - 1} d _ {1} ^ {(t - k - 1)} \times \text { number   of   CVS   commits } _ {i k}.\tag{5}
$$

Here, $d _ { 1 }$ is a discount factor and is positive but less than or equal to 1. Values of $d _ { 1 }$ closer to one would indicate lower decay in the impact of coding experience with time, whereas values closer to zero would indicate a high level of decay. $d _ { 1 }$ is considered a parameter and is estimated. Number $o f C V S$ commits is the number of CVS commits by the developer i in period k.

Learning from peers is captured through a devel-$\mathrm { o p e r } ^ { \prime } \mathrm { s }$ involvement in threaded communication. We consider three different aspects of a developer’s involvement in threaded communication. A thread usually serves the interests of a developer who started it by resolving her problems or through the discussion of issues in which she might be interested. To capture this effect, we consider the time-discounted cumulative number of threads started (TDC\_threads ${ } _ { s t a r t _ { i t } } )$ by a developer until period t. A developer might also participate in threads started by someone else. This involvement on the part of a developer might aim to provide help to the knowledge-seeker or seek help herself. This might serve the interests of a developer directly or indirectly. To capture this effect, we consider the time-discounted cumulative number of threads that a developer did not start but in which she participated (TDC\_threads ${ \bf \nabla } _ { p a r t _ { { i t } } } )$ until period t. While the developers may not become directly involved in a thread, they can still learn by reading the threads started and participated in by others. We constructed a variable, (TDC\_read\_ $t h r e a \dot { d } s _ { i t } ) .$ , which is the timediscounted cumulative number of threads posted in a project until period t. Hence, the three peer interaction variables are constructed as follows:

$$
T D C \_ t h r e a d s \_ s t a r t _ {i t} = \sum_ {k = 1} ^ {k = t} d _ {2} ^ {(t - k)} \times t h r e a d s s t a r t _ {i k},\tag{6}
$$

$$
T D C \_ t h r e a d s \_ p a r t _ {i t} = \sum_ {k = 1} ^ {k = t} d _ {3} ^ {(t - k)} \times t h r e a d s p a r t _ {i k},\tag{7}
$$

$$
T D C \_ r e a d \_ t h r e a d s _ {i t} = \sum_ {k = 1} ^ {k = t} d _ {4} ^ {(t - k)} \times r e a d t h r e a d s _ {i k}.\tag{8}
$$

Here, $d _ { 2 } , d _ { 3 } ,$ and $d _ { 4 }$ are discount factors and are positive but less than or equal to 1. We treat $d _ { 1 } , d _ { 2 } , d _ { 3 } ,$ and $d _ { 4 }$ as parameters that need to be estimated. Note that threads $s t a r t _ { i t }$ is the number of threads started by developer i in period t, threads $p a r t _ { i t }$ is the number of threads that developer i did not start but participated in during period $t ,$ and read $t h r e a d s _ { i t }$ is the number of threads posted in developer $i ^ { \prime } s$ project in period t.

## 5.2. Variables Impacting Code Contribution

The variables in $W _ { i t }$ are used to calculate state-dependent code contribution probabilities. We categorize these variables as developer characteristics, project characteristics, and project life-cycle effects.

5.2.1. Developer Characteristics. A developer’s code contributions to an OSS project are determined by her DK, PKS, the presence (absence) of external situations that affect intrinsic motivations and availability. The learning state-specific constant term in the contribution equation captures the differences in the code contributions of developers owing to differences in their capabilities (DK and PKS). The presence of extrinsic incentives such as status and future economic incentives might affect a developer’s intrinsic motivation to contribute (Lerner and Tirole 2002). Such extrinsic incentives are closely tied with a developer’s and a project’s visibility (Lerner and Tirole 2002). Project managers receive greater visibility based on their higher status. We control for this effect through the computation of a variable “manager,” representing whether a developer is a manager on the project or not. A project’s visibility is tied to its performance. Sourceforge provides a composite measure of project performance (“project rank”) by ranking the projects at the end of each month based on their activity and popularity among developers and users (Roberts et al. 2006, Crowston et al. 2003). Besides extrinsic incentives, long-time association with a project might make the developer more loyal to the project and, hence, could influence her contributions. We account for such loyalty by controlling for a developer’s level of past involvement in the project (“involvement quotient”). Because participation in OSS is not a full-time activity for most of the developers, they might not be available for code contributions in each period. We control for this effect by incorporating a variable called “availability” in period t as a dummy that equals 1 if the developer is involved in the project in period t or 0 otherwise. A developer’s motivation to participate in OSS due to creative pleasure, altruism, or intrinsic desire to fight against proprietary software might affect her contributions, but these elements are difficult to observe and hence are controlled for through the use of developer-specific unobserved random effect terms.

5.2.2. Project Characteristics. We control for those characteristics of projects that might influence the quality of developers attracted to a project and the quality bars for accepting code contributions. We control for whether the project is software development-related or not. We also control for whether the intended audience is technical (i.e., system administrators/developers) or not. We specifically control for these characteristics because projects with these characteristics are likely to attract sophisticated developers. Hence, these projects would provide an ideal environment for those developers who want to accrue reputation benefits to contribute and show their programming prowess to sophisticated peers. Because CVS commits are peer-reviewed, these projects might have high bars for accepting contributions.

Table 2 Descriptive Statistics of Key Variables

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Number of CVS commits</td><td>3.15</td><td>24.64</td></tr><tr><td> $TDC\_coding\_experience_{it-1}$ </td><td>86.95</td><td>123.65</td></tr><tr><td> $TDC\_threads\_started_{it}$ </td><td>2.16</td><td>2.98</td></tr><tr><td> $TDC\_threads\_participated_{it}$ </td><td>3.46</td><td>3.21</td></tr><tr><td> $TDC\_read\_threads_{it}$ </td><td>17.45</td><td>11.19</td></tr><tr><td>Manager</td><td>0.32</td><td>0.30</td></tr><tr><td> $Project\ rank_{t-1}$ </td><td>2,796.12</td><td>2,019.21</td></tr><tr><td> $Involvement\ quotient_t$ </td><td>11.03</td><td>24.88</td></tr><tr><td> $Availability_t$ </td><td>0.79</td><td>0.13</td></tr><tr><td>Software development</td><td>0.53</td><td>0.50</td></tr><tr><td>Technical audience</td><td>0.85</td><td>0.36</td></tr><tr><td> $Project\ age_t$ </td><td>35.1</td><td>17.35</td></tr></table>

5.2.3. Project Life-Cycle Effects. Project life cycle effects such as code complexity or code maturity with time may affect code contributions. To control for the effect of project life cycles on code contributions, we calculate a variable called “project age.” To account for any nonlinearity in the effect of project age on code contributions, we also include “project age squared” in the model.

## 5.3. Descriptive Statistics

The descriptive statistics for the variables described in Table 1 are provided in Table 2. The data set involves 25 projects and 251 developers. On average, a developer is observed for 53.31 periods, where a period length is one month. The mean number of threads started per developer is 35.42, and the mean number of threads participated in per developer is 59.36. On average, there are 692.9 threads that are started per project. Furthermore, the mean number of days a thread spans is 5.14. Note that to calculate the descriptive statistics of the variable that constitute $R _ { i t } ,$ we require values for $d _ { 1 } , \ d _ { 2 } , \ d _ { 3 } ,$ and $d _ { 4 } .$ The values used below are $d _ { 1 } = 0 . 9 8 5 , d _ { 2 } = 0 . 6 5 9 , d _ { 3 } = 0 . 6 2 1 ,$ and $d _ { 4 } = 0 . 1 0 6$ . These values were obtained following the estimation procedure explained in §6.2. The correlations of the key variables are presented in the appendix.

## 6. Estimation Procedure and Model Selection Criteria

## 6.1. Some Econometric Issues

There are three main theoretical and statistical challenges that might lead to inconsistent estimates: unobserved heterogeneity, reverse causality, and serial correlation (Greene 2007). Unobserved heterogeneity might exist on two levels—learning state-specific and developer-specific. Furthermore, at each level, unobserved heterogeneity could exist for learning behavior and code contribution behavior. For instance, because they have more knowledge and greater skill, developers in the high state are more likely to be available, show involvement in, or participate in peer interactions. The HMM controls for these state-specific unobserved effects through the inclusion of statespecific constant terms in the contribution equations and state-specific threshold parameters in transition equations. This specification is similar to state-specific fixed effects estimation.

In this study, developer-specific unobserved heterogeneity refers to the possibility that unmeasured (or immeasurable) differences (such as intrinsic motivation or external learning opportunities available to a developer) among observationally equivalent developers may affect their learning and their code contributions. This unobserved heterogeneity is controlled for in two ways in the model. The time-varying changes in the knowledge stocks, skill, and expertise of the developers are being captured by the learning states. The developer-specific inherent time-invariant unobserved effects are controlled for by explicit modeling using developer-specific random effects  and $\xi$ (Altman 2007). The problem of reverse causality is minimal in the present model, as participation in learning activities is lagged with respect to the code contributions. Finally, the state-space structure of our model accounts for the serial correlation, which leads to consistent and efficient estimates (MacDonald and Zucchini 1997).

## 6.2. Estimation Procedure

Maximum likelihood estimation (MLE) is used to estimate the HMM parameters in Equation (4).

Equation (2) is evaluated at a given value of  and $\hat { \boldsymbol { \xi } }$ to obtain the value of $L ( O ( { \dot { i } } ) | \eta , \xi )$ , which is inserted into Equation (4). To avoid any misspecification of heterogeneity distributions $G$ and $H ,$ we took a nonparametric approach (Heckman and Singer 1984). This involves approximating the underlying unknown probability distribution by a finite number of support points for  and $\xi$ and the location and probability mass function associated with them. We relate two normalizing constants, $C _ { \eta }$ and $C _ { \xi } ,$ with the support points and set the bounds on each of the random effects as 0 and 1. We apply an iterative procedure and add support points until the inclusion of an additional point leads to a situation wherein two support points overlap. We use the sequential BFGS Newton-Raphson algorithm to maximize the likelihood given in Equation (4) (LeSage 2005). We estimated our HMM with the initial state fixed at 55% in state 1, 25% in state 2, and 20% in state 3, for computational convenience and to reduce the number of parameters to be estimated. As is common in this approach, we ensured the stability of the results by running the analysis with several different randomly selected starting values for the parameters as well as initial state distributions.

Before we can estimate the model, we require values of $d _ { 1 } , d _ { 2 } , d _ { 3 } ,$ and $d _ { 4 }$ so that we can construct the variables that constitute $R _ { i t }$ . These parameters are treated as constant when calculating the value of the variables in $R _ { i t }$ . To identify the optimal value of $d _ { 1 } ,$ $d _ { 2 } , d _ { 3 } ,$ , and $d _ { 4 } ,$ we compared likelihoods for different values of $d _ { 1 } , d _ { 2 } , d _ { 3 } ,$ and $d _ { 4 }$ and chose the values that jointly provide the maximum likelihood.

One issue that remains to be considered is how to choose the number of states n. Greene and Hensher (2003) suggest the use of Bayesian information criterion (BIC) as a model selection measure for the comparison of models with different number of states estimated using MLE:

$$
\mathrm{BIC} = \ln L - s i z e \times \ln (D) / 2.
$$

Here, size is the number of parameters in the model and D is the number of developers. We estimated multiple models imposing a different number of states at a time by increasing the number of states starting with the one-state model and stopped the estimation at the four-state model. These scenarios are run separately and their log-likelihood values are obtained. The log-likelihoods for all scenarios are shown in Table 3. The three-state HMM outperforms all other model specifications. The one-state model assumes static code contribution behavior for a developer, i.e., no time-varying heterogeneity. It is outperformed by all of the other models that assume dynamic code contribution behavior. This implies that coding experience and peer interactions cause a heterogeneous change in the code contribution behavior of a developer.

6.3. Comparison of HMM with Other Alternatives We compared HMM with alternative models. Besides the HMM, we considered two other models. One of the alternative models is a standard learning curve model where along with the code contributionspecific variables, the learning activity-specific variables are also included as explanatory variables in a single equation that predicts code contributions. The other alternative model is a latent class learning curve model. Among other things equal, the class of a latent class model corresponds to a unique code contribution behavior. The only difference between this

Table 3 Comparison of HMM Models

<table><tr><td>Model</td><td>Number of states</td><td>Log-likelihood</td><td>BIC</td><td>Variables estimated</td></tr><tr><td rowspan="4">HMM</td><td>One</td><td>-2,4917.9</td><td>-2,4970.4</td><td>19</td></tr><tr><td>Two</td><td>-2,2497.8</td><td>-2,2624.9</td><td>46</td></tr><tr><td>Three</td><td>-2,2185.2</td><td>-2,2356.5</td><td>62</td></tr><tr><td>Four</td><td>-2,2166.5</td><td>-2,2384.8</td><td>79</td></tr></table>

Table 4 Comparison of Learning Models

<table><tr><td>Model</td><td>Log-likelihood</td><td>BIC</td><td>Variables estimated</td></tr><tr><td>Standard learning curve</td><td>-2,4917.9</td><td>-2,4970.4</td><td>19</td></tr><tr><td>Latent class learning curve model</td><td>-2,4101.3</td><td>-2,4222.9</td><td>44</td></tr><tr><td>HMM</td><td>-2,2185.2</td><td>-2,2356.5</td><td>62</td></tr></table>

model and a classical learning curve model is that the parameters of the learning curve are allowed to vary across classes. The classes are determined endogenously. This model would better account for developer heterogeneity and will collapse to a standard learning curve model if the developers are homogeneous. The difference between an HMM and a latent class model is that in the latter, a developer stays in the same class throughout, but in HMM, the developer is allowed to transition from one state (class) to another. If there are no transitions, then the HMM can be made to collapse to the latent class learning curve model. Hence, if there are no transitions and developers are homogenous, the HMM can be made to collapse to the classical learning curve model. The three models were compared in terms of BIC. The BICs for the models are given in Table 4. HMM outperforms both of the other models. This indicates that developers are heterogeneous, as well as that they transition from one state to another over time.

## 7. Results, Discussion,

The values $d _ { 1 } = 0 . 9 8 5 , \ d _ { 2 } = 0 . 6 5 9 , \ d _ { 3 } = 0 . 6 2 1$ , and $d _ { 4 } = 0 . 1 0 6$ provide the maximum likelihood. The results henceforth correspond to these values of the decay parameters. The value of $d _ { 1 }$ indicates that there is very little decay in the impact of distant coding experience, whereas the value of $d _ { 4 }$ indicates that the impact of reading threads decays very rapidly over time. There is also significant decay in the impact of threads started and participated in over time. The estimated parameters for the three-state model are shown in Table 5.

Table 5 Estimated Parameters for the Three-State HMM

<table><tr><td colspan="2">Parametersa</td><td colspan="3">Learning states</td></tr><tr><td>Variable type</td><td>Variable name</td><td>State 1</td><td>State 2</td><td>State 3</td></tr><tr><td colspan="5">State transition (β)</td></tr><tr><td>Learning from own experience</td><td>TDC_coding_experiencet</td><td>0.017</td><td>0.069***</td><td>0.121**</td></tr><tr><td rowspan="3">Learning from peers</td><td>TDC_threads_startt</td><td>0.479**</td><td>3.893***</td><td>1.387***</td></tr><tr><td>TDC_threads_partt</td><td>3.854***</td><td>1.032**</td><td>1.411**</td></tr><tr><td>TDC_read_threadst</td><td>0.709*</td><td>0.291*</td><td>0.066</td></tr><tr><td>Upper threshold</td><td>μh,s</td><td>3.116***</td><td>3.497***</td><td></td></tr><tr><td>Lower threshold</td><td>μl,s</td><td></td><td>-1.908***</td><td>-1.659**</td></tr><tr><td colspan="5">Coding (ρ)</td></tr><tr><td>Capability</td><td>Constant</td><td>-4.188***</td><td>0.975**</td><td>2.939***</td></tr><tr><td rowspan="2">Extrinsic incentives</td><td>Manager</td><td>2.062**</td><td>0.511*</td><td>0.535*</td></tr><tr><td>Project rankt-1</td><td>-2.251***</td><td>-0.569***</td><td>-0.065</td></tr><tr><td>Loyalty</td><td>Involvement quotientt</td><td>2.485**</td><td>1.587**</td><td>0.863**</td></tr><tr><td>Availability</td><td>Availabilityt</td><td>0.799</td><td>1.051**</td><td>0.775**</td></tr><tr><td rowspan="2">Project characteristics</td><td>Software development</td><td>-0.384</td><td>0.134*</td><td>0.367**</td></tr><tr><td>Technical audience</td><td>-2.809**</td><td>0.129**</td><td>0.822***</td></tr><tr><td rowspan="2">Project life-cycle effects</td><td>Project aget</td><td>-0.829**</td><td>-1.767**</td><td>-0.988**</td></tr><tr><td>Project age squaredt</td><td>1.395**</td><td>1.019*</td><td>0.379**</td></tr><tr><td colspan="2">Dispersion (θ)</td><td>1.475***</td><td>0.281**</td><td>0.875**</td></tr><tr><td colspan="5">Unobserved heterogeneity (η,ξ)</td></tr><tr><td>Cη=-1.981, Cξ=-0.129</td><td>η1=0</td><td>η2=0.178</td><td>η3=0.360</td><td>η4=1.000</td></tr><tr><td>Probability</td><td>0.027</td><td>0.364</td><td>0.379</td><td>0.230</td></tr><tr><td colspan="5">Conditional distribution: probability(ξ|η)</td></tr><tr><td>ξ1=0</td><td>0.9911</td><td>0.3085</td><td>0.2924</td><td>0.9551</td></tr><tr><td>ξ2=0.430</td><td>0.0034</td><td>0.3352</td><td>0.4126</td><td>0.0048</td></tr><tr><td>ξ3=1.000</td><td>0.0055</td><td>0.3563</td><td>0.2950</td><td>0.0401</td></tr></table>

<sup>a</sup>The variables were checked for problems of multicollinearity. The following scaling was performed to ensure solution stability and reduce correlation between variables. The project age variable is mean-centered and divided by 100. The project age squared variable is calculated as the square of scaled mean-centered project age. This transformation is performed to reduce the correlation between the two age-related variables (Gelman and Hill 2007). TDC\_threads\_start and TDC\_threads\_part are scaled down by a factor of 10. TDC\_read\_threads , involvement quotient , TDC\_coding\_experience , and project rank are scaled down by factors of 100, 100, 100, and 100,000, respectively. We have used a nonparametric approach to account for unobserved heterogeneity. We have restricted  and  to vary between zero and one; $\boldsymbol { C } _ { \eta }$ and $C _ { \xi }$ are the corresponding normalizing constants; the developer-specific heterogeneities are $\eta \ : { \cal { C } } _ { \eta }$ and $\xi \ C _ { \xi } .$  
$^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1$ (two-tailed t-test for all variables).

## 7.1. Learning State—Code Contribution Behavior Relationship

The variation in the coefficients of a variable across states for code contribution behavior indicate that a change in learning state causes a change in the code contribution behavior of the developers. The capability variable that corresponds to the state-specific constant term is (−4.188, p < 0001), (0.975, p < 0005), and (2.939, $p < 0 . 0 1 )$ for states 1, 2, and 3, respectively. This clearly indicates that a developer in state 1 is less capable than a developer in state 3. The capability of a developer increases as he moves from state 1 to 2 to 3. The coefficients corresponding to “manager” are (2.062, $p < 0 . 0 1 )$ , (0.511, $p < 0 . 1 )$ , and (0.535, $p < 0 . 0 1 )$ for states 1, 2, and 3, respectively. The positive coefficients in each state indicate that a manager on average contributes more than a developer. Furthermore, the difference between a manager’s and a developer’s contribution decreases as they move to higher states.

Because lower values for project rank indicate better project performance, the corresponding coefficients for developers in states 1 (−2.251, $p < 0 . 0 1 )$ and 2 (−0.569, $p < 0 . 0 1 )$ indicate that they are more likely to contribute when the project is doing well, whereas a developer’s code contribution in state 3 is insensitive to the performance of the project. More knowledgeable and skilled developers can direct the growth and architecture of the code by making major contributions. Hence, as a developer gains knowledge and skills, she becomes less sensitive to a project’s prior performance, as she has the potential to significantly influence future performance.

Developers who have been involved for a longer time on average contribute more code across the three states. The corresponding coefficients for states 1, (2.485, p < 0001), 2 (1.587, p < 0001), and 3 (0.863, $p < 0 . 0 5 )$ indicate that the marginal effect of the involvement quotient decreases as a developer moves from state 1 to 2 to 3. The availability of a developer in state 1 has no impact on his code contribution behavior, whereas a developer is more likely to contribute code if he is available and is in states 2 (1.051, $p < 0 . 0 5 )$ and 3 (0.775, $p < 0 . 0 5 )$ , with the marginal impact decreasing as the developer transitions from state 2 to 3. Developers in states 2 and 3 are more likely to contribute to a software development project [state 2 (0.134, p < 001) and state 3 (0.367, p < 0005)] or to a project aimed at technical audience [state 2 (0.129, $p < \bar { 0 } . 0 \dot { 5 } )$ and state 3 (0.822, $p < 0 . 0 1 ) ]$ than to other projects. The contributions of a developer in state 1 are insensitive to whether the project is software development-related or not. However, the developer in state 1 is less likely to contribute to a project that is aimed at a technical audience (−2.809, $p < 0 . 0 1 )$ . Furthermore, the difference between the contributions of a developer to a software development-related versus a nonsoftware development-related project increases as he moves from state 2 to 3. A similar change is observed for projects that are aimed at technical audiences or not. This confirms our belief that more skilled and knowledgeable developers would prefer to contribute to projects where the quality bars are higher. Furthermore, it would be tough for developers at a low skill level to contribute to such projects. Developers in all three states are less likely to contribute code as the project grows older. As a developer’s active involvement in the project grows, so do her contributions across the three states. On average, a developer is likely to contribute the highest amount of code when in state 3 and the least amount of code when in state 1. For example, at the mean levels of all variables that go into $W _ { i t } ,$ the mean number of CVS commits by a developer in state 1, state 2, and state 3 are 0.001, 3.064, and 41.169, respectively; additional information about these calculations is contained in the online appendix.<sup>5</sup> Note that there will be huge variation in the number of CVS commits around these mean values, as indicated by high values of state-specific dispersion parameters in Table 5. For the ensuing analysis, we refer to states 1, 2, and 3 as low, medium, and high, respectively.

## 7.2. Learning State Transitions

The threshold for moving from the low to the medium state is 3.116 $( p < 0 . 0 1 )$ , that for moving from the medium to the low state is −1.908 $( p < 0 . 0 1 )$ , that for moving from medium to high is 3.497 $( p < 0 . 0 1 )$ and that for moving from high to medium is −1.659 $( p < 0 . 0 5 )$ . As expected, the threshold for moving to higher (lower) states is positive (negative). Table 6 presents the intrinsic propensities toward transition for a developer. The probabilities in the transition matrices are calculated by plugging in the estimated thresholds and unobserved heterogeneity parameters to Equation (3), and a sample calculation is shown in the appendix. Table 6 shows that all the states are extremely “sticky.” One implication of this finding is that once a developer moves up (down) to a higher (lower) learning state, she is more likely to stay there. This signifies the persistence of learning and, hence, a persistent change in code contribution behavior. Also note that the probability of intrinsically transitioning to a lower state is much higher than the probability of intrinsically transitioning to a higher state. These nonzero intrinsic probabilities of transitioning to adjacent states illustrate the temporal nature of the utility and relevance of possessed knowledge in OSS development.

The parameters corresponding to learning activities are all significant, except the parameter for learning from one’s own experience in state 1 and the one for reading threads in state 3. From Table 5, if we compare the coefficients corresponding to coding experience across the three states, we can see that it benefits the developers in the highest state the most. Similarly, starting threads benefits the developer in the medium state the most, whereas reading threads and participation in threads started by others benefits the developers in the lowest state the most.

Table 6 Transition Matrix Intrinsic Propensity to Transition

<table><tr><td> $t \rightarrow t + 1$ </td><td>Low (%)</td><td>Medium (%)</td><td>High (%)</td></tr><tr><td>Low</td><td>95.63</td><td>4.37</td><td>0</td></tr><tr><td>Medium</td><td>12.68</td><td>84.30</td><td>3.02</td></tr><tr><td>High</td><td>0</td><td>15.71</td><td>84.29</td></tr></table>

## 7.3. Learning from Peers

Developers in all three learning states benefit from interactions with their peers. However, the results show that learning activities have differential impacts on the learning of the developers anchored in their current learning states. Starting threads benefit the developers in medium state (3.893, $p < 0 . 0 1 )$ the most, followed by those in the high state $( 1 . 3 8 7 , ~ p < 0 . 0 1 )$ and the low state (0.479, $p < 0 . 0 5 )$ . This represents nonmonotonic behavior, where the marginal impact of starting threads increases as the developer moves from the low to the medium state but decreases as he moves from a medium to a high state. Participation in threads started by others also reveals a nonmonotonic effect because it benefits the developers in the low state $( 3 . 8 5 4 , p < 0 . 0 1 )$ the most, followed by high state (1.411, $p < 0 . 0 1 )$ and medium state (0.1.032, p < 0005). It is these nonmonotonic marginal impacts of learning activities on the learning of developers at different knowledge and skill levels that are very hard to reveal in a classical learning curve framework without a priori information regarding the shape of the impact. Reading threads helps the developer in the low state (0.709, p < 001) the most, followed by the one in the medium state (0.291, $p < 0 . 1 )$ . Reading threads does not help a developer in the high state. To understand the true impact of mean level of participation in these activities they have to be combined with the threshold parameters to calculate the mean transition probabilities.

Tables 7, 8, and 9 indicate the impact of developer interactions at mean level for TDC\_threads\_start,

Table 7 Transition Matrix (TDC\_threads\_start )

<table><tr><td> $t \rightarrow t + 1$ </td><td>Low (%)</td><td>Medium (%)</td><td>High (%)</td></tr><tr><td>Low</td><td>95.18</td><td>4.82</td><td>0</td></tr><tr><td>Medium</td><td>5.90</td><td>87.36</td><td>6.74</td></tr><tr><td>High</td><td>0</td><td>12.13</td><td>87.87</td></tr></table>

Table 8 Transition Matrix (TDC\_threads\_part )

<table><tr><td> $t \rightarrow t + 1$ </td><td>Low (%)</td><td>Medium (%)</td><td>High (%)</td></tr><tr><td>Low</td><td>85.24</td><td>14.76</td><td>0</td></tr><tr><td>Medium</td><td>9.22</td><td>86.51</td><td>4.27</td></tr><tr><td>High</td><td>0</td><td>10.26</td><td>89.74</td></tr></table>

TDC\_threads\_part, and TDC\_read\_threads on learning, respectively. For a developer in medium state, asking questions by starting threads increase the probability of a transition to the high state from 3.02% to 6.74%, besides reducing her probability of a transition to the low state from 12.68% to 5.90%. A developer in the high state also increases her likelihood of staying in the same state from 84.29% to 87.87% by initiating threads. These changes are highly significant given the stickiness of the states and the amount of code contributions expected in the higher state. However, a developer in the low state does not learn much by starting threads. A possible explanation could be that a developer in the low learning state might not be able to frame her questions properly, resulting in other developers either not understanding the question or finding it difficult to answer (Raymond and Moen 2001). Besides, it also indicates that the developer in the low state might lack relevant knowledge required to comprehend others’ responses to her questions.

Participation in discussions started by others has a huge impact on the learning of developers in the low and high states. A developer in the high state might benefit because good questions help developers gain new understanding and often reveal problems they might not have noticed or thought about otherwise. Participation in others’ discussions increases a developer’s probability of staying in the high state from 84.29% to 89.74%. As Table 8 shows, the probability that a developer in the low state will transition to the medium state increases from 4.37% to 14.76%. This increase is quite significant given the “stickiness” of the low state. While the coefficients corresponding to reading threads in Table 5 are positive and significant for developers in low and medium states, our results indicate that overall effect of reading threads is very small. A potential reason is that OSS projects are very broad and projects follow a modular architecture. Hence, many threads might be irrelevant to a developer’s immediate work.

Table 9 Transition Matrix (TDC\_read\_threads)

<table><tr><td> $t \rightarrow t + 1$ </td><td>Low (%)</td><td>Medium (%)</td><td>High (%)</td></tr><tr><td>Low</td><td>95.09</td><td>4.91</td><td>0</td></tr><tr><td>Medium</td><td>12.13</td><td>84.69</td><td>3.18</td></tr><tr><td>High</td><td>0</td><td>15.70</td><td>84.30</td></tr></table>

Table 10 Transition Matrix (TDC\_coding\_experience)

<table><tr><td> $t \rightarrow t + 1$ </td><td>Low (%)</td><td>Medium (%)</td><td>High (%)</td></tr><tr><td>Low</td><td>95.63</td><td>4.37</td><td>0</td></tr><tr><td>Medium</td><td>12.03</td><td>84.77</td><td>3.20</td></tr><tr><td>High</td><td>0</td><td>14.36</td><td>85.64</td></tr></table>

## 7.4. Learning from Own Experience

Table 5 shows that the coefficients corresponding to TDC\_coding\_experience are positive and significant for developers in the medium (0.069, p < 0001) and high (0.121, $p < 0 . 0 5 )$ states but insignificant for a developer in the low learning state. A developer in the low state might not possess knowledge relevant to the project and hence might depend upon peers to acquire that knowledge. Although learning from one’s own experience has a positive impact on the transition of a developer to a medium or high state, the effects are much less pronounced. This might indicate that developers who contribute significantly are experienced in coding before joining the project. The small positive impact of cumulative coding experience might just be due to the developer’s learning about the architecture and design of the source code specific to the project. This result and reasoning is also supported by the findings in the classical learning curve literature. Shafer et al. (2001) have found that people with higher expertise in a given area have lower subsequent learning rate in that area. They argue that once a person becomes expert by learning from an activity, she has little capacity left to learn more from the same activity in that area. Table 10 shows the transition matrix for the impact of mean level of TDC\_coding\_experience on the learning of a developer.

Table 11 shows the transition matrix for a developer when she participates in all four activities at the mean level. As expected, participating in all of the learning activities has a huge impact on moving developers to or keeping developers in the higher states.

## 7.5. Accumulation and Depreciation of Learning

Now, we shift our focus to investigating how quickly or slowly knowledge accumulates or depreciates in OSS. Table 12 presents the transition matrices for situations where a developer has either been active for six months or stayed inactive for six months. The matrices in Table 12 are obtained using the Chapman-Kolmogorov equations. If a developer in a low learning state actively participates in all learning activities at average levels continuously for six months, then she has a probability of 16.21% of being in the high state in the sixth month. For the medium and high learning states, the probability of being in the high state after six months of continuous participation in learning activities is 37.63% or 71.87%, respectively.

Table 11 Transition Matrix (All Activities)

<table><tr><td> $t \rightarrow t + 1$ </td><td>Low (%)</td><td>Medium (%)</td><td>High (%)</td></tr><tr><td>Low</td><td>82.16</td><td>17.84</td><td>0</td></tr><tr><td>Medium</td><td>3.78</td><td>85.87</td><td>10.35</td></tr><tr><td>High</td><td>0</td><td>7.09</td><td>92.91</td></tr></table>

Table 12 Transition Matrix (Six-Step Transition Matrix)

<table><tr><td> $t \rightarrow t + 1$ </td><td>Low (%)</td><td>Medium (%)</td><td>High (%)</td></tr><tr><td colspan="4">Active for 6 months</td></tr><tr><td>Low</td><td>35.76</td><td>48.03</td><td>16.21</td></tr><tr><td>Medium</td><td>10.08</td><td>52.19</td><td>37.63</td></tr><tr><td>High</td><td>2.350</td><td>25.78</td><td>71.87</td></tr><tr><td colspan="4">Inactive for 6 months</td></tr><tr><td>Low</td><td>74.92</td><td>22.39</td><td>2.69</td></tr><tr><td>Medium</td><td>34.56</td><td>51.30</td><td>14.14</td></tr><tr><td>High</td><td>11.44</td><td>38.66</td><td>49.91</td></tr></table>

To calculate the transition matrix of a developer who has been inactive for six months, we considered a situation in which the developer was involved in learning activities at the mean level before the start of the six-month period. The transition matrix shown above indicates her transition probabilities. If a developer in the high state does not participate in any of the activities for six continuous months, then she has a 50.10% chance of moving to a lower state (specifically, 11.44% for moving to the low state and 38.66% for moving to the medium state). Similarly, continuous inactivity for 6 months on the part of a developer in the medium state leads to a 34.56% chance of his transitioning to the low state. Note that the probability of being in the high state is lower than that of being in the low state. This confirms the persisting but dissipating effects of learning found in related research (e.g., Darr et al. 1995).

## 7.6. Posterior Analysis of Individual Behaviors

A developer’s learning state in any given period can be probabilistically recovered using the filtering approach (Hamilton 1989). The filtering approach utilizes only the information known up to time t to recover a developer’s state in period t. The probability that a developer is in state s in period t is given by

$$
\begin{array}{r l} & P (S _ {i t} = s \mid O _ {i 1} O _ {i 2} \dots O _ {i t}) \\ & \quad = \pi (i) \Lambda (i, 1) Q (i, 1, 2) \Lambda (i, 2) Q (i, 2, 3) \\ & \qquad \dots Q _ {s} (i, t - 1, t) \Lambda (i, t) / L (O _ {i 1} O _ {i 2} \dots O _ {i t}). \end{array}\tag{9}
$$

Here, $Q _ { s } ( i , t - 1 , t )$ is the column of the transition matrix Q4i1 t − 11 t5 corresponding to the state s. $L ( O _ { i 1 } O _ { i 2 } \cdot \cdot \cdot O _ { i t } )$ is the likelihood of the observed outcome sequence up to time t.

In any given period, a developer can be classified as being in a particular state according to the posterior probability distribution calculated using Equation (5). Figure 3(a) depicts the over-time trend of the distribution of developers in the three states, where the two curves plot the boundaries that separate the low, medium, and high states. Overall, about 55%–60% of the developers belong to the low state. The medium state accounts for roughly 20%–25%, and the remaining developers are in the high state over the time horizon under study. This observation is confirmed in Figure 2(b), which shows that the state membership average is about 1.6–1.7.

At the individual level (Figure 4), we find various types of switching behaviors. Some developers move reasonable quickly to the highest state, some take quite some time to make the transition, and others never move to the highest state. One interesting observation from Figure 4 is that once a developer transitions to a state, she stays there for quite some time before transitioning back.

Figure 3(a), combined with our calculations regarding the mean amount of code contributions in each state, indicates that 20% of the developers are doing 80% of the work. When we combine Figure 3(a) with Figure (4), we can observe that which developers fall into this 20% group varies over time. This happens due to the accumulation and depreciation of learning. This finding is quite positive for the OSS community. It reveals that someone who is initially a peripheral developer can learn through subsequent participation in the project and evolve into a core developer over time.

Figure 3 State Distribution of Developers (a) and Average State (b) Against Time  
![](/api/attachments/6XSTPGUN/fulltext/images/cc94eee76d223affe7860f83f1e34b4596c5d804502d2c3ee80e00e06b2f79d8.jpg)

![](/api/attachments/6XSTPGUN/fulltext/images/9bae50c5ab212ce2c3bdaf704f2d73056acbdd571a0efea0903d38f72b68e77b.jpg)

## 7.7. Robustness Checks

Table 5 presents a reduced model of our original specification, which included several other code contribution-, project-, and developer-related controls. We controlled for other project-specific variables such as programming language, user interface, and operating system. CVS commits that deal with changes to an existing file might require more/less effort than do the ones that deal with new files. To account for these differences in the type of contribution, we computed a variable that represented a developer’s fraction of CVS commits that involved changes to existing files for each period. Of the 251 developers, 162 developers reported their expertise in the concerned software development area (on a scale of 1 to $5 ,$ with 5 being the highest) upon joining the project. Controlling for this effect does not produce significantly different results. The variable selection was conducted using BIC tests. Hence, we present only results for the reduced model.

One concern regarding our results is the appropriateness of the period length specification. We employed alternative lengths for a period (two months and three months) and re-performed the analysis. These alternate specifications did not produce qualitatively different results. A similar concern could be raised about the construction of an availability variable. We employed several different constructions of this variable (presence in period t or/and t − 1, presence in period t or/and t − 1 or/and t − 2). Although the results for other variables were not substantively different, the use of presence in period t as availability in period t provides the better BIC. Another concern could be that some developers dropped out of the projects during the six-year period. In the current model, they will transition to the lowest state and stay there once they have dropped out. This might lead to overstickiness for the lowest state. To address this concern, we added a fourth state (the drop-out state) in the model and estimated. The results from this estimation are similar to the ones reported in the paper.

## 7.8. Limitations and Future Research Directions

There are several limitations, and we do not want to overstate our findings. The latent-state concept is an effective method of examining whether participation in code development and peer interactions improves developer productivity and learning, but the latency of the states does not allow us to determine the exact impact of learning activities on each of the latent factors, DK and PKS. Another limitation is that we do not consider the effect of learning from other programming jobs besides the OSS projects on the developers. Future research can also consider how much learning from OSS is transferable to commercial development projects, and vice versa. Furthermore, because we are dealing with archival data, we cannot really distinguish whether all developers read threads or not. Our measure of reading threads might in fact be a better indicator of the amount of interaction going on in the project than it is a measure of developers’ reading patterns regarding threads.

Figure 4 State of an Individual Developer Against Time  
![](/api/attachments/6XSTPGUN/fulltext/images/ede736a25a068b4e7c8c494cb292d09fd3a7a634c7f8b797551b7ab5da9febaa.jpg)

HMM is based on the notion that the present state of the system contains all the relevant information needed to predict the future in a probabilistic sense. The transition probabilities in our model depend on the current state only and not the prior history. We assumed that the experience gathered in previous states is all present in the most recent state. We empirically tested whether this assumption is valid for our data, allowing the second-order Markov transition, and found that the states in t − 2 do not have statistically significant impacts on state transition. Even though our data showed that the first-order Markov chain is sufficient, this assumption of the property of independence of the past could be a strong assumption. For example, we cannot distinguish the quality or content of learning that occurred in the past. If a developer transitions from a higher state to a lower state, she is no different from one who has been in the lower state all the time. She forgot the knowledge and skills that she gained while in the higher state, and her current propensity to code is the same as that of someone who has been in the low state in the past. Finally, a simple replication of our research enriched with more detailed measures of aspects of peer interactions (such as communication network structure and better categorization of threads using text mining techniques) could potentially provide more insights. Each of these limitations represents an exciting area for future research.

![](/api/attachments/6XSTPGUN/fulltext/images/c5190f3753100d0788d6aae4d5a5f899e4b98d21aeb60f902ab5410eff233c09.jpg)

## 8. Conclusions

In this paper, we develop a dynamic model of developer learning in OSS projects. We consider two modes of learning: coding experience and peer interactions. Publicly available data from CVS repositories and mailing lists are used for model estimation. This allows us to identify three states that are increasing in terms of learning and are found to lead to progressively higher code contribution probabilities. We also examine the impacts of the two modes of learning on the transitioning of developers between these states. HMM reveals internal structures underlying learning dynamics and identifies the drivers of evolution that accelerate the rate of learning in each state.

## 8.1. Contributions

This study makes several contributions. First, this is the first study that investigates learning in an OSS environment. Second, this is the first study to model dynamics of developer productivity behavior. We have shown that past experience or peer interactions not only affect productivity directly but also shape a developer’s code contribution behavior. This modeling framework is a significant addition to the learning curve literature (Argote et al. 1990). Our model allows for the segmentation of developers according to their code contribution and learning abilities, which is not possible in the existing learning curve framework. This segmentation provides a tool to help managers to predict developers’ subsequent coding productivity for each segment and come up with effective strategies for each segment of developers to maximize learning and contributions. Third, whereas prior research that investigates learning in software development does not account for depreciation in learning, we provide a theoretical basis for this and account for it in our model. Fourth, prior research is silent on the mode of knowledge transfer involved in learning from one’s peers, we find that the amount of learning from one’s peers in OSS development is a function of the amount of use as well as different aspects of the mode (peer interactions). Finally, the

HMM modeling of this study contributes to the development of a theoretically grounded understanding of the learning behavior of individuals. Such a theory and associated findings have important managerial and operational implications for devising interventions to promote learning in a variety of settings.

## 8.2. Managerial Implications

Our results have several implications for attracting and sustaining developer contributions in OSS projects. Our results provide ways in which a project can achieve better learning environment. A project can highlight the learning culture to attract and sustain developers.

Our model can be used by project managers to identify the learning states of developers at any time. Once a state is identified, the manager can use appropriate learning activity to influence transition to higher states. Our results reveal that once a developer is engaged in a certain behavior, such behavior persists. The skill levels of the developers does not deteriorate quickly, but on the other hand, it is hard to raise their skill levels. This finding sends mixed messages. The positive message implies that a developer with more productive behavior is likely to persist with it without extraordinary effort. The negative message is that a developer engaged in less productive behavior would require significant effort to switch to a more productive behavior. Based on our findings, a manager can devise strategies to help transition the developers to a state that is more conducive to code contributions to the project.

Our findings also reveal that a developer in the high state sustains such behavior by participating in discussions started by others. An investigation of a select sample of threads participated in by developers in the high state revealed that the high-state developers were involved in solving others’ problems. Anecdotal evidence also suggests that more advanced developers benefit by helping others to solve interesting and intriguing problems (Raymond and Moen 2006). When in the low state, developers depend exclusively on their peers to learn. Hence, their code contributions are dependent upon the cooperativeness of their peers. Developers in the low state learn the most by participating in threads started by others. However, there is a subtle difference between the threads participated in by developers in the low and the high states. We found that the threads participated in by developers in the low state were directed toward getting help (compared to a focus on providing help, as was the case for high-state developers) for the same or closely related issues. Managers should help rephrase questions for low state developers to elicit help from higher state developers.

Once the developer states are identified, the withinand across-state knowledge sharing dynamics can be explored. We found that the threads posted by a developer are most often responded to by the developers in same state. This indicates a state divide, where the developers prefer to communicate with developers with similar skills and knowledge levels. This is unhealthy for the OSS community. A manager should encourage interaction among developers across states. She should encourage developers with higher skill levels and knowledge to respond to questions posted by low-state developers or to help low-state developers in better framing their questions. Overall, managerial initiative should be directed at ensuring that novice or low- and medium-state developers receive the help that would ensure their transition to higher states.

## 9. Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http:// isr.journal.informs.org/.

## Acknowledgments

This research was supported by grants from the Center for Organizational Learning and Innovation, Carnegie Mellon University, Hongik University new faculty research support fund, and Evert McCabe Faculty Fellowship, University of Washington.

## References

Altman, R. M. 2007. Mixed hidden Markov models: An extension of the hidden Markov model to the longitudinal data setting. J. Amer. Statist. Assoc. 102(477) 201–210.

Argote, L., D. Epple. 1990. Learning curves in manufacturing. Science 247(4945) 920–924.

Argote, L., S. L. Beckman, D. Epple. 1990. The persistence and transfer of learning in industrial settings. Management Sci. 26(2) 140–154.

Argote, L., B. McEvily, R. Reagans. 2003. Managing knowledge in organizations: An integrative framework and review of emerging themes. Management Sci. 49(4) 571–582.

Basili, V., G. Caldiera. 1995. Improve software quality by reusing knowledge and experience. Sloan Management Rev. 37(1) 55–64.

Boh, W., S. Slaughter, J. Espinosa. 2007. Learning from experience in software development: A multilevel analysis. Management Sci. 53(8) 1315–1331.

Brooks, F. P. 1987. No silver bullet, essence and accidents of software engineering. Computer 20(4) 10–19.

Campbell, J. P., R. D. Pritchard. 1976. Motivation theory in industrial and organizational psychology. M. Dunnette, ed. Handbook of Industrial and Organizational Psychology. Rand McNally, Chicago, 63–130.

Cohen, W. M., D. A. Levinthal. 1990. Absorptive capacity: A new perspective on learning and innovation. Admin. Sci. Quart. 35(1) 128–152.

Crowston, K., H. Annabi, J. Howison. 2003. Defining open source software project success. Proc. Internat. Conf. Inform. Systems, Seattle.

Darr, E. D., L. Argote, D. Epple. 1995. The acquisition, transfer, and depreciation of knowledge in service organizations: Productivity in franchises. Management Sci. 41(11) 1750–1762.

Dutton, J., A. Thomas. 1984. Treating progress functions as a managerial opportunity. Acad. Management Rev. 9(2) 235–247.

Epple, D., L. Argote, K. Murphy. 1996. An empirical investigation of the microstructure of knowledge acquisition and transfer through learning by doing. Oper. Res. 44(1) 77–86.

Fleming, L. 2001. Recombinant uncertainty in technological search. Management Sci. 47(1) 117–132.

Gelman, A., J. Hill. 2007. Data Analysis Using Regression and Multilevel/Hierarchical Models. Cambridge University Press, New York.

Greene, W. H. 2007. Econometric Analysis, 6th ed. Prentice Hall, Englewood Cliffs, NJ.

Greene, W. H., D. A. Hensher. 2003. A latent class model of discrete choice analysis: Contrasts with mixed logit. Transportation Res. B: Methodological 37(8) 681–698.

Grewal, R., G. Lilien, G. Mallapragada. 2006. Location, location, location: How network embeddedness affects project success in OSS. Management Sci. 52(7) 1043–1056.

Hamilton, J. D. 1989. A new approach to the economic analysis of nonstationary time series and the business cycle. Econometrica 57(2) 357–384.

Heckman, J. 1991. Identifying the hand of past: Distinguishing state dependence from heterogeneity. Amer. Econom. Rev. 81(2) 75–79.

Heckman, J., B. Singer. 1984. Econometric duration analysis. J. Econometrics 24(1–2) 63–132.

Herbsleb, J., A. Mockus, T. Finholt, R. Grinter. 2001. An empirical study of global software development: Distance and speed. Internat. Conf. Software Engrg., IEEE Press, Los Alamitos, CA, 81–90.

Kanfer, R. 1990. Motivation theory and industrial and organizational psychology. M. Dunnette, L. Hough, ed. Handbook of Industrial and Organizational Psychology, 2nd ed. Consulting Psychology Press, Palo Alto, CA, 75–170.

Kraut, R. E., L. A. Streeter. 1995. Coordinating in software development. Comm. Assoc. Comput. Machinery 38(3) 69–81.

Lakhani, K., E. V. Hippel. 2003. How open source software works: “Free” user-to-user assistance. Res. Policy 32(6) 923–943.

Larson, J. R., C. Christensen. 1993. Groups as problem-solving units: Towards a new meaning of social cognition. British J. Soc. Psych. 32(1) 5–30.

Lerner, J., J. Tirole. 2002. Some simple economics of open source. J. Indust. Econom. 50(2) 197–234.

LeSage, J. P. 2005. Econometrics Toolbox for MATLAB. http:// www.spatial-econometrics.com/.

MacDonald, I. L., W. Zucchini. 1997. Hidden Markov and Other Models for Discrete-Valued Time Series. Chapman and Hall, London.

Madey, G. 2006. SourceForge Research Data Archive. Notre Dame, IN. http://zerlot.cse.nd.edu/mywiki/.

Mehra, A., R. Dewan, M. Freimer. 2010. Firms as incubators of open source software. Inform. Systems Res. 22(1) 22-38.

Mockus, A., R. Fielding, J. Herbsleb. 2002. Two case studies of open source software development: Apache and Mozilla. ACM Trans. Software Engrg. Methodology 11(3) 309–346.

Mukhopadhyay, T., P. V. Singh, S. Kim. 2011. Learning curves of agents with diverse skills in information technology enabled physician referral systems. Inform. Systems Res. 22(3) 586–605.

Narduzzo, A., A. Rossi. 2003. Modularity in action: GNU/Linux and free/open source software development model unleashed. Retrieved October 20, 2005, http://opensource.mit.edu/papers/ narduzzorossi.pdf.

Rabiner, L. R. 1989. A tutorial on hidden Markov models and selected applications in speech recognition. Proc. IEEE 77(2) 257–285.

Raymond, E. S. 1998. The cathedral and the Bazaar. First Monday 3(3).

Raymond, E. S., R. Moen. 2006. How to ask questions the smart way. Retrieved March 16, 2006, http://www.catb.org/∼esr/ faqs/smart-questions.html.

Reagans, R., L. Argote, D. Brooks. 2005. Individual experience and experience working together: Predicting learning rates from knowing who knows what and knowing how to work together. Management Sci. 51(6) 869–881.

Roberts, J., I.-H. Hann, S. Slaughter. 2006. Understanding the motivations, participation, and performance of open source software developers: A longitudinal study of the Apache projects. Management Sci. 52(7) 984–999.

Rodney, M. A., J. P. Campbell, R. Cudeck. 1994. A confirmatory test of a model of performance determinants. J. Appl. Psych. 79(4) 493–505.

Sacks, M. 1994. On-the Job Learning in the Software Industry. Quorum Books, Westport, CT.

Schilling, M. A., P. Vidal, R. E. Ployhart, A. Marangoni. 2003. Learning by doing something else: Variation, relatedness, and the learning curve. Management Sci. 49(1) 39–56.

Shafer, S. M., D. A. Nembhard, M. V. Uzumeri. 2001. The effects of worker learning, forgetting, and heterogeneity on assembly line productivity. Management Sci. 47(12) 1639–1653.

Singh, P. V. 2010. The small-world effect: The influence of macrolevel properties of developer collaboration networks on opensource project success. ACM Trans. Software Engrg. Methodology 20(2) Article 6.

Singh, P. V., C. Phelps. 2009. Determinants of open source software license choice: A social influence perspective. CMU working paper, Carnegie Mellon University, Pittsburgh. http://papers .ssrn.com/sol3/papers.cfm?abstract\_id=1436153.

Singh, P. V., Y. Tan. 2009. Developer heterogeneity and formation of communication networks in OSS projects. J. Management Inform. Systems 27(3) 179–210.

Singh, P. V., Y. Tan, V. Mookerjee. 2007. Social capital, structural holes, and team composition: Collaborative networks of the open source software community. Proc. Internat. Conf. Inform. Systems, Montréal.

Singh, P. V., Y. Tan, V. Mookerjee. 2011. Network effects: The influence of social capital on open source project success. MIS Quart. 35(4). Forthcoming.

Van de Ven, A. H., D. Polley. 1992. Learning while innovating. Organ. Sci. 3(1) 92–116.

Von Krogh, G., E. von Hippel. 2006. The promise of research on open source software. Management Sci. 52(7) 975–976.
