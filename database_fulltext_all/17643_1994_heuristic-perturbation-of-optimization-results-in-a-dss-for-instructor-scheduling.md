---
otero_id: 17643
otero_key: "UZFTM3TP"
title: "Heuristic perturbation of optimization results in a DSS for instructor scheduling"
authors: "Arup Kumar Mukherjee"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90066-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Heuristic perturbation of optimization results in a DSS for instructor scheduling

Arup Kumar Mukherjee

Fort Hays State University, Hays, KS, USA

In this paper we have described a DSS that uses a unique approach of integrating the strengths of management science and human judgement to provide support for a scheduling problem that needs inputs from both these areas of human expertise. The manager has the option of accepting a solution developed using optimization technique or intervening directly or indirectly to improve the solution. In intervening directly the manager makes specific changes to a schedule presented in natural format. In intervening indirectly the manager specifies the direction of change along with a step size. Knowledge based heuristics act automatically to revise the schedule in the direction specified. In addition mechanisms have been provided for the user to adapt existing solution to certain kinds of changes in the environment while minimizing the number of perturbations to the existing solution. The DSS has been implemented for scheduling instructors to executive development programs conducted by the University of Tennessee, Knoxville.

Keywords: Human judgement and optimization models; instructor scheduling; DSS; perturbation in schedules; Knowledge based heuristics

Arup Kumar Mukherjee earned a Bachelor of Technology degree in Electrical Engineering from the Indian Institute of Technology, Kanpur, India in April, 1977 and Doctor of Philosophy degree at the University of Tennessee, Knoxville in 1991 with a major in Management Science. His principal research interests are in application of operational research, operations management, decision support systems, simulation and integer programming. He is a member of The Operations Research Society of America, The Decision Sciences Institute, The Production and Operations Management Society and The Institution of Engineers (India). He is a Certified Associate of The Indian Institute of Bankers and Chartered Engineer (India). The author has held industry positions in industrial marketing with the General Electric Co. of India and positions in banking, sick industry rehabilitation and industrial finance with the State Bank of India. He has joined the faculty of the Computer Information Systems Department at The Fort Hays State University in August 1990 as an assistant professor. He has published in SIMULATION and SIBMAG.

Correspondence to: Arup Kumar Mukherjee, Computer Information Systems Dept., School of Business, Fort Hays State University, Hays, KS 67601, USA.

Introduction

Many decision support systems have been developed using optimization models proposed by management scientists/operations researchers. The primary focus of these systems has been on finding an optimal solution to the formulated model. The implicit assumption is that the operations research analyst knows what is best for the user $[4]$ and hence a manager should accept a decision proposed by the optimal solution $[12]$ . In practice this attitude may run into difficulties because of three reasons. First, it must be recognized that the model is only a representation of essential details in the problem $[12]$ . Many unimportant details may have been left out from the mathematical model. A decision maker needs to incorporate the effect of these details as also the implications of the lessons learnt in the past in using the model. Second, effects of social, personal, behavioral, ethical and similar non-quantitative factors also influence real decision making in any organization $[11, p.56]$ . Third, a decision support system that requires unquestioned acceptance of an optimal solution produced by a management science model does not satisfy the need of a manager to exercise direct and personal control over the solution $[2]$ .

Further, there are circumstances when a change occurs in the problem environment that affects the solution that has already been developed. The usual management science approach is to generate a new optimal solution using the revised parameters. This approach may cause difficulties for a decision maker who has already acted on the basis of the previous solution. The real need, in such situations, is to change the old solution minimally while finding a suitable solution for the revised scenario.

In this paper we describe how the above diverse needs of a decision maker were addressed in a DSS for Instructor Scheduling. In general, the DSS (a) integrates the strengths of management science models with managerial judgment, experience and knowledge of non-quantitative factors, and (b) proposes a general schema for adapting an existing solution to changes in the environment.

First, we describe the instructor scheduling problem and discuss its mathematical programming formulation. Next, we describe the mechanisms that were implemented to integrate managerial judgment and adapt solution to changed circumstances. Then we describe some of the more interesting implementation details. Excerpts are presented from two sessions that does perturbation. This is followed by a general critique of the approach used.

