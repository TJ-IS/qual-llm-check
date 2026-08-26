---
otero_id: 1808
otero_key: "JFBAPSC4"
title: "Optimal planning of sensor networks for asset tracking in hospital environments"
authors: "Antonio Pietrabissa; Cecilia Poli; Dario Giuseppe Ferriero; Mauro Grigioni"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.031"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal planning of sensor networks for asset tracking in hospital environments

Antonio Pietrabissa <sup>a,</sup>⁎<sup>,1</sup>, Cecilia Poli <sup>b,1</sup>, Dario Giuseppe Ferriero <sup>a</sup>, Mauro Grigioni <sup>b</sup>

<sup>a</sup> Università degli studi di Roma “La Sapienza”, Dipartimento di Ingegneria Informatica, Automatica e Gestionale “Antonio Ruberti”, via Ariosto 25, 00185, Roma, Italy <sup>b</sup> Istituto superiore di Sanità (ISS), Dipartimento di Tecnologie e Salute, via Regina Elena 299, 00161, Roma, Italy

## a r t i c l e i n f o

Article history: Received 14 March 2012 Received in revised form 28 September 2012 Accepted 21 January 2013 Available online 13 February 2013

Keywords: Hospital asset tracking Sensor networks Optimal planning Reinforcement learning

## a b s t r a c t

An optimization framework is proposed to plan a sensor network in hospital environments aimed at tracking medical assets. Firstly, an innovative statistical simulation model of the asset movements is developed, to de<sup>fi</sup>ne the critical levels of the hospital locations. The model feeds an optimization algorithm, which determines the optimal placements of the sensors, modeled by their coverage characteristics. Since the optimization framework is modular, it can be used for different network technologies. Simulation results are presented, considering a case-study based on the plan of the cardiology department of the “San Camillo” hospital in Rome and on interviews with the personnel.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Tracking of medical assets is one of the key problems in the hospital management, due to the facts that i) they have to be available as soon as needed, and ii) asset losses/thefts constitutes a substantial economic damage [8]. Therefore, the use of automation systems in hospitals is fast increasing [6].

Currently, the most suitable solution to the problem is the development of an information system, available to the operator terminals (both <sup>fi</sup>xed and mobile), which locates the assets in real-time thanks to a sensor network placed in the hospital critical areas. To set up the information system, three steps must be undertaken:

1. selection of a sensor network technology;

2. placement of the sensors on the hospital area to guarantee a desired coverage;

3. development of the data management system, of the communication infrastructure and of the user interface.

This paper deals with the <sup>fi</sup>rst two points of the list, by de<sup>fi</sup>ning an optimization framework which can be con<sup>fi</sup>gured to account for different sensor technologies. As described in Section 1.2, the framework consists of three phases: data collection, model development and optimization.

Collected data concern the hospital plan, the assets to be tracked, their criticality and usage, and the sensor characteristics.

The developed models are: a model of asset daily movements on the hospital plan, and a model of the coverage area of the sensor node in its possible con<sup>fi</sup>gurations (e.g., in terms of orientation, beam power). The models are described in the following. The <sup>fi</sup>rst one is an innovative statistical simulation model to account for the different critical levels of the medical assets and for their most common movements within the hospital: the result is a critical map (analogous to the one introduced by [15]), which weights differently the zones of the hospital plan. The second model is implicitly technology-dependent; however, the modularity of the proposed approach is such that changing the network technology implies only changing the sensor model, whereas the other models and algorithms remain the same.

In the optimization phase, two planning problems are considered, aimed i) at the maximization of the coverage given a <sup>fi</sup>xed number of sensor nodes, and ii) at the minimization of the number of sensor nodes, given a desired minimum coverage. The problems are formulated as binary (linear) set covering problems, which can be ef<sup>fi</sup>ciently solved by commercial or open source solvers even for a very large set of variables.

Note that, besides providing the optimal positioning and con<sup>fi</sup>guration for the sensor networks, the proposed framework helps in the network selection decision by performing the optimizations with different sensor technologies.

## 1.1. Related work and proposed innovations

In the literature, tracking of assets, personnel and patients in hospital environments has been subject of studies and validated via test beds, motivated by the critical environment and by the cost of medical devices [20], by the time lost to simply retrieve the needed equipment [9], and by the necessity of enhancing the asset availability avoiding redundancy [20]. Already in 2002, the results of an experimentation showed that the asset utilization is truly enhanced by tracking assets [13]. Other examples are in [3–5,11,14,16,21].

The optimization of the planning of the sensor network is a fundamental problem [2], both from the effectiveness of the solution point of view (the same number of sensor nodes guarantees a better coverage, if optimally positioned), and from the economic point of view (the required coverage performance may be achieved by a smaller number of nodes). Examples of optimization of sensor network planning are in [2], with an integer programming approach, in [7] and in [15], with a genetic algorithm approach, and in [1], with a swarm-optimization approach.

To set up a tracking system, the main decision concerns the technology to be used. Nowadays, different automatic identi<sup>fi</sup>cation technologies are available without dif<sup>fi</sup>culty off-the-shelf, such as RFID (Radio Frequency Identi<sup>fi</sup>cation), Bluetooth, Zigbee, Smart Cards, Smart Badges, WPS (WiFi-based positioning systems), IR (Infrared), UWB (Ultra Wide Band), and other technologies are emerging or are in the development phase, such as WISP (Wireless Identi<sup>fi</sup>cation and Sensing Platform). As analyzed in [4], the technology selection must be carried out on the ground of several factors, such as accuracy requirements (e.g., WiFi used for monitoring [13] has a precision which goes from zone to room-level, ZigBee or RFID from room to bed-level, IR guarantees a bed-level precision), electro-magnetic compatibility with medical devices, tracking characteristics (e.g., IR requires that the transmitter and the receiver are in line-of-sight, whereas WPS or RFID does not), economic considerations (e.g., enhancing an already existing WiFi to have a WPS might be economic, whereas UWB tracking is currently rather expensive). To account for the different hospital tracking requirements, different technologies might be found at disposal and used in an ultimately hybrid tracking system (e.g., [6]). Hence, it is important to conceive a planning approach which is as independent as possible of the sensor technology, and that can be used to simultaneously plan multiple sensor networks. In this respect, even if the use case presented in this paper is based on RFID technology, the overall approach is kept as technology independent as possible.

