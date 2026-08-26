---
otero_id: 4342
otero_key: "SEZJ6KQZ"
title: "Examining Solver Performance in Crowdsourcing Contests: Does Ambidexterity Matter?"
authors: "Hua (Jonathan) Ye; Atreyi Kankanhalli; Bernard C. Y. Tan"
year: "2025"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00932"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2025

# Examining Solv er Performance in Cr   owdsour cing Contests: Does Ambidexterity Matter?

Hua (Jonathan) Ye , jonathan.ye@ou.edu

Atreyi Kankanhalli , atreyi@comp.nus.edu.sg

Bernard C. Y. Tan , btan@comp.nus.edu.sg

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Examining Solver Performance in Crowdsourcing Contests: Does Ambidexterity Matter?

Hua (Jonathan) Ye,<sup>1</sup> Atreyi Kankanhalli,<sup>2</sup> Bernard C. Y. Tan<sup>3</sup>

<sup>1</sup>University of Oklahoma, USA, Jonathan.ye@ou.edu <sup>2</sup> National University of Singapore, Singapore, atreyi@comp.nus.edu.sg <sup>3</sup>National University of Singapore, Singapore, btan@comp.nus.edu.sg

## Abstract

The performance of solvers is crucial to the success of crowdsourcing contest platforms. Sustained solver performance entails a combination of exploration and exploitation activities, i.e., solver ambidexterity. However, it can be arduous for solvers to engage in ambidexterity with limited knowledge of what its optimal levels are and little research informing this topic. Thus, this study examines the relationship between solver ambidexterity and performance, which is stated to be positive for workers in organizational research. We challenge this assumption and propose that the costs associated with ambidexterity will limit its efficacy beyond a certain level—i.e., we hypothesize an inverted U-shaped relationship between ambidexterity and solver performance. Moreover, how contest conditions shape this relationship is unclear. Drawing on the bounded rationality model, we hypothesize three moderators of the relationship, i.e., task reward, task diversity, and in-process feedback. We tested our model using a panel dataset of solvers from a major crowdsourcing contest platform. Our results support the inverted U-shaped relationship between solvers’ ambidexterity and performance. We find that the highest-performing solver cluster showed a ratio of 5.33 exploitation activities to 1 exploration activity, contradicting the prior premise that both activities are required to a similar extent. Additionally, task diversity and task reward are found to steepen the inverted U curve, while in-process feedback flattens the curve. Our study contributes to theoretical knowledge of the relationship between solvers’ ambidexterity and performance and its contingent conditions. The results also offer novel insights for solvers and platforms to manage ambidexterity and the trade-offs between exploration and exploitation.

Keywords: Crowdsourcing Contest, Solver Performance, Individual Ambidexterity, Bounded Rationality, Task Reward, Task Diversity, In-Process Feedback

Zhijie Lin was the accepting senior editor. This research article was submitted on January 10, 2024, and underwent two revisions.

## 1 Introduction

Crowdsourcing contests have gained traction as a popular form of work, where a crowd of solvers perform a variety of tasks for seeker firms (Jiang et al., 2022; Jin et al., 2021). Crowdsourcing platforms such as CrowdSpring, and Zhubajie host contests for tasks like graphic design, programming, and marketing, serving as virtual intermediaries between solvers and seekers (Boudreau et al., 2016; Jiang & Wang, 2020; Mo et al., 2018). Through such contests, seekers gain access to external expertise, aiming to save costs and obtain high-quality solutions (Nevo & Kotlarsky, 2020; Ye & Kankanhalli, 2015). However, the value of crowdsourcing contests is undermined by poor solver performance (Afuah & Tucci, 2012; Ye & Jensen, 2022). For instance, platforms like

99designs frequently receive generic and stock designs for websites and logos that do not satisfy seekers’ preferences (Attebery, 2017). Low-quality solutions deter seeker firms from posting tasks (Blohm et al., 2013) and have resulted in platform failures (Fixson & Marion, 2016).

Particularly, workers’ performance can suffer from an overreliance on exploiting existing knowledge rather than exploring new knowledge (Papanastasiou et al., 2018). Solvers often default to familiar approaches and solutions, thus restricting their ability to generate innovative outcomes (Althuizen & Chen, 2022; Hofstetter et al., 2021). This presents a crucial challenge to pursuing a combination of exploration and exploitation activities, i.e., ambidexterity, which is proposed as a key driver of performance (Gibson & Birkinshaw, 2004). Here, exploitation refers to solvers searching their existing knowledge base for contest solutions, whereas exploration involves seeking new knowledge to derive solutions (Schnellbächer et al., 2019). Ambidexterity entails difficult choices between time spent exploiting existing skills for task-solving versus exploring and developing new skills. The choices can determine solvers’ gains in crowdsourcing contests, as well as the quality of solutions on these platforms. The dilemma leads to questions regarding what the optimal level of solver ambidexterity is and how ambidexterity influences solvers’ performance.

Looking at prior literature, organizational studies suggest that ambidexterity has a positive linear effect on performance for individual employees and managers in various organizational contexts (Schnellbächer et al., 2019), including service and manufacturing firms (Mom et al., 2015). However, there is reason to believe that the costs associated with ambidexterity will limit its efficacy (Keller & Weibler, 2015; Roberts et al., 2021; Schnellbächer et al., 2019). People tend to focus on either exploration or exploitation activities, since deliberately switching between the activities incurs cognitive costs (Smith & Tushman, 2005). Such costs increase rapidly at higher levels of ambidexterity (Kiss et al., 2020; Roberts et al., 2021), resulting in cognitive strain (Kc, 2014). This poses an intellectual puzzle to understand the limits of ambidexterity. Our work challenges the assumption of a continued positive influence of ambidexterity on performance and aims to examine these limits.

Furthermore, the optimal level and proportion of exploration and exploitation for superior performance is unclear and can vary by context (Luger et al., 2018). Examining the optimal ratio of the two activities can extend the understanding of how to orchestrate ambidexterity for crowdsourcing and help solvers better allocate their time and resources in undertaking exploration and exploitation activities. Moreover, the relationship between ambidexterity and performance depends on the contextual characteristics of contest tasks (Puranam et al., 2015), which influence the contest solution process and the efficacy of ambidexterity.

Studying these boundary conditions of ambidexterity theory can inform related research and extend the applicability of this lens.

Driven by these knowledge gaps, we theorize and empirically test the relationship between ambidexterity and solver performance, as well as the moderating influence of contextual characteristics. We examine two research questions: (1) How does ambidexterity influence solver performance? and (2) How do contextual characteristics moderate the relationship between ambidexterity and solver performance?

To address the first question, we build on individual ambidexterity concepts to hypothesize an inverted Ushaped relationship between ambidexterity and solver performance. Regarding the second question, we identify specific task characteristics of crowdsourcing contests that influence the efficacy of solver ambidexterity (Birkinshaw & Gupta, 2013; Luger et al., 2018) drawing on the bounded rationality model (Birkinshaw & Gupta, 2013; Luger et al., 2018; Puranam et al., 2015). As we elaborate in the next section, the task environment as per the bounded rationality model can be represented by task diversity, task reward, and in-process feedback. In particular, the task diversity of contest tasks represents the search space for solvers to choose solutions and switch between exploration and exploitation activities. The task reward of contest tasks reflects the incentive for solvers to close the gap between optimal and satisficing choices and determines the search effort of the choice process. The feedback element of the bounded rationality model corresponds to the in-process feedback provided by seekers to solvers during contests on crowdsourcing platforms. We theorize how these contextual characteristics influence the efficacy of and switching costs between exploration and exploitation activities for solver performance. In other words, task diversity, task reward, and in-process feedback serve as moderators of the ambidexterity—solver performance relationship.

To test our model, we analyzed panel archival data collected from 6018 solvers over 12 months from a large crowdsourcing contest platform. We found empirical support for the inverted U-shaped relationship between ambidexterity and solver performance. We also performed cluster analysis of the solvers and found that the highest-performing solver cluster showed a ratio of 5.33 exploitation activities to 1 exploration activity. Moreover, task diversity and task reward positively moderated the inverted U-shaped relationship, i.e., steepened the curve of ambidexterity on performance. In contrast, in-process feedback exhibited a negative moderating relationship, i.e., flattened the curve.

Our study makes several important research contributions. First, it enriches our understanding of solver activities—i.e., the combination and trade-offs of exploration and exploitation—for optimal performance in crowdsourcing contests using the lens of ambidexterity.

This contributes to the body of research on solver performance in crowdsourcing (Bockstedt et al., 2016; Menon et al., 2020). Second, it adds to the IS and ambidexterity literatures (Liang et al., 2022; Mom et al., 2019) by demonstrating the inverted U-shaped relationship between ambidexterity and solver performance, departing from the earlier reported linear effects. This study further advances the literature by informing about the ratio of exploration to exploitation activities undertaken by high-performing solver groups in our study context.

Additionally, our work responds to calls for research on ambidexterity in non-organizational contexts (Pertusa-Ortega et al., 2020) by examining its role in crowdsourcing contests. We identify key moderators of the ambidexterity-performance relationship for solvers in crowdsourcing contests. This deepens our understanding of the boundary conditions of this relationship, and addresses calls for research about such contextual moderators (Schnellbächer et al., 2019). Our results inform solvers on how to manage their exploration and exploitation activities as well as crowdsourcing platforms on how to leverage solver ambidexterity for superior performance. We discuss the broader implications of our study for workers in general and for online platforms.

The paper proceeds as follows. The next section reviews related research on crowdsourcing and introduces the theoretical foundations of our study, i.e., individual ambidexterity and bounded rationality. Subsequently, we develop our hypotheses, describe the methodology, and present the study results. We conclude the paper by discussing its theoretical and practical contributions and outlining avenues for future research.

## 2 Conceptual Background

Two broad types of crowdsourcing have been highlighted in the literature, i.e., contest-based and non-contest-based crowdsourcing (Prpić et al., 2015; Schenk & Guittard, 2011). Contest-based crowdsourcing (also called tournament-based or selective crowdsourcing) uses a competition format to solicit, select, and reward the best performance from the crowd (Zhang et al., 2019). Exemplar platforms include TopCoder and Kaggle, where complex tasks are offered to the crowd, requiring specialized skills. Non-contest-based crowdsourcing involves open collaboration or integration of inputs from crowd members with or without rewards e.g., Wikipedia (Prpić et al., 2015; Schenk & Guittard, 2011). Another related concept is crowdwork (Durward et al., 2020), also referred to as microtask crowdsourcing or online labor markets (Prpić et al., 2015). Crowdwork involves digitally processible tasks being outsourced as paid work to a global workforce via internet platforms such as Amazon Mechanical Turk and Upwork (Pongratz, 2018). Crowdwork tasks are simple and do not require specialized skills e.g., filling out academic surveys, image tagging, and posting marketing messages on social media (Deng et al., 2016). Since our focus is on solver performance in crowdsourcing contests, we do not include other forms of crowdsourcing and crowdwork in our study. Particularly, there is a large body of crowdsourcing research <sup>1</sup> , including studies on solver participation in different types of crowdsourcing and their associated motivations (Bayus, 2013; Deng et al., 2016; Ye & Kankanhalli, 2015). Instead, proximate to our work, we review research on solver performance in crowdsourcing contests (Piezunka & Dahlander, 2015).

## 2.1 Related Research on the Antecedents of Solver Performance

Related research on the antecedents of solver performance can be classified into two major streams (see Table A1, Appendix A for a review of such empirical research). The first stream has examined solver-related antecedents of their performance in crowdsourcing contests. These studies explored the performance impacts of solvers’ number of contests participated before (Archak & Ghose, 2010; Bockstedt et al., 2016; Riedl & Seidel, 2018), their participation in task forums (Ye & Jensen, 2022), and in rating (Riedl & Seidel, 2018), and commenting on others’ work (Bayus, 2013), which were mainly positive. Other work in this stream has studied the effects of solver multi-tasking, i.e., the number of concurrent tasks (Mo et al., 2021), technical and social marginality e.g., gender (Jeppesen & Lakhani, 2010), and that of upstream/downstream experience on solver performance (Menon et al., 2020).

While we see myriad solver characteristics being studied, this stream of research falls short of examining the combined impacts of solvers’ exploration and exploitation activities and the trade-offs between them. At the same time, prior work (Bockstedt et al., 2016; Menon et al., 2020) has suggested that pursuing both exploration and exploitation activities is beneficial for solver performance. Yet the effects of doing so have not been explored, resulting in a lack of understanding of the interplay between these two fundamental solver activities and their influence on solver performance.

The second stream of related research has focused on the effects of contest task characteristics on solver outcomes. This includes examining the direct effects of task reward (Liu et al., 2014), task rivalry or competition intensity (Boudreau et al., 2016; Boudreau et al., 2011), task variety (Martinez, 2015), and seeker feedback (Jian et al.,

2019; Jiang & Wang, 2020; Jiang et al., 2022) on solver performance. Other studies in this stream have explored the effects of contest task characteristics on solver participation intention (Martinez, 2017), crowd size (Liu et al., 2021), and actual participation (Ye & Kankanhalli, 2017). This body of work has also identified other antecedents of these solver outcomes, such as perceptions of task autonomy (Martinez, 2017), significance, and clarity (Liu et al., 2021; Ta et al., 2021). Nevertheless, this stream lacks investigation of how such contest task characteristics might interact with ambidexterity in influencing solver performance.

Several of these studies (e.g., Liu et al., 2021; Ta et al., 2021) have suggested that contextual task characteristics moderate the effects of other antecedents on solver performance. However, prior research has stopped short of identifying, theorizing, and testing the moderating effects of these characteristics. Thus, critical questions regarding the task-related boundary conditions of the relationship between ambidexterity and solver performance remain unaddressed. We draw on the individual ambidexterity view and bounded rationality model to address the above questions.

## 2.2 Individual Ambidexterity

