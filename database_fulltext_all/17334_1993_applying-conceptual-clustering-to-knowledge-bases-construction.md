---
otero_id: 17334
otero_key: "B2YHVHWR"
title: "Applying conceptual clustering to knowledge-bases construction"
authors: "Kar yan Tam"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90037-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applying conceptual clustering to knowledge-bases construction

Kar Yan Tam

The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong

Concept hierarchy is a common approach to organizing structural knowledge in expert systems because of its efficient mechanism to store and generalize a large body of interrelated concepts. Construction of a concept hierarchy, however, is still an unstructured manual process. This laborious process, which is usually conducted by interviewing with human experts, is generally regarded as the bottleneck in developing an expert system. In this paper, a conceptual clustering approach to automatically generating a concept hierarchy is presented. Details of the automated process are illustrated with an experimental system. Initial findings obtained from this study indicate that: (1) construction of concept hierarchy can be automated; (2) inference making can be accomplished by partial matching; (3) conceptual clustering can be used as a general modeling tool in other management disciplines.

Keywords: Conceptual clustering; Machine learning; Expert systems; Category utility.

## 1. Introduction

Rapid advances in computer and information technologies have extended the scope and improved the quality of the decision making processes within an organization. At the individual level, decision makers are able to expand their decision choices by generating, evaluating, and comparing alternatives more effectively than before. At the corporate level, the strategic use of information technologies has been gaining increased attention in recent years.

Expert systems are one of the information technologies that have been adopted by different industries and applied in different domains. Yet, the use of expert systems still remains a controversial one. Both success and failure stories of expert systems abound in recent years. Some of the failures are attributed to the overwhelming optimisms of this technology $[27,35]$ . A common misconception is that an expert system can outperform human decision makers. While this is true in a limited sense, its usefulness should not be generalized beyond its intended domain. Failing to recognize this limitation will inevitably result in failure. On the other hand, successful applications of expert systems have reportedly advanced the competitive edges of adopting companies. A list of successful systems are reviewed in $[14]$ . A closer look at these systems reveals three important factors that attribute to their successes: First, their application domains are well defined and narrow in scope; second, the benefits of adopting expert systems can be formally measured and evaluated; third, expertise stored in the knowledge-bases are relatively static. The static nature of these domains justifies a carefully planned knowledge acquisition process which involves substantial cost and time overhead. But once the knowledge-base is developed, a longer lead time can be allowed between subsequent updates.

![](/api/attachments/B2YHVHWR/fulltext/images/4fd0e776ea4cba7a98ff3be85f730fc360ac45c1abef47d9757d02242713910b.jpg)

Although expert system developers are beginning to recognize the importance of a well-defined domain and an appropriate evaluation criteria in initializing projects, application domains are still primarily restricted to those that do not require frequent updates of the knowledge base. Unless applications can be extended to more dynamic domains, the potential of this technology will be limited. If expert systems were to be adopted by organizations to compete in a changing environment, issues such as knowledge acquisition and refinement must be addressed. Our view is shared by other researchers who contend that as techniques of eliciting expert knowledge become more mature and standard, organizations will start to construct expert systems that utilize their in-house expertise $[33,34,45]$ . Wisely used and timely implemented, expert systems will add to the intelligence of an organization $[14]$ . Huber $[23]$ recently suggests in one of his propositions that “Availability of more robust and user-friendly procedures for constructing expert systems leads to more frequent development and use of in-house expert systems as components of organizational memories”. Given the relevance of this topic from both the information systems (IS) and organizational perspectives, investigation into a robust knowledge acquisition technique is both warranted and desired.

An understanding of how knowledge is represented in an expert system provides a natural starting point in the study of knowledge acquisition and updating techniques. Currently, most development tools support two knowledge representation schema within a single expert system. The two schema, production rules and concept hierarchy, are designed to represent two different kinds of expertise. Production rules take the form of IF–THEN rules and are used to represent the reasoning process of human experts. Each production rule relates a set of conditions to a set of actions. A collection of production rules represents an expert's (or experts') reasoning process in problem solving. Concept hierarchy, on the other hand, is used to organize factual domain knowledge in the form of a generalization hierarchy.

Currently, acquiring expertise from human experts is a lengthy interactive effort. While numerous techniques such as protocol analysis, structured questions, and discourse analysis have been proposed to help knowledge engineers in this respect, these verbal methods are limited by how well the experts are able to articulate their expertise. According to recent surveys, it takes forty person years to develop an expert system to perform reasonably difficult tasks [1], and the cost of a typical moderate system (300 rules) runs at \$250 000 to \$500 000 [40] or \$700.00 per rule as reported by Fried [16]. Added to this complexity is the problem of aggregating knowledge from different sources and the lack of well trained knowledge engineers. Because of these reasons, knowledge acquisition is generally regarded as the bottleneck in building an expert system [6,10].

As an attempt to circumscribe the bottleneck problem, automated knowledge acquisition systems have been developed. These systems such as ID3 [36,37] and AQ11 [30] are based on machine learning techniques originated from artificial intelligence (AI) research. These techniques are aimed at inducing from a collection of examples (e.g., symptoms of patients), each belonging to a class (e.g., disease), a set of production rules that describe the class membership (e.g., diagnosis decisions). Impressive results were obtained from early experimental systems. For example, Michalski and Chilausky [30] demonstrate in the case of soy bean disease diagnosis that the knowledge acquired by using AQ11 outperformed human experts in diagnosis accuracy. Another successful case is a 2500 rules expert system built by British Petroleum [13]. With the help of knowledge acquisition aids, the project was finished within one year. Recent management applications such as Messier and Hansen's bankrupt prediction model [29], Shaw and Gentry's consumer credit scoring system [39], and Carter and Catlett's credit card applications evaluation system [8], have shown the relevance of these systems in the business IS environment.

So far, most of the knowledge acquisition systems are designed to acquire production rules; very little has been done in the automated acquisition of concept hierarchy. Unless similar techniques are developed for concept hierarchy and coupled with the rules acquisition systems, the bottleneck problem may not be fully resolved. The objective of this paper is to present a robust computerized procedure for the construction and updating of a concept hierarchy. The procedure was implemented in a system called HiC (an acronym of Hierarchy Constructor). Like the rules acquisition systems, the procedure is not designed to substitute human knowledge engineers but to assist them in aggregating, categorizing, and generalizing factual knowledge in such a way that the overall knowledge acquisition process and its subsequent refinement are expedited. Bearing in mind this objective and recognizing the rapidly changing business environment, we believe the procedure should deal with the following:

(1) In order to cope with the rapidly changing business environment, the system should be capable of incorporating new knowledge incrementally without massive rearrangement of the hierarchy.

(2) The concept hierarchy should not only store structural knowledge efficiently but support inference making with partial information.

(3) The system should be easily integrated with the production rules in an expert system. Therefore, the syntactic constructs used to describe a concept hierarchy should be similar to those used by production rules.

(4) The system should allow knowledge engineers to state their own preferences of the first two requirements by specifying a parameter set.

Like any system, the features provided by HiC are based on its design specifications. These features reflect our focus on two factors: (1) incremental acquisition and update of structural knowledge; and (2) ability to make inference with partial information. We believe these factors are highly relevant and are of interest to the IS community involved in expert systems development. The rest of the paper is organized into four sections. In the next section, a general overview of concept hierarchies and an example to illustrate their automated constructions are presented. A comparison is also made between numerical taxonomical techniques and the proposed procedure in the context of expert systems development. Section 3 gives a detailed account on the mechanism of HiC. Various design decisions are discussed. In section 4, the ability of a concept hierarchy to make inference using partial information is presented. The last section summarizes our experience with HiC. Future research directions and potential application domains are also outlined.

## 2. Concept hierarchy