Nowadays, RFID sensor networks are currently the most used ones for the tracking of material assets in hospital environments (just to mention a few: [3,5,11,17,19]). RFID wireless identi<sup>fi</sup>cation technology is based on the communication between two entities: the proper sensor nodes, called reader or interrogator, and the transponders, named tags, passive or active, containing a chip with encoded identi<sup>fi</sup>- cation data and an antenna. Active tags increase the reach of the readers but require a battery and of cost much more (at least by one order of magnitude). The fact that a reader can be used with both active and passive tags can be useful in the hospital scenario, where more critical, expensive and/or frequently moved assets could be provided with active tags, whereas the other assets could be provided with cheaper passive tags. A key advantage of the RFID technology is that, being based on radio frequency communications, the tags are not required to be in the line of sight of the reader.

The approach followed by this work is mainly based on the approach introduced in [15], with the following improvements:

1. To calculate the criticality map, the hospital operators are no more required to give excessively detailed information for each plan location (which, by the way, is very dif<sup>fi</sup>cult to obtain in a real and wide hospital infrastructure); in the proposed approach, coarse grain information is required, such as storage locations, usage locations, and usage frequency. In this respect, the paper contribution is the development of a statistical simulation of the asset movements in the hospital environment by means of Reinforcement Learning methods [18] (see Section 3.2).

2. The sensor model is explicitly taken into account in the optimization process, whereas in [15] a simple omnidirectional approximated sensor coverage was considered. Moreover, different sensor technologies are seamlessly encompassed in the optimization task (see Section 3.1).

3. The optimal planning problem is formulated as an integer (linear) programming problem, which is fast solvable even for large numbers of variables by commercial or open-source solvers (e.g., IBM ILOG CPLEX Optimization Studio, lp\_solve, GLPK). In particular, the problem is formulated as a binary set covering one. The problem dealt with in this paper is considerably harder with respect to the one in [15], since more realistic sensor models and more constraints are considered; nevertheless, the solution algorithms of the proposed binary programming problem formulation are significantly more ef<sup>fi</sup>cient. Moreover, a second optimal planning problem is proposed (namely, the optimal planning of the minimum number of sensor nodes with a desired network coverage), additionally to one proposed in [15] (namely, the optimal planning of a given number of sensor nodes to maximize the network coverage) (see Section 4).

## 1.2. Proposed approach and paper outline

The proposed approach is summarized in Fig. 1.

The problem de<sup>fi</sup>nition, dealt with in Section 2, requires the establishment of the optimization objectives (Section 2.1), the de<sup>fi</sup>nition of the scenario, in terms of hospital plan and asset characteristics (Section 2.2), and the de<sup>fi</sup>nition of the sensor network properties, in terms of possible con<sup>fi</sup>gurations and of coverage characteristics (Section 2.3).

The models needed for the optimization are developed in Section 3. The hospital inputs of Section 2.2 are used to develop a statistical model of the movements of the medical assets within the hospital plan, as described in Section 3.2; this model is then used to compute the criticality map via a Markov Decision Process approach. The technology-dependent inputs concerning the sensor network characteristics are used to develop a coverage model of the sensor node under the different possible sensor con<sup>fi</sup>gurations, as described in Section 3.1; the model is then used to compute the coverage coef<sup>fi</sup>- cients, which indicate the plan zones (i.e., the squares of the grid) covered by a sensor in a given position and in a given con<sup>fi</sup>guration.

The optimal planning problem formulations are de<sup>fi</sup>ned in Section 4. In particular, Section 4.1 deals with the maximization of the network coverage given a number of sensor nodes, whereas Section 4.2 deals with the minimization of the number of sensor nodes, given the desired network coverage. The inputs required by the optimization algorithm are the hospital inputs (Section 2.2), the criticality map (Section 3.2) and the coverage coef<sup>fi</sup>cients (Section 3.1). Note that technology changes are easily dealt with by the proposed approach: in fact, different technologies lead to different coverage models which, in turn, simply leads to different coverage coef<sup>fi</sup>cients; the whole rest of the algorithm remains the same.

Some simulation results are reported in Section 5.

Finally, in Section 6 the conclusions are drawn.

## 2. Problem de<sup>fi</sup>nition

## 2.1. Optimization objectives

As explained in Section 1, the objective of the planning task is aimed at achieving the best possible coverage of the hospital plan, while keeping the cost of the sensor network as low as possible.

Two objectives are then envisaged:

1. Maximization of the network coverage, given a number of sensor nodes: if the hospital is already provided with a sensor network with a given number of nodes (or if the hospital already established the budget for the sensor network, thus limiting the number of nodes which will be available), the planning problem aims at <sup>fi</sup>nding the node positions which maximize the coverage of the plan.

![](/api/attachments/JFBAPSC4/fulltext/images/9a16fe84fd4e9835d08c576215fc90c68d45c9d8352c26cbfa739acdd006eb97.jpg)  
Fig. 1. Flow chart of the proposed optimization approach.

2. Minimization of the number of sensor nodes, given a desired network coverage: if the hospital de<sup>fi</sup>nes the objective coverage which is needed to meet its requirements, the planning problem aims at minimizing the number of nodes (i.e., at minimizing the budget dedicated to the sensor network).

As speci<sup>fi</sup>ed in Section 2.2, the network coverage will be appropriately weighted according to the importance of the different areas of the plan.

## 2.2. Input from the hospital

The <sup>fi</sup>rst input is the hospital plan. By considering one <sup>fl</sup>oor only, the plan with Cartesian axes, will be denoted with $P { \subset } \mathbb { R } ^ { 2 }$

The key factor in evaluating the coverage of the sensor network is the quanti<sup>fi</sup>cation of the relative importance of the different areas of the hospital plan, which, clearly, must be retrieved via interviews with the hospital personnel. Hence, the hospital personnel are required to provide information about the hospital areas which are more critical, and, therefore, whose coverage is more important with respect to other areas.

In [15], a criticality map is obtained by discretizing the hospital plan into square areas, and by obtaining from the hospital personnel, for each square area, the following data: the asset severity (i.e., its importance level evaluated by experts on a <sup>fi</sup>vepoint Likert scale [10]), the dwell time of the asset spent in the area per day, the frequency of the asset in the area per day. This set of information appears to be problematic to obtain for each area, and it becomes even harder if the planning accuracy is increased by reducing the granularity of the discretization (i.e., by decreasing the size of the square areas). Therefore, this paper proposes a different approach, in which coarser grain information is required for each asset: severity, storage locations, usage locations, usage frequency. In this way, on the one hand the hospital personnel are required to give simpler (and therefore more reliable) information, on the other hand, the de<sup>fi</sup>nition of the criticality map is not affected by the planning accuracy.

