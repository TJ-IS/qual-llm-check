---
otero_id: 14166
otero_key: "MTW5UUB5"
title: "On the Ontological Quality and Logical Quality of Conceptual-Modeling Grammars: The Need for a Dual Perspective"
authors: "Roger Clarke; Andrew Burton-Jones; Ron Weber"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0631"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/MTW5UUB5/fulltext/images/df9411d0e5e809e838659d9c71af4c11a2045d6629700e43a7c2e2d30ba9c21c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# On the Ontological Quality and Logical Quality of Conceptual-Modeling Grammars: The Need for a Dual Perspective

Roger Clarke, Andrew Burton-Jones, Ron Weber

To cite this article:

Roger Clarke, Andrew Burton-Jones, Ron Weber (2016) On the Ontological Quality and Logical Quality of Conceptual-Modeling Grammars: The Need for a Dual Perspective. Information Systems Research

Published online in Articles in Advance 19 May 2016

http://dx.doi.org/10.1287/isre.2016.0631

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/MTW5UUB5/fulltext/images/74e1a2220312f288eec2a25d49c8f61d47b52a9164e63f955eb2a47ed1eed8e4.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# On the Ontological Quality and Logical Quality of Conceptual-Modeling Grammars: The Need for a Dual Perspective

Roger Clarke

School of Politics, International Studies and Philosophy, Queen’s University Belfast, Belfast BT7 1PB, United Kingdom, roger.clarke@qub.ac.uk

Andrew Burton-Jones

UQ Business School, University of Queensland, St Lucia, QLD 4072, Australia, abj@business.uq.edu.au

Ron Weber

UQ Business School, University of Queensland, St Lucia, QLD 4072, Australia; and Faculty of Information Technology, Monash University, Melbourne, VIC 3800, Australia, uqrweber@uq.edu.au

core activity in information systems development involves building a conceptual model of the domain that an information system is intended to support. Such models are created using a conceptual-modeling (CM) grammar. Just as high-quality conceptual models facilitate high-quality systems development, high-quality CM grammars facilitate high-quality CM. This paper provides a new perspective on ways to improve the quality of the semantics of CM grammars. For many years, the leading approach to this topic has relied on ontological theory. We show, however, that the ontological approach captures only half the story; it needs to be coupled with a logical approach. We explain how the ontological and logical qualities of CM grammars interrelate. Furthermore, we outline three contributions of a logical approach to evaluating the quality of CM grammars: a means of seeing some familiar CM problems in simpler ways, illumination of new problems, and proving the benefit of modifying existing CM grammars in particular ways. We demonstrate these benefits in the context of the Entity-Relationship grammar. More generally, our paper opens a new area of research with many opportunities for future research and practice.

Keywords: conceptual modeling; semantics; ontology; logic

History: Joey George, Senior Editor; Vijay Khatri, Associate Editor. This paper was received on October 2, 2013, and was with the authors 15 months for 3 revisions. Published online in Articles in Advance.

## 1. Introduction

For many years, the quality of the semantics embodied in conceptual modeling (CM) grammars has often been evaluated by mapping their constructs to the constructs in a benchmark ontology (e.g., Gregersen and Jensen 1999, Opdahl and Henderson-Sellers 2002, Recker et al. 2011, Wand and Weber 1993, zur Muehlen et al. 2007). To the extent a one-to-one and onto mapping exists, their semantics are deemed to be ontologically clear and complete, i.e., the meaning of each construct in the grammar is well defined (clarity), and the grammar has a set of constructs that can be used to represent each type of phenomena that occurs in the real world (completeness).

The ontological approach to evaluating the semantics of CM grammars has often provided important insights about the strengths and weaknesses of different grammars (e.g., Green et al. 2011, Recker et al. 2010). It has also produced some counterintuitive and controversial results, such as the potential problems associated with using certain kinds of grammatical constructs when generating scripts to represent a domain (e.g., Bodart et al. 2001, Gemino and Wand 2005, Burton-Jones et al. 2009). Nonetheless, predictions made using the ontological approach about the strengths and weaknesses of the semantics in a particular CM grammar have sometimes received strong empirical support (e.g., Recker et al. 2011). For these sorts of reasons, the ontological approach continues to motivate ongoing research on the merits of CM grammars and specific constructs in the grammars.

In this paper, however, we argue that the ontological approach to evaluating the semantics of CM grammars provides only a partial means of assessing the likely strengths and weaknesses of the grammars. We propose an alternative, complementary approach to evaluating the semantics of CM grammars, i.e., the logical approach. The logical approach evaluates the statements expressed in a CM script against a benchmark logic to determine whether the script is consistent and precise, i.e., whether the script contains any conflicting statements about its focal domain (consistency), and whether the script can answer all questions it is supposed to answer about its focal domain (precision). From an analysis of the consistency and precision of the scripts generated via a CM grammar, the strengths and weaknesses of the grammar can then be determined and solutions can be devised.

We show that the logical approach to evaluating the semantics of a CM grammar can pinpoint all of the defects leading to inconsistency and imprecision that must be addressed in the grammar. Moreover, it can devise solutions for the defects to ensure that all scripts created using the grammar will be logically consistent and precise. This achievement is unlikely using the traditional ontological approach. In part, this reflects that the logical and ontological approaches focus on different properties of a CM grammar in the analytical approaches they use; they foreground and background different properties of the grammar. Ultimately, any defects in a CM grammar might become apparent under both approaches, but each approach tends to reveal various defects and different solutions for addressing them because of the particular analytical approach it uses.

On the other hand, the logical and ontological approaches differ in their levels of generality. Every ontology embeds a logic: Commitment to an ontological theory entails commitment to a logical theory. Therefore, the results obtained from a logical analysis will be more general than the results obtained from an ontological analysis. If a result can be shown to hold given only the assumption of a certain logical theory, those results will hold for multiple ontologies. For example, Bunge’s (1977) ontology and Searle’s (1995) ontology assume classical first-order logic (FOL), so whatever can be shown to follow from FOL alone will hold in Bunge’s and Searle’s ontologies.

Our paper proceeds as follows. We begin by explaining the relationship between ontology and logic and why both are needed to evaluate the quality of the semantics of a CM grammar. Next, we explain the logical approach to evaluating the semantics of CM grammars and the relationship between the logical approach and ontological approach. We then show how the logical approach can be applied to identify certain types of semantic defects in a widely used conceptual modeling grammar, i.e., the entityrelationship modeling (ERM) grammar. We also show how the logical approach can be used to (a) identify how the ERM grammar can be modified to overcome these semantic defects, and (b) demonstrate that no more of these types of semantic defects exist in the modified ERM grammar. We conclude by discussing some implications of the logical approach for research and practice.

## 2. Background: Ontology, Logic, and the Semantics of Conceptual Modeling Grammars

Our focus is the semantics of CM grammars (the rules determining the meaning of the grammatical constructs) rather than their syntax (the symbols used to represent grammatical constructs and how these symbols can be combined) or their pragmatics (how grammars are used in different contexts). While the syntax and pragmatics of CM grammars are important factors affecting their overall merits (e.g., Ågerfalk 2010, Bera et al. 2014, Moody 2009), we see their semantics as primary. Ultimately, the implementation of an information system requires an unequivocal commitment to a particular set of semantics. If these semantics are not a faithful representation of someone’s or some group’s perception of the focal real-world domain, the efficacy of the information system is likely to be undermined (Dunn and McCarthy 1997, pp. 36–37; Sheth 1997; Wand and Weber 1995, p. 206).

We argue that ontology and logic both provide an important means to evaluate the semantics of CM grammars. In some cases, their contributions are unique; in other cases, their contributions are related. As background to our logical approach for evaluating CM grammars, therefore, in Sections 2.1 and 2.2 we briefly discuss the relationship between ontology and logic as foundations for evaluating the semantics of CM grammars.

## 2.1. Relationship Between Ontology and Logic

The disciplines of ontology and logic have multiple schools of thought. Moreover, a longstanding, healthy debate exists about how they relate (Hofweber 2014). In short, there is no single answer to their nature and relationship. For this reason, we take one wellaccepted account, which is that ontology presupposes logic, much as physics presupposes mathematics. By this we mean that one cannot begin to answer questions of ontology without first settling questions of logic. Just as mathematics provides the very language in which physical theories are expressed, logic provides the language in which ontological theories are expressed.

According to this account, a given ontology provides a theory about what kinds of phenomena exist in a domain. Such a theory requires a language, typically a logic, in which the theory can be specified (Hofweber 2014). Thus, any ontology will have a logic embedded in it. Bunge’s (1977, p. 14) ontology, the most widely used in information systems (IS) research (Fonseca 2007), explicitly takes this view. According to Bunge (1977, p. 102), a single logic should underlie all ontologies. Thus, while two distinct ontologies might disagree about the fundamental constituents of the world, they should agree on questions of logical consequence.

Because logic is in this sense prior to ontology (i.e., questions about logical consequence must be settled before we can address questions of the fundamental constituents of the world), the disciplines of logic and ontology operate at different levels of generality. Thus, logical and ontological analysis can be expected to foreground and background different properties of a script or grammar. Logicians are best equipped to evaluate a script in ways that do not depend on specific ontological commitments, giving results that hold across a variety of ontologies. On the other hand, ontologists can evaluate scripts for a more extensive, deeper reflection of their chosen ontology. In this sense, ontological and logical analyses are complementary: Results depending on logic alone are broader in their application, while committing to a specific ontology as well as its underlying logic facilitates deeper analysis of a script.

