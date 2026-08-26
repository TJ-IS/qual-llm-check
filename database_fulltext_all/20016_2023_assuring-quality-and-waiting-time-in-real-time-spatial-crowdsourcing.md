---
otero_id: 20016
otero_key: "HPF2Z5FQ"
title: "Assuring quality and waiting time in real-time spatial crowdsourcing"
authors: "Zhibin Wu; Lijie Peng; Chuankai Xiang"
year: "2023"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113869"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Assuring quality and waiting time in real-time spatial crowdsourcing<sup>☆</sup>

![](/api/attachments/HPF2Z5FQ/fulltext/images/59b88108213256388e87a14b9ffcfacf1edfa32a6033e40c5048c92cb346c70d.jpg)

Zhibin Wu <sup>\*</sup>, Lijie Peng , Chuankai Xiang

Business School, Sichuan University, Chengdu 610064, China

## A R T I C L E I N F O

Keywords: Spatial crowdsourcing Task assignmen Heuristic algorithm LightGBM

## A B S T R A C T

With the rapid development of mobile devices, spatial crowdsourcing has become an important way to collect data. Task assignment is an important aspect of spatial crowdsourcing. How to improve the quality of the results and decrease the travel distance has been extensively studied in recent years. Existing studies often assume that moving speed is constant or real-time road network information is known. In this paper, the travel time is predicted based on historical data. A framework for time-prediction-based task assignment approach in spatial crowdsourcing (TP-TASC) is proposed. Firstly, a prediction model based on the light gradient boosting machine (LightGBM) is used to predict the travel time of workers with the consideration of the spatial features, the temporal features, and the climate features. Secondly, a heuristic algorithm is proposed to assign the spatial crowdsourcing tasks to appropriate workers. When a task is assigned to a worker, the payment of the worker is also determined automatically. Finally, the simulation experiments based on a real-world taxi-hailing dataset show that the proposed method can not only effectively minimize the task requesters’ waiting time, but also maximize the results’ quality.

## 1. Introduction

Crowdsourcing was formally proposed in Wired Magazine for the first time in 2006 [1]. Karger et al. [2] pointed out that in the crowd sourcing systems, a large number of tasks are electronically distributed to a large number of “information pieceworkers”, which has become an effective paradigm for solving large-scale problems in many fields. In the past few years, many crowdsourcing platforms have emerged, such as AMT [3] and CrowdFlower [4]. Compared with traditional outsourcing, crowdsourcing can make better use of the free time of the public, and gather the wisdom of non-professionals with high efficiency and low cost [5–7]. So crowdsourcing has a wide range of applications in various fields, like translation, character recognition, and language recognition [8–10].

With the popularization of smart mobile devices, people can easily participate in tasks related to their location and current time [11]. Therefore, many crowdsourcing tasks have spatiotemporal attributes. A spatial crowdsourcing system consists of task requesters, workers, and a spatial crowdsourcing platform. Task requesters publish tasks on the spatial crowdsourcing platform, and workers are assigned to do these tasks. The work for the typical spatial crowdsourcing platform is to assign workers to complete tasks harmoniously with their location and current time. Spatial crowdsourcing is widely used in life. Smart freight trucks know traffic congestion on their route and can detour in advance through observing the crowdsourced data [12]. Urban planners also use smartphone microphones to monitor noise pollution [13]. Crowdshipping is an effective solution for last-mile delivery services [14].

A spatial crowdsourcing system needs a great number of workers to complete tasks [15]. Matching workers with tasks can effectively reduce costs, improve task quality [16], and reduce the burden on workers. Compared with the worker selection method in which workers actively choose tasks, the crowdsourcing platform quickly distributes many spatial crowdsourcing tasks to appropriate workers can ensure the overall utility of task completion is as high as possible. This method is called task assignment. In this case, workers cannot choose their favorite tasks, and the platform takes responsibility for task assignment. So various factors affecting task assignment need to be considered prudently.

Some task assignment strategies focus on how to decrease the dis tance from the tasks to the workers [17]. In those algorithms, the task is usually assigned to the worker that has the nearest distance to it. But the strategy based on the shortest distance assignment may not result in the shortest time. Task assignment strategy based on the shortest distance often ignores the time of tasks and workers [18,19]. Workers may not be able to complete tasks before the task expiration. And the longer the requesters’ waiting time, the lower the requesters’ satisfaction degree. To increase the requester’s satisfaction, task assignment needs to reduce the waiting time of requesters.

The existing spatial crowdsourcing task assignment methods mainly consider the Euclidean distance from the worker to the task. However, in the real world, the Euclidean distance cannot well evaluate the actual distance from the worker to the task, and the task assignment based on real-time road traffic information often requires high information costs. Some time-based assignment methods assume that workers move at a constant speed [20]. In the real world, it is more reasonable to dynamically evaluate the travel time for workers to arrive at the task location based on many factors.

To solve the problems mentioned above, a time-prediction-based task assignment approach for spatial crowdsourcing (TP-TASC) is pro posed, which has two stages, namely the prediction stage and the task assignment stage. In the prediction stage, the time required for workers to arrive at task positions is concerned. Specifically, historical data is used to predict workers’ travel time in the prediction model. In order to more accurately predict the travel time, three kinds of features: spatial features, temporal features, and climate features are considered. More specifically, a classic and effective model, the Light Gradient Boosting Machine (LightGBM) model is used. Note that, predicting the travel time of workers is used to calculate the waiting time of task requesters.

The quality of results is influenced by the reliability of the workers. Reputation modeling can effectively estimate the reliability of em ployees [21]. In other words, workers with high reputations tend to produce high-quality results. In the task assignment stage, this paper proposes a heuristic algorithm to improve the quality of results and reduce the waiting time of task requesters. In TP-TASC, workers with high reputations have more chances to be assigned.

The main contributions of this paper are as follows:

(1) An effective prediction model based on the LightGBM is used to predict workers’ travel time. Previous studies usually assumed that all workers move at a uniform speed or rely on real-time road network information. This paper builds a model based on historical data, which can effectively save information cost and improve the accuracy of travel time prediction.

(2) A heuristic algorithm is designed to assign tasks, which comprehensively considers workers’ reputation value and the spatiotemporal information of both tasks and workers, and, to maximize the quality of results and minimize the waiting time of task re questers. When a task is assigned to a worker, the payment of the worker is also obtained.

(3) To empirically validate the performance of the proposed task assignment model, extensive experiments were conducted based on a real-world taxi-hailing dataset.

The remainder of this paper is organized as follows. Section 2 re views the related work. Section 3 briefly describes the framework of the proposed model. Section 4 provides a formalization of the problem and shows the details of our model. Section 5 evaluates the proposed models, and conclusions are given in Section 6.

## 2. Related work

In this section, the related studies on task assignment models in crowdsourcing are reviewed.

Crowdsourcing tasks can fall into two categories [22]. One is simple task for which the worker can do individually, like the pickup and de livery problem, the traffic and road monitoring. The other is complex task, which may require multiple workers to complete together. Com plex tasks can be decomposed to a set of micro-subtasks that can be solved in multiple phases, like text improvement task [23]. Some com plex tasks require workers to work together [12,24]. In spatial crowdsourcing, workers need to go to specified places to complete tasks [25], such as reporting rainfall observations [26], reporting traffic conditions [27], and taking street view pictures [28]. These simple tasks should be assigned to the workers with high reputation values. In gen eral, each task only needs to be assigned to one worker. In this paper, the types of tasks are assumed to be those simple tasks.

There are three ways to ensure task results’ quality: the repeated labeling approach, the individual-oriented crowdsourcing approach, and the reputation mechanism. Firstly, for the repeated-labeling approach, if a task gets an unsatisfactory answer, the task will be repeatedly assigned to more workers [29]. Secondly, the individualoriented crowdsourcing approach focused on the personal skills of in dividual workers, and each assigned worker can complete the task individually and independently [30]. The third approach utilized reputation mechanisms to involve high-quality workers in tasks. Shi et al. [31] proposed a mechanism to ensure that workers could complete tasks with unknown answers when they were in a high-reliability state. Moayedikia et al. [32] present a novel task assignment algorithm to introduce an iterative quality measurement for task assignment. These quality-ensuring methods are proved to be effective and can be used for simple tasks. This paper follows the third approach to use the reputation values to ensure task results’ quality.

