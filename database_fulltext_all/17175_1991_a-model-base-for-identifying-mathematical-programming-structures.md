---
otero_id: 17175
otero_key: "7RUZ7DZU"
title: "A model base for identifying mathematical programming structures"
authors: "Jae Sik Lee"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90049-h"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A model base for identifying mathematical programming structures

Jae Sik Lee

College of Business Administration, The Ajou University, Suwon, Kyung-Gi-Do, Korea

In order to facilitate the functions of Model Management Systems more efficiently, structural information on the models should be stored together with their individual formulations. A language developed for storing model structures is presented and an efficient way to store mathematical programming models is proposed.

Keywords: Model management systems, Knowledge representation, Mathematical programming, AI/OR interface.

## 1. Introduction

![](/api/attachments/7RUZ7DZU/fulltext/images/382e4c3890c8c71c1bb3cef472828f9e1e29d0c7b2df1faf37799d0fd713d54b.jpg)

Jae Sik Lee has completed his dissertation in the Department of Decision Sciences at the Wharton School of the University of Pennsylvania. He holds an M.S. degree in Industrial Sciences and a B.B.A degree. He has published papers on heuristic algorithm and model management and presented talks on model management systems at national conferences. He is now an assistant professor in the Ajou University in Korea.

Mathematical programming models have been playing important roles in complex decision making situations for many years. While management scientists and operations researchers have built mathematical programming models, for a little more than a decade researchers in the information systems field have studied the way to manage those models efficiently: the Model Management Systems (MMS). Generally, the functions of MMS include Model Building, Model Representation, Interface with Database, Model Storage, Model Retrieval, Model Maintenance, Link between Models and Algorithms, and Model Solving. While practitioners have developed and used their matrix generators, e.g., GAMMA (developed by Bonner and Moore), MAGEN, PDS, OMNI (developed by Haverly Systems), to solve mathematical programming models for real world problems, theoreticians have tried to develop a conceptual framework of MMS applying characteristics similar to those of database management systems. For example, Elam et al. [5,6,7,8] employed the entity-relationship approach utilizing knowledge engineering concepts, Blanning [2,3,4] used the relational approach, and Konsynski and Dolk [11,12,13] adopted CODASYL's network approach. Geoffrion [9] suggested a unified framework for systematizing the model formulation process.

In this note, we will focus on how models should be stored to fully utilize the functions of MMS. In section 2, the important role of Model Storage, especially when mathematical programming models are involved, will be discussed. A language we developed for storing mathematical programming models will be introduced in section 3. In sections 4, 5 and 6, we will propose an efficient way to store mathematical programming models utilizing a data base and a knowledge base.

## 2. Model Storage

Since the way models are stored has a crucial effect on the performance of MMS, it cannot be taken for granted that a model is stored as its individual formulation when it is created for a particular problem, as in all systems mentioned in section 1. Disadvantages of this individual storage of models are as follows:

1. Since the number of models that can be created is almost infinite, storage and maintenance of all those models created as their individual formulations are inefficient.

2. It is hard to identify the special structure of a model for employing an efficient special algorithm because one needs expertise to extract the special structure from the given problem.

3. Even if one has analyzed a certain problem and applied an efficient special algorithm to that problem, this experience cannot be utilized automatically thereafter when facing another problem with the same structure.

4. In building a model, if models are stored not as their structural representation, but as their individual formulations, one must search all stored models without any guidance on structural relationships among them for the prototype which is appropriate for a particular problem.

To overcome these inefficiencies, one needs to store models as more abstract structures, not as their individual formulations, so that one can provide a common ground for all models in which the structure inside the formulation gets some meaning. In our proposed Model Storage, equations are stored as their structural representations separately from formulations. A formulation is then stored as a combination of those equation structures so that it can represent not only its own structure but also its structural relationship with other formulations.

## 2.1. Storing equations

In order to be able to identify identical (or similar) structures (or substructures) and establish structural relationships among models, one needs to separate the equation description from the model itself. The following examples illustrate this point. First, let us consider the following formulation of a 0-1 knapsack problem (0-1KP):

