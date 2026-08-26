---
otero_id: 28562
otero_key: "PBUN65Y8"
title: "Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach"
authors: "Tongxin Zhou; Yingfei Wang; Lu (Lucy) Yan; Yong Tan"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1191"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach

Tongxin Zhou,<sup>a,</sup>\* Yingfei Wang,<sup>b</sup> Lu (Lucy) Yan,<sup>c</sup> Yong Tan<sup>b</sup>

<sup>a</sup> W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85287; <sup>b</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>c</sup> Kelley School of Business, Indiana University, Bloomington, Indiana 47405 \*Corresponding author

Contact: tongxin.zhou@asu.edu, https://orcid.org/0000-0001-8505-4021 (TZ); yingfei@uw.edu, https://orcid.org/0000-0002-3634-3617 (YW); yanlucy@indiana.edu, https://orcid.org/0000-0001-8408-0404 (L(L)Y); ytan@uw.edu, https://orcid.org/0000-0001-8087-3423 (YT)

Received: August 22, 2019 Revised: September 13, 2020; September 29, 2021; June 23, 2022; October 28, 2022 Accepted: November 5, 2022 Published Online in Articles in Advance: January 19, 2023

https://doi.org/10.1287/isre.2022.1191

Copyright: © 2023 INFORMS

Abstract. Online healthcare platforms provide users with various intervention programs to promote personal wellness. Given the many options available, it’s often difficult for individuals to decide in which intervention to participate, especially when they lack the experience or knowledge to evaluate the interventions. This may discourage individuals’ continuous engagement in online health management. In this study, we are motivated to develop a personalized healthcare recommendation framework to help individuals better discover the interventions that fit their needs. Considering the challenges in intervention adaptation and diversification in a highly dynamic online healthcare environment, we propose an innovative online learning framework that synthesizes deep representation learning and a theoryguided diversity promotion scheme. We evaluate our approach through a real-world data set on users’ intervention participation in an online weight-loss community. Our results provide strong evidence for the effectiveness of our proposed recommendation framework and each of its design components. Our study contributes to the emerging information systems research on prescriptive analytics and the application of business intelligence. The proposed modeling framework and evaluation results offer important implications for multiple stakeholders, including online healthcare platforms, policymakers, and users.

History: Ahmed Abbasi, Senior Editor; Huimin Zhao, Associate Editor. Funding: This work was supported in part by the National Natural Science Foundation of China [Grant 71729001].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.1191.

Keywords: personal health management • online healthcare interventions • recommendation systems • health behavior dynamics • diversity • deep representation learning • multiarmed bandit • prescriptive analytics

## 1. Introduction

Personal health management has garnered increasing attention from the healthcare community because of its importance in chronic condition management and disease prevention. Different from professional care delivery that highlights physicians’ expertise, personal health management occurs in everyday life and relies mostly on individuals’ efforts to self-regulate their lifestyles. To support personal health management, many online healthcare platforms—such as fatsecret.com, diabetesfoodhub. org, myfitnesspal.com, and livestrong.com—provide users with online healthcare interventions, which are structured behavior treatment programs or plans to help users establish healthy living habits. Popular examples include nutrition plans/food recipes, exercise programs, and/or stress management tips that help users cope with certain chronic conditions or improve general fitness. Prior studies document the use of online healthcare interventions in multiple domains, including type 2 diabetes (Lorig et al. 2010), obesity (Krukowski et al. 2008), mental illness (Ybarra and Eaton 2005), alcohol use (White et al. 2010), and smoking cessation (West et al. 2015), among other chronic disorders. Compared with off-line intervention counseling, online healthcare interventions provide more accessible and costeffective information and, thus, may stimulate individuals long-term engagement in health management (Coelho et al. 2005, Tate et al. 2009).

Despite its potential, the choice overload issue may interfere with the online delivery of healthcare interven tions. Typically, online healthcare platforms provide a wide variety of intervention options to satisfy users heterogeneous needs. However, when individuals are provided with too many intervention options, their decision-making performance can drop significantly because of a failure to spot the truly relevant information (California HealthCare Foundation 2017). Most users lack adequate health-management experience, so it is difficult for them to properly evaluate each intervention option. This deters users’ active engagement in healthcare interventions. Though choice overload is not new to online settings, it can create unique issues in the healthcare domain. Researchers argue that a difficult decision-making process results in individuals failing to engage in any intervention (Oulasvirta et al. 2009), which harms their health-management performances (Hibbard et al. 2007). Thus, there is a pressing demand for services that can better promote online interventions with respect to individuals’ healthcare needs.

In this study, we are motivated to develop a personalized healthcare recommendation system, aiming to provide tailored suggestions for individuals’ engagement in online healthcare interventions. The objective is to provide a subset of intervention options to each individual at each time, help users quickly discover the interventions that fit their interests, and improve engagement rates. Whereas recommendation systems are widely studied in e-commerce settings, applying recommendations in healthcare settings can be challenging for the following reasons.

First, because of the evolving nature of health management, individuals’ healthcare preferences usually exhibit strong temporal dynamics. This phenomenon requires service providers to quickly adapt to users’ healthcare needs in real time (Nahum-Shani et al. 2018). Second, the healthcare needs of individuals must be addressed from multiple aspects. Typically, health management involves more than one outcome and/or behavior dimension(s). For example, managing cardiovascular conditions can entail multiple health monitoring (e.g., blood pressure, glucose, and/or cholesterol) and lifestyle changes (e.g., eating and exercising). As such, ideal healthcare recommendations need to cover important health-management aspects to provide well-rounded support. Third, characterizing individuals’ health-management contexts is more demanding and challenging given the complex sequence correlations and event irregularity embedded in users health and behavior trajectories (Morid et al. 2022). It is typical that individuals’ health-management activities are affected by their healthcare experiences, health histories, and social contexts (Johnson et al. 2002). Meanwhile, online healthcare data can contain many formats (e.g., numerical health measures versus categorical and/or textual behavior traits) and contents (e.g., static demographic features versus dynamic behavior sequences). A proper model to jointly process this information is critical to a comprehensive understanding of users’ health-related features and intervention personalization. To date, these challenges remain the major barriers in healthcare recommendation tasks.

We tackle these challenges by proposing a deep learning and diversity-enhanced bandit framework. Bandit is a specialized online machine learning algorithm that enables adaptation to real-time data streams to maximize cumulative payoffs over time (Gittins 1979, Auer et al. 2002). This capability is particularly useful in a dynamic healthcare-recommendation environment as it allows service providers to quickly learn users’ healthcare preference changes and promotes long-term engagement. To further address the challenges in healthcare recommendation diversification and context representation, our framework synthesizes two unique design components. First, we guide our recommendations with a theory-driven diversity promotion scheme, which enables us to structurally diversify interventions along major health-management dimensions. Second, to improve characterization of users’ health-management contexts, we deploy deep learning to capture critical information in healthcare decision making, including not only users’ static attribute features, but also the complex sequence patterns in users’ health histories and health-behavior paths. This enables us to better understand the contextual dependency of users’ healthcare decisions and enhance downstream recommendation. We propose a Thompson sampling (TS)–based algorithm to solve our recommendation as a stochastic optimization task.

We evaluate our proposed recommendation framework through a series of experiments conducted on a real-world data set. Our results provide evidence for the superiority of our approach compared with a wide range of benchmark models. We demonstrate the effectiveness of each design component, and through more granular analyses, we show that our recommendation framework can adapt well to the dynamics and diversity in individuals’ intervention preferences and promote engagement in a larger user population.

Our study makes several contributions to the literature and practice. One major contribution is the proposed healthcare recommendation framework, which demonstrates how prescriptive analytics can be integrated via a design science artifact (Chen et al. 2012, Abbasi et al. 2016) to provide decision-making support for individuals’ health management. The novel aspects of our recommendation framework include (1) a deep representation learning procedure that jointly captures key information in users’ health-management contexts, (2) a domain knowledge–driven diversity promotion design, and (3) a customized online machine learning scheme. From a practical perspective, our recommendation framework addresses real-world challenges in healthcare recommendations and benefits multiple stakeholders, such as users, platforms, and policymakers. We provide a detailed discussion of our contributions at the end of the paper.

## 2. Literature Review and Design Theories

Lifestyle intervention plays an important role in mitigating health risks and improving personal wellness. It is widely shown that poor living habits, such as physical inactivity, smoking, and excessive drinking, are associated with multiple chronic complications (Centers for Disease Control and Prevention 2019). Researchers have made a series of efforts to understand the key factors that affect users’ healthcare decisions. Prior studies suggest that individuals’ health management is a dynamic process, which needs to be understood with respect to specific contexts. According to Johnson et al. (2002), individuals frequently adapt their health behaviors based on their health condition trajectories, health-management experiences, treatment compliance, and self-monitoring. Not only personal health contexts, but also social contexts may play a role in shifting individuals’ healthmanagement behaviors (King et al. 2006, Yan and Tan 2014). Researchers find that the exchange of emotional or informational support among peers may encourage optimism and self-esteem in individuals (DiMatteo 2004), helping them to better comply with a treatment plan and make a behavior change (Krukowski et al. 2008, Johnson and Wardle 2011). In addition to temporal dynamics, prior behavioral health research also suggests that individuals’ healthcare needs are diverse and jointly cover multiple aspects regarding lifestyle changes and self-monitoring of health conditions (Cutler 2004). Researchers argue that well-diversified interventions help maintain users’ attention and reduce dropout rate (Kovacs et al. 2018). These patterns motivate us to incorporate dynamics and diversity-related considerations in a healthcare recommendation design. In the following, we first summarize related literature and identify research gaps in Section 2.1, and then we highlight our kernel design theories in Section 2.2.

## 2.1. Related Work

2.1.1. Overview of Recommendation Systems. The recommendation literature documents various methods and techniques to match users’ preferences in different settings. A large body of research focuses on batch learning–based recommendation methods, such as collaborative filtering, content-based filtering, and hybrid models (Zhang et al. 2019). Batch learning–based recommendation systems use a batch of historical data (e.g., prior purchase records or reviews) to infer users’ preferences (Adomavicius and Tuzhilin 2005, Sedhain et al. 2014). Recent advances in batch learning–based recommendation algorithms include context-aware recommendation systems that capture the context dependency of user behaviors (Chen 2005, Adomavicius and Tuzhilin 2011); model-based approaches, such as matrix factorization that capture latent information in user–item interactions (Mnih and Salakhutdinov 2008, Baltrunas et al. 2011); and deep learning recommenders that extract implicit information from users’ behavior sequence (Tang and Wang 2018, Yuan et al. 2019) and unstructured item content (e.g., news, music, video) (An et al. 2019, Wu et al. 2019).

Despite the various techniques, batch learning–based recommendation systems often face several common challenges. First, a fundamental assumption of batch learning–based recommendations is that the probability of a user choosing an item in the historical data set remains the same at the time of the recommendation. This may fail to capture the dynamic changes in users’ preferences (or environment). Second, most batch learning– based models are designed to maximize short-term rewards without considering the uncertainty and confidence associated with users’ preferences for each item. In other words, an item selected more frequently is more likely to be recommended to a new user. However, the frequency of the selections largely depends on the origi nal data collection policy, that is, the recommendation system itself. Even with frequent retraining, because the collected data always comes from the same recommendation algorithm, the fundamental assumption of batch learning–based models reinforces the same historical recommendation pattern without the chance to explore better options.

The aforementioned challenges can be better addressed by multiarmed bandit (MAB) algorithms, which balance exploitation and exploration through sequential decision making (Auer et al. 2002). Whereas exploitation enables reuse of highly rewarding alternatives from the past to secure immediate short-term rewards, exploration allows decision makers to occasionally deviate from the current “best” option to discover rewards associated with the less-explored actions to minimize long-term opportunity costs. As a form of online machine learning, bandit algorithms are useful to detect dynamic changes in users’ preferences as they are designed to adapt to users’ real-time feedback (Zhao et al. 2019). The balance between exploitation and exploration enables healthcare platforms to maximize long-term user engagement during the recommendation phase, which is essential to both users’ maintenance in health management and platform sustainability.

