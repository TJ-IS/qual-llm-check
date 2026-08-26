---
otero_id: 18375
otero_key: "XQ6XH3Z4"
title: "Variance tracking MIS in interdependent manufacturing contexts: An initial examination"
authors: "Randolph B. Cooper; James T. Mackey"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90002-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Variance Tracking MIS in Interdependent Manufacturing Contexts: An Initial Examination \*

Randolph B. Cooper

Graduate School of Business Administration, The University of Michigan, Ann Arbor, MI 48109, USA

James T. Mackey

School of Business and Public Administration, California State University-Sacramento, Sacramento, CA 95819, USA

There are many conflicting signals concerning the effectiveness of variance-tracking management information systems (MIS) in manufacturing contexts. Though there are anecdotal references to dissatisfaction with the systems and conceptual arguments concerning inaccuracy, no empirical evaluation of the effects of such system deficiencies could be found. This, combined with the widespread use of such MISs makes it of interest to further investigate them in manufacturing context. This paper provides an exploratory empirical examination of variance tracking MIS deficiencies. Via a simulation experiment, we find that, in an interdependent manufacturing context, variance-tracking MISs may severely misrepresent whether production departments are in or out of control. We thus agree with those who suggest that variance-tracking MISs may not be appropriate in interdependent manufacturing contexts. Contributions include an empirical demonstration of the kind and extent of MIS deficiencies that can occur in these contexts. However, the exploratory nature of this study imposes significant problems of external validity.

Keywords: MIS effectiveness, MIS productivity, manufacturing management information, cost variance reporting, cost accounting, interdependent manufacturing.

## 1. Introduction

One type of information system used by manufacturing management reports the deviations (variances) of actual manufacturing costs from standard costs in order to identify problems with the manufacturing process. However, the effectiveness of such variance-tracking MISs has been questioned. Though many people denounce their use for production management, others support their use [2] [6]. Those against the system argue that the measure used by variance-tracking MISs are not accurate [3] and do not include non-financial indicators necessary for good management [10]. However, all MISs contain inaccuracies and limitations. The question, then, is when variance-tracking MISs are deficient enough to warrant changing or abandoning them.

Evidence from the literature is far from conclusive. Though there are many anecdotal references

![](/api/attachments/XQ6XH3Z4/fulltext/images/7fe6cc26c9d0bce3b4cc65562bc40a6354359639c866489d48ad47b091dd2653.jpg)

![](/api/attachments/XQ6XH3Z4/fulltext/images/1cb57ebad8a99e3677c5894f6b857fa009c5816b387f108dc41a2554455bb041.jpg)

Randolph B. Cooper is an Assistant Professor of Computer and Information Systems at the School of Business Administration, University of Michigan in Ann Arbor. He received his B.A. in Economics, his M.B.A., and his Ph.D. in Management from the University of California at Los Angeles. His research interests include information requirements analysis and management information system productivity evaluation.

James T. Mackey is an Associate Professor at California State University - Sacramento. He received his Ph.D. in Accountancy from the University of Illinois, and is a C.P.A. and a C.M.A. He has taught at the University of Wisconsin - Madison, the University of Michigan - Ann Arbor, and York University in Canada. His teaching and research interests center around the role of accounting for control, costing, and capital budgeting within the new manufacturing technologies.

to dissatisfaction with MISs and conceptual arguments concerning their inaccuracy, no empirical evaluation of the effects of such system deficiencies could be found. This, combined with the widespread use of such MISs [4] [14] makes it valuable to investigate variance-tracking MISs in manufacturing contexts.

We investigated variance-tracking MISs using a simulation experiment. We found that in interdependent manufacturing contexts, they may severely misrepresent the degree of control in production departments. We thus agree with those who suggest that variance-tracking MISs may not be appropriate in more interdependent manufacturing contexts.

