---
otero_id: 10000
otero_key: "4XMGM65V"
title: "Formal correctness of supply chain design"
authors: "Joerg Leukel; Vijayan Sugumaran"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.06.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Joerg Leukel <sup>a</sup>, Vijayan Sugumaran <sup>b,c,</sup>⁎

<sup>a</sup> Department of Information Systems 2, University of Hohenheim, Schwerzstr. 35, 70599 Stuttgart, Germany

<sup>b</sup> School of Business Administration, Oakland University, 306 Elliott Hall, Rochester, MI 48309, USA

<sup>c</sup> Department of Global Service Management, Sogang Business School, Sogang University, Seoul 121-742, Republic of Korea

## a r t i c l e i n f o

Article history: Received 1 May 2012 Received in revised form 25 October 2012 Accepted 13 June 2013 Available online 20 June 2013

Keywords: Supply chain management Supply chain design Model veri<sup>fi</sup>cation SCOR

## a b s t r a c t

Many companies use supply chain models for designing the <sup>fl</sup>ow of goods and services from their suppliers all the way up to the <sup>fi</sup>nal customers. Over the past 15 years, the Supply Chain Operations Reference Model (SCOR) has become a widespread modeling technique for designing such supply chains and sharing design information with supply chain stakeholders. However, neither the syntax nor the semantics of SCOR are well de<sup>fi</sup>ned. This limitation has important consequences for its usage: Supply chain models may be ambiguous and their correctness cannot be veri<sup>fi</sup>ed. We address this problem by mapping SCOR supply chains onto graphs and formalize the semantics of SCOR. The mapping is driven by constructs from the supply chain management literature. The proposed artifact is a supply chain grammar, which we apply to a set of SCOR models taken from industry sources. We show the grammar's usefulness by verifying the correctness of these models using analytical techniques.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Supply chain design is a critical business problem. For many industries, supply chains have become an important focus for competitive advantage. With the increasing global division of labor, the performance of a single company depends more and more on its ability to maintain effective and ef<sup>fi</sup>cient relationships with its suppliers and customers. Thus, managerial decisions are moving from an organizational scale to a supply chain scale [20]. Supply chain design is the task of determining the basic, long-term structure of the supply chain by de<sup>fi</sup>ning its elements, objectives, locations, and key organizations [37]. The role of Information Systems (IS) to support this task has recently been the subject of inquiry.

In general, supply chain design faces two dif<sup>fi</sup>culties. First, the design space contains a vast number of alternatives, which makes it hard for designers to evaluate and select the best alternative. Second, designing a supply chain incorporates stakeholders from the supply and demand side, which requires sharing and understanding design information by various parties. These two dif<sup>fi</sup>culties can be mitigated through reference models that: (1) restrict the design space by providing core constructs that can be con<sup>fi</sup>gured under certain design constraints, and (2) de<sup>fi</sup>ne a common terminology for sharing designs across organizations. Supply chain management (SCM) has adopted this idea in the form of the Supply Chain Operations Reference Model (SCOR) [34,35]. Over the past 15 years, SCOR has become a widespread modeling technique for supply chain design. It is promoted by a stellar group of <sup>fi</sup>rms from various industries and can be regarded as a best practice. Research has made use of SCOR for designing both descriptive and analytical methods for various supply chain problems, in particular, performance management [23,41], con<sup>fi</sup>guration [32], and market-based balancing of demand and supply [27].

The main disadvantage of SCOR is that neither its syntax nor its semantics is well de<sup>fi</sup>ned. A formal speci<sup>fi</sup>cation of SCOR in the form of a grammar does not exist. The modeling technique is only described in a handbook [36], which provides a reference to model elements with simple example models that don't provide much explanation. The lack of well-de<sup>fi</sup>ned syntax and semantics has severe consequences. If SCOR users interpret the informal description of the technique in different ways, the supply chain models built using SCOR will become ambiguous and potentially error-prone. This practice may result in syntactically incorrect models that cannot be used by any third party. Software vendors who provide SCOR modeling tools are in danger of implementing the technique incorrectly. Ultimately, the two objectives of reducing the design space and enabling cross-organizational information sharing cannot be met.

Incorrect supply chain models affect the managerial use of these models. We brie<sup>fl</sup>y discuss the problems resulting from incorrect models by referring to the three use case of the SCOR technique [36]:

− Supply chain description aims at providing an unambiguous description of an actual or planned supply chain for parties that are interested or involved in this supply chain. Incorrect design manifests in con<sup>fi</sup>guring the constructs of the SCOR technique falsely, for example, invalid linkage of constructs or missing constructs. If these de<sup>fi</sup>cits cannot be detected and repaired, the description is only understandable by the designer and the individuals that share the designer's interpretation. Hence, the model is limited to a small group and does not extend to all the supply chain stakeholders.

− Supply chain measurement is concerned with measuring the performance of connected activities and the entire supply chain. For this purpose, the technique provides a standard set of metrics (e.g. cycle time, cost, <sup>fl</sup>exibility) and standard formulae for analyses, which rely on correct models as outlined in the supply chain description. For incorrect models, the aggregation process would yield either incorrect or no results. Hence, the supply chain performance cannot be correctly measured.

− Supply chain evaluation is the task of assessing different designs and selecting the best con<sup>fi</sup>guration with regard to certain criteria. These criteria include metrics as de<sup>fi</sup>ned by the SCOR technique. Evaluation is an iterative process of design (i.e., creating alternative models) and metrics-based measurement. If the measurement yields incorrect or no result for at least one model, then the evaluation will also become incorrect (by comparing con<sup>fi</sup>gurations that differ due to the interpretation of the technique) or incomplete and not feasible (due to missing data).

Adding a formal speci<sup>fi</sup>cation to SCOR is non-trivial, unless we are able to get this information from SCOR's inventors or at least articulate their interpretation explicitly. However, SCOR was invented by a dynamic group of individuals who worked over a long period in a more or less informal organization. Hence, it is dif<sup>fi</sup>cult to elicit this information from this group. What we need is a grammar that consists of a lexicon for supply chain design and a <sup>fi</sup>nite set of rules that specify allowable combinations of lexicon elements. There are two basic approaches for de<sup>fi</sup>ning this grammar: deduction and induction. Grammar deduction de<sup>fi</sup>nes lexicon and rules by analyzing relevant theories and axioms. Grammar induction learns lexicon and rules from a set of observations — here, the SCOR supply chain models. The latter's precision, however, is negatively affected by the share of incorrect models in the set of observations.

Current solutions fall into the category of grammar deduction. However, no research endeavor has yet used the existing body of knowledge from SCM research for deduction. Instead, the main source of deduction is the informal description of SCOR, which is then interpreted by the respective researcher. The disadvantage of these approaches is that the deduction is not made explicit to allow for reproducibility.

We address the problem of the lack of explicit de<sup>fi</sup>nition of SCOR by mapping SCOR supply chains onto directed graphs and formalizing the syntax and semantics. The mapping is a deduction process supported by the constructs from the SCM literature. These constructs enable us to enrich SCOR with additional constraints that have a strong theoretical underpinning. Thus, the objectives of this research are to: (1) develop the syntax and semantics of SCOR in the form of a supply chain grammar that allows for assessing the correctness of supply chain design, and (2) apply this artifact to a set of SCOR models to demonstrate its usefulness for model veri<sup>fi</sup>- cation. The contributions of this research are the formal speci<sup>fi</sup>cation (grammar) of SCOR and analysis techniques for SCOR-based supply chain design.

The remainder of this paper is organized as follows. In Section 2, we brie<sup>fl</sup>y introduce the SCOR technique and provide preliminary notions that will be used for enrichment by grammar deduction. In Section 3, we discuss the approaches to the correctness of supply chain design and compare our work with the relevant literature. In Section 4, we derive speci<sup>fi</sup>c constraints on supply chain design from the SCM literature and provide the grammar. In Section 5, we demonstrate the usefulness of our proposed grammar in verifying the correctness of SCOR models taken from industry sources. Section 6 concludes the paper and outlines some of our future work.

## 2. Preliminaries

## 2.1. SCOR technique

SCOR consists of an intuitive graphical supply chain description language and a set of supply chain metrics that can be associated with supply chain activities. The graphical language is targeted for the business audience, who uses this language for effective communication of supply chain structures at different levels of abstraction. At the strategic level, SCOR provides a modeling technique for primary product <sup>fl</sup>ows; the resulting model is called a SCOR thread diagram. The designer can then add details to these diagrams by incorporating plan processes (information <sup>fl</sup>ow), secondary product <sup>fl</sup>ows (return of products to the supplier), and describing more <sup>fi</sup>ne-grained activities associated with the primary product <sup>fl</sup>ow, e.g., receiving orders, packaging, and routing shipments. These activities can be con<sup>fi</sup>gured from a reference set of several hundred so called process elements. In the following, we consider only primary product <sup>fl</sup>ows, since this level represents the strategic con<sup>fi</sup>guration of supply chains.

A thread diagram shows the <sup>fl</sup>ow of products (including tangible goods and services) as a chain of linked activities. An example diagram is shown in Fig. 1. The technique provides the following elements:

− Process is an activity of either sourcing, manufacturing, or delivering a product (symbol: arrow-shaped rectangle). The symbols can have different colors to signify the type of activity; however, the color scheme is not precisely de<sup>fi</sup>ned in the SCOR technique.

− Product flow represents the transfer of a product from one process to another (symbol: arrow).

![](/api/attachments/4XMGM65V/fulltext/images/066c751255afa3c57b0168d7c2f9d2f1512cd54c7b38098d8861bc4a4d8cbd37.jpg)  
Fig. 1. Example SCOR thread diagram.

− Actor is an organizational entity that executes one or more processes (symbol: label of process).

− Tier re<sup>fl</sup>ects the level of involvement of actors when considering the entire supply chain. Tiers arrange actors from left to right (symbol: vertical swim lane).

