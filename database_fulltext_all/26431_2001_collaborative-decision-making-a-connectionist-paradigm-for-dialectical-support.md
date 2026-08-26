---
otero_id: 26431
otero_key: "Y6W7T9UQ"
title: "Collaborative Decision Making: A Connectionist Paradigm for Dialectical Support"
authors: "T. S. Raghu; R. Ramesh; Ai-Mei Chang; Andrew B. Whinston"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.4.363.9705"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 4R

![](/api/attachments/Y6W7T9UQ/fulltext/images/9f1f09111a493ab193c309743369ec94404b2dd69b58ebf45be196a6b05b519d.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Collaborative Decision Making: A Connectionist Paradigm for Dialectical Support

T. S. Raghu, R. Ramesh, Ai-Mei Chang, Andrew B. Whinston,

To cite this article:

T. S. Raghu, R. Ramesh, Ai-Mei Chang, Andrew B. Whinston, (2001) Collaborative Decision Making: A Connectionist Paradigm for Dialectical Support. Information Systems Research 12(4):363-383. http://dx.doi.org/10.1287/isre.12.4.363.9705

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/Y6W7T9UQ/fulltext/images/6ca215a6e5bd6332f9431bdde9c608d4559ebf9f0e4d5c3ef4fcc3485fcbaa0a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Collaborative Decision Making: A Connectionist Paradigm for Dialectical Support

T. S. Raghu • R. Ramesh • Ai-Mei Chang • Andrew B. Whinston

School of Accountancy and Information Management, Arizona State University, Tempe, Arizona 85287

Department of Management Science and Systems, School of Management, State University of New York at Buffalo, Buffalo, New York 14260

Information Resources Management College, National Defense University, Washington, District of Columbia 20319 Department of Management Information Systems, University of Arizona, Tucson, Arizona 85721 raghu.santanam@asu.edu • rramesh@acsu.buffalo.edu • chang@ndu.edu • abw@uts.cc.utexas.edu

he facilitation and analytical support of argumentation-based collaborative decision making is the focus of this research. We model collaborative decision making as an argumentation process. We develop a connectionist modeling framework, a network representation formalism for argument structures, connectionist network mechanisms, and their models of computations to extract the behavior of argument structures. We use two examples from the case study literature to illustrate the concepts. Several interesting properties of the connectionist network models are observed from our computational results. We find that although the length of the computation is affected by parametric values, the final activation levels of the units are largely unaffected. We observe that the initial activation levels of the defeasible units seem to have no effect on their final activation levels. The proposed modeling approach generates valuable insights into the characteristics of specific argumentative discussions. While the intention of this work is not to introduce the connectionist paradigm as a means to bring arguments to a closure (resolution), we show that certain resolution mechanisms can be easily implemented under the connectionist framework.

(Collaborative Decision Making; Connectionist Modeling; Dialectical Support; Argumentation)

## 1. Introduction

The focus of this research is on the development and analysis of a framework of system support for the dialectical (argumentative) processes in collaborative decision making. Collaborative decisions in most organizations typically evolve from either formal or informal deliberations in groups where the group members consider and debate various possible decision options. In general, most such decision problems tend to be highly unstructured, yielding limited modeling tractability. Consequently, such decision issues are resolved through discussions, where argumentative logic and persuasive presentation are critical. The proposed framework is essentially motivated by this. More specifically, our motivations can be stated as follows: First, there is a need to maintain a persistent discussion thread in order to sustain the group’s focus throughout the process. Second, periodic feedbacks on positional assessments to group members would foster creative problem solving and positional strategy development during a collaboration process. Third, automated support for conflict resolution and argument assessments is much needed in a fast-emerging facet of corporate collaborations: computer-supported distributed teamwork (Barua, Chellappa, and Whinston 1997).

In a collaborative discussion process, a group collectively addresses a set of common decision issues. The discussion takes the form of argumentation, where the positions of some individuals can be challenged. A challenge may occur either as a need for a valid argument to support a position or as a contraposition. In general, the discussion process involves both strict and defeasible reasoning (Vreeswijk 1992). Strict reasoning is structurally coherent and logically consistent, and is thus not open to argumentation; defeasible reasoning includes structures and logic that are open to argumentation. A group will focus on a discussion’s defeasible components, and systemic support is needed in this area.

Defeasible reasoning arises due to perceptual differences among individuals about claims that lack a strong support base in terms of evidential data or strict reasoning. The resolution of the differences hinges on strengthening the support base and/or persuasive presentation. Therefore, any analytical approach to assess a claim as ‘‘winning’’ or ‘‘losing’’ needs to model these differences, and can at best be heuristic. There is a growing body of literature in this area (Vreeswijk 1992, Fischer et al. 1991, Locks 1985) that attempts heuristic resolutions of defeasible logic, besides providing structural formalisms for representation. In this context, capturing human cognition is central to the analysis of defeasible logic, and connectionist modeling provides a natural approach for this purpose. Connectionist models similar to the one presented in this paper have been used to model propositional logic (Pinkas 1995), causal reasoning (Sun 1995), and explanatory coherence (Thagard 1989). In this paper, we have used the connectionist approach to model defeasible arguments in collaborative discussions. The connectionist approach is an attempt to emulate the massively parallel neuronal cognition of human beings (Feldman 1985). In this proposed connectionist architecture, arguments are structured into basic, atomic-level information units along with their logical and other humanintended relationships. The basic informational units are represented as the units and their relationships as the arcs in a connectionist network of defeasible logic.

The major contributions of this research are threefold. First, we develop a systematic framework for argument representation in modeling collaborative discussions. This framework includes both static formalisms for structural representation and dynamic formalisms for modeling dialectical games in collaboration. A key objective of developing this framework is to build and maintain discussion threads in the decision process. Second, we develop connectionist architectures using the representational formalisms for argument analyses during the course of a discussion. The objective here is to provide feedback to the participants about the strengths of various arguments. Third, we illustrate the concepts and ideas through connectionist models of practical discussions drawn from the published case study literature (Coopers and Lybrand 1990). We have developed a prototype of the connectionist system and have carried out detailed empirical studies with the illustrative cases. These analyses provide considerable insights into the connectionist assessments of human perceptions on defeasible logic, and into how we can build automated support for facilitating collaborative discussions.

The organization of the paper is as follows: Section 2 presents the foundations of this research; §3 presents the framework of formalisms for argument structure and the gaming process; §4 presents the connectionist paradigm; and §5 integrates it all through an illustration. The empirical studies are presented in §6, and the conclusions with directions for future research in §7.

## 2. Research Foundations

The current research draws from, and integrates, foundational concepts from three broad streams of research: argument analysis and defeasible reasoning studied in the domains of logic and artificial intelligence, Computer Supported Cooperative Work (CSCW) (Bowers and Benford 1991, Goldberg et al. 1992) and Group Support Systems (GSS) (Ellis, Gibbs, and Rein 1991, Greenburg 1991, Grief 1988), and connectionist modeling approaches. While the literature in each of these streams is extensive, we will focus on some of the immediately relevant and important works in the following discussion.

CSCW has emerged as a major research discipline with the advances in networking and communications technologies. Most of the applications developed in this area pertain to electronic meeting systems (Barua, Chellappa, and Whinston 1995), teleconferencing and messaging systems (Nunamaker et al. 1991), multiuser editors (Hill et al. 1992), and intelligent agents (Sheth and Maes 1993). These systems are primarily concerned with enabling distance communication in collaborative work processes, and using multimedia tools to support different modes of interactions. Our goal here is to develop an argumentation representation framework for facilitating cooperative work. We address this goal by integrating concepts from argument analysis, defeasible reasoning, and connectionism.

Analysis of arguments for their logical consistency and coherence has been traditionally considered to be in the domain of philosophy and cognitive science (Toulmin 1958, 1979; Mitroff et al. 1982; Locks 1985; Kimbrough 1986). The works of Toulmin, Mitroff et al., and Kimbrough develop formalisms for argument logic representation and methods for determining the logical consistency of arguments. A parallel yet alternate approach to argument analysis was proposed by Lorenzen (1965, 1984, 1987) which captures argumentation as a dialogue between a proponent and an opponent. The dialogical game continues until one of the two individuals reaches a self-contradiction. Ramesh and Whinston (1994) integrate the approaches of Toulmin and Lorenzen and propose formalisms for recording, organizing, and coordinating argumentative discussions in organizations. Though their formalisms provide flexible and adaptive coordination mechanisms to guide and focus the argumentation process, their formalisms do not provide a means to assess the strengths of arguments.

The research on defeasible reasoning is an outgrowth of the basic works on argument analysis, especially in artificial intelligence. However, mathematical logic and classical proof theories (Gensler 1990, Lorenzen 1984) do not provide an adequate framework for dealing with such arguments. Further, simple rule-based systems are not suitable for this problem as they are too categorical and too sensitive to the order of application of rules. For instance, a proposition in an argument cannot be rejected till all available evidence and arguments have been considered. However, rule-based systems do not provide a mechanism to evaluate all available propositions in parallel. The limitation of using binary categories (acceptance and rejection of propositions) can be overcome to some extent by using certainty factors. However, even with certainty factors one has to carefully engineer the rule base to keep track of the paths along which evidence is propogated (Russel and Norvig 1995). Recent works have shown that certainty factors are generally unreliable and strongly caution against using this method (Heckerman 1991). Several recent works—for example, Lin and Shoham (1995), Pollock (1991), Loui (1994), Nute (1988), and Vreeswijk (1992)—deal primarily with representation formalisms and heuristics for argument analysis, interpretation, and outcome prediction. Particularly notable works in the area of defeasible argument analysis include Swanson (1988), Nute and Erk (1998), Nute, Henderson, and Hunter (1998), and Hua and Kimbrough (1998). Nute and Erk (1998) present the notion of defeasible logic graphs that provide a visual representation of complex arguments. Nodes in the defeasible graphs are eventually marked as derivably true, derivably false, or undetermined. Nute, Henderson, and Hunter (1998) extend the theory of defeasible graphs and present a prototype system for argumentation support. Using a similar approach to defeasible logic representation, Hua and Kimbrough (1998) present an argumentation support system in which one can link nodes in the network to supporting documentation through hyperlinks. Hyperlinked documents in the system provide context-specific documentation for each node in the argumentation graph.

The approach used in this paper is to move towards a system of argument analysis in which one is not necessarily constrained to resolving argumentation to discrete categories. Using binary categories as a basis for rejecting or accepting arguments prevents one from assessing the relative strengths of the arguments. While connectionist models do not have the strong theoretical underpinnings of logic-based defeasible graphs, using connectionist models for this purpose has many advantages over methods that utilize simple binary categories of acceptance and rejection (Vreesjwick 1992). Connectionist modeling achieves better sensitivity in argument assessment by indicating the degree of acceptance or rejection of arguments. In addition, one can assign different weights on the arcs connecting the different units in the model. This enables one to capture not only the relations between units but also the strength of the relation.

## 3. Argumentation: Structure and Process

The specific research questions that we address in modeling argument-based teamwork are as follows:

• What formalisms of the argument logic would pragmatically and efficiently capture the structure and content of collaborative discussions?

• How can the evolution, interaction, and resolution of these information units be captured within the context of a dynamic gaming model of teamwork?

The above questions are the foundations of this work and lead to our research questions on connectionist modeling developed in the next section. We address the above questions by modeling defeasible argument logic based on the Toulmin and Lorenzen systems as follows.

## 3.1. Argument Structure

We model the collaborative decision-making process as a dynamic game in which individuals assert their positions through both primitive and derivative statements. A primitive is a stand-alone assertion and a derivative is obtained as a strictly logical or defeasible consequence of others. Although an individual could simply make a primitive assertion without regard to its effects on the overall discussion, a cogent argument requires the assertions to be linked and organized in some logical sense. The logical/defeasible argument structures generated in this process are the focus of a discussion entailing a dynamic sequence of challenges and responses. We first formalize the argument structures as follows:

Let G denote the group of individuals in a collaborative discussion. Let D denote the argument structure representing the various positions, facts, and their interrelationships generated in the discussion. Clearly, D is a temporal entity, evolving and changing over time as the discussion proceeds. The structure D is basically a collection of assertions made by the individuals in the group. This is indicated as follows:

## D - {A: A is an Assertion}.

An assertion A is of two types: positions and inferences. A statement of position is a claim, and is assumed to be a well-formed sentence. A statement of inference is a structural relationship among a set of positions and facts. We formalize the structure of these assertion types as follows:

Let L denote a language from which the structure D is constructed. The language L is a triple S, R, Q-, where S constitutes the sentences, R is a set of assertions built using sentences, and Q is a set of assertion qualifica tions. S provides the basis for the construction of positions and statements of fact. A factual statement is any evidential data that is commonly accepted by the group, while the positions are the subject of discussion. R provides the basis for the construction of positional and inferential assertions. This enables the construction of positional assertions from sentences obtained from S as well as inferential structures from other assertions. Q provides the basis for the qualification of an argument on whether it is strict or defeasible. While a defeasible argument is subject to debate and possibly defeat, a strict argument is a logical inference that will not be questioned by anyone in the group. R provides two constructs support- and oppose- to build inferential structures among positions and facts. Q provides two constructs strict- and defeasible- to qualify assertions. As a result, a combination of these constructs yields the following qualified inferences: strict support-, defeasible support-, strict opposition-, and defeasible opposition-. We indicate these qualified inferences as <sup>F</sup>-, ⇑-, <sup>f</sup>-, and ⇓-, respectively, in our structural formalism. Finally, we associate each assertion A with its proponents through a signature set r(A), which consists of all the individuals who subscribe to A. Putting it all together, we present a complete BNF-formalism for the representation of argument structures in Figure 1.

The argument structures captured through the above formalisms provide snapshot views of a dynamic argumentation process. A temporal sequence of such snapshots taken at discrete points in time would reveal the evolution of the argument structures. This evolution follows the dynamic progression of events in the group discussion with the snapshots capturing

## Figure 1 BNF for Representation of Argument Structures

<Argument Structure D > := { A: A is an assertion} Sentence Structure (S) definitions <Sentence Γ> := < defeasible sentence: Γd > | < factual sentence: Γf> <Defeasible sentence $\Gamma _ { \mathrm { d } } > : : =$ <position stated: $< \Gamma _ { \mathrm { d } } > \mid ~ { - } < \Gamma _ { \mathrm { d } } > \mid ~ < \Gamma _ { \mathrm { d } } > ~ \wedge ~ < \Gamma > \mid ~ < \Gamma _ { \mathrm { d } } > ~ \vee ~ < \Gamma > ~ >$ <Factual sentence $\Gamma _ { \mathrm { f } } > : : =$ <a statement of fact: <Γf>| <Γf> ∧ <Γf>|<Γf> ∨ <Γρ>> <Logical connectives C> := < And: ^ | Or: v > Assertion Structure (R) definitions <Assertion A > := <defeasible assertion: Å> | <strict assertion $\hat { A } >$ <Defeasible assertion Ä> := <defeasible sentence: $\Gamma _ { \mathrm { d } } { > } \vert$ <defeasible support: $\Gamma \Uparrow \Gamma _ { \mathrm { d } } > |$ < defeasible opposition: $\Gamma \Downarrow \Gamma _ { \mathrm { d } } \mathrm { > }$ <Strict assertior $\hat { A } >$ := <Strict support from facts: $\Gamma _ { \mathsf { f } } \uparrow \Gamma _ { \mathsf { d } } { > } |$ <Strict opposition from facts $\Gamma _ { \mathsf { f } } \downarrow \Gamma _ { \mathsf { d } } >$ Qualification Structure (Q) definitions < Strict Support ↑ > := {The support is universally accepted within the group} < Strict Opposition $\downarrow > : : = \{ \mathrm { T h e }$ opposition is universally accepted within the group} < Defeasible support  > ::= {The support is accepted only by its proponents } < Defeasible opposition $\Downarrow { > } \mathrel { : : = }$ {The opposition is accepted only by its proponents}

the group’s collective positions as successive developments occur. Therefore, dialectical support in collaborations can be provided by successive analyses of argument structures as they evolve. This requires the mapping of the argument structures to the debate process in collaborations. We develop a formalism to capture this debate process in the following discussion.

## 3.2. The Debate Process

In general, a group tends to be divided into two sets with regard to a defeasible assertion: proponents and opponents. A debate on a defeasible assertion usually proceeds in the form of challenge/response exchanges between its proponents and opponents with the members occasionally raising some questions and/or providing some explanatory insights on the debate issues. Before developing the formalism for the debate process, we present two example debates drawn from the case study literature in the auditing area (Coopers and Lybrand 1990) that illustrate the structure and content of a debate process.

3.2.1. Example 1: A Mortgage Loan Debate. The objective of business auditing is to ensure that a client organization reports a fair picture of its financial position and operating results. In this process, the auditors and the client face many issues and conflicting positions, which cannot be easily resolved through simple quantitative analyses and would require an elaborate discussion process between the client and the auditing team. In the discussion process, the auditors and the client make use of the facts available to them to assert their individual positions. One such issue that usually entails a discussion is the inclusion of amounts owed by the customers in the financial statements. The auditors have to examine a number of evidential data and the client assertions to determine if an amount owed by a customer could be included in the financial statement. This example deals with the auditing of a bank and the ensuing discussion.

The bank reports that it has mortgage receivable in the amount of \$5 million. The auditors’ responsibility is to obtain sufficient evidence to either support or refute the client’s claims. This decision problem thus involves a group consisting of the auditing team and representatives from the bank (the client firm). A typical interaction between the auditors and the client representatives is described below in the form of a debate process. The quotes below are paraphrased from the original case discussions and are presented in the form of a sequential debate process here. The defeasible assertions of the client are denoted as $C ^ { d }$ and those of the auditor are denoted as $U ^ { d } .$ The facts presented in the debate process are denoted as F.

We would like to emphasize here that we have used only parts of the case materials in building the discussion thread. The assertions and facts have been paraphrased from the original case discussion (Coopers and Lybrand 1990). The labeling of facts and defeasible assertions in the debate process presented below is based on our interpretation of the discussions between the auditors and the client. In essence, an assertion is modeled as a fact if it can be confirmed unconditionally by supporting evidence. For example, Fact $F _ { 5 }$ can be supported by data on realty values in the area. Similarly, Fact $F _ { 6 }$ can also be supported by the trend in realty values for that area. Assertions that can be challenged have been labeled as defeasible assertions. For instance, while it is agreed upon readily that the mortgagee has filed for bankruptcy $( F _ { 2 } )$ , the reasons put forth for this filing $( \mathrm { e . g . } , C _ { 3 } ^ { d } )$ has been challenged. We would like to acknowledge that we do not provide any systematic mechanisms to assess whether a statement should be accepted as a fact or as a defeasible assertion.

Client: $A _ { 1 } { \mathrm { : } }$ Since mortgagee’s financial condition is good $( C _ { 1 } ^ { d } )$ and mortgagee is a secured creditor $( F _ { 1 } ) _ { \ / }$ , the loan is collectible $( \bar { C _ { 2 } ^ { d } } ) . \{ A _ { 1 } \colon ( F _ { 1 } \wedge C _ { 1 } ^ { d } ) \ \uparrow \ C _ { 2 } ^ { d } \}$

Auditor: $A _ { 2 } { \mathrm { : } }$ Since mortgagee has filed for bankruptcy $( F _ { 2 } )$ , his financial condition is not good $( C _ { 1 } ^ { d } )$ This fact also raises concerns over the collectibility of the loan $( C _ { 2 } ^ { d } ) . \left\{ A _ { 2 a } : F _ { 2 } \right.$ ⇑ $C _ { 1 } ^ { d }$ and $A _ { 2 b } \colon F _ { 2 } \Downarrow C _ { 2 } ^ { d } \}$

Client: $A _ { 3 } { \mathrm { : } }$ Bankruptcy has been filed for planned reorganization $( C _ { 3 } ^ { d } )$ We think this supports our claim . that the financial condition of the mortgagee is good $( C _ { 1 } ^ { d } ) . \ \{ A _ { 3 } \colon { C _ { 3 } ^ { d } \Uparrow } \ C _ { 1 } ^ { d } \} \ A _ { 4 } .$ Moreover, realty value of the mortgage is of sufficient value to pay for mortgage which again implies that the loan is collectible <sup>d</sup> (C ), $( C _ { 2 } ^ { d } ) . \{ A _ { 4 } { : } C _ { 4 } ^ { d } \uparrow C _ { 2 } ^ { d } \}$

Auditor: $A _ { 5 } { \mathrm { : } }$ Mortgagee has defaulted on other interest payments $( F _ { 3 } )$ , therefore we do not believe the story that bankruptcy is for planned reorganization $( C _ { 3 } ^ { d } )$ $\{ A _ { 5 } \colon F _ { 3 } \Downarrow C _ { 3 } ^ { d } \} A _ { 6 } \colon$ Also, market share of mortgagee has dropped by 60% $( F _ { 4 } ) _ { . }$ , therefore, we cannot agree that mortgagee is in good financial condition $( C _ { 1 } ^ { d } ) . \{ A _ { 6 } \colon F _ { 4 }$ $\Downarrow C _ { 1 } ^ { d } \} A _ { 7 } \mathrm { : }$ Realty value has declined in the area $( F _ { 5 } ) _ { . }$ , so we do not think the realty value is sufficient to pay off the mortgage <sup>d</sup>(C ). <sub>4</sub> $\{ A _ { 7 } \colon F _ { 5 } \Downarrow C _ { 4 } ^ { d } \}$

Client: $A _ { 8 } { \mathrm { : } }$ Realty values are on the rise in the geographic area $( F _ { 6 } ) _ { . }$ , which implies that the decline in realty value is only temporary $( C _ { 5 } ^ { d } ) . \{ A _ { 8 } ; F _ { 6 } \Uparrow C _ { 5 } ^ { d } \} A _ { 9 } ;$ For this reason, we still think that realty value is sufficient to pay off the mortgage $( C _ { 4 } ^ { d } ) . \{ A _ { 9 } \colon C _ { 5 } ^ { d } \Uparrow C _ { 4 } ^ { d } \}$

Auditor: $A _ { \mathrm { { 1 0 } } } \mathrm { { : } }$ We think that the economic conditions are going to keep the realty value down Hence,<sup>d</sup> (U ). we feel that the decline in realty value is not temporary $( C _ { 5 } ^ { d } ) . \{ A _ { 1 0 } \colon U _ { 1 } ^ { d } \Downarrow C _ { 5 } ^ { d } \}$

3.2.2. Example 2: A Going Concern Debate. This case deals with the going concern assessment of a company by a team of auditors. The decision scenario involves a study of operations of Dermaceutics Inc., a biotechnical company that has just gone public, by its auditors. Dermaceutics provides two primary products: Cortoline and Bitroleen. Cortoline is a mature product, and has been facing increased competition in the market of late. Bitroleen is a new product with an uncertain market potential. Research and development on another product called TDR-42 has been completed at Dermaceutics, and is currently under limited production in anticipation of a large-scale market introduction in the near future. The company has of late embarked on a significant expansion of its facilities, and has invested large amounts in capital equipment and lease of new facilities.

Faced with the problem of deciding whether Dermaceutics is a going concern or not, the auditors have identified an initial list of issues to be addressed in their deliberations as follows: (i) operating performance of the firm, (ii) debt coverage of the firm $( \mathrm { i . e . }$ its ability to service debt with current cash flow levels), (iii) ability to cover operating needs with current cash flow levels, (iv) ability to keep pace with rapid changes in technology, (v) market potential of TDR-42, and (vi) market future of Cortoline and Bitroleen. In particular, the market potential of TDR-42 is needed for a justification of capital investments and other commitments made in producing ${ \mathrm { i t } } ,$ and the age of Cortoline and uncertainty of Bitroleen are critical factors in an assessment of the cashflows that are likely to be generated in the near future. The exchange between the auditors and the client in an ensuing argumentative discussion is as follows:

Client: $A _ { 1 } { \mathrm { : } }$ We consider ourselves as a going concern $( C _ { 1 } ^ { d } )$ Our operating performance has been good . $( C _ { 2 } ^ { d } )$ and our debt coverage is adequate as well <sup>d</sup> (C ). $\{ A _ { 1 } \colon$ $( C _ { 2 } ^ { d } \wedge C _ { 3 } ^ { d } ) \Uparrow C _ { 1 } ^ { d } \}$

Auditor: $A _ { 2 } { \mathrm { : } }$ There seems to be a low ratio of uncommitted cash flow This may affect the future of<sup>d</sup> (U ). your company $( C _ { 1 } ^ { d } )$ in an adverse manner. $\{ A _ { 2 } \colon U _ { 1 } ^ { d } \ \down$ ⇓ $C _ { 1 } ^ { d } \} \ A _ { 3 } \colon$ In addition, Dermaceutics markets are small and have been affected by heavy competition $( U _ { 2 } ^ { d } )$ This is the reason why we are concerned about the debt coverage $( C _ { 3 } ^ { d } ) . \{ A _ { 3 } \colon \bar { U } _ { 2 } ^ { d } \Downarrow C _ { 3 } ^ { d } \}$

Client: $A _ { 4 } \mathrm { : }$ Cortoline, one of our major products, will continue to produce significant revenues $( C _ { 4 } ^ { d } ) _ { . }$ there- ; fore we should not have problems with our debt coverage <sup>d</sup>(C ). <sub>3</sub> $\{ A _ { 4 } \colon C _ { 4 } ^ { d } \ \Uparrow \ C _ { 3 } ^ { d } \} \ A _ { 5 } ;$ Our confidence in Cortoline $( C _ { 4 } ^ { d } )$ is well supported in our decision to keep the . Cortoline line running at full capacity $( C _ { 5 } ^ { d } ) . \ \{ A _ { 5 } \colon C _ { 5 } ^ { d } \ \Uparrow \}$ <sup>d</sup> C }<sub>4</sub>

