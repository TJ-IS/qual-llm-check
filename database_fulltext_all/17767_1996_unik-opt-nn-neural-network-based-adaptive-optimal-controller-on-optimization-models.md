---
otero_id: 17767
otero_key: "AP9UDM7T"
title: "UNIK-OPT/NN Neural network based adaptive optimal controller on optimization models"
authors: "Wooju Kim; Jae K. Lee"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00017-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# UNIK-OPT/NN Neural network based adaptive optimal controller on optimization models

Wooju Kim $^{a,*}$ , Jae K. Lee $^{b}$

$^{a}$ Department of Industrial Engineering, Chonbuk National University, Chonju 560-756, South Korea $^{b}$ Department of Management Information Systems, Korea Advanced Institute of Science and Technology, 207-43, Cheongryang, Seoul 130-012, South Korea

## Abstract

When the future information for an optimization model is not complete, the model tends to incorporate such uncertainties as some assumptions on the coefficients. As time passes and more precise information is accumulated, the initial optimal solution may no longer be optimal, or even feasible. At this point, model builders want to modify the assumed and controllable coefficients to obtain the desired values of designated decision variables. To aid this process, a neural network could effectively be applied. So we develop a tool UNIK-OPT/NN which can support the construction and recall of the neural network model on top of the knowledge assisted optimization model formulator UNIK-OPT and the semantic neural network building aid UNIK-NEURO. By adopting a commonly interpretable semantic representation of optimization and neural network models, UNIK-OPT/NN can effectively automate most of the neural network construction and recall procedure for optimal control.

Keywords: Adaptive optimal control; Neural network; Optimization model

## 1. Introduction

Optimization models have been used as one of the major tools for managerial decision modelling. An optimization model determines the values of decision variables for a given model formulation and coefficients. When complete information for the formulation cannot be secured at one time, the initial model is obliged to include some assumptions which may be reflected in some coefficients. As additional information is gradually accumulated after the initial model building, the values of some decision variables may be restricted, which may not be attainable with the initial model. To overcome this situation, we can adjust controllable coefficients which were initially set under a certain assumption. The question is how to adjust the controllable coefficients to obtain the desired values of the restricted decision variables and the initial optimal objective function value as much possible as. Let's call this kind of adjustment “adaptive optimal control”. For this purpose, the mapping between the restricted decision variables and controllable coefficients for the adaptive optimal control is realized by adopting the neural network approach and the performance for the refinery case is empirically validated [9].

This paper deals with the development of a system UNIK-OPT/NN which helps implement adaptive optimal control. Section 2 reviews the process of adaptive optimal control using the neural network. Section 3 illustrates an application with a refinery case. Section 4 describes the system UNIK-OPT/NN with an example for the refinery.

## 2. Adaptive optimal control by neural network

To perform adaptive optimal control, we need to derive a mapping function between designated decision variables and controllable coefficients. To generate such a function, we adopt the approximate functional mapping capability of feedforward neural networks because no analytical method is applicable for this purpose. In the neural network, input nodes correspond to the designated decision variables, whereas output nodes to controllable coefficients. For the literature on the functional approximation capability of neural networks, readers may refer to the papers by Lapedes and Farber [6], Hecht-Nielsen [2], and Girosi and Poggio [1]. Applications of the real-numbered neural network can be found in many other control problem settings [3,5,10]. In this research, the back-propagation algorithm [11] is used to train the feedforward neural network because it is the most popular learning scheme with a variety of applications [12].

The process of performing the adaptive optimal control using the neural network can be summarized as follows [9]:

1. Generate instances of paired values of controllable coefficients and optimized values of designated decision variables from the optimization model.

2. Using the instances, train a neural network model which has the designated decision variables as input nodes and the controllable coefficients as output nodes.

3. Input the desired values of designated decision variables into the neural network to obtain the suggested values of controllable coefficients.

4. To evaluate the performance of neural network based control, the optimization model is modified with the suggested coefficients from the neural network, and the optimal solution is obtained accordingly. By comparing the desired decision values and the realized ones from the optimization model with the modified coefficients, the error of the neural network model can be computed.

This process is graphically depicted as Fig. 1 and is applied to the refinery case in the following section.

## 3. Adaptive optimal control in the refinery

## 3.1. Scheduling in the refinery

The need for adaptive optimal control is invoked while we attempt to develop a daily-basis 30-day scheduling expert system, UNIK-SCHD [7], for a refinery plant. Let us first describe a situation where a study of this type was necessary at a refinery. The refinery plant consists of the following processes as depicted in Fig. 2. On a certain day, a set of crude oils are delivered by a tanker. The delivered crude oils are transferred to storage tanks to be mixed with the old oil leftover in the tanks meeting the required specifications. The mixed crude oils from the selected tanks are then transferred to high sulphur (H/S) or low sulphur (L/S) charge tanks, respectively, to be charged to the Crude Distillation Units (CDUs). Each CDU can distill either high or low sulphur crude oils at a time. The output streams from all CDUs – called intermediate products – may be reformed by the secondary units, and then blended into final products such as diesel and bunker C oils.

Obtain Optimized Pairs  
![](/api/attachments/AP9UDM7T/fulltext/images/4b67b7d62a60927142419a070b5b978b01596c888f7b17504f51c6326727ee76.jpg)  
Fig. 1. Process of the adaptive optimal control using the neural network.

Scheduling the daily operations of the refinery plant requires determining the following facts each day: 1. Mix the crude oils by transferring to storage tanks according to the delivery schedule of tankers.