If a tier contains only one actor, then it is suf<sup>fi</sup>cient to add the actor label to only one process (instead of labeling all the processes). For example, in Fig. 1, the M3 process as well as all the other processes in this tier are executed by the “Engine Manufacturer” actor.

SCOR differentiates processes for primary product <sup>fl</sup>ows by the degree of customization (product speci<sup>fi</sup>city): (1) stocked products, (2) make-to-order products being manufactured for a speci<sup>fi</sup>c customer order, and (3) engineer-to-order products being designed and manufactured to a speci<sup>fi</sup>c customer requirement. This differentiation is then applied to all the processes of sourcing (S), manufacturing (M), and delivering (D) products. Each process is thus encoded by a 2-character code, which denotes the process category, e.g., D2 for delivery of make-to-order products. This differentiation is part of SCOR since 1997 (version 2.0) and was slightly modi<sup>fi</sup>ed in 2003 (version 6.0) by including the D4 process category for the delivery of retail products. This product speci<sup>fi</sup>city exists only for delivery processes.

## 2.2. Preliminary notions

We de<sup>fi</sup>ne the basic notions that formally capture the main elements of the SCOR technique for thread diagrams (as introduced in Section 2.1). These notions will serve as the baseline for adding constraints on correct diagrams in the succeeding sections. They are minimal in the sense that we avoid making assumptions about the technique that may not be justi<sup>fi</sup>ed by supply chain theory.

## De<sup>fi</sup>nition 1a. SCOR thread diagram

A SCOR thread diagram is a directed graph $T D = ( P , F , A , T , P C , P A , P T )$ where:

− P is a <sup>fi</sup>nite set of processes $p \in P ,$

− F is a <sup>fi</sup>nite set of product <sup>fl</sup>ows $f \in F$ with $F \subseteq P \times P ,$

− A is a <sup>fi</sup>nite set of actors $a \in A ,$

− T is a <sup>fi</sup>nite set of tiers $t \in T ,$

− PC is a function which maps each process onto a process category with $P C : P  \{ S 1 , S 2 , S 3 , M 1 , M 2 , M 3 , D 1 , D 2 , D 3 , D 4 \} ,$

− PA is a function which maps each process onto an actor with PA: $P  A ,$

− PT is a function which maps each process onto a tier with $P T { \mathrm { : } } P \to T .$

Using this de<sup>fi</sup>nition, the thread diagram shown in Fig. 1 can be formally de<sup>fi</sup>ned by all components of TD. For instance, the diagram contains eleven processes, which must be numbered $\mathsf { e . g . } , P = \{ p 1 , p 2 , . . . , p 1 1 \}$ Each arrow in the diagram denotes a product <sup>fl</sup>ow, e.g., $F = \{ ( p 1 , p 2 )$ $( p 3 , p 4 ) _ { \cdots } \}$ . The processes p1 and p3 belong to the process category D1, thus $P C = \{ ( p 1  D 1 ) , ( p 3  D 1 ) , . . \}$ , and are contained in the Supplier tier, thus $P T = \{ ( p 1  S u p p l i e r ) , ( p 3  S u p p l i e r ) , . . . \}$

## 3. Related work

## 3.1. Supply chain design

Two dimensions are constituent to the task of supply chain design. The process dimension relates to answering the question which activities must be performed by the designer in what order to produce the supply chain model. SCM research yields a plethora of analytical models and optimization methods [6,37]. The result dimension relates to the constructs, i.e., the conceptual vocabulary of the problem domain, and the formalisms used for articulating these constructs. Correctness of supply chain design is the ultimate concern of the result dimension. The SCOR technique addresses the result dimension.

The SCOR technique has been documented in a handbook [36], which provides de<sup>fi</sup>nitions of all the aforementioned elements. The handbook, however, falls short of providing a formal speci<sup>fi</sup>cation in the form of a grammar that is unambiguous and free of interpretation. It also provides very little information on how to link processes under consideration for process categories, actors, and tiers. The lack of a formal grammar has led to the conclusion that SCOR is less useful for analyzing supply chains through quantitative means [4,19]. Arns et al. argue for reducing the role of SCOR to description, whereas all model analysis tasks would require a more capable language providing a well-de<sup>fi</sup>ned execution semantics [4].

The literature yields several approaches for amending SCOR with a grammar. These approaches differ in the speci<sup>fi</sup>cation language used and the way they augment the SCOR technique.

Becker et al. [7] choose the Entity-Relationship-Model (ERM) for specifying a meta-model of SCOR. The rationale is that the ERM is adequate for capturing the SCOR constructs as well as the resulting meta-model and can easily be transformed into a database schema for model storage and retrieval. An interesting aspect of the proposed meta-model is the process category condition, which enforces that processes of a certain category must be connected with processes of another category (e.g., “make-to-stock” is succeeded by “deliver make-to-stock”). These conditions may help in assessing the correctness of supply chain designs, though they have not been made explicit, but were illustrated by an example only. Unfortunately, this research provides little information on how the meta-model was constructed. The authors try to provide convincing arguments for the meta-model and report about a prototype implementation; however, the prototype is not concerned with correctness of supply chain designs.

Millet et al. [26] propose a set of possible relationships between process categories denoted as rules. They assume that designing a supply chain implicates a certain body of rules. The explication process for these rules is, however, not described. The rules are not formally speci<sup>fi</sup>ed. In addition, the rule set is at best incomplete, since it misses product <sup>fl</sup>ows between different Make processes.

SCOntology is an ontological approach to formalizing the SCOR technique [15]. The rationale for using the Web Ontology Language (OWL) [38] is that OWL provides more expressiveness for de<sup>fi</sup>ning concepts and their interrelations than ERM. The scope of the proposed SCOR ontology is de<sup>fi</sup>ned by the so called competency questions. Insofar as these competency questions are concerned, a justi<sup>fi</sup>cation for them is not provided by these authors. In addition, the ontology is described using graphical means only, and thus lacks axioms. A brief case study is supplied to demonstrate the validity of the proposal.

The ontological approach by Sakka et al. [33] does not interpret the textual descriptions contained in the SCOR handbook, but starts with the meta-model that is implemented by the software tool ARIS/SCOR. This meta-model, which is speci<sup>fi</sup>ed in ERM, is then mapped onto an OWL ontology. The advantage is that this approach preserves all constructs and rules contained in the baseline meta-model. However, Sakka et al. admit that the designers of ARIS/SCOR were interpreting the SCOR handbook and thus made assumptions, which are unknown to the tool user.

The most comprehensive ontological approach is SCOR-FULL [42], which goes beyond SCOR thread diagrams by including SCOR metrics and input/output information. This ontology is aimed at the semantic interoperability of supply chain designs, without paying attention to correctness. Similar to [15], the rationale of this ontology is limited to answering an initial set of competency questions.

Our approach differs from existing research as follows. First, by grounding the grammar deduction on constructs and rules of the SCM literature, we aim at reducing the risk of interpreting the SCOR handbook in a subjective way. This risk may lead to a grammar that contradicts the insights from SCM research. Second, our research is informed by the use of ontology languages, but the proposed grammar is independent from the usage of a particular ontology language. Third, we address the formal correctness of supply chain design and aim at providing speci<sup>fi</sup>c means for assessing this property.

## 3.2. Business process management

Much progress has been made on developing methodologies for assessing and preserving the correctness of business process models. Since supply chain design also describes the business activities carried out (those for supplying products from suppliers to the <sup>fi</sup>nal customers), we review contributions from the business process management (BPM) literature that may be bene<sup>fi</sup>cial for supply chain design.

Process verification determines whether a process model complies with a speci<sup>fi</sup>ed structure and behavior. Veri<sup>fi</sup>cation depends foremost on the existence of formal semantics of the process description language used. Many widely used languages for business process modeling lack formal semantics, e.g., Event-driven Process Chains (EPC) [1] and the Business Process Modeling Notation (BPMN) [12]. Therefore, BPM research has investigated their mapping to more powerful modeling techniques, which also supply analysis techniques for correctness properties. Of particular signi<sup>fi</sup>cance are the works that adopt analysis techniques using Petri-nets. Mendling et al. [24] propose a Petri-net approach for detecting errors in EPCs and apply it to a set of real-world EPCs taken from the SAP Reference Model. They show that these EPCs are error-prone, because the model designers did not conform to the EPC semantics.

Supply chain design shows similarities to business process modeling. However, we need to be aware of important differences between product <sup>fl</sup>ow and control <sup>fl</sup>ow. The SCOR technique does not make the semantics of the product <sup>fl</sup>ow construct explicit. For instance, let us consider the diagram given in Fig. 1. The process of category M3 has three ingoing arcs (sourcing) and two outgoing arcs (delivery). Does it mean that this process transforms all three ingoing products into the two outgoing products? Or can this process be executed if at least one ingoing arc is activated? The answer cannot be given, because the execution semantics is unclear. We need to keep in mind that supply chain design is concerned with de<sup>fi</sup>ning the structure of supply chains, not their behavior. For instance, SCOR lacks logical connectors, which are common in control <sup>fl</sup>ow descriptions.

Arns et al. [4] combine the SCOR technique with a business process language as follows: They propose using a custom notation called ProC/B; the advantage is that ProC/B models can be translated into Petri-nets, which allow for analyzing behavioral properties to a great extent. Activities in such models are encoded as SCOR process categories. The only contribution of SCOR is the vocabulary for activities. This approach results in two modeling phases: First, a SCOR thread diagram is created. Then, its activities and <sup>fl</sup>ow relationships will be used for creating the ProC/B model. The disadvantage is that the second phase requires decisions to be made about the control <sup>fl</sup>ow, but this information is not supplied by the diagram from the <sup>fi</sup>rst phase (no execution semantics of process categories).