Individual ambidexterity refers to the behavioral ability of a person to pursue a combination of exploration and exploitation activities over a period of time (Mom et al., 2009; Tempelaar & Rosenkranz, 2019). <sup>2</sup> Though originally conceptualized at the organizational level, ambidexterity originates in the behaviors of individuals e.g., managers and employees (Birkinshaw & Gibson, 2004; Mom et al., 2007). People exhibit ambidexterity by exploring novel knowledge and exploiting existing knowledge in their tasks (Schnellbächer et al., 2019). Exploitation happens when individuals apply their prior knowledge base to current tasks (Mom et al., 2007; Tempelaar & Rosenkranz, 2019). Through exploitation, they utilize existing schemas and templates, which are cognitive structures in their knowledge base (Sweller, 1988). On the other hand, exploration occurs when individuals search for novel ideas, technologies, paradigms, and knowledge to find ways to tackle tasks. Exploration activities extend the extant schemas and competencies of individuals by availing new opportunities, experimenting with new concepts, and developing new schemas (Mom et al., 2009; Schnellbächer et al., 2019).

Though prior work has primarily examined individual ambidexterity for managers or employees in organizational contexts (Kobarg et al., 2017; Mom et al., 2019; Mom et al., 2015; Schnellbächer et al., 2019), we argue that ambidexterity is also important for workers in extra-organizational settings, such as solvers in crowdsourcing contests. Solvers may engage in both exploration and exploitation activities to tackle contest tasks. On the one hand, solvers can exploit knowledge gained from prior experiences to address current tasks (Ye & Jensen, 2022). For example, in TopCoder, solvers were found to exploit their knowledge and skills of particular programming languages for subsequent coding contests (Archak & Ghose, 2010). Indeed, crowdsourcing contest platforms often encourage solvers to exploit their past experience by recommending tasks that are similar to those that they have previously participated in and won (Mo et al., 2018). On the other hand, solvers can explore new knowledge by observing the work of others (Martinez, 2015), participating in discussion forums, and searching elsewhere (Ye & Jensen, 2022). For instance, platforms like Zhubajie.com allow solvers to view the winning solutions of others and their successful experiences shared in the discussion forum (Feng et al., 2018). Thus, while both exploration and exploitation are undertaken by solvers, the performance effects of pursuing them jointly (i.e., ambidexterity) remain unexplored.

The ambidexterity perspective suggests that independent of their direct impacts, attaining high levels of both exploitation and exploration activities is important for superior performance (Cao et al., 2009). The earlier balance logic posits that both activities need to be undertaken to similar extents. However, such balance could result from low levels of both exploration and exploitation activities, which would not enhance performance (He & Wong, 2004). Thus, the current combination logic posits that ambidexterity requires high levels of both exploration and exploitation (Mom et al., 2015; Smith & Tushman, 2005) while maintaining a balance between the two activities (Cao et al., 2009). This implies that ambidexterity involves conducting high levels of exploitation and exploration activities in a balanced manner so that individuals can achieve their synergistic benefits (Smith & Tushman, 2005).

Nevertheless, pursuing such ambidexterity entails costs and effort (Schnellbächer et al., 2019). Balancing high levels of exploration and exploitation activities is arduous, with prior studies highlighting the tensions involved (e.g., Kobarg et al., 2017; Laureiro‐Martínez et al., 2015). Research on organizational ambidexterity has proposed three approaches to reconcile both activities, i.e., sequential, structural, and contextual & Tushman, 2013). Sequential ambidexterity involves periods of exploration activities alternating with periods of exploitation activities. Structural ambidexterity is an approach where exploration and exploitation activities are pursued simultaneously—but by separate individuals or groups, such as different business units. Contextual ambidexterity entails pursuing exploration and exploitation activities simultaneously and internally, which typically requires organizations to foster it (Raisch & Birkinshaw, 2008). Since structural and contextual ambidexterity apply more to organizations, prior literature largely maintains that sequential ambidexterity best represents individual ambidexterity (Pertusa-Ortega et al., 2020). However, individuals tend to be biased towards one of these activities and often struggle to achieve synergies between both (Smith & Tushman, 2005). Particularly as the level of the two activities increases, it becomes arduous to balance and switch between them (Smith & Tushman, 2005). Thus, we argue that there is a limit to improving performance through ambidexterity. However, the limit of ambidexterity effects has not been theorized and tested, with prior studies mainly reporting its positive impacts on performance (Pertusa-Ortega et al., 2020).

Further, there is little understanding of the conditions that shape the relationship between ambidexterity and performance outside of organizational settings (Pertusa-Ortega et al., 2020). To address our second research question, we draw on the bounded rationality model to identify the contextual conditions (Luger et al., 2018; Posen & Levinthal, 2012) that determine how the combination of exploration and exploitation influences solver performance.

## 2.3 Bounded Rationality Model and Contextual Moderators

The bounded rationality model explains satisficing behavior and has been found to realistically describe human behavior and decision-making (Simon, 1972). A stream of ambidexterity literature has built on the bounded rationality model, highlighting the tension between exploration and exploitation activities and indicating that ambidexterity is extremely hard to achieve (Birkinshaw & Gupta, 2013; March, 1991). When applied to ambidexterity, the model distinguishes between exploratory choices, exploitative choices, and feedback from those choices. There are several basic elements of this model, i.e., the task environment and its representation, the choice process, and transformation (Puranam et al., 2015). The task environment captures the possible courses of action available to a human agent (e.g., exploration or exploitation), and the likelihood of attaining the desired goal of the agent for each course of action. These are represented through the agent’s beliefs about the task environment. The choice process refers to the procedure by which the agent chooses an action (exploration or exploitation) given the representation. Each choice garners feedback from the task environment depending on the gap between the desirable and current performance (Luger et al., 2018). The feedback triggers the transformation, which can result in a modification of representations and possibly choice processes.

In crowdsourcing contests, solvers can voluntarily choose contest tasks to work on, instead of being assigned tasks, as in organizational contexts (Martinez, 2015). Task diversity refers to the range of task types that the solver selects to participate in (Bayus, 2013). In this sense, it corresponds to the task environment and its representation in the solver’s mind as per the bounded rationality model. Task diversity reflects the search space in the choice process as solvers can choose different contest tasks (Zheng et al., 2011) that require exploration or exploitation activities to complete. Task reward (contest prize amount) refers to the incentive to attain a desirable performance outcome in the task environment. It reflects the amount of effort in the choice process (in terms of exploration and exploitation) needed to close the gap between optimal and satisficing performance. Inprocess feedback refers to the feedback that seeker firms provide to solvers that may lead them to revise their solutions (Jian et al., 2019; Jiang & Wang, 2020). In this sense, such feedback corresponds to the relative search success and can trigger solvers’ behavior transformation to satisfy seeker requirements. Thus, we identify task diversity, task reward, and in-process feedback as contextual characteristics that could influence the efficacy of the choice process (exploration versus exploitation) and moderate the relationship between ambidexterity and solver performance. We draw on the above two theories (ambidexterity and bounded rationality) to build our research model.

## 3 Research Model and Hypotheses

With the above foundations, we hypothesize the relationship between ambidexterity and solver performance, which refers to a solver’s number of winning submissions on the crowdsourcing platform in a time period. Additionally, we propose moderating effects of task diversity, task reward, and in-process feedback.

## 3.1 Solver Ambidexterity

In our study, ambidexterity refers to the extent to which a solver performs both exploration and exploitation activities over a period of time for participating in crowdsourcing contests (adapting from Mom et al., 2009). It is measured by the multiplication of the frequencies of the two types of activities (Liang et al., 2022; Mom et al., 2015).

When exploration and exploitation activities are carried out at low levels, solvers exhibit low ambidexterity. As solvers are utilizing their own knowledge base or searching for new knowledge to a limited extent, their performance would be low under these conditions. But as the levels of exploration and exploitation activities increase, solvers can reap the direct benefits of efficiency increase from exploitation activities and effectiveness increase from exploration activities (Mom et al., 2015). Solvers could also garner synergistic benefits from ambidexterity. Synergy arises when new knowledge gained from exploration is used to unlock the potential of existing knowledge and create new capabilities (Cao et al., 2009). Likewise, existing knowledge guides the pursuit of new knowledge, making the acquisition of new knowledge more efficient (Jansen et al., 2012). This integration of new knowledge with existing knowledge can lead to novel solutions for tasks (Nijstad et al., 2010) such as designing a logo for a contest drawing on past experience with brand identity design and new knowledge of image editing.

Yet we argue that such benefits from individual ambidexterity would taper off and hit a plateau. As ambidexterity (pursuing more exploration and exploitation) continues to increase, bounded rationality would kick in and place limits on an individual’s willingness and ability to process more information (Simon, 1972). In response, solvers would typically satisfice rather than persist when making decisions and developing solutions (Roberts et al., 2021). Thus, we propose that the benefits of solver ambidexterity eventually level off (see Figure 1a). Additionally, switching between and balancing high levels of exploration and exploitation incurs significant cognitive costs (Laureiro‐Martínez et al., 2015; Mom et al., 2009). Switching costs include acquainting oneself with the requirements of new tasks, i.e., cognitive setup costs, and thoughts about previous tasks lingering in the new tasks, i.e., attention residue costs (Leroy & Glomb, 2018; Staats & Gino, 2012). Those costs increase rapidly with higher levels of ambidexterity, i.e., frequent switching (see Figure 1b).

As switching costs increase beyond a certain point, solvers would experience cognitive overload due to the limits in cognitive capacity (Colicev et al., 2023; Kc, 2014). This would prevent them from reaping any synergistic benefits, i.e., they would be unable to use the novel knowledge acquired from exploration activities or unlock the current knowledge available from exploitation activities for completing contest tasks (Smith & Tushman, 2005). This results in a deterioration in solver performance, which can be seen as the outcome of combining a saturating benefit function (Figure 1a) with an exponentially increasing cost function (Figure 1b)

(Haans et al., 2016). The combined effect is an inverted U-shaped relationship between ambidexterity and performance (see Figure 1c). Thus, we hypothesize:

H1: Ambidexterity has an inverted U-shaped relationship with solver performance.

## 3.2 Task Diversity

In our study, task diversity refers to the extent to which solvers have undertaken different types of tasks (adapting from Bayus, 2013). Performance of different types of tasks exposes solvers to heterogeneous knowledge and skills (Boone & Hendriks, 2009; Heavey & Simsek, 2017), which has been linked to learning (Sweller, 1988), creativity (Martinez, 2015), and crowdsourcing performance (Bayus, 2013; Cheng et al., 2020; Ye & Jensen, 2022). We do not hypothesize the direct effect of task diversity on solver performance, which has already been reported, but focus on its moderating effect here.

When task diversity is high, this implies that solvers would have acquired a variety of skills from past tasks (Martinez, 2015) e.g., website design, creating apps, and marketing videos. As per the bounded rationality model, task diversity offers a wider search space for the choice processes (Luger et al., 2018; Posen & Levinthal, 2012). It can strengthen ambidexterity’s effect because it adds to the efficacy of the choice processes (Puranam et al., 2015). Thus, we expect that task diversity will steepen the benefit curve of ambidexterity (see Figure 2a).

At the same time, having diverse task experience (task diversity) could reduce solvers’ switching costs. Switching between tasks requires handling the setup costs of the new task (Kc, 2014). Task diversity provides individuals with better schemas for approaching new tasks, reducing cognitive setup costs (Staats & Gino, 2012). Also, as per the bounded rationality model, it helps individuals recognize the threats or risks hidden in a complex task environment (Ossenbrink et al., 2019) and avoid potential costs. Applied to our setting, task diversity should help solvers mitigate the increase in switching costs as their ambidexterity increases (see Figure 2b).

(a)  
![](/api/attachments/SEZJ6KQZ/fulltext/images/d51f8f0f4b28c101e3e11defa107854227c9139d8e644357441a8141d7889fc3.jpg)

(b)  
![](/api/attachments/SEZJ6KQZ/fulltext/images/7824bbacbe34ffffbe0d3fee030163e1a36a0a2e2b4452d128ea5244bb4a6c4f.jpg)

(c)  
![](/api/attachments/SEZJ6KQZ/fulltext/images/f0ce444309da0015392624de1d843bd2a262615f35d08bf078a2997a6d47d1d2.jpg)  
Figure 1. Ambidexterity and Solver Performance

(b)  
(a)  
![](/api/attachments/SEZJ6KQZ/fulltext/images/c8a5b0fc3dbd12c0834df4b8dff86b1c13a4e4cc86fb1b89ad7be478cf070a7e.jpg)

![](/api/attachments/SEZJ6KQZ/fulltext/images/a499a046d7ec91424a9b6b2b76725c9964c7488799ae10f20bf43c75d62e8f99.jpg)

![](/api/attachments/SEZJ6KQZ/fulltext/images/983eb7fd2deb3c08fb145ab763726def836b03a12fc7eae05751733dd46ddb52.jpg)  
Figure 2. Moderating Effect of Task Diversity

Combining these two effects (Figures 2a and 2b), we expect that solvers’ task diversity would steepen the curve and correspondingly amplify the peak of the inverted U-shaped relationship (Haans et al., 2016) between ambidexterity and solver performance (see Figure 2c). Hence, we hypothesize:

H2: The inverted U-shaped relationship between ambidexterity and solver performance will be steeper when task diversity is higher.

## 3.3 Task Reward

In our study, task reward refers to the average prize money of the contests that solvers participated in over a period of time. Task rewards generally motivate solver performance because high task rewards provide incentives to solvers to generate better solutions (Liu et al., 2021) and compete harder to win (Acar, 2019b).<sup>3</sup> We do not hypothesize the direct effect of task rewards on solver performance, since this has already been reported, but focus on its moderating effect on the ambidexterity-performance relationship.

When task rewards are high, individuals are typically motivated to stretch themselves to achieve desirable performance as per the task environment (Gibson & Birkinshaw, 2004). Such stretch (extra effort) assists in engaging in higher levels of exploration and exploitation since people may otherwise be less motivated to undertake both activities (Ahammad et al., 2015). Applied to our setting, high task rewards can motivate solvers to devote significant cognitive effort towards the tasks, whereby exploration and exploitation are more willingly undertaken and synergized. For example, motivated individuals will exert additional effort in closing the gap between satisficing and optimal performance, as per the bounded rationality model (Luger et al., 2018). Thus, task reward is expected to steepen the benefit curve of ambidexterity (Figure 3a).

