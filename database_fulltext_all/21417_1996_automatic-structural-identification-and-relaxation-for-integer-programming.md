---
otero_id: 21417
otero_key: "VKDFCQ9Q"
title: "Automatic structural identification and relaxation for integer programming"
authors: "Chulsoo Kim; Jae Kyu Lee"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)80003-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Automatic structural identification and relaxation for integer programming

Chulsoo Kim $^{a,*}$ , Jae Kyu Lee $^{b}$

$^{a}$ Department of Management Information Systems, Wonkwang University, Iksan, South Korea $^{b}$ Department of Management Information Systems, Korea Advanced Institute of Science and Technology, 207-43, Cheongryang, Seoul, 130-012, South Korea

## Abstract

This research investigates the automatic identification of typical embedded structures in the Integer Programming (IP) models and automatic transformation of the problem to an adequate Lagrangian problem which can provide tight bounds within the acceptable run time. For this purpose, the structural distinctivenesses of variables, constants, blocks of terms, and constraint chunks are identified to specify the structure of the IP model. To assist the identification of the structural distinctiveness, the representation by the knowledge based IP model formulator, UNIK-IP, is adopted. To reason for the structural identification, the hybrid of bottom-up, top-down, and case-based approaches are proposed. A system UNIK-RE-LAX is developed to implement the approaches proposed in this research.

Keywords: Model management systems; Integer programming; Lagrangian relaxation; Unified programming; UNIK

## 1. Introduction

Model management has been the concern of Decision Support Systems researchers for a long time. One of their major research points is the representation of problems. Since representing the general problems is not only difficult but also impractical, a group of researchers have narrowed its focus on the representation of a specific category of problems such as optimization problems $[17,21,24,28,29]$ .

The Intelligent Information Systems laboratory at Korea Advanced Institute of Science and Technology (KAIST) is in line with this research paradigm and has developed the tool UNIK (UNIfied Knowledge), which captures the optimization models at a semantic level. The first attempt was focused on linear programming $[24]$ , but the scope is expanded to include integer programming $[33]$ and a class of nonlinear programming problems. Currently, their research covers the unification of optimization with rule based systems $[26,27]$ and the unification of constraint satisfaction problems with rule based systems $[25]$ , both of which are intended to support the multiple criteria decision makings. In addition, the neural network could be used on top of the optimization model for control purposes $[20]$ . So far, the research scope was the semantic representation of such unified problems and the aiding model formulation process under the assumption that one of the standard solvers such as Simplex algorithm, Interior Point algorithm, and Branch and Bound algorithm can be used.

In the second phase of UNIK project, representing the solution procedures of NP-hard problems is investigated. As a first step toward this goal, the automatic identification of typical embedded structures in the model and the automatic transformation of the problem to a solvable Lagrangian problem are attempted. This paper describes these efforts in the following organization. Section 2 briefly reviews the concept of Lagrangian relaxation, which relaxes the hard portion of the constraints in complex integer programming problems still obtaining sharp bounds. Section 3 represents the distinctive components necessary to identify the typical embedded structures. Section 4 proposes the process of identifying embedded structures from a particular model, and Section 5 transforms the model to an adequate Lagrangian problem. Section 6 shows the architecture of UNIK-RELAX that implements this approach. The prototype UNIK-RELAX is developed on UNIK-IP, an aid to a knowledge based integer programming model formulation.

## 2. Review on Lagrangian relaxation

Suppose the following integer programming problem (1)-(3), which is very difficult to solve because of the constraint set;

Minimize $z(x)$

(1)

subject to:

$$
g _ {i} (\boldsymbol {x}) \geq 0, i = 1, \dots , r,\tag{2}
$$

$$
\boldsymbol {x} \in X\tag{3}
$$

A Lagrangian problem of this original problem has a new objective function $L(x, u) = z(x) + \sum_{i=1}^{r} u_i g_i(x)$ with the remaining constraints in (3), where $u_i$ 's mean Lagrangian multipliers. Thus the relaxed Lagrangian problem is

$$
\text { Minimize } L (x, u) = z (x) + \sum_ {i = 1} ^ {r} u _ {i} g _ {i} (x)\tag{4}
$$

subject to:

$$
\boldsymbol {x} \in X.\tag{5}
$$

Fisher [9] has shown that NP-hard problems such as generalized assignment, set covering and partitioning, location, scheduling, and traveling salesman problems can be relaxed to Lagrangian problems which can provide extremely sharp lower bounds within manageable computation times. These problems can be relaxed because they include at least one of the special structures which can lead to an efficient solution algorithm, while providing very tight bounds. So, it is necessary to identify such structures and to generate the relaxed

Table 1  
Relationships between embedded structure and adequate Lagrangian problem

<table><tr><td>No</td><td>Embedded structure</td><td>Adequate Lagrangian problem</td></tr><tr><td>1</td><td>0_1_Knapsack</td><td>0_1_Knapsack</td></tr><tr><td>2</td><td>Assignment (Perfect_2_Matching)</td><td>Assignment (Perfect_2_Matching)</td></tr><tr><td>3</td><td>0_1_General_Upper_Bound</td><td>0_1_General_Upper_Bound</td></tr><tr><td>4</td><td>0_1_Variable_Upper_Bound</td><td>0_1_Variable_Upper_Bound</td></tr><tr><td>5</td><td>1_Spanning_Tree</td><td>1_Spanning_Tree</td></tr><tr><td>6</td><td>Knapsack_with_Time_Horizon</td><td>Pseudo_Polynomial_Dynamic_Programming</td></tr><tr><td>7</td><td>General_IP_with_Unbounded</td><td>Group</td></tr></table>

