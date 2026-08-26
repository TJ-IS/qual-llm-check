---
otero_id: 7298
otero_key: "TBV88FY2"
title: "The generic/actual argument model of practical reasoning"
authors: "John L. Yearwood; Andrew Stranieri"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.07.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The generic/actual argument model of practical reasoning

John L. Yearwood<sup>\*</sup>, Andrew Stranieri

Centre for Informatics and Applied Optimization, University of Ballarat, Victoria, Australia

Received 30 September 2003; received in revised form 26 July 2004; accepted 26 July 2004 Available online 8 September 2004

## Abstract

In this paper, we present a model of reasoning called the generic/actual argument model (GAAM). Reasoning within a discursive community can be represented with this model so that participant claims can be accommodated without recourse to combative metaphors such as attack or defeat. The model facilitates the comprehension of complex reasoning for humans as well as being a computational representation for machine modelling of reasoning. As such, the model naturally integrates machine inferences with human. The model has been the basis for the development of practical systems to support reasoning and deliberation in areas of law and organizational decision making. Here, we present a formal description of the model and identify some of its characteristics.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Argumentation; Practical reasoning; Generic arguments; Decision support

## 1. Introduction

In this paper, we present a formal description of the generic/actual argument model (GAAM) and develop from this some of its characteristics, practical advantages and disadvantages. The GAAM is intended as a model for decision support for decision making by individuals within a group or discursive community. It can be used by individuals without inference support, by individuals with varying degrees of inference support or as a fully computational system. The GAAM has been used to model reasoning in copyright law by Stranieri and Zeleznikow [46], predict judicial decisions regarding a property split following divorce by Stranieri et al. [44], support refugee status decision makers by Yearwood and Stranieri [54], facilitate interactive ecommerce by Yearwood et al. [56], implement multiagent negotiation by Avery and Yearwood [4], and in determining eligibility for government funded legal aid by Stranieri and Zeleznikow [47]. Two shell programs that implement GAAM ideas are described in Stranieri and Zeleznikow [47] and Yearwood and Stanieri [55].

The GAAM was developed as a framework for modelling discretionary reasoning and has been used to develop practical decision support systems over the last 5 years. The objective of this paper is to provide a description of the GAAM in terms of:

<sup>!</sup> identifying its basic set of propositions and how they are combined

<sup>!</sup> identifying the elements that formally control or represent the structure of reasoning

<sup>!</sup> its inference mechanisms and how propositions are derived

<sup>!</sup> the extent to which derived propositions are valid and accepted

<sup>!</sup> the way in which it supports discretionary decision making

<sup>!</sup> setting out its capabilities as a non-dialectical model upon which a dialectical model can be built.

The remainder of this paper is organised as follows: Section 2 provides a brief review of Toulmin argument structures. Section 3 sets out how the elements of the GAAM relate to Toulmin argument structures and discusses inferences and the separation of inference from the structure of reasoning. Section 4 presents the GAAM more formally and in detail. Section 5 discusses some of the characteristics of the model, exploring deducibility and possible notions of argument strength and validity. Section 6 compares the model with other approaches.

## 2. Toulmin argument structures

Toulmin [48] concluded that most arguments, regardless of the domain, have a structure that consists of six basic invariants: claim, data, modality, rebuttal, warrant and backing. Every argument makes a claim based on some data. The argument in Fig. 1 is drawn from reasoning regarding refugee status according to the 1951 United Nations Convention relating to the Status of Refugees (as amended by the 1967 United Nations Protocol relating to the Status of Refugees) and relevant High Court of Australia rulings. The claim of the argument in Fig. 1 is the statement that Reff, an applicant for refugee status, has a well founded fear of persecution. This claim is made on the basis of two data items, that Reff has a real chance of persecution and that relocation within Reff’s country of origin is not appropriate. A mechanism is required to act as a justification for why the claim follows from data. This justification is known as the warrant which is, in Fig. 1, the statement that <sup>d</sup>The test for well founded fear is real chance of persecution unless relocation affords protection<sup>T</sup>. The backing provides authority for the warrant and in a legal argument is typically a reference to a statute or a precedent case. The rebuttal component specifies an exception or condition that obviates the claim. Reff may well have a real chance of persecution and relocation is unlikely, however, the claim that his fear is well founded does not hold if Reff’s persecution is due to criminal activities.

Argumentation has been used in knowledge engineering in two distinct ways; with a focus on the use of argumentation to structure reasoning (i.e. non-dialectical emphasis) and with a focus on the use of argumentation to model discourse (i.e. dialectical emphasis). Dialectical approaches typically automate the construction of an argument and counter arguments normally with the use of a non-monotonic logic where operators are defined to implement discursive primitives such as attack, rebut, or accept. Carbogim et al. [11] present a comprehensive survey of defeasible argumentation.

![](/api/attachments/TBV88FY2/fulltext/images/452e7e6c735440abb1523e372191f414eb4e2c038a90ade741b175a22b3c251b.jpg)  
Fig. 1. Toulmin argument structure for well founded fear.

Dialectical models have been advanced by Cohen [14], Fox [21], Vreeswijk [51], Dung [18], Prakken [36,37], Prakken and Sartor [38], Gordon [24], Fox and Parsons [22], Farley and Freeman, [20], Poole [35] and many others. In general, these approaches include a concept of conflict between arguments and the notion that some arguments defeat others. Most applications that follow a dialectical approach represent knowledge as first order predicate clauses, though engage a non-monotonic logic to allow contradictory clauses. Mechanisms are typically required to identify implausible arguments and to evaluate the better argument of two or more plausible ones.

In applications of argumentation to model dialectical reasoning, argumentation is used specifically to model discourse and only indirectly used to structure knowledge. Concepts of conflict and of argument preferences map directly onto a discursive situation where participants are engaged in dispute. In contrast, many uses of argumentation for knowledge engineering applications do not model discourse. This corresponds more closely to a nondialectical perspective.

A non-dialectical representation facilitated the organisation of complex legal knowledge for information retrieval by Dick [16,17]. She illustrates how relevant cases for an information retrieval query can be retrieved despite sharing no surface features if the arguments used in case judgements are represented as Toulmin structures. Marshall [31], Ball [5] and Loui et al. [29] have built hypertext based computer implementations that draw on knowledge organised as Toulmin arguments. Hypertext links connect an argument’s assertions with the warrants, backing and data of the same argument and also link the data of one argument with the assertion of other arguments. In this way, complex reasoning can be represented succinctly enabling convenient search and retrieval of relevant information.

Clark [13] represented the opinions of individual geologists as Toulmin structures so that his group decision support system could identify points of disagreement between experts. Matthijssen [32] provides a further example of benefits that arise from the use of the original Toulmin structure. He represented user tasks as Toulmin arguments and associated a list of keywords to the structure. These keywords were used as information retrieval queries into a range of databases. Results indicate considerable advantages in precision and recall of documents as a result of this approach compared with approaches that require the user to invent queries. Johnson et al. [27] identified different types of expertise using this structure and Bench-Capon et al. [7] used TAS to explain logic programming conclusions. Branting [8] expands TAS warrants as a model of the legal concept of ratio decidendi. In the Split Up project, Zeleznikow and Stranieri [57] and Stranieri et al. [44] used TAS to represent family law knowledge in a manner that facilitated rule/neural hybrid development.

Toulmin proposed his views on argumentation informally and never claimed to have advanced a theory of argumentation. He does not rigorously define key terms such as warrant and backing. He loosely specifies how arguments relate to other arguments and provides no guidance as to how to evaluate the best argument or identify implausible ones. Nevertheless, the structure was found to be useful as a tool for organising knowledge.

## 3. The generic/actual argument model

Often reasoning occurs in the context of a small group of stakeholders involved in dialogue who would like to reach agreement on some issue. Whilst there is much anecdotal evidence for this it is also true that most organizations like to see a team approach to the solution of problems but are keen to have frameworks that permit a range of views. In general, we can distil the following characteristics of small group reasoning:

<sup>!</sup> Membership of the discursive community is usually well defined

<sup>!</sup> Members have different beliefs about the base facts and also have different preferences for how to infer from base facts to claims

<sup>!</sup> The truth value of a claim or proposition, if it exists at all, is difficult to ascertain.

A key assumption underpinning our approach is the principle that reasoning within a discursive community can be represented as a set of generic arguments which link together to form a tree or graph structure. Each generic argument represents a class of actual arguments that may be made and structurally embodies the components that go towards shaping well considered decision making in uncertain domains. The framework called the GAAM is an attempt to develop a model for non-adversarial, structured reasoning. It currently acts as a non-dialectical framework in which a decision maker can be supported in making decisions about an issue. The model will underpin a dialectical model that will be developed in future work.

