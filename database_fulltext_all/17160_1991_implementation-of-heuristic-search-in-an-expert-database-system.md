---
otero_id: 17160
otero_key: "MKB72PDG"
title: "Implementation of heuristic search in an expert database system"
authors: "Oliver Günther"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90040-i"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Implementation of heuristic search in an expert database system \*

Oliver Günther

FAW-AI Laboratory, University of Ulm, D-7900 Ulm, Germany

This paper shows how a relational database management system (DBMS) may be extended in order to solve a complex heuristic search problem DBMS-internally, i.e., without using a host language. To achieve this goal, the query language has been modified to include abstract data types and sophisticated control structures for efficient rule processing. Compared with conventional expert system shells, this expert database approach seems particularly promising for problems that involve large amounts of data. The example application considered in this paper is the overland search problem, where one tries to find the best path between two points on a geographic map. In our system the map is represented by a set of disjoint adjacent polygons and stored in an INGRES relational database. The path search was implemented in a rule-based manner using an extension of the INGRES query language QUEL. In order to improve the performance of our system we also describe how to utilize geographic knowledge and geometric algorithms to perform a hierarchical decomposition of the given search problem.

![](/api/attachments/MKB72PDG/fulltext/images/f0541a4c58350c3ea27c4f84be65a470571b0a712298b8a87cccdc712c0df11d.jpg)

Oliver Günther received the Diploma degree in industrial engineering and applied mathematics from Karlsruhe University (Germany) in 1984, and the M.S. and Ph.D. degrees in computer science from the University of California at Berkeley in 1985 and 1987, respectively. Before returning to Germany, he was a Postdoctoral Fellow at the International Computer Science Institute (ICSI) in Berkeley and an Assistant Professor at the University of California, Santa Barbara.

