---
otero_id: 26637
otero_key: "DXTM5SXJ"
title: "Heuristics for Reconciling Independent Knowledge Bases"
authors: "Andrew Trice; Randall Davis"
year: "1993"
journal: "Information Systems Research"
doi: "10.1287/isre.4.3.262"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.255.6.125] On: 16 September 2016, At: 01:50 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## H4R

![](/api/attachments/DXTM5SXJ/fulltext/images/1c7173d546b07b65de2e01e325d9c0ee8aa730d56f852a2a6475089e102aa98e.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Heuristics for Reconciling Independent Knowledge Bases

Andrew Trice, Randall Davis,

## To cite this article:

Andrew Trice, Randall Davis, (1993) Heuristics for Reconciling Independent Knowledge Bases. Information Systems Research 4(3):262-288. http://dx.doi.org/10.1287/isre.4.3.262

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1993 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/DXTM5SXJ/fulltext/images/3710fdabc6a407cd78facd982923c9d42340b3afb8f2259cac824259fcac1a5b.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Heuristics for Reconciling Independent Knowledge Bases

Andrew Trice

Faculty of Commerce and Business Administration

2053 Main Mall, University of British Columbia

Vancouver, BC Canada V6T 1Z2

Randall Davis

MIT Artificial Intelligence Laboratory

545 Technology Square

Cambridge, MA 02139

One of the major unsolved problems in knowledge acquisition is reconciling knowledge originating from different sources. This paper proposes a technique for reconciling knowledge in two independent knowledge bases, describes a working program built to implement that technique, and discusses an exploratory study for validating the technique. The technique is based on the use of heuristics for identifying and resolving discrepancies between the knowledge bases. Each heuristic developed provides detection and resolution procedures for a distinct variety of discrepancy in the knowledge bases. Sample discrepancies include using synonyms for the same term, conflicting rules, and extra reasoning steps. Discrepancies are detected and resolved through the use of circumstantial evidence available from the knowledge bases themselves and by asking sharply focussed questions to the experts responsible for the knowledge bases. The technique was tested on two independently developed knowledge bases designed to aid novice statisticians in diagnosing problems in linear regression models. The heuristics located a significant number of the discrepancies between the knowledge bases and assisted the experts in creating a consensus knowledge base for diagnosing multicollinearity problems. We argue that the task of identifying discrepancies between independent bodies of knowledge is an inevitable part of any large knowledge acquisition effort. Hence the heuristics developed in this work are applicable even when knowledge acquisition is not done by reconciling two complete knowledge bases. We also suggest that our approach can be extended to other knowledge representations such as frames and database schemas, and speculate about its potential application to other domains involving the reconciliation of knowledge, such as requirements determination, negotiation, and design.

Knowledge acquisition—Consensus formation—Expert systems—Conflict resolution

## 1. Introduction

he problem of achieving a consensus opinion among a group has been studied extensively in management science and other fields (Helmer and Rescher 1959,

Hammond and Adelman 1976, Libby et al. 1987). With expert systems technology coming into wide use, developers of knowledge-based systems now face a new and important problem of this type, namely capturing the knowledge of multiple sources (typically experts) in a single, consensus knowledge base (CKB). The process by which experts interact to construct a CKB is called “consensus knowledge acquisition" (CKA). This paper proposes a technique for facilitating CKA, describes a working program built to implement that technique, and discusses an exploratory study for validating the technique.

## 1.1. Significance of Work

Commentators in both artificial intelligence (Mittal and Dym 1985, Davis 1982) and information systems (Fellers 1987) have identified CKA as an important research problem. There are three main rationales for the significance of CKA.

First, knowledge in organizations is inevitably distributed among multiple experts but most techniques and tools for knowledge acquisition focus on codifying the knowledge of a single individual. Multi-expert acquisition techniques that have been proposed address at best a very small portion of the CK A process, typically ignoring the difficult problem of determining where the experts agree and where they differ.

Second, as researchers and developers become more familiar with expert systems technology, they aspire to construct ever larger systems. Efforts at building very large-scale knowledge bases (e.g., Lenat and Guha 1989) have shown that the process of building such a system unavoidably involves large numbers of knowledge engineers and experts working for extended periods of time. Although efforts can be made to partition the task to limit the interaction between different parties, constructing such systems still requires methods for agreeing on shared terminology and reasoning. In addition, because such systems require extended time periods to build, the problem arises even if built based on the knowledge of a single expert: that expert must “agree with him/herself" over time (the expert may have one name for a concept at one point in time and use a slightly different name later on, yet mean the same thing by it.)

Finally, while the immediate focus of this article is on a specific knowledge acquisition task, results from this work also suggest possibilities for providing assistance in a number of other situations requiring consensus formation, which is a generic coordination task (Malone and Crowston, 1990). Many different situations require that we identify, explain, and reconcile differences in the reasoning used to make a decision. The problem arises in negotiation (e.g., bargaining between labor and management), legal disputes (e.g., arbitrating the amount of an award in a tort case), and organizational decision-making (e.g., deciding on a strategic plan), as well as in more traditional software development (e.g., agreeing on requirements specifications). Because it is a relatively well-specified consensus-building task, CKA is a good context for identifying consensus-building techniques that may have more general applicability.

## 1.2. The Central Idea

The key theme in the work presented here is that the structure provided by a particular knowledge representation can be exploited to assist experts in reaching consensus. To see how this is possible, imagine two experts' judgments on a specific issue (e.g., likelihood of a student's success at a university) and assume that they are represented as weighted combinations of cue variables (e.g., grade point average in high school, standardized test scores). If the experts' final judgments conflict, they may find it very useful to analyze the different results by examining the disparities in how they used the cue variables to make the judgment. For example, they might find that they reported different answers because they weighted one of the cues differently, or related a cue and a judgment using different functional forms. In this case, the representation in use provides a structure within which the experts can have a substantive discussion about why they disagreed. Exploring differences in knowledge in effect “sets the agenda" for discussion.

This paper applies this notion to support the construction of CKBs, by developing representation-specific heuristics for matching up and reconciling individual knowledge bases. These heuristics were identified through an examination of a particular production rule representation language. The heuristics were then tested by developing a system that implements the heuristics and conducting an experiment in which that system was used to reconcile two knowledge bases written in the representation. We offer this work as a first empirical test of our ideas about CKA.

## 1.3. Outline

We begin with an overview of the literature on knowledge engineering techniques for creating community knowledge bases. We then describe the methodology used in the present work and the system built to implement it, and present the results of an exploratory study that tested our technique. Finally, we examine the implications, limitations, and contributions of this research.

## 2. Related Work

Techniques for taking advantage of the knowledge of multiple experts have been with us for quite some time. For the sake of brevity, we focus here on techniques that have been used within the scope of expert systems and knowledge engineering. For a review of those applied outside of AI, see Libby et al. 1987, Delbecq 1971, Helmer and Rescher 1959, Hammond and Adelman 1976, and Trice 1990 for a summary of the work.

Interestingly, multiple experts have contributed to the construction of knowledge bases since the earliest efforts in expert systems, including DENDRAL (Lindsay et al. 1980) and MYCIN (Davis et al. 1977). The originators of these systems realized that a knowledge-based system could be understood as a medium of communication among experts building a theory of the domain as well as a problem-solving or consultation system. The focus of this early work was, understandably, on the representation of knowledge that led to high performance rather than the process of resolving conflicts among multiple experts. This community aspect of knowledge bases has been the focus of more recent commentaries that view the technology as a tool for facilitating a dialogue of evolving understanding among experts (Winograd and Flores 1986, Stéfik 1986).

As the use of expert systems has proliferated, CK A has begun to be recognized as an important problem (Mittal and Dym 1985, Fellers 1987, Davis 1982). However, to this point the literature on CK A is still small and rather fragmented. A few papers suggest outcome-based approaches, that is, techniques that combine the final judgments of multiple experts according to some formula (Gaglio et al. 1985, Aczel and Saaty 1983). Another advocates an adaptation of the Delphi technique (Jaganathan and Elmaghraby 1985). Some researchers have used the functions provided by group decision support system (GDSS) tools (e.g., brainstorming, voting) to support a CK A process (Lipp 1989, Liou and Nunnamaker 1990), while others suggest facilitated meetings between experts to resolve conflicts and pool information (Cung and Ng 1989, McGraw and Seale 1988).

A number of CK A efforts have taken place in the work based on the repertory grid notion (Boose 1986, Shaw and Gaines 1987, Shaw and Woodward 1988, Gaines and Shaw 1989). A repertory grid is a matrix in which the columns typically represent choices (e.g., investments) an expert wishes to distinguish between and the rows represent attributes of those choices (e.g., degree of riskiness). Each cell in the matrix represents an expert's numeric rating of a particular choice with respect to an attribute. For example, “commodities" may be given a rating of 6 on a scale of 1 to 7 on its "degree of riskiness." Efforts to facilitate CKA through the use of the grids focus primarily on comparing and exchanging grids elicited from different experts and from using the differences as a basis for negotiation.

Related work is found in the effort to build decision capture tools, programs that focus on helping group members deliberate by providing aids for representing and manipulating the logical structure underlying a decision. SIBYL (Lee 1990), for example, provides a language and a set of graphical objects for showing the connections between decision goals, alternatives, and claims. Users can also evaluate the impact of changing an assumption on the desirability of an alternative. Other tools in the same vein include Lowe, 1985; Conklin and Begeman, 1988; and Stefik et al., 1987.

