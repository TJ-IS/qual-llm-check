---
otero_id: 21415
otero_key: "99XDGNZA"
title: "Logical representation of integer programming models"
authors: "Kuhn Yeom; Jae Kyu Lee"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)80002-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Logical representation of integer programming models

Kuhn Yeom $^{a}$ , Jae Kyu Lee $^{b,*}$

$^{a}$ Department of Business Administration, Hanshin University, 411, Yangsandong, Osan, Kyunggido, 447-791, Korea $^{b}$ Department of Management Information Systems, Korea Advanced Institute of Science and Technology, 207-43, Cheongryang, Seoul, 130-012, Korea

Received 15 January 1994; revised 20 June 1994; 2 September 1995

## Abstract

From the formulation point of view, the Integer Programming (IP) formulation is no more than indicating some decision variables in a Linear Programming model to integer variables. Nevertheless, the interpretation as well as formulation of the IP model is not an easy task at all, because the model has implicit logical meanings in some of the variables and constraints. To explicitly represent the formulation of an integer programming model, eleven logical operators are identified. So the model formulated at this level is called the Logical Integer Programming model. To formalize the transformation process of the model to the solvable conventional integer programming model (called Base Level Integer Programming model), a series of theorems are derived. This approach is implemented on the system UNIK-IP. UNIK-IP opens a single threaded interface of optimization models with the rule based systems which imply the AND/OR relationships.

Keywords: Knowledge assisted formulation; Integer programming; Model management system; UNIK; Unified programming; High level expression

## 1. Introduction

In the research area of model management systems, the representation of complex problems in an easy way has been a long-lasting concern along with the identification of a suitable solution method for a particular problem. Without an effective aid of the formulation process, it is difficult to narrow the gap between the model builders and the decision makers. This has been unfortunately so with optimization modeling. To reduce the gap between them, the knowledge-assisted formulation aid for optimization is attempted $[7,15,18]$ . UNIK-LP (UNIfied Knowledge system for Linear Programming) is a system developed in such an effort, focusing on linear programming (LP). UNIK-LP represents the LP model in objects of a specific model, constraints, Blocks Of Terms (BOTs: a paired constant and variable that share the same summation sign), variables and constants. The beauty of UNIK-LP is the object-oriented semantic representation which can be transformed into a mathematical notational form, and in turn a tabular form to be solved by a solver such as the simplex algorithm.

As a next step in the line of this research, we attempt to aid the formulation of integer programming (IP) models and develop a system UNIK-IP. From the formulated model's point of view, IP is no more than having some of the decision variables identified as 0, 1 or integer. However, the interpretation as well as formulation of the IP model is not an easy task at all, because the model has implicit logical meanings in some of the variables and constraints. For instance, the variables may have a XOR relationship (eXclusive OR) and the constraints may have IF-THEN and AND/OR relationships. However, in IP models there is no other way but to represent these relationships by identifying certain variables as integer and adding constraints; the so called technical constraints [2,5]. Since the transformation of a logical relationship to an IP formulation is very difficult even for IP experts, supporting the transformation process is very important. Jeroslow [12] acknowledged this issue by saying that exploration of automatic transformation of a user description to a formal mixed integer programming is one of the most challenging problems.

This research attempts to provide model builders with an intuitive language – namely high level representation – using typical logical operators that can be used for the IP formulation: XOR, FIXED-CHARGE, EITHER-OR, OR, k-FOLD, AND/OR, and IF-THEN operators. Our next concern is how to transform such a high level formulation to a base level – the IP model represented as an extension of a LP form with some or all of the variables identified as 0, 1 or integer. The base level semantic representation by UNIK-IP can be automatically transformed to the mathematical and tabular forms which can be solved by a general purpose solver like the Branch and Bound algorithm.

The third concern is a compression methodology for good formulation. Prior to transformation to base level, it is necessary to compress toward a more efficient IP model if possible. For this, we establish a series of compression rules through which we can generate more efficient formulations.

To fulfill the goal of this research, we organize the remaining sections as follows. Section 2 shows the characteristics of high level representation of UNIK-IP in comparison with the base level representation. Section 3 proposes key logical operators necessary for IP formulation. Section 4 describes the transformation procedure to base level, and Section 5 describes the composite transformation procedure to base level with compression rules. Section 6 concludes with the contributions and potential benefits in integrating the optimization model with the rule base.

## 2. High level vs. base level representations of IP models

## 2.1. Representation of UNIK-LP

To explain UNIK-IP, let us briefly review the representation of UNIK-LP first. The example in Eqs. (1)-(4) is a well-known production planning model [18], which seeks the maximization of profit subject to 'plant capacity' and 'balance among production, sales and inventory amount' constraints for a certain period.

## (1) Definition of variables and coefficients

## Decision variables

$X_{ij}$ : production amount of product $i$ from plant $j$ ,

$I_{i}$ : ending inventory of product i.

## Coefficients

$a_{ij}$ : processing time to produce a unit of product $i$ from plant $j$ .

$b_{j}$ : production capacity of plant j,

$p_i$ : price of product $i$ ,

$I_{i}^{o}$ : beginning inventory of product i,

$s_i$ : sales quantity of product $i$ ,

$c_{ij}$ : unit cost of product $i$ from plant $j$ ,

$d_{j}$ : a fixed charge for opening plant $j$ .

## (2) LP model for production planning

Objective function: Maximize total\_profit = total\_revenue-total\_cost

Maximize $\sum_{i}\sum_{j}p_{i}X_{ij} - \sum_{i}\sum_{j}c_{ij}X_{ij}$

(1)

Constraints:

(1) plant\_capacity

$$
\sum_ {i} a _ {i j} X _ {i j} \leq b _ {j} \quad \forall j.\tag{2}
$$

(2) production\_sales\_inventory\_balance

$$
\sum_ {j} X _ {i j} + I _ {i} ^ {o} = s _ {i} + I _ {i} \quad \forall i.\tag{3}
$$

(3) Non-negativity condition

$$
X _ {i j}, I _ {i} \geq 0 \quad \forall i, j.\tag{4}
$$

According to UNIK-LP, the model in Eqs. (1)-(4) is represented by one LP\_MODEL, two CONSTRAINTs, eight BOTs, two VARIABLES, six CONSTANTS, and two INDEXes objects as shown in Fig. 1. Let us call this representation a base level representation in a sense that an IP model can be formulated by simply identifying the TYPE slots of decision variables as 0, 1 or integer.

## 2.2. High level representation of UNIK-IP

Suppose that new fixed charges for opening new plants should be considered additionally in the cost term of the objective function (Eq. (1)). The objective function (Eq. (1)) should be modified to Eq. (5).

Maximize

where

$$
\left. \begin{array}{l l} \sum_ {i} \sum_ {j} p _ {i} X _ {i j} - \sum_ {j} f _ {j} (X _ {i j}), & \\ f _ {j} (X _ {i j}) = \left\{ \begin{array}{l l} d _ {j} + \sum_ {i} c _ {i j} X _ {i j} & \text { if } \sum_ {i} X _ {i j} > 0 \forall j \\ 0 & \text { otherwise } \end{array} \right. \end{array} \right\}.\tag{5}
$$

The model denoted in Eq. (5) and Eqs. (2)-(4) is obviously easy to understand from the representational point of view, although not understandable by IP solvers. In this sense, this representation is called high level. This model should be transformed to the base level as shown in Eqs. (6)-(11), to be solved by a general purpose solver like the Branch and Bound algorithm.

$$
\text { Maximize } \sum_ {i} \sum_ {j} p _ {i} X _ {i j} - \sum_ {j} \left(d _ {j} Y _ {j} + \sum_ {i} c _ {i j} X _ {i j}\right),\tag{6}
$$

subject to

$$
\sum_ {i} a _ {i j} \cdot X _ {i j} \leq b _ {j} \quad \forall j,\tag{7}
$$

$$
\sum_ {j} X _ {i j} + I _ {i} ^ {o} = s _ {i} + I _ {i} \quad \forall i,\tag{8}
$$

$$
\sum_ {i} X _ {i j} \leq M _ {j} \cdot Y _ {j} \quad \forall j,\tag{9}
$$

$$
Y _ {j} \in \{0, 1 \} \quad \forall j,\tag{10}
$$

$$
X _ {i j}, I _ {i} \geq 0 \quad \forall i, j,\tag{11}
$$

where M is a large number and $Y_{j}$ 's are 0-1 variables.

