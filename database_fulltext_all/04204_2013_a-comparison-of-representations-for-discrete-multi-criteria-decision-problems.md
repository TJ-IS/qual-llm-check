---
otero_id: 4204
otero_key: "CEMAET9S"
title: "A comparison of representations for discrete multi-criteria decision problems"
authors: "Johannes Gettinger; Elmar Kiesling; Christian Stummer; Rudolf Vetschera"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.023"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A comparison of representations for discrete multi-criteria decision problems ☆

Johannes Gettinger <sup>a</sup>, Elmar Kiesling <sup>b</sup>, Christian Stummer <sup>c</sup>, Rudolf Vetschera <sup>d,</sup>⁎

<sup>a</sup> Institute of Interorganisational Management and Performance, University of Hohenheim, Stuttgart, Germany

<sup>b</sup> Institute of Software Technology and Interactive Systems, Vienna University of Technology, Vienna, Austria

<sup>c</sup> Faculty of Business Administration and Economics, Bielefeld University, Bielefeld, Germany

<sup>d</sup> Department of Business Administration, University of Vienna, Vienna, Austria

## a r t i c l e i n f o

Article history: Received 16 March 2011 Received in revised form 27 September 2012 Accepted 7 October 2012 Available online 13 October 2012

Keywords: Multi-criteria decision analysis Visualization Parallel coordinates Heatmaps

## a b s t r a c t

Discrete multi-criteria decision problems with numerous Pareto-ef<sup>fi</sup>cient solution candidates place a signi<sup>fi</sup>cant cognitive burden on the decision maker. An interactive, aspiration-based search process that iteratively progresses toward the most preferred solution can alleviate this task. In this paper, we study three ways of representing such problems in a DSS, and compare them in a laboratory experiment using subjective and objective measures of the decision process as well as solution quality and problem understanding. In addition to an immediate user evaluation, we performed a re-evaluation several weeks later. Furthermore, we consider several levels of problem complexity and user characteristics. Results indicate that different problem representations have a considerable in<sup>fl</sup>uence on search behavior, although long-term consistency appears to remain unaffected. We also found interesting discrepancies between subjective evaluations and objective measures. Conclusions from our experiments can help designers of DSS for large multi-criteria decision problems to <sup>fi</sup>t problem representations to the goals of their system and the speci<sup>fi</sup>c task at hand.

© 2012 Elsevier B.V. All rights reserved

## 1. Introduction

Many decision problems involve multiple, con<sup>fl</sup>icting, and incommensurate criteria. Methods of multi-criteria decision analysis aim at supporting decision makers (DMs) in such tasks. In discrete decision problems the number of solutions is <sup>fi</sup>nite, but may comprise hundreds, if not thousands of alternatives. Portfolio selection problems, in which collections of items (e.g., projects) are evaluated according to several properties, may serve as a prominent example. They can be tackled by a two phase-process: In the <sup>fi</sup>rst phase, (an approximation of) the set of ef<sup>fi</sup>cient alternatives is determined. In the second phase, DMs interactively explore this set in order to identify their most preferred solution. (For alternative approaches that avoid the task of initially generating all the ef<sup>fi</sup>cient solutions cf., e.g., [29,69].) Various interactive procedures may be used for this purpose. In particular, aspiration-based approaches have turned out to be useful tools. Applications have been reported from various <sup>fi</sup>elds such as information technology management [45], research and development management [54], radiation therapy treatment planning [20], strategic technology planning in hospital management [21], and municipal wastewater treatment [23].

Recently, advances in the development of algorithms and increased computing power have led to considerable improvements concerning the <sup>fi</sup>rst phase. Heuristic solution procedures can generate adequate approximations of the set of ef<sup>fi</sup>cient solutions to complex problems in reasonable time. In contrast, DMs' interactive search processes and their support through suitable problem representations are still poorly understood. So far, only few studies have examined user behavior during interactive, aspiration-based search [9,10,63]. These studies mainly focused on the process itself and the impact of different interactive methods. In this paper, we aim to link the behavioral and the technical aspects of supporting DMs and study the impact of three problem representations on the interactive search process. Although the importance of using an appropriate problem representation has been clearly identi-<sup>fi</sup>ed in the literature [19,25], and many visualization methods have been proposed for multi-criteria problems [30], this topic has not yet received suf<sup>fi</sup>cient attention [64].

We conducted a series of laboratory experiments, in which we studied the impact of problem representation on a wide range of outcome dimensions, encompassing subjective as well as objective measures of the decision process and solution quality. Measuring solution quality of multi-criteria decision methods is a dif<sup>fi</sup>cult issue. The attempt to verify it in an objective way leads to a paradox: The solution to a multi-criteria problem is by de<sup>fi</sup>nition subjective, since it is based on the DM's preferences. Therefore, any evaluation of solution quality must involve the DM. However, DMs need decision support exactly because it is dif<sup>fi</sup>cult for them to evaluate alternatives directly. Consequently, many empirical studies (e.g., [51]) use criteria such as con<sup>fi</sup>dence or perceived quality of a solution. We complement an immediate subjective evaluation with a two-stage approach, in which we asked subjects to re-evaluate alternatives several weeks after the original experiment. Although in reality a decision would be made immediately after using the system, consistency between the original decision and the ex-post test can be considered as an additional indicator that the original evaluation has re<sup>fl</sup>ected the subject's preferences. Similar retest methods are quite often used to evaluate preference elicitation methods [22,24].

The present study compares two visual representations, parallel coordinate plots and heatmaps, to numerical tables using a wide range of output dimensions. It builds upon and extends a previous study [28], in which we only focused on the graphical problem representations and a few immediate output dimensions.

The remainder of this paper is organized as follows: Section 2 describes the problem representations used in the experiments. Research questions are then presented in Section 3, followed by a description of the experimental design in Section 4. Section 5 explains the measurement methods, and the results are presented and discussed in Sections 6 and 7. The paper concludes in Section 8 with a summary and an outlook on further research.

## 2. Problem representations

The decision procedure applied in our experiments follows an a posteriori preference approach. Preferences are only implicitly articulated in the free search process by setting threshold levels for criteria, which de<sup>fi</sup>ne the set of admissible solutions (following the seminal work by [57]). During this search process, the problem representation must support a two-way interaction between user and system. The system conveys information about the entire range of ef<sup>fi</sup>cient solutions and their criteria values. Using the same representation, the user speci<sup>fi</sup>es and later on modi<sup>fi</sup>es the threshold levels for each criterion. The system then should provide immediate feedback on the effect of such <sup>fi</sup>ltering steps by indicating which solution candidates remain admissible.

In this paper, we focus on three possible problem representations: (i) tables, (ii) heatmaps, and (iii) parallel coordinate plots (PCP). They are representative of many other options (for a similar research approach cf. [31]).

## 2.1. Tables

Tables are the only non-graphical representation used in our experiments. In our implementation, criteria are assigned to columns and alternatives to rows. DMs can specify upper and/or lower bounds for criteria by right-clicking on a cell and selecting the appropriate action from the context menu. Note that the entire row will be highlighted, but nonetheless the constraints are determined only by the value in that particular cell. Constraints can be modi<sup>fi</sup>ed or completely removed in later stages. Furthermore, alternatives can be sorted by ascending or descending criterion values. Fig. 1 illustrates this representation as used in the actual experiment.

## 2.2. Heatmaps

Heatmaps represent an innovative variation of traditional tables; they are structurally similar to tables, but provide a more holistic perspective. This could be particularly helpful in problems involving numerous alternatives. In essence, heatmaps are matrices in which the cells are colored according to their values [15]. The high information density of this representation facilitates the identi<sup>fi</sup>cation of patterns such as correlations and trade-offs between criteria.

The use of (clustered) heatmaps for visualization originated in data mining, particularly in molecular biology and clinical applications (e.g., [67]). More recently their use as a means for visualizing the Pareto frontier was proposed by Pyrke et al. [47] and Lotov and Miettinen [38].

In our implementation, each column represents a criterion and each row represents an alternative. Cell colors refer to the relative value of a criterion for a particular solution. An example is provided in Fig. 2. We used a trichromatic mapping in which poor criterion values are represented by shades of red, medium values by shades of yellow, and premium values by shades of green. This mapping corresponds to the intuitive “stop light” color scheme that should be easy to grasp for users.

