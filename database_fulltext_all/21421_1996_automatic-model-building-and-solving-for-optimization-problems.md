---
otero_id: 21421
otero_key: "MCW3JR76"
title: "Automatic model building and solving for optimization problems"
authors: "Junichi Iijima"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)80005-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Automatic model building and solving for optimization problems

Junichi Iijima \*

Department of Industrial Management and Systems Engineering, Tokyo Institute of Technology, 2-12-1, O-okayama, Meguro-ku, Tokyo, 152, Japan

## Abstract

Automatic modelling is one of the key topics in model base management in DSS. We consider the design and implementation of a system which automatically specifies an optimization model from an abstract form with a given set of data specified by a user and solves it by calling an appropriate solver. We implement our idea as a prototype in Prolog and illustrate its validity by simple examples.

Keywords: Automatic modelling; Model base management; Optimization model

## 1. Introduction

Research on model base management is one of the main streams in decision support systems research. There are two main topics in model base management. One is on model description language and the other is on construction of models from modules.

One of the well-known approaches in the first category is to use a graphical modelling language to support modelling. Structural modelling by Geoffrion [1] is well-known in this direction. Murphy and Stohr developed a system in which a user can formulate a linear programming (LP) problem using a graph-based environment [2]. Most of these researches are focused on LP problems as their application.

In the latter topic, most researches are on joining AI techniques with LP models. Liang discussed the use of analogical reasoning and case-based learning to help model builders apply their experiences in modelling to construct a new model [3]. Binbasioglu also discussed the role of analogy in model construction and the process analogy approach in which modelling process, not the resultant model, is a target to be transferred analogically to construct new models [4]. Lee et al. discussed the post-model analysis with rule-based systems [5].

Recently, automatic model building is becoming one of the key topics in model base management. It can be also considered as a unification of AI with optimization for DSS. Krishnan designed PM\*, which is a first-order logic based language to help non-expert users construct LP models in the production, distribution and inventory planning fields [6]. He also implemented a tool called PDM based on Prolog [7]. Most of the researches in this context are also focused on LP problems.

In this paper, we propose a more general and abstract approach in automatic model building and solving for optimization problems. A model in this paper is simply an optimization model including LP and non-LP. Simultaneous linear/nonlinear equations are included as well. Our motivation of the paper is the fact that it depends on the substitution of data for variables whether a model is linear or nonlinear.

Let us illustrate our motivation by a simple example. Let us consider the following optimization model.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
minimize  $a * x * x + b * x + c * y$ 
subject to  $d * x + e * y - r = f$ $g * x + h * y - s = i$
</div>

If we know data such that

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$a = 0, b = 1.5, c = 1, d = 2.5, e = 5, f = 150, g = 5,$ $h = 2, i = 120,$
</div>

then it becomes the following LP model and we can solve it by an appropriate solver such as $LINDO^{TM}$ .

```ini
minimize 1.5 * x + y
subject to 2.5 * x + 5 * y - r = 150 .
5 * x + 2 * y - s = 120
```

Let us next suppose that we know data such that $a = 1, b = -2, y = r = s = d = f = g = i = 0$ ,

then it becomes the following unconstrained NLP model and we can solve it by an appropriate solver based on Newton's method and so on.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
minimize $x * x - 2 * x$.
</div>

While if we know data such that

$$
a = b = c = 0, d = 2. 5, e = 5, f = 1 5 0, r = 0, g = 5,
$$

$$
h = 2, s = 0, i = 1 2 0,
$$

then the model becomes the following simultaneous linear equation model and we can solve it by an appropriate solver based on the LU-decomposition method and so on.

```txt
2.5 * x + 5 * y = 150
5 * x + 2 * y = 120
```

The above example shows that the same model can be transformed to LP, unconstrained NLP and a simultaneous linear equation depending on the data and the choice of variables to be substituted by those data. Therefore it is useful if we can separate models, data and solvers, and connect them automatically in an appropriate way.

