---
otero_id: 17464
otero_key: "MBMSH4H5"
title: "A constraint logic programming language keyed CLP and its applications to decision making problems in OR/MS"
authors: "Kunihiko Hiraishi"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00020-s"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A constraint logic programming language keyed CLP and its applications to decision making problems in OR/MS

Kunihiko Hiraishi

School of Information Science, Japan Advanced Institute of Science and Technology, Hokuriku 15 Asahi-dai, Tatsunokuchi, Nomi-gun, Ishikawa 923-12, Japan

## Abstract

The aim of this research is to utilize constraint logic programming (CLP) for solving decision making problems in Operations Research/Management Science. In this research, a new constraint logic programming language Keyed CLP is developed. Keyed CLP has some characteristic features for solving problems in OR/MS. Key arguments can be attached to each predicate, where each key represents the functional dependency in the predicate, and is used for improving computational efficiency and readability of programs. In addition, Keyed CLP has built-in predicates for solving linear optimization problems. To illustrate these features, several examples of decision making problems are solved by Keyed CLP.

Keywords: Constraint logic programming; Decision making; Linear programming; Constraint solving; Modelling

## 1. Introduction

The aim of this research is to utilize constraint logic programming (CLP) for solving decision making problems in the field of Operations Research/Management Science. CLP languages are a kind of constraint languages [11] based on logic programming. Several constraint logic programming languages have been proposed so far, such as CLP(R) [9], CHIP [5], CAL [1], and PrologIII [3]. In this research, a new CLP language Keyed CLP is developed. Keyed CLP is characterized by keyed predicates. Ordinary prolog-type languages do not have global variables, and therefore we sometimes need redundant evaluation of programs, and additional variables for storing calculated data. Keyed predicates work as global variables, and are effective in improving computational efficiency and readability of programs. Moreover, Keyed CLP provides users with built-in predicates for solving linear optimization problems.

We can summarize the properties of decision making problems in OR/MS as follows:

(i) Numerical constraints are contained. Moreover, they are often restricted to be linear.

(ii) Objective functions/evaluation functions are given. The aim of the problem is to optimize the values of these functions or to keep the values above some desirable levels.

(iii) Many decision variables are contained. It is not easy to determine all the values of the variables at the same time. Therefore trial and error is needed.

(iv) Table-form data (relational data) are frequently used.

CLP framework is effective for solving problems having the above features, because of the following reasons:

(i) CLP enables to handle both symbolic constraints and numerical constraints.

(ii) Query/Answer type execution of logic programming is suitable for the problem solving through trial and error.

(iii) Each predicate in CLP program can be seen as a relation, and therefore CLP is suitable for representing relational data.

(iv) Since constraint satisfaction systems are embedded in a CLP interpreter, we do not have to describe explicit procedures for solving constraints.

In addition to these features, CLP languages have an important advantage in solving problems. In procedural programming languages, inputs and outputs must be specified for each program. In CLP languages, however, inputs and outputs are exchangeable. This enables to calculate input data that yields given desirable output. We call this function bi-directional computation. These features will be described by using examples.

In the field of OR/MS, Geoffrion [7] proposed a new modelling methodology, called Structured Modelling. In this methodology, each process of problem solving is decomposed into the following phases: (1) abstract level description of the problem, (2) data for making instances of the problem description, (3) constraint solvers and (4) interfaces between solvers and problem descriptions. In CLP languages, the phase (1) corresponds to rules, and the phase (2) to facts in a CLP program. Solvers and a solver interface are embedded in the CLP interpreter. The notion of model base management has been proposed as an analogy with DBMS (e.g., [6]). A model base management system provides users with functions for storing, searching and editing models on computer systems. The CLP framework will contribute to realizing (a part of) these functions in computer systems. CLP languages work as a model description language, a relational database and a constraint solver. In addition, declarative programming and modularity of predicates will make model manipulation easier.

In Section 2, the characteristic features of

Keyed CLP are described. In Section 3, three examples are shown to demonstrate the process of solving problems by using Keyed CLP. In Section 4, the advantages of Keyed CLP are discussed.

## 2. How to represent problems by keyed CLP

In this section, we will describe the characteristic features of Keyed CLP, and will show how these features work effectively in solving problems. We assume that the reader is familiar with logic programming languages such as Prolog [2].

## 2.1. Keyed predicates

In addition to ordinary predicates, Keyed CLP has a different type of predicates, called keyed predicates, which has the form

$$
\text { Predicate - Name } (\text { Key } _ {1}, \dots , \text { Key } _ {n} \text {   Arg } _ {1}, \dots , \text { Arg } _ {m}).
$$