2.2. Some Implications for Conceptual Modeling This relationship between logic and ontology, that ontology presupposes logic, suggests that logical analysis is both fundamental to CM research and long overdue. It is fundamental because it can provide results that hold regardless of the ontology used to evaluate CM grammars. For example, IS researchers have often debated whether they should choose Bunge’s or Searle’s ontologies (Allen and March 2006, p. 5; Lemieux and Limonad 2011, p. 34), but both presuppose classical FOL (Bunge 1977; Ludwig 2007; Searle 1995, pp. 104–112). Thus, if we can obtain results for conceptual modeling that depend only on FOL and nothing specific to Bunge’s (1977) or Searle’s (1995) ontologies, these results can be accepted by all parties to an ontological debate.

Because any ontology embeds a logic, a commitment to ontological analysis also entails a commitment to logical analysis. If CM researchers assume ontology helps them assess the semantics of CM grammars, they are implicitly assuming that logic also helps them assess the semantics of CM grammars. Thus, ontological analysis and logical analysis should go hand-in-hand. Indeed, given that ontology presupposes logic, logical analysis should precede ontological analysis. So far, this outcome has not occurred in the IS field. As a result, IS researchers have addressed some matters of semantics through ontological analysis, such as optionality (Bodart et al. 2001, Gemino and Wand 2005). We argue that these topics are more effectively addressed through logical analysis.

To make the implications of the relationship between ontology and logic more concrete, assume that we have been asked to evaluate the semantics in an ERM script. Through the lens of logic, the script is a set of statements about a domain together with their logical entailments. This set of statements can then be evaluated for consistency and precision: Does the script provide exactly one answer to each question we could ask about the domain using the script’s vocabulary? Through the lens of ontology, the script is a set of statements that describes what exists in the domain. These statements can then be evaluated for descriptive accuracy: Does the script’s description of the domain make ontological sense, using exactly one grammatical construct for each ontological construct? Logical and ontological analyses evaluate scripts along orthogonal dimensions. A script may be ontologically clear and complete without being logically consistent or precise, or vice versa. Ultimately, we need both properties in high quality scripts, and we need CM grammars capable of producing such scripts.

## 3. Evaluating the Semantics of Conceptual Modeling Grammars Using Logic

We are not the first to propose that logic can play a valuable role in research on the semantics of CM grammars. Table 1 provides an overview of and some examples of prior work that has been done.

Our approach differs from this prior work in two ways. First, our focus is not the development of languages (grammars) to support automated reasoning. Rather, we aim to discover properties of CM grammars that support the production of CM scripts with high-quality semantics. Second, our focus is not precisely articulating the semantics of specific constructs in a CM grammar. Rather, our focus is the logical analysis of CM grammars in toto to assess and ensure their overall semantic quality. This is an important shift in emphasis compared to the traditional approach taken in the ontological tradition of CM research. To date, researchers have used ontological theories to assess specific constructs in a grammar (e.g., Wand et al. 1999) or even entire grammars (e.g., Wand and Weber 1993), but they have not proposed ways to ensure that a grammar will have the property of always producing scripts with desirable ontological properties (such as ontological completeness or clarity).

We begin by articulating the semantic properties of CM scripts and grammars that are desirable from the perspective of a logical benchmark. Once we have these properties, we then explain how these properties complement the criteria used to undertake ontological evaluations of CM scripts and grammars.

Table 1 Examples of Prior Research Using Logic to Design or Evaluate CM Grammars

<table><tr><td>Focus of logical analysis</td><td>References</td></tr><tr><td>Development of computational ontologies that support reasoning within applications.</td><td>Calvanese et al. (1998), Fillotrani et al. (2012), Franconi (2004), Hitzler et al. (2012)</td></tr><tr><td>Specification of the semantics of set-based constraints.</td><td>Currim and Ram (2012), Ram and Khatri (2005)</td></tr><tr><td>Reconstruction of existing CM grammars to improve logical precision and to facilitate reasoning with and implementation of databases.</td><td>Thalheim (1993)</td></tr><tr><td>Development of a grammar to support implementation of and reasoning in knowledge-intensive information systems.</td><td>Jeusfeld et al. (2009), Mylopoulos et al. (1990), Steel (1986)</td></tr></table>

## 3.1. Desirable Logical Properties of Conceptual Modeling Scripts and Grammars

The basic idea behind our approach is that a CM script can be treated as a logical theory (for similar positions, see Mylopoulos et al. 1990, p. 351; Steel 1986, p. 259). Logical analysis then involves comparing the statements (theorems) expressed in a script against a benchmark logic.

If we conceive of a script as a logical theory, we can use two well-studied properties of logical theories, i.e., consistency and precision.<sup>1</sup> To determine whether a script has these properties, we use the following approach:

• Take as input a set of phenomena that has been modeled via a CM script.

• Convert the CM script into a set of sentences in the benchmark logic.

• Use the set of sentences in the benchmark logic and the benchmark logic to generate the complete set of questions that the CM script should be able to answer.<sup>2</sup>

• Check via the set of sentences in the benchmark logic whether the script provides either a “yes” or “no” answer to each question.

The test for consistency and precision is then relatively straightforward. If a script gives more than one answer to one or more questions (i.e., both a “Yes” and “No” answer to a single question), it is inconsistent. Somewhere the script provides contradictory representations of some phenomena. For example, it shows “managers” as both a subclass of “employees” and a subclass of “contractors” (those who are not employees).

If a consistent script fails to answer one of the questions with a “Yes” or “No” answer, however, it is imprecise. Somehow the script is ambiguous about domain phenomena. For example, it shows a class of “employees” and a class of “contractors,” but it does not indicate whether these two classes can overlap. In short, when a consistent but imprecise script does answer a Yes/No question, it provides only one answer to the question, but it does not provide an answer to all Yes/No questions.

Our two logical criteria are independent of each other (Figure 1). On one hand, an inconsistent CM script (one that provides both a “Yes” and “No” answer to at least one question) is neither precise nor imprecise. Once inconsistency exists, precision is not a relevant criterion to apply to the script. On the other hand, a consistent script may be precise or imprecise. It will be precise only if it answers all questions with either a “Yes” or “No” answer. If it fails to answer all questions, it might be consistent in relation to those questions it does answer, but nonetheless it is imprecise because it does not answer all questions.

Note that a logical approach cannot tell us whether a script is ontologically incomplete. In other words, it cannot tell us whether the script is unable to answer one or more questions that are deemed to be relevant about domain phenomena. For instance, the script fails to answer questions about managers because managers are not represented in the script, even though managers are deemed to be a relevant domain phenomenon. Incompleteness, however, is a difficult notion because identifying domain phenomena that might be relevant to stakeholders is often problematic (Pitts and Browne 2004). Indeed, discussions about the lay meaning of incompleteness often evoke the pragmatic notion of relevance, which logical analysis is not suited to uncovering.

A logical approach also cannot tell us whether a consistent script is inaccurate. In other words, it cannot tell us whether a script gives an incorrect answer to one or more questions about a domain. For example, it answers the question “Are all managers employees?” with “Yes” when the correct answer is “No.” Nonetheless, logical analysis can uncover inaccuracy when it detects that a script is inconsistent. An inconsistent script represents a domain in a logically impossible and therefore inaccurate way. Like incompleteness, however, inaccuracy is a difficult notion because accurately identifying domain phenomena and representing them accurately in a script are often problematic (Dawson and Swatman 1999, Hadar et al. 2014, Wastell 1996).

Figure 1 Relationship Between Consistency and Precision  
![](/api/attachments/MTW5UUB5/fulltext/images/19c5133911d3e7f756565d5da28a3d896f1c2ca81a7f8c3a8ee30d713498454a.jpg)

If the desirable logical properties of a CM script are consistency and precision, the desirable properties of a CM grammar are therefore that it always generates (a) consistent scripts, and (b) precise scripts. In other words, it should be impossible to use the constructs and production rules in the grammar in such a way that inconsistent or imprecise scripts are produced. Through logical analysis of the scripts that a CM grammar may produce, we seek to determine whether the grammar has these two properties.

## 3.2. Relationship Between Ontological and Logical Criteria for Evaluating Conceptual Modeling Grammars and Scripts

