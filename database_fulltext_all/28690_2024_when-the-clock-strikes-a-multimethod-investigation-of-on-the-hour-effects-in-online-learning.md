---
otero_id: 28690
otero_key: "HA7Z7WGM"
title: "When the Clock Strikes: A Multimethod Investigation of On-the-Hour Effects in Online Learning"
authors: "Ni Huang; Lingli Wang; Yili Hong; Lihui Lin; Xunhua Guo; Guoqing Chen"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.1234"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# When the Clock Strikes: A Multimethod Investigation of On-the-Hour Effects in Online Learning

Ni Huang,<sup>a</sup> Lingli Wang,<sup>b,</sup>\* Yili Hong,<sup>a</sup> Lihui Lin,<sup>c</sup> Xunhua Guo,<sup>c</sup> Guoqing Chen

<sup>a</sup> Miami Herbert Business School, University of Miami, Coral Gables, Florida 33146; <sup>b</sup> School of Modern Post, Beijing University of Posts and Telecommunications, Beijing 100876, China; <sup>c</sup> School of Economics and Management, Tsinghua University, Beijing 100084, Chin \*Corresponding author

Contact: nhuang@miami.edu, https://orcid.org/0000-0003-3416-513X (NH); wang.ll@bupt.edu.cn, https://orcid.org/0000-0002-8405-6196 (LW); khong@miami.edu, https://orcid.org/0000-0002-0577-7877 (YH); linlh@sem.tsinghua.edu.cn, https://orcid.org/0000-0003-0695-5214 (LL); guoxh@tsinghua.edu.cn (XG); chengq@sem.tsinghua.edu (GC)

Received: September 15, 2020 Revised: August 8, 2021; May 11, 2022; January 15, 2023 Accepted: February 6, 2023 Published Online in Articles in Advance: June 7, 2023

https://doi.org/10.1287/isre.2023.1234

Copyright: © 2023 INFORMS

Abstract. Online learners often experience a lack of sustained motivation given the selfpaced nature of online learning, resulting in inefficiency and a high dropout rate. Therefore, it is important to explore options that help users optimize their learning behavior and improve their learning performance. This study proposes that on-the-hour time points as external temporal cues can significantly influence online learning outcomes. Using a multimethod approach (i.e., archival data analysis, laboratory experiments, and framed field experiments), we show that (a) starting learning sessions at on-the-hour time points acti vates users’ implemental mindset, which supports them in building greater learning persistence and achieving better learning performance, and (b) social presence significantly attenuates the effects of on-the-hour time points in online learning. Our findings add to the literature on the design of online learning systems by clarifying the effects of temporal cue in user-system interactions, which provides implications for notification and reminder strategies that can be implemented to further enhance the effectiveness of online learning.

History: Juan Feng, Senior Editor; David (Jingjun) Xu, Associate Editor.

Funding: This work was supported by the National Natural Science Foundation of China [Grants 72201038 and 72293561], the Beijing University of Posts and Telecommunications Basic Scientific Research Program [Grant 2022RC21], the Tsinghua University Initiative Scientific Research Program [Grant 2019THZWYX08], the Research Center for Interactive Technology Industry of Tsinghua University [Grant RCITI2022T002], and the New Liberal Arts Program of the Ministry of Education in China [Grant 2021090003].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.1234.

Keywords: online learning systems • temporal cues • learning outcomes • social presence

## 1. Introduction

Online learning—also referred to as technology-mediated learning and e-learning—helps individuals acquire knowledge via information technology platforms virtually anywhere and anytime, and it is therefore of great interest to information systems (IS) researchers. According to ThinkImpact, the global online learning market is expected to experience a compound annual growth rate of 8% between 2020 and 2025 and will be valued at approximately \$375 billion by 2026.<sup>1</sup> Although online learning has been considered a cost-effective way to deliver education to large numbers of students at convenient times and locations (Santhanam et al. 2008), studies also suggest that it does not provide the anticipated benefits because many online learners struggle with self-control problems (Kizilcec and Halawa 2015) and are not motivated enough to learn (Brown 2001, Bell and Kozlowski 2002), leading to a high dropout rate and inefficient learning (Santhanam et al. 2008, Nawrot and Doucet 2014, Kizilcec et al. 2017).

Recently, IS scholars have started to explore how to leverage technology-based interventions and designs (e.g., feedback, instructions, and reminders) to help users en gage in learning activities and to enhance learning out comes (Santhanam et al. 2008, Liu et al. 2017, Huang et al. 2020). However, prior research has not considered the effects of an important environmental factor, namely temporal cues—time points that demarcate the beginning of new time cycles (Dai et al. 2014). Temporal cues are important in this context because time management is essential for learning, and these cues are likely to induce users to implement goal-directed behavior (Dai et al. 2014). For instance, salient temporal cues, such as the beginning of a year, month, or week, can motivate individuals to take action to pursue aspirational goals, such as searching for “diet” information on Google and committing to pursue goals on a goal-setting website (Dai et al. 2014, Sellier and Avnet 2014, Rai et al. 2016, Duckworth et al. 2018). As online learning systems remove the temporal restrictions on learning activities (e.g., learners can use mobile devices to learn anywhere at any time), it remains an interesting empirical question whether temporal cues can affect online learners’ learning activities and outcomes.

Grounding on the mindset theory (Gollwitzer 1990, Tu and Soman 2014), this work aims to explore the effects of one typical temporal cue, on-the-hour time points, as they are salient reference points for time management and individuals’ goal-directed behavior (Allen et al. 2017). We begin with exploring the direct impacts of on-the-hour time points on users’ online learning outcomes. In particular, we theorize that on-the-hour time points as temporal cues can help activate learners implemental mindset, which supports them in learningdirected behavior (Gollwitzer and Keller 2016). Further, we explore how on-the-hour time points influence user behavior in online learning with the provision of social presence (Gunawardena and Zittle 1997, Cobb 2009, Zhan and Mei 2013, Richardson et al. 2017), the recent introduction of which in online learning systems supports users in learning together in virtual environments.<sup>2</sup> Specifically, we conjecture that a higher level of social presence drives users to concentrate on implementing learning-directed behavior (Zajonc 1965) while attenuating the potential impacts of external temporal cues (Huguet et al. 1999, Muller and Butera 2007). Formally, we seek to address the following research questions.

Whether and how do on-the-hour time points influence users’ online learning persistence and performance? How does social presence moderate the effects of on-the-hour time points in online learning?

We answer these research questions using a multimethod approach with four studies. First, an analysis of archival data from an online learning mobile app in Study 1 revealed correlational evidence that users who start learning at on-the-hour time points (versus other time points) appear to have better overall learning performance. Second, a laboratory experiment in Study 2 revealed that on-the-hour time points (versus other time points) as external temporal cues lead to greater learning persistence and increased learning performance among participants in online learning. Third, a framed field experiment in Study 3 replicated the laboratory experiment and showed largely consistent findings, adding to the external validity of the results in the laboratory scenario. Furthermore, Study 4 explored plausible mechanisms and the moderating role of social presence in online learning. We find that users who begin learning at on-the-hour time points (versus other time points) appear to have a stronger implemental mindset, which then supports them in persisting longer and achieving higher learning performance. We also find that social presence significantly attenuates the impact of on-the-hour effects on online learning outcomes.

Our work contributes to the related literature in several ways. To begin with, we advance the literature on designing online learning systems by examining an external factor, namely on-the-hour time points. Previous studies have mainly focused on how learner charac teristics, technology features, and instructional strategies affect learners’ psychological processes and learning outcomes (Alavi and Leidner 2001, Santhanam et al. 2008, Gupta and Bostrom 2009, Huang et al. 2020). Our paper extends the related literature by investigating the effects of important intraday temporal cues, proposing and testing the mechanisms based on the mindset theory. Second, in extending the mindset theory to the online learning context (Gollwitzer 1990, Zhao et al. 2012, Tu and Soman 2014), our work reveals that on-thehour time points are important cues that can trigger a stronger implemental mindset in using learning systems, which further supports users to persist longer and to achieve better learning performance. Third, our find ings speak to the research stream on social presence in online learning. Although previous studies have ex plored Information Technology (IT) based designs that are enhanced by social presence (Gunawardena and Zittle 1997, Cobb 2009, Zhan and Mei 2013, Richardson et al. 2017), we demonstrate that social presence is an important moderating factor for on-the-hour effects in online learning.

This paper also offers multiple practical implications for users and operators of online learning platforms. Specifically, online learning platform users can leverage the on-the-hour effects to help themselves implement learning-directed behavior and thus, improve their online learning performance. At the same time, online learning platform operators can consider designing a reminder system that sends notifications to users that emphasize both the study start time and learning goals to increase users’ learning persistence. Finally, as users might start learning at random time points during a day, online learning platforms might introduce a functional design to allow users to virtually connect to other learners (e.g., a virtual study room).

## 2. Literature Review

## 2.1. Online Learning and Temporal Cues