## The instructor scheduling problem

In this section we present the problem of scheduling of instructors to sessions of executive development programs conducted by the Institute of Productivity Through Quality, University of Tennessee, Knoxville [7]. At first we present a discussion about how the instructor scheduling problem arises followed by a mathematical programming formulation of the problem.

Universities and specialized institutes conduct executive development programs for business executives round the year. These programs consist of a series of sessions spread out over a period of one to few weeks. The sessions are usually taught by faculty drawn from various academic departments and business organizations. An interesting scheduling problem arises when instructors are to be assigned to teach sessions of these programs. We will refer to this problem as the Instructor Scheduling Problem (ISP). From a scheduling point of view, a program is a collection of sessions planned to be conducted during non-overlapping time slots. The task of the scheduler is to find instructors to staff the different sessions of these programs while trying to satisfy diverse needs as discussed below.

Instructor preferences for teaching different programs need to be respected as far as practicable. The number of instructors required to staff can differ across sessions. For a given program, two or more similar sessions may be required to be taught by the same instructor for reasons of continuity. The total number of assignments made to each instructor should respect pre-specified lower and upper limits. Instructors may not be assigned sessions that are in time conflict with their academic teaching schedules or other commitments. There are weeks when two or more programs are being conducted for distinct sets of executives. In this scenario sessions of one program may be in time conflict with some sessions of other programs. This requires that a particular instructor not be assigned to two sessions that are in time conflict. No instructor may be assigned more than three sessions on any one day. The assignment of sessions to a particular instructor should be evenly spread out over the entire planning period. A planning period is about 16 to 18 weeks long and usually coincides with an academic semester.

The problem is further complicated by its dynamic nature. The teaching schedules, instructor non-availabilities and session offerings rarely remain fixed even over the limited planning horizon of a semester. Hence it is necessary to be able to re-schedule sessions without causing large numbers of changes in sessions allocated and announced to different instructors.

We now present a mathematical programming formulation that finds best assignments of instructors while satisfying the various requirements.

## A mathematical programming formulation

We use the following notation. Let $X_{ij}=1$ if instructor i is assigned to session j, 0 otherwise; $B_{ij}$ is the “benefit” of assigning instructor i to session j; $g_{j}=$ the number of instructors needed for session j; N is the total number of instructors; T is the total number of sessions; Li/Ui are the lower limit/upper limit on the total number of sessions assigned to instructor i; Let P be the total number of days in a planning period; $D\{k\}$ be the set of sessions on day k; $S_{im}$ be the maximum number of sessions that may be assigned to instructor i in week m; W be the total number of weeks in the planning period; $Q\{v\}$ be the set of sessions in week v; $G\{j\}$ be the set of sessions in time conflict with session j; $H\{j\}$ be the set of sessions that must have the same instructor as session j; these sessions that need to be taught by the same instructor are referred to as common-code sessions;

A mathematical programming formulation of ISP is given below.

$$
\text { Maximize } \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {T} B _ {i j} ^ {*} X _ {i j}\tag{1}
$$

subject to

$$
\sum_ {i = 1} ^ {N} X _ {i j} = g _ {j}; j = 1, \ldots T;\tag{2}
$$

$$
L _ {i} \leq \sum_ {j = 1} ^ {T} X _ {i j} \leq U _ {i}; i = 1, \dots N;\tag{3}
$$

$$
\sum_ {m \in Q \{v \}} X _ {i m} \leq S _ {i m}; i = 1, \dots N; v = 1, \dots W;\tag{4}
$$

$$
\sum_ {n \in D \{k \}} X _ {i n} \leq 3; i = 1, \dots N; k = 1, \dots P;\tag{5}
$$

$$
X _ {i j} + X _ {i l} \leq 1; i = 1, \dots N; j = 1 \dots T; l \in G \{j \}\tag{6}
$$

$$
X _ {i j} - X _ {i p} = 0; i = 1, \dots N; j = 1, \dots T;
$$

