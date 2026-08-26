---
otero_id: 21711
otero_key: "UZ89VUP6"
title: "Metagraphs in workflow support systems"
authors: "Amit Basu; Robert W. Blanning"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00006-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Metagraphs in workflow support systems

Amit Basu <sup>)</sup>, Robert W. Blanning <sup>1,</sup> <sup>2</sup>

Owen Graduate School of Management, Vanderbilt UniÕersity, NashÕille, TN, USA

## Abstract

Workflow support systems contain a network of tasks that process documents, some of which share common information elements. Metagraphs, an extension of directed graphs and hypergraphs, have been used to model the interactions among other types of DSS information: stored data, decision models, and expert knowledge. We show that metagraphs can also be used to model the interactions among workflow tasks and thus provide a comprehensive tool for modeling the various types of information managed by a DSS. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Workflow systems; Graph theory; Metagraphs; Higher-level views

## 1. Introduction

Increasing automation of business processes has led to the need for decision support tools that assist in the management of the complex workflows that are created due to the various activities in these processes. In recent years, there has been much interest, both within academic research circles and among business practitioners, in software systems for this purpose. We will call such systems workflow support systems WSS .Ž .

Workflows arise in the context of process management. Processes such as order fulfilment, new product development, and corporate budgeting cut across traditional organizational functions such as purchasing, manufacturing, distribution, and marketing. Process management takes place at three levels, and this layering is reflected in the design of WSS, as we will see in Section 4. These levels are:

<sup>Ø</sup> Top level: requirements analysis, in which one attempts to determine the customer needs that the process can help to fulfil.

<sup>Ø</sup> Middle level: resource allocation, in which revenues and other resources people, equipment,Ž etc. are allocated to tasks..

<sup>Ø</sup> Lower level: process logistics, to include scheduling, quality control, etc.

The need for effective process management has led to the need for effective workflow management <sup>w</sup> <sup>x</sup> 14,16,19 , which in turn has led to the development of commercially available workflow management tools 15,24 and to proprietary tools developed for<sup>w</sup> <sup>x</sup> specific purposes 22 . In addition, attempts have <sup>w</sup> <sup>x</sup> been made to uncover important process and workflow concepts by organizations such as the Workflow Management Coalition 26 and IBM 21 .<sup>w x</sup> <sup>w x</sup>

Although a few tools for workflow specification and analysis have been developed, available methodology for workflow analysis is still sparse. Most of the existing tools and frameworks are directed to workflow logistics rather than higher-level workflow support. For example, Burger et al. 13 used the<sup>w</sup> <sup>x</sup> HyTime modeling language to construct SGML DTDs i.e., document templates for a publishing Ž . application, Bubler and Jablonski 12 developed a<sup>w</sup> <sup>x</sup> prototype relating workflow processes to organization structures in order to assign people to workflows, Kumar and Zhao 17 developed a methodol- <sup>w</sup> <sup>x</sup> ogy for dynamic routing and integrity control in workflow systems, and Levine and Aurand 18 used<sup>w</sup> <sup>x</sup> the SIMAN simulation language to analyze possible workflow delays in a proposed document processing office. But it would be useful to have a methodology for structuring workflows and viewing them in terms of their fundamental components, such as information elements, documents, and tasks.

One approach that shows promise in this regard is based on a graph-theoretic construct called a metagraph 6 . A metagraph is similar to a directed graph,<sup>w</sup> <sup>x</sup> or digraph, in that it consists of elements and edges, but a metagraph edge connects two sets of elements, rather than a pair of elements as in a digraph. The elements in a metagraph represent atomic data items, such as the name of a person applying for a loan, the loan amount, or a credit rating. The invertices and outvertices of the edges represent documents, such as a loan application or a credit rating, which are sets of information elements. Finally, the edges in the metagraph represent workflow tasks, such as the task of determining an applicant’s credit rating or the task of making a loan decision. The purpose of constructing a metagraph is to examine its connectivity properties, which suggest ways in which the tasks may be integrated.

In this paper we will summarize the salient features of metagraphs and examine their use in integrating tasks into workflows. In Section 2 we will define metagraphs, differentiating them from the more traditional digraph structures, and we will also examine the connectivity properties of metagraphs and their applications to workflow systems. In Section 3 we will explore the notion of higher-level views and demonstrate that these views provide additional information for workflow support. Then in Section 4 we will present the concept of a workflow support system, which integrates task-oriented workflow information with three traditional types of decision support information—stored data, decision models, and production rules—to produce a single framework that encompasses both traditional DSS and workflow support.

## 2. Workflows and metagraphs

A workflow is defined here as a network of tasks that receive certain documents and transform them into other documents. The documents consist in turn of information elements, some of which may be found in several documents. Thus, there are three fundamental workflow concepts.

<sup>.</sup> Tasks: These may be human tasks, such as reviewing a loan application and other documents and making a loan decision, or computer-based tasks, such as retrieving a credit rating from a file. In many cases they will be computer-supported tasks performed by humans.

<sup>.</sup> Documents: These are the inputs and outputs of the tasks, such as a loan application or a credit report.

<sup>.</sup> Information elements: Each document is a set of information elements, such as a person’s name, credit rating, etc. A single information element may be found in several documents, and a single document may contain several information elements.