<table><tr><td>Portfolio</td><td>ECTS</td><td>Spare time (h)</td><td>Avg. course evaluation score</td><td>Avg. lecturer evaluation score</td><td>Worst success rate</td><td>Avg. no. participants</td><td>Avg. grade</td></tr><tr><td>0</td><td>19,00</td><td>84,00</td><td>7,40</td><td>7,98</td><td>0,79</td><td>39,25</td><td>3,31</td></tr><tr><td>1</td><td>34,00</td><td>64,83</td><td>7,36</td><td>7,84</td><td>0,66</td><td>73,71</td><td>3,33</td></tr><tr><td>2</td><td>10,00</td><td>86,50</td><td>7,93</td><td>8,63</td><td>0,79</td><td>20,00</td><td>3,27</td></tr><tr><td>3</td><td>41,00</td><td>69,00</td><td>6,39</td><td>6,78</td><td>0,30</td><td>68,44</td><td>3,67</td></tr><tr><td>4</td><td>33,00</td><td>63,50</td><td>6,61</td><td>7,26</td><td>0,58</td><td>43,86</td><td>3,57</td></tr><tr><td>5</td><td>30,00</td><td>71,50</td><td>7,03</td><td>8,10</td><td>0,74</td><td>76,29</td><td>3,37</td></tr><tr><td>6</td><td>43,00</td><td>60,00</td><td>6,54</td><td>6,90</td><td>0,31</td><td>49,44</td><td>3,69</td></tr><tr><td>7</td><td>41,00</td><td>63,50</td><td rowspan="3" colspan="2">Set as minimumSet as maximumReset criterionReset all</td><td>0,31</td><td>54,00</td><td>3,57</td></tr><tr><td>8</td><td>12,00</td><td>90,00</td><td>0,74</td><td>109,50</td><td>3,23</td></tr><tr><td>9</td><td>37,00</td><td>64,83</td><td>0,64</td><td>60,25</td><td>3,40</td></tr><tr><td>10</td><td>19,00</td><td>81,50</td><td>7,08</td><td>7,65</td><td>0,72</td><td>52,50</td><td>3,19</td></tr><tr><td>11</td><td>21,00</td><td>80,00</td><td>7,24</td><td>7,78</td><td>0,79</td><td>71,80</td><td>3,29</td></tr><tr><td>12</td><td>33,00</td><td>68,50</td><td>7,06</td><td>7,79</td><td>0,31</td><td>30,71</td><td>3,46</td></tr><tr><td>13</td><td>13,00</td><td>83,00</td><td>7,98</td><td>8,85</td><td>0,74</td><td>34,25</td><td>3,13</td></tr><tr><td>14</td><td>11,00</td><td>86,00</td><td>7,87</td><td>8,93</td><td>0,74</td><td>81,67</td><td>3,32</td></tr><tr><td>15</td><td>39,00</td><td>61,50</td><td>7,03</td><td>7,36</td><td>0,31</td><td>37,00</td><td>3,54</td></tr><tr><td>16</td><td>11,00</td><td>86,50</td><td>7,87</td><td>8,77</td><td>0,74</td><td>83,00</td><td>3,42</td></tr><tr><td>17</td><td>25,00</td><td>77,00</td><td>7,20</td><td>8,15</td><td>0,74</td><td>32,00</td><td>3,25</td></tr><tr><td>18</td><td>38,00</td><td>69,00</td><td>6,30</td><td>6,63</td><td>0,31</td><td>55,75</td><td>3,71</td></tr><tr><td>19</td><td>35,00</td><td>72,00</td><td>6,06</td><td>6,15</td><td>0,50</td><td>54,63</td><td>3,71</td></tr></table>

Fig. 1. Table representation (screen capture).

![](/api/attachments/CEMAET9S/fulltext/images/08abadd8a4cea006300cca0319a48772926f9b0bf7e1e5ba69cd69d98db0770b.jpg)  
Fig. 2. Heatmap visualization (screen capture).

The interaction mechanism works similar to the one for tables. Again, users can impose bounds to reduce the set of admissible solutions, reset these bounds, and sort alternatives via a context menu.

## 2.3. Parallel coordinate plots

Parallel coordinate plots [26] have been chosen as a fundamentally different third problem presentation because they can display several criteria without drastically increasing the complexity of the display or the cognitive burden on the DM. Furthermore, they allow for the implementation of user-friendly mechanisms for manipulating aspiration levels. In PCP, criteria values are displayed on separate axes laid out in parallel. Alternatives are depicted as pro<sup>fi</sup>le lines that connect points on the respective axes. The pro<sup>fi</sup>le lines of all admissible solutions are superimposed. This representation can be easily interpreted geometrically and provides a good overview of the distribution of values. Patterns such as positive or negative correlations can easily be identi<sup>fi</sup>ed in criteria laid out next to each other.

To set thresholds for criteria, users drag bars to mark the desired intervals. During dragging, the system indicates which solution candidates will be eliminated, thus providing the DM with immediate visual feedback. For an example see Fig. 3.

## 3. Research questions

Cognitive <sup>fi</sup>t theory postulates that a match of task and problem presentation improves decision performance in terms of time and/or accuracy [59,62]. The best performance is reached when symbolic tasks are supported by symbolic representation formats and when spatial tasks are supported by spatial representation formats. Symbolic tasks typically require the handling of precise data values, such as extracting and acting on values. In contrast, spatial tasks require a holistic assessment of the problem such as making associations, perceiving relationships, or interpolating values.

Graphical representations are spatial in nature and facilitate the acquisition of information in two ways. Firstly, they focus on single elements and secondly, they establish associations among values [59,60,62]. The sequential structure of PCP supports a large number of perceptual inferences at very low cognitive costs [7,33]. Moreover, the immediate feedback as well as the easy modi<sup>fi</sup>cation of thresholds should facilitate an exploratory approach when investigating the solution space. In contrast, tables are symbolic representations and present data in separable items and convey single point values more accurately than other formats [4,5,17,50]. This should support DMs particularly in the <sup>fi</sup>nal steps of the decision making process, when the last remaining alternatives are to be compared. Heatmaps exhibit both characteristics by enabling the visualization of high density information and providing exact data values in the cells.

Research has shown that expertise with the support provided leads to a reduction in decision time [14,34,43]. As we expect DMs to be familiar with tables and PCP but not with heatmaps, the use of heatmaps should result in longer decision time. Furthermore, the holistic nature of visual representations is expected to in<sup>fl</sup>uence the structure of the decision process. We expect DMs provided with either heatmaps or PCP to strongly oscillate the number of admissible portfolios over time by performing more <sup>fi</sup>ltering steps reducing as well as increasing the number of admissible portfolios. Therefore, in total, the use of heatmaps or PCP is expected to lead to a more explorative search behavior. These propositions result in our <sup>fi</sup>rst research question:

Research Question RQ1: How do the different problem representations, i.e., heatmaps, PCP, or tables, in<sup>fl</sup>uence the duration and the structure of multi-criteria decision processes?

Users of information technology search for a cognitive trade-off between the perceived effort of using a technology and its perceived usefulness and accuracy [16,61]. Prior experience enables DMs to use stable heuristics that require less effort [40,62]. DMs that experience more effort perceive the results as less accurate [1]. Accuracy of decisions is strongly related to decision quality that is typically linked to con<sup>fi</sup>dence in the decision [27,51,58].

At the very beginning of the selection process, DMs face a vast number of ef<sup>fi</sup>cient alternatives and need to limit their effort by using noncompensatory strategies such as elimination-by-aspect, lexicographic rules, or conjunctive strategies [13,31,32]. In a later stage of the process,

![](/api/attachments/CEMAET9S/fulltext/images/7dd0fd4c8c600363e5319070b320cb037fe5578cefddaba3d71d7ab1d759f572.jpg)  
Fig. 3. Parallel coordinate plot (screen capture).

DMs focus on fewer alternatives and refer to compensatory strategies and explicit trade-offs. The latter task was shown to increase decisional con<sup>fl</sup>ict and lower post-decisional con<sup>fi</sup>dence [1,32].

