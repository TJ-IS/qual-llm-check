---
otero_id: 17711
otero_key: "FC4VTVX9"
title: "Constraint by example"
authors: "Levent V. Orman"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00019-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Constraint by example

Levent V. Orman \*

Cornell University, Malott Hall, Ithaca, NY 14853, USA

## Abstract

First order static database constraints are expressed as counterexamples, i.e., examples that violate the integrity of the database. Examples are data and as such they can be specified and stored as data, structured into database files for efficient search and retrieval, and enforced efficiently since enforcement reduces to data comparison between the constraints as example data and the database. To express all first order constraints as counterexamples, a new normal form for first order logic is created which, after some syntactic transformation, is amenable to storage in flat files, efficient search and retrieval, and efficient testing of models for validity. Such efficient management of constraints is likely to lead to the development of large constraint bases since constraints are useful in a variety of contexts such as:

1. Maintaining data quality by catching in real time and eliminating a wide variety of errors ranging from typing mistakes to complex semantic violations,

2. Enforcing data security by monitoring and authorizing access and modification to protected data,

3. Implementing semantic data models within the simpler and better understood environment of relational model, 4. Building model libraries where complex decision models can be described, stored, retrieved, and manipulated by using constraints that establish the logical relationships between their inputs and outputs.

Keywords: Database constraints; Integrity maintenance; Constraint representation and storage; First order logic

## 1. Constraints

Database constraints are logical statements that have to be obeyed by the data at all times $[1,2,8,16]$ . We restrict ourselves to first order logic, and a closed world database where all facts not in the database are assumed false. First order constraints are critical in policing the database and weeding out a great percentage of incorrect and inconsistent data. They are usually implemented as procedures to be executed against the database, and after each modification to the database. However, they slow down the database maintenance process considerably, and in realistic large numbers they can bring the system operations to a complete halt. Consequently, their execution is often delayed and done in batches, leading to long periods of time when the correctness and the consistency of the database cannot be guaranteed. The inefficiency of database constraints emanate from three sources:

1. The inherent difficulty of executing these complex procedures against large databases [16].

2. The need to check all constraints for every modification to the database, since there is no efficient method to structure and organize the constraints so that only a small number of relevant constraints could be identified and retrieved for testing after each database modification. The attempts to ameliorate this problem produced minor improvements. One approach involves clustering constraints with respect to the files they reference, since a transaction involving a file F can only impact the constraints that reference F [10]. Another approach involves declarative specification of constraints, and theorem proving techniques to locate the constraints that may match a term of the transaction. This approach requires all constraints to be brought into the main memory and tested for matching terms, since there is no effective storage structure for constraints to accomplish the term matching directly on the secondary storage devices [4,6,14].

3. The difficulty of maintaining the constraints themselves as they change over time, since their semantics is buried within procedures. Often they can only be changed by completely rewriting them. This problem is partially overcome by declarative specification of constraints; however, both declarative specifications and procedures have to be stored as text, and identifying and retrieving the constraints affected by a change in requirements is still a significant problem $[5,14]$ .

Expressing constraints as example data attacks all three problems simultaneously. Examples are intuitive to end users and can be specified easily without extensive professional help; examples can be stored as data, structured into database files, and retrieved efficiently; and finally they can be enforced efficiently since enforcement reduces to data comparison between constraints as example data and the database [17]. The major contribution of this approach, however, is in efficient storage and retrieval of database constraints. The other two objectives, end user specification and constraint execution, have already benefitted enormously from query languages and query optimization respectively, since constraints can be defined and executed as queries that return null [10], but efficient storage and retrieval remains a serious problem. Section 2 will introduce a flat notation for database constraints for storage in relational databases, and for retrieval using database query languages. Section 3 will develop algorithms for efficient retrieval of constraints relevant to each transaction, and their efficient enforcement to maintain integrity. Section 4 will extend the notation and the algorithms to ensure first order completeness so that all common database constraints are expressible. Section 5 will compare the efficiency of this approach to other existing methods and state the main conclusions.

## 2. Constraint by example

