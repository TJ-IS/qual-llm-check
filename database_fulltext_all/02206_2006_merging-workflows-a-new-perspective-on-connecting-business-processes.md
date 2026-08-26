---
otero_id: 2206
otero_key: "SH2WPKU3"
title: "Merging workflows: A new perspective on connecting business processes"
authors: "Shuang Sun; Akhil Kumar; John Yen"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.07.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Merging workflows: A new perspective on connecting business processes

Shuang Sun <sup>a,\*</sup>, Akhil Kumar <sup>b</sup>, John Yen <sup>a</sup>

<sup>a</sup>School of Information Sciences and Technology, Pennsylvania State University, University Park, PA 16802, United States <sup>b</sup>SMEAL College of Business, Pennsylvania State University, University Park, PA 16802, United States

Received 18 May 2004; received in revised form 17 June 2005; accepted 3 July 2005 Available online 1 August 2005

## Abstract

This paper describes the concept of workflow merge and methods for merging business processes. We grouped merges in four categories according to the type of merge: sequential, parallel, conditional, and iterative, and describe the corresponding algorithms for performing these operations. We give results that allow us to determine whether a merge operation is sound. It is shown that to avoid invalid merges, one should choose merge points between which a sub-workflow, called a merge region, is well structured. These findings can provide useful guidance for future workflow merge research. We also raise issues of more complex merge problems, such as merge conflicts, semantic ambiguities and workflow splits. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Workflow management; Workflow merge; Workflow modeling; Business process reengineering; Sequential; Parallel; Conditional; Iterative merge

## 1. Introduction

For agile business operation, modern corporations must make frequent business process changes as well as organizational changes through mergers and acquisitions. In 2001, Hewlett-Packard Company and Compaq Computer Corporation announced a merger agreement to create an 87 billion dollar global technology leader. The merged company offers the most complete set of products and services in the IT industry with expected cost savings of approximately 2.5 billion dollar a year [10]. Many important issues arise in integrating the two giant organizations, one of them being how to integrate their business processes. Since frequent changes in business processes and operations are becoming increasingly common, both through internal reorganizations and through mergers and acquisitions, we have conducted preliminary research on how workflows can be modified dynamically to adapt to such changes. In addition, our research provides support for complex process composition, i.e., creating complex workflow processes from simple ones.

A workflow may be modified at a schema level that defines a workflow process or at an instance level that represents a specific instance of an already defined process [12]. For example, a two-step workflow, <sup>b</sup>place order,<sup>Q</sup> then <sup>b</sup>deliver,<sup>Q</sup> represents a simple business process at the schema level. Within this process there may be orders or instances of a process <sup>b</sup>order<sup>Q</sup> for customer <sup>b</sup>Sue<sup>Q</sup>. In this paper, we define the workflow concept and methods focused at the schema level. This research topic is important and has not been fully addressed by previous research efforts. Process reengineering and evolution have been studied from different perspectives such as: business process integration [5,17]; using generic workflow modeling methods to ensure flexibility [2]; describing methods for workflow evolution [12]; improving workflow interoperability [3,9,11,15]; and enhancing exception handling capabilities [14,19]. Dealing with more than one process makes a workflow merge different from other problems that commonly assume a single process, and makes existing methods inefficient for addressing workflow merging issues. Therefore, this topic does not fit well into the existing research frameworks. For example, the classic process integration methods [5,17] collaboratively bridge, adapt, and exchange information without actually modifying the processes of the business partners. Naturally, when companies merge, both process integration and merging of processes are necessary for streamlining their operations.

In the remainder of the paper, we first introduce a workflow modeling method with Petri nets. Next, in Section 3, we introduce the workflow merge concept and validate our approach. Section 4 introduces notions of sound and unsound merges, and gives two results related to soundness. Then, in Section 5, we discuss merge point detection and other issues such as conflicts, semantic ambiguities, and impact of merges on organizational roles and resources. Finally, Section 6 gives brief concluding remarks.

## 2. Workflow modeling

Many research efforts have investigated methods for modeling workflow processes, which define the steps of business operations. Dumas and Hofstede tried to specify workflows with activity diagrams of the Unified Modeling Language (UML) [6]. They demonstrated that activity diagrams can provide the expressive power that is required by most applications, and showed that an activity diagram is more powerful for express processes than most of the languages found in commercial workflow systems. A recent study by Aalst and Kumar [3] has demonstrated that the Extensible Markup Language (XML) can be used to model inter-organizational workflows. The main contribution of that research is to support process exchange through the internet. Aalst [1] has mapped the workflow concepts into Petri nets, giving a more formal way to represent and verify processes. In this paper, we also use Petri nets to specify workflows and related concepts. Dussart et al compared several workflow modeling methods such as Petri nets, WfMC, UML, ANSI, and EPC [7] on criteria such as formal basis, executability, ease of visualization, etc. Their study showed that Petri nets satisfied most of the criteria, and were therefore desirable. However, the merge concept and algorithms are independent of modeling techniques, and not limited to Petri nets. We choose Petri nets mainly because they offer a formal basis that helps to determine soundness of a merge. In this section, we briefly introduce important Petri net concepts and how to use Petri nets to represent a workflow.

Definition 1 (Petri net). A Petri net is a triple ( P, T, F):

– P is a finite set of places,

– T is a finite set of transitions ( P \ T = /)

$$
- F \subseteq (P \times T) \cup (T \times P) \text {   is   a   set   of   arcs   (flow   relation) }
$$

A place p is called an input place of a transition t if and only if there exists a directed arc from p to t. Place p is called an output place of transition t if and only if there exists a directed arc from t to p. We use <sup>!</sup>t (t<sup>!</sup>) to denote the set of input (output) places for a transition t, while <sup>!</sup>p ( p<sup>!</sup>) is the set of transitions sharing p as an input (output) place. Note that we restrict ourselves to arcs with weight 1. In the context of workflow procedures it does not make much sense to have other weights because places correspond to conditions.

Definition 2 (WF-net [1]). A Petri net PN = ( P,T,F) is a WF-net (WorkFlow net, or workflow for short) if and only if

(i) PN has two special places: i and o. Place i is a source place: <sup>!</sup>i = /; place o is a sink place: o<sup>!</sup>=/.

(ii) If we add a transition $t ^ { * }$ to PN which connects place o with i, then the resulting Petri net is strongly connected.

