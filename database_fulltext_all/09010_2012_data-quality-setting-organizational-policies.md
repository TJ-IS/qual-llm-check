---
otero_id: 9010
otero_key: "RHZAN6TS"
title: "Data quality: Setting organizational policies"
authors: "Veda C. Storey; Rajiv M. Dewan; Marshall Freimer"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.06.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data quality: Setting organizational policies

Veda C. Storey <sup>a,</sup>⁎, Rajiv M. Dewan <sup>b</sup>, Marshall Freimer <sup>b</sup>

<sup>a</sup> Department of Computer Information Systems, College of Business Administration, Georgia State University, Atlanta, GA 30302, United States <sup>b</sup> Wm. E. Simon Graduate School of Business Administration, University of Rochester, Rochester, NY 14627, United States

## a r t i c l e i n f o

Article history: Received 19 May 2010 Received in revised form 18 May 2012 Accepted 19 June 2012 Available online 27 June 2012

Keywords: Data quality Organizational policies Economic analysis Incentives Data ownership

## a b s t r a c t

The collection, representation, and effective use of organizational data are important to a <sup>fi</sup>rm because these activities facilitate the increasingly important analysis needed for business operations and business analytics. Poor data quality can be a major cause for damages or losses of organizational processes. The many tasks that individuals perform within an organization are linked and normally require access to shared data. These linkages are often documented as process <sup>fl</sup>ow diagrams that connect the data inputs and outputs of individuals. However, in such a connected setting, the differences among individuals in terms of their preferences for data attributes such as timeliness, accuracy, and others, can cause data quality problems. For example, individuals at the head of a process <sup>fl</sup>ow could bear all of the costs of capturing high quality data but not receive all of the bene<sup>fi</sup>ts, even though the rest of the organization bene<sup>fi</sup>ts from their diligence. Consequently, these individuals, in absence of any managerial intervention, might not invest enough in data quality. This research analyzes this problem and proposes a set of solutions to this, and similar, organizational data quality problems. The solutions focus on principles of employee empowerment, decentralization, and mechanisms to measure and reward individuals for their data quality efforts.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

With the explosion of the amount of data being captured within organizations, stored in data warehouses, and mined for competitive use, maintaining the quality of the data supporting business decisions continues to be important, but very dif<sup>fi</sup>cult [5,12]. High-quality corporate data has become a prerequisite for world-wide business process harmonization, global spend analysis, integrated service management, and compliance with regulatory and legal requirements [13]. Indeed, poor data quality can be a major cause for damages and losses on organizational processes. Furthermore, data management incurs various associated costs with its acquisition, storage, security and maintenance at appropriate quality levels [21]. At the same time, modern business trends are increasingly focusing on data mining and business intelligence as tools for competition due to declining costs of acquisition and storage and sophisticated data analysis techniques [6].

Although data quality is traditionally considered in terms of information systems, it is also an organizational issue [28]. Within information systems, data quality has been regarded as multi-dimensional including, for example, dimensions of data quality: accuracy, completeness, consistency, and timeliness [1,3,12,15]. Information systems efforts are often aimed at measuring, quantifying and developing guidelines for measurements on these four dimensions. The primary issue with this approach is that data quality is treated as an ‘end’ goal in itself, rather than as a ‘means’ to achieving organizational objectives. The importance of the organizational perspective has been recognized for a long time. Orr [19] de<sup>fi</sup>nes data quality as the measure of agreement between the data views presented by an information system and that same data in the real world. Orr [19] argues that the quality of data should be accurate enough, timely enough, and consistent enough for the organization to survive and make reasonable decisions.

Weber et al. [28] de<sup>fi</sup>ne Data Quality Management (DQM) as “qualityoriented management of data as an asset, that is, the planning, provisioning, organization, usage, and disposal of data that supports both decision-making and operational business processes, as well as the design of the appropriate context, with the aim to improve data quality on a sustained basis,” thus, highlighting the importance of the management of this resource.

The study of data quality in information systems has made many important and useful contributions with much more work required [16,17,22,27]. Important in considering data quality and data quality methodologies are the dimensions and metrics used to assess data quality levels; the various types of costs associated with data quality issues; the processes that create or update data with the goal of producing services required by users that are considered in the methodology. Steps taken to improve data quality should include: evaluation of costs; assignment of process responsibilities, which identi<sup>fi</sup>es the owners of the processes and their data management responsibilities [2]. If the whole process needed to be redesigned, then, this causes business process reengineering [2,11,23]. Hence, analyzing data quality from a process perspective would be very useful.

This research is intended to analyze data quality by modeling it from an organizational perspective, in which the improvements in decisions made is considered to be a key measure of data quality value. The research explicitly recognizes that data quality management involves multiple stakeholders, possibly with con<sup>fl</sup>icts of interest among them. The models developed in this research are intended to be applicable to data quality management policies that are important and commonly occur within organizations. Guidelines for improving data quality that stress human factors in addition to technology ones are derived.

Data quality research often treats the organization as a monolithic entity with no differences in incentives or preferences. In reality, however, data quality is not valued identically by all users, nor is the value or cost of data quality distributed evenly across the organization. These differences, combined with the interdependence of departments on common business data, create a number of management problems when setting organizational data quality policies.

The objectives of this research, therefore, are to: 1) identify and analyze sources of common data quality problems that arise in organizations; 2) suggest policies for organizations to follow when setting data quality standards; and 3) propose solutions for data quality management problems.

Setting reasonable organizational data quality goals and auditing their implementation is dif<sup>fi</sup>cult. The major source of this dif<sup>fi</sup>culty is the fact that data quality depends on the whole business process with all users of the data affected. Data quality management involves multiple stakeholders, possibly with con<sup>fl</sup>icts of interest amongst them.

For example, data quality decisions made by the department that is responsible for capturing and maintaining the data limit the quality of the data for other departments. The interdependence of departmental data quality decisions is best examined from a process perspective.

A business process consists of a set of activities that are performed in coordination in an organizational and technical environment [29]. A typical business process [8] begins with a customer that may be an entity inside or outside of the organization. It proceeds through a number of business departments that may use, update, or augment the data gathered from previous steps in the process. The various tasks that comprise a process are best illustrated by a work <sup>fl</sup>ow diagram as shown in Fig. 1.

