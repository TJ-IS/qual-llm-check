---
otero_id: 18920
otero_key: "YZJZ5ZTE"
title: "A multinomial project evaluation and review technique for information systems analysis and design"
authors: "Douglas G. Bonett; Richard F. Deckro"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90025-o"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Techniques

# A multinomial project evaluation and review technique for information systems analysis and design

Douglas G. Bonett

University of Wyoming, Laramie, WY, USA

Richard F. Deckro

Portland State University, Portland, OR, USA

PERT is an important tool for the management of information systems design and analysis projects. In applications where the activity completion times are uncertain, the classic PERT approach is based on the assumption that each activity time follows a Beta distribution. In addition, the composite project duration is assumed to follow a normal distribution. Such assumptions are unrealistic in many information system projects. A new approach to project review and evaluation is proposed, based on a multinomial distribution for activity times. This new approach leads to an exact discrete distribution of the project duration. The results are illustrated in an information systems and design example.

Keywords: Beta distribution; CPM; Systems analysis and design; Multinomial distribution; PERT; Project management

![](/api/attachments/YZJZ5ZTE/fulltext/images/1621b5c95c7374471cf84f10a3975968e294fcb87bc1b189d8c878b23f5a91af.jpg)  
Douglas G. Bonett is the Senior Research Professor in the College of Business at the University of Wyoming and an Adjunct Professor of Statistics. Dr. Bonett received his Ph.D. from UCLA in 1983. His research interests include discrete data analysis methods and statistical modeling. He teaches courses in information systems, operations management, and statistics.  
Correspondence to: D.G. Bonett, Department of Management and Marketing, College of Business, University of Wyoming, Laramie, WY 82071, USA.

## 1. Introduction

The analysis and design of an information system may be described as involving several different aggregate phases. For instance, Whitten, Bentley, and Barlow [7] discuss the following phases: survey, study, definition, selection, design, acquisition, construction, delivery, and maintenance. We may view these as a hierarchical aggregate plan which identifies specific tasks required to complete the project. Two key questions that must be answered in any systems analysis and design project focus on: (1) the expected project completion date, and (2) the potential variability in the completion date.

PERT (Project Evaluation and Review Technique) is an important and widely used analysis approach in systems analysis and design projects $[6]$ . To determine the total project time (and hence the project completion date), as well as the variability in total project time, expected time estimates for each activity duration are required. The critical path activities, subject to their index of criticality, dictate expected project completion time and variability.

In most information systems analysis and design applications, activity times will not be known

![](/api/attachments/YZJZ5ZTE/fulltext/images/0e5f0eb5c791ce253c2a8db6bc92e6670844c35e3516645d8a70bba50155a65b.jpg)  
Engineering Management, as well as being an active member of other professional societies.

Richard F. Deckro is a Professor of Engineering Management at Portland State University. Dr. Deckro holds a B.S.I.E from SUNNY Buffalo, an MBA and a DBA in Decision Sciences, both from Kent State University. His research interests are in the areas of project management, applied mathematical programming, advanced manufacturing methods, and multi-criteria decision making. Dr. Deckro is the current Chairperson of the TIMS College on Technology and with certainty. It is common practice to specify three parameters for each activity: (1) the optimistic time, (2) the most probable time, and (3) the pessimistic time. Based on the classic assumption that each activity time follows a Beta distribution [4], the mean and variance for each activity may be estimated using well known approximation formulas. The sum of the estimated means for each activity on the critical path gives an estimate of the expected project duration. Under the assumption that activity times are independent, the variance of project duration is defined as the sum of the variances for each activity on the critical path. Appealing to the Central Limit Theorem, project duration is assumed to be approximately normal with variance equal to the sum of the individual activity variances on the critical path.

There are two major problems with the application of PERT in systems analysis and design projects. First, the distribution of completion times for a given activity will not exactly follow a Beta distribution. Consequently, the estimated means and variance for each activity will be inaccurate. Second, the application of the Central Limit Theorem is questionable when the number of activities on the critical path is not large. With a small number of critical path activities (a common situation with hierarchical levels), the estimated project duration will not necessary follow a normal distribution with the specified variance. Since many information system analysis and design projects are quite costly, accurate estimates of project duration and variance are crucial to managerial decision making. The weakness of the Beta assumption has been discussed in detail in the project management literature $[3, 5$ among others].