In this paper, we firstly define several basic mathematical concepts in order to formulate our ideas using set-theoretical notions. Secondly, we give a procedure in which we convert a given abstract optimization model into a specific optimization model in normal form by assigning data, pass it to an appropriate solver and get the solution by the solver automatically. And we discuss the implementation of our idea. Our system is written in Prolog and we explain how to realize the functions that are formulated in Section 2 in Prolog. Finally, we illustrate its behaviour by simple examples.

Our approach in this paper is to unify numeric calculation and symbolic manipulation in the following sense. Target problems belong to the class of optimization problems and a concrete optimization problem is constructed by assigning values for variables in a given abstract optimization problem through symbolic manipulation in Prolog. Then the formulated optimization problem is solved by an appropriate solver using numeric calculation. Since symbolic manipulation can be understood as a typical characteristic of AI, our approach can be considered as one way of unification of AI with optimization for decision support. It is popular to consider problem solving consisting of three phases such as identification, analysis and evaluation. In optimization problems, it is an optimal solution for a given problem that is to be sought. Then the analysis phase and evaluation phase can be considered as one phase, that is, the solving phase. In our approach, we use an AI approach in the problem identification phase and an OR approach in the problem solving phase.

## 2. Mathematical formulation

Let us next define several basic concepts using set-theoretical notions. In model theory [8], we interpret constant symbols, function symbols and relation symbols as corresponding elements, operations and relations on a given underlying set. Then we have a formula to be decided as true or false on the mathematical structure after assigning values to variables in the formula. In this paper, we only focus on polynomials over the set of reals. Therefore we interpret our language on the set of reals.

## Definition 1. Polynomial on reals

Let $V = \{v_{1}, \ldots, v_{n}\}$ be a set of variables. The set of polynomials on reals over V is defined inductively as follows,

1. variable in V is a polynomial on reals over V,

2. real number $r \in R$ is a polynomial on reals over $V$ ,

3. if $t_{1}$ and $t_{2}$ are polynomials on reals over V, so are

$$
t _ {1} + t _ {2}, t _ {1} - t _ {2}, t _ {1} * t _ {2}, t _ {1} / t _ {2} \text {   if   } t _ {2} \neq 0,
$$

4. polynomials on reals over V are those and only those which we get from the above way in a finite number of steps.

Let $V = \{v_{1}, \ldots, v_{n}\}$ be a set of variables and $P(V)$ denote the set of polynomials on reals over $V$ .

We use $p(v_{1},\ldots,v_{n})$ to denote a polynomial whose variables form a subset of $\{v_{1},\ldots,v_{n}\}$ .

## Definition 2. Constraint

A constraint over $V = \{v_{1},\ldots ,v_{n}\}$ is of the form

$$
\left(p \left(v _ {1}, \dots , v _ {n}\right), o p, q \left(v _ {1}, \dots , v _ {n}\right)\right),
$$

where $p$ and $q$ are polynomials on reals over $V$ and $op \in \{=, \langle, \rangle, \leq, \geq\}$ . The set of constraints over $V$ is denoted by $Const(V)$ .

As a notation, we use objPrinciple = {max,min} to denote the set of the directions of optimization.

In this paper, we use the terms “abstract” and “specific” that have slightly different meanings as used in [4]. An abstract model is an optimization model before assigning values for variables.

## Definition 3. Optimization model

An optimization model over $V$ is a couple $\left(\{(o_1, p_1), \ldots, (o_k, p_k)\}, \{c_1, \ldots, c_m\}\right)$ , where $o_i \in objPrinciple$ , $p_i$ is a polynomial on reals over $V$ for $i = 1, \ldots, k$ and $c_i \in Const(V)$ for $i =$

1,...,m. That is, an optimization model is an element in $P(objPrinciple \times P(V)) \times \mathcal{P}\}(Const(V)) - \{(\emptyset, \emptyset)\}$ . Let us denote the set by $OM(V)$ .

By the above definition, it is possible to have an optimization problem such as $(\emptyset, \{c_1, \ldots, c_m\})$ and $\{(\{o_1, p_1), \ldots, (o_k, p_k)\}, \emptyset\}$ . The former is called an equational type model and the latter an unconstrained optimization model. Since it is meaningless to consider the case $(\emptyset, \emptyset)$ , we exclude it from $OM(V)$ .

