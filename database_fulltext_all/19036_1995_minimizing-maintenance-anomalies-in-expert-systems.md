---
otero_id: 19036
otero_key: "TQQFRWEY"
title: "Minimizing maintenance anomalies in expert systems"
authors: "R.C. Hicks"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)00041-g"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Minimizing maintenance anomalies in expert systems

R.C. Hicks

Department of Management, University of Nevada at Las Vegas, 4505 Maryland Parkway, Las Vegas, NV 89154, USA

## Abstract

Expert systems are emerging as a powerful technology for solving many problems previously requiring human experts. However, maintenance has been identified as a major difficulty in expert system implementations. Surprisingly, the problem of maintenance has only recently begun to receive attention in expert systems research, though it has long been an issue in databases. Databases are in a constant state of change, and the prevention of maintenance anomalies is essential. As similar maintenance operations are performed on rule bases, this paper investigates techniques to avoid maintenance anomalies in expert system rule bases. The result is an expert system rule base structure that is appropriate for volatile production use. In addition to lower maintenance demands, this approach favorably impacts on verification, computational efficiency, and storage requirements.

Keywords: Expert systems; Maintenance; Rule base; Anomalies; Normalization

## 0. Introduction

Maintenance is a major problem in expert systems; because of maintenance, CAT has been taken out of service and XCON [3,16] has been re-implemented in a low maintenance environment called RIME [1]. It should come as no surprise that retaining rule base accuracy during frequent modifications is a considerable challenge for maintainers. In procedural programs, maintenance usually consumes 70% of the software budget; in one project, the cost of maintenance was 100 times the cost of development [22]! The volatility of the domain has been identified as the major determinant of maintenance [2].

Frequent modifications to data have been a major research issue in the field of databases; the database concept of normalization is devoted to removing opportunities for maintenance anomalies. This paper takes these database concepts and extends them to rule bases. We will find similarities, but not a one-to-one correspondence, between database and rule base anomalies. Two types of update anomalies, implicit and explicit, may occur in rule bases. Implicit anomalies are caused by dependencies between conditions: they can be removed heuristically. Explicit anomalies are caused by either insufficient decomposition or irrelevant conditions; both types of explicit anomaly may be minimized algorithmically. This paper discusses only the anomalies associated with an individual set of rules. These concepts are demonstrated on a necessarily small rule base and the effect on maintenance of removing the anomalies is shown. These concepts are implemented in the CASE tool EZ-Xpert.

A taxonomy of opportunities for maintenance anomalies in rule bases is presented. Included with each type of anomaly is a description of the heuristic or algorithm that minimize these anomalies. The maintenance implications of each step are also discussed.

## 1. A taxonomy of maintenance anomalies

An expert system rule base is composed of a disjoint set of “rule clusters” [17]. Each rule cluster contains all the rules in which a common set of conditions are used to reach a common conclusion (or set of conclusions).

Each rule cluster may be represented as a decision table relation (DTR) formed by populating it with a Cartesian product of the domain values of the conditions and a mapping, by the expert, of conclusions (again, from the domain of the conclusions) to each set of conditions. Unlike database keys, conditions may be null. Each row of the DTR is equivalent to an expert system rule in conjunctive normal form. EZ-Xpert can assign conclusions to 1000 rows (or rules) per hour. DTRs have the following desirable characteristics.

1. Most local verification criteria, such as missing rules, contradictory rules, and conflicting rules, are met. The closed-world assumption is valid.

2. As two-dimensional arrays, DTRs are well suited to algorithmic refinement.

3. DTRs can be transposed to database relations for storage.

4. DTRs can be syntactically transformed into expert system rules.

Let us compare the problems with update anomalies in databases to the domain of rule bases. In an expert system rule base, an anomaly is a rule that does not accurately represent the domain modeled; it is caused by an error in the rule. The program will appear to function correctly, but certain questions will give inaccurate output (i.e., the wrong answer or no answer is given). If detected, these inaccuracies will require maintenance and may cause a loss of confidence in the expert system. If NOT detected, the results could be even more damaging.