The purchasing process begins with a report from the inventory control department on inventory levels of raw materials needed by the manufacturing department. Any inaccuracies in data capture at this stage will affect decisions down the line; for example, data capture errors by the Inventory Control department. Although some errors at this stage can be detected and corrected through the use of semantic and referential integrity constraints in databases and applications, those that persist throughout the process will result in incorrect decisions and actions. An undercount may result in the order of unneeded parts and a delay in manufacturing. An over count can result in unanticipated delays in manufacturing schedules. If the managers in the Inventory Control department take extra care in training its workers and build extra checks and balances into its data capturing process, the whole organization will bene<sup>fi</sup>t from these efforts while the inventory department bears all the cost. A manager making a decision on levels of diligence will probably under invest in them from an organizational perspective. This situation is modeled in the next section.

An organization may solve this data quality problem in a number of ways. For example, information systems can be decentralized to the departmental level so the department that values the data most is given ownership of it. A more conventional approach involves setting up a procedure to measure and reward data quality.

This paper proceeds as follows. The next section develops a model for predicting quality choices made by individuals and organizations. This model is applied to develop a set of organizational policies to solve data quality problems and the resulting managerial implications of the solutions identi<sup>fi</sup>ed. A discussion and conclusion follow.

## 2. A model of organizational data quality

This section presents a model to analyze organizational data quality problems. This analysis concentrates on de<sup>fi</sup>ning a model that can be adopted at the organizational level. It models the most important aspects of data quality considerations, while remaining <sup>fl</sup>exible enough for organizations to add activities that are speci<sup>fi</sup>c to their process <sup>fl</sup>ow.

![](/api/attachments/RHZAN6TS/fulltext/images/0303bd3041a0d22e8f80d5888ba35d8950a9990ca996a7afd238bbc16db2aca3.jpg)  
Fig. 1. Flow of data in a purchasing process.

Consider a process <sup>fl</sup>ow diagram, such as that shown in Fig. 1. The following notation describes the diagram and other parameters:

i index of activities, $1 , . . . , n$

$P _ { i }$ set of activities, excluding i, whose value is affected by the quality levels chosen for activity i. Nominally, it may include all the activities that follow i in the process <sup>fl</sup>ow. However, it may be empty or as large as a set of all activities other than i.

q<sub>i</sub> quality level chosen by worker performing activity i $c _ { i } ( q _ { i } )$ cost of quality level q to the worker

$\nu _ { i } ( q _ { i } , q _ { j } , j ; i \in P _ { j } )$ This is the value to a worker who performs activity i. It depends on i and on the activities that precede it.

$V _ { N }$ Value to the organization in the case when there is no synergy between the activities other than interdependence on data.

$V _ { S }$ Value to the organization in the case with synergy between the activities over and above interdependence on data.

The assumptions needed for the model are listed below and based upon accepted notions of how organizations operate and basic economic principles. These variables can be measured, at some level, so that it will be possible for an organization to measure the impact, even when given a range of values for analysis.

1. Cost of data quality effort: The cost of quality level $q _ { i }$ of activity i to the worker who performs it (and to the organization), $c _ { i } ( q _ { i } ) ,$ , is twice differentiable, convex and increasing in q . It is natural to expect that higher levels of quality cost more than lower level ones. If this were not so, it would be in the worker's self interest to choose higher levels of quality without any intervention from management and the problem would be trivial. Furthermore, it is natural to assume that a unit increase in quality at higher levels of quality costs more than a similar change at lower levels. This could arise for many reasons. Suppose, for example, that a worker has a number of means available to improve data quality. The worker would “cherry-pick the low hanging fruit” <sup>fi</sup>rst; that is, implement the quality improvements that are easiest to implement <sup>fi</sup>rst.

2. Value of data quality: The value of an activity to a worker is increasing and concave in the level of quality of all activities that affect it. The concavity assumption captures the fact that the value of decisions may increase with increases in the quality of the data, but at a decreasing rate. For example, in determining shipping rates, knowing the region, state, county, zip code and street address would offer increasing precision and quality of decisions, but the successive impact of increases in precision on the accuracy of shipping costs decreases relatively.

