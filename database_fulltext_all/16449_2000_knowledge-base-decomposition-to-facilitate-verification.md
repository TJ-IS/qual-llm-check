---
otero_id: 16449
otero_key: "6Q8DYXRN"
title: "Knowledge Base Decomposition to Facilitate Verification"
authors: "Sumit Sarkar; Mysore Ramaswamy"
year: "2000"
journal: "Information Systems Research"
doi: "10.1287/isre.11.3.260.12207"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [222.90.67.226] On: 28 April 2022, At: 05:11 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/6Q8DYXRN/fulltext/images/36efa978b3e8dc96bd7c4596fe2a8842e9129ee3f177046a64a40df3791620eb.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Knowledge Base Decomposition to Facilitate Verification

Sumit Sarkar, Mysore Ramaswamy,

Sumit Sarkar, Mysore Ramaswamy, (2000) Knowledge Base Decomposition to Facilitate Verification. Information Systems Research 11(3):260-283. https://doi.org/10.1287/isre.11.3.260.12207

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2000 INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individua professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Knowledge Base Decomposition to Facilitate Verification

Sumit Sarkar • Mysore Ramaswamy

PO Box 830688, MS JO44, School of Management, University of Texas at Dallas, Richardson, Texas 75083 Department of Management and Marketing, Southern University, Baton Rouge, Louisiana 70813 sumit@utdallas.edu • ramaswam@subr.edu

e examine the verification of large knowledge-based systems. When knowledge bases are large, the verification process poses several problems that are usually not significant for small systems. We focus on decompositions that allow verification of such systems to be performed in a modular fashion. We identify a graphical framework, that we call an ordered polytree, for decomposing systems in a manner that enables modular verification. We also determine the nature of information that needs to be available for performing local checks to ensure accurate detection of anomalies. We illustrate the modular verification process using examples, and provide a formal proof of its accuracy. Next, we discuss a meta-verification procedure that enables us to check if decompositions under consideration do indeed satisfy the requirements for an ordered polytree structure. Finally, we show how the modular verification algorithm leads to considerable improvements in the computational effort required for verification as compared to the traditional approach.

(Directed Hypergraphs; Knowledge Base Partitioning; Knowledge Base Verification; Polytree Decomposition; Rule-Based Systems)

## 1. Introduction

Knowledge-based systems have become prevalent in practice in recent years. For successful deployment of such systems, it is important that they be error-free. Therefore, the reliability of such systems is of paramount importance to users and, subsequently, designers of the systems. The processes of assuring the reliability of knowledge-based systems are called verification and validation (Plant and Preece 1996). Verification involves checking a knowledge base to see whether it is logically correct and complete. Validation requires checking a knowledge base to determine that it provides recommendations in a manner consistent with the user’s requirements. Several verification and validation techniques have been developed in recent years that enable detection of errors and anomalies in a knowledge-based system.

In this article, we examine the verification of large knowledge-based systems. Because production rules are the most widely used representation scheme for knowledge bases (Awad 1996), we focus on the verification issues associated with large rule bases. In particular, we focus on deterministic rule-based systems. There has been a significant increase in the size of deterministic rule bases used in industrial settings as compared to research laboratories (Murrell and Plant 1996). Several systems have been reported to contain thousands of rules (Soloway et al. 1987, Segev and Zhao 1994, Hou 1996, Goh et al. 1996, Huang and Lin 1996). The cognitive effort required to construct and implement large systems increases considerably with the size of the system (Hogarth 1987, O’Leary 1996). As a result, complex systems are more likely to have errors in design and implementation. Such observations have been well documented by researchers in software engineering in general (Conte et. al. 1986) and rule base development in particular (O’Leary 1996).

When rule bases are large, the verification process poses several problems that are usually not significant for small systems. This is true regardless of the verification technique employed. First, substantial amounts of processing power and storage space are required to perform verification of the entire rule base simultaneously (Coenen and Dunne 1997). Second, to perform verification checks, large amounts of domain knowledge are necessary. This includes information on which variables are observable (or input variables), which are hypotheses (goal) variables, feasible values that variables may take, and other related information (Ramaswamy et al. 1997). The amount of such domain knowledge required for performing verification can grow in a disproportionate manner with an increase in the size of the rule base. As a result, elicitation of such domain knowledge in a holistic manner for large rule bases becomes quite difficult. Finally, the propensity of a rule base to evolve over time is higher for large rule bases. Any revision to the rule base (such as addition, deletion, or modification of rules) requires conducting the set of verification checks for the entire rule base prior to its reuse.

A commonly used approach to minimize the occurrence of errors in large systems, and the effort required in maintaining such systems, is to use modular design methodologies. The idea is to decompose large, complex systems into components that are relatively easy to develop and maintain (Botten et al. 1988). This kind of decomposition has been widely adopted in traditional software development. In recent years, it has been noted that decomposition provides significant benefits for developing and maintaining large rulebased systems (Agarwal and Tanniru 1992b, Hicks 1995). Based on his experiments relating the number of errors to the size of a rule base, O’Leary (1996) also concludes that a modular approach is important when developing large rule bases. Modular development of rule bases has been observed and documented in realworld applications. There is empirical evidence to indicate that sets of rules in large rule bases are often sufficiently separated to allow the rule base to be decomposed into smaller sets (Jacob and Froscher 1986, Gulati and Tanniru 1993).

Although the value of decomposing large rule bases in ensuring the reliability of such systems seems to be generally accepted, there is no prior work that provides guidelines as to what constitutes a good decomposition for the purpose of verification. To characterize a decomposition as good, it is important to specify the basic objectives for performing the decomposition (Conte et al. 1986, Wand and Weber 1990). For rule bases, verification is an integral part of development and maintenance activities, and allows one to assess the reliability of such systems. For this reason, we focus on decompositions that enable verification of rule bases to be performed in a modular fashion. If verification could be efficiently performed for rule-based systems, it would help in significantly reducing the development and maintenance effort associated with such systems.

The main contributions of this research are two-fold. First, we identify a class of graphical structures that we call ordered polytrees, which characterize decompositions that enable verification of rule bases to be performed in a modular fashion. The ordered polytree structure provides a framework for decomposing large knowledge bases into smaller sets of connected partitions of rules. Ideally, we wish to be able to examine each partition independent of the rest of the rule base. Strictly speaking, however, it is not possible to ensure global integrity by performing local verification checks without considering some of the information contained in other partitions. This is so because the partitions must be interrelated (otherwise they are independent rule bases), and inference paths in one partition will influence inference paths in adjacent partitions. On the other hand, we do not wish to retain every detail of each inference path in a partition when examining its adjacent partitions (or other partitions)—in principle, that is equivalent to examining the entire rule base simultaneously. Decomposition schemes can help if we are able to identify that set of information in a partition that can potentially lead to errors or inconsistencies in the rest of the rule base, and, further, this information set can be compactly represented and used in the verification process. Therefore, as part of our first contribution, we also determine the nature of information that must be available during local verification of a partition to detect anomalies that occur because of rules that are in other partitions.

Our second contribution is the development of a methodology that enables efficient verification of large knowledge bases in a modular fashion without compromising on the accuracy of the verification process. We show that a simple extension to an existing verification technique, the directed hypergraph technique (Ramaswamy et al. 1997), enables global verification of a knowledge base by performing local verification of partitions in the ordered polytree decomposition. To take advantage of the modular verification process, it should be possible to verify that the partitions obtained do indeed form an ordered polytree. We present a procedure to determine whether a given set of partitions conforms to a polytree structure. We show how the modular verification algorithm leads, in general, to considerable improvements in the computational effort required for verification as compared to the traditional approach. The improvement is shown to be markedly higher when the knowledge base evolves in an incremental manner.

The rest of the article is organized as follows. In the next section, we provide a brief summary of the nature of structural errors in rule bases, discuss the domain knowledge required for their detection, and present an overview of the directed hypergraph technique to identify such errors. In §3, we first discuss characteristics of rule base structures decomposed as polytrees. Next, we identify the nature of information that must be available during local verification of a partition that would help in detecting anomalies that occur because of rules that are in other partitions. We demonstrate in §4 how an ordered polytree decomposition of a rule base can be accurately verified in a comprehensive manner by performing checks at local levels with the help of the information sets obtained from adjacent partitions. In the same section, we present a formal procedure to perform the verification in a modular fashion for a partitioned set of rules and establish the accuracy of the modular verification process. In §5 we discuss a procedure to verify that partitions provided by experts conform to the requirements of a polytree structure. In §6 we show how the modular verification procedure leads to significant improvements in computational efficiencies as compared to a traditional approach. Concluding remarks appear in §7.

## 2. Verification Using Directed Hypergraphs

We provide a brief overview of the types of problems that are addressed during verification of deterministic rule bases (§2.1) and discuss the nature of domain knowledge required for the verification process (§2.2). Next, we describe a directed hypergraph-based technique for performing verification (§2.3). This technique has been shown to accurately detect the different kinds of anomalies that are of concern during verification of rule bases (Ramaswamy et al. 1997). The technique is used later to demonstrate how verification can be performed in a modular fashion. We summarize the main features of the directed hypergraph technique and direct interested readers to the cited articles for additional details.

## 2.1. Verification of Knowledge Bases

The kinds of anomalies detected during the verification process are sometimes referred to as structural errors (Nazareth 1989). Nazareth has provided a taxonomy of these structural errors, which consist of redundancy, conflict, circularity, and incompleteness (dead ends and unreachable goals). These definitions are consistent with the classification of structural errors addressed in the existing literature (e.g., Murrell and Plant 1996).

A rule base demonstrates redundancy when two or more distinct sets of rules lead to the same conclusion from a given set of observed attribute-values. It should be noted that while it is possible to identify multiple inference paths from one clause to another, such a condition does not necessarily indicate redundant rules. As pointed out in the literature (Ramaswamy et al. 1997), if the intermediate clauses in an inference path are required to establish paths across some other clauses, then there may not exist any redundant rules even when there are multiple paths between two sets of clauses. Thus, multiple paths are identified as potentially implying redundancy. Rules are conflicting when the same premise leads to mutually exclusive conclusions. Rules demonstrate circularity when a premise leads back to itself (or a subset of itself) as a result of making inferences. The existence of such cycles can lead to system breakdowns when a rule that is part of a cycle is activated.

When performing checks for completeness, the objective is to identify if relevant rules inadvertently have been left out from the rule base. Such missing rules are indicated either by dead ends or by unreachable goals. When the conclusion of a goal is not a goal variable, nor is it part of the condition of some other rule, then that conclusion constitutes a dead end. When the antecedent of a rule does not consist of observable inputs, and one or more attribute-values in the antecedent have no inference paths that lead to it, then that rule cannot be fired under any circumstance. The conclusion of the rule is unreachable, because the antecedent is unreachable. The antecedent of that rule constitutes an unreachable goal (or subgoal).