In databases, three types of anomalies can occur; insert, delete, and update. Both the insert and delete database anomalies are caused by partial dependencies and result in a violation of key constraints $[6,8]$ . In a relational database as described by Codd $[5]$ , a key cannot be null. In rule bases, keys correspond to conditions and attributes correspond to conclusions. As it is possible, and even desirable, to have null conditions (ones that are not required in order to reach a conclusion), these anomalies do not occur in rule bases. We therefore concentrate on the update anomaly.

In an attempt to lower maintenance demands in XCON, RIME lowers the number of possibilities for an update anomaly through decomposition. This paper extends this concept by integrating it with normalization concepts as well as techniques suggested by boolean simplification and induction theories. This paper introduces a four step approach (that we refer to as refinement) to minimize opportunities for maintenance anomalies. The R4 Algorithms presented here are implemented in EZ-Xpert.

## 1.1. The implicit anomaly

The most dangerous type of anomaly is the implicit anomaly. An implicit anomaly occurs when one condition is dependent on another for its value, as in database transient dependencies. In this situation, changes to the dominant condition imply the need for a change to the dependent condition. However, the maintainer must be aware of this relationship and also make all of the necessary changes. If both changes are not made, the rule base is not accurate.

To illustrate this concept, consider a microcomputer version of XCON. A small computer manufacturer has built an expert system to determine what cabinet and monitor are needed for a specific computer. The conditions used to determine these conclusions are the amount of RAM memory, size of the hard disk, type of hard disk controller, and type of video card. The initial DTR in Table 1 could be developed by someone not fully aware of the dependencies between conditions and conclusions. Implicit anomalies are highlighted in bold italic.

<table><tr><td colspan="7">Table 1Initial DTR</td></tr><tr><td>Rule</td><td>RAM</td><td>Drive</td><td>Control</td><td>Video</td><td>Cabinet</td><td>Monitor</td></tr><tr><td>1</td><td>&gt; = 4mb</td><td>200mb</td><td>ESDI</td><td>VGA</td><td>Tower</td><td>Color</td></tr><tr><td>2</td><td>&lt; 4mb</td><td>200mb</td><td>ESDI</td><td>VGA</td><td>Desk</td><td>Color</td></tr><tr><td>3</td><td>&gt; = 4mb</td><td>40mb</td><td>ESDI</td><td>VGA</td><td>Desk</td><td>Color</td></tr><tr><td>4</td><td>&lt; 4mb</td><td>40mb</td><td>ESDI</td><td>VGA</td><td>Desk</td><td>Color</td></tr><tr><td>5</td><td>&gt; = 4mb</td><td>200mb</td><td>RLL</td><td>VGA</td><td>Tower</td><td>Color</td></tr><tr><td>6</td><td>&lt; 4mb</td><td>200mb</td><td>RLL</td><td>VGA</td><td>Desk</td><td>Color</td></tr><tr><td>7</td><td>&gt; = 4mb</td><td>40mb</td><td>RLL</td><td>VGA</td><td>Desk</td><td>Color</td></tr><tr><td>8</td><td>&lt; 4mb</td><td>40mb</td><td>RLL</td><td>VGA</td><td>Desk</td><td>Color</td></tr><tr><td>9</td><td>&gt; = 4mb</td><td>200mb</td><td>ESDI</td><td>Herc</td><td>Tower</td><td>B/W</td></tr><tr><td>10</td><td>&lt; 4mb</td><td>200mb</td><td>ESDI</td><td>Herc</td><td>Desk</td><td>B/W</td></tr><tr><td>11</td><td>&gt; = 4mb</td><td>40mb</td><td>ESDI</td><td>Herc</td><td>Desk</td><td>B/W</td></tr><tr><td>12</td><td>&lt; 4mb</td><td>40mb</td><td>ESDI</td><td>Herc</td><td>Desk</td><td>B/W</td></tr><tr><td>13</td><td>&gt; = 4mb</td><td>200mb</td><td>RLL</td><td>Herc</td><td>Tower</td><td>B/W</td></tr><tr><td>14</td><td>&lt; 4mb</td><td>200mb</td><td>RLL</td><td>Herc</td><td>Desk</td><td>B/W</td></tr><tr><td>15</td><td>&gt; = 4mb</td><td>40mb</td><td>RLL</td><td>Herc</td><td>Desk</td><td>B/W</td></tr><tr><td>16</td><td>&lt; 4mb</td><td>40mb</td><td>RLL</td><td>Herc</td><td>Desk</td><td>B/W</td></tr></table>