In logic programming languages, each predicate can be seen as a relation. The word key has the same meaning as in the relational database theory, and represents the functional dependency in the relation. Each keyed predicate corresponds to a tuple having $Key_{1},\ldots,Key_{n}$ as the key arguments. In a relation, a tuple is uniquely determined if all the values for the key arguments are specified. This property is preserved also in executing programs of Keyed CLP. Every predicate that has the same predicate name and the same values for the keyed arguments must have the same value for all the arguments. In the above predicate, if the values for key arguments $Key_{1},\ldots,Key_{n}$ are determined, then $Arg_{1},\ldots,Arg_{m}$ must have unique values.

We will show how keyed predicates work in executing programs. To do this, we use an example.

$$
\begin{array}{l} \text {Example 1.} \\ \mathrm{p(X:A).} \\ \mathrm {q(X,X+ Y) : - p(key:X), p(key:Y).} \\ |? - \mathrm{q(3,Z)}. \\ \mathrm{Z=6}. \\ ^ {* * *} \text {yes} ^ {* * *} \end{array}
$$

In Example 1, p(X: A) is a keyed predicate and the variable X is the key of this predicate. Execution of Keyed CLP programs is the same as in Prolog excepting that of keyed predicates. In the above program, q(3, Z) is evaluated first, and X = 3 and $Z = X + Y$ are extracted as constraints. Next p(key: 3) is evaluated, and then the value of predicate p having 'key' as the key value is determined as p(key: 3). Therefore, the next subgoal p(key: Y) is unified with p(key: 3), and the value of Z is obtained as $3 + 3 = 6$ . In this case, this keyed predicate works as a global variable.

In Example 1, keyed predicates keep only constants. The next example shows that keyed predicates can keep variables restricted by some numerical constraints.

$$
\begin{array}{l} \text {Example 2.} \\ \mathrm{a(1).} \\ \mathrm{a(2).} \\ \mathrm {p(X: A, B): - A > = B.} \\ \mathrm {q(Y,A1): - p(k:A,Y), a(A1), p(k:A1, _).} \\ |? - q (2, B). \\ \mathrm{B=2} \\ ^ {* * *} \text {yes} ^ {* * *} \end{array}
$$

In this example, by unifying p(k: A, 2) with p(X: A, B): -A >= B, the value of predicate p with key value k is determined as p(k: A, 2) with a numerical constraint A >= 2. The subgoal a(A1) first gets a value A1 = 1, and then p(k: 1, \_ ) fails because 1 >= 2 is not true. Next a(A1) gets a value A1 = 2, and then p(k: 2, \_ ) succeeds because 2 >= 1 is true. Therefore only B = 2 is the solution.

This mechanism of keyed predicates is effective in the following two points:

(i) improving computational efficiency by avoiding unnecessary recalculation,

(ii) improving readability of programs.

These features will be discussed in Section 4.

Next we will demonstrate how a problem is described by the Keyed CLP language, comparing with spread sheets. Spread sheets are widely recognized as a tool for modelling and problem solving on personal computers. In spread sheets, each problem is modeled on tables, and the constraints are described as a formula in each cell. Table 1 shows a simple example of spread sheet modelling.

Table 1  
An example of spread sheets

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>1</td><td>Goods</td><td>Unit price</td><td>Number</td><td>Total price</td></tr><tr><td>2</td><td>Computer</td><td>298,000</td><td>2</td><td>B2 * C2</td></tr><tr><td>3</td><td>Monitor</td><td>99,800</td><td>2</td><td>B3 * C3</td></tr><tr><td>4</td><td>Printer</td><td>324,000</td><td>1</td><td>B4 * C4</td></tr><tr><td>5</td><td>Software</td><td>86,000</td><td>2</td><td>B5 * C5</td></tr><tr><td>6</td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>Total</td><td></td><td></td><td>SUM(D2:D5)</td></tr></table>

Calculation of spread sheets is executed by substituting the value of each cell with the calculated data of the formula defined in the cell. Each cell is referred by its coordinate on the table like B3, C5. Therefore, though spread sheets have a form of tables, their topological structure as a table is not strongly reflected on modelling processes. By treating a table as a relational table, we can describe models in a more sophisticated manner.

The program in Fig. 1 is a Keyed CLP program corresponding to the spread sheet in Table 1. The values of unit price, number of purchases and payment are uniquely determined if the name of each goods is specified. Therefore, they can be expressed by keyed predicates having “goods” as the key argument. These keyed predicates correspond to the cells in the spread sheet. Executing the goal total\_payment(S), we obtain the answer.

|? - total\_payment(S).

S = 1291600

Next let us consider the problem to calculate the maximum number of computer sets we can purchase within a given payment. To do this, first

goods(computer).
goods(monitor).
goods(printer).
goods(software).

unit\_price(computer : 298000).

unit\_price(monitor : 99800).