The importance of examining interdependent manufacturing contexts comes from recent innovations in production planning and production technology, such as material requirements planning (MRP) approaches. These innovations have resulted in increased efficiency, by reducing traditional decoupling devices such as work-in-process inventories [1]. This reduction can result in faster, more reliable delivery times, lower reject rates, and lower overhead costs. In addition, however, reduced decoupling causes manufacturing departments to become more interdependent, increasing the sensitivity of one department's activities to those of others. Since the variance-tracking MISs currently used for manufacturing management were generally developed during times when production departments were more independent, an implicit assumption of these MISs was production department independence. It is thus necessary to determine the potential effect of these MISs in contexts where this assumption is violated.

The variance-tracking MIS examined here is a flexible budget variance tracking system; this is a monitoring tool used to facilitate management-by-exception in relatively decentralized environments. By monitoring variances from flexible budgets, upper management can determine whether departmental managers are exercising their discretion effectively. This has been shown to be effective in independent production contexts [7] [8] [9] [16].

## 2. The Experiment

The objective of our experiment was to examine the effect of an interdependent manufacturing environment upon the usefulness of a typical variance-tracking MIS. Because true operating states must be known, an actual factory environment would be very difficult to investigate. Similarly, a behavioral experiment would confound the analysis with behavioral issues - such as managerial motivation. In addition, an analytical analysis of the necessary complexity was found to be intractable. Thus, a simulation experiment was used to examine this MIS usefulness issue. A brief summary of the simulation model is presented below; the full detail is available in [12].

## 2.1. Simulation Model

The simulation model is made up of three sequentially interdependent departments; sequential interdependence is described by Thompson [15] as a typical core technology. In such a technology, the output of the preceding department serves as the input to the next. It is assumed that all raw material required by the first department is available. In addition, similar to a “make-to-order” factory, it is assumed that all orders are met on time; this eliminates the need for evaluating the cost of not meeting delivery dates.

Each department is simulated by implementing an identical production function derived from a five year study of a paint factory, which was conducted by Holt et al. [5]. Using their data, monthly production quotas are determined for each department. Weekly and daily production requirements are a function of these monthly quotas, adjusted for production-to-date, buffer inventories, etc.

The three department managers use their knowledge of the operating conditions to make optimal (cost minimizing) adaptations in production activity. For example, estimated production of the first and last departments, along with current inventory levels, labor costs, and inventory carrying costs are used by the middle department manager to determine production levels. This kind of decision making is appropriate in highly interdependent contexts, allowing global optimization. Such an approach was chosen to help focus upon the effectiveness of variance-tracking MIS, rather than confounding the study with departmental sub-optimization issues. Thus, the MIS can be evaluated in a context where managers are acting with appropriate knowledge and motivation to enable cost-minimizing production on a factory-wide basis.

The variance reporting used is typical; it is based upon production-related costs (excluding, for example, inventory carrying). A weekly variance is calculated for each department by subtracting actual costs from standard costs. Variance limits (i.e., limits beyond which costs are reported as an exception) were determined by running 100 replications of the five year simulation, assuming efficient production as discussed below. Dropping the first six weeks of cost data for each replication to allow the system to achieve steady state resulted in 25,400 weekly variances. The absolute values of these variances were ranked, and the largest 10 percent were considered to be excessive, reportable exceptions; this means that if variances are normally distributed, an exception variance report is issued when departmental costs are more than 1.65 standard deviations above or below those flexibly budgeted for a given week.

## 2.2 Hypotheses and Experimental Design

Previously referenced work indicates that the activities of independent responsibility centers do not significantly affect the usefulness of variance reports. However, the relatively high binding of variance-tracking systems with these independent contexts makes it reasonable to hypothesize an interaction between production department interdependence and the effectiveness of variance-tracking MIS.

Their usefulness to upper management depends upon their help in determining the efficiency of departmental activities. If variance reports are to be effective, they should be able to depict:

(1) changes in one department's inefficiency;

(2) inefficient departments from efficient ones;

(3) relative inefficiency across departments.

These three issues lead to the following three null hypotheses:

$H_{1}$ : Increased production inefficiency in a department will not result in increased exception variances reported for that department.

$H_{2}$ : Production inefficiency in one department will not result in significantly more exception variances for that department than for other, efficient, departments.

$H_{3}$ : The number of exception variances for one inefficient department will be significantly different from the number of variances for other equally inefficient departments.

