---
otero_id: 26669
otero_key: "6X86RDY6"
title: "Claims, Arguments, and Decisions: Formalisms for Representation, Gaming, and Coordination"
authors: "R. Ramesh; Andrew B. Whinston"
year: "1994"
journal: "Information Systems Research"
doi: "10.1287/isre.5.3.294"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/6X86RDY6/fulltext/images/c243073b9c1c744330be0ba5ab366ec62ae59043b91143412e87235e6aa1bb3b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Claims, Arguments, and Decisions: Formalisms for Representation, Gaming, and Coordination

R. Ramesh, Andrew B. Whinston,

To cite this article:

R. Ramesh, Andrew B. Whinston, (1994) Claims, Arguments, and Decisions: Formalisms for Representation, Gaming, and Coordination. Information Systems Research 5(3):294-325. http://dx.doi.org/10.1287/isre.5.3.294

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1994 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/6X86RDY6/fulltext/images/4397f78970e29c453d8bfe11578ff4ab246bb522ca57191587699d81939dab7f.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

Claims, Arguments, and Decisions: Formalisms for Representation, Gaming, and Coordination

R. Ramesh

Department of Management Science and Systems School of Management

State University of New York at Buffalo

Andrew B. Whinston

Buffalo. New York, 14260

Department of Management Science and Information Systems

College of Business Administration

The University of Texas at Austin

Austin, Texas 78712

Decisions in large corporations continually evolve from several group processes, shaping the focus of business activities over time. These decisions arise out of a combination of formal analyses and less formal interactions among decision makers. We address the pragmatics of group decision processes from the perspective of argumentation and analysis. We develop formalisms for the representation of argumentative knowledge, gaming the argumentation process and the coordination of the games. The representation formalism provides a framework for organizing the logic underlying the claims and arguments in a group. The gaming formalism provides a framework for conducting and regulating the group interactions. The coordination formalism addresses the issues of scheduling the games and the resolution process. The three formalisms together constitute the basis for designing computer-assisted systems that support argumentation processes in groups. We introduce the term Argumentative Reasoning Facilitation Systems (ARFS), and develop a framework for their design. These systems would serve to record, organize, regulate and coordinate argumentative decision processes in organizations. The formalisms provide new windows for research on novel applications of decision support systems in organizations. Some of the systemic, organizational and behavioral research issues identified from this work are also presented.

Organization-Decision-making-Groups-Argument theory-Knowledge representation-Nonmonotonic logic-Structured modeling-Systems integration

## 1. Introduction

he focus of this paper is on the claims and arguments that surround the decisions made in an organization. In most decision scenarios, unless a decision is obvi-

1047-7047/94/0503/0294/\$01.25 Copyright © 1994, The Institute of Management Sciences

Information Systems Research 5 : 3

ously clear-cut, there exists at least a loosely woven fabric of claims and arguments supporting or opposing the decision choices. In the context of group decision making in organizations, such a fabric evolves out of the interactions among the group members in both collaborative problem-solving and negotiating situations. Even in other contexts such as an individual making all the decisions or a deliberating jury, it is not unusual that decisions evolve from a substratum of claims and arguments. Furthermore, although it is conceivable that decisions could be influenced by certain less tangible forces such as persuasiveness or exigencies, for example, these forces usually manifest in the form of claims and arguments, and propel or inhibit decisions. Therefore, it is natural to analyze the strengths and weaknesses of the claims and arguments that drive a decision making process. The decision makers in general analyze the reasoning behind the arguments, albeit informally. However, arguments could assume highly subtle forms, and it could be extremely difficult to penetrate beneath their surface structure in validating their logical consistency and underlying premises (Mitroff et al. 1982). The analysis of arguments tends to be even more complex when several decision makers are involved and arguments for conflicting positions are proposed. The complexity of the arguments could impose a substantial cognitive burden in their assimilation and analysis, especially since most decision makers are limited by their bounds of rationality (Simon 1957). As a result, it is not uncommon that many organizational decisions tend to be molded by the less tangible forces, and their underlying arguments seldom penetrated. This observation provides the motivation as well as the stage for this research.

The objectives of this work are to develop a formalism for the representation and analysis of the arguments in a group, leading to mechanisms for gaming and coordinating the group interactions. These formalisms would form the basis for developing Argumentative Reasoning Facilitation Systems (ARFS), a term that we introduce in this paper. The role of such systems in group deliberations is to structure arguments in a logically sound and complete framework and facilitate the interactions effectively. Logical structuring of arguments and coordination are crucial to effective group decision making. The absence of logical structuring could lead to a poor grasp of the issues by the decision makers, and the absence of coordination could result in delayed and possibly incorrect decisions. Together, these could lead to either gridlocks or expedient decisions that are not necessarily well argued for and well supported by most. Therefore, it often becomes necessary for some individuals to take the initiative to structure the various positions in the group and focus the discussions. Systems such as ARFS could precisely provide this support by structuring and facilitating the discussions throughout. As an end result, we expect a reduction in the cognitive load on the decision makers, a better understanding of the issues and possibly faster convergence to fairly well supported decisions. These behavioral issues are promising avenues for future empirical research. With this perspective, we introduce the decision scenarios in consideration in the following discussion.

Decision making in large organizations is a complex evolutionary process. In a corporate environment, decisions continually evolve from several layers of the organizational structure, shaping the scope and direction of the business operations over time. In the evolutionary scheme, decisions often interact, in the sense that decisions build on past decisions and their consequences, and also affect the course of the future decisions. The dynamics of this evolution are captured in the conceptual paradigm shown in Figure 1. This paradigm is based on the premise that decisions evolve from the fabric of claims and arguments, and that the fabric is woven from the knowledge garnered from past experiences and the current environment. We illustrate this paradigm by adapting it to a group decision process as follows. Consider the problem of strategy formulation in the diversification of existing product lines facing a group of top-level executives. The issues here are: (i) selection of appropriate target markets to diversify into, (ii) committment of company resources in each line, and (iii) channeling of resources in the various diversifying operations. The individuals in the group perform their respective analyses of the issues, and propose certain courses of actions. The proposed actions have their respective lines of reasoning derived from the analyses. Each proposed action could have both supporters and opponents in the group, and the argumentation centers on these actions. As a result, certain actions may be accepted, while the others rejected. The acceptance or rejection of a proposal is the outcome of argumentation. This could generate certain new proposals as well, and thus extending the argumentation. This process continually evolves until all the primary issues are resolved. The above sequence is captured in the loop between proposals, argumentation and revised reasoning in the paradigm.

![](/api/attachments/6X86RDY6/fulltext/images/b3753b32bd007565b9bb0debfd8eb41b845f09103f6e6004df54414573393c3f.jpg)  
FIGURE 1. Decision Evolution Process

The acceptance of proposals translates to decisions to implement the actions contained in them. The effects of the actions are analyzed both during implementation and afterwards, causing the executives to learn more about their operations. The changing environment, the business operations and the outcomes of earlier decisions give rise to new issues. and the process of analysis and argumentation continues. This is captured as the feedback loop from learning in the paradigm.

The above paradigm constitutes the basis of the proposed formalisms. These formalisms have been specifically designed to support the argumentation process, which is the core of the paradigm. Decision scenarios as above are typical in corporate management, and constitute the focus of this research. We assume the following characteristics of an argumentation process which can, in general, be abstracted from many decision situations.

(1) The decisions are made by a group of individuals.

(2) The group is faced with an issue or a set of issues to be resolved.

(3) Proposals for actions addressing the issues are considered and debated by the group.

(4) The individuals in the group assume positions. A position is either a claim or a contrapositive of another claim, with or without supporting arguments.

(5) Argumentation centers on positions. The process is initiated by a challenging position. A challenge may occur either as a need for a valid argument to support a position or as a contraposition with or without supporting arguments.

(6) A challenged position requires appropriate response from the individuals asserting the position. The sequence of challenges and responses constitute the dialogical component of the argumentation process (Lorenzen 1987). This component is termed the argument game. An argument game terminates when either the position is upheld or withdrawn as a result of the game.

(7) A position may presuppose the assertion of a few other earlier positions as well. These earlier positions are termed pre-positions. Therefore, in defending a position, it may become necessary to defend certain pre-positions as well. As a result, a game could move into the pre-positions recursively.

(8) The ultimate issues are resolved from the argumentation according to the decision style of the group. Decision style is defined as the mechanism adopted by the group to reach the final resolution. Such a mechanism could be a voting rule, for example. The decision style is usually determined by the nature of decisions to be made, the group composition and the group size.

The key concepts in the above model of an argumentation process are: claims, arguments, positions, challenge, defense and decision style. Although a position is basically a claim, it signifies a major claim characterizing an individual's beliefs and can be regarded as a key claim in the chain of arguments proposed. An individual supporting a claim is said to be its proponent, and an individual challenging it is said to be its opponent. The proposed formalisms are based on the above model. We first develop a language for argument representation based on the principles of formal logic. Using this language, we then develop a network architecture of the arguments. This network is termed the Claims-Arguments-Proposals (CAP) Net. The CAP-net drives the argumentation process. The interactions during this process are modeled through an Argument Gaming formalism and a Coordination formalism. These formalisms are the central components of an ARFS, whose functions can be broadly described as follows.

(a) Provide a knowledge base using a logically consistent and sound representation that captures the collective knowledge of the individuals on the decision problem and the various proof strategies that they may use to establish claims and arguments.

(b) Provide a systematic framework to conduct and capture the exchanges between the individuals during argumentation.

(c) Provide flexible and adaptive coordination mechanisms to guide and focus the argumentation process. These mechanisms would employ the knowledge base and the framework for argumentation in facilitating the process.

(d) Provide systemic tools for testing arguments for logical validity and soundness (Gensler 1990) wherever possible. These tools can be regarded as the theorem-proving components of an ARFS, and are intended to facilitate the individuals in the construction of proof strategies.

(e) Provide systemic tools to assess the strengths of arguments using appropriate models of strength assessment and also enable what-if analyses, such as “what if a certain claim is accepted"

In this research, we address functions (a), (b) and (c). The functions (d) and (e) pertain to the expert assistance such systems could provide to the group. The constructs developed in this paper are the backbone of an ARFS system and can be adapted to various theorem-proving strategies and what-if analyses. We are currently developing some of these algorithms and models. We address the key attributes of the conceptual basis of an ARFS in the following discussion.

The collective knowledge base of a group could exhibit nonmonotonic behavior, since not all individuals may agree on certain claims and arguments. These points of contention drive the argumentation process. The CAP-net is used to identify these points, and the interactions among the individuals are scheduled around them. Consequently, an ARFS could act as a facilitator of a group, in addition to providing traditional information systems support. The proposed formalisms are rooted in the pragmatics of organizational decision making and avoid many of the problems with the conventional decision analysis tools, such as decision trees. The major problems with these methods can be summarized as follows. First, they require a prior knowledge of all decision alternatives and possible outcomes, while decision aternatives actually evolve and the outcomes could change over time in many organizational decision processes. Consequently, they fail to capture fully the time-dependent development of decisions in organizations. Second, they also ignore a key element of organizational decision making: argumentation. The important decisions in many organizations are products of argumentation and conflicting positions. Third, they rely heavily on quantitative parameters such as outcome probabilities, whose interpretation is not always objective. Decision tools employing a quantification of subjective assessments may fail to capture the imagination or the conviction of the decision makers. Conviction in proposed actions arises when they are justified argumentatively, unless decisions are made intuitively. Even in the intuitive cases, at least partially supporting lines of reasoning are usually presented to win group support Fourth, they usually employ decision criteria such as maximin, expected payoffs and others, which may not be truly consistent with the group behavior. The proposed approach specifically addresses these problems by taking into account the behavioral elements in organizational decision making. We do not assume that all the decision alternatives are available up front, but instead treat them as evolving from analyses and argumentation. In this way, we allow the group to determine all the interactions collectively and argumentatively. We eliminate the dependence on quantitative parameters and ad hoc decision criteria by replacing them with consensually reached determinations of possible outcomes. This captures the imagination, involvement and collective conviction of group members in choosing action plans. While the traditional tools are prescriptive models of decision making, the proposed system does not prescribe what decisions to make, but simply facilitates the decision makers in arriving at a best consensual decision. This is achieved using a descriptive model of the argumentation process, which forms the basis for structuring, coordinating and integrating group interactions in a practical and efficient manner.