Our approach is in contrast to other argument based models such as IBIS [41] and Gordon and Karacapilidis’ Zeno argumentation framework [25], which focus heavily on the way in which multiple agents combat and defeat each other. One of the important features of the GAAM is that it invites a discursive community to construct an agreed framework for reasoning that is flexible enough to permit a broad range of points of view. This framework is then used to make the reasoning of individuals clear to the group. The development of models that encourage deliberation and are helpful in moving groups towards agreement or at least understandings of the basis for disagreements is a social ideal. Such models not only have the potential to present a fresh approach to group and organizational decision making but also have the potential to contribute to more effective and informed decision making generally. Furthermore, increasingly, participants to a discussion are software agents. As software agents currently are not as flexible as humans, their use can more easily be integrated into a highly structured model that is designed for noncombative structured reasoning rather than adversarial based approaches. Using a highly structured nondialectical model helps agent communication as dialogue is more structured.

## 3.1. An example from refugee law

In order to demonstrate some of the ideas involved in the GAAM, we shall consider the story of Anju who is an applicant for refugee status in Australia. Australia is a signatory to the United Nations Convention on the Status of Refugees and so there is law and guidelines that set out to some degree the basis for determining refugee status.

Anju was a Sikh born in India in the 1970s. She had 13 years education there before she travelled to

Australia in the 1990s and married a Muslim. Her culture does not approve of marriage into other religions. She feels that her relatives in India would have nothing to do with her if she returned because she has done something that is culturally unacceptable. If she were to return to India now, at the very least she would face taunting and social ridicule over her marriage. She has recently divorced her husband and is being supported by relatives. She feels that it would be difficult to live in India without the support of relatives.

## 3.2. A structure for reasoning in this domain

The members of the Refugee Review Tribunal (RRT) of Australia represent a community of decision makers. From consultations with members of this community, we have been able to represent the reasoning that they use in determinations on refugee status as a tree of generic arguments. This tree comprises approximately 300 nodes and it sets out the structure of reasoning for these determinations. In determining refugee status, one component of the reasoning is concerned with establishing whether the applicant has a well founded fear of persecution. Awell founded fear of persecution depends on a number of relevant data: the incidents of harassment that have occurred in the past; the credibility of the applicant’s story; practices and policies in the country or region that target the applicant; whether these practices and policies have changed recently and whether or not the applicant could be relocated within the country of origin. Each one of these in turn depends on other nodes in the tree. This approach simply sets out a tree structure for reasoning in this domain where each node has a label that indicates the issues or facts that are used to construct reasoning.

## 3.3. Generalizing the structure

The Toulmin argument structure represents reasoning as arguments constructed from sentences which are claims and data. The reasoning that represents the position of the applicant (Anju) and the reasoning of the RRT member would be represented as two separate Toulmin diagrams. Fig. 2 sets out the section of a more complete tree that represents reasoning towards a claim on <sup>d</sup>well founded fear<sup>T</sup>. Each claim and data item are generalised to a sentence with a variable-value component that can accommodate the claims of both the applicant (Anju) and the member. In fact a range of claims can be accommodated.

![](/api/attachments/TBV88FY2/fulltext/images/bb7f73aa68d3a5a2c166c8ef9930567991fdb865afff5212020d9800d2011cf8.jpg)  
Fig. 2. The well founded fear argument for Anju.

## 3.4. The case as an actual argument

Anju’s actual argument is captured within this generic argument structure (GAS) by the selection of values for each data and claim item as shown in Fig. 2. Her argument is captured by the darker shaded values. The argument could be expressed as:

Anju has a well founded fear of persecution because: the incidents of harassment that have occurred in the past certainly constitute persecution due to a convention reason; her story is completely credible; relocation within her country of origin is not feasible; practices/policies of harassment that target her are likely and recently there has not been any change to these.

## 3.5. Generic arguments

The GAAM uses a variant of the layout of arguments advanced by Toulmin (1958). Arguments are represented at two levels of abstraction; the generic and the actual level. The generic level is sufficiently general so as to represent claims made by all members of a discursive community. All participants use the same generic arguments to construct, by instantiation, their own actual arguments. The generic arguments represent a detailed layout of arguments acceptable to all participants whereas the actual arguments capture a participant’s position with respect to each argument. The actual arguments that one participant advances are more easily compared with those advanced by another, in a dialectical exercise because, in both cases the actual arguments have been derived from a generic template that all participants share.

Fig. 3 represents the basic template for the knowledge representation we call a generic argument. A generic argument is an instantiation of the template that models a group of arguments. The generic argument includes:

![](/api/attachments/TBV88FY2/fulltext/images/ddb0007813716fbe87211e42ef4310ef808a05232961de9a372972552bb7bf67.jpg)  
Fig. 3. The generic argument template.

<sup>!</sup> a variable-value representation of the claim with a certainty slot

<sup>!</sup> a variable-value representation of the data items (with certainty slots) as the grounds on which such claims are made

<sup>!</sup> reasons for relevance of the data items in place of the Toulmin warrant

<sup>!</sup> a list of inference procedures that may be used to infer a claim value from data values in place of the warrant

<sup>!</sup> reasons for the appropriateness of the inference procedure

<sup>!</sup> context variables

<sup>!</sup> a claim value reason component(primarily for use when the inference procedure does not give an explanation).

The absence of the rebuttal component present in Toulmin’s original formulation is also noteworthy.

The idea is that the generic argument sets up a template for arguments that allows the representation of the claim and the grounds for the claim. The claim of a generic argument is a predicate with an unspecified value (which can be chosen from a set when an actual argument is being made).

A claim takes the form <sup>b</sup>PREFIX<sup>N</sup>{VALUES} <sup>b</sup>SUFFIX<sup>N</sup> as seen in Fig. 2. For example, the <sup>b</sup>well founded fear<sup>Q</sup> slot has the form <sup>b</sup>The applicant {has, does not have} a well founded fear of persecution<sup>Q</sup>. Each data item is also a predicate with an unspecified value, which can be taken from a specified set of values. The connection between the data variables and the claim variable is called an inference procedure and maps the data space to the claim space.

The argument template represents knowledge at a very high level of abstraction. There are two levels of instantiation made in applying the template to model arguments within a domain: the generic level and the actual level. A generic argument is an instantiation of the template where the following components are set:

<sup>!</sup> claim, data and context variables and their corresponding sets of possible values (are specified but not assigned values)

<sup>!</sup> relevance reason statements and backing statements are specified

<sup>!</sup> inference procedures are listed but a commitment to any one procedure is avoided

<sup>!</sup> inference procedure reasons are specified for each procedure

<sup>!</sup> claim and data variables are not assigned certainty values.

The generic argument is sufficiently general so as to capture the variety of perspectives displayed by members of a discursive community.

Fig. 4 illustrates the refugee argument above, as a generic argument. The claim variable has been labelled <sup>d</sup>well founded fear<sup>T</sup> and acceptable values specified. There are three inference procedures known to be appropriate in this example; the first is a rule set that derives from heuristics an immigration expert uses, the second is a neural network trained from past cases and the third is a human inference. This latter inference indicates that a human is empowered with sufficient discretion to infer a claim value from data item values in any way he or she likes.

![](/api/attachments/TBV88FY2/fulltext/images/9d6b8e99407fff0244f5023d81f7aaa595ab3ea07d0d3be326ee3a5ac7dd99b6.jpg)  
Fig. 4. Generic argument for claims about <sup>d</sup>well founded fear<sup>T</sup>.

## 3.5.1. Inference procedures

In the GAAM, the Toulmin warrant has been translated into three components: the inference procedure; the reasons for relevance of the data items and the reasons for the inference procedure. This relates to two different roles a warrant can play in an argument. As described above, the warrant indicates a reason for the relevance of a data item and on the other hand the warrant can be interpreted as a rule which, when applied to the data items leads to a claim inference. An inference procedure is an algorithm or method used to infer a claim value from data item values. Under this interpretation, an inference procedure is an operator on data variable values to deliver claim variable values. It is any procedure that will perform a mapping from data items to claim items. A mathematical function, an algorithm, a rule set, a neural network or procedures yet to be discovered are examples of inference procedures. Many inference procedures can be implemented in software. Thus, they can be automated in computer based systems. However, this need not necessarily be the case for a knowledge engineering framework. Claims can sometimes be inferred from data items by human agents without the explicit specification of an inference procedure. This occurs frequently in discretionary fields of law where, as Christie [12] notes, decision makers weight and combine relevant factors in their own way without articulating precisely how claims were inferred. This situation is accommodated within the generic actual argument framework with the specification of an inference type labelled, simply, myHuman.

The original Toulmin warrant can also be seen to be a reason for relevance or an inference procedure. Past contributions to a marriage are relevant in Australian family law. Past contributions appears as a data item in a generic argument regarding property distribution following divorce because a statute dictates that contributions are relevant. The wealth level of a marriage in Australia is made relevant by past cases and not by statute. The hair colour of the wife is considered irrelevant because there is no statutory or precedent basis for its relevance. Further, domain experts can think of no reason that would make this feature relevant.

## 3.5.2. Separation of inference from the structure of reasoning

