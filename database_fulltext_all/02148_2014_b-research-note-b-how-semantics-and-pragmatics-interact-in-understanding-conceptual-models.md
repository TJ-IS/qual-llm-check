---
otero_id: 2148
otero_key: "A98Y4HQM"
title: "<b>Research Note</b>—How Semantics and Pragmatics Interact in Understanding Conceptual Models"
authors: "Palash Bera; Andrew Burton-Jones; Yair Wand"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0515"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/A98Y4HQM/fulltext/images/6b9a66911eda971ef72b70df303981c06fa4dfeb0ea8a387d5e44b97955d1b18.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—How Semantics and Pragmatics Interact in Understanding Conceptual Models

Palash Bera, Andrew Burton-Jones, Yair Wand

To cite this article:

Palash Bera, Andrew Burton-Jones, Yair Wand (2014) Research Note—How Semantics and Pragmatics Interact in Understanding Conceptual Models. Information Systems Research 25(2):401-419. http://dx.doi.org/10.1287/isre.2014.0515

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/A98Y4HQM/fulltext/images/aa62a3e5a2e89ff3b7be49b08c0f4b2927d294ff0e0ec1ae76f4bc9bbff8d4c0.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# How Semantics and Pragmatics Interact in Understanding Conceptual Models

Palash Bera

John Cook School of Business, Saint Louis University, St. Louis, Missouri 63108, pbera@slu.edu

Andrew Burton-Jones

University of Queensland, UQ Business School, Brisbane, QLD 4072, Australia, abj@business.uq.edu.au

Yair Wand

Sauder School of Business, University of British Columbia, Vancouver, British Columbia, V6T 1Z2, Canada, yair.wand@sauder.ubc.ca

nderlying the design of any information system is an explicit or implicit conceptual model of the domain that the system supports. Because of the importance of such models, researchers and practitioners have long focused on how best to construct them. Past research on constructing conceptual models has generally focused on their semantics (their meaning), to discover how to convey meaning more clearly and completely, or their pragmatics (the importance of context in model creation and use), to discover how best to create or use a model in a given situation. We join these literatures by showing how semantics and pragmatics interact. Specifically, we carried out an experiment to examine how the importance of clear semantics in conceptual models—operationalized in terms of ontological clarity—varies depending on the pragmatics of readers’ knowledge of the domain shown in the model. Our results show that the benefit of ontological clarity on understanding is concave downward (follows an inverted-U ) as a function of readers’ prior domain knowledge. The benefit is greatest when readers have moderate knowledge of the domain shown in the model. When readers have high or low domain knowledge, ontological clarity has no apparent benefit. Our study extends the theory of ontological clarity and emphasizes the need to construct conceptual models with readers’ knowledge in mind.

Keywords: conceptual modeling; domain familiarity; ontological clarity; semantics; pragmatics

History: Joey George, Senior Editor; Glenn Browne, Associate Editor. This paper was received on September 11, 2012, and was with the authors 8 months for 2 revisions. Published online in Articles in Advance April 4, 2014.

## 1. Introduction

Any information system is built upon an understanding of the domain the system supports. A common practice to support this understanding is to construct a model (also known as a script) of the domain. Over time, one well-accepted principle to emerge in research and practice is that there are benefits in constructing and using models that are independent of the technology used to construct the system (Chen 1976, Denning 2003, Yourdon 1989). Such conceptual models formally describe some aspects of the domain for the purpose of understanding and communicating about it (Mylopoulos 1992).

Conceptual modeling has long been a key topic in academia (Siau and Rossi 2011) and industry (Fettke 2009). Historically, conceptual modeling research tended to be exploratory and atheoretical (Wand and Weber 2002), but over time, two theoretical traditions began to guide most research. One tradition focuses on semantics—i.e., meaning—and aims to improve conceptual modeling grammars (the constructs and rules used to construct scripts) and scripts (the descriptions of a domain produced using a grammar) so that their semantics can be conveyed more clearly and completely (Allen and March 2006, Recker et al. 2011, Weber 1997). The other tradition focuses on pragmatics—the contextual conditions that influence model creation and use—and aims to discover contexts in which models are more likely to be understood or preferred, e.g., depending on who is reading the model and what is represented (Agarwal et al. 1996, Khatri et al. 2006, Vessey and Conger 1994).

A recent review showed that there has been almost no overlap between these two traditions (Burton-Jones et al. 2009). This is problematic because a basic feature of language is that semantics and pragmatics interact, i.e., what people say and what people interpret are both a function of the context in which communication occurs (Parker and Riley 2005). This suggests that these two traditions should be studied in an integrated manner, rather than independently, so that the interaction between semantics and pragmatics can be accounted for. Following recent such calls (Khatri et al. 2006, Burton-Jones et al. 2009), we study how semantics and pragmatics interact. To scope our work, we focus on one semantic factor—the benefit of following ontological modeling guidance—and one pragmatic factor—the extent to which individuals who read conceptual modeling scripts know the domain shown in the scripts. We examine these in the context of a key task: understanding the domain shown in a script (Gemino and Wand 2004). Based on this scope, we aim to answer the following question: How does readers’ prior knowledge of the domain shown in conceptual modeling scripts moderate the effect of ontological clarity on the domain understanding that readers gain from these scripts?<sup>1</sup>

Answering this question is important theoretically because it could involve an extension to the theory of ontological clarity. It is important practically because it will shed light on the extent to which ontological guidance is likely to help in practice depending on readers’ level of domain knowledge. It is important methodologically too, because it has implications for the types of controls required in empirical studies. Finally, it has implications for other fields interested in communicating meaning. In the next sections, we describe our proposed theory, an experiment we carried out to test it, and then its implications.

## 2. Proposed Extension to the Theory of Ontological Clarity

Our intended theoretical contribution involves extending the theory of ontological clarity—an influential theory in conceptual modeling (Moody 2009, p. 774). We question one of the theory’s key assumptions— that grammars can be studied from a computational and algorithmic perspective alone (Shanks et al. 2008). That is, the theory’s predictions stem purely from a mapping between two sets—a set of ontological constructs and a set of grammatical constructs—with the central prediction being that if a script fails to exhibit a one-to-one mapping between ontological and grammatical constructs, then readers’ understanding of the represented domain will suffer. Shanks et al. (2008, p. 557) stress that such an explanation is sufficient; no psychological or contingency explanation is required:

0 0 0 the theory of ontological clarity provides a rationale for why ontological clarity is important 0 0 0 [but it] does not articulate neurophysiological processes 0 0 0 to support why this outcome will occur 0 0 0 0 Similarly, the theory of ontological clarity is not a psychological theory 0 0 0 0 [It] is also not a contingency theory. In other words, according to the theory, instances of [low clarity] will always undermine users’ understanding of conceptual models. Contextual factors 0 0 0 do not moderate associations among components in the theory (emphasis in original).

We believe that to yield reliable insights, the theory needs to be extended to include precisely such psychological and contingency aspects. Our extension is based on two arguments.

Our first argument builds upon a preliminary conference paper by Burton-Jones and Weber (1999). They drew on Mayer’s (1989, 2001) theory of learning to suggest that readers cannot help but interpret scripts in light of their prior domain knowledge. They also drew on research on long-term memory that suggests that when humans internalize a script, they do not internalize it “as is,” but rather tend to internalize it in a way that fits their existing mental model of that domain in long-term memory (Ashcraft 2002, Chinn and Brewer 1993). For example, if a script uses a construct inconsistently (offering two potential meanings), readers with extensive domain knowledge will typically just pick the meaning that makes sense in that domain. This is how individuals overcome the ambiguities of natural language in daily life (Miller 1996). These considerations led to the propositions that readers who have extensive knowledge of the domain shown in a script will be able to understand the script even if it lacks ontological clarity. Burton-Jones and Weber (1999) reported results from an experiment that provided some support for their argument. This preliminary paper has never been replicated or extended and it is to our knowledge the only direct test of the interaction between semantics and pragmatics in conceptual modeling research. Moreover, as we discuss later, the conclusions the authors drew from that study require reinterpretation in light of our work.

We illustrate these two perspectives in Figures 1(A) and 1(B). In Figure 1(C), we offer our perspective. Like Shanks et al. (2008), we propose that ontological clarity can help, and like Burton-Jones and Weber (1999), we assume that readers with extensive knowledge of the domain shown in a script (or knowledge of analogous domains) can use this knowledge to overcome ambiguities in the script. However, rather than assume a linear moderating effect, we propose an inverted-U relationship.

This leads to our second argument, regarding the form of the moderating effect. Specifically, Figure 1(C) is based on research on the assimilation of concepts in mental models and subsequent mental processing<sup>2</sup> that suggest the following:

Figure 1 Competing Propositions Regarding the Moderating Effect of Domain Knowledge

<table><tr><td>Positive effect of ontological clarity on understanding?YesNoLow Med High Reader&#x27;s domain knowledgeExplanation: Ontological clarity makes it easier to interpret the different constructs in a script and different phenomena in the domain shown in the script.</td><td>Positive effect of ontological clarity on understanding?YesNoLow Med High Reader&#x27;s domain knowledgeExplanation: As in Figure 1(A), but clarity matters less for readers with high domain knowledge because they can use their prior knowledge to resolve ambiguities in the script.</td><td>Positive effect of ontological clarity on understanding?YesNoLow Med High Reader&#x27;s domain knowledgeExplanation: As in Figure 1(B), but clarity matters less for readers with little or no domain knowledge because they will have difficulty internalizing even a clear script.</td></tr><tr><td>(A) Theory of ontological clarity (no moderation)</td><td>(B) Proposition in Burton-Jones and Weber (1999) (linear moderation)</td><td>(C) Our proposition (nonlinear moderation)</td></tr></table>