Thus, a workflow is a network of tasks, each of which may be described as a pair of information elements, one providing input to the task and one containing the output of the task. A task is viewed here as a ‘black box’ that transforms one set of information elements, in the form of a document, into another set of information elements, also in the form of a document. Since the documents associated with different tasks may have some information elements in common e.g., some tasks may provideŽ information to other tasks , the tasks are interdepen-. dent. Metagraphs are a useful way of analyzing such a structure.

Metagraphs extend the concept of directed graphs, or digraphs, which represent directed relationships between pairs of elements 10 , and of hypergraphs, <sup>w</sup> <sup>x</sup> in which edges are undirected sets of elements 11 .<sup>w</sup> <sup>x</sup> Important metagraph concepts, such as connectivity, are also found in digraphs, but metagraphs capture more fully the complexity of the interactions found in modern information systems 7,8 .<sup>w</sup> <sup>x</sup>

Consider the workflow illustrated in Fig. 1, the purpose of which is to determine whether a company should invest in a production facility. The system consists of four information elements and two tasks. Since there are two tasks, there are four documents, corresponding to the inputs and outputs of the tasks. The information elements, which are collectively called the generating set of the metagraph, are as follows:

INV identifier of the production facility proposed for investment

CAP capacity of the proposed production facility

UTIL utilization rate of the proposed production facility

REV revenues resulting from the proposed production facility

EXP expenses resulting from the proposed production facility

The two edges represent the following tasks.

Ž . 1 $\mathrm { e } _ { 1 }$ is performed by an operations analyst who accesses information about the proposed production facility and analyzes this information to determine the resulting production or service delivery capacity

Ž . 2 $\mathbf { e } _ { 2 }$ is performed by a financial analysis team that determines revenue and expense given the capacity and utilization of the proposed production facility.

The four documents, which are represented by the invertices and outvertices of the edges tasks , are asŽ . follows. The invertex of $\mathrm { \bf e } _ { 1 }$ is the singleton set INV 4 and the outvertex is the singleton set CAP , which 4 makes $\mathrm { \bf e } _ { 1 }$ very similar to a digraph edge. However, the invertex of $\mathbf { e } _ { 2 }$ is the set CAP, UTIL , and the  4 outvertex of $\mathrm { e } _ { 2 }$ is the set REV, EXP . The coinput  4 of an element in the invertex of an edge is the set of all other elements in the invertex to that edge, and the cooutput of an element in the outvertex of an edge is the set of all other elements in the outvertex. Thus, the coinput of CAP in $\mathbf { e } _ { 2 }$ is UTIL and the  4 cooutput of REV in $\mathrm { e } _ { 2 }$ is EXP . Coinputs represent 4 additional information needed to invoke a task corresponding to an edge, and cooutputs represent additional information that will be available once the task is invoked.

![](/api/attachments/UZ89VUP6/fulltext/images/2d5fe5310881c1a69433a565314879554dea86819a0d97608dfa23375e6d8d91.jpg)  
Fig. 1. A metagraph.

An important issue in workflow management is the relationship among various tasks. It may be the case that some tasks must be completed before others can begin, or there may be several sets of tasks that can be used to arrive at the same result. Intertask relationships are analyzed by examining the connectivity properties of the metagraph.

The simplest form of connectivity is represented by a path. As with digraphs, a path is a sequence of edges that connect two elements. We will use the term ‘simple paths’ for reasons that will soon become apparent. Given two elements, the first of which is called the source and the second of which is called the target, a simple path connecting them is a sequence of edges such that 1 the source is in theŽ . invertex of the first edge in the sequence, 2 theŽ . target is in the outvertex of the last edge in the sequence, and 3 for each pair of adjacent edges in Ž . the sequence the intersection of the outvertex of the first edge and the invertex of the second edge is non-null. For example, the sequence of edges $\langle \mathbf { e } _ { 1 } ,$ $\mathbf { e } _ { 2 } \rangle$ in Fig. 1 is a simple path connecting INV to REV.

Simple paths, like edges, have coinputs and cooutputs. The coinput of the source element in a path is the set of all elements in the invertices of the edges in the path, other than the source, that are not also in the outvertices of some edge in the path. For example, the coinput of INV in $\langle \mathbf { e } _ { 1 } , \mathbf { e } _ { 2 } \rangle$ is UTIL . 4 The cooutput of the target element in a simple path is the set of all elements in the outvertices of edges in the path other than the target. The cooutput of REV in $\langle \mathbf { e } _ { 1 } , \mathbf { e } _ { 2 } \rangle$ is the set CAP, EXP . 4

The interpretation of coinputs and cooutputs for a simple path is analogous to that for edges. The coinput of the source is the set of all elements, other than the source and any intermediate outvertex elements along the path, needed to invoke the edges in the path. For example, INV is not sufficient to determine REV; UTIL must be known as well. The cooutput of the target is the set of all elements, other than the target, whose values are determined by invoking the edges in the path. This information, CAP and EXP in our example, represents ‘free’ or ‘byproduct’ information obtained in the process of determining the value of the target.

The concept of a simple path as a sequence of edges, analogous to a path in digraphs, is not sufficient to describe connectivity in metagraphs. To see why, consider the example of Fig. 2, which represents a loan approval process with four elements and three tasks. The elements are as follows:

APP the loan application

CRED credit evaluation report for the applicant VIA viability report on the project for which the loan is requested

DEC the approval<sup>r</sup>disapproval decision