Lagrangian problems whose solution efficiency is proved in the past research. For this purpose, the types of NP-hard problems and their corresponding Lagrangian problems summarized in Table 1 can be utilized [9].

To automate the identification of embedded structures, we will focus on the seven well known ones in Table 1. However, the approach that we develop here can be easily adopted to the new types of embedded structures which may be found in the future. In the next section, we will explore how such typical embedded structures can be represented. Once the embedded structures are identified, the constraints can be relaxed in the following manners:

1. Structure 1-5 in Table 1: Relax the constraints not associated with the structure

2. Structure 6 in Table 1: Relax the constraints associated with the structure.

3. Structure 7 in Table 1: Relax all constraints concerned with the unbounded variables in the original model.

## 3. Representation of embedded structures

In this section, we represent the distinctive components necessary to identify the typical embedded structures. Since the UNIK-IP represents the integer programming model in objects, each object needs to have an additional attribute to describe the characteristics of embedded structures. Let us call such an attribute distinctiveness. The objects in UNIK-IP consist of variables and coefficients, blocks of terms (BOT is a pair of variable and coefficient that shares the same summation sign), constraint chunks (each of which consists of BOTs and an operator of EQ, GE, or LE), and a specific model (BOTs in the objective function and a set of constraint chunks). The indices are associated with variables, coefficients, BOTs, and constraint chunks.

## 3.1. Variables and coefficients

The distinctiveness of variables includes binary, nonnegative\_integer, and integer, and that of coefficients includes real, nonnegative, nonpositive, and constant.

## 3.2. Blocks of terms

The distinctiveness of BOT can be classified as elementary or composite.

3.2.1. Elementary distinctiveness in BOT

\- Integer\_Variable: each variable in the BOT is an integer variable.

\- 0\_1\_Integer\_Variable: each variable in the BOT is either 0 or 1.

\- Nonnegative\_Integer\_Variable: each variable in the BOT is a nonnegative integer variable.

• Real\_Coefficient: each coefficient in the BOT is a real number.

\- Nonnegative\_Real\_Coefficient: each coefficient in the BOT is a nonnegative real number.

\- Constant\_1\_Coefficient: each coefficient in the BOT is 1.

\- Constant\_2\_Coefficient: each coefficient in the BOT is 2.

\- Constant\_n\_Coefficient: each coefficient in the BOT is the same number $n$ .

\- Constant\_S - 1\_Coefficient: the value of coefficient in the BOT is the 'total number of elements included in the set S' minus 1.

\- Two\_Indices: there exist two summation indices in the BOT.

\- Precedence\_Restricted\_Index: the first index in the BOT has a precedence restriction over the second one in the Two\_Indices cases.

\- Sum\_with\_First\_Index: the BOT is summed by the first index.

\- Sum\_with\_Second\_Index: the BOT is summed by the second index.

\- Time\_Indexed: one of the indices in the BOT implies time unit.

\- First\_Index\_is\_1: all values of the first index in the BOT are fixed to 1.

## 3.2.2. Composite distinctiveness in a BOT

The elementary distinctivenesses can compose more composite distinctivenesses by employing operators: AND, OR, or XOR. For instance, we can consider the following six typical ones. A general format is:

OPERATOR(OPERATOR(Elementary\_distinctiveness\_1 Elementary\_distinctiveness\_2)

Elementary\_distinctiveness\_3)

• Volume\_Sum\_0\_1 = AND(Nonnegative\_Real\_Coefficient 0\_1\_Integer\_Variable)

\- Volume\_Sum\_Integer = AND(Nonnegative\_Real\_Coefficient Nonnegative\_Integer\_Variable)

\- Count\_Sum\_0\_1 = AND(Constant\_1\_Coefficient 0\_1\_Integer\_Variable)

\- Precedence\_Node = AND(Precedence\_Restricted\_Index 0\_1\_Integer\_Variable)

\- Starting\_Node = AND(AND (First\_Index\_is\_1 Sum\_with\_Second\_Index) 0\_1\_Integer\_Variable)

\- First\_XOR\_Second\_Index\_Sum = AND(XOR (Sum\_with\_First\_Index Sum\_with\_Second\_Index) Two\_Indices)

## 3.2.3. Inclusive Relationships between distinctivenesses of BOTs

The distinctivenesses of BOTs have the following inclusive relationships with each other. This relationship will be used for the identification of distinctiveness in the BOT objects.

\- 0\_1\_Integer\_Variable ⊂ Nonnegative\_Integer\_Variable

\- Nonnegative\_Integer\_Variable ⊆ Integer\_Variable

\- Constant\_1\_Coefficient $\subset$ Nonnegative\_Real\_Coefficient

\- Constant\_2\_Coefficient $\subset$ Nonnegative\_Real\_Coefficient

\- Constant\_n\_Coefficient $\subset$ Nonnegative\_Real\_Coefficient

\- Nonnegative\_Real\_Coefficient $\subset$ Real\_Coefficient

\- Count\_Sum\_0\_1 $\subset$ Volume\_Sum\_0\_1

• Volume\_Sum\_0\_1 ⊂ Volume\_Sum\_Integer