Each of the approaches above has significant limitations. The outcome-based approaches ignore the possibility that the experts could achieve consensus on the reasoning used to determine the outcomes, rather than simply agreeing on outcomes. (Agreeing on the reasoning has the obvious benefit that the same disagreement will not reoccur when the system is used in the future.) Outcome-based approaches are thus most useful when the experts responsible for the judgments cannot reach agreement on the reasoning or are unavailable.

The Delphi approach, while allowing examination of the reasoning underlying a decision, is entirely dependent on the skills of a human facilitator to compare the reasoning and feed back this analysis to the experts. The GDSS and facilitation approaches may support idea generation and ranking in the early phases of group knowledge acquisition process, but provide no specific tools for analyzing, comparing and reconciling knowledge structures (e.g., rules created by different experts).

The repertory grid approach provides a certain degree of context for discussion among experts, but provides no guidance for the resolutions of conflicts that are identified.

Finally, tools for representing the logic underlying a decision provide some useful structure for deliberation, structure that could be used in exactly the manner shown in this paper. To date, however, no such use has been reported.

To this point, the research on CK A has had little impact on the practice of CKA. Expert system developers often use multiple experts for KB construction, but do not use systematic techniques for resolving discrepancies in their knowledge. Developers do have the option of eliciting a KB from one expert and validating it by having other experts critique it (Benbasat and Dhaliwal 1989), but there is little guidance available for doing this systematically. In other cases developers elicit a KB from multiple experts, but appoint one of the experts as “knowledge czar," thereby giving that person the final word in any dispute (Sviokla 1986). Both of these approaches are simply ways of assigning roles or levels of influence to different experts, rather than systematic procedures for identifying and resolving substantive conflicts in their knowledge.

![](/api/attachments/DXTM5SXJ/fulltext/images/e07e86c4918fe06407c1028351d66ada3de39b2c933d916022285b23d62498c8.jpg)  
FIGURE 1. CARTER Scenario

## 3. CARTER, A System Employing Representation-specific Heuristics

Our approach to CK A uses the structure provided by a representation to develop representation-specific heuristics for reconciling independently created knowledge bases. To test the utility of this approach, we developed CARTER', a prototype program that assists in the reconciliation of two knowledge bases expressed in rules.

## 3.1. CARTER's Task

CARTER (Figure 1) takes as input two knowledge bases written to address the same problem and expressed in a particular form of production rules, as described below. Using its heuristics, it examines the constructs in each knowledge base, looks for discrepancies between them, decides which discrepancy to try to resolve, and suggests possible resolutions. The two experts² responsible for the KBs discuss the suggested resolutions and can choose to update their KBs as suggested, update them in some other manner, or not update them at all. This cycle repeats until either the two KBs agree exactly, yielding a consensus KB, or until no new discrepancies can be found.

Since we are concerned with CK A we begin at the point in the system construction process at which two knowledge bases have been developed independently, but the experts have not yet attempted to reconcile them. Our focus is on reconciling the knowledge, rather than having to elicit it from the expert. In addition, our approach assumes that the application domains for which the KBs are written are well suited for the knowledge representation we use. Otherwise, differences between the KBs will reflect different approaches to finessing shortcomings in the representation rather than genuine discrepancies in domain knowledge.

```txt
<Knowledge Base> ::= <Rule> | <Rule> <Knowledge Base>
<Rule> ::= IF <Premise> THEN <Conclusion>
<Premise> ::= <PremiseClause> | <PremiseClause> AND <Premise>
<Conclusion> ::= <ConclusionClause>
<PremiseClause> ::= ( <attribute> of <object> is <value> )
<ConclusionClause> ::= ( <attribute> of <object> is <value> ) |
(<attribute> of <object> is <value> <CF>)
<attribute>, <object>, and <value> are alphanumeric strings;
<CF> is a decimal between 0 and 1.
```  
FIGURE 2. BNF Form of Knowledge Bases.

Note also that the intent of our system is not to resolve the knowledge bases automatically, since this would require its own large body of domain expertise. Instead we are attempting to provide intelligent suggestions to the experts and knowledge engineers about where the knowledge bases match, where they conflict, and how to resolve the discrepancies.

## 3.2. Knowledge Representation Used by CARTER

The KBs CARTER operates on are expressed in a simplified version of production rules (Davis et al. 1977). A BNF structure for this rule language is shown in Figure 2.

The usage of this rule language is illustrated by the examples below, taken from the statistical KBs used in the empirical test of CARTER (§5.1).

(1) Facts about the world are represented as  attribute (of) object (is) value triples.

Example fact:

the Defect of Model is Heteroscedasticity.

This fact states that the a linear regression model has a defect, specifically heteroscedasticity (i.e., unequal variance of the residuals of the model).

(2) IF-THEN rules specify the connections between these fats; when the facts in the premise part of a rule hold, we may make the assertion shown in the conclusion part.

Example rule:

IF the Defect of Model is Heteroscedasticity

THEN the Next-Step of Analysis is Transform.

This rule states that if the regression model has problems with heteroscedasticity, then the next thing to be done is to transform the data in some fashion to remove the heteroscedasticity.

(3) Inexactness in the reasoning is represented by certainty factors in the conclusion of a rule.

Example: The rule above is in fact not absolutely certain; hence a more accurate version of it is

IF the Defect of Model is Heteroscedasticity

THEN the Next-Step of Analysis is Transform .7

Two factors made this representation appropriate for our initial efforts: rules are the representation most frequently employed to develop knowledge based systems, and the form of rule language we chose provided a relatively simple framework within which to compare bodies of knowledge.

<table><tr><td>PROBLEMS of KB1 matches DEFECT of KB2</td></tr><tr><td>Although the names do not match,the domain of PROBLEMS of KB2 andthe domain of DEFECT of KB2 matchValues in common are: MULTICOLLINEARITY HETEROSCEDASTICITYValues only KB1 has are:Values only KB2 has are:The attributes share the common object MODEL</td></tr><tr><td>In addition, the following related attributes also match: DETERMINANT</td></tr><tr><td>The most plausible cause of this difference is that PROBLEMS and DEFECT are synonyms.</td></tr><tr><td>The program is now going to try to help you consolidate PROBLEMS and DEFECT:</td></tr><tr><td>What is the relationship between these two concepts?1) They are essentially different concepts; the program made a mistake2) They are essentially identical concepts; you&#x27;d like to resolve them now3) You are not sure how they relate; you&#x27;d like to look at them more offline.Response: 2</td></tr><tr><td>What are you going to call this concept? problems</td></tr><tr><td>Fine. The program will change the attribute name in the KBs now.</td></tr><tr><td>FIGURE 3. Sample CARTER Dialogue.</td></tr></table>

## 3.3. Implementation of CARTER

CARTER was developed in Common Lisp and has a command-line interface, with all dialogue generated from simple templates. A sample interaction is provided in Figure 3. First, the system identifies a discrepancy—it has concluded that two attributes in the KB's with the same name, Problem and Defect, in fact refer to the same concept by different names. Second, it provides the evidence used to draw that conclusion—Problem and Defect, though they have different names, are used in the KBs in very similar ways. Third, the system helps the experts resolve the discrepancy by allowing them to enter a shared name for the concept. We now discuss the reconciliation techniques that underlie CARTER.

## 4. Reconciliation Methodology

To be successful, CARTER must know about a wide variety of discrepancies that can occur. In addition, it must have procedures for detecting and resolving these discrepancies. Therefore, the key task in this work was to develop a discrepancy catalog for CARTER that categorizes discrepancies and specifies how each can be detected and resolved. A secondary task is to develop a strategy for ordering the discrepancies between two KBs. The purpose of this section is to describe how these tasks were accomplished for this specific representation, and what the results of this process were.

As shown in Table 1, the development of each component of the reconciliation methodology was guided by one or more fundamental principles. To categorize discrepancies, we use descriptions of knowledge structures in the representation to enumerate a space of discrepancies. To develop discrepancy detection procedures, we used circumstantial evidence in the KBs and focussed questions to the experts. To find discrepancy resolution procedures, we identified a set of generic resolution categories. To develop a strategy for ordering discrepancies, we used several heuristics believed to make the reconciliation process focussed, coherent, and efficient. As described in §6.1, we believe that these principles can also be applied to other knowledge representations besides production rules.

Heuristics for Reconciling Independent Knowledge Bases  
TABLE 1

<table><tr><td colspan="2">Principles Underlying Development of Reconciliation Methodology</td></tr><tr><td>Reconciliation Task</td><td>Fundamental Principles</td></tr><tr><td>Discrepancy Categorization</td><td>Employ descriptions of knowledge structures to enumerate a space of discrepancies</td></tr><tr><td>Discrepancy Detection</td><td>Use circumstantial evidence in KBs, focussed questions</td></tr><tr><td>Discrepancy Resolution</td><td>Identify generic resolution categories</td></tr><tr><td>Ordering Strategy</td><td>Compare corresponding parts of KBs, establish agreement on vocabulary first, resolve easy discrepancies first</td></tr></table>