<table><tr><td colspan="3">{{production_planning_problem_modelIS-A:LP_MODELDIRECTION:MAXOBJECTIVE:(+ revenue_BOT)(- variable_cost_BOT)CONSTRAINT:plant_capacityproduction_sales_inventory_balanceBOT:processing_time_BOT plant_capacity_BOT production_amount_BOT beginning_inventory_BOTSales_amount_BOT inventory_amount_BOT revenue_BOT variable_cost_BOTATTRIBUTE:production_amount sales_amount inventory_amount processing_time beginning_inventoryunit_price plant_capacity unit_variable_cost sales_amountINDEX:product plant }}</td></tr><tr><td colspan="3">{{plant_capacity{{production_sales_inventory_balanceIS-A:CONSTRAINTOPERATOR:LE OPERATOR:EQLHS:(+ processing_time_BOT)LHS:(+ production_amount_BOT)(+ beginning_inventory_BOT)RHS:(+ plant_capacity_BOT)RHS:(+ sales_amount_BOT)(+ inventory_amount_BOT)UNIT_INDEX:plant }}UNIT_INDEX:product }}</td></tr><tr><td>{{production_amount_BOT{{processing_time_BOT{{inventory_amount_BOTIS-A:BOT IS-A:BOTATTRIBUTE:one production_amount production_amount inventory_amountSUMMATION_INDEX:product }}{{plant_capacity_BOT{{revenue_BOT{{sales_amount_BOTIS-A:BOTATTRIBUTE:one plant_capacity production_amountsummation_INDEX:plant }}}{{variable_cost_BOT{{beginning_inventory_BOTIS-A:BOTATTRIBUTE:unit_variable_cost production_amount beginning_inventorySUMMATION_INDEX:product plant }}}</td><td>{{revenue_BOT{{sales_amount_BOTIS-A:BOTATTRIBUTE:unit_price production_amountsummation_INDEX:plant }}}{{beginning_inventory_BOTIS-A:BOTATTRIBUTE:one beginning_inventorySUMMATION_INDEX:}}</td><td></td></tr><tr><td>{{production_amount{{inventory_amountIS-A:VARIABLEIS-A:VARIABLESYMBOL:X SYMBOL:ITYPE:REALLINKED_INDEX:product plant }}</td><td>{{beginning_inventory{{unit_priceIS-A:CONSTANTSYMBOL:Io SYMBOL:pLINKED_INDEX:product }}</td><td>{{unit_priceIS-A:CONSTANTSYMBOL:pLINKED_INDEX:product }}</td></tr><tr><td>{{processing_time{{beginning_inventory{{unit_priceIS-A:CONSTANTSYMBOL:a SYMBOL:Io SYMBOL:pLINKED_INDEX:product plant }}}</td><td>{{unit_variable_cost{{sales_amountIS-A:CONSTANTSYMBOL:cLINKED_INDEX:product plant }}</td><td>{{unit_variable_cost{{unit_variable_costSYMBOL:pLINKED_INDEX:product plant }}}</td></tr><tr><td>{{product{{plantIS-A:INDEXIS-A:INDEXSYMBOL:i SYMBOL:jLINKED_ATTRIBUTE:production_amount inventory }}}</td><td>{{product{{plantIS-A:INDEXSYMBOL:jLINKED_ATTRIBUTE:production_amount inventory }}}</td><td></td></tr></table>

Fig. 1. Base level representation of the LP model.

![](/api/attachments/99XDGNZA/fulltext/images/88fdeec6d6bcd55c36d0611f6c75d5d8d4a6be02d895d6fc0a03c6f026782826.jpg)  
Fig. 2. High level representation of the FIXED-CHARGE term.

Note that the objective function (Eq. (5)) is transformed to the objective function (Eq. (6)) and two added technical constraints in Eq. (9) and Eq. (10).

Fig. 2 semantically shows the high level representation of Eq. (5), while Fig. 3 shows the base level representation of Eqs. (6)–(11). The changed slots in HIGH-IP are highlighted in shades. In Fig. 2, the fixed charge term in Eq. (5) is represented in the HIGH-IP slot of variable\_cost\_BOT as FIXED-CHARGE(fixed\_cost, production\_amount). What UNIK-IP has to provide is the capability of high level representation to model builders, and its automatic transformation to base level representation.

## 3. Logical operators for high level representation of IP models

Now we need to define the logical operators which are necessary to represent IP models. For this purpose, we have comprehensively surveyed the literature about the IP formulations. It seems that the logical operators AND, k-FOLD, at\_least, at\_most, NOT, Binary, XOR, OR, EITHER-OR, IF-THEN, FIXED-CHARGE are sufficient for the formulation of IP models known in the literature. However, if some other additional operators are needed in the future, they can be added modularly in the same manner.

The operators can be classified into several levels depending upon their transformability to base level. The operator is called primitive if it can be directly transformed to the base level. The operator is called derivable primitive if it is one-to-one transformable to a primitive operator, although the form is more familiar to users than the primitive operator. The operator is called the composite if it is implicitly composed of the multiple primitive operators.

Let us define each type of operators one by one.

## 3.1. Primitive logical operators

Primitive logical operator can be further classified depending upon whether it is associated with constraints or variables.

## (1) Primitive logical operators for constraints

\- AND(constraint\_list): common AND relationships among constraints.

\- At\_Least\_⟨k⟩\_Constraint\_⟨m⟩(constraint\_list): at least k constraints among m constraints must be satisfied (Short form notation: L⟨k⟩C⟨m⟩).

![](/api/attachments/99XDGNZA/fulltext/images/e1d8de67f3bd1f6cee229f8eeb573b5639316c6098305f362c946aecde010222.jpg)  
Fig. 3. Base level representation of the integer programming model with the FIXED-CHARGE term.

\- $\langle k\rangle$ -Constraint\_ $\langle m\rangle$ (constraint\_list): exactly $k$ constraints among $m$ constraints must be satisfied (Short form notation: $\langle k\rangle C\langle m\rangle$ ).

\- $NOT(a\_constraint)$ : complement of the constraint;

For example, $\text{NOT}(f(X) \leq 0) = (f(X) > 0)$ .

• FIXED-CHARGE(d, X): add the fixed cost d if X > 0.

## (2) Primitive logical operators for variables

\- At\_Least\_⟨k⟩\_One\_⟨m⟩(binary\_variable\_list): set at least k variables to be ones among m 0 or 1 binary variables.

\- $\langle k\rangle_{\text{One}}\langle m\rangle$ (binary\_variable\_list): set exactly $k$ variables to be ones among $m$ 0 or 1 binary variables.

\- $\text{Binary}(x)$ : set $x$ to be a binary of 0 or 1.

## 3.2. Derivable primitive logical operators

User friendly derivable primitive logical operators can be one-to-one transformed to the corresponding primitive logical operators.

\- XOR(constraint\_list) = 1\_Constraint\_⟨m⟩(constraint\_list).

\- $XOR(\text{variable\_list}) = 1\_One\_<m>$ (variable\_list).

• EITHER-OR(a\_pair\_of\_constraints)

= At\_Least\_1\_Constraint\_2(a\_pair\_of\_constraints).

\- EITHER-OR(a\_pair\_of\_variables) = At\_Least\_1\_One\_2(a\_pair\_of\_variables).

\- $OR(\text{constraint\_list}) = At\_Least\_1\_Constraint\_<m>$ (constraint\_list).

\- OR(variable\_list) = At\_Least\_1\_One\_⟨m⟩(variable\_list).

\- At\_Most\_⟨k⟩\_Constraint\_⟨m⟩(constraint\_list): at most k constraints among m constraints must be satisfied

$= NOT(At\_Least\langle k + 1\rangle\_Constraint\langle m\rangle(\text{constraint\_list}))$

\- At\_Most\_⟨k⟩\_One\_⟨m⟩(variable\_list): at most k variables among m binary variables must be ones
  = NOT(At\_Least\_⟨k+1⟩\_One\_⟨m⟩(variable\_list)).

## 3.3. Composite logical operators

The IF-THEN operator is a composite logical operator. Note that the former constraint is a premise, while the latter is a consequence.

\- IF-THEN(constraint\_A, constraint\_B) = OR (NOT(constraint\_A), constraint\_B))

= At\_Least\_1\_Constraint\_2(NOT (constraint\_A), constraint\_B)).

We can see that two primitive operators compose the IF-THEN operator.

## 4. Transformation of primitive logical operators to base level

Our next concern is the transformation of high level representation to base level formulation.

## 4.1. Transformation of at least k fold m operators

## (1) At\_Least\_ $\langle k\rangle$ \_Constraint\_ $\langle m\rangle$ Operator for constraints

The operator which requires to satisfy at least $k$ out of $m$ constraints - At\_Least\_<k>\_Constraint\_<m>(f1(X) ≤ 0, ..., f\_m(X) ≤ 0) implies the addition of the technical constraints in

Eq. (12) and Eq. (14) to the original model. Note that the constraints in the list should have the canonical form of $f_{i}(X) \leq 0$ .

$$
f _ {i} (X) \leq M \cdot Y _ {i} \quad i = 1, \dots , m,\tag{12}
$$

$$
\sum_ {i = 1} ^ {m} Y _ {i} \leq m - k,\tag{13}
$$

$$
Y _ {i} \in \{0, 1 \} \quad i = 1, \dots , m.\tag{14}
$$

In Eq. (12), $M$ means a large number. So $Y_{i} = 1$ implies that the constraint is relaxed, while $Y_{i} = 0$ means that the constraint must be satisfied. The technical constraint (Eq. (13)) imposes that at least $kY_{i}$ 's should become 0's. In UNIK-IP, the syntax of this operator is At\_Least\_<k>\_Constraint\_<m>(list\_of\_constraint\_names).

The transformation rule in Eqs. (12)-(14) can be notationally coded as Proposition 4.1. Assume that all $Y_{i}$ 's are 0-1 variables throughout this paper.

## Proposition 4.1.

$$
A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) = A N D \binom{A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m)}{\sum_ {i = 1} ^ {m} Y _ {i} \leq m - k}.
$$

Fig. 4 shows examples of the high level representation of At\_Least\_<k>\_Constraint\_<m> operator and the base level representation of Eqs. (12)-(14). In Fig. 4, the At\_Least\_<k>\_Constraint\_<m> operator is represented in the CONSTRAINT slot as “L2C3(constraint\_list)”.

## (2) At\_least\_ $\langle k\rangle$ \_One\_ $\langle m\rangle$ operator for variables

The operator which requires at least \( k \) out of \( m \) binary (0 or 1) variables to be ones - At\_Least\_<k>\_One\_<m>(Y\_1,Y\_2,\ldots,Y\_m) \) implies the addition of the technical constraints in Eq. (15).

$$
\sum_ {j = 1} ^ {m} Y _ {j} \geq k \text {   and   } Y _ {j} \in \{0, 1 \} \quad j = 1, \dots , m.\tag{15}
$$

The transformation rule in Eq. (15) can be notationally coded as Definition 4.2, and the similar at\_most relationship can be coded as Definition 4.3.

## Definition 4.2.

$$
A t \_ L e a s t \_ \langle k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \equiv \left(\sum_ {i = 1} ^ {m} Y _ {i} \geq k\right).
$$

Definition 4.3.

$$
A t \_ M o s t \_ \langle k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \equiv \left(\sum_ {i = 1} ^ {m} Y _ {i} \leq k\right).
$$

If the variables $X_1, X_2, \ldots, X_m$ in At\_Least\_<k>\_One\_<m>(X\_1, X\_2, $\ldots$ , X\_m) are real numbers, the expression implies that at least $kX_i$ 's should be potentially non-negative. So the high level expression implies the addition of the technical constraints in Eq. (16) and Eq. (18).

$$
X _ {j} \leq M \cdot Y _ {j} \quad j = 1, \dots , m,\tag{16}
$$

$$
\sum_ {j = 1} ^ {m} Y _ {j} \geq k,\tag{17}
$$

$$
Y _ {j} \in \{0, 1 \} \quad j = 1, \dots , m.\tag{18}
$$

```prolog
Corollary 4.5.
At_Most_0_One_⟨m⟩(Y_i, i = 1, ..., m) = AND(Y_i = 0, i = 1, ..., m).
Corollary 4.6.
At_Least_⟨m⟩_Constraint_⟨m⟩(f_i(X) ≤ 0, i = 1, ..., m) = AND(f_i(X) ≤ 0, i = 1, ..., m).
```

## (a) High Level Semantic Representation

```txt
{{problem_example_At_Least_2_Constraint_3
IS-A : IP_MODEL
DESCRIPTION : Logical_IP_Model
DIRECTION : ......
OBJECTIVE : ......
CONSTRAINT : L2C3(fx_gx_hx) ......
....... }}
```

## (b) Base Level Semantic Representation

![](/api/attachments/99XDGNZA/fulltext/images/7d8cbc6b627e5971818a7f6cbf9f85bd64ce76bb403233398791bef952ec4354.jpg)  
Fig. 4. A representation example of the At\_Least\_<k>\_Constraint\_<m> operator.

## (3) Logical relationships among operators

The following theorems show the equivalency among the logical operators. Transformation of the high level expression to base level requires these relations. According to Proposition 4.1 and Definition 4.3, Theorem 4.4 can be derived. Proofs for theorems are attached in Appendix A.

## Theorem 4.4.

$$
\begin{array}{l} A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A t \_ M o s t \_ \langle m - k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right) \end{array}
$$

According to the Definitions 4.2 and 4.3, Corollaries 4.5 and 4.6 can be derived.

Similarly, the transformation rule of the at\_most relationship can be notationally coded as Proposition 4.7, from which Theorem 4.8, Corollaries 4.9 and 4.10 can be derived.

Proposition 4.7.

$$
\begin{array}{l} A t \_ M o s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ \left(\sum_ {i = 1} ^ {m} Y _ {i} \geq m - k\right) \end{array} \right). \end{array}
$$

Theorem 4.8.

$$
\begin{array}{l} A t \_ M o s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A t \_ L e a s t \_ \langle m - k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right). \end{array}
$$

Corollary 4.9.

$$
A t \_ L e a s t \_ \langle m \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) = A N D (Y _ {i} = 1, i = 1, \dots , m).
$$

Corollary 4.10.

$$
A t \_ M o s t \_ 0 \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) = A N D (f _ {i} (X) > 0, i = 1, \dots , m).
$$

## 4.2. Transformation of k fold m operators

## (1) $\langle k\rangle$ \_Constraint\_ $\langle m\rangle$ operator for constraints

The operator which requires to satisfy exactly $k$ out of $m$ constraints - $\langle k \rangle$ \_Constraint\_ $\langle m \rangle (f_1(X) \leq 0, \ldots, f_m(X) \leq 0)$ implies the addition of the technical constraints (Eq. (19) and Eq. (21)).

$$
f _ {i} (X) \leq M \cdot Y _ {i}, \quad i = 1, \dots , m,\tag{19}
$$

$$
\sum_ {i = 1} ^ {m} Y _ {i} = m - k,\tag{20}
$$

$$
Y _ {i} \in \{0, 1 \} \quad i = 1, \dots , m.\tag{21}
$$

The transformation rule in Eqs. (19)-(21) can be notationally coded as Definition 4.11.

Definition 4.11.

$$
\langle k \rangle_ {-} \text {Constraint} _ {-} \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \ldots , m \big) = A N D \left( \begin{array}{l} A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \ldots , m \big) \\ \left(\sum_ {i = 1} ^ {m} Y _ {i} = m - k\right) \end{array} \right).
$$

## (2) $\langle k\rangle_{\text{One}}\langle m\rangle$ operator for variables

The operator which requires to activate exactly $k$ out of $m$ variables $-\langle k\rangle\_One\_ \langle m\rangle (Y_1,Y_2,\ldots ,Y_m)$ implies the addition of the technical constraints in Eq. (22).

$$
\sum_ {j = 1} ^ {m} Y _ {j} = k \text {   and   } Y _ {j} \in \{0, 1 \} \quad j = 1, \dots , m.\tag{22}
$$

If the variables $X_1, X_2, \ldots, X_m$ in $\langle k \rangle\_One\_ \langle m \rangle (X_1, X_2, \ldots, X_m)$ are real numbers, the expression implies $kX_i$ 's should be potentially non-negative. So the high level expression implies the addition of the technical constraints in Eq. (23) and Eq. (25).

$$
X _ {j} \leq M \cdot Y _ {j}, \quad j = 1, \dots , m,\tag{23}
$$

$$
\sum_ {j = 1} ^ {m} Y _ {j} = k,\tag{24}
$$

$$
Y _ {j} \in \{0, 1 \} \quad j = 1, \dots , m.\tag{25}
$$

The transformation rule in Eqs. (23)-(25) can be notationally coded as Definition 4.12.

Definition 4.12.

$$
\langle k \rangle_ {-} O n e _ {-} \langle m \rangle (Y _ {i}, i = 1, \dots , m) = A N D \binom{A t _ {-} L e a s t _ {-} \langle k \rangle_ {-} O n e _ {-} \langle m \rangle (Y _ {i}, i = 1, \dots , m)}{A t _ {-} M o s t _ {-} \langle k \rangle_ {-} O n e _ {-} \langle m \rangle (Y _ {i}, i = 1, \dots , m)}.
$$

(a) High Level Semantic Representation

```txt
{{problem_example_IF-THEN
IS-A : IP_MODEL DESCRIPTION : Logical_IP_Model
DIRECTION : ......
OBJECTIVE : ......
CONSTRAINT {IF-THEN(fx gx) ......
....... }}
```

(b) Base Level Semantic Representation

```txt
{{problem_example_IF-THEN
IS-A : IP_MODEL DESCRIPTION : Canonical_IP_Model
DIRECTION : ......
OBJECTIVE : ......
CONSTRAINT : L1C2(NOT(fx) gx) ......
....... }}
```

![](/api/attachments/99XDGNZA/fulltext/images/0a8a5e2b1eeb31f668e0c8e4e05f9e83b306650666773f1891640788d0bdb39a.jpg)  
Fig. 5. High level and base level example of the IF-THEN operator.

## 4.3. Transformation of FIXED-CHARGE operator

As illustrated in Section 2, the fixed cost term can be represented by the FIXED-CHARGE operator.

$$
\text { Minimize } f (X _ {j}) = \left\{ \begin{array}{l l} d _ {j} + c _ {j} X _ {j} & \text { if } X _ {j} > 0 \\ 0 & \text { otherwise. } \end{array} \right.\tag{26}
$$

In UNIK-IP, the statement in Eq. (26) can be specified by the compact operator $FIXED-CHARGE(d_{j} X_{j}) ON c_{j} X_{j}$ . The FIXED-CHARGE operator implies to transform the objective function in Eq. (26) to Eq. (27) and addition of the technical constraints in Eqs. (28) and (29).

Minimize $d_{j}Y_{j} + c_{j}X_{j}$

(27)

subject to

$$
X _ {j} \leq M \cdot Y _ {j},\tag{28}
$$

$$
Y _ {j} \in \{0, 1 \}.\tag{29}
$$

## 4.4. Transformation of IF-THEN operator

The condition-action type relationship $IF-THEN(f(X) \leq 0, g(X) \leq 0)$ can be transformed $OR(f(X) > 0, g(X) \leq 0)) = At\_Least\_1\_Constraint\_2(f(X) > 0, g(X) \leq 0)$ . So the meaning of the IF-THEN operator is the addition of the constraints in Eqs. (30)-(33).

$$
- f (X) <   M \cdot Y _ {1},\tag{30}
$$

$$
g (X) \leq M \cdot Y _ {2},\tag{31}
$$

$$
Y _ {1} + Y _ {2} \leq 2 - 1,\tag{32}
$$

$$
Y _ {j} \in \{0, 1 \} \quad j = 1, 2.\tag{33}
$$

Fig. 5 shows examples of the high level representation of the IF-THEN operator and its base level representation of Eqs. (30)-(33).

## 5. Transformation of composite expressions to base level

Using the logical operators defined in Section 3, the IP model can be formulated using friendly expressions. However, the derivable primitive and composite logical operators need to be transformed to the primitive logical operators making the model a so called canonical IP model. The next issue is the transformation of the canonical model to the base level. The transformation needs to take the following three steps:

(i) Eliminate NOT operators.

(ii) Compress toward a more efficient IP model.

(iii) Handle operators with a group of expressions.

## 5.1. Elimination of NOT operators in the canonical IP model

The following definitions, propositions and theorems describe the transformation rules necessary to eliminate NOT operators. Proofs for these theorems are attached in Appendix B.

## Definition 5.1.

$$
\begin{array}{l} N O T (f (X) \geq 0) = (f (X) <   0), N O T (f (X) \leq 0) = (f (X) > 0), \\ N O T (f (X) > 0) = (f (X) \leq 0), N O T (f (X) <   0) = (f (X) \geq 0). \end{array}
$$

According to DeMorgan's laws and Definition 5.1, the following theorems can be derived.

## Theorem 5.2.

$$
\operatorname{NOT} \left(\operatorname{OR} \left(f _ {1} (X) \leq 0, \dots , f _ {m} (X) \leq 0\right)\right) = \operatorname{AND} \left(\operatorname{NOT} \left(f _ {1} (X) \leq 0\right), \right.
$$

$$
\left. \operatorname{NOT} \left(f _ {2} (X) \leq 0\right), \dots , \operatorname{NOT} \left(f _ {m} (X) \leq 0\right)\right) = A N D \left(f _ {1} (X) > 0, f _ {2} (X) > 0, \dots , f _ {m} (X) > 0\right).
$$

Theorem 5.3.

$$
\operatorname{NOT} \left(\text {AND} \left(f _ {1} (X) \leq 0, \dots , f _ {m} (X) \leq 0\right)\right) = O R \left(\operatorname{NOT} \left(f _ {1} (X) \leq 0\right), \right.
$$

$$
\left. \operatorname{NOT} \left(f _ {2} (X) \leq 0\right), \dots , \operatorname{NOT} \left(f _ {m} (X) \leq 0\right)\right) = O R \left(f _ {1} (X) > 0, f _ {2} (X) > 0, \dots , f _ {m} (X) > 0\right).
$$

Now let us define the axiomatic relationships between at\_least and at\_most. The Definitions 5.4 and 5.5 are associated with variables, while the Definitions 5.6 and 5.7 are associated with constraints.

Definition 5.4.

$$
N O T \left(A t _ {-} \text {Most} _ {-} \langle k - 1 \rangle_ {-} \text {One} _ {-} \langle m \rangle \left(Y _ {i}, i = 1, \dots , m\right) = A t _ {-} \text {Least} _ {-} \langle k \rangle_ {-} \text {One} _ {-} \langle m \rangle \left(Y _ {i}, i = 1, \dots , m\right)\right).
$$

Definition 5.5.

$$
N O T \left(A t \_ L e a s t \_ \langle k + 1 \rangle_ {-} O n e \_ \langle m \rangle \left(Y _ {i}, i = 1, \dots , m\right) = A t \_ M o s t \_ \langle k \rangle_ {-} O n e \_ \langle m \rangle \left(Y _ {i}, i = 1, \dots , m\right)\right).
$$

Definition 5.6.

$$
\begin{array}{l} N O T \big (A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big) \big) \\ = A N D \left( \begin{array}{l} A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m \big) \\ N O T \left(\sum_ {i = 1} ^ {m} Y _ {i} \leq m - k\right) \end{array} \right). \end{array}
$$

Definition 5.7.

$$
\begin{array}{l} N O T \big (A t \_ M o s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big) \big) \\ = A N D \left( \begin{array}{l} A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m \big) \\ N O T \left(\sum_ {i = 1} ^ {m} Y _ {i} \geq m - k\right) \end{array} \right). \end{array}
$$

According to the above definitions, the Theorems 5.8 and 5.9 can be derived.

Theorem 5.8.

$$
\begin{array}{r l} & N O T \big (A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big) \big) \\ & \quad = A t \_ M o s t \_ \langle k - 1 \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big). \end{array}
$$

Theorem 5.9.

$$
\begin{array}{r l} & N O T \big (A t \_ M o s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big) \big) \\ & = A t \_ L e a s t \_ \langle k + 1 \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big). \end{array}
$$

From the Definitions 5.10 and 5.11, Theorem 5.12 can be derived. Theorem 5.12 can be used for the transformation of the $\langle k\rangle$ -Constraint $_{\langle m\rangle}$ operator associated with the NOT operator.

Definition 5.10.

$$
N O T \big (\langle k \rangle_ {-} C o n s t r a i n t _ {-} \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \ldots , m \big) \big) = A N D \binom{A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \ldots , m \big)}{N O T \left(\sum_ {i = 1} ^ {m} Y _ {i} = m - k\right)}.
$$

