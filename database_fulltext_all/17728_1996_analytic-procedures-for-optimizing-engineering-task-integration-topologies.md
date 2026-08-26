---
otero_id: 17728
otero_key: "JT3KF6B4"
title: "Analytic procedures for optimizing engineering task integration topologies"
authors: "Jason D. Papastavrou; Shimon Y. Nof"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00028-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analytic procedures for optimizing engineering task integration topologies $^{1}$

Jason D. Papastavrou, Shimon Y. Nof

School of Industrial Engineering, Purdue University, West Lafayette, IN 47097, USA

## Abstract

Decision making, control and information processing for large scale systems are designed and implemented in a distributed manner. Decision integration is a method to improve the quality of decision making. This research effort builds on previous results in attempting to establish the theoretical foundation of operational decision integration for such systems. Properly designed integration always improves the quality of the decisions; this is demonstrated through the use of a distributed hypothesis testing model. The problem of organizing decision making agents into architectures of integration is addressed by analyzing several elementary decision architectures for organizations, and comparing their performance. Explicit algorithmic procedures are developed to determine the optimal decision integration methods for a variety of organizations. Five motivating examples are presented to explicitly demonstrate the effectiveness of the algorithms. These procedures constitute the fundamental building blocks for analyzing the architectures of larger more realistic systems.

Keywords: Integration process; Distributed manufacturing; Decision architectures; Optimization procedures; Hypothesis testing

## 1. Introduction and motivation

The motivation for the research reported here is as follows: Technologically, engineers and planners in modern production facilities with integrated computer systems for manufacturing, assembly, or maintenance can already benefit by interacting and communicating about their requirements, status, progress, delays, etc.. Therefore, they can potentially collaborate to increase the reliability and productivity of their production plans and operations. For instance, computer integrated product design and process information can provide the input for joint planning of production and quality control tasks, or resource allocation.

Industry is well aware of the important advantages of teamwork for competitiveness. There are several trends that motivate integration and teamwork, mainly: (1) the trend toward concurrent engineering design and life-cycle product engineering (e.g., [3,15]); (2) the trend toward “agile cooperation” within and between companies to benefit by sharing their scarce resources and limited personnel (e.g., [14,22]).

A related trend is the development of computer integrated tools, computer systems and expert systems to support team activities. For instance, the emergence of GDSS, group decision support systems, and MDSS, manufacturing decision support systems. (GDSS is oriented to higher level planning and MDSS more to operational planning and control.)

In fact, there exists a great number of recent publications that address the same issues and deal with very similar problems. But in these, the focus is on particular applications and not on the development of general systematic techniques for planning and optimizing the collaborative integration of engineering information and activities. For example, the relationship between organizational development and MIS/DSS was studied since organizational change quite often requires the existing information systems to be reconstructed $[23]$ . A method for the integration of different methods and techniques and the support of public decision making was considered for applications in urban traffic management $[4]$ . Successful and unsuccessful Expert Systems were compared in $[7]$ . Decision making methodologies for hierarchical structures were considered for a specific public health service application $[5]$ . A framework for the design of a Decision Support System for a strategic manpower planning problem of airline pilots was presented in $[29]$ , and the functional architectures of a production planning knowledge-based system were discussed in $[2]$ .

The problem is to develop systematic techniques for planning and even optimizing the collaborative integration of engineering information and activities. In distributed facilities, for instance, where planners are at different, remote locations, such integrated planning is critical for successful accomplishment of production and quality missions. However, the practice of engineering teams in industry and, in particular, the integration with computer systems is typically ad hoc. As a result, there are communication gaps, problems associated with time delays, lack of the right information when engineering decisions must be made, and similar inefficiencies. Clearly, this is not conducive to competitiveness. There is a need to investigate and understand the integration and collaboration processes and provide theory and models for their effective design and implementation.

The objective of this research is to investigate the collaboration and integration processes in distributed manufacturing. Distributed manufacturing is considered both within and between plants of the same company. The focus is on computer-assisted product design, production planning and quality functions, and in particular on one area of engineering task integration: mathematical modeling and computer-assisted engineering team organizations with the objective to optimize the timely benefits of the collaborative integration.

In a previous article [19] the fundamental elements of integration in distributed manufacturing were defined. They include:

1. The Integration Operator that defines the conversion of information inputs into certain decisions, designs or recommendations.

2. The Integration Procedure or algorithm that specifies step-by-step how the information inputs are integrated.

3. The Input / Output Streams of information, including, data, decisions, signals, materials, and general knowledge.

4. The Distributed Decision Making Entity which is defined as the most basic and elementary, autonomous unit of the distributed manufacturing organization.

5. The Integration Time that characterizes the constraint on how much information can be gathered and, during a given period, be processed; hence, the quality of the integrated output.

6. The Integration Models that provide the mathematical framework to analyze and optimize the whole integration process and its outcome.

Papastavrou and Nof also described how distributed hypothesis testing models can be applied to design engineering decision making architectures $[19]$ . They stressed the practical significance of the results on decentralized decision making in a hypothesis testing environment to distributed manufacturing. For design and control decisions in manufacturing, it was shown that when there are two DCs in the configuration, a tandem architecture would be preferred. For concurrent engineering, for instance, the concurrency of the considerations should still be evaluated in a tandem decision process. A globally dominant architecture does not exist for systems consisting of more than two DCs. In particular, the optimal architecture for organizations consisting of three DCs is either the two-consultant architecture or the tandem architecture. The two-consultant architecture is generally considered superior, when issues of robustness, resiliency and speed of response come into the picture.

It was also shown that for large systems, while the tandem architecture demonstrates great inefficiency under a multitude of decision protocols, the parallel architecture achieves good performance. Moreover, if the parallel system consists of identical DCs, they can all be restricted to employing identical decision rules without any deterioration on the system performance asymptotically. This suggests that it is worthwhile to restrict similar DCs at the same level of command to employing identical decision rules, because the reduction in complexity outweighs the deterioration in performance. Also, it was argued that the optimal architecture of a large distributed system should be diversified more horizontally than vertically, but the optimal mix remains a topic for future research. With respect to a manufacturing context, the conclusions of their analysis indicate that for small organizations hierarchical architectures are preferable. But as organizations grow, less hierarchical and more hierarchical architectures should be preferred. They conclude that a company should carefully examine the optimality of its decision integration architecture, keeping in mind that intuitive does not necessarily imply optimal.

This article builds on the previous foundation and elaborates on specific optimization procedures for selecting the best engineering task integration topologies. Five examples representing typical manufacturing situations are included, and the step-by-step optimization procedures are presented. The factors that influence the optimal topology and their effects are discussed analytically.

## 2. The optimization procedure

In this section the procedure for determining the optimal integration topology is presented through a series of examples motivated by realistic manufacturing situations. With the first example, the basic concepts associated with the models of engineering task integration are introduced. The basic concepts include the engineering task states, the prior probabilities, the observations, the task decision (or recommendation), the task decision rules, the ROC curve, the probability of detection and the probability of false alarm, the task decision threshold, and the optimization procedures. These concepts will be used repeatedly in the subsequent examples to analyze distributed manufacturing environments.

In the second example, the optimal topology for two distributed engineering tasks is obtained. In the next example, the optimal configuration for two distributed engineering tasks within a given tandem topology is determined; also, the dependence of this configuration on the communication protocols is established. In the fourth example, the parallel topology for two distributed engineering tasks is analyzed. In the last example, the optimal topology for three distributed engineering tasks is discussed, and generalizations are drawn for larger topologies.

## 2.1. Example 1: The basic engineering task integration problem

Consider an engineer (ME) who supervises a manufacturing facility of a certain product.

## 2.1.1. States and prior probabilities

Assume that there are two mutually exclusive states for the manufacturing system: it may be in satisfactory operating condition (state $S_{0}$ ), or it may be in a deteriorated operating condition (state $S_{1}$ ). If the system is in satisfactory operating condition, no action is needed by the ME. But if the system is in a deteriorated operating state, the ME must shut it down immediately in order to service and restore it to good operating order; otherwise, the condition will deteriorate further with costly consequences. Assume that the ME has some a priori probabilistic knowledge for the states of the system; for example suppose that the system is in deteriorated operating state 5% of the time and is in satisfactory operating condition the remaining 95% of the time (i.e., $P(S_{1}) = 0.05$ and $P(S_{0}) = 0.95$ ).

## 2.1.2. Observations

Every so often, say once every time period, the ME considers all the information that he or she has available and, based on this information, decides whether to shut the production line down in order to service it (because it is believed to be in deteriorated operating condition), or to take no action (because it is believed to be in satisfactory operating condition). The information available to the ME is obtained from a variety of sources; for example, by personal observations, readings of various instruments, or communications from other operators or engineers. Clearly, the information depends on the true state of the production line; for example, one expects to obtain different instruments readings if the production line is in good operating condition than if it is not. Furthermore, this information is noisy (i.e., not 100% accurate); for example, instruments readings may not unequivocally identify the true condition of the production line, or the communications from other engineers may be ambiguous.

In this example, for simplicity assume all the information available to the ME consists of a discrete random variable $(Y)$ , henceforth called the observation. Suppose Y can have one of three different values: Y=0 indicates the system is highly likely in satisfactory operating condition, Y=1 indicates that the system is probably in deteriorating operating condition, or Y=2 indicates the system is highly likely in deteriorating operating condition. As stated above, the observation, or rather the probability distribution of the observation, depends on the true state of the system (see Table 1). For instance, if the facility is in satisfactory operating condition (state $S_{0}$ ) then Y=0 occurs with probability 0.4, but if it is in deteriorating condition (state $S_{1}$ ) then Y=2 occurs with probability 0.3.

## 2.1.3. Task decisions and task decision rules

Every time the ME receives a new observation he or she must decide: either take no action $(u=0)$ , or interrupt the system so that it can be serviced $(u=1)$ . Every decision has certain consequences and hence costs associated with it; the costs depend on both the decision and the state of the system. If the system is in satisfactory operating condition (state $S_{0}$ ), there is obviously no cost incurred with no action $(u=0)$ because production is uninterrupted; but there is an unnecessary cost incurred if the decision is to interrupt and service the system $(u=1)$ . On the other hand, if the system is in deteriorating condition (state $S_{1}$ ), only the service cost is incurred if the decision is to interrupt $(u=1)$ , and a big cost is incurred if the decision is to take no action $(u=0)$ because the condition of the system will deteriorate further and it will be very expensive to repair. This indicates that there does not exist a (trivial) decision that is optimal for both states of the system; it is better to decide u=0 if $S_{0}$ is the true state, and to decide u=1 if $S_{1}$ is the true state. Therefore, the ME has to consider her observation and try to make the best possible decision for the given costs. Denote by $C(u,S_{i})$ , the cost associated with task decision u when $S_{i}$ is the true state of the system $(u=0,1,\text{and }i=0,1)$ .

Probability mass functions for the observation of the DE in example 1

<table><tr><td> $\mathbf{P}(Y|S_0)$ </td><td>0.4</td><td>0.5</td><td>0.1</td></tr><tr><td> $P(Y|S_1)$ </td><td>0.1</td><td>0.6</td><td>0.3</td></tr><tr><td>Y</td><td>0</td><td>1</td><td>2</td></tr></table>

As was just mentioned, the task decision depends only on the observation of the ME. This leads to the heart of the problem: determine the optimal task decision rule $\gamma^{*}$ for the decision u, that is the decision rule that minimizes the expected cost incurred by the engineering system. The task decision rule is a function that considers each possible observation Y and produces a decision u.

Remark. Then, the problem can be formalized as follows:

$$
\begin{array}{l} \min _ {\gamma} E [ C [ u, S _ {i} ] ] \\ = \sum_ {i = 0} ^ {1} \sum_ {Y = 0} ^ {2} \sum_ {u = 0} ^ {1} P (S _ {i}) P (Y | S _ {i}) P (u | Y) C (u, S _ {i}), \end{array}\tag{1}
$$

where $u = \gamma(Y)$ , and $E(\cdot)$ denotes the expectation. By making the substitution $P(u = 0|S_i) = 1 - P(u = 1|S_i)$ , Eq. (1) can be rewritten as:

$$
\begin{array}{l} \min _ {\gamma} E [ C [ u, S _ {i} ] ] \\ = P (S _ {0}) C (0, S _ {0}) + P (S _ {1}) C (0, S _ {1}) \\ \quad + \sum_ {i = 0} ^ {1} \sum_ {Y = 0} ^ {2} P (S _ {i}) P (Y | S _ {i}) P (u = 1 | Y) \\ \times [ C (1, S _ {i}) - C (0, S _ {i}) ]. \end{array}\tag{2}
$$

Observe that the first two terms of the right hand side of Eq. (2) are constants; therefore, they do not influence the minimization in any way and can be omitted.

Table 2  
Task decision rules for the DE in example 1 and the corresponding points on the ROC curve:

<table><tr><td></td><td> $(P_F, P_D)$ </td></tr><tr><td> $\gamma_1(Y) = 0 \text{ for } Y = 0, 1, 2$ </td><td>(0.0, 0.0)</td></tr><tr><td> $\gamma_2(Y) = 0 \text{ for } Y = 0, 1 \text{ and } 1 \text{ for } Y = 2$ </td><td>(0.1, 0.3)</td></tr><tr><td> $\gamma_3(Y) = 0 \text{ for } Y = 0, \text{ and } 1 \text{ for } Y = 1, 2$ </td><td>(0.6, 0.9)</td></tr><tr><td> $\gamma_4(Y) = 1 \text{ for } Y = 0, 1, 2$ </td><td>(1.0, 1.0)</td></tr></table>