We have enumerated these principles to provide a basis for judging the likely depth and breadth of applicability of our work. Given the nature of our work—an empirical undertaking, rather than a formal analytical task—it is not possible at this stage to formally prove that our methodology is either complete or optimal. For example, we cannot show that our discrepancy catalog includes all possible discrepancies that can be found between two production rule systems. While KBs are collections of symbols structured in a manner constrained by the formal syntax of the representation, this formal syntax neither defines or generates the discrepancies; rather, differences in the design choices or expertise of humans produce them. For example, different experts sometimes refer to the same concept by different names, or create rules that appear to arrive at contradictory conclusions but in fact are both overgeneralized. These discrepancies are empirical observations about how people represent knowledge or perceive the world differently, not formal properties of the representation being used. The representation provides structure that is very useful for categorizing and detecting discrepancies, but its formal description is not the sole means ofidentifying them.

Similar observations apply to the detection procedures, resolution procedures, and ordering strategies we developed. Where a theoretical basis from previous work was lacking, we adopted approaches that appeared promising and then subjected those approaches to an empirical test.

## 4.1. Discrepancy Categories

While the completeness of the discrepancy catalog cannot be proved, we can still identify discrepancies using a systematic method that reduces the chance of missing any obvious ones. Our method was to determine the dimensions by which each kind of knowledge structure in the representation could be described, and then exhaustively enumerate every way that two knowledge structures of this type could differ with respect to these dimensions. This method ultimately resulted in the identification of three fundamental types of knowledge structures—vocabulary, knowledge base topology, and rule content-along with various discrepancies involving each type.

4.1.1. Vocabulary Discrepancies. One fundamental underpinning of any representation is the terminology—the primitive vocabulary terms—that are used. In the current representation any vocabulary term in a KB is fully described by its name, its role in a fact (i.e., an attribute, an object, or a value), and its meaning. Since any two terms can be either the same or different with respect to these three dimensions, there are $2 ^ { 3 } = 8$ relationships that are possible, some of which constitute discrepancies and some of which do not (Table 2).

Trice • Davis  
TABLE 2  
Possible Relationships Between Two Vocabulary Terms

<table><tr><td>Case#</td><td>Name</td><td>Role</td><td>Meaning</td><td>Discrepancy?</td><td>Comments</td></tr><tr><td> $V_1$ </td><td>S</td><td>S</td><td>S</td><td>No</td><td>Terms are identical</td></tr><tr><td> $V_2$ </td><td>S</td><td>S</td><td>D</td><td>Yes</td><td>Same name, different meaning</td></tr><tr><td> $V_3$ </td><td>S</td><td>D</td><td>S</td><td>Yes</td><td>Same meaning, different role</td></tr><tr><td> $V_4$ </td><td>D</td><td>S</td><td>S</td><td>Yes</td><td>Terms are synonyms</td></tr><tr><td> $V_5$ </td><td>D</td><td>D</td><td>S</td><td>Yes</td><td>Composite of  $V_3$  and  $V_4$ </td></tr><tr><td> $V_6$ </td><td>S</td><td>D</td><td>D</td><td>Yes</td><td>Composite of  $V_2$  and  $V_3$ </td></tr><tr><td> $V_7$ </td><td>D</td><td>S</td><td>D</td><td>No</td><td>Same role, but clearly distinct concepts</td></tr><tr><td> $V_8$ </td><td>D</td><td>D</td><td>D</td><td>No</td><td>No connection between terms</td></tr></table>

(S = same, D = different)

Five categories of vocabulary discrepancy are evident from Table 2. In Case $\mathbf { v } _ { 2 } ,$ the terms have the same name and roles but different meanings; in Case $\mathbf { v } _ { 3 } ,$ , the terms have the same name and meanings, but are represented differently (e.g., one expert represents it as an object, the other as an attribute), and in Case $\bf { V _ { 4 } } ,$ the terms have the same meanings and roles but different names. In Case $\mathbf { v } _ { \mathsf { s } } ,$ , terms have the same meaning, but different names and roles; in Case $\mathbf { v _ { 6 } }$ , the terms have the same name, but different roles and meanings.

In addition to discrepancies between two terms, there is also the discrepancy in which there is a term in one KB representing a concept absent from the other KB. Note also that some categories of discrepancy, such as $\mathbf { v } _ { \mathsf { s } }$ and $\mathbf { V _ { 6 } }$ in Table 1, are composite discrepancies, in that the terms differ in more than one dimension. While these are included in the catalog for completeness, in practice they appear less frequently than discrepancies in which the terms differ in only one dimension.

Table 3 shows the most general categories of discrepancies that occur. We can often further subdivide these into more specific kinds of discrepancies. In the case of vocabulary, for example, Case $\mathbf { V } _ { 2 }$ (same name, different meaning) can occur in three ways: between two objects, two attributes, or two values. The subcategory provides additional guidance to the resolution procedures. Similarly, Case $\mathbf { V _ { 4 } }$ (synonyms) can be subdivided into three types, since it can occur between for attributes, objects and values. Finally Case $\mathbf { V } _ { 3 }$ (same name and meaning, different role) can be subdivided into three types: object-attribute pairs, attribute-value pairs, and object-value pairs.³

4.1.2. Topology Discrepancies. A second kind of structure, derivable from the vocabulary and the rules in which they are used, is the topology, or pattern of inference, in the KBs. Since any rule links values of attributes in its premise with values of the attribute in its conclusion, we can view a rule as a link in a directed graph in which the attributes are the nodes (see Agarwal and Tanniru, 1992, for a more formal treatment of this idea). For example, in one of the statistical knowledge bases, two rules used the Determinant of the coefficients in the regression model to determine whether Multicollinearity-Problems were detected in the model. This small segment of the topology of the knowledge base is represented as

![](/api/attachments/DXTM5SXJ/fulltext/images/dabb82098f7b5c1fe4816a06a0aaba207a0b59cf91fd72a9a0e6c01acd91cb2d.jpg)  
FIGURE 4. Topology of a Knowledge Base.

$$
\text { Determinant } \rightarrow \text { MultiCollinearity - Problems. }
$$

Note that in drawing topologies we use a single link to represent one or more rules linking the same attributes.

In a complete knowledge base, the originating nodes of the graph (those with no links/rules heading into them) represent the attributes whose values must be provided by the user; the nodes in the middle represent the intermediate attributes used in the reasoning process; while terminating nodes represent the attributes whose values we are seeking to determine as the outcome of the reasoning process (see Figure 4).

A KB with N attributes has a topology consisting of a set of relationships between its (N choose 2), or $( N ^ { * } ( N - 1 ) ) / 2 ,$ possible pairs of attributes. The relationship between any attribute pair is in turn described by the following information, which can be accumulated from the individual links in the KB:

(1) The number (N) of distinct paths between them (0 to infinity). A path is a set of one or more successive links (rules). If there are no paths, then the other information is moot.

(2) For each path, its direction (D). This indicates which attribute is the originating node (in the premise of a rule), and which is the terminating node (in the conclusion of a rule).

(3) For each path, its length (L), expressed in the number of links in the path (between 1 and infinity).

(4) For each path of length 1, its cardinality (C). A cardinality of 1 indicates that the value of the originating attribute in the link (in its role in the premise of a rule) uniquely determines the value of the terminating attribute (in its role in the conclusion of a rule). Higher cardinalities indicate that attributes other than the originating attribute are used to determine the its value (as when, for example, there is a conjunction of facts in the premise of a rule.)

Table 3 shows the possible relationships between two attribute pairs. All cases in which the relationship differs constitute topology discrepancies; differences in path existence, number of paths, path direction, path length, and path cardinality.

TABLE 3  
Possible Relationships Between Two Attribute Pairs

<table><tr><td>Case#</td><td>N</td><td>D</td><td>L</td><td>C</td><td>Discrepancy?</td><td>Comments</td></tr><tr><td> $T_1$ </td><td>S</td><td>S</td><td>S</td><td>S</td><td>No</td><td>Identical topology segments</td></tr><tr><td> $T_2$ </td><td>D</td><td>S</td><td>S</td><td>S</td><td>Yes</td><td>Extra link(s) in 1 KB</td></tr><tr><td> $T_3$ </td><td>S</td><td>D</td><td>S</td><td>S</td><td>Yes*</td><td>Paths in diff. directions</td></tr><tr><td> $T_4$ </td><td>S</td><td>S</td><td>D</td><td>S</td><td>Yes</td><td>Paths of diff. lengths</td></tr><tr><td> $T_5$ </td><td>S</td><td>S</td><td>S</td><td>D</td><td>Yes</td><td>Paths of diff. cardinalities</td></tr><tr><td> $T_6$  &amp; above</td><td></td><td></td><td></td><td></td><td>Yes*</td><td>Composite discrepancies</td></tr></table>

As with vocabulary, categories of topology discrepancy can be further subdivided. The difference in path numbers, length, or cardinalities can be equal to 1 or any higher number. As well, composite topology discrepancies are possible, but detected and resolved as a series of more primitive topology discrepancies (i.e. T2, T3, and $T _ { 4 } )$

Note also that the same segment of a topology can contain multiple discrepancies, as in the following segments

$$
\text { R - Squared } \longrightarrow \text { Explanatory - Power } \longrightarrow \text { Quality }
$$

R-Squared →Quality.