Definition 5.11.

$$
N O T \left(\sum_ {i = 1} ^ {m} Y _ {i} = k\right) = \left(\sum_ {i = 1} ^ {m} Y _ {i} \neq k\right) = O R \left( \begin{array}{l} \left(\sum_ {i = 1} ^ {m} Y _ {i} > k + 1\right) \\ \left(\sum_ {i = 1} ^ {m} Y _ {i} <   k - 1\right) \end{array} \right).
$$

Theorem 5.12.

$$
\begin{array}{l} N O T \big (\langle k \rangle_ {-} C o n s t r a i n t _ {-} \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big) \big) \\ = O R \left( \begin{array}{l} A t _ {-} M o s t _ {-} \langle k - 1 \rangle_ {-} C o n s t r a i n t _ {-} \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big) \\ A t _ {-} L e a s t _ {-} \langle k + 1 \rangle_ {-} C o n s t r a i n t _ {-} \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big) \end{array} \right). \end{array}
$$

Hereafter, we will assume that all NOT operators are eliminated in the canonical model.

5.2. Compression toward a more efficient IP model

The following definitions, propositions and theorems are necessary in identifying the special structures which can be compressed toward a more efficient IP model. The symbol $A \Rightarrow B$ means that A and B are logically equivalent, but B is a more efficient form than A.