Online learning is a popular form of technologymediated learning, in which information technology is used to mediate and support self-paced learning activi ties (Santhanam et al. 2008). It is believed to be a costeffective way of supporting large numbers of users to learn at convenient times and remote locations (Zhang et al. 2004, Santhanam et al. 2008, Huang et al. 2020). The literature on online learning or technology-mediated learning has demonstrated that factors related to learner characteristics (e.g., self-efficacy), learning context (e.g., learning goals), technology-based system designs (e.g., communication support), and instructional strategies (e.g., goal emphasis) have direct effects on learning outcomes (Alavi and Leidner 2001, Gupta and Bostrom

2009). Meanwhile, in online learning environments, one major challenge is that learners might feel isolated and disconnected from peers and instructors (Santhanam et al. 2008, Richardson et al. 2017) and at the same time, are exposed to various digital temptations that inadvertently lead to distractions (Lavoie and Pychyl 2001, Thatcher et al. 2008). Therefore, online learners often fai to exercise high levels of self-control, nor do they adequately self-motivate their learning, which results in a high dropout rate (Brown 2001, Bell and Kozlowski 2002, Zhang et al. 2004, Kizilcec and Halawa 2015) and ineffective learning (Nawrot and Doucet 2014, Kizilcec et al. 2017).

In contexts such as online learning that require individuals to exercise self-control and to discipline themselves to implement goal-directed activities, scholars often pay attention to factors that directly affect users self-control behavior. For example, prior studies suggest that self-control behavior can be affected by temporal cues (Dai et al. 2014, 2015; Duckworth et al. 2018). In particular, individuals treat salient temporal cues rather differently from other time points, and these cues can trigger their self-control behavior to support the pursuit of goals. As shown by Dai et al. (2014), aspirational behavior—such as searching for the term “diet,” gym visits, and goal commitments—increases with the occurrence of temporal cues, such as the beginning of a new week, month, semester, or year. Gabarron et al. (2015) also found an increase in searches for health information at the beginning of a workweek.

However, the related prior work primarily focused on temporal cues that are dispersed to a large extent—such as a new year, new month, and birthday. It is relatively understudied as to whether individuals respond to intraday temporal cues that would lead to the attainment of goals or improved performance, particularly in an online learning setting. Recently, Sellier and Avnet (2019) found that individuals often rely on clock time to control their behavior, and they slice time into quantifiable units and let an external clock dictate when certain activities begin and end. Extending this idea, we examine intraday temporal cues (i.e., on-the-hour time points) in online learning through the perspective of the mindset theory and empirically investigate how these temporal cues impact users’ interaction outcomes with the learning systems.

## 2.2. The Mindset Theory

Proposed by Gollwitzer (1990), the mindset theory provides a theoretical explanation for the effects of temporal cues in individuals’ goal-pursuit processes. Gollwitzer (1990) argued that two different mindsets, the deliberative and implemental mindsets, play important roles in supporting the pursuit of goals. In particular, individuals with a deliberative mindset tend to weigh the pros and cons of various choices, whereas those with an implemental mindset cognitively turn toward implementation-related information that facilitates the pursuit of goals (Gollwitzer 1990, Tu and Soman 2014). Once a specific mindset is activated, it can manifest through cognitive and behavioral dimensions (Gollwitzer 1990, Zhao et al. 2012). Typically, individuals with an implemental mindset (compared with a deliberative mindset) tend to be optimistic (Taylor and Gollwitzer 1995), are more likely to initiate goal-pursuit actions (Tu and Soman 2014), and can persist longer with problem solving (Brandstatter and Frank 2002).

Scholars have also investigated the factors that trigger a specific mindset. Deliberative mindsets can be activated by getting a person to decide between different choices (Gollwitzer et al. 1990), whereas space-related or time related cues can activate an implemental mindset (Tu and Soman 2014). For example, individuals are more implementation oriented after entering a shopping mall (Lee and Ariely 2006) or coming across situational cues, such as queue guides and area carpets (Zhao et al. 2012). In exploring the effects of on-the-hour time points, the mindset theory provides a potential theoretical lens to reveal the underlying mechanism of such effects. Therefore, this paper extends this stream of research by demonstrating that on-the-hour time points (compared with other time points) activate users’ implemental mindset in learning, which then motivates users to persist longer and thus, achieve better learning performance.

## 2.3. Online Learning System Design

As different IT features can be selectively applied to support users’ learning processes (Santhanam et al. 2008, 2016; Liu et al. 2017), IS scholars have focused on exploring how different technology-based interventions and designs influence learners’ psychology processes and enhance learning outcomes (Santhanam et al. 2008, Huang et al. 2020). Specifically, to overcome the problems of online learners feeling isolated from peers and instructors (Santhanam et al. 2008, Richardson et al. 2017) and being less motivated to engage in learning activities (Brown 2001, Bell and Kozlowski 2002, Zhang et al. 2004, Kizilcec and Halawa 2015), a type of technology-based design has been considered, namely implementing IT design to enhance users’ perceptions of the social presence of other users.

Social presence, the extent to which a medium allows one to establish a personal connection with others (Short et al. 1976, Pavlou et al. 2007, Animesh et al. 2011), is an important factor that affects users’ perceptions and behaviors in online and distance learning contexts (Gunawardena and Zittle 1997, Cobb 2009, Zhan and Mei 2013, Richardson et al. 2017). Research suggests that individuals are impacted by the real, implied, and imagined presence or actions of others (Latane 1981, Argo et al. 2005). A sense of human contact and the presence of others can elicit thoughts of being evaluated (Dahl et al. 2001, Gefen and Straub 2004). Therefore, individuals tend to select socially desired options (Ariely et al. 2009, Zwebner and Schrift 2020) and engage in impressionmanagement behavior (Leary and Kowalski 1990, Argo et al. 2005). The perception of social presence also drives individuals to implement and concentrate on goal/taskdirected behavior (Zajonc 1965, Bruning et al. 1968). Therefore, in online learning contexts, users’ perception of social presence shows a positive relationship with their learning engagement (Franceschi et al. 2009), participation (Tu and Mcisaac 2002), performance (Picciano 2002), and satisfaction (Zhan and Mei 2013, Richardson et al. 2017). Given that social presence-enhanced designs are considered to help overcome self-control problems and motivate users’ interaction with learning systems, in addition to exploring the direct effects of on-the-hour time points, this paper examines how these cues interact with social presence to affect users’ learning outcomes.

## 3. Hypothesis Development

## 3.1. On-the-Hour Effects in Online Learning

In an online learning environment, users usually interact with learning systems to achieve certain learning goals (e.g., improving English proficiency), which are typical results of “should” behavior and long-term value orientation. Initiating such “should” behavior is usually a big challenge for users, who often lack the self-control to expend the time and effort on learning and instead, postpone learning behavior (Milkman et al. 2008, Dai et al. 2014, Huang et al. 2020). According to prior studies, individuals’ self-control decisions are influenced by easy-totrack external temporal cues (Sellier and Avnet 2014, Rai et al. 2016, Duckworth et al. 2018). For example, the presentation of salient temporal cues—such as the beginning of a year, month, or week—can trigger individuals aspirational behavior, such as searching for diet information, gym visits, and goal commitment (Dai et al. 2014, 2015). Individuals are more likely to search for health information at the beginning of a workweek (Gabarron et al. 2015). At the intraday level, a salient temporal cue that might affect users’ self-control decisions is based on naturally occurring on-the-hour time points, which are usually treated as reference points for users’ management of goal-directed behavior (Allen et al. 2017).

Sellier and Avnet (2019) found that individuals tend to rely on clock time to control their behavior by slicing time into units and letting an external clock dictate the beginning and end of certain activities. In exploring the effects of numbers on users’ perceptions and behavior, Shoham et al. (2018) found that round numbers are usually perceived as category boundaries and that decimals are perceived to represent intermediate values. Crossing such round-number category boundaries can enhance the perceived magnitude of a change (Isaac and Schindler 2013, Shoham et al. 2018) and motivate aspirational behavior (Dai et al. 2014, 2015). Therefore, the occurrence of on-the-hour time points implies the transition from intermediate time points to round hours, thereby marking the beginning of new periods.

Drawing on the research on mindsets, space- and time-related cues—representing the transitions—can activate an individual’s implemental mindset (Zhao et al. 2012, Tu and Soman 2014). For example, walking into a grocery store makes shoppers more implementation oriented (Lee and Ariely 2006), and queue guides that mark entry into a specific area activate a strong implemental mindset in individuals (Zhao et al. 2012). Following this logic, because on-the-hour time points mark the beginning of new periods and serve as critical temporal cues for users to transition from a previous period of time to the current period of time, such time points can trigger a stronger implemental mindset among users. Therefore, we propose the following hypothesis.

Hypothesis 1. Starting a learning session at on-the-hour time points (versus other time points) triggers a stronger implemental mindset for users.

It has also been documented that an implemental mindset facilitates successful goal attainment across different tasks, such as writing reports (Gollwitzer and Brandstatter 1997) and performing medical checkups (Orbell and Sheeran 2000). Individuals with an imple mental mindset tend to concentrate on goal-related information (Buttner et al. 2014) and can persist longer in goal-directed behavior (Brandstatter and Frank 2002). In our research context, learning persistence (i.e., an individual’s action of persisting in a learning activity) and learning performance are important instrumental outcomes of using learning systems (Hanus and Fox 2015, Liu et al. 2017). When on-the-hour time points trigger a stronger implemental mindset for users in using learning systems, users are expected to concentrate on learning-related information and persist longer in interacting with learning systems. Consequently, they are likely to achieve a higher level of learning performance. Therefore, we propose the following hypothesis.