Thus, WF-nets are a special kind of Petri nets with the property that there is one source place and one sink place. Places in the set P represent nodes that contain tokens; transitions in the set T correspond to tasks or activities. By examining the locations of tokens, it is possible to determine the state of a Petri net, i.e., what tasks have been completed. Places can also represent conditions, as when one of multiple branches emerging from a place has to be chosen in an or-split (to be discussed shortly). Further note that the requirements for a workflow net stated in Definition 2 are minimal requirements. Even if these requirements are satisfied, a workflow process may still cause potential deadlocks. Although a Petri net does not have any notion of these constructs, we can use Petri nets to model commonly used workflow constructs such as AND-splits, AND-joins, OR-splits, and OR-joins. Fig. 1 shows each of these constructs as Petri net representations. In a workflow context, an AND-split with n branches represents parallelism among n activities; an OR-split with n parallel branches represents a choice among n possible activities. An AND-split (OR-split) with n outgoing branches usually has a corresponding AND-join (OR-join) with n incoming branches. For example, when creating a sales order, a condition of whether a customer is a preferred one may lead to different branches for preferred and regular customers. This process may be represented as an OR-split with the customer type as the split condition. Moreover, after creating the order there may be two independent follow-up actions: sending an order confirmation to the customer and sending a delivery note to the warehouse. These parallel actions may be represented with an AND-split.

A structured workflow is a workflow where (a) each OR-split has a matching OR-join, and each AND-split has a matching AND-join; and (b) if multiple splits and joins are properly nested inside each other. A simple algorithm can be used to check if a workflow is structured in this way. Our following definitions of structured WF-net and well-behaved WF-net are based on Kiepuszewski et al.’s work on structured workflow modeling [13].

Definition 3 (Structured WF-net). A structured WFnet (SWF) is a WF-net where:

1. A workflow consisting of a single activity is a SWF.

2. The concatenation of two SWF workflows, X and Y, where the final activity of X has a transition to the initial activity of Y, is a SWF (see Fig. 2a).

3. If X1,. . .,Xn are SWFs, they can be combined in parallel by a pair of and-split and and-join nodes (see Fig. 2b).

4. If X1,. . .,Xn are SWFs, they can be combined in parallel by a pair of or-split and or-join nodes. An or-split is also called a choice or decision node (see Fig. 2c).

5. If X and Y are SWFs, and j(s) are two-way orjoin (or-split) nodes, in an iteration structure, then the workflow with transition X between j and s, and transition Y between s and j, is also a SWF (see Fig. 2d). This is called an iteration structure.

![](/api/attachments/SH2WPKU3/fulltext/images/ff59ddcd7d57917f3aba4eceaa38faba51a3bbac16357e051e03f09260baa8d4.jpg)  
a) OR-split

![](/api/attachments/SH2WPKU3/fulltext/images/a44dceddf9e65ae40b2d96f2176a1ecd8cd48706ce81dd3b18df00a2a2c1eed3.jpg)  
b) OR-join

![](/api/attachments/SH2WPKU3/fulltext/images/31ad9bbe5a30c1de2a6e96dbe83e82a35632b816419f0074769ed24cddcb1ac6.jpg)  
c) AND-split

![](/api/attachments/SH2WPKU3/fulltext/images/89015715d8c001fcba947f8d78b6078b5eebf4a3d659a0bdb670b1e5808de263.jpg)  
d) AND-join  
Fig. 1. Petri net representations of commonly used workflow constructs.

![](/api/attachments/SH2WPKU3/fulltext/images/dc6e71369d35e416eda89a2080e1c654df010ae77ea917e211bc6aca62127426.jpg)  
a) Concatenation b) Parallel

![](/api/attachments/SH2WPKU3/fulltext/images/816d4fabad614a0f4efff3ff854b0093d50b919141f2dc2777a8f71e1d3eb357.jpg)  
c) Choice d) Iteration  
Fig. 2. Combining structured WF-nets (X and Y) to create more complex structured WF-nets.

Definition 4 (Well-behaved WF-net). A workflow model is well-behaved if it can never lead to deadlock nor result in multiple active instances of the same activity. Every structured workflow model is wellbehaved [13].

## 3. Workflow merge concepts

In this section, we introduce workflow merging concepts, a taxonomy, and general merging algorithms.

## 3.1. Workflow merging—scenarios

## 3.1.1. Scenario 1: organizational merge

Fig. 3 shows the first scenario<sup>1</sup> in which a computer manufacturer (company A) merges with its logistics services provider (company B), which is responsible for delivery. Company A takes customer orders and packs computers, then it sends a delivery note to company B. Upon receiving the delivery note, B will ship the computers to customers. In an attempt to reduce costs, say A decided to acquire company B and deliver computers by itself. The merged process has three tasks: order, packing, and delivery.

## 3.1.2. Scenario 2: business process reengineering

In the second scenario (Fig. 4), a sales process is merged with a production process. Suppose company A is a computer manufacturer, and it has two functional departments, sales and production. The sales department takes customers’ orders and ships finished products. The production department schedules factory production according to sales forecasts. In order to dynamically manage their production to meet market demand changes, say company A decides to use a new production mode—make to order (MTO). In the MTO mode, the production department only produces after new sales orders arrive. In other words, the production process will have to be merged into the sales process.

![](/api/attachments/SH2WPKU3/fulltext/images/33aef197354c2169ec36b36cd279993c6669b916531cad9ef2c28c626bdfbea7.jpg)  
Fig. 3. A scenario for merging two organizational processes.

![](/api/attachments/SH2WPKU3/fulltext/images/4aa4aa4a7822837c75c36f2e827fa23ae387a6830f9240730ee5dd9a719af771.jpg)  
Fig. 4. A business process reengineering scenario.

## 3.2. Concepts of workflow merge

We define workflow merge as the process of combining one workflow schema into another and removing redundant steps but keeping all necessary ones. In the first scenario, the workflow of company B is merged into the workflow of company A. After the merge, for example, company A keeps all of the necessary steps such as order, packing, and delivery, while redundant steps such as sending and receiving delivery notes are removed. We call the original workflows that are combined as merging workflows, and the resulting workflow the merged workflow.

Definition 5 (Workflow merge). When a WF-net $\mathrm { P N } ^ { \prime } = ( P ^ { \prime } , T ^ { \prime } , F ^ { \prime } )$ is combined with another WF-net $\scriptstyle \mathrm { P N } = ( P , T , F )$ , we call the process a workflow merge, if and only if:

(i) the result is a new WF-net $\mathrm { P N } ^ { \prime \prime } { = } ( P ^ { \prime \prime } , T ^ { \prime \prime } , F ^ { \prime \prime } )$ (ii) $T ^ { \prime \prime } \subseteq T \cup T ^ { \prime }$

(iii) $P ^ { \prime \prime } \subseteqq P \cup P ^ { \prime } \cup P _ { \mathrm { m } }$ (where $P _ { \mathrm { { m } } }$ are new merge points)

$$
\left(\mathbf {i v}\right) F ^ {\prime \prime} \subseteq F \cup F ^ {\prime} \cup \left(T ^ {\prime \prime} \times P _ {\mathrm{m}}\right) \cup \left(P _ {\mathrm{m}} \times T ^ {\prime \prime}\right)
$$

We call the merge function as $\mathrm { M e r g e } ( \mathrm { P N } , \mathrm { P N } ^ { \prime } ) ^ { 2 } ,$ and we call PN the primary WF-net and $\mathrm { P N } ^ { \prime }$ the secondary WF-net.

According to condition (ii), the merged workflow should not involve any new tasks that are not in the merging workflows; condition (iii) ensures that only result merge points (see Definition 6 below) can include new conditions; condition (iv) states that dependencies in the merging workflows should be compliant with the ones in merged workflows. More importantly, a workflow merge should not violate the soundness properties [1]. Later, in Section 4, we will show how to achieve a sound merge by keeping properties of well-structuredness in a merge function.

Definition 6 (Merge point). When a primary WF-net, $\mathrm { P N } ^ { \prime } { = } ( P ^ { \prime } , T ^ { \prime } , F ^ { \prime } )$ , is merged with a secondary WF-net, $\scriptstyle \mathrm { P N } = ( P , T , F )$ , and the merged workflow is a WF-net, $\mathrm { P N } ^ { \prime \prime } { = } ( P ^ { \prime \prime } , T ^ { \prime \prime } , F ^ { \prime \prime } )$ a place node such as $p \in \mathrm { P N }$ 2 $p ^ { \prime } \in \mathsf { P N } ^ { \prime }$ or $p _ { \mathrm { m } } { \in } \mathrm { P N } ^ { \prime \prime }$ is called a merge point, if and only if:

(i) if $p \in \operatorname { P N } \cap \operatorname { P N } ^ { \prime \prime }$ , at such that $t \in ( \bullet p \cup p \bullet ) \land t \in$ PNV, or

(ii) if $p ^ { \prime } \in \mathrm { P N } ^ { \prime } \cap \mathrm { P N } ^ { \prime \prime }$ , at such that $t \in ( \bullet p ^ { \prime } \cup p ^ { \prime } \bullet )$ $\Lambda t \in \mathrm { P N } , \mathrm { o r }$

(iii) $p _ { \mathrm { m } } \notin \mathsf { P N } \cup \mathsf { P N ^ { \prime } }$

The place nodes where two merging workflows, say wf1 and wf2, are connected are called merge points. Merge points are always in pairs and they are noted as $\left( { p / p ^ { \prime } } \right)$ which means that $p ^ { \prime }$ from wf2 will merge with p from wf1. The result merge points $p _ { \mathrm { m } }$ may be p as in $( \mathrm { i } ) , p ^ { \prime }$ as in (ii), or a new place as in (iii) which is different from $p$ or $p ^ { \prime } . P _ { \mathrm { m } } ,$ in Definition 5, is the set of result merge points. A merging workflow contains at least one merge point. When two merge points (p1 and p2) are specified in a merging workflow, if p1 is prior to p2, p1 is called beginning merge point, and $\mathtt { p } 2$ is called ending merge point, and vice versa.

For example, Fig. 5 depicts a merge function— Merge(PN,PNV), and the merged workflow is PNW. We call tx (in PNW) an auxiliary transition node that helps to connect two places because, in a Petri net, two place nodes (such as p2 and $\mathsf { p } 0 ^ { \prime } )$ ) cannot be connected directly without a transition node in between. Unlike a normal WF-net node, an auxiliary node represents neither conditions nor tasks. By eliminating redundant nodes (p2) and auxiliary node (tx) we can reduce $\mathrm { P N } ^ { \prime \prime }$ into PNj. This is a workflow simplification step. Places $\mathtt { p } 2$ and $\mathsf { p } 0 ^ { \prime }$ are the merge points and the resulting merge point isp0 V. We will explain auxiliary nodes and simplification further in Section 3.3.2.

![](/api/attachments/SH2WPKU3/fulltext/images/1369274d730074714000e7f54ac66b2cf55663002299bdd183a864e25483e5f3.jpg)  
Fig. 5. Workflow merge example (a sequential merge).

## 3.3. Workflow merging taxonomy

Next, we group workflow merges along two dimensions: lossy/lossless and by merge pattern. The first grouping method yields two types of merges: lossy merge or lossless merge. With the second dimension, we sort a merge by its pattern: sequential, conditional, parallel, or iterative merge.

## 3.3.1. Workflow merging taxonomy—lossless or lossy

Definition 7 (Lossless merge). When a WF-net $\mathrm { P N } ^ { \prime } = ( P ^ { \prime } , T ^ { \prime } , F ^ { \prime } )$ is merged with another WF-net $\scriptstyle \mathrm { P N } = ( P , T , F )$ and the result is a new WF-net $\mathrm { P N } ^ { \prime \prime } { = } ( P ^ { \prime \prime } , T ^ { \prime \prime } , F ^ { \prime \prime } )$ , we call the merge lossless if and only if $T \cup T ^ { \prime } \subseteq T ^ { \prime \prime }$ . Thus, in a lossless merge, all tasks in the merging workflows are preserved in the merged workflow.

Definition 8 (Lossy merge). When a WF-net $\mathrm { P N } ^ { \prime } = ( P ^ { \prime } , T ^ { \prime } , F ^ { \prime } )$ is merged with another WF-net PN = ( P,T,F) and the result is a new WF-net $\mathrm { P N } ^ { \prime \prime } { = } ( P ^ { \prime \prime } , T ^ { \prime \prime } , F ^ { \prime \prime } )$ , we call the merge lossy if and only if at such that $t \in ( T \cup T ^ { \prime } ) \land t \notin T ^ { \prime \prime }$ . A lossy merge does not guarantee that all tasks are retained after the merge.

