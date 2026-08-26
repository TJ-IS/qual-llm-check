---
otero_id: 24602
otero_key: "SPACRYUH"
title: "Investigating the Impacts of Managerial Turnover/Succession on Software Project Performance"
authors: "Tarek K. Abdel-Hamid"
year: "1992"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1992.11517961"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Investigating the Impacts of Managerial Turnover/Succession on Software Project Performance

Tarek K. Abdel-Hamid

To cite this article: Tarek K. Abdel-Hamid (1992) Investigating the Impacts of Managerial Turnover/Succession on Software Project Performance, Journal of Management Information Systems, 9:2, 127-144, DOI: 10.1080/07421222.1992.11517961

To link to this article: https://doi.org/10.1080/07421222.1992.11517961

![](/api/attachments/SPACRYUH/fulltext/images/be8bfbe8c7cbf27b1812ba61e561681dcc2d55b1d5154112ea5356ed6ef63608.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/SPACRYUH/fulltext/images/3f1bedb5de970dd8f3cd87f37455d028b3da819650947158d2a293329a3ec296.jpg)

Submit your article to this journal ↗

![](/api/attachments/SPACRYUH/fulltext/images/549f4774e920fd0124eb9f282d5a82b937766093ceab1e2a0a4a352b11902235.jpg)

Article views: 2

![](/api/attachments/SPACRYUH/fulltext/images/bdac1f89ccc08e42a28ecd7569c2acef21a600637e216bba16d335d1333ce239.jpg)

View related articles ↗

![](/api/attachments/SPACRYUH/fulltext/images/469069a86a4604320a561a063554d315925aff2324b543216909c0840d263786.jpg)

Citing articles: 15 View citing articles ↗

# Investigating the Impacts of Managerial Turnover/Succession on Software Project Performance

TAREK K. ABDEL-HAMID

TAREK K. ABDEL-HAMID is Associate Professor of Information Systems in the Department of Administrative Sciences at the Naval Postgraduate School. Prior to joining NPS, he spent two and a half years at the Stanford Research Institute consulting internationally on information systems issues. Since 1986 he has been an advisor to NASA's Jet Propulsion Lab on the development of computer-based tools for software project management. He received a B.S. degree in aeronautical engineering from Cairo University, Egypt, in 1972, and a Ph.D. in management information systems from M.I.T. in 1984. His research interests focus on software project management, system dynamics, and management information systems. He is the coauthor of Software Project Dynamics: An Integrated Approach and has authored or coauthored more than twenty papers in journals such as Communications of the ACM, Journal of Management Information Systems, MIS Quarterly, IEEE Software, and IEEE Transactions on Software Engineering. Dr. Abdel-Hamid is a member of the ACM, SIM, IEEE-CS, and the System Dynamics Society.

ABSTRACT: The persistent turnover problem in the software field combined with the tendency of managerial succession to promote instability make this phenomenon of crucial importance to the student as well as the practitioner of software project management. The focus of most studies to date has been on the use of aggregated statistical data to answer macro questions regarding aggregates of organizations. On the other hand, there is a serious lack of micro-empirical analysis of turnover/succession and its impacts on managerial performance. This paper reports the results of a simulation-based laboratory study to investigate the impacts of managerial turnover/succession on software project performance. Specifically, the study examines the staffing and cost/schedule trade-off choices of successor project managers, and compares them with the choices made by managers who run their projects from start to finish without interruption. The results indicate that managerial turnover/succession can lead to a discernible (albeit unintended) shift in cost/schedule trade-off choices, affecting staff allocations and ultimately project performance in terms of both cost and duration.

KEY WORDS AND PHRASES: managerial succession, managerial turnover, software project management, software project staffing.

## 1. Introduction

THE SUCCESSFUL DEVELOPMENT AND DELIVERY OF SOFTWARE systems is becoming an increasingly critical function in many organizations as computer-based technology continues to play an ever larger role in determining how organizations operate, how they create their products, and indeed in reshaping the products themselves [4, 26]. The evidence suggests that effective project management is a requisite for the successful delivery of software systems on budget and on schedule [7]. Conversely, ineffective project management is often the primary culprit in project failures ([13, p. 3] and [37, p. 16]). For example, Boehm [7] asserts that ineffective management can increase project cost “more rapidly than any other factor.” The critical role played by the project manager is highlighted in the Department of Defense report on the multimillion-dollar software engineering technology initiative called STARS (Software Technology for Adaptable, Reliable Systems):

The manager plays a major role in software and systems development and support. The difference between success or failure—between a project being on schedule and on budget or late and over budget—is often a function of the manager's effectiveness. [16]

If so, then it behooves us to better understand the possible impacts of project management turnover/succession on software project performance. “The universality of succession (e.g., due to turnover) in formal organizations and the tendency of the process to promote instability combine to make this phenomenon of crucial importance to organizational theory” [20]. The issue is more than academic in the software field, where high turnover continues to be a persistent and troublesome problem [13]. “The current annual turnover rate is 35 percent, and this turnover in computer people has been stable at this figure for the past few years” [38]. Citing the magnitude of the turnover problem and the potential disruptions of succession, a number of information systems researchers have called for “concentrated research in this area” [5].

