---
otero_id: 26262
otero_key: "93UZSHS7"
title: "Automated Construction of Knowledge-Bases from Examples"
authors: "Kar Yan Tam"
year: "1990"
journal: "Information Systems Research"
doi: "10.1287/isre.1.2.144"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.255.6.125] On: 19 September 2016, At: 09:04 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## H4R

![](/api/attachments/93UZSHS7/fulltext/images/c1b02a9550a801a962dcb1eb8b9fb980b85ca4a62f2f460528aa0dd0770036eb.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Automated Construction of Knowledge-Bases from Examples

Kar Yan Tam,

To cite this article:

Kar Yan Tam, (1990) Automated Construction of Knowledge-Bases from Examples. Information Systems Research 1(2):144-167. http://dx.doi.org/10.1287/isre.1.2.144

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1990 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/93UZSHS7/fulltext/images/a769f896e320900df9ff0c81442856e1b61aecbb361dc28a89a71da78602aad3.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Automated Construction of Knowledge-Bases from Examples

Kar Yan Tam

Department of Management Science and Information Systems

College and Graduate School of Business CBA 5.202

University of Texas at Austin

Austin, Texas 78712

The process of knowledge acquisition has long been regarded as the bottleneck in expert systems development. In this paper, a concept induction methodology for automated construction of knowledge-bases is presented and its use for knowledge acquisition is discussed. The applicability of such a tool to build expert systems is demonstrated using CONIS in some selected experiments. CONIS is a concept induction system that infers concept description from sample instances of the concept. We have also compared CONIS with conventional statistical techniques in solving classification problems. The results suggest that concept induction could become be a viable tool to automate the process of knowledge acquisition. By shortening the development cycle, domains that were once too volatile for expert systems application would become feasible using such an automated aid.

Expert systems—Knowledge acquisition—Machine learning—Knowledge-bases

## 1. Introduction

ne of the key issues in building an expert system is the acquisition of expert knowledge. Broadly, the term “knowledge acquisition" refers to the collective processes of eliciting, structuring, and coding human expertise in a form that is computationally tractable on a computer. This task is presently accomplished by repeated interviews between an expert and a knowledge engineer. The process, however, can be lengthy and is generally regarded as the bottleneck in expert systems development (Buchanan 1982, Boose 1986). Although widely adopted by knowledge engineers as the means to acquire knowledge, the interview method has a number of pitfalls. The major criticisms are:

(1) knowledge engineers fail to ask relevant questions;

(2) experts cannot articulate their expertise at the same competence level as they exercise it;

(3) there is no systematic way to compile and aggregate expertise from different sources;

(4) the lengthy process of interviews often renders it uneconomic to build expert systems in rapidly changing domains that require frequent updates of the knowledge-base.

The above criticisms are also applicable to techniques such as protocol analysis (Newell and Simon 1972) and discourse analysis (Hendrix 1979) which require verbal transcripts from the experts. Knowledge compiled from verbal transcripts may not be reliable because people often cannot articulate their reasoning processes precisely. It was suggested by Ericsson and Simon (1984) that only information residing in short term memory can be verbalized. Since human expertise embodies skills, heuristics, and problem-solving techniques that have evolved through years of practice, it may well be difficult to articulate. For a comprehensive account on the problems of using verbal data, the readers should refer to the work of Ericsson and Simon (1984) and of Bainbridge (1986)

Attempts have been made to circumscribe the bottleneck problem by building automatic or semi-automatic knowledge acquisition systems. CONIS (short for CONcept Induction System) is an experimental system developed for this purpose. The objective of this paper is not to study CONIS per se but rather to demonstrate the general applicability of such a system to knowledge acquisition. CONIS also serves as a testbed for a number of experiments conducted to compare concept induction with other statistical classification methods. CONIS shares a number of features that are common to other concept induction systems, our hope is that by discussing the mechanism of CONIS, the readers will gain a general understanding of concept induction and its application to expert systems development.

## 1.1. Background

Concept induction is a branch of machine learning research concerned with the acquisition of concept descriptions from examples. The principle of concept induction is to infer the general description of a concept by inspecting specific instances of the concept. Since concept induction is example-driven, it is also called “learning by example" or “induction learning." Winston's ARCH, one of the pioneers of this kind (Winston 1975), is a system that learns concepts (e.g., arch) in the block world. Other early experimental machine learning systems of this type include AQ (Michalski and Larson 1978, Michalski 1983), Mitchell's Version Space approach (Mitchell 1977), ID3 (Quinlan 1986), Thoth (Vere 1975), SPROUTER (Hayes-Roth and McDermott 1977), and Meta-DENDRAL (Buchanan and Mitchell 1978). These systems, together with a series of reports by their inventors, have established the basic principle of the mechanization of learning from examples.

It has long been suggested by AI researchers that these learning systems can be used to extract decision rules from past experience (Michie 1980). In fact, there are strong indications that concept induction could become a useful tool in building expert systems that deal with classification problems such as credit analysis and medical diagnosis. For instance AQ11 developed by Michalski and Chilausky (1980) has outperformed human experts in soybean disease diagnosis. Another successful application is a 2500-rule expert system built by British Petroleum for the design of hydrocarbon separation vessels. With the aid of an induction system, the project was completed in one year (Expert System User 1986).

The design of CONIS was inspired by the success of these systems. Like other induction learning systems, CONIS is designed to acquire diagnosis or classification knowledge. In practice, the use of concept induction systems should be viewed as a complement rather than a replacement for the interviewing process. Expert systems that perform tasks other than classification, such as planning, interpretation, design, instruction, monitoring and prediction (Stefik, Aikins, Balzer, Benoit, Birnbaum, Hayes-Roth and Sacerdoti 1982) still rely on interviewing as the primary knowledge acquisition medium. Yet some of the limitations associated with the interview method can be alleviated by using concept induction systems.

This current study has two objectives: (1) to discuss and demonstrate the general applicability of concept induction to expert systems development, and (2) to evaluate and compare concept induction with other statistical classification techniques. Discussions and comparisons are presented using CONIS as an example throughout the paper. The following section gives an overview of related work in machine learning. Section 3 follows with a detailed description of the concept induction methodology underlying CONIS. Section 4 discusses the implementation and evaluation of CONIS based on a number of experiments. Comparisons between discriminant analysis and concept induction in solving classification problems are discussed in §5. Section 6 concludes the paper with a discussion on future research directions and possible extensions of CONIS.

## 2. Related Work in Machine Learning

The ability to learn is a distinctive feature of intelligent beings. The goal of understanding the nature and the process of learning is shared by a number of disciplines (e.g., psychology, philosophy, biophysics, economics, cybernetics). In computer science, learning-related research was primarily focused on learning automata, neural modelling and grammatical inference in the 1950s and 1960s. With the advent of hardware and software technologies, the focus of research has been shifting towards a balance between theoretical study and experimental implementation. Recently, this is an increasing interest in machine learning and its applications, due in part to the success of some experimental systems. According to Fisher (1987), machine learning is concerned with “improving performance by automating knowledge acquisition and refinement."The different approaches to machine learning and their relation with CONIS are discussed in this section.

## 2.1. Learning Model

The most important element of a machine learning system is its learning model. The model describes (1) the setting of learning, (2) the entities involved in the learning process, (3) the goal of learning and (4) the mechanism of learning. Such a model provides operational guidelines to construct a learning program. The learning model of CONIS which is based on Dietterich's model (1982) is shown in Figure 1. It consists of three elements: (1) a learner, (2) a knowledge-base, and (3) a performance element. These three elements together form a self-contained entity that responds to stimuli from the environment. In this paper, we will focus on CONIS's learner. The performance element of CONIS, basically a classification system similar to that of a conventional rule-based inference engine, applies learned rules to perform classification tasks. How well the performance element perform is evaluated by its classification accuracy which in turn determines the degree of validity of the learned rules. Thus, CONIS's learning model is performance-driven. Improving performance is a salient feature in any learning process, as reflected in Simon's definition of learning (Simon 1983): “Learning denotes changes in the system that are adaptive in the sense that they enable the system to do the same task or tasks drawn from the same population more efficiently and more effectively the next time."

CONIS's learning model can be embodied in the larger Q-Morphism framework suggested in Holland, Holyoak, Nisbett, and Thagard (1986). Holland et al. maintained that success in any problem-solving activity hinges on the availability of an efficient model of the real world, and that learning is goal driven and should be defined in the context of problem-solving. A q-morphism is a model of the world by dividing the world into categories of states which are useful to achieve certain goals in a problem-solving activity. State changes in the world are captured by a transition function specifying the mapping between categories in a q-morphism. Categories in a q-morphism are organized as a default hierarchy. A higher layer, which is more general, provides default expectations unless certain exception categories are signalled. Exception categories are handled by more specific layers residing lower in the hierarchy. The process of learning is equivalent to continuously refining a q-morphism to approximate the world. A q-morphism can be realized as a rule-based system employing two kinds of rules: synchronic and diachronic rules. Synchronic rules describe category and association relationships between categories. Diachronic rules specify the transition function of a q-morphism. The learning model of CONIS is a special case of the q-morphism framework. CONIS's rules correspond to the synchronic rules of a q-morphism. The goal of CONIS's learner is to infer synchronic rules describing certain category relationships between objects in the real world.

![](/api/attachments/93UZSHS7/fulltext/images/8c4982fe8c5ad18983f2c2ef48b2464e077af6ad8316b4893c6ec1662c955af1.jpg)  
Learning System  
FiGURE 1. A Model of Machine Learning Systems.

## 2.2. Learning Strategies

There are so far five strategies to mechanize the process of learning. They are (1) rote learning, (2) learning by examples, (3) learning by observation, (4) learning by analogy and (5) explanation-based learning.

## 2.2.1. Rote Learning

In rote learning, which is the most direct form of learning, knowledge is “spoonfed" by a teacher to the learner. Programming is a form of rote learning in the sense that the computer simply follows the specification stated in the program. The degree of inference on the part of the learner is very limited. The learner is primarily concerned with storing the knowledge in a form that facilitates rapid retrieval later. Samuel (1959) used this technique to enhance state evaluation in a system that learned how to plav checkers. Most expert systems have been constructed using this strategy either directly by an expert or indirectly by a knowledge engineer.

## 2.2.2. Learning by Examples

Learning by examples or inductive learning is a kind of supervised learning because a teacher provides both positive and negative examples of a concept. The learner must generalize these examples so that the generalized concept can be used for prediction in the future. Induction systems such as AQ (Michalski and Chilausky 1980), Michalski (1983), Meta-DENDRAL (Buchanan and Mitchell 1978), ID3 (Quinlan 1986), SPROUTER (Hayes-Roth and McDermott 1977) have been constructed using this strategy to acquire knowledge in different domains and in various forms.

## 2.2.3. Learning by Observation (Unsupervised Learning)

Learning by observation, another form of inductive learning, does not require tagging the training instances, therefore, it is also called unsupervised learning. Since examples are not tagged, they are simply called observations. Each observation is described by a list of attribute-value pairs. According to the similarity between attribute-value pairs of different observations, a taxonomical hierarchy is derived which can be used to classify new observations. The conceptual clustering technique was built on this learning strategy (Michalski 1980, Fisher and Langley 1985). One of the earliest conceptual clustering systems is a program called CLUSTER/2 developed by Michalski and Stepp (1983). Recent developments in conceptual clustering have introduced systems that are capable of acquiring knowledge in an incremental manner and are applicable in a larger context (Lebowitz 1987, Fisher 1987)

## 2.2.4. Learning by Analogy

To learn by analogy is to create new concepts by transforming and augmenting existing ones which are similar to the new concepts. A concept can be a physical object or a problem-solving method. According to Carbonell (1983), the process is broken down into two phases: first, existing concepts which bear strong similarity with a new concept are sought; second, these concepts are mapped to the new concept. Successful systems based on learning by analogy require a reasonable measure of similarity. However, a general definition of this measure is difficult because it depends upon the kinds of concepts under consideration and the context of comparison. Because of this deficiency, relatively few systems have been implemented in this category.

## 2.2.5. Explanation-based Learning

Like induction learning, explanation-based learning is example driven, and the example is also tagged. The primary difference between learning by explanation and learning by examples is that the former focuses on a single example, and explains it by using its domain-specific knowledge (Mitchell, Kedar-Cabelli and Keller 1986, De-Jong and Moonley 1986). Applications of explanation-based learning can be found in VLSI circuit designs (LEAP by Mitchell, Mahadevan and Steinberg 1986), satellite control system (ACES by Pazzani 1986) and stories understanding (DeJong 1983). The ability to generalize a concept based on a single example lies in the availability, to the learner, domain-specific knowledge pertaining to the given example. For instance, to explain why a given VLSI circuit works (or does not work) will require prior knowledge in circuit theory. However, such background knowledge is usually not required in learning by examples

![](/api/attachments/93UZSHS7/fulltext/images/32f186e54da454410ebc78bc7bc01b288238bbd0281f157c25c1b775faad4ca3.jpg)  
FIGURE 2. A Schematic Diagram of CONIS.

## 3. Methodology of Concept Induction

CONIS is a knowledge acquisition system that is built on the principle of learning by examples. The schematic diagram of CONIS is shown in Figure 2. There are three inputs to the induction procedure: (1) example instances, (2) induction operators, and (3) induction criteria. The output consists of a concept description in the form of classification rules.

By induction, we mean the inference of general principles from specific instances. The inference process is described pictoraially in Figure 3. Given a collection of examples (positive and negative examples of a concept), the induction procedure will search for rules that are consistent with the input examples. The search is performed by systematically applying the induction operators to generate and test candidate classification rules. Unlike most induction systems which have a rigid consistency measure, CONIS allows a knowledge engineer to state his own preference for the degree of consistency. This is accomplished by assigning different parameter values to the induction procedure.

![](/api/attachments/93UZSHS7/fulltext/images/00a19dfe218a5390a4c8f34883583d75649b10d75d4b9f78eba5dcd8a59b96d6.jpg)

=> - partitioning of the attribute space

o - positive example

x - negative example

FiGURE 3. Examples Driven Induction Procedure

![](/api/attachments/93UZSHS7/fulltext/images/cebf2b089dd57a8ebd93e526ddeff9cc766fb07ffdb8ab0f48510c01a5938663.jpg)  
FIGuRE 4. An Example of the Acyclic Graph of a Structural Attribute.

For candidate rules that satisfy the induction criteria, CONIS will attempt to further generalize them until the criteria are violated. In terms of space partitioning, the positive and negative examples serve as initial partitions of the attribute space. CONIS applies the induction operators to expand, split and merge the candidate partitions (rules) during the search. The allowable degree of generalization of a partition is determined by the number of positive and negative examples covered by the partition. The exact number is specified in the induction criteria by the knowledge engineer. We proceed by first describing how concepts are represented in CONIS.

## 3.1. Concept Representations

In CONIS, examples and concept descriptions are represented in the same form. Each example or concept is described by a list of attribute-value pairs.

$$
C _ {1} C _ {2} \cdot \cdot \cdot C _ {n} \Rightarrow D
$$

where $C _ { i } , 1 \le i \le n ,$ are the attribute-value pairs corresponding to the conditions of a production rule, and D is the concept identification also stated as an attribute-value pair. Each attribute A is associated with a domain denoted by Dom(A) which specifies all possible values of A. There are two types of attributes in CONIS, namely, nominal and structural attributes. For nominal attributes, their domains are simply sets of elements. For example, Dom(Course) = {CS112, EE101, Math124}. For a structural attribute, there exists a binary relation ISA between its elements. Such an ISA relation represents the inheritance relationship between elements of a structural domain.

In CONIS, the ISA relation of a structural attribute S is represented by an acyclic graph $G = \langle V , E \rangle$ , where $V = \mathbf { D o m } ( S )$ and ${ \pmb E } = \pmb { \mathrm { I S A } }$ where (Dom(S) × Dom(S)) $\supseteq$ iSA. While only tree-like relations are supported in other induction systems, CONIS allows attribute values to be represented as an ayclic graph. The ability to “inherit" from different value hierarchies makes it possible for CONIS to “switch context" during an induction process. For instance, in Figure $^ { 4 , }$ East Germany is an European nation as well as a communist state.' It will be too restrictive if only tree-like ISA relations are permitted. CONIS will attempt to generalize rules according to the different branches associated with the acyclic graph of a structural attribute.

## 3.2. Induction Operators

Induction operators are functions that transform a single concept description into one or more general descriptions; hence, they are also called generalization operators.

Three operators are used in CONIS, namely (1) dropping-condition, (2) extendingreference, and (3) climbing-up-acyclic-graph. Each of these operators is explained in more detail below

(1) Dropping-condition. The dropping-condition operator generalizes a rule by dropping a condition from the rule. For example,

$$
(\text { Trade - Deficit   large }) (\text { Japan - Interest - Rate   high }) \Rightarrow (\text { Buy   yen - future })
$$

is generalized to

$$
(\text { Trade - Deficit   large }) \Rightarrow (\text { Buy   yen - future }),
$$

and

$$
(\text { Japan - Interest - Rate   high }) \Longrightarrow (\text { Buy   yen - future }).
$$

This operator is applicable to both nominal and structural attributes.

(2) Extending-reference. The extending-reference operator generalizes a rule by expanding the value set of one or more of its attributes. This operator can only be applied to nominal attributes in the current version of CONIS. For example,

$$
(\text { Trade - Deficit   medium }) \Rightarrow (\text { Buy   yen - future })
$$

is generalized to

$$
(\text { Trade - Deficit } \{\text { medium }, \text { large } \}) \Rightarrow (\text { Buy   yen - future }),
$$

and

$$
(\text { Trade - Deficit   } \{\text { low,   medium } \}) \Rightarrow (\text { Buy   yen - future })
$$

$$
\text { where   } \operatorname{Dom} (\text { Trade - Deficit }) = \{\text { low,   medium,   high } \}.
$$

(3) Climbing-up-acyclic-graph. The climbing-up-acyclic-graph operator, which is applied only to structural attributes, replaces the value of a structural attribute with a more general one as implied by its ISA relation (i.e., this operator climbs up the acyclic graph of a structural attribute).

For example in Figure $4 , ^ { 2 }$

$$
(\text { Country   E.   Germany }) \Rightarrow (\text { Economy   central - planning })
$$

is generalized to

$$
(\text { Country   European   Nation }) \Rightarrow (\text { Economy   central - planning })
$$

and

$$
(\text { Country   Communist   Country }) \Rightarrow (\text { Economy   central - planning })
$$

where (E. Germany, European Nation〉 and (E. Germany, Communist Country> ∈ ISA.

## 3.3. Induction Criteria

As mentioned earlier, performance is a major concern in any learning task. The performance measure CONIS is closely related to its induction criteria. In a survey by

Angluin and Smith (1983) on inductive inference, the majority of practical and theoretical studies on inductive inference methods are associated with two conflicting criteria: simplicity and goodness of fit. In CONIS, simplicity is measured by the number of conditions of a classification rule, while goodness of fit is assessed by its degree of consistency with the examples. Based on these two criteria, a simple and consistent description is sought in characterizing a concept. Given the same degree of consistency. CONIS would prefer a rule that has the fewest attribute-value pairs in its condition part. Thus, less information would be needed to make a decision. Computationally, simpler rules are more efficient in a rule-based system because fewer attribute-value pairs need to be matched during reasoning. This requirement is crucial in application domains such as medical diagnosis or foreign exchange trading where fast decisions are essential.

In a search for the simplest description of a concept, the resultant rule might involve few attribute-value pairs. Although efficient, it might be too general to apply. For instance, the statement “all human beings are good students"is too general in describing good students. In order to prevent a rule from being overly generalized, the induction process in CONIS is driven by the provided examples. In CONIS, the ideal case is to have rule(s) that separate all positive examples from negative examples. However, such a rule (or set of rules) would probably be very complicated $( \ i . \ e . ,$ consist of many attribute-value pairs) in order to cover all positive examples and reject all negative examples. The extreme case is to have all positive examples serve as the classification rules. However in this case, the classification rules are too specific to be useful. As one can see, simplicity and goodness of fit are two conflicting criteria that require a trade-off to be made by the knowledge engineer. In CONIS, the tradeoff between these two criteria is specified by five parameters:

$w _ { 1 }$ —minimal percentage of positive examples covered by a rule (local)

$w _ { 2 } \cdot$ —minimal percentage of negative examples rejected by a rule (local)

$w _ { 3 }$ —maximal number of attribute-value pairs in the condition part of a rule

$w _ { 4 }$ —minimal percentage of positive examples covered by a set of rules (global)

$w _ { 5 }$ —minimal percentage of negative examples rejected by a set of rules (global)

Here, a distinction is made between the number of examples covered (or rejected) by a rule and that covered (or rejected) by a set of rules. The reason for introducing ${ \pmb w } _ { \pmb q }$ and ${ \pmb w } _ { \pmb 5 }$ is that more than one rule may be required to classify a concept. This happens when examples form clusters in the attribute space which need to be described individually. Therefore, $w _ { 4 }$ and $w _ { 5 }$ are required when rules of the same concept are assessed collectively. For instance in Figure ${ \mathfrak { s } } ,$ there are two positive and two negative examples in a space defined by two attributes. Suppose we specify that each rule in Figure 5 covers at least 30% of the positive examples $( w _ { 1 } = 3 0 \% )$ ) and rejects at least 30% of the negative examples $( w _ { 2 } = 3 0 \% )$ . Furthermore, we require that the two rules together cover 50% of the positive examples $( w _ { 4 } = 5 0 \% )$ and reject 20% of the negative examples $( w _ { 5 } = 2 0 \% )$ . In this example, $w _ { 3 }$ is set to 2. It is obvious that the two rules in Figure 5 are satisfied individually. However, if the two rules are considered jointly they together cover 100% of the positive examples and reject 0% of the negative examples! Clearly, the requirement $w _ { 5 } = 2 0 \%$ is violated.

As indicated in the previous example, there seems to exist a relationship between the global acceptânce/rejection rate and the local acceptance/rejection rate. In fact, given a set óf rules, the global acceptance rate is always greater than or equal to the local acceptance rate. But the reverse is true for rejection rates. That is, the local rejection rate is always greater than or equal to the global rejection rate. This happens because the proportion of positive examples covered by a rule cannot exceed the proportion covered by all the rules combined. Similarly, the proportion of negative examples rejected by a single rule cannot be smaller than the proportion rejected by all the rules combined. These two inequalities can be used as a guideline in selecting parameter values for $w _ { 1 } , w _ { 2 } , w _ { 4 }$ and $w _ { 5 }$ . We suggest that knowledge engineers use a set of parameters which satisfy the following conditions:

![](/api/attachments/93UZSHS7/fulltext/images/9c27ae33808c6287fad609d09ef9b14b72d47c818f124ab892c6c50789fe0104.jpg)  
FiGURE 5. An Example with Two Rules Each Covering 50% Positive Examples and 50% Negative Examples.

$$
\begin{array}{l l} (1) & w _ {1} \leq w _ {4} \\ (2) & w _ {5} \leq w _ {2}. \end{array}
$$

These two conditions, however, are neither sufficient nor necessary to guarantee a feasible solution. They simply serve as a heuristis in selecting a parameter set. To illustrate this, consider the following two sets of parameters with respect to Figure 5:

$$
\begin{array}{l} \text {(1)} w _ {1} = 30\%, w _ {2} = 50\%, w _ {3} = 2, w _ {4} = 20\%, w _ {5} = 0\% \\ \text {(2)} w _ {1} = 40\%, w _ {2} = 50\%, w _ {3} = 2, w _ {4} = 80\%, w _ {5} = 20\%. \end{array}
$$

The first set $( w _ { 1 } = 3 0 \% , w _ { 2 } = 5 0 \% , w _ { 3 } = 2 , w _ { 4 } = 2 0 \% , w _ { 5 } = 0 \%$ violates the first condition $( w _ { 1 } = 3 0 \% > w _ { 4 } = 2 0 \% )$ ) but is feasible. On the other hand, the second set $( w _ { 1 } = 4 0 \% , w _ { 2 } = 5 0 \% , w _ { 3 } = 2 , w _ { 4 } = 8 0 \% , w _ { 5 } = 2 0 \% )$ satisfies both conditions, but the two rules together are not a feasible solution $( w _ { s } = 2 0 \%$ is not satisfied)

The values selected for $w _ { 1 } \cdot \cdot \cdot w _ { 5 }$ represent the inductive criteria needed to be satisfied by the learned rules. The induction procedure, as discussed in the next section, may or may not find rules that are feasible with respect to a given set of examples. This happens either because the parameter values are too restrictive or they conflict with one another. Parameters are said to be conflicting if they violate the inequalities. In the former case, there is not much we can do except to change the inductive criteria. However, we can reduce the likelihood of parameter conflict by closely following the two conditions, $w _ { 1 } \leq w _ { 4 }$ and $w _ { 5 } \leq w _ { 2 }$ , Although the two conditions cannot guarantee feasible solutions, they help us avoid potential conflicting parameters. The importance of a non-conflicting parameter set will become apparent as we describe the induction mechanism in the next section.

## 3.4. Induction Procedure

The induction procedure is a generalization-based search algorithm [ ] that systematically applies induction operators to search for rules that satisfy the induction criteria. Positive examples serve as the seeds of generalization in the algorithm outlined below:

## Induction Algorithm

Input: $w _ { 1 } , w _ { 2 } , w _ { 3 } , w _ { 4 } , w _ { 5 }$ , positive examples, negative examples

Output: a set of rules that satisfy $w _ { 1 } , w _ { 2 } , w _ { 3 } , w _ { 4 } .$ , and $w _ { 5 }$

Method:

1. Initialize the candidate rule set with positive examples and the final rule set to $\left\{ \begin{array} { r l } \end{array} \right\}$

2. New rules are generated by applying induction operators (dropping-condition, extending-reference, and climbing-up-acyclic-graph) to a rule in the candidate rule set.

3. For each new rule generated in step 2, check to see ifit rejects at least $w _ { 2 }$ negative examples.

4. For each rule that satisfies $w _ { 2 }$ , check to see if it covers any existing rules in the candidate rule set. If ves, eliminate the redundant rule(s). Add the rule back to the candidate rule set.

5. For the parent rule (the parent rule is the rule which the induction operators are applied to in step $^ { 2 ) , }$ , check to see whether any of its children are added to the candidate rule set in step 4.

6. If none of its children are added to the candidate rule set in step $^ { 4 , }$ the parent is added to the final rule set only if all of the following are satisfied: (1) it covers at least $w _ { 1 }$ examples, (2) it contains less than $w _ { 3 }$ conditions, and (3) it is not covered by any rule in the final rule set. Delete the parent rule from the candidate rule set.

7. If the candidate rule set is not empty, go to step $^ { 2 , }$ otherwise proceed to step 8.

8. If the final rule is empty, then exit; otherwise see if the final rules satisfy ${ \pmb w } _ { \pmb 4 }$ and ${ \pmb w } _ { \pmb S }$

9. Output the final rule set.

The induction algorithm maintains two rule sets: the final rule set and the candidate rule set. Step 1 initializes the two rule sets with { } and positive examples, respectively. In Step 2, a rule is selected from the candidate rule set. Induction operators are then applied to generate generalized versions of the selected rule. The order of rules to be selected in the candidate rule set depends on the search mechanism. Two different search mechanisms, depth-first search without backtracking and breadthfirst search, are supported by CONIS. (This will be discussed further in §4.3.) Steps 3–4 determine which newly generalized rules are eligible for further generalization. To be eligible, a newly generalized rule must satisfy $w _ { 2 }$ . All eligible rules are then added to the candidate rule set. Steps 5-6 check whether the parent rule selected in Step 2 can be put in the final rule set. The decision is stated as follows: if all of its children are rejected in Step 4, the parent rule is discarded from the candidate rule set and is added to the final rule set only if it satisfies $w _ { 1 }$ and $w _ { 3 } ;$ ; otherwise, the parent rule is simply eliminated from the candidate rule set. In the first case, the parent cannot be generalized anymore. Such a parent rule represents a potential feasible solution and is saved in the final rule set for further checking against global parameters in Steps 8–9. In the second case, the children are more general than the parent rule itself, therefore there is no need to keep the parent. The above steps (Steps 2–7) are repeated until no more rules can be generalized (i.e., the candidate rule set becomes empty). After the procedure exits from the main search loop, rules in the final rule set are tested against the specified global parameters ${ \pmb w } _ { \pmb 4 }$ and $w _ { \mathfrak { s } }$ . Finally, the final rule set is output as the classification rules.

TABLE 1  
List of Attributes Used in the Congressmen Voting Experiment

<table><tr><td>Key Votes</td><td>Attribute</td><td>Domain</td></tr><tr><td>Raise Social Security Retirement age to 67 (1983)</td><td> $V_1$ </td><td>{Y, N}</td></tr><tr><td>Bar covert U.S. Aid to Nicaragua (1983)</td><td> $V_2$ </td><td>{Y, N}</td></tr><tr><td>Reduce dairy price support (1983)</td><td> $V_3$ </td><td>{Y, N}</td></tr><tr><td>Pass Equal Right&#x27;s Amendment (1983)</td><td> $V_4$ </td><td>{Y, N}</td></tr><tr><td>Freeze physicians&#x27; fees under Medicare (1984)</td><td> $V_5$ </td><td>{Y, N}</td></tr><tr><td>Bar aid to anti-Sandinista forces in Nicaragua (1984)</td><td> $V_6$ </td><td>{Y, N}</td></tr><tr><td>Pass bill to revise immigration laws (1984)</td><td> $V_7$ </td><td>{Y, N}</td></tr><tr><td>Cut education spending (1984)</td><td> $V_8$ </td><td>{Y, N}</td></tr><tr><td>Authorize procurement of 21 MX missiles (1984)</td><td> $V_9$ </td><td>{Y, N}</td></tr></table>

Y—voted for  
N—voted against

## 4. Implementation and Evaluation

CONIS is implemented using Franz Lisp in an Encore Multiprocessor UNIX environment. A number of experiments have been conducted to study the behavior of CONIS. Some of these experiments are simulation studies which investigate the behavior of CONIS under different grouping patterns of examples and using different search methods. Others are based on actual knowledge provided by users or extracted from texts. Two of these experiments are briefly reported in this section. Empirical findings based on these experiments will then be discussed.

## 4.1. Classification of Congressmen—A Voting Record Approach

The objective of this experiment is to obtain a general description of “conservative" and “liberal" congressmen based on their voting records on major issues in Congress. Democrats and Republicans are usually tagged with different ideologies—“liberal" for the former and “conservative" for the latter. In this experiment, Democrats and Republicans, respectively, serve as positive and negative examples of liberal congressmen. Since our classification is binary, the negation of the derived rules is used to describe conservative congressmen. One hundred congressmen, 50 Democrats and 50 Republicans, are randomly selected from Politics in America (Ehrenhatt 1985). Each congressman is described by his/her voting record on nine major issues in the 98th and 99th Congress. (A list of these issues is shown in Table 1.) Out of the 100 congressmen, 50 are used as training examples (25 Democrats and 25 Republicans). The remaining 50 (also evenly split into Democrats and

TABLE 2  
Sample Rule Sets of the Congressmen Voting Experiment

<table><tr><td rowspan="2">w1</td><td rowspan="2">w2</td><td colspan="2">Actual Global Rate</td><td colspan="2">Actual Classification Rate</td><td rowspan="2">Combined Classification Rate</td></tr><tr><td>Acceptance</td><td>Rejection</td><td>Acceptance</td><td>Rejection</td></tr><tr><td>10%</td><td>70%</td><td>92%</td><td>80%</td><td>84%</td><td>80%</td><td>82%</td></tr><tr><td colspan="7">classification rules: ((V9(N)))</td></tr><tr><td></td><td></td><td>((V2(Y)))</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>((V1(N)))</td><td></td><td></td><td></td><td></td></tr><tr><td>10%</td><td>90%</td><td>88%</td><td>80%</td><td>92%</td><td>88%</td><td>90%</td></tr><tr><td colspan="7">classification rules: ((V5(N)))</td></tr><tr><td></td><td></td><td>((V3(N)) (V4(Y)))</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>((V2(Y)) (V3(N)))</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>((V1(N)))</td><td></td><td></td><td></td><td></td></tr><tr><td>10%</td><td>100%</td><td>80%</td><td>100%</td><td>92%</td><td>92%</td><td>92%</td></tr><tr><td colspan="7">classification rules: ((V3(N)) (V9(N)))</td></tr><tr><td></td><td></td><td>((V3(N)) (V6(Y)) (V7(Y)))</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>((V3N)) (V4(Y)) (V7(Y)))</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>((V5(N)))</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>((V1(N)) (V3(N)) (V4(Y)))</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>((V2(Y)) (V3(N)))</td><td></td><td></td><td></td><td></td></tr><tr><td>20%</td><td>100%</td><td>76%</td><td>100%</td><td>88%</td><td>100%</td><td>94%</td></tr><tr><td colspan="7">classification rules: ((V5(N)))</td></tr><tr><td></td><td></td><td>((V1(N)) ((V3(N)) (V4(Y)))</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>((V2(Y)) (V3(N)))</td><td></td><td></td><td></td><td></td></tr><tr><td>30%</td><td>90%</td><td>68%</td><td>92%</td><td>80%</td><td>96%</td><td>88%</td></tr><tr><td colspan="7">classification rules: ((V2(Y)) (V3(N)))</td></tr><tr><td></td><td></td><td>((V1(N)))</td><td></td><td></td><td></td><td></td></tr><tr><td>40%</td><td>80%</td><td>84%</td><td>84%</td><td>72%</td><td>80%</td><td>76%</td></tr><tr><td colspan="7">classification rule: ((V9(N)))</td></tr><tr><td>50%</td><td>90%</td><td>84%</td><td>84%</td><td>72%</td><td>80%</td><td>76%</td></tr><tr><td colspan="7">classification rule: ((V9(N)))</td></tr></table>

Note: The training examples are used to calculate the actual global acceptance and rejection rates. Actual classification acceptance and rejection rates are calculated using the test examples. Combined classification rate is the average of the actual classification acceptance and rejection rates. Classification rules are derived using the depth-first (no backtracking) search option of CONIS.

Republicans) are used to evaluate the classification accuracy of the output rules from CONIS. Table 2 depicts sample rule sets with different induction criteria.

As shown in Table 2, the classification accuracy of CONIS is quite impressive. Correct classification rates up to 94% are obtained for small $w _ { 1 }$ values. Larger $w _ { 1 }$ values tend to cover more negative examples, decreasing the classification rate to 76%. The results indicate that five votes (i.e., $V _ { 1 } , V _ { 2 } , V _ { 3 } , \bar { V } _ { 5 }$ and $V _ { 9 } )$ are found to be significant in characterizing Democrats, implying that Democrats are divided among themselves in the remaining four issues.

## 4.2. An Investigation of the Pacific Basin Economy

The economic growth of the “Four Tigers" (the four Newly Industrialized Economies (NIEs): Hong Kong, Singapore, South Korea and Taiwan) was frenzied during the last two decades. The rapid growth of GNP in the past two decades has transformed these once unnoticed regions into a regime that plays a significant role in world trade. However, neighbors of these four NIEs did not experience the same economic growth rate. Some performed poorly during the same period of time. The objective of this experiment is to find out the commonalities of these four NIEs that distinguish them from other countries in the same region. Unlike the previous experiment in which predictability is a concern, this experiment focuses on the explanation of this economic phenomenon. With the exception of North Korea and Afghanistan, all countries in the Far East are used in this study. They are represented by 19 positive examples and 27 negative examples. Since the four NIEs are unique, no test example is used in this experiment. Data used in this experiment are obtained from various sources. Since these four economies are export-oriented, the attributes are mainly trade-related issues as shown in Table 3. An acyclic graph associated with each structural attribute is shown in Figure 6.

TABLE 3  
List of Attributes Used in the Pacific Basin Economy Experimeni

<table><tr><td colspan="2">Nominal Attribute</td><td>Domain</td></tr><tr><td rowspan="8"></td><td>Colony</td><td>{Yes, No}</td></tr><tr><td>Political Stability</td><td>{low, medium, high}</td></tr><tr><td>Military Budget</td><td>{low, medium, high}</td></tr><tr><td>Capital goods tariff</td><td>{Yes, No}</td></tr><tr><td>Natural resources tariff</td><td>{Yes, No}</td></tr><tr><td>Consumption goods tariff</td><td>{Yes, No}</td></tr><tr><td>Import quota</td><td>{Yes, No}</td></tr><tr><td>Currency valuation</td><td>{under, equal, over}</td></tr><tr><td>Structural Attribute</td><td colspan="2">Domain</td></tr><tr><td>Export Incentive</td><td colspan="2">{financial-incentive, factor-incentive, fiscal-incentive, state-incentive, low-interest-loan, interest-reduction, guarantee, tax-exemption, depreciation-allowance, exemption-remittance-customs-duties, training, research-development, infrastructure-development, all-export-incentive}</td></tr><tr><td>Industry</td><td colspan="2">{all-industry, light, heavy, natural, hi-tech, service, plastic, watch, consumer-electronics, toy, textile, light-machinery, food-processing, steel, chemical, ship-building, heavy-machinery, automobile, cement, crop, mining, fishing, fuel, computer, communication, defense, tourism, shipping, finance, trading}</td></tr><tr><td>Export Market</td><td colspan="2">{world, North-America, Europe, Asia, Canada, US, Japan, Asean (without Singapore), China, HK, Australia, S-Korea, India, UK, France, Italy, W-Germany, Taiwan, Singapore, developed-nations, developing-nations}</td></tr></table>

The results of this experiment show that these four NIEs are divided into two groups, with Hong Kong and Singapore forming one group and South Korea and Taiwan forming the other. The major difference between these two groups lies in their import trade policy, military spending as a percentage of GNP, and political stability. Hong Kong and Singapore do not raise import barriers against foreign imports, while South Korea and Taiwan do restrict or discourage foreign imports by setting up import barriers such as tariffs on consumption goods. Another distinction between the two groups is political stability. South Korea and Taiwan are considered to be less stable, and their military spending accounts for a larger percentage of GNP than in the other group. However, these two groups do share commonalities in their export incentives, export markets, undervalued currency, and in their being or having been a colony of another country. A sample rule set is shown in Table 4.

Tam  
![](/api/attachments/93UZSHS7/fulltext/images/2cbc3c93f62f1c886c6a8f193a1197716db4175dac5db22b5edb1231560b3b61.jpg)  
FiGuRE 6. Acyclic Graphs of Structural Attributes Used in the Pacific Basin Economy Experiment

## 4.3. Observations and Findings

On the basis of these experiments (including the above two), we have made a number of observations:

(1) Depth-first search (no backtracking) vs. breadth-first search: In general, depthfirst search is more efficient than breadth-first search. Efficiency is measured by the number of candidate rules generated before converging to a final rule set. Figure 7 depicts a typical program trace of the two search strategies. Given the same induction criteria $( \mathbf { e . g . , } w _ { 1 } = 2 0 \% , w _ { 2 } = 1 0 0 \%$ in Figure 7), depth-first search usually converges faster than breadth-first search. The reason for this is that breadth-first search tends to discover more overlapping rules (rules that differ in only one or two attributes), while depth-first search reduces this overlapping by pruning the search tree in the early stage of the search. Pruning is possible because the depth-first search method used by CONIS does not backtrack in the generalization process. The "deeper" the search goes, the more general the generated rules will be. It is very likely that the newly generated rules will eventually cover some existing rules in the candidate rule set. Elimination of redundant rules in Step 4 of the algorithm in effect prune some branches of the search tree. While breadth-first search is an exhaustive method, depth-first search with no backtracking will favor candidate rules will fewer conditions. As shown in Table 5, more rules are generated using breadth-first search than depth-first search (Table 2) under identical induction criteria.

<table><tr><td>TABLE 4A Sample Rule Set of the Pacific Basin Economy Experiment</td></tr><tr><td> $w_{1} = 20\%$  $w_{2} = 90\%$ </td></tr><tr><td>Actual Global Acceptance Rate: 100%Actual Global Rejection Rate: 86%</td></tr><tr><td>classification rules:((political Stability (high)) (Currency evaluation (equal under)) (Export (world)) (Export Incentive (all-export incentive)))((Colony (Yes)) (Export Incentive (all-export-incentive)) (Political (medium high)) (Military Budget (low)))((Political Stability (medium high)) (Industry (all-industry)) (Military Budget (medium)))((Colony (Yes)) (Export (world)) (Military Budget (medium)) (Industry (all-industry)))((Political Stability (medium)) (Military Budget (high)) (Currency (under)) (Consumption Goods Tariff (Yes)))((Military Budget (low high)) (Political Stability (medium)) (Currency evaluation (equal under))(Consumption Goods Tariff (Y)))((Colony (Yes)) (Political Stability (low medium)) (Military Budget (low high)) (Consumption Goods Tariff (Yes)) (Industry (all-industry)))((Colony (Yes)) (Military Budget (high)) (Export (world)) (Industry (all-industry)) (Currency (under))(Export Incentive (all-export-incentive)))((Colony (Yes)) (Export (world)) (Political Stability (low medium)) (Currency under)))</td></tr></table>

Note: Actual global acceptance and rejection rates are calculated using the training examples. Classification rules are derived using the depth-first (no backtracking) search option.

![](/api/attachments/93UZSHS7/fulltext/images/4a42549dcf84645afffc68ae7a66b811877a84e843b6d86e51af8d1b85a886c7.jpg)  
FiGURE 7. A Sample Program Trace of Depth-first Search (No Backtracking) and Breath First Search under Identical Induction Criteria.

TABLE 5  
Sample Rule Sets of the Congressmen Voting Experiment Using Breath-first Search Method

<table><tr><td rowspan="2"> $w_1$ </td><td rowspan="2"> $w_2$ </td><td colspan="2">Actual Global Rate</td><td colspan="2">Actual Classification Rate</td><td rowspan="2">Combined Classification Rate</td><td></td></tr><tr><td>Acceptance</td><td>Rejection</td><td>Acceptance</td><td>Rejection</td><td></td></tr><tr><td>20%</td><td>100%</td><td>88%</td><td>100%</td><td>92%</td><td>92%</td><td>92%</td><td></td></tr><tr><td colspan="2">classification rules:</td><td colspan="6"> $((V_3 (N)) (V_9 (N)))$  $((V_1 (N)) (V_4 (Y)) (V_7 (N)))$  $((V_2 (Y)) (V_6 (Y)) (V_7 (N)))$  $((V_1 (N)) (V_6 (Y)) (V_7 (N)))$  $((V_6 (Y)) (V_7 (N)) (V_9 (N)))$  $((V_1 (N)) (V_5 (N)))$  $((V_2 (Y)) (V_5 (N)))$  $((V_4 (Y)) (V_5 (N)))$  $((V_3 (N)) (V_8 (N)))$  $((V_5 (N)) (V_7 (N)))$  $((V_1 (N)) (V_2 (Y)) (V_3 (N)))$  $((V_1 (N)) (V_3 (N)) (V_6 (Y)))$  $((V_2 (Y)) (V_3 (N)) (V_4 (Y)))$  $((V_2 (Y)) (V_3 (N)) (V_6 (Y)))$  $((V_4 (Y)) (V_7 (N)) (V_8 (N)))$ </td></tr><tr><td>30%</td><td>100%</td><td>76%</td><td>100%</td><td>88%</td><td>100%</td><td>94%</td><td></td></tr><tr><td colspan="2">classification rules:</td><td colspan="5"> $((V_1 (N)) (V_5 (N)))$  $((V_3 (N)) (V_5 (N)))$  $((V_4 (Y)) (V_5 (N)))$  $((V_5 (N)) (V_6 (Y)))$  $((V_1 (N)) (V_3 (N)) (V_8 (N)))$  $((V_2 (Y)) (V_3 (N)) (V_4 (Y)))$ </td><td></td></tr></table>

Note. The training examples are used to calculate the actual global acceptance and rejection rates. Actual classification acceptance and rejection rates are calculated using the test examples. Combined classification rate is the average of the actual classification acceptance and rejection rates. Classification rules are derived using the breadth-first search option of CONIS.

Another interesting observation which deserves further investigation is that as ${ \pmb w } _ { \bf l }$ increases, both search methods tend to converge to the similar rule set. For example, both methods generate the same rule $( \mathrm { i } . \mathsf { e } . , ( V _ { 9 } ( \mathbb { N } ) ) )$ for $w _ { 1 } \geq 4 0 \%$ in the congressmenvoting experiment.

(2) Discovering clusters: For those examples that form clusters (sets of examples that share similar attributes), the “seed growing" algorithm of CONIS is able to rediscover these clusters. However, for sparse positive examples, the generalization process is less efficient. A larger number of overlapping candidate rules are generated before converging to a final rule set. It also requires a smaller w, in this case. $w _ { 1 }$

(3) Redundancy checking is very important: A redundancy check is performed every time a rule is added to the candidate rule set. Such checks largely reduce the number of duplicating rules in the rule set, and hence improve the efficiency of the procedure.

(4) In classification tasks involving a small number of mutually exclusive categories (e.g., granting a loan vs not granting a loan), the induction algorithm can start with negative examples. The result is the negation of the final rules. In general, it is not feasible to learn from negative examples, particularly in the case of “unimodal" categories. This is because what constitutes a negative example is not clear in these situations.

(5) For faster processing, classification rules of a concept can be translated to a production rule language that supports disjunction (i.e., OR). Using disjunctive operators the final rule set can be translated into a single rule. Such a translation can be done by evoking the optional rule translator shown in Figure 2. For example, the third rule set shown in Table 2 is equivalent to the following rule:

$$
\begin{array}{l} \left(\text { (OR } (V _ {5} (\mathrm{N})) \text {(AND} (V _ {3} (\mathrm{N})) \text {(OR} (V _ {9} (\mathrm{N})) (V _ {2} (\mathrm{Y})) \text {(AND} (V _ {6} (\mathrm{Y})) (V _ {7} (\mathrm{Y}))) \text {(AND} (V _ {4} (\mathrm{Y})) \text {(OR} (V _ {7} (\mathrm{Y})) (V _ {1} (\mathrm{N})))))\right) \Rightarrow \text {(Congressman Conservative)} 0. 9 0). \end{array}
$$

A common approach to measure the validity of a rule is the use of confidence factors (CF). The confidence factor of a rule, which usually takes on values between 0 and 1 (or –1 and 1), is a subjective assessment of the rule by a human expert. In CONIS, the confidence factor of a rule is measured by the degree of consistency of the rule with respect to the examples. A straightforward way to calculate the CF of a rule is the weighted average of the proportion of positive examples covered and negative examples rejected by the rule. For example, the CF of the above rule is 0.9 which is calculated by averaging its global acceptance rate (0.8) and global rejection rate (1.0) $\left( \mathrm { i . e . , } \left( 0 . 5 \right) \left( 0 . 8 \right) + \left( 0 . 5 \right) \left( 1 . 0 \right) \right)$ 1

## 5. Concept Induction vs. Discriminant Analysis: A Micro-Study

While both concept induction and discriminant analysis deal with classification problems, the difference between the two can be viewed as that between symbolic and numerical classification. Discriminant analysis is concerned with the classification of observations into two or more groups on the basis of one or more numeric variables. Early application of statistical theory to discriminant analysis can be dated back to a classic paper by Fisher (1936). Since then, a vast array of statistical techniques, both parametric and nonparametric, have been developed. While both concept induction and discriminant analysis are concerned with classifying objects into different classes, little has been done to compare the two. In this section, two statistical methods, logit regression and k-nearest-neighbor, are compared with CONIS in a classification task.³ We would like to compare the predictive accuracy of CONIS on novel data with that of the other two methods. Logit regression and kNN are chosen for two reasons: (1) both can handle category data in a properly coded form, and (2) the former requires a functional form and the latter does not, thus improving the generality of the comparison. The same congressmen data set is used in the experiment.

The logit model used is

Estimates of the Logit Model

TABLE 6

<table><tr><td colspan="5">Estimates of the Logit Model</td></tr><tr><td>Coefficient</td><td>Estimates</td><td>Standard Error</td><td> $\chi^2$ </td><td>P</td></tr><tr><td> $\beta_0$ </td><td>0.588</td><td>0.4878</td><td>1.46</td><td>0.2277</td></tr><tr><td> $\beta_3$ </td><td>-2.051</td><td>0.6871</td><td>15.16</td><td>0.0001</td></tr><tr><td> $\beta_5$ </td><td>-2.675</td><td>0.7320</td><td>7.85</td><td>0.0051</td></tr><tr><td> $\beta_9$ </td><td>-1.452</td><td>0.5728</td><td>6.42</td><td>0.0113</td></tr></table>

Model $\pmb { \chi } ^ { 2 } = 9 8 . 6 0$  
Sample șize = 100

$$
Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \beta_ {3} X _ {3} + \beta_ {4} X _ {4} + \beta_ {5} X _ {5} + \beta_ {6} X _ {6} + \beta_ {7} X _ {7} + \beta_ {8} X _ {8} + \beta_ {9} X _ {9}\tag{5-1}
$$

and

$$
\operatorname{Prob} (Y) = 1 / \left(1 + e ^ {- Y}\right)\tag{5-2}
$$

where,

$$
\begin{array}{l l} Y = 1 & \text { if   Democrat } \\ = 0 & \text { if   Republican } \\ X _ {i} = - 1 & \text { if   voted   against } V _ {i}, \quad 1 \leq i \leq 9 \\ = 0 & \text { if   did   not   vote } \\ = 1 & \text { if   voted   for } V _ {i}, \quad 1 \leq i \leq 9. \end{array}
$$

Coefficients of the model are estimated using a stepwise maximum-likelihood procedure. Both forward and backward options are used, and the results are consistent with each other. Our first attempt to estimate the logit model using 50 training samples as we did in CONIS failed because the sample size was too small for 10 coefficients. Instead, all 100 congressmen in the initial data set were used to estimate the logit model. Reasonable estimates were obtained this time, as shown in Table 6.

Using the forward-stepwise procedure, a variable is added to the model only if it improves the chi-square of the model. Variables $\mathbf { X } _ { 3 } , \mathbf { X } _ { 5 } ,$ and $\mathbf { X } _ { 9 }$ are found to be significant (Table 6). All other variables are insignificant $( \mathbf { i . e . } ,$ , their coefficients are equal to zero). Classification accuracy of the logit model using the training data is shown in the first row of Table 7. Since the same data set is used for both estimation and testing, the result is biased.

TABLE 7  
Classification Accuracy of the Logit Model

<table><tr><td rowspan="2"></td><td colspan="2">Actual Global Rate</td><td rowspan="2">Combined Classification Rate</td></tr><tr><td>Acceptance</td><td>Rejection</td></tr><tr><td>Classification accuracy using training examples</td><td>92%</td><td>98%</td><td>95%</td></tr><tr><td>Classification accuracy using test examples</td><td>84%</td><td>84%</td><td>84%</td></tr></table>

Note: Combined classification rate is the average of global acceptance and rejection rates.

TABLE 8  
Classification Accuracy of the kNN Procedure

<table><tr><td rowspan="2">k</td><td colspan="2">Actual Global Rate</td><td colspan="2">Actual Classification Rate</td><td rowspan="2">Combined Classification Rate</td></tr><tr><td>Acceptance</td><td>Rejection</td><td>Acceptance</td><td>Rejection</td></tr><tr><td>2</td><td>60%</td><td>68%</td><td>72%</td><td>64%</td><td>68%</td></tr><tr><td>3</td><td>84%</td><td>84%</td><td>88%</td><td>88%</td><td>88%</td></tr><tr><td>4</td><td>76%</td><td>80%</td><td>88%</td><td>80%</td><td>84%</td></tr><tr><td>5</td><td>76%</td><td>84%</td><td>92%</td><td>84%</td><td>88%</td></tr></table>

Note: The training examples are used to calculate the actual global acceptance and rejection rates. Actual classification acceptance and rejection rates are calculated using the test examples. Combined classification rate is the average of the actual classification acceptance and rejection rates.

For comparison purposes, another 50 congressmen were randomly selected (Ehrenhatt 1985) to assess the classification accuracy of the logit model. The result is shown in the second row of Table 7. For each of the 50 congressmen, the probability of being a Democrat is calculated by plugging the congressman's voting record into the estimated logit model (5-1). The classification decision is to assign a congressman to the Democratic party if the associated probability (5-2) exceeds 0.5; otherwise, to the Republican party. Using test examples, the classification rate dropped from 95% to 84%.

While the logit model is limited in identifying disjoint clusters, the kNN procedure is capable of rediscovering clusters as the data reveals itself. The principle of this classification procedure is to classify an observation into the class that contains the majority of its first k nearest neighbors. Therefore, if there are dense regions in the data (i.e., if examples form clusters in the attribute space), it is very likely that the kNN procedure will rediscover these clusters. The distance between any two examples is defined as $( x - y ) / \mathbf { C O V } ^ { - 1 } ( x - y )$ where x and y are individual vectors, each representing the voting record of a congressman. COV is the covariance matrix of the examples. Given $\pmb { k } ,$ an observation is classified into the group that contains the majority of its first k nearest neighbors. In case of a tie, which only occurs in even k, the $k ,$ observation is concluded to be undecided. Using the same variable coding as in the logit model, the procedure is run with four different values of k (2 thru 5). The results are shown in Table 8.

The results show that the classification accuracy of kNN is not as good as that of CONIS. The best classification rate is 88% (with k = 3 and 5) as compared with 94% for CONIS. Another deficiency of kNN is due to its nonparametric nature; very little implication can be derived from the results in assessing the importance of individual variables.

The above experiment, though limited in scope and based on a single data set, does provide certain insights pertaining to these two methods in knowledge acquisition. They are summarized below:

(1) In parametric discriminant analysis, discriminant functions are usually derived from the optimization of certain criteria as compared with CONIS which is concerned with feasibility checking (i.e., set covering). Analytical solutions are available for most commonly used discriminant analysis techniques. However, extensive search is required for concept induction which renders it more time-consuming as compared with its statistical counterpart.

(2) Classification rules inferred from CONIS are expressed in symbolic form while the coefficients of discriminant functions might be difficult to interpret and validate without the assistance of experienced statisticians. Using CONIS, naive users can input examples in English-like syntax and obtain classification rules in self-explanatory form.

(3) To identify possible data clusters, a clustering analysis is usually performed prior to a discriminant analysis. This step is essential in parametric discriminant analysis because observations belonging to the same class often form clusters. Since the number of discriminant functions to be estimated is dependent on the number of distinct groups (clusters), classification accuracy will be impaired if the number of discriminant functions is not specified correctly. Furthermore, because commonly used discriminant analysis techniques are linear, the estimated coefficients of a discriminant function are interpreted conjunctively. Unless the number of discriminant functions corresponds properly to the number of distinct groups (or clusters), such an interpretation would be incorrect. CONIS adopts a “seed growing"algorithm that automatically takes care of grouped examples. We have performed experiments on CONIS by placing examples in clusters. Results of these experiments show that CONIS is able to rediscover these clusters in most of the cases.

(4) The ability to implant domain-specific knowledge in the induction process is a distinct feature of concept induction systems. CONIS enables two kinds of domain specific knowledge (structural attributes and prior information/belief of the concept) to be incorporated in the induction procedure. Hierarchical relationships can be specified in the form of acyclic graphs in CONIS. Since existing discriminant analysis techniques cannot take care of structural attributes, no comparison with CONIS is made in this regard. Furthermore, if prior information and/or belief of the concept is available, it can be incorporated in CONIS to guide the search. For example, given our belief of the economy stated as "(Unemployment-rate high) → (Economy bad)", the candidate rule set in Step 1 of the algorithm can be initialized with this rule as if it is one of the positive examples. The induction procedure will start generalizing the Unemployment-rate attribute by dropping the condition altogether or extending its value set. Generalization that starts with prior information is more efficient because it prunes redundant branches of the search tree earlier.

(5) Depending on the number of coefficients to be estimated, the size of the data set required may be very large in discriminant analysis. In the above experiment, the logit model requires 100 observations before reasonable estimates can be obtained. Yet its classification accuracy still lags behind CONIS which uses only half of the training examples. Thus, classification tasks which have a large number of variables but relatively few training examples may not be feasible using conventional discriminant analysis techniques.

## 6. Conclusion

In summary, we have presented a method to acquire expert knowledge in the form of classification rules and demonstrated its applicability to expert systems development using CONIS (short for CONcept Induction System) in two selected experiments. A virtue of CONIS is that it allows hierarchical representation of structural attribute values and adopts parametric induction criteria to assert the consistency and simplicity of the acquired rules. We have also compared CONIS with two statistical discriminant analysis techniques. Results based on these experiments indicate that concept induction is comparable with other statistical classification techniques in terms of classification accuracy. In some cases, it is even better. Implications derived from these experiments suggest that the choice between discriminant analysis and concept induction in extracting classification rules from experts is dependent on the following:

(1) How well do the examples satisfy the probability assumption of discriminant analysis?

(2) Is there any hierarchical relationships between elements in a domain?

(3) How competent is the knowledge engineer in interpreting results of discriminant analysis?

(4) Are prior information and/or beliefs of the concept available?

(5) How easily can the classification rules be incorporated in the knowledge-base?

The concept induction approach discussed here is obviously not “THE" solution to circumvent the bottleneck problem, but a competitive alternative among possible ones, especially under the following conditions:

(1) attributes exhibit hierarchical relationships;

(2) there is the availability of background knowledge and constraints;

(3) nominal and structural attributes dominate the attribute set;

(4) easy integration with symbolic expert systems development tools is possible.

In cases where examples exist in large numbers and follow a certain probability distribution, statistical techniques may be more appropriate in terms of robustness and computational efficiency. So far, the major deficiency of CONIS and concept induction systems in general is the time-consuming search process. In terms of CPU time, CONIS lags behind the statistical packages used in this study, due largely to the "generate-and-test" search method of CONIS, and partly to the time-consuming garbage collection process $( \mathbf { i . e . } ,$ , memory management) of Lisp. Depending on the number of examples, the CPU time of CONIS range from a few seconds to one and a half hours. Fine tuning of CONIS is underway to improve its performance.

The methodology presented here is, nevertheless, a candidate for extension and improvements. Heuristics can be incorporated in different steps of the algorithm to suit the needs of a particular task. For instance, the current version of CONIS applies purely syntactic induction operators which may not be computational efficient as the number of examples grows. The possibility of combinatorial explosions is high unless operators are applied more intelligently. For example, one can use a heuristic that has a preference to drop only those conditions which occur more frequently in the positive examples and less frequently in the negative examples. Likewise, the range of extension of the extending-reference operator can be increased to include more values. The question of what heuristics are appropriate depends, to a large extend, on the attribute domains and the distribution of values in the examples. Since these heuristics in one way or the other will generate “induction leaps,"their uses must be well orchestrated with the induction criteria to avoid conflicting situations (e.g., heuristics which lead to large induction leaps should be avoided if a large value, say 100%, is assigned to $w _ { 1 }$ and $w _ { 2 } )$

Furthermore, the current version of CONIS is nonincremental $( \mathbf { i . e . } ,$ , the entire procedure may need to be rerun for every new example). A possible extension of CONIS would be to make it incremental by applying heuristic rules to partition the old example set into two subsets, with one containing rules to be retained and one containing rules to be rerun with the new example. Another extension of CONIS is to apply heuristic rules to order the candidate rules for generalization. It was observed that the efficiency of the procedure is sensitive to the ordering of candidate rules. By generalizing the most “promising" rule first, duplicate effort in generalizing similar rules in the candidate rule set could be reduced. Extensions in these two directions would further improve the practical use of concept induction as a knowledge acquisition tool for expert systems development.

Acknowledgements. The author is grateful for the constructive comments from the Associate Editor and the anonymous reviewers.\*

\* Steven O. Kimbrough, Associate Editor, This paper was received on July 11, 1988, and has been with the author 5 months for 2 revisions.

## References

Angluin. D. and C. H. Smith. "Inductive Inference: Theory and Methods," Computing Survey, 15, 3 (1983), 237–269.

Bainbridge, L., “Asking Questions and Accessing Knowledge," Future Computing Systems, 1 (1986).

Boose, J. H., Expertise Transfer for Expert System Design, Elsevier, New York, 1986.

Buchanan B. G., “New Research in Expert Systems." in J. E. Hayes, D. Michie, and Y. H. Pao (Eds.), Machine Intelligence, 10 Edinburgh University Press, 1982

Buchanan. B. G. and T. M. Mitchell, "Model-Directed Learning of Production Rules,"in D. A. Waterman and F. Hayes-Roth (Eds.), Pattern Directed Inference Systems, Academic Press, New York, 1978.

Carbonell, J. G., “Learning by Analogy: Formulating and Generalizing Plans from Past Experience," in R S. Michalski. J. G. Carbonell, and T. M. Mitchell (Eds.), Machine Learning: An Artificial Intelligence Approach, 1 Morgan Kaufmann, Los Altos, CA, 1983.

DeJong, G. F., “Acquiring Schemata through Understanding and Generalizing Plans," Proceedings of the Eighth Internat. Joint Conf. on Artificial Intelligence, Pittsburgh, PA, 1982.

and R. Mooney. “Explanation-Based Learning: An Alternative View," Machine Learning, 1, 2 (1986), 145–176.

Dietterich. T. G., “Learning and Inductive Inference," in P. Cohen and E. Feigenbaum (Eds.), Handbook of Artificial Intelligence, 3 William Kaufmann, California, 1982.

Ericsson, K. A, and H. A. Simon. Protocol Analysis: Verbal Reports as Data, MIT Press, Cambridge, MA; 1984.

Ehrenhatt, A. (Ed.), Politics in America, Congressional Quarterly Press, Washington D. C., 1985

Expert System User, August 1986, 16–19.

Fisher, D. H., “Knowledge Acquisition via Incremental Conceptual Clustering," Machine Learning, 2, 2 (1987), 139–172.

Fisher. D. H. and P. Langley. “Approaches to Conceptual Clustering," Proceedings of the Ninth Internat Joint Conf. on Artificial Intelligence, Los Angeles, CA, 1985.

Fisher, R. A., “The Use of Multiple Measurements in Taxonomic Problems," Annals of Eugenics, 7, (1936) 179–188.

Haves-Roth. F. and J. McDermott. “Knowledge Acquisition from Structural Descriptions,"Proceedings of the Fifth Internat. Joint Conf, on Artificial Intelligence, Cambridge, MA, 1977.

Hendrix, G., in D. E. Walker, Ed., Discourse Analysis in Understanding Spoken Knowledge, Elsevier, New York, 1979.

Holland I. H.. K. F. Holvoak. R. E. Nisbett, and P. R. Thagard, Induction: Process ofInference, Learning, and Discovery, MIT Press, Cambridge, MA, 1986.

I ebowitz. M., "Experiments with Incremental Concept Formation: UNIMEM," Machine Learning, 2, 2 (1987), 103–138.

Michalski R. S.. “K nowledge Acquisition through Conceptual Clustering: A Theoretical Framework and

an Algorithm for Partitioning Data into Conjunctive Concepts," Internat. J. Policy Analysis and Information Systems, 4, 3 (1980), 219–244.

“A Theory and Methodology of Inductive Learning," in R. S. Michalski, J. G. Carbonell, and T. M. Mitchell (Eds.), Machine Learning: An Artificial Intelligence Approach, 1 Morgan Kaufmann, Los Altos, CA, 1983.

and R. L. Chilausky, "Learning by Being Told and Learning by Examples: An Experimental Comparison of Two Methods of Knowledge Acquisition in the Context of Developing an Expert System for Soybean Disease Diagnosis," Internat. J. Policy Analysis and Information Systems, 4, 2 (1980).

and J. B. Larson, “Selection of Most Representative Training Examples and Incremental Generation of VL1 Hypotheses: The Underlying Methodology and the Description of Programs ESEL and AQ11," Rep. No. 867, Computer Science Dept., University of Illinois. Urbana. 1978.

-and R. E. Stepp, “Automated Construction of Classifications: Conceptual Clustering versus Numerical Taxonomy," IEEE Transactions on Pattern Analysis and Machine Intelligence, 5. 4 (1983). 396-409.

Michie, D., “Inductive Rule Generation in the Context of the Fifth Generation."Proceedings ofthe Second Internat. Machine Learning Workshop, Urbana, Illinois, 1983.

Mitchell, T. M., "Version Spaces: A Candidate Elimination Approach to Rule Learning." Proceedings of the Fifth Internat. Conf. on Artificial Intelligence, Cambridge, MA, 1977.

S. Kedar-Cabelli, and R. Keller, “Explanation-Based Generalization: A Unifying Framework." Machine Learning, 1, 1 (1986), 47–80

S. Mahadevan, and L. Steinberg, "LEAP: A Learning Apprentice System for VLSI Design," Internat. Meetings on Advances in Learning, Les Arc, France, 1986.

Newell, A. and H. A. Simon, Human Problem Solving, Prentice-Hall, New Jersey, 1972.

Pazzani, M. J., "Explanation-Based Learning for Knowledge-Based Systems," Proceedings of the Knowledge Acquisition for Knowledge-based Systems Workshop, Alberta, Canada, 1986.

Quinlan, J. R., "Induction of Decision Trees," Machine Learning, 1, 1 (1986), 81–106.

Samuel, A. L., "Some Studies in Machine Learning Using the Game of Checkers," IBM J. Research and Development, 3 (1959), 210–229.

Simon, H. A., "Why Should Machine Learn?" in R. S. Michalski, J. G. Carbonell, and T. M. Mitchell (Eds.), in Machine Learning: An Artificial Intelligence Approach, 1 Morgan Kaufmann, Los Altos. CA. 1983.

Stefik, M., J. Aikins, R. Balzer, J. Benoit, L. Birnbaum, F. Hayes-Roth, and E. Sacerdoti, “The Organization of Expert Systems, A Tutorial," Artificial Intelligence, 18, 2 (1982), 135–173.

Vere, S. A., "Induction of Concepts in the Predicate Calculus," Proceedings of the Fourth Internat. Joint Conf. on Artificial Intelligence, Tbilisi, USSR, 1975.

Winston, P. H., "Learning Structural Descriptions from Examples," in P. H. Winston (Ed.), Psychology of Computer Vision McGraw Hill, New York, 1975.