Explicitly representing the inference method enables the use of a variety of inference procedures. For example, the method used to infer an assertion in the family law application, split up is a rule for some arguments and a neural network for others [44]. Branting [9] provides a framework that captures legal reasoning using both rules and exemplars. In his framework, rules and exemplars differ primarily in that exemplars are much less abstract than rules and can be used to provide a bridge between the abstract rule descriptions and the specific case descriptions. A knowledge representation framework that separates the inference method from other components is very flexible. We argue that our argument based approach captures the granularity of reasoning necessary in the most appropriate way by:

<sup>!</sup> collectively deciding on a set of generic arguments

<sup>!</sup> collectively agreeing on the choice of inference procedures

<sup>!</sup> allowing actual arguments to be built by instantiating generic arguments. In fact, agreeing on the set of values that claims and data items may be drawn from

<sup>!</sup> allowing actual arguments to be built that extend the generic set.

The argumentation framework advanced here not only departs from the Toulmin formulation by distinguishing inference procedure from reason for relevance but it also represents context explicitly.

## 3.5.3. Context

Fig. 4 illustrates two context variables; the determining country and the person about whom the argument is being made. The respective values are a list of world nations for the determining country and Anju or the more universal X for the person. Context variables represent something of the background knowledge that impacts on the generic argument. For example, the context variable determining country in Fig. 4 represents a scope constraint on the argument. This indicates that an actual argument can be made based on the generic argument however the determining country sets a context for the argument. The context variable is an articulation of the presuppositions that underpin the generic argument.

The context variable can also represent the scope of variables used in the generic argument. For example, the person context variable will be assigned the value X for a discourse participant intent on making the more universal argument that relates to well founded fear of anyone. The participant that restricts the argument to Anju does so be setting the context variable to Anju. In general, context is a difficult concept to define. In the framework defined here, context is defined as presupposition and variable scope. However, other definitions can also be accommodated as long as they can be captured as variable-value tuples.

## 3.5.4. Rebuttal

The Toulmin rebuttal which is not explicitly represented in the GAAM would be captured within a generic argument structure as a different instance argument possibly using a different inference procedure that produces different claim values. The rebuttal is more clearly regarded to be a dialectical component and is therefore omitted from this essentially nondialectical frame. For instance, discursive participants may create actual arguments as instances of the same generic argument in ways that are quite different from others. Participant A may assert a different claim value than B, yet have perfect agreement on all data item values because a different inference procedure was selected. Any discussion regarding this difference, including exchanges that make the point that the difference constitutes an attack, or exchanges that seek to defend A or B’s assertion, or exchanges that seek to identify the stronger argument involve dialectical exchange and are omitted from the nondialectical frame.

A generic argument has to capture the whole range of claims including the rebuttal claim. The model is therefore able to represent the rebuttal and reasoning towards it; however, the fact that it is a rebuttal of some other proposition that the generic argument permits is not represented at this level. It will be a matter for a further dialectical model based on the GAAM.

## 3.5.5. Relevance

The concept of relevance is in itself difficult to define generally. van Dijk [49] describes the concept of relevance as it applies to a class of modal logics broadly called <sup>d</sup>relevance logics<sup>T</sup> as a concept grounded firmly in the pragmatics, and not the semantics or syntax of language. Within a discursive community, the data items in a generic argument must be relevant to the claim to the satisfaction of members of the community. A generic argument in the field of family law property division may include hair colour as a relevant data item for inferring property division if a reason for its relevance that is acceptable, even if not held, by many in the community, is advanced. Perhaps, the utterance <sup>b</sup>Blond women will remarry more readily<sup>Q</sup> as a reason for the relevance of hair colour as a data item may not be held by all participants to a discourse but reflects a belief that is understood as plausible by many.

It is important to appreciate that the notion of a generic argument can be used to capture a shared understanding about what a core set of arguments in a domain are. In some respects there is some similarity to Aristotle’s <sup>d</sup>topic theory<sup>T</sup> [3], in that an important aspect in constructing each generic argument is a search for the premises or grounds for that argument. The generic argument represents the results of this search as the data items articulated and their reasons for relevance. These are considered to be <sup>d</sup>nearly<sup>T</sup> complete knowledge about the possible grounds for that argument. As such they would include general exclusionary reasons as described by Raz [40], which are often the basis for rebuttals. Establishing the generic arguments in a domain provides considerable structure for developing arguments. Engisch [19] observes that <sup>d</sup>reaching a conclusion as such gives rise to a minimum of effort; the main difficulty lies in finding premises for it<sup>T</sup>. We argue that establishing the generic arguments in a domain is an effective part of acquiring, representing, reasoning and providing justification and transparency for decision making.

Fig. 3 also includes certainty slots for each data item, claim and inference procedure. These recognize that there is uncertainty in the processes of developing actual arguments. The certainty values are assigned when values are assigned in the process of constructing an actual argument. A generic argument is an agreed approximation to a world but still may only be partial knowledge. We do not explicitly put a certainty or confidence value on a generic argument although we permit generic arguments to change over time. The structure of generic arguments that describe a domain will not be static. As knowledge within the domain evolves new versions of the generic argument structure will be required. New factors emerge as being relevant to some arguments and new inference procedures may be needed as new rules emerge or new cases become precedents. Most actual arguments in a domain are then underpinned by a particular version of the generic argument structure.

The knowledge in a domain of discourse can be represented as a tree of these generic arguments with a data item of an argument being the claim of another argument. Part of the tree for reasoning in refugee law appears in Fig. 2 where the reason for relevance of the <sup>d</sup>relocation<sup>T</sup> data item is shown (as being specified in the UN convention). The generic arguments within a domain can be established by engaging participants in a discussion in the development of the GAS or through their contributions to a common view of the structure and each participants reasons for relevance [1]. The intention is to have participants agree on a structure for reasoning developed from their shared understanding. The open textured nature of many areas of reasoning mitigates against the representation of all arguments in a domain as generic arguments but a large proportion of arguments in many domains can be represented in this way. It is also useful to know when particular actual arguments diverge from instantiations of generic arguments and to detect whether or not they are accepted.

## 3.6. Making actual arguments

Actual arguments made are instances of a generic argument where each data slot has a value, an inference procedure can be chosen and executed to deliver a value for the claim slot. Fig. 2 illustrates an actual argument for the story of Anju described in Section 3.1 with data values indicated as the dark shaded selections and the particular inference procedure selected is inferencing based on her own human reasoning, which may be captured by the myHuman inference procedure. The reasoning of the tribunal member is also indicated as the light coloured selections and these may conform to an inference based on a rule set myRules.

The claim value reason for this actual argument provides a reason for the specific claim value inferred rather than other claim values. The claim value reason in Fig. 2 would express a reason for why, <sup>b</sup>well founded fear<sup>Q</sup> is likely, given the data items and inference procedure selected. With human inferencing, there is not necessarily a reason for the inference procedure given at the generic level and there is therefore a need to justify the claim value produced by the human inference. This is represented in an actual argument diagram as the claim value reason slot. In Anju’s case, the reason for claiming well founded fear is based on her personal perception of difficult circumstances if returned to India.

The member’s justification for his claim would come from the reasons for the rules in this rule set and their appropriateness for reasoning with this data about this claim. This is what would be called deductive justification by MacCormick [30]. The claim value asserted in Fig. 2 <sup>b</sup>does not have<sup>Q</sup> needs to be justified and this justification is the claim value reason which is provided at the stage of making an actual argument rather than at the generic argument stage. If the inference procedure is a mathematical function or has mechanisms that are not visible, such as a neural network, then the articulation of a reason for the inference procedure is not an adequate justification of the value. Conceptually, it is more correct to say it is a reason for a particular value that has arisen as a result of the application of an inference procedure.

Certainty values are assigned when a participant creates an actual argument. The certainty value represents the degree of certainty the participant has that the claim (or data) variable value selected is the true value. A certainty value may be set directly by the participant or calculated by the inference procedure. A certainty value of 80% associated with the data item value, <sup>d</sup>does not have<sup>T</sup> for the well founded fear variable in Fig. 2, would be read as a high (80%) degree of certainty that well founded fear of persecution is likely. This is calculated by the inference procedure selected, myRules. However, if the inference procedure selected does not calculate certainty values (e.g. human inferences), then the participant must set a certainty value. The way in which the data item certainty values are combined is a feature of the mapping performed by the particular inference procedure selected so is not made explicit in the GAAM.

Linguistic variable values such as very elderly, elderly, middle aged, young and very young seem to represent certainty in themselves so as to make the specification of a certainty value redundant. However, the inclusion of a certainty value slot in the GAAM enables the specification of membership function values if fuzzy reasoning was selected as the inference procedure, conditional probability if a Bayesian inference [42] was selected or certainty factors if MYCIN [10] like rule inferences were used as the inference procedure.

Generic and actual argument structures correspond to a non-dialectical perspective. They do not directly model an exchange of views between discursive participants but rather describe assertions made from premises and the way in which multiple claims are organized. Claim variables are inferred using an inference procedure, which may not necessarily be automated, from data item values. The reasoning occurs within a context and the extent to which the data items correspond to true values, according to the proponent of the argument, is captured by certainty values.

