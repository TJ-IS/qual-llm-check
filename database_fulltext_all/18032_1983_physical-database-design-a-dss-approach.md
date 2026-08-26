---
otero_id: 18032
otero_key: "BZFXTZBV"
title: "Physical database design: A DSS approach"
authors: "J.V. Carlis; S.T. March; G.W. Dickson"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90008-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Gary W. Dickson is Professor of MIS in the Department of Management Sciences at the University of Minnesota. He has published previously in Information & Management and has just retired as Founding Senior Editor of the MIS Quarterly.

# Physical Database Design: A DSS Approach

J.V. Carlis

Dept. of Computer Science, University of Minnesota, 136 Lind Hall, 207 Church Street S.E., Minneapolis, MN 55455, USA

## and

S.T. March and G.W. Dickson

Dept. of Management Sciences, University of Minnesota, School of Management, 271 19th Avenue South, Minneapolis, MN 55455, USA

This paper presents a working decision support system for use in the physical design of a database. Physical database design, a structured decision problem, lends itself to a decision support approach because closed form algorithms are computationally infeasible. The paper describes the physical database design problem, presents an overview of a software system for use in solving this problem, and evaluates the use of the system in solving a sample problem.

Keywords: Database, Physical Design, Decision Support System, Database Administration.

![](/api/attachments/BZFXTZBV/fulltext/images/c3da8d29f7f8775014b04869e99ccf1bab0ad80d66cad6a761941e3c70c82dd0.jpg)

Salvatore T. March is an Assistant Professor of MIS in the Department of Management Sciences at the University of Minnesota. He received his Ph.D. in Operations Research from Cornell University. He has published articles on database design in Transactions on Database Systems, Computing Surveys and ACM SIGMOD Conference Proceedings.

## 1. Introduction

Decision support systems (DSS), although a relatively recent phenomenon, have been applied in a variety of settings. Corporate planning [22], the medical area [6], the determination of advertising budgets [17], and personnel administration [1,7] are but a few examples of areas of DSS applications. In each of these instances a DSS approach has been adopted because the problems inherent in these situations are largely unstructured (or at least semi-structured). The decision support system has been an interactive computer based system which has helped the decision maker by providing data and models for application in the problem solving process [4,31].

There is another related setting in which a decision support approach is very appropriate. This is a situation in which the decision is structured and a single decision criterion is present (say, minimum cost) but no analytical optimization algorithm exists and there are too many alternative solutions to test them all in a feasible time period. The well known police beat allocation problem addressed by Carlson and his colleagues [5] is such a situation (at least for a given decision criterion). The travelling salesman problem has been similarly addressed in the Operations Research literature [12].

![](/api/attachments/BZFXTZBV/fulltext/images/a38b568eba8de9779e9e5247fac9de6a9aa6deed9504003e24e907c7cd80b439.jpg)  
John V. Carlis is an Assistant Professor of Computer Science at the University of Minnesota. He received his Ph.D. in MIS from the University of Minnesota. He has published in Computing Surveys.

Another problem having these characteristics is that of the design of a large physical database. Theoretically the designer, call this person the Data Base Administrator (DBA), can choose a design which minimizes the total operating cost over some time period. This can be done by evaluating all possible combinations of design parameters and choosing the one having the lowest cost. Unfortunately, even a modestly sized problem has so many possible combinations that a manual approach is infeasible.

In such cases, a computer is frequently employed to facilitate the evaluation process. Here again, however, the sheer number of solution alternatives makes even this approach infeasible. A solution to the small, sample problem which will be discussed in this paper, for example, is estimated to take 13 centuries on the CDC Cyber 74 computer to evaluate all possible combinations of solution (design) parameters. A “real world” problem which is being addressed by the authors for the U.S. Navy [16] is conservatively estimated to require $10^{18}$ centuries of time on the same computer system for its solution if an enumerative procedure was employed. An approach to the solution of problems of this type is to develop a decision support system to assist a human decision maker in arriving at a “good” solution to the problem within a reasonable expenditure of computer and human resources.

This paper describes how a decision support approach was applied to the problem of physical database design. This approach has been suggested by Gambino and Gerritsen [8] and by Hoffer [13], but up until now a fully functioning system has not been implemented. The following section describes the nature of the problem and the decision parameters involved in its solution. The next section presents an overview of the solution procedure with emphasis on those aspects having DSS properties. The concluding section evaluates the efficiency and effectiveness of the DSS approach in this area of application.

## 2. The Database Design Problem

Database design is a challenging task. Because of the size and complexity of the problem and interdependence among various aspects of the design, the best data organization is seldom obvious. Design alternatives which are quite efficient may also be complex, requiring deep analysis and substantial development efforts. Unfortunately, such designs may never even be considered due to a lack of knowledge and/or expertise on the part of the designer. As a result, inappropriate designs are often adopted with concomitant operating inefficiencies and poor performance [21,29].

A myriad of different data organizations can satisfy a given set of required uses. Evaluating the performance of even one design requires thousands of calculations involving such factors as:

1. Volume and volatility of the data,

2. Characteristics of data retrieval,

3. Physical equipment attributes,

4. Data redundancy,

5. Intrinsic structure of data.

It should also be noted that design performance has several measures (e.g., access time, costs, storage requirements, and complexity), many of which can be in conflict.