unit\_price(printer : 324000).

unit\_price(software : 86000).

number\_of\_purchases(computer : 2).

number\_of\_purchases(monitor : 2).

number\_of\_purchases(printer : 1).

number\_of\_purchases(software : 2).

payment(G : P \* N):-

unit\_price(G : P), number\_of\_purchases(G : N).

total\_payment(S):-

sum(X, (goods(G), payment(G : X)), S).

Fig. 1. Keyed CLP program corresponding to Table 1.

we change the predicate number\_of\_purchases as follows.

number\_of\_purchases(computer: X).

number\_of\_purchases(monitor: X): -

number\_of\_purchases(computer: X).

number\_of\_purchases(software: X): -

number\_of\_purchases(computer: X).

Given a payment 2,000,000, the number of computer sets is calculated by

|? - total\_payment(2000000),

number\_of\_purchases(computer: X).

$\mathbf{X} = 3.464241$

```javascript
\*\*\* yes \*\*\*
```

Such bi-directional computation is one of the characteristic features of constraint programming.

## 2.2. Solving constraints and optimization

The most important difference between ordinary Prolog and CLP languages is that we can describe numerical constraints directly in programs. In Keyed CLP, the followings are used as numerical constraints:

Expr = Expr, Expr > = Expr,

Expr <= Expr, Expr > Expr, Expr < Expr,

where each expression Expr is composed of variables, constants, and numerical operators +, -, \* and /. Each variable in numerical constraints is defined over the domain of real numbers. In each derivation step of executing programs, the simplex method is used for verifying whether the new constraint is consistent with existing ones. When the new constraint contains a nonlinear term, the term is replaced with a variable, and the nonlinear term is separated from the linear constraint. Evaluation of nonlinear constraints is delayed until they become linear by substituting variables or by solving other constraints. When the derivation step is successful, Keyed CLP interpreter outputs the substitutions to the variables in the initial goal and remaining (linear and nonlinear) constraints. By this ability of solving numerical constraints, Keyed CLP can treat problems that contains both qualitative constraints and quantitative constraints.

Basically, Keyed CLP solves only linear constraints. However, since the target domain of Keyed CLP is in OR/MS, the linear constraint solver covers many problem areas. In addition, it is essential to handle inequalities when practical problems are considered, because each value usually has some allowable range. It is not easy to treat inequalities when we solve nonlinear constraints.

Keyed CLP also has the following higher order predicates for solving linear optimization problems.

min(Expr, Goal),

max(Expr, Goal)

where Expr is a linear formula. The predicate min (max) finds a substitution to variables which minimizes (maximizes) the value of Expr, i.e., min(Expr, Goal) (max(Expr, Goal)) is equivalent to the statement “Expr = V, Goal”, where V is the minimum (maximum) value of Expr satisfying constraints in Goal. If Goal has alternatives, then min (max) searches every optimum value for each alternative and then finds the optimum value among them. Even when the region represented by given constraints is the union of some convex areas, the predicate min (max) correctly finds the optimum solution. We demonstrate how the predicate min (max) finds the optimum value by the following example.

![](/api/attachments/MBMSH4H5/fulltext/images/cc752a2f47a7cb17c35036739c3288de13e1e43f20ebf7284a3ce7abcdba4af7.jpg)  
Fig. 2. Union of two convex sets.

Example 3.

```prolog
region(X, Y): - X >= 0, Y >= 0, X + Y <= 1.
region(X, Y): - X >= 0, X <= 2, Y >= 0,
    Y <= X
|? - max(Y, region(X, Y)).
X = 2
Y = 2
*** yes ***
```

The region represented by the predicate region(X, Y) is the union of two convex sets (Fig. 2). The predicate max finds the maximum value of Y for each region (the maximum value for the first set is Y = 2, and Y = 1 for the second set), and then takes the maximum value Y = 2.

The optimum value for previous alternatives is used as the upper (lower) bound when another alternative is evaluated. At each derivation step, if the new alternative does not generate a value which is better than the previous bound, then the derivation step stops at the step and backtracking occurs. The second argument Goal of min (max) can also contain min/max. This allows us to solve the min-max (max-min) type optimization problems. Examples of nested optimization problems will be shown in 3.3.

In addition to min and max, Keyed CLP has the following higher order predicates.

sum(Expr, Goal, Res):

Res is the resulting summation of the value

of Expr for each alternative of Goal;

avg(Expr, Goal, Res):

Res is the resulting average of the value of Expr for each alternative of Goal;

count(Goal, Res):

Res is the resulting number of alternatives of Goal; all(Goal): find all alternatives of Goal.

## 2.3. Keyed CLP interpreter