$$
a l l p \in H \{j \}\tag{7}
$$

$$
X _ {i j} \in [ 0, 1 ], \text { integer }.\tag{8}
$$

The objective function (1) maximizes the “benefit” of assigning instructor i to session j. The benefit is a composite index representing the degree of match between instructor i and session j and is based on instructor preferences and scheduler’s experience about performance of the instructor. Constraint (2) ensures that each session is staffed by the right number of instructors. Constraint (3) ensures that the total assignment to any instructor remains within pre-specified lower and upper limits. Constraint (4) imposes a limit on the total number of session assignments made to an instructor in a particular week. Constraint (5) restricts the total number of assignments made to an instructor in a day to three. Constraint (6) prevents assignment of an instructor to two sessions that are in time conflict. Constraint (7) requires that pre-specified sessions be taught by the same instructor. Insights about solution strategies for this problem were gained, among others, from reported results on nurse scheduling [5], telephone operator scheduling [9], assignment of courses to faculty members [6] and assignment of students to groups for class projects [1]. LINDO [8] used over 48 minutes of C.P.U. time to find the optimal solution for the data relating to Fall 1988. The user considered this to be too long. Hence, in finding minimally perturbed adaptations of the optimal solution, knowledge based heuristics were deployed as they needed less than 1% of the time taken by LINDO.

## Heuristic perturbation of optimization results

In this section we describe the mechanisms built in to allow the scheduler to exercise direct control and/or adapt solution to the changed circumstances. We describe the system in terms of a flowchart, discuss the terminology used and the steps in direct or indirect managerial intervention.

In Figure 1 we present a visual representation of the DSS in terms of a flow chart. In using the system the user has two major options. Either the problem is to be solved for a new set of data or an existing solution needs to be adapted to changed conditions. In either case the system follows up the computer generated or adapted solution with a mechanism for direct or indirect managerial intervention.

If it is necessary to solve a new problem, the relevant data is collected and input into pre-designed data files. A mathematical program to represent the problem for the current data set is generated and solved. The non-zero assignment variables are stored. A post-processor converts the optimal solution to a schedule. When it is necessary to adapt existing solution to new scenario in order to respond to changes in the environment, the user starts by finding out the nature of the change. Data adaptors are used to update databases. Solution adaptors are used to adapt solution to new scenario. The new or adapted solution is subsequently presented to the user in natural spreadsheet format. If the solution is acceptable, desired reports are generated and the solution is printed in natural format. If the solution is not acceptable the user has the option of intervening directly or indirectly to improve the solution. The user is said to intervene directly if he acts manually to improve the solution. The intervention is indirect if he uses built in solution modifiers to direct the solution into desired avenues.

Several terms have been used in the above description of the essential processes in the DSS

and are explained below. A solution will be said to be in natural format if it is in a form that agrees with any logical representation of the solution that the user is accustomed to work with. For example, a teaching schedule showing courses that a teacher will be assigned to teach in a semester will be deemed to be in natural format if it is shown in a tabular format. Data Adaptors are in-built modules that a user may use to update a database. For a given change in any data file, these adaptors have the additional responsibility of updating all related data files that are affected by this change. In other words, the user is no longer responsible for ensuring that the effects of a change are correctly reflected in every data file.

![](/api/attachments/UZFTM3TP/fulltext/images/731a79fbb6e4ee6b45f491e885432e4e63cc3f9dbe5ae18d84ea844965f36644.jpg)  
Fig. 1. A flow chart of the DSS.

Two kinds of changes in the scheduling scenario demand a revised solution. The change may be in faculty data or in the problem structure. Changes in faculty data include changes in faculty availability, preferences, teaching schedule and limits on total assignments. Changes in problem structure include addition of a program offering, dropping of a program offering, addition of a session/dropping of a session, change in session time, content and common code. Solution adaptors are in-built modules that find good revised solutions in the changed scenario. The revised solution is good if it is feasible and changes the existing solution minimally. Note that it is possible to devise optimal ways to find the revised solution. However, because of the need to find a revised solution quickly and since the revised solution will also be subject to further managerial intervention, we have opted to use knowledge based heuristics to develop the revised solution.