Hypothesis 2. A stronger implemental mindset triggered by on-the-hour time points enhances users’ learning outcomes: that is, (a) learning persistence and (b) learning performance.

## 3.2. Moderating Effects of Social Presence

Herein, we use the construct of social presence to capture the extent to which users perceive the presence of other learners (without verbal interactions) while using online learning systems or performing a learning task. According to the literature, social presence plays an important role in contexts such as online learning (Kehrwald 2008, Cobb 2009, Richardson et al. 2017). Prior studies on online learning have explored the direct effects of social presence on users’ participation (Cobb

Figure 1. Research Model  
![](/api/attachments/HA7Z7WGM/fulltext/images/0752847dc1cec018074ab20292ae9e39fe60dcc1cf249d066023c6164260afa6.jpg)  
Note. H, hypothesis.

2009), online collaboration (Richardson et al. 2017), satisfaction (Gunawardena and Zittle 1997, Cobb 2009), and learning achievement (Zhan and Mei 2013).

These studies, along with their respective streams of literature, suggest that social presence improves individuals’ activity engagement and concentration (Picciano 2002, Animesh et al. 2011). According to Zajonc (1965), individuals’ perception of social presence helps them feel an increased drive (i.e., an urgent need pressing for satisfaction) to perform tasks, suggesting that social presence may also enhance individuals’ implemental mindset and supports them in concentrating on task-/ goal-related behavior. Under such these conditions, social presence might moderate the effects of several influencing environmental factors (Bruning et al. 1968, Huguet et al. 1999). For example, Bruning et al. (1968) showed that the perception of social presence leads to decreased utilization of external cues. Meanwhile, the mere presence of an attentive or invisible audience results in attention focusing while participants complete the Stroop task (Huguet et al. 1999). According to Muller and Butera (2007), the perception of social presence results in a potential threat to self-evaluation (i.e., concern about not reaching standards or goals), which overloads individuals’ cognitive systems and results in narrow attention focusing and a reduction in participants’ cue utilization (Bruning et al. 1968, Muller et al. 2004, Muller and Butera 2007). In isolation, individuals are more likely to pay attention to and be affected by external or periphera cues (Huguet et al. 1999). In contrast, the presence of others (attentive audience, invisible audience, or coactors) allows individuals to focus on the task at hand and ignore external cues (Huguet et al. 1999, Muller and Butera 2007). In particular, we expect social presence to attenuate the effects of on-the-hour time points on the implemental mindset and improve learning persistence and learning performance. Considering this, we propose the following hypothesis.

Hypothesis 3. Social presence moderates the effects of onthe-hour time points such that social presence attenuates the effects of on-the-hour time points on users’ (a) implemental mindset, further resulting in lower levels of (b) learning persistence and (c) learning performance.

To test the proposed hypotheses, we conducted a series of studies. In Study 1, we analyzed the archival data from an online learning app to provide correlational evidence of the relationships between on-thehour time points and users’ learning performance. In Study 2, we conducted a laboratory experiment to demonstrate the causal effects of on-the-hour time points in online learning, thereby indicating that the manipulated on-the-hour time points increase users’ learning persistence and learning performance. In Study 3, we performed a framed field experiment to showcase the external validity of our laboratory findings. In Study 4, we conducted an online experiment to explore the underlying mechanism of on-the-hour effects and identified social presence as a key moderating factor for on-thehour effects. The research model is shown in Figure 1.

## 4. On-the-Hour Effects in Learning Systems

## 4.1. Study 1: Effects of On-the-Hour Time Points in Archival Data Analysis

In Study 1, we analyzed the archival data from an online learning app to provide evidence of on-the-hour effects, as we find that starting learning sessions with regular learning modules at on-the-hour time points is positively related to users’ learning performance.

4.1.1. Data. We obtained archival data from an online learning app that supports users in learning English as a foreign language. By July 2016, the learning app had over 30 million registered users and was highly ranked in the app stores. The online learning app is shown in Online Appendix A. Our data set consisted of a random sample of 15,011 users and their activities over a period of four months (from November 2016 to February 2017). In particular, we measured the number of English words a user learned during the observation period (Learning Performance). We also used the variable Active Day to capture the number of days a user used the learning app. As additional control variables, we measured users engagement with certain activities (using the learning and gamification module) in the app.<sup>4</sup> Table 1 presents the summary statistics of the variables in Study 1.

Table 1. Summary Statistics

<table><tr><td>Variable</td><td>Min</td><td>Max</td><td>Mean</td><td>Standard deviation</td><td>Observations</td></tr><tr><td>Learning Performance</td><td>0</td><td>3,897</td><td>190.51</td><td>336.89</td><td>15,011</td></tr><tr><td>Active Day</td><td>0</td><td>129</td><td>7.12</td><td>10.78</td><td>15,011</td></tr><tr><td>Learning Activity</td><td>1</td><td>5,273</td><td>13.73</td><td>61.54</td><td>15,011</td></tr><tr><td>Gamification Activity</td><td>1</td><td>466</td><td>7.00</td><td>15.73</td><td>15,011</td></tr></table>

4.1.2. On-the-Hour Time Points and Learning Performance. In this study, we first tested how the occurrence of on-the-hour time points affects learning performance using the following specification, referring to Balasubramanian et al. (2018).

$$
\begin{array}{l} \text {Learning Performance} _ {i} \\ = \gamma_ {1} R L _ {i} ^ {k} + \gamma_ {2} \text {Active Day} _ {i} + \gamma_ {3} \text {Learning Activity} _ {i} \\ \quad + \gamma_ {4} \text {Gamification Activity} _ {i} + \epsilon_ {i}, \end{array}\tag{1}
$$

$$
\text { where } R L _ {i} ^ {k} = \frac {\text { records   of   beginning   to   use   the   regular   learning   module   in   the   first } k \text { minutes   for   user } i}{\text { records   of   using   the   regular   learning   module   for   user } i},
$$

$R L _ { i } ^ { k }$ represents the proportion that user i uses the regular learning module in the first k minutes of an hour, and $\epsilon _ { i }$ is the error term.

The regression results are presented in Table 2. Consistent with our prediction, the results in Table 2 indicate that the coefficients of $R L _ { i } ^ { 1 } , R L _ { i } ^ { 5 }$ , and $R L _ { i } ^ { 1 0 }$ are positively significant, showing that users tend to achieve better learning performance when they are more likely to begin using regular learning modules at on-the-hour time points. In particular, the results in Table 2 indicate that users who have one-unit increase in the proportion of using the regular learning module in the first minute of an hour tend to learn 35.84 more words. The corresponding numbers of words for the first 5 and 10minutes of an hour are 28.41 and 24.95, respectively. Given that, on average, users learn 190.51 words during our observation (from November 2016 to February 2017), these differences are substantial (18.81%, 14.91%, and 13.10% higher relative to the average learning performance). We also examined archival behavioral trace data to explore the effects of on-the-hour time points and half-hour time points. The results suggest that the occurrence of on-thehour and half-hour time points has a significant relationship with learning performance (see details in Online Appendix B).

4.1.3. Discussion of Study 1. Study 1 demonstrates that starting a learning session at on-the-hour time points has a positive relationship with learning performance. Therefore, this archival study confirms the salient on-thehour effects, which motivates us to further study the said effects. Although evidence from the interviews helps strengthen our confidence in on-the-hour effects, we acknowledge that Study 1 is observational in nature and only provides correlational evidence of and motivation for the phenomenon. Therefore, we conducted a series of experiments to (a) establish a causal on-the-hour effect, (b) uncover the potential underlying mechanism of the on-the-hour effect, and (c) understand the moderating role of social presence. Specifically, these experimental studies manipulate the occurrence of on-the-hour time points, as external cues, to examine how on-the-hour time points (compared with other time points) affect users’ interaction with learning systems and the out comes thereof.

## 4.2. Study 2: Identifying On-the-Hour Effects in a Laboratory Experiment

4.2.1. Experimental Design. The goal of Study 2 is to extend Study 1 and evaluate evidence for a causal onthe-hour effect. Study 2 has a two-level, single-factor (task start time: on-the-hour time points versus other time points) between-subject design. Table 3 lists the manipulations in the experimental groups and the corresponding participant instructions. Figure 2 presents examples of the manipulations in the experiment. Participants assigned to the on-the-hour time points group were manipulated to believe that they began a learning task that was designed in reference to the regular learning module in the online learning app in Study 1 at certain on-the-hour time points. In contrast, participants assigned to the other time points group were manipulated to perceive that they began the same learning task six or eight minutes after the round hour.<sup>5</sup>

