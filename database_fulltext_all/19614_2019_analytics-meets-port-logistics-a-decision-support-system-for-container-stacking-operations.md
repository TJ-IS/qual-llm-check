---
otero_id: 19614
otero_key: "FZDUX9V8"
title: "Analytics meets port logistics: A decision support system for container stacking operations"
authors: "Sebastián Maldonado; Rosa G. González-Ramírez; Francisca Quijada; Adrián Ramírez-Nafarrate"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.04.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Analytics meets port logistics: A decision support system for container stacking operations

Decision Support Systems

Sebastián Maldonado, Rosa G. González-Ramírez, Francisca Quijada, Adrián Ramírez-Nafarrate

![](/api/attachments/FZDUX9V8/fulltext/images/ad6c0e49db89fa19851a1a468f316d5a3d59abfaf2e04f62deffdcda30e3ace1.jpg)

PII: S0167-9236(19)30073-9

DOI: https://doi.org/10.1016/j.dss.2019.04.006

Reference: DECSUP 13057

To appear in: Decision Support Systems

Received date: 18 December 2018

Revised date: 22 April 2019

Accepted date: 26 April 2019

Please cite this article as: S. Maldonado, R.G. González-Ramírez, F. Quijada, et al., Analytics meets port logistics: A decision support system for container stacking operations, Decision Support Systems, https://doi.org/10.1016/j.dss.2019.04.006

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Analytics meets Port Logistics: A Decision Support System for Container Stacking Operations

Sebasti´an Maldonado<sup>a,∗</sup>, Rosa G. Gonz´alez-Ram´ırez<sup>a</sup>, Francisca Quijada<sup>a</sup>, Adri´an Ram´ırez-Nafarrate<sup>b</sup>

<sup>a</sup>Facultad de Ingenier´ıa y Ciencias Aplicadas, Universidad de los Andes, Mons. Alvaro<sup>´</sup> del Portillo 12455, Las Condes, Santiago, Chile.

<sup>b</sup>Escuela de Ciencias Econ´omicas y Empresariales, Universidad Panamericana, Prol. Calzada Circunvalaci´on Pte. 49, Zapopan, Jalisco, M´exico.

## Abstract

A Decision Support System (DSS) is proposed in this paper for improving container stacking operations. This DSS addresses the stacking problem for import containers via a two-step strategy. First, dwell times are predicted for each container using analytics techniques. This prediction is used as an input for a mathematical programming model that minimizes container rehandles heuristically. Numerical examples are presented using data from the Port of Arica in Chile as a case study. The results confirm the virtues of the proposed DSS to efectively support planning decisions at the container yard. Furthermore, results also show good performance of the operations at the yard in terms of rehandles in comparison with the current practices of this port terminal and well-known stacking strategies.

Keywords: Port logistics, Model-driven decision support systems, Analytics, Dwell time prediction, Container stacking.

## 1. Introduction

Maritime ports play a key role as part of the international transport chain in guaranteeing eficient cargo handling, serving as the transfer infrastructure for cargo being transported by vessels. The introduction of bigger size vessels by the shipping lines is putting more pressure at the port termi nals, requiring to handle more containers in shorter time periods. For this reason, DSSs play an important role to support decision making for planning operations.

During the transfer services at a port terminal, containers are stored temporarily at the yard, that is divided into blocks. The time spent by a container at the port terminal is denoted as dwell time. This is a key performance metric of container terminals, whose goal is to minimize it (B¨ose, 2011; Merckx, 2005). As the exact retrieval sequence is not known in advance, it is quite common to incur in rehandles of containers to move containers that are blocking the one to be retrieved. Hence, one of the objectives of yard managers is to define a stacking policy that may reduce such rehandles that may reflect in a better space utilization and minimizing both ship turnaround times and truck turnaround times (Borgman et al., 2010; B¨ose, 2011).

Considering the Port Terminal of Arica (TPA) in Chile as a case study, we propose a DSS for the stacking problem of import containers. This port has the particularity that 70% of the cargo there corresponds to in-transit cargo from or to Bolivia. This is important since no storage fees are charged on Bolivian cargo due to the Peace Agreement of 1904 between these two countries (T´ellez, 1989). This fact leads to highly variable and large dwell times. The proposed DSS first estimates dwell times using the well-known analytics approach called Random Forest for regression. Then, heuristic approaches are proposed for minimizing rehandles by avoiding blocking containers that have short expected dwell times with containers with longer dwell times. The main contribution of our approach is the combination of these two domains. Although dwell time prediction and container stacking, have been studied and reported in the OR literature independently, we propose a DSS that integrates a novel stacking strategy based on predictive analytics to support decision planning.

The DSS proposed in this manuscript supports decision making in a very complex situation that port managers face day-to-day. Since the port

# ACCEPTED MANUSCRIPT

managers do not have information in advance on the dispatching sequence and container flows, the traditional methodologies for solving the container stacking problem fail to support decision making due to this uncertainty. The proposed approach introduces a new methodological approach that combines predictive tools with analytical heuristics, and considers the operations of a medium-size port terminal in Chile as a case study. The situation in which port managers do not control truck arrivals, and in which operations are non-automated is very typical in medium-size ports, especially in nondeveloped economies. Hence, the methodology proposed can be extended to other case studies that face similar complex operations.

The remainder of this paper is organized as follows: In Section 2 there is a literature review of papers regarding the main topics of this research. The proposed DSS for the container stacking operations is described in Section 3. In Section 4 the case study is introduced, and numerical experimentation to evaluate the performance of the proposed approach is provided. Conclusions and recommendations for further research are outlined in Section 5.

## 2. Literature Review

The literature concerning the container stacking problem have been widely reported (see Bazzazi et al., 2009; Nishimura et al., 2009; Park et al., 2011; Gharehgozli et al., 2014; Ries et al., 2014; Sharma and Singhal, 2014; Goerigk et al., 2016; Lim and Xu, 2006; Guerra-Olivares et al., 2017; G¨uven and T¨ursel Eliiyi, 2018, among others). Some of the approaches have considered a hierarchical framework in which decision making is divided into two stages. The first stage considers an aggregated approach on assigning containers to blocks, while the second stage relates to the real-time decisions on the exact locations of containers (Chen and Lu, 2012; Park et al., 2011; Zhang et al., 2003). A review on storage yard operations in container terminals can be found in Carlo et al. (2014).

Several authors have contributed to the design and implementation of DSS to address diferent decision problems related to container handling operations. Legato and Mazza (2018) provide a classification of DSS for container handling operations in the literature, diferentiating the integrative and specific problem-oriented approaches. Furthermore, for a general overview of the main contributions in this matter, the reader can refer to Mar-Ortiz et al. (2018).