• Ontologically clearer scripts should offer little to no benefit for readers with low or very low prior domain knowledge because we expect that these readers will have an insufficiently developed mental model to incorporate much meaning from the script at all, even if it is clear. As Chinn and Brewer (1993, p. 20) explain, imagine that a student who does not know meteors’ composition is presented with this factually clear passage: “The best evidence for the impact theory of Cretaceous extinctions is the unusually high concentration of iridium in the K-T boundary.” Chinn and Brewer argue that the student is unlikely to understand the statement well enough to realize that it refers to the effect of a meteor. In other words, even factually clear information is not easily assimilated into one’s mental structure if that mental structure is itself insufficiently developed. And when assimilation fails, mental processing cannot readily occur, leading to poor

• Ontologically clearer scripts should also offer little to no benefit for model readers with high or very high domain knowledge, for the reason argued by

Burton-Jones and Weber (1999): because readers can use their knowledge to overcome ambiguities in the script (Freebody and Anderson 1983), just as people overcome ambiguities in natural language (Miller 1996). In their review of educational research, Chinn and Brewer (1993) found that this tendency was strong: “subjects will reject or reinterpret anomalous data” (p. 20) and “reinterpret [ambiguous] information to be consistent with [their] current framework” (p. 27). Not only can such subjects with high domain knowledge assimilate new concepts easily, whether they are clear or not, they can undertake subsequent mental processing easily too, because the necessary mental scripts already exist in long-term memory and can be run unconsciously, resulting in high understanding (Carston 2002, Chi et al. 1982).<sup>4</sup>

• Finally, ontologically clearer scripts should benefit readers with moderate domain knowledge. Such readers are likely to have a sufficiently developed mental model of the domain to assimilate elements of the script into long-term memory (Chinn and Brewer 1993), but are unlikely to have a sufficiently developed mental model with which to resolve all ambiguities in the script when they engage in assimilation, resulting in errors of interpretation (Miller 1996). In lay terms, we expect they will have “just enough knowledge to misunderstand” the script. In addition to facilitating assimilation, clarity also helps subsequent mental processing. In contrast to contexts where domain knowledge is high or low, when domain knowledge is moderate, deeper processing is both required (because a person does not have all the mental scripts to delegate to the unconscious) and feasible (because the person now has at least a partial mental model from which to engage in processing) (Carston 2002). Clarity facilitates processing (and thus understanding) by limiting the number of interpretations and thus the relevant space of solutions to search (Newell and Simon 1972).

Underpinning all three of these effects is a more general claim: the primacy of pragmatics over semantics. That is, as domain knowledge (a pragmatic factor) becomes very high or very low, we predict that it will tend to override or wash out the effects of ontological clarity (a semantic factor). Such a view has quite a strong precedent in linguistics. Some years ago, linguists assumed that semantic processing preceded pragmatics, i.e., when faced with a sentence, a reader would initially process the semantics and only then bring to bear prior knowledge to interpret it (Leech and Thomas 1990). However, this view was gradually displaced by the view that pragmatics precedes semantics, i.e., prior knowledge influences both what is assimilated and what is processed (Carston 2002, Leech and Thomas 1990, Sanford 2002). As linguists have now shown, a person’s domain knowledge has a very strong effect on his or her understanding of textual sentences, and it interacts with (and often overrides) the effects wrought by the grammatical structure of such sentences (Carston 2002). In this paper, we extend such work on textual sentences and guidelines of English grammar, to conceptual models and guidance from ontology.

Overall, the preceding arguments lead to our study’s formal proposition:

<sup>Proposition.</sup> The benefit of ontological clarity on readers’ understanding of a domain from a conceptual modeling script will be higher when readers have moderate prior knowledge of the domain than when they have high or low prior knowledge of the domain.

We should note two complexities that underlie this proposition. First, the three key factors in our theory— semantics, pragmatics, and understanding—are, in fact, deeply intertwined. For instance, ontological clarity is a semantic factor because it is the output of mapping grammatical constructs to real-world referents (Wand and Weber 1993), but it is also partially pragmatic because an ontology is a set of beliefs about the world and beliefs are ultimately constructed pragmatically (via experience and evolution) (Bunge 1977). One’s stock of knowledge and one’s stock of beliefs (ontology) also overlap because of the simple fact that no knowledge is certain. Semantics and pragmatics must also overlap with domain understanding (our dependent variable) because people process new information in light of their existing knowledge and beliefs, and so any test of understanding will partially reflect them.

Notwithstanding these complex overlaps, we proceed in the same fashion as linguists who have shown that even though the various components of language (syntax, semantics, and pragmatics) are intertwined, we can and should study how they interact (Leech and Thomas 1990). As we discuss later, we also proceed by separating them in our research design, e.g., by using a general ontology rather than a domain-specific one (the latter dealing more concretely with pragmatics) and by measuring domain knowledge before showing people a script and measuring domain understanding after showing it to them.

A second complexity relates to the potential range of each variable in our proposition. For ontological clarity, we scoped our study by examining whether a specific difference in clarity has an effect on understanding. Readers’ ability to use prior knowledge to overcome ambiguities might well depend on the amount of clarity lacking (e.g., a little versus a lot), but we leave this for future research. For domain knowledge, our predictions require us to cover a wide range of its values (low to high). For reasons of scope, we limit our proposition to just three points on this continuum (low, moderate, high), which we discuss further in our method section.

In summary, we aim to contribute to theory by suggesting an extension to the theory of ontological clarity. This theory currently makes no assumptions about basic cognitive processes such as assimilation and processing. We suggest expanding the theory to include them, as in Figure 1(C). We discuss potentially broader implications for theory later, but first describe our experiment and its findings.

## 3. Methodology

We used a laboratory experiment to test our proposition because there have been very few studies on this topic and we therefore wanted to maximize internal validity (per Calder et al. 1981).

## 3.1. Participants

Our participants were 54 students from a midwestern university in the U.S., taking MBA courses in management information systems and database systems. Participants received 2% of their course grade for participation. Despite concerns regarding student subjects (Compeau et al. 2012), we believe our sample was suitable for three reasons. First, research shows that students can be a fair approximation of young working professionals in this context. For instance, in a study of individuals’ ability to maintain java programs and understand UML diagrams, Arisholm and Sjoberg (2004) found little difference between students and junior professionals. Second, our study’s topic was personally and professionally relevant for our students because they were covering extended entity-relationship (EER) concepts in these two courses and many were considering careers in consulting and business analysis. Students in our study also had an average of three years’ work experience, so they had the maturity of young professionals. Third, the phenomena we are studying—the communication of meaning through visual representations—is actually a very general phenomenon. For instance, Mayer’s (1989, 2001) theories and methods, which we draw on, originated in the student learning context. Thus, we believe that a student sample is quite appropriate.

## 3.2. Task

We used the “transfer task” in both experiments, following recent studies (Bera et al. 2011, Gemino 1998). This involves asking subjects to read a conceptual modeling script and provide answers to inferential problem-solving questions about the domain shown in the script. The questions (described later) are designed to test subjects’ deep understanding of the domain after reading the script and reasoning about it rather than simply their surface understanding of the script’s features (Mayer 1989). This was necessary because our proposition focuses on participants’ understanding of the domain rather than their understanding of the script per se. Another reason for focusing on the domain rather than the script is that participants’ understanding of the script is strongly influenced by their knowledge of its syntax (Khatri et al. 2006), which was not our focus. We allowed subjects to look at their scripts when answering questions rather than requiring that they work from memory (Parsons and Cole 2005).

## 3.3. Treatments

To manipulate ontological clarity, we followed recent work (Evermann and Wand 2006, Soffer and Hadar 2007) by proposing and testing guidance for creating ontologically clear scripts. To manipulate domain knowledge, we likewise followed past work (Burton-Jones and Weber 1999, Khatri et al. 2006) in using scripts of multiple domains of differing familiarity. We describe each treatment below.

3.3.1. Ontological Clarity. Ontological clarity is affected by any of the following defects: construct overload, construct redundancy, construct excess, or construct deficit. We chose to manipulate ontological clarity via construct overload to allow us to add to recent discussions regarding its effect (Shanks et al. 2008, Shanks and Weber 2012).

Construct overload occurs when one grammatical construct is used to show more than one ontological construct. One occurrence of construct overload that has received little attention to date involves the representation of roles.<sup>5</sup> Roles are a fundamental feature of organizations (Walsh and Ungson 1991) and practitioners often use conceptual models to show roles (e.g., “customer,” “employee”). However, there are no detailed guidelines for distinguishing, in a conceptual modeling script, between things and the roles they play. For example, a modeller using the entity relationship (ER) grammar might represent a thing in the domain (e.g., person) and a role it takes (e.g., customer) using the same type of grammatical symbol (e.g., an entity with attributes). Such a conceptual modeling script would exhibit construct overload.

To address this problem, we drew on Bunge’s (1977) ontology, the most widely used ontology in information systems (IS) research (Fonseca 2007). To avoid potential confusion, we should note that in the original ER specification, and many subsequent database texts, the term “role” refers to an annotation on a script that clarifies the meaning of a relationship (Chen 1976, p. 12; Silberschatz et al. 2011). In contrast, we use “role” to refer to a distinct ontological phenomenon—the roles that actors (individuals, units) in a domain assume— and our contention is that, like any other distinct ontological phenomenon, they should be modeled in an ontologically clear way. Our arguments could be applied to many conceptual modeling grammars but we study the implications for the EER grammar (Teorey et al. 1986) because of its widespread popularity (Davies et al. 2006, Fettke 2009, Khatri et al. 2006).

In Bunge’s ontology, a thing acts on another if the first affects the state of the other. Two things are said to interact if at least one acts on the other. An interaction is manifested via a special kind of property known as a mutual property that is meaningful only in the context of two or more interacting things, e.g., the “salary of an employee” is mutual to the employee person and the organization it works for (Bunge 1977, p. 102). We use the notions of class and interaction to define a role. A class is a set of instances that possess a necessary set of common properties (Parsons and Wand 1997). These properties can be intrinsic or mutual—in the latter case they reflect interactions that all instances of the class engage in. A role is defined by additional interactions that an instance of a class may engage in with other instances (in the same or in another class). It is this set of interactions that defines the role. We term the original class the base class with respect to the role. Thus, a role is a derived ontological construct (Wand and Weber 1993) that can be represented in terms of mutual properties acquired by instances of a class when they engage in interactions. The instances of a role are instances of a base class that have acquired additional mutual properties reflecting the interactions. Such instances form a subclass of the base class. In other words, a modeller can distinguish between instances of the base class that do not assume the role, and instances of the role, by showing an additional set of mutual properties reflecting the interactions. For example, a “student” role can be shown by mutual properties such as “date\_of\_admission” and “tuition\_fee” that arise between instances of the classes “person” and “university.”