Consider the four possible deterministic task decision rules that can be employed by the ME of Table 1 (Table 2).

(1) If the ME employs task decision rule $\gamma_{1}$ , the ME always decides not to take any action (u=0) independent of the observation received (i.e., whenever the ME receives Y=0, 1, or 2).

(2) If the ME employs task decision rule $\gamma_{2}$ , the ME decides not to interrupt the system (u=1) only when he or she believes that the system is very likely in deteriorating operating condition (i.e., whenever the ME receives Y=2), and the ME takes no action otherwise.

(3) If the ME employs task decision rule $\gamma_{3}$ , the ME decides not to take any action (u=0) when he or she believes that the system is very likely in good operating condition (i.e., whenever the ME receives Y=0), and the ME interrupts the system otherwise.

(4) If the ME employs task decision rule $\gamma_{4}$ , the ME always decides to interrupt the system (u=1) independent of the observation received (i.e., whenever the ME receives Y=0, 1, or 2).

## 2.1.4. The ROC curve

Associated with every distributed engineering unit, the individual ME in our example, is a curve called the Receiver Operating Characteristic (ROC) curve. This is a powerful tool employed in a variety of applications from Signal Detection Theory [28] to Human Factors [12]. The ROC curve provides the probability of detection $P_{D}$ as a function of the probability of false alarm $P_{F}$ and describes completely the capability of a decision making entity. The probability of detection is the probability of deciding u = 1 given that the true state of the environment is $S_{1}$ , while the probability of false alarm is the probability of deciding u = 1 given that the true state of the environment is $S_{0}$ . The nomenclature comes from Signal Detection Theory where state $S_{1}$ corresponds to the presence of a problem target and state $S_{0}$ corresponds to the absence of the target. When the decision is to take action to solve the problem (u = 1) and a target is actually present (state $S_{1}$ ), then target detection is achieved; when the decision is to take action to solve the problem (u = 1) and a target is not present (state $S_{0}$ ), then false alarm takes place. The ROC curve can be obtained theoretically in the form of a pair of parametric equations [28], and experimentally for engineering units [12].

Remark. Using the notation introduced in the previous paragraph, the minimization of Eq. (2) can be written as:

$$
\begin{array}{l} \min _ {\gamma} E [ C [ u, S _ {i} ] ] \\ = P (S _ {0}) C (0, S _ {0}) + P (S _ {1}) C (0, S _ {1}) \\ \quad + \min _ {(P _ {F}, P _ {D}) \text {in} R O C} \left\{P (S _ {0}) P _ {F} [ C (1, S _ {0}) - C (0, S _ {0}) ] \right. \\ \quad + P (S _ {1}) P _ {D} [ C (1, S _ {1}) - C (0, S _ {1}) ] \}. \end{array}\tag{3}
$$

Every task decision rule determines a unique point on the ROC curve. Returning to our example, when task decision rule $\gamma_{1}$ is employed, the point $(P_{F}, P_{D}) = (0, 0)$ of the ROC curve is determined since the ME always decides u = 0 (and, thus, never decides u = 1). When task decision rule $\gamma_{2}$ is employed, the point $(P_{F}, P_{D}) = (0.1, 0.3)$ is determined since the ME decides u = 1 only if she receives Y = 2, and the ME receives Y = 2 with probability 0.3 if $S_{0}$ is true and with probability 0.5 if $S_{1}$ is true. When task decision rule $\gamma_{3}$ is employed, the point $(P_{F}, P_{D}) = (0.6, 0.9)$ is determined since the ME decides u = 1 if he or she receives Y = 1 or Y = 2, and the ME receives that with probability 0.6 (= 0.5 + 0.1) if $S_{0}$ is true and with probability 0.9 (= 0.6 + 0.3) if $S_{1}$ is true. When task decision rule $\gamma_{4}$ is employed, the point $(P_{F}, P_{D}) = (1, 1)$ is determined since the ME always decides u = 1. We, thus, obtain the ROC curve of Fig. 1 that completely describes the ME.

All ROC curves have several useful properties. They are concave curves that go from $(0, 0)$ to $(1, 1)$ .

Table 3  
![](/api/attachments/JT3KF6B4/fulltext/images/d69f25646daff8549aeae63287995f7461ae8a75a343396737ff94d408b62c7c.jpg)  
Fig. 1. ROC curve for the DE in example 1.

They also provide a graphical method to solve the minimization of Eq. (3), and, hence, the original decision problem. First, calculate the task decision threshold $\eta$ , which depends only on given parameters (the prior probabilities and the costs) as follows:

$$
\eta = \frac {P (S _ {0}) [ C (1 , S _ {0}) - C (0 , S _ {0}) ]}{P (S _ {1}) [ C (0 , S _ {1}) - C (1 , S _ {1}) ]}.\tag{4}
$$

Then, consider a line of slope $\eta$ and “shift it upwards”. (Formally, consider the line $P_{D} = \eta P_{F} + k$ as k increases.) The last point(s) that belongs in the intersection of the ROC curve and the line is the solution to the problem [28].

The ROC curve also provides a good way of ranking the engineering decision making entities. The higher the ROC curve the better the engineering decision making entity, because for the same level of false alarm, a higher probability of detection can be achieved. Thus, A is better than B in Fig. 2a. But, if the ROC curves intersect (Fig. 2b) such an unequivocal statement cannot be made; for some levels of false alarm A is better than B, and for the rest B is better than A.

![](/api/attachments/JT3KF6B4/fulltext/images/84554c9f1b7c307f425fd2939caec8ed80e3bc8cec5f00a44dffd05b5aeae7da.jpg)

![](/api/attachments/JT3KF6B4/fulltext/images/7b26f83268be805bc89ac1c2009da0303a579228c77529855b0530ab2fadba43.jpg)  
Fig. 2. Ranking engineering decision making entities: (a) A better than B, (b) no unequivocal ranking exists.

## 2.1.5. The environment

In the distributed hypothesis testing framework, the environment consists of factors that are endogenous and exogenous to the organization. The endogenous factors consist of the observations because these can be controlled by the organization; for example, the accuracy of the observations, and thus the performance of the organization, can be improved through training. These endogenous factors are captured by the ROC curve that corresponds to the ME. On the other hand, the exogenous factors are external to the organization because they cannot be controlled by the members of the organization. These include the states, the prior probabilities, and the misclassification costs; all these are captured in the calculation of the task decision threshold on Eq. (4). They also include the communication protocols (which are not relevant in this example because there exists only a single engineer); they are captured in the form of the solution equations.

These factors completely describe the environment in which an organization operates in this framework. In order to be able to optimize its performance, an organization needs to know precisely the exogenous factors. Given the exogenous factors, the organization can determine the optimal decision rules that can be implemented using its observations.

## 2.1.6. A “brute force” optimization approach

Considering each and every possible task decision rule (i.e., using complete enumeration) and calculating the expected cost associated with it, the optimal task decision rule that yields the minimum expected cost is obtained. For this example, consider the two prior probability and cost assignments for the problem presented in Table 3. For example, in assignment 1, $P(S_{0}) = 0.95$ implies that 95% of the time the system is in good operating condition (state $S_{0}$ ), and $C(0, S_{1}) = 100$ implies that a cost of one hundred units is incurred if the system is in deteriorating condition (state $S_{1}$ ) and the ME does not take any action (u=0). The expected costs incurred by the manufacturing system for each of the four task decision rules and each assignment are presented in Table 4. For example, for assignment 1 and task decision rule $\gamma_{2}$ , a cost of 4.05 is incurred by the system on the average; this can be calculated from Eq. (3) by substituting the values of the prior probabilities and the cost from assignment 1 and substituting the point of the ROC curve ( $P_{F}, P_{D}$ ) = (0.1, 0.3) which corresponds to task decision rule $\gamma_{2}$ .

Cost and prior probability assignments for example 1

<table><tr><td></td><td> $P(S_0)$ </td><td> $P(S_1)$ </td><td> $C(0, S_0)$ </td><td> $C(1, S_0)$ </td><td> $C(0, S_1)$ </td><td> $C(1, S_1)$ </td><td> $\eta$ </td></tr><tr><td>Assignment 1</td><td>0.95</td><td>0.05</td><td>0</td><td>5</td><td>100</td><td>5</td><td>1.0</td></tr><tr><td>Assignment 2</td><td>0.75</td><td>0.25</td><td>0</td><td>10</td><td>50</td><td>30</td><td>1.5</td></tr></table>

From Table 4, the optimal task decision rule (i.e., the task decision rule that minimizes the average cost) for assignment 1 is task decision rule $\gamma_{3}$ with a corresponding expected cost of 3.575. Also, the optimal task decision rule for assignment 2 is task decision rule $\gamma_{2}$ with a corresponding expected cost of 11.75.

## 2.1.7. The efficient optimization procedure

A formal and efficient algorithm, that determines the optimal point of the ROC curve and consequently the optimal task decision rule and optimal cost for the problem described above, is presented. This algorithm is an adaptation of the classical solution methodology (i.e., likelihood ratio test) for hypothesis testing (for example, see [28]).

## ALGORITHM I

Step 0: Consider the given cost assignment and prior probabilities; calculate $\eta$ using Eq. (4).

Step 1: Determine the point $(P_{F}^{*}, P_{D}^{*})$ of the ROC curve at which the line $P_{D} = \eta P_{F} + k$ is tangent to the ROC curve; if there exist more that one such points, select one arbitrarily.

Step 2: Calculate the optimal expected cost associated with the optimal point $(P_{F}^{*}, P_{D}^{*})$ using Eq. (2).

The solution to the problem can be obtained more efficiently using the Algorithm I. For assignment 1 the task decision threshold is $\eta=1.0$ ; consider the line $P_{D}=1.0P_{F}+k$ , as k increases. The point of the ROC curve that corresponds to the maximum value of k is $(P_{F}^{*}, P_{D}^{*})=(0.6, 0.9)$ (Fig. 3). To determine this, note that the slope of the line segment from (0.1, 0.3) (the previous point of the ROC curve) to (0.6, 0.9) is 3 (>1), and that the slope from (0.6, 0.9) to (1, 1) (the next point of the ROC curve) is 0.25 (<1). As was explicitly discussed above, $(P_{F}^{*}, P_{D}^{*})=(0.6, 0.9)$ is achieved when the ME employs task decision rule $\gamma_{3}$ ; thus, task decision rule $\gamma_{3}$ is optimal for assignment 1.

Expect costs associated with each task decision rule and cost assignment

<table><tr><td></td><td> $\gamma_1$ </td><td> $\gamma_2$ </td><td> $\gamma_3$ </td><td> $\gamma_4$ </td></tr><tr><td>Assignment 1</td><td>5.0</td><td>4.05</td><td>3.575</td><td>5.0</td></tr><tr><td>Assignment 2</td><td>12.5</td><td>11.75</td><td>12.5</td><td>15.0</td></tr></table>

![](/api/attachments/JT3KF6B4/fulltext/images/675fe3a06a71f019e5fc87f23cb25f442b734175eeef5827679b65036b5b77f6.jpg)  
Fig. 3. Graphical solution of the problem for the furst cost assignment in example 1.

Similarly, for assignment 2 the task decision threshold is $\eta=1.5$ . Then the optimal point is the point $(P_{F}^{*}, P_{D}^{*})=(0.1, 0.3)$ , because the slope of the line segment from $(0, 0)$ to $(0.1, 0.3)$ is $3 (>1.5)$ , and the slope of the line segment from $(0.1, 0.3)$ to $(0.6, 0.9)$ is $3 (>1)$ . Thus, $\gamma_{2}$ is the optimal task decision rule for this assignment.

In summary, a simple example was used to introduce the basic concepts associated with these models of decision integration. They include the engineering task states, the prior probabilities, the observations, the task decision, the task decision rules, the ROC curve, the probability of detection and of false alarm, the decision threshold, and the optimization procedures. These concepts will be used repeatedly in the sequel to analyze distributed manufacturing systems.

## 2.2. Example 2: topology for two distributed engineering tasks

Consider the first example that involves more than one decision making entity, that is the first distributed engineering integration topology. The objective is to obtain the optimal topology of a facility that consists of two distributed engineering tasks.

![](/api/attachments/JT3KF6B4/fulltext/images/997488cab5becc32df26297afdc10655f3b9dcd10bf32bec7fbaa9dd00c8c311.jpg)  
Fig. 4. Topologies for two distributed engineering tasks: (a) Tandem topology, (b) Parallel topology.

Consider a development engineer (DE) and a manufacturing engineer (ME) who have to decide on whether to go ahead with the production of a new line of a certain product. There are two different ways to organize these two engineers (or engineering groups): (1) the tandem topology (Fig. 4a), or the parallel topology (Fig. 4b).

The Tandem Topology. In the tandem topology, the ME is designated by the manager as the design team leader (DTL). The DE has to report her opinion to the ME who is responsible for the final task decision. The ME considers the opinion of the DE together with his or her own information and then decides on whether to go ahead with the production of the new line.

The Parallel Topology. In the parallel topology, both the ME and the DE make their individual task decisions, which they relate directly to the manager. In this case, the manager is the design team leader and is responsible for the task final decision. But, assuming the manager has many other responsibilities and time constraints he or she cannot analyze the situation in depth, and must rely exclusively on the communications from the engineers.

The problem is to determine which topology is better. There exist some engineering task integration problems that can be solved optimally, without having to resort to complicated mathematical analysis, by using logic; the problem considered in this example falls precisely into this category. The tandem topology is shown to be always better; a formal proof can be found in [16].

