---
otero_id: 21181
otero_key: "HKQFK56C"
title: "Improving recruit distribution decisions in the US Marine Corps"
authors: "Hemant K. Bhargava; Kevin J Snoap"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00136-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving recruit distribution decisions in the US Marine Corps

Hemant K. Bhargava <sup>a,</sup>\*, Kevin J. Snoap <sup>b</sup>

<sup>a</sup>Penn State University, University Park, PA 16802, USA

<sup>b</sup>US Navy, USA

Accepted 3 July 2002

## Abstract

The United States Marine Corps (USMC) accomplishes its mission ‘‘to put the right Marine in the right place at the right time with the right skills and quality of life’’ in various ways. One of these is a recruit distribution modeling (RDM) and information system that assigns new recruits to entry-level schools, thereby determining the entire career paths. This article proposes improvements to the existing Marine Corps decision processes and information systems for recruit distribution. The proposed system, recruit distribution decision support system (RDdss), provides intuitive navigation through a hierarchy of switchboards, and promotes data integrity by eliminating manual data entry for data already available in the system. It incorporates four objective measures for understanding the quality of proposed distributions, and allows the user to generate and compare multiple solutions based on the trade-off between these objectives. It is a fully functional working prototype system that was installed into the USMC manpower environment, and demonstrated to provide several improvements over the current technology.

<sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Decision support system; Manpower modeling; Recruit distribution

Recruit distribution in the United States Marine Corps (USMC) is the process that assigns recruits to an entry-level school leading to a military occupational specialty (MOS). These assignments are made about 48 times a year, during the last week of the Marine Corps Recruit Depot (MCRD) training, at the end of which the ‘‘recruit’’ becomes a Marine. In the years of this study, the Marine Corps made assignment decisions on about 30,000 recruits a year. These recruits stay an average of 4 years in the Marine Corps, and the organization estimates the annual cost of each Marine to be about US\$30,000.

For many decades, the USMC has done recruit distribution using a computer-based recruit distribution model (RDM), developed and owned by a USMC contractor firm. Our research efforts at improving recruit distribution were part of a broader initiative for modernizing the USMC manpower division’s decision processes and systems, some of which (including RDM) are 40 years old and consist of proprietary software owned by external contractors. In support of this initiative, we studied and analyzed the recruit distribution problem (described in Section 1), developed mathematical models for identifying good distributions (Section 2.1), and developed a DSS for improving the process and quality of distribution decisions. Making good distribution decisions requires an effective use of these models and integration of the results with the judgement of model managers. Section 2.2 describes how the DSS supports this process. Section 3 describes the architecture and functional components of the decision support system. In the conclusion, we discuss some practical and organizational challenges that arose in deploying this system for actual use.

## 1. Recruit distribution

Recruit distribution is a critical manpower function for both individual Marines and the USMC. Quantitatively, the problem is important because of its size and financial implications. Qualitatively, recruit distributions are critical because the school determines the Marine’s military occupational specialty (MOS) which, in turn, determines his or her career. Creating school assignments that match the Marine’s desire and qualifications is in the best interest of both the Marine and USMC. The USMC vision is ‘‘to put the right Marine in the right place at the right time with the right skills and quality of life’’.

The desire of the Marine is sought to be fulfilled through a contract guarantee called a program enlisted for (PEF), specified during the recruiting process. A PEF establishes which schools a recruit wishes to go to. For instance, a PEF = 19 is the ‘‘Tank and Assault

Amphibian Option’’, which is presently associated with two schools (‘‘M1A1 Tank Crewman’’ and ‘‘Assault Amphibian Crewman’’). So, a recruit who chose this program desires to go into these two schools and no other.

A second concern in recruit distribution is the suitability of a Marine to a school. Suitability is determined by matching a Marine’s qualifications and the school’s requirements, described as properties. Example properties are Age>18 and Clerical <sub>z</sub> 80 (the latter refers to test scores from the Armed Services Vocational Aptitude Battery test).

A third concern is the timing of distributions. Schools are broken down by classes, and identified by start dates. Some schools have a class starting each week, others every month, and others only every quarter. New Marines, on the other hand, come out of MCRD training every week. Therefore, recruit distributions are made every week, but each run involves classes starting over approximately the next 12 weeks (see Fig. 1). On the average, each run involves about 700 Marines and 500 classes with about 8000 seats.

