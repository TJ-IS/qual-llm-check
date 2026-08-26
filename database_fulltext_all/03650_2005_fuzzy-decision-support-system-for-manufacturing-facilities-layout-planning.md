---
otero_id: 3650
otero_key: "Z7S3Z78F"
title: "Fuzzy decision support system for manufacturing facilities layout planning"
authors: "S.K. Deb; B. Bhattacharyya"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.12.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fuzzy decision support system for manufacturing facilities layout planning

S.K. Deb<sup>a,</sup>\*, B. Bhattacharyya<sup>b</sup>

<sup>a</sup> Jorhat Engineering College, Jorhat 785007, India <sup>b</sup> Production Engineering Department, Jadavpur University, Kolkata 700032, India

Received 1 November 2002; accepted 1 December 2003 Available online 28 March 2004

## Abstract

Manufacturing facility layout problem is an unstructured decision-making problem due to natural vagueness associated with the inputs to the models. Arbitrary numerical ratings are assigned for relationship chart to determine facility selection routine. This paper presents a distinct decision support system based on multifactor fuzzy inference system (FIS) for the development of facility layout with fixed pickup/drop-off points. The algorithm searches several candidate points with different orientation of incoming machine blocks in order to minimize flow cost, dead space and area required for the development of layout. The proposed methodology is coded in C<sup>+</sup> language and implemented in a Pentium III, 550-MHz machine. The experimental results with a test problem are illustrated with encouraging result with its advanced soft computational effectiveness.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Facility layout; Fuzzy decision; Flow cost; Dead space; Minimum required area

## 1. Introduction

The most significant objective of any enterprise has been the maximum utilization of facilities available to achieve desired goal of productivity and profitability. Two-dimensional facility layout deals with the selection of most appropriate and effective arrangements of departments in the continuous plane to allow greater working efficiency [2,3]. Owing to the complex and unstructured nature of facility layout, many researchers have proposed various approaches, which had varying degrees of success in dealing with the complexities associated with the problem.

Regardless of the type of data, there is an element of vagueness or fuzziness in it [6]. Traditional layout method treats these data as exact and cannot satisfy the desire of managers in handling real problems [12]. Kawasaki and Evans [9] illustrated the potential application of fuzzy set theory to various areas of production management. One of the prominent areas identified by the authors was facility planning which includes such problem as facilities layout design. Raoot and Rakshit [10] have also presented a framework of an algorithm for the development and evaluation of a layout based on fuzzy linguistic variables and their fuzzy relation. The integrated expert system approach of Abdou and Dutta [1] determines the movement of material-handling equipments first to determine its effect on the layout.

Recently, Dweiri [6] proposed a fuzzy decisionmaking application for developing relationship charts and comparing the layouts generated with them. The concept has been applied to develop layout in the line of computer-relative layout programme that was not efficient as compared to conventional layout procedure. He suggested further research work to improve the procedure or developing a new algorithm for the facility layout design.

The facility layout problems fall in to the class of NP-complete solutions, and heuristic approaches are usually adopted to develop the layout [8]. Most of the models and algorithms available in the literature are based on the quadratic assignment problem with an objective to minimize transportation costs or maximize total closeness rating. The facility selection routine required for the development of layout was solved by considering a single quantitative factor as flow chart. Moreover, the move (distance) traversed is considered from center to center of the departments without considering the practical issue of entry and exit of the departments.

Most of the existing methods have been developed on the grid-based system without considering actual dimensions of departmental block and entry/ exit locations, thus resulting in irregular shapes. Deb et al. [3] have already developed a hybrid modeling for the management of material-handling equipment selection planning while generating a manufacturing facility layout. The authors herein have also proposed different projects of integrating facility layout and material-handling equipment selection by using a knowledge base and optimization approach [5]. They utilized the material flow interaction matrix in finding the facility placement sequence. The authors have already developed a decision model and algorithm for material-handling equipment selection routine under facility layout planning by using fuzzy multi-criteria decision-making methods [4].

Therefore, the present research work follows in the same direction of author’s previous work to integrate various linguistic assessments to evaluate facility selection routine and its impact on the development of facility layout. The applicability of the suggested methodology is demonstrated with a six-machine layout problem considering subjective factors such as supervision, information and environmental condition. The material flows between the different departments are assumed as the objective factor for the development of selection routine. The heuristic search algorithms proposed in this paper take care of optimal placement of incoming facilities based on a multi-criteria optimization function. The performance of the proposed multifactor fuzzy facility selection routine is compared with the multifactor normalized facility selection routine for the development of facility layout under the auspices of a manufacturing environment.

## 2. Fuzzy set and decision-making system

