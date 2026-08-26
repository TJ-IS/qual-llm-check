---
otero_id: 16875
otero_key: "78426RC6"
title: "Sequencing nonprocedural financial models"
authors: "G.R. Finnie"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90243-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sequencing Nonprocedural Financial Models

G.R. FINNIE

Department of Computer Science, University of Natal, P.O. Box 375, Pietermaritzburg 3200, Republic of South Africa

Any nonprocedural language must be mapped to a procedural form for evaluation. This paper suggests a general method for establishing an evaluation sequence in nonprocedural financial modelling systems using directed graphs and topological sorting. Simultaneous equations in the model give rise to cycles in the graph and must be extracted for separate processing.

Keywords: Nonprocedural Languages; Financial Models; Directed Graphs; Topological Sorting; Simultaneous Equations.

![](/api/attachments/78426RC6/fulltext/images/f0b2181febc0b5b91e9c6724b2244f35ee0294ceae804375daa0d8f1ddeea048.jpg)

Gavin R. Finnie has been Senior Lecturer in the Department of Computer Science at the University of Natal in Pietermaritzburg since 1981. He holds an MSc in Computer Science and an MBA from the University of Cape Town and is currently completing a DBL at the University of South Africa. He is a Fellow of the South African Institute of Computer Scientists. His research interests include Decision Support Systems, Human Factors in computing and Expert Systems.

## 1. Introduction

The issue of ‘user-friendliness’ is one that has enjoyed considerable attention in decision support systems (DSS) and decision support system generators. One aspect of this concept which remains a point of controversy is the degree to which the user language is procedural. Although many system designers equate nonprocedural with ‘user-friendly’, much of the little empirical research evidence available appears to support the value of the procedural approach. Welty and Stemple [1], for example, found that there appeared to be a point of problem complexity beyond which a procedural specification proved simpler. Soloway et al. [2] found a positive carryover from procedural language training to problem solving ability, using algebra word problems as an example. Sime et al. [3] suggest that both sequential and descriptive information are necessary in problem solving. Proponents of the nonprocedural approach, however, believe that this is a more ‘natural’ technique. Lee [4], for example, holds the view that knowledge may be more simply specified in a declarative (nonprocedural) form and models using this knowledge should be simpler to specify nonprocedurally.

Novice and occasional users of financial modelling systems constitute an important DSS user class. The author is currently developing a simplified nonprocedural financial modelling system to investigate the role of procedurality and other aspects of user-friendliness in the man-machine interface. There appears to be little published literature on techniques for establishing an evaluation sequence in these systems; thus, a method based on topological sorting of directed acyclic graphs was developed. The graph could also provide a useful measure of the degree to which these specific nonprocedural features are used.

## 2. Nonprocedural Financial Modelling Systems

Financial modelling systems are becoming increasingly popular in business planning and, as most users are not computer experts, 'simplicity of use' has been a major design factor. Commercially available systems provide examples of both procedural and nonprocedural (e.g., IFPS) approaches [6]. The system under development is fairly similar to IFPS.

Financial models map directly onto a matrix of data: the rows in the matrix correspond to variables; the columns generally refer to time periods, although they may be used in a stand-alone capacity, e.g., for totals. An example of a simple model with its equivalent data matrix is given in Fig. 1. The keywords LAST and NEXT are used here to refer to entries in columns preceding or succeeding the current column, respectively.

In a general nonprocedural financial modelling system a variable entry (i.e., a specific matrix position) may effectively refer to any other location in the matrix. In order to evaluate any location correctly, all items referenced by this location must have been previously assigned a value. An order of evaluation for the entire model must thus be established.

## 3. Using Directed Graphs (Digraphs)

The relationship between all locations in the data matrix can be represented as a directed graph or a set of directed graphs. Direction is established in the sense that a variable is 'dependent on' the values of other variables or a variable is 'depended upon' by other variables. Arcs are drawn from a variable to those variables whose value it requires. The model of Fig. 1 can be represented as the directed graph in Fig. 2, where the subscript indicates the column and I is INVENTORY, C is CASH OUT, and S is SALES. Row 10 would not be included to avoid unnecessary resequencing.