A lossy merge is not necessarily bad because it can often result in improvement of a process by merging two tasks into one, and thus pruning redundant tasks. Determining what tasks in merging workflows are redundant requires more knowledge about the process and cannot be easily automated. On the other hand, if a lost task is not redundant, the lossy merge yields an incomplete process, which is undesirable.

A lossy merge must specify the merge direction because it is important to note that Merge(PN,PNV)p Merge(PNV,PN). The order of arguments of the merge function indicates the merge direction Thus, in Fig. 6, when PNV merges into PN, it is specified as Merge(PN,PN V), while in Fig. 7, where PN merges into PN V, it is specified as Merge(PN V,PN), and the results are different.<sup>3</sup>

## 3.3.2. Workflow merging taxonomy—by merging result pattern

The second dimension of our taxonomy is based on the result patterns. Workflows have basic process patterns, such as sequential, parallel, conditional, and iterative [4]. In basic merge situations, we assume that two merging workflows contain a single pattern in the merged workflow and two pairs of merge points: a pair of beginning merge points and a pair of ending merge points. In more complex situations, a merged workflow may contain multiple merge points. However, a complex merge can be represented by combining simple merge patterns. In the rest of this section, we define the different types of merge functions and give algorithms for performing these merge functions. The merge functions cannot guarantee that a merged workflow has a sound process. We will discuss the issue of soundness in detail in Section 4.

Definition 9 (Sequential merge). When two workflows, PN and PNV, merge at merge points (p1/ $\mathsf { p } 1 ^ { \prime } , \mathsf { p } 2 / \mathsf { p } 2 ^ { \prime } ) , ^ { 4 }$ if $\mathsf { p } 1$ is replaced by $\mathsf { p } 1 ^ { \prime }$ and $\mathsf { p } 2$ by $\mathfrak { p } 2 ^ { \prime }$ V, it is a sequential merge. The tasks or steps of PN between p1 and $\mathsf { p } 2$ are replaced by the steps in PNV between $\mathsf { p } 1 ^ { \prime }$ and ${ \mathfrak { p } } 2 ^ { \prime }$ V. In general, no new place nodes are created in a sequential merge.

In a sequential merge, parts of one workflow merge with another in a sequential manner. There are two types of sequential merges: replacement merge and insertion merge. Fig. 8 shows a replacement— Merge<sup>\_</sup>Seq (PN,PNV,p1,p0V,p2,p1V) where t2 is replaced by t1V. Fig. 9 shows an insertion—Merge<sup>\_</sup>Seq (PN,PNV,p1,p1V,p1,p2V) where, in the primary workflow, place p1 is both the start place and the end place. Recall that in Fig. 3, the <sup>b</sup>Delivery<sup>Q</sup> process of Company B was put after the <sup>b</sup>Packing<sup>Q</sup> process of Company A in the newly merged workflow called <sup>b</sup>Company A New<sup>Q</sup>; so the organizational merge in Fig. 3 is also an example of sequential merge.

![](/api/attachments/SH2WPKU3/fulltext/images/0c2b232df3bc399b3df55f27ae6ae7d4d62b20c9bb4e9465fd74131ea4507862.jpg)  
Fig. 6. Merge(PN,PN V).

As mentioned in Section 3.2, a sequential merge involves two steps: initial merge and simplification. In the first step, the merging workflows are combined through two pairs of auxiliary-node sets at the merging points. In Fig. 8, an auxiliary node, tx, is connected to the merge point, p1, while another auxiliary node txV is connected to p2. As discussed above, the auxiliary transition nodes are required to connect two place nodes in a Petri net. Between the auxiliary node is the merge region of $\mathrm { P N } ^ { \prime }$ V. The use of the auxiliary nodes in the merge guarantees a sequential relation between the merging workflows.

![](/api/attachments/SH2WPKU3/fulltext/images/cd30e1c73a6aef6a67beecad2cafce1b52fdef72e2bc1b7cfefd16d7ee0ff56c.jpg)  
Fig. 7. Merge(PN V,PN).

![](/api/attachments/SH2WPKU3/fulltext/images/48dacb9d1ed6d0503c64f56eb740655fca9ff139b2491d6e9881b248e9a12ba0.jpg)  
Fig. 8. Replacement merge.

![](/api/attachments/SH2WPKU3/fulltext/images/88f5b7a99ab33f70f6acdfa2dc027cea41dc45ace21ba77c9628f35d4984b863.jpg)  
Fig. 9. Insertion merge.

To simplify and make the workflow nets concise, we need to eliminate the redundant nodes and auxiliary transitions. In Fig. 8, the merge begins with p1. Since task t2 is eliminated after the merge, p1 is redundant. In addition, $\mathsf { p } 1 ^ { \prime }$ is also redundant because it is the post-condition of $\mathrm { t } 1 ^ { \prime }$ a deleted transition. Task tx and $\mathbf { t x } ^ { \prime }$ are auxiliary transitions that indicate sequential merges and when fired, they will simply pass tokens to their output nodes. In both Figs. 8 and 9, $\mathrm { P N } ^ { \prime \prime }$ represents the result of the initial merge and $\mathrm { P N } ^ { \prime \prime \prime \prime }$ is the result after simplification. It is easy to see that $\mathrm { P N } ^ { \prime \prime }$ and $\mathrm { P N } ^ { \prime \prime \prime \prime }$ are equivalent. However, because the auxiliary nodes are not essential in the final merge result, we provide an algorithm that obtains the merged workflow without involving any auxiliary nodes. The algorithm for a sequential merge (see Fig. 8) is defined below:

$$
\text { Algorithm   Merge\_Seq } (P N, P N ^ {\prime}, p 1, p 1 ^ {\prime}, p 2, p 2 ^ {\prime})
$$

1. Remove $\mathsf { p } 1$ , the arcs after p1, and the arcs before $\mathrm { p } 1 ^ { \prime }$

2. Connect <sup>!</sup>p1 to $\mathsf { p } 1 ^ { \prime } \mathsf { \Pi } ( \mathrm { i } . \mathsf { e } .$ , connect the input transitions of $\mathsf { p } 1$ to $\mathsf { p } 1 ^ { \prime }$ with new arcs).

3. Remove $\cdot { \mathsf { p } } 2 ,$ , arcs before $\mathtt { p } 2$ , and arcs after ${ \mathfrak { p } } 2 ^ { \prime }$

4. Connect $\bullet _ { \mathrm { p } 2 ^ { \prime } }$ V to p2 (i.e., connect all input transitions of place $\mathsf { p } 2 ^ { \prime }$ V to the place p2 with new arcs).