The criticality map is de<sup>fi</sup>ned over a discretized plan, which is a grid of $N _ { G }$ square areas. Each area is identi<sup>fi</sup>ed by the coordinates (x,y) of its center. The areas are collected in an ordered set $G = \{ 1 , 2 , . . . , N _ { G } \}$

An example of the described inputs follows, based on a preliminary interview with the personnel of the San Camillo hospital in Rome. Fig. 2 shows the plan of the cardiology department of the hospital, already approximated by the discretized map, with 1 m×1 m square areas. Table 1 shows an example of a list of the assets to be tracked, each one associated to a criticality indexes, storage locations, usage locations, and a usage frequency.

## 2.3. Technology-dependent input

The third kind of input required by the planning problem concerns the sensor technology, and is required to de<sup>fi</sup>ne the coverage of a given sensor node placed in a given plan area.

The coverage area of the sensor depends on the antenna characteristics, such as frequency range, beam width, and power. Moreover, usually the sensors can be set in different con<sup>fi</sup>gurations, for example by varying the beam orientation, the level of power, and the beam widths. The frequency range impacts on the way the sensor coverage is affected by the environment (i.e., walls, furniture, persons). The required data are detailed in the data sheets of the off-the-shelf sensors.

In this paper, we consider an approximated coverage model of an RFID sensor, based on the data sheet of the model Alien Technology®ALR-8610 EPC (http://www.prosign.dk). Considering the plan P, a suf<sup>fi</sup>ciently generic model is described by the <sup>fi</sup>ve variables.

![](/api/attachments/JFBAPSC4/fulltext/images/3a99021747f21b247c67ac60c0282f0f11ac76411598b71115496fcc952d3bb5.jpg)  
Fig. 2. Discretized hospital plan.

\- The couple $( x _ { r } , y _ { r } ) \in P _ { r } \subseteq P$ indicates the position of the sensor within the plan; P<sub>r</sub> is the set of allowed sensor positions in the plan. In this paper, all the positions in the plan close to a wall are considered as allowed; however, the set P is in reality smaller, both for the presence of furniture (i.e., cabinets, tables, shelves, …) and for places or rooms where placing a radio frequency sensor is not conceivable (e.g., in clean rooms).

\- The orientation of the antenna $\vartheta \in \Theta \equiv [ 0 , 2 \pi )$ , where, without loss of generality, we consider a 0 rad orientation if it is parallel to the x axis of the grid;

\- The angle of coverage of the antenna $\alpha \in \Theta \equiv [ 0 , \pi )$

\- The sensor range h∈ $H \equiv [ h _ { m i n } , h _ { m a x } ] , \mathrm { i . e . }$ , the maximum distance between the sensor and the tag, which depends on the reader power.

The tuple $\{ x _ { r } , y _ { r } , \vartheta , \alpha , h \} { \in } P _ { r } { \times } \Theta { \times } H$ de<sup>fi</sup>nes a feasible sensor con<sup>fi</sup>guration.

Let $( x _ { t } , y _ { t } ) \in P$ be the generic position of a tag. As depicted in Fig. 3a), the generic tag at location $\left( x _ { t } , y _ { t } \right)$ is then covered by a reader in con<sup>fi</sup>guration $\{ x _ { r } , y _ { r } , \vartheta _ { r } , h _ { r } \}$ if the following equations hold:

$$
d = \sqrt {(x _ {r} - x _ {t}) ^ {2} + (y _ {r} - y _ {t}) ^ {2}} <   h,\tag{1}
$$

$$
\vartheta - \alpha <   \beta <   \vartheta + \alpha ,\tag{2}
$$

where d is the distance between the reader and the tag and β is the angle between the x axis and the line joining the sensor position $( x _ { r } ,$ y ) and the tag position $\left( x _ { t } , y _ { t } \right)$

Sensors are subject to attenuations due to walls, furniture or any other object interposed between the antenna and the tag. An example of an approximate coverage variation due to the presence of a wall is shown in Fig. 3b). In this representation, it is assumed that the only effect of the wall is a complete attenuation. In reality, the effects due to objects between the sensor and the tag depend on many parameters, such as the object material and its thickness.

## 3. Problem models

3.1. Model to describe the sensor coverage under the different configurations

Among the sensor characteristics collected in the data sheets (see Section 2.3), the most relevant one to the planning problem is the coverage, which depends on the position of the sensor and on the shape and the dimension of the area where the tags can be sensed.

Eqs. (1) and (2) are nonlinear; moreover, the attenuation effects of the walls are nonlinear as well. Therefore, the formulation of an optimization problem in which those equations were implemented would be nonlinear, with drawbacks in terms of complexity and scalability.

Table 1 List of medical assets.