Due to their characteristics, heatmaps should provide the best support for non-compensatory strategies. Compensatory strategies are explicitly supported by PCP via their geometric interpretability [7,33]. In contrast, DMs supported by tables and heatmaps have to engage explicitly in trade-off tasks. We therefore expect DMs provided with either PCP or tables to perceive the <sup>fi</sup>nal solution as more accurate and the representation as more user-friendly. Furthermore, we expect DMs provided with PCP to perceive less decisional con<sup>fl</sup>ict and effort. These assumptions lead to the second research question:

Research Question RQ2: How do the different problem representations, i.e., heatmaps, PCP, or tables, in<sup>fl</sup>uence users' perception of the quality and effort of the multi-criteria decision process?

Task complexity is de<sup>fi</sup>ned as the cognitive burden placed on the DM and results from the number of criteria and alternatives involved [11,68]. A higher level of task complexity requires more effort from the DM and results in an increase in decision time and/or a decrease in decision quality. This in turn leads to lower con<sup>fi</sup>dence in the solution [8,41,55]. Moreover, decisional con<sup>fl</sup>ict and perceived effort are negatively related to users' attitudes toward the system [1,12]. However, effort is also positively related to decision quality, which increases decision con<sup>fi</sup>dence and consequently perceived usefulness of the system [27].

In PCP, all alternatives are visualized in a display of <sup>fi</sup>xed size. Therefore, an increase in the number of alternatives leads to an increase in information density and visual complexity. This makes it more dif<sup>fi</sup>cult for the DM to observe individual values and detect relationships in the data. In contrast, tabular representations can be extended by adding more rows. However, due to the fact that subjects have to scroll more to observe all alternatives when using tables, we expect them to need more time in more complex tasks. These differences should be re<sup>fl</sup>ected in subjective as well as objective measures (as de<sup>fi</sup>ned in Section 5) of the process, especially for DMs provided with PCP compared to heatmaps or tables:

Research Question RQ3: How does the level of problem complexity in<sup>fl</sup>uence subjective and objective measures of the multi-criteria decision process and the outcome for the different problem representations?

In addition to the task-technology <sup>fi</sup>t, recent research highlights the importance of DMs' cognitive characteristics [36]. Decision-making style refers to the way individuals process information in order to solve problems. It is de<sup>fi</sup>ned as a stable learned habitual response pattern based on cognitive abilities used in decision situations [49,56]. Scott and Bruce [49] de<sup>fi</sup>ne <sup>fi</sup>ve behavioral dimensions based on DMs' self-evaluation: (i) a rational, (ii) an intuitive, (iii) a dependent, (iv) an avoidant, and (v) a spontaneous style. Studies have shown that even though an individual may have a predominant style, decision styles are not mutually exclusive [37,53,56].

Empirical research contends that gender has no in<sup>fl</sup>uence on the preferred decision making style [37,53]. Similarly, recent research indicates that gender differences in adoption and use of technology do not exist anymore for younger subjects [44]. Therefore, we expect the decision making style to have an impact on subjective as well as on objective outcome dimensions, while we do not expect gender to have an impact on either dimension:

Research Question RQ4: How do individual characteristics of a DM such as decision making style or gender in<sup>fl</sup>uence subjective and objective measures of the multi-criteria decision process and outcome?

Understanding of concepts consists of three components: DMs <sup>fi</sup>rst have to develop connections between internal mental structures (building), then reach the state of having these connections available at a given time (having), and <sup>fi</sup>nally to use the connections to solve a problem or construct a response to a question (enacting) [18]. A DM understanding a concept should be able to see its deeper characteristics, look for speci<sup>fi</sup>c information more quickly, draw analogies, or put it in simpler terms [3,46].

Empirical research has shown that the sequential structure of spatial information presentation makes it easier for DMs to “get the message”

when large amounts of quantitative information are presented [17,50]. In contrast, tables support comprehension of discrete values, while heatmaps again take an intermediate position.

Research Question RQ5: How do the three problem representations, i.e., heatmaps, PCP, or tables, in<sup>fl</sup>uence users' understanding of the decision problem?

In one of the earliest studies about the impact of information representation on ex-post tests, tables were found to provide best support for the recall of speci<sup>fi</sup>c values [42,65]. In contrast, Umanath and Scamell [58] report that using graphs provides better support than tables for recall tasks that involve pattern recognition. However, they do not <sup>fi</sup>nd any differences in recall performance for factual information due to the presentation format.

Watson and Driver [66] examined the impact of three-dimensional graphics and tables on subjects' performance in immediate and ex-post evaluation. Subjects performed a ranking task – similar to the task used in the present paper – directly after receiving the information and four weeks later. While neither representation format provided superior support, re-evaluation performance drastically decreased over time.

Research Question RQ6: How do the three problem representations, i.e., heatmaps, PCP, or tables, in<sup>fl</sup>uence users' performance in ex-post tests?

## 4. Experimental design

We conducted a controlled experiment that adopted a between subject approach. Treatments consisted of different problem representations (tables, heatmaps, PCP) and problem complexity levels (simple vs. complex), which affected the number of criteria as well as of ef<sup>fi</sup>cient solutions. To provide a realistic background for our experiment, we used a portfolio-type problem with which student subjects could readily identify. At Austrian universities, students are not provided with a ready-made schedule, but are free to set it up individually. The selection of courses for a semester is a multi-criteria portfolio problem. By using this familiar task, we achieved a high level of identi<sup>fi</sup>cation with the problem.

## 4.1. Problem setting

In the “simple problem” treatment, three criteria were used: Total number of ECTS (European Credit Transfer System) points obtained (maximize), total remaining spare time per week (maximize), and average evaluation of the courses by students in previous semesters (maximize). In the “complex problem” treatment, four more criteria were added: Average evaluation score of lecturers by students in previous semesters (maximize), percentage of students who passed the course having the lowest pass rate in the selected course schedule (maximize), prospective average number of students in class (minimize), and average grade obtained by students in past courses. Since grades in the Austrian system are represented by numbers, one representing the best grade, this criterion was also minimized.

Sets of ef<sup>fi</sup>cient course packages for both problem instances were calculated using actual data on 31 Bachelor-level courses offered at the University of Vienna. Ef<sup>fi</sup>cient alternatives were identi<sup>fi</sup>ed by completely enumerating all $2 ^ { 3 1 } { > } 2 ^ { \cdot } 1 0 ^ { 9 }$ combinations, eliminating infeasible combinations and conducting pairwise dominance checks.

In total, there are 331 ef<sup>fi</sup>cient solutions in the simple problem and 2614 ef<sup>fi</sup>cient solutions in the complex problem. While the complete set was used for the simple problem, only 999 randomly selected alternatives were used in the complex problem, since using all solutions would have slightly degraded the responsiveness of the system.

All problem representations were implemented in C# on Windows. The program automatically recorded and time-stamped each action performed by subjects. During experiments, the program was simultaneously run on 15 identical computers in a computer lab.

## 4.2. Procedure

The main part of our experiment consisted of a scripted verbal introduction, a training session, a scripted explanation of the problem setting, the actual course selection exercise, and an online survey. Total time for a complete session was about 45 min. Three weeks after the main experiment, an ex-post evaluation task was performed.

At the beginning of a session, the scripted verbal introduction brie<sup>fl</sup>y demonstrated the problem representation used in the respective treatment. Then, a training session that used a simple, generic problem instance involving 15 randomly generated ef<sup>fi</sup>cient alternatives and the same number of criteria as the actual treatment was completed by each participant.

Next, the class schedule selection task was explained to participants. In order to ensure uniformity and control across groups, questions were generally not entertained. However, a written summary was available to all subjects during the experiment. In the exercise, subjects had to narrow down the set of admissible alternatives and <sup>fi</sup>nally indicate their most preferred option. They could then terminate the process and proceed to the survey. A maximum time limit of 15 min was allowed for the task and shown as a countdown on screen. Finally, a ten-page online survey was used to collect demographic information, elicit subjective outcome measures, and test problem understanding. We conducted a thorough pre-test of the whole setup that involved <sup>fi</sup>ve subjects.

The ex-post test took place three weeks after completion of each experimental session. Subjects were e-mailed a link to a web-based questionnaire that presented descriptions (criteria values) of <sup>fi</sup>ve alternatives. These alternatives were selected individually for each subject to make sure that they represented a range of class schedules eliminated during different stages of the main experiment. Subjects had to rank these alternatives according to their preferences.

## 4.3. Participants