In this paper, we propose an alternative time estimation technique based on a multinomial distribution of each activity time. The exact probability distribution of the project duration may then be derived. This alternative methodology will be referred to as Multinomial PERT (M-PERT).

## 2. The Multinomial PERT

In many information system and design applications, it may be possible to specify a small number of discrete completion times for each activity. For instance, a systems analyst might believe that the survey phase will be completed in either two, three, or four months. Based on data from previously completed projects of a similar nature, combined with information obtained from experts, probabilities may be assigned to each of the discrete completion times. This estimation procedure may be repeated for each activity in much the same manner as classic PERT estimates are obtained.

Let $\pi_{ij}$ represent the probability of completing task i in time category j. Let $t_{ij}$ represent the duration of task i in category j. The $t_{ij}$ value is expressed in the same metric (e.g., weeks, months) for all tasks. Under the multinomial assumption, the mean expected completion time for task i is defined as

$$
\mu_ {i} = \sum_ {j} \left[ \pi_ {i j} t _ {i j} \right],\tag{1}
$$

where the summation is over the discrete time categories for a given task i. Mean completion times are computed for each activity and these means (rather than the means computed under an assumption of a Beta distribution) are used to determine the critical path as in the classic PERT. Recall that the critical path is the longest one (i.e., the one predicted as taking the most time) from the initial node to the terminal node; it therefore determines the minimum expected project duration. If any activity on the critical path is delayed, completion of the entire project is delayed.

Let s denote the number of activities on the critical path. It is known that the joint distribution of s independent multinomial random variables is also a multinomial random variable [1]. The joint multinomial random variable will have $v = k_{1} \times k_{2} \ldots k_{s}$ categories where $k_{i}$ is the number of time-duration categories for task i. Given the assumption of independent activities (i.e., the same as the Beta based PERT), the probabilities associated with each of the v categories are defined as the product of the appropriate marginal probabilities. Each of the v categories will correspond to a possible project duration value, denoted as $t_{n}$ , defined as the sum of $t_{ij}$ marginal values that correspond to that category. Note that the $t_{n}$ values will not necessarily be unique and the probability associated with each $t_{n}$ value will be the sum of all cell probabilities across cells having a particular $t_{n}$ value. Let $\pi_{n}$ denote the probability of each $t_{n}$ value.

Table 1

<table><tr><td>Project duration</td><td>Probability</td><td>Cumulative probability</td></tr><tr><td> $t_1$ </td><td> $\pi_1$ </td><td> $\pi_1$ </td></tr><tr><td> $t_2$ </td><td> $\pi_2$ </td><td> $\pi_1 + \pi_2$ </td></tr><tr><td> $t_3$ </td><td> $\pi_3$ </td><td> $\pi_1 + \pi_2 + \pi_3$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td> $t_n$ </td><td> $\pi_n$ </td><td>1.0</td></tr></table>

The project duration distribution will be discrete and is conveniently represented in tabular form as shown in Table 1. Let $\pi_{i}$ denote the probability associated with a given value of the project duration $t_{i}$ . The estimated mean project duration may then be defined as:

$$
\mu = \sum_ {i} \left[ t _ {i} \pi_ {i} \right],\tag{2}
$$

and the estimated variance of the project duration is defined as:

$$
\sigma = \sum_ {i} \left[ \left(t _ {i} - \mu\right) ^ {2} \pi_ {i} \right],\tag{3}
$$

where the summation is over all possible project duration values.

In some applications the systems analyst will want to determine the probability of completing the project on or before a specified duration. This is a common analysis in classic PERT. With M-PERT, the probability of completing the project on or before a specified duration is obtained directly from the cumulative probabilities.

## 3. Example

Consider the software development component of an information systems project presented by Jordon and Machesky [2]. Each task and its immediate predecessors are listed in Table 2. A activity on arc diagram of the project is presented in Figure 1. The tasks and predecessors for this example typify most software development projects. Possible completion times for each activity and the probabilities of each time value are presented in Table 3: the estimated mean completion time for each activity is computed using equation (1) and listed in the last column. From the Beta based PERT approach, Jordon and Machesky found that there are four activities on the critical path. These arc: (a) program specification, (b) program coding, (c) program testing, and (d) applications testing.

