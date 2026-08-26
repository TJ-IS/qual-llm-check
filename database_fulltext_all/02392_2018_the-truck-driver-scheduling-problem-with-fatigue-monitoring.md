---
otero_id: 2392
otero_key: "FPZNAQVG"
title: "The truck driver scheduling problem with fatigue monitoring"
authors: "Zachary E. Bowden; Cliff T. Ragsdale"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.03.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

## The truck driver scheduling problem with fatigue monitoring

Zachary E. Bowden, Cliff T. Ragsdale

![](/api/attachments/FPZNAQVG/fulltext/images/e8c8bbe9f2dfebceaf6e3c1301096aae8d3b3148f0d89198dfc9cd0fb1e93910.jpg)

<table><tr><td>PII:</td><td>S0167-9236(18)30048-4</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.03.002</td></tr><tr><td>Reference:</td><td>DECSUP 12937</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>22 May 2017</td></tr><tr><td>Revised date:</td><td>9 March 2018</td></tr><tr><td>Accepted date:</td><td>9 March 2018</td></tr></table>

Please cite this article as: Zachary E. Bowden, Cliff T. Ragsdale , The truck driver scheduling problem with fatigue monitoring. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi:10.1016/j.dss.2018.03.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# The Truck Driver Scheduling Problem with Fatigue Monitoring

Zachary E. Bowden<sup>1</sup> and Cliff T. Ragsdale<sup>2</sup>

1: Virginia Tech Transportation Institute

2: Department of Business Information Technology, Virginia Tech

## Abstract

In the United States, approximately 4,000 fatalities due to truck and bus crashes occur each year. Of these, up to 20% are estimated to involve fatigued drivers [48]. However, no model currently exists that incorporates a measure of drowsiness or fatigue into the Truck Driver Scheduling Problem (TDSP). We introduce a fatigue-aware model for determining the optimal schedule for a driver while maintaining an acceptable level of alertness as well as abiding by time windows and hours of service (HOS) regulations. Additionally, we examine a shortcoming in existi regulations, specifically related to assumptions made about the rest and alertness of a driver at the start of the workweek.

## KEYWORDS

Vehicle Scheduling, Scheduling Policies, Scheduling Systems, Alertness, Fatigue Management

# ACCEPTED MANUSCRIPT

## The Truck Driver Scheduling Problem with Fatigue Monitoring

## 1. Introduction

Driver fatigue has been empirically identified as a major factor in vehicle crashes [15]. Approximately 4,000 fatalities due to truck and bus crashes occur each year in the United States. Of these, up to 20% are estimated to involve fatigued drivers [48]. In a previous study, Bowman et al. [10] conclude that driver fatigue is the probable cause of 30% of crashes. Fatigue has also been shown to significantly increase the number of close calls and near crashes in commercial truck driving [47]. While in-vehicle accident hotspot warnings based on locational analytics offer one promising technology for reducing highway accidents [53], research into fatigue monitoring, prediction, and optimization offers another important opportunity for improving traffic safety.

For commercial trucks, many countries (and the European Union) have hours of service (HOS) regulations that attempt to control the amount of fatigue a truck driver experiences while driving [12,21]. When these regulations are modified, studies are conducted attempting to quantify the effect of the changes on safety outcomes [7,30]. These regulations attempt to balance the safety benefits with the added costs of compliance. Quantifying these benefits, costs, and other factors introduced with regulatory compliance is an area of active research. However, the currently available results point to significant opportunity for additional research, particularly with respect enforcing regulations that produce the desired safety benefits without being overly burdensome [31,37,41].

Various mathematical models and solution techniques for the Truck Driver Scheduling Problem (TDSP) and Vehicle Routing Problem (VRP) incorporating HOS constraints have been suggested in the literature [6,25,26,59]. Goel and Vidal [27] model and compare several countries’ HOS constraints from both a cost and risk standpoint. However, we have been unable to find a model that incorporates fatigue into the model itself. Véronneau and Cimon [58] address the challenges of maintaining robust decision capability through so-called critical operations such as piloting aircraft, navigating ships, conducting military operations, and controlling aircraft traffic. They conclude that in such scenarios, “careful consideration must be given to the interplay among humans, systems, and the environment in which they operate” [58]. We posit that driving heavy trucks at high speeds on congested interstates also represents a critical operation where incorporating human fatigue into the scheduling process can improve the safety of the resulting system.

Mathematical models for predicting alertness have existed at least since Borbely’s two-process model was published in 1982 [8]. Since then several additional models have been published, many of which are derived from Borbely’s initial work and produce similar results [57]. See Mallis et al. [45], Gundel et al. [28], and Dawson et al. [17] for a review of these models. Additionally, it has been shown that one can predict vehicle crashes reasonably well with a mathematical model that uses a sleep/wake predictor based on the Three Process Model of Alertness [2]. The Three Process Model of Alertness (TPMA) is itself an extension of Borbely’s original model.

We extend the Truck Driver Scheduling Problem with Fatigue Monitoring (TDSPFM) by incorporating the TPMA. This allows us to create schedules where the driver is most likely to remain alert, thereby reducing the likelihood of a crash. A key contribution of this work is that it facilitates the quantification and understanding of the magnitude of the tradeoff between route duration and alertness levels. Additionally, the extended model provides a comparative basis for measuring the effectiveness of different types of TDSPFM models that incorporate HOS regulations. Finally, our model allows us to examine how the initial alertness level of a driver impacts predicted fatigue levels throughout the rest of the week.

## 2. Literature Review

As mentioned earlier, there exists an established body of research around both the VRP and TDSP with a wide array of variations and additional constraints [19,33,40,54,56]. Additionally, the literature on fatigue prediction is reasonably well established [14,17,60]. What is missing, and the void this paper seeks to fill, is the merger of these two areas of research to create a mathematical model for determining optimal driving schedules while maintaining an acceptable level of predicted alertness. The fact that, heretofore, there has not been a TDSPFM does not imply that there is no research into reducing driver fatigue. Fatigue detection is an active area of research and product development [11,14,44,60].

# ACCEPTED MANUSCRIPT

However, in all of the articles we reviewed, the focus was on detecting driver fatigue in the vehicle. Generally speaking, the goal of that research/work is to alert the driver before an accident occurs by using data captured during the trip. For instance, one could use yawn and blinking frequency to predict fatigue using computer vision technologies [38] and then alert the driver when the fatigue estimate crosses some pre-defined threshold.

Workplace fatigue has been well-studied and results in “an unsafe condition in the workplace” [42]. Entire systems of accounting for and managing the risk that fatigue introduces, aptly named Fatigue Risk Management Systems (FRMS), have been defined and advocated [22]. Workplace fatigue research is also directly applicable to vehicle crashes [42]. The Fatigue Avoidance Scheduling Tool (FAST) based on the Sleep, Activity, Fatigue, and Task Effectiveness (SAFTE) model has been developed for the aviation and rail transportation industries, but also has applicability to driver scheduling [34]. The Circadian Alertness Simulator (CAS) has also been applied to managing driver fatigue risk [46]. The North American Fatigue Management Program provides training to address issues of driver fatigue by way of online courses and presentations [49].

## 2.1 Theoretical Foundations of Fatigue Research

A thorough summary of the history and current state of the broad topic of theoretical fatigue research is provided by Hockey [32], showing that formal, published research into the theory of fatigue and its practical application goes back at least to the 1890s. Fatigue is a complex construct that can be modeled and defined in many different ways [50]. Chalder et al. describe the concept of fatigue as “both a ubiquitous symptom and is difficult to define” [13]. Gander et al. define fatigue as “the inability to function at the desired level due to incomplete recovery from the demands of prior work and other waking activities” [23]. These “demands of prior work” could refer to a high level of exertion (e.g., long hours of manual labor in the hot sun for instance) and would result in being “worn out” at the end of the day. Fatigue researchers typically refer to this type of fatigue as physical fatigue; where one’s body is physically tired, out of energy, and needs rest. Alternatively, the “demands of prior work” could refer to driving a tractor-trailer all day, resulting in a driver that is very mentally fatigued at the end of the day.

We build on the theoretical research and modeling efforts related to mental fatigue; particularly mental fatigue as it relates to sleep and recovery.