The generic argument provides a level of abstraction that accommodates most points of view within a discursive community and anticipates the creation of actual arguments, by participants, as instantiations of a generic argument. However, it is conceivable, given the open textured nature of reasoning, that a participant will seek to advance an actual argument that is a departure from the generic argument. This is a manifestation of discretion and can be realized with the introduction of a new variable (data, claim or context) value, with the use of a new inference procedure or, with a new claim value reason.

A non-dialectical argumentation model must model discretion and open texture. The concept of open texture was introduced by Waismann [52] to assert that empirical concepts are necessarily indeterminate. A definition for open textured terms cannot be advanced with absolute certainty unless terms are defined axiomatically, as they are, for example in mathematics. Gold may be defined as that substance, which has a certain set of spectral emission lines, and is coloured deep yellow. However, because there is the possibility of a substance with the same spectral emission as gold but without the colour of gold, the concept for gold is open textured.

The concept of open texture is significant in the legal domain because new uses for terms and new situations constantly arise in legal cases. Prakken [36] discerns three sources of open texture: reasoning which involves defeasible rules, vague terms or classification ambiguities. Judicial discretion is conceptualised by Christie [12] and Bayles [6] as the exibility decision-makers have in weighing relevant factors when exercising discretion although articulating an assignment of weights is typically difficult. This view of discretion does not derive from defeasible rules, vague terms or classification ambiguities so is regarded as a fourth type of situation that contributes to the open textured nature of law.

The link between the GAAM and discretion is described in detail by Stranieri et al. [45]. Broadly, discretion manifests as the exibility for a participant to construct an actual argument from a generic argument by:

<sup>!</sup> Adding data item factors into the actual argument that are not in the generic tree

<sup>!</sup> Removing a data item factor from the actual argument that is in the generic tree

<sup>!</sup> Selecting a data, claim or context variable value from those specified in the generic tree

<sup>!</sup> Selecting a data, claim or context variable value that has not been specified in the generic tree

<sup>!</sup> Selecting an inference procedure from the list specified in the generic tree

<sup>!</sup> Selecting an inference procedure not specified in the generic tree

<sup>!</sup> Leaving data items, reasons for relevance, inference procedure and reasons for the appropriateness of inference procedures implicit

<sup>!</sup> Introducing a claim value reason statement

<sup>!</sup> Selecting certainty values.

This framework including the generic/actual distinction, the clear separation of inference procedure from other components and the inclusion of reasons for relevance and context introduces a structure that represents knowledge applicable to a discursive community.

Situations will arise where an argument needs to be made for which no generic argument exists. In these cases, a new argument specific to that situation is created. Ultimately, the series of actual arguments made in a case is built and represents the full argument in that situation. Some of the arguments are instances of generic arguments, others are newly created.

## 4. Defining the GAAM

The GAAM is a means of specifying generic argument structures to model reasoning within a domain.

## 4.1. A generic argument structure

Definition: A GAS is a pair (CV, G) where CV is a set of context variables and G is a connected directed bipartite graph that has two kinds of nodes called, claim slots C and inference slots I.

The term bipartite means that every arc links a claim slot with an inference slot. There are no arcs that link claim slots together or link inference slots together.

<sup>!</sup> Every arc a of G must link an inference slot I in G to a claim slot C in G. The arc a is said to belong to the inference slot I; it is said to be attached to the claim slot C but does not belong to C

<sup>!</sup> Every arc that belongs to an inference slot in G must be attached to exactly one claim slot in ${ \mathcal { G } } .$

The tree of Fig. 2 is part of a GAS for reasoning in refugee law. Each of the nodes represents a claim slot. The inference slot would be located at the junction of the arcs labelled <sup>d</sup>inference<sup>T</sup>.

Definition: Claim slot. Every claim slot C has a prefix $C _ { \mathrm { p } } ,$ set of values $C _ { \mathrm { v } }$ and a suffix $C _ { \mathrm { s } } .$ Each claim slot also has two variables. A variable r of type string and a variable c of type num <sup>a</sup> [1, 1].

The variable r is a place holder for the claim value reason and the variable c a place holder for the certainty factor. These are not instantiated at the generic level but at the actual argument level.

For example, the claim slot in Anju’s argument for well founded fear is [The applicant has, does not have a well founded fear of persecution]. The prefix is <sup>d</sup>The applicant<sup>T</sup>, the set of values is has, does not have and the suffix is <sup>d</sup>a well founded fear of persecution<sup>T</sup>.

Definition: Inference slot. Every inference slot I has an arity (n) and a set of pairs of operators and strings $( I _ { j } , J _ { j } ) { : } j { = } 1 . . . k$

The number of arcs that belong to I is one more than its arity. An inference slot of arity n is represented with n inward arcs and one outward arc. Such an inference slot is called an n-ary inference slot. The set of $n { + 1 }$ claim slots $\left. C _ { 1 } , . . . . , C _ { n } , C _ { n + 1 } \right.$ is called the signature of I. The set of operators is a set of n-ary operators. Each operator is of the form $I _ { j } \colon C _ { \mathrm { 1 v } } \times . . .$ $\times C _ { n \mathrm { v } } { \times } C V V { \longrightarrow } C _ { n + 1 } ,$ 1v and operates on the sets of values of the first n claim slots in its signature and the set of context variable values. The strings $J _ { j }$ are intended to store the justification for the jth operator.

For example, in making an inference about a claim of <sup>d</sup>well founded fear of persecution<sup>T</sup> the arity of the inference slot would be 5 and there may be three operators that map the sets of values of the <sup>d</sup>relocation<sup>T</sup>, <sup>d</sup>credibility<sup>T</sup>, <sup>d</sup>practices/policies that target the applicant<sup>T</sup>, <sup>d</sup>incidents<sup>T</sup> and the <sup>d</sup>change of practice/ policy<sup>T</sup> claim dots (as well as a set of context variable values) to the values of the <sup>d</sup>well founded fear<sup>T</sup> claim slot. The three operators shown in Fig. 4 are myRules, myNeural and myHuman.

Definition: Claim slot to inference slot Arc. Every arc from a claim slot to an inference slot is a relevance relation pair $( C _ { i } , C _ { n + 1 } )$ and has two string attributes, RR and B.

For the relevance relation pair $( C _ { i } , C _ { n + 1 } )$ , RR is of type string and is the reason that $C _ { i }$ is relevant to inferring $C _ { n + 1 } . \ B$ is also of type string and is the backing that provides authority for the reason for relevance and in a legal argument is typically a reference to a statute or a precedent case.

Definition: Inference slot to claim slot arc. There is a unique arc from an inference slot to a claim slot.

If G is connected with at most one arc from any claim slot, at most one arc into any claim slot and only one claim slot has no leaving arc then the GAS G is a tree. In this case, the claim with no leaving arcs is the root or top level claim. A claim with no entering arcs is a leaf.

A reasoning tree is a structure in which there is a unique path from any claim slot $C _ { i }$ to another $C _ { j \cdot } \operatorname { A }$ source in a reasoning tree is a unique claim from which all other claims in the structure are accessible. $\mathrm { A }$ reasoning tree with a source may be called an <sup>d</sup>out tree<sup>T</sup>. In a reasoning tree, all reasoning towards a claim must pass through a single inference slot. $\mathrm { S o } ,$ semicircles are avoided. In the case of a single claim slot with no leaving arc, then we have a structure that represents reasoning towards a single claim or decision node. In most cases of representing practical reasoning, the above conditions have been met and the GAS avoids circularity.

## 4.2. Defining generic arguments

A generic argument is a GAS that consists of a single inference slot and the claim slots that are attached to its arcs. A full GAS can be formed by connecting individual generic arguments one for each inference slot in G. Fig. 5 illustrates in diagrammatic form a formal generic argument corresponding to that in Fig. 2 although not all five claim slots that act as data are visible. The single inference slot with the choice of three inference procedures is the focus of the generic argument.

## 4.3. Defining actual arguments

An actual argument is an instantiation of a GAS with context variable values, a choice of inference operator (and reason pair) for the inference slot, the assignment of claim values, claim value reasons to the claim value reason variables and the assignment of certainty values to the certainty factor variables.

First note that a claim slot $C _ { i }$ defines a set of propositions and the choice of a particular value $C _ { \mathrm { v k } }$ from the set of values $C _ { \mathrm { v } }$ defines a proposition (claim): $C _ { \mathrm { p } } C _ { \mathrm { v k } } C _ { \mathrm { s } } .$ The actual (atomic) argument for this proposition is then represented as being derived by the application of an inference procedure $I _ { \mathrm { h } }$ from the inference slot I (leading to the claim slot $C _ { i } )$ to n values $( C _ { 1 \mathrm { v } _ { i 1 } } , . . . , C _ { n \mathrm { v } _ { i n } } )$ and CVV. So, $I _ { \mathrm { h } } ( C _ { 1 \mathrm { v } _ { i 1 } } , \dots .$ $C _ { n \mathrm { v } _ { i n } } , \mathrm { C V V } ) { = } { \dot { C } } _ { \mathrm { p } } C _ { \mathrm { v k } } C _ { \mathrm { s } } .$