Table 2. Timing of Using the Regular Learning Module and Learning Performance

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td> $RL_{i}^{1}$ </td><td>35.85*** (5.37)</td><td></td><td></td></tr><tr><td> $RL_{i}^{5}$ </td><td></td><td>28.41*** (4.85)</td><td></td></tr><tr><td> $RL_{i}^{10}$ </td><td></td><td></td><td>24.95*** (4.41)</td></tr><tr><td>Active Day</td><td>21.32*** (0.18)</td><td>21.36*** (0.18)</td><td>21.38*** (0.18)</td></tr><tr><td>Learning Activity</td><td>0.46*** (0.03)</td><td>0.46*** (0.03)</td><td>0.47*** (0.03)</td></tr><tr><td>Gamification Activity</td><td>0.87*** (0.13)</td><td>0.89*** (0.13)</td><td>0.90*** (0.13)</td></tr><tr><td>Number of observations</td><td>15,011</td><td>15,011</td><td>15,011</td></tr><tr><td> $R^{2}$ </td><td>0.517</td><td>0.517</td><td>0.517</td></tr></table>

Note. Standard errors are reported in parentheses.

Table 3. Participant Notifications and Manipulations in Study 2

<table><tr><td>Experimental group</td><td>Participant instruction</td><td>Manipulation</td></tr><tr><td>On-the-hour time points</td><td>Participants were told to arrive at the laboratory 20 minutes before a round hour (i.e., 8:40 a.m., 9:40 a.m., 10:40 a.m., 1:40 p.m., 2:40 p.m., 3:40 p.m., 4:40 p.m., 6:40 p.m., 7:40 p.m., or 8:40 p.m.)</td><td>Participants were told, “It is 9:00 a.m. now (or 10:00 a.m., 11:00 a.m., 2:00 p.m., 3:00 p.m., 4:00 p.m., 5:00 p.m., 7:00 p.m., 8:00 p.m., 9:00 p.m.); please begin the learning task.”</td></tr><tr><td>Other time points</td><td>Participants were told to arrive at the laboratory 10 minutes before a round hour (i.e., 8:50 a.m., 9:50 a.m., 10:50 a.m., 1:50 p.m., 2:50 p.m., 3:50 p.m., 4:50 p.m., 6:50 p.m., 7:50 p.m., or 8:50 p.m.)</td><td>Participants were told, “It is 9:06/9:08 a.m. now (or 10:06/10:08 a.m., 11:06/11:08 a.m., 2:06/2:08 p.m., 3:06/3:08 p.m., 4:06/4:08 p.m., 5:06/5:08 p.m., 7:06/7:08 p.m., 8:06/8:08 p.m., 9:06/9:08 p.m.); please begin the learning task.” The experiment assistant randomly told participants that the time was 6 or 8 minutes past a round hour.</td></tr></table>

4.2.2. Experimental Procedure. Seventy students recruited from a large public university in China participated in the experiment and were each offered a reward of \$4.65 for their participation. They were randomly assigned to one of the two experimental groups to complete an English word-learning task. To avoid peer influence among the participants, they were asked to participate in the experiment separately. During the experiment, items that might provide clues about the time (e.g., the clock in the laboratory and the time displayed on the computer) were removed. The participants were required to leave their cell phones and watches in a locker.

The flow of the experimental procedure is depicted in Figure 3. After a participant arrived at the laboratory, the experiment assistant informed them that the objec tive of the experiment was to test a newly designed online learning system. The experiment included two stages. In the first stage, the participant was required to complete a vocabulary test, wherein they were asked to select the correct translation (in Chinese) for 30 English words.<sup>6</sup> These English words were randomly selected from the vocabulary book of the Test of English as a Foreign Language (TOEFL),<sup>7</sup> which is one of the two major English-language tests in the world. After completing the test, each participant was told to take a short break of five minutes.

After the break, the experiment assistant announced the beginning of the second stage. The participants were told to learn English words that were randomly selected from the TOEFL vocabulary book (see the word list in

Figure 2. (Color online) Examples of Manipulations in Study 2  
![](/api/attachments/HA7Z7WGM/fulltext/images/aafa1606636def9273c9504cf31cad7e31bc88c4de6644d88253ec1a10c7e42c.jpg)

![](/api/attachments/HA7Z7WGM/fulltext/images/c5c8a4b8f26ae063c4f475f4bc72846dc79b80a8c6f8f104f311579eb73bca98.jpg)  
Notes. (a) One example of a manipulation in the on-the-hour time points group. (b) One example of a manipulation in the other time points group.

Figure 3. Flow of the Experimental Procedure in Study 2  
![](/api/attachments/HA7Z7WGM/fulltext/images/4513d11e1a93c2206f79f4d1303a933391b9b7941c04c1dac6506a6674023f6b.jpg)

Online Appendix C) and were given the freedom to decide how many words to learn and for how long. Before the beginning of the word-learning task, the experiment assistant intentionally looked at her watch and announced the “current” time to manipulate the start time of the learning task (irrespective of what the actual time was). Each participant in the on-the-hour time points group was told, “It is XX:00 now; please begin the learning task.” Each participant in the other time points group was told, “It is XX:06 or XX:08 now (the experiment assistant randomly told the participants that the time was six or eight minutes past a round hour); please begin the learning task” (see details in Table 3).

In both groups, the specific time point the experiment assistant relayed to a participant was displayed on the computer screen for five seconds. The participants then began learning the English words, including the meaning of each word and how to spell, pronounce, and use each word. In addition, two example sentences were displayed to explain the meaning of each word. A test followed each word to ensure that the participants had learned each word. The participants were given a sentence with the newly learned word and were asked to select one picture from four pictures that matched the meaning of the sentence most closely. Finally, the participants themselves decided when to end the learning task and were asked to recall the exact time points at which they began the learning task.

4.2.3. Results of Study 2. Two participants in the other time points group who failed to recall the task start time were removed from the sample. Therefore, the data of 68 participants were analyzed. First, we conducted a t test to compare the performance of the two groups in the vocabulary test (the first stage of the experiment), and the result revealed no significant difference. The t tests also indicated no statistically significant difference between the pair of experimental groups in terms of age and gender. These tests suggest that there were no preexperiment differences between the two groups.

Figure 4 presents the means and standard errors of learning persistence (measured by the time duration a participant persists in performing the learning task) and learning performance (measured by the number of words the participants learned in the experiment) in each experimental group. The results of the t tests are reported in Table 4. As predicted, the participants in the on-the-hour time points group (M � 17.46, standard deviation (SD) � 6.51) persisted significantly longer (p < 0.05) than those in the other time points group (M � 14.82, SD � 6.27) when performing the wordlearning task. Meanwhile, the participants who were manipulated to begin the learning task at on-the-hour time points tended to learn more words (M � 36.40, SD � 19.20) than those in the other time points group (M � 28.15, SD � 12.80, p < 0.05). Therefore, the results support Hypothesis 2, (a) and (b) and illustrate that naturally occurring on-the-hour time points function as important external cues and motivate individuals to have greater learning persistence and achieve better learning performance.

4.2.4. Discussion of Study 2. Study 2 replicated the findings in Study 1, according to which the participants displayed better learning performance when they started learning at on-the-hour time points (compared with other time points). Furthermore, addressing the endogeneity concern in the correlational evidence in Study 1, we manipulated the on-the-hour time points and observed the participants’ usage of the learning system designed in reference to the regular learning module in Study 1. The findings of our laboratory experiment support the internal validity of our findings and provide evidence for the activation of an implemental mindset from the behavioral dimension (i.e., participants in the on-the-hour group persisted longer in performing the learning task). In Studies 3 and 4, we sought to evaluate the external validity of the findings and further explore the underlying mechanisms, respectively.

Figure 4. Learning Persistence and Learning Performance in Study 2  
![](/api/attachments/HA7Z7WGM/fulltext/images/5d81b478def571606889aaf24f1ad516554ad3e4afd9c36e9baf8a5e5cea9035.jpg)  
Learning Persistence

![](/api/attachments/HA7Z7WGM/fulltext/images/9a15cd511fbe543cb225600e968ab3918cda16fb5ecf338b69c26b92fa2196a3.jpg)  
Learning Performance  
Note. Error bars represent standard errors.

## 4.3. Study 3: Identifying On-the-Hour Effects in a Framed Field Experiment

To enhance the external validity of our findings in Study 2, in Study 3 we conducted a framed field experiment that considered more other time points and explored how on-the-hour time points affect the use of the regular learning module.<sup>8</sup> We found that, consistent with our prior findings, on-the-hour time points increase participants’ learning persistence.

4.3.1. Method. In Study 3, we collaborated with the online learning app mentioned in Study 1 to conduct the framed field experiment. We recruited students who had never used the learning app before, again at a Chinese public university. The participants were invited to perform specific experimental tasks in the learning app and were promised a reward of an equivalent of \$4.65. In Study 3, the participants were recruited to use the regular learning module. The study had a one-factor, two-level (task start time at on-the-hour time points versus other time points) between-subjects experimental design.

The participants signed up for the experiment one week in advance and were asked to download and instal the learning app. Following our experimental protocol, the same vocabulary range was set for all participants in the app. We helped the participants become familiar with different functional modules of the app. The participants were then randomly assigned to the experimental groups. One day before the experiment began, the experiment assistant sent participants an email to inform them to strictly follow the instructions (e.g., start time and minimum use time) when completing the experimental tasks. Furthermore, when performing the experimental task, the participants were allowed to decide how long (no less than five minutes) they would use the regular learning module. After the task, they were asked to complete an online demographic information survey. Table 5 summarizes the experimental tasks in Study 3. After the experiment, we extracted behavior data, which included the time stamps of beginning and ending the use of the regular learning modules from the learning app.