This periodicity is important since distributions are made only once a week, and each seat is prepaid, guaranteeing its availability to the USMC. Any seats left unfilled in classes beginning the first week of a distribution are a wasted resource. A final concern is the problem of unassigned Marines. This may happen because of the lack of seats in the only classes for which the Marine is eligible for, or perhaps because she is not qualified for any of the schools consistent with her PEF guarantee.

![](/api/attachments/HKQFK56C/fulltext/images/131b8d2667ec7c6499bede141718af93896f7880040fedcb2f176e1e488577d4.jpg)  
Fig. 1. Assigning Marines to school classes. Every week, a group of Marines completing the MCDR training is assigned to a collection of classes beginning over the next 3 months.

Stakeholders in the USMC recruit distribution process include the USMC, training schools, each of the recruits, and the contractor firm that maintains the RDM and a few other major USMC manpower systems. The USMC spends over a million dollars in contractor costs each year on these systems. Within the USMC manpower modeling division, two groups have interest in these models: the information systems group (MI) maintains the modeling systems, and the manpower analysis group (MA) is interested in the quality of the manpower models and analysis. Finally, there is one last significant stakeholder, the American taxpayer: it is imperative that wise decisions are made with respect to assigning Marines to schools.

## 1.1. Recruit distribution environment

USMC policy makers forecast and decide how many recruits and corresponding school seats are needed over the next few years. They also determine how many PEFs to make available for a given year. The recruit and PEF authorizations for the following year are given to the USMC recruiters, and the school seats or quotas determined for the following years are inputted into the By Name Assignment (BNA) system. Recruiters use the recruit and PEF authorizations in recruiting from the general public. Once the candidate signs a contract with the USMC, his or her test scores, PEF, and other personal data are entered into the Automated Recruit Management System (ARMS).

The RDM system, which is the focus of this work, retrieves recruit and school information from the ARMS and BNA systems that reside on large mainframe databases. RDM also receives data from two other sources. The MCRD instructors provide special assignment inputs. These are personnel identified as having the talents or abilities well suited for a particular school. The other data comes from the MCT. They provide the RDM manager with reclassification information. For instance, a Marine is reclassified if he or she is injured during MCT and is unable to make the start date of their assigned school.

All this recruit and school data is inputted into the RDM, where it is stored in the Military Operational Data Store (MODS). Then the model was run. Once a satisfactory set of assignments is obtained, the RDM manager uploads the approved assignments to the ARMS and BNA systems. From this assignment information, the MCRD generates orders for the Marines graduating from the MCRD.

## 1.2. Opportunities for improving recruit distribution systems

The RDM system has a number of limitations that prompted the USMC to consider reengineering it. RDM is implemented using proprietary software and procedures, resulting in a lack of control and high costs for the USMC. The RDM user interface needed improvement in its navigation and user flow: it was neither obvious where one should start nor where one should go next. Data management in the RDM was also poor, leading to numerous data entry errors. For example, the RDM violates the basic rule of never requiring the user to enter data already in the system [5]. These errors, in turn, adversely affect the quality of model solutions.

From the perspective of our research, the most important opportunity for improvement concerned the decision models used in making the assignments. Recruit distribution is inherently a multi-objective problem (in principle, objectives include minimizing unfilled seats, improving quality of fit, and reducing waiting times). For example, a distribution that left more seats unfilled but created a better quality of fit might be better than the one with fewer unfilled seats but where assignments did not match the recruits interests. However, the decision model and algorithms employed in RDM focused on a single criterion (the number of unfilled seats) and adopt a sequential approach (see Section 2.1). This is, in good part, a legacy problem, since speed and memory consumption were critical issues in the 1950s when the algorithm originated. Over the years, recruit distribution was thought of as transaction processing task for the RDM system: the operator feeds it various inputs, turns the crank, and gets the results. The decision process did not involve measuring the quality of a solution or comparing multiple solutions on quality measures. As a result, it was not clear that in general, a better overall distribution may involve a small (or sometimes no) sacrifice in the most visible objective: unfilled seats in schools with an early start date.

## 2. Recruit distribution modeling

After a careful analysis of the process and business rules underlying recruit distribution in the Marine Corps (described in detail in Ref. [8], Chapter 2), we set out to develop a new computer-based recruit distribution decision support system (RDdss). Our improvements fall broadly in two areas: improvements in the problem-solving process, discussed below, and improvements at the information system level (system architecture, functionality, and user interface), discussed in a later section.