Both KBs contain attributes R-Squared, Explanatory-Power, and Quality, but one uses the R-Squared statistic to infer the Explanatory-Power of the model, which in turn infers the Quality of the model, while the other uses R-Squared to infer Quality directly. These segments contain both two cases of $\scriptstyle { T _ { 2 } }$ (the links between R-Squared and Explanatory-Power, and Explanatory-Power to Quality do not exist in the second fragment) and one case of $\pmb { T _ { 4 } }$ (the first path is of length 2, the second of length 1). In cases such as these, it is necessary to formulate a strategy for ordering the discrepancies to be resolved (see §4.4).

4.1.3. Rule Discrepancies. The third fundamental structure in the representation is the rules that link conjunctions of premises with their corresponding conclusions. Since (as we will see) vocabulary and topology are checked first (and, if necessary, repaired), when we compare two rules that connect the same sets of attributes, we can usually assume that the rules are reasoning about the same things, since the terminology in them has been previously agreed upon.

For simplicity, we also assume that the values the attributes take on are discrete. If the KBs are written properly, every possible combination of premise values is covered by a rule (a rule that lacks a value for an attribute can be transformed into a set of equivalent rules, one for each value).

Recall that a rule in this representation consists of a premise (P), a conjunction of attribute-object-value triples; a conclusion (C), a single attribute-object-value triple, and a certainty factor (CF) attached to the conclusion (assumed to have a value of 1 if absent). As Table 4 shows, a rule discrepancy occurs when two rules with the same premises differ in their conclusions, strengths of certainty, or both.

As with vocabulary, our table for rules does not cover the discrepancy in which a rule in one KB is absent from the other.

For rule discrepancies, we were able to categorize the discrepancies still further according to how a particular syntactic difference can be explained. For example, when two rules have the same premises, but different conclusions and certainty factors, we distinguish between discrepancies in which (i) one rule is incorrect; (ii) both rules are valid; (iii) both rules are overgeneralized; (iv) both rules employ values on a scale of insufficient granularity (e.g., three values are used where five are needed); (v) both rules include implicit reasoning steps that must be made explicit and (recursively) reconciled. A subset of these more specific discrepancies apply to each of the other discrepancy categories listed in Table 4 (see Trice 1990, for details).

Heuristics for Reconciling Independent Knowledge Bases  
TABLE 4  
Possible Relationships Between Two Rules

<table><tr><td>Case#</td><td>P</td><td>C</td><td>CF</td><td>Discrepancy?</td><td>Comments</td></tr><tr><td> $R_1$ </td><td>S</td><td>S</td><td>S</td><td>No</td><td>Rules are identical</td></tr><tr><td> $R_2$ </td><td>S</td><td>S</td><td>D</td><td>Yes</td><td>Same conc., diff. CF</td></tr><tr><td> $R_3$ </td><td>S</td><td>D</td><td>S</td><td>Yes</td><td>Same CF, diff. conc.</td></tr><tr><td> $R_4$ </td><td>S</td><td>D</td><td>D</td><td>Yes</td><td>Composite of  $R_2$  and  $R_3$ .</td></tr><tr><td> $R_5-R_8$ </td><td>D</td><td></td><td></td><td>No</td><td>Rules are not comparable</td></tr></table>

## 4.2. Developing Detection and Resolution Procedures

After defining the discrepancy categories for the representation, the next step is to develop detection and resolution procedures for each discrepancy.

4.2.1. Detection Procedures. Discrepancy detection is accomplished by using evidence available from the KBs themselves and information gathered by asking sharply focussed questions of the experts.

Evidence available from the KBs themselves include both names of vocabulary terms and relationships between vocabulary terms. For example, any attribute in a KB has a name, takes on certain values, belongs to an object, and is connected to other attributes through rules. This information provides circumstantial evidence that can be used to determine how concepts in the KBs are related, as illustrated below.

Focussed questions to the experts are necessary when the evidence in the KBs is not sufficient to identify a discrepancy. For example, when two rules are inconsistent, there is no more detailed information about those inferences in the KBs, and thus the system must turn to some external source (the experts) to determine what caused it and how it can be resolved. The utility of the system in this situation is not in its ability to detect a discrepancy independently, but is instead in its ability to ask the experts well-chosen questions that will in turn permit it to determine what is wrong.

A detection procedure for a discrepancy consists of a scheme for weighting evidence in the KBs and/or one or more questions asked of the experts. Because the evidence in the KBs is circumstantial, there is no standard formula for combining it in any particular case. Hence we settled on a conservative approach, weighting each of them roughly equally, assigning a matching score, and comparing this score to an empirical threshold (Trice 1990 contains details). This is plausible in part because we view its task as providing advice for ratification by the experts, rather than coming to conclusions on its own.

4.2.2. Resolution Procedures. Any possible resolution to a discrepancy belongs to one of four general categories. Two of the categories, negation and compromise, resolve structures in the KBs that overlap but are inconsistent. The other two categories, incorporation and elaboration, add structures that are lacking in at least one of the KBs.

![](/api/attachments/DXTM5SXJ/fulltext/images/34892273b3df970bf97e1c04ceda3b6bcc0a46b2de7add30b4f0296794f945b1.jpg)  
FIGURE 5. Growth of the Consensus KB.

A negation resolution occurs when one expert changes something to remove a defect in his KB, after the other expert convinces him that one of his judgments or vocabulary terms is incorrect. A compromise resolution occurs when both experts change their KBs. This is helpful when the experts wish to establish a shared vocabulary or negotiate an intermediate settlement. For instance, the experts may assign different strengths of certainty to a rule (e.g., 0.7 vs. 0.9) and resolve the discrepancy by choosing a strength of certainty of 0.8. An incorporation resolution occurs when one expert adds something to his KB that the other already has (or conversely, that the other should remove). This is useful when one KB has an incomplete set of vocabulary, rules, or test cases (or the other KB has extraneous vocabulary, rules, or test cases). An elaboration resolution occurs when both experts add something to the KBs in order to remove discrepancies not otherwise resolvable by changing either KB individually. For instance, the experts may both need to add an extra attribute to their rules to remove an inconsistency between them.

This framework is useful for identifying various resolutions to a discrepancy. Given any discrepancy in the catalog, we can search for a possible resolution falling into each of the four categories.

Figure 5 shows the four resolution types graphically. The consensus KB is represented by the part of the two KBs that overlap (i.e., pertain to the same situation or concept) and that agree. The regions marked Negation and Compromise correspond to knowledge that overlaps but is in conflict; incorporation refers to knowledge that is in one KB but not the other; elaboration refers to knowledge in neither KB. As the CKA process proceeds and changes to the KBs are made, the area of the consensus KB region increases while the four resolution regions shrink.

Note that resolution procedures vary in their complexity, and always require the assistance of the experts. For example, if the experts agree that they used two different terms to refer to the same concept, the resolution is straightforward; the experts are asked to choose one of the names as the consensus term. Other resolutions require more substantial editing of the knowledge bases; if, for example, a new attribute must be added to the knowledge bases to resolve two inconsistent rules, the experts must examine all other rules of that type to determine whether the new attribute should be included in those as well. See Trice (1990) for the complete list of discrepancy resolutions found.

## 4.3. Examples

We now provide two examples of how the discrepancy detection and resolution process works. In the first example, circumstantial evidence is primarily used to detect the discrepancy, while in the second, diagnostic questions are primarily used.

4.3.1. Using Circumstantial Evidence. Circumstantial evidence is used to help decide whether two terms refer to the same concept. In the statistical knowledge bases. for example, one expert used an attribute labelled Problem, while the other used an attribute labelled Defect , yet it turned out that they in fact referred to the same concept, Four kinds of evidence, available from the knowledge bases themselves, are used in such a case:

• Are the concept names the same? In this case they are not (Problem vs. Defect), but this can of course be an artifact of name choice or (in other circumstances) variations in spelling or abbreviation. Conversely, a match in names is useful evidence but certainly no guarantee of match in meaning.

• Are the values associated with the attributes the same? Here the answer is yes (e.g., both attributes can take on the values of Heteroscedasticity and Multicollinearity).

• Are the objects associated with the attributes? In this case the answer is yes (both are attributes of the obiect Mode1). which is weak evidence of a match.

• Are they inferred from the samé concepts and are they in turn used to infer the same concepts? That is, do the occupy similar places in the local topology of the knowledge base? In this case the answer is yes, because there is another attribute in both knowledge bases, Determinant, which is used to infer the value of both Problem and Defect . Furthermore, both of them are terminating nodes (i.e., the concepts are not in turn used to infer other attributes).

Weighing the evidence in the case at hand, the detection mechanism in this case suggests (correctly) that the two concepts are the same.

Note that any attempt to determine whether two concepts mean the same thing must be based on circumstantial evidence. Even a human attempting the task must rely on clues such as how the terms are labelled and the contexts in which they are used. Humans are of course more successful at matching up the concepts than a system like CARTER, but this is because people are able to draw on more sources of circumstantial evidence. Someone familiar with statistics, for example, might know that in this domain, Problem and Defect are often synonymous. However, no agent (human or automated) performing this task can ever formally guarantee that two concepts represented by two different experts mean the same thing.

4.3.2. Asking the Experts Ouestions. Use of information from the experts for discrepancy detection is illustrated by the problem of inconsistent rules, that is, rules with the same premises but different conclusions, as for example, this pair:4

KB1 IF F-TEST less-than CRITICAL-VALUE THEN QUALITY of MODEL is POOR

