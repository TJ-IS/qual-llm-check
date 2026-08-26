---
otero_id: 17983
otero_key: "BRAN6G66"
title: "Project Management Systems"
authors: "Norman R. Howes"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90005-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Project Management Systems

Norman R. Howes

Brown & Root, Inc., P.O. Box 3, Houston, TX 7700J, USA

Whenever new products are developed, management must deal with how the development will be managed. Several industries have standardized management practices for development projects. Although all industries experience cost and schedule overruns, those industries with standard management techniques seem to do a better job controlling these overruns than those without.

In the dataprocessing industry, software development has caused dataprocessing management to focus more on coding techniques and system architecture than on how to manage the development. In recent years, "structured programming" and "structured analysis" have received more attention than what techniques software development managers should use to manage. Moreover, these coding techniques and architectural considerations are often advanced as the key to a smooth running, well managed project.

The purpose of this paper is not to minimize the importance of "software engineering" but to contribute to the creation of standard management practices for software development through the documentation of a technique that has been used to manage the development of several large scale management information systems. Furthermore, this technique has been "automated" and the principles contained herein are the basis of that automation.

Keywords: Software Development Management, Work Breakdown Structure, Software Estimating, Budget/Schedule Integration, Performance Evaluation, Productivity Evaluation, Forecasting, Variance Tracking, Multibudgeting, Software Engineering

## 1. Introduction

Since 1977, we have been developing a Project Management System to support worldwide operations. It is designed to assist project managers and heir teams in the day to day management of large engineering and construction jobs. Over one million manhours have been expended in the development of this system and it is estimated that another million will be expended before training and installation is complete.

One of the interesting aspects of this effort is that it was managed using the system that was being developed, but in a manual rather than automated mode. This lends credence to the thesis that the design and construction of anything (whether buildings or computer systems) can be managed in the same manner. It is often stated that the development of software cannot be estimated and scheduled with the same precision a contractor estimates and schedules the design and construction of a plant; however, this has not proved to be the case with us.

Some of the techniques employed in this system have been used in the engineering and construction fields for several years and have received adequate treatment in the literature. However, some are unique to the Brown and Root development effort, and to the knowledge of the author, have not been employed elsewhere in the engineering and construction industry, or the data processing field.

![](/api/attachments/BRAN6G66/fulltext/images/ceddf75961ad0508d0dc19ae3e6c18ac3566c9742520395e0e5193d3320217ef.jpg)  
the University of Dallas. He is the author of several papers in mathematics, physics and computer science.

![](/api/attachments/BRAN6G66/fulltext/images/64f8a5f66221b1645b105747cb7e9502c9a2c08c6d7c1f31e41730707f37d136.jpg)

## 2. Getting Started

The fundamental principle behind sound estimating and scheduling is quantification. The basic axiom is: "If you can't quantify it, you can't estimate it." Although producing estimates and schedules has always been a function of management, the mechanics of how this is done are frequently misunderstood. A great deal has been written in recent years about Work Breakdown Structure (WBS). This approach is illustrated by the example in Fig. 1 which shows a typical WBS for the construction of a power plant.

A WBS is a decomposition of a piece of work into its component parts. Moreover, this decomposition is accomplished by a series of subsequent decompositions called “levels”. In this example there are 5 levels. The “boxes” at the lowest level of the WBS are called “control packages”; this is the level at which the work will be controlled. Thus, the control package labeled “concrete” may have been decomposed further into “forms”, “rebar” and “pour concrete.” But, in this example a decision was made not to control the work at such a detailed level, therefore the decomposition stops at “concrete”.

One of the major problems in setting up a WBS is in knowing where to stop: in other words, knowing how to "package the work". There is no mystery if common sense is employed. The following is the author's list of characteristics that control packages should possess:

1. they should consist of one generic type of work with a narrow range of activities,

2. they should be of short duration,

3. they should be logically related to the way the work is to be performed, and

4. it should be possible to assign the responsibility for the completion of any given control package to one person.

It will be noted that developing a WBS is similar to designing a computer system using “top down architecture.” However, it must not be confused with a top down architecture, for in a WBS it is the work to be done that is being broken out and not the system functions to be designed.