5. The process that contains $\mathsf { p } 1 ^ { \prime }$ and $\mathsf { p } 2$ is the merged workflow.

Definition 10 (Parallel merge). When two workflows PN and $\mathrm { P N } ^ { \prime }$ merge at merge points $( { \mathsf { p } } 1 / { \mathsf { p } } 1 ^ { \prime } , { \mathsf { p } } 2 / { \mathsf { p } } 2 ^ { \prime } ) ,$ 5 if, after the merge, p1 and $\mathsf { p } 1 ^ { \prime }$ construct an AND-split and $\mathtt { p } 2$ and $\mathfrak { p } 2 ^ { \prime }$ V construct an AND-join, it is a parallel merge, i.e., PN and PNV have been connected at points $\mathsf { p } 1 / \mathsf { p } 1 ^ { \prime }$ and $\mathsf { p } 2 / \mathsf { p } 2 ^ { \prime }$ V, in parallel. In general, no new place nodes are created in a parallel merge.

The algorithm for a parallel merge (see Fig. 10) is defined below:

Fig. 10. Parallel merge.  
![](/api/attachments/SH2WPKU3/fulltext/images/1a6331c189589489c27c1dd50d752db21bed0d5a4685181e6c978f60598bc13d.jpg)

Algorithm Merge Parð Þ PN; PNV; p1; p1V; p2; p2V

1. Remove the arcs before p1Vand connect <sup>!</sup>p1 to $\mathsf { p } 1 ^ { \prime }$

2. Remove the arcs after ${ \mathfrak { p } } 2 ^ { \prime }$ V and connect $\mathfrak { p } 2 ^ { \prime }$ V to $\mathrm { p } 2 \bullet$

Parallel merges are used when the causal order between the merging workflows is not relevant. Fig. 10 illustrates a parallel merge where the order of tasks t2 and $t 2 ^ { \prime }$ is not relevant.

Definition 11 (Conditional merge). When two workflows PN and $\mathrm { P N } ^ { \prime }$ merge at merge points $\left( \mathsf { p } 1 / \mathsf { p } 1 ^ { \prime } , \mathsf { p } 2 / \right.$ $\mathbf { p } 2 ^ { \prime } ) , ^ { 6 }$ if p1 and $\mathrm { p } 1 ^ { \prime }$ construct an OR-split and $\mathtt { p } 2$ and $\mathfrak { p } 2 ^ { \prime }$ construct an OR-join, it is a conditional merge, $\mathrm { i . e . }$ , PN and PNV have been connected at points p1/ $\mathsf { p } 1 ^ { \prime }$ and $\mathsf { p } 2 / \mathsf { p } 2 ^ { \prime }$ with additional conditions. A new place called a condition place will be created in a conditional merge.

The algorithm for a conditional merge (see Fig. 11) is defined below:

$$
\text { Algorithm   MergeCond } (P N, P N ^ {\prime}, p 1, p 1 ^ {\prime}, p 2, p 2 ^ {\prime}, C)
$$

1. Remove the arcs before $\mathsf { p } 1 ^ { \prime }$ , and connect p1V<sup>!</sup> to p1.

2. Remove the arcs after $\mathfrak { p } 2 ^ { \prime }$ V, and connect $\bullet _ { \mathrm { p } 2 ^ { \prime } }$ V to $\mathfrak { p } 2 .$

![](/api/attachments/SH2WPKU3/fulltext/images/c9a1fa6332f9c5ab46defa008ab597d3523de58945f9c9f79d13f85a12262efc.jpg)  
Fig. 11. Conditional merge.

3. Modify the conditions in p1 according to new choice conditions C and $\mathsf { p } 1 ^ { \prime }$

Fig. 11 is an example of a conditional merge, Merge $\mathrm { . C o n d ( P N , P N ^ { \prime } , p 1 , p 1 ^ { \prime } , p 2 , p 2 ^ { \prime } , } C )$ In the merged workflow, p1 and $\mathrm { p } 1 ^ { \prime }$ are merged into a new place called $\mathsf { p } 1 ^ { \prime \prime }$ that contains conditions for choosing between tasks t2 and $t 2 ^ { \prime }$ . Because the transitions after place ${ \mathfrak { p } } 2 ^ { \prime }$ are not included in the result, the conditions in ${ \mathfrak { p } } 2 ^ { \prime }$ are useless in the merged workflow. Therefore, the merge point of the secondary merging workflow is removed. In the real world, conditional merges can be used to model the combination of two processes that requires satisfying certain criteria, such as $C : : = \mathrm { i f }$ (order<sup>\_</sup>value <sup>N</sup> discount<sup>\_</sup>qualify)—to check whether a customer’s order is big enough to qualify for a discount. If it qualifies then one branch out of the condition place will be taken; otherwise, the other one is taken.

Definition 12 (Iterative merge). When two workflows PN and PNV merge at merge points $( \mathsf { p } 1 / \mathsf { p } 2 ^ { \prime } , \mathsf { p } 2 / \mathsf { p } 1 ^ { \prime } ) ,$ 7 if p1 and ${ \mathfrak { p } } 2 ^ { \prime }$ construct an OR-join and $\mathtt { p } 2$ and $\mathsf { p } 1 ^ { \prime }$ construct an OR-split, it is an iterative merge, i.e., PN and $\mathrm { P N } ^ { \prime }$ have been connected at point $\mathsf { p } 1 / \mathsf { p } 2 ^ { \prime }$ and $\mathfrak { p } 2 /$ $\mathsf { p } 1 ^ { \prime }$ with additional conditions. A new place will be created in an iterative merge.

The algorithm for an iterative merge (see Fig. 12) is defined below:

Algorithm Merge Iterative

$$
\times (P N, P N ^ {\prime}, \mathrm{p1,p2} ^ {\prime}, \mathrm{p2,p1} ^ {\prime}, C)
$$

1. Remove the arcs before p1V, and connect p2 $\tan { \mathfrak { p } } 1 ^ { \prime } \cdot$

2. Remove the arcs after $\mathfrak { p } 2 ^ { \prime }$ , and connect <sup>!</sup> ${ \mathfrak { p } } 2 ^ { \prime }$ to p1.

3. Modify the conditions in p2 according to the new choice conditions C and original conditions in ${ \tt p } 2 .$