4.3.2. Results and Discussion of Study 3. We conducted a series of pairwise comparison t tests on the participants’ demographic information. Our results indicated no statistically significant difference between any pair of experimental groups in terms of age and gender. In particular, in Study 3, we recruited 59 participants, 36 of whom completed their tasks strictly following our requirements.

Table 4. Results of Study 2

<table><tr><td>Experimental group</td><td>Learning Persistence (minutes)</td><td>Learning Performance</td></tr><tr><td>On-the-hour time points (N = 35)</td><td>17.46 (SD = 6.51)</td><td>36.40 (SD = 19.20)</td></tr><tr><td>Other time points (N = 33)</td><td>14.82 (SD = 6.27)</td><td>28.15 (SD = 12.80)</td></tr><tr><td>p-value of t tests</td><td>&lt;0.05</td><td>&lt;0.05</td></tr></table>

Note. SDs are reported in parentheses.

Table 5. Details of Experimental Tasks in Study 3

<table><tr><td>Experimental group</td><td>Details of experimental tasks</td></tr><tr><td>On-the-hour time points</td><td>Participants were told to begin using the regular learning module at 9:00 p.m. They were allowed to decide how long they would use the regular learning module (no less than 5 minutes).</td></tr><tr><td>Other time points</td><td>Participants were told to begin using the regular learning module at a time point that the experiment assistant randomly selected—8:36 p.m. to 8:50 p.m. or 9:11 p.m. to 9:25 p.m. The participants were allowed to decide how long they would use the regular learning module (no less than 5 minutes).</td></tr></table>

Comparing the participants’ learning persistence between both groups enabled us to examine the effects of on-the-hour time points $\left( \mathrm { i . e . , } 9 { : } 0 0 \mathrm { p . m . } \right)$ on the use of the regular learning module. The results of the t tests in Table 6 suggest that the participants who were assigned to begin learning at on-the-hour time points (M � 11.73, SD � 6.51) persisted longer (p < 0.05) than those who began performing the same task at other time points $( \mathrm { M } { = } 7 . \dot { 1 } 7 , \mathrm { S D } { = } 3 . \dot { 1 } 2 ) . ^ { 9 }$ The results are shown in Figure 5. Consistent with our findings in Study 2, in support of Hypothesis 2(a), the results indicated that on-the-hour time points motivate individuals to spend more time performing learning tasks.

## 4.4. Study 4: Exploring Potential Mechanisms and the Moderating Effects of Social Presence

In Study 4, we conducted an online experiment to reveal the mindset activated by on-the-hour time points and to explore a possible moderator of the on-the-hour effects. As Gollwitzer et al. (1990) indicated, individuals tend to recall implementation-related information (e.g., how to take an action) in an implemental mindset and deliberation-related information (e.g., why or why not take an action) in a deliberative mindset. Referring to prior studies, we designed a recall task in Study 4 to further verify the mindset induced in our experiment (Chandran and Morwitz 2005, Dhar et al. 2007). After completing a learning task, the participants were required to perform a recall task by recalling both deliberative and implemental statements related to the decision to purchase an online course. In line with the Dhar et al. (2007) study, we conducted a pilot study to ask 20 pretest participants to list six pros and six cons of purchasing an online course (deliberative statements). In addition, we asked them to list six actions that were necessary after deciding to purchase an online course (implementa statements). We listed the six most mentioned statements in each mindset in Online Appendix D. Furthermore, in Study 4, we explored the moderating effects of the design that enhances users’ perceptions of social presence, leveraging the “breakout room” function of Zoom software, wherein we varied the number of participants in the respective breakout rooms in the experiment.

Table 6. Results of Study 3

<table><tr><td>Experimental group</td><td>Learning Persistence (minutes)</td></tr><tr><td>On-the-hour time points (n = 21)</td><td>11.73 (SD = 6.51)</td></tr><tr><td>Other time points (n = 15)</td><td>7.17 (SD = 3.12)</td></tr><tr><td>p-value of t tests</td><td>&lt;0.05</td></tr></table>

Note. SDs are reported in parentheses.

Study 4 explored how task start time (on-the-hour time points versus other time points) affected the participants’ mindset, learning persistence, and learning performance while they performed a learning task. The results of Study 4 indicate that on-the-hour time points (versus other time points) activate participants’ implemental mindset while they are performing a learning task, which in turn, supports them in having greater learning persistence and better learning performance. Meanwhile, social presence significantly attenuates the effects of on-the-hour time points.

4.4.1. Method. Students from several public universities in China were recruited to participate in our experiment, with a compensation equivalent to \$5.7. Ultimately, 169 participants performed a learning task identical to that performed in Study 2.<sup>10</sup> Study 4 had a two-factor, twolevel (task start time × social presence) between-subjects experimental design. Participants were instructed to complete the learning task for as long as they wanted and then perform the recall task. We manipulated the task start time by beginning the first experimental task at onthe-hour time points (i.e., 11:00 a.m.) or at other time points (i.e., 11:08 a.m.). The participants in the social presence condition were assigned to perform the experimental task in Zoom breakout rooms with other participants. Those in the no social presence condition completed their tasks alone in separate Zoom breakout rooms.

Figure 5. Learning Persistence in Study 3  
![](/api/attachments/HA7Z7WGM/fulltext/images/6269ba8f1d8c6c492f278138974bb3def6a8a3558256b691c7244e620930293b.jpg)  
Note. Error bars represent standard errors.

Figure 6. Flow of the Experimental Procedure in Study 4  
![](/api/attachments/HA7Z7WGM/fulltext/images/4741da39930bc552667230eee2049bf44cd5638910d553988dcd03874c900a2b.jpg)

Figure 6 illustrates the experimental procedure in Study 4. The research assistant invited the participants to join a Zoom virtual meeting and introduced the experimental tasks (performing a learning task and completing a recall task). The research assistant explained the guidance given on an experimental website and shared the link of the experimental website (on Qualtrics.com) with the participants through the chat box of the Zoom meeting. The participants were informed that they would receive an experimental code to begin the experiment after entering the Zoom breakout room and that they would need to remain connected to each other in the breakout room during the experiment.<sup>11</sup> Thereafter, the participants were assigned to either the same Zoom breakout room with other participants (in the social presence condition) or separate Zoom breakout rooms (in the no social presence condition). The assistant informed the participants of the experimental code one minute before the manipulated time points and asked them to begin the experimental tasks.<sup>12</sup> Similar to the design in Study 2, once the participants input the experimental code, a specific manipulated time point (i.e., 11:00 a.m. or 11:08 a.m.) was displayed on the experimental website for five seconds. The participants then began the first experimental task.

The participants learned English words on the experimental website for as long as they wanted. After completing the first task, they were asked to recall the exact time points at which they began the task and whether they performed the tasks with others in the same breakout room or a separate one. We conducted manipulation checks based on these answers. Thereafter, we measured the participants’ perception of social presence (Gefen and Straub 2004), self-efficacy (Fujita et al. 2007), and task commitment (Fujita et al. 2007).<sup>13</sup> Next, referring to Dhar et al. (2007), all participants were asked to read 12 thoughts that a hypothetical person might have when deciding whether to buy an online course and what to do after the decision to purchase was made (see details in Online Appendix D). After two filler tasks, the parti cipants were required to recall as many thoughts as they could.

4.4.2. Results and Discussion of Study 4. In Study 4, valid responses from 125 participants were used for the analyses.<sup>14</sup> The Cronbach’s alpha score of social presence was 0.87, and the participants in the social presence condition had a higher perception of social presence (M � 2.842 versus M � 2.141, p � 0.004) than those in the no social presence condition, thereby indicating the success of our manipulation.

Table 7 lists the statistical results of Study 4, and Figure 7 illustrates these results. As depicted in the table, among the participants who performed the learning task in the no social presence condition, those who began at an on-thehour time point recalled significantly more implemental statements than those who began at other time points (M � 2.324 versus M � 1.594, p � 0.044), thereby verifying our prediction that on-the-hour time points activate an individual’s implemental mindset (Hypothesis 1). Meanwhile, consistent with our findings in Studies 2 and 3, the participants tended to have greater learning persistence (M � 14.755 versus M � 8.556, p � 0.001) and achieve better learning performance (i.e., learned more English words) in the on-the-hour time points group (M � 19.324 versus M � 11.438, p � 0.014) than in the other group, supporting Hypothesis 2, (a) and (b). However, under the condition in which the participants completed the learning task in a Zoom breakout room with others (the social presence condition), we did not find significant differences in the number of recalled implemental statements, the number of recalled deliberative statements, learning persistence, or learning performance.