In what follows, BRICS (Brown and Root Integrated Control System) will be used in referring to the project management systems being documented here. Fig. 2 is an overview of the WBS used in the development of BRICS. It shows only a few of the control packages. The control package "finalizeize system flows" can be further decomposed into the following "activities":

1. prepare final batch flowcharts,

2. prepare final on-line flowcharts,

3. prepare batch flow narratives, and

4. prepare on-line flow narratives.

This demonstrates the concept of “work packaging” or “activity packaging” for the purpose of controlling the work. For BRICS, estimates were developed from the activities, whereas budgets were assigned, costs were collected, and progress was monitored at the control package level.

The final step in developing a WBS is to assign "control codes" to each box in the hierarchy. This facilitates record keeping, and the control codes serve a function similar to the account codes of general accounting. For this reason, the list of control codes is often called the project's chart of accounts. To distinguish between control codes that correspond to control packages and those that correspond to WBS elements (boxes) at a higher level, the latter will be termed "summary level" control codes.

## 3. Quantification

After a WBS is developed for controlling the work, it is possible to "quantify" the scope of the work in each control package. The first step in quantification consists of listing the activities in each control package and their "units of measure." Fig. 3 illustrates the Detailed Estimate Worksheets used for quantifying and estimating the BRICS development project. The units of measure for the "finalizeize system flows" control package were flowcharts for activities 2.2.20.1 and 2.2.20.2 and reports for activities 2.2.20.3 and 2.2.20.4.

![](/api/attachments/BRAN6G66/fulltext/images/4702a32178904097d9bf7262d390c5398a964a9f6a600979ebe423262c7fa852.jpg)

<table><tr><td colspan="7">DETAILED ESTIMATE WORKSHEETPROJECT BRICS PAGE 1 OF 1PREPARED BY CONTROL PACKAGE 2.2.20 DATE 9-19-79</td></tr><tr><td>ACTIVITY</td><td>DESCRIPTION</td><td>UNITS</td><td>QTY</td><td>MHRS</td><td>$</td><td>REF</td></tr><tr><td rowspan="2">2.2.20.1</td><td>Prepare Final Batch</td><td>Charts</td><td>60</td><td>720</td><td></td><td>101</td></tr><tr><td>Flowcharts</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">2.2.20.2</td><td>Prepare Final On-Line</td><td>Charts</td><td>30</td><td>380</td><td></td><td>102</td></tr><tr><td>Flowcharts</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">2.2.20.3</td><td>Prepare Batch Flow</td><td>Reports</td><td>60</td><td>360</td><td></td><td></td></tr><tr><td>Narratives</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">2.2.20.4</td><td>Prepare On-Line Flow</td><td>Reports</td><td>30</td><td>240</td><td></td><td></td></tr><tr><td>Narratives</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total</td><td></td><td></td><td>1680</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 3. Detailed Estimate Worksheet.