The tasks represented by the edges are as follows. $\mathrm { e } _ { 3 }$ is the task of evaluating the creditworthiness of the applicant, performed by a credit analysis team. $\mathrm { e } _ { 4 }$ is the task of analyzing the viability of the project for which the loan is requested, performed by a specialist team.

$\mathrm { e } _ { 5 }$ is the task of approving or disapproving the loan, performed by the vice president for finance.

We note that there is no simple path connecting APP to DEC with a null coinput. There are indeed two simple paths with APP as source and DEC as target, $\langle \mathbf { e } _ { 3 } , \mathbf { e } _ { 5 } \rangle$ and $\langle \mathbf { e } _ { 4 } , \mathbf { e } _ { 5 } \rangle$ , but the first has coinput  4  4 VIA and the second has coinput CRED . But one should not infer from this that it is impossible to use APP alone to determine DEC. One needs only to invoke all three tasks—that is, the tasks represented by the edges, $\mathrm { e } _ { 3 } , \mathrm { e } _ { 4 }$ , and $\mathrm { e } _ { 5 } .$ . The only problem is that this is not a simple path, since it is a set of edges and not a sequence; $\mathrm { e } _ { 3 } , \mathrm { e } _ { 4 }$ and $\mathrm { e } _ { 5 }$ cannot be arranged in a sequence. Therefore, we need a more general concept of a path, which we will call a metapath 3,8 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/UZ89VUP6/fulltext/images/8cd12d006576d867c44c7a24d69990bb5dc0b13d4caf5475ab06f843a9bb4f04.jpg)  
Fig. 2. Metagraph with metapath.

A metapath, like a simple path, connects a source to a target. However, the source and the target are sets, not elements. In this example they are singleton sets, but they need not be. A metapath from a source set to a target set is a set not a sequence of edgesŽ . such that 1 each element in the invertex of anyŽ . edge in the metapath is found in the source or in the outvertex of some edge in the metapath, 2 eachŽ . element in the target is found in the outvertex of some edge in the metapath, and 3 each edge in theŽ . metapath lies on a simple path from some element in the source to some element in the target and all of the other edges in that simple path are in the metapath as well. The first of these conditions ensures that the source elements are sufficient to invoke the edges in the metapath; the second condition ensures that all of the target elements are determined once the metagraph edges have all been invoked; and the third condition ensures that there are no ‘isolated’ edges—that is, edges that do not contribute to the invocation of edges in the metapath.

Thus, in the example of Fig. 2 we can invoke $\mathrm { e } _ { 3 }$ with APP to obtain CRED; we can invoke $\mathrm { e _ { 4 } }$ with APP to obtain VIA and we can invoke $\mathrm { e } _ { 5 }$ with both CRED and VIA to obtain DEC. Thus, the set of edges $\{ \mathbf { e } _ { 3 } , \ \mathbf { e } _ { 4 } , \ \mathbf { e } _ { 5 } \}$ is a metapath from the source  4  4 APP to the target DEC . We note that a metapath differs from a simple path in three ways: 1 theŽ . source and target are sets rather than elements, 2Ž . the edges in the metapath are a set rather than a sequence, and 3 the concept of a coinput is unnec-Ž . essary because the source is sufficient to determine the target.

The definition of a metapath requires us to omit ‘irrelevant’ edges—that is, edges that are not on a path from a source element to a target element. However, it does allow us to include redundant edges or redundant source elements. A redundant edge is one that is not needed to determine the value of a target element because the metapath contains another edge that can be used for the same purpose. An example is the metagraph illustrated in Fig. 3, which is the same as that of Fig. 2 except for the inclusion of edge $\mathrm { e } _ { 6 } .$ . We can see that there are three metapaths from APP to DEC. The first, as before, is $\{ \mathbf { e } _ { 3 } , \ \mathbf { e } _ { 4 } , \ \mathbf { e } _ { 5 } \}$ , the second is $\{ \mathbf { e } _ { 6 } \}$ , and the third is $\{ \mathbf { e } _ { 3 } , \mathbf { e } _ { 4 } , \mathbf { e } _ { 5 } , \mathbf { e } _ { 6 } \}$ . Similarly, if there were an additional information element not connected to the metagraph —for example, a gross national product GNP, then either of the two metapaths identified above would also be a metapath from the source APP, GNP to 4  4 DEC . However, GNP is redundant, since APP is sufficient to calculate DEC without GNP. A metapath that contains redundant edges or redundant source elements is said to be nondominant. A dominant metapath is a metapath in which 1 it is not possibleŽ . to remove any edges from the metapath and still have a metapath from the source to the target and 2Ž . it is not possible to remove any of the source elements and still have a metapath from the remaining source elements to the target. Thus, the metapath $\{ \mathbf { e } _ { 3 } ,$ $\mathbf { e } _ { 4 } , \mathbf { e } _ { 5 } , \mathbf { e } _ { 6 } \}$ from APP, GNP to DEC is nondomi-  4  4 nant for two reasons. First, it contains redundant edges: the set of edges $\{ \mathbf { e } _ { 3 } , \mathbf { e } _ { 4 } , \mathbf { e } _ { 5 } \}$ and the singleton set containing the edge $\{ \mathbf { e } _ { 6 } \}$ . Both of these sets of edges are metapaths from APP, GNP to DEC , 4  4 and either one can be eliminated without destroying the connectivity from APP, GNP to DEC . Sec-  4  4 ond, this metapath contains a redundant source element, GNP, which is not needed to determine the value of DEC.

