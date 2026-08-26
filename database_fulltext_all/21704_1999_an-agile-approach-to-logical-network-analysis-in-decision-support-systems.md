---
otero_id: 21704
otero_key: "DTB524XT"
title: "An agile approach to logical network analysis in decision support systems"
authors: "Chun-Che Huang"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00091-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An agile approach to logical network analysis in decision support systems

Chun-Che Huang )

Department of Information Management, National Chi-Nan UniÕersity, Pu-Li, Nan-Tau 545, Taiwan

Accepted 4 December 1998

## Abstract

Decision support system DSS is an interactive computer-based system, which helps decision makers utilize data andŽ . models to solve unstructured problems. Current business is undergoing a major paradigm shift that is taking it from traditional management into a world of agility. An agile corporation should be able to rapidly respond to the market changes. Solution approaches to quickly support decision making and model analyzing are crucial in business management. The approaches may support solutions for the decision makers who are geographically separated and operate on differing computer platforms. In this paper, a generalized label-correcting GLC approach is developed to analyze the modelsŽ . represented with logical networks. This GLC approach is agile because by combining various operators and comparators, different types of paths in the networks can be solved with one algorithm for different values of the initial node. The main contribution of this paper is to provide an approach in analyzing the logical networks, and the approach is implemented through the World Wide Web WWW regardless of the geographical constraints and platforms used. Ž . q 1999 Elsevier Science B.V. All rights reserved

Keywords: Decision support system; Model analysis; Logical networks; World Wide Web

## 1. Introduction

Decision support system DSS is an interactiveŽ . computer-based system, which helps decision makers utilize data and models to solve unstructured problems 24 . Managerial decision making is synony-<sup>w</sup> <sup>x</sup> mous with the whole process of management such as planning, modeling and controlling. All managerial activities revolve around decision making 25 . Cur-<sup>w</sup> <sup>x</sup> rent business is undergoing a major paradigm shift that is taking it from traditional management into a world of agility. An agile corporation should be able to rapidly respond to the market changes. Solution approaches to quickly support decision making are crucial. The approaches may support solutions to the decision makers who may be geographically separated and operate on differing computer platforms. Paramount among the challenges of future DSS is the development and delivery of decision support technologies that are agile and portable to ever changing decision situations 3 . The implementation <sup>w</sup> <sup>x</sup> environment through the World Wide Web WWW Ž . is one approach to cope with the challenge.

A major characteristic of decision support systems is the inclusion of a modeling capacity. The representation of systems or problems through models can be done at various degrees of abstraction; therefore models are classified, according to their degree of abstraction, into three degrees: iconic, analog and mathematical models 27 . A logical network is one<sup>w</sup> <sup>x</sup> of useful mathematical models that aim at most for the numerical analysis of DSS. It is constructed with traditional network with logic connectors, e.g., AND, OR and EXCLUSIVE OR. Circuit structural model is an example of logical networks for design of integrated circuits 1 . Graph Evaluation and Review<sup>w</sup> <sup>x</sup> Technique GERT has been used to travel the net- Ž . work with logical nodes 29 . The IDEF3 acronym<sup>w</sup> <sup>x</sup> Ž for a family of Integrated DEFinition methods is a. widely accepted tool for modeling and analysis of business processes. A logical tree is one of such models which helps designers to represent and record the structure involved at the product design 13 . <sup>w</sup> <sup>x</sup> Logical networks have been used in numerous modeling. However, a generic approach for exploring the networks, e.g., determining the paths of interests, is not considered.

Traditional networks networks without logicalŽ connectors used in Project Evaluation and Review. Technique PERT and Critical-Path Method CPMŽ . Ž . are useful to aid in planning and control. Goal decision network GDN is successfully used to iden-Ž . tify optimal solutions and the tradeoffs between problem objectives. Numerous useful algorithms have been developed for the traditional networks, e.g., the label-correcting LC algorithm to determine theŽ . shortest path 6 , the generic preflow-push algorithm<sup>w</sup> <sup>x</sup> to determine the maximum flow path 11 , the outof-kilter algorithm to determine the minimum cost path 18 . However, there are several differences<sup>w</sup> <sup>x</sup> between the logical and the traditional network representations:

1. Logical networks have two types of nodes: activities and logical nodes. There are no logical connectors in traditional networks.

2. The weights, for example, costs, are placed on nodes in a logical network and on edges in some type of traditional network models.

3. In logical networks, different types of flows are considered, e.g., object flow, information and electrical flow. There is normally one notion of flow in traditional networks.

4. In logical networks AND, OR and EXCLUSIVE OR connectors are used. A branch in a traditional network corresponds to an OR relationship.

Networks with logical connectors have been studied by numerous authors. Lunts 14 firstly studied<sup>w</sup> <sup>x</sup> the algebra path by applying Boolean matrix algebra. Yoeli 31 and Moisil 19 extended his results to a<sup>w x</sup> <sup>w x</sup> more general structure. Carre 4 summarized a wide<sup>w</sup> <sup>x</sup> variety of path problems and solved them by matrix operations. However, transforming the matrices is computationally complex.

In this paper, a generalized label-correcting GLCŽ . approach is developed to analyze logical networks based on the label-correcting algorithm 6 , which is a useful tool to determine the shortest path for traditional networks. This GLC approach is agile because by combining various operators and comparators, different types of paths can be solved with one algorithm for different values of the initial node. It aims at quick model analyzing for decision making, and supports the solutions through the WWW to the decision makers who may be geographically separated and operate on differing computer platforms. This paper is organized as follows. Section 2 introduces the logical network modeling. A generalized label-correcting approach is developed in Section 3. Section 4 illustrates two applications. Section 5 concludes the paper. The main contribution of this paper is to provide an agile approach for the analysis of logical models, and the approach is implemented through the WWW regardless of the geographical constraints and platforms used.

## 2. Logical networks

A logical network is a directed graph with logical Ž . AND<sup>r</sup>OR nodes. It is pervasive and arises in numerous application models. Decision making uses the models to aid the managers in determining the solution approaches. The network is used to mimic the behavior of real systems, e.g., electrical product design, business information flow systems and production process planning. The issues involved in the network analysis include the determination of the paths and nodes of interests, e.g., the shortest paths and critical paths. In Sections 2.1 and 2.3, two illustrations of logical networks are presented and the issues are in Sections 2.2 and 2.4, respectively.