Grammar was <sup>fi</sup>rst used as a metaphor for describing business processes in organizational studies and has since then spread to BPM research. Pentland [30] proposed a systematic approach for developing models of organizational processes by adopting the grammar metaphor. This approach was then extended by Lee et al. [22] for using process grammar for constraining the design space of business processes. The objective of constraining also holds for the SCOR reference model, which should help in creating supply chains by referring to valid supply chain structures that are supplied by only SCOR. Our research is in<sup>fl</sup>uenced by the grammar metaphor. Unlike Lee et al., who use production rules as constructs for context-free grammars, we employ graph algebra that allows asserting constraints on valid graphs.

Surprisingly, Pentland also proposes in one of his early works [29] the process grammar approach for supply chains. He argues that supply chains are well-suited for grammars because of their repetitive constituents, high degree of modularization, and centering on product <sup>fl</sup>ows, which all result in a rather limited set of supply chain constructs. He de<sup>fi</sup>nes a supply chain grammar of seven constructs (activities) and nine “tentative” supply chain patterns. This grammar was motivated by experiences gained from three case studies. However, its expressiveness is severely limited, e.g., patterns are sequences of activities only, with no further constraints on valid linkages as well as no formalization of the grammar.

## 4. Grammar deduction

In this section, we describe the process of deducing the grammar for SCOR thread diagrams from the SCM literature. For each element of the basic model (as de<sup>fi</sup>ned in Section 2.2), we add theoretical <sup>fi</sup>ndings that further constrain the supply chain design.

## 4.1. Supply chain literature

Supply chain is the unit of analysis of SCM, which over the past 30 years has evolved from a <sup>fi</sup>eld in operations management into a discipline of management research [10]. The recent past has seen an increasing debate about the state of SCM as a discipline [8] as well as a call for theory building [9,20].

For our purpose of grammar deduction, it is important to state that the majority of SCM researchers use existing theories from other disciplines to explain different aspects of the supply chain [8]. SCM is inter-disciplinary, which encompasses logistics, purchasing, operations management, marketing, strategy, and others. Therefore, the grammar deduction will include both supply chain body of knowledge and its antecedents. The scope of the body of knowledge is constrained by supply chain design as de<sup>fi</sup>ned in Section 1, i.e., determining the long-term, basic structure of supply chain activities, which are connected by product <sup>fl</sup>ows. We are thus interested in constructs that are commonly used in SCM research to describe these structures. Due to the absence of a single “original” theory of supply chain, we extract relevant constructs from seminal SCM works in the related <sup>fi</sup>elds. These constructs are higher order abstractions that can be used in supply chain models, speci<sup>fi</sup>cally in supply chain design (descriptive nature of constructs).

## 4.2. Deduction from SCM frameworks

Descriptive constructs can be found in research that condenses the terminology used in SCM and frames the main issues into conceptual frameworks. These works represent the effort to consolidate the abundant but disparate literature [11,14,25]. An important contribution stems from Lambert and Cooper [20], whose framework consists of three main elements: Supply chain network structure includes the <sup>fi</sup>rms and the links between these <sup>fi</sup>rms. Supply chain business processes move the product from supplier to the customer, and SCM components are managerial variables that are used to integrate the business processes.

There are strong ties between these elements and supply chain design as discussed below. The Network structure answers the following question: who are the relevant supply chain members (in SCOR: actors) with whom to link the processes? Relevance is determined by examining whether an actor carries out value-adding activities to produce a speci<sup>fi</sup>c output for a customer or market. Therefore, supporting actors, who for example only provide resources to other actors, are not the unit of analysis. We deduce that: (1) every actor's processes must be linked to at least one process, and (2) no actor

exists without such a process. Using formal notion, we represent these two constraints as follows:

<table><tr><td>ID</td><td>Description</td><td>Formal definition</td></tr><tr><td>C1</td><td>Each process p has at least one incoming or outgoing product flow f.</td><td>For each $ p \in P $ there exists at least one $ f \in F $ with $ f = (m, p) $ or $ f = (p, m) $, and $ m \in P $, $ m \neq p $.</td></tr><tr><td>C2</td><td>Each actor a carries out at least one process p.</td><td>For each $ a \in A $ there exists at least one $ p \in P $ with $ PA(p) = a $.</td></tr></table>

The framework further de<sup>fi</sup>nes structural dimensions. The Horizontal structure introduces the construct of tier, which is de<sup>fi</sup>ned as the set of actors sharing the same horizontal position within the end points of the supply chain. Thus, all tiers can be arranged in graphical models with no overlaps. It has become common practice to place the <sup>fi</sup>nal customer as the rightmost tier; this holds also true for the SCOR technique. When referring to a particular tier, all the tiers to its left are called upstream and those to the right are called downstream. For expressing the horizontal segmentation, we <sup>fi</sup>rst introduce a numbering scheme for tiers by extending the de<sup>fi</sup>nition of the thread diagram (de<sup>fi</sup>nition 1b). The function N assigns an integer to each tier; the tier number ranges from 1 to |T| for the total number of tiers.

## De<sup>fi</sup>nition 1b. SCOR thread diagram

A SCOR thread diagram is a directed graph $T D = ( P , F , A , T , P C , P A , P T ,$ N) where N is a function that de<sup>fi</sup>nes the order of tiers, $N ( T ) \colon = \{ 1 , . . , | T | \} .$

Using this de<sup>fi</sup>nition, the formal representation of the diagram shown in Fig. 1 can be enriched as follows. The diagram is made of three tiers $\boldsymbol { T } = ( \{ S u p p l i e r$ , Manufacturer, Customer)}, which are arranged from left to right. Therefore, we add $\boldsymbol { N } = ( \{ S u p p l i e r  3 , $ Manufacturer ➔ 2, Customer ➔ 1)}.

Then, we add the constraint C3, which prevents the existence of “empty” tiers.

<table><tr><td>ID</td><td>Description</td><td>Formal definition</td></tr><tr><td>C3</td><td>Each tier  $t$  contains at least one process  $p$ .</td><td>For each  $t \in T$  there exists at least one  $p \in P$  with  $PT(p) = t$ .</td></tr></table>

The Vertical structure refers to the number of actors within each tier. Depending on the number, a tier may be characterized as rather narrow or wide. The narrowest tier is a tier that contains only one actor and process; this requirement is already captured by C3 and C2.

The Horizontal position describes the actor's closeness to the point of origin and the distance from the point of consumption of the supply chain. The point of origin is the tier for which no further supplier exists (tier denoted by $N = \left| { \cal T } \right| )$ . The point of consumption is the tier in which no further value is added, but the product is consumed (tier denoted by $N = 1 )$ . For SCOR, we deduce that every thread diagram has: (1) one origin tier that includes at least one process with no incoming product <sup>fl</sup>ow, and (2) one consumption tier that includes at least one Source or Deliver process with no outgoing product <sup>fl</sup>ow. To be able to state constraints on the number of incoming and outgoing <sup>fl</sup>ows, we <sup>fi</sup>rst need to introduce the notion of predecessor and successor processes. For a given process p, we denote its predecessor processes by •p and its successor processes by p• (de<sup>fi</sup>nition 2). For instance, in Fig. 1, the process of D1 (denoted by p1) in the Supplier tier has no incoming product <sup>fl</sup>ow, thus •p1 = {∅}, and one outgoing <sup>fl</sup>ow to the process denoted by p2, thus $p 1 \cdot = \{ p 2 \}$

## De<sup>fi</sup>nition 2. Predecessors, successors

For $p \in P , \bullet p = \{ m | ( m , p ) \in F \}$ denotes the set of predecessors of p, with $m \in P ,$ and $p \bullet = \{ m | ( p , m ) \in F \}$ denotes the set of successors of p, with $m \in P .$

Then we are able to de<sup>fi</sup>ne the constraints for the origin tier (C4) and the consumption tier (C5).

<table><tr><td>ID</td><td>Description</td><td>Formal definition</td></tr><tr><td>C4</td><td>The left most tier  $t$  contains at least one process  $p$  with no incoming product flow  $f$ .</td><td>For  $t \in T$  with  $N(t) = |T|$  there exists at least one  $p \in P$  with  $PT(p) = t \land |\bullet p| = 0$ .</td></tr><tr><td>C5</td><td>The right most tier  $t$  contains at least one process  $p$  of Source or Deliver with no outgoing product flow  $f$ .</td><td>For  $t \in T$  with  $N(t) = 1$  there exists at least one  $p \in P$  with  $PT(p) = 1 \land PC(p) \in \{S1, S2, S3, D1, D2, D3, D4\} \land |\bullet p| = 0$ .</td></tr></table>

The existence of origin and consumption tiers implies that another tier, which comprises the focal <sup>fi</sup>rm, lies between these tiers. The de<sup>fi</sup>nition by Mentzer et al. makes this implication explicit by de<sup>fi</sup>ning supply chain “as a set of three or more entities… directly involved in the upstream and downstream <sup>fl</sup>ows” [25]. Therefore, the number of tiers, as well as the actors is at least three. Thus, C6 and C7 are the cardinality constraints on the tiers and actors.

<table><tr><td>ID</td><td>Description</td><td>Formal definition</td></tr><tr><td>C6</td><td>Each thread diagram TD consists of at least three tiers (t).</td><td>For any TD: |T| ≥ 3.</td></tr><tr><td>C7</td><td>Each thread diagram TD consists of at least three actors (a).</td><td>For any TD: |A| ≥ 3.</td></tr></table>

With respect to Supply chain business processes, the framework in [20] provides taxonomies of processes and process links. Both taxonomies are, however, more detailed and broader than SCOR. In particular, they consider also information <sup>fl</sup>ows. The SCOR categories of Source, Make, and Deliver map to those of procurement, manufacturing <sup>fl</sup>ow management, and demand management. Product speci<sup>fi</sup>city is not found in the framework.