Table 2  
Tasks and predecessors for a software development project.

<table><tr><td>Task description</td><td>Immediate predecessor</td></tr><tr><td>a. Program specifications</td><td></td></tr><tr><td>b. Program coding</td><td>a</td></tr><tr><td>c. Program testing</td><td>b</td></tr><tr><td>d. Application testing</td><td>a, g, k, n</td></tr><tr><td>e. Equipment specification</td><td></td></tr><tr><td>f. Vendor selection</td><td>e</td></tr><tr><td>g. Equipment installation and testing</td><td>f</td></tr><tr><td>h. Data files specification</td><td></td></tr><tr><td>i. Test files created</td><td>a, e, h</td></tr><tr><td>j. File conversion</td><td></td></tr><tr><td>k. Production files testing</td><td>j</td></tr><tr><td>l. Work procedures specifications</td><td></td></tr><tr><td>m. Training specifications</td><td>k</td></tr><tr><td>n. Pre-installation training</td><td>e</td></tr></table>

The discrete probability distribution from the M-PERT is presented in Table 4. The expected project duration is 7.1 months using M-PERT. For the purpose of discussion, we have assumed that the project manager would round the project duration to seven months. The estimated variance is 1.21. The probability of completing the project in six or less months is 0.304.

It is interesting to compare the M-PERT results with classic PERT results. To do this, we set the optimistic time equal to the shortest activity time, the pessimistic time equal to the longest activity time, the most likely time equal to the time with the highest probability for each activity (or the average across activity times having the same probabilities). For instance, for task g we set the optimistic value to 0.5, the pessimistic value to 1.5, and the most likely value to 1. The estimated project duration using the Beta based PERT is then 7.83, or rounded to eight months. The estimated variance for this time estimate is 0.194. The estimated probability of completing the project in six or less months is less than 0.001 under the assumptions of the Beta based PERT.

![](/api/attachments/YZJZ5ZTE/fulltext/images/8034f3c2a440828ebeeb9132c1bae1b37aebfc6500f524850f69915a227b91e3.jpg)  
Fig. 1. Activity on arc diagram for design and analysis project.

Table 3  
M-PERT estimated activity times and probabilities for each task.

<table><tr><td>Expected task</td><td colspan="4">Completion times (months)</td><td>Duration</td></tr><tr><td>a</td><td>1 (0.8)</td><td>2 (0.2)</td><td></td><td></td><td>1.2</td></tr><tr><td>b</td><td>2 (0.1)</td><td>3 (0.7)</td><td>4 (0.2)</td><td></td><td>2.8</td></tr><tr><td>c</td><td>1 (0.5)</td><td>2 (0.5)</td><td></td><td></td><td>1.5</td></tr><tr><td>d</td><td>1 (0.4)</td><td>2 (0.6)</td><td></td><td></td><td>1.6</td></tr><tr><td>e</td><td>1 (0.8)</td><td>2 (0.2)</td><td></td><td></td><td>1.2</td></tr><tr><td>f</td><td>0.5 (1.0)</td><td></td><td></td><td></td><td>0.5</td></tr><tr><td>g</td><td>0.5 (0.2)</td><td>1 (0.6)</td><td>1.5 (0.2)</td><td></td><td>1.0</td></tr><tr><td></td><td>1 (0.9)</td><td>2 (0.1)</td><td></td><td></td><td>1.1</td></tr><tr><td>i</td><td>0.5 (0.8)</td><td>1 (0.2)</td><td></td><td></td><td>0.6</td></tr><tr><td>j</td><td>2 (0.1)</td><td>3 (0.4)</td><td>4 (0.3)</td><td>5 (0.1)</td><td>3.1</td></tr><tr><td>k</td><td>1 (0.5)</td><td>2 (0.5)</td><td></td><td></td><td>1.5</td></tr><tr><td>l</td><td>1 (0.2)</td><td>2 (0.4)</td><td>3 (0.3)</td><td>4 (0.1)</td><td>1.7</td></tr><tr><td>m</td><td>1 (0.1)</td><td>2 (0.6)</td><td>3 (0.2)</td><td>4 (0.1)</td><td>2.3</td></tr><tr><td>n</td><td>1 (0.2)</td><td>2 (0.6)</td><td>3 (0.2)</td><td></td><td>2.0</td></tr></table>

