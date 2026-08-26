---
otero_id: 24445
otero_key: "PFD5FK3F"
title: "Information System Verification and Validation during Requirement Analysis Using Petri Nets"
authors: "S. Sakthivel; Mohan R. Tanniru"
year: "1988"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1988.11517831"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information System Verification and Validation during Requirement Analysis Using Petri Nets

## S. Sakthivel & Mohan R. Tanniru

To cite this article: S. Sakthivel & Mohan R. Tanniru (1988) Information System Verification and Validation during Requirement Analysis Using Petri Nets, Journal of Management Information Systems, 5:3, 33-52, DOI: 10.1080/07421222.1988.11517831

To link to this article: http://dx.doi.org/10.1080/07421222.1988.11517831

![](/api/attachments/PFD5FK3F/fulltext/images/34294bd17aa2141613ee33a5b9695f38de152ca92717350a4552655886c6c675.jpg)

Published online: 23 Dec 2015.

![](/api/attachments/PFD5FK3F/fulltext/images/f1e2622ffded47198144d1cfdab26d0499269d6ca7078cd1817a5c3d02de6112.jpg)

Submit your article to this journal ↗

![](/api/attachments/PFD5FK3F/fulltext/images/3264c373db269f86c3e7123697b17be48458e777b5408d3769177ed47ee812a7.jpg)

View related articles ↗

# Information System Verification and Validation during Requirement Analysis Using Petri Nets

S. SAKTHIVEL and MOHAN R. TANNIRU

S. SAKTHIVEL is an Assistant Professor of MIS at Bowling Green State University. He is working towards a Ph.D. from Syracuse University. His research interests are in systems analysis and database management.

MOHAN R. TANNIRU is an Associate Professor of MIS at Syracuse University. He received his Ph.D. in 1978 from Northwestern University. He has published in a number of journals and presented papers at various meetings. His research interests are in systems analysis, decision support systems, and expert systems.

ABSTRACT: Requirement analysis is the first step in the development of information systems, and its objective is to ensure that any proposed system meets the projected requirements of the user. As a part of this requirement analysis, an analyst is asked to verify that any proposed system is representationally accurate in deriving the needed information and to validate such a system against the time and resource requirements specified by the user. This article performs both the representational verification and dynamic performance validation by expressing the information system, current or proposed, in the form of a Petri Net and using its structural characteristics to perform a set of static and dynamic checks.

KEY WORDS AND PHRASES: Verification of information systems, validation of information systems, system requirement analysis, Petri Nets, system development.

## Introduction

ORGANIZATIONS RELY ON ACCURATE and timely information for making decisions and managing their operations. The availability of correct information and, in turn, the systems that provide such information, are critical to supporting the basic purposes and goals of an organization. The development of such correct information systems is dependent on how well a user's needs are specified (requirement specification) and an information system designed to meet these needs (system design and implementation). In Figure 1, this requirement specification is shown as an end result of the requirement analysis phase of the traditional system-development life cycle.

<table><tr><td>Requirement definition</td><td>Current or proposed system representation</td><td>Generation of feasible alternatives</td><td>Requirement specification</td></tr></table>

Figure 1. A Framework for Requirement Analysis

The objective of this paper is to extend the well-developed modeling capabilities of Petri Nets to represent the information system of an organization and verify its accuracy. In addition, the modeling capabilities of the Petri Nets are used to simulate the information system performance and validate it against the user's system performance needs. The next section will discuss some earlier research with regard to requirement verification and validation. The third section will discuss the basic features of Petri Nets as they are used to model information systems. The fourth section will illustrate how the Petri Net representation can be used for system verification, and the fifth section will use the modeling capability of Petri Nets to simulate an information system performance. The last section will show some extensions to this approach and research directions.

## System Verification and Validation

IN VERIFYING THE ACCURACY of a system representation, one needs to test for the “derivability of the output” requested by the user using “logic” and “precedence” information of the processes in the system. Successive iterations of this step on each output eventually should lead to the definition of the “boundary conditions” (where the system meets its external environment). When a complex system is represented in a hierarchical manner, the successive iteration of the output derivability step should also ensure consistency among levels in the hierarchy. In addition, one needs to ensure that all the process and data flow/file definitions are consistent, i.e., there exists no redundant or overlapping definition of either the process or data.

To validate the performance of the proposed system against certain user-provided operational needs, one must test the timeliness of output either in absolute terms (e.g., output needed Monday morning of each week), or in relative terms (e.g., ship goods within a day of order receipt). In addition, the system should be tested for its ability to resolve operational conflicts and backlogs. Given that meeting these operational requirements is contingent upon having certain resources (economic/organizational), the system needs to be tested at this stage for its feasibility with respect to any resource limitations. Table 1 summarizes these verification checks (static in nature) and validation tests (dynamic in nature).

<table><tr><td>Table 1 Verification checks and validation tests</td></tr><tr><td>I. Verification checks1. Output derivability,2. Precedence relationships,3. Boundary condition,4. Hierarchical consistency, and5. Input and output consistency.</td></tr><tr><td>II. Validation tests1. Absolute and relative timeliness,2. System performance in managing conflicts and backlogs, and3. System’s ability to meet resource constraints.</td></tr></table>