Alt et al. [33] proposed a location-based spatial crowdsourcing platform. They found that workers are mainly inclined to work close to their locations. Furthermore, GeoTruCrowd considered each worker has a different reputation value [34]. Their algorithm maximizes the num ber of allocated tasks under the constraints of the worker’s location and reputation value.

With the consideration of workers’ reputations and the Euclidian distance from workers to tasks into consideration, Miao et al. [18] emphasized the choice of workers with high reputation. They proposed a budget-aware task allocation approach for spatial crowdsourcing to maximize the tasks’ quality under a given budget. The approach clas sified workers into three categories and paid them according to their reputation. The cost of reaching the tasks’ location is defined to be same for workers in different locations. Workers farther away from the task often need more compensation to motivate them to complete the task. Wu et al. [17] considered to package the task with diversified payment. These two studies both used Euclidean distance to evaluate the distance. However, they ignored the time factors. They did not care about the task expiration time and the travel time of the worker.

Time is an important indicator for the design of a task assignment strategy. Alternatively, Ma et al. [35] searched for the best driver for a rider based on time and monetary constraints. In order to provide a good user experience and improve allocation efficiency, Guo et al. [36] designed greedy and random mechanisms to reduce the allocation time. Gao et al. [20] assumed that time is proportional to distance, that is, the workers’ speed is a constant. But at different time periods, there would be different traffic conditions, which would affect the travel time of workers. Seow et al. [37] designed a distributed taxi scheduling system based on multi-agent collaborative allocation. That task assignment al gorithm assumes that the real-time traffic information is known. How ever, not every spatial crowdsourcing platform has sufficient real-time map data (such as road network and real-time traffic information) and real-time road traffic information usually requires high information costs. And taking the Euclidean distance as the distance is usually not accurate enough in spatial crowdsourcing.

These representative task allocation algorithms for spatial crowd sourcing tasks are summarized in Table 1.

Most of these existing task allocation algorithms have focused on the result quality and distance, but ignored the task time limitation of spatial crowdsourcing tasks. In the real world, the timeout may lead to the cancellation of the task. In ride-hailing, if drivers took too long to arrive at the pick-up point, the passengers may cancel their ride orders. Excessive overtime will lead to task failure. In general, the shorter the waiting time of the task requester, the higher the requester’s satisfaction. For the estimation of travel time, many existing papers adopt the road network distance divided by the average speed. However, it is not feasible in the case of limited or missing road network infor mation, and the calculation of travel time using the average speed may lead to a large error. The LightGBM, a classic and effective prediction method, is adopted in this paper. The LightGBM is an ensemble learning model based on the decision tree algorithm [38]. It has been widely used to solve regression, prediction, and other data mining tasks due to its advantages of fast and high performance.

Summary of representative task allocation algorithms for spatial crowdsourcing tasks.

<table><tr><td>Studies</td><td>Considers result quality</td><td>Considers waiting time</td><td>Considers limited road network</td></tr><tr><td>Seow et al. [37]</td><td>×</td><td>√</td><td>×</td></tr><tr><td>Kazemi et al. [34]</td><td>√</td><td>×</td><td>×</td></tr><tr><td>Miao et al. [18]</td><td>√</td><td>×</td><td>×</td></tr><tr><td>Gao et al. [20]</td><td>×</td><td>√</td><td>×</td></tr><tr><td>Wu et al. [17]</td><td>√</td><td>×</td><td>×</td></tr><tr><td>Shi et al. [31]</td><td>√</td><td>×</td><td>×</td></tr></table>

Historical data contain a wealth of information that reflects the usual traffic conditions [39]. For some tasks, such as taking photos/videos, historical data can be used to estimate the arrival time instead of real time road information. Task assignment can be made based on the estimated travel time. Considering time prediction is helpful to assign tasks with a more accurate time, the requesters may make a more practical plan on the tasks to be completed. Therefore, this study pro poses a task assignment model based on worker travel time prediction, which aims to minimize the waiting time of task requesters and maxi mize the quality of results.

## 3. A framework for task assignment

In this section, the framework of the proposed model is shown in Fig. 1.

A time-prediction based task assignment approach for spatial crowdsourcing (TP-TASC) is proposed to assure quality and waiting time. The TP-TASC consists of two components: (1) a prediction model of worker travel time based on historical information; (2) a task assignment model to minimize the waiting time of task requesters and maximize the quality of the task. In the prediction stage, this paper predicts the time required for workers to arrive at the task location through historical data. Specifically, during the data preprocessing, the spatial features, the temporal features, and the climate features are comprehensively considered to describe the dynamics of travel time. The LightGBM model is used to predict the workers’ travel time. Furthermore, the requesters’ waiting time can be calculated. Then a heuristic algorithm assigns tasks to appropriate workers to minimize the task requester waiting time and maximize the quality of tasks.

## 4. The proposed model

This section introduces the formalization of the problem and shows the details of TP-TASC.

## 4.1. Definitions of symbols

For readability, symbols adopted in this study are shown in Table 2 in the order of their appearance.

## 4.2. Problem definition

This section first describes the relevant definitions of spatial crowdsourcing task assignment and then describes the constraints, goal, matching rules, etc.

In different spatial crowdsourcing scenarios, task assignment in volves different constraints and optimization objectives. Simple tasks, such as Waze’s traffic monitoring or Google Maps Street View, can be done easily with a smartphone camera. This study focuses on the assignment of such simple tasks to workers. Let $T = \{ t _ { 1 } , t _ { 2 } , . . . , t _ { M } \}$ be the set of M tasks in a time period. A spatial crowdsourcing task $t _ { j }$ is rep resented by a tuple $t _ { j } = \langle l _ { j } , R _ { j } , s t _ { j } , e n _ { j } , a _ { j } \rangle . ~ l _ { j }$ contains the latitude and longitude information of task $t _ { j } .$ If the distance from the task to a worker is larger than $R _ { j } ,$ , the task will not be assigned to the worker. $s t _ { j }$ and en represent the start and expiration time o $\dot { \boldsymbol { { \mathbf { \ell } } } } t _ { j }$ respectively. $a _ { j }$ is the priority of task $t _ { j } .$ In addition, the maximum waiting time of task $t _ { j }$ is defined as its valid time val , which is obtained by $e n _ { j } - s t _ { j }$ . In spatial crowdsourcing scenario, a task can only be done after a worker arrives at a specific location. Noteworthily, in this study, if the worker arrives at a task location before the task expiration, then it is assumed that the task is completed.

![](/api/attachments/HPF2Z5FQ/fulltext/images/79407b08af0b42338311326cd85b68a352a7859f0e053415d9486a44c68abc98.jpg)  
Fig. 1. The framework of TP-TASC.

Table 2 List of symbols.