The set of nine SCM components spans a wide range of managerial variables by which activities across the supply chain are integrated. They address physical/technical, as well as behavioral variables. Due to the framework's abstract nature, we can only deduce that supply chain design is one SCM component (under the term “product <sup>fl</sup>ow facility structure”, which determines the “network structure for sourcing, manufacturing, and distributing across the supply chain” [20]).

Referring to the main elements of the SCOR technique as provided in de<sup>fi</sup>nition 1a (Section 2.2), we found corresponding descriptive constructs in these frameworks, which also de<sup>fi</sup>ne the terminology of SCM. We mapped the framework's constructs to SCOR and enriched the de<sup>fi</sup>nition to some extent. To further underpin SCOR, we need to study SCM and its antecedents for constructs and <sup>fi</sup>ndings about processes, product <sup>fl</sup>ows, and their interdependencies along the supply chain.

## 4.3. Processes

SCM research yields a variety of process classi<sup>fi</sup>cations, which differ in the level of detail and coverage (i.e., <sup>fl</sup>ow of product, information, and resources). For instance, there are seven classi<sup>fi</sup>cations provided in [29], eight in [20], and ten in [25]. When breaking these classi<sup>fi</sup>cations down to the activities that directly modify the product with regard to its structure, location, or market, the resulting activities can be grouped into three basic activities of any <sup>fi</sup>rm: (1) buying resources from other <sup>fi</sup>rms, (2) combining and converting these resources into products, and (3) selling these products to customers. These activities are also constituent to the SCOR technique under the terminology source, make, and deliver, respectively. They correspond to the decision areas that represent the operations management origin of SCM [6,8].

Product speci<sup>fi</sup>city is the second determinant of SCOR processes. The rationale is that stocked, make-to-order, and engineer-to-order products each require different operational strategies [13]. This determinant can be traced back to manufacturing management, which uses these types of product speci<sup>fi</sup>city to describe when a particular product is linked to a particular customer order:

− Make-to-stock (stocked product): a particular product is not linked to a speci<sup>fi</sup>c customer order, but the order can be ful<sup>fi</sup>lled by any product instance from stock.

− Make-to-order: a particular product is linked to a speci<sup>fi</sup>c order at the time of order.

− Engineer-to-order, design-to-order: a particular product is linked to a speci<sup>fi</sup>c order at the time the collaborative engineering starts.

Operations management has emphasized that dedicated methods are required for these product speci<sup>fi</sup>cities [16,18]. Moreover, speci-<sup>fi</sup>city is an important determinant for deciding about the decoupling point, i.e., the tier, where the linkage between a particular product and the order is established [28].

The dependencies between product speci<sup>fi</sup>city and supply chain tier must be considered in using the SCOR technique. Prior to adding further constraints, we must de<sup>fi</sup>ne the two determinants of the processes – activity type and product speci<sup>fi</sup>city – formally. We add these classi<sup>fi</sup>cations by de<sup>fi</sup>ning the SCOR technique in de<sup>fi</sup>nition 3 and using SCOR's terminology (management process for activity type). This de<sup>fi</sup>nition contains three sets for process categories, management processes, and product speci<sup>fi</sup>cities and two functions that map process categories to management processes and product speci<sup>fi</sup>cities.

## De<sup>fi</sup>nition 3. SCOR thread diagram technique

The SCOR thread diagram technique is a tuple $T D T = ( C , M , C M , S , C S )$ where:

− C is the set of process categories $c \in C ,$ with C = {S1, S2, S3, M1, M2, M3, D1, D2, D3, D4},

− M is the set of management processes m ∈ M, with M = {Source, Make, Deliver},

− CM is a function which maps each process category c ∈ C onto a management process m ∈ M, with CM = {S1 ➔ Source, S2 ➔ Source, S3 ➔ Source, M1 ➔ Make, M2 ➔ Make, M3 ➔ Make, D1 ➔ Deliver, D2 ➔ Deliver, D3 ➔ Deliver, D4 ➔ Deliver},

− S is the set of product speci<sup>fi</sup>cities s ∈ S, with S = {Stock, Order, Engineer, Retail},

− CS is a function which maps each process category c ∈ C onto a product speci<sup>fi</sup>city $s \in S ,$ with CS = {S1 ➔ Stock, S2 ➔ Order, S3 ➔ Engineer, M1 ➔ Stock, M2 ➔ Order, M3 ➔ Engineer, D1 ➔ Stock, D2 ➔ Order, D3 ➔ Engineer, D4 ➔ Retail}.

## 4.4. Product flows

Product <sup>fl</sup>ows are of paramount importance to supply chain design, since they implement the linkages between actors and their processes. In this section, we clarify the semantics of product <sup>fl</sup>ow, which is regarded as a critical shortcoming of the SCOR technique. We de<sup>fi</sup>ne the semantics by asserting constraints on the product <sup>fl</sup>ow relation, i.e., on $F \subseteq P \times P .$

## 4.4.1. Product flows within actors

The rationale for product <sup>fl</sup>ows is that each <sup>fl</sup>ow must indicate that the preceding process has added value to the product, i.e., each process adds value to the product up to the process of consumption by the <sup>fi</sup>nal customer. SCM is also concerned with the value-adding activities that take place within an actor. Thus, the actor is not perceived as a “black box” of input/output relations, but regarded as a set of value-adding activities. For this reason, the SCM frameworks contain classi<sup>fi</sup>cations of such activities [20,25].

In SCOR, the three management processes of Deliver, Make, and Source span a set of nine potential product <sup>fl</sup>ows as shown in Fig. 2. However, only the downstream <sup>fl</sup>ows indicate added value; these <sup>fl</sup>ows are Source to Deliver, Source to Make, and Make to Deliver. In addition, manufacturing is often a complex activity that adds value in several steps. Therefore, processes of Make can be connected with other Make processes. The literature denotes these systems as multi-stage manufacturing systems [21].

Next, we formulate the constraint C8 for capturing the possible product <sup>fl</sup>ows inside an actor.

<table><tr><td>ID</td><td>Description</td><td>Formal definition</td></tr><tr><td>C8</td><td>Each flow inside an actor is between one of the following management processes:Source to Deliver, Source to Make, Make to Make, or Make to Deliver.</td><td>For each  $f = (p_i, p_j)$  with  $PA(p_i) = PA(p_j)$ : $(CM(PC(p_i)) = \{Source\} \land CM(PC(p_j)) = \{Deliver\}) \lor (CM(PC(p_i)) = \{Source\} \land CM(PC(p_j)) = \{Make\}) \lor (CM(PC(p_i)) = \{Make\} \land CM(PC(p_j)) = \{Make\}) \lor (CM(PC(p_i)) = \{Make\} \land CM(PC(p_j)) = \{Deliver\})$ </td></tr></table>

We de<sup>fi</sup>ne the product <sup>fl</sup>ow as $f = ( p _ { i } , p _ { j } )$ . First, we require that the two processes p<sub>i</sub> and p<sub>j</sub> belong to the same actor, i.e., by referring to the function PA. Second, we enumerate the four allowed combinations by using the function PC to each process (which yields the process category, e.g., D1) and applying the function CM (which yields the respective management process, e.g., Deliver).

## 4.4.2. Product flows between actors

These <sup>fl</sup>ows materialize through the transfer of a product from the supplier's Deliver process to the buyer's Source process. The analysis of the dyadic buyer–supplier relationship is an important antecedent of SCM [2]. We must restrict product <sup>fl</sup>ows between actors to buyer– supplier relationships that add value downstream in the supply chain. Fig. 3 illustrates that these <sup>fl</sup>ows take place at the interface of two tiers (example on the left hand), but not inside the same tier (example on the right hand).

In constraint C9, we consider a product <sup>fl</sup>ow $f = ( p _ { i } , p _ { j } )$ , which takes place between two different actors (we use the function PA to separate the actors). First, the actors must not only be different, but the actor of process $p _ { i }$ must be the supplier of the actor of process p ; hence the tier number of ${ \dot { p } } _ { i }$ must be greater than that of $p _ { j } .$ Finally, we state the buyer–supplier relationship by using the functions CM and PC.

<table><tr><td>ID</td><td>Description</td><td>Formal definition</td></tr><tr><td>C9</td><td>Each flow between two actors connects a Deliver process with a Source process and the preceding actor&#x27;s tier is left from the succeeding actor&#x27;s tier.</td><td>For each  $f = (p_i, p_j)$  with  $PA(p_i) \neq PA(p_j)$ : $N(PT(p_i)) > N(PT(p_j)) \land CM(PC(p_i)) = \{Deliver\} \land CM(PC(p_j)) = \{Source\}$ </td></tr></table>

4.4.3. Dependence on product specificity

The speci<sup>fi</sup>city of a given product does not change along the supply chain. The reason is that speci<sup>fi</sup>city is de<sup>fi</sup>ned (as described in Section 4.3) by the time the respective product is linked to a particular customer order. Once a product is linked to an order, the linkage cannot be broken by downstream processes [28], unless the product is transformed through manufacturing into another product.

First, we look at product <sup>fl</sup>ows between two actors as restricted by constraint C9. The source process in the downstream tier is the activity of buying the product from the upstream tier, thus the speci<sup>fi</sup>city of both processes must be the same (e.g., buying a make-to-order product is only possible from the deliver process of make-to-order) except for retail products and its respective D4 process. We retrieve the speci<sup>fi</sup>city of both linked processes by using the function CS and de<sup>fi</sup>ne constraint C10.

![](/api/attachments/4XMGM65V/fulltext/images/d0796e581e0ef054a3c648e394ed453904730967b0463ddaffdba47e09ffb92b.jpg)  
Fig. 2. Possible product <sup>fl</sup>ows inside an actor by management process.