2. Transfer a certain amount of stored crude oils to either high or low sulphur charge tanks.

3. Determine the levels of distillation, reformation, and blending.

Necessity of adaptive optimal control in this setting is invoked due to the information gap in the daily demands between two time points: 3-months ahead for purchase contract and 1-month ahead for the operation of the plant according to the scheduled crude oil delivery. An earlier purchase contract is necessary because of the long delivery time requirement for crude oils – usually three months from origin to plant. At this point, the exact daily demand is not known. Therefore, we are obliged to schedule based on the average daily demand levels which can be computed from the monthly demand forecast. This implies that the plant is assumed to be operated at the average mixing, distilling, and reforming levels. Under this assumption, the only decision variables left to be optimized is about blending, while the assumed average operational plan is reflected in the coefficient values of the blending LP model.

![](/api/attachments/AP9UDM7T/fulltext/images/844500358be1dc28f2243617aa8396308fd2edf29bbfce968a4fcaf9b7cc2f16.jpg)  
Fig. 2. Operational stages in a refinery plant.

Now, let's shift to the 1-month ahead time point for operational scheduling. At this point, the detailed daily demand for the next 30 days become known. The demanded amounts to be distributed through pipes are quite stable daily. However, severe fluctuations due to shipment by very large vessels are unavoidable. To accommodate such peak demands, the initial production plan should be adjusted to some extent. This can be realized by adjusting the coefficient terms concerning the operational plan in such a way as to meet the daily required production amount which are decision variables in the linear programming models. Such a process is exactly the same as that of the adaptive optimal control. Since this phenomenon observed in the refinery is very common in other process industries as well, the adaptive optimal control should be quite generally applicable.

## 3.2. Adaptive optimal control with blending model

To illustrate adaptive optimal control, let us look at the linear programming model for daily blending under the assumptions of the average operational plan.

## Notations

(1) Decision Variables

$XP_{j}$ : Production amount of final product j.

$X\dot{N}P_{ij}$ : Blending amount of intermediate product i into final product j.

$XRP_{kj}$ : Blending amount of reformed product k into final product j.

$D_{jq}^{+}$ : Over-qualified level of quality property $q$ in final product $j$ .

$D_{jq}^{-}$ : Under-qualified level of quality property $q$ in final product $j$ .

$SP_{jq}$ : Quality specification of property q in final product j.

(2) Coefficients

$sn_{ig}$ : Quality specification of property q in intermediate product i.

$sr_{kq}$ : Quality specification of property q in reformed product k.

$sp_{jq}^{U}$ : Upper limit of quality specification of property $q$ in final product $j$ .

$sp_{jq}^{L}$ : Lower limit of quality specification of property $q$ in final product $j$ .

$\gamma_{jq}$ : Target quality specification of property q in final product j.

$w_{jq}^{+}$ : Penalty weight of over-qualification of property q in final product j.

$w_{jq}^{2}$ : Penalty weight of under-qualification of property q in final product j.

$xn_{i}$ : Amount of intermediate product $i$ which is directly blended into final product without reforming.

$xr_{k}$ : Amount of reformed product k to be blended.

$xp_{i}^{U}$ : Upper limit of production amount of final product j.

$xp_{j}^{L}$ : Lower limit of production amount of final product j.

Subscripts

$i \in \{\text{Intermediate Products}\}$ .

$j \in \{\text{Final Products}\}$ .

$k \in \{\text{Reformed Products}\}$ .

$q \in \{\text{Components}\}$ .

Upper case letters denote decision variables, while lower case letters denote coefficients. Using the above notations, the daily blending optimization model can be formulated as (1)-(10).

Daily blending optimization model

$$
\operatorname{Min} \sum_ {j} \sum_ {q} \left(w _ {j q} ^ {+} D _ {j q} ^ {+} + w _ {j q} ^ {-} D _ {j q} ^ {-}\right),\tag{1}
$$

$$
\sum_ {i} s n _ {i q} X N P _ {i j} + \sum_ {k} s r _ {k q} X R P _ {k j} - \gamma_ {j q} X P _ {j} + D _ {j q} ^ {+} - D _ {j q} ^ {-} = 0 \quad \forall j, q,\tag{2}
$$

$$
\sum_ {i} X N P _ {i j} + \sum_ {k} X R P _ {k j} = X P _ {j} \quad \forall j,\tag{3}
$$

$$
\sum_ {j} X N P _ {i j} = x n _ {i} \quad \forall i,\tag{4}
$$

$$
\sum_ {j} X R P _ {k j} = x r _ {k} \quad \forall k,\tag{5}
$$

$$
X P _ {j} \leq x p _ {j} ^ {U} \quad \forall j,\tag{6}
$$

$$
X P _ {j} \geq x p _ {j} ^ {L} \quad \forall j,\tag{7}
$$

$$
\sum_ {i} s n _ {i q} X N P _ {i j} + \sum_ {k} s r _ {k q} X R P _ {k j} - s p _ {j q} ^ {U} X P _ {j} \leq 0 \quad \forall j, q,\tag{8}
$$

$$
\sum_ {i} s n _ {i q} X N P _ {i j} + \sum_ {k} s r _ {k q} X R P _ {k j} - s p _ {j q} ^ {L} X P _ {j} \geq 0 \quad \forall j, q,\tag{9}
$$

$$
X P _ {j}, X N P _ {i j}, X R P _ {k j}, D _ {j q} ^ {+}, D _ {j q} ^ {-} \geq 0 \quad \forall i, j, k, q.\tag{10}
$$