One of the earliest contributions in DSS for container handling operations was presented by Van Hee and Wijbrands (1988). More recently, Murty et al. (2005) proposed an integrated DSS for daily operations of a container terminal, addressing the allocation of storage space to the yard. Liu et al. (2010) propose an integrated DSS that includes six modules but none address specifically container stacking decisions. For transshipment operations, Legato and Mazza (2018) propose a DSS with an integrated perspective of the operations that occur across the quayside, transfer and yard areas.

Other planning decision problems such as real-time transportation planning have been addressed by Van Riessen et al. (2016), Bandeira et al. (2009), and Shen and Khoong (1995). For ship planning decisions, authors have been focused on problems such as crane scheduling (Wan, 2004), the berth allocation problem (Wang and Lim, 2007), and the integrated problem known as the BACAP (Ursavas, 2014).

Although dwell time is a key performance indicator in port terminals, the task of dwell time prediction has not been addressed extensively in the scientific literature. Moini et al. (2012) is one of the few studies that analyzed the factors that afect dwell times, and used analytics techniques for dwell time prediction, such as na¨ıve Bayes and CART decision trees. Ports in the United States were analyzed. Some of the factors that were identified as relevant were the type of port, geographical location, container trafic patterns, container content, and customs services, among others. Kourounioti et al. (2016) used regression models and neural networks for dwell time prediction in order to identify the significant factors.

An early version of this study was published as a conference proceeding in Gaete et al. (2017). The work aims at predicting dwell times using a multi-class classification approach. This idea, however, led to very large predictive errors since the exact number of days was estimated. A simulation approach was used as the stacking strategy, which was also diferent from the mathematical programming and heuristic strategies suggested in this study.

To the best of our knowledge, the only Decision Support Systems proposed in the literature that consider the container stacking problems are Murty et al. (2005), Liu et al. (2010), and Legato and Mazza (2018). However, none of these studies incorporated predictive analytics techniques as inputs for the optimization models, nor considered container dwell times for solving the container stacking problem. These components of our proposal are therefore our main contributions.

Our proposed approach incorporates elements that have been shown to be efective at reducing rehandles. For example, Dekker et al. (2006) found that a stacking policy based on categories reduces the number of rehandles. Along the same line, Borgman et al. (2010) suggest that rehandling movements can be reduced if containers are classified according to the expected departure times, and stacked so that containers that will depart sooner are located at the top.

The novelty of our proposal resides in the fact that container terminals can make use of historical data for designing efective stacking rules. The minimization of rehandles leads to a reduction in operational costs, and also improves the service levels for the external users of the port.

## 3. Proposed Decision Support System for Container Stacking

The proposed DSS is intended to solve an operational level decision problem, as a module of the corresponding Terminal Operating System (TOS) of the container terminal. The architecture of the proposed DSS is presented in Figure 1. This DSS includes two modules for solving the inbound container stacking problem (import containers). The first module includes a model that predicts the container dwell times using traditional and advanced analytics techniques. This model requires information regarding the vessel and the containers to be retrieved at the port. This information is used to predict container dwell times at the beginning of the shift, which can be done in seconds with the analytic model.

The second module takes into account state information about the vessel, the berths and the yard to assign containers to a block using a mathematical model that minimizes travelling distances from the corresponding berth to the block. Then, the exact location within the assigned block is determined based on a heuristic approach that takes the predicted dwell time into account. Notice that both the model for block selection and the stacking heuristic are very fast computationally.

Some assumptions have been made for utilizing the proposed DSS. First, it is assumed that the areas for stacking import and export containers are separated, which is a common practice in container terminals. We also assume that it is not possible to know the sequence of container retrievals in advance. In the case of inbound containers, the retrieval sequence depends on the container dispatching schedule. If an appointment system has not been implemented at the port, which is very common at small and mediumsized ports in emerging countries, then the dispatching sequence depends on the consignee logistics.

![](/api/attachments/FZDUX9V8/fulltext/images/3af82fb847743df183412135bc64048d797f25a9a9c248ae9bbd6beeec7d00c3.jpg)  
Figure 1: Proposed DSS Architecture for Container Stacking.

## 3.1. Dwell Time Prediction

Dwell time prediction is performed by following the KDD process (Knowledge Discovery in Databases) proposed by Fayyad et al. (1996). The KDD process has the following steps: data selection, preprocessing, transformation, data mining, evaluation, and knowledge extraction. A dataset of historical container movements at the TPA was available from year 2016, and used to fit three well-known predictive models: multiple linear regression, decision trees, and random forest. A container is labeled into various categories according to its expected dwell time using data binning. The thresholds for these bins can be defined according to data-driven arguments (for example, using percentiles), or expert criteria related to the functioning of the port.

For predicting dwell times, we recommend using random forests (Breiman, 2001) among other approaches. Random forest has several virtues, including superior predictive performance due to its ability to capture non-linear patterns, eficient model construction, and robustness in the presence of noise (Baesens, 2014; Fern´andez-Delgado et al., 2014). However, no single model is always able to achieve the best performance, and an empirical comparison of various approaches is therefore recommended. The following predictive models are used in our analysis:

1. Multiple linear regression: This well-known technique estimates the target variable as a weighted sum of the covariates and their coeficients, which are usually obtained using Ordinary Least Squares (OLS) (Baesens, 2014).

2. Decision trees: Decision trees are popular classification and regression methods that split the training set using if-then rules in a recursive manner (Baesens, 2014). This strategy is particularly useful when most covariates are nominal variables.

3. Random forest: This method consists of an ensemble of multiple decision trees, which are constructed via bootstrapping (Baesens, 2014; Breiman, 2001).

The performance measures used for a comparative analysis are the mean absolute percentage error (MAPE) and balanced accuracy (BA). The first metric is used to assess regression models, and represents the average percentage error between the predicted labels $\hat { y }$ and the real values y, i.e. $\begin{array} { r } { M A P E = \sum _ { i = 1 } ^ { N } \frac { 1 0 0 } { N } | \frac { y _ { i } - \hat { y _ { i } } } { y _ { i } } | } \end{array}$ Balanced accuracy, by contrast, is designed to evaluate the performance of multiclass classification problems, and computes the average recall for all classes. The recall for class k is defined as the number of correct class k matches divided by the total number of actual class k cases (Sokolova et al., 2006).

## 3.2. Container Stacking

