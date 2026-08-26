---
otero_id: 18179
otero_key: "3BRZ2RDD"
title: "Distributed computer system design: An interactive procedure"
authors: "Hemant K. Jain"
year: "1985"
journal: "Information & Management"
doi: "10.1016/0378-7206(85)90051-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distributed Computer System Design: An Interactive Procedure

Hemant K. Jain

School of Business Administration, University of Wisconsin-Milwaukee, P.O. Box 742, Milwaukee, WI 53201, USA

This paper presents an overview of an interactive system for the design of a distributed computer system. The system helps the designer in finding the optimal combination of processors of varying power to be located at various nodes of the system. It also helps in finding the optimal allocation of data files or databases. The system allows the designer to trade-off between the conflicting objectives: low investment and operating cost and high availability of data. Reasonable relative weights are assigned to each data file, and design objectives can be assigned priorities. A value added network such as TELENET is assumed for data communication. Also, multiple copies of the data file or database may exist in the system to achieve higher data availability and better response time.

Keywords: Distributed Processing System Design, Interactive System, File Allocation, Computer Selection, Multicriteria Decision Making.

![](/api/attachments/3BRZ2RDD/fulltext/images/d5bf85c5acd6a1992440b39fd5e0e24419b28f5c0fcd06c4eacd12f493470191.jpg)

Hemant K. Jain is assistant professor of Management Information Systems in the School of Business Administration at the University of Wisconsin-Milwaukee. He also held faculty positions in the Department of Industrial Engineering and Operations Research at Syracuse University, and at the National Institute For Training In Industrial Engineering (NITIE), Bombay. His research interests lie in the area of Distributed Computer Systems, Computer Networking, Design

of centralized and distributed databases, Decision Support System, Expert System and CAD/CAM.

He received his B.S. in Mechanical Engineering from University of Indore (India) in 1973, a M. Tech. in Industrial Engineering from I.I.T. Kharagpur (India) in 1975 and Ph.D. in Industrial Engineering from Lehigh University, Bethlehem PA. in 1981. He is a member of ACM, IEEE Computer Society and TIMS.

## 1. Introduction

The decreasing cost of computers and advances in data communication and computer networking technology is increasing the use of distributed computer systems in many areas of business, government, and academia. The laws governing the economies of scale in computers are complicated due to the availability of micro, mini, and super computers. Prior to these developments, a commonly accepted rule was Grosch's law [8], which postulated that “the costs of computer systems increase at a rate equivalent to the square root of their power.” These economies of scale in computing led to centralization. Now the processing cost per machine instruction is less on micro computers than on a large mainframe. The reason is related to the use of VLSI circuits, which can be mass-produced. The development cycle of micro and minicomputer is much shorter than that of large machines; therefore they tend to have later technology which is less expensive. This situation is likely to change in the future.

In comparing the cost of processing a transaction, software also plays an important role. When a transaction is processed on a computer system, in addition to the instructions in the application programs, a large number of operating system and utility program instructions are executed. The total number of machine instructions executed for a transaction is referred to as the software path length. A typical micro computer has low software overhead because of its simple operating system and utility programs; its software path length is often less than one thousand. A mainframe with a virtual operating system supporting multi-tasking and large numbers of concurrent users, database, and data communication facilities, has a software path length which is often greater than one or two hundred thousand.

Thus, for mainframe computers the cost of processing a machine instruction is higher and the number of machine instructions executed per transaction can be a hundred times greater than in a micro computer. However, micro computers have a much simpler instruction set and differ from mainframe computers in terms of architecture, speed, multitable memory capacity, richness of storage and peripherals. Also the complex and general purpose software of mainframe has many benefits, in terms of their capability to process a complex application. In early 70's the Reduced Instruction Set Computer (RISC) experiments at IBM showed that in a typical commercial system a large percentage of transactions require only a simple instruction set [18]. Also the complex software of mainframe computers supporting multitasking, large number of concurrent users, database and data communication facilities may not be necessary for many simple day-to-day transactions.