Fig. 12 is an example of iterative merge, Merge<sup>\_</sup> Iterative $( \mathrm { P N } , \mathrm { P N } ^ { \prime } , \mathrm { p } 1 , \mathrm { p } 2 ^ { \prime } , \mathrm { p } 2 , \mathrm { p } 1 ^ { \prime } , C )$ . In the merged workflow, $\mathfrak { p } 2 ^ { \prime \prime }$ is a new place that contains conditions for choosing between tasks t3 and t4. To illustrate the need for an iterative merge, suppose PN is a purchase request process with the following steps: t1 is filling the form (by an employee); t2 is checking the form (by a secretary); t3 is approving the purchase request (by a manager). Sometimes, however, after task t2, the form may need to be modified (if it is incorrect or some information is missing). Therefore, another step, say task $^ { \mathrm { t 4 , } }$ modifying the form, (by the employee)

![](/api/attachments/SH2WPKU3/fulltext/images/b2b7d4cd37b0347c06a453b2e885e86933188511f41d0b4522c620711967bf2d.jpg)  
Fig. 12. Iterative merge.

may be added as shown in Fig. 12. In general, t4 could also be a sub-workflow itself. This shows how a workflow may be modified dynamically, while still maintaining its correctness.

Definition 13 (Complex merge). When two workflows PN and PNV merge at more than two pairs of merge points, it is called a complex merge.

A complex merge may involve multiple merge patterns. For example, Fig. 13 shows that in a merge process, company A (primary workflow) has merged company B’s <sup>b</sup>check availability process<sup>Q</sup> sequentially, and it has also merged company B’s <sup>b</sup>check stock<sup>Q</sup> in parallel.

A complex merge could be expressed formally with the following merge function:

Merge par Merge ð Seq ðPNA; PNB; <sup>d</sup>new sales<sup>T</sup>;

<sup>d</sup>new sales<sup>T</sup>; <sup>d</sup>credit OK<sup>T</sup>; <sup>d</sup>within due date<sup>T</sup>Þ;

PNB; <sup>d</sup>order created<sup>T</sup>; <sup>d</sup>order created<sup>T</sup>;

<sup>d</sup>payment received<sup>T</sup>; <sup>d</sup>stock enough<sup>T</sup>Þ

Hence, the primitive merge operations discussed above can be combined to create more complex merges.

![](/api/attachments/SH2WPKU3/fulltext/images/0c746c7fc7e22829e9accf9636d6adec216427790cbb1f742f9e96087d5b0c31.jpg)  
Fig. 13. A complex merge scenario.

## 4. Workflow merge analysis

Above we discussed various types of functions or operations for merging two workflows. However, without properly chosen merge points and merge functions, two merging workflows cannot yield a sound result, even a syntactically sound one. Fig. 14, Merge<sup>\_</sup>Seq(PN,PNV,p4,p6V,p7,p1V), gives an example of an unsound merged workflow because node p5, after the merge, becomes dangling, and the whole workflow, $\mathrm { P N } ^ { \prime \prime }$ , is ill structured. This problem leads us to investigate the situations where a sound merge is not possible. In this section, we introduce the notions of sound and unsound merges, and analyze a workflow merge at the structural level of a process.

If a workflow merge yields a correct result, we call it a sound merge. On the other hand, in some situations, two workflows cannot be merged correctly, and we call such merges unsound. Fig. 14 shows an unsound merge. Naturally, it is desirable to find rules that can ensure a sound merge. Therefore, we developed some rules to distinguish between sound and unsound merges.

By analyzing the structure of processes, we obtained two theorems that can provide necessary and sufficient conditions for sound merges. A structural analysis treats the sub-process between merge points as a whole entity. We call the entity a merge region, and define it first.

![](/api/attachments/SH2WPKU3/fulltext/images/9908dff94d86b0e87e1f2bcae9b14b7a0ecc4112e3b5cc955983103c741124fe.jpg)  
Fig. 14. An unsound merged workflow.

Definition 14 (Merge region). When two workflows PN and $\mathrm { P N } ^ { \prime }$ are merged at merge points $\left( \mathsf { p } 1 / \mathsf { p } 1 ^ { \prime } , \mathsf { p } 2 / \right.$ $\mathsf { p } 2 ^ { \prime } )$ , by the operation merge $( \mathrm { P N } , \mathrm { P N } ^ { \prime } , \mathrm { p } 1 , \mathrm { p } 1 ^ { \prime } , \mathrm { p } 2 , \mathrm { p } 2 ^ { \prime } ) , ^ { 8 }$ the sub-process between p1 and $\mathsf { p } 2$ (or between $\mathsf { p } 1 ^ { \prime }$ and $\mathsf { p } 2 ^ { \prime } )$ is called a merge region. The merge region for a merging workflow, say PN (or PNV), can be obtained through the following algorithm:

1. Remove <sup>!</sup>p1 and $\mathrm { p } 2 \bullet$ (or $\bullet \mathfrak { p } \mathbb { 1 } ^ { \prime }$ and $\mathsf { p } 2 ^ { \prime } \bullet )$

2. The sub-process that contains merge points p1 and $\mathtt { p } 2$ (or $\mathsf { p } 1 ^ { \prime }$ and $\mathsf { p } 2 ^ { \prime } )$ is the merge region for the merging workflow PN (or PNV).

For example, the corresponding merge regions for PN and $\mathrm { P N } ^ { \prime }$ , shown in Fig. 15, are MR and MRV, respectively. It is easy to see that both these regions are structured because they conform to the definition of a structured WF-net (see Definition 3).

Theorem 1. If the merge regions of two merging workflows are structured WF-nets, the merged workflow constructed with sequential, parallel, conditional, and iterative merge functions is structured too.

Proof. The proof is by construction and relies on Definition 3 where different forms of structured workflows are discussed. All the merging functions described above are based on combining structured workflows to create new workflows that are also structured. Thus, in performing a merge, we are essentially taking a structured region from a workflow, and replacing it with another structured region. The proof follows from a case by case analysis.

Case (a) Concatenate, insert, replace. In this case, two workflows are merged by concatenation or insertion, or a structured workflow is replaced by another structured workflow. Since each workflow is structured, the resulting workflow is also structured (by Definition 3(2)).

Case (b) Parallel merge. When two structured workflows are combined in parallel using ANDsplit and $\mathbf { A N D - j o i n }$ , the resulting workflow is also structured (by Definition 3(3)).

![](/api/attachments/SH2WPKU3/fulltext/images/8e155ccba1adb3f88a634b2a12e4566b4fcd9b78e41c998b8cc19a3fdc0cd28e.jpg)  
Fig. 15. Merge regions (MR and MR V for PN and PN V).