Current version of Keyed CLP interpreter is written by C language on UNIX operating system. Fig. 3 shows an overview of the system. User's queries are processed by Engine. Program control for higher order predicates and keyed predicates are also processed here. Numerical constraints are separated into linear constraints and nonlinear constraints. Linear constraints are solved by Simplex Solver. Evaluations of nonlinear constraints are delayed until they become linear. If some nonlinear constraints become linear by substitutions to variables or by solving other constraints, then they are moved to linear constraint stack. Built-in functions are processed by Built-in Function Module and their evaluations are delayed until every argument in the function becomes constant.

![](/api/attachments/MBMSH4H5/fulltext/images/8711960434c1e8fffaebebf821ceae731d3f74de3a534d6172cea6899c81727f.jpg)  
Fig. 3. Keyed CLP interpreter - system overview.

## 3. Examples of problem solving by keyed CLP

In this section, we will demonstrate three examples of solving problems by using Keyed CLP.

## 3.1. Production planning

The program in Appendix I represents a linear programming problem for production planning in a small company. The company produces four kinds of products a, b, c and d. For each product, there are three kinds of resources (material, electric power and man power) necessary for production. For each resource, an upper limit of available quantity is given. The aim of this problem is to find quantity of production for each product that maximizes the total profit and satisfies the resource constraints. In addition, there is a constraint $(\mathrm{Pb}=0;\mathrm{Pc}=0;\mathrm{Pd}=0)$ , where Pb, Pc and Pd are quantity of production for each product b, c and d, respectively. This constraint means that at least one of the three products should not be produced. Therefore, the region of feasible solution is the union of three convex sets. These sets are obtained by backtracking, and the built-in predicate max finds the optimum solution among these sets.

```txt
|? - max(S, Feasible(S, Pa, Pb, Pc, Pd)).  
S = 740  
Pa = 53.333333  
Pb = 0  
Pc = 23.333333  
Pd = 6.666667  
*** yes ***
```

We can also obtain the values of Pa \~ Pd for a given value of S.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\mid ? - \text{Feasible} (S, 37, 0, 7, 23).$ $S = 642$ $* * *$ yes $^{***}$
</div>

```c
|? - Feasible(642, Pa, Pb, Pc, Pd).
Pa = 37.000000 + 0.166667 * _136 - _138
Pb = 0
Pc = 7.000000 + 0.5 * _136 + 0.666667 * _138
Pd = 23 - 0.5 * _136 + 0.333333 * _138
_136 >= 0
12.000000 + 0.166667 * _136 - _138 >= 0
_138 >= 0
37.000000 + 0.166667 * _136 - _138 >= 0
7.000000 + 0.5 * _136 + 0.666667 * _138 >= 0
23 - 0.5 * _136 + 0.333333 * _138 >= 0
169.5 - 2.416667 * _136 - 2.166667 * _138 >= 0
147 - 2.833333 * _136 - 0.666667 * _138 >= 0
*** yes ***
```

Where each expression \_n (n is a natural number) represents an internal variable generated by the Keyed CLP interpreter. The values for Pa \~ Pd are not uniquely determined, and so the result is shown by using formulas. When we intend to know the range of these variable, we can execute the following goal.

```prolog
|? - RANGE(Pa, Feasible(642, Pa, _, _, _), L, U).
Pa = ?
L = 25 (Lower bound)
U = 54.315789 (Upper bound)
*** yes ***
where the predicate RANGE is defined as
RANGE(V, X, L, U): - min(V, X, L),
max(V, X, U).
```

## 3.2. PERT diagram

Next we consider a scheduling problem using PERT (Program Evaluation and Review Technique). The PERT diagram in Fig. 4 represents a process of manufacturing new cars [14]. The number associated with each arc is the duration of the activity. The arc from node 20 to 40 has 0 as the duration because it is a dummy arc that represents only the precedence relation. Using a PERT diagram, the earliest start time and the latest finish time are calculated for each node, and critical activities are found. The earliest start time for each activity is obtained by taking the maximum of “the earliest start time + the duration” for each of its preceding activities. The latest finish time for each activity is obtained by taking the minimum of “the latest finish time-the duration” for each of its successive activities. Using the build-in predicate max, the earliest start time and the latest finish time for each node can be easily written as follows.

![](/api/attachments/MBMSH4H5/fulltext/images/7fae38eb1f75c5010f9bade653783946d6b72aeed1ef1f0b602558388668a21b.jpg)  
Fig. 4. PERT diagram for manufacturing cars.