![](/api/attachments/TBV88FY2/fulltext/images/13d007d0bd32f632e2e5d19a4fafbe2ac0993b75b7f1415e7ee1af3a6e96e6eb.jpg)  
Fig. 5. Diagram of a formal generic argument.

## 4.4. Linked and convergent reasoning

One of the significant features of a complete generic argument is that it captures all claims that are relevant to making an inference about the target claim of an inference slot. Therefore, for a complete generic argument, the only path into a claim is through the inference slot of its generic argument. This requires the inference slot to be able to represent the different ways in which inferences to the target claim can be made. The operators of this inference slot then need to deliver reasoning that may be linked or convergent. Walton [53] discusses in detail the distinction between linked arguments (where the premises work cooperatively and both are needed, see Fig. 6(a)) and convergent arguments (where the premises work independently, see Fig. 6(b)) and strongly puts the case that there is a third option when it is not known whether the argument is linked or convergent. He considers it a serious problem with the conventional method of argument diagramming that the third option cannot be represented. He suggests that the way out of this, in cases where the evidence is incomplete to judge an argument as linked or convergent, is through the use of digraphs and numbering the arrows leading to a common point. In

![](/api/attachments/TBV88FY2/fulltext/images/588ecf73595109cf67680766944ea297ad469274b59c70ba935feefb9f8ce2d2.jpg)  
Fig. 6. Argument diagrams.

Fig. 6, the two arrows into Z having the same numbers would indicate that both steps are part of the same inference (linked). In contrast, in Fig. 6(c), the two arrows have different numbers and would indicate two separate steps of inference making the reasoning convergent.

For example, in representing the top level of reasoning in refugee law, a determination has to be made on the basis of whether the tribunal has jurisdiction, whether or not the applicant is excluded from refugee status on the basis of the UN Convention and whether or not the applicant has a well founded fear of persecution. The application of this reasoning proceeds by first considering if the tribunal has jurisdiction in the matter, then whether the applicant is excluded and then the case for well founded fear is considered. This reasoning is most usually represented by the more procedural nature of a decision tree. The representation as a generic argument puts aside the considerations of procedural order and questions of whether the inferences are linked or convergent in its top level structural representation. That is, the three considerations as claims are the input claim nodes to the single inference slot of this generic argument.

It is at the stage of constructing the operator/ justification pairs that form the inference slot that the linked/convergent distinction may need to be resolved. If we consider the example of refugee determination above more carefully, then we observe that if the value of the jurisdiction variable is <sup>d</sup>has (jurisdiction)<sup>T</sup> and the value of the exclusion variable is <sup>d</sup>not (excluded)<sup>T</sup> then the determination depends on the <sup>d</sup>well founded fear of persecution<sup>T</sup> variable. So the three factors, with these values are linked in making an inference about the <sup>d</sup>determination<sup>T</sup> variable. However, if either of the <sup>d</sup>jurisdiction<sup>T</sup> or <sup>d</sup>exclusion<sup>T</sup> variables has the value <sup>d</sup>no<sup>T</sup>, then the values of the <sup>d</sup>well founded fear of persecution<sup>T</sup> variable are not linked into the consideration.

Returning to our example of Reff in Section 2, the actual argument that Reff has a well founded fear of persecution can be represented in the software Araucaria by Chris Reed and Glenn Rowe [43] as a linked argument as shown in Fig. 7. Indeed the actual argument for Anju would also be represented as a linked argument.

Arguments for <sup>d</sup>well founded fear of persecution<sup>T</sup>, according to the UN convention may be made on grounds of persecution due to race, religion, nationality, political opinion and social group. It is possible that severity values of incidents of persecution due to race and the severity values of incidents of persecution due to political opinion combine to provide a linked inference about the <sup>d</sup>yes<sup>T</sup> value of well founded fear. However, each of the incidents independently may have been severe enough to provide independent arguments for a <sup>d</sup>yes<sup>T</sup> value on <sup>d</sup>well founded fear of persecution<sup>T</sup>. In this case, the inference would be convergent.

![](/api/attachments/TBV88FY2/fulltext/images/188e0d912fae3a90f161bc1f7bbe8a6f8e233b7b058a7870d2bdad2590c4d130.jpg)  
Fig. 7. Araucaria representation of Reff actual argument as a linked argument.

Prior knowledge about the linked/convergent nature of an inference can be useful in the construction of an inference operator. In cases where the nature is not clear, it can be investigated after construction of the operator by consideration of the values and how they are assigned. However, it is worth noting that the GAAM allows the setting out of reasoning in a GAS and permits the linked/convergent distinction to be made later at the level of individual inference values.

In the case of an operator that is simply a support for human reasoning, the justification variable can be used to provide information on the order of considering factors in a human inference process.

## 5. Formal characteristics of the GAAM

## 5.1. Syntax and deducibility

The propositions of a GAS for a domain modelled by the GAAM are the claims that can be formed within claim slots. So, this is the finite set of expressions of the form $C _ { \mathrm { p } } C _ { \mathrm { v k } } C _ { \mathrm { s } }$ . All logical connectives, if needed, are encoded in the inference procedures of inference slots. Propositions can only be combined if they occur together attached to inward arcs of the same inference slot. Their combination then has to be with any other claim slots that occur in the domain of this inference slot.

There is also a set of meta-propositions that fill out the reasoning but are not involved at the level of the calculus. These are reasons for relevance propositions, inference procedure justifications and claim value reasons. Their function is to allow the synthesis of reasoning in the case of human reasoning or the automatic construction of verbal reasoning that is human understandable when computational reasoning has been used. It is possible that a relevance calculus be developed that would permit gauging the importance of claims based on properties of the reasons for relevance; however, this is not considered here.

A proposition $C _ { \mathrm { p } } C _ { \mathrm { v k } } C _ { \mathrm { s } }$ is deducible if there is an instantiated subtree of the GAS with this claim as top level. By an instantiated subtree, we mean a choice of inference procedure from each inference slot and a selection of claim values at the leaf node level so that the application and composition of the inference procedures to the leaf level claim values leads to the proposition. Because each inference procedure is an operator (function), it is not possible to get different claims from the same data values with a single set of inference procedures. However, allowing different choices of inference procedures may permit the same data to derive different claims. In this sense, the model permits inconsistency and the inconsistencies can be identified and resolved. In Fig. 2, different claims are made by the tribunal member and Anju. These different claims are made on the basis of different data and different inference procedures but it would have been possible for them to agree on the data and reach different conclusions by differences in the inference procedures used: myRules and myHuman.

It can also be seen that we can have more than a single derivation of a proposition C from a set of propositions C. For example, $I _ { j } ^ { 1 } ( I _ { k } ^ { 2 } ( { \cal T } ) )$ may be one derivation and $I _ { l } ^ { 1 } ( I _ { m } ^ { 2 } ( T ) )$ another. Here, we are assuming that the proposition can be obtained by the composition of just two inference procedures

$$
\Gamma \colon \xrightarrow {I _ {k} ^ {2}} C _ {t} \xrightarrow {I _ {m} ^ {l}} C
$$

where $I _ { k } ^ { 2 }$ is an inference procedure from the slot $I ^ { 2 }$ and $I _ { m } ^ { 1 }$ is an inference procedure from the slot $I ^ { 1 }$ .

## 5.2. Deducibility

The methods for deducing (reasoning towards) a proposition C from a set of propositions C are presented above. Now, given a proposition $C _ { \mathrm { p } } C _ { \mathrm { v k } } C _ { \mathrm { s } }$ and asked to decide whether it can be proved (reasoned towards) from C becomes a search problem which is best done by proceeding forward from C to the claim slot C associated with $C _ { \mathrm { p } } C _ { \mathrm { v k } } C _ { \mathrm { s } } .$ This is reachable in a finite number of compositions and each inference slot along the way has only a finite number of inference procedures to check, each acting on a finite set of values. It is then simply a matter of checking whether any of the paths yields the value $C _ { \mathrm { v k } }$ . In fact, all distinct arguments that yield $C _ { \mathrm { p } } C _ { \mathrm { v k } } C _ { \mathrm { s } }$ will be returned.

## 5.3. Argument strength and validity

So far, the focus has been on the syntactic aspects of the GAAM. It is clear what constitutes a proposition and how they can be acted on by inference procedures to produce new propositions. At the syntactic level, each inference procedure is internally consistent but the use of different inference procedures may produce inconsistent results. The usual approach is now to consider the semantics of the model. One approach to semantics is to use truth tables, whereby any proposition in the system is assigned a truth value. Another approach is to use model theory where meaning is attached to propositions in terms of possible interpretations of the propositions. Krause et al. [28] use a different approach from the Tarskian approach by ascribing a meaning to the proofs in their logic of argumentation (LA) and not to the propositions themselves. As arguments are what makes LA different from other logics, they in fact ascribe meaning to the arguments in LA. They develop a proof theoretic semantics of LA which is expressed using category theory. Ambler [2] achieves this by using the Curry-Howard isomorphism, which relates the proofs of minimal logic to terms of a simply typed k-calculus and hence to the arrows of a free cartesian closed category which can be viewed as a deductive system. The notion of a category of arguments that can be viewed as a system of uncertain inference is developed by providing a general theory of the strength of an argument in all such categories. This allows the accumulation or aggregation of distinct arguments for the same proposition. This definition of the strength of an argument is achieved in terms of a confidence measure on an evidential closed category.