<table><tr><td>Symbols</td><td>Meaning</td></tr><tr><td> $j$ </td><td>Subscript of the spatial crowdsourcing task  $t_j$ </td></tr><tr><td> $T$ </td><td>Task set</td></tr><tr><td> $l_j$ </td><td>Locations (latitude and longitude) of task  $t_j$ </td></tr><tr><td> $M$ </td><td>The total number of tasks in a spatial crowdsourcing system</td></tr><tr><td> $R_j$ </td><td>Acceptable radius for task  $t_j$ </td></tr><tr><td> $(st_j, en_j)$ </td><td>The start and expiration time of the task  $t_j$ </td></tr><tr><td> $a_j$ </td><td>The priority of task  $t_j$ </td></tr><tr><td> $val_j$ </td><td>Valid time of the task  $t_j$ </td></tr><tr><td> $i$ </td><td>Subscript of the spatial crowdsourcing worker  $w_i$ </td></tr><tr><td> $W$ </td><td>Worker set</td></tr><tr><td> $l_i$ </td><td>A location (latitude and longitude) of worker  $w_i$ </td></tr><tr><td> $r_i$ </td><td>Worker  $w_i$ &#x27;s reputation</td></tr><tr><td> $N$ </td><td>The total number of workers in a spatial crowdsourcing system</td></tr><tr><td> $(st_i, en_i)$ </td><td>Time of appearance and time of departure of worker  $w_i$ </td></tr><tr><td> $d_{ij}$ </td><td>Distance from worker  $w_i$  to task  $t_j$ </td></tr><tr><td> $ER$ </td><td>Earth radius</td></tr><tr><td> $W_{ij}$ </td><td>Task requester  $j$ &#x27;s waiting time if task  $t_j$  is allocated to worker  $w_i$ </td></tr><tr><td> $s_{ij}$ </td><td>The travel time of worker  $w_i$  arriving at task  $t_j$ &#x27;s location  $l_j$ </td></tr><tr><td> $Q_j$ </td><td>Set for workers that can complete task  $t_j$ </td></tr><tr><td> $P_{ij}$ </td><td>Worker  $w_i$ &#x27;s payment for completing task  $t_j$ </td></tr><tr><td> $e$ </td><td>The compensation ratio</td></tr><tr><td> $Th_{HM}$ </td><td>The threshold to distinguish between high and medium reputation values</td></tr><tr><td> $Th_{ML}$ </td><td>The threshold to distinguish between medium and low reputation values</td></tr><tr><td> $i_j$ </td><td>Worker  $w_i$  is selected for task  $t_j$ </td></tr><tr><td> $S$ </td><td>Set of all matching relationships</td></tr><tr><td> $B$ </td><td>Total budget</td></tr><tr><td> $P_j$ </td><td>Task  $t_j$ &#x27;s payment</td></tr><tr><td colspan="2">Measurement indicators</td></tr><tr><td> $\alpha$ </td><td>Average waiting time</td></tr><tr><td> $\beta$ </td><td>Average reputation of the selected workers</td></tr><tr><td> $\gamma$ </td><td>Average cost</td></tr><tr><td> $\delta$ </td><td>Assignment rate</td></tr><tr><td> $\in$ </td><td>Average travel distance</td></tr></table>

Let $W = \{ w _ { 1 } , w _ { 2 } , . . . , w _ { N } \}$ be a set of N workers in a time period. A spatial crowdsourcing worker w is represented by a tuple $w _ { i } = \langle l _ { i } , r _ { i } , s t _ { i } .$ en 〉. l contains the latitude and longitude information of the worker w . $r _ { i }$ is the reputation value of worker $w _ { i } .$ . It represents the historical probability of workers being selected to complete the task, which is obtained from statistical data $( r _ { i } \in [ 0 , 1 ] )$ ). The lower the value of $r _ { i } ,$ the lower the worker’s reputation. In this paper, workers are roughly divided into three categories: low reputation workers, medium reputa tion workers, and high reputation workers. Th separates high and medium reputation workers, and $T h _ { M L }$ separates high and medium reputation workers. It is obvious that $0 { \leqslant } T h _ { M L } { \leqslant } T h _ { H M } { \leqslant } 1$ . The reputation value determines the worker’s priority for tasks. st and en represent the start and expiration time of $w _ { i }$ respectively. The valid time of worker $w _ { i } .$ $\nu a l _ { i } ,$ is obtained by $e n _ { i } - s t _ { i }$

The distance between all tasks and workers based on longitude and latitude is computed by Haversine formula [40]. The distance, $d _ { i j } ,$ , from worker w to task $t _ { j }$ is defined as

$$
d _ {i j} = 2 E R ^ {*} \arcsin \sqrt {\sin^ {2} (\frac {\text { lat } _ {i} - \text { lat } _ {j}}{2}) + \cos (\text { lat } _ {i}) \cos (\text { lat } _ {j}) \sin^ {2} (\frac {\text { long } _ {i} - \text { long } _ {j}}{2}))},\tag{1}
$$

where ER is earth radius, lat and long are latitude and longitude of task $t _ { j }$ respectively, lat and long are latitude and longitude of worker w respectively.

Let $W _ { i j }$ be the requester $j ^ { \prime } s$ waiting time if task $t _ { j }$ is allocated to worker $w _ { i } ,$ then $W _ { i j }$ is determined by

$$
W _ {i j} = \left(s t _ {i} - s t _ {j}\right) + s _ {i j},\tag{2}
$$

where $s t _ { i }$ is the start time of $w _ { i } , s t _ { j }$ is the start time of $t _ { j } , s _ { i j }$ is the travel time of w to $t _ { j } .$ .

In task assignment, the travel time of each task and each worker could require a very long time to be computed. To improve the computing speed, a worker filtering method is proposed. For a task, we can find suitable workers in a certain range around it, and add the workers who meet the distance limit into the candidate worker pool for the task. $Q _ { j }$ is a set of candidate workers for $t _ { j } .$ . Workers who satisfy the distance of task $t _ { j }$ will be added into $Q _ { j } .$ . That is, if the distance from worker w to task $t _ { j }$ is larger than the accepted radius $R _ { j } ( d _ { i j } > R _ { j } ) _ { i }$ , worker $w _ { i }$ will be rejected by task $t _ { j } . \mathrm { ~ } Q _ { j } = \{ w _ { 1 _ { j } } , w _ { 2 _ { j } } , w _ { 3 _ { j } } , \ldots \}$ represents all workers who may complete task t .

In order to motivate workers to complete tasks, certain economic benefits should be given to workers who complete tasks [41,42]. In this paper, worker w ’s payment for task $t _ { j } , P _ { i j } ,$ is determined by travel time $s _ { i j }$ and the reputation of $w _ { i } ,$

$$
P _ {i j} = e \cdot s _ {i j} \cdot r _ {i},
$$

where e represents the compensation ratio.

(3)

## 4.3. Time prediction model

The LightGBM is developed to predict $s _ { i j } .$ . The essence of the travel time estimation problem is a regression problem. Ensemble learning as a kind of advanced machine learning method is one of the most popular approaches to solve the regression problems [43]. On one side, in order to assign tasks to workers and reduce the waiting time of tasks effi ciently, it is required that the time prediction model should have a high forecast precision and a high running speed. On the other side, the LightGBM is a powerful model in ensemble learning and is suitable for big data due to its faster training speed and higher efficiency. The reli ability of the LightGBM has been proved in many fields, such as the train delay prediction [44], the protein–protein interactions prediction [45], and the short-term traffic flow prediction [46]. Considering these rea sons, the LighTGBM is selected as the time prediction model in this paper. The prediction model using the LightGBM is not theoretical new. However, like the existing researches [44–46], the contribution of using the LightGBM lies in the development of features and determination of hyperparameters for the LightGBM algorithm in a practical problem. In the following, this section first introduces the LightGBM, and then it is focused on developing the selected features and determining the hyperparameters.

Given a training data set with n examples, the purpose of the LightGBM is to find a function $f _ { t } ,$ which minimizes the expected value of the loss function. Specifically, the iteration process can be described as

$$
\widehat {y} _ {i} ^ {h} = \widehat {y} _ {i} ^ {(h - 1)} + f _ {h} (\mathbf {x} _ {i}),\tag{4}
$$

where $\widehat { \boldsymbol { y } } _ { i } ^ { h }$ is the ith prediction value at the hth iteration. $f _ { h }$ represents the residuals of the corresponding tree. $\mathbf { x } _ { i }$ is the ith training data.

According to Eq. (4), each new prediction value is generated from its residuals and the previous prediction value. The whole training process can be described as Eq. (5), and the objective function and residual can be expressed as Eqs. (6) and (7).