Figure 2 Distinguishing Between Things and Roles in a Domain (Guided and Unguided Versions)  
![](/api/attachments/A98Y4HQM/fulltext/images/31dc3318c4328bd1a9104973d17b3db9c411527705cb1051bfee8cb38db63d48.jpg)

Figure 2(A) shows an EER script of a library domain that follows this guidance—a guided script. It shows that a borrower is a role of a person, and that when people serve in this role they interact with a library, e.g., by having subscriptions. In this script, borrower is represented as a subclass of person, and thus it inherits all attributes of person. It has no attributes of its own, but is engaged in a relationship. Several mutual properties emerge from (manifest) the interaction— properties shared by the library and borrower—such as library\_card\_no and subscription\_end\_date. These are shown as attributes of the relationship, consistent with recent studies (Evermann and Wand 2005, 2006; Parsons 2011).

Figure 2(B) shows a script that violates the proposed guidance. In this script, Borrower is shown as a subset entity of person, but borrower contains attributes that are mutual to the borrower and library thus violating the proposed approach. We refer to it as an unguided script. The guided script has greater ontological clarity because the symbols distinguish the different types of phenomena in the domain— base classes and roles—whereas the unguided script does not and instead requires the reader to derive this distinction himself (herself) (likely based on some knowledge of the library domain). Although the same symbol (a rectangle, representing an entity type) is used to represent both things and roles in both scripts, the guided script eliminates construct overload by following a strict convention whereby entity types that reflect roles never have attributes whereas entity types that reflect things always have at least one attribute. We note that for simplicity we excluded cardinality from these scripts (and the scripts in our experiments). However, the placement of attributes in the guided script would be the same irrespective of the number of instances of borrowers and libraries (one or multiple)

and irrespective of the potential cardinalities on the relationship (1:1, 1:N, or N:M).<sup>6</sup>

Finally, we should note the effect of following the proposed guidance on the information content of scripts. As Burton-Jones et al. (2009) explain, not only should a script with greater ontological clarity be easier to interpret, it should also convey more information—in our case, information about roles. Thus, in contrast to guidelines regarding informationally equivalent scripts (Parsons and Cole 2005, Siau 2004), the approach proposed here should lead to informationally inequivalent scripts. The purpose of our experiment is to test whether this difference in information helps recipients understand the domain more effectively, and whether subjects’ prior domain knowledge or lack of such knowledge would eliminate the advantage of ontological clarity, even when it results in higher informativeness.

3.3.2. Domain Knowledge. We manipulated domain knowledge by picking three domains that we expected would vary widely in familiarity (per Burton-Jones and Weber 1999, Khatri et al. 2006). In this choice, we tried to balance the competing demands of internal validity and realism. To maximize internal validity, some researchers have studied domains that people have no knowledge of, e.g., those described purely with Greek letters (Parsons and Cole 2005). We did not do so because we felt that the reduction in ecological validity was too great as people are unlikely to see models of domains of which they have absolutely no knowledge of Parsons and Cole (2005). Conceptual models are also unlikely to be used when all people involved have complete knowledge of a domain. Even if “complete knowledge” is possible, there would be little point to using a conceptual model in such a context, because conceptual models are used to help people understand a domain (Mylopoulos 1992), so they would offer little benefit in this context.

In contrast to these extreme cases, we chose three points (low, moderate, high) that would allow us to create a strong treatment, and thereby maximize internal validity (Calder et al. 1981), which was our primary aim, while still maintaining some realism. After all, it is well known that system development projects bring together people with very different levels of domain knowledge (Vessey 2006, Vlaar et al. 2008) and we believe that the three conditions in our study correspond to the following sorts of cases:

• High domain knowledge. Users and other subject matter experts are often assigned to projects because of their deep knowledge of a domain. They are often good candidates for validating conceptual models (Genero et al. 2008, p. 538; Kim and March 1995, p. 103), even though this is often done poorly in practice (Dawson and Swatman 1999, Dobing and Parsons 2006).

• Moderate domain knowledge. Consulting firms typically operate by applying lessons from one firm to other firms. Their consultants are likely to have moderate knowledge of how any given firm works based on direct or analogous experience with other firms, but will inevitably lack detailed knowledge of a client’s unique way of doing things, at least at first. Many developers, too, are likely to acquire moderate domain knowledge of an area through working on it over time.

• Low domain knowledge. New staff on a project typically know very little about the domain until they are up to speed (Choi and Thompson 2005, p. 122). Programmers and other technical staff often lack domain knowledge too. For example, Kajko-Mattson et al. (2010, p. 55) described how a team “only received brief story descriptions or acceptance criteria. Having insufficient domain knowledge, they could not even make educated guesses.” Finally, offshoring centres often hire novices and the use of their services often entails “inherent knowledge 0 0 0 asymmetries 0 0 0 increasing the potential for misunderstandings” (Vlaar et al. 2008, p. 231).

We created the familiar, moderately familiar, and unfamiliar conditions by choosing three domains: library, aquarium management, and pharmacology.<sup>7</sup>

The library domain included concepts such as borrower and library, which we expected our student subjects to know very well. We chose aquarium management as a moderately familiar domain. It has concepts such as quarantine, exhibited animals, and habitats. Although subjects might have visited an aquarium, we expected that they would not have detailed knowledge of how one worked. For the unfamiliar domain, we focused on the impact of a drug—hydrocortisone. We did not expect business students to know its detailed workings. A Ph.D. student in pharmacology wrote the drug narrative and helped create the associated EER script.

## 3.4. Materials

For each domain, we created two EER scripts: guided and unguided, yielding six scripts in total (see Appendix A for excerpts). The difference between the guided and unguided scripts was that the unguided script violated the proposed guidance for modeling roles, whereas the guided script followed it. Specifically, the unguided scripts failed to distinguish between regular entity-types and roles, and properties of entitytypes and properties that arise out of interactions that manifest a role. Thus, the unguided scripts were overloaded because the symbols for the entity and the attribute-of-an-entity conveyed a mix of information about entities, roles, and interactions, whereas the guided scripts distinguished between entities and roles, and attributes-of-an-entity and attributes emerging from interactions that manifest a role. For example, our Appendix shows the following:

—In the library scripts (Figures A.1(A) and A.1(B), Appendix A), the guided script distinguishes between the role of librarian (shown with no attributes) and the base class library worker. In the unguided script, the librarian entity also includes attributes such as “areas of responsibilities.” The guided script clarifies that these are associated with a set of interactions (providing service) that manifest the librarian’s role.

—In the aquarium scripts (Figures A.2(A) and A.2(B), Appendix A), the guided script distinguishes between the role of animal handler (shown with no attributes) and the base class employee. The guided script also shows which attributes arise out of interactions that manifest the animal handler role (e.g., in the inspects interaction) whereas the unguided script showed these as attributes of regular entity types.

—In the pharmacology scripts (Figures A.3(A) and A.3(B), Appendix A), the guided script distinguishes between the role of memory impairing agent (shown with no attributes) and the base class hydrocortisone. In the unguided script, the entity hippocampus also includes an aspect (neurotransmitter types), which is related to both the affected organ (hippocampus) and to hydrocortisone when it acts in the role of the memory impairing agent. The guided script shows that “neurotransmitter types” is an attribute of the role.

Table 1 Illustrating the Effect of Guided and Unguided Scripts on Problem-Solving

<table><tr><td colspan="2">Example problem: If veterinarians do not report to work, what problems could the aquarium face?</td></tr><tr><td>Example correct responses</td><td>Why the guided script (see Figure A.2(A), Appendix A) should be more effective than the unguided script (see Figure A.2(B), Appendix A) in helping individuals identify such responses</td></tr><tr><td>—Animals may not get proper diet —New animals may die because of lack of proper diet</td><td>In the unguided script, suggested diet is an attribute of the animals, therefore it is difficult to associate the role of the veterinarian with an animal&#x27;s suggested diet. Figure A.2(A) (guided) shows suggested diet as a mutual property between the animals and the veterinarian and thus it is easier to relate veterinarian with suggested diet. Thus the reader of the guided model should be able to come up with correct responses more easily.</td></tr></table>

We included legends in all the scripts to explain the meanings of the symbols we used. We also ensured that there was minimal difference in the layout of the two diagrams (guided/unguided) of each domain to reduce the risk that a visual/layout difference would confound the study.

## 3.5. Dependent Measures and Hypotheses

As noted earlier, we used the transfer task to test understanding, and we used subjects’ performance in this task as our dependent measure. In Table 1, we show the effect of using guided and unguided scripts in this task. In Table 2, we show the questions used in the transfer tasks in our study and other questions for our manipulation checks and control variables. Appendix B provides details on coding.

As one of our reviewers noted, it is instructive to relate our definition of domain knowledge (shown earlier, in footnote 1) to the type of questions in the transfer task, and to our measures of prior domain knowledge in Table 2. Regarding the transfer task, Mayer (1989) explained that this task requires subjects to develop creative solutions that go beyond the semantics explicitly shown in a script by “running” their mental model of how the domain works. One’s mental model, in turn, is a product of the information shown in the script and one’s prior domain knowledge (both declarative and procedural aspects) in long-term memory (Mayer 1989). The transfer task is tailor made, therefore, for the aim of our study: examining the effects of both the script, and prior domain knowledge, on understanding. Regarding our manipulation questions, we did not include separate questions for declarative and procedural knowledge. Rather, for the self-report questions, we used general questions that would cover both aspects, and for the actual-knowledge questions, we used a mix of questions, some more declarative and others more procedural. We took this approach because we were interested in the overall effect of domain knowledge rather than the specific effect of each type (declarative/procedural). As a result, we believe the measures used in our study for domain understanding and prior domain knowledge were appropriate.