The methods used to verify a proposed information system include many manual techniques, such as structured walk-throughs and do's and don't's associated with documentation conventions. However, most of these methods are time-consuming when used to analyze large, complex systems [3].

A number of automated methods are discussed in the literature to assist in this verification process. These include Software Requirements Engineering Methodology/Requirements Engineering and Validation Systems (SREM/REVS) [2], Systems Architects Apprentice (SARA) [39], GYPSY [9], HDM [15], AFFIRM [1], SYSDOC/SYSTEMATOR by Aschim et al. [21], Systems Descriptor and Logical Analyzer by Knuth et al. [21], D2S2 by MacDonald and Palmer [21], DADES by Olive [21], USE by Wasserman [21], NIAM by Verheijn et al. [21], Remora by Rolland and Richard [21], PSL/PSA [37, 38], and SODA [19]. Refer to Schneider [35] for additional references. Many of these check for inconsistent definition of inputs and outputs, and output derivability. However, many of these tend to be oriented to program verification rather than system verification.

PSL/PSA and SREM use automated cross-referencing for verification, or provide data flow, control flow, and data structure diagrams for manual cross-referencing. These aids are good for checking consistency and closure properties such as missing functions. PSL/PSA is shown to be weak, however, in hierarchical representation and dynamic analysis $[10]$ . SREM is shown to represent dynamic environments well, but is considered a weak verification tool $[29, 34]$ . In addition, it is shown to be weak in describing distributed and parallel processing situations where time sequences are important $[36]$ . CAPO $[13]$ is a software product developed to extract process interdependencies using incidence, precedence, and reachability matrices. This information is primarily used, however, to assist the clustering of processes during system design.

Structured Analysis and Design Technique (SADT) [27, 28] and DFD [7] are commonly used in business today. Structured analysis techniques use data flow diagrams (DFD) to represent a system. These methods are excellent for user/analyst communication, but are weak in facilitating performance evaluation over time. In addition, these methodologies are primarily manual and have no analytical basis for system verification. Some tools such as PSL/PSA and SODA use analytical procedures such as

Langefor's precedence matrix [14], while some others use Marimont's procedure [16]. Other theoretical concepts based on information algebra [5] and Young and Kent language [40] are developed for design and automatic programming. However, many of these are not directly applied in the requirement analysis phase.

Methodologies such as the Structured Requirements Definition of Orr [22], Jackson System Depvelopment (which has a time dimension) of Jackson [12], and Information Engineering of Martin [17] suffer from inadequacies such as lack of a theoretical basis for verification and difficulty in simulation for performance evaluation.

The Petri Net, developed by C. A. Petri [25], is an abstract tool for modeling information flow. It has become a powerful tool for modeling and analysis of computer hardware and software systems. Petri Nets are useful for modeling systems that exhibit events which are asynchronous, concurrent or sequential, constrained by precedence relationships, and have varying execution times and frequencies. These are based on sound mathematical principles, can be computerized for efficiency, and can be simulated to evaluate system performance. For example, Petri Nets have been used in developing a design and programming technique for communication systems [10]. In an application involving electronic authorization of credit cards, Petri Nets were used to design the hardware component configuration of the communication system along with protocols and program interface. Another application of Petri Nets is in the computerization of various asynchronous office procedures [41]. A number of other applications of Petri Nets can be found in the literature [4, 8, 11, 18, 20, 23, 24, 26, 30]. For additional discussion of Petri Nets, see [18, 23]. The next section will illustrate the Petri Net representation of information systems.

## Petri Net Representation of Information Systems

A PETRI NET HAS TWO TYPES OF NODES called places $(P)$ and transitions $(T)$ . Places can be the input $(I)$ or the output $(O)$ of transitions. The input and output functions relate transitions and places. The input function defines, for each transition Ti, the set of input places $I(Ti)$ , needed to enable (or trigger or fire) the transition. Similarly, the set $O(Ti)$ defines the set of output places associated with Ti. The state of the system is defined by the tokens associated with each place. Tokens are indicated by dots inside the places and the execution of a Petri Net is controlled by the position and movement of these tokens. The placement of these tokens in a Petri Net at any given instant of time is defined by vector M. The structure of a Petri Net is, thus, represented by these three elements—T, $I(T)$ , and $O(T)$ —and M represents the state of the system.

The Petri Nets defined above can be represented as a Petri Net graph. The places are represented as circles, transitions as vertical bars, and the functional relation between places and transitions as directed arcs. The arcs can be directed only between an element of one set (places or transitions) and an element of the other set (transitions or places). The static properties of a system are represented by such a Petri Net graph and the dynamic properties of a system result from its execution.

![](/api/attachments/PFD5FK3F/fulltext/images/a49e7719afa824cae070c3a62f086b2f8ad23a3b6e26013848c7883bd97c5a95.jpg)  
Figure 2. Petri Net and DFD representations of order preparation