The final step in quantification is to assign quantities to each activity (in that activity's unit of measure). How this was done for the "finalize system flows" control package of BRICS is also shown in Fig. 3.

## 4. Estimating and the Budget

In order to estimate the total manhours and cost of a project, one must make an estimate for each activity in each control package. Since each activity has already been quantified, this is now straightforward. As an example, it can be seen from Fig. 3 that the estimate for control package 2.2.20 (finalize system flows) is 1,680 manhours. This is achieved by summing the manhours for each activity in the control package.

The last column on the right of the estimating worksheet titled "REF" is for references to estimating assumptions. For example, reference 101 might read as follows:

This estimate is based on the assumption that the level 2 system flowchart will not require more than 80 manhours of rework after the reviews conducted at the end of the functional design phase.

It is not necessary to document all estimating assumptions. The fact that 720 manhours were estimated to complete the 60 flowcharts of activity 2.2.20.1 records an “implicit” estimating assumption that the flowcharts take 12 manhours each to complete.

Sound estimates are based on experience. When an estimate is based on experience gained from executing a similar task, no documentation of assumptions is necessary. Only when factors exist that cause the activity to be unlike those within our range of experience does the documentation of an assumption need to be made. In this case, a rational assumption is made that takes the uncertainty out of existing factors and allows us to bring the activity to be estimated within our realm of experience. At a later stage, it may be found that this assumption is not valid, and a “variance” to the original estimate may need to be added.

Once estimates have been completed for each control package and approved by project management, the sum of these estimates is called the "original budget." The approved estimate for a given control package is called the original budget for that package. It is also meaningful to talk about budgets for any WBS element at any level.

All the WBS elements at a given level that are connected to a particular WBS element at the next higher level are said to "roll up" into this particular WBS element. This particular WBS element may, in turn, roll up into yet another higher level element. Thus the original budget for a given WBS element is simply the sum of all the original budgets for control packages that summarize (roll up) into it.

Knowing the budget is essential in managing a project, but the comparison of expenditures and progress with the budget is even more important. This requires a way to measure how efficiently the work is being performed so corrective action can be taken while there is time, if the work is not progressing as planned.

## 5. Time Phasing the Budget

“Time Phasing” shows graphically how the budget is to be expended over time. Fig. 4 shows the time phasing of the technical design and implementation portion of the BRICS budget. From this it can be seen that the technical design and implementation of BRICS was planned to span a period of 20 months and to consume over 250,000 manhours.

Time phasing is first estimated at the control package level and then rolled up to obtain time phasing at higher levels. This roll up is, however, more complex than for the budget, and it is helpful to have a compute produce the time phasing.

In order to time phase an individual control package, one must first know when the work is to begin and end. This information is obtained from the project schedule. Scheduling techniques range from very simple manually prepared barcharts to PERT charts, CPM calculations and arrow diagramming networks. For the purposes of this paper, we assume some form of schedule exists that gives the “start and end dates” of each control package. An example of the BRICS schedule for technical design is given in Fig. 5.

It is important to recognize the purpose of scheduling. Just as a budget is not project management, neither is a schedule. It gives dates but not insight into the success of a project. A common misconception is that scheduling is managing; but it is just a tool to aid in project management endeavors. The essence of managing a project is in understanding the interrelationship between budget and schedule and in using a method of measuring performance against this interrelationship. This interrelationship is the time phased budget. It is also referred to as the “project plan” or the “base-line”. When used this way, one really means that it is a concise representation of the project plan.

The appropriate level at which the schedule is to be prepared is either the activity level or the control package level, depending on the size of the project and whether the schedule is automated or not. Scheduling at a level lower than this tends to create far too many elements which cause the schedule to become unwieldy and often incomprehensible. Scheduling at a higher level limits time phasing roll up options and may not relate to the level at which the work is being controlled. Proper subdivision of the work should lead to a WBS with no more than 500 control packages and a schedule with no more than 2,000 activities.

If the schedule has been so prepared, the start and end dates for each control package are easily derived from it. If the schedule consists of activities, the start date for a control package is the earliest start date of all activities contained in the control package. End dates are similarly derived. Clearly the start and end dates correspond to when the control package's budget expenditure is planned to begin and end.

The next step is to determine the planned pattern of expenditure of the budget over the time period between start and end dates for each control package. These patterns of expenditure will be called “spread curves”. There are several methods available: perhaps the simplest is to assume the budget for each activity will be expended in one lump at the time of completion. An example of this “step function” spread curve is given in Fig. 6(a).

Another way is to use a simple linear approximation to the step function spread curve as shown in Fig. 6(b). If the schedule has been prepared at the control package level, the linear approximation spread curve reduces to a straight line that corresponds to a constant rate of expenditure during the life of the control package. Such a straight line spread curve is usually adequate for most control packages.

The reason for this is that if the work has been properly subdivided, the majority of control packages will have budgets of the same order of magnitude, and their durations (period between start and end dates) will be short: usually spanning no more than a couple of reporting periods. In this case, if there are 500 control packages, the "typical" control package will have a budget that represents only two tenths of one percent of the total budget. Consequently, no matter what the shape of the spread curve (as will presently be seen), it is unlikely to have a noticeable effect on the time phasing of the total budget.

BROWN & ROOT, INC. - BRICS DEVELOPMENT
TECHNICAL DESIGN / IMPLEMENTATION
PROJECT STATUS SUMMARY  
![](/api/attachments/BRAN6G66/fulltext/images/5bf94b028007270b2cf21aa9df024a5fa7162f8b155b498d69fc0dd7485493e4.jpg)

<table><tr><td rowspan="2">BUDGET</td><td>MHRS PER PERIOD</td><td>10</td><td>10</td><td>10</td><td>10</td><td>14</td><td>15</td><td>14</td><td>16</td><td>21</td><td>23</td><td>20</td><td>15</td><td>15</td><td>14</td><td>11</td><td>8</td><td>8</td><td>8</td><td>5</td><td>5</td></tr><tr><td>ACCUMULATED MHRS</td><td>10</td><td>20</td><td>30</td><td>40</td><td>53</td><td>69</td><td>83</td><td>99</td><td>120</td><td>143</td><td>163</td><td>178</td><td>193</td><td>207</td><td>218</td><td>226</td><td>233</td><td>241</td><td>248</td><td>251</td></tr><tr><td rowspan="2">EARNED</td><td>MHRS PER PERIOD</td><td>6</td><td>5</td><td>5</td><td>16</td><td>15</td><td>15</td><td>6</td><td>16</td><td>20</td><td>20</td><td>33</td><td>12</td><td>13</td><td>16</td><td>11</td><td>10</td><td></td><td></td><td></td><td></td></tr><tr><td>ACCUMULATED MHRS</td><td>8</td><td>13</td><td>18</td><td>34</td><td>50</td><td>65</td><td>72</td><td>88</td><td>108</td><td>128</td><td>181</td><td>172</td><td>186</td><td>202</td><td>213</td><td>223</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">ACTUAL</td><td>MHRS PER PERIOD</td><td>9</td><td>6</td><td>6</td><td>18</td><td>11</td><td>9</td><td>18</td><td>18</td><td>18</td><td>23</td><td>21</td><td>18</td><td>17</td><td>16</td><td>10</td><td>7</td><td></td><td></td><td></td><td></td></tr><tr><td>ACCUMULATED MHRS</td><td>9</td><td>15</td><td>21</td><td>38</td><td>48</td><td>58</td><td>75</td><td>93</td><td>110</td><td>133</td><td>154</td><td>173</td><td>189</td><td>206</td><td>216</td><td>223</td><td></td><td></td><td></td><td></td></tr></table>

Fig. 4. Earned Value Plotted Against Baseline.

BRICS PROJECT SCHEDULE
TECHNICAL DESIGN PHASE  
![](/api/attachments/BRAN6G66/fulltext/images/f85cef3ff766af31d9c34c51915c8ebb3fd64258f0beef2577a2bffd082623f2.jpg)  
Fig. 5 Project Schedule for Technical Design Phase.

However, in the case that a single control package has a substantially larger budget than the average and is not of short duration (such as an overhead control package) the “spreading” may need to be handled in a more sophisticated manner. Instead of developing the spread curve from the estimate for each activity and its relative position in the schedule the spread curve can be based on historical information or schedule resource loading information. In either case, the appropriate spread curve is fit between the start and end dates such as in the example given in Fig. 6(c).

After the budget for each control package has been spread, it is possible to produce time phased budgets for any WBS element at any level. This is illustrated in Fig. 7, where a time phased budget at a summary level WBS element is obtained by first adding up all budgets that roll up into the summary level element, then by determining the start and end dates of the summary level element as the earliest start date and latest finish date of all its control packages and finally by summing the budget contribution of each control package during each time period in the summary level element's duration.

## 6. Performance Evaluation

Performance evaluation is the comparison of actual progress and expenditures against the project plan, or baseline. A convenient measure of actual progress is “earned value”. Earned value for a control package or activity is defined as the “percent complete” multiplied by the budget for the control package or activity. Earned value at a summary level WBS element is obtained by summing the earned value of each control package that rolls up into the summary level element.

TIME PHASING OF CONTROL PACKAGE 2.2.20
(FINALIZE SYSTEM FLOWS)  
![](/api/attachments/BRAN6G66/fulltext/images/a31941e2fa490eb16a210e74be2aa5560c5f2cd9bb3d93d5ea87385707672989.jpg)  
Fig. 6. Various Spread Curve Examples.

There are several methods for calculating percent complete for a control package. The only one discussed here is the “quantities” method. If, in the example of Fig. 3, 60 batch flowcharts are required to complete activity 2.2.20.1 and 45 flowcharts are finished, activity 2.2.20.1 is considered to be 75% complete. Since the budget for activity 2.2.20.1 is 720 manhours, the earned value (earned manhours) for this activity is 540 manhours. The earned value for the control package is obtained by summing the earned value for each activity in the package.

![](/api/attachments/BRAN6G66/fulltext/images/100ca5c807cc6aae3ea40df53c1e5b7c92335a56ef3397f289043760a25eac76.jpg)

![](/api/attachments/BRAN6G66/fulltext/images/b543f5ebf96e5fc85635178c9e3d394516c62ca1d7448bf004317dbb64a05bfc.jpg)

![](/api/attachments/BRAN6G66/fulltext/images/e130b2e7061d39b61f61b5bd041b756b2f4c6ca8d426f62ebe16119817033c31.jpg)

![](/api/attachments/BRAN6G66/fulltext/images/52025743f666e10ba8b19be10eacff8ed0a22d2df3a001a7914d61b64960981b.jpg)  
Time Phasing for a Summary Level WBS Element.

Classical cost accounting methods are applied in collecting actual expenditures on a project. Each control package is considered as a ledger account and each cost incurred for each control package is posted to the appropriate account as it is paid. Manhour expenditures should be posted weekly, even when costs are being posted monthly. For plotting purposes it is advisable to maintain a historical record of the actual cost for each control package at the end of each reporting period.

Collection of costs at the control package level allows computing the actual expenditure at any summary level WBS element by summing. A plot of earned value and actual expenditures against the base-line for the technical design and implementation of BRICS was given in Fig. 4.

## 7. Project Management

Suppose that for some project, the three curves shown in Fig. 8 are calculated at the end of some reporting period denoted by t, with the budget curve labeled B, the actual expenditure curve labeled A and the earned value curve labeled E. Here, the “actual” curve is “leading” the budget curve and the “earned” curve is “trailing” the budget curve (i.e., actual expenditures are being incurred at a faster rate than planned and progress is less than planned).

When a project is not progressing as planned, the question is: "How far behind schedule is it?" This can be answered by comparison of the earned and budget curves. At time $t$ , $B(t)$ represents how much value should have been earned at item $t$ . Drawing a horizontal line through $B(t)$ and extending the earned curve $E$ until it intersects this horizontal line yields a point $X$ and a corresponding time $t_x$ at which $B(t)$ value will be earned (if progress continues at its present rate). It will then take until $t_{x}$ to earn as much value as should have been earned at time t and the deviation in schedule (denoted $\Delta S$ ) is $t_{x} - t$ .

Another question is: "How much over (under) budget is the project?" The overrun (underrun, at item $t$ is $A(t) - E(t)$ ). But since $B(t)$ worth of value will not be earned until $t_x$ , the budget overrun at that time is shown as $\Delta B$ in Fig. 8.

These curves can also be used for elementary forecasting. Fig. 9 depicts a set of curves for some hypothetical project at a given time t. First, the earned value curve E is extended until it intersects the horizontal line that depicts 100% of originally planned expenditure at the point X. Corresponding to the point X is a time $t_{x}$ . The originally planned time to finish is $t_{f}$ . The schedule deviation at project completion is then $\Delta S = t_{x} - t_{f}$ . The budget deviation at project completion, denoted by $\Delta B$ , is then found by projecting the actual expenditure curve A until it intersects the vertical line drawn through $t_{x}$ at point Y. The difference between Y and X measured along this vertical line then represents the budget deviation; i.e., $\Delta B = Y - X$ .

The information obtainable from these curves lends itself well to the so called “management by exception” philosophy. If the actual and earned curves are “tracking” the base-line (budget curve) closely enough, the indication is that the project is progressing as planned. However, if there are significant deviations, corrective action needs to be taken.

To determine where corrective action is needed, one analyzes the three curves at lower summary level WBS elements. Those summary level elements where the earned and actual curves are tracking the base-line closely are considered to be progressing as planned, whereas those with significant deviation are considered as candidates for closer analysis. Management can continue this process until the problem control packages are identified.

In analyzing problem areas, management frequently is interested in the cost per unit to accomplish the various control packages. During quantification, the unit of measure was determined for each activity in the control package. At this time, one of these units of measure is selected as the "key" unit of measure for the control package. In the case of control package 2.2.20 of Fig. 3, the key unit of measure would be flowcharts. It is always possible to select such a key unit of measure; this follows from characteristics 1 and 3 of how the work should be packaged.

![](/api/attachments/BRAN6G66/fulltext/images/eb7a988ecbd0c4b4f61fee82d72628ade125efbcc41cb4c72cc27659744b3acb.jpg)  
Fig. 8. Budget and Schedule Deviations.

![](/api/attachments/BRAN6G66/fulltext/images/1d0c9b9bc4526ff31a2bb0c1b49996aae6eb014e84219bb4f191cf70eeb113ce.jpg)  
elementary Forecasting.

The quantity for a control package is the sum of the quantities for activities in the package with the same unit of measure as the key unit of measure. The budget divided by this quantity represents a “budgeted cost/unit” for the control package. The actual costs (manhours) divided by the units currently installed represents an “actual cost/unit.” If the actual cost per unit is lower than the budgeted cost per unit, the “productivity” is better than planned.

This measure of productivity is valuable to project management and a weekly report comparing actual productivity (cost, unit) with planned productivity should be available. Clearly, the concept of key unit of measure will often be meaningful at summary level WBS elements. When this is the case, productivity information can also be reported at summary levels.

Once problem control packages have been identified, corrective action can be taken. This usually involves extracting higher productivity from those executing the control packages or redeploying resources. Normally, the visibility given work that is not progressing as planned by this performance measurement method tends to stimulate productivity. However, there are cases when work is not progressing as planned but productivity is not the problem. These cases need to be recognized and handled differently. There are three reasons why work does not progress as planned:

1) changes in the scope of the work,