<table><tr><td>ID</td><td>Description</td><td>Formal definition</td></tr><tr><td>C10</td><td>Each flow into a Source process of S2 or S3 starts at a preceding actor&#x27;s Deliver process of the same product specificity.</td><td>For each  $f = (p_i, p_j)$  with  $PA(p_i) \neq PA(p_j)$  $\land (PC(p_j) = \{S2\} \lor PC(pj) = \{S3\})$ : $N(PT(p_i)) > N(PT(p_j))$  $\land CM(PC(p_j)) = \{Source\}$  $\land CS(CM(PC(p_i))) = CS(CM(PC(p_j)))$ </td></tr></table>

It is worth noting that D4 was added to the SCOR technique as a variant of D1 (available since version 6.0). Retail products can be retrieved from either S1 or S2 processes and will then be sold at a retail store, which maintains the D4 process. We include this case into a speci<sup>fi</sup>c constraint (C11).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
ID Description Formal definition
C11 Each flow into a Source process of S1 starts at a preceding actor's Deliver process of specificity Stock or Retail. For each  $f = (p_i, p_j)$  with  $PA(p_i) \neq PA(p_j) \land PC(p_j) = \{S1\}$ :  $N(PT(p_i)) &gt; N(PT(p_j))$ $\land CM(PC(p_i)) = \{Source\}$ $\land CS(CM(PC(p_i))) \in \{Stock, Retail\}$
</div>

Second, we analyze product <sup>fl</sup>ows within actors. Flows within actors describe the value-adding activities, which can be more complex in terms of number of processes and <sup>fl</sup>ows. In particular, we must pay attention to all four cases mentioned in Section 4.4.1 and their interplay.

Let us consider the example shown in Fig. 4, which shows that the actor sells two products. The stocked product is bought via a S1 process and then sold via a corresponding D1 process. The make-to-order product results from two subsequent M2 processes, with the <sup>fi</sup>rst transforming a make-to-order product into an intermediate product, and the second process combining it with another stocked product into the <sup>fi</sup>nal product.

![](/api/attachments/4XMGM65V/fulltext/images/d44dc01af5763ea93e07420e3565da7bbfb265543863efc9ba3e6117cc156833.jpg)  
Fig. 4. Example of possible and forbidden product <sup>fl</sup>ows within an actor.

What we are missing so far is the semantics of the Make processes: Manufacturing transforms productive inputs into products of higher value, thus every Make process transforms the product. On the contrary, Source does not transform the product, but transfers the product to the next process of either Make or Deliver. Similarly, Deliver transfers the product to another tier.

The issue of product transformation vs. transfer is closely related to product speci<sup>fi</sup>city. We summarize this dependency by analyzing the four cases of product <sup>fl</sup>ows within actors.

Source to Deliver transfers a product, which will be directly sold to the customer. The delivery process may link the product to a particular customer order, thus speci<sup>fi</sup>city can increase from S1 to D2. The S1 process can also transfer the product to D4. These requirements are captured by C12 and C13.

```txt
ID Description Formal definition
C12 Each flow from Source of S2 or S3 (pre) to Deliver (suc) connects to processes of the same specificity.
C13 Each flow from Source of S1 (pre) to Deliver (suc) connects to processes of specificity Stock, Order, or Retail.
For each f with f = (pre, suc) ∧ PC(pre) ∈ {S2, S3} ∧ CM(PC(suc)) = {Deliver}: CS(CM(PC(pre))) = CS(CM(PC(suc)))
For each f with f = (pre, suc) ∧ PC(pre) = {S1} ∧ CM(PC(suc)) = {Deliver}: CS(CM(PC(suc))) ∈ {Stock, Order, Retail}
```

Source to Make transfers a product that will be transformed into another product. The speci<sup>fi</sup>city may increase along the supply chain, but not decrease (C14). In the example in Fig. 4, it is forbidden to link the S3 process with the M2 process, because the manufacturing relies on a product speci<sup>fi</sup>cation, but this speci<sup>fi</sup>cation would not be available due to the engineer-to-order product of S3.

Make to Make is the product transfer in multi-stage manufacturing. Again, speci<sup>fi</sup>city may increase in succeeding stages, but not decrease (C15).

![](/api/attachments/4XMGM65V/fulltext/images/d668192b81f57b127eb58df9f0f80a5a2f7edd6346b91cf9d74f978ec5287665.jpg)  
Fig. 3. Possible (left) and forbidden (right) product <sup>fl</sup>ows between actors.

Make to Deliver is the transfer to the last process within the actor. The product <sup>fl</sup>ow must respect the correspondence of speci<sup>fi</sup>cities (C16).

<table><tr><td>ID</td><td>Description</td><td>Formal definition</td></tr><tr><td>C14</td><td>Each flow from Source(pre) to Make (suc) connects processes of the same or higher specificity.</td><td>For each  $f$  with  $f = (pre, suc)$  $\wedge CM(PC(pre)) = \{Source\} \wedge CM(PC(suc)) = \{Make\}$ : $(CS(CM(PC(pre))) = \{Stock\}$  $\wedge CS(CM(PC(suc))) \in \{Stock, Order, Engineer\}) \vee$  $(CS(CM(PC(pre)))) = \{Order\}$  $\wedge CS(CM(PC(suc))) \in \{Order, Engineer\}) \vee$  $(CS(CM(PC(pre))) = \{Engineer\}$  $\wedge CS(CM(PC(suc))) = \{Engineer\})$ </td></tr><tr><td>C15</td><td>Each flow from Make(pre) to Make (suc) connects processes of the same or higher specificity.</td><td>For each  $f$  with  $f = (pre, suc)$  $\wedge CM(PC(pre)) = \{Make\} \wedge CM(PC(suc)) = \{Make\}$ : $(CS(CM(PC(pre))) = \{Stock\}$  $\wedge CS(CM(PC(suc))) \in \{Stock, Order, Engineer\}) \vee$  $(CS(CM(PC(pre)))) = \{Order\}$  $\wedge CS(CM(PC(suc))) \in \{Order, Engineer\}) \vei$  $(CS(CM(PC(pre))) = \{Engineer\}$  $\wedge CS(CM(PC(suc))) = \{Engineer\})$ </td></tr><tr><td>C16</td><td>Each flow from Make(pre) to Deliver (suc) connects processes of the same specificity.</td><td>For each  $f$  with  $f = (pre, suc)$  $\wedge CM(PC(pre)) = \{Make\} \wedge CM(PC(suc)) = \{Deliver\}$ : $CS(CM(PC(pre))) = CS(CM(suc))$ </td></tr></table>

## 4.5. Correctness properties

In this section, we summarize the grammar deduction process by describing the usefulness of each constraint for verifying the correctness of SCOR thread diagrams. Each constraint represents a particular correctness property. Table 1 shows the correctness properties for the constraints C1 through C16.

If a particular constraint is violated by a given diagram, then we are able to (1) identify the incorrect elements of the model and (2) interpret the reported problem by referring to the informal description of the respective constraint. For instance, constraint C9 requires that each <sup>fl</sup>ow between two actors connects the Deliver and the Source processes where the preceding actor belongs to the tier on the left of the succeeding actor's tier. If this constraint is breached, we characterize the problem as a false connection of processes between actors. The usefulness of the constraint is that it helps determine such problems.

## 5. Evaluation

From the perspective of the design science paradigm [17], the artifact that has been developed in this research is the SCOR grammar. The objective of this evaluation is to demonstrate the usefulness of this artifact for assessing the correctness of existing SCOR thread diagrams.

## 5.1. Evaluation procedure