![](/api/attachments/PFD5FK3F/fulltext/images/f80c6fca3911ef673253d7d1d00f3d9782d278b19bc63f9d44be4c8321abc30a.jpg)  
Figure 3. Execution of a Petri Net

An example of a Petri Net representation is shown in Figure 2. Here “order” and “catalog” represent input places (or conditions) and “sales order” represents an output place. The process “prepare sales order” represents a transition. This Petri Net is executed by firing or enabling the transition T1. The transition T1 is fired when the two input places have at least one token in them, i.e., both the order and catalog information are available. The result of such a firing is a token in the output place, as shown in Figure 3.

Several variations to this representation are possible and the rest of this section discusses these Petri Net features as they are used to model an “order validation” system. The use of structured tools (data flow diagram, structured English, and process sequence diagram) to represent this system is shown in Figure 4.

![](/api/attachments/PFD5FK3F/fulltext/images/657e537f1a63768e124571dc96bcc958ad30388f2a7f6dcd5dabf2c01e45f9f5.jpg)

![](/api/attachments/PFD5FK3F/fulltext/images/37c5ea0a5fca223b2c2d85862e0ed632c0690ec8d73c6ecee073089d216dcb9a.jpg)  
Figure 4. Structured representation of Order Processing System

1. Token Conservation: Since the firing of a transition removes a token from its input, certain places having no input (for example, permanent files) can be shown to have an infinite number of tokens. This situation is represented by a “c” in the place. On the other hand, we can have these places maintain a single token all the time by making them part of both the input and output sets of the appropriate transition. Figure 5 and the reachability tree (Figure 7) use the latter approach, while the matrix discussion uses the former approach. All internal and external files are represented as conserving nodes (shown as shaded places in Figures 5 through 9) in order to illustrate their passive nature, i.e., non-involvement in the triggering of an event.

![](/api/attachments/PFD5FK3F/fulltext/images/c23d41fe7646d4a3c2d2d20d88a7c3cfd12510acd4807243ac3b2562806f082c.jpg)  
Figure 5. Petri Net representation of Order Processing System

2. Multiple-token input: There can be many arcs from a place to a transition. If there are n arcs (or single arc with an “n” written above it) entering a transition from a single place, then that input place must have at least n tokens to enable the transition.

3. Time-based triggering: A transition can be fired at certain periodic intervals with the use of a “time” place, which gets a token at a predefined time period. This is an example of a typical batch processing application and is illustrated in Figure 5 by making T5 (update catalog) a batch process.

4. Multiple-token transfer: A transition, when fired, can move all the tokens from the input place to the output place(s). For example, in Figure 5, if the number of changes accumulates to 20 when the time place gets its token and enables the transition T5, then all 20 of these “changes” can be moved from the input place “product changes” to the output place “catalog” in one firing.

5. Conflict in transition firing: If a single place is an input to two transitions, then only one of these transitions can be fired at any given point in time. This type of structure allows for the representation of operational conflicts (two events that cannot occur at the same time). In Figure 5, the “catalog” place is input to transitions T1 and T5 (update catalog). If T5 is to be triggered immediately upon the receipt of a product change (with no time delay), then only one of these two transitions can be fired at any given point in time.

6. Alternate or mutually exclusive transitions: Conditional logic can be explicitly expressed in a Petri Net rather than buried in the structured English associated with many structured methodologies (see Figure 4). For example, if acceptance of a sales order is based on the availability of credit, then two possible output places (accepted order and rejected order) can result from this evaluation. This is illustrated in Figure 5 by having these two output places generated by the firing of appropriate transitions T2 and T3.

7. Hierarchical representation: The tokens in places “credit available” and “credit not available” are derived from the sales order value and credit limit. This can be shown in a lower-level Petri Net as in Figure 6. This type of hierarchical structure in Petri Nets allows for a top-down, modular representation of an information system consistently. Note that the places “sales order” and “catalog” are both input links to the lower-level Petri Net and the places “credit available” and “credit not available” become the output links to the top-level Petri Net. These places will be referred to as “link nodes.” Also note that the transitions Tx, Ty, and Tz are “interpretative” transitions (firing is based on an interpretation of the inputs rather than existence of a token).

8. Precedence in transition firing: Precedence relationships in a Petri Net are explicit as they include both the triggering mechanism (when each process is acted upon) and informational dependency in their representation. The parallelism of credit validation and sales log update is shown explicitly in Figure 5. Both P3 and P3' represent the same sales order in order to maintain the parallel nature of transitions T4, and (T2 and T3). At the same time, the sequential nature of sales-order preparation and order validation is also shown explicitly by having each produce distinctly different places P3 (sales order), P6 (accepted order), and rejected order (P7).

9. State reachability: When a Petri Net is executed, the marking associated with that Petri Net is altered, i.e., the state of the system is changed. The new marking enables the Petri Net to fire again, resulting in another set of markings. If marking M0 is the starting state, and M1 is the marking upon the first firing, and M2 is the result of a second firing, then M2 is said to be reachable from M0. In general, a set of all markings reachable from an initial set of markings is called the reachability set. The reachability set associated with the example in Figure 5 is shown in Figure 7 in a tree structure.