The problem with this DTR is that the type of controller determines the type of hard disk. The computer builder knows that an ESDI controller dictates a 200mb drive while an RLL controller dictates a 40mb drive. Half of the rules in this rule base represent combinations that should never occur. It would be possible to ship a 200mb drive with an RLL controller (which would not work) with this system.

Now, consider maintenance on this system. Assume that a 100mb drive is offered to replace the 40 mb drive, and that this drive uses an IDE controller. If the maintainer was not aware of this, he would replace all of the occurrences of 40mb with 100mb and think that maintenance is complete. As the 100mb drive cannot use an RLL controller, the result of this is that the rule base is 75% inaccurate.

An even more insidious problem arises when the rule base builder realizes that only one of the conditions is necessary to reach a conclusion but is inconsistent in which one is used. If, for example, the condition “Drive = 40mb” is used in one rule and another condition such as “Control = RLL” is used in the next rule, maintenance would be very difficult to perform accurately.

The solution to this problem is to “normalize” the DTR. The goal of rule base normalization is for every action to be dependent on every condition, and for the conditions to be mutually independent. In this case, the “controller/drive” relationship would be represented with another set of rules, and the condition “drive” would be removed from this DTR. Note that normalization implies an understanding of the data and cannot be treated algorithmically. As in databases, one cannot distinguish between true functional dependencies and coincidental patterns in the data. The R4 Normalization heuristic in Table 2 recognizes and treats implicit anomalies. Representing propositions with capital letters, normalization is dictated when:

## A & B & C & D → X

## $\mathrm{B}\rightarrow \mathrm{C}$

By removing the controller and drive relationship to a separate DTR, the maintenance problems shown with implicit anomalies are eliminated. Note that in Table 3, all opportunities for an implicit anomaly have been removed. Explicit anomalies are also minimized; in the initial DTR, each value (such as RAM < 4mb) occurs eight times. After normalization is performed, each value occurs four times.

Another dependency possible in a DTR is where a conclusion determines another conclusion. It is, of course possible to “normalize” this dependency also. If, however, there is not a conflict between values in sets of conclusions, it is not desirable to “normalize” them. The R4 Normalization Heuristic may be applied to conclusions. It is especially advantageous to “normalize”

## Table 2

## Normalization heuristic

Table 3  
Normalized DTR

<table><tr><td>Rule</td><td>RAM</td><td>Control</td><td>Video</td><td>Cabinet</td><td>Monitor</td></tr><tr><td>1</td><td> $> = 4mb$ </td><td>ESDI</td><td>VGA</td><td>Tower</td><td>Color</td></tr><tr><td>2</td><td> $< 4mb$ </td><td>ESDI</td><td>VGA</td><td>Desk</td><td>Color</td></tr><tr><td>3</td><td> $> = 4mb$ </td><td>RLL</td><td>VGA</td><td>Desk</td><td>Color</td></tr><tr><td>4</td><td> $< 4mb$ </td><td>RLL</td><td>VGA</td><td>Desk</td><td>Color</td></tr><tr><td>5</td><td> $> = 4mb$ </td><td>ESDI</td><td>Herc</td><td>Tower</td><td>B/W</td></tr><tr><td>6</td><td> $< 4mb$ </td><td>ESDI</td><td>Herc</td><td>Desk</td><td>B/W</td></tr><tr><td>7</td><td> $> = 4mb$ </td><td>RLL</td><td>Herc</td><td>Desk</td><td>B/W</td></tr><tr><td>8</td><td> $< 4mb$ </td><td>RLL</td><td>Herc</td><td>Desk</td><td>B/W</td></tr><tr><td>Rule</td><td>Drive</td><td>Control</td><td></td><td></td><td></td></tr><tr><td>1</td><td>200mb</td><td>ESDI</td><td></td><td></td><td></td></tr><tr><td>2</td><td>40mb</td><td>RLL</td><td></td><td></td><td></td></tr></table>

