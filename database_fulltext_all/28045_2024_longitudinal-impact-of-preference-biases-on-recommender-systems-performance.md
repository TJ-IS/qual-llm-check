---
otero_id: 28045
otero_key: "72KZPB3W"
title: "Longitudinal Impact of Preference Biases on Recommender Systems’ Performance"
authors: "Meizi Zhou; Jingjing Zhang; Gediminas Adomavicius"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0133"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Longitudinal Impact of Preference Biases on Recommender Systems’ Performance

Meizi Zhou,<sup>a,</sup>\* Jingjing Zhang,<sup>b</sup> Gediminas Adomavicius<sup>c</sup>

<sup>a</sup> Boston University, Boston, Massachusetts 02215; <sup>b</sup> Indiana University, Bloomington, Indiana 47405; <sup>c</sup> University of Minnesota, Minneapolis, Minnesota 55455

\*Corresponding author

Contact: mzzhou@bu.edu, https://orcid.org/0000-0002-2654-7333 (MZ); jjzhang@indiana.edu, https://orcid.org/0000-0002-6805-8685 (JZ); gedas@umn.edu, https://orcid.org/0000-0001-5251-5098 (GA)

Received: March 7, 2021 Revised: May 30, 2022; March 13, 2023; September 22, 2023; September 30, 2023 Accepted: October 11, 2023 Published Online in Articles in Advance: November 21, 2023

https://doi.org/10.1287/isre.2021.0133

Copyright: © 2023 INFORMS

Abstract. Research studies have shown that recommender systems’ predictions that are observed by users can cause biases in users’ postconsumption preference ratings. This can happen as part of the standard, normal system use, where biases are typically caused by the system’s inherent prediction errors (i.e., because of the less-than-perfect accuracy of recommendation methods). Because users’ preference ratings are typically fed back to the system as training data for future predictions, this process is likely to influence the performance of the system in the long run. We use a simulation approach to study the longitudi nal impact of preference biases (and their magnitude) on the dynamics of recommender systems’ performance. Our simulation results show that preference biases significantly impair the system’s prediction performance (i.e., prediction accuracy) as well as users’ consumption outcomes (i.e., consumption relevance and diversity) over time. The impact is nonlinear to the size of the bias, that is, large bias causes disproportionately large negative effects. Also, items that are less popular and less distinctive (in terms of their content) are affected more by preference biases. Furthermore, given the impact of preference bias on the recommender systems’ performance, we explore the problem of debiasing usersubmitted ratings. We empirically demonstrate that relying solely on historical rating data is unlikely to be effective in debiasing. We also propose and evaluate two debiasing approaches that take into account additional relevant information that can be collected by recommendation platforms. Our findings provide important implications for the design of recommender systems.

History: Olivia Liu Sheng, Senior Editor; Huimin Zhao, Associate Editor. Supplemental Material: The e-companion is available at https://doi.org/10.1287/isre.2021.0133.

Keywords: recommender systems • longitudinal dynamics • preference biases • system performance • debiasing • agent-based simulatio

## 1. Introduction

Recommender systems (RS) are ubiquitous online and are highly valuable for providers (e-commerce retailers, streaming platforms, etc.) and consumers. Such systems not only help users discover items that match their interests and needs, but they also help boost sales and retain users for service providers. For example, recommendations are estimated to drive about 35% of revenue for Amazon (Marshall 2006), more than 80% of what people watch on Netflix (Gomez-Uribe and Hunt 2015), about 60% of homepage video clicks on YouTube (Davidson et al. 2010), and the increase of monthly users from 75 to 100 million on Spotify (Leonard 2016). The interactions between users and RS form a feedback loop, consisting of preconsumption and postconsumption phases. Preconsumption, the system provides recommendations to users to help them find relevant items. After item consumption, users provide feedback to the system. One common way to provide user feedback for items is via explicit numeric ratings. For example, Amazon users are asked to rate the items they have purchased on a five-star scale (with one being “I hate it” and five being “I love it”). The system then uses this feedback to adjust and improve the subsequent recommendations.

There is a rich and diverse landscape of literature related to different “biases” that stem from the interactions between users and the RS, pertaining to both preconsumption and postconsumption phases. With respect to the preconsumption activities, research has reported that systems’ recommendations significantly affect users’ consumption choices, reflecting several well-known biases, such as position bias, presentation bias, and ranking bias (see a review by Baeza-Yates 2018). This is not unexpected, as recommendations are explicitly designed to provide value at the preconsump tion stage (e.g., to help users find relevant content). However, the recommendations are not presumed to continue providing value or impact after the consumption choice is made and a user has experienced the item, that is, at the postconsumption phase. Yet, researchers have consistently observed biases in users’ feedback ratings; more specifically, it has been consistently observed that users’ self-reported postconsumption ratings are biased toward the recommendations displayed to them (Cosley et al. 2003; Adomavicius et al. 2013, 2018). Such preference biases are observed across a variety of domains, recommendation types, and presentation forms.

Existing research has studied preference biases in static settings, for example, evaluating bias using a one-time snapshot of data. A real-world RS, however, is dynamic and iterative, and thus could potentially facilitate and even amplify long-lasting biasing effects. For example, after users submit biased preference ratings on newly consumed items to the system, these “polluted” ratings will be incorporated by the recommendation engine as additional training data to update the model and calculate subsequent recommendations. These recommendations will induce further biases in users’ consumption choices and feedback ratings. In other words, because of the iterative nature of the userrecommender interactions, the biased feedback ratings provided by users could accumulate in the system over time, causing a long-lasting negative impact on the system’s recommendations and users’ consumption outcomes. This potential longitudinal dynamic leads to many unexplored questions. For example, how does the preference bias change the system performance and users’ consumption over time? How does bias accumulate in the system over time? What items are likely to be influenced the most? How does it longitudinally affect users with different levels of susceptibility to bias? How can the longitudinal impacts of preference bias be reduced or eliminated?

This paper explores the longitudinal impact of preference biases using an agent-based simulation framework introduced in prior research (Zhang et al. 2020). Our study makes several important research contributions. In particular, we contribute to the literature by addressing the underexplored area of postconsumption-related biases, known as “preference biases,” from a longitudinal perspective. Prior research has mainly focused on various preconsumption-related biases (i.e., selection biases) and their remedies; in contrast, we shed light on how the postconsumption-related biases (i.e., preference biases) in users’ feedback snowball over time and detrimentally impact recommendation accuracy, relevance, and diversity. Our findings reveal interesting and important patterns regarding the impact of bias: for example, high bias leads to a disproportionately larger impact on recommendation performance and consumption outcomes. Additionally, our analysis of the consumption process highlights how and why bias accumulates more on those items that are less popular and have significant content similarity to other items. Furthermore, we examine heterogeneous user populations with varying degrees of preference bias, illustrating how different groups of users influence each other’s recommendation performance asymmetrically. Our study also provides important practical implications for the design of RS, particularly regarding the critical issue of debiasing self-reported user ratings. We explore the problem of debiasing and empirically demonstrate that solely relying on standard historical rating data is unlikely to effectively eliminate preference bias. To address this, we propose and explore two debiasing methods tailored to mitigate postconsumption preference biases induced by the system’s recommendations. These ap proaches are advantageous in reducing the longitudinal impact of bias and, at the same time, emphasize the need for additional knowledge about the user popula tion (i.e., going beyond the historical rating data).

## 2. Related Work

Our work is closely related to two research areas within the RS literature: (1) the longitudinal dynamics and (2) the preference biases in RS.

## 2.1. Longitudinal Dynamics of RS

RS use user feedback on consumed items as inputs for their personalization techniques, which estimate individual preferences for other items, that is, items that have not yet been consumed. These estimated preferences allow the system to find items that match indi vidual interests and tastes. Highly relevant items are then presented to users in the form of the system’s recommendations to help the users make consumption choices. Then, users’ feedback ratings for the newly consumed items serve as additional inputs to the RS to adjust and improve the model, completing a “feedback loop.” Through iterative user-recommender interactions, the RS can significantly influence product sales and users’ consumption behaviors. In turn, users consumption and feedback patterns also affect the system’s performance. A growing body of literature examines the longitudinal impacts of RS from various perspectives.

From the system perspective, over time, the interactions between users and the RS significantly influence the system’s performance, including recommendation accuracy, diversity, relevance, etc. For example, Zhang et al. (2020) show that users’ reliance on the system’s recommendations to make item choices consistently leads to a longitudinal “performance paradox” of RS. In particular, users’ reliance on RS, although helping users discover relevant items, tends to make the system less useful in the long run, as it negatively impacts the diversity of the recommended and consumed items as well as impairs the system’s ability to improve predictive accuracy. Paradoxically, in the long run, the system’s accuracy and diversity would comparatively improve more if users were to ignore recommendations and randomly choose items to consume.

To optimize the long-term performance of an RS, for example, defined by its predictive accuracy, some prior studies have incorporated reinforcement learning into the traditional recommendation framework to model the long-term effects of an action (i.e., a system recommendation), which are often formulated as the expected sum of rewards/costs. For example, Zeng et al. (2016) incorporate the time-varying contextual information to maximize the cumulative value of recommendations, and Theocharous et al. (2015) propose a framework that takes into account all the available knowledge about the user to select an offer that maximizes the user’s lifetime value in ad recommendations. Besides the accuracy, prior research has also examined the influence of user-recommender interactions on other recommendation performance metrics, such as diversity and relevance. Fleder and Hosanagar (2009) show that, over time, recommendations can lead to a concentrated consumption of a small set of popular items, that is, a “rich-get-richer, poor-getpoorer” effect for product sales. Lee and Hosanagar (2019) demonstrate that traditional collaborative filtering is associated with a decrease in sales diversity relative to a system without product recommendations. In session-based recommendation settings, relatively simple reranking strategies to introduce exploration may improve long-term recommendation diversity (Ferraro et al. 2020). Following this general research stream, we are also interested in the longitudinal dynamics of RS performance and its various aspects, including accuracy, relevance, and diversity. However, in this study we focus specifically on how the preference biases in users’ feedback ratings affect the system’s long-term performance.

From the user perspective, prior research shows that online recommendations can significantly influence users’ consumption choices and product sales (Senecal and Nantel 2004, De et al. 2010). The system’s recommendations can also bias users’ preference ratings and economic behaviors (Adomavicius et al. 2013, 2018). Recent work has examined the algorithmic confounding in RS due to the feedback loop; that is, recommendations are generated based on data from users already exposed to algorithmic recommendations (Chaney et al. 2018). Such algorithmic confounding amplifies the homogenization of user behavior at both the population and individual levels, decreases the utility that users gain from recommendations by urging them to make suboptimal choices, and amplifies the impact of RS on the distribution of item consumption.

## 2.2. Biases Caused by Recommendations

Prior research has studied various types of “biases” that stem from both preconsumption and postconsumption interactions between users and RS. Accord ingly, many recommendation biases can be broadly categorized as either selection biases or preference biases. Selection biases are heavily related to users’ preconsumption activities; that is, they reflect that users’ item choices are significantly affected by RS. Some examples of selection biases include popularity bias, which suggests users are more likely to be recommended, to consume, and thus to provide feedback on popular items than on unpopular items (e.g., Steck 2011, Prawesh and Padmanabhan 2014, Abdollahpouri et al. 2017); position bias, which describes a tendency of people to notice or interact with items in certain positions of lists with higher probability, regardless of the items’ actual relevance (e.g., Hofmann et al. 2014, Collins et al. 2018); and exposure bias, which occurs when users are only exposed to certain subsets of items and underexposed to other items (e.g., Chen et al. 2020). These selection biases can lead to “filter bubbles,” “echo chambers,” or outcomes that are biased with respect to some desired “fairness” criteria (e.g., Pariser 2011, Flaxman et al. 2016, Ekstrand et al. 2019, Abdollahpouri et al. 2020, Ge et al. 2020).

Preference biases, on the other hand, are related to users’ postconsumption activities. Specifically, existing literature shows that recommendations displayed at the item selection time (i.e., preconsumption) can still lead to substantial distortions in users’ subsequent self-reported ratings, even after item consumption (Cosley et al. 2003; Adomavicius et al. 2013, 2018). Such preference biases have been consistently observed across a variety of domains (e.g., movies, music, TV shows, and jokes), recommendation types (e.g., personalized recommendations and nonpersonalized aggregate user ratings), and presentation forms (e.g., numeric star ratings, graphic displays, and binary displays) (Adomavicius et al. 2013, 2019). This is problematic, as the users’ self-reported, postconsumption ratings are routinely assumed to represent the “ground-truth” preference information, which is commonly used as training data for developing and testing recommendation techniques.

In other words, the two types of biases—selection biases and preference biases—are different in many ways. They occur at different times (i.e., preconsumption versus postconsumption), they differ in how they influence the users $( \mathrm { i . e . , }$ one affects the consumption choices and the other affects how users rate the items), and they also negatively influence recommendation outcomes via very different mechanisms (i.e., one affects which user-item pair is added to the rating data, leading to a skewed distribution of item consumptions, whereas the other determines/distorts the specific rating value that is added to the data, leading to inaccurate representation of the user’s true preferences).