Formulation 1. 0-1KP Formulation

$$
\begin{array}{l} \text {Max} Z = \sum_ {j = 1} ^ {n} C _ {j} X _ {j} \\ \text {st} \quad \sum_ {j = 1} ^ {n} a _ {j} X _ {j} \leq b, \\ X _ {j} \in \{0, 1 \}, \forall j. \end{array}
$$

and a formulation having the same structure as Formulation 1 but different names for index sets, parameters and variables as follows:

$$
\begin{array}{l} \text {Max} X = \sum_ {p = 1} ^ {k} D _ {p} Y _ {p} \\ \text {st} \quad \sum_ {p = 1} ^ {k} b _ {p} Y _ {p} \leq c, \\ Y _ {p} \in \{0, 1 \}, \forall p. \end{array}
$$

Obviously, the second formulation is also a formulation for 0-1KP even though it uses different names for index sets, parameters and variables. This simple analogy among formulations might go undetected if those two formulations are stored as their individual formulations. Let us now consider a generalized assignment problem (GAP):

## Formulation 2. GAP Formulation

$$
\begin{array}{l} \text {Max} Z = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} C _ {i j} X _ {i j} \\ \text {st} \quad \sum_ {j = 1} ^ {n} a _ {i j} X _ {i j} \leq b _ {i}, \forall i \\ \sum_ {i = 1} ^ {m} X _ {i j} = 1, \forall j \\ X _ {i j} \in \{0, 1 \}, \forall i, \forall j. \end{array}
$$

The objective functions, the first constraints and the binary variable constraints of 0-1KP and GAP, respectively, have a similar structure. This kind of information is very important because we can use an algorithm for 0-1KP to solve GAP after relaxing the second constraint of GAP. However, if we store those formulations individually, it will be hard to find any relationship between them. If we assign unique numbers to equations (note that an equation of a formulation in this research is actually a set of equations (equality or inequality) which have the same structure, i.e., an objective function or a part of constraint set which is divided by equation groups) in 0-1KP and GAP as in table 1 and store those equations and their numbers in a database, which we shall call the Equation Structure Base (ESB), then we can simply represent those formulations as follows:

Equation Numbers and Equations.

<table><tr><td>Number</td><td>Equation</td></tr><tr><td> $\langle 1 \rangle$ </td><td> $Z = \sum_{j=1}^{n} C_j X_j$ </td></tr><tr><td> $\langle 2 \rangle$ </td><td> $\sum_{j=1}^{n} a_j X_j < b$ </td></tr><tr><td> $\langle 3 \rangle$ </td><td> $X_j \in \{0, 1\}, \forall j$ </td></tr><tr><td> $\langle 4 \rangle$ </td><td> $Z = \sum_{i=1}^{m} \sum_{j=1}^{n} C_{ij} X_{ij}$ </td></tr><tr><td> $\langle 5 \rangle$ </td><td> $\sum_{j=1}^{n} a_{ij} X_{ij} < b_i, \forall i$ </td></tr><tr><td> $\langle 6 \rangle$ </td><td> $\sum_{i=1}^{m} X_{ij} = 1, \forall j$ </td></tr><tr><td> $\langle 7 \rangle$ </td><td> $X_{ij} \in \{0, 1\}, \forall i, \forall j$ </td></tr></table>

0-1KP: Maximize $\langle1\rangle$ subject to $\langle2\rangle$ and $\langle3\rangle$ ,
GAP: Maximize $\langle4\rangle$ subject to $\langle5\rangle$ , $\langle6\rangle$ and $\langle7\rangle$ .

In fact, however, $\langle2\rangle$ and $\langle5\rangle$ , $\langle3\rangle$ and $\langle7\rangle$ , respectively, are identical structures. It is therefore extremely important to be able to represent identical structures identically, i.e., to extract and store information about equations in such a way that structure recognition will be automatic. This led us to realize that one should separate equation storage from formulation storage.

## 2.2. Storing Formulations