plural conclusions (i.e., those which return all possible conclusions).

Normalization is detected and treated by the user as conclusions are assigned. The Cartesian product of the DTR guarantees that all combinations of condition values are evaluated; any conflicting condition values signal the presence of implicit anomalies and the need for normalization.

## 1.2. Explicit anomalies

An explicit anomaly occurs if all instances of a condition value are not changed consistently. In other words, every duplication of an condition value presents an opportunity for an explicit anomaly. Each set of rules should perform a single task or reach a minimal set of conclusions. To determine if this is true, the rule base builder looks for independent sets of conditions and actions represented in the same DTR. In Table 3, note that the determination of the monitor used is independent of the decision about what cabinet is used. The monitor choice is determined by only the video card, and the cabinet used is determined only by the RAM and controller installed. By decomposing this DTR, we remove opportunities for explicit anomalies, simplify the representation, and lower maintenance efforts.

Decomposition is dictated when:

$$
\mathrm{A} \&\mathrm{B} \&\mathrm{C} \rightarrow \mathrm{X} \&\mathrm{Y}
$$

$$
\mathrm{A} \&\mathrm{B} \rightarrow \mathrm{X}
$$

$$
\mathrm{C} \rightarrow \mathrm{Y}
$$

The R4 Algorithms perform decomposition algorithmically as shown in Tables 4 and 5. To avoid computational expense, two preliminary tests are used to determine if decomposition is possible.

The result of decomposition is shown in Table 6 (the controller/drive DTR is not changed).

The effect of decomposition is to lower the number of occurrences of each condition value. In the bottom DTRs, each value occurs only

## Table 4

Decomposition tests

## Table 5

## Decomposition algorithm

Table 6
Decomposed DTR

<table><tr><td>Rule</td><td>RAM</td><td>Control</td><td>Cabinet</td></tr><tr><td>1</td><td>&gt; = 4mb</td><td>ESDI</td><td>Tower</td></tr><tr><td>2</td><td>&lt; 4mb</td><td>ESDI</td><td>Desk</td></tr><tr><td>3</td><td>&gt; = 4mb</td><td>RLL</td><td>Desk</td></tr><tr><td>4</td><td>&lt; 4mb</td><td>RLL</td><td>Desk</td></tr><tr><td>Rule</td><td>Video</td><td>Monitor</td><td></td></tr><tr><td>1</td><td>VGA</td><td>Color</td><td></td></tr><tr><td>2</td><td>Herc</td><td>B/W</td><td></td></tr></table>

once. In the top, each value appears twice. Contrast these DTRs with the initial DTR in which every value occurs eight times.

RIME prescribes only decomposition to minimize the opportunities for explicit anomalies, but other techniques allow further refinement. Induction algorithms such as ID3 [18] are commonly used to produce a simplified rule cluster from a set of examples. Boolean simplification techniques, such as the Karnaugh Map and Quine-McClusky algorithm, can be extended to further simplify expert system rules. Examining the first DTR in Table 6, we notice that in rules 3 and 4, all values for RAM, when combined with a RLL controller, result in a desk cabinet. In these rules, and possibly only in these rules, RAM is irrelevant. Similarly, in rules 2 and 4, both types of controller result in a desk cabinet when combined with <4 mb of RAM. We can eliminate the irrelevant test from these rules, remove any redundant rules, and remove more opportunities for explicit anomalies using the algorithm shown in Table 7. Simplification is dictated when:

Table 8  
Simplified DTR

<table><tr><td>Rule</td><td>RAM</td><td>Control</td><td>Cabinet</td></tr><tr><td>1</td><td>$ &gt; = 4\text{mb} $</td><td>ESDI</td><td>Tower</td></tr><tr><td>2</td><td>$ &lt; 4\text{mb} $</td><td>-</td><td>Desk</td></tr><tr><td>3</td><td>-</td><td>RLL</td><td>Desk</td></tr></table>

$$
\mathrm{A} \&\mathrm{B} \rightarrow \mathrm{C}
$$

$$
\mathrm{A} \&\sim \mathrm{B} \rightarrow \mathrm{C}
$$

The results of this simplification are shown in Table 8.