Because of the large number of design alternatives and the complexity of evaluating their performance, the selection of an optimal or nearly optimal physical design is extremely difficult. The results of “poor” or inappropriate database designs are, however, quite obvious: excessive cost to organizations in terms of poor system performance or computer resource requirements and, in some cases, avoidance of database applications because of perceived impossibility. In order to appreciate the complexity of the database design process, an overview of the process is in order.

## 2.1. The Database Design Process

For any information system there are two levels of database design: logical and physical [15,24,34]. At the logical level, the information requirements of the user community are integrated and a global logical database structure is developed. This logical structure must support the individual user views of the data so that the information requirements of each user can be met. It must do so, however, in a manner which is independent of the physical structures which will be used to support it. That is, the logical level describes WHAT information and processing must be supported; the physical level describes HOW these information and processing requirements will be supported. There are a large number of alternative physical structures by which the logical structures can be supported. During physical database design, these alternative physical structures must be evaluated and an appropriate physical structure selected.

This article addresses physical database design assuming that logical database design has been accomplished. As illustrated in Fig. 1 the process of physical database design has three inputs and one output. The inputs are:

1. Data description: Specification of the structure and volume of the data contained in the database. It is described by concepts such as entities, attributes, relationships, identifiers, cardinality, etc.

2. Uses of data: Specification of retrieval and update activities including report content, order, frequency, etc.

3. Computer system environment: Specification of the computer architecture including such factors as channel transfer rate, disk access times, etc.

The output of the process is a database design characterized by a grouping of elementary data items into records (types) and a set of access paths (i.e., algorithms and system data) which are used to store, retrieve, and maintain the data. The process chooses a design which will yield a good performance when implemented where performance is measured by the sum of storage, retrieval, and maintenance costs.

The inputs to the process are assumed to be known and available. The data description and the uses of data both come from the logical database design process. The computer system environment comes from the given characteristics of present or planned equipment. The methods available for logical database design are primitive and the determination of the logical problem is difficult (see [15]). However, much research is focused on the process of “problem definition” or “information requirements analysis” (see [9,23,26,27,32,33]) and progress in this area is being made. The result of this process is a logical description of the problem which specifies the structure and volume of the data in the database as well as the uses of this data.

Fig. 2 shows the logical data structure of a sample problem involving workers within an organization. The graphical representation employed (one of several available methods) is based upon Senko's "infological model" [28]. This model is based upon binary relationships. A binary relationship characterizes an association between exactly two entities. Each entity in a relationship both describes and is described by the other entity in the relationship. Therefore each relationship has two relationship descriptors, one describing each entity in the relationship. The relationship between EMPLOYEE and EDUCATION, for example, has both EDUCATION-OF-EMPLOYEE and EMPLOYEE-OF-EDUCATION relationship descriptors. Note that when there are multiple relationships connecting entities, labels are used to clarify the meaning. For example, there are two relationships between DEPARTMENT and EMPLOYEE. The unlabelled relationship connects EMPLOYEES and the DEPARTMENTS in which they work. The labelled relationship, DEPT-MGR, connects DEPARTMENTS and the EMPLOYEES who manage them. Tables 1–3 show partial listing of other types of input data describing the volume and uses of the data. The characteristics of the computer environment are given in Table 4.

![](/api/attachments/BZFXTZBV/fulltext/images/46303eec60a7b3ea444ae2c1da9805e105cae1fabe09a39e8bccd63a22147862.jpg)  
Fig. 1. The Physical Database Design Process.

![](/api/attachments/BZFXTZBV/fulltext/images/6cb8d4a702bac0e8d2f5e594746eeef47cbadedd52bdbea94924c156742708f0.jpg)  
Fig. 2. Logical Data Structure of Sample Problem involving Workers within an Organization.

From this type of problem description, the designer (DBA) must select a good physical level design which satisfies all of these logical level requirements. The logical content of the database must be organized into datasets composed of record instances at the physical level, retrievals must be supported by access paths and updates to the database must be accommodated via some type of storage space maintenance mechanisms. A single dataset with its associated access paths and maintenance mechanisms we call a file organization. A

Table 1  
Data Description and Use (Partially Shown)

<table><tr><td>Entity Descriptor</td><td>Identifier</td><td>Average Length (Characters)</td></tr><tr><td colspan="3">Department</td></tr><tr><td>Dept-no</td><td>Dept-no</td><td>4</td></tr><tr><td>Dept-name</td><td></td><td>30</td></tr><tr><td colspan="3">Address</td></tr><tr><td>City-name</td><td>City-name</td><td>20</td></tr><tr><td>State-name</td><td>State-name</td><td>2</td></tr><tr><td colspan="3">Employee</td></tr><tr><td>Emp-no</td><td>Emp-no</td><td>10</td></tr><tr><td>SSN</td><td></td><td>9</td></tr><tr><td>Emp-name</td><td></td><td>30</td></tr><tr><td>Salary</td><td></td><td>10</td></tr></table>

Table 2  
Data Volume and Update

<table><tr><td>Entity</td><td>Quantity</td><td>Additions/ Month</td><td>Deletions/ Month</td><td>Modifications/ Month</td></tr><tr><td>Department</td><td>150</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Employees</td><td>30,000</td><td>500</td><td>500</td><td>500</td></tr><tr><td>Assignments</td><td>60,000</td><td>1,500</td><td>1,200</td><td>5,000</td></tr></table>

## Table 3

## Typical Reports

\- Departments and their employees, ordered by department numbers then by employee name.