For the case described here, let us assume that an order has been received. A token must be present in the place “order” (P1). The initial state of the system can now be represented by the marking (1 1 0 0 0 0 0 0 1 0), where the first entry shows the marking in place $P1$ (= 0), second entry shows the marking in place $P2$ (= 1, a conserving node), third entry shows the marking in place $P3$ (= 0), and so on. The presence of a token in $P1$ and $P2$ will fire the transition $T1$ . This firing will remove a token from $P1$ and deposit a token in $P3$ and $P3'$ . Note that $P2$ is a conserving node

![](/api/attachments/PFD5FK3F/fulltext/images/0a5e1dc709d4d0fb5cafe0c2e98d05b3d591a84eb184e7e652ed8eff35d3e5cb.jpg)  
Figure 6. Hierarchical decomposition of a Petri Net

![](/api/attachments/PFD5FK3F/fulltext/images/5fcc2fb34540716e4d11cfc8efe7d997a66362e7d0c8e2f0536554ddb04ea126.jpg)  
\* It is assumed that T4 would have been fired by the time T2 or T3 gets enabled. This is based on the assumption that each firing, including those in the lower level net, takes one clock cycle.

Figure 7. Reachability tree associated with Petri Net of Figure 5

conserving node), third entry shows the marking in place $P3 (= 0)$ , and so on. The presence of a token in $P1$ and $P2$ will fire the transition $T1$ . This firing will remove a token from $P1$ and deposit a token in $P3$ and $P3'$ . Note that $P2$ is a conserving node and, thus, will retain its token. This state is represented by the marking (0 1 1 1 0 0 0 0 1 0). This marking allows $T4$ (update the sales log) to fire with the resultant marking (0 1 1 0 0 0 0 0 0 1 0). Since $P3$ is a common input to $T2$ and $T3$ , representing a conflict situation, only one of these can be fired. Which one of these two will be fired depends on the presence of a token in either $P4$ or $P5$ . This determination is made within the lower-level net (also shown in Figure 7) using interpretative information. The lower-level net, thus, sends a marking for either $P4$ or $P5$ , and this will enable either $T2$ or $T3$ to fire. The markings that result from such a firing are shown in Figure 7.

In summary, a Petri Net describes the structure of a system, the markings of a Petri Net describe the state of that system, and the evolution of markings describes the tion tool, while the Petri Nets are used in the analysis and modeling of information systems. Guidelines to derive the Petri Net representation from structured documentation (as shown in Figure 4) are currently under development [32]. The next section will illustrate how the static representation of a Petri Net can be used to verify the information system characteristics.

Table 2 Matrix representation of place/transition relationships

<table><tr><td></td><td>P1</td><td>P2</td><td>P3</td><td> $P3'$ </td><td>P4</td><td>P5</td><td>P6</td><td>P7</td><td>P8</td><td>P9</td></tr><tr><td>T1</td><td>-1</td><td>c</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>T2</td><td></td><td></td><td>-1</td><td></td><td>-1</td><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td>T3</td><td></td><td></td><td>-1</td><td></td><td></td><td>-1</td><td></td><td>1</td><td></td><td></td></tr><tr><td>T4</td><td></td><td></td><td></td><td>-1</td><td></td><td></td><td></td><td></td><td>c</td><td></td></tr><tr><td>T5</td><td></td><td>c</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-1</td></tr><tr><td></td><td></td><td>P2</td><td>P3</td><td></td><td>P4</td><td>P5</td><td></td><td>P12</td><td>P13</td><td></td></tr><tr><td></td><td>Tx</td><td>c</td><td>-1</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td></tr><tr><td></td><td>Ty</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>-1</td><td>c</td><td></td></tr><tr><td></td><td>Tz</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>-1</td><td>c</td><td></td></tr></table>

Legend: P1: order; P2: catalog; P3: sales order; P4: credit available; P5: credit not available; P6: accepted order; P7: rejected order; P8: sales log; P9: product changes; P12: order value; P13: credit limit; P3': sales order.

## Petri Net Representation for Information System Verification

INFORMATION SYSTEMS, AS DEMONSTRATED in the previous section, can be represented as a Petri Net, where places correspond to the availability of data and transitions correspond to the processes that operate on these data. This section will use such a Petri Net representation to perform the “static” checks described in Table 1. These are: input and output consistency, boundary condition, output derivability, hierarchical consistency, and precedence relationships.

The interdependency of places and transitions can be illustrated in the form of a matrix (see Table 2). The matrix D has rows to represent the transitions and columns to represent the places. The $\mathbf{D}(i,j)$ entry is +1 if place j is an output of transition i, and -1 if place j is an input to transition i. Since the places whose tokens need be conserved are presented as input and output to a transition, its entry in the matrix will be a “0”. In the matrix these will be represented, however, by an entry “c”.