3. Increase in data quality by a worker helps others: The cross partial derivatives of the value of an activity to a worker is positive on activities that affect it, i.e., $\frac { \partial ^ { 2 } \nu _ { i } } { \partial q _ { j } \partial q _ { k } } > 0$ for j, $k \in \{ i \cup \{ j \colon i \in P _ { j } \} , j \neq k$ and zero otherwise. This implies that the quality efforts by workers are complementary, i.e., increases in the quality of one activity makes the quality of others more valuable. To illustrate, consider a simple organization in which Worker 1 observes and captures the data and Worker 2 processes it. Processing the data more carefully may be worthwhile only if it has been captured accurately in the <sup>fi</sup>rst place (“garbage in–garbage out.”) Conversely, it is worth more to capture data accurately if it is used with greater precision for decision making.

Next, the organization as a whole is considered, recognizing the interdependency of information technology, the organization, and the processes. With respect to the value of the organization, two cases need to be considered by making one of two alternative assumptions:

4. (Interdependence but No Synergy) The value of the tasks to the organization is the sum of the values to the individual divisions. This is a simple case where there is no synergy in the value of the tasks, but yet, there is still an interdependence that arises through common data usage. In this case $V _ { N } = \sum _ { i } { \nu _ { i } }$ and the marginal value of quality to the organization is the sum of the values to the individuals, $\mathrm { i . e . , } \frac { \partial V _ { N } } { \partial q _ { i } } { = } \sum _ { j } \frac { \partial \nu _ { j } } { \partial q _ { i } } .$

5. (Interdependence and Synergy) The value to the organization is larger than the sum of value to the individual, i.e, $V _ { S } > \sum _ { i } { \mathrm { . } }$ v . In this case, it is also assumed that $V _ { S }$ is concave and that the marginal value of quality to the organization is strictly greater than the marginal value of quality to any one worker, i.e., $\frac { \partial V _ { S } } { \partial q _ { i } } > \frac { \partial V _ { N } } { \partial q _ { i } } = \sum _ { j } \frac { \partial \nu _ { j } } { \partial q _ { i } }$ for all i. This can occur in a variety of ways. One common scenario is that the quality of work done in a task in a process affects other processes within the company. Consequently, the marginal value for the organization that cares about the value of all work <sup>fl</sup>ows is greater than that of the worker performing the task at that one station. As is the case with the $\nu _ { i } ,$ assume that $\frac { \partial ^ { 2 } V _ { s } } { \partial q _ { j } \partial q _ { k } } > 0$ if there is activity i such that $j , k \in \{ i \cup \{ j \colon i \in P _ { j } \} , j \neq k$ and zero otherwise.

With these assumptions in place, consider <sup>fi</sup>rst a situation in which each worker selects the quality that is best for him or her. Since the value of quality to the worker depends on the quality level chosen by others, the worker has to consider another's decision while making his or her own. Given the quality level that the worker expects others to choose, he or she picks a level that is best for himself or herself. Every worker makes a decision in a similar fashion. The equilibrium that exists in this setting is referred to in economics (speci<sup>fi</sup>cally game theory) as Nash Equilibrium [24]. A situation is in Nash Equilibrium if no one involved would be better off by changing his or her strategy while the other people involved (in this case the workers) retain their strategies. This is represented below.

Each worker i, picks quality level q<sub>i</sub><sup>∗</sup> such that:

$$
q _ {i} ^ {*} \in \underset {q _ {i}} {\arg \max} v _ {i} \left(q _ {i}, q _ {j} ^ {*} j: i \in P _ {j}\right) - c _ {i} (q _ {i})
$$

The <sup>fi</sup>rst order conditions for the above are:

$$
\frac {\partial v _ {i}}{\partial q _ {i}} = \frac {\partial c _ {i}}{\partial q _ {i}}
$$

Second, consider a situation in which the organization with no synergy between tasks (Assumption 4) selects the quality level for each worker.

$$
\max _ {q = \left(q _ {1} \dots q _ {n}\right)} V _ {N} (q) - \sum_ {i = 1 \dots n} c _ {i} \left(q _ {i}\right)
$$

where $V _ { N } = \sum _ { i } { \nu _ { i } } .$

The <sup>fi</sup>rst order condition for the organization's optimization problem

$$
\text { is: } \frac {\partial v _ {i}}{\partial q _ {i}} + \sum_ {j: i \in P _ {j}} \frac {\partial v _ {j}}{\partial q _ {i}} = \frac {\partial c _ {i}}{\partial q _ {i}} \text {   for   all   } i.
$$

Let $q _ { 1 } ^ { * * } , . . . , q _ { N } ^ { * * }$ be the organization's choice.

## Theorem 1. Interdependence but No Synergy

Considering an organization in which the value to the organization is the sum of the value to the individuals, the individuals under-invest in quality compared to the organization's optimal choice, i.e., individual workers voluntarily select a quality level lower than the level optimal for the organization.

## The proof is provided in Appendix A.

This theorem highlights the quality management problem that exists in organizations. If managers do not intervene, then the workers, left to select the quality levels themselves, will not choose ones that are the best for the organization. This kind of situation is common whenever the actions of an individual create a bene<sup>fi</sup>t for others. Such actions are said to create a positive externality. The individual making his or her own decision ignores the value created for others. As a result, the individual compares only the marginal cost of an additional unit of quality to the marginal value to the individual alone, rather than for the individual and the rest of the organization. It is this self-interested behavior that leads to a less than optimal solution for the organization. Many similar situations occur, such as the “Tragedy of the Commons” [18], a situation in which individuals, acting on their own selfinterests, will eventually deplete a scarce resource when it is not of anyone's interest in the long run to do so.

The problem gets even worse when there is synergy as the individual workers ignore this too in selecting their individually optimal quality levels.

## Theorem 2. Interdependence and Synergy

For an organization in which the value to the organization is greater than the sum of the value to the individuals, the individuals under-invest in quality even more than in organizations with no synergy.

The proof is found in Appendix A.

## 3. Organizational policies to address data quality problems

Organizations do not operate in a vacuum. Rather, they are affected greatly by the environment within which they operate and the new and existing technologies they adopt. Changes in information technology, especially, development of technologies for collaboration among local and virtual teams; enterprise wide integrated data warehouses and planning systems; and other management information systems, can help to provide a number of solutions to the problems of data quality in organizations. Employees are an organization's strongest asset. Therefore, solutions to organizational data quality problems should be approached from both employee and organizational perspectives.

Employee based:

1. Personal computing: the decision maker processes the information.

2. Employee empowerment: the worker at the head of the process, closest to the customer (customer-facing), makes decisions.

3. Teams: multi-skilled teams, with IT-facilitated, rich interaction, perform the process jointly.

Organization theory based:

4. Data quality program: program for data quality measurement and incentives for key employees in the process.

5. Ownership: change data ownership.

These solutions depend as much on organizational theory as they do on technology. Problems with under-investment by individuals have been addressed by setting up incentive schemes [14] or changing ownership rights to projects [4,7]. Relevant sociobehavioral theories include enhanced participation in decision making, hierarchy of authority [9], top management involvement [10], establishing leadership in data quality [26], and others [2].

Each of the solutions is analyzed below. The <sup>fi</sup>rst employee-based perspectives reply on mathematical analysis. The organizational perspectives are discussion based.

## 3.1. Personal computing

The last decade has seen advances in technology being increasingly responsible for integration, communication, collaboration, and computing ease. This helps to address some of the economic problems faced by organizations by allocating decision rights to the person to whom it matters. The ubiquitous proliferation of increasingly powerful personal computers, and user friendly software and browsers, as well as reliable telecommunications has resulted in a two decade long trend in growth of personal computing. Historically, business processes have wended their way through many departments, each of which collects, modi<sup>fi</sup>es and updates data until it reaches a decision maker who uses the data. Long data <sup>fl</sup>ows describing such processes are common. Quality decisions, made earlier by workers and managers, who themselves may not use some of the data collected, impact the decisions made at the end of the <sup>fl</sup>ow. This causes a number of problems related to data quality.

First, a long data <sup>fl</sup>ow that separates data capturing and processing from the <sup>fi</sup>nal decision making also puts the workers at the early parts of the process at an information disadvantage. Since they do not make the decision, the workers do not know the value of data qualities such as accuracy and timelines. This can, obviously, be a source of data quality problems.

Consider an employee who is entering data into an electronic form while talking to a customer. Eventually, a decision may be made that depends upon this data. The worker capturing the data may not know the importance of the quality of different data elements in different cases. For instance, the model year of a car may be critical for diagnosing a certain kind of failure but not as relevant for others. This kind of knowledge is useful in motivating additional effort for data quality, but hard to judge by anyone but the decision maker.

Second, worker motivation can be a problem when the quality investment must be made by one worker. and the benefits from better decision making accrue to someone else. In such situations, the organization must craft an incentive mechanism that measures and, accordingly, rewards workers.

One solution to these data quality problems is task consolidation in which the initial tasks of data capturing and processing are consolidated with decision making. Task consolidation also offers bene<sup>fi</sup>ts of hand off and cycle time reductions. The value of having the decision maker perform the data processing tasks is analyzed in the example below, based upon the model presented above.

Example 1. Consider the “Audit Inventory” and “Materials Planning” tasks at the head of the process <sup>fl</sup>ow diagram in Fig. 1. The worker in the Inventory Control department, Worker 1, counts and enters the inventory levels, which is used for materials planning by Worker 2 in the Manufacturing department. Let the value of data quality to worker 1 be $\nu _ { 1 } = q _ { 1 } ( a _ { 1 } – b _ { 1 } q _ { 1 } )$ where $q _ { 1 }$ is the level of quality picked by worker 1, $0 { \leq } q _ { 1 } { \leq } 1$ , and $a _ { 1 } > 2 b _ { 1 } > 0 .$ A value of $q _ { 1 } = 1$ , represents that the quality is the best. The variables $a _ { 1 }$ and $b _ { 1 }$ are used in the analysis to capture the desired direction. It is easily veri<sup>fi</sup>ed that $\nu _ { 1 }$ is increasing and concave over the range. The cost of achieving the quality level is $c _ { 1 } q _ { 1 } ^ { 2 } ,$ , where $c _ { 1 } > a _ { 1 } / 2 - b _ { 1 }$

Worker 2 decides on the quantity to order for each part using the inventory data collected by worker 1. The value of purchase planning is affected by the quality of inventory data capture, $q _ { 1 } ,$ , and the quality of materials planning, q .

$$
v _ {2} = q _ {2} (a _ {2} - b _ {2} q _ {2}) + \mathsf {e} q _ {1} (b _ {2} q _ {2} - q _ {1})
$$

where ε is small enough so that εb $\frac { a _ { 2 } } { 2 } - b _ { 2 } ; \varepsilon < 4 / b _ { 2 } .$ . The cost of data qual ity is $c _ { 2 } q _ { 2 } ^ { 2 } .$ . This is easily veri<sup>fi</sup>ed by $\nu _ { 2 }$ being concave and increasing in $q _ { 2 } .$

Assume that the organization accrues the total value of $\nu _ { 1 } + \nu _ { 2 }$ and the total cost of the effort. First, consider the case when each worker individually picks the data quality. Workers choose a quality level that maximizes the net bene<sup>fi</sup>t to them. It is easily veri<sup>fi</sup>ed, for the parameter ranges listed above, that the solution is interior and <sup>fi</sup>rst order conditions are necessary and suf<sup>fi</sup>cient. These are:

$$
\begin{array}{l} a _ {1} - 2 b _ {1} q _ {1} = 2 c _ {1} q _ {1} \\ a _ {2} - 2 b _ {2} q _ {2} + \varepsilon b _ {2} q _ {1} = 2 c _ {2} q _ {2} \end{array}
$$

Solving these simultaneously, we obtain the Nash solution:

$$
q _ {1} ^ {*} = \frac {a _ {1}}{2 (b _ {1} + c _ {1})}, q _ {2} ^ {*} = \frac {a _ {2}}{2 (b _ {2} + c _ {2})} + \varepsilon \frac {a _ {1} b _ {2}}{4 (b _ {1} + c _ {1}) (b _ {2} + c _ {2})}
$$

Obviously, by applying Theorem 1, the organization would prefer that individual workers do not set the quality level.

Corollary 1. Using $\nu _ { 1 } , \nu _ { 2 } , V _ { N } ,$ and costs defined above, the workers individually will under-invest in quality from an organizational perspective.

It is easily veri<sup>fi</sup>ed that Assumptions 1–4 hold when $\varepsilon { < } \frac { 4 } { b _ { 2 } } .$

This solution is explored further by determining the quality levels the organization would select:

$$
\begin{array}{l} q _ {1} ^ {* *} = \frac {2 a _ {1} (b _ {2} + c _ {2}) + a _ {2} b _ {2} \varepsilon}{4 (b _ {1} + c _ {1}) (b _ {2} + c _ {2}) + 4 (b _ {2} + c _ {2}) \varepsilon - b _ {2} ^ {2} \varepsilon^ {2}} \\ q _ {2} ^ {* *} = \frac {2 a _ {2} (b _ {1} + c _ {1} + \varepsilon) + a _ {1} b _ {2} \varepsilon}{4 (b _ {1} + c _ {1}) (b _ {2} + c _ {2}) + 4 (b _ {2} + c _ {2}) \varepsilon - b _ {2} ^ {2} \varepsilon^ {2}} \end{array}
$$

Consider an alternative process organization in which Worker 2 picks the quality levels and performing both of the activities. To obtain the solution, assume that Worker 2 receives a total value of $\nu _ { 1 } + \nu _ { 2 } .$ . The worker needs to spend q<sup>2</sup> and $q _ { 2 } ^ { 2 }$ hours respectively for quality $\mathbf { \nabla } q _ { 1 }$ and $q _ { 2 }$ on inventory audit and planning, respectively. The cost to the worker (and the organization) is $c _ { 2 } ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } )$