At the same time, high task rewards will elicit greater focus and attention from solvers. Such focus and attention can help mitigate cognitive setup and residue costs when switching between tasks (Colicev et al., 2023; Staats & Gino, 2012). In other words, switching costs between exploration and exploitation would be reduced with greater focus (due to high task reward) as solver ambidexterity increases (see Figure 3b). Combining the two effects (Figures 3a and 3b), we expect that high task reward would steepen the curve and correspondingly amplify the peak of the inverted U-shaped relationship (Haans et al., 2016) between ambidexterity and solver performance (see Figure 3c). Hence, we hypothesize:

H3: The inverted U-shaped relationship between ambidexterity and solver performance will be steeper when task reward is higher.

## 3.4 In-Process Feedback

In our study, in-process feedback refers to the quantity of feedback received by solvers from seeker firms during crowdsourcing contests in a time period. Solvers have a tendency to adopt the feedback of seeker firms (Koh, 2019). Prior findings are mixed about whether such feedback helps (Chan et al., 2021; Koh, 2019; Mamykina et al., 2016) or hinders (Acar, 2019a; Jiang et al., 2022) solver performance, though there is more evidence in support of in-process feedback. Here, we focus on its moderating effect on the ambidexterityperformance relationship.

By right, in-process feedback from seekers should answer important queries from solvers and help to clarify task requirements (Jiang & Wang, 2020), which can help solvers to avoid pursuing inappropriate requirements and focus their efforts on producing high-quality solutions (Koh & Cheung, 2022). Hence, in-process feedback should steepen the benefit curve of ambidexterity by offering valuable information to help solvers achieve synergy in developing solutions (see Figure 4a).

![](/api/attachments/SEZJ6KQZ/fulltext/images/fec7e794c81c362d2761f5aa82af80bbab381c9dc9d73ae2b0d7aef501c355e1.jpg)

![](/api/attachments/SEZJ6KQZ/fulltext/images/6332a6c6b64c53bfe49cd92707006de443ddc515d13cbc096084445c0f77fdfc.jpg)

![](/api/attachments/SEZJ6KQZ/fulltext/images/e21c7c85fb520b416c99622c7d9e8a628c3be2aec7b8be4b35e5213f30b5c60a.jpg)  
Figure 3. Moderating Effect of Task Reward

![](/api/attachments/SEZJ6KQZ/fulltext/images/34268eec42c4a150439d76d9b858accf798c6183320d96acbea00d7c09367e18.jpg)

(b)  
![](/api/attachments/SEZJ6KQZ/fulltext/images/30ac8c6447df2ea71058b4456acc4ae83d88222dfe4d8bb8f8abba1dc9531d6c.jpg)

![](/api/attachments/SEZJ6KQZ/fulltext/images/ea13e9daa4498c021a6dfa6082c44e7f2afecddf84d02f6a563015ef35e30ab5.jpg)  
Figure 4. Moderating Effect of In-Process Feedback

However, when in-process feedback is high, this implies that solvers would receive a large number of comments from seeker firms when undertaking their tasks and expend additional cognitive costs to process such feedback (Cheng et al., 2020; Huang et al., 2018; Jiang et al., 2022). Extra switching costs could also be incurred when switching between task solving and feedback processing (Jiang et al., 2022; Koh & Cheung, 2022), which would accentuate the switching costs when solvers increase their ambidexterity (see Figure 4b). Solvers will become more prone to mental congestion in such situations, Such high levels of feedback could suggest that a major transformation is needed and could undermine the choice process (Puranam et al., 2015). This will add to the costs of the choice process.

In combination (Figures 4a and 4b), despite the benefit increase, we expect that high in-process feedback would flatten the curve and correspondingly lower the peak of the inverted U-shaped relationship (Haans et al., 2016) between ambidexterity and solver performance due to the considerable increase in switching costs (see Figure 4c). We expect the converse with low in-process feedback. Hence, we hypothesize:

H4: The inverted U-shaped relationship between ambidexterity and solver performance will be flatter when in-process feedback is higher.

## 4 Methodology

Our empirical context is one of the largest crowdsourcing contest platforms in China, Zhubajie (ZBJ.com). Founded in 2006, ZBJ.com connects knowledge workers (solvers) with small to mediumsized firms to offer professional services (such as product marketing, logo design, website design, and software design). It has more than 33 million registered users, 26 million clients, and a range of services that cover 25 countries and regions around the world. <sup>4</sup> ZBJ.com is a suitable platform for this study for several reasons. First, the platform hosts a number of contests simultaneously, and solvers can participate in any of these to win prizes (Jiang et al., 2022). Contest tasks include logo and virtual identity design, programming, marketing, and animation design, among others.<sup>5</sup> Thus, there is a considerable variety of tasks for solvers, which they can view in the task center. Second, the platform has a recommender system that notifies solvers of tasks that are most similar to the prior contests in which they have participated (Mo et al., 2018). This allows solvers to exploit their prior experience to complete future tasks. Solvers can also explore the discussion forum and previous winning solutions (Ye & Jensen, 2022). Thus, solvers can engage in ambidexterity by pursuing exploitation and exploration activities on the platform.

Third, the contests on the platform provide wide-ranging rewards with a wide range from 1 Chinese yuan to 68,500 (USD 0.15 to 10,041).<sup>6</sup> Solvers can participate in tasks offering any level of reward. Finally, to facilitate communication between seeker firms and solvers, the platform has features for seeker firms to provide inprocess feedback to solvers. Seeker firms can directly comment on submissions and request further modifications or adjustments (Feng et al., 2018; Jiang & Wang, 2020). Seeker firms can also provide ratings to winning solvers.

## 4.1 Data Collection

We examined all 2,836 contests that took place on ZBJ.com during the study period of 1 year (from March 1, 2018, to February 28, 2019). In line with prior research (Jiang & Wang, 2020), we dropped incomplete contests and contests that had a reward below 50 Chinese yuan (\~7 USD), as these were test runs. After this 2515 contests remained, with $6 { , } 1 2 4$ unique individual solver participants. As per our study’s focus, we further excluded those solvers who mainly worked on microtasks that did not need specialized skills, e.g., filling out academic surveys, image tagging, and posting marketing messages on social media. As a result, 6,018 solvers remained, who had largely performed tasks such as designing logos, virtual identities, or brands; creating websites, apps, or animation; or performing engineering or industrial tasks. Solvers had to explore new ideas and exploit their existing skills to perform such tasks. We collected the monthly panel data of the $6 { , } 0 1 8$ solvers from the platform for the 12-month period above. In total, there were 71,257 observations.

## 4.2 Variables and Measures

Solver performance (PER) was measured by the number of task contests won by the solver in a month. $P E R _ { i t }$ refers to the number of task contests solver i won in month t. To compute the measure for ambidexterity, we used the skillset listed on a solver’s profile to classify whether a contest task was exploitative or explorative for the solver (see Figure B1 in Appendix B for a sample solver’s profile screenshot and Figure B2 for a sample contest screenshot). We used a two-step approach to measure individual ambidexterity, which has been widely used in prior research (Mom et al., 2009, 2015; Tempelaar & Rosenkranz, 2019). In the first step, the extent of exploitation and exploration by solvers were measured separately. Exploitation refers to task activities where solvers use their existing knowledge (Schnellbächer et al., 2019). Therefore, exploitation (EPT) was measured by the number of contest tasks undertaken that were within the skillset listed on the solver’s profile in month t. Exploration refers to task activities where solvers look for new knowledge (Mom et al., 2015; Schnellbächer et al., 2019) reflected in performing tasks that require more than their existing expertise (Jeppesen & Lakhani, 2010). Thus, exploration (EPR) was measured by the number of contest tasks undertaken that were not within the skillset list on the solver’s profile in month t. Since the website only allows seeker firms and solvers to choose from the predefined contest task types and skillsets, respectively, we used exact keyword matching to identify whether solver skillsets fell within the contest task type for contests they participated in (see Table B1 in Appendix B). In the second step, we measured ambidexterity (AMB) by multiplying the values for exploration and exploitation (Liang et al., 2022; Mom et al., 2015) obtained from the first step. All measures were standardized before analyses.

Adapting from prior studies (Bayus, 2013), we measured the diversity of all contest tasks a solver undertook before the current month. We calculated task diversity<sub>it,</sub> (TDV) using an entropy measure over the contest task types: $- \sum _ { i j } p _ { i j }$ ln (p<sub>ij</sub>), where $p _ { i j }$ is the proportion of contest tasks of type j that solver i undertook in all months prior to time t. Task type j refers to the task type specified by the website (see Appendix B for an example of calculating AMB and TDV). If a solver only undertook one type of task prior to that month, then task diversity would be 0. Task reward<sub>it</sub> (TRW) was measured by the average of rewards (in RMB) of all contests which solver i participated in for month t. We have plotted the average task reward among exploitation and exploration tasks across time in Figure C1 of Appendix C—both show similar patterns. In-process feedback<sub>it</sub> (IPF) was measured by the average number of comments from seeker firms that solver i received in all contests participated in month t.

We added total submissions (TOS), past performance (t-1), exploitation, exploration, solver level, platform tenure, and competition intensity as control variables in our model, as these variables could influence solver performance (Boudreau et al., 2016; Goes et al., 2016). Solver level (LVL) was posted on the platform and used as an indicator of their reputation. It was measured by the platform as a composite score that captured solvers overall contributions, activities, and on-platform duration. Platform tenure (TEN ) was measured by the number of months a solver had been registered on the platform at the end of month t. Competition intensity $( \mathrm { C M P } _ { i t } )$ was measured by the average number of competitors (solvers) across all contests that solver i participated in for month t. We added 1 to each variable and log-transformed the variables to reduce skewness. Table 1 shows the descriptive statistics of the variables. Table 2 shows the variable correlations. VIF values of the variables ranged from 1.25 to 2.33, suggesting that multicollinearity was not an issue.

Table 1. Descriptive Statistics

<table><tr><td>Variable</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>Solver performance (PER)</td><td>0.73</td><td>1.05</td><td>0</td><td>8</td></tr><tr><td>Exploitation (EPT)</td><td>6.21</td><td>4.09</td><td>0</td><td>21</td></tr><tr><td>Exploration (EPR)</td><td>0.89</td><td>1.12</td><td>0</td><td>6</td></tr><tr><td>Ambidexterity (AMB)</td><td>5.52</td><td>6.15</td><td>0</td><td>85</td></tr><tr><td>Task diversity (TDV)</td><td>0.75</td><td>1.11</td><td>0</td><td>1.89</td></tr><tr><td>Task reward (TRW)</td><td>520.18</td><td>215.66</td><td>80</td><td>2200</td></tr><tr><td>In-process feedback (IPF)</td><td>0.84</td><td>0.75</td><td>0</td><td>3</td></tr><tr><td>Total submissions (TOS)</td><td>7.10</td><td>3.95</td><td>0</td><td>23</td></tr><tr><td>Solver level (LVL)</td><td>8.36</td><td>5.21</td><td>3</td><td>23</td></tr><tr><td>Platform tenure (TEN)</td><td>28.34</td><td>15.07</td><td>7</td><td>48</td></tr><tr><td>Competition intensity (CMP)</td><td>11.32</td><td>5.63</td><td>4.25</td><td>38.24</td></tr></table>

Table 2. Correlations Among Variables

<table><tr><td></td><td>PER</td><td>AMB</td><td>EPT</td><td>EPR</td><td>TOS</td><td>TDV</td><td>IPF</td><td>TRW</td><td>CMP</td><td>TEN</td><td>LVL</td></tr><tr><td>PER</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AMB</td><td>0.25*</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EPT</td><td>0.29*</td><td>0.42**</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EPR</td><td>-0.10</td><td>0.35**</td><td>0.18</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TOS</td><td>0.12*</td><td>0.43**</td><td>0.44**</td><td>0.39**</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TDV</td><td>0.19*</td><td>0.16*</td><td>0.06</td><td>0.13</td><td>0.32*</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IPF</td><td>0.10</td><td>0.05</td><td>0.01</td><td>0.05</td><td>0.15</td><td>0.05</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>TRW</td><td>0.30**</td><td>0.20*</td><td>-0.09</td><td>0.12*</td><td>0.09</td><td>0.17**</td><td>0.05</td><td>1</td><td></td><td></td><td></td></tr><tr><td>CMP</td><td>0.04</td><td>-0.11</td><td>0.11</td><td>0.01</td><td>0.08</td><td>0.03</td><td>0.03</td><td>0.13</td><td>1</td><td></td><td></td></tr><tr><td>TEN</td><td>-0.05</td><td>0.13*</td><td>0.02</td><td>-0.11</td><td>0.10</td><td>-0.10*</td><td>-0.05</td><td>-0.02</td><td>-0.02</td><td>1</td><td></td></tr><tr><td>LVL</td><td>0.21*</td><td>0.04</td><td>0.06</td><td>0.06</td><td>0.11</td><td>0.15*</td><td>-0.04</td><td>0.18*</td><td>0.03</td><td>-0.03</td><td>1</td></tr><tr><td colspan="12">Note: *p&lt;0.05; **p&lt;0.01; ***p&lt;0.001</td></tr></table>

## 5 Results

The Hausman test results indicated that a fixed-effects model was more appropriate than a random-effects model $( \chi ^ { 2 } = 4 1 8 . 6 2 , p < 0 . 0 0 1 )$ for our estimation. Table 3 shows the results of testing the hypotheses using panel fixedeffects regression. All models used clustered standard errors at the solver level. In Table 3, Model 1 shows the results for the main effects and control variables, while Models 2 and 3 show the results of adding the first-order and second-order moderating effects, respectively.

The results of Model 1 in Table 3 show that ambidexterity has an inverted U-shaped relationship with solver performance (β = -3.065, p < 0.001), thus supporting H1. The results of Model 3 in Table 3 indicate that task diversity (β = 1.295, p < 0.001) and task reward (β = 0.081, p < 0.05) positively moderated the inverted Ushaped relationship between ambidexterity and solver performance, thus supporting H2 and H3. In contrast, the moderating effect of in-process feedback on the inverted U-shaped relationship between ambidexterity and solver performance was significant (β = 3.017, p < 0.05). However, the main effect of in-process feedback was negative. Thus, H4 was supported.