Organizing structural knowledge into a concept hierarchy is a common approach to constructing the knowledge base of an expert system. A concept hierarchy takes the form of a generalization tree in which the most specific concepts (concept instances) form the leaves of the tree and the internal nodes represent intermediate concepts. A concept instance is described by a list of attribute-values (e.g., a car may be described by

$\{(\text{Color Black})(\text{Type Sport})(\text{Model 325i})(\text{Manufacturer BMW})\}$ .

Each intermediate concept is derived from generalizing concepts residing immediately at the next lower level (i.e., children). Thus, a path from the root to a leaf corresponds to a sequence of concepts, each obtained by adding more specific information to the previous one. In a concept hierarchy, a concept only needs to store information specific to itself; other general properties, which are also shared by its siblings, are inherited from its ancestors. A concept hierarchy, augmented with a value inheritance mechanism, provides a powerful way to represent structural knowledge. Although tools to support concept hierarchies with multiple-inheritance have appeared recently, this paper will focus on single-inheritance hierarchies only. Unless otherwise stated, the terms concept hierarchy and generalization tree will be used interchangeably for the rest of the paper.

The notion of concept hierarchy is not new and can be found in a number of computer science areas, most notably in artificial intelligence, programming languages, and databases. In artificial intelligence, a frame is a general knowledge representation scheme which provides constructs for value inheritance [46]. In fact, frames extend the notion of inheritance to other constructs such as procedures and demons. In programming language research, class hierarchy forms the programming paradigm of object-oriented languages (OOLs). These languages, such as Smalltalk, Loops, Clu, and C++ [43], encapsulate data and procedures $^{1}$ into a single entity called an object. Each object is an instance of a class. Classes are organized in a hierarchy in such a way that attributes and procedures of a class are inherited by its descendants (i.e., subclasses). However, for OOLs that support multiple inheritance, each object could be an instance of more than one class, and each class could have multiple parents. Paralleling the work in programming languages is research in data models. It has long been advocated that a conceptual data model should provide an abstraction mechanism for class generalization [41]. Research along this direction has introduced conceptual modelling languages such as Adaplex [3], SDM [21], Taxis [32] and Galileo [2], which provide constructs to operationalize the notion of class generalization.

![](/api/attachments/B2YHVHWR/fulltext/images/b9fa32f1c22e9f0c778b6d868d74feb8adeff95a06b2e142068341b1de66f7ed.jpg)  
Fig. 1. Integrating production rules and concept hierarchy in knowledge representation.

In expert systems development, combining concept hierarchies and production rules has proven to be an efficient and effective method of knowledge organization. Numerous expert system shells such as KEE, LOOPS, and ART $^{2}$ are designed to support the integration of rules and concept hierarchies. Using these tools, no explicit programming effort is required to query the attributes of a concept within a rule. All queries and pattern matching operations are supported by a value inheritance mechanism which is transparent to the rule inference engine. Such an arrangement, as shown in fig. 1, facilitates the organization of a knowledge base by providing a clean separation between factual and heuristic knowledge, and at the same time supporting integrated reasoning.

However, the task of organizing domain specific structural knowledge into a concept hierarchy is not a trivial one. Conventional methods for acquiring production rules (e.g., interviews and protocol analysis) are not suitable because they are mainly aimed at eliciting decision rules from experts. Construction of a concept hierarchy on the other hand requires summarizing and generalizing a knowledge domain. This is a task which is erroneous, if not impossible, for those who have limited or partial knowledge of the domain. Furthermore, the holistic nature of the knowledge may be so immense that no human expert has the competence to accomplish the task effectively.

## 2.1. Concept categorization

Quantitative techniques have been developed for the purpose of concept categorization. These techniques can be classified along two dimensions: (1) numerical vs. symbolic; and (2) discriminating vs.

<table><tr><td rowspan="3">Symbolic</td><td>Rules Inductione.g., AQ11 ID3</td><td>Conceptual Clusteringe.g., CLUSTER/2,COBWEB, UNIMEM</td></tr><tr><td>Discriminant Analysise.g., Linear, LogisticKNN</td><td>Numerical Clusteringe.g., single linkage,average linkage</td></tr><tr><td>Discriminating</td><td>Clustering</td></tr></table>

Fig. 2. A dichotomy of classification techniques.

clustering (fig. 2). The first dimension deals with the way a concept is represented. The second dimension is concerned with the class membership of concepts. Discriminating techniques are used to categorize concepts into known classes (e.g., classifying banks into failed and non-failed banks), while clustering techniques are used to organize concepts into a hierarchy by grouping similar concepts to form classes (e.g., to identify similar products in a market segmentation study). In the latter case, the number and type of classes are not known beforehand.

Previous work on clustering techniques has centered around the term numerical taxonomy or cluster analysis. Recent advent of artificial intelligence has introduced a new conceptual clustering approach to the categorization problem. Although the two approaches share a common goal, which is to group 'similar' concepts in a class, they are different in numerous aspects with regard to explanation capability, computational complexity, and measure of similarity. In the present section, we will focus on conceptual clustering and contrast it with its numerical counterpart in the context of expert systems development.

## 2.1.1. Numerical clustering

Development in numerical clustering has focused primarily on the metric and goodness of clustering (For a survey on numerical clustering techniques, see $[4,12,23]$ ). So far, there is no conclusive agreement on the relative superiority of each metric or goodness measure.

Numerical clustering techniques have a number of limitations when used to construct concept hierarchies for expert systems. They are: (1) limited expressive power; (2) inefficient storage mechanisms; and (3) lack of generalization. The synthetic nature of these clustering techniques generates little semantic information about the concept hierarchy. Each cluster is simply a set of vectors, and its meaning is difficult to express in symbolic form. The only available information is the pairwise distance between any two vectors. However, vector pairs having equal distances may have different meanings. The coding scheme for categorical variables further distorts the 'similarity' between two vectors. Hierarchies so constructed require all vectors to be stored explicitly because the clustering procedure has to be rerun for every new concept instance. In cases where the new instance is very similar to some stored concepts and can be placed in an existing cluster, rerunning the entire procedure is, although redundant, yet unavoidable. While numerical clustering techniques are appropriate in domains where concept instances can be described numerically and the domain is relatively static, they are less appealing for representing symbolic structural knowledge.

## 2.1.2. Conceptual clustering

Stepp and Michalski [42] define conceptual clustering as: “a form of learning from observations and its goal is to structure given observations into a hierarchy of meaningful categories.” Conceptual clustering goes beyond the mere categorization of concepts by providing a symbolic explanation to each concept cluster. An intermediate concept in the hierarchy does not contain its descendants as in the case of numerical clustering, but their generalization.

Unlike rules acquisition procedures which require a class tag for each example, conceptual clustering requires no predefined class membership. Using the classic example of disease diagnosis, the input to a rule acquisition system is a set of symptom/disease pairs. The system will infer, for each disease, the corresponding symptoms. On the other hand, the input to a conceptual clustering system is a collection of concept instances, each described by a list of attribute-values. No assumption is made on the causal relationship between attributes in the list. The output is a concept hierarchy which groups 'similar' instances to form classes. This grouping process proceeds hierarchically upward from the concept instances. It is controlled by a clustering criterion and is reflected by the structure of the resultant hierarchy. HUATUO, a disease diagnosis system based on conceptual clustering techniques [9], discovered classes of symptoms and diseases automatically. After close inspection, it was found that these classes matched closely with the taxonomy suggested previously in medical literature.

Since attributes are inherited from the ancestors, each node requires less storage space. Because of the potential gain in storage efficiently, hierarchical knowledge organization has been suggested as a cognitive model in the study of human intelligence. In $[17]$ , Gagne describes human learning in terms of a hierarchy. Arbib $[5]$ states a concept hierarchy “reduces the burden of computation at higher level” and claims “more space is available and information flow is substantially reduced in comparison to an organization having only one level of command.” It is suggested in Arbib $[5]$ , Lashley $[25]$ , and Rock $[38]$ that hierarchical organization underlies animal nervous systems.

An illustrative example We will describe a conceptual clustering system called HiC which accepts a sequence of concept instances and organizes them in the form of a concept hierarchy. Before we move into the details of HiC, let us illustrate its mechanism by considering the following example. Suppose we have six programming languages: COBOL, PASCAL, C, Smalltalk, LISP and Prolog. The attribute-values of each concept are shown in table 1. To simplify the example, the description of each concept is limited to only four attributes.

Many concept hierarchies can be constructed from these six instances. Some of these hierarchies are shown in fig. 3. As compared with fig. 3b and 3c, fig. 3a seems to be a reasonable way to summarize the six instances by creating three new intermediate concepts $I_{1}$ , $I_{2}$ , and $I_{3}$ . The first level of the hierarchy suggests that there are two different classes of programming languages, $I_{1}$ and $I_{2}$ , which can be described respectively as: (1) programming languages with no mathematical foundation; and (2) declarative, integrated data/procedure languages for AI applications.

In the second level of the hierarchy, $I_{1}$ is further specialized into three subclasses: (1) Smalltalk; (2) COBOL; and (3) $I_{3}$ (procedural languages with separated data and procedures). The two concept instances in $I_{3}$ , PASCAL and C, are identical in all attributes except their applications. Similarly, $I_{2}$ contains Prolog and LISP which are distinguished by their mathematical foundation (logic for Prolog and Lambda-Calculus for LISP).

Table 1  
Attribute-values of six programming languages.

<table><tr><td>Concept</td><td>Program organization</td><td>Application area</td><td>Data/procedure</td><td>Mathematical foundation</td></tr><tr><td>COBOL</td><td>Procedural</td><td>Data Processing</td><td>Separate</td><td>nil</td></tr><tr><td>PASCAL</td><td>Procedural</td><td>General</td><td>Separate</td><td>nil</td></tr><tr><td>C</td><td>Procedural</td><td>System Programming</td><td>Separate</td><td>nil</td></tr><tr><td>Smalltalk</td><td>Object</td><td>General</td><td>Local</td><td>nil</td></tr><tr><td>LISP</td><td>Declarative</td><td>Artificial Intelligence</td><td>Local</td><td> $\lambda$ -Calculus</td></tr><tr><td>Prolog</td><td>Declarative</td><td>Artificial Intelligence</td><td>Local</td><td>Logic</td></tr></table>

![](/api/attachments/B2YHVHWR/fulltext/images/4aab337bad8fbc23024326dcff3e9025a413a2084d9275b1f665c1b07e016ab2.jpg)  
Fig. 3A, B and C. A concept hierarchy for the six programming languages.

Since instances belonging to the same class share similar attribute-values, only the set of distinct attribute-values and their inheritance relationships may need to be stored. As evidenced from fig. 3a, organizing concepts in a hierarchy is a very 'space efficient' method to store a large pool of concepts with exhibit a significant degree of regularity. In the programming language example, storage saving is approximately $33.33\%^{3}$ .

The concept hierarchy shown in fig. 3a was constructed using HiC. This example illustrates a number of issues. First, selection of the best concept hierarchy is dependent on having a clustering criterion. By adopting such a criterion, a clustering program can theoretically create a total ordering of all the hierarchies that can be constructed from the given set of concept instances. However, the number of hierarchies may be so large that an exhaustive search is impossible. In this case, the criterion may be used as a heuristic to guide the search for good rather than the best solutions. For example, fig. 3a is not the optimal hierarchy in terms of storage efficiency but it is a reasonably good one. $^{4}$ Second, little generalization can be obtained if only identical attribute-values among a set of concept instances are used to form a new class. In order to relax this restriction in favor of a more generalized concept hierarchy, a less restricted grouping rule needs to be specified. Third, the ease of adding new concept instances to a hierarchy has a significant impact on the practical usefulness of the clustering procedure. If new instances could be incorporated with limited rearrangement of the original hierarchy, then updating he knowledge-base can be done incrementally.

Implications from these issues can be used as design guidelines in building automated concept hierarchy construction systems. Yet, different standpoints would result in systems that have large discrepancies in functionally and efficiently. In fact, some of these requirements conflict with each other (e.g., optimal hierarchy vs. ease of adding a new instance), thus necessitating a tradeoff to be made by the knowledge engineer. In the following sections, we will discuss, in conjunction with the requirements mentioned earlier, our positions on these issues along with a description of HiC's mechanism.

## 3. Mechanism of HiC

Two major objectives are specified in the design of HiC: (1) incremental construction of concept hierarchies; and (2) inference making with incomplete information.

HiC adopts a top-down (divisive) approach as compared with the bottom-up (agglomerative) approach in the construction of concept hierarchies. In the latter approach which has been adopted by CLUSTER/2 [31] and HUATUO [9], all concept instances are processed in batch. A concept hierarchy is constructed by merging concepts at the lower levels until all concepts are grouped into a single concept (i.e., the root). Using this approach, it is very difficult to add new instances after the hierarchy is built. The only way is to rerun the procedure with the new instances. The top-down approach, as demonstrated by COBWEB [15] and UNIMEM [26], allows concept instances to be added incrementally. This is made possible by merely rearranging a certain portion of the hierarchy instead of rebuilding it from scratch. Since concept hierarchy is used to organize structural knowledge which typically exhibit evolutionary rather than revolutionary changes, a significant portion of the hierarchy will remain the same. Two questions needed to be answered in adopting a top-down approach: (1) Which portion of the hierarchy needs to be updated? and (2) once located, how can it be rearranged? The first question leads directly to the notion of clustering criterion. That is, how does one quantitatively evaluate the 'goodness' of a hierarchy?

## 3.1. Category utility

In view of the second design objective, the ability of inference making under incomplete information hinges on a clustering criterion which exploits the regularity among the stored concepts so that missing information of a new concept instance can be predicted from the hierarchy. We found category utility an appropriate criterion in meeting this objective. Category utility provides a relative measure of how well a hierarchy exploits the regularity of stored concepts in terms of attribute-values prediction accuracy. Category utility is a metric originally developed by Gluck and Corter [19] to predict those concept categories that can be retrieved faster during object recognition. Fisher [15] describes category utility as a compromise between intra-class similarity and inter-class dissimilarity of concepts. According to the way concepts are clustered, different hierarchies will have different category utilities.

The category utility of a hierarchy is defined as follow: Given a set of concept instances S organized in a concept hierarchy. Each concept instance is described by N attributes $\{A_{1},\ldots,A_{N}\}$ . Suppose the total number of concepts, including both concept instances and intermediate concepts in the hierarchy, is M, denoted by $\{C_{1},\ldots,C_{M}\}$ , and that each concept $C_{j}$ is described by an unordered attribute-value list $\{(A_{1}V_{j1})(A_{2}V_{j2})\ldots(A_{N}V_{jN})\}$ , $1\leqslant j\leqslant M$ . Further assume that there is: (1) a probability distribution $P(A_{i}=V_{ij})$ on the values of each attribute; (2) a conditional probability distribution $P(A_{i}=V_{ij}|C_{k})$ on the values of each attribute conditioned on the concept $C_{k}$ (i.e., those attribute-values contained in $C_{k}$ );

Table 2  
Attribute-value distribution of intermediate concepts in fig. 3a.

<table><tr><td>Concept</td><td>Attribute</td><td>Value</td><td>Prob(attribute = value/concept)</td></tr><tr><td rowspan="12"> $R_{H}$ </td><td rowspan="3">Program organization</td><td>Procedural</td><td>0.500</td></tr><tr><td>Object</td><td>0.167</td></tr><tr><td>Declarative</td><td>0.333</td></tr><tr><td rowspan="4">Application area</td><td>Data processing</td><td>0.167</td></tr><tr><td>General</td><td>0.333</td></tr><tr><td>System programming</td><td>0.167</td></tr><tr><td>Artificial intelligence</td><td>0.333</td></tr><tr><td rowspan="2">Data/procedure</td><td>Separate</td><td>0.500</td></tr><tr><td>Local</td><td>0.500</td></tr><tr><td rowspan="3">Mathematical foundation</td><td>nil</td><td>0.666</td></tr><tr><td>Lambda calculus</td><td>0.167</td></tr><tr><td>Logic</td><td>0.167</td></tr><tr><td rowspan="8"> $I_1$ </td><td rowspan="2">Program organization</td><td>Procedural</td><td>0.750</td></tr><tr><td>Object</td><td>0.250</td></tr><tr><td rowspan="3">Application area</td><td>Data processing</td><td>0.250</td></tr><tr><td>General</td><td>0.500</td></tr><tr><td>System programming</td><td>0.250</td></tr><tr><td rowspan="2">Data/procedure</td><td>Separate</td><td>0.750</td></tr><tr><td>Local</td><td>0.250</td></tr><tr><td>Mathematical foundation</td><td>nil</td><td>1.000</td></tr><tr><td rowspan="5"> $I_2$ </td><td>Program organization</td><td>Declarative</td><td>1.000</td></tr><tr><td>Application area</td><td>Artificial Intelligence</td><td>1.000</td></tr><tr><td>Data/procedure</td><td>Local</td><td>1.000</td></tr><tr><td rowspan="2">Mathematical foundation</td><td>Logic</td><td>0.500</td></tr><tr><td>Lambda calculus</td><td>0.500</td></tr><tr><td rowspan="5"> $I_3$ </td><td>Program organization</td><td>Procedural</td><td>1.000</td></tr><tr><td rowspan="2">Application area</td><td>General</td><td>0.500</td></tr><tr><td>System programming</td><td>0.500</td></tr><tr><td>Data/procedure</td><td>Separate</td><td>1.000</td></tr><tr><td>Mathematical foundation</td><td>nil</td><td>1.000</td></tr></table>

and (3) a probability distribution $\mathbf{P}(C_{k})$ on the concepts. The category utility of the given concept hierarchy is defined as

$$
\frac {\sum_ {k = 1} ^ {M} \mathrm{P} (C _ {k}) \sum_ {i} \sum_ {j} \mathrm{P} \left(A _ {i} = V _ {i j} \mid C _ {k}\right) ^ {2} - \sum_ {i} \sum_ {j} \mathrm{P} \left(A _ {i} = V _ {i j}\right) ^ {2}}{M - 1}.
$$

Category utility can be interpreted as the increase in the expected number of attribute-values that can be correctly predicted given $\{C_{1},\ldots,C_{M}\}$ over the expected number of attribute-values correctly predicted otherwise. The category utility of a hierarchy is always greater than zero but assumes different values in different hierarchies. Given two hierarchies, the one with a higher category utility implies that it has a higher accuracy of attribute-value prediction than the other. A hierarchy with a larger category utility enhances inference making with incomplete information because the missing attribute-values can be readily predicted by known ones.

In HiC, $\mathrm{P}(C_{k})$ is estimated by dividing the total number of concept instances contained in $C_{k}$ by the total number of concept instances in the hierarchy. Conditional probabilities $\mathrm{P}(A_{i}=V_{ij}|C_{k})$ are determined by computing the relative frequency of $A_{i}=V_{ij}$ in the concept instances contained in $C_{k}$ , and $\mathrm{P}(A_{i}=V_{ij})$ is equal to the relative frequency of $A_{j}=V_{ij}$ in all concept instances. For example, the conditional probabilities of each intermediate concept in fig. 3a are shown in table 2.

Given a set of concept instances S, one can rank all the possible concept hierarchies by their category utilities. The one having the largest category utility is then selected as the optimal hierarchy. To accomplish this, an exhaustive search is required. However, the number of hierarchies grows exponentially with $|S|$ . Thus, it will not be practical for HiC to support incremental additions of new concept instances and guarantee optimal solutions simultaneously.

## 3.2. Rearranging a concept hierarchy

Instead of enumerating all possible hierarchies of S, HIC only rearranges a subhierarchy of the original hierarchy when a new concept instance is added. HiC compared the new instance with existing nodes in the hierarchy. The node that best matches the instance in terms of attribute-values, say $r_{H}$ , is selected. All the changes made to the hierarchy are restricted to the subhierarchy rooted by $r_{H}$ .

Once $r_{H}$ is identified, HiC provides four concept operators, New-class, Best-host, Merge, Split, to rearrange its sub-hierarchy. The search space includes only the candidate hierarchies generated by these operators. HiC then selected the one with the largest category utility.

A concept operator can be interpreted as a function that transforms an existing hierarchy into a new hierarchy. The following notations are defined to describe the mechanism of each operator: C is a concept described by an attribute-value list; $R_{H}$ is the root of the entire concept hierarchy; and $r_{H}$ is an intermediate concept (i.e., the root of a sub-hierarchy).

The four concept operators make use of two auxiliary functions, Inherit and Update. Value inheritance in HiC is supported by the function Inherit that returns all inherited attribute-values of a concept in the hierarchy.

```txt
Inherit (C)
begin
    if C is null then
    return ({})
    else begin
    let A-V be all attribute-values in C with relative frequencies equal to 1.0;
    return (A-V ∪ Inherit (parent of C))
    end
```

end

For each ancestor of a concept, Inherit returns those attribute-values of its ancestors with relative frequencies equal to 1.0. Inherit will visit all concepts along the path from C to $R_{H}$ . Although not explicitly stated for the rest of our discussion, Inherit is used whenever the attribute-values of a concept are queried.

The function of Update is to enforce consistency of a hierarchy by propagating the attribute-values of the new concept instance up to its ancestors.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Update $(C_1, C_2)$   
begin for each attribute $A$ in $C_1$ do if $A$ appears in $C_2$ and has the same value then increase the count of $A$'s value by 1 in $C_2$ else recalculate the frequency distribution of $A$ in $C_2$; add 1 to the count of concept instances in $C_2$; return $(C_2)$
</div>

end

Given a new concept instance $C_{1}$ and an existing concept $C_{2}$ in the hierarchy, Update updates the attribute-value list of $C_{2}$ as if $C_{1}$ is one of its children. The updated $C_{2}$ is then returned. Update is used by all concept operators to propagate the information of a new instance up to its ancestors. (see fig. 4.) We discuss each operator in the form of a procedure as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. Adding a new concept instance to an intermediate concept $r_{\mathrm{H}}$  
New-Class $(C, r_{\mathrm{H}})$  
begin  
    let $C$ be a child of $r_{\mathrm{H}}$;  
    for each ancestor $C_{\mathrm{A}}$ of $C$ do  
    $C_{\mathrm{A}} = \text{Update}(C, C_{\mathrm{A}})$;  
    return (Category-utility $(R_{\mathrm{H}}))$  
end  
New-Class appends a new concept instance $C$ to $r_{\mathrm{H}}$ (fig. 5). Attribute-values of the new concept instance are propagated up the hierarchy. The category utility of the new hierarchy is then returned.
</div>

![](/api/attachments/B2YHVHWR/fulltext/images/dd5ea5b5bf41106392dc96c065a6942f8e33495851d4c06d54dc1e3c17e5d7e9.jpg)  
Fig. 4. Updating the ancestors of a concept.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
2. Adding a new concept instance to a child of an intermediate concept $r_{\mathrm{H}}$  
Best-Host $(C, r_{\mathrm{H}})$  
begin  
    for each child $c_i$ (indexed by $i$) of $r_{\mathrm{H}}$ do begin  
    if $c_i$ is not a leaf then begin  
    let $C$ be a child of $c_i$;  
    for each ancestor $C_A$ of $C$ do  
    $C_A = Update(C, C_A)$;  
    $U_i = Category - utility(R_H)$  
    end  
    end;  
    return ($max\{U_i\}$)  
end
</div>

end

![](/api/attachments/B2YHVHWR/fulltext/images/8732e4ea39691256647c50f09bcce06d688561bdd25a96a2aad5e7415725cb09.jpg)  
Fig. 5. Adding a new concept instance to an intermediate concept.

Best-Host selects the best child of $r_{H}$ to host C (fig. 6). It puts C in each of $r_{H}$ 's non-leaf children and calculates the category utility of the resultant hierarchy. The hierarchy with the highest category utility among all possible hosts is then returned.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
3. Merging a new concept instance with an existing concept instance hosted by $r_{\mathrm{H}}$

Merge $(C, r_{\mathrm{H}})$

begin
    let $S$ be the set of leaf-children of $r_{\mathrm{H}}$;
    for each $c_i$ element in $S$ (indexed by $i$) do begin
    create a new concept New with $r_{\mathrm{H}}$ as its parent and $\{c_i, C\}$ as its children;
    delete $c_i$ from the children list of $r_{\mathrm{H}}$;
    for each ancestor $C_A$ of New do
    $C_A = Update(C, C_A)$;
    $U_i = Category - utility(R_H)$
    end;
    return ($max\{U_i\}$)
end

Merge selects a leaf-child $c_i$ of $r_{\mathrm{H}}$ to merge with $C$ (fig. 7). A new child of $r_{\mathrm{H}}$, which hosts $c_i$ and $C$, is created. The category utilities of all possible merges are calculated and the largest value is returned.

4. Splitting existing concepts hosted by $r_{\mathrm{H}}$ and combining them with a new concept instance
Split$(C, r_{\mathrm{H}})$

begin
    let $S$ be the set of non-leaf children of $r_{\mathrm{H}}$;
    for each element $c_i$ in $S$ (indexed by $i$) do begin
    if all $c_i$'s children are leaves then begin
    delete $c_i$ in $S$ and put all children of $c_i$ in the children list of $r_{\mathrm{H}}$;
    add $C$ to $r_{\mathrm{H}}$;
    for each ancestor $C_A$ of $C$ do
    $C_A = Update(C, C_A)$;
    $U_i = Category - utility(R_H)$
    end
    end;
    return ($max\{U_i\}$)
end

Split deletes a non-leaf child of $r_{\mathrm{H}}$ and splits its children (fig. 8). The children, together with the new concept instance, become $r_{\mathrm{H}}$'s children. All non-leaf children of $r_{\mathrm{H}}$ are attempted and their category utilities calculated. The best category utility is returned.
These four operators restrict the search space to one that grows linearly with the size of $|S|$. The four operators are chosen to localize the rearrangement of the concept hierarchy when new instances are added. They restrict the search space to hierarchies which are different from the original one by changing at most two levels of the hierarchy (tbl. A).
</div>

A major concern in our selection of operators is computational complexity. That is, the time it takes to add a new instance. While it is possible to generalize these operators to work on any arbitrary levels of the hierarchy, the saving in storage may not justify the combinatorial explosion of the search. Of course, the way we limit the search space may lead to suboptimal hierarchies. Based on results obtained from our experiments, we found that reasonably good hierarchies were obtained for a relatively large number of instances.

![](/api/attachments/B2YHVHWR/fulltext/images/d53d707d4455f54164c1a83ba0b282e55ed04456acb07314259bddf8f787a2e5.jpg)  
Fig. 6. Adding a new concept to a child of an intermediate concept.

Although not shown in the above procedures, each operator keeps an updated version of the hierarchy in temporary storage. The original hierarchy will not be changed. Only the affected concepts are stored because there is no need to keep he entire hierarchy of each version. When a decision is made as to which operator should be applied, the version associated with the selected operator will replace the existing hierarchy, and all other versions are discarded to free up space.

![](/api/attachments/B2YHVHWR/fulltext/images/f53ab2b39a901aa581f3b9f6b76ad1fed465ef6fcdaf02c1b71e9640cfd4e5e3.jpg)  
Fig. 7. Merging a new concept instance with an existing concept.

![](/api/attachments/B2YHVHWR/fulltext/images/bb2fd893892c402c212a187c40dca500d910dd4e19392fee09c7b694b109e295.jpg)  
Fig. 8. Splitting existing concepts.

The control mechanism of HiC was implemented in two procedures: Match and Insert.

Control $(C, R_{\mathrm{H}}, t_m)$

begin

$$
\begin{array}{l} r _ {\mathrm{H}} = \text { Match } (C, R _ {\mathrm{H}}, t _ {m}); \\ \text { Insert } (C, r _ {\mathrm{H}}) \end{array}
$$

end

Match locates the concept $r_{H}$ that best matches C. The degree of matching is measured by a similarity index which is defined as follows: Given two concepts $C_{1}$ and $C_{2}$ , a function similarity-index( $C_{1}, C_{2}$ ) is defined as the number of common attribute-values in $C_{1}$ and $C_{2}$ divided by the total number of attribute-values in $C_{1}$ . Notice that similarity-index is not commutative (i.e., in general, similarity-index( $C_{1}, C_{2}$ ) ≠ similarity-index( $C_{2}, C_{1}$ )). A parameter $t_{m}, 0.0 \leqslant t_{m} \leqslant 1.0$ , determines the index's threshold value. The value of $t_{m}$ is specified by the knowledge engineer. By best matching, we mean to locate the most specific concept in the hierarchy which does not violate the threshold value. The effect of specifying a larger $t_{m}$ will increase the likelihood of adding a new instance to a more general concept in the hierarchy. On the other hand, a small $t_{m}$ will force HiC to match the new instance with more specialized concepts reside lower in the hierarchy.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Match (C,  $r_{H}$ ,  $t_{m}$ )
begin
    for each child  $c_{i}$  of  $r_{H}$  (indexed by i) do
    $S_{i} = similarity-index(C, c_{i})$ ;
    $S_{j} = \max\{S_{i}\}$ 
    if  $S_{j} \geqslant t_{m}$  then
    if  $c_{j}$  is a leaf then
    return ( $r_{H}$ )
    else
    Match( $C, c_{j}, t_{m}$ )
    else
    return ( $r_{H}$ )
end

Insert (C,  $r_{H}$ )
begin
    U = max{New-Class (C,  $r_{H}$ ), Best-Host (C,  $r_{H}$ ),
    Merge( $C, r_{H}$ ), Split( $C, r_{H}$ )};
    Replace the initial hierarchy with the version associated with U;
end
</div>

Table A

<table><tr><td>Operators</td><td>Number of levels affected</td></tr><tr><td>New-Class</td><td>1</td></tr><tr><td>Best-Host</td><td>1</td></tr><tr><td>Merge</td><td>2</td></tr><tr><td>Split</td><td>2</td></tr></table>

Once the best concept is located by Match, Insert applies the four operators and selects the one that gives the largest category utility. The existing hierarchy is then replaced by the version associated with the best operator.

## 3.3. Generalization of a concept hierarchy

HiC supports both summarization and generalization. The distinction between the two is as follows. Summarization does not change the attribute-values of each concept instance. It simply identifies common attribute-values so as to improve storage efficiency. Generalization will, on the other hand, smooth out the minor discrepancies between similar concepts and abstract a general description from them. By so doing, the attribute-values of the original concept instances may be changed.

Generalizing a concept in HiC is equivalent to selecting the most representative value of each attribute of the concept. As shown below in the Generalize-update procedure, the attribute-value which has the highest relative frequency (specified by a parameter $t_{g}$ ) is selected as the most representative value of that attribute. Its relative frequency is then set to 1.00. All other values of that attribute are discarded from the concept. The representative value overrides all other values of that attribute. Generalization is only applicable to intermediate concepts because all attributes of a concept instance have singleton values.

Represent finds for each attribute, the most representative value of the attribute.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Represent $(C, t_{\mathrm{g}})$   
begin  
    R-A-V = { };  
    for each $A_{i}$ in $C$ do begin  
    Let $V_{i}$ be the value that has the highest relative frequency;  
    if the relative frequency of $V_{i} \geqslant t_{\mathrm{g}}$ then  
    R-A-V = R-A-V ∪ $\{(A_i V_i)\}$  
    end  
    return (R-A-V)  
end
</div>

The main procedure to generalize a concept hierarchy is Generalize-update. Generalize-update is used for both summarization and generalization. The choice is made by specifying the value of $t_{g}$ as follow: $t_{g} = 1.00$ for summarization and $0.0 < t_{g} < 1.0$ for generalization. Since the distinction is only a choice of parameter value, we will use generalization as a generic term referring to both summarization and generalization.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Generalize-update $(r_{\mathrm{H}}, t_{\mathrm{g}})$   
begin  
    A-V = { };  
    A-V = Represent $(r_{\mathrm{H}}, t_{\mathrm{g}})$;  
    for each $(A_i V_i)$ in A-V do begin  
    delete all occurrences of $(A_i V_{ij})$ except $(A_i V_i)$;  
    set the relative frequency of $V_i$ for $A_i$ to 1.00  
    end
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Update-descendants $(r_{\mathrm{H}},\mathrm{A - V})$ if $r_{\mathrm{H}} = R_{\mathrm{H}}$ then stop else Generalize-update(parent of $r_{\mathrm{H}},t_{\mathrm{g}})$
</div>

Generalization is a bottom-up process which starts from the parent of a newly added concept instance. In order to assure all the descendants of a concept inherit the representative values, attribute which have been generalized are deleted from the concept's descendants. This is accomplished by calling Update-descendants. Update-descendants performs a traverse of the sub-hierarchy with $r_{H}$ as the root. All attributes which have been generalized are deleted from each concept in the sub-hierarchy. This ensures that only the representative value of an attribute is shared by $r_{H}$ 's descendants.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Update-descendants ( $r_{H}$ , A-V)
begin
    if  $r_{H}$  is null then
    return ()
    else
    for each child  $c_{i}$  of  $r_{H}$  do
    begin
    delete all attribute-values ( $A_{i}V_{ij}$ ) where  $A_{i}$  appears in A-V;
    Update-descendants ( $c_{i}$ , A-V)
    end
end
</div>

After all descendants are updated, changes are propagated to $r_{H}$ 's ancestors by repeatedly calling Generalize-update. Notice that the most time-consuming task is to update the descendants. To improve the efficiency of Generalize-update, only those concepts in the sub-hierarchy which have not been visited are updated. This is accomplished by marking a binary flag for each child in the children list of a concept. By doing so, Update-descendants will visit at most $2|S|-1$ concepts in the worst case. $^{5}$ (See proposition 1 in the appendix.)

An illustrative example To illustrate the mechanism of HiC, consider the programming languages example in section 2. Suppose the sequence of concept instances input to HiC is {COBOL, PASCAL, LISP, Prolog, Smalltalk, C}, and $t_{m}=0.5$ . A trace of the program is depicted in fig. 9.

Iteration 1. COBOL is added to the hierarchy as the only concept instance. Since there is only one concept in the initial hierarchy which is the root, the only way to incorporate COBOL is to let it be a child of $R_{H}$ (fig. 10a). The category utility of the hierarchy is zero because its predictability is the same as a singleton class.

Iteration 2. PASCAL is added to the hierarchy. Match(PASCAL, 0.5) returns $R_{H}$ . The four concept operators are then applied to $R_{H}$ . As shown in fig. 9, only New-Class and Merge are applicable to $R_{H}$ . The category utilities of both operators are returned with Merge offering a higher value (1.3333) than New-Class (0.2500). A new concept is created by HiC, denoted by $I_{1}$ , to merge COBOL and PASCAL together (fig. 10b).

Iteration 3. With $t_{m}=0.50$ , there is no concept that matches with Prolog. Hence, it is appropriate for Prolog to form a class of itself. The category utility of the new hierarchy, as shown in fig. 10c, is 1.0833.

<table><tr><td>New-Concept COBOL</td><td>New-Class 0.0000</td><td>Best-Host N.A.</td><td>Merge N.A.</td><td>Split N.A.</td></tr><tr><td colspan="5">&gt; Match PASCAL with  $R_H$ </td></tr><tr><td>New-Concept PASCAL</td><td>New-Class 0.2500</td><td>Best-Host N.A.</td><td>Merge 1.3333</td><td>Split N.A.</td></tr><tr><td colspan="5">&gt; Merge PASCAL with COBOL to form  $I_1$ </td></tr><tr><td colspan="5">&gt; Match Prolog with  $R_H$ </td></tr><tr><td>New-Concept Prolog</td><td>New-Class 1.0833</td><td>Best-Host 1.0000</td><td>Merge N.A.</td><td>Split 0.6667</td></tr><tr><td colspan="5">&gt; Add Prolog to  $R_H$ </td></tr><tr><td colspan="5">&gt; Match LISP with  $R_H$ </td></tr><tr><td>New-Concept LISP</td><td>New-Class 0.8000</td><td>Best-Host 0.7500</td><td>Merge 0.9583</td><td>Split 0.5625</td></tr><tr><td colspan="5">&gt; Merge LISP and Prolog to form  $I_2$ </td></tr><tr><td colspan="5">&gt; Match Smalltalk with  $R_H$ </td></tr><tr><td>New-Concept Smalltalk</td><td>New-Class 0.7314</td><td>Best-Host 0.7600</td><td>Merge N.A.</td><td>Split 0.6200</td></tr><tr><td colspan="5">&gt; Add Smalltalk to  $I_1$ </td></tr><tr><td colspan="5">&gt; Match C with  $I_1$ </td></tr><tr><td>New-Concept C</td><td>New-Class 0.65265</td><td>Best-Host N.A.</td><td>Merge 0.7130</td><td>Split N.A.</td></tr><tr><td colspan="5">&gt; Merge C with PASCAL to form  $I_3$ Fig. 9. A session of hierarchy construction</td></tr></table>

Fig. 9. A session of hierarchy construction.

Iteration 4. LISP is matched with $r_{H}$ . All four operators are applicable this time. Their category utilities are 0.8 for New-Class, 0.75 for Best-Host, 0.9583 for Merge, and 0.5625 for Split. Since Merge has the highest category utility, a new concept $I_{2}$ is created that merges Prolog and LISP together (fig. 10d).

Iteration 5. Smalltalk is added and matched with $R_{H}$ . Only New-Class, Best-Host, and Split are applicable to $R_{H}$ . Best-Host, with category utility (0.7600) higher than New-Class (0.7314) and Split (0.6200), is selected. The resultant hierarchy is shown in fig. 10e.

Iteration 6. Lastly, C is added to the hierarchy. The best match for C is $I_{1}$ . Only two operators, New-Class and Merge, are applicable. Merge, with category utility (0.7130) higher than that of New-Class (0.6525), is selected. PASCAL and C are merged under a new concept $I_{3}$ as shown in fig. 10f.

Suppose we want to generalize the hierarchy after each instance is added and the value of $t_{g}$ is set to 0.70. Table 3 depicts the attribute-values of each concept in the resultant hierarchy after all the instances are added.

Congressmen classification The foregoing example is for illustrative purposes. To study the behavior of HiC in dealing with complex domains, testing with actual concepts is warranted. In this experiment, 50 congressmen were randomly selected from Ehrenhatt [11]. Each congressman was described by his or her party affiliation and voting records on nine major issues in the 98th and 99th Congress. A list of these attributes is shown in table 4.

![](/api/attachments/B2YHVHWR/fulltext/images/d9df657c03bd0ac73f4be1b2f53d8d3154671693409dd82949f1c4fc1dd05d4b.jpg)  
Fig. 10A: Adding COBOL. B: Adding PASCAL. C: Adding Prolog. D: Adding LISP. E: Adding Smalltalk. F: Adding C.

These 50 congressmen were randomly ordered in a sequence and input to HiC. The same sequence was run with different values of $t_m$ , ranging from 0.0-1.0. Three final hierarchies with $t_m = 0.0, 0.5$ , and 1.0 are shown in fig. 11a, b, and c, respectively.

As shown in fig. 11a, the hierarchy with $t_m = 0.0$ has only a single level of concepts. However for $t_m = 0.5$ and 1.0, three distinct classes of congressmen can be easily identified (fig. 11b and c). Each of these classes forms a sub-hierarchy. A detailed examination reveals that the three classes correspond to: (1) congressmen that are not active in voting (represented by cluster $A$ ); (2) Democrats (represented by cluster $B$ ); and (3) Republicans (represented by cluster $C$ ). Note that no priori information is given to HiC as to how the congressmen should be classified, yet HiC arrived at a grouping scheme that used party affiliation as a major classification attribute – an attribute that we would normally use if we were given the same task.

Product Positioning To demonstrate the usefulness of conceptual clustering in managerial domains, we applied HiC to product positioning – a problem faced by market researchers on a daily basis. A crucial step in formulating a marketing strategy is to position a firm's products in terms of competitive offerings and consumers' perceptions. Marketing researchers have developed a number of procedures to produce a position map of competitive offerings. A common approach involves using numerical clustering techniques to generate product clusters that share similar characteristics such as packaging, design, and functionalities. The data sample used here was taken from [20] which comprised of 18 spot-remover products. Each product was defined by five attributes: Package design, brand name, price, house keeping seal, and money-back guarantee.

Table 3  
Attribute-value distribution of each concept in fig. 10f with $t_{g}=0.7$ .

<table><tr><td>Concept</td><td>Attribute</td><td>Value</td><td>Prob(attribute = value/concept)</td></tr><tr><td rowspan="12"> $R_{11}$ </td><td rowspan="3">Program Organization</td><td>Procedural</td><td>0.500</td></tr><tr><td>Declarative</td><td>0.333</td></tr><tr><td>Object</td><td>0.167</td></tr><tr><td rowspan="4">Application area</td><td>Data processing</td><td>0.167</td></tr><tr><td>General</td><td>0.333</td></tr><tr><td>Artificial intelligence</td><td>0.333</td></tr><tr><td>System programming</td><td>0.167</td></tr><tr><td rowspan="2">Data/procedure</td><td>Separate</td><td>0.500</td></tr><tr><td>Local</td><td>0.500</td></tr><tr><td rowspan="3">Mathematical foundation</td><td>nil</td><td>0.666</td></tr><tr><td>Logic</td><td>0.167</td></tr><tr><td>Lambda calculus</td><td>0.167</td></tr><tr><td rowspan="8"> $I_1$ </td><td rowspan="2">Program organization</td><td>Procedural</td><td>0.750</td></tr><tr><td>Object</td><td>0.250</td></tr><tr><td rowspan="3">Application area</td><td>Data processing</td><td>0.250</td></tr><tr><td>General</td><td>0.500</td></tr><tr><td>System programming</td><td>0.250</td></tr><tr><td rowspan="2">Data/procedure</td><td>Separate</td><td>0.750</td></tr><tr><td>Local</td><td>0.250</td></tr><tr><td>Mathematical foundation</td><td>nil</td><td>1.000</td></tr><tr><td rowspan="3"> $I_2$ </td><td>Program organization</td><td>Declarative</td><td>1.000</td></tr><tr><td>Application area</td><td>Artificial intelligence</td><td>1.000</td></tr><tr><td>Data/procedure</td><td>Local</td><td>1.000</td></tr><tr><td rowspan="5"> $I_3$ </td><td>Program organization</td><td>Procedural</td><td>1.000</td></tr><tr><td rowspan="2">Application area</td><td>System programming</td><td>0.500</td></tr><tr><td>General</td><td>0.500</td></tr><tr><td>Data procedure</td><td>Separate</td><td>1.000</td></tr><tr><td>Mathematical foundation</td><td>nil</td><td>1.000</td></tr><tr><td>COBOL</td><td>Application area</td><td>Data processing</td><td>1.000</td></tr><tr><td>PASCAL</td><td>Application area</td><td>General</td><td>1.000</td></tr><tr><td>Prolog</td><td>Mathematical foundation</td><td>Logic</td><td>1.000</td></tr><tr><td>LISP</td><td>Mathematical foundation</td><td>Lambda calculus</td><td>1.000</td></tr><tr><td rowspan="3">Smalltalk</td><td>Program organization</td><td>Object</td><td>1.000</td></tr><tr><td>Application area</td><td>General</td><td>1.000</td></tr><tr><td>Data/procedure</td><td>Local</td><td>1.000</td></tr><tr><td>C</td><td>Application area</td><td>System programming</td><td>1.000</td></tr></table>

The products were clustered using HiC and the resultant hierarchy is shown in fig. 12. As evidenced from the hierarchy, 4 distinct clusters were formed and were labeled as A, B, C, and D. The semantic meaning of each cluster are stated below:

A. products from Glory with poor or no housekeeping seal;

B. products with poor or no housekeeping seal and no money-back guarantee;

C. products with good housekeeping seal and no money-back guarantee;

D. products from K2R with money-back guarantee.

Table 4  
Voting records of congressmen.

<table><tr><td>Key votes</td><td>Attribute</td><td>Valuesa</td></tr><tr><td>Raise social security retirement age to 67 (1983)</td><td> $V_1$ </td><td>{Y, N, U}</td></tr><tr><td>Bar covert US aid to Nicaragua (1983)</td><td> $V_2$ </td><td>{Y, N, U}</td></tr><tr><td>Reduce dairy price support (1983)</td><td> $V_3$ </td><td>{Y, N, U}</td></tr><tr><td>Pass equal right&#x27;s amendment (1983)</td><td> $V_4$ </td><td>{Y, N, U}</td></tr><tr><td>Freeze physicians&#x27; fees under medicare (1984)</td><td> $V_5$ </td><td>{Y, N, U}</td></tr><tr><td>Bar aid to anti-Sandinista forces in Nicaragua (1984)</td><td> $V_6$ </td><td>{Y, N, U}</td></tr><tr><td>Pass bill to revise immigration laws (1984)</td><td> $V_7$ </td><td>{Y, N, U}</td></tr><tr><td>Cut education spending (1984)</td><td> $V_8$ </td><td>{Y, N, U}</td></tr><tr><td>Authorize procurement of 21 MX missiles (1984)</td><td> $V_9$ </td><td>{Y, N, U}</td></tr></table>

$^{a}$ Y - voted for; N - voted against; U - did not vote.

It was found that price and package design were inadequate to differentiate the eighteen products. These facts have important ramifications for a marketing strategy. For example, a strategy targeted at market development should concentrate on characteristics that are different from these four groups. In the event that these eighteen products represent the full spot-remover market, the hierarchy generated by HiC provides a valuable piece of information for the marketing researchers to study the market structure of spot-removers.

![](/api/attachments/B2YHVHWR/fulltext/images/a9655407a8df190ad587ad49e48c856f5aae7a6b439e5d53cc482e96d782c52d.jpg)  
A

![](/api/attachments/B2YHVHWR/fulltext/images/95c93d3cb0b16fc75c9b952dfe025ed3ae7dc625763274e08fff0c6477606df9.jpg)  
B

![](/api/attachments/B2YHVHWR/fulltext/images/c845c6e575045b52990d2759548e9958ddf458c51be22aa98e98e475975eb8b1.jpg)  
Fig. 11A: Congressmen hierarchy with $t_{m}=0.0$ . 11B: Congressmen hierarchy with $t_{m}=0.5$ . IIC: Congressmen hierarchy with $t_{m}=1.0$ .

![](/api/attachments/B2YHVHWR/fulltext/images/2530086e4211466f43c9689aa6c0c406686548b57c63bb6c838c134b0d4904ab.jpg)  
Fig. 12. Concept hierarchy for spot-remover products.

Unlike COBWEB, HiC is not bias towards the first few levels of the hierarchy in adding new instances. In fact, a trace of category utility in the congressmen experiment (fig. 13) indicates that bias towards shallow hierarchy (i.e., smaller $t_{m}$ ) will result in hierarchies with lower category utilities (e.g., $t_{m} = 0.0$ ). As mentioned earlier, HiC is designed to complement rather than substitute human knowledge engineers. Thus, HiC is more flexible than COBWEB by allowing knowledge engineers to state their own preference of grouping concepts by specifying $t_{m}$ .

## 4. Making inference with incomplete information in a concept hierarchy

Apart from providing an efficient mechanism to store knowledge, a concept hierarchy can also be used in making inferences. In problem solving, an important inference task is completion. In a completion task, a partial description of a situation is given. The problem is to complete the description by filling in the missing information. Completion tasks are closely associated with category learning of human beings $[18]$ . Holistic and analytical learning are suggested to be the two modes of category learning by cognitive psychologists $[24]$ . Both of which can be described as completion tasks. Holistic category learning involves storing category information and making decisions about new instances on the basis of their global similarity to known exemplars $[7,28]$ . Analytical category learning involves forming a rule about category membership that is based on one or more independent attributes.

![](/api/attachments/B2YHVHWR/fulltext/images/591f584ad4b99c38107dcf89a8d570ca15ab028e8ca2c7b0e32ea7dc9d801a5a.jpg)  
Number of Concepts  
Fig. 13. A trace of category utility of the congressmen experiment.

If the concept instances exhibit a high degree of regularity, then it is reasonable to predict the missing attribute-values of a new instance by matching it with existing ones in a hierarchy. Unlike rules acquisition systems, completion is not limited to a single attribute in HiC; rather, any set of attributes can be used to predict others.

The completion task is to predict the missing attribute-values of a partially described concept instance C by matching it with an existing concept in the hierarchy. The inference process of HiC works as follows: given C, HiC uses a procedure Search to locate the concept that best matches C. Two parameters $t_{s}$ and $t_{r}$ are used to control the search. The degree of matching is controlled by $t_{s}$ which specifies the similarity index of C and the representative attribute-values of the matched concept. The representative attribute-values of the concept are specified by $t_{r}$ . Both $t_{r}$ and $t_{s}$ assume a range of [0.0, 1.0]. If $t_{s}$ is close to 1.0, Search will return the concept instance which shares the largest number of identical attribute-values with C. For small $t_{s}$ , Search may stop at an intermediate concept. In either case, the representative values of the matched concept are used to complete the description of C.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Search (C,  $r_{H}$ ,  $t_{r}$ ,  $t_{s}$ )
begin
    if  $r_{H}$  is a leaf then
    return ( $r_{11}$ )
    else begin
    for each child  $c_{i}$  of  $r_{H}$  do
    $S_{i} = similarity-index$  (C, (Represent ( $c_{i}$ ,  $t_{r}$ )));
    $S_{j} = \max\{S_{i}\}$ ;
    if  $S_{j} \geqslant t_{s}$  then
    return ((Represent ( $c_{j}$ ,  $t_{r}$ )))
    else
    Search (C,  $c_{j}$ ,  $t_{r}$ ,  $t_{s}$ )
    end
end
</div>

To illustrate how a completion task is carried out by partial matching, we present an example using a concept hierarchy with $t_{m}=0.5$ created by the foregoing congressmen experiment. Another 50 congressmen were randomly selected from Ehrenhatt [11] as the test sample. The task was to use a set of nine attributes to predict the remaining attribute and to compare the prediction accuracy with one that is based on simple relative frequency. The relative frequency of an attribute-value was taken from all concepts instances, and the largest one was used to predict the value of that attribute. The experiment was repeated for each of the ten attributes with $t_{s}=1.00$ and $t_{r}=1.00$ . The result is summarized in fig. 14.

The prediction accuracies using partial matching all exceeded 50%, ranging from 54% for $V_{6}$ to 82% for $V_{4}$ . Comparing with those that based on simple relative frequency, it is clear that partial matching provides far better results. In simple frequency, the predictions accuracies of attributes $V_{3}$ and $V_{9}$ were less than 50%. It was found that voting records and party affiliation were highly correlated with each other. For example, the affiliation of a congressmen to either the Democratic or the Republican party could be determined fairly accurately (80%). As illustrated by this experiment, HiC is capable of identifying the underlying regularity and of constructing a concept hierarchy that capitalizes on this information. The resultant hierarchy is one that tends to minimize storage space and maximize prediction accuracy.

![](/api/attachments/B2YHVHWR/fulltext/images/f50a6056ea21e070d1fe335e5de440af4b0d4ec95b15db32a9805317f1bc5c78.jpg)  
Fig. 14. Prediction accuracy of HiC.

## 5. Conclusion

Concept hierarchy is used to organize symbolic structural knowledge in expert systems because of its efficient mechanism to generalize a large body of interrelated concepts. In this paper, we have presented a procedure to incrementally construct a concept hierarchy from a set of concept instances. The system called HiC was written in Franz LISP and run on an Encore Multiprocessor machine. We have performed a number of experiments to study the behavior of HiC. Initial results obtained can be used as guidelines to pursue future research in this area. We have also identified some interesting extensions of HiC:

(1) The order of concept instances is important, especially when the number of concept instances is small. We observed that the concept hierarchy constructed by the first few concept instances will form the skeleton of the hierarchy which is expanded by adding the remaining instances. A trace of the operators used in the construction of the congressmen hierarchy with $t_{m}=1.0$ in section 3 indicates that there are two distinct stages of the construction process (fig. 15).

In the first stage, there are a lot of merges. These merges create a skeleton of the hierarchy. During the second state, new instances are added using New-Class and Best-Host as the major operators. The Split operator is seldom used during the construction process in our experiments (it is not used at all in fig. 15). This phenomenon is typical in the experiments we have conducted. A plausible explanation is the intrinsic limitation of the concept operators to rearrange an existing concept hierarchy. Because of computational considerations, the four operators are limited to only a subset of the possible rearrangements. For instance, it is not possible to either merge or split concepts between any arbitrary levels in the hierarchy. This explains why the programming language hierarchy constructed by HiC is not the optimal one. A possible extension of HiC is to provide more operators to expand the search space. In order to reduce the effects of input ordering in HiC, one may divide the concept instances into two sets. First, perform an exhaustive search on the first set to create an optimal hierarchy. Then, add the second set to the hierarchy incrementally using HiC.

![](/api/attachments/B2YHVHWR/fulltext/images/d22f22ce0c1ba61c7fde730f9ce3de8ce2e67991878a1d0bcaff5ee404463f66.jpg)  
Number of Primitive Concepts  
Fig. 15. A trace of the concept operators used in the construction of congressmen hierarchy.

(2) In HiC, concepts are grouped in the form of a tree. Values can only be inherited from a single parent. An extension of HiC to include multiple-inheritance seems to be appropriate if such an arrangement provides a more meaningful representation of the domain knowledge.

(3) The current version of HiC supports only qualitative attribute-values. Extensions to include quantitative attributes will be a subject of future work.

(4) There is a trend towards integrated reasoning using a hybrid of knowledge schema. This poses new challenges to the design of the underlying knowledge acquisition systems. In particular, such a knowledge acquisition system should support a suite of knowledge schema (e.g., production rules, concept hierarchy) as well as their acquisition methods. The method presented in this paper focuses merely on the acquisition of structural knowledge. Research is underway to combine HiC and CONIS – a rules acquisition system [44] as a first step towards the construction of a general acquisition knowledge system for expert systems development.

The conceptual clustering procedure discussed in this paper is not restricted merely to the development of expert systems. It can be used as a general modelling tool in other disciplines. As shown earlier, a market researcher can apply this method in the market segmentation study of a product. A production planner can use the same method to identify families of parts which share similar operations and requirements in cellular manufacturing. Likewise, a database designer can delegate part of his job to such a system in constructing a database schema. These are just a few of the many applications that we foresee will be appropriate for conceptual clustering.

## Appendix

Proposition 1. Given a set of concept instances $S$ , the number of concepts in a hierarchy is between $|S| + 1$ and $2|S| - 1$ .

Proof. The lower bound is obtained by having a single level tree with all concept instances in S being the leaves of the tree. For the upper bound, it is sufficient to show that the number of concepts in a

hierarchy is maximized when the hierarchy is a binary tree. Let us hypothesize that the hierarchy which contains the largest number of concepts is not a binary tree, or equivalently that there exists an internal node that has a branching factor larger than 2. Let x be such a node. We consider two cases of x:

Case 1. The branching factor is an even number. x can be split into two concept classes, $x'$ and $x''$ , each holding half of x's children. As a result, the number of concepts in the hierarchy is increased by 1 which contradicts our hypothesis. This proves that all concepts having an even number of children have only two children.

Case 2. The branching factor is an odd number. For branching factor greater than or equal to 5, x can be divided into $x'$ and $x''$ where $|x'| = \lfloor x \rfloor/2$ and $|x''| = (\lfloor x \rfloor/2) + 1$ . If the branching factor of x equal 3, then a new concept, say y, is created which inherits any two children of x, and y is then assigned to be a child of x. In either case, the number of concepts in the hierarchy is increased by 1. This proves that the number of concepts in the original hierarchy is not maximized.

Since the maximized hierarchy must contain concepts that have only 2 children, it follows that the total number of concepts in a maximized hierarchy is equivalent to the number of nodes in a binary tree which is equal to the number of internal nodes plus the number of leaves. Since the number of internal nodes equals the number of leaves minus one, this implies the maximum number of concepts in a hierarchy with $|S|$ concept instances is $|S| + |S| - 1 = 2|S| - 1$ .

## References

[1] M.J. Abdolmohammadi, Decision Support and Expert Systems in Auditing: A Review and Research Directions, Accounting and Business Research (Spring, 1987).

[2] A. Albano, L. Cardelli and R. Orsini, Galileo: A Strongly Typed, Interactive Conceptual Language, Report 83-11271-2, Bell Laboratories, Murray Hill, NJ (July 1983).

[3] ADAPLEX: Rationale and Reference Manual, Technical Report CCA-83-03, Computer Corporation of America (May 1983).

[4] M.R. Anderberg, Clustering Analysis for Applications (Academic Press, New York, 1973).

[5] M.A. Arbib, The Metaphorical Brain: An Introduction to Cybernetics as Artificial Intelligence and Brain Theory (John Wiley, New York, 1972).

[6] A. Barr and E.A. Feigenbaum, The Handbook of Artificial Intelligence, Vol. II (Pittman Books, Ltd., London, 1982).

[7] L. Brooks, Nonanalytical Concept Formation and Memory for Instances, in: E. Rosch and B. Lloyd, Eds., Cognition and Categorization (Erlbaum, Hillsdale, NJ, 1978).

[8] C. Carter and J. Catlett, Assessing Credit Card Applications Using Machine Learning, IEEE Expert (Fall, 1987).

[9] Y. Cheung and K.S. Fu, Conceptual Clustering in Knowledge Organization, IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 7, No. 5 (1985).

[10] R.O. Duda and E.H. Shortliffe, Expert Systems Research, Science 15 (April 1983).

[11] Ehrenhatt, A., Ed., Politics in America (Congressional Quarterly Press, Washington, DC, 1985).

[12] B. Everitt, Clustering Analysis (Heinemann Educational Books, London, 1974).

[13] Expert System User (August, 1986) 16–19.

[14] E. Feigenbaum, P. McCorduck, and H.P. Nei, The Rise of the Expert Company (Times, New York, 1988).

[15] D. Fisher, Knowledge Acquisition via Incremental Conceptual Clustering, Machine Learning, Vol. 2, No. 2, (1987).

[16] L. Fried, The Dangers of Dabbing in Expert Systems, Computerworld (June 29, 1987).

[17] R.M. Gagne, Contributions of Learning to Human Development, in: J. Elliot, Ed., Human Development and Cognitive Processes (Holt, Rinehart and Winston, 1971).

[18] W. Garner, The Processing of Information and Structure (Erlbaum, Potomac, MD, 1974).

[19] M. Gluck and J. Corter, Information, Uncertainty, and the Utility of Categories, Proceedings of the Seventh Annual Conference of the Cognitive Science Society (Lawrence Erlbaum, Irvine, 1985).

[20] P.E. Green and D.S. Tull, Research for Marketing Decisions (Prentice-Hall, New Jersey, 1978).

[21] M. Hammer and D. McLcod, Database Description with SDM: A Semantic Model, ACM Transaction Database Systems, Vol. 6, No. 3 (1981).

[22] J.A. Hartigan, Clustering Algorithm (John Wiley, New York, 1975).

[23] G. Huber, A Theory of the Effects of Advanced Information Technologies on Organizational Design, Intelligence, and Decision Making, working paper, Management Department, University of Texas (1989).

[24] D.G. Kemler, Holistic and Analytic Modes in Perceptual and Cognitive Development, in: T. Tighe and B. Shepp, Eds., Perception, Cognition, and Development: Interactional Analyses (Erlbaum, Hillsdale, NJ, 1983).

[25] K.S. Lashley, The Problem of Serial Order of Behavior, in: A. Jeffres, Ed., Cerebral Mechanism in Behavior – The Hixon Symposium (John Wiley, New York, 1951).

[26] M. Lebowitz, Experiments with Incremental Concept Formation: UNIMEM, Machine Learning, Vol. 2, No. 2 (1987).

[27] G.R. Martins, The Overselling of Expert Systems, Datamation (November, 1984).

[28] D.L. Medin and P.L. Schwanenflugel, Linear Separability in Classification Learning, Journal of Experimental Psychology: Human Learning and Memory (1981).

[29] W.F. Messier and J.V. Hansen, Inducing Rules for Expert System Development: An Example Using Default and Bankruptcy Data, Management Science 34, No. 12 (1988).

[30] R.S. Michalski and R.L. Chilausky, Learning by Being Told and Learning by Examples: An Experimental Comparison of Two Methods of Knowledge Acquisition in the Context of Developing an Expert System for Soybean Disease Diagnosis, International Journal of Policy Analysis and Information Systems 4, No. 2 (1980).

[31] R.S. Michalski and R.E. Stepp, Automated Construction of Classifications: Conceptual Clustering versus Numerical Taxonomy, IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 5, No. 4 (1983).

[32] J. Mylopoulos, P.A. Bernstein, and H.K.T. Wong, A Language Facility for Designing Interactive Database-Intensive Systems, ACM Transaction Database Systems, Vol. 5, No. 2 (1980).

[33] J.R. Olson and H.H. Rueter, Extracting Expertise From Experts: Methods for Knowledge Acquisition, Expert Systems (Fall 1987).

[34] D.E. O'Leary, Methods of Validating Expert Systems, Interfaces 18 (1988).

[35] K.C. Pamela, Why Expert Systems Fall? Financial Management 17, No. 2 (1988).

[36] J.R. Quinlan, Discovering Rules by Induction from Large Collection of Examples, in: D. Michie, Ed., Expert Systems in the Micro Electronic Age (Edinburgh University Press, Edinburgh, 1979).

[37] J.R. Quinlan, Learning Efficient Classification Procedures and Their Applications to Chess End Games, in: R.S. Michalski, J.G. Carbonell and T.M. Mitchell, Eds., Machine Learning: An Artificial Intelligence Approach, Vol. I (Tioga Publishing Company, Palo Alto, 1983).

[38] I. Rock, The Logic of Perception (MIT Press, Cambridge, MA, 1983).

[39] M.J. Shaw and J.A. Gentry, Using an Expert System with Inductive Learning to Evaluate Business Loans, Financial Management 17, No. 3 (1988).

[40] R. Simon, The Morning After, Forbes (October 19, 1987).

[41] J.M. Smith and D.C.P. Smith, Database Abstractions: Aggregation and Generalization, ACM Transactions on Database Systems, Vol. 2, No. 2 (1977).

[42] R.E. Stepp and R.S. Michalski, Conceptual Clustering: Inventing Goal-Oriented Classifications of Structured Objects, in: R.S. Michalski, J.G. Carbonell, and T.M. Mitchell, Eds. Machine Learning: An Artificial Intelligence Approach Vol. 2 (Morgan Kaufmann, Los Altos, 1986).

[43] B. Stroustrup, What is Object-Oriented Programming, IEEE Software (May 1988).

[44] K.Y. Tam, Automated Construction of Knowledge-bases from Examples, Information Systems Research 1, No. 2 (1990).

[45] D.A. Waterbank, A Guide to Expert Systems (Addison-Wesley, 1986).

[46] P.H. Winston, Artificial Intelligence (Addison-Wesley, 1984).