<table><tr><td>Asset</td><td>Severity [1-5]</td><td>Storage location (x,y)</td><td>Usage location (x,c)</td><td>Frequency (per day)</td></tr><tr><td>Disposable medical devices</td><td>1</td><td>(17,8)</td><td>(3,3)</td><td>10</td></tr><tr><td>Dressing medical devices</td><td>3</td><td>(17,15)</td><td>(3,15)</td><td>10</td></tr><tr><td>Anesthetic medical equipment</td><td>2</td><td>(3,26)</td><td>(17,37)</td><td>20</td></tr><tr><td>Blood pressure measuring equipment</td><td>4</td><td>(3,26)</td><td>(3,25)</td><td>30</td></tr><tr><td>Surgical instruments</td><td>4</td><td>(17,31)</td><td>(17,15)</td><td>45</td></tr><tr><td>Implantable medical devices</td><td>5</td><td>(3,3)</td><td>(17,26)</td><td>30</td></tr><tr><td>Parenteral feeding devices</td><td>3</td><td>(17,37)</td><td>(17,37)</td><td>50</td></tr><tr><td>Orthopedic medical devices</td><td>1</td><td>(3,26); (17,3)</td><td>(17,15); (16,31)</td><td>20</td></tr><tr><td>Sterile medical drapes</td><td>1</td><td>(17,37)</td><td>(16,32)</td><td>35</td></tr><tr><td>Bed and anti-decubitus mattress</td><td>5</td><td>(3,26); (3,8); (17,31)</td><td>(17,17); (17,31); (3,32)</td><td>45</td></tr><tr><td>Infusion pump</td><td>5</td><td>(3,20); (19,38); (17,37)</td><td>(3,31); (17,15); (17,38)</td><td>10</td></tr><tr><td>Portable X-ray equipment</td><td>4</td><td>(3,26)</td><td>(17,37)</td><td>15</td></tr><tr><td>Ultrasound equipment</td><td>3</td><td>(3,15)</td><td>(3,26)</td><td>20</td></tr><tr><td>Cardiac monitor</td><td>5</td><td>(3,26); (3,20)</td><td>(3,37); (19,38)</td><td>35</td></tr><tr><td>Defibrillators</td><td>5</td><td>(3,3); (17,37)</td><td>(3,20); (9,20)</td><td>15</td></tr><tr><td>Mechanical ventilation devices</td><td>5</td><td>(17,20)</td><td>(17,32)</td><td>25</td></tr><tr><td>Accessories for portable medical equipment</td><td>1</td><td>(17,32)</td><td>(17,37)</td><td>45</td></tr><tr><td>Wheelchair</td><td>3</td><td>(17,15); (3,20); (17,38)</td><td>(17,32); (17,37); (9,20)</td><td>35</td></tr><tr><td>Stretcher</td><td>3</td><td>(17,25); (3,3); (17,37)</td><td>(17,37); (17,3); (17,38)</td><td>35</td></tr></table>

![](/api/attachments/JFBAPSC4/fulltext/images/d13483642b01e4aad75219d4727ab3ee6d7a6a57335b4fa8f37c377d78005e3e.jpg)

![](/api/attachments/JFBAPSC4/fulltext/images/77be949f31d90edd8cf11c7a4bc6374c0c5e250f69ae01dba095126464bfadb8.jpg)  
Fig. 3. Sensor coverage, without a) and with b) the presence of a wall between the sensor and the tag.

To formulate the problem as a linear set covering one, this paper proposes to preliminary compute the possible coverage areas of the sensors in all the possible con<sup>fi</sup>gurations. To achieve this result, a discretization of all the variables de<sup>fi</sup>ned above is required.

Let $P _ { r } \subseteq P$ be the set of allowed sensor positions in the plan $P ,$ discretized into a subset of the grid $G _ { r } \subseteq G ;$ let N be the number of areas in $G _ { r } ,$ with $N _ { r } { \le } N _ { G }$

Concerning the sensor con<sup>fi</sup>gurations, the sensor position is now limited by the set $G _ { r }$ the orientation of the antenna ϑ is limited to $N _ { \vartheta }$ values, $\begin{array} { r } { \vartheta { \in } \Big \{ i \frac { 2 \pi } { N _ { \vartheta } } \Big \} _ { i = 0 , 1 , \dots , N _ { \vartheta } - 1 } , } \end{array}$ , the angle of coverage α is limited to $N _ { \alpha }$ values, $\scriptstyle \alpha \in \left\{ i { \frac { \pi } { N _ { \alpha } } } \right\} _ { i = 0 , 1 , \dots , N _ { \alpha } - 1 } ,$ , and the sensor range h is limited to $N _ { h }$ values, $\begin{array} { r } { h { \in } \Big \{ h _ { m i n } + i \frac { h _ { m a x } - h _ { m i n } } { N _ { \mathrm { h } } - 1 } \Big \} _ { i = 0 , 1 , \dots , N _ { \mathrm { h } } - 1 } } \end{array}$ . Let R be the (<sup>fi</sup>nite, discrete) <sup>¼</sup>set of possible readers' con<sup>fi</sup>gurations, whose cardinality (i.e., the total number of possible sensor con<sup>fi</sup>gurations) is then $N _ { r } { \times } N _ { \vartheta } { \times } N _ { \propto } { \times } N _ { h } .$ The discretization granularity is a project parameter which clearly leads the tradeoff between accuracy of the solution and scalability of the optimization problem.

Finally, also the tag position is discretized, and the allowed positions are the areas in G.

The main idea of the approach proposed in this paper is that the sensor con<sup>fi</sup>gurations are used to compute the tag coverage as input of the optimization problem, instead of explicitly implementing the discretized versions of Eqs. (1) and (2) in the problem. In this way, as shown in Section $^ { 4 , }$ it is possible to formulate a linear optimization problem.

In particular, the coverage coef<sup>fi</sup>cients $a _ { i j }$ are introduced:

$$
a _ {i j} = \left\{ \begin{array}{c} 1 \text {   if   a   reader   in   configuration   } i \text {   covers   a   tag   in   position   } j \\ 0 \text {   otherwise } \end{array} , i \in R, j \in G. \right. \tag {3}
$$

The generic coverage coef<sup>fi</sup>cient $a _ { i j }$ is computed according to Eqs. (1) and (2), and also taking into account that the coef<sup>fi</sup>cient value is 0 if there is a wall between the sensor and the tag. In Eq. (3), $\left( x _ { r } y _ { r } \right)$ are now the coordinates of the center of the grid area of the reader in con<sup>fi</sup>guration $i \in R ,$ whereas $( x _ { t } , y _ { t } )$ are the coordinates of the center of the grid area j∈G where the tag is positioned. Let A be the set of coverage coef<sup>fi</sup>cients, which serves as input for the optimization problem.

Remark 3.1.1. Even if a very simple attenuation model is considered in this paper, this methodology allows adding more complex and realistic models in a straightforward way. In fact, even considering the whole planning algorithm, the attenuation model is used only to compute the coverage coef<sup>fi</sup>cients. By collecting data on the wall and the furniture present in the hospital, more precise coverage coef<sup>fi</sup>cients $a _ { i j }$ can be computed by considering the effects of the wall and the objects located between the position of the sensor and the center of the grid area j.

Remark 3.1.2. The only part of the planning procedure related to the sensor's technical characteristics are the coverage coef<sup>fi</sup>cients $a _ { i j } .$ In fact, by changing the sensor type, the coverage characteristics would be different; however, as already mentioned in Section 1.2, it is suf<sup>fi</sup>- cient to change the admissible values of the parameters (or, at the most, to add parameters to model possibly advanced sensor characteristics) to describe the con<sup>fi</sup>gurations of the new sensor and to compute the coverage coef<sup>fi</sup>cients, which, then, can be seamlessly used in the optimization procedure described in Section 4. This means that the optimization tool proposed in this paper can be used to compare different sensor types or even different sensor technologies, provided that the coverage characteristics are properly modeled.

Remark 3.1.3. The plan was already similarly discretized in [15], but the reader con<sup>fi</sup>gurations were not speci<sup>fi</sup>ed (the sensor coverage was modeled as if the sensor was provided with a simple omnidirectional antenna) and, therefore, the nonlinear constraints were not dealt with as in this paper.

## 3.2. Model to describe the movements of the hospital assets

In the previous section, it is explained how it is possible to describe the fact that a reader in a given position on the grid is able to sense a tag in another position. This section deals with the problem of identifying the positions on the grid which are more important to cover.

Starting from the inputs identi<sup>fi</sup>ed in Section 2.2, the idea is <sup>fi</sup>rstly to estimate the path of the assets to be tracked from the repository to the places where they are used (Section 3.2.1), then to estimate the probability that the assets are located in each grid area (Section 3.2.2); <sup>fi</sup>nally the criticality map is obtained by weighting the probabilities by the asset criticalities (Section 3.2.2).

## 3.2.1. Computation of the asset paths

For each asset, since the start and end points of the movements are given by the hospital inputs (described in Section 2.2), it would be straightforward computing the path between the start and the end points. However, it must be considered that the hospital operators are not likely to always follow the same path, due to various reasons. Therefore, in this paper we propose to develop a statistical model to account for unplanned deviations.

For each asset, the path discovery problem is formulated as a Reinforcement Learning (RL) task [18]. Considering an agent taking decisions in a statistical environment, RL is a methodology, widely used in the literature for routing problems (e.g., [12]) which computes the agent's optimal policy based on the observation of the environment after a decision is taken. In brief, the RL task is organized in stages $t { \in } [ 1 , 2 , . . . , T ]$ , where T can also be in<sup>fi</sup>nite, and requires the de<sup>fi</sup>nition of a <sup>fi</sup>nite state space S, a <sup>fi</sup>nite set $A ( s )$ of actions a which can be chosen in state s, a reward function r which maps each state to a real number. Hereafter, the state, action and reward at stage t will be denoted with, $s _ { t } , a _ { t }$ and $r _ { t } ,$ respectively.

The agent operates according to an ‘action-value’ function Q(s,a), de-<sup>fi</sup>ned for each state s∈S and for each action a∈ $\operatorname { \mathrm { : } } A ( s )$ :the value $Q ( s , a )$ , in fact, represents the expected reward for the agent when it is in state s and takes action a. The agent is said to follow the greedy policy if, in each state $s ,$ it always chooses the best action (i.e., the action which has the highest value in $Q ( s , a ) , a \in A ( s ) ;$ ). Another common policy is the so-called ε-greedy policy, where the agent selects the best action with probability $1 - \varepsilon ,$ and a random action (among the ones available in A(s)) with probability ε.

The RL objective is to estimate the values of $Q ( s , a )$ . The agent starts with a arbitrary action-value function ${ \cal Q } ( s , a ) ~ ( \mathrm { e . g . } , { \cal Q } ( s , a ) = 0$ for each s and a) and updates it on-line: at each stage t, the agent in state $s _ { t } \ 1 )$ takes an action a among the set $A ( s _ { t } ) , 2 )$ observes the next state $s _ { t + 1 }$ and the associated reward $r _ { t + 1 } ,$ and 3) updates the value of $Q ( s _ { t } , a _ { t } )$ . Several algorithms (see [18] and references therein) exist which appropriately de<sup>fi</sup>ne the update rule in order to achieve the optimal estimates of the action-value function.

In our problem, the agent is the operator transporting the asset m from the start to the end point; the state space is given by the (discretized) grid $G ,$ and the states are the grid areas $j \in G ;$ in each state, the agent actions are the movement direction, e.g., north ↑, east →, south ↓, west ←; the reward is 1 if the agent reaches the end point, 0 otherwise. Among the available algorithms, we used the Q-learning algorithm to update the action value function and an ε-greedy policy to drive the agent's decisions. The $\scriptstyle { \mathrm { Q } } \ { \mathrm { } }$ -learning was selected since it is already successfully being used in several applications and since it has a simple update rule:

$$
Q \left(s _ {t}, a _ {t}\right) \leftarrow Q \left(s _ {t}, a _ {t}\right) + \left[ r _ {t + 1} + \gamma \max _ {a \in A \left(s _ {t + 1}\right)} Q \left(s _ {t + 1}, a\right) - Q \left(s _ {t}, a _ {t}\right) \right],\tag{4}
$$

where $Q _ { m }$ denotes the action-value function computed for asset m, $\begin{array} { r } { m = 1 , 2 , . . . , M , } \end{array}$ , α is the step-size and $\gamma \in [ 0 , 1 )$ is the discount factor. The step-size must be chosen in order to guarantee convergence; in the implementation we selected a standard step-size $\alpha { = } 1 / t$ . The discount factor is signi<sup>fi</sup>cant in different <sup>fi</sup>elds (e.g., economics) to account for the preference of incurring in immediate rewards with respect to delayed rewards; in the considered case, the discount factor is not this relevant, and we set it as $\gamma { = } 0 . 9 9$ (for insights on the Q-learning, the interested reader is referred to [18]).

For each asset, the result of the Q-learning algorithm is the identi-<sup>fi</sup>cation, in each grid area, of the best direction the agent has to take to arrive at destination. Fig. 4 shows an example of optimal directions computed via the proposed procedure on a simple 15×11 grid, starting from a random policy.<sup>2</sup> The found optimal policy constitutes the model of the asset movements: the asset moves according to an ε-greedy choice over the available directions, i.e., it moves in the optimal direction with probability ε and in a random direction with probability 1−ε. This model is used in the following section to simulate the asset movements over the hospital plan.

3.2.2. Simulation of the asset movements and computation of the criticality map

The model of asset movements is used to compute the criticality map c, which associates each grid area $j { \in } G$ to a real number $c _ { j }$ representing the criticality value.