In a recent study Ein-Dor [7] concluded that “it is most effective to accomplish any task on the least powerful type of computer capable of performing it.” For analytical purposes computers were divided into five classes: micro computers, mini computers, small mainframes, mainframes and super computers. Ein-Dor also concluded that Grosch’s law holds within each class; therefore, it is advantageous to use the most powerful computer within the appropriate class. Thus in many instances the optimal solution will be an integration of computers of varying power. The problem of finding this optimal integration is addressed here.

Because of advances in data communication and computer networking technology, it is now possible to have mini or micro computers at end user locations performing most of the simple routine transactions (short path length), while more complex transactions can be sent to large mainframes. Thus, a distributed system can have a variety of computers at geographically separate locations connected by data communication channels to share data and processing resources. These systems are well suited to environments where large portions of the data are either used by the location which generates that data or by locations which are geographically close to the generating location. Many large to medium-sized organizations, such as banks, insurance companies, realtors and government agencies, as well as large multidivisional firms with geographically dispersed plants, warehouses, and sales branches satisfy these criteria.

The problem of designing a distributed system is complex. Apart from the processing cost many other factors, such as: communication cost, organization control and security, need to be considered in the design. Allocation of data files or databases will affect these factors to a large extent. The designer may find that objectives such as low investment and operating cost, rapid access to data, high availability of data, and security and control considerations are in conflict. A trade-off between these objectives is required. Because of the need for such complex decisions, many systems are not designed to realize the full potential of the distributed system concept. Choosing proper alternatives without computational aid is extremely difficult.

Since the design problem in its entirety is quite complex, it is not surprising that attempts have been made to study particular aspects of this problem in isolation. Mitrani and Sevick [16] and Buhr [2] address the problem of selecting the optimal speed of processors. Several studies have developed methods to minimize some measure of system cost as a function of database file locations [3,5,14,17]. Another class of models has been developed for the design of communication network topology and allocation of data files [10,13]. Dutta and Jain [6] address the combined problems of processor selection, file allocation, and network design. Gavish and Hasan [9] address the problems of file allocation and processor selection and location. Most of the above models fail to consider the differences in the cost of processing a transaction on different classes of computers. Also, most of the models are not in an interactive form that can be used as a decision aid.

In many organizations using a distributed system, the volume of data transmission over long distances is not large enough to warrant the design of a private network. It is economical for them to use the services of a value-added network such as TELENET, TYMNET, or TRANSPAC. Thus, the designer of such a distributed system at a global level needs to address only the problems of selecting a class of computer, its processing speed, primary and secondary storage required for each location, and allocation of data files or databases.

## 2. Distributed System Design Problem

Figure 1 shows the typical structure of a distributed system considered here. The location of nodes in the network is assumed to be given and a value-added communication network is used to implement the system. Each job arriving at a node requires processing and/or some data from a local or remote file. A job can also generate update transactions for remote or local data files.

Based on the architecture, speed, multitable memory capacity, and the richness of storage, peripherals and instruction set computers can be divided into five classes: micro computers, mini computers, small mainframes, large mainframes, and super computers. For the purpose of analysis, jobs can also be divided into five classes based on the power of hardware and software required to process it. A job is locally processed at a node if its class is less than or equal to the class of processor located at that node; otherwise it is sent to a remote node capable of processing it. For the initial global design of the system it can be assumed that all the remote nodes having processors capable of processing the job have equal probability of receiving it. The following input parameters and decision variables are used in the model. The interactive system provides a systematic way of specifying and changing values of these parameters.

## 2.1. Input Parameters

S: Set of all network nodes (s represents an individual node).

K: Set of all data files (k represents an individual data file).

M: Set of all classes of processor available (m represents an individual class of processor).

$\mathrm{RELI}_m$ : Reliability of processors in class $m$ .

$V_{k}$ : Size of file k in kilobytes.

$\lambda_{s}$ : The arrival rate of jobs at node s.

![](/api/attachments/3BRZ2RDD/fulltext/images/be6cd7924740ea294a369785d5c3dcfb657c9cb6526b8a062d2253ac4e5fc5a6.jpg)  
Fig. 1. A Typical Distributed System.