The experimental treatment consists of taking each department and programming it to be inefficient (i.e., reducing actual output) by 10, 20, and 30 percent. This results in a three-by-three experimental matrix consisting of three inefficiency levels by three positions for the inefficient department (first, middle, and last). Another dimension to this experimental design indicates the department whose variances are being examined. For example, although the first department may be inefficient by 20 percent, because of the potential for interaction, the department being examined for exception cost variance could be the first, middle, or last department. The final dimension includes the type of distributions representing productive activity. Two distributions are used: Normal and Gamma. The Normal is used to represent more labor-intensive (less machine dependent) production, where major production interruptions are highly un-

Table 1  
Average number of exception variances.

<table><tr><td rowspan="2"></td><td rowspan="2">Inefficiency level</td><td colspan="3">Department being examined</td></tr><tr><td>First department</td><td>Middle department</td><td>Last department</td></tr><tr><td colspan="5">For Normal distribution</td></tr><tr><td rowspan="3">First depart.</td><td>10%</td><td>23.885</td><td>23.630</td><td>23.390</td></tr><tr><td>20%</td><td>24.125</td><td>23.210</td><td>22.285</td></tr><tr><td>30%</td><td>24.530</td><td>22.270</td><td>19.230</td></tr><tr><td rowspan="3">Middle depart.</td><td>10%</td><td>23.800</td><td>23.680</td><td>23.750</td></tr><tr><td>20%</td><td>23.790</td><td>23.700</td><td>23.760</td></tr><tr><td>30%</td><td>23.765</td><td>23.675</td><td>23.785</td></tr><tr><td rowspan="3">Last depart.</td><td>10%</td><td>30.170</td><td>26.975</td><td>26.650</td></tr><tr><td>20%</td><td>29.420</td><td>31.115</td><td>33.590</td></tr><tr><td>30%</td><td>29.435</td><td>33.700</td><td>38.440</td></tr><tr><td colspan="5">For Gamma distribution</td></tr><tr><td rowspan="3">First depart.</td><td>10%</td><td>23.440</td><td>23.495</td><td>23.000</td></tr><tr><td>20%</td><td>24.320</td><td>24.050</td><td>22.990</td></tr><tr><td>30%</td><td>24.495</td><td>24.490</td><td>21.000</td></tr><tr><td rowspan="3">Middle depart.</td><td>10%</td><td>23.095</td><td>16.000</td><td>23.460</td></tr><tr><td>20%</td><td>21.445</td><td>15.000</td><td>23.590</td></tr><tr><td>30%</td><td>22.490</td><td>16.000</td><td>23.575</td></tr><tr><td rowspan="3">Last depart</td><td>10%</td><td>15.000</td><td>22.490</td><td>26.000</td></tr><tr><td>20%</td><td>17.180</td><td>23.490</td><td>23.990</td></tr><tr><td>30%</td><td>25.970</td><td>23.490</td><td>24.000</td></tr></table>

Table 2  
Analysis of variance table for type SPF-qru.p design. $^{a}$