In the standard model theoretic approach, there is concern that each inference rule is sound and complete. These notions depend on the notion of C logically following from a set of propositions C. This simply means that C is true for every interpretation where C is true.

This requirement (logically following) is too strong for the generic argument structures developed by the GAAM. The derivation of inconsistent propositions from the same data C is permitted and so there will be some interpretations in which C is true and some where CV is true. The only cases for which we might expect that propositions logically follow in the GAAM is for inference slots where there is a unique inference operator. In this case, the discursive community has decided that all arguments from C and context variable values CVV can be effectively reasoned about in a single way. Whilst this is an appeal to a single syntactic mechanism, it also means that the validity of the proposition must be strong.

We take an approach that is closer to that taken by Krause et al. [28] with LA. They go to some length to establish a confidence measure on their evidential closed category of propositions and arguments between them. Considering a semantics for the GAAM is interesting. First, we note that there may be a number of arguments that lead to a given proposition. So, one possible view of the validity of a proposition may take account of this by aggregating these arguments. The rationale for this approach would be that the truth of a proposition should reflect something of the ways that it can be established. Given that the GAAM has associated with each GAS a discursive community and the inference procedures reflect the agreed ways of reasoning within that community it makes some sense to give more credibility to a proposition that is supported by many arguments than one that is only supported by a few. <sup>d</sup>Just because there are more roads leading to Rome, doesn’t make Rome better to go to than Florence—but somehow it does<sup>T</sup>. The GAAM as a model, prescribes by agreement of the discursive community, the structure of the reasoning in a domain as well as the variety of permissible inference procedures in each inference slot. The specification of a set of inference procedures in an inference slot permits a notion of strength to be defined which is based on an aggregation of similar arguments. This is similar to the approach taken by Krause et al. [28].

Consider a single actual argument A which can be represented as a set of propositions (actually each proposition in C specifies a value) C mapped to a claim value $C _ { \mathrm { v } }$ by an inference procedure $I _ { j } .$ This actual argument is instantiated from a generic argument with inference slot I. Let I contain a set of inference procedures $\{ I _ { i } | i { = } 1 . . . k \}$ . We may define the strength of A as

$$
\begin{array}{c} s _ {\Gamma , \mathrm{C}} (\mathcal {A}) = \frac {| \left\{I _ {i} | I _ {i} (\varGamma) = I _ {j} (\varGamma) \wedge i = 1 \dots k \right\} |}{k} \\ = \frac {\text { number   of   agreements }}{k} \end{array}
$$

where $I _ { j }$ is the inference procedure used in A.

Note that from this definition of strength we have the following. If there is a unique inference procedure in the inference slot (k=1), then the strength of any argument based on this slot is 1 and this corresponds to a situation of having no alternative ways of reasoning and total agreement on the values inferred from the reason values given. Furthermore, the strength of all arguments based on the generic argument corresponding to this slot is the same. The formula defines the strength of an actual argument and not the strength of an inference procedure although the strength of an inference procedure may now be defined as a function on the various sets of propositions C in its domain using the above.

The above approach simply counts the arguments in support. It could be called the inference agreement approach. It can be augmented by the certainty values for those inference operators that generate the claim of A. One way of doing this would be to weight the effect of each contributing inference operator by the certainty factor that it gives to the claim of A.

$$
s _ {\Gamma , C} (\mathcal {A}) = \frac {\sum_ {\{i | I _ {i} (\Gamma) = I _ {j} (\Gamma) \wedge i = 1 . . . k \}} c _ {i}}{\sum_ {i = 1 . . . k} c _ {i}}
$$

where $c _ { i }$ is the certainty associated with the inference operator $I _ { i }$ in slot I. The weighting means that arguments in which a minority of inference operators support the claim but do so with high certainty would count as much as having some support from many.

There are other possible approaches and we mention two others here. It is possible within the model to consult the extent to which a particular claim is supported by past actual arguments and then assign strength to an actual argument on the basis of support from these arguments. This approach might be called the data agreement approach. In the last approach, we recognize that each inference operator within an inference slot is supported by a reason. The weighted formula above could further be modified by a factor representing the strength of the reason for the inference procedure. For example, in law, an inference procedure may derive from the latest most on point precedent yet not fully accepted by the community. In this case, the older inference procedures may not be yet deleted. The new inference procedure ought to be the strongest but it will not be on data agreement and probably not on number or weighted number agreement.

The approaches considered above all adopt a formulation of the strength of an argument from within the GAS. Another set of approaches could be categorized as taking evidence for the strength of an argument from within the discursive community attached to the GAS. For example, the evidence of the strength of an argument from within the discursive community could be based on the number of members of the community that advance the claim of argument A. Another approach would be to consider the authority of each member advancing that claim.

The approach to the formulation and view of strength of an argument is connected to the nature of the discursive community. For example, in the scientific community, an argument’s strength would be based more on the number of methodologies that support it rather than the number of individual’s (actual arguments) that support it. This would therefore correspond to the inference agreement approach. On the other hand, a group of medical experts may choose to deviate from the established ways of reasoning and act based on a number of them agreeing to the same line of action. This would be an approach based on a notion of strength outside the GAS and based more in the discursive community.

## 5.4. Comparing arguments—classes of arguments

In considering the validity and strength of arguments, we are able to give a measure of confidence to any atomic actual argument. In the case of actual arguments that are not atomic, we can specify the strength of the compound argument as the product of the atomic arguments which compose it. Notice that different arguments can be obtained by using different inference procedures in each slot and the strengths of the resulting arguments to the same conclusion may be different. It would therefore be possible to computationally define the strength of a non-atomic argument as the average of the strength of all arguments from the same data to the same claim and this could be based on any of the formulae considered in Section 5.3. In the case of not using certainty values, then it may be appropriate to simply have a binary weighting of strength indicating classes as either <sup>b</sup>weak<sup>Q</sup> or <sup>b</sup>strong<sup>Q</sup> based on a cutoff value for the numerical value of strength.

In the case of the actual argument of Anju (Fig. 2 on well founded fear) and the conflicting argument of the tribunal member, it is easy to identify that they make a conclusion on <sup>d</sup>well founded fear<sup>T</sup> based on different data but also by using different inference procedures. For example, the different claim for whether <sup>d</sup>the incidents taken together constitute persecution<sup>T</sup> highlight attention for the argument towards this claim slot and some focus on the strength of each of these arguments. The strength of the well founded fear argument may also depend on the community acceptability of the inference procedure used.

The GAAM does not specify how the certainty values for each proposition are combined for any inference procedure in an inference slot. Therefore, the GAAM leaves open the way in which inferences are made within each inference slot and the way in which certainty values are obtained. This can be elaborated at the level of the inference procedures themselves.

## 6. Other approaches

Our work here has focused on the use of argumentation to structure reasoning (i.e. a nondialectical emphasis) rather than on the use of argumentation to model discourse (i.e. a dialectical emphasis). Argumentation has usually been associated with defeasible reasoning and many have approached defeasible reasoning from the point of view of developing formal logics. For example, Nute [34] describes defeasible reasoning as:

When some new fact causes us to reject a prior conclusion, we will say that the conclusion together with the reasoning that gave rise to it are defeated. Any bit of reasoning that could in principle be defeated by further information we will call defeasible reasoning.

Two methods that have been most often used to capture defeasible reasoning are probabilistic reasoning and approaches that require the explicit listing of all exceptions as conditions for a rule. Nute argues that neither of these approaches provides a natural representation of many simple patterns of defeasible reasoning. He reviews other approaches by Glymour and Thomason [23] (which rejects conditionals as new evidence is discovered—order of antecedent dependent); Reiter’s default logic (1980) also cannot handle the example of Nute (here order of antecedents is not important but the order in which the rules are applied makes a difference). McDermott and Doyle [33] develop what they call nonmonotonic logic and do not allow a choice of the order of rule application— they propose instead that only those conclusions that show up regardless of the order of rule application should be accepted. Nute develops the defeasible logic system LDR with absolute rules, defeasible rules and defeaters. The usual way to explain meaning in formal semantics is by giving truth conditions. That is, a sentence is understood when we know what circumstances would make it true and what circumstances would make it false. Nute uses another approach to thinking about the meaning of a defeasible rule. This approach suggests that we understand a rule when we know how to follow it or comply with it. Therefore, instead of truth conditions, we can explain what a rule means by specifying compliance conditions for it. So rules of LDR can be thought of as policies for belief revision.

In the GAAM, defeasible reasoning is captured as actual arguments which differ in their claim values. Whilst operations such as attack and rebut are not modelled explicitly, it is easy to identify differences in the actual arguments for the purposes of comparison. Accepting that one argument defeats another could be based on strength as discussed in Section 5.3. Sometimes, a new defeating argument will require a revision of the GAS by the introduction of a new data item and inference procedure.