## Input and Output Consistency:

Here we are concerned with proper definition of the input conditions needed to enable a transition and output conditions that result from such a transition. Inconsistent definition of output places (same-place output by two different transitions) is often a result of either improper naming of these output places or incorrect definition of the associated transitions. For example, in Figure 5, if “sales order” is defined as an output of both “prepare sales order” (T1) and “accept order” (T2) transitions, then the role of each transition is left ambiguous, except for one special case discussed in the next paragraph. However, if the output place associated with the transition “accept order” is named as “accepted order,” then this ambiguity is eliminated. Alternatively, the “sales order” may be an input to multiple transitions such as “process accepted orders,” “process rejected orders,” and “update sales log” as long as they use the same “sales order” state or value.

![](/api/attachments/PFD5FK3F/fulltext/images/a65b035375edd9ceac6c125f1fa1af159709f7f913b3a7cb453fa055c3546fc4.jpg)  
Figure 8. Alternate generation of a single place (sales order)

As every process in an information system must have at least one input and one output, no transition in the Petri Net representation can have only a “-1” or a “+1” entry. In order to represent mutually exclusive processes, a single place is input to multiple transitions (for example, P3 is input to T2 and T3). Therefore, in the matrix, two or more “-1” entires will be found in the same column to represent such mutual exclusion. Note also that the rows associated with these -1 entries have no common +1 entry, in general, as such a situation would imply the generation of a single output by multiple transitions. However, Figure 8 provides an exception.

## Boundary Conditions:

All columns that have only one “-1” entry and no “+1” entry (negative elementary vector) represent either a boundary condition, i.e., input from an external source, or a link node from another net. In this example, “order” and “product changes” are external inputs to the system, while “credit available” and “credit not available” are the link nodes. Note that the catalog and sales order are the link nodes in the lower-level net. Similarly, all columns that have only one “+1” entry and no “-1” entry (elementary vector) represent either a boundary condition, i.e., output to an external source, or a link node. In this example, “rejected order” and “approved order” are boundaries to the external system, and the “credit available” and credit not available” are the link nodes in the lower-level net. Also, the columns with a “c” represent files.

## Output Derivability:

This is primarily concerned with the ability of the system to generate the needed outputs from the defined input conditions. Even though the highest level Petri Net corresponds to information flows in their aggregate form, it is necessary to ensure that the conditional logic associated with each of these output flows is clearly identified, i.e., what input conditions generate each of these outputs, what conditions, in turn, are needed to generate these input conditions, etc., until all the input conditions are shown to be derived, external, conserved, or extracted from a lower/higher-level Petri Net. The matrix can assist in determining the paths by systematically going from the column with only a “+1” entry to eventually a set of all columns that have only a “-1” entry. The reachability tree of Figure 7 also provides these paths and is preferred for systems that are relatively complex.

## Hierarchical Consistency:

All the places that are identified as links to lower/higher-level Petri Nets (called “link nodes”) should have appropriate entries in these nets. A place (column) that has only a “-1” entry means that it is an external input or derived from another net. In general, each link node should have a corresponding Petri Net to generate its value. This implies that a place having only a “-1” entry in the higher-level net and being a link node must have a corresponding “+1” entry in the lower-level net. While collapsing of the two nets (higher- and lower-level) can be used to ensure consistency, certain mathematical properites (S invariance, liveness, etc.) can be used to ensure the same. These are discussed in detail in Sakthivel [32].

## Precedence Information:

Given that the representation requires the identification of which input conditions are needed to generate an output place, the sequential nature of the processes is explicitly represented in a Petri Net. The path derived from the matrix or reachability tree in testing for the output derivability will also ensure that all precedence information is explicitly incorporated in the static representation of the information system. This precedence information can be helpful in the performance analysis of the system under varying processing times, triggering frequencies, and external input arrival distributions. This will be discussed in the next section.

## Petri Net Representation for Performance Validation

IN THIS SECTION THE PETRI NET REPRESENTATION of the current “order validation” system will be used to evaluate the performance of several alternatives in meeting both the content and context requirements of a user. Let us assume that the user requirements are stated as follows:

— perform an analysis of rejected sales orders to evaluate the current credit policy, and

— generate information on the type of customer (industrial vs. consumer) and the region (northeast, midwest, etc.) being serviced most by the organization.

In addition,

— provide the customer profile and credit evaluation reports once a month, and
— ensure that the order validation will not take more than an hour upon its arrival.

The current system has to be altered to facilitate the customer and credit analysis, and these content requirements are incorporated in the Petri Net representation as shown in Figure 9. Note the addition of two transitions—T6 and T7—that operate on the existing data flows: rejected orders (represented as $P7'$ ) and accepted orders (represented as $P6'$ ). It is assumed that the data needed to generate these two reports are available in the sales order. If not, new data have to be input from an external source (new place), or the existing sales-order flow altered. The exact data elements needed to support these processes will be determined during the logical design phase.

