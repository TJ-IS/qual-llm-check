---
otero_id: 10814
otero_key: "WMYH9Y2S"
title: "MOPEN: A computational package for Linear Multiobjective and Goal Programming problems"
authors: "R. Caballero; M. Luque; J. Molina; F. Ruiz"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.06.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# MOPEN: A computational package for Linear Multiobjective and Goal Programming problems

R. Caballero<sup>\*</sup>, M. Luque, J. Molina, F. Ruiz

Department of Applied Economics (Mathematics), Faculty of Economics, University of Ma´laga, Campus El Ejido s/n. Ma´laga, 29071, Spain

Received 30 November 2002; accepted 1 June 2004 Available online 14 August 2004

## Abstract

MOPEN is a computational package designed as a global tool for Linear Multiobjective and Goal Programming problems with continuous and/or integer variables. The main existing techniques for these problems have been included in this package. That is, it is possible to generate or approximate the efficient set using Generating Methods, to obtain Compromise solutions or to use Goal Programming or reference Point approaches. As will be described, many advanced options have been implemented with every method. MOPEN has been implemented under a Windows environment; thus, it is easy to build and handle the data entry files and the result layout files. The behavior of MOPEN—in terms of CPU time used to solve large problems—can be considered as good; therefore, this package is a powerful tool to handle the previously mentioned problems. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Multiobjective Programming; Computational package; Goal Programming; Integer programming

## 1. Introduction

## 1.1. Basic Definitions

In this paper, the general Linear Multiobjective problem

$$
\begin{array}{c} \operatorname{Min} (f _ {1} (\mathbf {x}), f _ {2} (\mathbf {x}), \dots , f _ {p} (\mathbf {x})) = \left(\mathbf {c} _ {1} ^ {t} \mathbf {x}, \mathbf {c} _ {2} ^ {t} \mathbf {x}, \dots , \mathbf {c} _ {p} ^ {t} \mathbf {x}\right) \\ (L M O P) \qquad \text {s.t.:} \mathbf {x} \in X = \{\mathbf {x} \in R ^ {n}: A \mathbf {x} \leq \mathbf {b} \} \\ A \in M _ {s \times n} (R), \mathbf {b} \in R ^ {s} \end{array}
$$

will be considered. The following classical concepts will be used throughout the paper:

<sup>!</sup> Let $\mathbf { X } _ { i } ^ { * }$ be the optimum value of $f _ { i } \colon f _ { i } ( \mathbf { x } _ { i } ^ { * } )$ =min $\{ f _ { i } ( { \bf x } ) / { \bf x } { \in } R ^ { \mathrm { n } }$ , A<sup>d</sup> xVb}. $\mathbf { X } _ { i } ^ { * }$ is called the Ideal Solution of $f _ { i } ,$ and $f _ { i } { } ^ { * } { = } f ( \mathbf { x } _ { i } { } ^ { * } )$ is its Ideal Value.

<sup>!</sup> The pay-off matrix is formed by the values of all the functions $f _ { i }$ in all the ideal solutions:

$$
\left( \begin{array}{c c c c} f _ {1} (\mathbf {x} _ {1} ^ {*}) & f _ {1} (\mathbf {x} _ {2} ^ {*}) & \dots & f _ {1} (\mathbf {x} _ {n} ^ {*}) \\ f _ {2} (\mathbf {x} _ {1} ^ {*}) & f _ {2} (\mathbf {x} _ {2} ^ {*}) & \dots & f _ {2} (\mathbf {x} _ {n} ^ {*}) \\ \vdots & \vdots & & \vdots \\ f _ {n} (\mathbf {x} _ {1} ^ {*}) & f _ {n} (\mathbf {x} _ {2} ^ {*}) & \dots & f _ {n} (\mathbf {x} _ {n} ^ {*}) \end{array} \right)
$$

The elements of the main diagonal of the pay-off matrix are the ideal values of each function. The maximum value per column, ma $\mathrm { x } _ { j = 1 ; \cdot \cdot , p } \left\{ f _ { i } \left( \mathbf { x } _ { j } * \mathbf { \right) } \right\}$ , is called the Anti-ideal Value of $\dot { \boldsymbol { f } } _ { i }$ and is denoted by $\mathbf { \widetilde { f } } ^ { ( i ) }$ The corresponding solution is called the Anti-ideal Solution of ${ \bf \dot { \boldsymbol { f } } } _ { i }$ and is denoted by $\mathbf { x } ^ { ( i ) }$

<sup>!</sup> A feasible solution $\mathbf { x } ^ { * } { \in } X$ is said to be efficient for (LMOP) (or Pareto optimal) if there does not exist any other solution $\mathbf { x } { \in } X ,$ such that:

$$
f _ {i} (\mathbf {x}) \leq f _ {i} (\mathbf {x} ^ {*}) \quad \forall i = 1, \dots , p
$$

with at least one $j { \in } \{ 1 , . . . , p \}$ such that $f _ { j } ( \mathbf { x } ) { < } f _ { j } ( \mathbf { x } ^ { * } )$ <sup>!</sup> A feasible solution ${ \mathbf { x } } ^ { * } \in \mathrm { X }$ is said to be weakly efficient for (LMOP) (or weakly Pareto optimal ) if there does not exist any other solution $\mathbf { x } { \in } X ,$ such that:

$$
f _ {i} (\mathbf {x}) <   f _ {i} \left(\mathbf {x} ^ {*}\right) \quad \forall i = 1, \dots , p.
$$

The most widely accepted classification of the existing techniques to solve these problems depends on the information flow between the decision maker and the analyst. The first possibility is that the decision maker provides his/her preferences only by stating which objectives have to be minimized and which ones have to be maximized. In this case, the aim of the methods is to show the Pareto efficient set (or an approximation of it). The techniques corresponding to this scheme are called Generating Techniques (see, for example, Ref. [16]). Second, the decision maker may want to overcome the conflict among the objectives, without having to state a clear preference towards a specific one. In this case, an efficient solution has to be found, characterized by creating a compromise or equilibrium among the objectives. This is the basic idea of Compromise Programming [23,24,15]. On the other hand, ${ \mathrm { i f } } ,$ prior to the resolution process, the decision maker provides information in the form of target values, $\mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega }$ for each objective, and possibly preference levels among them, then this constitutes the Goal Programming scheme (see Refs. [5,6,8]). Similarly, the Reference Point method [22] lets the decision maker establish aspiration levels for the objectives, without having to renounce the efficiency of the solutions. Finally, in the Interactive Techniques (see, for example, [9]), there exists a continuous flow of information between the analyst and the decision maker, throughout the whole resolution process).