![](/api/attachments/UZ89VUP6/fulltext/images/da4d1a8479c3b137e3fe62b5b5e26bcf1d6215be7e9821fbc25c3d3cbc9bd5b3.jpg)  
Fig. 3. Metagraph with non-dominant metapath.

The examples given above have been illustrated with diagrams. However, it is possible to analyze metagraphs using an algebraic structure based on matrices 7 . The principal matrix is an adjacency <sup>w</sup> <sup>x</sup> matrix, which is analogous to the adjacency matrices used in digraphs. A metagraph adjacency matrix, denoted A, is a square matrix with one row and one column corresponding to each element in the generating set. Each member of the matrix is a set of zero or more triples, one for each edge in which the row element is in the invertex and the column element is in the outvertex. If there are no such edges, then the member of the matrix is null.

Consider the metagraph of the investment evaluation process illustrated in Fig. 1. In this case $\begin{array} { r } { \mathsf { a } _ { \mathrm { C A P , U T L } } = \mathsf { n u l l } , \mathsf { a } _ { \mathrm { R E V , E X P } } = \mathsf { n u l l } , } \end{array}$ , and $\mathbf { a } _ { \mathrm { I N V , U T I L } } =$ null. If there are one or more edges connecting the row and column elements, then there is a triple in the corresponding member of A for each such edge. The triple consists of the following components: 1 theŽ . coinput of the row element in the edge, 2 theŽ . cooutput of the column element in the edge, and 3Ž . the edge. For example

$$
\begin{array}{l} \mathrm {a_ {\text {INV,CAP}} = \{\langle \text {null,null,} \langle e_ {1} \rangle\rangle\}} \\ \mathrm {a_ {\text {CAP,REV}} = \{\langle \{\text {UTIL} \}, \{\text {EXP} \}, \langle e_ {2} \rangle\rangle\}} \\ \mathrm {a_ {\text {UTIL,EXP}} = \{\langle \{\text {CAP} \}, \{\text {REV} \}, \langle e_ {2} \rangle\rangle\}} \end{array}
$$

There is a multiplication operator for metagraph matrices that will identify simple paths connecting the elements. When the matrices are the same, repeated multiplication will produce powers of the matrix, denoted $\mathbf { A } ^ { n } .$ . Each member of $\mathbf { A } ^ { n }$ consists of zero or more tuples, one for each simple path of length n connecting the row element with the column element. In our example, $\mathbf { A } ^ { n }$ consists entirely of null members except for the following:

$$
\begin{array}{l} \mathrm {a_ {\text { INV,REV }} ^ {2}} = \{\langle \{\text { UTIL } \}, \{\text { CAP,EXP } \}, \langle \mathrm {e_ {1} , e_ {2}} \rangle \rangle \} \\ \mathrm {a_ {\text { INV,EXP }} ^ {2}} = \{\langle \{\text { UTIL } \}, \{\text { CAP,REV } \}, \langle \mathrm {e_ {1} , e_ {2}} \rangle \rangle \} \end{array}
$$

Since there are no paths of lengths greater than two, we have $\mathbf { a } _ { \mathrm { X , Y } } ^ { n } =$ null for all elements X and Y and for $n > 2$

The closure of a metagraph adjacency matrix is the sum $\mathbf { A } + \mathbf { A } ^ { 2 } + \mathbf { A } ^ { 3 } + \ldots$ , where the sum of two adjacency matrices is a member-by-member union of the triples in each row–column intersection. Since the multiplication operator is defined so that a cycle need not be traversed more than once, $\mathbf { A } ^ { n }$ will consist entirely of null members when for all n greater than the number of edges in the metagraph. With the closure we can find all simple paths of any length in the metagraph. Therefore, we can find all metapaths, since they are unions of the edges in simple paths. We can also find all cycles, since a cycle is a simple path from an element to itself and will be disclosed by non-null members in some of the diagonal members of the closure of A.

## 3. Higher-level views of workflows

We now examine three higher-level views of workflows, each of which can be modeled with metagraphs. The first view is a projection 3 . This is a way of focusing on a few of the elements in a metagraph and examining any relationships among them. For example, in the metagraph of Fig. 3 we may be interested only in the set of elements APP, DEC . The set on which we wish to focus must be a4 subset of the generating set. A projection of the original metagraph, which we will now call the base metagraph, along this subset of the generating set is a metagraph in which only the elements in the subset can appear and in which any dominant metapaths connecting these elements in the base metagraph appear as edges in the projection. The projection of the metagraph in Fig. 3 along the subset APP, DEC 4 is illustrated in Fig. 4. It is a single edge, $\mathbf { e ^ { \prime } } ,$ , with  4  4 invertex APP and outvertex DEC . The edge $\mathbf { e ^ { \prime } }$ represents the fact that there is at least one dominant metapath connecting APP to DEC . In fact there 4  4 are two dominant metapaths, $\{ \mathbf { e } _ { 3 } , \mathbf { e } _ { 4 } , \mathbf { e } _ { 5 } \}$ and $\{ \mathbf { e } _ { 6 } \}$