Finally, we can perform range simplification to remove more opportunities for explicit anomalies. The R4 Range Simplification Algorithm is shown in Table 9.

Table 10 contains a set of rules suited to numeric simplification. Note that any value of RAM less than 8 mb combined with an ESDI hard disk controller dictates a desk cabinet. The result of range simplification is shown in Table 11.

Table 9

<table><tr><td>Range simplification algorithm</td></tr><tr><td>1. Partition a DTR into subsets which reach the same conclusion(s).</td></tr><tr><td>2. Within the subsets, test each pair of rules to determine if the value for only one condition is different. We will refer to the different condition as the test condition, the others as the constant values.</td></tr><tr><td>3. If such a pair exists, examine all rules which have the same constant values.A. If the values are numeric, check each rule to see if an adjoining numeric range reaches the same conclusion for the same constant values. If so, expand the range in one rule to cover the combined range and remove the other.B. If the values are dates, check to see if adjoining dates reach the same conclusion with the same constant values. If so, expand the date ranges in one rule to include both ranges and remove the other.</td></tr><tr><td>4. Remove redundant and subsumed rules.</td></tr></table>

If desired, the rules may now be ordered for efficiency in the host environment. It may be desirable, for example, to place the rules with the fewest conditions first. This step is implementation-specific.

The R4 Algorithms are based in formal logic. They are more computationally expensive than heuristic approaches such as ID3, but results in greater simplification. On the 96 clause Lens test case, ID3 produces a 31 clause rule cluster, where the R4 Simplification Algorithm produces a logically identical rule cluster with 25 clauses. Additionally, the R4 Algorithms allows simplifications to be “undone” in order to perform maintenance and correct specifications.

The R4 Algorithms produces the maximum simplification possible because they are exhaustive, not heuristic. The negative consequence of exhaustive algorithms is their computational inefficiency when combinatorial explosion becomes problematic. For exotic (or poorly specified) rule clusters larger than 256 rules, a more efficient algorithm such as ID3 may be used to populate the DTR or as a front-end to R4. Of course, the knowledge engineer may choose to hand-code these exotic rule clusters, but these choices imply the burdens of verification and maintenance for these rules.

Table 10  
Simplified DTR partition

<table><tr><td>Rule</td><td>RAM</td><td>Control</td><td>Cabinet</td></tr><tr><td>1</td><td> $> = 8\text{mb}$ </td><td>ESDI</td><td>Tower</td></tr><tr><td>2</td><td> $> = 4, < 8\text{mb}$ </td><td>ESDI</td><td>Desk</td></tr><tr><td>3</td><td> $< 4\text{mb}$ </td><td>ESDI</td><td>Desk</td></tr></table>

Table 11  
Range simplified DTR

<table><tr><td>Rule</td><td>RAM</td><td>Control</td><td>Cabinet</td></tr><tr><td>1</td><td>&gt; = 8mb</td><td>ESDI</td><td>Tower</td></tr><tr><td>2</td><td>&lt; 8mb</td><td>ESDI</td><td>Desk</td></tr></table>

If the goal is to compact the rule base as much as possible, the operators OR and ELSE may be introduced now. However, we feel that these operators, like the procedural GOTO statement, cause confusion and inaccuracies. After simplification is performed, maintenance anomalies have been minimized as much as possible. Confidence factors and explanations may be added to the rules at this time. We can now syntactically transform the DTRs into a rule base. Generating a generic interface (for VP-Expert) results in the rule base shown in Table 12.

```txt
Table 12
Generated rule base

Actions
FIND Cabinet
FIND Monitor
DISPLAY “The correct cabinet is a {Cabinet ~}
DISPLAY “The correct monitor is a {Monitor ~};
IF RAM >= 4 and Control = ESDI THEN Cabinet = Tower;
IF RAM < 4 THEN Cabinet = Desk;
IF Control = RLL THEN Cabinet = Desk;
IF Video = VGA THEN Monitor = Color;
IF Video = Herc THEN Monitor = B/W;
IF Drive = 200mb THEN Control = ESDI;
IF Drive = 40mb THEN Control = RLL;
ASK RAM: “How much RAM memory is installed?”;
ASK Control: “Which hard disk controller is installed?”;
CHOICES Control: RLL, ESDI;
ASK Video: “Which video card is installed?”;
CHOICES Video: VGA, Herc;
ASK Drive: “What is the capacity of the installed hard disk?”;
CHOICES Drive: 200mb, 40mb;
```