When the user intervenes indirectly to improve a solution he acts through solution modifiers. These modifiers contain mechanisms for the user to suggest a direction of change, the step size, portions of the solution that must not be changed in the modification process and constraints that may be relaxed, if any, and the degree of such relaxation. In addition there is a mechanism that coordinates all of the above to move the solution to a desired revised position. At this point it is necessary to point out the difference between adaptors and modifiers. Solution adaptors are invoked and act automatically in a pre-defined manner to find a revised solution in the new scenario. In contrast, the user specifies the sequence for use of solution modifiers.

In the direct intervention process, the manager (i) reviews solution in natural format, (ii) reviews summary information, (iii) decides on specific change to the solution and (iv) uses a menu-driven approach to record the specific decision. The computer system is responsible for updating records on the basis of the solution decided upon by the manager. A related approach where the manager develops and adapts the solution in natural format has been developed by IBM for the San Jose police department for development of police beats [3].

## Implementation highlights

In this section we discuss some of the more interesting implementation details. We describe how the system prevents scheduling conflicts, recommends feasible perturbations and allows the concerned faculty to directly update the availability data file. We indicate that there are no limits on the number of perturbations that a manager could impose. An optimal approach that the user could use if the heuristic fails to find a feasible solution is described.

At this point it is necessary to state that a schedule is developed in advance for a semester of activities. This usually involves using 15 faculty to teach about 600 sessions. Thus the problem is very large and this fact influenced many of our implementation decisions.

## Prevention of conflicts

A scheduling problem is interesting because conflicts have to be prevented. It is possible to represent the problem of finding different faculty for time conflicting sessions as a coloring problem on a graph. Specifically, the vertices represent sessions. Further, conflicting sessions have an edge connecting them and are considered to be “adjacent”. The goal is to look for an assignment of colors to the vertices such that no adjacent pair of vertices has the same color. The distinct colors could represent distinct faculty. Since the number of faculty are limited, we want a solution using the fewest number of colors. However, this problem of finding a minimal assignment of colors to vertices is NP-complete [10]. In addition, ISP requires that certain pre-specified sets of sessions $H\{j\}$ be taught by the same faculty. These considerations make it necessary for us to investigate other ways to prevent conflicts. A discussion on strategies implemented to prevent conflicts with teaching schedules and between sessions is presented below.

## Prevention of conflicts with teaching schedules

Teaching schedules are stored in a natural format. For example, suppose that faculty KK teaches a class every Tuesday and Thursday from 9:30 AM to 10:45 AM. In the data file this is stored as “KK TR 0930 1045”. When this data is read it is converted to information about non-availability in sessions in conflict with the above teaching schedule. In the mathematical program the appropriate faculty-session assignment variable is not generated if the faculty is not available for the session. In the heuristics a non-available faculty is not considered for assignment. Thus this conflict is prevented implicitly.

## Prevention of conflicts between two sessions

In the mathematical program constraint (6) prevents assignments to two sessions that are in time conflict. To see how the heuristic prevents these conflicts, consider the following example for session 1.

$$
\begin{array}{l} H \{1 \} = \{3 \}; G \{1 \} = \{4, 5, 7, 1 1 \}; \\ G \{3 \} = \{7, 1 5, 1 7 \}; \end{array}
$$

$H\{1\}=\{3\}$ means that sessions 1 and 3 need to be taught by the same faculty. $G\{1\}=\{4,5,7,11\}$ and $G\{3\}=\{7,15,17\}$ indicates that session 1 is in time conflict with sessions 4, 5, 7 and 11 and session 3 is in time conflict with sessions 7, 15 and 17. To find a faculty suitable for teaching session 1 we need to ensure that he is suitable for teaching session 3 too.