Suppose that the engineering team is organized in the parallel topology and that $\gamma_{1}$ , $\gamma_{2}$ and $\gamma_{3}$ are the optimal task decision rules for the DE, the ME and the DTL, respectively; that is, given that the team members are organized in the parallel topology with the manager as the DTL, $\gamma_{1}$ , $\gamma_{2}$ and $\gamma_{3}$ are the best possible task decision rules that they can employ. It will be argued that the tandem topology can always duplicate the optimal performance of the parallel topology.

For this, consider the following task decision rules assignment for the two engineers in the tandem topology. The DE employs task decision rule $\gamma_{1}$ , the same optimal task decision rule for the DE in the parallel topology. Then, the ME, who is also the DTL in this case, makes the final task decision in two steps. In the first step, the ME considers only his or her own personal data and makes a preliminary task decision using decision rule $\gamma_{2}$ ; then the ME considers the task decision of the DE and his or her own preliminary task decision and, just as the DTL did in the parallel topology, he or she makes the final task decision on whether to go ahead with the new production line using task decision rule $\gamma_{3}$ . Therefore, the tandem topology can always duplicate the optimal performance of the parallel topology and, since in some cases it can do even better, the tandem topology is optimal.

In Example 5 the use of logic to analyze and compare the performance of different engineering task integration topologies will be discussed again.

## 2.3. Example 3: assigning engineering tasks within a given integration topology

Determining the optimal topology is only the first step towards determining the optimal engineering task integration topology. Once a topology has been selected the optimal configuration of the team, that is the optimal placement of the engineering decision tasks within the chosen topology, has to be determined as well. In this example, the optimal configuration for the topology that consists of two engineering tasks in tandem is discussed.

Consider again a development engineer (DE) and a manufacturing engineer (ME) who have to decide on whether to go ahead with the production of a new product or whether to abandon the project. Since for two decision engineering tasks, the tandem topology is always superior to the parallel topology (see Example 2), it has been decided that the tandem topology will be employed. The problem is to decide which of the two engineers should be designated as the design team leader (DTL) and, therefore, carry the burden of the final task decision: the DE (Fig. 5a) or the ME (Fig. 5b)? To clearly demonstrate the difficulties associated with this problem, only a specific instance of the problem in which one of the engineers is unequivocally better than the other in the ROC sense needs to be analyzed.

![](/api/attachments/JT3KF6B4/fulltext/images/64894b18e0259154ac807efe19c7497fc864aca2813d7f54b2c4d143c7bcd825.jpg)  
Fig. 5. Possible configurations for tandem topology in example 3: (a) The ME is the DTL, (b) the DE is the DTL.

Assume that there are two mutually exclusive engineering task states for the environment as far as the introduction of the new product is concerned; either the state of the environment is good (state $S_{1}$ ) and the product should be introduced, or it is bad (state $S_{0}$ ) and the project should be abandoned or at least delayed. Further assume that the state of the environment completely describes all the factors that can influence the success or failure of the new product (e.g., manufacturing capability, product attractiveness, market conditions and prices), and it can either be conducive to the new product or not. Also assume that the costs and prior probabilities are known.

Each engineer performs an extensive analysis to form his or her own personal assessment of the situation. The assessment (i.e., observation) of the DE can be summarized as follows: the DE can come to the conclusion that either the product will most likely be a failure $Y=0$ , or the product will probably be a failure $Y=1$ , or the product will probably be a success $Y=2$ , or the product will most likely be a success $Y=3$ . The conditional probability mass functions of the DE's observation given the true state of the environment are presented in Table

Probability mass functions for the observation of the $DE^{a}$ and $ME^{b}$ in example 3

<table><tr><td> $P(Y|S_0)^a$ </td><td>0.6</td><td>0.2</td><td>0.1</td><td>0.1</td></tr><tr><td> $P(Y|S_1)^a$ </td><td>0.1</td><td>0.1</td><td>0.2</td><td>0.6</td></tr><tr><td> $Y^a$ </td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td> $P(X|S_0)^b$ </td><td>0.5</td><td>0.4</td><td>0.1</td><td></td></tr><tr><td> $P(X|S_1)^b$ </td><td>0.1</td><td>0.5</td><td>0.4</td><td></td></tr><tr><td> $X^b$ </td><td>0</td><td>1</td><td>2</td><td></td></tr></table>

5; for example, the probability that the assessment of the DE is that the product will probably be a success $Y=2$ , given that the state of the environment is good for the introduction of the product $S_{1}$ is 0.2. The corresponding ROC curve for the DE is presented in Fig. 6a.

Similarly, the assessment of the ME can be summarized as follows: the ME can come to the conclusion that either the product will most likely be a failure (X = 0), or the situation could go either way (X = 1), or the product will most likely be a success (X = 2). The conditional probability mass functions of the ME's observation given the true state of the environment are presented in Table 5 and the associated ROC curve is presented in Fig. 6. The DE is better than the ME, since the ROC curve of the DE lies above the ROC curve of the ROC curve of the ME (Fig. 7).

Assume that only one of two messages can be communicated to the DTL; either that the system should go ahead with the production of the new product ( $\nu=1$ ) or that the project should be abandoned ( $\nu=0$ ). The problem is to determine the configuration that minimizes the expected cost for each of the two assignments of costs and prior probabilities of Table 6. Since the DE is better than the ME, it seems intuitive (and several people had conjectured so in the literature) that the DE should be entrusted with the final task decision. Intuition is reinforced further if one considers that the DE's observation takes four distinct values, while the ME's observation takes only three distinct values. Therefore, it seems intuitive that the information lost by summarizing (compressing) the observation of the DE into the binary communication message is more than the information lost by summarizing the observation of the ME into the binary communication message; thus, the ME should be designated as the DTL. But, it will be shown that the optimal configuration depends not only on the characteristics of the system (e.g., the engineers involved), but also on factors that are external to the organization; that is factors that the system cannot control, like the costs and the prior probabilities.

![](/api/attachments/JT3KF6B4/fulltext/images/28745469dab4a4f95384db053864f1d1a701654c6a959dfa73ce69fe7b438d91.jpg)

![](/api/attachments/JT3KF6B4/fulltext/images/8aa768240c8d6d80407641d49412d32cd8b6131a36be06eb8bcab62394ed397a.jpg)  
Fig. 6. ROC curves for the DE and the ME in example 3: (a) ROC curve of the ME, (b) ROC curve of the DE.

![](/api/attachments/JT3KF6B4/fulltext/images/c04be201b60b68d9b4b4ebf17eb762da6cf93b924e39818f83dd582ab7166ee4.jpg)  
Fig. 7. Comparison of the ROC curves of the DE and the ME in example 3.

## 2.3.1. A “brute force” optimization approach

Consider the first cost and prior probability assignment of Table 6. The problem is to determine the optimal configuration for the DE and the ME in the tandem topology. Define by $(P_{F}^{0}, P_{D}^{0})$ the point of the ROC curve that the DTL will employ when the message from the other engineer is to abandon the project $(\nu=0)$ , and by $(P_{F}^{1}, P_{D}^{1})$ the point of ROC curve that the DTL will employ when the message from the other engineer is to go ahead with the project ( $\nu=1$ ). This implies that if the message communicated to the DTL is to go ahead with the project, the DTL decides to go ahead (u=1) with probability $P_{F}^{1}$ when the state of the environment is bad ( $S_{0}$ ), and with probability $P_{D}^{1}$ when the state of the environment is good ( $S_{1}$ ). Further, define by ( $P_{F}^{c}$ , $P_{D}^{c}$ ) the point of the ROC curve that the other engineer employs to communicate his or her message to the DTL. This implies that the message communicated to the DTL is to go ahead with the project ( $\nu=1$ ) with probability $P_{F}^{c}$ when the state of the environment is bad, and with probability $P_{D}^{c}$ when the state of the environment is good.

Table 6  
Cost and prior probability assignments for example 3

<table><tr><td></td><td> $P(S_0)$ </td><td> $P(S_1)$ </td><td> $C(0, S_0)$ </td><td> $C(1, S_0)$ </td><td> $C(0, S_1)$ </td><td> $C(1, S_1)$ </td><td> $\eta$ </td></tr><tr><td>Assignment 1</td><td>0.50</td><td>0.50</td><td>65</td><td>120</td><td>50</td><td>0</td><td>1.1</td></tr><tr><td>Assignment 2</td><td>0.25</td><td>0.75</td><td>2</td><td>110</td><td>100</td><td>0</td><td>0.36</td></tr></table>

First, the minimum expected cost for the system if the DE is the DTL is determined. There are only two sensible task decision rules that the ME can employ for his or her communication message; these are presented in Table 7. The first task decision rule is to advise the DTL to go ahead with the project ( $\nu=1$ ) if his or her own assessment is that the product will most likely be a success (X=2), and to otherwise abandon the project; this corresponds to operating at the point ( $P_{F}^{c}, P_{D}^{c}$ ) = (0.1, 0.4) of the ROC curve. The second task decision rule is to advise the DTL to abandon the project ( $\nu=0$ ) if her own assessment is that the product will most likely be a failure (X=0), and to otherwise go ahead with the project; this corresponds to operating at the point ( $P_{F}^{c}, P_{D}^{c}$ ) = (0.5, 0.9) of the ROC curve. These are the only sensible task decision rules, because if the ME always communicated $\nu=0$ or $\nu=1$ to the DTL, the message would not provide the DTL with any information.

Then, the task decision rules of the DTL, that is the DE, are considered. The DTL may decide to completely ignore the communicated message. In that case he or she has five task decision rules to choose from (the first five in Table 8). For example, if the DTL employs task decision rule $\gamma_{2}$ he or she decides to go ahead with the project $(u=1)$ if his or her assessment is that the project will most likely be a success $(Y=3)$ , and he or she decides to abandon the project otherwise; in this case $(P_{F}^{0}, P_{D}^{0}) = (P_{F}^{1}, P_{D}^{1}) = (0.1, 0.6)$ .

Table 7  
Task decision rules for the ME when the DE is the DTL, and the corresponding points of the ROC curve

<table><tr><td></td><td> $(P_{F}^{c}, P_{D}^{c})$ </td></tr><tr><td> $\gamma_{1}^{m}(X)=0 \text{ for } X=0, 1 \text{ and } 1 \text{ for } X=2$ </td><td>(0.1, 0.4)</td></tr><tr><td> $\gamma_{2}^{m}(X)=0 \text{ for } X=0 \text{ and } 1 \text{ for } X=1, 2$ </td><td>(0.5, 0.9)</td></tr></table>

On the other hand, the DTL may decide to take into consideration the message communicated from the ME. Then, there exist ten different sensible task decision rules that he or she may employ (six through fifteen in Table 8). For example, consider task decision rule $\gamma_{7}$ . If the communicated message is to abandon the project ( $\nu=0$ ), the DTL always decides to abandon the project (u=0) no matter what his or her own personal assessment is; thus, $(P_{F}^{0}, P_{D}^{0}) = (0, 0)$ . If the communicated message is to go ahead with the project ( $\nu=1$ ), the DTL decides to abandon the project if his or her personal assessment is that the project will most likely be a failure, or probably be a failure (Y=0, 1), and to abandon the project otherwise; thus, $(P_{F}^{1}, P_{D}^{1}) = (0.2, 0.8)$ . These are the only sensible task decision rules because the DTL should be more likely to decide to go ahead with the project (u=1) when the communicated message is to go ahead with the project ( $\nu=1$ ), than when the communicated message is to abandon the project ( $\nu=0$ ).

Thus, there exist twenty five different task decision rules for the system as a whole; five, if the DTL decides to ignore the communicated message, and ten task decision rules for each of the two possible task decision rules for the communicated message. For each of the twenty five choices the corresponding expected cost for the system can be calculated using the following equation:

$$
\begin{array}{l} E \big [ C (u, S _ {i}) \big ] \\ = P (S _ {0}) \big [ (1 - P _ {F} ^ {c}) \big [ (1 - P _ {F} ^ {0}) C (0, S _ {0}) \\ \quad + P _ {F} ^ {0} C (1, S _ {0}) \big ] + P _ {F} ^ {c} \big [ (1 - P _ {F} ^ {1}) C (0, S _ {0}) \\ \quad + P _ {F} ^ {1} C (1, S _ {0}) \big ] \big ] \\ \quad + P (S _ {1}) \big [ (1 - P _ {D} ^ {c}) \big [ (1 - P _ {D} ^ {0}) C (0, S _ {1}) \\ \quad + P _ {D} ^ {0} C (1, S _ {1}) \big ] + P _ {D} ^ {c} \big [ (1 - P _ {D} ^ {1}) C (0, S _ {1}) \\ \quad + P _ {D} ^ {1} C (1, S _ {1}) \big ] \big ] \\ = P (S _ {0}) C (0, S _ {0}) + P (S _ {1}) C (0, S _ {1}) \\ \quad + P (S _ {0}) \big [ (1 - P _ {F} ^ {c}) P _ {F} ^ {0} + P _ {F} ^ {c} P _ {F} ^ {1} \big ] \big [ C (1, S _ {0}) \\ \quad - C (0, S _ {0}) \big ] \\ \quad + P (S _ {1}) \big [ (1 - P _ {D} ^ {c}) P _ {D} ^ {0} + P _ {D} ^ {c} P _ {D} ^ {1} \big ] \\ \quad \times \big [ C (1, S _ {1}) - C (0, S _ {1}) \big ]. \end{array}\tag{5}
$$

This first equality can be easily obtained from the probability tree of Fig. 8 and the second follows after some straightforward algebraic manipulations. As an example, if the ME employs the second task decision rule from Table 7 and the DE employs the seventh task decision rule from Table 8, the expected cost for the system is obtained as follows:

Table 8  
Task decision rules for the DE who is the DTL, and the corresponding points of the ROC curve

<table><tr><td></td><td> $(P_{F}^{0}, P_{D}^{0})$ </td><td> $(P_{F}^{1}, P_{D}^{1})$ </td></tr><tr><td> $\gamma_{1}^{d}(Y, \nu) = 0 \text{ for } Y = 0, 1, 2, 3$ </td><td>(0.0, 0.0)</td><td>(0.0, 0.0)</td></tr><tr><td> $\gamma_{2}^{d}(Y, \nu) = 0 \text{ for } Y = 0, 1, 2 \text{ and } 1 \text{ for } Y = 3$ </td><td>(0.1, 0.6)</td><td>(0.1, 0.6)</td></tr><tr><td> $\gamma_{3}^{d}(Y, \nu) = 0 \text{ for } Y = 0, 1 \text{ and } 1 \text{ for } Y = 2, 3$ </td><td>(0.2, 0.8)</td><td>(0.2, 0.8)</td></tr><tr><td> $\gamma_{4}^{d}(Y, \nu) = 0 \text{ for } Y = 0 \text{ and } 1 \text{ for } Y = 1, 2, 3$ </td><td>(0.4, 0.9)</td><td>(0.4, 0.9)</td></tr><tr><td> $\gamma_{5}^{d}(Y, \nu) = 1 \text{ for } Y = 0, 1, 2, 3$ </td><td>(1.0, 1.0)</td><td>(1.0, 1.0)</td></tr><tr><td> $\gamma_{6}^{d}(Y, \nu) = 0 \text{ otherwise and } 1 \text{ for } Y = 3 \text{ and } \nu = 1$ </td><td>(0.0, 0.0)</td><td>(0.1, 0.6)</td></tr><tr><td> $\gamma_{7}^{d}(Y, \nu) = 0 \text{ for } Y = 0, 1, \text{ cr } \nu = 0 \text{ and } 1 \text{ otherwise}$ </td><td>(0.0, 0.0)</td><td>(0.2, 0.8)</td></tr><tr><td> $\gamma_{8}^{d}(Y, \nu) = 0 \text{ for } Y = 0, \text{ or } \nu = 0 \text{ and } 1 \text{ otherwise}$ </td><td>(0.0, 0.0)</td><td>(0.4, 0.9)</td></tr><tr><td> $\gamma_{9}^{d}(Y, \nu) = 0 \text{ otherwise and } 1 \text{ for } \nu = 1$ </td><td>(0.0, 0.0)</td><td>(1.0, 1.0)</td></tr><tr><td> $\gamma_{10}^{d}(Y, \nu) = 0 \text{ otherwise and } 1 \text{ for } Y = 3, \text{ or } Y = 2 \text{ and } \nu = 1$ </td><td>(0.1, 0.6)</td><td>(0.2, 0.8)</td></tr><tr><td> $\gamma_{11}^{d}(Y, \nu) = 0 \text{ otherwise and } 1 \text{ for } Y = 3, \text{ or } Y = 1, 2 \text{ and } \nu = 1$ </td><td>(0.1, 0.6)</td><td>(0.4, 0.9)</td></tr><tr><td> $\gamma_{12}^{d}(Y, \nu) = 0 \text{ otherwise and } 1 \text{ for } Y = 3, \text{ or } \nu = 1$ </td><td>(0.1, 0.6)</td><td>(1.0, 1.0)</td></tr><tr><td> $\gamma_{13}^{d}(Y, \nu) = 0 \text{ for } Y = 0, \text{ or } Y = 1 \text{ and } \nu = 0 \text{ and } 1 \text{ otherwise}$ </td><td>(0.2, 0.8)</td><td>(0.4, 0.9)</td></tr><tr><td> $\gamma_{14}^{d}(Y, \nu) = 0 \text{ otherwise and } 1 \text{ for } Y = 2, 3, \text{ or } \nu = 1$ </td><td>(0.2, 0.8)</td><td>(1.0, 1.0)</td></tr><tr><td> $\gamma_{15}^{d}(Y, \nu) = 0 \text{ for } Y = 0, \text{ or } \nu = 0 \text{ and } 1 \text{ otherwise}$ </td><td>(0.4, 0.9)</td><td>(1.0, 1.0)</td></tr></table>

![](/api/attachments/JT3KF6B4/fulltext/images/5d3adbf6751beab2a1582089d7b954cfae0799f9dd61196c7b1df9e3d4c6f41e.jpg)  
Fig. 8. Decision tree for example 3.

$$
\begin{array}{r l} E \big [ C (u, S _ {i}) \big ] & = 0. 5 \times 6 5 + 0. 5 \times 7 5 + 0. 5 \\ & \times [ 0. 5 \times 0 + 0. 5 \times 0. 2 ] [ 1 2 0 - 6 5 ] \\ & + 0. 5 \times [ 0. 1 \times 0 + 0. 9 \times 0. 8 ] \\ & \times [ 0 - 7 5 ] = 4 8. 5. \end{array}
$$

Eq. (5) can be used to calculate the minimum expected cost over all twenty five task decision rules, and consequently to obtain the optimal task decision rules and expected cost for the system configuration that has the DE as the DTL (Table 9).

After the system configuration with the DE as the DTL has been completely analyzed, it is time to turn our attention to the other configuration in which the ME is the DTL. Proceeding in an analogous manner as before, there exist three sensible alternative task decision rules for the communication message of the DE. The ME has four alternative task decision rules if he or she completely ignores the communicated message and six alternative sensible decision rules if he or she takes the message into consideration. Thus, there exist twenty two $(22 = 4 + 3 \times 6)$ different task decision rules for the system. Using Eq. (5) the expected cost to the system can be evaluated for each choice of task decision rules. Hence, the optimal task decision rules and expected cost are obtained (Table 9).

Therefore, for the first cost and prior probability assignment of Table 6, the optimal configuration of the system is to designate the ME as the DTL.

## 2.3.2. The efficient optimization procedure

An algorithm that determines the optimal task decision rules and, consequently, the optimal expected cost for a given configuration of the tandem topology is presented. This is a more sophisticated, more complex, and far more computationally efficient method to optimally solve the problem than the naive “brute force” method used above. This algorithm is an adaptation of the likelihood ratio tests with constant but coupled thresholds that were presented in [17].

Optimal task decision rules and expected cost for both configurations of example 3

<table><tr><td>Config.</td><td>ME worse → DE better →</td><td>DE better → ME worse →</td></tr><tr><td colspan="3">Assignment 1</td></tr><tr><td>DE</td><td> $\gamma_{13}^{d}(Y, \nu) = 0 \text{ for } Y + \nu \leq 1 \text{ and } 1 \text{ otherwise}$  $(P_{F}^{0}, P_{D}^{0}) = (0.2, 0.8)$  $(P_{F}^{1}, P_{D}^{1}) = (0.4, 0.9)$ </td><td> $\gamma_{2}^{d}(Y) = 0 \text{ for } Y = 0, 1 \text{ and } 1 \text{ for } Y = 2, 3$  $(P_{F}^{c}, P_{D}^{c}) = (0.1, 0.4)$ </td></tr><tr><td>ME</td><td> $\gamma_{1}^{m}(X) = 0 \text{ for } X = 0, 1 \text{ and } 1 \text{ for } X = 2$  $(P_{F}^{c}, P_{D}^{c}) = (0.2, 0.8)$ </td><td> $\gamma_{2}^{m}(X, \nu) = 0 \text{ for } X\nu = 0 \text{ and } 1 \text{ otherwise}$  $(P_{F}^{0}, P_{D}^{0}) = (0.0, 0.0)$  $(P_{F}^{1}, P_{D}^{1}) = (0.5, 0.9)$ </td></tr><tr><td>Cost</td><td>42.55</td><td>42.55*</td></tr><tr><td colspan="3">Assignment 2</td></tr><tr><td>DE</td><td> $\gamma_{13}^{d}(Y, \nu) = 0 \text{ for } Y + \nu \leq 1 \text{ and } 1 \text{ otherwise}$  $(P_{F}^{0}, P_{D}^{0}) = (0.2, 0.8)$  $(P_{F}^{c}, P_{D}^{c}) = (0.1, 0.4)$ </td><td> $\gamma_{2}^{d}(Y) = 0 \text{ for } Y = 0, 1 \text{ and } 1 \text{ for } Y = 2, 3$  $(P_{F}^{1}, P_{D}^{1}) = (1.0, 1.0)$ </td></tr><tr><td>ME</td><td> $\gamma_{2}^{m}(X) = 0 \text{ for } X = 0 \text{ and } 1 \text{ for } X = 1, 2$  $(P_{F}^{c}, P_{D}^{c}) = (0.2, 0.8)$ </td><td> $\gamma_{5}^{m}(X, \nu) = 0 \text{ otherwise and } 1 \text{ for } 2\nu + X \geq 2$  $(P_{F}^{0}, P_{D}^{0}) = (0.1, 0.4)$  $(P_{F}^{1}, P_{D}^{1}) = (1.0, 1.0)$ </td></tr><tr><td>Cost</td><td>16.85*</td><td>17.06</td></tr></table>

## ALGORITHM II

Step 0: Consider the given cost assignment and prior probabilities; calculate $\eta$ from Eq. (4).

Step 1: For a corner point $(P_{F}^{c}, P_{D}^{c})$ [other than $(0, 0)$ and $(1, 1)$ ] of the ROC curve of the engineer that communicates the message to the DTL, calculate:

$$
\eta_ {0} = \eta \frac {1 - P _ {F} ^ {c}}{1 - P _ {D} ^ {c}} \text {   and   } \eta_ {1} = \eta \frac {P _ {F} ^ {c}}{P _ {D} ^ {c}}.
$$

Step 2: Determine the point $(P_{F}^{0}, P_{D}^{0})$ of the ROC curve of the DTL at which the slope of the tangent to the ROC curve is $\eta_{0}$ . Also, determine the point $(P_{F}^{1}, P_{D}^{1})$ of the ROC curve of the DTL at which the slope of the tangent to the ROC curve is $\eta_{1}$ .

Step 3: Calculate:

$$
\eta_ {c} = \eta \frac {P _ {F} ^ {1} - P _ {F} ^ {0}}{P _ {D} ^ {1} - P _ {D} ^ {0}}.
$$

Step 4: Determine the point $(P_{F}, P_{D})$ of the ROC curve of the communicating engineer at which the slope of the tangent to the ROC curve is $\eta_{c}$ . If the point $(P_{F}, P_{D})$ is the same as $(P_{F}^{c}, P_{D}^{c})$ of Step 1, save the three points because they could define the optimal task decision rules; otherwise reject them.

Step 5: If all the corner points of the ROC curve have not been examined, select the next one and go back to Step 1.

Step 6: If only one set of potentially optimal points have been saved, these define the optimal task decision rules. Otherwise, calculate the expected cost for each set using Eq. (5); the points that yield the minimum expected cost define the optimal task decision rules.

As an example, this algorithm is employed to obtain the optimal task decision rules for the second cost and prior probability assignment of Table 6 if the DE is designated as the DTL. (Recall, from Fig. 6, that the slopes of the ROC curve of the ME in decreasing order 4, 1.25 and 0.2, and the slopes of the ROC curve of the DE in decreasing order are 6, 2, 0.5 and 0.1667.)

Step 1: $(P_F^c, P_D^c) = (0.1, 0.4)$ ; $\eta_0 = 0.54$ ; $\eta_1 = 0.09$ .

Step 2: $0.5 < \eta_0 = 0.54 < 2$ , thus: $(P_F^0, P_D^0) = (0.2, 0.8)$ ; $\eta_1 = 0.09 < 0.1667$ , thus: $(P_F^1, P_D^1) = (1.0, 1.0)$ .

Step 3: $\eta_{c} = 1.44$ .

Step 4: $1.25 < \eta_c = 1.44 < 4$ , thus: $(P_F, P_D) = (0.1, 0.4) = (P_F^c, P_D^c)$ ; save the points as SET 1.

Step 5: Go back to Step 1.

Step 1: $(P_F^c, P_D^c) = (0.5, 0.9)$ ; $\eta_0 = 1.8$ ; $\eta_1 = 0.2$ .  
Step 2: $0.5 < \eta_0 = 1.8 < 2$ , thus: $(P_F^0, P_D^0) = (0.2, 0.8)$ ; $0.1667 < \eta_1 = 0.2 < 0.5$ , thus: $(P_F^1, P_D^1) = (0.4, 0.9)$

Step 3: $\eta_c = 0.72$ .

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 4: $0.2 &lt; \eta_c = 0.72 &lt; 1.25$, thus: $(P_F, P_D) = (0.5, 0.9) = (P_F^c, P_D^c)$; save the points as SET 2. Step 5: Go to Step 6.
</div>

Step 6: The expected cost is 17.06 for SET 1, and 16.85 for SET 2. Thus, SET 2 is optimal.

The optimal task decision rules that correspond to SET 2 can be found in Table 9 (the first column of decision rules for Assignment 2). On the other hand, if the ME is designated as the DTL:

Step 0: $\eta = 0.36$ .  
Step 1: $(P_F^c, P_D^c) = (0.1, 0.6)$ ; $\eta_0 = 0.81$ ; $\eta_1 = 0.06$ .  
Step 2: $0.2 < \eta_0 = 0.81 < 1.25$ , thus: $(P_F^0, P_D^0) = (0.5, 0.9)$ ; $\eta_1 = 0.06 < 0.2$ , thus: $(P_F^1, P_D^1) = (1.0, 1.0)$

Step 3: $\eta_c = 1.8$ .