In Figs. 2 and 3, the quality levels picked by Workers 1 and 2 are plotted against increasing interaction, ε where the following values have been set: $a _ { 1 } = 3 , b _ { 1 } = 1 , c _ { 1 } = 8$ and $a _ { 2 } = 1 0 , b _ { 2 } = 8 , c _ { 2 } = 9$

In Fig. 2 the quality of inventory audit picked by Worker 1 is lower than that preferred by the organization. In fact, while the organization prefers to have an increase in quality of inventory audit as the interaction level increases, the worker continues to pick the same low level. If we follow the principle above, and have Worker 2 perform inventory audit and planning, then the quality level of inventory audit selected by this worker more closely tracks the organization's desired quality level and increases as the interaction level increases.

![](/api/attachments/RHZAN6TS/fulltext/images/b40781b9e73e86812c10c98bec2e132547dcbfafad28d66c6ab49cf782b5430e.jpg)  
Fig. 2. Quality of activity 1 (q ) versus interaction level (ε).

![](/api/attachments/RHZAN6TS/fulltext/images/8ee7c57b6cfaba04bc51efadff63b5e2819cf8fe770737e15b6fd1e66f5fa7c6.jpg)  
Fig. 3. Quality level of activity 2 (q<sub>2</sub>) versus interaction level (ε).