Although it was necessary for the squared term to be significant to establish the presence of a U-shaped relationship between AMB and PER, this alone would not be sufficient (Haans et al., 2016). We conducted a formal test for an inverted U-shaped relationship, as described in Lind and Mehlum (2010), to see if the slope was sufficiently steep at both ends of the data range. We found that the slope at the lower bound was 0.521 with p < 0.01 (positive, significant) and the slope at the upper bound was -3.085 with p < 0.001 (negative, significant). This overall test for the presence of an inverted Ushaped relationship (p < 0.001) confirmed the inverted U-shaped relationship between ambidexterity and solver performance.

To better visualize the moderating effects, we graphically plotted the results in Figures 5a, 5b, and 5c.<sup>7</sup> Figure 5a indicates that when task diversity is high, the inverted U-shaped curve is steeper. Figure 5b shows that when task reward is high, the inverted U-shaped curve is slightly steeper. Figure 5c indicates that when inprocess feedback is high, the inverted U-shaped curve is flatter. These observations are consistent with the arguments for H2 to H4.

a very informative adjunct to numerical statistical results” when analyzing the interaction term in a non-linear model.

Table 3. Results of Hypothesis Testing

<table><tr><td>DV = Ln(PERit + 1)</td><td colspan="2">Model 1</td><td colspan="2">Model 2</td><td colspan="2">Model 3</td></tr><tr><td></td><td>β</td><td>Robust SE</td><td>β</td><td>Robust SE</td><td>β</td><td>Robust SE</td></tr><tr><td>Ln(AMBit + 1)</td><td>1.582***</td><td>0.275</td><td>0.734**</td><td>0.238</td><td>2.006***</td><td>0.503</td></tr><tr><td>Ln((AMBit)2 + 1)</td><td>-3.065***</td><td>0.364</td><td>-1.916***</td><td>0.402</td><td>-7.024**</td><td>2.111</td></tr><tr><td>Ln(TDVit + 1) × Ln(AMBit + 1)</td><td></td><td></td><td>0.151***</td><td>0.030</td><td>0.467***</td><td>0.087</td></tr><tr><td>Ln(TRWit + 1) × Ln(AMBit + 1)</td><td></td><td></td><td>0.009*</td><td>0.003</td><td>0.009</td><td>0.010</td></tr><tr><td>Ln(IPFit + 1) × Ln(AMBit + 1)</td><td></td><td></td><td>0.079</td><td>0.057</td><td>-0.563*</td><td>0.260</td></tr><tr><td>Ln(TDVit + 1) × Ln((AMBit)2 + 1)</td><td></td><td></td><td></td><td></td><td>1.295***</td><td>0.334</td></tr><tr><td>Ln(TRWit) × Ln((AMBit)2 + 1)</td><td></td><td></td><td></td><td></td><td>0.081*</td><td>0.039</td></tr><tr><td>Ln(IPFit) × Ln((AMBit)2 + 1)</td><td></td><td></td><td></td><td></td><td>3.017*</td><td>1.222</td></tr><tr><td>Ln (EPRit + 1)</td><td>-1.394***</td><td>0.175</td><td>-0.859***</td><td>0.192</td><td>-1.140***</td><td>0.201</td></tr><tr><td>Ln (EPTit + 1)</td><td>0.373***</td><td>0.124</td><td>0.793***</td><td>0.140</td><td>0.598***</td><td>0.146</td></tr><tr><td>Ln(PERi(t-1) + 1)</td><td>0.875***</td><td>0.158</td><td>0.800***</td><td>0.158</td><td>0.370***</td><td>0.058</td></tr><tr><td>Ln(CMPit + 1)</td><td>0.062</td><td>0.066</td><td>0.060</td><td>0.066</td><td>0.063</td><td>0.066</td></tr><tr><td>Ln(LVLit + 1)</td><td>2.333***</td><td>0.684</td><td>2.290***</td><td>0.685</td><td>2.121***</td><td>0.685</td></tr><tr><td>Ln(TDVit + 1)</td><td>0.885***</td><td>0.033</td><td>0.243*</td><td>0.123</td><td>1.012***</td><td>0.239</td></tr><tr><td>Ln(IPFit + 1)</td><td>0.078</td><td>0.089</td><td>-0.149*</td><td>0.073</td><td>-2.464*</td><td>0.967</td></tr><tr><td>Ln(TRWit + 1)</td><td>0.092**</td><td>0.004</td><td>0.051**</td><td>0.017</td><td>0.315*</td><td>0.157</td></tr><tr><td>Ln(TENit + 1)</td><td>-0.103</td><td>0.065</td><td>-0.103</td><td>0.060</td><td>-0.099</td><td>0.060</td></tr><tr><td>Fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Month dummies</td><td colspan="2">Included</td><td colspan="2">Included</td><td colspan="2">Included</td></tr><tr><td>Clustered standard errors</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Within R square</td><td colspan="2">0.411</td><td colspan="2">0.417</td><td colspan="2">0.431</td></tr><tr><td>Number of observations</td><td colspan="6">71,257</td></tr><tr><td colspan="7">Note: *p&lt;0.05; **p&lt;0.01; ***p&lt;0.001</td></tr></table>

<table><tr><td><img src="/api/attachments/SEZJ6KQZ/fulltext/images/fe73061f41c75efa8ae4499a51073c15e5200726511c58b03d102ce75edae5b6.jpg"/>Low AMB High AMB</td><td><img src="/api/attachments/SEZJ6KQZ/fulltext/images/3053d5952f90928e53b7342a2da188968ae4fcd0e614a987e6457387bff4c79b.jpg"/></td></tr><tr><td>Figure 5a. Moderating Effect of Task Diversity</td><td>Figure 5b. Moderating Effect of Task Reward</td></tr><tr><td colspan="2">Solver PerformanceLow AMB High AMB</td></tr><tr><td colspan="2">Figure 5c. Moderating Effect of In-Process Feedback</td></tr></table>

## 6 Robustness Checks

We conducted several robustness checks to assess the validity of our results. First, we used alternative measures for ambidexterity. Second, we corrected for selection bias by using the Heckman model. Third, we used the instrumental variable approach to account for potential endogeneity. Fourth, we lagged our independent variables and moderators to predict the dependent variable and conducted the Granger causality test.

## 6.1 Alternative Measures for Ambidexterity

As an alternative, we conducted the analysis with a balance measure for ambidexterity (Cao et al., 2009). To control total submissions, we used proportional measures of exploration and exploitation, i.e., the percentage of explorative and exploitative activities among total activities. Ambidexterity as balance was calculated as 1 minus the absolute difference between proportional exploitation and proportional exploration (1 ̶ exploitation-exploration|). Results in Table 4a show that the balance measure of ambidexterity largely produces similar results as in Table 3, except for the nonsignificant moderation effect of task reward. This supports the robustness of our main findings.

Considering possible difficulties in interpreting ambidexterity results on their own, prior research has used cluster analysis to classify individuals into distinct groups based on the extent of exploration and exploitation (Gibson & Birkinshaw, 2004; Jansen et al., 2012; Kristal et al., 2010). As per Jansen et al. (2012) and Kristal et al. (2010), we conducted a K-means cluster analysis based on proportional exploitation and exploration measures on the entire sample using Python. A three-cluster solution was identified (see Table 4b). We conducted ANOVA and Tukey’s HSD tests to compare solver performance across the three clusters. Cluster 2, with a moderate level of ambidexterity using either the interaction or balance measure, exhibited the highest solver performance of 0.905. This suggests that ambidexterity has an inverted U-shaped relationship with solver performance, offering additional support for H1. Furthermore, the results in Table 4b indicate that undertaking both exploration and exploitation to some degree (Clusters 2 and 3) produces better performance than overreliance on exploitation alone (Cluster 1). Interestingly, the best solver performance was seen in the combination of 81.1% exploitation and 15.2% exploration (Cluster 2) rather than the 50%-50% combination suggested in prior studies (e.g., Cao et al., 2009; He & Wong, 2004).

Table 4a. Results with Alternative (Balance) Measure of Ambidexterity

<table><tr><td></td><td colspan="2">DV = Ln(PERit + 1)</td></tr><tr><td></td><td>β</td><td>Robust SE</td></tr><tr><td>Ln(AMBit + 1)</td><td>3.565***</td><td>0.465</td></tr><tr><td>Ln((AMBit)2 + 1)</td><td>-2.976***</td><td>0.390</td></tr><tr><td>Ln(TDVit + 1) × Ln(AMBit + 1)</td><td>0.528***</td><td>0.086</td></tr><tr><td>Ln(TRWit + 1) × Ln(AMBit + 1)</td><td>0.018</td><td>0.010</td></tr><tr><td>Ln(IPFit + 1) × Ln(AMBit + 1)</td><td>0.326***</td><td>0.078</td></tr><tr><td>Ln(TDVit + 1) × Ln((AMBit)2 + 1)</td><td>1.385***</td><td>0.328</td></tr><tr><td>Ln(TRWit) × Ln((AMBit)2 + 1)</td><td>-0.025</td><td>0.039</td></tr><tr><td>Ln(IPFit) × Ln((AMBit)2 + 1)</td><td>0.623***</td><td>0.180</td></tr><tr><td>Ln (EPRit + 1)</td><td>-0.602***</td><td>0.113</td></tr><tr><td>Ln (EPTit + 1)</td><td>0.758***</td><td>0.103</td></tr><tr><td>Ln(PERi(t-1) + 1)</td><td>0.075</td><td>0.058</td></tr><tr><td>Ln(CMPit + 1)</td><td>0.046</td><td>0.065</td></tr><tr><td>Ln(LVLit + 1)</td><td>2.283**</td><td>0.681</td></tr><tr><td>Ln(TDVit + 1)</td><td>0.884***</td><td>0.229</td></tr><tr><td>Ln(IPFit + 1)</td><td>-0.227*</td><td>0.097</td></tr><tr><td>Ln(TRWit + 1)</td><td>0.047</td><td>0.027</td></tr><tr><td>Ln(TENit + 1)</td><td>-0.109</td><td>0.060</td></tr><tr><td>Fixed effects</td><td colspan="2">Yes</td></tr><tr><td>Month dummies</td><td colspan="2">Included</td></tr><tr><td>Clustered standard errors</td><td colspan="2">Yes</td></tr><tr><td>Within R square</td><td colspan="2">0.422</td></tr><tr><td>Number of observations</td><td colspan="2">71,257</td></tr><tr><td colspan="3">Note: *p&lt;0.05; **p&lt;0.01; ***p&lt;0.001</td></tr></table>

Table 4b. Cluster Analysis Results and Comparisons across Clusters

<table><tr><td></td><td>Exploitation</td><td colspan="2">Exploration</td><td>Ambidexterity measured with interaction</td><td>Ambidexterity measured with balance</td><td>Solver performance</td></tr><tr><td>Cluster 1</td><td>0.928</td><td colspan="2">0.068</td><td>0.063</td><td>0.140</td><td>0.476</td></tr><tr><td>Cluster 2</td><td>0.811</td><td colspan="2">0.152</td><td>0.122</td><td>0.341</td><td>0.905</td></tr><tr><td>Cluster 3</td><td>0.725</td><td colspan="2">0.244</td><td>0.177</td><td>0.519</td><td>0.684</td></tr><tr><td colspan="3">Cluster 1 vs. Cluster 2 (F value)</td><td colspan="4">65.98***</td></tr><tr><td colspan="3">Cluster 1 vs. Cluster 3 (F value)</td><td colspan="4">32.66***</td></tr><tr><td colspan="3">Cluster 2 vs. Cluster 3 (F value)</td><td colspan="4">35.95***</td></tr><tr><td colspan="7">Note: *** p&lt;0.001</td></tr></table>

Table 5. Results of Heckman Selection Bias Correction

<table><tr><td>DV = Ln(PERit + 1)</td><td colspan="2">Heckman selection bias model</td></tr><tr><td></td><td>Coefficient</td><td>Robust SE</td></tr><tr><td>Ln(AMBit + 1)</td><td>0.529*</td><td>0.265</td></tr><tr><td>Ln((AMBit)2 + 1)</td><td>-1.657*</td><td>0.665</td></tr><tr><td>Ln(TDVit + 1) × Ln(AMBit + 1)</td><td>0.266***</td><td>0.070</td></tr><tr><td>Ln(TRWit + 1) × Ln(AMBit + 1)</td><td>0.000</td><td>0.008</td></tr><tr><td>Ln(IPFit + 1) × Ln(AMBit + 1)</td><td>-0.018</td><td>0.120</td></tr><tr><td>Ln(TDVit + 1) × Ln((AMBit)2 + 1)</td><td>0.162*</td><td>0.078</td></tr><tr><td>Ln(TRWit) × Ln((AMBit)2 + 1)</td><td>0.051*</td><td>0.023</td></tr><tr><td>Ln(IPFit) × Ln((AMBit)2 + 1)</td><td>0.047*</td><td>0.023</td></tr><tr><td>Ln (EPRit + 1)</td><td>-0.584***</td><td>0.180</td></tr><tr><td>Ln (EPTit + 1)</td><td>1.020***</td><td>0.128</td></tr><tr><td>Ln(PERi(t-1) + 1)</td><td>0.086**</td><td>0.058</td></tr><tr><td>Ln(TDVit + 1)</td><td>0.316*</td><td>0.169</td></tr><tr><td>Ln(IPFit + 1)</td><td>-0.198*</td><td>0.065</td></tr><tr><td>Ln(TRWit + 1)</td><td>0.056*</td><td>0.028</td></tr><tr><td>Inverse Mills ratioit</td><td>0.571**</td><td>0.146</td></tr><tr><td>Control variables</td><td colspan="2">Yes</td></tr><tr><td>Fixed effects</td><td colspan="2">Yes</td></tr><tr><td>Month dummies</td><td colspan="2">Included</td></tr><tr><td>χ2 (df)</td><td colspan="2">-49651.21(38)</td></tr><tr><td>Number of observations</td><td colspan="2">71,257</td></tr><tr><td colspan="3">Note: * p &lt; 0.05; ** p &lt; 0.01; *** p &lt; 0.001</td></tr></table>

## 6.2 Heckman Selection Bias Correction