KB2 IF F-TEST less-than CRITICAL-VALUE THEN QUALITY of MODEL is FAIR

Notice that while both rules reason from the identical premise (F-TEST less-than CRITICAL-VALUE), they draw two different conclusions (MODEL is POOR vs. MODEL is FAIR). Now, having identified this inconsistency (through a trivial pattern match), the system must determine what caused it. That is, it must determine which category of rule discrepancy listed in §4.1.3 accounts for the inconsistency (e.g., one rule incorrect, both rules overgeneralized, and so forth).

All knowledge representations are based on some set of primitives which they cannot further explain. In rule-based systems the most primitive inference is that produced by a single rule. There is no more detailed information about thát inference in the knowledge base, thus CARTER must ask the experts a series of diagnostic questions.

In this case CARTER knows about six possible explanations that it asks the experts to consider:

(1) One of the rules is incorrect and should be removed.

(2) Both rules are over-generalized as stated: they are both missing an attribute whose value constitutes an important unstated assumption that the experts know but forgot to make explicit.

(3) There is a misunderstanding about the vocabulary: Poor and Fair might be synonyms, hence the rules are actually identical.⁵

(4) There is not really a mismatch because both rules should be in both knowledge bases (each expert forgot one rule that the other remembered).

(5) There is not sufficient precision in the vocabulary terms to differentiate between the two outcomes, e.g., perhaps both experts actually view the model as a borderline case between Poor and Fair, but had to choose one of those two values arbitrarily because no intermediate value (e.g., Mediocre) existed

(6) There is a chain of inference between F-Test and Quality that has not been made explicit in the current KBs and the discrepancy lies somewhere along that chain.

CARTER's questions of this form to the experts aid the experts in determining the correct discrepancy for any rule inconsistency.

## 4.4. Ordering Strategy

The discrepancy catalog defines the heuristics for detecting discrepancies and a set of associated resolutions that can be used to arrive at a consensus knowledge base. However, the catalog does not specify a strategy for ordering the discrepancies; for example, it does not tell us which two concepts should be compared first, or how to compare two sets of rules corresponding to a segment of a topology. This is a significant issue in any two knowledge bases of nontrivial size. An ordering strategy is required to make the consensus-building process focussed and coherent. Such a strategy is defined as a second set of heuristics: heuristics about what should be resolved first when trving to reach consensus. In our system the strategy is built into a set of nested procedures.

CARTER's overall strategy employs three main heuristics (additional details can be found in Trice, 1990). The first heuristic is to establish agreement on the final outcomes of the KBs (the terminating nodes of the topologies), then work backward systematically, achieving consensus between the two topologies one step at a time. That is, first make sure the two systems are attempting to establish the same kind of outcome, then proceed "backward"through the rules from there. This heuristic relies on the principle that two KBs about the same topic are likely to have matching concepts at corresponding places in their topologies (e.g., the ultimate outcomes will match, the attributes one reasoning step back from there are likely to match, etc.).

The second heuristic is to order the analysis of a single step of the directed graphs by searching first for vocabulary discrepancies, then for topology discrepancies, then for rule discrepancies. The heuristic here is that it is sensible to create a shared language (the vocabulary) before discussing how the concepts relate, and then agree on general relationships between the concepts (the topology) before discussing specific cases that the rules cover. For example, after reaching agreement on the vocabulary directly connected to the outcomes, the experts then focus on the patterns of inference that link these nodes to the outcomes. This in turn enables comparison of the specific rules that establish the goal in each KB.

The third heuristic is to order discrepancies within one of these three categories—vocabulary, topology, and rules—by searching for discrepancies that are easy to repair before looking for ones that are harder to repair. For example, in choosing what vocabulary discrepancy to identify next, a synonym discrepancy would be tried before a representation choice discrepancy, because a substantial restructuring of the knowledge bases is required to resolve the latter. This heuristic improves the efficiency of the CKA process because it spares the experts the trouble of considering complicated solutions to problems when a simple one may suffice.

## 5. Empirical Test

After developing the heuristics and implementing them in CARTER, we tested the system using two independently developed KBs. CARTER was used to analyze the knowledge bases and assist the experts in creating a consensus knowledge base.

## 5.1. The Knowledge Bases

The two KBs were designed to assist novice statisticians in diagnosing and repairing problems in applving linear regression models. The two expert systems both test for the validity of the assumptions underlying use of linear regressions (e.g., the assumptions that the independent variables are not correlated). Both systems also suggest alternatives for improving the model where needed, so that linear regression can be appropriately applied (e.g., model transforms, removing an outlying point from the dataset). In the ensuing discussion, the two knowledge bases are referred to as KB1 and KB2.

KB1 contained 32 rules, while KB2 had 54. The rules were expressed in the rule language described below. The attributes, objects, and values used in this rule language were the primitive vocabulary of each system; KB1 had a total of 70 such terms. KB2 had 108. KB1 had been previously built as an MS thesis in 1986 (Stephens 1986): KB2 was developed by providing another expert with a high-level description of the task and àsking him to create his own independent knowledge base. (Trice (1990) contains complete listings of the knowledge bases.)

<table><tr><td colspan="2">Attribute discrepancies (synonyms) in the KBs identified by CARTER:</td></tr><tr><td>Attribute in KB1:</td><td>Attribute in KB2:</td></tr><tr><td>PROBLEMS of REGRESSION</td><td>DEFECT of MODEL</td></tr><tr><td>QUALITY of REGRESSION</td><td>RELATIVE-QUALITY of MODEL</td></tr><tr><td>R.BAR.SO of REGRESSION</td><td>R-SOUARED of MODEL</td></tr><tr><td>HETERO.SOLUTION of REGRESSION</td><td>NEXT-STEP of ANALYSIS</td></tr><tr><td>F.STATISTIC of REGRESSION</td><td>F-TEST of MODEL</td></tr><tr><td colspan="2">Attribute discrepancies (synonyms) in the KBs not identified by CARTER:</td></tr><tr><td colspan="2">COEFFICIENTS.JOINTLY.SIGNIFICANT SIGNIFICANCE of MODELof REGRESSION</td></tr></table>

FIGURE 6.Attribute Discrepancies in Regression KBs

## 5.2. Using CARTER to Analyze the KBs

In the first phase of the analysis, the discrepancy catalog was tested by having CARTER compare corresponding fragments of KB1 and KB2 and search for all discrepancies and matches of all types it could find. (A match is a case in which two terms are identical in both name and meaning. The system can recognize matches as well as discrepancies using circumstantial evidence). For example, to detect any attribute synonyms (attributes with different names but the same meaning), it first compared all goal attributes, then all attributes one reasoning step from the goal, and so forth. No resolutions to discrepancies were attempted during this phase; the goal was to determine how successful the catalog was in simply identifying the discrepancies. The KBs were then searched manually for discrepancies that CARTER had not detected.

We present the findings in two parts: cases in which the system successfully identified both discrepancies and matches in the KBs, and cases in which the system incorrectly inferred overlaps in meaning.

5.2.1. Discrepancies Between the KBs. CARTER located nine vocabulary discrepancies and matches between the two KBs and two topology discrepancies. Its analysis identified five out of six attribute pairs (Figure 6) that were synonyms, four out of nine value pairs (Figure 7) that were synonyms or matches, and zero out of one object pair (Regression and Model) that were synonyms.

The system also correctly identified some vocabulary in the KBs as terms that appeared in one of the KBs but not the other. Specifically, CARTER located 58% (29 out of 50) of the unmatched attributes in the KBs.

CARTER found two cases in which the experts used the same concepts but reasoned with them differently, leading to topology discrepanciès (Figure 8). Case (A) was a Finer Reasoning discrepancy (see Appendix): both experts reasoned from the value of the R.BAR.SQ (R- SQUARED ) statistic to the QUALITY (RELATIVE- QUA-LITY ) of the model, but one expert made the inference indirectly by inferring a value for the EXPLANATORY.POWER of the model from R.BAR.SQ statistic, and then in

Heuristics for Reconciling Independent Knowledge Bases

Value discrepancies (synonyms) and matches in the KBs identified by CARTER:

Value in KB1: Value in KB2:

Identified by CARTER:

PROBLEMS is HETEROSCEDASTICITY DEFECT is HETEROSCEDASTICITY

PROBLEMS is MULTICOLLINEARITY DEFECT is MULTICOLLINEARITY

QUALITY is GOOD RELATIVE-QUALITY is GOOD

HETERO.SOLUTION is LOG.TRANSFORM NEXT-STEP is TRANSFORM

Value discrepancies (synonyms) not identified by CARTER:

QUALITY is BAD QUALITY is POOR

R.BAR.SQ is LT-CRITICAL-VALUE R-SQUARED is RELATIVELY-LOW

R.BAR.SQ is GT-CRITICAL-VALUE R-SQUARED is RELATIVELY-HIGH

F.STAT is EXCEEDS-CRITICAL-LEVEL F-TEST is SIGNIFICANT

F.STAT is BELOW-CRITICAL-LEVEL F-TEST is NOT-SIGNIFICANT

FiGURE 7. Value Discrepancies and Matches in Regression KBs.

turn inferring QUALITY from EXPLANATORY. POWER. Case (B) was an Extra Data Operation discrepancy: the first expert finished by inferring the QUALITY of the model, while the second inferred the RELATIVE - QUALITY of the model, then went on to suggest a NEXT - STEP in the analysis as well. The system successfully detected both topology discrepancies in the KBs.