2) quantity deviations, and

3) productivity deviations.

Changes in the scope of the work are redefinitions of the original requirements. They can be introduced by a client, management or those executing the work. Their basis can range from a change in policy or operating philosophy to the discovery of a better design alternative.

Quantity deviations arise from errors in the quantification process. Productivity deviations arise from not accomplishing the work at the planned unit rate (cost/unit). This may be due to poor management, lack of cooperation among team members, inaccurate unit rate estimates, or unforeseen external forces. In order to insure against poor unit rate estimates, it is desirable to have these estimates made by those responsible for performing the work: they should then represent a commitment to complete the work at the cost per unit agreed upon.

The reason for carefully distinguishing among the causes for deviations from the plan is twofold. First, management cannot compensate for the first two and must understand this. If work is not progressing as planned because of low productivity, then pressure can be applied to increase it. But applying pressure when productivity meets or exceeds the plan may be counter-productive. Workers need to be rewarded for exceeding planned productivity estimates even though the actual expenditure far exceeds the budget because of poor quantification or changes in the scope of work.

## 8. Variances and Multibudgeting

The second reason for distinguishing among causes for deviations is to “keep the base-line current.” This means providing for an up-to-date account of the scope of work and an audit trail of how the original base-line “evolved” into the current base-line. If the base-line is not kept current, the percent complete and earned value calculations will not be correct.