Solver participation in a contest could be due to certain unobservable solver (Jeppesen & Lakhani, 2010) or task characteristics (Boudreau et al., 2011). It is possible that such unobservable characteristics affect solver performance, thereby introducing selection bias into our results. We addressed this concern using the two-stage Heckman selection bias model (Heckman, 1974, 1976; Wooldridge, 2010).

In the first stage, we used a Probit model to estimate the likelihood of a solver participating in a contest task. The platform allows solvers to show their interest in a contest task by signing up first. For each contest, around 32.65% of solvers who signed up submitted a solution eventually. We could thus estimate the propensity of a solver, who has signed up, to make a submission for the contest task while ruling out the confounding explanation that the solver lacks awareness of the contest task. Following prior research (Jeppesen & Lakhani, 2010), we used solver and contest characteristics to predict the propensity of them submitting a solution for the contest task. Specifically, existing task reward and other variables, such as whether the task type matches the exploitative task type of the solver, the number of solvers who registered for the contest task, the total available contest tasks, the total available contest tasks of a particular type, the solver rating, and the average rating of the other registered solvers were used as predictors. Results of the first-stage estimation are shown in Table C1 in Appendix C.

We then calculated the inverse Mills ratio based on the Probit regression for the first-stage estimation and included it as an additional control variable in the second-stage estimation of solver performance. The results (shown in Table 5) are consistent with the results in Model 3 of Table 3. These results suggest that our main findings are not due to selection bias.

Table 6. Results of Instrumental Variable Estimation

<table><tr><td>DV = Ln(PERit + 1)</td><td colspan="2">Model 1</td><td colspan="2">Model 2</td></tr><tr><td></td><td>β</td><td>Robust SE</td><td>β</td><td>Robust SE</td></tr><tr><td>Ln(AMBit + 1)</td><td>40.148***</td><td>11.509</td><td>51.59</td><td>16.11</td></tr><tr><td>Ln((AMBit)2 + 1)</td><td>-157.862***</td><td>45.515</td><td>-227.72</td><td>71.70</td></tr><tr><td>Ln(TDVit + 1) × Ln(AMBit + 1)</td><td>0.364*</td><td>0.132</td><td>-0.02</td><td>0.22</td></tr><tr><td>Ln(TRWit + 1) × Ln(AMBit + 1)</td><td>-0.061**</td><td>0.026</td><td>-0.09*</td><td>0.04</td></tr><tr><td>Ln(IPFit + 1) × Ln(AMBit + 1)</td><td>-18.157**</td><td>5.311</td><td>-26.49**</td><td>8.42</td></tr><tr><td>Ln(TDVit + 1) × Ln((AMBit)2 + 1)</td><td>1.557**</td><td>0.499</td><td>0.65*</td><td>0.27</td></tr><tr><td>Ln(TRWit) × Ln((AMBit)2 + 1)</td><td>0.131*</td><td>0.068</td><td>0.32*</td><td>0.13</td></tr><tr><td>Ln(IPFit) × Ln((AMBit)2 + 1)</td><td>84.291**</td><td>24.529</td><td>128.16**</td><td>40.66</td></tr><tr><td>Ln(TDVit + 1)</td><td>1.762***</td><td>0.418</td><td>0.21</td><td>0.59</td></tr><tr><td>Ln(TRWit + 1)</td><td>0.167**</td><td>0.052</td><td>0.04</td><td>0.06</td></tr><tr><td>Ln(IPFit + 1)</td><td>-61.512***</td><td>17.832</td><td>-98.27**</td><td>31.14</td></tr><tr><td>Control variables</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Instrumental variables</td><td colspan="2">Total number of available contest tasks in month t</td><td colspan="2">(Total number of available contest tasks in month t)2</td></tr><tr><td>Fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Month dummies</td><td colspan="2">Included</td><td colspan="2">Included</td></tr><tr><td>R square</td><td colspan="2">0.106</td><td colspan="2">0.103</td></tr><tr><td>Cragg-Donald Wald F</td><td colspan="2">20.24</td><td colspan="2">16.67</td></tr><tr><td>Number of observations</td><td colspan="4">71,257</td></tr><tr><td colspan="5">Note: *p&lt;0.05; **p&lt;0.01; ***p&lt;0.001</td></tr></table>

## 6.3 Instrumental Variable Estimation

The presence of endogeneity issues needs to be investigated. It is possible that ambidexterity could be influenced by solver characteristics that are unobserved and dynamic over time and solver reactions to the conditions of contest tasks, which also influence performance. The instrumental variable approach can be an effective way to address such potential endogeneity issues (Wooldridge, 2010).

For ambidexterity, we identified the total market supply of contest tasks, measured by the total number of available contest tasks on the platform in month t, which determines if solvers have enough contest tasks to undertake (Boudreau et al., 2011) and opportunities for engaging in ambidexterity but not solver performance (Chen et al., 2021). This variable has been used to instrument the impact of solver experience on contest performance (Menon et al., 2020) and the impact of top contestants on contestant performance (Chen et al., 2021) in prior studies. Thus, we used the total number of available contest tasks in month t to instrument for ambidexterity in this study (see Table 6).

We examined the validity of the instrumental variable. First, we confirmed that the instrumental variable met the exclusion restrictions, as mentioned above. Second, we ran regressions with each endogenous variable as the dependent variable and the instrumental variable as the predictor. The instrumental variable was highly significant, and the F-statistics exceeded the usual threshold of 10 and the critical value of 10% maximal IV size, indicating it was relevant and strong (Stock & Yogo, 2002). Tests of underidentification and weak instrumental variables suggested that our models did not suffer from underidentification or weak instruments. Third, to confirm the validity of the inferences about the instrumental variable, we checked the incremental explanatory power of the exogenous instrumental variable for ambidexterity (Rossi, 2014). Table C2 in Appendix C shows that the incremental R squares are statistically significant (ΔR<sup>2</sup> = 0.089, p < 0.001 for ambidexterity; $\Delta \mathrm { R } ^ { 2 } = 0 . 0 3 0 , p < 0 . 0 0 1$ for squared ambidexterity).

After this, the two-stage instrumental variable test was used to correct for potential endogeneity. In the first stage, we ran regression models using the instrumental variable and other exogenous variables as inputs to predict our main variables (Ln(AMB<sub>it</sub>) and Ln(AMB )<sup>2</sup>). We used the command xtivreg2 in Stata to carry out the instrumental variable estimation. The results of these tests, presented in Table 6, are consistent with our main results, attesting to the robustness of our main findings.

## 6.4 Additional Robustness Tests

To further address potential endogeneity issues, we lagged our independent variables and moderators and reran the analysis. The results shown in Table 7 are consistent with those in Model 3 of Table 3. The TRW finding is reasonable, as rewards of past tasks should have a limited impact on the performance of future tasks. Results also suggest that ambidexterity has an impact on future performance. This finding is interesting, as it suggests that the effects of ambidexterity can be lasting and that individuals internalize the knowledge learned from orchestrating exploration and exploitation activities.

Table 7. Results with Lagged Independent Variables and Moderators

<table><tr><td colspan="3">DV = Ln(PERit + 1)</td></tr><tr><td>Term</td><td>Coefficient</td><td>Robust SE</td></tr><tr><td>Ln(AMBi(t-1) + 1)</td><td>0.341***</td><td>0.023</td></tr><tr><td>Ln(AMBi(t-1) + 1)2</td><td>-0.891***</td><td>0.035</td></tr><tr><td>Ln(TDVi(t-1) + 1) × Ln(AMBi(t-1) + 1)</td><td>0.121***</td><td>0.030</td></tr><tr><td>Ln(TRWi(t-1) + 1) × Ln(AMBi(t-1) + 1)</td><td>0.023</td><td>0.021</td></tr><tr><td>Ln(IPFi(t-1) + 1) × Ln(AMBi(t-1) + 1)</td><td>-0.508***</td><td>0.153</td></tr><tr><td>Ln(TDVi(t-1) + 1) × Ln(AMBi(t-1) + 1)2</td><td>0.045***</td><td>0.006</td></tr><tr><td>Ln(TRWi(t-1) + 1) × Ln(AMBi(t-1) + 1)2</td><td>0.019*</td><td>0.010</td></tr><tr><td>Ln(IPFi(t-1) + 1) × Ln(AMBi(t-1) + 1)2</td><td>0.082*</td><td>0.034</td></tr><tr><td>Ln(TDVi(t-1) + 1)</td><td>0.225***</td><td>0.069</td></tr><tr><td>Ln(TRWi(t-1) + 1)</td><td>0.049*</td><td>0.025</td></tr><tr><td>Ln(IPFi(t-1) + 1)</td><td>-0.195*</td><td>0.088</td></tr><tr><td>Control variables</td><td colspan="2">Yes</td></tr><tr><td>Fixed effects</td><td colspan="2">Yes</td></tr><tr><td>Clustered standard errors</td><td colspan="2">Yes</td></tr><tr><td>Within Rsquare</td><td colspan="2">0.401</td></tr><tr><td>Number of observations</td><td colspan="2">71,257</td></tr><tr><td colspan="3">Note: *p&lt;0.05; **p&lt;0.01; ***p&lt;0.001</td></tr></table>

## 6.4.1 Granger Causality Test

To rule out reverse causality, we ran the Granger causality test (Granger, 1988). The results, shown in Table C3 in Appendix C, suggest that ambidexterity granger caused solver performance, supporting our main hypothesis. Also, the results show that task diversity and task reward Granger caused solver performance, which is consistent with the literature (Bayus, 2013; Liu et al., 2021). However, solver performance did not Granger cause any other constructs in this study.

## 7 Discussion and Contributions

Motivated by the aim to improve solver performance in crowdsourcing contests and the lack of understanding about how solvers’ ambidexterity ability (a combination of exploration and exploitation activities) interacts with contextual characteristics to affect their performance, this study examines the relationship between ambidexterity and solver performance and accounts for the moderating effects of key task characteristics on this relationship. As hypothesized, our results reveal that ambidexterity has an inverted U-shaped relationship with solver performance. Furthermore, task diversity and task reward positively moderate the inverted Ushaped relationship, whereas in-process feedback negatively moderates the relationship.

## 7.1 Theoretical Contributions

This study contributes to crowdsourcing literature as well as related individual ambidexterity and job characteristics studies in several important ways. First, various streams of research on crowdsourcing have examined the predictors of organizational adoption of crowdsourcing (e.g., Allen et al., 2018), solver participation in crowdsourcing (e.g., Jian et al., 2019; Ye & Kankanhalli, 2017), submission quality (e.g., Martinez, 2017), and solver performance (Menon et al., 2020). This study adds to the last stream of research by adopting a novel lens, i.e., the individual ambidexterity perspective (Mom et al., 2007; Mom et al., 2009) to examine the antecedents of solver performance. Our study relies on the individual ambidexterity lens to explain how appropriately combining exploration and exploitation can achieve optimal performance. By doing so, our study extends the crowdsourcing literature and paves the way for future research that can build on the findings.

In addition, while ambidexterity is recognized as a key organizational capability, there is limited knowledge of how effective ambidexterity is for individuals and particularly for their crowdsourcing performance. Thus, we used the ambidexterity lens to theorize the performance impacts of the combination of exploration and exploitation activities rather than focusing on their separate effects. Our findings challenge prior suggestions (e.g., Papanastasiou et al., 2018) that a greater balance between exploration and exploitation will always produce higher performance. Our results also depart from earlier suggestions that a perfect balance (i.e., 50% exploration and 50% exploitation) is the best strategy for superior performance (Cao et al., 2009; He & Wong, 2004). Rather, our findings indicate that the cluster of bestperforming solvers mainly employed an exploitation strategy combined with some degree of exploration— in our case, a ratio of 5.33 exploitation activities to 1 exploration activity (see Table 4b). Our work adds to the literature by explicating the proportion of constituent activities of ambidexterity needed for high performance in the context of our study.

Second, our work contributes to crowdsourcing research examining the effects of contest and task characteristics on solver outcomes by drawing on the bounded rationality model. Prior studies have explored the direct effects of contest and task characteristics on the number of solver participants (Chen et al., 2021; Liu et al., 2021), participation intention (Martinez, 2017), actual participation (Ye & Kankanhalli, 2017), and solver performance. Here, we identify three key task characteristics (i.e., task diversity, task reward, and inprocess feedback) in crowdsourcing settings that influence the relationship between ambidexterity and solver performance. By doing so, our work adds to the literature by identifying the contextual contingencies for the curvilinear relationship. Also, we respond to calls for research on contextual characteristics that moderate the relationship between ambidexterity and performance (Schnellbächer et al., 2019) and generate fresh insights into this topic.

Third, our results add to the body of work on individual ambidexterity in both IS and management domains. While prior research has proposed a linear relationship between ambidexterity and performance in organizational IS and management studies (Im & Rai, 2008; Mom et al., 2015; Schnellbächer et al., 2019), we uncover a nonlinear (i.e., inverted U-shaped) relationship between ambidexterity and solver performance in the crowdsourcing context. Furthermore, unlike organizations that can use structural approaches, such as division of labor (Mom et al., 2009), to gain continued benefits of ambidexterity, our findings suggest that there is a limit to which individual solvers can keep increasing ambidexterity to improve their performance. More broadly, both IS and management studies have examined the ambidexterity of managers and employees in organizational settings (Mom et al., 2019; Schnellbächer et al., 2019), including in the IS function (Roberts et al., 2021; Werder & Heckmann, 2019). Here, we examine the concept in the crowdsourcing context with its distinguishing characteristics. By doing so, our work responds to calls for research on the relationship between ambidexterity and performance in non-organizational contexts (Pertusa-Ortega et al., 2020).

## 7.2 Practical Implications

Leveraging crowdsourcing contests can be a challenge for seeker firms and contest platforms. The lack of ex ante contractual relationships makes solver performance difficult to manage because contest platforms have limited control over the solution composition process (Zhang et al., 2019). In these circumstances, the results of this study offer valuable insights for solvers, contest platforms, and seeker firms. First, solver performance can be enhanced through solvers calibrating their engagement in exploration and exploitation activities. The inverted Ushaped relationship between ambidexterity and solver performance suggests that low or high levels of ambidexterity may not help win contests. Rather, engaging in moderate levels of ambidexterity would be optimal for solver performance.