\- Assignments ordered by employee.

\- Employees in the Shipping Department ordered by employee name.

## Table 4

Computer System and Operating Environment Description.

<table><tr><td>Random Access Time</td><td>43.3 milliseconds</td></tr><tr><td>Local Access Time</td><td>36.3 milliseconds</td></tr><tr><td>Data Transfer Rate</td><td>1.13 MB/second</td></tr><tr><td>Length of a Memory Block</td><td>13030 characters</td></tr><tr><td>Memory Blocks per Locality</td><td>19</td></tr><tr><td>Length of a Memory Pointer</td><td>4 characters</td></tr><tr><td>Maximum Sort/Merge Order</td><td>2</td></tr><tr><td>Cost of Storage</td><td>$.68/locality-month</td></tr><tr><td>Cost of Retrieval Time</td><td>$.01/second</td></tr><tr><td>Cost of Maintenance Time</td><td>$.01/second</td></tr><tr><td>Cost of Buffer Space</td><td>$2.27 × 10/char-sec</td></tr><tr><td>Expected Life</td><td>12 months</td></tr></table>

physical database consists of a set of interconnected file organizations. Thus the DBA, must specify the following types of design parameters:

1. Some number of records (types), the union of which covers all elements of the logical data structure - each record defines the content of a file organization (its dataset);

2. For each file organization thus defined:

a. Record formats describing the grouping of data items into record segments (for efficiency purposes "smaller, high use" data items may be stored on primary segments while "larger, low use" data items are stored on secondary segments);

b. A dominant access path which establishes the ordering and positioning of record instances;

c. Auxiliary (secondary) access paths which connect selected subsets of record instances;

d. Maintenance mechanisms - procedures and system data to manage storage space for update operations; and

3. Interconnections among file organizations (typically implemented by direct or symbolic pointers between record instances in different file organizations).

Many alternatives exist for each of the above. For example, the number of alternative records is exponential in the number of relationships and for each record the number of alternative record formats is exponential in the number of data items in that record. Clearly the solution space from which a design must be selected is enormous.

## 2.2. Design Complexity and the DSS Approach

The selection of an efficient physical database design must be based upon the logical structure of the data, its volume, the frequency with which it is updated, the formats and frequency with which it is retrieved, and the access and cost characteristics of the media on which it is stored. All these parameters affect system performance, measured by storage and processing costs, in inter-dependent and complex ways.

Consider the following example, Suppose two different users need the information about the entity, ASSIGNMENT (from Fig. 2), but need it in different orders. Ordering ASSIGNMENT by PROJECT-OF-ASSIGNMENT may yield fast access for one user but it may be very slow for another. Ordering ASSIGNMENT by EMPLOYEE-OF-ASSIGNMENT may produce opposite results. One solution is to keep two copies of the record instances, one in each order. This would produce fast access but high storage and update costs. Another possibility the DBA could choose would be to order ASSIGNMENT by some other criterion (e.g., to reduce update costs) and form indexes according to PROJECT and EMPLOYEE.

Other solutions could be chosen by the DBA, even for this simple illustration. Many more possibilities exist as the problem complexity expands. The question is – how is the DBA to pick a set of design parameters that has optimal (or nearly optimal) performance and cost from among the vast array of possibilities?

We suggest that the DBA can make these choices more intelligently if supported by a machine system that (1) performs calculations to aid in the evaluation of solution alternatives (2) contains mechanisms which reduce the size of the solution space and (3) helps to structure the solution process. In terms of the well known Simon model of decision making [30], the DBA needs machine assistance in the phases involving design and choice. The first phase, intelligence, which deals with searching the environment for conditions calling for a decision is part of the logical database design process and is outside of the scope of this research. Design (developing and analyzing possible courses of action) and choice (selecting a course of action) are the phases of decision making addressed by this research.

Sprague [31] suggests that decision support systems:

\- combine the use of models and analytic techniques with traditional data access functions;

\- focus on features which make them easy to use by non-computer people in an interactive mode; and

\- emphasize flexibility and adaptability to accommodate changes in the environment and the decision making approach of the user.

The Information System Design Optimization System (ISDOS) is an early example of this type of system [32]. The main contribution of this work, however, is in the area of requirements determination and documentation rather than system design [33]. The Data Base Design System (DBDS), which will be described in the next section, is also a system of this type, but specifically focused on database design. The DBA interacts with the system in an iterative manner at several stages in the problem solving process. The interaction allows human judgment to be used to reduce the solution space. Additionally, the DBDS contains heuristics which further reduce the solution space. Finally, imbedded optimization models are used where they are appropriate to solve design sub-problems as encountered by the system or as posed by the DBA. The Data Base Design System emphasizes flexibility to explore solution sensitivity and can adapt to new requirements coming from the environment or the DBA.

## 3. The Database Design System

To date, traditional mathematical optimization techniques have not been successfully applied to the global solution of the physical database design problem. The problem contains integer decision variables, nonlinear constraints, and discontinuous objective functions. In addition, problem and solution characteristics affect system performance in such complex ways that they defy exact analysis. Furthermore, there are many nonquantifiable factors which must be considered. Thus, in order to guarantee the selection of a globally optimal design, all possible combinations of model parameters would have to be evaluated. Unfortunately, as discussed above, the number of possible design alternatives is so large that, even with an automated design evaluator, such a bruteforce approach is computationally intractable. Therefore, as an alternative, a decision support system approach has been adopted.

