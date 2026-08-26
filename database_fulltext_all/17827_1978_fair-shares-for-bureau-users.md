---
otero_id: 17827
otero_key: "ZEQ3ATDA"
title: "Fair shares for bureau users"
authors: "R. Gilbraith"
year: "1978"
journal: "Information & Management"
doi: "10.1016/0378-7206(78)90033-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fair Shares for Bureau Users

R. Gilbraith

Rank Xerox (UK) Ltd, Bushey WD2 1DN, UK

The problem of allocating the resources of a Data Centre fairly between independent users is one faced by many organizations, but the literature is not rich in documented solutions. In this article the writer describes in non-technical terms the way one Company has solved this problem in a batch, demand-processing environment by enhancing the job-entry sub-system to create and control a number of "logical computers". The number of these assigned to each user is recalculated each month using work forecasts and a simple agreed formula; each user then has a basis for planning his work schedules which cannot be greatly affected by the activities of other users and which cannot be arbitrarily changed by the Data Centre.

The implementation is based on an IBM 158 using VS2 Release 1 and ASF, but the principles are of general applicability.

Keywords: Demand-processing, scheduling, fairness, allocation, priority, utility, remote, batch.

![](/api/attachments/ZEQ3ATDA/fulltext/images/cbc1bebdd42cbf4c0db16489bd029698f342b03c65b136c7c45f27664fa06873.jpg)

Mr. Gilbraith was educated at Manchester University, England, and worked for eight years prior to 1968 as an IBM Systems Engineer. Since then he has built, organized and managed two in-house Data Centres for multi-site organisations using IBM equipment.

## 1. Introduction

Traditionally commercial data processing bureaux negotiate separate contracts with each customer, make independent bi-lateral arrangements at the user, job class or even job level, and no one customer is interested in the service provided to another; the supplier of computer power either meets his commitments to a user or does not—and if he fails, the user always has the option to take his business elsewhere (at least in principle). The internal “bureau” manager has a different relationship with users; each of them is very interested in getting a “fair deal” in relation to the others, particularly when they have no practical alternative open to them. If this concern is not recognised and addressed actively, it can lead to time-consuming and even acrimonious disputes between the bureau manager and his users; such disputes are essentially unproductive and it is worth while devoting some time and resource to avoiding them.

When Rank Xerox set up three internal computer activities in Europe during 1974/5 to serve most of its subsidiary companies and functional divisions this need was not foreseen initially—but within a year, as the workload on each installation built up from the trivial to the considerable, it became very clear.

## 2. The computing environment

The Rank Xerox bureaux were established as demand-driven, batch processing activities; that is, each installation provides its users with a range of functional capabilities (software facilities, packages and aids) and access to raw computing power. How this computing power is used—for what applications, in what mix, in what sequence—is entirely under the control of the user, subject to him observing certain Data Centre standards governing the maximum © North-Holland Publishing Company
Information & Management 1 (1978) 109--112 resources available to each job; all the Data Centre needs to know is which users require service at what times and each user's total requirement each month for each computer resource (processor time, disk packs, tape reels, and so on).

Data Centre operators are not involved in scheduling the work, in changing job priorities or in recovering jobs that fail, they are concerned only with maintaining system availability to all users at all committed times.

The equipment configurations in all three Data Centres are based on IBM 370-158 processors, and all users are supplied with leased telephone lines and remote batch terminals (RBT); from the outset, no jobs were accepted “over the counter” (indeed there is no counter) and user staffs at the RBT locations are responsible for input control, data preparation, job assembly and output control functions. No printing of user output is performed in the Data Centre.

In order to provide users with the ability to control and alter job priorities (and also to meet a number of other requirements that are not directly related to machine scheduling) it was decided to use ASP with the SVS operating system (Single Virtual System-VS2 Release 1; ASP is a job entry sub-system which supports multiple central processors). In its initial implementation, ASP allowed users a variety of job classes and automatically associated each with a pre-setup priority; ASP tries to set jobs up (provide mountable devices and get volumes mounted on them) in advance of assigning processor resources (initiators, main storage and central processor time) to them in order that—as far as possible—initiators are not idle while operators locate and mount volumes. It selects jobs for setup in priority sequence, and thus by adjusting priorities from their RBT consoles user operators can vary the sequence in which their jobs will run (subject to peripheral device and volume availability).