Constraints can be expressed as example data that violate the integrity of the database. Given the following relational database for a university environment:

STUDENT (name, dept)

COURSE (course#, dept)

REG (name, course#)

containing the names and departments of students, course# and departments of courses, and courses registered for by each student. Also given are the following database constraints:

C1: The students who take CS100 also take CS200.

C2: All CS students take all CS courses.

They can be expressed as examples violating the database as follows:

C1: A student $x$ takes CS100 but not CS200. REG(x, CS100), - REG(x, CS200)

C2: There is a CS student $x$ who does not take a CS course $y$ .

STUDENT(x, CS), COURSE(y, CS), -REG(x,y)

Clearly, variables such as x and y stand for unknown data items that would violate the integrity of the database if any data item existed to take their place.

Once the constraints are expressed as example data, they can be placed in a constraint base. The constraint base contains the same files and the same structure as the database except for a constraint# field attached to each file. Constraint# field contains a unique identifier for each constraint. The constraint base also contains negative files such as -REG. However, these negative files can be included in the positive files such as

REG by merely attaching a negative sign to the constraint# of those negative records. The constraint base for the above constraints is shown below where the constraint# field is separated only for visual appeal:

constraint# name dept constraint# course# dept constraint# name course#

$$
2 \quad \left[ \begin{array}{c c} & \\ \mathrm{x} & C S \\ & \end{array} \right] \quad 2 \quad \left[ \begin{array}{c c} & \\ \mathrm{y} & \mathrm{CS} \\ & \end{array} \right] \quad \begin{array}{c c} 1 & \\ - 1 & \\ - 2 & \end{array} \quad \left[ \begin{array}{c c} \mathrm{x} & \mathrm{Cs100} \\ \mathrm{x} & \mathrm{Cs200} \\ \mathrm{x} & \mathrm{y} \end{array} \right] \quad \text {STUDENT}
$$

The structure of the constraint base closely mirrors the structure of the database. Consequently, their management is similar, and any change in the data model is reflected in the database and the constraint base in exactly the same way. Moreover, irrelevant variables in the constraint base can be replaced with blank to improve readability. Similarly, the constraint specification can be slightly modified for users who do not need to see the schema, by allowing them to use attribute names instead of the position of the attribute. The language becomes less compact when attribute names are used, but the users have less to remember.

C1: REG.name = x, REG.course# = CS100,

\- REG.name = x, - REG.course# = CS200.
C2: STUDENT.name = x, STUDENT.dept = CS,
COURSE.course# = y, COURSE.dept = CS,
- REG.name = x, - REG.course# = y.

An alternative user oriented structure is a visually based table structure as in Query by Example [17]. The constraint language of this section is identical to that of Query by Example where a variable is viewed as an example (i.e., a constant whose value is unknown), and distinguished from constants through a syntactic mechanism. The difference from Query by Example is the existence of negative variables which stand for impossible examples, and they will be introduced in Section 4. Negative variables are different from negative records, since not only they do not exist, but they cannot exist. Negative variables make the language first order complete with a minimal number of constructs, where Query by Example had to introduce ad hoc constructs.

Database constraints are useful in a variety of contexts beyond simple error checking. Consequently, their use and significance are expected to rise as their management becomes more efficient, possibly paralleling the explosion in the use and significance of data in organizations, as its management became more efficient. Some general areas of impact are listed below with simple examples:

1. A general purpose constraint base is useful in maintaining data quality especially in statistical and managerial support databases. These databases are subject to a variety of error sources, and simple errors, if undetected, can propagate over time and corrupt them in unexpected areas. Anticipated types of errors can be prespecified and stored in a constraint base which allows the system to catch these errors in real time without the delays of periodic auditing, and without the corruption that may be caused by such delays [15]. A typical constraint of this type in the university environment is the requirement that all MIS students take MIS101, or the violation if an MIS student x does not take MIS101: STUDENT(x,MIS), - REG(x,MIS101). Another typical constraint is the requirement that all students take at least 12 credits, or the violation if a student takes less than 12 credits: REG(x,y),COURSE(y,c),SUM(c,x,s),s < 12 where SUM(c,x,s) states that the sum of all course credits c for a given student x is s. An alternative notation for end users is $\text{SUM}(c, x) \rightarrow s$ , but the notation for storage needs to be flat even if slightly unintuitive.

2. Database constraints are also useful in enforcing data security. Combined with log-files that monitor and record data access and modification, constraints can be specified to detect suspicious activity ranging from access to specific protected files to unauthorized modification of specific data values. A typical example in a university environment is to prevent students from accessing other students' registration records. Given a file LOG $(x,y,z)$ which captures access by user x to file y and record (with key value)z, a violation would be an access by student x to STUDENT file record z where z is a different student from x. STUDENT $(x,d)$ , LOG $(x, STUDENT, z)$ , $x \neq z$

3. Database constraints can be used to implement semantic data models $[1,2]$ within the relative simplicity of relational databases. Many semantic constructs can be expressed as simple relational constraints defined within the relational model of data as shown in the following examples:

3.1. Inclusion dependencies declare an entity type as a subtype of another entity type. These type-subtype hierarchies are the most common distinguishing characteristic of semantic data models, and they are sometimes referred to as ISA hierarchies. In the university environment, STUDENT entity type can have the subtypes GRAD(name, dept) and PART-TIME(name, dept) containing graduate and part-time students. The inclusion dependency declares all graduate and part-time students as students, or a violation occurs if a grad x is not a student, or a part-time student x is not a student. GRAD(x,\_), - STUDENT(x,\_)

PARTTIME(x, ), - STUDENT(x, )

3.2. Complete covering refers to a collection of subtypes completely covering their supertype. In the university environment GRAD and PARTTIME would provide a complete covering of STUDENT if all students belonged to one or both of those categories. In other words a violation would occur if a student was not grad and not part-time. STUDENT(x,y),

$$
- \operatorname{GRAD} (x, y), - \text { PARTTIME } (x, y)
$$

3.3. No overlap among the subtypes of a type simply declares them as mutually exclusive. GRAD and PARTTIME would be mutually exclusive if no grads were part-time, or a violation would occur if a grad was also part-time. GRAD(x,y),PARTTIME(x,y)

3.4. Aggregation and association dependencies require the entities forming the aggregation or association to be subtypes of other entity types. REG in the university example is an association between STUDENT and COURSE entity types, and hence the student attribute and the course attribute of REG are expected to be subtypes of STUDENT and COURSE respectively. A violation occurs when REG involves a student x not in STUDENT, or a course y not in COURSE.

$\operatorname {REG}(x,y), - \operatorname {STUDENT}(x,d)$

REG(x,y),- COURSE(y,d)

4. Database constraints can be used to specify statistical, optimization and organizational decision models at a high level of abstraction. Such specifications are useful in building and storing large organizational model libraries and maintaining and retrieving them using query languages. They are also useful in locating all models that are capable of solving specific problems by using logical inference with database constraints. Constraints serve this purpose by treating input and output of models as data, and capturing correct input-output relationships as data constraints. A simple example in the university environment is the determination of the largest class size as LARGEST(m), or a violation if the largest size m is not captured in LARGEST(m). REG(s,c), COUNT(s,c,t), MAX(t,m),

-LARGEST(m) where count $(s,c,t)$ states that the count of s for each c is t, and MAX(t,m) states that maximum of all t is m.

## 3. Constraint enforcement

In the constraint base environment, locating and retrieving the constraints relevant to a particular database transaction is a simple database operation. One only needs to search for the constraints that match the data records involved. The only assumption needed for matching is that the variables (such as x) match all constants. In a file with m attributes and n records and assuming a binary search for each attribute, at most $m \log_{2} n$ records need to be checked to find a match. This number can be improved even further by utilizing a multiattribute search technique [13].

Example: A transaction involving STUDENT(SMITH, CS) can only effect the constraint 2 since it matches only the student record STUDENT(x,CS). A transaction involving REG(SMITH,CS100) may effect constraints 1 and 2, since it matches the REG records REG(x,CS100) and REG(x,y).

The execution of constraints involves comparing the constraint base to the database to find a match indicating a violation of the database integrity. The violations can be detected by creating a violation file V for each constraint where V contains a column for each variable in the constraint, a positive record for each match between the positive records of the constraint base and the database; and a negative record for each match between the negative records of the constraint base and the database. Subtracting negative records from the positive records leaves only the violations in the V file. Each record in the V file is a violation of the database integrity.

Example: Given the following university database:

$$
\left[ \begin{array}{c c} \text {SMITH} & \text {CS} \\ \text {JONES} & \text {CS} \end{array} \right] \left[ \begin{array}{c c} \text {CS100} & \text {CS} \\ \text {CS200} & \text {CS} \end{array} \right] \left[ \begin{array}{c c} \text {SMITH} & \text {CS100} \\ \text {SMITH} & \text {CS200} \\ \text {JONES} & \text {CS100} \end{array} \right]
$$

## STUDENT COURSE

REG

Constraint Cl is REG(x,CS100),

\- REG(x,CS200). The corresponding Vl is:

<table><tr><td>1</td><td> $\begin{bmatrix} x \\ SMITH \\ JONES \\ SMITH \\ V1 \end{bmatrix}$ </td><td> $\begin{bmatrix} x \\ JONES \\ \\ \\ V1 \end{bmatrix}$ </td></tr></table>

since REG(x,CS100) matches in the database REG(SMITH,CS100) and REG(JONES,CS100), and -REG(x,CS200) matches in the database the record REG(SMITH,CS200). Subtracting the negative records from the positive records, we get JONES. Intuitively, JONES is a violation of CI since he takes CS100 but not CS200.

Similarly, constraint 2 is STUDENT(x,CS), COURSE(y,CS), -REG(x,y). The corresponding V2 is:

$$
\left[ \begin{array}{c c} x & y \\ 2 & \text {SMITH} & \text {CS100} \\ 2 & \text {SMITH} & \text {CS200} \\ 2 & \text {JONES} & \text {CS100} \\ 2 & \text {JONES} & \text {CS200} \\ - 2 & \text {SMITH} & \text {CS100} \\ - 2 & \text {SMITH} & \text {CS200} \\ - 2 & \text {JONES} & \text {CS100} \\ & & v _ {2} \end{array} \right] 2 \left[ \begin{array}{c c} x & y \\ \text {JONES} & \text {CS200} \\ & \\ & \\ & \\ & \\ & v _ {2} \end{array} \right]
$$

since STUDENT(x,CS) matches

STUDENT(SMITH,CS) and STUDENT (JONES,CS), and COURSE(y,CS) matches the records COURSE(CS100,CS) and COURSE (CS200,CS), and -REG(x,y) matches all the records in REG. Subtracting the negative records from the positive ones we get JONES CS200. Intuitively JONES CS200 is a violation of C2 since JONES is a CS student but fails to take a CS course, namely CS200.

In general, not all constraints need to be checked for every transaction. Integrity can be maintained incrementally, by assuming integrity before a transaction, and ensuring that the transaction does not violate it. Integrity maintenance then involves two separate tasks.

1. The identification and retrieval of relevant constraints for each transaction.

2. The execution of those constraints against the database to detect possible integrity violations. Moreover, the execution does not need to involve the whole database, and the identification and retrieval of the relevant portion of the database is another possible source of efficiency.

Both insertions and deletions of records into the database can be handled by merely matching the records involved against the constraint base, identifying the constraints involved. The only additional assumption is that the insertions are required to match only the positive records, and deletions match only the negative records. Once the relevant constraints are identified, a V file is created for each to detect violations. The database is also restricted only to the data records involved.

Example: Given the constraints:

$$
\begin{array}{l l} \text {Cl:} & \text {REG} (x, \text {CS100}), - \text {REG} (x, \text {CS200}) \\ \text {C2:} & \text {STUDENT} (x, \text {CS}), \quad \text {COURSE} (y, \text {CS}), \\ & - \text {REG} (x, y) \end{array}
$$

Insertion into REG file of the record REG(DOE,CS200) fails to match any constraint records since the only records that match CS200 are negative ones. Consequently, no violations can occur. No further checks are necessary. Similarly, deleting from the STUDENT file the record (SMITH,CS) can cause no violations since - STUDENT(SMITH,CS) fails to match any constraint records. On the other hand, inserting into STUDENT the record STUDENT(DOE,CS) will cause a match with STUDENT(x,CS), and, hence, the constraint C2 may be violated. Restricting $x = \text{DOE}$ , and forming V2:

$$
\begin{array}{l} 2 \left[ \begin{array}{c c} x & y \\ \text {DOE} & \text {CS100} \\ \text {DOE} & \text {CS200} \\ & v _ {2} \end{array} \right] \end{array}
$$

which indicates a violation. Intuitively, the violation follows from the fact that all CS students have to take all CS courses. DOE is a CS student, but takes neither CS100 nor CS200. Note that V2 is a restricted V file. It does not need to be fully developed for a given transaction, but it is restricted to the matches found, x = DOE in this case, resulting in a very efficient enforcement algorithm.

Similarly, deleting the record REG-(SMITH,CS100) may violate the constraint C2, since -REG(SMITH,CS100) matches -REG(x,y). Restricting x = SMITH and y = CS100, and developing V2:

$$
2 \left[ \begin{array}{c c} x & y \\ \text { SMITH } & \text { CS100 } \\ & v _ {2} \end{array} \right]
$$

V2 does not contain a record -2(SMITH,CS100) since it has been deleted, and hence a violation results. The violation follows intuitively from the fact that a CS student (SMITH) fails to take a CS course (CS100).

## 4. Extensions

In the general case, a constraint language requires the power of first order logic, and that power can be acquired by extending the constraint base with negative variables such as -x meaning “no such x” [8]. These constraints are less frequent in real life databases, however the constraint base can be extended to handle them for theoretical completeness.

Example: The following constraints indicate a violation of the database integrity if:

C3: There is a CS student taking no courses.

C4: Every CS student takes at least one course (i.e., let x be a student taking no CS courses; there is no such CS student).

Such general constraints can easily be stored in a constraint base. The only additional requirement is the storage of negative variables. The constraint base containing C3 and C4 is shown below:

$$
\begin{array}{l} 3 \left[ \begin{array}{c c} \mathbf {x} & \mathbf {C S} \\ - \mathbf {x} & \mathbf {C S} \end{array} \right] 3 \left[ \begin{array}{c c} \mathbf {x} & - \mathbf {y} \\ \mathbf {x} & - \mathbf {y} \end{array} \right] \end{array}
$$

STUDENT REG

Detecting violations in this general environment is similar to the special case of Section 2, but may involve multiple steps of V file formation, one for each negative variable in the constraint. The following algorithm is used to detect violations:

1. Replace P(x), Q(x, -y) with P(x) - Q(x, y) for any P, Q, x and y, where P and Q are relations and x and y are variables.

2. Use the resulting formula to derive the V file by subtracting the negative records from the positive records at each step.

3. If the formula is negative, form a -V file by negating the formula and then derive the file as in step 2. A violation is indicated if a nonempty V file or an empty -V file results. Intuitively, the algorithm corresponds to a rewriting rule. Constraints involving negative variables can be rewritten in terms of joins and subtractions of files. The resulting formula can then be used to create a V file as in Section 2.

Example: Given the following university database:

$$
\left[ \begin{array}{c c} ^ {\mathrm{x}} & ^ {\mathrm{y}} \\ S M I T H & C S \\ J O N E S & C S \end{array} \right] \left[ \begin{array}{c c} S M I T H & C S 1 0 0 \\ S M I T H & C S 2 0 0 \end{array} \right]
$$

STUDENT

COURSE

$$
\text { C3:STUDENT } (x, \text { CS }), \text { REG } (x, - y)
$$

indicates a violation if there is a CS student taking no courses. Clearly, JONES is a violation.

Applying the algorithm:

$$
\mathrm{V} 3 = \text { STUDENT } (\mathrm{x}, \mathrm{CS}) - \text { REG } (\mathrm{x}, \mathrm{y})
$$

$$
\begin{array}{r} - 3 \left[ \begin{array}{c c} x & y \\ \text { SMITH } & \text { CS100 } \\ \text { SMITH } & \text { CS100 } \\ \text { SMITH } & - \\ \text { JONES } & - \\ & v _ {3} \end{array} \right] \left[ \begin{array}{c c} x & y \\ \text { JONES } & - \\ & \\ & v _ {3} \end{array} \right] \end{array}
$$

V3 is obtained by subtracting the negative records from the positive records, and indicates a violation by JONES. Note that - indicates an irrelevant entry and matches any other data item during subtraction.

C4: STUDENT(-x,CS), REG(x,-y) indicates a violation if every CS student takes at least one course. Clearly, this constraint is not violated since there is JONES taking no courses. Applying the algorithm:

$$
\mathrm{V} 4 = - \left(\text { STUDENT } (\mathrm{x}, \mathrm{CS}) - \operatorname{REG} (\mathrm{x}, \mathrm{y})\right)
$$

$$
- \mathrm{V} 4 = \text { STUDENT } (\mathrm{x}, \mathrm{CS}) - \operatorname{REG} (\mathrm{x}, \mathrm{y})
$$

$$
\begin{array}{r} - 4 \left[ \begin{array}{c c} ^ {\mathrm{x}} & ^ {\mathrm{x}} \\ \text {SMITH} & \text {CS100} \\ \text {SMITH} & \text {CS200} \\ \text {SMITH} & - \\ \text {JONES} & - \end{array} \right] \left[ \begin{array}{c c} ^ {\mathrm{y}} & ^ {\mathrm{y}} \\ \text {JONES} & - \\ - \text {V4} & - \text {V4} \end{array} \right] \end{array}
$$

The algorithm terminates with a nonempty negative file, hence no violation is indicated. A record in the negative file can be interpreted as a record preventing a violation. Clearly, JONES in this case is the record preventing a violation.

Insertions and deletions can be handled similarly by forming V files after each transaction to detect violations. However, not all constraints need to be checked for each transaction, but only a small number of constraints and a small segment of the database is relevant to each transaction. Identifying the relevant constraints and the data items accurately, without any unnecessary checks is a major source of efficiency in a constraint base environment.

Identifying the relevant constraints is a slightly more difficult process when negative variables are involved. A new “sign” field is created in each file in the constraint base, containing $a + \text{or } a -$ for each record, depending on the number of negative variables in that record. First, all variables in a constraint are classified as + or -. A variable x is negative if there is a -x in the constraint, otherwise it is positive. Then, each record is assigned $a + \text{sign}$ if it contains an even number of negative variables, or a - sign if it contains an odd number of negative variables.

Example: The university constraint base is expanded as follows:

constraint# name depth sign constraint# name

course# sign

$$
\begin{array}{l} 3 \left[ \begin{array}{c c} \mathrm{x} & \mathrm{CS} \\ - \mathrm{x} & \mathrm{CS} \end{array} \right] + 3 \left[ \begin{array}{c c} \mathrm{x} & - \mathrm{y} \\ \mathrm{x} & - \mathrm{y} \end{array} \right] - \\ 4 + \end{array}
$$

STUDENT

REG

since the third constraint has x as a positive variable, and y as a negative; and the fourth constraint has both x and y as negative variables.

Once the sign field is created, the insertions and deletions are handled similar to the special case of Section 2, where insertions match only the positive records and deletions match only the negative records. The database is restricted for each transaction to the data items matching the positive variables of the constraint.

Example: Given the following university database:

$$
\begin{array}{l} \left[ \begin{array}{c c} \text {SMITH} & \text {CS} \\ \text {JONES} & \text {CS} \end{array} \right] \left[ \begin{array}{c c} \text {SMITH} & \text {CS100} \\ \text {SMITH} & \text {CS200} \\ \text {JONES} & \text {CS100} \end{array} \right] \\ \text {STUDENT} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {REG} \end{array}
$$

and the constraints:

$$
\mathrm{C3}: \text { STUDENT } (\mathrm{x}, \mathrm{CS}) +, \mathrm{REG} (\mathrm{x}, - \mathrm{y}) -
$$

$$
\mathrm{C4}: \text { STUDENT } (- x, \mathrm{CS}) -, \mathrm{REG} (x, - y) +
$$

Deletion of REG(JONES,CS100) results in a match between REG(JONES,CS100) - and REG(x,-y)-, and consequently the constraint C3 needs to be checked for possible violations. Applying the algorithm with the restriction $x =$ JONES:

$$
\left[ \begin{array}{c c} x & y \\ \text {JONES} & - \\ & v _ {3} \end{array} \right]
$$

resulting in a violation. Intuitively, C3 is violated when a CS student takes no courses, and deleting (JONES,CS100) does violate it since JONES takes no other courses.

Similarly, insertion of REG(JONES,CS200) results in a match between REG(JONES,CS200) + and REG(x,-y)+, and the constraint C4 needs to be checked for possible violations. No restrictions to the database is possible since C4 has no positive variables. Applying the algorithm:

$$
\begin{array}{l} - \left[ \begin{array}{c c} x & y \\ \text {SMITH} & \text {CS100} \\ \text {SMITH} & \text {CS200} \\ \text {JONES} & \text {CS100} \\ \text {JONES} & \text {CS200} \\ \text {SMITH} & - \\ \text {JONES} & - \\ - V 4 \end{array} \right] \left[ \begin{array}{c c} x & y \\ - V 4 \end{array} \right] \end{array}
$$

indicating a violation. Intuitively, C4 is violated when each CS student takes at least one course, and both SMITH and JONES are taking courses.

## 5. Comparison and conclusions

The current practice in constraint management is to store constraints either as procedures or as queries, but in both cases as unstructured text, where all constraints need to be retrieved and executed periodically (or after each transaction for real-time enforcement). The only major attempts to structure constraints on storage devices used very minimal indexing, only with respect to the relation names referenced [1,10]. Even such minimal indexing provided considerable improvement in efficiency compared to sequential retrieval of all constraints. With a database of n constraints and m relations, where each constraint references $p$ distinct relations on average, and each transaction updates $q$ distinct relations; the number of constraints retrieved from secondary storage for each transaction reduces to $(npq/m)$ which compares favorably to the total n when the number of relations $(m)$ is large, and the transactions are small $(q \ll m)$ as in real time constraint enforcement.

n = number of constraints

np = number of all relation references by all constraints

$(np / m) =$ number of references to each relation $=$ number of constraints per relation

$(npq/m)$ = number of constraints per transaction

The example-based storage and retrieval scheme proposed in this article produces much more dramatic and more consistent improvement in efficiency. Above and beyond the simple indexing with respect to relation names, this scheme involves two more components:

1. Indexing of the constraint records with respect to the type of transactions that may effect them (insertions or deletions). This component produces a 50% improvement in efficiency assuming a 50–50 split between insertions and deletions received by the system, and since each constraint record is relevant to either insertions or deletions to a given relation, but not both as shown in Section 3.

2. Indexing of the constraint atoms with respect to their constants, which produces a 100r% improvement in efficiency, where r is the proportion of constraint records that have constants (see Section 2).

= proportion of constraint records with constants

l - r = proportion of constraint records with no constants = proportion retrieved automatically with no constant check

s = probability of a transaction matching the constants of a constraint record = 1/(the number of possible constants for a constraint record) $^{2}$

rs = proportion of constraint records that match a transaction

$(l-r)+rs=$ proportion of constraints that are retrieved for a transaction due to constant match or no constants = 1 - (1 - s)r ≈ l - r since s ≪ 1.

$(npq/m)$ = the proportion of constraints re- $(1-r/2)$ retrieved due to matching relations,
matching transaction type (insertion/
deletion), and matching constants.

This is a dramatic increase in efficiency over and above what was achieved by simple indexing with respect to relation names. While indexing with respect to relation names produced widely varying improvement (0–90%) depending on the values of m, p, and q; the example-based indexing produces consistent improvement in efficiency varying between 25–45% over and above the improvement achieved by simple indexing since r typically varies between 0.10–0.50. The total improvement in efficiency ranges between 25–95% over simple sequential execution of all constraints.

There are also other significant advantages to expressing all first order constraints as example data. Data have simple semantics and expressing constraints is simplified when they are reduced to data. Data are well understood in terms of storage and retrieval in large quantities and this knowledge could immediately be transferred to constraint management since commercial databases often need large numbers of constraints. Integrity maintenance involves a comparison between the database and the constraints, and expressing constraints as data simplifies this process. The development in this paper is similar in philosophy to the development of clausal form of logic. As clausal form of first order logic proved useful in theorem proving, counter example form of first order logic is designed to be useful in storage and retrieval of first order sentences.

## References

[1] E.N. Hanson, Rule Condition Testing and Action Execution in Ariel, Proceedings of ACM-SIGMOD Conference (1992) 49–58.

[2] M. Hammer and D. McLeod, Database Description with SDM: A Semantic Data Model, Transactions on Database Systems 6(3) (1981) 351–386.

[3] I. Kobayashi, Validating Database Updates, Information Systems 9(1) (1986) 1–17.

[4] W. McCune and L.J. Hernchen, Maintaining State Constraints in Relational Databases: A Proof Theoretic Basis, Journal of ACM 36(1) (1989).

[5] M. Morgenstern, Constraint Equations: Declarative Expression of Constraints with Automatic Enforcement, VLDB (1984) 33–42.

[6] J.M. Nicholas, Logic for Improving Integrity Checking in Relational Databases, Acta Informatica 18 (1982) 227-253.

[7] L.V. Orman, Information Cost as a Determinant of System Architecutre, Information and Software Technology 36(3) (1994) 165–172.

[8] L.V. Orman, Constraint Maintenance as a Database Design Criterion, Computer Journal 34(1) (1991) 73–79.

[9] A. Shephard and L. Kerschberg. PRISM: A Knowledge Based System for Semantic Integrity Specification and Enforcement in Database Systems, Proceedings of SIGMOD Conference (1984)307–315.

[10] M. Stonebraker et al., The Postgres Rules System, Transactions on Software Engineering 14 (1988) 7.

[11] A.U. Tansel, M.E. Arkun and G. Ozsoyoglu, Time by Example Query Language for Historical Databases, Transactions on Software Engineering 15(4) (1989) 464–478.

[12] S. Tsur and C. Zaniolo, A Logic-Based Data Language, VLDB (1986).

[13] J.D. Ullman, Principles of Data and Knowledge Base Systems, Computer Science Press (1989).

[14] S.D. Urban and L.M.L. Delcambre, Constraint Analysis: Specifying Operations on Objects, Transactions on Knowledge and Data Engineering 2(4) (1990) 391–400.

[15] R. Wang, Information Technology in Action (MIT Press, Cambridge, 1993).

[16] R. Weber, EDP Auditing (McGraw Hill, NY, 1982).

[17] M.M. Zloof, Query by Example: A Database Language, IBM Systems Journal 16 (1977) 4.

![](/api/attachments/FC4VTVX9/fulltext/images/54ed94213ea4109ed99d6790961f73cf9892260975f24ba096efcc0a62bbe76e.jpg)

Levent V. Orman is associate professor of Information Systems at Cornell University, Graduate School of Management. He has received MM and PhD degrees from Northwestern University. His professional interests include design, specification, and evaluation of information systems, with particular emphasis on data base and knowledge base architectures and languages. His recent articles appeared in Information Systems, Journal of

MIS, MIS Quarterly, Intelligent Information Systems, Applied Artificial Intelligence, Data and Knowledge Engineering, and Transactions on Software Engineering.