2.1.2. Healthcare Recommendations. Healthcare recommendations are less explored compared with recommendations in other application settings. Researchers have made several initial efforts to design algorithms to automate the generation of healthcare recommendations (Zaman and Li 2014, Lei et al. 2017, Tomkins et al. 2021). Several studies motivate the use of online machine learn ing to adapt healthcare interventions to users’ changing needs (Paredes et al. 2014, Rabbi et al. 2015, Tewari and Murphy 2017). Nevertheless, prior studies contain several research gaps in recommendation personalization and diversification. For example, a pioneer study (Rabbi et al. 2015) adopts a simple ε-greedy heuristic that exploits 90% of the time from users’ most frequently adopted interventions and explores the infrequent op tions otherwise. This approach does not consider the adaptation to users’ personal health-management contexts. Although other studies incorporate individual heterogeneity in their recommendation designs (Paredes et al. 2014, Tomkins et al. 2021), the sequential patterns in individuals’ health and health-behavior histories are not accounted for. In terms of diversification, prior studies mainly consider increasing the randomness or stochasticity in the recommendations provided (Kovacs et al. 2018). This approach, however, may not guarantee intervention recommendations to cover individuals’ major health-management needs.

## 2.2. Design Principles: Dynamic Online Adaptation

We develop dynamic online adaptation principles to guide our recommendation design. Specifically, we use adaptation to describe the capability of quickly adjusting healthcare services (i.e., interventions) based on users dynamic needs with the goal of improving long-term service outcomes. Based on behavioral health theories, we conceptualize that adaptation in the healthcare recommendation setting should contain the following aspects: (1) adaptation to (unobserved) uncertainty, (2) adaptation to observed dynamics through improving context representation, and (3) adaptation to individuals’ diverse healthcare needs. The first two aspects seek to address challenges in recommendation personalization in a highly dynamic environment, in which the evolution of healthcare-related contexts may not be well-understood. The third aspect addresses the challenge in intervention diversification. Next, we provide a detailed discussion of our kernel theories.

2.2.1. Design Objective. The major objective of our recommendation design is to maximize user engagement. Continuous user engagement indicates maintenance and compliance (Barello et al. 2016) and is positively correlated with improved long-term health outcomes (Hibbard et al. 2007). Eysenbach’s (2005) work on user attrition reveals that, because many online healthcare interventions are self-help based, encouraging continued participation is essential. Consistent with this line of research, our study aims to promote users’ long-term intervention participation through a personalized recommendation framework.

2.2.2. Improving Recommendation Performance Under Uncertainty. Healthcare recommendations should be delivered flexibly to address users’ changing needs. Researchers emphasize the importance of tailoring healthcare interventions based on individuals’ evolving contexts so that “right” interventions can be delivered to the “right” person at the “right” time (Nahum-Shani et al. 2018). In an ongoing recommendation process, as data are obtained sequentially, service providers typically face uncertainty about users’ preferences. This urges the service providers to adopt an online machine learning strategy, which enables adaptive learning of user preferences during the recommendation process. On the one hand, service providers need to leverage users’ historical data to learn about exhibited patterns (i.e., “exploitation”). On the other hand, without full information, service providers need to efficiently gather information regarding the unknowns and detect potential changes in users’ healthcare preferences that were not captured by the data (i.e., “exploration”) (Zhao et al. 2019).

2.2.3. Improving Healthcare Context Representation. Context representation is critical to healthcare recommendation design. It helps service providers understand the dynamic patterns presented in the data so that they can derive insights on how to tailor and generalize interventions based on observed context variables (e.g., individual features, intervention attributes, etc.). Drawing from prominent behavioral health theories, we propose the following principles to improve healthcare context representation.

2.2.3.1. Integrating Static User Features with Dynamic Sequence Features. Health-management context involves both users’ static features (e.g., demographic information) and temporal dynamic features (e.g., health trajectories, health-behavior paths). Integrating both types of features is challenging, yet it is important for accurate healthcare predictions (Morid et al. 2022).

2.2.3.2. Dynamics Associated with Multisequence Data. Individuals’ health management is a self-influenced process that involves multiple dynamics. According to behavioral health theories, key health management– related behaviors include self-monitoring, treatment compliance, and social connections (Johnson et al. 2002). Whereas self-monitoring and treatment compli ance capture essential health-management experiences (Bandura 2004), social connections capture the external social influence on individuals’ health (King et al. 2006). Prior studies indicate that individuals’ health and behavior sequences can share both intersequence and intrasequence correlations. For instance, individuals social interactions can influence the dynamics of their self-management behaviors (Yan 2018, Zhou et al. 2021); how health conditions evolve can depend on individuals health histories (Johnson et al. 2002). In addition to the chronological order, the timing process of a healthcare sequence also matters (e.g., the time intervals between a patient’s visits can vary over time) (Morid et al. 2022). To this end, healthcare sequence data should be jointly processed through careful model design to reveal the implicit information and learn how they reshape individuals’ preferences for future decision making. Although prior literature documents a series of sequence-based approaches (Tang and Wang 2018, Yu et al. 2019, Yuan et al. 2019), the proposed methods consider mainly the sequential order of a single behavior event (e.g., customers’ purchase/click histories) and may not be applicable to healthcare recommendation settings that contain complex multisequence dynamics.

2.2.3.3. Incorporating Impact of Health Outcomes on Individuals’ Preferences. From individuals’ perspectives, intervention participation has two outcomes: engagement and distal health outcomes (the ultimate health goal to achieve) (Nahum-Shani et al. 2018). Health behavior motivation theories suggest that individuals use their health outcomes as feedback to reinforce their health behaviors (Bandura 2004). When individuals observe positive feedback in health outcomes, they tend to increase their engagement in similar behavior interventions and vice versa. This indicates that individuals healthcare intervention preferences are driven by both their personal tastes and the targeted health outcomes.

Learning representations for healthcare interventions can also be more sophisticated as they contain important feature dimensions that need to be evaluated based on health-regulation theories. Healthcare interventions help users establish goals for health and/or healthbehavior changes. Researchers argue that goal setting reinforces individuals’ motivations, and well-structured goal formulation has positive and directional effects on individuals’ task performances (Locke and Latham 1990). To better understand the functionalities of an intervention goal, researchers propose the SMART metric, which stands for five feature dimensions: specific, measurable, attainable, relevant, and time-bound (Doran

1981). The SMART metric is used as a gold standard for evaluating the quality of intervention goals (Ogbeiwi 2018). In this study, we use the SMART metric to guide the learning of intervention representations.

2.2.4. Adaptation to Diverse Healthcare Needs. To guide the diversification of healthcare interventions, we follow the social cognitive theory on self-regulation (Bandura 1991, 2004), which conceptualizes individuals major health-management dimensions in a self-regulation cycle. The theory suggests that individuals need to pay attention to both their health outcomes and health behavior routines. Managing health outcomes enables individuals to understand their progress and identify desirable directions for behavior changes, whereas managing behavior routines helps individuals establish behavior-change skills to tackle challenges and fulfill expectations. These dimensions represent the fundamental needs of individuals’ health management and provide a theoretical guideline for diversifying intervention recommendations. We design a specific diversification scheme to ensure that healthcare recommendations provide support for both individuals’ outcome coping and behavior courses.

2.2.5. Summary. In Table 1, we summarize our design principles and how we use them to address the existing research gaps.

## 3. A Deep Learning and Diversity-Enhanced Online Learning Framework

Building on the design guidelines in the previous section, we propose a deep learning and diversity-enhanced online learning framework for adapting healthcare intervention recommendations. We formulate the learning of the optimal recommendation policy as a constrained contextual bandit problem. Bandit (or multiarmed bandit) is a well-adopted online machine learning framework extensively studied in the fields of statistics and machine learning (Gittins 1979, Auer et al. 2002). It seeks to solve the exploitation-versus-exploration trade-off through leveraging the reward estimation confidence to adaptively update the decision-making policy. To address the challenges in healthcare context representation and adaptation, we consider the contextual bandit setting, in which each action and status of patients are expressed by a set of context features. Other online learning methods $( \mathrm { e . g . }$ , full reinforcement learning with Markovian decision processes (Sutton and Barto 2018) or contextual decision processes (Jiang et al. 2017)) may also be considered. However, they usually require large amounts of data and strong domain knowledge on the system dynamics to be successful. Another difficulty is that many healthcare behavior sequences are exogenous and are neither controlled nor influenced by the recommendation system. Hence, contextual bandits are adopted as a more flexible approach for modeling the complex healthcare context dependency.<sup>1</sup> We integrate bandit with a theory-guided diversity promotion constraint to enhance the recommendation diversity along desired dimensions. In addition, we augment the bandit design with deep learning neural networks to facilitate learning of unstructured healthcare information, such as individuals’ health-management sequences and intervention characteristics.

Table 1. Summary of Design Principles, Research Gaps, and Design Components

<table><tr><td>Dynamic online adaptation principles</td><td>Targeted research gaps</td><td>Design components</td></tr><tr><td>Adaptation to data uncertaintyThe necessity to adapt to new user preference patterns in a real-time fashion</td><td>Many studies focus on batch learning-based recommendation; existing online machine learning algorithms present research gaps in context representation and diversification.</td><td>Online machine learning framework with neural-enhanced contextualization and theory-guided diversity promotion scheme</td></tr><tr><td rowspan="2">Adaptation to observed healthcare context dynamicsIntegrating static user features with dynamic sequence featuresCapturing dynamics associated with multiple sequencesIncorporating the impact of health outcomesImproving intervention characterizationAdaptation to diverse healthcare needsImproving diversity promotion by identifying major health-management dimensions</td><td>The hybrid combination of both users’ static features and dynamic sequence features is important yet challenging and understudied in a healthcare context. In addition, complex dynamics associated with users’ multiple health and behavior sequences, such as the intrasequence and intersequence correlations and event irregularity, are not considered.</td><td>A wide and deep neural network with an enhanced LSTM module and health-outcome auxiliary loss to improve user representation, and a deep neural network based on SMART metric to improve intervention representation</td></tr><tr><td>Prior diversity promotion techniques mainly focus on increasing the randomness in recommendations; key health-management dimensions are not incorporated to guide the diversification.</td><td>Theory-driven diversity promotion constraint</td></tr></table>

Figure 1 provides an illustration of our design. The design artifact takes a series of user and item (i.e., intervention) features as input, and then the features are fed into the deep learning networks to extract deep embeddings for users and items to enhance context representations. We use a diversity-enhanced bandit algorithm, shown on the right side of Figure 1, to adaptively learn users’ preferences during the recommendation procedure. In the following, we describe the diversityenhanced contextual bandit problem and elaborate on the deep neural network designs.

## 3.1. Optimizing Intervention with Diversity-Enhanced Bandit

3.1.1. Problem Setup. The recommendation problem we consider is to adaptively provide the best K healthcare interventions to each user in each period $( \mathrm { i . e . , }$ , week) with the goal of maximizing users’ overall engagement in online healthcare interventions during the entire recommendation periods. Suppose there are I users on the platform, and the total number of recommendation periods is $T .$ . Each period $t ,$ the platform chooses from the available intervention set $C _ { t }$ and provides a subset of interven tions $S _ { i t }$ that contains K intervention options to each user $i ,$ that is, $S _ { i t } \subseteq C _ { t }$ . The choice set $C _ { t }$ may vary with time. Let $r _ { t } ( i , k )$ denote user i‘s engagement decision for intervention k. This information serves as a feedback or “reward” for the platform’s recommendations. In the fol lowing periods, the platform uses the feedback to update its knowledge about users’ preferences and adjust its subsequent recommendations.

We solve this recommendation task using a contextual bandit model and leverage recommendation decisions upon a set of contextual features of the environment, including the attributes of intervention alternatives and user characteristics. We denote users’ health-management contexts as $\mathbf { x } _ { i t }$ and attributes of healthcare interventions as $\mathbf { z } _ { k }$ . We assume that users’ feedback, that is, the intervention engagement decision $r _ { t } ( i , k )$ , is stochastically generated by an underlying probability that depends on $\mathbf { x } _ { i t }$ and $\mathbf { z } _ { k } \mathbf { : }$

$$
E [ r _ {t} (i, k) \mid \mathbf {v} _ {i t k} ] = (1 + \exp (- \pmb {\theta} _ {*} ^ {T} \mathbf {v} _ {i t k})) ^ {- 1},\tag{1}
$$

where $\mathbf { v } _ { i t k }$ is the overall context vector containing x<sub>it</sub>, z<sub>k</sub> and their interactions; h<sub>∗</sub> denotes the underlying coefficient vector. The parameter vector h is unknown to the decision makers and needs to be learned adaptively during the recommendation process by balancing the exploitation-versus-exploration trade-off. The objective is to maximize the expected cumulative user engagement during the entire course of recommendation, that is,

$$
\max _ {S _ {i t}} \sum_ {t \in [ T ]} \sum_ {i \in [ I ]} \sum_ {k \in S _ {i t}} E [ r _ {t} (i, k) \mid \mathbf {v} _ {i t k} ].\tag{2}
$$