5.2.2. Incorrect Inferences by CARTER. In some instances CARTER made incorrect inferences about the degree of overlap in the meaning of concepts. The false positives and false negatives had different causes.

The majority of the false positives arose from naming accidents. While it is clearly sensible to pay attention to the names experts use in referring to concepts when attempting to match up the two KBs, in this particular experiment the system gave concept names too much weight. For example, in a number of cases attributes were judged to match because their values matched, and the values in turn matched because they shared common substrings. For instance, COEFFICIENTS .JOINTLY. SIGNIFICANT of KB1 matched with STATUS of KB2 because both attributes had

A) KB1:R.BAR.SQ EXPLANATORY-POWERQUALITY

KB2: R-8QUARED RELATIVE-QUALITY

B) KB1: QUALITY

KB2:RELATIVE-QUALITY NEXT-STEP

FIGURE 8. Topology Discrepancies in Regression KBs.

the substring OK in many of their values. There were fifteen cases of this type, indicating that the system's metrics for matching concepts clearly placed too much emphasis on substring name matches.

There were a significant number of this type of error in these particular KBs because was many of the attributes in the KBs happened to take on general values (e.g., OK-NOT .OK, GOOD-BAD, YES - NO) rather than terms specific to the domain (e.g., HETEROSCEDASTICITY,R-SQUARED).

Only a few false negatives occurred. In six cases, the system did not detect a match between two values that meant the same thing because neither the names nor topology of the values matched. For instance, CARTER did not match up the values BAD and POOR of the attributes QUALITY and RELATIVE-QUALITY because their names did not match and they were not connected to similar values in the KBs through rules.

In summary, CARTER was moderately effective in detecting the discrepancies in the vocabulary and reasoning of the two experts. The system located five out of the six attributes in the KBs that matched, four out of the nine values in the KBs that matched, and the two.topology discrepancies. It also identified 29 of the 50 attributes in the KBs that did not match. Where the system failed to make the correct inference, it was usually due to placing too much faith in substring name matches. It is very easy to change the weights the system assigns to different pieces of evidence, hence trying out a variety of other weighting schemes would not be difficult.

## 5.3. Using CARTER to Create a Consensus KB

In the second phase of the test, the two experts who constructed the knowledge bases were given an opportunity to interact with CARTER to reconcile them. The result was a consensus KB for detecting the problem of multicollinearity, achieved through the mutual incorporation of rules that applied the results of different statistical tests.

The session took place in an office containing a terminal through which the experts interacted with CARTER, a whiteboard for keeping a common record of the discussion, and a personal computer running a statistical analysis package. To introduce them to the system, the experts were shown an example of CARTER resolving two financial planning knowledge bases. They were then allowed to use the system to explore and resolve the differences in their knowledge bases.

As the experts used the system, it quickly became apparent that resolving all the differences between the KBs would require a number of complicated, time-consuming repairs. Because of time limitations, it was decided to focus on gaining agreement on a subset of the two KBs. We chose the subsets that detected the problem of multicollinearity because multicollinearity is a central problem in linear regression models, and because it was a problem that both experts addressed in their KBs in some detail, yet the number of rules to be reconciled was manageable (15 rules in KB1 and 7 rules in KB2),

Once the multicollinearity rules were identified as the focus, the experts were able to create a consensus KB in approximately two and a half hours. In assisting the experts in reaching consensus, CARTER helped the experts identify and repair a total of 15 discrepancies. Eight of these discrepancies were extra attributes found in only one of the knowledge bases; these became attributes in the consensus KB. The primary operation used to build the consensus KB was the mutual incorporation of rules; typically rules applying various statistical tests found in KB1 or KB2, but not both. For example, the experts found that KB1 used the value of the DETERMINANT of the correlation matrix of the independent variables, the NUMBER. OF . VARIABLES in the model, and the combination of the F. STATISTIC and the number of INSIG-NIFICANT.T.STATISTICS, while KB2 uSed the SIGNS, CONDITION-NUM-BERS, and VIFs of the coefficients.

During the session, it was evident that the process of interaction between the experts was primarily one of combining complimentary knowledge, rather than resolving conflicting knowledge. Most of the eight attributes lacking in one KB and added to the consensus KB represented statistical measures that one of the experts was not experienced with interpreting. Each time CARTER identified an attribute found in only one KB, the expert using that attribute explained its purpose, rationale, and interpretation to the other. Typically, the other expert agreed with the need for the attribute and the rules it was used in, and then added this material to his KB.

There was little disagreement between them, and no sign that either attempted to assert control over the contents of the consensus KB. Instead both relied on each other's experience in areas they knew less well. The relative lack of controversy in the consensus formation process was largely due to the lack of conflict (i.e., contradictory knowledge) in the KBs and the differing subspecialties of the individuals involved. It would also be interesting to use the tool in situations where the knowledge bases are more conflicting.

In summary, the consensus KB developed reflected a broader perspective because it used more sources of information than either KB1 or KB2 alone. This is one small yet concrete illustration of the potential payoff of using multiple experts in knowledge acquisition; each expert learned something from what the other had done and incorporated the information in the consensus KB.

After the experiment, the experts were asked for their impressions of CARTER Their comments confirmed our observation that the system was useful for helping them create a CKB that reflected a broader perspective. They also made two suggestions for extending the system, which we will discuss in §7. First, they indicated that the process would have been easier had they had better tools for comparing the problem-solving strategies they used in addition to the domain knowledge expressed directly in the KBs (see §7.3). Second, while they thought CARTER's ordering strategy of beginning at the goal and working backwards was effective, starting at the inputs and working forwards seemed more natural to them (see §7.4).

## 6. Generalizing the Use of Heuristics for Reconciling Knowledge

The preceding results demonstrate how representation-specific heuristics can be used to create a consensus knowledge base of rule-based expertise. However, we suggest that representation-specific heuristics are significantly more broadly applicable. We consider two possibilities for generalizing our approach: developing a discrepancy catalog for another representation, and using representation-specific heuristics to facilitate consensus formation tasks other than CKA.

## 6.1. Creating a Discrepancy Catalog for Another Representation

To see how a discrepancy catalog organized around another representation could be developed, consider the example of decision trees. A discrepancy catalog for this representation could be created by going through the same steps as for rules. First, identify the various elements of the representation: in the case of decision trees, these are things such as alternatives, events, payoffs, and probabilities. Second, develop a taxonomy of how the representations can differ across these elements. For instance, one possible discrepancy is that one expert may have an extra alternative in his decision tree. Third, develop detection and resolution procedures for each of these discrepancies. For instance, the discrepancy just mentioned could be detected using circumstantial evidence (e.g., the name of the extra alternative does not match with any of the alternatives, but belongs to the same decision as other alternatives found in both decision trees) and resolved by adding the extra alternative to the other decision tree. There are also strategy heuristics that could be developed for resolving decision trees; like rules, decision trees have topologies that could be traversed in a systematic fashion to make the consensus formation focussed and coherent.

The ease with which we can begin to apply our approach to this different representation suggests some of the potential breadth of applicability of our approach.

## 6.2. Facilitating Other Consensus-Formation Tasks

Representation-specific heuristics can also be applied to domains other than knowledge acquisition for expert systems. There are indications that this is already occurring. For example, some requirements specification languages, such as PRISM (Ohlsson and Langley 1986) have sufficient structure that a catalog of discrepancies for system requirements has been constructed (Leite and Freeman 1991). In addition, in the domain of labor relations, Sycara (1989) provides a technique for comparing the structure of the positions of each side to suggest compromises. A third example is provided by the work of Klein (1989), whose work focuses on resolving conflicting design specifications in computer-aided design systems. All three of these contributions are very much in the spirit of the approach advocated here: study the representation used by the parties for hints about to organize knowledge about resolving conflicts between knowledge bases. This basic approach appears to work whether the representation is a knowledge representation language, a requirements specification language, a negotiation model, or a design specification.

There is also the potential to use representation-specific heuristics in group support systems (GSS). DeSanctis and Gallupe (1987) discuss how a GSS might provide and apply expert rules for structuring interaction between meeting participants. While the types of rules they suggested primarily concern the interaction process (e.g. deciding who is allowed to speak next and other procedural issues), representation-specific heuristic rules would help address the substance of the interactions. For instance, in a planning meeting in which the participants construct and reconcile cognitive maps (Montazemi and Conrath 1986), representation-specific heuristics could be constructed that suggest why different maps conflict.

## 7. Limitations and Future Work

While the initial results of this work are encouraging, significant work must be done before the practice of consensus knowledge acquisition is well understood and efficient. Some of the research issues discussed below bear directly on the development and performance of representation-specific heuristics, while others are more general CK A design process issues that arose during the test of CARTER. Exploration of these issues will involve construction of new tòols and empirical testing to determine what design choices will lead to superior consensus knowledge bases.

## 7.1. Refining Techniques for Matching up Concepts

Much of what CARTER does falls into the general category of discerning how concepts match in meaning by bootstrapping from the existing KBs, i.e., gathering various pieces of circumstantial evidence in the KBs, assigning a matching score based on a plausible rating function, and comparing this score to an empirical threshold. This method is surprisingly effective, but could be improved in two ways.