## 3.3. Distinctiveness of constraint chunks

Defining distinctiveness of constraint chunks requires additional operators - like AT\_LHS, AT\_RHS, and XOR {EQ GE LE} - to describe the mathematical relationship and the location of BOTs. A general format is:

ALL BOT; for all BOTs

(AT\_LHS (Distinctivenesses of BOTs in LHS); at left hand side

AND

AT\_RHS (Distinctivenesses of BOTs in RHS)); at right hand side

AND

OPERATOR = XOR {EQ GE LE}

In case that there are more than one BOT in either LHS (Left Hand Side) or RHS (Right Hand Side), the quantifier ALL BOT will be used to identify the distinctivenesses of each side.

The constraint chunk's distinctivenesses necessary to represent the aforementioned seven embedded structures are the following ten types.

## (1) Capacity Constraint

ALL BOT

(AT\_LHS (Volume\_Sum\_0\_1)

AND
AT\_RHS (Nonnegative\_Real\_Coefficient))
AND
OPERATOR = LE

(2) First\_Matching Constraint
ALL BOT
(AT\_LHS (Count\_Sum\_0\_1 Sum\_with\_first\_index)
AND
AT\_RHS (Constant\_1\_Coefficient))
AND
OPERATOR = EQ

(3) Second\_Matching Constraint
ALL BOT
(AT\_LHS (Count\_Sum\_0\_1 Sum\_with\_second\_index)
AND
AT\_RHS (Constant\_1\_Coefficient))
AND
OPERATOR = EQ

(4) 0\_1\_GUB(Generalized Upper Bound) Constraint
ALL BOT
(AT\_LHS (Count\_Sum\_0\_1 First\_XOR\_Second\_Index\_Sum)
AND
AT\_RHS (Constant\_1\_Coefficient))
AND
OPERATOR = EQ

(5) 0\_1\_Bounded Constraint
ALL BOT
(AT\_LHS (Count\_Sum\_0\_1)
AND
AT\_RHS (Volume\_Sum\_0\_1))
AND
OPERATOR = LE

(6) One\_Cycle Constraint
ALL BOT
(AT\_LHS (Precedence\_Node)
AND
AT\_RHS (Constant\_S - 1\_Coefficient))
AND
OPERATOR = LE

(7) Starting\_Node\_Degree Constraint
ALL BOT
(AT\_LHS (Starting\_Node)
AND
AT\_RHS (Constant\_2\_Coefficient))

```c
(1) 0_1_Knapsack Structure
IF (EXIST CONSTRAINT (capacity))
THEN STRUCTURE = 0_1_Knapsack
```

```txt
AND
OPERATOR = EQ

(8) Edge_All Constraint
ALL BOT
(AT_LHS (Precedence_Node)
AND
AT_RHS (Constant_n_Coefficient))
AND
OPERATOR = EQ

(9) Polynomial_Recursive Constraint
ALL BOT
(AT_LHS (Volume_Sum_Integer Time_Indexed)
AND
AT_RHS (Nonnegative_Real_Coefficient))
AND
OPERATOR = EQ

(10) Group Constraint
ALL BOT
(AT_LHS (Integer_Variable)
AND
AT_RHS (Real_Coefficient))
AND
OPERATOR = LE
```

## 3.4. Distinctiveness of objective function

The objective function needs to describe whether MAX or MIN and the distinctiveness of the BOTs in it. ALL BOT

(OBJECTIVE (Distinctivenesses of the BOTs in Objective Function))

DIRECTION = XOR {MAX MIN}

## 3.5. Distinctiveness of embedded structures in the models

Finally, a particular integer programming model can be identified by the distinctivenesses of constraint chunks and objective function. Seven typical embedded structures can be represented as follows:

(2) Assignment Structure
IF (EXIST CONSTRAINT (first\_matching second\_matching))
THEN STRUCTURE = Assignment

(3) 0\_1\_GUB Structure
IF (EXIST CONSTRAINT (0\_1\_GUB))
THEN STRUCTURE = 0\_1\_GUB

$$
\begin{array}{l} \text {(4) 0_ {1} \_ VUB Structure} \\ \text {IF (EXIST CONSTRAINT (0_ {1} \_bounded))} \\ \text {THEN STRUCTURE = 0_ {1} \_VUB} \end{array}
$$

$$
\begin{array}{l} \text {(5) 1\_Spanning\_Tree Structure} \\ \text {IF (EXIST CONSTRAINT (one\_cycle starting\_node\_degree edge\_all))} \\ \text {THEN STRUCTURE = 1\_Spanning\_Tree} \end{array}
$$

$$
\begin{array}{l} \text {(6) Knapsack\_with\_Time\_Horizon Structure} \\ \text {IF (EXIST CONSTRAINT (polynomial\_recursive))} \\ \text {AND (ALL BOT (OBJECTIVE (volume\_sum\_integer)))} \\ \text {THEN STRUCTURE = Knapsack\_with\_Time\_Horizon} \end{array}
$$

$$
\begin{array}{l} \text {(7) General\_IP\_with\_Unbounded Structure} \\ \quad I F (E X I S T C O N S T R A I N T (g r o u p)) \\ \quad T H E N S T R U C T U R E = G e n e r a l \_ I P \_ w i t h \_ U n b o u n d e d \end{array}
$$

AND/OR relationships of distinctiveness among embedded structures, constraints, and BOTs are depicted in Fig. 1.