```txt
Earliest_Start_Time(A: Es): -
Diagram(A, N, _),
max(Es, (
Diagram(B, _, N), Duration(B: D),
Earliest_Start_Time(B: Es1),
ES = ES1 + D
)), !.
Earliest_Start_Time(A: 0).
Latest_Finish_Time(A: Lf): -
Diagram(A, _, N),
min(Lf, (
Diagram(B, N, _), Duration(B: D),
Latest_Finish_Time(B: Lf1),
Lf = Lf1 - D
)), !.
Latest_Finish_Time(A: Es + D): -
Earliest_Start_Time(A: Es),
Duration(A: D).
In this program, each predicate Diagram(a, n1, n2) means that an activity a is represented by an
```

arc from node n1 to node n2. The following is a result of the execution of the predicate time \_analysis, which calculates for each activity the earliest start time, the earliest finish time, the latest start time, the latest finish time and the total float (= latest finish time - earliest finish time).

```txt
|? - time_analysis.
Activity: Design_Engine
Earliest Start Time = 0
Earliest Finish Time = 5
Latest Start Time = 0
Latest Finish Time = 5
Total Float = 0
Activity: Design_Body
Earliest Start Time = 0
Earliest Finish Time = 4
Latest Start Time = 1
Latest Finish Time = 5
Total Float = 1
Activity: Order_Body_Metal
Earliest Start Time = 0
Earliest Finish Time = 1
Latest Start Time = 2
Latest Finish Time = 3
Total Float = 2
...
```

## 3.3. Combining qualitative and quantitative constraints

We consider a problem shown in [4]. This problem is for deciding a computer system to purchase, and is described as follows.

There are four choice sets: hardware, air-conditioning units, operating systems, and database management systems. Each alternative is defined over the set of choice-set attributes, e.g., hardware has four attributes: Cost, MIPS, Memory (M bytes) and Annual maintenance. This choice-set of hardware is written as the following Keyed CLP Program:

```c
/*
Hardware Specifications
Name: Cost(K), MIPS, Memory(M bytes),
Annual maintenance
*/
```

Hardware('DEC').

Hardware('IBM').

Hardware('CDC').

Hardware('ATT').

HW\_Spec('DEC': 300000, 5, 8, low).

HW\_Spec('IBM': 500000, 5, 8, high).

HW\_Spec('CDC': 350000, 5, 8, high).

constraints: - quantitative\_constraints,

qualitative\_constraints.

quantitative\_constraints:-

selection(: HW, AC, OS, DB, N),

HW\_Spec(HW: HWcost, HWmips,

HWmem, HWmaint),

AC\_Spec(AC: ACcost, ACpower, ACspace),

OS\_Spec(OS: OScost, OSmem),

DB\_Spec(DB: DBcost, DBmem, DBrec),

/\* Rule A1:
At least 6M bytes must be available apart from memory requirements of the operating system and the database system. \*/
HWmem - OSmem - DBmem / 1024 >= 6.0,
/\* Rule A2:
The total cost of the various information system components should not exceed \$375,000. \*/
HWcost + ACcost + OScost
+N \* DBcost <= 375000.
qualitative\_constraints:
selection( : HW, AC, OS, DB, N),
HW\_Spec(HW: HWcost, HWmips, HWmem, HWmaint),
AC\_Spec(AC: ACcost, ACpower, ACspace),
OS\_Spec(OS: OScost, OSmem),
DB\_Spec(DB: DBcost, DBmem, DBrec),
/\* Rule B1:

If IBM is selected as the hardware,

then the OS must be CMS. \*/

IF(EQ(HW, 'IBM'), EQ(OS, 'CMS')),

/\* Rule B2:

If IBM is selected as the hardware,

then the AirConditioning power must be

greater than 400 KW. \*/

IF(EQ(HW, 'IBM'), ACpower > 400),

/\* Rule B3:

If the Hardware is DEC and the OS is UNIX,

then INGRES must be selected as the DBMS. \*/

IF((EQ(HW, 'DEC'), EQ(OS, 'UNIX')),

EQ(DB, 'INGRES')),

/\* Rule B4:

If IMS is selected as the OS,

then the hardware must be IBM. \*/

IF(EQ(OS, 'IMS'), EQ(HW, 'IBM')),

/\* Rule B5:
If INGRES is selected as the DBMS,
then the hardware must not be CDC. \*/
IF(EQ(DB, 'INGRES'), NEQ(HW, 'CDC')),

/\* Rule B6:
VMS operating system should not be installed on hardware that is less than 5 MIPS. \*/
IF(HWmips < 5, NEQ(OS, 'VMS')).

Where the predicate selection is a keyed predicate with empty key that works as global variables containing selected tuple from the choice sets. As usual, the predicate IF is defined as IF(Cond, Then): - call(Cond), !, call(Then).

IF $(-,-)$ .

EQ(X,Y) succeeds when X and Y are unifiable and NEQ succeeds when X and Y are not unifiable. Feasible solutions are written as follows:

Feasible(HW, AC, OS, DB, N, TotCost,

HWmips): -