Gambino and Gerritsen [8] and Hoffer [13] suggest the utility of a DSS approach to the solution of the physical database design problem. Gerritsen [10], in fact, developed a DSS for physical database design. This system is, however, limited in its ability to model logical data structures and physical access paths; furthermore, it only evaluates designs posed by the DBA in contrast to optimizing parts of the design.

The database design methodology described below goes well beyond previous efforts in this area (e.g., [28]). The methodology provides: (1) a multiple level descriptive model of the database design problem space and its solution space (see [3]) and (2) a software system which supports a DBA in the task of database design.

Together, a DBA and the software form a person/machine system which takes advantage of both the intuition and experience of a DBA (per-

![](/api/attachments/BZFXTZBV/fulltext/images/6b0db0e282d648ef63ed25f743829febc512e7321bdb40644b1da9d273ec0e88.jpg)  
Fig. 3. The Major Modules of the Design System and the Flow of Information among them.

son) as well as the computational capabilities of modern computer systems. The DBA must formulate the problem and create a tabularized problem description expressed in the logical level of the descriptive model (see Table 1-3) for input to the design system software. The software (machine) includes a number of heuristic as well as optimization and evaluation procedures which automati cally generate “good” physical database designs and/or evaluate particular designs suggested by the DBA. These procedures are executed under the control of the DBA and interact with the DBA in order to produce an efficient physical database design expressed in the physical level of the descriptive model.

Fig. 2 shows the four major modules of the design system, (FORM, CONVERT, DESIGN, and SELECT) and the flow of information among them. Input to the system is: (1) a statement of the information requirements of the user community including a tabularized description of the logical data structure (LDS), data volumes and retrieval and update characteristics as discussed earlier and, (2) commands and constraints, e.g., controlling the level of detail of the output produced by the system, and/or dictating generic types of solutions to be considered (record structures, access paths, etc.), or specifying partial solutions (records, individual access paths for specific retrievals, etc.). Output from the system is a database design and performance estimates for that design.

The operation of the design system is briefly described below (for a more detailed discussion of the exact nature of the human interface and the procedures used by the various modules, the reader is directed to [2]).

## 31 FORM

FORM creates sets of records (types) for which file organizations will be designed. Each set contains or "covers" all of the logical data structure; each record covers one or more entities. We restrict the formation of records as follows:

a. all instances of a record are in the same file organization;

b. all attributes of an entity are in the same record:

c. relationship descriptors are represented by one of five representations: symbolic pointer, direct pointer, both symbolic and direct pointers, absorption (repeating groups of attributes or relationship descriptors) and no representation.

These five representations allow us to bound the computing task facing FORM. If there are NE entities and NR relationships then an upper bound on the number of records and therefore on the computing done by the design software is N\*5\*\* (2\*NR) (or NE\*25\*\*NR). This bound is large even for small values of NR. To reduce the computational burden we use these techniques:

a. Limit representations. Not all representations will be efficient. FORM has embedded within it heuristics (see [2]) which will eliminate most of the possible relationship representations. The heuristics lower the upper bound to NE\*3\*\*NR, which still results in a large number of records. The DBA can constrain the set of records generated by selectively overriding the heuristics and suggesting one of several representations (based on, for example, company policy, DBMS constraints, and knowledge about the problem, perhaps anticipating future needs) for one or more relationships.

b. Identify subproblems. Using the above limited representations, FORM searches for subproblems, called connected graphs (of entities). Relationships between entities in different connected graphs have exactly one (non-absorbing) representation while those between entities in the same connected graph may have several possible representations. Connected graphs define subproblems because the cost of a file organization depends on which representations are chosen for intra-connected graph relationships but not on which are chosen for inter-connected graph relationships (the representation for each inter-connected graph relationship is fixed by, definition). If several connected graphs are constructed then the upper bound is significantly reduced; it becomes a sum of products. Let NCG be the number of connected graphs, NECG, be the number of entities in the $i$ th connected graph, NRCG, be the number of relationships in the $i$ th connected graph, and NREP, be the number of representations for the $j$ th relationship in the $i$ th connected graph. Then the upper bound is:

$$
\sum_ {i = 1} ^ {\mathrm{NCG}} \mathrm{NECG} \prod_ {j = 1} ^ {\mathrm{NRCG},} \mathrm{NREP} _ {i j}.
$$

In general, the heuristics mentioned above will not produce multiple connected graphs; this must be done by constraints imposed by the DBA. By locating sets of entities which are “nearly” disconnected by the heuristics and specifying single representations for some number of relationships the DBA may produce multiple connected graphs and thus reduce the computational load faced by the DBDS. For large problems this interaction by the DBA is critical to assure computational feasibility.

c. Eliminate infeasible skeletons. FORM enumerates sets of records for connected graphs by systematically varying representations. We call each set of records a skeleton. A skeleton may be found to be infeasible and be discarded. Infeasibility is caused by representations dictating an entity's absorption into different records (violates the first restriction above) or dictating a circuit of absorption (has no root entity for the record).

d. Identify duplicate records. In enumerating skeletons, FORM will create records which appear in more than one skeleton. Processing is saved since FORM identifies these duplicates and a file organization is designed (i.e., DESIGN is executed) only once for each unique record. Later, in SELECT, skeleton costs are computed by summing the proper file organization costs.

## 3.2. CONVERT