## 4. Identification of embedded structures

## 4.1. Semantic representations of specific models

Now let us see how we can automatically identify the embedded structures based on the integer programming model specified by the tool, UNIK-IP [33]. Let's consider a specific formulation of the plant assignment problem in (6)-(9).

$$
\text { Minimize } \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} c _ {i j} x _ {i j}\tag{6}
$$

subject to

$$
\sum_ {i = 1} ^ {m} a _ {i j} x _ {i j} \leq b, J = 1, \dots , n,\tag{7}
$$

$$
\sum_ {j = 1} ^ {n} x _ {i j} = 1, i = 1, \dots , m,\tag{8}
$$

$$
x _ {i j} = \{0, 1 \} \forall_ {i j},\tag{9}
$$

where i and j mean product and plant respectively.

This model is one of the generalized assignment problems. Using the tool UNIK-IP, this model is represented by an IP model object, two constraint objects, five BOT objects, one variable object, four coefficient objects, and two index objects as shown in Fig. 2. Note the value 'binary' in the TYPE attribute of the assignment\_var object, which restrict the variables to 0 or 1 as (9).

The current objects in Fig. 2 do not have the attribute distinctiveness. However, to apply the Lagrangian Relaxation, the distinctiveness of all objects should be identified until the one named EMBEDDED\_STRUCTURE in the IP-MODEL object is identified as shown in Fig. 3. UNIK-RELAX performs the identification for each object. For this, we can think of the following three approaches.

![](/api/attachments/VKDFCQ9Q/fulltext/images/152dd143dfe2d8c41c1148982c55df95b83cc6aada00db1c844d70ca20716c64.jpg)

![](/api/attachments/VKDFCQ9Q/fulltext/images/e91f64cb1ad495e443bb0ac71e1722c7ee3adb69d303e30cf7875ddf8fe91453.jpg)  
Fig. 2. An illustrative formulation of plant assignment problem using UNIK-IP.

## 4.2. Bottom-up approach

The bottom-up approach identifies the distinctivenesses in the order of variables and coefficients, BOTs, constraints, and the embedded structure of specific model. Fig. 3 shows the identified distinctiveness and embedded\_structure attributes generated by UNIK-RELAX from the plant assignment problem in Fig. 2. Note that the plant assignment problem have two embedded structures: 0\_1\_Knapsack and 0\_1\_GUB structures.

Since the bottom-up approach may identify more than one embedded structure, we need to resolve the conflict according to efficiency between them as shown in Table 2 [1,9,16]. In this case, 0\_1\_Knapsack problem is more efficient to solve than 0\_1\_GUB problem. The efficiency comparison knowledge is prepared in advance based on the computational experiences, modeler preference, and domain dependent characteristics. Among the embedded structures in Table 1, the structures 6 and 7 cannot be compared with other structures, because those do not have binary variables and so cannot co-exist with other structures in the same model.

```txt
{{ plant_assignment_problem
    IS-A : IP_MODEL
    DIRECTION: min
    OBJECTIVE: (+ total_cost_BOT)
    CONSTRAINT: plant_capacity_constraint  plant_assignment_constraint
    MODEL_STRUCTURE : Generalized_Assignment
    EMBEDDED_STRUCTURE : 0_1_knapsack : 0_1_GUB }}   
{{ plant_capacity_constraint
    IS-A : CONSTRAINT
    OPERATOR: LE
    LHS: (+ plant_sum_BOT)
    RHS: (+ plant_capacity_BOT)
    UNIT_INDEX: plant
    DISTINCTIVENESS: capacity }}   
{{ total_cost_BOT
    IS-A : BOT
    ATTRIBUTE: unit_cost assignment_var
    SUMMATION_INDEX: product plant
    DISTINCTIVENESS: volume_sum_0_1}}   
{{ plant_sum_BOT
    IS-A : BOT
    ATTRIBUTE: plant_volume assignment_var
    SUMMATION_INDEX: product
    DISTINCTIVENESS: volume_sum_0_1 }}   
{{ plant_choice_BOT
    IS-A : BOT
    ATTRIBUTE: one assignment_var
    SUMMATION_INDEX: plant
    DISTINCTIVENESS: count_sum_0_1
    first_XOR_second_index_sum }}   
{{ assignment_var
    IS-A : VARIABLE
    SYMBOL: x
    LINKED_INDEX: product plant
    TYPE: binary
    DISTINCTIVENESS: binary }}   
{{ unit_cost
    IS-A : COEFFICIENT
    SYMBOL: c
    LINKED_INDEX: product plant
    DISTINCTIVENESS: nonnegative }}   
{{ plant_capacity
    IS-A : COEFFICIENT
    SYMBOL: b
    LINKED_INDEX: plant
    DISTINCTIVENESS: nonnegative }}   
{{ product
    IS-A : INDEX
    SYMBOL: i
    LINKED_ATTRIBUTE: assignment_var
    unit_cost plant_volume }}
```  
Fig. 3. Identified embedded structures in the plant assignment problem.

Efficiency priority between embedded structures

Table 2