<table><tr><td>5</td><td>COLUMNS 1-4</td><td></td><td></td><td></td></tr><tr><td>10</td><td>OPENING INVENTORY = 120,0</td><td></td><td></td><td></td></tr><tr><td>20</td><td>INVENTORY = OPENING INVENTORY+CASHOUT-SALES*0.5, LAST INVENTORY+CASHOUT-SALES*0.5</td><td></td><td></td><td></td></tr><tr><td>30</td><td>CASH OUT = NEXT SALES*0.5 FOR 3,250</td><td></td><td></td><td></td></tr><tr><td>40</td><td>SALES = 150, 200, 300, 400</td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>10</td><td>120</td><td>0</td><td>0</td><td>0</td></tr><tr><td>20</td><td>145</td><td>195</td><td>245</td><td>295</td></tr><tr><td>30</td><td>100</td><td>150</td><td>200</td><td>250</td></tr><tr><td>40</td><td>150</td><td>200</td><td>300</td><td>400</td></tr></table>

Fig. 1. Sample Model with Data Matrix.

The compilation phase of the system under development is responsible for establishing the directed graph(s) using an adjacency list technique. In order to avoid unnecessary resequencing for cases in which variables are already in evaluation order, the compiler will only build graphs within a specific forward reference range and resequencing is performed as soon as a range is exceeded. Variables within this range which are dependent only on variables preceding this range may also be excluded.

Once the graph is fully established a set of candidate 'root' nodes (vertices) is extracted by determining those vertices which have no arcs entering them, e.g., I4 in Fig. 2. These variables are not depended upon by any other location. If no such vertex can be established, a set of simultaneous equations exists and must be handled separately (see below).

Topological sorting is a well-established method for ordering directed acyclic graphs in applications such as critical path analysis (see, e.g., [7]) Topological sorting will provide a linear ordering of the graph in the sense that if there is an arc from vertex i to vertex j then i appears before j in the ordering.

A depth-first algorithm for topological sorting is given below [7]. The algorithm uses a stack to hold any vertex until all descendants of that vertex are visited, at which stage it is released from the stack. All successors of a vertex v are held on a list L[v]. The evaluation sequence is held in a vector SEQUENCE:

procedure dfs (v: vertex)

![](/api/attachments/78426RC6/fulltext/images/47bfa11d83db355c761493fac9d715429b752bded76d20d6b8ecc29ca7f93325.jpg)  
Fig. 2. Directed Graph for Sample Model.

```vhdl
begin
    mark[v]:=visited;
    push(v, stack);
    for each vertex w on L[v]do
    if mark[w]=unvisited then
    dfs(w);
    sequence[next]:=top(stack); next:=next + 1;
    pop(stack)
end;
```

Using a depth-first search the output is in reverse order which is in fact the evaluation sequence required. The actual sequence deduced is, of course, dependent on the ordering of dependent nodes in $L[v]$ . Applying this algorithm to Fig. 2 with starting point I4 and a left-to-right order of descendants will give the evaluation sequence:

## S1 S2 C1 I1 S3 C2 I2 S4 C3 I3 C4 I4

If a number of candidate root vertices exist then each is used as an entry point for a depth-first search. This ensures that all vertices in a particular graph are visited and that all graphs are processed.

Although the elimination of arbitrary sequencing is only one aspect of the concept of nonprocedurality [8], the amount of resequencing required is a useful measure of the degree to which this specific feature is used. Although simple 'forward reference' counts could be used, a more sophisticated measure could be based on the depth-first spanning forests for the digraphs generated during compilation and on the depth-first search numbers determined during the search process. The spanning forests are defined by tree arcs, i.e., arcs that lead to unvisited vertices during the search. The number of tree arcs together with the depth of the related vertices could provide a measure suitable for experimental comparison of subjects, although not necessarily as an absolute measure. Several alternative forms of this measure are being investigated experimentally in conjunction with forward reference measures.

## 4. Simultaneous Equations

Topological sorting can only be applied to acyclic directed graphs. A problem arises when simultaneous equations are introduced into a model as these give rise to cycles due to variable interdependency. An example of a model containing simultaneous equations with its equivalent graph is given in Fig. 3.

Simultaneous equations can occur at any stage in a model and the depth-first search must test continuously for loops in the graph. If no root vertex has been established then one is arbitrarily selected and all vertices are treated as potential roots. In the latter case it is necessary to test for unvisited vertices following completion of each search. This case is unlikely to arise frequently in real applications.