$$
\left\{ \begin{array}{l} \widehat {y} _ {i} ^ {0} = 0 \\ \widehat {y} _ {i} ^ {1} = f _ {1} (\mathbf {x} _ {i}) = \widehat {y} _ {i} ^ {0} + f _ {1} (\mathbf {x} _ {i}) \\ \widehat {y} _ {i} ^ {2} = f _ {1} (\mathbf {x} _ {i}) + f _ {2} (\mathbf {x} _ {i}) = \widehat {y} _ {i} ^ {1} + f _ {2} (\mathbf {x} _ {i}) \\ \dots \\ \widehat {y} _ {i} ^ {h} = \sum_ {k = 1} ^ {h} f _ {k} (\mathbf {x} _ {i}) = \widehat {y} _ {i} ^ {h - 1} + f _ {h} (\mathbf {x} _ {i}) \end{array} , \right.\tag{5}
$$

$$
\widehat {\boldsymbol {\theta}} _ {h} = \arg \min _ {\boldsymbol {\theta}} \sum_ {i = 1} ^ {n} L (y _ {i}, \widehat {y} _ {i} ^ {h}) + R (f _ {h}),\tag{6}
$$

$$
R (f _ {h}) = \rho T + \frac {1}{2} \sigma \sum_ {j = 1} ^ {T} v a l u e _ {j} ^ {2},\tag{7}
$$

where y is the true value, $\widehat { \boldsymbol { y } } _ { i } ^ { t }$ is the prediction value, $\textstyle \sum I$ is the sum of the loss between each group of y and $\widehat { \boldsymbol { y } } _ { i } ^ { h } .$ . k represents the kth decision tree. θ is the parameter vector in the LightGBM. $\textstyle \sum R$ is the penalty of nodes, which presents the complexity of decision trees. T represents the number of leaf nodes in the tree. value is the value of the jth leaf node in the tree. The complexity of the decision tree model is determined by the number of leaf nodes in the generated tree and the $L _ { 2 }$ norm score corresponding to leaf nodes. $\rho$ and σ control the weights to determine whether the number of leaves in the tree is more important or the value of leaf nodes.

In addition, the LightGBM adopts a Gradient-based One-Side Sam pling (GOSS) algorithm to discard some samples that are not helpful to the calculation of information divergence. According to the definition of information divergence, the sample with a larger gradient has a greater impact on information divergence. Therefore, GOSS only retains the data with a large gradient when sampling. However, if all the data with a small gradient are directly discarded, the overall distribution of the data will inevitably be affected. Therefore, the GOSS algorithm sorts the samples based on the absolute value of the gradient. It deletes most samples with small gradients, and only adopts the remaining samples to compute the information divergence. By doing this, it balances the amount of data and ensures accuracy.

In order to reasonably construct and extract features, the influencing factors of travel time need to be analyzed first. According to the influ encing factors, the corresponding data should be selected and the fea tures should be extracted. There are many factors affecting the travel time of workers, which can be roughly divided into three aspects: (1) The spatial factors: different starting places affect the travel time. Some travel routes are outside the city, the road along this kind of route is clear. Some travel routes are in densely populated areas. There are many pedestrians and vehicles along these travel routes, and the travel time is longer. (2) The temporal factor: different departure times have different vehicle conditions [47]. The travel time is longer in rush hours and shorter in non-rush hours. (3) The climate factors: It showed that the weather factors have an impact on travel times [48]. The LightGBM is used to estimate the travel time according to spatial, temporal, and climate features in this paper.

Under the condition of considering these factors, there are 14 related features were considered in the time prediction model. $( x _ { 1 i } , x _ { 2 i } , \cdots , x _ { 1 4 i } , y _ { i } ) ^ { T }$ represents ith sample data. The 14 independent variables are shown as follows. Spatial features include the latitude of tasks $( x _ { 1 } ) _ { i }$ , the longitude of tasks $( x _ { 2 } )$ , the latitude of workers $( x _ { 3 } ) ,$ the longitude of workers $\left( x _ { 4 } \right)$ , distance between tasks and workers (x ), and direction of tasks and workers $\left( x _ { 6 } \right)$ . Temporal features include the day of the month $( x _ { 7 } )$ , the hour of the day $( x _ { 8 } )$ , the minute of the day $\left( x _ { 9 } \right)$ , and the second of the minute $\left( x _ { 1 0 } \right)$ . Climate features include the maximum temperature $( x _ { 1 1 } )$ , the minimum temperature $( x _ { 1 2 } ) _ { : }$ , the average tem perature $\left( x _ { 1 3 } \right)$ , and the air quality index $\left( x _ { 1 4 } \right)$ . The dependent feature y is the travel time.

The main hyperparameters used in the LightGBM algorithm control and optimization include: (1) learning rate: the higher the learning rate, the faster the iteration speed. (2) n estimators: the number of weak generators, which is used to control the number of iterations. (3) num leaves: the number of leaf nodes, which is used to adjust the complexity of the tree. (4) max depth: the maximum depth of the tree, which is set to prevent the model from overfitting.

In this study, the hyperparameters are given as learning $. r a t e \mathrm { ~ = ~ } 0 . 1$ , n estimators = 500, num leaves = 1000, and max depth = 25.

## 4.4. Task assignment model

When the information of workers and tasks is known, the goal of the spatial crowdsourcing platform is to assign tasks to appropriate workers.

While minimizing the requester’s waiting time, the assignment strategy should ensure the quality of assigned tasks. The quality of the results is influenced by the reliability of the workers reflected by their reputation level [21]. In this paper, we aim to minimize the waiting time of the requester and maximize workers’ reputations. The objectives can be expressed as:

$$
\left\{ \begin{array}{l} \min \frac {1}{| S |} \sum_ {i _ {j} \in S} W _ {i _ {j} j} \\ \max \frac {1}{| S |} \sum_ {i _ {j} \in S} r _ {i _ {j}}, \end{array} \right.\tag{8}
$$

where $i _ { j }$ represents worker w is selected for task $t _ { j } , S$ is the set of all matching relationships, |S| is the number of elements in set ${ \cal { S } } , { \cal { W } } _ { i _ { j } j }$ is the task requester $j ^ { \prime } s$ waiting time if task $t _ { j }$ is assigned to worker $w _ { i } , r _ { i _ { j } }$ is worker w<sub>i</sub>’ reputation value if task $t _ { j }$ is assigned to worker w<sub>i</sub>.

The proposed task assignment method is described in Algorithm1. It contains three stages. In the first stage, the LightGBM is trained, then some data like the distance and travel time for each worker and task are calculated. For a task, the workers who satisfy spatial constraints are selected to be candidate workers. This step can effectively reduce the number of candidates to reduce the complexity of spatial crowdsourcing task assignment. In the second stage, workers with high reputation value are assigned to do tasks. In the last stage, workers with medium repu tation value are assigned to do tasks.

Algorithm1

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: A spatial crowdsourcing system with N workers and M tasks, training data set, parameters, budget B.

Output: Set of all matching relationship S.

1: Train the LightGBM model using the training data set according to Section 4.3;
2:  $S = \{\varnothing\}; k = 0; TP = 0;$ 
3: Rank tasks in an ascending order according to their priority  $a_{j}$ ;
4: forj = 1 to M do
5:    fori = 1 to N do
6:    Compute  $d_{ij}$  according to Eq. (1);
7:    Compute  $s_{ij}$  according to the LightGBM model;
8:    Compute  $W_{ij}$  according to Eq. (2);
9:    if  $d_{ij} &lt; R_{j}$  &amp;  $st_{j} + W_{ij} &lt; en_{j}$  &amp;  $st_{i} + W_{ij} &lt; en_{i}$  then
10:    Put worker  $w_{i}$  into set  $Q_{j}$ ;
11: forj = 1 to M do
12:    for high reputation workers in  $Q_{j}$  do
13:    Select the worker  $w_{i}$  with minimum  $W_{ij}$ ;
14:    Calculate the payment for worker i according to Eq. (3);
15:    $TP = TP + P_{j}$ ;
16:    ifTP &lt; Bthen
17:    k = k + 1;
18:    $S(k,:) = (k, t_{j}, w_{i}, P_{j}, W_{ij})$ ;
19: for unassigned task do
20:    for medium reputation workers in  $Q_{j}$  do
21:    Select the worker  $w_{i}$  with minimum  $W_{ij}$ ;
22:    Calculate the payment for worker i according to Eq. (3);
23:    $TP = TP + P_{j}$ ;
24:    ifTP &lt; Bthen
25:    k = k + 1;
26:    $S(k,:) = (k, t_{j}, w_{i}, P_{j}, W_{ij})$ ;
27: return set S.
</div>

When the spatial crowdsourcing platform assigns tasks, the training date set is firstly used to train the lightGBM model. the well-trained model is then used to predict the travel time $s _ { i j }$ (Line 1). Next, the al gorithm ranks the tasks in an ascending order according to their prior ities $a _ { j }$ (Line 3). Then the distance $d _ { i j }$ and travel time $s _ { i j }$ for worker $w _ { i }$ and task $t _ { j }$ are calculated (Line 5 to Line 8). Workers who satisfy the distance and time limitation will be added into the candidate worker set $Q _ { j }$ for task $t _ { j }$ (Line 9 and Line 10). These previous steps exclude remote and overtime workers, which effectively reduce the number of candidates in task assignment to improve the computation efficiency. The high repu tation workers in $Q _ { j }$ will be assigned tasks with higher priority (Line 11 to Line 18). After all high reputation workers have been assigned, me dium reputation workers are selected to do the unassigned tasks in the last assignment (Line 19 to Line 26). When a worker is assigned to a task, the payment is calculated at the same time (Line 14 and Line 22).

Remark 1. Reinforcement learning is a kind of popular method to solve the task assignment problem [49–51]. Reinforcement learning is the novel method for combinatorial optimization, which is essentially a Markov decision process suitable for dynamic decisions. Following the existing research line [17,18], the task assignment scenario considered in this paper is static. The proposed heuristic task assignment algorithm is more suitable for solving such a problem. It is an interesting future research direction to use reinforcement learning to solve task assign ment problems.

## 4.5. Discussion for decision support system

In this section, the relevance of the proposed approach to decision support system (DSS) is discussed.

Inspired by [52], a typical spatial crowdsourcing decision making process is given in Fig. 2. The key elements of the spatial crowdsourcing decision-making process are divided into five basic components: the task, the worker, the spatial crowdsourcing planform, the task execution process, and the evaluation. In the beginning, the task requesters may decide to use crowdsourcing to complete one specified spatial task (or a series of spatial tasks). The requester then ‘submit’ their tasks to the spatial crowdsourcing platform. The tasks are then assigned to the workers through the spatial crowdsourcing platform. The framework of TP-TASC shown in Fig. 1 can be used in the task assignment process to select the appropriate workers. Then in ‘task execution process’, the selected workers ‘perform tasks’. After the process, the ‘outcomes’ are collected. In the ‘evaluation’ step, the platform and the task requesters evaluate the workers and the outcomes to get ‘task results’ and ‘workers reputation value’. The evaluation step may vary according to the application scenarios. In the application of taking street view pictures, the photos taken from many workers could be combined into a complete 3D street view map. In taxi hailing, some workers may not pick up passengers, and their outcome is task failure. If another worker picks up the passengers, then the overall task result is that the task has been completed. The workers’ reputation value will affect the next task assignment. The task requester can then use the task results to solve the problem.

A DSS could be built based on the prosed task assignment strategy. The spatial crowdsourcing platform, the worker, and the task requester all can benefit from such a DSS.

With respect to the crowdsourcing platform, the DSS can automati cally select appropriate workers to execute tasks. The reduction of in dividual task completion time can increase the number of tasks. A shorter task completion time increases the task completion rate, implying that the platform is more efficient in assigning tasks.

For the workers, assigning the workers who can reach the task location fastest can shorten the time for each worker to complete a task. Therefore, the workers have more opportunities to do more tasks. Further, an increase in the number of completed tasks increases the total payments of workers. It can encourage workers to participate in crowdsourced tasks.

For the task requesters, the faster arrival time of workers means less waiting time for the task requesters, which reduces the time cost for both parties. A shorter waiting time of task requesters is conducive to improving the satisfaction degree of the task requesters.

## 5. Experimental evaluation

In this section, several experiments are given to validate the pro posed models in practice. Comparisons with the existing approach is also given.

## 5.1. Dataset

In this paper, the effectiveness of the proposed algorithm is validated by the GAIA open dataset [53]. The dataset includes the order dataset in Chengdu in November 2016. The data from the 1st to the 10th weekday (1–4 and 7–10) of November 2016 are selected as the real dataset. It contains 1467309 pieces of order data. The spatiotemporal information of workers and tasks was selected according to the order data set. We take the order start location and time as the worker location and start time. The order end location is regarded as the task location. The travel time is calculated by the order end time minus the order start time. At the same time, the corresponding weather data were collected.<sup>1</sup> The main preprocessing procedures are demonstrated as follows:

• Add the maximum temperature $( x _ { 1 1 } )$ , the minimum temperature $( x _ { 1 2 } ) _ { \mathrm { { ; } } }$ , the average temperature $( x _ { 1 3 } ) _ { \mathrm { { ; } } }$ , and the air quality index $( x _ { 1 4 } )$ from the weather data set to the train and test dataset. The weather data is matched with the order data based on date.

• Change the format of the date in the train and test datasets. Add some features: the day of the month (x ), the hour of the day $\left( \boldsymbol { x } _ { 8 } \right)$ , the minute of the day (x ), and the second of the minute (x ).

• In order to prevent the abnormal travel time from affecting the simulation results, only the samples where travel time is within two standard deviations above or below the mean are kept.

• Calculate the distance between tasks and workers $\left( x _ { 5 } \right)$ and the di rection of tasks and workers (x ).

• The distribution of travel time is right-skewed, so a logtransformation of travel time is done.

More details are available online.<sup>2</sup>

Some data are randomly selected to simulate spatial crowdsourcing tasks and workers. In the task assignment, 2000 pieces of worker data and 1000 pieces of task data were selected. The default parameters used in our experiments are summarized in Table 3.

## 5.2. Prediction stage

The algorithm proposed in this paper firstly uses the training data to get a model to estimate the arrival time. The estimated time of arrival is a regression problem. The evaluation metric of the model used in this paper is Root Mean Squared Logarithmic Error (RMSLE), and Mean Absolute Error (MAE). RMSLE and MAE are defined as

$$
R M S L E = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} \left[ l o g (\widehat {y} _ {i} + 1) - l o g (y _ {i} + 1) \right] ^ {2}}\tag{9}
$$