In Fig. 3, the quality level of planning picked by Worker 2 is lower than that preferred by the organization. Note that this is the case even though the value of inventory audit is not affected by the quality of planning. When Worker 2 performs both tasks, he or she picks a higher quality for planning (and for inventory audit, as shown earlier). This is because the higher level of quality of inventory audit makes an increased investment in the quality of planning more worthwhile. From a process <sup>fl</sup>ow perspective, Worker 2 decides to process the data more carefully when the data capturing is done with higher quality.

This analysis indicates the presence of quality problems for the organization. Having Worker 2 perform both of the activities greatly alleviates the problem. This is true even when Worker 2 is more skilled and better paid than Worker 1 for larger interaction levels. This can be seen in Fig. 4 where the net value to the organization from different processes is plotted, for $c _ { 2 } > c _ { 1 } ,$ i.e., Worker 2's time is more valuable than that of Worker 1. For large dependence, when ε is larger, the organization would prefer Worker 2 do the job of the less skilled Worker 1, in addition to his or her own job. In fact, Worker 2 picks a higher quality level for both the activities if the worker does the whole process. In the case of $c _ { 1 } > c _ { 2 } ,$ , this preference is true à fortiori.

## 3.2. Employee empowerment

Employee empowerment uses technology to support decision making and solves some of the externality problems. Employee empowerment is another form of task consolidation where the worker earlier in the process, who typically is less skilled, performs many of the tasks that use the data he or she captures. This approach was originally proposed by the Reengineering Principle: “Subsume information processing work into real work that produces the information.” [11]. This principle suggests that employees who capture the information also do more of the processing associated with decision making.

Employee empowerment creates challenges for the information system to integrate information and provide decision support and expert systems to aid hitherto lesser skilled workers to make a decision. This approach offers the advantages of reducing handoffs and increasing quality. These advantages may outweigh the cost of IT support and relative inef<sup>fi</sup>ciency of lesser skilled workers. To explore this, consider once again the “Audit Inventory” and “Materials Planning” tasks at the head of the process diagrammed in Fig. 1. If Worker 1, who previously only performed the inventory audit, is asked to do the material planning as well, he or she might not perform the planning task as ef<sup>fi</sup>ciently as Worker 2. Let η capture the increase in costs from the inef<sup>fi</sup>ciency and additional technological support when Worker 1 performs the more complicated planning task. In particular, the cost of performing Worker 2's task by Worker 1 is (1+η) c<sub>1</sub> q<sub>2</sub><sup>2</sup>.

![](/api/attachments/RHZAN6TS/fulltext/images/bba7d3a4656b141ae3d12ae6298c736974c469c5bcdcf20dcec4a65cc172b9f7.jpg)  
Fig. 4. organizational net value versus interaction level (ε).

In Fig. 5, η is set equal to 0.1 and the task dependence parameter varied from 0 to 1. The net value to the organization is higher when Worker 1 performs all tasks than when the tasks are highly dependent. In this case, the value of task consolidation exceeds the cost of having a relatively inef<sup>fi</sup>cient worker perform all of the tasks.

In general, the choice of a worker to perform the whole task; that is, the choice between worker empowerment and end-user computing, will depend upon the relative inef<sup>fi</sup>ciency of the lesser skilled worker and the cost of IT support versus the cost of using a highly skilled worker to perform tasks that require lower skill levels.

## 3.3. Use of teams

Over the past two decades, the increased use of teams to replace parts of a hierarchical organization has been well-documented and believed to be one of the most powerful enablers of organization structural change [8]. Teams facilitate interactions, often involved and numerous, among individuals. The interaction and awareness of each other's quality decisions can change the choices made by an individual to one that more closely re<sup>fl</sup>ects the choice of the organization. Teams, including virtual teams, are the favored method for organizing large projects [20]. The value of teams for improving data quality is illustrated below.

Example 2. This example continues the scenario explored in Example 1, which shows that worker i's self-motivated choice was to pick a level of quality $q _ { i }$ such that:

$$
a _ {i} - 2 b _ {i} q _ {i} + \varepsilon b _ {i} \sum_ {i \in P _ {j}} q _ {j} = 2 c _ {i} q _ {i}
$$

Assume that individuals are similar and have similar interactions. Let each individual interact, on average, with m other individuals. Invoking symmetry and simultaneously solving the conditions for each worker, we obtain:

$$
q ^ {*} = \frac {a}{2 (b + c) - m \varepsilon b}
$$

![](/api/attachments/RHZAN6TS/fulltext/images/fca3c484145fcca279cd4e545a63ff1c05c33e1222d0244421471cc8498baec6.jpg)  
Fig. 5. Employee empowerment: net value versus interaction level (ε).

The case where the organization picks the quality level is:

$$
q ^ {* *} = \frac {a}{2 (b + c) - m \varepsilon b - m \varepsilon (b - 2)}
$$

For $b > 2 ,$ the denominator for $q ^ { * * }$ is smaller by mε $( b - 2 ) , s 0 ,$ , for this case, $q ^ { * * } { > } q ^ { * }$ . The same relationship would have been obtained by employing Theorem 1.

Corollary 2. Using the value and cost functions of Example 2, workers under-invest in quality, $i . e . , q ^ { * * } { \geq } q ^ { * }$

It is interesting to examine the performance of self-managed workers as the interaction level increases. This is explored in Figs. 6 and 7.

The solid line is the benchmark case in which the organization dictates the quality level for all workers, and the value of each worker depends on six others. The benchmark case is represented by a solid line. The dashed line is for a self-managed organization with levels of interaction ranging from 1 (star organization), 2 (straight line or hierarchy of any span), and larger teams. We see that the individual quality levels and organization value increases as teams get larger. (Of course, there may be a point where team size becomes too unwieldy.) The difference at interaction level 6 is the difference between dictated levels and voluntary choice $( q ^ { * * } - q ^ { * } )$ .

## 3.4. Incentive schemes

Setting up business procedures and incentive schemes to coordinate choices solves data quality problems within organizations. There are three parts to this process: 1) set clear individual and group goals for data quality; 2) set incentives that are tied to success in meeting goals; and 3) build-in mechanisms for measuring and compensating workers based on performance.