## 2.1. Solving the recruit distribution problem

We formulated the recruit distribution problem as an assignment model (see Appendix A) that makes assignments subject to basic constraints representing the business rules (e.g. eligibility conditions, school quotas) for recruit distribution. The assignment model has an explicit multicriteria objective function: a combination of fit and fill objectives. While the assignment model is straightforward, this approach shifts the burden towards developing credible models for estimating the input parameters (e.g. shortfall penalties) for the assignment model. We discuss these below.

## 2.1.1. Shortfall penalties vs. school priorities

The current RDM solver embeds a sequential procedure based on school priorities (typically, schools starting earlier are given a higher priority level than schools starting later). At each step, the available Marines are assigned to the one school under consideration, and the assigned Marines are removed from the available pool as the solver moves on to the next school. This priority-based approach implicitly means that filling a higher priority school is infinitely more important than filling a lower priority school. This makes the approach inconsistent with the true intent of the Marine Corps manpower policy.

In RDdss, we discriminate between schools by associating a numerical shortfall penalty with each school. Due to the perishable nature of school seats and the high fixed costs for operating a class, we require that the penalty be lower for schools with a distant start date, and that it be disproportionately high for schools starting the following week (since there is no further opportunity to fill seats in these schools). As a specific example, we developed a penalty function displayed in Fig. 2, where the penalty is an inverse function of the school’s start date, and schools in week 1 have a disproportionately high shortfall penalty.

The use of a cardinal penalty function—rather than ordinal rankings used in RDM—allows our assignment model to be solved with a global, rather than a sequential, optimization procedure. The priority-based approach of RDM may be seen as a special case of our penalty-based approach, and can be obtained by setting the penalty for a higher priority school to be vastly larger than the penalty for a lower priority school.

## 2.1.2. Optimization objectives: fit and fill

The Marine Corps’ vision concerning the quality of assignment decisions is well summarized in the desire to put the right Marine in the right place at the right time. RDM, however, was based on a decision procedure aimed at minimizing unfilled seats, with the related secondary objective of reducing the length of time that recruits wait before they begin school. There is an obvious trade-off between this objective and the desire to achieve a good fit in the distributions: the best fitting distributions will possibly have a lower performance on wait time and unfilled seats (and vice versa).

![](/api/attachments/HKQFK56C/fulltext/images/5237694d14ee17cba276c025c5b88395a754b927414373862ba239585c125995.jpg)  
Fig. 2. Penalty function for not filling the school seats. The penalty is disproportionately high for week 1 classes since unassigned seats will remain unutilized.

In RDdss, this trade-off is made explicit via a multicriteria objective function of the form

$$
\begin{array}{r l} \text { Maximize   Total   Utility } & = K _ {\mathrm{fit}} \cdot \text { Fitness   Score } \\ & - K _ {\mathrm{fill}} \cdot \text { Penalty   Score } \end{array}\tag{1}
$$

where $K _ { \mathrm { f i t } }$ and $K _ { \mathrm { f i l l } }$ are trade-off parameters. Further, as discussed below, $K _ { \mathrm { f i t } }$ and $K _ { \mathrm { f i l l } }$ become control parameters that become part of an interactive decision process, wherein decision makers can adjust these parameters to create and choose between multiple alternative distributions.

To compute fitness, we employed the existing idea of school properties (matched against a Marine’s qualifications). Recall that each school has mandatory properties that affect eligibility, and may have additional desirable properties (these are organized along a descending importance in levels one through six). It is the latter, desirable properties, which are relevant in determining the fit between a Marine and school, i.e. in discriminating between different Marines for any given school. An obvious approach, therefore, is to assign higher fitness scores to those Marines that possess more (and more important) desirable properties for that school. However, we need to ensure an equal treatment to schools, including those that are quite flexible and do not specify many desirable properties. We translate this into a requirement that the average fitness score, taken over all eligible Marines for a school, be the same for all schools. Hence, we have the following two-step procedure for computing Marine-to-school fitness.

(1) For each school, assign a fixed initial score to all Marines who meet the eligibility criteria for that school (ineligible Marines get a score of zero). This score (a typical value is 70) represents the weight given to the mandatory properties in computing suitability. Then, examine desirable properties and assign additional points according to the level of the property to Marines who meet each desirable property (see Fig. 3). The result is an initial fitness score for each Marine for the given school.