Step 4: $0.5 < \eta_c = 1.8 < 2$ , thus: $(P_F, P_D) = (0.2, 0.8) \neq (P_F^c, P_D^c)$ : reject.

Step 5: Go back to Step 1.

Step 1: $(P_F^c, P_D^c) = (0.2, 0.8)$ ; $\eta_0 = 1.44$ ; $\eta_1 = 0.09$ .

Step 2: $1.25 < \eta_0 = 1.44 < 4$ , thus: $(P_F^0, P_D^0) = (0.1, 0.4)$ ; $\eta_1 = 0.09 < 0.2$ , thus: $(P_F^1, P_D^1) = (1.0, 1.0)$

Step 3: $\eta_{c} = 0.54$ .

Step 4: $0.5 < \eta_c = 0.54 < 2$ , thus: $(P_F, P_D) = (0.2, 0.8) = (P_F^c, P_D^c)$ : save the points as SET 1.  
Step 5: Go back to Step 1.

Step 1: $(P_F^c, P_D^c) = (0.4, 0.9)$ ; $\eta_0 = 2.16$ ; $\eta_1 = 0.16$ .

Step 2: $1.25 < \eta_0 = 2.16 < 4$ , thus: $(P_F^0, P_D^0) = (0.1, 0.4)$ ; $\eta_1 = 0.16 < 0.2$ , thus: $(P_F^1, P_D^1) = (1.0, 1.0)$

Step 3: $\eta_c = 0.54$ .

Step 4: $0.2 < \eta_c = 0.54 < 2$ , thus: $(P_F, P_D) = (0.2, 0.8) \neq (P_F^c, P_D^c)$ : reject.

Step 5: Go to Step 6.

Step 6: The optimal expected cost is 17.06 for SET 1.

The optimal task decision rules that correspond to SET 2 can be found in Table 9 (the last column of decision rules for Assignment 2). Therefore, for this cost assignment the optimal configuration is to designate the DE as the DTL (for an expected cost of 16.85). Furthermore, any interested readers who used the “brute force” method to determine the optimal decision rules will certainly appreciate the efficiency of Algorithm II.

Note. The deterioration of the system performance if the optimal configuration is not employed is 0.30 cost units (0.71%) for assignment 1, and 0.21 (1.25%) cost units for assignment 2. This seems to misleadingly suggest that the optimal configuration does not have a significant effect in the performance of the system.

To summarize, for the first cost and prior probability assignment the optimal configuration of the system is to designate the ME as the DTL, while for the second cost and prior probability assignment the optimal configuration of the system is to designate the DE as the DTL. Therefore, even in the special case in which one engineer is clearly better than the other in the ROC curve sense, the optimal configuration depends on parameters that are external to the system; that is, parameters that cannot be controlled by the system, like the costs and the prior probabilities.

## 2.4. Example 3.A: effects of communications on optimal integration topology

Consider again the problem of the previous example for the first cost and prior probability assignment of Table 6. In the optimal configuration the ME is designated as the DTL for an expected cost of 42.25. Recall that in this case the message communicated to the DTL is binary; either that the system should go ahead with the production of the new product ( $\nu = 1$ ), or that the project should be abandoned ( $\nu = 0$ ).

Suppose that the message communicated to the DTL is allowed to be ternary; either that the system should go ahead with the production of the new product ( $\nu = 2$ ), or that the DTL should decide because the consulting engineer does not have a strong opinion either way ( $\nu = 1$ ), or that the project should be abandoned ( $\nu = 0$ ). The objective is to obtain the optimal configuration for the system in this case. The analysis proceeds in a manner analogous to the previous example.

Define by $(P_{F}^{0}, P_{D}^{0})$ the point of the ROC curve that the DTL will employ when the message from the other engineer is to abandon the project $(\nu = 0)$ , by $(P_{F}^{1}, P_{D}^{1})$ the point of ROC curve that the DTL will employ when the message from the other engineer is that the DTL should decide $(\nu = 1)$ , and by $(P_{F}^{2}, P_{D}^{2})$ the point of ROC curve that the DTL will employ when the message from the other engineer is to go ahead with the project $(\nu = 2)$

Also, define by $(P_{F}^{ca}, P_{D}^{ca})$ and by $(P_{F}^{cb}, P_{D}^{cb})$ the points of the ROC curve that the other engineer employs to communicate his or her message to the DTL (with $P_{F}^{ca} < P_{D}^{cb}$ ). This implies that the message communicated to the DTL is to go ahead with the project $(\nu = 2)$ with probability $P_{F}^{ca}$ when the state of the environment is bad $(S_{0})$ , and with probability $P_{F}^{ca}$ when the state of the environment is good $(S_{1})$ . It also implies that the message communicated to the DTL is that he or she does not have a strong opinion either way $(\nu = 1)$ with probability $(P_{F}^{cb} - P_{F}^{ca})$ when the state of the environment is bad, and with probability $(P_{F}^{cb} - P_{D}^{ca})$ when the state of the environment is good. Thus, the message communicated to the DTL is that the project should be abandoned $(\nu = 0)$ with probability $(1 - P_{F}^{cb})$ when the state of the environment is bad, and with probability $(1 - P_{D}^{cb})$ when the state of the environment is good.

## 2.4.1. The “brute force” optimization approach

To determine the minimum expected cost for the system if the DE is the DTL the “brute force” approach may be used. There exists only one sensible task decision rule that the ME should employ for his or her communication message. The task decision rule is to advise the DTL to go ahead with the project ( $\nu=2$ ) if his or her own assessment is that the product will most likely be a success (X=2), and to otherwise abandon the project; this corresponds to operating at the points $(P_{F}^{ca}, P_{D}^{ca})=(0.1, 0.4)$ and $(P_{F}^{cb}, P_{D}^{cb})=(0.5, 0.9)$ of the ROC curve.

Then, the task decision rules of the DTL, that is the DE, is considered. The DTL may decide to completely ignore the communicated message; in that case, just as in the previous example, he or she has five task decision rules to choose from. If the DTL decides to take into consideration the message communicated from the ME, there exist thirty different sensible task decision rules that he or she may employ. Thus, there exist thirty five different task decision rules for the system as a whole. For each of the thirty five choices the corresponding expected cost for the system can be calculated using the following equation:

$$
\begin{array}{l} E \big [ C (u, S _ {i}) \big ] \\ = P (S _ {0}) \big [ \big (1 - P _ {F} ^ {c b} \big) \big [ \big (1 - P _ {F} ^ {0} \big) C (0, S _ {0}) \\ + P _ {F} ^ {0} C (1, S _ {0}) \big ] + \big (P _ {F _ {c b}} - P _ {F} ^ {c a} \big) \\ \times \big [ \big (1 - P _ {F} ^ {1} \big) C (0, S _ {0}) + P _ {F} ^ {1} C (1, S _ {0}) \big ] \\ + P _ {F} ^ {c a} \big [ \big (1 - P _ {F} ^ {2} \big) C (0, S _ {0}) + P _ {F} ^ {2} C (1, S _ {0}) \big ] \big ] \\ + P (S _ {1}) \big [ \big (1 - P _ {\mathcal {D}} ^ {c b} \big) \big [ \big (1 - P _ {D} ^ {0} \big) C (0, S _ {1}) \\ + P _ {D} ^ {0} C (1, S _ {1}) \big ] \\ + \big (P _ {D} ^ {c b} - P _ {D} ^ {c a} \big) \big [ \big (1 - P _ {D} ^ {1} \big) C (0, S _ {1}) \\ + P _ {D} ^ {1} C (1, S _ {1}) \big ] + P _ {D} ^ {c a} \big [ \big (1 - P _ {D} ^ {2} \big) C (0, S _ {1}) \\ + P _ {D} ^ {2} C (1, S _ {1}) \big ] \big ] \\ = P (S _ {0}) C (0, S _ {0}) + P (S _ {1}) C (0, S _ {1}) \\ + P (S _ {0}) \big [ \big (1 - P _ {F} ^ {c b} \big) P _ {F} ^ {0} + \big (P _ {F} ^ {c b} - P _ {F} ^ {c a} \big) P _ {F} ^ {1} \\ + P _ {F} ^ {c a} P _ {F} ^ {2} \big ] \big [ C (1, S _ {0}) - C (0, S _ {0}) \big ] \\ + P (S _ {1}) \big [ \big (1 - P _ {D} ^ {c b} \big) P _ {D} ^ {0} + \big (P _ {D} ^ {c b} - P _ {D} ^ {c a} \big) P _ {D} ^ {1} \\ + P _ {D} ^ {c a} P _ {D} ^ {2} \big ] \big [ C (1, S _ {1}) - C (0, S _ {1}) \big ]. \end{array}\tag{6}
$$

This equation is obtained in an analogous manner to Eq. (5). Eq. (6) is used to calculate the minimum expected cost over all thirty five task decision rules, and consequently to obtain the optimal task decision rules for the system configuration that has the DE as the DTL (Table 10).

## 2.4.2. The efficient optimization procedure

An algorithm, that determines the optimal task decision rules and consequently the optimal expected cost for a given configuration of the tandem topology when ternary communication message are employed, is presented. This is a direct generalization of Algorithm II. Again, this algorithm is an adaptation of the likelihood ratio tests with constant but coupled thresholds that were presented in [17].

## Algorithm II.A

Step 0: Consider the given cost assignment and prior probabilities; calculate $\eta$ from Eq. (4).

Step 1: For a pair of corner points $(P_F^{ca}, P_D^{ca})$ and $(P_F^{cb}, P_D^{cb})$ of the ROC curve of the engineer that communicates the message to the DTL [other than (0, 0) and (1, 1)], with $P_F^{ca} < P_F^{cb}$ , calculate:

$$
\eta_ {0} = \eta \frac {1 - P _ {F} ^ {c b}}{1 - P _ {D} ^ {c b}}, \eta_ {1} = \eta \frac {P _ {F} ^ {c b} - P _ {F} ^ {c a}}{P _ {D} ^ {c b} - P _ {D} ^ {c a}} \text { and } \eta_ {2} = \eta \frac {P _ {F} ^ {c a}}{P _ {D} ^ {c a}}.
$$

Step 2: Determine the point $(P_{F}^{0}, P_{D}^{0})$ of the ROC curve of the DTL at which the slope of the tangent to the ROC curve is $\eta_{0}$ . Determine the point $(P_{F}^{1}, P_{D}^{1})$ of the ROC curve of the DTL at which the slope of the tangent to the ROC curve is $\eta_{1}$ . Also, determine the point $(P_{F}^{2}, P_{D}^{2})$ of the ROC curve of the DTL at which the slope of the tangent to the ROC curve is $\eta_{2}$ .

Step 3: Calculate:

$$
\eta_ {c a} = \eta \frac {P _ {F} ^ {2} - P _ {F} ^ {1}}{P _ {D} ^ {2} - P _ {D} ^ {1}} \text {   and   } \eta_ {c b} = \eta \frac {P _ {F} ^ {1} - P _ {F} ^ {0}}{P _ {D} ^ {1} - P _ {D} ^ {0}}.
$$

Step 4: Determine the point $(P_{F}^{a}, P_{D}^{a})$ of the ROC curve of the communicating engineer at which the slope of the tangent to the ROC curve is $\eta_{ca}$ . Also, determine the point $(P_{F}^{b}, P_{D}^{b})$ of the ROC curve of the communicating engineer at which the slope of the tangent to the ROC curve is $\eta_{cb}$ . If the points $(P_{F}^{a}, P_{D}^{a})$ and $(P_{F}^{b}, P_{D}^{b})$ are the same as $(P_{F}^{ca}, P_{D}^{ca})$ and $(P_{F}^{cb}, P_{D}^{cb})$ of Step 1, save the five points because they could define the optimal task decision rules; otherwise reject them.

Step 5: If all the pairs of corner points of the ROC curve have not been examined, select the next pair and go back to Step 1.

Table 10  
Optimal task decision rules and cost for both configurations of example 3A

<table><tr><td>Config.</td><td>ME worse → DE better →</td><td>DE better → ME worse →</td></tr><tr><td colspan="3">Binary messages</td></tr><tr><td>DE</td><td> $\gamma_{13}^{d}(Y, \nu) = 0 \text{ for } Y + \nu \leq 1 \text{ and } 1 \text{ otherwise}$  $(P_{F}^{0}, P_{D}^{0}) = (0.2, 0.8)$  $(P_{F}^{1}, P_{D}^{1}) = (0.4, 0.9)$ </td><td> $\gamma_{2}^{d}(Y) = 0 \text{ for } Y = 0, 1 \text{ and } 1 \text{ for } Y = 2, 3$  $(P_{F}^{c}, P_{D}^{c}) = (0.1, 0.4)$ </td></tr><tr><td>ME</td><td> $\gamma_{1}^{m}(X) = 0 \text{ for } X = 0, 1 \text{ and } 1 \text{ for } X = 2$  $(P_{F}^{c}, P_{D}^{c}) = (0.2, 0.8)$ </td><td> $\gamma_{2}^{m}(X, \nu) = 0 \text{ for } X\nu = 0 \text{ and } 1 \text{ otherwise}$  $(P_{F}^{0}, P_{D}^{0}) = (0.0, 0.0)$  $(P_{F}^{1}, P_{D}^{1}) = (0.5, 0.9)$ </td></tr><tr><td>Cost</td><td>42.55</td><td>42.25*</td></tr><tr><td colspan="3">Ternary messages</td></tr><tr><td>DE</td><td> $\gamma_{19}^{d}(Y, \nu) = 0 \text{ otherwise and } 1 \text{ for } Y + \nu \geq 3$  $(P_{F}^{0}, P_{D}^{0}) = (0.1, 0.6)$  $(P_{F}^{1}, P_{D}^{1}) = (0.2, 0.8)$  $(P_{F}^{2}, P_{D}^{2}) = (0.4, 0.9)$ </td><td> $\gamma_{3}^{d}(Y) = 0 \text{ for } Y = 0 \text{ and } 1 \text{ for } Y = 1 \text{ and } 2 \text{ for } Y = 2, 3$  $(P_{F}^{ca}, P_{D}^{ca}) = (0.2, 0.8)$  $(P_{F}^{cb}, P_{D}^{cb}) = (0.4, 0.9)$ </td></tr><tr><td>ME</td><td> $\gamma_{1}^{m}(X) = 0 \text{ for } X = 0 \text{ and } 1 \text{ for } X = 1 \text{ and } 2 \text{ for } X = 2$  $(P_{F}^{ca}, P_{D}^{ca}) = (0.1, 0.4)$  $(P_{F}^{cb}, P_{D}^{cb}) = (0.5, 0.9)$ </td><td> $\gamma_{5}^{m}(X, \nu) = 0 \text{ otherwise and } 1 \text{ for } X + \nu \geq 3$  $(P_{F}^{0}, P_{D}^{0}) = (0.0, 0.0)$  $(P_{F}^{1}, P_{D}^{1}) = (0.1, 0.4)$  $(P_{F}^{2}, P_{D}^{2}) = (0.5, 0.9)$ </td></tr><tr><td>Cost</td><td>41.675*</td><td>41.80</td></tr></table>

