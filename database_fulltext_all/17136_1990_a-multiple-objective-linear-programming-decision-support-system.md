---
otero_id: 17136
otero_key: "FD99HRUU"
title: "A multiple objective linear programming decision support system"
authors: "Pekka Korhonen; Jyrki Wallenius"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90017-l"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Multiple Objective Linear Programming Decision Support System

Pekka KORHONEN and Jyrki WALLENIUS \*
Helsinki School of Economics, 00100 Helsinki, Finland

In this paper we describe the principles of VIG (Visual Interactive Goal Programming), a Multiple Criteria Decision Support System, recently developed by Korhonen. PARETO RACE is a corner-stone of the system, which is designed to support both the modelling and solving of a multiple objective linear programming problem. A menu, spreadsheets, and interactive computer graphics play a key role.

Keywords: Decision Support; Computer Graphics; Multiple Criteria.

![](/api/attachments/FD99HRUU/fulltext/images/0b11fdf967c146301f870e9c75c47abed80a82af6cfd4c421d9e7e8437df892e.jpg)

Pekka J. Korhonen is Professor of Statistics at the Helsinki School of Economics, Finland. He received a B.S. and M.S. in Mathematics and Ph.D. in Applied Mathematics, all from the University of Helsinki. His research interests are multiple criteria decision making, interactive computer graphics, computational statistics, the applications of such models to management problem solving. His articles have appeared in The Journal of the Operational Research Society, Management

Science, Computational Statistics & Data Analysis, Quarterly Publication of the International Research Institute of Management Sciences (MNIIPU), European Journal of Operational Research, Naval Research Logistics Quarterly, Fuzzy Sets and Systems, Interfaces, Operations Research, VNIISI Publications, Belgian Journal of Operations Research, Statistics and Computer Science, Mathematical Modelling.

The authors wish to thank Mr. Hannu Törmä, University of Jyväskylä, for making the illustrative example available to them. The research is supported, in part, by grants from the Y. Jahnsson Foundation, the Foundation for Economic Education, the Foundation of the Helsinki School of Economics, and the Foundation of the Student Union of the Helsinki School of Economics.

## 1. Introduction

As Weber [16] points out, the concept of Decision Support Systems (DSS) is now more than a decade old. Decision Support Systems have over the years been developed and successfully implemented in many organizations by individuals at different organizational levels. Various definitions have been offered for decision support. Ginzberg and Stohr [2] define a DSS as “a computer-based information system used to support decision-making activities in situations where it is not possible or not desirable to have an automated system perform the entire decision process”. Multiple Criteria Decision Support Systems (MCDSS) are considered by Jelassi et al. [4] as a “specific” type of system within the broad family of DSS. Even though MCDSS include much the same components as “traditional” Decision Support Systems, MCDSS have special characteristics that distinguish them from other DSS. Such characteristics include the fact that they allow analysis of multiple criteria; they use a variety of multiple criteria decision methods to compute efficient solutions; they incorporate user’s input in various phases of modelling and solving a problem. While it has been customary to consider algorithms as the focal point of decision support, emphasis is shifting to the database and modelling activities. See, for example, Keen and Scott-Morton [5],

![](/api/attachments/FD99HRUU/fulltext/images/6d782cfc574c4792a47068744294d934ddfa1356de9f8f8f9b54b64ae958bfce.jpg)

Jyrki Wallenius serves as Professor of Management at the Helsinki School of Economics. He received his Ph.D. from the Helsinki School of Economics, Dr. Wallenius' research interests include multiple criteria optimization, decision analysis, and decision support systems. He is the author or coauthor of numerous articles in such journals as Management Science, Operations Research, Naval Research Logistics, and the Journal of the Operational Research Society, among others. He is an

Associate Editor of the European Journal of Operational Research. Dr. Wallenius is presently an Associate Professor of Management at the University of Jyväskylä, Finland, and has been a Visiting Professor at Purdue University and Arizona State University, in the United States.

Sprague and Carlson [11], Bui [1], and Van Hee [14].