## 3.4.1. Setting data quality goals

First, clear data quality goals must be set. From a process perspective, the choice of data quality goals is dictated by the goal of maximizing net value to the customers of the process. Applying this to the work <sup>fl</sup>ow in Fig. 1, the key “customers” are the manufacturing department that schedules its activities based on parts availability and the supplier who must be paid for goods and services rendered. The manufacturing department would bene<sup>fi</sup>t greatly from an accurate inventory count and reduced cycle time for the parts ordering process. The supplier wants a short cycle time from shipping to payment. Additionally, there could be organizational goals for control and accounting.

Information systems standards, which are part of any control mechanism for information systems, play a key role in formulating and communicating data quality goals. Programming standards (mandated structured walk-throughs, documentation requirements, etc.) are an example of information systems standards that help improve the quality of data by reducing errors from software bugs, improving relevance of data, and so forth. Standards play a role similar to that of budgets in <sup>fi</sup>nancial management. They set the minimal acceptable level that all participants must meet to qualify for incentives.

![](/api/attachments/RHZAN6TS/fulltext/images/c083d43115f9dae018ecac210ca3adeb9661a57c9f6018f4891c1c22624473a6.jpg)  
Fig. 6. Impact of team size on quality level.

![](/api/attachments/RHZAN6TS/fulltext/images/65296be944ba32dc286c90aba6ffc3264fe0801547f9762d91bdfe7d5e843fc7.jpg)  
Fig. 7. Net value versus team size.

## 3.4.2. Setting incentives

Differences in costs and bene<sup>fi</sup>ts from data quality are a source of dif-<sup>fi</sup>culty in managing data quality within an organization as discussed earlier. Consequently, it is only natural to expect incentives, which alter a decision maker's preferences, to play a role in providing a solution. Group and individual incentives that are tied to clear organizational goals can be very effective. These incentives, may change, not only the on time performance, but also large changes in employee morale and cooperation.

## 3.4.3. Measuring performance

Setting goals and incentives work only if they are credible. Credibility requires a commitment to reward performance. This, in turn, requires that performance be measured in clear and direct terms in order to provide feedback to employees. Fortunately, information systems are uniquely suited to facilitate measurement. Numerous tools are available to measure human and machine performance. The key is to choose one that makes measurements which are directly connected to data quality goals. For example, if cycle time is an important goal, the information system can be enhanced to use the time stamps on customer orders to regularly print out average cycle times. A measurement example is the percentage scanned report that is regularly generated at large retailers to measure the performance of point of sale personnel. A certain amount of skill and diligence is required to reliably scan items at the point of sale terminal. The system keeps track of the percentage of items that the employee scans, instead of typing-in the product code. Thus, percentage correctly scanned is a quality measure that is directly measured by the information system used by the retailers. Employees who obtain the highest scanning percentages are recognized; others may require additional training. This analysis identi<sup>fi</sup>es a speci<sup>fi</sup>c action to be taken by the organization.

## 3.5. Data ownership policies

Data ownership polices involve decentralization of information technology resources, departmental computing, etc. Coase [7] suggested that ownership or allocation of decision making rights can achieve a similar purpose. The work <sup>fl</sup>ow in Fig. 1 can be used to illustrate Coase's approach. First, consider a situation in which the inventory control department does not report to the manufacturing department and maintains its data in its own or corporate database system. Provided the manufacturing department does not have direct control and incentives are not used, the inventory department manager will under invest in data quality for data capture from the perspective of the manufacturing manager. This situation was illustrated in Fig. 2. One solution to the problem is to make the inventory department report to the manager of the manufacturing department who would then set the data quality standards. (A similar solution was proposed by Van Alstyne et al. [25].)

Decentralization of data ownership and management means that, instead of having a centralized database, the data is decentralized and managed by systems owned by the departments. In cases where there is a clear bene<sup>fi</sup>ciary from the quality of certain data, Coase's [7] approach requires that the department that derives the most bene<sup>fi</sup>t from the data quality also owns the data. It is then free to manage the data server and set usage policies that are aligned with its data quality requirements. This completely obviates the externality problem described in Sections 2 and 3. In cases where there is not a clear bene<sup>fi</sup>- ciary of data quality, a combination of ownership policies and incentive schemes will be needed to manage the data quality of the organization. A system of data stewardship would be appropriate because the bene<sup>fi</sup>- ciaries of data quality exist across the <sup>fi</sup>rm). Data governance (which includes a combination of ownership policies and incentive schemes) is needed to manage the data quality of the organization.

## 4. Discussion and implications

## 4.1. Organizational data interdependencies

Data quality characterizes the whole business process rather than just the data found in corporate databases. Each step in the process, from data capture to processing for decision support, has an impact on the <sup>fi</sup>nal quality of the data. This creates interdependencies in the organization where the net value that an individual or department receives from data quality depends upon the choices of others. The result is a source of data quality management problems in an organization. The problems may manifest themselves as under investment in data quality enhancing activities by individuals as they do not appreciate the value they create for others within the organization. Even if managers are diligent in enhancing data quality, the multi-attribute nature of data quality poses additional problems. Managers make tradeoffs between data quality attributes that suit their decision making, but not necessarily the organization as a whole.

## 4.2. Solution approaches

Solutions to these data interdependent data quality problems require attention to both the human and machine portions of the information system. Data quality problems and solutions must be considered as early as the design stage of an information system. To the extent that data quality problems can be anticipated, automated checks such as traditional referential and integrity constraints can be built into database management systems. With these constraints in place, all applications that read or update data will transparently receive the bene<sup>fi</sup>t of these checks. It is also easier to build in data quality performance measurements into the information system at the design stage. It would be useful to analyze the decisions and determine the impact of data quality on them. Then, a measurement system can be built to measure these key data quality attributes.

Data quality considerations should play a large role in the design of information systems with data ownership a key decision. The department that owns the data should also manage the data server and sets policies for data use update. Hence, it would be bene<sup>fi</sup>cial if the department that derives the most bene<sup>fi</sup>t from the data is the one to own and manage it. This would reduce the interdependency problem. The remaining issues could be dealt with by an incentive system.

Finally, to improve data quality, the human part of the information systems deserves as much conscious attention as the machine part. Identifying key data quality characteristics, setting clear data quality goals, and building incentive systems to reward individuals who perform well are essential parts of an organizational architecture.

## 4.3. Limitations