## 2.1. IDEF3 modeling

IDEF modeling has become widely used in business process reengineering BPR , total quality man- Ž . agement TQM and concurrent engineering CE Ž . Ž . efforts 5 . The IDEF3 has been extensively used for <sup>w</sup> <sup>x</sup> modeling manufacturing processes. The IDEF3 model can be viewed as a digraph with some logical connectors 17 . One of the main advantages of the<sup>w</sup> <sup>x</sup> IDEF3 model is its simplicity and its vast descriptive power 15 . An IDEF3 model provides several im-<sup>w</sup> <sup>x</sup> portant characteristics for successful analysis of the manufacturing control, i.e., 1 stage description thatŽ . specifies each activity, 2 structure of underlying Ž . stages and 3 flow of objects and their relationship.Ž . The dependencies among activities in an IDEF3 process model are represented as a directed graph Ž . named process graph where a vertex denotes an activity and a directed edge denotes a dependency. In some cases, a single activity may be partitioned into two or more concurrent activities with a logical connector. In others, two or more serial activities may be merged into a single activity with a logical connector.

The graphical syntax of IDEF3 includes boxes, labels, arrows and connection symbols see Fig. 1 .Ž .

A box represents an activity occurring at a certain stage. Relationships between boxes are modeled with three types of links: precedence, relational and object flow. Precedence links express simple temporal precedence between boxes. The relational links highlight the existence of a relationship between two or more boxes; however, no temporal constraint is implied. This relationship is specified by the link description. Such a link use allows the analyst to capture knowledge about a relationship without having to provide a mechanism structure to account for that knowledge. The object flows are a means of highlighting the participation of an object in two box instances. The links provide a mechanism for capturing object related constraints between boxes and carry the same temporal semantics as a precedence link.

The logic of branching in an IDEF3 model is represented with junctions. Junctions are classified as AND Ž . Ž . Ž . & , OR O and EXCLUSIVE OR X . Multiple process paths are classified as fan-in or fan-out corresponding to converging and diverging paths, respectively. The relative timing of process paths that converge or diverge at a junction are classified as synchronous or asynchronous. An example of IDEF3 process flow diagram is shown to represent the component through three operations: in stage A or B, stage C and the inspection stage. At the end, the component is either accepted or rejected Fig. 2 . Ž .

## 2.2. Issues of IDEF3 modeling

The IDEF3 models a manufacturing system with multiple stages where each stage may include more than one production activity. Some stages are high value-adding and some do not add value, e.g., inspection. The manufacturing characteristics and the value-added at each stage may be crucial factors to production control. Focused stages may include 10 :<sup>w</sup> <sup>x</sup>

<sup>Ø</sup> Critical stages CS : the stages along the criticalŽ . path with the total flow time equal to the flow time of the entire product.

<sup>Ø</sup> Value-adding stages VAS : the stages increasing Ž . the value of parts or products.

<sup>Ø</sup> Bottleneck stages BS : the stages utilized most. Ž . Often, the highest volume of WIP occurs at these stages.

<sup>Ø</sup> Batch-production stages BPS : the stages in Ž . which parts are processed in batches to decrease the unit setup cost, e.g., the heat treatment process.

Box

1 Labeled box

& And connector

0 Or connector

Fig. 1. Basic elements of IDEF3.

X Exclusive Or connector <sup>Ø</sup> Assembly stages AS : the stages where assembly Ž . operations are performed after all parts needed have arrived.

![](/api/attachments/DTB524XT/fulltext/images/81126e2b0e2f7c745332af1266a7c3724aa7a0bc70850748e21f2075def4c20e.jpg)  
Fig. 2. Example of IDEF3 process flow diagram.

Among these five focused stages, the AS and BPS stages can be determined without difficulties. The CS, BS and VAS may not be easy to determine. An approach to determine the stages and related paths needs to be developed.

## 2.3. Circuit structural modeling

A typical structural model of a circuit specifies the I<sup>r</sup>O lines calledŽ . nets of the system, its components and the I<sup>r</sup>O signals of each component. The definition of a component includes its type and the specification of its I<sup>r</sup>O terminals. The interconnections are implicitly described by the signal names attached to these terminals. For example, the primary inputs G and H are connected to the OR gate M Fig. Ž 3 . Components include logic gates and function. gates. Logic gates are components characterized by single output and functionally equivalent inputs.

In a circuit system, a natural representation of a structural model is a directed network in which the components and nets are mapped, respectively, into nodes and edges of the network. Every logical-gate component, e.g., gate AND or OR, in the circuit system corresponds to a logical node of the logical network model. For example, AND gate J corresponds to the ‘&J’ node of the logical network in Fig. 4. Non-logical-gate component corresponds to a node, e.g., component N in Fig. 3 corresponds to node N in Fig. 4.

![](/api/attachments/DTB524XT/fulltext/images/f1042aa10a9cbb7c01f3abefb1634c062561f6416dbe167a34bf2cc121284487.jpg)  
Fig. 3. Example of a circuit structural model.

## 2.4. Issues of circuit structural modeling

Modeling plays a central role in the design, fabrication and testing of circuit products. Testing and testable design of circuit products are increasingly important, as the cost of testing is becoming the major component of manufacturing cost of a new product. The emphasis on the quality of the shipped circuit products, coupled with the growing complexity of integrated circuit designs, require testing issues to be considered early in the modeling process such that the design can be modified to simplify the testing process. In this paper, the testing issues are discussed.