The action-value functions of each asset $Q _ { m } ( s , a ) , \ m = 1 , 2 , . . . , M$ (computed as explained in the previous section) are used to perform simulations of the asset movements. In particular, for a given asset m, a number num\_sim of simulation runs is performed: the duration of each simulation run is equal to one day, and the number of times the asset is moved in each run is given by table in Section 2.2. Each time the asset m is moved, starting from its start point, the path toward the destination is decided by using its action-value function $Q _ { m } ( s , a )$ according to an ε-greedy policy. Each time the asset is on a grid area $j \in G ,$ its criticality value is increased by the criticality index of asset m.

Once num\_sim simulation runs are performed for each asset m, $\begin{array} { r } { m = 1 , 2 , . . . , M , } \end{array}$ the criticality map is normalized to the highest criticality value of all the grid areas, to obtain a map c with values between 0 and 1.

Fig. 5 shows the criticality map obtained considering the map and the asset parameters of Section 2.2, with num $\AA . 5 i m = 3 0$ and $\varepsilon = 0 . 1$

## 4. Optimal planning

On the ground of the coverage coef<sup>fi</sup>cients $a _ { i j } , i { \in } R , j { \in } G ,$ , computed in Section 3.1, and of the criticality values $c _ { j } , j { \in } G ,$ computed in Section 3.2, this section formulates the planning problem as a set covering binary programming problem.

Two problems are formulated to account for the two optimization objectives de<sup>fi</sup>ned in Section 2.1: the maximization of the sensor network coverage, given a number of sensor nodes, de<sup>fi</sup>ned in Section 4.1, and the minimization of the number of sensor nodes, given a desired network coverage, de<sup>fi</sup>ned in Section 4.2.

4.1. Maximization of the network coverage, given a number of sensor nodes

With this problem, the number of sensor nodes is given; therefore, the problem solution must determine the con<sup>fi</sup>guration of each sensor. As stated in Section 3.1, for each sensor the number of con<sup>fi</sup>gurations is R. Let Q be the number of sensor. Then, the problem has $R \times Q$ binary variables $x _ { r i \cdot }$