Case (c) Conditional merge. When two structured workflows are combined in parallel using OR-split and OR-join, the resulting workflow is also structured (by Definition 3(4)).

Case (d) Iterative merge. This is a variant of case (c), and here the OR-JOIN occurs first and it is followed by a matching OR-SPLIT. Since the two component workflows that are merged are structured, it follows that the resulting workflow is also structured (by Definition 3(5)).

Thus, in all cases the workflow that results from the four types of merges is structured if the merge regions themselves are structured. 5

As discussed earlier, more complex merges can be created by combining these primitive merges as building blocks.

Lemma 1. If the merge regions of two merging workflows are structured, then the merged workflow constructed with sequential, parallel, conditional, and iterative merge functions is well-behaved.

Proof. This follows from Theorem 1 and Definition 4, which states that every structured workflow is wellbehaved. Thus, we can conclude that Theorem 2 is true. 5

By choosing a proper merge point, we can change an unsound merge to a sound one. In Fig. 16, Merge<sup>\_</sup> $\mathrm { S e q ( P N , P N ^ { \prime } , p 3 , p 1 ^ { \prime } , p 5 , p 2 ^ { \prime } ) }$ results in PNW, which is not well-structured. If we change a merge point of PN from $p 5$ to p4—thus, Merge<sup>\_</sup> $\mathrm { S e q ( P N , P N ^ { \prime } , p 3 , p 1 ^ { \prime } , p 4 , p 2 ^ { \prime } ) }$ , the new result $\mathrm { P N } ^ { \prime \prime \prime \prime }$ is well-structured and sound. Thus, unless two merging workflows have an inherent conflict in the sequencing of their activities, in most of the cases one can achieve a sound merge by choosing merging points properly. In the next section, we will discuss the issue of suitable merge point detection.

## 5. Discussion

We have defined workflow merge concepts, categories of merges, and studied how routing and process structures affect a workflow merge. Here, we will briefly discuss merge point detection methods and other issues such as conflicts, semantic ambiguities, and impact of merges on organizational roles and resources.

Automatically finding merge points and applying merge functions can greatly simplify a workflow merge task. The key step is to find out valid merge points. This process is called merge point detection. Our hypothesis is that merge points could be detected by applying the syntactic rules discussed in Section 4, and by reasoning about process dependencies. As a simple example, in Fig. 17, delivery notes are generated in the step <sup>b</sup>print delivery note<sup>Q</sup> and are fed into the step <sup>b</sup>get delivery notes<sup>Q</sup>; so <sup>b</sup>get delivery note<sup>Q</sup> is dependent on <sup>b</sup>print delivery notes,<sup>Q</sup> and must follow it. However, a general algorithm for merging real workflows is a much more complex problem. Developing algorithms for automatic merge point detection is a topic for future research.

![](/api/attachments/SH2WPKU3/fulltext/images/536a4997f7a3d2bebc34eaa932a036e2e8478f950bfe8e7d537cd541a7cbffc0.jpg)  
Fig. 16. Example of choosing a proper merge point.

![](/api/attachments/SH2WPKU3/fulltext/images/36a41cc81376357bc8f243ad3c121d01c4be733a7c876d571ceb8c5619faea76.jpg)  
Fig. 17. An example of merge point detection.

Workflow merges are normally more complicated than the ones described above. Ambiguities and conflicts can cause errors. Multiple merge points and constraints from organizational changes increase the complexity of a merge. In this section, we will raise these issues, but not attempt to solve them. Moreover, the issues listed here are not an exhaustive list; we expect that other issues will appear as more research is conducted.

First, often merging workflows have conflicting dependencies between the same pair of tasks. For example, Fig. 18 shows two such processes in two companies. Notice how the order of two processes, Packing and Delivery, in the two companies is reversed. Therefore, this conflict must be resolved manually before performing a merge.

Second, different companies may name workflow processes in their own way, so semantic meanings of the steps in the merging workflows should be clarified to avoid ambiguities. For example, while a general term <sup>b</sup>packing<sup>Q</sup> can represent packing for a particular part on a production line, it can also represent packing finished products into a container before shipment. If the difference in meaning is not noticed before the merge, the result will be wrong. We can either manually check the semantics or let merging workflows follow certain standards, such as RosettaNet [17,18]. Moreover, two organizations may also use different workflow systems, which have very different ways of modeling business processes. In such cases, it becomes even harder to merge the two workflows unless one is converted into the modeling schema of the other, or both are converted into a common schema.

![](/api/attachments/SH2WPKU3/fulltext/images/1d2d5add8692556ccf1745e8ad54dfd50a0f8809f186b7ac96e8666014b474d1.jpg)  
Fig. 18. A simple example of merge conflicts.

Next, the analytical method adopted in this research demands validation and evaluation in a real world application setting or in controlled simulation experiments. In such a setting, the interaction of factors such as throughput, reliability, flexibility, and quality can be studied. For example, throughput of a merged workflow relies on its flexibility, quality, and reliability. Those problems are often hard to study with analytical models, but they can be tackled better by an application or through simulation. In addition to validating the research, such application and experiments may also provide us with valuable insights into real problems that are encountered when workflows merge.

Last, but not least, workflow splitting is another interesting topic of study. A workflow split is the reverse of a workflow merge. Business units often split, or outsource parts of their processes to other companies. In such situations, it is important to develop algorithms to split a process into two or more separate sub-processes. A process split requires finding split points (as opposed to merge points) and ensuring that the splitting is correct. We expect that the research on workflow splits can benefit from some of our present results for workflow merge.

## 6. Conclusion

This paper discussed fundamental concepts, models, and methods of various types of workflow merge operations. We formally defined a workflow merge operation and also proposed merge methods. Merges were grouped into four categories: sequential, parallel, conditional, and iterative. More importantly, we showed the conditions under which a merge will yield a sound result. This framework is promising for developing applications to serve the business world, and its potential benefits lie in: (1) performing simulations that can help decision makers visualize merges for business processes; (2) creating virtual enterprises that make flexible business operations possible; and (3) planning merges that allow software agents to share process knowledge. It also offers a systematic approach for building complex workflows from simple ones by incorporating changes and new sub-processes into them in a correct way. Thus, this methodology also plays a useful role in workflow evolution.

Decision makers can gain valuable experience through simulating their proposed workflow merge operation. The simulation results can provide crucial information to help them modify their plans and optimize the new processes. Such an effort will eventually help to cut costs, increase throughput, and create more value.