<table><tr><td>Source</td><td>Regular df.</td><td>Sum of squares</td><td>Mean squares</td><td>Normal F ratio</td><td>Conservative F</td></tr><tr><td>Between subjects</td><td>nqru-1=3599</td><td></td><td></td><td></td><td></td></tr><tr><td>B</td><td>q-1=2</td><td>2572.00</td><td>1286.0</td><td>98.79 *</td><td></td></tr><tr><td>C</td><td>r-1=2</td><td>41910.20</td><td>20955.10</td><td>1609.82 *</td><td></td></tr><tr><td>D</td><td>u-1=1</td><td>39445.33</td><td>39445.33</td><td>3030.30 *</td><td></td></tr><tr><td>BC</td><td>(q-1)(r-1)=4</td><td>11285.85</td><td>2821.46</td><td>216.75 *</td><td></td></tr><tr><td>BD</td><td>(q-1)(u-1)=2</td><td>450.11</td><td>225.05</td><td>17.29 *</td><td></td></tr><tr><td>CD</td><td>(r-1)(u-1)=2</td><td>37469.04</td><td>18734.52</td><td>1439.24 *</td><td></td></tr><tr><td>BCD</td><td>(q-1)(r-1)(u-1)=4</td><td>1574.33</td><td>393.58</td><td>30.24 *</td><td></td></tr><tr><td>subjects within groups</td><td>qru(n-1)=3582</td><td>46626.82</td><td>13.17</td><td></td><td></td></tr><tr><td>Within subjects</td><td>nqru(p-1)=7200</td><td></td><td></td><td></td><td></td></tr><tr><td>A</td><td>p-1=2</td><td>3885.17</td><td>1942.58</td><td>326.77</td><td>6.631 *</td></tr><tr><td>AB</td><td>(p-1)(q-1)=4</td><td>841.95</td><td>210.49</td><td>35.41</td><td>4.61 *</td></tr><tr><td>AC</td><td>(p-1)(r-1)=4</td><td>20641.17</td><td>5160.29</td><td>868.03</td><td>4.61 *</td></tr><tr><td>AD</td><td>(p-1)(u-1)=2</td><td>2335.98</td><td>1167.99</td><td>196.47</td><td>6.63 *</td></tr><tr><td>ABC</td><td>(p-1)(q-1)(r-1)=8</td><td>1776.55</td><td>222.07</td><td>37.36</td><td>3.32 *</td></tr><tr><td>ABD</td><td>(p-1)(q-1)(u-1)=4</td><td>4203.36</td><td>1050.84</td><td>176.77</td><td>4.61 *</td></tr><tr><td>ACD</td><td>(p-1)(r-1)(u-1)=4</td><td>9846.38</td><td>2461.60</td><td>414.08</td><td>4.61 *</td></tr><tr><td>ABCD</td><td>(p-1)(q-1)(r-1)(u-1)=8</td><td>13438.88</td><td>1679.86</td><td>282.58</td><td>3.32 *</td></tr><tr><td>AX subjects within groups</td><td>qru(n-1)(p-1)=7164</td><td>42588.55</td><td>5.945</td><td></td><td></td></tr></table>

$^{a}$ A = department being examined.  
B = inefficiency levels.  
C = inefficient department.  
$\mathbf{D} =$ distribution.  
\* = Significant at less than 0.01.

likely. The Gamma is skewed towards inefficient production, allowing for major production interruptions due, for example, to machine breakdowns in more machine-intensive (machine dependent) production.

The experiment is thus a split plot factorial design with repeated measures on the department being examined. This results in 54 individual cells $(3 \times 3 \times 3 \times 2)$ . The dependent variable is the average number of exception variances per week occurring over a 5 year simulation. The simulation was run 3,600 times, enabling 200 observations for each of the 54 cells (every 5 year simulation gave one observation for each of the three departments being examined).

## 2.3. Results

Table 1 summarizes the average number of exception variances reported under each of the experimental conditions. The analysis of variance is summarized in table 2. Because of the repeated measures, conservative F-tests suggested by Kirk [11] are computed. All main effects and interactions are significant at the 0.01 level. However, the three hypotheses of interest require further investigation. These are described below, and are evaluated using Scheffe's a posteriori comparison method as outlined by Kirk.

$H_{1}$ is concerned with the positive correlation between departmental inefficiency and the frequency of exception variance reports for that department. If $H_{1}$ is rejected, then the variance-tracking system does help depict changes in a specific department's inefficiency. As illustrated in table 3, $H_{1}$ is rejected (alpha = 0.01) in only one out of the six possible cases (for the last department when production is described by a Normal distribution).

Detail for hypothesis one (the average number of exception variances for each inefficient department are compared across inefficiency levels, for both Normal and Gamma distributions). $^{a}$