CONVERT changes processing requirements expressed in the logical level model to accessing patterns of the records formed in (1) effectively yielding a set of file organization design problems. CONVERT is conceptually quite simple. The complex nature of retrieval activities and the existence of hierarchic physical records with multiple nested repeating groups, however, make the computations accomplished by this module rather complex.

## 3.3. DESIGN

DESIGN produces an efficient file organization design for each problem from (2). It has three major components: (a) a probabilistic model which evaluates the expected performance of alternative secondary memory management schemes (see [18]), (b) a bi-criterion $^{1}$ mathematical programming algorithm which selects an optimal assignment of data items to primary and secondary segments (Hammer and Niamir [11] and Hoffer and Severance [14] provide a motivation for and discussion of record segmentation), and (c) a branch and bound algorithm which selects an optimal set of data access paths from a set of potentially useful data access paths which are heuristically generated.

The heuristics for generating potentially useful data access paths are based upon the activity which must be satisfied. For example, auxiliary access paths such as lists and inverted lists are generated for all retrievals requiring less than ten percent of the data records. In addition, identifier searching access paths such as hashing, ISAM, full indexes, etc., are generated for all individual record retrievals and for update operations.

The proper execution of each component of DESIGN is dependent upon the results from each of the others. Therefore, DESIGN proceeds by heuristically generating an initial record segmentation (primary segments and secondary segments are set to equal lengths) and an initial set of data access paths (all retrievals requiring less than one percent of the data record instances are directly accessed, all others are sequentially accessed). The three components are then executed in sequence using the actual results from previously executed components. The record segmentation algorithm is then executed again using the access paths selected by the branch and bound algorithm. If the assignment of data items to primary and secondary segments has changed, then the procedure iterates once.

Again, the DBA may optionally constrain the solution space by specifying partial solutions to be considered or even complete solutions for evaluation only. This is accomplished, for example, by specifying a set of secondary memory management schemes to be evaluated and/or by modifying the set of potentially useful access paths heuristically generated. In addition, the record segmentation algorithm can be bypassed, further restricting the solution space to single segment records. Finally, specific access paths may be explicitly defined for all or some of the activity supported by the file organization.

Output from DESIGN is an efficient combination of a secondary memory management scheme, a record segmentation and a set of data access paths along with performance estimates for each file organization designed. Performance is measured by a composite of storage, retrieval, and maintenance costs. While the algorithms used to estimate the performance of file organization design are complex, the estimates are reasonably accurate. A simulation study demonstrated accuracy to within four percent for a realistic file organization design problem [19]. The contents and the form of the output produced by the system are discussed in the following section of this paper.

## 3.4. SELECT

SELECT picks a set of file organizations which efficiently meets the user information requirements. This module automatically selects the most efficient (lowest cost) set of file organizations from among those produced by DESIGN. The total cost of a database is the sum of the skeleton costs for each connected graph. A skeleton's cost is the sum of the costs of the file organization for each of the skeleton's records. Since there are many nonquantifiable factors which are not considered by DESIGN and which may have considerable impact on overall database performance, the DBA may use SELECT to display a set of alternatives produced by DESIGN and which are within some percent of the least cost design. The DBA may then subjectively evaluate this set of design alternatives and/or perform sensitivity analysis by varying critical design factors and iteratively executing the above modules prior to selecting a design for implementation.

FORM, CONVERT, DESIGN, and SELECT are the modules of our database design system (DBDS). They represent approximately 10,000 lines of executable FORTRAN code. The DBDS is operational on both IBM and Control Data computer systems with the test results presented in this paper being generated on the latter system (CDC Cyber 74).

While the design system cannot guarantee optimality, database designs produced by it are intuitively reasonable and substantially more efficient than simplistic designs (e.g., a set of flat files) generated for the same problem. In addition, designs are quickly produced and evaluated by the system, thus providing a vehicle for sensitivity analysis on critical design parameters and a benchmark against which to evaluate the performance of proposed alternative solutions.

## 4. Application of the Design System

With the authors serving as the human component (the DBA function), the system has been applied to a number of design problems. To illustrate a design solution, the problem described in Fig. 2 and Tables 1–3 was input to the system together with a description of the computer system and operating environment in which the database was to be implemented (see Table 4). With no additional input (i.e., using only the design heuristics described above), a database design was automatically generated in approximately 30 seconds

Table 5  
Assignment of Retrieval Activities

<table><tr><td>Retrieval</td><td>Retrieve From File Organization</td><td>Access Path</td><td>Retrievals Per Month</td><td>Retrieval Cost Per Month</td></tr><tr><td rowspan="2">1</td><td>1</td><td>1</td><td>5</td><td>$0.01</td></tr><tr><td>2</td><td>4</td><td>150</td><td>2.44</td></tr><tr><td rowspan="2">2</td><td>1</td><td>1</td><td>10</td><td>0.02</td></tr><tr><td>2</td><td>1</td><td>500</td><td>0.32</td></tr><tr><td>3</td><td>2</td><td>2</td><td>20</td><td>0.27</td></tr><tr><td>4</td><td>2</td><td>6</td><td>1</td><td>0.26</td></tr><tr><td>5</td><td>2</td><td>3</td><td>3000</td><td>2.26</td></tr><tr><td rowspan="2">6</td><td>2</td><td>5</td><td>18</td><td>0.29</td></tr><tr><td>3</td><td>1</td><td>2</td><td>0.01</td></tr><tr><td colspan="4">Total Retrieval Cost per Month</td><td>$ 5.88</td></tr><tr><td colspan="4">Total Fixed Cost per Month</td><td>4.23</td></tr><tr><td colspan="4">Total Operating Cost per Month</td><td>$10.11</td></tr></table>