$b_{s,r}$ : The probability that job arriving at node s is of class r.

$q_{rk}$ : The probability that job of class r will result in updating file k.

$p_{rk}$ : The probability that job of class $r$ will query file $k$ .

$o_{rk}$ : The average length of data transmission required to update a copy of file k by a job of class r.

$t_{rk}$ : The average length of data transmission required to satisfy a query from file k by a job of class r.

$g_{r}$ : The average length of jobs in class r (in terms of number of transactions).

$e_{r}$ : The average primary storage required for jobs in class r.

$b_{sr}^{\prime}$ : The expected number of jobs of class r processed at node s. It can be calculated from above parameter values.

## 2.2. Decision Variables

The essential decisions to be made by the designer of a distributed system at the global design stage are: (a) class of processor for each node, (b) processing power, and primary and secondary storage capacity required at each node, (c) location of data files in the network. The following variables are used in the model to represent these decisions:

$$
d _ {m s} = \left\{ \begin{array}{l l} 1 & \text { If   computer   of   class } m \\ & \text { is   assigned   to   site } s \\ 0 & \text { Otherwise } \end{array} \right.
$$

$Z_{s}$ = Speed of processor at node $s$ in millions of instructions per second

$M1_{s}$ = Primary storage capacity required at node s in kilobytes

$H_{s}$ = Secondary storage capacity required at node s in kilobytes

$$
X _ {s k} = \left\{ \begin{array}{l l} 1 & \text {   If   } k \text {-th   data   file   is   located   at   node   } s. \\ 0 & \text {   Otherwise   } \end{array} \right.
$$

It is assumed that multiple processors of a class can be used to satisfy the throughput requirement at the node. Also, to keep the problem tractable, it is assumed that the processors of a single class are located at a node. The model is currently being extended to allow for multiple classes of processors at a node.

## 2.3. Objective Functions

The design of distributed system involves compromises among several different and conflicting objectives. The following three objectives have been considered to demonstrate the process. Other objectives representing organizational control, rapid access to data, and security considerations can be considered without affecting the basic structure of the problem.

(i) Minimum operating cost, includes processing cost, transmission cost and storage cost.

(ii) Minimum investment cost, includes cost of processor along with required primary and secondary storage.

(iii) Maximum file availability.

The mathematical expression in terms of input parameters and decision variables are developed for each of the above objectives. The detailed derivation of these expressions can be obtained from the author. The basic logic of these expressions is briefly described here.

## Operating Cost

Only the portion of the operating cost directly affected by the decision variables are considered in the model. It consists of the cost of processing the transactions and the transmission cost. The transmission cost has the following three components: (a) Due to transactions executed at remote node.

(b) Due to updating files at remote node.

(c) Due to a query requiring data from files stored at remote node.

## Investment Cost

The investment cost of the system consists of the cost of processors located at each node and the cost of secondary storage devices required for data files. It is assumed that the cost of processors depends on its class and includes the CPU, required memory, and a basic amount of secondary storage along with the cost of appropriate system software. The basic amount of secondary storage holds the operating system, other system programs, utilities, virtual memory storage, etc. The cost of developing the application system is not considered, as it should not be affected by the decision variables.

## File Availability

The files located at various nodes are accessed during transaction processing. Due to either failure of processors at nodes or to network links, certain files may become unavailable for access. It is desirable that the probability of files being available be as high as possible. Denoting by $AV_{k}$ the availability of file K, it is clear that $AV_{k}$ is affected by the reliability of processors at various nodes in the network and the number of file copies stored in the system. Based on the importance of each file and the application which processes it, the designer can assign relative weights to each data file. The weighted file availability is then maximized.

## 3. Solution Procedure

The distributed system design problem described in section 2 has a conflicting set of design objectives. It has been formulated as a non-linear goal programming problem [11]. Since there is no one best way to obtain an exact optimal solution to practical size non-linear programming problems, a heuristic procedure is used to obtain a satisfactory solution. The proposed method consists of two routines: the starting routine and the optimizing routine. The starting routine generates an initial solution. Starting with an initial solution, the optimizing routine attempts to improve it by a combination of exchange search [1] and steepest ascent [12] heuristic.

The starting routine consists of the following three steps:

(1) Find the assignment of processors to nodes such that the processing cost and the communication cost due to jobs processed at remote node is minimized.

(2) Using the optimal assignment of processors obtained above, find the allocation of files such that communication cost due to queries processed at remote nodes and due to update transactions is minimized.

(3) Using the processor and file assignment obtained above, compute the values of variables representing the processor speed $(Z_{s})$ , primary storage capacity $(M1_{s})$ , and secondary storage capacity $(H_{s})$ .

The optimizing routine begins with the initial solution $\bar{x}^{(1)}$ obtained above, and seeks to improve it. $\bar{x}^{(1)}$ serves as the first trial point $\bar{t}_{1,0}$ .

(1) A search similar to pattern search is conducted about each trial point by perturbing variables one at a time. For zero-one variables the permutation search heuristic is used to define neighborhood in terms of exchanges.

(2) Once all the variables about a trial point are perturbed, $\bar{t}_{k,n}$ is compared to the previous base point $\bar{x}^{(k)}$ . If the objective function improves, it becomes the new starting point $\bar{x}^{(k+1)}$ , and a portion of the pattern is formed. The search is terminated when two sequential iterations do not improve the solution by a specified $\bar{e}$ .

## 4. Overview of the Interactive Procedure

The distributed system design procedure described above is implemented on a UNIVAC 1100/81 computer. One of the principal design criteria was to make the software as transportable as possible. The programs are strictly modular and the programming language is ANSI standard FORTRAN. The system is designed to be self-instructive. It guides the designer through the design process by appropriate prompts and questions. When a choice or decision is needed, it presents either a “yes” or “no” question or a menu of alternatives. The designer can change a single input parameter and obtain a new design along with the results of evaluation on the terminal screen. The designer can also interactively assign and change the priority of design objectives to obtain alternative designs. The system can generate an initial starting solution or can use the user specified starting solution. Figure 2 depicts the overall design procedure.

## 5. Numerical Example and Sample Session

The interactive procedure is illustrated using a small numerical example. Much larger problems have been solved, but their display would be too long for our purposes here. The problem considered had 3 network nodes, 2 data files, and 3 classes of processors. The input parameters for the problem are shown in Tables 1, 2, 3, and 4. The processor related data of Table 1 can be obtained from the requirement specifications of the hardware under consideration. The processor reliability data can be obtained from the vendors under consideration. The job site and file related data needs to be estimated from previous experience and the analysis of proposed system. For large real life problems, input data can also be read from sequential files.

![](/api/attachments/3BRZ2RDD/fulltext/images/1d0fa9afc83a1fb1b82bc0d3f0bcfd77aa08939a12bdd85f6511ae733cc0b3ee.jpg)  
Fig. 2. Flow Chart of Design Procedure.

The following conventions hold in this illustration: all prompt or output messages which emanate from the system are shown in mixed upper and lower case letters. The designer's responses consist only of upper case letters and are underlined. The session begins with a greeting and a menu of 5 choices (see Figure 3) displayed by the system.

Specification of code 1 will let designers read either previously stored input parameters or specify or change any input parameters (see Figure 4). The Processor, Job, Site and File related data of Figure 4 refers to the input parameters.

Operation 2 will allow the designer either to read a previously-stored initial design or to specify a new initial solution (Figure 5). The option of a system-generated initial solution is currently being implemented.

<table><tr><td>Code</td><td>Operation</td></tr><tr><td>1</td><td>Specify, read, or change input parameter values</td></tr><tr><td>2</td><td>Specify, read, or change initial design</td></tr><tr><td>3</td><td>Specify or change priority of design objective</td></tr><tr><td>4</td><td>Evaluate initial design and find optimal design</td></tr><tr><td>5</td><td>Exit</td></tr></table>

Fig. 3. Menu of Choices.

<table><tr><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr><tr><td>*</td><td colspan="13">WELCOME TO DISTRIBUTED SYSTEM DESIGNER</td><td>*</td></tr><tr><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr></table>

Please specify operation you want to perform.
(Type 0 for list of operations available)

Specify parameter you want to change.

Fig. 4. Input Parameters.

Please specify operation you want to perform.
(Type 0 for list of operations available)

Please select an option:

<table><tr><td>Code</td><td>Option</td></tr><tr><td>1</td><td>Read previously stored initial design.</td></tr><tr><td>2</td><td>Use system generated initial design.</td></tr><tr><td>3</td><td>Specify or change initial design.</td></tr><tr><td>=&gt;3</td><td></td></tr></table>

Please select variable you want to specify or change:

<table><tr><td>Code</td><td>Variable</td></tr><tr><td>1</td><td>Processor assignment at each site ( $d_{ms}$ )</td></tr><tr><td>2</td><td>Processor speed at each site ( $Z_s$ )</td></tr><tr><td>3</td><td>Primary storage required at each site ( $M1_s$ )</td></tr><tr><td>4</td><td>Secondary storage required at each site ( $M_s$ )</td></tr><tr><td>5</td><td>File assignment ( $X_{sk}$ )</td></tr></table>

Fig. 5. Initial Solution Specification.

Table 1

Processor Related Data

<table><tr><td rowspan="2"></td><td colspan="3">Processor class</td></tr><tr><td>Micro</td><td>Mini</td><td>Mainframe</td></tr><tr><td>Reliability</td><td>0.990</td><td>0.980</td><td>0.978</td></tr><tr><td>Cost of processing a million machine instruction in dollars</td><td>0.001</td><td>0.002</td><td>0.003</td></tr><tr><td>Software path length in thousands of instruction</td><td>1.0</td><td>10.0</td><td>70.0</td></tr><tr><td>Cost of buying a kilobyte of secondary storage capacity</td><td>0.20</td><td>0.25</td><td>0.35</td></tr><tr><td> $C_1$ </td><td>1.0</td><td>100.0</td><td>400.0</td></tr><tr><td> $C_2$ </td><td>5.0</td><td>80.0</td><td>750.0</td></tr><tr><td> $C_3$ </td><td>0.003</td><td>0.005</td><td>0.1</td></tr></table>

Note: $C_1, C_2,$ and $C_3$ are constants in the following processing cost equation, their values depend on processor class and current level of technology.  
Cost = $C_{1} + C_{2}$ (processor speed) + $C_{3}$ (primary storage capacity).

Please specify operation you want to perform.
(Type 0 for list of operations available)

=>3

Please select an option:

Code Option

1 Assign or change objective priority

2 Assign or change relative weights of file

=>1

Please assign distinct priorities to the following objectives

Serial No. Description

1 Minimize operating cost of system

2 Minimize investment required

3 Maximize weighted file availability

Input serial number of the objective to which priority needs to be assigned or changed. (Type 0 if done)

=>3

Please indicate the priority of objective 3 (one indicates the highest priority, two indicates lower than one, and so on).

=>2

Input serial number of the objective to which priority needs to be assigned or changed. (Type 0 if done)

=>0

Please select an option:

Code Option

1 Assign or change objective priority

2 Assign or change relative weights of file

=>2

Input serial number of file for which weightage needs to be assigned or changed. (Type 0 if done)

=>1

Indicate relative weight to be assigned to file 1. (1.0 is the normal weight, higher number will indicate the higher weight, while a number lower than 1.0 will indicate a lower weight.)

=>0.5

Fig. 6. Objective Priority and Weights.

Table 2
Job Related Data

<table><tr><td rowspan="2"></td><td colspan="3">Job class</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Average length of jobs (gr)</td><td>100.0</td><td>400.0</td><td>800.0</td></tr><tr><td>Transmission required in kilobyte to remotely execute the job (αr)</td><td>7.5</td><td>30.0</td><td>100.0</td></tr><tr><td>Average primary storage required in K byte</td><td>64.0</td><td>100.0</td><td>500.0</td></tr></table>

Operation 3 will allow the designer to specify or change priority of each design objective. Currently three objectives representing investment cost, operating cost, and weighted file availability have been implemented. Designers can also assign and change relative weights of each file (see Figure 6).

Please specify operation you want to perform.
(Type 0 for list of operations available)

The initial design is feasible:

Objective function values are:

1. Operating cost per year \$1,542,000

2. Investment Cost \$5,000,000

3. Weighted file availability 0.995

Do you want to continue with optimization? (If yes, type "Y"; else type "N")

=>Y

Search algorithm completed

Tolerances for improved solutions satisfied

Objective function values are:

1. Operating cost per year \$ 500,000

2. Investment Cost \$5,000,000

3. Weighted file availability 0.995

Do you want to display this solution?

(If yes, type "Y"; else type "N")

=>Y

Fig. 7. Optimal Solution.

<table><tr><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr><tr><td>*</td><td colspan="6">PRESENT DESIGN</td><td>*</td></tr><tr><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr></table>

Processor Assignment

<table><tr><td>Node #</td><td>Processor Class</td><td>Processor Speed MIPS</td><td>Primary Storage required in Megabyte</td><td>Secondary Storage required in Megabyte</td></tr><tr><td>1</td><td>Main Frame</td><td>4.564</td><td>1.084</td><td>13.5</td></tr><tr><td>2</td><td>Mini Computer</td><td>0.03</td><td>0.025</td><td>13.5</td></tr><tr><td>3</td><td>Main Frame</td><td>6.824</td><td>1.764</td><td>0</td></tr></table>

File Assignment

<table><tr><td colspan="4">Nodes</td></tr><tr><td>File #</td><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>x</td><td>x</td><td></td></tr><tr><td>2</td><td>x</td><td>x</td><td></td></tr></table>

Fig. 8. Optimal Design of Distributed System.

Operation 4 will first check the feasibility of the initial design specified or generated, then evaluate it with respect to design objectives and will display the results (see Figure 7). The heuristic procedure will then be executed to find and display the optimal solution. The designer can now display the values of design variables (see Figure 8).

Table 3  
Site Related Data

<table><tr><td rowspan="2"></td><td colspan="3">Site</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Arrival rate/hr ( $\lambda_s$ )</td><td>1500.0</td><td>200.0</td><td>2000.0</td></tr><tr><td>Probability job Class 1</td><td>0.1</td><td>0.2</td><td>0.1</td></tr><tr><td>Probability job Class 2</td><td>0.3</td><td>0.5</td><td>0.1</td></tr><tr><td>Probability job Class 3</td><td>0.6</td><td>0.3</td><td>0.8</td></tr></table>

After comparing this design with any previous ones, the designer may either accept it and stop, or change the objective priority and weights or values of any input parameters (see Figure 9). A design can be stored as a preferred design. The designer may also try to change the initial solution to get another optimal solution (the heuristic algorithms do not guarantee a global optimal solution, so it is

Table 4  
File Related Data

<table><tr><td rowspan="3">Files</td><td rowspan="3">Size in Kilo Byte</td><td rowspan="3">Weight Assigned</td><td colspan="3"> $Q_{rk}$ </td><td colspan="3"> $p_{rk}$ </td><td colspan="3"> $O_{rk}$ </td><td colspan="3"> $t_{rk}$ </td></tr><tr><td colspan="3">Sites</td><td colspan="3">Sites</td><td colspan="3">Sites</td><td colspan="3">Sites</td></tr><tr><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>3500.0</td><td>0.5</td><td>0.9</td><td>0.5</td><td>0.5</td><td>0.65</td><td>0.2</td><td>0.8</td><td>10.0</td><td>30.0</td><td>60.0</td><td>1.0</td><td>0.3</td><td>10.0</td></tr><tr><td>2</td><td>10,000.0</td><td>4.0</td><td>0.1</td><td>0.5</td><td>0.5</td><td>0.35</td><td>0.8</td><td>0.2</td><td>0.1</td><td>1.0</td><td>7.0</td><td>3.0</td><td>5.0</td><td>8.0</td></tr></table>

Fig. 9. Comparing Designs.

possible that the solution obtained by changing the initial solution is different). This process can thus be repeated until a satisfactory solution is obtained.

## Conclusion

An interactive procedure for the design of distributed computer system has been described. The design problem addressed is that of selecting a class of computer, its processing speed, and the primary and secondary storage, for each node of a distributed system. Also considered was the problem of allocating data files in a distributed system. It is assumed that a value added network is used for data communication. In cases involving large communications volumes, a dedicated network may be used. In that case the communication cost function in the model needs to be modified. The difference in cost of processing a transaction on a smaller computer as compared to a large mainframe (due to lower cost per machine instruction and lower software path length) was considered. Multiple copies of data files were allowed to exist in the system. A friendly user interface which allows the designer to specify and change any input parameters, initial solution, and objective priority was implemented. The system was tested by solving a large number of example problems.

## References

[1] Beveridge, G. and Schechter, R., Optimization Theory and Practice, McGraw-Hill Book Company, 1970, New York.

[2] Buhr, R.J.A., and Woodwide, C.M., “Microscopic economic planning models for distributed information systems.” INFOR, Vol. 15, No. 2, (1977).

[3] Casey, R.G., “Allocation of Copies of a File in an Information Network,” AFIPS Conference Proceedings, Vol. 40, 1972, SJCC, pp. 617–625.

[4] Chen, P., and Akoka, J., “Optimal Design of Distributed Information Systems,” IEEE Transactions on Computers, Vol. C-29, No. 12 (1980), pp. 1068–1080.

[5] Chu, W.W., “Optimal File Allocation in Multiple Computer Systems,” IEEE Transactions on Computers, Vol. C-18 (1969), pp. 885–889.

[6] Dutta, A., and Jain, H., “A DSS for Distributed Computer System Design in the Presence of Multiple Conflicting Objectives,” Decision Support Systems, Vol. 1, No. 3, 1985.

[7] Fin-Dor. P., “Grosch’s Law Re-Revisited: CPU Power and the Cost of Computation,” Communications of ACM, Vol. 28, No. 2, February 1985.

[8] Grosch, H.A., “High speed arithmetic: The digital computer as a research tool,” Journal of Operations Research Society, Vol. 43, No. 4 (April 1953).

[9] Gavish, B., and Hasan, P., “Allocation of Databases and

Processors in a Distributed Computing System," Management of Distributed Data Processing, J. Akoka (Ed.), North-Holland Publishing Co., 1982.

[10] Ignizio, J.P., Palmer, D.F., and Murphy, C., “A Multicriteria Approach to Super System Architecture Definition,” IEEE Transactions on Computers, Vol. C-31, No. 5, May 1982, pp. 410–418.

[11] Ignizio, J.P., Goal Programming and Extensions. Lexington Books, Massachusetts, 1976.

[12] Ignizio, J.P., “Solving Large-Scale Problems: A Venture Into a New Dimension,” Journal of the Operations Research Society, Vol. 31, No. 3, 1980.

[13] Irani, K.B., and Khabbaz, N.G., “A Methodology for the Design of Communication Networks and the Distribution of Data in Distributed Super Computer Systems,” IEEE Transactions on Computers, Vol. C-31, No. 5, May 1982, pp. 419–434.

[14] Mahmoud, S., and Riordan, J.S., “Optimal Allocation of Resources in Distributed Information Networks,” ACM Trans. on Database Systems, Vol. 1, No. 1, 1976, pp. 66–78.

[15] Martin, J., Design and Strategy for Distributed Data Processing, Prentice-Hall, Inc., Englewood Cliffs, N.J., 1981.

[16] Mitrani, I., and Sevick, “Evaluating the Trade-off Between Centralized and Distributed Computing,” Proc. 1st International Conference on Distributed Computing Systems, Oct. 1979, pp. 520–528.

[17] Morgan, H.L., and Levin, K.D., “Optimal Program and Data Locations in Computer Networks,” Communications of ACM, Vol. 20, No. 5, 1977, pp. 315–321.

[18] Radin, G., “The 801 Minicomputer,” Proc. of Symposium on Architectural Support for Programming Languages and Operating Systems, 1982, pp. 39–47.