Note: Probabilities are in parentheses.

If we assume that the activity times are discrete and the probability estimates are correct, the classic PERT yields an estimate of the project duration that is about one month longer than the M-PERT duration estimate. The classic PERT also gives a variance estimate that is considerably smaller than the M-PERT variability estimate. Furthermore, one would conclude that it is virtually impossible to complete the project in six months or less based on the classic PERT results while the M-PERT results indicate that this probability is 0.304. This result is not surprising, as the M-PERT approach captures the expert's estimates of the likelihood for each activity completion time, while the classic PERT merely forces the time estimates into a specific approximation for the Beta distribution.

Table 4  
Discrete probability distribution from M-PERT.

<table><tr><td>Project duration (months)</td><td>Probability</td><td>Cumulative probability</td></tr><tr><td>5</td><td>0.064</td><td>0.064</td></tr><tr><td>6</td><td>0.240</td><td>0.304</td></tr><tr><td>7</td><td>0.344</td><td>0.648</td></tr><tr><td>8</td><td>0.248</td><td>0.896</td></tr><tr><td>9</td><td>0.092</td><td>0.988</td></tr><tr><td>10</td><td>0.012</td><td>1.000</td></tr></table>

## 4. Conclusion

Classic PERT analysis assumes activity times that are Beta distributed. While the estimates traditionally used for this distribution are convenient, because of its fixed end points and unimodal shape, its use assumes a continuous distribution within the range defined by these endpoints. This condition assumes that any fraction of a time period, be it months, weeks, or days, can accurately be estimated and assigned to a task. In large scale, hierarchical development projects of the type considered here, systems analysts and project managers typically estimate activity times in terms of discrete time units.

Classic PERT also assumes that the Central Limit Theorem can be applied to obtain an estimate of the project duration. This assumption may be justified in projects having a large number of activities on a single critical path. In large scale, hierarchical development projects, the critical path will be short and application of the Central Limit Theorem is difficult to defend.

Our approach addresses these two weaknesses. It allows expert opinion to be utilized by freeing the analyst from the Beta distribution. Aggregate activities are estimated over discrete time ranges, with a statement of the probabilities associated with each activity. Furthermore, the M-PERT approach does not rely on the Central Limit Theorem to obtain an estimate of the project duration.

Our approach provides all of the information that can be obtained from the classic approach. Specifically, estimates of expected project duration and variance, as well as probabilities for specified duration values, may be obtained from the M-PERT. It is simple to apply to small projects.

In a large project with many critical path activities, each having many possible durations, computer assistance is required. The required computations are easily programmed. Even large projects may be analyzed on a personal computer.

The choice of using M-PERT or classic PERT is a modeling decision. In applications where the activity completion times are most accurately estimated as discrete values and when probabilities can be assigned to each value, the M-PERT approach will be preferred. When activity times must be considered continuous with a unimodal distribution and when the decision maker is able to specify the necessary parameters of the Beta distribution, the classic PERT will be preferred. Managers may now choose the method that is most appropriate.

Acknowledgements: We wish to thank the Editor and the reviewers for their helpful comments and suggestions.

## References

[1] Bishop, Y.M.M., Fienberg, S.E., and Holland, P.W. Discrete Multivariate Analysis. MIT Press, Cambridge, MA., 1975.

[2] Jordan, E.W., and Machesky, J.J. Systems Development: Requirements, Evaluation, Design, and Implementation. PWS-Kent, Boston, 1990.

[3] MacCrimmon, K.R. and Ryavec, C.A. “An Analytical Study of the PERT Assumptions.” Operations Research, 12, 1964, 16–37.

[4] Malcolm, D.G., Roseboom, J.H., Clark, C.E. and Farzar, W. "Applications of a Technique for R&D Program Evaluation." Operations Research, 7, 1959, 646–669.

[5] Moder, J.J., Phillips, C.R., and Davis, E.W. Project Management with CPM, PERT, and Precedence Diagramming, 3rd Ed. Van Nostrand Reinhold Company, New York, 1983.

[6] Ostle, J. Information Systems Analysis and Design. Burgess, Minneapolis, MN., 1985.

[7] Whitten, J.L., Bentley, L.D., and Barlow, V.M. Systems Analysis and Design Methods. Irwin, Boston, 1989.