Subjects were recruited from various classes in the undergraduate and graduate business administration programs at the University of Vienna, Austria. As an incentive for participation, a lottery was held in which twelve brand name MP3 music players were distributed among subjects. The 148 subjects were assigned to one of 21 groups. All subjects in a group solved the same problem under the same treatment conditions. Table 1 provides an overview of the sample composition and the distribution across treatments.

All subjects were pro<sup>fi</sup>cient in the use of personal computers. The mean age of subjects was 24.13 years (SD=2.32). Participation in the experiment was voluntary. It was pointed out to subjects that the “diligent execution” of all tasks was a necessary requirement for entering the lottery drawings.

## 5. Measurement of variables

Our research questions relate the factors problem representation, problem complexity, and user characteristics to process characteristics, subjective evaluations, problem understanding, and consistency in the ex-post test. The two factors problem representation and problem complexity are de<sup>fi</sup>ned by our experimental procedure. Since the subject population was quite homogeneous, we used gender as the only demographic variable, and considered decision styles as the most important user characteristic. Decision styles were measured via the instrument developed by Scott and Bruce [49].

Table 1 Sample composition and treatments.

<table><tr><td>Problem</td><td colspan="3">Simple</td><td colspan="3">Complex</td></tr><tr><td>Mode\Participants</td><td>Male</td><td>Female</td><td>Total</td><td>Male</td><td>Female</td><td>Total</td></tr><tr><td>Table</td><td>11</td><td>14</td><td>25</td><td>10</td><td>15</td><td>25</td></tr><tr><td>Heatmap</td><td>9</td><td>14</td><td>23</td><td>13</td><td>16</td><td>29</td></tr><tr><td>PCP</td><td>10</td><td>12</td><td>22</td><td>10</td><td>14</td><td>24</td></tr></table>

The <sup>fi</sup>rst two process measures refer to effort, measured by the total time spent and the number of filtering steps (i.e., changes in aspiration levels) performed by subjects. The latter measure more closely re<sup>fl</sup>ects the activities of subjects. However, large time intervals between actions could also indicate that subjects extensively deliberated each step. Using both measures in parallel provides a comprehensive picture of the effort objectively involved in the task.

The third process measure captures the “smoothness” of the process. In setting the thresholds, subjects could progressively “zoom in” toward the most preferred region in criteria space, or backtrack frequently to explore different regions. In the latter case, the number of admissible alternatives strongly oscillates over time. If a <sup>fi</sup>ltering step leads to an increase, rather than a decrease, in the number of admissible solutions, we label it as a “reversal” of the search process. The number of reversals is an indicator of explorative, backtracking behavior.

Even if the number of admissible alternatives decreases monotonically, subjects might follow very different convergence paths. They could <sup>fi</sup>rst tighten the bounds rather cautiously, and converge to their most preferred solution only at the end. Alternatively, they could quite rapidly focus on an interesting region, and then spend more time in local search. To capture these differences, we calculated the average number of admissible solutions (standardized by the number of ef<sup>fi</sup>cient alternatives) in the <sup>fi</sup>rst and last third of the process. The resulting measures are denoted average 1 and average 3.

Subjective measures represent evaluations of the decision process, its outcomes, and the system in general [63]. We used two measures developed by Aloysius et al. [1] for subjective evaluation of the process: Perceived effort and decisional conflict. Perceived effort is the subjective counterpart of the objective measures of effort, and decisional con<sup>fl</sup>ict measures the emotional burden, stress, and anxiety involved in decision making. To evaluate the subjective quality of the solution, we used the construct perceived accuracy, also developed by Aloysius et al. [1], which measures the con<sup>fi</sup>dence of users in having achieved the best solution.

Finally, subjects also provided a general evaluation of the system. Since the underlying method was the same in all treatments, differences directly relate to the problem representations. For this evaluation, we used the well-established Technology Acceptance Model (TAM) by Davis [16], which explains attitudes toward an information system via the constructs perceived usefulness and perceived ease of use. For both constructs, the original scales developed by Davis [16] were used.

In order to test subjects' understanding of the problem, they had to provide estimates of three average values of criteria across all alternatives, and estimates of three correlations between criteria. Averages were provided as numerical values, correlations on a seven point scale ranging from “It was very dif<sup>fi</sup>cult to obtain good values in both criteria” to “… very easy …”, recoded to values between −1 and +1. For both types of questions, relative deviations from true values were calculated and averaged across questions of the same type. Since the correlation questions in the simple and complex treatment involved different criteria, we also computed deviations only for the <sup>fi</sup>rst correlation question, which was identical in both treatments.

In the ex-post test, rankings of <sup>fi</sup>ve selected class schedules elicited three weeks after the experiment were compared to the ranking of the same class schedules during the experiment. Since the experiment did not directly generate a ranking, we inferred it from the process.

Assuming that alternatives are roughly eliminated according to preference, we used the number of the last step in which the class schedule was admissible for this purpose. Two measures were used to compare the two rankings. The <sup>fi</sup>rst is the ex-post evaluation rank of the alternative selected in the experiment. The second measure is the sum of absolute differences in the ranks of all <sup>fi</sup>ve class schedules and therefore checks consistency across the entire range of solutions. However, the measurement may have been distorted to some degree by unforeseeable factors such as subjects having changed their mind in the meantime.

## 6. Results

We <sup>fi</sup>rst performed con<sup>fi</sup>rmatory factor analyses for decision styles and multi-item subjective evaluation variables to test the validity of constructs used in our research.<sup>1</sup> These analyses mostly con-<sup>fi</sup>rmed the theoretical assignment of items to constructs. Concerning decision styles, the only deviation from theoretical assignments was that one item of the spontaneous style exhibited a loading >0.4 on a factor related to the intuitive style. The analysis of subjective evaluation constructs indicated that one item intended for perceived effort instead loaded on the factor related to decisional con<sup>fl</sup>ict. However, given the theoretical foundation of both scales, as well as the suf<sup>fi</sup>- ciently high values of Cronbach's alpha for all constructs in question (0.855 for spontaneous and 0.814 for intuitive decision styles, 0.761 for decisional con<sup>fl</sup>ict, and 0.683 for perceived effort), we decided to retain the original assignment of items to constructs.

Although subjects were recruited from a quite homogeneous population of students, they are still quite different in terms of their decision styles. Fig. 4 shows the distribution of the <sup>fi</sup>ve dimensions of decision styles used in our analysis. All styles exhibit a considerable range of values. This makes it possible to use decision styles as independent variables in the following analyses.

To analyze the research questions formulated in Section 3, we performed several regression analyses of the relevant outcome dimensions (process, subjective evaluation, problem understanding, and the ex-post test) on experimental factors, user characteristics, and their interactions. Regression results are summarized in Table 2. In all regressions, problem representations were coded using tables as reference categories. Table 2 thus shows coef<sup>fi</sup>cients indicating the difference of heatmaps and PCP in comparison to tables.

Problem representations, in particular PCP, exhibit a consistent and signi<sup>fi</sup>cant effect on process variables. Users of PCP performed signi<sup>fi</sup>- cantly more <sup>fi</sup>ltering steps (i.e., changes in aspiration levels) and backtracked signi<sup>fi</sup>cantly more often, but nevertheless managed to have fewer admissible solutions throughout the process. While total time is also reduced by the use of PCP, this effect is not re<sup>fl</sup>ected in a statistically signi<sup>fi</sup>cant coef<sup>fi</sup>cient. As Fig. 5 shows, the difference between heatmaps and PCP is even larger than the one between tables and PCP. In Figs. 5 and 6, treatment groups are identi<sup>fi</sup>ed by problem representation and complexity level, e.g. “Table/3” indicates the treatment group using tables and solving the three criteria (low complexity) problem. A regression analysis using heatmaps as reference category indicates that this difference is indeed signi<sup>fi</sup>cant (t=4.038,pb0.001).

We observed only few signi<sup>fi</sup>cant effects of our experimental factors on subjective evaluations. Subjects found heatmaps to be signi<sup>fi</sup>cantly less user-friendly than tables. Users of PCP experienced less decisional con<sup>fl</sup>ict and lower effort. In contrast to problem representation, decision making styles had some highly signi<sup>fi</sup>cant effects. Users who scored high on the rational dimension of their decision making style perceived the system both easier to use and more useful. This effect occurred regardless of the problem representation. Subjects who scored high on the dependent dimension experienced signi<sup>fi</sup>cantly more decisional con<sup>fl</sup>ict. Subjects with an avoiding decision style perceived the effort to be higher.