First, it would be beneficial to reduce the weight given to matches between terms with general meanings. The results of the test on the statistical KBs showed that the system can be misled into believing that two attributes mean the same thing because of naming coincidences between their values (as we saw in §5.1). One simple solution to this problem would be to compile a list of nonspecific value terms (e.g., Ok, Good, Bad, High, Low) and assign a lower weight to such terms when they appeared in the KBs.

Second, it would be useful to test alternative rating functions on a number of other knowledge base pairs and determine which weightings are most effective on this set on average. Several different weightings have explored in this research thus far; however, more data is needed to improve these weightings.

## 7.2. Exploring Other Ordering Strategies

A second issue is the choice of a strategy for attacking the discrepancies between the experts. For the present work, one strategy was developed and adopted, but a large space of possibilities remains untested. There are three components to any strategy: the direction of traversal of the knowledge bases, the pattern of traversal, and the source of the initiative for conflict resolution.

CARTER's direction of traversal was backward from the terminating nodes (goals) of the knowledge bases. Alternative strategies include working forward from inputs and beginning at any intermediate point of agreement and expanding in both directions.

CARTER's pattern of traversal was to proceed in a breadth-first fashion; it resolves all conflicts at one level of the network before proceeding to the next, back one level. The result is a comparison of each component of the knowledge bases, independent of how these elements would be used in a consultation. By contrast, a depth-first traversal would involve comparing an entire chain of reasoning from each final outcome back to the ultimate inputs that determined it. This results in a comparison that is organized around tracing the reasoning in a specific consultation.

Regarding the source of the initiative in the CKA process, the process can be driven either by the system or by the experts. In CARTER the CKA process was driven almost entirely by the system. Future efforts should also explore allowing the experts more initiative, perhaps by having them begin the CKA process by examining any part of the knowledge base(s) that they desire.

These observations about ordering strategy point to two agenda items for future work. First, tools for CK A should allow developers to employ a variety of traversal techniques. If one kind of traversal does not result in progress towards consensus in a particular situation, it should be easy to attempt another. Second, empirical research is necessary to determine what degree of structure experts need to build consensus most effectively. This would enable prescriptions to be made about how much initiative to leave to the experts and how much should reside with the system.

## 7.3. Comparing Domain Knowledge vs. Comparing Strategic Knowledge

Another important issue to be considered is the kind of knowledge that is compared during the CK A process. When experts solve problems they need to apply not only domain knowledge but a particular diagnostic or problem-solving strategy. For example, a statistician knows that heteroscedasticity can be corrected by performing a transformation on the data (domain knowledge) but arrives at the diagnosis of heteroscedasticity by a process of ruling out all other possible diagnoses by running a series of tests on the data (strategic knowledge).

It is difficult to write production rule systems that clearly distinguish between these two types of knowledge. The rules can be written in a way that both defines the domain knowledge and results in the desired diagnostic strategy; however, the diagnostic strategy is often embedded in the rules in a way that makes it hard for someone not intimately familiar with the system to discern it (Clancey 1983).

The present approach to CK A focussed primarily on comparing domain knowledge, because it compares the rules and attribute, object, value triples in the two knowledge bases. The experts can also use CARTER to discuss some aspects of their diagnostic strategies, by, for example, examining the topologies of their knowledge bases. However, since the representation we used does not capture problem-solving strategies explicitly, CARTER does not compare the relevant strategic knowledge directly. To some extent the experts using CARTER must abstract from the rules in the knowledge bases to reconstruct what their diagnostic strategies were, a process that can be time-consuming.

These observations, our experience in the empirical test, and other empirical evidence that experts use different strategies (Feltovich 1981) suggest that developers of CKBs should give experts an opportunity to discuss and agree on the overall problem-solving approach before diving into the details of reconciling the specific representations such as rules. In addition, future research should focus on developing tools that focus explicitly on comparing strategic knowledge, as a complement to tools like CARTER. These tools could be used in the earlier stages of knowledge base construction, particularly when the problem is still being defined. Tools such as CARTER could then be used in the later stages, when the experts must agree on specific terms and decision rules.

Note, however, that any discussion between experts, whether about domain knowledge or strategic knowledge, must be grounded in a set of terms and other knowledge structures which must be agreed upon. Therefore heuristics for comparing strategic knowledge can in principle be defined as well.

## 7.4. Exploring Other Initial Conditions

By “initial conditions" we mean the amount of work done by the experts prior to any interaction between them. The present approach assumed that the experts had independently constructed two KBs before the start of the CK A process.

There are at least two other kinds of initial conditions in which our approach could be employed. In one possible scenario, only a single KB has been created, representing the knowledge of just one of the experts. The CKA process then consists of the second expert's efforts to critique and enhance this KB in consultation with the first expert (Trice 1990, Lef kowitz and Lesser 1988).

A second scenario assumes that there is no knowledge codified beforehand at all. The experts simply agree on the rules through a face-to-face discussion, without any help from a system like CARTER. In this case, the experts would have to apply the heuristics for resolving conflicts either on their own or with the help of a human facilitator.

Finally, we could of course combine the above approaches. For example, the experts could define only the vocabulary independently, meet to resolve that, then have one expert define the rules based on the consensus vocabulary and have the other expert critique those rules.

For this initial work, we chose the conditions that allowed us the most stringent test of our ideas about consensus knowledge acquisition, namely the situation in which the program could work on the task independently (i.e., it had two complete KBs which it could attempt to reconcile).

The techniques we have developed are also useful in face-to-face discussions between experts. For example, if two experts propose rules that are inconsistent (e.g., have the same premises but different conclusions), they can use the possible explanations identified in our discrepancy catalog as a checklist for determining why they disagreed and resolving the conflict.

One objection to constructing two KBs separately as we have done is that it involves redundant work, especially if the knowledge bases are large. But while largescale knowledge bases will likely not be constructed by reconciling two complete, independently created systems, the techniques we have developed may be even more crucial in this setting. Consider, for example, the case in which one expert has created a substantial knowledge base on a topic and a second expert wishes to enter a concept to it. Whether the two experts use the same terminology or not, it will be very timeconsuming for the second expert to browse through the entire knowledge base to ensure that the concept does not in fact already exist in the knowledge base. It would be much more efficient for the expert to tell the knowledge acquisition tool what he knows about the concept (e.g., its name, what it is used to infer, its possible values) and then have the tool use this circumstantial evidence to search for matches in the existing knowledge base, just as CARTER does now.

The task CARTER does is a task any expert must do when confronted with the task of trying to understand and modify any knowledge base that someone else has created. This task is difficult and intellectually challenging, and therefore, heuristics such as the ones outlined in this paper are likely to provide important assistance to humans doing knowledge engineering in groups.

## 8. Conclusions

This work has produced three results that are useful for developing consensus knowledge bases: a body of knowledge, a set of techniques, and a model. The body of knowledge is the discrepancy catalog, a collection of representation-specific heuristics for reconciling knowledge represented in rules. The set of techniques includes the detection methods for inferring whether concepts in two KBs overlap in meaning using circumstantial evidence in the KBs themselves, asking focused diagnostic questions to identify discrepancies, and presenting the experts with a coherent flow of tasks by ordering the discrepancies to be resolved. The model is a general procedure for using the structure of a representation to develop a taxonomy of discrepancies and repairs for systems expressed in that representation.

## 8.1. The Discrepancy Catalog

The discrepancy catalog developed for rules is a store of detailed information codified for facilitating CK A. It represents a substantial, systematic, and explicit expression of knowledge about how to detect and resolve disagreements in rule-based expertise.

The entries in the catalog were derived mainly from the concepts of rules and attribute-object-value triples provided by the knowledge representation in use. Using this framework made it possible to rapidly uncover a variety of discrepancies in the vocabulary, pattern of inference, and rules of different KBs.

The key insight underlying the discrepancy catalog is that the structure of the representation used to express expertise can itself be used to facilitate consensus formation, even if the tool (or the human facilitator) has no knowledge of the application domain apart from the knowledge bases it attempts to reconcile

## 8.2. Techniques for Facilitating CKA

A primary technique that makes the representation-specific heuristics effective is their detection procedures for inferring whether concepts in the KBs overlap. Other techniques employed include an array of diagnostic questions to help experts determine why rules are inconsistent and an ordering strategy to ensure that the experts are presented with a coherent flow of tasks.

CARTER displays a surprising degree of success in its task of matching concepts in different knowledge bases using circumstantial evidence. It has to make its best guess about whether two terms match based on circumstantial evidence about how the concepts are used in the KBs.

In cases where circumstantial evidence is not sufficient to determine the nature of a difference in knowledge, the system has an array of diagnostic questions it asks the experts. When the system detects two rules in the KBs that are inconsistent, for instance, it inquires whether the problem could be due to the fact that both rules could be correct, one rule could be incorrect, both rules are overgeneralized, and other causes. These questions act as a checklist that helps experts explore all their options for reaching consensus.

Finally, to ensure that the CK A process proceeds smoothly and systematically, a discrepancy ordering strategy with three main heuristics was devised. First, to increase the chances of making intelligent suggestions about where the KBs match up the system begins the CKA process by matching up the goals of the experts and then working backwards. Second, to help the experts build up the agreement at a more refined level, the system first resolves the vocabulary at a level in the directed graph then the topology that connects the vocabulary to the concepts it infers, then the specific rules that makes up the topology. Third, to facilitate the task of identifying and resolving discrepancies, the system first explores discrepancies whose repairs are easy before those whose repairs are more difficult.