In this paper, the software MOPEN is described, in which the main algorithms belonging to the two first groups have been implemented, while the interactive techniques are implemented in PROMOIN (see Ref. [4]).

## 1.2. Existing implementations

Two main implementations can be found within the previously described framework: ADBASE and the systems GPSYS and IGPSYS. ADBASE was developed by Ralph Steuer in 1974, in the FOR-TRAN language, although, since then, it has undergone several revisions and improvements. This software determines all the efficient vertices and edges of a Linear Multiobjective problem. Besides this, it also has the option to solve a Lexicographic Goal Programming problem. This program runs under an MSDOS environment and uses a specific format for the data entry files. The original idea of the author was to create a code that was general enough to be implemented under any operating system, in a personal computer, and at a time when the use of Windows was not very widespread. These data entry files can only be edited by an MSDOS program, and this fact can be inconvenient when using Windows. On the other hand, GPSYS and IGPSYS, developed by M. Tamiz and D.F. Jones, are practically the only implementations for Goal Programming problems available at the moment. GPSYS solves Linear Goal Programming problems, and IGPSYS solves Integer Linear Goal Programming problems. Both programs have been implemented in the FORTRAN language and run under MSDOS. The implementations include all the normalization possibilities for Goal Programming as well as several options to detect and restore the efficiency of the final solutions. Nevertheless, the difficulties encountered regarding editing the data entry file are similar to those described for ADBASE. Thus, both implementations are highly efficient from a computational point of view, although they do not take advantage of the benefits offered by the implementation under a Windows environment.

Within the MOP implementations under Windows, the TOMMIX package [1] can be found in the literature. This software includes some of the most widely used Interactive MOP methods (STEM, Ziont–Wallenius, Interval Criterion Weights and Pareto Race methods) as well as their own method, TRIMAP. This package takes advantages of the Windows environment, but is mainly focused on Interactive methods. Apart from this specific software, all the main LP solvers can be used to obtain efficient solutions or to solve Goal Programming approaches. Obviously, these programs do not make a thorough analysis from the multicriteria point of view.

The implementation described in this paper tries to fulfill the need for systems for Multiobjective and Goal Programming problems under a Windows environment so that the data entry and layout format is simple and intuitive.

## 2. MOPEN

## 2.1. Technical features

MOPEN is a program for Windows, implemented in the C++ language; that is, the compiler Microsoft Visual C++, version 6.0, has been used. Presently, two versions of MOPEN are available.

MOPEN 1.1 uses as the libraries NAG in C (see Ref. [10]), mark 4, CPLEX version 6.5.1 (see Ref. [7]) and NAG in FORTRAN, mark 18 (see Ref. [11]) to solve the single criterion linear problems. MOPEN 1.2 has its own incorporated subroutines to solve such problems. The advantage of the former version is its quickness, while the latter is slower but does not require any license to use the libraries. In these current versions, the program can only solve linear problems, more precisely problems with up to 15,000 variables, 1500 constraints and 100 objective functions can be solved. Both versions are available upon request for all the researchers who wish to have a copy.

The performance of MOPEN, in terms of CPU time, is shown in Table 1, where the times for a series of test problems appear.

## 2.2. Working environment

Fig. 1 shows the main window frame of MOPEN, where the resolution, weight determination, options and help menus can be observed. Inside the main frame, the file-editing zone can also be seen. This zone makes it very simple to manage and visualize the information throughout the resolution process. The format of these files, as previously mentioned, is simple and intuitive, and they are edited in the same way as any text file in

Table 1  
Performance of MOPEN for a series of test problems

<table><tr><td>Problem</td><td>Variables</td><td>Constraints</td><td>Functions</td><td>Goals</td><td>P levels</td><td>Type</td><td>Time</td></tr><tr><td>#1</td><td>5</td><td>5</td><td>4</td><td>-</td><td>-</td><td>Cont.</td><td>7.64 s</td></tr><tr><td>#2</td><td>5</td><td>5</td><td>-</td><td>4</td><td>2</td><td>Cont.</td><td>0.31 s</td></tr><tr><td>#3</td><td>6</td><td>6</td><td>3</td><td>-</td><td>-</td><td>Int.</td><td>27.36 s</td></tr><tr><td>#4</td><td>6</td><td>7</td><td>-</td><td>4</td><td>2</td><td>Int.</td><td>8.68 s</td></tr><tr><td>#5</td><td>8</td><td>8</td><td>3</td><td>-</td><td>-</td><td>Cont.</td><td>1.74 s</td></tr><tr><td>#6</td><td>8</td><td>10</td><td>-</td><td>3</td><td>1</td><td>Cont.</td><td>2.38 s</td></tr><tr><td>#7</td><td>10</td><td>12</td><td>4</td><td>-</td><td>-</td><td>Cont.</td><td>9.93 s</td></tr><tr><td>#8</td><td>128</td><td>100</td><td>20</td><td>-</td><td>-</td><td>Cont.</td><td>21.03 s</td></tr><tr><td>#9</td><td>128</td><td>84</td><td>-</td><td>48</td><td>6</td><td>Cont.</td><td>0.98 s</td></tr><tr><td>#10</td><td>140</td><td>36</td><td>-</td><td>140</td><td>3</td><td>Cont.</td><td>0.96 s</td></tr><tr><td>#11</td><td>252</td><td>171</td><td>3</td><td>-</td><td>-</td><td>Cont.</td><td>3.25 s</td></tr><tr><td>#12</td><td>252</td><td>171</td><td>3</td><td>-</td><td>-</td><td>Int.</td><td>2 min 46 s</td></tr><tr><td>#13</td><td>3,124</td><td>712</td><td>3</td><td>710</td><td>5</td><td>Int.</td><td>3 h 46 min</td></tr></table>