Figure 1. (Color online) A Deep Learning and Diversity-Enhanced Online Learning Framework  
![](/api/attachments/PBUN65Y8/fulltext/images/dc3196079362f533e1ed646d85d2e7642ec0601d4ae55364aef0e2941814fe9e.jpg)

Table 2. Summary of Major Notations

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $I, i$ </td><td> $I$  denotes the total number of users with  $i$  being the user index</td></tr><tr><td> $T, t$ </td><td> $T$  denotes the total number of periods with  $t$  being the period index</td></tr><tr><td> $K, k$ </td><td> $K$  denotes the number of interventions recommended with  $k$  being the intervention index</td></tr><tr><td> $C_t$ </td><td>The available intervention set each period</td></tr><tr><td> $S_{it}$ </td><td>The recommendation set,  $|S_{it}| = K$ </td></tr><tr><td> $r_t(i,k)$ </td><td>User  $i$ &#x27;s engagement decision on intervention  $k$  at period  $t$ </td></tr><tr><td> $\mathbf{x}_{it}$ </td><td>User  $i$ &#x27;s health-management context at period  $t$ (learned through deep learning in our model)</td></tr><tr><td> $\mathbf{z}_k$ </td><td>Attributes of intervention  $k$  (learned through deep learning in our model)</td></tr><tr><td> $\mathbf{v}_{itk}$ </td><td>Context vector containing  $\mathbf{x}_{it}, \mathbf{z}_k$  and their interactions</td></tr><tr><td> $\boldsymbol{\theta}_*$ </td><td>Underlying coefficient vector in the logistic reward predictor</td></tr></table>

We provide a summary of the major notations in our recommendation problem in Table 2.

3.1.2. Structured Diversity Promotion. A bandit algorithm naturally promotes recommendation diversity through making exploratory decisions. Nevertheless, healthcare recommendations require a more refined diversification scheme to account for individuals’ needs in multiple aspects. In light of the social cognitive theory, we conceptualize two major health-management dimensions: outcome- and behavior-oriented dimensions. The former refers to an individual’s need to selfattend to health outcomes, whereas the latter refers to the need to self-manage behavior routines. Both dimensions may contain several subdimensions. For instance, as chronic conditions are often correlated, individuals may need to jointly manage multiple health aspects (e.g., blood pressure and/or cholesterol). Health behaviors may also include multiple types, such as diet, physical activity, smoking, substance use, and sleep (Short and Mollborn 2015). In many health-management scenarios, individuals may need to focus on more than one type of health behavior. To provide comprehensive intervention suggestions, we integrate the following diversity promotion constraint into the bandit framework to structurally mixing intervention recommendations:

$$
\begin{array}{c} D = \{| S \cap d i m _ {o u t c o m e 1} | \geq 1, | S \cap d i m _ {o u t c o m e 2} | \geq 1, \ldots , \\ | S \cap d i m _ {b e h a v i o r 1} | \geq 1, | S \cap d i m _ {b e h a v i o r 2} | \geq 1, \ldots \}, \end{array}\tag{3}
$$

where S denotes the recommendation set; $d i m _ { o u t c o m e }$ denotes the outcome-oriented dimension(s), and $d i m _ { b e h a v i o r }$ denotes the behavior-oriented dimension(s), which need to be customized based on specific health-management contexts. The diversity promotion constraint ensures that the recommendation set contains at least one intervention for each type.

Incorporating the diversity promotion constraint leads to a stochastic optimization task, in which the exploration of bandit is guided by preset theory-driven dimensions. To solve this task, we propose an algorithm that is adapted from TS. TS is best understood in a Bayesian setting in which it computes the posterior distribution of the unknown parameters h in the likelihood function (Equation (1)) given the realized stochastic feedback. The rationale of TS is to encourage exploration through prob ability matching. That is, in each round, TS randomly draws alternatives according to its probability of being optimal. Research shows that TS generally has better empirical performance than alternative bandit algorithms, such as Upper Confidence Bound (UCB) and ε- greedy (Chapelle and Li 2011). We propose a TS variant (Algorithm 1) that provides a solution for the constrained stochastic optimization problem with the goal of maxi mizing users’ cumulative engagement over time subject to the diversity constraint.

Algorithm 1 (TS Algorithm with Diversity Constraint) Input: Prior mean $m _ { j }$ and prior variance $\sigma _ { j }$ for each parameter $\theta _ { j } , j = 1 , \dot { 2 } , \ldots d ;$ constant λ that controls the extent of exploitation and exploration. For $t = 1 , 2 , \dots , \bar { T }$ do

For each available intervention, pass the title and description data to construct item embeddings $\mathbf { z } _ { k }$ , $k \in C _ { t } ;$

For $i = 1 , 2 , \dots , I$ do

Construct user representation $\mathbf { x } _ { i t }$ using data prior to period t

$( \mathrm { i . e . , } D ^ { t } = \{ a _ { 1 } , a _ { 2 } , \ldots , a _ { n } , \{ s _ { 1 } ^ { 1 } , \ldots s _ { 1 } ^ { t - 1 } \} , \{ s _ { 2 } ^ { 1 } , \ldots s _ { 2 } ^ { t - 1 } \} , \ldots ,$ $\bigl \{ s _ { m } ^ { 1 } , \ldots s _ { m } ^ { t - 1 } \bigr \} \bigr \} \bigl ) .$

Step 1 (random draw):

Draw $\hat { \theta } _ { j }$ from $N ( m _ { j } , \lambda \dot { \sigma } _ { j } ) . \hat { \pmb { \theta } } = ( \hat { \theta } _ { 1 } , \hat { \theta } _ { 2 } , \dots , \hat { \theta } _ { d } ) .$

For arm $k \in C _ { t }$ do

Compute expected reward: $\hat { r } _ { t } ( i , k ) = ( 1 + \exp $ $( - \mathbf { v } _ { i t k } ^ { T } \hat { \mathbf { \theta } } ) ) ^ { - 1 }$ , where the context vector $\mathbf { v } _ { i t k }$ contains user embedding $\mathbf { x } _ { i t } ,$ item embedding $\mathbf { z } _ { k } ,$ , and their interaction terms vec $\left( \mathbf { x } _ { i t } \otimes \mathbf { z } _ { k } \right)$ ).

End for

Step 2 (Optimization):

Solve the following optimization problem:

$$
\begin{array}{l} \max _ {q _ {k}, k \in C _ {t}} \sum_ {k = 1} ^ {K} \hat {r} _ {t} (i, k) q _ {k} \\ s. t. \quad \sum_ {k \in d i m _ {o u t c o m e}} q _ {k} \geq 1, (\text { for   each   outcome   dimension }) \\ \sum_ {k \in d i m _ {b e h a v i o r}} q _ {k} \geq 1, (\text { for   each   behavior   dimension }) \\ \sum_ {k \in C _ {t}} q _ {k} \leq K, q _ {k} = 0 \text { or } 1 (\forall k). \end{array}
$$

Offer item k to individual i if $\begin{array} { r } { q _ { k } ^ { * } = 1 . \ S _ { i t } = \{ \forall k , } \end{array}$ $q _ { k } ^ { * } = 1 \}$ End for

Observe users’ feedback $r _ { t } ( i , k ) , \ i \in [ I ] , \ k \in S _ { i t }$ and update users’ sequence data: $s _ { 1 } ^ { t } , \ldots , s _ { m } ^ { t }$ Update the posterior mean by

$$
\begin{array}{l} \mathbf {m} = \underset {\boldsymbol {\theta}} {\arg \min} \frac {1}{2} \sum_ {j = 1} ^ {d} \sigma_ {j} ^ {- 1} (\theta_ {j} - m _ {j}) ^ {2} \\ \qquad + \sum_ {i = 1} ^ {I} \sum_ {k \in S _ {i t}} \log (1 + \exp (- r _ {t} (i, k) \boldsymbol {\theta} ^ {T} \mathbf {v} _ {i t k})). \end{array}
$$

Update the posterior variance by

$$
\sigma_ {j} ^ {- 1} = \sigma_ {j} ^ {- 1} + \sum_ {i = 1} ^ {I} \sum_ {k \in S _ {i t}} v _ {j i t k} ^ {2} p _ {i t k} (1 - p _ {i t k}),
$$

where $p _ { i t k } = ( 1 + \exp { ( - { \bf m } ^ { T } { \bf v } _ { i t k } ) } ) ^ { - 1 } ,$ , v<sub>jitk</sub> is the $j \mathrm { t h }$ element of $\mathbf { v } _ { i t k }$

## End for

In each iteration, our algorithm randomly draws a posterior parameter vector to calculate the expected reward (whether the user selects each intervention), which depends on the context information of users and intervention features. The user context is constructed dynamically using the data prior to the current period. Specifically, at period $t ,$ only the data (e.g., health records, intervention histories, etc.) from periods 1 to t � 1 are passed into the trained neural network to construct the user embedding/features. The neural network is trained separately from the main recommendation procedure. Our algorithm then solves an optimization problem based on the calculated expected rewards, subject to the diversity promotion constraint, to generate the top-K recommendations for each user.<sup>2</sup> After collecting user feedback, the algorithm updates the posterior distributions for the parameters and enters the next iteration. We obtain the Laplace approximation of the logistic predictor and apply the Bayes rule to update the parameters. Because we do not have prior knowledge of the parameter values, we set the prior means to be zero and the prior variances to be equally valued, which is equivalent to l<sub>2</sub>-regularized logistic regression.

## 3.2. Deep Learning–Based Contextualization

We propose a deep learning procedure to improve user and item representation in the healthcare context. Our context representation leverages two unique deep learning models to extract user and item embeddings.

3.2.1. User-Embedding Model. Our user-embedding model leverages a wide and deep neural network to combine users’ static attribute and dynamic sequence features that are relevant in an online health-management environment. The wide and deep structure was originally proposed for user response modeling in mobile apps (Cheng et al. 2016) to combine a wide set of cross-product feature transformations and a deep feed-forward neural network for representation of sparse, high-dimensional categorical features. We adopt the gen eral idea of the wide and deep architecture and yet innovate the two branches in the following ways. We build a “wide” branch to process users’ attribute features, considering that certain intervention suggestions can be more actionable for specific users given their static attributes. We design a “deep” branch that builds upon long short-term memory (LSTM) and an attention mechanism to learn the sequential dynamics in the time-series features.

The static features can usually be obtained from user profiles, such as gender, age, and membership duration. The dynamic sequence features can be tracked through users’ online footprints, such as their health-management activities. Based on prior health studies and theories (Johnson et al. 2002, King et al. 2006, Yan and Tan 2014), we identify the following sequence features that are criti cal in users’ health-management contexts: the history of users’ health conditions, history of interventions, selfmonitoring activities, and social activities. Online health care platforms can find proxies for these sequence features through their functionality. For instance, many healthcare platforms enable users to track their health variations; this allows us to extract information regarding users’ self-monitoring activities and logged health histories (Lupton 2013). Users can also participate in social activities, such as publishing posts in a health forum, making friends, and supporting each other (Yan and Tan 2014); these activities enable platforms to obtain proxies for the social influence on users’ health management. Our user-embedding network structure enables learning from multiple sequence features of different formats (cat egorical, numerical, and/or textual), so we can flexibly leverage information from multiple sources to improve user representation.

Specifically, we denote the static attribute features as $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ and convert them into one-hot encoding if the attribute is categorical. We apply normalization to the numerical features with mean zero and standard deviation one. The converted attribute features are $\tilde { a } _ { 1 } ,$ $\widetilde { a } _ { 2 } , \ldots , \widetilde { { a } } _ { n }$ . We concatenate them to get a single vector a˜ as the input for the wide branch and apply a standard three-layer fully connected neural network (with dimensions 256, 128, and 64, respectively) to account for possible interactions among the attribute features. After the fully connected layers, we obtain a vector $\xi _ { 3 } ,$ , which is the endpoint of the shallow attribute features.

We use $s _ { 1 } ^ { t } , s _ { 2 } ^ { t } , \ldots , s _ { m } ^ { t }$ to denote the deep sequence features, where t is the time coordinate. We use BERT embedding for each text feature (e.g., posts published by users at time t) and one-hot encoding for categorical features, and the raw deep input features are converted to $\tilde { s } _ { 1 } ^ { t } , \tilde { s } _ { 2 } ^ { t } , \ldots , \tilde { s } _ { m } ^ { t }$ . To tackle the challenges in handling mul tiple sequence features as noted in Section 2.2, we propose using an enhanced LSTM module, called eLSTM, to first simultaneously transform all the sequential features into a single meta-sequence via learnable weights and then use the compound node within the meta-sequence to quantify the user’s states. Formally, we first apply a transformation to each of the encoding sequences:

$$
\begin{array}{r l} & r _ {1} ^ {t} = \mathrm{Relu} (W _ {1} ^ {S} \tilde {s} _ {1} ^ {t} + b _ {1} ^ {S}), r _ {2} ^ {t} = \mathrm{Relu} (W _ {2} ^ {S} \tilde {s} _ {2} ^ {t} + b _ {2} ^ {S}), \ldots , \\ & r _ {m} ^ {t} = \mathrm{Relu} (W _ {m} ^ {S} \tilde {s} _ {m} ^ {t} + b _ {m} ^ {S}). \end{array}\tag{4}
$$

This transformation brings together different features with different scales in different spaces, followed by a concatenation operation:

$$
\tilde {r} ^ {t} = \mathrm{Concat} (r _ {1} ^ {t}, r _ {2} ^ {t}, \ldots , r _ {m} ^ {t}).\tag{5}
$$

Then, we apply another nonlinear transformation to further merge the information for different sequences to get a unified input sequence of encodings as

$$
x ^ {t} = \mathrm{Relu} (\tilde {W} ^ {S} \tilde {r} ^ {t} + \tilde {b} ^ {S}).\tag{6}
$$

We apply an LSTM module to this unified input sequence and obtain a sequence of latent vectors $[ h _ { 1 } ,$ $\bar { h } _ { 2 } , \ldots , h _ { t } ]$ . Note that the length of the sequence t is also a variable because we build user representations given a history chunk with any size.

Furthermore, instead of forming a dense sequence with equal spacing as in natural language processing applications, our problem sees event irregularity when two consecutive intervention selections may be separated by a different number of idle days. No activities and repeated intervention selections may imply different user engagement. For example, if a user has no activities for some periods, then the user might prefer lighter exercises to start over. Hence, we apply the self-attention mechanism to automatically identify patterns within the sequence that may affect users’ preferences (e.g., the order of the events, idleness between intervention selections, etc.), and the weight patterns of each event in the sequence is learned during training. As such, more informative patterns get higher weight via the attention mechanism, which eventually become stronger signals in the latent space. The attention score is learned from a fully connected network:

$$
u _ {t} = \tanh (W ^ {a t t} \cdot h _ {t} + b ^ {a t t}),\tag{7}
$$

$$
\chi_ {t} = \exp (u _ {t} \cdot v) / \sum_ {t} \exp (u _ {t} \cdot v),\tag{8}
$$

$$
\eta_ {1} = \sum_ {t} \chi_ {t} h _ {t}.\tag{9}
$$

Concatenating the endpoint of the shallow branch $\xi _ { 3 }$ and the endpoint of the deep branch $\eta _ { 1 } ,$ we obtain a latent layer combining the information from both the wide features and the deep features:

$$
\phi_ {1} = \operatorname{Concat} (\xi_ {3}, \eta_ {1}).\tag{10}
$$

We enhance the deep branch by an auxiliary loss function with healthcare outcome as the goal. The considerations are twofold. First, we use the auxiliary loss to incorporate the effects of health outcomes on individuals’ preferences on interventions. This is unique to the healthcare recommendation setting in which individuals’ health behaviors can be fundamentally driven by the goal of optimizing their health outcomes (Nahum-Shani et al. 2018). Second, as a related task, the auxiliary loss side-head can guide the main model to properly extract relevant signals from the sequence features, especially when the main task is noisy or with limited data. Otherwise, the gradient flow is unbalanced and dominated by the shallow structure. For the auxiliary-loss branch, we apply fully connected operators to the endpoint of the deep features:

$$
\eta_ {2} = \mathrm{Relu} \big (W _ {1} ^ {u s e r} \phi_ {1} + b _ {1} ^ {u s e r} \big),
$$

$$
\eta_ {3} = \mathrm{Relu} (W _ {2} ^ {h e a l t h} \eta_ {2} + b _ {2} ^ {h e a l t h}).\tag{11}
$$

(12)

The auxiliary prediction $\eta _ { 3 }$ is a prediction of the health outcome $\alpha ( i , t )$ . We choose a combined loss of mean squared error for absolute value prediction and crossentropy loss for the health-variation sign prediction, considering that both provide important signals for health outcome prediction. Finally, the full loss function for user representation learning is written as

$$
\begin{array}{l} L = - \frac {1}{| \Omega |} \omega_ {1} \sum_ {(i, t) \in \Omega} \frac {f (i , t) \cdot c (i , t)}{| | f (i , t) | | _ {2} | | c (i , t) | | _ {2}} \\ \qquad + \frac {1}{| \Omega |} \sum_ {(i, t) \in \Omega} \Big \{\omega_ {2} \big | \eta_ {3} - \alpha (i, t) \big | ^ {2} \\ \qquad + \omega_ {3} C r o s s E n t r o p y (s i g n (\eta_ {3}), s i g n (\alpha (i, t))) \Big \}, \end{array}\tag{13}
$$

where $\Omega = \{ ( i , t ) \}$ there exists a selection from user i at time t}, |Ω| denotes the cardinality of set Ω, and $\Vert \cdot \Vert _ { 2 }$ is the $l _ { 2 }$ norm. The first part of the loss function measures the distance of the last hidden layer (user embedding) f (i, t) and item embedding $c ( i , t ) ^ { 3 }$ of the chosen intervention, and the remaining part measures the health outcome–driven auxiliary loss. The full loss function is a weighted combination of these losses with weights ω<sub>1</sub>, ω<sub>2</sub>, and ω<sub>3</sub>. More details of the user-embedding model are provided in Online Appendix A2. Figure 2 contains an illustration of the proposed deep learning architecture for user embedding construction.

3.2.2. Item-Embedding Model. Our item-embedding model is generically designed based on the text format of online healthcare interventions. Typically, online healthcare interventions are presented by a keyword title that highlights the main intervention theme to facilitate user search and a longer paragraph to describe detailed intervention information. For example, an exercise intervention may be titled “running camp,” which instructs users to achieve running goals (e.g., number of miles to run on a daily/weekly basis, etc.). To capture the semantics embedded in online healthcare interventions, we build a hybrid model in which we apply LSTM to learn the semantics of intervention descriptions and use average token-level embedding to extract signals from intervention titles. Formally, taking intervention title n(k) and description d(k) as inputs, we first apply pretrained token-level embedding to the tokenized title and description of an intervention k to obtain $\gamma _ { n } ( k ) = ( \gamma _ { n } ( k ,$ $1 ) , \gamma _ { n } ( k , 2 ) , \ldots , \gamma _ { n } ( k , l _ { k } ) )$ and $\gamma _ { d } ( k ) = ( \gamma _ { d } ( k , 1 ) , \gamma _ { d } ( k , 2 ) , \ldots ,$ $\gamma _ { d } ( k , s _ { k } ) )$ ). Then, the flattened title vector is calculated as $\begin{array} { r } { \tilde { \gamma } _ { n } ( k ) = \frac { 1 } { l _ { k } } \sum _ { j = 1 } ^ { l _ { k } } \gamma _ { n } ( k , j ) } \end{array}$ , and the flattened description is calculated as the vanilla LSTM processed tokensequence $\widetilde { \gamma } _ { d } ( k ) = L S T M ( \gamma _ { d } ( k , 1 ) , \gamma _ { d } ( k , 2 ) , \ldots , \gamma _ { d } ( k , s _ { k } ) )$

Figure 2. (Color online) Illustration of the Base Architecture of the User-Embedding Model  
![](/api/attachments/PBUN65Y8/fulltext/images/f9b1df5afbe04bf7cdb0a48379cf5e63cc37b30f26b90c506d5bd173796d2419.jpg)

We concatenate the flattened name vector and description vectors, followed by three fully connected layers. For the pretrained token-level embedding, we adopt the FastText model, which can leverage subtoken information for token embedding. We fine-tune the token-level embeddings to ensure low information loss. The dimension of LSTM cell latent vector is set to 100, which equals the FastText dimension; hence, the contributions of the intervention title and description are balanced. The dimensions of the fully connected layers are 256, 64, and 16, respectively. The output of the itemembedding network maps to the key intervention meta attributes based on the SMART metric (Doran 1981, Ogbeiwi 2018), including specificity (whether the intervention is specifically defined), measurability (whether the intervention goal is measurable), attainability (the intensity level of the intervention), relevancy (whether the intervention is related to a specific aspect, such as diet or physical activity), and duration (the time span of the intervention). Intervention duration is an integer variable, and the others are categorical. Let att $r _ { \mathrm { i n t e r v } } ( \bar { k } , j )$ denote the jth attribute of intervention k. The loss at the end is a weighted combination of the cross-entropy for the categorical meta attributes and the mean squared error for intervention duration; that ${ \mathrm { i } } \mathbf { s } ,$

$$
\begin{array}{c} O B J _ {\text {interv}} = w _ {1} M S E (a t t r _ {\text {interv}} (k, 0), F _ {\text {interv}} ^ {0} (\tilde {\gamma} _ {n} (k), \tilde {\gamma} _ {d} (k))) \\ + w _ {2} \sum_ {j > 0} C r o s s E n t r o p y (a t t r _ {\text {interv}} (k, j), \\ F _ {\text {interv}} ^ {j} (\tilde {\gamma} _ {n} (k), \tilde {\gamma} _ {d} (k))), \end{array}\tag{14}
$$

where we use $a t t r _ { \mathrm { i n t e r v } } ( k , 0 )$ to denote intervention dura tion and $w _ { 1 }$ and w<sub>2</sub> represent the weights.

## 4. Evaluation: Context and Design

We evaluate our recommendation framework on a real-world data set collected from a leading online weight-loss community in the United States. Weight management represents a typical setting for personal health management, in which individuals regulate their living routines to maintain healthy body weight. Given the prevalence of overweight and obesity, weight management is now a popular topic in many online health care platforms. The focal platform provides healthcare interventions called weight-loss challenges to help users lose/control weight. Typical weight-loss challenges require users to modify a dietary behavior (e.g., “No food after $7 \mathrm { p . m . ^ { \prime \prime } } )$ or increase participation in certain physical activities (e.g., “30-minute jogs twice per week”). We provide a screenshot for the weight-loss challenges in Online Appendix A3.

Our data collection window is from January 1 to April 30, 2014. During this time, there were 1,049 users who participated in at least one intervention. We collected users’ intervention participation histories on a weekly basis, which help us to learn their evolving preference patterns. For each user, we collected a series of auxiliary information, including gender, age, initial weight, membership duration, weekly weigh-in records, number of friends, and posts published in the community forum. This helps us build users’ health-management contexts on the platform. We collected challenge textual information (title and description) to learn intervention representations. In our data set, there were 165 challenges that were chosen by at least one user. A summary of data statistics is provided in Online Appendix A4.

## 4.1. Descriptive Analysis of the Data

In this section, we conduct a descriptive analysis of users challenge participation patterns to provide empirical evidence for the dynamics and diversity in users’ intervention preferences. Users, on average, chose about two challenges per week. When users chose any challenge, they chose multiple challenges about 70% of the time. To shed light on users’ participation diversity, we examine the types of challenges they chose. In general, the challenges contain three types: interventions that require users to modify a dietary behavior (diet-oriented), interventions that encourage users to increase physical activities (exercise-oriented), and interventions that aim for a weight change in a certain period (weight loss–oriented). The diet- and exercise-oriented challenges provide behavioral guidance for individuals’ weightmanagement routines, whereas weight loss–oriented challenges help users establish outcome-driven motivation. We find that users tended to choose different types of challenges whenever they chose multiple challenges. Specifically, users chose more than two types of challenges 92% of the time, and they chose all three types of challenges roughly 51% of the time. These results confirm that users’ preferences on healthcare interventions are often diverse and cover multiple aspects.

In addition, users’ challenge preferences are shown to drift over time. To quantify the extent to which users preferences changed, we calculate the proportion of time that users selected a different challenge type. Specifically, for each time stamp, we denote users’ challenge selections as a three-dimensional vector with each dimension representing whether the user selected a particular challenge type (e.g., diet-, exercise-, weight loss–oriented). For instance, if a user participated in diet- and exerciseoriented challenges for week $t ,$ the corresponding selection vector is $v e c _ { i t } = \left( 1 , 1 , 0 \right)$ . We calculate the overlap ratio of two adjacent selection vectors by $v e c _ { i t - 1 } \cdot v e c _ { i t } /$ $s u m ( v e c _ { i t - 1 } )$ . The higher the overlap ratio, the less variation in users’ preferences. Our results show that the average overlap ratio in users’ challenge selection data is 0.37, which indicates strong dynamics in users’ challenge preferences.