The model developed in this analysis was based on understanding and providing a representation of issues related to modeling data quality within organizations, taking into consideration the decision makers and their roles. The model needs to be implemented as a prototype tool and tested for robustness with a range of values for the variables, and applied to real world organizations to empirically assess its effectiveness. Initially, values can be generated based upon experienced estimates to test for robustness before application to real world case studies.

Data quality activities generally appear in the following stages [2].

State reconstruction collects information on organizational processes and services, data collections and related management procedures, quality issues and corresponding costs. This requires a collection of these values from cooperating sites. It is unlikely that such values would be available a prior and, thus, would need to be collected manually or by implementing speci<sup>fi</sup>ed collection variables.

Assessment/measurement measures the quality of data collected from a set of data quality measurements. In this case, the model will be applied in an attempt to isolate the areas where improvements to poor data quality situations are needed.

Improvement efforts will require the development of the strategies and procedures that need to be put into place to obtain new data quality levels. Since the model developed incorporates variables that take into consideration the decision makers, multiple conclusions should be reached for what actions to take for improvements.

Thus, this general approach of collecting information to instantiate the variables, measuring, analyzing and attempting to improve the data quality, may require iterations that might lead to changes in business rules and improvement in data quality monitoring and analysis.

## 5. Conclusion

This paper has proposed an analytical model to represent data quality management scenarios that involve multiple stakeholders. Application of the model to different scenarios, with varying values of the model's attributes, illustrated the sensitivity to the changes. The analysis was used to generate a set of organizational policy considerations. Guidelines for improving data quality that stress human factors in addition to technology ones were derived.

This research makes several notions explicit. It recognizes that there are multiple aspects of, and need for, modeling data quality, with different users of information having different data quality needs. It focuses on data quality and processes, with the notion that users can actually select the level of quality. There are different ways to view and address the data quality problems that any organization faces. Although the research provides one formalized model of data quality, it recognizes that there are others and that the overall increase in data quality by one employee helps another. Data quality depends on the whole business process and explicitly provides value to the <sup>fi</sup>rm. Data quality problems, then, should be approached from both employee and organizational perspectives.

Future research is needed to implement the model into a tool and test it on simulated values of variables and real world data. The policies might then be modi<sup>fi</sup>ed and expanded to re<sup>fl</sup>ect changing organizational forms. An assessment is needed of the challenges involved in identifying and estimating values for the variables involved in the models.

## Acknowledgements

This research was supported by Georgia State University and the University of Rochester. The authors gratefully acknowledge the assistance of the editor-in-chief, the managing editor, and the reviewers.

## Appendix A

Proof of Theorem 1. Note that the <sup>fi</sup>rst order conditions for the individuals' choices are:

$$
\frac {\partial v _ {i}}{\partial q _ {i}} = \frac {\partial c _ {i}}{\partial q _ {i}}
$$

for each individual i. Let ${ q _ { 1 } } ^ { * } , . . . , { q _ { n } } ^ { * }$ solve these equations.

The <sup>fi</sup>rst order conditions for optimality for the organization with no synergy are:

$$
\frac {\partial v _ {i}}{\partial q _ {i}} + \sum_ {j: i \in P _ {j}} \frac {\partial v _ {j}}{\partial q _ {i}} = \frac {\partial c _ {i}}{\partial q _ {i}}
$$

for each task i. Let ${ q _ { 1 } } ^ { * * } , . . . , { q _ { n } } ^ { * * }$ solve these equations.

Consider any activity i that is an ‘initial’ activity, i.e., v only depends on $q _ { i \cdot }$ There must be at least one j with $i \in { \cal P } _ { j }$ or else i would not be a part of the network of activities. By assumption 2 we have $\frac { \partial v _ { j } } { \partial q _ { i } } > 0$ and hence we have $\sum _ { j : i \in P _ { j } } \frac { \partial \nu _ { i } } { \partial q _ { j } } > 0 .$ . An activity is ‘terminal’ if there is no i with with $i \in P _ { j } .$

Substituting this into the <sup>fi</sup>rst order condition for individual's choice, we get:

$$
\left[ \frac {\partial v _ {i}}{\partial q _ {i}} - \frac {\partial c _ {i}}{\partial q _ {i}} \right] _ {q = q * *} <   0
$$

Since activity i has been taken to be an ‘initial’ activity, $\nu _ { i }$ depends only on $q _ { i \cdot }$ As a function of $q _ { i } , v _ { i } - c _ { i }$ is strictly concave and so ${ q _ { i } } ^ { * } { < q _ { i } } ^ { * * }$

If activity i is not initial, then we similarly have:

$$
\left[ \frac {\partial v _ {i}}{\partial q _ {i}} - \frac {\partial c _ {i}}{\partial q _ {i}} \right] _ {q = q * *} <   0 \text {   if   the   activity   is   not   terminal   and   0   otherwise. }
$$

Note that $c _ { i }$ depends only on $q _ { i }$ while $\nu _ { i }$ depends on $q _ { i }$ and on all $q _ { k }$ where k precedes i. We can make an inductive hypothesis that $q _ { k } ^ { * } < q _ { k } ^ { * * }$ for all k that precede i. For such k we have $\frac { \partial ^ { 2 } \nu _ { i } } { \partial q _ { i } \partial q _ { k } } > 0$ and so $\left. \frac { \partial \nu _ { i } } { \partial q _ { i } } \right| _ { q _ { i } = q _ { i } * * a n d q _ { k } = q _ { k } * i f k \neq i } < \frac { \partial \nu _ { i } } { \partial q _ { i } } \Bigg | _ { q = q * * } .$

Hence $\left[ \frac { \partial \nu _ { i } } { \partial q _ { i } } - \frac { \partial c _ { i } } { \partial q _ { i } } \right] _ { q _ { i } = q _ { i } * * a n d q _ { k } = q _ { k } * i f k \ne i } < 0 .$

As before this gives ${ q _ { i } } ^ { * } { < q _ { i } } ^ { * * }$ for activities i that are not initial. QED

Proof of Theorem 2. For λ: $0 \leq \lambda \leq 1$ , de<sup>fi</sup>ne:

$$
f (q; \lambda) = \lambda (V _ {S} (q) - \sum c _ {i} (q _ {i})) + (1 - \lambda) (V _ {N} (q) - \sum c _ {i} (q _ {i}))
$$

Let q(λ) solve Let q(λ) solve $\nabla f ( q ; \lambda ) = 0 .$