To facilitate exploitation activities, contest platforms provide tools to recommend tasks that are similar to solvers’ prior tasks (Mo et al., 2018). To facilitate exploration activities, contest platforms have been publicizing past winning solutions and encouraging solvers to participate in discussion forums for exposure to diverse ideas (Ye & Jensen, 2022). Other means include prompting solvers to use social media for exploration and exploitation (Castillo et al., 2021) or providing opportunities for solvers to review peers’ work (Riedl & Seidel, 2018). Going beyond these suggestions, our findings indicate that contest platforms could help solvers attain their optimal ambidexterity levels by identifying the turning point of their inverted U-shaped relationship. Platforms can estimate the turning point for solvers based on their performance and provide features to selectively nudge them to operate near their turning point. Solvers whose ambidexterity is lower than the optimal level could be nudged to increase their exploitation or exploration activities, while those who are above the level could be alerted to the negative effects of doing so. The measure for ambidexterity used here allows contest platforms to develop metrics for tracking ambidexterity, through which solver performance can be enhanced. In addition, platforms can consider using AI algorithms to help reduce taskswitching costs (Gong & Png, 2023) for solvers.

Second, our finding that task diversity steepens the inverted U-shaped relationship between ambidexterity and solver performance suggests that it is beneficial for solvers to perform diverse tasks. Contest platforms can enhance task diversity by encouraging solvers to attempt different task types. Because solvers tend to participate in exploitative tasks, contest platforms can selectively promote other task types for solvers (Rietveld et al., 2019). The skillset list on solvers’ profiles allow these platforms to track the task diversity of solvers with the objective of nudging them to pursue task types that they may not prefer. For instance, platforms could offer incentives to solvers who are willing to go beyond their favorite task type to attempt other task types. They could also incorporate some degree of variety in the tasks they recommend to solvers.

Third, our result that task reward steepens the inverted Ushaped relationship between ambidexterity and solver performance suggests that task contests need to be priced appropriately. Because of the conventional wisdom that crowdsourcing is a means of cost reduction (Wang et al., 2017; Ye & Kankanhalli, 2015), there is a tendency for seeker firms to offer inadequate rewards for task contests. However, pricing task contests lower than what the solutions are worth may not garner quality solutions (Liu et al., 2021). To tackle this issue, contest platforms can offer recommendations to seeker firms about the appropriate levels of task rewards for various task types. The base level of task reward for each task type can be determined from past data that reveals the reward level below which quality solutions are unlikely to be submitted. Contest platforms can also inform seeker firms about the median and maximum levels of task rewards for each task type to assist in their price setting. Finally, we found that in-process feedback flattens the U-shaped relationship between solver ambidexterity and performance. Although many crowdsourcing design platforms allow seeker firms to provide feedback to solvers, such feedback may not always be beneficial. Platforms could suggest that seekers adopt more mindful approaches to regulate the amount of in-process feedback they provide to solvers.

More broadly, our study offers suggestions for workers in general. Our findings highlight that workers often keep performing the same tasks they are good at. Given that existing jobs could become redundant or automated, especially with AI advances, workers need to anticipate and be prepared for a transition to other roles while improving the quality of performing their existing role (Lysyakov & Viswanathan, 2023). Some exploration could be helpful and should be encouraged for workers. For example, companies like Google and Facebook have implemented autonomy programs where employees spend an afternoon every week working on their own projects to pursue their passions (Kotler, 2021).

Furthermore, our study offers suggestions for skill development for the online labor market. For worker skill development, organizations need to consider job allocation and rotation. However, our study suggests there should be careful consideration of ambidexterity issues (the degree of exploration versus exploitation needed) in the rotation and assignment of new jobs, which is contextdependent. Although it is appealing to develop new skills, our study suggests that a small extent of exploration combined with mostly exploitation can help individual workers attain better performance. This suggestion is in line with research stating that developing a T-shaped skill set should be encouraged for workers’ performance (Caputo et al., 2023; Demirkan & Spohrer, 2018).

## 7.3 Limitations and Future Research

The results of this work need to be interpreted in light of its limitations, which, however, point to several avenues of future research. First, this study involved a single crowdsourcing contest platform (i.e., ZBJ.com), so caution must be exercised in generalizing the results to other contest platforms. It is likely that the results could apply to other contest platforms with similar affordances for solver ambidexterity (e.g., 99designs). However, when platforms rank solver performance (e.g., TopCoder), the relationship between ambidexterity and solver performance could differ from what we found. Future work could examine the relationship between ambidexterity and solver performance under such varied conditions, including for non-contest-based crowdsourcing and crowdwork.

Second, building on this study, future research could explore the predictors of ambidexterity to improve the understanding of how solver ambidexterity can be enhanced. It would be interesting to discover what contributes to the decision process of exploration vs. exploitation. What mechanism underlies the choice process? How does transformation take place when feedback is received?

Third, we examined the moderating effects of three contextual characteristics (i.e., task diversity, task reward, and in-process feedback) on the relationship between ambidexterity and solver performance. While these results enrich our understanding of the boundary conditions of this relationship, future studies could examine the moderating effects of other contextual characteristics, such as solver experience (Chan et al., 2021; Ye & Jensen, 2022), task variability (Blohm et al., 2016), solver demographics (Jeppesen & Lakhani, 2010), environmental characteristics (Boudreau et al., 2016), and formal training mechanisms.

Fourth, we used measures for solver performance that indicate its quantity (i.e., number of task contests won). Future research could employ quality indicators (e.g., submission novelty) to further explore the relationship between ambidexterity and solver performance. Fifth, we checked whether tasks fall under their profile skill list to measure the exploitation and exploration activities of solvers. Although this measure has its own merits, future work could attempt to more directly capture whether solvers are exploiting their experience or exploring new possibilities. Finally, future research could conduct experiments to reveal the mechanisms that explain the causal effects of ambidexterity on solver performance.

## 8 Conclusion

Crowdsourcing contests often suffer from poor solver performance. Solver ambidexterity could potentially improve their performance; however, little is known about how it can be enhanced and provide value in crowdsourcing contests. Thus motivated, we theorize and empirically validate an inverted U-shaped relationship between ambidexterity and solver performance. We also explore the underlying mechanisms and outline the boundary conditions of this relationship. Specifically, we show that three contextual characteristics, i.e., task diversity, task reward, and in-process feedback, moderate this relationship. In the years ahead, crowdsourcing would be an increasingly important means for seeker firms to find solutions to their problems (Jiang et al., 2022). Research that generates theoretical insights about how to improve the practice of crowdsourcing can significantly benefit the ecosystem of seeker firms, solvers, and contest platforms. This study makes salient contributions in this direction.

## References

Acar, O. A. (2019a). Why crowdsourcing often leads to bad ideas. Harvard Business Review. https://hbr.org/2019/12/why-crowdsourcingoften-leads-to-bad-ideas

Acar, O. A. (2019b). Motivations and solution appropriateness in crowdsourcing challenges for innovation. Research Policy, 48(8), Article 103716.

Afuah, A., & Tucci, C. (2012). Crowdsourcing as a solution to distant search. Academy of Management Review, 37(3), 355-375.

Ahammad, F. M., Mook Lee, S., Malul, M., & Shoham, A. (2015). Behavioral ambidexterity: The impact of incentive schemes on productivity, motivation, and performance of employees in commercial banks. Human Resource Management, 54(S1), s45-s62.

Allen, B., Chandrasekaran, D., & Basuroy, S. (2018). Design crowdsourcing: The impact on new product performance of sourcing design solutions from the “crowd.” Journal of Marketing, 82(2), 106-123.

Althuizen, N., & Chen, B. (2022). Crowdsourcing ideas using product prototypes: the joint effect of prototype enhancement and the product design goal on idea novelty. Management Science, 68(4), 3008-3025.

Archak, N., & Ghose, A. (2010). Learning-by-doing and project choice: A dynamic structural model of crowdsourcing. Proceedings of the International Conference on Information Systems.

Attebery, P. (2017). The problem of 99Designs. Medium. https://medium.com/designcue/the-plague-of-99designs-7e67935c25f1

Bayus, B. (2013). Crowdsourcing new product ideas over time: An analysis of the Dell Ideastorm community. Management Science, 59(1), 226- 244.

Birkinshaw, J., & Gibson, C. (2004). Building ambidexterity into an organisation. MIT Sloan Management Review, 45(4), 47-55.

Birkinshaw, J., & Gupta, K. (2013). Clarifying the distinctive contribution of ambidexterity to the field of organization studies. Academy of Management Perspectives, 27(4), 287-298.

Blohm, I., Leimeister, J. M., & Krcmar, H. (2013). Crowdsourcing: How to benefit from (too) many great ideas. MIS Quarterly Executive, 12(4), 199-211.

Blohm, I., Riedl, C., Füller, J., & Leimeister, J. M. (2016). Rate or trade? Identifying winning ideas in open idea sourcing. Information Systems Research, 27(1), 27-48.

Bockstedt, J., Druehl, C., & Mishra, A. (2016). Heterogeneous submission behavior and its implications for success in innovation contests with public submissions. Production and Operations Management, 25(7), 1157-1176.

Boone, C., & Hendriks, W. (2009). Top management team diversity and firm performance: Moderators of functional-background and locus-of-control diversity. Management Science, 55(2), 165-180.

Boudreau, K., Lakhani, K. R., & Menietti, M. (2016). Performance responses to competition across skills-level in rank-order tournaments: Field evidence and implications for tournamenet design. RAND Journal of Economics, 47(1), 140-165.

Boudreau, K. J., Lacetera, N., & Lakhani, K. R. (2011). Incentives and problem uncertainty in innovation contests: An empirical analysis. Managemnt Science, 57(5), 843-863.

Cao, Q., Gedajlovic, E., & Zhang, H. (2009). Unpacking organizational ambidexterity: Dimensions, contingencies, and synergistic effects. Organization Science, 20(4), 781-796.

Caputo, F., Cillo, V., Fiano, F., Pironti, M., & Romano, M. (2023). Building T-shaped professionals for mastering digital transformation. Journal of Business Research, 154, Article 113309.

Castillo, A., Benitez, J., Llorens, J. & Braojos, J. (2021). Impact of social media on the firm’s knowledge exploration and knowledge exploitation: The role of business analytics talent. Journal of the Association for Information Systems, 22(5), 1472-1508.

Chan, K. W., Li, S. Y., Ni, J., & Zhu, J. J. (2021). What feedback matters? The role of experience in motivating crowdsourcing innovation. Production and Operations Management, 30(1), 103-126.

Chen, P. Y., Pavlou, P., Wu, S., & Yang, Y. (2021). Attracting high‐quality contestants to contest in the context of crowdsourcing contest platform. Production and Operations Management, 30(6), 1751-1771.

Cheng, X., Fu, S., De Vreede, T., De Vreede, G.-J., Seeber, I., Maier, R., & Weber, B. (2020). Idea convergence quality in open innovation crowdsourcing: A cognitive load perspective.

Journal of Management Information Systems, 37(2), 349-376.

Colicev, A., Hakkarainen, T., & Pedersen, T. (2023). Multi‐project work and project performance: Friends or foes? Strategic Management Journal, 44(2), 610-636.

Demirkan, H., & Spohrer, J. C. (2018). Commentary— cultivating T-shaped professionals in the era of digital transformation. Service Science, 10(1), 98-109.

Deng, X., Joshi, K. D., & Galliers, R. D. (2016). The duality of empowerment and marginalization in microtask crowdsourcing. MIS Quarterly, 40(2), 279-302.

Durward, D., Blohm, I., & Leimeister, J. M. (2020). The nature of crowd work and its effects on individuals’ work perception. Journal of Management Information Systems, 37(1), 66-95.

Feng, Y., Ye, H. J., Yu, Y., Yang, C., & Cui, T. (2018). Gamification artifacts and crowdsourcing participation: Examining the mediating role of intrinsic motivations. Computers in Human Behavior, 81, 124-136.

Fixson, S., & Marion, T. (2016). A case study of crowdsourcing gone wrong. Harvard Business Review. https://hbr.org/2016/12/a-case-studyof-crowdsourcing-gone-wrong

Gibson, C. B., & Birkinshaw, J. (2004). The antecedents, consequences, and mediating role of organizational ambidexterity. Academy of Management Journal, 47(2), 209-226.

Goes, P. B., Guo, C., & Lin, M. (2016). Do incentive hierarchies induce user effort? Evidence from on online knowledge exchange. Information Systems Research, 27(3), 497-516.

Gong, J., & Png, I. (2023). Automation enables specialization: Field evidence. Management Science, 70(3), 1580-1595

Granger, C. W. (1988). Some recent development in a concept of causality. Journal of Econometrics, 39(1-2), 199-211.

Greene, W. (2010). Testing hypotheses about interaction terms in nonlinear models. Economics Letters, 107(2), 291-296.

Haans, R. F., Pieters, C., & He, Z. L. (2016). Thinking about U: Theorizing and testing U‐and inverted U‐shaped relationships in strategy research. Strategic Management Journal, 37(7), 1177- 1195.

He, Z.-L., & Wong, P.-K. (2004). Exploration vs. exploitation: An empirical test of the ambidexterity hypothesis. Organization Science, 15(4), 481-494.

Heavey, C., & Simsek, Z. (2017). Distributed cognition in top management teams and organizational ambidexterity: The influence of transactive memory systems. Journal of Management, 43(3), 919-945.

Heckman, J. (1974). Shadow prices, market wages, and labor supply. Econometrica, 42(4), 679-694.

Heckman, J. J. (1976). The common structure of statistical models of truncation, sample selection and limited dependent variables and a simple estimator for such models. Annals of economic and social measurement, 5(4), 475- 492).

Hofstetter, R., Dahl, D. W., Aryobsei, S., & Herrmann, A. (2021). Constraining Ideas: How Seeing Ideas of Others Harms Creativity in Open Innovation. Journal of Marketing Research, 58(1), 95-114.

Huang, N., Burtch, G., Gu, B., Hong, Y., Liang, C., Wang, K., Fu, D., & Yang, B. (2018). Motivating usergenerated content with performance feedback: Evidence from randomized field experiments. Management Science, 65(1), 327-345.