## 4.2. Model Operationalization

As noted in Section 3.2, our user-embedding model adopts a wide and deep network structure to jointly process users’ static attributes and sequence features. In our evaluation context, users’ attribute features include gender, age, initial weight, and membership duration. The sequence features we construct include the following: users’ historical weigh-in records, challenge selections, number of weigh-ins, number of friends, and published forum posts. Weigh-in records track users weight variations and offer a proxy for users’ health trajectories, the sequence of challenges chosen by individuals accounts for users’ health-management experiences and reflects personal preferences on interventions, the number of weigh-ins measures users engagement in self-monitoring, and the number of friends and the published forum posts capture users social behaviors. We provide a summary of these features in Online Appendix A5. For the main loss function (Equation (13)), as the three losses are in the same scale, we adopted equal weights in our experiments. More careful considerations can be given by (expensive) grid search or dynamic weighting strategies.

Our item-embedding model takes challenge title and description as the inputs and the annotated challenge meta attributes as the outputs. Table 3 provides a summary of the output features. The first nine attributes are based on the SMART metric. We also consider two features that may affect individuals’ intervention participation: motivational and self-monitoring. Motivational measures whether a challenge statement contains motivational words/sentences to encourage user participation. Self-monitoring describes whether a challenge requires individuals to regularly report their weightloss progress. These features can help users build inner motivation (Locke and Latham 1990, Bandura 1991) and, thus, likely affect their challenge preferences. The detailed annotation procedure is discussed in Online Appendix A6.

Table 3. Annotation of Challenge Meta Attributes

<table><tr><td>Features</td><td>Definition</td></tr><tr><td>Specific</td><td>Whether a challenge is specifically defined (0 or 1)</td></tr><tr><td>Measurable</td><td>Whether a challenge goal is measurable (0 or 1)</td></tr><tr><td>Diet</td><td>Whether a challenge is related to dietary behaviors (0 or 1)</td></tr><tr><td>Intensity_Diet</td><td>Intensity level for a diet-oriented challenge (L, M, H)</td></tr><tr><td>Activity</td><td>Whether a challenge is related to physical activities (0 or 1)</td></tr><tr><td>Intensity_Activity</td><td>Intensity level for an activity-oriented challenge (L, M, H)</td></tr><tr><td>Weight-Loss</td><td>Whether a challenge contains a goal for weight changes (0 or 1)</td></tr><tr><td>Intensity_Weight_Loss</td><td>Intensity level for a weight loss-oriented challenge (L, M, H)</td></tr><tr><td>Duration</td><td>Time span (in weeks) of a challenge</td></tr><tr><td>Motivational</td><td>Whether a challenge contains motivational words/sentences (0 or 1)</td></tr><tr><td>Self-Monitoring</td><td>Whether a challenge requires individuals to regularly monitor and report their weight-loss progress, for example, body weight, daily diet, running mileage (0 or 1)</td></tr></table>

Figure 3. (Color online) t-SNE Visualization of Challenge Embeddings  
![](/api/attachments/PBUN65Y8/fulltext/images/5f5c360015ec007730c6f6742e9eea86c42091da53bae37e5d857cf6d8b97439.jpg)

To operationalize the diversity promotion constraint, we identify and incorporate the following dimensions: weight loss, diet, and exercise. Weight loss relates to selfmanaging body weight, which is the primary outcomedriven dimension in our context. Diet and exercise represent the major behavior dimensions individuals need to focus on in a weight-management process. We specify the diversity promotion constraint as follows: $\begin{array} { r } { \bar { D } = \left\{ \left| S \cap d i m _ { w e i g h t l o s s } \right| \geq 1 , \left| S \cap d i m _ { d i e t } \right| \geq 1 , \left| S \cap d i m _ { e x e r c i s e } \right| \geq 1 \right\} } \end{array}$ where S represents the recommendation set at each round. As such, we ensure that our recommendations contain at least one diet-, one exercise-, and one weight loss–oriented challenge at a time.

## 4.3. t-Distributed Stochastic Neighbor Embedding (t-SNE) Visualization of Context Embeddings

We use t-SNE visualization to provide intuitional insights on the constructed embeddings. t-SNE is a nonlinear dimensionality reduction technique that is well-suited for deconstructing high-dimensional data (van der Maaten and Hinton 2008). It can project high-dimensional vectors into lower dimensions without changing the data structure such that two points that are shown close to each other in a t-SNE plot have similar embeddings. We present the visualization results for challenge embeddings in Figure 3. The results show that challenges belonging to the same type are tightly clustered. In addition, within each challenge-type cluster, challenges of the same intensity level tend to be close to each other. These patterns indicate that our learned item embeddings can capture intrinsic challenge attributes effectively.

The t-SNE plot for our constructed user embeddings is presented in Figure 4(a). As our model incorporates users’ time-varying sequence features, each user generates different embeddings at different times. We distinguish users’ gender, age groups,<sup>4</sup> and in-period weight-loss status to show the clustering patterns. Our visualization results show that users gather into sequence clusters when they have similar features. For example, we find that each sequence cluster typically comprises the same gender. Users of a similar age range are clustered close together. Finally, we find that users whose weight remains unchanged tend to show up together, whereas users with weight changes tend to gather elsewhere. The sequence shape of the clusters in Figure 4(a) motivates us to further investigate granular individual-level patterns as the points in a sequence are likely generated by the same or similar users. We randomly sampled several individual users and plotted their embeddings in Figure 4(b). As can be seen, the em beddings of the same user are located close together and tend to be concatenated into a trajectory, whereas the embeddings of different users are located relatively far apart. These results indicate that the sequential patterns in users’ health-management behaviors are captured by our user-embedding model.

Figure 4. (Color online) User Embedding t-SNE Visualization  
(a)  
![](/api/attachments/PBUN65Y8/fulltext/images/027502282a6b5ce22e2c19f4ef21af5069d8fe542f3379a70de38cdaad26908f.jpg)  
Note. (a) Full Visualization. (b) Samples Users.

(b)  
![](/api/attachments/PBUN65Y8/fulltext/images/8896155abbcae0dacd936e61ee47ef5856a928afbeaf2a16a5b89015e60a51ab.jpg)

## 5. Performance Analysis and Results

We conduct a variety of experiments to rigorously evaluate the performance of our recommendation framework. In Section 5.1, we compare our recommendation framework with a wide range of state-of-the-art recommendation systems to demonstrate the effectiveness of our model design. In Section 5.2, we granularly test our design components, such as the diversity promotion scheme and deep context representation. We particularly examine our model performance in adapting to users’ dynamic preferences in Section 5.3. To demonstrate how our model improves healthcare recommendation diversity, we examine the diversity distribution in recommendations in Section 5.4. We further demonstrate the macroutility of our recommendation in user improvement in Section 5.5. Finally, as an extension, we discuss how our recommendation framework can be used to improve health-oriented outcomes in Section 5.6.

## 5.1. Experiment 1: Comparison with Benchmark Recommendation Systems

To demonstrate the overall effectiveness of our proposed recommendation framework, we compare it with a series of state-of-the-art recommendation systems. Because a large amount of recommendation literature focuses on batch learning–based methods, we incorporate various batch models, such as context-aware collaborative filtering (CACF) (Chen 2005), social collaborative filtering (SCF) (Sedhain et al. 2014), probabilistic matrix factorization (PMF) (Mnih and Salakhutdinov 2008), context-aware matrix factorization (CAMF) (Baltrunas et al. 2011), standard content-based filtering approach (CB), a hybrid model that mixes CB with standard collaborative filtering (hybrid\_pure), and hybrid model that mixes CB and CACF (hybrid\_cacf). In addition, we consider a set of deep learning–based recommenders, which represent the latest advances in recommendation studies. We incorporate sequence-based models, such as SLi-Rec (Yu et al. 2019), Caser (Tang and Wang 2018), Gru4Rec (Hidasi et al. 2016), A2SVD (Yu et al. 2019), and NextItnet (Yuan et al. 2019), which consider users’ evolving preferences and are relevant to our context. In addition, we consider two content-based deep recommenders: NPA (Wu et al. 2019) and LSTUR (An et al. 2019), among which the latter considers users’ diverse interests on items. We also consider FAST (Howard and Gugger 2020), which is a classic deep recommender to capture latent user embeddings based on their item-selection histories. Finally, we compare our model to UCB and ε-greedy, which are two alternative bandit algorithms. We provide the details of these benchmark models in Online Appendix A7.

The models, if applicable, are trained from a separated training data set. As some batch-learning models cannot handle new users (e.g., CACF, PMF), we use the first four weeks for the test users as an additional warm-up period, and all the models in comparison are evaluated weekly by the overall recommendation performance within the same recommendation period (weeks 5–16). Batch learning–based models are retrained and updated afte each week, incorporating the new data collected in that period. Our proposed model does not have such a warm-up period and, instead, learns adaptively during the recommendation process. To control the extent of exploitation/exploration, we vary the value of the prior variances from 0.01, 0.1, and 1 to 10; our parameter tuning results suggest that the optimal value for the prior variances is 0.1. The parameter settings for the deep learning models are reported as follows. For SLi-Rec, the batch size is 100, the learning rate is 0.001, and the number of epochs is 20. For Caser, GRU4Rec, A2SVD, and NextItNet, the batch size is 200, the learning rate is 0.001, and the number of epochs is 20. For LSTUR and NPA, the batch size is 32, the learning rate is 0.0001, the number of epochs is 10, and the dropout rate is 0.2. The FAST model uses n\_factors of 40 and weight decay of 0.1.

We apply the Adam optimizer for both our user and the item-embedding models. The decay parameters are set as $\beta _ { 1 } = 0 . 9$ and $\beta _ { 2 } = 0 . 9 9 9$ . For the itemembedding model, we set the learning rate to 0.001. The batch size is set to 16, and the number of epochs is 10. Training the user-embedding model is nontrivial as the complexities and the scales of gradients are different in different components of the neural network. In our training process, the batch size is set to 64. We first train the auxiliary task of health outcome prediction for 20 epochs with learning rates 0.001 for eLSTM and 0.003 for the fully connected layers. After that, we change the learning rate for eLSTM to 0.0002 and the learning rate for the fully connected layers of the auxiliary task to 0.001. The learning rate for the wide branch and the fully con nected layer of the user embedding is set to 0.003. Then, the whole neural network is trained together for another 30 epochs.

We use precision, recall, nDCG, and MAP as the main evaluation metrics. Precision and recall are standard accuracy metrics for evaluating recommendation relevance (Cremonesi et al. 2010), whereas nDCG and MAP are rank-aware metrics that evaluate the relative preferences of recommendation items (Valcarce et al. 2018). For a more robust evaluation, we consider doubly robust (DR) estimation and omniscient simulation as two additional evaluation methods. DR is an off-line evaluation approach that accounts for potential bias in the collected data<sup>5</sup> (Dud´ık et al. 2011). Omniscient simulation enables us to generate user feedback in a simulated environment. Specifically, we construct a logistic predictor for users’ binary challenge-selection decisions; that is, $r _ { t } ( i , k ) = ( 1 + \exp { ( - { \bf v } _ { i t k } { } ^ { T } { \bf \zeta } ) } ) ^ { - 1 }$ , where v is a concatenation of user embeddings, challenge embeddings, and their interactions. The weight vector <sup>z</sup> could be chosen arbitrarily; here, we use a perturbed version of the weight vector trained on a randomly constructed training set (Nguyen et al. 2017). The performance evaluation is conducted on a test set. We provide more details of the evaluation approaches in Online Appendix A8.

The evaluation results for top-10 recommendations are outlined in Table 4, and the results for top-5 recommendations are provided in Online Appendix A9. We run each model 30 times and use t-statistics to compare the sample means. A superscripted asterisk denotes that a benchmark model performs significantly worse than the proposed model. The evaluation results provide strong evidence for the effectiveness of our proposed recommendation framework. It is worth noting that the batch learning–based models in general do not perform well. This echoes the importance of dynamic online adaption to users’ evolving preference patterns during the recommendation process. Compared with the benchmark models, our proposed recommendation framework can better discover the uncaptured user preference patterns through the balance between exploitation and exploration.<sup>6</sup> In addition, our model outperforms alternative online-learning bandit algorithms, such as UCB and ε-greedy. This is consistent with the bandit literature that Thompson sampling usually yields better performance than UCB and ε-greedy (Chapelle and Li 2011).

Together, these results demonstrate the efficiency of our customized bandit framework, which synthesizes enhanced context representation and diversity promotion scheme to better adapt to users’ healthcare preferences.

## 5.2. Experiment 2: Ablation Analysis of Model Components