$$
x _ {r i} = \left\{ \begin{array}{l} 1 \text {   if   sensor   } r \text {   is   in   configuration   } i \\ 0 \text {   otherwise } \end{array} , r = 1, 2,..., R, i = 1, 2,..., Q. \right.\tag{5}
$$

Moreover, additional G variables $y _ { j }$ account for the coverage of the grid areas:

$$
y _ {j} = \left\{ \begin{array}{l} 1 \text {   if   grid   area   } j \text {   is   covered } \\ 0 \text {   otherwise } \end{array} \right., j = 1, 2,..., G.\tag{6}
$$

The objective function is aimed at maximizing the network coverage, weighted by the criticality map (computed in Section 3.2) which determines the importance of covering the grid areas:

$$
J (x, y) = \sum_ {j = 1, 2, \dots , G} c _ {j} y _ {j}.\tag{7}
$$

To specify that each sensor can be in only one con<sup>fi</sup>guration, the following constraints are implemented:

$$
\sum_ {i = 1, 2, \dots , Q} x _ {r i} = 1, r = 1, 2, \dots , R.\tag{8}
$$

![](/api/attachments/JFBAPSC4/fulltext/images/afc87a4d6e695b86c9d182c78f48337ba42a0169f0944e69fbad2efcf1a75336.jpg)  
Fig. 4. Example of the computation of the path of one asset on a simple grid-world

The following constraints express the dependence of the variable y on the sensor con<sup>fi</sup>guration x, by exploiting to the information collected in the coverage coef<sup>fi</sup>cients (computed in Section 3.1):

$$
y _ {j} \leq \sum_ {i = 1, 2, \dots , Q} a _ {i j} x _ {r i}, j = 1, 2, \dots , G.\tag{9}
$$

In fact, if no sensor is in a con<sup>fi</sup>guration which covers grid area $j ,$ constraint (9) ensures that the variable $y _ { j }$ is null. On the other hand, if at least one con<sup>fi</sup>guration covers the grid area, constraint (9) is not activated, in the sense that $y _ { j }$ can be either 0 or 1. However, in this case, since the problem aims at maximizing Eq. (7), in the optimal solution y will be set to 1.

Finally, the following constraints specify that the variables are binary ones:

$$
x _ {r i} \in \{0, 1 \}, r = 1, 2, \dots , R, i = 1, 2, \dots , Q,\tag{10}
$$

$$
y _ {j} \in \{0, 1 \}, j = 1, 2, \dots , G.\tag{11}
$$

In conclusion, the binary programming problem 4.1 is to maximize the objective function (7) subject to the constraints (8)–(11)

4.2. Minimization of the number of sensor nodes, given a desired network coverage

With this problem, the value C of the minimum acceptable coverage is given, while the number of sensor nodes has to be minimized; therefore, the problem solution must determine both the number of sensors and their con<sup>fi</sup>guration.

The main difference is that now there is no <sup>fi</sup>xed number of readers Q. As stated in Section 3.1, for each sensor the number of con<sup>fi</sup>gurations is R. The problem has R binary variables $x _ { r 1 }$ and G binary variables y , de<sup>fi</sup>ned by Eqs. (5) (with Q=1) and (6). Since, in practice, 2 readers cannot have the same con<sup>fi</sup>guration (also recalling that the position is part of the con<sup>fi</sup>guration parameters), the meaning of the generic variable $x _ { r 1 }$ is as follows: if $x _ { r 1 } = 1 ,$ , there is a reader in con<sup>fi</sup>guration $r ;$ if $x _ { r 1 } = 0$ , there is no reader in con<sup>fi</sup>guration r. The number of reader is the sum of the variables $x _ { r 1 } , \ r = 1 , . . . , R .$

Therefore, constraint (8) no longer holds, whereas constraint (9) is modi<sup>fi</sup>ed as follows:

$$
y _ {j} \leq \sum_ {r = 1, 2, \dots , R} x _ {r 1}, j = 1, 2, \dots , G.\tag{12}
$$

![](/api/attachments/JFBAPSC4/fulltext/images/23b49e30354e12d08e9eccae4d956ddccaef508a797f7951ed249fd8f36876dd.jpg)  
Fig. 5. Example of criticality map.

![](/api/attachments/JFBAPSC4/fulltext/images/80fe555164da124c8760fa3c89b94696e41cc407e40291d31a5322b0f704ae18.jpg)  
Fig. 6. Maximum coverage (43.98%) with 3 readers.

Constraints (10)–(11) still hold. Finally, the following constraint is added to check that the obtained coverage is suf<sup>fi</sup>cient:

$$
\sum_ {j = 1, 2, \dots , G} c _ {j} y _ {j} \geq C.\tag{13}
$$

The objective function is now aimed at minimizing the number of sensors $\sum { } _ { i = 1 } ^ { R } x _ { r 1 } .$ . However, maximizing the network coverage is still important. A second term is then added to the objective function, which accounts for the obtained coverage, in a multi-objective fashion:

$$
J (x, y) = \sum_ {i = 1} ^ {R} x _ {r 1} - \omega_ {C} \sum_ {j = 1, 2, \dots , G} c _ {j} y _ {j},\tag{15}
$$

where $\omega _ { C }$ is the weight of the obtained coverage. The value of the coverage coef<sup>fi</sup>cients $c _ { j }$ is between 0 and 1; by setting $\omega _ { C } { < } \frac { 1 } { G } ,$ the second term of Eq. (15) is smaller than 1; in practice, this means that it is in charge of maximizing the coverage only once the number of sensors is minimized.

In conclusion, the binary programming problem 4.2 is to minimize the objective function (15) subject to the constraints (10)–(13).

## 4.3. Considerations

The problems can be straightforwardly extended to the case of heterogeneous networks, $\mathrm { e . g . }$ , of networks using more technologies for the sensors and/or for the tags. For example, let us consider a RFID network encompassing both passive and active tags. This case is meaningful since it is conceivable to use active tags (more ef<sup>fi</sup>cient but more expansive) for the critical assets, and passive tags for the others. To address this case, it is suf<sup>fi</sup>cient to de<sup>fi</sup>ne two criticality maps, one for the assets with active tags and one for the assets with passive tags, i.e., to compute two sets of criticality values, and to correspondingly compute two coverage models, i.e., to compute two sets of coverage coef<sup>fi</sup>cients. Hence, the placement of a sensor with a given con<sup>fi</sup>guration gives rise to two different coverage coef<sup>fi</sup>cients, one for the active and one for the passive tags.

Finally, since the algorithms which are available to solve binary programming problems are vastly more ef<sup>fi</sup>cient than the ones used in previous researches (e.g., genetic algorithms in [7] and [15], swarm optimization in [1]), the proposed approach can be conveniently used also to plan a much wider sensor network, covering for example an entire hospital building.

![](/api/attachments/JFBAPSC4/fulltext/images/0f8de0c0786f7bda5fd0ab3056df04172b2cf7b7093e70c433c026b241e2c324.jpg)  
Fig. 7. Minimum number of readers (4) to obtain 50% coverage.

![](/api/attachments/JFBAPSC4/fulltext/images/04006cc297a247c62e0fc4663f9046d6bd0a2c7aae16fa0aa6d7f6b109f8f69e.jpg)  
Fig. 8. Coverage obtained with and without considering the criticality in the planning phase.

## 5. Simulation results

This section presents some simulation results obtained by implementing the models and the algorithms de<sup>fi</sup>ned in Sections 3 and 4, respectively. The following data ranges were considered for the sensor nodes:

\- the allowed sensor positions, i.e., the areas in the set $G _ { r }$ , are only the areas which are limited by at least one wall area;

\- the orientation of the antenna ϑ is limited to $N _ { \vartheta } = 8$ values: $\vartheta { \in } \{ i \textstyle { \frac { \pi } { 4 } } \} _ { i = 0 , 1 , \ldots , 7 } ;$

<sup>¼</sup>- the angle of coverage α is <sup>fi</sup>xed to $3 5 ^ { \circ } \left( N _ { \alpha } = 1 \right)$

\- the sensor range h is limited to $N _ { h } { = } 3$ values between 5 m and 7 m: $h \in \{ 5 + i \} _ { i = 0 , 1 , 2 }$

Two examples of simulation results are shown in Figs. 6 and 7. Fig. 6 shows the optimal con<sup>fi</sup>guration of the readers when the number of readers is 3; the maximum coverage, evaluated by taking into account the criticality map, is 43.98%. Fig. 7 shows the optimal placement of the minimum number of readers (4), in the example in question needed to achieve the target 50% of coverage.

To evaluate the effectiveness of the obtained planning, two sets of simulations were set up. Each set consists of 19 simulations, aimed at minimizing the number of readers with increasing values of the desired coverage, from 5% to 95%. In the <sup>fi</sup>rst set, the criticality map was used within the optimization algorithm, as described in Section 4.2, whereas, in the second set, no criticality map was implemented. Fig. 8 shows that, by identifying the critical areas of the plan, the criticality map allows a signi<sup>fi</sup>cant reduction of the required number of readers, and hence of the sensor network cost; on average, the reduction was of about 40%.<sup>3</sup>

## 6. Conclusions and on-going research

This paper presented an optimization framework for the planning of a sensor network in hospital environments. Three main innovations were introduced: 1) the development of a statistical model of the asset movements in the hospital environment by means of Reinforcement Learning methods; 2) the development of a technology-dependent sensor model which is explicitly taken into account in the optimization algorithm; 3) the formulation of the optimal planning problem as a binary (linear) programming problem. Furthermore, the overall procedure is modular, in such a way that changing the sensor technology just requires the de<sup>fi</sup>nition of the related model, leaving the other parts of the procedure unchanged; in this way, the proposed procedure can be used to support the choice of the most appropriate sensor technology.

On-going work is aimed at enhancing the models of the plan and of the sensor coverage to obtain more accurate simulation of the actual sensor network coverage. In particular, a <sup>fi</sup>ner grid is required to cope not only with walls but also with the other objects present in the hospital (such as cabinets, desks, beds), which can interfere with the sensor beams; correspondingly, the sensor model is being enhanced to take into account those interferences. Field-tests by the “San Camillo” hospital are also foreseen.

## Acknowledgments

The authors wish to gratefully thank Dr. Sergio Pillon, President of the Italian Telemedicine Society (SIT), Prof. Luciano Tarricone, head of the ElectroMagnetic Lab Lecce of the University of Salento, and Dr. Silvia Canale of the University of Rome Sapienza for their precious help. The work is partially supported by the Strategic Program of the Ministry of Health: “Sicurezza e Tecnologie Sanitarie”.

## References