The second module for the proposed DSS consists of locating containers in the yard in order to minimize rehandles. This is performed via two steps, following an approach introduced by Chen and Lu (2012) and Zhang et al. (2003): First, we have the block container assignment. In this case, containers are assigned to a block in the yard. Then, we implement diferent stacking strategies to define the location of containers within the block, based on a heuristic algorithm.

## 3.2.1. Storage Assignment Problem

This step involves the assignment of containers to a block in the yard, considering a single period planning horizon. A mathematical programming approach is proposed, taking some elements from the models proposed by Chen and Lu (2012) and Zhang et al. (2003) into consideration. The main diference with respect to Zhang et al. (2003) is that while they assign block positions to both outbound and inbound containers at the yard, in our model, outbound and inbound containers are located in diferent areas and do not share yard equipment, so they can be treated independently. In Chen and Lu (2012), their model includes both minimizing travel distances and balancing the workload content of the bays. In our case, the balancing workload aspects are included in the stacking strategies which is the reason we only consider traveling distances as criteria to optimize.

The mathematical model used in this step is formalized in Appendix A. Notice that this model is not our main contribution since the predicted dwell times are not used in the storage assignment problem; rather we focus on the container stacking problem, which is solved for each block, and has a greater impact in the operational costs caused by container rehandles. Our proposals are formalized below.

## 3.2.2. Container Stacking Problem

Once the block in which the container will be stacked is determined, the location coordinates must be defined. For this, three diferent heuristics are formalized: (1) Sequential Stacking based on Nominal Prediction (Nom.Pred); (2) Stacking based on Nominal and Numerical Prediction (Nom/ Num Pred.); and (3) Stacking based on Numerical Prediction (Num.Pred). But first, some important concepts are introduced.

Containers are arranged within each block using the three-dimensional coordinate system known as BaRoTi (Bay, Row or Stack, and Tier). The sequence in which containers are stacked can follow a horizontal or a vertical scheme depending on the policy that the port terminal managers employ, and the available yard equipment. In the horizontal scheme, containers are placed tier by tier. Once the whole tier is filled, the next containers are placed in the corresponding bay-rows of the next tier. On the other hand, if a vertical strategy is employed, containers are filled row by row (or stack by stack). In this case, containers are stacked in an available bay-tier until the whole stack is filled. The yard equipment restricts which strategy can be employed. When using Rubber Tyred Gantry (RTG) cranes, it is possible to place containers following both a horizontal and a vertical strategy. However, if reachstackers or top-lifter vehicles are employed, only a vertical strategy can be used since the vehicles have access to only the immediate positions in the block, not to all of them. Figure 2 illustrates the diferences between these two stacking schemes, where containers are labeled with numbers in an increasing order, representing the unloading sequence from a vessel.

![](/api/attachments/FZDUX9V8/fulltext/images/ecc8eaa9f477dec4c0c9ecec498e1f79078f09f89157487f647772bea82a0aa5.jpg)  
Figure 2: Horizontal/Vertical Stacking Schemes

Another characteristic of container stacking algorithms is how the predicted container dwell times are used to support stacking decisions. In this regard, we can consider the numerical value of the predicted dwell times as a rule for locating a container above another already stacked, or in turn, containers can be classified into categories according to this value using data binning. In both cases, containers are stacked in such a way that those with longer predicted dwell times are located under those with lower values. When dwell times are binned into categories, we propose a threeclass scheme: short, medium, and long predicted dwell time. These two dwell times, while lighter ones show the opposite.

![](/api/attachments/FZDUX9V8/fulltext/images/59cb42fab2a4c3c8b5ab86d184b185a1bbac9d0623454eecec7faf23b597c4af.jpg)  
Figure 3: Dwell Time Prediction Schemes

The proposed stacking strategies can be used considering either a horizontal or vertical stacking approach. Here we describe the heuristics considering only a horizontal scheme, while the vertical case can be derived straightforwardly by using a [tier, bay, row] scheme in the stacking process, instead of the [bay, row, tier] scheme discussed in the algorithms.

Prior to describing the stacking strategies, the models and algorithms require defining the following sets, parameters, and variables presented in Tables 1, 2 and 3, respectively.

The last variable also depends on the vessel $\begin{array} { r l r } { v } & { { } \in } & { V } \end{array}$ from which the container was unloaded, and is computed as:

$$
T _ {c, v} ^ {*} = D T _ {c} + T _ {v}\tag{1}
$$