Based on these measurement items and the aforementioned treatments, we can now decompose our proposition into the following two hypotheses:

<sup>Hypotheses.</sup> The benefit of using guided scripts versus unguided scripts on participants’ performance in problemsolving questions will be higher in the moderate domain knowledge condition than in

—the low domain knowledge condition [H1];

—the high domain knowledge condition [H2].

## 3.6. Procedures

The experiment used a mixed within-and-between design, with ontological clarity manipulated between groups, and domain knowledge manipulated within groups, such that each participant received either the guided or unguided script (by random assignment) and received scripts of all three domains. The experiment had two phases: training and main study. In the training phase, subjects began by responding to our questionnaire regarding modeling knowledge and domain knowledge. They were then given 15 minutes to review basic EER concepts. For those subjects who received guided scripts, this review material explained how roles were shown in the scripts. After the review period, subjects then practiced answering problemsolving questions using a simple case, and received feedback on their performance in that task. In the main study, subjects were first asked to write down the contents of the scripts as they understood them. This task was not used to obtain a dependent measure. Rather, because problem-solving tasks require deep understanding (Mayer 1989), we used this task to engage and familiarize subjects with the scripts before the main task. After the subjects finished describing the scripts, they performed the main task of answering the problem-solving questions. This sequence was repeated with the other two domains (the order of domains being randomized to control for order effects).

As Table 2 shows, we measured participants’ modeling knowledge and domain knowledge to serve as control variables. We measured both using self-reports, following past practice (Burton-Jones and Weber 1999, Bera et al. 2011). In addition, because of the importance of domain knowledge in this study, we also used a test of actual domain knowledge, consistent with studies in psychology (O’Reilly and McNamara 2007). As additional control variables, we recorded the order of diagrams presented to subjects and the time they took to complete the task. The study took about 60 minutes to complete, but subjects varied in the exact time they took.

Table 2 Measurement Instruments

<table><tr><td>Items for the dependent variable—Problem-solving  $task^a$ </td></tr><tr><td>Library domain:1. On a certain day if the help desk person is absent, what problems might arise in the library?2. On a certain day if the library system is down, what problems might occur in the library?3. On a certain day if the librarian is absent, what problems might arise in the library?Aquarium domain:1. If a shipped animal is placed in the exhibit tank, what problems might arise?2. If a quarantine tank is broken, how can this situation be handled?3. If veterinarians do not report to work, what problems can the aquarium face?Pharmaceutical domain:1. A patient with diabetes was administered hydrocortisone intravenously. What possible reactions might happen?2. An AIDS patient with pneumonia was given hydrocortisone. What are the possible effects?3. What might be the negative long term effects of stress on the human body?</td></tr><tr><td>Items for control variables and manipulation check</td></tr><tr><td>Self-reported modeling knowledge (7-point Likert scale)1. To what extent do you have knowledge of data modeling concepts (such as entities, classes, and properties)?2. To what extent do you have experience in using data modeling concepts (such as entities, classes, and properties)?Self-reported domain knowledge (7-point Likert scale)Library domain:1. To what extent are you familiar with the different types of responsibilities of users of a library?2. To what extent do you have knowledge of the responsibilities of users of a library?Aquarium domain:1. To what extent are you familiar with the different types of employees that work in an aquarium?2. To what extent do you have knowledge of the responsibilities of employees working in an aquarium?Pharmaceutical domain:1. To what extent are you familiar with the pharmaceutical drug hydrocortisone?2. To what extent do you have knowledge of the pharmaceutical drug hydrocortisone?Actual domain knowledge (5-point  $scale)^a$ Library domain:1. Name the different types of items that can be borrowed from a library?2. Explain the functions of a library system?3. Explain briefly how a borrower can borrow items from a library?Aquarium domain:1. Name the different types of employees that might work in an aquarium?2. Describe in a few sentences the responsibilities of a veterinarian of an aquarium?3. Describe the steps taken when a new animal arrives in an aquarium?Pharmaceutical domain:1. What is hydrocortisone?2. What is the effect of hydrocortisone on bones?3. What is the effect of hydrocortisone on the immune system?</td></tr></table>

<sup>a</sup>For our coding of participants’ responses to these questions, please see Appendix B.

## 4. Results

We analyzed our results in two steps. We first checked the descriptive statistics, shown in Table 3, and the results for reliability and validity. We then tested our two hypotheses.

We first examined participants’ domain knowledge. On a seven-point scale, the average scores for selfreported domain knowledge were 5.6, 3.5, and 1.3 for the familiar, moderate, and unfamiliar domains, respectively. On a five-point scale, the average scores for actual domain knowledge were 4.7, 3.2, and 1.2. The differences were significant on both scales (p < 00001). As a result, the manipulations of domain knowledge appeared to work, offering us a suitable basis for testing our hypotheses.<sup>8</sup>

Table 3 Descriptive Statistics

<table><tr><td>Variables</td><td>Scale</td><td>Mean G</td><td>SD. G</td><td>Mean U</td><td>SD. U</td><td>Mean Av</td><td>SD. Av</td></tr><tr><td>1. Work Experience</td><td>No. of years</td><td>2.96</td><td>0.85</td><td>3.00</td><td>1.07</td><td>2.98</td><td>0.96</td></tr><tr><td>2. EER modeling familiarity</td><td>1-7</td><td>4.76</td><td>0.63</td><td>4.81</td><td>0.40</td><td>4.79</td><td>0.52</td></tr><tr><td>3. Domain familiarity P—library</td><td>1-7</td><td>5.46</td><td>0.66</td><td>5.67</td><td>0.65</td><td>5.56</td><td>0.70</td></tr><tr><td>4. Domain familiarity P—aquarium</td><td>1-7</td><td>3.35</td><td>0.60</td><td>3.56</td><td>0.58</td><td>3.45</td><td>0.60</td></tr><tr><td>5. Domain familiarity P—pharma.</td><td>1-7</td><td>1.31</td><td>0.44</td><td>1.28</td><td>0.45</td><td>1.30</td><td>0.44</td></tr><tr><td>3. Domain familiarity A—library</td><td>1-5</td><td>4.63</td><td>0.32</td><td>4.74</td><td>0.28</td><td>4.69</td><td>0.31</td></tr><tr><td>4. Domain familiarity A—aquarium</td><td>1-5</td><td>3.14</td><td>0.67</td><td>3.19</td><td>0.73</td><td>3.16</td><td>0.69</td></tr><tr><td>5. Domain familiarity A—pharma.</td><td>1-5</td><td>1.17</td><td>0.28</td><td>1.16</td><td>0.30</td><td>1.17</td><td>0.29</td></tr><tr><td>6. PS average—library</td><td> $1-6^a$ </td><td>4.16</td><td>0.90</td><td>4.19</td><td>0.62</td><td>4.17</td><td>0.77</td></tr><tr><td>7. PS average—aquarium</td><td> $1-7^a$ </td><td>2.80</td><td>0.61</td><td>2.12</td><td>0.72</td><td>2.46</td><td>0.75</td></tr><tr><td>8. PS average—pharma.</td><td> $0-3^a$ </td><td>0.28</td><td>0.20</td><td>0.23</td><td>0.22</td><td>0.26</td><td>0.21</td></tr><tr><td>9. PS time—library</td><td>Mins.</td><td>7.00</td><td>1.10</td><td>7.44</td><td>0.85</td><td>7.22</td><td>1.00</td></tr><tr><td>10. PS time—aquarium</td><td>Mins.</td><td>7.04</td><td>0.90</td><td>6.89</td><td>0.89</td><td>6.96</td><td>0.89</td></tr><tr><td>11. PS time—pharma.</td><td>Mins.</td><td>4.00</td><td>0.56</td><td>4.11</td><td>0.70</td><td>4.06</td><td>0.63</td></tr></table>

Note. PS: problem solving, G: guided group (N = 28), U: unguided group (N = 28); Av: average of the two groups, SD.: standard deviation, P: perceived, A: actual.  
<sup>a</sup>The maximum range indicates the practical maximum score as obtained in the study.

We next examined participants’ problem-solving responses. We recruited two graduate students to grade the responses using a detailed coding document. Appendix B describes the coding procedures for scoring problem-solving responses and subjects’ actual domain familiarity. Both coders coded all the responses and the responses of coder 1 were used for analysis. For inter-rater reliability, we calculated kappa values for all individual responses coded by the two coders. After multiple rounds of coding, the final kappa values were 0.92, 0.88, and 0.95 for the familiar, moderately familiar, and unfamiliar domains, respectively (similar to the final reliability values in Khatri et al. 2006). Next, we checked the reliability (internal consistency) of the problem-solving scores and their convergent validity (i.e., the extent to which the results for the three questions on each domain were consistent and followed a similar pattern). We used Cronbach’s alpha to check for reliability and the scores were acceptable (alpha = 0072). To check convergent validity, we ran a MANOVA with the responses to each problem-solving question as a dependent variable. For the highly familiar and highly unfamiliar domains, no items were significant at the 0.05 level (p = 0046, p = 0009, p = 0027 for highly familiar and p = 0007, p = 0010, p = 0014 for highly unfamiliar domains) but for the moderately familiar domain, all items were significant at the 0.05 level (p = 00004, p = 00005, p = 00001). Based on these results, we were satisfied with the reliability and validity of the data and we proceeded to test our hypotheses.