The focus of most studies to date (both inside and outside the information systems field) has been on the use of aggregated statistical data to answer macro questions regarding aggregates of organizations. For example, researchers have investigated turnover rates $[38, 43]$ , causes of turnover $[13, 25]$ , organizational size and managerial succession $[18]$ , executive compensation and managerial turnover $[11]$ , and so on.

On the other hand, there has been a serious lack of micro-empirical analysis of turnover/succession and its impacts on managerial decision-making behavior. This deficiency can be attributed, in part, to the difficulty of conducting controlled experimentation of dynamic decision making tasks $[8]$ .

A dynamic decision-making task differs from the static decision-making tasks that have traditionally been the focus of study in the psychology literature in at least three ways [8]: (1) it requires a series of decisions rather than a single decision; (2) the decisions are interdependent; and (3) the environment changes, both autonomously and as a consequence of the subjects' decisions. These three aspects characterize many of the important decision tasks undertaken by software project managers. Because actual events on a software project almost always differ from the assumed events that project plans were designed to meet, software project managers must continuously adjust their staffing levels, estimates, resources, and the like to an evolving project and organizational environment. Quoting Putnam [1, p. 83], "with software development, the problem is always changing. Therefore, the solution is always changing." According to Brehmer, a primary reason for the relative neglect of dynamic decision making tasks by researchers is that,

[T]he study of real-time, dynamic decision-making requires new forms of research technology. One cannot study dynamic tasks using the ordinary paper-and-pencil approach of psychological research. Instead, interactive computer simulations of dynamic tasks are required. The technology for this has only recently become available in psychological laboratories.

Most later experiments on dynamic decision making have used computer simulations of dynamic tasks. [8]

This paper reports the results of such a simulation-based laboratory study to investigate the impacts of managerial turnover/succession on software project performance. Specifically, the study examines the staffing and cost/schedule trade-off choices of successor managers, and compares them with the choices made by managers who run their projects without interruption from start to finish. In addition, the study sought to assess the impacts of the differences (if any) on project performance in terms of ultimate project cost and duration.

## 2. Formulating the Research Question

THREE PREMISES UNDERLIE THE FORMULATION of the study's research question:

Premise No. 1. A software system's ultimate development cost and duration are not "preordained" outcomes, but, rather, are highly dependent on management's cost/schedule trade-off choices.

For example, a project manager can, if he or she so chooses, compress a project's schedule, at the price of an increase in project cost. Schedule compressions, however, need to be planned for early in the life cycle. For example, to compress a schedule using the COCOMO software estimation tool $[6]$ , it is assumed that “the project manager knows about any required schedule acceleration or stretchout in advance, and is able to plan and control the project in the most cost-effective way with respect to an off-nominal schedule.” Planning for schedule compression may include increasing the staff size (early in the life cycle), acquiring software-based automation aids, buying added computer hardware resources to support faster coding, checkout, and testing, and the like $[6]$ .

Conversely, a “good” manager can turn an overestimated schedule into a self-fulfilling prophecy if he or she chooses to. This, for example, may be achieved through lowering staff levels and/or allowing more slack. “The degrees of freedom which allow the project manager to do this are the common slack components of the software person’s typical work week” [6].

Premise No. 2: Staffing decisions are integral to management's cost/schedule trade-off choices.

Of the myriad functions undertaken by project managers, staffing actions are among the most consequential [7]. For example, in a study that spanned a number of projects across many organizations, Jeffery [22] found that “staff loading consistently explains over 70% of the productivity variation experienced.”

Staffing decisions are not carried out in isolation; they affect and are affected by scheduling and costing considerations. For example, by dividing the value of effort remaining (in person-days) at any point in the project, by the time remaining, managers can determine the average work force level needed to complete the project on time $[1]$ .

In addition to scheduling, staffing decisions can also be driven by cost and work force stability considerations. For example, before adding new staff, consideration may be given to the training and communication overheads associated with staff acquisitions, and their impact on project cost.

Furthermore, these cost/schedule trade-offs are not static; rather they change dynamically throughout the life cycle. For example, toward the end of a project, managers often become increasingly reluctant to acquire new people, even if the project is behind schedule. This happens when the time left is judged insufficient for acquainting new people with the mechanics of the project, assimilating them into the project team, and training them in the necessary technical areas $[2]$ .

## Premise No. 3: The psychological impacts of past (sunk) staff allocation decisions bias future decisions.

The consequences of any single staffing decision can have implications about the utility of previous choices as well as determining future events or outcomes. This is due, in part, to the fact that sunk costs may not be sunk psychologically, but may enter into future decisions. The psychological impact of past (sunk) resource allocation decisions and how they may bias or systematically affect future decisions has been studied extensively in the organization behavior literature. The most complete and persuasive analysis is found in the work of Barry Staw on “escalating commitment” [34].

Staw and his associates conducted a series of experiments in which subjects were required to make multiple resource allocation decisions to some entity (e.g., a project). And they compared the behaviors of subjects who were responsible for making the entire series of decisions with those who took over in midstream.

In one series of experiments, Staw used a business case in which students played the role of a corporate financial officer who is asked to allocate research and development funds to one of two operating divisions of a company. Subjects were then given feedback on their initial decision and asked to make further allocations of R&D funds. Staw found that more resources were allocated after failure than after success. He also found that more resources were allocated when the subject was personally responsible for the decision, by virtue of having made the initial decision, than when the earlier decision had been made by someone else $[31]$ .