In this paper we describe the principles of VIG (Visual Interactive Goal Programming), a Multiple Criteria Decision Support System recently developed by Korhonen [7,8]. The system is user-friendly and it is designed to support both the modelling and solving of a multiple objective linear programming problem. Menus, spreadsheets, and interactive use of computer graphics play a central role. Constraints and objectives are treated uniformly (see, e.g., [3]); their role may be changed during a session. VIG is written in TURBO PASCAL and implemented on an IBM PC/1 microcomputer. To benefit fully from VIG, a color monitor should be used. In this system, PARETO RACE, a visual, dynamic, search procedure for exploring the efficient frontier of a multiple objective linear programming problem, plays a central role [10]. In PARETO RACE the user sees the objective function values (flexible goals) on a display in numeric form and as bar graphs, as he travels along the efficient frontier. The keyboard controls include an accelerator, gears, brakes, and a steering mechanism.

This paper consists of six sections. The introduction explains the underlying philosophy of VIG. The second section consists of the mathematical foundations. The third section provides an illustrative example that is used throughout the paper. The fourth section describes the structure of VIG. The fifth section discusses PARETO RACE. The sixth section concludes the paper.

## 2. Mathematical Foundations

In multiple objective linear programming, the DM selects a number of outcome variables as objective functions and attempts to maximize (or minimize) them, simultaneously. Since this problem has rarely, if ever, a unique solution, the DM is expected to choose a solution from among the set of nondominated (efficient) solutions.

Generally, the multiple objective linear programming problem can be formulated as follows: "max" Cx

subject to:

$$
\boldsymbol {x} \in X = \left\{\boldsymbol {x} \mid A \boldsymbol {x} = \boldsymbol {b}, \boldsymbol {x} \geq \mathbf {0} \right\}.\tag{2.1}
$$