What they could not do in the early days was to ensure that any of their own jobs would run ahead of, or even at the same time as, jobs submitted by other users. In particular, the user who got up early in the morning could submit large numbers of jobs while others slept and effectively monopolize the system for as long as the jobs ran—this situation was clearly unacceptable, particularly to the heavy sleepers! The fact that normal working hours were different in different locations—due to local arrangements and to some users being in different European time zones from others—meant that there was a constant bias which worked in favour of some and against others.

It was obvious that a change to ASP was required to ensure that, in any relatively short period, each user could, if he wanted to, get some work processed, and to ensure that over a longer period (the day shift, for example), when in general all users were submitting more work than the system could handle immediately, the resources of the system were allocated in a reasonably fair way between users; the change that was planned and implemented became known as “the window scheduling algorithm”.

## 3. Window scheduling

In concept, the plan was to create a number of “windows” through which jobs could pass into the ASP setup process (these ‘windows’ each represent the possibility of processing one job in a scheduling cycle, the job to be processed at any time being selected from the top of the appropriate user’s logical job queue—see Appendix: ASP Implementation). These windows would be allocated to users (hereafter referred to as National Data Centres or NDCs) in proportion to their total workload forecasts. These forecasts would be made monthly and the windows re-allocated each month; no attempt would be made to take account of users requiring a predominance of prime shift time or users having particularly heavy demands on particular days or weeks—it is Company policy that each NDC will, as far as possible, smooth its demand through each day and each month.

Forecasts would be expressed only in “problem program CPU hours” as measured by SMF (System Measurement Facility: the IBM-supplied means of capturing accounting data for the system), this being the only resource for which demand consistently exceeded supply for several hours each day; it also has the merits of being simple, easy to measure and report on, relatively easy to estimate, and relatively stable for the same job from run to run.

The total number of windows to be assigned would be determined by two potentially conflicting considerations:

1. The greater the number of windows, the longer will be the "cycle" time (the time to pass one job through each window and execute it, and be ready to start again at the first one). It is important that this time be short, particularly for the NDC with only a small number of windows and a lot of small jobs, otherwise such a user will not be able to get its fair share of resources.

2. There should be sufficient windows to allow them to be allocated to NDCs broadly in proportion to workload; if there are eight NDCs and one of them only has 5% of the total workload, it is clearly unfair to allocate it one window out of a total of eight—the more windows there are to allocate, the more accurately will the allocation reflect the workload proportions.

With these concerns in mind, the total number of windows was set at about twice the number of NDCs, this being felt to be the most appropriate compromise. A Data Centre serving eight NDCs would thus allocate about sixteen windows (the precise number varying from month to month as the result of a formula given below); with an average job elapsed time of about eight minutes and with six batch initiators being used (that is, the capability for six concurrently executing jobs) this leads to an average cycle time of about twenty minutes—so that a small NDC with only one window can still expect three jobs per hour when the system is at its busiest.

## 4. Window allocation

In deciding how to calculate the window allocation for each NDC it was felt necessary to build in provision to penalise the bad forecaster--and the inveterate cheat! A simple way of doing this is to adjust each forecast by a factor derived from last month's forecast and actual usage:

Next month's forecast $\times \frac{\text{Last month's actual}}{\text{Last month's forecast}}$ .

The process then becomes:

1. Calculate the adjustment factor for each NDC.

2. Multiply it by next month's forecast.

3. Sum the total adjusted forecasts.

4. Divide each adjusted forecast by the sum and multiply by 13.

5. Round the result up or down to give the allocation of windows for each NDC (obviously no NDC can be allocated less than one window so that any result less than 1 must be rounded up—the multiplier in Step 4 is taken as 13 rather than 16 to compensate for this and still give a total of windows allocated that is not consistently greater than 16).

In practise, this calculation process was found to give rise to two unforeseen consequences, and has since been modified to minimise the impact of these. The first was that some NDCs' forecasting was so bad that their adjustment factors were sometimes coming out as low as 0.5 or as high as 3.0—with the result either that they were allocated too few windows to allow their work to be processed, or so many that they obtained an unfairly high level of service (for one month); this problem was solved by restricting the adjustment factor to the range 0.75 to 1.25.

The second undesirable consequence was that some NDCs were being allocated one window one month, two the next, and one again the next as their proportion of work gave a calculated window allocation which oscillated around 1.5 (the conventional rounding point); particularly when an NDC had had two windows for several months and then found they were only entitled to one, this caused considerable difficulty for them in meeting their user schedules (which had been agreed on the basis of past experience with two windows). Although this was seen as essentially a problem that each NDC should guard against (by committing to less exacting schedules with its users) the formula was adjusted to minimise the impact of it by making the change of allocation take effect at a lower adjusted workload level—the conventional rounding rules (round up at 1.5, 2.5, 3.5 and so on) were replaced by rounding up at 1.2, 2.4, 3.5, 4.5, and so on; this seems to have been a worthwhile change, for the NDCs are satisfied with it.

## 5. Conclusion

The foregoing paragraphs have presented an overview of the “fair shares” problem in an in-house computer activity and how it has been solved by one organization. A number of aspects have necessarily had to be omitted (for example, the provision of a separate facility for handling small non-setup jobs which bypasses the window algorithm) and the treatment has been deliberately non-technical. The implementation of the scheme described cast about three man months of systems programming time and has been successful in eliminating earlier feelings of "unfairness" among users of the utilities.

The key points in planning and using an approach of this kind haven been found to be:

1. The concept and detailed logic were discussed with and agreed by all users before the project was implemented.

2. The arithmetic involved in allocating windows is very simple, entirely non-judgemental and completely visible to all users (each month a simple table showing exactly how the calculation for next month has been done is circulated to all NDCs).

3. Each user can now plan his schedules on the basis of having at his disposal his own "logical computer", of known capacity and largely guaranteed availability, which he can control absolutely in terms of job execution sequence (assuming that the total mountable resource available is always adequate to meet the total demand—which is a problem that this scheduling scheme does not attempt to address).

4. The implementation method is such that total system throughput is not affected—the overhead involved in the scheduling itself is so small as to be invisible (given that ASP was already in use) and the algorithm ensures that the initiators are kept fed with work even though only one or two users may have jobs in the system.

## Appendix

## ASP implementation

Control of scheduling is achieved by direct control of the actions of the ASP Main Device Scheduler (MDS), commonly known as "Setup". To make the control completely effective, all jobs requiring a Main Processor phase are forced to pass through MDS.

Scheduling operates at two levels, the NDC level and the system level. The NDC level scheduling is primary and attempts to share resources fairly between NDCs. The system level is present only to ensure that NDC considerations do not lead—if avoidable—to a severely under-utilised system.

NDC level scheduling is based upon “service control”. In the ASP ‘INIT’ deck the Data Centre specifies “service limits” for each NDC. These reflect the relative workloads of NDCs (the number of ‘windows’ allocated), and largely control the numbers of jobs scheduled for those NDCs. As each job is scheduled, a “service count” is incremented. Normally only those NDCs whose service counts are less than their service limits are eligible to have jobs scheduled.

"Job termination counts" are maintained to reflect how many jobs from each NDC have run and ended on the Main processor. When all NDCs have reached their service limits, a "service period" is considered to be complete. The service count of each NDC is decremented by the number of job terminations which occurred for that NDC in that service period. This makes NDCs eligible again, and a new service period starts with the newly-computed service counts.

At the system level, the scheduler monitors and controls the number of jobs concurrently scheduled. A maximum value, specified in the 'INIT' deck, places an upper limit to this number. A minimum value, also specified in the 'INIT' deck, defines a threshold for the number of concurrently scheduled jobs below which some scheduling constraints are relaxed in the interests of keeping the system supplied with work.