<table><tr><td>0_1_Knapsack Assignment</td><td>0_1_GUB</td><td>0_1_VUB</td></tr><tr><td>0_1_Knapsack Assignment</td><td>0_1_GUB</td><td></td></tr><tr><td>0_1_Knapsack Assignment</td><td>0_1_VUB</td><td>0_1_VUB</td></tr><tr><td>1_Spanning_Tree</td><td>Assignment</td><td>0_1_VU</td></tr><tr><td>1_Spanning_Tree</td><td>1_Spanning_Tree</td><td></td></tr><tr><td>1_Spanning_Tree</td><td>1_Spanning_Tree</td><td></td></tr><tr><td>1_Spanning_Tree</td><td></td><td></td></tr></table>

According to the efficiency priorities among the embedded structures, an embedded structure can be selected, and the relaxation to Lagrangian problems can be initiated (refer to Section 5).

To implement this approach, a forward chaining tool like UNIK-FWD [28] can be used. In Fig. 4, illustrative rules for the identification of 0\_1\_Knapsack structure are represented in the UNIK-FWD syntax. The first two rules identify the volume\_sum\_0\_1 and nonnegative\_real\_coefficient BOTs, the third rule the capacity constraint, and the last rule the 0\_1\_Knapsack structure.

The efficiency priority can be represented by using meta-rules in UNIK-FWD. Fig. 5 shows that 0\_1\_Knapsack is more efficient than 0\_1\_GUB, and assignment is more efficient than 0\_1\_Knapsack.

## 4.3. Top-down approach

Top-down approach checks the embedded structure of a specific model according to the efficiency order in Table 2. Then the associated constraints, BOTs, and variables and coefficients can be identified in turn. For the

```lisp
(RULE volume_sum_0_1_BOT
IF
(BOT
^frame-name <BOT>
^ATTRIBUTE (equal (get-value (nth 0 <>)'DISTINCTIVENESS)'nonnegative_real_coefficient)
^ATTRIBUTE (equal (get-value (nth 1 <>)'DISTINCTIVENESS)'0_1_integer_variable))
THEN
(new-value <BOT> 'DISTINCTIVENESS 'volume_sum_0_1 ))
(RULE nonnegative_real_coefficient_BOT
IF
(BOT
^frame-name <BOT>
^ATTRIBUTE (equal (get-value 'DISTINCTIVENESS)'nonnegative)
THEN
(new-value <BOT> 'DISTINCTIVENESS 'nonnegative_real_coefficient ))
(RULE capacity_constraint
IF
(CONSTRAINT
^frame-name <CONSTRAINT>
^LHS (equal (get-value <>'DISTINCTIVENESS)'volume_sum_0_1 )
^RHS (equal (get-value <>'DISTINCTIVENESS)'nonnegative_real_coefficient )
^OPERATOR = 'LE)
THEN
(new-value <CONSTRAINT> 'DISTINCTIVENESS 'capacity ))
(RULE 0_1_knapsack_structure
[structure 0_1_knapsack]
IF
(MODEL
^frame-name <MODEL>
^CONSTRAINT (equal (get-value <> 'DISTINCTIVENESS) 'capacity ))
THEN
(new-value <MODEL> 'EMBEDDED_STRUCTURE '0_1_knapsack ))
```  
Fig. 4. Illustrative rules for the identification of 0\_1\_Knapsack Structure in the UNIK-FWD syntax.

```lisp
(RULE 0_1_GUB_structure
[ structure 0_1_GUB ]
IF
(MODEL
^frame-name <MODEL>
^CONSTRAINT (equal (get-value <> 'DISTINCTIVENESS) '0_1_GUB ))
THEN
(new-value <MODEL> 'EMBEDDED_STRUCTURE '0_1_GUB Panama)
(RULE 0_1_knapsack_structure
[ structure 0_1_knapsack ]
IF
(MODEL
^frame-name <MODEL>
^CONSTRAINT (equal (get-value <> 'DISTINCTIVENESS) 'capacity Panama)
THEN
(new-value <MODEL> 'EMBEDDED_STRUCTURE '0_1_knapsack Panama)
(RULE assignment_structure
[ structure assignment ]
IF
(MODEL
^frame-name <MODEL>
^CONSTRAINT (equal (get-value <> 'DISTINCTIVENESS) 'first_matching Panama)
^CONSTRAINT (equal (get-value <> 'DISTINCTIVENESS) 'second_matching Panama)
THEN
(new-value <MODEL> 'EMBEDDED_STRUCTURE 'assignment Panama)
(META_RULE assignment_vs_0_1_knapsack
IF
(RULE
^structure (or (member 'assignment <>)(member '0_1_knapsack Panama))
THEN
(new-value <MODEL> 'EMBEDDED_STRUCTURE 'assignment Panama)
(META_RULE 0_1_knapsack_vs_0_1_GUB
IF
(RULE
^structure (or (member '0_1_knapack <>)(member '0_1_GUB Panama)))
THEN
(new-value <MODEL> 'EMBEDDED_STRUCTURE '0_1_knapsack Panama)
```  
Fig. 5. Illustrative meta-rules for the conflict resolution in the UNIK-FWD syntax.

Table 3  
Types of integer programming problems and adequate Lagrangian problems