The proposed system must meet the above requirements and handle a load of 20 orders per hour. Also, assume that product price changes are to be made at a rate of 15 per day. Table 3 shows the information processing times under both the current (i.e., manual) and automated system alternatives.

Table 4 provides three alternative scenarios for evaluating the proposed system performance against the context requirements of the user. Alternative 1 is the current manual system that is set up to process orders as they come in. Alternative 2 represents an on-line, real-time system that is similar to alternative 1, but it is fully automated. The third alternative is also a fully automated system except that both the sales log and credit validation are done in batch mode (once a day and once every hour respectively). Note here that “real time” for a process implies that it is done immediately after its preceding process(es).

Assume that orders arrive uniformly at a rate of 20 per hour and on average about 10 percent of these are rejected due to insufficient credit. A simulation of the proposed system is run for a 160-hour period (one month) using GPSS and the results are tabulated in Table 5.

All three proposed alternatives will meet the order validation time requirement (validation of an order to be completed within one hour of its arrival). However, the labor resource needed to meet this demand in the manual system is about 9 full-time personnel and some part-time assistance, while a single data-entry person and 135 hours of processing assistance are needed under the automation alternatives. Alternative 2 (on-line and real-time system), however, needs a significant amount of on-line storage to store catalog, sales log, sales order, and credit files, while only the sales order and catalog files have to be on-line under alternative 3 (on-line data entry and batch process).

![](/api/attachments/PFD5FK3F/fulltext/images/5e379b17a185db9e7fb1217d076b4faa3a194304323df3705d69de15c418c004.jpg)  
Figure 9. Petri Net for revised Order Processing System

Table 3

<table><tr><td></td><td>Manual alternative</td><td>Under automation</td></tr><tr><td>Prepare sales order (T1)</td><td>10 minutes</td><td>2 minutes</td></tr><tr><td>Update sales log (T4)</td><td>3 minutes</td><td>5 seconds</td></tr><tr><td>Evaluate customer credit and validate order (T2, T3)</td><td>10 minutes</td><td>30 seconds</td></tr><tr><td>Perform credit/customer analysis (T6, T7)</td><td>8 hours</td><td>10 minutes</td></tr><tr><td>Update catalog file (T5)</td><td>2 minutes/catalog</td><td>5 seconds</td></tr></table>

Processing assumptions: Times for manual and computerized alternatives are assumed for the purposes of illustration.

Table 4

<table><tr><td></td><td>Manual alternative (1)</td><td>Automated alternative (2)</td><td>Automated alternative (3)</td></tr><tr><td>Prepare sales order (T1)</td><td rowspan="2">as it comes immediately</td><td rowspan="2">on-line real-time</td><td rowspan="2">on-line once/day</td></tr><tr><td>Update sales log (T4)</td></tr><tr><td>Evaluate customer credit and validate order (T2, T3)</td><td>immediately</td><td>real-time</td><td>once/hour</td></tr><tr><td>Perform credit/customer analysis (T6, T7)</td><td rowspan="2">once/month once/day</td><td rowspan="2">once/month once/day</td><td rowspan="2">once/month once/day</td></tr><tr><td>Update catalog file (T5)</td></tr></table>

If manual, batch process such as “order filling” and “billing” succeed the “order validation” system described here, the processing speed associated with alternative 2 may not be of much value and alternative 3, thus, may meet the user needs more effectively. However, if the response time associated with these processes is critical, then alternative 2 may be chosen. The cost of both alternatives 2 and 3 has to be compared against the resource expenses associated with alternative 1 before any alternative is chosen for design considerations. The system attributes (such as labor cost, on-line storage, hardware and software costs) can be expressed as a utility or weighted function and the alternative with the greatest utility or the highest weight may be selected.

By varying the processing assumptions (on-line, real-time, or batch) and the order-arrival frequency and distribution, an analyst can simulate the performance of the system and study its ability in meeting the “context” requirements of the user. One can also impose additional constraints, such as delays in obtaining credit information to evaluate credit (if external sources are involved in providing credit information), or availability of labor resource (if the labor resource is limited by external factors), to assess the operational feasibility of certain alternatives as well as, possibly, the requirements themselves.

Resource needs—file storage:

Table 5 Performance evaluation—average response time

<table><tr><td></td><td>Manual(1)</td><td>Automated(2)</td><td>Automated(3)</td></tr><tr><td>Accepted order</td><td>25 minutes</td><td>2.5 minutes</td><td>37 minutes</td></tr><tr><td>Rejected order</td><td>25 minutes</td><td>2.5 minutes</td><td>37 minutes</td></tr><tr><td>Update saleslog</td><td>43 minutes</td><td>2.0 minutes</td><td>4.1 hours</td></tr><tr><td>Update catalog</td><td>4.2 hours</td><td>3.8 hours</td><td>3.8 hours</td></tr></table>

Resource needs—Labor resource needs:

<table><tr><td>Load:3200 orders / month</td><td>Manual(1)</td><td>Automated(2 and 3)</td></tr><tr><td>Prepare sales order (T1)</td><td>532 hours (4 man-months)</td><td>106 hours</td></tr><tr><td>Update sales log (T4)</td><td>160 hours (1 man-month)</td><td>4 hours</td></tr><tr><td>Evaluate credit and validate order (T2 and T3)</td><td>532 hours (4 man-months)</td><td>27 hours</td></tr><tr><td>Update catalog (T5)</td><td>40 hours (1 man-week)</td><td>.5 hours</td></tr><tr><td>Perform credit/customer analysis</td><td>8 hours (1 man-day)</td><td>.17 hours</td></tr></table>

<table><tr><td></td><td>Automated (2)</td><td>Automated (3)</td></tr><tr><td>Orders(to prepare sales order)</td><td>1 order(on-line)</td><td>1 order(on-line)</td></tr><tr><td>Sales orders(for credit validation)</td><td>1 sales order(on-line)</td><td>27 sales orders(on-line)</td></tr><tr><td>Sales orders(for sales log update)</td><td>1 sales order(on-line)</td><td>160 sales orders(on-line)</td></tr><tr><td>Product changes(to update catalog)</td><td>15 changes(off-line)</td><td>15 changes(off-line)</td></tr><tr><td>Validated orders for customer(for customer analysis)</td><td>2890 sales orders(off-line)</td><td>2890 sales orders(off-line)</td></tr><tr><td>Invalid orders(for credit analysis)</td><td>310 sales orders(off-line)</td><td>310 sales orders(off-line)</td></tr><tr><td></td><td>Catalog, sales log,sales order, andcredit files haveto be on-line.</td><td>Only the catalog andsales order fileshave to be on-line.</td></tr></table>

## Conclusions and Extensions

REQUIREMENT ANALYSIS IN SYSTEMS DEVELOPMENT plays a critical role in allowing the analyst and user to develop an accurate requirement specification. This requirement specification (both the content of the information to be presented and the context within which this presentation is to occur) is used for an eventual system design. This paper illustrates how a single Petri Net representation can be used both to verify the representational accuracy of the current or proposed system, and to validate its operational feasibility in meeting the timing requirements of the user. In addition, this representation can provide useful information for the evaluation of the economic feasibility of each alternative (labor, processing, and file needs as seen in the last section).

The structural properties of the Petri Nets are amenable for automation, hence facilitating a computer-assisted verification process $[32]$ . In addition to the static checks discussed in this paper, more detailed data flow analysis, at the data element level, is needed to move from the requirement analysis phase to the logical design phase. The use of PROLOG is being investigated to provide such a detailed data flow analysis $[33]$ .

Given that Petri Nets can be derived from information captured in the analysis phase using structured tools (such as data flow diagrams, structured English, and process-sequence diagrams), these tools can still be used for effective user communication, with its corresponding Petri Net assisting in verification and validation. The use of PROLOG in facilitating such a transformation for verification is currently under study $[31]$ .

The information derived during simulation can be used effectively in the physical design. Information about the operational mode of each process (batch, on-line, real-time), frequency (number of times a file is accessed and updated), and order (keyed vs. sequential) of file access can be used in the physical file design (content as well as organization). For instance, the file access frequencies for catalog, sales log, and credit information are:

catalog 3,500
on product no. key (for sales order preparation) 3,200
on vendor product no. key (for product change up-
date) 300
sales log 3,200
credit information 3,200

This frequency of access information along with the mode of access can be used to partition a file (if multiple processes are accessing the file under different operational modes for different information), organize a file (indexed for quick access vs. sequential for batch access), and, if indexed, on what key (based on the most frequently used, immediately needed access strategy).

## REFERENCES

1. AFFIRM System Documentation: AFFIRM Reference Manual. Marina Del Rey, CA: Information Sciences Institute, February 1981.

2. Bell, T. E.; Bixler, D. C.; and Dyer, M. E. An extendable approach to computer-aided software requirements engineering. IEEE Transactions on Software Engineering, SE-3, 1 (January 1977), 49–59.

3. Boehm, B. W. Validating and verifying software requirements and design specifications. IEEE Software, 1, 1 (January 1984), 75–88.

4. Brauer, W. Net Theory and Applications. New York: Springer-Verlag, 1980.

5. CODASYL Development Committee. An information algebra phase I report. Communications of the ACM, 5, 4 (April 1962), 190–204.

6. Davis, G. B., and Vick, C. R. The Software Development System. IEEE Transactions on Software Engineering, SE-3, 1 (January 1977), 69–84.

7. DeMarco, T. Structured Analysis and Systems Specification. New York: Yourdon Press, 1978.

8. Girault, C., and Reisig, W. Application and Theory of Petri Nets. New York: Springer Verlag, 1982.

9. Good, D. I. Constructing verifiably reliable and secure communication processing system. Tech. Report, ICSCACMP-6. Univ. of Texas at Austin, January 1977.

10. Hildebrand, T. Design and processing of interfaces for monetic applications using Petri Nets. In G. Rozenberg (ed.), Advances in Petri Nets. New York: Springer-Verlag, 1984, 197–214.