Let $data:(V)\to R$ be a partial function which assigns values for variables in $dom(data)$ , where $dom(data)$ denotes the domain of the partial function data. Then the assignment is defined as follows.

## Definition 4. Assignment

A function $assign(data): P(V) \to P(D)$ , where $D = V \sim dom(data)$ , is inductively defined as follows,

1. assign(data)(v) = data(v), v ∈ V - D,

2. assign(data)(v) = v, v ∈ D,

3. assign(data)(r) = r, r ∈ R,

4. if assign(data)(t₁) = s₁
    and assign(data)(t₂) = s₂, then
    assign(data)(t₁ + t₂) = s₁ + s₂,
    assign(data)(t₁ \* t₂) = s₁ \* s₂,
    assign(data)(t₁ - t₂) = s₁ - s₂,
    assign(data)(t₁ / t₂) = {s₁ / s₂  s₂ ≠ 0
    0 otherwise.

Let V be a set of variables in a problem and $D \subset V$ a set of decision variables. Let $p(v_{1}, \ldots, v_{n})$ be a polynomial on reals over V. Then we will have a polynomial on reals over D by assigning data for variables in V - D.

We call a constraint over V an “abstract” constraint and a constraint over D a “specific” one.

## Definition 5. Specialization

Let $data:(V)\to R$ be a function. Then we define a function specialize(data): $OM(V)\to OM(D)$ , where $D=V-dom(data)$ , as follows.

$$
\begin{array}{c} \text {specialize} (d a t a) \big (\big \{(o _ {1}, r _ {1}), \ldots , (o _ {k}, r _ {k}) \big \}, \\ \big \{(p _ {1}, o p _ {1}, q _ {1}), \ldots , (p _ {m}, o p _ {m}, q _ {m}) \big \} \big) \end{array}
$$

$$
\begin{array}{l} = \big (\big \{o _ {1}, a s s i g n (d a t a) (r _ {1}) \big), \ldots , \\ \big (o _ {k}, a s s i g n (d a t a) (r _ {k}) \big) \big \}, \\ \big \{\big (a s s i g n (d a t a) (p _ {1}), o p _ {1}, a s s i g n (d a t a) (q _ {1}) \big), \\ \ldots , \big (a s s i g n (d a t a) (p _ {m}), o p _ {m}, a s s i g n (d a t a) \\ \times (q _ {m}) \big) \big \} \big). \end{array}
$$

Let us next define the concept of models in normal form.

Definition 6. Constraints in normal form
A constraint in normal form over $V = \{v_{1}, \ldots, v_{n}\}$ is of the form

$$
\big (p \big (v _ {1}, \dots , v _ {n} \big), o p, r \big),
$$

where $p$ is a polynomial on reals over $V$ with no constant subterms, $op \in \{= , < , > , \leq , \geq \}$ and $r \in R$ .

The set of constraints in normal form over V is denoted by $\text{ConstNorm}(V)$ .

Let us call an element in $P(objPrinciple \times P(D)) \times ConstNorm(D) - \{(\emptyset, \emptyset)\}$ a specific optimization model in normal form. And let us denote the set by $OMN(D)$ .

Conversion of a specific optimization model into that in normal form can be formulated as follows.

Definition 7. Normalization

A function normalize: $OM(D) \rightarrow OMN(D)$ is defined as follows,

$$
\begin{array}{l} \text { normalize } \big (\{(o _ {1}, r _ {1}), \dots , (o _ {k}, r _ {k}) \}, \\ \big \{(p _ {1}, o p _ {1}, q _ {1}), \dots , (p _ {m}, o p _ {m}, q _ {m}) \big \} \big) \end{array}
$$

$$
\begin{array}{l}= \left(\left\{\left(o _ {1}, r _ {1}\right), \dots , \left(o _ {k}, r _ {k}\right) \right\}, \right.\\\left\{\left(p _ {1} ^ {\prime}, o p _ {1}, s _ {1}\right), \dots , \left(p _ {m} ^ {\prime}, o p _ {m}, s _ {m}\right)\right\}\left. \right),\end{array}
$$