In testing our hypotheses, recall that we manipulated domain knowledge by selecting domains of differing familiarity (per Burton-Jones and Weber 1999, Khatri et al. 2006). Thus, differences in participants’ problemsolving performance could stem partly from differences in participants’ knowledge of each domain (the factor of interest) and partly from differences in the questions asked about each domain (which is not a factor of interest). Thus, we needed to control for potential differences in the questions. To do so, we tested our hypotheses according to subjects’ percentage of correct answers rather than their absolute number of correct answers. This is consistent with several studies in psychology that have used proportions of correct responses rather than absolute performance to measure differences in knowledge or competence (Ricks et al. 2007, Ricks and Wiley 2009). There are also statistical benefits to this approach, because proportional methods often have greater power (Conway et al. 2005). One difficulty with applying this procedure is that it is not possible to precisely specify a theoretical maximum for inferential problem-solving questions, because they are open-ended (Khatri et al. 2006, Mayer 1989). However, we can specify a practical maximum, based on the total number of possible correct answers that we and our coders identified, as specified in our coding document. We used this figure as the denominator for each group. Following this approach, we calculated for each subject the proportion of correct answers he or she gave for each question and for each domain, and we then averaged his or her performance across the three questions to obtain his or her overall performance for that domain.

Table 4 Relative Performance in Problem-Solving per Group

<table><tr><td rowspan="2">Group</td><td colspan="3">Problem-solving performance(average percent of correct answers)</td></tr><tr><td>High familiarity</td><td>Moderate familiarity</td><td>Low familiarity</td></tr><tr><td>Guided</td><td>0.53</td><td>0.41</td><td>0.07</td></tr><tr><td>Unguided</td><td>0.53</td><td>0.31</td><td>0.05</td></tr><tr><td>Difference</td><td>0.00</td><td>0.10</td><td>0.02</td></tr></table>

each have a main effect, as each factor tends to improve performance. To test the interaction effect—the focus of our study—we need to examine the row for the difference in Table 4. Figure 4 shows these results visually. If our hypotheses are supported, we would see an inverted-U in Figure 4, like the one shown earlier in Figure 1(C). The pattern in Figure 4 indeed supports that prediction.

Because we had treatments both between and within subjects, we used a linear mixed model to test our hypotheses. We first ran a mixed model that included our control variables, but they were not significant so we excluded them from subsequent tests. We ran two further mixed models to test our hypotheses. First, we ran a mixed model that included ontological clarity and domain knowledge as fixed factors and participants as the random factor. Our interest in this test was whether the interaction effect between ontological clarity and domain knowledge was significant. This result is necessary to support our hypotheses, but it is not sufficient because it does not indicate the form of the interaction. Thus, we needed to run a second mixed model to determine whether the form of the interaction supported H1 and H2. For this test, we computed a new factor with six levels, each level corresponding to one of the six (2 × 3) combinations in our experimental design.<sup>9</sup> We then ran a mixed model with this new variable as the fixed factor.<sup>10</sup> If the fixed factor was significant, it would indicate that the effect on performance varies across the six levels. We could then test if this variation reflects the differences that we predicted in our hypotheses by conducting specific tests for each one. The test of H1 can be written as 6MG − MU − 4LG − LU57 > 0, and the test for H2 can be written as 6MG − MU − 4HG − HU57 > 0, where each letter pair, such as MG, refers to the fixed effect estimate for that condition (e.g., MG refers to the fixed effect estimate in the moderately familiar, guided condition, per the acronyms in footnote 9 below).

Figure 3 Relative Performance in Problem-Solving Across Groups—Overall Effects  
![](/api/attachments/A98Y4HQM/fulltext/images/fdd2054faf28e389ed35e83d70d98fe10d3935dc5264900ca95acbae5c8bac95.jpg)  
Note. DK: Domain knowledge.

Figure 4 Relative Performance in Problem-Solving Across Groups—Interaction Effects  
![](/api/attachments/A98Y4HQM/fulltext/images/52e14255b356a7432107e490b61af5bf55f577d42acc585d98b095da6c88da0b.jpg)  
Note. DK: Domain knowledge.

Following this approach, we tested H1 and H2 by first obtaining the estimates of fixed effects from the output of the mixed model, then calculating the differences in the fixed effects according to the formulae above for each hypothesis, and finally manually calculating the standard error (SE) for each condition using the covariance matrix for the estimates of fixed effects. Using these figures, we could determine the significance of each effect using a t-test. For instance, the difference in the estimates of fixed effects for the test of H1 6MG − MU − 4LG − LU57 was 0.0860, the SE was 0.02754, and the degrees of freedom (df) was 135, and thus our hypothesis that the difference was greater than 0 was accepted (p = 00005). Table 5 shows our results. The first row shows the result for the interaction in the first mixed model. The second row shows the significance of the overall effect in the second mixed model (the combined factor’s effect). The significant results in these first two rows support our arguments but they are not specific enough to test our hypotheses. The third and fourth rows show that our tests for H1 and H2 were supported.

Table 5 Statistical Tests of Hypotheses

<table><tr><td rowspan="2">Results for fixed effects</td><td colspan="2">Experiment results</td></tr><tr><td>Statistics</td><td>Interpretation</td></tr><tr><td>1. Interaction (clarity × domain knowledge)</td><td> $F = 8.06, p = 0.001$ </td><td>Supported</td></tr><tr><td>2. Overall model (for the 2nd mixed model)</td><td> $F = 239.63, p < 0.001$ </td><td>Supported</td></tr><tr><td>3. Test of H1(low to moderate)</td><td> $t = 3.12 \text{ (df, } 135), p = 0.005$ </td><td>Supported</td></tr><tr><td>4. Test of H2(moderate to high)</td><td> $t = 3.74 \text{ (df, } 135), p = 0.005$ </td><td>Supported</td></tr></table>

To give a more detailed understanding of these results, we carried out two post-hoc tests. First, to ensure that our results were not driven by our use of relative rather than absolute performance scores, we ran a separate ANCOVA for each domain using the average (absolute) problem-solving scores. We obtained the same pattern of results: the effect of ontological clarity was insignificant in the highly familiar domain $( p = 0 . 9 1 )$ and the unfamiliar domain $( p = 0 . 4 0 )$ , but significant in the moderately familiar domain $( p < 0 . 0 0 1 )$ ). We do not report $R ^ { 2 }$ values for our mixed models because there is no firmly accepted way to calculate them (Kramer 2005). However, the adjusted $R ^ { 2 } { \bf s }$ for the moderately familiar domain in our ANCOVA was 0.20, suggesting a medium effect. Our second post-hoc test related to our measure of the time that participants took to complete their tasks. As noted earlier, our covariates (including time taken) were insignificant in our mixed model. However, another way to control for the effect of time is to calculate a normalized performance score (i.e., performance/time taken). We ran a separate ANCOVA for each domain using this measure and the results were again in line with our predictions: the effect of ontological clarity was insignificant in the highly familiar domain (p = 0020) and the highly unfamiliar domain $( p = 0 . 2 4 )$ but significant in the moderately familiar domain $( p = 0 . 0 2 )$ .

## 5. Discussion

In this section, we summarize the results from the study and discuss its implications.

## 5.1. Summary of the Results

Both of our hypotheses were supported. As Figure 4 and Table 5 show, the effect of ontological clarity on problem-solving performance was significantly greater in the moderately familiar case than in the unfamiliar case (per H1), and significantly greater in the moderately familiar case than in the highly familiar case (per H2). Comparing the pattern of results in Figure 4 with those of Figure 1(A) (the theory of ontological clarity), Figure 1(B) (the proposition of Burton-Jones and Weber 1999), and Figure 1(C) (our proposition), the pattern clearly resembles Figure 1(C). Overall, our results support our proposition and refute the prior proposals reflected in Figures 1(A) and 1(B). The results also support the usefulness of the new guidance we offered for modeling roles (in the moderate familiarity condition, as predicted).

## 5.2. Implications for Research

Our research underscores the need to account for domain knowledge when studying the impact of ontological principles. Specifically, if a set of ontological principles can benefit domain understanding, our results suggest that the benefit will be greatest for model readers with moderate domain knowledge, rather than low or high domain knowledge. Rather than having a consistent effect, as the theory of ontological clarity proposed (Shanks et al. 2008), or a linear moderating effect as Burton-Jones and Weber (1999) proposed, the effect of ontological clarity depends in a nonmonotone way on readers’ prior knowledge. Our work confirms the value of combining research on semantics and pragmatics, as called for but not yet studied in depth (Bera et al. 2011, Burton-Jones et al. 2009, Khatri et al. 2006).

To date, Burton-Jones and Weber (1999) is the only study to have examined whether or not domain knowledge moderates the effect of ontological clarity on understanding. Our study replicates their finding that ontological clarity ceases to matter when domain knowledge is high, and it does so with a different set of subjects and a different ontological treatment. It is also the first replication of that study. Given the vital role of replications in research (Ioannidis 2005), we believe that this is an important finding. Even so, our study is not a mere replication. In the case where domain knowledge is low, our theory and results are opposite to those of Burton-Jones and Weber (1999). Whereas they argued and found that ontological clarity would help in this context, we argued and found that ontological clarity had no effect. Moreover, whereas they suggested that the impact of ontological clarity is monotonic with the degree of knowledge, we proposed and corroborated a nonmonotonic inverted-U effect. In short, Burton-Jones and Weber (1999) did not explore the functional form of the interaction and their assumption regarding its form turned out to be incorrect. Our paper reveals its functional form (an inverted-U ).

Despite these different aims and assumptions, how could the two studies have arrived at such different (and opposite) results in the low-domain-knowledge condition? One simple explanation is that the so-called “low” domain-knowledge treatment in their study was not really low, but rather “moderate” for which we have shown that a positive effect exists. Burton-Jones and Weber (1999) did not report measures of participants’ domain knowledge, so this remains unknown. However, this could be tested directly in future research by replicating their study with a more-unfamiliar condition.