A “Variance” will denote the documentation of a deviation from the plan. A “change order” is a variance that represents an agreed upon change in scope of work. If the work is being done for a client, a change order will be a client approved variance and will result in a change to the contract. Then the original contract plus all change orders represent the current contractual environment under which the work is being performed.

Variances other than change orders will be designated as quantity or productivity variances depending upon whether they arose as the result of a (current or projected) quantity or productivity deviation. Sometimes an observed deviation will have both a quantity and productivity component. It is important that the distinction be made and a separate variance be used to document each component. This is because quantity variances will be used to update the base-line whereas productivity variances will only be for updating the forecast, as will be explained later in this section.

In practice it is impractical to keep track of every quantity and productivity variance. Significant variances need to be assigned a variance number and classified as a change order, quantity variance, or productivity variance. No variance should be of more than one type (e.g., both a quantity variance and a productivity variance). The variances for a project need to be retained and each variance needs to have line items that correspond to control packages.

A change in the scope of work may effect more than one control package; it may even necessitate adding new control packages. When a variance effects more than one control package there needs to be a line item within the description of the variance for each control package. In all cases, the variance should record new units of measure, quantification, or unit rates, as appropriate.

Each variance line item needs to be cross referenced to the control package to which it applies. It is assumed here that project management maintains a control package file that contains the budget, cost, and status information for each control package. If the project management information is to be maintained manually, it is useful to keep a Control Package Notebook and a Variance Notebook. The Control Package Notebook should be indexed by control package and the Variance Notebook by variance number. The cross referencing should consist of having a copy of each variance line item that corresponds to a given control package filed in that particular section of the Control Package Notebook that corresponds to this control package.