Definition 5.13.

$$
A N D \left(A N D \left(f _ {i} (X) \leq 0, i = 1, \dots , k _ {1}\right), \dots , A N D \left(f _ {i} (X) \leq 0, i = k _ {s}, \dots , m\right)\right) \Rightarrow A N D \left(f _ {i} (X) \leq 0, i = 1, \dots , m\right)
$$

Definition 5.14.

$$
O R \left(O R \left(f _ {i} (X) \leq 0, i = 1, \dots , k _ {1}\right), \dots , O R \left(f _ {i} (X) \leq 0, i = k _ {s}, \dots , m\right)\right) \Rightarrow O R \left(f _ {i} (X) \leq 0, i = 1, \dots , m\right).
$$

Proposition 5.15.

$$
\begin{array}{l} 1 _ {-} \text {Constraint} _ {-} \langle k \rangle \left( \begin{array}{c} 1 _ {-} \text {One} _ {-} \langle m _ {1} \rangle (Y _ {1 j}, j = 1, \ldots , m _ {1}) \\ 1 _ {-} \text {One} _ {-} \langle m _ {2} \rangle (Y _ {2 j}, j = 1, \ldots , m _ {2}) \\ \vdots \\ 1 _ {-} \text {One} _ {-} \langle m _ {k} \rangle (Y _ {k j}, j = 1, \ldots , m _ {k}) \end{array} \right) \\ \Rightarrow 1 _ {-} \text {Ones} _ {-} \langle m _ {1} + \ldots + m _ {k} \rangle (Y _ {i j}, i = 1, \ldots , k \text {and} j = 1, \ldots , m _ {i}). \end{array}
$$

Using the Definitions 5.13–5.14 and Proposition 5.15, the following Theorems 5.16–5.21 can be derived. The proofs are attached in Appendix B.