(2) For each school, normalize the initial scores so that the average fitness score computed over all Marines eligible for that school is 100. This condition is critical for gaming RDdss to produce good recruitment decisions.

![](/api/attachments/HKQFK56C/fulltext/images/2918db44601a0f5ec4fc130828ec7058fa10a2e198d2bb98ba094239a04d1179.jpg)  
Fig. 3. Exponential function for assigning fitness points based on the level of the property satisfied.

As an example, consider a school that has three eligible Marines and two desirable properties (one each at levels 1 and 2). Marine A meets none of these properties, and so gets an initial score of 70. Marine B meets both properties, resulting in 48 additional points (32 and 16) for a total score of 118. Marine C meets only the second property, getting a total score of 86. After normalization, the scores are 77, 94, and 129, respectively for Marines A, B, and C, resulting in an average fitness of 100. For a second school that has no desirable properties at all, the final fitness score of each eligible Marine will be 100.

## 2.2. Making good distribution decisions

The preprocessing component of RDdss computes the school penalties and the Marine-to-school fitness matrix. These, along with school quotas, are fed into the assignment model that produces the optimal solution based on the total utility function (Eq. (1)). Once the necessary decision models, data, and algorithms are in place, there are two important ingredients for making good decisions: a meaningful set of metrics for measuring the quality of candidate solutions, and a procedure for obtaining the ideal solution on the defined metrics.

Given the assignment model, it may seem that the optimal solution can be found via a fully automated procedure, once the desired weights are established. However, this is not practical for three reasons. First, while fit and fill are important aspects of solution quality—and result in an objective function that can easily be quantified and optimized—they are not the only ones. Second, the relative importance of fit and fill has not been established in the Marine Corps; hence, it did not appear reasonable to specify weights or scaling in advance. Further, as we show below, a solution obtained from predetermined weights need not even be Pareto-optimal. Third, the utility score cannot be used for comparative purposes, partly because it is vulnerable to the choice of scales for measuring penalty and fitness.

Thus, while the aggregate utility score is easy to optimize on, it is not a sufficient metric, and maximizing it will not necessarily lead to the best distribution. What we need is (a) a more complete set of metrics, and (b) an interactive procedure to make trade-offs between individual metrics. Based on our understanding of the USMC manpower planning objectives, we defined four primitive metrics for evaluating the quality of alternative distribution decisions. RDdss reports all the four metrics for each solution, and provides detailed graphical output relating to those measures. These outputs may be used to compare alternative distributions and choose the one that best fit the needs of the Marine Corps at the time. We elaborate on these points below.

## 2.2.1. Metrics for evaluating solutions

The first three metrics listed below are quite obvious, and the relevance of the fourth is explained below.

1. Fill: total number of unfilled seats in schools starting in the first week. These represent wasted resources.

2. Wait: average number of weeks Marines wait before beginning school. Experience has shown that the probability of disciplinary problems is a function of the wait time.

3. Unassignables: total number of Marines not assigned to any school.

4. Fit: fitness premium (averaged over all schools) compared to an average distribution. This is the difference between the average fitness for the proposed distribution and average fitness (by definition, 100) for an average distribution.

Now it may be seen why it is important to normalize fitness scores as explained in Section 2.1.2. Since all schools have an average fitness score of 100, an average distribution will have a score of 100 for every problem instance. Hence, any increase (decrease) in average fitness can be interpreted as a fitness premium that can then be traded-off against any loss (gain) in the other three metrics. This concept of a fitness premium supports the trade-off analysis that is necessary to choose a good final solution.

## 2.2.2. Choosing good solutions

Given a set of trade-off parameters $K _ { \mathrm { f i t } }$ and $K _ { \mathrm { f i l l } } ,$ RDdss determines the distribution with the highest utility subject to those parameters. By repeatedly changing these parameters, the model manager can produce alternative distributions and compare them using the above metrics. But what parameters should be used, and when should the comparison stop? We propose a simple heuristic procedure to answer this question.

(1) Run the model with $K _ { \mathrm { f i t } } { = } 0$ and $K _ { \mathrm { f i l l } } = 1$ . The $^ { 6 6 } \mathrm { f i l l } ^ { 5 }$ and ‘‘wait’’ scores for this run are, by definition, the best achievable fill and wait scores for the given problem instance.