C is a $k \times n$ matrix of coefficients of the objective functions ( $C' = [C_1, C_2, \ldots, C_k]$ ), A is an $m \times n$ matrix of coefficients of the constraints, b is an m-vector of the rhs, $b \in R^m$ , and x is an n-vector of decision variables, $x \in R^n$ .

We define efficiency and weak efficiency in the usual manner:

Definition 1. A point $\pmb{x}^0 \in X$ is efficient iff there does not exist another $\pmb{x} \in X$ such that $C\pmb{x} \geq C\pmb{x}^0$ and $C_i\pmb{x} \neq C_i\pmb{x}^0$ for at least one $i \in \{1, 2, \ldots, k\}$ .

Definition 2. A point $\pmb{x}^0 \in X$ is weakly-efficient iff there does not exist another $\pmb{x} \in X$ such that $C\pmb{x} > C\pmb{x}^0$ .

The criterion vectors corresponding to (weakly) efficient points are called (weakly) efficient or nondominated solutions.

For generating efficient solutions for the DM's evaluation, some rules bearing a relationship to the DM's aspirations must be established. Such rules may be based on an implicitly or explicitly defined achievement (scalarizing) functions as suggested by Wierzbicki [17]. Such a function projects any given (feasible or infeasible) point $g \in R^{k}$ onto the set of (weakly) nondominated solutions. The function is suitable for generating non-dominated solutions. We use the following simple function:

$$
\begin{array}{l} z (\boldsymbol {g}, \boldsymbol {q}, \boldsymbol {w}) \\ = \max \left[ \left(g _ {i} - q _ {i}\right) / w _ {i}, \quad i \in \{1, 2, \dots , k \} \right], \end{array}\tag{2.2}
$$

where w > 0 is a k-vector of weights, $g \in R^{k}$ an arbitrary vector, the components of which are called aspiration levels, and $q \in Q = \{Cx \mid x \in X\}$ . By minimizing $z(g, q, w)$ subject to $q \in Q$ , we find a weakly nondominated solution vector $q^{0}$ (see, e.g., Wierzbicki [17,18]). If the given solution $g \in R^{k}$ is feasible, then $q^{0} \in Q$ , $q^{0} \geq g$ . To generate only nondominated (instead of weakly nondominated) solutions, more complicated forms have to be used. However, this simple form is computationally efficient.

Using the achievement function (2.2), the multiple objective linear programming problem can be presented in the following parametric form (see, [10]), which makes all efficient solutions extreme point solutions:

min y

s.t.

$$
\begin{array}{l l} C x + w y - I z = g \\ A x & = b \\ x, z & \geq 0, \end{array}\tag{2.3}
$$

where y is a scalar variable to be minimized and z is the k-vector of surplus variables for objective rows. Given $g \in R^{k}$ , as a solution we will find a weakly efficient point x. To move on the efficient frontier, we can vary the vector w or the aspiration levels g. We use the latter way by formulating the problem in a parametric programming form: min y

s.t.

$$
\begin{array}{l l} C x + w y - I z = g + t d \\ A x & = b \\ x, z & \geq 0, \end{array}\tag{2.4}
$$

where $d \in R^{k}$ is a so-called reference direction (Korhonen and Laakso [6]), and $t \geq 0$ a parameter. In the VIG-system the reference direction is specified dynamically by the system.

Furthermore, it is not even necessary to make a conceptual difference between objective functions and constraints, because their roles can be changed during the solution process. A unified formulation for objective functions and constraints can be written as follows (see, [10]):

min $y$

s.t.

$$
\begin{array}{l} D \boldsymbol {u} + w y = \boldsymbol {b} ^ {+}, \\ \boldsymbol {u} \geq \mathbf {0}, \end{array}\tag{2.5}
$$

where $w \geq 0$ is now a $(k + m)$ -vector whose components are

$$
w _ {i} \left[ \begin{array}{l} = 0, \text {   if   } i \text {   refers   to   a   constraint }, \\ > 0, \text {   if   } i \text {   refers   to   an   objective }, \end{array} \right.
$$

$u \in R^{n+k}, D$ is a $(k+m) \times n$ matrix of coefficients:

$$
D = \left[ \begin{array}{c c} C & - I \\ A & 0 \end{array} \right],
$$

and $b^{+}$ is a $(k+m)$ -vector, $b^{+}=[g',b']'$ , consisting of aspiration levels g and the rhs-vector b.

The treatment of the multiple objective linear programming problem in the VIG-system is based on formulation (2.5).

## 3. An Illustration

Consider the following (real) problem: The Finnish Government is interested in decreasing the industry's demand for energy by manipulating the factor prices for capital, labor, energy, and raw-materials. The demand structure is described using the following set of equations

$$
\sum_ {j} e _ {i j} \mathrm{d} P _ {j} - \mathrm{d} X _ {i} = 0, \quad i, j = \mathrm{C}, \mathrm{L}, \mathrm{E}, \mathrm{M},
$$

where $e_{ij}$ stands for the cross elasticity of demand, $dP_{j}$ represents the (percentage) change in factor price, $dX_{i}$ is the (percentage) change in the demand for factor input. Indices C, L, E, and M stand for the factor inputs: capital, labor, energy, and raw-materials, respectively.

The estimated cross elasticities $(e_{ij})$ are the following:

<table><tr><td></td><td>C</td><td>L</td><td>E</td><td>M</td></tr><tr><td>C</td><td>-0.278</td><td>0.128</td><td>0.032</td><td>0.118</td></tr><tr><td>L</td><td>0.036</td><td>-0.140</td><td>0.024</td><td>0.079</td></tr><tr><td>E</td><td>0.065</td><td>0.169</td><td>-0.408</td><td>0.174</td></tr><tr><td>M</td><td>0.011</td><td>0.025</td><td>0.008</td><td>-0.044</td></tr></table>

Source: Törmä [12] and [13].

The problem is to

\- maximize the increase in the demand for labor,
- maximize the decrease in the demand for energy,

\- minimize increases in the factor prices,

such that the percentage changes in the factor prices range from -5 to +7, and the demand for capital and raw-materials remains unchanged.

Mathematically, we formulate the problem as a multiple objective linear programming problem:

$$
\text { Max } \quad \mathrm{d} X _ {\mathrm{L}} = \sum_ {j} e _ {\mathrm{L} j} \mathrm{d} P _ {j},
$$

$$
\mathrm{Min} \quad \mathrm{d} X _ {\mathrm{E}} = \sum_ {j} e _ {\mathrm{E} j} \mathrm{d} P _ {j},
$$

$$
\mathrm{Min} \quad \mathrm{d} P _ {j} \quad j = \mathrm{C}, \mathrm{L}, \mathrm{E}, \mathrm{M},
$$

subject to

$$
\mathrm{d} X _ {\mathrm{C}} = \sum_ {j} e _ {\mathrm{C} j} \mathrm{d} P _ {j} = 0,
$$

$$
\mathrm{d} X _ {\mathbf {M}} = \sum_ {\mathbf {M}} e _ {\mathbf {M} j} \mathrm{d} P _ {j} = 0,
$$

$$
- 5 \leqslant \mathrm{d} P _ {j} \leqslant 7 \quad (j = \mathrm{C}, \mathrm{L}, \mathrm{E}, \mathrm{M}).
$$

We use the above problem to illustrate the different functions of VIG.

## 4. The Structure of the System

VIG is implemented in the spirit of visual interaction. Following the terminology of goal programming, constraints are regarded as a subset of goals. In fact, constraints are inflexible goals.

VIG has four main functions:

(1) Model Management Function (Allowing us to create, edit, store, and retrieve models.)

(2) Model Development Function (Allowing us to provide the decision variables and outcome variables (goals) with names, specify the technology matrix describing the relationships among the variables, and determine aspiration levels for the goals.)

(3) Problem Solving Function (Allowing us to tell the system, how the problem should be solved – and actually to solve it. With more than one objective (flexible goals), PARETO RACE is invoked. With one or no objectives, no user's intervention is necessary.)

(4) Solution Output Function (Allowing us to examine solutions on the screen, and store intermediate results for later consideration or for writing reports.)

Each main function consists of one or more subfunctions, which are all chosen from the main menu (fig. 1). At each stage, the available choices are shown using light cyan. All functions are not available all the time. For example, one cannot examine a solution before it is computed. Using only one main menu makes it easy to keep the control of the program in the user's hands. The user is welcome to choose anyone of the available functions without "having to run through the entire list". When a function is terminated (using the F10-key), the system prints the main menu. By moving the cursor up and down, we can trace all available choices.

## Model Management Function

“Select Model” and “Save the Model” activate Model Management Functions. When we enter “Select Model”, the system prompts us to provide the model with a name. If we are creating a model, the system uses “Temp” as a default name. If we wish to save the model, another name should be used. “Temp” will be erased at the end of the session. By entering “Save the Model” we store the current version of the model into the default directory. We can rename it or use the old name.

## Model Development Function

The model is entered in three phases. Each phase has its own spreadsheet format. Using arrow keys, we can move from one field to another. The use of any other key activates the field, and makes it ready for out input.

![](/api/attachments/FD99HRUU/fulltext/images/3358ee68e49d6d807f30a783ffd2cfea060e0d0929e65b83038f7afac2b0df9f.jpg)  
Fig. 1. The Main Menu.

<table><tr><td colspan="4">Editing the Types and Aspiration Levels of Goals</td></tr><tr><td>Names</td><td>Types</td><td>Given Values</td><td>Current Values</td></tr><tr><td>DXC</td><td>==</td><td>0.0000000</td><td>0.0000000</td></tr><tr><td>DXL</td><td>&gt;=</td><td>0.0000000</td><td>0.0000000</td></tr><tr><td>DXE</td><td>&lt;=</td><td>5.0000000</td><td>0.0000000</td></tr><tr><td>DXM</td><td>==</td><td>0.0000000</td><td>0.0000000</td></tr><tr><td>DPC (U)</td><td>&lt;=</td><td>7.0000000</td><td>0.0000000</td></tr><tr><td>DPL (U)</td><td>&lt;=</td><td>7.0000000</td><td>0.0000000</td></tr><tr><td>DPE (U)</td><td>&lt;=</td><td>7.0000000</td><td>0.0000000</td></tr><tr><td>DPM (U)</td><td>&lt;=</td><td>7.0000000</td><td>0.0000000</td></tr><tr><td>DPC (L)</td><td>&gt;=</td><td>-5.0000000</td><td>0.0000000</td></tr><tr><td>DPL (L)</td><td>&gt;=</td><td>-5.0000000</td><td>0.0000000</td></tr><tr><td>DPE (L)</td><td>&gt;=</td><td>-5.0000000</td><td>0.0000000</td></tr><tr><td>DPM (L)</td><td>&gt;=</td><td>-5.0000000</td><td>0.0000000</td></tr></table>

Fig. 2. Aspiration Levels.

Initially, we are asked to provide the decision variables (columns) and goals (rows) with names. At this stage we are urged to consider the question: “What are my options and what are their consequences?”, without incorporating numbers. When creating a model, only the frames of the names are provided.

Next, we enter the choice “Edit Matrix Coefficients” and specify the technology matrix of the problem. In other words, we specify the dependences of the goals on the decision variables. At this stage, the relevant question is: “How will my decisions affect the values of the goals?”

Finally, we define aspiration levels for the goals (the right-hand-side vector) (fig. 2: Given Values). We also define the directions of the inequalities (Types). The direction indicates, whether we wish to exceed the aspiration levels or fall below them. For example, the “greater than or equal” symbol associated with DXL indicates that we wish to maximize the increase in the demand for labor. Similarly, the “less than or equal” symbol of DXE indicates minimization of increases in the demand for energy. No changes in the demand for capital or raw-materials are allowed (Type “=”). The RHS-vector also specifies the upper and lower bounds (+7 and -5) for the factor price changes.

Note that up to this point we have not made any distinction between objectives and constraints. We have treated them in a uniform manner.

Problem Solving Function

This function consists of three phases: Classifying the Goals, Specifying Ranges for Flexible Goals, and Solving the Problem. Initially, all goals are assumed to be inflexible (that is, constraints). Moving the cursor to point to a row name and pressing SPACE BAR once changes the status of the goal (from inflexible to flexible, and vice versa). On the screen, brown stands for inflexible and white for flexible goals.

If none of the goals is specified to be flexible, the program will find a feasible solution, if one exists. If one of the goals is specified flexible, the program solves a linear programming problem after we have entered “Solve the Problem”. This is done without user’s intervention. If more than one goal is flexible, the system invokes PARETO RACE. PARETO RACE needs the user to specify approximate ranges for the flexible goals (fig. 3). In our example we have six flexible goals. DXL and DXE are (initially) allowed to vary from -5 to +5. As bounds for the factor price changes we use the values specified in fig. 2.

Ranges for flexible goals are needed for defining the ranges for the lengths of the bars on the screen, and specifying the weight vector w in formula (2.5). To obtain a maximum benefit from the visual feature of PARETO RACE, we recommend careful consideration of the ranges (even though they are automatically updated by the system). Sometimes it is advisable to respecify the ranges during the race. In the use of the program, experience is a good teacher.

<table><tr><td>Names</td><td>Types</td><td>Given Values</td><td>Current Values</td><td>Lower Bounds</td><td>Upper Bounds</td></tr><tr><td>DXL</td><td>&gt;=</td><td>0.0000000</td><td>0.0000000</td><td>-5.000000</td><td>5.0000000</td></tr><tr><td>DXE</td><td>&lt;=</td><td>5.0000000</td><td>0.0000000</td><td>-5.000000</td><td>5.0000000</td></tr><tr><td>DPC (U)</td><td>&lt;=</td><td>10.000000</td><td>0.0000000</td><td>-5.0000000</td><td>7.0000000</td></tr><tr><td>DPL (U)</td><td>&lt;=</td><td>10.000000</td><td>0.0000000</td><td>-5.0000000</td><td>7.0000000</td></tr><tr><td>DPE (U)</td><td>&lt;=</td><td>10.000000</td><td>0.0000000</td><td>-5.0000000</td><td>7.0000000</td></tr><tr><td>DPM (U)</td><td>&lt;=</td><td>10.000000</td><td>0.0000000</td><td>-5.0000000</td><td>7.0000000</td></tr></table>

Fig. 3. Bounds for Flexible Goals.

By entering “Solve the Problem”, the PARETO RACE screen is displayed (fig. 4). Mathematically, the system finds an initial solution by projecting the given values of goals onto the efficient frontier. This is accomplished by solving a linear programming problem of type (2.3). Since PARETO RACE is a corner-stone of our system, it is explained more in detail in the next section.

Solution Output Function

After using PARETO RACE, the choices “Display the Values of Goals”, “Display the Values of Decision Variables”, and “Save the Solution” become available. They enable us to examine the values of all flexible and inflexible goals, and the values of nonzero decision variables. We can save intermediate solutions on a diskette or a hard disc. It is possible to store all solutions in the same file.

![](/api/attachments/FD99HRUU/fulltext/images/6db4e540e4bc0bfede147d58c3b2de3ba8eac96822f37b950c5bc2f53674476a.jpg)  
Fig. 4. An Example of PARETO RACE: Initial Solution (Making a Turn).

![](/api/attachments/FD99HRUU/fulltext/images/aab52c231c3adcf3a39fd16414f35ff4bfaf3900d3796b25a9abd4438d2e16c1.jpg)  
Fig. 5. An Example of PARETO RACE: Final Solution.

Afterwards we may examine solutions using a text processing system or a text editor.

Having obtained one solution, we can go back and edit the model, change the set of flexible goals, or respecify the ranges for the flexible goals for a better visual effect. We can also return to PARETO RACE. The race starts from the current solution, if we have not edited the model in the meantime. In our example, due to the simplicity of the problem, all the necessary information can be found in fig. 5 (without entering “Display the Values of Decision Variables”). At the final solution, prices for capital, labor, and raw-materials decrease from last year. The price for energy remains constant. The demand for labor slightly increases (0.26%) and the demand for energy considerably decreases (1.8%).

## 5. Pareto Race

In PARETO RACE, we can freely search the efficient frontier of a multiple objective linear programming problem. Specific keys are used to control the speed and direction of motion. On a display, we see the objective function values in numeric form and as bar graphs whose lengths are dynamically changing as we move about on the efficient frontier. The keyboard controls include the following function keys (see, fig. 4 and fig. 5):

(SPACE) BAR: An "Accelerator"

We proceed in the current direction at constant speed.

F1: “Gears (Backward)” Increase speed in the backward direction.

F2: “Gears (Forward)” Increase speed in the forward direction.

F3: “Fix the Aspiration Level of a Specific Goal” The current value of a specific goal is taken as an absolute lower (upper) bound.

F4: “Relax the Aspiration Level of a Fixed Goal” The fixed goal becomes flexible again.

F5: "Brakes"
Reduce speed.

num: "Turn"

num: "Turn"
Change the direction of motion by pressing the number key corresponding to the goal's ordinal number once or several times.

F10: "EXIT"

Exit to the main menu.

Initially, we are going to see (graphically and numerically) an efficient solution on the computer screen (fig. 4). Arrows indicate an initial direction chosen by the computer (based on our aspiration levels). If we like this initial direction, we hold SPACE BAR down and observe the solutions change. We are “travelling” at base speed. If we like to increase the speed, press the F2-key once or several times (depending on the desired speed)

and hold SPACE BAR down. If at some point the direction is no longer attractive, we initiate a turn (see, fig. 4). Assume that the user wishes to improve a certain goal (goal number $5 =$ price for energy). To accomplish this, the goal's corresponding number key is pressed once or several times, depending on the amount of desired improvement. Mathematically, the system updates the reference direction $\pmb{d}$ in (2.4) in a certain systematic way as explained in more detail in Korhonen and Wallenius [10] and projects it onto the efficient frontier. Note that the DM will only see the feasible and nondominated values of the objectives on the screen. To reduce speed, we use brakes (F5-key). If we wish to resume base speed, the most convenient way is to press the F1-key (gears: backward) and then the F2-key (gears: forward). We reverse direction twice and start travelling at base speed. When a flexible goal is fixed by using the F3-key, the system asks us to specify the number of the goal to be fixed; then an asterisk appears next to the name of such a goal. The goal may be relaxed by using the F4-key; the asterisk disappears.

When we terminate PARETO RACE, we are welcome to examine the values of the decision variables and goals. Just exit to the main menu. In fact, the user can examine the values of the decision variables and goals also during the race (and save such intermediate results for later use). Simply enter “Solve the Problem” in the main menu and we are back in the race. We can also change the role of flexible and rigid goals during the race. We feel that this adds flexibility to the system and extends it beyond “classical” multiple objective linear programming.

## 6. Conclusion

In this paper we have described a software package called VIG. It is essentially a Multiple Criteria Decision Support System for modelling and solving multiple objective linear programming problems. The computer program is written in TURBO PASCAL and it implements PARETO RACE as an essential ingredient. The necessary hardware consists of an IBM compatible Personal Computer with at least one diskette drive and a graphics card. The minimum memory size is 256 Kbytes. Preferably, a color monitor should be used. The current version of the program is capable of solving problems with a maximum of 96 variables and 100 goals, from which at most ten may be flexible, simultaneously. The size of the array may technically be increased, but for computational reasons the race starts to resemble “the crawl of a turtle” when the problem size is increased. To solve large-scale problems requires a different approach. For this purpose, we are developing a method, which is based on blending some of our previous research ideas.

The VIG-system consists of more than 3000 lines of code, most of which is used to build up an attractive interface. One can easily construct or edit one's models with computer graphics playing a central role. VIG was updated in August of 1987, with many desirable features added.

The program has been and is being applied to several practical problems, for instance

(1) The determination of optimal price changes in an alcohol sales monopoly in Finland. [9]

(2) Stockpiling critical materials for a national emergency in Finland.

(3) Managing sewage sludge disposal in the New York Bight. [15]

Our objective is to make the program widely available, and pursue these and other applications.

## References

[1] X.T. Bui, Building Effective Multiple Criteria Decision Support Systems, Systems, Objectives, Solutions 4, Nr. 1 (1984) 3–16.

[2] M. Ginzberg, and E. Stohr, Decision Support Systems: Issues and Perspectives, in: M. Ginzberg, W. Reitman, W., and E. Stohr, eds., Decision Support Systems, (North-Holland Publ. Comp., Amsterdam, 1982).

[3] J.P. Ignizio, Generalized Goal Programming, Computers and Operations Research 10, (1983) 277–289.

[4] M.T. Jelassi, M. Jarke, and E. Stohr, Designing a Generalized Multiple Criteria Decision Support System, Journal of Management Information Systems I, (1985) 24–43.

[5] P.G.W. Keen, and M. Scott-Morton, Decision Support Systems: An Organizational Perspective (Addison Wesley, 1978).

[6] P. Korhonen, and J. Laakso, A Visual Interactive Method for Solving the Multiple Criteria Problem, European Journal of Operational Research 24, Nr. 2 (1986) 277–287.

[7] P. Korhonen, VIG - A Visual Interactive Support System for Multiple Criteria Decision Making, Belgian Journal of Operations Research, Statistics and Computer Science 27, Nr. 1 (1987) 3-15.

[8] P. Korhonen, VIG (A Visual Interactive Approach to Goal Programming) - User's Guide (1987).

[9] P. Korhonen, and M. Soismaa, A Multiple Criteria Model for Pricing Alcoholic Beverages, European Journal of Operational Research 37, Nr. 2 (1988) 165–175.

[10] P. Korhonen, and J. Wallenius, A Pareto Race, Naval Research Logistics 35, Nr. 6 (1988) 615–623.

[11] R.H. Sprague, and E.C. Carlson, Building Effective Decision Support Systems (Prentice-Hall, 1982).

[12] H. Törmä, Pääoman, työn, energian ja raaka-aineiden substituutio Suomen, Ruotsin ja Norjan tehdasteollisuudessa, (in Finnish), Discussion Papers, 233, Research Institute of the Finnish Economy (1987).

[13] H. Törmä, Energian säästömahdollisuuksien tutkiminen lineaarisen monitavoite-optimointimallin avulla, (in Finnish), unpublished manuscript (1987).

[14] K.M. Van Hee, Features of the Architecture of Decision Support Systems, Paper presented at the 12th Symposium

on Operations Research, Gesellschaft für Mathematik, Ökonomie und Operations Research, Universität Passau, September 9–11 (1987).

[15] H. Wallenius, T.M. Leschine, and W. Verdini, Multiple Criteria Decision Methods in Formulating Marine Pollution Policy: A Comparative Investigation, unpublished manuscript (1987).

[16] E.S. Weber, Systems to Think With: A Response to “A Vision for Decision Support Systems”, Journal of Management Information Systems II, (1986) 85–97.

[17] A. Wierzbicki, The Use of Reference Objectives in Multi-objective Optimization, in Multiple Criteria Decision Making, Theory and Application, G. Fandel and T. Gal, Eds., Springer-Verlag, Berlin, (1980) 468–486.

[18] A. Wierzbicki, On the Completeness and Constructiveness of Parametric Characterizations to Vector Optimization Problems, OR-Spectrum 8, (1986) 73–87.