Step 6: If only one set of potentially optimal points have been saved, these define the optimal task decision rules. Otherwise, calculate the expected cost for each set using Eq. (6); the points that yield the minimum expected cost define the optimal task decision rules.

As an example, this algorithm is used to obtain the optimal task decision rules for the other configuration where the ME is designated as the DTL. (Again recall, from Fig. 6, that the slopes of the ROC curve of the ME in decreasing order 4, 1.25 and 0.2, and the slopes of the ROC curve of the DE in decreasing order are 6, 2, 0.5 and 0.1667.)

Step 0: $\eta = 1.1$ .  
Step 1: $(P_F^{ca}, P_D^{ca}) = (0.2, 0.8)$ ; $(P_F^{cb}, P_D^{cb}) = (0.4, 0.9)$ ; $\eta_0 = 6.6$ ; $\eta_1 = 2.2$ ; $\eta_2 = 0.275$ .  
Step 2: $4 < \eta_0 = 6.6$ , thus: $(P_F^0, P_D^0) = (0.0, 0.0)$ ; $1.25 < \eta_1 = 2.2 < 4$ , thus: $(P_F^1, P_D^1) = (0.1, 0.4)$ ; $0.2 < \eta_2 = 0.275 < 1.25$ , thus: $(P_F^2, P_D^2) = (0.5, 0.9)$ .  
Step 3: $\eta_{ca} = 0.88$ ; $\eta_{ca} = 0.275$ .

Step 4: $0.5 < \eta_{ca} = 0.88 < 2$ , thus: $(P_F^a, P_D^a) = (0.2, 0.8) = (P_F^{ca}, P_D^{ca})$ ; $0.1667 < \eta_{cb} = 0.275 < 0.5$ , thus: $(P_F^b, P_D^b) = (0.4, 0.9) = (P_F^{cb}, P_D^{cb})$ ; save as SET 1.

Step 5: Go to Step 1.

Step 1: $(P_F^{ca}, P_D^{ca}) = (0.1, 0.6)$ ; $(P_F^{cb}, P_D^{cb}) = (0.4, 0.9)$ ; $\eta_0 = 6.6$ ; $\eta_1 = 1.1$ ; $\eta_2 = 0.183$ . Step 2: $4 < \eta_0 = 6.6$ , thus: $(P_F^0, P_D^0) = (0.0, 0.0)$ ; $0.2 < \eta_1 = 1.1 < 1.25$ , thus: $(P_F^1, P_D^1) = (0.5, 0.9)$ ; $\eta_2 = 0.183 < 0.2$ , thus: $(P_F^2, P_D^2) = (1.0, 1.0)$ .

Step 3: $\eta_{ca} = 5.5$ ; $\eta_{cb} = 0.6111$ .

Step 4: $2 < \eta_{ca} = 5.5 < 6$ , thus: $(P_F^a, P_D^a) = (0.1, 0.6) \neq (P_F^{ca}, P_D^{ca})$ : reject.

Step 5: Go to Step 1.

Step 1: $(P_F^{ca}, P_D^{ca}) = (0.1, 0.6)$ ; $(P_F^{cb}, P_D^{cb}) = (0.2, 0.8)$ ; $\eta_0 = 4.4$ ; $\eta_1 = 0.55$ ; $\eta_2 = 0.1833$ .  
Step 2: $4 < \eta_0 = 4.4$ , thus: $(P_F^0, P_D^0) = (0.0, 0.0)$ ; $0.2 < \eta_1 = 0.55 < 1.25$ , thus: $(P_F^1, P_D^1) = (0.5, 0.9)$ ; $\eta_2 = 0.1833 < 0.2$ , thus: $(P_F^2, P_D^2) = (1.0, 1.0)$ .

Step 3: $\eta_{ca} = 5.5$ ; $\eta_{cb} = 0.6111$ .

Step 4: $2 < \eta_{ca} = 5.5 < 6$ , thus: $(P_F^a, P_D^a) = (0.1, 0.6) = (P_F^{ca}, P_D^{ca})$ ; $0.5 < \eta_{cb} = 0.6111 < 2$ , thus: $(P_F^b, P_D^b) = (0.2, 0.8) = (P_F^{cb}, P_D^{cb})$ ; save as SET 2. Step 5: Go to Step 6.

Step 6: The expected cost is 41.8 for SET 1, and 42.125 for SET 2. Thus, SET 1 is optimal.

The optimal task decision rules that correspond to SET 1 can be found in Table 10 (in the last column for ternary messages). Therefore, for the first cost and prior probability assignment of Table 6 and for ternary communication messages, the optimal configuration of the system is to designate the DE as the DTL.

The fact that the optimal configuration of the system depends on the number of messages should not be surprising. But, what is surprising is the way that the increase in the number of messages influences the optimal configuration.

To see this consider the two limit cases. In the first, zero communication messages are allowed (i.e., no communication). It should be clear that in this case the optimal configuration is to designate the better decision making entity (the DE in our case) to be the DTL; in other words if one member of the system has to make the decision in isolation, let the best one do it. In the second limiting case, an infinite number of communication messages is allowed (i.e., centralized decision making). In this case, it does not matter who the DTL is; therefore, the worse decision making entity may be designated to be the DTL without any deterioration in the performance of the system.

Thus, by considering the limiting cases one concludes that as the amount of communication allowed between the engineers increases, it becomes easier for the worse one to be the DTL. But in this example, as the number of messages increases from two to three, the optimal configuration changes from having the (worse) ME as the DTL to having the (better) DE as the DTL. This is a counterintuitive result that suggests that no obvious generalizations can be made.

## 2.5. Example 4: integrating two engineering tasks in a parallel topology

A special case of the parallel topology for two engineers is analyzed; in this case both engineers have the same capability. It will be established that, contrary to intuition, the optimal task decision rules for these engineers do not have to be identical.

Consider again a development engineer (DE) and a manufacturing engineer (ME) who have to decide on whether to go ahead with the production of a new product or whether to abandon the project. Suppose that their manager wants to have the final word, that is be the design team leader (DTL). It has thus been decided that the parallel topology will be employed (Fig. 4b). Recall that both the ME and the DE make their individual recommendations which they relate directly to the manager (DTL) who is responsible for the final task decision. The DTL does not analyze personally the situation and relies exclusively on the communications from the engineers.

Assume, as in Example 3, that there are two mutually exclusive states for the environment as far as the introduction of the new product is concerned; either the state of the environment is good (state $S_{1}$ ) and the product should be introduced, or it is bad (state $S_{0}$ ) and the project should be abandoned or at least delayed. Also assume that the costs and prior probabilities are known.

Assume that each of the two engineers can communicate to the DTL one of two recommendations; either that the system should go ahead with the production of the new product ( $\nu=1$ ) or that the project should be abandoned ( $\nu=0$ ). Unless he or she decides to ignore the communicated recommendations, the DTL has two alternative sensible task decision rules: (1) the AND decision rule (i.e., to go ahead with the project only if both the ME and the DE believe that the system should go ahead), and (2) the OR decision rule (i.e., to go ahead with the project if either the ME or the DE believe that the system should go ahead).

Both the AND and the OR decision rules are symmetric (i.e., they do not distinguish between the engineers). Also, the cost and prior probability assignment of Table 11 is perfectly symmetric. Therefore, one would expect that if the two engineers were identical (i.e., have the exact same ability to assess the situation), their optimal task decision rules would be identical. This conjecture is intuitively appealing because one would expect that similar engineers performing optimally, at the same level of an organization, and faced with the same assessment of the situation (i.e., observation), would come to the same conclusion (i.e., decision). It is shown that this is not always true; this serves as another reminder of the intrinsic difficulties associated with optimal engineering integration topologies.

Cost and prior probability assignments for example 4

<table><tr><td> $P(S_0)$ </td><td> $P(S_1)$ </td><td> $C(0, S_0)$ </td><td> $C(1, S_0)$ </td><td> $C(0, S_1)$ </td><td> $C(1, S_1)$ </td><td> $\eta$ </td></tr><tr><td>0.50</td><td>0.50</td><td>10</td><td>100</td><td>100</td><td>10</td><td>1.0</td></tr></table>

Probability mass functions for the observations of the DE and the ME in example 4

<table><tr><td> $P(Y|S_0)$ </td><td>0.5</td><td>0.2</td><td>0.3</td></tr><tr><td> $P(Y|S_1)$ </td><td>0.1</td><td>0.1</td><td>0.8</td></tr><tr><td>Y</td><td>0</td><td>1</td><td>2</td></tr></table>

Each of the two identical engineers performs an extensive analysis to form his or her own personal assessment of the situation. The assessment (i.e., observation) of each can be summarized as follows: either the product will most likely be a failure $Y = 0$ , or the situation is unclear $Y = 1$ , or the product will most likely be a success $Y = 2$ . The conditional probability mass functions of the observations given the true state of the environment are presented in Table 12. The corresponding ROC curve for the engineers is presented in Fig. 9.

## 2.5.1. A “brute force” optimization approach

Consider the cost and prior probability assignment of Table 11. The problem is to determine the optimal decision rules for the DE and the ME in the parallel topology. Define by $(P_{F}^{d}, P_{D}^{d})$ the point of the ROC curve that the DE employs for his or her communication message, and by $(P_{F}^{m}, P_{D}^{m})$ the point of ROC curve that the ME employs for his or her communication message. This implies that the DE decides to go ahead (u = 1) with probability $P_{F}^{d}$ when the state of the environment is bad ( $S_{0}$ ), and with probability $P_{D}^{d}$ when the state of the environment is good ( $S_{1}$ ).

There are only two sensible task decision rules that the DE can employ for his or her recommendation. The first task decision rule is to advise the DTL to go ahead with the project $(\nu=1)$ if his or her own assessment is that the product will most likely be a success $(Y=2)$ , and to otherwise abandon the project; this corresponds to operating at the point $(P_{F}^{d}, P_{D}^{d})=(0.3, 0.8)$ of the ROC curve. The second task decision rule is to advise the DTL to abandon the project $(\nu=0)$ if his or her own assessment is that the product will most likely be a failure $(Y=0)$ , and to otherwise go ahead with the project; this corresponds to operating at the point $(P_{F}^{d}, P_{D}^{d})=(0.5, 0.9)$ of the ROC curve. Since both engineers are identical (i.e., their observations have the same probability mass functions), the same two task decision rules are the only sensible decision rules for the ME as well.

![](/api/attachments/JT3KF6B4/fulltext/images/fdeffb1430769456c5ab85d84b53707ac22f110024c1252d2fd23f1cc0607cfe.jpg)  
Fig. 9. ROC curves for the DE and the ME in example 4.

If the DTL decides to ignore the recommendations, he or she decides either to always go ahead with the project $(u=1)$ or to always abandon the project $(u=0)$ . As was already discussed, if the DTL decides to take into consideration the recommendations of the DE and the ME, he or she has two alternative sensible task decision rules: the AND and the OR. Thus, there exist ten different task decision rules for the system as a whole; two, if the DTL decides to ignore the recommendations, and two task decision rules for each of the four possible decision rules of the engineers. For each of the ten choices the corresponding expected cost for the system can be calculated using the following equations:

If the AND decision rule is employed:

$$
\begin{array}{l} E \big [ C (u, S _ {i}) \big ] \\ = P (S _ {0}) \Big [ \big (1 - P _ {F} ^ {d} P _ {F} ^ {m} \big) C (0, S _ {0}) \\ \quad + P _ {F} ^ {d} P _ {F} ^ {m} C (1, S _ {0}) \Big ] \\ \quad + P (S _ {1}) \Big [ \big (1 - P _ {D} ^ {d} P _ {D} ^ {m} \big) C (0, S _ {1}) \\ \quad + P _ {D} ^ {d} P _ {D} ^ {m} C (1, S _ {1}) \Big ] \\ = P (S _ {0}) C (0, S _ {0}) + P (S _ {1}) C (0, S _ {1}) \\ \quad + P (S _ {0}) P _ {F} ^ {d} P _ {F} ^ {m} \big [ C (1, S _ {0}) - C (0, S _ {0}) \big ] \\ \quad + P (S _ {1}) P _ {D} ^ {d} P _ {D} ^ {m} \big [ C (1, S _ {1}) - C (0, S _ {1}) \big ]. \end{array}\tag{7a}
$$