Beyond investigating the differences between those two studies, several new research directions emerge from our theory and results. One involves identifying the range of domain knowledge over which ontological clarity matters. For internal validity reasons, we manipulated domain knowledge strongly (per Calder et al. 1981). Accordingly, our results suggest that there is a tipping point somewhere between low and moderate domain knowledge (between our self-reported scores of 1.3/7.0 and 3.5/7.0) after which ontological clarity matters and a second point between moderate and high domain knowledge (between our self-reported scores of 3.5/7.0 and 5.6/7.0) after which it ceases to matter. Therefore, ontological clarity may matter over a wide range (using our data—from 1.3 to 5.6/7.0) or a narrow range (e.g., around 3.5/7.0) of domain knowledge. Future work would be needed to explore these alternatives. It is perhaps unrealistic to assume that researchers could identify precise and generalizable tipping points, but over a series of studies it should be possible to gain qualitative insights into the range of domain knowledge over which ontological clarity matters. This would be very useful theoretically (by deepening our understanding of the functional form of the interaction) and empirically (by revealing when ontological clarity is most helpful in practice).

A second direction would be to replicate our study with a deceptively familiar domain. Research has long shown that when faced with new phenomena, people inevitably make assumptions about it based on their knowledge of other instances of that type of phenomena that they can recall from prior experience (Chinn and Brewer 1993, Tversky and Kahneman 1973). This is clearly a relevant problem for business analysts and others who validate requirements in practice. In familiar domains, ambiguities in scripts could be especially dangerous because analysts may draw on past knowledge to resolve the ambiguities, but do so incorrectly, because they assume that the domain operates in the manner they expect. Research on such “familiarity bias” is beginning (Hadar et al. 2012) and could be extended. In such work on domain knowledge, we would particularly encourage researchers to investigate alternative ways of manipulating familiarity. The practice that we adopted (showing diagrams of alternative domains) is the most commonly used approach in the literature (Burton-Jones and Weber 1999, Khatri et al. 2006), but this area of research is at an early stage and it may turn out that other approaches (such as training participants in a domain prior to a task) yield different results.

Another research direction would involve examining effect sizes. In our experiments, ontological clarity did not have a large effect on domain understanding in any of the domains we studied. For instance, the value for R<sup>2</sup> from our ANCOVAs in the moderately familiar domain was 0.20. One interpretation of this could be that ontological guidance does not, in fact, matter much. Such a view would add to research that shows that ontological guidelines can help—but not dramatically so—in practice (Recker et al. 2011). However, as noted earlier, our study aimed to examine how domain knowledge moderated a given difference in clarity, not how it depended on the amount of clarity manipulated (e.g., a little versus a lot). If ontological clarity was manipulated more strongly (through violating ontological principles in more parts of a script or throughout larger scripts), the effect sizes would likely increase and the way in which domain knowledge moderates this effect would likely change too. In fact, we hope researchers will test our proposition over different levels of ontological clarity and different levels of domain knowledge to reach a more complete understanding of the moderating effect.

As stated at the outset, the intended theoretical contribution of this study was to extend the theory of ontological clarity. However, the potential theoretical contribution is broader. Specifically, conceptual modeling can be viewed as a special type of communication. In the broader literature on communication, we have not been able to find any detailed research program on the interaction of semantics and pragmatics. The closest we found to what we studied in this paper is research on the interpretation of natural language text and, in particular, the interaction between the clarity of the text (such as the presence of anomalous terms or unclear English grammar) and the domain knowledge of the reader, which has been studied to a limited extent in basic and applied psychology (Carston 2002, Chinn and Brewer 1993, O’Reilly and McNamara 2007, Ozuru et al. 2009). Even in that research, however, we were not able to find any explicit discussion of domain knowledge moderating the effect of clarity in an inverted U -shaped manner as we studied. Moreover, such research has explicitly referred to the complexity of work in this area and the need for more research (e.g., O’Reilly and McNamara 2007). Thus, we believe that our study may provide a useful contribution to that more general line of work by explicitly documenting the form of the interaction between clarity and domain knowledge, and extending the boundaries of such work from natural language sentences and the rules of English grammar to conceptual models and guidance from ontological theory.

The approach followed in our paper is quite general— it need not be limited to a specific modeling language such as ER, nor limited to a particular ontology, nor even ontology at all. It could be extended in all of these ways. For instance, rather than derive rules from ontology to improve semantic clarity, researchers could derive them from concept theory or speech-act theory (Wand et al. 1995). Our prediction would remain the same. For example, if we used rules from speech act theory to improve the semantic clarity of a sequence diagram, we would once again predict that their benefit would be greatest for readers with moderate domain knowledge. Given the importance of semantics and pragmatics in conceptual modeling and related fields (McNally 2013, Thalheim 2012), the general approach offered in our paper is important because it offers multiple directions for extension. The pragmatic aspects of conceptual modeling, in particular, are rich and largely unstudied. We investigated one aspect (domain knowledge), but other aspects such as fitness for purpose have long awaited detailed study (Lindland et al. 1994). The interaction between semantics and pragmatics can also be studied from the perspective of different philosophies of language. Although we took a formal language perspective, other more constructivist perspectives could be adopted that have different implications for the links between pragmatics and semantics that also offer exciting opportunities for research (Eriksson and Ågerfalk 2005).

A final direction for future research would be to move beyond the study of semantics and pragmatics alone and study the interactions “above” and “below” them. Research on semiotics (the study of signs) informs us that any collection of symbols, such as a script, can be examined over at least six levels (e.g., physical, empirical, syntactic, semantic, pragmatic, and social) (Stamper 1996). Although a few studies have studied the implications of these layers for systems development in general (Barron et al. 1999, Burton-Jones et al. 2005, Shanks 1999), we are not aware of any studies of the interactions among these layers in conceptual modeling. In their review of the literature, for instance, Burton-Jones et al. (2009) found that no studies had yet examined the interaction between syntax and semantics, and with the possible exception of the theoretical work by Hirschheim et al. (1995) we are not aware of any conceptual modeling studies to have examined the interaction between the pragmatic and social dimensions either. Examining these interactions in more detail would be very useful. For instance, are the effects shown in our study sensitive to the particular syntax we used to represent roles? This could be investigated using Moody’s (2009) principles for syntactic design. Similarly, it would be valuable to test potential three-way interactions between conceptual modeling knowledge, domain knowledge, and ontological clarity. Khatri et al. (2006) showed a significant interaction between conceptual modeling knowledge and domain knowledge and we showed a significant interaction between domain knowledge and ontological clarity, but a three-way interaction has not been studied.

## 5.3. Implications for Practice

As noted earlier, we weighed internal validity more heavily than ecological validity, so we have to be cautious in drawing implications for practice. Our scripts were small compared to some in industry (Moody 2009) and they did not contain symbols or semantics that were not required to create the treatment effect (e.g., concepts such as cardinality or aggregation). Likewise, we used student subjects rather than working professionals and we used tasks and measurement instruments that were created artificially for the purpose of the study. The generalizability of our study is limited in all of these ways. Nonetheless, our study can offer clues regarding the effects that might be observed in real-world settings and the kinds of real-world studies that might be undertaken to investigate these effects further.

The main implication for practice from our study would appear to be that modelers should consider the recipient of the script when deciding whether to follow ontological guidance (and, on a more general level, when deciding how much attention to pay to the semantic clarity of conceptual models). In some contexts, modelers know who will receive the scripts they create. In such cases, modelers can use our results as guides for how to create them. For instance, if the recipients have a moderate knowledge of the domain, modelers should create ontologically clear scripts. If the intended recipients have substantial domain knowledge, a rough script (even if ontologically unclear) would be adequate and the extra effort needed to produce an ontologically clear script would be unnecessary.<sup>11</sup> If the intended recipients have very little domain knowledge, no conceptual model will likely be sufficient (even, as our results show, if the scripts are ontologically clear). In such cases, other forms of communication should be used in addition or instead (e.g., verbal communications or rich narrative).

In many contexts, however, modelers will not know the recipients of the script they create because scripts can be long-lived artifacts and modelers often have little control over who obtains them and how they are interpreted (Sarker and Lee 2006). In such contexts, our results would suggest that it is best to create ontologically clear scripts, because they were no less effective than unclear scripts in any of the groups in our study and more effective in one group (the moderately familiar group, which arguably represents the most common of the three cases in practice as well). We hope future studies will test this claim in real-world settings, such as in a field experiment or an action research study.

The other reason why modelers should err on the side of creating ontologically clear scripts relates to the process of validating them with other stakeholders. For example, consider the case of analysts who create a script of a work domain and ask users to verify whether or not it accurately reflects the domain. Because users have high domain knowledge, they will likely be untroubled by ambiguities in the script, and so our results would suggest that they could approve the script as being correct even though it contains ambiguities. Unless the analysts are aware of this possibility, our results would suggest that they could then interpret the semantics incorrectly (because of their lack of knowledge of the domain) and then make inappropriate recommendations or design decisions accordingly. Thus, it would seem from the pragmatics of conceptual modeling contexts that keeping semantics clear will often be beneficial. The risk of inappropriate validation of user requirements is particularly high given that the different stakeholders involved in IS development are often unaware of each other’s lack of domain knowledge (Levina and Vaast 2008, p. 315) and analysts often do not take the process of validating requirements seriously (Dawson and Swatman 1999, Wastell 1996) and frequently misappropriate and misinterpret other peoples’ scripts (Sarker and Lee 2006). For instance, in a case study by Wastell (1996, p. 27), analysts freely admitted their lack of attention to the requirements validation process:

0 0 0 a lot of people wanted to avoid talking to users 0 0 0 they would send the documentation through the internal post [rather than talking with them] 0 0 0 users just did not understand all the documentation we threw at them.

Several studies have even found that systems analysts refrain from validating conceptual models with users because they consider the scripts to be too technical (Dawson and Swatman 1999, Dobing and

Parsons 2006). Our hope is that continued research on ways to improve the clarity and informativeness of conceptual modeling scripts—such as the research carried out here—will make conceptual models more amenable to user validation. Such research is vital given the longstanding importance of conceptual modeling in the process of systems development (Fettke 2009, Hirschheim et al. 1995).

## 6. Conclusion