Testing of a circuit system is an experiment in which the system is exercised and its resulting response is analyzed to ascertain whether it behaved correctly. After the system has been assembled, the complete system’s behavior turns into a black box of the combined complexity of all its components. For instance, the component’s behavior can be modeled using a state machine, expressing its behavior in terms of states, transitions and conditions. Verifying all state transitions tests the component’s valid behavior. In general, if a component has N states, there are at least N different transitions, each requiring at least one test. In a system with several components, the number of states increases exponentially $( N ^ { k }$ in case of k components . The insufficient access to. individual components often decreases the testability of the system. But, the testability of the system would improve considerably if circuit hardware– software designs incorporate access paths for testing of separates components in the modeling process.

![](/api/attachments/DTB524XT/fulltext/images/fbb526a57ab72f8dcda64bf31fe3d542587a8e092913abc2260f5a987fb96eba.jpg)  
Fig. 4. The logical network of the circuit in Fig. 3.

In structural modeling, the following paths and components are crucial corresponding to the testing system 1,21,28 :<sup>w</sup> <sup>x</sup>

<sup>Ø</sup> Critical path tracing,

<sup>Ø</sup> Shortest path to tracing,

<sup>Ø</sup> Maximum reliability path,

<sup>Ø</sup> Minimum reliability path,

<sup>Ø</sup> Least liable component,

<sup>Ø</sup> Minimum controllability path,

<sup>Ø</sup> Minimum observability path,

<sup>Ø</sup> Transparent path with signal 0,

<sup>Ø</sup> Transparent path with signal 1, and

<sup>Ø</sup> Access path to the point of control and observation PCOŽ .

## 2.4.1. Critical path tracing and shortest path tracing

Critical path and shortest path tracing 1 includes<sup>w</sup> <sup>x</sup> and extends features of earlier fault simulation techniques for combinational circuits 9,23,26 . For every <sup>w</sup> <sup>x</sup> input vector, critical path tracing first simulates the fault-free circuit, then it determines the detected faults by ascertaining which signal values are critical, and the shortest path tracing with respect to the least values.

## 2.4.2. Maximum reliability path, minimum reliability path and least liable component

Reliability analysis of a circuit structural modeling identifies reliable nodes, e.g., least liable components in the model, improves its performance, and decreases operating cost of the testing process. Reliability evaluation of a circuit structural modeling can be complex as the model may include a large number of nodes. This complexity warrants applications of the reliability evaluation techniques.

A maximum minimum reliability path set of anŽ . IDEF3 model is the set of nodes whose functioning ensures the functioning of the model with the most Ž . least reliability value. To compute the reliability value, the reduction approach, the minimal path and minimal cut set methods are useful evaluation methodologies 12 .<sup>w</sup> <sup>x</sup>

## 2.4.3. Minimum controllability path and minimum obserÕability path

In technical terms, testability incorporates controllability and observability. Controllability is a measure of the ease or difficulty of driving a circuit into a known state. Observability is a measure of the ability to determine the logic values present in a circuit. A generally accepted set of measures for controllability and observability at each node of a circuit consists of six values divided into two classes <sup>w</sup> <sup>x</sup> 8 . The two classes are combinational and sequential values, and each class consists of the controllability of achieving a 1 at the node, the controllability for a 0, and the observability of the value at the node. Here, the following notation CC1, CC0, CO, SC1, SC0 and SO, is used:

CC0: combinational controllability values, and the node stuck at 0

CC1: combinational controllability values, and the node stuck at 1

SC0: sequential controllability values, and the node stuck at 0

SC1: sequential controllability values, and the node stuck at 1

CO: combinational observability value

SO: sequential observability value

The examples of controllability and observability equations are presented next 8 .<sup>w</sup> <sup>x</sup>

For a three-input AND gate with inputs X1, X 2 and X 3 and output Y,

$$
\mathrm{CC1} (Y) = \mathrm{CC1} (X 1) + \mathrm{CC1} (X 2) + \mathrm{CC1} (X 3) + 1
$$

$$
\operatorname{CC0} (Y) = \min \left\{\operatorname{CC0} (X 1), \operatorname{CC0} (X 2), \operatorname{CC0} (X 3) \right\}
$$

The combinational observability for input 1 of the AND–OR Invert circuit in Fig. 5 is

$$
\begin{array}{r l} \mathrm{CO} (1) & = \operatorname{Min} \left\{\mathrm{CO} (\mathrm{G}) + \mathrm{CC1} (2) + \mathrm{CC0} (3), \mathrm{CO} (\mathrm{G}) \right. \\ & \left. + \mathrm{CC1} (2) + \mathrm{CC0} (4) \right\} + 1 \end{array}
$$

The sequential observability for node P in Fig. 6 is computed using a similar equation:

$$
\mathrm{SO} (\mathrm{P}) = \mathrm{SO} (\mathrm{N}) + \mathrm{SC1} (\mathrm{Q}) + \mathrm{SC1} (\mathrm{R})
$$

The values of controllability<sup>r</sup>observability for the gates are computed in such a way that the higher numbers are assigned to the gates which are more difficult to control or observe.

## 2.4.4. Transparent path with signal 0 and transparent path with signal 1

Transparent-test mode TTM is a type of testŽ . functions to improve testability 28 . The accessibil-<sup>w</sup> <sup>x</sup> ity problem can be eliminated if the components that constitute a path to the component under test are transparent in the sense that they convey signals without change. Whenever a component becomes a transparent-test mode, it passes incoming events directly to the outgoing events in a predefined way, providing a transparent path from the system inputs to its outputs.

## 2.4.5. Point of control and obserÕation PCO( )

Inserting points at the module boundaries allows one to control and observe interconnections between modules. A PCO inserted in an interconnection between two modules has three operation modes: transparent, observation and test. A complete PCO implementation supports all three modes, however it is also possible to implement only two. In an observation mode, the PCO is used to monitor the content of a data store. In the test mode, the PCO can be used to read and write a data store. A PCO in a system is controlled individually via its input. A common mode can control multiple PCOs.

![](/api/attachments/DTB524XT/fulltext/images/09a89b2dec613c759b78afdaca55645d27853308b8b3afe2a977672ecb244ff9.jpg)  
Fig. 5. AND–OR Invert circuit.

![](/api/attachments/DTB524XT/fulltext/images/6bc361cd7ff8c5b751b3414af420ca276ef27789a276651751295c2329c177c9.jpg)  
Fig. 6. Node observability.

TTM and PCO functionality offers paths between the system environment and the modules embedded. In addition to the test information, these paths can also transport system management information, such as programming updates and data.

In this section, the computations of the path values involve addition, subtraction, multiplication and comparative operations. By combining various operators $( + , \mathrm { ~ - ~ } \mathrm { a n d ~ } \times )$ and comparators $( \geq \mathrm { ~ a n d ~ } \leq ) .$ different types of problems can be solved with one procedure for different values of the initial node. For example, the operator $\cdot + \cdot \cdot$ is used for problems involving adding cost or time, and $\mathbf { \epsilon } \cdot \mathbf { \alpha } \times \mathbf { \epsilon } \cdot \mathbf { \alpha }$ for problems involving reliability. The comparator $^ { \circ } \leq ^ { \prime }$ is used for the minimization problem and $\mathbf { \partial } ^ { \ast } \geq \mathbf { \partial } ^ { \ast }$ for the maximization problem. Next, the generalized label-correcting approach is developed where a generic algorithm is coded with Java language based on the concept of combining various operators and comparators, and is implemented through the WWW environment.

## 3. The Generalized label-correcting approach

A generalized label-correcting GLC algorithmŽ . from the label-correcting algorithm is developed to determine the areas of focus and paths presented in

![](/api/attachments/DTB524XT/fulltext/images/a07ca87702b6824accd07b0f76e1dec30f1976867469e2b59eca3df38a24829d.jpg)  
Fig. 7. The overall architecture of GLC approach.

Section 2. The GLC algorithm is implemented with the Java language. Decision makers use the browsers to construct the network, input the problem type and run the GLC applet through the WWW regardless of what platforms are used Fig. 7 .Ž .

The WWW is a very large collection of clients and servers that support the Hyper Text Transfer Protocol HTTP . This is an open standard and isŽ . implemented on a wide variety of platforms. The popularity of the WWW arises from its being accessible on a wide number of platforms, the ease of moving information from one platform to another and from its graphical user interface usually called aŽ browser . The client uses a browser to help form a. request, send it to a server and receive the results from the server. A server receives and validates the request, retrieves data and delivers them to the requesting client. The result is a mechanism to share data with little regard to distance or to the different computer platforms in use.

The interaction between WWW servers and clients can be classified into three main groups as follows.

Problem types and the corresponding operators, comparators and objectives

<table><tr><td>Problem type</td><td>Node initial value  $D_{\text{int}}$ </td><td>Operator [cpp]</td><td>Operator [op]</td><td>Comparator [cp]</td><td>IDEF3 modeling objective</td><td>Circuit structural modeling objective</td></tr><tr><td>P1</td><td>{Input nodes}</td><td></td><td>Append</td><td>∈</td><td>Accessible stage</td><td>Access path</td></tr><tr><td>P2</td><td>{Destination nodes}</td><td></td><td>Append</td><td>∈</td><td>Set of upstream (downstream) stages</td><td>Set of upstream (downstream) paths</td></tr><tr><td rowspan="7">P3</td><td>∞</td><td>Min</td><td>+</td><td>≤</td><td>Shortest path</td><td>Shortest path</td></tr><tr><td>CC0(I) = CC1(I) = 1</td><td></td><td></td><td></td><td></td><td>Minimum controllability path</td></tr><tr><td>CC0(N) = CC1(N) = ∞</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SC0(I) = SC1(I) = 0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SC0(N) = SC1(N) = ∞</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CO(Y) = 0 SO(Y) = 0</td><td></td><td></td><td></td><td></td><td>Minimum observability path</td></tr><tr><td>CO(N) = ∞ SO(N) = ∞</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P4</td><td>-∞</td><td>Min</td><td>+</td><td>≥</td><td>Critical path</td><td>Critical path</td></tr><tr><td>P5</td><td>-∞</td><td>Π</td><td>*</td><td>≥</td><td>Maximum reliability path</td><td>Maximum reliability path</td></tr><tr><td>P6</td><td>∞</td><td>Π</td><td>*</td><td>≤</td><td>Minimum reliability path</td><td>Minimum reliability path</td></tr><tr><td>P7</td><td>-∞</td><td>Σ</td><td>+</td><td>≥</td><td>Maximum value-adding path</td><td></td></tr><tr><td rowspan="2">P8</td><td>-∞</td><td>Π</td><td>*</td><td>=</td><td></td><td>Transparent path with signal 0</td></tr><tr><td></td><td>Σ</td><td>+</td><td></td><td></td><td>Transparent path with signal 1</td></tr></table>

$D _ { \mathrm { i n t } } \colon$ node initial value in the generalized LC algorithm.  
<sup>w</sup> <sup>x</sup> cpp : the operator for the set of paths connected with AND connectors.  
<sup>w</sup> <sup>x</sup> op : the operator type.  
<sup>w</sup> <sup>x</sup> cp : the comparison operator comparator .Ž .  
CC0: combinational controllability values, and the node stuck at 0.  
CC1: combinational controllability values, and the node stuck at 1.  
SC0: sequential controllability values, and the node stuck at 0.  
SC1: sequential controllability values, and the node stuck at 1.  
CO: combinational observability value.  
SO: sequential observability value.  
I: primary input.  
Y: primary output.  
N: internal node.

Ž .1 The WWW server sends a static file to the client as a result of a HyperText Transmission Protocol HTTP request from the client. This static docu-Ž . ment can be in any format but the formats that are recognized readily by browsers include Hyper Text Mark Up Language HTML , Virtual Reality Model- Ž . ing Language VRML and image files that are inŽ . the standard formats. Other formats may invoke the software on the client in the HTML-formatted page back to the HTTP requesting WWW browser.

Ž . 2 The WWW server can process data in response to input from client browser. Such process can include, for example, extracting the information from the corporate databases in response to the client browser requests using Common Gateway Interface Ž .CGI .

Ž . 3 A program can be downloaded from the WWW server to a client which can then carry out the programmed actions on the client. Programs written in Java are an example of this mode of operation.

![](/api/attachments/DTB524XT/fulltext/images/76f3514a45830c4eadcf665bd16626ea67e15a510ca6d5cbc5cf776867c5f7a2.jpg)  
Fig. 8. The flow chart of the generalized LC algorithm.

The WWW is potentially useful for remote decision making since it allows the disparate functions that are involved in remote decision making to share data relatively easily.

The main idea behind the label-correcting algorithm is that distance between any two nodes i and j satisfies the following optimality condition, $d ( j ) \leq$ $( i ) + c _ { i j }$ for all $( i , j ) \in \{ \mathrm { s e t }$ 4of edges 7 . At each<sup>w</sup> <sup>x</sup> stage, the algorithm maintains a set of distance labels $d ( \cdot )$ Ž . . The label j is either \`; indicating that a directed path from source to node j has not been determined, or it is the length of a directed path from the source to node j. All nodes in the path are tracked by a predecessor index predŽ .j . The following is a formal description of the label-correcting algorithm 20 :<sup>w</sup> <sup>x</sup>

begin

d sŽ . Ž . <sup>s</sup> 0 and pred s <sup>s</sup> 0

d j Ž . <sup>s</sup> \` for each j <sup>g</sup> N <sup>y</sup>  4s

while some edge Ž .i, j satisfies $d ( j ) > d ( i ) + c _ { i j }$

![](/api/attachments/DTB524XT/fulltext/images/8d7715ce2c2c2b6eca0f6ae8381c3e5700a1fd4137db79f8e213f1bd11a51442.jpg)

<table><tr><td>Act-node</td><td>node of an IDEF3 model which is not a logical connector, e.g., an activity node</td></tr><tr><td>&amp;, O, X</td><td>logical connectors</td></tr><tr><td>G</td><td>IDEF3 model</td></tr><tr><td> $G_{j}$ </td><td>sub-model j of IDEF model G</td></tr><tr><td>d(i)</td><td>the distance between the source node and node i</td></tr><tr><td>l(i)</td><td>the value or symbol of node i itself, e.g., cost</td></tr><tr><td>P</td><td>the path(s) determined in the sub-model  $G_{j}$ </td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
do
begin
    $d(j) = d(i) + c_{ij}$ $\text{pred}(j) = i$
end
</div>

end

In this paper, the necessary condition for optimality, ${ d ( j ) \leq d ( i ) + c _ { i j } }$ for all $( i , j ) \in \{ \mathrm { s e t }$ 4  of edges , is applied. By combining various operators and comparators, different types of problems can be solved with one algorithm for different values of the initial node see Table 1 .Ž .

The following notations are used in the generalized LC algorithm:

Table 2  
```txt
Succ(i) the list of activity nodes succeeding act-node i
Stack set of nodes or logical connectors stored according to the first-in-last-out rule
Input to the algorithm The network G
Output of the algorithm According to the objective function (see the last column of Table 1).
The GLC algorithm:
GLC(G)
initialize
begin
push output node into Stack
while stack not empty
pop node i from Stack
if node i = &
for each node j directly connect to node i
create sub-graph Gj
P = [CCP] GLC(Gj)
d(j) = d(i) + d(P)
succ(j) = succ(i) + P
else
for each node j directly connect to node i
if j in succ(i)
```

Process plans

<table><tr><td>Part name</td><td>Process</td><td>Process time (h)</td><td>Machine</td><td>Stage no.</td></tr><tr><td rowspan="4">Shaft</td><td>Sawing</td><td>0.05</td><td>Sawing</td><td> $Stage_{11}$ </td></tr><tr><td>Turning</td><td>0.15</td><td>Lathe</td><td> $Stage_{12}$ </td></tr><tr><td>Heat treatment</td><td>1</td><td></td><td> $Stage_{13}$ </td></tr><tr><td>Finish turning</td><td>0.2</td><td>Lathe</td><td> $Stage_{14}$ </td></tr><tr><td rowspan="5">Housing</td><td>Draw line</td><td>0.01</td><td>Bench work</td><td> $Stage_{21}$ </td></tr><tr><td>Drilling</td><td>0.04</td><td>Drilling machine</td><td> $Stage_{22}$ </td></tr><tr><td>Turning eccentric holes</td><td>0.20</td><td>Lathe</td><td> $Stage_{23}$ </td></tr><tr><td>Drawing line</td><td>0.01</td><td>Bench work</td><td> $Stage_{24}$ </td></tr><tr><td>Drilling</td><td>0.04</td><td>Drilling machine</td><td> $Stage_{25}$ </td></tr><tr><td rowspan="3">Cover</td><td>Turning</td><td>0.1</td><td>Lathe</td><td> $Stage_{31}$ </td></tr><tr><td>Drawing line</td><td>0.1</td><td>Bench work</td><td> $Stage_{32}$ </td></tr><tr><td>Drilling</td><td>0.1</td><td>Drilling machine</td><td> $Stage_{33}$ </td></tr><tr><td rowspan="6">Oval-gear</td><td>Sawing</td><td>0.4</td><td>Sawing machine</td><td> $Stage_{41}$ </td></tr><tr><td>Heat treatment</td><td>1</td><td></td><td> $Stage_{42}$ </td></tr><tr><td>Turning</td><td>0.15</td><td>Lathe</td><td> $Stage_{43}$ </td></tr><tr><td>Draw line</td><td>0.05</td><td>Bench work</td><td> $Stage_{44}$ </td></tr><tr><td>Shaping</td><td>0.1</td><td>Slotting machine</td><td> $Stage_{45}$ </td></tr><tr><td>Hobbing</td><td>0.4</td><td>Hobbing machine</td><td> $Stage_{46}$ </td></tr><tr><td>Sleeve</td><td>Turning</td><td>0.1</td><td>Lathe</td><td> $Stage_{51}$ </td></tr><tr><td>Five parts</td><td>Assembly</td><td>0.2</td><td></td><td>Assembly</td></tr></table>

![](/api/attachments/DTB524XT/fulltext/images/002077d82065e3541dde07b1e3aef1dcd530dc1efe9412b6cb35951a6586ef9b.jpg)  
Fig. 10. IDEF3 model for the oval-gear flow-meter production process.

‘There exist a loop . . . ’ else

succŽ . Ž . j <sup>s</sup> succ i push j into Stack

![](/api/attachments/DTB524XT/fulltext/images/9d37bcae83479d02cb4c89144568e1095e07ea3bc9b965ccce7cdb41837c51ac.jpg)

The flow chart of the generalized LC algorithm is presented in Fig. 8. The algorithm performs a backward search, from a selected output point to all

Fig. 11. The corresponding of logical network.

![](/api/attachments/DTB524XT/fulltext/images/3b9304ec3e2f46213f2bbcdd1f9b43e6fe428e3a76f5bd29fbf0a9a687bbc4f4.jpg)  
Fig. 12. The assembly structure of the oval-gear flow-meter.

accessible points. It processes the Stack of nodes or logical connectors based on the LIFO rule. At each iteration, a node in the stack is pulled out to explore and its precedent node s is are pushed into the Ž . Ž . stack. For the act-node and OR gate, the GLC maintains a set of distance labels dŽ . <sup>P</sup> which satisfies the optimality condition. For the AND gate, an AND stack a recursive subroutine is created. The label-Ž .

correcting algorithm recurs at each AND stack and determine the paths for the sub-graph G j. The algorithm terminates when all nodes in the stack are pulled, i.e., the stack is empty. The running time of the generalized label correcting algorithm is $O ( V ^ { 2 } +$ E., which is the same as Dijkstra’s algorithm, where V is the number of nodes and E is the number of edges.

The decision makers construct a logical network using a browser URL1 . The input window is shownŽ . in Fig. 9. The system assumes that each logical network has the input and output nodes. The procedure of executing the GLC approach can be referred on URL1.

Note that in selecting ‘Problem No’ and ‘Load Demo’ bottoms, the illustrative examples in Section 4 to determine the shortest and critical paths and upstream stages will be presented.

![](/api/attachments/DTB524XT/fulltext/images/61ad7785de22214f82a4fb6c0fa5a6695395f732836cd0ed3067b79c1f015a22.jpg)  
Fig. 13. Stages in the critical path.

## 4. Application

The case studies illustrate the approach presented in Section 3. In Section 4.1, the IDEF3 model of oval-gear flow-meter manufacturing process is applied to. Section 4.2 solves the problem of testing by applying the approach to a circuit structural model.

## 4.1. Application of IDEF3 modeling

The H factory produces oval-gear flow-meters used to measure the flow in the petrol industry. Currently this factory produces 1000 units<sup>r</sup>year. An oval-gear flow-meter is made of five parts. Table 2 presents the process plans for all parts. The IDEF3 model of production process of the oval-gear flowmeter is presented in Fig. 10. The corresponding logical network is presented in Fig. 11. The assembly structure of the oval-gear flow-meter is presented in Fig. 12.

![](/api/attachments/DTB524XT/fulltext/images/edc3bfce086fa1b423679088b79d77c303bf96cb684b94326aa61a1bca792f3b.jpg)  
Fig. 15. The circuit.

In Table 2, $\mathrm { S t a g e } _ { 1 3 }$ and $\mathrm { S t a g e } _ { 4 2 }$ denote the heat treatment processes in which parts are processed at the rate of about one batch per hour. There are two auxiliary operations, heating and cooling of the oven. It takes more than 1.8 h to process a batch from heating the oven to cooling the oven and collecting the parts in a container. The H factory has only one heat treatment facility. In order to achieve maximum efficiency, the oval-gears and shaft are treated in one batch whenever enough of them are available. Furthermore, each of the stages $S _ { \mathrm { S t a g e } _ { 1 4 } }$ $\mathrm { S t a g e } _ { 2 3 }$ and $\mathrm { S t a g e } _ { 4 6 }$ involves more than 0.2 hour of processing time. These stages add value to the parts, however, a high WIP occurs. This manufacturing system is a mixture of a job shop and flow shop. The upstream stages $\mathrm { S t a g e } _ { 1 3 }$ and $\mathrm { S t a g e } _ { 4 2 }$ process parts in batches. The assembly system is of a flow shop. The final products, oval-gear flow-meters, are produced in a repetitive mode.

![](/api/attachments/DTB524XT/fulltext/images/5783a648e0b6fb136de90980d75097dfa9beec65e14ba9c9b1e26b5af8d6f709.jpg)  
Fig. 14. Upstream stages of the bottleneck machine $\mathrm { ( S t a g e _ { 1 3 } }$ or ${ \mathrm { S t a g e } } _ { 4 2 } ) .$

![](/api/attachments/DTB524XT/fulltext/images/f4e45aa5f5b60cb41d15d7bfa136a318e6fa58a7c4ff54d7a99f135e540d3c76.jpg)  
Fig. 16. The logical network of the circuit in Fig. 15.

Determination of the following set of stages in IDEF modeling aims at choosing the production control policy, push or pull:

$\mathrm { \mathbf { S } } _ { 1 } \mathrm { \dot { : } }$ set of critical stages

$\mathrm { S } _ { 2 } \mathrm { : }$ set of downstream value-adding stages

$\mathrm { S } _ { 3 } \mathrm { : }$ set of upstream bottleneck stages

$\mathrm { S } _ { 4 } \mathrm { : }$ set of upstream batch-production stages

${ \bf \cal S } _ { 5 } \mathrm { : }$ set of upstream assembly stages

BPS, BS and VAS.

The implementation of the push–pull approach is as follows:

G is the digraph in Fig. 11.

$$
\text { Node   set } = \{\text { Stage } _ {1 1}, \text { Stage } _ {1 2}, \text { Stage } _ {1 3}, \text { Stage } _ {1 4},
$$

$$
\text { Stage } _ {2 1}, \text { Stage } _ {2 2}, \text { Stage } _ {2 3}, \text { Stage } _ {2 4}, \text { Stage } _ {2 5},
$$

$$
\text { Stage } _ {3 1}, \quad \text { Stage } _ {3 2}, \quad \text { Stage } _ {3 3}, \quad \text { Stage } _ {4 1}, \quad \text { Stage } _ {4 2},
$$

$$
\left. \text {Stage} _ {4 3}, \text {Stage} _ {4 4}, \text {Stage} _ {4 5}, \text {Stage} _ {4 6}, \text {Stage} _ {5 1} \right\}
$$

$$
\mathrm{AS} = \{\text { Assembly } \}
$$

$$
\mathrm{BPS} = \{\text {Stage} _ {1 3}, \text {Stage} _ {4 2} \}
$$

Apply the generalized LC algorithm. The following solutions are obtained:

<sup>Ø</sup> Critical stages $\mathrm { S 1 } = \mathrm { \{ S t a g e _ { 4 1 } } $ , Stage , Stage , <sub>42 43</sub> $\mathrm { S t a g e _ { 4 4 } , S t a g e _ { 4 5 } , S t a g e _ { 4 6 } , A s s e m b l y } \}$

Table 3  
Controllability values

<table><tr><td>N</td><td>CC0(N)</td><td>CC1(N)</td></tr><tr><td>6</td><td>2</td><td>3</td></tr><tr><td>7</td><td>2</td><td> $\infty$ </td></tr><tr><td>8</td><td>2</td><td>3</td></tr><tr><td>9</td><td>2</td><td>2</td></tr><tr><td>10</td><td>7</td><td>4</td></tr></table>

<sup>Ø</sup> BPS <sup>s</sup>  4 Stage , Stage <sub>13 42</sub>

$\mathbf { S } _ { 4 } = \{ \mathrm { S t a g e } _ { 1 1 } , \mathrm { S t a g e } _ { 1 2 } , \mathrm { S t a g e } _ { 4 1 } \}$

${ \bf B } { \bf S } = \{ \mathrm { S t a g e } _ { 2 3 } , \mathrm { S t a g e } _ { 1 4 } \}$

<sup>Ø</sup> S <sup>s</sup>  4 Stage , Stage <sub>3 21 22</sub>

<sup>Ø</sup> There is no VAS in the digraph GŽ . N, E .

$\mathrm { S } _ { 5 } = \{ \mathrm { S t a g e } _ { 2 4 } , \mathrm { S t a g e } _ { 2 5 } , \mathrm { S t a g e } _ { 3 1 } , \mathrm { S t a g e } _ { 3 2 } , \mathrm { S t a g e } _ { 3 3 } ,$ $\mathrm { S t a g e } _ { 5 1 } \}$

The stages in the critical path and the upstream stages of the bottleneck machine are presented in Figs. 13 and 14, respectively. With the sets determined, the production control strategy, push or pull control, can be decided based on the characteristics and value-added at these stages in the production control DSS.

## 4.2. Application of circuit structural modeling

The generalized LC approach is more useful in various ways to determine the testability values, points and paths.

Example 4.2.1: Consider the circuit in Fig. 15, which is an important module in the design of circuit product 16 . The determination of the minimum <sup>w</sup> <sup>x</sup> controllability and observability paths is fuzzy and crucial in the concurrent engineering field. The logical network of the circuit in Fig. 15 is presented in Fig. 16.

The result: Applying the generalized LC algorithm with the values in Tables 3 and 4, the minimum controllability and observability paths to the output is: 6,10 or 8,10 . The output window of the mini- 4  4 mum controllability path is presented in Fig. 17.

Table 4  
Observability values

<table><tr><td>N</td><td>CO(N)</td></tr><tr><td>6</td><td>5</td></tr><tr><td>7</td><td>5</td></tr><tr><td>8</td><td>5</td></tr><tr><td>9</td><td>∞</td></tr></table>

With the relevant controllability<sup>r</sup>observability value of components determined, the components desired are included to the generation of products in the circuit product design DSS. Furthermore, with the relevant testability points<sup>r</sup>paths determined seeŽ Table 1 , the corresponding test functionality points. are placed at the point<sup>r</sup>path boundary based on IEEE standards, e.g., the standard 1149 22 . <sup>w</sup> <sup>x</sup>

Example 4.4.2: Consider the ANS 310 module 30 .<sup>w</sup> <sup>x</sup> Determine the minimum signal loss path to output 2 in the logical network in Fig. 18 P3 type problem inŽ

Table 1 . The node in this logical network is either a. function gate or logic gate. Assume that each label number denotes the signal loss in a gate, l iŽ . where i<sup>s</sup>0 to 10.

The result: For any node j, the shortest path to Output 2 is SuccŽ . Ž . j , of the length <sup>s</sup> d j . For an instance, the minimum signal loss path from Input 1 to Output 2 <sup>s</sup> Succ 0Ž . <sup>s</sup>  4 0, 1, 2, 7, output 2 . The length<sup>s</sup>dŽ . Ž . 0 <sup>s</sup>10 Fig. 19 . Note that the minimum signal loss path is solved with the problem type P3. The signal loss in each component corresponds to the cost of each node in the shortest path problem.

‘Signal loss’ is one of the selection criteria which differ mainly by cost functions to measure quality assessment in testing. In case the ‘signal loss’ is

![](/api/attachments/DTB524XT/fulltext/images/e70ed4ccd9ebbf55fbea43bf48c8eecd7fec2c269a25cc8dbafb33618e99bd22.jpg)  
Fig. 17. The minimum controllability path of the circuit in Fig. 16.

![](/api/attachments/DTB524XT/fulltext/images/9b903ea9adf3ea02c0448859b374c3f6b03aeeee69dac003499f21b3254efde5.jpg)  
Fig. 18. The logical network of the ANS 310 module.

replaced with other selection criterion, e.g., signal delay time or testability value, the approach solves the corresponding fault searching problem 2 . With the relevant minimum ‘selection criterion’ path determined, the testability of circuit products can be enhanced in the design DSS.

![](/api/attachments/DTB524XT/fulltext/images/8b55bc8ddac9c7df63a3be06cb811efc630049a95ce2d5d33eaf6b72dd52e6ba.jpg)  
Fig. 19. The minimum signal loss path in Fig. 18.

## 5. Conclusions

In this paper, the logical networks were introduced. The generalized label-correcting GLC ap- Ž . proach was presented to analyze the logical networks and determine the desired paths and stages presented in Section 2. Two applications were illustrated. The paths determined with the GLC approach supported the decision making in production control and circuit product design<sup>r</sup>testing. This GLC approach is agile because, by combining various operators and comparators, different types of paths can be solved with one algorithm for different values of the initial node. The main contribution of this paper is to provide the GLC approach to analyzing the logical networks, and the approach is implemented through the WWW regardless the geographical constraints and what platforms are used.

The following issues require further studies: 1Ž . the production control rules for various focused stages need to be developed to determine whether the push or pull approach should be applied in the non-ideal manufacturing DSS environment; 2 anŽ . expert system supporting the guidelines to identify testability points and paths need to be developed for decision support in the circuit product design; 3Ž . interface programs need to be developed to transfer any network into the default logical network automatically.

## Acknowledgements

This work was partially supported by funds from the National Science Council of Taiwan NSC87-Ž 2218-E-260-004 ..

## References

<sup>w</sup> <sup>x</sup> 1 M. Abramovici, M. A Breuer, A.D. Friedman, Digital Systems Testing and Testable Design, IEEE Press, New York, 1990, pp. 26–29.

<sup>w</sup> <sup>x</sup> 2 V.D. Agrawal, M.R. Mercer, Testability measures—what do they tell us? Digest of Papers 1982 International Test Conference, 1982, pp. 391–396.

<sup>w</sup> <sup>x</sup> 3 T.X. Bui, Decision support in the future tense, Decision Support Syst. 19 2 1997 149–150. Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 B. Carre, Graphs and Networks, Clarendon Press, Oxford, England, 1979, pp. 81–85.

5 R.B. Chase, N.J. Aquilano, Production and Operations Management: A Life Cycle Approach, Richard D. Irwin, Homewood, IL, 1985.

<sup>w</sup> <sup>x</sup> 6 L.R. Ford, Network Flow Theory, Report of Rand, Santa Monica, CA, 1956, p. 239.

7 L.R. Ford, D.R. Fulkerson, Flows in Networks, Princeton Univ. Press, NJ, 1962.

<sup>w</sup> <sup>x</sup> 8 L.H. Goldstein, E.L. Thigpen, Scoap: Sandia Controllability<sup>r</sup>Observability Analysis Program, Proceedings of the 17th Design Automation Conference, ACM, 1980, pp. 190–196.

<sup>w</sup> <sup>x</sup> 9 S.J. Hong, Fault Simulation Strategy for Combinational Logic Networks, Design of Papers 8th Annual International Conference on Fault-Tolerance Computing, 1978, pp. 96–99.

<sup>w</sup> <sup>x</sup> 10 C.-C. Huang, A. Kusiak, Manufacturing control with a push–pull approach, Int. J. Product. Res. 36 1 1998Ž . Ž . 251–275.

<sup>w</sup> <sup>x</sup>11 A.V. Karzanov, Determining the maximal flow in a network by the method of preflow, Soviet Math. Dokl. 15 1974Ž . 434–437.

<sup>w</sup> <sup>x</sup> 12 A. Kusiak, A. Zakarian, Reliability evaluation of process models, IEEE Trans. Components, Packaging, and Manufacturing Technol., Part A 19 2 1996 268–275.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 A. Kusiak, E. Szczerbicki, A formal approach to specifications in conceptual design, ASME J. Mech. Design 114 12 Ž . Ž . 1992 659–666.

<sup>w</sup> <sup>x</sup> 14 A.G. Lunts, The application of Boolean matrix algebra to the analysis and synthesis of relay-contact networks, Dokl. Akad. Nauk., SSSR 70 1950 421–423.Ž .

<sup>w</sup> <sup>x</sup> 15 R.J. Mayer, T.P. Cullinane, P.S. de Witte, W.B. Knappenberger, B. Perakath, M.S. Wells, Information Integration for Concurrent Engineering IICE IDEF3 Process Description Ž . Capture Method Report, Armstrong Laboratory, Wright-Patterson AFB, Ohio 45433, AL-TR-1992-0057, 1992.

16 A. Miczo, Digital Logic Testing and Simulation, Harper& Row, New York, 1990, p. 269.

<sup>w</sup> <sup>x</sup> 17 C. Menzel, R.J. Mayer, D.D. Edwards, IDEF3 process descriptions and their semantics, in: C.H. Dagli, A. Kusiak Ž . Eds. , Intelligent Systems in Design and Manufacturing, ASME Press, New York, 1994, p. 174.

<sup>w</sup> <sup>x</sup> 18 G.J. Minty, Monotone networks, Proc. R. Soc. London A 257 1960 194–212.Ž .

<sup>w</sup> <sup>x</sup> 19 G.R. Moisil, Asupra unor representari ale grafurilor ce intervin in problem de economia transorturilor, Comunle. Acad. Rep. Pop. Rom. 10 1970 647–652.Ž .

<sup>w</sup> <sup>x</sup> 20 E.F. Moore, The shortest path through a maze, Proceedings of the International Symposium on the Theory of Switch, Part II, 1957, pp. 285–292.

<sup>w</sup> <sup>x</sup>21 F.W.E. Ozguner, W.E. Donath, C.W. Cha, On fault simulation techniques, J. Design Automation and Fault-Tolerant Comput. 3 4 1979 83–92.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 K. Parker, The Boundary-Scan Handbook, Kluwer Academic Publishers, Boston, MA, 1992.

<sup>w</sup> <sup>x</sup> 23 J.P. Roth, W.G. Bouricius, P.R. Schneider, Concurrent hierarchy fault simulation, IEEE Trans. Comput. EC 16 10Ž . Ž . 1967 567–579.

<sup>w</sup> <sup>x</sup> 24 M.S. Scott-Morton, Management Decision System: Computer Based Support for Decision Making, Division of Research, Harvard Univ., Cambridge, MA, 1971.

25 H. Simon, The New Science of Management Decision, Prentice-Hall, Englewood Cliffs, NJ, 1977.

<sup>w</sup> <sup>x</sup> 26 S.Y.H. Su, Y.-C. Cho, A new approach to the fault location of combinational circuits, IEEE Trans. Comput. C 21 1Ž . Ž . 1972 21–30.

<sup>w</sup> <sup>x</sup> 27 E. Turban, Decision Support and Expert Systems, Prentice-Hall, Englewood Cliffs, NJ, 1995, p. 42.

<sup>w</sup> <sup>x</sup> 28 H.P.E. Vranken, M.F. Witteman, R. van Wuijtswinkel, Design for testability in hardware–software systems, IEEE Design and Test of Comput. 12 3 1996 79–81.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 Gary E. Whitehouse, Systems Analysis and Design Using Network Techniques, Prentice-Hall, Englewood Cliffs, NJ, 1973.

<sup>w</sup> <sup>x</sup> 30 Wu-Tain, Handbook of Circuit Design, Wu-Tain, Taiwan, 1990.

<sup>w</sup> <sup>x</sup> 31 M. Yoeli, A note on a generalization of Boolean Matrix Theory, Am. Math., Mon. 68 1961 552–557. Ž .

![](/api/attachments/DTB524XT/fulltext/images/d4faf592af02008efe5dce7236070661e4db41e070726bd86840b466f6196eee.jpg)

Chun-Che Huang received the PhD degree in Industrial Engineering from the University of Iowa, Iowa City in 1997, and the MS degree in Operations Research from Columbia University, New York, NY in 1994. He is an Assistant Professor in the Department of Information Management, National Chi-Nan University, Taiwan. He is interested in DSS, intelligent systems and concurrent engineering. His papers have appeared in, among others, IEEE Transactions on

Systems, Man and Cybernetics, IEEE Transactions on Components, Packaging and Manufacturing Technology, International Journal of Production Research and Computer-Aided Design.