Table 2: Parameters

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\boxed{b\in \{1,\dots ,B\} \quad :\quad \text{Blocks at the yard.}$ $v\in \{1,\dots ,V\} \quad :\quad \text{Vessels arriving at the port.}$ $i\in \{1,\dots ,I\} \quad :\quad \text{Predicted dwell time classes.}$ $t\in \{1,\dots ,T\} \quad :\quad \text{Time periods.}$
</div>

## Table 1: Sets

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$T_{v}$  : Arrival time for vessel  $v \in V$ .
 $C_{v}$  : Set of containers to be unloaded from vessel  $v \in V$ .
 $DT_{c}$  : Predicted dwell time for container  $c \in C_{v}$ .
 $C_{v,b}$  : Number of containers from vessel v assigned to block  $b \in B$ .
 $C_{v,b,i}$  : Number of containers in  $C_{v,b}$  that belongs to dwell time class  $i \in I$ .
 $C_{b}$  : Number of containers stacked at block b at the beginning of the planning horizon.
 $Ntier_{b}$  : Number of tiers belonging to block  $b \in B$ .
 $Nrow_{b}$  : Number of rows belonging to block  $b \in B$ .
 $Nbay_{b}$  : Number of bays belonging to block  $b \in B$ .
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$C_{b,t}$ : Set of containers stacked at block $b$ in period $t$.  
$C_{b,t}^{*}$ : Set of available stacking slots at block $b$ in period $t$.  
$bay_c$ : Bay to locate container $c \in C_{b,t}$.  
$row_c$ : Row to locate container $c \in C_{b,t}$.  
$tier_c$ : Tier to locate container $c \in C_{b,t}$.  
$r_c$ : Number of rehandles needed to retrieve container $c \in C_{b,t}$.  
$T_{c,v}^{*}$ : Estimated retrieval time for container $c \in C_{b,t}$ from vessel $v$.
</div>

Table 3: Variables

The performance of the proposed and alternative container stacking strategies is evaluated using the number of rehandles given by:

$$
R e h a n d l e s = \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {| B |} \sum_ {c \in C _ {b, t}} r _ {c}\tag{2}
$$

The three proposals are formalized below. These strategies use the mathematical programming model presented in Appendix A for assigning contain ers to blocks optimally, and then the containers are arranged in the block based on their predicted dwell times. The reasoning behind these approaches is simple: we avoid blocking containers that have short expected dwell times with containers that have longer expected dwell times. The stacking process ends when all the containers have been unloaded from the vessel and stored in their assigned blocks. These three methods difer to each other with respect to the way containers from the same class are rearranged:

• Sequential Stacking based on Nominal Prediction (Nom. Pred.): Stacking is performed sequentially based on the binned values of the predicted dwell times. Containers from class $i \in I ,$ the one with the longest predicted dwell times, are stacked first, followed by containers of class $i \mathrm { ~ - ~ } 1 \in I$ , and so on until class 1. For the horizontal case, containers are located tier by tier from the first empty position of the block, as illustrated in Figure 3a for a three-class example. The pseudo-code for this strategy is presented in Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: B,  $C_{v}$ 
Identify  $C_{v,b}$  from  $C_{v}$  for all  $b \in B$ ;
for b in B do
    Identify  $C_{v,b,i}$  from  $C_{v,b}$  for  $i \in \{1, 2, 3\}$ ;
    for  $i \leftarrow 3$  to 1 do
    | b ← Sequential Stacking( $C_{b,v,i}$ , b);
    end
    b ← UpdateVolume(b);
end
Output: B
Algorithm 1: Sequential Stacking based on Nominal Prediction
</div>

• Stacking based on Nominal and Numerical Prediction (Nom/ Num. Pred.): This strategy is a slight variation on the previous stacking model, whose idea is to use the numerical prediction to arrange the containers within each class instead of using the sequential approach. For each class, containers are then sorted from those with longest to shortest predicted dwell time and stacked following this sequence. This strategy can be observed in Figure 3b for a three-class example.

• Stacking based on Numerical Prediction (Num. Pred): In contrast with the previous heuristics, this strategy does not use the predicted classes, but stacks containers using solely the numerical prediction. Container c has been unloaded from the vessel in period t. The best location in the corresponding block for stacking the container is defined by determining whether any positions are available on the first tier. If so, the container is located in the first available position found. If not, we compute the range of periods of time between the predicted dwell times of container c and container $c ^ { * }$ as $D T r a n g e _ { c , c ^ { * } }$ Then, we have:

$$
D T r a n g e _ {c, c ^ {*}} = D T _ {c} - D T _ {c ^ {*}}\tag{3}
$$

As t corresponds to the period in which container c has been unloaded and needs to be stacked, dwell time of container $c ^ { * }$ has to be updated from the moment it was stacked to reflect the expected remaining time in period t. If $D T r a n g e _ { c , c ^ { * } }$ is positive or zero for one or more $c ^ { \ast } \in C _ { b , t } ^ { \ast } ,$ container c will be stacked on top of container $c ^ { * }$ . Otherwise, container c will be stacked on container $c ^ { * }$ with the minimum negative value of $D T r a n g e _ { c , c ^ { * } }$ . The pseudo-code for this strategy is presented in Algorithm 2, including the function GetPosition $( b , c )$ , which consists of determining the best position in which to stack container c in block b at period t.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: B,  $C_{v}$ 
Identify  $C_{v,b}$  from  $C_{v}$  for all  $b \in B$ ;
for b in B do
    for c in  $C_{b,v}$  do
    bay, row, tier = GetPosition(b, c);
    Locate c in  $[bay_{c}, row_{c}, tier_{c}]$  position of b;
    end
    b ← UpdateVolume(b);
end

Output: B

GetPosition(b, c) function
Input: b, c
if available positions on floor then
    bay, row, tier = First empty position on floor;
end
else
    $DT_{c} = Predicted\ dwell\ time\ of\ c;$ 
    for  $c^{*} \in C_{b,t}^{*}$  do
    $DT_{c*}^{*} = Predicted\ dwell\ time\ of\ c^{*}\ updated\ at\ period\ t;$ $DTrange_{c,c*} = DT_{c*} - DT_{c}^{*};$ 
    end
    if  $max(DTrange_{c,c*}) &gt; 0$  then
    bay, row, tier = Locate container c on top of container
    $c^{*} \in C_{b,t}^{*}$  satisfying argmax( $DTrange_{c,c*}$ );
    end
    else
    bay, row, tier = Locate container c on top of container
    $c^{*} \in C_{b,t}^{*}$  satisfying argmin( $DTrange_{c,c*}$ );
    end
end

Output: bay, row, tier
Algorithm 2: Stacking based on Numerical Prediction
</div>

## 4. Experimental Results

In this section we evaluate the performance of the proposed DSS in comparison with well-known stacking heuristics that do not use dwell time

# ACCEPTED MANUSCRIPT

predictions. Several stacking algorithms have been reported in the literature, but they usually assume that dwell times are known in advance, or, at least, that the container terminal has partial information about the expected dwell times. This is usually true for export containers in developed countries (Gharehgozli et al., 2014; Ries et al., 2014; Guerra-Olivares et al., 2017; G¨uven and T¨ursel Eliiyi, 2018). In our case study, however, the container terminal does not have this information, and has not implemented any type of Truck Appointment System. Therefore, the proposed DSS is suitable for their current operational conditions, which are unlike those in the existing literature. This situation is common in medium-size container terminals in developing countries.

The aim of the analysis is to evaluate the quality of the solutions obtained, and confirm that using dwell time predictions in the DSS provides better results. As we propose three diferent stacking algorithms that can be implemented following either a vertical or horizontal strategy, the results of the analysis can also be used for stacking policy recommendations, which is a tactical level decision problem. This decision, however, will also be restricted by the yard equipment and limitations of the container terminal.

## 4.1. Case Study and Dataset Description

The TPA is located Arica, in northern Chile, and is considered to be among the most active ports in the country due to its geographical location. It serves as the main gate for Bolivian cargo: in 2017, the port handled 3,157,032 tonnes, of which 79% corresponded to in-transit cargo from Bolivia. Due to the Friendship Treaty of 1904 established between Chile and Bolivia, there are important advantages for Bolivian cargo, including freeof-charge storage for one year for import containers, and three months for export containers. This fact causes great uncertainty on the dispatching sequence, long container dwell times, and long truck turnaround times. All of this is aggravated by the lack of coordination systems. The yearly average dwell time on average is 11.27 days.

The current stacking policy of the TPA corresponds to semi-random assignment, in which all the import containers are stacked together when they are unloaded from the vessels, with the only goal being eficient utilization of the storage space. Since reachstackers are used, they can use only the vertical stacking strategy because their equipment does not have access to the entire block. This strategy causes a large number of rehandles when containers are retrieved to be dispatched, leading to large operational costs, truck congestion, and long truck turnaround times. The proposed approach is motivated by the need to improve this situation, and we expect that its implementation can have a large positive impact on the TPA.

The dataset used to perform dwell time prediction contains 23,167 samples of import containers between 2015 and 2016. After filtering out missing values and inconsistencies, 21,591 observations remained. The following variables were available as covariates:

• Container type: Type of container representing characteristics of size and height.

• Dispatching type: The dispatching procedure is categorized based on whether custom clearance procedures are fulfilled. If the procedure has been done prior to the arrival of the cargo, then this is classified as a direct dispatch. Otherwise, it is considered to be an indirect dispatch.

• Status: If the container is full or empty.

• Weight: Numerical variable representing the weight in kilograms of a container.

• Dispatch consignee: Categorical variable representing the consignee of the cargo.

• Month: Categorical variable representing the month in which a container arrives at a port terminal. The idea of including this variable is to analyze possible seasonal patterns.

• Port of origin: Categorical variable representing the origin port of the cargo.

Regarding data transformation, categorical variables such as Dispatch Consignee, Container Type, and Port of Origin were aggregated to reduce the number of levels by creating a category called others that includes the less represented levels in the respective variable. Subsequently, these variables were transformed into numerical covariates using dummy coding. Table 4 summarizes the information related to the variables and their corresponding levels.

<table><tr><td>Variable</td><td>Type</td><td>Categories</td></tr><tr><td>Container Type</td><td>Categorical</td><td>20GP, 40HC, 40GP, Others</td></tr><tr><td>Dispatch Type</td><td>Categorical</td><td>Direct, Indirect</td></tr><tr><td>Status</td><td>Categorical</td><td>Full, Empty</td></tr><tr><td>Weight</td><td>Numerical</td><td>-</td></tr><tr><td>Consignee</td><td>Categorical</td><td>Mediterranean Shipping Co., Ian Taylor Chile, Ultramar Agencia Marítima Ltda., Others</td></tr><tr><td>Month</td><td>Categorical</td><td>{Jan···Dec}</td></tr><tr><td>Port of Origin</td><td>Categorical</td><td>Callao, Shangai, Guayaquil, Qingdao, Tianjin, Buenaventura, Ningbo, Balboa, Others</td></tr></table>

Table 4: Container Descriptive Variables after Preprocessing

## 4.2. Results for the Dwell Time Prediction Step

Various experiments were performed to test the performance of the different predictive analytics models. The predicted dwell time was binned in three classes, which were defined based on the mean and standard deviation of the target variable, as well as on the requirements of the port terminal managers, who suggested that three is an adequate number of classes that would not afect the current operations strongly. The three classes are defined as follows:

• C1 : Less than one week

• C2 : Between one and two weeks

## • C3 : More than two weeks

Model selection was performed using 10-fold cross-validation for the predictive methods with the default settings of the CARET package in R. The pruning parameters were tuned for the CART model, while the number of trees and variables selected were tuned for the random forest method. A total of 20,000 samples were used for training and validation, while 1,591 observations were used for testing (the last month of our study).

The results obtained for the three predictive methods using both the MAPE and Balanced Accuracy metrics are summarized in Table 5.

<table><tr><td>Model</td><td>MAPE(%)</td><td>C1</td><td>C2</td><td>C3</td><td>BA</td></tr><tr><td>Multiple Linear Regression</td><td>44.5</td><td>0.61</td><td>0.54</td><td>0.67</td><td>0.61</td></tr><tr><td>Decision Trees</td><td>40.1</td><td>0.61</td><td>0.55</td><td>0.70</td><td>0.62</td></tr><tr><td>Random Forest</td><td>38.7</td><td>0.61</td><td>0.54</td><td>0.68</td><td>0.61</td></tr></table>

Table 5: MAPE and Balanced Accuracy Performance Measures for Analytics Algorithms

It can be observed in Table 5 that random forest achieves the best performance, showing the lowest numerical error when MAPE is used. After binning the prediction, the three methods achieved very similar performances, with a balanced accuracy ranging between 0.61 and 0.62. We chose random forest as the best alternative because it achieves the lowest MAPE, and has also proved to be one of the most efective predictive methods reported in the literature. For example, the study by Fern´andez-Delgado et al. (2014) performed a comprehensive comparison among several machine learning methods and, in it, random forest achieved the best average performance among 179 methods using 121 diferent datasets. In our experiments, a total of 2,000 trees was used, each one having three variables selected randomly.

## 4.3. Results for the Container Stacking Problem

Once the dwell time values have been predicted and grouped into three classes, the second module of the DSS aims to assign containers to blocks and specific locations. In order to assess the performance of the proposed

# ACCEPTED MANUSCRIPT

DSS, we carried out a set of simulated experiments. For these simulations, our goal is reproducing the current practices and layouts of the TPA. In particular, the current information on container arrivals and retrievals is used. The experimental design follows:

• The time lapse T for the simulations corresponds to 500 hours, which is approximately one month of operations (assuming 20 working days). In this period, 1,591 containers were handled on average.

• The current layout of the port has 209 bays distributed into 19 blocks, with a total of 3760 slots (TEUs) at the yard for inbound containers. Given that some blocks are used for 20 and 40 foot containers, a total of 2,578 slots is considered as the actual stacking capacity.

• Six berths are available at the TPA for the arrival of vessels.

• According to the dataset, 16 vessels arrived during T .

• It is assumed that the yard is operated with RTG yard cranes. We also assume that the yard equipment is always available to perform the required movement of containers.

• The maximum percentage of occupancy for each bay is set at 70%, which is the current practice in the port in case of high congestion.

• The maximum number of bays assigned to each berth is unrestricted, representing the real situation of the Port Terminal of Arica (209 bays).

• The distance matrix between each bay and the berths is computed following the configuration of the TPA yard layout.

• The capacity of each bay is defined based on the real data of the port. The static capacity of the yard is 3,760 slots for inbound containers.

• One hundred replications were performed for each demand scenario for computing its performance.

• Two demand scenarios were constructed: the average scenario, which consists of the expected case based on the actual data, and a stressed scenario that reflects the peak periods. For the average scenario, the arrival of 250 containers in T is considered, with an initial condition of 500 containers stacked in the yard. On the other hand, the stressed scenario is based on the arrival of 500 containers in T , with an initial condition of 1,000 containers stacked in the yard. This scenario was defined with the assumption that the port operates with approximately 70% of utilization of the yard. It is important to notice that a scenario of low demand is not studied since it leads to few rehandles, thus not being useful for benchmarking.

• The random variables in the experiment are related to the vessel/berth in which each container arrives, the sequence for retrieval (based on the real data), and the dwell times. The “real” and predicted dwell times were simulated as two normally-distributed variables with averages, standard deviations, and bivariate correlation given by the relation between the real dwell times and the output of the random forest model.

The simulation was implemented during the horizon planning of one month, that consisted of 20 working days translated into 500 hours as indicated. In order to account for the transient period of the simulation, another month of data was generated, and the performance metric is computed for this second month of the simulation. The performance metric consists on the rehandles incurred when the diferent container stacking strategies are employed. The strategies that use the dwell time as an input variable receive the predicted dwell times and used that information to locate the containers. When the containers are retrieved according to their actual dwell times, the number of rehandles is calculated. It is assumed that the port terminal operates with RTG cranes in the yard. Containers that were blocking the one to be retrieved are relocated in such a way that the original configuration is respected.

For comparison purposes, we implemented two alternative approaches, having a total number of five modeling methods for each of the two scenarios and the two stacking approaches (Horizontal or Vertical, H or V). For the first algorithm, Sequential Stacking - Random Block (Seq. R.B.), containers are stacked in a semi-random fashion. The block is selected randomly, and containers are stacked sequentially in the block until its maximum capacity it is reached. For the second algorithm, Sequential Stacking - Optimal Block, containers are also stacked sequentially, but the block is selected considering the proposed mathematical model defined in Section 3.2.1. The sequential stacking procedure consists of searching for the first empty slot in a block b, and locating a group of containers $C _ { v , b }$ sequentially until all the containers are stored or the maximum capacity of the block is reached.

The performance for the ten stacking strategies in terms of total number of rehandles is presented in figures 4 and 5 for the average and stressed scenario, respectively. Each figure presents the distribution of the total number of rehandles in the form of a box plot.

Several conclusions can be drawn from the results presented in figures 4 and 5:

• Important diferences can be observed between the vertical and horizontal strategies: The latter strategies clearly perform better for all scenarios. However, one limitation of the horizontal strategies is that they require RTG equipment to access the containers in the whole block; those port terminals operating with reachstackers cannot implement these strategies.

• The three proposed strategies also perform undoubtedly better than the alternative methods that do not predict dwell times for all scenarios. Hence, we can conclude that the proposed approach is suitable to be implemented using the more suitable stacking strategy (vertical or horizontal) for the port terminal. In the particular case of the Port of Arica, we would recommend to consider the vertical strategy using the numerical prediction. This is because the terminal operates with

![](/api/attachments/FZDUX9V8/fulltext/images/46e716f43e3d0fb68b12e594256a1e8ab8b23363eb7f83cf96c63c99eae9f4ed.jpg)  
Figure 4: Performance in Terms of Total Rehandles for the Various Stacking Strategies. Average Scenario.

• Although the diferences between the three proposals are relatively small, the stacking strategy based on numerical prediction performs best for both scenarios using the vertical strategy. In the case of the horizontal strategy, this method performs better only for the average scenario.

• We can also observe from the results that the stressed scenario requires approximately twice as many rehandles in comparison with the average scenario, leading to the conclusion that an eficient stacking strategy is not only able to reduce operational costs by minimizing rehandles, but is also useful to avoid scenarios of high congestion, which lead to an important increase in the total number of rehandles.

![](/api/attachments/FZDUX9V8/fulltext/images/92e9f8cc5c901de3db6832fbdc2b8f112c7f7c585b5d34a9782ff5ff53c23fbc.jpg)  
Figure 5: Performance in Terms of Total Rehandles for the Various Stacking Strategies. Stressed Scenario.

• In terms of practical implementation, the simplest strategy is the stacking based on numerical prediction. This is because a container is stacked directly when it is unloaded from the vessel, without any concern about the type of class it belongs to. With the exception of a stressed scenario and a vertical strategy, this is the container stacking method that performs better in terms of rehandles.

• The stacking approach based on nominal and numerical predictions (Nom/Num. Pred) is the most complex strategy to be implemented because it not only requires segregating containers into classes, but also determining a sequence for them according to their numerical dwell times. This is based on the assumption that the port terminal has enough space at the yard for the sequencing of the containers that are unloaded from the vessel.

## 5. Conclusions and Future work

In this paper, a DSS for container stacking is proposed. The reasoning behind our proposal is to make use of the information of past dwell times to develop novel stacking strategies based on predicted dwell times. The prediction is done using the well-known random forest method, which has been proven to be very efective in both classification and regression tasks. Based on this input, strategies for container stacking within blocks are developed for both vertical and horizontal stacking, while containers are assigned to blocks in the yard using a variation of the models proposed by Chen and Lu (2012) and Zhang et al. (2003).

Three stacking strategies are proposed, difering in the way the predictive dwell times are used: either nominal or numerical. Random forest provides a numerical prediction which can be used directly for ranking containers according to their expected dwell times. This prediction can be binned into categories, simplifying the stacking rules. A third category was also presented by combining the nominal and numerical predictions.

This research was inspired by the current practices and needs of the Port Terminal of Arica (TPA) in Chile. This port terminal faces high levels of uncertainty in the dispatching of import containers, along with large dwell times due to a political agreement establishing special conditions for the in-transit cargo of Bolivia, which represents more than 70% of the total volume. Hence, current practices for handling import containers consider a semi-random strategy since there are no criteria for segregating cargo at the yard. This causes a large number of rehandles when containers are retrieved.

Based on data provided by the TPA, we assessed the diferent container stacking strategies proposed, comparing them with simple stacking strategies that represent the current practices in the port. Results demonstrated the virtues of the proposal, which outperformed the strategies that ignore

# ACCEPTED MANUSCRIPT

this information for two demand scenarios and two stacking options (horizontal and vertical). We conclude that for average scenarios, the best strategy corresponds to the stacking policy with numerical prediction, which also corresponds to the simplest strategy in terms of its implementation. For stressed scenarios, stacking based on nominal predictions yields the best results.

Another important conclusion is that horizontal stacking outperformed the vertical stacking strategy. Although the limitation of horizontal strategies is that they require RTG cranes for the container handling to access the entire block, purchasing them may be worth the investment since their use leads to important reductions in the operational costs.

As further research, we propose optimizing the number and size of container categories obtained in the binning process of the dwell time prediction. For the TPA case study, three classes were defined arbitrarily based on the average dwell times and the suggestions made by our counterpart, and this information was assumed as a fixed parameter in the stacking heuristics. We also propose extending the proposed DSS to incorporate other decision variables, such as the number of yard cranes to be employed. Further extensions include the design of a Truck Appointment System that uses the predicted dwell times to define gate capacity and resource assignment (yard cranes and vehicles for the horizontal transport of containers). Finally, other storage policies and their related planning problems can be addressed by a dwelltime prediction approach, such as the pre-marshalling of containers or the block relocation problem. For these cases, retrieval times could be predicted using analytic techniques, and become an input for solution methodologies of such planning decisions.

## Appendix A. Storage Location Assignment Model

This sub-stage considers the assignment of containers to a block at the yard, using a single period planning horizon. A mathematical model is proposed, extending the models proposed by Chen and Lu (2012) and Zhang et al. (2003). The model minimizes the distance between the berth, the place where containers are unloaded from the vessel, and the block position in the yard. The model assumes that the berth at which the vessel is moored is known, as well as the unloading sequence of containers, and the total number of containers to be unloaded. We also assume that the containers are of the same type. Furthermore, it is considered that a number of bays of each block have been previously allocated for the containers of each vessel. Since we are interested in the block assignment, we assume that bays of the same block are of equal distance to the berths (at the center of the block).

The sets, parameters and variables of the mathematical model are presented in presented in Tables A.1, A.2 and A.3, respectively:

![](/api/attachments/FZDUX9V8/fulltext/images/2f9f0fadf42595dd555aa9e806d0624975f847745d7bf9d79c27760dac5325fa.jpg)  
Table A.2: Parameters

<table><tr><td> $\delta_{i,j}$ </td><td>: Binary variable: 1 if bay i is assigned to vessel at berth j; 0 otherwise.</td></tr><tr><td> $x_{i,j}$ </td><td>: Number of containers assigned to bay i which are unloaded from vessel at berth j.</td></tr><tr><td> $V_i$ </td><td>: Number of containers in bay i at the end of the planning horizon.</td></tr></table>

Table A.3: Variables

The space allocation problem can be formulated as follows:

• Objective Function

$$
M i n \sum_ {i = 1} ^ {B} \sum_ {j = 1} ^ {S} d _ {i, j} x _ {i, j}\tag{A.1}
$$

Subject to:

• Constraints:

$$
\sum_ {i = 1} ^ {B _ {j}} x _ {i, j} = n _ {j}\tag{∀j}
$$

$$
x _ {i, j} \leq \delta_ {i, j} n _ {j}\tag{A.2}
$$

$$
\forall i, j\tag{A.3}
$$

$$
V _ {i} \leq C _ {i} \gamma\tag{∀i}
$$

(A.4)

$$
V _ {i} = V _ {i} ^ {0} + \sum_ {j = 1} ^ {S} x _ {i, j}\tag{∀i}
$$

(A.5)

$$
\sum_ {i} \delta_ {i, j} \leq B _ {j}\tag{∀j}
$$

$$
x _ {i, j}, V _ {i} \in \mathbb {Z} ^ {+}\tag{A.6}
$$

$$
\forall i, j\tag{A.7}
$$

$$
\delta_ {i, j} \in \{0, 1 \}\tag{∀i, j}
$$

(A.8)

The objective function minimizes the sum of distances between the berths and the bays (of the corresponding blocks). The set of constraints (2) guarantees that all the containers are assigned to a bay in the yard. Constraints (3) avoid locating containers in unassigned bays. Constraints (4) limit the usage of bays to a predefined maximum γ. Constraints (5) compute the number of containers assigned to each bay during the planning horizon. Finally, constraints (6) guarantee that the number of bays assigned to a vessel does not exceed the maximum number of bays defined by the operating policies of the port.

## Acknowledgements

The first author was supported by FONDECYT project 1160738. This research was partially funded by the Complex Engineering Systems Institute, ISCI (ICM-FIC: P05-004-F, CONICYT: FB0816).

## References

Baesens, B., 2014. Analytics in a Big Data World. John Wiley and Sons.

Bandeira, D. L., Becker, J. L., Borenstein, D., 2009. A dss for integrated distribution of empty and full containers. Decision Support Systems 47 (4), 383–397.

Bazzazi, M., Safaei, N., Javadian, N., 2009. A genetic algorithm to solve the storage space allocation problem in a container terminal. Computers & Industrial Engineering 56 (1), 44–52.

Borgman, B., van Asperen, E., Dekker, R., 2010. Online rules for container stacking. OR spectrum 32 (3), 687–716.

B¨ose, J. W., 2011. General considerations on container terminal planning. In: Handbook of terminal planning. Springer, pp. 3–22.

Breiman, L., 2001. Random forests. Machine learning 45 (1), 5–32.

Carlo, H. J., Vis, I. F., Roodbergen, K. J., 2014. Storage yard operations in container terminals: Literature overview, trends, and research directions. European Journal of Operational Research 235 (2), 412–430.

Chen, L., Lu, Z., 2012. The storage location assignment problem for outbound containers in a maritime terminal. International Journal of Production Economics 135 (1), 73–80.

Dekker, R., Voogd, P., van Asperen, E., 2006. Advanced methods for container stacking. OR spectrum 28 (4), 563–586.

Fayyad, U., Piatetsky-Shapiro, G., Smyth, P., 1996. The kdd process for extracting useful knowledge from volumes of data. Communications of the ACM 39 (11), 27–34.

Fern´andez-Delgado, M., Cernadas, E., Barro, S., Amorim, D., 2014. Do we need hundreds of classifiers to solve real world classification problems? Journal of Machine Learning Research 15, 3133–3181.

Gaete, M., Gonz´alez-Araya, M. C., Gonz´alez-Ram´ırez, R. G., Astudillo, C., 2017. A novel storage space allocation policy for import containers. In: International Conference on Operations Research and Enterprise Systems. Vol. 884. Springer, pp. 293–316.

Gharehgozli, A. H., Yu, Y., de Koster, R., Udding, J. T., 2014. A decisiontree stacking heuristic minimising the expected number of reshufles at a container terminal. International Journal of Production Research 52 (9), 2592–2611.

Goerigk, M., Knust, S., Le, X. T., 2016. Robust storage loading problems with stacking and payload constraints. European Journal of Operational Research 253 (1), 51–67.

Guerra-Olivares, R., Smith, N. R., Gonz´alez-Ram´ırez, R. G., Garc´ıa-Mendoza, E., C´ardenas-Barr´on, L. E., 2017. A heuristic procedure for the outbound container space assignment problem for small and midsize maritime terminals. International Journal of Machine Learning and Cybernetics, 1–14.

G¨uven, C., T¨ursel Eliiyi, D., 2018. Modelling and optimisation of online container stacking with operational constraints. Maritime Policy & Management, 1–16.

Kourounioti, I., Polydoropoulou, A., Tsiklidis, C., 2016. Development of models predicting dwell time of import containers in port container terminals–an artificial neural networks application. Transportation Research Procedia 14, 243–252.

Legato, P., Mazza, R. M., 2018. A decision support system for integrated container handling in a transshipment hub. Decision Support Systems 108, 45–56.

Lim, A., Xu, Z., 2006. A critical-shaking neighborhood search for the yard allocation problem. European Journal of Operational Research 174 (2), 1247–1259.

Liu, Y., Zhou, C., Guo, D., Wang, K., Pang, W., Zhai, Y., 2010. A decision support system using soft computing for modern international container transportation services. Applied Soft Computing 10 (4), 1087–1095.

Mar-Ortiz, J., Gracia, M. D., Castillo-Garc´ıa, N., 2018. Challenges in the design of decision support systems for port and maritime supply chains. In: Exploring Intelligent Decision Support Systems. Springer, pp. 49–71.

Merckx, F., 2005. The issue of dwell time charges to optimize container terminal capacity. In: Proceedings IAME 2005 Annual Conference, Limassol, Cyprus, 23-25 June 2005. pp. CD–ROM.

Moini, N., Boile, M., Theofanis, S., Laventhal, W., 2012. Estimating the determinant factors of container dwell times at seaports. Maritime Economics & Logistics 14 (2), 162–177.

Murty, K. G., Liu, J., Wan, Y.-w., Linn, R., 2005. A decision support system for operations in a container terminal. Decision Support Systems 39 (3), 309–332.

Nishimura, E., Imai, A., Janssens, G. K., Papadimitriou, S., 2009. Container storage and transshipment marine terminals. Transportation Research Part E: Logistics and Transportation Review 45 (5), 771–786.

Park, T., Choe, R., Kim, Y. H., Ryu, K. R., 2011. Dynamic adjustment of container stacking policy in an automated container terminal. International Journal of Production Economics 133 (1), 385–392.

Ries, J., Gonz´alez-Ram´ırez, R. G., Miranda, P., 2014. A fuzzy logic model for the container stacking problem at container terminals. In: International Conference on Computational Logistics. Springer, pp. 93–111.

Sharma, J., Singhal, R. S., 2014. Genetic algorithm and hybrid genetic algorithm for space allocation problems-a review. International Journal of Computer Applications 95 (4).

Shen, W., Khoong, C., 1995. A dss for empty container distribution planning. Decision Support Systems 15 (1), 75–82.

Sokolova, M., Japkowicz, N., Szpakowicz, S., 2006. Beyond accuracy, f-score and roc: A family of discriminant measures for performance evaluation. In: Advances in Artificial Intelligence. Springer, Berlin Heidelberg, pp. 1015–1021.

T´ellez, T. L., 1989. Historia general de la frontera de Chile con Per´u y Bolivia, 1825-1929. Vol. 17. Universidad de Santiago de Chile.

Ursavas, E., 2014. A decision support system for quayside operations in a container terminal. Decision Support Systems 59, 312–324.

Van Hee, K., Wijbrands, R., 1988. Decision support system for container terminal planning. European Journal of Operational Research 34 (3), 262– 272.

Van Riessen, B., Negenborn, R. R., Dekker, R., 2016. Real-time container transport planning with decision trees based on ofline obtained optimal solutions. Decision Support Systems 89, 1–16.

Wan, G., 2004. An intelligent decision support system for crane scheduling in a container terminal. Applied Artificial Intelligence 20.

Wang, F., Lim, A., 2007. A stochastic beam search for the berth allocation problem. Decision support systems 42 (4), 2186–2196.

Zhang, C., Liu, J., Wan, Y.-w., Murty, K. G., Linn, R. J., 2003. Storage space allocation in container terminals. Transportation Research Part B: Methodological 37 (10), 883–903.

Sebastián Maldonado received his B.S. and M.S. degree from the University of Chile, in 2007, and his Ph.D. degree from the University of Chile, in 2011. He is currently Associate Professor at the School of Engineering and Applied Sciences, Universidad de los Andes, Santiago, Chile. His research interests include statistical learning, data mining and business analytics. Sebastián Maldonado has published more than 60 scientific contributions including more than 40 Thomson Reuters’ ISI papers in the last five years.

Rosa G. González-Ramírez is Assistant Professor at the Faculty of Engineering and Applied Sciences, Universidad de Los Andes, Santiago, Chile. She has a PhD degree from Monterrey Tech in Mexico and a M.Sc. in Industrial Engineering from Arizona State University as well as a M.Sc. in Quality and Productivity Systems from Monterrey Tech. Her research interests are related to maritime and port logistics, supply chain management, optimization problems and metaheuristics. She has published several contributions in both scientific journals as well as technical reports. She is currently the coordinator of the Scientific Committee of the Network of Digital and Collaborative Ports in Latin America and the Caribbean promoted by the Economic System of Latin America and the Caribbean (SELA) and the Development Bank CAF.

Francisca Quijada has a bachelor’s degree in Industrial Engineering from the Universidad de Los Andes, Chile. During her studies, she worked as Teaching Assistant of the courses of Data Mining and Logistics. She also worked as Research Assistant under the supervision of Prof. Sebastian Maldonado and Rosa González while developing her thesis on the container stacking problem. She participated in the Business Analytics on Finance and Industry (BAFI) in 2017 and the OPTIMA Conference in 2018.

Adrian Ramirez Nafarrate is Professor in the School of Entrepreneurial and Economical Sciences at Universidad Panamericana in Zapopan, Jalisco, Mexico. He received his Ph.D. in Industrial Engineering from Arizona State University. His research interests include simulation and optimization of manufacturing and service systems. His published research has appeared in peer review journals including Production and Operations Management, European Journal of Operational Research, International Journal of Production Economics and Journal of Business Research. He received the Best Student Paper Award in the 2010 Winter Simulation Conference. He is a member of INFORMS, IISE, Decision Sciences Institute and the Mexican OR Society. He has served in the INFORMS International Activities Committee and he was chair for the International Conference on OR for Development in 2016.

## Highlights

 A novel profit-driven strategy for churn prediction is proposed.

 The proposed framework optimizes profit directly via robust optimization.

 The Minimax Probability Machine is extended to the domain of profit measures.

 Experiments on well-known churn prediction datasets were performed.

 Our proposal archives the largest average profit compared with benchmark methods.