Before a rule base is verified for correctness, a requirement often imposed is that all rules are in unitized form (Pederson 1989, Ramaswamy et al. 1997). This implies that compound antecedent clauses in rules only allow conjunctions, and only simple clauses are allowed as conclusions. Each simple clause corresponds to an attribute-value pair. Formally, the unitized rule structure, expressed in Bacchus-Naur form, is:

```autohotkey
<Rule> ::= IF <Premise> THEN <Conclusion>
<Premise> ::= <PremiseClause> | <PremiseClause> AND <Premise>
<Conclusion> ::= <ConclusionClause>
<PremiseClause> ::= (<attribute> has <value>)
<ConclusionClause> ::= (<attribute> has <value>)
```

This structure is widely used, often with an additional numeric certainty factor associated with the ConclusionClause (Trice and Davis 1993).

We note that many development shells allow disjunctions in antecedent clauses, as well as conjunctions of clauses in the conclusions of rules; however, converting such a set of rules to a logically equivalent set of unitized rules is easy. If a rule has disjunctions in its antecedent clause, it can be converted into a set of equivalent unitized rules by having a separate rule corresponding to each subclause in its antecedent. Similarly, if a rule has multiple conclusions (conjunctions of clauses), it is converted into a set of equivalent unitized rules by having a separate rule corresponding to each individual conclusion with the same antecedent as the original rule. Disjunctions are not allowed in the conclusions of rules in rule-based expert systems since inference engines cannot reason with such rules.

Therefore, without loss of generality, we assume that all rules are in unitized form before they are used to detect errors. We note that rules in unitized form can be viewed as Horn clauses.

2.2. Domain Knowledge Required for Verification Automated techniques that perform verification of knowledge bases require domain knowledge about an application to identify some of the anomalies described earlier. This domain knowledge is in addition to the rules themselves. When detecting conflicts it is necessary to know which attribute-value pairs are mutually exclusive. In some situations, this information may be easily derived from the rules themselves (e.g., when each value of an attribute is considered to be distinct and exclusive of other values of the same attribute). Otherwise, values of attributes that are contradictory must be clearly identified during the knowledge elicitation process and stored as part of the knowledge base. This information may be stored as a separate list (the mutual exclusion list) that comprises sets of mutually exclusive attribute-values. For in stance, if only some values of an attribute are mutually exclusive, only those values would be included as a set in this list. If attribute-value pairs of different attributes are mutually exclusive, these will be included in the list as well. For notational convenience, we assume in some examples that different values of the same attribute are mutually exclusive. The veracity of our procedure is not affected by this assumption since the verification mechanism uses information in the mutual exclusion list to detect conflicts. To detect dead ends and unreachable goals, it is necessary to know which attributes have values that will be provided by the user of the system at run time (what we call input variables), which ones are eventual goal variables, and which ones are intermediate variables provided by the domain expert to capture the dependencies between the input and output variables.

Many of the verification techniques proposed in the literature focus on anomalies that can be detected with domain knowledge of the nature discussed above (e.g., Nazareth and Kennedy 1991, Agarwal and Tanniru 1992a). Those studies focus on identifying structural errors that can be detected by tracing paths that originate from antecedent clauses of a single rule. It is possible to detect additional structural anomalies when more domain knowledge is available from experts (Ginsberg 1988, Nazareth 1993, Preece 1993, Sarkar et al. 1995). In particular, additional structural anomalies can be detected when we consider situations where paths are traced from sets of antecedent clauses that correspond to multiple rules. To perform such checks, it is necessary to obtain from experts valid combinations of simultaneously observable attribute-values. This additional domain knowledge can be high in volume, and typically requires a substantially larger amount of effort on the part of the experts. Note that it is not meaningful to consider arbitrary (or all) combinations of observable attribute-values, because many combinations are infeasible (e.g., involving two or more mutually exclusive attribute-values) and should not be used for verification. When this additional domain knowledge is available, the directed hypergraph technique is able to easily incorporate the knowledge in the verification process to broaden the search for anomalies (detailed discussion is provided in Sarkar et. al. 1995). For ease of exposition, in this article we use examples of structural anomalies that can be detected based on the domain knowledge described earlier (without requiring the additional domain knowledge corresponding to valid combinations of simultaneously observable attribute-values).

## 2.3. The Directed Hypergraph Approach

Graphical techniques have been found to provide a good framework for the detection of errors that may appear in a rule base (Nazareth and Kennedy 1991, Agarwal and Tanniru 1992a, Nazareth 1993, Ramaswamy et al. 1997). Graphs provide an easy to use framework for visualizing and representing conceptual dependencies across attributes (as well as attribute-values). At the same time, they allow for rigorous verification checks based on their associated matrix representations. In this article, we consider the directed hypergraph approach for verification of rule bases (Ramaswamy et al. 1997). The primary reason for using directed hypergraphs is that compound clauses in rules can be explicitly represented by such graphs without recourse to contrived representations. The approach allows rules to be represented in a manner that clearly identifies complex dependencies across compound clauses in the rule base. Connectivity across compound clauses is accurately represented, and the associated verification procedure has been shown to detect errors in an accurate fashion. We have used the directed hypergraph technique to illustrate the value of modularizing rule bases because of the generality of the approach. This generality is achieved without incurring additional computational effort as compared with other techniques (Ramaswamy et al. 1997).

We provide a brief overview of the directed hypergraph representation of a rule base before discussing the verification approach itself. In this representation, simple and compound clauses in a rule base are represented as simple and compound nodes, respectively. Thus, a node is compound if it consists of a conjunction of two or more attribute-value pairs. Each node appears exactly once in a directed hypergraph. A rule is uniquely represented as a directed arc across nodes (simple or compound as the case may be) that correspond to its antecedent and conclusion clauses. The direction of the arc is determined by the causality implied by the rule. There is a unique directed hypergraph representation for each set of rules. We use a stylized set of rules, adapted from a project termination model for R&D projects (Balachandra and Raelin 1980), to illustrate the directed hypergraph representation.

<table><tr><td>Rule 1: IF</td><td>the expected return on investment is high (a1),</td></tr><tr><td>THEN</td><td>the degree of commitment of project leader is high (d1).</td></tr><tr><td>Rule 2: IF</td><td>the likelihood of technical success is high (b1),</td></tr><tr><td>AND</td><td>the likelihood of commercial success is high (c1),</td></tr><tr><td>THEN</td><td>the project can be completed within three years (e1),</td></tr><tr><td>Rule 3: IF</td><td>the likelihood of technical success is high (b1),</td></tr><tr><td>AND</td><td>the likelihood of commercial success is high (c1),</td></tr><tr><td>THEN</td><td>federal grants are available (f1).</td></tr><tr><td>Rule 4: IF</td><td>the degree of commitment of project leader is high (d1),</td></tr><tr><td>AND</td><td>the project can be completed within three years (e1).</td></tr><tr><td>THEN</td><td>the project classification is “A” (g1).</td></tr><tr><td>Rule 5: IF</td><td>the project can be completed within three years (e1),</td></tr><tr><td>AND</td><td>federal grants are available (f1),</td></tr><tr><td>THEN</td><td>the project classification is “A” (g1).</td></tr><tr><td>Rule 6: IF</td><td>federal grants are available (f1),</td></tr><tr><td>THEN</td><td>allocate more personnel (h1).</td></tr><tr><td>Rule 7: IF</td><td>the project can be completed within three years (e1),</td></tr><tr><td>THEN</td><td>do not allocate more personnel (h2).</td></tr></table>

For notational convenience, we represent rules symbolically as described below. Each attribute-value is represented by a lower case alphabet paired with a numeric digit; the alphabet indicates an attribute and the numeric digit indicates the value for that attribute. Thus, an attribute A with three legal values is represented as a1, a2, and a3. For example, rule R2 is denoted as: b1  c1 → e1. At times, for the sake of compactness, we also use the form b1,c1 → e1 to represent a rule. The rule set is symbolically represented as follows.

$$
\begin{array}{l l l l l}\text {Rule 1:}&a 1&&\rightarrow&d 1\\\text {Rule 2:}&b 1 +&c 1&\rightarrow&e 1\\\text {Rule 3:}&b 1 +&c 1&\rightarrow&f 1\\\text {Rule 4:}&d 1 +&e 1&\rightarrow&g 1\\\text {Rule 5:}&e 1 +&f 1&\rightarrow&g 1\\\text {Rule 6:}&f 1&&\rightarrow&h 1\\\text {Rule 7:}&e 1&&\rightarrow&h 2\end{array}
$$

Figure 1 illustrates the directed hypergraph representation for the above rules.

The condition clause of Rule 2 consists of a conjunction of two attribute-value pairs. Therefore, the rule is represented by a directed arc from a compound node (corresponding to the compound condition clause b1 AND c1) to a simple node (corresponding to the rule’s conclusion e1). The conclusions (attribute-values) that can be inferred from the premise of a rule are determined from the hypergraph by identifying those nodes that are reached by following the directed arcs. Thus, feasible inference paths from one set of clauses to another are indicated by reachability relations across the corresponding nodes in the hypergraph. We should point out that a path from a compound node (b1,c1) to a simple node (e1) does not imply that e1 can be reached from either b1 or c1 individually. On the other hand, if (b1,c1) reaches e1, all supersets of (b1,c1) can also reach e1.

Figure 1 Directed Hypergraph for Rules 1 through 7  
![](/api/attachments/6Q8DYXRN/fulltext/images/0336ad36f2f4be7597922fb5897e100e0d125a89be400d4d846c00395b916b88.jpg)

A node corresponding to either the condition clause or the conclusion clause of a rule is called a hypernode. A hypernode is a simple node if it comprises a single attribute-value pair, otherwise it is a compound node. We refer to a hypernode by using either the attributevalue(s) of the corresponding clause or an uppercase character with an underscore. For example, Rule 2 can be written as U; V-, where U - (b1, c1) and V - (e1).