where $p_i - q_i = p_i' - s_i, p_i'$ has no constant subterms and $s_i \in R$ .

Consequently, we can define a conversion of an abstract optimization model into a specific optimization model in normal form by the juxtaposition of assign(data) and normalize.

From now on, we will discuss optimization models with a single objective function for the sake of simplicity. Generally, optimization models can be categorized as shown in Table 1.

According to Table 1, we define a mapping that assigns each specific optimization model in normal form over V to the corresponding problem type.

Let us define a mapping categorize-Problem: OMN(D) → Problems, where Problems is a set of problems. The definition of Problems depends on implementation. For example, we use Problem = {LP,NLP,SLE,SNLE} in our present prototype. According to the problem categorization, we call a corresponding solver for each problem. Let Solver be a set of solvers. Then we can define the solver assignment function assignSolver: Problem → Solver such that assignSolver(problem) is a solver for the problem, problem. It also depends on the implementation what sort of solvers is assigned for each problem. We will state this in the next section.

## 3. Design and implementation

Let us next show the idea of modelling and solving optimization problems in this paper using concepts formulated in the previous section. We design a system in which a user follows the following steps.

Table 1  
Categorization of problems $^{a}$

<table><tr><td>Objective function constraints</td><td>None</td><td>Linear</td><td>Quadratic</td><td>Nonlinear</td></tr><tr><td>None</td><td>-</td><td>-</td><td>Unconstrained NLP</td><td></td></tr><tr><td>Linear equalities</td><td>LE/SLE</td><td>LP</td><td>QP</td><td>Constrained NLP</td></tr><tr><td>Linear inequalities</td><td>-</td><td>LP</td><td>QP</td><td>Constrained NLP</td></tr><tr><td>Nonlinear equalities</td><td>NLE/SNLE</td><td>Constrained NLP</td><td></td><td></td></tr><tr><td>Nonlinear inequalities</td><td>-</td><td>Constrained NLP</td><td></td><td></td></tr></table>

$^{a}$ LP: linear programming; QP: quadratic programming; NLP: nonlinear programming; LE: linear equations; SLE: simultaneous linear equations; NLE: nonlinear equations; SNLE: simultaneous nonlinear equations.

Step 1. A user gives an objective function, that is, a polynomial on reals with finitely many variables and a decision principle whether the objective function is to be maximized or minimized. Then he/she gives constraints that are inequalities or equalities of polynomials on reals with finitely many variables.

At this stage, the system knows an abstract optimization model

$$
\left(o, r, \left\{\left(p _ {1}, o p _ {1}, q _ {1}\right), \dots , \left(p _ {m}, o p _ {m}, q _ {m}\right) \right\}\right) \in O M (V),
$$

where V is the set of variables which occurs in the abstract objective function and the abstract constraints.

Step 2. Then he/she user chooses decision variables in V. Let $D \subset V$ be the set of decision variables.

Step 3. Assign data: $(V) \to R$ for the objective function r and transfer it to a polynomial on reals over $D = V - dom(data)$ . At this stage, we have a specific objective function $assign(data)(r)$ .

Step 4. Assign data: $(V) \to R$ for constraints and transfer it to constraints on reals over $D = V - dom(data)$ . At this stage, we have specific constraints,

$$
\begin{array}{c} \bigl \{\bigl (a s s i g n (d a t a) (p _ {1}), o p _ {1}, a s s i g n (d a t a) (q _ {1}) \bigr), \ldots , \\ \bigl (a s s i g n (d a t a) (p _ {m}), o p _ {m}, a s s i g n (d a t a) (q _ {m}) \bigr) \bigr \}. \end{array}
$$

And then we have a specific optimization problem over D.