Huang, Y., Singh, P. V., & Srinivasan, K. (2014). Crowdsourcing New Product Ideas Under Consumer Learning. Management Science, 60(9), 2138-2159.

Im, G., & Rai, A. (2008). Knowledge Sharing Ambidexterity in Long-Term Interorganizational Relationships. Management Science, 54(7), 1281-1296.

Jansen, J. J., Simsek, Z., & Cao, Q. (2012). Ambidexterity and performance in multiunit contexts: Crosslevel moderating effects of structural and resource attributes. Strategic Management Journal, 33(11), 1286-1303.

Jeppesen, L. B., & Lakhani, K. R. (2010). Marginality and problem solving effectiveness in broadcast search. Organization Science 21(5), 1016-1033.

Jian, L., Ba, S., Lu, L., Jiang, L. C., & Yang, S. (2019). Managing the crowds: The effect of prize guarantees and in-process feedback on participation in crowdsourcing contests. MIS Quarterly, 43(1), 97-112.

Jiang, J., & Wang, Y. (2020). A theoretical and empirical investigation of feedback in ideation contests. Production and Operations Management, 29(2), 481-500.

Jiang, Z. Z., Huang, Y., & Beil, D. R. (2022). The role of feedback in dynamic crowdsourcing contests: A structural empirical analysis. Management Science, 68(7), 4755-5555.

Jin, Y., Lee, H. C. B., Ba, S., & Stallaert, J. (2021). Winning by Learning? Effect of Knowledge Sharing in Crowdsourcing Contests. Information Systems Research, 32(3), 675-1097.

Karaca‐Mandic, P., Norton, E. C., & Dowd, B. (2012). Interaction terms in nonlinear models. Health Services Research, 47(1.1), 255-274.

Kc, D. S. (2014). Does multitasking improve performance? Evidence from the emergency department. Manufacturing & Service Operations Management, 16(2), 168-183.

Keller, T., & Weibler, J. (2015). What it takes and costs to be an ambidextrous manager: Linking leadership and cognitive strain to balancing exploration and exploitation. Journal of Leadership & Organizational Studies, 22(1), 54-71.

Kiss, A. N., Libaers, D., Barr, P. S., Wang, T., & Zachary, M. A. (2020). CEO cognitive flexibility, information search, and organizational ambidexterity. Strategic Management Journal, 41(12), 2200-2233.

Kobarg, S., Wollersheim, J., Welpe, I. M., & Spörrle, M. (2017). Individual ambidexterity and performance in the public sector: A multilevel analysis. International Public Management Journal, 20(2), 226-260.

Koh, T. K. (2019). Adopting seekers’ solution exemplars in crowdsourcing ideation contests: antecedents and consequences. Information Systems Research, 30(2), 486-506.

Koh, T. K., & Cheung, M. Y. (2022). Seeker Exemplars and Quantitative Ideation Outcomes in Crowdsourcing Contests. Information Systems Research, 33(1), 265-284.

Kotler, S. (2021). Why a free afternoon each week can boost employees’ sense of autonomy. Fastcompany. https://www.fastcompany.com 90595295/why-a-free-afternoon-each-weekcan-boost-employees-sense-of-autonomy

Kristal, M. M., Huang, X., & Roth, A. V. (2010). The effect of an ambidextrous supply chain strategy on combinative competitive capabilities and business performance. Journal of Operations Management, 28(5), 415-429.

Laureiro‐Martínez, D., Brusoni, S., Canessa, N., & Zollo, M. (2015). Understanding the exploration–

exploitation dilemma: An fMRI study of attention control and decision‐making performance. Strategic Management Journal, 36(3), 319-338.

Leroy, S., & Glomb, T. M. (2018). Tasks interrupted: How anticipating time pressure on resumption of an interrupted task causes attention residue and low performance on interrupting tasks and how a “ready-to-resume” plan mitigates the effects. Organization Science, 29(3), 380-397.

Liang, H., Wang, N., & Xue, Y. (2022). Juggling information technology (IT) exploration and exploitation: A proportional balance view of IT ambidexterity. Information Systems Research, 33(4), 1386-1402.

Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U‐shaped relationship. Oxford Bulletin of Economics and Statistics, 72(1), 109-118.

Liu, T. X., Yang, J., Adamic, L. A., & Chen, Y. (2014). Crowdsourcing with all-pay auctions: A field experiment on taskcn. Management Science, 60(8), 2020-2037.

Liu, Z., Hatton, M. R., Kull, T., Dooley, K., & Oke, A. (2021). Is a large award truly attractive to solvers? The impact of award size on crowd size in innovation contests. Journal of Operations Management, 67(4), 420-449.

Luger, J., Raisch, S., & Schimmer, M. (2018). Dynamic balancing of exploration and exploitation: The contingent benefits of ambidexterity. Organization Science, 29(3), 449-470.

Lysyakov, M., & Viswanathan, S. (2023). Threatened by AI: Analyzing Users’ Responses to the Introduction of AI in a Crowd-sourcing Platform. Information Systems Research, 34(3), 1191-1210.

Mamykina, L., Smyth, T. N., Dimond, J. P., & Gajos, K. Z. (2016). Learning from the Crowd: Observational Learning in Crowdsourcing Communities. Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems..

March, J. G. (1991). Exploration and Exploitation in Organizational Learning. Organization Science, 2(1), 71-87.

Martinez, M. G. (2015). Solver engagement in knowledge sharing in crowdsourcing communities: Exploring the link to creativity. Research Policy, 44(8), 1419-1430.

Martinez, M. G. (2017). Inspiring crowdsourcing communities to create novel solutions: Competition design and the mediating role of trust. Technological Forecasting and Social Change, 117, 296-304.

McCrae, R., & Costa, P., Jr. (1990). Personality in adulthood. Personality in adulthood. Guilford Press.

McCrae, R. R., & Costa, P. T. (1987). Validation of the five-factor model of personality across instruments and observers. Journal of Personality and Social Psychology, 52(1), 81-90.

Menon, N., Mishra, A., & Ye, S. (2020). Beyond Related Experience: Upstream vs. Downstream Experience in Innovation Contest Platforms with Interdependent Problem Domains. Manufacturing & Service Operations Management, 22(5), 1045-1065.

Mo, J., Sarkar, S., & Menon, S. (2018). Know When to Run: Recommendations in Crowdsourcing Contests. MIS Quarterly 42(3), 919-944.

Mo, J., Sarkar, S., & Menon, S. (2021). Competing tasks and task quality: An empirical study of crowdsourcing contests. MIS Quarterly, 45(4), 1921-1948.

Mom, T. J., Chang, Y.-Y., Cholakova, M., & Jansen, J. J. (2019). A multilevel integrated framework of firm HR practices, individual ambidexterity, and organizational ambidexterity. Journal of Management, 45(7), 3009-3034.

Mom, T. J., Fourné, S. P., & Jansen, J. J. (2015). Managers’ work experience, ambidexterity, and performance: The contingency role of the work context. Human Resource Management, 54(S1), s133-s153.

Mom, T. J., van den Bosch, F. A., & Volberda, H. W. (2007). Investigating managers’ exploration and exploitation activities: The influence of topdown, bottom‐up, and horizontal knowledge inflows. Journal of Management Studies, 44(6), 910-931.

Mom, T. J., Van Den Bosch, F. A., & Volberda, H. W. (2009). Understanding variation in managers' ambidexterity: Investigating direct and interaction effects of formal structural and personal coordination mechanisms. Organization Science, 20(4), 812-828.

Nevo, D., & Kotlarsky, J. (2020). Crowdsourcing as a strategic IS sourcing phenomenon: Critical review and insights for future research. Journal of Strategic Information Systems, 39, 1-22.

Nijstad, B. A., De Dreu, C. K., Rietzschel, E. F., & Baas, M. (2010). The dual pathway to creativity model: Creative ideation as a function of flexibility and persistence. European Review of Social Psychology, 21(1), 34-77.

O’Reilly, C. A., III, & Tushman, M. L. (2013). Organizational ambidexterity: Past, present, and future. Academy of Management Perspectives, 27(4), 324-338.

Ossenbrink, J., Hoppmann, J., & Hoffmann, V. H. (2019). Hybrid ambidexterity: How the environment shapes incumbents’ use of structural and contextual approaches. Organization Science, 30(6), 1319-1348.

Papanastasiou, Y., Bimpikis, K., & Savva, N. (2018). Crowdsourcing exploration. Management Science, 64(4), 1727-1746.

Pertusa-Ortega, E. M., Molina-Azorín, J. F., Tarí, J. J., Pereira-Moliner, J., & López-Gamero, M. D. (2020). The microfoundations of organizational ambidexterity: A systematic review of individual ambidexterity through a multilevel framework. Business Research Quarterly, 23, 1-17.

Piezunka, H., & Dahlander, L. (2015). Distant search, narrow attention: How crowding alters organizations’ filtering of suggestions in crowdsourcing. Academy of Management Journal, 58(3), 856-880.

Pongratz, H. J. (2018). Of crowds and talents: discursive constructions of global online labour. New Technology, Work and Employment, 33(1), 58- 73.

Posen, H. E., & Levinthal, D. A. (2012). Chasing a moving target: Exploitation and exploration in dynamic environments. Management Science, 58(3), 587-601.

Prpić, J., Taeihagh, A., & Melton, J. (2015). The fundamentals of policy crowdsourcing. Policy & Internet, 7(3), 340-361.

Puranam, P., Stieglitz, N., Osman, M., & Pillutla, M. M. (2015). Modelling bounded rationality in organizations: Progress and prospects. Academy of Management Annals, 9(1), 337-392.

Raisch, S., & Birkinshaw, J. (2008). Organizational ambidexterity: Antecedents, outcomes, and moderators. Journal of Management, 34(3), 375-409.

Riedl, C., & Seidel, V. P. (2018). Learning from Mixed Signals in Online Innovation Communities. Organization Science, 29(6), 1010-1032.

Rietveld, J., Schilling, M. A., & Bellavitis, C. (2019). Platform strategy: Managing ecosystem value through selective promotion of complements. Organization Science, 30(6), 1232-1251.

Roberts, N., Qahri-Saremi, H., & Vijayasarathy, L. R. (2021). Understanding IT value at the managerial level: Managerial ambidexterity, seizing opportunities, and the moderating role of information systems use. The Data Base for Advances in Information Systems, 52(3), 39-55.

Rossi, P. E. (2014). Even the rich can make themselves poor: A critical examination of IV methods in marketing applications. Marketing Science, 33(5), 655-672.

Schenk, E., & Guittard, C. (2011). Towards a characterization of crowdsourcing practices. Journal of Innovation Economics Management, 7(1), 93-107.

Schnellbächer, B., Heidenreich, S., & Wald, A. (2019). Antecedents and effects of individual ambidexterity–A cross-level investigation of exploration and exploitation activities at the employee level. European Management Journal, 37(4), 442-454.

Simon, H. A. (1972). Theories of bounded rationality. Decision and organization, 1(1), 161-176.

Smith, W. K., & Tushman, M. L. (2005). Managing strategic contradictions: A top management model for managing innovation streams. Organization Science, 16(5), 522-536.

Staats, B. R., & Gino, F. (2012). Specialization and variety in repetitive tasks: Evidence from a Japanese bank. Management Science, 58(6), 1141-1159.

Stock, J., & Yogo, M. (2002). Testing for weak instruments in linear IV regression (Technical Working Paper 284). National Bureau of Economic Research.

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. Cognitive Science, 12(2), 257-285.

Ta, H., Esper, T. L., & Tokar, T. (2021). Appealing to the crowd: Motivation message framing and crowdsourcing performance in retail operations. Production and Operations Management, 30(9), 3192-3212.

Tempelaar, M. P., & Rosenkranz, N. A. (2019). Switching hats: The effect of role transition on individual ambidexterity. Journal of Management, 45(4), 1517-1539.

Wang, J., Ipeirotis, P., & Provost, F. (2017). Cost-effectie quality assurance in crowd-labeling. Information Systems Research, 28(1), 137-158.

Werder, K., & Heckmann, C. S. (2019). Ambidexterity in information systems research: Overview of conceptualizations, antecedents, and outcomes. Journal of Information Technology Theory and Application, 20(1), 28-52.

Wooldridge, J. M. (2010). Econometric analysis of cross section and panel data. MIT Press.

Ye, H., & Kankanhalli, A. (2015). Investigating the antecedents of organizational task crowdsourcing. Information & Management, 52(1), 98-110.

Ye, H. J., & Kankanhalli, A. (2017). Solvers’ participation in crowdsourcing platforms: Examining the impacts of trust, and benefit and cost factors. The Journal of Strategic Information Systems, 26(2), 101-117.

Ye, J., & Jensen, M. (2022). Effects of introducing an online community in a crowdsourcing contest platform. Information Systems Journal, 32(6), 1203-1230.

Zhang, S., Singh, P. V., & Ghose, A. (2019). A structural analysis of the role of superstars in crowdsourcing contests. Information Systems Research, 30(1), 15-33.

Zheng, H., Li, D., & Hou, W. (2011). Task design, motivation, and participation in crowdsourcing contests. International Journal of Electronic Commerce, 15(4), 57-88.

## Appendix A: Literature Review

To gain a better understanding of current knowledge in the literature, we conducted a review of empirical research on solver performance in crowdsourcing contests. We performed a Google Scholar search using the search terms “crowdsourcing,” “contests,” and “performance.” We limited our results to publications in the Financial Times 50 journals from 2010 to date. The search yielded a total of 155 papers. We then reviewed the abstracts of each of these papers and removed ones that did not include original research or any data analysis. We also excluded papers that did not address solver performance. Eleven papers that are conceptually proximal to our phenomenon of interest remained (see Table A1).

Table A1. Empirical Research on Solver Performance