## 8.3. A Model for Detecting and Resolving Discrepancies in Knowledge Representations

While the catalog developed in this work removes discrepancies in rules and attribute-object-value triples, similar catalogs can be developed for other kinds of representations as well, as we have shown in §6. For instance, Wagner (1988) provides an example of a taxonomy for resolving different database schemas. It is also possible to catalog discrepancies for frame-based knowledge representation languages such as KL-ONE (Brachman and Sċhmolze 1985). For a brief example, see Trice, 1990. Finally, a recent paper by Terveen and Wroblewski (1991) explores discrepancies (which they refer to as troubles) that arise when people collaborate to enhance the CYC knowledge base (Lenat and Guha 1989).

The overall body of work described here has provided a technique for facilitating CKA that relies on the structure of a knowledge representation to identify, explain, and resolve discrepancies in knowledge. We have also identified a number of important unexplored problems and possibilities that lie at the frontier of the work reported here. We believe that this research will serve as the starting point for recognizing the barriers to consensus and making possible the effective engineering of consensus knowledge bases.\*

Acknowledgements. This research was supported by the International Financial Services Research Center at the MIT Sloan School of Management and the Natural Sciences and Engineering Research Council of Canada. The authors would also like to thank the Associate Editor and three anonymous reviewers for their helpful comments.

\* Michael J. Shaw, Associate Editor. This paper was received on May 29, 1992, and has been with the authors 5 months for 1 revision.

## References

Agarwal, R. and M. Tanniru, “A Structured Methodology for Developing Production Systems," Decision Support Systems, 8 (1992), 482–499.

Azcel, J. and T. Saaty, "Procedure for Synthesizing Ratio Judgments," Journal of Mathematical Psychology, 27 (1984), 93–102.

Benbasat, I. and J. Dhaliwal, “A Framework for the Validation of Knowledge Acquisition," Knowledge Acquisition, 1 (1989), 215–233.

Boose, J., Expertise Transfer for Expert System Design, Elsevier, Amsterdam, 1986.

Brachman, R. and J. Schmolze, “An Overview of the KL-ONE Knowledge Representation System," Cognitive Sci., 9 (1985), 171–216.

Clancey, W., “The Epistemology of a Rule-Based Expert System—A Framework for Explanation," Artifi cial Intelligence, 20 (1983), 215–251.

Conklin, J. and M. Begeman, “gIBIS: A Hypertext Tool for Exploratory Policy Discussion," Proceedings of the Second Conference on Computer-Supported Cooperative Work, Association for Computing Machinery, Portland, OR, 1988.

Cung, L. and T. Ng, “DESPLATE: A Diagnostic Expert System for Faulty Plan View Shapes of Steel Plates," in J. R. Quinlan, (Ed.), Applications of Expert Systems, 2, Addison-Wesley, Reading, MA, 1989, 156–169.

Davis, R., Expert Systems: Where do we go from here? MIT AI Lab Memo 665, 1982

, B. Buchanan and E. Shortliffe, “Production Rules as a Representation for a Knowledge-Based Consultation Program," Artificial Intelligence, 8 (1977), 15–45.

Delbecq, A. and A. Van de Ven, “A Group Process Model for Problem Identification and Program Planning," J. Applied Behavioral Science, 7 (1971), 466–492.

DeSanctis, G. and Gallupe, B., “A Foundation for the Study of Group Decision Support Systems," Management Science, 33 (1987), 589–609.

Fellers, J., “Skills and Techniques for Knowledge Acquisition: A Survey, Assessment, and Future Directions," Proceedings of the Eighth International Conference on Information Systems, Philadelphia, PA, Society for Information Management and The Institute of Management Sciences, 1987, 118–132.

Feltovich, P., Knowledge Based Components of Expertise in Medical Diagnosis, Unpublished Doctoral Dissertation, University of Minnesota, 1981.

Gaglio, S., R. Minciardi and P. Puliafito, “Multiperson Decision Aspects in the Construction of Expert Systems," IEEE Transactions on Systems, Man, and Cybernetics, 15 (1985), 536–539

Gaines, B. and M. Shaw, “Comparing the Conceptual Systems of Experts," Proceedings of IJCAI-89, Detroit, MI, International Joint Conference on Artificial Intelligence, 1989, 633–638.

Hammond, K. and L. Adelman, “Science, Values, and Human Judgment," Science, 194 (1976), 389– 396.

Helmer, O. and N. Rescher, “On the Epistemology of the Inexact Sciences," Management Sci., 6 (1959), 25-52.

Jagannathan, V. and A. Elmaghraby, "MEDK AT: Multiple Expert Delphi-Based Knowledge Acquisition Tool,"Engineering Mathematics and Computer Science Department Technical Report, University of Louisville, Louisville, KY, 1985.

Klein, M., "Towards a Theory of Conflict Resolution in Cooperative Design," Proceedings of the 9th

Workshop on Distributed Artificial Intelligence, Seattle, WA, American Association for Artificial Intelligence, 1989, 329–349.

Lee, J., "SIBYL: A Tool for Managing Group Decision Rationale," Proceedings of the Third Conference on Computer-Supported Cooperative Work, 1990, 79–91.

Lef kowitz, L. and V. Lesser, "Knowledge Acquisition as Knowledge Assimilation," International J. Man Machine Studies, 29 (1988), 215–226.

Leite, J. and P. Freeman, “Requirements Validation Through Viewpoint Resolution,"IEEE Transactions on Software Engineering, 17 (1991), 1253–1269

Lenat, D. and R. Guha, Building Large Knowledge-based Systems: Representation and Inference in the Cyc Project, Addison-Wesley, Reading, MA, 1989.

Libby, R., K. Trotman, and I. Zimmer, "Member Variation, Recognition of Expertise, and Group Perfor mance," J. Applied Psychology, 72 (1987), 81–87

Lindsay, R., B. Buchanan, E. Feigenbaum, and J. Lederberg, DENDRAL: Artificial Intelligence and Chemistry, McGraw-Hill, New York; 1980.

Liou, Y. and J. Nunnamaker, "Using a Group Decision Support System Environment for Knowledge Acquisition: A Field Study," Proceedings of the 1990 Hawaii International Conference on Systems Sciences. Kona, HI, The Institute of Management Sciences, 1990, 40–49.

Lipp, A., A Knowledge-Based System Built with the Aid of a Group Decision Support System, Unpublished Doctoral Dissertation, University of Georgia, 1989.

Lowe, D., “Co-operative Structuring of Information: The Representation of Reasoning and Debate," International J. Man-Machine Studies, 23 (1985), 97–111.

Malone, T. and K, Crowston, "What is Coordination Theory and How Can it Help Design Cooperative Work Systems?." Proceedings of the Third Conference on Computer-Supported Cooperative Work, Los Angeles, CA, November 1992, Association for Computing Machinery, New York, 357–370.

McGraw, K. and M. Seale, "Knowledge Elicitation with Multiple Experts: Considerations and Tech niques," Artificial Intelligence Review, 2 (1988), 31–44.

Mittal, S. and C. Dym, “Knowledge Acquisition from Multiple Experts," The AI Magazine, 6 (Summer 1985), 32–36.

Montazemi, A. and D. Conrath, "The Use of Cognitive Mapping for Information Requirements Analy sis," MIS Ouarterly. 10 (March 1986), 45–56.

Ohlsson, S. and P. Langley, PRISM: Tutorial and Manual, University of California at Irvine, Computer Science Department Technical Report #86-02, February 1986.

Shaw, M. and B. Gaines, “An Interactive Knowledge-Elicitation Technique Using Personal Construct Technology," in Knowledge Acquisition for Expert Systems, A. Kidd (Ed.), Plenum Press, New York, 1987.

and B. Woodward, “Validation in a Knowledge Support System: Construing and Consistency with Multiple Experts," International J. Man-Machine Studies, 29 (1988), 329–350.

Stefik, M., "The Next Knowledge Medium," The AI Magazine, 7 (1986), 34–46.

, Gregg Foster, Daniel G. Bobrow, Kenneth Kahn, Stan Lanning, and Lucy Suchman, "Beyond the Chalkboard," Comm. of the ACM, 30, 1 (1987), 32–47.

Stephens, J., An Expert System for Marketing Statistics, Unpublished Master's Thesis, MIT Sloan School of Management, June 1986.

Sviokla, J., "Business Implications of Knowledge-Based Systems, Part I," Data Base, 17 (Summer 1986), 5-19.

Sycara, K., “Multiagent Compromise via Negotiation," in L. Gasser and M. Huhns (Eds.), Distributed Artificial Intelligence, 2, Morgan Kaufmann, London, 1989, 119–138.

Terveen, L. and D. Wroblewski, “A Tool for Achieving Consensus in Knowledge Representation," Proceedings of the National Conference of the American Association for Artificial Intelligence, 1991, AAAI Press, Menlo Park, CA, 74–79.

Trice, A., Facilitating Consensus Knowledge Acquisition, Unpublished Doctoral Dissertation, MIT, 1990.

Wagner, C., Simplification of the Database Design Process: Automated View Integration, Unpublished Doctoral Dissertation, University of British Columbia, 1988.

Winograd, T. and F. Flores, Understanding Computers and Cognition, Ablex, Norwood, NJ, 1986