We obtained models from the SCOR website (http://supply-chain. org/<sup>fi</sup>lemanager/active) that provides both case studies and training materials in the form of reports or slides. We selected the models based on size (minimum of 10 processes to exclude “toy” models). The selection was documented and the models were stored in their original format. The evaluation set contained 8 models. Table 2 shows the characteristics of these models.

For representing the selected models in a prototype system, we chose a Description Logic-based approach [5]. Description logic (DL) is a family of formalisms for representing knowledge within a domain and is well-suited for reasoning about this knowledge. These formalisms have been adopted successfully for model veri<sup>fi</sup>cation in a number of related areas [3,31]. For specifying the SCOR grammar, we employ the Web Ontology Language (OWL 1.0) [38] and its complementing Semantic Web Rule Language (SWRL) [39]. The latter is used for determining the correct and incorrect model elements (instances of the ontology) and adding them to speci<sup>fi</sup>c classes for each constraint C1 through C16.

Each model was manually mapped to the ontology and the assertions stored in an OWL knowledge base using the Protégé 3.5 editor and framework. Protégé provides full support for both OWL and SWRL, and has become a reference tool for developing ontology-based applications. The mapping procedure was required because the original models are not machine-readable (due to the absence of a data exchange format). Each model was analyzed for correctness by using the built-in reasoner in Protégé and checking for each constraint separately. The reasoner populated the speci<sup>fi</sup>c classes with the correct and incorrect instances.

## 5.2. Results

The model veri<sup>fi</sup>cation found that seven out of the eight models in the sample contained errors, i.e., violated one or more constraints. Collecting this data required performing the veri<sup>fi</sup>cation for each model separately and then handing the results over to a data analysis tool. The current prototype system is not designed for presenting the veri<sup>fi</sup>cation results directly in the graphical model. Fig. 5 presents a visualization of the veri<sup>fi</sup>cation results for model TD2 by highlighting the erroneous processes and product <sup>fl</sup>ows, and identifying the constraints that have been violated (shown in square brackets).

We observed several cases in which the designer apparently used a customized version of the SCOR technique. While most of these changes are extensions that introduced new constructs, the model

Correctness properties for SCOR thread diagrams.

<table><tr><td>ID</td><td>Correctness property</td><td>Usefulness</td></tr><tr><td>C1</td><td>Value-adding processes</td><td>Determines processes that do not add value to the product.</td></tr><tr><td>C2</td><td>Value-adding actors</td><td>Determines actors that do not add value to the product.</td></tr><tr><td>C3</td><td>Value-adding tiers</td><td>Determines tiers that do not add value to the product.</td></tr><tr><td>C4</td><td>Origin tier</td><td>Determines the existence of the origin tier.</td></tr><tr><td>C5</td><td>Consumption tier</td><td>Determines the existence of the consumption tier.</td></tr><tr><td>C6</td><td>Minimum tiers</td><td>Determines if the diagram lacks tiers.</td></tr><tr><td>C7</td><td>Minimum actors</td><td>Determines if the diagram lacks actors.</td></tr><tr><td>C8</td><td>Correct product flows inside actors</td><td>Determines false connections of processes inside an actor.</td></tr><tr><td>C9</td><td>Correct product flows between actors</td><td>Determines false connections of processes between actors.</td></tr><tr><td>C10</td><td>Correct flows into the Source of S2 and S3 from supplier</td><td>Determines false usage of product specificity between actors for S2 and S3.</td></tr><tr><td>C11</td><td>Correct flows into the Source of S1 from supplier</td><td>Determines false usage of product specificity between actors for S1.</td></tr><tr><td>C12</td><td>Correct flows from the Source of S2 and S3 to the Deliver processes inside actors</td><td>Determines false usage of product specificity inside actors for S2 and S3.</td></tr><tr><td>C13</td><td>Correct flows from the Source of S1 to the Deliver processes inside actors</td><td>Determines false usage of product specificity inside actors for S1.</td></tr><tr><td>C14</td><td>Correct flows from Source to Make processes</td><td>Determines false usage of product specificity inside actors for Source to Make processes.</td></tr><tr><td>C15</td><td>Correct flows from the Make to Make processes</td><td>Determines false usage of product specificity inside actors for Make to Make processes.</td></tr><tr><td>C16</td><td>Correct flows from Make to Deliver processes</td><td>Determines false usage of product specificity inside actors for Make to Deliver processes.</td></tr></table>

Table 2  
Basic characteristics of the sample.

<table><tr><td>ID</td><td>Source</td><td>Industry</td><td>Year</td><td>|T|</td><td>|A|</td><td>|P|</td><td>|F|</td></tr><tr><td>TD1</td><td>Cheng et al.</td><td>Construction</td><td>2009</td><td>5</td><td>6</td><td>13</td><td>11</td></tr><tr><td>TD2</td><td>GE</td><td>Jet engines</td><td>2006</td><td>5</td><td>5</td><td>13</td><td>11</td></tr><tr><td>TD3</td><td>KLATencor</td><td>Service parts</td><td>2006</td><td>4</td><td>5</td><td>12</td><td>12</td></tr><tr><td>TD4</td><td>Schenker</td><td>Logistics</td><td>2006</td><td>5</td><td>7</td><td>18</td><td>17</td></tr><tr><td>TD5</td><td>Marine Corps</td><td>Military deployment</td><td>2006</td><td>3</td><td>7</td><td>28</td><td>27</td></tr><tr><td>TD6</td><td>Nortel</td><td>Telecommunication</td><td>1997</td><td>4</td><td>6</td><td>15</td><td>14</td></tr><tr><td>TD7</td><td>SCOR Primer</td><td></td><td>1997</td><td>5</td><td>6</td><td>11</td><td>9</td></tr><tr><td>TD8</td><td>SCOR configuration</td><td></td><td>1997</td><td>4</td><td>7</td><td>20</td><td>20</td></tr><tr><td>MIN:</td><td></td><td></td><td></td><td>3</td><td>5</td><td>11</td><td>9</td></tr><tr><td>MAX:</td><td></td><td></td><td></td><td>5</td><td>7</td><td>28</td><td>27</td></tr><tr><td>MEAN:</td><td></td><td></td><td></td><td>4.38</td><td>6.13</td><td>16.25</td><td>15.13</td></tr></table>

TD3 contains modi<sup>fi</sup>cations of the original constructs. Let us consider the model TD3 shown in Fig. 6.

First, the diagram arranges tiers vertically and uses a speci<sup>fi</sup>c symbol for vertical processes between actors of the same tier. This modi-<sup>fi</sup>cation, however, does not add information to the underlying formal representation, but changes the visual presentation. Whether this presentation is more intuitive or better suited for communicating supply chain design, remains to be assessed. The second modi<sup>fi</sup>cation introduces compositions of D1 and D4 processes denoted by D1/4. Again, this modi<sup>fi</sup>cation can be mapped to the formal model without losing information. Speci<sup>fi</sup>cally, each composite process can be replaced by two elementary processes (e.g., D1 and D4), which must then be connected to the respective preceding and succeeding processes of the composite process.

We summarize the veri<sup>fi</sup>cation results in Table 3. The table shows for each model (TD1 through TD8) and constraint (C1 through C16) the <sup>fi</sup>ndings as follows: ‘Ok’ indicates that the constraint is ful<sup>fi</sup>lled and ‘Error/x’ indicates that x number of model elements breach the respective constraint. For instance, ‘Error/1’ for C1 means that one process is not linked to any other process. If the model contains no element relevant to the constraint, then the constraint is not applicable and we indicate this case in the table by a hyphen. For instance, C15 is concerned with links between Make processes; however, no model in the sample contained any link between such processes.

We calculate two metrics for each model. The process error rate (PER) represents the relative number of erroneous processes compared to the total number of processes in the model. This metric is affected by constraint C1, which is the only constraint dealing with processes. For instance, TD1 contains one such process out of 13 processes, hence the PER is 7.7%. Similarly, the flow error rate (FER) measures the proportion of erroneous product <sup>fl</sup>ows and is dependent on C8 through C16. In addition, we de<sup>fi</sup>ne the constraint error rate (CER), which signi<sup>fi</sup>es the relative number of error-prone models compared to all models for which the constraint is meaningful. For instance, C12 was breached by two out of four models that contain relevant product <sup>fl</sup>ows and thus CER is 50.0%.

For further analysis, we divide the sixteen constraints into three larger groups as follows. C1 through C7 enforce the correct usage of the main constructs of process, tier, actor, and product <sup>fl</sup>ow, without speci<sup>fi</sup>cally considering their interrelation. C8 and C9 check the correct usage of the construct of management process, thus Source, Make, and Deliver. Finally, C10 through C16 assess the correct usage of the construct of product speci<sup>fi</sup>city. We aggregate the veri<sup>fi</sup>cation results accordingly in Table 4.

## 5.3. Discussion

The results presented in Tables 3 and 4 lead to a number of observations. First, we found errors in all but one model. However, the error-free model TD4 stems from the transport logistics in which all processes are of make-to-order speci<sup>fi</sup>city and no manufacturing takes place. TD4 thus contains only S2 and D2 processes, which describe a product <sup>fl</sup>ow with no branches. This could limit the appearance of syntactic errors. On the other hand, each error-prone model violates two or three constraints.

Second, as shown in Table 3, the highest CER is reported for C11 (71.4%), C10, and C12 (both at 50.0%). All three constraints relate to the usage of product speci<sup>fi</sup>city as a determinant of linked processes from Source to Deliver or Deliver to Source. In general, product speci-<sup>fi</sup>city appears to be the most ambiguous construct of SCOR, since Table 4 reveals that its aggregated CER is as high as 87.5%. In the other two constraint groups, errors are found in three out of the eight models. The management process construct was used falsely as well: Two models contain a sequence of Make-Deliver-Make as shown in Fig. 7, whereas only Make-Make would be correct. One model arranged two actors that exchange products within the same tier instead of separating them into two different tiers (TD3, shown in Fig. 6).

When interpreting the results, in particular the relatively high error rates, we must be aware of the sample size. Since our sample is too small for further statistical analysis, it did not allow us to provide evidence in terms of factors that affect the error rate of a particular model. However, we believe that our initial <sup>fi</sup>ndings suggest some ambiguity in the existing body of knowledge that is available to supply chain designers. This knowledge ranges from the SCOR documentation and supplementing training material to other references and software tools. We also found errors in the two models that originated directly from the SCOR organization, which were presented at the SCOR Fall Conference 1997 (TD7, TD8).

![](/api/attachments/4XMGM65V/fulltext/images/9ebf05fe39803fab71e6c0f2e55f164cf1a689ebb0bdcc36a2c933f6e2db2e20.jpg)  
Fig. 5. Model veri<sup>fi</sup>cation results for model TD2 (four errors identi<sup>fi</sup>ed).

![](/api/attachments/4XMGM65V/fulltext/images/bd85357887d89117ad278922fa6a3a42b48b779b27b9a3d44607b05e901e0940.jpg)  
Fig. 6. Customized SCOR technique used in model TD3

The proposed methodology and the prototype successfully detect errors in SCOR models. These errors must be corrected by the supply chain designer. Next, we illustrate how our approach can assist the designer in correcting incorrect models. We have to consider that often several alternatives exist for <sup>fi</sup>xing the errors, from which the designer has to choose the alternative that matches the desired structure. For instance, the model in Fig. 5 shows for the OEM tier an invalid link between the D2 process and the S1 process of the Warehouse tier. There exist at least two alternatives for the designer, i.e., either modifying D2 to D1 or modifying S1 to S2. We can automatically generate these alternatives and present them to the designer by deriving a rule from the formal de<sup>fi</sup>nition of C11 as follows: For each <sup>fl</sup>ow ${ \boldsymbol { f } } = ( p _ { i } , p _ { j } )$ in error class C11, modify the model as follows: $C S ( C M ( P C ( p _ { i } ) ) ) \colon = \{ S t o c k \} \vee C S ( C M ( P C ( p _ { j } ) ) ) \colon = \{ R e t a i l \}$

In this way, we are able to construct rules for every constraint (by enumerating the alternatives that are offered by the constraint) and present the alternatives to the designer to choose from. A practical limitation of this repair approach is that <sup>fi</sup>xing a particular error may cause subsequent errors. For instance, if the designer changes the S1 process of the Warehouse tier (Fig. 5) into S2, the link to its succeeding D1 process becomes invalid (violation of constraint C12). These cascading errors could propagate both upstream and downstream the supply chain and thus arriving at a correct model maybe somewhat cumbersome. Therefore, assisting the designer in developing correct models from the start is another direction to take by proactively providing suggestions for linking processes to prevent errors. Next, we outline how the deduced constraints can be used for assisting the designer in this task.

Table 3  
Results of model veri<sup>fi</sup>cation.

<table><tr><td></td><td>TD1</td><td>TD2</td><td>TD3</td><td>TD4</td><td>TD5</td><td>TD6</td><td>TD7</td><td>TD8</td><td>CER</td></tr><tr><td>C1</td><td>Error/1</td><td>Error/1</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Error/1</td><td>Ok</td><td>37.5%</td></tr><tr><td>C2</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>0.0%</td></tr><tr><td>C3</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>0.0%</td></tr><tr><td>C4</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>0.0%</td></tr><tr><td>C5</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>0.0%</td></tr><tr><td>C6</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>0.0%</td></tr><tr><td>C7</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>0.0%</td></tr><tr><td>C8</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Error/1</td><td>Ok</td><td>Ok</td><td>Error/2</td><td>25.0%</td></tr><tr><td>C9</td><td>Ok</td><td>Ok</td><td>Error/1</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>12.5%</td></tr><tr><td>C10</td><td>Ok</td><td>-</td><td>-</td><td>Ok</td><td>Error/2</td><td>Error/1</td><td>-</td><td>-</td><td>50.0%</td></tr><tr><td>C11</td><td>Ok</td><td>Error/2</td><td>Error/1</td><td>-</td><td>Error/2</td><td>Ok</td><td>Error/2</td><td>Error/1</td><td>71.4%</td></tr><tr><td>C12</td><td>Error/1</td><td>Ok</td><td>-</td><td>Ok</td><td>-</td><td>Error/1</td><td>-</td><td>-</td><td>50.0%</td></tr><tr><td>C13</td><td>-</td><td>Ok</td><td>Ok</td><td>-</td><td>-</td><td>-</td><td>Ok</td><td>-</td><td>0.0%</td></tr><tr><td>C14</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>0.0%</td></tr><tr><td>C15</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>C16</td><td>Ok</td><td>Error/1</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Error/4</td><td>25.0%</td></tr><tr><td>PER</td><td>7.7%</td><td>7.7%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>9.1%</td><td>0.0%</td><td></td></tr><tr><td>FER</td><td>9.1%</td><td>27.3%</td><td>16.7%</td><td>0.0%</td><td>18.5%</td><td>14.3%</td><td>22.2%</td><td>35.0%</td><td></td></tr></table>

We consider an upstream design in which the designer de<sup>fi</sup>nes all the tiers, adds processes to the rightmost tier, and then places linked processes in the upstream tiers. For instance, the rightmost tier contains a single S2 process denoted by p1, with $P C ( p 1 ) = \{ S 2 \}$ and $N ( P T ( p 1 ) ) = 1$ . Two other tiers exist. The question is what kind of processes p2 may link to p1 by the <sup>fl</sup>ow $f 1 = ( p 2 , p 1 ) \colon$ We can generate all valid answers by analyzing those constraints that are concerned with <sup>fl</sup>ows into S2 processes:

− Constraint C8 is not relevant, because it relates only to <sup>fl</sup>ows inside an actor. Constraint C9 allows <sup>fl</sup>ows into Source processes from Deliver processes of preceding tiers. Therefore, we use the de<sup>fi</sup>nition of this constraint and add an axiom to the design space: $( P C ( p 2 ) { : = }$ {D1} $\times ~ P C ( p 2 ) \colon = \{ D 2 \} ~ \lor ~ P C ( p 2 ) \colon = \{ D 3 \} ~ \lor ~ P C ( p 2 ) \colon = \{ D 4 \} )$ ∧ $( N ( P T ( p 2 ) ) \colon = 2 \lor N ( P T ( p 2 ) ) \colon = 3 )$

− Constraint C10 helps us in suggesting the right product speci<sup>fi</sup>city of p2, i.e., speci<sup>fi</sup>city of p2 must be the same as that of p1. We add to the design space: $C S ( C M ( P C ( p 2 ) ) ) \colon = C S ( C M ( P C ( p 1 ) ) )$

− Next, we can assess the design space, which consists of two axioms. Since CS(CM(PC(p1))) is given in the model as Order, we replace the second axiom by CS(CM(PC(p2))): = {Order}. Therefore, the design space is further reduced to: $P C ( p 2 ) \colon = \{ D 2 \} \wedge ( N ( P T ( p 2 ) ) \colon = 2 \vee$ $N ( P T ( p 2 ) ) \colon = 3 )$

Finally, the designer can select from these two suggestions by placing a D2 process as an input for the S2 process, in either tier left of the customer tier. In this way, we are able to generate candidate incoming <sup>fl</sup>ows for all the process categories and suggest them to the designer to choose from. We have illustrated the required analytical steps for the upstream design only. In case of the downstream design, the analysis would be quite similar, by taking from the constraint definitions those parts that are concerned with the succeeding process and converting them into axioms.

## 5.4. Implications

Our research has implications for both the users and developers of SCOR. Users should carefully revisit the existing SCOR documentation and base their supply chain design on a formal grammar instead of being inspired by only the brief descriptions and example models. Otherwise, they are in danger of developing models that may contain subjective interpretations of the technique and thus cannot be exchanged, formally analyzed, and shared with supply chain stakeholders. This risk would also hamper bene<sup>fi</sup>ting from the two posited advantages of reference models for supply chain design. The evaluation results suggest that the product speci<sup>fi</sup>city construct leads to a number of design alternatives that must be carefully evaluated by the user to select a correct design. At least, its original de<sup>fi</sup>nition lacks clarity to enable its correct usage. However, the SCM literature provides suf<sup>fi</sup>cient underpinning, as discussed in Section 4.4.3, for clarifying the syntax and semantics of processes and product <sup>fl</sup>ows under consideration with respect to product speci<sup>fi</sup>city.

Table 4  
Results of model veri<sup>fi</sup>cation per constraint group.

<table><tr><td>Constraint group</td><td>TD1</td><td>TD2</td><td>TD3</td><td>TD4</td><td>TD5</td><td>TD6</td><td>TD7</td><td>TD8</td><td>CER</td></tr><tr><td>Usage of the constructs of process, tier, actor, and product flow</td><td>Error</td><td>Error</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Ok</td><td>Error</td><td>Ok</td><td>37.5%</td></tr><tr><td>Usage of the construct of management process</td><td>Ok</td><td>Ok</td><td>Error</td><td>Ok</td><td>Error</td><td>Ok</td><td>Ok</td><td>Error</td><td>37.5%</td></tr><tr><td>Usage of the construct of product specificity</td><td>Error</td><td>Error</td><td>Error</td><td>Ok</td><td>Error</td><td>Error</td><td>Error</td><td>Error</td><td>87.5%</td></tr></table>

While the proposed methodology successfully detects incorrect models, our research also has implications for the use of validated models and the development of decision support systems (DSS) within SCM. These implications concern the third use case of the SCOR technique (discussed in Section 1), namely, supply chain evaluation. The DSS must assist the designer in creating alternative designs and assessing their performance through appropriate metrics. For this type of DSS, the proposed artifact provides not only the formalization for model representation and storage, but also automatic generation of alternative designs. The dif<sup>fi</sup>culty in generating alternative designs is the sheer number of alternatives that may result from adding, removing, and modifying each single model element (processes, <sup>fl</sup>ows, actors, and tiers). The proposed artifact could be used for answering questions such as what downstream and upstream alternatives exist for a particular process. For instance, the M3 process in Fig. 1 has three upstream processes of category S1 and S2. We can generate alternatives for either process by utilizing the constraint that is concerned with these processes, namely, C14. The formal definition of C14 spans the design space, which consists of two alternatives for each upstream process (S2 and S3 for the S1 process, and S1 and S3 for the S2 process). In this way, the proposed constraints could be used by the DSS for generating alternative designs and presenting them to the designer. Similarly, while correcting invalid models, each alternative for a particular process may result in subsequent errors, both downstream and upstream. In this case, the DSS could apply the “repair” methodology as described in the preceding section to avoid cascading errors.

## 6. Conclusion and future work

This research presents a supply chain grammar and analysis techniques for SCOR-based supply chain design. The grammar adapts SCM constructs and rules to avoid making assumptions about supply chain design that are not justi<sup>fi</sup>ed by the literature.

There are three main results of this work. First, this research demonstrates that the SCM literature provides the rules to be able to effectively restrict the design space that is spanned by the SCOR technique. This research could be extended to support reverse product <sup>fl</sup>ows (return processes), information <sup>fl</sup>ows (plan processes) as well as other parts of the SCOR Model. However, any endeavor must <sup>fi</sup>rst clarify the main constructs for primary product <sup>fl</sup>ows, which is the main focus of our research.

Second, our work represents an effort to improve the understanding of supply chain designs across organizational boundaries. Speci<sup>fi</sup>- cally, it highlights the need to clearly de<sup>fi</sup>ne the formal semantics of primary product <sup>fl</sup>ows in SCOR thread diagrams, which is missing so far. The initial evaluation suggests that the current adoption of the SCOR technique is negatively impacted by its informal description, which leads to error-prone supply chain designs.

Third, the grammar is an initial step in understanding the many factors that affect the correctness of models created, the perceptions of model users, and the performance of individuals who use these models for solving problems in a particular domain. Speci<sup>fi</sup>cally, it is still unknown how a particular error rate is correlated with factors such as the design environment (e.g., grammar used, software tool support) and domain (e.g., industry, size and complexity of the diagram). These effects could be studied by incorporating the general <sup>fi</sup>ndings from conceptual modeling research [40].

Our future work will use the deduced supply chain grammar to study the factors that affect the extent to which model users understand the domain semantics that is conveyed in a thread diagram. Our current study suggests that the original version of the SCOR grammar, which is provided in the SCOR handbook, causes dif<sup>fi</sup>culties for effectively de<sup>fi</sup>ning mappings between real-world phenomena and their representations. For instance, the original grammar lacks rules that guide designers how to connect processes under consideration of the supply chain context. These rules were added by deduction from the existing SCM literature. Positing that de<sup>fi</sup>ciencies in the grammar exist, we plan to empirically validate in a laboratory experiment, the effects of such de<sup>fi</sup>ciencies on the user's problem solving performance when using models generated from the grammar.

![](/api/attachments/4XMGM65V/fulltext/images/e1faca667af50e2dc0f506ccc5b38290e44a516d7a3340a7166def1ae57b5b6b.jpg)  
Fig. 7. Incorrect use of the management process construct in model TD5 (left) and TD8 (right).

## Acknowledgements

The work of the <sup>fi</sup>rst author has been partly supported by the German Ministry of Education and Research under the project InterLogGrid (BMBF 01IG09010E). The work of the second author has been partly supported by Sogang Business School’s World Class University Program (R31–20002) funded by Korea Research Foundation, and Sogang University Research Grant of 2011.

## References

[1] W.M.P. van der Aalst, Formalization and veri<sup>fi</sup>cation of event-driven process chains, Information and Software Technology 41 (1999) 639–650.

[2] J.C. Anderson, H. Håkansson, J. Johanson, Dyadic business relationships within a business network context, Journal of Marketing 58 (1994) 1–15.

[3] A. Ankolekar, M. Paolucci, K. Sycara, Towards a formal veri<sup>fi</sup>cation of OWL-S process models, in: Y. Gil, E. Motta, V. Benjamins, V.M. Musen (Eds.), The Semantic Web — ISWC, Springer, Berlin, 2005, pp. 37–51.

[4] M. Arns, M. Fischer, P. Kemper, C. Tepper, Supply chain modelling and its analytical evaluation, Journal of the Operational Research Society 53 (2002) 885–894.

[5] F. Baader, I. Horrocks, U. Sattler, Description logic, in: F. van Harmelen, V. Lifschitz, B. Porter (Eds.), Handbook of Knowledge Representation, Springer, Berlin, 2007, pp. 135–179.

[6] B.M. Beamon, Supply chain design and analysis: models and methods, International Journal of Production Economics 55 (1998) 281–294.

[7] J. Becker, R. Knackstedt, A. Stein, Extending the supply chain operations reference model: potentials and their tool support, ECIS 2007 Proceedings, Paper 123, 2007.

[8] K. Burgess, P.J. Singh, R. Koroglu, Supply chain management: a structured literature review and implications for future research, International Journal of Operations & Production Management 26 (2006) 703–729.

[9] I.J. Chen, A. Paulraj, Towards a theory of supply chain management: the constructs and measurements, Journal of Operations Management 22 (2004) 119–150.

[10] P.D. Cousins, B. Lawson, B. Squire, Supply chain management: theory and practice — the emergence of an academic discipline? International Journal of Operations & Production Management 26 (2006) 697–702.

[11] S. Croom, P. Romano, M. Giannakis, Supply chain management: an analytical framework for critical literature review, European Journal of Purchasing & Supply Management 6 (2000) 67–83.

[12] R.M. Dijkman, M. Dumas, C. Ouyang, Semantics and analysis of business process models in BPMN, Information and Software Technology 50 (2008) 1281–1294.

[13] M.L. Fisher, What is the right supply chain for your product? Harvard Business Review 75 (1997).105-116

[14] B.J. Gibson, J.T. Mentzer, R.L. Cook, Supply chain management: the pursuit of a consensus de<sup>fi</sup>nition, Journal of Business Logistics 26 (2005) 17–25.

[15] S. Gonnet, M. Vegetti, SCOntology: a formal approach toward a uni<sup>fi</sup>ed and integrated view of the supply chain, in: M.M. Cunha, B.C. Cortes, G.D. Putnik (Eds.), Adaptive Technologies and Business Integration: Social, Managerial and Organizational Dimensions, IGI Global, Hershey, 2007, pp. 137–158.

[16] A. Gunasekaran, E.W.T. Ngai, Build-to-order supply chain management: a literature review and framework for development, Journal of Operations Management 23 (2005) 423-451

[17] A. Hevner, S. March, J. Park, S. Ram, Design science in information systems research MIS Ouarterly 28 (2004) 75-105

[18] C. Hicks, T. McGovern, C.F. Earl, Supply chain management: a strategic issue in engineer to order manufacturing, International Journal of Production Economics 65 (2000) 179–190.

[19] S.H. Huan, S.K. Sheoran, G. Wang, A review and analysis of supply chain operations reference (SCOR) model, Supply Chain Management 9 (2004) 23–29.

[20] D.M. Lambert, M.C. Cooper, Issues in supply chain management, Industrial Marketing Management 29 (2000) 65–83

[21] G. Liberopoulos, Y. Dallery, A uni<sup>fi</sup>ed framework for pull control mechanisms in multi-stage manufacturing systems, Annals of Operations Research 93 (2000) 325–355.

[22] J. Lee, G.M. Wyner, B.T. Pentland, Process grammar as a tool for business process design, MIS Quarterly 32 (2008) 757–778.

[23] A. Lockamy, K. McCormack, Linking SCOR planning practices to supply chain performance: an exploratory study, International Journal of Operations & Production Management 24 (2004) 1192–1218.

[24] J. Mendling, H.M.W. Verbeek, B.F. van Dongen, W.M.P. van der Aalst, G. Neumann, Detection and prediction of errors in EPCs of the SAP reference model, Data and Knowledge Engineering 64 (2008) 312–329.

[25] J.T. Mentzer, W. DeWitt, J.S. Keebler, S. Min, N.W. Nix, C.D. Smith, Z.G. Zacharia, De<sup>fi</sup>ning supply chain management, Journal of Business Logistics 22 (2001) 1–25.

[26] P.-A. Millet, P. Schmitt, V. Botta-Genoulaz, The SCOR model for the alignment of business processes and information systems, Enterprise Information Systems 3 (2009) 393–407.

[27] T. Moyaux, P. McBurney, M. Wooldridge, A supply chain as a network of auctions, Decision Support Systems 50 (2010) 176–190.

[28] J. Olhager, Strategic positioning of the order penetration point, International Journal of Production Economics 85 (2003) 319–329.

[29] B.T. Pentland, Process Grammars: A Generative Approach to Process Redesign, Working Paper Series 178, MIT Center for Coordination Science, Cambridge, MA, 1994.

[30] B.T. Pentland, Grammatical models of organizational processes, Organization Science 6 (1995) 541-556.

[31] D. Rodríguez, E. García, S. Sánchez, De<sup>fi</sup>ning software process model constraints with rules using OWL and SWRL, International Journal of Software Engineering and Knowledge Engineering 20 (2010) 533–548.

[32] A. Röder, B. Tibken, A methodology for modeling inter-company supply chains and for evaluating a method of integrated product and process documentation, European Journal of Operational Research 169 (2006) 1010–1029.

[33] O. Sakka, P.-A. Millet, V. Botta-Genoulaz, An ontological approach for strategic alignment: a supply chain operations reference case study, International Journal of Computer Integrated Manufacturing 24 (2011) 1022–1037.

[34] S. Stephens, Supply chain operations reference model 5.0: a new tool to improve supply chain ef<sup>fi</sup>ciency and achieve best practice, Information Systems Frontiers 3 (2001) 471–476.

[35] G. Steward, Supply-chain operations reference model (SCOR): the <sup>fi</sup>rst cross-industry framework for integrated supply chain management, Logistics Information Management 10 (1997) 62–67.

[36] Supply-Chain Council, Supply Chain Operations Reference Model (SCOR®), Version 9.0, Washington DC, 2009.

[37] C.J. Vidal, M. Goetschalckx, Strategic production–distribution models: a critical review with emphasis on global supply chain models, European Journal of Operational Research 98 (1997) 1–18.

[38] W3C, OWL web ontology language, W3C recommendation 10 February 2004, http://www.w3.org/TR/owl-ref/, (accessed on April 12, 2012)

[39] W3C, SWRL: a semantic web rule language combining OWL and RuleML, W3C Member Submission 21 May 2004, http://www.w3.org/Submission/SWRL/.

[40] Y. Wand, R. Weber, Information systems and conceptual modeling — a research agenda, Information Systems Research 13 (2002) 363–376.

[41] W.Y.C. Wang, H.K. Chan, D.J. Pauleen, Aligning business process reengineering in implementing global supply chain systems by the SCOR model, International Journal of Production Research 48 (2010) 5647–5669.

[42] M. Zdrayković H. Panetto M. Trajanović A. Aubrey, An approach for formalising the supply chain operations. Enterprise Information Systems 5 (2011) 401–421.

Joerg Leukel is a Senior Researcher and Lecturer in the Department of Information Systems 2 at the University of Hohenheim, Stuttgart, Germany. He obtained a PhD in Information Systems from the University of Duisburg—Essen, Germany. His research interests focus on inter-organizational information systems, supply chain management, ontologies, and service-oriented computing. Joerg has published in journals including IEEE Systems Journal, Knowledge and Information Systems, and International Journal of IT Standards and Standardization Research.

Vijayan Sugumaran is Professor of Management Information Systems in the Department of Decision and Information Sciences at Oakland University, Rochester, Michigan, USA, and WCU Visiting Professor at Sogang University, Seoul, Korea. He received his Ph.D. in Information Technology from George Mason University. His research interests are in the areas of Service Systems, ontologies and Semantic Web, intelligent agent and multi-agent systems, and component-based software development. Vijayan has published in top journals including Information Systems Research, ACM Transactions on Database Systems, IEEE Transactions on Engineering Management, and Communications of the ACM. He is the editor-in-chief of the International Journal of Intelligent Information Technologies and also serves on the editorial board of seven other journals.