![](/api/attachments/BZFXTZBV/fulltext/images/9ad952989b40a659199ad461bc27314ef1cc81b637b717bd7fd3bf91426b51cc.jpg)

```txt
FILE ORGANIZATION 1
Contains DEPARTMENT information:
DEPT-NO
DEPT-NAME
DEPT-BUDGET
MANAGER-OF-DEPARTMENT (EMP-NO)
ADDRESS-OF-DEPARTMENT (CITY,STATE)
```

<table><tr><td>Access Paths</td><td>Key Data Items</td><td>Selection Criteria</td><td>Fixed Costs (Storage and Maintenance)</td></tr><tr><td>1 Unordered Sequential File</td><td>None</td><td>All</td><td>$.05</td></tr><tr><td colspan="3"></td><td>$.05</td></tr></table>

```txt
FILE ORGANIZATION 2
Contains EMPLOYEE information:
EMP-NO
EMP-NAME
AGE
SEX
SOC-SEC-NO
DEPARTMENT-OF-EMPLOYEE (DEPT-NO)
EDUCATION-OF-EMPLOYEE ([DEGREE, GRADES]*)\nASSIGNMENT-OF-EMPLOYEE ([STATUS, PROJ-NO]*)\nADDRESS-OF-EMPLOYEE (CITY, STATE)
```

<table><tr><td>Access Paths</td><td>Key Data Items</td><td>Selection Criteria</td><td>Fixed Costs (Storage and Maintenance)</td></tr><tr><td>1 Hashed Full Index</td><td>EMP-NO</td><td>All</td><td>$1.83</td></tr><tr><td>2 ISAM</td><td>EMP-NAME</td><td>All</td><td>2.02</td></tr><tr><td>3 Hashing via a Scatter Table</td><td>EMP-NO</td><td>All</td><td>.04</td></tr><tr><td>4 Cellular I/L</td><td>DEPT-NO</td><td>All by Dept</td><td>.02</td></tr><tr><td>5 Cellular I/L</td><td>DEPT-NO</td><td>ALL by Proj</td><td>.01</td></tr><tr><td>6 File Scan</td><td>None</td><td>All</td><td>.00</td></tr><tr><td colspan="3"></td><td>$3.92</td></tr></table>

```txt
FILE ORGANIZATIONS 3
Contains PROJECT information:
PROJ-NO
PROJ-NAME
PROJ-BUDGET
MANAGER-OF-PROJECT (EMP-NO)
```

<table><tr><td>Access Paths</td><td>Key Data Items</td><td>Selection Criteria</td><td>Fixed Costs (Storage and Maintenance)</td></tr><tr><td>1 Unordered Sequential File</td><td>None</td><td>All</td><td>$.26</td></tr><tr><td colspan="3"></td><td>$.26</td></tr></table>

Fig. 4. A Database Design Summary. \*Note: The Notation [ ] indicates a Nested Repeating Group.

of computer time. The time is, of course, for one iteration by the DBA testing one combination of variables. This timing figure is drastically affected by the problem size. Since the illustrative problem used here is small, this figure is low. As can be imagined, a real problem of, say, ten times the size would take substantially more computer time. The judgment of the DBA is critical in controlling total computing time.

A summary of the database design selected and estimates for fixed storage and maintenance costs for each of its component file organizations are given in Fig. 4. Table 5 shows the assignment of retrieval activities to file organization access paths and summarizes total costs by file organization. The DBDS produces additional design and performance details which are omitted here.

The design system also provides a convenient means for comparing the performance of various design alternatives. For example, the solution selected by the design system has three file organizations, one of which (the employee record) is hierarchically structured (contains repeating groups for education and assignment). Clearly, a database containing only flat files (i.e., normalized relations) is simpler and more flexible (many extensions to the database content will not disturb the existing file organizations). In order to determine the operational cost of obtaining this design simplicity and added flexibility, the design system was invoked again and the solution space constrained to flat file representations (by limiting the relationship representations as discussed above). The resulting design and its costs are summarized in Table 6. Total monthly operational costs are seen to have increased by an order of magnitude from \$10 to \$111 per month. Provided with such performance estimates, a designer can more objectively decide if increased design complexity and its associated implementation costs are justified by significant savings in operating costs.

Table 6  
A Flat File Database Design