The purpose of a projection is to allow us to simplify a base metagraph by taking a higher-level view of the elements that are important to us while preserving the relationships among them as repre-Ž sented by the edges . This might be of use to a. manager or analyst who cares only about investments and the resulting returns on these investments, but is not interested in any intermediate elements. In this case the fact that the loan application document is sufficient to determine the loan decision is important, but how this is done i.e., which edges areŽ invoked and which other elements are involved is. not important.

![](/api/attachments/UZ89VUP6/fulltext/images/d5dcf87a337f55378e0b1fde4bd4fb0d8a31ea1a2ac0eec38c728bb27d7d1543.jpg)  
Fig. 4. A projection.

![](/api/attachments/UZ89VUP6/fulltext/images/41395e253066c029f8f63c4fba7c81835906129b7c0dcd3b8defd9efc94eda33.jpg)  
Fig. 5. A conditional metagraph.

Second, we examine the concept of assumptions and contexts 1 . An assumption is a proposition— <sup>w</sup> <sup>x</sup> that is, a statement that may be either true or false—that appears in the invertex of an edge and that must be true for the edge to be used in a metapath. Assumptions appear in the generating set along with the other elements. For example, the metagraph in Fig. 5 is similar to that of Fig. 3 except that there are two assumptions: hist and int. The first assumption, hist, is the statement ‘‘A history of previous investments is available.’’ If this assumption is true, then the edge $\mathrm { e } _ { 6 }$ can be used to calculate DEC directly from APP. The second assumption, int, is ‘‘The interest rate is nor more than 15%,’’ and this must be true before $\mathrm { e } _ { 5 }$ can be used in a metapath.

For example, if int is known to be true and hist is known to be false, then the context of the metagraph in Fig. 5 becomes the metagraph in Fig. 2, in which $\mathrm { e } _ { 6 }$ is eliminated because hist is false and int is eliminated from the invertex of $\mathrm { e } _ { 5 }$ because int is true. It can be demonstrated that context and projection are commutative—that is, for any conditional metagraph and any context and projection operator, one can apply the projection and then the context or one can first apply the context and then the projection; the result will be the same. For example, the projection of the metagraph in Fig. 2 along the set of elements APP, DEC is the metagraph in Fig. 6,  4 which is similar to that of Fig. 4 except that the edge $\mathrm { e } ^ { \prime \prime }$ represents the metapath $\{ \mathbf { e } _ { 3 } , \mathbf { e } _ { 4 } , \mathbf { e } _ { 5 } \}$ . Similarly, the projection of the metagraph in Fig. 5 along the set of elements APP, DEC with the assumptions hist and  4 Ž int included in the projection is the metagraph in. Fig. 7, in which $\mathrm { e } ^ { \prime \prime \prime }$ represents the metapath $\{ \mathbf { e } _ { 6 } \}$ and $\mathrm { e } ^ { \prime \prime \prime \prime }$ represents the metapath $\{ \mathbf { e } _ { 3 } , \mathbf { e } _ { 4 } , \mathbf { e } _ { 5 } \}$ . The context of this projection with int assumed to be true and hist assumed to be false, is also the metagraph in Fig. $^ { 6 , }$ in which $\mathbf { e ^ { \prime } }$ once again represents the metapath $\{ \mathbf { e } _ { 3 }$ $\mathbf { e } _ { 4 } , \mathbf { e } _ { 5 } \}$

![](/api/attachments/UZ89VUP6/fulltext/images/16cc3519fc7f4188d318bbcfda134cd0cfa9820c5670d29d31235d26bde2d1db.jpg)  
Fig. 6. Context and projection.

![](/api/attachments/UZ89VUP6/fulltext/images/efc37e363248dd9e989a16906ef4ad39d5ea6bfae58f1ce3fcf1ebd3a85fda8d.jpg)  
Fig. 7. Projection of the conditional metagraph.

The third view of a metagraph is a dual 4 . In this <sup>w</sup> <sup>x</sup> case the edges in the original primal metagraphŽ . become the elements in the dual and vice versa. The dual of a metagraph is not itself a metagraph, but it provides an important view of the flows of information elements between the edges in the metagraph. Thus, a dual is similar to a data flow diagram.

The dual of the primal metagraph in Fig. 2Ž . appears in Fig. 8. There are two new objects in the dual not found in the primal—the source vertex and the sink vertex. There is an edge from the source vertex corresponding to each ‘pure’ input element in the primal—that is, corresponding to each element in the primal that is not in an outvertex of some edge in the primal. Similarly, there is an edge leading into the sink corresponding to each ‘pure’ output element in the primal—that is, corresponding to each element in the primal that is not in an invertex of some edge in the primal. The remaining edges in the dual correspond to information elements in the primal, and vice versa.

![](/api/attachments/UZ89VUP6/fulltext/images/c6ab385c42b8adfe4a97336e77bced1514d91a0597298817e0dc2bcd60702ab8.jpg)  
Fig. 8. Dual metagraph.

![](/api/attachments/UZ89VUP6/fulltext/images/3abb7cf46ea21105d64fafbd111dc849e42ae676b7ddafc76a06128036d664e4.jpg)  
Fig. 9. Pseudodual metagraph.