Step 5. Normalize a specific optimization problem $(o,r,\{(p1,op_1,q_1),\ldots,(p_m,op_m,q)\})$ to its normal form $\{o,r,\{(p_1',op_1',s_1),\ldots,(p_m',op_m,s_m)\}$ .

Step 6. Categorize the specific optimization model in normal form into a corresponding problem.

Step 7. According to the categorization of the specific optimization model in normal form, the system calls an appropriate solver after preprocessing the specific model in normal form to an appropriate form for the solver.

Step 8. After getting a solution by the corresponding solver, the system shows the solution to the user after post-processing it in normal form (Fig. 1).

![](/api/attachments/MCW3JR76/fulltext/images/0d3f26c5d798875f34c5c9e79e97942b39052def12ef547d662f0529a82c20d6.jpg)  
Fig. 1. Flow of automatic modelling and solving.

Let us next show how the above design is implemented. According to the formulation discussed in the previous section, we implemented a prototype system in which we can treat problems in Problem = {LP,NLP,SLE,SNLE}. The followings are critical points in implementation,

1. how to assign data for a given polynomial, that is, to implement $assign(data)$ ,

2. how to assign data for given constraints and get constraints in normal form, that is, to implement normalize,

3. how to categorize specific models into problems, that is, to implement categorizeProblem.

Since our system is implemented in Prolog, let us explain how the above points are implemented by showing predicates in Prolog.

In order to implement assign(data), we have the following predicate,

```prolog
getNewPolynomial(Polynomial, NewPolynomial) := getData(Data),
assign(Polynomial, Data, NewPolynomial).
```

The predicate assign(Polynomial, Data, NewPolynomial) signifies that Polynomial is of the form NewPolynomial if we assign Data that is defined as a list of equations. Then the implementation of it is straightforward.

Since a constraint is of the form $(p(x_1, \ldots, x_m)$ ,

```javascript
[NewLHS=<NewRHS|NewConstraints]]:=
```

getNewConstraints([LHS=<RHS|Constraints], $op,q(x_{1},\ldots,x_{m}))$ , we can implement normalize by moving $q(x_{1},\ldots,x_{n})$ to the left hand side, assigning Data and then moving constant terms to the right hand side.

An example of the predicate is as follows,

In order to categorize specific models in normal form into problems, we have to determine polynomials as linear or nonlinear. We use the following predicate to determine a polynomial as linear.

```prolog
linear(Polynomial, X) := polynomial_normal_form(Polynomial, X, PolyNormalForm), for_all(member((C, N), PolyNormalForm), linear1(C, N)). linear1(C, 1) := number(C). linear1(_, 0).
```

The predicate polynomial\_form(Polynomial, X, PolyNormalForm) is originally used in PRESS system [9] and it is to transform a given Polynomial to a polynomial normal form PolyNormalForm of the variable X.

If a polynomial is of the form $a_{n}x^{n}+\ldots+a_{1}x+a_{0}$ , then its polynomial normal form for x is given by $[(a_{n},n),\ldots,(a_{1},1),(a_{0},0)]$ . Therefore, if all of the terms $(C,N)$ in its polynomial normal form are of order $0(N=0)$ or of order $1(N=1)$ with a numeric coefficient for any variables in the polynomial, then it is categorized as linear. Other categorization is similarly implemented.

The system is implemented in the SB-Prolog System on SUN workstation. We call solvers such as $LINDO^{TM}$ and others via system call from Prolog program. And the communication between SB-Prolog and solvers is implemented through text files.

## 4. Illustration

In order to illustrate the behaviour of the prototype system, let us take the example stated in Section 1.

Example 1. Let us consider the following optimization problem.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
minimize $a*x * x + b*x + c*y$ subject to $d*x + e*y - r = f$ . $g*x + h*y - s = i$
</div>

The above problem is represented as the following abstract optimization model in this system.

```prolog
objective(min, a*x*x+b*x+c*y).
constraint(d*x+e*y-r, =, f).
constraint(g*x+h*y-s, =, i).
```

Suppose that we know the following data,

$h = 2, i = 120.$

In this case, decision variables are x and y, then we have the following specific model in normal form after assigning data in $V - \{x, y, r, s\}$ and normalization.

```prolog
objective(min,1.5*x+y).
constraint(2.5*x+5*y-r,=,150).
constraint(5*x+2*y-s,=,120).
```

Since the objective function and constraints in the above specific model in normal form are linear, it is categorized as LP. Then the system assigns LINDO $^{TM}$ as its corresponding solver. Since LINDO $^{TM}$ needs a specific form of input files, we need pre-processing of the specific model in normal form. By preprocessing, we have the following input file for LINDO $^{TM}$ .

```txt
1.5x+y
st
2.5a+5y-r=150
5x+2y-s=120
end
```

After solving the problem, LINDO $^{TM}$ returns solution as follows.

<table><tr><td colspan="3">OBJECTIVE FUNCTION VALUE</td></tr><tr><td colspan="3">1) 45.0000000</td></tr><tr><td>VARIABLE</td><td>VALUE</td><td>REDUCED COST</td></tr><tr><td>X</td><td>15.000000</td><td>0.000000</td></tr><tr><td>Y</td><td>22.500000</td><td>0.000000</td></tr><tr><td>R</td><td>0.000000</td><td>-0.100000</td></tr><tr><td>S</td><td>0.000000</td><td>-0.250000</td></tr></table>

After post-processing, we get solution in normal form as follows.

```prolog
data(1.5*x+y,45.0).
data(x,15.0).
data(y,22.5).
```

## 5. Conclusion

In this paper, we proposed automatic model building and solving for general optimization problems. The range of optimization problems in this paper covers LP, QP, NLP and simultaneous linear/non-linear equations as well. We formulated our idea using set-theoretical notions and designed it as a procedure in which a user can construct a model in an automatic way. We also discussed the implementation of our idea. Since our system is written in Prolog, we explained how to realize functions formulated as predicates in Prolog. Finally, we illustrated its behaviour by simple examples including linear programming and simultaneous linear equations.

As shown in the illustration, our prototype system is restricted handling of the problems in LP, SLE, NLP and SNLE. It is necessary to extend our framework to include IP, QP and multi-objectives.

Since the paper is rather theoretical, it is necessary to show the effectiveness of our approach by solving a practical problem. Therefore it is future work to extend the idea to identify rather practical problem types, for example, job shop scheduling problems. And it is also necessary to have an experiment to show the functionality provided in this approach.

## Acknowledgements

The author would like to thank anonymous referees for helpful comments and suggestions for improving the paper.

## References

[1] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37, No. 1 (1989).

[2] F.H. Murphy and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2 (1986).

[3] Ting-Peng Liang, Analogical Reasoning and Case-Based Learning in Model Management Systems, Decision Support Systems 10 (1993).

[4] M. Binbasioglu, Process-Based Reconstructive Approach to Model Building, Decision Support Systems 12 (1994).

[5] J.K. Lee and Y.U. Song, UNIK-PMA: A Unifier of Optimization Model with Rule-Based Systems by the Post-Model Analysis, forthcoming in Annals of Operations Research.

[6] R. Krishnan, A Logic Modeling Language for Automated Model Construction, Decision Support Systems 6 (1990).

[7] R. Krishnan, PDM: A Knowledge-Based Tool for Model Construction, Decision Support Systems 7 (1991).

[8] C.C. Chang and H.J. Keisler, Model Theory (North-Holland, 1973).

[9] Sterling and E. Shapiro, The Art of Prolog (The MIT Press, 1986).

![](/api/attachments/MCW3JR76/fulltext/images/1d0065d1bc27810b353e513f3b8bdee43bbbd1517b82c58f096cf88ebd008126.jpg)

Junichi Iijima is an associate professor of the Department of Industrial Management and Systems Engineering, Faculty of Engineering, Tokyo Institute of Technology. He graduated in control engineering at Tokyo Institute of Technology. He holds a Doctor of Engineering in Systems Science from Tokyo Institute of Technology, Japan. His recent interests include systems theory and information systems. He published in several professional journals on systems theory

as International Journal of General Systems and on information systems as Journal of JASMIN (in Japanese). He is an author of several books on systems theory and information systems.