A fuzzy set can be thought of a class of concepts/ objects in which no well-defined boundary exists between the concepts/objects that belong to the class and those which do not belong. Formally, if $B { = } \{ x _ { i } | i \varepsilon N \}$ is a set of objects, then the fuzzy set C on B is defined by its membership function f<sub>C</sub>(x) that assigns to each element x <sub>q</sub>B a real number in the interval [0,1] which represents the grade of membership of x in C or the degree to which x belongs to C. Thus, C can be written as

$$
C = \{(f _ {\mathrm{C}} (x) / x) | x \varepsilon B \}; B \to [ 0, 1 ].
$$

Linguistic variables are words in natural language, while numerical variables use numbers as values. Since words are usually less precise than numbers, linguistic variables provide a method to characterize complex systems that are ill structured to be described in traditional quantitative terms. A linguistic variable is defined by the name of the variable x, and the set term S(x) of the linguistic values of x with each value being a fuzzy number defined on U. For example, if material flow (MF) is a linguistic variable, its term set S(MF)={Very High (VH), High (H), Medium (M), Low (L), Very Low (VL)}, where each term is characterized by a fuzzy set in a universe of discourse U.

A fuzzy decision-making system (FDMS) consists of four main components [14] as shown in Fig. 1. The four components of FDMS are given below:

(i) Fuzzification: In this interface, the different input and output variables are measured and converted into natural language;

(ii) Knowledge base: In this component, the membership functions are decided by the experts based on their knowledge of the system;

(iii) Decision rules: In this interface, the experts decision-making ability is simulated based on a fuzzy concept. The connective ‘and’ is implemented as a fuzzy conjunction in a Cartesian product space in which the input variables take in their respective universe of discourses. The minimum operator is used, and the rules are in the form of IF–THEN statement; and

(iv) Defuzzification: In this interface, the fuzzy outputs are converted into crisp (no fuzzy) values by center-of-area (COA) method.

## 3. Problem formulation and procedure

Facility layout design under a manufacturing environment is mainly based on machine, move and methods. Each machine block can be considered as an individual facility having rectangular shape with proper dimensions of length and width. The rectangular facilities are represented by the top left corner point and bottom right corner point. The ‘move’ is considered as the several interactions associated between the two facilities. The ‘method’ is considered as the material-handling equipments engaged with each move to perform the movement of material from pickup to drop-off point between two facilities to facilitate the production processes. Pickup and dropoff points are assumed to be located at the middle point of edges of the rectangular machine blocks. The generation of model for layout construction is a critical step because of its unstructured and vast nature. The complexity increases further due to multifactor influence on the development of facility selection routine for its sequential placement in the open plane. Out of various types of facility layout environment, very less work has been carried out under the continual planner approach because of its complexity and flexibility in the generation process starting from the center of the plane considering zero base area allocation [3–5]. The inherent difficulties of generating such kind of layout are the generation of dead space. As the layout expands from the center of the continual plane, it is very difficult to predict the possible location for incoming facilities. The formulation of facility layout design problem mainly consists of two modules:

(i) facility selection routine and

(ii) facility placement routine

## 3.1. Facility selection routine

The layout generation depends highly on the sequential facility selection order that in turn directly depends on several quantitative as well as qualitative factors that are very difficult to describe precisely. The input variables assumed for the present problem are level of material flow (MF) as the objective variable and supervision link (SL), job condition or environmental link (EL) and information link (IL) as subjective variables. The multifactor fuzzy inference system (FIS) for the proposed methodology is shown in Fig. 2. The multiple-input, single-output (MISO) fuzzy inference system (FIS) measures the values of the input and output variables, transfers the range of these values into a corresponding universe of discourse and converts them into associated values (very low, low, medium, etc.). The values associated with different linguistic variables used in the formulation of proposed FIS are

![](/api/attachments/Z7S3Z78F/fulltext/images/ce2f155ca9e86a2aa8243e351a37c0c2f6151313b49b9730bd0d2004810791da.jpg)  
Fig. 1. Fuzzy decision support system configuration.

![](/api/attachments/Z7S3Z78F/fulltext/images/09de765186b903bb74a59206e7587e5fd1f3969948afc0c3174e6650ac8686dd.jpg)  
Fig. 2. Multifactor fuzzy inference system for facility layout.

$$
f (x) = 1 - x \quad 0 \leq x \leq 1. 0
$$

U : ð0; 1:0; 1:0; 2:0Þ

(i) material flow (very high, high, medium, low, very low),

(ii) supervision link (negligible, considerable, moderate, essential, very essential),