![](/api/attachments/CEMAET9S/fulltext/images/410dafe2b94349819c341935c8f718b8fe98404dce2a472967acba5f6c67bc42.jpg)  
Fig. 4. Distribution of scores in the <sup>fi</sup>ve dimensions of decision styles.

All problem representations lead to similar results in our measures of understanding. Since our regression analysis also did not indicate any signi<sup>fi</sup>cant impact of user characteristics, we do not report detailed results in the interest of brevity. As Fig. 6 shows, this lack of statistically signi<sup>fi</sup>cant results is indeed caused by very similar results for all treatment groups, rather than by excessive variance within groups. Most subjects in all treatment groups provided quite reasonable estimates of attribute means with a relative error of less than 50%.

Problem complexity had a strong effect on performance in the ex-post test, where subjects had to rank <sup>fi</sup>ve (ef<sup>fi</sup>cient) class schedules according to their preferences three weeks after completion of the experimental session. In the simple problems, the alternative which was ranked best in the original experiment received a median rank of one among the <sup>fi</sup>ve alternatives presented in the ex-post test from users of tables and PCP. This indicates that more than half of these subjects (64% for tables and 62% for PCP) were consistent in their choice. The median rank for heatmap users was two; nevertheless, about 45% of heatmap users also ranked it <sup>fi</sup>rst. However, in the complex problem, most users deviated considerably from their original ranking. The median rank was only three for users of tables and PCP with only 20% of table users and 24% of PCP having remained consistent. For heatmap users, this rate drops to about 4% and the median rank is four.

![](/api/attachments/CEMAET9S/fulltext/images/64f860f5839fb7743ca83eb89c4dd9719957e3711d689a8dc7736ecac951855f.jpg)  
Fig. 5. Boxplot of total time for different treatment groups.  
Table 2 Regression results.

This strong in<sup>fl</sup>uence of problem complexity is also visible in the regression results shown in the last two columns of Table 2. Problem complexity has a signi<sup>fi</sup>cant effect in the ex-post test on the rank of the best alternative as well as on the total difference of rankings. Neither heatmaps nor PCP led to a signi<sup>fi</sup>cant impact when contrasted with tables. For this analysis, we treated the rank as a metric variable. However, a logistic regression in which reaching the correct (<sup>fi</sup>rst) rank was used as dependent variable, led to identical results.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="5">Process measures</td><td colspan="5">Subjective measures</td><td colspan="2">Ex-post test</td></tr><tr><td>Steps</td><td>Time</td><td>Reversals</td><td>Average 1</td><td>Average 3</td><td>Perceived usefulness</td><td>Perceived ease of use</td><td>Decisional conflict</td><td>Perceived effort</td><td>Perceived accuracy</td><td>Rank best alternative</td><td>Difference of ranks</td></tr><tr><td rowspan="2">(Intercept)</td><td>β</td><td>11.20</td><td>* 345.67</td><td>3.29</td><td>*** 0.56</td><td>0.14</td><td>0.97</td><td>8.45</td><td>*** 10.39</td><td>*** 8.05</td><td>** 9.39</td><td>0.99</td><td>0.47</td></tr><tr><td>t</td><td>0.67</td><td>2.52</td><td>0.84</td><td>4.36</td><td>1.30</td><td>0.22</td><td>1.34</td><td>3.83</td><td>4.23</td><td>3.29</td><td>1.14</td><td>0.24</td></tr><tr><td rowspan="2">Heatmap</td><td>β</td><td>1.48</td><td>65.35</td><td>2.40</td><td>0.01</td><td>0.05</td><td>0.01</td><td>*-6.24</td><td>1.48</td><td>-0.28</td><td>-1.00</td><td>0.40</td><td>1.13</td></tr><tr><td>t</td><td>0.20</td><td>1.09</td><td>1.40</td><td>0.25</td><td>1.18</td><td>0.01</td><td>-2.27</td><td>1.24</td><td>-0.34</td><td>-0.80</td><td>1.13</td><td>1.36</td></tr><tr><td rowspan="2">PCP</td><td>β</td><td>*** 37.03</td><td>-66.06</td><td>*** 9.48</td><td>*** -0.23</td><td>** -0.13</td><td>2.60</td><td>0.49</td><td>*-2.52</td><td>*-2.09</td><td>-0.39</td><td>0.26</td><td>-0.20</td></tr><tr><td>t</td><td>5.01</td><td>-1.09</td><td>5.46</td><td>-4.04</td><td>-2.89</td><td>1.31</td><td>0.17</td><td>-2.10</td><td>-2.48</td><td>-0.31</td><td>0.72</td><td>-0.24</td></tr><tr><td rowspan="2">Complex</td><td>β</td><td>-6.18</td><td>28.78</td><td>-0.89</td><td>0.04</td><td>-0.03</td><td>2.54</td><td>1.80</td><td>-1.42</td><td>-1.34</td><td>0.33</td><td>*** 1.74</td><td>*** 4.68</td></tr><tr><td>t</td><td>-0.85</td><td>0.48</td><td>-0.52</td><td>0.75</td><td>-0.58</td><td>1.29</td><td>0.66</td><td>-1.20</td><td>-1.61</td><td>0.27</td><td>4.75</td><td>5.53</td></tr><tr><td rowspan="2">Female</td><td>β</td><td>1.43</td><td>° 58.77</td><td>0.89</td><td>-0.02</td><td>0.01</td><td>-0.48</td><td>-2.60</td><td>0.18</td><td>-0.35</td><td>-1.17</td><td>-0.34</td><td>-0.43</td></tr><tr><td>t</td><td>0.34</td><td>1.70</td><td>0.90</td><td>-0.82</td><td>0.34</td><td>-0.42</td><td>-1.63</td><td>0.27</td><td>-0.72</td><td>-1.63</td><td>-1.57</td><td>-0.88</td></tr><tr><td rowspan="2">Rational DS</td><td>β</td><td>0.07</td><td>4.34</td><td>0.01</td><td>0.00</td><td>0.00</td><td>*** 0.54</td><td>*** 0.69</td><td>*-0.16</td><td>-0.04</td><td>0.09</td><td>0.00</td><td>° 0.09</td></tr><tr><td>t</td><td>0.16</td><td>1.29</td><td>0.10</td><td>0.08</td><td>0.90</td><td>4.92</td><td>4.46</td><td>-2.39</td><td>-0.93</td><td>1.32</td><td>0.00</td><td>1.83</td></tr><tr><td rowspan="2">Intuitive DS</td><td>β</td><td>0.42</td><td>° 6.46</td><td>0.08</td><td>-0.00</td><td>0.00</td><td>0.12</td><td>0.25</td><td>-0.07</td><td>0.01</td><td>-0.02</td><td>0.01</td><td>0.06</td></tr><tr><td>t</td><td>0.99</td><td>1.87</td><td>0.81</td><td>-1.09</td><td>0.68</td><td>1.03</td><td>1.56</td><td>-0.95</td><td>0.27</td><td>-0.27</td><td>0.60</td><td>1.11</td></tr><tr><td rowspan="2">Dependent DS</td><td>β</td><td>-0.41</td><td>°-5.12</td><td>°-0.14</td><td>0.00</td><td>-0.00</td><td>° 0.16</td><td>0.07</td><td>** 0.17</td><td>0.01</td><td>0.06</td><td>0.02</td><td>0.01</td></tr><tr><td>t</td><td>-1.17</td><td>-1.79</td><td>-1.77</td><td>1.59</td><td>-0.99</td><td>1.69</td><td>0.55</td><td>2.94</td><td>0.42</td><td>1.00</td><td>0.87</td><td>0.31</td></tr><tr><td rowspan="2">Avoiding DS</td><td>β</td><td>0.43</td><td>4.03</td><td>0.06</td><td>-0.00</td><td>-0.00</td><td>0.01</td><td>-0.14</td><td>0.02</td><td>* 0.08</td><td>-0.05</td><td>*-0.04</td><td>0.03</td></tr><tr><td>t</td><td>1.31</td><td>1.48</td><td>0.82</td><td>-1.39</td><td>-0.97</td><td>0.06</td><td>-1.12</td><td>0.44</td><td>2.11</td><td>-0.91</td><td>-2.12</td><td>0.79</td></tr><tr><td rowspan="2">Spontaneous DS</td><td>β</td><td>-0.47</td><td>-4.92</td><td>-0.10</td><td>0.00</td><td>0.00</td><td>0.06</td><td>0.13</td><td>0.07</td><td>-0.05</td><td>0.08</td><td>0.04</td><td>-0.01</td></tr><tr><td>t</td><td>-1.01</td><td>-1.30</td><td>-0.93</td><td>0.83</td><td>0.29</td><td>0.49</td><td>0.73</td><td>0.87</td><td>-0.90</td><td>1.06</td><td>1.50</td><td>-0.23</td></tr><tr><td rowspan="2">Heatmap×Complex</td><td>β</td><td>10.18</td><td>94.81</td><td>0.57</td><td>*-0.18</td><td>-0.03</td><td>-2.87</td><td>1.04</td><td>-0.81</td><td>0.94</td><td>0.34</td><td>0.06</td><td>-0.86</td></tr><tr><td>t</td><td>0.99</td><td>1.13</td><td>0.24</td><td>-2.33</td><td>-0.48</td><td>-1.04</td><td>0.27</td><td>-0.48</td><td>0.80</td><td>0.19</td><td>0.11</td><td>-0.73</td></tr><tr><td>PCP ×</td><td>β</td><td>* 21.72</td><td>87.64</td><td>-0.26</td><td>-0.06</td><td>-0.01</td><td>°-4.94</td><td>-3.24</td><td>* 4.28</td><td>° 2.32</td><td>-1.02</td><td>-0.27</td><td>-0.00</td></tr><tr><td>Complex</td><td>t</td><td>2.04</td><td>1.00</td><td>-0.10</td><td>-0.70</td><td>-0.19</td><td>-1.72</td><td>-0.81</td><td>2.48</td><td>1.92</td><td>-0.56</td><td>-0.50</td><td>-0.00</td></tr><tr><td> $R^2$ </td><td></td><td>0.46</td><td>0.17</td><td>0.35</td><td>0.30</td><td>0.24</td><td>0.26</td><td>0.30</td><td>0.23</td><td>0.12</td><td>0.07</td><td>0.40</td><td>0.43</td></tr><tr><td>Adj. $R^2$ </td><td></td><td>0.42</td><td>0.10</td><td>0.29</td><td>0.24</td><td>0.18</td><td>0.20</td><td>0.24</td><td>0.16</td><td>0.04</td><td>-0.01</td><td>0.34</td><td>0.38</td></tr></table>

