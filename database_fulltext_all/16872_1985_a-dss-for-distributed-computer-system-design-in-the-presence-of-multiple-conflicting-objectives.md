---
otero_id: 16872
otero_key: "CEV9BBUB"
title: "A DSS for distributed computer system design in the presence of multiple conflicting objectives"
authors: "Amitava Dutta; Hermant K. Jain"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90242-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DSS for Distributed Computer System Design in the Presence of Multiple Conflicting Objectives

Amitava DUTTA $^{+}$ and Hemant K. JAIN $^{*}$

$^{*}$ The Graduate School of Management, The University of Rochester, Rochester, NY 14627 and $*$ School of Business Administration, University of Wisconsin at Milwaukee, Milwaukee, WI 53201, U.S.A.

The design of distributed computer systems (DCS) requires compromise among several desirable and conflicting objectives. Design tools for this purpose should, therefore, facilitate the process of making such tradeoffs. To this end, this paper presents a prototype Decision Support System (DSS) which uses multicriteria decisions making techniques as the underlying methodology to aid the designer in making compromises in a systematic and efficient manner.

While there are several isolated subproblems of DCS design that can be modelled and solved quantitatively, there are also, many design aspects that are difficult to quantify and/or formalize. Thus the design process requires a synthesis of analytic model execution and informed judgement on the part of the designer. The DSS aids in this iterative process by executing appropriate models and generating a sequence of 'Pareto-optimal' or non-dominated set of solution vectors. The relatively unsstructured task of making tradeoffs among the components of each vector is left in the hands of the designer. Efficiency is achieved by avoiding needles search through clearly inferior solutions and focusing on non-dominated ones only. Various details of the prototype, implemented on a UNIVAC 1100 and an IBM PC AT, are highlighted in an example session. The potential advantages of using multicriteria techniques as opposed to the widespread practice of using single criteria optimization methods are also noted in this paper.

Keywords: Keywords: Distributed Systems; Design; Multiobjective Decision Making; Distributed Databases; Tradeoffs.

## 1. Introduction

The environment of a Distributed Computer System (DCS) consists of a collection of sites interconnected by a communication network. Processors and storage media are located at various nodes and the nodes usually share an integrated database. DCS are usually characterized by physical distribution and logical centralization. Many automobile and airline reservation systems, for instance, would fall into this class. The design of DCS is a complex process which requires compromise among several desirable and conflicting objectives. It is possible to list several such objectives:

(i) Low response time to online queries/transactions;

(ii) Low system cost;

(ii) High system availability;

![](/api/attachments/CEV9BBUB/fulltext/images/9a179b223fb34fa677a1164236acdb7eacfdf6d02cebe0ac9e4e5e6da721582b.jpg)

Amitava Dutta is assistant professor of computer and information systems at the Graduate School of Management at The University of Rochester. He received a B. Tech. in electronics from the Indian Institute of Technology, Kharagpur in 1976, and M.S. in computer science from UC Santa Barbara, and a 'h.D. in Management from Purdue University in 1981. His research interests lie in the areas of knowledge-based expert systems, artificial intelligence applications in

management, parallel computer architectures and distributed databases.  
![](/api/attachments/CEV9BBUB/fulltext/images/bae447b733f6547ea2ee87b5a738b41c22de647e24e32a55acbb8e573edc8097.jpg)

Hemant K. Jain is assistant professor of Management Information Systems at the School of Business Administration at the University of Wisconsin-Milwaukee. He received his B.S. in Mechanical Engineering from University of Indore (India) in 1973, a M.Tech. in Industrial Engineering from I.I.T. Kharagpur (India) in 1975 and a Ph.D. in Industrial Engineering from Lehigh University. Bethlehem PA. in 1981. His research interests lie in the areas of distributed computer

systems, computer networking, design of centralized and distributed databases, decision support systems, expert systems and CAD/CAM.

(iv) Easy expandibility

(v) Easy modifiability.

While the above is by no means an exhaustive list, it is clear that some objectives are easier to quantify than others. Furthermore, there exists conflicts among the different objectives. For instance, low response time may require certain redundancies which will drive up cost. The same kind of trade-off exists between system cost and availability. Any 'good' DCS design methodology will have to achieve some compromise among such conflicting objectives by appropriately manipulating the decision variables. Such variables include the selection of storage and processing power and the location thereof. Network topology, routing and location of database files are other important decision variables.

The prototype DSS in this paper aids this iterative process in the following manner. First, by using multicriteria optimization techniques, the DSS allows the designer to concentrate on only the 'best' alternatives during any given iteration. The alternatives are 'best' in the sense that none of them dominates any other in all respects. This feature avoids needless search through inferior solutions. Next, the designer can experiment with perturbations and see the resulting solutions. In this way, analytical model execution is combined with the designer's judgement in iterating towards a final acceptable solution. The operation of the DSS is demonstrated through an example session. Mathematical details appear elsewhere [1] and are only briefly presented in section 3. Another example of the use of multicriteria techniques (for super-computer systems design) appears in [2].

## 2. Underlying Methodology

The methodology underlying the operation of the DSS is that of multicriteria decision making. A particular form, called the generalized binary vectorminizing problem [3] is adopted, which can be stated as:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\min \underline{Z} (\underline{x})$ $\underline{x}\in \Omega$   
Where   
$\underline{Z}\colon \underline{S}^{m}\to \mathbf{R}^n,X = \{0,1\}$ $\Omega \subseteq \underline{S} ^m$ is the feasibility region   
$\underline{Z}$ is the vector objective function   
$\underline{x}$ is the vector decision variable
</div>

Note that multiple objective functions are allowed. In the presence of multiple objectives, the meaning of the 'Min' operation has to be modified from its usual interpretation. The Min consists of finding so called nondominated solutions. More formally:

$\underline{x}^{\prime}\epsilon\Omega$ is said to be dominated if there exists $\underline{x}^{\prime\prime}\epsilon\Omega$ , $\underline{x}^{\prime}\neq\underline{x}^{\prime\prime}$ such that

$\underline{Z}(\underline{x}^{\prime\prime}) \leq \underline{Z}(\underline{x}^{\prime})$ (strict inequality holds for at least one component of $\underline{Z}$ ).

Similarly, a solution $x^{\prime}\epsilon\Omega$ is said to be a non-dominated solution if:

$$
\begin{array}{l} \forall \underline {{x}} ^ {\prime \prime} \epsilon \Omega \underline {{Z}} (\underline {{x}} ^ {\prime \prime}) \leq \underline {{Z}} (x ^ {\prime}) \\ (\underline {{x}} ^ {\prime \prime} \neq \underline {{x}} ^ {\prime}) \end{array}
$$

(At least one component of $\underline{Z} (\underline{x} '') >$ that of $\underline{Z} (\underline{x}')$ .)

Thus it is clear that the process of finding the nondominated solutions will generate only the 'best' alternatives noted earlier in the paper. Choice of an appropriate solution from among these nondominated ones is made by the designer based on informed judgment. The method used to generate nondominated solutions is the Exchange Search Heuristic [4]. Also an $\varepsilon$ constraint method is used to limit the number of nondominated solutions generated in an iteration. This heuristic gives the DSS its interactive nature. A similar heuristic has also been used in [2]

## 2.1. The Exchange Search Heuristic

The exchange search heuristic is simply a systematic method for generating the nondominated solutions during each iteration. It needs an initial feasible solution as the starting point. (Recall that this would be a vector since there would be multiple values corresponding to the different objective function. Generation of an initial solution is discussed in section 3.5 after problem formulation.) Then given some tolerances for each component of this initial solution vector, the heuristic systematically generates nondominated solution vectors that satisfy these given tolerances. The specification of tolerances limits the number of nondominated solution generated to a manageable number. Thus the decision maker is not burdened with a very large number of solutions to choose from. In the absence of such systematic generation, the user may waste considerable effort in exploring clearly inferior solutions.

Assume that $x^{1}\epsilon\Omega$ is an initial feasible solution. Since $x^{e}\epsilon S^{m}$ , some components of $x^{1}$ are set to 1 while others are set to 0. The heuristic exchanges the value of one or more variables with value 1 for one or more variables with value 0. Exchanges considered in practice are 1–1, 1–2, and possibly 2–2. For example, if:

$\underline{x}^1 = \{1, 1, 0, 1, 1, 0, 0, 0\}$ , then:

![](/api/attachments/CEV9BBUB/fulltext/images/052f075d77096d6a374a77daa9d2bfff42c89a88706a3dad1c6f58af814ba90f.jpg)  
Fig. 1. The Exchange Search Heuristic.

$\underline{x}^2 = \{0, 1, 1, 1, 1, 0, 0, 0\}$ is a 1-1 exchange $\underline{x}^3 = \{0, 1, 0, 1, 1, 1, 0, 0\}$ is also a 1-1 exchange
on $x^1$ .

Assuming that only 1–1 exchanges are attempted, (types 1–2, 2–2 etc. may be included without affecting the subsequent development). let $\Gamma$ be the set of all possible 1–1 exchanges.

If $|\Gamma| = M$ , then $\Gamma = \left\{ \underline{x}^2, \underline{x}^3, \ldots, \underline{x}^{M+1} \right\}$

Let $\underline{Z}^1 = \underline{Z}(\underline{x}^1)$ be the initial vector objective solution.

Now, define:

$$
\Omega_ {\xi} = \Omega \cap \left\{\underline {{{x}}} \epsilon \underline {{{S}}} ^ {m} | [ \underline {{{Z}}} (\underline {{{x}}}) - \underline {{{Z}}} ^ {1} ] \leq \xi \right\}
$$

where $\xi\in R^{n+}$ is called the vector of allowed tolerances, and:

$$
\left[ \underline {{Z}} (\underline {{x}}) - \underline {{Z}} ^ {1} \right] = \left[ \begin{array}{c} {\left[ Z _ {1} (\underline {{x}}) - Z _ {1} ^ {1} \right]} \\ {\left[ Z _ {2} (\underline {{x}}) - Z _ {2} ^ {1} \right]} \\ \vdots \\ {\left[ Z _ {n} (\underline {{x}}) - Z _ {n} ^ {1} \right]} \end{array} \right]
$$

The exchange search heuristic, whose flowchart appears in Fig. 1, consists of finding the non-dominated solutions within the set $E = \Gamma \cap \Omega_{\xi}$ , dominated in the sense that no solution in the set $E$ dominates them. The set of nondominated solutions in $E$ is denoted by $N$ .

Notice the interactive nature of the heuristic. The structured task of the generation of alternatives is assumed by the procedure while input from the designer is required in the selection from the set of alternatives. This heuristic lies at the heart of the operation of the DSS. Before proceeding with operational details, it is necessary to present briefly some of the conflicting objective functions in DCS design along with some of the structural constraints of the design environment.

## 3. Formulation of the DCS Design Problem

Before we can proceed with details of the system it is necessary to present formally the DCS design problem in terms of the decision variables, the objective functions and the relationships between various decision variables and the objective functions. A summary will suffice for purposes here. Further details and justifications thereof can be found elsewhere [1].

![](/api/attachments/CEV9BBUB/fulltext/images/d5f717aaa2c022b09c95abea0b59d09a67fd353fa11ca1c6381ec0a1b1137866.jpg)  
Fig. 2. The DCS Environment.

## 3.1. Input Variables

$n_{s}$ = number of physically different sites

$n_{f}$ = number of files constituting the database

$n_{c}$ = number of different types of communication channels (Each type may have a different cost, probability of failure and speed of transmission.)

$n_{t}$ = number of different types of processors available, each type with a possibly different cost and reliability

$L_{ij} =$ distance between sites i and j

$SI_{f} =$ size of file f

$r_{s}$ = reliability of communication channel of type s

$p_{l} =$ reliability of processor of type $l$

$c_{l} = \text{cost of processor of type } l$

## 3.2 Decision Variables

Three important decision variables have been selected from among the many possible, for implementation purposes. They are:

(i) Selection of processing power and location thereof

(ii) Selection of channel capacity and network topology

(iii) Location of database files

Accordingly, the following variables are defined:

$$
D _ {l k} = \left\{ \begin{array}{l l} 1 & \text { if   processor   of   type } l \text { is   at   sitc } k \\ 0 & \text { otherwise } \end{array} \right.
$$

$CH_{ij} = \text{type of channel linking sites i and j. This value is 0 if there is no link between i and j}$

$$
w _ {\mathrm{fk}} = \left\{ \begin{array}{l l} 1 & \text { if   file   f   is   located   at   site   k } \\ 0 & \text { other   wise } \end{array} \right.
$$

While it is possible to name additional variables that have a bearing on the design, the above three collectively cover the decision variables commonly considered in the literature.

## 3.3. Objective Functions

Three important objective functions are considered here to demonstrate the process of making trade-offs between conflicting objectives. They are:

(i) Minimum system cost, where such cost is the sum of processor costs, communication network costs and storage costs;

(ii) Minimum weighted average response time;
(iii) Maximum file availability.

Each of these is discussed in turn;

## 3.3.1. Processor Cost $\Psi_{p}$

The first component of system cost is that of processor costs which can be written, using the variables introduced earlier, as:

$$
\Psi_ {\mathrm{p}} = \Sigma c _ {l} \cdot D _ {l k} \quad \begin{array}{l l} l = 1, \dots , n _ {\mathrm{i}} \\ k = 1, \dots , n _ {\mathrm{s}} \end{array}
$$

Processors have different reliabilities in this model which result in higher costs for the more reliable ones.

## 3.3.2. Communication Network Costs $\Psi_{CCN}$

Network costs have two components: a fixed termination cost depending on the line capacity; and a variable cost depending both on the line capacity and the physical distance covered by the line. Thus, network topology and the capacity selected for particular lines affects the network cost. This can be written as:

$$
\Psi_ {\mathrm{CCN}} = \Psi_ {\mathrm{FCN}} + \Psi_ {\mathrm{VCN}}
$$

where:

$$
\Psi_ {\mathrm{FCN}} = \text {   fixed   cost   of   network   }
$$

$$
\Psi_ {\mathrm{VCN}} = \text { variable   cost   of   network }
$$

$$
\begin{array}{l l} \Psi_ {\mathrm{FCN}} = & \Sigma_ {i, j} \tau (\underline {{C H}} _ {i j}) \\ \Psi_ {\mathrm{VCN}} = & \Sigma_ {i, j} \nu (\underline {{C H}} _ {i j}, L _ {i j}) \end{array}
$$

$\tau(.)$ is the fixed cost function, while $\nu(.,.)$ is the variable cost function.

## 3.3.3. Storage Costs $\Psi_{s}$

This cost arises from the need to store large amounts of data on secondary storage, in the form of program and data files. Again, this cost can be compactly expressed as:

$$
\Psi_ {\mathrm{s}} = \sum_ {\mathrm{f}, \mathrm{k}} S I _ {\mathrm{f}} \cdot w _ {\mathrm{fk}} \begin{array}{l} f = 1, \dots , n _ {\mathrm{f}} \\ k = 1, \dots n _ {\mathrm{s}} \end{array}
$$

It is sometimes necessary to include query and update communication costs as part of the system cost. This is appropriate in the case of a common carrier network where the user has to pay a fee based on the amount of traffic generated on the network by him [5]. Note, however, that in our model we are assuming that the network topology is a decision variable. Thus the environment is that of a private custom-designed network. Here, there is no tariff on the amount of communicating traffic generated. Thus it would be improper to include query and update costs in our model of system cost. This is not to say that such traffic patterns are irrelevant to the design process. They are more appropriately included in the analysis of system response time, as will be seen shortly.

## 3.3.4. System Response Time

The DCS has transactions originating from each node, which may access files at other nodes in the network. There will be communication delays for these transactions. It is assumed that accesses to files are independent. The objective is to minimize some weighted response times over all sites and all files, which in turn implies that the weighed average response time is minimized. If we denote by $\rho$ the total weighted response time, then:

$$
\rho = \sum_ {\mathrm{if}} g _ {\mathrm{if}} R E S _ {\mathrm{if}}
$$

where $g_{if}$ is some appropriate weight assigned to the access of file f from site i. The procedure for estimating $RES_{if}$ appears in detail in [1] and is summarized here.

Since there may be multiple copies of a file in our model, it is proper to assume that queries are answered from the 'nearest' site that stores a copy of the desired file. On the other hand, update to a file must be communicated to all copies of a file. Note that values for decision variables must have been set prior to the computation of system response time. In particular, the number of copies and placement of different files are known together with the network topology. An adaptive routing strategy is used [6] to route the access from a site to a file. For each combination of site and file, the communication delay can be computed for the particular route determined by this strategy. The collection of such delays both for queries and updates are weighted appropriately and then added to get the value for $\rho$ .

## 3.3.5. File Availability

It was observed that files located at various locations are accessed during transaction processing. Due to a combination of link/node failures, certain files may become unavailable for access. This happens when a certain site cannot access any copy of a desired file. Denoting by $A_{f}$ the availability of file f, it is clear that $A_{f}$ is affected by the reliability of processors at various nodes, along with the reliability of individual links in the network. The routing pattern for messages also has an effect since different routes for access involve different nodes and sequences of links, implying different failure probabilities for each distinct route. It has been shown in [1] that:

$$
A _ {f} = R (1 - \prod_ {i} (1 - w _ {f i} (1 - \prod_ {l} (1 - p _ {l} D _ {l i}))))
$$

where:

R = network reliability and other variables have been defined previously

The interpretation of the above expression is quite simple. The term $\prod_{i}(1-p_{i}D_{li})$ is the probability that all processors at site i are down. Hence, $w_{fi}(1-\prod(1-p_{i}D_{li}))$ represents the likelihood of at least one processor being up at a site that has a copy. Proceeding in this manner, the right hand side of the above expression is the likelihood that at least one processor at one site containing a copy of file f is up and that the network is connected. This value is computed for each file, It is, of course, possible to suggest alternative measures of file availability which are further aggregated or disaggregated. The network reliability R is the probability that it is connected, and can be computed along the lines developed in [7, 8].

## 3.4. Summary of Design Process

Figure 3 shows a flowchart depicting the design process using the system. The real value of the DSS lies in its ability to generate systematically the best alternative solution vectors for the multiple objectives. The human designer is given the task best suited for him - that of making trade-offs, while the various procedures/algorithms in the DSS perform the more structured tasks of generation of alternative solutions. The design process itself is iterative as observed at the start of the paper. Notice how the generation of alternatives is performed by the system, while the human designer has control over when to terminate the design process or from which alternative to proceed. The designer's control is quite crucial since there are many design aspects that are hard to quantify/formalize. Furthermore, certain trade-offs cannot be expressed algorithmically. Later in the paper an example of a session is shown where these points are highlighted.

## 3.5. Initial Feasible Solution

The exchange search procedure needs an initial feasible solution from which to proceed. This consists of finding one set of values for the decision variables which does not violate any model constraints. In particular, values must be assigned to $D_{1k}$ (processor allocation), $CH_{ij}$ (channel capacity and network topology) and $W_{fk}$ (file allocation) so that all structural constraints are met. As Fig. 3 shows, this can be done in one of two ways. One alternative is to have the user specify an initial solution. This is useful when the designer has some prior ideas of the general nature of the final solution or when he is proceeding from a solution generated from an earlier iteration and stored for future use.

The other alternative of course is to have the system generate a starting solution. In the present stage of implementation we start with a minimum spanning tree with minimum capacity assigned to each link. There are various models in the literature that address file and processor allocation in isolation [9,10]. A simplified version of any of these will suffice since a feasible solution is required initially as opposed to an optimal solution. Since the structural constraints are not very complex, the starting solution for file and processor allocation is chosen according to the following guidelines. A single copy of each file is kept at or near the site that accesses it most frequently. A processor is then placed at each site so chosen. This follows from the restriction that a processor must be located at any site that has storage capacity assigned to it. Recall that this does not preclude the placement of extra processors at additional sites.

![](/api/attachments/CEV9BBUB/fulltext/images/a8ed25fa80b9a138d1a0e6f9aba888f23f6d0cd242bb477dc7649ce5ef69e9d0.jpg)  
Fig. 3. Flowchart for DCS Design Using Prototype DSS.

Note that a method used to generate an initial feasible solution cannot be repeatedly used to converge to a 'best' solution. This is because the initial solution, in and of itself, does not give us any systematic way to alter the decision variables in order to improve the overall solutions. Note that optimal solutions to isolated subproblems (say network topology or file allocation) do not give us any such scheme either. The exchange search heuristic systematically searches the solution space and generates Pareto-optimal objective function vectors. Our formulation (or any multiobjective formulation for that matter) thus explicitly recognizes the presence of multiple conflicting objectives and attempts to achieve trade-offs among them in a systematic manner. The alternative approach of repeatedly executing single criteria model is contrasted in section 5:

## 4. Session Example

The prototype DSS consists of several FORTRAN modules. The most important module is perhaps the exchange search module. There are others for determining system response time, file availabilities and system cost. It is quite easy to generalize the system to handle other or additional objectives. The parameters for a small problem are shown below. Much larger problems have been attempted, but their display would be too long for our purposes here.

The session has been displayed in meaningful sections to highlight various features. It begins by recalling the initial solution which had been stored previously in a separate file. Figures 4 and 5 Number of Sites: 5

Processors  
Files

<table><tr><td>File #</td><td>Size</td><td>Availability Weight</td></tr><tr><td>1</td><td>250K</td><td>3.0</td></tr><tr><td>2</td><td>600K</td><td>1.0</td></tr><tr><td>3</td><td>800K</td><td>2.0</td></tr></table>

<table><tr><td>Processor type</td><td>Cost</td><td>Reliability</td></tr><tr><td>1</td><td>1000000</td><td>0.98</td></tr><tr><td>2</td><td>750000</td><td>0.95</td></tr></table>

Access Frequencies

<table><tr><td>File No.</td><td>Query Freq.</td><td>Query Wght.</td><td>Update Freq.</td><td>Update Wght.</td><td></td></tr><tr><td>1</td><td>100</td><td>3.0</td><td>300</td><td>1.5</td><td rowspan="3">Site 1</td></tr><tr><td>2</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>3</td><td>200</td><td>1.0</td><td>200</td><td>0.5</td></tr><tr><td>1</td><td>0.0</td><td>0.0</td><td>50</td><td>1.0</td><td rowspan="3">Site 2</td></tr><tr><td>2</td><td>300</td><td>1.0</td><td>0.0</td><td>0.0</td></tr><tr><td>3</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>1</td><td>600</td><td>3.0</td><td>150</td><td>1.0</td><td rowspan="3">Site 3</td></tr><tr><td>2</td><td>1000</td><td>1.0</td><td>130</td><td>0.5</td></tr><tr><td>3</td><td>500</td><td>0.5</td><td>300</td><td>0.5</td></tr><tr><td>1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td rowspan="3">Site 4</td></tr><tr><td>2</td><td>70</td><td>1.0</td><td>0.0</td><td>0.0</td></tr><tr><td>3</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>1</td><td>0.0</td><td>0.0</td><td>1000</td><td>1.0</td><td rowspan="3">Site 5</td></tr><tr><td>2</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>3</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Communication Channels

<table><tr><td>Channel Type</td><td>Speed Baud</td><td>Reliab.</td><td>Fixed Cost</td><td>Var. Cost</td></tr><tr><td>1</td><td>1200</td><td>1</td><td>300</td><td>0.2</td></tr><tr><td>2</td><td>4800</td><td>1</td><td>450</td><td>0.5</td></tr><tr><td>3</td><td>9600</td><td>1</td><td>600</td><td>0.75</td></tr></table>

Note: Fixed cost in \$/month  
Variable cost in \$/month/mile

Distance Matrix $(L_{ij})$

<table><tr><td>Site No.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>0</td><td>500</td><td>800</td><td>1000</td><td>700</td></tr><tr><td>2</td><td></td><td>0</td><td>400</td><td>800</td><td>600</td></tr><tr><td>3</td><td></td><td></td><td>0</td><td>300</td><td>550</td></tr><tr><td>4</td><td></td><td></td><td></td><td>0</td><td>450</td></tr><tr><td>5</td><td></td><td></td><td></td><td></td><td>0</td></tr></table>

Input Data for Problem

Do you want to retrieve previously stored Input Data if any

> Y

Do you want to retrieve previously stored initial solution > Y

<table><tr><td colspan="4">THE VALUES OF OBJECTIVE FUNCTIONS ARE</td></tr><tr><td>Solution No</td><td>Total Cost</td><td>Weighted Availability</td><td>Weighted Response time</td></tr><tr><td>1</td><td>3797450.00</td><td>.96500</td><td>.57</td></tr><tr><td colspan="4">Do you want to see details of solution listedIf yes input 0</td></tr><tr><td colspan="4">&gt;0</td></tr><tr><td colspan="4">Non-Dominated solution number 1</td></tr><tr><td colspan="4">Objective Function values are</td></tr><tr><td colspan="4">Cost 3797450.00</td></tr><tr><td colspan="4">Availability .96500</td></tr><tr><td>Response time</td><td>0.57</td><td></td><td></td></tr></table>

Fig. 4. Recall of Initial Solution Stored Prior to Session.

present details of that solution. In particular, there is no processor assigned to site 5 and no files are located at sites 2, 4 and 5. Files 2 and 3 are co-located at site 3 while file 1 is located at site 1. Note that the display of solution details is at the discretion of the user; any or all details can be suppressed at will. This ability may be useful during the initial iterations when the designer is only getting familiar with the nature of the final solution.

To try out different solutions, the designer next specifies that a deviation of \$1 000 000 is acceptable in total cost, 0.01 in weighted file availability and 2.9 seconds in weighted response time. This is the vector $\xi$ of acceptable deviations defined in section 2.1. As Fig. 6 shows, these deviations may be altered before proceeding. This vector $\xi$ is now

<table><tr><td colspan="6">COMPUTER TYPE SELECTED</td></tr><tr><td>Node #</td><td colspan="2">Computer Type</td><td colspan="3">Cost</td></tr><tr><td>1</td><td colspan="2">1</td><td colspan="3">1000000.00</td></tr><tr><td>2</td><td colspan="2">2</td><td colspan="3">750000.00</td></tr><tr><td>3</td><td colspan="2">2</td><td colspan="3">750000.00</td></tr><tr><td>4</td><td colspan="2">1</td><td colspan="3">1000000.00</td></tr><tr><td colspan="6">Press 1 to continue and 2 to suspend printing</td></tr><tr><td colspan="6">&gt;1</td></tr><tr><td colspan="6">FILE ASSIGNMENT</td></tr><tr><td>Node #</td><td colspan="2">File #</td><td colspan="3"></td></tr><tr><td>1</td><td colspan="2">1,</td><td colspan="3"></td></tr><tr><td>2</td><td colspan="2"></td><td colspan="3"></td></tr><tr><td>3</td><td colspan="2">2, 3,</td><td colspan="3"></td></tr><tr><td>4</td><td colspan="2"></td><td colspan="3"></td></tr><tr><td>5</td><td colspan="2"></td><td colspan="3"></td></tr><tr><td colspan="6">Press 1 to continue and 2 to suspend printing</td></tr><tr><td colspan="6">&gt;1</td></tr><tr><td colspan="6">CHANNEL ASSIGNMENT MATRIX</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td></td></tr><tr><td>1</td><td>0.00</td><td>1200.00</td><td>0.00</td><td>0.00</td><td>1200.00</td></tr><tr><td>2</td><td>1200.00</td><td>0.00</td><td>4800.00</td><td>1200.00</td><td>0.00</td></tr><tr><td>3</td><td>0.00</td><td>4800.00</td><td>0.00</td><td>4800.00</td><td>0.00</td></tr><tr><td>4</td><td>0.00</td><td>1200.00</td><td>4800.00</td><td>0.00</td><td>9600.00</td></tr><tr><td>5</td><td>1200.00</td><td>0.00</td><td>0.00</td><td>9600.00</td><td>* 0.00</td></tr></table>

Fig. 5. Details of Values for Decision Variables in Initial Solution.

<table><tr><td>Please input the acceptable deviations on objective function values</td></tr><tr><td>Current Cost is 3797450.00 Please input deviation &gt;1000000</td></tr><tr><td>Current Weighted Availability is .96500 Please input deviation ⇒</td></tr><tr><td>&gt;0.01</td></tr><tr><td>Current weighted response time is 0.57 Please input deviation ⇒</td></tr><tr><td>&gt;2.9</td></tr><tr><td>DEVIATIONS SPECIFIED ARE</td></tr><tr><td>Cost 1000000.00</td></tr><tr><td>Availability .01000</td></tr><tr><td>Response Time 2.90</td></tr><tr><td>Do you want to change any of these</td></tr><tr><td>&gt;No</td></tr></table>

Fig. 6. Specification of the Vector of Acceptable Deviations in Objective Function Values.

used by the exchange search heuristic to generate alternate solutions. Clearly, it is necessary to examine the nondominated solutions as defined earlier in the paper. Figure 7 shows that there are no other nondominated solutions within the allowed tolerance vector $\xi$ , as seems possible due to the small tolerance allowed for file availability. Note that solution details have been suppressed by the designer at this point.

The design process proceeds in Fig. 8 with wider tolerances being specified for the three objectives. As might be expected, this admits more solutions and as Fig. 9 shows, there are three nondominated solutions within the specified vector $\xi$ . Comparing solution 1 and 2, it appears that higher availability has been achieved in 2 at the expense of weighted response time. Alternatively, a high availability has been achieved in 3 compared to 1 by sacrificing cost and response time. If these aggregate figures do not seem acceptable along any of the three dimensions, the designer always has the option of specifying a wider tolerance vector and proceeding from a more acceptable solution.

![](/api/attachments/CEV9BBUB/fulltext/images/3b47a16d4fd21dcd2096d47208122a1f55ec6888630a614567916992d2ec1ea6.jpg)  
Fig. 7. Generation of Nondominated Solutions that Meet the Vector $\xi$ .  
Fig. 8. Designer Specifies Wider Deviations to Examine More Alternatives.

In Fig. 10–12 the designer instead, opts to examine the details of solution 2 and 3 before proceeding. This comparison has resulted in his choosing solution 2 as the starting point for further search. Note that since solutions 2 and 3 do not dominate each other, the DSS has no mechanism to choose between them. This choice is based on informed judgment of the designer. In this particular iteration, the choice was influenced by the lower response time for solution 2. The observation that solution 3 had worse response time in spite of multiple copies of a file, further prompted the choice of solution 2. Since multiple file copies have attendant update costs, it may be desirable to avoid them as long as the response time does not suffer excessively. The session continues in Fig. 13–16.

## 5. Alternate Solution Methodologies

Since quantitative models for DCS design abound in the literature, it is only reasonable that our approach can be contrasted with existing ones. The first major difference is that these models admit single criteria [9–11]. Thus, one of the three objectives chosen for our session would have to be picked as this single criterion while the other two could be included as constraints. For instance, the formulation could read:

<table><tr><td colspan="4">There are 3 Non-dominated solutionsDo you want to see solutions or specify new deviation&#x27; on objectives and start a new iteration</td></tr><tr><td colspan="4">Input 1. to see solutions2. to specify new deviations</td></tr><tr><td colspan="4">&gt;1</td></tr><tr><td colspan="4">THE VALUES OF OBJECTIVE FUNCTIONS ARE</td></tr><tr><td>Solution No</td><td>Total Cost</td><td>Weighted Availability</td><td>Weighted Response time</td></tr><tr><td>1</td><td>3797450.00.</td><td>96500</td><td>0.57</td></tr><tr><td>2</td><td>3797450.00.</td><td>98000</td><td>0.60</td></tr><tr><td>3</td><td>4029780.00.</td><td>98950</td><td>1.14</td></tr><tr><td colspan="4">Please note numbers of the solution which are interesting</td></tr><tr><td colspan="4">Do you want to see details of any solution listedIf yes input solution number else input 0</td></tr><tr><td colspan="4">&gt;2</td></tr></table>

Fig. 9. DSS generates Three Nondominated Solutions Meeting the Wider Tolerance Vector $\xi$ .

Maximize: {Weighted file availability}
Subject to: Total Network cost $\leq C_{N}$ Average Response time $\leq C_{R}$ {Structural Constraints}

or, alternatively,

$$
\begin{array}{l l} \text {Minimize:} & \{\text {Total Network Cost} \} \\ \text {Subject to:} & \{\text {Weight file availability} \} \geq W _ {\mathrm{F}} \\ & \{\text {Average response time} \} \leq C _ {\mathrm{R}} \\ & \{\text {Structural Constraints} \} \end{array}
$$

Typically, such formulations contain integer variables and various optimization techniques have been used to obtain solutions. However, there is no explicit recognition of trade-offs in these methods. The values of $W_{F}$ , $C_{N}$ , $C_{R}$ must be supplied and the solution consists of one set of values of the decision variables which optimize the single objective function. In order to achieve trade-offs, the problems can be resolved over and over again with different combinations of values for $W_{F}$ , $C_{R}$ , $C_{N}$ . This is not very systematic and is also likely to be inefficient since many inferior solutions can be examined (Inferior in the sense that the solutions are completely dominated by earlier ones). A procedure like exchange search, which eliminates dominated solutions, helps in achieving trade-offs. The process of specifying tolerance vectors ( $\xi$ ) and examination of nondominated solutions meeting these tolerances is a much more natural way to explore trade-offs in a systematic manner than resolving single criteria problems in a trial and error fashion.

<table><tr><td colspan="3">Non-Dominated Solution number 2</td></tr><tr><td colspan="3">Objective function values are</td></tr><tr><td colspan="3">Cost 3797450.00</td></tr><tr><td colspan="3">Availability 0.98000</td></tr><tr><td colspan="3">Response Time 0.60</td></tr><tr><td colspan="3">COMPUTER TYPE SELECTED</td></tr><tr><td>Node #</td><td>Computer Type</td><td>Cost</td></tr><tr><td>1</td><td>1</td><td>1000000.00</td></tr><tr><td>2</td><td>2</td><td>750000.00</td></tr><tr><td>3</td><td>2</td><td>750000.00</td></tr><tr><td>4</td><td>1</td><td>1000000.00</td></tr><tr><td colspan="3">Press 1 to continue and 2 to suspend printing</td></tr><tr><td colspan="3">&gt;1</td></tr><tr><td colspan="3">FILE ASSIGNMENT</td></tr><tr><td>Node #</td><td>File #</td><td></td></tr><tr><td>1</td><td>1,</td><td></td></tr><tr><td>2</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td></tr><tr><td>4</td><td>2, 3,</td><td></td></tr><tr><td>5</td><td></td><td></td></tr><tr><td colspan="3">Press 1 to continue and 2 to suspend printing</td></tr><tr><td colspan="3">&gt;1</td></tr></table>

Fig. 10. Details of Solution 2.

CHANNEL ASSIGNMENT MATRIX

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>.00</td><td>1200.00</td><td>.00</td><td>.00</td><td>1200.00</td></tr><tr><td>2</td><td>1200.00</td><td>.00</td><td>4800.00</td><td>1200.00</td><td>.00</td></tr><tr><td>3</td><td>.00</td><td>4800.00</td><td>.00</td><td>4800.00</td><td>.00</td></tr><tr><td>4</td><td>.00</td><td>1200.00</td><td>4800.00</td><td>.00</td><td>9600.00</td></tr><tr><td>5</td><td>1200.00</td><td>.00</td><td>.00</td><td>9600.00</td><td>.00</td></tr></table>

Do you want to see details of any solution listed
If yet input solution number else input 0

>3

Non-Dominated solution number 3

Objective function values are

Cost 4029780.00

Availability .98950

Response Time 1.14

COMPUTER TYPE SELECTED

<table><tr><td>Node #</td><td>Computer Type</td><td>Cost</td></tr><tr><td>1</td><td>1</td><td>1000000.00</td></tr><tr><td>2</td><td>1</td><td>1000000.00</td></tr><tr><td>3</td><td>2</td><td>750000.00</td></tr><tr><td>5</td><td>1</td><td>1000000.00</td></tr></table>

Press 1 to continue and 2 to suspend printing

<table><tr><td>&gt;1</td></tr></table>

Fig. 11. Designer Examines Details of Nondominated Solution 3 at this Point.

<table><tr><td colspan="2">FILE ASSIGNMENT</td></tr><tr><td>Node #</td><td>File #</td></tr><tr><td>1</td><td>1,</td></tr><tr><td>2</td><td></td></tr><tr><td>3</td><td>1,</td></tr><tr><td>4</td><td></td></tr><tr><td>5</td><td>2, 3,</td></tr></table>

Press 1 to continue and 2 to suspend printing

>1

CHANNEL ASSIGNMENT MATRIX

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>.00</td><td>.00</td><td>1200.00</td><td>.00</td><td>.00</td></tr><tr><td>2</td><td>.00</td><td>.00</td><td>1200.00</td><td>4800.00</td><td>1200.00</td></tr><tr><td>3</td><td>1200.00</td><td>1200.00</td><td>.00</td><td>.00</td><td>4800.00</td></tr><tr><td>4</td><td>.00</td><td>4800.00</td><td>.00</td><td>.00</td><td>.00</td></tr><tr><td>5</td><td>.00</td><td>1200.00</td><td>4800.00</td><td>.00</td><td>.00</td></tr></table>

Do you want to see details of any solution listed
If yes input solution number else input 0

<table><tr><td>&gt;0</td></tr></table>

Fig. 12. Details of Nondominated Solution 3 (contd.)

Do you want to see solutions or specify new deviation' on objectives and start a new iteration

>2

From the solutions displayed select the solution which you like best. This will be starting solution for the next iteration. Please try to be consistent in your selection

INPUT: serial no. of solution you like or 0 to display the solutions again

>2

Do you want to try another iteration or store the above solution as the final solution

INPUT: S to store the above solution and stop N to try new iteration

> No

Please input the acceptable deviations on objective' function values

Current Cost is 3797450.00 Please input deviation > 3000000.

Fig. 13. DSS Prompts Designer to Specify New Deviations.

<table><tr><td>Current Weighted Availability is 0.9800Please input deviation ⇒</td></tr><tr><td>&gt;0.01</td></tr><tr><td>Current weighted response time is .60Please input deviation ⇒</td></tr><tr><td>&gt;120.0</td></tr><tr><td>DEVIATIONS SPECIFIED ARE</td></tr><tr><td>Cost 3000000.00</td></tr><tr><td>Availability .01000</td></tr><tr><td>Response Time 120.00</td></tr><tr><td>Do you want to change any of these</td></tr><tr><td>There are 2 Non-dominated solutionsDo you want to see solutions or specify new deviation' on objectives and start a new iteration</td></tr><tr><td>Input 1. to see solutions2. to specify new deviation</td></tr><tr><td>&gt;1</td></tr></table>

<table><tr><td colspan="4">THE VALUES OF OBJECTIVE FUNCTIONS ARE</td></tr><tr><td>Solution No</td><td>Total Cost</td><td>Weighted Availability</td><td>Weighted Response time</td></tr><tr><td>1</td><td>3797450.00</td><td>.98000</td><td>.60</td></tr><tr><td>2</td><td>4029780.00</td><td>.98980</td><td>1.94</td></tr><tr><td colspan="4">Please note numbers of the solution which are interesting</td></tr></table>

FILE ASSIGNMENTS

<table><tr><td>Node #</td><td>File #</td></tr><tr><td>1</td><td>1,</td></tr><tr><td>2</td><td>1,</td></tr><tr><td>3</td><td></td></tr><tr><td>4</td><td></td></tr><tr><td>5</td><td>2, 3.</td></tr><tr><td colspan="2">Press 1 to continue and 2 to suspend printing</td></tr><tr><td>&gt;1</td><td></td></tr></table>

Fig. 15. Designer Examines Details of One of the Solutions.

Fig. 14. DSS Generates New Nondominated Solutions.

<table><tr><td colspan="6">CHANNEL ASSIGNMENT MATRIX</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>.00</td><td>.00</td><td>1200.00</td><td>.00</td><td>.00</td></tr><tr><td>2</td><td>.00</td><td>.00</td><td>1200.00</td><td>4800.00</td><td>1200.00</td></tr><tr><td>3</td><td>1200.00</td><td>1200.00</td><td>.00</td><td>.00</td><td>4800.00</td></tr><tr><td>4</td><td>.00</td><td>4800.00</td><td>.00</td><td>.00</td><td>.00</td></tr><tr><td>5</td><td>.00</td><td>1200.00</td><td>4800.00</td><td>.00</td><td>.00</td></tr></table>

Do you want to see details of any solution listed If yes input solution number else input 0

Do you want to see details of any solution listed
If yes input solution number else input 0

> 2

Non-Dominated solution number 2

Objective function values are

<table><tr><td colspan="3">COMPUTER TYPE SELECTED</td></tr><tr><td>Node #</td><td>Computer Type</td><td>Cost</td></tr><tr><td>1</td><td>1</td><td>1000000.00</td></tr><tr><td>2</td><td>1</td><td>1000000.00</td></tr><tr><td>3</td><td>2</td><td>750000.00</td></tr><tr><td>5</td><td>1</td><td>1000000.00</td></tr></table>

Press 1 to continue and 2 to suspend printing  
Fig. 16. Designer Stores the last Chosen Solution and Terminates.

Cost 4029780.00

Availability .98980

Response Time 194

>0

Do you want to see solutions or specify new deviation' on objectives and start a new iteration

Input 1. to see solutions

2. to specify new deviation.

From the solutions displayed select the solution which you like best. This will be starting solution for the next iteration. Please try to be consistent in your selection

INPUT: serial no. of solution you like or 0 to display the solutions again

Do you want to try another iteration or store the above solution as the final solution

INPUT: S to store the above solution and stop N to try new iteration

## 6. Conclusions

A prototype DSS for DCS design has been presented. It is currently operational on a UNIVAC 1100 and an IBM PC AT. The underlying methodology stresses the systematic exploration of alternative solutions in the presence of multiple conflicting objectives. It combines quantitative model execution for structured parts of the design together with the designer's informed judgement on those aspects which are not easily quantified or are qualitative in nature. The process of making trade-offs is made systematic and efficient by presenting only Pareto-optimal alternatives to choose from. While it is clear that all aspects of DCS design are not quantifiable, it is useful to apply quantitative models to the extent possible, and apply judgement thereafter.

As noted earlier, an alternative to multicriteria modelling is the repeated execution of single criteria models. There does not appear to be a systematic method of approaching the latter. Even sensitivity analysis falls short. Both single and multiple criteria models are affected by the actual formulation, which in turn is influenced by the judgement and experience of the designer. The extra cost of using multicriteria techniques is that they currently require appreciably more storage than single criteria techniques and seem to converge more slowly. The benefits of the former have been noted throughout the paper and should become more attractive as the solution techniques improve.

## References

[1] Dutta, A. and H.K. Jain, Distributed Computer Systems Design: A Multicriteria Methodology, working paper, Graduate School of Management, University of Rochester, Rochester NY (Dec. 1983).

[2] Ignizio, J.P. D.F. Palmer and C.M. Murphy, A Multicriteria Approach to Super System Architecture Definition, IEEE Trans. on Computers C31 (May 1982) 410–418.

[3] Zionts, S., Multiple Criteria Decision Making: An Overview and General Approach, Working Ppaer No. 545, School of Management, SUNY at Buffalo, Buffalo NY (1980).

[4] Spath, H., Computational Experiences with the Exchange Method, Eur. J. Operations Research No 1. (1977) 23–31.

[5] Mahmoud, S., and J.S. Riordan, Optimal Allocation of Resources in Distributed Information Networks, ACM Trans. Database Systems Vol. 1, No. 1, (1976) 66–78.

[6] Tanenbaum, A.S., Computer Networks. pp. 196–214 (Prentice Hall, Englewood Cliffs NY, 1981).

[7] Santianarayana, A., A Unified Formula for Analysis of Some Network Reliability Problems, IEEE Trans. Reliability R-31 No. 1. (April 1982) 23–31.

[8] Ball, M.O. and J. Provan, Calculating Bounds on Reachability and Connectedness in Stochastic Networks, Networks 13 (1983) 258–278.

[9] Chen, P. and J. Akoka, Optimal Design of Distributed Information Systems, IEEE Trans. Computers, C-29 (1980) 1068–1080.

[10] Casey, R.G., Allocation of Copies of a File in an Information Network, AFIPS Conference Proceedings SJCC 40 (1972) 617–625.

[11] Irani, K.B. and N.G. Khabaaz, A Methodology for the DEsign of Communication Networks and the Distribution of Data in Distributed Super Computer Systems. IEEE Trans. Computers C-31 (1982) 419–434.