In addition to the ESB, we need a knowledge base to store knowledge about formulations. We shall call it the Formulation Knowledge Base (FKB).

Formulations are represented in relation to the equation structures stored in the ESB using IF-THEN rules. For instance, knowledge about the formulation of GAP would be represented as follows:

IF the objective function is to be maximized, the objective function is $\langle 4\rangle$ , there are three constraints, one of the constraints is $\langle 5\rangle$ , one of the constraints is $\langle 6\rangle$ , one of the constraints is $\langle 7\rangle$ ,

THEN the formulation is a generalized assignment problem.

To summarize, we will store models in a unified way as the model base by integrating the Equation Structure Base and the Formulation Knowledge Base. In fact, since one could use different names for indices, parameters or variables and since the relationships between the objective function and the constraints or among the constraints are not explicitly expressed, the IF-THEN rules described above are not sufficient to represent the corresponding formulation completely. These issues will be discussed in sections 5 and 6.

## 3. A Language for Equation Syntax Abstraction

In this section, we shall demonstrate on an example the abstraction process that allows one to extract the structure of a model, i.e., transform a mathematical programming formulation represented in a model description language into a formulation represented in a structure description language. For a model description language, we chose GAMS $[1,10,17]$ for its representation ability and its independence of algorithms, even though there are some difficulties in representing certain kinds of combinatorial problems such as the traveling salesman problem or the vehicle routing problem. For a structure description language, we designed a high level language based on GAMS syntax, which we shall call ALESA, A Language for Equation Syntax Abstraction $[15]$ .

Consider the formulation of GAP given in Formulation 2. The same optimization problem can be formulated in various ways, such as using different naming conventions, switching the positions of terms in an equation, or representing an equation in a different way. Formulation 2 is selected merely to describe our principle of Model Storage. The formulation of GAP expressed in our GAMS-like language (note that GAMS modeling language is adopted and slightly modified to suit our research) is given in fig. 1.

```matlab
INDEX SET I:1:M;
J:1:N;
POSITIVE PARAMETER C(I,J);
POSITIVE PARAMETER A(I,J);
POSITIVE PARAMETER B(I);
FREE VARIABLE Z;
BINARY VARIABLE X(I,J);
MAXIMIZE
SUM((I,J),C(I,J)*X(I,J))=E=Z;
SUBJECT TO
SUM(J,A(I,J)*X(I,J))=L=B(I);
SUM(I,X(I,J))=E=1;
Fig. 1. GAMS-like Formulation of GAP.
```

Since specific names for index sets, parameters or variables are not important from the viewpoint of equation structure, only their relative positions in the equations are specified in ALESA. Depending on the use of an index in an equation, the index is expressed differently. An index can be used for summation, for equation grouping, for indexing a literal (parameter or variable) or just as a literal. Indices used for indexing a literal are assimilated and treated as a part of the literal. Indices used for equation grouping are expressed as G. Indices used for summation or as literals are expressed as In (I1, I2, ... : I stands for Index). Literals are expressed as Ln (L1, L2, ... : L stands for Literal). n in In or Ln starts from 1 and is increased by 1 every time one encounters a different index (for In) or literal (for Ln) during the scanning of the equation from left to right. This numbering of indices or literals is in effect within a single individual equation. For example, the structure of the first constraint in fig. 1 is represented in ALESA as follows:

$$
\operatorname{SUM} (\mathrm{I1}, \mathrm{L1} * \mathrm{L2}) = \mathrm{L} = \mathrm{L3};\tag{ES(3.1}
$$

In the same manner, we can represent the structure of the second constraint in fig. 1 as follows without causing any conflict with the numbering in ES(3.1):

$$
\operatorname{SUM} (\mathrm{I1}, \mathrm{L1}) = \mathrm{E} = 1;\tag{ES(3.2}
$$

More about the ALESA language will be introduced in the next section as we discuss the Equation Structure Base. Readers are referred to Lee [15] for the ALESA language in detail.

## 4. Equation Structure Base

This database should consist of all possible structures of equations (equality or inequality) which can appear in a formulation. An equation structure in the ESB is represented using ALESA, i.e., not using any specific names for indices or literals. Moreover, equations with the same structure ought to be stored as the same equation.

For example, consider the following equations EQ(4.1) and EQ(4.2):

$$
\sum_ {i} a _ {i} X _ {i} \leq b,\tag{EQ(4.1}
$$

$$
\sum_ {j} a _ {i j} X _ {i j} \leq b _ {i}, \forall i.\tag{EQ(4.2}
$$

In GAMS-like language, these equations are represented as follows:

$$
\operatorname{EQ} (4. 1) \Rightarrow \operatorname{SUM} (\mathrm{I}, \mathrm{A(I)} * \mathrm{X(I)}) = \mathrm{L} = \mathrm{B};
$$

$$
\operatorname{EQ} (4. 2) \Rightarrow \operatorname{SUM} (\mathrm{J}, \mathrm{A} (\mathrm{I}, \mathrm{J}) * \mathrm{X} (\mathrm{I}, \mathrm{J})) = \mathrm{L} = \mathrm{B} (\mathrm{I});
$$

Yet, the equation structure ES(3.1) is sufficient to represent the structure of both equations. The only difference is that the group index for EQ(4.1) and EQ(4.2) is none and I, respectively.

As seen in ES(3.1), indices which are part of literals have disappeared during the abstraction process and group indices are not visible. However, since an index used in ES(3.1) must be either for summation or for equation group, indices other than I1 are captured as for equation group. This information is preserved in the instantiation process which will be discussed in the next section.

By the same manner, equation structure ES(4.1) is sufficient to represent any nonnegativity constraint on variable such as equations EQ(4.3) and EQ(4.4):

$$
\text { POSITIVE   VARIABLE   L1 };\tag{ES(4.1}
$$

$$
X _ {j} \geq 0, \forall j,\tag{EQ(4.3}
$$

$$
Y _ {i j} \geq 0, \forall i, j.\tag{EQ(4.4}
$$

By using ALESA, we store only a small number of possible structures in the ESB and the actual equation is instantiated when we process the actual formulation. A sample ESB is presented in table 2 (the number in the first column is the unique number assigned to each equation structure).

```matlab
For SUM(J, A(I, J) * X(I, J)) = L = B(I);
Matched with ES(3.1), i.e.,
SUM(I1, L1 * L2) = L = L3;
I1 is instantiated to J,
L1 is instantiated to A(I, J),
L2 is instantiated to X(I, J),
L3 is instantiated to B(I),
G is instantiated to I.
For SUM(I, X(I, J)) = E = 1;
Matched with ES(3.2), i.e.,
SUM(I1, L1) = E = 1;
I1 is instantiated to I,
L1 is instantiated to X(I, J),
G is instantiated to J.
Since these two equations are constraints within the same formulation, a cross checking of the
```

```txt
- category name of model,
- individual name of model.
```

Table 2  
A Sample Equation Structure Base.

<table><tr><td>Number</td><td>Equation Structure</td></tr><tr><td>1</td><td>FREE VARIABLE L1;</td></tr><tr><td>2</td><td>POSITIVE VARIABLE L1;</td></tr><tr><td>3</td><td>BINARY VARIABLE L1;</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td>6</td><td>POSITIVE PARAMETER L1;</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td>10</td><td>SUM((I1, I2), L1 * L2) = E = L3;</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td>15</td><td>SUM(I1, L1 * L2) = L = L3;</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td>20</td><td>SUM(I1, L1) = E = 1;</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td></tr></table>

## 5. Instantiation of Equation

When an actual formulation is input by the user, each equation of the formulation is checked with the ESB to see if there is an equation structure in the ESB that matches the actual equation. The matching equation structure is selected from the ESB and all index names and literal names in the selected equation structure, e.g., I1, I2 and L1, L2, etc., become instantiated to the corresponding actual index names and literal names [14]. The result of matching two equations in the constraints of GAP in fig. 1 with the ESB is as follows:

matchings should be done to make sure that they are part of the same model. For instance, I1 in ES(3.1) and G in ES(3.2) must be instantiated to the same index J, and L2 in ES(3.1) and L1 in ES(3.2) must be instantiated to the same variable X(I, J). This integrity maintenance should be considered in designing the FKB and this will be discussed in the next section.

## 6. Formulation Knowledge Base

The FKB is the collection of knowledge about model formulations using a rule-based method which centers on the use of IF-THEN statements. However, unlike conventional knowledge bases, in the FKB, a single chunk of knowledge is implicitly divided into an IF part and a THEN part, and the knowledge is expressed by information from the ESB and the instantiation process described in section 5. A formulation is not stored as a whole formulation with specific names for indices and literals, but stored as a collection of relevant equation structure numbers of the ESB and a matching list of indices and literals obtained through instantiation.

In the implicit IF part, the following information is stored:

\- optimizing direction of objective function, i.e., minimize or maximize,

\- equation structure number of the objective function,

\- list of equation structure numbers of the constraints,

\- list of indices and literals matching.

In the implicit THEN part, the following information is stored:

For example, formulation knowledge of GAP in fig. 1 is represented as in table 3. Note that only the second column of this table, i.e., Stored Knowledge, is stored in the FKB.

Recall the sample ESB given in table 2. Constraint number list [6,6,6,1,3,15,20] represents that the formulation contains three positive parameters, one free variable, one binary variable and two constraints whose equation structures are 15 and 20. In the matching list, each element is composed of an equation structure number and a position in the equation structure. For example, the matching list [6L1,10L1] for C(I, J) represents that the parameter C(I, J) appears in the position L1 in equation structure 6, i.e., positive parameter, and in the position L1 in equation structure 10. # is the exclusive OR operator, therefore, 10I1#I2 in the matching list for I means that index I appears either in I1 or in I2 in equation 10, but not in both. This matching list is a modal net which is cast over the formulation to make sure that a certain index or literal in a certain position cannot be anything else.

Table 3  
Formulation Knowledge of GAP.

<table><tr><td>Part</td><td>Stored Knowledge</td><td>Description</td></tr><tr><td>IF</td><td>maximize,</td><td>optimizing direction</td></tr><tr><td>part</td><td>10,[6, 6, 6, 1, 3, 15, 20],[[6G, 6G, 6G, 3G, 10I1 #I2, 15G, 20I1],[6G, 6G, 3G, 10I1 #I2, 15I1, 20G],[6L1, 10L1],[3L1, 10L2, 15L2, 20L1],[1L1, 10L3],[6L1, 15L1],[6L1, 15L3] ],</td><td>objective function number constraint number list matching list for I for J for C(I, J) for X(I, J) for Z for A(I, J) for B(I)</td></tr><tr><td>THEN</td><td>assignment,</td><td>category name</td></tr><tr><td>part</td><td>generalized-assignment</td><td>individual name</td></tr></table>

The elements in the constraint number list or in the matching list that we obtain from an actual formulation does not have to be in the same order as the elements stored in the FKB. What matters is the elements of the list, not their order. If the constraint number list and matching lists of an actual formulation contain one or more lists stored in the FKB, then we can conclude that the actual formulation has special (sub)structure(s) that is already stored in the FKB and for which we may have customized efficient algorithms.

A model in its original form can be reconstructed, i.e., retrieved, utilizing the knowledge stored in the FKB. Given the individual name of the model, the corresponding equation structures, i.e., ALESA representations, of its objective function and constraints are selected from the ESB. Then, with the information in the matching lists, the ALESA representations are transformed into the actual equations, e.g., the equations as in fig. 1, by plugging specific names for indices and literals in the positions specified in the equation structures. The specific names can be provided by the user or default names can be stored in the FKB alongside each matching list.

## 7. Conclusion

We have devised an efficient framework for storing and maintaining mathematical programming models by integrating two kinds of data bases: the ESB and the FKB. Some advantages of this framework are as follows:

1. Economical Storage: Since structures of equations, not individual equations, are stored in the ESB and the knowledge of formulation structures using the ESB is stored in the FKB, we can store models using a minimum of storage space.

2. Ease of Update: When one stores a new formulation, all one has to do is to add the structures of the newly encountered equations, if any, of this new formulation to the ESB, and add one line of knowledge to the FKB.

3. Building Structural Families of Models: By representing models in their structural formulations, models are grouped according to their structural analogies, not their application similarities.

4. Intelligent Link between Models and Algorithms: By capturing formulation structures, we can employ an algorithm designed for a certain formulation for problems with analogous structures after relaxing or decomposing those problems' formulations.

Some of limitations of this framework should also be noted:

1. We only considered mathematical programming models that can be expressed in a model description language, e.g., GAMS. Optimization models such as network flow problems or the traveling salesman problem can be expressed and stored more efficiently than our proposed method.

2. As stated in section 3, unlimited variations involved in mathematical programming formulations [16] are not addressed in the proposed method. A procedure for standardizing the equation forms needs to be incorporated in the proposed method in order to maintain the ESB more efficiently.

## References

[1] Bisschop, J. and A. Meeraus, On the Development of a General Algebraic Modeling System in a Strategic Planning Environment, Math. Prog. Study 20 (1982), 1–29.

[2] Blanning, R.W., Data Management and Model Management: A Relational System, Proc. ACM 12th SE Regional Conference (1982), 139–149.

[3] Blanning, R.W., Issues in the Design of Relational Model Management Systems, IFIPS Conference Proc. (1983), 395–401.

[4] Blanning, R.W., Language Design for Relational Model Management, in: Management and Office Information Systems, S.K. Chang (ed.), Plenum, New York (1984).

[5] Elam, J.J., Model Management Systems: A Framework for Development, Working Paper 79-02-04, Dept. of Decision Sciences, The Wharton School, Univ. of PA, PA 19104 (1979).

[6] Elam, J.J., Model Management Systems: An Overview, Working Paper 79-12-04, Dept. of Decision Sciences, The Wharton School, Univ. of PA, PA 19104 (1979).

[7] Elam, J.J. and J.C. Henderson, Knowledge Engineering Concepts for Decision Support System Design and Implementation, Proc. 14 $^{th}$ Hawaii Int. Conf. on System Sciences, (1981), 639–643.

[8] Elam, J.J., J.C. Henderson and L. W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proc. First Int. Conf. on Information Systems (1980), 98–110.

[9] Geoffrion, A.M., An Introduction to Structured Modeling, Management Science 33, 5 (1987), 547–588.

[10] Kendrick, D. and A. Meeraus, GAMS: An Introduction, Development Research Dept., The World Bank, Washington D.C. 20433 (1985).

[11] Konsynski, B., On the Structure of a Generalized Model Management System, Proc. 14 $^{th}$ Hawaii Int. Conf. on System Sciences (1981), 630–638.

[12] Konsynski, B., Model Management in Decision Support Systems, in: Data Base Management: Theory and Applications, C.W. Holsapple and A.B. Whinston (eds.), Reidel, Dordrecht (1983), 131–154.

[13] Konsynski, B. and D. Dolk, Knowledge Abstractions in Model Management, DSS-82 Transactions (1982), 187–202.

[14] Lee, J.S., A Model Base for Identifying Mathematical Programming Structures, Working Paper 86-06-05, Dept. of Decision Sciences, The Wharton School, Univ. of PA, PA 19104 (1986).

[15] Lee, J.S., ALESA: A Language for Equation Syntax Abstraction. Working Paper 86-06-09, Dept. of Decision Sciences, The Wharton School, Univ. of PA, PA 19104 (1986).

[16] Lee, J.S., C.V. Jones and M. Guignard, MAPNOS: Mathematical Programming Formulation Normalization System, Expert Systems with Applications 1, 4 (1990).

[17] Meeraus, A., An Algebraic Approach to Modeling, Journal of Economic Dynamics and Control 5 (1983), 81–108