## Staw theorized that:

[I]individuals are motivated by a competence drive, in that they seek to predict and control their immediate environments, and to attain their goals. However, to the extent that an individual has a strong need to be correct or accurate, he/she is also likely to

feel compelled to justify his/her actions, in order to prove to himself/herself and to others that he/she is indeed competent and rational. [42]

The series of staff allocation decisions made throughout the life of a software project are not unlike the fund allocation decisions studied by Staw. As mentioned earlier, staff allocations are often driven by the desire to complete the project on schedule. As the ability to estimate software development accurately continues to elude us $[17, 40]$ , it is all too common for software managers to experience schedule delays on their projects. So, not unlike Staw's corporate financial officers who had to contemplate allocating additional R&D resources after financial failure, software project managers (or their successors) often must contemplate whether or not to allocate additional resources to slipping software projects. Staw's results suggest that there could be significant differences between successor and start-to-finish managers in how they allocate project resources.

## Hypotheses

H1: Project staffing profiles of successor managers will be different from those pursued by start-to-finish managers.

Following the results of Staw [34], it is hypothesized that successor managers would be less committed to problematic project goals they “inherit” (e.g., a schedule slippage), and that, as a result, they would pursue different staffing profiles (e.g., refrain from excessive hiring of new staff).

Because staff loading directly impacts software development productivity, and hence project cost and duration, it is further hypothesized that:

H2: Turnover/succession impacts project performance in terms of ultimate project cost and duration.

## 3. The Experimental Setting

THE RESEARCH ISSUES WERE EXPLORED IN THE context of a role-playing project simulation game. Thirty-six graduate students at a U.S. business school participated as part of a software engineering management course requirement. The subjects were fifth- and sixth-quarter masters students studying in the computer systems management curriculum.