Thus, in order to find a faculty that may be assigned to a session j, the heuristic (i) verifies availability of the candidate in session j along with availability in all common code sessions $H\{j\}$ , (ii) verifies that the candidate faculty has not been assigned to any session in $G\{j\}$ and (iii) verifies that the candidate faculty has not been assigned to any session in $G\{H\{j\}\}$ for all sessions in $H\{j\}$ . By using such a faculty in j the heuristic guarantees that a faculty will never be used in two sessions that are in conflict.

## Recommending feasible perturbations

Since there are about 600 sessions in a schedule, it was decided to display only one weeks' sessions at a time for one program. This ensures that the user sees about 25 sessions in a display. Further, the session assignments are shown along with the session particulars and assignments in neighboring sessions. This permits the user to take non-quantitative factors into consideration while evaluating the schedule.

Two possibilities arise in this context. When the manager intervenes directly to decide on the faculty that should teach a particular session, he asks for a list of faculty “usable and available” to teach this session. Upon seeing this list he makes a determination and the DSS carries out the necessary record keeping. Excerpts of such a session is presented in the next section. On the other hand, when the manager intervenes indirectly, he specifies the change and the DSS does what is necessary to implement the required change. In the initial version of the DSS we had opted to display 3 distinct feasible alternatives for each perturbation. However, it was found that around 20% of the assignments to sessions were invariably required to be decided by direct intervention. This was true for all alternatives offered to the scheduler. As a consequence it was decided to find one good feasible schedule and let the user carry out improvements to it as he saw fit.

## Updating of availability data

The availability of faculty changes constantly. However, the scheduler needs to have access to the latest availability data to ensure that assignments made are feasible. This calls for an effective way to update the availability data file. The responsibility of updating the availability data has been passed onto the concerned faculty in the following way. Whenever a change takes place in their availability, the faculty access their VAX account, run a menu-driven program, answer questions and this automatically updates the scheduler's availability data file (also in a VAX account). If a faculty forgets to update the availability file and is assigned to a session when he is not available, he is held responsible for finding a suitable replacement. This arrangement has gone a long way to ensure relatively few scheduling conflicts due to an outdated availability file.

## Flexibility to add perturbations in phase II

In the second phase of the DSS the scheduler may either intervene directly or indirectly to improve the schedule. From actual observations it was found that the user would use indirect and direct intervention in random order. Each of these processes would be used more than 20 times in one sitting. Sometimes this process of schedule refinement would be repeated after a few days.

Accordingly the DSS has been designed to respond to this need for flexibility in the number of perturbations that it can handle in the second phase by not having any limit on the number of perturbations that the scheduler may investigate.

## When heuristic fails to find a feasible solution

If the heuristic fails in finding a feasible solution under a perturbation scenario, the user has two options. In the first option, the user may change the total limits of different faculty and try to run the heuristic again. If several trials are not successful the second option may be tried. In this option, a mathematical program is generated for the revised problem. The objective function coefficients of existing assignments are taken at large positive values. In the process of maximizing the objective function, it is expected that the existing assignments will be respected as far as practicable.

## Excerpts of perturbation sessions

In this section we present brief excerpts of indirect and direct intervention sessions. The figures used have been kept small to save space.

We present excerpts from an indirect intervention session where the scheduler uses solution modifiers to direct schedule refinement. In particular we describe session reallocation from one faculty to another. The indirect perturbation menu is shown in Figure 2. In order to judge the overall effectiveness of the current solution and decide on the direction of change to be specified, the user would first ask for a summary report (Figure 3) by choosing option 1. Suppose that the user now wants to allocate 5 sessions from RS to KK. By selecting option 4 of Figure 2 the user is guided through the steps necessary to do this (Figure 4).

```txt
Indirect Schedule Refinement
Type in your choice and hit Return.
[1] To see a summary report on current solution.
[2] To adjust limits and rerun the program.
[3] To increase/decrease assignments of a faculty.
[4] To allocate sessions from a specified faculty to a specified faculty
[5] Quit.
```  
Fig. 2. Indirect perturbation menu.