$$
M A E = \frac {1}{n} \sum_ {i = 1} ^ {n} | \widehat {y} _ {i} - y _ {i} |\tag{10}
$$

where n is the total number of observations for travel time, $\widehat { \boldsymbol { y } } _ { i }$ is the predicted variable, $y _ { i }$ is the actual value. The smaller the RMSLE and MAE, the better the model.

In this paper, Python 3.7 was used to get the function of the LightGBM. Under the settings described in the Section 4.3 for the LightGBM, it follows that: RMSLE = 0.2368,MAE = 0.0236.

## 5.3. Evaluation metrics

The following five metrics are used in the evaluation:

![](/api/attachments/HPF2Z5FQ/fulltext/images/8a2ecdad7854d8b392958118e8d89f65e4109eaca0d81a8771d02a79f04c0ccd.jpg)  
Fig. 2. The spatial crowdsourcing process for decision support.

Table 3  
The default parameter settings.

<table><tr><td>Parameter</td><td>Settings</td></tr><tr><td>Worker&#x27;s reputation ( $r_i$ )</td><td> $N(0.8, 0.2)$ </td></tr><tr><td>Discount rate (e)</td><td>1</td></tr><tr><td>The threshold of high and medium reputation ( $Th_{HM}$ )</td><td>0.7</td></tr><tr><td>The threshold of medium and low reputation ( $Th_{ML}$ )</td><td>0.6</td></tr><tr><td>Task radius ( $R_j$ ) (km)</td><td>2</td></tr><tr><td>Valid time of tasks ( $en_j - st_j$ ) (second)</td><td>1800</td></tr><tr><td>Valid time of workers ( $en_i - st_i$ ) (second)</td><td>1800</td></tr></table>

(1) Average waiting time (α): This metric is calculated as average time from start to completion of the assigned task,

$$
\alpha = \frac {1}{| S |} \sum_ {i _ {j} \in S} W _ {i _ {j} j}.\tag{11}
$$

(2) Average reputation value of all selected workers (β): The metric is calculated as the average reputation value of all selected workers,

$$
\beta = \frac {1}{| S |} \sum_ {i _ {j} \in S} r _ {i _ {j}}.\tag{12}
$$

(3) Average cost (γ): The metric is calculated as the ratio of total cost of assigned spatial crowdsourcing tasks to the number of all assigned spatial crowdsourcing tasks,