That a dual is not a metagraph can be seen from the interpretation of CRED and VIA leading into the dual vertex $\{ \mathbf { e } _ { 5 } \}$ . A metagraph interpretation would suggest that either CRED or VIA would be sufficient to execute $\mathrm { e } _ { 5 } .$ . However in a dual, multiple edges leading into a vertex represents and ‘AND’ relationship rather than an $\cdot _ { \mathrm { O R } } ,$ relationship. However, it is possible to transform the dual into a pseudodual, in which case the metagraph interpretation obtains, but the resulting metagraph is not analogous to a data flow diagram. The pseudodual appears in Fig. 9, and the edge denoted corresponds to the conjunction of the primal elements CRED and VIA.

## 4. The design of workflow support systems

In a WSS structured tasks, both manual and automated, are central components. The principal types of information are documents, which are represented by the invertices and outvertices of edges, and the edges correspond to human tasks 5 . However, the<sup>w</sup> <sup>x</sup> edges may also correspond to components of a DSS, and specifically to stored data, decision models, and production rules in a knowledge-based system. We will first describe in more detail how metagraphs may be used in designing a WSS and then describe briefly the use of metagraphs in integrating WSS with DSS.

As we pointed out briefly in Section 1, a WSS will operate at three levels. At the top level we are concerned with the customer requirements that give rise to the need for a workflow system and with the way in which the system relates to other DSS components. For example, one might begin with the projection illustrated in Fig. 4 stating that we need to be able to determine the ROI resulting from the investment. This might then be elaborated to produce a data flow diagram, in the form of a dual metagraph, as shown in Fig. 8. The dual metagraph would then be transformed into the primal metagraph of Fig. 2, at which point the assumptions hist and int and the additional task ${ \mathrm { e } } _ { 6 }$ would be added to produce the conditional metagraph of Fig. 5. Alternatively the assumptions could be identified first, giving the projection of Fig. 7, and this would then be elaborated to produce the conditional metagraph of Fig. 5.

At the middle level, we are concerned with the allocation of revenues to perform workflow tasks and therefore with the selection of tasks to be performed. At this point we determine the truth values of the assumptions, and we identify the specific sets of tasks forming a metapath from the available information source to the required information identi-Ž . fied at the top level target . For example, if we find,Ž . as we assumed in Section 3, that int is true and hist is false, then the metapath illustrated in Fig. 2 would be selected. If both int and hist are true, then we must choose between the metapaths $\{ \mathbf { e } _ { 3 } , \mathbf { e } _ { 4 } , \mathbf { e } _ { 5 } \}$ and $\{ \mathbf { e } _ { 6 } \}$ . If both int and hist are false, then we must do further work to identify tasks and<sup>r</sup>or assumptions that will allow us to arrive at the decision DEC from the available information.

At the lower level, we are concerned with scheduling, transaction management, error detection, etc. This includes monitoring the WSS to detect or anticipate existing or impending problems. The principal contribution of metagraphs at this level is to provide a framework for the development of lowerlevel scheduling and monitoring systems.

An important issue found at all levels of a work flow system is the allocation of resources. Examples of resources are a market research team, a specialized forecasting package, or a powerful workstation. To some extent, resource allocation can be accomplished using the metagraph tools described in Sections 2 and 3, and specifically the notions of assumptions and conditional metagraphs. That is, the requirement that a resource be available before a task can be executed can be viewed as an assumption. For example, in the conditional metagraph of Fig. 5, hist meant that a loan history was available. Thus, loan history can be viewed as a resource. In the case where resources are measured quantitatively e.g., Ž numbers of workstations or levels of expenditures on software , additional analysis would be needed. But. even in this case, metagraphs may provide a platform for the development of workflow resource allocation tools.

The information describing a metagraph—that is, the descriptions of data elements, documents, and tasks—could be organized in a fashion similar to that used in a data dictionary<sup>r</sup>directory in a database-management system 20,23 . A metagraph dic- <sup>w</sup> <sup>x</sup> tionary<sup>r</sup>directory MD Ž . <sup>r</sup>D would contain descriptions of the elements in the generating set, along with the appropriate metadata, such as the source of the information, estimates as to its reliability, etc. Similarly, an MD<sup>r</sup>D would identify the documents that form the invertices and outvertices of the edges Ž . tasks , the elements found in these documents, and the tasks with which they are associated. The MD<sup>r</sup>D would also identify the tasks, their associated documents, and any appropriate metadata, such as the persons responsible for the tasks, any resources needed for the tasks, and so forth.

Metagraphs may be useful in integrating WSS with more conventional types of DSS. The information found in traditional DSS is not documents but rather stored data, decision models, and expert knowledge 25,27 . Metagraphs have been used to<sup>w</sup> <sup>x</sup> model these types of information as well 2 . In the<sup>w</sup> <sup>x</sup> case of stored data, the elements represent data attributes, the edges represent data relations, and the invertices and outvertices represent the key and content attributes of the relations. In the case of decision models, the elements represent model variables, the edges represent the models, and the invertices and outvertices represent the model inputs and outputs. In the case of knowledge-based DSS, the systems of interest are typically rule-based systems in which metagraph elements represent propositions that may be true or false, the edges represent the rules, and the invertices and outvertices represent the antecedents and consequents of the rules. This is summarized and compared with the workflow interpretation of metagraphs in Table 1.

Table 1  
Metagraph interpretations