<table><tr><td>Retrieval</td><td>Retrieve From File Organization</td><td>Access Path</td><td>Retrievals per Month</td><td>Retrieval Cost per Month</td></tr><tr><td rowspan="2">1</td><td>DEPARTMENT</td><td>Unordered Sequential</td><td>5</td><td>$ 0.02</td></tr><tr><td>EMPLOYEE</td><td>Cellular I/L (DEPT-NO)</td><td>150</td><td>4.23</td></tr><tr><td rowspan="2">2</td><td>DEPARTMENT</td><td>Unordered Sequential</td><td>10</td><td>0.03</td></tr><tr><td>EMPLOYEE</td><td>Hashed Full Index (EMP-NO)</td><td>500</td><td>0.50</td></tr><tr><td rowspan="2">3</td><td>EMPLOYEE</td><td>ISAM (EMP-NO)</td><td>20</td><td>0.33</td></tr><tr><td>ASSIGNMENT</td><td>Cellular I/L (EMP-NO)</td><td>2000</td><td>12.20</td></tr><tr><td rowspan="3">4</td><td>EMPLOYEE</td><td>Scan</td><td>1</td><td>0.39</td></tr><tr><td>ASSIGNMFNT</td><td>Scan</td><td>2</td><td>0.06</td></tr><tr><td>EDUCATION</td><td>Cellular I/L (EMP-NO)</td><td>3000</td><td>21.97</td></tr><tr><td rowspan="2">5</td><td>EMPLOYEE</td><td>Hashed Full Index (EMP-NO)</td><td>3000</td><td>2.97</td></tr><tr><td>ASSIGNMENT</td><td>Cellular I/L (EMP-NO)</td><td>3000</td><td>25.55</td></tr><tr><td rowspan="2">6</td><td>ASSIGNMENT</td><td>Unordered Sequential</td><td>18</td><td>0.51</td></tr><tr><td>PROJECT</td><td>Unordered Sequential</td><td>2</td><td>0.01</td></tr><tr><td colspan="4">Total Retrieval Cost per Month</td><td>$ 68.77</td></tr><tr><td colspan="4">Total Fixed Cost per Month</td><td>42.41</td></tr><tr><td colspan="4">Total Operating Cost per Month</td><td>$111.18</td></tr></table>

## 41 Sensitivity Analysis

As discussed above, the design system requires an input a parametric description of the data, its uses and the computer system environment in which the database will be operated. The process of determining these parameters is ill defined and the problem description is likely inexact. Therefore a DBA is concerned with the sensitivity of the database design to fluctuations in these parameters. The design solution presented above is relatively stable for a number of variations in the problem parameters. We executed the DBDS for nine candidate sets of records and for each candidate we tried 20 different variations in the problem parameters. The parameters varied were: blocking factor (1 or 4 blocks/track); reorganization interval (between 6 and 36 months); device contention (random and local accesses were nearly the same, or widely different); and maintenance mechanisms (six different ones were employed).

The following results were observed.

1. The design software worked. The results were deemed reasonable by the authors.

2. The ranking of the candidate sets of records was stable across the variations in parameters. Thus, at least for this simple problem, the choice of records is the most important decision.

3. For the best candidate set of records the access paths were stable across variations of parameters with only minor exceptions.

4. Varying parameters primarily affected costs rather than structure,

a. A longer block has the effect of increasing costs for individual record retrieval, due to a longer block retrieval time, but of decreasing costs for scanning since the number of blocks which must be accessed is reduced.

b. A longer reorganization interval has the effect of increasing costs due to an increased use of overflow areas for updates.

c. Where there was contention for a device, the time for local access and, therefore its cost, was higher.

d. Maintenance mechanisms using direct pointers were found to be cheaper where there was little update.

This sensitivity analysis is typical of the kind of testing a DBA might do. Other parameters which might reasonably vary are the frequency of updates or retrievals, the number of entity instances, attribute lengths, relationship degrees, etc.

## 5. DSS Assessment and Future Directions

The Database Design System (DBDS) described in this paper is based upon the standard decision support system procedure of imbedded models and heuristics coupled with a human/machine interactive process. The division of labor between human (DBA) and machine (software) is as follows. The DBA must: (1) abstract the problem from the real world and express it in the form of the logical level descriptive model; (2) just simply constrain the solution space and execute the DBDS software (machine); and (3) subjectively evaluate the set of efficient database designs produced by the DBDS (machine) and select a design for implementation. The DBDS software (machine) quickly searches the constrained solution space for efficient database designs (by optimally solving various design subproblems) and/or evaluates subsets of the solution space as directed by the DBA.

The DBDS is a tool to support a DBA in the task of physical database design [16]. It facilitates the explicit specification of the design problem and greatly expands the number of design alternatives which can be considered for a particular design problem. Through an interactive interface it allows the DBA to restrict the types of solutions considered (e.g., for particular DBMS software), or to specify particular design components or even a complete design for comparison purposes.

As the retrieval and update activities of the user community evolve over time, the performance of a database design degrades. The DBDS can support a DBA in evaluating the benefits of redesigning an existing database by generating a new design for the current usage and evaluating the operational cost savings of the new design. The DBA must assess the cost of reloading the database and doing any necessary software modification.

The description of the Data Base Design System and the illustration of its application to a sample problem should be convincing evidence that this is indeed a DSS approach to attacking problems of physical database design. Our tests of the Data Base Design System indicate that this approach supports the selection of very good database designs with a reasonable use of computer and human resources. In addition, the system provides the opportunity for sensitivity testing needed to explore the physical database design problem and to fully support the evolution of the database design as the user requirements evolve. Thus, the DSS criteria of flexibility and adaptability are also met.

## References

[1] P. Berger and F. Edleman, "IRIS: A Transaction-Based DSS for Human Resources Management," Data Base (8:3), Winter, 1977, pp. 22–29.

[2] J.V. Carlis, An Investigation Into the Modeling and Design of Large, Logically Complex Multi-User Databases, Unpublished Ph.D. Dissertation, University of Minnesota, 1980.

[3] J.V. Carlis, and S.T. March, "A Multiple Level Descriptive Model for Expressing Logical Database Design Problems and Their Physical Solutions," MISRC Working Paper 81-10, University of Minnesota, March 1981.