We conduct an ablation analysis to examine the effectiveness of each major design component. Specifically, we consider a set of baseline MABs in which one or more proposed design components are muted so that we can separate the effect of the component(s). To test the proposed diversification scheme, we consider an ordinary TS in which the diversity constraint is removed. To examine whether the proposed context representation is effective, we replace the constructed deep learning embeddings with regular context variables and compare the model performance.<sup>8</sup> To shed more light on the effectiveness of our unique deep learning network design, we consider alternative deep learning models, such as Collab\_Filter and Tabular provided by python Fastai library to construct user embeddings and BERT and FastText to construct intervention item embeddings.

We report the comparison results for top-10 recommendations in Table 5 and the results for top-5 recommendations in Online Appendix A9. Our results show that the baseline MABs generally have an inferior performance. Specifically, when the diversity promotion constraint is not incorporated, the performance drops by 6.48%. When user embeddings are not used, the performance drops by 2.94%. When challenge embeddings are not used, the performance drops by 12.16%. These results indicate that each of our proposed design components is effective. The performance gap is relatively large for the no challenge–embedding model. A possible reason is that the baseline MAB uses the annotated challenge meta attributes, which are mostly categorical and one-hot encoded; therefore, they may not provide much information for the learning process. In comparison, the learned embeddings are dense, high-dimensional feature vectors that capture continuous semantics to improve intervention characterization. When both embeddings and the diversity promotion constraint are removed, the performance reduces even more.

Table 4. Comparison with State-of-the-Art Benchmarks (Top-10 Recommendations)

<table><tr><td>Model</td><td>Precision@10</td><td>Recall@10</td><td>nDCG@10</td><td>MAP@10</td><td>DR@10</td><td>Simu@10</td></tr><tr><td>DLDE-MAB</td><td>0.5311</td><td>0.0654</td><td>0.7944</td><td>0.0366</td><td>0.5003</td><td>0.4458</td></tr><tr><td>FAST</td><td>0.4014***</td><td>0.0501***</td><td>0.6104***</td><td>0.0291***</td><td>0.3796***</td><td>0.3850***</td></tr><tr><td>SLi_Rec</td><td>0.3959***</td><td>0.0457***</td><td>0.2356***</td><td>0.0245***</td><td>0.3913***</td><td>0.3988***</td></tr><tr><td>Caser</td><td>0.4006***</td><td>0.0463***</td><td>0.2015***</td><td>0.0255***</td><td>0.4066***</td><td>0.4016***</td></tr><tr><td>GRU4Rec</td><td>0.3937***</td><td>0.0454***</td><td>0.2290***</td><td>0.0252***</td><td>0.4004***</td><td>0.3995***</td></tr><tr><td>A2SVD</td><td>0.3921***</td><td>0.0453***</td><td>0.1961***</td><td>0.0255***</td><td>0.3953***</td><td>0.3973***</td></tr><tr><td>NextItNet</td><td>0.3892***</td><td>0.0449***</td><td>0.2292***</td><td>0.0251***</td><td>0.4034***</td><td>0.3886***</td></tr><tr><td>LSTUR</td><td>0.5026***</td><td>0.0618***</td><td>0.2937***</td><td>0.0322***</td><td>0.4326***</td><td>0.4174***</td></tr><tr><td>NPA</td><td>0.4222***</td><td>0.0519***</td><td>0.1794***</td><td>0.0346***</td><td>0.4341***</td><td>0.4338**</td></tr><tr><td>CACF</td><td>0.3149***</td><td>0.0412***</td><td>0.5043***</td><td>0.0228***</td><td>0.4272***</td><td>0.4324**</td></tr><tr><td>SCF</td><td>0.3970***</td><td>0.0495***</td><td>0.7026***</td><td>0.0305***</td><td>0.3977***</td><td>0.4024***</td></tr><tr><td>PMF</td><td>0.2147***</td><td>0.0269***</td><td>0.5183***</td><td>0.0120***</td><td>0.3637***</td><td>0.4010***</td></tr><tr><td>CAMF</td><td>0.2653***</td><td>0.0342***</td><td>0.6718***</td><td>0.0210***</td><td>0.3365***</td><td>0.3670***</td></tr><tr><td>CB</td><td>0.2661***</td><td>0.0340***</td><td>0.5431***</td><td>0.0151***</td><td>0.4022***</td><td>0.4346**</td></tr><tr><td>hybrid_pure</td><td>0.2492***</td><td>0.0319***</td><td>0.6683***</td><td>0.0162***</td><td>0.4073***</td><td>0.4403</td></tr><tr><td>hybrid_cacf</td><td>0.2895***</td><td>0.0375***</td><td>0.4813***</td><td>0.0187***</td><td>0.4150***</td><td>0.4388*</td></tr><tr><td>UCB</td><td>0.3582***</td><td>0.0434***</td><td>0.7270***</td><td>0.0268***</td><td>0.3966***</td><td>0.4237**</td></tr><tr><td>ε-greedy</td><td>0.4453***</td><td>0.0547***</td><td>0.7599 ***</td><td>0.0338***</td><td>0.4414***</td><td>0.4167***</td></tr></table>

Note. Asterisk in superscript denotes that a benchmark model performs significantly worse than the proposed model. $^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 \hat { 5 } ; ^ { * * * } p < 0 . 0 1$

Table 5. Ablation Analysis Results (Top-10 Recommendations)

<table><tr><td>Model</td><td>Precision@10</td><td>Recall@10</td><td>nDCG@10</td><td>MAP@10</td><td>DR@10</td><td>Simu@10</td></tr><tr><td>DLDE-MAB</td><td>0.5311</td><td>0.0654</td><td>0.7944</td><td>0.0366</td><td>0.5003</td><td>0.4458</td></tr><tr><td>No cons</td><td>0.4967***</td><td>0.0614***</td><td>0.7866***</td><td>0.0355*</td><td>0.4859*</td><td>0.4359</td></tr><tr><td>No user embs</td><td>0.5155*</td><td>0.0634**</td><td>0.7816***</td><td>0.0327***</td><td>0.4897</td><td>0.4223**</td></tr><tr><td>No chlng embs</td><td>0.4665***</td><td>0.0574***</td><td>0.7658***</td><td>0.0302***</td><td>0.4269***</td><td>0.3763***</td></tr><tr><td>No embs</td><td>0.3634***</td><td>0.0444***</td><td>0.6596***</td><td>0.0283***</td><td>0.4195***</td><td>0.3986***</td></tr><tr><td>No embs no cons</td><td>0.3564***</td><td>0.0436***</td><td>0.6099***</td><td>0.0267***</td><td>0.4180***</td><td>0.3736***</td></tr><tr><td>DLDE-Collab</td><td>0.4790***</td><td>0.0588***</td><td>0.7740***</td><td>0.0363</td><td>0.4845*</td><td>0.4306*</td></tr><tr><td>DLDE-Tabular</td><td>0.4665***</td><td>0.0574***</td><td>0.7573***</td><td>0.0358*</td><td>0.4541***</td><td>0.3967***</td></tr><tr><td>DLDE-BERT</td><td>0.4797***</td><td>0.0594***</td><td>0.7296***</td><td>0.0350**</td><td>0.4340***</td><td>0.4024***</td></tr><tr><td>DLDE-FastText</td><td>0.5077***</td><td>0.0626***</td><td>0.7333***</td><td>0.0361</td><td>0.4465***</td><td>0.3939***</td></tr></table>

Note. Asterisk in superscript denotes that a benchmark model performs significantly worse than the proposed model. $^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 \hat { 5 } ; ^ { * * * } p < 0 . 0 1$

Moreover, we observe that performance decreases when we replace our embeddings by alternative deep learning embeddings. The performances for Collab-Filter and Tabular are shown to be worse than that of the no user–embeddings model. The reason could be that Collab-Filter and Tabular embeddings introduce high dimensionality, whereas they fail to capture useful information regarding users’ health-management dynamics (an illustrative demonstration is provided in Online Appendix A9.3). Although Collab-Filter accounts for latent information in users’ challenge-selection behaviors, it does not explicitly model the synergies among users’ multiple health and health-behavior sequences. The Tabular model learns embeddings based on users tabular attributes, such as gender and age; however, the sequential behavior patterns are not captured. BERT and FastText are state-of-the-art word2vec deep learning models. They do not perform as well in our healthcare recommendation task because they do not incorporate specific designs to capture the key features of healthcare interventions.

## 5.3. Experiment 3: On Dynamics of Users Preferences

In this experiment, we focus on the users whose challenge preferences vary the most to examine how our recommendation framework performs in adapting to user preference dynamics. Specifically, we select 30 users whose challenge choices vary most significantly<sup>9</sup> from the test user set. We then rerun our recommendation algorithm and the benchmark models on these dynamic users. Our model still outperforms all benchmark models. We report the evaluation results in Online Appendix A9.4. In Figure 5, we plot the differences between the new recommendation results (on the dynamic users) and the original results on the full test user set to display the performance changes. The y-axis represents the percentage changes in recommendation precision for each model in consideration.

Figure 5. (Color online) Relative Change in Precision When Evaluated on Dynamic Users  
(a)  
![](/api/attachments/PBUN65Y8/fulltext/images/f669547d40d805f4411e6e794df8c63aa579dde3dc100457b9d5b1dc12ed30f3.jpg)  
Notes. (a) Top-5 Recommendations. (b) Top-10 Recommendations.

(b)  
![](/api/attachments/PBUN65Y8/fulltext/images/5218b532d76cd5280d5767a1e421bf4af0efe89dab52e221bf4d529d38c5d300.jpg)

The results show that our model performs better when evaluated on the dynamic user set. This suggests that the advantage of our recommendation framework is further strengthened. UCB performs slightly better for top-5 recommendations, but the performance declines for top-10 recommendations. ε-greedy has a performance increase when recommending top-10 options, but the performance declines when top-5 options are recommended. Finally, batch learning–based models generally decline in performance. This can be due to the “first learn, then earn” recommendation scheme adopted, which heavily relies on historical data without accommodating potential uncertainty in users’ preference patterns.

## 5.4. Experiment 4: Analysis of Recommendation Diversity

We evaluate the diversity distribution of our recommendations to examine whether the proposed artifact can effectively approximate the true diversity patterns in users’ challenge preferences. Specifically, we calculate the recommendation frequency for each challenge type to construct the diversity distribution. Then, we compare the distribution with the one calculated from the real challenge-selection data, which reveals the true diversity structures in users’ preferences. We quantify the similarity level between two diversity distributions by Jensen-Shannon divergence (JSD) (Fuglede and Topsoe 2004). In Table 6, we present the calculated JSD values for each recommendation model for top-10 recommendations, and we observe similar patterns for top-5 recommendations. Our model is shown to have the smallest JSD value, which indicates that the diversity distribution it generates is most similar to the one observed in the data. These results suggest that our diversity-enhanced recommendation framework can deliver intervention portfolios that most align with users’ inherent healthcare needs.

## 5.5. Experiment 5: User Improvement

From a macroperspective, we examine whether our recommendation framework benefits more users. We define user improvement as the percentage of users who receive more preferred items from a focal recommendation algorithm than from a baseline algorithm. We use PMF as our baseline algorithm. PMF is a model-based, batch-learning method. It captures hidden user representations based on past item interactions; however, context information, such as users’ attributes and sequence features, are not leveraged in the recommendation process. As such, PMF serves as a good comparison basis to demonstrate the importance of healthcare context representation and online learning. We present our results for top-10 recommendations in Figure 6. The results for top-5 recommendations are very similar. Our proposed recommendation approach has the highest user improvement rate (\~97%). ε-greedy and UCB also achieve a high user improvement (ε-greedy: \~93%, UCB: \~92%). Comparatively, the batch learning–based models achieve lower user improvement (\~20%–80%). These results show the value of our recommendation design in improving user welfare at the platform level. This finding is associated with practical significance as when users find more preferred items on the platform, they are more likely to continuously engage in online healthmanagement activities. The improvement in user population can benefit the platform ecosystem and long-term sustainability (Bateman et al. 2011).

Table 6. JSD Similarity