Signi<sup>fi</sup>cance levels: ∘: pb10%, \*: pb5%, \*\*: pb1%, \*\*\*: pb0.1%.

Relative error in estimating averages  
![](/api/attachments/CEMAET9S/fulltext/images/9e4db2bdc51598addc49ffef064d3fa80e9256e96136d25e96c0f80e08cb74cd.jpg)  
Fig. 6. Boxplot of errors in estimating attribute averages.

## 7. Discussion

The main goal of our paper was to study the impact of different problem representations on the solution process of multi-criteria decision problems. In line with prior research [39,52], we <sup>fi</sup>nd no method to be universally superior. Outcomes depend on characteristics of the user and the problem.

Table 3 summarizes our results according to the factors we studied. Different problem representations mainly have short term effects. They lead to different decision processes and subjective evaluations, but the ex-post test showed that differences disappear over time. This <sup>fi</sup>nding is in line with prior empirical research [58,66] <sup>fi</sup>nding no long-term impact of representation formats on symbolic recall tasks.

Heatmaps are perhaps the least familiar problem representation which we tested. This is re<sup>fl</sup>ected in subjective evaluations, in which heatmaps performed signi<sup>fi</sup>cantly weaker in terms of perceived ease of use. Heatmap users spent signi<sup>fi</sup>cantly more time than users of PCP on the decision task, nevertheless, they performed worse in the ex-post test, although this effect was statistically not signi<sup>fi</sup>cant. Both effects can be attributed to a lack of familiarity with heatmaps.

PCP perhaps were more familiar to our subjects than heatmaps. Consequently, the subjective evaluation is quite similar to that of tables, which are probably the most familiar representation. The strongest impact of PCP is in terms of the decision process. The use of PCP led to what can be called a more explorative behavior of subjects: On the one hand, they performed considerably more <sup>fi</sup>ltering steps and also reversed their settings more often. On the other hand, the process converged more quickly to only few admissible alternatives. Taken together, these two effects indicate a process which jumps between narrowly de<sup>fi</sup>ned regions. In contrast, the other two methods lead to a broader approach. However, in terms of problem understanding and long term recall, both processes seem to be about equally effective.

While tables are more similar to PCP in terms of subjective criteria, the search process they induce is more similar to heatmaps. This is not surprising, since the structure of heatmaps is very similar to that of tables, and interaction also basically works in the same way. The assumed impact of familiarity is also supported by the fact that even though DMs using PCP performed most steps, they expressed the lowest perceived effort. This may be due to the exploratory approach they used.

The effects of problem representations are moderated by problem complexity. Several regression analyses shown in Table 2 exhibit significant interaction terms between the two factors. In less complex problems, decisional con<sup>fl</sup>ict is perceived to be highest by heatmap users and lowest by users of PCP, while in high complexity problems, it is highest for users of PCP. A similar, although not signi<sup>fi</sup>cant effect can be observed for perceived usefulness, for which the relative position of PCP drops from <sup>fi</sup>rst to second. These results con<sup>fi</sup>rm our expectation that an increase in complexity has a major impact on the decision making process.

Apart from this moderating effect, complexity has a strong direct effect on long term performance. For more complex problems, both measures indicate signi<sup>fi</sup>cantly lower correspondence between the original solution and the ex-post test. A similar, although statistically insigni<sup>fi</sup>cant, effect can also be observed for understanding in Fig. 6.

User characteristics form the third group of factors. Since our subject population is quite homogeneous, the only demographic variable we considered was gender. In line with recent research showing that there are no gender differences regarding perception and decision about technology adoption within younger subjects [44], we did not <sup>fi</sup>nd signi<sup>fi</sup>cant impact.

In contrast, decision making styles have a strong impact on subjective evaluation. The kind of decision support we studied here seems to be particularly useful for subjects having a rational style. Additional regression analyses which we performed did not indicate any signi<sup>fi</sup>- cant interactions between problem representation and decision style. We also noted a weakly signi<sup>fi</sup>cant effect of decision making style on the performance in the ex-post test: Subjects having a high score in the avoiding style performed signi<sup>fi</sup>cantly worse, perhaps indicating that they did not identify as strongly with the solutions obtained during the experiments as other subjects.

## 8. Conclusions and future research

We have studied the impact of problem representations, problem complexity, and user characteristics on a wide range of outcome dimensions including subjective and objective measures, and short as well as long term effects. This breadth of dependent variables allowed us to provide a more differentiated view on the impact of our factors than was possible in previous research.

Table 3 Strength of effects.

<table><tr><td></td><td>Duration</td><td>Process structure</td><td>Subjective evaluation</td><td>Understanding</td><td>Re-evaluation</td></tr><tr><td>Problem representation</td><td>RQ1</td><td>RQ1Strong</td><td>RQ2Weak</td><td>RQ5</td><td>RQ6</td></tr><tr><td>Complexity</td><td>RQ3</td><td>RQ3</td><td>RQ3</td><td>RQ5</td><td>RQ6Strong</td></tr><tr><td>User characteristics</td><td>RQ4</td><td>RQ4</td><td>RQ4Strong</td><td>RQ5</td><td>RQ6Weak</td></tr><tr><td>Complexity × Representation</td><td>RQ3Weak</td><td>RQ3</td><td>RQ3Weak</td><td>RQ5</td><td>RQ6</td></tr></table>

Two main conclusions can be drawn from the results summarized in Table 3. First, although different problem representations induce differences in the decision making process, these differences do not seem to have long term effects on either problem understanding or performance in an ex-post test. Second, there is a considerable difference between objective characteristics of the decision process and its subjective evaluation by participants. A comprehensive picture can thus only be obtained by considering both objective and subjective measures.