Theorem 5.16.

$$
\begin{array}{r l} & A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} A t \_ L e a s t \_ 1 \_ O n e \_ \langle m _ {1} \rangle (Y _ {1 j}, j = 1, \dots , m _ {1}) \\ A t \_ L e a s t \_ 1 \_ O n e \_ \langle m _ {2} \rangle (Y _ {2 j}, j = 1, \dots , m _ {2}) \\ \vdots \\ A t \_ L e a s t \_ 1 \_ O n e \_ \langle m _ {k} \rangle (Y _ {k j}, j = 1, \dots , m _ {k}) \end{array} \right) \\ & \Rightarrow A t \_ L e a s t \_ 1 \_ O n e s \_ \langle m _ {1} + \dots + m _ {k} \rangle (Y _ {i j}, i = 1, \dots , k \text { and } j = 1, \dots , m _ {i}). \end{array}
$$

Lemma 5.17.

$$
\begin{array}{l} A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} A t \_ M o s t \_ \langle m _ {1} - 1 \rangle \_ O n e \_ \langle m _ {1} \rangle (Y _ {1 j}, j = 1, \dots , m _ {1}) \\ A t \_ M o s t \_ \langle m _ {2} - 1 \rangle \_ O n e \_ \langle m _ {2} \rangle (Y _ {2 j}, j = 1, \dots , m _ {2}) \\ \vdots \\ A t \_ M o s t \_ \langle m _ {k} - 1 \rangle \_ O n e \_ \langle m _ {k} \rangle (Y _ {k j}, j = 1, \dots , m _ {k}) \end{array} \right) \\ \Rightarrow A t \_ M o s t \_ \langle m _ {1} + \dots + m _ {k} - 1 \rangle \_ O n e \_ \langle m _ {1} + \dots + m _ {k} \rangle (Y _ {i j}, i = 1, \dots , k \text { and } j = 1, \dots , m _ {i}). \end{array}
$$

Theorem 5.18.

$$
A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle m _ {1} \rangle \big (f _ {1 j} (X) \leq 0, j = 1, \dots , m _ {1} \big) \\ A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle m _ {2} \rangle \big (f _ {2 j} (X) \leq 0, j = 1, \dots , m _ {2} \big) \\ \vdots \\ A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle m _ {k} \rangle \big (f _ {k j} (X) \leq 0, j = 1, \dots , m _ {k} \big) \end{array} \right)
$$

$$
\Rightarrow A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle m _ {1} + \dots + m _ {k} \rangle \left(f _ {i j} (X) \leq 0, i = 1, \dots , k \text {   and   } j = 1, \dots , m _ {i}\right).
$$

Theorem 5.19.

$$
\begin{array}{l} 1 _ {-} \text {Constraint} _ {-} \langle m _ {1} \rangle \left(f _ {1 j} (X) \leq 0, j = 1, \dots , m _ {1}\right) \\ 1 _ {-} \text {Constraint} _ {-} \langle m _ {2} \rangle \left(f _ {2 j} (X) \leq 0, j = 1, \dots , m _ {2}\right) \\ \vdots \\ 1 _ {-} \text {Constraint} _ {-} \langle m _ {k} \rangle \left(f _ {k j} (X) \leq 0, j = 1, \dots , m _ {k}\right) \\ \Rightarrow 1 _ {-} \text {Constraint} _ {-} \langle m _ {1} + \dots + m _ {k} \rangle \left(f _ {i j} (X) \leq 0, i = 1, \dots , k \text {and} j = 1, \dots , m _ {i}\right). \end{array}
$$

Theorem 5.20.

Let $k \leq m$ , then

$$
\begin{array}{l} A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ A t \_ L e a s t \_ 2 \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ \vdots \\ A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \end{array} \right) \\ \Rightarrow A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m). \end{array}
$$

Theorem 5.21.

$$
\begin{array}{l} A N D \left( \begin{array}{l} A t \_ M o s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \ldots , m \big) \\ A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \ldots , m \big) \end{array} \right) \\ \Rightarrow \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \ldots , m \big). \end{array}
$$

The current efficiency pursuing theorems may not be complete yet. As additional theorems come to be found in the future, they can be incrementally added modularly.

Example.

Let us consider the following example to illustrate the efficient model.

$$
\left( \begin{array}{c c} \text {If} & f (X) > 0 \\ \text {Then} & g (X) \leq 0 \end{array} \right) O R \left( \begin{array}{c c} \text {Either} & h (X) \leq 0 \\ \text {Or} & I (X) \leq 0 \end{array} \right).\tag{34}
$$

This logical relationship can be transformed to the canonical IP model as follows.

$$
A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ 2 \left( \begin{array}{c} A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ 2 (f (X) \leq 0, g (X) \leq 0) \\ A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ 2 (h (X) \leq 0, I (X) \leq 0) \end{array} \right).
$$

At this point, we can consider two transformation procedures. The first procedure is direct transformation to the base level using primitive transformation rules starting with the innermost operator; the second is to compress toward a more efficient model first (using Theorem 5.18 in this example), and then transform to the base level.

According to the direct transformation procedure, the expression (Eq. (34)) can be transformed to the base level formulation Eqs. (35)-(42).

$$
f (X) \leq M \cdot Y _ {1} + M \cdot Y _ {5},\tag{35}
$$

$$
g (X) \leq M \cdot Y _ {2} + M \cdot Y _ {5},\tag{36}
$$

$$
Y _ {1} + Y _ {2} \leq 1,\tag{37}
$$

$$
h (X) \leq M \cdot Y _ {3} + M \cdot Y _ {6},\tag{38}
$$

$$
I (X) \leq M \cdot Y _ {4} + M \cdot Y _ {6},\tag{39}
$$

$$
Y _ {3} + Y _ {4} \leq 1,\tag{40}
$$

$$
Y _ {5} + Y _ {6} \leq 1,\tag{41}
$$

$$
Y _ {i} \in \{0, 1 \} \quad i = 1, \dots , 6.\tag{42}
$$

However, using Theorem 5.18, the model (Eq. (34)) can be transformed to the more efficient IP model (Eq. (43)).

$$
A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ 4 (f (X) \leq 0, g (X) \leq 0, h (X) \leq 0, I (X) \leq 0).\tag{43}
$$

The model (Eq. (43)) then can be transformed to the base level using primitive transformation rules. So, the resulting formulation is Eqs. (44)-(49) which is more efficient than Eqs. (35)-(42).

$$
f (X) \leq M \cdot Y _ {1},\tag{44}
$$

$$
g (X) \leq M \cdot Y _ {2},\tag{45}
$$

$$
h (X) \leq M \cdot Y _ {3},\tag{46}
$$

$$
I (X) \leq M \cdot Y _ {4},\tag{47}
$$

$$
Y _ {1} + Y _ {2} + Y _ {3} + Y _ {4} \leq 4 - 1,\tag{48}
$$

$$
Y _ {i} \in \{0, 1 \} \quad i = 1, \dots , 4.\tag{49}
$$

## 5.3. Handling the operators with a group of expressions

When an operator has to be applied to a group of expressions, we need a special operational procedure. This kind of phenomenon typically happens when the big-M term is added to a set of constraints. The following propositions and theorems are developed for this operational procedure.

For the transformation of a group of constraints with the simple AND relationship, Proposition 5.22 implies that the big-M term should be added to the RHS (right hand side) of each constraint.

## Proposition 5.22.

$$
A N D \left(f _ {i} (X) \leq 0, i = 1, \dots , m\right) + M \cdot Y _ {a} = A N D \left(f _ {i} (X) \leq M \cdot Y _ {a}, i = 1, \dots , m\right).
$$

The Theorems 5.23 and 5.24 can be derived from Proposition 5.22 and the Definitions 4.2 and 4.3.

Theorem 5.23.

$$
A t \_ L e a s t \_ \langle k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) + M \cdot Y _ {a} = \left(\sum_ {i = 1} ^ {m} Y _ {i} \geq k - M \cdot Y _ {a}\right).
$$

Theorem 5.24.

$$
A t \_ M o s t \_ \langle k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) + M \cdot Y _ {a} = \left(\sum_ {i = 1} ^ {m} Y _ {i} \leq k + M \cdot Y _ {a}\right).
$$

In case of At\_Least\_<k>\_Constraint\_<m>, IF-THEN, and FIXED-CHARGE operators, the Propositions 5.25 and 5.27 and Theorem 5.26 can be derived in a similar manner.

## Proposition 5.25.

$$
\begin{array}{l} A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0 i = 1, \dots , m) + M \cdot Y _ {a} \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i} + M \cdot Y _ {a}, i = 1, \dots , m) \\ A t \_ M o s t \_ \langle m - k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right). \end{array}
$$

Theorem 5.26.

$$
\begin{array}{l} I F - T H E N \left( \begin{array}{l} A N D (f _ {i} (X) \leq 0, i = 1, \dots , k) \\ A N D (f _ {i} (X) \leq 0, i = k + 1, \dots , m) \end{array} \right) + M \cdot Y _ {a} \\ = A N D \left( \begin{array}{l} O R (f _ {i} (X) > - M \cdot Y _ {1} + M \cdot Y _ {a}, i = 1, \dots , k) \\ A N D (f _ {i} (X) \leq M \cdot Y _ {2} + M \cdot Y _ {a}, i = k + 1, \dots , m) \\ A t \_ M o s t \_ 1 \_ O n e s \_ 2 (Y _ {i}, i = 1, 2) \end{array} \right). \end{array}
$$