The results of the two-way analysis of variance (ANOVA) (see Table 8) indicated that the effects of the interaction term (i.e., on-the-hour time points × social presence) on the participants’ recall of implemental statements (p� 0.078), learning persistence (p� 0.008), and learning performance (p� 0.032) were significant, supporting Hypothesis 3, (a), (b), and (c). Furthermore, to explore the extent to which an implemental mindset explained the main effect of on-the-hour time points on learning outcomes (i.e., learning persistence and learning performance) and the moderating effect of social presence, we applied a standard bootstrap procedure (model 7 in

Table 7. Results of Study 4

<table><tr><td>Experimental group</td><td>Number of Implemental Statements</td><td>Number of Deliberative Statements</td><td>Learning Persistence</td><td>Learning Performance</td></tr><tr><td colspan="5">No social presence</td></tr><tr><td>On-the-hour time points (n = 34)</td><td>2.382 (1.349)</td><td>2.971 (1.141)</td><td>14.755 (6.989)</td><td>19.324 (14.677)</td></tr><tr><td>Other time points (n = 32)</td><td>1.531 (1.319)</td><td>3.156 (1.273)</td><td>8.556 (4.585)</td><td>11.438 (7.560)</td></tr><tr><td colspan="5">Social presence</td></tr><tr><td>On-the-hour time points (n = 29)a</td><td>2.207 (1.590)</td><td>2.724 (1.461)</td><td>14.524 (8.237)</td><td>19.414 (12.813)</td></tr><tr><td>Other time points (n = 30)b</td><td>2.200 (1.540)</td><td>2.867 (1.432)</td><td>15.870 (9.701)</td><td>20.433 (14.968)</td></tr></table>

Note. Standard errors are reported in parentheses.  
<sup>a</sup>Thirty-three participants finished the experiment task in this experimental group, and four of them were excluded from the data analysis because they failed to correctly answer the manipulation check questions. Therefore, there were 29 valid samples in this group.  
<sup>b</sup>Thirty-seven participants finished the experiment task in this experimental group, and six of them were excluded in the data analysis because they failed to correctly answer the manipulation check questions. Therefore, there were 31 valid samples in this group.

Hayes 2013). Specifying a confidence interval (CI) of 95% with 5,000 bootstrap resamples, we found that the indirect effect of on-the-hour time points on learning persistence through an implemental mindset is significant in the no social presence condition (indirect effect � 1.270; 95% CI [0.246, 2.678]). However, the results indicated an insignificant mediating effect of the implemental mindset on learning persistence (indirect effect � �0.123; 95% CI [�1.289, 0.841]) in the social presence condition. Consistently, the indirect effect of on-thehour time points on learning performance through an implemental mindset is significant in the no social presence condition (indirect effect � 2.347; 95% CI [0.544, 4.700]) but insignificant (indirect effect � �0.227; 95% CI [�2.388, 1.519]) in the social presence condition.

Figure 7. Results of Study 4  
![](/api/attachments/HA7Z7WGM/fulltext/images/23a3e380aae6e24308d0fe4b4bbfc6fcdf0bd8a48a8dba57df97a20609d618b7.jpg)  
Implemental Statements

![](/api/attachments/HA7Z7WGM/fulltext/images/8983e867a36253a1f610b0083b3485c8dc674b306f6cbef4daaa1f3393451a61.jpg)  
Learning Persistence

![](/api/attachments/HA7Z7WGM/fulltext/images/b84541ea2c8bd7df60e524d8cbab6687f018b871fb847e8ccb0162ea6821ff31.jpg)  
Learning Performance  
Note. Error bars represent standard errors.

Table 8. Results of Two-Way ANOVA in Study 4

<table><tr><td>Variables</td><td>Number of Implemental Statements (p-value)</td><td>Number of Deliberative Statements (p-value)</td><td>Learning Persistence (p-value)</td><td>Learning Performance (p-value)</td></tr><tr><td>On-the-hour Time Point</td><td>0.149</td><td>0.486</td><td>0.073</td><td>0.261</td></tr><tr><td>Social Presence</td><td>0.209</td><td>0.259</td><td>0.009</td><td>0.036</td></tr><tr><td>On-the-hour Time Point × Social Presence</td><td>0.078</td><td>0.945</td><td>0.009</td><td>0.032</td></tr><tr><td>Self-efficacy</td><td>0.915</td><td>0.243</td><td>0.730</td><td>0.206</td></tr><tr><td>Task Commitment</td><td>0.218</td><td>0.292</td><td>0.759</td><td>0.202</td></tr><tr><td>Age</td><td>0.570</td><td>0.710</td><td>0.472</td><td>0.131</td></tr><tr><td>Gender</td><td>0.823</td><td>0.036</td><td>0.973</td><td>0.633</td></tr><tr><td>Education Background</td><td>0.028</td><td>0.187</td><td>0.562</td><td>0.160</td></tr></table>

To obtain qualitative evidence from the participants perspective, we invited 41 participants in the study to participate in one-on-one debriefing interviews (see details in Online Appendix F). Interview answers supported our explanations for the on-the-hour effects and the moderating effects of social presence. When the participants were asked to imagine performing the same task beginning at on-the-hour time points (versus other time points), 31 (75.6%) confirmed that the differences in their perceptions or behavior were caused by task start time. They stated as follows. “On-the-hour time points represent new start points.” “These time points/temporal cues are natural constraints that motivate me to begin a serious task.” “I feel more comfortable to begin a learning task at on-the-hour time points, and it is much easier for me to focus on my task.” “Beginning a task at on-the-hour time points brings me a feeling of ritual. I will feel more energetic, take the task more seriously, and persist much longer.”

Meanwhile, 35 of 41 participants said that being virtually assigned to the same Zoom breakout room with other participants (versus being alone in a separate Zoom breakout room) is helpful for “building a psychological connection to others.” “It makes me feel that someone is in company with me.” “I feel comfortable following others’ behavior. If I know that others are stil learning, I will persist longer.” Furthermore, approximately 15 participants directly mentioned that the difference between on-the-hour time points and other time points can be mitigated and even disappear in the social presence condition. They stated as follows. “The constraining effects elicited by on-the-hour time points will disappear because I can directly refer to others behavior to make decisions.” “Being virtually connected with others, I will care less about the start time.”

In summary, the results of Study 4 provide evidence for the underlying mechanism of the effects of on-thehour time points from the cognitive dimension, thereby indicating that when performing a learning task, the occurrence of on-the-hour time points activates an implemental mindset in participants, which then supports them in achieving better learning performance. In addition, we demonstrated that social presence mitigates the effects of on-the-hour time points when participants performed a learning task, thereby supporting Hypothesis 3, (a), (b), and (c).

## 5. Discussion

## 5.1. Key Findings

In this paper, we adopted a multimethod approach and conducted a series of studies to examine how naturally occurring, intraday, on-the-hour time points that function as external cues impact users’ online learning behavior and outcomes.<sup>15</sup> In Study 1, the analysis of archival data obtained from an online learning app provided correlational evidence that beginning to use the regular learning module at on-the-hour time points had a positive relationship with learning performance. The results of a laboratory experiment in Study 2 indicated that users who began performing the word-learning task at the manipulated on-the-hour time points tended to persist longer and achieve better learning performance. In Study 3, a framed experiment revealed that the participants persisted longer in their learning when they began using the regular learning module at on-thehour time points. In Study 4, we conducted an online experiment to replicate the findings of Studies 2 and 3; the results of this study also provided evidence for the underlying mechanism by revealing that the occurrence of on-the-hour time points activated individuals’ implemental mindset while performing a learning task. We also found that social presence significantly mitigated the effects of on-the-hour time points when the participants were performing a learning task; thus, social presence serves as an important boundary condition for the effects of on-the-hour time points. We summarize our study designs and results in Online Appendix H.

## 5.2. Contribution to the Literature

Overall, this paper makes several contributions to the existing literature. First, it introduces and examines the effects of temporal cues in online learning contexts. Prior studies have mainly focused on factors related to learner characteristics, learning context, technology features, and instructional strategies that affect learners’ psychological processes and learning outcomes (Alavi and Leidner 2001, Santhanam et al. 2008, Gupta and Bostrom 2009, Huang et al. 2020). In particular, to help online learners overcome self-control problems and motivate user-system interactions, IS scholars have examined the effectiveness of several technologybased designs within learning systems, including selfregulated learning instructions (Santhanam et al. 2008), call-to-action reminders (Huang et al. 2020), and socia presence-enhanced designs (Franceschi et al. 2009). We extend prior related studies by considering temporal cues outside learning systems, which play an important role in motivating users to tackle their goals (Dai et al. 2014, 2015). Our paper demonstrates that intraday temporal cues, in the form of on-the-hour time points, substantially affect users’ learning persistence and learning performance. Second, our research sheds light on the literature on the mindset theory (Gollwitzer 1990, Taylor and Gollwitzer 1995, Zhao et al. 2012). Scholars have demonstrated that space- (e.g., queue guides and area carpets) (Zhao et al. 2012) or time-related cues (e.g., the categorization of time) (Tu and Soman 2014) can activate an implemental mindset. We examine the underlying mechanism for the on-the-hour effects, showing that onthe-hour time points can activate users’ implemental mindset when users start engaging with the regular learning module or learning systems, which helps users have greater learning persistence and better learning performance. Third, our research explores the role of social presence in the effects of on-the-hour time points in online learning. Other studies have explored the direct effects of various social presence, indicating that IT-enabled social presence significantly affects learning engagement (Franceschi et al. 2009), participation (Tu and Mcisaac 2002), performance (Picciano 2002), and satisfaction (Zhan and Mei 2013, Richardson et al. 2017). As an extension, our research explores how IT-based social presence interacts with on-the-hour time points to affect users’ mindsets and online learning outcomes, revealing that social presence mitigates the on-the-hour effects on the implemental mindset, learning persistence, and learning performance.