The most effective (and some posit the only) way to recover from mental fatigue is with sleep [18]. While a full night’s sleep is a very common way to obtain this recovery, the literature suggests that shorter sleep periods (such as napping) are quite effective as well [18]. Much research has focused on modeling and predicting when fatigue reaches a critical point where sleep is needed, the amount of sleep needed at a time, and the frequency at which sleep periods should occur. Prior research has attempted to study fatigue in a variety of industries (e.g., airlines, trucking, oil and gas pipelines, etc.) and covers a variety of individual differences (e.g., sleep disorders, sleep deprivation, mental disabilities, etc.).

Our focus is on developing a general-purpose modeling approach for scheduling problems involving the biomathematical modeling of fatigue. Over the past several decades, researchers developed biomathematical models of fatigue that build on the theoretical foundations of current fatigue research. Mallis et al. [45] describe biomathematical fatigue models as “models that quantify the effects of circadian and sleep/wake processes on the regulation of alertness and performance … in an effort to predict the magnitude and timing of fatigue-related responses in a variety of contexts.” The TPMA is one of the most popular biomathematical fatigue models that has been part of the fatigue literature for decades [9] including works to validate and extend the model [3,36].

## 2.2 Three Process Model of Alertness (TPMA)

The TPMA model utilized in this research consists of three primary processes that have been published previously [4] and are described briefly below. Process C represents the circadian influence on alertness; this process encompasses the effect that the time of day can have on sleepiness. Process S describes the exponential decline in alertness as a function of the time awake. This decline is then reversed in process S’ which describes recovery as a function of the time asleep. Figure 1 shows the way these processes effect alertness at different times during the day. The TPMA model also includes a process W that describes the lack of alertness at the time of waking up. Since we assume driving does not take place immediately following waking up, we ignore the W in this research. Finally, since the original publication of the TPMA model, another process has been added [1]. This process is U, which stands for “ultradian” and explains an afternoon dip in alertness.

## { Insert Figure 1 here. }

For the implementation of our TDSPFM model, we use the validated TPMA model and parameters presented in [36]. Therefore, our model predicts alertness while driving as the summation of S+C+U. This produces an alertness score with values ranging from 1 to 21. According to the sleep literature, a TPMA value (or score) of “3” corresponds to extreme sleepiness, while “14” represents high alertness, and “7” to a borderline sleepiness threshold [4]. While a minimum allowed alertness score is a required parameter in our model, the appropriate value of this parameter is a matter for further research.

## 2.3 Alertness Score Levels

An advantage of the TPMA alertness score is that it can be transformed into a prediction of the subjective Karolinska Sleepiness Scale (KSS) which has been shown to be a valid means for measuring sleepiness [39]. The KSS is a scale that “measures the subjective level of sleepiness at a particular time during the day” [55] and was introduced by Åkerstedt and Gillberg [5]. Because the KSS is obtained by simply asking a driver to rate their sleepiness on a 9-point Likert scale, future research could validate the schedules and alertness scores proposed by our model. The transformation from TPMA to KSS is based on the work by Ingre et al. [36] and can be calculated as follows:

$$
\mathrm{KSS} = 1 0. 7 5 - (0. 4 6 * \text { TPMA   alertness   score })
$$

This allows us to transform a TPMA alertness score into a KSS score and vice-versa. More research has been done correlating KSS to driver drowsiness and suggests that an appropriate sleepiness threshold for drivers may be higher than the suggested value of 7 from existing sleep literature [2,35,43]. One important difference between the TPMA alertness scale and the KSS is that the TPMA measures alertness whereas the KSS measures sleepiness. Therefore, a high KSS value implies the subject is sleepy and thus less alert whereas a high TPMA alertness score implies the subject is highly alert. To complicate matters, both the KSS and the TPMA use a value of 7 as the sleepiness threshold. This can make

# ACCEPTED MANUSCRIPT

switching between TPMA and KSS confusing. To avoid confusion, we only use TPMA values for results and parameter values, converting KSS values from previously published research to TPMA equivalents.

## 2.4 Sleep Assumptions

When implementing the TDSPFM in this paper, we make some conservative estimates regarding sleep. First, we assume that the driver is well-rested and alert at the start of their workweek. Second, we do not consider caffeine or other drug use that could affect the driver’s level of sleepiness or alertness. Additionally, we assume that when the driver takes a long rest break, they get an uninterrupted period of recovering sleep. In other words, we do not factor in things like sleep disorders, noise and other distractions inhibiting sleep, or drivers that choose to do things other than sleep during the time when they could be sleeping.

It is worth noting that the TPMA allows one to predict sleep schedules and to factor in those results into the alertness recovery process (S’). For this paper, we will not take advantage of this functionality in favor of simplifying the driver scheduling process. However, it is an area to consider for future research. The reader is encouraged to see [2] for more information.

## 2.5 Hours of Service Regulations

In general, HOS regulations function primarily by imposing rules related to how long drivers may stay on the road, the conditions relating to rest frequency, and the duration/types of rest periods. As a result, a driver’s schedule for a particular day might appear as shown in Figure 2. In the remainder of this paper we consider the HOS regulations in the United States, though other HOS restrictions could easily be accommodated by our model.

{ Insert Figure 2 here. }

## 3. Mathematical Model

Our model for the TDSPFM pursues the objective of finding the schedule that has the minimal route duration while maintaining an acceptable level of alertness, abiding by HOS regulations, and complying with the time windows at each location on the route. We consider a sequence of N locations to be visited by a truck driver. As in [24] and [25], we assume that all rest breaks occur at stops along the

# ACCEPTED MANUSCRIPT

route. Since the sequence of locations and driving time between locations is fixed, the primary decisions required are those regarding the duration of rest periods at each location denoted by $r _ { i }$ for all $i \in N$

Each location $i \in N$ has a time window and some duration of work associated with it. We let the opening time window of each location be zero for the sake of simplicity and focus on the closing time window, which is denoted as $L _ { i }$ for each $i \in N$ . The work duration is denoted as $w _ { i }$ for each location ?? ∈ $t _ { i , i + 1 }$ arrival time and departure time of each location $i \in N$ is denoted as $A _ { i }$ and $D _ { i }$

The route duration to minimize is the difference between the arrival time at the final location and the departure time at the first location. We use parameters representative of the HOS regulations in the United States as defined and explained in Goel [26]. These parameters and their associated values used in our implementation of the TPMA are displayed in Table 1 and come from Ingre et al. [36].

$$
\{\text {   Insert   Table   1   here.   } \}
$$

In order to abide by the HOS regulations, we track the following variables, presented along with their associated definitions:

 HOS regulations limit the amount of time spent driving between long rest breaks. We compute total time driving since the last long rest upon arriving at location i, $k _ { i } ^ { d r i v e }$