<table><tr><td>Model</td><td>JSD value</td><td>Model</td><td>JSD value</td><td>Model</td><td>JSD value</td></tr><tr><td>DLDE-MAB</td><td>0.0456</td><td>NextItNet</td><td>0.0589</td><td>CAMF</td><td>0.3519</td></tr><tr><td>FAST</td><td>0.1721</td><td>LSTUR</td><td>0.0493</td><td>CB</td><td>0.1656</td></tr><tr><td>SLi_Rec</td><td>0.0503</td><td>NPA</td><td>0.0823</td><td>hybrid_pure</td><td>0.2674</td></tr><tr><td>Caser</td><td>0.0662</td><td>CACF</td><td>0.0572</td><td>hybrid_cacf</td><td>0.1348</td></tr><tr><td>GRU4Rec</td><td>0.0610</td><td>SCF</td><td>0.1775</td><td>UCB</td><td>0.3253</td></tr><tr><td>A2SVD</td><td>0.0458</td><td>PMF</td><td>0.0470</td><td> $\varepsilon$ -greedy</td><td>0.0951</td></tr></table>

Figure 6. (Color online) User Improvement: Using PMF as Baseline  
![](/api/attachments/PBUN65Y8/fulltext/images/2f52e79de4a99ada3e1f7bc34a1a0f3e2098c9e5365157128a4211b0c65edaf9.jpg)

## 5.6. Experiment 6: Using Our Recommendation Framework to Improve Health Outcomes

Given that both user engagement and health outcomes can be important considerations, we conduct an exploratory analysis on the potential usage of recommendation systems for improving users’ health outcomes. Specifically, we aim to demonstrate the flexibility of our proposed framework such that, by providing a different reward signal without a change to the implementation or the model architecture, our online learning scheme can automatically learn with respect to the new target/ recommendation goal. We consider the scenario in which the decision makers care more about the effect of recommendations on users’ weight-loss outcomes rather than the number of challenge selections. The logistic reward predictor is the same as Equation (1) with the reward signal r (i, k) modified to users’ in-period weightloss rate, which is defined as the propensity of weight loss or weight unchanged within a period (i.e., weight $\leq w e i g h t _ { t - 1 } )$

Table 7. Weight Loss as Recommendation Goal

<table><tr><td>Model</td><td>Top-5</td><td>Top-10</td><td>Model</td><td>Top-5</td><td>Top-10</td></tr><tr><td>DLDE-MAB</td><td>0.7275</td><td>0.7361</td><td>CACF</td><td>0.6589***</td><td>0.6504***</td></tr><tr><td>FAST</td><td>0.6307***</td><td>0.6756***</td><td>SCF</td><td>0.6596***</td><td>0.6615***</td></tr><tr><td>SLi_Rec</td><td>0.4354***</td><td>0.4379***</td><td>PMF</td><td>0.6630***</td><td>0.6527***</td></tr><tr><td>Caser</td><td>0.4365***</td><td>0.4381***</td><td>CAMF</td><td>0.6661***</td><td>0.6643***</td></tr><tr><td>GRU4Rec</td><td>0.4456***</td><td>0.4472***</td><td>CB</td><td>0.6592***</td><td>0.6533***</td></tr><tr><td>A2SVD</td><td>0.4362***</td><td>0.4383***</td><td>hybrid_pure</td><td>0.6460***</td><td>0.6511***</td></tr><tr><td>NextItNet</td><td>0.4359***</td><td>0.4375***</td><td>hybrid_cacf</td><td>0.6622***</td><td>0.6619***</td></tr><tr><td>LSTUR</td><td>0.5899***</td><td>0.5774***</td><td>UCB</td><td>0.6339***</td><td>0.6082***</td></tr><tr><td>NPA</td><td>0.5935***</td><td>0.5864***</td><td>ε-greedy</td><td>0.6268***</td><td>0.6393***</td></tr></table>

Note. Asterisk in superscript denotes that a benchmark model performs significantly worse than the proposed model. $^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1$

In order to evaluate the performance of various recommendation models, we need to generate counterfactual weight-loss outcomes. To this end, in addition to the omniscient simulator we built in Section 5.1 that simulates users’ challenge-selection behaviors upon recommendations, we simulate users’ expected weight loss based on their selected challenges through a weight vector h<sub>∗</sub> of the logistic reward predictor. Both simulators are trained on a separated data set, and we follow the prior studies to perturb the trained weight vectors to approximate the noises contained in the user-feedback signaling procedure in real-world settings (Nguyen et al. 2017). We report our evaluation results in Table 7.

The result columns represent the average in-period weight-loss rate under top-5 and top-10 recommendations, respectively. Our model achieves higher average in-period weight-loss rates (72.75% for top-5 and 73.61% for top-10 recommendations) compared with the benchmark models. Particularly, the batch learning–based deep recommenders have the worst performance (\~40%–60%). This is because they heavily exploit information in users challenge-selection histories, whereas healthcare outcomes and other health-related information are not considered. In comparison, our proposed framework can effectively use weight loss as feedback to optimize health-related rewards. As our user-embedding model combines both weight trajectories and behavior paths in learning the user representations, it has a stronger learning capability to adapt to users’ weight-loss signals.

## 6. Discussion and Concluding Remarks

In this study, we develop a personalized recommendation system to help individuals participate in online healthcare interventions. Following the design science paradigm, we test the performance of our recommendation framework through a series of experiments. The evaluation results suggest that the proposed recommendation system is effective in adapting to users’ dynamic and diverse healthcare preferences and outperforms various state-of-the-art recommendation models.

Our study contributes to the emerging literature on the application of business intelligence (Chen et al. 2012, Abbasi et al. 2016). We demonstrate that prescriptive analytics can be integrated with IT artifacts to generate applicable insights. We enrich the healthcare recommendation literature by designing and evaluating a novel framework for automating personalized healthcare recommendations. Our proposed recommendation design makes several methodological contributions. First, we propose an effective multiarmed bandit approach that is enhanced by theory-guided diversification and deep context representation, which provides a unified framework for addressing challenges regarding healthcare recommendation personalization, adaptation, and diversity promotion. Second, our proposed deep learning networks encompass several methodological novelties. In designing the user-embedding model, we account for users’ multiple behavior seq uences that correlate to their healthcare preferences, including their personal health contexts and external impacts of online social interactions. We propose an enhanced LSTM to jointly process these sequence features to capture potential correlations among the time series and use an auxiliary loss function to incorporate the impact of health outcomes on users’ intervention preferences. These innovations contribute to the extant design science literature by providing insights into user healthcare representation and showing viable approaches to multisequence management (Morid et al. 2022).

From a practical perspective, our recommendation framework addresses real-world challenges in online healthcare interventions and can be used to benefit multiple stakeholders. Our recommendation framework helps users better engage in healthcare interventions and improve their compliance in behavior regulation. We provide an actionable solution to improve the user engagement experience and contribute to healthcare platform sustainability. Finally, for policymakers, we demonstrate a way to improve healthcare personalization by integrating IT artifacts with healthcare delivery. Online healthcare recommendation systems can account for user heterogeneity by automatically tracking and leveraging personal health (and behavior) data. Policymakers may consider integrating recommendation systems into major online healthcare-delivery portals to help individuals obtain personalized information.

## 6.1. Generalizability

Our evaluation setting is a representative context of personal health management in which individuals make behavior changes to improve wellness (e.g., weight loss). In managing other chronic conditions, such as type-2 diabetes and cardiovascular conditions, individuals are often required to regulate similar health and behavior aspects (e.g., blood glucose/pressure, nutrition, exercise, etc.). Our proposed recommendation design is generic and can be applied to multiple health-management settings. The major design components, such as the deep representation learning and the diversification constraint, can be customized within our framework to capture context-related features. For example, our deep learning models can process different sets of health and behavior data without changing the model structure. The diversity promotion constraint can incorporate different dimensions for outcome and behavior management.

Potentially, our proposed recommendation framework can be applied to broader healthcare problems. As noted, our context representation approach is inspired by common challenges faced by healthcare prediction problems (Morid et al. 2022). Therefore, the neural network design can be used to improve user modeling in other healthcare-delivery tasks. In addition, our study can be extended to recommendations in wearable devices or mobile health applications, in which service providers push notifications based on individuals’ specific health and behavior contexts. Service providers need to track users’ health and/or behavior histories (e.g., through fixed user account IDs) to characterize users’ health-management dynamics. In addition, our item-embedding model can be used to characterize other online healthcare items, such as nutrition therapies and medical documents, which usually take a similar text format. Finally, service providers may consider formulating recommendation constraints to incorporate domain expertise or data-driven insights to guide the learning of user behaviors. For example, if there are strong theory indications or empirical evidence for users’ preference dimensions, it is desirable to design a specific diversification scheme to guide the recommendations along the identified dimensions.

## 6.2. Limitations and Future Work

Our study utilizes individuals’ online data to form recommendation strategies given that off-line data may not always be available for service providers. Future studies may incorporate users’ off-line information if data permits. For instance, it is possible to obtain individuals’ daily behavior trajectories and health signals through wearable devices. In addition, researchers can obtain more accurate health data to improve recommendations with the use of personal health records from hospitals/clinics. Our research also opens an opportunity for investigating alternative online machine learning approaches (with a more detailed discussion provided in Online Appendix A1.3). In a healthcare setting, future contexts (patients’ healthcare status and/or future preferences) may be affected by the chosen interventions. One limitation of the bandit model adopted in this work is that it ignores this dependency and assumes independent and identically distributed contexts. A more complete model of our problem falls into the umbrella of reinforcement learning (RL), which is a strict generalization of contextual bandits. RL models a setting in which the agents’ actions can influence the future states and exert a significant long-term effect. We discuss several challenges in applying full RL in healthcare contexts. First, healthcare recommendation contexts typically contain many exogenous behavior variables/processes (e.g., users’ self-monitoring and support seeking). It can be challenging to define a state variable in this setting such that it entails all the necessary information for describ ing users’ decision making. In addition, the dynamic evolution of the healthcare-related contexts over time are usually not yet well-understood. Using modelbased RL may need strong theory support for defining state transitions.

Second, in a healthcare setting in which the effectiveness of each intervention largely depends on users’ characteristics and past behavior sequences, the state space is expected to be large and/or continuous. Hence, learning a full RL can be extremely data-hungry, which can be difficult to implement in a healthcare context. Recent advancements on both the Atari platform (Mnih et al. 2015) and Go (Silver et al. 2016) leverage advances in deep learning for powerful function approximation and yet require strong domain knowledge and large amounts of data to be successful. Bandit algorithms, on the other hand, enjoy a relatively fast learning rate, which is critical because of the high abandonment rate of online healthcare platforms (McLean 2011) and can offer a reasonable approximation (Lei et al. 2017, Tewari and Murphy 2017). We leave the design of a full RL framework to future work.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their insightful com ments and constructive suggestions throughout the review process.

## Endnotes

<sup>1</sup> It is challenging to define a state variable to apply full RL in the focal context as health management usually involves lots of unobserved factors that affect decision making (Houlihan 2018). We provide more discussions about why bandit is desirable in our research setting in Section 6.2 and Online Section A1.

<sup>2</sup> The optimization problem is an integer linear program with binary decision variables, which can be solved through the continuous relaxation of the model. The exact solution can be found using methods such as branch and bound.

<sup>3</sup> As we aim to use the user-embedding model to improve the downstream recommendation task, the output of the deep model is the embeddings of the adopted healthcare interventions. We introduce the item embedding construction in the next section.

<sup>4</sup> Age groups are encoded as follows: group 0: ≤29, group 1: 30–39, group 2: 40–49, group 3: 50–59, group 4: 60–69, group 5: >69.

<sup>5</sup> As the data are precollected, we can observe only the rewards for the chosen action in the data. As such, rewards for certain actions can be estimated less accurately if the action is not frequently chosen in the historical data.

<sup>6</sup> We further illustrate the importance of online learning through a side experiment in Online Appendix A9.1 in which we compare our learning algorithm with pure exploitation and pure exploration.

<sup>7</sup> We also conduct a robustness check on our evaluation data set. The results confirm the superiority of our approach and are reported in Online Appendix A9.2.

<sup>8</sup> Regular context variables are the features that are not processed by deep learning, such as users’ static attributes, the nonsequence version of online behaviors (e.g., number of weigh-ins, friends, etc.), and the meta challenge attributes described in Section 4.2.

<sup>9</sup> Users’ choice variations can be quantified by the variance of selected challenges’ embeddings. As challenge embeddings are vectors, we define the variance of embeddings as the minimum value of the variances of the elements.

## References

Abbasi A, Sarker S, Chiang RH (2016) Big data research in information systems: Toward an inclusive research agenda. J. Assoc. Inform. Systems 17(2):3.

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6):734–749.

Adomavicius G, Tuzhilin A (2011) Context-aware recommender systems. Ricci F, Rokach L, Shapira B, Kantor PB, eds. Recom mender Systems Handbook (Springer, Berlin), 217–253.