If the OR decision rule is employed:

$$
\begin{array}{r l} & E \big [ C (u, S _ {i}) \big ] \\ & \quad = P (S _ {0}) \big [ \big (1 - P _ {F} ^ {d} \big) \big (1 - P _ {F} ^ {m} \big) C (0, S _ {0}) \\ & \quad + \big [ 1 - \big (1 - P _ {F} ^ {d} \big) \big (1 - P _ {F} ^ {m} \big) \big ] C (1, S _ {0}) \big ] \end{array}
$$

$$
\begin{array}{l} + P (S _ {1}) \left[ \left(1 - P _ {D} ^ {d}\right) \left(1 - P _ {D} ^ {m}\right) C (0, S _ {1}) \right. \\ + \left[ 1 - \left(1 - P _ {D} ^ {d}\right) \left(1 - P _ {D} ^ {m}\right) \right] C (1, S _ {1}) ] \\ = P (S _ {0}) C (1, S _ {0}) + P (S _ {1}) C (1, S _ {1}) \\ + P (S _ {0}) \left(1 - P _ {F} ^ {d}\right) \left(1 - P _ {F} ^ {m}\right) \left[ C (0, S _ {0}) \right. \\ - C (1, S _ {0}) ] + P (S _ {1}) \left(1 - P _ {D} ^ {d}\right) \left(1 - P _ {D} ^ {m}\right) \\ \times \left[ C (0, S _ {1}) - C (1, S _ {1}) \right]. \end{array}\tag{7b}
$$

These equations are obtained in a manner analogous to that of Example 3. They can be used to calculate the minimum expected cost over all task decision rules, and consequently to obtain the optimal task decision rules as well as the optimal identical task decision rules for the system (Table 13). As can be seen, the optimal task decision rules are not identical, even though both engineers are identical and the problem is perfectly symmetric; another counterintuitive result.

## 2.5.2. The efficient optimization procedure

An algorithm that determines the optimal configuration for the system, the optimal task decision rules and the optimal expected cost for the parallel topology is presented. Formally, the optimal task decision rules are obtained as likelihood ratio tests with constant thresholds [20]. As before, this is a more sophisticated, and far more computationally efficient method to optimally solve the problem. Also, this algorithm is an adaptation of the likelihood ratio tests with constant but coupled thresholds that were presented in [17].

## ALGORITHM III

Step 0: Consider the given cost assignment and prior probabilities; calculate $\eta$ from Eq. (4).

Step 1: For a corner point $(P_F^d, P_D^d)$ [other than (0, 0) and (1,1)] of the ROC curve of the $DE$ , calculate:

$$
\eta_ {m} ^ {A N D} = \eta \frac {P _ {F} ^ {d}}{P _ {D} ^ {d}} \text {   and   } \eta_ {m} ^ {\vee} = \eta \frac {1 - P _ {F} ^ {d}}{1 - P _ {D} ^ {d}}.
$$

Step 2: Determine the point $(P_{F}^{m}, P_{D}^{m})$ of the ROC curve of the ME at which the slope of the tangent to the ROC curve is $\eta_{m}^{AND}$ . If $(P_{F}^{m}, P_{D}^{m}) = (0, 0)$ or $(1, 1)$ , go to Step 4. Otherwise, calculate:

$$
\eta_ {d} ^ {A N D} = \eta \frac {P _ {F} ^ {m}}{P _ {D} ^ {m}}.
$$

Step 3: Determine the point $(P_{F}, P_{D})$ of the ROC curve of the DE at which the slope of the tangent to the ROC curve is $\eta_{d}^{AND}$ . If the point $(P_{F}, P_{D})$ is the same as $(P_{F}^{d}, P_{D}^{d})$ of Step 1, save the three points because they could define, together with the AND decision rule for the DTL, the optimal task decision rules; otherwise reject them.

Step 4: Determine the point $(P_{F}^{m}, P_{D}^{m})$ of the ROC curve of the ME at which the slope of the tangent to the ROC curve is $\eta_{m}^{OR}$ . If $(P_{F}^{m}, P_{D}^{m}) = (0, 0)$ or $(1, 1)$ , go to Step 4. Otherwise, calculate:

$$
\eta_ {d} ^ {O R} = \eta \frac {1 - P _ {F} ^ {m}}{1 - P _ {D} ^ {m}}.
$$

Step 5: Determine the point $(P_{F}, P_{D})$ of the ROC curve of the DE at which the slope of the tangent to the ROC curve is $\eta_{d}^{OR}$ . If the point $(P_{F}, P_{D})$ is the same as $(P_{F}^{d}, P_{D}^{d})$ of Step 1, save the three points because they could define, together with the OR decision rule for the DTL, the optimal task decision rules; otherwise reject them.

Step 6: If all the corner points of the ROC curve have not been examined, select the next one and go back to Step 1.

Table 13  
Optimal task decision rules and expected cost for example 4

<table><tr><td></td><td>Optimal task decision rules</td><td>Optimal identical task decision rules</td></tr><tr><td>DE</td><td> $\gamma_{2}^{d}(Y) = 0$  for Y = 0 and 1 for Y = 1, 2 $(P_{F}^{d}, P_{D}^{d}) = (0.5, 0.9)$ </td><td> $\gamma_{2}^{d}(Y) = 0$  for Y = 0 and 1 for Y = 1, 2 $(P_{F}^{d}, P_{D}^{d}) = (0.5, 0.9)$ </td></tr><tr><td>ME</td><td> $\gamma_{1}^{m}(X) = 0$  for X = 0, 1 and 1 for X = 1 $(P_{F}^{m}, P_{D}^{m}) = (0.3, 0.8)$ </td><td> $\gamma_{2}^{m}(X) = 0$  for X = 0 and 1 for X = 1, 2 $(P_{F}^{m}, P_{D}^{m}) = (0.5, 0.9)$ </td></tr><tr><td>DTL</td><td>AND</td><td>AND</td></tr><tr><td>Cost</td><td>29.35*</td><td>29.80</td></tr></table>

Step 7: Calculate the expected cost if the DTL ignores the communicated messages. Calculate the expected cost for each set that was saved, if any, using Eq. (7). The points that yield the minimum expected cost define the optimal task decision rules.

## 2.6. Example 5. integrating three engineering tasks

As our last example we consider a marketing engineer (RE), a development engineer (DE), and a manufacturing engineer (ME). These have to decide on whether to go ahead with the production of a new line of a certain product. There are four different ways to organize these three engineers into a system: they may be organized in a tandem topology, in the two consultant topology, in a parallel topology, and the asymmetrical topology (Fig. 10). In the former two, the ME is designated as the design team leader (DTL), while in the latter two, a manager is designated as the DTL. Using arguments similar to the ones in Example 2, it can be shown that the optimal topology for the system could either be the tandem or the two consultant topology.

In the tandem topology, the RE forms his or her own assessment of the situation and communicates a message to the DE. The DE forms his or her own personal assessment and also considers the message received from the RE; then, the DE communicates a message to the ME. The ME in turn forms his or her own personal assessment of the situation and considers the message received from the DE; then, the ME makes the final binding decision on whether the new product should be produced or not.

In the two consultant topology, both the RE and the DE form their own assessment of the situation and then each communicates a message to the ME. The ME makes his or her own personal assessment, considers the messages from the other engineers, and then makes the final binding decision on whether the new product should be produced or not.

We would like to compare the performance of the tandem and the two consultant topology. Since the analysis is analogous to that of Example 3, repetitive arguments and explanations will be omitted for brevity. To simplify our analysis, we consider only the special case where all three engineers are identical; thus, we do not have to worry about the optimal configuration for the system.

![](/api/attachments/JT3KF6B4/fulltext/images/09200059b21439b6bc53577e9df7ce08a9414450614bd7450b3864b06161592b.jpg)

![](/api/attachments/JT3KF6B4/fulltext/images/e600c36ccd61ea3e72220ec103d7794e5b100bb533e4ed731b98706c0e2bc9c7.jpg)  
(b). The Two-Consultant Topology

![](/api/attachments/JT3KF6B4/fulltext/images/62796d447fa6337999aa234fb41be5225e5357b8e2fb6911a5802fdd019dd867.jpg)

(c). The Parallel Topology  
![](/api/attachments/JT3KF6B4/fulltext/images/a319e0a2394117329e99f8ce9d638ae9e7fa89207be80071a8ed2d8054e72633.jpg)  
(d). The Asymmetrical Topology  
Fig. 10. Topologies for three engineering tasks.

Assume, as in Example 3, that there are two mutually exclusive states for the environment as far as the introduction of the new product is concerned; either the state of the environment is good (state $S_{1}$ ) and the product should be introduced, or it is bad (state $S_{0}$ ) and the project should be abandoned or at least delayed. Also assume that the costs and prior probabilities are known.

Table 14  
Prob. mass functions for the observations of the DE, ME and RE in example 5

<table><tr><td> $P(Y|S_0)$ </td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td> $P(Y|S_1)$ </td><td>0.0</td><td>0.2</td><td>0.6</td><td>0.2</td></tr><tr><td>Y</td><td>0</td><td>1</td><td>2</td><td>3</td></tr></table>

Table 15  
Cost and prior probability assignments for example 5

<table><tr><td></td><td> $P(S_0)$ </td><td> $P(S_1)$ </td><td> $C(0, S_0)$ </td><td> $C(1, S_0)$ </td><td> $C(0, S_1)$ </td><td> $C(1, S_1)$ </td><td> $\eta$ </td></tr><tr><td>Assignment 1</td><td>0.50</td><td>0.50</td><td>25</td><td>75</td><td>50</td><td>0</td><td>1.0</td></tr><tr><td>Assignment 2</td><td>0.75</td><td>0.25</td><td>25</td><td>100</td><td>50</td><td>0</td><td>4.5</td></tr></table>

Each engineer performs an extensive analysis to form his or her own personal assessment of the situation. Each engineer's assessment can be summarized as follows: either the product will most likely be a failure (Y = 0), or the product will probably be a failure (Y = 1), or the product will probably be a success $(Y=2)$ , or the product will most likely be a success $(Y=3)$ . The conditional probability mass functions of the observations given the true state of the environment are presented in Table 14. The corresponding ROC curve is presented in Fig. 11.

![](/api/attachments/JT3KF6B4/fulltext/images/fc555ead8cdb3dcf77993365173746e4a5cdb3ca81827c39df94e33c53bd9960.jpg)  
Fig. 11. ROC curve for the DE, ME and RE in example 5.

Assume that the RE and the DE can only communicate one of two messages; either that the system should go ahead with the production of the new product ( $\nu = 1$ ) or that the project should be abandoned ( $\nu = 0$ ). We would like to find the topology that minimizes the expected cost for each of the two assignments of costs and prior probabilities of Table 15. It had been conjectured in the literature that the two consultant topology is optimal [9,20]. But, as we demonstrate the optimal topology depends not only on the characteristics of the system (e.g., the engineers involved), but also on factors that are external to the organization; that is factors that the system cannot control, like the costs and the prior probabilities.

Table 16  
Optimal task decision rules and expected cost for both architectures of example 6

<table><tr><td>Archit.</td><td>Tandem</td><td>Two-consultant</td></tr><tr><td colspan="3">Assignment 1</td></tr><tr><td>RE</td><td> $\gamma_{2}^{r}(Z) = 0 \text{ for } Z = 0, 1 \text{ and } 1 \text{ for } Z = 2, 3$  $(P_{F}^{r}, P_{D}^{r}) = (0.2, 0.8)$ </td><td> $\gamma_{2}^{r}(Z) = 0 \text{ for } Z = 0, 1 \text{ and } 1 \text{ for } Z = 2, 3$  $(P_{F}^{r}, P_{D}^{r}) = (0.2, 0.8)$ </td></tr><tr><td>DE</td><td> $\gamma_{2}^{d}(Y, w) = 0 \text{ otherwise and } 1 \text{ for } Y(2w + 1) > 2$  $(P_{F}^{d0}, P_{D}^{d0}) = (0.0, 0.2)$  $(P_{F}^{d1}, P_{D}^{d1}) = (0.8, 1.0)$ </td><td> $\gamma_{2}^{d}(Y) = 0 \text{ for } Y = 0, 1 \text{ and } 1 \text{ for } Y = 2, 3$  $(P_{F}^{d}, P_{D}^{d}) = (0.2, 0.8)$ </td></tr><tr><td>ME</td><td> $\gamma_{2}^{m}(X, v) = 0 \text{ otherwise and } 1 \text{ for } X(2v + 1) > 2 \}$  $(P_{F}^{m0}, P_{D}^{m0}) = (0.0, 0.2)$  $(P_{F}^{m1}, P_{D}^{m1}) = (0.8, 1.0)$ </td><td> $\gamma_{4}^{m}(X, v, w) = 0 \text{ for } X + v + w < 3 \text{ and } 1 \text{ otherwise}$  $(P_{F}^{00}, P_{D}^{00}) = (0.0, 0.2)$  $(P_{F}^{10}, P_{D}^{10}) = (0.2, 0.8)$  $(P_{F}^{01}, P_{D}^{01}) = (0.2, 0.8)$  $(P_{F}^{11}, P_{D}^{11}) = (0.8, 1.0)$ </td></tr><tr><td>Cost</td><td>18.9</td><td>17.3*</td></tr><tr><td colspan="3">Assignment 2</td></tr><tr><td>RE</td><td> $\gamma_{2}^{r}(Z) = 0 \text{ for } Z = 0, 1 \text{ and } 1 \text{ for } Z = 2, 3$  $(P_{F}^{r}, P_{D}^{r}) = (0.2, 0.8)$ </td><td> $\gamma_{2}^{r}(Z) = 0$  for  $Z = 0, 1 \text{ and } 1 \text{ for } Z = 2, 3$  $(P_{F}^{r}, P_{D}^{r}) = (0.2, 0.8)$ </td></tr><tr><td>DE</td><td> $\gamma_{1}^{d}(Y, w) = 0 \text{ for } Y + w < 3 \text{ and } 1 \text{ otherwise}$  $(P_{F}^{d0}, P_{D}^{d0}) = (0.0, 0.2)$  $(P_{F}^{d0}, P_{D}^{d0}) = (0.2, 0.8)$ </td><td> $\gamma_{2}^{d}(Y) = 0 \text{ for } Y = 0, 1 \text{ and } 1 \text{ for } Y = 2, 3$  $(P_{F}^{d}, P_{D}^{d}) = (0.2, 0.8)$ </td></tr><tr><td>ME</td><td> $\gamma_{2}^{m}(X, v) =0 \text{ otherwise and } 1 \text{ for } X(2v + 1) > 2$  $(P_{F}^{m0}, P_{D}^{m0}) = (0.0, 0.2)$  $(P_{F}^{m1}, P_{D}^{m1}) = (0.8, 1.0)$ </td><td> $\gamma_{2}^{m}(Z, v, w) = 0 \text{ for } Z(Z + v + w) \leq 6 \text{ and } 1 \text{ otherwise}$  $(P_{F}^{00}, P_{D}^{00}) = (0.0, 0.2)$  $(P_{F}^{10}, P_{D}^{10}) = (0.0, 0.2)$  $(P_{F}^{01}, P_{D}^{01}) = (0.0, 0.2)$  $(P_{F}^{11}, P_{D}^{11}) = (0.8, 1.0)$ </td></tr><tr><td>Cost</td><td>23.75*</td><td>24.15</td></tr></table>