$$
\gamma = \frac {1}{| S |} \sum_ {i _ {j} \in S} P _ {i _ {j} j}.\tag{13}
$$

(4) Assignment rate (δ): The metric is the ratio of assigned tasks to the total number of spatial crowdsourcing tasks,

$$
\delta = \frac {| S |}{| M |}.\tag{14}
$$

(5) Average travel distance (∊): The metric is calculated as the average travel distance by the selected workers for those assigned spatial crowdsourcing tasks,

$$
\epsilon = \frac {1}{| S |} \sum_ {i _ {j} \in S} d _ {i _ {j} j}.\tag{15}
$$

For task requesters, the first metric, the second metric, and the fifth metric should be as low as possible, and the other two metrics should be as high as possible.

## 5.4. Comparative experiments and discussion

This paper compares the RB-TPSC approach with our model in the five metrics mentioned above. The RB-TPSC approach focuses on the problem of task package allocation [17], aiming at improving the task allocation rate and the expected quality, and it not considering time limitations. The simulation experiments are done under the default parameter settings shown in Table 3. In the experiment, task radius (km), the valid time of tasks (second), the valid time of workers (sec ond), and the mean value of workers’ reputation values are changed to simulate different scenes. The analysis under different parameter set tings helps compare different approaches.

Radius is an important factor in Algorithm 1 for the task assignment stage. The value of task radius provides a circular range whose center is the location of the task [54]. In the matching problem for ride-sourcing markets, the matching radius between drivers and passengers is in general imposed in most matching algorithms [55]. In the context of this paper, a bigger value of task radius implies that more workers can be selected as candidate workers for the given task. Following the setting of [17], the default task radius is set to 2 km. In the simulation, the task radius changes from 0.5 to 5 units in the first experiment. The experi mental results are shown in Fig. 3.

As Fig. 3 shown, the average reputation is better than that of RB-TPSC. In general, the higher the value of task radius, the higher the values for the five evaluation metrics except for average reputation. Due to the fact that more remote workers are assigned to do tasks, the task assignment rate increases. However, the average waiting time increases.

The valid time of tasks changes from 300 to 1800 s in the second experiment. The results at different valid time of tasks are shown in Fig. 4. The average reputation is better than that of RB-TPSC while the average waiting time is similar. The reason why the trends of average distance and average waiting time are similar may be that the distance and the travel time are generally positively correlated. When more similar data exist in the historical data, the estimation of the LightGBM

![](/api/attachments/HPF2Z5FQ/fulltext/images/123132465dc0064d727d709e5956300571f297a8463fc143c9696da0fcb192a0.jpg)  
(a)

![](/api/attachments/HPF2Z5FQ/fulltext/images/e9009b11d51561996ee8ac3b1b24df57ccbceba5df2573ab387666d658dcb2a8.jpg)  
(b)

![](/api/attachments/HPF2Z5FQ/fulltext/images/c0bc47062402185cc427d61b2e454ad1554fae6fa6bd509c65ff0c1b779ebe48.jpg)  
(c)

![](/api/attachments/HPF2Z5FQ/fulltext/images/f5ce09024e305033c8ff0d8ca541d3297739a866c984b1434a9071f9c5a7f7fd.jpg)  
(d)

![](/api/attachments/HPF2Z5FQ/fulltext/images/f8dc3d0ee18fbe59d4be6387f5fcfa0f9852f28e8cec41926aef60ee4bcc33ad.jpg)

![](/api/attachments/HPF2Z5FQ/fulltext/images/486ed65d4b0d18b0751c4da1b3dd92170616f4486d577e347189392bb3c9d23d.jpg)

(e)  
Fig. 3. Main results for different task radius.  
![](/api/attachments/HPF2Z5FQ/fulltext/images/caf9be4519e7ccf0c1aef1d82aa1b201c24c5d5cee055b9792e20f4e89284e8a.jpg)  
(a)

![](/api/attachments/HPF2Z5FQ/fulltext/images/0bf9487cf213d8269d46f529d202f195d6e4454ae341a6531b33d99c4b1b87b9.jpg)  
(b)

![](/api/attachments/HPF2Z5FQ/fulltext/images/e4ef88f1045476c279875c5447999166fe27ca9d6aa0982c617d8cf0d5fc98b8.jpg)  
(c)

![](/api/attachments/HPF2Z5FQ/fulltext/images/cfa76399c3fb3a946e79920f3f5098fd6b1e13661540d90d9f4090649749a1e3.jpg)  
(d)

![](/api/attachments/HPF2Z5FQ/fulltext/images/a15adb17e65bb623328d8457451575b6e99e8ad749abff88119cf041d6d262d1.jpg)  
(e)

![](/api/attachments/HPF2Z5FQ/fulltext/images/390943878950427bbe86a310fcf8621975f7888bb2c8f69807dd937842b471a4.jpg)  
Fig. 4. Main results for different valid time of tasks.

will be more accurate.

The valid time of workers changes from 300 to 1800 s in the third simulation experiment. The results are shown in Fig. 5. The average waiting time is better than that of RB-TPSC. The proposed task assign ment model can assign tasks to appropriate workers.

According to Figs. 3–5, when the task radius, the valid time of tasks, and the valid time of workers increase, the average waiting time have an increasing trend. The reason is that more remote workers are assigned tasks. At the same time, the average payment is increased. Analyzing those settings can provide meaningful advice for spatial crowdsourcing platforms to set an appropriate task assignment strategy.

A fourth experiment assigned tasks to groups of workers of different quality. Assuming that workers’ reputation values obey normal distri bution, the mean value of workers’ reputation values changes from 0.7 to 0.9, and the standard deviation difference is 0.2. The results are shown in Fig. 6.

As Fig. 6 shown, the average waiting time of TP-TASC was lower than that of RB-TPSC, and the reputation value of TP-TASC was higher than

![](/api/attachments/HPF2Z5FQ/fulltext/images/7d81cd63b6728c70029b1f7426d78807d57b4cfe1f96a7b87669b87910752cb6.jpg)  
(a)

![](/api/attachments/HPF2Z5FQ/fulltext/images/4d653afa67aa54f6ac2a96b6502d8fae85e7c479afc60b81fdfb0d681512ba0b.jpg)  
(b)

![](/api/attachments/HPF2Z5FQ/fulltext/images/573c2d42efd69fedada0ac441d71fcc6270c5b54bbd9153d07ff758771eed9a1.jpg)  
(c)

![](/api/attachments/HPF2Z5FQ/fulltext/images/a73bd703047890afa5ea36860b39e41461c8fde78114c5d637508f8f9cb0b7a5.jpg)  
(d)

![](/api/attachments/HPF2Z5FQ/fulltext/images/df8987f2621c3952b89c6c6c1fdf22567f4749d400f043d6fd53d4dfc7fcca39.jpg)

![](/api/attachments/HPF2Z5FQ/fulltext/images/055619670c7742b43a882ac5a4431486fbedb5f1e5db8e2d41ca77de25ef608e.jpg)

(e)  
Fig. 5. Main results for different valid time of workers.  
![](/api/attachments/HPF2Z5FQ/fulltext/images/94c0b32682947ca72a5c2230ddb957405d9abaa25cb1704d92e9e8e321623777.jpg)  
(a)

![](/api/attachments/HPF2Z5FQ/fulltext/images/a3b87b7b954760b639087e955e309dd15a67d6cb0db0556d8f17c007fcfeea8b.jpg)  
(b)

![](/api/attachments/HPF2Z5FQ/fulltext/images/3a8b4eb4786967f037cabc50bb4df04e23a62dfcfac85937a43add6fd8819a03.jpg)  
(c)

![](/api/attachments/HPF2Z5FQ/fulltext/images/8586fcc6eea80a252af2c6eb17620e7640dce97af8558fceee305672b567ef17.jpg)  
(d)

![](/api/attachments/HPF2Z5FQ/fulltext/images/4b014d33bc6f1b40dfba53884decb88e3ddf5459f3016df0a2571e26c47ef5ae.jpg)  
(e)