The original budget for a control package together with all the change orders is the “control budget.” The control budget plus all the quantity variances is the “target budget.” The sum of the target budget and all the productivity variances is the “forecast.”

The schedule was used to time phase the original budget. As changes occur and variances are recorded, the schedule needs to be changed accordingly. A new schedule based upon the scope of work as currently understood needs to be maintained to time phase the target budget. Other schedules can be maintained for forecasting purposes but the schedule used for time phasing the target budget should only contain activities related to control packages in the target budget.

It is now possible to generate the three curves for tracking against the target budget. Earned value is always calculated using the target budget. Plotting earned and actuals against this budget shows how the work is progressing against the real scope of work. This is the proper measure of the effectiveness of the application of the work force to the work as the work force cannot compensate for the deviations caused by change orders and quantification errors. This is the plot that project management uses to control the project.

A comparison of the budgets and the forecast for a hypothetical project is given in Fig. 10. Comparing the control to the original budget summarizes the impact of all change orders. Comparing the target to the control budget is a measure of how well the project was quantified. Poor productivity will show up in the comparison of the forecast to the target budget but this comparison is not a direct measure of the effectiveness of project execution if the project is effected by outside forces beyond its control.

It is impractical to attempt tracking every single variance. In practice, one relies on the “Law of Compensating Error” to balance out small or insignificant variances and concentrates on tracking the significant ones. All scope changes are considered significant and should be tracked. The conditions (possibly contractual) under which the work is performed wall dictate who “pays” for the change in scope. But regardless of who pays, if the original scope changes, the budget (quantities, manhours, and monies) must be adjusted to reflect the new scope. Otherwise, earned value computations will be inaccurate.