Auditor: $A _ { 6 } { \mathrm { : } }$ Cortoline sales have declined $( F _ { 1 } ) ;$ this causes concerns about Cortoline’s continuing sales $( C _ { 4 } ^ { d } ) . \{ A _ { 6 } ; F _ { 1 } \downarrow \downarrow C _ { 4 } ^ { d } \} A _ { 7 } \{$ Cortoline’s production costs have increased $( F _ { 2 } ) _ { . }$ , which will again affect Cortoline’s future $( C _ { 4 } ^ { d } ) . \{ A _ { 7 : } F _ { 2 \Downarrow } C _ { 4 } ^ { d } \}$

Client: $A _ { 8 } { \mathrm { : } }$ TDR-42 will be a major source of cashflow $( C _ { 6 } ^ { d } )$ which will improve our cashflow situation . $( U _ { 1 } ^ { d } )$ $\{ A _ { 8 } \colon C _ { 6 } ^ { d } \Downarrow U _ { 1 } ^ { d } \}$

Auditor: $\operatorname { A } _ { 9 } \colon$ Strict FDA rules may affect the approval of TDR-42 which causes concern about the ability <sup>d</sup> (U ). of TDR-42 to be a source of cashflow in future $( C _ { 6 } ^ { d } )$ $\{ A _ { 9 } \colon U _ { 3 } ^ { d } \Downarrow C _ { 6 } ^ { d } \}$

Client: $A _ { 1 0 } { \mathrm { : } }$ The extra effort invested in TDR-42 <sup>d</sup> (C ) should help us in getting FDA approval $( U _ { 3 } ^ { d } ) . \ \{ A _ { 1 0 } \colon$ $C _ { 7 } ^ { d } \Downarrow U _ { 3 } ^ { d } \}$

Auditor: $A _ { 1 1 } { \mathrm { : } }$ Jeldine lab’s new drug could pose direct competition to TDR-42 which may affect cash- <sup>d</sup> (U ), <sub>4</sub> flow expectations from TDR-42 $( C _ { 6 } ^ { d } ) . \{ A _ { 1 1 } \colon U _ { 4 } ^ { d } \Downarrow C _ { 6 } ^ { d } \} A _ { 1 2 } \colon$ Dermaceutics’ top managers are research scientists and lack financial skills $( U _ { 5 } ^ { d } )$ We feel this may affect both . operating performance and debt coverage <sup>d</sup>(C ).<sub>2</sub> $( C _ { 3 } ^ { d } )$ $\{ \bar { A } _ { 1 2 a } \colon U _ { 5 } ^ { d } \Downarrow C _ { 2 } ^ { d } , A _ { 1 2 b } \colon U _ { 5 } ^ { d } \Downarrow ( C _ { 3 } ^ { d } )$

Client: $A _ { 1 3 } { \mathrm { : } }$ We have a good track record; you have, in fact, managed an IPO in the recent past for us $( F _ { 3 } ) ;$ this should allay fears about top management capabilities $( U _ { 5 } ^ { d } ) . \{ A _ { 1 3 } ; ( F _ { 2 } \Downarrow U _ { 5 } ^ { d } \}$

Auditor: $A _ { \mathrm { { 1 4 } } } \mathrm { { : } }$ Jeldine is having problems in getting approval for their product $( F _ { 4 } ) ;$ this may actually favor the cashflow expectations from TDR-42 <sup>d</sup> (C ). $\{ A _ { 1 4 } \colon F _ { 4 }$ ⇑ $C _ { 6 } ^ { d } \} \ A _ { 1 5 } .$ Also, science and trade journals have viewed TDR-42 favorably $( F _ { 5 } )$ . Both the above facts should help TDR-42’s market potential $( C _ { 6 } ^ { d } ) . \{ A _ { 1 5 } ; F _ { 5 } \Uparrow C _ { 6 } ^ { d } \} A _ { 1 6 } ;$ Even though TDR-42 is a high margin product, it is cheaper than the available drugs $( F _ { 6 } )$ . Hence we concede that its market potential may be good $( C _ { 6 } ^ { d } ) . \ \{ A _ { 1 6 } \}$ $F _ { 6 } \Uparrow C _ { 6 } ^ { d } \}$

Client: $A _ { 1 7 } { \mathrm { : } }$ Yes, with TDR-42, we expect to gain a significant market share This should significantly<sup>d</sup> (C ). help us in overcoming the cashflow problems we are currently facing $( U _ { 1 } ^ { d } ) . \{ A _ { 8 } \}$

In both the above examples, we have two parties engaged in a debate due to a conflict in their positions. Consequently, we model the core of a debate process as an exchange between two sets of individuals denoted as the proponent (P) and opponent (O) with regard to a defeasible position A<sup>¨</sup> . We first address a two-person debate game where the sets P and O comprise one individual each, and subsequently show how the gaming model can be extended to multiperson debate games.

Consider a two-person debate game of the type discussed in §3.2. Let $D _ { p }$ and $D _ { o }$ denote the argument structures proposed by P and O, respectively. Hence, $\sigma ( A ) = P \forall A \in D _ { p }$ and $\sigma ( A ) = O \forall A \in D _ { o } .$ . The following definition establishes the rules for conflict between P and O:

Definition 1 (Conflict). In a two person-debate game, P and O are said to be in conflict if $\exists A ^ { p } \in D _ { p }$ and $\exists A _ { o } \in D _ { o }$ such that either $A ^ { { p } } \downarrow \downarrow A ^ { { o } } { \mathrm { o r } } A ^ { { o } } \downarrow \downarrow A ^ { { p } }$

Note from the above definition that $D _ { p }$ and $D _ { o }$ need not be mutually exclusive. For example, the auditor’s assertion in Example 1, $A _ { 2 b } \colon F _ { 2 } \Downarrow C _ { 2 } ^ { d } ,$ causes the client and the auditor to be in conflict. The intersection of $D _ { p }$ and $D _ { o }$ would be the set of all concurring arguments and their differences yield the conflicts, since P and O could concur on some of the assertions and disagree on some others. Based on this, we define a conflict set of the debate as follows:

Definition 2 (Conflict set). The conflict set of a debate $\langle D _ { p } , D _ { o } \rangle$ , denoted as $C ,$ is the union of all the assertions $A ^ { p } \in D _ { p }$ and $A ^ { o } \in D _ { o }$ that satisfy at least one of the conditions of conflict in Definition 1.

For instance, the conflict set for Example 2 after the first exchange of assertions between the client and the auditor $( \mathrm { i . e . , }$ after the auditor makes the assertion $A _ { 3 } )$ is $\{ C _ { 3 } ^ { d } , ~ C _ { 1 } ^ { d } \}$ A debate is a live process and develops . over time. Hence, it is possible for positions to be either upheld or defeated during its course. This is due to the changes in the belief structures of the debating individuals as a result of the discussions. This leads to the following definition:

Definition 3 (Recency of assertion). Let A denote the assertion of an individual at some time t in the debate process. If $A _ { t } \equiv \Gamma \Uparrow ( \Downarrow ) \Gamma _ { d }$ and an earlier assertion $A _ { t - x } \equiv \Gamma \Downarrow ( \Uparrow ) \Gamma _ { d } ,$ for $t , t - x \geq 0$ , then $A _ { t }$ is denoted as the recent assertion, and supercedes $A _ { t - x } .$ Consequently, $A _ { t - x }$ is said to be null and void, and is replaced with $A _ { t - x }$ in $\langle D _ { p } , D _ { o } \rangle$

The stipulation that every assertion in $\langle D _ { p } , D _ { o } \rangle$ satisfies the recency criterion captures the dynamics of the debate process and also eliminates self-contradiction within an individual. We now address the resolution of a debate process as follows:

Definition 4 (Resolution). A debate is said to be resolved if either the conflict set C is empty or if any resolution mechanism c reaches its trigger condition $\zeta ,$ resulting in a debate verdict. A resolution mechanism could be any resolution procedure adopted by the debating individuals, such as timeout, arbitrator decision, jury, etc., from which the final decisions on $\langle D _ { p } ,$ $D _ { o } \rangle$ are generated. The trigger condition invokes the resolution mechanism and brings the debate to a closure.

In the above definition, the resolution mechanisms and their trigger conditions can be mutually devised and agreed upon prior to the debate by the participating individuals. The above resolution components are critical to the development of the debate model described as follows.

3.3. Two-Person Debate: A Procedural Formalism A debate starts with the initial debate structure $\langle D _ { p } ,$ $D _ { o } \rangle$ . In a two-person debate, each structure $D _ { p }$ and $D _ { o }$ represents a structured string of arguments ending with a final concluding defeasible position. While a debate can occur about any defeasible assertion, we consider the argument structures of P and O in their entirety in the following formalism. The conflict set C of $\langle D _ { p } , D _ { o } \rangle$ is said to be the agenda of the debate. The debate is modeled as a sequence of argument steps where, in each step, each of the two parties could: (i) challenge the defeasible assertions of the other with or without introducing new argument logic, (ii) defend a challenged position by introducing new argumentative logic, (iii) simply seek a clarification of a position from the other, or (iv) do nothing, let the opportunity pass, and allow the other to continue. The debate structure would dynamically change and evolve as a result of this. We capture this evolution as follows: Let $d _ { p } ^ { i }$ and $d _ { o } ^ { i }$ denote the argument structures introduced by $P$ and $O ,$ respectively, during Step i of the debate. If no such structure is introduced (as in case [iii] and [iv] above), then the corresponding $d _ { p } ^ { i }$ or $d _ { o } ^ { i }$ is set to empty (-). Let $\langle D _ { p } ^ { i } , D _ { o } ^ { i } \rangle$ denote the overall debate structure that has evolved at the end of Step i. We define the debate structure recursively as follows:

$$
\begin{array}{c} D _ {p} ^ {i} \leftarrow D _ {p} ^ {i - 1} \& d _ {p} ^ {i}, D _ {o} ^ {i} \leftarrow D _ {o} ^ {i - 1} \& d _ {o} ^ {i}, D _ {p} ^ {1} \\ \leftarrow d _ {p} ^ {1} \text {and} D _ {o} ^ {1} \leftarrow d _ {o} ^ {1} \end{array}
$$

The operator $\&$ indicates an update of $D _ { p }$ or $D _ { o }$ through modifications, additions, and deletions caused by the newly introduced $d _ { p }$ or $d _ { o } ,$ respectively.

The debate continues until a condition for resolution is reached. We capture this as the boolean resolution trigger $\zeta ,$ which indicates that the resolution mechanism c is to be activated when $\zeta = \mathrm { T R U E }$ and to allow the debate to proceed when $\zeta = \mathrm { F A L S E }$ . The condition for toggling f is contained in the prior agreement between the debating individuals on when to activate c.

The proposed procedural formalism consists of two components: debating and structure tracking. The debating component captures the exchanges between P and $O ,$ and generates the argument structures $D _ { p }$ and $D _ { o } .$ The structure tracking component maintains and updates the debate structure $\langle D _ { p } , D _ { o } \rangle$ , schedules interactions in the debating component, checks for resolution, and manages the trigger. The two components operate in sequence, and we segregate them by indenting and highlighting the debating component in presenting the formalism. We employ the OR operator | to distinguish the response options to an individual at each step, and denote the ‘‘clarification’’ and ‘‘do nothing’’ options as ? and $\varnothing ,$ respectively. The procedural formalism of the two-person debate process is given in Figure 2.

3.3.1. Multi-Person Debates: A Generalization. The above model of a two-person debate can be generalized to a multiperson debate as follows: Recall that each debating individual acts as either the proponent or the opponent of a defeasible assertion in a twoperson game. Consequently, each defeasible assertion has a unique signature. Hence, the entire argument structure, D, can be divided into three mutually exclusive sets of assertions based on the signatures: the assertion set of the first individual (which is contested by the second), the assertion set of the second (which is contested by the first), and possibly, a third set on which both agree. The first two sets are essentially the basis for the debate. However, in a multiperson debate, there can be a unique set of proponents, opponents and neutral members surrounding each defeasible assertion. Consequently, several different debates can occur concurrently, with a defeasible assertion as the focal point of each debate. While each such debate could entail several debating individuals organized into P (proponents), O (opponents), and N (neutral members), an individual could participate in any one of

## Figure 2 The Debate Process

```vhdl
Step ← 1; { Initialize debate }
ζ ← FALSE; { Set resolution trigger }
<\(D_p^0, D_o^0\)> ← <∅,∅>; { Initialize debate structure }

P: \(d_p^1\) { Initial proponent argument structure }
\(D_p^1\) ← \(D_p^0\) & \(d_p^1\); { Initialize \(D_p\)}

O: \(d_o^1 \Downarrow D_p^1\) | ? \(D_p^1\); { Opponent's initial challenge|question }
\(D_o^1\) ← \(D_o^0\) & \(D_o^1\); { Initialize \(D_o\})

Step ← 2;
While { C ≠ ∅ | O: ? \(D_p^{step-1}\) | P: ? \(D_o^{step-1}\) | [(\(D_p^{step-1} \neq D_p^{step-2}\)) ∩ (\(D_o^{step-1} \neq D_o^{step-2}\)) ] }
Begin
P: [\(d_p^{step}\) ∃ { \(d_p^{step} \Downarrow D_o^{step-1}\) | \(d_p^{step} \Uparrow D_p^{step-1}\)}]
? \(D_o^{step-1}\)
: ∅

O: [\(d_o^{step}\) ∃ { \(d_o^{step} \Downarrow D_p^{step-1}\) | \(d_o^{step} \Uparrow D_o^{step-1}\)}]
? \(D_p^{step-1}\)
: ∅

\(D_p^{step}\) ← \(d_p^{step}\) & \(D_p^{step-1}\); { Update \(D_p\)}
\(D_o^{step}\) ← \(d_o^{step}\) & \(D_o^{step-1}\); { Update \(D_o\})

Test ζ;
If (ζ = TRUE) Then
    Activate γ;
    Stop Debate
Else
    Step ← Step + 1;
End;

End;
```

these capacities in several debates. The structure of each such debate is basically the same as that of a twoperson debate, with the following differences, however: Each debate could involve several proponents and opponents as opposed to unique proponent and an opponent in the two-person games, and could involve neutral parties. In this case, by identifying the sets $P , O ,$ and N for each debate, and allowing the neutral members to raise questions as the opponents and add insights to a discussion, the same model of a twoperson debate can be adapted to the multiperson discussion. However, scheduling such concurrent debates and maintaining a focus in the discussions become much more critical than in two-person debates. Therefore, it is necessary to identify an overall agenda of focal assertions over which the debates are to be conducted and to maintain the focus throughout the debate process. Given such an agenda, each debate in the agenda can be conducted along the lines of an adapted two-person debate as described above, leading to an overall resolution of the discussion agenda. We develop a connectionist paradigm to provide intelligent system support at each stage of a debate process in the following discussion.

## 4. Collaboration Support: A Connectionist Paradigm

During the process of collaborative decision making, the argument logic along with the assertions and facts can grow significantly. This necessitates providing computational support to the group members involved in collaborative decision making. With proper computational support, it is possible to analyze the discussion and arrive at an assessment of the strengths and weaknesses of the various positions contained in it. Such assessments can be carried out dynamically as the discussion evolves. In this context, we develop a connectionist approach to argument analysis as a form of computational support for collaborative decision making.

In the following sections, we first propose a connectionist network formalism and map the argumentation formalism of the previous section to this connectionist network. A computational model of the connectionist constructs is then presented from an argumentation perspective. Subsequently, examples of argumentative decision making are presented and analyzed to evaluate the intuitive validity of the connectionist network formalism.

## 4.1. The Connectionist Formalism

We define a connectionist network in graph theoretic terms as follows:

Definition 5 (Connectionist Network). A connectionist network is defined as a 4-tuple: $\Sigma = \langle N , a _ { N } , A _ { \scriptscriptstyle { M } }$ $W _ { A } )$ where, N denotes the set of connectionist units, $a _ { N } .$ $N  \Re$ is a real valued activation function that maps each element of N to a real number, A is the set of directed arcs $W _ { A } \colon A \to \Re$ is a real valued arc weight function that maps A to a real number.

Given the above definition of a connectionist network we can define an argument network as a mapping of the argumentation system D to a connectionist network R as follows:

Definition 6 (Argument Network). An argument network is a mapping of an argumentation system D to a connectionist network R. The $\langle S , R , Q \rangle$ framework is translated to the connectionist formalism by mapping S- to $\langle N , a _ { N } \rangle$ , and $\left. R , Q \right. \tan \left. A , W _ { A } \right.$ . We represent the sentences (C) of the sentence structure (S ) of an argument as units in the argument network. Two types of units are defined corresponding to the type of sentence they represent. Defeasible sentences $( \Gamma _ { d } )$ are represented as defeasible units $( N _ { d } )$ and factual sentences $( \Gamma _ { F } )$ are represented as factual units $( N _ { F } )$ in the network. In addition, logical connectives (such as $\wedge , \vee$ are represented using logical units $( N _ { L } )$

Factual sentences and defeasible sentences differ in their activation level assignments in the argument network. Similarly, logical units express their behavior by their specific activation level assignments. We illustrate this as follows:

Define $a _ { N } = \{ a _ { N } ^ { d } , a _ { N } ^ { F } , a _ { N } ^ { L } \}$ where $a _ { N } ^ { d }$ is the activation function for $N _ { d } , a _ { N } ^ { F }$ is the activation function for $N _ { \mathrm { F } } ,$ and $a _ { N } ^ { L }$ is the activation function for $N _ { L }$ . Each qualification type from the qualification structure Q, namely, defeasible support, defeasible opposition, strict support, and strict opposition, is mapped to a corresponding arc type in the connectionist network. The set of directed arcs is defined as ${ \cal A } = \{ A ^ { \Uparrow } , A ^ { \Downarrow } , A ^ { \uparrow } , A ^ { \downarrow } \}$ , where $A ^ { \Uparrow }$ represents defeasible support, $A ^ { \Downarrow }$ represents defeasible opposition, $A ^ { \uparrow }$ represents strict support, and $A ^ { \downarrow }$ represents strict opposition. Each arc type may have a different weight assignment function. We define the weight assignment function $W _ { A }$ as ${ \cal W } _ { A } \ = \ \{ { \cal W } _ { A } ^ { \Uparrow }$ <sup>⇓</sup>  <sub>A</sub> , W , $W _ { A } ^ { \uparrow } , ~ W _ { A } ^ { \downarrow } \}$ where, ${ W } _ { A } ^ { \Uparrow }$ is the arc weight function for $A ^ { \Uparrow }$ $W _ { A } ^ { \Downarrow }$ is the arc weight function for $A ^ { \Downarrow }$ $W _ { A } ^ { \uparrow }$ is the arc weight function for $A ^ { \uparrow } ,$ , and $W _ { A } ^ { \downarrow }$ is the arc weight function for A<sup>f</sup>.

Sentences that make use of logical connectives to combine different defeasible and factual sentences are termed compound sentences. Compound sentences are transformed into a connectionist network with the logical node $( N _ { L } )$ as the resultant unit for that sentence in accordance with the following definition. Consider a compound sentence of the form $( \Gamma _ { a } \mathrm { \bf ~ X } \Gamma _ { b } ) ,$ where $\Gamma _ { a }$ and $\Gamma _ { b }$ can be defeasible or factual sentences or compound sentences, and V is a logical connective (and, or). The connectionist mapping of this sentence is defined as follows:

$D { \because } ( \Gamma _ { a } \mathrm { X } \Gamma _ { b } ) \to N _ { L }$ such that $N _ { L } \in \Sigma \ = \ < \ \{ N _ { a } , \ N _ { b } , \ N _ { L } \} .$

$$
\{a _ {N} ^ {a}, a _ {N} ^ {b}, a _ {N} ^ {L} \}, \{A ^ {\uparrow} (N _ {a}, N _ {L}), A ^ {\uparrow} (N _ {b}, N _ {L}) \}, \{W _ {A} ^ {\uparrow}, W _ {A} ^ {\uparrow} \} >
$$

The above mapping implies that a compound sentence is transformed into an equivalent connectionist network. This connectionist network consists of two units that represent the two disjoint sentences being connected and an additional logical unit that is linked to these two units through an arc of type strict support.

We can use the connectionist mapping to map the argument structures of the mortgage loan and the going concern examples discussed in Section 3 to corresponding argument networks. The resulting argument network and the unit descriptions for Example 1 are shown in Figure 3 and Table 1 respectively. The corresponding information for Example 2 is in Figure 4 and Table 2.

The above definitions lay the foundation for the connectionist modeling of arguments. These definitions provide a one-one mapping from the argumentation formalism to a connectionist formalism. This formalism is further refined in the following sections for argument evaluation purposes. We develop the connectionist modeling framework using the above formalisms as follows.

## 4.2. The Modeling Framework

While the logical structure of the arguments is captured by the argument network formalism, the argument evaluation mechanisms are captured in the connectionist framework. The connectionist framework can be used to assess the validity and acceptability and can implicitly represent the value of their informational content and logical coherence of the arguments. We develop the connectionist model in the following discussion.

In the connectionist model, each unit is associated with an activation level that ranges between 1 and

Figure 3 Argument Network for the Mortgage Loan Example  
![](/api/attachments/Y6W7T9UQ/fulltext/images/5d4db0e212ab4bb8df5156ec7e7120e3023129bd8eef9abe36550ea519dace62.jpg)

Information Systems Research Vol. 12, No. 4, December 2001

1. The activation level of a unit is a measure of its validity. Activation values closer to 1 indicate strongly supported arguments with relatively high validity. Similarly, values closer to 1 represent strongly refuted arguments, while values closer to 0 indicate ambiguous cases that need further investigation. An arc from a unit $p$ to a unit $q$ transmits an amount of activation to $q$ that is proportional to that of $p .$ This transmission is computed by using weights associated with the arcs. The nature of the relationships contained in the arcs determines these weights. Strict and defeasible support arcs transmit excitatory or positive activation, while strict and defeasible opposition arcs transmit inhibitory or negative activation. As a result, an excitatory activation would enhance the activation

Figure 4 Argument Network for the Going Concern Example  
![](/api/attachments/Y6W7T9UQ/fulltext/images/8971b45d415b0507cdd2f1812c2f5db9a9049b237bc9c56ba5df15e91a2a2658.jpg)

Table 1 Meanings of the Network Units in Example 1

<table><tr><td>Unit</td><td>Meaning</td></tr><tr><td> $C_1^d$ </td><td>Mortgagee&#x27;s financial condition is good.</td></tr><tr><td> $C_2^d$ </td><td>The mortgaged loan is collectible.</td></tr><tr><td> $C_3^d$ </td><td>Bankruptcy is filed for planned reorganization.</td></tr><tr><td> $C_4^d$ </td><td>Realty value of the mortgage is sufficient to cover the loan.</td></tr><tr><td> $C_5^d$ </td><td>Decline in realty values is only temporary.</td></tr><tr><td> $U_1^d$ </td><td>Economic conditions are going to keep the realty value down.</td></tr><tr><td> $F_1$ </td><td>Mortgagee is a secured creditor.</td></tr><tr><td> $F_2$ </td><td>Mortgagee has filed for bankruptcy.</td></tr><tr><td> $F_3$ </td><td>Mortgagee has defaulted on other interest payments.</td></tr><tr><td> $F_4$ </td><td>Market share of the mortgagee has dropped 60%.</td></tr><tr><td> $F_5$ </td><td>Realty value of the mortgaged property has declined.</td></tr><tr><td> $F_6$ </td><td>Realty values are increasing in the geographic area.</td></tr></table>

Table 2 Meanings of the Network Units in Example 2

<table><tr><td>Unit</td><td>Meaning</td></tr><tr><td> $C_{1}^{d}$ </td><td>Dermaceutics is a going concern.</td></tr><tr><td> $C_{2}^{d}$ </td><td>Operating Performance of Dermaceutics is good.</td></tr><tr><td> $C_{3}^{d}$ </td><td>Dermaceutics has adequate debt coverage.</td></tr><tr><td> $C_{4}^{d}$ </td><td>Cortoline&#x27;s market future is bright.</td></tr><tr><td> $C_{5}^{d}$ </td><td>We will keep Cortoline line at full capacity.</td></tr><tr><td> $C_{6}^{d}$ </td><td>TDR-42 can generate enough cashflows.</td></tr><tr><td> $C_{7}^{d}$ </td><td>Dermaceutics has expended extra effort in checking the process and safety of TDR-42.</td></tr><tr><td> $U_{1}^{d}$ </td><td>There seems to be a low ratio of uncommitted cash flows.</td></tr><tr><td> $U_{2}^{d}$ </td><td>Dermaceutics&#x27; markets are small and are affected by heavy competition.</td></tr><tr><td> $U_{3}^{d}$ </td><td>FDA approval for TDR-42 may be affected by strict FDA rules.</td></tr><tr><td> $U_{4}^{d}$ </td><td>Jeldine&#x27;s new drug may pose direct competition to TDR-42.</td></tr><tr><td> $U_{5}^{d}$ </td><td>Dermaceutics&#x27;s top managers are research scientists and lack financial skills.</td></tr><tr><td> $F_{1}$ </td><td>Cortoline sales have declined.</td></tr><tr><td> $F_{2}$ </td><td>Cortoline&#x27;s production costs have increased.</td></tr><tr><td> $F_{3}$ </td><td>Dermaceutics recently carried out an IPO.</td></tr><tr><td> $F_{4}$ </td><td>Jeldine is having problems in getting approval for their product.</td></tr><tr><td> $F_{5}$ </td><td>Science and trade journals have viewed TDR-42 favorably.</td></tr><tr><td> $F_{6}$ </td><td>TDR-42 is cheaper than available drugs.</td></tr></table>

of the receiving unit from its current level, and an inhibitory activation would decrease it. The strength and sign (opposition or inhibitory) of this transmission is controlled by the weights. A strict support (opposition) arc transmits greater excitatory (inhibitory) activation than a defeasible support (opposition) arc. Thus, the activation level of a unit at any time is a function of the sum total of the activations it receives through its input arcs and its own current activation level. In this model, the activation levels of only the defeasible units are allowed to change over time. The activation of a fact unit is set to the value 1 since facts are treated as indisputable and accepted by all.

The operations of the connectionist mechanisms are as follows: Initially, all defeasible units are assigned an activation value close to zero, and all fact units are fixed at the value 1. The support arcs carry positive weights with strict weights greater than the defeasible weights. The opposition arcs carry negative weights with strict weights less than the defeasible weights. The exact values of the initial unit activation assignments and arc weights are system parameters, and can be altered to suit any desired configuration. Starting from the initial assignment configuration, the entire model propagates the activations over time. The entire set of transmissions is discretized into time slices denoted as $t _ { 1 } , t _ { 2 } , \ldots t _ { \infty } ,$ , where the activation levels at any time t determine the activation levels at time $( t ~ + ~ 1 )$ Furthermore, the activation level of a unit is modeled to decay during a time slice according to a decay factor, which captures the time-dependent neuronal decays in human cognition. The rate of decay is also a system parameter and can be chosen at any desired level. The model updates the activation levels continuously in cycles corresponding to the time slices until a prespecified number of time slices have elapsed or the activation levels of all the units have asymptotically converged to some values. The final activation level of a unit is a measure of its dialectical power. If a unit is the final conclusion of an individual, its activation level measures the dialectical power of that individual’s argument. The computational model underlying the connectionist analysis and its algorithmic implementation are developed as follows.

4.2.1. The Computational Model To begin with, we develop basic models for the computation of the activation levels of individual units in the connectionist algorithm. Subsequently we address specific connectionist constructs required for argument evaluation.

Let $( i , j ) \in A$ denote an arc from unit i to unit j in an argument network R. Let $w _ { i j }$ denote the weight associated with arc $( i , j )$ . Let $t = 1 , \ldots , \infty$ denote the discretized time slices, and $a _ { i } ( t )$ denote the activation level of unit i at time t. The arc weights are time invariant, fixed value parameters, while the activation levels are temporal variables. The activation levels of all the units are initialized at some parametrically chosen values $a _ { i } ( 0 ) , \forall i \in N .$ . The activation levels are set according to factual superiority as defined below.

## Factual Superiority

Factual sentences in an argument have higher intrinsic dialectical value over defeasible sentences. Factual units therefore should have higher activation levels than defeasible units in an argument network. This stipulation is specified by the condition: $a _ { m } \geq a _ { n } \ \forall$ m $\in N _ { F } ,$ and $n \in N _ { d } ,$ and $- 1 \leq a _ { n } \leq 1$ . The activation levels of factual units are set as follows: $a _ { i } ( t ) = 1 \forall i \in$

$N _ { F } ,$ ∀t. An implicit notion of this principle is the commonly observed phenomenon that an argument, however detailed and intricate it may be, is well grounded if it is supported by as many indisputable facts as possible.

Starting from the initial conditions, the connectionist algorithm updates the activation levels of all the defeasible units in each time slice as follows. Consider a defeasible unit $j \in N _ { F }$ . Let $\mathcal { M } _ { i } \in N$ denote the set of units such that an arc $( i , j )$ exists in R for all $i \in { \mathcal { M } } _ { j } .$ Each such arc can be any of the four types as discussed earlier. Arc weight assignment is made based on the following two heuristics.

## Power of Reasoning

Strict reasoning is a result of logical inference that is not disputed by anyone in a group. Defeasible reasoning, on the other hand, is subject to debate and possibly defeat. Therefore, strict reasoning is considered superior to defeasible reasoning. For this reason, the following condition is defined for arc weight assignment: $W _ { A } ^ { \uparrow } \ge W _ { A } ^ { \Uparrow }$ and $\mid W _ { A } ^ { \downarrow } \mid \ge \mid W _ { A } ^ { \downarrow } \mid$ The above condition. distinguishes the difference in the power of reasoning by assigning a higher weight to logical reasoning as compared to defeasible reasoning.

## Support Versus Opposition

Individuals in an argument present supporting assertions to strengthen their argument positions. Similarly, individuals challenge the argument positions of their opponents by presenting opposing assertions. Thus, supporting inference structures should provide excitatory links in an argument network, and opposing inference structures should provide inhibitory links in an argument network. This condition is captured as follows: $W _ { A } ^ { \uparrow } , W _ { A } ^ { \Uparrow } \in \mathfrak { R } ^ { + }$ , and $W _ { A } ^ { \downarrow } , W _ { A } ^ { \downarrow } \in \mathfrak { R } ^ { - }$ . The above definition implies that arc weights of strict and defeasible support arcs are positive and arc weights of strict and defeasible opposition arcs are negative. These definitions lead to the following relationship between the arc weights.

$$
- 1 \leq W _ {A} ^ {\downarrow} \leq W _ {A} ^ {\Downarrow} \leq 0 \leq W _ {A} ^ {\uparrow} \leq W _ {A} ^ {\uparrow} \leq 1
$$

The activation level of a defeasible unit j at time t is determined from (i) the activation level of j at time (t  1), (ii) the activation of each $i \in \mathcal { M } _ { j }$ at time $\left( t - 1 \right)$

(iii) the weights along the arcs $( i , j ) , \forall i \in { \mathcal { M } } _ { j } ,$ and (iv) a decay factor d, as defined below.

Activation Levels of Defeasible Units

Let $\alpha _ { j } ( t \textrm { -- } 1 ) = \Sigma _ { i \in m _ { j } } w _ { i j } a _ { i } ( t \textrm { -- } 1 )$ . Then:

$$
a _ {j} (t) = \left\{ \begin{array}{l} \text {Min} \{1, a _ {j} (t - 1) [ 1 - \delta ] + a _ {j} (t - 1) \\ [ 1 - a _ {j} (t - 1) ] \} \text {if} a _ {j} (t - 1) > 0 \\ \text {Max} \{- 1, a _ {j} (t - 1) [ 1 - \delta ] + a _ {j} (t - 1) \\ [ 1 + a _ {j} (t - 1) ] \} \text {if} a _ {j} (t - 1) <   0 \end{array} \right.
$$

The above model of computation ensures that the activation levels always lie between 1 and 1. The decay parameter shows that the activation loses its strength by a fraction $0 \leq \delta < 1$ in each time slice. The value of d indicates the memory power of each neuronal unit, and can be chosen anywhere in the range provided. If $\alpha _ { j } ( t \textrm { -- } 1 ) > 0 ,$ then unit j receives positive or excitatory net input, and if $\alpha _ { j } ( t \textrm { -- } 1 ) < 0 ,$ , then the net input is inhibitory. The above model also reflects the following connectionist behavior. As a unit becomes increasingly stronger, any further positive input will have a decreasing influence on it, and if negative inputs arrive, then they will have an increasing influence. Similarly, if a unit becomes increasingly weaker, then positive inputs can revive it much more effectively while the results of further negative inputs tend to be increasingly marginal.

Now, consider the case of logic units in an argument network. Such units are handled by using the strict support arcs as described earlier. We develop models for updating the activation levels of logical units during the connectionist cycles as follows.

## Logical Unit Computations

Let a unit $j \in N ,$ be a logical unit of type AND that combines a set of units $\mathcal { M } _ { j } \in N .$ In Boolean logic, AND requires that all inputs must be true for the output to be true. However, in the connectionist model, unit activation levels vary continuously between 1 and 1. Therefore, using the Boolean system, we define the activation of unit j at time t as the minimum of the activation levels of the units in $\mathcal { M } _ { j }$ at time $\left( t \mathrm { ~ - ~ } 1 \right)$ . Therefore, $a _ { j } ( t ) =$ Minimum $( a _ { i } ( t - \bar { 1 } ) \forall i \in \mathcal { M } _ { i } )$

Further, let a unit $j \in N \vee$ be a logical unit of type OR that combines a set of units $\mathcal { M } _ { j } \in N .$ In Boolean logic, OR requires that at least one of the inputs be true for the output to be true. However, in the connectionist model, unit activation levels vary continuously between 1 and 1. Therefore, using the Boolean system, we define the activation of unit j at time t as the maximum of the activation levels of the units in $\mathcal { M } _ { j }$ at time $\left( t - 1 \right)$ . Therefore, - Maximum<sup>4</sup> a (t) $( a _ { i } ( t - 1 )$ ∀i $\in \mathcal { M } _ { j } )$

## Argument Simplicity

We now introduce the concept of Argument Simplicity. An assertion A that depends on fewer other assertions for its sustenance than another assertion B is considered to be the simpler of the two. While this is one such measure of simplicity, other interpretations of simplicity could also be employed. A simpler argument is generally a more favored argument structure. This is also a commonly observed phenomenon in practice, where an assertion built on too many other assertions (possibly, without enough factual support) is more vulnerable to attack than another that is based more on facts and less on other assertions. Similarly, individuals opposed to an assertion would do well if they raise a few meaningful defeasible challenges rather than a large number of challenges. Clearly, favoring simpler arguments would discourage individuals from spinning complex, and possibly unnecessary, arguments. This would foster focused discussions leading to faster resolutions.

This concept is implemented as detailed in the definition below. Consider a unit j and the set $\mathcal { M } _ { j }$ as before. The set $\mathcal { M } _ { j }$ could contain units that provide either support or opposition to unit $j .$ Accordingly, we partition $\mathcal { M } _ { j }$ into two sets $\mathcal { M } _ { j } ^ { + }$ and $\mathcal { M } _ { j } ^ { - }$ We normalize the. weights along the arcs $( i , j ) \forall i \in { \mathcal { M } } _ { j }$ using these partitions as follows.

$$
w _ {i j} \leftarrow \frac {w _ {i j}}{| \mathcal {M} _ {j} ^ {+} |}, \text {   if   } i \in \mathcal {M} _ {j} ^ {+}
$$

$$
w _ {i j} \leftarrow \frac {w _ {i j}}{| \mathcal {M} _ {j} ^ {-} |}, \text {   if   } i \in \mathcal {M} _ {j} ^ {-}
$$

$( \mid \mathcal { M } _ { j } ^ { + } \mid$ represents the number of units in the set $\mathcal { M } _ { j } ^ { + }$ and, $\mid \mathcal { M } _ { j } ^ { - }$ represents the number of units in the<sup></sup>| set $\mathcal { M } _ { j } ^ { - } . )$ This simple normalization relatively decreases the effective weight of an arc by the number of similar other arcs issuing from ${ \mathcal { M } } _ { j } \mathrm { t o } j .$

The following section provides the connectionist algorithm that utilizes the computational models described above. In the algorithm, the asymptotic change value (e) is used for terminating the algorithm within the stipulated number of cycles when the activation level of the defeasible units levels off. If none of the defeasible units change the activation level by more than $\varepsilon ,$ the algorithm terminates.

The algorithm in Figure 5 implements the computational model described in §4.2.1. and formalizes the computational framework presented earlier in §4.2.

## 4.3. Resolution Mechanisms

The connectionist mechanisms described in the previous section enable decision makers to assess the relative strengths of assertions made during a discussion process. However, in order to bring a closure to the discussion, group members have to agree upon a resolution mechanism. A number of resolution mechanisms can be utilized in conjunction with the connectionist argument networks. The choice of the resolution mechanism to be used for a particular decision-making problem, however, is left to the group. As described earlier, the activation levels of the defeasible units are indicators of the dialectical strength of the assertions. In the course of a discussion, several such defeasible assertions may be made; the activation levels of the corresponding units determine how well the defeasible assertions are supported or opposed by the members during the discussion. Given a distribution of dialectical powers in an argument network, several resolution mechanisms can be used to make positional assessments as well as bring closure to the discussion procedure. Some of the well-known resolution mechanisms in the literature are Winner Takes All, Maximum Total Dialectical Power, Maximum Number of Winning Positions, and Maximum Mean Dialectical Power (Vreeswijk 1992). An analysis of these mechanisms is beyond the current scope of this work. In general, resolution mechanisms have to be determined by a group, and the proposed framework simply provides assessments of the various positions at any stage of a discussion, and thus, leads to ultimate resolutions as may be agreed by the group.

In the next section we provide results of computational analyses of the two examples discussed in this section.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Figure 5 Algorithm for Computing Activation Levels
Algorithm : ACME /* Argumentative analysis by a Connectionist Modeling Environment */
Input : The Network $\Sigma = &lt;N, a_N, A, W_A&gt;$,
    The decay parameter $\delta$,
    The maximum number of cycles T,
    The initial activation levels $a_i(0), \forall i \in N$,
    and the asymptotic change value, $\varepsilon$.
Output : The final activation levels $a_i(T), \forall i \in N$
Begin
    Set $a_i(0) = 1$ $\forall i \in N_F$;
    compute_activation_levels( );
    print activation levels $a_i(T), \forall i \in N$;
End;
Procedure compute_activation_levels( );
Begin
    Set t := 1;
    asymptotic_change := TRUE
    While (t ≤ T .and. asymptotic_change = TRUE) Do
    Begin
    asymptotic_change := FALSE;
    For all j ∈ N Do
    Begin
    If j ∈ $N_L$ then
    Compute new activation level.
    Else If j ∈ $N_d$ then
    Form the sets $\mathcal{M}_j^+$ and $\mathcal{M}_j^-$;
    Compute $\alpha_j(t-1)$ using $\mathcal{M}_j^+$ and $\mathcal{M}_j^-$;
    compute $a_i(t)$ using $\delta$, $\alpha_j(t-1)$ and $a_i(t-1)$;
    if (($a_i(t) \sim a_i(t-1)$) ≥ $\varepsilon$) then
    asymptotic_change := TRUE;
    End;
    t = t + 1;
    End;
    End;
    End;
End;
</div>

## 5. Computational Analysis

In this section, the mortgage loan and the going concern debates of the previous section are used in a computational study to illustrate the connectionist behavior. We first summarize our overall observations from a parametric analysis of connectionist networks. Next, we address computational results on the above two examples.

## 5.1. Parametric Analysis of Connectionist Networks

The parameters that can be varied in the connectionist model are (1) the weight of the defeasible arcs, (2) the value of the decay parameter, (3) the initial values of the defeasible units, (4) the number of time cycles, and (5) the asymptotic change value (which is used to stop the cycles).

The parameters for the asymptotic change value and the number of time cycles affect the asymptotic convergence of the defeasible units. We tested the connectionist models for a number of different combinations of these two parameters. While the parameters had an effect on the length of the runs, they had almost negligible effect on the final activation levels of the defeasible units (except at extremely low values). Both parameters’ values should be set to values such that the connectionist models run for a sufficient length of time to attain the steady state values. For this reason, the parameters are set to the following values: Asymptotic Change Value: 0.0001; Number of Time Cycles: 50. Our tests show that the asymptotic change values in the range of 0.001 to 0.0001 are enough to limit the number of time cycles below 100. Higher change values can reduce the number of time cycles substantially. Our tests also show that the number of time cycles should ideally be between 30 and 100.

The decay parameter (d) determines how fast a defeasible unit loses its activation level value with each time cycle. A high value of d will make the defeasible units rapidly lose their activation levels. We carried out computations with the decay parameter value set between 0.05 and 0.5 at 0.05 increments. The value of the decay parameter has an effect on the number of cycles. The number of cycles decrease as the decay rate is increased. Since it is desirable to run the connectionist model for a longer duration to let the unit activation levels settle down, a smaller value of decay parameter is more suitable. For this reason, the decay parameter value for the subsequent experiments is fixed at 0.1.

Defeasible units are initialized to an activation level of less than 1. In this experimental scenario, we fixed the other parameters and varied the initial activation level of the defeasible units between 0.05 and 1.0. We find that the final activation level of the units is independent of initial activation levels. The activation level of a defeasible unit is dependent to a large extent on the factual units supporting or opposing it; thus, the activation levels are largely independent of their initial values.

Defeasible arc weights transmit a portion of the activation values from factual and other defeasible units to a defeasible unit. Hence it is reasonable to expect that the magnitude of defeasible arc weights will have a role to play in the final activation levels reached by the defeasible units. We varied the defeasible arc weights between 0.05 and 1.0. For each setting, we recorded the final activation levels of the defeasible units. Figure 6 presents the results of this experiment for examples 1 and 2. The graphs show that the defeasible arc weights affect the final activation levels. We observe that the activation level of $C _ { 2 } ^ { d }$ (which represent the client’s main thesis) decreases steadily with increasing defeasible arc weight. In contrast, we observe that the activation level of (from example 2) increases<sup>d</sup> C steadily with increasing defeasible arc weight.

## 5.2. Analysis of Example 1

We have plotted the activation level of the client’s main thesis after each stage of the argumentation process in Figure 7. In each stage, we compute the activation levels for the nodes in the argument network that is built based on the assertions made up to that stage. For instance, after the auditors’ attack against $C _ { 1 } ^ { d }$ and $C _ { 2 } ^ { d }$ using facts $F _ { 1 }$ and $F _ { 2 } ,$ the activation level of the client’s main thesis drops to 0.8. The client’s counterargument based on unsupported assertions lifts the activation level in the next stage only slightly. However, the client’s main thesis is overwhelmingly defeated well before the end of the discussion.

Figure 6 Effect of Defeasible Arc Weights on Final Activation Level Example 1  
![](/api/attachments/Y6W7T9UQ/fulltext/images/970dfb40738162f55578b01ce70cdd76e7b3934f012f01abc835eb0b10e89f16.jpg)

Example 2  
![](/api/attachments/Y6W7T9UQ/fulltext/images/baf73ec1a48e2e66a491565a0f69b9e1f73e3baa3a397ea0406298a58980244a.jpg)  
Information Systems Research Vol. 12, No. 4, December 2001

Figure 7 Activity Level at Each Stage of the Debate Process in Example 1  
![](/api/attachments/Y6W7T9UQ/fulltext/images/ad041f92b294e1bc1c6f77383923353965bef328696eb4d01f1a2448be9c6e11.jpg)

All the defeasible units of the client’s arguments, except $C _ { 5 } ^ { d } ,$ settle to activation levels between 0.4 and 0.85 (see Table 3 below). Since a majority of defeasible assertions are below zero, we conclude that the client’s entire argument is very weak, and does not have adequate factual or other basis for support. Furthermore, the auditors challenge these assertions with substantial factual support. Note that while only the fact $F _ { 6 }$ lends direct support to the client’s position, all other facts are in opposition (except $F _ { 1 } ,$ which forms part of a logical assertion and does not provide any direct support). The connectionist model clearly reflects this situation. In the role of an impartial assessor, the model highlights the weaknesses in the client’s argument.

Further, we observe from Figure 6 that the activation level of $C _ { 2 } ^ { d }$ decreases steadily with increasing defeasible arc weight. The range of activation level values is between 0.3 and 0.9. Thus, over the entire range of defeasible arc weights, the client’s main thesis has negative activation level. This indicates that the argument against the client’s main thesis is strong. Based on the above analysis, we can conclude that the client’s argument supporting the assertion that the mortgage loan of \$5 million can be reported as receivables is weak. The auditors, armed with an array of facts, seem to have a strong argument against the client’s claim.

Table 3 Final Activation Levels of the Defeasible Units in Example 1

<table><tr><td>Unit Name</td><td> $U_1^d$ </td><td> $C_5^d$ </td><td> $C_3^d$ </td><td> $C_4^d$ </td><td> $C_1^d$ </td><td> $C_1^d \wedge F_1$ </td><td> $C_2^d$ </td></tr><tr><td>Final Activation Level</td><td>0.0001</td><td>0.714</td><td>-0.833</td><td>-0.417</td><td>-0.825</td><td>-0.825</td><td>-0.789</td></tr></table>

Figure 8 Activity Level at Each Stage of the Debate Process in Example 2  
![](/api/attachments/Y6W7T9UQ/fulltext/images/804797ccdc9e5a1e89f7a005ccaef2fbdf5e6746dd885b7ae8c9e0bc477564bc.jpg)

## 5.3. Analysis of Example 2

We have plotted the activation level of the client’s main thesis after each stage of the argumentation process in Figure 8. The initial stages of the arguments do not contain any facts, and therefore the activation level of $C _ { 1 } ^ { d } ,$ the main thesis of the client, is neutral. When the auditor presents the facts $F _ { 1 }$ and $F _ { 2 } ,$ the activation level drops to around 0.6. The activation level remains negative till the client presents fact $F _ { 3 } ;$ thereafter, the activation level of $C _ { 1 } ^ { d }$ remains positive. This example shows how an argument’s strength can switch from one party to another over the course of the debate process.

Example 2 differs from Example 1 in that the client’s positions end up being supported by the facts. The client’s final thesis that Dermaceutics is a going concern $( C _ { 1 } ^ { d } )$ achieves a dialectical power close to 0.7 (see Table 4 below). Further, while $\{ \hat { C } _ { 2 } ^ { d }$ and $C _ { 6 } ^ { d }$ achieve positive activation, the rest of the propositions are at negative or near zero activation level. The client’s assertion that Cartolene will continue to produce significant revenues $( C _ { 4 } ^ { d } )$ is defeated primarily due to the fact that Cartolene’s sales are declining $( F _ { 1 } )$ , and Cartolene’s production costs have increased $( F _ { 2 } )$ . Figure 6 can again be used to investigate the behavior of the connectionist model of example 2 with respect to changes in the arc strength parameter. From Figure 6 we notice that the connectionist model again exhibits a monotonic behavior with respect to arc weight variation. The activation level of the client’s main thesis raises from near zero to a value of close to 0.9. Thus, client’s main thesis is not defeated over the entire range of defeasible arc weights. It is possible to conclude from this analysis that the argument is leaning towards the client’s main thesis. However, the client may wish to provide additional supporting arguments to strengthen the assertion that the debt coverage is adequate . <sup>d</sup> (C )

Table 4 Final Activation Levels of the Defeasible Units in Example 2

<table><tr><td>Unit Name</td><td> $U_{5}^{d}$ </td><td> $U_{4}^{d}$ </td><td> $U_{3}^{d}$ </td><td> $U_{2}^{d}$ </td><td> $U_{1}^{d}$ </td><td> $C_{7}^{d}$ </td><td> $C_{6}^{d}$ </td><td> $C_{5}^{d}$ </td><td> $C_{4}^{d}$ </td><td> $C_{3}^{d}$ </td><td> $C_{2}^{d}$ </td><td> $C_{1}^{d}$ </td></tr><tr><td>Final Activation Level</td><td>-0.83</td><td>0.0</td><td>-0.001</td><td>0.0</td><td>-0.78</td><td>0.0</td><td>0.75</td><td>0.0</td><td>-0.77</td><td>0.096</td><td>0.806</td><td>0.68</td></tr></table>

One intriguing aspect of this example is that some of the facts provided by the auditors actually favor the client (facts $F _ { 4 } , F _ { 5 } ,$ and $F _ { 6 } )$ . This is an example of a scenario where the two debating teams are not suppressing facts from each other, even when the facts may adversely affect their (in this case, the auditors’) assertions.

## 6. Concluding Remarks and Future Research

We have developed the core concepts of a dialectical support system based on a connectionist paradigm that can be used to analyze collaborative discussions. Our experiments with the connectionist model have been conducted under a parametrically controlled environment focusing on the asymptotic convergence of the connectionist models. The paper presents these results using two examples of collaborative decision making drawn from the published case study literature. While the intention of the paper is not to introduce the connectionist paradigm as a means to bring arguments to a closure (resolution), certain resolution mechanisms can be easily implemented under the connectionist framework.

The proposed approach, however, has some limitations. The proposed approach provides a novel representation of argument structures as connectionist networks with associated analysis mechanisms to enable decision makers to assess the relative strengths of arguments on a continuous scale. However, it does not provide a logic-based analysis leading to discretevalued assessments of arguments as either winning or losing as in Vreesjwik (1992), Nute and Erk (1998), Nute, Henderson, and Hunter (1998), and Hua and

Kimbrough (1998). In logic-based methods, arguments are eventually marked as derivably true, derivably false, or undetermined, using proofs that are sound and complete. Logical analysis of arguments surrounding business discussions most often leads to inferences that are inconclusive or undetermined. In general, the final assessments of arguments will be undetermined in nonmonotonic and logically consistent defeasible reasoning, and this impasse is broken using decision rules on legitimacy as imposed by an analyst. While the discrete-valued, logically based argument analysis methods provide a way to declare an argument as winning or losing based on predetermined decision rules, they do not provide the means to assess the relative strengths of arguments involved in the discussion. Further, the validity of such decision rules in defeasible argument analysis may also be debatable. In this context, we do not make such declarative assessments in the proposed approach. Instead, we only provide an assessment of the relative strengths of competing arguments on a continuous scale. While the proposed connectionist framework is not concerned with ensuring the soundness and completeness of argument structures, its main goal is only to assess their relative strengths. In fact, this really may not be a drawback, as the argument structures can be preprocessed with any of the existing methods of logical analysis to ensure their soundness and completeness prior to assessing their relative strengths using the connectionist framework. In this regard, the connectionist approach can be viewed as a logical next step in the methodological research on defeasible argument analysis. Further, connectionist networks also have been shown to soundly represent simultaneous relations and nonmonotonic logic (Feldman and Ballard 1982, Pinkas 1995). Numerical algorithms of the type used in the paper are demonstrated to be an efficient way of satisfying parallel constraints implicit in the kind of networks we build to represent the arguments (Thagard

1989). It must also be noted that the connectionist approach is inherently massively parallel in its computations and therefore has many advantages over reasoning methods that use certainty factors. With certainty factors one has to carefully engineer the rule base to keep track of the paths along which evidence is propagated (Russel and Norvig 1995). Second, the proposed approach need not necessarily address all kinds of dialectic decision-making situations. The pro posed approach is extremely useful for analyzing arguments that are based extensively on evidential reasoning. Evidential reasoning is quite common in accounting/auditing, operational decision making, diagnostics and troubleshooting, and legal situations. Such situations easily lend themselves to structured dialog. Third, argument networks have traditionally followed the approach of taking atomic statements as nodes with the arcs between nodes representing qualified inferences (Vreesjwik 1992). We have followed the same approach here. However, connectionist models have been proposed to represent specific logic statements such as propositional logic (Pinkas 1995), causality (Sun 1995), and rule-based reasoning (Dolan and Smolensky 1988). Such models could perhaps be integrated with connectionist argument networks to model the different logic systems. Fourth, we do not provide any mechanisms to assess whether a statement should be accepted as a fact or as a defeasible assertion. Finally, we have provided limited guidelines on how to set the parameter values (especially the arc weights). However, the computational results indicate that the activation levels in a connectionist network are dependent on the decay parameter and the arc weights. We observe from computational results that the decay parameter should be set to a value close to 0. As far as the arc weights are concerned, one can vary the arc weight values to capture their effects on the activation levels. In fact, this may actually provide greater insights into the argumentation structure. For instance, while the activation level of the main thesis in Example 1 declined monotonically with arc weights, activation level of the main thesis in Example 2 increased. It lends credence to the conclusion that the argument is leaning towards the auditor (in Example 1), and towards the client (in Example 2). Despite these limitations, the connectionist paradigm presents a novel way of capturing group deliberations and provides decision support for argumentative decision making.

Parsing the argument statements to build specific connectionist models within an argumentation network is a difficult and open problem, and this has not been addressed here. However, several solutions exist for argument parsing and automated construction of arguments. Most of these systems use variants of natural language-processing concepts. There is a stream of literature that tackles the issue of development of argument understanding systems. Cohen (1987) suggests a model for computational understanding of arguments. The model uses a restricted processing strategy to determine where a proposition fits with respect to an argument and how it relates to some prior proposition. Strategies for accomplishing this include (1) pre-order transmissions, where the speaker states a claim followed by evidence, (2) post-order transmissions, where the speaker states an evidence followed by a claim, and (3) hybrid transmissions, i.e., arguments that contain both pre-order and post-order transmissions. Algorithms have been proposed to deal with each of the above types of arguments. Another component of the argument-understanding systems is the use of linguistic clues. Linguistic clues are phrases or words used by argument participants to indicate the structure of arguments (Cohen et al. 1988). Such clues include phrases such as ‘‘returning to $\dots , \dots , ^ { \prime \prime } \quad ^ { \prime \prime } { \sf a s }$ a result . . . ,’’ ‘‘because of this . . . ,’’ ‘‘and . . . ,’’ ‘‘also . . . ,’’ etc. Hypertext-based interactive environments have also been used for creating argumentation threads (Bernstein 1992). These systems use graphics to explore the structure of the arguments. Recent work in this area has approached this problem by building intelligent dialog systems that make use of agent models and user-adapted interaction techniques to process arguments (McRoy et al. 1999). The use of multimodal interfaces that blend natural language processing and Graphical User Interfaces (GUI) hold much promise with regard to building automated argumentationunderstanding systems.

Several avenues of research arise from this work. Some of the important research questions to be addressed in future are:

• How can the connectionist formalism be integrated with an online system to provide support for distance deliberations among a group of geographically dispersed members? What structured communication language would be needed for this? What underlying data model should be used to capture the logic of collaborative discussions? What different intelligent analysis and support tools can be provided to the members as a form of argumentation support?

• How can the connectionist networks capture practical considerations such as argument cogency, persuasiveness, gaming, power structure, and other human traits that influence teamwork?

• What is the technological framework for developing dialectical support systems? How do users interact over such a system? What user interfaces and structural communication tools are needed?

• What field studies are required to analyze the effects of the proposed system on the performance of teams in terms of efficient information filtering and discussion structuring, generating focal attention on critical issues through analysis, facilitating innovative argument strategy development, ease and speed of communication, and resolution of differences?

• Another useful function of a system based on this approach would be to identify and highlight fallacies in arguments (such as cyclical arguments, disconnected arguments, and self-contradictions). We intend to pursue this in future research.

## References

Barua, A., R. Chellappa, A. B. Whinston. 1997. Design and implementation of internet and intranet based collaboratories. J. Electr. Comm. 1(2) 32–58.

—, ——, ——. 1995. Creating an MIS collaboratory in cyberspace: Theoretical foundations and an implementation. J. Organ. Comput. 5(4) 417–442.

Bernstein, B. 1992. Euclid: Supporting collaborative argumentation with hypertext. Technical report, University of Colorado, Boulder, CO.

Bowers, J. M., S. D. Benford, eds. 1991. Studies in Computer Supported Cooperative Work: Theory, Practice and Design. North-Holland, Amsterdam, The Netherlands.

Cohen, R. 1987. Analyzing the Structure of Argumentative Discourse. Comput. Linguistics 13(1) 11–24.

—, et al. 1988. On the semantics of natural language sentences in logic programming. V. Dahl, P. Saint-Dizier, eds. Natural Language Understanding and Logic Programming II. Elsevier Science Publishers B.V., North-Holland, Amsterdam, The Netherlands.

Coopers and Lybrand. 1990. Excellence in audit education. Case Material. Cooper and Lybrand, New York.

Dolan, C., P. Smolensky. 1988. Implementing a connectionist production system using tensor products. D. Touretzky et al., eds. Proc. 1988 Connectionist Summer School. Morgan Kaufmann, San Mateo, CA 265–272.

Ellis, C. A., S. J. Gibbs, G. L. Rein. 1991. Groupware: Some issues and experiences. CACM 34(1) 38–58.

Feldman, J. A., D. H. Ballard. 1982. Connectionist models and their properties. Cogn. Sci. 6 205–254.

——. 1985. Special issue on connectionism. Cogn. Sci. 9(1)

Fischer G., A. C. Lemke, R. McCall, A. I. Morch. 1991. Making argumentation serve design. Human-Comput. Interaction 6 393– 419.

Fodor, J. A., Z. W. Pylyshyn. 1988. Connectionism and cognitive architecture: A critical analysis. Cogn. 28 3–17.

Gensler, H. J. 1990. Symbolic Logic. Prentice-Hall, Englewood Cliffs, NJ.

Goldberg, D., B. Oki, D. Nichols, D. B. Terry. 1992. Using collaborative filtering to weave an information tapestry. CACM 35(12) 61–70.

Greenburg, S., ed. 1991. Computer Supported Cooperative Work and Groupware. Academic Press, London, U.K.

Grief, I., ed. 1988. Computer-Supported Cooperative Work: A Book of Readings. Morgan Kaufmann, San Mateo, CA.

Heckerman, D. 1991. Probabilistic Similarity Networks. MIT Press, Cambridge, MA.

Hill, W., J. Hollan, D. Wrobleski, T. McCandless. 1992. Edit wear and read wear. Proceedings of CHI ‘92, Human Factors in Computing Systems. ACM Press, New York 3–9.

Hua, G., S. Kimbrough. 1998. On Hypermedia based argumentation decision support systems. Decision Support Systems 22 259–275.

Jessup, L. M., J. S. Valacich, eds. 1993. Group Support Systems. Mc-Millan Publishing Company, New York.

Katzenbach, J. R., D. K. Smith. 1993. The Wisdom of Teams: Creating the High Performance Organization. Harper Business, New York.

Kimbrough, S. O. 1986. A graph representation for management of logic models. Decision Support Systems. 2(1) 27–37.

Lin, F., Y. Shoham. 1995. Provably correct theories of action. J. Assoc. Comput. Machinery 42(2) 293–320.

Locks, M. O. 1985. The logic of policy as argument. Management Sci. 31(1) 109–116.

Lorenzen, P. 1987. Constructive Philosophy. University of Massachu setts Press, Amherst, MA.

——. 1965. Formal Logic. Reidel Publishing Company, Dardrecht, The Netherlands.

——. 1984. Normative Logic and Ethics. Bibliographisches Institute Mannheim/Wein/Zurich, B.I. Wissenschaftsverlag.

Loui, R. P. 1994. Argument and Arbitration Games. Workshop on Computational Dialectics, AAAI Conference. 72–83.

McRoy, S. W., S. S. Ali, A. C. Restificar, S. Channarukul. 1999. Building intelligent dialog systems. Intelligence 10(1).

Meyers, R. A. 1989. Persuasive arguments theory: A test of assumptions. Human Comm. Res. 15(3) 357–381.

Mitroff, I. I., R. O. Mason, V. P. Barabba. 1982. Policy as argument-A logic for ill-structured decision problems. Management Sci. 28(12) 1391–1404.

Nunamaker, J. F., A. R. Dennis, J. S. Valacich, D. R. Vogel, J. F. George. (July) 1991. Electronic meeting systems to support group work. CACM 34(7) 40–61.

Nute, D. 1988. Defeasible Reasoning and Decision Support Systems. Decision Support Systems 4(1) 97–110.

——, K. Erk. 1998. Defeasible logic graphs I: Theory. Decision Support Systems 22 277–293.

Izak Benbasat, Senior Editor. This paper was received on January 9, 1998, and has been with the authors 9 months for 3 revisions.

——, C. Henderson, Z. Hunter. 1998. Defeasible logic graphs II: Implementation. Decision Support Systems 22 295–306.

Pinkas, G. 1995. Reasoning, nonmonotonicity and learning in connectionist networks that capture propositional knowledge. Artificial Intelligence 77 203–247.

Pollock, J. L. 1991. A theory of defeasible reasoning. Internat. J. In telligent Systems 6 33–54.

Ramesh, R., A. B. Whinston. 1994. Claims, arguments and decisions: Formalisms for representation, gaming and coordination. Inform. Systems Res. 5(3) 294–325.

Russel, S., P. Norvig. 1995. Artificial Intelligence: A Modern Approach. Prentice-Hall, Englewood Cliffs, NJ.

Sheth, B., P. Maes. 1993. Evolving Agents for Personalized Information Filtering. Proceedings of the 9th IEEE Conference on Artficial Intelligence for Applications.

Sun, R. 1995. A new approach toward modeling causality in commonsense reasoning. Internat. J. Intelligent Systems. 10 581–616.

Swanson, E. B. 1988. Business Value as Justificatory Argument. P. A. Strassmann, et al., eds. Measuring Business Value of Information Technologies. ICIT Press, International Center for Information Technologies, Washington, D. C. 121–138.

Thagard, P. 1989. Explanatory Coherence. Behavioral and Brain Sciences 12 435–502.

Toulmin, S. 1958. The Uses of Arguments. Cambridge University Press, Cambridge, U.K.

——, R. Rieke, A. Janik. 1979. An Introduction to Reasoning. Macmillan, NY.

Vinokur, A., E. Burnstein. 1974. Effects of partially shared persuasive arguments on group induced shifts: A group problem-solving approach. J. Personality and Soc. Psych. 29 305–315.

Vreeswijk, G. 1992. Reasoning with defeasible arguments: Example and applications. G. Wagner, D. Pearce, eds. Proceedings of the European Workshop on Logic in AI, (JELIA). Springer-Verlag, Berlin, Heidelberg, 189–211.