<table><tr><td rowspan="2">Inefficient department being examined</td><td colspan="3">Inefficiency level differences</td></tr><tr><td>10%-20%</td><td>20%-30%</td><td>10%-30%</td></tr><tr><td colspan="4">For Normal distribution</td></tr><tr><td> $A_1C_1$ </td><td>-0.24</td><td>-0.41</td><td>-0.65</td></tr><tr><td> $A_2C_2$ </td><td>-0.02</td><td>0.03</td><td>0.01</td></tr><tr><td> $A_3C_3$ </td><td>-6.94 *</td><td>-4.85 *</td><td>-11.79 *</td></tr><tr><td colspan="4">For Gamma distribution</td></tr><tr><td> $A_1C_1$ </td><td>-0.88</td><td>-0.18</td><td>-1.06</td></tr><tr><td> $A_2C_2$ </td><td>-1.00</td><td>1.00</td><td>0.00</td></tr><tr><td> $A_3C_3$ </td><td>2.01 **</td><td>0.00</td><td>2.01 **</td></tr></table>

$^{a}A_{n}=$ Department being examined is n (n=1 for first department, n=2 for middle department, n=3 for last department).  
$C_{m} =$ Inefficient department $m$ (see $n$ , above).  
\* = Significant at alpha = 0.01. Scheffe's test: $F_{\text{critical}} = 17(2.01, 17.7164) = 17(1.96) = 33.32$ . Critical difference between means: (33.32 [5.945 (2/200)]) $^{1/2}$ = 1.41.  
\*\* = Significant at alpha = 0.01, but in the wrong direction.

$H_{2}$ addresses the ability to distinguish inefficient from efficient departments. If $H_{2}$ is rejected, then the variance-tracking system can differentiate between inefficient and efficient departments. As illustrated in table 4, $H_{2}$ is rejected for the first and the last departments (alpha = 0.01) for both production distributions. However, $H_{2}$ cannot be rejected for the middle department. In fact, the middle department tends to generate fewer exception variance when it is inefficient (alpha = 0.01 for Gamma production).

$H_{3}$ is concerned with the detection of relative inefficiency across departments. If $H_{3}$ is rejected, then equally inefficient departments produce significantly different numbers of exception variances. The variance-tracking system thus could not be used to identify the relative inefficiency of different departments. As illustrated in table 5, $H_{3}$ is rejected (alpha = 0.01) in all but 28 percent of the cases. The variance-tracking system seems to react appropriately only when the first is compared to the middle department with Normal production.

Detail for hypothesis two (the average number of exception variances reported by each inefficient department is compared with the average of those reported by the other two (efficient) departments. These comparisons are done for both the Normal and the Gamma distributions). $^{a}$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$A_{1}C_{1}-(A_{2}C_{1}+A_{3}C_{1})/2$

Normal 24.18-(23.04+21.64)/2=1.84 *
Gamma 24.09-(24.01+22.33)/2=0.92 *
$A_{2}C_{2}-(A_{1}C_{2}+A_{3}C_{2})/2$

Normal 23.69-(23.79+23.77)/2=-0.09
Gamma 15.67-(22.34+23.54)/2=-7.27 **
$A_{3}C_{3}-(A_{1}C_{3}+A_{2}C_{3})/2$

Normal 32.89-(29.68+30.60)/2=2.76 *
Gamma 24.66-(19.38+23.16)/2=3.39 *
</div>

$^{a} A_{n}=$ Department being examined is n (n=1 for first department, n=2 for middle department, n=3 for last department).  
$C_{m} =$ Inefficient department $m$ (see $n$ , above).  
\* = Significant at alpha = 0.01. Scheffe's test: $F_{\text{critical}} = 2(F_{0.01,2,7164}) = 2(4.61) = 9.22$ . Critical difference between means: (9.22 [5.945 (0.5/600)] $^{1/2}$ = 0.21.  
\*\* = Significant at alpha = 0.01, but in the wrong direction.

Detail for hypothesis three (the average number of exception variances for one inefficient department is compared to that of each other inefficient department at various inefficiency levels. This is done for both the Normal and Gamma distributions). $^{a}$