<table><tr><td>Information type</td><td>Metagraph element</td><td>Metagraph edge</td><td>Edge invertex</td><td>Edge overtext</td></tr><tr><td>Data file</td><td>Data attribute</td><td>Data realtion</td><td>Key attribute</td><td>Content attribute</td></tr><tr><td>Decision model</td><td>Variable</td><td>Algorithm</td><td>Input variable</td><td>Output variable</td></tr><tr><td>Rule</td><td>Proposition</td><td>Rule</td><td>Antecedent</td><td>Consequent</td></tr><tr><td>Workflow</td><td>Dataw element</td><td>Task</td><td>Document</td><td>Document</td></tr></table>

The metagraph literature described in this paper suggests that there are two advantages of using metagraphs in DSS modeling. First, metagraphs can establish connectivity or lack thereof in data, model, or knowledge bases and thus determine whether and how inferences can be drawn from available information. In other words, the existence or nonexistence of a metapath in such a system may be helpful in determining whether and how the system can be used to link known source information to desiredŽ . Ž . target information. Second, metagraphs can be used to integrate the different information types—stored data, decision models, and expert knowledge—found in a DSS. We can now see a third advantage: metagraphs can be used to integrate established DSS information types with the information types found in a WSS. Thus, a metagraph may represent a mixture of DSS<sup>r</sup>WSS components that are collectively used to address important organizational problems.

## 5. Conclusion and future research

Metagraphs provide a powerful tool for analyzing the interactions among components of a DSS, whether they be models, data relations, or rules. We have seen that these components may also include workflow tasks. As a result, the domain of metagraph applications can be extended to encompass a variety of the information processing activities that are found in a modern organization.

Using metagraphs as a foundation for workflow management suggests several areas for further research. These include resource allocation, task scheduling, and the development of software for WSS planning and control. Some of these issues have already been addressed in a preliminary way <sup>w</sup> <sup>x</sup> 5,9 . There appear to be substantial additional opportunities for research in WSS—for example, in the incorporation of intelligence into a workflow system. Although metagraphs have been applied in a preliminary way to analyze knowledge bases, and specifically rule bases 2 , there is substantial room for <sup>w</sup> <sup>x</sup> additional work in this area, both inside and outside of the workflow context. In summary, metagraphs may provide a useful foundation for WSS development and for the integration of WSS and DSS.

## References

<sup>w</sup> <sup>x</sup> 1 A. Basu, R.W. Blanning, The analysis of assumptions in model bases using metagraphs, Management Science 44 7Ž . Ž . 1998 982–995.

<sup>w</sup> <sup>x</sup> 2 A. Basu, R.W. Blanning, A graph-theoretic approach to analyzing knowledge bases containing rules, models, and data, in: Blanning, R.W., Shaw, M.J. Eds. , Annals ofŽ . Operations Research, Special Issue on Artificial Intelligence and Management Science, Vol. 75, December 1997.

<sup>w</sup> <sup>x</sup> 3 A. Basu, R.W. Blanning, A. Shtub, Metagraphs in hierarchical modeling, Management Science 43 5 1997 623–639.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 A. Basu, R.W. Blanning, Metagraph transformations and workflow management, Proceedings of the Thirtieth Annual Hawaii International Conference on Systems Sciences, Vol. IV, January 1997, pp. 359–366.

<sup>w</sup> <sup>x</sup> 5 A. Basu, R.W. Blanning, A Formal Approach to Workflow Analysis, Owen Graduate School of Management, Vanderbilt University, Nashville, 1996.

<sup>w</sup> <sup>x</sup> 6 A. Basu, R.W. Blanning, Metagraphs, Omega 23 1 1995 Ž . Ž . 13–25.

<sup>w</sup> <sup>x</sup> 7 A. Basu, R.W. Blanning, Metagraphs: a tool for managing decision support systems, Management Science 40 12 Ž . Ž .1994 1579–1600.

<sup>w</sup> <sup>x</sup> 8 A. Basu, R.W. Blanning, Model integration using metagraphs, Information Systems Research 5 3 1994 195–218.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 A. Basu, R.W. Blanning, Metagraphs and petri nets in model

management, Proceedings of the Second Annual Workshop on Information Technologies and Systems WITS 92 , De-Ž . cember 1992, pp. 64–73.

<sup>w</sup> <sup>x</sup> 10 C. Berge, Graphs, 2nd edn., North-Holland, Amsterdam, 1985.

<sup>w</sup> <sup>x</sup> 11 C. Berge, Hypergraphs, North-Holland, Amsterdam, 1985.

<sup>w</sup> <sup>x</sup> 12 C. Bubler, S. Jablonski, An approach to integrate workflow modeling and organizational modeling in an enterprise, Proceedings of the Third Workshop on Enabling Technologies: Infrastructure for Collaborative Enterprises, April 1994, pp. 81-95.

<sup>w</sup> <sup>x</sup> 13 F. Burger, G. Quirchmayr, S. Reich, A.M. Tjoa, Using hytime for modeling publishing workflows, SIGOIS Bulletin 16 1 1995 39–45.Ž . Ž .

<sup>w</sup> <sup>x</sup>14 T.H. Davenport, Process Innovation: Reengineering Work Through Information Technology, Harvard Business School Press, Boston, 1993.

<sup>w</sup> <sup>x</sup> 15 D. Georgkopoulos, M. Hornick, A. Sheth, An overview of workflow management: from process modeling to workflow automation infrastructure, Distributed and Parallel Databases 3 1995 119–153.Ž .