The computer simulation game is similar in many ways to the flight simulators that pilots use to mimic flying an aircraft. Instead of flying an aircraft, though, this simulator mimics the life of a software project from the start of the design phase until the end of testing. (A description of the model's structure is provided in the appendix.)

The subjects played the role of the project manager. Their task was to track the project's progress using model-generated monthly status reports (figure 1) on resources used, work accomplished, and the like, and to manage their staffing resources "wisely and efficiently while aiming to complete the project on time." Although devising a more precise goal was certainly possible, it was felt that this formulation is a more “realistic” characterization of software managers’ goals.

<table><tr><td colspan="3">Reported Project Statistics at Time 100</td></tr><tr><td colspan="3">CURRENT INTERVAL STATISTICS: Elapsed time = 100</td></tr><tr><td colspan="3">INITIAL ESTIMATES: (These will not change throughout the project)</td></tr><tr><td>Project size</td><td>42,880</td><td>DSI</td></tr><tr><td>Person-day cost</td><td>2,359.00</td><td>Person-days</td></tr><tr><td>Project duration</td><td>297</td><td>Days</td></tr><tr><td colspan="3">REPORTED STATISTICS</td></tr><tr><td>at Time →</td><td>100</td><td>Days</td></tr><tr><td>% project reported complete</td><td>22.19</td><td>Percent</td></tr><tr><td>Updated size of project</td><td>47,086</td><td>DSI</td></tr><tr><td>Updated estimate of total person-days</td><td>2,515.33</td><td>person-days</td></tr><tr><td>Total number – full-time equiv. staff</td><td>5.7</td><td>Full-time staff</td></tr><tr><td colspan="3">Effort expenditures to date:</td></tr><tr><td>Development activities</td><td>606.15</td><td>Person-days</td></tr><tr><td>Design and coding</td><td>401.06</td><td>Person-days</td></tr><tr><td>Rework (i.e.,fixing errors)</td><td>114.18</td><td>Person-days</td></tr><tr><td>Quality assurance</td><td>90.92</td><td>Person-days</td></tr><tr><td>Testing</td><td>0.00</td><td>Person-days</td></tr><tr><td>Total person-days expended</td><td>606.15</td><td>Person-days</td></tr><tr><td>New estimate of project duration (start → end)</td><td>339</td><td>Days</td></tr><tr><td>Max. tolerable project duration</td><td>400</td><td>Days</td></tr><tr><td colspan="3">Write your new desired staffing level on the documentation sheet provided and press</td></tr></table>

Figure 1. Monthly Status Report

The initial estimates for the project's size, cost, and schedule were 42,800 delivered source instructions (DSI), 2,359 person-days, and 296 working days (15 calendar months) respectively. (The person-day and schedule estimates were derived from the basic COCOMO model, which is “one of the most widely accepted and applied models for software effort and cost estimation” [39, p. 708].) As is the case for many real projects, the simulated project was initially undersized, and as a consequence underestimated. New requirements were added to the project throughout the project's simulated life cycle, causing the project's size to expand to 64,000 DSI.

The subjects were advised to give whatever weight they saw fit to the status report information. As mentioned above, the subjects were in their final stages of a masters program in computer systems management. As such, they appreciated the real-life complexities of the control task. For example, they understood that the reported “percent complete” may not be totally reliable in the early phases of the project (as is typically the case on real projects) [12].

Each subject's monthly staffing decision was entered into the model through a menu screen, as well as hand-written on a special documentation sheet. The simulation was played over approximately a one-hour session, with each subject working alone. Ten percent of each student's grade in the course was based on performance on this exercise.

## 4. Experimental Design

THE THIRTY-SIX SUBJECTS WERE RANDOMLY DIVIDED INTO two experimental groups of eighteen. Each subject in the first group, designated “START,” ran his or her individual project from start to finish. Subjects in the second group, designated “SUCCESSOR,” took over their respective projects at the start of the sixth month. They were told that the project’s original manager left to join another organization (i.e., the loss was due to turnover).

In order to establish a common reference point for comparison, it was necessary to ensure that at precisely the end of the fifth month (i.e., the time when the “SUCCESSOR” subjects took over their projects), the status of all projects in both groups was identical (in terms of resources used to date, work accomplished to date, etc.). To accomplish this, the model’s gaming interface was designed to disregard the “START” subjects’ inputs for the first five months. That is, the simulated project’s staff allocation function was not driven by the subjects’ inputs (as the subjects believed it did). Instead, the model relied on an internal staff allocation structure that was modeled after the staffing pattern observed in a real organization. This, of course, had to be accomplished transparently so as to sustain the “illusion” that the “START” subjects were in control of their projects’ staffing functions.

It was possible to maintain such an illusion because the subjects understood that managers in real life (and hence in the game) do not necessarily get all the staff they desire, or do not get them immediately. Factors beyond a manager's control such as hiring delays, turnover, or work force ceiling limitations are some of the reasons why.

The “START” subjects’ inputs for the first five months were handled as follows: If a subject entered a desired staffing level that was higher than the model’s self-generated value, the model would report to the subject (in the end-of-month status report) the lower model value, and the difference would be attributed to the above set of uncontrollable factors. If, on the other hand, the subject entered a staffing level that was below the model’s, the subject’s value would be reported (since factors such as hiring delay or turnover are unlikely to increase the staffing level beyond that desired).

As for the “SUCCESSOR” subjects, their projects were first run by lab teams through the first five months (with the same internal staff allocation structure engaged). Thus, at the end of the fifth month all subjects (unknowingly) received identical status reports, the one depicted in figure 1. Notice that at this point the project is already experiencing a schedule slippage, from the initial 296 days to 339 days.

From this point on, the model's internal staffing mechanism was transparently and automatically decoupled for all subjects, allowing the subjects' staffing inputs to drive their respective projects. This, incidently, did not mean that staff size would be necessarily equal to the value input by the subject. Remember, the subjects' inputs were desired staff levels. And, as mentioned earlier, the model faithfully mimics reality, in that project managers rarely get all the staff they desire, or get them immediately.

Postexperimental interviews of the “START” subjects were conducted to assess whether or not the switch from the model’s internal staffing mechanism to the users’ inputs at the end of the fifth month was indeed transparent to the subjects. The interview results indicated that none of the “START” subjects were at any time in doubt that they were in fact “calling the shots” during the initial five months, and through project completion.

## 5. Experimental Results and Statistical Analysis

FOR EACH SUBJECT, DATA WERE COLLECTED on his or her monthly desired staff level inputs and the project's ultimate cost and duration. Cases in which subjects made significant errors were discarded, $^{1}$ and data from thirty-four subjects (eighteen "START" and sixteen "SUCCESSOR") were retained for analysis. Table 1 presents group summary statistics for the final project cost and duration outcomes of both groups.

Figure 2 depicts the means of the two groups' monthly staff level inputs throughout the life cycle. The "START" group's initial five inputs (the ones ignored by the model) are not shown. The plot for each group terminates at the group's mean project duration.

A repeated measures analysis of the data (from day 100 to day 400) yielded the results of Table 2. Since the cell sizes were unequal, we used the General Linear Models procedure on the SAS statistical package.

The between-subjects component of the test, which assesses the effects of turnover/succession, produced a p value of 0.0012. This rejects the null hypothesis of no between-subject staffing differences. That is, the results suggest that there were significant differences between the staffing levels of the two experimental groups. Specifically, the “START” group opted for a significantly higher staffing level throughout the life cycle (figure 2). Hypothesis 1 is, therefore, supported.

That established, the next step was to investigate whether the shapes of the staffing profiles were also different (i.e., did the two groups use different staffing strategies?). As shown in Table 2, the component of the test measuring the effect of time on the subjects' staffing decisions yielded a $p$ value of 0.0013. This suggests a significant time effect, that is, that the subjects' staffing levels (of figure 2) are significantly nonhorizontal, changing dynamically over the life cycle. But, were there differences between the two groups? The last component of the test is for the time\*group effect. The test's high $p$ value of 0.3056 suggests that the interaction is not significant. This indicates that the shapes of the two groups' staffing profiles were not significantly different, that is, that the lines of figure 2 are essentially parallel.

Table 1 Summary Statistics

<table><tr><td rowspan="2">Group</td><td rowspan="2">N</td><td colspan="2">Cost (person-days)</td><td colspan="2">Duration (days)</td></tr><tr><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td></tr><tr><td>START</td><td>18</td><td>5,162</td><td>495.8</td><td>414</td><td>35.8</td></tr><tr><td>SUCCESSOR</td><td>16</td><td>4,618</td><td>481.9</td><td>462.5</td><td>21.9</td></tr></table>

![](/api/attachments/SPACRYUH/fulltext/images/a6cc2a5807be3cb7954a30754609062418d304c042c9cfb6ed333a2b39df6d40.jpg)  
Figure 2. The Two Groups' Staffing Decisions over Time

Thus, put together, the results indicate that while the staffing decisions of both groups did exhibit similar patterns over time (i.e., were parallel), they were not identical (between-subjects result). Specifically, the “START” group opted for a significantly higher staffing level throughout the life cycle (figure 2).

Finally, the impact of the different staffing levels on project cost and duration was investigated (hypothesis 2). The nonparametric Wilcoxon Rank Sum test was used to statistically compare the final cost and duration values for the two groups. (Because of the small sample sizes and the large range of final cost and duration values, normality of the groups' results was doubted. This was confirmed through a formal normality test which yielded a p value of 0.01.) The results of the Wilcoxon Rank Sum test are shown in Table 3.

With a p value of 0.0007, the null hypothesis of equal project costs was rejected. This allows us to conclude that the “START” group’s project costs were significantly higher than those of the “SUCCESSOR” group.

The second test compared the final project durations, and resulted in a p value of 0.0001. The low p value rejects the null hypothesis that the average project durations were equal. We therefore conclude that the “SUCCESSOR” group’s staff allocations did lead to a significantly larger schedule overrun. Hypothesis 2 is therefore supported.

Table 2 Repeated Measures Analysis

<table><tr><td></td><td>F value</td><td>p</td></tr><tr><td colspan="3">Between-subjects</td></tr><tr><td>Succession</td><td> $F(1,29)^a = 12.9$ </td><td>0.0012</td></tr><tr><td colspan="3">Within-subjects</td></tr><tr><td>Time</td><td> $F(15,15)^b = 5.27$ </td><td>0.0013</td></tr><tr><td>Time * succession</td><td> $F(15,15)^b = 1.31$ </td><td>0.3056</td></tr></table>

$^{a}$ Test and residual degrees of freedom.  
$^{b}$ Numerator and denominator degrees of freedom.

Table 3 Wilcoxon Rank Sum Test

<table><tr><td rowspan="2">Group</td><td rowspan="2">Mean cost</td><td rowspan="2">N</td><td colspan="2">Wilcoxon scores</td></tr><tr><td>Sum</td><td>Mean</td></tr><tr><td>START</td><td>5,162</td><td>18</td><td>414</td><td>23.00</td></tr><tr><td>SUCCESSOR</td><td>4,618</td><td>16</td><td>181</td><td>11.31</td></tr><tr><td colspan="2">Wilcoxon 2-sample test</td><td rowspan="2" colspan="2">S = 181Prob. &gt; Z = 0.0007CHISQ = 11.67Prob &gt; CHISQ = 0.0006</td><td rowspan="2">Z = -3.3988DF = 1</td></tr><tr><td colspan="2">Kruskal-Wallis test</td></tr><tr><td rowspan="2">Group</td><td rowspan="2">Mean duration</td><td rowspan="2">N</td><td colspan="2">Wilcoxon scores</td></tr><tr><td>Sum</td><td>Mean</td></tr><tr><td>START</td><td>414</td><td>18</td><td>203</td><td>11.28</td></tr><tr><td>SUCCESSOR</td><td>462.5</td><td>16</td><td>392</td><td>24.50</td></tr><tr><td colspan="2">Wilcoxon 2-sample test</td><td rowspan="2" colspan="2">S = 392Prob. &gt; Z = 0.0001CHISQ = 15.00Prob &gt; CHISQ = 0.0001</td><td rowspan="2">Z = 3.8557DF = 1</td></tr><tr><td colspan="2">Kruskal-Wallis test</td></tr></table>

While the subjects of both groups had identical task objectives (i.e., to deliver the project on time), it is obvious (figure 2) that the “START” subjects were more willing to commit more staff in an attempt to turn around the early (at month five) schedule slippage. Recall that the project’s initial schedule was underestimated because the project was undersized. The price paid by the “START” group’s sustained commitment to an underestimated (and potentially infeasible) schedule is a significant cost overrun (figure 3).

The “SUCCESSOR” subjects, on the other hand, exhibited a greater concern for minimizing their cost overruns. Postexperimental interviews shed further light on the group’s behavior. The “SUCCESSOR” subjects’ responses indicated that they were very much influenced by the status of the project at the time of succession. Recall that at the end of the fifth month (see figure 1), the project was already experiencing schedule and cost overruns. The schedule overrun was, however, more serious (14 percent versus 6.6 percent). Turning the schedule problem around, thus, appeared to be less feasible. Upon concluding that, the successor subjects elected to focus on minimizing their cost overrun (which they perceived to be much more doable), secured in the knowledge that any schedule slippage could ultimately be blamed on their predecessors. This explained why the “SUCCESSOR” subjects refrained from excessive hiring of new staff. Figure 3 depicts the differences in the cost/schedule trade-off choices between the two groups.

The above results are in line with Staw's earlier findings, namely, that individuals tend to increase their commitment to decision alternatives for which they have had some prior involvement (due to the need to exhibit consistency of actions over time) [33]. In this case, more staffing resources were allocated after failure (the schedule slippage) by the “START” subjects, who felt personally responsible for the initial staff allocations. The above experimental results can now be summarized as follows:

1. Managerial succession led to shifts in managerial commitment away from the more problematic project goal(s).

2. Cost/schedule commitment shifts induced corresponding shifts in staff allocation levels.

3. Project cost and duration were significantly influenced by differences in project staffing levels.

## 6. Limiting Factors to Generalizability

ALTHOUGH ALL THE STUDENT SUBJECTS HAD SOFTWARE engineering management training, and a majority of them had managerial experience, we must still question whether they were reasonable surrogates for software managers? Most experiments that focus on decision making have used students as subjects. For example, in the experiments on the escalation of commitment, Staw [34] used a simulated business case in which students played the role of a corporate financial officer who is asked to allocate research and development funds to one of two operating divisions of a company. Brehmer [8] used undergraduate students on a computer-simulation game of fighting forest fires. And Sterman [36] used experienced economists as well as students in his simulations, and found dysfunctionalities across the board.

The reason why student subjects are used as surrogates for managers is no mystery:

This is largely so because of the availability of student subjects and the difficulty in obtaining managers as subjects. The subjects selected are usually from business schools, giving their use some apparent validity because they will be the managers of tomorrow. [30]

In a study to investigate the use of graduate students as surrogates for managers, Remus [30] found no significant differences between students and managers in making production scheduling decisions. Although software project management decisions are somewhat different from production scheduling decisions, they are similar enough to apply his findings and assume that software engineering graduate students are acceptable surrogates in this experimental investigation.

A second potentially limiting factor concerns the nature of the experimental task. It is not claimed that the above results generalize to all types of project situations. In this experiment the project simulated was medium in size (i.e., between 16,000 and 64,000 DSI), and was developed in a familiar in-house environment, that is, in a project environment in which “Most people connected with the project have extensive experience in working with related systems within the organization, and have a thorough understanding of how the system under development will contribute to the organization’s objectives” [6, p. 78].

![](/api/attachments/SPACRYUH/fulltext/images/6d87ff2619b2645b2bd23be32e0473e18632a8a8a5171db6026cd40160b588bf.jpg)

![](/api/attachments/SPACRYUH/fulltext/images/7704971136ac7e98cc10152a63c8c89c451617f5b8f995812ac096f7e537a475.jpg)  
Figure 3. Cost and Duration Frequencies for the Two Groups

Third, the parameters of the game limited the subjects' decision task to a single dimension, namely, staffing. As mentioned earlier, staffing was selected because there is an abundance of evidence indicating its significant influence on performance [22]. The evidence on the impacts of other factors, such as the use of automated tools, is either still lacking, or is not as convincing. In reality, of course, managers must make many additional decisions besides staffing. While the experiment's design allows for better control of the decision context, by the same token, it underrepresents the full impact of the turnover/succession dynamic on software project performance. (For example, Gouldner [19] observed an increase in tension and a deterioration of morale and productivity.)

Finally, one cannot claim external validity for any laboratory-type study. That said, it is encouraging to report that reviews of the gaming literature indicate considerable similarity between decision making in games and managerial decision making per se $[3, 27, 29]$ . Encouraged by these findings, the use of simulation-based laboratory experiments has steadily increased in recent years as they continue to shed significant light on human behavior in a variety of decision-theoretic contexts $[36]$ .

## 7. Conclusion

THE CONTRIBUTIONS OF THIS EXPERIMENTAL STUDY are twofold. First, the study reveals the significant impact that managerial turnover/succession can have on cost/schedule trade-off choices, staff allocation strategies, and ultimately project cost and duration. What makes the results particularly interesting is the fact that these impacts are unintended side-effects of the managerial succession process.

That managers can directly influence project outcomes through actions such as staffing or technology investments is clear. What this study suggests, which may not be as clear, is that succession can also have indirect (often unintended) consequences. Specifically, our results show that succession can alter the cost/schedule trade-off choices on a project and, in turn, project staffing. The study also shows that such (unintended) effects significantly influence project performance in terms of ultimate project cost and duration.

This result, together with a persistently high turnover rate in the software field, makes it crucially important that top management understand the impacts, both direct and indirect, of succession in order to plan it, or at least plan for it. This is especially critical for organizations undertaking strategic software projects, which often must meet strict schedule objectives. For example, top management must guard such projects against any premature “de-escalation of commitment” by successor managers. One possible safeguard is to ensure that successor managers are appointed from among those team members who were originally involved in the formulation of the project's goal(s) (if capable ones could be found). Such individuals will tend to exhibit a higher and more sustainable level of commitment due to their need to exhibit consistency of actions over time.

Second, and at a more general level, this research effort underscores both the importance and the feasibility of studying dynamic decision-making behavior in the software project domain. It is hoped that, by demonstrating the utility as well as the viability of conducting simulation-based laboratory experimentation on software management dynamics, this research effort will motivate further study in this critical and ripe research area, leading to increased innovation in the management of software development.

## NOTES

1. Two “successor” subjects misunderstood the concept of productivity using person-days/task instead of tasks/person-day. This constituted a significant conceptual error since productivity plays a central role in assessing project resources. For this reason, the two subjects were excluded from the analysis.

## REFERENCES

1. Abdel-Hamid, T.K. The dynamics of software project staffing: a system dynamics based simulation approach. IEEE Transactions on Software Engineering, 15, 2 (February 1989), 109–119.

2. Abdel-Hamid, T.K., and Madnick, S.E. Software Project Dynamics: An Integrated Approach. Englewood Cliffs, NJ: Prentice-Hall, 1991.

3. Babb, E.M.; Leslie, M.A.; and Van Syke, M.D. The potential of business gaming methods in research. Journal of Business, 39 (1966), 465–472.

4. Bales, C.F. The myths and realities of competitive advantage. Datamation, October 1, 1988.

5. Bartol, K.M., and Martin, D.C. Managing information system personnel: a review of the literature and managerial implications. MIS Quarterly, 6, 4 (December 1982), 49–70.

6. Boehm, B.W. Software Engineering Economics. Englewood Cliffs, NJ: Prentice-Hall, 1981.

7. Boehm, B.W. Improving software productivity. Computer, 20, 9 (September 1987), 43–57.

8. Brehmer, B. Strategies in real-time, dynamic decision making. In H. Einhorn and R. Hogarth (eds.), Insights in Decision Making. Chicago: University of Chicago Press, 1990.

9. Brooks, F.P. No silver bullet: essence and accidents of software engineering. Computer, 20, 4 (April 1987), 10–19.

10. Cleland, D.I., and King, W.R. Systems Analysis and Project Management. New York: McGraw-Hill, 1975.

11. Coughlan, A.T., and Schmidt, R.M. Executive compensation, management turnover, and firm performance: an empirical investigation. Journal of Accounting and Economics, 7 (1985), 43–66.

12. DeMarco, T. Controlling Software Projects. New York: Yourdon Press, 1982.

13. DeMarco, T., and Lister, T. Peopleware: Productive Projects and Teams. New York: Dorset House, 1987.

14. Denning, P.J. Technology or management. Communications of the ACM, 34, 3 (March 1991), 11–12.

15. Dickson, G.W., and Wetherbe, J.C. The Management of Information Systems. New York:

McGraw-Hill, 1985.

16. Department of Defense. Strategy for DoD software initiative. Department of Defence, October 1, 1982. (An edited public version was published in Computer, 16, 11 [November 1983].)

17. Genuchten, M., and Koolen, H. On the use of software cost models. Information & Management, 21 (1991), 37–44.

18. Gordon, G., and Becker, S. Organizational size and managerial succession: a reexamination. American Journal of Sociology, 70 (1964), 215–233.

19. Gouldner, A.W. Patterns of Industrial Bureaucracy. New York: Free Press, 1954.

20. Grusky, O. Administrative succession in formal organizations. Social Forces, 39 (1960), 105–115.

21. Hogarth, R.M. Beyond discrete biases: functional and dysfunctional aspects of judgemental heuristics. Psychological Bulletin, 90 (1981), 197–217.

22. Jeffery, D.R. The relationship between team size, experience, and attitudes and software development productivity. COMPSAC, Tokyo, October 1987, 2–8.

23. Kitchenham, B., and Taylor, N. Software project development cost estimation. Journal of Systems and Software, 5 (1985), 267–278.

24. Kotter, J.P. Organizational Dynamics: Diagnosis and Intervention. Reading, MA: Addison-Wesley, 1978.

25. Mobley, W.H.; Griffeth, R.W.; Hand, H.H.; and Meglino, B.M. Review and conceptual analysis of the employee turnover process. Psychological Bulletin, 86, 3 (May 1979), 493–522.

26. Porter, M.E., and Millar, V. How information gives you competitive advantage. Harvard Business Review (July–August 1985), 149–160.

27. Prohaska, C.R., and Frank, E.J Using simulations to investigate management decision making. Simulation & Gaming, 21, 1 (March 1990), 48–58.

28. Putnam, L. Software Cost Estimating and Life-Cycle Control: Getting the Software Numbers. Los Alamitos, CA: IEEE Computer Society Press, 1980.

29. Remus, W.E. Testing Bowman's managerial coefficient theory using a competitive gaming environment. Management Science, 24, 8 (April 1978), 827–835.

30. Remus, W.E. Graduate students as surrogates for managers in experiments on business decision making. Journal of Business Research, 14 (1986), 19–25.

31. Schwenk, C.R. Information, cognitive biases, and commitment to a course of action. Academy of Management Review, 11, 2 (1986), 298–310.

32. Shaw, M.E. Group Dynamics, 3d ed. New York: McGraw-Hill, 1981.

33. Staw, B.M. Knee-deep in the big muddy: a study of escalating commitment to a course of action. Organizational Behavior and Human Performance, 16 (1976), 27–44.

34. Staw, B.M. The escalation of commitment to a course of action. Academy of Management Review, 6, 4 (1981), 577–587.

35. Steers, R.M., and Porter, L.W. Motivation and Work Behavior, 4th ed. New York: McGraw-Hill, 1987.

36. Sterman, J.D. Misperception of feedback in dynamic decision making. Organizational Behavior and Human Decision Processes, 43 (1989), 301–335.

37. Thayer, R.H. Tutorial: Software Engineering Project Management. Washington, DC: Computer Society Press of the IEEE, 1988.

38. Thomsett, R. Effective project teams. American Programmer (July/August 1990), 25–34.

39. Van Mayrhauser, A. Software Engineering: Methods and Management. Boston: Academic Press, 1990.

40. Vicinanza, S.; Mukhopadhyay, T.; and Prietula, M. Software effort estimation: a study of expert performance. Carnegie Mellon University, Graduate School of Industrial Administration, Working Paper 89–002, 1989.

41. Weick, K.E. The Social Psychology of Organization, 2d ed. Reading, MA: Addison-Wesley, 1979.

42. Whyte, G. Escalating commitment to a course of action: a reinterpretation. Academy of Management Review, 11, 2 (1986), 311–321.

43. Willoughby, T.C. Computing personnel turnover: a review of the literature. Computer Personnel, 7, 1–2 (Autumn 1977), 11–13.

## APPENDIX: Overview of Model Structure

FIGURE A.1 SHOWS A HIGH-LEVEL VIEW of the model's four subsystems: human-resource management, software production, control, and planning, and some of the relations among them. The actual model is very detailed and contains more than 100 causal links; a full description of the model's structure and its mathematical formulation is published in [2].

## Human-Resource Management

This subsystem captures the hiring, assimilation, and transfer of people. The project's work force is segregated into employee types (newly hired and experienced, for example). This distinction is made because new team members are usually less productive than veterans.

This segregation also allows us to capture the training process to assimilate new members. The veterans usually train the newcomers, both technically and socially. This is important, because this training can significantly affect a project's progress by reducing the veteran's productivity.

In deciding how big a work force they need, project managers typically consider several factors. One, of course, is the project's scheduled completion date. Another is the work force's stability, so managers try to predict project employment time for new members before they are hired. In general, the relative weight managers give to stability versus completion date changes as the project progresses.

## Software Production

This subsystem models development; it does not include the operation and maintenance phases. The development phases included are designing, coding, and testing.

As software is developed, it is reviewed to detect any errors such as using quality assurance activities such as structured walkthroughs. Errors detected through such activities are reworked. Not all software errors are detected during development; however, some escape detection until the testing phase.

The software-production subsystem models productivity and its determinants in great detail. Productivity is defined as potential productivity minus the loss from faulty processes. Potential productivity is the level of productivity that can occur when an individual or group makes the best possible use of its resources, and is a function of the nature of the task and the group's resources [2]. Loss from faulty processes are losses in productivity from things like communication and coordination overhead and low motivation.

## Control Subsystem

As progress is made, it is reported. A comparison of the degree of project progress to the planned schedule is captured within the control subsystem.

![](/api/attachments/SPACRYUH/fulltext/images/8ed5277a2a5d5bb0edd2bddcf2ed4fa59554aa9e2777cfacf0658ba6af9b0ca4.jpg)  
Figure A.1. Model Structure

In all organizations, decisions are based on the information available to the decision maker. Often, this information is inaccurate. Apparent conditions may be far removed from those actually encountered, depending on information flow, time lag, and distortion.

Progress rate is a good example of a variable that is difficult to assess during the project. Because software is basically an intangible product during most of the development, it is difficult to measure things like programming performance and intermediate work. In the earlier phases of development, progress is typically measured by the rate of resource expenditure rather than accomplishments. But as the project advances toward its final stages, work accomplishments become relatively more visible and project members better perceive how productive the work force has actually been.

## Planning Subsystem

In the planning subsystem, project estimates are made and revised as the project progresses. For example, when a project is behind schedule, the plan may be revised to hire more people, extend the schedule, or both.

By dividing the value of person-days remaining at any point in the project by the time remaining, a manager can determine the indicated work force level, which is the work force needed to complete the project on time. However, hiring decisions are not made solely on the basis of scheduling requirements. Managers also consider the training requirements and the work force's stability. Thus, before adding new project members, management assesses the project employment time for the new members. In general, the relative weighting between the desire for work force stability and the desire to complete the project on time is not static; it changes throughout the project's life.

Although management determines the work force level needed to complete the project, this level does not necessarily translate into the actual hiring goal. The hiring goal is constrained by the ceiling on new hires. This ceiling represents the highest work force level management believes can be adequately handled by its experienced project members.

Thus, three factors—scheduled completion time, work force stability, and training requirements—affect the work force level.

## Model Validation

The model was developed on the basis of field interviews of software project managers in five organizations, complemented by an extensive database of empirical findings from the literature. The following tests were conducted to validate the model:

\- Face validity test. To test the fit between the rate/level/feedback structure of the model and the essential characteristics of real project environments. This fit was confirmed by the software project managers involved in the study.

\- Replication of reference modes. To test whether the model can endogenously reproduce the various reference behavior modes characterizing real environments. Reference modes reproduced by the model included a diverse set of behavior patterns both observed in the organizations studied as well as reported in the literature (e.g., the “90 percent syndrome,” diminishing returns of QA effort, the deadline effect, etc.).

\- Case studies. Five case studies (two by the author, and three conducted independently by three separate organizations) were conducted after the model was completely developed. All case studies were conducted in organizations other than the five organizations studied during model development.