[4] E.D. Carlson, "DSS Conference Overview," Data Base (8:3), Winter, 1977, p. 2.

[5] E.D. Carlson, B.F. Grace, and J. Sutton, "Case Studies of End User Requirements for Interactive Problem-Solving Systems," MIS Quarterly (1:1), March, 1977.

[6] R. Davis, "A DSS for Diagnosis and Therapy," Data Base (8:3), Winter. 1977, pp. 58–72.

[7] F. Edleman, "Managers, Computer Systems, and Productivity," Management Information Systems Quarterly (5:3), September, 1981, pp. 1-20.

[8] T.J. Gambino, and R. Gerritsen, "A Data Base Design Decision Support System," Proceedings of the Third International Conference on Very Large Databases, Tokyo, Japan. October, 1977, pp. 551–557.

[9] D. Gane, and T. Sarson, Structured Systems Analysis, Prentice-Hall, Englewood Cliffs, New Jersey, 1979.

[10] R Gerritsen, "A Preliminary System for the Design of DTBG Data Structures," Communications of the ACM (18-10), October, 1975, pp. 551-557.

[11] M Hammer, and B. Niamir, "A Heuristic Approach to Attribute Partitioning," Proceedings ACM SIGMOD, Boston, Massachusetts, June, 1979, pp. 93-100.

[12] A V. Hill. "An Experimental Comparison of Human Subjects and Heuristic Algorithm for the Traveling Salesman Problem". Journal of Operations Management, Vol. 2, No. 4, August, 1982.

[13] J. Hoffer. "Database Design Practices for Inverted Files," Information and Management (3), 1980, pp. 149-161.

[14] J.A. Hoffer and D.G. Severance, "The Use of Cluster Analysis in Physical Data Base Design," Proceedings of the International Conference on Very Large Data Bases, Framingham, Massachusetts, September, 1975, pp. 69–86.

[15] IBM 1978 New Orleans Database Design Workshop, IBM Technical Report Number RJ2554, IBM Corporation, San Jose, California, 1978.

[16] D Jefferson, "The Development and Application of Data Base Design Tools and Methodology." Proceedings of the Sixth International Conference on Very Large Databases, Montreal, Canada, October 1-3, 1980.

[17] J.D.C. Little, "Models and Managers: The Concept of a Decision Calculus," Management Science (16:8), April, 1980, pp. 466-485

[18] S. F. March, D.G. Severance, and M. Wilens, "Frame Memory: A Storage Architecture to Support Rapid Design and Implementation of Efficient Databases," ACM Transactions to Database Systems, (6:3) September, 1981, pp. 441-463.

[19] S T March, and D.G. Severance, "A Mathematical Modeling Approach to the Automatic Selection of Database Designs." Proceedings of the ACM SIGMOD, Austin, Texas, 1978, pp. 112-126.

[20] S. I. March, and D.G. Severance, "The Determination of Efficient Record Segmentations and Blocking Factors for

Shared Data Files," ACM TODS (2:3), September, 1977, pp. 279–296.

[21] J. Martin, Computer Data-Base Organization, Prentice-Hall, Englewood Cliffs, New Jersey, 1975.

[22] E.R. McLean, and T.F. Reising, "MAPP: A DSS for Financial Planning," Data Base (8:3), Winter, 1979, pp. 9–11.

[23] M.C. Munro, and B.R. Wheeler, "Planning Critical Success Factors and Management's Information Requirements," MIS Quarterly (4:4), December, 1980, pp. 27-38.

[24] S. Navathe, and Scholnick. "View Representation in Logical Database Design," SIGMOD Proceedings, Austin, Texas, 1978, pp. 114–156.

[25] J.F. Nunamaker, B.R. Konsynski, T. Ho, and C. Singer, "Computer-Aided Analysis and Design of Information Systems," CACM (19:12) December, 1976, pp. 674-687.

[26] J.R. Rockart, "Chief Executives Define Their Own Data Needs," Harvard Business Review (57:2), March-April, 1979, pp. 81-93.

[27] D.T. Ross, and K.E. Schoman, "Structured Analysis for Requirements Determination," IEEE Transactions on Software Engineering (3:1), January 1977, pp. 53–67.

[28] M.E. Senko, "Specification of Stored Data Structures and Desired Output Results in DIAM II with FORAL," Proceedings of the Conference on Very Large Data Bases, Framingham, Massachusetts, 1975, pp. 557-587.

[29] D.G. Severance, Some Generalized Modelling Structures for Use in Design of File Organizations, Ph.D. Dissertation, University of Michigan, 1972.

[30] H.A. Simon, The New Science of Management Decision, Harper and Row, Publishers, Inc., New York, 1960.

[31] R.J. Sprague, Jr. "A Framework for the Development of Decision Support," MIS Quarterly (4:4), December, 1980, pp. 1-26.

[32] D. Teichroew, and H. Sayani, "Automation of System Building," Datamation (17:3), August, 1971, pp. 25-30.

[33] D. Teichroew, and E.A. Hershey, "PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems", IEEE Transactions on Software Engineering (3:1), 1977, pp. 15–27.

[34] S.S. Yao, and S.B. Navathe, "An Integrated Approach to Logical Database Design", NYU Symposium on Database Design, New York University, New York, May 18-19, 1978, pp. 1-14.