The aim of our research was to study the potential interaction between semantics and pragmatics on understanding conceptual models. We did so by examining whether and, if so, how domain knowledge moderates the effect of ontological clarity on readers’ understanding of a conceptual modeling script. Consistent with our hypotheses, the results suggest that the moderating effect is concave downwards (follows an inverted-U ): ontological clarity helps when domain knowledge is moderate but does not help when domain knowledge is low or high. The underlying reason for these results seems to be the power of the human mind to make sense of unfamiliar or ambiguous stimuli. Even when a domain is quite unfamiliar, individuals seem remarkably able to leverage a little extra clarity when trying to understand a domain, and once a domain is quite familiar, individuals seem remarkably able to overcome a lack of clarity in their scripts by drawing on their prior knowledge. In addition to offering a fairly clear answer to our research question, our results affirm the basic idea that motivated our study—the idea that conceptual modeling research would benefit from a joint consideration of semantics and pragmatics. There are many ways in which this idea can be extended, and we hope future research will do so.

## Acknowledgments

The authors thank participants in the research seminar at the University of British Columbia for their comments on earlier versions of the paper. The senior editor, associate editor, and reviewers gave many valuable suggestions that helped improve the paper. We thank Bernard McKenna and Rick White for their helpful advice too. The research was supported by funds from the Natural Sciences and Engineering Council of Canada.

## Appendix A. Excerpts from the Scripts Used in the Experiments

For brevity, we just show excerpts of the full scripts used in the experiment to illustrate how the guided and unguided versions differed. The size of the full scripts used in the study were as follows: familiar domain (guided script: 13 entities, 8 relationships; unguided script: 11 entities, 8 relationships); moderately familiar domain (guided script: 14 entities, 9 relationships; unguided script: 12 entities, 9 relationships); unfamiliar domain (guided script: 13 entities, 6 relationships; unguided script: 8 entities, 6 relationships).

Figure A.1 Parts of the Guided (A) and Unguided (B) EER Scripts from the Library Domain

Scripts for the familiar domain

![](/api/attachments/A98Y4HQM/fulltext/images/699723a8c16d5ae87307dbdcc3dc689d63bf8a016e4b69d2a449de08ce68248d.jpg)

Figure A.2 Parts of the Guided (A) and Unguided (B) EER Scripts from the Aquarium Domain<sup>a</sup> Scripts for the moderately familiar domain  
![](/api/attachments/A98Y4HQM/fulltext/images/5452658bdddc3a775219ed5b362f233e069d2156be18925ed6924beb62591b77.jpg)  
<sup>a</sup>Although the excerpts in this appendix are generally self-explanatory, the entity type for “animals” in Figure A.2(A) may appear unclear. To clarify, aquarium animals are a role of species. The base class—“species”—is not shown here but was part of the larger script in the experiment. The full script showed how aquarium animals are a role assumed by some species and they inherit all properties of the appropriate species.

## Appendix B. Coding Procedures

This appendix briefly summarizes our procedures for coding participants’ responses to the problem-solving questions and the domain knowledge questions in Table 2.

## Coding Participants’ Responses to the

## Problem-Solving Questions

The following steps were taken to code the problem-solving responses (adapted from Khatri et al. 2006):

1. An extensive coding manual was prepared with a list of possible correct responses. Table B.1 provides an example of answers for one question. For the unfamiliar domain, the manual contained a description of the pharmaceutical drug and a list of incorrect responses. The description and the list were prepared by a Ph.D. student in pharmacology.

The list of incorrect responses was prepared to help the coders distinguish between those responses and other potentially correct responses.

2. The coding manual was provided to two independent coders who were unaware of the study’s aims and treatments. The first author explained the coding procedure to both coders. The coders were then asked to code sample questions and discuss their coding results. Once the coders felt that they understood the fine details of the coding procedure, they were asked to independently code the responses.

3. Before the coders started the coding they were told to refer to the sample coding first. This ensured that both coders began the coding from the same perspective, reducing the potential for “coder drift,” i.e., the tendency to change the way coding is done over time (Khatri et al. 2006).

Scripts for the unfamiliar domain

![](/api/attachments/A98Y4HQM/fulltext/images/6b3019986649d59c98115c9516a7c520cba17811978e4583ca2b5e485a515503.jpg)  
Figure A.3 Parts of the Guided (A) and Unguided (B) EER Scripts from the Pharmaceutical Domain

4. After the coding procedure was complete, both coders met with the first author and went over their responses. Where coders did not agree on particular codes, the coders discussed the differences. If they agreed after discussion then they changed their codes accordingly, else they left them unchanged. Because of the large number of responses, three such meetings were conducted.

As in Khatri et al. (2006), kappa values were around 0.70 after the first meeting and increased after subsequent meetings.

5. After the final round of comparison and agreement, the reliability of the coding was assessed and the kappa values were excellent (as noted in our Results). The coding of coder 1 was then used for analysis.

Table B.1 Sample Codes

<table><tr><td>Sample questions</td><td>Possible answers</td></tr><tr><td colspan="2">Problem solving—Moderate familiarity domain</td></tr><tr><td rowspan="2">If veterinarians do not report to work, what problems can the aquarium face?</td><td>1. Animal checkups will not take place2. Animals that are sick will not be treated3. New animals that are brought cannot be inspected4. Wrong diet can be given to existing animals5. Will not be able to suggest diet for new animals6. If an emergency situation arises with an animal then it cannot be handled</td></tr><tr><td>Domain familiarity—Actual</td></tr><tr><td>1. Explain the functions of a library system?</td><td>1. Help locate a book/journal of a specific subject (online or offline)2. Suggest books from other sources if not available in the library3. Inform the status of the book in a library (borrowed or available)4. Borrow e-book5. Provide details of the library account of a borrower</td></tr><tr><td>2. What is the effect of hydrocortisone on immune system?</td><td>1. It suppresses the immune system of a person2. The person will feel physically weak3. The person becomes susceptible to diseases4. The person will fall sick very easily5. If the person has an existing sickness then the condition will worsen rapidly</td></tr></table>

## Coding Participants’ Responses to the Domain Knowledge Questions

These questions were coded by an independent coder using a coding manual that contained a list of possible answers. The coder provided a number from 1 to 5 for each set of responses based on the following procedure: 0: no response or incorrect response; 1: one correct response; 2: two correct responses; 3: three correct responses; 4: four correct responses; and 5: five or more correct responses. Table B.1 provides examples of correct responses for each question.

## References

Agarwal R, Sinha AP, Tanniru M (1996) Cognitive fit in requirements modeling: A study of object and process methodologies. J. Management Inform. Systems 13(2):137–164.

Alexander PA (1992) Domain knowledge: Evolving themes and emerging choices. Educational Psych. 27(1):33–51.

Allen GN, March ST (2006) The effects of state-based and event-based data representations on user performance in query formulation tasks. MIS Quart. 30(2):269–290.

Arisholm E, Sjoberg DIK (2004) Evaluating the effect of a delegated versus centralized control style on the maintainability of objectoriented software. IEEE Trans. Software Engrg. 30(8):521–534.

Ashcraft MH (2002) Cognition, 3rd ed. (Prentice Hall, Upper Saddle River, NJ).

Barron TM, Chiang RHL, Storey VC (1999) A semiotics framework for information systems classification and development. Decision Support Systems 25:1–17.

Bera P, Burton-Jones A, Wand Y (2011) Guidelines for designing visual ontologies to support knowledge identification. MIS Quart. 35(4):883–908.

Bera P, Burton-Jones A, Wand Y (2013) Improving the representation of roles in conceptual modeling: Theory, method, and evidence. Working paper, Saint Louis University, St. Louis.

Bunge M (1977) Treatise on Basic Philosophy: Volume 3: Ontology I: The Furniture of the World (Reidel, Boston).

Burton-Jones A, Weber R (1999) Understanding relationships with attributes in entity-relationship diagrams. De P, DeGross JI, eds. 20th Internat. Conf. Inform. Systems, Charlotte, NC (AIS, Atlanta), 214–228.

Burton-Jones A, Wand Y, Weber R (2009) Guidelines for empirical evaluations of conceptual modeling grammars. J. Assoc. Inform. Systems 10(6):495–532.

Burton-Jones A, Storey VC, Sugumaran V, Ahluwalia P (2005) A semiotic metrics suite for assessing the quality of ontologies. Data and Knowledge Engrg. 55(1):84–102.

Calder BJ, Phillips LW, Tybout AM (1981) Designing research for application. J. Consumer Res. 8(September):197–207.

Carston R (2002) Linguistic meaning, communicated meaning and cognitive pragmatics. Mind and Language 17(1–2):127–148.

Chen PPS (1976) The entity-relationship model: Toward a unified view of data. ACM Trans. Database Systems 1(1):9–36.

Chi MTH, Glaser R, Rees E (1982) Expertise in problem solving. Sternberg RJ, ed. Advances in the Psychology of Human Intelligence (Erlbaum, Hillsdale, NJ), 7–75.

Chinn CA, Brewer WF (1993) The role of anomalous data in knowledge acquisition: A theoretical framework and implications for science instruction. Rev. Educational Res. 63(1):1–49.

Choi H-S, Thompson L (2005) Old wine in a new bottle: Impact of membership change on group creativity. Organ. Behav. Human Decision Processes 98:121–132.

Compeau DR, Marcolin BL, Kelley H, Higgins C (2012) Generalizability of information systems research using student subjects—A reflection on our practices and recommendations for future research. Inform. Systems Res. 23(4):1093–1109.

Conway AR, Kane MJ, Bunting MF, Hambrick DZ, Whilhelm O, Engle RW (2005) Working memory span tasks: A methodological review and user’s guide. Psychonomic Bull. Rev. 12(5):769–786.

Davies I, Green P, Rosemann M, Indulska M, Gallo S (2006) How do practitioners use conceptual modeling in practice? Data Knowledge Engrg. 58(3):358–380.