Statement (1) shows the objective function which tries to minimize the penalty on over- and under-qualification of final products. Statement (2) defines the level of over- and under-qualifications of final product $D_{jq}^{+}$ and $D_{jq}^{-}$ in conjunction with the inflows and outflows to the blending process. Statements (3), (4), and (5) balance the input and output amounts in the subsystems of the refinery plant. Statements (6) and (7) bound the production amount of final products, while statements (8) and (9) bound the quality specification of final products. Non-negativity constraints to the decision variables are shown in statement (10).

Due to the information gap between the 3-months ahead model and the 1-month ahead model, the bounds of production amounts in (6) and (7) become tighter in the 1-month ahead model, which causes the goal in (1) to be degraded or the feasibility lost. To avoid this, we need to adjust some of the controllable coefficients concerning the operational plan represented in $sn_{iq}$ , $sr_{kq}$ , $xn_{i}$ , and $xr_{k}$ . The same logic holds for the quality specifications of final products $SP_{jq}$ , which can be derived by the function in (11).

$$
S P _ {j q} = \left(\sum_ {i} s n _ {i q} X N P _ {i j} + \sum_ {k} s r _ {k q} X R P _ {k j}\right) / X P _ {j} \quad \forall j, q.\tag{11}
$$

In summary, the set of controllable coefficients are $sn_{iq}$ , $sr_{kq}$ , $xn_{i}$ , and $xr_{k}$ , and the designated decision variables, $XP_{j}$ and $SP_{jq}$ .

## 3.3. Development of a neural network model for the refinery

Let's illustrate the neural network for the refinery. The overall architecture is depicted in Fig. 3. In this example, we focus on four typical fuel products: DS04 (low sulphur diesel), DS10 (high sulphur diesel), BC16 (low sulphur bunker C), and BC40 (high sulphur bunker C), because they are the most important and produced in the largest volumes. Thus on the input side of the neural network model, there are four final products each with one production amount node (XP) and three quality specification nodes (sulphur content $SP_{SUL}$ ; pore $SP_{POR}$ ; and viscosity $SP_{VIS}$ ). So there are 16 input nodes: $XP_{DS04}$ , $SP_{DS04,SUL}$ , $SP_{DS04,POR}$ , $SP_{DS04,VIS}$ , $XP_{DS10}$ , $SP_{DS10,SUL}$ , $SP_{DS10,POR}$ , $SP_{DS10,VIS}$ , $XP_{BC16}$ , $SP_{BC16,SUL}$ , $SP_{BC16,POR}$ , $SP_{BC16,VIS}$ , $XP_{BC40}$ , $SP_{BC40,SUL}$ , $SP_{BC40,POR}$ , and $SP_{BC40,VIS}$ . At the same time, the 44 controllable coefficient nodes are placed at the output layer, which can be categorized into two groups: the eight intermediate products group (32 nodes) and the three reformed products group (12 nodes). Each group has a blending amount node (either $xn$ for intermediate product, or $xr$ for reformed product) and three quality specification nodes (sulphur, pore, and viscosity) for each product. The symbolic subscripts of output nodes are substituted with a simple number in Fig. 3 as follows. The values {HKR, LKR, HLG, LLG, HHG, LHG, HRC, LRC} are the names of intermediate products $i$ , and the values {HL1, HL2, VGO} are the names of reformed products $k$ .

Subscript i of blending amount of intermediate product xn

$$
\begin{array}{l} H K R = 1 \\ H H G = 5 \end{array}
$$

$$
\begin{array}{l} L K R = 2 \\ L H G = 6 \end{array}
$$

$$
\begin{array}{l} {H L G = 3} \\ {H R C = 7} \end{array}
$$

$$
\begin{array}{l} L L G = 4 \\ L R C = 8 \end{array}
$$

Subscript k of blending amount of reformed product xr

$$
H L I = 1
$$

$$
H L 2 = 2
$$

$$
V G O = 3
$$

Subscripts i and q for the quality specification of intermediate product sn

$$
\{i = H K R; q = S U L \} = 1
$$

$$
\{i = H K R; q = P O R \} = 2
$$

$$
\{i = H K R; q = V I S \} = 3
$$

$$
\{i = L K R; q = S U L \} = 4
$$

$$
\{i = L K R; q = P O R \} = 5
$$

$$
\{i = L K R; q = V I S \} = 6
$$

$$
\{i = H L G; q = S U L \} = 7
$$

$$
\{i = H L G; q = P O R \} = 8
$$

$$
\{i = H L G; q = V I S \} = 9
$$

$$
\{i = L L G; q = S U L \} = 1 0
$$

$$
\{i = L L G; q = P O R \} = 1 1
$$

$$
\{i = L L G; q = V I S \} = 1 2
$$

$$
\{i = H H G; q = S U L \} = 1 3
$$

$$
\{i = H H G; q = P O R \} = 1 4
$$

$$
\{i = H H G; q = V I S \} = 1 5
$$

$$
\{i = L H G; q = S U L \} = 1 6
$$

$$
\{i = L H G; q = P O R \} = 1 7
$$

$$
\{i = L H G; q = V I S \} = 1 8
$$

$$
\{i = H R C; q = S U L \} = 1 9
$$

$$
\{i = H R C; q = P O R \} = 2 0
$$

$$
\{i = H R C; q = V I S \} = 2 1
$$

$$
\{i = L R C; q = S U L \} = 2 2
$$

$$
\{i = L R C; q = P O R \} = 2 3
$$

$$
\{i = L R C; q = V I S \} = 2 4
$$