![](/api/attachments/HPF2Z5FQ/fulltext/images/853b43d5e93b68473dc44c906cf0da054a2fdbd74dfd4539e4b8990a9595d5a8.jpg)  
Fig. 6. Main results for different workers’ mean reputation values.

that of RB-TPSC.

Some studies can predict the task demand and the number of workers in the region in advance. After predicting the short-term demand of a certain region, the method proposed in this study provides a method for the advanced scheduling of workers. And it can analyze the supply and demand within the region for a given time period. In a specific area and time, if the number of tasks waiting to be assigned is small and the task requester’s average waiting time is short, some workers can be assigned to other areas to improve the total number of assigned tasks in all areas.

By doing so, it can reduce the waiting time of task requesters in all areas with fewer workers and improve the satisfaction of task requesters.

## 6. Conclusions

This paper provides a framework for time-prediction-based task assignment in spatial crowdsourcing. The proposed model includes two stages. In the first prediction stage, the LightGBM model is used to es timate worker travel time according to spatial, temporal, and climate features. In the second task assignment stage, a heuristic algorithm with the goal of minimizing the requesters’ waiting time and maximizing selected workers’ reputation is designed to assign tasks. When a task is assigned to a worker, the cost of that match is determined.

An efficient task assignment strategy can optimize the sup ply–demand relationship, improve the quality of assigned tasks, and reduce the travel cost of workers. On the other hand, it can reduce the waiting time of task requesters and improve task requesters’ satisfaction degree. The contribution of this paper can be summarized as follows:

(1) An effective prediction model based on the LightGBM is used to predict the workers’ travel time. Previous studies usually assumed that all workers move at a uniform speed or rely on real-time road network information. This paper builds a model based on historical data, which can effectively save information costs and improve the accuracy of travel time prediction.

(2) A heuristic algorithm is designed to assign tasks, which comprehensively considers the spatio-temporal information of spatial crowdsourcing tasks and workers, and workers’ reputation value, to maximize the quality of results and minimize the waiting time of task requesters.

(3) To empirically validate the performance of the proposed task assignment model, extensive experiments were done based on a realworld taxi-hailing dataset. Experiments show that TP-TASC can reduce the waiting time of task requesters and effectively improve the task quality under a low budget.

The research has implications for crowdsourcing platforms. In spatial crowdsourcing, the framework proposed in this paper can make auto matic decisions to assign tasks to suitable workers. Before task assign ment, the method proposed in this paper can estimate the waiting time of the task requesters in advance according to various factors, and can filter out workers with overtime from the candidate worker pool. TP-TASC can assign tasks to workers who can complete tasks on time and improve the satisfaction of the task requesters. Assigning tasks to the workers who can complete the tasks fastest is conducive to improving the efficiency of the task assignment system. Within a certain time range, the shorter the time to complete the tasks, the more the number of tasks will be completed. In the long run, the task assignment rate will also be improved and the revenue of the platform will be increased. The pro posed approach can be used for traffic and road monitoring. After modification, it can also be used on crowdsourced takeout platforms to determine assignment based on reliability and speed.

There are some limitations that provide avenues for future research. Firstly, the tasks are assigned in a static environment in this paper. The proposed method does not consider how to balance the requester waiting time for assignment with the potential benefits of expected future tasks in a dynamic environment. In the real world, it makes sense to balance the two factors. Future studies can consider how to balance the requester waiting time for assignment with the potential benefits of expected future tasks in a dynamic environment. Secondly, the predic tion accuracy of the prediction model influences the quality of the re sults in the task assignment stage. To improve the prediction accuracy of the travel time prediction model, the difference in data distribution in different periods is worth considering. And in some crowdsourcing en vironments, it is also meaningful to consider the task cancellation probability in future research.

## CRediT authorship contribution statement

Zhibin Wu: Conceptualization, Methodology, Writing-originaldraft, Supervision, Writing-review-editing, Funding-acquisition. Lijie Peng: Methodology, Software, Writing-original-draft, Writing-reviewediting. Chuankai Xiang: Writing-review-editing.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

The authors do not have permission to share data.

## Acknowledgments

The authors are grateful to the editors and anonymous reviewers for their insightful comments which have lead to an improved version of this paper.

## References

[1] J. Howe, The rise of crowdsourcing, Wired Magazine 14 (6) (2006) 1–4

[2] D.R. Karger, S. Oh, D. Shah, Budget-optimal task allocation for reliable crowdsourcing systems, Oper. Res. 62 (1) (2014) 1–24.

[3] Amazon Mechanical Turks (AMT).https://www.mturk.com/. Accessed: 20.03.2021.

[4] CrowdFlower.http://www.crowdflower.com/. Accessed: 20.03.2021.

[5] N. Luz, N. Silva. P. Novais. A survey of task-oriented crowdsourcing. Artif. Intell Rev, 44 (2) (2015) 187–213.

[6] Y. Tong, Y. Yuan, Y. Cheng, L. Chen, G. Wang, Survey on spatiotemporal crowdsourced data management techniques, J. Softw. 28 (1) (2017) 35–58

[7] R.Y. Ali, S. Shekhar, S. Athavale, E. Marsman, ULAMA: a utilization-aware matching approach for robust on-demand spatial service brokers, Future Gener. Comput. Syst. 108 (2020) 1030–1048.

[8] P. Cheng, L. Chen, J. Ye, Cooperation-Aware Task Assignment in Spatial Crowdsourcing, in: 2019 IEEE 35th International Conference on Data Engineering (ICDE), 2013, pp. 1442–1453

[9] A. Persaud, S. O’Brien, Quality and acceptance of crowdsourced translation of web content, in: Social Entrepreneurship: Concepts, Methodologies, Tools, and Applications, 2019, pp. 1177–1194.

[10] R.M. Borromeo, T. Laurent, M. Toyama, M. Alsayasneh, S. Amer-Yahia, V. Leroy, Deployment strategies for crowdsourcing text creation, Inf. Syst. 71 (2017)

[11] B. Guo, Y. Liu, L. Wang, V.O. Li, J.C. Lam, Z. Yu, Task allocation in spatial crowdsourcing: current state and future directions, IEEE Internet Things J. 5 (3) (2018) 1749–1764.

[12] S. Chandra, R.T. Naik, J. Jimenez, Crowdsourcing-based traffic simulation for smart freight mobility, Simul. Model. Pract. Theory 95 (2019) 1–15.

[13] G. Marques, R. Pitarma, Noise mapping through mobile crowdsourcing for enhanced living environments, in: International Conference on Computational Science, 2019, pp. 670–679.

[14] S. Nieto-Isaza, P. Fontaine, S. Minner, The value of stochastic crowd resources and strategic location of mini-depots for last-mile delivery: a Benders decomposition approach, Transp. Res. B: Methodol. 157 (2022) 62–79.

[15] E. Estell´es-Arolas, F. Gonzalez-Ladr´ on-de-Guevara, ´ Towards an integrated crowdsourcing definition. J. Inf. Sci, 38 (2) (2012) 189–200

[17] P. Wu, E.W. Ngai, Y. Wu, Toward a real-time and budget-aware task package allocation in spatial crowdsourcing, Decis, Support Syst, 110 (2018) 107–117

[18] C. Miao, H. Yu, Z. Shen, C. Leung, Balancing quality and budget considerations in mobile crowdsourcing, Decis, Support Syst. 90 (2016) 56–64.

[19] L.B. Zheng, L. Chen, Multi-Campaign Oriented Spatial Crowdsourcing, IEEE Trans.

[20] G. Gao, M. Xiao, Z. Zhao, Optimal multi-taxi dispatch for mobile taxi-hailing systems, in: 2016 45th International Conference on Parallel Processing (ICPP). 2016, pp. 294–303.

[21] A. Jøsang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decis, Support Syst, 43 (2) (2007) 618–644.

[22] W. Wang, J. Jiang, B. An, Y. Jiang, B. Chen, Toward efficient team formation for crowdsourcing in noncooperative social networks, IEEE Trans. Cybern. 47 (12) (2017).4208–4222

[23] J. Jiang, B. An, Y. Jiang, D. Lin, Context-aware reliable crowdsourcing in social networks, JEEE Trans, Syst, Man Cybern.: Syst, 50 (2) (2020) 617–632