Since 1989, he has been with FAW Ulm, a new computer science research laboratory in Ulm, Germany, where he heads the Environmental Information Systems Division. His research interests include spatial databases and data structures, solid modeling, geographic information systems, and knowledge-based systems. He has several publications in these areas, including a book entitled Efficient Structures for Geometric Data Management (Springer-Verlag). Most recently, he coedited the proceedings of the First Symposium on the Design and Implementation of Large Spatial Databases (SSD '89). He is also the program chair of SSD '91 and a consultant to various government agencies and industrial companies on issues relating to environmental data management.

A preliminary version of this paper was presented at the BTW Conference on Database Systems for Office Automation, Engineering and Scientific Applications, Darmstadt, Germany, and published in its proceedings [Günther87]. Since then the paper has been substantially revised and extended.

Keywords: Expert database systems, Spatial data bases, Overland search problem, Heuristic search.

## 1. Introduction

Many of the prototype expert systems that are currently available are designed for applications that involve only relatively small amounts of data. In this case, the required data can be kept in main memory; it is not necessary to provide special features for an efficient data management. In many practical applications, however, the amount of data involved exceeds the capacity of current main memories by far. There are three possibilities to deal with this problem:

(i) by extending expert system shells to support large persistent databases [Barbedette90];

(ii) by interfacing expert system shells with DBMSs [Jarke84, Abarbanel86, Ceri86];

(iii) by extending DBMSs to support rule systems and inference mechanisms [Stonebraker86, Stonebraker90].

This paper gives an example for the third approach. The relational DBMS INGRES and its query language QUEL are extended by abstract data types in order to facilitate spatial operations [Stonebraker83] and by sophisticated control structures to support inference mechanisms and efficient rule processing [Stonebraker86]. Then we solve a complex heuristic search problem DBMS-internally, i.e., without using a host language. We therefore avoid many of the problems that are typical for an embedded query language approach. In particular, this solution avoids the inherent performance penalties associated with each single access from a host language to the database. Each such access requires a context switch from the host language to the query language, the execution of the query, the transfer of the results to the data structures of the host language, and another context switch back to the host language. In the case of numerous accesses interleaved with short computations in the host language (as is typical for most expert system applications) such an approach becomes prohibitively expensive.

The search problem we chose to illustrate our techniques is the overland search problem, where one tries to find the best path between two points on a geographic map (say San Francisco Airport and the restaurant “Chez Panisse” in Berkeley). This problem has recently received a lot of attention [Kuan84, Parodi84], partly because of its practical relevance, partly because it is a challenging application for rule-based and knowledge-based systems as well as heuristic search. Moreover, this problem raises interesting data management questions due to the enormous amount of data that is encoded in geographic maps. For example, one has to choose appropriate data and storage structures and, if a database is used, design an interface between the database and the path search system. We believe that a database management system is a practical necessity, and we use an INGRES relational database to store the map.

Note that in this paper the overland search problem only serves as an illustrative example for a heuristic search application. The techniques presented here may be applied in other contexts as well, where heuristic and rule-based search is used in connection with large amounts of data. Applications of this kind often occur, for example, in decision support, robotics, or cartography.

The remainder of this paper is organized as follows. Section 2 gives a more concise definition of the overland search problem and introduces the abstraction of the problem that is employed in this paper. Section 3 describes a heuristic system of rules for the greedy path search and shows how to implement it in an extension of the query language QUEL. The following two sections discuss several improvements to this system and their implementation. Section 4 describes a knowledge-based approach for the hierarchical decomposition of the overland search problem. Section 5 presents the concept of map coarsening; on a coarsened map one may find an approximate solution very quickly. Section 6 contains our conclusions.

## 2. The overland search problem

In the overland search problem one tries to find the best path between two given points in a given environment. The solution to such an overland search problem does not only depend on the start and destination point. It also depends on the kind of vehicle used, on the road conditions, on the time of day, on the cost function to be used, and so on. For example, some vehicles are restricted to travel on roads, whereas other vehicles can choose an overland route; the time to cross Golden Gate Bridge during rush hour is about five times higher than during off-peak hours; to minimize fuel consumption one will often choose a different route than to minimize travelling time.

Therefore, an instance of the overland search problem is formally given by a start point and a destination point in the plane, and a scalar cost function. The cost function is defined completely over all points in the plane and indicates the marginal cost of moving the vehicle under the given conditions from a given point into a given direction. The cost function incorporates all data about the vehicle, the road conditions, the time of the day, the minimization criterion, and so on. For practical purposes, the cost function can be thought of as a grey-level map where the degree of darkness of an area reflects the marginal cost to move the given vehicle in this area.

This paper deals with the following abstraction of the overland search problem. Given is a partition of a plane into polygons. The polygons may be concave and may have holes. Each polygon P has a cost coefficient $C_{P}$ . The cost of moving within the polygon P one unit of distance is $C_{P}$ . The direction of the vehicle's move does not matter as long as it stays inside the same polygon. Clearly, this polygon partition of the plane is a simplified version of the grey-level map described above. This approach is in contrast to the approaches of [Kung84] and [Parodi84] where the map is assumed to be discretized and processed into a grid-like graph with costs for each pair of points that are neighbors in the grid.

The main characteristics of the overland search problem are as follows. The database required to store the map information is very large, compared to databased in typical expert systems. The problem can hardly be solved exactly; it usually has to be approached by means of heuristic search. The knowledge base that stores the heuristic rules and geographic knowledge may be large as well, depending on the complexity of the path planning algorithms and the amount of geographic knowledge available. Finally, the problem is inherently geometric, i.e., geometric data types and operators are essential for finding a solution. Except for the last aspect, these characteristics are shared by decision and optimization problems in many other domains, such as business administration or environmental information management.

## 3. A rule system for path generation

This section presents a system of path generation rules that has been designed to simulate the path finding strategy of a human map reader. Most humans seem to perform a best-first strategy: they look for the cheapest nearby areas that lead them closer to their destination and continue from there. This strategy can be simulated by the following heuristic approach.

Note that the rule system itself is not the main focus of this paper. In fact, there may be path planning algorithms and rule systems that are superior to our approach. Our focus is to show how such a rule system can be implemented in an extended relational DBMS.

## 3.1. The algorithm FINDNEXT

In the given abstraction of the overland search problem, the map is represented by a set of adjacent polygons. The cost of moving between two points within the same polygon is proportional to their distance. The solution path will be represented by a list of path nodes. The greedy path search retrieves this path, node by node. In order to find the next path node $\pi_{nex}$ from the current path node $\pi_{cur}$ the following algorithm FIND-NEXT is performed.

Starting at $\pi_{cur}$ , FINDNEXT looks towards the destination $\Omega$ and scans the boundary segments of the current polygon $\Psi_{cur}$ that lie within the optic angle $\alpha$ . $\Psi_{cur}$ has been determined when $\pi_{cur}$ was found; it contains $\pi_{cur}$ and the path from $\pi_{cur}$ to the next path node $\pi_{nex}$ . The optic angle $\alpha$ is the angle that is rooted at $\pi_{cur}$ and halved by the axis ( $\pi_{cur}, \Omega$ ). Its size is to be defined by the user (fig. 1).

![](/api/attachments/MKB72PDG/fulltext/images/8b381ffa57141113a7156827f20ea81a474204cd2791dc83430db861924352af.jpg)  
Fig. 1. An optic angle

FINDNEXT selects the cheapest polygon $\Psi_{nex}$ among all polygons that are adjacent to any of those boundary segments. If $\Psi_{nex}$ is no more expensive than $\Psi_{cur}$ then $\pi_{nex}$ is the closest point within the optic angle that lies on the boundaries of $\Psi_{nex}$ and $\Psi_{cur}$ . If $\Psi_{nex}$ is more expensive than $\Psi_{cur}$ but still feasible, then FINDNEXT prefers $\Psi_{cur}$ over $\Psi_{nex}$ and stays in $\Psi_{cur}$ as long as it leads closer to $\Omega$ . In this case, $\pi_{nex}$ is the point within the optic angle that lies on the boundaries of $\Psi_{nex}$ and $\Psi_{cur}$ and is closest to the destination $\Omega$ .

A polygon is feasible if its cost coefficient is below a given threshold which depends on the vehicle. If all polygons within the optic angle are infeasible then there is some obstacle in the way. In this case, FINDNEXT continues with a larger optic angle, up to an angle of $360^{\circ}$ where all adjacent polygons are taken into consideration. If this does still not yield a new path node, FINDNEXT gives up. Note that a larger optic angle makes FINDNEXT less greedy: it does not only take a rather direct route into consideration but also considers routes that might lead to the destination less directly.

In order to avoid endless loops, FINDNEXT checks each pair $(\pi_{nex}, \Psi_{nex})$ whether it has occurred previously. In that case, the new path node is rejected and FINDNEXT continues from the current path node with the next cheapest adjacent polygon within the optic angle.

If a new path node $\pi_{nex}$ has been found and validated then FINDNEXT checks if the straight line between $\pi_{nex}$ and the old path node $\pi_{cur}$ lies completely within the current polygon $\Psi_{cur}$ . If $\Psi_{cur}$ is not convex there might be some obstacles (in most cases, more expensive polygons) in the way. In this case, FINDNEXT introduces additional path nodes to construct a detour path inside $\Psi_{cur}$ around those other polygons.

Finally, for each new path node $\pi_{nex}$ , FINDNEXT checks if $\pi_{nex}$ is in the same polygon as the destination $\Omega$ . If yes, FINDNEXT is done: it draws the straight line between $\pi_{nex}$ and $\Omega$ , and refines it according to the detour rule mentioned above. Otherwise, $\pi_{cur}$ and $\Psi_{cur}$ are replaced by $\pi_{nex}$ and $\Psi_{nex}$ , respectively, and FINDNEXT enters another iteration.

![](/api/attachments/MKB72PDG/fulltext/images/3f50f92fa3b9eb57ac22b938dc62fe619a00166b68d7ad4dac150c52a5726ea4.jpg)  
Fig. 2. Rule 3 & Rule 1

FINDNEXT can be described more concisely by the following rules. Here, $(\alpha_{0},\ldots,\alpha_{k}=360^{\circ})$ is the user defined increasing sequence of optic angles, and G is the upper cost bound for a feasible polygon. i is initialized as 0.

(1) IF $\pi_{cur}$ and $\Omega$ are in the same polygon THEN let $\pi_{nex}$ be $\Omega$ , execute rule (5), and ELSE STOP

(2) IF the cheapest adjacent polygon within angle $\alpha_{i}$ (looking towards $\Omega$ ) is no more expensive than $\Psi_{cur}$

![](/api/attachments/MKB72PDG/fulltext/images/5f5a361f7e00cc02aff87b4ec72f16815b40162439e20a237876404a9c9ea785.jpg)  
Fig. 3. Rule 2, Rule 5 & Rule 1

THEN let $\Psi_{nex}$ be that polygon, $\pi_{nex}$ be the closest point of $\Psi_{nex}$ that lies within angle $\alpha_{i}$

(3) IF the cheapest adjacent polygon within angle $\alpha_{i}$ (looking towards $\Omega$ ) is more expensive than $\Psi_{cur}$ but has cost $\leq G$ THEN let $\Psi_{nex}$ be that polygon, $\pi_{nex}$ be the point on the common boundary of $\Psi_{cur}$ and $\Psi_{nex}$ that lies within angle $\alpha_{i}$ and is closest to $\Omega$

ELSE IF i < k THEN $\{i := i + 1;$ continue with rule (2)  
ELSE FAILURE.

Table 1
Geometric operators.

<table><tr><td>Operator</td><td>Meaning</td><td>Opd-1</td><td>Opd-2</td><td>Result</td><td>Comments</td></tr><tr><td>$</td><td>stay-in</td><td>line</td><td>polygon</td><td>path</td><td rowspan="2">returns a path inside Opd-2 whose endpoints are the same as the endpoints of Opd-1 returns the point in Opd-2 that is closest to Opd-1</td></tr><tr><td>||</td><td>closest point</td><td>point</td><td>polygon</td><td>point</td></tr><tr><td>@</td><td>adjacency test</td><td>polygon</td><td>polygon</td><td>boolean</td><td></td></tr><tr><td>()</td><td>inclusion test</td><td>point</td><td>polygon</td><td>boolean</td><td></td></tr><tr><td>()</td><td>inclusion test</td><td>polygon</td><td>polygon</td><td>boolean</td><td></td></tr><tr><td>&amp;</td><td>concatenation</td><td>path</td><td>line</td><td>path</td><td></td></tr><tr><td>∪</td><td>union</td><td>polygon</td><td>polygon</td><td>polygon</td><td></td></tr><tr><td>∩</td><td>intersection</td><td>polygon</td><td>polygon</td><td>polygon</td><td></td></tr><tr><td>#</td><td>optic angle</td><td>point</td><td>real</td><td>polygon</td><td>returns the area covered by angle Opd-2 that is rooted at Opd-1 and halved by the line (Opd-1, Ω)</td></tr><tr><td>line</td><td>line</td><td>point</td><td>point</td><td>line</td><td></td></tr><tr><td>length</td><td>length</td><td>path</td><td>-</td><td>real</td><td></td></tr></table>

(4) IF the pair $(\pi_{nex},\Psi_{nex})$ has occurred previously

THEN discard this new path node $\pi_{nex}$ ; continue with the rule and the optic angle that yielded this path node and take the next cheapest polygon for $\Psi_{nex}$ instead.

(5) IF the straight line $(\pi_{cur},\pi_{nex})$ intersects polygons other than $\Psi_{cur}$

THEN construct a detour path inside $\Psi_{cur}$ .

Note, that except the start and the destination point, all path nodes lie on polygon boundaries. Figs. 2 and 3 give examples for the application of these rules. The circled numbers denote the cost coefficients of the polygons, and the optic angle in fig. 3 is $90^{\circ}$ .

## 3.2. Implementation of path generation rules

The map is stored in an INGRES database. The rules are coded in an extension of QUEL that includes abstract data types [Stonebraker83] and sophisticated control structures for efficient rule processing [Stonebraker86, Stonebraker90]. In particular, we use the EXECUTE\* and the EXECUTE-UNTIL command, which are defined as follows.

## EXECUTE\*(QUEL-PROG) where (QUAL)

executes the command sequence QUEL-PROG over and over again until it fails to modify the database or until the qualification QUAL is false.

## EXECUTE-UNTIL (QUEL-PROG)

tries to execute the commands in the command sequence QUEL-PROG one after another until one command does actually have some effect on the database. This command is the only command that will be executed.

The EXECUTE-UNTIL command is applied to the set of rules as EXECUTE-UNTIL (RULES). Each command in RULES represents one of the rules (1), (2), and (3). Hence, only one rule applies to a current point and only one path is alive at a given time. Note that explicit QUEL-statements are only needed for the rules (1), (2), and (3). Rule (4) will be covered in the where clauses, and rule (5) is implied by the stay-in operator (see below).

Table 2  
Performance measurements

<table><tr><td></td><td>Number of nodes on path</td><td>Number of polygons of path</td><td>Time [seconds]</td></tr><tr><td>Example 1</td><td>2</td><td>1</td><td>9</td></tr><tr><td>Example 2</td><td>3</td><td>2</td><td>17</td></tr><tr><td>Example 3</td><td>21</td><td>5</td><td>148</td></tr><tr><td>Example 4</td><td>104</td><td>42</td><td>621</td></tr><tr><td>Example 5</td><td>173</td><td>64</td><td>1120</td></tr></table>

The solution uses the concept of abstract data types to implement the geometric data types polygon, line, path and point, where path is a polygonal line. For the operations that are defined on those types see table 1.

All abstract data types and operators are implemented in C and encapsulated such that they cannot be accessed from the DBMS. All operators are computed at run time. For efficiency reasons, however, the adjacency operator @ is supported by a relation ADJ (poly-1,poly-2) that contains entries for each pair of adjacent polygons on the given map. Therefore the system uses the following four relations.

<table><tr><td>MAP (polygon,cost)</td><td>...</td><td>map polygons</td></tr><tr><td>PATHS (path,cost,cur-poly,cur-pt,next-poly,next-pt)</td><td>...</td><td>paths</td></tr><tr><td>OLD (node,next-poly)</td><td>...</td><td>pairs ( $\pi_{nex}$ ,  $\Psi_{nex}$ )that have occurred previously</td></tr><tr><td>ADJ (poly-1,poly-2)</td><td>...</td><td>map polygon adjacencies</td></tr></table>

The heuristic search can now be coded inside the DBMS as follows. For brevity reasons we only list the code of the MAIN LOOP and of RULE 2.

```txt
range of m,ml,m2,m3 is MAP
range of p is PATHS
range of o is OLD

MAIN LOOP:
EXECUTE * (
    EXECUTE-UNTIL (RULES;
    append to OLD (node = p.next-pt,
    next-poly = p.next-poly)))
where p.cur-pt ≠ Ω

RULE 2:
replace p (path = p.path&(line(p.cur-pt,p.next-pt)$p.cur-poly),
    cost = p.cost + ml.cost * length
    (line(p.cur-pt,p.next-pt)$p.cur-poly),
    cur-poly = p.next-poly,
    next-poly = m3.polygon,
```

```txt
cur-pt = p.next-pt,
    next-pt = p.next-pt||(#(p.next-pt,αi) ∩ m3.polygon)
where m1.polygon = p.cur-poly
and m2.polygon = p.next-poly
and m3.cost = min(m.cost
    where m.polygon @ (p.next-poly ∩ #(p.next-pt,αi))
    and m.cost ≤ m2.cost)
and any (o.node where o.node = p.next-pt||
    (#(p.next-pt,αi) ∩ m3.polygon
    and o.next-poly = m3.polygon)) = 0
```

## 3.3. Performance

The map we used in our experiments is a topographic map of a 36 square mile area of Santa Cruz County, California. This area is extremely mountainous with deep valleys and an extensive river system. The map is represented by a plane partitioning into 420 polygons; the adjacency relation has 2039 tuples. The sequence of optic angles we used was (90°,180°,360°). On a SUN 3/60 we obtained the performance figures (see table 2). As expected, there seems to be an approximate correspondence between the complexity of the path (both measured in polygons and nodes) and the time required to compute it. Note that the number of nodes is typically two to four times higher than the number of polygons of the path, due to the stay-in rule and the non-convexity of the map polygons.

The bulk of the computation time seems to be spent on the underlying geometric operations. In particular, one has to ask complicated queries in order to retrieve certain boundary segments, and to perform expensive computations to find out which boundary segments lie in a given optic angle. In order to speed up the search we suggest the following improvements. First, we propose to utilize geographic knowledge to perform a hierarchical decomposition of the given problem. Second, we describe how to produce a coarse version of the given map, where the system can compute an approximate solution very quickly. From there, the path can be refined further. These suggestions are discussed in detail in the following two sections.

## 4. Hierarchical problem decomposition

In order to speed up the path search, a given overland search problem can be decomposed by rules embodying geographic knowledge about the area. Then the path search can be performed in two phases:

(i) decomposition of the given problem by means of path decomposition rules that incorporate geographic knowledge;

(ii) parallel processing of the subproblems by means of the path generation rules presented in section 3.

For example, suppose a car driver wants to drive as fast as possible from his apartment on Blake Street in Berkeley to “Mc Donald’s” in San Francisco. The only geographic knowledge he has can be stated in the following two rules:

IF you want to go by car from any point in Berkeley to any point in San Francisco as fast as possible

THEN you have to use the Bay Bridge

IF you want to go by car from Blake Street to the Bay Bridge as fast as possible

THEN you have to take Ashby Street.

The application of these two rules yields three subproblems: how to get from Blake to Ashby, how to get from Ashby to the Bay Bridge, and how to get from the Bay Bridge to “Mc Donald’s”. One does not have any geographic knowledge that is applicable to any of these subproblems. Instead one has to resort to a map that approximates the cost function and to a more general rule system like the one described in section 3.

To implement path decomposition rules, we use an additional extension to QUEL: the trigger command EXECUTE\*\*:

## EXECUTE\*\* (QUEL-PROG) where (QUAL)

executes the command sequence QUEL-PROG whenever the qualification QUAL is true. The difference between this command and the EXECUTE\* command is that an EXECUTE\*\* command does not become obsolete when QUAL is or becomes false. It remains active; whenever QUAL becomes true again, the command sequence QUEL-PROG will be triggered, i.e., executed again. This command may be implemented with so-called trigger locks [Stonebraker86].

Given a relation DEC (start,dest) that contains the start and destination point of the route to be decomposed, our example rule may now be coded as follows.

```sql
EXECUTE** (
append to DEC (start = X, dest = 'Bay Bridge')
append to DEC (start = 'Bay Bridge', dest = Y)
delete DEC where DEC.start = X and
DEC.dest = Y)
where DEC.start = X
and DEC.dest = Y
and X( )'Berkeley'
and Y( )'San Francisco'
```

This rule will be triggered whenever the relation DEC contains a tuple $(X, Y)$ where X is a location in Berkeley and Y a location in San Francisco. Note that this decomposition appends two tuples to DEC, which may then trigger other decomposition rules, and so on.

## 5. Map coarsening

The comprehension of most human map readers often involves an initial conceptual coarsening of the given map to obtain an approximate solution path very quickly. The human reader then continues with further refinements of this path, taking more and more details into account.

This approach is also a kind of hierarchical decomposition of the problem. Instead of applying path decomposition rules that are based on geographic knowledge, the map is coarsened. On the coarsened map it is much easier for the search heuristics to recognize larger areas where the cost of moving is relatively low. The resulting main road paths are then subject to further refinements by means of a less coarsened map.

In the given abstraction of the overland search problem, a map can be coarsened by merging adjacent polygons. Thereby the number of polygons will be substantially reduced and the path finding algorithm will yield a path much faster than on the original map. One possibility would be to merge adjacent polygons with similar cost coefficients. The user specifies several disjoint cost ranges whose union is the set of positive real numbers such as, for example: $[0,30)$ , $[30,100)$ , and $[100,\infty)$ . The coarsening algorithm will then merge all adjacent polygons with a cost coefficient in the same range. The cost coefficient of a new polygon is, for example, the average of the cost coefficients of its component polygons.

An experienced user could perform several coarsenings with different cost ranges, let the system find an optimal path for each of the coarsened maps, and then choose the path that seems most appropriate for his purposes. The selection of appropriate cost ranges is a matter of practical experience with the system.

The polygon merging has been implemented using the EXECUTE\* command as follows.

```txt
range of m1,m2 is MAP
EXECUTE* (
    append to MAP(poly = m1.poly ∪ m2.poly,
    cost = ... )
    where m1.poly @ m2.poly
    and (0 ≤ m1.cost < 30 and 0 ≤ m2.cost < 30
    or 30 ≤ m1.cost < 100 and
    30 ≤ m2.cost < 100
    or m1.cost > 100 and m2.cost > 100)
    delete m1
    where m1.poly( )m2.poly
    and m1.poly != m2.poly)
```

When applied to the map described above, the coarsening takes about 660 seconds on a SUN 3/60. The resulting map has 143 polygons, compared to 420 polygons on the original map. Consequently, the times for the path search examples used in section 3.3 dropped by factors between 2.5 and 3.

## 6. Conclusions

In this paper we presented an expert database system for the overland search problem. The resulting system is based on rules and the utilization of geographic knowledge about the area. Our system shows how a relational database system like INGRES can be extended to implement heuristic search algorithms and to manage non-standard data such as geographic maps.

The query language QUEL has been extended by more sophisticated algorithmic control structures, which greatly facilitated programming the search algorithms and rule constructs. Our system also shows the importance of having efficient algorithms and data structures for geometric data available in the DBMS. The heuristic search could not have been coded efficiently without them.

Our results have to be compared to approaches that are based on AI languages such as LISP. Many of these approaches suffer from not having an efficient data management. This major disadvantage will become even more obvious when these systems are used for real-world applications that involve large amounts of data. Database systems, on the other hand, are known for their ability to perform well on large data sets. We therefore believe that extended database systems like the one we proposed will remain a promising topic for future research.

## References

[Abarbanel86] Abarbanel, R. and Williams, M. "A Relational Representation for Knowledge Bases", Proc. 1st International Conference on Expert Database Systems, Charleston, S.C., April 1986.

[Barbedette90] Barbedette, G., “LISPO $_{2}$ : A Persistent Object-Oriented Lisp”, Advances In Database Technology Proc. EDBT '90, Lecture Notes in Computer Science No. 416, Springer-Verlag, Berlin, 1990.

[Ceri86] Ceri, S. et al., "Interfacing Relational Databases and

Prolog Efficiently", Proc. 1st International Conference on Expert Database Systems, Charleston, S.C., April 1986.

[Günther87] Günther, O., "An Expert Database System for the Overland Search Problem", Proc. BTW 87-Database Systems for Office Automation, Engineering, and Scientific Applications, Informatik-Fachberichte No. 136, Springer-Verlag, Berlin, 1987.

[Jarke84] Jarke, M., Clifford, J., Vassilion, Y., "An Optimizing PROLOG Front-End to a Relational Query System", Proc. 1984 ACM-SIGMOD Conf., Boston, Ma., June 1984.

[Kuan84] Kuan, D. et al., "Automatic Path Planning for a Mobile Robot Using a Mixed Representation of Free Space", Proc. First IEEE Conference on Artificial Intelligence Applications, Dec. 1984.

[Kung84] Kung, R. et al., “Heuristic Search in Data Base Systems”, Proc. 1st International Workshop on Expert Database Systems, Kiowah, S.C., October 1984.

[Parodi84] Parodi, A., "A Route Planning System for an Autonomous Vehicle", Proc. First IEEE Conference on Artificial Intelligence Applications, Dec. 1984.

[Stonebraker83] Stonebraker, M. et al., "Application of Abstract Data Types and Abstract Indices to CAD Data", Proc. Engineering Applications Stream of the ACM-SIGMOD Conf., San Jose, Ca., May 1983.

[Stonebraker86] Stonebraker, M. and Rowe, L., "The Design of POSTGRES", Proc. 1986 ACM-SIGMOD Conf., Washington, DC., June 1986.

[Stonebraker90] Stonebraker, M., Rowe, L., Hirohama, M., "The Implementation of POSTGRES", IEEE Trans. Knowledge and Data Eng., Vol. 2, No. 1, March 1990.