[1] I. Bhattacharya, U.K. Roy, Optimal placement of readers in an RFID network using particle swarm optimization, International Journal of Computer Networks & Communications (IJCNC) 2 (2010) 225–234.

[2] K. Chakrabarty, S.S. Iyengar, H. Qi, E. Cho, Grid coverage for surveillance and target location in distributed sensor networks, IEEE Transactions on Computers 51 (2002) 1448–1453

[3] S. Davis, Tagging along. RFID helps hospitals track assets and people, Health Facilities Management 17 (2004) 20–24.

[4] I. D'Souza, Wei Ma, C. Notobartolo, Real-time location systems for hospital emergency response, IT Professional 13 (2011) 37–43.

[5] J.A. Fisher, Indoor positioning and digital management: emerging surveillance regimes in hospitals, in: T. Monahan (Ed.), Surveillance and Security: Technologica Politics and Power in Everyday Life, Routledge, New York, 2006, pp. 77–88.

[6] G.H.P. Florentino, H.U. Bezerra, H.B. de A. Júnior, M.X. Araújo, R.A. de M. Valentim, A.H.E. Morais A.M.G. Guerreiro G.B. Brandão C.A. Paz de Araúio Hospital automation RFID-based: technology stored in smart cards, Proc. World Congress on Engineering 2008 (WCE 2008), July 2–4, 2008, London, UK., IAENG, pp. 1692–1695.

[7] Q. Guan, Y. Liu, Y. Yang, W. Yu, Genetic approach for network planning in the RFID systems, Proc. of the Sixth International Conference on Intelligent Systems Design and Applications, 2006, pp. 567–572.

[8] S.H. Lee, A.W. Ng, K. Zhang, The quest to improve Chinese healthcare: some fundamental issues, International Journal of Health Care Quality Assurance 20 (2007) 416–428.

[9] L.S. Lee, K.D. Fiedler, J.S. Smith, Radio frequency identi<sup>fi</sup>cation (RFID) implementation in the service sector: a customer-facing diffusion model, International Journal of Production Economics 112 (2008) 587–600.

[10] R. Likert, A technique for the measurement of attitudes, Archives of Psychology 22 (1932) 1–55.

[11] P. Lindqvist,R<sup>fi</sup>d monitoring of health care routines and processes in hospital envi ronment, M.Sc. thesis, Aalto University (2006)

[12] D. Macone, G. Oddi, A. Pietrabissa, MQ-Routing: mobility-, GPS- and energy-aware routing protocol in MANETs for disaster relief scenarios, Ad Hoc Networks, October 15 2012, (Available online).

[13] S. Manfredi, A reliable and energy ef<sup>fi</sup>cient cooperative routing algorithm for wireless monitoring systems, IET Wireless Sensor Systems 2 (2012) 128–135.

[14] T. Ostbye, D. Lobach, D. Cheesborough, A. Lee, K. Krause, V. Hasselblad, D. Bright Evaluation of an infrared/radiofrequency equipment-tracking system in a tertiary care hospital, Journal of Medical Systems 27 (2003) 367–380.

[15] A. Oztekin, F.M. Pajouh, D. Delen, L.K. Swim, An RFID network design methodology for asset tracking in healthcare, Decision Support Systems 49 (2010) 100–109.

[16] A. Panangadan, S. Muhammad Ali, A. Talukder, Markov decision processes for control of a sensor network-based health monitoring system, Proceedings of the National Conference on Arti<sup>fi</sup>cial Intelligence 20 (2005) 1529–1534.

[17] E. Paul, Reengineering medication management from the bedside using bar-coding and wireless technology, HIMSS Publication 1 (2004) 61–69.

[18] Barto Sutton, Reinforcement Learning: An Introduction, MIT Press, Cambridge, MA 1998.

[19] Y.J. Tu, W. Zhou, S. Piramuthu, Identifying RFID-embedded objects in pervasive healthcare applications, Decision Support Systems 46 (2009) 586–593.

[20] S.F. Tzeng, W.H. Chen, F.Y. Pai, Evaluating the business value of RFID: evidence from <sup>fi</sup>ve case studies, International Journal of Production Economics 112 (2008) 601–613.

[21] U. Varshney, Pervasive healthcare computing: EMR/EHR, Wireless and Health Monitoring, Springer Science and Business Media, New York, NY, 2009.

Dr. Antonio Pietrabissa is Assistant Professor with the “Dipartimento di Ingegneria Informatica, Automatica e Gestionale” of the University of Rome “La Sapienza”, where he received his Master's degree and his PhD in 2000 and 2004, respectively, and where he holds the course “Foundations of Systems Theory”. His research focus is the application of system and control theory methodologies to telecommunication networks. He has been involved in several EU and ESA funded projects (GEOCAST, DOMINO2, SATIP6, SATSIX, SAFEDEM, DAIDALOS, EUQoS, DLC-VIT4IP, MONET) and Italian-funded projects on telecommunications. He is author of more than 60 papers and book chapters on these topics.

Dr. Cecilia Poli is a Researcher of the Department of Technology and Health of the “Istituto Superiore di Sanità” (ISS) of Rome- the Italian National Institute of Health. She received her Master's degree in electronic engineering in 2003 and her PhD in 2006 with the University of Rome “La Sapienza” focusing the attention on biomedical applications. She is expert on the EU regulatory framework of medical devices and has been involved in several Ministry of Health projects based on the safety of medical devices and health technologies.

Dario Giuseppe Ferriero received his Master's degree in systems engineering at the University of Rome “La Sapienza” in 2011. His studies focus on the application of modeling, control theory and software development to bioengineering. He has been involved in a EU funded project (SM4ALL).

Dr. Mauro Grigioni is a Research Director of the Department of Technology and Health of the “Istituto Superiore di Sanità” (ISS) of Rome. He received the Master's degree in electronic engineering in 1985 at the University of Rome “La Sapienza”. Since 1988 he has been in the Cardiovascular Bioengineering Unit of ISS. In 2007 he was appointed head of the Biomechanics and Rehabilitative Technology Unit of the Department of Technology and Health. He has also the responsibility to coordinate the EU Medical Device directives Technology Assessment for the same department. His skills are in the Cardiovascular Biomechanics, Blood Damage and diagnostic techniques such as US, MRI etc., telemedicine and health care systems for chronicity. He has been involved in several national and EU research projects with the scienti<sup>fi</sup>c responsibility.