[24] H. Gimpel, V. Graf-Drasch, R.J. Laubacher, M. Wohl, ¨ Facilitating like Darwin: supporting cross-fertilisation in crowdsourcing, Decis. Support Syst. 132 (2020), 113282.

[25] S. Wan, D. Zhang, A. Liu, J. Fang, Extra-budget aware task assignment in spatial crowdsourcing, in: International Conference on Web Information Systems Engineering, 2021, pp. 636–644.

[26] L. Tran, H. To, L. Fan, C. Shahabi, A real-time framework for task assignment in hyperlocal spatial crowdsourcing. ACM Trans. Intell. Syst. Technol. (TIST) 9 (3) (2018) 1–26.

[27] F. Tang, H. Zhang, Spatial task assignment based on information gain in crowdsourcing, IEEE Trans. Netw. Sci. Eng. 7 (1) (2019) 139–152.

[28] M.F. Goodchild, Citizens as sensors: the world of volunteered geography, GeoJournal 69 (4) (2007) 211–221.

[29] A. Moayedikia, W. Yeoh, K.L. Ong, Y.L. Boo, Improving accuracy and lowering cost in crowdsourcing through an unsupervised expertise estimation approach, Decis. Support Syst. 122 (2019), 113065.

[30] J. Jiang, B. An, Y. Jiang, C. Zhang, Z. Bu, J. Cao, Group-oriented task allocation for crowdsourcing in social networks, IEEE Trans. Syst. Man Cybern.: Syst. 51 (7) (2019) 4417–4432.

[31] P. Shi, W. Wang, Y. Zhou, J. Jiang, Y. Jiang, Z. Hao, J. Yu, Practical POMDP-based test mechanism for quality assurance in volunteer crowdsourcing, Enterp. Inf. Syst. 13 (7–8) (2019) 979–1001

[32] A. Moayedikia, H. Ghaderi, W. Yeoh, Optimizing microtask assignment on crowdsourcing platforms using Markov chain Monte Carlo, Decis. Support Syst. 139 (2020), 113404.

[33] F. Alt, A.S. Shirazi, A. Schmidt, U. Kramer, Z. Nawaz, Location-based crowdsourcing: extending crowdsourcing to the real world, in: Proceedings of the 6th Nordic Conference on Human-Computer Interaction: Extending Boundaries, 2010, pp. 13–22.

[34] L. Kazemi, C. Shahabi, L. Chen, Geotrucrowd trustworthy query answering with spatial crowdsourcing, in: Proceedings of the 21st ACM Sigspatial International Conference on Advances in Geographic Information Systems, 2013, pp. 314–323.

[35] S. Ma, Y. Zheng, O. Wolfson, Real-time city-scale taxi ridesharing, IEEE Trans. Knowl. Data Eng. 27 (7) (2014) 1782–1795.

[36] G. Guo, Y. Xu, A deep reinforcement learning approach to ride-sharing vehicle dispatching in autonomous mobility-on-demand systems, IEEE Intell. Transp. Syst. Mag. 14 (1) (2022) 128–140.

[37] K.T. Seow, N.H. Dang, D.H. Lee, A collaborative multiagent taxi-dispatch system, IEEE Trans. Autom. Sci. Eng. 7 (3) (2009) 607–616.

[38] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, et al., LightGBM: a highly efficient gradient boosting decision tree, in: Advances in Neural Information Processing Systems, 2017, pp. 30.

[39] M.A. Esfeh, L. Kattan, W.H. Lam, M. Salari, R.A. Esfe, Road network vulnerability analysis considering the probability and consequence of disruptive events: a spatiotemporal incident impact approach, Transp. Res. C: Emerg. Technol. 136 (2022), 103549.

[40] K. Gade, A non-singular horizontal position representation, J. Navig. 63 (3) (2010) 395–417.

[41] L. Tran-Thanh, S. Stein, A. Rogers, N.R. Jennings, Efficient crowdsourcing of unknown experts using bounded multi-armed bandits, Artif. Intell. 214 (2014)

[42] X. Shi, R.D. Evans, W. Shan, What motivates solvers’ participation in crowdsourcing platforms in China? A motivational-cognitive model. JEEE Trans. Eng, Manage. (2022) 1–13.

[43] C. Bent´ejac, A. Csorg¨ o, ˝ G. Martínez-Munoz, ˜ A comparative analysis of gradient boosting algorithms. Artif, Intell, Rey, 54 (3) (2021) 1937–1967.

[44] H. Laifa, H.H.B. Ghezalaa, Train delay prediction in Tunisian railway through LightGBM model, Proc. Comput, Sci, 192 (2021) 981–990.

[45] C. Chen, Q. Zhang, Q. Ma, B. Yu, LightGBM-PPI: predicting protein-protein interactions through LightGBM with multi-information fusion, Chemometr. Intell. Lab. Syst. 191 (2019) 54–64.

[46] Z. Mei, F. Xiang, L. Zhen-hui, Short-term traffic flow prediction based on combination model of Xgboost-Lightgbm. in: 2018 International Conference on Sensor Networks and Signal Processing, 2018, pp. 322–327.

[47] Z. Wall, D.J. Dailey, An algorithm for predicting the arrival time of mass transit vehicles using automatic vehicle location data, in: 78th Annual Meeting of the Transportation Research Board, 1999, pp. 1–11.

[48] J. Patnaik, S. Chien, A. Bladikas, Estimation of bus arrival times using APC data. J. Public Transp. 7 (1) (1999) 1.

[49] T. Ahamed, B. Zou, N.P. Farazi, T. Tulabandhula, Deep reinforcement learning fo crowdsourced urban delivery, Transp. Res. B: Methodol. 152 (2021) 227–257.

[50] Y. Guo, Y. Zhang, Y. Boulaksil, Real-time ride-sharing framework with dynamic timeframe and anticipation-based migration, Eur. J. Oper. Res. 288 (3) (2021) 810–828.

[51] M. Haliem, G. Mani, V. Aggarwal, B. Bhargava, A distributed model-free ridesharing approach for joint matching, pricing, and dispatching using deep reinforcement learning, IEEE Trans. Intell. Transp. Syst. 22 (12) (2021) 7931–7942.

[52] C. Chiu, T. Liang, E. Turban, What can crowdsourcing do for decision support? Decis. Support Syst. 65 (2020) 40–49.

[53] GAIA open dataset.https://outreach.didichuxing.com/research/opendata/ Accessed: 20.03.2021

[54] Y. Tong, Z. Zhou, Y. Zeng, L. Chen, C. Shahabi, Spatial crowdsourcing: a survey, VLDB J. 29 (1) (2020) 217–250.

[55] H. Yang, X. Qin, J. Ke, J. Ye, Optimizing matching time interval and matching radius in on-demand ride-sourcing markets, Transp. Res. B: Methodol. 131 (2020) 84–105.

![](/api/attachments/HPF2Z5FQ/fulltext/images/f5f7d37dd059d0fbcec61ed866c0a200b78719061dcd662dcf1a5763d5245ca4.jpg)

Zhibin Wu received the Ph.D. degree in management science and engineering from Sichuan University, Chengdu, China, in 2012. He is currently a professor at the Business School, Sichuan University, Chengdu, China. His published more than 40 international peer-reviewed journal papers in Decision Support Systems, European Journal of Operational Research, Fuzzy Sets and Systems, Group Decision and Negotiation, IEEE Transactions on Cybernetics, IEEE Transactions on Fuzzy Systems, and Omega, among others. His research interests include group decision making, crowdsourcing, and machine learning with applications.

![](/api/attachments/HPF2Z5FQ/fulltext/images/fc58cca4009aeef5ab86211c001dcac73842b8f0babc294edefb6e1cc43941d0.jpg)

Lijie Peng is currently a graduate student at Sichuan Univer sity. Her research interests include spatial crowdsourcing and machine learning

Chuankai Xiang is currently a Ph.D. student at Sichuan Uni versity. His research interests include artificial intelligence application in transportation research, spatial crowdsourcing and machine learning.

![](/api/attachments/HPF2Z5FQ/fulltext/images/22c6d2c83b84d2ace0da0c388c03172418150aa483bd58a350683efcdda7cb24.jpg)