There are special cases where all quantity variances should be tracked. The “unit price” contract (on a cost per unit basis) allows the client the option of purchasing additional “units” at a fixed

FORECAST

![](/api/attachments/BRAN6G66/fulltext/images/69e0bea442e0ee780fa7575241df301515ad540941487ba143c43ca9c5643131.jpg)  
Fig. 10. Budget and Forecast Comparisons.

rate for a fixed period of time. In such a situation, all quantity variances will be paid by the client (they eventually become change orders).

Most of the time, only the significant quantity and productivity variances are tracked. Which variances are significant needs to be determined by project management. Normally this determination is based on some preset percentage of the budget for the control packages involved and the total project budget. It is more important to be complete with quantity variances than productivity variances, as they effect the target budget.

Unless the target budget is fairly accurate, project management does not have a good base-line to judge how well the work is being executed, but if some of the productivity variances are omitted, the effect is only on the forecast (which may or may not be important). Furthermore, there are limitations to the forecast accuracy and in some instances other forecasting methods might be employed.

development. Schedule deviations of only a few days have been realized on all phases of system development and testing. However, it is important that software managers be completely familiar with the method prior to using it on a project. To attempt to convert an unstructured project to a formal management method such as this in "midstream" may prove to be more than bargained for.

Those interested in additional reading related to software development techniques may find the following references [1] and [2] helpful. [1] deals with developing Requirement Specifications and the so-called "Top Down" software development methodology. The principles included therein formed the basis for the Work Breakdown Structure shown in Fig. 2. [2] deals with a variety of problems encountered during software development and a number of opinions and suggestions on how to deal with them.

## 9. Conclusion

We have found this method of project management to be extremely well suited for software

## References

[1] N.R. Howes, Development of Effective Command and Control Systems, Signal Magazine (Journal of the Armed Forces Communications and Electronics Association) February (1977) 44–48.

## 258 Techniques

[2] J.I. Schwartz, Construction of Software, Problems and Practicalities, in: Practical Strategies for Developing Large Software Systems (a compilation of papers from the 1974

USC Seminar entitled: Modern Techniques for the Design and Construction of Reliable Software (Addison - Wesley 1975) 15-54.