Subscripts k and q for the quality specification of reformed product sr

$$
\{k = H L I; q = S U L \} = 1
$$

$$
\{k = H L I; q = P O R \} = 2
$$

$$
\{k = H L 2; q = S U L \} = 4
$$

$$
\{k = H L 2; q = P O R \} = 5
$$

$$
\{k = H L I; q = V I S \} = 3
$$

$$
\{k = H L 2; q = V I S \} = 6
$$

$$
\{k = V G O; q = S U L \} = 7
$$

$$
\{k = V G O; q = P O R \} = 8
$$

$$
\{k = V G O; q = V I S \} = 9
$$

To train and test the neural network model, we have generated the paired input/output data sets from the optimal blending model. Details of training and testing procedure can be founded in the paper by Lee and Kim [9]. They showed that the neural network approach can perform the adaptive optimal control for a refinery with a 3.08% error level from the desired values on average, which verifies that the neural network approach can outperform human experts in the real world (with a 10% error level, on average). They also devised an algorithm to resolve the one-to-many relationships in the data set to improve the performance of the neural network, which empirically reduced the error level to 1.50%.

## 4. Adaptive optimal controller: UNIK-OPT/NN

## 4.1. Introduction

Since it is very difficult and time-consuming for users to perform the adaptive optimal control process using two independent optimization and neural network packages, we need to develop a tightly coupled tool which can systematically support the whole procedure in a single thread. Without a tightly coupled tool for adaptive optimal control, at least ten different files are necessary to interface between an optimization model and a neural network model. If we need to decompose the neural network model into multiple smaller ones to enhance the performance [9], the number of files to interface increases dramatically. Such an explosion in the number of files means redundancy of data, which not only causes inefficiency, but makes implementation impossible in a practical sense.

To realize the tightly coupled (fully integrated) architecture, it is necessary that the optimization and neural network modeler be able to share a common representation of models and data. To meet this requirement, we adopt two tools: UNIK-OPT [8] and UNIK-NEURO [4] which can represent the optimization model and the neural network model in frames at semantic level, respectively. On top of these two compatible tools, we developed an integrating tool for the adaptive optimal control UNIK-OPT/NN.

## 4.2. Architecture of UNIK-OPT / NN

The architecture of UNIK-OPT/NN in conjunction with UNIK-OPT and UNIK-NEURO is depicted in Fig. 4. UNIK-OPT/NN consists of two parts: an adaptive optimal control model constructor and an adaptive optimal controller. The constructor supports the construction of neural network models and may link UNIK-OPT to support the formulation of optimization models (or selection of one if it already exists). In this process, the generic capabilities of UNIK-OPT and UNIK-NEURO are embeddedly employed. The adaptive optimal controller, on the other hand, utilizes UNIK-NEURO to identify the required adjustment of coefficients and UNIK-OPT to validate the degree of conformation to the targets set on the decision variables. Section 4.3 describes five steps in the construction process and Section 4.4 describes the controller.

![](/api/attachments/AP9UDM7T/fulltext/images/101acc4a147eaa9bd3f01ea869a03ac44eda24674714914c26a2b27c2ceb3056.jpg)  
Fig. 3. Architecture of the neural network model in the refinery case.

![](/api/attachments/AP9UDM7T/fulltext/images/cfadc2bc4268aaa7db8cbafe510356db780c7b25c0e12ffed831767ffeaeeeff.jpg)  
Fig. 4. Architecture of UNIK-OPT/NN environment.

## 4.3. Adaptive optimal control model constructor

## 4.3.1. Semantic optimization model formulation

The first step in preparing the adaptive optimal control system is formulation (or selection) of a target optimization model. In UNIK-OPT/NN, the knowledge-assisted formulation capability of UNIK-OPT can simply be brought in, which will generate a semantic level representation of the linear programming model in frames. For the formulation process itself, refer to [8]. For instance, the blending optimization model (1)-(10) described in Section 3 is represented as follows:

{{BLENDING\_OPT\_MODEL

(IS-A OPTIMIZATION-MODEL)

<table><tr><td>(MENU</td><td colspan="2">&quot;Optimal Blending LP Model&quot;) / *Title in the menu list of files* /</td></tr><tr><td>(DOMAIN</td><td colspan="2">REFINERY_DOMAIN)</td></tr><tr><td>(OBJECTIVE</td><td colspan="2">(+ PENALTY_OVER_QUALITY_LEVEL_BOT)(+ PENALTY_UNDER_QUALITY_LEVEL_BOT))</td></tr><tr><td>(DIRECTION</td><td colspan="2">MIN)</td></tr><tr><td>(CONSTRAINT</td><td colspan="2">(PRODUCT_SPEC_REQUIRED (PRODUCT QUALITY_SPEC))(FINAL_PRODUCT_MATERIAL_BALANCE (PRODUCT))(STREAM_MATERIAL_BALANCE (STREAM))(RU_MATERIAL_BALANCE (REFORMED_PRODUCT))(FINAL_PRODUCT_AMOUNT_UPPER_LIMIT (PRODUCT))(FINAL_PRODUCT_AMOUNT_LOWER_LIMIT (PRODUCT))(QUALITY_SPEC_UPPER_LIMIT (PRODUCT QUALITY_SPEC))(QUALITY_SPEC_LOWER_LIMIT (PRODUCT QUALITY_SPEC))</td></tr><tr><td>(FUNCTION</td><td colspan="2">(SP_FUNCTION (PRODUCT QUALITY_SPEC))</td></tr><tr><td rowspan="9">(BOT</td><td>PRODUCTION_AMOUNT_BOT</td><td>STREAM_PRODUCTION_BOT</td></tr><tr><td>I_BLENDING_AMOUNT_BOT</td><td>R_BLENDING_AMOUNT_BOT</td></tr><tr><td>STREAM_REFORM_AMOUNT_BOT</td><td>I_BLENDING_ASSAY_BOT</td></tr><tr><td>R_BLENDING_ASSAY_BOT</td><td>MINIMUM_SPEC_BOT</td></tr><tr><td>MAXIMUM_SPEC_BOT</td><td>RES_BOT</td></tr><tr><td>PRODUCTION_AMOUNT_LOWER_BOT</td><td>PRODUCTION_AMOUNT_UPPER_BOT</td></tr><tr><td>OVER_QUALITY_LEVEL_BOT</td><td>UNDER_QUALITY_LEVEL_BOT</td></tr><tr><td>PENALTY_OVER_QUALITY_LEVEL_BOT</td><td>PENALTY_UNDER_QUALITY_LEVEL_BOT</td></tr><tr><td>SPEC_OF_STREAM_BOT</td><td>SPEC_OF_REFORMED_BOT)</td></tr><tr><td rowspan="10">(VARIABLE</td><td colspan="2">(PRODUCTION_AMOUNT/ *XP*/ (PRODUCT (_ALL)))</td></tr><tr><td colspan="2">(I_BLENDING_AMOUNT/ *XNP*/ (PRODUCT (_ALL)) (STREAM (_ALL)))</td></tr><tr><td colspan="2">(R_BLENDING_AMOUNT/ *XRP*/ (PRODUCT (_ALL))</td></tr><tr><td></td><td>(REFORMED_PRODUCT (HL1 HL2 VGO)))</td></tr><tr><td colspan="2">(OVER_QUALITY/ *D* / (PRODUCT (_ALL))</td></tr><tr><td></td><td>(QUALITY_SPEC (_ALL)))</td></tr><tr><td colspan="2">(UNDER_QUALITY/ *D* / (PRODUCT (_ALL))</td></tr><tr><td></td><td>(QUALITY_SPEC (_ALL)))</td></tr><tr><td colspan="2">(SPEC_OF_PRODUCT/ *SP*/ (PRODUCT (_ALL))</td></tr><tr><td></td><td>(QUALITY_SPEC (_ALL))))</td></tr><tr><td rowspan="12">(CONSTANT</td><td colspan="2">(STREAM_AMOUNT/ *xn*/ (STREAM (_ALL)))</td></tr><tr><td colspan="2">(STREAM_REFORMED/ *xr*/ (REFORMED_PRODUCT (_ALL)))</td></tr><tr><td colspan="2">(SPEC_OF_STREAM/ *sn*/ (STREAM (_ALL)) (QUALITY_SPEC (_ALL)))</td></tr><tr><td colspan="2">(SPEC_OF_REFORMED/ *sr*/ (REFORMED_PRODUCT (HL1 HL2 VGO))</td></tr><tr><td></td><td>(QUALITY_SPEC (_ALL)))</td></tr><tr><td colspan="2">(UPPER_LIMIT_SPEC/ *spU*/ (PRODUCT (_ALL)) (QUALITY_SPEC (_ALL)))</td></tr><tr><td colspan="2">(LOWER_LIMIT_SPEC/ *spL*/ (PRODUCT (_ALL)) (QUALITY_SPEC (_ALL)))</td></tr><tr><td colspan="2">(TARGET_SPEC/ *γ*/ (PRODUCT (_ALL)) (QUALITY_SPEC (_ALL)))</td></tr><tr><td colspan="2">(UPPER_LIMIT_OF_PRODUCTION/ *xpU*/ (PRODUCT (_ALL)))</td></tr><tr><td colspan="2">(LOWER_LIMIT_OF_PRODUCTION/ *xpL*/ (PRODUCT (_ALL)))</td></tr><tr><td colspan="2">(OVER_PENALTY_WEIGHT/ *w* / (PRODUCT (_ALL)) (QUALITY_SPEC (_ALL)))</td></tr><tr><td colspan="2">(UNDER_PENALTY_WEIGHT/ *w* / (PRODUCT (_ALL)) (QUALITY_SPEC (_ALL))))</td></tr><tr><td rowspan="4">(INDEX</td><td colspan="2">(PRODUCT/ *j*/ (DS04 DS10 BC16 BC40))</td></tr><tr><td colspan="2">(STREAM/ *i*/ (HRC HHG HLG HKR LRC LHG LLG LKR))</td></tr><tr><td colspan="2">(REFORMED_PRODUCT/ *k*/ (HL1 HL2 VGO HR1 HR2 HR3 LR1 LR2 LR3 HTK LTK))</td></tr><tr><td colspan="2">(QUALITY_SPEC/ *q*/ (SUL POR VIS SPG)))</td></tr></table>

The above frame BLENDING\_OPT\_MODEL explains the overall structure of the blending linear programming model by showing the objectives, constraints, deriving functions, blocks of terms (BOT), variables, constants, and indices. The BOT means the set of terms that share the same “Σ” sign, and is suffixed with “\_BOT”. The symbol “\_ALL” in the parentheses following the index names in the VARIABLE and CONSTANT denotes that all members of index values are applicable. The strings encapsulated by “/ \*” and “\* /” are the comments that show the corresponding notational symbols in the statements (1)-(11).

In this example, the third constraint, e.g. STREAM\_MATERIAL\_BALANCE (STREAM), means that the constraint should be satisfied for each STREAM, which corresponds to statement (4). The constraint itself is further represented in the following frame, explaining the composing BOTs on the left- and right-hand side of the equal sign.

```txt
{{STREAM_MATERIAL_BALANCE
(IS-A    CONSTRAINT)
(OPERATOR    EQ)
(LHS    (+ I_BLENDING_AMOUNT_BOT))
(RHS    (+ STREAM_PRODUCTION_BOT))
}}
```

Each BOT in the constraint is described in another frame. For instance, IBLENDING\_AMOUNT\_BOT, referring to the term $\Sigma_{j}XNP_{ij}$ in statement (4), is represented as:

```txt
{{IBLENDING_AMOUNT_BOT
(IS-A BOT)
(COEFFICIENT 1)
(DECISION I_BLENDING_AMOUNT)
(SUM_INDEX PRODUCT)
}}
```

As mentioned in statement (11), the derived variables $SP_{jq}$ from the solution of the optimization model are represented by FUNCTION frames.

```lisp
{{SP_FUNCTION
(IS-A FUNCTION)
(EQUAL_TO SPEC_OF_PRODUCT)
(FUNCTION_FORM
(/ (+ SPEC_OF_STREAM_BOT SPEC_OF_REFORMED_BOT)
PRODUCTION_AMOUNT_BOT))
}}
```

By using the above semantic representation of optimization model, UNIK-OPT/NN can interpret the model for the adaptive optimal control purpose. On the other hand, the semantically represented model can automatically be transformed to the notational form which can be understood by solver packages.

## 4.3.2. Definition of the adaptive optimal control model

The definition of adaptive optimal control model requires that the users determine the designated decision variables and controllable coefficients from the optimization model. UNIK-OPT/NN supports this process at two levels of abstraction: aggregate and individual notational levels. At the aggregate notational level, the model builder simply selects index-free decision variables and coefficients. The system then automatically identifies the combination of compatible indices. For instance, in Fig. 5, the decision variable SPEC\_OF\_PRODUCT is selected. Then the indices associated with the selected decision variables are retrieved. On the other hand, at the individual notational level, the model builder may also select indexed coefficients and decision variables one by one. The screen with the defined adaptive optimal control model is illustrated in Fig. 6.

The definition is internally captured in frames as follows:

```txt
{{BLENDING_ADAPTIVE_OPTIMAL_CONTROL_MODEL
(IS-A ADAPTIVE_OPTIMAL_CONTROL_MODEL)
(OPT_MODEL BLENDING_OPT_MODEL)
(DESIGNATED_DECISION_VARIABLES /*Input Nodes*/
(PRODUCTION_AMOUNT /*XP*/
(PRODUCT DS04 DS10 BC16 BC40))
(SPEC_OF_PRODUCT /*SP*/
(PRODUCT DS04 DS10 BC16 BC40)
(QUALITY_SPEC SUL POR VIS))
(CONTROLLABLE_COEFFICIENTS /*Output Nodes*/
(STREAM_AMOUNT /*xn*/
(STREAM HRC HHG HLG HKR LRC LHG LLG LKR))
(REFORMED_AMOUNT /*xr*/
(REFORMED_PRODUCT HL1 HL2 VGO))
......
......
......
(SPEC_OF_REFORMED /*sr*/
(REFORMED_PRODUCT HL1 HL2 VGO)
(QUALITY_SPEC SUL POR VIS)))
(NEURAL_NETWORK /*unfilled*/)
(TRAIN_INSTANCE_CLASS (CLASSNAME /*unfilled*/)
NUMBER /*unfilled*/))
(TEST_INSTANCE_CLASS (CLASSNAME /*unfilled*/)
(NUMBER /*unfilled*/))
(AAE_BOUND /*unfilled*/)
(AER_BOUND /*unfilled*/)
}) /*End of Initial Adaptive Optimal Control Model Definition*/
```

The current frame BLENDING\_ADAPTIVE\_OPTIMAL\_CONTROL\_MODEL keeps DESIGNATED\_DECISION\_VARIABLES and CONTROLLABLE\_COEFFICIENTS along with seven still unfilled items.

## 4.3.3. Generation of the neural network model

From the BLENDING\_ADAPTIVE\_OPTIMAL\_CONTROL\_MODEL, UNIK-OPT/NN can automatically derive the overall architecture of the neural network as described in the following frame BLENDING\_OPT\_MODEL\_NN.

![](/api/attachments/AP9UDM7T/fulltext/images/d83cd9e53767d09c659d32b6c8a2cdd69b737ef3351b56df7ca8f7d59895cc69.jpg)  
Fig. 5. An illustrative screen of desired decision variable selection.

![](/api/attachments/AP9UDM7T/fulltext/images/17d8580d1beeba8af0e5a03cb68bbb7e151b3151d85c9c0b1541e13bbf5e26d7.jpg)  
Fig. 6. An illustrative screen of definition of adaptive optimal control.

<table><tr><td colspan="2">{{BLENDING_OPT_MODEL_NN / *Architecture */</td></tr><tr><td>(IS-A</td><td>NEURAL_NETWORK)</td></tr><tr><td>(NUMBER_OF_INPUTS</td><td>16)</td></tr><tr><td>(NUMBER_OF_OUTPUTS</td><td>44)</td></tr><tr><td>(HIDDEN_LAYER</td><td>(1 33))</td></tr><tr><td>(STRATEGY</td><td>LEARN_STG_OF_BLEND_MODEL)</td></tr><tr><td>}}</td><td></td></tr></table>

The number of hidden layers and nodes in it (1 and 33 in this example) are internally generated although they may be set by the user explicitly. The default learning strategy is also generated as the following illustrative frame.

<table><tr><td colspan="2">{{LEARN_STG_OF_BLEND_MODEL / *Control Strategy */</td></tr><tr><td>(IS-A</td><td>LEARNING_STRATEGY)</td></tr><tr><td>(LEARNING_RULE</td><td>BACK-PROPAGATION)</td></tr><tr><td>(LEARNING_RATE</td><td>0.5)</td></tr><tr><td>(MOMENTUM</td><td>0.9)</td></tr><tr><td>(ERROR_CRITERIA</td><td>0.001)</td></tr><tr><td>(ERROR_TREND_CRITERIA</td><td>0.01 100)</td></tr><tr><td>(LEARNING_STEPSIZE</td><td>INSTANCE)</td></tr><tr><td>(ENDING_EPOCH</td><td>1000 2000 3000)</td></tr><tr><td>(RANDOM_RANGE</td><td>0.10)</td></tr><tr><td>}}</td><td></td></tr></table>

The value of the attribute LEARNING\_STEPSIZE can be either INSTANCE or EPOCH depending on whether the learning takes place for each instance or for all instances set. The description for each input and output node is generated in each frame. For instance, an output node REFORMED\_AMOUNT-HL1 which corresponds to the controllable coefficient REFORMED\_AMOUNT indexed with HL1 is represented as:

<table><tr><td colspan="2">{{REFORMED_AMOUNT-HL1</td></tr><tr><td>(OUTPUT-OF</td><td>BLENDING_OPT_MODEL_NN)</td></tr><tr><td>(TYPE</td><td>OUTPUT)</td></tr><tr><td>(REFERENCE</td><td>REFORMED_AMOUNT HL1)</td></tr><tr><td>(ACTIVATION</td><td>)</td></tr><tr><td>(MAX_CONTROL_RANGE</td><td>5.000)</td></tr><tr><td>(MIN_CONTROL_RANGE</td><td>0.000)</td></tr><tr><td>(FROM</td><td>(HIDDEN_NODE1 -0.312) / * Initial Random Weight */ (HIDDEN_NODE2 +0.567)</td></tr><tr><td></td><td>......</td></tr><tr><td></td><td>......</td></tr><tr><td></td><td>(HIDDEN_NODE30 -0.712))</td></tr><tr><td>(TO</td><td>)</td></tr><tr><td>}}</td><td></td></tr></table>

![](/api/attachments/AP9UDM7T/fulltext/images/93aaf0493b27785967508c53fcddc2179effeb1d32ea832b56047b9f628d3e11.jpg)  
Fig. 7. An illustrative screen of the generated neural network model.

![](/api/attachments/AP9UDM7T/fulltext/images/88bb990b5573693a353eb7a34c0c73423a9189d17eaa620fc0031a145b8c251c.jpg)  
Fig. 8. An illustrative screen of configuration of architecture.

The graphic form of the network is shown as Fig. 7. It is the strategy of UNIK-OPT/NN to provide the default values of all attributes necessary to define the neural network model, although they can be changed by the users by calling the inherent user interface of UNIK-NEURO as illustrated in Figs. 8 and 9.

## 4.3.4. Training and testing instances generation

To train and test the neural network, we need to collect a sufficient number of instances. Such instances may be either collected from the historical records or generated from the optimization model. UNIK-OPT/NN provides the capability of automatic generation by internally generating the random coefficients within the meaningful ranges and by solving the optimization model with the coefficients. In this example, 100 instances are generated for training, while 25 for testing. The following frame BLEND\_TRAIN\_INSTANCE-85 illustrates a generated training instance.

In this example, the first two attributes (PRODUCTION\_AMOUNT and SPEC\_OF\_PRODUCT) are computed from the optimization model which used the randomly generated coefficients in the remaining attributes. The beauty of the above semantic representation of the instances is that the values can be directly interfaced with the optimization model as well as the neural network model.

## 4.3.5. Training and testing the neural network model

Now, UNIK-OPT/NN is ready to train and test the performance of the neural network. The training procedure can be performed purely by calling UNIK-NEURO. However, the testing procedure depicted in Fig. 1 requires coordination with UNIK-OPT as well. Therefore, the representation used for instances in Section 4.3.4 can also be used for the common interfaces. The criteria adopted for validation of the neural network are Average Absolute Error (AAE) and Average Error Ratio (AER) as illustrated in Fig. 10. The 1.79% AER in this example seems quite satisfactory in comparison with the user defined upper bound of 5%.

![](/api/attachments/AP9UDM7T/fulltext/images/a105d07b3612cedede36859b3f965e74e4677f6225cd77bca245940e8a4623c7.jpg)  
Fig. 9. An illustrative screen of configuration of learning strategy.

![](/api/attachments/AP9UDM7T/fulltext/images/41ea5eaa0ee2e93cecad167229fc139ad3889cb15ca1308e08f008000ac11bd5.jpg)  
Fig. 10. An illustrative screen of validation of the neural network model.

\} / \* End of Adaptive Optimal Control Model Definition\* /

![](/api/attachments/AP9UDM7T/fulltext/images/1d917a9e1cbce52c4e00dd5ba19f209c9f2abeefe138fe923e5a6111e2d0f9de.jpg)  
Fig. 11. An illustrative screen of performance result from adaptive optimal control.

After validation, UNIK-OPT/NN can fill in all of the empty spots of the adaptive optimal control model which was partially defined in Section 4.3.2.

![](/api/attachments/AP9UDM7T/fulltext/images/10a68d834d194daceef99cec4d21475c397b410017dc53683b29bea66bb8eaa6.jpg)

## 4.4. Adaptive optimal controller

When a user wants to perform the adaptive optimal control on an optimization model, UNIK-OPT/NN recalls the related neural network model with the desired values on the designated decision variables in the optimization model. Then the suggested values on the controllable coefficients by UNIK-NEURO are transferred to UNIK-OPT to adjust the optimization model accordingly, and the realized value is displayed as illustrated in Fig. 11.

In this example, the user had to produce 106,460 barrels of low sulphur diesel (DS04). However, the realized amount was 107,410 barrels. The evaluation of this result in terms of AAE and AER is 950 barrels and 0.89%, respectively, which is more than satisfactory.

## 5. Conclusion

To support adaptive optimal control using a neural network model, a tool UNIK-OPT/NN is developed which can automate most of the procedure of neural network construction on top of the knowledge-assisted optimization model formulator UNIK-OPT. This paper has shown how the neural network can be effectively used with the optimization models by adopting a commonly interpretable representation at a semantic level. UNIK-OPT/NN should be useful for the development of many adaptive control systems on optimization models.

## References

[1] F. Girosi and T. Poggio, Networks for Learning: A View from the Theory of Approximation of Functions, in: V. Milutinovic and P. Antognetti, Eds., Neural Networks: Concepts, Applications, and Implementations (Prentice Hall, 1991) 110–76.

[2] R. Hecht-Nielsen, Neurocomputing (Addison-Wesley, 1990).

[3] M.I. Jordan and R.A. Jacobs, Learning to Control an Unstable System with Forward Modeling, in: D.S. Touretzky, Ed., Advances in Neural Information Processing Systems 2 (Morgan Kaufmann, 1990) 324–331.

[4] W. Kim, Connection of Neural Network with Expert System, Intelligent Information Systems (in Korean) 2, No. 3 (1993) 102–110.

[5] M. Kuperstein and J. Rubinstein, Implementation of an Adaptive Neural Controller for Sensory-Motor Coordination, in: R. Pfeifer, J. Schreter, F. Fogelman-Soulie and L. Steels, Eds., Connectionism in Perspective (North-Holland, 1989) 49–61.

[6] A. Lapedes and R. Farber, How Neural Nets Work, in: D.Z. Anderson, Ed., Neural Information Processing Systems (American Institute of Physics, New York, 1988) 442–456.

[7] J.K. Lee, S.B. Oh, M.S. Suh, M.Y. Kim and Y.U. Song, Knowledge Network for Planning and Control of Refinery Industry: UNIK-R Project Experience, Proceedings of the Fourth International Conference on Expert Systems in Production and Operations Management (May 1990) 16-32.

[8] J.K. Lee and M.Y. Kim, Knowledge-assisted Optimization Model Formulation: UNIK-OPT, Forthcoming in Decision Support Systems (1994).

[9] J.K. Lee and W. Kim, Neural Network Surrogate of the Optimization Model's Adaptive Sensitivity Analysis: A Refinery Case, Working Paper (KAIST, 1993).

[10] D.H. Nguyen and B. Widrow, Neural Networks for Self-Learning Control Systems, IEEE System Magazine (April 1990) 18–23.

[11] D.E. Rumelhart, G.E. Hinton and R.J. Williams, Learning Internal Representations by Error Propagation, in: D.E. Rumelhart, J.L. McClelland and the PDP Research Group, Eds., Parallel Distributed Processing: Explorations in the Microstructures of Cognition, Vol. 1: Foundations, Ch. 8 (MIT Press, 1986).

[12] L. Xu, S. Klasa and A. Yuille, A Survey on Supervised Learning Techniques for Static Feedforward Networks, Proceedings of the International Joint Conference on Neural Networks, Vol. II (1992(2)) 320–325.

![](/api/attachments/AP9UDM7T/fulltext/images/48f02e821ebab32ba41af28e7bc10864d714623dfecbc9cfddbdc852a53bcd8f.jpg)  
Wooju Kim is a full-time lecturer in the Department of Industrial Engineering, Chonbuk National University, South Korea. He received his B.B.A. degree from Yonsei University in 1987 and his M.Sc. from KAIST in 1989. He had also received his Ph.D. in Management Science from KAIST in 1994. His major research interests include Neural Networks, Expert Systems, S/W Engineering, Knowledge Representation and Acquisition, Managerial Forecasting. He is a member of Korea Expert Systems Society.

![](/api/attachments/AP9UDM7T/fulltext/images/94a1afd051add8d956c0c1f1f0b2155ea42d2de28d1e82c4dea6ff8357e9695e.jpg)

Jae Kyu Lee is a Professor of Management Information Systems at Korea Advanced Institute of Science and Technology. He received a B.A. from Seoul National University and M.S. from the Korea Advanced Institute of Science and Technology, and a Ph.D. from the Wharton School, University of Pennsylvania. He has authored several books on expert systems, and published numerous papers in the journals like Management Science, Decision Support Systems, Expert Systems with Applications: An International Journal, Decisions Sciences, Fuzzy Sets and Systems, and International Journal of Man-Machine Studies. Currently, he is an editorial member of the journals Decision Support Systems, Expert Systems with Applications: An International Journal, International Journal of Intelligent Systems in Accounting, Finance and Management, and New Review of Applied Expert Systems.