Proposition 5.27.

$$
F I X E D - C H A R G E (d, X _ {i}) + M \cdot Y _ {a} = \left\{ \begin{array}{l} \text {Minimize} d _ {i} Y _ {i} + c _ {i} X _ {i} \\ \text {s.t.} \\ X _ {i} \leq M \cdot Y _ {i} + M \cdot Y _ {a} \\ Y _ {i} \leq M \cdot (1 - Y _ {a}). \end{array} \right.
$$

As a result of above propositions and theorems, we can suggest Proposition 5.28 which can transform a group of expressions to the base level.

Proposition 5.28.

$$
\begin{array}{l} A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \binom {f _ {i} (X) \leq 0, i = 1, \ldots , m - 1} {G r o u p \_ o f \_ E x p r e s s i o n s} \\ = A N D \left( \begin{array}{c} A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \ldots , m - 1 \big) \\ G r o u p \_ o f \_ E x p r e s s i o n s + M \cdot Y _ {m} \\ A t \_ M o s t \_ \langle m - k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \ldots , m) \end{array} \right). \end{array}
$$

## 6. Conclusion

We have seen that eleven primitive logical operators can represent the integer programming models at a semantically higher level than the conventional integer programming models. A series of definitions, propositions and theorems are developed to formalize the transformation of the logical integer programming model to a solvable base level integer programming model. This idea is implemented on the system UNIK-IP. For more information about the system, see $[32]$ .

The benefit of UNIK-IP is not only the aid of an integer programming model formulation per se, but also the single threaded integration with the rule based systems that imply the AND/OR relationships among constraints and variables. Thus, UNIK-PMA $[21,22]$ which integrate the linear programming model with a rule based system is a beneficiary of UNIK-IP. Recently, a system UNIK-RELAX, which can identify and solve a complex integer program models using the Lagrangian relaxation approach is developed to aid the solution process of NP hard problems $[13]$ .

The UNIK(UNIfied Knowledge) project in the Korea Advanced Institute of Science and Technology that encompassed UNIK-LP (Knowledge assisted Linear Programming modeler), UNIK-IP (Knowledge assisted Integer Programming modeler), UNIK-RELAX (automatic relaxation of Integer Programming models), UNIK-PMA (unification of optimization with rule based systems), UNIK-CRSP (unification of constraint satisfaction problems with rules) [19], and UNIK-OPT/NN (neural network based control on optimization models) [20] should be a foundation toward the Unified Programming that seeks the boundless problem formulation and solution between Optimization and Artificial Intelligence.

## Appendix A. Proof of theorems in Section 4

Proof of Theorem 4.4.

By Proposition 4.1 and Definition 4.3,

$$
\begin{array}{l} A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ \sum_ {i = 1} ^ {m} Y _ {i} \leq m - k \end{array} \right) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A t \_ M o s t \_ \langle m - k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right). \quad \square \end{array}
$$

Proof of Corollary 4.6.

By Theorem 4.4 and Corollary 4.5,

$$
\begin{array}{r l} & A t \_ L e a s t \_ \langle m \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ & = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A t \_ M o s t \_ 0 \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right) \\ & = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A N D (Y _ {i} = 0, i = 1, \dots , m) \end{array} \right) \\ & = A N D (f _ {i} (X) \leq 0, i = 1, \dots , m). \quad \square \end{array}
$$

Proof of Theorem 4.8.

By Proposition 4.7 and Definition 4.1,

$$
\begin{array}{l} A t \_ M o s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ \sum_ {i = 1} ^ {m} Y _ {i} \geq m - k \end{array} \right) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A t \_ L e a s t \_ \langle m - k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right). \quad \square \end{array}
$$

Proof of Corollary 4.10.

By Theorem 4.8 and Corollary 4.9,

$$
\begin{array}{l} A t \_ M o s t \_ 0 \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A t \_ L e a s t \_ \langle m \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A N D (Y _ {i} = 1, i = 1, \dots , m) \end{array} \right) = A N D (N O T (f _ {i} (X) \leq 0), i = 1, \dots , m). \end{array}
$$

According to Theorem 5.2 and Definition 5.1, this is equivalent to $AND(f_i(X) > 0, i = 1, \ldots, m)$ .

## Appendix B. Proof of theorems in Section 5

Proof of Theorem 5.8.

By the Definitions 5.6, 5.4 and 4.2 and Theorem 4.8,

$$
\begin{array}{l} N O T \left(A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \left(f _ {i} (X) \leq 0, i = 1, \dots , m\right)\right) \\ = A N D \left( \begin{array}{l} A N D \left(f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m\right) \\ N O T \left(\sum_ {i = 1} ^ {m} Y _ {i} \leq m - k\right) \end{array} \right) \\ = A N D \left( \begin{array}{l} A N D \left(f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m\right) \\ \sum_ {i = 1} ^ {m} Y _ {i} \geq m - k + 1 \end{array} \right) \end{array}
$$

$$
\begin{array}{l} = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A t \_ L e a s t \_ \langle m - k + 1 \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right) \\ = A t \_ M o s t \_ \langle k - 1 \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m). \quad \square \end{array}
$$

Proof of Theorem 5.9.

By the Definitions 5.7, 5.5 and 4.3 and Theorem 4.4,

$$
\begin{array}{l} N O T \big (A t \_ M o s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big) \big) \\ = A N D \left( \begin{array}{l} A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m \big) \\ N O T \left(\sum_ {i = 1} ^ {m} Y _ {i} \geq m - k\right) \end{array} \right) = A N D \left( \begin{array}{l} A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m \big) \\ \sum_ {i = 1} ^ {m} Y _ {i} \leq m - k - 1 \end{array} \right) \\ = A N D \left( \begin{array}{l} A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m \big) \\ A t \_ M o s t \_ \langle m - k - 1 \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right) \\ = A t \_ L e a s t \_ \langle k + 1 \rangle \_ C o n s t r a i n t \_ \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m). \quad \square \end{array}
$$

Proof of Theorem 5.12.

By the Definitions 5.10 and 5.11,

$$
\begin{array}{r l} & N O T \big (\langle k \rangle_ {-} C o n s t r a i n t _ {-} \langle m \rangle \big (f _ {i} (X) \leq 0, i = 1, \dots , m \big) \big) = A N D \left( \begin{array}{l} A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m \big) \\ N O T \left(\sum_ {i = 1} ^ {m} Y _ {i} = m - k\right) \end{array} \right) \\ & = A N D \left( \begin{array}{l} A N D \big (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m \big) \\ O R \left( \begin{array}{l} \sum_ {i = 1} ^ {m} Y _ {i} \geq m - k + 1 \\ \sum_ {i = 1} ^ {m} Y _ {i} \leq m - k - 1 \end{array} \right) \end{array} \right). \end{array}
$$

From distributive laws, this is equivalent to

$$
O R \left( \begin{array}{l} A N D \left( \begin{array}{l} \left(f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m\right) \\ \sum_ {i = 1} ^ {m} Y _ {i} \geq m - k + 1 \end{array} \right) \\ A N D \left( \begin{array}{l} \left(f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m\right) \\ \sum_ {i = 1} ^ {m} Y _ {i} \leq m - k - 1 \end{array} \right) \end{array} \right).
$$

By the Propositions 4.1 and 4.7, this is equivalent to

$$
O R \binom{A t _ {-} M o s t _ {-} \langle k - 1 \rangle_ {-} C o n s t r a i n t _ {-} \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m)}{A t _ {-} L e a s t _ {-} \langle k + 1 \rangle_ {-} C o n s t r a i n t _ {-} \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m)}. \quad \square
$$

Proof of Theorem 5.16.

By Definition 5.4, Corollary 4.5 and Theorem 5.3,

$$
\begin{array}{l} A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} A t \_ L e a s t \_ 1 \_ O n e \_ \langle m _ {1} \rangle (Y _ {1 j}, j = 1, \dots , m _ {1}) \\ \vdots \\ A t \_ L e a s t \_ 1 \_ O n e \_ \langle m _ {k} \rangle (Y _ {k j}, j = 1, \dots , m _ {k}) \end{array} \right) \\ = A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} N O T (A t \_ M o s t \_ 0 \_ O n e \_ \langle m _ {1} \rangle (Y _ {1 j}, j = 1, \dots , m _ {1})) \\ \vdots \\ N O T (A t \_ M o s t \_ 0 \_ O n e \_ \langle m _ {k} \rangle (Y _ {k j}, j = 1, \dots , m _ {k})) \end{array} \right) \\ = A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} N O T (A N D (Y _ {1 j} = 0, j = 1, \dots , m _ {1})) \\ \vdots \\ N O T (A N D (Y _ {k j} = 0, j = 1, \dots , m _ {k})) \end{array} \right) \\ = A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} O R (Y _ {1 j} = 1, j = 1, \dots , m _ {1}) \\ \vdots \\ O R (Y _ {k j} = 1, j = 1, \dots , m _ {k}) \end{array} \right). \end{array}
$$