The organization of this paper is as follows. The foundations of the proposed formalisms are discussed in §2. The formalism for representation is developed in §3. The argument gaming formalism is developed in §4 and the coordination formalism in §5. The concluding remarks and the issues for future research are presented in §6.

## 2. Research Foundations

The focus of the current research is on the application of argument analysis to group decision problems, leading to the development of information systems for both traditional and argumentation support. Argument analysis has traditionally been considered in the domain of logic and philosophy, and some of the earliest works date as far back as Socrates and Aristotle. Modern renditions of logical argument analysis have come from pioneering philosophers such as Russell, Lorenzen, and Toulmin, among others. Toulmin (1958, 1979) proposed a framework of analysis to capture the subtleties and intricacies of the process of reasoning in argumentation. Toulmin analyzed arguments using five basic constructs: claims, warrants, backing for warrants, supporting data, and rebuttals. Using the Toulmin system, Mitroff et al. (1982) propose a framework for analyzing ill-structured decision problems. Using plausibility theory, they determine a maximally consistent set of assertions that is likely to be most plausible. However, they do not address the problems of reconciling conflicting positions and arriving at a common resolution. Locks (1985) provides a review and evaluation of the framework of Mitroff et al. with more insights on the boolean implications of their logic formalism. Kimbrough (1986) develops a graph representation of arguments and develops algorithms for determining whether a claim is logically consistent with the basic premises from which the claim is derived. The system proposed by Kimbrough is a full theorem-prover for sentence logic using a graph model of arguments, and is an alternative to that of Mitroff et al., which uses the well-known logic reduction method. In summary, the works of Toulmin, Mitroff et al. and Kimbrough develop formalisms for argument logic representation and methods for determining their logical consistency.

Alongside the Toulmin system, Lorenzen (1965, 1984, 1987) proposed an alternate approach to the analysis of arguments. Lorenzen introduced the construct of a dialogical argument game and captured argumentation as a dialogue between a proponent and an opponent. According to the Lorenzen model, a dialogical argument game proceeds as follows. Initially, a proponent makes a set of assertions and derives a conclusion, without providing the argument for proving the conclusion logically from the assertions. Agreeing with the proponent's assertions, the opponent challenges the conclusion, initiating the argumentation process. In defense, the proponent makes a set of new assertions derived from the earlier ones. If the opponent agrees with all the new assertions, then the proponent continues to produce more new assertions as before. If the opponent challenges any of the assertions, then the proponent could respond with either a counterchallenge or continue the proof process with more defending assertions. With a counterchallenge, it becomes mandatory for the opponent to defend his challenging position. Consequently, the opponent derives a series of assertions, and the two now reverse their roles with the proponent challenging the opponent's claims. The Lorenzen model requires that each derived assertion be logically consistent with the earlier assertions accepted by the deriving individual.

The dialogical game continues until one of the two individuals reaches a self-contradiction. Lorenzen presents a set of winning rules for a proponent under a variety of debates as above, and also hints at the complexity of the resolution process.

The Lorenzen model, although construed as a dialogical game, is a general framework for a theorem-prover. The dialogical game could also capture the thought processes within an individual solving a logic problem. A comparison of the Toulmin and Lorenzen systems leads to several useful insights in modelling argumentation processes. This is shown as follows.

The Toulmin system is essentially a representation formalism, which can be used by a theorem-prover in determining the logical consistency of arguments. The systems proposed by Mitroff et al. and Kimbrough essentially do that. In contrast, the Lorenzen model is a formalism for gaming and coordination. The focus of the Lorenzen model is on the proof strategies, rather than on formal representation. Consequently, any representation scheme can be used in following his proof strategies. In fact, Lorenzen develops his models using the standard language of predicate logic. The key notion in the Lorenzen model is that proof strategies can be developed as a dialogue between two individuals, which captures the essence of argumentation.

In our view. the Toulmin and the Lorenzen systems ideally complement each other. Together, they provide a framework for the representation and gaming of arguments. The proposed formalisms are rooted in an integration of these two systems. The CAP-net is motivated by the Toulmin system of representation, and the formalisms for gaming and coordination are motivated by the Lorenzen system of argumentation. Although the concepts developed by Toulmin and Lorenzen originate from the domains of logic and philosophy, they have considerable relevance to the problem of group decision making, where argumentation is a key player. The proposed formalisms are an adaptation of the two systems to the development of practical computer aids for group decision making.

The above discussion positions our work in the context of research on argument analysis. We now consider other related research in the contexts of knowledge representation and group decision making. The proposed representation formalism captures nonmonotonic knowledge and is similar to the truth maintenance systems proposed in the knowledge representation literature (Doyle 1979, Zlatareva 1992). In fact, many truth maintenance systems attempt to find most consistent conclusions from a nonmonotonic knowledge base and in this respect are somewhat similar to the systems proposed by Mitroff et al. and Kimbrough. For example Chang et al. (1993) present mechanisms for argument resolution in the audit process. However, in the proposed architecture of an ARFS, the resolution is arrived at by the decision makers through argumentation. The conceptual foundations of an ARFS are similar to those of Issue Based Information Systems (IBIS) (Kunz and Rittel 1970, McCall 1987) and deductive database systems (Gallaire et al. 1984). However, IBIS is mainly an architecture for information storage and retrieval and does not address the logic components of argumentation or the issues of gaming and coordination. The deductive database systems are only concerned with intelligent query processing through deductive mechanisms and do not address the specific issues of argumentation. In contrast, an ARFS is intended to support argumentation through mechanisms for the storage and retrieval of argumentative knowledge, gaming, and coordination of the argumentation processes. Therefore, an ARFS can be considered an enhancement of these earlier systems, designed specifically for the needs of argumentation processes.

Thagard (1989) addresses the problem of coherence in competing arguments and develops a connectionist version of a resolution mechanism. Similar connectionist models can be adaptively developed in the present context as well, and this could be the component of an ARFS to assess the strengths of arguments and provide what-if analyses. This is an area that we intend to study in the future. While research on group decision making is quite extensive, we are not aware of any work that addresses this problem from the point of view of supporting decisions from an argumentation process. Although some recent works on electronic meeting rooms (DeSanctis and Gallupe 1985, Kyng 1991, and Pager 1972) provide research support on group facilitation, they do not specifically address the underlying argumentation process. We develop the proposed formalisms in the following discussion.

## 3. The Representation Formalism

In this section, we develop the structure of the knowledge base underlying an argumentation process. We first develop a representation language for argumentative reasoning. Next, we develop the structure of CAP-nets, which integrate arguments expressed in this language. Finally, we develop an object-oriented architecture for CAP-net design.

## 3.1. Argument Representation Language

A cognitive agent such as an individual in a group interprets the external world in terms of entities, their attributes and relationships. An entity could be either abstract or physical. Abstract entities are generally identified as concepts, such as employee welfare. Physical entities are identified by their existence, such as a production system or the market for a given product. Attributes define the qualities of entities and have associated values. For example, an attribute such as “percentage of market share" for an entity "brand X of product Y" could have the value “20%." The relationships $\mathbf { Y } ^ { \pmb { \nu } }$ define the linkages between entities. For example, the entity “brand X" $\mathbf { X } ^ { \ast }$ is also an entity “product $\mathbf { Y } , \ "$ and the two entities are linked by an IS-A relationship. In general, the subject of an argumentation can be captured as an entity-relationship diagram, which is widely used in other applications such as database and knowledge base design. We employ the entity-relationship paradigm to describe the subject of an argumentation process. We develop the basic constructs of the representation language as follows.

Let Γ = < ∆, Λ, Ω, Σ, T) denote the subject of an argumentation process, where: ∆ is the set of all entities, Λ is the set of all entity attributes, Ω is the union of the sets of possible values of the attributes in Λ, Σ is a mapping of the attributes of each entity to their values, and T is the set of defining relationships among the entities in ∆. The claims, arguments and proposals are focused on Γ, the subject. The subject could also be viewed as a collection of beliefs of the individuals, which need not be consistent. As a result, the subject could dynamically change due to argumentation or the environment or both.

The knowledge base defining the argumentation process is the pentuple Φ =  Γ, S. P, D, Ψ), where: Λ is the subject, S is a set of statements on the subject, Pis a set of proposals for action, D is a set of data used to support statements, and Ψ is a set of arguments developed from the statements, proposals and data. We formally introduce and develop the structure of the knowledge base components in the following discussion.

In the proposed formalism, we do not specifically address the structure of the subject Γ. This is because several formalisms exist for capturing Γ (such as E-R diagrams, extended E-R diagrams, semantic nets, frames and others), and any one of them as appropriate can be used in a given situation. The structure of the other components is described as follows. A statement is a description of some part of the subject. The statements are characterized by four attributes: statement types, statement units. states of condition, and states of assertion. In this formalism, we consider statements of three types: tokens, existentials, and universals. A token is any statement in propositional logic, while an existential or universal is a statement in quantificational logic. For example, a token is a statement such as "the market share of brand X is 10%", An existential is a statement such as "there exists some brand with a market share of at least 10%", and a universal is a statement such as “the market share of every brand is less than 10%." While the proposed formalism addresses statements in propositional and quantificational logic, it is also possible to enrich its descriptive power by including other systems of logic such as modal, deontic, and belief. This is an important area for future research, since many organizational argumentation processes could employ these other forms of logic as well. The proposed formalism is a first step in this direction, and we are currently extending the formalism to these systems.

The statement units are of two types: atomic and molecular. An atomic unit is any statement that is indivisible by any logic operation. Correspondingly, a molecular unit is a compound statement that can be broken down into its atomic units. For example, the statement “the market share of brand X is 10%" is atomic, while the statement “the market share of brand X is 10% and it is also greater than that of brand Y"is molecular, Each statement is defined to be in one of two possible states of condition: unconditional and conditional. While an unconditional is a freestanding statement, a conditional is a suppositional statement. A conditional, for instance, is a statement such as “suppose that the market share of brand X is 10%."It is important to distinguish between the two states because a conditional is not necessarily supported by its proponent, while an unconditional is. Finally, each statement is defined to be in one of two possible states of assertion: unasserted and asserted. The states of assertion can be illustrated using a simple example as follows. Consider the statement "the market share of brand X is either 10% or 15%." This is a molecular unit and can be broken down into two atomic units as follows: “the market share of brand X is 10%" and "the market share of brand X is 15%."Note that while a proponent asserts the molecular unit. it is not clear whether the atomic units are asserted or not. Furthermore, it is possible to assert the molecular unit even without asserting the atomic units. For example, the proponent may be sure that the market share is either 10% or 15%. but cannot exactly pinpoint one of the two values. Hence, the molecular unit is said to be asserted. leaving the atomic units in the unasserted state. The distinction between the two states of assertion in a formal representation is important because it is necessary to distinguish between statements an individual makes and those that can be derived as their constituting elements.