<table><tr><td colspan="2">Types of IP ProblemsGeneralized assignment</td><td>Adequate Lagrangian Problems0-1 Knapsack</td><td>ResearchersChalmet et al. (1976) [5]; Fisher et al.(1980) [15]</td></tr><tr><td rowspan="2">General IP</td><td>- Unbounded variables</td><td>Group problem</td><td>Fisher and Shapiro (1974) [10]; Burdet(1977) [4]</td></tr><tr><td>- 0-1 variables</td><td>Generalized upper bound</td><td>Etcheberry (1978) [8]</td></tr><tr><td rowspan="2">Set coveringand partitioning</td><td>- Covering</td><td>Generalized upper bound</td><td>Etcheberry (1977) [7]</td></tr><tr><td>- Partitioning</td><td>Matching</td><td>Nemhauser and Weber (1979) [6]</td></tr><tr><td rowspan="3">Location</td><td>- Uncapacitated</td><td>Variable upper bound</td><td>Cornuejols et al. (1977) [6]</td></tr><tr><td>- Capacitated</td><td>Variable upper bound</td><td>Geoffrion (1978) [18]</td></tr><tr><td>- Databases in computer network</td><td>Variable upper bound</td><td>Fisher et al. (1981) [9]</td></tr><tr><td rowspan="3">Scheduling</td><td>- n|m weighted tardiness</td><td>Pseudo polynomial DP</td><td>Fisher (1973) [12]</td></tr><tr><td>- 1 machine tardiness</td><td>Pseudo polynomial DP</td><td>Fisher (1976) [11]</td></tr><tr><td>- Unit commitment</td><td>Pseudo polynomial DP</td><td>Muckstadt (1977) [30]</td></tr><tr><td>Traveling salesman</td><td>- Symmetric</td><td>Spanning Tree Perfect 2-Matching</td><td>Held et al. (1970) [19]; Balas et al. (1976) [2]</td></tr></table>

![](/api/attachments/VKDFCQ9Q/fulltext/images/30210e247a37e50fbfeb8e23dec39ffb11e309a7ab08999fc57b7562ddfffe4e.jpg)