Hua and Kimbrough [26] describe the development of a hypermedia based argumentation decision support system (HADSS) based on logic graphs and sweeping presumptions. Formal logic can be thought of as providing a computational and normative theory of argument. As might be expected of any effort in formalization, there are problems of limitations in scope. These limitations mean that formal logical languages still fall well short of the requirements of everyday practical deliberation. Formal logics have a second serious problem in that it is simply not reasonable to expect users to have a meaningful understanding of formalized expressions. These problems have led to the study of informal logics. Any HADSS would have two broad categories of hypermedia links: links between elements of the argumentation network (internal links) and links to the elements outside the network (external links). An external link might be used to display corroborating documents, videos and so on for the assertion of tha node. These systems should facilitate interactive ad hoc construction and modification of arguments and provide hypertext style access to documents relevant to particular arguments. An example of such a system is gIBIS [15]. The most salient limitation of the gIBIS framework is that it is not a logic and does not support logical inference. Hua and Kimbrough also carried out experiments, which indicate that the logic graph representation method is a useful tool for helping people in deductive reasoning. The graphical representation of conditional statements allows inductive reasoning processes to be simply represented as graph traversal. These experiments may provide some indirect support for using the GAAM to help participants in a discussion structure their reasoning.

Bart Verheij’s ArguMed [50] is an argument assistance system based on the defeasible logic DEFLOG. The ArguMed system uses the notion of a warranted dialectical argument. A dialectical argument is one in which counter-arguments (based on undercutting exceptions) are incorporated. The system allows warrants, both for argument steps (the reasons that support conclusions) and for undercutters (for the exceptions that block the connections between a reason and the conclusion). Step warrants express that a particular statement can be adduced as a reason for another statement. Undercutter warrants express that a particular statement provides an exception that breaks the connection between a reason and conclusion. Whether a dialectical argument justifies its conclusion depends on the structure of the argument, that is, on the reasons, conclusions, exceptions and warrants that occur in it, and on the way they are related. The system automatically determines the justification status of an argument. The notions of reason, conclusion, step warrant and reason for a step warrant are respectively similar to the GAAM’s notions of data item, claim, inference and reason for inference procedure. The exceptions, like the Toulmin rebuttal make the argumentation defeasible. The undercutter warrants have no counterpart in Toulmin’s scheme but would correspond to an inference to a contrary claim at the actual argument level in the GAAM. Toulmin does not give an explicit characterisation of the justification status of statements and the GAAM does not necessarily attempt to do this in an absolute sense but relative to the norm of the group’s GAS. This approach is much more explicit for dialectic ends and is free in terms of adducing reasons (backwards) or inferring conclusions (forwards) but is not as explicit in structuring reasoning. In the GAAM, adduction takes place at the first stage when the group establishes the structure, then individual inferences to conclusions can proceed subsequently within the structure.

Dialectical approaches typically automate the construction of an argument and counter arguments normally with the use of a non-monotonic logic. Raghu et al. [39] have developed and analysed a connectionist framework for systems support for dialectical argumentative processes in collaborative decision making. This is a different approach from those mentioned earlier. Collaborative decisions in most organisations typically arise from either formal or informal deliberations in groups, where the group members consider and debate various possible decision options. These decision problems tend to be highly unstructured and are therefore difficult to model. Consequently, such decision issues are resolved through discussions, where argumentative logic and persuasive presentation are critical. In general, the discussion process involves both strict and defeasible reasoning. Strict reasoning is structurally coherent and logically consistent, and is thus not open to argumentation; defeasible reasoning includes structures of logic that are open to argumentation.

Defeasible reasoning arises due to perceptual differences among individuals about claims that lack a strong support base in terms of evidential data or strict reasoning. The resolution of the differences hinges on strengthening the support base and/or persuasive presentation. They develop a systematic framework for argument representation in modelling collaborative discussions. Secondly, they develop a connectionist architecture using their representational formalisms for argument analyses during the course of a discussion. Thirdly, the ideas are illustrated through connectionist models of practical discussions drawn from the published case study literature.

They define an argument structure as a simple set of assertions. Assertions can be of two types: positions or inferences. A statement of position is a claim. A statement of inference is a structural relationship among a set of positions and facts. Assertions are built up from a language, which is a triple S, R, Q, where S constitutes the sentences, R is a set of assertions built using sentences and Q is a set of assertion qualifications. A connectionist network formalism is used to model the debate or discussion. The connectionist network is defined as a four-tuple with nodes, an activation function, a set of arcs and a set of weights. The network contains nodes which represent claims and arcs, which represent strict or defeasible support. The computational model accounts for actual power of reasoning support versus opposition, the activation levels of feasible units, as well as the simplicity of an argument. The cases analysed indicate that the computational model provides insight into the strength of support for various arguments. This approach does not provide a logic based on analysis, leading to discrete valued assessments of arguments as either winning or losing. However, logical analysis of arguments surrounding business decisions most often leads to inferences that are inconclusive or undetermined. In contrast to the logic based argument and analysis, the connectionist approach provides the means to assess the relative strengths of arguments in the discussion.

As mentioned before, the GAAM does not try to represent the dynamics of group decision making or dialogue. However, an individual GAS is a consensus representation of the structure of decision making within a domain. The connectionist model presented above by Raghu et al. may be a useful approach for developing the generic arguments with the domain. The next stage of our work will be to develop a full dialectical model based on the non-dialectical GAAM. The models that we have considered and most argumentation models tend to focus on the dialectic. They use propositions as their underlying nondialectical model. This provides significant freedom but the use of GAAM structured propositions, we believe will realize other advantages in a dialectical model. It is important to appreciate that at this stage the GAAM is connected to a discursive community in that, the community constructs a GAS for a domain of discourse. However, without the full dialectical model, it does not permit the group to use the model for dialectical exchanges.

There are some similarities between the argument trees of the GAAM and conventional decision trees. Decision trees are rooted, usually binary trees, with simple classifiers placed at each internal node and a classification at each leaf. The outputs of the simple classifiers at the nodes determine a unique path from the root to a leaf of the decision tree. This path is known as the evaluation path. The classification associated with an object is the leaf reached by the evaluation path. Typically, the simple classifier at an internal node compares one of the input attributes against a threshold. The main difference is in the level of complexity. In a decision tree, there would need to be at least one decision node for each possible value of a node in the GAS. This means, that a GAS serves as a more compact representation of reasoning within the domain.

## 7. Conclusion

In this paper, we have described the generic/actual argument model. The model derives exibility and power from: nodes whose generality is efficient in capturing many instance arguments that essentially have the same structure: a clear layout of the structure of reasoning, a clear delineation of inferences, capturing dialectical positions within a common structure. We have:

<sup>!</sup> identified its basic set of propositions and how they are combined

<sup>!</sup> identified the elements that formally control or represent the structure of reasoning

<sup>!</sup> set out its reasoning mechanisms and how propositions are derived

<sup>!</sup> discussed the extent to which derived propositions are valid and accepted as well as explored notions of argument strength that may suit different groups

<sup>!</sup> set out the way in which the model supports discretion

<sup>!</sup> clarified the boundaries of the non-dialectical model in supporting individual decision making as distinct from group decision making

<sup>!</sup> discussed how the model supports the identification of points of similarity and difference in reasoning and is not altogether focussed on defeat of another argument.

We have also noted that, although it is Toulmin based, it is quite different in its approach to modelling reasoning from other argument based models. The salient features of the approach are its connection to a discursive community, its mechanism for dealing with inconsistencies and its two levels of abstraction. The development of the complete dialectical model based on the GAAM is underway and this will provide a closer connection to the discursive community.

## Acknowledgement

This research was supported by the Australian Research Council.

## References

[1] Faezi Afshar, John Yearwood, Andrew Stranieri, Capturing consensus knowledge from multiple experts, in: Max Bramer (Ed.), Research and Development in Intelligent Systems XIX, Springer-Verlag, London, 2002.

[2] Simon Ambler, A categorical approach to the semantics of argumentation, Mathematical Structures in Computer Science 6 (1996) 167 – 188.

[3] Aristotle, The Works of Aristotle, i. logic, translated by W. A. Pickard-Cambridge, chapter Topica, Oxford, 1928, p. 100.

[4] John Avery, John Yearwood, Andrew Stranieri, An argumentation based multi-agent system for etourism dialogue, in: A. Abraham, M. Koeppen (Eds.), Hybrid Information Systems, Physica-Verlag, Heidelberg, 2002, pp. 497 – 512.

[5] W.J. Ball, Using virgil to analyse public policy arguments: a system based on Toulmin’s informal logic, Social Science Computer Review 12 (1) (1994 Spring) 26 – 37.

[6] M.D. Bayles, Procedural Justice. Allocating to Individuals, Kluwer, Dordrecht, 1990.

[7] Trevor J.M. Bench-Capon, D. Lowes, A.M. McEnery, Argument-based explanation of logic programs, Knowledge Based Systems 4 (3) (1991 September) 177– 183.