The research on workflow merge also promises more flexible business models, such as virtual enterprises, to address dynamic business environments. A virtual enterprise is a business model that dynamically organizes small companies into its business processes. A virtual enterprise can provide more services in a flexible manner and lead to more efficiencies as compared to a single enterprise providing multiple services. Moreover, such coalitions can disband when they are no longer effective [16]. At present, coalition formation for virtual organizations is limited. We anticipate that automation of coalition formation by using workflow merge technologies will save both time and labor. In complex settings, workflow merge techniques may also be more effective at finding better coalitions than other technologies or manual methods.

In a multi-agent environment, if a software agent’s plan (essentially a process) is incomplete, other agents may be able to help with the other parts of the solution. Then the problem is how to assimilate such piecemeal solutions into the existing processes, which is equivalent to merging several plans [8]. As workflows and plans are both based on process specifications and can use similar representations, we believe that workflow merge technologies can be applied in plan merging too.

In summary, research on workflow merge offers a new way to connect business processes. This paper has highlighted the importance of the workflow merge problem and also raised many questions, such as resolution of merge conflicts, semantic considerations, workflow splits, etc., for future studies.

## References

[1] W.M.P.v.d. Aalst, The application of Petri nets to workflow management, Journal of Circuits, Systems and Computers 8 (1) (1998) 21 – 66.

[2] W.M.P.v.d. Aalst, Generic workflow models: how to handle dynamic change and capture management information? Conference on Cooperative Information Systems, 1999.

[3] W.M.P.v.d. Aalst, A. Kumar, XML based schema definition for support of inter-organizational workflow, Information Systems Research 14 (1) (2003) 23– 47.

[4] W.M.P.v.d. Aalst, A.H.M.T. Hofstede, B. Kiepuszewski, A.P. Barros, Workflow patterns, Distributed and Parallel Databases 14 (1) (2003) 5 – 51.

[5] A. Dan, D.M. Dias, R. Kearney, T.C. Lau, T.N. Nguyen, F.N. Parr, M.W. Sachs, H.H. Shaikh, Business-to-business integration with tpaML and a business-to-business protocol framework, IBM Systems Journal 40 (1) (2001) 68– 90.

[6] M. Dumas, A.H.M.t. Hofstede, UML activity diagrams as a workflow specification language, International Conference on the Unified Modeling Language (UML), Springer Verlag, Toronto, Canada, 2001.

[7] A. Dussart, B.A. Aubert, M. Patry, An evaluation of interorganizational workflow modeling formalisms, Journal of Database Management 15 (2) (2004) 74 – 104.

[8] D.E. Foulser, M. Li, Q. Yang, Theory and algorithms for plan merging, Artificial Intelligence 57 (2–3) (1992) 143 – 181.

[9] B. Gronemann, G. Joeris, S. Scheil, M. Steinfort, H. Wache, Supporting cross-organizational engineering processes by distributed collaborative workflow management—the MOKASSIN approach, 2nd Symposium on Concurrent Mulitdisciplinary Engineering (CME’99)/3rd Int. Conf. on Global Engineering Networking (GEN’99), Institute for Aerospace Technology, Bremen, Germany, 1999.

[10] Hewlett-Packard and Compaq, Hewlett-Packard and Compaq Agree to Merge, Creating \$87 Billion Global Technology Leader (2001).

[11] Y. Hoffner, H. Ludwig, C. Gu¨ lcu¨ , P. Grefen, An architecture for cross-organizational business processes, in: Second International Workshop on Advance Issues of E-Commerce and Web-Based Information Systems (WECWIS 2000), IEEE Computer Society Press, Milpitas, CA, 2000.

[12] G. Joeris, O. Herzog, Managing evolving workflow specifications, in: The 3rd Int. IFCIS Conf. on Cooperative Information Systems (CoopIS’98), IEEE Computer Society Press, New York, 1998.

[13] B. Kiepuszewski, A.H.M.t. Hofstede, C. Bussler, On structured workflow modelling, Int. Conference on Advanced Information Systems Engineering (CAiSE), Springer Verlag, Stockholm, 2000.

[14] M. Klein, C. Dellarocas, A knowledge-based approach to handling exceptions in workflow systems, Computer Supported Cooperative Work 9 (2000) 399– 412.

[15] A. Lazcano, G. Alonso, H. Schuldt, C. Schuler, The WISE approach to electronic commerce, International Journal of Computer Systems Science and Engineering 15 (5) (2000) 345– 357.

[16] M. Luck, P. McBurney, C. Preist, Agent Technology: Enabling Next Generation Computing—A Roadmap for Agent-Based Computing, AgentLink, 2003.

[17] RosettaNet, eBusiness Standards for the Global Supply Chain, http://www.rosettanet.org, 2003.

[18] M. Sayal, F. Casati, U. Dayal, M.-C. Shan, Integrating workflow management systems with business-to-business interaction standards, 18th International Conference on Data Engineering, ICDE, IEEE Computer Society, San Jose, CA, 2002.

[19] D.M. Strong, S.M. Miller, Exceptions and exception handling in computerized information processes, ACM Transactions on Information Systems (TOIS) 13 (2) (1995) 206– 233.

Shuang Sun is a PhD candidate at the School of Information Sciences and Technology (IST), the Pennsylvania State University. Before he joined IST in 2001, he had been an application consultant at NOKIA and Deloitte and Touche. His research interests include supply chain management, workflow management, cognitive modeling, and intelligent agent technologies. His thesis is on collaborative information sharing and decision making.

Akhil Kumar is a professor of Information Systems at the Smeal College of Business at Pennsylvania State University. He has a PhD from Berkeley, and has published more than 60 papers in the areas of database systems and structures, data replication, machine learning and workflow systems in leading academic journals, and international conferences and workshops. He serves on the editorial boards for Information Systems Research, INFORMS Journal on Computing, and Information Technology and Management. His current research interests are in design, analysis and verification of workflow processes, design and implementation of e-services, and web-based technologies.

John Yen is a University Professor of Information Sciences and Technology and Professor-in-Charge at the School of Information Sciences and Technology, the Pennsylvania State University. He is the founding director of the Intelligent Agent Laboratory at Penn State. He holds a PhD in computer science from University of California, Berkeley. He is a Fellow of IEEE. His current research focus is developing team-based agent technologies for supporting human decision making teams as well as transferring these technologies into applications related to homeland security, information fusion, and web service composition.