As compared with selection biases, preference biases have been relatively underexplored in the research literature. In this study, we comprehensively explore the impact of preference biases on RS performance. Prior literature has studied preference bias only in static settings, i.e., evaluating bias using a one-time snapshot of data. Because the preference bias is caused by the errors of the displayed ratings (i.e., the difference between displayed ratings and users’ true preferences) and the errors can be either positive or negative, users biased feedback ratings could be either higher or lower than their true preferences. Because a large number of users’ biased ratings can be submitted to the RS over time, it is not immediately clear whether the effects of these biases would cancel out or accumulate. It is also unclear if the size of the bias in users’ ratings is large enough to have a noticeable impact on important recommendation and consumption outcomes. Thus, the main objective of the paper is to examine the longitudinal dynamics of preference biases and how they affect RS performance and users’ consumption outcomes. We examine when and how the impact of preference bias can accumulate in the system to influence the recommendations and consumptions, and we examine what types of items are more likely to be influenced by such bias as well as any possible interplay between user subpopulations with different bias levels.

Prior research has developed a number of approaches that attempt to remove various biases from human decision making. The “proactive” approaches develop strategies for preventing preference bias from happening, that is, ensuring that users submit unbiased ratings, either by modifying the person or by modifying the environment (Soll et al. 2015). The “modifying the person” approach attempts to mitigate the bias through educating the decision maker about biases (Larrick 2004) or using decision models to generate judgments for users (Casey et al. 2001). The “modifying the environment” approach changes the presentation of the information to decision makers (Adomavicius et al. 2019). In contrast, a more popular stream in the RS literature has been to develop “reactive” approaches, which design computational methods to remove bias from ratings after they have been submitted by the users. Multiple algorithmic methods have been proposed to reduce the existing bias in the numeric ratings (e.g., Sinha et al. 2016, Sun et al. 2019, Zhang et al. 2019, Abdollahpouri et al. 2020, Gao and Shah 2020). In this paper, we build on this research stream by demonstrating the key challenges of existing “general-purpose” debiasing approaches and then proposing and evaluating techniques specifically designed to mitigate preference biases.

In summary, prior studies have looked into the unintended consequences of both preconsumption and postconsumption interactions between users and the RS. Our work substantially extends the existing literature by studying the longitudinal dynamics and impact of the postconsumption preference bias on the system’s performance and users’ consumption behaviors.

## 3. Simulation Framework

We use the agent-based simulation methodology to analyze the longitudinal dynamics of preference biases. The simulation-based approach provides a rich environment for exploration, allowing for targeted manipu lations and controlling (and separating the effects of) different factors, such as the type of platform, user population, item population, recommendation algorithms, users’ susceptibility to bias, consumption frequency, etc. It also allows for analyzing intermediate results and process metrics to understand the underlying mechanics of the preference bias’s impact on RS performance. In other words, for this type of research question, the simulation-based approach can be advantageous in several ways, as compared with other methodologies. For instance, in real-world large-scale field experiments, it can be extremely difficult (if not impossible) to control for key factors, for example, to induce specific levels of preference bias, and the potential negative impact of certain levels of bias may result in a loss in revenue for companies. Or, compared with laboratory experiments, simulation can be conducted on large-scale user populations and have users interact with an RS for hundreds of iterations. And, unlike analytical modeling approaches, which may require direct mathematical assumptions about the outcomes of complex machine learning algorithms, simulation testbeds are highly configurable and can incorporate a multitude of recommendation algo rithms directly. Of course, the usefulness of simulationbased methods directly depends on their ability to rep resent real-world phenomena with a sufficient degree of fidelity. Thus, in this work, we focus on the direct, algorithmic effects of preference bias (which manifests itself directly via users’ self-reported postconsumption preference ratings) on the RS performance. Additional considerations (using even more sophisticated models of user behavior) could potentially be explored as part of future research, such as modeling the changes of users’ trust in the RS as well as users’ economic behav ior over time due to the effects of bias.

In this research, we adopt an agent-based simulation framework developed in prior literature (Zhang et al. 2020) and extend this framework to explore the effects of preference biases on the longitudinal dynamics of RS performance. We adjust the framework by enriching the modeling of users’ feedback behavior (i.e., to incorporate preference biases) and explore different settings to show the effects of preference biases on the system’s longitudinal dynamics.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 1. Overview of Simulation Procedure
Initialization (t = 0)
Step 0: System Initialization
Initialize UserTastes for all users based on real-world rating data.
Initialize ItemContent for all items based on real-world rating data.
Initialize available ratings  $R^{0}$ .
Calculate item predictions  $P^{0}$ .
Prepare the list of recommendations for each user u, that is,  $L_{u}^{0} = \text{GenerateRecs}(P_{u}^{0})$ .
Evaluate recommendation performance.
Main Simulation (perform Steps 1 and 2 at t = 1, 2, 3, ...)
Step 1: Main Interaction/Consumption/Feedback Process
Use all currently available rating data at current time t:  $R^{t-1}$ .
For each user u who is due for an item consumption at time t:
    User u selects an item i for consumption from recommendations  $L_{u}^{t-1}$  in accordance with UserConsStrat $_{u}$ .
    User u consumes an item i and submits her preference rating  $S_{ui}$ .
    Update known rating data to include the new rating, that is,  $R^{t} = R^{t-1} \cup S_{ui}$ .
    Update next consumption time for user u, that is, UserNextCons $_{u}$  = UserNextCons $_{u}$  + UserConsPeriod $_{u}$ .
Step 2: System Update
Recalculate item predictions  $P^{t} = \text{PredictRatings}(R^{t})$ .
Prepare the list of recommendations for each user u, that is,  $L_{u}^{t} = \text{GenerateRecs}(P_{u}^{t})$ .
Evaluate recommendation performance.
</div>

## 3.1. General Procedure

Our simulation follows the general procedure outlined in prior work (Zhang et al. 2020): in a given time period, some users choose to visit the platform; the RS provides personalized recommendations to these users; a given user can choose an item to consume and submit a feedback rating for it; the system incorporates all feedback ratings to update the model and recalculate recommendations for the next time period. Table 1 provides an overview of the simulation procedure. We use a discrete-time iterative simulation procedure to advance the system state from one time period to the next. The simulation includes three main components: item population, user population, and recommender engine. Table 2 summarizes the modeling notation related to these components.

3.1.1. System Initialization. We use latent features to model the item and user populations. The content of each item i is represented by a vector of K continuous latent features, that is, ItemConten $t _ { i } = ( q _ { 1 } , \dots , q _ { K } )$ . Similarly to item content, the preferences of each user u fo items are represented as a vector of continuous latent features in the same K-dimensional latent space, that is, $U s e r T a s t e _ { u } = ( p _ { 1 } , . . . , p _ { K } )$ . In our experiments, we keep a fixed set of items and users for the entire simulation period because we aim to isolate the impact of preference bias and avoid adding complexity from other aspects, such as the arrival rates of new users and new items.

Before the main simulation, the three components (i.e., item population, user population, and recommendation engine) are initialized according to some desired distributional characteristics (i.e., Step 0). We seed the simulation with a set of items and users, and some initial ratings $R ^ { 0 }$ representing user-item consumptions at time t � 0. To achieve realistic distributions of item content ItemContent and user preferences UserTaste across the entire item and user populations, we apply a matrix factorization model to extract the latent item features and user preferences from real-world ratings. Specifically, we use a basic Singular Value Decomposition (FunkSVD) approach (Funk 2006) to decompose the rating matrix into two low-rank submatrices where each user u and each item i are represented by a vector of latent features, that is, $U s e r T a s t e _ { u }$ and ItemContent<sub>i</sub>, respectively. FunkSVD iteratively adjusts the latent feature vectors to find the values that minimize the regularized squared difference between predicted and actual ratings, that is, values that best represent user tastes and item content. We use standard machine learning practices (e.g., grid search, crossvalidation) to decide the best parameters of the FunkSVD for initialization.

Table 2. Summary of Modeling Notations Used in This Study