$$
k _ {i} ^ {d r i v e} = \left\{ \begin{array}{l l} k _ {i - 1} ^ {d r i v e} + t _ {i - 1, i}, & r _ {i - 1} <   t ^ {r e s t} \\ t _ {i - 1, i}, & r _ {i - 1} \geq t ^ {r e s t} \end{array} \right., \forall i \in N
$$

 In addition to driving time, HOS regulations limit the amount of time a driver is on duty between long rest breaks. We compute the time on duty since the last long rest upon arriving at location $i ,$ $k _ { i } ^ { d u t y }$

$$
k _ {i} ^ {d u t y} = \left\{ \begin{array}{l l} k _ {i - 1} ^ {d u t y} + t _ {i - 1, i} + r _ {i - 1} + w _ {i}, & r _ {i - 1} <   t ^ {r e s t} \\ t _ {i - 1, i} + w _ {i} & , \quad r _ {i - 1} \geq t ^ {r e s t} \end{array} \right., \forall i \in N
$$

 HOS regulations also ensure that drivers take short breaks during their time spend on duty. We calculate the time elapsed since the driver’s last break upon arriving at location i, $k _ { i } ^ { b r e a k }$

$$
k _ {i} ^ {b r e a k} = \left\{ \begin{array}{l l} k _ {i - 1} ^ {b r e a k} + t _ {i - 1, i} + r _ {i - 1} + w _ {i}, & r _ {i - 1} <   t ^ {b r e a k} \\ t _ {i - 1, i} + w _ {i}, & r _ {i - 1} \geq t ^ {b r e a k} \end{array} \right., \forall i \in N
$$

To determine the alertness of the driver at a given location i (??????????????????<sub>i</sub>), we need to introduce the following variables:

 The time the driver has been awake upon arriving at location i, $k _ { i } ^ { a w a k e }$

$$
k _ {i} ^ {\text {awake}} = \left\{ \begin{array}{l l} k _ {i - 1} ^ {\text {awake}} + t _ {i - 1, i} + r _ {i - 1} + w _ {i} & , \quad r _ {i - 1} <   t ^ {\text {rest}} \\ t _ {i - 1, i} + (r _ {i - 1} - t ^ {\text {maxsleep}}) + t ^ {\text {awakedelay}} + w _ {i}, & r _ {i - 1} \geq t ^ {\text {rest}} \end{array} \right., \forall i \in N
$$

 The time of day upon arriving at location i, $k _ { i } ^ { d a y }$ :

$$
k _ {i} ^ {d a y} = A _ {i} \mod 2 4, \forall i \in N
$$

Finally, we show the calculations related to the components of the TPMA that allow us to compute an alertness score at a given location i (alertness<sub>i</sub>):

 Process S at location i, S<sub>i</sub>:

$$
S _ {i} = l a + (S _ {i - 1} ^ {\prime} - l a) * e ^ {d * k _ {i} ^ {a w a k e}} \forall i \in N
$$

 Subprocess $S B _ { i } ,$ used to determine the proper $S _ { \textit { i } } ^ { \prime }$ to use:

$$
S B _ {i} = h a - (h a - s s _ {i}) e ^ {g \left(t ^ {m a x s l e e p} - t ^ {s l e e p d e l a y}\right)}, \forall i \in N
$$

where

$$
s s _ {i} = l a + (S _ {i - 1} ^ {\prime} - l a) e ^ {d (k _ {i} ^ {a w a k e} + t ^ {s l e e p d e l a y})}, \forall i \in N
$$

 Process $\mathrm { \Delta S ^ { \prime } }$ at location i, S’<sub>i</sub>:

$$
S ^ {\prime} _ {i} = \left\{ \begin{array}{l l} h a - (h a - b l) e ^ {g \left(t ^ {m a x s l e e p} - t ^ {s l e e p d e l a y} - b t _ {i}\right)} \quad , & r _ {i - 1} \geq t ^ {r e s t} A N D S B _ {i} \geq b l \\ S _ {i} + g \big (t ^ {m a x s l e e p} - t ^ {s l e e p d e l a y} \big) * (b l - h a), & r _ {i - 1} \geq t ^ {r e s t} A N D S B _ {i} <   b l \quad , \forall i \in N \\ S ^ {\prime} _ {i - 1} & r _ {i - 1} <   t ^ {r e s t} \end{array} \right.
$$

 Process C at location $i , \mathbf { C } _ { i } .$ :

$$
C _ {\mathrm{i}} = C m + C a * \cos \left(\left(2 \frac {\pi}{2 4}\right) * \left(k _ {i} ^ {d a y} - p\right)\right), \forall i \in N
$$

 Process U at location i, U<sub>i</sub>:

$$
U _ {\mathrm{i}} = U m + U a * \cos \left(\left(2 \frac {\pi}{1 2}\right) * \left(k _ {i} ^ {d a y} - p - 3\right)\right), \forall i \in N
$$

The above processes allow us to compute the alertness score at a given location i (alertness<sub>i</sub>):

$$
a l e r t n e s s _ {i} = S _ {i} + C _ {i} + U _ {i}, \forall i \in N
$$

Recall from the TPMA discussion above, the process components that make up the alertness score are non-linear. Therefore, it is very likely that the minimum alertness score will not happen at a given location i, but rather during the drive between i-1 and i. We use the pseudo-code presented in Figure 3 below to calculate the minimum alertness score (minalertness<sub>i</sub>) along a given route segment. { Insert Figure 3 here. }

Our formulation of the TDSPFM is then given as follows,

Minimize:

$$
A _ {l a s t} - D _ {f i r s t}\tag{1}
$$

Subject To:

$$
A _ {i} + r _ {i} + w _ {i} = D _ {i} \forall i \in N\tag{2}
$$

$$
D _ {i} + t _ {i, i + 1} = A _ {i + 1} \quad \forall i \in N\tag{3}
$$

$$
k _ {i} ^ {d r i v e} \leq t ^ {d r i v e}, \forall i \in N\tag{4}
$$

$$
k _ {i} ^ {w o r k} \leq t ^ {e l a p s e d | R}, \forall i \in N\tag{5}
$$

$$
k _ {i} ^ {\text { break }} \leq t ^ {\text { elapsed } | B}, \forall i \in N\tag{6}
$$

$$
A _ {l a s t} + w _ {l a s t} \leq t ^ {\mathrm{horizon}}\tag{7}
$$

$$
0 \leq r _ {i} \leq t ^ {\max \_ r e s t} \forall i \in N\tag{8}
$$

$$
A _ {i} \leq L _ {i}, \quad \forall i \in N\tag{9}
$$

$$
m i n a l e r t n e s s _ {i} \geq T P M A ^ {\min}, \quad \forall i \in N\tag{10}
$$

$$
r _ {i} \geq 0, \forall i \in N\tag{11}
$$

The objective in (1) is to minimize the route duration. Constraints (2) and (3) ensure our arrival and departure times capture the time consumed at each location. Constraints (4)-(7) enforce HOS regulations. Constraint (4) is the HOS drive time constraint. Constraint (5) is the HOS working time constraint. Constraint (6) ensures that a short rest break is taken in accordance with HOS regulations. Constraint (7) ensures that the arrival time and associated work time of the last location $( A _ { l a s t }$ and $w _ { l a s t } ,$ respectively) occur within the time horizon specified for the problem. The parameter ??<sup>??????\_????????</sup> specifies the maximum rest time and constraint (8) ensures that the rest time at each location (r<sub>i</sub>) is within that limit.

Constraint (9) is the time window restriction ensuring that the arrival time of each location is prior to the time window of that location (L<sub>i</sub>) closing. For the sake of simplicity, we allowed an opening time window at each location to be 0 though an additional constraint to account for an opening time window can easily be added. Constraint (10) allows us to specify an alertness threshold $( T P M A ^ { \mathrm { m i n } } )$ and ensures that the alertness score stays above that value. It is worth noting that constraint (10) is specified as a “greater than or equal to” constraint; however a “strictly greater than” or “equal to” relationship between the alertness score and the alertness threshold could be used if desired. Should we only want to use the HOS constraints, we set $T P M A ^ { \mathrm { { m i n } } } = 0$ . Finally, constraint (11) ensures the rest time at location i (r<sub>i</sub>) is non-negative.

We populate the initial arrival time $\left( A _ { f i r s t } \right)$ to correspond with a 6 AM start for the workweek. We set a moderate initial alertness score of 10.32 based on the Karolinska Sleepiness Scale (KSS) [39,55] and the conversion from KSS to TPMA scores [36]. We also set the initial rest time and work time $( r _ { f i r s t } , w _ { f i r s t }$ respectively) to be 0 and thus we can calculate the departure time $( D _ { f i r s t } )$ . For the purposes of the results presented below, we use a work time at all other locations (w<sub>i</sub>) of 30 minutes. Similar to the model in

Goel [24], the TDSPFM only allows the driver to rest after arrival at a location and completing any work required at the location. Should we want to consider rest areas or other stops designed for non-work related activities, dummy locations along the route can be added to the model with a work time of zero.

Calculating minalterness<sub>i</sub> in constraint (10) (and as summarized in Figure 3) makes the TDSPFM problem a difficult nonlinear optimization model that requires a heuristic solution technique. We therefore implemented the model in Microsoft Excel 2013 and solved it using the built-in Solver’s Evolutionary solution method [51]. The TDSPFM is a planning problem; thus, we are interested in finding good solutions in a reasonable amount of time. After some experimentation, we settled on a maximum run time of 600 seconds, finding that Solver rarely found better solutions to these problems even with considerably longer run times. While solutions obtained with heuristics might not be globally optimal, Solver’s Evolutionary algorithm typically finds good solutions to hard problems<sup>1</sup>. Our test problems were solved on a computer with 128 GB of RAM, 2 2.60 GHz Intel Xeon processors, running the 64-bit Windows 7 operating system. Because the travel times and sequence of locations to be visited are given, we coded a repair function that would force a rest of at least ??<sup>????????</sup> in length if continuing would violate one of the HOS restrictions. As is common in genetic algorithm formulations, we used penalty functions to capture violations of time windows, HOS regulations, and alertness constraints.

## 3.1 Model Limitations

The TDSPFM as presented here is limited in a number of ways. First, we model the length and quality of sleep as a deterministic value. The model requires that we know with certainty the amount of recoverable sleep time that the driver will receive at each long rest break. In real-world scenarios this is not the case as unexpected events happen related to both environmental (noises outside the cab) and behavioral (the driver decides to stay awake longer) factors.

The second category of limitations is biological differences between individual drivers. These could be related to sleep disorders, such as sleep apnea, that might cause the quality of sleep to vary between individuals. The different components of the TPMA can also be different between individuals. For instance, we used parameter values to model the circadian rhythm (process C) as if it is the same for all drivers when in fact individuals can have different rhythms.

The third category of limitations is that the TDSPFM does not account for stimulants or other drugs that impact a driver’s alertness levels. In practice, drivers often utilize these substances for pleasure, out of habit, or with the intention of trying to stay awake longer. Caffeine is likely the most common stimulant in use. Modeling its effects on alertness is an area of active research [52].

## 4. Results

We created 30 randomly generated benchmark problems in order to compare the TDSPFM’s performance over a range of minimum alertness levels. Following the methodology of Goel [24], we focus solely on minimizing the route duration while abiding by the constraints including time windows and HOS restrictions. We first solved the problem with no alertness minimum $( T P M A ^ { \mathrm { m i n } } = 0 )$ , which results in minimizing the route duration while abiding by the HOS restrictions described above. These results are identified as “Baseline HOS (0)” in Table 2. This leads to a greedy solution that could be considered overly aggressive when compared to realistic truck driving schedules, but provides a baseline for comparison.

Next, we compared the baseline solution with those obtained by setting minimum alertness levels $( T P M A ^ { \mathrm { m i n } } )$ at 7.07, 8.15, and 9.24. These minimum alertness levels were chosen in accordance with the Karolinska Sleepiness Scale (KSS) levels discussed in Ingre et al. [36], Shahid et al. [55], and Kaida et al. [39]. These alertness levels are closer to being considered “sleepy” than being “alert”. We assume that it would be unrealistic to have a minimum alertness level set so high that the driver can never be tired at any time. Therefore, we study levels that could be described as:

 tired (as opposed to sleepy), alertness level 7.07

semi-tired, alertness level 8.15

## not tired, alertness level 9.24

Because these alertness levels represent constraints that tighten the solution space, we anticipate the optimal objective value of the total route duration to increase as the minimum alertness level is increased.

Table 2 shows the averaged results of route duration, minimum alertness, and average alertness for all 30 benchmark problems as well as the worst-case minimum alertness observed. In addition to summarizing the results, we conducted ANOVA testing to determine if there were differences between our problem configurations. The ANOVA results showed there were statistically significant differences. Thus, we utilized Tukey-Kramer HSD test (α = 0.05) to find where the differences were, comparing the results of different alertness level constraints to the baseline (HOS only constraints).

{ Insert Table 2 here. }

With only the HOS constraints, the average minimum alertness stays above the TPMA sleepiness threshold of 7, though the worst-case scenario was at the 7.0 level. Therefore, it is not surprising to see non-statistically significant increases in either route duration or alertness when enforcing an alertness threshold of tired. However, at the semi-tired threshold, we see a 5.13% increase in the minimum alertness score with a mere 1.18% increase in route duration. The difference in minimum alertness was statistically significant (p < 0.0001); however, the increase in route duration was not statistically significant at the semi-tired threshold. Finally, when the threshold is set to prevent the driver from getting below the “not tired” stage, we observed statistically significant increases in both route duration and minimum alertness (p < 0.0001).

In this study, the average driver alertness ranged between 9.9 and 10.6, which indicates that fatigue is not a major safety concern on average. The results also show a small spread that indicates that there are few points along the route where driver sleepiness reaches critical thresholds. These results illustrate that the existing HOS regulations appear to be reasonable with respect to allowing drivers to abide by existing regulations and remain above the general sleepiness level. Recall that an alertness level of 7 is considered to be the "sleepy" cutoff in the literature; however, that threshold cutoff value does not take into account what activity the human subject may be performing at the time. Thus, one could argue that the average sleepiness level for someone driving an 80,000-pound vehicle at interstate speeds should be greater than a minimum threshold value of 7.

## 5. HOS Examination

In the results presented above, we set the driver’s alertness level at the start of their workweek to an acceptable level of 10.32. In all of the HOS regulations that we examined, the regulatory bodies essentially do the same thing; specifically, the assumption is that drivers begin their workweek in a rested and alert state. Based on the work of Crum and Morrow [16], who concluded that “starting the workweek tired was the single most important factor influencing truck driver fatigue”, this is a generous and potentially erroneous assumption.

We reviewed several countries and the European Union's HOS regulations and found none to have provisions related to how rested a driver must be when they begin their workweek. Thus, it is possible for a driver to be fatigued before they even begin their workweek. Regardless of how fatigued a driver might be at the beginning of the week, he/she can report to work and immediately begin driving a fully loaded tractor-trailer for 8 straight hours before their first break. The only HOS stipulation is that the driver not be driving, on-duty, or otherwise working for their employer during the 34 hour period prior to their workweek starting. A publicized example of a driver beginning his workweek in a less than rested condition occurred on June 7, 2014 in the fatal crash involving comedians Tracy Morgan, James McNair, and three other passengers [29]. We are therefore motivated to look at how different levels of fatigue at the beginning of the workweek might affect the alertness of the driver for the remainder of the route.

## 5.1 Example Schedule

Using our TDSPFM model in combination with an actual truck driver's schedule taken from the "Driver's Daily Log Book," we can empirically observe the values of key performance indicators pertaining to fatigue. We can also observe how changing the starting alertness level at the beginning of the week affects the key performance measures throughout the workweek. The driver's typical workday was from 1 AM until noon. For the weekly route we modeled, the duration of the route was 125 hours and involved 30 stops (including the beginning and ending locations for the entire trip duration) with varying work durations per stop. We assume that the driver was reasonably well-rested and had been awake for 2 hours at the start of his/her work shift. The initial TPMA alertness level was set at 12.5, which corresponds to a KSS score of 5 indicating that the driver was neither sleepy nor alert at the beginning of the workweek. In this case, our results show that the minimum alertness for the driver's schedule was 7.11 with an average alertness of 8.48. Recall, the generally accepted alertness threshold in the TPMA literature is 7, so the minimum alertness score is slightly above the published minimum alertness threshold and the average alertness score for the entire trip duration is very close to that threshold.

Next, we adjusted the starting alertness level to investigate what effect that had on the key performance indicators. The results are displayed in Table 3. Graphically, the alertness levels are represented in Figure 4. As the graph shows, the low initial starting alertness reduces the average alertness over the example weekly schedule. Additionally, the minimum alertness is substantially reduced when the initial alertness level is low.

## { Insert Table 3 here. }

## { Insert Figure 4 here. }

To gain an understanding of the alertness level over the course of the week, in Figure 5 we show the different components of the TPMA as a function of the different stops in the example week’s route using a starting alertness of 12.5. Rests occur at points where the S curve slopes upward. However, the resulting recovery can be dampened by other components in the TPMA, particularly the circadian effect (process C). One can also observe how on several occasions the minimum alertness level gets close to the TPMA threshold of 7.

{ Insert Figure 5 here. }

The alertness measures captured from the sample log entries show that the less alert the driver is when starting the week, the less alert the driver will be (both in the overall minimum and on average) throughout the week. The results illustrate how the model can be used in practice and is based on actual driver behavior. However, the data only capture the behavior of one driver for one workweek. We would have to examine a larger sample of driver logbooks before determining if our results are representative of general trends within the trucking industry.

## 5.2 Computational Testing and Results

To understand the magnitude of the potential effect of the starting alertness level, we created 30 benchmark problems in the same manner as described in section 4 and varied the starting alertness level as follows:

 High, alertness level 12.5

 Medium, alertness level 10.32

 Low, alertness level 8.15

We then used the same minimum alertness thresholds (????????<sup>min</sup>) utilized in section 3:

 not tired, $T P M A ^ { \mathrm { { m i n } } } = 9 . 2 4 $

 semi-tired, $T P M A ^ { \mathrm { m i n } } = 8 . 1 5$

 tired, $T P M A ^ { \mathrm { { m i n } } } = 7 . 0 7$

 hours of service only, $T P M A ^ { \mathrm { { m i n } } } = 0$

Combining the above configurations results in 12 combinations of starting alertness levels and minimum alertness thresholds. To study these combinations, we configured and solved the 30 benchmark problems for each combination. This leads us with 10 sets of 30 problems each from which to derive our results. (Note there would be no feasible solutions available with starting TMPA levels of 8.15 and required $T P M A ^ { \mathrm { { m i n } } }$ of either 7.07 or 8.15.)

The box and whiskers plots in Figures 6, 7, and 8 show the results of these sample problems. We group the problems along the x-axis by starting alertness level. Figure 6 shows how each problem set performed with respect to the route durations. These results are consistent with the results presented in section 4. At the “not tired” level $( T P M A ^ { \mathrm { { m i n } } } = 9 . 2 4 ) $ we see a slight increase in duration and an increase in the variability of the result. Overall, the starting alertness level has little effect on the route duration.

# ACCEPTED MANUSCRIPT

In Figure 7, we present the results of the minimum alertness for our problem sets. The minimum alertness observations themselves are in line with the setting of $T P M A ^ { \mathrm { { m i n } } }$ in that the lower whisker of the plot is roughly at the $T P M A ^ { \mathrm { { m i n } } }$ value. The most interesting result here is the observation that as ????????<sup>min</sup> increases, the variability of the result decreases. In general though, the results show the same behavior presented in Table 2. Regarding the minimum alertness of the trip, the initial starting alertness level has little effect if we throw out the obvious infeasible solutions.

{ Insert Figure 7 here. }

The most interesting observation derived from our results is presented in Figure 8, where we compare the averaged alertness level of our problem sets. Here we clearly see that the starting alertness level has an impact on the week’s average alertness level. The impact is most pronounced when the starting alertness is low. These results support the conclusion of Crum and Morrow [16] concerning the importance of a driver being well-rested at the beginning of the workweek.

{ Insert Figure 8 here. }

Much of the focus in our results presented thus far and in the existing driver fatigue research has been on the minimum alertness level. In other words, trying to keep the driver from becoming too fatigued at any given point along the route in order to avoid a crash or other disruptive event at that given point in time. This is a valid idea to study and has merit as a possible crash reduction or fatigue management strategy. However, while the minimum alertness covers a single point in time along the route, the average alertness looks more inclusively at the time driving during the week as a whole. Presumably, there will be many more situations where the driver is at or near the average alertness level where they will need to make important decisions that could be impaired by fatigue. Therefore, as a fatigue management strategy, the average alertness may be equally or perhaps more important than the minimum alertness level.

## 5.2.1 Highway To The Danger Zone

Average alertness becomes even more important when we consider how fatigue might impact driver decision making over the course of an entire workweek as opposed to just examining the impact of fatigue in situations where a driver falls asleep at the wheel or loses control of the vehicle. When considering the impact of fatigue on a driver's decision-making, such as making a maneuver to avoid a potential crash or the need for quick reactions, the average alertness level may be a more important performance measure than the minimum alertness level. We conjecture that the more alert the driver is on average, the more likely it is that they will have the capacity to make good decisions and make them quickly. To investigate this further, we set the initial alertness level to a value representing a situation where external factors such as poor sleep or a change in the schedule increases the chance that the driver's average alertness falls below the $T P M A ^ { \mathrm { { m i n } } }$ . We refer to this level as the "danger zone". In this case, we are particularly interested in the time periods when the driver's alertness level falls into this danger zone. To provide a meaningful comparison of results across different model configurations, we use a danger zone value of 9.7 (a 5% increase in the "not tired" parameter value). We acknowledge that an appropriate value for this threshold is an open topic of research that we hope to investigate further in the future.

The danger zone is represented by the areas in the schedule where the driver's TPMA alertness level is between 9.7 and the $T P M A ^ { \mathrm { { m i n } } }$ parameter value. From a fatigue management perspective, this V area is an important component of driver scheduling that is motivated by real-world scheduling uncertainties. For instance, the TDSPFM assumes that a driver spends most of their long rest break getting high quality sleep. On points along the route where the driver's predicted alertness level is close to the $T P M A ^ { \mathrm { { m i n } } }$ , it is critical that driver behaviors in the prior rest periods are consistent in the assumed alertness recovery. However, if the recovery assumption is changed, and the driver gets less sleep than assumed, the alertness recovery is reduced and the resulting alertness on later segments of the route may end up being below the $T P M A ^ { \mathrm { { m i n } } }$

{ Insert Figure 10 here. }

# ACCEPTED MANUSCRIPT

A graphical representation of our proposed danger zone is shown in Figure 9. We use an example problem created earlier to model the minimum TPMA alertness score at each stop on the optimal schedule. Figure 9 allows us to compare alertness scores between different model parameters (no ????????<sup>min</sup> versus a starting alertness of Low compared to $T P M A ^ { \mathrm { m i n } } = \mathrm { } ^ { \prime \prime } \mathrm { n o t t i r e d } ^ { \prime \prime }$ versus a starting alertness of High). This allows us to observe the portion of the schedule in the danger zone (in the shaded area).

{ Insert Figure 9 here. }

For a more rigorous analysis, Figure 10 below shows the modeled percentage of time driving while the alertness level is in the danger zone across all of our example problems. Intuitively, when $T P M A ^ { \mathrm { { m i n } } }$ is set to “not tired” (9.24), the portion of the danger zone that is in the feasible solution space is smaller and thus percentage of time is lower. However, the more important observation is how much of an effect starting alertness has on the percentage of time in the danger zone. As shown in Figure 10, starting at the lower level of alertness results in significantly more time spent driving in the danger zone.

In summary, we conclude that the initial starting alertness level significantly affects the average alertness and the percentage of time in the danger zone. At the lowest level of starting alertness that we looked at, this was especially pronounced as the majority of driving time occurred with a fatigue level in the danger zone. There currently exist no regulatory provisions pertaining to the initial alertness level. However, from the perspective of public safety policy, initial alertness is an issue where greater regulatory oversight is possible and, as our results demonstrate, can have a significant impact. Thus, our research points (at least) to the need for investigation into the practicality of such provisions.

## 5.2.2 Managerial and Policy Implications

This work demonstrates the ability to produce schedules that account for alertness as well as the typical scheduling constraints that a scheduling manager would need to take into account. Additionally, our work shows that it is possible to produce schedules with significantly improved alertness levels with small to moderate increases in schedule duration. From a policy standpoint, our work shows that initial

# ACCEPTED MANUSCRIPT

alertness levels have a significant effect on the overall alertness levels of a driver throughout their workweek. This should motivate policy makers to further study ways to consider the initial alertness level for future regulatory purposes. In addition, this serves as a solid starting point for companies to take proactive measures to prevent drivers from beginning work in a compromised alertness condition and to monitor their alertness throughout the week.

This should further motivate managers to create and implement a Fatigue Risk Management System (FRMS) in order to systematically introduce and implement policies aimed at reducing fatigue related risks and monitoring their effectiveness. An FRMS is defined in [20] as, “a data-driven and scientifically based process that allows for continuous monitoring and management of safety risks associated with fatigue-related error.” A key component of a FRMS is a fatigue aware decision support system for scheduling drivers. By building the DSS on top of the TDSPFM, a manager would be able to produce schedules with an appropriate predicted fatigue level and then monitor the effectiveness of the produced schedules.

## 6. Conclusions and Future Work

This paper introduced the TDSPFM, which is the first model to include the necessary variables and constraints to enforce a minimum alertness level within the vehicle scheduling domain. Our results show how this model facilitates the production of schedules that meet existing HOS constraints while also meeting a minimum alertness level. The TDSPFM model also allows for an estimate of the magnitude of the increased route duration required in order to increase driver alertness level. Thus, this work serves as a starting point for developing more cost-effective ways to develop safer schedules for commercial truck drivers and safer highways for the traveling public.

In terms of future work, we have identified three primary areas for potential expansion of the TDSPFM model: sleep variability, sleep prediction, and driver specific alertness modifications. We can look at sleep variability from both the standpoint of individual variations and specific rest period variations. In this paper, we looked at the typical/average sleep functions. However, the TPMA can easily support user specific functions; for instance, certain people may recover during sleep at different rates or be more affected by being awake and needing to work at 3 AM. The proliferation of biometric monitoring devices like the Fitbit will likely facilitate this sort of research in the future.

An advantage of using TPMA scores in the TDSPF model is that they can be transformed into a prediction of the subjective Karolinska Sleepiness Scale (KSS), which has been shown to be a valid means for measuring sleepiness [5,39,55]. While a KSS measure is easy to obtain, it does introduce the possibility of drivers lying or being inconsistent in their responses. Objective measures of fatigue, such as electroencephalographic (EEG) testing or psychomotor vigilance task (PVT) are more costly to obtain but eliminate the subjective weaknesses of the KSS [39]. Thus, future research could validate the schedules proposed by our model as well as the alertness parameter values we use.

As mentioned in the literature review, detecting fatigue in near real-time is an active area of research and product development. We do not dispute the importance of that type of solution in ensuring the safety of our roadways. However, incorporating fatigue directly into driver scheduling can reduce the reliance on real-time fatigue detection. An effective schedule development strategy to ensure both cost effective scheduling and safety is one that takes fatigue and alertness into account during the planning stage. A reactive approach of forcing a driver to stop and take an unplanned rest due to a fatigue detection by a real-time system will be much more costly than proactively avoiding fatigue by developing a safer schedule.

In this work, we used model parameters representative of the United States HOS regulations. In future work, we could investigate ways to generalize our model to support HOS regulations of other countries. This would then allow us to not only improve our model by making it more flexible, but also allow us to compare the resulting alertness levels across different HOS regulations.

Finally, our model assumes non-stochastic sleep times during rest periods. However, the amount of time a person actually sleeps on a given night is dependent upon many factors (e.g., noise levels, comfort, temperature, etc.). Future research could also incorporate a stochastic element into the model to represent how these environmental factors affect sleep duration.

## 7. References

[1] T. Åkerstedt, J. Axelsson, G. Kecklund, Individual validation of model predictions of sleepiness and sleep hours, Somnologie. 11 (2007) 169–174. https://doi.org/10.1007/s11818-007-0315-7.

[2] T. Åkerstedt, J. Connor, A. Gray, G. Kecklund, Predicting road crashes from a mathematical model of alertness regulation—The Sleep/Wake Predictor, Accident Analysis & Prevention. 40 (2008) 1480–1485. https://doi.org/10.1016/j.aap.2008.03.016.

[3] T. Åkerstedt, S. Folkard, Validation of the S and C components of the three-process model of alertness regulation, Sleep. 18 (1995) 1–6.

[4] T. Åkerstedt, S. Folkard, C. Portin, Predictions from the Three-Process Model of Alertness, Aviation, Space, and Environmental Medicine. 75 (2004) A75–A83.

[5] T. Åkerstedt, M. Gillberg, Subjective and objective sleepiness in the active individual, The International Journal of Neuroscience. 52 (1990) 29–37.

[6] C. Archetti, M. Savelsbergh, The Trip Scheduling Problem, Transportation Science. 43 (2009) 417– 431. https://doi.org/10.1287/trsc.1090.0278.

[7] M. Blanco, R.J. Hanowski, R.L. Olson, J.F. Morgan, S.A. Soccolich, S.-C. Wu, F. Guo, The Impact of Driving, Non-Driving Work, and Rest Breaks on Driving Performance in Commercial Motor Vehicle Operations (DOT-HS-810594), (2011). http://ntl.bts.gov/lib/51000/51300/51387/Work-Hours-HOS.pdf Accessed 15.01.15.

[8] A.A. Borbély, A Two Process Model of Sleep Regulation, Human Neurobiology. 1 (1982) 195–204.

[9] A.A. Borbély, S. Daan, A. Wirz-Justice, T. Deboer, The two-process model of sleep regulation: a reappraisal, Journal of Sleep Research. 25 (2016) 131–143. https://doi.org/10.1111/jsr.12371.

[10] D.S. Bowman, W.A. Schaudt, R.J. Hanowski, Advances in Drowsy Driver Assistance Systems Through Data Fusion, in: A. Eskandarian (Ed.), Handbook of Intelligent Vehicles, Springer London, 2012: pp. 895–912.

[11] T. Brown, R. Johnson, G. Milavetz, Identifying Periods of Drowsy Driving Using EEG, Annals of Advances in Automotive Medicine. 57 (2013) 99–108.

[12] F. Cappuccio, M.A. Miller, S.W. Lockley, Sleep, Health, and Society: From Aetiology to Public Health, Oxford University Press, 2010.

[13] T. Chalder, G. Berelowitz, T. Pawlikowska, L. Watts, S. Wessely, D. Wright, E.P. Wallace, Development of a fatigue scale, Journal of Psychosomatic Research. 37 (1993) 147–153. https://doi.org/10.1016/0022-3999(93)90081-P.

## ACCEPTED MANUSCRIPT

[14] T.-H. Chang, Y.-R. Chen, Driver fatigue surveillance via eye detection, in: 2014 IEEE 17th International Conference on Intelligent Transportation Systems (ITSC), 2014: pp. 366–371. https://doi.org/10.1109/ITSC.2014.6957718.

[15] C. Chen, Y. Xie, The impacts of multiple rest-break periods on commercial truck driver’s crash risk, Journal of Safety Research. 48 (2014) 87–93. https://doi.org/10.1016/j.jsr.2013.12.003.

[16] M.R. Crum, P.C. Morrow, The Influence of Carrier Scheduling Practices on Truck Driver Fatigue, Transportation Journal. 42 (2002) 20–41.

[17] D. Dawson, Y. Ian Noy, M. Härmä, T. Åkerstedt, G. Belenky, Modelling fatigue and the use of fatigue models in work settings, Accident Analysis & Prevention. 43 (2011) 549–564. https://doi.org/10.1016/j.aap.2009.12.030.

[18] D. Dawson, K. McCulloch, Managing fatigue: It’s about sleep, Sleep Medicine Reviews. 9 (2005) 365–380. https://doi.org/10.1016/j.smrv.2005.03.002.

[19] M. Desrochers, C.V. Jones, J.K. Lenstra, M.W.P. Savelsbergh, L. Stougie, Towards a model and algorithm management system for vehicle routing and scheduling problems, Decision Support Systems. 25 (1999) 109–133. https://doi.org/10.1016/S0167-9236(98)00090-6.

[20] Federal Aviation Administration, Review and Acceptance of Fatigue Risk Management Plans (FRMP), 2016. http://fsims.faa.gov/PICDetail.aspx?docId=8900.1,Vol.3,Ch58,Sec1 Accessed 17.06.06.

[21] Federal Motor Carrier Safety Administration, Summary of Hours of Service Regulations, (2013). http://www.fmcsa.dot.gov/regulations/hours-service/summary-hours-service-regulations Accessed 15.04.22.

[22] C. Fourie, A. Holmes, S. Bourgeois-Bougrine, C. Hilditch, P. Jackson, Fatigue Risk Management Systems: A review of the literature - Road Safety Research Report 110, Department of Transport, London, 2010.

[23] P. Gander, L. Hartley, D. Powell, P. Cabon, E. Hitchcock, A. Mills, S. Popkin, Fatigue risk management: Organizational factors at the regulatory and industry/company level, Accident Analysis & Prevention. 43 (2011) 573–590. https://doi.org/10.1016/j.aap.2009.11.007.

[24] A. Goel, The minimum duration truck driver scheduling problem, EURO Journal on Transportation and Logistics. 1 (2012) 285–306. https://doi.org/10.1007/s13676-012-0014-9.

[25] A. Goel, The Canadian minimum duration truck driver scheduling problem, Computers & Operations Research. 39 (2012) 2359–2367. https://doi.org/10.1016/j.cor.2011.12.016.

[26] A. Goel, Hours of service regulations in the United States and the 2013 rule change, Transport Policy. 33 (2014) 48–55. https://doi.org/10.1016/j.tranpol.2014.02.005.

## ACCEPTED MANUSCRIPT

[27] A. Goel, T. Vidal, Hours of Service Regulations in Road Freight Transport: An Optimization-Based International Assessment, Transportation Science. 48 (2014) 391–412. https://doi.org/10.1287/trsc.2013.0477.

[28] A. Gundel, K. Marsalek, C. ten Thoren, A critical review of existing mathematical models for alertness, Somnologie. 11 (2007) 148–156. https://doi.org/10.1007/s11818-007-0312-x.

[29] J. Hanna, R. Marsh, NTSB: Trucker’s fatigue likely led to Tracy Morgan crash - CNN.com, CNN. (2015). http://www.cnn.com/2015/08/11/us/ntsb-tracy-morgan-crash/index.html Accessed 15.08.11.

[30] R.J. Hanowski, J.S. Hickman, R.L. Olson, J. Bocanegra, Evaluating the 2003 revised hours-ofservice regulations for truck drivers: The impact of time-on-task on critical incident risk, Accident Analysis & Prevention. 41 (2009) 268–275. https://doi.org/10.1016/j.aap.2008.11.007.

[31] K. Heaton, Truck Driver Hours of Service Regulations: The Collision of Policy and Public Health, Policy, Politics, & Nursing Practice. 6 (2005) 277–284. https://doi.org/10.1177/1527154405282841.

[32] R. Hockey, The Psychology of Fatigue: Work, Effort and Control, Cambridge University Press, New York, 2013.

[33] X. Hu, L. Sun, L. Liu, A PAM approach to handling disruptions in real-time vehicle routing problems, Decision Support Systems. 54 (2013) 1380–1393.

[34] S.R. Hursh, T.J. Balkin, J.C. Miller, D.R. Eddy, The Fatigue Avoidance Scheduling Tool: Modeling to Minimize the Effects of Fatigue on Cognitive Performance, SAE Technical Paper 2004-01-2151. (2004). https://doi.org/10.4271/2004-01-2151.

[35] M. Ingre, T. Åkerstedt, B. Peters, A. Anund, G. Kecklund, A. Pickles, Subjective sleepiness and accident risk avoiding the ecological fallacy, Journal of Sleep Research. 15 (2006) 142–148. https://doi.org/10.1111/j.1365-2869.2006.00517.x.

[36] M. Ingre, W. Van Leeuwen, T. Klemets, C. Ullvetter, S. Hough, G. Kecklund, D. Karlsson, T. Åkerstedt, Validating and Extending the Three Process Model of Alertness in Airline Operations, PLoS ONE. 9 (2014) e108679. https://doi.org/10.1371/journal.pone.0108679.

[37] A. Jensen, S. Dahl, Truck drivers hours-of-service regulations and occupational health, Work: A Journal of Prevention, Assessment and Rehabilitation. 33 (2009) 363–368. https://doi.org/10.3233/WOR-2009-0884.

[38] S. Jin, S.-Y. Park, J.-J. Lee, Driver fatigue detection using a genetic algorithm, Artificial Life and Robotics. 11 (2007) 87–90. https://doi.org/10.1007/s10015-006-0406-8.

[39] K. Kaida, M. Takahashi, T. Åkerstedt, A. Nakata, Y. Otsuka, T. Haratani, K. Fukasawa, Validation of the Karolinska sleepiness scale against performance and EEG variables, Clinical Neurophysiology. 117 (2006) 1574–1581. https://doi.org/10.1016/j.clinph.2006.03.011.

[40] P.B. Keenan, Spatial decision support systems for vehicle routing, Decision Support Systems. 22 (1998) 65–71. https://doi.org/10.1016/S0167-9236(97)00054-7.

[41] E. Kemp, S.W. Kopp, E. Kemp, Six days on the road: Will I make it home safely tonight? Examining attitudes toward commercial transportation regulation and safety, The International Journal of Logistics Management. 24 (2013) 210–229.

[42] S.E. Lerman, E. Eskin, D.J. Flower, E.C. George, B. Gerson, N. Hartenbaum, S.R. Hursh, M. Moore-Ede, Fatigue Risk Management in the Workplace:, Journal of Occupational and Environmental Medicine. 54 (2012) 231–258. https://doi.org/10.1097/JOM.0b013e318247a3b0.

[43] C.C. Liu, S.G. Hosking, M.G. Lenné, Predicting driver drowsiness using vehicle measures: recent insights and future challenges, Journal of Safety Research. 40 (2009) 239–245. https://doi.org/10.1016/j.jsr.2009.04.005.

[44] X. Luo, R. Hu, T. Fan, The driver fatigue monitoring system based on face recognition technology, in: 2013 Fourth International Conference on Intelligent Control and Information Processing (ICICIP), 2013: pp. 384–388. https://doi.org/10.1109/ICICIP.2013.6568102.

[45] M.M. Mallis, S. Mejdal, T.T. Nguyen, D.F. Dinges, Summary of the Key Features of Seven Biomathematical Models of Human Fatigue and Performance, Aviation, Space, and Environmental Medicine. 75 (2004) A4–A14.

[46] M. Moore-Ede, A. Heitmann, R. Guttkuhn, D. Croke, Circadian Alertness Simulator for Fatigue Risk Assessment in Transportation: Application to Reduce Frequency and Severity of Truck Accidents, Aviation Space and Environmental Medicine. (2004).

[47] P.C. Morrow, M.R. Crum, Antecedents of fatigue, close calls, and crashes among commercial motor-vehicle drivers, Journal of Safety Research. 35 (2004) 59–69. https://doi.org/10.1016/j.jsr.2003.07.004.

[48] National Academies of Sciences, Engineering, and Medicine, Commercial Motor Vehicle Driver Fatigue, Long-Term Health, and Highway Safety: Research Needs, National Academies Press, Washington DC, USA. (2016). https://doi.org/10.17226/21921.

[49] North American Fatigue Management Program, Module 9: Driver Scheduling and Tools, (2012). http://www.nafmp.org/en/downloads.html Accessed 15.03.16.

[50] R.O. Phillips, An assessment of studies of human fatigue in land and sea transport, Institute of Transport Economics (TØI), Oslo, Norway, 2014. https://www.toi.no/getfile.php/1339685/Publikasjoner/TØI%20rapporter/2014/1354-2014/1354- 2014-sum.pdf Accessed 17.08.23.

[51] C.T. Ragsdale, Spreadsheet Modeling and Decision Analysis (8th ed.), Cengage Learning, Boston, 2018.

## ACCEPTED MANUSCRIPT

[52] J. Reifman, K. Kumar, N.J. Wesensten, N.A. Tountas, T.J. Balkin, S. Ramakrishnan, 2B-Alert Web: An Open-Access Tool for Predicting the Effects of Sleep/Wake Schedules and Caffeine Consumption on Neurobehavioral Performance, Sleep. 39 (2016) 2157–2159. https://doi.org/10.5665/sleep.6318.

[53] B. Ryder, B. Gahr, P. Egolf, A. Dahlinger, F. Wortmann, Preventing traffic accidents with invehicle decision support systems - The impact of accident hotspot warnings on driver behaviour, Decision Support Systems. 99 (2017) 64–74. https://doi.org/10.1016/j.dss.2017.05.004.

[54] L. Santos, J. Coutinho-Rodrigues, C.H. Antunes, A web spatial decision support system for vehicle https://doi.org/10.1016/j.dss.2010.11.008.

[55] A. Shahid, K. Wilkinson, S. Marcu, C.M. Shapiro, Karolinska Sleepiness Scale (KSS), in: STOP, THAT and One Hundred Other Sleep Scales, Springer, New York, 2011: pp. 209–210.

[56] Y. Suzuki, A decision support system of vehicle routing and refueling for motor carriers with timesensitive demands, Decision Support Systems. 54 (2012) 758–767. https://doi.org/10.1016/j.dss.2012.09.004.

[57] H.P.A. Van Dongen, Comparison of Mathematical Model Predictions to Experimental Data of Fatigue and Performance, Aviation, Space, and Environmental Medicine. 75 (2004) A15–A36.

[58] S. Véronneau, Y. Cimon, Maintaining robust decision capabilities: An integrative human–systems approach, Decision Support Systems. 43 (2007) 127–140. https://doi.org/10.1016/j.dss.2006.08.003.

[59] H. Xu, Z.-L. Chen, S. Rajagopal, S. Arunapuram, Solving a Practical Pickup and Delivery Problem, Transportation Science. 37 (2003) 347–364. https://doi.org/10.1287/trsc.37.3.347.16044.

[60] M. Zhang, G. Longhui, Z. Wang, X. Xu, B. Yao, L. Zhou, Hybrid Model for Early Onset Prediction of Driver Fatigue with Observable Cues, Mathematical Problems in Engineering. 2014 (2014) e385716. https://doi.org/10.1155/2014/385716.

Figure 1: Components of the TPMA

Figure 2: A Truck Driver Schedule

Figure 3: Pseudo-code of Minimum Alertness Calculation

Figure 4: TPMA Alertness Levels

Figure 5: TPMA Alertness in Example Schedule

Figure 6: Box and Whiskers Plot – Duration

Figure 7: Box and Whiskers Plot – Minimum Alertness Level

Figure 8: Box and Whiskers Plot – Average Alertness Level

Figure 9: Minimum Alertness Comparison

Figure 10: Box and Whiskers Plot – Percentage of Time Driving in Danger Zone

<table><tr><td>Parameter Name</td><td>Value (hours)</td><td>Description</td></tr><tr><td> $t^{rest}$ </td><td>10</td><td>Minimum rest time to be considered a long rest</td></tr><tr><td> $t^{break}$ </td><td>0.5</td><td>Minimum Break</td></tr><tr><td> $t^{horizon}$ </td><td>168</td><td>Planning Horizon (1 week)</td></tr><tr><td> $t^{drive}$ </td><td>11</td><td>Maximum drive time since last long rest</td></tr><tr><td> $t^{elapsed/R}$ </td><td>14</td><td>Maximum time since last long rest</td></tr><tr><td> $t^{elapsed/B}$ </td><td>8</td><td>Maximum time since last break</td></tr><tr><td> $t^{maxsleep}$ </td><td>10</td><td>Maximum amount of sleep allowed</td></tr><tr><td> $t^{awakedelay}$ </td><td>0.5</td><td>The delay after waking before driving can begin</td></tr><tr><td> $t^{sleepdelay}$ </td><td>1</td><td>The delay after rest begins before falling asleep</td></tr><tr><td> $t^{max\_rest}$ </td><td>16</td><td>Maximum rest period allowed</td></tr><tr><td> $la$ </td><td>2.4</td><td>Lower asymptote of the internal alertness scale</td></tr><tr><td> $d$ </td><td>-0.0353</td><td>Decay in alertness</td></tr><tr><td> $g$ </td><td>-0.38135645</td><td>Recovery multiplier</td></tr><tr><td> $ha$ </td><td>14.3</td><td>Higher asymptote of the internal alertness scale</td></tr><tr><td> $bl$ </td><td>12.5</td><td>Break level of recovery function S&#x27;</td></tr><tr><td> $Cm$ </td><td>0</td><td>Mesor of process C</td></tr><tr><td> $Ca$ </td><td>2.5</td><td>Amplitude of process C</td></tr><tr><td> $p$ </td><td>16.8</td><td>Default circadian phase</td></tr><tr><td> $Um$ </td><td>0.5</td><td>Mesor of process U</td></tr><tr><td> $Ua$ </td><td>0.5</td><td>Amplitude of process U</td></tr></table>

<table><tr><td rowspan="2">Problem(alertness level constraint)</td><td colspan="3">-Average</td><td rowspan="2">Duration % Increase Over Baseline</td><td rowspan="2">Minimum Alertness % Increase Over Baseline</td><td rowspan="2">Worst Case Minimum Alertness</td></tr><tr><td>Duration (hours)</td><td>Minimum Alertness</td><td>Average Alertness</td></tr><tr><td>Baseline HOS (0)</td><td>99.20</td><td>7.9</td><td>9.9</td><td>-</td><td>-</td><td>7.0</td></tr><tr><td>HOS (tired)</td><td>99.22</td><td>7.9</td><td>9.9</td><td>0.02%</td><td>0.05%</td><td>7.1</td></tr><tr><td>HOS (semi-tired)</td><td>100.37</td><td> $8.3^a$ </td><td>10.0</td><td>1.18%</td><td>5.13%</td><td>8.2</td></tr><tr><td>HOS (not tired)</td><td> $104.65^a$ </td><td> $9.3^a$ </td><td> $10.6^a$ </td><td>5.49%</td><td>17.94%</td><td>9.2</td></tr></table>

Table 2: Benchmark Results  
a: Indicates statistically significant differences from the Baseline HOS (0) at the 0.05 level.

<table><tr><td>Initial Alertness</td><td>Minimum Alertness</td><td>Average Alertness</td></tr><tr><td>High - 12.5</td><td>7.11</td><td>8.48</td></tr><tr><td>Medium - 10.32</td><td>7.01</td><td>7.96</td></tr><tr><td>Low - 8.15</td><td>5.89</td><td>7.37</td></tr></table>

Table 3: Example Schedule Alertness Levels

# Biographical Sketch

Zachary E. Bowden is a Senior Research Associate at the Virginia Tech Transportation Institute. Over the past decade, he has architected and supported research computing solutions at both the Virginia Bioinformatics Institute and Virginia Tech Transportation Institute. He received his Ph.D. in Business Information Technology from Virginia Tech and also holds M.B.A, Masters of Information Technology, and B.S. degrees from Virginia Tech. He also teaches as an adjunct professor for Radford University and Virginia Tech.

Cliff T. Ragsdale is the Bank of America Professor of Business Information Technology and Academic Director of the Center for Business Intelligence and Analytics in the Pamplin College of Business at Virginia Tech. His primary research interest centers on the use of analytical modeling in support of decision making. He has published over 50 articles in various scholarly journals and is also author the book Spreadsheet Modeling & Decision Analysis: A Practical Introduction to Business Analytics now in its 8<sup>th</sup> edition. He received his PhD in management science and information technology from the University of Georgia.

## The Truck Driver Scheduling Problem with Fatigue Monitoring Highlights

 A fatigue-aware mathematical model for driver scheduling is proposed.

 Minimum and average driver alertness levels increase as a result of scheduling with fatigue measures in the model.

 Failure to account for start-of-schedule alertness may result in dangerous levels of fatigue and compromised safety.

 Start-of-schedule alertness should be considered in legislation related to hours-of-service regulations.

![](/api/attachments/FPZNAQVG/fulltext/images/dcd297872257ceda1cdff14e3ee1ccf31dd10117526ef63cb162bc5f9d03ef44.jpg)  
Figure 1

![](/api/attachments/FPZNAQVG/fulltext/images/1829793982395c690802a68f99733b51f752153ad14806fc4fee3017ce78b3cb.jpg)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
// step through times from leaving the previous location (i-1) to
// arriving at current location (i) in 15 minute increments
for $t_{now}$ in $D_{i-1}$ to $A_i$ step 0.25:
$k_{now}^{day} = t_{now} \mod 24 // time of day for C and U calculations$ $k_{now}^{awake} = taw_{i-1} + t_{now} // time awake$ $S_{now} = la + (S'_{i-1} - la) * e^{d*k_{now}^{awake}}$ $C_{now} = Cm + Ca * cos((2\frac{\pi}{24}) * (k_{now}^{day} - p))$ $U_{now} = Um + Ua * cos((2\frac{\pi}{12}) * (k_{now}^{day} - p - 3))$ $alertness_{now} = S_{now} + C_{now} + U_{now}$
// keep track of minimum alertness
if $alertness_{now} &lt; minalertness_i$ then
$minalertness_i = alertness_{now}$
</div>

![](/api/attachments/FPZNAQVG/fulltext/images/795a7449c364c2df424a658804b23e837ecd345e49adefd2b32e85f2b9d82580.jpg)  
Figure 4

![](/api/attachments/FPZNAQVG/fulltext/images/89dd0f171715569253c8f7928377b7038fd891d2cf9a21b270eb2b20d23df5de.jpg)  
Figure 5

![](/api/attachments/FPZNAQVG/fulltext/images/30134afb9a146c914aed13f1cbdc56af1cc3b25dcd8ec65e27e015a1d1a751df.jpg)  
Figure 6

![](/api/attachments/FPZNAQVG/fulltext/images/d91067e1866534a84102a8bbdf96f69b27ef9c0932515bef544576d04beddea1.jpg)  
Figure 7

![](/api/attachments/FPZNAQVG/fulltext/images/8c62ff11b513eb0d1b590083c175b126070726d4fb11d5ddabedadcbe8f5da31.jpg)  
Figure 8

Minimum Alertness Comparison with Danger Zone  
![](/api/attachments/FPZNAQVG/fulltext/images/a623e51ea496b2813acd369d70305529018c711ba4e2d662de52f86944884b57.jpg)  
Figure 9

![](/api/attachments/FPZNAQVG/fulltext/images/3e24ae4e4f3983e2e059a68497214df17925215e9f980ebd302a85fdd97c5e16.jpg)  
Figure 10