## 2. Results

In each of the four steps of refinement, opportunities for maintenance anomalies are removed. In normalization and decomposition, new data structures are derived. The major significance of this approach is to remove opportunities for maintenance anomalies. In the original example, there are 16 opportunities for implicit anomalies and 56 opportunities for explicit anomalies. After normalization, all opportunities for implicit anomalies have been removed by normalization, but eighteen opportunities for explicit anomalies remain. After decomposition, four opportunities for explicit anomalies remain. Thus, at the end, all opportunities for both explicit and implicit anomalies have been removed. This is, of course, an illustrative example. In tests of simplified rule bases submitted by graduate students knowledgeable about refinement and trained in simplification, this approach reduced the number of tests in the student's rule bases by 35.6% and the number of explicit anomalies by 41.5%. On the Lens Test Set, which has 87 explicit anomalies, the R4 Simplification Algorithm alone produces the rule cluster with 16 explicit anomalies shown in Table 13, a reduction of 82%. ID3 produces a rule cluster with 22 explicit anomalies.

As a side-effect of knowledge refinement, the storage space needed for the rule base is reduced (in the example, from 3341 bytes to 1290) and computational efficiency is improved (the worst-case execution time for the original rule base is 7.14 seconds, but with the final rule cluster it is 1.03 seconds).

Table 13  
EZ-Xpert lens simplification

<table><tr><td>Age</td><td>Prescrip</td><td>Astig</td><td>Tear_pro</td><td>Lens</td></tr><tr><td>*</td><td>*</td><td>*</td><td>Reduced</td><td>None</td></tr><tr><td>*</td><td>Myope</td><td>Yes</td><td>Normal</td><td>Hard</td></tr><tr><td>*</td><td>Hypermetrope</td><td>No</td><td>Normal</td><td>Soft</td></tr><tr><td>Young</td><td>*</td><td>Yes</td><td>Normal</td><td>Hard</td></tr><tr><td>Pre_presbyopic</td><td>Hypermetrope</td><td>Yes</td><td>*</td><td>None</td></tr><tr><td>Presbyopic</td><td>Hypermetrope</td><td>Yes</td><td>*</td><td>None</td></tr><tr><td>Young</td><td>*</td><td>No</td><td>Normal</td><td>Soft</td></tr><tr><td>Pre_presbyopic</td><td>*</td><td>No</td><td>Normal</td><td>Soft</td></tr><tr><td>Presbyopic</td><td>Myope</td><td>No</td><td>*</td><td>None</td></tr></table>

In addition, the knowledge expressed by the expert is presented in its most simplified form, and can provide deeper insight into the domain by removing the “noise” of extraneous conditions. Refined knowledge is especially beneficial in teaching systems and implementing systems with unusually complex domains.

## 3. Integrated research

This paper describes one component of The Relational Intelligence Management Methodology (TRIMM). TRIMM has been implemented in a computer program named EZ-Xpert. This research is concerned with methodologies and tools for building and maintaining production expert systems. Major concerns addressed are maintenance, verifiability, and computational efficiency.

This paper defines three types of maintenance anomalies present in rule based expert systems and the appropriate refinement to minimize these anomalies. The output is a rule base structure (the local view) that is suitable for long-term maintenance. The next step is to examine the global view of the relationships between rule clusters.

Verification is another major problem in expert systems. Two sets of verification criteria must be met: local for each rule cluster and global. Local verification is concerned with missing or contradictory rules; for example, while global verification is concerned with referential integrity and reachability. EZ-Xpert performs 12 local verification tests on each DTR and 8 global verification tests.

AI applications are traditionally inefficient. If a suitable compiler is available for the application, DTRs can be transformed into code suitable for compilation. Schwartz uses “complete K-trees” to generate Pascal code for an admissions advisor expert system $[19]$ , achieving dramatic increases in performance and dramatic decreases in storage capacity and hardware requirements. Other languages such as C++ may be more suitable. In this way, EZ-Xpert can function as a CASE tool for generating compiled expert systems.