<table><tr><td>Variables</td><td>Definition</td></tr><tr><td> $ItemContent_i$ </td><td>A latent vector of item  $i's modeled content features$ </td></tr><tr><td> $UserTastes_u$ </td><td>A latent vector that represents user  $u's modeled taste profile$ </td></tr><tr><td> $R^t$ </td><td>Known ratings in the system at time  $t$ </td></tr><tr><td> $r_{ui}$ </td><td>User  $u's actual (i.e., ground-truth) preference rating for item \( i$ </td></tr><tr><td>bias</td><td>The degree of preference bias (i.e., users&#x27; susceptibility to bias), ranging from 0 to 1</td></tr><tr><td> $P^t$ </td><td>System prediction for all users over the whole set of items at time  $t$ </td></tr><tr><td> $L_u^t$ </td><td>System recommendation list for user  $u$  at time  $t$ </td></tr><tr><td> $S_{ui}$ </td><td>User  $u's submitted rating for item \( i$  (i.e., feedback to the system)</td></tr><tr><td> $UserConsPeriod_u$ </td><td>Representation of length of time between user  $u's two consecutive consumptions$ </td></tr><tr><td> $UserNextCons_u$ </td><td>Next scheduled consumption for user  $u$ </td></tr><tr><td> $UserConsStrategy_u$ </td><td>User  $u's consumption strategy$ </td></tr><tr><td> $C_t$ </td><td>All user-item consumption pairs at time  $t$ </td></tr><tr><td> $Q_t$ </td><td>All unique items consumed at time  $t$ </td></tr></table>

These derived latent vectors are used to calculate users’ actual preference ratings (ground truth) for items. Prior literature suggests that real users exhibit idiosyncratic randomness when providing ratings, and users are often inconsistent in their ratings on the same items at different times (Amatriain et al. 2009). Thus, in our simulations, we follow prior literature to model users actual preference ratings with random noise; that is, we choose to simulate the final submitted preference ratings to be normally distributed around users’ true preferences with a standard deviation of 1.0 (on a rating scale of 1–5). Specifically, preference rating $r _ { u i }$ for a user u on item i is calculated as

$$
r _ {u i} = \text { ItemContent } _ {i} \cdot \text { UserTaste } _ {u} + \varepsilon_ {u i}, \quad \varepsilon_ {u i} \sim \mathcal {N} (0, 1).\tag{1}
$$

We then seed the system at time t � 0 with preexisting ratings $R ^ { 0 }$ computed based on Equation (1). The distribution of these initial ratings (i.e., which user-item pairs contain known ratings at $t = 0 )$ follows real-world ratings; that ${ \mathrm { i } } \mathbf { s } ,$ each user’s preexisting item consumption corresponds to the known user-item pairs in the original real-world data set that was used to initialize the simulation.

There are several key points to note about the initialization stage. In particular, we do not directly use the real-world ratings as ground truth in our simulation; instead, we use real-world ratings to simulate ground truth. It is because, among all possible user-item consumption combinations, only a small portion of the real-world ratings is typically known; however, in our simulations, we need to know the ground truth for every user-item combination, that is, to be able to simulate the actual rating feedback for any item that any user may choose to consume. Furthermore, these ground-truth ratings are not directly observed by recommendation algorithms; they are used for determining the user-submitted ratings to the system after each consumption. It is these user-submitted ratings that are then used by the recommendation algorithms as training data (as is the case in real-world RS). After the initialization, user-submitted ratings may be infused with different levels of preference bias depending on the specific simulation scenario. Given the same system initialization, the main focus of the study is to understand and quantify what happens to the system when newly incoming ratings are affected by preference bias in different ways.

3.1.2. User Consumption Choices. In each subsequent simulation period $t = 1 , 2 , 3 , \ldots$ , the system predicts each user’s preference ratings for unconsumed items using any recommendation technique or a combination of techniques. We model the system’s recommendations for each user u as a list of items $L _ { u } ^ { t }$ ranked based on system-predicted ratings $P _ { u } ^ { t }$ for that user. The items are displayed along with their predicted ratings to every user. Each user who consumes at time t chooses an item based on the system’s recommendation list, where the probability of an item being selected depends on its rank in the list (i.e., items ranked higher have a higher probability of being selected). Specifically, following prior literature (Zhang et al. 2020), we use an exponential decay function to model the diminishing consumption likelihood based on the item’s rank in a recommendation list. For an item ranked at the i-th position, its probability of consumption is

$$
p r o b _ {i} = (\alpha - 1) \cdot \alpha^ {- i}.\tag{2}
$$

The α value in Equation (2) can be viewed as the degree of the user’s reliance on the recommendation list for choosing items, that is, the user’s consumption strategy. In our main results throughout the paper, we set $\alpha = 2 ,$ which indicates that users heavily rely on the recommendation list to make consumption choices. In particular, the probability of consuming the first recommended item is 50%, the second item is 25%, the third item is 12.5%, and so forth; the probability of consuming one of the top-5 recommendations is around 97%. Based on various industry reports, our item-selection behavior settings for simulated users are consistent with real users on existing platforms (e.g., Davidson et al. 2010, Gomez-Uribe and Hunt 2015, Hale 2021, Dean 2022) and also reflect the focus of RS literature on top-N behavior and performance (Karypis 2001, Deshpande and Karypis 2004, Cremonesi et al. 2010, Ja¨rvelin and Keka¨la¨inen 2017).<sup>1</sup>

We use the consumption timespan (UserConsPeriod ) to model how frequently user u consumes items; it represents the average length of time between a user’s two consecutive consumptions. For example, a value of two means that, on average, this user consumes one item every two time periods. We calibrate the average timespan for each user based on the real-world data and normalize it to the set $\{ 1 , \ldots , 5 \}$ . In the experiment, user u’s first consumption period $( U s e r N e x t C o n s _ { u } ^ { 0 } )$ is randomly generated from the set $\{ 1 , \ldots , 5 \}$ . In subsequent rounds, the actual timespans between two consecutive consumptions for u are drawn from a normal distribution around u’s mean timespan.

3.1.3. User Postconsumption Feedback. After item consumption, the user provides a feedback rating for the newly consumed item (i.e., how relevant the item was to the user). One key component in our simulation is that we explicitly model the effect of preference bias in the users’ postconsumption ratings. In particular, the postconsumption rating that user u submits for item i $( S _ { u i } )$ depends on both the user’s true preference for the item $( r _ { u i } )$ and the level of preference bias (bias) induced by the displayed system rating $( P _ { u i } ^ { t } )$ . Thus, the submitted rating $S _ { u i }$ of user u for item i is

$$
S _ {u i} = r _ {u i} + (P _ {u i} ^ {t} - r _ {u i}) \cdot b i a s.\tag{3}
$$

The rate of bias can range from zero to one, where zero means a user submits her true preference rating without being affected by the system-displayed ratings, and one means the user submits what the system displays, that is, the user is fully swayed by the system’s rating. All newly submitted ratings are added to the system’s training data, that is, are used to update recommendation models for future periods. Prior research has shown that the biasing effects of system-displayed ratings on user-submitted ratings are continuous and linear (Adomavicius et al. 2013, p. 972, fig. 7); thus, we assume a linear functional form in Equation (3), that is, the user’s submitted rating is linearly shifted from the ground-truth rating toward the system-displayed rating in proportion to the bias degree.

3.1.4. Simulation Assumptions. Simulation is a simplified version of the real-world environment. There are many factors that affect real users’ consumption choices and rating behaviors, but it is not possible for an agentbased model to consider and quantify all these variables. Our simulation studies make several assumptions about the users and the environment: (1) each user consumes and rates an item at most once, that is, no repeated consumption; (2) there are no monetary factors involved when users select items; (3) items do not have inventory restrictions and can be simultaneously consumed by multiple users (e.g., as is the case with most digital goods); (4) the recommendations to all users are generated by the same system; (5) user preferences are “stable,” that is, they do not change over the short-term time window of our simulation; and, (6) we focus on understanding the impact of preference bias specifically in the context of canonical recommendation algorithms and, thus, do not consider other potential sources of information for user decision making in our simulations, such as nonpersonalized, aggregate (average) item ratings, social-network-based data, domainknowledge-based recommendations (e.g., of complementary items), etc.

## 3.2. Performance Evaluation

We measure the quality of recommendations along three traditionally important RS performance dimensions: prediction accuracy, consumption relevance, and consumption diversity.

First, prediction accuracy measures the prediction performance of the system, that is, how well a system can identify each user’s preferences for unconsumed items. We evaluate prediction accuracy using the root mean squared error (RMSE) metric. Throughout the simulation, as users continue to consume more items, the remaining unconsumed user-item pairs keep decreasing over time. To keep the evaluation set consistent across all time periods, we calculate accuracy based on the entire set of unknown ratings at time $t = 0 \ ( \mathrm { i . e . }$ , the evaluation set T includes all the unknown user-item pairs at the initialization stage). RMSE of the system’s predictions at time t is calculated by comparing the system’s predicted ratings at t $( \mathrm { i } . \mathrm { e } . , P ^ { t } )$ and users’ true preference ratings (i.e., R):

$$
R M S E _ {t} = \sqrt {\sum_ {(u , i) \in T} (P _ {u i} ^ {t} - r _ {u i}) ^ {2} / | T |}\tag{4}
$$

The second metric, consumption relevance, focuses on the consumption outcomes, that is, what the users end up consuming as a result of their interactions with the system. The relevance metric provides a user-centric view of the system’s performance that captures the quality of users’ actual consumption experiences and outcomes. The consumed item relevance at each time t is measured by the average true preference ratings of all items consumed by users at time $t \ ( \mathrm { i . e . , } \ C _ { t } )$ . Thus, high relevance values appropriately indicate the situations where the users end up consuming items that they truly like. Formally, the consumption relevance at time t is calculated as

$$
R e l e v a n c e _ {t} = \sum_ {(u, i) \in C _ {t}} r _ {u i} / | C _ {t} |.\tag{5}
$$

Additionally, consumption diversity is a measure of the system’s discovery performance, that is, the capability to discover a broad, diverse set of relevant items while providing users with personalized recommendations $( \mathrm { e . g . }$ , individualized suggestions tailored to match each user’s unique preferences). We measure consumption diversity at the aggregate level; that is, providing the same set of “good” items to a user population would represent a low level of discovery performance, thus also indicating a potentially low level of personalization.<sup>2</sup> We use the cumulative number of unique items consumed by all users at each time $t \left( \mathrm { i . e . , } Q _ { t } \right)$ to measure the aggregate diversity of item consumption:

Table 3. Summary of Experimental Application Settings

<table><tr><td>Data set</td><td>Description</td><td>Users</td><td>Items</td><td>Ratings</td><td>Density</td></tr><tr><td>Sample of Netflix</td><td>Movie ratings distributed by Netflix</td><td>3,000</td><td>3,000</td><td>344,021</td><td>3.82%</td></tr><tr><td>Sample of Yelp</td><td>Business ratings released by Yelp</td><td>4,000</td><td>2,000</td><td>62,476</td><td>0.78%</td></tr></table>

$$
D i v e r s i t y _ {t} = | Q _ {1} \cup Q _ {2} \cup \dots \cup Q _ {t} |, \quad Q _ {t} = \{i | (u, i) \in C _ {t} \}\tag{6}
$$

## 3.3. Application Settings

In our experiments, we simulated two different application settings by seeding our simulation testbed with publicly available data sets, which came from different application domains and had different data characteristics. The data sets include a subset of the Netflix 100M data set (Bennett and Lanning 2007), from which we randomly sampled $3 { , } 0 0 0$ movies and extracted a random sample of 3,000 users who rated at least one of these movies, and a subset of Yelp rating data, from which we randomly sampled 2,000 restaurants and extracted a random sample of 4,000 users.<sup>3</sup> All ratings are integer values between one and five, where one represents the least-liked items, and five represents the most-liked items. The data sets are summarized in Table 3. For each application setting, we generated user and item populations, and the known user-item consumptions represent the initial state $( \mathrm { i . e . , ~ } t = 0 )$ of our simulations. The user and item profiles were represented by 20 latent features in the Netflix simulation setting and by 150 features in the Yelp setting.

We compare the longitudinal performance dynamics of several popular recommendation techniques, including an item-based nearest-neighbor approach (ItemKNN) (Sarwar et al. 2001), a matrix factorization approach based on SVD (Koren 2008), and a deep-learning approach item-based Autoencoder (I-AutoRec) (Sedhain et al. 2015).<sup>4</sup> Our results demonstrate highly consistent bias-related patterns across these techniques. Because of page limits, we report only the results of ItemKNN and I-AutoRec in the paper. Results for all techniques can be found in Online Appendix D. Online Appendix E includes a summary of the final hyperparameters and grid search settings for all techniques. Also, in all experiments, we repeat the simulation 10 times and report the average results. The detailed mean and standard deviation values of the 10 runs are reported in Online Appendix F.

## 4. Experiment 1: Longitudinal Dynamics with Varying Degrees of Bias

Our main objective is to understand how biased feedback influences the system’s performance over time. The first set of experiments focuses on exploring homogeneous user populations with the same level of bias; that is, all users are affected by the system predictions to the same extent. We consider preference biases caused by the intrinsic prediction errors of recommendation algorithms.

## 4.1. Experiment Setting

In Experiment 1, we examine the preference biases caused by the prediction errors of recommendation algorithms $( \mathrm { i . e . , }$ the deviations between users’ true preferences and the system’s predictions). Prediction errors are inherent to RS (i.e., their predictive models are not 100% accurate), yet the errors can cause preference biases in postconsumption user ratings.

We vary the bias degree from zero to one to simulate different levels of user preference biases. At one extreme, a bias degree of zero means that users are not affected at all by the displayed system predictions (i.e., users’ postconsumption ratings are the same as their true preference ratings). In contrast, a bias degree of one represents the other extreme, where users report their preferences entirely based on the system’s predictions (i.e., users postconsumption ratings are the same as the system’s predicted ratings). In this set of experiments, we simulated homogeneous user populations with six different bias degrees: 0, 0.2, 0.4, 0.6, 0.8, and 1. We control for all other variables, including item features, users’ prefer ences, consumption frequency, users’ reliance on recommendations, etc.

## 4.2. Results

Figure 1 illustrates the temporal changes in the overall RMSE (i.e., predictive accuracy), the average true rating of consumed items (i.e., consumption relevance), and the number of unique items consumed (i.e., consumption diversity) for ItemKNN and I-AutoRec based on Netflix and Yelp data. The results indicate biases in users’ postconsumption ratings caused by the RS’s inherent prediction errors significantly affect the system’s longitudinal dynamics and consumption outcomes.

In terms of the system’s predictive accuracy, as illustrated in the first row of Figure 1, when bias � 0 (i.e., meaning that users submit their true preference ratings), as more user ratings get submitted to the system over time, the system’s overall predictive accuracy across all items naturally improves (i.e., RMSE keeps decreasing). When bias > 0, users’ submitted ratings are pulled toward the displayed system predictions.

Figure 1. (Color online) Impact of Varying Degrees of Preference Biases  
(a) Accuracy (Netflix, ItemKNN)  
![](/api/attachments/72KZPB3W/fulltext/images/dc0436d18019cfbc876c50add5391ba48fe6d20cf2b909b05ec54474a108967b.jpg)  
(b) Relevance (Netflix, ItemKNN)

(d) Accuracy (Netflix, I-AutoRec)  
![](/api/attachments/72KZPB3W/fulltext/images/55d720b230f1e6a6b1754dd7ed7eeb98501049bdf4b55fa996be200357632b19.jpg)  
(e) Relevance (Netflix, I-AutoRec)

(g) Accuracy (Yelp, ItemKNN)  
![](/api/attachments/72KZPB3W/fulltext/images/a53508326abcd5a588edb23a2f2208c3b12e9938c3d8be19b2b0006cd155bb96.jpg)  
(h) Relevance (Yelp, ItemKNN)

(j) Accuracy (Yelp I-AutoRec)  
![](/api/attachments/72KZPB3W/fulltext/images/f758f2b7d52f65eeb6d5671fc7f3ee75055b47c99da6991f40a273c263128084.jpg)  
(k) Relevance (Yelp, I-AutoRec)

![](/api/attachments/72KZPB3W/fulltext/images/fc712385b890e087976f1771ed6b964e57a70d7c2fb94b998e15f430d29caa49.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/0f93467077084218daa784694313ca7405f60409b06d9e242add02eec8cbc4e6.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/a07cec283798f492fe03976bd446ff9e38a156c5368ec379fca2eac2bad867e0.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/83efc7c6a0805990b95e2bd98efe4d138119c46cbbaf6e26a00a032fd72dc908.jpg)  
(i) Diversity (Yelp, ItemKNN)  
(l) Diversity (Yelp, I-AutoRec)

(c) Diversity (Netflix, ItemKNN)  
![](/api/attachments/72KZPB3W/fulltext/images/9d089735027c145d67aeb5cf2094955d9d169995720233a7dedcefcf235cb9da.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/f6ceeb4d065af9fdb80b45fa15d1c8faaa31772e946d04b03d959de05f8758c3.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/5a2df999058aff56baa3589a597b2b8411c0fe0e9bebe0b876552af40e22d737.jpg)  
+bias=0 ▲ bias=0.2 bias=0.4bias=0.6bias=0.8 ×bias=1.0

![](/api/attachments/72KZPB3W/fulltext/images/626e67685f7fd637110819a4f66eeb294e1c5eda691465d46e1b790c088a19ce.jpg)

Because the system is not entirely accurate, these ratings are contaminated by the system’s inherent prediction errors and then added to the system’s training data, weakening the system’s ability to learn users’ true preferences. As the bias increases from zero to one, the improvement in RMSE becomes smaller over time. When bias is close to one (i.e., users’ postconsumption ratings are close to the displayed system ratings), the overall RMSE can even increase over time, demonstrating a disruptive impact of high preference bias. In terms of consumption relevance (see the second row of Figure 1), our results show that, when bias increases from 0 to 0.8, the trends of consumption relevance are nearly indistinguishable from that of $b i a s = 0 .$ . However, when bias further increases from 0.8 to 1, we observe a more substantial decrease of consumption relevance across all simulation periods. In other words, the changes in consumption relevance are not linearly proportional to the size of bias. In addition, the third row of Figure 1 illustrates the changes in consumption diversity over time. In general, consumption diversity improves over time, but its improvement is negatively associated with the bias degree: the largest diversity growth over time is observed when bias � 0, and the growth becomes much smaller as bias increases.

Overall, our results show that preference bias signifi cantly impairs the RS predictive performance (i.e., overall prediction accuracy) as well as consumption outcomes (i.e., consumption relevance and diversity). An important observation is that the impact of preference bias on consumption outcomes is nonlinear in the size of the bias; that is, very large bias causes disproportionately large negative effects on RS performance. The next subsection further explores this phenomenon.

## 4.3. Analysis of Preference Bias Effects on System Performance

To obtain a more in-depth understanding of the potential mechanisms that drive the (nonlinear) effects of pref erence bias on longitudinal RS performance, we conduct a series of analyses of the simulation process and intermediate results. We investigate the changes in the training data (i.e., users’ submitted ratings) and the items different susceptibility to bias. Because of page limits, we include only the analysis results of the ItemKNN algorithm on the Netflix data in the main paper.

4.3.1. Inflation of Users’ Submitted Ratings. The underlying mechanism of how preference bias influences RS performance is based on rating inflation (represented by the difference between submitted and ground-truth ratings). As discussed earlier, preference bias injects distortions into underlying rating data by affecting users submitted postconsumption ratings. Specifically, substantial bias can create large inflation on some consumed items and distort their average ratings $( \mathrm { i . e . , }$ distort the underlying training data). In subsequent periods, these highly inflated items will receive higher predicted scores from recommendation algorithms and, thus, are more likely to be recommended to users.<sup>5</sup> Further, these recommendations will lead to new consumptions, which in turn will lead to additional biased ratings and reinforce the rating inflation on these items. As a result, preference inflation can accumulate over time. The dynamics of rating inflation are explored in Figure 2, where we vary the population bias degree from zero to one with an increment of 0.2 and examine its impact during the 100 simulation time periods. In particular, Figure 2(a) shows a disproportionately large influence of the high levels of bias on consumption relevance: as the bias degree increases, the mean relevance of the consumed items decreases nonlinearly. This is directly related to the fact that, as bias increases from zero to one, the mean rating inflation increases in an accelerating fashion (Figure 2(b)). In other words, for small levels of bias, the rating inflation for consumed items is minimal; as bias increases, a sizable inflation in users’ submitted ratings is created.

Figure 2, (c) and (d), provides an explanation of the nonlinear effects of bias observed in Figure 2, (a) and (b). Specifically, for high levels of bias, there will be disproportionately more ratings submitted with high inflation (Figure 2(c)). This will lead to substantial differences in underlying rating data, as illustrated by the number of items with very high average ratings (Figure 2(d)). When the rating inflation is high enough, it will distort the underlying rating data sufficiently enough to push some of these items into the top recommendation lists, which will then start affecting users’ consumption choices. This can generate more biased ratings in the future and have a snowball effect over time.

4.3.2. Items’ Susceptibility to Preference Bias. An important question is: Are all items equally susceptible to preference bias? For example, are some items more susceptible and do they accumulate inflation more easily than others? In our analysis, we focus on two item char acteristics: (i) the popularity of an item $( \mathrm { i . e . , }$ , the amount of consumptions) and (ii) the content distinctiveness of an item (i.e., the number of other items that share simila content features with the focal item). We conjecture that unpopular items (i.e., items with few consumptions) and content-wise common items (i.e., items that share similar features with many other items) are more likely to accumulate the rating inflation than items that are more popular and more distinctive. For unpopular items, because they do not have many preexisting ratings, a small number of inflated new ratings could easily increase their average rating, which leads to inflation in the system’s predicted scores for these items in subsequent periods. For common items, the inflation in their feedback ratings will bias the predictive model to inflate the predictions for other items with similar features. The more common a focal item is (i.e., the more “similar” items it has), the more other items are biased by the focal item’s inflated ratings. In subsequent periods, these similar items are more likely to be recommended and consumed, which, in turn, leads to additional inflated user ratings, and consequently reinforces the bias of the pre diction model and further inflates the system’s predic tions for the focal item.

To test this conjecture, we compare the consumptions of the same group of items consumed by user populations with different bias degrees. Specifically, we focus on all the items consumed in the first period (t � 1). Because of the same system initialization, these item consumptions are identical across all bias levels, and, thus, represent an ideal set for comparison. We then compare the consumption counts of these items over 100 iterations under two bias levels: zero and one.

Figure 2. (Color online) Analysis of Preference Bias Impact on Users’ Submitted Ratings (Netflix, ItemKNN)  
(a) Mean relevance of all consumed items  
![](/api/attachments/72KZPB3W/fulltext/images/cf5740388a7758b7dfac6127168cef2c2b2704c70b2ab9850461be80786b3255.jpg)

(b) Mean inflation of submitted ratings  
![](/api/attachments/72KZPB3W/fulltext/images/c13a35da64c49677bf093611bab5c1f06daeca1c7511c8f3da2c2d81b67a3d66.jpg)

(c) Number of submitted ratings with inflation > 2  
![](/api/attachments/72KZPB3W/fulltext/images/ed6f4b213c44f4e9b0125f5d7ffe910fb1d77a6e202381089e001e1940ded3e6.jpg)

(d) Number of items with average rating > 4.5  
![](/api/attachments/72KZPB3W/fulltext/images/30116ea1a339956b84226221fc0c6a314b0cb24956dfd03c45a9043a64a98ef3.jpg)  
+bias=0 ▲ bias=0.2 bias=0.4bias=0.6bias=0.8 ×bias=1.0

Table 4. Consumption Distribution over 100 Iterations of Items in Different Categories (Netflix, ItemKNN)

<table><tr><td colspan="3"></td><td>N</td><td>Bias = 0</td><td>Bias = 1</td></tr><tr><td colspan="3">Total consumption of big-error items</td><td>100</td><td>25,797</td><td>47,391</td></tr><tr><td rowspan="4">% Consumptions of subgroups of big-error items</td><td rowspan="2">Subgroup based on consumption popularity</td><td>Popular</td><td>43</td><td>43.23%</td><td>2.86%</td></tr><tr><td>Unpopular</td><td>57</td><td>56.77%</td><td>97.14%</td></tr><tr><td rowspan="2">Subgroup based on content distinctiveness</td><td>Distinctive</td><td>36</td><td>28.30%</td><td>6.39%</td></tr><tr><td>Common</td><td>64</td><td>71.70%</td><td>93.61%</td></tr></table>

Among all items consumed at t � 1, we first categorize them based on the size of their prediction errors. If an item’s average prediction error surpasses the median error value, we classify it as a “big-error” item. Otherwise, we classify it as a “small-error” item. Because users rely on system recommendations to choose items, all these consumed items have high predicted ratings. Thus, the big-error items are likely to have lower true ratings that were predicted to be high, whereas the small-error items likely are the true high-rating items. To analyze preference inflation, we focus on the big-error items because bias will have an impact when prediction error is substantial; in contrast, bias has minimal impact on feedback ratings for small-error items regardless of bias levels.

We further classify the big-error items by their popularity and content distinctiveness. First, we separate these items based on their popularity score (i.e., each item’s consumption count) at initialization. If an item’s popularity is less than the median popularity score of all items in the system, it is classified as an “unpopular” item. Otherwise, it is a “popular” item. Second, we separate the big-error items based on the distinctiveness of their content. In particular, we measure the contentbased similarity between each pair of items based on the cosine similarity of their latent feature vectors (i.e., Item-Content). Then, for each item, we calculate the number of its “neighbors,” which is defined as any item with a similarity score above 0.8.<sup>6</sup> Using the median number of neighbors of all items in the system, we classify the items with a high number of neighbors as “common” items and the other half (i.e., with a low number of neighbors) as “distinctive” items.

Table 4 summarizes the size and consumption count of different item subgroups. It shows that the presence of bias significantly raises the consumption of big error items. Also, comparing the subgroups of the big error items, with bias, users consume substantially more unpopular items (i.e., 97.14% of the big-error consumptions are unpopular items when bias � 1 versus 56.77% when bias � 0) and more common items (i.e., 93.61% of the big-error consumptions are unpopular items when bias � 1 versus 71.7% when bias � 0), and fewer popular and distinctive items, correspondingly. That is, preference bias significantly inflates the consumption of unpopular and common items.

We further plot the longitudinal changes of the mean item consumption for the “unpopular” (Figure 3(a)) and “common” (Figure 3(b)) subgroups of the bigerror items, when users have bias zero and one. As shown in the figure, with bias, users increasingly con sume more and more of the unpopular and common items. With high bias (i.e., bias � 1), users’ ratings are significantly inflated by the system’s inaccurate initial predictions at t � 1. These inflated ratings are then used as new input data by the system for subsequent recommendation generations. Items that are less popular and less distinctive are more likely to be influenced by these inflated ratings, leading to increasingly more recommendations and consumptions of these items in subsequent periods.

We further vary the degree of bias from 0 to 1 by 0.1. Figure 3, (c) and (d), compares the mean consumption count of different subgroups of big-error items over 100 iterations. The figure shows that bias does not evenly influence all items but changes users’ consumption in certain directions—that is, as the bias degree increases, the consumption of unpopular and common items increases nonlinearly in an accelerating fashion, whereas the consumption of popular and distinctive items decreases.

Figure 3. (Color online) Mean Item Consumption of Subgroups of Big-Error Items (Netflix, ItemKNN)  
(a) Unpopular items  
![](/api/attachments/72KZPB3W/fulltext/images/3953411a79a440d65260d25b7d5d28b62e9113bb72d39c1a86b9186f5cbd237b.jpg)

(b) Common items  
![](/api/attachments/72KZPB3W/fulltext/images/9b95f2e4588981ee75124b964b7240a819a402d62fc3fc1dab9dad6aeab39bdc.jpg)

(c) Popular vs. Unpopular  
![](/api/attachments/72KZPB3W/fulltext/images/32456e47e34fcf811772b5afc9434596d5094c85728133ce9df12d5b6512f80b.jpg)

(d) Distinctive vs. Common  
![](/api/attachments/72KZPB3W/fulltext/images/9dfddbf856f4e9363ff6ecee963957564978c7814004d35f6938eb205bff65fd.jpg)

In summary, Experiment 1 shows that, as preference bias increases from zero to one, the user-submitted ratings are pulled farther away from users’ true preferences. More specifically, a high degree of bias introduces large inflation in ratings of consumed items (especially so for unpopular and common-content items) and moves them into top-ranked recommendations for more users. This distorts the RS’s training data over time and, consequently, negatively affects the system’s predictive accuracy and users’ consumption outcomes.

## 5. Experiment 2: Heterogeneous User Populations

Experiment 1 focused on understanding the general effect that the preference bias degree has on the RS longitudinal performance and, thus, used user populations with homogeneous bias, that is, where every user had the same degree of preference bias. However, real users may exhibit different degrees of bias. Therefore, Experiment 2 explores the user populations with heterogeneous preference biases, focusing specifically on the interplay between subpopulations with different bias degrees.

## 5.1. Experiment Setting

We explore the impact of bias heterogeneity using two extreme bias degrees (i.e., zero and one) and model users using two subpopulations with different degrees of bias: (a) a “high-bias” group in which each user has the same bias level 1, and (b) a “no-bias” group in which each user has bias level 0. We investigate two ways of separating users: (i) 50/50-random, which randomly assigns 50% of the users into the “no-bias” group and the other 50% into the “high-bias” group; (ii) 50/50-frequency, which assigns users based on their consumption frequency; that is, the high-consuming 50% of users are assigned to a “high-bias” group and the remaining users to a “no-bias” group. To compare RS performance in the presence of heterogeneous versus homogeneous bias populations, we also include the results of homogeneous populations with biases 0 and 1 (from Experiment 1). Thus, we compare four user populations: (1) “100-bias(0)” where all users have bias 0, (2) “50/50-random,” (3) “50/50-frequency,” and (4) “100-bias(1)” where all users have bias 1.

## 5.2. The Longitudinal Effect with Heterogeneous Biases

Figure 4 compares the overall prediction accuracy, consumption relevance, and consumption diversity across the four user populations on two application settings (Netflix and Yelp). We use the same recommendation techniques as in Experiment 1. The results are highly consistent across recommendation algorithms and application settings.

In terms of the system’s predictive accuracy (Figure 4, (a), (d), (g), and (j)), the performance of “50/50-random” lies in between the two homogeneous situations (i.e., bias 0 and 1), as would be expected. Also, the accuracy of “50/50-frequency” is always worse than that of “50/ 50-random,” because a higher number of inflated ratings is submitted to the system in “50/50-frequency.” However, interestingly, as shown in Figure 4, (b), (e), (h), and (k), the average consumption relevance of the two heterogeneous populations, that is, “50/50-random” and “50/50-frequency,” is largely comparable to that of the homogeneous population with no bias (i.e., “100- bias(0)”), and much better than that of the homogeneous population with bias 1 (i.e., “100-bias(1)”). This suggests that, even when half of the users have bias 1, the system can still successfully identify highly relevant items for all users. However, it does not mean that users still consume the same items. In fact, the recommendation diversity of “50/50-random” and “50/50-frequency” is substantially lower than that of the “100-bias(0),” as shown in Figure 4, (c), (f), (i), and (l), suggesting that the recommendations (and, consequently, consumptions) are more concentrated for the two heterogeneous populations (“50/50-random” and “50/50-frequency”) when compared with “100-bias(0).”

We further examine the item consumption distribution of different user populations. Similar to the approach in Section 4.3, we only focus on the items that are consumed in t � 1 (because they are the same across all user popula tions and, thus, represent an ideal set for comparison) and have large prediction errors (because bias only has an impact on user-submitted ratings when the prediction error is substantial). We classify these items by their initial popularity and content distinctiveness and then compare their consumption distributions for different user populations. Figure 5 illustrates the analysis results and further validates the finding from Experiment 1 that the consumption differences mainly concentrate on items with low popularity and common content. Specifically, as shown in Figure 5, (a) and (b), the “50/50-random” and “50/50-frequency” populations have a comparable number of unpopular and common item consumptions to the homogeneous population “100-bias(0).” The difference is nonlinear to the ratio of users with bias 1; that is, the results of “50/50-random” and “50/50-frequency” are much closer to “100-bias(0)” than “100-bias(1).”

We further vary the mixture of heterogeneous user populations by assigning 0%, 10%, 20%, … , 100% of randomly selected users to have bias 1 and the remaining users to have bias 0. Figure 5, (c) and (d), compares the mean consumption count of different subgroups of big-error items over 100 iterations, for the different population mixtures. As the ratio of users with bias 1 increases, the consumption of unpopular and common items increases nonlinearly in an accelerating fashion, whereas the consumption of popular and distinctive items decreases. This suggests that, when the user population contains a small percentage of biased users, the inflation in submitted ratings is not large enough to substantially distort the consumption outcomes. But when the ratio of biased users is high, large inflation in submitted ratings will start affecting the top-ranked recommendation list.

Figure 4. (Color online) Impact of Heterogeneous Biases  
(a) Accuracy (Netflix, ItemKNN)  
![](/api/attachments/72KZPB3W/fulltext/images/895a5047d89f968205a3c750e49a3d369930f6376f090fbf1865e88ec4511ab3.jpg)  
(b) Relevance (Netflix, ItemKNN)

(d) Accuracy (Netflix, I-AutoRec)  
![](/api/attachments/72KZPB3W/fulltext/images/a03405ddb4438a19c61e65d197b08a63f8053e40d681a44914cf43af1d2e337a.jpg)  
(e) Relevance (Netflix

(g) Accuracy (Yelp, ItemKNN)  
![](/api/attachments/72KZPB3W/fulltext/images/4395ad84effffc1834e74d8a546aaa74f6903cb0e162ac779abb7e39b9199e49.jpg)  
(h) Relevance (Yelp,  
(j) Accuracy (Yelp, I-AutoRec)

![](/api/attachments/72KZPB3W/fulltext/images/908aa63cb6a22c12a2ac822f5e7960d59b9ceaeac0bde4a14c94056b00dd45d9.jpg)  
(k) Relevance (Yelp, I-AutoRec)

![](/api/attachments/72KZPB3W/fulltext/images/0d834edee3a6deeb85cf54b29296846b6698d5f2bb90c3a788df8d845c1a6619.jpg)  
(c) Diversity (Netfix, ItemKNN)

![](/api/attachments/72KZPB3W/fulltext/images/804a1945bdd0e725fe28eb4571f8b2d4bdf720d576fb8ac6cc21eb94a5e34191.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/c40bc2cb63a775ad11eb674d751f92911a11f6e68eabd73eb312d2dbc4d6f939.jpg)  
(f) Diversity (Netflix, I-AutoRec)

![](/api/attachments/72KZPB3W/fulltext/images/56efcf98754a4c5a7bc450379593c08bc1d76350411905559839b9bc7c6912bd.jpg)  
(i) Diversity (Yelp, ItemKNN)  
(l) Diversity (Yelp, I-AutoRec)

![](/api/attachments/72KZPB3W/fulltext/images/5cd8da4fd9347ff8c2373efb525a35a2c375fd8450899ebbbe1a3cb76e839697.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/f897678cb4a0269f8d0f69654877497f6a9de1d4381e82c2497cce41f457392b.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/4b8d4c9556f733ffb75dd968c8aa8c1736cfc5ad462400e6ae83ae7e3515b187.jpg)  
+ 100-bias(0) ×100-bias(1)50/50-frequency 50/50-random

![](/api/attachments/72KZPB3W/fulltext/images/69e8681c4d3794a41103d8092e9ee5ab957e5a114def9c1aa0f91d91a53ca67a.jpg)

## 5.3. Spillover Effects Between Subpopulations with Heterogeneous Biases

In Section 5.2, we observed that, when a subset of users with bias 1 submits biased feedback ratings, these ratings influence the overall RS performance. As a result, even the users that do not have preference bias may also be affected. On the other hand, for users with bias 1, their recommendations may be partially corrected by the unbiased ratings from their counterparts without bias. In other words, both subpopulations may provide and/or receive spillover effects. Thus, this section

Figure 5. (Color online) Mean Consumption of Subgroups of Big-Error Items for Heterogeneous Users (Netflix, ItemKNN)  
(a)  
![](/api/attachments/72KZPB3W/fulltext/images/58ed564227e01a38bc6333d668a32b9edfdb49f8df502cf48ef98a67b8488145.jpg)

(b) Common items  
![](/api/attachments/72KZPB3W/fulltext/images/a6dcea6351524361040cb344e1ffbb3352bd2f6852d27da7339ac2d6d5eae248.jpg)

(c) Popular vs. Unpopular  
![](/api/attachments/72KZPB3W/fulltext/images/6ab01ddc736bacd1df548d0904cdba85529352a6b5c3ccc242f5787d4824c2f6.jpg)

(d) Distinctive vs. Common  
![](/api/attachments/72KZPB3W/fulltext/images/a2e3b309386c5c2c005cc832bc5abecf0fdb51d5b0da6229b120d6f80168c960.jpg)

A-bias(1), B-bias(0)

Figure 6. (Color online) Performance for Focal Group A (Netflix, ItemKNN)  
![](/api/attachments/72KZPB3W/fulltext/images/d752d0d2517e43dac82d0d9a07657881bb2c5dd4b6c307a0435dd7769ed9f6e1.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/1bbc068eef3320fa5a582e40ad2bddf30645aa840c1caedf46373d7c391cf689.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/d51741efdfe9951aed06e1b21727ce79de5aaf7e48cfc9d8bd2cbd3680abdfdb.jpg)

investigates the potential spillover effects of preference biases between user subpopulations.

To explore the impact of heterogeneous biases, we randomly separate all users into two groups, A and B, and assign them two levels of preference biases, 0 and 1. This generates four different user populations: (1) “A-bias(0), B-bias(0)” where both A and B have bias 0; (2) “A-bias(0), B-bias(1)” where A has bias 0, and B has bias 1; (3) “A-bias(1), B-bias(0)” where A has bias 1, and B has bias 0; and (4) “A-bias(1), B-bias(1)” where both A and B have bias 1. Because the two groups are distributionally identical (as each represents a random half of the same population), we use group A as the focal group to illustrate the spillover effects between the two groups. Figure 6 compares the recommendation performance of the ItemKNN algorithm for group A in the Netflix application setting. The results for other algorithms and/or in other application settings, reported in Online Appendix D, are highly consistent. As shown in Figure 6, group A performances in the two homogeneous population settings in which users either all have bias 0 or bias 1 provide the upper and lower bounds for the system’s accuracy, relevance, and diversity performance.

Let’s consider the accuracy performance for group A under two heterogeneous population scenarios, “Abias(0), B-bias(1)” and “A-bias(1), B-bias(0).” As shown in Figure 6(a), accuracy for group A in the “A-bias(0), B-bias(1)” setting is highly consistent with that of “A-bias(0), B-bias(0).” On the other hand, the accuracy performance for group A in the “A-bias(1), B-bias(0)” setting is more similar to (though slightly better than) that of “A-bias(1), B-bias(1).” Therefore, group A performance is extremely different under two heterogeneous population scenarios, depending on whether group A has bias. Furthermore, the spillover effects between the focal group A and its peer group B are highly asymmetric. When the focal group has bias, if the peer group has no bias, then the peer group’s data will provide positive spillover effects on A’s accuracy (i.e., when A has bias 1, the accuracy for A is better when B has bias 0 than when B has bias 1). However, when the focal group has no bias (i.e., A with bias 0), if the peer group has bias (i.e., B with bias 1), we do not see a decrease in the prediction accuracy of A. That is, interestingly, no significant negative spillover effect is observed on the focal group’s accuracy when only the peer group has bias.

Within heterogeneous population mixtures, the relevance and diversity for the focal group A are consistently higher in the “A-bias(0), B-bias(1)” scenario than in “A-bias(1), B-bias(0),” as shown in Figure 6, (b) and (c). Also, in both heterogeneous population mixtures, the relevance and diversity of the focal group’s consumption (whether it is the group with bias) are worse than those of “A-bias(0), B-bias(0).” That is, even though the focal group has no bias (i.e., A with bias 0), if its peer group has bias 1 (i.e., B with bias 1, as opposed to 0), the focal group’s consumption relevance and diversity are slightly (and negatively) affected; that is, small negative spillover effects are observed. On the other hand, when the focal group has bias 1 (i.e., A with bias 1), if its peer group has no bias (i.e., B with bias 0, as opposed to 1), the focal group’s consumption relevance and diversity are substantially and positively elevated; that is, large positive spillover effects are observed.

We conducted further analyses of the spillover effect between subpopulations of users with different bias degrees (i.e., subgroups A and B). Our results, reported in Online Appendix I, show that the spillover effect can be attributed to the differential rating inflation across the two subgroups. Also, in addition to the “50/50-random” split, we explored the “50/50-frequency” split based on consumption frequency (i.e., A includes more-frequently consuming users and B includes less-frequentlyconsuming users). We conducted a similar analysis to examine the spillover effects between the subgroups of this heterogeneous population. The results, reported in Online Appendix G, are highly consistent with the ones for the “50/50-random” split reported in this section.

Overall, we observe small negative spillover effects from the biased subpopulation on the unbiased subpopulation regarding accuracy, relevance, and diversity. In contrast, we observe much larger positive spillover effects from the unbiased subpopulation on the biased subpopulation, especially in consumption outcomes (as measured by consumption relevance and diversity). One practical implication of this finding is that it highlights the benefits of population diversification.

## 6. Experiment 3: Post Hoc Rating Debiasing

Given the well-established phenomenon of preference bias and its impact on longitudinal RS performance, we explore how to mitigate or eliminate preference bias. That is, can user-submitted ratings be adjusted to remove this bias? In this section, we discuss some of the key challenges of reducing preference bias. We use the same data sets and recommendation algorithms as in the previous experiments. To simulate the realistic, heterogeneous, noisy bias levels of real-world users, we model the preference bias $( b i a s _ { u i } )$ of user u for item i as follows:

$$
b i a s _ {u i} = b i a s _ {u} + \epsilon_ {u i}, \quad b i a s _ {u} \sim \mathcal {N} (a, b) \quad \epsilon_ {u i} \sim \mathcal {U} (- c, c)\tag{7}
$$

Specifically, bias follows a uniform distribution centering around user u’s mean bias, that is, bias . The noise, $\epsilon _ { u i } ,$ is uniformly distributed following $\mathcal { U } ( - 0 . 1 _ { \cdot }$ 0:1), whereas $b i a s _ { u }$ is drawn from a normal distribution ${ \mathcal { N } } ( a , b )$ . A higher value of a means a higher average bias of the user population, and a higher value of b means more heterogeneity among users in terms of bias levels. In our experiments, we simulate four representative settings of user populations (i.e., high versus low bias and high versus low heterogeneity): ${ \mathcal { N } } ( 0 . 8 ,$ 0:2), N (0:8, 0:05), N (0:4, 0:2), N (0:4, 0:05). Also, $b i a s _ { u i }$ should be within the range from zero to one, so we truncate the values at both ends. The noisy individual bias distribution (as detailed in Equation (7)) not only allows us to examine and address debiasing challenges that arise when dealing with populations exhibiting diverse bias levels, but also reflects practical, realistic, and demanding settings where the ability to detect each individual’s bias degree with perfect accuracy is fundamentally highly unlikely and, thus, which represent important testing environments for debiasing techniques.

## 6.1. Debiasing with Computational Approaches Using Historical Rating Data

One stream of approaches for dealing with biases in RS has been to design computational, algorithmic approaches for detecting bias in historical (already collected) data (e.g., preference ratings) and correcting data accordingly. Prior literature has proposed several post hoc debiasing approaches for adjusting the usersubmitted ratings. The intuition behind such post hoc adjustments is to “reverse-engineer” users’ true ratings from their submitted ratings by removing biasing effects caused by various factors (such as system recommendations, item popularity, and average ratings).

One example of such work is the Historical Influence Aware Latent Factor (HIALF) model (Zhang et al. 2019), an algorithm with the general goal of detecting and mitigating biases in users’ historical rating data. HIALF positions itself as a method capable of detecting bias patterns in historical rating data and adjusting for such patterns, resulting in improved prediction per formance. HIALF has shown better performance than several other debiasing methods, such as HEARD (Wang et al. 2014) and LF (Ricci et al. 2010). HIALF models the potential impact of “user expectations” and “item quality” on the user-submitted rating of each consumed item. In particular, the authors conjecture an assimilation-contrast effect: users either “assimilate” (conform) to historical ratings (which represent user expectations) if these ratings are not far from the item quality, or users “contrast” (deviate) from historical ratings if these ratings are significantly different from the item quality. Therefore, each (biased) submitted rating can be modeled by:

$$
\hat {r} _ {i, k, u} = g + b _ {u} + b _ {i} + x _ {u} ^ {T} y _ {i} + a _ {u} f (| \mathcal {H} _ {i, k} |) \beta (e _ {i, k} - q _ {u, i}).\tag{8}
$$

Here, $\hat { r } _ { i , k , u }$ denotes the k-th rating of item i, which is submitted by user u; g is the overall average rating; $b _ { u }$ and $b _ { i }$ denote the average deviations of user u and item i from the overall average rating, respectively; $x _ { u }$ and $y _ { i }$ represent latent feature vectors for user u and item i. All these components are the same as those in the traditional latent factor models used for RS (e.g., Ricci et al. 2010). Further, $a _ { u }$ models how easily user u will be influenced by historical ratings; larger $a _ { u }$ means that user u is more easily affected. $\mathcal { H } _ { i , k }$ denotes a sequence of k-1 prior ratings on item i and $| \mathcal { H } _ { i , k } |$ is the set size; $e _ { i , k }$ denotes the prior expectation formed on $\mathcal { H } _ { i , k }$ which is calculated as the average of the ratings weighted by their submission recency; $q _ { u , i }$ denotes user $u ^ { \prime } \mathrm { s }$ experienced quality of item i and is modeled as $q _ { u , i } = g + \bar { b } _ { i } + x _ { u } ^ { T } y _ { i }$ . Last, f and $\beta$ are defined as magnitude function and kernel regression. The last term in Equation (8) is conjectured to represent the bias information in a submitted rating. Using the proposed HIALF model, one can obtain users’ and items’ intrinsic features $( b _ { u } , b _ { i } , x _ { u } , y _ { i } )$ and calculate the debiased rating for user u and item i as

$$
r _ {i, u} = g + b _ {u} + b _ {i} + x _ {u} ^ {T} y _ {i}.\tag{9}
$$

In order to explore HIAL $\mathbf { \nabla } \mathbf { F } ^ { \prime } \mathbf { s }$ potential to reduce preference bias, we apply it on heterogeneous user populations affected by different degrees of bias. Following the procedure described in Section 3.1, users submit postconsumption ratings to the system, and these ratings are biased according to Equation (7). Because HIALF is a one-snapshot debiasing strategy, we apply it to all ratings submitted by users during the simulation at the end of 100 iterations. We then compare the rating prediction accuracy (measured in RMSE) based on training data that are either debiased by HIALF or not.

Table 5. Prediction Accuracy (RMSE) When Training Ratings Are Debiased vs. Not Debiased (Netflix)

<table><tr><td rowspan="2">Prediction accuracy (RMSE)</td><td colspan="3">ItemKNN</td><td colspan="3">I-AutoRec</td></tr><tr><td>NoDebias</td><td> $HIALF_{all}$ </td><td> $HIALF_{sim}$ </td><td>NoDebias</td><td> $HIALF_{all}$ </td><td> $HIALF_{sim}$ </td></tr><tr><td> $\mathcal{N}(0.8,0.2)$ </td><td>0.9431</td><td>1.0612</td><td>0.9557</td><td>0.9289</td><td>1.0451</td><td>0.9508</td></tr><tr><td> $\mathcal{N}(0.8,0.05)$ </td><td>0.9424</td><td>1.0615</td><td>0.9561</td><td>0.9287</td><td>1.0453</td><td>0.9504</td></tr><tr><td> $\mathcal{N}(0.4,0.2)$ </td><td>0.9378</td><td>1.0571</td><td>0.9526</td><td>0.9229</td><td>1.0418</td><td>0.9419</td></tr><tr><td> $\mathcal{N}(0.4,0.05)$ </td><td>0.9373</td><td>1.0571</td><td>0.9518</td><td>0.9236</td><td>1.0416</td><td>0.9402</td></tr></table>

Table 5 presents the rating prediction accuracy and the debiasing performance results of two recommendation algorithms, ItemKNN and I-AutoRec, on the Netflix data.<sup>7</sup> We compare three scenarios: “NoDebias,” $\mathrm { H I A L F } _ { a l l } ,$ and $\mathrm { H I A L F } _ { s i m } .$ In the “NoDebias” case, submitted ratings are not adjusted—we train the recommendation algorithms using the biased ratings and compute the prediction accuracy on the remaining unknown ratings (i.e., the same RMSE calculation used in prior experiments). In the $\mathrm { H I A L F } _ { a l l }$ case, we apply HIALF on all the historical ratings, including both the initialization ratings and the submitted ratings during 100 simulation iterations. However, in our simulation setting, debiasing may not be necessary for the initialization ratings because they are not biased. Therefore, in the $\mathrm { H I A L F } _ { s i m } ^ { - }$ case, only the biased submitted ratings generated over 100 simulation iterations are debiased using $\mathrm { H I A L F } ^ { 8 }$ These debiased ratings are then merged with the unbiased initialization ratings to train a recommendation algorithm. Table 5 shows that, as might be expected, $\mathrm { H I A L F } _ { s i m }$ performs better than $\mathrm { H I A L F } _ { a l l }$ under all four bias degree settings. Importantly, however, the prediction performance for both $\mathrm { H I A L F } _ { a l l }$ and $\mathrm { H I A L F } _ { s i m }$ is actually worse than that of $' \mathrm { { N o D e b i a s } ^ { \prime \prime } ; }$ that is, using HIALF to address preference bias is less advantageous than leaving biased rating data as is. In summary, the results suggest that HIALF cannot effectively eliminate preference bias from historical data of user-submitted ratings.

The poor performance of HIALF illustrates key challenges in reducing preference bias. In particular, there are many types of biases. Different, specialized techniques may need to be developed to deal with different biases. Also, in some cases, just the knowledge of the standard historical data (e.g., previously submitted preference ratings by users) may not be sufficient for successful debiasing; that is, additional knowledge of users’ behavior may be necessary. HIALF makes some highly specific assumptions about hypothetical user behavior, for example, that users’ submitted ratings are biased by the weighted average of historical ratings. If these assumptions do not match the actual user behavior (as is the case with HIALF for our scenario and possibly for many other recommendation settings), the debiasing would be highly challenging. In the real world, users may not be aware of the other (historical) ratings for a given item, and may not be influenced by rating recency. In other words, it is clear that HIALF cannot be considered as a general-purpose debiasing approach, as it is explicitly designed to model the bias entirely based on the assimilation-contrast effects, while not considering other types of bias (e.g., preference bias, position bias), patterns of which may not be identifiable from traditional rating data. As discussed below, designing effective approaches for addressing preference bias will likely involve going beyond the analysis of traditional rating data and toward a deeper understanding of the specific preference bias levels of different users.

## 6.2. Debiasing with Global and Individual Bias Knowledge

As discussed in Section 2.2, preference bias is an inherent decision-making bias where user-submitted postconsumption preference ratings tend to be influenced by the system-predicted ratings (typically observed by the users during their preconsumption decision processes, such as item selection). Thus, for accurate debiasing of a given user-submitted rating, it is important to have information about the system-provided rating (if any) that the user was exposed to as well as some understanding of the specific user’s level of bias (i.e., susceptibility to the type of influence in question). In this subsection, we propose and explore two debiasing techniques, assuming (a) the knowledge of what information users have been exposed to (i.e., systemprovided ratings) prior to making their item consumption choices and (b) varying degrees of knowledge about the bias levels in the user population. As far as we know, this information is not part of any publicly available rating data sets; however, practically, this information is obtainable. Obtaining knowledge (a) is more straightforward, as the system should be able to record the information displayed to users (e.g., the displayed system-predicted rating $P _ { u i }$ for user u and item i). Obtaining knowledge (b) may require specially designed experimental interventions, such as laboratory or field experiments using $\mathrm { A } / \mathrm { B } \cdot$ -testingtype methodology. However, it is clearly feasible; for example, Adomavicius et al. (2013) conducted several randomized controlled experiments to examine and quantify the bias levels of a user population. In this set of experiments, assuming knowledge (a) and (b), we focus on how to debias users’ ratings and how the debiased ratings may improve the system’s predictive performance.

We propose two debiasing techniques, Global and Individual, representing two different scenarios of knowledge (b): (1) when only the average bias level for the entire population is known (denoted as $b i a s _ { g l o b a l } ) .$ , and (2) when the mean bias level for each individual user u is known (denoted as $b i a s _ { u } )$ . These two scenarios illustrate an important tradeoff. On the one hand, the aggregate, population-level bias knowledge $( b i a s _ { g l o b a l } )$ is likely to be more feasible and less costly to estimate than the specific degrees of bias for individual users $( b i a s _ { u } )$ . On the other hand, the more fine-grained, individual-level bias knowledge is likely to lead to better debiasing results.

To operationalize our proposed debiasing strategies, we build upon the preference bias model discussed in Section 3.1 and described by Equation (3). Recall that this model expresses the biased submitted rating $S _ { u i }$ as a function of the user’s true preference $r _ { u i } ,$ systempredicted rating $P _ { u i }$ (observed by the user), and bias level of the user bias (reflecting how much the user is swayed by the system’s rating). Solving Equation (3) for the user’s actual preference $r _ { u i } ,$ we obtain Equations (10) and (11), which employ either the aggregate level of bias across all users $( b i a s _ { g l o b a l } )$ or the specific individual user’s bias level $( b i a s _ { u } )$ as bias estimates, respectively, to debias each submitted rating ${ S _ { u i } } ^ { 9 }$

$$
g l o b a l \_ d e b i a s \_ r _ {u i} = \frac {S _ {u i} - P _ {u i} \cdot b i a s _ {g l o b a l}}{1 - b i a s _ {g l o b a l}}\tag{10}
$$

$$
i n d i v i d u a l \_ d e b i a s \_ r _ {u i} = \frac {S _ {u i} - P _ {u i} \cdot b i a s _ {u}}{1 - b i a s _ {u}}\tag{11}
$$

For our empirical comparisons, using the general procedure in Section 3.1 we simulate four versions of RS, which differ in what happens every time users’ ratings for consumed items are fed back to the system for training: (1) NoBias, where users submit unbiased ratings (i.e., bias is set to be 0 for all users); (2) NoDebias, where users submit biased ratings and no debiasing method is applied; thus, these biased ratings are directly used as future training data; (3) Global, where users submit biased ratings, but these ratings are debiased based on global bias levels (using Equation (10)) before being added back to RS as future training data; and (4) Individual, where users submit biased ratings, but these ratings are debiased based on each individual user’s bias level (using Equation (11)) before being added back to RS as future training data. The first two versions serve as two boundary conditions, and the latter two represent our proposed debiasing techniques.

We evaluate Global and Individual debiasing strategies on the four different user populations introduced at the beginning of Section 6. Recall that these four populations follow the bias distributions $\mathcal { N } ( 0 . 8 , 0 . 2 )$ $\bar { \mathcal { N } } ( 0 . 8 , 0 . 0 5 ) , \mathcal { N } ( 0 . 4 , 0 . 2 )$ , and $\mathcal { N } ( 0 . 4 , 0 . 0 5 )$ , respectively, and represent settings with high versus low average population bias as well as high versus low bias heterogeneity. Figure 7 illustrates the effectiveness of the debiasing methods in enhancing predictive accuracy across the four user populations. Also, in order to illustrate the rating “pollution” in the training data, we compute the difference between (i) each user-submitted rating in the training data set after applying the debiasing method (denoted as $t r a i n _ { u i } )$ and (ii) the corresponding groundtruth rating (denoted as $r _ { u i } )$ , both of which we are fully aware of in our simulation testbed. Thus, for a specific user-submitted rating, difference $( t r a i n _ { u i } - r _ { u i } )$ measures the rating distortion remaining in the training data. Figure 8 uses binned scatterplots to indicate the average trends of such rating differences across different bias levels, for the four user populations. Finally, to show the impact of the proposed debiasing strategies beyond the predictive performance, Figure 9 presents recommendation diversity for the four user populations. Figures 7–9 use an example setting of the ItemKNN recommendation algorithm applied to the Netflix data set;<sup>10</sup> other settings will be discussed below.

Figure 7. (Color online) Predictive Accuracy for User Populations with Different Bias Distributions (Netflix, ItemKNN)  
(a)  
![](/api/attachments/72KZPB3W/fulltext/images/15a924ca4de6688960c4f23b84cc9bab44f065612fa11037925360ecfd123f42.jpg)

(b)  
![](/api/attachments/72KZPB3W/fulltext/images/ae32723e0f784b563ca3600c4f7d7a48ee6563d547a9a20d23ae33ced4a84d19.jpg)

(c)  
![](/api/attachments/72KZPB3W/fulltext/images/cb0fe6dba64375e427017db34c209adf541eb579640e2caae6678c6c8c590107.jpg)

(d)  
![](/api/attachments/72KZPB3W/fulltext/images/fcaaceedd893cef92ea484333304bcc85bece0c43d404163e1ba7f19969ee3ed.jpg)

Figure 8. (Color online) Average Difference between Debiased and Ground-Truth Ratings (Netflix, ItemKNN)  
(a)  
![](/api/attachments/72KZPB3W/fulltext/images/3686e4667ecd2a956630084dc618d8201eedf9333b86250ded576bb8d9a738ee.jpg)

(b)  
![](/api/attachments/72KZPB3W/fulltext/images/021c2d313562740d6c3003fb02059263524fe5368751000106954a6d36704c46.jpg)

(c)  
![](/api/attachments/72KZPB3W/fulltext/images/34c877f2b475cae57e310f8cdfff1f69bca7651b13fabe309e2822fa45e84202.jpg)

(d)  
![](/api/attachments/72KZPB3W/fulltext/images/7e6ce12c145b364491045e9e4b85365c81e98eb680710b76153411b9d5ac97df.jpg)  
Notes. (1) NoBias is not included because user-submitted ratings are equal to ground-truth ratings in this scenario; that is, there is no difference between the two. (2) After 100 iterations of the longitudinal RS simulation, we calculate the differences between every user-submitted rating (after debiasing is applied) and its corresponding nonbiased ground-truth rating. All these data points are then sorted by their corresponding user’s bias level, Bias . For better illustration of the average trends, each dot on the binned scatterplot is the average of every 1,000 data points in the sorted list (i.e., the bin size is 1,000); the x coordinate of each dot is the mean of user bias levels (Bias ) over the 1,000 ratings in a given bin; th y coordinate of each dot represents the average of rating “pollution” $( t r a i n _ { u i } - r _ { u i } )$ over the 1,000 ratings in a given bin.

The computational experiments, represented by Figures 7–9, provide a number of insights about the performance of debiasing techniques. First, consistent with the earlier results of this paper, the populationlevel bias has a major impact on the accuracy performance. When the average bias degree in the population is low (Figure 7, (c) and (d)), the preference bias does not significantly affect recommendation accuracy. This is in stark contrast to populations where the overall bias degree is high (Figure 7, (a) and (b)). This is also directly supported by the rating “pollution” data in Figure 8; that is, the mean trend of $( t r a i n _ { u i } - r _ { u i } )$ for NoDebias is much closer to zero in Figure 8, (c) and (d), than in Figure 8, (a) and (b). And, as shown in Figure 9 (and consistent with prior results), the negative impact of bias on recommendation diversity increases with the average degree of bias in the population, and this impact is already sizeable even for the low-bias populations (Figure 9, (c) and (d)).

Second, compared with NoDebias, both Global and Individual generally provide substantial performance improvements. In terms of accuracy, these improvements naturally are larger for the high-bias populations (Figure 7, (a) and (b)), that is, populations that have more “pollution” to be debiased (as discussed). The insights behind the performance benefits can be gleaned from Figure 8, which shows that the difference $( t r a i n _ { u i } - r _ { u i } )$ of NoDebias is further away from zero, on average, than that of Global and Individual. Notably, both Global and Individual debiasing strategies are able to restore the diversity performance to the levels of unbiased data performance.

Third, contrasting Global versus Individual strategies, Individual consistently exhibits better predictive accuracy. Generally, knowing more granular information about users’ varying degrees of bias (Individual) helps enhance prediction accuracy more than knowing only the aggregate, population-level bias information (Global), and these accuracy advantages are more substantial for the populations with high bias heterogeneity. For instance, predictive performance differences between Global and Individual are larger in Figure 7(a) (higher bias variance in the population) than in Figure 7(b) (lower bias variance). Figure 8, (a) and (b), again provides an explanation—although the remaining rating $\tilde { \mathbf { \Lambda } ^ { \prime \prime } } \mathrm { p o l l u t i o n } \tilde { \mathbf { \Lambda } ^ { \prime \prime } } \left( t r a i n _ { u i } - r _ { u i } \right)$ of both Global and Individual seems to be close to zero on average, the distribution of rating “pollution” is quite different for the two strategies. As shown in Figure 8, (a) and (b), whereas Individual is able to debias ratings consistently across the entire population (that is, “pollution” is close to zero for users across all bias levels), Global is able to do so only for the average user (that is, “pollution” is around zero only for users with bias level 0.8). And, for Global, debiasing is not nearly as accurate for users further away from the average. Thus, predictive performance benefits of Global are more limited in populations with more bias heterogeneity (with more users significantly away from the average), as can be seen by comparing Figure 8, (a) and (b). The simplicity of Global (which requires less granular knowledge about bias in a user population than Individual) also comes with a side effect of overcorrection during debiasing. As shown in Figure 8, for users that have lower-than-average bias, Global (which assumes an average bias for everybody) ends up reducing the rating “pollution” too much, resulting in the negative $( t r a i n _ { u i } - r _ { u i } )$ values, which under some circumstances can possibly even increase the net “pollution” in the system. Finally, although the proposed Global and Individual approaches dramatically outperform the techniques from prior literature (such as HIALF), it is important to point out that even

Figure 9. (Color online) Consumption Diversity for User Populations with Different Bias Distributions (Netflix, ItemKNN)  
(a)  
![](/api/attachments/72KZPB3W/fulltext/images/c2725aa4c2c0d4dd0c00fe59c1292e8d9e9d539e08a6de9ec95a254f1b3ab462.jpg)

(b)  
![](/api/attachments/72KZPB3W/fulltext/images/aa59ba627e8da70557a9e0fcc09e1278918676786bb0c3b775249e31d8d45c80.jpg)

(c)  
![](/api/attachments/72KZPB3W/fulltext/images/0a6361b16af7ee19e8e8e162015dd6c287d93400d137df3858884cee68d62113.jpg)  
+ NoBias NoDebiasGlobal Individual

(d)  
![](/api/attachments/72KZPB3W/fulltext/images/8198d1fa2e18a84f7a749fe11407eaabd54b555d37d3b638a8aaf9ecba64667f.jpg)

Figure 10. (Color online) RMSE for Different Algorithms and Data Sets with User Bias $\mathcal { N }$ (0.8, 0.2)  
![](/api/attachments/72KZPB3W/fulltext/images/5a086fe58756f254320e7f72f8bb44fef550dde1542248393862bee8fd151cde.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/6a872b6c9d524e11b55e79339391b454d9932fc53b44b6b515c634d3d3788ce8.jpg)

![](/api/attachments/72KZPB3W/fulltext/images/07dd2c5d0f6a48777cef278b24c5549f70f8f2d21ba86586cc781005596deeb4.jpg)  
+ NoBias  NoDebias GlobalIndividua

![](/api/attachments/72KZPB3W/fulltext/images/b8be7952326133b0c8bb3c67171f31bd784b4bc309fc862fb59eb4e9acadf2f5.jpg)

Individual cannot fully restore accuracy performance to NoBias levels, because of the noisy nature of individual biasing effects, as discussed (and modeled) at the beginning of Section 6.

To illustrate the performance of the proposed debiasing techniques across multiple settings, Figure 10 reports the prediction accuracy (in RMSE) of two algorithms (ItemKNN and I-AutoRec) and two data sets (Netflix and Yelp) for the population with high average bias and high bias heterogeneity, that is, bias distribution N (0:8, 0:2).<sup>11</sup> Although the specific performance will naturally depend on the characteristics of the given data set and the given algorithm, the key qualitative patterns and insights—for example, the significant impact of preference bias on predictive performance (i.e., difference between NoBias and NoDebias), the improvements of Global and Individual over NoDebias, relative advantages of Individual over Global, and difficulty of achieving per fect debiasing even with Individual—are all consistently reflected across different algorithms and data sets.

The proposed debiasing approaches suggest practical, implementable guidelines for an RS platform to reduce

## Table 6. Prescriptive Steps for Rating Debiasing Process

$$
b i a s _ {e s t}
$$

$$
u,
$$

$$
d e b i a s \_ r _ {u i} = \frac {S _ {u i} - P _ {u i} \cdot b i a s _ {e s t}}{1 - b i a s _ {e s t}}
$$

$$
b i a s _ {e s t}
$$

$$
S _ {u i}
$$

$$
P _ {u i}.
$$

$$
S _ {u i},
$$

$$
\_ r _ {u i}
$$

the impacts of preference biases, and Table 6 summarizes the key prescriptive steps of the proposed framework. Specifically, Step 1 ensures that the data necessary for implementing the proposed debiasing techniques effectively are available (i.e., are being acquired or estimated). Step 2 is the process of debiasing users’ submitted ratings $S _ { u i }$ based on the aforementioned knowledge acquired in Step 1. Step 3 focuses on integrating the debiased ratings into the RS.

## 7. Conclusions

This study focuses on how preference biases affect the longitudinal dynamics of RS’ performance. We summarize the findings of this work and discuss its implications.

## 7.1. Summary of Findings

In this work, through simulation experiments, we show that preference biases caused by a recommendation algorithm’s prediction errors have a substantial adverse effect on the system’s performance when users rely on recommendations. A high preference bias leads to lower recommendation accuracy, relevance, and diversity. The negative effect increases nonlinearly (in an accelerating manner) in the size of the bias. Preference bias leads to inflated submitted ratings for the consumed items, which further inflates the system’s predicted ratings of these items for users who have not consumed them. But only when the bias is large can it create enough inflation on less-liked items and move them up to the top of the recommendation lists, and thus affect users’ consumption choices. We also analyze the different types of items and show that the inflation accumulates on items that are less popular and less distinctive content-wise, which provides important insights into the underlying mechanisms of preference bias propagation in RS.

We further analyze the longitudinal effects of bias for heterogeneous user populations in which users have different levels of preference bias. When half of the users have no bias and the other half have full bias, the overall accuracy and diversity are in between the two homogeneous situations (i.e., no-bias and high-bias populations), but the overall consumption relevance is close to the homogeneous population with no bias. By examining the two user subgroups separately, we observe that, unsurprisingly, the recommendation performance for users with no bias is better on accuracy, relevance, and diversity than for users with high bias. More interestingly, we also observe spillover effects between the two subgroups. With the existence of biased users, unbiased users get slightly less accurate, less diverse, and less relevant recommendations. In comparison, the positive spillover effect from the unbiased group on the biased group is much larger. When there are unbiased users, the biased subgroup’s recommendation gets improved by a significant amount, especially in the actual consumption outcomes as measured by relevance and diversity.

Finally, we explore the problem of debiasing usersubmitted ratings in RS. Using a prevailing approach from prior literature, we empirically demonstrate that relying solely on the standard historical rating data is unlikely to be effective in eliminating preference biases induced by the system’s recommendations. We also propose debiasing methods specifically for removing preference biases by leveraging the additional knowledge about the user population and users’ exposure to recommendations, which demonstrate substantial performance improvements.

## 7.2. Implications of Findings

Our findings have important practical implications for the design of RS. This study establishes and quantifies the substantial longitudinal implications of preference biases. Although the rating inflation (because of preference bias) in each user-submitted rating may be small, we demonstrate how the small biases can snowball over time, leading to long-lasting changes in the system’s performance and users’ consumption outcomes; that is, as users submit their ratings, the bias accumu lates in the system and negatively affects the system’s overall accuracy, relevance, and diversity over time. Our in-depth analyses also provide nuanced insights on how preference bias propagates in the presence of certain types of items and heterogeneous user populations, which provides the system designers important further understanding of RS vulnerabilities in realworld settings. Importantly, our study underscores the importance of reducing preference bias in user ratings, which has not been addressed in prior work. For this purpose, we discuss and analyze the challenges of detecting and removing preference bias, and introduce effective debiasing techniques that recommendation platforms can use for substantial bias reduction.

This work also opens up several promising directions for future research. First, this work focuses on numeric bias in self-reported user ratings induced by the displayed system-predicted ratings. Other displayed information, such as the ranking of recommended items, may interact with preference bias or may lead to different types of biases (e.g., bias in comparative ranking). For example, some systems may incorporate additional information into ranking strategies (e.g., item profitability or popularity) in order to achieve desired outcomes. Therefore, it is important to study how preference bias may accumulate and evolve under different ranking strategies.

Second, further research is needed to examine preference bias in a variety of contexts. We list several possibilities. (1) This study focuses on the context where each user consumes and rates an item at most once. Although this is a common setting in many research studies and real-world systems, further work can expand the setting to allow users to repeatedly consume and rate items, such as in music streaming or in exercise/fitness applications. (2) This study focuses on studying the short-term longitudinal dynamics of userrecommender interactions. Thus, in our setting, each user’s preferences and bias levels are stable; that is, they do not change over time. However, over longer time horizons (say, over several years), users’ preferences can shift, leading to even more complex and nuanced relationships between preference bias and RS performance. Additional research would be needed to study such long-term dynamics and take into account various potential long-term shifts in user behavior— users’ tastes in items, users’ trust in the system, users reliance on recommendations, user’s consumption patterns, items’ availability over time, and so forth—as many of these aspects are unlikely to stay the same over the truly long periods of time. (3) The current study explored the impact of preference bias on users’ explicit numeric ratings. Future research should study preference biases in implicit feedback settings (e.g., where user preferences are reflected by clicks or the dwell time on a web page) and explore the impact of such biases on recommendation performance and consumption outcomes. (4) Quantifying bias levels for a specific recommendation platform is an important input for the proposed debiasing techniques. Prior literature has already suggested some approaches (typically based on field experiments or A/B testing) that can help quantify aggregate bias degrees in a given application (Adomavicius et al. 2013), while also observing that the bias degree can be platform dependent, user dependent, and context dependent. Thus, quantifying bias reliably in specialized recommendation contexts and possibly at even more granular levels (for each item separately, for each individual rating, etc.) is an interesting direction for future research.

Third, this work focuses on studying the dynamics of users’ preference biases that are induced by personalized recommendations; however, in the real world, users may make decisions based on many other factors. For example, to select movies, users may ask friends for recommendations, read movie reviews, watch movie trailers, look at box office performances, etc. Recent research has shown that aggregate ratings lead to similar levels of preference biases as the personalized recommendations (Adomavicius et al. 2022). Other aspects (such as the arrangement of the ratings sorted by date or popularity) may also influence users’ preferences and decisions. A comprehensive investigation and comparison of these different sources of biases constitutes a highly relevant research direction.

Fourth, understanding and improving algorithms robustness to preference bias represents another underexplored research topic. This paper focuses on the key high level performance patterns of preference bias, which are qualitatively similar and consistent across various recom mendation algorithms, whereas the investigation of secondary effects—that is, nuanced, quantitative differences between numerous different algorithms with respect to preference bias—is well beyond the scope of this study. Such differences may depend on a combination of many factors, including the algorithms themselves, characteristics of training data, and parameter settings. Further research is needed to investigate the algorithm-specific implications in the presence of preference bias.

Fifth, in addition to the inherent prediction errors of RS, preference biases can potentially be caused by intentional perturbations of predicted ratings and recommendations external to RS, for example, deliberate promotions/demotions of certain items or third-party attacks (hacks). Such attacks could exacerbate the impact of preference biases on RS performance, and future studies could focus on the unexplored topic of the interplay between external perturbations and preference biases.

Sixth, simulation reflects a simplified version of the real world, and the usefulness of simulation-based methods directly depends on their ability to represent real-world phenomena with a sufficient degree of fidel ity. As detailed in the paper, our agent-based simulation models are based on a set of assumptions and modeling choices capturing most-relevant factors about the environment, users, and the system. However, the assumptions and modeling choices may differ for different recommendation settings, and some additional factors may need to be considered in various specialized recommendation scenarios. Future research may explore additional modeling possibilities in order to generalize our understanding of preference biases beyond the settings of the current study.

Finally, in contrast to the “reactive” approach to debiasing discussed in this paper, an alternative, “proactive” approach would be to develop strategies for preventing preference bias from happening to begin with, that is, ensuring that users submit unbiased ratings. Future work may focus on bias-proof (or bias-aware) user-system interaction designs (e.g., redesigning interfaces for recommendation presentation or rating collection) or properly educating users about preference bias.

## Endnotes

<sup>1</sup> We also conduct a robustness analysis with a different α value (i.e., α � 1:2) in Online Appendix A. Lower α values indicate that users are likely to explore a larger number of top-recommended items, representing a scenario where users are relatively less reliant on the recommender. Specifically, for α � 1:2, the probability of con suming the first recommended item is 16.7%, the second 13.9%, the third 11.6%, and so forth; the probability of consuming one of the top-20 recommendations is around 97%.

<sup>2</sup> Consumption diversity represents the population-level consumption outcomes and is a practically relevant perspective on RS performance (Fleder and Hosanagar 2009). Besides consumption diversity, we have explored two alternative metrics that capture the diversity of top recommendations: (1) aggregate diversity of top-5 recommendations across all users (Adomavicius and Kwon 2014), and (2) indi vidual, list-based diversity of top-5 recommendations (Kunaver and Pozˇrl 2017). We observe similar bias-related patterns across different diversity metrics. Online Appendix B reports the results for the addi tional metrics.

<sup>3</sup> The Yelp data set (from https://www.yelp.com/dataset) contains information from several metropolitan areas. We used data from a single metropolitan area for our simulations.

<sup>4</sup> We explored three deep-learning approaches and chose to include I-AutoRec in our main experiments because of its high prediction accuracy. A comparison of different deep-learning approaches is included in Online Appendix C.

<sup>5</sup> For example, in part because many recommendation techniques explicitly consider the item’s average ratings as a modeling component when making predictions (e.g., Deshpande and Karypis 2004, Koren et al. 2009, Koren 2010).

<sup>6</sup> We have used multiple values for this threshold (from 0.6 to 0.9), and the results are consistent.

<sup>7</sup> We conducted the same analysis on the Yelp data, and the main takeaways are the same.

<sup>8</sup> In many real-world applications, it would not be easily apparent which historical ratings may (or may not) be biased and, thus, need adjustment. However, we have this knowledge in our simulation setting and, therefore, are providing it as an additional (hypothetical) advantage to the HIALF method as a further illustration of debiasing challenges.

<sup>9</sup> When bias is equal or very close to one (i.e., the denominator in Equation (11) is equal or very close to zero), debiasing using bias is impossible or very inaccurate because the submitted rating is (or almost is) equal to the predicted rating; that is, essentially no or very little information about the user’s actual preference is reflected in the submitted rating. Therefore, as part of the Individual debiasing strategy, we explicitly exclude ratings generated by users with extremely high levels of bias (e.g., bias<sub>u</sub> ≥ 0:95) from the RS’s training data; not exclud ing such ratings leads to a decrease in predictive performance. We empirically compared several “exclusion” threshold values, including 0.9, 0.95, and 0.99, and obtained highly consistent results. We chose to use 0.95 for all debiasing experiments reported in the paper.

<sup>10</sup> The results for all metrics (i.e., accuracy, relevance, and diversity) for this setting are in Online Appendix H.

<sup>11</sup> The complete results of all RS performance metrics (i.e., accuracy, relevance, and diversity) are in Online Appendix H.

## References

Abdollahpouri H, Burke R, Mobasher B (2017) Controlling popularity bias in learning-to-rank recommendation. Proc. 11th ACM Conf. on Recommender Systems (Association for Computing Machinery, New York), 42–46.

Abdollahpouri H, Mansoury M, Burke R, Mobasher B (2020) The connection between popularity bias, calibration, and fairness in recommendation. Proc. 14th ACM Conf. on Recommender Systems (Association for Computing Machinery, New York), 726–731.

Adomavicius G, Kwon Y (2014) Optimization-based approaches for maximizing aggregate recommendation diversity. INFORMS J. Comput. 26(2):351–369.

Adomavicius G, Bockstedt J, Curley S, Zhang J (2022) Effects of personalized recommendations vs. aggregate ratings on postconsumption preference responses. Management Inform. Systems Quart. 46(1):627–643.

Adomavicius G, Bockstedt J, Curley SP, Zhang J (2019) Reducing recommender system biases: An investigation of rating display designs. Management Inform. Systems Quart. 43(4):1321–1341.

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2013) Do recom mender systems manipulate consumer preferences? A study of anchoring effects. Inform. Systems Res. 24(4):956–975.

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2018) Effects of online recommendations on consumers’ willingness to pay. Inform. Systems Res. 29(1):84–102.

Amatriain X, Pujol JM, Oliver N (2009) I like it … I like it not: Evaluating user ratings noise in recommender systems. Houben GJ, McCalla G, Pianesi F, Zancanaro M, eds. Internat. Conf. on User Modeling, Adaptation, and Personalization (Springer, Berlin), 247–258.

Baeza-Yates R (2018) Bias on the web. Commun. ACM 61(6):54–61.

Bennett J, Lanning S (2007) The Netflix prize. Proc. KDD Cup and Workshop 2007 (Association for Computing Machinery, New York), 35.

Casey BM, McIntire DD, Leveno KJ (2001) The continuing value of the Apgar score for the assessment of newborn infants. N. Engl. J. Med. 344(7):467–471.

Chaney AJ, Stewart BM, Engelhardt BE (2018) How algorithmic confounding in recommendation systems increases homogeneity and decreases utility. Proc. 12th ACM Conf. on Recommende Systems (Association for Computing Machinery, New York), 224–232.

Chen J, Dong H, Wang X, Feng F, Wang M, He X (2020) Bias and debias in recommender system: A survey and future directions. Preprint, submitted October 7, https://arxiv.org/abs/2010.03240.

Collins A, Tkaczyk D, Aizawa A, Beel J (2018) Position bias in recommender systems for digital libraries. Internat. Conf. on Inform. (Springer, Cham, Switzerland), 335–344.

Cosley D, Lam SK, Albert I, Konstan JA, Riedl J (2003) Is seeing believing? How recommender system interfaces affect users’ opinions. Proc. SIGCHI Conf. on Human Factors in Comput. Systems (Association fo Computing Machinery, New York), 585–592.

Cremonesi P, Koren Y, Turrin R (2010) Performance of recommender algorithms on top-n recommendation tasks. Proc. Fourth ACM Conf. on Recommender Systems (Association for Computing Machin ery, New York), 39–46.

Davidson J, Liebald B, Liu J, Nandy P, Van Vleet T, Gargi U, Gupta S, et al. (2010) The YouTube video recommendation system. Proc. Fourth ACM Conf. on Recommender Systems (Association for Com puting Machinery, New York), 293–296.

De P, Hu Y, Rahman MS (2010) Technology usage and online sales: An empirical study. Management Sci. 56(11):1930–1945.

Dean B (2022) We analyzed 4 million Google search results. Accessed March 1, 2023, https://backlinko.com/google-ctr-stats.

Deshpande M, Karypis G (2004) Item-based top-n recommendation ACM Trans. Inform. Systems

Ekstrand MD, Burke R, Diaz F (2019) Fairness and discrimination in recommendation and retrieval. Proc. 13th ACM Conf. on Recommender Systems (Association for Computing Machinery, New York), 576–577.

Ferraro A, Jannach D, Serra X (2020) Exploring longitudinal effects of session-based recommendations. Proc. 14th ACM Conf. on Recommender Systems (Association for Computing Machinery, New York), 474–479

Flaxman S, Goel S, Rao JM (2016) Filter bubbles, echo chambers, and online news consumption, Public Opin, Ouart, 80(S1):298–320

Fleder D, Hosanagar K (2009) Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Man agement Sci. 55(5):697–712.

Funk S (2006) Netflix update: Try this at home. Accessed October 10, 2020, https://sifter.org/\~simon/journal/20061211.html.

Gao R, Shah C (2020) Counteracting bias and increasing fairness in search and recommender systems. Proc. 14th ACM Conf. on Rec ommender Systems (Association for Computing Machinery, New York), 745–747.

Ge Y, Zhao S, Zhou H, Pei C, Sun F, Ou W, Zhang Y (2020) Understanding echo chambers in e-commerce recommender systems. Proc. 43rd Internat. ACM SIGIR Conf. (Association for Comput ing Machinery, New York), 2261–2270.

Gomez-Uribe CA, Hunt N (2015) The Netflix recommender system: Algorithms, business value, and innovation. ACM Trans. Man agement Inform. Systems 6(4):1–19.

Hale J (2021) Tiktok’s recommendation algorithm is even more powerful—and potentially dangerous—than YouTube’s. Accessed March 1, 2023, https://www.tubefilter.com/2021/07/21/tiktokrecommendation-algorithm-wall-street-journal-guillaume-chaslot/.

Hofmann K, Schuth A, Bellogin A, de Rijke M (2014) Effects of posi tion bias on click-based recommender evaluation. European Conf. on Inform. Retrieval (Springer, Berlin), 624–630.

Ja¨rvelin K, Keka¨la¨inen J (2017) IR evaluation methods for retrieving highly relevant documents. ACM SIGIR Forum 51(2):243–250.

Karypis G (2001) Evaluation of item-based top-N recommendation algorithms. Proc. Tenth Internat. Conf. on Inform. and Knowledge Management (Association for Computing Machinery, New York), 247–254.

Koren Y (2008) Factorization meets the neighborhood: A multifaceted collaborative filtering model. Proc. 14th ACM SIGKDD Internat. Conf. on Knowledge Discovery and Data Mining (Association for Computing Machinery, New York), 426–434.

Koren Y (2010) Factor in the neighbors: Scalable and accurate collaborative filtering. ACM Trans. Knowledge Discov. Data 4(1):1–24.

Koren Y, Bell R, Volinsky C (2009) Matrix factorization techniques for recommender systems. Computer 42(8):30–37.

Kunaver M, Pozˇrl T (2017) Diversity in recommender systems—A survey. Knowledge-Based Systems 123:154–162.

Larrick RP (2004) Debiasing. Koehler DJ, Harvey N, eds. Blackwell Handbook of Judgment and Decision Making (Blackwell Publishing Ltd, Oxford, UK), 316–337.

Lee D, Hosanagar K (2019) How do recommender systems affect sales diversity? A cross-category investigation via randomized field experiment. Inform. Systems Res. 30(1):239–259.

Leonard D (2016) Spotify is perfecting the art of the playlist. Accessed October 27, 2023, https://www.bloomberg.com/news/articles 2016-09-21/spotify-is-perfecting-the-art-of-the-playlist.

Marshall M (2006) Aggregate knowledge raises \$5m from Kleiner, on a roll. Accessed October 10, 2020, https://venturebeat.com/2006 12/10/aggregate-knowledge-raises-5m-from-kleiner-on-a-roll/.

Pariser E (2011) The Filter Bubble: How the New Personalized Web Is Changing What We Read and How We Think (Penguin Press, New York).

Prawesh S, Padmanabhan B (2014) The “most popular news” recommender: Count amplification and manipulation resistance. Inform. Systems Res. 25(3):569–589.

Ricci F, Rokach L, Shapira B (2010) Introduction to recommender systems handbook. Ricci F, Rokach L, Shapira B, Kantor P, eds Recommender Systems Handbook (Springer, Boston), 1–35.

Sarwar B, Karypis G, Konstan J, Riedl J (2001) Item-based collaborative filtering recommendation algorithms. Proc. 10th Internat. Conf. on World Wide Web (Association for Computing Machinery, New York), 285–295

Sedhain S, Menon AK, Sanner S, Xie L (2015) Autorec: Autoencoders meet collaborative filtering. Proc. 24th Internat. Conf. on World Wide Web (Association for Computing Machinery, New York), 111–112.

Senecal S, Nantel J (2004) The influence of online product recommen dations on consumers’ online choices. J. Retailing 80(2):159–169.

Sinha A, Gleich DF, Ramani K (2016) Deconvolving feedback loops in recommender systems. Lee DD, Sugiyama M, Luxburg Uv, Guyon I, Garnett R, eds. Adv. Neural Inform. Processing Systems (NeurIPS, Barcelona, Spain), 3243–3251.

Soll JB, Milkman KL, Payne JW (2015) A user’s guide to debiasing. Keren G, Wu G, eds. The Wiley Blackwell Handbook of Judgment and Decision Making, vol. II (John Wiley & Sons, Ltd, Chichester UK), 924–951.

Steck H (2011) Item popularity and recommendation accuracy. Proc. Fifth ACM Conf. on Recommender Systems (Association for Com puting Machinery, New York), 125–132.

Sun W, Khenissi S, Nasraoui O, Shafto P (2019) Debiasing the human-recommender system feedback loop in collaborative filtering. Proc. 2019 World Wide Web Conf. (Association for Com puting Machinery, New York), 645–651.

Theocharous G, Thomas PS, Ghavamzadeh M (2015) Personalized ad recommendation systems for life-time value optimization with guarantees. Proc. 24th Internat. Joint Conf. on Artificial Intelligence (AAAI Press, Washington, DC), 1806–1812.

Wang T, Wang D, Wang F (2014) Quantifying herding effects in crowd wisdom. Proc. 20th ACM SIGKDD Internat. Conf. on Knowledge Discovery and Data Mining (Association for Comput ing Machinery, New York), 1087–1096.

Zeng C, Wang Q, Mokhtari S, Li T (2016) Online context-aware recommendation with time varying multi-armed bandit. Proc. 22nd ACM Internat. Conf. on Knowledge Discovery and Data Mining (Association for Computing Machinery, New York), 2025–2034.

Zhang J, Adomavicius G, Gupta A, Ketter W (2020) Consumption and performance: Understanding longitudinal dynamics of recommender systems via an agent-based simulation framework. Inform. Systems Res. 31(1):76–101.

Zhang X, Xie H, Zhao J, Lui JC (2019) Understanding assimilationcontrast effects in online rating systems: Modelling, debiasing, and applications. ACM Trans. Inform. Systems 38(1):1–25.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