A path (alternately referred to as a hyperpath) is a collection of rules that makes up the inference path from one hypernode to some other hypernode. To uniquely identify a hyperpath, it is necessary to specify the originating and terminal hypernodes and the collection of rules that makes up the hyperpath. In Figure 1, the inference path between (b1,c1) and (h1) can be written as P{b1, c1; h1 \ b1, c1; f1-, f1; h1-{. Providing only the originating and terminal hypernodes is not enough to specify a hyperpath because there may be multiple inference paths (through different rules) between the originating and terminal hypernodes. Providing only the rules is also not adequate, because the same set of rules can be used to represent hyperpaths with different originating hypernodes. Thus, in Figure 1, the two hyperpaths P{e1, f1; h1 \ f1; h1-} and P{f1; h1 \ f1; h1-} have the same rule set. We consider these two paths as distinct because the originating hypernodes are different. This enables us to detect errors that result from different paths, when the originating hypernode of one path subsumes the originating hypernode of another path. Because the representation for a hyperpath may consist of a large number of rules, we do sometimes use a shorthand notation consisting of only the originating and terminal hypernodes in situations where there is no ambiguity.

In some situations, there can be more than one sequence in which the rules are fired to reach the terminal hypernode. In Figure 1, the hyperpath between the two compound nodes $( \mathrm { b } 1 , \mathrm { c } 1 )$ and (e1,f1) can be written as either P{b1,c1,f1 \ b1, c1; e1-, b1, c1; f1-} or as P{b1,c1,f1 \ b1, c1; f1-, b1, c1; e1-}. This is confusing when the inference chain consists of a large number of rules that are interdependent. The actual sequence in which rules are fired will depend on the control strategy of the inference engine that is used. To make our notation implementation independent, we use the notion of a segment to identify the logical sequence of rules that constitutes a hyperpath. For the sake of illustration, we assume the following: (1) Rules are fired using forward chaining, and (2) when one or more attribute-values are provided to the system at run time, the inference mechanism examines every rule in each pass of the rule base (thus, multiple rules may be fired in each pass of the rule base). We define the first segment of a hyperpath as those rules in the inference path that are fired in the first pass, when the attribute-value(s) of the originating hypernode is (are) known to be true. The next segment corresponds to those rules in the inference path that are fired when the conclusions of the first segment are added to the set of known assertions. Thus, a hyperpath is an ordered sequence of segments, with rules in a segment being fired in the same pass of the rule base. When two rules b1, c1; e1- and b1, c1; f1- are part of the same segment, then we denote them as: «b1, c1; e1-, b1, c1; f1-». To explicitly identify each segment when representing the hyperpath P{b1, c1; g1}, we denote it as P{b1, c1; g1 \ «b1, c1; e1-, b1, c1; f1-», «e1, f1; g1-»}. The order of rules within each segment is not important. However, the order of each segment is important and helps identify the flow of reasoning in a path. We note that the assumption of forward chaining is used merely to help define a segment, and that the definition of errors and the procedures for their detection is a function of the rule base and not of the inference mechanism that is used.

Paths in directed hypergraphs are classified into two categories, simple paths and strict hyperpaths. A path between two nodes is simple if every segment of the path has exactly one rule. In Figure 1, the path from (b1, c1) to (h1) is a simple path. The first segment has rule R3, and the second rule R6. A path between two nodes is a strict hyperpath if at least one segment of the path has two or more rules. The path from (b1, c1) to (g1) in Figure 1 is a strict hyperpath. The first segment of this strict hyperpath has two rules R2 and R3. The second segment has the rule R5. This distinction between simple and strict hyperpaths helps to comprehensively identify the different paths of each type that may exist between a pair of hypernodes.

The main idea behind the verification procedure is to accurately identify all feasible inference paths for a given rule base, taking care to not generate spurious paths. This translates to identifying all paths (simple and strict hyperpaths) in the directed hypergraph. The identification of paths and performing the checks to identify anomalies are accomplished by using an adjacency matrix representation of the directed hypergraph. The adjacency matrix has a row and a column for every hypernode in the hypergraph. In addition to standard matrix operations, we define two additional operations called row revision and column revision to accurately detect strict hyperpaths. The adjacency matrix, A, is initialized by capturing simple paths of length one (i.e., those corresponding to the rules themselves). Paths (hyperpaths) of longer length are obtained by performing certain operations on the adjacency matrix in a specified sequence. New matrices are generated in the process. The verification procedure consists of a series of checks that use the domain knowledge in conjunction with the generated matrices to identify all of the anomalies in the rule base (i.e., conflicts, potential redundancies, cycles, dead ends, and unreachable goals). The computational complexity of this technique is of the same order as that of other graph-based techniques (Ramaswamy et al. 1997). We provide in the appendix a summary of the important results and a small example to illustrate the verification procedure.

When additional domain knowledge in the form of combinations of simultaneously observable attributevalues (as discussed in §2.2) is available, the hypergraph technique is able to incorporate this knowledge in the search for errors quite elegantly. Each such combination is considered to be a compound node. Subsequently, inference paths that originate from such compound nodes are traced by the verification procedure, and anomalies (not otherwise detectable) are accurately identified. Interested readers are directed to Sarkar et al. (1995) for an in-depth discussion of this procedure.

## 3. Requirements for Modular Verification of Large Knowledge Bases

We consider decompositions of rule bases where the partitions consist of disjoint sets of rules. Partitions are connected to each other through attribute-values that appear as part of two or more rules, and each rule is in a different partition. Such partitions are considered to be adjacent, and the attribute-value is considered to be shared across the partitions. We note that the same attribute-value may be shared by more than two partitions. We are interested in identifying decomposition structures that enable verification of rule bases to be performed in a modular fashion, thereby facilitating the development and maintenance of such systems. In other words, we desire those decomposition schemes that enable us to infer about the global integrity of a rule base by performing local verification on the decomposed partitions. As discussed in §1, it is not possible to ensure global integrity by performing local verification checks without considering some of the information contained in other partitions. Decomposition schemes can help if we are able to identify that set of information in a partition that can potentially lead to errors or inconsistencies in the rest of the rule base, and, further, this information set can be compactly represented and used in the verification process.

In this section, we first discuss what constitutes an ordered polytree structure in the context of rule base decompositions, and then identify the nature of information that must be available during local verification of a partition that would help in detecting anomalies that occur from rules in different partitions.

## 3.1. Ordered Polytrees

We identify three requirements that characterize decomposition structures that allow modular verification. These requirements are used to provide a formal definition of such structures, which we call ordered polytrees.

Definition: A partitioned set of rules forms an ordered polytree if:

(i) any two partitions are connected through an unique set of intermediate partitions;

(ii) all pairs of adjacent partitions can be ordered; and

(iii) all nodes corresponding to mutually exclusive attribute-values appear in the same partition(s).

We should point out that the first requirement precludes the possibility of having cycles across partitions. Cycles that exist within a partition are detected during local verification of the partition using the directed hypergraph approach.

3.1.1. Polytree Structured Partitions. To ensure that the information set needed for the partition under review does not become as voluminous as the entire set of paths in all the other partitions, it is necessary that nodes in different partitions do not have paths via different sets of intermediate partitions. The first requirement, then, is that any two partitions are connected through only one set of intermediate partitions. We term decomposition schemes that meet this requirement as polytrees (these structures are similar to causal polytrees defined by Pearl 1988). Figure 2a illustrates a polytree structure; Figure 2b illustrates a structure that is not a polytree (this is because partition P4 is connected to P1 through partition P2 as well as P3). For the purpose of verification, nonpolytree structures are undesirable, as illustrated in the following example. Consider Figure 2b. Let there be a path from an attribute-value (say, a1) in P1 to an attribute-value (say, b1) in P4 that traverses through P2. Let there be another path from a1 to b1 that traverses through P3. When examining P4, to recognize the existence of these multiple paths from a1 to b1, we will typically need to remember all paths in P1, P2, and P3.

When three or more partitions are mutually adjacent, it is necessary that each shared attribute-value appear in each of those partitions. Thus, in the example shown in Figure 3, it is necessary that all the shared attribute-values appear in the region indicated by I, and the regions marked II, III, or IV do not consist of any attribute-values. Otherwise, it would be possible to have an inference path from an attribute-value in P1 to an attribute-value in P3 that passes through attribute-values that appear in II and IV, as well as another inference path across the same originating and terminating attribute-values that passes through nodes in III. In effect, partitions P1 and P3 would be connected by more than one set of intermediate partitions if the above requirement is not met, thus disabling modular verification.

(b)  
Figure 2 Polytree and Nonpolytree Decompositions  
![](/api/attachments/6Q8DYXRN/fulltext/images/45629f7d8596584abfe464bf50a7ee2492407edf41faff0e7f738f6fb55629c8.jpg)  
(a)

An important implication of the polytree requirement is that when two partitions are adjacent, all paths originating in one and ending in the other must pass through a subset of the set of nodes shared by the two partitions. Similarly, for all nonadjacent partitions, all paths originating in one and ending in the other must pass through the same set of intermediate partitions.

3.1.2. Ordering of Partitions. A second requirement for modular verification is that it should not be necessary to examine the same partition multiple times during the verification process. This requirement suggests that partitions be ordered prior to the verification process, and the information set needed when examining a partition should be derived from its immediately preceding adjacent partitions. The partitions can be ordered by using the causality implicit in the rules themselves. For example, if two adjacent partitions share an attribute-value that is a conclusion of a rule in the first partition and the antecedent (or part of the antecedent) of a rule in the second partition, then the first partition is considered to precede the second one. Orderings across partitions are considered to be transitive. Therefore, if partition P1 precedes P2, and P2 precedes P3, then P1 is considered to precede P3 as well. Using the property of transitivity and orderings across adjacent partitions, we derive a complete ordering for all of the partitions that constitute a rule base. We term polytree decomposition schemes that consist of ordered partitions as ordered polytrees.

![](/api/attachments/6Q8DYXRN/fulltext/images/4bb389f426a5dba784cb347e69385c4acd1761e765adf6afc800499b39a080e0.jpg)

Figure 3 Polytree Structure with Three Mutually Adjacent Partitions  
![](/api/attachments/6Q8DYXRN/fulltext/images/04ef5fb2c039aa3529c3d3deee2748a4bc6c0e6c1b0f029abb1fe4a555b41502.jpg)

Figure 4 Rule Base Partitioned as a Polytree  
![](/api/attachments/6Q8DYXRN/fulltext/images/04fd6d20b18f90a55db87ae704c3002c44920c88987edfa52a836fdec5ad62db.jpg)

In some situations, more than one ordering of partitions may be feasible based on the pairwise orderings implied by the rules. The example rule base shown in Figure 4 helps illustrate this. In this example, the rule base has been decomposed into five partitions, which are as follows:

Partition P1: R1 a1  b1 → c1

$$
\mathrm{R2} \quad \mathrm{a2+b2→c2}
$$

Partition P2: R3 d1  e1 → f1

$$
\mathrm{R4} \quad \mathrm{d2+e2} \rightarrow \mathrm{f2}
$$

Partition P3: R5 g1  c1 → j1

$$
\mathrm{R6} \quad \mathrm{c2+f1} \rightarrow \mathrm{k1}
$$

$$
\mathrm{R7} \quad \mathrm {f2+ h1\rightarrow m1}
$$

$$
\mathrm{R10} \quad \mathrm{m1} + \mathrm{n1} \rightarrow \mathrm{q2}
$$

We find that partition P1 precedes P3 based on the rules in those partitions. This is because the shared attribute-values c1 and c2 are conclusions of rules in P1 and part of antecedents of rules in P3. In a similar manner, we can determine that P2 precedes P3, and P3 precedes both P4 and P5. Four distinct complete orderings are feasible based on these pairwise orderings. They are:

(i) P1, P2, P3, P4, P5;

(ii) P2, P1, P3, P4, P5;

(iii) P1, P2, P3, P5, P4; and

(iv) P2, P1, P3, P5, P4.

Each of these orderings is valid, and can be used as the sequence for examining partitions during the verification process.

There are situations where no valid ordering is possible between two adjacent partitions. Such situations arise when there exist among the shared attribute-values some that are (part of) antecedents in the first partition and some that are part of conclusions in the first partition, as well as some that are part of antecedents in the second partition and some that are part of conclusions in the second. In other words, in each partition there is at least one rule with a shared attribute-value as a conclusion and another rule with a shared attribute-value as an antecedent (or part thereof). In these situations, it is possible to have paths that originate in the first partition and end in the second, as well as paths that originate in the second and end in the first. Moreover, it is possible that a path originates in the first partition, traverses through the second, and eventually ends again in the first partition! This prevents us from using any one sequence to examine the partitions and ensure the integrity of the entire rule base. Figure 5 illustrates such a situation. Consider e1 and e2 to be mutually exclusive. Then, the two conflicting paths from (a1,b1) to e1 and $\mathrm { e } 2 ,$ respectively, cannot be detected in a modular fashion regardless of the order in which the partitions are examined.

We do not allow decompositions that lead to partitions that cannot be ordered. We wish to emphasize that this is the case if and only if there is a possibility for inference paths in both directions across adjacent partitions. In all other situations, a feasible ordering is possible. For instance, in Figure 5 if R4 was not part of the partition P1, then we could order P1 to precede P2. This is because there would be no rule in P1 that had a shared attribute-value as an antecedent, and therefore there could be no paths from P2 to P1 (which are not included entirely in P1). Similarly, if R6 was not part of P2, we could order P2 to precede P1. In this case, there would be no rule in P2 with a shared attribute-value as an antecedent, and therefore there could be no paths from P1 to P2 (which are not included entirely in P2). We note that in some cases it may be possible to provide any arbitrary ordering for two adjacent partitions. This occurs where either all of the shared nodes are strictly conclusions in both partitions or where all of the shared nodes are strictly antecedents in both.

Figure 5 Adjacent Partitions That Cannot Be Ordered  
![](/api/attachments/6Q8DYXRN/fulltext/images/1d266308412b601885a8f93769c9b05d886e4c2fb617efd1606bdbc95eb34029.jpg)

3.1.3. All Mutually Exclusive Attribute-Values in the Same Partition. The third requirement for a feasible decomposition structure that allows modular verification is that when an attribute-value is in a particular partition, all other mutually exclusive attributevalues must also appear in the same partition. The simple example in Figure 6 shows why this is necessary. Consider that d1 and g1 are mutually exclusive. If a1 and b1 are observed to be true, then we find that both d1 and g1 are inferred to be true, which is contradictory. Consider the nodes corresponding to attributevalues d1 and g1 to be in separate partitions as shown in the figure. When examining partition P2, it is necessary to remember all the paths in P1 to recognize the contradiction implicit in the rule base.

The three requirements we have discussed provide us with the necessary characterization of the decomposition structures that allow modular verification. We note that the attribute parameter network presented in Gulati and Tanniru (1993) is a special instance of an ordered polytree. The attribute parameter network corresponds to a simple hierarchy where adjacent partitions are allowed to share nodes corresponding to only a single variable. For example, partitions P3, P4, P5, and P6 in Figure 2a would correspond to a simple hierarchy derived from an attribute parameter network if adjacent partitions shared exactly one variable. As evident from the polytree requirements, it is considerably less restrictive than an attribute parameter network in terms of overall structure and number of shared variables.

Figure 6 Mutually Exclusive Attribute-Values d1 and g1 in Different Partitions  
![](/api/attachments/6Q8DYXRN/fulltext/images/6cc4d3839983891d39ebfe3267453b3c45ef17923cdb46b34ac8424990d5294a.jpg)

## 3.2. Information Set for Modular Verification

To highlight the nature of information that is needed from adjacent partitions when performing local checks, we use a simple example to illustrate some of the difficulties encountered when verifying partitions locally. The rule base used in the example consists of two partitions with six rules in each partition. The rules are:

```txt
Partition P1
R1. a1 + b1 → d1
R2. a1 → f1
R3. a1 + b1 → g1
R4. a1 + b1 → h1
R5. b1 + c1 → i1
R6. d1 → e1
R7. e1 → k1
R8. j1 → m1
R9. gl → ml
R10. g1 → ml
R11. h1 → q1
R12. h1 + i1 → n1
```

The directed hypergraph for the rule base is shown in Figure 7.

The following domain information is assumed to be available for this example.

• Attribute-values k1 and q1 are mutually exclusive.

• Attributes a, b, and c are observable (i.e., attributevalues a1, b1, and c1 are the observable facts). These attributes are called global inputs and are identified with \* in the hypergraph.

• Attributes k, m, n, and q are global outputs (i.e., attribute-values k1, m1, n1, and q1 are goals). They are identified using the # symbol in the hypergraph.

All other attribute-values in the rule base are assumed to correspond to intermediate variables provided to help capture the dependencies across the input and output variables. The anomalies that exist in this example rule base are:

Figure 7 Directed Hypergraph for Rules R1 – R12 Decomposed into Two Partitions  
![](/api/attachments/6Q8DYXRN/fulltext/images/b51b8209ce388df71b5d030775f4c68ff0b0c99506c616c69f4752d9175d13a8.jpg)

(i) Redundancy: There are two paths from (a1, b1) to m1. One path is through rules R3 and R9, the other through R4 and R10.

(ii) Contradiction: Goal k1 can be reached from (a1,b1) via rules R1, R6, and R7, whereas goal q1 is reached from (a1, b1) through rules R4 and R11.

(iii) Dead end: The attribute-value f1 (conclusion of rule R2) is neither a goal variable nor is it an antecedent of another rule. Thus, it constitutes a dead end.

(iv) Unreachable goal: The attribute-value j1 (antecedent of rule R8) is neither an input variable nor is it a conclusion of any rule. Thus, it constitutes an unreachable goal.

There are several reasons why we cannot examine the two partitions in isolation of each other. Consider partition P1. Given the domain information, and the set of rules R1 through R6, we cannot find any instances of contradictions or multiple paths across pairs of nodes (hypernodes). There are no unreachable goals to be found here either. What we can find is that the attribute-values e1, f1, g1, h1, and i1 are all potential instances of dead ends (since they do not correspond to global output variables and are not antecedents, nor part of antecedents, of rules in partition P1). However, since they could be antecedents of rules in the other partition, we are not able to definitively conclude anything about them. Now consider partition P2. Here, too, based on rules R7 through R12, we cannot find any instances of contradictions or redundant paths. There are no dead ends in partition P2 either. There do exist a few nodes that are potentially unreachable goals. The nodes e1, g1, h1, i1, and j1 are neither global inputs for the rule base, nor are they conclusions of any rule in P2. Once again we cannot conclude whether these nodes are truly unreachable or are reached by rules in P1.

Of course, the reason for not being able to detect any of the errors is that, in the above scheme, we have not considered how the rules in partition P1 are interrelated with those in partition P2. When examining a particular partition, to detect the errors accurately we must first identify the information set from adjacent partitions that must be available. We next discuss the nature of this information set.

From the above example, we find that to identify dead ends and unreachable goals, we need to know which nodes are shared with each adjacent partition. For example, we can see from Figure 7 that node f1 is not shared with partition P2. If we know this when examining partition P1, we can conclude that f1 is indeed a dead end. On the other hand, knowing that node g1 is shared with partition P2, when we examine P1 we do not conclude that node g1 is a dead end. Later, when examining P2, we note that g1 is a shared node with a predecessor partition P1, and thus recognize that it is not an unreachable goal. In a similar manner, nodes e1, h1, and i1 are not identified as dead ends when examining P1, or as unreachable goals when examining P2. At the same time, node j1 can be conclusively identified as an unreachable goal in partition P2 because it is not shared with any other partition.

A different kind of information is required to accurately identify the contradictions and redundancies in the above example. The localized checks miss the two paths from (a1, b1) to m1 since they pass through different shared nodes (g1 for the path P{a1, b1; m1 \ «‹a1, b1: g1-», «g1; m1-»}, and h1 for the path P{a1, b1; m1 \ «a1, b1: h1-», «h1; m1-»}). To detect these two paths, when checking P2 we need to be aware of the fact that both nodes g1 and h1 are reached by the same antecedent (a1,b1) in P1. Note that we do not wish to remember all the paths in P1 when verifying P2 (or vice versa). Instead, when verifying P1 we need to recognize that the shared nodes g1 and h1 have a common antecedent. By considering this information when verifying P2, we can recognize that there are two paths from the same originating hypernode to node m1, indicating the existence of multiple paths.

Figure 8 Partition P1 Before and After Verification  
![](/api/attachments/6Q8DYXRN/fulltext/images/e2940a7cecb95f96cffb7869bbd3d9ec8a3956abc48d6a9f70307292e9e47e6c.jpg)  
sets (i) and (ii) can be easily obtained prior to the verification process. The information set (iii) can be collected during local verification of predecessor partitions.

The kind of information used in detecting redundancies also helps in recognizing the contradiction in the example rule base. When examining P1, we find that the compound antecedent (a1,b1) reaches the shared node e1 in addition to g1 and h1. Therefore, considering this when examining P2, we can determine that there exist paths from the same originating hypernode that reach both k1 and q1, indicating a contradiction.

The above example illustrates what should constitute the information set that a local verification procedure needs to obtain from adjacent partitions. The required information set, then, consists of the following:

(i) List of all preceding partitions that are adjacent and nodes shared with each such adjacent partition.

(ii) List of all succeeding partitions that are adjacent and nodes shared with each such adjacent partition.

(iii) For the set of shared nodes in every predecessor, those subsets of nodes that are reached from the same hypernode.

For the information identified in (iii), we should emphasize that a common originating hypernode could be in the adjacent predecessor partition or in some partition that is a more distant predecessor. Information

## 4. Global Verification Through Local Checks

We show how the directed hypergraph procedure can be easily extended to detect anomalies in a modular fashion by incorporating the information set in the procedure. This is accomplished by appropriately capturing the relevant sets of information from adjacent partitions. We first provide an example to illustrate the process and then provide the formal procedure. Finally, we present two important proofs that establish the accuracy of the verification technique.

## 4.1. Example

We use the example shown in Figure 7 to illustrate how the directed hypergraph procedure can accommodate the information from adjacent partitions. Figure 8a shows how partition P1 is revised to capture the relevant information prior to its verification. Figure 8b also includes the information generated during the verification of P1 that is relevant when examining P2.

Nodes e1, g1, h1, and j1 are italicized in Figure 8a to indicate that they are shared with partition P2. During local verification, node f1 can be recognized as a dead end because it does not appear as a shared node with the succeeding partition, nor is it a global output. No other anomalies are noted during this verification process. Before verifying partition P2, the relevant information set is obtained from P1. This is shown in Figure 8b. The fact that nodes e1, g1, h1, and i1 are shared, and P1 precedes P2, leads us to consider them as observable when P2 is examined (it is akin to considering these nodes as reachable in partition P1—note that if any one of these nodes was not reachable in P1 and was a shared node, then it would have been identified as unreachable in P1 itself). All nodes shared with adjacent preceding partitions are considered to be strictly local inputs for partition P2. Note that they are distinct from global inputs. This is indicated with the help of double asterisks in Figure 8b. Another useful piece of information obtained when verifying P1 is that, among all of the shared nodes, nodes e1, g1, and h1 can be reached by a common hypernode (a1, b1). The directed hypergraph procedure recognizes these reachability relations from the final matrix obtained for partition P1 (which is the final $\mathbf { B _ { i } }$ matrix as defined in the appendix). These reachability relations are captured by creating a virtual hypernode comprising of the three nodes (e1, g1, h1).

Figure 9 shows the revised partition P2 prior to verification. Nodes e1, g1, h1, and i1 are considered to be observable (strictly local inputs) at this stage of the verification process; thus, although they are not reachable locally in P2, they are not flagged as unreachable goals in the rule base. There are no global inputs in P2. As a result, it is possible to correctly conclude that node j1 is an unreachable goal. When examining P2, the virtual hypernode (e1, g1, h1) created earlier is treated as just another hypernode. Subsequently, the hypergraph technique recognizes that there are two distinct paths from this virtual hypernode to node m1, indicating potential redundancies in the rule base. The technique also identifies the paths from the virtual hypernode to the two nodes k1 and q1, indicating contradiction in the rule base. Thus, each anomaly present in the rule base is accurately identified.

Figure 9 Revised Partition P2 before Verification  
![](/api/attachments/6Q8DYXRN/fulltext/images/c8c501c5c28b4ef945c6ce93620b19d4349e8c2805e319ef01fa47c8faf957d6.jpg)

In the example shown, the redundant and contradictory paths identified in P2 originated from the hypernode (a1, b1) in the immediate predecessor partition. It is easy to see that the generation of virtual hypernodes allows us to detect such anomalies across longer sequences of partitions. For instance, consider a hypothetical partition P3 that shares nodes k1 and m1 with partition P2. After verifying P2, we would create the virtual hypernode (k1, m1) since they are both reached from (e1, g1, h1). When examining P3, the new virtual hypernode would be used in the local verification process, accurately identifying global reachabilities (and therefore anomalies, where appropriate).

## 4.2. Procedure for Modular Verification

We present here the modular verification procedure using the directed hypergraph approach. For this discussion, we assume that the expert has provided a set of partitions that conforms to the characteristics required for an ordered polytree structure (we discuss in §5 a procedure to ensure that a given decomposition scheme has the desired structure). The procedure consists of three main processes. First, the set of adjacent partitions, along with the appropriate shared nodes, are identified. Next, a valid ordering of partitions is obtained. This is derived from the pairwise ordering of adjacent partitions, which is, in turn, obtained from the rules in the partitions. Finally, for each partition, local checks are performed, and the information sets for succeeding adjacent partitions are generated.

## Stage 1: Identifying adjacent partitions.

• Create two lists, one that will keep track, for each partition, of all of the adjacent partitions (adjacent partitions list) and another that will keep track of all the shared attribute-values (nodes) between pairs of adjacent partitions (shared nodes list).

• Perform the following procedure for all partitions in any sequence. For each node in a partition, examine all other partitions to see if that node appears in them. If it does, modify the adjacent partitions list and the shared nodes list if necessary.

## Stage 2: Obtaining a valid ordering.

• For each pair of adjacent partitions, determine the precedence ordering. To do this, examine the shared nodes in each partition, checking to see whether they are in antecedents of rules, or in conclusions, or both. If one or more shared node in a partition is a conclusion of one partition, and one or more shared node is an antecedent of the other, then the former precedes the latter. Otherwise, no pairwise ordering is assigned for those two partitions (any ordering would work).

• Identify, from the set of available partitions, a partition that has no predecessor. Label it as the first partition (note that there may be several candidates).

• Repeat the following until all partitions are labeled.

• Ignore the pairwise orderings that involve the labeled partition(s), and eliminate those partitions from further consideration. Label as the next partition that which has no predecessors in the revised list of pairwise orderings.

## Stage 3: Performing verification checks.

• Repeat the following steps for each partition in the appropriate order.

• Generate the appropriate matrices for the partition under consideration. Perform the following checks for the different types of anomalies:

Unreachable goals: If a node is not a conclusion of a rule in that partition, and it is not identified as either a global input or a strictly local input, then that node is unreachable.

Dead ends: If a node is not an antecedent of a rule in that partition, it is not identified as a global output, and it is not shared by a succeeding partition, then that node is a dead end.

Cycles: If there exists a path from a node (hypernode) that ends in itself (or a part of itself), it indicates a cycle.

Redundancies: If there exist multiple distinct paths from a hypernode (virtual or otherwise) to another node in that partition, it indicates the existence of multiple paths in the rule base. If the originating hypernode is not virtual, the multiple paths are entirely localized. Otherwise, the multiple paths span two or more partitions.

Conflicts: If there exist paths from a hypernode (virtual or otherwise) to two or more nodes that are mutually exclusive (as identified in the mutual exclusion list), it indicates the existence of conflicting paths in the rule base. If the originating hypernode is not virtual, the conflicting paths are entirely localized. Otherwise, the conflicting paths span two or more partitions.

• Revise the information set for each adjacent successor partition as follows.

Strictly local input: Identify each node shared with a successor partition as a strictly local input for that successor.

Virtual hypernode: Consider shared nodes that are reached from the same hypernode as a virtual hypernode. This is operationalized in the matrix procedures by identifying (in the final C matrix defined in the appendix) those sets of nodes that are shared with the successor partition and reached from the same hypernode.

It should be pointed out that, operationally, all of the checks for verification, and the steps for identifying the information sets for adjacent successors, can be easily performed by examining the different matrices generated during local verification of a partition. It is recommended that anomalies be eliminated before proceeding to the next partition. If this is not done prior to verifying adjacent successor partitions, the same errors could manifest themselves as new errors in the successors. For example, if a contradiction is identified in a partition, paths (sub-paths) that originate from these contradictory attribute-values could also indicate contradictions in successive partitions, all of which may be due to the original anomaly.

## 4.3. Proof of Accuracy for the Modular Verification Process

We state and prove two important theorems that establish the validity of the modular verification process. The first states that our procedure is accurate for ordered polytree decompositions. The second asserts that no part of the information set can be dropped without compromising the accuracy of the verification procedure.

Theorem 1. If the partitions of a rule base form an ordered polytree, then the modular verification approach will accurately identify all of the anomalies in the rule base without identifying spurious anomalies.

Proof. We prove this by showing that the modular procedure identifies an anomaly if and only if such an anomaly exists in the rule base.

## Accuracy of Completeness Checks

(a) Dead ends. First, consider the situation where an anomaly of this kind exists in the rule base. This will happen when a node is not an antecedent (or part of an antecedent) of any rule, nor does it correspond to a global output. Consider what happens in the modular approach when the last partition (say, $\mathrm { { P _ { i } } ) }$ that includes that node is being examined (note there may either be only one partition that includes the node, or the node could be shared across several partitions). It is not shared by any adjacent successor partition, it is not a global output, nor does it appear as an antecedent in any rule in $\mathrm { P _ { i } } .$ Therefore, the local verification procedure will detect it is a dead end when examining $\mathrm { { P _ { i } } . }$

When a node is identified as a dead end in a partition by our approach, it must be because the node is not a global output, nor an antecedent of a rule in that partition, nor shared by any adjacent successor partition. Clearly, there cannot exist any path that includes the node and leads to a global output.

(b) Unreachable goals. This occurs when a node is not a conclusion of any rule, nor is it a global input. Consider what happens when the first partition (say, P<sub>j</sub>) that includes that node is being examined (of course, there may either be only one partition that includes the node, or the node could be shared across several partitions). It is not shared by any adjacent predecessor partition, so it cannot be a strictly local input. Because it is not a global input, the local verification process will detect it as an unreachable goal when examining $\mathrm { P _ { j } } .$

When a node is identified by our approach as an unreachable goal in a partition, it must be because the node is not a global input, nor a strictly local input, nor a conclusion of a rule in that partition. Clearly, there cannot be any path from global input nodes that reach the identified node.

## Accuracy of Consistency Checks

## (a) Contradiction

For notational convenience, and without loss of generality, we can assume that the two attribute-values v1 and v2 are mutually exclusive.

Case 1: U and v1, v2 are in the same partition $\mathrm { P _ { i } } .$ Let there exist conflicting paths from U to v1 and $\mathbf { v } 2 ,$ respectively. Because of the requirements specified for an ordered polytree, it is necessary that both paths lie entirely in the partition $\mathrm { P _ { i } } .$ Consider that one path did indeed span multiple partitions. If it spanned only one adjacent partition $\mathrm { P _ { j } } ,$ then it would not be possible to order $\mathrm { { P _ { i } } }$ and $\mathrm { P _ { j ^ { \prime } } }$ because there would exist subpaths that originated in $\mathrm { { P _ { i } } }$ and ended in $\mathrm { P _ { j } } ,$ and vice versa. If it spanned more than one other partition, then those partitions must be connected in such a manner that they form a cycle that violates the basic polytree requirement. Because the paths lie entirely in $\mathrm { P _ { i } } ,$ the local verification process would identify the contradiction (from corollary 2 in the appendix).

Now consider the situation where our verification process has detected conflicting paths from U to v1 and $\mathbf { v } 2 ,$ respectively. It follows from proposition 1 in the appendix that these paths do exist in that partition and, therefore, contradict each other.

Case 2: U is in partition $\mathrm { { P _ { i } } }$ and v1, v2 are in an adjacent partition $\mathrm { P _ { j } }$ . Let there exist conflicting paths from U to v1 and $\mathbf { v } 2 ,$ respectively. Since $\mathrm { { P _ { i } } }$ and $\mathrm { P _ { j } }$ are adjacent, all paths from $\mathrm { { P _ { i } } }$ to $\mathrm { P _ { j } }$ must pass through the set of shared attribute-values. Let X denote the set of shared attribute-values that appear in the path from U to v1, and let Y denote the set of shared attribute-values that appear in the path from U to v2 (note that X and Y need not be disjoint sets). Because every attribute-value in $X$ as well as in Y must be reachable from $U ,$ it follows that when verifying $\mathrm { P _ { i } } ,$ each such path would be identified (from proposition 1 in the appendix). Further, because all these attribute-values are shared by $\mathrm { { P _ { i } } }$ and $\mathrm { P _ { j ^ { \prime } } }$ when verifying $\mathrm { { P _ { i } } }$ a virtual hypernode $Z ~ ( = X \cup ~ Y )$ would be created consisting of all these attribute-values. When verifying $\mathrm { P _ { j ^ { \prime } } }$ the procedure would detect that both v1 and v2 are reached from $Z ,$ indicating contradiction.

Next, consider the situation where, during verifying $\mathrm { P _ { j ^ { \prime } } }$ the verification process has detected the existence of conflicting paths to v1 and v2. If the originating hypernode corresponds to the antecedent of a rule in partition $\mathrm { P _ { j ^ { \prime } } }$ then there exist conflicting paths that are entirely contained in $\mathrm { P _ { j } }$ Otherwise, the originating hypernode must be virtual (say W). The only way the hypernode would be formed is if there existed a hypernode in $\mathrm { { P _ { i } } }$ (say U) that reached every element of W. It follows that U can also reach v1 and $\mathbf { v } 2 ,$ , and therefore conflicting paths from U to v1 and $\mathbf { v } 2$ do exist.

Case 3: U is in Partition $\mathrm { { P _ { i } } }$ and v1, v2 are in a nonadjacent partition $\mathrm { P _ { j } } .$ Let $\mathrm { { P _ { i } } }$ and $\mathrm { P _ { j } }$ be connected through the set of ordered intermediate partitions $\mathrm { { P _ { a } , } }$ $\mathrm { P _ { b } , . . . , P _ { m } , }$ and there exist conflicting paths from U to v1 and $\mathbf { v } 2 ,$ respectively. Since the set of intermediate partitions must be unique, it follows that both the paths traverse through the same set of partitions. Let $X _ { \mathrm { r s } }$ denote the set of attribute-values that appear in the path from U to v1 and are shared by partitions P<sub>r</sub> and $\mathrm { P _ { s } }$ (where P<sub>r</sub> and $\mathrm { P _ { s } }$ refer to adjacent pairs of partitions that lie in the path from U to v1). Similarly, let $Y _ { \mathrm { r s } }$ denote the set of shared attribute-values that appear in the path from U to v2 and are shared by $\mathrm { P _ { r } }$ and $\mathrm { P _ { s } . }$ After partition $\mathrm { { P _ { i } } }$ is examined during verification, the virtual node $Z _ { \mathrm { i a } } ~ ( = X _ { \mathrm { i a } } \cup ~ Y _ { \mathrm { i a } } )$ will be formed because U reaches all of its elements. Subsequently, after examining $\mathrm { { P _ { a } , } }$ the virtual node $Z _ { \mathrm { a b } } ~ ( = X _ { \mathrm { a b } } \cup Y _ { \mathrm { a b } } )$ will be formed because $Z _ { \mathrm { i a } }$ reaches all of the elements of $Z _ { \mathbf { a b } } .$ Proceeding in this manner, the virtual node $Z _ { \mathrm { m j } } ( = X _ { \mathrm { m j } }$  $Y _ { \mathrm { m j } } )$ will be formed after examining $\mathrm { { P _ { m } } . }$ Finally, when $\mathrm { P _ { j } }$ is examined, the procedure would identify the paths from $Z _ { \mathrm { m j } }$ to both v1 and $\mathbf { v } 2 ,$ indicating contradiction.

Now, consider that conflicting paths to v1 and $\mathbf { v } 2$ are detected when verifying $\mathrm { P _ { j } } .$ If the originating hypernode corresponds to the antecedent of a rule in $\mathrm { P _ { j } }$ (i.e., the originating hypernode is “real”), then there exist conflicting paths that are entirely contained in Pj. Otherwise, the originating hypernode must be virtual (say $W _ { \mathrm { m j } } )$ . The only way the hypernode would be formed is if there existed a hypernode in $\mathrm { P _ { m } }$ that reached every element of $W _ { \mathrm { m j } } .$ If that hypernode is real, then there exists conflicting paths from that hypernode to v1 and v2. If it is virtual, then all of its elements can be reached by a hypernode in the predecessor partition. It follows by induction that there exists a real hypernode in one of the predecessors that reaches both v1 and v2.

## (b) Cycles

The requirements for an ordered polytree structure preclude the possibility of a partition being connected to itself through a set of intermediate partitions. As a result, cycles that span multiple partitions cannot exist. All cycles that exist must lie entirely in one partition. The verification procedure accurately detects such events (from corollaries 3a and 3b in the appendix).

The proof for redundancy checks is analogous to that for contradictions and, therefore is not provided. 

Theorem 2. The required information set is minimal for modular verification of ordered polytree decompositions.

Proof. To prove this theorem, we show that if any part of the information set is not considered during the modular verification process, then certain instances of anomalies will be undetectable, or anomalies would be indicated in a spurious manner.

The first part of the information set is the list of all preceding partitions that are adjacent and nodes shared with each such adjacent partition. Clearly, a positive identification of an unreachable goal can be made only if we know that the attribute-value is not reachable in a predecessor partition and, therefore, is not shared with such a partition.

The second part of the information set is the list of all succeeding partitions that are adjacent and nodes shared with each such adjacent partition. A dead end can be positively identified only if we know that the attribute-value is not an antecedent of a rule in a successor partition and, therefore, is not shared with such a partition.

The third part of the information set consists of the subsets of nodes—from the shared nodes in each predecessor partition—that are reached from the same hypernode (i.e., all virtual nodes from adjacent predecessor partitions). Identification of contradictory or redundant paths that span multiple partitions can be made only if this information is available during local checks (e.g., paths from the hypernode (a1,b1) to k1 and q1, respectively, in Figure 7). 

## 5. Identifying Ordered Polytree Structures

In the previous section, when discussing the modular verification approach, we have assumed that the partitioned set of rules conforms to an ordered polytree structure. It is possible that, in practice, the domain expert provides us with a set of partitions that do not form an ordered polytree. To take full advantage of the modular verification process, it should be possible to first verify that the partitions obtained do indeed form an ordered polytree. We have developed a metaverification procedure to identify whether a given decomposition scheme has the desired structure. The procedure checks to see if the partitions violate any of the three requirements for an ordered polytree. The first requirement (i.e., any two partitions being connected through a unique set of partitions) is checked in two stages. In the first stage (requirement 1a), we present a procedure to check for unique connections among mutually adjacent partitions. In the second stage (requirement 1b), a procedure to check for unique connections among nonadjacent partitions is presented. Subsequently, we present checks to verify the second and third requirements for an ordered polytree, respectively.

Requirement 1a. Unique connections among mutually adjacent partitions.

• Examine the nodes (attribute-values) that are shared by two or more partitions and create a list consisting of shared nodes and the partitions in which they appear.

• Inspect the list to see whether any group of partitions corresponding to a shared node is a proper subset of any other group of partitions corresponding to a different shared node. Such an occurrence indicates the existence of multiple connections among three or more mutually adjacent partitions, thereby violating the first polytree requirement.

For example, in Figure $^ { 3 , }$ consider node a1 contained in region II and node b2 contained in region I. Then (P1, P2) and (P1, P2, P3) would be the groups of partitions corresponding to shared nodes a1 and b2, respectively. Since (P1, P2) is a proper subset of (P1, P2, P3), this would indicate that partitions P1, P2, and P3 do not form a polytree.

Requirement 1b. Unique connections among nonadjacent partitions.

• Construct a simple undirected graph (that we call the connectivity graph) in which partitions are considered to be nodes and adjacencies are arcs between them (the adjacencies can be obtained from the adjacent partitions list as discussed in §4.2).

• Perform the following transformation for each occurrence of three or more mutually adjacent partitions that are considered valid after checking for requirement 1a. The transformation incorporates a new node in the connectivity graph that has arcs to the nodes corresponding to the mutually adjacent partitions. The original arcs between nodes corresponding to these partitions are dropped.

• Use the transformed graph to check for the existence of cycles in the following manner. Identify a spanning tree for the new graph using one of the wellknown techniques discussed in the literature (Horowitz and Sahni 1984). If there exists an arc in the graph that is not included in the spanning tree, it indicates the existence of a cycle. If cycles exist, it indicates that the partitions are connected through more than one set of intermediate partitions.

The following two examples illustrate how the above procedure correctly identifies multiple connections among nonadjacent partitions, while not flagging the existence of multiple adjacent partitions that are uniquely connected. Figure 10 illustrates the connectivity graph corresponding to the partitions shown in Figure 2(b). No transformations are needed for this example. A possible spanning tree could consist of arcs (P1, P2), (P1, P3), and (P2, P4). Because arc (P3, P4) is not part of the spanning tree, it indicates the existence of multiple connections between the nonadjacent Partitions P1 and P4.

Figure 10 Graph Showing Connectivity across Partitions in Figure 2(b)  
![](/api/attachments/6Q8DYXRN/fulltext/images/50602b5966db82a7b9c9683cf7814abd02310c371d414e6c93e07c07e7d9c121.jpg)

For the second example, consider the three partitions in Figure 3 to be uniquely connected (i.e., no nodes in regions II, III, and IV, and therefore requirement 1a is satisfied). Figure 11(a) shows the corresponding connectivity graph before transformation, and Figure 11(b) is the graph obtained after transformation, with P the new node added to the graph. The transformation allows us to correctly recognize the fact that the three partitions are acyclic and therefore uniquely connected.

## Requirement 2. Existence of valid ordering.

• Identify the adjacencies across partitions and the corresponding sets of shared attribute-values based on the procedure stated in §4.2 (stage 1).

• Perform the following check for each pair of adjacent partitions: For each partition, determine whether there exists a rule with a shared node (between these two adjacent partitions) as part of its antecedent, as well as a rule with a shared node as its conclusion. The adjacent partitions cannot be ordered only if such rules exist in both the partitions.

Consider, for example, partitions P1 and P2 shown in Figure 5. These partitions share nodes c1 and d1. For each partition, there exists a rule with one of these shared nodes as the antecedent as well as a rule with one of these shared nodes as the conclusion. This indicates that a valid ordering is not possible between P1 and P2.

Requirement 3. All mutually exclusive attributevalues in the same partition.

• For each attribute-value in the mutual exclusion list and every partition where the attribute-value appears, check whether all nodes corresponding to the

Figure 11 Connectivity Graph Before and After Transformation for Partitions in Figure 3

![](/api/attachments/6Q8DYXRN/fulltext/images/b0a00b13517629bf4a0bb36ea2f7b1ce44e8793f25dde7ac43485d07d4075c5c.jpg)  
(a) before transformation

![](/api/attachments/6Q8DYXRN/fulltext/images/a6961cb5a586ea082250b9689c59d21d1107ea1c098adcdf4ca12179edca8ea9.jpg)  
(b) after transformation

corresponding mutually exclusive attribute-values also appear in all of those partitions.

For example, in Figure 3, if node a1 is in partition P1 but not in P2 or P3, then all attribute-values that are mutually exclusive to a1 must be in P1 as well. Similarly, if a1 is in region I (i.e., shared by P1, P2, and P3), then all attribute-values that are mutually exclusive to a1 must also be in region I.

In some situations, domain experts may find it difficult to provide partitions. The requirements for polytree structures provide useful guidelines to help the experts in those situations. The metaverification procedure presented above helps to quickly identify undesirable structures and can be used as a support tool during the elicitation process. Of course, the experts are responsible for revising the partitions to get to a reasonably ordered polytree structure, which may take considerable effort. Based on the nature of violations to the ordered polytree structure identified by the metaverification process, experts can better assess what kinds of revisions would lead to desirable structures. An interesting issue for future research is to develop techniques that could help automate the identification of reasonable ordered polytree structures from the rules themselves.

## 6. Rule Base Modification and Computational Efficiency

The modular verification approach is particularly beneficial for applications where the rule base evolves over time, which is often true for large rule bases. We discuss how the procedure can take advantage of the decomposition when performing verifications under such circumstances. We then show how the modular verification procedure leads to significant improvements in computational efficiencies as compared to a traditional approach.

## 6.1. Rule Base Modification

Usually, the evolution process is incremental, requiring only a few rules to be added, deleted, or modified. However, without the use of partitions, it becomes necessary to reexamine the entire rule base to ensure that the rule base remains error-free after the changes are made. In the modular approach, when rules in a partition (called the target partition) are modified, the verification process needs to examine the target partition and, if necessary, those partitions adjacent to the target partition that may be affected as a result of the changes. The verification process for the target partition is as described in §4.2. If one or more adjacent partitions need further examination, then partitions adjacent to them (i.e., partitions once removed from the target partition) may also need to be examined. An attractive feature of the modular verification approach is that it is easy to determine whether adjacent partitions may be affected or not by suitably revising the information set to reflect the changes in the rule base.

Because modifying an existing rule is logically equivalent to deleting that rule and adding a new one, we restrict our discussion to how additions and deletions of rules lead to revisions of the information set. When a rule is added to a partition, it could affect the integrity of the adjacent partition(s) if the set of virtual hypernodes is affected. When adding new rules to a partition results in cycles, dead ends, or unreachable goals (within that partition), these are detected during local verification of that partition. If new virtual hypernodes are formed across nodes shared with a succeeding adjacent partition, then that partition must be examined as well. This helps to identify whether the addition of rules has led to conflicts or potential redundancies that span across multiple partitions. Adding new rules could increase the size of matrices used for verification by adding new rows and columns. As discussed in §6.2, the worst-case computational effort required for performing verification is of polynomial complexity in the number of rules. Analogous to other verification techniques, the computational effort needed may increase (polynomially) when rules are added. Of course, if adding new rules does not lead to additional rows and columns in the adjacency matrix, then the computational effort remains unchanged.

When a rule is deleted from a partition, it could affect adjacent partitions if either (i) one or more of its conditions is shared with a predecessor partition, (ii) its conclusion is shared with a succeeding partition, or (iii) the set of virtual hypernodes is affected. When the deletion of rules leads to a node no longer being shared with a preceding adjacent partition, then that node becomes a dead end in the preceding partition. At the same time, nodes in the target partition may also become unreachable; of course, they are identified in the local verification process. When the deletion of rules leads to a node no longer being shared with a succeeding adjacent partition, then that node becomes a dead end in the target partition, with the added possibility of creating unreachable goals in the successor. When the deletion of rules leads to revising the set of shared virtual hypernodes with a succeeding partition, there is no immediate danger of conflicts or redundant paths being newly created. Nevertheless, it is important to reflect the changes in the set of shared virtual hypernodes, as future modifications could lead to spurious observations of conflicting or redundant paths if the revision is not recorded.

It is indeed possible that changes to rules in one partition of the rule base lead to performing verification checks for all other partitions because of cascading modifications of information sets across adjacent partitions. However, that happens when potential conflicting or redundant paths span the entire set of partitions. When the potential redundancies span a small set of partitions, the information set enables us to identify the relevant partitions easily, and therefore not spend resources in examining other partitions. When substantial changes are being made to a rule base, it is possible that several partitions may have to be merged or otherwise redefined. Even in those situations, the revised partitions can be examined locally, and a new information set derived from them to determine if adjacent partitions need verification.

## 6.2. Computational Efficiencies Achieved Through Modular Verification

The computational complexity of the directed hypergraph technique is of the same order as that of other graph-based techniques, and is shown to be $O ( m n ^ { 3 } \mathrm { ~ + ~ }$ $\bar { m } n ^ { 2 } r ^ { 2 } )$ where $m , n ,$ and r are defined as follows (details of the derivation are provided in Ramaswamy et al. (1997).

m: the length of the longest chain of rules (length of the longest inference path);

n: the number of rules in the rule base; and

r: the maximum number of attribute-value pairs in any hypernode.

The ability to perform verification in a modular fashion leads to considerable improvement in the computational effort required for verification. Consider the situation where a rule base has been decomposed into p partitions, where the number of rules in the ith partition is $n _ { i } .$ It follows that the computational complexity of verifying the ith partition is no worse than $O ( m n _ { i } ^ { 3 } \ + \ m n _ { i } ^ { 2 } r ^ { 2 } )$ This assumes that the length of the. longest chain of rules in the partition is the same as the entire rule base, whereas in reality it could be much less. Even considering this worst-case scenario, the overall computational complexity for modular verification is given by $\Sigma _ { i = 1 , p } \ O ( m n _ { i } ^ { 3 } + m n _ { i } ^ { 2 } r ^ { 2 } )$ which is of , the order $O ( p m n _ { i } ^ { 3 } \ + \ p m n _ { i } ^ { 2 } r ^ { 2 } )$ If the partitions are of . approximately equal size, we have $n _ { i } \cong n / p$ . Then, the overall computational complexity is $\begin{array} { r } { \sum _ { i = 1 , p } O ( m n _ { i } ^ { 3 } \ + } \end{array}$ $m n _ { i } ^ { 2 } r ^ { 2 } ) = O ( p m n _ { i } ^ { 3 } + p m n _ { i } ^ { 2 } r ^ { 2 } ) = O ( m n ^ { 3 } / p ^ { 2 } + m n ^ { 2 } r ^ { 2 } / p ) [$ Large rule bases typically consist of several partitions, leading to significant improvements in computational complexity. In particular, if the first term in the complexity expression is dominant for a particular application, the efficiency improvements are markedly higher. As a related point, if verification resulting from incremental updates to the rule base is localized to one or a few partitions, the complexity of such verification processes is only $O ( m n ^ { 3 } / p ^ { 3 } + m n ^ { 2 } r ^ { 2 } / p ^ { 2 } )$

In some applications, it is possible that there are several different decomposition schemes that are considered feasible by the domain expert. Our analysis indicates that decompositions that lead to smaller partitions are preferred in general. Of course, it is important to verify that the suggested partitions do conform to an ordered polytree structure. This is achieved by the metaverification procedure discussed in §5.

## 7. Conclusion

We have examined the verification issues associated with large rule bases. We have identified a graphical framework, which we call an ordered polytree, for decomposing rule bases in a manner that enables the verification tasks to be performed in a modular fashion. We have also determined the nature of information that needs to be available for performing local checks to ensure accurate detection of anomalies. We have illustrated the modular verification process using examples, and have provided a formal proof of its accuracy. We have discussed a metaverification procedure that enables us to determine whether available decompositions do indeed satisfy the requirements for an ordered polytree structure. Finally, we have shown how the modular verification procedure leads to significant improvements in computational efficiencies, as compared to a traditional approach.

There are some similarities between polytree decompositions in the context of rule-based expert systems and stratified rules in the context of logic programming. In logic programming environments, sets of rules are stratified to allow certain types of negation in the presence of recursion (Apt et al. 1988, Baral et al. 1991). However, the stratification of rules is not identical to polytree decompositions, and it has some important limitations in the context of rule base verification. If one were to use stratification requirements for rules in the context of rule-based expert systems, the stratified sets will not allow us to detect redundancies in the rule base in a modular manner (using local checks to perform global verification) when inference paths span several partitions of rules. The same is true for contradictions that are caused by inference paths that span several partitions. Furthermore, in logic programming when a fact is not concluded given the existing rules, the negation of that fact is automatically inferred. This is not true in rule-based expert systems. As a result, stratified sets of rules would also allow existence of dead ends in the context of rule-based expert systems.

We have presented the decomposition scheme in the context of the verification process for knowledge bases, but the proposed framework also has some important implications regarding the overall design process. First, the framework can be used during the elicitation process itself to help the expert in decomposing complex problem environments. For such environments, the cognitive limitations of humans have often been identified as a critical bottleneck. The process of decomposing the knowledge base can lead to significantly reducing the cognitive requirements of experts, and thus facilitates the knowledge elicitation process. Second, the verification process may be integrated as part of a larger validation effort. The process of validation helps to identify rules that incorrectly represent the domain knowledge but do not directly lead to structural errors in the rule base. With the help of sample scenarios, it would be possible to examine the desired recommendations with the recommendations of the knowledge-based system. When these recommendations are not identical, the partitions would provide a logical framework that can help in identifying where the inference path arrived at by the system deviates from the intentions of the expert.

A related issue for large rule bases is to achieve efficiencies in performance at run time. Gulati and Tanniru (1993) propose a way to improve performance by prioritizing the rules in a manner that minimizes the expected number of rules that have to be examined by the inference engine to determine which rule is fired next. They show that by estimating the probability distribution of input parameters based on past usage, it is possible to determine a prioritization that, on average, results in faster execution time. The nature of decomposition of a rule base proposed in this research is perfectly amenable to rule prioritization, as well as the ordering of clauses in the premise. Furthermore, modularization allows the prioritization to be done at the partition level, thereby reducing the effort required to analyze the usage data for determining the probability distribution of input parameters. This can be significant when the probability distributions across different parameters are not independent. We are currently examining these issues in ongoing research.

Acknowledgments. The authors gratefully acknowledge the helpful comments and suggestions of the associate editor and three anonymous reviewers of Information Systems Research. The article has benefited greatly from their careful and thorough reviews.

## Appendix

As indicated in §2.3, the main idea behind the verification procedure is to accurately identify all feasible inference paths, taking care not to generate spurious paths. This is accomplished by performing certain operations on the adjacency matrix in a specified sequence. The important intermediate matrices generated during the verification process are:

B<sub>i</sub> Identifies all simple paths and strict hyperpaths of length  i ending in simple nodes.

C Identifies all simple paths and strict hyperpaths of length  i ending in simple as well as compound nodes.

D<sub>i</sub> Identifies only strict hyperpaths of length i ending in either simple or compound nodes.

E Identifies strict hyperpaths of length i that end in simple nodes. All of the above matrices are of the same size as the adjacency Matrix A. We note that the Matrix A<sup>i</sup> identifies all simple paths of length i. The important results are (proofs in Ramaswamy et al. 1997):

Proposition 1. If there are k distinct paths of length  i from a hypernode (simple or compound) U to a simple node v, then $B _ { i } I U , v \ : = \ : k$

Corollary 1. If B [U, v]  1, then there potentially exists a redundant rule, or a chain of redundant rules, from U to v in the rule base.

Corollary 2. If B [U, v] - 1, B [U, w] - 1, and v and w are mutually exclusive, then the rule sets that comprise P{U; v} and P{U; w} are definitely conflicting.

Corollary 3A. If an element A [U, V] - 1, and U - V, then the rules that comprise the path P{U; V} are circular.

Corollary 3B. If an element E [U, V} - 1, and U - V, then the rules that comprise the path(s) P{U; V] are circular.

Proposition 2. If every element of a row in Matrix A is zero, the row does not correspond to a goal variable, and the corresponding node is not a subset of a compound node, then it indicates a dead end.

Proposition 3. If every element of a column in matrix A is zero, the column corresponds to a simple node, and the column does not correspond to an input variable, then it indicates an unreachable goal.

Conflicts and potential redundancies are identified by examining matrix B<sub>i</sub> (follows from Corollaries 2 and 1, respectively). Cycles are identified by examining Matrices A<sup>i</sup> and E (follows from Corollaries 3a and 3b). Dead ends and unreachable goals are identified by examining matrix A (follows from Propositions 2 and 3, respectively). The presence of cycles can lead to paths of infinite length in the rule base. Therefore, it is recommended that all cycles be eliminated as early in the verification process as possible.

Figure 12 The Adjacency Matrix A for Rules 1–7 Shown in Figure 1.

<table><tr><td></td><td>a1</td><td>b1, c1</td><td>d1</td><td>e1</td><td>f1</td><td>d1, e1</td><td>e1, f1</td><td>g1</td><td>h1</td><td>h2</td></tr><tr><td>a1</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>b1, c1</td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>d1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>e1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>f1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td></tr><tr><td>d1, e1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td></tr><tr><td>e1, f1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td></tr><tr><td>g1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>h1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>h2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The adjacency matrix A for the rules in Figure 1 is shown in Figure 12. In this matrix, all simple paths of length 1 (established by the rules themselves) are indicated.

In this example, the length of the longest inference path is 2. Therefore, matrix ${ \bf B } _ { 2 }$ identifies all feasible paths that end in simple nodes. After performing the necessary operations, we obtain matrix $\mathbf { B } _ { 2 }$ shown in Figure 13 (we note that intermediate matrices $\mathbf { B } _ { 1 } , \mathbf { C } _ { 1 } ,$ $\mathbf { D } _ { 1 } , \mathbf { E } _ { 1 } ,$ and ${ \bf A } ^ { 2 }$ are constructed to obtain $\mathbf { B } _ { 2 } ;$ for the sake of brevity the intermediate matrices are not shown). New paths established in $\mathbf { B } _ { 2 }$ (indicated in bold lettering) are: (b1, c1) to g1, h1, and h2; (d1, e1) to h2; and (e1, f1) to h1 and h2. Because there are paths from (b1, c1) to both h1 and h2, this indicates a conflict in the rule base. Indeed, on examining the original rules (in §2.3), we find that when the likelihood of technical success is high and the likelihood of commercial success is high, the system will conclude that more personnel be allocated (through rules 3 and 6), as well as more personnel be not allocated (through rules 2 and 7).

Figure 13 Matrix $\mathsf { B } _ { 2 }$ for Rules 1–7 in Figure 1.

<table><tr><td></td><td>a1</td><td>b1, c1</td><td>d1</td><td>e1</td><td>f1</td><td>d1, e1</td><td>e1, f1</td><td>g1</td><td>h1</td><td>h2</td></tr><tr><td>a1</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>b1, c1</td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td>1</td><td>1</td><td>1</td></tr><tr><td>d1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>e1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>f1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td></tr><tr><td>d1, e1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td></tr><tr><td>e1, f1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td></tr><tr><td>g1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>h1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>h2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## References

Agarwal, R., M. R. Tanniru. 1992. A Petri-Net based approach for verifying the integrity of production systems. Internat. J. Man Machine Systems 36 447–468.

, ——. 1992b. A structured methodology for developing production systems. Decision Support Systems 8 483–499.

Apt, K. R., H. A. Blair, A. Walker. 1988. Towards a theory of declarative knowledge. J. Minker, ed. Foundations of Deductive Databases and Logic Programming. Morgan Kaufmann, Los Altos, CA. 89–148.

Awad, E. M. 1996. Building Expert Systems: Principles, Procedures, and Applications. West Publishing Company, St. Paul, MN.

Balachandra, R., A. J. Raelin. 1980. How to decide when to abandon a project. Res. Management 23(7) 81–93.

Baral, C., K. Sarit, J. Minker. 1991. Combining multiple knowledge bases. IEEE Trans. Knowledge and Data Engrg. 3(2) 208–220.

Botten, N., A. Kusiak, T. Raz. 1988. Knowledge bases: Integration, verification, and partitioning. Eur. J. Oper. Res. 42 111–128.

Coenen, F., P. Dunne. 1997. Verification and validation of rulebases

using a binary encoded incidence matrix technique. Proc. 4th Eur. Sympos. Validation and Verification of Knowledge Based Systems, Leuven, Belgium, 43–54.

Conte, S., H. Dunsmore, V. Shen. 1986. Software Engineering Metrics and Models. Benjamin/Cummings Publishing, New York.

Ginsberg, A. 1988. Knowledge-Base reduction: A new approach to checking knowledge bases for inconsistency and redundancy. Proc. National Conf. Artificial Intelligence, St. Paul, MN, 589–595.

Goh, C., M. Tsukamoto, S. Nishio. 1996. Knowledge discovery in deductive databases with large deduction results: The first step. IEEE Trans. Knowledge and Data Engrg. 8(6) 952–956.

Gulati, D., M. R. Tanniru. 1993. A model-based approach to investigate performance improvements in rule-based expert systems. Decision Sci. 24(1) 42–59.

Hicks, R. C. 1995. Verification properties of knowledge dictionaries for expert systems. Heuristics: The J. Intelligent Tech. 8(4) 61–81.

Hogarth, R. 1987. Judgement and Choice. John Wiley, Chichester, New York.

Horowitz, E., S. Sahni. 1984. Fundamentals of Computer Algorithms. Computer Science Press, Rockville, MD.

Hou, W. 1996. Extraction and applications of statistical relationships in relational databases. IEEE Trans. Knowledge and Data Engrg. 8(6) 939–945.

Huang, Y., S. Lin. 1996. An efficient inductive learning method for object-oriented database using attribute entropy. IEEE Trans. Knowledge and Data Engrg. 8(6) 946–951.

Jacob, R., J. Froscher. 1986. Developing a software engineering methodology for rule-based systems. Proc. Fall Joint Comput. Conf. Dallas, TX. 179–183.

Lloyd, J. W. 1984. Foundations of Logic Programming. Springer-Verlag, Germany.

Murrell, S., R. Plant. 1996. On the validation and verification of production systems: A graph reduction approach. Internat. J. Human-Comput. Stud. 44(2) 127–144.

Nazareth, D. L. 1989. Issues in the verification of knowledge in rulebased systems. Internat. J. Man-Machine Stud. 30 255–271.

——. 1993. Investigating the applicability of Petri nets for rule-based system verification. IEEE Trans. Knowledge and Data Engrg. 4(3) 402–415.

——, M. H. Kennedy. 1991. Verification of rule-based knowledge using directed graphs. Knowledge Acquisition 3 339–360.

O’Leary, D. 1996. The relationship between errors and size in knowledge-based systems. Internat. J. Human-Computer Stud. 44(2) 171–185.

Plant, R., A. D. Preece. 1996. Editorial: Special issue on verification and validation. Internat. J. Human-Comput. Stud. 44(2) 123–125.

Pearl, J. 1988. Probabilistic Reasoning in Intelligent Systems. Morgan Kauffmann, San Mateo, CA.

Pederson, K. 1989. Well-structured knowledge bases. AI Expert. 4 44– 55.

Preece, A. D. 1993. A new approach to detecting missing knowledge in expert system rule-bases. Internat. J. Man-Machine Stud. 38 661–688.

Ramaswamy, M., S. Sarkar, Y. Chen. 1997. Using directed hypergraphs to verify rule-based expert systems. IEEE Trans Knowledge and Data Engrg. 9(2) 221–237.

Sarkar, S., M. Ramaswamy, Y. Chen. 1995. A hypergraph-based tool to support verification and validation of rule-based expert systems. Heuristics: The J. Knowledge Engrg. and Techn. 8(4) 61–81.

Segev, A., L. Z. Zhao. 1994. Rule management in expert database systems. Management Sci. 40(6) 685–707.

Soloway, E., J. Bachant, L. Z. Jensen. 1987. Assessing the maintainability of XCON-in-RIME: Coping with the problems of a very large rule base. Proc. the AAAI-87. Morgan Kaufman, Los Altos, CA.

Trice, A., R. Davis. 1993. Heuristics for reconciling independent knowledge bases. Inform. Systems Res. 4(3) 262–288.

Wand, Y., R. Weber. 1990. An ontological model of an information system. IEEE Trans. Software Engrg. 16(11) 1282–1292.

Michael Shaw, Associate Editor. This paper was received on March 20, 1998, and was with the authors 6 months for 2 revisions.
