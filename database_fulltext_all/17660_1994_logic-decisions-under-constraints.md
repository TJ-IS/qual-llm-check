---
otero_id: 17660
otero_key: "FHS74UZC"
title: "Logic decisions under constraints"
authors: "Angelo Monfroglio"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90076-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Logic decisions under constraints

Angelo Monfroglio

OMAR Institute of Technology, Novara, Italy

A fundamental issue in the decision process and automated reasoning is how to efficiently obtain logic decisions under constraints. Logic Constraint Satisfaction problems are in general NP-hard and a general deterministic polynomial time algorithm is not known. The present paper illustrates two different approaches: the first based on Constrained Heuristic Search and the second based on Integer and Linear Programming. Both algorithms compare favourable with the best known techniques to solve decisions problems under logic constraints. Complexity of the algorithms and results of significant tests are reported.

Keywords: Logical choice; Constraint satisfaction; Conjunctive Normal Form Satisfaction (CNF-SAT); Constrained Heuristic Search (CHS); Linear Programming (LP).

## 1. Introduction

Logic Constraint Satisfaction plays a crucial role in the real world and in the field of Artificial Intelligence and Decision Support Systems. Several discrete optimization problems, planning problems (scheduling, engineering, timetabling, robotics), operations research problems (project management, advisory systems), data base management problems, pattern recognition problems, multitasking problems, may be reduced in part to constraint satisfaction problems (Rich, 1983; Daniel, 1983; Grant, 1986; Phelps, 1986). A good introductory theory of discrete optimization is Parker and Rardin (1988).

Unfortunately the general constraint satisfaction problem (GCSP) belongs to the NP class of hard problems for which polynomial time deterministic algorithms are not known (Cook, 1971; Garey & Johnson, 1979).

The general constraint satisfaction problem may be expressed in formal terms following Mackworth Freuder (1985): given a conjunction of goals $Gi(x1, x2, \ldots, xNi)$ , and a conjunction of constraints of the form $Cj(x1, x2, \ldots, xGj, y1, y2, \ldots, yLj)$ , with xi global variable, that is a goal variable, yi local variable, that is a variable which appears as argument in a constraint but does not appear as argument in a goal, we must find an instantiation of all the variables that satisfies all the goals and all the constraints.

We consider here only finite domains that is variables that range over a finite number of values and a problem with only one goal. We name these CSPs Logic Constraint Satisfaction Problems, or simply CSPs.

Rossi (1988) shows the mapping between a CSP and a logic program having the same semantics. That paper formally defines a CSP as a labelled connection hypergraph and introduces a theorem which states that given a CSP C and the mapped logic program P(C), the semantics of P(C) coincides with the solution of C.

A CSP is defined as a hypergraph $(N, A, c, l, a)$ , where N is a set of variables to be instantiated in a given finite domain U, with $\#N = n$ ; A is a ranked set of hyperarcs, called constraints; c is the connection function and $c(h) = (x1, \ldots, xk)$ means that h connects the nodes $x1, \ldots, xk$ in this order; l is the labelling function, $l: A \to L$ , where L is a finite set of labels; a is an additional hyperarc, called connection hyperarc, that connects the nodes which we are interested in from the solution point of view.

The solution of a CSP is defined as the instantiation of the variables connected by the connection hyperarc, such that all the constraints in A are satisfied.

Any variable in a CSP can be represented by a corresponding variable in logic programming, any constraint by an atom whose predicate symbol is the name of the constraint and whose arguments are the variables connected by that constraint.

Due to its relational form and the possibility of writing metaprograms in the same language, it is evident that logic programming is a convenient programming language to represent, relax and solve constraint satisfaction problems, but most of the times the logic program produces the solution of the CSP in a very inefficient way.

Let us also decompose the argument list of goal G in two parts: $x1, x2, \ldots, xc$ instantiated as input constants and $xc + 1, xc + 2, \ldots, xn$ to obtain as output instantiated values.

## 1.1. Related work

Some resource allocation problems can be reduced to the matching problem for bipartite graphs (with the simplifying assumptions that all variables can be assigned a resource): a polynomial time approach for the maximum matching in arbitrary graphs is Edmonds (1965); Hopcroft and Karp (1973) have an $O(n^{2.5})$ algorithm for maximum matching in bipartite graphs. Our approach is however more general. [Micali S., V.V. Vazirani, 1980] give an algorithm for maximum matching in general graphs that is deterministic and has a complexity of the square root in the number of vertices times the number of edges.

In the opinion of Van Hentenryck (1987), backtracking (intelligent backtracking included) is more a remedy to a symptom of the malady than to the malady itself.

So new techniques have been presented that avoid failures by reducing the search space in a ‘a priori’ way and are Consistency Techniques yet introduced by D. Waltz, Mackworth A.K., Montanari U., A. Martelli, E.C. Preuder, Mohr R., Henderson and others. These techniques are also called “relaxation algorithms” when applied as a preprocessor before the backtrack search.

Van Hentenryck (1987) and Van Hentenryck (1988) give a survey of consistency techniques in Logic Programming to solve Combinatorial Problems. A new logic programming language is introduced that incorporates consistency techniques as an extension of Prolog.

The key idea is to introduce the domain concept inside logic programming and some declarations for inference rules. The domain concept allows the user to specify the range of a variable. The consistency techniques are for example Forward checking and Looking ahead. Forward checking makes sure that each not yet assigned variable has at least one consistent value with the already assigned variables. Looking ahead makes sure that each not yet assigned variable has at least one consistent value with all the other not yet assigned variables. Van Hentenryck has tested the new language to solve a series of constraint satisfaction and optimization problems such as puzzles (N-queens, mastermind, cryptarithmetic, etc.) and operations research applications (graph coloring, scheduling with disjunctive constraints, etc.). The results are better than any form of intelligent backtracking yet implemented. See also Simonis H. and M. Dincbas (1990).

Recently Jaffar J. and J.L. Lassez proved that it was possible to define languages in a more general logic framework, called “the Constraint Logic Programming Scheme”. Specific Prolog extensions, such as Colmerauers’s PROLOG II and PROLOG III, were then proven to be instances of the scheme.

In the context of constraint satisfaction problems and symbolic computation, a choice in usual logic programming corresponds to the instantiation of a variable. A logic choice is a crucial issue in the reasoning process for decision support systems.

In his invited talk at ECAI'90, M. Fox (1990) has described an approach to scheduling through 'a contention graph' which is an analogous to ours about heuristic constraint satisfaction (as presented in Monfroglio A. (1987, 1989). The technique we have introduced is now well known and usually adopted. M. Fox, for instance, has used an almost similar technique at Carnegie Mellon in a system called CORTES that solves scheduling problem using Constrained Heuristic Search.

In Fox M.S. (1991), Fox proposes a model of decision making that provides structure by combining constraint satisfaction and heuristic search. He introduces the concepts of topology and texture to characterize problem structure. Fox has identified few fundamental problem textures among which the most important are:

\- value contention: degree to which variables are contending for the same value;

\- value conflict: degree to which a variable's assigned value is in conflict with existing constraints.

These textures are decisive for identifying bottlenecks in decision support. In the successive section we will describe our techniques first introduced in Monfroglio A. (1987) which use a slightly different terminology: for value contention we use “shared resource index” and for value conflict we adopt the term “exclusion index”.

As expected, the experimental results for our algorithms have been comparable or superior than other known approaches such as described in Gallio G. and G. Urbani (1989).

In Monfroglio A. (1991) we describe a connectionist approach to Constrained Heuristic Search.

## 2. The Shared Resource Allocation Algorithm (SRAA)

Let us begin with the Shared Resource Allocation Algorithm, we first present informally. We suppose to have a lot of variables (or processes) and a lot of shared resources; each variable can obtain a resource among a choice of alternatives, two or more variables may not have the same resource.

The Constraint graph of Freuder E.C. (1982) is a complete graph, since each variable is constrained by the others not to share a resource (alternative). Even in the applications we describe in the following sections, the graph is a complete graph. So we can not use the fundamental result of Freuder E.C. (1982):

a sufficient condition for a backtrack-free search is that the level of strong consistency is greater than the width of the constraint graph and a connected constraint graph has width 1 if and only if it is a tree. Our constraint graph is not a tree and the width is equal to the order of the graph minus 1.

Dechter R. and J. Pearl (1989) presents a systematic way of regrouping constraints into hierarchical structures capable of supporting search without backtracking. A general strategy is used to form clusters of variables such that the interactions between the clusters are tree structured and then to solve the problem by efficient tree algorithms. However, the subproblems must be solved by some approach such as ours. Moreover, our complete constraint graph is not well suited for clustering. As an example of our problem consider:

v1: E, C, B    v2: A, E, B    v3: C, A, B
v4: E, D, D    v5: D, F, B    v6: B, F, D,

where v1, v2, v3, v4, v5, v6 are variables (or processes) and E, C, etc. are resources. Note that a literal may have double occurrences, because our examples are random generated.

Let us introduce our algorithm. Consider the trivial case where:

$v1:B$ $v2:C$ $v3:A$

Obviously the problem is solved, we say that each variable has a Shared Resource Index equal to zero. Now let us slightly modify the situation:

Now v1 shares with v3 the resource A, we say that v1 has a Shared Resource Index greater than v2. Moreover the alternative A for v1 has a Shared Resource Index greater than B.

Our algorithm is based on this simple observation and on the Shared Resource Index. It computes four Shared Resource Indexes:

1. the first Shared Resource Index for the alternatives

2. the first Shared Resource Index for the variables

3. the total Shared Resource Index for the alternatives

4. the total Shared Resource Index for the variables.

Now we go back to our example of v1, v2, v3, v4, v5, v6 and we describe all the steps of our algorithm. For v1 E is shared with v2 and v4, C with v3, B with v2, v3, v4, v6.

The algorithm builds the Shared Resource List for each alternative of each variable and then the length of each list that we name first Shared Resource Index for the alternatives.

We can easy verify that the first Share Indexes for the alternatives are:

```txt
v1: 2, 1, 4 v2: 1, 2, 4 v3: 1, 1, 4
v4: 2, 2, 2 v5: 2, 1, 4 v6: 4, 1, 2.
```

Then the algorithm builds the first Shared Resource Index for each variable as the sum of all the first Shared Resource Indexes of its alternatives:

```javascript
v1: 7; v2: 7; v3: 6; v4: 6; v5: 7; v6: 7.
```

Through the Shared Resource List for each alternative the system computes the total S.R. Index as the sum of the first Variable Indexes:

```javascript
v1: 13, 6, 27 v2: 6, 13, 27 v3: 7, 7, 28
v4: 14, 14, 14 v5: 13, 7, 27 v6: 27, 7, 13.
```

For instance, in $v1$ we have the alternative $E$ which is shared with $v2$ (Index 7) and $v4$ (Index 6) for a sum of 13.

Finally the algorithm determines the total Shared Resource Index for each variable as the sum of its total Shared Resource Indexes for the alternatives:

```javascript
v1: 46; v2: 46; v3: 42; v4: 42; v5: 47; v6: 47.
```

If at any time a variable has only one alternative, this is immediately assigned to that variable.

Then it assigns for the variable with the lowest Share Index the alternative with the lowest Shared Resource Index: v3 with C (also v4 has the same Shared Resource Index).

The system updates the problem deleting the assigned variable with all its alternatives and the assigned alternative for each variable. Then the algorithm continues as a recursive call. In the example the assignments are:

```txt
v3: C; v1: E; v2: A; v4: D; v5: F; v6: B.
```

Consider the following example:

```javascript
v1: A, B; v2: A, D; v3: D, E; v4: E, F, G; v5: E, F, G; v6: E, F, G; v7: B, H; v8: H, I;
v9: I, J, K; v10: I, G, K
```

The total indexes are:

```txt
v1: 2, 2    4    v2: 2, 4    6
v3: 2, 21    23    v4: 18, 14, 14    46
v5: 18, 14, 14    46    v6: 18, 14, 14    46
v7: 2, 3    5    v8: 2, 8    10
v9: 7, 4, 4    15    v10: 7, 4, 4    15.
```

Here, the choice of $A$ for the first variable leads to no solution, while the choice of $B$ leads to the solution:

```txt
v1: B; v2: A; v3: D; v4: E; v5: F; v6: G; v7: H; v8: I; v9: J; v10: K.
```

In case of equal minimal indexes, the algorithm must compute additional indexes using the yet computed as first indexes. For the first variables we find: v1: 6, 5, and we must assign B to the variable v1.

The additional indexes are non-monotonic: in the above example, if we compute 4 successive indexes, we can see that for the variable v1 with the choice B (which gives the solution) we have minimal index for the iterations 2 or 3, the iteration 4 gives v7 as the first variable to instantiate and does not give a solution:

Indexes for the variables in 4 iterations:

<table><tr><td>v1</td><td>v2</td><td>v3</td><td>v4</td><td>v5</td><td>v6</td><td>v7</td><td>v8</td><td>v9</td><td>v10</td></tr><tr><td>4</td><td>6</td><td>23</td><td>46</td><td>46</td><td>46</td><td>5</td><td>10</td><td>15</td><td>15</td></tr><tr><td>11</td><td>27</td><td>144</td><td>299</td><td>299</td><td>299</td><td>14</td><td>35</td><td>55</td><td>55</td></tr><tr><td>41</td><td>155</td><td>924</td><td>1938</td><td>1938</td><td>1938</td><td>46</td><td>124</td><td>200</td><td>200</td></tr><tr><td>201</td><td>965</td><td>5969</td><td>12552</td><td>12552</td><td>12552</td><td>165</td><td>446</td><td>724</td><td>724</td></tr></table>

The indexes for the alternatives of the variable v1 in the iteration 2 are:

```txt
v1: A 6; v1: B 5 (minimum).
```

So how can we know where to stop in computing the successive indexes to find the solution? We have found the best results using the following procedure. We will introduce the ‘dependence level’. In our example, we have:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
level 1: $v1$: $v2$ (choice $A$), $v7$ (choice $B$)
</div>

level 2: $v2$ : $v3$ (choice $D$ ); $v7$ : $v8$ (choice $H$ )

level 3: v3: v4, v5, v6 (choice E); v8: v9, v10 (choice I).

The level is 3 and we must compute 3 successive indexes. Of course if we start with a different variable, we find a differential level. For example, if we start with v2, we find a level 4:

```txt
level 1: v2: v1; v3
level 2: v1: v7; v3: v4, v5, v6
level 3: v7: v8
level 4: v8: v9, v10.
```

The ‘dependence tree’ is constructed as following:

\- starting with the chosen variable $vi$ , examine the variables which share with $vi$ some alternative and that we have not yet considered and increment the level (initialized as 1)

\- repeat until no more variables are present (the variables appear one time each). We can summarize:

<table><tr><td>Starting var.</td><td>Level of dep.</td><td>Start. var.</td><td>Lev. of d.</td></tr><tr><td> $v1$ </td><td>3</td><td> $v6$ </td><td>6</td></tr><tr><td> $v2$ </td><td>4</td><td> $v7$ </td><td>4</td></tr><tr><td> $v3$ </td><td>5</td><td> $v8$ </td><td>4</td></tr><tr><td> $v4$ </td><td>6</td><td> $v9$ </td><td>6</td></tr><tr><td> $v5$ </td><td>6</td><td> $v10$ </td><td>6.</td></tr></table>

As one can see, the minimal dependence level is 3 for the first variable.

We can see easily that we have, in the worst case and in the absence of repetitions which can speed up the evaluation for the S.R.A. Algorithm $N*N*(N-1)=N^{2}*(N-1)$ comparisons for the first assignment, then $(N-1)^{2}*(N-2)$ , etc. for the successive assignments, giving an asymptotic complexity (apart from constants and minor exponents) of $0\left(\mathrm{N}^{4}\right)$ .

Hopcroft J.E. and R.M. Karp (1973) give an $0(n^{2.5})$ algorithm for maximum matchings in bipartite graphs. If we restrict our study to the present problem without considering the problems of the successive sections, we can use that algorithm.

Fox M. (1990) has used a similar technique in a system called CORTES that solves the scheduling problem using Constrained Heuristic Search. M. Fox reports his experience in using conventional CSP techniques that do not perform well in either finding an optimized or satisfying solution. He has found that for a class of problems where each variable is contending for the same value, i.e., the same resource, it is beneficial to introduce another type of graph, he calls a contention graph. It is needed to identify where the highest amount of contention is, then is clear where to make the next decision. The easy decisions are activities that don't contend for bottlenecked resources, the difficult decisions are activities that contend more. The Fox's contention graph is about analogous to our techniques with the shared resource indexes.

## 2.1. Formal description of the Shared Resource Allocation Algorithm (SRAA)

Our algorithm solves problems with a finite number of variables each variable having a finite number of choices. In formal terms we have:

v1: a11, a12, ..., a1j, ..., a1M1

$$
v 2: a 2 1, a 2 2, \dots , a 2 j, \dots , a 2 M 2
$$

$$
v i: a i 1, a i 2, \dots , a i j, \dots , a i M i
$$

$$
v n: a n 1, a n 2, \dots , a n j, \dots , a n M n,
$$

with $Mi$ , $n > 0$ and finite and, lexicographically ordered, a finite number $P > = n$ of distinct alternatives. Each variable must have an assignment among a set of alternatives and two or more variables can not have incompatible assignments (here, the incompatibility means equality; in the following application, two assignments are incompatible if they are the negated and unnegated versions of the same literal). We must find the following assignments:

v1: a1k v2: a2l v... vn: anz,

with $a1k$ not equal to $a2l$ , etc.

The main structure of the algorithm is the recursive call:

1. $v$ if constraints and assign1 and $v$ .

The call holds while the list of variables to be assigned is not empty.

2. The call constraints does the following:

if the list of alternatives for a variable has length 1, i.e. has only one alternative, then that alternative is assigned to the variable and then the call update is used for the problem.

3. The update procedure deletes the assigned alternative in the set of currently available alternatives for each variable, and deletes the instantiated variable in the list of variables to instantiate.

4. The procedure constraints makes then two things:

4.1. it constructs for each variable X, and for each alternative Y for X, a relation if that alternative is shared with another variable and the same relation is not yet present in memory.

For example, if

$$
v 1: B, C, E v \dots v 3: A, B;
$$

the relation $c(1, B, 3)$ is created (if the same relation is not yet present in memory).

4.2. it constructs the 4 shared resource indexes: FASRI, FVSRI, TASRI, TVSRI.

4.2.1. it computes the First Shared Resource Index for the alternatives:

for each variable X for each alternative Y in the set associated with the variable if there exists a relation $c(X, Y, Z)$ then increments the FASRI(X, Y).

4.2.2. for each variable X, it computes the sum FVSRI(X) of the FASRI(X, Y).

4.2.3. for each variable X for each alternative Y if there exists a relation $c(X, Y, Z)$ then adds the FVSRI(Z) to the current TASRI(X, Y).

4.2.4. for each variable X, it computes the sum TVSRI(X) of the TASRI(X, Y).

5. The procedure assign1 finds the Min TVSRI(X) and for that variable, the Min TASRI(X, Y), then this alternative is assigned to the variable, and the procedure update is used.

If there are two or more equal indexes for a variable then additional indexes are computed in the same manner, using the total indexes yet computed as first indexes to break ties. The number of additional indexes that are computed is determined by the dependence level as we have shown in the previous section.

## 2.1.1. Outline of soundness for the SRAA

First it is obvious that the solutions provided by our SRAA algorithm, if any, are correct. Indeed, each time a variable receives an assignment, the incompatible alternatives for all the variables are deleted through the step 3. So the algorithm can not assign incompatible values.

We must ensure that the algorithm is complete too. We suppose to have the following solution for a problem with 4 variables:

```txt
v1: B; v2: A; v3: D; v4: C.
```

This solution was found of course through a choice among several alternatives for each variable:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$v1:\ldots ,B,\ldots$ $v2:\ldots ,A,\ldots$ $v3:\ldots ,D,\ldots$ $v4:\ldots ,C,\ldots$
</div>

Nevertheless we may suppose to have found that solution for a different problem, a problem which has only one alternative for each variable:

```txt
v1: B; v2: A; v3: D; v4: C.
```

Now this is the problem and the solution too. All the FASRI, FVSRI, TASRI, TVSRI of the steps 4.2.1, 4.2.2, 4.2.3, 4.2.4 are null because incompatible alternatives are not present.

Let us now slightly complicate our problem, adding an alternative for a variable. We can have the following cases:

1. the alternative is equal to the alternative which was assigned to that variable: this is a trivial case, for instance v1: B, B;

2. the alternative is different from all the present alternatives, for example: v1: B, E.

In this case the number of global distinct alternatives becomes larger, we have two different solutions, but the case is still trivial, because we have not incompatible alternatives and our indexes remain null. 3. the alternative is incompatible with some other, for example:

```javascript
v1: B, A; v2: A; v3: D; v4: C;
```

where A in v1 and A in v2 are incompatible. This is equivalent to the problem:

```javascript
v1: A, B; v2: A; v3: D; v4: C,
```

where the alternatives are ordered in alphabetic order.

Now the indexes are different: $A$ for $v1$ has an index higher than $B$ , $v1$ and $v2$ have higher indexes than $v3$ and $v4$ . The problem has only one solution among the possible choices. This solutions remains:

```javascript
v1: B; v2: A; v3: D; v4: C,
```

which has all indexes in accord with those of our algorithms. The choice:

```javascript
v1: A; v2: A; v3: D; v4: C,
```

which is not a solution (A and A are incompatible) does not respect the indexes.

Now we complicate our example adding two (or more) alternatives. We may find two cases: 3.1. the problem is not symmetric in respect to the indexes of our algorithms, for instance:

```txt
v1: A, B v1: 1, 0
v2: A, C v2: 1, 1
v3: D v3: 1
v4: C, D v4: 1, 1.
The solution remains:
v1: B; v2: A; v3: D; v4: C,
in accord with our algorithm.
```

3.2. the problem is symmetric in respect to the indexes:

```csv
v1: B, A v1: 1, 1
v2: A, C v2: 1, 1
v3: D, B v3: 1, 1
v4: C, D v4: 1, 1
```

In this case all the indexes are equal but our primitive solution remains the solution that is in accord with our algorithm.

In conclusion, there is no way to add new alternatives which do not fall in one of the 1, 2, 3.1, 3.2 cases. We have illustrated the outline of the proof for a case of 4 variables, but a general case with a finite number n of variables can not, of course, show different situations, because all the arguments of part 1, part 2 and part 3 are not dependent on the number of variables: in (1) we checked if the added alternative was equal to that yet assigned for that variable, in (2) we tested if the alternative was different from all the present alternatives, in (3) the alternative is incompatible with some other, do not mind how many, in (3.1) and (3.2) the matter is symmetry.

Indeed, if we start with a desired solution and complicate the problem adding more and more alternatives that solution remains in accord with our minimal indexes and the algorithm finds it.

## 2.2. Implementation and tests

We have done random generated tests for the algorithms. We used an automatic testing procedure: a routine generates a solution, for instance:

```txt
v1: A; v2: C; v3: B; v4: D; v5: F; v6: E.
```

Then another routine adds more randomly generated alternatives for each variable, in accord with the user's directions. So a solution is guaranteed. Finally, the problem is solved by our algorithm. We have done hundreds of tests.

In addition, we have done special hand constructed tests, suggested by our first revisers in the previous publications. All the tests were positive. The real complexity was about $O(N^{3.4})$ in the dimension of the problem (the number of variables or constraints or processes).

## 3. The satisfaction of a conjunctive normal form

Now let us consider a different situation: the classic problem of the Satisfaction of a Conjunctive Normal Form. This problem is considered a NP problem and is very important because all NP problems may be reduced in polynomial time to CNF satisfaction (Cook S.A., 1971). In formal terms the problem is:

Given a Conjunctive Normal Form, find an assignment for all variables that satisfies the conjunction. An example of CNF is:

$$
(A + B). (C + D). \left(\tilde {B} + \tilde {C}\right). \left(\tilde {A} + \tilde {D}\right)
$$

where + means OR, . AND, \~ NOT.

A possible assignment is $A =$ true, $B =$ false, $C =$ true, $D =$ false.

We reconduct the problem to a Shared Resource Allocation:

\- we name 'variable' each term $(A + B)$ ,

\- each term must be satisfied: since this term is a logical OR, it is sufficient that $A$ or $B$ is true

\- we consider as 'alternative' each literal $A, B$ .

\- We use upper case letters

for non-negated alternative and lower case letters for negated alternatives. So we achieve:

$$
v 1 \colon A, B; v 2 \colon C, D; v 3 \colon b, c; v 4 \colon a, d.
$$

Of course, the choice of $A$ for the variable 1, does not permit the choice of NOT $A$ , that is the alternative $a$ , for the variable 4.

If we find allocation for the variables, we find also an assignment true/false for the CNF. For example:

```txt
v1: A; v2: C; v3: b; v4: d leads to:
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$A = \text{true}, C = \text{true}, B = \text{false}, D = \text{false}.$
</div>

There may be cases where the choices let undetermined some letter. In this case more than one assignment is possible.

Consider the example:

$$
(A + B). \left(\tilde {A} + \tilde {C} + D\right). \left(\tilde {A} + \tilde {B} + C\right). \left(\tilde {D}\right)
$$

that is transformed in:

```javascript
v1: B, B; v2: a, c, D; v3: a, b, C; v4: d.
```

The choice:

v1: B; v2: a; v3: a; v4: d leads to the assignment:

## $A =$ false, $B =$ true, $D =$ false and $C =$ undetermined $(C =$ true or $C =$ false).

Now we use an algorithm analogous to the above Shared Resource Allocation Algorithm. Each upper case letter excludes the same lower case letter and vice versa. A with A, b with b, c with c, or B with B, etc. are not of course considered mutually exclusive.

We compute:

1. the first Alternative Exclusion Index (I1)

2. the first Variable Exclusion Index (I2)

3. the total Alternative Exclusion Index (I3)

4. the total Variable Exclusion Index (I4).

In our example:

```txt
v1: 2, 1 v2: 1, 1, 1 v3: 1, 1, 1 v4: 1
v1: 3 v2: 3 v3: 3 v4: 1
v1: 6, 3 v2: 3, 3, 1 v3: 3, 3, 3 v4: 3
v1: 9 v2: 9 v3: 7 v4: 3.
```

Now we assign the variable with the lowest Exclusion Index, and the alternative for that variable, with the lowest Exclusion Index: v4: d, that is D = false.

Note that this variable v4 is immediately instantiated because it has only one alternative.

Then we update the problem deleting all the alternatives not permitted by this choice, that is all the $D$ alternatives.

In our case, we find:

```txt
v1: A, B v2: a, b, C v3: a, c
v1: 2, 1 v2: 1, 1, 1 v3: 1, 1
v1: 3 v2: 3 v3: 6
v3: a, (A = false), v2: a, v1: B (B = true) and C = undetermined.
```

If at any time a variable has only one choice this is immediately instantiated to that value. Now let us consider another example:

```csv
v1: A, B 1, 1 2 3, 3 6  
v2: a, C 1, 2 3 2, 7 9  
v3: b, D 2, 1 3 5, 4 9  
v4: c, d 2, 2 4 6, 6 12  
v5: B, C 1, 2 3 3, 7 10  
v6: c, D 2, 1 3 6, 4 10
```

```txt
v1: A, B v2: a, H v3: h, C, D v4: c, G v5: c, g  
v6: d, G v7: d, g v8: f, G v9: b, F  
v10: F, g, I v11: f, D, J.
```

Here, the first variable to be assigned is $v1$ (index = 6). $v1$ has two alternatives with equal indexes of

3. If we assign $A$ to $v1$ , the problem has no solutions. If we assign $B$ to $v1$ , the solution is:

a (false), B (true), c (false), D (true); a solves v2; B solves v1, v5; c solves v4, v6; D solves v3, v6. So our algorithm must be modified. We compute other indexes:

5. the first Alternative Compatibility Index (I5)

6. the first Variable Compatibility Index (I6)

7. the total Alternative Compatibility Index (I7)

8. the total Variable Compatibility Index (I8),

which account for the fact that a chosen alternative solves more than one variable.

As difference between the correspondent indexes, we calculate:

9. the first Alternative Constraint Index I9 = I1-I5

10. the first Variable Constraint Index I10 = I2-I6

11. the total Alternative Constraint Index I11 = I3-I7

12. the total Variable Constraint Index I12 = I4-I8.

In our example:

<table><tr><td>I5</td><td>I6</td><td>I7</td><td>I8</td><td>I11</td><td>I12</td></tr><tr><td>v1: 0, 1</td><td>1</td><td>0, 2</td><td>2</td><td>3, 1</td><td>4</td></tr><tr><td>v2: 0, 1</td><td>1</td><td>0, 2</td><td>2</td><td>2, 5</td><td>7</td></tr><tr><td>v3: 0, 1</td><td>1</td><td>0, 2</td><td>2</td><td>5, 2</td><td>7</td></tr><tr><td>v4: 1, 0</td><td>1</td><td>2, 0</td><td>2</td><td>4, 6</td><td>10</td></tr><tr><td>v5: 1, 1</td><td>2</td><td>1, 1</td><td>2</td><td>2, 6</td><td>8</td></tr><tr><td>v6: 1, 1</td><td>2</td><td>1, 1</td><td>2</td><td>5, 3</td><td>8.</td></tr></table>

So the choice for v1 is the alternative B (index = 1). The reason is that the situation here is different in respect to that of the Shared Resource Allocation Algorithm. If an alternative has the same exclusion index but solves more variables, we must prefer that choice. As another example, consider:

The Exclusion Indexes are (for brevity we report here only 2 indexes, but the dependence level is 4)

<table><tr><td>v1: 1, 1</td><td>2</td><td>2, 3</td><td>5</td></tr><tr><td>v2: 1,</td><td>2</td><td>2, 5</td><td>7</td></tr><tr><td>v3: 1, 2, 2</td><td>5</td><td>2, 8, 8</td><td>18</td></tr><tr><td>v4: 1, 3</td><td>4</td><td>2, 8</td><td>10</td></tr><tr><td>v5: 1, 3</td><td>4</td><td>2, 8</td><td>10</td></tr><tr><td>v6: 2, 3</td><td>5</td><td>6, 8</td><td>14</td></tr><tr><td>v7: 2, 3</td><td>5</td><td>6, 8</td><td>14</td></tr><tr><td>v8: 2, 3</td><td>5</td><td>6, 8</td><td>14</td></tr><tr><td>v9: 1, 2</td><td>3</td><td>2, 6</td><td>8</td></tr><tr><td>v10: 2, 3, 0</td><td>5</td><td>8, 8, 0</td><td>16</td></tr><tr><td>v11: 2, 2, 0</td><td>4</td><td>5, 9, 0</td><td>14.</td></tr></table>

<table><tr><td colspan="4">The Compatibility Indexes are:</td></tr><tr><td>v1: 0, 0</td><td>0</td><td>0, 0</td><td>0</td></tr><tr><td>v2: 0, 0</td><td>0</td><td>0, 0</td><td>0</td></tr><tr><td>v3: 0, 0, 1</td><td>1</td><td>0, 0, 2</td><td>2</td></tr><tr><td>v4: 1, 2</td><td>3</td><td>3, 6</td><td>9</td></tr><tr><td>v5: 1, 2</td><td>3</td><td>3, 6</td><td>9</td></tr><tr><td>v6: 1, 2</td><td>3</td><td>3, 6</td><td>9</td></tr><tr><td>v7: 1, 2</td><td>3</td><td>3, 6</td><td>9</td></tr><tr><td>v8: 1, 2</td><td>3</td><td>2, 6</td><td>8</td></tr><tr><td>v9: 0, 1</td><td>1</td><td>0, 3</td><td>3</td></tr><tr><td>v10: 1, 2, 0</td><td>3</td><td>1, 6, 0</td><td>7</td></tr><tr><td>v11: 1, 1, 0</td><td>2</td><td>3, 1, 0</td><td>4.</td></tr></table>

## The final Constraint Indexes are:

<table><tr><td>v1: 2, 3</td><td>5</td><td>v2: 2, 5</td><td>7</td></tr><tr><td>v3: 2, 8, 6</td><td>16</td><td>v4: -1, 2</td><td>1</td></tr><tr><td>v5: -1, 2</td><td>1</td><td>v6: 3, 2</td><td>5</td></tr><tr><td>v7: 3, 2</td><td>5</td><td>v8: 4, 2</td><td>6</td></tr><tr><td>v9: 2, 3</td><td>5</td><td>v10: 7, 2, 0</td><td>9</td></tr><tr><td>v11: 2, 8, 0</td><td>10.</td><td></td><td></td></tr></table>

Here v4 and v5 have minimal indexes, choosing the first, we find: v4: c; v5: c.

Updating the problem and repeating the procedure, we have: v2: a; v1: B. Again updating, we find: v9: F; v10: F; v8: G; v6: G; v7: d; v3: h; v11: J.

## 3.1. Formal description

Formally the description of this algorithm is the same as the SRAA, apart from the following modifications:

## 1. the relation of step 4.1

c (variable1, alternative, variable2) is created if in the set of alternatives for the variable 1 there is a literal L, and in the set for the variable 2, there is the same literal in negated form or vice versa. In fact the implementation uses lower and upper case letters for the non negated and negated form of a literal.

The FAEI, FVEI, TAEI, TVEI indexes are then computed in the same manner as the FASRI, FVSRI, TASRI, TVSRI indexes.

2. the procedure update now has two parts:

a. the first part deletes in the set of each variable the negated form of the literal currently assigned (in fact, the upper case version if the currently assigned alternative is a lower case letter and vice versa);

b. the last part does a search in the set of each variable for the same literal currently assigned. If another variable has the same alternative, this alternative is immediately assigned to that variable, and the variable is deleted in the list of variables to instantiate. So in this case a single call of the relation assign1 may assign more than one variable.

3. The procedure which computes the minimum for TAEI checks if there are two or more identical values. If this is the case, 4 other indexes are computed as discussed in the above presented examples, i.e. the FACI, FVCI, TACI, TVCI indexes. These are in fact the previously defined Shared Resource Indices. Finally, the last 4 indices are computed and the assignment procedure is the same as in the previous algorithm.

We find here the cases:

(I) problems with solution without multiple occurrences, for instance:

v1: A v2: B v3: C v4: D.

We have:

1. $v1:A,A$ $v1:A,a$

2. v1: A, E all trivial.

3. $v1: A, B$

4. v1: A, b.

(II) problems with solution with multiple occurrences of the same alternative, for example:
v1: A
v2: B
v3: B
v4: C.

We have:

1. $v1: A, A$

v1: A, a

2. v1: A, D which are trivial.

3. v1: A, C

we find here, for the alternative C, the same Exclusion Index (with greater Compatibility (Index): if the variable 1 is selected for instantiation, the alternative C has a preference as we said in the above modification 3 of the SRAA.

4. $v1: A, c$

here we have a greater Exclusion Index for the choice $c$ : of course our algorithm prefers the alternative $A$ .

5. v1: A, b greater Exclusion Index and for more variables if we choose the alternative b: this case is analogous to the previous case 4.

6. $v2:B,D$

the same Exclusion Index for D and, if we assign D to v2, less Compatibility Index (D solves only v2 and does not solve v3): as in the case 3, our algorithm assigns B, if the variable 2 is currently to instantiate.

One may suspects that the combination of 3-, 4-, 5-, 6- cases may lead to a situation where to find a solution we must violate the principle of minimal indexes, i.e. a solution is possible if we use a different algorithm. In particular, we may suppose that starting with a variable or an alternative with worse Exclusion Index, we may find a solution and the problem has only that solution. One may argue for example that it is due to a greater Compatibility Index. Random generated tests never have exhibited such a case, but there may be hand constructed tests which fail. The technique can be considered a good heuristic which may fail in special cases, but is useful in most of practical instances.

The reason why completeness may be lost in because in this case the heuristics are in fact two: the Compatibility Index and the Exclusion Index. The interaction between the indexes may lose the completeness, while the computational efficiency in random generated tests remains very much improved, since the probability that the interaction violates the principle of minimal index is very low.

Our algorithm has in fact other limitations, it does not find all solutions, but one solution, and if a complete solution does not exist, it does not guarantee to find the largest possible partial-solution. It is possible that a different choice leads to a larger solution even if a complete solution is not possible.

Iwama K. (1987) describes a new algorithm, called IS, developed specifically for CNF SAT and investigates its complementary nature against the conventional backtracking approach. The average time complexity is polynomial, but the worst case remains NP. Even Brown C and P. Purdom (1981) and P. Purdom and C. Brown 1983) show that random CNF SAT problems can be solved in polynomial average time by improvements of backtracking.

Average time complexity of our Constrained Heuristic Search approach is comparable with the above quoted algorithms.

Average time complexity of our Constrained Heuristic Search approach is comparable with the above quoted algorithms.

In the next sections we will present the second approach, based on linear programming.

## 4. Conjunctive Normal Form Satisfaction and Linear Programming

Now we will illustrate the second approach: we present a technique to solve a CNF-SAT problem by means of linear programming (LP).

Useful insight for this work may be found in Parker and Rardin (1988), Balas (1975), Chvatal (1985), Edmonds (1965), Gomory (1963) and Megiddo (1983).

As well known, every linear program can be rearranged to have the matrix form (called primal)

$$
A 1 1 x 1 + A 1 2 x 2 > = b 1
$$

$$
A 2 1 x 1 + A 2 2 x 2 = b 2
$$

with $x1 > = 0$ , $x2$ unrestricted.

By adding nonnegative slack or surplus variables to convert any inequalities to equalities, replacing any unrestricted variables by differences of nonnegative variables, deleting any redundant rows, and taking the negative of a maximize objective function (if any), a linear program can be written in the famous simplex standard form

$$
\begin{array}{l} \min c x \\ A x = b \\ x > = 0. \end{array}
$$

Modern optimization began with George Dantzig's development of the Simplex algorithm (1947).

However, the worst case complexity of the Simplex algorithm is exponential, even if the Simplex typically requires a low-order polynomial number of steps to compute an optimal solution.

Recently, Khachian's Ellipsoid algorithm (Khachian, 1979) and Karmarkar's Projective Scaling Algorithm (Karmarkar, 1984), have been introduced that are provable polynomial.

An integer problem in Simplex standard linear programming has the form

$$
\begin{array}{l} \min c x \\ A x = b \\ x > = 0, x \text {   integer } \end{array}
$$

The integrity constraint renders the problem more difficult and in fact, 0-1 integer solvability is in general an NP-hard problem, while Linear Programming is in the class of P-complexity. Remember that 0-1 integer solvability may be formulated: given an integer matrix A and an integer vector b, does there exist a 0-1 vector x such that Ax = b?

The maximal set of linearly independent columns of a linear program is called a basis submatrix.

A constraint matrix $A$ is said to be unimodular if every basis matrix $B$ of $A$ has determinant $\det(B) = +1$ or $-1$ .

Veinott and Dantzig (1968) show that if A is an integer matrix with linearly independent rows and A is unimodular then extreme-points of $S = \{x: Ax = b, x > = 0\}$ are integer for any integer right-hand-side b.

A matrix A is said to be totally unimodular if every square submatrix of A has determinant $= +1$ or -1 or 0.

Hoffman and Kruskal (1956) show that if $A$ is an integer matrix and is totally unimodular then extreme-points (among which there are the solutions of the optimization problem) are integer for any integer right-hand-side $b$ . The proof is an easy application of Cramer's Rule for solving systems of linear equations (Bixby, 1982).

Of course, totally unimodular matrices are desirable in discrete optimization, because they assure integer solvability (for integer right-hand-side), i.e. we have the fundamental result that we can solve the problem through linear programming and the known LP algorithms, without considering the additional integrity constraint. That is, we can solve the problem by Linear Programming and the solution is guaranteed to be integer without resorting to additional techniques for integer programming.

A hypergraph is said to be unimodular if its incidence matrix is totally unimodular. An unimodular hypergraph has no odd cycles and is a generalization of Bipartite Graphs (See Berge (1989) and Berge (1985)). So the matching problem is well solved in bipartite graphs through the algorithm (Hopcroft and Karp (1973)), the CNF-SAT problem is well solved if we can use hypergraphs generalizing bipartite graphs, i.e. without odd cycles.

Seymour (1980) has developed an elegant scheme for checking if a generic matrix is totally unimodular that is based on regular matroids. We do not present here a complete treatment on matroid: for a survey the reader can consult (Parker and Rardin (1988), Berge (1989), Welsh (1976) and Bixby (1982).

## 4.1. Transformation of a CNF-SAT problem in an integer LP problem

We show here how we can transform a generic CNF-SAT problem in an integer LP problem of the form

```txt
min cx
Ax = b, x >= 0, x integer,
```

with A integer matrix, b, c integer vectors. Moreover, all elements of A, b, c are 0 or 1. The solution of the integer LP problem is a valid solution of the CNF-SAT problem.

We suppose to have the CNF-SAT problem in the form of section 3:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$v1:a11,a12,\ldots ,a1p1$ $v2:a21,a22,\ldots ,a2p2$ $v\dots$   
vm:am1,am2,...,ampm,
</div>

with m variables, n distinct non negated alternatives, n negated alternatives, i.e. 2n distinct alternatives.
In Karp (1972) taxonomy, the following problem is classified as NP (CNF-SAT): Given an integer matrix A and an integer vector b, does there exist a 0-1 vector x such that Ax = b?
where $a_{ij} = 1$ if xj is a literal in clause ci, -1 if negated xj is a literal in clause ci, 0 otherwise.

With this representation, the problem is NP, because the matrix A is specific of the particular instance of the CNF-SAT problem. Therefore, to say that the n-dimension CNF-SAT problem with a particular dimension n, is solvable through LP, we must test all instances of that dimension. These instances grow exponentially with the dimension of the problem.

## 4.1.1. Formal description

We present here our algorithm in formal terms and we then illustrate it through some examples.

The idea is to devise a transformation from SAT to Integer Programming in which the resulting matrix A and the right-hand-side b dependent only on the numbers of variables and clauses in the instance, not on their identity. The identity is encoded into the weight vector c.

We use a representation different in respect to that of Karp. Our representation gives a matrix A that is general and valid for any n-dimension instance of the problem, we represent the problem in general terms, as following:

(1)

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>...</td><td>a</td><td>b</td><td>c</td><td>...</td></tr><tr><td>v1</td><td>x11</td><td>x12</td><td>x13</td><td>...</td><td>x1</td><td>... x1</td><td>... x1</td><td>2n</td></tr><tr><td>v2</td><td>x21</td><td>x22</td><td>x23</td><td>...</td><td>x2</td><td>... x2</td><td>... x2</td><td>2n</td></tr><tr><td>v...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>vm</td><td>xm1</td><td>xm2</td><td>xm3</td><td>...</td><td>xm</td><td>... xm</td><td>... xm</td><td>2n</td></tr></table>

with $m, n > 0$ , where $x11, x12$ , etc. are 0-1 values to assign: 0 means the respective alternative is not chosen, 1 means it is chosen.

Then we rearrange the matrix of xij in a column vector x:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
x11 x1   
x12 x2   
$x\dots$ $x\dots$   
xm 2n $x$ 2mn
</div>

of $m$ times 2 times $n$ values.

At this point, we construct our constraint matrix $A$ . The constraints are:

(c) multiple choice constraints which ensure that exactly one of several 0-1 xij in each row must equal 1, i.e. for each variable vi and for each j of xij in (1) a 1-value must be present in the matrix A;

(e) constraints which ensure that each pair literals such as A and a, B and b, etc. (i.e. non negated and negated forms) are mutual exclusive, that is at most one of two is 1. For each couple of such a values, the respective positions in the matrix A must hold a 1-value.

## 4.1.2. Some examples

Let us illustrate our formal algorithm through some examples. For instance, if $m = 2$ , $n = 2$ , we have:

$$
\begin{array}{c c c c c c c c c c c} & A & B & a & b \\ \hline v 1 & x 1 1 & x 1 2 & x 1 3 & x 1 4 \\ v 2 & x 2 1 & x 2 2 & x 2 3 & x 2 4 \\ \hline x 1 = x 1 1 & x \text {column vector of 8 elements,} & 1 & b \text {column vector} \\ x 2 = x 1 2 & (+ 4 \text {slack variables}) & 1 & \text {of 6 elements} \\ x 3 = x 1 3 & & 1 \\ x 4 = x 1 4 & & 1 \\ x 5 = x 2 1 & & 1 \\ x 6 = x 2 2 & & 1 \\ x 7 = x 2 3 \\ x 8 = x 2 4. \\ \text {The matrix A results:} \\ \hline 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & (c) \text {type constraints} \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & (c) \text {type constraints} \\ 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & (e) \text {type constraints} \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & (e) \text {type constraints} \\ 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & (e) \text {type constraints} \\ 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & (e) \text {type constraints}. \end{array}
$$

The first row assures $x11 + x12 + x13 + x14 = 1$ , i.e. exactly one of the 0-1 x1i must equal 1, that is one alternative is chosen for the variable v1. The second row in analogous.

The third and the following rows ensure compatibility among the choices. For example, the third row ensures that $x11 + x23 <= 1$ , i.e. either A or a, in exclusive manner, is chosen. The <= is necessary here, because there may be cases where neither A nor a is chosen. As usual for the Simplex, we add a slack variable to gain equality.

It is easy to see that the number of (e)-type constraints is:

2 times $n$ times $m$ times $(m - 1) / 2$ , i.e. $2n * m(m - 1) / 2$ .

The b column vector does contain $m + 2n * m(m - 1)/2$ elements all equal 1. The c vector of the integer linear program is constructed with respect to the particular problem and serves to maximize the assignments for all variables. It does contain $m * 2n$ elements + $2n * m(m - 1)/2$ (slack) elements.

For example, if we have the problem:

```txt
For example, if we have the problem:
v1: A, b
v2: a
the c row vector is
1 0 0 1 0 0 1 0 0 0 0 0
(1 for each alternative in the problem)
```

which is then transformed in

to obtain a minimization problem from the original maximization, as required.

After a suitable Simplex procedure, we find for the above example the following Tableau:

<table><tr><td>2</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>-1</td><td>0</td><td>0</td><td>-1</td></tr><tr><td>1</td><td>0</td><td>-1</td><td>-1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr></table>

which gives for the non-basic variables the usual zero values:

$x2 = 0 = >x12 = 0$ (in the original matrix)

$$
x 3 = 0 = > x 1 3 = 0
$$

$$
x 5 = 0 = > x 2 1 = 0
$$

$$
x 6 = 0 = > x 2 2 = 0
$$

$x9 = 0 = >x01 = 0$ (slack variable in the original constraints)

$$
x 1 2 = 0 = > x 0 4 = 0 (\text { slack   variable })
$$

and for the 6 basic variables:

$$
x 1 = b 1 = 0 = > x 1 1 = 0
$$

$$
x 4 = b 8 = 1 = > x 1 4 = 1
$$

$$
x 7 = b 3 = 1 = > x 2 3 = 1
$$

$$
x 8 = b 2 = 0 = > x 2 4 = 0
$$

$$
x 1 0 = b 4 = 1 = > x 0 2 = 1 (\text { slack   variable })
$$

$$
x 1 1 = b 5 = 1 = > x 0 3 = 1 (\text { slack   variable })
$$

The meaning is:

$x23 = 1 = >v2$ is assigned to $a$

$x02 = 1$ , $x03 = 1$ slack variables equal to 1 (because $A$ is not chosen for $v1$ , etc.).

The objective function is minimized for -2, i.e. it is maximized for a value of 2, that is the two variables to which assign a value.

Note that for each variable exactly one alternative is chosen, then the only way to maximize the objective function is to give an assignment to all variables and the choice must be one where the corresponding alternative is present. Thus the original problem is solved.

The matrix A is general and valid for any 2-variables problem, the c vector is specific.

Consider now the 3-variables case, i.e. the case with $m = n = 3$ . If we re-order the alternatives, we find:

<table><tr><td></td><td>A</td><td>a</td><td>B</td><td>b</td><td>C</td><td>c</td></tr><tr><td>v1</td><td>x11</td><td>x12</td><td>x13</td><td>x14</td><td>x15</td><td>x16</td></tr><tr><td>v2</td><td>x21</td><td>x22</td><td>x23</td><td>x24</td><td>x25</td><td>x26</td></tr><tr><td>v3</td><td>x31</td><td>x32</td><td>x33</td><td>x34</td><td>x35</td><td>x36</td></tr></table>

<table><tr><td>3</td><td>0</td><td>1</td><td>0</td><td>10</td><td>1</td><td>0</td><td>1</td><td>10</td><td>1</td><td>1</td><td>10</td><td>1</td><td>1</td><td>1</td><td>1</td><td>10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>11</td><td>1</td><td>0</td><td>0</td><td>00</td><td>0</td><td>0</td><td>00</td><td>0</td><td>0</td><td>0</td><td>000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</td><td>1</td><td>0</td><td>0</td><td>0</td><td>00</td><td>0</td><td>1</td><td>1</td><td>11</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>11</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>00</td><td>0</td><td>1</td><td>1</td><td>11</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>00</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>00</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>-1</td><td>-10</td><td>-1</td><td>-1</td><td>-1</td><td>-10</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-10</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-10</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

where for simplicity only the 1-values are reported. Consider the following instance of the 3-variables case:

A. Monfroglio / Logic decisions under constraints

which gives for the non-basis variables the zero-values, and for the 21 basis variables:

$$
x 5 = 1, x 1 0 = 1, x 1 4 = 1 (\text { non   slack }) = > v 1: C, v 2: b, v 3: a = > A = B = \text { FALSE }, C = \text { TRUE }
$$

$$
x 1 9 = 1, x 2 0 = 1, x 2 1 = 0, x 2 2 = 1, x 2 3 = 0, x 2 4 = 1, x 2 5 = 0, x 2 6 = 1, x 2 7 = 1, x 2 8 = 1,
$$

$$
x 2 9 = 0, x 3 0 = 1, x 3 1 = 0, x 3 2 = 1, x 3 3 = 1, ^ {\prime} c 3 4 = 0, x 3 5 = 1, x 3 6 = 1, (\text { slack   variables }).
$$

## 4.2. Outline of soundness.

In general the matrix A is constructed with modules of the matrices for the problems with lower dimensions and has an even repetition schema for any dimension of the original problem, that is by means of a recursive use of modules from constructions for smaller values of the parameters of our problem.

Testing Total Unimodularity of our matrix A for any dimension m can be done efficiently, by means of Seymour's algorithm and Seymour's theorem, because our problem representation gives a general matrix A for an n-dimension CNF-SAT case. Seymour's theorem for recognizing totally unimodular matrices, decomposes the matrix in typical building blocks and checks these blocks to see whether the corresponding component matroids are graphic, cographic or isomorphic to a special totally unimodular matrix not arising from any graph.

All such decompositions can be produced in polynomial time and checking the blocks can also be done in polynomial time. Thus regularity of a matroid and total unimodularity of a matrix can be determined in polynomial time.

However, total unimodularity is not strictly necessary for our approach.

## 4.2.1. Theorem 1. The matrix $A$ is integer solvable in the $n$ -CNF-SAT for $n > = 3$

Note that the proof is not the same for the 2-case. In fact, the 2-case is a special case because every column has only two 1-values and the LP of matrix A is said to be a generalized-network problem (Bixby, 1982).

We know in fact that the 2-CNF-SAT problem is well solved. With $m > 2$ , every column has $q > 2$ 1-values and the proof should be totally different: we can't say that if the 2-case has a totally unimodular matrix, the $m$ -case has a totally unimodular matrix too.

Proof. Our general procedure for solving the integer problem is the following: (1) consider the linear program in the general form of the section 4.1.1; (2) consider the obtained Simplex Tableau; (3) for some negative values in the first row of such a Tableau, i.e. in the row of vector c, operate a pivot operation in the correspondent column and in a suitable row of the first m rows of the matrix A, i.e. in the rows $2\ldots(m+1)$ of the Tableau, until the Tableau is in the canonical form. Note that these pivot operations may be chosen in m! different ways and in general may require m! steps. Moreover, if the instance of the SAT problem (encoded in the vector c) does not have a solution, we cannot obtain such a canonical form and the Tableau given a bi<0 with all $a_{ij}(j=1,\ldots)=0$ .

The pivot-operation is performed as follows:

(1) choose a $cj < 0$ in the first row of the Tableau with a $aij > 0$ in the column $j$ (note that there always exists such a term $aij > 0$ because the matrix $A$ has all 0-1 values)

(2) add the row $i$ to the first row in the Tableau

(3) if in the column $j$ there are terms $akj > 0$ then consider the row $k$ and subtract the row $i$ from the row $k$

(4) repeat the step (3) for all $akj > 0$

Remember that the matrix A has all terms 0 or 1. After the steps (1), (2), (3) and (4), the matrix A contain 0, 1 - 1 values. The solution is always integer.

We say that a linear program is in canonical form if - given $S = \{s1, s2, \ldots, sp\}$ with $p$ integer values ( $p$ is the number of rows in the matrix $A$ , i.e. the number of equations)

\- $Cs = \{Cs1, Cs2, \ldots Csp\}$ column vector of dimension $p$ obtained from the $c$ vector of the original problem

\- $As =$ identity matrix $Ip$ of dimension $p$ ( $p =$ the number of rows in matrix $A$ )

$$
- C s = 0
$$

For our matrix $A$ , there are $m * 2n + 2n * m(m - 1)/2$ columns and $m + 2n * m(m - 1)/2$ rows.

We must provide an identity matrix of dimension $p = m + 2n * m(m - 1)/2$ . The module (4) of our matrix A, as we have shown at the beginning of this section, offers us an identity matrix of dimension $2n * m(m - 1)/2$ . We must add m columns and m rows. We achieve this result by performing m pivot-operations.

After these m pivot-operations in the $2\ldots(m+1)$ rows of the Tableau, it is easy to see that the c vector (that is the first row of the Tableau) has all values > = 0. The $2\ldots(m+1)$ rows in fact have the structure

$$
\begin{array}{c c c c c c c c c c c} 1 & 1 & \ldots & 1 \\ & & & & 1 & 1 & \ldots & 1 \\ & & & & & & & 1 & 1 & \ldots & 1 \end{array}
$$

etc.

Thus, after adding these rows to the first row (the c vector of the original LP problem), the first row becomes > = 0, because all -1 values are reduced to 0-values.

In a LP problem in canonical form, there always exist an admissible solution, called basic solution:

$$
\begin{array}{l} X s i = b i i \text { in } \{1, 2, \dots , P \} \\ X j = 0. \end{array}
$$

The fundamental theorem of the Simplex Algorithm ensures that the basic solution is optimal because our c has all values > = 0, and the special form of the matrix A ensures that the solution is integer too. So, the key result is to have our LP in canonical form.

In general, without considering any particular instance of the SAT problem, it is always possible to perform m pivot operation and to preserve the solvability of the LP, that is to avoid cases of bi < 0 with all $a_{ij} = 0$ . In fact, the matrix A, as one can easily see, does always permit such a pivot operation.

Suppose for absurd that each pivot operation in a row does not permit successive pivot operations which preserve LP solvability: that would mean each assignment of a variable in the correspondent clause would be not admissible which is absurd.

Of course, our matrix A (for each n dimension) cannot present that situation, as one can easily see. Each pivot-operation in the first m rows of matrix A is incompatible with only one pivot-operation in an other of the first m rows.

For example:

$$
\begin{array}{c c c c c c c c c c c c c} \underline {{1}} & 1 & 1 & 1 & 1 & 1 \\ & & & & & 1 & 1 & 1 & 1 & 1 & 1 \\ \underline {{1}} & & & & & \underline {{1}} \\ \text {etc.} \end{array} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad
$$

A pivot-operation in a11 is incompatible with a pivot-operation in a28. This is obvious because the assignment A in the first clause is incompatible with the assignment a in the second clause.

We can conclude that it is general always possible to make m pivot operation in the first m rows to reduce the matrix A in echelon form.

Thus the Simplex algorithm provides at least one integer solution, if the n-CNF-SAT problem has a solution.

Of course, there may be additional non-integer solutions for the LP that are useless for us to solve CNF-SAT.

The Karmarkar's algorithm must be able to find all solutions the Simplex finds, i.e. the integer solutions too. However, Karmarkar's algorithm has the additional property to be polynomial in the worst case complexity.

We must then observe that the total unimodularity of the matrix A is not strictly necessary for our problem to be solvable. The total unimodularity is a stronger property that gives extreme points of the LP problem are integer for any integer right-hand side b. Our problems have a special b vector of all 1-values and a special A matrix. It is sufficient that our m-CNF-SAT Integer Problem has the same type of A-matrix and b-vector as the 3-CNF-SAT Integer Program. This is our case.

W must then prove that the solution of the integer program derived from the original CNF-SAT problem is a solution for the latter and that if the CNF-SAT problem has a solution the IP problem has a solution too.

## 4.2.2. Correctness

The integer program solution provides exactly one alternative for each variable among the set of available choices, thus each variable is assigned a value.

The e-type constraints of section 4.1 assure no incompatible values can be chosen, so the solution is admissible.

In conclusion, the solution of the IP is always a solution for the CNF-SAT problem.

## 4.2.3. Completeness

One can be in doubt whether there may be cases where the IP has no finite solution for an original CNF-SAT problem which is solvable.

The Simplex convergence theory assures that a LP, in canonical form, after a finite number of steps, show either an optimal solution or that the objective function is not limited.

Suppose that a CNF-SAT has a solution then the associate LP problems has every time a solution, because all variables have an assignment and thus all rows have exactly one element = 1, all (e) constraints of section 4.1 are satisfied and the objective function is maximized.

In conclusion the Simplex algorithm must find such a solution in a finite (may be exponential) number of steps. Moreover, the special form of the matrix A ensures that this solution is an integer solution too.

## 4.3. Complexity

The matrix A is bigger than for the well known default transformation method, but has a regular structure and is no longer problem specific.

The worst case complexity in the dimensions $[m * n]$ of our original CNF-SAT problem is for our algorithm

number of columns: $m \times 2n + 2n \times m(m - 1)/2$

number of rows: $m + 2n * m(m - 1)/2$ .

If we consider the case where $m = n$ , we have:

$$
c = n ^ {3} + n ^ {2}
$$

$$
r = n ^ {3} - n ^ {2} + n
$$

giving a cubic Worst Case Complexity (we must then add the complexity of solving Linear Programming). However, we have considered the complete-case, i.e. the case where for each variable each alternative is present. This is not the case of course: if all alternatives are present the problem is yet solved.

Thus the number of constraints that are necessary is always lower and so the complexity.

It is well known that the Simplex is exponential in the worst case, but typically requires a low-order polynomial number of steps to compute an optimal solution. We have investigated the average performance of the algorithm described in the present paper, under reasonable assumptions on random data and in typical situations: if n = number of clauses, m = number of literals for $n = m$ , $n \gg m$ , $n \ll m$ . The average-time performance was very favourable, as expected. It is important to observe that we have used a C language compiled function that implements the simplex algorithm for linear programming and in general does not obviously guarantee the integrity of the result. As an experimental evidence of our technique, all results were integer.

We have tested the approach through the Karmarkar's algorithm too and the result is accord of the well known advantages ad disadvantages of the two algorithms. The first presentation of the present work is Monfroglio (1991).

## 5. Conclusions

We have implemented the above presented algorithms during a six years long research on logic constraint solving and discrete combinatorial optimization aiming to reduce or eliminate the backtracking (Monfroglio 1986, 1987, 1988, 1989, 1991 and 1992).

The first technique is well suited as a stand-alone part of a decision support system, the second algorithm may be incorporated in a constrained logic programming (CLP) language for the implementation of a decision support system.

Let us show some limitations. From a complexity point of view all NP-hard problems can be polynomially transformed in CNF-SAT. However, practical experience seems to indicate that this transformation does not always yield computationally satisfactory results when compared with a direct constraint propagation method. Thus, additional research effort is needed.

Moreover, from a CLP (Constrained Logic Programming) language point of view, our technique requires additional work. For example, a general problem solver should be incremental, i.e. one can add constraints after some reasoning steps have already been performed, without having to restart the computation completely.

## Acknowledgements

I am very grateful to professor Maurice Nivat, Chevilly-Larue, France, for determinant suggestions and encouragement on this work, and to Dr. Hans-Jochen Schneider, Editor-in-chief for DSS and Dr. Dimitris Karagiannis, assistant to editor-in-chief.

## References

[1] Bahgat R., S. Gregory, Pandora: Non-deterministic Parallel Logic Programming, Imperial College, London, 1988.

[2] Balas E., Disjunctive Programming: Cutting Planes from Logical Conditions, in Nonlinear Programming 2, Academic Press, New York, 1975, pp. 279–312.

[3] Berge C., Graphs, Second revised edition, North-Holland, Amsterdam, 1985.

[4] Berge C., Hypergraphs, North-Holland, Amsterdam, 1989.

[5] Bixby R.E., Matroids and Operations Research, in H. Greenberg, F. Murphy, S. Show, Advanced Techniques in O.R., North-Holland, Amsterdam, 1982, pp. 333–458.

[6] Brown C., P. Purdom Jr., An Average time analysis of backtracking, SIAM J. Comput., 10 (1981), pp. 12–26.

[7] Chvatal V., Cutting Planes in Combinatorics, European Journal of Combinatorics, 6, 1985, pp. 217–226.

[8] Cook S.A., The Complexity of Theorem Proving Procedures, Proc. 3rd ann. ACM Symp. Theory Comput. (1971), pp. 151–158.

[9] Daniel L., Planning and Operation Research, in Artificial Intelligence, (Eisenstadt, Harper & Row, 1983).

[10] Dechter R., J. Pearl, Network-based heuristics for constraint-satisfaction problems, Artificial Intelligence, vol. 34, 1, 1988, pp. 1–38.

[11] Dechter R., J. Pearl, Tree Clustering for Constraint Networks, Artificial Intelligence, Vol. 38, 3, 1989, pp. 353–366.

[12] Dechter R., Enhancement Schemes for Constraint Processing: Backjumping, Learning, and Cutset Decomposition, Artificial Intelligence, vol. 41, 3, 1990 pp. 273–312.

[13] Dhar V., N. Ranganathan, Integer Programming vs. Expert System: An Experimental Comparison, CACM, 1990, pp. 323–337.

[14] Dincbas M., H. Simonis, P. Van Hentenryck, Solving a cutting-stock problem in Constraint Logic Programming, Proceedings of the 5th International Conference and Symposium on Logic Programming, R.A. Kowalski and K.A. Bowen eds., MIT PRESS, Cambridge, Mass., 1988, pp. 42–58.

[15] Edmonds J., Maximum Matching and Polyhedron With 0,1-Vertices, Journal of Research of the National Bureau of Standards(B), 69, (1965), pp. 125–130.

[16] Fox M., why is scheduling difficult? A CSP perspective, Proceedings of ECAI'90, 1990.

[17] Fox M.S., Problem Topology, texture and Objectives, AIIA News, Vol. III, N.3, 1991.

[18] France J., M. Paull, Probabilistic analysis of the Davis Putman procedure for solving the satisfiability problem, Discrete Applied Mathematics, Vol. 5, 1983.

[19] Freuder E.C., A sufficient condition of backtrack-free search, J. ACM 29, 1 1982, pp. 24–32.

[20] Gallio G., G. Urbani, Algorithms for Testing the Satisfiability of Propositional Formulae, Journal of Logic Programming, North-Holland, Amsterdam, 1989.

[21] Garey M.R. e D.S. Johnson, Computer and Intractability, (Freeman, San Francisco, 1979).

[22] Gomory R.E., An Algorithm for Integer Solutions to Linear Programs, in Recent Advances in Mathematical Programming, McGraw-Hill, New York, 1963, pp. 269–302.

[23] Grant T., Lessons for O.R. from A.I.: A Scheduling Case Study, Journal of the Operational Research Society, 37 (1), (1986), pp. 41–57.

[24] Hoffman A.J., J.B. Kruskam, Integral Boundary Points of Convex Polyhedra, in Linear Inequalities an Related Systems (H.W. Kuhn and A.W. Tucker eds). Princeton University Press, Princeton, 1956, 223–246.

[25] Hopcroft, R. Karp, The matching problem for bipartite graphs, in SIAM J. Comput., (1973) pp. 225–231.

[26] Iwama K, Complementary Approaches to CNF Boolean Equations, in Discrete Algorithms and Complexity, edited by D.S. Johnson, T. Nishizeki, A. Nozaki, H.S. Wilf, Proc. Japan-US Joint Seminar, Kyoto, Japan, 1986, Academic Press, Orlando (1987) pp. 223–236.

[27] Jaffar J. and J.L. Lassez, Constraint Logic Programming, Proceeding of the Conference on Principles of Programming Languages, Munich, 1987.

[28] Karmarkar N, A New Polynomial Time Algorithm for Linear Programming, in Proceedings of the 16th Annual ACM Symposium on Theory of Computing, 1984, pp. 302–311.

[29] Karp R.M., Reducibility Among Combinatorial Problems, in Complexity of Computer Computations (R.E. Miller and J.W. Thatcher, eds), Plenum Press, New York, 1972, pp. 85–103.

[30] Khachian L.G., A Polynomial Algorithm for Linear Programming, Soviet Mathematics Dklady, Nauk USSR, 1979, pp. 191–194.

[31] Mackworth A.K. & E.C. Freuder, The complexity of some polynomial network consistency algorithms for constraint satisfaction problem, A.I. Vol. 25, N. 1 (1985), pp. 65–74.

[32] Martelli A. & U. Montanari, Optimization Decision Trees Through Heuristically Guided Search, CACM, Vol. 21, N. 12 (1978), pp. 1025–1039.

[33] Megiddo N., Towards a Genuinely Polynomial Algorithm for Linear Programming, SIAM Journal on Computing, V. 12, 1983, pp. 347–353.

[34] Micali S., V.V. Vazirani, An algorithm for finding maximum matching in general graphs, Proceedings of the 21st Annual Symposium on the Foundation of Computer Science, IEEE, New York, (1980), pp. 17–27.

[35] Monfroglio A., School Time Table Scheduling in Prolog, SIGART newsletter, N. 96, (1986), pp. 20–22.

[36] Monfroglio A., Soddisfacimento di vincoli e programmazione logica parallela, Rivista di informatica, Vol. XVI, n. 4, (1986), 353–364.

[37] Monfroglio A., Soddisfacimento di vincoli e allocazione di risorse condvise: un algoritmo polinomiale deterministico (Constraint satisfaction and resource allocation: a polynomial time deterministic algorithm), Rivista di Informatica, A.I.C.A., Vol. XVII, n. 4, (1987), pp. 307–315.

[38] Monfroglio A., A graphical interface to logic programming, SIGART Newsletter, N. 101, (1987), pp. 26–28.

[39] Monfroglio A., A General Logic Constraint Solver, Operations Research and Artificial Intelligence, A.I.R.O. Pisa, (1988) pp. 29–44.

[40] Monfroglio A., Timetabling through a deductive data base, a case study, Data & Knowledge Engineering, North Holland, Amsterdam, N. 3 (1988), pp. 1–27.

[41] Monfroglio A., Efficient Logic Constraint Satisfaction, in Atti Congresso Annuale A.I.C.A., Trieste, Italy, 1989, pp. 167–182.

[42] Monfroglio A., General Heuristics for Logic Constraint Satisfaction, in Proceedings of the first AIIA Conference, Trento, Italy, 1989, pp. 306–315.

[43] Monfroglio A., Un algoritmo per il problema del Commesso Viaggiatore basato sull'Allocazione di Risorse Condivise (A resource allocation based algorithm for the Traveling Salesman Problem), Rivista di Informatica A.I.C.A., 4/1989 pp. 359–367.

[44] Monfroglio A., Connectionist networks for constraint satisfaction, Neurocomputing, Elsevier Science, Amsterdam, 3, 1991, pp. 29–49.

[45] Monfroglio A., Integer programs for logic constraint satisfaction, Theoretical Computer Science, the Journal of the EATCS, North-Holland, vol. 97, 1992, pp. 105–130.

[46] Montanari U., Networks of constraints: fundamental properties and applications in picture processing, Inform. Sci. 7 (1974), pp. 95–132.

[47] Montanari U., F. Rossi, Exact solution in linear time of Network of Constraints using Perfect Relaxation, in Ronald Brachman, Hector Levesque and Ray Reiter editors of the Proceedings of the first international conference of knowledge representation and reasoning, 1989.

[48] Montanari U., Francesca Rossi, Constraint relaxation may be perfect, Artificial Intelligence, Vol. 48, Number 2, march 1991, Elsevier Science, Amsterdam, pp. 143–170.

[49] Pai-chun Ma, F.H. Murphy, E.A. Stohr, A Graphical Interface for Linear Programming, CACM, Vol. 32, N. 8, 1989, pp. 996–1012.

[50] Papadimitriou C.H., M. Yannakakis, The Complexity of Facets (and Some Facets of Complexity), in Proceedings of the Fourteenth Annual ACM Symposium on Theory of Computing, San Francisco, 1982, pp. 244–259.

[51] Parker R.G., R.L. Rardin, Discrete Optimization, Academic Press, San Diego, CA, 1988.

[52] Phelps R.I., Artificial Intelligence- An Overview of Similarities with O.R., Journal of the Operational Research Society, 37, (1), (1986), pp. 13–20.

[53] Purdom P., C. Brown, An analysis of backtracking with research rearrangement", SIAM J. Comput., 12 (1983), pp. 436-449.

[54] Rich E., Artificial Intelligence, McGraw-Hill, (1983).

[55] Rossi F., Constraint Satisfaction Problems in Logic Programming, SIGART Newsletter, N. 106, (1988).

[56] Sasaki G.H., B. Hajek, The time complexity of Maximum Matching by Simulated Annealing, Journal of ACM, Vol. 35, N.2, (1988), pp. 387–403.

[57] Seymour P.D., Decomposition of Regular Matroids, Journal of Combinatorial Theory, 1980, pp. 305–359.

[58] Simonis H., M. Dincbas, Propositional Calculus Problems in CHIP, in Algebraic and Logic Programming, 2nd Int. Conf. Nancy, France, 1990, H. Kirchner, W. Wechler Eds., Springer Verlag, Lectures Notes in Computer Science N. 463, 1990 pp. 189–203.

[59] Steels L., Artificial Intelligence and Complex Dynamics, Note di Software, Univ. Milano & Bull systems, Milano, 1988.

[60] Sussman G.J. & G.L. Steele Jr., Constraints: A Language for Expressing A most-Hierarchical Descriptions, A.I., Vol. 14, (1980).

[61] Tsiligirides T., Heuristic Methods Applied to Orienteering, J. Op. Res. Soc., 9, 1984.

[62] Van Hentenryck P. and M. Dincbas, Forward checking in Logic Programming, Fourth International Conference on Logic Programming, Proc., Melbourne, Australia, (1987), pp. 229–256.

[63] Van Hentenryck P., A Framework for Consistency Techniques in Logic Programming, IJCAI Proc., Milan, Italy, (1987), pp. 2–8.

[64] Van Hentenryck P., A Constraint Approach to Mastermind in Logic Programming, SIGART Newsletter, N. 103, 1988, pp. 31–34.

[65] Van Hentenryck P., Constraint Satisfaction in Logic Programming, MIT PRESS, Cambridge, 1989.

[66] Veinott, A.F., G.B. Dantzig, Integral Extreme Points, SIAM Review, 10, 1968. pp. 371–372.

[67] Welsh D., Matroid Theory, Academic Press, New York, 1976.