<table><tr><td colspan="2">(RULE 0_1_knapsack_structure</td></tr><tr><td>[RULE_GROUP MODEL]</td><td>; meta-rule about rule group</td></tr><tr><td>[PRIORITY 1]</td><td>; meta-rule about priority</td></tr><tr><td>IF (IS CONSTRAINT.DISTINCTIVENESS &#x27;capacity)</td><td></td></tr><tr><td>THEN (IS EMBEDDED_STRUCTURE &#x27;0_1_knapsack))</td><td></td></tr><tr><td colspan="2">(RULE capacity_constraint</td></tr><tr><td colspan="2">[RULE_GROUP CONSTRAINT]</td></tr><tr><td>IF (IS BOT.DISTINCTIVENESS OF RHS &#x27;nonnegative_real_coefficient)</td><td></td></tr><tr><td>AND (IS BOT.DISTINCTIVENESS OF LHS &#x27;volume_sum_0_1)</td><td></td></tr><tr><td>AND (IS OPERATOR &#x27;LE)</td><td></td></tr><tr><td>THEN (IS DISTINCTIVENESS &#x27;capacity))</td><td></td></tr><tr><td colspan="2">(RULE volume_sum_0_1_BOT</td></tr><tr><td colspan="2">[RULE_GROUP BOT]</td></tr><tr><td>IF (IS DISTINCTIVENESS OF ATTRIBUTE (&#x27;nonnegative_real_coefficient &#x27;0_1_integer_variable))</td><td></td></tr><tr><td>THEN (IS DISTINCTIVENESS &#x27;volume_sum_0_1))</td><td></td></tr><tr><td colspan="2">(RULE nonnegative_real_coefficient_BOT</td></tr><tr><td colspan="2">[RULE_GROUP BOT]</td></tr><tr><td>IF (IS DISTINCTIVENESS OF ATTRIBUTE &#x27;nonnegative)</td><td></td></tr><tr><td>THEN (IS DISTINCTIVENESS &#x27;nonnegative_real_coefficient))</td><td></td></tr></table>

Fig. 6. Illustrative rules associated with 0\_1\_Knapsack Structure in the UNIK-BWD syntax.

pointed objects, distinctivenesses are asked in the top down fashion. So if the distinctiveness of an object is not known, ask the conditions necessary for the identification described in the lower level objects. This approach may stop when a first structure is found. In UNIK-RELAX, this approach can be implemented using a backward chaining tool like UNIK-BWD [28]. In Fig. 6, illustrative rules for the identification of 0\_1\_Knapsack structure are represented in the UNIK-BWD syntax.

## 4.4. Case-based approach

In Section 2, we have mentioned that typical NP-hard problems such as the generalized assignment problem can be effectively relaxed. The relationships between the types of NP-hard problems and adequate Lagrangian problems are listed in Table 3 [9].

Fig. 7. Illustrative rules that relaxes Generalized Assignment Problem to 0\_1\_Knapsack Problem in the UNIK-BWD syntax.

To apply this approach, we need to identify the structure of model per se either by bottom-up or by top-down approach. However, the structural information about the model might have been provided by the user or knowledge engineer beforehand. In this case, the distinctivenesses of associated constraints, BOTs, and variables and coefficients need to be identified in a top-down manner to relax the problem to a Lagrangian problem. Fig. 7 shows an illustrative rule that relaxes the generalized assignment problem to 0\_1\_Knapsack problem in the UNIK-BWD syntax. For the example in Fig. 3, the structure of problem is identified as generalized assignment problem and is suggested to be relaxed to the 0\_1\_Knapsack problem. Note that this result is the same as the one by the embedded structural approach.

## 4.5. Integration of three approaches

The above three approaches - bottom-up, top-down, and case-based approaches - can be integrated as the procedure in Fig. 8. If the structural information of the model per se is given, the case-based approach can be the most efficient way of generating the relaxed problem. If the structural information about the model per se is not known but the embedded structural information is given, the top-down approach can be more efficient than the bottom-up approach.

![](/api/attachments/VKDFCQ9Q/fulltext/images/7ad2e23b652223fe2947888c4afa25924a9521d21c49da25ab60ab1758c955cf.jpg)  
Fig. 8. Integration of three approaches.

## 5. Relaxation to Lagrangian problems

After having identified embedded structure in the model (or structure of the model per se), UNIK-RELAX relaxes the problem to a Lagrangian problem as described in Section 2. The relaxation can be performed by the following five steps. The relaxed Lagrangian problem of the generalized assignment problem in Fig. 2 is a 0\_1\_Knapsack problem as shown in Fig. 9. Note the added BOTs and modified constants by the multipliers are in shades, while the eliminated ones are in the solid rectangles.

![](/api/attachments/VKDFCQ9Q/fulltext/images/30056ea58bcfd165639979fc36d2167fb4e3c47dab32ba41404b90b7251c61fb.jpg)  
Fig. 9. Relaxed Lagrangian problem.

Let us examine these steps with the plant assignment problem shown in Fig. 3.

Step 1. Identify the constraint objects to be relaxed.

\- If the embedded structure is one of structures #1–5 in Table 1, select the constraints not associated with the structure.

\- If the embedded structure is structure #6 in Table 1, select the constraints associated with the structure.

\- If the embedded structure is structure #7 in Table 1, select the constraints concerned with unbounded variables.

[Example]

The plant assignment problem has the embedded structure #1 (i.e. 0\_1\_Knapsack).

Relax the constraints not associated with 0\_1\_Knapsack, which is plant\_assignment\_constraint.

Step 2. Generate new attribute for Lagrangian multipliers in the lambda objects.

For the generation of lambda coefficients, apply the following rules [12]:

IF OPERATOR of relaxed constraint is EQ,

THEN DISTINCTIVENESS of lambda object is real.

IF OPERATOR of relaxed constraint is LE,

THEN DISTINCTIVENESS of lambda object is nonnegative.

IF OPERATOR of relaxed constraint is GE,

THEN DISTINCTIVENESS of lambda object is nonpositive.

[Example]

The lambda object is illustrated in (4) of Fig. 9.

Step 3. Generate new BOTs that incorporate the Lagrangian multipliers in the coefficients. [Example]

The new BOTs are illustrated in (2) and (3) of Fig. 9.

Step 4. Add the Lagrangian BOTs to the OBJECTIVE of the IP-model object.

[Example]

The added BOTs are illustrated in (1) of Fig. 9.

In this example, the constraint plant\_assignment\_constraint and its exclusively associated BOTs - plant\_choice and one BOTs - are eliminated from the Fig. 3.

## 6. Conclusion

To implement the automatic identification of embedded structures and generation of Lagrangian problem, we develop a system UNIK-RELAX. The overall architecture of UNIK-RELAX is depicted in Fig. 10. Beside the key processors – ‘Structural Identification’ and ‘Lagrangian Problem Generation’ – explained in the earlier sections, the Solver Controller generates the adequate numbers for the Lagrangian multipliers and associates the primal solution algorithm (Branch and Bound) with the computed bounds by the Lagrangian problems.

![](/api/attachments/VKDFCQ9Q/fulltext/images/498e566caadc5f50e1d01712d6546155cdfd110e816587ecd5b9b9e84f52f9d8.jpg)  
Fig. 10. Architecture of UNIK-RELAX environment.

A prototype of UNIK-RELAX is developed using the UNIK environment. The relevant capabilities employed from UNIK are objects (UNIK-OBJECT), forward chaining (UNIK-FWD) and backward chaining (UNIK-BWD) reasoning, and linear (UNIK-LP) and integer programming (UNIK-IP) model representation and formulation aid [23].

This research has shown that the automatic identification of the typical embedded structures in the computationally complex integer programming models and the automatic transformation of the model to a relaxed Lagrangian problem can be accomplished. This work should contribute to the research toward the general purpose automatic generation of solution procedure based on the characteristics of the problem.

## Acknowledgements

This research is dedicated to my most respectable professor Marshall L. Fisher, who has taught me the world of complexity while I was a doctoral student under his supervision. – Jae K. Lee.

## References

[1] V. Aggarwal, A Lagrangian relaxation method for the constrained assignment problem, Computers and Operations Research, 12 (1995).

[2] E. Balas and N. Christofides, Talk presented at the Ninth International Symposium on Mathematical Programming, Budapest (August, 1976).

[3] M.S. Bazaraa and J.J. Goode, The traveling salesman problem: A duality approach, Mathematical Programming, 13 (1977).

[4] C.A. Burdet and E.L. Johnson, A subadditive approach to solve linear integer programs, Annals of Discrete Mathematics, 1 (1977).

[5] L.G. Chalmet and L.F. Gelders, Lagrangian relaxation for generalized assignment problem, Proc. Second European Congress on Operations Research (Amsterdam, North-Holland, 1976).

[6] G. Cornuejols, M. L. Fisher, and G. L. Nemhauser, Location of bank accounts to optimize float: An analytic study of exact and approximate algorithms, Management Science, 23 (1977).

[7] J. Etcheberry, The set-covering problem: A new implicit enumeration algorithm, Operations Research, 21 (1977).

[8] J. Etcheberry, C. Conca, and E. Stacchetti, An implicit enumeration approach for integer programming using subgradient optimization, Pub. No. 78/04/c, Universidad de Chile (March, 1978).

[9] M.L. Fisher, The Lagrangean relaxation method for solving integer programming problems, Management Science, 27(1) (1981).

[10] M.L. Fisher, A dual algorithm for the one-machine scheduling problem, Mathematical Programming, 11 (1976).

[11] M.L. Fisher, Optimal solution of scheduling problems using Lagrange multipliers: Part I, Operations Research, 21 (1973).

[12] M.L. Fisher and D.S. Hochbaum, Database location in computer networks, Journal of the Association for Computing Machinery (1981).

[13] M.L. Fisher, R. Jaikumar, and L. Wassenhove, A Multiplier adjustment method for the generalized assignment problem, Decision Sciences Working Paper, University of Pennsylvania (May 1980).

[14] M.L. Fisher, G.L. Nemhauser, and L.A. Wolsey, An analysis of approximation for finding a maximum weight Hamiltonian circuit, Operations Research, 27 (1979).

[15] M.L. Fisher and J.F. Shapiro, Constructive duality in integer programming, SIAM Journal of Applied Mathematics, 27 (1974).

[16] C.O. Fong and M.R. Rao, Capacity expansion with two producing regions and concave costs, Management Science, 22 (1975).

[17] A.M. Geoffrion, The formal aspects of structured modeling, Operations Research 37(1) (1989).

[18] A.M. Geoffrion and R. Mcbride, Lagrangian relaxation applied to capacitated facility location problems, AIIE Transactions, 10 (1978)

[19] M. Held and R.M. Karp, The traveling-salesman problem and minimum spanning trees, Operations Research, 18 (1970)

[20] Wooju Kim and Jae K. Lee, UNIK-OPT/NN: Neural network-based adaptive optimal controller on the optimization models, Decision Support Systems (1995).

[21] R. Krishnan, PDM: A knowledge-based tools for model construction, Proceedings of the 22nd Hawaii International Conference on System Science, Vol. 3, pp. 467–474 (1989)

[22] R. Krishnan, X. Li, and D. Steier, A knowledge-based mathematical model formulation system, Communications of the ACM 35(9) (1992).

[23] Jae K. Lee, Integration and competition of AI with quantitative methods for decision support, Expert Systems with Applications 1 (1990).

[24] Jae K. Lee and M.Y. Kim, Knowledge-assisted optimization model formulation: UNIK-OPT, Decision Support Systems 13 (1995).

[25] Jae K. Lee. and S.B. Kwon, ES\*: An expert systems development planner using a constraint and rule-based approach, Expert Systems with Applications 9(1) (1995).

[26] Jae K. Lee. and Y.U. Song, Unification of linear programming with a rule-based system by the post-model analysis approach, Management Science 41(9) (1995).

[27] Jae K. Lee. and Y.U. Song, UNIK-PMA: A unifier of optimization model with rule-based systems by post-model analysis, Annals of Operation Research (1995).

[28] Jae K. Lee. et al., UNIK User Manual, Intelligent Information System Laboratory in Korea Advanced Institute of Science and Technology, Seoul (1994).

[29] T.P. Liang, Development of a knowledge-based model management system, Operations Research 36(6) (1988).

[30] J.A. Muckstadt and S.A. Koenig, An application of Lagrangian relaxation to scheduling in power generation systems, Operations Research, 25 (1977)

[31] F.H. Murphy, E.A. Stohr, and P. Ma, Composite rules for building linear programming models from component models, Management Science 38(7) (1992).

[32] G.L. Nemhauser and G. Weber, Optimal set partitioning matchings and Lagrangian duality, ORSA/TIMS Meeting, (1978).

[33] Kuhn Yeom and Jae K. Lee, Logical representation of integer programming models, Decision Support Systems (1995).

![](/api/attachments/VKDFCQ9Q/fulltext/images/67c66a9126b56547fe03b3a1e39cde1908765a6a94c87ed0e4a0dfc073387816.jpg)

Jae Kyu Lee is a professor of Management Information Systems at Korea Advanced Institute of Science and Technology. He received a B.A. from Seoul National University, an M.S. from the Korea Advanced Institute of Science and Technology (KAIST), and a Ph.D. from the Wharton School, University of Pennsylvania. He has authored several books on expert systems, and published numerous papers in journals including Management Science, Decision Support Systems, Expert Systems with Applications: An International Journal, Decision Sciences, Fuzzy Sets and Systems, and International Journal of Man-Machine Studies. Currently, he is an editorial member of the journals Decision Support Systems, Expert Systems with Applications: An International Journal, International Journal of Intelligent Systems in Accounting, Finance and Management, and New Review of Applied Expert Systems.

![](/api/attachments/VKDFCQ9Q/fulltext/images/ebf3dd0dec58584769a9842fa9faa21126f88e20ded3fcc658c94dc5a293d770.jpg)

Chulsoo Kim is a professor of school of Business Administration at Wonkwang University. He received a B.A. from Korea University, an M.S. in Management Science from KAIST, and a Ph.D. in Management Information Systems from KAIST. His research interests include integration of model management systems and OR heuristic algorithms, implementation of expert systems in the scheduling problem, design of distributed knowledge-bases for organizational decision making, and artificial intelligence applications to the design of communication networks.