<sup>w</sup> <sup>x</sup> 16 S. Khoshafian, M. Bukiewicz, Introduction to Groupware, Workflow and Workgroup Computing, Wiley, New York, 1995.

<sup>w</sup> <sup>x</sup> 17 A. Kumar, J.L. Zhao, A framework for dynamic routing and operational integrity controls in a workflow management system, Proceedings of the 29th Annual Hawaii International Conference on System Sciences, January 1996, pp. 492–501.

<sup>w</sup> <sup>x</sup> 18 L.O. Levine, S.S. Aurand, Evaluating automated work-flow systems for administrative processes, Interfaces 24 5 1994Ž . Ž . 141–151.

<sup>w</sup> <sup>x</sup> 19 R.T. Marschak, Workflow: Applying Automation to Group Processes, in: Coleman, D., Khanna, R. Eds. , Groupware: Ž . Technologies and Applications, Chap. 3, Prentice-Hall, Upper Saddle River, 1995, pp. 71–77.

<sup>w</sup> <sup>x</sup> 20 McFadden, Hoffer, 1988.

<sup>w</sup> <sup>x</sup> 21 C. Mohan, D. Agrawal, G. Alonso, A. El Abbadi, R. Guenther, M. Kamath, Exotica: a project on advanced transaction management and workflow systems, SIGIOS Bulletin 161 Ž . 1995 45–50, Special Issue: Business Process Reengineering.

<sup>w</sup> <sup>x</sup> 22 S. Morschheuser, H. Raufer, C. Wargitsch, Challenges and solutions of document and workflow management in a manufacturing enterprise: a case study, Proceedings of the Twenty-Ninth Annual Hawaii International Conference on System Sciences, Vol. V, Digital Documents, January 1996, pp. 4–12.

<sup>w</sup> <sup>x</sup> 23 R. Narayan, Data Dictionary: Implementation, Use, and Maintenance, Prentice-Hall, Englewood Cliffs, 1988.

<sup>w</sup> <sup>x</sup> 24 B. Silver, Automating the Business Environment, in: L. Fischer Ed. , The Workflow Paradigm, Future Strategies, Ž . Lighthouse Point, 1995, pp. 173–195.

<sup>w</sup> <sup>x</sup> 25 R. Sprague, Jr., E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, 1982.

<sup>w</sup> <sup>x</sup> 26 K.D. Swenson, Workflow Management Standards and Interoperability, in: L. Fischer Ed. , The Workflow Paradigm,Ž . Future Strategies, Lighthouse Point, 1995, pp. 25–36.

<sup>w</sup> <sup>x</sup> 27 E. Turban, Decision Support and Expert Systems: Management Support Systems, 4th edn., Prentice-Hall, Englewood Cliffs, 1995.

Amit Basu is an Associate Professor of Management at the Owen Graduate School of Management, Vanderbilt University. He is a member of the Telecommunications and Electronic Commerce faculty at the school. His research interests are in the areas of database systems, knowledge-based systems, decision support systems, workflow management and electronic commerce. He has published technical papers on these topics in a variety of leading journals, including Management Science, Information Systems Research, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man and Cybernetics, IEEE Computer, Decision Support Systems, Journal of Management Information Systems, Omega and the European Journal of Operational Research. He has also served on the organizing committees and program committees for several leading international conferences. He serves as Area Editor for the INFORMS Journal on Computing, and as Associate Editor for the Telecommunications Systems Journal and the Information Technology and Management Journal. Prior to joining Vanderbilt University in 1990, he was on the faculty of the University of Maryland at College Park. He received his PhD in Computers and Information Systems from the William Simon School of Business Administration at the University of Rochester.

![](/api/attachments/UZ89VUP6/fulltext/images/a544a551890d1c56846f9f4ea07a4141b750a275f3839b8df45f8d0a7e471313.jpg)

Robert W. Blanning is Professor of Management at the Owen Graduate School of Management of Vanderbilt University. He holds a B.S. in Physics from the Pennsylvania State University, an M.S. in Operations Research from the Case Institute of Technology, and a Ph.D. from the Wharton School of the University of Pennsylvania. He was a member of the faculties of the Wharton School and of the Schools of Business at New York University, a nuclear engi-

neer at the Knolls Power Laboratory of the General Electric Company, and a research analyst in the Corporate Operations Research Department of the Mobil Oil Corporation. His research and teaching interests are in decision support systems, information economics, and in the application of artificial intelligence to organizational modeling. He has published in such journals as Management Science, Communications of the ACM, Decision Support Systems, Naval Research Logistics Quarterly, Decision Sciences, Omega, Policy Analysis and Information Systems, International Journal of Policy and Information, Long Range Planning, and Technological Forecasting and Social Change. He has presented papers at the annual meetings of such conferences as the International Conference on Information Systems, the Workshop on Information Technologies & Systems, the Hawaii International Conference of Systems Sciences, and the International Conference on Decision Support Systems. He is an Area Editor of Decision Support Systems, and a member of the Editorial Board of Journal of Management Information Systems. He is editor of the book Foundations of Expert Systems for Management, which was published by Verlag Rheinland in 1990. He is coeditor, with David R. King, of two books: Current Research in Decision Support Technology, which was published by IEEE Computer Society Press in 1992 and Organizational Intelligence: AI in Organizational Design, Modeling, and Control, which was published by the IEEE Computer Society Press in 1996.