Although this search for cycles is potentially time-consuming search efficiency can be improved by using depth-first numbering. All descendants of a particular vertex i are assigned search numbers greater than that assigned to i. Four types of arcs can be distinguished in directed graphs, viz. tree arcs, forward arcs, back arcs and cross arcs. A cycle exists if there is a corresponding back arc. Forward arcs and tree arcs go from low-numbered to high-numbered vertices while back arcs and cross arcs go from high-numbered to low-numbered vertices. If a descendant of a vertex has a lower search number than the vertex itself then a simple check against the stack will determine whether this is a back arc, i.e., whether a cycle exists. As cross arcs link vertices which are neither descendants nor ancestors of each other in the particular section of the graph being searched, these vertices would not appear in the stack. In most practical cases forward arcs or tree arcs will appear so the search procedure should not dramatically impact efficiency. Consider as an example the graph in Fig. 3. Assuming the arc D → A is traversed before $D \rightarrow C$ , the contents of the stack with depth-first search numbers will be as in Fig. 4. When D is visited as a descendant of B the lower search number implies the existence of a back arc or cross arc. A check of the stack will confirm that D is also an ancestor of B, i.e., the arc $B \rightarrow D$ is a back arc.

![](/api/attachments/78426RC6/fulltext/images/3a7d6413ad9354944749f879d7cfa9a87553c7e75917681cc667628169ee8a16.jpg)  
Fig. 3. Model and Digraph for Simultaneous Equations.

<table><tr><td>Stack</td><td>Search Numbers</td></tr><tr><td>B</td><td>4</td></tr><tr><td>A</td><td>3</td></tr><tr><td>D</td><td>2</td></tr><tr><td>E</td><td>1</td></tr></table>

Fig. 4. Stack Contents when Visiting Vertex B.

Once simultaneous equations are detected, those vertices within the loop are marked and the back arc may be ignored. The elements of this group will be in sequence in the stack. This is because each descendant of a vertex is searched to completion before the search is continued from that vertex. Using Fig. 3 again, if vertices F and G appeared before B on L[A], these and all their descendants would have been visited and popped from the stack before B is pushed onto the stack.

As members of the simultaneous group are popped from the stack they would be held as a separate list and, until the last member of the group is released, it is necessary to compare all descendants of any member of the group against this list. This test is required as it is possible that an inner loop has been detected which is in fact part of a larger set of simultaneous equations. Consider again the situation in Fig. 3. If the loop $D \rightarrow A \rightarrow B$ has been detected, vertices A and B will have been released from the stack before vertex C is visited. The system must note the arc $C \rightarrow A$ , determine that A is part of the simultaneous group and include C as part of this set. When the last member of this group is popped from the stack, the entire set must be added to the evaluation sequence for simultaneous solution.

Techniques such as Gauss-Seidel iteration could be used here.

## 5. Conclusion

Topological sorting provides a relatively general purpose technique for establishing sequence in nonprocedural financial models. The method is to a certain extent removed from the language and the translation method used which has the advantage, in an experimental environment, of allowing fairly flexible language development and enhancement. The complexity and depth of the graphs could also provide a suitable measure for the amount of resequencing required in models. This and other measures will be extracted for further research on the man-machine interface for novice and occasional users.

## References

[1] C. Welty and D.W. Stemple, Human Factors Comparison of a Procedural and a Nonprocedural Query Language, ACM Trans. Database Systems 6/4 (1981) 626–649.

[2] E. Soloway, J. Lockhead and J. Clement, Does Computer Programming enhance Problem Solving Ability, in: R.J. Seidel, R.E. Anderson and B. Hunter, Eds., Computer Literacy (Academic Press, New York, NY, 1982).

[3] M.F. Sime, T.R.G. Green and D.J. Guest, Scope Markings in Computer Conditionals – a Psychological Evaluation, Int. J. Man–Machine Studies 9 (1977) 107–118.

[4] R.M. Lee, Epistological Aspects of Knowledge-Based Decision Support Systems, in: H.G. Sol., Ed., Processes and Tools for Decision Support (North-Holland, Amsterdam, New York 1982; ISBN 0-444-86569-1).

[5] J.I. Pfaltz, Computer Data Structures (McGraw-Hill, New York NY, 1977).

[6] IFPS Users Manual, Execucom Systems Corporation.

[7] A.V. Aho, J.E. Hopcraft and J.D. Ullman, Data structures and Algorithms (Addison-Wesley, Reading MA, 1983; ISBN 0-201-00023-7).

[8] B.M. Leavenworth and J.E. Sammet, An Overview of Nonprocedural Languages, ACM Sigplan Notices 9/4 (1974) 1–12.