Consider the first cost and prior probability assignment of Table 15. We first determine the minimum expected cost for the system if the tandem topology is employed. Let us define by $(P_{F}^{r}, P_{D}^{r})$ the point of the ROC curve that the RE employs to communicate his or her message to the DE. Define by $(P_{F}^{d0}, P^{Dd0})$ the point of the ROC curve that the DE employs when the message from the RE is to abandon the project $(w=0)$ , and by $(P_{F}^{d1}, P_{D}^{d1})$ the point of ROC curve that the DE employs when the message from the RE is to go ahead with the project $(w=1)$ . Also define by $(P_{F}^{m0}, P_{D}^{m0})$ the point of the ROC curve that the ME employs when the message from the DE is to abandon the project $(\nu=0)$ , and by $(P_{F}^{m1}, P_{D}^{m1})$ the point of ROC curve that the ME employs when the message from the DE is to go ahead with the project $(\nu=1)$ .

For each of choice of decision rules, the corresponding expected cost for the system can be calculated using a long equation that is very similar to Eq. (5) and is omitted for brevity. The optimal decision rules for the tandem topology are presented in Table 16. These yield a minimum expected cost of 18.9.

Turning our attention to the two consultant topology, define by $(P_{F}^{r}, P_{D}^{r})$ the point of the ROC curve that the RE employs to communicate his or her message to the ME. Define by $(P_{F}^{d}, P_{D}^{d})$ the point of the ROC curve that the DE employs to communicate his or her message to the ME. Also define by $(P_{F}^{\nu w}, P_{D}^{\nu w})$ the point of the ROC curve that the ME employs when the message from the DE is $\nu (\nu = 0, 1)$ and the message from the RE is w (w = 0, 1). The optimal decision rules for the two consultant topology are presented in Table 16. These yield a minimum expected cost of 17.3.

Therefore, for the first cost and prior probability assignment of Table 15, the optimal topology for the system is the two consultant topology.

The algorithm that determines the optimal topology for the system is a generalization of Algorithm II. (This algorithm is also an adaptation of the likelihood ratio tests with constant but coupled thresholds that were presented in [17].) Using this algorithm for the second cost and prior probability assignment of Table 15, and duplicating the analysis described above, we obtain the optimal decision rules and associated expected cost for the two topologies; these are presented in Table 16. For the tandem topology, the optimal expected cost is 23.75. For the two consultant topology, the optimal expected cost is 24.15. Therefore, for this cost assignment the optimal topology is the tandem topology.

To summarize, for the first cost and prior probability assignment the optimal topology for the system is the two consultant topology, while for the second cost and prior probability assignment the optimal topology for the system is the tandem topology. Thus, unlike the case where the system consists of two engineers (Example 2), if the system consists of three engineers, no topology exists that is always optimal. This example again reveals the inherent complexities associated with the engineering integration topologies. Furthermore, note that no topology exists that it is always optimal if the system consists of more than three engineers. This can argued intuitively as follows: Consider a system that consists of n (n > 3) engineers; suppose that n - 3 of these engineers are very weak decision makers (i.e., their ROC curves are almost the same as the diagonal). Then, the problem of finding the optimal topology for this system of n engineers effectively reduces to finding the optimal topology for a system of three engineers, and as we saw such a topology does not exist.

## 3. Summary

Decision integration is a method to improve the quality of decision making. This research effort builds on previous results in attempting to establish the theoretical foundation of operational decision integration for such systems, and to determine the managerial implications of decision integration. A distributed hypothesis testing model is used to demonstrate that properly designed integration always improves the quality of the decisions. Several elements tary decision architectures for organizations were analyzed in order to determine the optimal architectures of integration for decision making agents. Explicit algorithmic procedures were developed to determine the optimal decision integration methods for a variety of organizations. Five motivating examples were presented to explicitly demonstrate the effectiveness of the algorithms. These procedures constitute the fundamental building blocks for analyzing the architectures of larger more realistic systems. The integration problems should be approached cautiously because counterintuitive results are common. Still, the intuitive solutions, although not necessarily optimal, result in considerable reduction in the complexity of the problem and in relatively good performance. Thus, it may be advisable to sacrifice optimality in favor of simple but reliable suboptimal solutions.

## Acknowledgements

This research was supported in part by the National Science Foundation under grant DDM-9309579, and grant DDM-92-14143, “Models for Engineering Task Integration.”

## References

[1] C. Abhijit, S.Y. Nof and A.B. Whinston, New Directions in Decision Support for Manufacturing, in: I.B. Turksen, Ed., Computer Integrated Manufacturing (Springer-Verlag, Berlin, New York, 1989) 171–188.

[2] A. Artiba and C. Tahon, Production Planning Knowledge-based System for Pharmaceutical Manufacturing Lines, European Journal of Operations Research 61 (1992) 18–28.

[3] R.G. Askin, P. Ritchie and A.H. Knight, Product and Manufacturing System Design, Proceedings of the 15th Conference on Production Research and Technology (Berkeley, CA, 1988) 489–491.

[4] M. Bielli, A DSS Approach to Urban Traffic Management, European Journal of Operations Research 61 (1992) 106–113.

[5] E. Carrizosa, E. Conde, F.R. Fernandez and J. Puerto, A Management Tool for Indicator-supported Systems: A Public Health Service Application, European Journal of Operations Research 61 (1992) 204–214.

[6] S. De, S.Y. Nof and A.B. Whinston, Decision Support in Computer Integrated Manufacturing, Decision Support Systems 1, No. 1 (1985) 37–55.

[7] P. Duchessi and R.M. O'Keefe, Contrasting Successful and

Unsuccessful Expert Systems, European Journal of Operations Research 61 (1992) 122–134.

[8] R.E. Eberts and S.Y. Nof, Distributed Planning of Collaborative Production, International Journal of Advanced Manufacturing Technology 8 (1993) 258–268.

[9] L.K. Ekchian and R.R. Tenney, Detection Networks, Proceedings of the 21st IEEE Conference on Decision and Control (1982) 686–691.

[10] T.D. Garvey et al., An Inference Technique for Integrating Knowledge from Disparate Sources, Proceedings of the 7th International Conference on AI (Vancouver, Canada, 1981).

[11] J.F. Gilmore and S.S. Shapiro, Synergistic Integration of Heuristic Reasoning in Image Understanding Systems, Proceedings of SPIE Applications of AI Conference (Orlando, FL, 1988).

[12] D.M. Green and J.A. Swets, Signal Detection Theory and Psychophysics (Wiley, New York, 1966).

[13] I.V. Hoballah and P.K. Varshney, Neyman–Pearson Detection with Distributed Sensors, Proceedings of the 25th IEEE Conference on Decision and Control (1986) 237–241.

[14] S.Y. Nof, R.E. Eberts and J.D. Papastavrou, Computer-Based Collaborative Integration of Distributed Manufacturing Engineering, Proceedings NSF Conference on Design and Manufacturing (San Diego, CA, January 1995).

[15] P. O'Grady and R.E. Young, Constraint Nets for Life Cycle Engineering: Concurrent Engineering, Proceedings of NSF Conference on Design and Manufacturing Systems (Atlanta, GA, 1992) 743–748.

[16] J.D. Papastavrou, Decentralized Decision Making in a Hypothesis Testing Environment, PhD Dissertation, LIDS-TH-1974, LIDS (MIT Press, Cambridge, MA, 1990).

[17] J.D. Papastavrou and M. Athans, On the Optimal Decision Architectures in a Hypothesis Testing Environment, IEEE Transactions on Automatic Control 37, No. 8 (1992) 1154–1169.

[18] J.D. Papastavrou and M. Athans, The Team ROC Curve in a Binary Hypothesis Testing Environment, IEEE Transactions in Aerospace and Electronic Systems 31, No. 1 (1995) 96–105.

[19] J.D. Papastavrou and Nof S.Y., Decision Integration Fundamentals in Distributed Manufacturing Topologies, IIE Transactions 24, No. 3 (1992) 27–42.

[20] A.R. Reibman and L.W. Nolte, Optimal Detection and Performance of Distributed Sensor Systems, IEEE Transactions on Aerospace and Electronic Systems AES-23 (1987) 24–30.

[21] A.R. Reibman and L.W. Nolte, Design and Performance Comparison of Distributed Detection Networks, IEEE Transactions on Aerospace and Electronic Systems AES-23 (1987) 789–797.

[22] M. Reich, Who is Them? Harvard Business Review (March–April, 1990).

[23] H. Salmela and M. Ruohonen, Aligning DSS Development with Organizational Development, European Journal of Operations Research 61 (1992) 57–71.

[24] R.R. Tenney and N.R. Sandell, Jr., Detection with Distributed Sensors, IEEE Transactions on Aerospace and Electronic Systems AES-17, No. 4 (1981) 501–510.

[25] J.N. Tsitsiklis, Decentralized Detection, to appear in Advances in Statistical Signal Processing 2: Signal Detection (1993) 297–344.

[26] J.N. Tsitsiklis and M. Athans, On the Complexity of Decentralized Decision Making and Detection Problems, IEEE Transactions on Automatic Control AC-30, No. 5 (1985) 440–446.

[27] J.N. Tsitsiklis, Decentralized Detection by a Large Number of Sensors, Mathematics of Controls, Signals and Systems 1 (1988) 167–182.

[28] H.L. Van Trees, Detection and Estimation, and Modulation Theory, Vol. I (Wiley, New York, 1968).

[29] P.J. Verbeek, Decision Support Systems — An Application in Strategic Manpower Planning of Airline Pilots, European Journal of Operations Research 55 (1991) 368–381.

[30] D. Waterman, A Guide to Expert Systems (Addison-Wesley, 1986).

![](/api/attachments/JT3KF6B4/fulltext/images/d2318ce215efec8fbe8d599be54d0fb007982e202c952ecfee7403822db50218.jpg)

Jason D. Papastavrou was born in Athens, Greece, in 1962. He received the B.S. degree in mathematics, the M.S. and Ph.D. degrees in electrical engineering all from the Massachusetts Institute of Technology, Cambridge, MA, in 1984, 1986, and 1990, respectively. Since 1990 he has been with the School of Industrial Engineering at Purdue University, West Laffayette, IN, where he is currently Assistant Professor. His research interests are in the areas of sys-

tems theory, operations research, and decentralized decision making.

![](/api/attachments/JT3KF6B4/fulltext/images/1ad103ca99a3605efcf564d20fbc6b665e5d28c5f667da6a2c25a95a8f060fa0.jpg)

Dr. Shimon Y. Nof is a Professor at Purdue University; director of the NSF and industry supported PRISM Project (Production Robotics and Integration Software for Mfg.) and co-director of Purdue's ITS (Intelligent Transportation Systems) Program. He also serves on Purdue's Technical Assistance Program for technology transfer into small-to-medium industries. Specializing in computer integrated manufacturing and industrial robotics, his recent work fo

cused on integration and collaboration of distributed agents/processors. He is a Fellow of IIE, Secretary General of IFPR, and a member of ACM, IFIP, IFAC, and SME. Dr. Nof has published over 200 articles on production engineering and information technology, is the editor of the Handbook of Industrial Robotics (Wiley, NY, 1985), Robotics and Material Flow (Elsevier Science, Amsterdam, 1986), consulting editor of Wiley's International Encyclopedia of Robotics (1988) and Concise International Encyclopedia of Robotics Applications and Automation (1990), co-editor of Advanced Information Technologies for Industrial Material Flow Systems (Springer-Verlag, Berlin, 1989) and Editor of Information and Collaboration Models of Integration (Kluwer Academic Publishers, Dordrecht, 1994.)