[8] Karl L. Branting, A computational model of ratio decidendi, Artificial Intelligence and Law: An International Journal 2 (1994) 1 – 31.

[9] L. Karl Branting, Reasoning with Rules and Precedents—A Computational Model of Legal Analysis, Kluwer Academic Publishers, Dordrecht, 2000.

[10] B.G. Buchanan, E.H. Shortliffe (Eds.), Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project, Addison Wesley Publishing, Reading, MA, 1984.

[11] D. Carbogim, D. Robertson, J. Lee, Argument-based applications to knowledge engineering, Knowledge Engineering Review 15 (2) (2000) 119–149.

[12] G.C. Christie, An essay on discretion, Duke Law Journal (1986) 747 – 778.

[13] P. Clark, A model of argumentation and its application in a cooperative expert system, PhD thesis, Turing Institute. Department of Computer Science. University of Strathclyde, Glasgow 1991.

[14] P. Cohen, Heuristic Reasoning About Uncertainty: An Artificial Intelligence Approach, Pitman, London, 1985.

[15] Jeff Conklin, Michael L. Begeman, gIBIS: a hypertext tool for exploratory policy discussion, ACM Transactions on Office Information Systems 6 (4) (1988 October) 303– 331.

[16] Judith P. Dick, Conceptual retrieval and case law, Proceedings of the First International Conference on Artificial Intelligence and Law, ACM Press, 1987, pp. 106– 115.

[17] Judith P. Dick. A conceptual, case-relation representation of text for intelligent retrieval, PhD thesis, Department of Computer Science, University of Toronto, 1991.

[18] Phan Minh Dung, On the acceptability of arguments and its fundamental role in non-monotonic reasoning, logic programming and n-person games, Artificial Intelligence 77 (2) (1995) 321– 357.

[19] K. Engisch, Logische Studien zur Gesetzesanwendung, 2nd ed., Heidelberg Press, 1960.

[20] A.M. Farley, K. Freeman, Burden of proof in legal argumentation, Proceedings of the Fifth International Conference on Artificial Intelligence and Law, ACM Press, 1995, May 21–24, pp. 156– 164.

[21] John Fox, Knowledge, decision making and uncertainty, in: A. Gale (Ed.), Artificial Intelligence and Statistics, Addison-Wesley, Reading, MA, 1986.

[22] John Fox, Simon Parsons, Arguing about beliefs and actions, in: A. Hunter, S. Parsons (Eds.), Applications of Uncertainty Formalisms, Springer, Berlin, 1998, pp. 266 – 302.

[23] Clark Glymour, Richmond Thomason, Default reasoning and the logic of theory perturbation, Proceedings of the AAAI Workshop on Nonmonotonic Reasoning, 1984, pp. 17 – 19.

[24] T.F. Gordon, The pleadings game: an exercise in computational dialectics, Artificial Intelligence and Law 2 (4) (1995) 239 – 292.

[25] Thomas F. Gordon, Nikos I. Karacapilidis, The Zeno argumentation framework, Proceedings of the Sixth International Conference on Artificial Intelligence and Law, ACM Press, 1997, pp. 10 – 18.

[26] Gary H. Hua, Stephen O. Kimbrough, On hypermedia-based argumentation decision support systems, Decision Support Systems 22 (1988) 259 – 275.

[27] P.E. Johnson, I.A. Zualkernan, D. Tukey, Types of expertise: an invariant of problem solving, International Journal of Man Machine Studies 39 (1993) 641– 652.

[28] P.J. Krause, S. Ambler, M. Elvang-Goransson, J. Fox, A logic of argumentation for reasoning under uncertainty, Computational Intelligence 11 (1) (1995) 113 – 131.

[29] J. Ron Loui, J. Norman, D. Altepeter, D. Pinkard, J. Craven, M. Lindsay, Progress in room 5: a testbed for public interactive semi-formal legal argumentation, Proceedings of the Sixth International Conference on Artificial Intelligence and Law, ACM Press, New York, 1997, pp. 207 – 214.

[30] Neil MacCormick, Legal Reasoning and Legal Theory, Oxford University Press, Oxford, 1978.

[31] C.C. Marshall, Representing the structure of legal argument, Proceedings of the Second International Conference on Artificial Intelligence and Law, ACM Press, USA, 1989, pp. 121 – 127.

[32] L. Matthijssen, Interfacing between Lawyers and Computers. An architecture for Knowledge Based Interfaces to Legal Databases, Kluwer Law International, The Netherlands, 1999.

[33] Drew McDermott, Jon Doyle, Non-monotonic logic, Artificial Intelligence 13 (1980) 41–72.

[34] Donald Nute, Defeasible reasoning and decision support systems, Decision Support Systems 4 (1988) 97 – 110.

[35] D.L. Poole, A logical framework for default reasoning, Artificial Intelligence 36 (1988) 27 – 47.

[36] H. Prakken, Logical tools for modelling legal argument. PhD thesis, Vrije University, Amsterdam, The Netherlands, 1993.

[37] Henry Prakken, A logical framework for modelling legal argument, Proceedings of the Fourth International Conference on Artificial Intelligence and Law, ACM Press, New York, 1993, pp. 1 –9.

[38] Henry Prakken, Giovanni Sartor, A dialectical model of assessing conicting arguments in legal reasoning, Artificial Intelligence and Law 4 (1996) 331 – 368.

[39] T.S. Raghu, R. Ramesh, Ai-Mei Chang, Andrew B. Whinston, Collaborative decision making: a connectionist paradigms for dialectical support, Information Systems Research 12 (4) (2001) 363 – 383.

[40] Joseph Raz, Practical Reason and Norms, 2nd ed., Oxford University Press, 1990.

[41] H.W.J. Rittel, M.W. Webber, Dilemmas in a general theory of planning, Policy Sciences 4 (1973) 155–169.

[42] Christian Robert, The Bayesian Choice, Springer Verlag, 2001.

[43] G.W.A. Rowe, C.A. Reed, J. Katzav, Araucaria: marking up argument, Working Notes of the European Conference on Computing and Philosophy, 2003.

[44] A. Stranieri, J. Zeleznikow, M. Gawler, B. Lewis, A hybrid rule-neural approach for the automation of legal reasoning in the discretionary domain of family law in Australia, Artificial Intelligence and Law 7 (2–3) (1999) 153– 183.

[45] A. Stranieri, J. Yearwood, T. Meikle, The dependency of discretion and consistency on knowledge representation, International Review of Law Computers & Technology 14 (3) (2000) 325– 340.

[46] Andrew Stranieri, John Zeleznikow, Copyright regulation with argumentation agents, Information and Communications Technology Law 10 (1) (2001) 123– 137.

[47] Andrew Stranieri, John Zeleznikow, Webshell: the development of web based expert system shells, Research and Development in Expert Systems XVIII. Proceedings of ES2001—The Twenty-first SGES International Conference on Knowledge Based Systems and Applied Artificial Intelligence, Springer-Verlag, London, 2001, pp. 245 – 258.

[48] Stephen Toulmin, The Uses of Argument, Cambridge University Press, Cambridge, 1958.

[49] T.A. van Dijk, Relevance in logic and grammar, in: J. Norman, R. Sylvan (Eds.), Directions in Relevant Logic, Kluwer Academic Publishers, Dordrecht, 1989, pp. 25 – 57.

[50] Bart Verheij, Automated argument assistance for lawyers, ProceedingsoftheSeventhInternationalConferenceonArtificial Intelligence and Law, ICAIL’99, 1999, June 14–18, pp. 43 – 52.

[51] G. Vreeswijk, Defeasible dialectics: a controversy-oriented approach towards defeasible argumentation, Journal of Logic and Computation 3 (3) (1993) 3 – 27.

[52] F. Waismann, Verifiability, in: A. Flew (Ed.), Logic and Language, Blackwell, 1951.

[53] Douglas N. Walton, Argument structure: a pragmatic theory, Toronto Studies in Philosophy, University of Toronto Press, Toronto, 1996.

[54] J. Yearwood, A. Stranieri, Integration of retrieval, reasoning and drafting for refugee law: a third generation legal knowledge based system, Proceedings of Seventh International Conference on Artificial Intelligence and Law, ICAIL’99, 1999, June 14–18, pp. 117–125.

[55] John Yearwood, Andrew Stranieri, An argumentation shell for supporting the development and drafting of legal documents, Information and Communications Technology Law 11 (1) (2002).

[56] John Yearwood, Andrew Stranieri, John Avery, Negotiation and argumentation based agents to facilitate ecommerce, Proceedings of the International Conference on Advances in Infrastructure for Electronic Business, Science and Education on the Internet, SSGRR2001, 2001, pp. 100 – 109.

[57] John Zeleznikow, Andrew Stranieri, The split up system: integrating neural networks and rule based reasoning in the legal domain, Proceedings of the Fifth International Conference on Artificial Intelligence and Law. ICAIL’95, ACM Press, New York, 1995, pp. 185– 194.