Dawson L, Swatman P (1999) The use of object-oriented models in requirements engineering: A field study. De P, DeGross JI, eds. Internat. Conf. Inform. Systems, Charlotte (AIS, Atlanta), 260–273.

Denning P (2003) Great principles of computing. Comm. ACM 46(11):15–20.

Dobing B, Parsons J (2006) How UML is used. Comm. ACM 49(5): 109–113.

Eriksson O, Ågerfalk PJ (2005) Information modeling based on semantics and pragmatic meaning. Siau K, ed. Advanced Topics in Database Research, Vol. 4 (Idea Group Publishing, Hershey, PA), 201–217.

Evermann J, Wand Y (2005) Ontology based object-oriented domain modeling: Fundamental constructs. Requirements Engrg. 10: 146–160.

Evermann J, Wand Y (2006) Ontological modeling rules for UML: An empirical assessment. J. Comput. Inform. Systems 46(5):14–29.

Fettke P (2009) How conceptual modeling is used. Comm. AIS 25(1):571–592.

Fonseca F (2007) The double role of ontologies in information science research. J. Amer. Soc. Inform. Sci. Tech. 58(6):786–793.

Freebody P, Anderson RC (1983) Effects of vocabulary difficulty, text cohesion, and schema availability on reading comprehension. Reading Res. Quart. 18(3):277–294.

Gemino A (1998) To be or may to be: An empirical comparison of mandatory and optional properties in conceptual modeling. Tannous GF, ed. Annual Conf. Admin. Sci. Assoc. Canada, Inform. Systems Division, Saskatoon, Saskatchewan (College of Commerce, University of Saskatchewan, Saskatoon, Canada), 33–44.

Gemino A, Wand Y (2004) A framework for empirical evaluation of conceptual modeling techniques. Requirements Engrg. 9(4, November):248–260.

Genero M, Poels G, Piattini M (2008) Defining and validating metrics for assessing the understandability of entity-relationship diagrams. Data Knowledge Engrg. 64:534–557.

Hadar I, Soffer P, Kenzy K (2012) The role of domain knowledge in requirements elicitation via interviews: An exploratory study. Requirements Engrg. J. ePub ahead of print September 23, http://dx.doi.org/10.1007/s00766-012-0163-2.

Hirschheim R, Klein H, Lyytinen K (1995) Information Systems Development and Data Modeling: Conceptual and Philosophical Foundations (Cambridge University Press, Cambridge, UK).

Ioannidis JPA (2005) Why most published research findings are false. PLoS Medicine 2(8):0696–0701, http://www.plosmedicine.org/ article/info:doi/10.1371/journal.pmed.0020124.

Kajko-Mattson M, Azizyan G, Magarian MK (2010) Classes of distributed agile development problems. Freudenberg S, Chao J, Kruchten P, eds. 2010 Agile Conf., August 9–13 (IEEE Computer Society, Washington, DC), 51–58.

Khatri V, Ramesh V, Vessey I, Clay P, Park S-J (2006) Understanding conceptual schemas: Exploring the role of application and IS domain knowledge. Inform. Systems Res. 17(1):81–99.

Kim YG, March ST (1995) Comparing data modeling formalisms. Comm. ACM 38(6):103–115.

Kramer M (2005) R<sup>2</sup> statistics for mixed models. Proc. 17th Annual Kansas State University Conf. Appl. Statist. Agriculture, Kansas, April 24–26 (Kansas University Press, Manhattan, Kansas), 148–160.

Leech G, Thomas J (1990) Language, meaning and context: Pragmatics. Collinge NE, ed. An Encyclopaedia of Language (Routledge, London), 94–113.

Levina N, Vaast E (2008) Innovating or doing as told? Status differences and overlapping boundaries in offshore collaboration. MIS Quart. 32(2):307–332.

Lindland OI, Sindre G, Sølvberg A (1994) Understanding quality in conceptual modeling. IEEE Software 11(2):42–49.

Mayer R (1989) Models for understanding. Rev. Educational Res. 59:43–64.

Mayer RE (2001) Multimedia Learning (Cambridge University Press, New York).

McNally L (2013) Semantics and pragmatics. Wiley Interdisciplinary Reviews: Cognitive Science 4(3):285–297.

Miller GA (1996) Contextuality. Oakhill J, Garnham A, eds. Mental Models in Cognitive Science (Psychology Press, East Sussex, UK), 1–18.

Moody DL (2009) The “physics” of notation: Toward a scientific basis for constructing visual notations in software engineering. IEEE Trans. Software Engrg. 35(6):756–779.

Mylopoulos J (1992) Conceptual modeling and Telos. Loucopoulos P, Zicari R, eds. Conceptual Modeling, Databases and Case: An Integrated View of Information Systems Development (John Wiley & Sons, New York), 49–68.

Newell A, Simon HA (1972) Human Problem Solving (Prentice Hall, Englewood Cliffs, NJ).

O’Reilly T, McNamara DS (2007) Reversing the reverse cohesion effect: Good texts can be better for strategic, high-knowledge readers. Discourse Processes 43(2):121–152.

Ozuru Y, Dempsey K, McNamara DS (2009) Prior knowledge, reading skill, and text cohesion in the comprehension of science texts. Learn. Instruction 19:228–242.

Parker F, Riley K (2005) Linguistics for Non-Linguists: A Primer with Exercises, 4th ed. (Pearson/Allyn and Bacon, Boston).

Parsons J (2011) An experimental study of the effects of representing property precedence on the comprehension of conceptual schemas. J. Assoc. Inform. Systems 12(6):441–462.

Parsons J, Cole L (2005) What do the pictures mean? Guidelines for experimental evaluation of representation fidelity in diagrammatical conceptual modeling techniques. Data and Knowledge Engrg. 55(3):327–342.

Parsons J, Wand Y (1997) Choosing classes in conceptual modeling. Comm. ACM 40(6):63–69.

Recker J, Rosemann M, Green P, Indulska M (2011) Do ontological deficiencies in modeling grammars matter? MIS Quart. 35(1): 57–79.

Ricks TR, Wiley J (2009) The influence of domain knowledge on the functional capacity of working memory. J. Memory Language 61(4):519–537.

Ricks TR, Turley-Ames KJ, Wiley J (2007) Effects of working memory capacity on mental set due to domain knowledge. Memory Cognition 35(6):1456–1462.

Sanford AJ (2002) Context, attention and depth of processing during interpretation. Mind Language 17(1–2):188–206.

Sarker S, Lee AS (2006) Does the use of computer-based BPC tools contribute to redesign effectiveness? Insights from a hermeneutic study. IEEE Trans. Engrg. Management 53(1):130–145.

Shanks G (1999) Semiotic approach to understanding representation in information systems. Dampney CNG, ed. Proc. Inform. Systems Foundations Workshop (Macquarie Universtiy, Sydney, Australia).

Shanks G, Weber R (2012) The hole in the whole: A response to Allen and March. MIS Quart. 36(3):965–980.

Shanks G, Tansley E, Nuredini J, Tobin D, Weber R (2008) Representing part-whole relations in conceptual modeling: An empirical evaluation. MIS Quart. 32(3):553–573.

Siau K (2004) Informational and computational equivalence in comparing information modeling methods. J. Database Management 15(1):73–86.

Siau K, Rossi M (2011) Evaluation techniques for systems analysis and design modeling methods—A review and comparative analysis. Inform. Systems J. 21:249–268.

Silberschatz A, Korth H, Sudarshan S (2011) Database System Concepts (McGraw Hill Education, New York).

Soffer P, Hadar I (2007) Applying ontology-based rules to conceptual modeling: A reflection on modeling decision making. Eur. J. Inform. Systems 16(5):599–611.

Stamper RK (1996) Signs, information, norms and systems. Holmqvist B, Andersen PB, Klein H, Posner R, eds. Signs at Work (De Gruyter, Berlin), 349–397.

Teorey TL, Yang D, Fry JP (1986) A logical design methodology for relational databases using the extended entity-relationship approach. ACM Comput. Surveys 18(2):197–222.

Thalheim B (2012) Syntax, semantics, and pragmatics of conceptual modeling. Bouma G, Ittoo A, Metais E, Wortmann H, eds. 17th Internat. Conf. Appl. Natural Language Processing to Inform. Systems (NLDB) (Springer, Groningen), 1–10.

Tversky A, Kahneman D (1973) Availability: A heuristic for judging frequency and probability. Cognitive Psych. 5:207–232.

Vessey I (2006) The effect of the application domain in IS problem solving: A theoretical analysis. Hart D, Gregor S, eds. Information Systems Foundations: Theory, Representation, and Reality (ANU Press, Canberra, Australia), 25–48.

Vessey I, Conger SA (1994) Requirements specification: Learning object, process, and data methodologies. Comm. ACM 37(5): 102–113.

Vlaar PWL, van Fenema PC, Tiwari V (2008) Cocreating understanding and value in distributed work: How members of onsite and offshore vendor teams give, make, demand, and break sense. MIS Quart. 32(2):227–255.

Walsh JP, Ungson GR (1991) Organizational memory. Acad. Management Rev. 16(1):57–91.

Wand Y, Weber R (1993) On the ontological expressiveness of information systems analysis and design grammars. J. Inform. Systems 3:217–237.

Wand Y, Weber R (2002) Information systems and conceptual modeling—A research agenda. Inform. Systems Res. 13(4):363–376.

Wand Y, Monarchi DE, Parsons J, Woo CC (1995) Theoretical foundations for conceptual modeling in information systems development. Decision Support Systems 15:285–304.

Wastell DG (1996) The fetish of technique: Methodology as a social defence. Inform. Systems J. 6:25–40.

Weber R (1997) Ontological Foundations of Information Systems (Coopers & Lybrand and Accounting Association of Australia and New Zealand, Melbourne, Australia).

Wiley J (1998) Expertise as mental set: The effects of domain knowledge in creative problem solving. Memory and Cognition 26(4):716–730.

Yourdon E (1989) Modern Structured Analysis (Prentice Hall, Englewood Cliffs, NJ).