An M, Wu F, Wu C, Zhang K, Liu Z, Xie X (2019) Neural news recommendation with long-and short-term user representations. Korhonen A, Traum D, Ma\`rquez L, eds. Proc. 57th Annual Meeting. Assoc. Comput. Linguistics (Association for Computational Linguistics, Florence), 336–345.

Auer P, Cesa-Bianchi N, Fischer P (2002) Finite-time analysis of the multiarmed bandit problem. Machine Learn. 47(2–3):235–256.

Baltrunas L, Ludwig B, Ricci F (2011) Matrix factorization techniques for context aware recommendation. Proc. Fifth ACM Conf. Recom mender Systems (ACM, New York), 301–304.

Bandura A (1991) Social cognitive theory of self-regulation. Organ. Behav. Human Decision Processes 50(2):248–287.

Bandura A (2004) Health promotion by social cognitive means. Health Ed. Behav. 31(2):143–164.

Barello S, Triberti S, Graffigna G, Libreri C, Serino S, Hibbard J, Riva G (2016) eHealth for patient engagement: A systematic review. Frontiers. Psych. 6:2013. https://psycnet.apa.org/record/ 2016-18429-001.

Bateman PJ, Gray PH, Butler BS (2011) Research note—The impac of community commitment on participation in online communities. Inform. Systems Res. 22(4):841–854.

California HealthCare Foundation (2017) Consumers in healthcare: The burden of choice. Accessed October 30, 2019, https://www. chcf.org/wp-content/uploads/2017/12/PDF-ConsumersIn HealthCareBurdenChoice.pdf.

Centers for Disease Control and Prevention (2019) About chronic diseases. Accessed October 23, 2019, https://www.cdc.gov/ chronicdisease/about/index.htm#:\~:text=Many%20chronic%20 diseases%20are%20caused,Lack%20of%20physical%20activity.

Chapelle O, Li L (2011) An empirical evaluation of Thompson sam pling. Adv. Neural Inform. Processing Systems 24:2249–2257.

Chen A (2005) Context-aware collaborative filtering system: Predicting the user’s preference in the ubiquitous computing environment. Internat. Sympo. Location Context Awareness (Springer), 244–253.

Chen H, Chiang RH, Storey VC (2012) Business intelligence and analytics: From big data to big impact. Management Inform. Sys tems Quart. 36(4):1165–1188.

Cheng H-T, Koc L, Harmsen J, Shaked T, Chandra T, Aradhye H, Anderson G, Corrado G, Chai W, Ispir M (2016) Wide & deep learning for recommender systems. Proc. First Workshop Deep Learn. Recommender Systems, 7–10.

Coelho JJ, Arnold A, Nayler J, Tischkowitz M, MacKay J (2005) An assessment of the efficacy of cancer genetic counselling using real-time videoconferencing technology (telemedicine) compared with face-to-face consultations. Eur. J. Cancer Care (England) 41(15):2257–2261.

Cremonesi P, Koren Y, Turrin R (2010) Performance of recommender algorithms on top-n recommendation tasks. Proc. Fourth ACM Conf. Recommender Systems, 39–46.

Cutler DM (2004) Behavioral health interventions: What works and why. Critical Perspectives on Racial and Ethnic Differences in Health in Late Life, 643–674.

DiMatteo MR (2004) Social support and patient adherence to medi cal treatment: A meta-analysis. Health Psych. 23(2):207–218.

Doran GT (1981) There’s a SMART way to write management’s goals and objectives. Management Rev. 70(11):35–36.

Dud´ık M, Langford J, Li L (2011) Doubly robust policy evaluation and learning. Preprint, submitted March 23, https://arxiv.org/ abs/1103.4601.

Eysenbach G (2005) The law of attrition. J. Medical Internet Res. 7(1)

Fuglede B, Topsoe F (2004) Jensen-Shannon divergence and Hilbert space embedding. Proc. Internat. Sympos. Inform. Theory (IEEE), 31.

Gittins JC (1979) Bandit processes and dynamic allocation indices. J. Roy. Statist. Soc. B 41(2):148–164.

Hibbard JH, Mahoney ER, Stock R, Tusler M (2007) Do increases in patient activation result in improved self-management beha viors? Health Services Res. 42(4):1443–1463.

Hidasi B, Karatzoglou A, Baltrunas L, Tikk D (2016) Session-Based Recommendations with Recurrent Neural Networks (ICLR, San Juan, Puerto Rico).

Houlihan S (2018) Dual-process models of health-related behaviour and cognition: A review of theory. Public Health 156:52–59.

Howard J, Gugger S (2020) Fastai: A layered API for deep learning. Inform. (Basel) 11(2):108.

Jiang N, Krishnamurthy A, Agarwal A, Langford J, Schapire RE (2017) Contextual decision processes with low Bellman rank are PAC-learnable. Internat. Conf. Machine Learn. (PMLR), 1704–1713.

Johnson F, Wardle J (2011) The association between weight loss and engagement with a web-based food and exercise diary in a commercial weight loss programme: A retrospective analysis. Internat. J. Behav. Nutrition Physical Activity 8(1):83

Johnson PE, Veazie PJ, Kochevar L, O’Connor PJ, Potthoff SJ, Verma D, Dutta P (2002) Understanding variation in chronic disease outcomes. Health Care Management Sci. 5(3):175–189.

King G, Willoughby C, Specht JA, Brown E (2006) Social support processes and the adaptation of individuals with chronic disabilities. Qualitative Health Res. 16(7):902–925.

Kovacs G, Wu Z, Bernstein MS (2018) Rotating online behavior change interventions increases effectiveness but also increases attrition. Proc. ACM Human Comput. Interaction (CSCW), 1–25.

Krukowski RA, Harvey-Berino J, Ashikaga T, Thomas CS, Micco N (2008) Internet-based weight control: The relationship between web features and weight loss. Telemedicine J. E-Health 14(8): 775–782.

Lei H, Tewari A, Murphy SA (2017) An actor-critic contextual bandit algorithm for personalized mobile health interventions. Preprint, submitted June 28, https://arxiv.org/abs/1706.09090.

Locke EA, Latham GP (1990) A Theory of Goal Setting & Task Perfor mance (Prentice-Hall, Inc., Hoboken, NJ).

Lorig K, Ritter PL, Laurent DD, Plant K, Green M, Jernigan VBB, Case S (2010) Online diabetes self-management program: A randomized study. Diabetes Care 33(6):1275–1281.

Lupton D (2013) The digitally engaged patient: Self-monitoring and self-care in the digital health era. Soc. Theory Health 11(3): 256–270.

McLean V (2011) Motivating patients to use smartphone health apps. PR Web 113. Accessed November 24, 2019, http://www. prweb.com/releases/2011/04/prweb5268884.htm.

Mnih A, Salakhutdinov RR (2008) Probabilistic matrix factorization. Adv. Neural Inform. Processing Systems 20:1257–1264.

Mnih V, Kavukcuoglu K, Silver D, Rusu AA, Veness J, Bellemare MG, Graves A, Riedmiller M, Fidjeland AK, Ostrovski G (2015) Human-level control through deep reinforcement learning. Nature 518(7540):529–533.

Morid MA, Sheng ORL, Dunbar J (2022) Time series prediction using deep learning methods in healthcare. ACM Trans. Management Inform. Systems, ePub ahead of print April 22, https:// doi.org/10.1145/3531326.

Nahum-Shani I, Smith SN, Spring BJ, Collins LM, Witkiewitz K, Tewari A, Murphy SA (2018) Just-in-time adaptive interventions (JITAIs) in mobile health: Key components and design principles for ongoing health behavior support. Ann. Behav. Medicine 52(6):446–462.

Nguyen K, Daume ´ H III, Boyd-Graber J (2017) Reinforcement learning for bandit neural machine translation with simulated human feedback. Preprint, submitted July 24, https://arxiv. org/abs/1707.07402.

Ogbeiwi O (2018) General concepts of goals and goal-setting in health care: A narrative review. J. Management Organ. 27(2):324–341.

Oulasvirta A, Hukkinen JP, Schwartz B (2009) When more is less: The paradox of choice in search engine use. Proc. 32nd Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval, 516–523.

Paredes P, Gilad-Bachrach R, Czerwinski M, Roseway A, Rowan K, Hernandez J (2014) PopTherapy: Coping with stress through pop-culture. Proc. Eighth Internat. Conf. Pervasive Comput. Tech. Healthcare, 109–117.

Rabbi M, Pfammatter A, Zhang M, Spring B, Choudhury T (2015) Automated personalized feedback for physical activity and dietary behavior change with mobile phones: A randomized con trolled trial on adults. JMIR Mhealth Uhealth 3(2):e4160.

Sedhain S, Sanner S, Braziunas D, Xie L, Christensen J (2014) Social collaborative filtering for cold-start recommendations. Proc. Eighth ACM Conf. Recommender Systems, 345–348.

Short SE, Mollborn S (2015) Social determinants and health behaviors: Conceptual frames and empirical advances. Current Opin ion Psych. 5:78–84.

Silver D, Huang A, Maddison CJ, Guez A, Sifre L, Van Den Driessche G, Schrittwieser J, Antonoglou I, Panneershelvam V,

Lanctot M (2016) Mastering the game of Go with deep neural networks and tree search. Nature 529(7587):484–489.

Sutton RS, Barto AG (2018) Reinforcement Learning: An Introduction (MIT Press, Cambridge, MA).

Tang J, Wang K (2018) Personalized top-n sequential recommendation via convolutional sequence embedding. Proc. 11th ACM Internat. Conf. Web Search Data Mining, 565–573.

Tate DF, Finkelstein EA, Khavjou O, Gustafson A (2009) Cost effec tiveness of internet interventions: Review and recommendations. Ann. Behav. Medicine 38(1):40–45.

Tewari A, Murphy SA (2017) From ads to interventions: Contextual bandits in mobile health. Mobile Health (Springer), 495–517.

Tomkins S, Liao P, Klasnja P, Murphy S (2021) IntelligentPooling: Practical Thompson sampling for mHealth. Machine Learn. 110:2685–2727.

Valcarce D, Bellog´ın A, Parapar J, Castells P (2018) On the robustness and discriminative power of information retrieval metrics for top-N recommendation. Proc. 12th ACM Conf. Recommender Systems (ACM, New York), 260–268.

van der Maaten L, Hinton G (2008) Visualizing data using t-SNE. J. Machine Learn. Res. 9:2579–2605

West R, Raw M, McNeill A, Stead L, Aveyard P, Bitton J, Stapleton J, McRobbie H, Pokhrel S, Lester-George A (2015) Health-care interventions to promote and assist tobacco cessation: A review of efficacy, effectiveness and affordability for use in national guideline development. Addiction 110(9):1388–1403.

White A, Kavanagh D, Stallman H, Klein B, Kay-Lambkin F, Proudfoot J, Drennan J, Connor J, Baker A, Hines E (2010) Online alcohol interventions: A systematic review. J. Medical Internet Res. 12(5):e1479.

Wu C, Wu F, An M, Huang J, Huang Y, Xie X (2019) NPA: Neural news recommendation with personalized attention. Proc. 25th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining, 2576–2584.

Yan L (2018) Good intentions, bad outcomes: The effects of mismatches between social support and health outcomes in an online weight loss community. Production Oper. Management 27(1):9–27.

Yan L, Tan Y (2014) Feeling blue? Go online: An empirical study of social support among patients. Inform. Systems Res. 25(4): 690–709.

Ybarra ML, Eaton WW (2005) Internet-based mental health interventions. Mental Health Services Res. 7(2):75–87

Yu Z, Lian J, Mahmoody A, Liu G, Xie X (2019) Adaptive user modeling with long and short-term preferences for personalized recommendation. Proc. 28th Internat. Joint Conf. Artificial Intelligence, 4213–4219.

Yuan F, Karatzoglou A, Arapakis I, Jose JM, He X (2019) A simple convolutional generative network for next item recommendation. Proc. 12th ACM Internat. Conf. Web Search Data Mining, 582–590.

Zaman N, Li J (2014) Semantics-enhanced recommendation system for social healthcare. 2014 IEEE 28th Internat. Conf. Adv. Inform. Networking Appl. (IEEE, Piscataway, NJ), 765–770.

Zhang S, Yao L, Sun A, Tay Y (2019) Deep learning based recommender system: A survey and new perspectives. ACM Comput Surveys 52(1):1–38

Zhao X, Xia L, Tang J, Yin D (2019) Deep reinforcement learning for search, recommendation, and online advertising: A survey ACM Sigweb Newsletter, 1–15.

Zhou T, Yan L, Wang Y, Tan Y (2021) Turn your online weight management from zero to hero: A multidimensional, continuous-time evaluation. Management Sci. 68(5):3507–3527.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