$$
f (x) = \left\{ \begin{array}{l l} x & 0 \leq x \leq 1. 0 \\ 2 - x & 1. 0 \leq x \leq 2. 0 \end{array} \right.
$$

(iii) environmental link (very safe, safe, unsafe, hazardous, very hazardous), and

O: ð1:0; 2:0; 2:0; 3:0Þ

(iv) information link (very strong, strong, medium, weak, very weak).

$$
f (x) = \left\{ \begin{array}{l l} x - 1 & 1. 0 \leq x \leq 2. 0 \\ 3 - x & 2. 0 \leq x \leq 3. 0 \end{array} \right.
$$

The crisp output of the FIS measures the rating with standard associated values usually in practice [2,12] under facility layout planning X, U, O, I, E and Awithin the universe of discourse [0,6]. The universe of discourse and set of the grades of membership were developed within the existing knowledge and experience of facility layout designers using the subjective approach, which is in line with the view of Zadeh [13], who indicated that the grade of membership are subjective, in the sense that their specification is a matter of definition rather than experimentation. The shape of the membership function reflects the expert’s knowledge, experience and preference regarding the importance of different relationships (‘sharp’ slope for important relationship and ‘flat’ slope for less important relationships). The membership function of each linguistic value in the crisp output rating set $R { = } [ X , U , O , I , E , A ]$ is shown in the following expressions:

I : ð2:0; 3:0; 3:0; 4:0Þ

$$
f (x) = \left\{ \begin{array}{l l} x - 2 & 2. 0 \leq x \leq 3. 0 \\ 4 - x & 3. 0 \leq x \leq 4. 0 \end{array} \right.
$$

E: ð3:0; 4:0; 4:0; 5:0Þ

$$
f (x) = \left\{ \begin{array}{l l} x - 3 & 3. 0 \leq x \leq 4. 0 \\ 5 - x & 4. 0 \leq x \leq 5. 0 \end{array} \right.
$$

A: ð4:0; 5:0; 5:0; 6:0Þ

$$
f (x) = \left\{ \begin{array}{l l} x - 4 & 4. 0 \leq x \leq 5. 0 \\ 6 - x & 5. 0 \leq x \leq 6. 0 \end{array} \right.
$$

X : ð0; 0; 0; 0; 1:0Þ

In decision rules module, the expert’s decisionmaking ability is simulated based on a fuzzy concept. The entire knowledge of the decision maker is stored as rules in the knowledge base of the FIS. The development of rules may be time consuming. An intuitively developed strategy for finding the rating of each move based on the values of their relationships can be summarized as follows:

(i) If the material flow (MF) relationship between two facilities is very high, then they should be located very close to each other, i.e., rating given is $^ { \circ } A ^ { \prime }$

(ii) If the supervision link (SL) between two facilities is very high, then they should be located very close to each other, i.e., rating given is $\cdot _ { A } ,$

(iii) If the environmental link (EL) between two departments is very hazardous, then they should be located very far to each other, i.e., rating given is $^ { \circ } U ^ { \prime }$

(iv) If the information flow (IF) between two facilities is very strong, then they should be located very close to each other, i.e., rating given is ‘A’.

The mapping of the inputs to the outputs for a fuzzy system is in part characterized by a set of condition ! action rules in the form of IF–THEN. The connective ‘and’ is implemented as a fuzzy conjunction in a Cartesian product space in which the input variables take on their respective universe of discourses. For this study, the [minimum] operator will be used. The membership value of the control action of each rule is the minimum value of the input variables’ membership values. In this paper, multiinput, single-output (MISO) is considered under heuristic design rules in the following form:

IF ðMFÞ is ðVHÞ and ðIFÞ is ðVHÞ

and 	 	 	 THEN rating is ðAÞ:

IF ðMFÞ is ðHÞ and ðELÞ is ðhazardousÞ

and 	 	 	 THEN rating is ðUÞ:

The values of linguistic variables are considered within a designed weighing scale [0, 10] with levels [VL, L, M, H, VH], and the values of the output rating are designed within a weighing scale [0,6] with generally accepted levels $[ X , U , O , I , E , A ]$ . The triangular membership function is considered for objective variable material flow and rating score. The subjective variables supervision link, information link and environmental link are considered as trapezoidal membership functions. The number of rules (N) used in controlling the system using fuzzy control is represented by:

$$
N = \sum_ {j = 1} ^ {m} \left(\prod_ {i = 1} ^ {n} L _ {i}\right)
$$

where, m = number of set of rules, L<sub>i</sub> = number of membership functions or levels, N = number of input variables used in one set of rules. When m = 1, n = 4 and $L _ { i } = 5 ,$ , then number of rules (N) becomes: $5 \times 5 \times 5 \times 5 = 6 2 5$

The following steps are established to find the selection routine of facilities in an open field:

1. Prepare the input values for all moves (activities). The total activities are $n \times ( n - 1 )$ , where n is number of departments.

2. Find the minimum values of the input variables’ membership values using minimum operator for every activity.

3. Scan the heuristic design rules for all the moves, and find the crisp output of the rating $( R _ { i j } ^ { \mathrm { c } } )$ by using center-of-area (COA) method.

4. Determine the fuzzy rating matrix as $R _ { n ^ { * } n } =$ $[ R _ { i j } ^ { \mathrm { c } } ] \forall i , j = 1 , 2 \ \dots \ n$ and $R _ { i j } ^ { \mathrm { c } } { = } 0$ for $i { = } j .$

5. Calculate the total fuzzy rating of the ith department with the other departments and find the maximum value $( F _ { k } )$ to select the first facility as department $\cdot _ { k } ,$

$$
F _ {i} = \sum_ {j} (R _ {i j} ^ {\mathrm{c}} + R _ {j i} ^ {\mathrm{c}}) \forall i, j = 1, 2 \dots n.
$$

$$
F _ {k} = \max \left\{F _ {i} \right\} \forall i = 1, 2 \dots n.
$$

6. Next, find the department that has maximum fuzzy rating value with the facility already included in the selection routine.

7. Repeat step 6 until all facilities are included in the selection routine.

## 3.2. Facility placement routine

Heuristic is deterministic and hence suboptimal. Not that this is a bad thing. The generalized QAP facility layout formulation is NP complete. Indeed, the heuristic is novel and provides an interesting approach to the classical facility layout problem. Most of the earlier approaches used the concept of area under rectangular grid system and the distance from centroid to centroid of the blocks. The methods could not address the development of real layout, which are characterized by dimension of length and width, pickup/drop-off points (P/D), orientation of blocks for making P/D closer in the passage. An incoming facility is placed at a point called a candidate point on the periphery of the already placed block, and its optimality is tested under various placement styles in order to minimize the value of objective function. Generally, three styles of placements are considered around a candidate point. It may be either left or right of candidate point or on the middle of the candidate point. Blocks must be placed either horizontally or vertically within designated site area without overlapping. The commonly used objective function in the facility layout is the minimization of the sum of material-handling cost (MHC), i.e.,

$$
\text { Minimize   MHC } = \sum \sum c _ {i j} \times f _ {i j} \times d _ {i j}
$$

where $c _ { i j } =$ material-handling cost coefficient involved between machine i and $j , f _ { i j } { = } \mathrm { m a t e r i a l }$ flow volume and $d _ { i j } =$ the distance between machines i and $j .$

The decision variables of the objective function are coordinates of the rectangular block, pickup/drop-off points. The move is measured between the pickup and drop-off points of the machine blocks. The first block is placed at the center of the plane continuum horizontally. To solve the problem of nonoverlapping criteria, several possible alternatives of machine block placements are tested at the candidate point on each edge. The incoming blocks may be placed horizontally (H) or vertically (V) resulting in six possible arrangements denoted by HL, VL, HM, VM, HR and VR. These six possible arrangements are given $1 8 0 ^ { \circ }$ rotation to change the fixed pickup/drop-off points that are on the edges of the machine blocks. Thus, it allows 12 search space per candidate point. The ‘HL’ arrangement under $1 8 0 ^ { \circ }$ rotation is denoted by HLR. Similarly, the remaining rotations are shown in Fig. 3. Heuristic search is carried out through all candidate points on the four edges of the already placed blocks to fulfill the nonoverlapping condition and to locate the incoming blocks at minimum value of the bicriterion objective function (see Appendix A) with two parts as flow cost and dead space. The heuristic optimization is carried out under the consideration of

Table 1  
Data table for machine configuration

<table><tr><td>Machines</td><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td><td>M6</td></tr><tr><td>Length (in m)</td><td>60</td><td>30</td><td>120</td><td>48</td><td>72</td><td>54</td></tr><tr><td>Width (in m)</td><td>30</td><td>30</td><td>30</td><td>36</td><td>24</td><td>36</td></tr><tr><td>Pickup</td><td>0,15</td><td>0,15</td><td>60,0</td><td>24,0</td><td>0,12</td><td>27,0</td></tr><tr><td>Drop-off</td><td>60,15</td><td>30,15</td><td>60,30</td><td>24,0</td><td>36,0</td><td>0,18</td></tr></table>

![](/api/attachments/Z7S3Z78F/fulltext/images/167565a5f7683f12b3d90a8a699e245a66f77caedbb6e322dbcca2b08cea3f27.jpg)  
(HM=Horizontal Middle, VM=Vertical Middle, HMR=Horizontal Middle Rotation, HR=Horizontal Right. HL=Horizontal Left, HRR=Horizontal Right Rotation etc, 1C1-1C12 is 12 possibilities of placement routines at the first candidate point.).  
Fig. 3. Different configurations and orientations of incoming rectangular blocks.

Table 2  
Fuzzy system input data and output rating

<table><tr><td>Move number</td><td>MF</td><td>SL</td><td>EL</td><td>IL</td><td> $R_{ij}^{c}$ </td><td> $R_{ij}^{n}$ </td></tr><tr><td>1-2</td><td>1</td><td>5</td><td>9</td><td>10</td><td>3.00</td><td>0.20</td></tr><tr><td>2-1</td><td>5</td><td>8</td><td>2</td><td>2</td><td>3.00</td><td>0.18</td></tr><tr><td>1-3</td><td>2</td><td>3</td><td>8</td><td>5</td><td>1.00</td><td>0.15</td></tr><tr><td>3-1</td><td>2</td><td>2</td><td>7</td><td>6</td><td>1.99</td><td>0.15</td></tr><tr><td>1-4</td><td>1</td><td>1</td><td>6</td><td>8</td><td>1.00</td><td>0.13</td></tr><tr><td>4-1</td><td>4</td><td>6</td><td>1</td><td>9</td><td>3.00</td><td>0.19</td></tr><tr><td>1-5</td><td>2</td><td>8</td><td>5</td><td>2</td><td>3.00</td><td>0.15</td></tr><tr><td>5-1</td><td>1</td><td>3</td><td>4</td><td>5</td><td>1.99</td><td>0.11</td></tr><tr><td>1-6</td><td>3</td><td>5</td><td>2</td><td>8</td><td>3.00</td><td>0.16</td></tr><tr><td>6-1</td><td>0</td><td>7</td><td>3</td><td>6</td><td>3.00</td><td>0.12</td></tr><tr><td>2-3</td><td>1</td><td>2</td><td>5</td><td>7</td><td>1.99</td><td>0.17</td></tr><tr><td>3-2</td><td>3</td><td>2</td><td>6</td><td>8</td><td>1.99</td><td>0.21</td></tr><tr><td>2-4</td><td>2</td><td>9</td><td>9</td><td>5</td><td>3.00</td><td>0.01</td></tr><tr><td>4-2</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1.04</td><td>0.05</td></tr><tr><td>2-5</td><td>1</td><td>2</td><td>1</td><td>2</td><td>1.09</td><td>0.11</td></tr><tr><td>5-2</td><td>2</td><td>3</td><td>4</td><td>3</td><td>1.99</td><td>0.17</td></tr><tr><td>2-6</td><td>2</td><td>4</td><td>6</td><td>9</td><td>3.00</td><td>0.15</td></tr><tr><td>6-2</td><td>2</td><td>6</td><td>5</td><td>4</td><td>3.00</td><td>0.16</td></tr><tr><td>3-4</td><td>3</td><td>8</td><td>3</td><td>3</td><td>3.00</td><td>0.15</td></tr><tr><td>4-3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1.04</td><td>00</td></tr><tr><td>3-5</td><td>2</td><td>1</td><td>5</td><td>6</td><td>1.99</td><td>0.12</td></tr><tr><td>5-3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1.04</td><td>00</td></tr><tr><td>3-6</td><td>1</td><td>1</td><td>2</td><td>2</td><td>1.99</td><td>0.11</td></tr><tr><td>6-3</td><td>0</td><td>2</td><td>0</td><td>0</td><td>3.00</td><td>0.07</td></tr><tr><td>4-5</td><td>1</td><td>1</td><td>1</td><td>5</td><td>1.00</td><td>0.28</td></tr><tr><td>5-4</td><td>5</td><td>8</td><td>9</td><td>9</td><td>3.00</td><td>0.13</td></tr><tr><td>4-6</td><td>2</td><td>5</td><td>6</td><td>1</td><td>3.00</td><td>0.20</td></tr><tr><td>6-4</td><td>2</td><td>8</td><td>8</td><td>6</td><td>3.00</td><td>0.20</td></tr><tr><td>5-6</td><td>1</td><td>3</td><td>5</td><td>4</td><td>1.99</td><td>0.11</td></tr><tr><td>6-5</td><td>10</td><td>9</td><td>7</td><td>3</td><td>1.99</td><td>0.16</td></tr></table>

MF = material flow, SL = supervision link, EL = environmental link, IL = information link.

unit flow cost coefficient $( \mathrm { i } . \mathrm { e } . , c _ { i j } = 1 )$ and unit penalty cost coefficient for the dead space (i.e., $P _ { \mathrm { c } } { = } 1 )$ . The penalty cost coefficient is defined as the cost of dead space per unit area that is considered as a parameter, which varies from place to place.

Table 3  
Fuzzy crisp activity relation matrix

<table><tr><td>Machines</td><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td><td>M6</td></tr><tr><td>M1</td><td>-</td><td>3.00</td><td>1.00</td><td>1.00</td><td>3.00</td><td>3.00</td></tr><tr><td>M2</td><td>3.00</td><td>-</td><td>1.99</td><td>3.00</td><td>1.09</td><td>3.00</td></tr><tr><td>M3</td><td>1.99</td><td>1.99</td><td>-</td><td>3.00</td><td>1.99</td><td>1.99</td></tr><tr><td>M4</td><td>3.00</td><td>1.04</td><td>1.04</td><td>-</td><td>1.00</td><td>3.00</td></tr><tr><td>M5</td><td>1.99</td><td>1.99</td><td>1.04</td><td>3.00</td><td>-</td><td>1.99</td></tr><tr><td>M6</td><td>3.00</td><td>3.00</td><td>3.00</td><td>3.00</td><td>1.99</td><td>-</td></tr></table>

Table 4  
Multifactor-normalized relation matrix

<table><tr><td>Machines</td><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td><td>M6</td></tr><tr><td>M1</td><td>-</td><td>0.20</td><td>0.16</td><td>0.13</td><td>0.16</td><td>0.16</td></tr><tr><td>M2</td><td>0.18</td><td>-</td><td>0.17</td><td>0.01</td><td>0.11</td><td>0.16</td></tr><tr><td>M3</td><td>0.16</td><td>0.21</td><td>-</td><td>0.15</td><td>0.12</td><td>0.11</td></tr><tr><td>M4</td><td>0.19</td><td>0.05</td><td>00</td><td>-</td><td>0.38</td><td>0.20</td></tr><tr><td>M5</td><td>0.11</td><td>0.17</td><td>00</td><td>0.13</td><td>-</td><td>0.11</td></tr><tr><td>M6</td><td>0.12</td><td>0.16</td><td>0.07</td><td>0.20</td><td>0.16</td><td>-</td></tr></table>

3.3. Steps of algorithm for facility placement routine

1. Find the facility selection routine applying multifactor FIS.

2. Locate the first block at the center of the open plane horizontally.

3. Select the next block for placement according to placement routine of facilities.

4. Select the candidate point, and check the feasible quarter. If not feasible, go to step 7, else go to next step.

5. Locate the block according to placement possibil ities, and check for nonoverlapping. If not satisfied, repeat next possible placement as explained in Section 4, else go to step 6.

6. Calculate the value of objective function, if it is better than previous update configuration and objective function value. Go to step 5 for searching other possibilities at the candidate point.

7. Select next candidate point. If all candidate points of the selected block are already considered, go to step 8; otherwise, go to step 4.

8. Select the next block. If all blocks are selected, go to step 9, else go to step 3.

![](/api/attachments/Z7S3Z78F/fulltext/images/ab4342318c10430f5ee30774f288fbb0859e14134f4208f82e77a5a1fbdf37d7.jpg)  
Fig. 4. Membership function for material flow.

![](/api/attachments/Z7S3Z78F/fulltext/images/667b87c8fae39439ae64ff9c62cf5760346678c41e49bce774f926c9a618d07b.jpg)  
Fig. 5. Membership function for supervision link.

9. Locate the block, which provides the best value of objective function.

## 4. Experimentation and results

The experimentation was carried out in order to investigate the applicability and effectiveness of the proposed methodology based on multifactor fuzzy inference system, and the results have been compared with the facility selection routine developed as an extension of the multifactor plant layout methodology by Harmonosky and Tothero [7]. The algorithm was coded in $\dot { \mathrm { C } } ^ { + }$ language, and the problem was run on an IBM Pentium III, 550-MHz machine. The data table related to machine dimensions, P/D locations and move characteristics used for computer simulation having six machines, 30 moves under the consideration of four influencing factors are taken from earlier research work [3–5] and listed in Tables 1 and 2. The values of subjective variables supervision link (SL), information link (IL), environment link (EL) and objective variable material flow (MF) are taken arbitrarily within designed weighing scale [0,10]. The values of crisp output rating $( R _ { i j } ^ { \mathrm { c } } )$

![](/api/attachments/Z7S3Z78F/fulltext/images/9894891c1836190f4467ffcbeacbd37f0d4ceda3881b25577db294267fc91fab.jpg)  
Fig. 6. Membership function for output variable score.

Table 5  
Experimental results using fuzzy and normalized approach

<table><tr><td>Facility layout selection routine</td><td>Methods applied</td><td>Flow cost (T-m)</td><td>Minimum required area of layout</td><td>Dead space ( $m^{2}$ )</td><td>Value of fuzzy score</td></tr><tr><td>1-2-6-4-5-3</td><td>(A) Multifactor normalized</td><td>2998</td><td>17280</td><td>7580</td><td>7.14</td></tr><tr><td>6-4-2-1-5-3</td><td>(B) Multifactor fuzzy method</td><td>3015</td><td>17199</td><td>5499</td><td>7.32</td></tr></table>

obtained by applying the proposed methodology and normalized rating obtained by applying the methodology of Harmonosky and Tothero [7] for each move are presented in Table 2. The fuzzy activity relation matrix and normalized activity relation matrix are shown in Tables 3 and 4 respectively. Membership functions of material flow, supervision link and score are shown in Figs. 3– 5. A triangular membership function is considered for the material flow and score (Fig. 6). For other variables, trapezoidal membership functions are considered. The values of material flow cost, minimum required area and dead space for different selection routine are presented in Table 5. Figs. 7 and 8 show the layouts developed by using the proposed algorithm under multifactor fuzzy inference system and multifactor normalized selection routine as discussed in Section 3. The values of FC, DS and MRAL are converted to fuzzy score and its value for the six-machine layout problem is shown in Table 5.

![](/api/attachments/Z7S3Z78F/fulltext/images/addbf4c21d77ef8883bcfc3c9fb57b430f55864de60483a0e9b267c9e460fe0e.jpg)  
Fig. 7. Layout based on multifactor fuzzy selection routine.

![](/api/attachments/Z7S3Z78F/fulltext/images/bf4f4b2695cad9d74f8d95178b52d3b253b4bb8cdad69b3eeae2bee29067ee27.jpg)  
Fig. 8. Layout based on multifactor-normalized selection routine.

## 5. Conclusions

The fuzzy decision support system presented in this paper is an effective way to handle inexact and vague data. However, it is yet to work on the problem in a mathematically strict and rigorous way. The experimental results obtained from the computer simulation illustrate that the proposed methodology has been very effective in reducing MRAL and DS, while developing green-field layouts. The value of flow cost obtained by using the proposed approach is slightly higher than the layout developed with the selection routine based on multifactor-normalized method. The slightly higher value of flow cost is comparable to the fuzzy decision-making method under the present consideration of developing green-field layouts where MRAL and DS are considered very important evaluating parameters. Applying the fuzzy scoring methodology typically yields higher scores for the multifactor fuzzy approach.

The firm can save initial investment costs by adopting the proposed facility layout methodology. The methodology presented in this paper is simple and can easily be implemented on a personal computer.

## 6. Future research

The present work simply demonstrates the potential applicability of fuzzy set theory and offers a systematic guidance to the decision makers in planning manufacturing facilities layout under fuzzy environment. This research can be directed towards finding a scientific method for determining the values of the subjective variables—supervision link (SL), information link (IL), environmental link (EL) and the objective variable-material flow (MF), by applying Satty’s analytical hierarchy process [11], which are chosen arbitrarily here.

## Appendix A. Objective function for placement routine

## A.1 . Minimization of material flow cost

$$
\begin{array}{c} \text {Minimize} Z _ {j} ^ {1} = (c _ {i j} \times f _ {i j} (| x _ {j} ^ {p} - x _ {i} ^ {d} | + | y _ {j} ^ {p} - y _ {i} ^ {d} |) + \\ c _ {j i} \times f _ {i j} (| x _ {i} ^ {p} - x _ {j} ^ {d} | + | y _ {i} ^ {p} - y _ {j} ^ {d} |)) \forall j = 2, 3, \ldots n. \end{array}
$$

## A.2. Minimization of dead space

$$
\begin{array}{l} \text {Minimize} Z _ {j} ^ {2} = P _ {\mathrm{c}} \times [ (x _ {b} ^ {j} - x _ {t} ^ {j}) \times (y _ {b} ^ {j} - y _ {t}) \\ \qquad - \sum_ {i = 1} ^ {j} l _ {i} \times w _ {i} ] \forall j = 2, 3, \ldots n. \end{array}
$$

where $x _ { b } ^ { j } = \operatorname { M a x } \{ x _ { b i } \} \forall i = 1 , 2 , . . . n ; x _ { t } ^ { j } = \operatorname { M a x } \{ x _ { t i } \}$ $\forall i = 1 , 2 , ~ \ldots ~ n ; ~ y _ { b } ^ { j } = \operatorname { M a x } \{ y _ { b i } \} \forall i = 1 , 2 , ~ \ldots ~ n ; ~ y _ { t } ^ { j } =$ Max $\{ y _ { t i } \} \forall i = 1 , 2 , . . . \ n ; l _ { i }$ and $w _ { i }$ are the length and width of the ith rectangular machine block; $\textstyle \sum _ { i = 1 } ^ { j } l _ { i } \times$ $w _ { i }$ is the sum of all the machine blocks.

## A.3. Minimization of flow cost and dead space

$$
\text { Minimize } Z _ {j} = w _ {1} \times Z _ {j} ^ {1} + w _ {2} \times Z _ {j} ^ {2}
$$

where $w _ { 1 }$ and $w _ { 2 }$ are weights of FC and $\mathrm { D S } ; ( x _ { i } ^ { \mathrm { p } } , y _ { i } ^ { \mathrm { p } } )$ is the input coordinate of ith department; $( x _ { i } ^ { \mathrm { d } } , y _ { i } ^ { \mathrm { d } } )$ is the exit coordinate of the ith department; $( x _ { j } ^ { \mathrm { p } } , y _ { j } ^ { \mathrm { p } } )$ is the input coordinate of the jth department; $( \bar { x } _ { j } ^ { \mathrm { d } } , \bar { y } _ { j } ^ { \mathrm { d } } )$ is the exit coordinate of the jth department; $f _ { i j }$ and $f _ { j i }$ are the material flow between departments $i \mathrm { - } j$ and $j - i ; c _ { i j }$ and $c _ { j i }$ are the flow cost coefficients between moves $i - j$ and $j - i ; P _ { \mathrm { c } }$ is the penalty cost coefficients for dead space.

## References

[1] G. Abdou, S.P. Dutta, An integrated approach to facilities layout design using expert system, International Journal of Production Research 28 (1990) 685–708.

[2] J.M. Apple, Plant Layout and Material Handling, Wiley, New York, 1977.

[3] S.K. Deb, B. Bhattacharyya, S.K. Sorkhel, Management of machine layout and material handling system selection using hybrid approach, 1st International Conference on Logistic and Supply Chain Management, PSG Tech, India, 2001.

[4] S.K. Deb, B. Bhattacharyya, S.K. Sorkhel, Material Handling Equipment Selection by Fuzzy Multi-Criteria Decision Making Methods. Lecture Notes in Artificial Intelligence, Springer-Verlag, Berlin, 2002.

[5] S.K. Deb, B. Bhattacharyya, S.K. Sorkhel, Facility layout and material handling equipment selection planning using hybrid methodology, International Journal of Industrial Engineering 10 (3) (2003 September) 436 – 443.

[6] F. Dweiri, Fuzzy development of crisp activity relationship charts for facilities layout, Computer and Industrial Engineering 36 (1999) 1 – 16.

[7] C.M. Harmonosky, K. Tothero, Multi factors plant layout methodology, International Journal of Production Research 30 (1992) 1773–1789.

[8] S.S. Heragu, A. Kusiak, Machine layout: an optimization and knowledge-based approach, International Journal of Produc tion Research 28 (1990) 615– 635.

[9] W. Kawasaki, G.W. Evans, A layout design heuristic employing theory of fuzzy set, International Journal of Production Research 25 (1987) 1431– 1450.

[10] A. Raoot, A. Rakshit, A linguistic pattern approach for multiple criteria facility layout problems, International Journal of Production Research 31 (1993) 203– 222.

[11] T.L. Saaty, The Analytical Hierarchy Process, McGraw-Hill, New York, 1980.

[12] J.A. Tompkins, J.A. White, Facilities Planning, Wiley, New York, 1984.

[13] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338– 553.

[14] H.J. Zimmermann, Fuzzy Sets. Decision Making and Expert Systems, Kluwer Academic Publishing, Boston, 1987.

![](/api/attachments/Z7S3Z78F/fulltext/images/33d95c4efc229ca70ff218be9b90af921cfd5be25f259826e401697e470a12b0.jpg)

S.K. Deb is assistant professor of the Mechanical Engineering Department, Jorhat Engineering College, Jorhat-7, India. He secured his MTech and MBA degree from IIT, Kharagpur and Gauhati University, respectively. Recently, he has obtained his PhD (Engg) from Jadavpur University, Kolkata, India. The author has teaching and research experience of about 18 years. His area of specialization is Facility Layout Planning and Operations

Management. He has published several research papers in national and international journals.

![](/api/attachments/Z7S3Z78F/fulltext/images/159638d5089fe5ff4dcf0797c2cea86ee0ef280410be7208344de7136340c18f.jpg)

B. Bhattacharyya is professor and former head of the Production Engineering Department, Jadavpur University, Kolkata, India. He did his MProd (Engg) and PhD (Engg) from Jadavpur University, Kolkata. At present, he is the coordinator of Center of Advanced Studies (CAS) and Quality Improvement Program (QIP) of Jadavpur University. His area of specialization is non-traditional manufacturing and production manage-

ment. He has published about 50 research papers in international and national journals.