Table 2 shows the ontological and logical criteria that we propose for use as a basis for evaluating the semantic quality of CM grammars and scripts. Because the ontological criteria we propose differ slightly from the traditional ontological criteria used to evaluate the semantics of CM grammars, Online Appendix I (available as supplemental material at http://dx.doi .org/10.1287/isre.2016.0631) provides a brief description of the traditional criteria and the ways in which the ontological criteria in Table 2 differ from these traditional criteria.

Note in Table 2 how our logical criteria complement ontological criteria as a basis for evaluating the semantic quality of CM grammars and scripts. Significantly, our logical criteria are independent of the ontological criteria. On one hand, the properties of ontological clarity and completeness are associated with mapping between the basic constructs of a CM grammar and the constructs of a benchmark ontology. On the other hand, the properties of logical consistency and precision are associated with mapping between the entailments (theorems) of a script and the sentences of a benchmark logic. In other words, using the criteria of ontological clarity and completeness, the ontological approach evaluates the nonlogical symbols (grammatical constructs) in a CM grammar, whereas using the criteria of logical consistency and precision the

Table 2 Ontological and Logical Criteria for Assessing Semantic Quality

<table><tr><td rowspan="2"></td><td colspan="2">Application to</td></tr><tr><td>CM script</td><td>CM grammar</td></tr><tr><td rowspan="2">Application of: Ontology</td><td></td><td>Ontologically complete</td></tr><tr><td>Ontologically clear</td><td>Always ontologically clear</td></tr><tr><td rowspan="2">Logic</td><td>Logically consistent</td><td>Always logically consistent</td></tr><tr><td>Logically precise</td><td>Always logically precise</td></tr></table>

Definitions related to ontology:

Ontologically clear : Each grammatical construct in a script represents only one construct in the chosen ontological benchmark (i.e., no construct overload or excess).

Ontologically complete: A CM grammar offers all constructs needed to produce scripts containing any construct in the chosen ontological benchmark (i.e., no construct deficit ).

Always ontologically clear : A CM grammar ensures that in all scripts it produces, each grammatical construct represents only one construct in the chosen ontological benchmark (i.e., no construct overload or excess).

Definitions related to logic:

Logically consistent : A CM script does not provide both a “Yes” and “No” answer to any question the script purports to answer.<sup>a</sup>

Logically precise: A logically consistent CM script does provide either a “Yes” or “No” answer to all questions the script purports to answer.

Always logically consistent : A CM grammar ensures any script it produces does not provide both a “Yes” and “No” answer to any question the script purports to answer.

Always logically precise: A CM grammar ensures any logically consistent script it produces provides either a “Yes” or “No” answer to any question the script purports to answer.

<sup>a</sup>By “all questions the script purports to answer,” we mean all questions that can be formulated using only the script’s vocabulary (i.e., those class, attribute, and relationship labels appearing in the script). By using a given class/attribute/relationship label, a script commits itself to modeling the named phenomenon—thus, we say it purports to answer questions about that phenomenon.

logical approach takes the nonlogical symbols (grammatical constructs) as given and evaluates the ways in which these symbols (grammatical constructs) are combined. In conjunction with the ontological criteria, therefore, our logical criteria provide a more comprehensive basis for evaluating the semantics of CM grammar and scripts.

## 4. Evaluating Whether the ERM Grammar Is a Logically Always-Precise Grammar

In this section, we demonstrate how logic can be used to evaluate the semantics of the ERM grammar. We chose the ERM grammar because it is well known and widely used by researchers and practitioners. Nonetheless, the form of our analysis can be applied to other grammars (e.g., the Unified Modeling Language).

In our illustrative analysis, for three reasons we focus only on evaluating logical precision in the ERM grammar; in other words, we do not address logical consistency. First, for those aspects of the ERM grammar that we study, precision is more challenging to ensure than consistency. Second, based on our analyses, we believe our results for precision are more interesting and novel than those we have obtained for consistency. Third, some aspects of consistency have already been studied in the CM literature (e.g., Mylopoulos et al. 1990); thus, possible approaches to evaluate whether, or prove that, a CM grammar generates consistent scripts are available. In short, by focusing on precision and not consistency in our illustrative analysis, we believe we provide a more powerful and compelling demonstration of the value of the logical approach to evaluating CM grammars.<sup>3</sup>

## 4.1. Choice of Benchmark Logic

The first step in evaluating the logical precision of a CM grammar is to choose a benchmark logic. For three reasons, we chose FO<sup>2</sup>, which is the two-variable fragment of FOL without identity (“=”).

First, a logic based on FOL provides a powerful benchmark. Relative to weaker logics (such as propositional modal logic), FOL formulas allow us to place more constraints on a domain, describing the world in finer detail. In some applications, FOL’s power is an obstacle; for instance, first-order consequence is not decidable (Church 1936, Turing 1936).<sup>4</sup> In our case, however, it increases the significance of our results. Recall that we aim to show that all consistent scripts produced by a CM grammar are precise, which means they give an answer to every question one can ask about the phenomena represented in the script. Because FOL is powerful, it allows us to ask more questions than a weaker logic. Therefore, showing that a grammar is always precise relative to FOL is a greater achievement than obtaining the same outcome with a weaker logic.

Second, first-order theories (that is, collections of FOL formulas with their consequences) have a wellstudied property, what logicians call completeness,<sup>5</sup> which mirrors our notion of precision in CM scripts. A first-order theory is complete iff, for every FOL formula , either  or not- (but not both) is a consequence of the theory. This definition clearly matches our definition of precision. Thus, by taking FO<sup>2</sup> as our benchmark logic, we open a route to demonstrating that a script is precise or that a grammar is always precise. In particular, we use the following strategy: Give a semantics that translates CM scripts as firstorder theories, then show that the result is logically complete.

Third, we do not need the full expressiveness of FOL to show how to enact a logical evaluation of the ERM grammar. For instance, in an ERM script, we do not expect to make a statement that a class of entities contains more than n members $( n \geq 1 ) . ^ { 6 }$ Whereas such a statement can be made in FOL, it cannot be made in FO<sup>2</sup>. We facilitate our work by using a more restricted version of FOL in the form of FO<sup>2</sup>.

## 4.2. Restricting the ERM Grammar

To effectively apply FO<sup>2</sup>, we needed to restrict the ERM grammar in three ways. This is because our CM grammar must match our benchmark logic in expressive power. For example, because FO<sup>2</sup> cannot express the claim that a class has more than n members, we restrict ERM’s ability to express this claim, too. These restrictions mean that our results only constitute the beginning of a full logical analysis of the ERM grammar.

The first restriction we imposed was removing ternary and higher-order relations from the grammar’s constructs. If we included these constructs in our modified grammar, we suspect, but do not prove, that our modified grammar would still be always precise, relative to an appropriately chosen fragment of FOL. In the interest of simplicity, however, we consider only binary associations between classes.

The other two conditions we imposed were (a) prohibiting nondichotomic properties,<sup>7</sup> and (b) prohibiting cardinality notation. At this time, we are unsure whether it is possible to prove that an ERM grammar containing these constructs is always precise. For the moment, it is easier to prove that our modified ERM grammar is always precise if these constructs are proscribed.

## 4.3. Evaluation Process

To evaluate whether the restricted ERM grammar is always precise, we followed two major steps.

First, we composed a formal semantics for ERM scripts. That is, we gave instructions for determining, for any ERM script, what the script entails, with these entailments expressed in the language of the benchmark logic. In our case, the benchmark logic is FO<sup>2</sup>, so a formal semantics specifies a mapping from ERM scripts to FO<sup>2</sup> theories (equivalently, sets of sentences).

Second, once we had a formal semantics, we sought to determine whether any consistent ERM scripts are imprecise. This process is iterative. Most likely, several solution paths exist. Nonetheless, given we have a mapping from ERM scripts to $\mathrm { F O } ^ { 2 }$ theories, we can address the question of whether any consistent ERM scripts are imprecise using the machinery of FOL. Specifically, the question of whether any consistent ERM scripts are imprecise reduces to the question of whether any theory in the range of the mapping is incomplete (in the logician’s sense). In this regard, logical incompleteness is a well-studied property. Thus, many theorems exist that we can use to facilitate this stage of the analysis. For instance, we have many proven theorems of the form, “If a theory T has the property A, then T is (in)complete.” In Online Appendix II we use such a theorem in our proof of ERM-R’s always-preciseness.<sup>8</sup>

To find ways in which a consistent ERM script might be imprecise, we look to our ERM semantics. When translating ERM scripts into $\mathrm { F O } ^ { 2 }$ , we encounter three types of predicate symbols: For each class in a script, we have a unary predicate $C _ { i } ;$ for each attribute, we have a unary predicate $P _ { j } ;$ and for each relation, we have a binary predicate ${ \bf \check { \phi } } _ { R _ { k } }$ . Given the established theorems on which our proof relies (see footnote 8), we can safely restrict our attention to open formulas, i.e., formulas without quantifiers (∀ and ∃). What, then, are the open formulas in the language of T ? They will be Boolean combinations of the following atoms:

• $C _ { i } x$ and $C _ { i } y .$ , for all class predicates $C _ { i } ;$

$P _ { j } x$ and $P _ { j } y ,$ , for all attribute predicates $P _ { j } ;$

$\vec { R _ { k } x x } , R _ { k } \dot { x } y , R _ { k } y x ,$ , and $R _ { k } y y$ , for all association predicates $R _ { k }$

Because $\mathrm { F O } ^ { 2 }$ lacks an identity predicate and does not allow more than two variables per formula, the range of possible formulas is restricted. We need only consider combinations of the above types of atomic formulas, possibly with one existential quantifier prefixed. In doing so, we found the following problem cases:

1. $C _ { i } x \wedge C _ { j } y \wedge \neg R _ { k } x y$

• If the association $R _ { k }$ between $C _ { i }$ and $C _ { j }$ is mandatory, we can ask whether the relation holds between all members of $C _ { i }$ and all members of $C _ { j }$ . This is the question of cardinality (Section 5.2.1).

$$
R _ {k} x y \wedge R _ {k} y x
$$

• If x bears a relation to y, must/can y bear that same relation to x? This is the question of symmetric and asymmetric relations (Section 5.2.2).

3. $R _ { k } x x$

• Can an individual bear a given relation to itself? This is the question of reflexive relations (Section 5.2.3).

$$
R _ {k} x y \wedge R _ {m} x y
$$

• If x bears relation $R _ { k }$ to $y ,$ must/can x also bear the distinct relation $R _ { m }$ to the same individual y? This is the question of individuation of relations (Section 5.2.4).

5. $C _ { 1 } x \wedge C _ { 2 } x$

• Do classes $C _ { 1 }$ and $C _ { 2 }$ overlap, or are they disjoint? Do the subclasses $C _ { 4 }$ and $C _ { 5 }$ exhaust the superclass $C _ { 3 } ?$ This is the question of overlap, disjointness, and exhaustiveness (Section 5.2.5).

$$
6. C _ {i} x \wedge P _ {j} x \wedge R _ {k} x y
$$

• Suppose the attribute $P _ { j }$ and the relation $R _ { k }$ are both optional for the class $C _ { i } ^ { ' } .$ . Can a member of $C _ { i }$ both have $P _ { j }$ and bear $R _ { k }$ to something? This is the problem of optionality (Section 5.2.6).

## 5. Making the ERM Grammar Always Logically Precise

Having pinpointed six defects in the ERM grammar, in this section we propose modifications that will

Table 3 Legend for Non-Standard ERM Notation

Arrows indicate direction of relation (A bears R to B).

Small circle indicates optionality (not all members of A have property P ).

Line with indicates subset (all members of A are members of A).

Cardinality notation (see Section 5.2.1): Each member of A bears R to at least one member of B; equivalent to standard “1    N” notation.

Cardinality notation (see Section 5.2.1): Each member of A bears R to each member of B.

Symmetric relation (see Section 5.2.2): If a member a of A bears R to a member b of B, then b must also bear R to a.

Relation symbol in attribute-type circle indicates reflexive relation (see Section 5.2.3): Members of A bear R to themselves.

mitigate the effects of these defects and ensure that the grammar never generates imprecise scripts. We denote the modified ERM grammar as ERM-R.

We begin by discussing an important assumption that underlies the changes we made to the ERM grammar. We then discuss the six changes we made to the ERM grammar to address the defects. Finally, we summarize our recommendations for disciplined use of the ERM grammar.

## 5.1. The “Completeness” Assumption

We note one assumption we make before proceeding. Specifically, we assume that ERM scripts are intended to present a complete rather than a partial representation of the domain they model. Formally, this assumption entails that we understand the absence of a claim as a claim of absence. For instance, if a script has no class called “students,” we interpret the script as claiming the domain modeled does not include any students.

That we assume scripts are complete should not be a surprise. A script intended as only a partial representation of a domain will, necessarily, leave questions unanswered. This outcome is borne out in our formal proof. In providing a formal semantics for our modified ERM grammar, the success of our proof depends on scripts being interpreted to include a claim that the modeled domain includes no entities other than those represented.<sup>9</sup>

Interpreting scripts as complete should not be confused with making a “closed-world assumption”

(Reiter 1978) or as conflicting with agile methods (Ambler 2002). The classical closed-world assumption involves treating everything not known to be true as false. Thus, under a closed-world assumption, scripts are not subject to revision. On the contrary, we treat scripts as presenting a complete picture of the modeler’s knowledge of a domain at a point in time. In this light, the absence of a class of students in a script means that, according to the modeler’s understanding at that time, the modeled domain has no students. As the modeler’s understanding of the domain unfolds, a class of students might be included in the script.

## 5.2. Modifications to the ERM Grammar

The six subsections below describe the specific modifications we made to the restricted ERM grammar (see Section 4.2) to achieve always-preciseness. Each subsection begins with an example of an imprecise ERM script. We show why the script is imprecise by providing a question that the script is unable to answer. In essence, we seek to provide the intuition behind our formal results (Online Appendix II). Because some ERM notation we use is nonstandard, Table 3 provides a legend.

Significantly, note that all of our modifications to the ERM grammar are semantically motivated. Some introduce (Sections 5.2.1–5.2.3) or eliminate (Section 5.2.6) syntactic elements, but these amendments to ERM’s syntax are designed to improve the grammar’s semantics. On the other hand, some of our modifications (Sections 5.2.4 and 5.2.5) leave the ERM’s syntax unchanged, instead modifying the semantic rules for interpreting ERM scripts. That is, Sections 5.2.4 and 5.2.5 modify how one is to read a script (and hence how a competent modeler would construct a script), rather than adding or removing vocabulary elements.

Figure 2 Problem: Inadequate Cardinality Notation  
![](/api/attachments/MTW5UUB5/fulltext/images/ce0a5fa1fad08656bc198befc60b50bfd2c68c021cdf7d9e971bc6418969cd1e.jpg)

5.2.1. New Cardinality Notation. Example possible unanswered question (Figure 2):

$$
\begin{array}{l} \exists x \exists y \big [ \text { ResearchStudent } (x) \\ \quad \land \text { MethodsCourse } (y) \land \neg \text { EnrolledIn } (x, y) \big ] \\ - \text { Must   research   students   enroll   in } \\ \quad a l l \text { methods   courses? } \end{array}
$$

We begin with the standard way of representing mandatory associations between classes, which fails to distinguish logically distinct ways in which two classes can be related.

Suppose an ERM script indicates that a relation holds between two classes. For example, Figure 2 shows a class Research Student bearing the relation enrolls in to the class Methods Course. Given that the relation is mandatory for both classes (see Section 5.2.6 for discussion of mandatory and optional associations), we can ask the following question in FO<sup>2</sup>: Does every research student enroll in every methods course, or may a research student enroll only in some methods courses? (In symbols, we are asking whether

$$
\begin{array}{c} \forall x \forall y [ \text { ResearchStudent } (x) \land \text { MethodsCourse } (y) \\ \to \text { enrolls } (x, y) ] \end{array}
$$

is true.) An ERM script cannot answer this question. Our modeling grammar must answer this sort of question if it is to produce precise scripts. Therefore, we introduce a new type of cardinality notation. When class A is linked to class B via the relation R, we use the annotation “ ” (all) at both ends of the link to indicate that all members of A bear R to all members of B, and vice versa. Likewise, we use the annotation “ ” (some) to indicate that all members of A bear R to at least one member of B, and vice versa. (The “ ” cardinality notation is effectively equivalent to the standard “1    N ” notation.) For convenience, we sometimes refer to associations with the notation “<sub>∀</sub>” as <sub>∀</sub>-type associations and associations with the notation “<sub>∃</sub>” as <sub>∃</sub>-type associations. Thus, in Figure 3 the enrolls in association between Masters Student and Methods Course is -type, whereas the enrolls in association between PhD Student and Methods Course is -type. (Note that “all” and “some” as used here are technical, logical notions, and they should not be confused with any vague, informal concept.)

Note that restoring standard cardinality notation to our fragment of the ERM grammar, by itself, does not suffice to avoid the kind of ambiguity we resolve here. Using standard cardinality notation to resolve the ambiguity would require specifying in advance the cardinality of the classes A and B, which in general is not possible. Without such a specification, we cannot choose a number n such that bearing R to n members of class B entails bearing R to all members of class B. We would then indicate only <sub>∃</sub>-type cardinalities but not <sub>∀</sub>-type cardinalities.

Figure 3 Solution: New Cardinality Notation  
![](/api/attachments/MTW5UUB5/fulltext/images/3a166171a7a24c01d4ae25d767c64bd164d0c6e6e01e1b046e04f13e70cb89f1.jpg)

Past research in computer science has also provided formal treatments of cardinality (Thalheim 1992, Hartmann 1998, Dullea et al. 2003). Although that work and our work are similar (in relying on formal logic), the two programs of research are distinct; yet both are necessary. Our work focuses on precisely modeling organizational domains; the computer science work focuses on improved database design.

5.2.2. Symmetric and Asymmetric Relations. Example possible unanswered question (Figure 4):

<sub>∃</sub>x<sub>∃</sub>yLabPartnerx y <sub>∧</sub> <sub>¬</sub>LabPartnery x <sub>−</sub> If x is lab partner to y, must y also be lab partner to x?

We must be able to tell when an association between classes is symmetric. If a relation R is symmetric, then whenever a bears R to b, b also bears R to a. For example, the relation lab partner of in Figure 4(a) is symmetric: If Alice is Bob’s lab partner, then Bob must be Alice’s lab partner.

On the other hand, for an asymmetric relation R, whenever a bears R to b, b does not bear R to a. In Figure 4(b), we have the relation moderates exam. This relation means that teaching staff members serve as second marker, or moderator, on each other’s exams before marks are finalized. At the university represented in Figure 4(b), if staff member a moderates the exam in staff member b’s class, then b is prohibited from doing the same for a’s class. The university imposes this constraint to protect the integrity of the moderation. Therefore, moderates exam is an asymmetric relation. The problem in Figure 4, however, is that symmetry and asymmetry are not distinguished.

Figure 4 Problem: Symmetric or Asymmetric Relations?  
![](/api/attachments/MTW5UUB5/fulltext/images/ecefea3b18bff4745f1075512909bd3c05d10bbd2562310d000fb1f2f425a66c.jpg)

Figure 5 Solution: Symmetric and Asymmetric Relations  
![](/api/attachments/MTW5UUB5/fulltext/images/3a8b307379a93e92dc4238673fab061c90ea4edc9d672dede19490431756a16e.jpg)  
Figure 6 Problem: Reflexive Relations

Because we can express the statement that R is (a)symmetric in $\mathrm { F O } ^ { 2 }$ (with the formula $\forall x \forall y [ R ( x , y )$ $\scriptstyle \to R ( y , x ) ]$ for symmetry, or $\forall x \forall y [ R ( x , y )  \neg R ( y , x ) ]$ for asymmetry), we must distinguish symmetric from asymmetric relations in our scripts to achieve alwayspreciseness. We solve this problem by requiring that all relations be symmetric or asymmetric. Moreover, they must be explicitly specified as such. Thus, the association lab partner in Figure 5(a) bears the annotation $^ { \prime \prime } \mathrm { S } , ^ { \prime \prime }$ indicating that it is symmetric; the association moderates exam in Figure 5(b) lacks this annotation, indicating that it is asymmetric.

Although some relations are neither symmetric nor asymmetric, we can resolve any such relation into symmetric and asymmetric component relations. If R is neither symmetric nor asymmetric, then define $R _ { 3 }$ and $R _ { 4 }$ as follows: a bears $R _ { 3 }$ to b iff a bears R to b and b bears R to $a ;$ a bears $R _ { 4 }$ to b iff a bears R to b and b does not bear R to a. Then $R _ { 3 }$ will be symmetric, $R _ { 4 }$ will be asymmetric, and the union of $R _ { 3 }$ and $R _ { 4 }$ is just the original relation R. Thus, by requiring relations to be symmetric or asymmetric, we lose no expressive power.

5.2.3. Reflexive Relations. Example possible unanswered question (Figure 6):

<sub>∃</sub>xModeratesx x

Can someone moderate their own exam marking?

![](/api/attachments/MTW5UUB5/fulltext/images/6939864ddf67dc890aa0270b91f4f932c88039a2fad39a0d7cb54a426e9c7b39.jpg)

In ${ \mathrm { F O } } ^ { 2 } ,$ we can say that an individual bears a (binary) relation R to itself. It distinguishes this case from the case of an individual having a (unary) property P . For example, consider the class Teaching Staff in Figure 6. This class has two recursive associations on this class, i.e., moderates exam and refers plagiarism. These associations represent two different tasks teaching staff perform for each other: First, staff moderate each other’s exam marking, meaning that each staff member’s marking is given to a second marker, or moderator, before being finalized; second, each teaching staff member has a designated staff member to whom all cases of plagiarism are to be reported. Only one of these associations represents a relation that teaching staff may bear to themselves. That is, a staff member may be in charge of handling cases of plagiarism in her own courses, in which case she will bear the relation refers plagiarism to herself. On the other hand, no staff member will moderate her own marking; the point of moderation is to have a second marker. ERM is unable to represent this difference.

Figure 7 Solution: Reflexive Relations  
![](/api/attachments/MTW5UUB5/fulltext/images/c19a028c18407e9f5ac57ca77a65abfd3f25383f528a65b6db75adf91a182959.jpg)

Figure 7 shows how ERM-R solves this problem. In the revised diagram, a subclass Plagiarism Supervisor of Teaching Staff exists with an attribute refers plagiarism. This representation indicates that members of this subclass report cases of plagiarism to themselves. More generally, in ERM-R diagrams, attributes that bear the same label as an association indicate that the relation denoted by the association is reflexive (on the class to which the attribute belongs). In Figure 7, no class bears an attribute labeled moderates exam, which indicates that the corresponding relation is irreflexive.

5.2.4. Individuation of Relations. Example possible unanswered question (Figure 8):

<sub>∃</sub>x<sub>∃</sub>ySupervisesx y <sub>∧</sub> Employsx y <sub>−</sub> Can someone both supervise and employ the same person?

In Figure 8, two associations exist between Academic Staff and Graduate Student: Both supervises and employs are -type. Our question is whether the same research staff member can both supervise and employ the same research student. Figure 8 does not answer this question. It could be that all research staff must supervise at least one research student and employ at least one research student but that these students must be different (perhaps to avoid a conflict of interest).<sup>10</sup> Also, this ambiguity cannot be resolved through the use of subclasses.

Figure 8 Problem: Unindividuated Relations  
![](/api/attachments/MTW5UUB5/fulltext/images/aa312a01d4b6cda88fd92b6e27190dade3854a331bfa4325c7a8ef75a62cd327.jpg)

Our solution is to require that associations be individuated finely: A -type association labeled $' \prime R _ { 1 } ' $ between A and B indicates that members of A bear $R _ { 1 }$ and no other relation to members of B. If we want to indicate that members of $A$ bear $R _ { 1 }$ and also $R _ { 2 }$ to members of $B ,$ then we use an association labeled $^ { \prime \prime } R _ { 1 } \& R _ { 2 } . ^ { \prime \prime }$ If we want to indicate that members of A bear one or more of the relations $R _ { 1 }$ and $R _ { 2 }$ to members of $B ,$ we split A and B into the corresponding subclasses (those associated by $R _ { 1 }$ alone, by $R _ { 2 }$ alone, and by both $R _ { 1 }$ and $R _ { 2 } )$ , with their associations explicitly depicted. Figure 9 illustrates this approach wherein we introduce the new association supervises and employs.

We also introduce three<sup>11</sup> subclasses of Academic Staff to ensure that we express the following information. It is mandatory for each member of the Academic Staff to supervise at least one Graduate Student and also to employ at least one Graduate Student. Academic Staff are subject to no further restrictions, however, on whom they may supervise or employ. In particular, it is not mandatory that they both supervise and employ any single Graduate Student. Thus, we cannot draw a mandatory association supervises and employs between Academic Staff and Graduate Student. Therefore, we introduce the subclass Supervisor-Employer for Academic Staff who supervise and employ the same Graduate Student and the subclasses Supervisor and Employer for, respectively, Academic Staff who supervise (employ) a Graduate Student whom they do not employ (supervise). We also introduce parallel subclasses of Graduate Student for the same reasons.

Figure 9 Solution: Individuation of Relations  
![](/api/attachments/MTW5UUB5/fulltext/images/5b7cead2bf411cd731a659f0ce4b04c2abf29550073cd72f7cfa05559890bfa0.jpg)

5.2.5. Overlapping, Disjoint, and Exhaustive Subclasses. Example possible unanswered question (Figure 10):

xOnlineCoursex  BlendedCoursex

Can an online course also be a blended course?

Consider the ER script in Figure 10, which models the modes of course offerings in a university. The script tells us that the university offers courses in three modes, i.e., on-campus, online, and blended. It does not tell us whether the three modes are disjoint (all courses are offered in one mode only) or overlapping (some courses are offered in more than one mode). Furthermore, it does not tell us whether these modes are exhaustive (are there other ways of offering a course, such as a massive open online course (MOOC)?). Such facts are expressible in FO<sup>2</sup>, so we must amend our fragment of ERM to ensure that it is capable of generating consistent and precise scripts when questions are asked about relationships among subclasses and among subclasses and classes. Specifically, any script generated using the ERM-R must show for all subclasses represented in the script (a) which subclasses are disjoint and which subclasses are overlapping, and (b) whether subclasses are exhaustive or nonexhaustive of their superclass.

We need a solution to resolve any ambiguity about whether subclasses are disjoint or overlapping and exhaustive or nonexhaustive. Our solution is to ensure that the bottom-level classes of a model (classes depicted as having no subclasses) are disjoint and exhaustive. That is, every individual of the domain belongs to exactly one bottom-level class. For other classes, we can tell whether they are disjoint or overlapping simply by checking whether they have any subclasses in common.

Figure 10 Problem: Overlap, Disjointness, and Exhaustiveness of Subclasses  
![](/api/attachments/MTW5UUB5/fulltext/images/2d29cb7d5769d07ea3f5343693632a0360a23407dd235a55baa7ecf9dafc919d.jpg)

Different notations can be used to achieve this objective. We rely on a simple subclass notation in this paper, but other notations that explicitly denote overlapping, disjoint, and exhaustive relationships among subclasses can also be used (e.g., Elmasri and Navathe 2014, pp. 247–249). Regardless of notation, the key objective (which we have not seen explicitly discussed in the ontological tradition of CM research) is to ensure that all questions of class membership can be addressed, and that this outcome can be achieved by ensuring that all bottom-level classes are disjoint and exhaustive.

For example, consider the ERM-R script in Figure 11. Here we have four bottom-level classes: Research-Only Staff, Research and Teaching Staff, Teaching-Only Staff, and Adjunct Staff. Because these are bottom-level classes, they are disjoint. Furthermore, because they are the only bottom-level classes, they are exhaustive. Likewise, we can see that the two classes Research Staff and Teaching Staff are overlapping because they have the subclass Research and Teaching Staff in common. Also, they are not exhaustive of Academic Staff because that superclass has another subclass, i.e., Adjunct Staff.

We do not suggest that the value of clarifying disjointness/overlap and exhaustiveness (or lack thereof) is unknown in the literature or in practitioner communities. Recall that our central claim is not that each issue we highlight in these six subsections is a source of imprecision. Rather, our headline result is that no other issue results in imprecision. The lessons of this subsection are simply that an always-precise grammar must ensure that questions of disjointness and exhaustivity are answered and that the approach suggested in this section will achieve that objective.

Figure 11 Solution: Overlap, Disjointness, and Exhaustiveness of Subclasses  
![](/api/attachments/MTW5UUB5/fulltext/images/44c1196e399d70d4b0de8f6d9b75f98bd8b906bfb022d8fc8ade5283fb25763d.jpg)

5.2.6. Optional Attributes and Associations. Example possible unanswered question (Figure 12):

<sub>∃</sub>x<sub>¬</sub>HasPublicationx <sub>∧</sub> <sub>∃</sub>y Supervisesx y <sub>−</sub> Can research staff without publications supervise Ph.D. students?

Several researchers have cautioned against using optional attributes and associations in conceptual models. Weber and Zhang (1996, p. 158) and Wand et al. (1999, p. 512) were perhaps the first to suggest that optional attributes and associations obfuscate domain semantics. Wand et al. (1999, p. 518) suggest that difficulties with optionality might arise because information about the “laws” that cover the properties of things is lost when optional attributes and associations are used. Burton-Jones et al. (2012) take this proposition as a starting point for ontological analysis of the difficulties with optionality, using Bunge’s (1977, pp. 77–80) definition of laws. Their ontological analysis finds that in some cases optionality leads to loss of information that cannot be categorized as information about laws. Specifically, on Bunge’s definition of laws, when two classes are mutually exclusive, no lawful relation exists between the two. Nonetheless, the information that two classes are exclusive can be obscured through the use of optionality. Thus, the problem of information loss due to use of optional attributes is more general than the ontological category of laws. In short, a clear understanding of and solution to this problem still eludes ontological analysis.

Figure 12 Problem: Optionality  
![](/api/attachments/MTW5UUB5/fulltext/images/3e115a349b5196ace082871b6d0e99e9a5586cd2f5bf2bb370fec958d8e9b092.jpg)

Logical analysis lets us more precisely characterize the problem with optionality, through the notion of precision as described in Section 3. When a grammar allows optional attributes or associations, it cannot be always precise. The reason is that some scripts with optionality will be ambiguous between multiple, incompatible interpretations. Information about which of these interpretations is lost in such a script, to use Burton-Jones et al. (2012) terminology. In our terminology, such a script is imprecise. Note that the problem identified here is at the level of grammars, not scripts. As Burton-Jones et al. (2012) found, scripts with only one instance of an optional attribute or association do not suffer from loss of information. That is, some scripts containing optional attributes or associations are precise. Nonetheless, a grammar that includes optional attributes or associations will allow imprecise scripts to be generated.

To illustrate why optionality prevents always-preciseness, consider Figure 12. Here, publication is an optional property of the class Research Staff. Similarly, the relation supervises between the classes PhD Student and Research Staff is optional for the latter: some Research Staff do not supervise any PhD Students. These two instances of optionality, taken together, raise the question: Are Research Staff lacking a publication allowed to supervise a PhD Student? This question is unanswered in Figure 12’s script.

Multiple possible solutions exist to the problems that arise when optional attributes and associations are used. We could restrict the ways optional attributes/ associations may be used. For example, to avoid the ambiguities just mentioned, we could prohibit optional attributes for classes with subclasses. This solution would be ungainly, however; many such restrictions would have to be introduced to eliminate all possible ambiguities. Thus, we recommend instead a general proscription against optionality. Our modified grammar ERM-R does not allow optional attributes or associations.

Without optional attributes or associations, we must use subclasses to indicate partiality, i.e., that some but not all members of a (super)class have some property or bear some relation. Thus, in Figure 13, for example, we represent the same situation represented in Figure 12. In the revised script, using subclasses instead of optionality, our previously unanswered question is now answered. We can see that the Research Staff with a publication and those who supervise a PhD Student are the same. Specifically, only the Research Active Staff have publications, and only they supervise the PhD Students.

Figure 13 Solution: Optionality Eliminated via Subclasses  
![](/api/attachments/MTW5UUB5/fulltext/images/6ea953419e618ee51ce0f78e28469f394c0aa3422a6e51373aa7c9402a27ca45.jpg)

In summary, our contribution to the discourse on optional properties is twofold. First, our logical analysis shows that disputes about whether the appropriate ontology has been used or a particular ontology has been correctly used to analyze the nature of optional properties (e.g., Allen and March 2006, pp. 3–4) can be set aside. Our logical analysis shows that optional properties are problematic irrespective of the ontology used or the way an ontology is used to assign them meaning. Second, our logical analysis shows that the question of whether optional properties are problematic from the perspective of generating precise semantics is not “an empirical question” nor one best resolved by “cognitive theories” (Allen and March 2006, p. 4). It is first and foremost a logical problem associated with generating imprecise CM scripts. For pragmatic reasons, conceptual modelers might still choose to use optional properties, but from the perspective of having precise semantics they should understand the potentially negative consequences of their choice.

## 5.3. Summary and Discussion

These are the modifications to our fragment of the ERM grammar needed to produce the ERM-R grammar, for which our result holds (an always-precise grammar). Nonetheless, the focus of our logical analysis is not the individual defects per se. The lesson to be drawn is that the problems we identify with our targeted fragment of the ERM grammar are the only problems with that fragment. Moreover, the theorem proved in Online Appendix II tells us that addressing the problems identified in Sections 5.2.1–5.2.6 results in a grammar with no further sources of imprecision. As we presented these problems, we offered solutions. Our result shows that these solutions are sufficient to produce an always-precise grammar, but not that they are necessary. Other solutions to the problems we identify may be preferable for some particular application, and other possible solutions exist.

Although other solutions exist to the six problems we identified, it is important to highlight the value of a logical approach over a purely ontological approach. In our view, for two reasons the traditional ontological approach could not have satisfactorily identified and resolved these problems. First, the common characteristic of all six problems is that inconsistencies and imprecision can arise in a script due to the way that grammatical constructs combine to make statements about a domain. The possible inconsistency and imprecision lie in the statements, not the individual constructs. Moreover, the problems with the statements are logical, i.e., problems of consistency and precision. Traditionally, ontological analysis has examined the clarity and completeness of individual constructs in a grammar, not statements. In cases where researchers have examined statements from an ontological perspective (as in the work of Evermann and Wand 2005a, b), the focus has naturally been on the ontological properties of the statements (such as ontological completeness and clarity) rather than logical properties. Each theory (logic and ontology) provides a lens that foregrounds some issues at the expense of others. For that reason, it is not surprising that the existing literature (which has largely taken an ontological perspective) has not (to our knowledge) identified the value of addressing all six problems identified in this paper or shown the more fundamental nature of some of the problems.

We also believe the ontological approach could not have satisfactorily addressed these issues because logic is more general than ontology. Recall that ontology presupposes logic. As a result, if researchers use an ontology that relies on FOL, they could use that ontology to identify all six defects examined in this paper. However, doing so would amount to performing a logical analysis. The added value of the ontology lies in the specific constructs it offers beyond those offered by the logic that it presupposes. We argue that identifying and resolving these issues from a logical perspective alone is more satisfactory than doing so from the perspective of a given ontological theory. Adopting an ontological benchmark commits the analyst to the additional claims made by that ontology; logical analysis frees the researcher from this constraint. For instance, researchers can use the results of this paper regardless of whether they prefer Bunge’s (1977) or Searle’s (1995) ontology. Indeed, they can use the results even if they prefer to use no ontological theory. This is not to say that ontological theories do not offer their own benefits. Logical analysis cannot offer insights into ontological completeness and clarity. Each theory offers distinct benefits, i.e., a dual perspective is needed.

## 6. Implications for Research

In light of the outcomes of our work, we believe that future research on the logical approach to evaluating the quality of the semantics of CM grammars and scripts could proceed in a number of directions. In Sections 6.1–6.3, we outline some possible topics that might be pursued in the context of the semantics, pragmatics, and syntax of CM grammars.<sup>12</sup>

## 6.1. Semantics

We have undertaken our logical analysis using a restricted subset of the ERM grammar, i.e., one that omits ternary and higher-order relations, nondichotomic properties, and cardinality notation. Conducting a logical analysis of those aspects of the ERM grammar that we have omitted from our analysis would be valuable as a basis for determining whether an expanded ERM-R grammar is capable of ensuring precise scripts.

In the interest of brevity and our belief that our results for precision are more interesting and innovative, we have not developed the logical analysis of the ERM grammar for consistency. As restrictions on the ERM-R grammar are relaxed, however, evaluating whether an expanded ERM-R grammar is capable of ensuring consistent scripts is likely to prove more challenging. Potentially more interesting and innovative results will emerge.

Just as researchers in the ontological tradition have investigated the applicability of multiple ontological benchmarks, further research could be conducted using different logical benchmarks to evaluate the semantic quality of CM grammars. Whereas we used FO<sup>2</sup>, other logics could be investigated, such as unrestricted FOL, description logic and other modal logics, and even nonstandard logics (e.g., paraconsistent logics). Use of these logics may produce different insights about the ability of CM grammars to generate consistent and precise scripts.

The relationship between the ontological and logical dimensions of the quality of semantics bears investigating. We took one fairly well-accepted view on the relationship between ontology and logic, but other views on this matter exist (Hofweber 2014). Researchers could take a different perspective, or even investigate whether a unifying theory of both types of semantic quality could be developed. Interesting theoretical work has also been done on the kinds of questions that can be asked about a domain that could help IS researchers identify new ways of thinking about and questioning real-world domains (Anderson and Belnap 1975, Belnap 1982).

The semantics of other CM grammars could be evaluated to determine their logical quality, e.g., the different types of grammars available in the Unified

Modeling Language (UML) and the various business process modeling grammars that now exist (such as the Business Process Modeling Notation (BPMN)). The extent to which and the ease with which these grammars can be modified to consistently produce precise scripts can be assessed. The extent to which our results might impact the design of new CM grammars could also be investigated (e.g., through discussions with and working with the designers of CM grammars).

## 6.2. Pragmatics

Just as researchers in the ontological tradition have made progress by empirically testing ontological predictions (Burton-Jones et al. 2009), work could be done to empirically test whether different stakeholders benefit from having more consistent and precise CM grammars and scripts. For instance, the extent to which such grammars and scripts result in better system designs and enable end-users to better query a database could be investigated.

Researchers could also examine whether the usefulness of consistent and precise CM grammars and scripts varies across contexts. In this regard, some researchers following the ontological approach (e.g., Bodart et al. 2001) have found that ontologically clear scripts are more useful when stakeholders require a more detailed understanding of a domain rather than a rough understanding. Others (e.g., Burton-Jones et al. 2012) have found that the positive effects of clearer (and more precise) scripts on stakeholder understanding weaken as the scripts become more complex.

Similar contingencies are likely to apply to precise CM scripts and always-precise CM grammars. For instance, precise scripts and always-precise grammars will probably be most useful in contexts where stakeholders are motivated to avoid misunderstandings because of their potential for serious negative consequences, e.g., in high-reliability organizations (Roberts 1990). In contexts in which misunderstandings are less likely to occur or where they have milder effects, stakeholders may not see the benefits of precise scripts and always-precise grammars; less-precise scripts and grammars may suffice or even be preferable because of their ease of use.

Just as researchers in the ontological tradition have designed CM methods (e.g., Evermann and Wand 2005b) and tools (e.g., Wand et al. 2008) based on ontological insights, researchers could create new methods and tools (or amend existing methods and tools) based on the results of logical analysis (such as those presented in this paper) to assist stakeholders to do higher-quality CM work. Indeed, there is a long tradition of creating tools to help modelers create models with more accurate and complete semantics (Khatri et al. 2006, Sugumaran and Storey 2006).

Creating better methods and tools seems a particularly promising avenue for research using logical analysis given the computable properties of some logics. Possible links between the logical approach outlined in this paper and the logical approach carried out in computer science research could then be pursued (e.g., Fillotrani et al. 2012).

## 6.3. Syntax

Researchers could express the modified ERM semantics articulated in this paper using different syntactic forms. They could then empirically test whether some forms (e.g., those following the physics of notations, Moody 2009) are easier to understand.

In Section 5.2.5, we pointed out that various forms of syntax have been described in prior literature to show whether subclasses in conceptual models are overlapping or disjoint and exhaustive or nonexhaustive. We used a more parsimonious syntax that motivates a modeling approach requiring bottom-level subclasses in a level structure of classes to be disjoint and exhaustive. Empirical work could be conducted to see whether the syntax and the modeling approach it motivates leads to better representations of domain phenomena and better system designs.

## 7. Implications for Practice

The practical implications of our analysis are quite clear. We offer and validate (by proof) a logically “always-precise” fragment of ERM, i.e., ERM-R. Although empirical work is required to test its practical utility, we have shown that it is semantically more precise than ERM. Accordingly, we advocate the use of ERM-R over ERM for practitioners who work in areas where precise semantics are crucial. Moreover, we showed that modelers must be mindful of the six sources of imprecision we identified with the ERM grammar when they use it to prepare CM scripts.

Some practitioners may be aware of the debates on ontologies in the IS literature and have firm preferences about which should be adopted (e.g., Bunge’s ontology or Searle’s ontology). Other practitioners may be unaware of, or see little value in, such debates. Nonetheless, because FO<sup>2</sup> underwrites many ontologies (including Bunge’s and Searle’s ontologies) and depends on none of them, practitioners can adopt ERM-R and our recommendations for using ERM-R regardless of their views about ontological issues.

While the focus of our logical analysis has been the ER grammar, the problems we have identified also apply to other CM grammars. For instance, the UML grammar does not distinguish between symmetric and asymmetric associations. The object role modeling (ORM) grammar makes this distinction (Halpin 1996), but it does not distinguish between “all” (∀) associations and “some” (∃) associations. Where such associations are important phenomena in the domain to be modeled, UML and ORM will not generate precise scripts. Practitioners who use CM grammars other than the ER grammar can use our results, therefore, to evaluate whether the grammar they use is likely to generate imprecise scripts. They may also use the modifications we have made to the ER grammar as a basis for improving the precision of scripts generated via the CM grammar they use.

Finally, while we focused here on implications for CM, an interesting practical question is whether the paper has broader implications for the design and use of IS. We did not address this issue in the paper for reasons of scope, but we have conducted extensive interviews with a database designer with over 20 years of experience on this topic. Three insights came from these discussions.

First, the database designer found that creating a relational database based on our solutions to all six issues described in Section 5 was easy. Moreover, he could attest to the practical relevance of all six issues we identified in light of his experience (e.g., in designing databases for the Department of Education in his state).

Second, rather than developing the database to exactly reflect a particular script, he would work with an application designer to decide how best to reflect the real-world semantics in the information system (while also considering other design decisions such as speed). In other words, the scripts would inform but not determine his database designs.

Third, as many systems analysts have noted (e.g., Yourdon 1989), the designer confirmed that the conceptual issues we addressed in ERM-R cannot be solved through application or database design. No matter how good the application and database, users querying the database will be unable to answer certain questions (yes/no) if they do not have precise knowledge about the domain. If users have access to precise CM scripts, however, they can then query the database to discern whether the data conforms with the real-world phenomena reflected in the script. In future work, we plan to carry out field work with users to discern their ability to use precise scripts as a means of detecting defects in a database.

## 8. Conclusions

Semantics lies at the heart of conceptual modeling. It provides the connection between our representations (scripts) and the reality they are supposed to represent. It underpins the meaning that stakeholders ascribe to representations.

Current approaches to evaluating the semantics of CM grammars and scripts rely primarily on ontology with little, if any, engagement with logic. Ontology gives us only half the picture in evaluating the quality of the semantics in a grammar or script. It tells us what is in the reality we aim to represent with a CM script, but it cannot tell us how our scripts and grammars can represent that reality. A grammar with wholly adequate semantics must allow two outcomes to be achieved: (a) representation of all and only the relevant phenomena in the target domain (ontology), and (b) representation of the phenomena consistently and precisely (logic).

In this paper, we have outlined the differences between an ontological approach and a logical approach to evaluating the quality of the semantics of CM grammars and scripts. Moreover, we have identified an issue in the design of CM grammars, i.e., precision, that cannot be adequately treated using a purely ontological approach. We have also characterized precision using logical analysis.

Finally, we have given a rigorous application of our logical analysis of precision to provide concrete recommendations for the redesign of and disciplined use of the ERM grammar to avoid imprecise (ambiguous) scripts. In particular, we have identified the need for a program of logical investigation into the quality of the semantics of CM grammars and scripts. We have initiated that research program both in theory and in application.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2016.0631.

## Acknowledgments

The authors thank the senior editor, associate editor, and three reviewers for their helpful comments on earlier versions of this paper. The authors also thank Vern Bawden, Denis Duncan, Marta Indulska, Wolfgang Maass, Rachel Pottinger, Veda Storey, Wei Sun, Yair Wand, as well as participants in presentations at SIGSAND 2012 and ICIS 2013. The authors acknowledge financial support from the Sauder School of Business, University of British Columbia, UQ Business School, and the Australian Research Council (ARC) [DP110104386].

## References

Ågerfalk P (2010) Getting pragmatic. Eur. J. Inform. Systems 19: 251–256.

Allen GN, March ST (2006) A critical assessment of the Bunge-Wand-Weber ontology for conceptual modeling. Sinha A, Venkataraman R, eds. Proc. 16th Annual Workshop Inform. Technologies Systems, Milwaukee, 25–30.

Ambler SW (2002) Agile Modeling: Effective Practices for eXtreme Programming and the Unified Process (John Wiley, New York).

Anderson AR, Belnap ND (1975) Entailment: The Logic of Relevance and Necessity, Vol. 1 (Princeton University Press, Princeton, NJ). Belnap ND (1982) Display logic. J. Philos. Logic 11:375–417.

Bera P, Burton-Jones A, Wand Y (2014) Research note—How semantics and pragmatics interact in understanding conceptual models. Inform. Systems Res. 25:401–419.

Bodart F, Patel A, Sim A, Weber R (2001) Should optional properties be used in conceptual modeling? A theory and three empirical tests. Inform. Systems Res. 12(4):383–405.

Bunge M (1977) Ontology I: The Furniture of the World, Treatise on Basic Philosophy, Vol. 3 (D. Reidel, New York).

Burton-Jones A, Wand Y, Weber R (2009) Guidelines for empirical evaluations of conceptual modeling grammars. J. Assoc. Inform. Systems 10:495–532.

Burton-Jones A, Clarke R, Lazarenko K, Weber R (2012) Is use of optional attributes and associations in conceptual modeling always problematic? Theory and empirical tests. George JF, ed. 34th Internat. Conf. Inform. Systems (AIS, Atlanta), 1–16.

Calvanese D, Lenzerini M, Nardi D (1998) Description logics for conceptual data modeling. Chomicki J, Saake G, eds. Logics for Databases and Information Systems (Kluwer Academic Publishers, Dordrecht, Netherlands), 229–264.

Church A (1936) An unsolvable problem of elementary number theory. Amer. J. Math. 58:345–363.

Currim F, Ram S (2006) Understanding the concept of “completeness” in frameworks for modeling cardinality constraints. Sinha A, Venkataraman R, eds. Proc. 16th Annual Workshop Inform. Technologies Systems, Milwaukee, 31–36.

Currim F, Ram S (2012) Modeling spatial and temporal set-based constraints during conceptual database design. Inform. Systems Res. 23(1):109–128.

Dawson L, Swatman P (1999) The use of object-oriented models in requirements engineering: A field study. De P, DeGross JI, eds. Internat. Conf. Inform. Systems (AIS, Atlanta), 260–273.

Dullea J, Song IY, Lamprou I (2003) An analysis of structural validity in entity-relationship modeling. Data Knowledge Engrg. 47:167–205.

Dunn CL, McCarthy WE (1997) The REA accounting model: Intellectual heritage and prospects for progress. J. Inform. Systems 11:31–51.

Elmasri R, Navathe SB (2014) Fundamentals of Database Systems, 6th ed. (Addison-Wesley, Boston).

Evermann J, Wand Y (2005a) Ontology based object-oriented domain modelling: Fundamental constructs. Requirements Engrg. 10:146–160.

Evermann J, Wand Y (2005b) Toward formalizing domain modeling semantics in language syntax. IEEE Trans. Software Engrg. 31:21–37.

Fillotrani P, Franconi E, Tessaris S (2012) The ICOM 3.0 intelligent conceptual modelling tool and methodology. Semantic Web J. 3:293–306.

Fonseca F (2007) The double role of ontologies in information science research. J. Amer. Soc. Inform. Sci. Tech. 58:786–793.

Franconi E (2004) Using ontologies. IEEE Intelligent Systems 19: 76–79.

Gemino A, Wand Y (2005) Complexity and clarity in conceptual modeling: Comparison of mandatory and optional properties. Data Knowledge Engrg. 55:301–326.

Grädel E, Kolaitis PG, Vardi MY (1997) On the decision problem for two-variable first-order logic. Bull. Symbolic Logic 3:53–69.

Green P, Rosemann M, Indulska M, Recker J (2011) Complementary use of modeling grammars. Scandinavian J. Inform. Systems 23:1–27.

Greenspan SJ, Borgida A, Mylopoulos J (1986) A requirements modeling language and its logic. Inform. Systems 11:9–23.

Gregersen H, Jensen CS (1999) On the ontological expressiveness of temporal extensions to the entity-relationship model. Chen PP, Embley DW, Kouloumdjian J, Liddle SW, Roddick JF, eds. Advances in Conceptual Modeling, Lecture Notes Comput. Sci., Vol. 1727 (Springer-Verlag, Berlin Heidelberg), 110–121.

Hadar I, Soffer P, Kenzi K (2014) The role of domain knowledge in requirements elicitation via interviews: An exploratory study. Requirements Engrg. 19:143–159.

Halpin TA (1996) Business rules and object role modeling. Database Programming Design 9:66–72.

Hartmann S (1998) On the consistency of int-cardinality constraints. Ling TW, Ram S, Lee ML, eds. Proc. 17th Internat. Conf. Conceptual Modeling 4ER ’985, Lecture Notes Comput. Sci., Vol. 1507 (Springer, Singapore), 211–225.

Hitzler P, Krotzsch M, Parsia B, Patel-Schneider PF, Rudolph S, eds. (2012) OWL 2 Web Ontology Language Primer, 2nd ed., http:// www.w3.org/TR/owl2-primer/.

Hofweber T (2014) Logic and ontology. Zalta EN, ed. The Stanford Encyclopedia of Philosophy, Fall 2014 ed. http://plato.stanford .edu/archives/fall2014/entries/logic-ontology/.

Jeusfeld MA, Jarke M, Mylopoulos J, eds. (2009) Metamodeling for Method Engineering (MIT Press, Cambridge, MA).

Khatri V, Ram S, Snodgrass RT (2006) On augmenting database design-support environments to capture the geo-spatio-temporal data semantics. Inform. Systems 31:98–133.

Lemieux V, Limonad L (2011) What “good” looks like: Understanding records ontologically in the context of the global financial crisis. J. Inform. Sci. 37:29–39.

Ludwig K (2007) Foundations of social reality in collective intentional behavior: Essays on John Searle’s social ontology. Tsohatzidis SL, ed. Intentional Acts and Institutional Facts (Springer, Dordrecht, Netherlands), 49–71.

Moody DL (2009) The “physics” of notations: Towards a scientific basis for constructing visual notations in software engineering. IEEE Trans. Software Engrg. 35:756–778.

Mortimer M (1975) On languages with two variables. Zeitschrift für Mathematische Logik und Grundlagen der Mathematik 21:135–140.

Mylopoulos J, Borgida A, Jarke M, Koubarakis M (1990) Telos: Representing knowledge about information systems. ACM Trans. Inform. Systems 8:325–362.

Opdahl AL, Henderson-Sellers B (2002) Ontological evaluation of the UML using the Bunge-Wand-Weber model. Software Systems Modeling 1:43–67.

Pitts MG, Browne GJ (2004) Stopping behavior of systems analysts during information requirements elicitation. J. Management Inform. Systems 21:203–226.

Ram S, Khatri V (2005) A comprehensive framework for modeling set-based business rules during conceptual database design. Inform. Systems 30:89–118.

Recker J, Indulska M, Rosemann M, Green P (2010) The ontological deficiencies of process-modeling in practice. Eur. J. Inform. Systems 19(5):501–525.

Recker J, Rosemann M, Green P, Indulska M (2011) Do ontological deficiencies in modeling grammars matter? MIS Quart. 35: 57–79.

Reiter R (1978) On closed world data bases. Gallaire H, Minker J, eds. Logic and Data Bases (Plenum Press, New York), 119–140.

Roberts KH (1990) Managing high reliability organizations. California Management Rev. 32:101–113.

Searle JR (1995) The Construction of Social Reality (Free Press, New York).

Sheth A (1997) Panel: Data semantics: What, where and how? Meersman R, Mark L, eds. Database Applications Semantics (Chapman & Hall, London), 601–610.

Shoenfield JR (1967) Mathematical Logic (Addison-Wesley, Reading, MA). [Reprinted 2001 by Association for Symbolic Logic/A.K. Peters, Natick, MA.]

Steel TB (1986) A minimal conceptual schema language for life, the universe, and everything. Steel TB, Meersman R, eds. Database Semantics (North-Holland, Amsterdam), 255–284.

Sugumaran V, Storey VC (2006) The role of domain ontologies in database design: An ontology management and conceptual modeling environment. ACM Trans. Database Systems 31: 1064–1094.

Thalheim B (1992) Fundamentals of cardinality constraints. Pernul G, Tjoa AM, eds. Proc. 11th Internat. Conf. Entity-Relationship Approach 4ER ’925, Lecture Notes Comput. Sci., Vol. 645 (Springer-Verlag, Berlin Heidelberg), 7–23.

Thalheim B (1993) Foundations of entity-relationship modeling. Ann. Math. Artificial Intelligence 7:197–256.

Turing AM (1936) On computable numbers, with an application to the Entscheidungsproblem. Proc. London Math. Soc. 4Ser. 25 42:230–265.

Wand Y, Weber R (1993) On the ontological expressiveness of information systems analysis and design grammars. J. Inform. Systems 3:217–237.

Wand Y, Weber R (1995) On the deep structure of information systems. Inform. Systems J. 5:203–223.

Wand Y, Storey VC, Weber R (1999) An ontological analysis of the relationship construct in conceptual modeling. ACM Trans. Database Systems 24:494–528.

Wand Y, Woo C, Wand O (2008) Role and request based conceptual modeling—A methodology and a case tool. Li Q, Scappapietra S, Yu E, Olivé A, eds. Proc. CAiSE’08 Forum (Springer, Berlin), 77–80.

Wastell DG (1996) The fetish of technique: Methodology as a social defence. Inform. Systems J. 6:25–40.

Weber R, Zhang Y (1996) An analytical evaluation of NIAM’s grammar for conceptual schema diagrams. Inform. Systems J. 6(2):147–170.

Yourdon E (1989) Modern Structured Analysis (Prentice Hall, Englewood Cliffs, NJ).

zur Muehlen M, Recker J, Indulska M (2007) Sometimes less is more: Are process modeling languages overly complex? Taveter K, Gasevic D, eds. 11th Internat. IEEE EDOC Conf. Workshops (IEEE, Annapolis, MD), 197–204.