11. IEEE International Workshop on Timed Petri Nets, Torino, Italy, 1985. IEEE Catalog Number 85CH2 187–3.

12. Jackson, M. A. Systems Development. London: Prentice-Hall International, 1983.

13. Karimi, J. An automated software design methodology using CAPO. Journal of Management Information Systems, 3, 3 (Winter 1986–87), 71–100.

14. Langefors, B. Information system design computations using generalized matrix algebra. BIT, 5 (1965), 96–121.

15. Levitt, K. L.; Robinson L.; and Silverberg, B. A. The HDM Handbook, Vol. 1–3. Menlo Park, CA: Computer Science Lab., SRI International, June 1979.

16. Marimont, R. B. A new method of checking the consistency of precedence matrices. Journal of the ACM, 6, 2 (April 1959).

17. Martin, J., and Finkelstein, C. Information Engineering. Carnforth, Lancashire, England: Savant Research Studies, 1981.

18. Murata, T. Petri Nets and their application—An introduction. In Shi-Kuo Chang (ed.), Management and Office Information Systems. New York: Plenum, 1984.

19. Nunamaker, J. F. A methodology for the design and optimization of information processing systems. AFIPS Conference Proceedings. 38 (May 1971, 283–293.

20. Oh Gil-Rock. Graphic modelling by Petri Nets for production planning. In Advances in Production Management Systems. New York: IFIP, North Holland, 1984.

21. Olle, T. W.; Sol, H. G.; and Verrijn Stuart, A. A. Information System Design and Methodologies—A Comparative Review, Proceedings of IFIP WG 8.1 Conference. New York: North Holland, 1982.

22. Orr, K. T. Structured Requirements Definition. Topeka, KS: Ken Orr and Associates, 1981.

23. Peterson, J. L. Petri Nets. Computing Surveys, ACM, 9, 3 (September 1977). 223-252.

24. Peterson, J. L. Petri Net Theory and Modelling of Systems. Englewood Cliffs, NJ: Prentice-Hall, 1981.

25. Yetri, C. A. Communication with Automation, University of Berlin, 1962. English translation by C. F. Greene, Jr. Communication with Automata. Supplement 1 to Tech. Report RADC-TR-65-377, Vol I. Rome, NY: Rome Air Development Center, Griffiss Air Base, 1965.

26. Reisig, W. Petri Nets—An Introduction. New York: Springer-Verlag, 1982.

27. Ross, D. T. Structured Analysis (SA): A language for communicating ideas. IEEE Transactions on Software Engineering, SE-3, 1 (January 1977), 16–33.

28. Ross, D. T., and Schoman, Jr., K. E. Structured analysis for requirements definition. IEEE Transactions on Software Engineering, SE-3, 1 (January 1977), 6–15.

29. Scheffer P. A.; Stone, A. H.; and Rzepka, W. E. A case study of SREM. Computer, 18, 4 (April 1985), 47–54.

30. Rozenberg, G. Advances in Petri Nets. New York: Springer, 1984.

31. Sakthivel, S., and Tanniru, M. R. Knowledge based support for system verification during requirement analysis. Proceedings of the 1987 ACM SIGBDP-SIGCPR Conference (March), 163–181.

32. Sakthivel, S. Verification and validation during requirement analysis using Petri Nets.

33. Sakthivel, S., and Agarwal, R. Verifying the correctness of information systems using PROLOG interpreted Petri Nets. Proceedings of the 1987 Decision Science Institute Conference. Boston, November 1987.

34. Salwin, A. E. A test case comparison of URL/URA and RSL/REVS. Tech. report FS-

77-161. Laurel, MD: Fleet Systems Department, Johns Hopkins University, Applied Physics Laboratory, July 1977.

35. Schneider, H. J. Formal Models and Practical Tools for Information Systems Design—Proceedings of IFIP TC.8 Conference. New York: North Holland, 1979, 307–320.

36. Stainer, H. M. An evaluation of PSL/PSA and RSL/REVS: Two computer-assisted software requirements/ specification/ description tools. Tech. Report FS-76-205. Laurel, MD: Fleet Systems Department, Johns Hopkins University, Applied Physics Laboratory, October 1976.

37. Teichroew, D. Problem Statement Analysis: Requirements for the Problem Statement Analyzer, [PSA]-ISDOS. Ann Arbor: Dept. of Ind. Eng., Univ. of Michigan, 1977.

38. Teichroew, D., and Hershey, E. A. PSL/PSA—A computer-aided technique for structured documentation and analysis of information systems. IEEE Transactions on Software Engineering, SE-3, 1 (January 1977), 41–48.

39. Winchester, J. W., and Estrin, G. Requirements definition and its interface to SARA design methodology for computer based systems. National Computer Conference (1982), 369–379.

40. Young, J. W., and Kent, H. Abstract formulation of data processing problems. Journal of IE, 9, 6 (November-December 1958), 471–479.

41. Zisman, M. D. Representation, specification and automation of office procedures. Ph.D. dissertation, Wharton School, Univ. of Pennsylvania, Philadelphia, 1977.