For the designers of DSS for multi-criteria decision problems, this means that user satisfaction requires the system to be adaptable to users' particular decision making styles, although the objective impact of the system is driven by other factors. While our research thus has immediate implications, it should be noted that it also has some limitations, which need to be addressed in future studies.

Our experiments were performed using one task and a quite homogeneous population of student subjects. While the use of student subjects limits the generalizability of our results, business students represent future managers, who will probably use similar DSS in the future. Moreover, we have taken into account several factors regarding the external validity of our results [35]. To avoid self-selection, subjects were also actively recruited from classrooms and assigned randomly to one of the treatments. Furthermore, anonymity of subjects was fully preserved to prevent approval effects. In addition, subjects were provided with proper motivation (MP3 music players) to take the experimental tasks seriously.

The task we used for our experiments was a portfolio selection problem. While the underlying portfolio structure was not directly visible in the problem representations, the choice of this particular task still might have had some in<sup>fl</sup>uence on the choice process. From a more general perspective, we can characterize the decision problem in terms of the number of criteria, the number of alternatives, as well as the particular structure of attribute values. Although our simple and complex treatments differed in the number of attributes and alternatives, we still were comparing only problems with three and seven attributes, and several hundred alternatives. The representations we studied here probably are not adequate for problems of far larger size. To our knowledge, there are no studies indicating that patterns of attribute values, in particular correlations among attributes, are systematically different between portfolio problems and other multi-criteria decision problems. Still, the problem we used in our experiment involved a certain pattern of correlations between attributes, which could have in<sup>fl</sup>uenced outcome dimensions like decisional con<sup>fl</sup>ict. Generalizing our results to other tasks and other user groups thus requires additional experiments.

Another important factor, which we did not consider in our experiment, is time pressure. Although we imposed a time limit of just 15 min, many subjects completed their task before the deadline. Time pressure, therefore, seems to have played no role in our experiments. While the time of 15 min seems to be short for solving a complex problem, it should be kept in mind that our experiment covered only the last stage in a multi-stage decision process. Before ef<sup>fi</sup>cient alternatives can be compared in an interactive process, they must be generated using an adequate model. However, prior research has shown that time pressure in this interactive phase is indeed an important factor for assessing different representation formats [6] as well as decision making strategies [2,48], and therefore could also make a difference compared to the setting studied here.

Combining the wide range of outcome measures applied in this study with a wider range of experimental factors like different levels of time pressure, different decision problems, or different subject populations could create a research program that eventually leads to improved problem representations and better decisions in discrete multi-criteria problems.

## References

[1] J.A. Aloysius, F.D. Davis, D.D. Wilson, A.R. Taylor, J.E. Kottemann, User acceptance of multi-criteria decision support systems: the impact of preference elicitation techniques, European Journal of Operational Research 169 (2006) 273–285.

[2] M. Aminilari, R. Pakath, Searching for information in a time-pressured setting: experiences with a text-based and an image-based decision support system, Decision Support Systems 41 (2005) 37–68.

[3] P. Barmby, T. Harries, S. Higgins, J. Suggate, How can we assess mathematical understanding?, in: J. Woo, H. Lew, K. Park, D. Seo (Eds.), Proceedings of the 31st Conference of the International Group for the Psychology of Mathematical Education, volume 2, Seoul, pp. 41–48.

[4] V. Beattie, M.J. Jones, Measurement distortion of graphs in corporate reports: an experimental study, Accounting, Auditing and Accountability Journal 15 (2002) 546–564.

[5] I. Benbasat, A.S. Dexter, An experimental evaluation of graphical and color-enhanced information presentation, Management Science 31 (1985) 1348–1364.

[6] I. Benbasat, A. Dexter, An investigation of the effectiveness of color and graphical information presentation under varying time constraints, MIS Quarterly 10 (1986) 59–83.

[7] J.L. Bierstaker, R.G. Brody, Presentation format, relevant task experience and task performance, Managerial Auditing Journal 16 (2001) 124–128.

[8] A.F. Borthick, P.L. Bowen, D.R. Jones, M.H.K. Tse, The effects of information request ambiguity and construct incongruence on query development, Decision Support Systems 32 (2001) 3–25

[9] J.T. Buchanan, An experimental evaluation of interactive MCDM methods and the decision making process, Journal of the Operational Research Society 45 (1994) 1050–1059.

[10] J. Buchanan, L. Gardiner, A comparison of two reference point methods in multiple objective mathematical programming, European Journal of Operational Research 149 (2003) 17–34.

[11] D.J. Campbell, Task complexity: a review and analysis, The Academy of Management Review 13 (1988) 40–52.

[12] P.C. Chu, E.E. Spires, The joint effects of effort and quality on decision strategy choice with computerized decision aids, Decision Sciences 31 (2000) 259–292.

[13] P. Chu, E.E. Spires, Perceptions of accuracy and effort of decision strategies, Organizational Behavior and Human Decision Processes 91 (2003) 203–214.

[14] R. Coll, J. Coll, G. Thakur, Graphs and tables: a four-factor experiment, Communi cations of the ACM 37 (1994) 77–86.

[15] D. Cook, H. Hofman, E.-K. Lee, H. Yang, B. Nikolau, E. Wurtele, Exploring gene expression data, using plots, Journal of Data Science 5 (2007) 151–182.

[16] F. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (1989) 319–340.

[17] G. Dickson, G. DeSanctis, D.J. McBride, Understanding the effectiveness of computer graphics for decision support: a cumulative experimental approach Com munications of the ACM 29 (1986) 40–47.

[18] J.M. Duf<sup>fi</sup>n, A.P. Simpson, A search for understanding, The Journal of Mathematical Behavior 18 (2000) 415–427.

[19] J.S. Dyer, P.C. Fishburn, R.E. Steuer, J. Wallenius, S. Zionts, Multiple criteria decision making, multiattribute utility theory: the next ten years, Management Science 38 (1992) 645-654

[20] M. Ehrgott, I. Winz, Interactive decision support in radiation therapy treatmen planning, OR Spectrum 30 (2008) 311–329.

[21] A. Focke, C. Stummer, Strategic technology planning in hospital management, OR Spectrum 25 (2003) 161–182.

[22] P.E. Green, K. Helsen, B. Shandler, Conjoint internal validity under alternative profile presentations, Journal of Consumer Research 15 (1988) 392–397

[23] J. Hakanen, K. Miettinen, K. Sahlstedt, Wastewater treatment: new insight provided by interactive multiobjective optimization, Decision Support Systems 51 (2011) 328–337.

[24] J.C. Hershey, P.J.H. Schoemaker, Probability versus certainty equivalence methods in utility measurement: are they equivalent? Management Science 31 (1985) 1213–1231.

[25] J. Huysmans, K. Dejaeger, C. Mues, J. Vanthienen, B. Baesens, An empirical evaluation of the comprehensibility of decision table, tree and rule based predictive models, Decision Support Systems 51 (2011) 141–154.

[26] A. Inselberg, Parallel Coordinates: Visual Multidimensional Geometry and Its Applications, Springer, Dordrecht, 2009.

[27] A. Kamis, E. Stohr, Parametric search engines: what makes them effective when shopping online for differential products? Information Management 43 (2006) 904–918.

[28] E. Kiesling, J. Gettinger, C. Stummer, R. Vetschera, An experimental comparison of two interactive visualization methods for multi-criteria portfolio selection, in: A. Salo, J. Keisler, A. Morton (Eds.), Advances in Portfolio Decision Analysis: Improved Methods for Resource Allocation, Springer, New York, 2011, pp. 187–209.

[29] P. Korhonen, A visual reference direction approach to solving discrete multiple criteria problems, European Journal of Operational Research 34 (1988) 152-159

[30] P. Korhonen, J. Wallenius, Visualization in the multiple objective decision-making framework, in: J. Branke, K. Deb, K. Miettinen, R. Slowinski (Eds.), Multiobjective Optimization (LNCS 5252), Springer, Berlin, 2008, pp. 195–212.

[31] P. Korhonen, O. Larichev, A. Mechitov, H. Moshkovich, J. Wallenius, Choice behavjour in a computer-aided multiattribute decision task Journal of Multi-Criteria Decision Analysis 6 (1997) 233–246.

[32] J. Kottemann, F. Davis, Decisional con<sup>fl</sup>ict and user acceptance of multicriteria decision-making aids, Decision Sciences 22 (1991) 918–926.