<table><tr><td>Inefficiency level</td><td> $A_{1}C_{1}-A_{2}C_{2}$ </td><td> $A_{1}C_{1}-A_{3}C_{3}$ </td><td> $A_{2}C_{2}-A_{3}C_{3}$ </td></tr><tr><td colspan="4">For Normal distribution</td></tr><tr><td>10%</td><td>0.21</td><td>-2.77 *</td><td>-2.97 *</td></tr><tr><td>20%</td><td>0.43</td><td>-9.47 *</td><td>-9.89 *</td></tr><tr><td>30%</td><td>0.86</td><td>-13.91 *</td><td>-14.77 *</td></tr><tr><td colspan="4">For Gamma distribution</td></tr><tr><td>10%</td><td>7.44 *</td><td>-2.56 *</td><td>-10.00 *</td></tr><tr><td>20%</td><td>9.32 *</td><td>0.33</td><td>-8.99 *</td></tr><tr><td>30%</td><td>8.50 *</td><td>0.50</td><td>-8.00 *</td></tr></table>

$^{a} A_{n}=$ department being examined is n(n=1 for first department, n=2 for middle department, n=3 for last department).  
$C_{m} =$ inefficient department $m$ (see $n$ , above).  
\* = Significant at alpha = 0.01. Scheffe's test: $F_{\text{critical}} = 17(F_{0.01,17.7164}) = 17(1.96) = 33.32$ . Critical difference between means: (33.32 [5.945 (2/20G)]) $^{1/2}$ = 1.41.

## 3. Discussion of Results

The results of our experiment indicate that the popular use of variance-tracking MIS to help control interdependent production departments may be inappropriate. Under these conditions, this type of MIS may not reliably indicate:

(1) changes in one department's inefficiency,

(2) inefficient versus efficient departments,

(3) relative inefficiency across departments.

In addition to unreliability, there are interesting cases when variance-tracking works in a counter-intuitive manner. For example, the evidence surrounding $H_{2}$ indicates that variance-tracking is effective for depicting when the first or the last department is inefficient. Problems occur when tracking the variances associated with the middle department. In fact, with Gamma production, exception reporting occurs in a counter-intuitive manner: the reports decrease for the middle department when it is inefficient. These findings can be explained by the reaction to inefficiencies by surrounding departments. To give an understanding of these departmental interactions, and their effect upon exception reporting, this result is further discussed below.

Though other departmental reactions to an inefficient department may be globally optimal, they typically result in decreased individual department productivity. For example, if the middle department is inefficient in one period, the first department will reduce its production to reduce inventory holding costs, while the last department has a good chance of production halts due to insufficient material input. Since the middle department's difficulties are short run, the first and last departments do not lay off personnel. This results in higher costs per unit produced for these two departments, though they have reacted in an optimal manner given the middle department's inefficiency. In this scenario, there is a good chance that all three departments will generate an exception report. Thus it seems reasonable to find no significant difference with Normal production between the number of exception reports for the three departments when the middle department is inefficient.

The effects of Gamma production in this context illustrates an interesting variation. Rather than having an equal number of exception reports, the end departments actually have more than the middle department. This can be explained by envisioning the middle department to be very inefficient in one period, the Gamma Distribution being skewed toward inefficiency. This very large disturbance results in extreme production cutback by the end departments, which takes several periods to overcome. Because of the requirement to meet finished goods demand, all three departments subsequently attempt to employ overtime labor to increase output; the use of overtime increases the chance for an exception report. However, for the middle and last departments, the use of this extra labor is constrained by the availability of input inventories, while for the first and middle departments, the use of this extra labor is constrained by the ability of subsequent departments to use the output (so that excess buffer inventories are not produced). These constraints increase the time required for the system to return to “normal” production, but also temper the potential for exception reports. Thus, the middle department has both types of constraints, while the other two departments only have one constraint each. It is for this reason that the middle department can have fewer exception reports when it is inefficient. It is interesting to note that, though not statistically significant, exception reports with Normal production also show this pattern.

## 4. Conclusion

The combination of widespread use of variance-tracking systems in manufacturing contexts with the controversy surrounding the validity of such systems led to this exploratory research. A simulation was built which depicted an interdependent three stage production process based upon data gathered from a paint manufacturing firm. The simulation revealed potential problems with using traditional variance-tracking MISs in such interdependent manufacturing contexts.

Given these problems, the question is: why do these MISs currently enjoy wide-spread popularity in manufacturing firms? Such continued use could be because the systems:

(1) have not become deficient enough to warrant the cost of updating (they are noisy but still useful).

(2) are an example of neutral mutation [13] and serve no useful nor harmful purpose,