(2) Run the model with $K _ { \mathrm { f i t } }$ to 1 and $K _ { \mathrm { f i l l } }$ to 0. The ‘‘fit’’ score for this run is the best possible fitness for the given instance, and this is usually accompanied by a large loss in fill and wait. Since fill and wait are clearly the most important to the Marine Corps, the results of this run are unlikely to be selected as the final solution. However, the purpose of this result is that it establishes a ‘‘fitness $\mathrm { g a p ' }$ , which needs to be bridged.

Table 1  
Example: finding a good distribution

<table><tr><td></td><td>Run 1</td><td>Run 2</td><td>Run 3</td><td>Run 4</td><td>Run 5</td></tr><tr><td>K (fit, fill)=</td><td>(0, 1)</td><td>(1, 0)</td><td>(1, 1)</td><td>(1, 6)</td><td>(1, 4)</td></tr><tr><td>Unfilled seats (week 1)</td><td>23</td><td>38</td><td>25</td><td>23</td><td>23</td></tr><tr><td>Average fitness premium</td><td>28</td><td>34</td><td>33</td><td>29</td><td>33</td></tr><tr><td>Unassigned Marines</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Average wait (weeks)</td><td>1.3</td><td>1.7</td><td>1.4</td><td>1.3</td><td>1.32</td></tr></table>

The first two columns represent extreme solutions on fit and fill. Run 3 achieves excellent fit, but at some loss in fill and wait. Run 4 makes only a marginal improvement in fitness. Run 5 achieves an excellent fit while keeping the best scores on the fill and wait metrics.

![](/api/attachments/HKQFK56C/fulltext/images/9faeddf2b360c49f4c9a34e8b749e48e91cb9fd7f7dbded4b653f38be9a52e78.jpg)  
1. The Marines are ordered by SSN from lowest to highest  
2. Fit coefficient = 1  
3. Fill coefficient = 1  
4. Average fitness = 133

![](/api/attachments/HKQFK56C/fulltext/images/c896837ea95e7b424f64ef3028715524e355f3470ffffce9d14ed62eaa0c75d6.jpg)  
1. The classes are ordered by penalty from highest to lowest.  
2. Fit coefficient = 1  
3. Fill coefficient = 1  
5. Fitness premium = 33  
4. Marines unassigned = 3 out of 344  
5. Average wait (weeks) = 1.4

Fig. 4. Distribution of Marine fitness and unfilled seats for a candidate solution. Competing solutions can be compared on the basis of their corresponding graphs.

(3) Set $K _ { \mathrm { f i t } }$ to 1 and $K _ { \mathrm { f i l l } }$ to around 10. This run closes part of the fitness gap, but possibly results in some loss in fill and/or wait.

(4) Conduct additional runs by successively increasing (or decreasing) the fill weight depending on whether the aim is to improve the fill (or fit). The final decision is made by comparing the scores on the four metrics.

Table 1 gives a representative example of this procedure. Notice that the solution of Run 1 is dominated (on all metrics) by the solution of Run 4, so that the solution of Run 1 is not even Paretooptimal. This underscores the need for an interactive procedure for gaming the system, as explained above. The procedure may produce more than one Paretooptimal solution. In our experience, to date, a ‘‘pretty good’’ solution (i.e. one that closes the fitness gap considerably while resulting in zero or negligible loss in the other metrics) is found within 5–10 runs. We have further found that RDdss, compared to RDM, can produce distributions that dominate on all four metrics. Computation times on RDdss are similar to those for RDM, and even better on some of the preprocessing steps.

![](/api/attachments/HKQFK56C/fulltext/images/5a413e9dae5b9281579270c14d39b4510d00f53fc5dc61a74a583c0508908628.jpg)  
Fig. 5. Understanding why some recruits were left unassigned in a distribution. The display indicates that 12 recruits were unassigned. For the Marine being displayed, there was one candidate school that matched the Marine’s PEF. The school’s requirements are listed in the School Properties area, and the Marine’s data pertaining to these requirements is displayed in the top row.

Aggregate statistics do not tell the entire story, and when there are school seats left unfilled or Marines who are unassigned, model managers need to understand which, who, and why. Therefore, finding an efficient solution does not end the recruit distribution analysis. RDdss, besides reporting the four summary metrics (which are averages or totals), also provides features for examining the solution quality in detail. These include graphical output pertaining to the metrics, as well as the ability to inspect the critical aspects of a distribution such as which Marines were unassigned (and why). Fig. 4 depicts sample graphs that display data pertaining to solution objectives. Graphs for a particular solution reveal the distribution of the metric, and alternative candidate solutions can be compared in terms of these graphs. Fig. 5 depicts a representative screen from RDdss that allows the manager to understand why some Marines were unassigned (e.g. did they fail to meet the minimum requirements for schools, or were the schools filled to capacity?).

## 3. RDdss: architecture and functional components

The functional improvements described in the previous sections were delivered in a completely redesigned information system. The architecture of RDdss is depicted in Fig. 6. The system has six components: the switchboard, relational database, preprocessor, assignment model, solver, and analyzer. The switchboard and the analyzer comprise the interface between the user and RDdss. The preprocessor, assignment model, and solver comprise the modeling subsystem.

## 3.1. System components

The RDdss user interface is realized as a hierarchy of switchboards that lead to actionable forms (see Fig. 7 for an example leading to the model execution step). The switchboard is the mechanism by which the user navigates through RDdss. The forms allow the user to inspect, enter, or update data, and launch commands that are executed by the database or modeling components. This user interface paradigm is an important improvement: it provides an intuitive navigation sequence, via the use of hierarchical switchboards, and minimizes the potential for data entry errors by automating the data entry process as far as possible.

The analyzer is the other component making up the user interface. This is where the RDdss manager analyzes assignment results, seeking insights for developing a ‘‘good’’ solution (see earlier discussion about metrics and representations for solution analysis). Additionally, important questions about any particular distribution (e.g. why some Marine was left unassigned) are answered in a couple of mouse clicks. This is an entirely new component that has no counterpart—either automated or manual—in the previous system.

![](/api/attachments/HKQFK56C/fulltext/images/667d8068c1325e00d9a5e32b5c31408106b6ef935e1c049e2a70578494aebe73.jpg)  
Fig. 6. RDdss architecture.

![](/api/attachments/HKQFK56C/fulltext/images/46443b399612847487f7eb4d307e9ad001ebffcb81b3495fb91651e711ab7f16.jpg)  
Fig. 7. Setting up a model run.

Standard relational database technology and design principles (see, e.g. Refs. [2 – 4]) were used in the RDdss. This leads to a large reduction in data entry errors, and eliminates the need to enter data already known to the system. Data management in RDdss follows a data warehousing approach [6] wherein data tables relevant to the model execution are extracted from a transactional database, and are stored and manipulated in the DSS.

The preprocessor component computes the information necessary for setting up the assignment model instance. Using the database extract corresponding to the problem instance, it determines the demand for each class, the penalty associated with a unit shortfall in each class, and the Marine-to-class fitness matrix. The assignment model (see Appendix A), implemented algebraically in AMPL, is the other component of the modeling subsystem.

## 3.2. Using RDdss

Using the RDdss involves three activities, (1) setting up a run, (2) executing the model, and (3)

customizing a run and results. We now discuss each activity briefly.

Setting up an RDdss run is straightforward. Fig. 7 graphically illustrates the steps that the model manager executes by following the hierarchical order. The high-level steps include data import, data maintenance, and preprocessing. The detailed steps can be read-off the figure and are quite self-explanatory. The model operator can specify the relative importance of the mandatory and desired properties in computing the overall fitness scores. The end result of this stage is the creation of AMPL input files.

Execution of the assignment model takes place next. As explained above, the model operator is able to perform multiple runs by modifying the fit and fill weights. RDdss produces the optimal assignment, values of the metrics, and graphical representations of detailed performance information about each solution. This process is essential for determining a ‘‘good’’ solution, as described in the previous section. The interface also allows the model operator to make some manual assignments (these are called ‘‘reclassification’’ and ‘‘special assignments’’) where necessary.

## 4. Conclusion

We believe the innovations and capabilities introduced by the RDdss can greatly benefit the USMC’s Marine Enlisted Assignments branch. It can help the USMC to more effectively accomplish its mission as stated by the Commandant of the Marine Corps, ‘‘to put the right Marine in the right place at the right time with the right skills and quality of life’’. While our initial objectives were to produce a research prototype, we not only delivered a working functional system, but also interfaced it with the existing USMC subsystems (for input data import and solution export) and with RDM (to facilitate parallel testing and computation of metrics for RDM results). To a large degree, our success was due to an integration of information technology concepts with concepts from operations research and decision analysis. Many of these design concepts and features can be applied to decision support systems developed in support of other problems.

For much of the project duration, there was almost no interest in RDdss within the USMC. Even with its many limitations, the current RDM system ‘‘worked’’ and has worked for 30 years, in the sense that it does produce an output file. This may have led to an attitude of ‘‘if it ain’t broke, don’t fix it’’ especially in an organization where other operational activities were more important. Fortunately, our work on RDdss was noticed by an internal think tank set up by the head of the manpower division to create or find innovative ideas for improving manpower processes and systems, and brought to the attention of the top management. Following this, we installed and linked RDdss into the operational USMC manpower systems, tested it on real data sets, and demonstrated considerable benefits over RDM.

Demonstrating the value of a better recruit distribution required a leap of faith for USMC management: while unfilled seats had a direct monetary cost, there was no way to value improvements in fitness, and some managers were unconvinced of the value of improving fitness even when that meant no loss in fill. To demonstrate the benefit, we consider an

RDdss solution that improves only the fitness metric and equals the RDM solution on all other metrics. Using the standard USMC estimate of the annual cost of each Marine (about US\$30,000), let us make a very conservative claim: a 1% fitness improvement causes a 0.01% improvement in the Marine’s effectiveness. Thus, a 1% overall improvement in fitness translates into a US\$3 value to the Marine Corps per Marine. This results in a US\$360,000 annual value to the Marine Corps considering there are about 30,000 recruits a year, who stay an average of 4 years. Thus, even a 3% gain in fitness compared to RDM would result in an annual benefit of over one million dollars.

In spite of our success in developing a working system, installing and integrating it with the existing systems, and convincing top management of its benefits, RDdss remains unused in the USMC. Institutional resistance was a factor. So was the organizational structure: the models and systems are controlled by the information systems group whose interest was in ensuring that the systems ‘‘worked’’, whereas the manpower analysis group cared about the quality of the modeling but did not control these systems. Following our successful demonstration of RDdss to the top management, and an agreement to parallel-test RDdss with the RDM system, a physical move of the USMC headquarters led to the disruption of computing. Critical personnel changes, soon after this move, proved to be the last straw that broke this camel’s back. Our project team was not equipped to deal with problems of this sort. The parallel testing plan did not take off.

The situation regarding manpower planning is not too dissimilar in the other US military services. Recent research by Tivnan [9] examines this issue, and this paragraph is based on Tivnan’s findings. In the US Army, Schank et al. [7] found that a civilian contractor owns and maintains the code, including minor upgrades. The Army cannot even run this model independently of the contractor: ‘‘excessive runtimes and the expertise required to conduct the monthly runs likely will prevent the USA from ever conducting the MOSLS runs independent of the supporting civilian contractor’’. In the Navy, a system called Enlisted Personnel Allocation and Nomination System (EPANS) was developed in the 1990s. It lies unused, however, because of institutional resistance and lack of interest [1]. In discussions with the Navy personnel, Tivnan found that the Navy employs a crude sequential ‘‘first come, first served’’ approach to assignment, a process that ‘‘is not efficient but. . . done it this way for 30 years’’.

In the larger scheme of things, recruit distribution is a rather small problem for the US Marine Corps and other branches of the military, each of whose annual budget is in billions of dollars. However, classical decision science ideas such as those expressed in this article can cause significant improvements in decision making in a wide variety of situations, including many other manpower decisions. Recognition of this fact by top USMC manpower leadership was an important outcome of this project.

## Acknowledgements

This research was supported by a research grant from the Deputy Chief of Staff (Manpower and Reserve Affairs), US Marine Corps (1997–1998).

## Appendix A. Mathematical model

Once the rules for Marine eligibility and desirability for a school have been satisfied by developing an appropriate fitness score for each Marine-school pair, the recruit distribution problem is formulated as a standard assignment model.

## A.1. Sets

M: Marines

C: Classes

## A.2. Exogenous variables

$\mathrm { f i t } _ { m , c } \colon$ the desirability of assigning Marine m, to class $c \ ( \mathrm { f i t } _ { m , c }$ for where either the Marine m does not meet the class’ mandatory properties, or where the class c does not fulfill the Marine’s PEF guarantee).

demand : demand for Marines to be trained at class c.

penalty : penalty for each unit of demand not met (a higher value means that it is more critical to fill the class).

## A.3. Decision variables

$x _ { m , c }$ (binary integer): 1, if Marine m, is assigned to class c; 0 otherwise.

## A.4. Control variables

$k _ { 1 } \mathrm { { : } }$ : Weight assigned to fitness.

$k _ { 2 } \mathrm { : }$ Weight assigned to fill.

## A.5. Objective

Maximize the Total Utility: (Total Reward  Total Penalty)

$$
\begin{array}{l} \mathrm{TU} = k _ {1} \left(\sum_ {c \in \mathcal {C}} \sum_ {m \in \mathcal {M}} \operatorname{fit} _ {m, c} x _ {m, c}\right) \\ - k _ {2} \left(\sum_ {c \in \mathcal {C}} \text { penalty } _ {c} (\text { demand } _ {c} - \sum_ {m \in \mathcal {M}} x _ {m, c})\right) \end{array}\tag{2}
$$

## A.6. Constraints

 Assignment limit: a Marine is assignable to one school at most

$$
\sum_ {c \in \mathcal {C}} x _ {m, c} \leq 1 \quad \forall m \in \mathcal {M}\tag{3}
$$

 Eligibility: a Marine is only assignable to a class they are fit for (this prevents assigning Marines with a fitness score of zero)

$$
x _ {m, c} \leq \operatorname{fit} _ {m, c} \quad \forall m \in \mathcal {M}, \forall c \in \mathcal {C}\tag{4}
$$

 Capacity: schools cannot be oversupplied

$$
\sum_ {m \in \mathcal {M}} x _ {m, c} \leq \text { demand } _ {c} \quad \forall c \in \mathcal {C}\tag{5}
$$

## References

[1] A. Ali, J. Kennington, T. Liang, Assignment with en route training of navy personnel, Naval Research Logistics 40 (1993) 581–592.

[2] C. Batini, S. Ceri, S.B. Navathe, Conceptual Database Design:

An Entity-Relationship Approach, Benjamin/Cummings Publishing, Redwood City, 1992.

[3] E.F. Codd, A relational model of data for large shared databanks, Communications of the ACM 13 (6) (June 1970) 377 – 387.

[4] C. Date, An Introduction of Database Systems, Volume 1, 5th ed., Addison-Wesley Publishing, Reading, MA, 1990.

[5] J. Dumas, Designing User Interfaces for Software, Prentice Hall, Upper Saddle River, NJ, 1988.

[6] W. Inmon, Information Engineering for the Practitioner, Chapter 13, DSS Derived Data Environment, Yourdon Press, Englewood Cliffs, NJ, 1988, pp. 155–174.

[7] J.F., Schank, M.C., Harrell, H.J., Thie, M.M., Pinto, J.M., Sollinger, Relating resources to personnel readiness. Technical report, RAND, 1997.

[8] K.J., Snoap, Reengineering the United States Marine Corps recruit distribution model, rdm. Master’s thesis, Naval Post graduate School, 1998.

[9] B.F., Tivnan, Optimizing United States Marine Corps enlisted assignments. Master’s thesis, Naval Postgraduate School, 1998.

Hermant Bhargava is a Professor in the Management Science and Information Systems at Penn State University’s Smeal College of Business Administration. He received his PhD in Decision Sciences from The Wharton School, University of Pennsylvania, in 1990. Dr. Bhargava is Area Editor (Computing and Decision Technology) for Operations Research, and also serves on the Editorial Boards of the journals Decision Support Systems and Electronic Commerce Research and Applications. He is a member of INFORMS and IEEE Computer Society, and is on the Board of the INFORMS Computing Society. His primary research interests cover decision technologies, logic modelling, and problems in the economics of technology-enabled business, including bias and network effects in information intermediaries and gatekeepers, market segmentation through versioning, contingent-price contracts in electronic commerce, and inventory and pricing policies for electronic retailers. His research has appeared in several journals including INFORMS Journal on Computing, Decision Support Systems, Journal of Management Information Systems, IEEE Computer, and International Journal of Electronic Commerce.