This research is funded in part by a research grant from First Interstate Bank.

## References

[1] "AI Trends," High Technology, September 1988.

[2] Bachant, Judith and Soloway, Elliot, “The Engineering of XCON,” Communications of the ACM, Volume 32, Number 3, March 1989.

[3] Barker, Virginia E. and O'Connor, Dennis E., "Expert Systems for Configuration at Digital: XCON and Beyond," Communications of the ACM, Volume 32, Number 3, March 1989.

[4] Boose, John N., Expertise Transfer for Expert Systems Design, 1986.

[5] Codd, E.F., “Further Normalization of the Database Relational Model,” Data Base Systems, Courant Science Symposium Series, Volume 6, 1972.

[6] Date, C.J., An Introduction To Database Systems, Volume 2. Addison-Wesley, 1984.

[7] Date, C.J., An Introduction to Database Systems, Volume 1. Addison-Wesley, 1986.

[8] Fagin, R., “A Normal Form for Relational Databases That Is Based on Domains and Keys,” ACM TODS, Volume 6, Number 3, September, 1981.

[9] Harmon, Paul and King, David, Expert Systems: Artificial Intelligence in Business, John Wiley Publishing, 1985.

[10] Hicks, Richard C., "TRIMMer: A CASE Tool For Maintainable Rule-Based Systems," Proceedings of the 1992 Golden West Conference on Intelligent Systems, Reno, Nevada June 1992.

[11] Holsapple, Clyde W. and Whinston, Andrew B., Business Expert Systems, Irwin Publishing, 1987.

[12] Korth, Henry F. and Silberschatz, Abraham, Database System Concepts, McGraw-Hill, 1986.

[13] Lee, R.M., “Application Software and Organizational Change: Issues in the Representation of Knowledge,” Information Systems, Volume 8, Number 3, 1983.

[14] Leonard-Barton, Dorothy and Sviokla, John J., "Putting Expert Systems to Work," Harvard Business Review, March-April 1988.

[15] Martin, James and Oxman, Steven, Building Expert Systems, Prentice-Hall, 1988.

[16] McDermott, J., "R1: A Rule-Based Configurer of Computer Systems," Artificial Intelligence, Volume 19, 1982.

[17] Nguyen, T.A., Perkins, W.A., Laffey, T.J. and Pedora, D., “Checking an Expert System for Consistency and Completeness,” Proceedings of the Ninth International Joint Conference on Artificial Intelligence, 1985.

[18] Qunilan, J.R., “Simplifying Decision Trees,” Knowledge Acquisition for Knowledge-Based Systems, Gaines, B. and Boose, J. Editors, Academic Press, 1988.

[19] Schwartz, Edward N., "Using Complete K-Trees to Generate Code in Pascal for an Expert System," SIGART Bulletin, Volume 1, No. 2, July 1990.

[20] Soloway, Elliot, “I Can’t Tell What In The Code Implements What In The Specs,” Proceedings of the Second International Human-Computer Interaction Conference, Honolulu, Hawaii, 1987.

[21] Soloway, Elliot, Bachant, Judy and Jensen, Keith, "Assessing the Maintainability of XCON-in-RIME: Coping with the Problems of a VERY Large Rule-Base," Proceedings of AAAI-87, Volume 2.

[22] Wulf, W.A., “Some Thoughts on the Next Generation of Programming Languages,” Perspectives on Computer Science, Academic Press, 1977.

![](/api/attachments/TQQFRWEY/fulltext/images/6953f42133c61225b4980a09164bc431d9eb9df20833d2b6f309ca8739fc88ee.jpg)

Richard C. Hicks is an Associate Professor of Information Systems in the Department of Management at the University of Nevada, Las Vegas. He received a M.B.A. from Boston University in 1985 and a Ph.D. in Information Systems from the University of Texas at Austin in 1991. His research interests focus on verification of expert systems, including development methodologies which transparently meet verification criteria and

minimize opportunities for maintenance anomalies. He is the developer of the expert system CASE tool EZ-Xpert.