This means that at least one $Y_{i}$ among $(m_{1} + \ldots + m_{k})Y_{i}$ 's should be 1. Hence, the last expression is equivalent to

$$
A t \_ L e a s t \_ 1 \_ O n e \_ \langle m _ {1} + \dots + m _ {k} \rangle (Y _ {i j}, i = 1, \dots , k \text {   and   } j = 1, \dots , m _ {i}).
$$

Proof of Lemma 5.17.

By Definition 5.5, Corollary 4.9, and Theorem 5.3,

$$
\begin{array}{l} A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} A t \_ M o s t \_ \langle m _ {1} - 1 \rangle \_ O n e \_ \langle m _ {1} \rangle (Y _ {1 j}, j = 1, \dots , m _ {1}) \\ \vdots \\ A t \_ M o s t \_ \langle m _ {k} - 1 \rangle \_ O n e \_ \langle m _ {k} \rangle (Y _ {k j}, j = 1, \dots , m _ {k}) \end{array} \right) \\ = A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} N O T (A t \_ L e a s t \_ \langle m _ {1} \rangle \_ O n e \_ \langle m _ {1} \rangle (Y _ {1 j}, j = 1, \dots , m _ {1})) \\ \vdots \\ N O T (A t \_ L e a s t \_ \langle m _ {k} \rangle \_ O n e \_ \langle m _ {k} \rangle (Y _ {k j}, j = 1, \dots , m _ {k})) \end{array} \right) \\ = A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} N O T (A N D (Y _ {1 j} = 1, j = 1, \dots , m _ {1})) \\ \vdots \\ N O T (A N D (Y _ {k j}, j = 1, \dots , m _ {k})) \end{array} \right) \\ = A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} O R (Y _ {1 j} = 0, j = 1, \dots , m _ {1}) \\ \vdots \\ O R (Y _ {k j} = 0, j = 1, \dots , m _ {k}) \end{array} \right). \end{array}
$$

Because $At\_Least\_1\_Constraint\_ \langle k \rangle$ means an $OR$ relationship, this means that at least one $Y_i$ among $(m_1 + \ldots + m_k) Y_i$ 's should be 0. Therefore, by Definition 5.14, this is equivalent to $At\_Most\_ \langle m_1 + \ldots + m_k - 1 \rangle\_One\_ \langle m_1 + \ldots + m_k \rangle (Y_{ij}, i = 1, \ldots, k \text{ and } j = 1, \ldots, m_i)$ .

Proof of Theorem 5.18.

By Theorem 4.4,

$$
\begin{array}{l} A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{l} A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle m _ {1} \rangle (f _ {1 j} (X) \leq 0, j = 1, \dots , m _ {1}) \\ \vdots \\ A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle m _ {k} \rangle (f _ {k j} (X) \leq 0, j = 1, \dots , m _ {1}) \end{array} \right) \\ = A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{l} A N D \left( \begin{array}{l} A N D (f _ {1 j} (X) \leq M \cdot Y _ {1 j}, j = 1, \dots , m _ {1}) \\ A t \_ M o s t \_ \langle m _ {1} - 1 \rangle \_ O n e s \_ \langle m _ {1} \rangle (Y _ {1 j}, j = 1, \dots , m _ {1}) \end{array} \right) \\ \vdots \\ A N D \left( \begin{array}{l} A N D (f _ {k j} (X) \leq M \cdot Y _ {k j}, j = 1, \dots , m _ {k}) \\ A t \_ M o s t \_ \langle m _ {k} - 1 \rangle \_ O n e s \_ \langle m _ {k} \rangle (Y _ {k j}, j = 1, \dots , m _ {k}) \end{array} \right) \end{array} \right). \end{array}
$$

Since the constraint selection by the At\_Least\_1\_Constraint $\langle k\rangle$ operator depends only on the 0-1 values of $Y_{i}$ 's, the result can be derived as follows using Definition 5.13, Lemma 5.17 and Theorem 4.4.

$$
\begin{array}{l} A N D \left( \begin{array}{c} A N D \Big (f _ {1 j} (X) \leq M \cdot Y _ {1 j},   j = 1, \dots , m _ {1} \Big) \\ A N D \left( \begin{array}{c} \vdots \\ A N D \big (f _ {k j} (X) \leq M \cdot Y _ {k j},   j = 1, \dots , m _ {k} \big) \end{array} \right) \\ A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle k \rangle \left( \begin{array}{c} A t \_ M o s t \_ \langle m _ {1} - 1 \rangle \_ O n e \_ \langle m _ {1} \rangle \big (Y _ {1 j},   j = 1, \dots , m _ {1} \big) \\ \vdots \\ A t \_ M o s t \_ \langle m _ {k} - 1 \rangle \_ O n e \_ \langle m _ {k} \rangle \big (Y _ {k j},   j = 1, \dots , m _ {k} \big) \end{array} \right) \\ = A N D \left( \begin{array}{c} A N D \big (f _ {i j} (X) \leq M \cdot Y _ {i j},   i = 1, \dots , k   \text {and}   j = 1, \dots , m _ {i} \big) \\ A t \_ M o s t \_ \langle m _ {1} + \dots + m _ {k} - 1 \rangle \_ O n e \_ \langle m _ {1} + \dots + m _ {k} \rangle \\ (Y _ {i j},   i = 1, \dots , k   \text {and}   j = 1, \dots , m _ {i}) \end{array} \right) \\ = A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ \langle m _ {1} + \dots + m _ {k} \rangle \big (f _ {i j} (X) \leq 0,   i = 1, \dots , k   \text {and}   j = 1, \dots , m _ {i} \big). \end{array}
$$

Proof of Theorem 5.19.

The proof is similar to that of Theorem 5.18.

Proof of Theorem 5.20.

For $k \leq m$ , At\_Least\_1\_Constraint\_⟨m⟩(f\_i(X) ≤ 0, i = 1, ..., m) is subsumed by At\_Least\_⟨k⟩\_Constraint\_⟨m⟩(f\_i(X) ≤ 0, i = 1, ..., m). So, the result is obvious. □

Proof of Theorem 5.21.

By the Propositions 4.1 and 4.7, and the Definitions 5.13 and 4.11,

$$
\begin{array}{l} A N D \left( \begin{array}{l} A t \_ M o s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \\ A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) \end{array} \right) \\ = A N D \left( \begin{array}{l} A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ \left(\sum_ {i = 1} ^ {m} Y _ {i} \geq m - k\right) \end{array} \right) \\ A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ \left(\sum_ {i = 1} ^ {m} Y _ {i} \leq m - k\right) \end{array} \right) \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A N D \left( \begin{array}{l} \left(\sum_ {i = 1} ^ {m} Y _ {i} \leq m - k\right) \\ \left(\sum_ {i = 1} ^ {m} Y _ {i} \leq m - k\right) \end{array} \right) \\ = \langle k \rangle_ {-} C o n s t r a i n t _ {-} \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m). \end{array} \right. \\ \square
$$

Proof of Proposition 5.22.

$AND(f_{i}(X) \leq 0, i = 1, \ldots, m) + M \cdot Y_{a}$ means that all constraints in the AND relationship should be selected or not depending on the value of $Y_{a}$ . Hence, the $M \cdot Y_{a}$ term should be added to the RHS of all constraints simultaneously. $\square$

Proof of Theorem 5.23.

From Definition 4.2, $At\_Least\_ \langle k \rangle\_One\_ \langle m \rangle(Y_i, i = 1, \ldots, m) + M \cdot Y_a = AND(\sum_{i=1}^m Y_i \geq k, i = 1, \ldots, m) + M \cdot Y_a$ . This relationship means that if $Y_a = 0$ , we should consider $At\_Least\_ \langle k \rangle\_One\_ \langle m \rangle(\ldots)$ constraint; if $Y_a = 1$ , we do not. Since the result $AND(\sum_{i=1}^m Y_i \geq k - M \cdot Y_a, i = 1, \ldots, m)$ also implies this relationship, they are mutually equivalent.

Proof of Theorem 5.24.

The proof is similar to that of Theorem 5.23. $\square$

Proof of Proposition 5.25.

By Theorem 4.4,

$$
\begin{array}{l} A t \_ L e a s t \_ \langle k \rangle \_ C o n s t r a i n t \_ \langle m \rangle (f _ {i} (X) \leq 0, i = 1, \dots , m) + M \cdot Y _ {a} \\ = A N D \left( \begin{array}{l} A N D (f _ {i} (X) \leq M \cdot Y _ {i}, i = 1, \dots , m) \\ A t \_ M o s t \_ \langle m - k \rangle \_ O n e \_ \langle m \rangle (Y _ {i}, i = 1, \dots , m) \end{array} \right) + M \cdot Y _ {a}. \end{array}
$$