## 5.3. Practical Implications

This paper offers actionable implications for practice. First, according to our findings, online learning platforms’ learners and instructors can leverage common temporal cues (i.e., on-the-hour time points) to schedule learning activities to motivate themselves to improve their learning persistence and to achieve better learning performance. Based on our findings, developers can design an effective reminder system to motivate users to persist longer in the use of regular learning modules or learning systems. For example, a reminder system can indicate the appropriate timing (e.g., on-the-hour time points) to send messages that emphasize both these time points and instrumental outcomes (e.g., specific long-term learning goals) to support users’ goalpursuit behavior.

Second, this paper demonstrates the power of technology-based social presence in the online learning context. Online learning platforms can adopt a design that enables users who are geographically separated to be virtually connected (e.g., referring to the design of the StudyStream platform (https://www.studystream.live focus-room)) to improve their learning productivity. The findings of our study indicate that incorporating social presence-enhanced designs effectively mitigates the impact of temporal cues on users’ learning outcomes. Therefore, online learning platforms should take into consideration that the combined use of social presenceenhanced designs and temporal cues does not necessar ily yield additive benefits. Platforms may opt to leverage these design elements separately to help users improve their learning outcomes.

Finally, the current practice for online platforms is to issue mass notifications to users, typically early in the morning (Zhang et al. 2021), with the expectation of attracting and sustaining users’ attention in actively engaging with the platforms. Considering the findings of our research, platforms need to pay attention to both the value (i.e., utilitarian value or hedonic value) that platforms provide for users and the timing of issuing notifications. For example, entertainment apps mainly provide users with hedonic value; therefore, it would be beneficial for these platforms to send reminders to users at time points other than on-the-hour time points. In contrast, the use of health management apps is related to the pursuit of long-term health goals. These apps can remind users at on-the-hour time points to help them overcome willpower problems and motivate them to take immediate action.

## 5.4. Limitations and Future Research Opportunities

This work has several limitations that suggest ample research opportunities in the future. First, we investigated the short-term effect of on-the-hour time points. Although the short-term effect of the temporal cue is the focus of this study, it would be interesting for future studies to explore whether the effects of temporal cues will persist over time, particularly when users repeatedly perform the same task. Second, although our study is situated in the online learning context and focuses on the effects of on-the-hour time points on users’ learning outcomes, future work can explore the influence of onthe-hour time points in systems that focus on other types of outcomes, such as hedonic systems in which user enjoyment is important.

## Endnotes

<sup>1</sup> The source is https://www.thinkimpact.com/online-learningmarket-size/.

<sup>2</sup> For example, platforms, such as the StudyStream, enable learners to virtually connect with others to help them focus on their learning tasks and boost productivity (source: https://www.studystream. live/focus-room)

<sup>3</sup> As our data set did not include records of when users stopped using the regular learning module, we were unable to comprehensively evaluate all our hypotheses, which were formally tested in subsequent experimental studies.

In the online learning app, users use the regular learning module to learn how to spell, pronounce, and use new words. While analyz ing the effects of on-the-hour time points, we tried to control factors that may affect learning performance by controlling user activities in other modules in this app (i.e., the number of times users use a gamified learning module that enables them to compete with others). In the analysis, Learning Activity captured the number of times a user used the learning module, and Gamification Activity captured the number of times a user used the gamification module.

In Study 2, we considered the effects of on-the-hour time points during the periods of 9:00 a.m. to 11:59 a.m., 2:00 p.m. to 5:59 p.m., and 7:00 p.m. to 9:59 p.m. (no experiments were scheduled during lunchtime and dinnertime). Such a design enables us to consider the effects of different on-the-hour time points during the daytime. Based on a pilot study, we found that, on average, it takes approximately 15 min utes for activities (including an experiment introduction, an English vocabulary test, and a short break) before the formal manipulations in the experiment begin. To make our manipulations plausible, participants who were assigned to the on-the-hour time points group were told to arrive at the laboratory 20 minutes before a round hour and were manipulated to believe that they began the learning task at onthe-hour time points. Meanwhile, participants who were assigned to the other time points group were told to arrive at the laboratory 10 minutes before a round hour and were manipulated to believe that they began the learning task 6 or 8 minutes after the round hour. Because of the limitation of the laboratory experiment, we only considered two other time points in Study 2. As a complement, in the framed field experiment (Study 3), we further compared the effects of on-the-hour time points and other time points both before and after round hours.

<sup>6</sup> The comparability of subjects in different experimental groups can be assessed through the analysis of vocabulary test results. Addi tionally, the vocabulary test serves as a tool to influence consumers perception of time, making the manipulation of task start time more justifiable for all subjects.

<sup>7</sup> See https://www.ets.org/toefl.

<sup>8</sup> In Study 2, although choosing “the other time point,” we only considered some time points after specific on-the-hour time points. In Study 3, we considered more other time points by manipulating participants to complete their learning tasks at a time point randomly selected before (from 8:36 p.m. to 8:50 p.m.) or after (from 9:11 p.m. to 9:25 p.m.) a specific on-the-hour time point (i.e., 9 p.m.). <sup>9</sup> In Study 3, our access to data was limited to learning persistence data from the cooperative online learning platform. As a result, we were unable to examine the effects of on-the-hour time points (versus other time points) on learning performance in Study 3.

<sup>10</sup> The first experimental task of Study 4 involved performing a learning task. There was only one difference between the learning tasks in Studies 2 and 4. In Study 2, the words for learning were randomly selected from a TOEFL vocabulary book, whereas in Study 4, they were randomly selected from a Test of English for International Com munication vocabulary book (see the word list in Online Appendix C).

<sup>11</sup> Specifically, participants were instructed not to interact with other participants during the experiment. They were instructed to have the camera on and the mic off. During the experiment, the research assistant cycled the breakout rooms (for the social presence conditions) and confirmed that participants did not interact with others in the break room.

<sup>12</sup> We used this experimental design to ensure that participants strictly followed our instructions to perform the first experimental task at specific time points. We also checked the records of Qualtrics.com to eliminate those who failed to follow our instructions.

<sup>13</sup> In Study 4, we attempted to control goal-related variables by referring to Fujita et al. (2007). Specifically, we considered participants perception of task feasibility and measured it with self-efficacy. We also considered participants’ desire for goal attainment in performing our tasks and measured their task commitment on a seven-point Likert scale, where one equals strongly disagree and seven equals strongly agree. In Study 4, we designed another question: “What is the reward you get from participating in this experiment?” Participants in Study 4 answered this question on a seven-point Likert scale, where one equals money and seven equals learning new words. The answers in Study 4 (M � 3.74, SD � 1.53) indicate that the participants did not merely care about money in the experiment. The items are listed in Online Appendix E.

<sup>14</sup> We recruited 169 participants, 25 of whom were excluded because of technical problems (i.e., failing to open the experimental website, getting disconnected from the Zoom breakout room during the experiment) and 19 were excluded because they failed to correctly answer the manipulation check questions.

<sup>15</sup> We also conducted ordinary least squares regression in Studies 2–4 to verify the effects of on-the-hour time points with age, gender, and other variables as control variables. The results (see Online Appendix G) are consistent with our findings in the manuscript.

## References

Alavi M, Leidner D (2001) Research commentary: Technology medi ated learning—A call for greater depth and breadth of research. Inform. Systems Res. 12(1):1–10.

Allen EJ, Dechow PM, Pope DG, Wu G (2017) Reference-dependent preferences: Evidence from marathon runners. Management Sci. 63(6):1657–1672.

Animesh A, Pinsonneault A, Yang S, Oh W (2011) An odyssey into virtual worlds: Exploring the impacts of technological and special environments on intention to purchase virtual products. MIS Quart. 35(3):789–810.

Argo JJ, Dahl DW, Manchanda RV (2005) The influence of a mere social presence in a retail context. J. Consumer Res. 32(2):207–212.

Ariely D, Bracha A, Meier S (2009) Doing good or doing well? Image motivation and monetary incentives in behaving prosocially. Amer. Econom. Rev. 99(1):544–555.

Balasubramanian N, Lee J, Sivadasan J (2018) Deadlines, workflows, task sorting, and work quality. Management Sci. 64(4):1804–1824.

Bell BS, Kozlowski SW (2002) Adaptive guidance: Enhancing self regulation, knowledge, and performance in technology-based training. Personnel Psych. 55(2):267–306.

Brandstatter V, Frank E (2002) Effects of deliberative and implemental mindsets on persistence in goal-directed behavior. Personal ity Soc. Psych. Bull. 28(10):1366–1378.

Brown K (2001) Using computers to deliver training: Which employees learn and why? Personnel Psych. 54(2):271–296.

Bruning JL, Capage JE, Kozuh GF, Young PF, Young WE (1968) Socially induced drive and range of cue utilization. J. Personality Soc. Psych. 9(3):242–244.

Buttner OB, Wieber F, Schulz AM, Bayer UC, Florack A, Gollwitzer PM (2014) Visual attention and goal pursuit: Deliberative and implemental mindsets affect breadth of attention. Personality Soc. Psych. Bull. 40(10):1248–1259.

Chandran S, Morwitz VG (2005) Effects of participative pricing on consumers’ cognitions and actions: A goal theoretic perspective. J. Consumer Res. 32(2):249–259.

Cobb SC (2009) Social presence and online learning: A current view from a research perspective. J. Interactive Online Learn. 8(3):241–254.

Dahl DW, Manchanda RV, Argo JJ (2001) Embarrassment in consumer purchase: The roles of social presence and purchase familiarity. J. Consumer Res. 28(3):473–481.

Dai H, Milkman KL, Riis J (2014) The fresh start effect: Temporal landmarks motivate aspirational behavior. Management Sci. 60(10): 2563–2582.

Dai H, Milkman KL, Riis J (2015) Put your imperfections behind you: Temporal landmarks spur goal initiation when they signal new beginnings. Psych. Sci. 26(12):1927–1936.

Dhar R, Huber J, Khan U (2007) The shopping momentum effect. J. Marketing Res. 44(3):370–378.

Duckworth AL, Milkman KL, Laibson D (2018) Beyond willpower: Strategies for reducing failures of self-control. Psych. Sci. Public Interest 19(3):102–129.

Franceschi K, Lee RM, Zanakis SH, Hinds D (2009) Engaging group e-learning in virtual worlds. J. Management Inform. Systems 26(1): 73–100.

Fujita K, Gollwitzer PM, Oettingen G (2007) Mindsets and preconscious open-mindedness to incidental information. J. Experi ment. Soc. Psych. 43(1):48–61.

Gabarron E, Lau AYS, Wynn R (2015) Is there a weekly pattern for health searches on Wikipedia and is the pattern unique to health topics? J. Medical Internet Res. 17(12):e286.

Gefen D, Straub DW (2004) Consumer trust in B2C e-commerce and the importance of social presence: Experiments in e-products and e-services. Omega 32(6):407–424.

Gollwitzer PM (1990) Action phases and mind-sets. Higgins ET, Sorrentino RM, eds. Handbook of Motivation and Cognition: Founda tions of Social Behavior (Guilford Press, New York), 53–92.

Gollwitzer PM, Brandstatter V (1997) Implementation intentions and effective goal pursuit. J. Personality Soc. Psych. 73(1):186–199.

Gollwitzer PM, Keller L (2016) Encyclopedia of Personality and Individ ual Differences (Springer, Cham, Switzerland).

Gollwitzer PM, Heckhausen H, Steller B (1990) Deliberative and imple mental mind-sets: Cognitive tuning toward congruous thoughts and information. J. Personality Soc. Psych. 59(6):1119–1127.

Gunawardena CN, Zittle FJ (1997) Social presence as a predictor of satisfaction with a computer-mediated conferencing environment. Amer. J. Distance Ed. 11(3):8–26.

Gupta S, Bostrom RP (2009) Technology-mediated learning: A comprehensive theoretical model. J. Assoc. Inform. Systems 10(9):686–714.

Hanus MD, Fox J (2015) Assessing the effects of gamification in the classroom: A longitudinal study on intrinsic motivation, social comparison, satisfaction, effort, and academic performance. Comput. Ed. 80:152–161.

Hayes AF (2013) Introduction to Mediation, Moderation, and Conditional Process Analysis: A Regression-Based Approach (Guilford Press, New York).

Huang N, Zhang J, Burtch G, Li X, Chen P (2020) Combating procrastination on massive online open courses via optimal calls to action. Inform. Systems Res. 32(2):301–316.

Huguet P, Galvaing MP, Monteil JM, Dumas F (1999) Social presence effects in the Stroop task: Further evidence for an attentional view of social facilitation. J. Personality Soc. Psych. 77(5):1011–1025.

Isaac MS, Schindler RM (2013) The top-ten effect: Consumers’ subjective categorizations of ranked lists. J. Consumer Res. 40(6): 1181–1202.

Kehrwald B (2008) Understanding social presence in text-based online learning environments. Distance Ed. 29(1):89–106.

Kizilcec RF, Halawa S (2015) Attrition and achievement gaps in online learning. Proc. Second ACM Conf. Learn. Scale (Association for Computing Machinery, New York), 57–66.

Kizilcec RF, Perez-Sanagustin M, Maldonado JJ (2017) Self-regulated learning strategies predict learner behavior and goal attainment in massive open online courses. Comput. Ed. 104:18–33.

Latane B (1981) The psychology of social impact. Amer. Psych. 36(4): 343–356.

Lavoie JAA, Pychyl TA (2001) Cyberslacking and the procrastination superhighway: A web-based survey of online procrastination, attitudes, and emotion. Soc. Sci. Comput. Rev. 19(4):431–444

Leary MR, Kowalski RM (1990) Impression management: A literature review and two-component model. Psych. Bull. 107(1):34–47.

Lee L, Ariely D (2006) Shopping goals, goal concreteness, and condi tional promotions. J. Consumer Res. 33(1):60–70.

Liu D, Santhanam R, Webster J (2017) Toward meaningful engagement: A framework for design and research of gamified infor mation systems. MIS Quart. 41(4):1011–1034.

Milkman KL, Rogers T, Bazerman MH (2008) Harnessing our inner angels and demons: What we have learned about want/should conflicts and how that knowledge can help us reduce shortsighted decision making. Perspect. Psych. Sci. 3(4):324–338.

Muller D, Butera F (2007) The focusing effect of self-evaluation threat in coaction and social comparison. J. Personality Soc. Psych. 93(2): 194–211.

Muller D, Atzeni T, Butera F (2004) Coaction and upward social comparison reduce illusory conjunction effect: Some support for distraction-conflict theory. J. Experiment. Soc. Psych. 40:659–665.

Nawrot I, Doucet A (2014) Building engagement for MOOC students: Introducing support for time management on online learning platforms. Proc. 23rd Internat. Conf. World Wide Web (Association for Computing Machinery, New York), 1077–1082.

Orbell S, Sheeran P (2000) Motivational and volitional processes in action initiation: A field study of the role of implementation inten tions. J. Appl. Soc. Psych. 30(4):780–797.

Pavlou PA, Liang H, Xue Y (2007) Understanding and mitigating uncertainty in online exchange relationships: A principal–agent perspective. MIS Quart. 31(1):105–136.

Picciano AG (2002) Beyond student perceptions: Issues of interaction, presence, and performance in an online course. J. Asyn chronous Learn. Networks 6(1):21–40.

Rai D, Lin CWW, Ierlan MT (2016) The influence of scheduling style on assortment size. Management Marketing 11(4):553–565.

Richardson JC, Maeda Y, Lv J, Caskurlu S (2017) Social presence in relation to students’ satisfaction and learning in the online learning environment: A meta-analysis. Comput. Human Behav. 71:402–417.

Santhanam R, Liu D, Shen W (2016) Research note-gamification of technology-mediated training: Not all competitions are the same Inform. Systems Res. 27(2):453–465.

Santhanam R, Sasidharan S, Webster J (2008) Using self-regulatory learning to enhance e-learning-based information technology training. Inform. Systems Res. 19(1):26–47.

Sellier AL, Avnet T (2014) So what if the clock strikes? Scheduling style, control, and well-being. J. Personality Soc. Psych. 107(5):791–808.

Sellier AL, Avnet T (2019) Scheduling styles. Current Opinions Psych. 26:76–79.

Shoham M, Moldovan S, Steinhart Y (2018) Mind the gap: How smaller numerical differences can increase product attractiveness. J. Consumer Res. 45(4):761–774.

Short J, Williams E, Christie B (1976) The Social Psychology of Telecom munications (Wiley, London).

Taylor SE, Gollwitzer PM (1995) Effects of mindset on positive illu sions. J. Personality Soc. Psych. 69(2):213–226.

Thatcher A, Wretschko G, Fridjhon P (2008) Online flow experi ences, problematic Internet use and Internet procrastination. Comput. Human Behav. 24(5):2236–2254.

Tu CH, Mcisaac MS (2002) An examination of social presence to increase interaction in online classes. Amer. J. Distance Ed. 16(3):131–150.

Tu Y, Soman D (2014) The categorization of time and its impact on task initiation. J. Consumer Res. 41(3):810–822.

Zajonc RB (1965) Social facilitation. Science 149(3681):269–274.

Zhan Z, Mei H (2013) Academic self-concept and social presence in face-to-face and online learning: Perceptions and effects on students’ learning achievement and satisfaction across environments. Comput. Ed. 69:131–138.

Zhang D, Zhao JL, Zhou L, Nunamaker JF (2004) Can e-learning replace classroom learning? Comm. ACM 47(5):75–79.

Zhang Z, Zhang Z, Chen P (2021) Early bird vs. late owl: An empiri cal investigation of individual shopping time habit and its effects. MIS Quart. 45(1):117–162.

Zhao M, Lee L, Soman D (2012) Crossing the virtual boundary: The effect of task-irrelevant environmental cues on task implemen tation. Psych. Sci. 23(10):1200–1207.

Zwebner Y, Schrift RY (2020) On my own: The aversion to being observed during the preference-construction stage. J. Consumer Res. 47(4):475–499.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>