In summary, a statement s ∈ S is a hextuple defined as follows: s:  t(s), u(s), c(s), a(s), <statement>>, where, t(s), u(s), c(s), a(s) and <statement) specify the type, unit, state of condition, state of assertion, and the actual contents of statement s. We now consider the other elements of the knowledge base as follows.

The sets P and D simply represent the proposals and data sets introduced in the argumentation process. The structure of the set of arguments Ψ is developed as follows. The general structure of an argument is: <argument>: <premise 〉 → 〈conclusion>, where, <premise〉 and conclusion〉 are any statements, and the symbol → represents implication. In the conventional language of logic, the <premise> and 〈conclusion〉 are known as the antecedent and consequent of an implication respectively. More formally, we define the 〈premise〉 and the <conclusion of an argument as follows.

DEFINITION 1. A 〈premise> is a statement of any type, any unit, any state of condition and any state of assertion. A premise can be an <argument> as well.

DEFINITION 2. A conclusion  is a statement of any type, any unit, unconditional and unasserted. A conclusion can be <argument> as well.

A conclusion is required to be an unconditional, as it does not make sense otherwise. A 〈conclusion > is also unasserted because the assertion, if it exists, is on the implication and not on the <conclusion >. However, if the <conclusion > is also to be asserted, then it is treated as à separate statement. A complete and formal description of the representation language using the Backus-Naur Form (BNF) (Ralston and Reilly 1993) is given below. We describe statements according to their type, unit, state of condition, and state of assertion. For simplicity, an atomic statement is indicated as an 〈A-statement> and a molecular as an <M-statement>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Axiomatic Definitions.
$\langle$entity$\rangle$::= An element of the subject domain
$\langle$entity-attribute$\rangle$::= A qualifying characteristic of an entity
$\langle$entity-relationship$\rangle$::= A linkage between two or more entities
$\langle$subject$\rangle$::= Set of $\langle$entities$\rangle$, $\langle$entity-attributes$\rangle$ and $\langle$entity-relationships$\rangle$ $\langle$token$\rangle$::= A statement on the subject in propositional logic
$\langle$existential$\rangle$::= THERE EXISTS $\langle$statement on the subject$\rangle$ $\langle$universal$\rangle$::= ALL $\langle$statement on the subject$\rangle$ $\langle$proposal$\rangle$::= Proposed action plan
$\langle$data$\rangle$::= Supporting information
$\langle$gate$\rangle$::= ∧ (and) | ∨ (or) | ∇ (exclusive or)| ≡ (equivalent)
$\langle$negate$\rangle$::= ∼ (not)$^\prime$
Structural Definitions.
$\langle$statement$\rangle$::= $\langle$token$\rangle$| $\langle$existential$\rangle$| $\langle$universal$\rangle$|
    ($\langle$token$\rangle$)| ($\langle$existential$\rangle$)| ($\langle$universal$\rangle$)
$\langle$A-statement$\rangle$::= $\langle$indivisible statement$\rangle$| $\langle$negate$\rangle$ $\langle$indivisible statement$\rangle$ $\langle$M-statement$\rangle$::=    $\langle$A-statement$\rangle$| $\langle$M-statement$\rangle$ $\langle$gate$\rangle$ $\langle$M-statement$\rangle$|
    $\langle$negate$\rangle$ $\langle$M-statement$\rangle$ $\langle$argument$\rangle$::= $\langle$M-statement$\rangle$ → $\langle$M-statement$\rangle$| $\langle$M-statement$\rangle$ → $\langle$argument$\rangle$| $\langle$argument$\rangle$ → $\langle$M-statement$\rangle$| $\langle$argument$\rangle$ → $\langle$argument$\rangle$ $⟨unconditional\rangle$::= $\langle$M-statement$\rangle$| $\langle$argument$\rangle$ $⟨conditional\rangle$::= IF $\langle$M-statement$\rangle$| IF $\langle$argument$\rangle$ $⟨asserted statement\rangle$::= ASSERT $\langle$M-statement$\rangle$|ASSERT $\langle$argument$\rangle$ $⟨unasserted statement\rangle$::= UNASSERT $\langle$M-statement$\rangle$| UNASSERT $\langle$argument$\rangle$
</div>

The above formalism addresses the basic elements of propositional and quantificational logic. This formalism can be extended to include quantifier domains in terms of possible worlds and strengths of operators (Gensler 1990). Such an extension would add the dimensions of modal logic to the current formalism and considerably enrich its representational power. These extensions are beyond our current scope but are important and significant avenues for future research.

## 3.2. Structure of CAP-Nets

A CAP-net is a unified network representation of the arguments introduced by the individuals in a group. The various statements, proposals, and data from the individuals are expressed in the representation language and integrated into a network. The structure of a CAP-net is developed as follows. First, we introduce the basic constructs of the network. Second, we develop the circuitry of the network and show how a logical sequence of arguments can be represented as a network. Third, we develop the component-structure of the network. Fourth, we develop an object-oriented architecture for CAP-nets and discuss their management issues. Finally, we illustrate the proposed architecture using a comprehensive example.

3.2.1. Network Elements. The structure of CAP-nets is analogous to that of electrical circuits. An electrical circuit is basically composed of devices and gates connected according to a specified logic. Each gate has a set of inputs and outputs, and a current flows through the circuit elements and links. This flow is altered by the logic of the gates. Further, a circuit has an initial set of inputs, and a final set of outputs. In an analogous fashion, we define the structure of a CAP-net as follows. A CAP-net is composed of statements, proposals, data and gates connected into a circuit. Note that <negate〉 in our BNF formalism is also a type of gate which directly produces the negation of a given statement. The net is defined as a directed graph $G = \{ V , A \}$ where V is the set of nodes and A is the set of arcs. An arc from node v1 to node v2 ${ \pmb v } _ { 1 }$ $v _ { 2 }$ is denoted as $( v _ { 1 } , v _ { 2 } )$ . The arc $( v _ { 1 } , v _ { 2 } )$ is called an input arc of ${ \mathfrak { v } } _ { 2 }$ and an output arc of ${ \pmb v } _ { 1 }$ Correspondingly, v, is called the input node and v2 the output node of arc $v _ { 1 }$ ${ \mathfrak { v } } _ { 2 }$ $( v _ { 1 } , v _ { 2 } )$ Note that each arc connects exactly two nodes. The nodes contain information, and are classified into six types based on their content as follows: UA (unconditional A-statement) CA (conditional A-statement), AR (argument point), GT (gate), PR (proposal) and DA (data). Let UA, CA, AR, GT, PR and DA denote the sets of corresponding nodes. Therefore, V is the union of these sets of nodes. The UA, CA, PR and DA nodes contain specific information provided by the individuals in a group. Each GT node contains one of the logic operators, and an AR node contains the implication operator. In addition, the net also includes transmitter nodes, which are simple circuit connections transmitting their inputs to all their output nodes. The symbolic representation of the nodes is shown in Figure 2.

Consider any arc $( v _ { 1 } , v _ { 2 } )$ . The output of node $v _ { 1 }$ is said to flow through this arc into $\pmb { v _ { 2 } } , \pmb { \mathrm { I f } } \ \pmb { v _ { 1 } }$ is one of {UA, CA, PR, DA }, then the information contained in it flows through this arc. $\mathbf { I f } \ v _ { \mathbf { I } }$ is either a GT or AR node, then the output of the corresponding logic operation flows through this arc. These flows constitute the issues in argumentation. Each flow is qualified on its state of assertion. When individuals make statements, it is not necessary that they should be atomic. A molecular statement is parsed into its atomic elements, which are stored in a CAP-net as nodes. The circuitry among these nodes captures the logic of the molecular statement, which is the output flow from the circuit. We illustrate this composition process using a simple example in the following discussion.

![](/api/attachments/6X86RDY6/fulltext/images/d366a44570c5b18e1633ed7329829e55ca57750f0ecd1294299123d1a214203f.jpg)

![](/api/attachments/6X86RDY6/fulltext/images/6e90da40b49fdc74492390c082d5529884ae7dbf6996bb661fe7811996af94b2.jpg)

![](/api/attachments/6X86RDY6/fulltext/images/4e3f9fd93841d123cd633314dc4f8020f157eb99aa975ec0d0fd26ee9100ed75.jpg)

![](/api/attachments/6X86RDY6/fulltext/images/ffe641ab786800f0cd337cf77702f3e439fd5f7049942c5dab7adeaa4e532958.jpg)

![](/api/attachments/6X86RDY6/fulltext/images/a146dbabab36565d7ec515f90014ee0f5c7d8c97a7fc285167065a865de25cbe.jpg)

![](/api/attachments/6X86RDY6/fulltext/images/9925eaec4239b0a0f9255a1b5b594380ae6206ac69b6fef172153062b48cc46b.jpg)

![](/api/attachments/6X86RDY6/fulltext/images/18400a28c0ef5db73dc799b9ef2880efd8a651694a31b157b29de6d3aed5e053.jpg)

![](/api/attachments/6X86RDY6/fulltext/images/01564dca2243285fd2b6fda3d34995d96046bcf1e89ef754644c5ca2b6be892c.jpg)  
FIGURE 2. Architecture of the Elements of a CAP-Net.

3.2.2. Network Circuitry.Consider the following statements in an argumentation process.

(a) 50% of the users of a leading brand M of a product do not view the brand favorably anymore.

(b) The above fact implies that either better products have arrived at the market or that the users' expectations of the product have increased.

![](/api/attachments/6X86RDY6/fulltext/images/0e835d11678b170ebc099c98c7870a4492a836a782550ad792c931ea6c79256c.jpg)  
FIGURE 3. Integrating Arguments into a CAP-Net.

(c) If better products have arrived, then the market for brand M should show a declining trend.

(d) No perceptible decline in the market for brand M has been observed.

(e) Therefore, we conclude that the users' expectations of the product have increased.

Let us analyze the above arguments. Statement (a) is atomic and is denoted as A1. Statement (b) is an argument and is denoted as A1 → (A2 V A3), where A2 and A3 are the atomic components of the molecular consequent of the argument. Statement (c) is also an argument, and is denoted as A2 → A4, where A4 is its consequent. Statement (d) is atomic, and is simply\~ A4. Statement (e) is the final conclusion derived from statements (a)-(d). This argument is denoted as: {(A1) ∧ (A1 → (A2 ∨ A3)) ∧ (A42 → A4) ∧ (\~ A4) } → A3. The CAP-net circuitry of the above set of arguments consists of the four UA-statements A1, A2, A3 and\~ A4, and the logic derived from them according to the statements (a)-(e). The CAP-net is illustrated in Figure 3. We now derive the states of assertion of the flows along the arcs of the network as follows.

A statement is said to be asserted by its proponent if he accepts it to be true. Note that in making a series of statements as above, assertions are made explicitly as well as implicitly. Every complete statement made by an individual is said to be explicitly asserted. For example, each statement (a)-(e) is explicitly asserted. An explicitly asserted statement can be one of the following: <M-statement>, <argument>, <proposal >, <data 〉. The implicit assertions of an individual are contained in the explicit assertions he makes and can be determined from the logic contained in a coherent set of explicit assertions as in statements (a)-(e). The CAP-net circuitry links the explicit assertions into a coherent argument of an individual and provides mechanisms to identify the implicit assertions from its network structure. This determination is carried out as follows.