<table><tr><td colspan="4">SUMMARY OF FACULTY ASSIGNMENTS</td></tr><tr><td>INITIALS</td><td>TOTAL ASSIGNED</td><td>REQUESTS LOW</td><td>HIGH</td></tr><tr><td>HA</td><td>53</td><td>50</td><td>70</td></tr><tr><td>CC</td><td>12</td><td>5</td><td>15</td></tr><tr><td>KG</td><td>30</td><td>30</td><td>40</td></tr><tr><td>LH</td><td>31</td><td>25</td><td>45</td></tr><tr><td>KK</td><td>112</td><td>100</td><td>130</td></tr><tr><td>RS</td><td>67</td><td>60</td><td>80</td></tr></table>

Fig. 3. Summary report on current solution.

```txt
Enter Initials of faculty whose total assignments needs to be reduced and hit Return.
Enter your answer now: RS
Enter Initials of faculty whose total assignments needs to be increased and hit Return.
Enter your answer now: KK
Enter total number of sessions to be reallocated from the outgoing faculty and hit Return.
Enter your answer now: 5
```  
Fig. 4. Guided reallocation from one faculty to another.

```txt
Direct Schedule Refinement
Type in your choice and hit Return.
[1] To see a summary report on current solution.
[2] To see assignments to sessions.
[3] To make changes to the assignments.
[4] To see faculty availability for specific sessions.
[5] Quit.
```  
Fig. 5. Direct perturbation menu.

<table><tr><td colspan="5">Week No. 2 Program No. 1Title: Week 1 of 3 week Institute for ProductivityDates: 0108 - 0114 Location: SMC</td></tr><tr><td>MONDAY 0109</td><td>TUESDAY 0110</td><td>WEDNESDAY 0111</td><td>THURSDAY 0112</td><td>FRIDAY 0113</td></tr><tr><td>0810-0940Intro toStat. Mgt.KK</td><td>0810-0940ProcessAnalysisJLS</td><td>0810-0940U and CChartsDS</td><td>0810-0940XBAR &amp; RChartsRAM</td><td>0810-0940Intro.toVariablesJRE</td></tr><tr><td>1000-1130Charts forfractionnonconforKK</td><td>1000-1130ProcessAnalysisJLS</td><td>1000-1130U and CChartsDS</td><td>1000-1130Moving Avg&amp; RangechartsJRE</td><td>1000-1130Variablescontd.JRE</td></tr></table>

Fig. 6. Assignments to specific sessions.

<table><tr><td colspan="6">Instructors available for this particular session.</td></tr><tr><td>Faculty Initials</td><td>Total assigned</td><td>Lower Limit</td><td>Upper Limit</td><td>Total sessions assigned This day</td><td>This week</td></tr><tr><td>CC</td><td>21</td><td>5</td><td>55</td><td>1</td><td>1</td></tr><tr><td>KG</td><td>27</td><td>25</td><td>65</td><td>1</td><td>4</td></tr><tr><td>LH</td><td>38</td><td>33</td><td>77</td><td>2</td><td>7</td></tr><tr><td>RAM</td><td>26</td><td>10</td><td>66</td><td>0</td><td>5</td></tr></table>

Fig. 7. Instructor availability report.

We describe excerpts from a direct intervention session where the scheduler decides on replacing a specific faculty assigned to teach that session. The direct perturbation menu is shown in Figure 5. The first step is to find the actual assignments to a specific session or group of sessions. The user selects option 2, answers questions to identify the session(s) of interest and is presented with the schedule in spreadsheet format (Figure 6). Suppose that the scheduler wants someone other than KK to teach the session on “Charts for fraction non-conforming” on Monday, January 9th. He needs information about faculty available for that session along with relevant statistics about their assignments. This information is included in an availability report accessed through option 4 (Figure 7). Once the user makes up his mind about who to use in that session, he selects option 3 and the program guides him through a series of questions to carry out the desired changes.

## Critique of the approach used in this DSS

We believe that the approach used in this DSS and depicted in the flow chart of Figure 1 have certain lessons for DSS design. In this section we discuss the strengths, weaknesses and circumstances of suitability of this approach.