<table><tr><td>Reference</td><td>Dependent Variable</td><td>Context</td><td>Independent variables</td><td>Effects of exploration?</td><td>Effects of exploitation?</td><td>Effects of ambidexterity?</td><td>Moderators?</td></tr><tr><td>Jeppesen &amp; Lakhani (2010)</td><td>·Likelihood of winning</td><td>InnoCentive</td><td>Technical marginality (expertise distance), social marginality (gender)</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Bayus (2013)</td><td>·Likelihood of proposing an implemented idea·Likelihood of proposing diverse ideas</td><td>Dell&#x27;s IdeaStorm</td><td>The number of past implemented ideas, diversity of past commenting activity</td><td>Yes: exploration as diversity of past commenting</td><td>Yes: exploitation as number of past implemented ideas</td><td>No</td><td>No</td></tr><tr><td>Lee et al. (2018)</td><td>·Prediction accuracy of the submitted algorithm</td><td>Kaggle</td><td>Salience bias</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Riedl &amp; Seidel (2018)</td><td>·Crowd-rated scores of submissions·Likelihood of winning</td><td>Threadless</td><td>Prior submissions and prior ratings of peer submissions</td><td>No</td><td>Yes: prior submissions</td><td>No</td><td>No</td></tr><tr><td>Cheng et al. (2020)</td><td>·Idea convergence quality by raters: task relevance and idea development</td><td>Lab experiment using ideas from OpenIDEO</td><td>Intrinsic cognitive load, extraneous cognitive load, and germane cognitive load</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Menon et al. (2020)</td><td>·Peer-reviewed code accuracy score</td><td>TopCoder</td><td>Related experience, unrelated experience, upstream experience, and downstream experience</td><td>Yes: exploration as unrelated experience</td><td>Yes: exploitation as related experience</td><td>No</td><td>Yes: Contest duration</td></tr><tr><td>Althuizen &amp; Chen (2022)</td><td>·Idea novelty by judges·Idea appropriateness by judges</td><td>Lab experiment</td><td>Prototype&#x27;s level of enhancement and product design goal</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Chan et al. (2021)</td><td>·Crowd-voted idea quality (popularity and attractiveness)</td><td>Dell&#x27;s IdeaStorm</td><td>Feedback valence feedback source</td><td>No</td><td>No</td><td>No</td><td>Yes: ideation experience</td></tr><tr><td>Hofstetter et al. (2021)</td><td>·Top-box innovativeness: composite measure with idea originality and usefulness</td><td>Field and lab experiments</td><td>Exposure to prior ideas and competitive presentation</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Mo et al. (2021)</td><td>·Solution quality score by seeker firms</td><td>CrowdSpring</td><td>Competing tasks, multi-tasking level, multi-tasking similarity</td><td>No</td><td>No</td><td>Discuss multi-tasking and task-switching - related, but differs from ambidexterity</td><td>Yes: task similarity</td></tr><tr><td>Koh &amp; Cheung (2022)</td><td>·Quantity of images searched, listed, and submitted·Image quality (composite measure: novelty, feasibility, attractiveness)</td><td>Lab experiment on photo contest</td><td>Local exemplars, mixed exemplars, and distant exemplars</td><td>No</td><td>No</td><td>No</td><td>No</td></tr></table>

## Appendix B. Website Information and Ambidexterity Calculation

Please find the contest categories on the website in Table B1. We coded the 7 categories as the task types. Within each category, there are subcategories. Solvers are required to choose their skills by selecting the subcategories’ keywords on the crowdsourcing site. For example, in Figure B1, the solver’s skillset keywords overlap with contest Categories 1 and 4 in Table B1.

Table B1. Contest Categories (Task Types) and Subcategories (Skills)

<table><tr><td>Contest categories</td><td>Subcategories</td></tr><tr><td>(1) Identification design</td><td>Logo design, brand slogan/identity design, virtual identity (VI) pamphlet design, font design, avatar design; mascot design; trademarks design;</td></tr><tr><td>(2) Package design</td><td>Packaging box/bag design, illustration packaging, bottle label design, gift package design storefront /interior design</td></tr><tr><td>(3) Animation/game design</td><td>Cartoon design, Cartoon avatar/character design, emoji design, game icon character modeling and design, game animation</td></tr><tr><td>(4) Promotional strategy/design</td><td>Brochure design, poster design, flyer/menu design; billboard design, book cover/album design; online advertising image, inkjet photo design; product/promotion strategy, guide design; direct mail (DM) form design</td></tr><tr><td>(5) Office design (writing related)</td><td>PPT customization, business cards, business plans, brand case planning/writing, advertising plans, marketing campaign plans, feasibility report, brand/enterprise naming</td></tr><tr><td>(6) IT/Software design</td><td>App development, WeChat Mini apps, Mini apps for TikTok, catering apps design, iOS app, Android app, mobile game apps development</td></tr><tr><td>(7) Website/webpage design</td><td>Corporate website, e-commerce website, web portals, marketing website, website UI design, app interface</td></tr></table>

![](/api/attachments/SEZJ6KQZ/fulltext/images/0a66b6860aee31d987206c1a19e4eed5211000b8b50314afa57fc3c66df0854e.jpg)  
Figure B1. Skills specified in Example Solver’s Profile

## Mapping Between a Specific Contest and the Skills Listed in Solvers’ Profiles

Take the contest in Figure B2, for example. The contest belongs to Category 1 since it is about brand identity design and VI design.

Solver 1 (“Pleased”) has skills related to Category 4 (i.e., product/promotion strategy) and Category 5 (i.e., brand case planning, brand/enterprise naming) but not related to Category 1. Thus, this submission is coded as exploration for Solver 1.

Solver 2 (“星龙设计”) has the skills of brand design and logo design related to Category 1, the same as the contest category. Hence, this submission is coded as exploitation for Solver 2.

![](/api/attachments/SEZJ6KQZ/fulltext/images/d071be6117a308309fff9ab1e5cf8a9233191a1936c5b1320ebf9854778972f6.jpg)  
Figure B2. Contest and Solver Examples

## Calculation of Task Diversity, Exploration, and Exploitation

For example, for the earlier solver in Figure B1, contests of Categories 1 and 4 are within the solver’s stated skillset.

The number of task types is calculated based on the seven categories to compute task diversity.

Within a month, the above solver has submitted to 10 contests, among which five contests belong to Category 1, three to Category 4, and two to Category 3.

Then, the task diversity is computed as:

$$
- \sum_ {i j} p _ {i j} \ln (p _ {i j}) = - [ 5 / 1 0 \ln (5 / 1 0) + 3 / 1 0 \times \ln (3 / 1 0) + 2 / 1 0 \times \ln (2 / 1 0) ] = 0. 4 4 7 1
$$

Exploitation (EPT) was measured by the number of tasks undertaken that were within the broad category of skills listed on the solver’s profile in month t.

Exploration (EPR) was measured by the number of tasks undertaken that were not within the broad category of skills list on the solver’s profile in month t.

Thus, exploration for this solver EPR = 2, whereas exploitation EPT = 5+3 = 8.

## Appendix C. Results of Robustness Checks

## First Stage of Heckman Selection Estimation

Results of the first stage of Heckman selection estimation are shown in Table C1. j refers to the contest. Scores of the inverse Mills ratio from the solver-contest data were averaged to construct the score for the solver-month data. Results for the first stage of instrumental variable estimation are shown in Table C2.

Table C1. Results of the First Stage of Heckman Selection Estimation

<table><tr><td>DV = if submit ij</td><td colspan="2">Stage 1 of Heckman selection bias model</td></tr><tr><td></td><td>Coefficient</td><td>Robust SE</td></tr><tr><td>Ln(total available  $contests_t + 1$ )</td><td>-0.094*</td><td>0.039</td></tr><tr><td>Ln (total available contests of a particular  $type_t + 1$ )</td><td>-0.118*</td><td>0.042</td></tr><tr><td>Ln(task  $reward_{ij} + 1$ )</td><td>0.161***</td><td>0.031</td></tr><tr><td>If preferred  $task_j$ </td><td>0.155***</td><td>0.007</td></tr><tr><td>Ln(number of other registered solvers $_j$  + 1)</td><td>-0.136**</td><td>0.054</td></tr><tr><td>Solver rating  $_{ij}$ </td><td>0.133*</td><td>0.060</td></tr><tr><td>Average rating of other registered solvers $_j$ </td><td>-0.165*</td><td>0.074</td></tr><tr><td>Pseudo  $R^2$ </td><td colspan="2">0.251</td></tr><tr><td>Fixed effects</td><td colspan="2">Yes</td></tr><tr><td>Month dummies</td><td colspan="2">Included</td></tr><tr><td> $\chi^2 (df)$ </td><td colspan="2">2236.23 (38)</td></tr><tr><td>Number of observations</td><td colspan="2">158,125</td></tr></table>

Table C2. First Stage Results of Instrumental Variable Estimation

<table><tr><td rowspan="2"></td><td colspan="2">DV = Ln (ambidexterity + 1)</td><td colspan="2">DV = Ln(ambidexterity + 1) $^2$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Ln(average description length $_{it}$  + 1)</td><td>0.241 (0.019) ***</td><td>0.084 (0.018) ***</td><td>0.020 (0.005)***</td><td>0.016 (0.005)**</td></tr><tr><td>Ln (total available contest $_t$  + 1)</td><td></td><td>2.280 (0.096) ***</td><td>0.453 (0.027)***</td><td>5.872 (0.470)***</td></tr><tr><td>Ln (total available contest $_t$  + 1) $^2$ </td><td></td><td></td><td></td><td>-1.387 (0.119)***</td></tr><tr><td>Ln(contest reward $_{it}$  + 1)</td><td>0.075 (0.005) ***</td><td>0.029 (0.006) ***</td><td>0.005 (0.001)**</td><td>0.005 (0.001)***</td></tr><tr><td>Ln(contest competition $_{it}$  + 1)</td><td>0.113 (0.049)*</td><td>0.145 (0.045)*</td><td>0.021 (0.012)</td><td>0.023 (0.012)</td></tr><tr><td>Ln(contestant level $_{ii}$  + 1)</td><td>-0.155 (0.065)*</td><td>-0.031 (0.062)</td><td>-0.000 (0.016)</td><td>-0.001 (0.016)</td></tr><tr><td>Ln(platform tenure $_{it}$  + 1)</td><td>-0.130 (0.085)</td><td>-0.137(0.080)</td><td>-0.045 (0.021)*</td><td>-0.032 (0.021)</td></tr><tr><td> $R^2$ </td><td>0.100</td><td>0.189</td><td>0.115</td><td>0.145</td></tr><tr><td>Fixed effects</td><td colspan="4">Yes</td></tr><tr><td>Observations</td><td colspan="4">71,257</td></tr></table>

## Granger Causality Test

The Granger causality test (Granger, 1980) was performed with two lags, when AIC is lowest. The results in Table C3 suggest that ambidexterity Granger caused solver performance, which is consistent with our main findings. Also, task diversity and task reward Granger caused solver performance, which was consistent with prior literature (Bayus, 2013; Liu et al., 2021).

Table C3. Granger Causality Test Result

<table><tr><td rowspan="2"></td><td colspan="5">Dependent variables</td></tr><tr><td>PER</td><td>AMB</td><td>TDV</td><td>IPF</td><td>TRW</td></tr><tr><td>PER</td><td>-</td><td>0.022</td><td>0.021</td><td>0.010</td><td>0.055</td></tr><tr><td>AMB</td><td>0.333**</td><td>-</td><td>0.035</td><td>0.025</td><td>0.015</td></tr><tr><td>TDV</td><td>0.030*</td><td>0.011</td><td>-</td><td>0.110</td><td>0.021</td></tr><tr><td>IPF</td><td>0.011</td><td>-0.032</td><td>0.030</td><td>-</td><td>-0.022</td></tr><tr><td>TRW</td><td>0.117*</td><td>0.035</td><td>0.051</td><td>0.023</td><td>-</td></tr></table>

![](/api/attachments/SEZJ6KQZ/fulltext/images/967cbc585ecd66fab38422a9914ad076f64ce9e9658f15f1a3c53d0d63eee0bb.jpg)  
Figure C1. Average Task Reward by Exploitation and Exploration across Time

## About the Authors

Hua (Jonathan) Ye is an associate professor in the MIS Division of the Price College of Business at the University of Oklahoma. His research interests include generative AI, AI-generated content, crowdsourcing, and service innovation. His research appears in top journals, including MIS Quarterly, Production and Operations Management, Journal of Management Information Systems, Journal of the Association for Information Systems, among others, and in the proceedings of premium conferences. He has been serving as an associate editor for the European Journal of Information Systems.

Atreyi Kankanhalli is Provost’s Chair Professor at the Department of Information Systems and Analytics, National University of Singapore. She is co-director of the Centre for Computational Social Science and Humanities. She conducts research on online communities, human-AI collaboration, and digital innovation with a focus on healthcare. Her work has appeared in premium journals and has been highly cited. She serves or has served on the editorial boards of Information Systems Research (senior and associate editor), MIS Quarterly (senior and associate editor), and Journal of the Association for Information Systems (senior editor) among others. She has been ICIS doctoral consortium cochair, ICIS program co-chair, PACIS program co-chair, and AIS vice president for Region 3. She received the ACM-SIGMIS Best Doctoral Dissertation award, AIS Sandra Slaughter Service Award and was recognized as AIS Fellow. Her awards for broader impact include the IBM Faculty Award, the Singapore 100 Women in Tech Award, and the Asia Women Tech Leaders Award.

Bernard C. Y. Tan is senior vice provost at the National University of Singapore (NUS), where he chairs the university curriculum committee. He is Shaw Professor in the Department of Information Systems and Analytics at NUS. He is a recipient of university awards for research and teaching and a recipient of the NUS Outstanding Computing Alumni Award. He was the 15th President of the Association for Information Systems (AIS). He is a recipient of the AIS LEO Award, the AIS Fellow Award, and the AIS Sandy Slaughter Service Award. He has served on the editorial boards of MIS Quarterly (senior editor), Journal of the Association for Information Systems (senior editor), IEEE Transactions on Engineering Management (department editor), Management Science (associate editor), ACM Transactions on Management Information Systems (associate editor), and Journal of Management Information Systems (editorial board member). He has served as ICIS doctoral consortium co-chair, ICIS program co-chair, ICIS junior faculty consortium co-chair, and ICIS awards co-chair and will serve as the ICIS conference co-chair (in 2025). His research has been published in various journals and conference proceedings in the field of information systems.

Copyright © 2025 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