The columns indicate the problem number, number of variables, number of constraints, number of objective functions, number of goals, number of priority levels, type of variables (continuous or integer) and overall computing time. The computing time is the mean time required in five randomly generated problems of the same size.

![](/api/attachments/WMYH9Y2S/fulltext/images/64a3f4549595a49e1ea2db2d7a3a17d36193d0a89f53fc62d41331fea4362870.jpg)  
Fig. 1. MOPEN: Main window.

Windows. Finally, MOPEN has a complete help system, where all the details concerning the functioning of the program can be found. In addition, information regarding the creation of data files, details about the algorithms implemented, normalization options, efficiency tests, etc., appear in the help system. All the available methods can be applied to a problem whose corresponding data are stored in a single file.

All the Multiobjective Programming algorithms implemented in the program can be found in the resolution menu. Many methods require the decision maker to give local weights for the objective functions and/or goals. As this may not be an easy task, MOPEN offers, in the <sup>d</sup>Weight Assistant<sup>T</sup> menu, a series of options devoted to facilitate this weight determination process. The user can generate weights by direct assignment methods (Ordering, Simple Assessing and Ratio Comparison) and by pairwise comparison methods (AHP, Geometric Mean, Pseudo-Inverse and Goal Programming). All the details concerning these weight determination methods can be found in Ref. [13]. The menu offers the possibility of including these weights in the file corresponding to the problem.

## 2.3. Data entry

MOPEN makes it possible to include in a single file all the data regarding the objective functions, goals and general features of the problem. This file can be created using a template (New File) or using an assistant program (Use Assistant). For small problems, the use of the assistant is recommended because it allows the user to provide all the data through a series of windows in an intuitive way. On the other hand, for large problems, it will generally be more comfortable to use the template because this option makes it possible to import in an easy way data that have been previously stored in other files, e.g., spreadsheets.

For example, let us consider the following problem ( P):

Objective functions (for the generating techniques):

$$
\begin{array}{l} \max f (x, y, z, t, u, v) = 4 x + 3 y + z - 3 t + 2 u \\ \min g (x, y, z, t, u, v) = 3 x + 2 y + 6 z - 2 t + v \\ \min h (x, y, z, t, u, v) = x + y + z - t + u - v \end{array}
$$

– Goals (for the Goal Programming option):

$$
\begin{array}{l l} \text {Priority} & G f: 4 x + 3 y + z - 3 t + 2 u + n _ {1} - p _ {1} = 2 5 \quad (\min n _ {1}) \\ \text {Level 1} & \\ \text {Priority} & G g: 3 x + 2 y + 6 z - 2 t + v + n _ {2} - p _ {2} = 1 1 \quad (\min p _ {2}) \\ \text {Level 2} & \\ \text {Priority} & G h: x + y + z - t + u - v + n _ {3} - p _ {3} = 1 0 \quad (\min p _ {3}) \\ \text {Level 3} & \end{array}
$$

– Constraints:

$$
\begin{array}{l l} & x + y - z + 3 t + u + 2 v \leq 1 5 \\ \text { s.t. } & 2 x + y + 3 z - t + 4 u + v \leq 2 4 \\ & x, y, z, t, u, v \geq 0 \\ & x, y, z, t, u, v \in R \end{array}
$$

The data file corresponding to problem ( P) will be called Sample.txt and is displayed in Fig. 2.

Let us observe that in this file, each group of data is labeled. Thus, lines such as Problem\_Name, Number\_ of\_variables or Number\_of\_Objectives appear in the file. These lines allow the program to identify the data, and any modification of such labels would cause a reading error. In order to prevent the user from modifying these lines, the template already contains them so that the user will only have to introduce the data.

## 2.4. Resolution

In order to solve the Multiobjective problems, MOPEN offers five groups of resolution algorithms. First, there are the efficient set generating techniques. In this group, the user can find the Weighting Method which, apart from introducing the weights during run time, has the option to automatically generate a set of weights in order to obtain an approximation of the efficient set with as many points as desired. The weight generating process is as follows:

Step 1 The user is asked to give the number q of weights for each objective (apart from the 0 weight).

Step 2 Function 1: from $i _ { 1 } { = } q$ to $i _ { 1 } { = } 0$ (step 1). Function 2: from $i _ { 2 } { = } q { - } i _ { 1 }$ to $i _ { 2 } { = } 0$ (step 1), . . . Function $p \colon i _ { p } = q - i _ { 1 } - i _ { 2 } - . . . - i _ { p - 1 } .$ Given the vector $( i _ { 1 } , i _ { 2 } , . . . , i _ { p - 1 } )$ , let:

$$
\lambda_ {j} = \frac {i _ {j}}{q}.
$$

Finally, the vector of weights $( \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { p } )$ is normalized according to the scheme chosen by the user (see Section 2.5).

It must be taken into account that if some zero weight is given, then the corresponding solution is only guaranteed to be weakly efficient. In this situation, MOPEN carries out an efficiency test of the solution. Namely, if $\mathbf { X } ^ { * }$ is the solution to be tested, the following p constraint problems are solved:

$$
\left(C _ {j}\right) \left\{ \begin{array}{l l} \min & f _ {1} (\mathbf {x}) \\ \text { s.t. } & \mathbf {x} \in X \\ & f _ {i} (\mathbf {x}) \leq f _ {i} (\mathbf {x} ^ {*}) \end{array} \right. \quad (i = 1, \dots , p; i \neq j)
$$

$\operatorname { I f } \mathbf { x } ^ { * }$ is an optimal solution for all the problems, then it is guaranteed that it is an efficient solution of $( P )$ . If not, $\mathbf { X } ^ { * }$ is just weakly efficient (and at least an efficient solution that dominates it is found in this process).

The Constraint Method can also be found in this group. Analogously to the previous case, the constraints can be either introduced by the user during run time or automatically generated by the program in order to approximate the efficient set. In this case, the bounds generation process is as follows:

Step 1 The user is asked to give the number q of bounds for each objective between its ideal and its anti-ideal values $( q { \ge } 2 )$ .

Step 2 From $i { = } 1$ to $p .$ Function 1: from $k _ { 1 } { = } i _ { 1 } { \ast }$ to $\begin{array} { r } { i ^ { ( 1 ) } \operatorname { s t e p } \frac { 1 } { a } \big ( i ^ { ( 1 ) } - i _ { 1 } * \big ) . } \end{array}$ (excluding function i). Function $p \colon$ from $k _ { p } = { i _ { p } } ^ { * }$ to $i ^ { ( p ) }$ step $\textstyle { \frac { 1 } { q } }$ $\left( i ^ { ( p ) } - i _ { p } * \right)$

The following constraint problem is generated:

$$
(C _ {j}) \left\{ \begin{array}{l l} \min & f _ {1} (\mathbf {x}) \\ \text {s.t.} & \mathbf {x} \in X \\ & f _ {j} (\mathbf {x}) \leq k _ {j} \end{array} \right. \quad (j = 1, \dots , p; j \neq i).
$$

The second group is related to Compromise Programming [23]. More precisely, in this option, for a given vector of weights, the $L _ { 1 }$ and $L _ { \infty }$ compromise solutions associated with the multicriteria problem under study are obtained. These are only two of the infinite compromise solutions that can be obtained (one for each metric $L _ { p } )$ . Only in the case when there are only two objectives do these two solutions define the compromise set (which is the segment that joins them). Again, an option is offered to automatically generate sets of weights (following the same procedure used for the weighting method) so as to generate efficient solutions for the problem.

![](/api/attachments/WMYH9Y2S/fulltext/images/e3eb62ef3c2d69b48443fbcfbc75a8c53464f2e55b3e20dc1f2b35d4db4b99ff.jpg)  
Fig. 2. Data file corresponding to problem ( P).

The third group incorporates all the Goal Programming techniques. Thus, any of the main schemes of this field can be applied, namely, the Lexicographic, Minimax, Weighted, Extended and Interval options are available. The differences among these options are the achievement functions considered in each of them. Let the goals have the form $f _ { i } ( { \bf x } ) { + } n _ { i } { - } p _ { i } { = } \alpha _ { i } ,$ then the three most common achievement functions are functions of the undesired deviation variables. Let $I _ { k }$ denotes the set of indexes corresponding to the goals placed in the kth priority level, whose undesired deviation variable is $p .$ Similarly, $J _ { k }$ is defined for the goals whose undesired deviation variable is $n ,$ and $K _ { k }$ for $n { + p }$ (if there is just one level, the subscript will not be used).

<sup>!</sup> Weighted scheme:

min

$$
\begin{array}{l} H (\mathbf {n}, \mathbf {p}) = \sum_ {i \in I} \mu_ {i} p _ {i} + \sum_ {i \in J} \mu_ {i} n _ {i} \\ \qquad + \sum_ {i \in K} \mu_ {i} (p _ {i} + n _ {i}), \end{array}
$$

<sup>!</sup> Minmax scheme:

$$
\begin{array}{c} H (\mathbf {n}, \mathbf {p}) = \max _ {i \in I} \left\{\mu_ {i} p _ {i} \right\} + \max _ {j \in J} \left\{\mu_ {i} n _ {i} \right\} \\ + \max _ {i \in K} \left\{\mu_ {i} (p _ {i} + n _ {i}) \right\}, \end{array}
$$

<sup>!</sup> Lexicographic scheme:

lexmin $( h _ { 1 } ( { \bf n } , { \bf p } ) , h _ { 2 } ( { \bf n } , { \bf p } ) , \cdot \cdot \cdot , h _ { s } ( { \bf n } , { \bf p } ) )$

<sup>!</sup> The Extended Lexicographic Goal Programming approach is a compromise scheme between the weighted and the minmax ones:

$$
\left\{ \begin{array}{l l} \text {lexmin} & (\lambda_ {1} d _ {1} + (1 - \lambda_ {1}) h _ {1} (\mathbf {n}, \mathbf {p}), \dots , \lambda_ {s} d _ {s} \\ & + (1 - \lambda_ {s}) h _ {s} (\mathbf {n}, \mathbf {p})) \\ \text {s.t.} & \mathbf {x} \in X \\ & f _ {i} (\mathbf {x}) + n _ {i} - p _ {i} = \alpha_ {i}, i = 1, \dots , p \\ & \mu_ {i} ^ {k} p _ {i} \leq d _ {k}, i \in I _ {k}, k = 1, \dots , s \\ & \mu_ {i} ^ {k} n _ {i} \leq d _ {k}, i \in J _ {k}, k = 1, \dots , s \\ & \mu_ {i} ^ {k} (p _ {i} + n _ {i}) \leq d _ {k}, i \in K _ {k}, k = 1, \dots , s \end{array} \right.
$$

<sup>!</sup> Finally, the Interval Goal Programming scheme allows the use of the so-called U-Penalty penalizing functions for the unachievements of the goals. In these functions, the user can establish different thresholds so that different unachievement levels are given different importance. For further details, see Refs. [17] and [19].

Once the Goal Programming resolution has been carried out, following any of the previously mentioned techniques, MOPEN allows the user to use several techniques of efficiency restoration of the solution. The efficiency restoration can be carried out using the Direct, Preference Based, Interactive or G.S.I. (see Ref. [3]) methods. All the details about Goal Programming and Restoration methods can be found in Ref. [18] for the continuous case and Ref. [21] for integer problems.

A new approach can be found in the fourth group: Satisfying and Efficient Solutions (see Ref. [2]). Under this approach, if the Goal Programming problem has solutions that satisfy all the goals, then efficient solutions are calculated within the satisfying set, i.e., within the set $S { = } \{ { \bf x } { \in } X / f _ { i } ( { \bf x } ) { \le } \alpha _ { i } ,$ $( i { = } 1 , . . . , p ) \}$ . To this end, the Weighting Method and the Constraint Method can be used, where families of weights or bounds, respectively, are automatically generated as previously described for the generating techniques. The efficiency of the solutions may be determined with respect to a set of objectives, which may or may not be related to the goals (see Section 2.6).

Finally, the fifth option corresponds to the Reference Point Method (see Ref. [22]). This method uses the Tchebychev achievement function in order to obtain, for a given set of target values and a given vector of weights, a satisfying and efficient solution. Again, the weights can be automatically generated in order to obtain a good approximation of the set of efficient and satisfying solutions.

The menu corresponding to these five groups of methodologies can be seen in Fig. 3.

Once the data file has been selected, a window appears in the screen, which shows the default names of all the solution files where the solutions corresponding to the current problem will be stored. Generally, the names of such files are assigned taking into account the problem name and the resolution method:

Sol <sup>b</sup>Resolucion Method´ <sup>N b</sup>File Name=

Problem Name<sup>N</sup>:txt

Finally, after solving the problem using a certain algorithm, the user will be offered the option of filtering the solutions obtained. This possibility will be described in Section 2.5. The default name of the file where the filtered solutions are stored is Fil\_<sup>b</sup>Name of the corresponding Solution File<sup>N</sup>. All these default names can be changed at any moment during the resolution process.

![](/api/attachments/WMYH9Y2S/fulltext/images/449cc0f50ea8374033db343ee6c84dee1fe365e17d7bdb02d999ac8210ee669c.jpg)  
Fig. 3. Resolution menu of MOPEN.

## 2.5. Utilities

The Options menu of MOPEN offers a series of tools in order to make it easier for the user to solve a problem, complete the data of a problem, choose normalization options, visualize data, etc. Fig. 4 shows these options.

First, let us highlight the Obtain Ideal and Anti-Ideal Values option. It can be very useful in many cases to know the ideal and anti-ideal values corresponding to each goal and/or objective, before starting the resolution process. In the case of a goal, it will be assumed that the corresponding function is to be maximized if the goal takes the form $f _ { i } ( \mathbf { x } ) { \geq } \alpha _ { i }$ and to be minimized if the goal takes the form $f _ { i } ( { \bf x } ) { \le } { \alpha } _ { i }$ . In general, these values can be helpful when fixing target values, choosing a function to be optimized, choosing the bounds in the weighting method or selecting a normalizing option. The Filtering option can also be found in this menu. First, the user is asked whether he/she prefers to filter using the values of the decision variables or the values of the objective functions. After this, the filtering radio r must be provided, which determines how fine the filtering process will be. Let us assume that the user decides to filter the results taking into account the values of the decision variables and let $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , . . . , \mathbf { x } _ { n } \right\}$ be the list of solutions to be filtered. Then the process is as follows:

![](/api/attachments/WMYH9Y2S/fulltext/images/4d40d317c698b288b6c475dae163d896448a1fea05a2d0a2c2db3f8557af33a6.jpg)  
Fig. 4. Options Menu of MOPEN.

Step 0 Let $X _ { f } = \varnothing .$ . Let ${ \bf { X } } _ { r } \mathrm { { = } } { \bf { X } } _ { n }$ be the reference point. Let $X _ { 1 } { = } \{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , . . . , \mathbf { x } _ { n - 1 } \}$ . Let k=0.

Step 1 Let $k { = } k { + } 1 . ~ X _ { f } { = } X _ { f } { \cup } \{ { \bf x } _ { r } \} . ~ A { = } \emptyset .$ For all $\begin{array} { r } { \mathbf { x } _ { i } { \in } \dot { X _ { k - 1 } } , \operatorname { i f } \ \sum _ { j = 1 } ^ { n } | x _ { i } ^ { j } - x _ { r } ^ { j } | \leq r , } \end{array}$ then make $A { = } A \cup \left\{ \mathbf { x } _ { i } \right\}$

Step 2 Let $X _ { k } { = } X _ { k - 1 } \backslash A .$

Step 3 If $X _ { k } { = } \emptyset ,$ then go to Step 5.

Step 4 Let $\mathbf { X } _ { r }$ be the point belonging to $X _ { k }$ whose subindex is the greatest. Go to Step 1.

Step 5 End of the filtering procedure. The set of filtered solutions, $X _ { f } ,$ is transferred to the file Fil\_<sup>b</sup>Name of the corresponding Solution File<sup>N</sup>.

The Branch and Bound Options of MOPEN offers a series of strategies for the application of the Branch and Bound method to integer problems. The user has the possibility to choose among the many different options of the method. This fact gives MOPEN a greater capacity and efficiency for the resolution of computationally expensive problems and turns it into an effective tool for integer Multiobjective Problems. The user can provide certain values such as the backtrack parameter and the cut threshold. Besides this, several options can be chosen for: selecting the next node to be examined, selecting the variable to be branched, choosing the branching option, deciding which kind of cuts can be made on the feasible set, deciding whether to use heuristic approaches or not and selecting options for the preprocessing phase. More details about the particularities of the Branch and Bound algorithm can be found in Ref. [12].

It is well known that the weights play an important role in the resolution of a Goal Programming problem. In order to avoid the possible bias effect of the solutions due to the different measurement units of the goals, MOPEN offers six different normalization options in the Goal Programming Normalizations menu. Namely, the user can choose among No Normalization, Percentage, Euclidean, L<sub>1</sub>, Zero– One or Free (see Section 2.6) normalization options. More details about these normalizations and their properties can be found in Ref. [20]. For the same reason, in the generating methods, the normalization of the weights assure a better distribution of the efficient solutions obtained. Therefore, the Efficient Set Generation Normalizations menu of MOPEN offers six different options to normalize the objective functions: No Normalization, Range (Ideal–Anti-Ideal), Euclidean, $L _ { 1 } ,$ , Ideal or Free (see Section 2.6).

Finally, the Transfer Solutions to an Excel File option offers the possibility to create an Excel file containing the solution of the problem. An assistant subroutine allows the user to send the solutions corresponding to any file to an Excel spreadsheet named Excel\_<sup>b</sup>Resolution Option<sup>N</sup>\_<sup>b</sup>Problem Name<sup>N</sup>.xls where the data are conveniently ordered.

## 2.6. Some programming aspects

In this section, some problems and challenges that have appeared during the programming process of MOPEN are mentioned, as well as the way they have been handled.

<sup>!</sup> When the Weighting Method is used as a generating technique in order to obtain efficient solutions, especially if the automatic generation option is chosen, the number of solutions calculated can be huge in not very large problems. This is why it was decided to include the filtering option of these solutions, described in Section 2.5. This way, the user can work with a more reasonable number of solutions contained in a smaller file. The same option is available when using the Constraint Method or compromise programming.

<sup>!</sup> When some zero weight is used in the weighting method, the corresponding solution is only guaranteed to be weakly efficient. This is why the efficiency test described in Section 2.4 is carried out in these cases. However, the problems $( C _ { j } )$ that are solved in this test are very likely to have a single feasible solution, $\mathbf { X } ^ { * }$ . This fact can cause instability problems when solving the problem, when it has large dimensions. This is why, in practice, a small tolerance is allowed in the constraints,

$$
f _ {i} (\mathbf {x}) \leq f _ {i} (\mathbf {x} ^ {*}) + \alpha
$$

and a similar tolerance is allowed for the corresponding optimal solutions.

<sup>!</sup> When using the Constraint Method as a generating technique, especially if the automatic generation option is chosen, many of the resulting constraint problems may have an empty feasible set. This fact has turned out to be the cause of computing errors when solving large problems. In order to overcome this eventuality, a Goal Programming approach has been used to test whether there are feasible solutions for the constraints of each problem. If there are feasible solutions, then the constraint problem is solved. If not, this information is transferred to the solution file, and the method proceeds to the next set of bounds.

<sup>!</sup> In general, the normalization of the weights or the functions in the different approaches are just a technical issue, in order to avoid undesired bias effects. However, the resulting solutions may be senseless for the decision maker. In a real application of our software, the decision makers expressed their wishes to divide the goals by numbers they considered significant (for example, for a function that determined the budget, a public hospital was going to receive from the government, they decided to divide it by the amount required by the hospital). These wishes did not fit any of the existing normalizations scheme, but still they turned out to be good normalizations from both the algorithmic and the decisional points of view. Thus, the so-called free normalization option was allowed. In this scheme, the user can give a number for each objective function or goal, so that each one will be divided by the given number.

<sup>!</sup> The resolution of compromise programming problems, using metrics different from $L _ { 1 } \ : \mathrm { o r } L _ { \infty } ,$ cannot be carried out using linear programming schemes because the objective function is nonlinear. Currently, the authors are working on the development of a version of MOPEN for certain kinds of nonlinear problems. This will make it possible to solve more compromise programming problems.

<sup>!</sup> As is well known, a Goal Programming scheme can produce a final solution which achieves all the goals, but is not efficient for the objectives underlying each goal. In this case, the efficiency restoration schemes mentioned in Section 2.4 can be used. However, in some real applications, the decision makers expressed their wish (once the achievement of the goals was assured) to search, within the satisfying set, efficient solutions for other objective functions. This is why MOPEN allows the possibility to use different functions for the goals and for the objectives.

<sup>!</sup> When working with problems with a large number of solutions, it is very likely that the user has the data previously stored in another format (e.g., an Excel spreadsheet). In this case, the conversion of the solution files to the spreadsheet may not be an easy task for the user. This is why MOPEN offers the possibility to export the solution files to an Excel spreadsheet, so that the final solutions can be visualized in a more convenient format.

<sup>!</sup> In order to test whether MOPEN was able to solve large Goal Programming problems, many randomly generated test problems were used. Their size was up to 1000 variables, and the results were compared with those given by CPLEX. This test proved that MOPEN could handle this type of problem.

## 3. Example

Next, problem ( P) (see Section 2.3) is solved using different methods, in order to show the behavior of MOPEN. First, the Weighting Method is used to generate efficient vertices by assigning weights to the objective functions. Using a single vector or weights, the solution shown in Fig. 5 is obtained. The user can choose between visualizing the solution function values or the solution point in the decision space. Besides this, the options of changing the weights and changing the normalization scheme are offered at this stage. This way, different solutions can be obtained using this method. Fig. 6 shows a fragment of the corresponding solution file (Sol\_WeightedSums\_ example.txt).

![](/api/attachments/WMYH9Y2S/fulltext/images/9ef96bff2c2b790978ef80bfb022f7b480a9daf83b4985c813d4cb92766b392b.jpg)  
Fig. 5. Resolution of ( P) by the Weighting Method.

```txt
Solutions using the file :Sample.txt
Problem Name :Sample

Pay-off Matrix
x*1 : f optimum    f(x*1) = 54    g(x*1) = 48    h(x*1) = 19.5
x*2 : g optimum    f(x*2) = -15    g(x*2) = -10    h(x*2) = -5
x*3 : h optimum    f(x*3) = 0    g(x*3) = 7.5    h(x*3) = -7.5

f : ideal = 54 anti-ideal = -15
g : ideal = -10 anti-ideal = 48
h : ideal = -7.5 anti-ideal = 19.5

Weighted-Sums solutions
Normalization used :Range Normalization (ideal—anti-ideal values)

Solution Point 1:
x = 0
y = 0
z = 0
t = 0
u = 0
v = 7.5
Objective function values at this point
f = 0
f weight = 1 * 0.0144928
g = 7.5
g weight = 1 * 0.0172414
h = -7.5
h weight = 1 * 0.037037
```  
Fig. 6. Initial fragment of the solution file corresponding to ( P), using the Weighting Method.

![](/api/attachments/WMYH9Y2S/fulltext/images/13db3415f343bb8f346d3d17879db835e2fecc36b1259a9c654e0b8a4aebaee2.jpg)  
Fig. 7. Resolution of ( P) by Goal Programming.

It can be observed that the weights used have been factorized so that both the original weight given by the user and the normalization factor can be seen. For example, for function $f ,$ the original weight is 1, and the normalizing factor is 0.0144928. This way, the user can visualize the solutions for the original weights, because the normalized ones can be meaningless from a preferential point of view. On the other hand, an experienced analyst can find out whether the normalizing option chosen is effective enough or not. If some zero weight is given, then the efficiency test described in Section 2.4 is carried out, and this information is transferred to the solution file.

Next, problem ( P) will be solved using the Lexicographic Goal Programming scheme. The Percentage option has been chosen to normalize weights assigned to the goals, and the Interactive option has been used to restore the efficiency of the original solution. In the example, there exist solutions that satisfy all the goals for the given target values, as shown in Fig. 7. This screen lets the user analyze the current satisfying solution. It is possible to change one or some target values, giving new absolute values for them or to relax all the unachieved target values up to a given percentage. If the Proceed to Restoration option is chosen, MOPEN starts the interactive restoration algorithm. In this case, the screen shown in Fig. 8 appears, where the current state of each goal (efficient, dominated or unbounded, see Ref. [20]) is displayed.

In our example, it can be seen that all goals are dominated. Goal Gf was chosen for restoration, and an efficient solution was obtained. All the results of the Goal Programming process, including the restoration scheme, are transferred to the file Sol\_Goal-Progrm\_Sample, which is shown in Fig. 9.

The information regarding the pay-off matrix is shown at the beginning of the file. It must be pointed out that a goal is not, and does not necessarily come from, a criterion to be maximized or minimized. Thus, it may seem senseless to talk about the corresponding pay-off matrix or the ideal or anti-ideal values of a goal. Nevertheless, as this information may be helpful for the user in order to give the target values, it is assumed that a goal $f _ { i } ( \mathbf { x } ) { \leq } u _ { i }$ is identified with a criterion to be minimized, and a goal of the form $f _ { i } ( \mathbf { x } ) { \geq } u _ { i }$ is identified with a function to be maximized. This is the way the elements of the pay-off matrix are obtained. Therefore, the user must be aware of this identification when interpreting the values of the payoff matrix. For example, for equality goals or goals with a nonclearly defined optimization (maximization or minimization) character, the pay-off matrix may not give significant information.

Next, the solutions of each priority level are shown. That is, the solution point, the values of its corresponding deviation variables, the optimal value

![](/api/attachments/WMYH9Y2S/fulltext/images/7a6a50247e95cd968ba6daae002f6381744013325294d0ffde849197bc344387.jpg)  
Fig. 8. Interactive Restoration of the Goal Programming solution.

```txt
Solutions using the file :Sample.txt
Problem Name : Sample
Pay-off Matrix
x*1 : Gf optimum Gf(x*1) = 54 Gg(x*1) = 48 Gh(x*1) = 19.5
x*2 : Gg optimum Gf(x*2) = -15 Gg(x*2) = -10 Gh(x*2) = -5
x*3 : Gh optimum Gf(x*3) = 0 Gg(x*3) = 7.5 Gh(x*3) = -7.5

Gf : ideal = 54 anti-ideal = -15
Gg : ideal = -10 anti-ideal = 48
Gh : ideal = -7.5 anti-ideal = 19.5

Target values:
f: 25
g: 11
h: 9.5

Normalization :Percentage
N[1] = 0.04
N[2] = 0.0909091
N[3] = 0.1
Pareto Restoration :Interactive restoration

Goal Programming solutions:
Priority Level :1
This problem has no unique solution
Solution Point:
x = 4.33333
y = 0
z = 0
t = 0
u = 3.83333
v = 0

Deviational variables:
n1 0
p1 0
n2 0
p2 2
n3 1.83333
p3 0
Achievement Function value :0

Goals values at this point:
Gf = 25
Gg = 13
Gh = 8.16667

Solution after 3 priority levels :
Solution Point:
x = 1
y = 4
z = 0
t = 0
u = 4.5
v = 0

Restoration :Interactive Restoration
Gf
current value :25
attainable value :25.0769
Inefficient Goal
```  
Fig. 9. Lexicographic Goal Programming solution file for problem ( P).

```txt
Gg
current value :11
attainable value :10.9091
Inefficient Goal
Gh
current value :9.5
attainable value :9.42857
Inefficient Goal

Interactive Restoration: Iteration 1
Solution Point :
x = 0
y = 5.30769
z = 0
t = 0
u = 4.57692
v = 0.384615

Deviational variables:
n1 0
p1 0.0769231
n2 0
p2 0
n3 0
p3 0
Goals values at this point:
Gf = 25.0769
Gg = 11
Gh = 9.5
Gf
current value :25.0769
attainable value :25.0769
Gg
current value :11
attainable value :11
Gh
current value :9.5
attainable value :9.5

Solution Point:
x = 0
y = 5.30769
z = 0
t = 0
u = 4.57692
v = 0.384615
Deviational variables:
n1 0
p1 0
n2 0
p2 0
n3 2.21271e-010
p3 0
Goals values at this point:
Gf = 25.0769
Gg = 11
Gh = 9.5
```  
Fig. 9 (continued).

of the achievement function and the current values of all the goals are displayed. If the optimal solution obtained for the current priority level is not unique, this fact is also pointed out by MOPEN. This information is very helpful to the user, in order to identify possible redundant levels, and to evaluate how optimistic or pessimistic the target values are. Finally, the information regarding the efficiency restoration procedure is shown including the status (efficient, dominated or unbounded) of each goal in each iteration and finishing with the final satisfying and efficient solution of the problem.

## 4. Conclusions

The computational package MOPEN has been described in this paper. MOPEN has been designed in order to use the main Multiobjective Programming and Goal Programming techniques, for linear problems with continuous and/or integer variables. Besides this, this package has been implemented under Windows environment. Thus, the user can enjoy all the advantages of such an implementation, i.e., a friendly interface, simple and intuitive data entry and layout procedures, etc. Generally speaking, the package has been designed in order to facilitate the resolution of linear multiple criteria problems of any kind (continuous, integer or binary variables), with a wide variety of methods (Efficient Set Generation, Goal Programming, Compromise Programming or Reference Point). The programs make it easy to build the data entry file, edit any of the files related to the solution of the problem, generate the weights for the criteria, edit the solution in a Excel spreadsheet, visualize the problem data and, fundamentally, apply any of the previously mentioned methodologies. These facts, together with a reasonably good performance, as shown in Section 2.1, turn MOPEN into a powerful tool for solving Linear Multiobjective problems, and it can be easily used in both teaching or research environments.

The wide variety of options in all the methods (normalization, determination of weights, efficiency restoration, etc.) can be very useful for an experimented analyst. In this sense, it must be pointed out that MOPEN has not been designed in order to substitute the analyst. On the contrary, an experienced analyst is necessary in order to use this package and make the best use of its potential capabilities.

Finally, there are two main future research lines in this field. First, this implementation must be validated, using it to solve real Multiobjective problems. Besides this, the Meta-Goal Programming option (see Ref. [14]) will be included. Second, a version of the package for nonlinear problems is presently being designed.

## Acknowledgements

The authors wish to express their gratitude to the anonymous referees who have made significant contributions to improve the quality of the original manuscript. This research has been partially founded by the research projects SEJ 417 (Andalusian Regional Government) and SEC 2001-1742, BFM 2001-1844 and BFM 2002-11282-E (Spanish Ministry of Science and Technology).

## References

[1] C.H. Antunes, M.J. Alves, A. Silva, J. Climaco, An integrated MOLP method base package—a guided tour of TOMMIX, Computers & Operations Research 19 (7) (1992) 609 – 625.

[2] R. Caballero, L. Rey, F. Ruiz, Determination of satisfying and efficient solutions in convex multi-objective programming, Optimization 37 (1996) 125 – 137.

[3] R. Caballero, L. Rey, F. Ruiz, Lexicographic improvement of the target values in convex goal programming, European Journal of Operational Research 107 (1998) 644– 655.

[4] R. Caballero, M. Luque, J. Molina, F. Ruiz, PROMOIN: an interactive system for multiobjective programming, International Journal of Information Technology and Decision Making 1 (4) (2002) 635– 656.

[5] J.P. Ignizio, Goal Programming and Extensions, Lexington Books, Massachusetts, 1976.

[6] Y. Ijiri, Management Goals and Accounting for Control, North Holland, Amsterdam, 1965.

[7] ILOG CPLEX, ILOG CPLEX 6.5, Reference Manual, ILOG S.A., Madrid, 1999.

[8] S.M. Lee, Goal Programming for Decision Analysis, Auerbach Publishers, Philadelphia, 1972.

[9] K. Miettinen, Nonlinear Multiobjective Optimization, Kluwer Academic Publishers, 1999.

[10] NAG (Numerical Algorithm Group Limited), NAG C Library Manual. Mark 4, NAG, Oxford, 1996.

[11] NAG (Numerical Algorithm Group Limited), NAG FOR-TRAN Library Manual. Mark 18, NAG, Oxford, 1997.

[12] G.L. Nemhauser, L.A. Wolsey, Integer and Combinatorial Optimization, Wiley, New York, 1988.

[13] J.C. Pomerol, S. Barba-Romero, Multicriterion Decision Making in Management, Kluwer, London, 2000, Kluwer Series in Operation Research.

[14] M.V. Rodrı´guez Urı´a, R. Caballero, F. Ruiz, C. Romero, Metagoal programming, European Journal of Operational Research 136 (2002) 422– 429.

[15] C. Romero, Handbook of Critical Issues in Goal Programming, Pergamon, Oxford, 1991.

[16] R.E. Steuer, Multiple Criteria Optimization: Theory, Computation, and Application, Wiley, New York, 1986.

[17] M. Tamiz, D.F. Jones, Expanding the flexibility of goal programming via preference modelling techniques, Omega 23 (1995) 41–48.

[18] M. Tamiz, D.F. Jones, Goal programming and Pareto efficiency, Journal of Information and Optimization Sciences 17 (2) (1996) 1 – 17.

[19] M. Tamiz, D.F. Jones, A. El-Darzi, Review of goal programming and its applications, Annals of Operations Research 58 (1995) 39 – 53.

[20] M. Tamiz, D.F. Jones, C. Romero, Goal programming for decision making. An overview of the current state-of-theart, European Journal of Operational Research 111 (1998) 569 – 581.

[21] M. Tamiz, S.K. Mirrazavi, D.F. Jones, Extensions of Pareto efficiency analysis to integer goal programming, Omega 27 (1999) 179–188.

[22] A.P. Wierzbicki, The use of reference objectives in multiobjective optimization, in: G. Fandel, T. Gal (Eds.), Multiple Criteria Decision Making: Theory and Application, Lecture Notes in Economics and Mathematics Systems, vol. 177, Springer-Verlag, Heidelberg, 1979.

[23] P.L. Yu, A class of solutions for group decision problems, Management Science 19 (1973) 936 – 946.

[24] M. Zeleny, Compromise programming, in: J.L. Cochrane, M. Zeleny (Eds.), Multiple Criteria Decision Making, University of South Carolina Press, Columbia, 1973.

![](/api/attachments/WMYH9Y2S/fulltext/images/14f5d1ae228b79758f62061f998fdff05ddf7a8bf8979801dd314011756cf042.jpg)  
Rafael Caballero is a Professor in the Department of Applied Economics (Mathematics), University of Ma´laga, Spain. He holds a PhD degree in Mathematics obtained from the University of Ma´laga. He is interested in the field of Multiple Objective Programming (linear, quadratic, convex, combinatorial, etc.). Presently, his research is in heuristics methods and application to problems in the public sector.

![](/api/attachments/WMYH9Y2S/fulltext/images/1e3c1e4acce87e707cc099b00311768622aba64b839f013ba1cab4bdf19418a1.jpg)  
Francisco Ruiz is an Assistant Professor in the Department of Applied Economics (Mathematics), University of Ma´ laga, Spain. He holds a PhD degree in Economics Sciences obtained from the University of Ma´laga. His research has been carried out in the field of linear, quadratic, convex, combinatorial, hierarchical Multiple Objective Programming. Presently, he is interested in interactive methods.

![](/api/attachments/WMYH9Y2S/fulltext/images/217919dc827f3afb534a8fca71115644857710158e298a9fc9d9dce8e328671d.jpg)

Mariano Luque holds a PhD degree in Economics Sciences and holds a senior lecturing post at the University of Ma´laga. Nearly all his research has been carried out in the field of Hierarchical Multiple Objective Programming. Presently, his research is based on interactive methods.

![](/api/attachments/WMYH9Y2S/fulltext/images/006538a7e83ebd0e093bcc1f785aae62b0b795b6ddb5902b8c3a60fde6de4114.jpg)  
Julian Molina holds a PhD degree in Economic Science obtained from the University of Ma´laga. His research has been carried out in the field of Multiple Objective integer and continuous Programming,. Presently, his research is based on metaherustic algorithms for Multiple Objective Programming problems and their applications.