While $At\_Most\_ \langle m - k \rangle\_One\_ \langle m \rangle(Y_i, i = 1, \ldots, m)$ decides the selectivity of individual constraint among $(f_i(X) \leq M \cdot Y_i, i = 1, \ldots, m)$ , the $M \cdot Y_a$ term decides the selectivity of all or none of the constraints. Hence, the $M \cdot Y_a$ term should be added to the RHS of all the constraints simultaneously except the $At\_Most\_ \langle m - k \rangle\_One\_ \langle m \rangle(\ldots)$ constraint.

Proof of Theorem 5.26.

From the primitive transformation rules described in Section 4.4 and Theorem 5.3,

$$
\begin{array}{l} I F - T H E N \left( \begin{array}{l} A N D (f _ {i} (X) \leq 0, i = 1, \dots , k) \\ A N D (f _ {i} (X) \leq 0, i = k + 1, \dots , m) \end{array} \right) + M \cdot Y _ {a} \\ = A t \_ L e a s t \_ 1 \_ C o n s t r a i n t \_ 2 \left( \begin{array}{l} O R (f _ {i} (X) > 0, i = 1, \dots , k) \\ A N D (f _ {i} (X) \leq 0, i = k + 1, \dots , m) \end{array} \right) + M \cdot Y _ {a} \\ = A N D \left( \begin{array}{l} O R (f _ {i} (X) > 0, i = 1, \dots , k) + M \cdot Y _ {1} \\ A N D (f _ {i} (X) \leq 0, i = k + 1, \dots , m) + M \cdot Y _ {2} \\ A t \_ M o s t \_ 1 \_ O n e \_ 2 (Y _ {i}, i = 1, 2) \end{array} \right) + M \cdot Y _ {a}. \end{array}
$$

According to Proposition 5.22, this can be transformed to

$$
\begin{array}{l} \text {AND} \left( \begin{array}{l} O R \big (f _ {i} (X) > - M \cdot Y _ {1}, i = 1, \dots , k \big) \\ A N D \big (f _ {i} (X) \leq M \cdot Y _ {2}, i = k + 1, \dots , m \big) \\ A t \_ M o s t \_ 1 \_ O n e \_ 2 (Y _ {i}, i = 1, 2) \end{array} \right) + M \cdot Y _ {a} \\ = A N D \left( \begin{array}{l} O R \big (f _ {i} (X) > - M \cdot Y _ {1} + M \cdot Y _ {a}, i = 1, \dots , k \big) \\ A N D \big (f _ {i} (X) \leq M \cdot Y _ {2} + M \cdot Y _ {a}, i = k + 1, \dots , m \big) \\ A t \_ M o s t \_ 1 \_ O n e \_ 2 (Y _ {i}, i = 1, 2) \end{array} \right). \quad \square \end{array}
$$

Proof of Proposition 5.27.

This relationship means that if $Y_{a}=0$ , we should consider $FIXED-CHARGE(d,X_{i})$ ; if $Y_{a}=1$ , we do not. Since the result also implies this relationship, they are mutually equivalent. ☐

## References

[1] E. Balas, Disjunctive Programming and a Hierarchy of Relaxations for Discrete Optimization Problems, SIAM Journal on Algebraic and Discrete Methods 6 (1985).

[2] C. Coullard and R. Fourer, Interdependence of Methods and Representations in Design of Software for Combinatorial Optimization, Working Paper (1995).

[3] V. Dhar and N. Ranganathan, Integer Programming vs. Expert Systems: An Experimental Comparison, Communications of the ACM 33, No. 3 (March 1990).

[4] M.L. Fisher, The Lagrangian Relaxation Method for Solving Integer Programming Problems, Management Science 27, No. 1 (January 1981).

[5] R. Fourer and D.M. Gay, Expressing Special Structures in an Algebraic Modeling Language for Mathematical Programming, ORSA Journal on Computing, Vol. 7, No. 2 (1995).

[6] R.S. Garfinkel and G.L. Nemhauser, Integer Programming (John Wiley and Sons, Inc., 1972).

[7] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987).

[8] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37, No. 1 (1989a).

[9] A.M. Geoffrion, Computer-Based Modeling Environments, European Journal of Operational Research 41 (1989b).

[10] F. Glover, Future Paths for Integer Programming and Links to Artificial Intelligence, Computer and Operations Research 13, No. 5 (1986).

[11] S.Y. Huh, Modelbase Construction with Object-Oriented Constructs, Decision Sciences 24, No. 2 (1993).

[12] R.G. Jeroslow, Logic-Based Decision Support: Mixed Integer Model Formulation (Elsevier Science Publishers B.V., 1989).

[13] C.S. Kim and Jae K. Lee, Automatic Structural Identification and Lagrangian Relaxation for Integer Programming, forthcoming in Decision Support Systems (1995).

[14] R. Krishnan, Knowledge Based Aids for Model Construction, Ph.D. Thesis, The University of Texas at Austin (1987).

[15] R. Krishnan, X. Li and D. Steier, A Knowledge-Based Mathematical Model Formulation System, Communications of the ACM 35, No. 9 (1992).

[16] H.G. Lee, Constraint Logic Programming and Mixed Integer Programming, Ph.D. Candidacy Paper, The University of Texas at Austin (1992).

[17] Jae K. Lee, Integration and Competition of AI with Quantitative Methods for Decision Support, Expert Systems with Applications I (1990).

[18] Jae K. Lee and M.Y. Kim, Knowledge-Assisted Optimization Model Formulation: UNIK-OPT, Decision Support Systems 13, No. 2 (1995).

[19] Jae K. Lee and S.B. Kwon, ES\*: An Expert Systems Development Planner Using a Constraint and Rule-Based Approach, Expert Systems with Applications 9, No. 1 (1995).

[20] Jae K. Lee and W. Kim, UNIK-OPT/NN: Neural Network based Adaptive Optimal Controller on the Optimization Models, forthcoming in Decision Support Systems (1995).

[21] Jae K. Lee and Y.U. Song, Unification of Linear Programming with a Rule-Based Systems by the Post-Model Analysis Approach, Management Science 41, No. 9 (1995a).

[22] Jae K. Lee and Y.U. Song, UNIK-PMA: A Unifier of Optimization Model with Rule-Based Systems by Post-Model Analysis, forthcoming in Intelligent Systems in Accounting, Finance, and Management (1995b).

[23] J.S. Lee, A Model Base for Identifying Mathematical Programming Structures, Decision Support Systems 7 (1991).

[24] J.S. Lee, C.V. Jones and M. Guingnard, MAPNOS: Mathematical Programming Formulation Normalization System, Expert Systems with Applications 1 (1990).

[25] M. Minsky, A Framework for Representing Knowledge, in: R.J. Brachman and H.J. Levesque, Eds., Readings in Knowledge Representation (Morgan Kaufmann, 1985).

[26] F.H. Murphy, E.A. Stohr and A. Asthana, Representation Schemes for Linear Programming Models, Management Science 38, No. 7 (1992).

[27] F.H. Murphy, E.A. Stohr and P. Ma, Composite Rules for Building Linear Programming Models from Component Models, Management Science 38, No. 7 (1992).

[28] H.A. Taha, Integer Programming: Theory, Applications, and Computations (Academic Press, 1975).

[29] P. Van Hentenryck, Constraint Satisfaction in Logic Programming (The MIT Press, Cambridge, MA, 1989).

[30] Kuhn Yeom and Jae K. Lee, Knowledge-Assisted Integer Programming Formulator: UNIK-IP, Proceedings of INFORMS Los Angeles Spring 1995 National Meeting (April, 1995).

[31] Kuhn Yeom and Jae K. Lee, A Study about Higher Level Representational Aid for Integer Programming Formulation, The 1995 Fall Conference of Korea OR/MS Society (September, 1995).

[32] Kuhn Yeom and Jae K. Lee, Knowledge-Assisted Integer Programming Formulation Aid: UNIK-IP, Working Paper, KAIST (1995).

![](/api/attachments/99XDGNZA/fulltext/images/82ce27add2be8a445f4f4bc4dc58e0bc7ac71ab3c7d1167c7cecc24006b630dc.jpg)  
Kuhn Yeom is Associate Professor of Business Administration at the Hanshin University, Korea. He received his B.B.A. in Business Administration from the Seoul National University, and his M.S. in Management Science and Ph.D. in Management Information Systems from the Korea Advanced Institute of Science and Technology. His research interests include expert systems, decision support systems and artificial intelligence applications in business.

![](/api/attachments/99XDGNZA/fulltext/images/fa0653505dab278dfed55149781d2f345715aa57ede4e77faea5cc25af452549.jpg)

Jae Kyu Lee is Professor of Management Information Systems at the Korea Advanced Institute of Science and Technology. He received his B.S. from the Seoul National University, and his M.S. from the Korea Advanced Institute of Science and Technology and his Ph.D. from the Wharton School, University of Pennsylvania. He has authored several books on expert systems, and published numerous papers in the journals like Management Science, Decision Support Systems, Expert Systems with Applications: An International Journal, Decision Sciences, Fuzzy Sets and Systems, and International Journal of Man-Machine Studies. Currently, he is an editorial member of the journals Decision Support Systems, Expert Systems with Applications: An International Journal, International Journal of Intelligent Systems in Accounting, Finance and Management, and New Review of Applied Expert Systems.