Note that every arc originates from one of the following nodes: M-statement > (gate>, <argument〉, 〈proposal>, <data〉. First, all flows representing explicit assertions are asserted. The remaining arcs could originate from nodes representing either 〈M-statement〉 or (gate> or <argument>. The following rules are used in determining their states of assertion.

(i) The output of an AND (∧) gate is asserted if all its inputs are already asserted.

(ii) Converse to (i), the inputs of an AND (∧) gate are all asserted if its output is already asserted.

(iii) The output of an OR (V) gate is asserted only if at least one ot its inputs is already asserted.

(iv) The output of an exclusive OR (∇) gate is asserted only if exactly one of its inputs is already asserted, and not the rest

(v) If a flow is asserted, then its negation is not asserted, and vice versa.

(vi) The output of an equivalent (=) gate is always unasserted, unless it is explicitly asserted by an individual.

(vii) If the output and one of the inputs of an equivalent (=) gate are asserted, then its other input is also asserted.

(viii) The output of an argument node is always unasserted, unless it is explicitly asserted by an individual.

(ix) If the output and the antecedent of an argument node are asserted, then the consequent is also asserted.

While the rules (i)-(vi) are fairly self-evident, rules (vii)–(ix) require explanation. Consider rule (vii) and some equivalence statement $p \equiv q .$ . Assume that an individual explicitly asserts that p = q and that p is true, but does not indicate anything on the truth or falsity of q. However, he implicitly believes that q is true, since he believes p $\pmb q .$ and p = q to be true. Logically, this implication can be stated as: $( p \land ( p \equiv q ) \to q )$ Rule (vii) provides an easy way of determining this from the CAP-net. Rule (viii) requires that every argument should be explicitly asserted, since they are claims made by an individual. This is similar to rule (vi) where an explicit assertion is required of an equivalence claim as well. Now, consider rule (ix) and some argument ${ p  q } .$ Assume that an individual explicitly asserts that p → q and that p is true but does not $\mathbfcal { p }$ indicate anything about q. However, his belief in the truth of q is implicit from his ${ \pmb q } .$ $\pmb q$ argument, since his explicit statements can be logically combined into (p ∧ (p → q) → q), yielding his implicit assertion of q from the assertions on p and ${ p  q } .$ We illustrate the above process of determining the assertion states using the CAP-net in Figure 3 as follows.

The explicit assertions of the proponent in this example are: (a) A1, (b) A1 → (A2 ∨ A3), (c) A2 → A4, (d) \~ A4, and (e) {(A1) ∧ (A1 → (A2 √ A3)) ∧ (A2 → A4) ∧ (\~A4)} → A3. From (a) and (d), we assert the flows A1 and \~ A4 in the

CAP-net. Consider statement (b). Since this argument and its antecedent (which is A1) are both explicitly asserted, the implicit assertion of its consequent (A2 V A3) is derived from applving rule (ix). Consider statement (c). While this argument is explicitly asserted, its antecedent (which is A2) is not. Therefore, we can not deduce the assertion of its consequent (which is A4), and is left as unasserted. Consider statement (e). In this case, the main argument of (e) is explicitly asserted. Further, the antecedent of this argument is implicitly asserted because it is an AND (∧) of four statements that are all explicitly asserted (from (a)-(d)), and applying rule (i), the implicit assertion follows. As a result, we find that the consequent of (e), which is A3, is also implicitly asserted from applying rule (ix). The states of assertion thus determined are shown in Figure 3. The assertion of A3 can also be seen intuitively from examining statements (a)-(e) of the proponent, who concludes his logic with A3 as his final claim.

After determining the assertion states as above, the remaining arcs, if any, are indicated as unasserted. Note that argumentation centers on assertions. The above scheme provides a mechanism to identify statements that are subject to argumentation. In argument logic, it is important to recognize that an individual could use certain statements without asserting them in formulating his arguments. Similarly, certain statements could be implicitly asserted because of other explicitly stated assertions. The identification of both the implicit and explicit assertions in a network is important to the gaming and coordination of argumentation processes.

3.2.3. Network Components.Every argument has two principal components: a theorem component and a proof component. A theorem component is a logical development of an assertion from other statements made by an individual. For example, the network shown in Figure 3 is the theorem component of an argument terminating in the final claim. Extending this definition to each argument in the network, it can be seen that every asserted argument has a theorem component. The theorem component of an argument is the subnetwork comprising of all nodes and arcs that lead to the arc denoting the argument. Therefore, a node belongs to the theorem component of an argument if there is a directed path from the node to the argument. More formally, $T ( v _ { 1 } , v _ { 2 } ) \subseteq G$ is the theorem component of an argument along arc $( v _ { 1 } , v _ { 2 } )$ if:

(i) $T ( v _ { 1 } , v _ { 2 } )$ is connected,

(ii) for every node $u \in T ( v _ { 1 } , v _ { 2 } )$ , there exists a directed path from u to ${ \mathfrak { v } } _ { 1 } .$ , and (iii) there does not exist a node $u \in G \setminus T ( v _ { 1 } , v _ { 2 } )$ from which a directed path to $v _ { 1 }$ exists in G.

The above definition implies that a theorem component is maximal, in the sense that no proper subset of $T ( v _ { 1 } , v _ { 2 } )$ can fully describe the logical development of an argument. and any node not included in $T ( v _ { 1 } , v _ { 2 } )$ is not necessary for the argument.

While the theorem component of an argument shows how the claim of the argument is arrived at, it need not be supported by all the individuals in a group. There $\mathbf { a t } ,$ could exist individuals who would challenge either the argument, or the way it is arrived at, or both. Consequently, the proponent of an argument may have to produce additional logic and/or data to defend the claim. The component of the network that is used to defend a claim is termed its proof component. For example, consider the theorem component in Figure 3. Assume that an individual challenges the final assertion. In defense, the proponent could produce the following lines of reasoning:

![](/api/attachments/6X86RDY6/fulltext/images/fe74d7d2c93e614de6eeaa6d9cc27b9d84375b35139ac5c369bf1255ea4a7bf7.jpg)  
FIGURE 4. Theorem and Proof Components of the CAP-Net in Figure 3.

(f) Assume that the users' expectations of the product have not increased.

(g) Therefore, better products should have arrived at the market (from statements (a), (b), and (f)).

(h) Therefore, the market for brand M should show a declining trend (from statements (c) and (g)). This contradicts statement (d). Hence, statement (f) cannot be correct.

Let us analyze these statements. Statement (f) is atomic and is conditional. Further, this statement is the negation of statement (e). Hence, statement (f) is denoted as \~ A3. Statement (g) is an argument derived from (a), (b) and (f), and is denoted as $\{ ( A 1 ) \land ( A 1 \to ( A 2 \lor A 3 ) ) \land ( \sim A 3 ) \} \to A 2$ . Statement (h) is an argument derived from (c) and (g) and is denoted as $\{ ( A 2  A 4 ) \land \{ \{ ( A 1 ) \land ( A 1  ( A 2 $ $\vee A 3 ) ) \wedge ( \sim A 3 ) \}  A 2 \}  A 4 \}$ . Statement (h) contradicts statement (d), thus invalidating the conditional (f). The above line of reasoning constitutes a proof by contradiction, and the proof component is illustrated in Figure 4. The contradiction is shown as a null node at the end of the proof component. Apart from proofs by contradiction, other proof mechanisms such as direct proofs and conditional proofs (Gensler 1990) are also possible in practical argumentation. Since every proof mechanism is an argument by itself, they can be represented using the same network constructs. A contradiction proof ends in a null node, while other proofs would end in the original argument being defended.

The proof components are of several types. For example, a claim can be defended by logically combining the statements in the theorem component as in the above illustration. We term such a proof as a basic logic proof. However in some cases, a proponent may make certain new claims (which could be subject to further argumentation) in addition to those contained in the theorem component in deriving a proof. We term such a proof as an extended logic proof. If a basic logic proof is sound and all the subclaims contained in a theorem component are accepted by the challenger, then argumentation clearly terminates. However, argumentation could recursively move into the subclaims if they are not accepted, even though the proof may be sound. An extended logic proof could clearly give rise to further argumentation, because of the new assertions introduced. In cases where a logic proof is not possible, a proponent may produce data as evidence in support of a claim. We term such proofs as empirical proofs. Finally, a proponent could employ a combination of logic and empirical elements in defending a claim. Such proofs are termed as hybrid proofs. The empirical and hybrid proofs could also give rise to further argumentation. The interaction dynamics in these cases are modelled in the subsequent sections.

The proof component of an argument $( v _ { 1 } , v _ { 2 } )$ is denoted as $P ( v _ { 1 } , v _ { 2 } )$ . Together, the two components support a claim. In general, the theorem component of an argument initiates argumentation, leading to the development of the proof component through the argument game. The termination of the game is the resolution of the argument, which could be favorable or unfavorable to the proponent.

3.2.4. Network Design.The object-oriented paradigm lends nicely to the design and implementation of CAP-nets. Using this paradigm, the nodes can be represented as objects and the arcs as links between the objects. The storage of information is quite simple in this architecture, since it is restricted only to the nodes of a CAP-net. Any complex statement contained in a CAP-net can be produced efficiently by retrieving a sequence of objects and concatenating them into the statement logic. The proposed design of the object base is as follows.

CAP\_NET: SET OF {A\_NODE, PR\_NODE, DA\_NODE, GT\_NODE, AR\_NODE}

A\_NODE: RECORD OF {NID: integer, CONTENT: string, CONDITION: condition\_state, ASSERT: assert\_state, OUTARCS: arc\_set }

GT\_NODE: RECORD OF {NID: integer, GATE: gate\_type, ASSERT: assert\_state, INARCS: arc\_set, OUTARCS: arc\_set }

AR\_NODE: RECORD OF {NID: integer, ANTE: arc\_set, CONS: arc\_set, AS-SERT: assert\_state, OUTARCS: arc\_set }

PR\_NODE: RECORD OF {NID: integer, CONTENT: string, ASSERT: assert\_state, OUTARCS: arc\_set}

DA\_NODE: RECORD OF {NID: integer, CONTENT: string, ASSERT: assert\_state, OUTARCS: arc\_set }

condition\_state: MEMBER OF {CA, UA }

assert\_state: MEMBER OF {A, U}

gate\_type: MEMBER OF {\~, ∧, √, ∇, ≡}

arc\_set: SET OF {arc\_\_type }

arc\_type: RECORD OF {NID: integer, COMPONENT: component\_type, PROOF\_NODE: proof\_point}

component\_type: MEMBER OF {T, P} proof\_point: MEMBER OF {∅, set of NID in object base }

Most of the definitions in the object base are self-explanatory. Each object captures four types of information: node content, states of assertion/condition, pointers to input, and output objects. These pointers record the arcs in the network. The attribute NID is the node identifier. The object type “arc\_set" defines the input and output arcs of a node as follows. The NID points to the input or output object as appropriate. The object "componenttype" specifies whether the arc belongs to a theorem or proof component. The attribute PROOF\_NODE is set to null (∅) if the arc belongs to a theorem component. Otherwise, PROOF\_NODE points to the objects in whose proof components the arc belongs. As a result, it is possible to retrieve selectively any theorem or proof component in the network by following this attribute in accessing objects. Several integrity checks on this object base are possible. For example, the INARCS and OUTARCS of a GT\_NODE or AR.\_NODE should be nonempty. The rules for assertion states developed earlier provide additional integrity checks. Using the logical properties of the network, it is possible to devise several more such checks. We illustrate the proposed design by defining the objects of the network shown in Figure 3 as follows. This network is a theorem component and has 4 A-statements, 3 gates and 3 arguments. The transmitter nodes are used only for diagrammatic illustration, and need not be stored explicitly as objects. For the sake of clarity, let the object identifiers be {1, 2, 3, 4 } for A\_NODE, $\{ a , b , c \}$ for GT\_NODE and $\left\{ \alpha , \beta , \right.$ $\pmb { \gamma } \}$ for AR\_NODE objects.

The node identifiers are indicated in Figure 3 as well. The object base for this network is:

A\_NODE Objects

$$
\bullet \{1, \{* \}, U, A, \{\{\alpha , T, \emptyset \}, \{c, T, \emptyset \} \} \}
$$

$$
\left. \bullet \{2, \{* \}, U, U, \{\{\beta , T, \emptyset \}, \{a, T, \emptyset \} \} \right\}
$$

$$
\bullet \{3, \{* \}, U, A, \{\{\gamma , T, \emptyset \}, \{a, T, \emptyset \} \} \}
$$

$$
\bullet \{4, \{* \}, U, U, \{\{\beta , T, \emptyset \}, \{b, T, \emptyset \} \} \}
$$

where { } indicates the node content.

GT\_NODE objects

$$
\bullet \{c, \wedge , A, \{\{1, T, \emptyset \}, \{\alpha , T, \emptyset \}, \{\beta , T, \emptyset \}, \{b, T, \emptyset \} \}, \{\gamma , T, \emptyset \} \}
$$

AR\_NODE Objects

$$
\bullet \{\beta , \{2, T, \varnothing \}, \{4, T, \varnothing \}, A, \{c, T, \varnothing \} \}
$$

$$
\bullet \{\gamma , \{c, T, \emptyset \}, \{3, T, \emptyset \}, A, \{E, T, \emptyset \} \}
$$

Now, consider a query on the above object base as follows: Retrieve the theorem component leading to statement α. In processing this query, the object α is retrieved first. This is an AR\_NODE object. By backtracking from this object, the objects 1 and a are retrieved. Object 1 is an A\_NODE, while object a is a GT\_NODE. By backtracking from object a, the A\_NODE objects 2 and 3 are retrieved. Then, by combining the objects according to their logic, we find that the theorem component is $A 1  ( A 2 \lor A 3 )$ . The above design leads to several opportunities for access path optimization in query processing. The development of such access aids is an interesting and useful avenue for future research. The management of the above object base is fairly simple. When new logic is added to a CAP-net, the appropriate objects are created using the object definitions and added to the object base. Similarly, the deletion of logic components corresponds to the deletion of objects, and changes result in object modifications. In all these update procedures, it is necessary to maintain the integrity of the objects, continuity of the network and the logical consistency of the object base. Design of these procedures is an important area for future research, and we are currently developing them for our prototype model.

## 3.3. Putting It All Together

Putting all the above developments together, we illustrate the overall structure of CAP-nets using a complete argumentative discussion as follows. Assume that a group of top executives are engaged in a discussion on product line expansion. Let the issue currently facing the group be: Should we expand our line to enter market X?Let some of the executives advocate the expansion and the rest be either unsure or opposed to the idea. We denote the advocates as the “proponents," and combine all the rest as the “opponents."This grouping is rather ad hoc and is introduced only for purposes of clarity. This is because the individuals can dynamically change their positions, and anvone can introduce arguments both in favor of as well as against certain proposals. Consider the following line of reasoning introduced by the proponents:

Market studies by Surveys, Inc., show that 60% of the market for product X is controlled by brand M, produced by the market leader. The same study indicates that all other manufacturers of product X are really small, and each of these brands commands less than 5% of the market. Further, recent investigations of consumer attitude towards product X by the same market research firm indicate that at least 50% of the users of brand M are dissatisfied with the product and are willing to switch to a better brand but are unable to do so because all other existing brands are perceived to be even inferior to brand M. Consequently, at least 30% of the market for product X is for grabs. We suggest entering the market, and here are our detailed plans for production, marketing, distribution, and pricing. The plans include annual outlays in each function over the next five years. The proposed plan with a pricing policy of p dollars will capture at least 30% of the market at the end of the third year, and the annual profits will be $q _ { 1 } , \ldots , q _ { s }$ over the next five years.

The opponents, while accepting the facts of the surveys, do not agree with the line of reasoning and the final conclusions of the proponents. They develop the following line of counterreasoning:

Note that the survey also indicates that there are no visible barriers to entry into this market for our perceived potential competitors. Given the high market share of brand M. the low profile of other manufacturers and the substantial dissatisfaction among the users of brand M. we conclude that the market is potentially attractive to any manufacturer with adequate resources. Coupled with the lack of entry barriers, we conclude that our competitors definitely will be attracted to this market, regardless of whether we enter or not. Consequently, the projected market share of at least 30% is clearly not possible. In fact, it could be much less.

Our production units are growing old, and consequently the production costs are going up. Hence, if we choose to enter this market, we should either upgrade our machinery or subcontract part of the work. Further, introducing a new product means retraining some of the workers. All of these imply additional costs that are not considered in your proposal. Your projected outlay in this project is, therefore, grossly inadequate. Hence, at the suggested pricing policy, it is not possible to achieve the claimed profits.

The protocol of the proponents is organized into the following nodes:

A1: Market studies by Surveys, Inc. show that 60% of the market for product X use brand M, produced by the market leader

A2: The same study indicates that the market share of every other brand is less than 5%, and these producers are really small manufacturers.

A3: The same study also shows that at least 50% of the users of brand M are dissatisfied with the product, and are willing to switch if a better product is available.

A4: It is possible to capture at least 30% of the market for product X.

P1: Proposed plans, outlays, and pricing structures.

A5: The proposed strategy will capture at least 30% of the market in three vears and yield profits $q _ { 1 } , \ldots , q _ { s }$ over the next five years.

Now, the protocol of the opponents is organized into the following nodes.

A6: The survey also indicates that there are no visible barriers to entry into this market for our potential competitors.

A7: The market is potentially attractive to any manufacturer with adequate resources.

A8: Competitors will definitely be attracted to this market, regardless of whether we enter or not.

A9: Consequently, the projected market share of at least 30% is not possible. In fact. due to the attractiveness of the market, it will be much less.

A10: Production costs are continually going up, because our machinery is getting old.

A11: Consequently, we should either upgrade our machinery or subcontract part of the work.

A12: Introducing a new product implies retraining some of the workers.

A13: This implies additional costs not considered in the proposal.

A14: Projected outlay is inadequate

A15: At the suggested pricing structure, it is not possible to achieve the claimed profits.

The logical organization of the above protocols using the atomic statements and the proposal is as follows.

Proponents' logic

M1: $\{ ( A 1 \land A 2 \land A 3 )  A 4 \}$ 0

M2: $\{ ( M 1 \land P 1 )  A 5 \}$

Opponents' logic

M3: $\{ ( A 1 \land A 2 \land A 3 )  A 7 \}$

M4: $\{ ( M 3 \land A 6 )  A 8 \}$

M5: {M4 → A9 }

M6: {A10 → A11}

M7: {(M6 ∧ A12) → A13}

M8 {(M7 ∧ P1) → A14}

The molecular statements are indicated as M1-M9 in the above list. A CAP-net structure of the above arguments is shown in Figure 5. The object base for this net contains 15 A NODE. 6 GT\_NODE, 9 ARNODE and 1 PRNODE objects. Note that this integrated object base contains arguments from the proponents and the opponents as well. In order to differentiate between the two sets of arguments, we introduce the concept of object ownership. An individual is said to own the objects that he subscribes to. The objects owned by an individual are said to constitute his object set. To illustrate, let the objects be assigned identifiers 1-31, with 1-15 for A NODE, 16–21 for GT\_NODE, 22-30 for AR\_NODE and 31 for PR\_NODE objects. These identifiers are shown in Figure 5. The object set of the proponents is {1–5, 16, 17, 23, 31 }, and that of the opponents is {1-3, 6–16, 18–21, 24–-30 } . Note that an object can be owned by several individual while an individual can own several objects. This concept can be extended to each individual separately in a group. This assignment enables the selective retrieval of arguments provided or subscribed to by an individual. This retrieval can be carried out easily by testing the objects pointed to by a currently retrieved object for membership in the concerned individual's object set. This selective retrieval is important in scheduling the argument games, which is discussed in the following section.

## 4. The Gaming Formalism

The argumentation process is viewed as a game between the proponent of a claim and its opponent in the spirit of the Lorenzen model. The focal point of an argument game is an asserted statement and is either accepted or rejected by both the individuals at termination. We do not consider stalemate conditions, as any stalemate will either have to be finally resolved or decisions have to be made with only partial support from the group in practical situations. We address some of these issues in the discussion on resolution. The argument game model is as follows. Consider some assertion by an individual, stored in the CAP-net. Assume that another individual questions the validity of this assertion. In response, the proponent could possess several strategies for defending his assertion. Each defense strategy contains an alternate line of reasoning supporting the assertion. These strategies are termed proof paths, and each proof path provides a proof component of the assertion in question. Assume that the proponent selects one of the proof paths and presents its proof component. The proof component itself could contain certain new assertions, which could be questioned as well. Thus, the presentation of a proof path could take the proponent into an inner loop, and the process continues recursively. We term this process the recursive inner proof. At any stage of the recursive inner proof process, the following distinct outcomes are possible.

(1) The proponents may be able to successfully establish all his claims. In this case. he has succeeded in establishing his original assertion which started the argument.

(2) Some claim of the proponent in an inner proof may be challenged by the opponent. In this case, the proponent may choose one of the following paths:

(i) He may decide to continue the recursive proof process, starting from a claim currently challenged.

(ii) He may accept the inability to defend the claims currently challenged. In this case, the proof path chosen by him has failed. Consequently he may choose one of the following alternatives available to him:

(a) He may choose an entirely different proof path, and start a new line of reasoning about his original assertion.

(b) He may accept his inability to defend his original claim. In this case, the argument terminates with disproving the original claim. 7

The proof or disproof of a claim simply means that either the opponent or the proponent accepts the other in the present context. In the presence of uncertainty and empirically oriented proof paths, it is impossible to determine the absolute truth or falsity of a claim. This is usually the case in many organizational decisions. There are two clear advantages to our position on this. First, it mirrors reality, and second, it affords a way of altering the true/false status of a claim dynamically, as the acceptance/rejection of a claim might change over time. This dynamic change is a result of the nonmonotonic nature of the beliefs of the individuals. This is a significant departure from the traditional logic considered in the argument theory literature, where knowledge is monotonic, and established claims remain true forever.

The above argument game is quite similar to a search process. We develop the structure of the game under different proof strategies in the following discussion

## 4.1. Logic Proofs

Logic proofs are common in many argument games. Such games are often played even in daily life, where people argue about their beliefs when questioned. Such arguments arise in a variety of circumstances, ranging from a simple encounter between two individuals to organized committee discussions. In all these cases, a common proof strategy is as follows. Assume that an individual goes about making assertions, while the others need not necessarily concur with them. When another individual raises his disagreement, the proposing individual attempts to defend his position using logical reasoning at first. In this process, he could draw from common techniques such as simple linear reasoning, suppositional reasoning, reasoning by contradictions, instantiations and transformations, demonstrations in analogous systems, and a host of other techniques. Hence, logic proofs constitute the core of many argument games, which could lead to empirical proofs if the logic proofs are not sustainable. We first focus on logic proofs in the following discussion.

Logic proofs can be either basic or extended. If the basic proof is sound, then it should be acceptable to the challenger, unless he claims that the proponent has overlooked certain facts which could alter the acceptability of the contended assertion. In this case, the basic proof becomes an extended proof, and the game continues. An extended proof path could lead to a recursive inner proof process. We illustrate this as follows. Consider a statement {(A1 ∧ A2) ∧ ((A1 ∧ A2) → A3) } by a proponent. Assume that an opponent disagrees with the implication, while agreeing with (A1 ∧ A2). Assume that the proponent has the following alternative extended logic proof paths:

Path 1: {(A1 ∧ A2) ∧ {(A1 ∧ A2) → A4} ∧ (A4 → A3)} → A3 Path 2: {(A1 ∧ A2) ∧ {(A1 ∧ (\~A3)) → A5 } ∧ {A5 → (\~ A2)} → A3.

Clearly, both the paths are extended logic. Assume that Path 1 is initially presented in defense. As a result, the opponent could react in one of the following possible ways:

(i) accept the proof, (ii) challenge (A1 ∧ A2) → A4, (iii) challenge $A 4  A 3 ,$ (iv) challenge both. If the opponent challenges, then the proponent should react in one of the following possible ways: (a) accept his original assertion as false, (b) proceed to defend the attacked assertions in the proof path by developing further logic, and (c) give up the proof path, and choose the other path for argument.

If the proponent accepts his original assertion as false, then the argument is terminated. If he chooses (b), then he should proceed with defending all the attacked assertions in the proof path, Otherwise, the path fails. In this case, he may have several proof paths to defend the attacked assertions. Although separate proof paths might exist for subsets of these assertions, we combine them into a set of proof paths, where each path addresses all the attacked assertions. This consolidation is done mainly for clarity of exposition, and proof paths for subsets can be incorporated easily in this framework. In either (b) or (c), the proponent would introduce additional logic, which is subiect to attack by the opponent. This dialogical game continues recursively, until either the proponent or the opponent succeeds.

The recursive inner proofs constructed by the dialogical game can be structured as a directed tree. Let T' denote a rooted directed tree, where each node represents a set of assertions of the proponent that are attacked by the opponent, and each arc represents a proof path. The root represents the original assertion from the CAP-net that started the argument. The tree is ordered into levels, with the root at level 1 and the levels numbered in a top-down manner. For example, two nodes, u and v, occur at level i, if their respective parents occur at level $( i - 1 )$ . The direction of the arcs is oriented top-down, and points from parents to siblings. The nodes and arcs are denoted as follows. Let $\pmb { A } _ { k } ^ { i }$ denote the kth node at level i. Let $P _ { j } ( A _ { k } ^ { i } )$ denote the jth proof path developed to defend $\pmb { A } _ { k } ^ { i }$ . The arc $P _ { j } ( A _ { k } ^ { i } )$ would terminate in one of three possible siblings of $A _ { k } ^ { i } { : } ( \mathbf { i } )$ a node $A _ { k ^ { \prime } } ^ { i + 1 }$ , which represents a set of assertions in $P _ { j } ( A _ { k } ^ { i } )$ that are attacked by the opponent, and to which the proponent chooses to respond in his next move, (ii) a null-by-opponent node $\phi _ { o } ,$ ,which implies that the opponent has accepted the proponent's claims, and (iii) a null-by-proponent node $\phi _ { p } ,$ which implies that the proponent has abandoned the current chain of proof paths form the root because of his inability to defend the attacks on the claims made in $P _ { j } ( A _ { k } ^ { i } )$

The recursive inner proof tree is constructed dynamically as the dialogical game proceeds. Note that each arc actually represents a proof component derived for the proof path. Thus, the recursive inner proof tree can be considered a meta net comprising proof components and contentional assertions. The tree can be constructed in different ways, and it depends on the proponent's decision when the opponent attacks a claim. For instance, if he decides to abandon the current chain of proof paths, he can backtrack $l ( \geq 1 )$ levels up and start a new process of proof construction. However, the maximum he can backtrack is up to the root level, at which point he should decide whether to give up his original claim altogether, or start a new line of proof. We summarize this generalized strategy in the algorithm presented in a pseudocode form in Appendix A.

The actual storage of the proof components follows the object base architecture developed earlier. The objects belonging to the proof components represented by the nodes of the inner proof tree are owned by the proponent and are identified accordingly in the object base. Each node of the inner proof tree simply contains a pointer to the assertion object for which a proof path is currently being pursued. The recursive exploration of proofs follows a depth-first extension. Consequently, it is necessary to maintain only one chain of the tree from the root leading to the current node in consideration at any time. When such a chain of proof paths is defended successfully, the objects of this chain together constitute a proof component for the original claim. Whenever a proof path fails, its objects can be discarded, as the proponent could choose an alternate line of defense. If the proponent fails to establish his claim and accepts failure at the end of the game, the original assertion object is undefended and has no proof component. Consequently, the proponent would give up his ownership of that object. Thus, the inner proof tree is simply a recursive mechanism to order and guide the interactions during an argument game using logic proof paths.

## 4.2. Empirical Proofs

Empirical demonstrations of stated claims are also used quite often in practical argumentation. Empirical proof strategies usually do not move into recursive inner stages as logic proofs, unless they are combined with some logic proof path in a hybrid manner. In the case of purely empirical proofs, the proponent of a claim could provide alternate or equivalent statements of the claim which can be verified empirically. In this case, each alternate statement is an empirical proof path, and the proponent could choose to test them in some sequence until either some proof path succeeds or he accepts failure at some stage. The data supporting an empirically defended claim is its proof component and is added as a data object to the CAP-net. We illustrate this process using an example as follows. Assume that the proponent makes an assertion $( A \land B ) \to C ,$ , where A, B and C are statements about a population Ω. Let $x \in \mathfrak { a }$ be an instance of the population, and $\pmb { A } ( \pmb { x } ) , \pmb { B } ( \pmb { x } )$ and $C ( x )$ be the statements applied to the instance x. For example, if Ω is the population of users of product $\mathbf { X } , \mathbf { A } { \mathrm { : } }$ {uses brand M }, B: { dilssatisfied with brand M } and C: { willing to switch }, then $( A \land B ) $ C is an assertion about users of brand M who are dissatisfied with it. Clearly, this claim is empirically based and can be accepted only within a certain degree of statistical error. If an opponent challenges this claim, then its validity can be shown using samples from the population. Thus, the proof mechanism involves sampling and statistical analysis. Assume a random sample of $\omega \in \Omega$ individuals is used to verify this claim and that the sample size is statistically appropriate. The proponent could use à variety of proof paths derived from this sample and possibly, further samples, and we show four of them here:

Path 1: $\left\{ A ( x ) \wedge B ( x ) \wedge C ( x ) \right\} \forall x \in \psi _ { 1 } , \psi _ { 1 } \subseteq \omega , | \psi _ { 1 } | \geq m _ { 1 } | \omega | .$

Path 2: $\{ A ( x ) \wedge \sim C ( x )  \sim B ( x ) \} \forall x \in \psi _ { 2 } , \psi _ { 2 } \subseteq \omega , | \psi _ { 2 } | \geq m _ { 2 } | \omega | .$

Path 3: $\{ B ( x ) \wedge \sim C ( x )  \sim A ( x ) \} \forall x \in \psi _ { 3 } , \psi _ { 3 } \subseteq \omega , | \psi _ { 3 } | \geq m _ { 3 } | \omega |$

$$
\text { Path   4: } \{\sim C (x) \rightarrow \sim A (x) \vee \sim B (x) \} \forall x \in \psi_ {4}, \psi_ {4} \subseteq \omega , | \psi_ {4} | \geq m _ {4} | \omega |.
$$

Proof path 1 is a direct proof mechanism using instantiations of the original assertion. Paths $2 , 3 ,$ , and 4 employ instantiated contradictions. The parameters $m _ { 1 } , m _ { 2 } ,$ $m _ { 3 } ,$ and $\pmb { m _ { 4 } }$ are proportions of sample size and are based on the statistical levels of significance acceptable to the opponent. In fact, the proof paths provide statistical hypotheses that are equivalent to the original claim and are only subject to the acceptability by the opponent. Since the validity of a claim is only subject to the acceptance by an opponent, exploring alternate proof mechanisms is meaningful in the present context.

The empirical proof game proceeds as follows. Assume that the proponent decides to test his claims using paths 1-4 in that order. Initially, the assertion of path 1 is tested using a sample. Let ${ \pmb { \alpha } } _ { \bf 1 }$ be the proportion of the sample that tests positively with respect to the assertion of path 1. If $\pmb { \alpha } _ { 1 } ^ { \prime } \geq m _ { 1 }$ , then the proponent has succeeded empirically in establishing his claim. Otherwise, the proponent could either accept his statement as false and proceed with the next proof path available. This process continues until either the claim is established empirically or all the proof paths are exhausted with the proponent unable to defend the claim successfully. The empirical proof game can be modelled as a stochastic dynamic programming problem when we take into account the costs of empirical proofs and the outcome of the game. The dynamic programming model is presented in Appendix B.

## 4.3. Hybrid Proofs

Hybrid proof strategies incorporate the features of both logic and empirical proofs. For example, consider the logic proof path 1 discussed earlier. Assume that the proponent chooses this line of defense. In this path, he makes two additional assertions: $( A 1 \land A 2 ) \to A 4 { \mathrm { ~ a n d } } A 4 \to A 3$ . If the opponent challenges these assertions as well, then the game moves into the recursive inner proofs. At this point, the proponent may choose to defend them using logic or any empirical strategy. If an empirical strategy is chosen for some assertion, then the game follows the pattern of empirical argumentation about this assertion. Thus an empirical proof is contained in an overall logic proof path. Note that an empirical proof path does not lead to any logic proof components, while a logic proof path could lead to empirical components. In such hybrid proofs, the proof structure is organized as a recursive inner proof tree as in the case of pure logic proofs, except that a proof path could contain empirical components as well. If the claim is defended successfully, then the chain of proof paths supporting the claim could contain both logic and empirical components. The overall proof component of the claim would contain both logic and data objects in this case. Consequently, a hybrid proof strategy is handled similar to the logic proofs, but with the additional provision to incorporate empirical components wherever used.

## 5. The Coordination Formalism

The coordination of the argument games among the group individuals is crucial to effective décision making. Coordination in such group processes usually evolves informally through the initiatives of some individuals to focus the deliberations. In a computer-supported environment, focusing the group on critical issues can be achieved in several ways. We formalize one of these approaches in the present context of argument gaming in the following discussion.

In a group decision making problem, several alternate proposals for action and their supporting arguments could arise. Therefore, it is necessary to consider each alternative systematically, assess its merits and drawbacks, and reach a decision on an appropriate course of action. This process entails a systematic capture of the arguments, regulation of the argument games and the application of appropriate resolution mechanisms to reach a final decision. The formalisms for representation and gaming address the issues of argument capture and game regulation. The coordination formalism addresses how the games can be conducted and finally resolved.

Consider a group of n members debating m proposals for action. The knowledge base pertaining to the m proposals is organized as follows: Let $\Phi = \left\{ \Phi _ { 1 } , \ldots , \Phi _ { m } \right\}$ denote the total knowledge base comprising m components, where component $\Phi _ { i }$ is the knowledge base corresponding to proposal i. The overall structure of $\Phi _ { i }$ follows the design developed in $\ S 3 .$ . Each component $\Phi _ { i }$ contains a thesis subcomponent denoted as $\Phi _ { i } ( T )$ and a set of antithesis components denoted as ${ \Phi } _ { i } ^ { j } ( A ) , j = 1 , \ldots , t _ { i }$ where t, denotes the number of such subcomponents for proposal i. In terms of our $t _ { i }$ representation formalisms, these components are defined as follows. Each component Φ, is a CAP-net pertaining to proposal ¿. The thesis subcomponent of Φ, is the $\Phi _ { i }$ $\Phi _ { i }$ part of the CAP-net consisting of arguments supporting the proposal and terminating at the final claim in support of the proposal. The final claim is called the thesis. For each proposal, there could be several opposing sets of arguments, with each set terminating at a claim opposed to the proposal. These claims are termed antitheses. Each set of these arguments constitutes an antithesis subcomponent of Φ, . For example, $\Phi _ { i }$ Figure 5 shows a thesis and an antithesis subcomponents of a proposai. In general, the thesis and antithesis subcomponents of a proposal can be stored together as an independent CAP-net. Hence, all the statements on the subject under consideration can be organized as a set of independent, proposal-based CAP-nets. While this organization yields efficient strategies for object base management, it also yields simple and convenient mechanisms for coordination.

![](/api/attachments/6X86RDY6/fulltext/images/565cf29593e70f9622d098854c7f878b5f58c96c5ff48fe805adf8dda1d9c08b.jpg)  
FIGURE 5. CAP-Net for the Illustration.

Group interactions can be scheduled using the set of m CAP-nets. Consider the CAP-net for any proposal for example. The group can be divided into subsets with respect to this net as proponents and opponents. While the thesis subcomponent is uniformly subscribed to by all the proponents, the opponents could accept the statements in this subcomponent to varying degrees, rejecting the rest. Similarly, the level of acceptance of the statements in the antithesis components could vary from individual to individual. The consideration of the proposals can be conducted either independently or concurrently. In concurrent analysis, different proposals may be evaluated in comparison with each other. In this case, it is possible that a propósal could appear in the CAP-net of another proposal. Consequently, it may become necessary to combine different CAP-nets into a single net for this analysis. In this case, the thesis subcomponent of a proposal can be viewed as an antithesis component of another. For the sake of simplicity, we consider a sequential analysis of proposals in the following discussion: This analysis can be extended to the case of concurrent consideration of proposals by combining the CAP-nets.

We employ two determining factors in a sequential consideration of proposals: critical mass and timeout. Many group decision processes are subject to time constraints, and resolution is usually achieved by some critical mass of individuals in support of a proposal. The critical mass and timeout parameters are either organizational policy decisions or are determined collectively by the group. For example, a majority vote in a faculty senate or a tenure decision committee is an organizational policy parameter. Similarly, instances of resolution of conflicting positions by the chairman of a committee as an internal working policy of the committee are also possible. In a corresponding manner, the time by which a tenure recommendation should be given by the decision committee is an organizational policy parameter, while other instances of committee decisions subject to an internally adopted time span are also possible. The timeout defines the appropriate distribution of the time available for the consideration of different proposals. The two parameters are closely related. and a behavioral study of these parameters in organizational decisions is an important area for future research. The proposed formalism for computer-assisted coordination employs these concepts as follows.

The consideration of the proposals is first organized into some sequence as agreed by the group. The critical mass and timeout parameters determine the scope of argumentation on each proposal. Then, the CAP-nets are posted by the system in sequence for argumentation. An opponent could choose appropriate points of argumentation in the thesis subcomponent, and the proponents are scheduled for its defense. Similarly, a proponent could choose to challenge some assertion in an antithesis subcomponent, and the supporters of this assertion are scheduled for its defense, In order to maintain a logical development of arguments and focus on critical issues, it is necessary for a challenger to specify the earliest claim in the string of logic in the net that he disagrees with. On the other hand, the challenger may choose to overlook certain claims that he may disagree with, in order to focus on the more important ones that appear later in the net. This facility in the coordinating mechanism is important, since it enables individuals to concentrate on major issues and attempt to find resolution quickly. The challenges on the assertions are thus scheduled by identifving their supporters and opponents. When a challenge is scheduled, an argument game is conducted about the challenged assertion and resolved as discussed earlier.

When the timeout condition of a proposal discussion is reached, the strength of its support is assessed by voting or other appropriate mechanisms chosen by the group. If the group decides to accept the proposal based on its support in comparison with the critical mass considerations, then the process is completed. Otherwise, the discussion on the current proposal is saved with the final assessments, and the next proposal is taken up for analysis. If all the proposals have thus been analyzed and no decision has yet been made, then the group could collectively assess the strengths of the proposals determined thus far through argumentation and decide to resolve through appropriate mechanisms selected by the group.

## 6. Concluding Remarks

Decisions in large corporations continually evolve from several group processes, shaping the focus of business activities over time. These decisions arise out of a combination of formal analyses and less formal interactions among decision makers. We characterize such decision situations from the perspective of argumentation and decision making within a group. Argumentation is a key element in many group decisions, and we propose formalisms for the representation, gaming and coordination of such processes. The representation formalism provides a framework for organizing the logic underlying the claims and arguments in a group. The gaming formalism provides a framework for conducting and regulating the group interactions. The coordination formalism addresses the issues of scheduling the games and the resolution process. The three formalisms together constitute the basis for designing computer-assisted systems that support argumentation processes in groups.

The representation formalism is a language for capturing arguments. Using this language, a network structure of the underlying knowledge base is developed. The knowledge base is designed as an object-oriented system, which greatly facilitates efficient storage and retrieval of arguments. This system is conceptualized as the driving element in argumentation processes, while it could also provide traditional information systems support. The argument gaming strategies and the coordination mechanisms are based on the architecture of the knowledge base. We develop strategies for gaming a variety of argumentation processes and show how they can be integrated with the knowledge base. The coordination mechanisms serve as supervisory and regulatory agents of the games, which can be dynamically controlled by a group.

This research has been motivated by a perceived need for efficient computer support for argumentative group decision processes. Using these formalisms, we propose the design of Argumentative Reasoning Facilitation Systems (ARFS), which could serve to record, organize, regulate, and coordinate argumentative decision processes in organizations. We conceptualize such systems as shells that can provide automatic support for these tasks, and be readily imported to any group decision making situation. We have developed the concepts underlying these formalisms in a general manner, such that systemic tools based on these ideas could provide the needed support in a variety of group processes. An ARFS would facilitate its users to record their logic and peruse the knowledge base using appropriate modules for storage and access. The modules for conducting argumentation games and scheduling the interactions would facilitate both synchronous and asynchronous interactions. This research is a futuristic vision of computer-assisted group decision support in organizations, where a computer is used as a repository of knowledge, theorem-prover of arguments provided by individuals, conductor of argument games and group facilitator. We are currently building a prototype shell of ARFS in a client-server environment. Several avenues of future research arise from this work. We outline some of them in the following discussion.

The proposed formalism for representation encompasses propositional and quantificational logic forms in argumentation. However, modal (necessity/possibility) and deontic (imperative statements) logic forms also occur commonly in practical argumentation. Therefore, expanding the scope of the representation language to accommodate modal and deontic elements of logic would considerably enrich the system and its expressive power. Development of theorem-proving modules to automatically test the logical validity of arguments would considerably enhance the supporting capabilities of the proposed system. The theorem-provers could produce basic logic proofs for arguments and ensure their validity. As a result, argumentation games involving just the basic logic proofs can be avoided. The development of appropriate natural language interfaces for logic construction and user-friendly interactions between the system and its users is an important area for future research. The study of the dynamics of argument games and coordination is very important from the viewpoint of organizational research. Issues such as modelling group dynamics in argument games, analysis of winning strategies, the study of resolution mechanisms such as critical mass and timeout, and modelling group perceptions on argumentation as it evolves are important organizational and behavioral research areas that are critical to the development of efficient and practical computer-assisted systems for argumentation support. We are currently studying some of these areas. These are new windows for the future, from the points of view of both research and practice.

## Appendix A: Recursive Inner Proof Tree Construction

The strategy of the recursive proof tree algorithm follows a depth-first extension of the proof tree. Consequently, it is necessary to maintain only one chain of the tree from the root leading to the current node in consideration at any time. Hence we drop the indices j and k, and present the algorithm as follows.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm: Logic_Proof_Tree
Begin
Let $A^1$ denote the original assertion;
Let l denote the number of levels to backtrack;
$\langle *l \text{ can be dynamically varied by the proponent*} \rangle$
i := 1;
Construct_Net(i);
End.
Procedure Construct_Net(i);
Begin
If there is no proof path from $A^i$
    Then
    If i = 1
    Then
    Return the failure of proponent
    Else
    Begin
    Select appropriate level l to backtrack;
    i := i - l;
    Construct_Net(i);
    End;
Else
    Begin
    Select a proof path $P(A^i)$;
    Present the arguments to the opponent;
    Determine opponent's response;
    If his response is $\phi_o$
    Then
    Begin
    Return the success of proponent;
    Save the logic from $P(A^1)$ through $P(A^i)$;
    End;
    Else
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
&lt;*he attacks $P(A^{i})$&gt; Begin Determine $A^{i+1}$; Determine proponent's response; If his response is $\phi_{p}$ Then Begin Select appropriate $l$ to backtrack; $i := i - l$; Construct_Net(i); End; Else Begin $i := i + 1$; Construct_Net(i); End; End; End; End.
</div>

## Appendix B: Dynamic Programming Model of Empirical Games

The empiriçal proof game can be modeled as a stochastic dynamic programming problem. This is shown as follows. Given a set of available proof paths, the proponent has the following decisions to make:

(i) the order in which the proof paths are going to be tried, and

(ii) if a proof path fails, decide whether to choose another proof path or accept his claim as false.

The objective in this process is to minimize the cost of proving, while keeping the Type I error (rejection of a false hypothesis) and the Type II error (acceptance of a true hypothesis) within acceptable levels. Since each proof process could involve data collection and/or analysis, we can determine their respective costs. We develop the overall framework of the dynamic programming model in the discussion below.

Let $P _ { 1 } , \ldots , P _ { n }$ be the proof paths available. Let $c _ { 1 } , \ldots , c _ { n }$ denote the respective costs associated with the proof paths. Let S denote a subset of proof paths $\operatorname { L e t } q ( P _ { i } | S )$ denote the probability that proof path $\pmb { P _ { i } }$ will be successful, given that the proof paths in S have failed. Let $t _ { 1 } ( P _ { i } , S )$ denote the probability of Type I error if the proof paths in S have failed, and path $P _ { i }$ results in accepting the claim. Similarly, we define $t _ { 2 } ( P _ { i } , S )$ as the probability of Type I error if the proof paths in S have failed, and the proponent agrees to reject the claim after the failure of path $\pmb { P _ { i } } .$ . Given the statistical nature of the experimentation, these probabilities can, in general, be estimated with reference to the context. Further, if the experimentation is consistent, the error functions $t _ { 1 } ( P _ { i } , S ) \{ t _ { 2 } ( P _ { i } , S ) \}$ will be monotonically nondecreasing {nonincreasing} functions of the size of S. Let α and β denote the acceptable levels of Type I and Type II errors, respectively

The decision problem consist of n stages. At any stage $\pmb { k } ,$ the proponent has $( n - k + 2 )$ possible moves. Each state in a stage k is characterized by the sequence of decisions made so far, from stage 1 to stage (k - 1). Note that the decision at any stage is either the selection of a new proof path or the termination of the argument by accepting failure. Accordingly, each state is characterized by the set of proof paths that have failed so far, from stage 1 to stage (k – 1). If a proof path tried out at stage (k – 1) actually succeeds, then stages k through n will not be realized. If all possible decisions at stage (k – 1) actually fail, then stage k potentially has $\pmb { n _ { k } } = \pmb { C _ { k - } ^ { n } }$ states.

Let $\{ s _ { k j } , k = 1 , \ldots , n , j = 1 , \ldots , n _ { k } \}$ denote the state vector, where each state corresponds to a decision point. Let $\theta _ { k } { \mathcal { N } } + 1 \gamma$ denote the set of states at stage $( k + 1 )$ that can be reached from state $k _ { k j } \mathbf { \hat { i } f } \mathbf { : ( i ) }$ a proof path is chosen at state $s _ { k J } ,$ and (ii) the chosen proof path fails. Let $d _ { k j }$ denote the decision variable representing the proof path chosen from $s _ { k j } .$ If the above two conditions are met, then the decision $d _ { k j }$ will lead to some state in $\theta _ { k j } ( k + 1 )$ . For instance, if $\mathop { d _ { k j } ^ { \prime } } = P _ { i } ,$ , then this decision could lead to a state at stage (k $+ 1 )$ , which comprises all the proof paths represented in $\bar { s } _ { k j }$ and $P _ { j }$ . Let $d _ { k j } ^ { \prime } = \emptyset$ imply that the proponent has chosen to terminate the argument by accepting failure. Given this notation, we represent $\pmb { q } , \pmb { t _ { 1 } } , \pmb { t _ { 2 } }$ and C to be consistent with it as follows: g $( d _ { k } ) ( \mathrm { i f } d _ { k } )$ is not null), $t _ { 1 } ( d _ { k j } )$ (it $\mathbf { \Delta } _ { \mathbf { { d } } _ { k j } }$ is not null), $t _ { 2 } ( d _ { k j } ) ( \mathrm { i f } d _ { k j } )$ is null), and $C ( d _ { k j } )$ . Note that $C ( d _ { k j } ) = 0 \mathrm { i f } d _ { k j } ^ { ' } = \emptyset$ . This is because, i $\mathbf { f } d _ { k j } \neq \emptyset ,$ and the proof path succeeds, then $t _ { 1 } ( d _ { k j } )$ is incurred, and if $d _ { k j } = \emptyset$ then $t _ { 2 } ( d _ { k j } )$ is incurred. Clearly, $q ( d _ { k j } )$ is applicable only if $d _ { k j } \neq \emptyset$ Let $D _ { k J }$ denote the minimum total cost from state $\pmb { S _ { k j } }$ to the end, such that the constraints on errors (whichever is applicable) are satisfied. A state sk, is termed a feasible state, only if there is at least one path $\mathbb { s } _ { k j }$ from sk, to completion satisfying the appropriate error constraint. Similarly, a stage k is termed a feasible $\bar { s } _ { k j }$ stage, only if it contains at least one feasible state. A decision dk, from a feasible state s ,is said to exist, only $d _ { k j }$ $s _ { k _ { i } }$ if it leads to another feasible state it $\ell s _ { k j } \neq \emptyset$ , and if it leads to a feasible termination if $d _ { k j } = \mathcal { D }$ . Infeasible states and stages are eliminated form consideration right at the outset. Hence, we assume that every state in consideration is feasible and summarize the recursions for the stagewise decision problem as follows.

Let m(≤n) feasible stages exist. The terminal conditions of the recursions are: $D _ { m j } = c ( d _ { m j } ) { \mathrm { i f } } d _ { m j } = \emptyset$ and $\begin{array} { r } { D _ { m j } = 0 , } \end{array}$ , otherwise, $\forall s _ { m } ,$ . Note, at this stage, only two decisions are possible from each state $s _ { m j } =$ either $d _ { m j } = \dot { 0 } ,$ or $d _ { m j }$ is the only available proof path. Since $s _ { m j }$ is feasible, at least one of these two possible decisions will lead to a feasible termination. If the null decision does not exist, then the only alternative is to try out the available proof path. In this case, we require that $t _ { 1 } ( d _ { m } ) \leq \alpha$ if the proof path succeeds, and $t _ { 2 } ( d _ { m j } ) \leq \beta$ if it fails. Otherwise, state $s _ { m } )$ , is infeasible and will not be considered

Now, consider any state $s _ { k j } . \mathbf { C l e a r l y } , \mathbf { i } \bar { \mathbf { f } } d _ { k j } = \emptyset$ exists, then it is the best decision to make. If it does not, then three cases arise. Consider some nonnull decision $d _ { k j }$ . This proof path could either succeed or fail. If it succeeds, then the argument is terminated if $\dot { \iota } _ { 1 } ( d _ { k j } ) \leq \alpha .$ Otherwise, the argument should still go on and find a feasible solution. Let δ denote the cost of future argumentation. $\mathrm { I f } t _ { 1 } ( d _ { k j } ) \leq \alpha _ { \mathrm { : } }$ , then $\hat { \boldsymbol \theta } = 0 , \operatorname { I f } t _ { 1 } ( d _ { k _ { J } } )$ $> \alpha ,$ then $\delta = D _ { k + 1 , j ^ { \prime } } , j ^ { \prime } { \in } \theta _ { k j } ( k + 1 )$ . If the argument fails, then $\delta = D _ { k + 1 , j } . \operatorname { L e t } \dot { r ( } d _ { k j } )$ be the probability that $t _ { 1 } ( d _ { k j } ) \leq \alpha$ will be achieved. This probability is also context-sensitive and should be assessed with reference to the argumentation environment. In all cases, the cost $C ( d _ { k j } )$ is incurred. Hence, the expected total future cost following decision $\pmb { d } _ { k j }$ is

$$
E \left(d _ {k j}\right) = C \left(d _ {k j}\right) + q \left(d _ {k j}\right) \left(1 - r \left(d _ {k j}\right)\right) D _ {k + 1, j ^ {\prime}} + \left(1 - q \left(d _ {k j}\right)\right) D _ {k + 1, j ^ {\prime}}, j ^ {\prime} \in \theta_ {k j} (k + 1)
$$

which simplifies to:

$$
E (d _ {k j}) = C (d _ {k j}) + (1 - q (d _ {k j}) r (d _ {k j})) D _ {k + 1, j ^ {\prime}}, j ^ {\prime} \in \theta_ {k j} (k + 1).
$$

In general, the monotonically nondecreasing nature o $[ t _ { 1 }$ suggests that r will be monotonically nonincreasing. Hence, it is possible to estimate r from the behavior in the first few stages and employ appropriate approximation. However, for the initial stages, we could assume $\pmb { r } = \mathbf { 0 . 5 } ,$ , in the absence of any available data or r. Putting it all together, the recursion for state $s _ { k j }$ simplifies to: $D _ { k j } =$ min $\{ E ( d _ { k j } ) \}$ } over all $d _ { k j } \operatorname { i f } d _ { k j }$ = ∅ does not exist, and $D _ { k j } = 0 ,$ , otherwise.

The recursions terminate by finding D1, and the decision corresponding to stage 1 is made initially. This $D _ { 1 1 }$ begins the proof net construction. Decisions are made dynamically a stage at a time, observing the outcome of each stage. The costs are recomputed after each stage, and the optimal decision for the current stage is chosen. The constraints on the error probabilities act in opposite directions in this decision making process. During the initial stages, Type I error constraints (t2) tend to be binding, forcing the proponent to continue $( t _ { 2 } )$ the proof process. Consequently, the null decisions may not exist during these stages. During the final stages, Type II error tends to predominate. This discourages the proponent from continuing the process due to increasing costs and decreasing chances of success. If the argument continues till a point where a null decision exists, then it makes sense to terminate the argument by accepting failure, since any further argumentation may not improve the chances of success. Accordingly, we need to consider the stages along a chain of proof paths only till a null decision appears. Intuitively, this implies that the proponent should continue to argue along the optimal chain of proof paths, until either he succeeds or the first chance to a feasible rejection appears, This point of appearance is a stopping time in the argumentation process.\*

\* Steven O. Kimbrough, Associate Editor. This paper was received on August $4 , 1 9 9 2 ,$ , and has been with the authors for 2 revisions.

## References

Applegate, L., C. A. Ellis, C. Holsapple, F. Radermacher, and A. B. Whinston, "Organizational Computing: Definitions and Issues," Organizational Computing, 1, 1 (1991).

Chang, A., A. Bailey, J. Mutchler, and A. Whinston, "Modeling the Going Concern—Judgement Using Argumentation Theory" Organizational Computing, 3, 1 (1993).

DeSanctis, G. and B. Gallupe, "Group Decision Support Systems: A New Frontier," Database, 16, 2 (1985) 2-10.

Doyle, Jr., “A Truth Maintenance System," Artificial Intelligence, 12, (1979).

Fischer, G., R. McCall, and A. Morch, "Design Environment for Constructive and Argumentative Design," Proceedings of SIGCHI, Austin, TX, 1989.

Fisher, A., The Logic of Real Arguments, Cambridge University Press, Cambridge, MA, 1988.

Gallaire, H., J. Minker, and J. M. Nicolas, "Logic and Databases: A Deductive Approach," ACM Comput ing Surveys, 16, 1 (1984) 154–185.

Gensler, H. J., Symbolic Logic, Prentice-Hall, Englewood Cliffs, NJ, 1990.

Kimbrough, S. O., “A Graph Representation for Managemènt of Logic Models," Decision Support Systems, 2, 1 (1986) 27–37.

, "Notes on the Argumentation Theory for Decision Support Systems," in Proceedings of the 1990 International Society on DSS Conference, Austin, TX, September, 1990.

Krasner. H., McInroy, J., Jr. and D. B. Walz, "Groupware Research and Technology Issues with Applications to Software Process Management," IEEE Transactions on Systems, Man and Cybernetics, 21, 4 (1991).

Kunz, W. and H. Rittel, Issues as Elements if Information Systems, Center for Planning and Development Research, University of California, Berkeley, Working Paper No. 131, 1970.

Kyng, M., “Designing for Co-operation: Co-operating in Design," CACM, 34, 12 (1991).

Locks, M. O., "The Logic of Policy as Argument," Management Science, 31, 1 (1985) 109–114.

Lorenzen, P., Formal Logic, Reidel Publishing Company, Dordrecht, The Netherlands, 1965. P., 1

, Normative Logic and Ethics, Bibliographisches Institute Mannheim/Wien/Zurich, B. I. Wissenschaftsverlag, 1984.

Constructive Philosophy. University of Massachusetts Press, 1987.

Marschak, Jr., Economic Theory of Teams, Yale University Press, New Haven, CT, 1972.

McCall. R., “PHIBIS: Procedurally Hierarchical Issue-based Information Systems," Proceedings of 1987 Conference on Planning and Design in Architecture, American Society ofMechanical Engineers, 1987.

McGuire, C. B. and R. Radner, Decision and Organization, North-Holland, Amsterdam, The Netherlands, 1972.

Mitroff, I. I., R. O. Mason, and V. P. Barabba, "Policy as Argument—A Logic for Ill-Structured Decision Problems," Management Science, 28, 12 (1982) 1391–1404.

Pager, D., “A Proposal for a Computer-based Interactive Scientific Community," CACM, 15, 2, 1972

Potts, C. and G. Bruns, “Recording the Reasons for Design Decisions," MCC Technical Report STP-304- 87, Austin, TX, 1987.

Ralston. A. and E. D. Reilly, (Eds.), Encyclopedia of Computer Science, (3rd Ed.), Van Nostrand, NY, 1993.

Rittel. H., “A Concept for an Argumentative Planning Information Systems," Institute for Urban and Regional Development, University of California at Berkeley Working Paper No. 324, Berkeley, CA, 1980.

Simon. H.. Administrative Behavior, The Free Press, NY, 1957.

Swanson. E. B., “Business Value as Justifactory Argument," in Measuring Business Value of Information Technologies, P. A. Strassmann, P. Berger, E. B. Swanson, C. H. Kriebel, and R. J. Kauffman, (Eds.), ICIT Press. International Center for Information Technologies, Washington, D.C., 1988.

Thagard. P., “Explanatory Coherence." Behavioral and Brain Sciences, 12, (1989) 435–502.

Toulmin, S., The Uses of Arguments, Cambridge University Press, Cambridge, England, 1958 l ouimin, S., 1 ne Uses of Argumenls,

, R. Rieke, and A. Janik. An Introduction to Reasoning, Macmillan, 1979.

Winograd. T. and F. Flores, Understanding Computers and Cognition, Addison-Wesley, Reading, MA 1986.

Zlatareva. N. P., "Truth Maintenance Systems and Their Applications for Verifying Expert System Knowledge Bases," Artificial Intelligence Review, 6, 1 (1992), 67–110.