selection(: HW, AC, OS, DB, N),

constraints,

TotalCost(:TotCost),

HW\_Spec(HW: HWcost, HWmips, HWmem, HWmaint).

The following predicate go1 finds the solution that minimizes the total cost.

min(TotCost, Feasible(HW, AC, OS, DB, N,

The following predicate go2 finds the solution that maximizes MIPS value.

The aim of this problem is to find a solution optimizing both of the objectives, i.e., minimizing costs and maximizing MIPS value. We use here a technique of sequential optimization $[13]$ . In this technique, the optimum value is determined by assigning an order of evaluation among the objectives. The predicate go3 first finds solutions that maximize MIPS value, and among them finds the solution that minimizes the total cost. The predicate go4 first finds solutions that minimize the total cost, and among them finds the solution that maximizes MIPS value.

```prolog
go3: -
min(TotCost,
max(HWmips, Feasible(HW, AC, OS, DB, N,
TotCost, HWmips))
),
write_ans(HW, AC, OS, DB, N, TotCost,
HWmips, Space).
go4:-
max(HWmips,
min(TotCost, Feasible(HW, AC, OS, DB, N,
TotCost, HWmips))
),
```

write\_ans(HW, AC, OS, DB, N, TotCost,

```txt
Nesting levels of min and max are n
stricted. The followings are the results of e
ing these goals.
|? - go1.
Ans:
Hardware Maker = DEC (5 MIPS)
Air-Conditioner = Borg
Operating System = TOPS
Database Software = RIM * 1
Total Cost = 329000
*** yes ***
|? - go2.
Ans:
Hardware Maker = DEC (5 MIPS)
Air-Conditioner = Borg
Operating System = UNIX
Database Software = INGRES * _6
Total Cost = _7
_6 = 1.000000 + _24
_7 = 337000.000000 + 7000.000000 * _24
_24 >= 0
_24 <= 5.428571
*** yes ***
Retry? y
Ans:
Hardware Maker = DEC (5 MIPS)
Air-Conditioner = Borg
Operating System = TOPS
Database Software = INGRES * _6
Total Cost = _7
_6 = 1.000000 + _24
_7 = 332000.000000 + 7000.000000 * _24
_24 >= 0
_24 <= 6.142857
*** yes ***
Retry? y
...
|? - go3.
```

```ini
Ans:
Hardware Maker = DEC (5 MIPS)
Air-Conditioner = Borg
Operating System = TOPS
Database Software = RIM * 1
Total Cost = 329000
*** yes ***
| ? - go4.
Ans:
Hardware Maker = DEC (5 MIPS)
Air-Conditioner = Borg
Operating System = TOPS
Database Software = RIM * 1
Total Cost = 329000
*** yes ***
```

In the execution of go2, the number of data base software has some allowable range. This range is shown in the form of inequalities.

## 4. Discussions

4.1. Improving computational efficiency by Keyed predicates

Keyed predicates can be used as global variables, each value of which is specified by key arguments. By storing calculated values and constraints in keyed predicates, these values can be used in another predicate-call, and therefore unnecessary recalculations are avoided. We will show a typical example in which keyed predicates play key roles in improving computational efficiency. The following program calculates the Fibonacci numbers.

```prolog
Example 4.
fib(0: 1).
fib(1: 1).
fib(N: X1 + X2): -N > 1, fib(N - 1: X1),
fib(N - 2: X2).
```

Let us consider a goal fib(5: X). It is determined by fib(4: X1) and fib(3: X2). The subgoal fib(4: X1) is determined by fib(3: X1) and fib(2: X2). Fig. 5 shows the derivation process for this goal. The number associated with each node of the tree represents the ordering in the execution in Keyed CLP. For keyed predicates in nodes 7, 8 and 9, there exist keyed predicates having the same key value in nodes 5, 4 and 3, respectively. Therefore, evaluation of the body part of these predicates 7, 8, and 9 are avoided.

![](/api/attachments/MBMSH4H5/fulltext/images/d2bc6a95b6b25d5f709be82806a46f8bcbca712e24efa92d3e41eff6ca775ffe.jpg)  
Fig. 5. Execution of fib(5: X).

This mechanism has worked effectively in the example of PERT Diagram (3.2). When the goal time\_analysis is executed, Latest\_Finish\_Time('Manufacture\_body': Lf1) is called three times, in the execution of Latest\_Finish\_Time('Deliver\_body\_metal': Lf), Latest\_Finish\_Time('Design\_body': Lf) and Latest\_Finish\_Time(dummy: Lf). By the mechanism of keyed predicates, recalculation of this predicate can be avoided.

When we intend to make a model of decision making problems in OR/MS, each value calculated by some predicate-call is often referred by other predicates. For example, when we build a budget plan, some basic data, such as costs of manufacturing goods, cost of materials and sales units, are often used for calculating other values. If we describe these values by using non-keyed predicates like sales\_units(Products, Units):-... then the body part will be evaluated whenever sales\_units is called. However, the value of sales units is uniquely determined if the name of products is given. Therefore, once the value is calculated, recalculation is not necessary. This problem is avoidable by using keyed predicates with the products name as the key argument, like sales\_units(Products: Units):-...

## 4.2. Improving readability of programs by Keyed predicates

Keyed predicates improve readability of programs. We can refer to each variable by specifying its key, while in Prolog (and also in other CLP languages) we need to write variables as arguments of each predicate. Let us consider the program in Appendix I. If we do not use keyed predicates, then the program is written as follows.

TotProfit(S, Pa, Pb, Pc, Pd): -

Profit(a, Ya), Profit(b, Yb),

Profit(c, Yc), Profit(d, Yd),

$$
\mathrm{S} = \mathrm{Pa} ^ {*} \mathrm{Ya} + \mathrm{Pb} ^ {*} \mathrm{Yb} + \mathrm{Pc} ^ {*} \mathrm{Yc} + \mathrm{Pd} ^ {*} \mathrm{Yd}.
$$

Resource\_Constraint(R, Pa, Pb, Pc, Pd): -

Resource\_Needs(R, a, Xa),

Resource\_Needs(R, b, Xb),

Resource\_Needs(R, c, Xc),

Resource\_Needs(R, d, Xd),

$$
\mathrm{Z} = \mathrm{Xa} ^ {*} \mathrm{Pa} + \mathrm{Xb} ^ {*} \mathrm{Pb} + \mathrm{Xc} ^ {*} \mathrm{Pc} + \mathrm{Xd} ^ {*} \mathrm{Pd},
$$

Resource\_Available(R, L), Z <= L.

constraints(Pa, Pb, Pc, Pd): -

Resource\_Constraint(materials,

Pa, Pb, Pc, Pd),

Resource\_Constraint(epower, Pa, Pb, Pc, Pd),

Resource\_Constraint(mpower, Pa, Pb, Pc, Pd),

$\mathrm{Pa} > 25, \mathrm{Pb} + \mathrm{Pc} + \mathrm{Pd} > = 30,!,$

$(\mathrm{Pb} = 0; \mathrm{Pc} = 0; \mathrm{Pd} = 0)$ .

Feasible(S, Pa, Pb, Pc, Pd): -

TotProfit(S, Pa, Pb, Pc, Pd),

constraints(Pa, Pb, Pc, Pd).

Each predicate in the above program has decision variables Pa, Pb, Pc, and Pd as its arguments. It is not so easy to understand that the variable Pa represents the quantity of production for goods a. However, it is easy if Pa is described in the keyed predicate Product(a: Pa). In addition, when we intend to add a new goods, say e, we have to rewrite the program so that each predicate has a variable Pe as one of the arguments. By using keyed predicates, we have only to add a predicate Goods(e) and some necessary data for goods e. There is no need to change the predicates TotProfit(S) and Resource - Constraint(R).

The advantages of the Keyed CLP syntax can be summarized as follows:

(i) Each variable in a program represents some value of an object (e.g., in the above program the variable Pa is the value of an object “Product” for goods a). Such relationship between each variable and the corresponding object can be described in the form of keyed predicates. This feature improves readability of programs.

(ii) By using keyed predicates as places to store global variables, we do not have to add these variables as the arguments of each predicate. Therefore, the number of arguments in each predicate can be reduced.

(iii) Programs using keyed predicates have flexibility in adding new data. If keyed predicates are not used, then we have to add new arguments corresponding to the new data to each predicate. By using keyed predicates and the higher order predicates such as sum and all, we do not have to change the arguments.

## 4.3. Keyed CLP as an LP-formulator

One of the purposes of Keyed CLP is modelling of linear programming problem. It is not easy to extract constraints directly in the form of formulas when the size of a model becomes large. In addition, modelling by formulas is not good in the viewpoint of reutilizing models, i.e., using old models for new problems that have similar structures. There have been several systems which aim to generate LP-problems without manipulating formulas directly $[12]$ $[10]$ . In Keyed CLP, each problem is described as a set of constraints, relations and logical formulas, and the Keyed CLP interpreter extracts linear constraints from the description and passed them to the linear constraint solver. The described program is easy for users to understand, and is also readable for computers. Keyed CLP can be considered as an

LP-Formulator that generates LP problems from user's description.

## Acknowledgment

I thank Dr. Mitsuhiko Toda, Fujitsu Laboratories for giving me variable suggestions.

## 5. Appendix

Production planning model

/\* There are four kinds of goods \*/
Goods(a).
Goods(b).
Goods(c).
Goods(d).

/\* The quantity of production for each goods
\*/
Product(a: X): -X >= 0.
Product(b: Y): -Y >= 0.
Product(c: Z): -Z >= 0.
Product(d: Z): -Z >= 0.

/\* There are three kinds of resources \*/
Resource(materials.
Resource(epower).
Resource(mpower).

/\* The quantity of each resource required for producing each goods \*/
Resource\_Needs(materials, a: 2.5).
Resource\_Needs(materials, b: 5).
Resource\_Needs(materials, c: 6).
Resource\_Needs(materials, d: 2).

Resource\_Needs(epower, a: 5).
Resource\_Needs(epower, b: 6).
Resource\_Needs(epower, c: 7).
Resource\_Needs(epower, d: 3).

Resource\_Needs(mpower, a: 3).
Resource\_Needs(mpower, b: 2).
Resource\_Needs(mpower, c: 2).
Resource\_Needs(mpower, d: 5).

```txt
/* The profit for producing each goods */
Profit(a: 9).
Profit(b: 5).
Profit(c: 8).
Profit(d: 11).
```

/\* The upper limit of the quantity of each resource \*/
Resource\_Available(materials: 350).
Resource\_Available(epower: 450).
Resource\_Available(mpower: 240).

TotProfit(S): - sum(X \* Y, (Goods(P), Product(P: X), Profit(P: Y)), S).

Decision \_Vars(: Pa, Pb, Pc, Pd): -
Product(a: Pa), Product(b: Pb), Product(c: Pc), Product(d: Pd).

Resource\_Constraint(R): –
sum(X \* Y, (Resource(R), Goods(P), Resource\_Needs(R, P: X), Product(P: Y)), Z),
Resource\_Available(R: L), Z <= L.

constraints: -
all((Resource(R), Resource\_Constraint(R)),
Decision\_Vars(: Pa, Pb, Pc, Pd),
Pa > 25, Pb + Pc + Pd >= 30,!, (Pb = 0; Pc = 0; Pd = 0).

Feasible(S, Pa, Pb, Pc, Pd): –
Decision\_Vars(: Pa, Pb, Pc, Pd), TotProfit(S), constraints.

## References

[1] A. Aiba, K. Sakai, Y. Sato et al., Constraint Logic Programming Language CAL, Proc. of the Int. Conf. on FGCS 1988 (1988) 252–262.

[2] W. Clocksin and C. Mellish, Programming in Prolog, Springer-Verlag (1981).

[3] A. Columerauer, Opening the Prolog III Universe, BYTE, August (1987) 177–195.

[4] V. Dhar and A. Croker, Knowledge-Bases Decision Support in Business: Issues and a Solution, IEEE Expert, Spring (1988) 53–62.

[5] M. Dincbas, P. Van Hentenryck et al., The Constraint Logic Programming Language CHIP, Proc. of the Int. Conf. on FGCS 1988 (1988) 693–702.

[6] D. Dolk, Data as Models: An Approach to Implementing Model Management, Decision Support Systems 2 (1986) 73–80.

[7] A. Geoffrion, An Introduction to Structured Modelling, Management Science, 33-5 (1987) 547–588.

[8] K. Hiraishi, A Constraint Logic Programming Language Keyed CLP and Its Applications to Decision Making Problems in OR/MS, IIAS-SIS Research Report RR-91-19E, Fujitsu laboratories Ltd. (1991).

[9] J. Jaffer and J. Lassez, Constraint Logic Programming, in Proc. of POPL-87, Munich, (1987).

[10] R. Krishnan, A Logic Modelling Language for Automated Model Construction, Decision Support Systems 6 (1990) 123–152.

[11] W. Leler, Constraint Programming Languages, (Addison-Wesley, 1988).

[12] F. Murphy and E. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems, Vol. 2 (1986) 39–47.

[13] F. Szdarovszky, Techniques for Multi-objective Decision Making in System Management (1986) 210–211.

[14] R. Willis, Computer Models for Business Decisions, (John Wiley and Sons, 1987).

![](/api/attachments/MBMSH4H5/fulltext/images/b3ed89562a526bca3dcfa9e52ec8c7724b637294b87cf51bd705744f75cec5a8.jpg)

Kunihiko Hiraishi received the B.E. degree from the Tokyo Institute of Technology in 1983, the M.S. degree in 1985, and the Ph.D. degree in 1990. In 1986 he joined the IIAS-SIS, Fujitsu Laboratories Ltd. Since 1993 he has been an Associate Professor at Japan Advanced Institute of Science and Technology, Hokuriku. His current research interests include computer supported decision making, control of discrete event systems, and

Petri net theory.