[33] J. Larkin, H. Simon, Why a diagram is (sometimes) worth ten thousand words, Cognitive Science 11 (1987) 65–100.

[34] Z. Lee, C. Wagner, H.K. Shin, The effect of decision support system expertise on system use behavior and performance, Information Management 45 (2008) 349–358.

[35] S.D. Levitt, J.A. List, What do laboratory experiments measuring social preferences reveal about the real world? Journal of Economic Perspectives 21 (2007) 153–274.

[36] Y. Liu, Y. Lee, A.N. Chen, Evaluating the effects of task-individual-technology <sup>fi</sup>t in multi-DSS models context: a two-phase view, Decision Support Systems 51 (2011) 688–700.

[37] R. Loo, A psychometric evaluation of the general decision-making style inventory, Personality and Individual Differences 29 (2000) 895–905.

[38] A. Lotov, K. Miettinen, Visualizing the Pareto frontier, in: J. Branke, K. Deb, K. Miettinen, R. Slowinski (Eds.), Multiobjective Optimization (LNCS 5252), Springer, Berlin, 2008, pp. 213–243.

[39] H.C. Lucas, An experimental investigation of the use of computer-based graphics in decision making, Management Science 27 (1981) 757–768.

[40] E. Lusk, M. Kersnick, The effect of cognitive style and report performance on task performance: the MIS design consequences, Management Science 25 (1979) 787–798.

[41] B. Mennecke, M. Crossland, B. Killingsworth, Is a map more than a picture? The role of SDSS technology, subject characteristics, and problem complexity on map reading and problem solving, MIS Ouarterly 24 (2000) 601-629.

[42] J. Meyer, A new look at an old study on information display: Washburne (1927) reconsidered, Human Factors 39 (1997) 333–340.

[43] J. Meyer, D. Shinar, D. Leiser, Multiple factors that determine performance with tables and graphs, Human Factors 39 (1997) 268–286.

[44] M.G. Morris, V. Venkatesh, P.L. Ackerman, Gender and age differences in employee decisions about new technology: an extension of the theory of planned behavior, IEEE Transactions on Engineering Management 52 (2005) 69–84.

[45] T. Neubauer, C. Stummer, Interactive selection of Web services under multiple objectives, Information Technology and Management 11 (2010) 25–41.

[46] R.S. Nickerson, Understanding understanding, American Journal of Education 93 (1985) 201–239.

[47] A. Pyrke, S. Mostaghim, A. Nazemi, Heatmap visualisation of population based multi objective algorithms, in: S. Obayashi, K. Deb, C. Poloni, T. Hiroyasu, T. Murata (Eds.), Evolutionary Multi-Criterion Optimization (LNCS 4403), Springer, Berlin, 2007, pp. 361–375.

[48] J. Rieskamp, U. Hoffrage, Inferences under time pressure: how opportunity cost affect strategy selection, Acta Psychologica 127 (2008) 258–276.

[49] S. Scott, R. Bruce, Decision-making style: the development and assessment of a new measure, Educational and Psychological Measurement 55 (1995) 818–831.

[50] P. Shah, J. Hoeffner, Review of graph comprehension research: implications for instruction, Educational Psychology Review 14 (2002) 47–69.

[51] R. Sharda, S.H. Barr, J. McDonnell, Decision support effectiveness: a review and an empirical test, Management Science 34 (1988) 139–159.

[52] C. Speier, The in<sup>fl</sup>uence of information presentation formats on complex task decision-making performance, International Journal of Human Computer Studie 64 (2006).1115-1131

[53] D. Spicer, E. Sadler-Smith, An examination of the general decision making style questionnaire in two UK samples, Journal of Managerial Psychology 20 (2005) 137-149.

[54] C. Stummer, E. Kiesling, W.J. Gutjahr, A multicriteria decision support system for competence-driven project portfolio selection, International Journal of Informa tion Technology and Decision Making 8 (2009) 379–401.

[55] M. Swink, C. Speier, Presenting geographic information: effects of data aggregation, dispersion, and users' spatial orientation, Decision Sciences 30 (1999) 169–195.

[56] P. Thunholm, Decision-making style: habit, style or both? Personality and Individual Differences 36 (2004) 931–944.

[57] A. Tversky, Elimination by aspects: a theory of choice, Psychological Review 79 (1972) 281–299.

[58] N.S. Umanath, R.W. Scamell, An experimental evaluation of the impact of data display format on recall performance, Communications of the ACM 31 (1988) 562–570.

[59] N. Umanath, I. Vessey, Multiattribute data presentation and human judgement: a cognitive <sup>fi</sup>t perspective, Decision Sciences 25 (1994) 795–824.

[60] I. Vekiri, What is the value of graphical displays in learning? Educational Psychology Review 14 (2002) 261–312.

[61] V. Venkatesh, F. Davis, A theoretical extension of the technology acceptance model: four longitudinal <sup>fi</sup>eld studies, Management Science 46 (2000) 186–204.

[62] I. Vessey, Cognitive <sup>fi</sup>t: a theory-based analysis of the graphs versus tables literature, Decision Sciences 22 (1991) 219–240.

[63] J. Wallenius, Comparative evaluation of some interactive approaches to multicriterion optimization, Management Science 21 (1975) 1387–1396.

[64] J. Wallenius, J.S. Dyer, P.C. Fishburn, R.E. Steuer, S. Zionts, K. Deb, Multiple criteria decision making, multiattribute utility theory: recent accomplishments and what lies ahead, Management Science 54 (2008) 1336–1349

[65] J.N. Washburne, An experimental study of various graphic, tabular and textual methods of presenting quantitative material, Journal of Educational Psychology 18 (1927) 361–376.

[66] C.J. Watson, R.W. Driver, The in<sup>fl</sup>uence of computer graphics on the recall of information, MIS Quarterly 7 (1983) 45–53.

[67] J.N. Weinstein, A postgenomic visual icon, Science 319 (2008) 1772–1773.

[68] R. Wood, Task complexity: de<sup>fi</sup>nition of the construct, Organizational Behavior and Human Decision Processes 37 (1986) 60–82.

[69] S. Zionts, A multiple criteria method for choosing among discrete alternatives, European Journal of Operational Research 7 (1981) 143–147.

Johannes Gettinger is a post‐doctoral research assistant and lecturer at the University of Hohenheim, Germany. He holds a master's degree in International Business Administration at the University of Vienna and the University of Bologna and a PhD in economics and social sciences from the Vienna University of Technology. His research focus is on con<sup>fl</sup>ict resolution, in particular electronically supported decision-making and negotiation, decision as well as negotiation support systems, and the role of information in decision‐making and negotiation.

Elmar Kiesling is a research assistant in the Information & Software Engineering Group at the Vienna University of Technology, Austria. Furthermore, he is a senior researcher at Secure Business Austria, an industrial research center for IT security. His research interests include decision support systems, risk and information security management, agent‐based modeling and simulation, visualization of multivariate data, and gaming simulations for blended learning. Elmar teaches courses in innovation management, business engineering, and business intelligence. He is a graduate of the school of Business, Economics, and Statistics at the University of Vienna, Austria, where he served as a project assistant and lecturer and obtained a Master's degree in business administration and a PhD degree in management.

Christian Stummer holds the Chair of Innovation and Technology Management at the Department of Business Administration and Economics at Bielefeld University, Germany. He has served as an associate professor at the University of Vienna, Austria, as the head of a research group at the Electronic Commerce Competence Center (EC3) at Vienna, and as a visiting professor at the University of Texas at Šan Antonio, United States. His research focuses on (quantitative) modeling and providing proper decision support particularly so with respect to new product diffusion and project portfolio selection. Prof. Stummer has published two books, more than thirty papers in reviewed journals, and numerous other works.

Rudolf Vetschera is a professor of organization and planning at the school of Business, Economics and Statistics, University of Vienna, Austria. He holds a PhD in economics and social sciences from the University of Vienna, Austria. Before his current position, he was full professor of Business Administration at the University of Konstanz, Germany. He has published three books and more than eighty papers in reviewed journals and collective volumes. His main research area is in the intersection of organization, decision theory, and information systems, in particular negotiations, decisions under incomplete information, and the impact of information technology on decision making and organizations.