Using the Implicit Function Theorem, we get: $\frac { \mathrm { d } q ( \lambda ) } { \mathrm { d } \lambda } = - H ^ { - 1 }$ $( \nabla V _ { S } - \nabla V _ { N } )$ where H is the Hessian Matrix of f(.).

(Note that the $\frac { \partial c } { \partial q }$ terms are independent of λ and hence they do not enter into the above equation.)

Using convexity of c and concavity of $V _ { S }$ and $\nu _ { i } ,$ H is a negative de<sup>fi</sup>nite matrix.

By hypothesis, it has positive off diagonal elements.

By Takayama, Pg. 393, Thm. $4 . \mathsf { D } . 3 , H ^ { - 1 }$ is non-positive.

$\nabla V _ { S } - \nabla V _ { N }$ is non-negative by hypothesis.

Hence $\frac { \mathrm { d } q ( \lambda ) } { \mathrm { d } \lambda } { \geq } 0 .$ . This implies tha $q ( 0 ) { \leq } q ( 1 )$ , i.e., the optimal quality choice by the organization with synergy is greater than one without synergy. QED

## References

[1] D.P. Ballou, H.L. Pazer, Modeling data and process quality in multi-input, multi-output information systems,, Management Science 31 (1995) 150–162.

[2] C. Batini, C. Cappiello, C. Francalanci, A. Maurino, Methodologies for data quality assessment and improvement, ACM Computing Surveys 41 (2009) 1–52.

[3] R. Blake, P. Mangiameli, The effects and interactions of data quality and problem complexity on classi<sup>fi</sup>cation, ACM Journal of Data and Information Quality (JDIQ) 1 (2011).

[4] J.A. Brickley, C.W. Smith Jr., J.L. Zimmerman, Managerial Economics and Organizational Architecture, Irwin, 2006.

[5] C. Cappiello, C. Francalanci, B. Pernici, Data Quality Assessment From the User's Perspective, In: Proceedings of the International Workshop on Information Qualit in Information Systems (IQIS'04), 2004.

[6] S. Chaudhuri, U. Dayal, V. Narasayya, An overview of business intelligence technology, Communications of the ACM 54 (8) (2011) 88–98.

[7] R. Coase, The problem of social cost, Journal of Law and Economics 3 (1960) 1–44.

[8] T.H. Davenport, Process Innovation: Reengineering Work Through Information Technology, Harvard Business School Press, 1993.

[9] R. Deshpande, The organizational context of marketing research use, Journal of Marketing 46 (1982) 91–101.

[10] D. Halloran, S. Manchester, J. Morlarty, R. Riley, J. Rohrman, T. Skramstad, Systems development quality control, MIS Quarterly 2 (1978) 1–12.

[11] M. Hammer, Reengineering work: don't automate, obliterate, Harvard Business Review (1990) 104–112.

[12] B. Heinrich, M. Kaiser, M. Klier, A procedure to develop metrics for currency and its application in CRM, ACM Journal of Data and Information Quality 1 (2009)

[13] K.M. Huner, M. Ofner, B. Otto, Towards a Maturity Model for Corporate Data Quality Management, In: Proceedings of the 2009 ACM symposium on Applied Computing (SAC '09), 2009.

[14] M. Jensen, Organization theory and methodology, The Accounting Review 58 (1983) 319–339.

[15] Y.W. Lee, L.L. Pipino, J.S. Funk, R.Y. Wang, Journey to Data Quality, 1, MIT Press, 2009.

[16] S.E. Madnick, Y. Lee, Search of novel ideas and solutions with a broader context of data quality in mind, ACM Journal of Data and Information Quality 4 (2012).

[17] S.E. Madnick, Y. Lee, R.Y. Wang, H. Zhu, Overview and framework for data and information quality research, ACM Journal of Data and Information Quality 1 (2009).

[18] P. Milgrom, J. Roberts, Economics, Organization and Management, Prentice Hall, 1992.

[19] K. Orr, Data quality and systems theory, Communications of the ACM 41 (1998) 66–71.

[20] A. Powell, G. Piccoli, B. Ives, Virtual teams: a review of current literature and directions for future research, ACM SIGMIS Database 35 (2004) 6–36.

[21] L. Rao, K.-M. Osei-Bryson, An approach for incorporating quality-based cost–bene<sup>fi</sup>t analysis in data warehouse design, Information Systems Frontiers 10 (2008) 361–373.

[22] T.C. Redman, Improve data quality for competitive advantage, In: SloanManagement Review, Winter 1995, pp. 99–107.

[23] M. Stoica, N. Chawat, N. Shin, An Investigation of the Methodologies of Business Process Reengineering, In: Proceedings of the Information Systems Education Conference, 2003.

[24] A. Takayama, Mathematical Economics, Dryden Press, 1985.

[25] M. Van Alstyne, E. Brynjolfsson, S. Madnick, Why Not One Big Database? In: Principles for Data Ownership, Decision Support Systems, vol.15, 1995.

[26] R. Wang, H.B. Kon, Towards Total Data Quality Management (TDQM), In: Information Technology in Action: Trends and Perspectives, Prentice Hall, Englewood Cliffs, NJ, 1993, pp. 179–197.

[27] R. Wang, V.C. Storey, C. Firth, Data quality research: a framework, survey, and analysis, IEEE Transactions on Knowledge and Data Engineering 7 (1995) 835–842.

[28] K. Weber, B. Otto, H. Oesterie, One size does not <sup>fi</sup>t all — a contingency approach to data governance, ACM Journal of Data and Information Quality 1 (2009).

[29] M. Weske, Business Process Management: Concepts, Languages, Architectures Springer, 2010.

Rajiv Dewan is the Senior Associate Dean for Faculty and Research, Wm. E. Simon Graduate School of Business Administration, University of Rochester. He has research interests in information technology and strategy and in managing information systems in organizations.

Veda C. Storey is the Tull Professor of Computer Information Systems, J. Mack Robinson College of Business, Georgia State University. She has teaching and research interests in the Semantic Web, data management, conceptual modeling, and knowledge management

Professor Freimer, is professor of operations and computer information systems, Wm. E. Simon Graduate School of Business Administration, University of Rochester. He has teaching and research interests in applied probability and optimization. He applies his work to the analysis of problems in information systems and marketing. His work appears in management, engineering, economics, statistics and mathematics journals.