The many strengths of this approach include: (a) the manager feels in control of the decision making process, (b) the manager can influence the solution based on his own experiences, (c) the manager can modify the solution to take into account other non-quantifiable factors, (d) the approach integrates the optimal solution with knowledge of the human expert thus utilizing the strengths of both the approaches, (e) the decision maker has access to the solution in “natural format” and can play “what if” games without having to bring in an outside analyst.

The major weakness of this approach is the large amount of effort that would be necessary to identify and program “adaptors” and “modifiers”. While there are many advantages to this approach, the extra effort needed during systems analysis, design and development makes it necessary for us to restrict using this approach to situations where the benefits outweigh the costs. We give below a set of conditions where this approach is expected to be useful. All of these conditions must be met for a problem to qualify for the approach used in this DSS.

The problem must be such that (a) it is possible to use optimization, (b) it is necessary to incorporate human judgement into the solution, (c) it is necessary for a decision maker to feel that he is in charge of decision making, (d) it is expected to exist generally in the same scenario for a reasonable period of time; what is reasonable would depend on the particular problem; while economic criterion like payback period could be used, we have refrained from using it because it is hard to quantify the benefits of a decision support system in “\$” terms; in our opinion a time period is reasonable for these purposes if it is at least five times the total time needed in systems development. It would appear that decisions that involve or affect humans directly or indirectly are suitable for this approach. For example, scheduling of people, school districting, designing a police beat, deciding on transfers and promotions, location of “obnoxious” facilities, routing of “hazardous” materials, location of “emergency” equipment and selection of careers are all decision making problems that are suitable for this approach.

## Conclusion

In this paper we have described a DSS that integrates managerial judgement with optimization techniques in a unique way to develop schedules for instructor scheduling. The instructor scheduling problem is solved as a zero-one integer program and the optimal solution is presented to the user in natural format. The user may then either use knowledge based heuristics or intervene directly to refine the schedule. At all times the scheduler exercises direct personal control over finalization of the schedule. Further, the system has been provided with a mechanism to respond to changed circumstances and produce a minimally perturbed version of the existing schedule.

## References

[1] M.B. Ardekani and M.A. Mahmood, Development and Validation of a Tool for Assigning Students to Groups for Class Projects, Decision Sciences 17, No. 1, (1986) 92–110.

[2] E.D. Carlson, An Approach for Designing Decision Support Systems, Database 10, No. 3 (1979) 3–15.

[3] E.D. Carlson and J.A. Sutton, A Case Study of Non-Programmer Interactive Problem Solving, IBM Research Report RJ1382, San Jose, California (1974).

[4] T.M. Cook, Smart Vs. Dumb Systems: A Challenge for the 1990's, Decision Line, 22, No. 3, (1991) 3–4.

[5] C. Maier-Rothe and H.B. Wolfe, Cyclical Scheduling and Allocation of Nursing Staff, Socio-Economic Planning Sciences 7, (1973) 471–487.

[6] R.H. McClure and C.E. Wells, A Mathematical Programming Model for Faculty Course Assignments, Decision Sciences 15, No. 3, (1984) 421–433.

[7] A.K. Mukherjee, Active Resource Scheduling with Equivalent Tasks, Unary Demands and Hierarchical Structure Capacity Constraints, Ph.D. Dissertation, University of Tennessee, Knoxville, 1991.

[8] L. Schrage, User's Manual for Linear, Integer and Quadratic Programming with LINDO (Scientific Press, Third Edition, Red Wood City, California, 1987).

[9] M. Segal, The Operator Scheduling Problem: A Network Flow Approach, Operations Research 22, No. 4, (1974) 808–823.

[10] H.F. Smith, Data Structures: Form and Function (Harcourt Brace Jovanovich, New York, 1987).

[11] E. Turban, Decision Support and Expert Systems (Macmillan Publishing Company, New York, 1990).

[12] H.M. Wagner, M.H. Rothkopf, C.J. Thomas and H.J. Miser, The Next Decade in Operations Research: Comments on the CONDOR report, Operations Research 37, No. 4 (1989) 664–672.