(3) are deficient enough to warrant the cost of updating but production managers are unaware of the problems.

Based upon our simulation, there is evidence that, in todays interdependent manufacturing contexts, variance-tracking systems can be worse than noisy: they can provide misinformation. The noisy-but-useful and the neutral mutation arguments are thus not supported. Current use of variance-tracking MISs may then be because production managers are unaware of the extent of the problem. This research can then serve to make production managers more aware of this issue.

What are potential solutions to these variance-tracking problems? There are at least three possibilities. First, if the manufacturing processes are highly interdependent it may not make sense to treat departments as autonomous decision making units. Rather, the entire factory (or that subset of highly interdependent departments) should be treated as a single unit for control purposes. Second, variance-tracking systems can become more sophisticated and include factory-wide efficiency factors (inventory holding costs, effect of stockouts upon other departments' efficiencies) in addition to the traditional intra-departmental efficiency factors (idle labor, overtime labor, idle machines). Finally, variance-tracking systems should be treated as only one of many information sources used to evaluate departmental control [2]. Other information can include quality measures, physical productivity measures, and work force skill and morale measures [10].

As a final note, the issue of external validity should be raised. Because of the exploratory nature of this study, any generalizations must be made tentatively. Further research is required to validate these results for other continuous manufacturing environments, as well as for intermittent and job shop environments.

## References

[1] Sumer C. Aggarwal, "MRP, JIT, OPT, FMS? Making Sense of Production Operations Systems", Harvard Business Review, Sept.-Oct. 1985, pp. 8-16.

[2] James B. Edwards and Julie A. Heard, "Is Cost Accounting the No. 1 Enemy of Productivity", Management Accounting, June 1984, pp. 44-49.

[3] Eliyahu M. Goldratt, as described in "Is Cost Accounting the No. 1 Enemy of Productivity", by Edwards and Heard, Management Accounting, June 1984. pp. 44–49.

[4] Robert H. Hayes and Kim E. Clark, "Why Some Factories Are More Productive Than Others", Harvard Business Review, Sept.-Oct. 1986, pp. 66–73.

[5] C. Holt, R. Modigliani, J. Muth, and H. Simon, Planning Production, Inventories, and Work Force, Prentice-Hall, 1960.

[6] Charles T. Horngren, Cost Accounting: A Managerial Emphasis, fifth ed., Prentice-Hall, 1982.

[7] F. Jacobs, "An Evaluation of the Effectiveness of Some Cost Variance Investigations Models", Journal of Accounting Research, Vol. 16, No. 1, Spring 1978, pp. 190–203.

[8] F. Jacobs and K.S. Lorek, "A Note on the Time Series Properties of Control Data in an Accounting Environment", Journal of Accounting Research, Vol. 17, Autumn 1979, pp. 618–621.

[9] F. Jacobs and K.S. Lorek, "Distributional Testing of Data for Manufacturing Processes", Decision Sciences, Vol. 11, 1980, pp. 259–271.

[10] Robert S. Kaplan, "Yesterday's Accounting Underwines Production". Harvard Business Review, July-Aug. 1984, pp. 95-101.

[11] Roger E. Kirk, Experimental Design: Procedures for the Behavioral Sciences, Brooks, 'Cole Publishing, 1958.

[12] J.T. Mackey, "Variance Contamination Due to a Systems Environment", unpublished Ph.D. dissertation, University of Illinois, 1981. Available from University Microfilms, 300 North Zeeb Road, Ann Arbor, MI.

[13] Merton H. Milier, "Debt and Taxes", Journal of Finance, Vol. 32, No. 2, May 1977, pp. 261–275.

[14] Frank Rayburn and Ashley T. Stewart, "An Analysis of Standard Cost in Practice", Cost and Management, Jan.-Feb. 1981, pp. 30-32.

[15] J. Thompson, Organizations in Action, McGraw-Hill, 1967.

[16] Z.S. Zannetos. "Standard Cost as a First Step to Probabilistic Control: A Theoretical Justification, an Extension and Implications", The Accounting Review, Vol. 29, Apr. 1964, pp. 296–304.
